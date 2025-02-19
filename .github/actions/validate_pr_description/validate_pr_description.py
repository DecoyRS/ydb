import sys
import re
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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: validate_pr_description.py <path_to_pr_description_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    is_valid, txt = validate_pr_description_from_file(file_path)
    from post_status_to_github import post
    post(is_valid, txt)
    if not is_valid:
        sys.exit(1)