import sys
import re
import datetime
import os
import json
from github import Github, Auth as GithubAuth
from github.PullRequest import PullRequest
from typing import Tuple

issue_patterns = [
    r"https://github.com/ydb-platform/ydb/issues/\d+",
    r"https://st.yandex-team.ru/[a-zA-Z]+-\d+"
]
def validate_pr_description(description, is_not_for_cl_valid=True) -> bool:
    result, _  = check_pr_description(description, is_not_for_cl_valid)
    return result

def check_pr_description(description, is_not_for_cl_valid=True) -> Tuple[bool, str]:
    try:
        if not description.strip():
            txt = "PR description is empty. Please fill it out."
            print(f"::warning::{txt}")
            return False, txt

        if "### Changelog category" not in description and "### Changelog entry" not in description:
            return is_not_for_cl_valid, "Changelog category and entry sections are not found."

        # Extract changelog category section
        category_section = re.search(r"### Changelog category.*?\n(.*?)(\n###|$)", description, re.DOTALL)
        if not category_section:
            txt = "Changelog category section not found."
            print(f"::warning::{txt}")
            return False, txt

        categories = [line.strip('* ').strip() for line in category_section.group(1).splitlines() if line.strip()]

        if len(categories) != 1:
            txt = "Only one category can be selected at a time."
            print(f"::warning::{txt}")
            return False, txt

        category = categories[0]
        for_cl_categories = [
            "New feature",
            "Experimental feature",
            "User Interface",
            # "Improvement", # Obsolete category
            "Performance improvement",
            "Bugfix",
            "Backward incompatible change"
        ]

        not_for_cl_categories = [
            "Documentation (changelog entry is not required)",
            "Not for changelog (changelog entry is not required)"
        ]
        
        valid_categories = for_cl_categories + not_for_cl_categories

        if not any(cat.startswith(category) for cat in valid_categories):
            txt = f"Invalid Changelog category: {category}"
            print(f"::warning::{txt}")
            return False, txt

        if not is_not_for_cl_valid and any(cat.startswith(category) for cat in not_for_cl_categories):
            txt = f"Category is not for changelog: {category}"
            print(f"::notice::{txt}")
            return False, txt

        if not any(cat.startswith(category) for cat in not_for_cl_categories):
            entry_section = re.search(r"### Changelog entry.*?\n(.*?)(\n###|$)", description, re.DOTALL)
            if not entry_section or len(entry_section.group(1).strip()) < 20:
                txt = "The changelog entry is less than 20 characters or missing."
                print(f"::warning::{txt}")
                return False, txt

            if category == "Bugfix":
                def check_issue_pattern(issue_pattern):
                    return re.search(issue_pattern, description)

                if not any(check_issue_pattern(issue_pattern) for issue_pattern in issue_patterns):
                    txt = "Bugfix requires a linked issue in the changelog entry"
                    print(f"::warning::{txt}")
                    return False, txt

        print("PR description is valid.")
        return True, "PR description is valid."

    except Exception as e:
        txt = f"Error during validation: {e}"
        print(f"::error::{txt}")
        return False, txt

def validate_pr_description_from_file(file_path) -> Tuple[bool, str]:
    try:
        with open(file_path, 'r') as file:
            description = file.read()
        return check_pr_description(description)
    except Exception as e:
        txt = f"Failed to validate PR description: {e}"
        print(f"::error::{txt}")
        return False, txt
    
def post_status_to_github(is_valid, error_description):
    gh = Github(auth=GithubAuth.Token(os.environ["GITHUB_TOKEN"]))

    with open(os.environ["GITHUB_EVENT_PATH"]) as fp:
        event = json.load(fp)

    pr = gh.create_from_raw_data(PullRequest, event["pull_request"])

    header = f"<!-- status pr={pr.number}, validate PR description status -->"

    body = comment = None
    for c in pr.get_issue_comments():
        if c.body.startswith(header):
            print(f"found comment id={c.id}")
            comment = c
            body = [c.body]

    if body is None:
        body = [header]

    status_to_header = {
        True: "Validation successful",
        False: "Validation failed"
    }

    color = "green" if is_valid else "red"
    indicator = f":{color}_circle:"
    timestamp_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    body.append(f"{indicator} `{timestamp_str}` {status_to_header[is_valid]}")

    if not is_valid:
        body += f"\n{error_description}"

    body = "\n".join(body)

    if comment:
        print(f"edit comment")
        comment.edit(body)
    else:
        print(f"post new comment")
        pr.create_issue_comment(body)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: validate_pr_description.py <path_to_pr_description_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    is_valid, txt = validate_pr_description_from_file(file_path)
    post_status_to_github(is_valid, txt)
    if not is_valid:
        sys.exit(1)