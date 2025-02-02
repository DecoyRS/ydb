## YDB release HEAD (9cb9dec87f5bac630075d63568accc93a792bafa) as compared to 44a1cd02b9d9f3e11eed6d02ac5fe4649e6f6dd7 (44a1cd02b9d)

### Backward incompatible change
* Remove time difference public api fields. [#6335](https://github.com/ydb-platform/ydb/pull/6335) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Few changes in grammar for better antlr4 backward compatibility. [#6713](https://github.com/ydb-platform/ydb/pull/6713) ([Orlov Pavel](https://github.com/OrlovPavel)).
* Change grammar for antlr4 backward compatibility. [#8186](https://github.com/ydb-platform/ydb/pull/8186) ([Orlov Pavel](https://github.com/OrlovPavel)).
* ... [#12637](https://github.com/ydb-platform/ydb/pull/12637) ([Alexey Efimov](https://github.com/adameat)).
* ... [#13274](https://github.com/ydb-platform/ydb/pull/13274) ([Alexey Efimov](https://github.com/adameat)).

### New feature
* Copy section `host_configs` into `config.yaml` configuration. [#3012](https://github.com/ydb-platform/ydb/pull/3012) ([Aleksei Kobzev](https://github.com/kobzonega)).
* Add reason for pending action in maintenance public API. [#3289](https://github.com/ydb-platform/ydb/pull/3289) ([Ilia Shakhov](https://github.com/pixcc)).
* Add `ydb scheme permissions {clear,set}-inheritance` commands. Add `ydbd db schema access {clear,set}-inheritance` commands. [#3776](https://github.com/ydb-platform/ydb/pull/3776) ([ijon](https://github.com/ijon)).
* Add Pack/Unpack method implementations to TTupleLayoutFallback class. [#4905](https://github.com/ydb-platform/ydb/pull/4905) ([Alexander](https://github.com/san-kir-k)).
* [issue](https://github.com/orgs/ydb-platform/projects/37?pane=issue&itemId=67157010) - Added oidc-proxy configuration parameters. This includes `auth-profile`, which determines the logic that oidc_proxy will follow. Possible options: `y-profile`, `n-profile`. Default is `y-profile` - For oidc_proxy handlers, added a new version of logic depending on `auth-profile`. The old handlers were not changed, so some logic is duplicated. I plan to combine some of the logic in a minor refactoring later. - For tokenator (mvp authentithication) added a new version of logic depending on `auth-profile` also. I plan to new version support for `meta` later. - Moved new iam spec to github into public api - Changed the endpoint names in tests to more neutral ones. [#6059](https://github.com/ydb-platform/ydb/pull/6059) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Ca factory in executer to support extra allocations and memory tracking everywhere. [#6084](https://github.com/ydb-platform/ydb/pull/6084) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Implemented HeapIterator for VDisk iterators. [#6136](https://github.com/ydb-platform/ydb/pull/6136) ([mregrock](https://github.com/mregrock)).
* Add feature flag enableimplicitqueryparametertypes to table service config to not restart database when feature flag is changed. [#6286](https://github.com/ydb-platform/ydb/pull/6286) ([VPolka](https://github.com/VPolka)).
* Add PG upgrade script. Add missing catalog/sql files from 14.2. [#6307](https://github.com/ydb-platform/ydb/pull/6307) ([Andrey Neporada](https://github.com/nepal)).
* Switch generate_kernels.py to python3. Regenerate kernels. [#6328](https://github.com/ydb-platform/ydb/pull/6328) ([Andrey Neporada](https://github.com/nepal)).
* Upgrade pg_wrapper to PostgreSQL 14.3. [#6334](https://github.com/ydb-platform/ydb/pull/6334) ([Andrey Neporada](https://github.com/nepal)).
* Upgrade pg_wrapper to PostgreSQL 14.5. [#6346](https://github.com/ydb-platform/ydb/pull/6346) ([Andrey Neporada](https://github.com/nepal)).
* Document copy_src.sh and PostgreSQL update process. [#6372](https://github.com/ydb-platform/ydb/pull/6372) ([Andrey Neporada](https://github.com/nepal)).
* Upgrade pg_wrapper to PostgreSQL 14.8. [#6373](https://github.com/ydb-platform/ydb/pull/6373) ([Andrey Neporada](https://github.com/nepal)).
* Hide deprecated operation kinds in `operation list`. [#6407](https://github.com/ydb-platform/ydb/pull/6407) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Create separate trace id for BlobStorage requests and link them to original traces. [#6444](https://github.com/ydb-platform/ydb/pull/6444) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Change default value to enable spilling. [#6462](https://github.com/ydb-platform/ydb/pull/6462) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Added request time info printing. [#6479](https://github.com/ydb-platform/ydb/pull/6479) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#6509](https://github.com/ydb-platform/ydb/pull/6509) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* Improve memory limits errors observability (add debugging details). [#6551](https://github.com/ydb-platform/ydb/pull/6551) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Move allocate resources call before actor launch from node service to factory. [#6583](https://github.com/ydb-platform/ydb/pull/6583) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Added benchmarks and implemented HeapIterator in code. [#6611](https://github.com/ydb-platform/ydb/pull/6611) ([mregrock](https://github.com/mregrock)).
* Use same on memory limit handler everywhere. [#6641](https://github.com/ydb-platform/ydb/pull/6641) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Fixed WM counters. [#6643](https://github.com/ydb-platform/ydb/pull/6643) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#6651](https://github.com/ydb-platform/ydb/pull/6651) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#6655](https://github.com/ydb-platform/ydb/pull/6655) ([Mars Agliullin](https://github.com/marsaly79)).
* Added CPU monitoring and yaml configs. [#6675](https://github.com/ydb-platform/ydb/pull/6675) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Added retries for CURLE_COULDNT_RESOLVE_HOST. [#6732](https://github.com/ydb-platform/ydb/pull/6732) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Add spilling nodes and pragma. [#6769](https://github.com/ydb-platform/ydb/pull/6769) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Randomize default spilling root. [#6781](https://github.com/ydb-platform/ydb/pull/6781) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* ... [#6784](https://github.com/ydb-platform/ydb/pull/6784) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#6791](https://github.com/ydb-platform/ydb/pull/6791) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* Added feature flag for resource pools on sls. [#6808](https://github.com/ydb-platform/ydb/pull/6808) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Allow enabling spilling for compute nodes. [#6895](https://github.com/ydb-platform/ydb/pull/6895) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* ... [#6916](https://github.com/ydb-platform/ydb/pull/6916) ([vporyadke](https://github.com/vporyadke)).
* Add queued time into query stats. [#6965](https://github.com/ydb-platform/ydb/pull/6965) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Periodically update node resource maximum to reflect as thread pool sizes changes. [#6967](https://github.com/ydb-platform/ydb/pull/6967) ([vporyadke](https://github.com/vporyadke)).
* ... [#7042](https://github.com/ydb-platform/ydb/pull/7042) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Refactor viewer backend closes [#6668](https://github.com/ydb-platform/ydb/issues/6668). [#7071](https://github.com/ydb-platform/ydb/pull/7071) ([Alexey Efimov](https://github.com/adameat)).
* Temporary files that are created during spilling now will be stored in /tmp/spilling-service-tmp/node_\<nodeId\>_\<guid\> and will be removed on next SpillingService run. [#7108](https://github.com/ydb-platform/ydb/pull/7108) ([Vladluk](https://github.com/vladl2802)).
* Added pools cache. [#7186](https://github.com/ydb-platform/ydb/pull/7186) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Improve node deletion in hive. [#7218](https://github.com/ydb-platform/ydb/pull/7218) ([vporyadke](https://github.com/vporyadke)).
* Added grpc endpoint into kqprun. [#7231](https://github.com/ydb-platform/ydb/pull/7231) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Renamed oidc `endpoint` parameters to `url-path`. [#7246](https://github.com/ydb-platform/ydb/pull/7246) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Fix handling of schema elements in .sys directory. [#7429](https://github.com/ydb-platform/ydb/pull/7429) ([Alexey Efimov](https://github.com/adameat)).
* Removed abort. Added error event instead. ... [#7435](https://github.com/ydb-platform/ydb/pull/7435) ([Filitov Mikhail](https://github.com/lll-phill-lll)).
* `arrow::Type::STRING`, `arrow::Type::BINARY`, etc types are now not optional with type inferring. [#7456](https://github.com/ydb-platform/ydb/pull/7456) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Add group-by function to storage/groups handler. many fixes. [#7480](https://github.com/ydb-platform/ydb/pull/7480) ([Alexey Efimov](https://github.com/adameat)).
* Closes [#7478](https://github.com/ydb-platform/ydb/issues/7478). [#7481](https://github.com/ydb-platform/ydb/pull/7481) ([Alexey Efimov](https://github.com/adameat)).
* Https://github.com/orgs/ydb-platform/projects/37/views/1?filterquery=%5b%5bnebius+iam+integration%5d%5d&pane=issue&itemid=67157010 remove unnecessary - unused variable accessservicetype - handle tevhttpincomingresponse dublicates - removeappliedcookie method. cookie removed like in the first version now. [#7487](https://github.com/ydb-platform/ydb/pull/7487) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Remove start message for kqprun. [#7490](https://github.com/ydb-platform/ydb/pull/7490) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Support memory pools configurations & improve spilling settings. [#7510](https://github.com/ydb-platform/ydb/pull/7510) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Support EnforceUserTokenCheckRequirement option for the case of mTLS. [#7511](https://github.com/ydb-platform/ydb/pull/7511) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Add `--pgwire-port` and `--pgwire-address` command line options for ydbd process. [#7528](https://github.com/ydb-platform/ydb/pull/7528) ([Timofey Koolin](https://github.com/rekby)).
* [refactoring] Remove unused GatherParents API. [#7541](https://github.com/ydb-platform/ydb/pull/7541) ([Andrey Neporada](https://github.com/nepal)).
* Add audit logging for login operation. [#7546](https://github.com/ydb-platform/ydb/pull/7546) ([ijon](https://github.com/ijon)).
* [issue](https://github.com/ydb-platform/ydb/issues/4611) -- changed `StorageUsage` to `TablesStorage`. If there is no quota info about specifi storage type - it doesn't return -- added `DatabaseStorage` -- use `SoftQuota` for storage limit. [#7554](https://github.com/ydb-platform/ydb/pull/7554) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* ... [#7574](https://github.com/ydb-platform/ydb/pull/7574) ([Innokentii Mokin](https://github.com/Enjection)).
* When client says that it expects data in json format, send issues in json format instead of html. It improves issues display in YDB UI. [#7576](https://github.com/ydb-platform/ydb/pull/7576) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Schedule tablets even when all nodes report extremely high network or cpu usage. [#7583](https://github.com/ydb-platform/ydb/pull/7583) ([vporyadke](https://github.com/vporyadke)).
* Limit transformation count while trying to annotate single node. [#7588](https://github.com/ydb-platform/ydb/pull/7588) ([Andrey Neporada](https://github.com/nepal)).
* Query Hints for Cardinality and Join algorithms are added to the Cost Based Optimizer. [#7629](https://github.com/ydb-platform/ydb/pull/7629) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* Refactor constructors of DSProxy requests. [#7631](https://github.com/ydb-platform/ydb/pull/7631) ([Sergey Belyakov](https://github.com/serbel324)).
* ... [#7667](https://github.com/ydb-platform/ydb/pull/7667) ([Innokentii Mokin](https://github.com/Enjection)).
* Pass actor system config into testlib. [#7693](https://github.com/ydb-platform/ydb/pull/7693) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Add interrupt-inheritance flag to acl handler. [#7701](https://github.com/ydb-platform/ydb/pull/7701) ([Alexey Efimov](https://github.com/adameat)).
* Https://st.yandex-team.ru/yq-2830. [#7734](https://github.com/ydb-platform/ydb/pull/7734) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Add stats for queries with errors. [#7753](https://github.com/ydb-platform/ydb/pull/7753) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Added validations on not existing for alter/drop object. [#7757](https://github.com/ydb-platform/ydb/pull/7757) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Don't penalize resource pools after consumption peaks. [#7763](https://github.com/ydb-platform/ydb/pull/7763) ([Mikhail Surin](https://github.com/ssmike)).
* Добавил версии RetryQuery, которые возращают TASyncStatus и TStatus и которые принимают ламбду, принимающую TQueryClient. [#7777](https://github.com/ydb-platform/ydb/pull/7777) ([stanislav_shchetinin](https://github.com/stanislav-shchetinin)).
* Increase future wait timeout. [#7780](https://github.com/ydb-platform/ydb/pull/7780) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Refactoring tests for `ydb-cli`. The tests use a recipe. It creates a database `/local` with the user `root`. [#7781](https://github.com/ydb-platform/ydb/pull/7781) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Removed session creation per file and added saving for describe result before import start, that allows to load more than 50 files without "active sessions limit" error. [#7785](https://github.com/ydb-platform/ydb/pull/7785) ([Bulat](https://github.com/Gazizonoki)).
* Support client cert in WhoAmI (it has separate implementation). [#7816](https://github.com/ydb-platform/ydb/pull/7816) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#7836](https://github.com/ydb-platform/ydb/pull/7836) ([Vadim Averin](https://github.com/avevad)).
* Fix for [yq-2576](https://st.yandex-team.ru/yq-2576). [#7842](https://github.com/ydb-platform/ydb/pull/7842) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Pass allow local files into runtime listing and schema inference. [#7844](https://github.com/ydb-platform/ydb/pull/7844) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* [ydb-cli] saving plan & ast even on errors. [#7874](https://github.com/ydb-platform/ydb/pull/7874) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Minor style fixes. [#7907](https://github.com/ydb-platform/ydb/pull/7907) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Add more introspection into PDisk's ChunkWrite and LogWrite. [#7941](https://github.com/ydb-platform/ydb/pull/7941) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Currently mkql allocator makes requests by chunks of 30mib minimum, so making that configurable and changing that limit to 8mib. [#7951](https://github.com/ydb-platform/ydb/pull/7951) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Improve error in s3 applicator actor. [#7976](https://github.com/ydb-platform/ydb/pull/7976) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Added s3 wildcards validations. [#8017](https://github.com/ydb-platform/ydb/pull/8017) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Ensure per_az followers are created when new datacenter is registered & are deleted when it is deregistered. [#8069](https://github.com/ydb-platform/ydb/pull/8069) ([vporyadke](https://github.com/vporyadke)).
* Add monitoring sensors for `Node Broker` tablet. [#8091](https://github.com/ydb-platform/ydb/pull/8091) ([Ilia Shakhov](https://github.com/pixcc)).
* Type inference json suppoty. [#8102](https://github.com/ydb-platform/ydb/pull/8102) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Optimize nodes handler fix issues with serverless databases fix http redirects issues switch viewer ut to in-memory disks add cookie to scheme board actor. [#8111](https://github.com/ydb-platform/ydb/pull/8111) ([Alexey Efimov](https://github.com/adameat)).
* Implement tpc benchmarks as tests. [#8125](https://github.com/ydb-platform/ydb/pull/8125) ([Vladluk](https://github.com/vladl2802)).
* ... [#8131](https://github.com/ydb-platform/ydb/pull/8131) ([Sergey Belyakov](https://github.com/serbel324)).
* Add support redirects for oidc proxy. [#8151](https://github.com/ydb-platform/ydb/pull/8151) ([Andrey Molotkov](https://github.com/molotkov-and)).
* ... [#8160](https://github.com/ydb-platform/ydb/pull/8160) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Fix for [#7989](https://github.com/ydb-platform/ydb/issues/7989). [#8210](https://github.com/ydb-platform/ydb/pull/8210) ([Ivan](https://github.com/abyss7)).
* ... [#8232](https://github.com/ydb-platform/ydb/pull/8232) ([Oleg Doronin](https://github.com/dorooleg)).
* Support for `partitioned_by`, `file_pattern` and `csv_delimiter` parameters with schema inference. [#8252](https://github.com/ydb-platform/ydb/pull/8252) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Added default values for `Family` and `FamilyName` fields when use describe handler. [#8266](https://github.com/ydb-platform/ydb/pull/8266) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Implement security tags passthrough in DQ. [#8308](https://github.com/ydb-platform/ydb/pull/8308) ([Vadim Averin](https://github.com/avevad)).
* If DataShard detects IsSubDomainOutOfSpace than it should return DISK_SPACE_EXHAUSTED error. [#8318](https://github.com/ydb-platform/ydb/pull/8318) ([azevaykin](https://github.com/azevaykin)).
* Do not use Likely() as a sign of already performed pushdown * Add more cases when pushdown should not be done. [#8360](https://github.com/ydb-platform/ydb/pull/8360) ([Andrey Neporada](https://github.com/nepal)).
* ... [#8376](https://github.com/ydb-platform/ydb/pull/8376) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* CMS request priorities is enabled by default. [#8380](https://github.com/ydb-platform/ydb/pull/8380) ([Ilia Shakhov](https://github.com/pixcc)).
* ... [#8395](https://github.com/ydb-platform/ydb/pull/8395) ([pilik](https://github.com/pashandor789)).
* ... [#8396](https://github.com/ydb-platform/ydb/pull/8396) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Change a little how feature flags are returned. [#8434](https://github.com/ydb-platform/ydb/pull/8434) ([Alexey Efimov](https://github.com/adameat)).
* Improved overload issues. [#8437](https://github.com/ydb-platform/ydb/pull/8437) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix cors headers for traces. [#8458](https://github.com/ydb-platform/ydb/pull/8458) ([Alexey Efimov](https://github.com/adameat)).
* Support per-query limits [#4889](https://github.com/ydb-platform/ydb/issues/4889). [#8520](https://github.com/ydb-platform/ydb/pull/8520) ([Mikhail Surin](https://github.com/ssmike)).
* Collect security tags properly from table content files. [#8542](https://github.com/ydb-platform/ydb/pull/8542) ([Vadim Averin](https://github.com/avevad)).
* Add audit logging for (database/tables) export and import operations. [#8550](https://github.com/ydb-platform/ydb/pull/8550) ([ijon](https://github.com/ijon)).
* ... [#8567](https://github.com/ydb-platform/ydb/pull/8567) ([Vitaly Stoyan](https://github.com/vitstn)).
* Add doc for parallel scans. [#8585](https://github.com/ydb-platform/ydb/pull/8585) ([Mikhail Surin](https://github.com/ssmike)).
* More confident DS proxy phantom blob checking logic. [#8611](https://github.com/ydb-platform/ydb/pull/8611) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Relax FlatMap over Extend requirements. [#8626](https://github.com/ydb-platform/ydb/pull/8626) ([Andrey Neporada](https://github.com/nepal)).
* ... [#8637](https://github.com/ydb-platform/ydb/pull/8637) ([Sergey Belyakov](https://github.com/serbel324)).
* ... [#8657](https://github.com/ydb-platform/ydb/pull/8657) ([Vitaly Stoyan](https://github.com/vitstn)).
* Interactive CLI (`ydb` command) now works over QueryService instead of QueryService - Interactive CLI now terminates on "quit" or "exit" commands. [#8665](https://github.com/ydb-platform/ydb/pull/8665) ([Nikolay Perfilov](https://github.com/pnv1)).
* Added issues for timeout and cancelled. [#8718](https://github.com/ydb-platform/ydb/pull/8718) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Allow SelfHeal operation while in DEGRADED state. [#8734](https://github.com/ydb-platform/ydb/pull/8734) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Inference projections support. [#8744](https://github.com/ydb-platform/ydb/pull/8744) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* ... [#8755](https://github.com/ydb-platform/ydb/pull/8755) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#8760](https://github.com/ydb-platform/ydb/pull/8760) ([Vitaly Stoyan](https://github.com/vitstn)).
* Warn user that timestamp format params are not supported with type inferring. [#8762](https://github.com/ydb-platform/ydb/pull/8762) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Always show table with broken locks. [#8763](https://github.com/ydb-platform/ydb/pull/8763) ([Nikita Vasilev](https://github.com/nikvas0)).
* Report errors on databases ignore host in incoming cache. [#8766](https://github.com/ydb-platform/ydb/pull/8766) ([Alexey Efimov](https://github.com/adameat)).
* Added cancel after for script requests. [#8768](https://github.com/ydb-platform/ydb/pull/8768) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#8785](https://github.com/ydb-platform/ydb/pull/8785) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Split wideCombiner's state into buckets earlier - when the memory limit is set. It should prevent OOM after hash table x2 growth ... [#8804](https://github.com/ydb-platform/ydb/pull/8804) ([Filitov Mikhail](https://github.com/lll-phill-lll)).
* Better spilling errors ... [#8812](https://github.com/ydb-platform/ydb/pull/8812) ([Filitov Mikhail](https://github.com/lll-phill-lll)).
* Enable column shard by default in kqprun. [#8820](https://github.com/ydb-platform/ydb/pull/8820) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Added validations for resource pool parametres. [#8831](https://github.com/ydb-platform/ydb/pull/8831) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Support PG types in YT export and some build fixes. [#8833](https://github.com/ydb-platform/ydb/pull/8833) ([Ivan Nikolaev](https://github.com/lex007in)).
* ... [#8902](https://github.com/ydb-platform/ydb/pull/8902) ([Vitaly Stoyan](https://github.com/vitstn)).
* Add IListBuilder to UDF ABI. [#8914](https://github.com/ydb-platform/ydb/pull/8914) ([Vadim Averin](https://github.com/avevad)).
* Move redirects to base class, solve problem with redirects in serverless databases. [#8934](https://github.com/ydb-platform/ydb/pull/8934) ([Alexey Efimov](https://github.com/adameat)).
* Optimize waiting for index creation during restore in YDB CLI. [#8936](https://github.com/ydb-platform/ydb/pull/8936) ([Ilia Shakhov](https://github.com/pixcc)).
* ... [#8946](https://github.com/ydb-platform/ydb/pull/8946) ([Andrey Molotkov](https://github.com/molotkov-and)).
* ... [#8947](https://github.com/ydb-platform/ydb/pull/8947) ([Andrey Molotkov](https://github.com/molotkov-and)).
* ... [#8948](https://github.com/ydb-platform/ydb/pull/8948) ([Andrey Molotkov](https://github.com/molotkov-and)).
* ... [#8982](https://github.com/ydb-platform/ydb/pull/8982) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Fixed AS pools and added validations. [#9030](https://github.com/ydb-platform/ydb/pull/9030) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Added resource pools classifiers validations. [#9037](https://github.com/ydb-platform/ydb/pull/9037) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Add audit logging for web logout operation. [#9050](https://github.com/ydb-platform/ydb/pull/9050) ([ijon](https://github.com/ijon)).
* Added DisableExternalDataSourcesOnServerless feature flag. [#9062](https://github.com/ydb-platform/ydb/pull/9062) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#9080](https://github.com/ydb-platform/ydb/pull/9080) ([Andrey Molotkov](https://github.com/molotkov-and)).
* General improvements for in-test tpc benchs that run in nightly-run. [#9124](https://github.com/ydb-platform/ydb/pull/9124) ([Vladluk](https://github.com/vladl2802)).
* ... [#9192](https://github.com/ydb-platform/ydb/pull/9192) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Implement merge reads option for data query. [#9206](https://github.com/ydb-platform/ydb/pull/9206) ([Mikhail Surin](https://github.com/ssmike)).
* ... [#9245](https://github.com/ydb-platform/ydb/pull/9245) ([Vitaly Stoyan](https://github.com/vitstn)).
* 1. Inherit column group usage from YtMerge/YtCopy consumers to minimize data transformations in merge ops 2. Validate that YtCopy has equal input/output column groups 3. ResPull behaves like YtPublish without column group hint - a possible full result should have no column groups. [#9269](https://github.com/ydb-platform/ydb/pull/9269) ([Roman Udovichenko](https://github.com/rvu1024)).
* Fix for [YQ-3677](https://st.yandex-team.ru/YQ-3677). [#9278](https://github.com/ydb-platform/ydb/pull/9278) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Put spilling stats in metrics in order to get those from dqrun. [#9282](https://github.com/ydb-platform/ydb/pull/9282) ([Vladluk](https://github.com/vladl2802)).
* Add easier way to get content of a group: - filter_group_by = group kind - filter_group = content for filtering. [#9289](https://github.com/ydb-platform/ydb/pull/9289) ([Alexey Efimov](https://github.com/adameat)).
* Support all arrow types in size calcer except of: * DENSE_UNION * DICTIONARY * EXTENSION. [#9296](https://github.com/ydb-platform/ydb/pull/9296) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#9305](https://github.com/ydb-platform/ydb/pull/9305) ([Vitaly Stoyan](https://github.com/vitstn)).
* Limit inflight cross-database scheme requests in the replication controller. [#9334](https://github.com/ydb-platform/ydb/pull/9334) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Support PG types in arrow and clickhouse. [#9335](https://github.com/ydb-platform/ydb/pull/9335) ([Ivan Nikolaev](https://github.com/lex007in)).
* Support PG types in CDC. [#9337](https://github.com/ydb-platform/ydb/pull/9337) ([Ivan Nikolaev](https://github.com/lex007in)).
* ... [#9379](https://github.com/ydb-platform/ydb/pull/9379) ([Sergey Belyakov](https://github.com/serbel324)).
* ... [#9403](https://github.com/ydb-platform/ydb/pull/9403) ([Vitaly Stoyan](https://github.com/vitstn)).
* Highlight YQL using common lexer in YDB CLI interactive mode. [#9404](https://github.com/ydb-platform/ydb/pull/9404) ([Victor Smirnov](https://github.com/vityaman)).
* Support Fetch and Replace operations for storage_config.yaml. [#9412](https://github.com/ydb-platform/ydb/pull/9412) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Node roles in cluster handler. [#9479](https://github.com/ydb-platform/ydb/pull/9479) ([Alexey Efimov](https://github.com/adameat)).
* Add more sort options for nodes handler. [#9481](https://github.com/ydb-platform/ydb/pull/9481) ([Alexey Efimov](https://github.com/adameat)).
* Make execute-query default action for query handler. [#9483](https://github.com/ydb-platform/ydb/pull/9483) ([Alexey Efimov](https://github.com/adameat)).
* Ignoring columns with unsupported parquet and json types (a.k.a. lists, structs, maps, dicts, etc) with type inferring. [#9524](https://github.com/ydb-platform/ydb/pull/9524) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Tune trace names. [#9540](https://github.com/ydb-platform/ydb/pull/9540) ([Alexey Efimov](https://github.com/adameat)).
* ... [#9553](https://github.com/ydb-platform/ydb/pull/9553) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#9556](https://github.com/ydb-platform/ydb/pull/9556) ([Oleg Doronin](https://github.com/dorooleg)).
* `ydb workload query run` command is now working over QueryService instead of ScriptingService. [#9564](https://github.com/ydb-platform/ydb/pull/9564) ([Nikolay Perfilov](https://github.com/pnv1)).
* Fix for [YQ-3691](https://st.yandex-team.ru/YQ-3691). [#9571](https://github.com/ydb-platform/ydb/pull/9571) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Add new field to sort lwtrack on it. [#9576](https://github.com/ydb-platform/ydb/pull/9576) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Remove state from cookie. Create random string, sign this string by client secret and send this pair as state. Remove isAjaxRequest from cookie. [#9588](https://github.com/ydb-platform/ydb/pull/9588) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Added session settings. [#9589](https://github.com/ydb-platform/ydb/pull/9589) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Added kqp proxy database cache. [#9644](https://github.com/ydb-platform/ydb/pull/9644) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Help is now printed if a command is executed without required free arguments. [#9693](https://github.com/ydb-platform/ydb/pull/9693) ([Nikolay Perfilov](https://github.com/pnv1)).
* CMS allows to evict all vdisks from a rack. [#9740](https://github.com/ydb-platform/ydb/pull/9740) ([Ilia Shakhov](https://github.com/pixcc)).
* Add traces and database redirects to local rpc calls unify parameters and method checks and bootstrap procedures. [#9745](https://github.com/ydb-platform/ydb/pull/9745) ([Alexey Efimov](https://github.com/adameat)).
* This way profiler stacks are resolved much more precisely - and include inlined frames now. [#9766](https://github.com/ydb-platform/ydb/pull/9766) ([Ivan](https://github.com/abyss7)).
* Added database id for workload manager. [#9768](https://github.com/ydb-platform/ydb/pull/9768) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix empty group names closes [#9762](https://github.com/ydb-platform/ydb/issues/9762). [#9775](https://github.com/ydb-platform/ydb/pull/9775) ([Alexey Efimov](https://github.com/adameat)).
* Wide combiner spill during state split. ... [#9785](https://github.com/ydb-platform/ydb/pull/9785) ([Filitov Mikhail](https://github.com/lll-phill-lll)).
* Support relative paths in scheme service. [#9846](https://github.com/ydb-platform/ydb/pull/9846) ([Alexey Efimov](https://github.com/adameat)).
* Add support PG types in CellMaker. [#9856](https://github.com/ydb-platform/ydb/pull/9856) ([Ivan Nikolaev](https://github.com/lex007in)).
* Use CH udf in json parsing. [#9878](https://github.com/ydb-platform/ydb/pull/9878) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Groups sorting. [#9892](https://github.com/ydb-platform/ydb/pull/9892) ([Alexey Efimov](https://github.com/adameat)).
* Added pushdown for extract members in PQ provider. [#9939](https://github.com/ydb-platform/ydb/pull/9939) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#10015](https://github.com/ydb-platform/ydb/pull/10015) ([Vitaly Stoyan](https://github.com/vitstn)).
* Replace conanfile.txt by conanfile.py. [#10066](https://github.com/ydb-platform/ydb/pull/10066) ([Dmitrii Dmitriev](https://github.com/dimdim1177)).
* Add url params to trace attributes. [#10076](https://github.com/ydb-platform/ydb/pull/10076) ([Alexey Efimov](https://github.com/adameat)).
* Https://github.com/ydb-platform/ydb/issues/10112 added grpc connection keep alive properties to avoid deadline exceeded. [#10101](https://github.com/ydb-platform/ydb/pull/10101) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Support optimizers for AssumeUnique/AssumeDistinct callables in DQ/YT providers. [#10102](https://github.com/ydb-platform/ydb/pull/10102) ([Roman Udovichenko](https://github.com/rvu1024)).
* ... [#10199](https://github.com/ydb-platform/ydb/pull/10199) ([Vitaly Stoyan](https://github.com/vitstn)).
* Add history to some logs in dsproxy. [#10214](https://github.com/ydb-platform/ydb/pull/10214) ([VPolka](https://github.com/VPolka)).
* Delay making EquiJoin inputs unordered until CROSS JOIN is rewritten to inner. [#10229](https://github.com/ydb-platform/ydb/pull/10229) ([Andrey Neporada](https://github.com/nepal)).
* Do not trigger dead tablet issue during creation of a lot of tablets (e. g. a backup operation). [#10235](https://github.com/ydb-platform/ydb/pull/10235) ([vporyadke](https://github.com/vporyadke)).
* More detailed trace in viewer/tenantinfo. [#10239](https://github.com/ydb-platform/ydb/pull/10239) ([Alexey Efimov](https://github.com/adameat)).
* Minor fixes for storage groups. [#10249](https://github.com/ydb-platform/ydb/pull/10249) ([Alexey Efimov](https://github.com/adameat)).
* ... [#10254](https://github.com/ydb-platform/ydb/pull/10254) ([Nikita-Levuskin](https://github.com/Nikita-Levuskin)).
* Https://nebius.atlassian.net/browse/nbydb-475 added mask for token in mvp. [#10276](https://github.com/ydb-platform/ydb/pull/10276) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Option for tests with topics. [#10292](https://github.com/ydb-platform/ydb/pull/10292) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* ... [#10311](https://github.com/ydb-platform/ydb/pull/10311) ([Vitaly Stoyan](https://github.com/vitstn)).
* Https://nebius.atlassian.net/browse/nbydb-475 mask set-cookie in http response. [#10316](https://github.com/ydb-platform/ydb/pull/10316) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Support PG types for TTL in datashard. [#10318](https://github.com/ydb-platform/ydb/pull/10318) ([Ivan Nikolaev](https://github.com/lex007in)).
* Add compression level validation for S3 backups. [#10329](https://github.com/ydb-platform/ydb/pull/10329) ([Ilia Shakhov](https://github.com/pixcc)).
* ... [#10367](https://github.com/ydb-platform/ydb/pull/10367) ([stanislav_shchetinin](https://github.com/stanislav-shchetinin)).
* ... [#10379](https://github.com/ydb-platform/ydb/pull/10379) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#10399](https://github.com/ydb-platform/ydb/pull/10399) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Https://nebius.atlassian.net/browse/nbydb-475 don't use `getrawdata` for logging. [#10450](https://github.com/ydb-platform/ydb/pull/10450) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Supported optional columns as NULLs. [#10452](https://github.com/ydb-platform/ydb/pull/10452) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Now we won't immediately flush all following changes after first uncommitted changes read. [#10507](https://github.com/ydb-platform/ydb/pull/10507) ([Nikita Vasilev](https://github.com/nikvas0)).
* Now with the `SysLogToStdErr` option from `TLogConfig` enabled, logs are duplicated in stderr. [#10595](https://github.com/ydb-platform/ydb/pull/10595) ([Dmitry Razumov](https://github.com/dvrazumov)).
* Enhance help for ImportData option in ydb tools restore. [#10599](https://github.com/ydb-platform/ydb/pull/10599) ([Ilia Shakhov](https://github.com/pixcc)).
* Improve whiteboard tracing and skip invalid path id. [#10704](https://github.com/ydb-platform/ydb/pull/10704) ([Alexey Efimov](https://github.com/adameat)).
* ... [#10732](https://github.com/ydb-platform/ydb/pull/10732) ([Vitaly Stoyan](https://github.com/vitstn)).
* Supported computation graph invalidation in purecalc in push stream mode, it is required for stateless execution. [#10799](https://github.com/ydb-platform/ydb/pull/10799) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#10848](https://github.com/ydb-platform/ydb/pull/10848) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#10856](https://github.com/ydb-platform/ydb/pull/10856) ([Oleg Doronin](https://github.com/dorooleg)).
* Support pg types in datashard. [#10872](https://github.com/ydb-platform/ydb/pull/10872) ([Ivan Nikolaev](https://github.com/lex007in)).
* Add nodes group by state. [#10877](https://github.com/ydb-platform/ydb/pull/10877) ([Alexey Efimov](https://github.com/adameat)).
* ... [#10890](https://github.com/ydb-platform/ydb/pull/10890) ([Oleg Doronin](https://github.com/dorooleg)).
* Add some logs to dsproxy. [#10905](https://github.com/ydb-platform/ydb/pull/10905) ([VPolka](https://github.com/VPolka)).
* `tools restore`: print location in error messages. [#10948](https://github.com/ydb-platform/ydb/pull/10948) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Stop wide combiner state from growing unlimited and spill it if spilling is enabled. [#10997](https://github.com/ydb-platform/ydb/pull/10997) ([Vladluk](https://github.com/vladl2802)).
* Use -FreeSlots() as PickerScore in BSC to properly populate disks of unequal size. [#11008](https://github.com/ydb-platform/ydb/pull/11008) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Add test for shard splitting by PG key * Support PG types for PartitionKeySchema in PQ. [#11023](https://github.com/ydb-platform/ydb/pull/11023) ([Ivan Nikolaev](https://github.com/lex007in)).
* ... [#11068](https://github.com/ydb-platform/ydb/pull/11068) ([Vitaly Stoyan](https://github.com/vitstn)).
* Support PG and Decimal in scheme board cache viewer. [#11076](https://github.com/ydb-platform/ydb/pull/11076) ([Ivan Nikolaev](https://github.com/lex007in)).
* #10907 Don't take locks in ShapshotReadOnly. [#11085](https://github.com/ydb-platform/ydb/pull/11085) ([Mikhail Surin](https://github.com/ssmike)).
* ... [#11091](https://github.com/ydb-platform/ydb/pull/11091) ([Vitaly Stoyan](https://github.com/vitstn)).
* Added new options to `ydb workload topic`: --tx-commit-interval and --tx-commit-messages, allowing you to specify commit interval either in milliseconds or in number of messages written. Also now you can load test YDB topics, using wide transactions that span over all partitions in the topic. This works both in write and in end-to-end workload scenarios. ... [#11141](https://github.com/ydb-platform/ydb/pull/11141) ([Andrey Serebryanskiy](https://github.com/a-serebryanskiy)).
* Supported Json columns without predicate. [#11150](https://github.com/ydb-platform/ydb/pull/11150) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#11152](https://github.com/ydb-platform/ydb/pull/11152) ([Vitaly Stoyan](https://github.com/vitstn)).
* Add simplified mirror-3dc support in CMS. [#11190](https://github.com/ydb-platform/ydb/pull/11190) ([Ilia Shakhov](https://github.com/pixcc)).
* ... [#11207](https://github.com/ydb-platform/ydb/pull/11207) ([Roman Udovichenko](https://github.com/rvu1024)).
* ... [#11219](https://github.com/ydb-platform/ydb/pull/11219) ([Vitaly Stoyan](https://github.com/vitstn)).
* Add YQL highlighting tests. [#11234](https://github.com/ydb-platform/ydb/pull/11234) ([Victor Smirnov](https://github.com/vityaman)).
* Human readable `cluster_name` property from logconfig (instead of runconfig with uuid format) - fix `node_type` session meta property value. [#11240](https://github.com/ydb-platform/ydb/pull/11240) ([Aleksei Kobzev](https://github.com/kobzonega)).
* For tickets in ticket parser cashe set low priority for requests to access service. [#11278](https://github.com/ydb-platform/ydb/pull/11278) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Force oldest (not newest) locks into shard locks due to range limits. [#11329](https://github.com/ydb-platform/ydb/pull/11329) ([Aleksei Borzenkov](https://github.com/snaury)).
* Support strings parsing in Json columns. [#11331](https://github.com/ydb-platform/ydb/pull/11331) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* New CLI flag here: --no-consumer. It allows user to read topic without creating a consumer in advance. Boosts the debugging through the CLI speed. ... [#11352](https://github.com/ydb-platform/ydb/pull/11352) ([Andrey Serebryanskiy](https://github.com/a-serebryanskiy)).
* Added obfuscated cookie logs. [#11367](https://github.com/ydb-platform/ydb/pull/11367) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Specify more clearly what concrete type of timestamp is in options - Support different timestamp formats. [#11387](https://github.com/ydb-platform/ydb/pull/11387) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Optimized purecalc memory usage. [#11394](https://github.com/ydb-platform/ydb/pull/11394) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Supported COALESCE and IF pushdown. [#11397](https://github.com/ydb-platform/ydb/pull/11397) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#11401](https://github.com/ydb-platform/ydb/pull/11401) ([Alexey Efimov](https://github.com/adameat)).
* Add field LogMessage to structure TError of ticket parser for return special message for log. [#11403](https://github.com/ydb-platform/ydb/pull/11403) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Return special error messages for write to log from ldap auth provider. [#11404](https://github.com/ydb-platform/ydb/pull/11404) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Switch actor system to lock-free mailboxes with intrusive event lists. [#11419](https://github.com/ydb-platform/ydb/pull/11419) ([Aleksei Borzenkov](https://github.com/snaury)).
* Evwrite optimizations. [#11428](https://github.com/ydb-platform/ydb/pull/11428) ([Nikita Vasilev](https://github.com/nikvas0)).
* Supported OR split during pushdown. [#11439](https://github.com/ydb-platform/ydb/pull/11439) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#11443](https://github.com/ydb-platform/ydb/pull/11443) ([Oleg Doronin](https://github.com/dorooleg)).
* Support PG literals in KQP. [#11446](https://github.com/ydb-platform/ydb/pull/11446) ([Ivan Nikolaev](https://github.com/lex007in)).
* ... [#11450](https://github.com/ydb-platform/ydb/pull/11450) ([Alexey Efimov](https://github.com/adameat)).
* ... [#11470](https://github.com/ydb-platform/ydb/pull/11470) ([Alexey Efimov](https://github.com/adameat)).
* # Docker image. [#11472](https://github.com/ydb-platform/ydb/pull/11472) ([Aleksei Kobzev](https://github.com/kobzonega)).
* Replace usage of `CPP_STYLE_TEST_16` with `STYLE_CPP`. [#11523](https://github.com/ydb-platform/ydb/pull/11523) ([andrei-levitskii](https://github.com/andrei-levitskii)).
* Supported mod pushdown. [#11543](https://github.com/ydb-platform/ydb/pull/11543) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix for [yq-2950](https://st.yandex-team.ru/yq-2950). [#11608](https://github.com/ydb-platform/ydb/pull/11608) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Add direct conversion from Ydb::Value tuple to Cell in rpc_read_table. [#11615](https://github.com/ydb-platform/ydb/pull/11615) ([Ivan Nikolaev](https://github.com/lex007in)).
* Supported regexp pushdown. [#11626](https://github.com/ydb-platform/ydb/pull/11626) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Added limit for parser buffer size. [#11627](https://github.com/ydb-platform/ydb/pull/11627) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Support ALTER TABLE for adding PG types. [#11630](https://github.com/ydb-platform/ydb/pull/11630) ([Ivan Nikolaev](https://github.com/lex007in)).
* Use `DEBUGINFO_LINES_ONLY` param for ydbd binary in breakpad docker tag This will allow to extract the correct stacktraces and see lines in coredumps (thanks to @iddqdex). [#11671](https://github.com/ydb-platform/ydb/pull/11671) ([Aleksei Kobzev](https://github.com/kobzonega)).
* Replace logical ids with 0 in canonized files as it is done in dq_file. [#11683](https://github.com/ydb-platform/ydb/pull/11683) ([Andrey Neporada](https://github.com/nepal)).
* Bump breakpad dependency to `v2023.06.01` - disable useless thread events from gdb output for stacktrace - add debug symbols into pkg.json for build docker `debug` image - add readme.md for `breakpad_init` package. [#11735](https://github.com/ydb-platform/ydb/pull/11735) ([Aleksei Kobzev](https://github.com/kobzonega)).
* Allow running stock bench for Olap shards. [#11757](https://github.com/ydb-platform/ydb/pull/11757) ([Nikita Vasilev](https://github.com/nikvas0)).
* Minidump_script.py in docker breakpad should firstly extract backtrace from current thread. [#11815](https://github.com/ydb-platform/ydb/pull/11815) ([Aleksei Kobzev](https://github.com/kobzonega)).
* Added per node partition limit. [#11830](https://github.com/ydb-platform/ydb/pull/11830) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* In 24-3, support for redirecting requests to dynodes was added. The fix adjusts the scenario where a redirect is not possible: instead of throwing a "Failed to resolve database" error, the request is processed locally on the node that received it. [#11841](https://github.com/ydb-platform/ydb/pull/11841) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Allow to enable and kafka api port for ydb-local docker image. [#11892](https://github.com/ydb-platform/ydb/pull/11892) ([Timofey Koolin](https://github.com/rekby)).
* Removed S3 MaxReadSizePerQuery config. [#11936](https://github.com/ydb-platform/ydb/pull/11936) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Passed UV from filter to read actor + topic session refactor. [#11940](https://github.com/ydb-platform/ydb/pull/11940) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* New internal error status for EvWriteResult from data_events: wrong shard state. [#11955](https://github.com/ydb-platform/ydb/pull/11955) ([Daniil Timizhev](https://github.com/dahbka-lis)).
* Add signal information for the coredump that was generated from the minidump. This information is parsed from the `minidump_stackwalk` output and appended to the gdb-generated information with backtraces. [#12011](https://github.com/ydb-platform/ydb/pull/12011) ([Aleksei Kobzev](https://github.com/kobzonega)).
* Audit logs have sanitized_token field. Provide this field also for login audit record. [#12031](https://github.com/ydb-platform/ydb/pull/12031) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* MinStep value - transactions are ordered by (Step, TxId) - the name of the state instead of the number. [#12060](https://github.com/ydb-platform/ydb/pull/12060) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Supported pushdown for SafeCast, ToBytes, FlatMap. [#12066](https://github.com/ydb-platform/ydb/pull/12066) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* There are situations when we need to generate a new trace id (or throttle existing one) not only from grpc proxy actor, but in several other places (long living topic session). For this case I refactored tracing configurator so that it can be available from every actor system thread. [#12067](https://github.com/ydb-platform/ydb/pull/12067) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Additional validation for s3 writes, double optional types are now explicitly unsupported. [#12082](https://github.com/ydb-platform/ydb/pull/12082) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* If the transaction is not scheduled, a dash is shown in the Step field. [#12085](https://github.com/ydb-platform/ydb/pull/12085) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* It is now allowed to describe index table using `ydb cli scheme describe <table_path>/<index_name>`. [#12103](https://github.com/ydb-platform/ydb/pull/12103) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#12105](https://github.com/ydb-platform/ydb/pull/12105) ([Vitaly Stoyan](https://github.com/vitstn)).
* Added script execute stats_mode in swagger. [#12137](https://github.com/ydb-platform/ydb/pull/12137) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* ... [#12149](https://github.com/ydb-platform/ydb/pull/12149) ([vporyadke](https://github.com/vporyadke)).
* [YQL-19309] Switch YT provider to DQ nodes from yql/essentials. [#12158](https://github.com/ydb-platform/ydb/pull/12158) ([Andrey Neporada](https://github.com/nepal)).
* Improve WriteActor: - move serialization to fwd actor - remove table resolve - fixed segfault. [#12167](https://github.com/ydb-platform/ydb/pull/12167) ([Nikita Vasilev](https://github.com/nikvas0)).
* [YQL-19309] Sync with Arcadia. [#12219](https://github.com/ydb-platform/ydb/pull/12219) ([Andrey Neporada](https://github.com/nepal)).
* ... [#12285](https://github.com/ydb-platform/ydb/pull/12285) ([Vitaly Stoyan](https://github.com/vitstn)).
* [YQL-19206] Sync with Arcadia. [#12300](https://github.com/ydb-platform/ydb/pull/12300) ([Andrey Neporada](https://github.com/nepal)).
* Add some more direct read cache proxy counters. [#12317](https://github.com/ydb-platform/ydb/pull/12317) ([FloatingCrowbar](https://github.com/FloatingCrowbar)).
* Now describe consumer result in CPP SDK have more fields. LastReadTime, MaxReadTimeLag and MaxWriteTimeLag ... [#12347](https://github.com/ydb-platform/ydb/pull/12347) ([alexnick88](https://github.com/alexnick88)).
* Added TYQLConclusionStatusImpl with NYql::TIssues as error. [#12452](https://github.com/ydb-platform/ydb/pull/12452) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Add support for topic operations in BufferWriteActor with enabled OLTP sink. [#12464](https://github.com/ydb-platform/ydb/pull/12464) ([Daniil Timizhev](https://github.com/dahbka-lis)).
* Improved metadata objects errors. [#12486](https://github.com/ydb-platform/ydb/pull/12486) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Stream requests are long running session requests such as topic sessions. That's why they require special handling. [#12493](https://github.com/ydb-platform/ydb/pull/12493) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Minidump_script `signal_name` split by space - minidump_script limit gdb threads by 999. [#12501](https://github.com/ydb-platform/ydb/pull/12501) ([Aleksei Kobzev](https://github.com/kobzonega)).
* Collect Sink Stats. [#12507](https://github.com/ydb-platform/ydb/pull/12507) ([Nikita Vasilev](https://github.com/nikvas0)).
* Optimize memory allocation for schema versions on CS init. [#12533](https://github.com/ydb-platform/ydb/pull/12533) ([Semyon](https://github.com/swalrus1)).
* Try to preserve in-memory state (locks in particular) across datashard restarts. [#12567](https://github.com/ydb-platform/ydb/pull/12567) ([Aleksei Borzenkov](https://github.com/snaury)).
* Clean up fields of TIndexInfo to reduce memory footprint. [#12593](https://github.com/ydb-platform/ydb/pull/12593) ([Semyon](https://github.com/swalrus1)).
* Added parser mkql counters. [#12607](https://github.com/ydb-platform/ydb/pull/12607) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#12644](https://github.com/ydb-platform/ydb/pull/12644) ([Alexey Efimov](https://github.com/adameat)).
* Added more compatibilty with ydb configuration for ydbd_slice. [#12658](https://github.com/ydb-platform/ydb/pull/12658) ([Alexander Petrukhin](https://github.com/shmel1k)).
* The duplication in the code has been removed. References to values are used along with copies. Remove the unnecessary `TCacheEvictionStrategy:: SaveUserOffset` method. [#12661](https://github.com/ydb-platform/ydb/pull/12661) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Add support for immediate commit and rollback with topics in BufferWriteActor. ... [#12669](https://github.com/ydb-platform/ydb/pull/12669) ([Daniil Timizhev](https://github.com/dahbka-lis)).
* Reuse schemas between cs on the same node. [#12673](https://github.com/ydb-platform/ydb/pull/12673) ([Semyon](https://github.com/swalrus1)).
* ... [#12677](https://github.com/ydb-platform/ydb/pull/12677) ([VPolka](https://github.com/VPolka)).
* Add support for column tables with topics in BufferWriteActor. [#12686](https://github.com/ydb-platform/ydb/pull/12686) ([Daniil Timizhev](https://github.com/dahbka-lis)).
* ... [#12687](https://github.com/ydb-platform/ydb/pull/12687) ([Alexey Efimov](https://github.com/adameat)).
* Abort volatile transactions during graceful restarts. [#12689](https://github.com/ydb-platform/ydb/pull/12689) ([Aleksei Borzenkov](https://github.com/snaury)).
* Add test to check counters are created for newly added consumer. [#12711](https://github.com/ydb-platform/ydb/pull/12711) ([FloatingCrowbar](https://github.com/FloatingCrowbar)).
* Change algorithm for create fingerprints of certificates from sha1 to sha256. [#12723](https://github.com/ydb-platform/ydb/pull/12723) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Now Put requests with blobs of 0 size are validated and rejected with ERROR status. [#12881](https://github.com/ydb-platform/ydb/pull/12881) ([Sergey Belyakov](https://github.com/serbel324)).
* Rename block-4-2 to block-4-2-8-nodes. [#12888](https://github.com/ydb-platform/ydb/pull/12888) ([Alexander Petrukhin](https://github.com/shmel1k)).
* Improved slices template configuration. [#12899](https://github.com/ydb-platform/ydb/pull/12899) ([Alexander Petrukhin](https://github.com/shmel1k)).
* Now if you specify `pqconfig.require_credentials_in_new_protocol: false` in cluster config, it will not require credentials to read/write/administrate topics through Kafka proxy. [#12900](https://github.com/ydb-platform/ydb/pull/12900) ([Andrey Serebryanskiy](https://github.com/a-serebryanskiy)).
* Ydbd_slice: add `sys_log: true` to default logging configuration. [#12968](https://github.com/ydb-platform/ydb/pull/12968) ([Alexander Petrukhin](https://github.com/shmel1k)).
* User can change self password by yourself. [#12983](https://github.com/ydb-platform/ydb/pull/12983) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Process follower updates in chunks to definitely avoid hitting commit size limit. [#13023](https://github.com/ydb-platform/ydb/pull/13023) ([vporyadke](https://github.com/vporyadke)).
* New column `CreatedAt` was added to schemeshard localdb in table `Sids`. [#13044](https://github.com/ydb-platform/ydb/pull/13044) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Added the TxInFly and TxCompleteLag metrics for the PQ tablet. [#13072](https://github.com/ydb-platform/ydb/pull/13072) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* New functions added. [#13120](https://github.com/ydb-platform/ydb/pull/13120) ([jsjant](https://github.com/jsjant)).
* Prepare login lockout info in order to use it in system view. [#13123](https://github.com/ydb-platform/ydb/pull/13123) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Added confirmation for ydbd_slice install/clear/format. [#13146](https://github.com/ydb-platform/ydb/pull/13146) ([Alexander Petrukhin](https://github.com/shmel1k)).
* Improved multi query mode and storage settings. [#13177](https://github.com/ydb-platform/ydb/pull/13177) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Added TMemoryControllerConfig support in ydbd_slice. [#13250](https://github.com/ydb-platform/ydb/pull/13250) ([Alexander Petrukhin](https://github.com/shmel1k)).
* Data integrity for OLAP. [#13277](https://github.com/ydb-platform/ydb/pull/13277) ([Nikita Vasilev](https://github.com/nikvas0)).
* Support folders in S3 URIs for CS tiers. [#13337](https://github.com/ydb-platform/ydb/pull/13337) ([Semyon](https://github.com/swalrus1)).
* ... [#13386](https://github.com/ydb-platform/ydb/pull/13386) ([Alexey Efimov](https://github.com/adameat)).
* Added NodeInterlace to `TScore` so that in case there are multiple VDisks in one rack (and group's DomainInterlace is > 0) next PDisk would not be selected from nodes that already have disks from this group. [#13458](https://github.com/ydb-platform/ydb/pull/13458) ([Semyon Danilov](https://github.com/SammyVimes)).
* Coordinator plan resolution can now be configured using immediate control board. [#13721](https://github.com/ydb-platform/ydb/pull/13721) ([Aleksei Borzenkov](https://github.com/snaury)).
* [Schema object limits](https://ydb.tech/docs/en/concepts/limits-ydb#schema-object) are now available as metrics. [#13723](https://github.com/ydb-platform/ydb/pull/13723) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Https://nebius.atlassian.net/browse/nbydb-770 add max-age to session cookie depending on iam response specification said that set-cookie max-age attribute is unsigned 31 bit. [#13732](https://github.com/ydb-platform/ydb/pull/13732) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Maintain access to populated tiers removed from TTL on CS. [#13733](https://github.com/ydb-platform/ydb/pull/13733) ([Semyon](https://github.com/swalrus1)).
* Default level of cost based optimization is set to 2, which means the cost based optimizer will only work on queries that include at least one column shard. ... [#13740](https://github.com/ydb-platform/ydb/pull/13740) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* This feature will help to easily add additional params to local_ydb in docker. [#13789](https://github.com/ydb-platform/ydb/pull/13789) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Grammar fix. Wrote some .stg to generate protobuf with antlr4 in the same format as at antlr3. Not tested with code yet. [#2977](https://github.com/ydb-platform/ydb/pull/2977) ([Orlov Pavel](https://github.com/OrlovPavel)).
* Implement cpu limiter in node service. [#4891](https://github.com/ydb-platform/ydb/pull/4891) ([Mikhail Surin](https://github.com/ssmike)).
* Added pragma that enables spilling in grace join. ... [#6253](https://github.com/ydb-platform/ydb/pull/6253) ([Filitov Mikhail](https://github.com/lll-phill-lll)).
* YDB FQ: Support MDB MySQL in DatabaseResolver. [#6257](https://github.com/ydb-platform/ydb/pull/6257) ([Timur Sufiyanov](https://github.com/skywalker-jpg)).
* YDB FQ: Add MySQL to fq proxy. [#6298](https://github.com/ydb-platform/ydb/pull/6298) ([Timur Sufiyanov](https://github.com/skywalker-jpg)).
* Allow to set trace verbosity and ttl. [#6310](https://github.com/ydb-platform/ydb/pull/6310) ([Alexey Efimov](https://github.com/adameat)).
* Adding query 'ALTER TABLE table ALTER COLUMN column DROP NOT NULL'. [#6342](https://github.com/ydb-platform/ydb/pull/6342) ([flown4qqqq](https://github.com/flown4qqqq)).
* Support load cpu threshold. [#6360](https://github.com/ydb-platform/ydb/pull/6360) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#6420](https://github.com/ydb-platform/ydb/pull/6420) ([pilik](https://github.com/pashandor789)).
* Add UserSID (Security ID) who created long-running operation (export, import). [#6463](https://github.com/ydb-platform/ydb/pull/6463) ([Ilia Shakhov](https://github.com/pixcc)).
* Add security_tags table write hint. [#6574](https://github.com/ydb-platform/ydb/pull/6574) ([Vadim Averin](https://github.com/avevad)).
* Add sensors for duration of tablet starts and number of tablets currently starting. [#6584](https://github.com/ydb-platform/ydb/pull/6584) ([vporyadke](https://github.com/vporyadke)).
* ... [#6603](https://github.com/ydb-platform/ydb/pull/6603) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* ... [#6680](https://github.com/ydb-platform/ydb/pull/6680) ([kruall](https://github.com/kruall)).
* YDB FQ: support Oracle as an external data source. [#6723](https://github.com/ydb-platform/ydb/pull/6723) ([Grigorii Papashvili](https://github.com/lifthelm)).
* ... [#6731](https://github.com/ydb-platform/ydb/pull/6731) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#6765](https://github.com/ydb-platform/ydb/pull/6765) ([Vitaly Stoyan](https://github.com/vitstn)).
* Support metadata storage over pdisk. [#6814](https://github.com/ydb-platform/ydb/pull/6814) ([Alexander Rutkovsky](https://github.com/alexvru)).
* New handler for returning groups data. more oriented for paging. [#6859](https://github.com/ydb-platform/ydb/pull/6859) ([Alexey Efimov](https://github.com/adameat)).
* Http viewer capabilities to check for supported features. [#6872](https://github.com/ydb-platform/ydb/pull/6872) ([Alexey Efimov](https://github.com/adameat)).
* `meta.meta_database_token_name` is used in the `Nebius` auth profile to specify the Jwt token that should be used for - `access_service_type` in tokenator config is used to detemine tokenator refreshing algorithm - requests to the meta database - rewrote `GetTableClient`, it depends on `access_service_type` now - renamed config parameter `auth-profile` to `access_service_type`. [#6878](https://github.com/ydb-platform/ydb/pull/6878) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* ... [#6886](https://github.com/ydb-platform/ydb/pull/6886) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#6911](https://github.com/ydb-platform/ydb/pull/6911) ([pilik](https://github.com/pashandor789)).
* Support AnsiImplicitCrossJoin mode. [#6950](https://github.com/ydb-platform/ydb/pull/6950) ([Andrey Neporada](https://github.com/nepal)).
* Support ydb scheme ls for resource pools. [#6956](https://github.com/ydb-platform/ydb/pull/6956) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* New Change Data Capture (CDC) record format — `DEBEZIUM_JSON`. [#7052](https://github.com/ydb-platform/ydb/pull/7052) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#7077](https://github.com/ydb-platform/ydb/pull/7077) ([Hor911](https://github.com/Hor911)).
* Add config option to specify ttl for user logins closes [#7035](https://github.com/ydb-platform/ydb/issues/7035). [#7083](https://github.com/ydb-platform/ydb/pull/7083) ([Alexey Efimov](https://github.com/adameat)).
* Async replication: concept, yql reference. [#7110](https://github.com/ydb-platform/ydb/pull/7110) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#7112](https://github.com/ydb-platform/ydb/pull/7112) ([Vitaly Stoyan](https://github.com/vitstn)).
* Added the ability to merge additional config to the main config. [#7136](https://github.com/ydb-platform/ydb/pull/7136) ([Nikita-Levuskin](https://github.com/Nikita-Levuskin)).
* ... [#7157](https://github.com/ydb-platform/ydb/pull/7157) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix config apply behavior - add reserved prefixes generation to plugin - use deprecated options in dynconfig. [#7162](https://github.com/ydb-platform/ydb/pull/7162) ([Innokentii Mokin](https://github.com/Enjection)).
* OAuth 2.0 token exchange. Allow multiple resource parameters. Update docs. [#7163](https://github.com/ydb-platform/ydb/pull/7163) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#7197](https://github.com/ydb-platform/ydb/pull/7197) ([Vitaly Stoyan](https://github.com/vitstn)).
* Include port in worker-name header. [#7250](https://github.com/ydb-platform/ydb/pull/7250) ([Alexey Efimov](https://github.com/adameat)).
* ... [#7338](https://github.com/ydb-platform/ydb/pull/7338) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#7383](https://github.com/ydb-platform/ydb/pull/7383) ([Vitaly Stoyan](https://github.com/vitstn)).
* Support sql for resource pool classifiers. [#7389](https://github.com/ydb-platform/ydb/pull/7389) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#7416](https://github.com/ydb-platform/ydb/pull/7416) ([yumkam](https://github.com/yumkam)).
* ... [#7430](https://github.com/ydb-platform/ydb/pull/7430) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#7432](https://github.com/ydb-platform/ydb/pull/7432) ([Vitaly Stoyan](https://github.com/vitstn)).
* Resource pools enabled. [#7443](https://github.com/ydb-platform/ydb/pull/7443) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#7447](https://github.com/ydb-platform/ydb/pull/7447) ([Hor911](https://github.com/Hor911)).
* Add YQL syntax highlighting to YDB CLI. [#7448](https://github.com/ydb-platform/ydb/pull/7448) ([Victor Smirnov](https://github.com/vityaman)).
* Support resource pool classifiers objects saving. [#7491](https://github.com/ydb-platform/ydb/pull/7491) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Add database parameter to viewer/tabletinfo handler closes [#7171](https://github.com/ydb-platform/ydb/issues/7171). [#7499](https://github.com/ydb-platform/ydb/pull/7499) ([Alexey Efimov](https://github.com/adameat)).
* ... [#7503](https://github.com/ydb-platform/ydb/pull/7503) ([Alexey Ozeritskiy](https://github.com/resetius)).
* Add spilling stats per task. [#7505](https://github.com/ydb-platform/ydb/pull/7505) ([Vladluk](https://github.com/vladl2802)).
* ... [#7516](https://github.com/ydb-platform/ydb/pull/7516) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#7534](https://github.com/ydb-platform/ydb/pull/7534) ([Sergey Belyakov](https://github.com/serbel324)).
* ... [#7548](https://github.com/ydb-platform/ydb/pull/7548) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#7550](https://github.com/ydb-platform/ydb/pull/7550) ([pilik](https://github.com/pashandor789)).
* ... [#7559](https://github.com/ydb-platform/ydb/pull/7559) ([Filitov Mikhail](https://github.com/lll-phill-lll)).
* ... [#7564](https://github.com/ydb-platform/ydb/pull/7564) ([ya-at](https://github.com/ya-at)).
* ... [#7602](https://github.com/ydb-platform/ydb/pull/7602) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#7605](https://github.com/ydb-platform/ydb/pull/7605) ([Alexey Ozeritskiy](https://github.com/resetius)).
* ... [#7606](https://github.com/ydb-platform/ydb/pull/7606) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#7609](https://github.com/ydb-platform/ydb/pull/7609) ([Alexey Ozeritskiy](https://github.com/resetius)).
* Added decompression support for schema inference (https://st.yandex-team.ru/YQ-3528). [#7632](https://github.com/ydb-platform/ydb/pull/7632) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Collect statistic about unsuccessful block rewrites for callables and types. [#7642](https://github.com/ydb-platform/ydb/pull/7642) ([Andrey Neporada](https://github.com/nepal)).
* Support resource pool classifiers cache in kqp_proxy. [#7688](https://github.com/ydb-platform/ydb/pull/7688) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#7707](https://github.com/ydb-platform/ydb/pull/7707) ([Alexey Ozeritskiy](https://github.com/resetius)).
* Add limit_rows and truncated to viewer/query closes [#7702](https://github.com/ydb-platform/ydb/issues/7702). [#7715](https://github.com/ydb-platform/ydb/pull/7715) ([Alexey Efimov](https://github.com/adameat)).
* Config option for dynamic node registration token. Like config option `StaffApiUserToken` for CMS request. [#7754](https://github.com/ydb-platform/ydb/pull/7754) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* The client receives the code `EES_WRITTEN_IN_TX` in response if he writes a message as part of a transaction. [#7766](https://github.com/ydb-platform/ydb/pull/7766) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* ... [#7794](https://github.com/ydb-platform/ydb/pull/7794) ([Vitaly Stoyan](https://github.com/vitstn)).
* Support filter on DNS names in client cert authentication. [#7797](https://github.com/ydb-platform/ydb/pull/7797) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Tests preparation before resource pool enable. [#7818](https://github.com/ydb-platform/ydb/pull/7818) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Prepared canondata tests before enable resource pools. [#7819](https://github.com/ydb-platform/ydb/pull/7819) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Implement additional state for TKqpDataExecuter in which it will wait for all children Compute Actors for graceful shutdown. [#7829](https://github.com/ydb-platform/ydb/pull/7829) ([Ivan](https://github.com/abyss7)).
* Https://github.com/ydb-platform/ydb/issues/6822 add http-handle returning configs. [#7830](https://github.com/ydb-platform/ydb/pull/7830) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* ... [#7869](https://github.com/ydb-platform/ydb/pull/7869) ([Vitaly Stoyan](https://github.com/vitstn)).
* The options `--use-tx`, `--commit-period` and `--commit-messages` have been added to the `workload topic run write` command. [#7872](https://github.com/ydb-platform/ydb/pull/7872) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* ... [#7895](https://github.com/ydb-platform/ydb/pull/7895) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#7948](https://github.com/ydb-platform/ydb/pull/7948) ([Vitaly Stoyan](https://github.com/vitstn)).
* Support all types of private keys, not only RSA. Set max TLS version to 1.3 instead of 1.2. [#7954](https://github.com/ydb-platform/ydb/pull/7954) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#7972](https://github.com/ydb-platform/ydb/pull/7972) ([pilik](https://github.com/pashandor789)).
* YDBOPS-9806. [#7985](https://github.com/ydb-platform/ydb/pull/7985) ([Artem](https://github.com/ArtemTrofimushkin)).
* Added MaxCommonLogChunks icb parameter for SSD/NVME and HDD. [#8001](https://github.com/ydb-platform/ydb/pull/8001) ([mregrock](https://github.com/mregrock)).
* ... [#8031](https://github.com/ydb-platform/ydb/pull/8031) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#8047](https://github.com/ydb-platform/ydb/pull/8047) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#8058](https://github.com/ydb-platform/ydb/pull/8058) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* ... [#8062](https://github.com/ydb-platform/ydb/pull/8062) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#8094](https://github.com/ydb-platform/ydb/pull/8094) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#8106](https://github.com/ydb-platform/ydb/pull/8106) ([pilik](https://github.com/pashandor789)).
* ... [#8115](https://github.com/ydb-platform/ydb/pull/8115) ([pilik](https://github.com/pashandor789)).
* ... [#8119](https://github.com/ydb-platform/ydb/pull/8119) ([azevaykin](https://github.com/azevaykin)).
* ... [#8167](https://github.com/ydb-platform/ydb/pull/8167) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* Support reading UUIDs from YT tables. [#8179](https://github.com/ydb-platform/ydb/pull/8179) ([Vadim Averin](https://github.com/avevad)).
* New feature in ydb cli: topic consumer describe command. According to RFC: https://github.com/ydb-platform/ydb-rfc/blob/main/cli_topic_consumer_describe.md. [#8221](https://github.com/ydb-platform/ydb/pull/8221) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#8233](https://github.com/ydb-platform/ydb/pull/8233) ([Vitaly Stoyan](https://github.com/vitstn)).
* Allow to alter CDC topic's retention period. [#8264](https://github.com/ydb-platform/ydb/pull/8264) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#8284](https://github.com/ydb-platform/ydb/pull/8284) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* ... [#8287](https://github.com/ydb-platform/ydb/pull/8287) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Fix cors headers, closes [#7906](https://github.com/ydb-platform/ydb/issues/7906). [#8303](https://github.com/ydb-platform/ydb/pull/8303) ([Alexey Efimov](https://github.com/adameat)).
* Add storage/groups latencies and ignore empty vslot status. [#8320](https://github.com/ydb-platform/ydb/pull/8320) ([Alexey Efimov](https://github.com/adameat)).
* ... [#8334](https://github.com/ydb-platform/ydb/pull/8334) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* ... [#8340](https://github.com/ydb-platform/ydb/pull/8340) ([Alexey Ozeritskiy](https://github.com/resetius)).
* ... [#8344](https://github.com/ydb-platform/ydb/pull/8344) ([Vitaly Stoyan](https://github.com/vitstn)).
* Новая логика уровней оптимизаций:. [#8348](https://github.com/ydb-platform/ydb/pull/8348) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* Refactor whiteboard info, to reduce possible footprint and allow to specify which fields are required. [#8366](https://github.com/ydb-platform/ydb/pull/8366) ([Alexey Efimov](https://github.com/adameat)).
* ... [#8424](https://github.com/ydb-platform/ydb/pull/8424) ([Sergey Belyakov](https://github.com/serbel324)).
* ... [#8445](https://github.com/ydb-platform/ydb/pull/8445) ([Oleg Doronin](https://github.com/dorooleg)).
* Pushdown non-separable filters over Aggregate. [#8468](https://github.com/ydb-platform/ydb/pull/8468) ([Andrey Neporada](https://github.com/nepal)).
* ... [#8469](https://github.com/ydb-platform/ydb/pull/8469) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#8472](https://github.com/ydb-platform/ydb/pull/8472) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#8502](https://github.com/ydb-platform/ydb/pull/8502) ([stanislav_shchetinin](https://github.com/stanislav-shchetinin)).
* ... [#8504](https://github.com/ydb-platform/ydb/pull/8504) ([pilik](https://github.com/pashandor789)).
* Fixes [#8513](https://github.com/ydb-platform/ydb/issues/8513). [#8535](https://github.com/ydb-platform/ydb/pull/8535) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#8541](https://github.com/ydb-platform/ydb/pull/8541) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#8554](https://github.com/ydb-platform/ydb/pull/8554) ([pilik](https://github.com/pashandor789)).
* ... [#8599](https://github.com/ydb-platform/ydb/pull/8599) ([Олег](https://github.com/iddqdex)).
* Kqprun support creating tennants. [#8675](https://github.com/ydb-platform/ydb/pull/8675) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#8707](https://github.com/ydb-platform/ydb/pull/8707) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#8742](https://github.com/ydb-platform/ydb/pull/8742) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* ... [#8748](https://github.com/ydb-platform/ydb/pull/8748) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#8848](https://github.com/ydb-platform/ydb/pull/8848) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#8893](https://github.com/ydb-platform/ydb/pull/8893) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* ... [#8912](https://github.com/ydb-platform/ydb/pull/8912) ([Orlov Pavel](https://github.com/OrlovPavel)).
* ... [#8941](https://github.com/ydb-platform/ydb/pull/8941) ([Orlov Pavel](https://github.com/OrlovPavel)).
* Fix decimal output for builtin query requests closes [#8920](https://github.com/ydb-platform/ydb/issues/8920). [#8950](https://github.com/ydb-platform/ydb/pull/8950) ([Alexey Efimov](https://github.com/adameat)).
* ... [#8959](https://github.com/ydb-platform/ydb/pull/8959) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#9002](https://github.com/ydb-platform/ydb/pull/9002) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* ... [#9012](https://github.com/ydb-platform/ydb/pull/9012) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#9040](https://github.com/ydb-platform/ydb/pull/9040) ([Vitaly Stoyan](https://github.com/vitstn)).
* Add microseconds and seconds format in Datetime UDF. [#9081](https://github.com/ydb-platform/ydb/pull/9081) ([Vadim Averin](https://github.com/avevad)).
* ... [#9091](https://github.com/ydb-platform/ydb/pull/9091) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#9112](https://github.com/ydb-platform/ydb/pull/9112) ([Alexey Ozeritskiy](https://github.com/resetius)).
* Add tracing to healthcheck. [#9143](https://github.com/ydb-platform/ydb/pull/9143) ([Alexey Efimov](https://github.com/adameat)).
* Export current_public_dir in test_ya for use in tests in which you want to publish the results in s3 for each retry separately. [#9147](https://github.com/ydb-platform/ydb/pull/9147) ([Vladluk](https://github.com/vladl2802)).
* Fixes [#8658](https://github.com/ydb-platform/ydb/issues/8658). [#9158](https://github.com/ydb-platform/ydb/pull/9158) ([Artem Alekseev](https://github.com/fexolm)).
* Ydb/tests/postgres_integrations/go-libpq/[docker_wrapper_test.py] chunk chunk. [#9160](https://github.com/ydb-platform/ydb/pull/9160) ([Kirill Rysin](https://github.com/naspirato)).
* Fixes [#8659](https://github.com/ydb-platform/ydb/issues/8659). [#9246](https://github.com/ydb-platform/ydb/pull/9246) ([Artem Alekseev](https://github.com/fexolm)).
* Add field `sanitized_token` for audit log. It contains token without signature. [#9287](https://github.com/ydb-platform/ydb/pull/9287) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#9336](https://github.com/ydb-platform/ydb/pull/9336) ([azevaykin](https://github.com/azevaykin)).
* There is a problem in handling operation_timeout parameter during rate limiter request. The ways how in works causes race, when rate limiter can reply OK (and spend resource), but RPC timeout will say to the user that request timeouted. It is much better to support more safe cancel_after parameter < operation_timeout. In this case response will be consistent with quoter service. [#9348](https://github.com/ydb-platform/ydb/pull/9348) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Adds `--emulate-pq` option for dqrun. [#9349](https://github.com/ydb-platform/ydb/pull/9349) ([Fiodar Miron](https://github.com/fedor-miron)).
* GROUP BY HOP now supports static inputs like AS_TABLE. [#9370](https://github.com/ydb-platform/ydb/pull/9370) ([Alexey Pozdniakov](https://github.com/APozdniakov)).
* ... [#9372](https://github.com/ydb-platform/ydb/pull/9372) ([Artem Alekseev](https://github.com/fexolm)).
* Added parameters to `ydb sql` command - Refactored input options. [#9388](https://github.com/ydb-platform/ydb/pull/9388) ([Nikolay Perfilov](https://github.com/pnv1)).
* Add node roles, like: * bootstrapper * statestorage * statestorageboard * schemeboard. [#9413](https://github.com/ydb-platform/ydb/pull/9413) ([Alexey Efimov](https://github.com/adameat)).
* Add session info. [#9420](https://github.com/ydb-platform/ydb/pull/9420) ([Alexey Efimov](https://github.com/adameat)).
* Added query script `execute` and `fetch` handlers post `/query/script/execute` get `/query/script/fetch` - each handler evokes grpc service `queryservice` - changed grpc_services for the work. [#9423](https://github.com/ydb-platform/ydb/pull/9423) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Added recipe for kqprun. [#9453](https://github.com/ydb-platform/ydb/pull/9453) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#9517](https://github.com/ydb-platform/ydb/pull/9517) ([Evgeniy Ivanov](https://github.com/eivanov89)).
* Simple http rate limiter. [#9541](https://github.com/ydb-platform/ydb/pull/9541) ([Alexey Efimov](https://github.com/adameat)).
* Fix nodes type, introduce storage type for nodes. [#9575](https://github.com/ydb-platform/ydb/pull/9575) ([Alexey Efimov](https://github.com/adameat)).
* Pass decimal parameters from KQP and SDK to Datashard and ColumnShard. [#9587](https://github.com/ydb-platform/ydb/pull/9587) ([azevaykin](https://github.com/azevaykin)).
* ... [#9627](https://github.com/ydb-platform/ydb/pull/9627) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* Add setting to configure min delay before node shutdown. [#9688](https://github.com/ydb-platform/ydb/pull/9688) ([Ilia Shakhov](https://github.com/pixcc)).
* ... [#9738](https://github.com/ydb-platform/ydb/pull/9738) ([Sergey Belyakov](https://github.com/serbel324)).
* Improvements in the SDK. The Commit call waits for the topic writing session to receive all Acks. [#9761](https://github.com/ydb-platform/ydb/pull/9761) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* YDB FQ: Connector filtering modes. [#9778](https://github.com/ydb-platform/ydb/pull/9778) ([Vitaly Isaev](https://github.com/vitalyisaev2)).
* Implement resource pool weights. [#9839](https://github.com/ydb-platform/ydb/pull/9839) ([Mikhail Surin](https://github.com/ssmike)).
* You can use `TTxControl` to commit a transaction. The SDK waits for the recording session to receive all ACKs for written messages. [#9890](https://github.com/ydb-platform/ydb/pull/9890) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Add cpus info to cluster handler. [#9896](https://github.com/ydb-platform/ydb/pull/9896) ([Alexey Efimov](https://github.com/adameat)).
* Enable 3 modes for Arrow memory tracking: - serialization-deserialization (default) - deep-copy - no tracking. [#9951](https://github.com/ydb-platform/ydb/pull/9951) ([Ivan](https://github.com/abyss7)).
* ... [#9959](https://github.com/ydb-platform/ydb/pull/9959) ([Artem Alekseev](https://github.com/fexolm)).
* Make block combine hashed use stream instead of flow. [#9979](https://github.com/ydb-platform/ydb/pull/9979) ([Vladluk](https://github.com/vladl2802)).
* ... [#10033](https://github.com/ydb-platform/ydb/pull/10033) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* ... [#10058](https://github.com/ydb-platform/ydb/pull/10058) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* ... [#10065](https://github.com/ydb-platform/ydb/pull/10065) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* Fix nodes grouping and uptime calculations. [#10075](https://github.com/ydb-platform/ydb/pull/10075) ([Alexey Efimov](https://github.com/adameat)).
* ... [#10117](https://github.com/ydb-platform/ydb/pull/10117) ([Vitaly Stoyan](https://github.com/vitstn)).
* Support output for audit logs siilar to json log format for usual debug logs. [#10143](https://github.com/ydb-platform/ydb/pull/10143) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* YDB FQ: set up filtering options for YQL Generic Read Actor and Lookup Actor. [#10161](https://github.com/ydb-platform/ydb/pull/10161) ([Vitaly Isaev](https://github.com/vitalyisaev2)).
* Add rate limiting settings to http. [#10164](https://github.com/ydb-platform/ydb/pull/10164) ([Alexey Efimov](https://github.com/adameat)).
* Add hint for compact Join. [#10236](https://github.com/ydb-platform/ydb/pull/10236) ([Vadim Averin](https://github.com/avevad)).
* Switch to json2proto to allow decode of any. [#10269](https://github.com/ydb-platform/ydb/pull/10269) ([Alexey Efimov](https://github.com/adameat)).
* ... [#10402](https://github.com/ydb-platform/ydb/pull/10402) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* Add ydb2 schema, add some crazy types to render to json closes [#8043](https://github.com/ydb-platform/ydb/issues/8043). [#10443](https://github.com/ydb-platform/ydb/pull/10443) ([Alexey Efimov](https://github.com/adameat)).
* Follower statistics is passed: * datashard; * schemeshard; * sys_view partition_stats. [#10482](https://github.com/ydb-platform/ydb/pull/10482) ([azevaykin](https://github.com/azevaykin)).
* ... [#10509](https://github.com/ydb-platform/ydb/pull/10509) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* Add node name filter, improve filter behavior closes [#10554](https://github.com/ydb-platform/ydb/issues/10554). [#10585](https://github.com/ydb-platform/ydb/pull/10585) ([Alexey Efimov](https://github.com/adameat)).
* `AFTER MATCH SKIP PAST LAST ROW` is default option now. [#10597](https://github.com/ydb-platform/ydb/pull/10597) ([Alexey Pozdniakov](https://github.com/APozdniakov)).
* Added new field COMPRESSION_LEVEL in Column Family. [#10645](https://github.com/ydb-platform/ydb/pull/10645) ([Vladislav Gogov](https://github.com/vlad-gogov)).
* Added database & node_id for logging backend. [#10666](https://github.com/ydb-platform/ydb/pull/10666) ([Alexander Petrukhin](https://github.com/shmel1k)).
* Log events during backup/restore. [#10681](https://github.com/ydb-platform/ydb/pull/10681) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Add memorydetailed field to viewer/nodes handler. [#10694](https://github.com/ydb-platform/ydb/pull/10694) ([Alexey Efimov](https://github.com/adameat)).
* ... [#10752](https://github.com/ydb-platform/ydb/pull/10752) ([azevaykin](https://github.com/azevaykin)).
* Add setting of external traces' detalization level to tracing config. [#10784](https://github.com/ydb-platform/ydb/pull/10784) ([Sergey Belyakov](https://github.com/serbel324)).
* ... [#10800](https://github.com/ydb-platform/ydb/pull/10800) ([beehelit](https://github.com/beehelit)).
* ... [#10842](https://github.com/ydb-platform/ydb/pull/10842) ([Vitaly Stoyan](https://github.com/vitstn)).
* Sys columns support for YT map block input mode. [#10844](https://github.com/ydb-platform/ydb/pull/10844) ([Mark Ziganshin](https://github.com/loochek)).
* Follower statistics is passed: * datashard; * schemeshard; * sys_view partition_stats; * sys_view top_partitions_one_minute; * sys_view top_partitions_one_hour. [#10849](https://github.com/ydb-platform/ydb/pull/10849) ([azevaykin](https://github.com/azevaykin)).
* ... [#10883](https://github.com/ydb-platform/ydb/pull/10883) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* Implement intermixed inplace and huge blobs and add test for this case. [#10973](https://github.com/ydb-platform/ydb/pull/10973) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Extend network diagnostics. [#10981](https://github.com/ydb-platform/ydb/pull/10981) ([Alexey Efimov](https://github.com/adameat)).
* Calculate disconnections in last hour. [#11007](https://github.com/ydb-platform/ydb/pull/11007) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#11015](https://github.com/ydb-platform/ydb/pull/11015) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#11155](https://github.com/ydb-platform/ydb/pull/11155) ([Sergey Belyakov](https://github.com/serbel324)).
* ... [#11189](https://github.com/ydb-platform/ydb/pull/11189) ([azevaykin](https://github.com/azevaykin)).
* Add fetch and replace public api. [#11313](https://github.com/ydb-platform/ydb/pull/11313) ([mregrock](https://github.com/mregrock)).
* Add network diagnostics columns to viewer/nodes handler. [#11344](https://github.com/ydb-platform/ydb/pull/11344) ([Alexey Efimov](https://github.com/adameat)).
* ... [#11393](https://github.com/ydb-platform/ydb/pull/11393) ([Evgeniy Ivanov](https://github.com/eivanov89)).
* ... [#11411](https://github.com/ydb-platform/ydb/pull/11411) ([Artem Alekseev](https://github.com/fexolm)).
* Https://nebius.atlassian.net/browse/nbydb-594. [#11449](https://github.com/ydb-platform/ydb/pull/11449) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Support the configuration setting to wrap log records into a fixed json envelope, based on the log record nature. To be used when a single-stream unified logs delivery system is in place (like stderr in k8s installations), with all logs streamed there (including audit), and which needs to have some environment-specific information in the message to decide which system to forward a particular record to. [#11466](https://github.com/ydb-platform/ydb/pull/11466) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#11546](https://github.com/ydb-platform/ydb/pull/11546) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* ... [#11585](https://github.com/ydb-platform/ydb/pull/11585) ([Oleg Doronin](https://github.com/dorooleg)).
* A new balancing option "group_slots" has been added, which enables uniform distribution of VDisks belonging to specific storage groups or storage pool across PDisks. [#11589](https://github.com/ydb-platform/ydb/pull/11589) ([kruall](https://github.com/kruall)).
* ... [#11590](https://github.com/ydb-platform/ydb/pull/11590) ([Sergey Belyakov](https://github.com/serbel324)).
* If the `blobstorage_config` section is omitted, use distconf. Introduce `fail_domain_type` setting that's useful for the 3-node cluster case. [#11632](https://github.com/ydb-platform/ydb/pull/11632) ([Ivan Blinkov](https://github.com/blinkov)).
* ... [#11675](https://github.com/ydb-platform/ydb/pull/11675) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* Report CPU consumtion of TSkeleton actor. [#11719](https://github.com/ydb-platform/ydb/pull/11719) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Datashard reports statistics about its locks. [#11731](https://github.com/ydb-platform/ydb/pull/11731) ([azevaykin](https://github.com/azevaykin)).
* Add support for ydbd server start with dynconfig (config with metadata and selectors). [#11745](https://github.com/ydb-platform/ydb/pull/11745) ([mregrock](https://github.com/mregrock)).
* ... [#11759](https://github.com/ydb-platform/ydb/pull/11759) ([Arseny](https://github.com/what-the-fawk)).
* YDB FQ: support Logging as an external data source. [#11765](https://github.com/ydb-platform/ydb/pull/11765) ([Vitaly Isaev](https://github.com/vitalyisaev2)).
* ... [#11771](https://github.com/ydb-platform/ydb/pull/11771) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#11786](https://github.com/ydb-platform/ydb/pull/11786) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#11925](https://github.com/ydb-platform/ydb/pull/11925) ([Alexey Efimov](https://github.com/adameat)).
* Added the ability to check users' passwords whenever they are set with `CREATE USER` and `ALTER USER` Were added following checks: - Minimum password length - Passwords must include a lowercase character - Passwords must include an uppercase character - Passwords must include a number - Passwords must include a special character from list `!@#$%^&*()_+{}|<>?=` All checks can be enabled or disabled over configuration. [#11963](https://github.com/ydb-platform/ydb/pull/11963) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Works in the memory profiling mode only. [#11968](https://github.com/ydb-platform/ydb/pull/11968) ([Ivan](https://github.com/abyss7)).
* ... [#12042](https://github.com/ydb-platform/ydb/pull/12042) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#12044](https://github.com/ydb-platform/ydb/pull/12044) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#12048](https://github.com/ydb-platform/ydb/pull/12048) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* ... [#12075](https://github.com/ydb-platform/ydb/pull/12075) ([Alexey Efimov](https://github.com/adameat)).
* ... [#12262](https://github.com/ydb-platform/ydb/pull/12262) ([Oleg Doronin](https://github.com/dorooleg)).
* Added a backup of changefeeds when calling the tools dump command in the ydb cli. [#12283](https://github.com/ydb-platform/ydb/pull/12283) ([stanislav_shchetinin](https://github.com/stanislav-shchetinin)).
* ... [#12286](https://github.com/ydb-platform/ydb/pull/12286) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* Add ydb cli replace and fetch commands into ydb_cli. [#12312](https://github.com/ydb-platform/ydb/pull/12312) ([mregrock](https://github.com/mregrock)).
* Valid link https://hub.docker.com/r/ydbplatform/local-ydb. [#12371](https://github.com/ydb-platform/ydb/pull/12371) ([Vladislav Polyakov](https://github.com/polRk)).
* ... [#12374](https://github.com/ydb-platform/ydb/pull/12374) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#12405](https://github.com/ydb-platform/ydb/pull/12405) ([Semyon](https://github.com/swalrus1)).
* Implement GetBlockRequest. [#12431](https://github.com/ydb-platform/ydb/pull/12431) ([mregrock](https://github.com/mregrock)).
* ... [#12521](https://github.com/ydb-platform/ydb/pull/12521) ([kungurtsev](https://github.com/kunga)).
* Changed the default compression to LZ4 - Added the ability to change the default compression through the CS configuration. - If compression is not specified for a column in a schema, plain compression will not be specified. - Added error checking if compression level is set but compression type is not specified. [#12542](https://github.com/ydb-platform/ydb/pull/12542) ([Vladislav Gogov](https://github.com/vlad-gogov)).
* ... [#12544](https://github.com/ydb-platform/ydb/pull/12544) ([Alexey Efimov](https://github.com/adameat)).
* ... [#12563](https://github.com/ydb-platform/ydb/pull/12563) ([Oleg Doronin](https://github.com/dorooleg)).
* `ydb import file csv` command now saves import progress. Relaunching import command will continue from the line it was interrupted on. [#12570](https://github.com/ydb-platform/ydb/pull/12570) ([Nikolay Perfilov](https://github.com/pnv1)).
* Automatically account lockout after some attempts to login with wrong password. User is unlocked after `AttemptResetDuration` time in config. If `AttemptResetDuration` is 0 then user is locked out permanently. [#12578](https://github.com/ydb-platform/ydb/pull/12578) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Support tracing feature in topic write session. There are three commands in write session: init, write and update token requests. For all these commands we generate separate sampled traces as for single grpc requests. [#12649](https://github.com/ydb-platform/ydb/pull/12649) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Addi BSC/Console interaction protocol for single config replacement. [#12662](https://github.com/ydb-platform/ydb/pull/12662) ([mregrock](https://github.com/mregrock)).
* ... [#12664](https://github.com/ydb-platform/ydb/pull/12664) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#12730](https://github.com/ydb-platform/ydb/pull/12730) ([Oleg Doronin](https://github.com/dorooleg)).
* Ydb/apps/ydb/ut ydbworkloadtopic.full_statistics_usetx. [#12786](https://github.com/ydb-platform/ydb/pull/12786) ([Kirill Rysin](https://github.com/naspirato)).
* Added BSController transaction to stop PDisk - Added new PDisk state `Stopped`. [#12799](https://github.com/ydb-platform/ydb/pull/12799) ([Semyon Danilov](https://github.com/SammyVimes)).
* Snapshot Isolation. [#12825](https://github.com/ydb-platform/ydb/pull/12825) ([Nikita Vasilev](https://github.com/nikvas0)).
* Export changefeed's configuration to s3. [#12882](https://github.com/ydb-platform/ydb/pull/12882) ([stanislav_shchetinin](https://github.com/stanislav-shchetinin)).
* ... [#12897](https://github.com/ydb-platform/ydb/pull/12897) ([Dmitry O](https://github.com/alephonea)).
* Add validation of backup file checksums during importing from S3. [#12909](https://github.com/ydb-platform/ydb/pull/12909) ([Ilia Shakhov](https://github.com/pixcc)).
* ... [#12946](https://github.com/ydb-platform/ydb/pull/12946) ([SloNN](https://github.com/SloNN)).
* New option in query: CREATE USER user LOGIN; CREATE USER user NOLOGIN; ALTER USER user LOGIN; ALTER USER user NOLOGIN;. [#12957](https://github.com/ydb-platform/ydb/pull/12957) ([flown4qqqq](https://github.com/flown4qqqq)).
* ... [#12962](https://github.com/ydb-platform/ydb/pull/12962) ([Alexey Efimov](https://github.com/adameat)).
* This control from Immediate Control Board was interfering with tcmalloc's default memory soft limit from MemoryController - since I found no way to combine both I have to remove the control. [#13008](https://github.com/ydb-platform/ydb/pull/13008) ([Ivan](https://github.com/abyss7)).
* Https://st.yandex-team.ru/yq-4000. [#13028](https://github.com/ydb-platform/ydb/pull/13028) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#13046](https://github.com/ydb-platform/ydb/pull/13046) ([Oleg Doronin](https://github.com/dorooleg)).
* Remove verify that checks generation increases by one. [#13076](https://github.com/ydb-platform/ydb/pull/13076) ([mregrock](https://github.com/mregrock)).
* New oidc handler for cleaning cookie. [#13097](https://github.com/ydb-platform/ydb/pull/13097) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Support Console interoperation through distconf. [#13109](https://github.com/ydb-platform/ydb/pull/13109) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Add block-4-2-4-nodes and block-4-2-2-nodes erasure types for ydbd_slice. [#13163](https://github.com/ydb-platform/ydb/pull/13163) ([Alexander Petrukhin](https://github.com/shmel1k)).
* Use discovery for kafka proxy port (instead of single port assigned in configs). ... [#13197](https://github.com/ydb-platform/ydb/pull/13197) ([FloatingCrowbar](https://github.com/FloatingCrowbar)).
* Default compression setting via CS config and its validation. [#13203](https://github.com/ydb-platform/ydb/pull/13203) ([Vladislav Gogov](https://github.com/vlad-gogov)).
* Add erasure none for slices. [#13208](https://github.com/ydb-platform/ydb/pull/13208) ([Alexander Petrukhin](https://github.com/shmel1k)).
* Added CREATE TABLE text suggestion on scheme error during `ydb import file csv`. [#13247](https://github.com/ydb-platform/ydb/pull/13247) ([Nikolay Perfilov](https://github.com/pnv1)).
* Add top-level security config declaration. [#13273](https://github.com/ydb-platform/ydb/pull/13273) ([mregrock](https://github.com/mregrock)).
* ... [#13307](https://github.com/ydb-platform/ydb/pull/13307) ([Alexey Efimov](https://github.com/adameat)).
* ... [#13371](https://github.com/ydb-platform/ydb/pull/13371) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* Also fix heap-use-after-free for failed allocation backtrace. [#13376](https://github.com/ydb-platform/ydb/pull/13376) ([Ivan](https://github.com/abyss7)).
* ... [#13389](https://github.com/ydb-platform/ydb/pull/13389) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* Adds streaming support to viewer query executions, closes [#13327](https://github.com/ydb-platform/ydb/issues/13327). [#13488](https://github.com/ydb-platform/ydb/pull/13488) ([Alexey Efimov](https://github.com/adameat)).
* Usage example: ```text StorageLoad: { DurationSeconds: 300000 Tablets: { Tablets: { TabletName: "Loader" Channel: 4 GroupId: 2181038080 Generation: 1 } Tablets: { TabletName: "Loader" Channel: 5 GroupId: 2181038081 Generation: 1 } Tablets: { TabletName: "Loader" Channel: 6 GroupId: 2181038082 Generation: 1 } Tablets: { TabletName: "Loader" Channel: 7 GroupId: 2181038083 Generation: 1 } Tablets: { TabletName: "Loader" Channel: 8 GroupId: 2181038084 Generation: 1 } Tablets: { TabletName: "Loader" Channel: 9 GroupId: 2181038085 Generation: 1 } Tablets: { TabletName: "Loader" Channel: 10 GroupId: 2181038086 Generation: 1 } Tablets: { TabletName: "Loader" Channel: 11 GroupId: 2181038087 Generation: 1 }. [#13547](https://github.com/ydb-platform/ydb/pull/13547) ([Sergey Belyakov](https://github.com/serbel324)).
* Add network utilization aggregate. [#13550](https://github.com/ydb-platform/ydb/pull/13550) ([Alexey Efimov](https://github.com/adameat)).
* ... [#13680](https://github.com/ydb-platform/ydb/pull/13680) ([Alexander Avdonkin](https://github.com/aavdonkin)).
* The new sensor name is "Stats/MemMapsCount". [#13758](https://github.com/ydb-platform/ydb/pull/13758) ([Ivan](https://github.com/abyss7)).
* ... [#13768](https://github.com/ydb-platform/ydb/pull/13768) ([Oleg Doronin](https://github.com/dorooleg)).
* Add command line option for kafka ports. [#13799](https://github.com/ydb-platform/ydb/pull/13799) ([FloatingCrowbar](https://github.com/FloatingCrowbar)).

### Performance improvement
* ... [#6333](https://github.com/ydb-platform/ydb/pull/6333) ([Roman Udovichenko](https://github.com/rvu1024)).
* Permanently enable extended payload format generation. [#6434](https://github.com/ydb-platform/ydb/pull/6434) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Do not trigger tablet balancer when all nodes have high usage. [#6532](https://github.com/ydb-platform/ydb/pull/6532) ([vporyadke](https://github.com/vporyadke)).
* Added milestone queue in replication to reduce work unit computations. [#6561](https://github.com/ydb-platform/ydb/pull/6561) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#6705](https://github.com/ydb-platform/ydb/pull/6705) ([yumkam](https://github.com/yumkam)).
* ... [#6753](https://github.com/ydb-platform/ydb/pull/6753) ([Oleg Doronin](https://github.com/dorooleg)).
* Make less coordinator&mediator moves. [#6840](https://github.com/ydb-platform/ydb/pull/6840) ([vporyadke](https://github.com/vporyadke)).
* ... [#6951](https://github.com/ydb-platform/ydb/pull/6951) ([yumkam](https://github.com/yumkam)).
* Optimize tenantinfo handler add trace spans. [#7699](https://github.com/ydb-platform/ydb/pull/7699) ([Alexey Efimov](https://github.com/adameat)).
* ... [#8146](https://github.com/ydb-platform/ydb/pull/8146) ([yumkam](https://github.com/yumkam)).
* Closes [#8382](https://github.com/ydb-platform/ydb/issues/8382). [#8619](https://github.com/ydb-platform/ydb/pull/8619) ([Alexey Efimov](https://github.com/adameat)).
* Fix autocomplete to work with directories, optimize a little. [#9074](https://github.com/ydb-platform/ydb/pull/9074) ([Alexey Efimov](https://github.com/adameat)).
* ... [#9099](https://github.com/ydb-platform/ydb/pull/9099) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Little optimizations for healthcheck. [#9221](https://github.com/ydb-platform/ydb/pull/9221) ([Alexey Efimov](https://github.com/adameat)).
* ... [#9298](https://github.com/ydb-platform/ydb/pull/9298) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Pre-serialize topic's bootstrap config. [#9331](https://github.com/ydb-platform/ydb/pull/9331) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#9332](https://github.com/ydb-platform/ydb/pull/9332) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Disable blob header by default in VDisk. [#9491](https://github.com/ydb-platform/ydb/pull/9491) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#9572](https://github.com/ydb-platform/ydb/pull/9572) ([yumkam](https://github.com/yumkam)).
* Fix buggy IC setting leading to performance degradation. [#9707](https://github.com/ydb-platform/ydb/pull/9707) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#9715](https://github.com/ydb-platform/ydb/pull/9715) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* PDisk will choose different BufferPool sizes based on underlying device type - it's important for NVMe to have more buffers with less size. [#9865](https://github.com/ydb-platform/ydb/pull/9865) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Parse CDC topic's partitioning once and more efficiently. [#9914](https://github.com/ydb-platform/ydb/pull/9914) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Improved connection loss handling in Change Data Capture. [#9993](https://github.com/ydb-platform/ydb/pull/9993) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#10085](https://github.com/ydb-platform/ydb/pull/10085) ([Nikolay Shestakov](https://github.com/nshestakov)).
* ... [#10130](https://github.com/ydb-platform/ydb/pull/10130) ([yumkam](https://github.com/yumkam)).
* Optimized batch processing in Topics. [#10131](https://github.com/ydb-platform/ydb/pull/10131) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Added simdjson parser into RD. [#10204](https://github.com/ydb-platform/ydb/pull/10204) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Disable pipe retries by default. [#10238](https://github.com/ydb-platform/ydb/pull/10238) ([Alexey Efimov](https://github.com/adameat)).
* The `UpdateOffsetsInTransaction` method is retrieved once before COMMIT. [#10273](https://github.com/ydb-platform/ydb/pull/10273) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* ... [#10288](https://github.com/ydb-platform/ydb/pull/10288) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* Added messages accumulating. [#10380](https://github.com/ydb-platform/ydb/pull/10380) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Support of block input in map operations jobs (using Arrow input format provided by YT). [#10587](https://github.com/ydb-platform/ydb/pull/10587) ([Mark Ziganshin](https://github.com/loochek)).
* Query service: optimize result passing over trailing results. [#10690](https://github.com/ydb-platform/ydb/pull/10690) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* Passed UV from parser to filter. [#10721](https://github.com/ydb-platform/ydb/pull/10721) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* The PQ tablet can perform transactions in parallel. [#10885](https://github.com/ydb-platform/ydb/pull/10885) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Optimize hive start time. [#10969](https://github.com/ydb-platform/ydb/pull/10969) ([vporyadke](https://github.com/vporyadke)).
* ... [#11010](https://github.com/ydb-platform/ydb/pull/11010) ([Aleksei Borzenkov](https://github.com/snaury)).
* Enabled LLVM in purecalc filters. [#11442](https://github.com/ydb-platform/ydb/pull/11442) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Increased ydb import file csv throughput approximately from 40 to 70 MiB/s. [#11679](https://github.com/ydb-platform/ydb/pull/11679) ([Nikolay Perfilov](https://github.com/pnv1)).
* Increased ydb import file csv throughput approximately from 70 to 90 MiB/s. [#11864](https://github.com/ydb-platform/ydb/pull/11864) ([Nikolay Perfilov](https://github.com/pnv1)).
* ... [#11872](https://github.com/ydb-platform/ydb/pull/11872) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* Increased ydb import file csv throughput approximately from 90 to 130 MiB/s. [#11907](https://github.com/ydb-platform/ydb/pull/11907) ([Nikolay Perfilov](https://github.com/pnv1)).
* Removed mutex for purecalc compilation. [#12136](https://github.com/ydb-platform/ydb/pull/12136) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Now we are giving all messages to the end of the blob in which they are stored to reduce the load when reading small messages. [#12153](https://github.com/ydb-platform/ydb/pull/12153) ([Nikolay Shestakov](https://github.com/nshestakov)).
* Enhanced parallelism of data restoring in `ydb tools restore`. [#12203](https://github.com/ydb-platform/ydb/pull/12203) ([Ilia Shakhov](https://github.com/pixcc)).
* Previous pr - https://github.com/ydb-platform/ydb/pull/9332. [#12366](https://github.com/ydb-platform/ydb/pull/12366) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Use new YQL mechanic for the Arrow buffer resize - to shrink in 100% of times when consuming blocks for DqOutput. Otherwise we get over-allocated buffers with very small accounted logical size - it leads to OOMs. [#12373](https://github.com/ydb-platform/ydb/pull/12373) ([Ivan](https://github.com/abyss7)).
* Added parallel purecalc compilation and abort requests. [#12505](https://github.com/ydb-platform/ydb/pull/12505) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Add caching for `ListNodes` request in `DynamicNameserver`. [#12694](https://github.com/ydb-platform/ydb/pull/12694) ([Ilia Shakhov](https://github.com/pixcc)).
* Node TNodeLocation processing to NodeWarden in order to reduce CPU consumption. [#12776](https://github.com/ydb-platform/ydb/pull/12776) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#13174](https://github.com/ydb-platform/ydb/pull/13174) ([Maksim Zinal](https://github.com/zinal)).

### Experimental feature
* Support for UPDATE operation in EvWrite. [#6339](https://github.com/ydb-platform/ydb/pull/6339) ([azevaykin](https://github.com/azevaykin)).
* Syntax for creating vector index ```sql ALTER TABLE table ADD INDEX idx GLOBAL USING vector_kmeans_tree ON (col) COVER (col) WITH (key=value) ```. [#6602](https://github.com/ydb-platform/ydb/pull/6602) ([azevaykin](https://github.com/azevaykin)).
* ColumnShard + Datashard Reads. [#6800](https://github.com/ydb-platform/ydb/pull/6800) ([Nikita Vasilev](https://github.com/nikvas0)).
* ... [#6877](https://github.com/ydb-platform/ydb/pull/6877) ([Oleg Doronin](https://github.com/dorooleg)).
* Partial implementation of https://github.com/ydb-platform/ydb-rfc/blob/main/0104_incr-backup-sql.md Add basic (create/alter/drop) `BACKUP COLLECTION` entity with settings. [#7255](https://github.com/ydb-platform/ydb/pull/7255) ([Innokentii Mokin](https://github.com/Enjection)).
* Support for new granular timecast protocol in mediator tablets. [#7986](https://github.com/ydb-platform/ydb/pull/7986) ([Aleksei Borzenkov](https://github.com/snaury)).
* Use granular mediator time that is not blocked by other tablets. [#8090](https://github.com/ydb-platform/ydb/pull/8090) ([Aleksei Borzenkov](https://github.com/snaury)).
* ... [#8147](https://github.com/ydb-platform/ydb/pull/8147) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* ... [#8400](https://github.com/ydb-platform/ydb/pull/8400) ([Aleksei Borzenkov](https://github.com/snaury)).
* ExtractCommonPredicatesFromLogicalOps setting and optimizers. [#8570](https://github.com/ydb-platform/ydb/pull/8570) ([Andrey Neporada](https://github.com/nepal)).
* ... [#9003](https://github.com/ydb-platform/ydb/pull/9003) ([Aleksei Borzenkov](https://github.com/snaury)).
* Support for DISTINCT clause for aggregation functions calculated over window. [#9090](https://github.com/ydb-platform/ydb/pull/9090) ([Mark Ziganshin](https://github.com/loochek)).
* Exporting CMake with skip platforms with errors. [#10067](https://github.com/ydb-platform/ydb/pull/10067) ([Dmitrii Dmitriev](https://github.com/dimdim1177)).
* Feature flag `enable_antlr4_parser` helps to enable the ANTLRv4 parser inside docker container local-ydb. [#11764](https://github.com/ydb-platform/ydb/pull/11764) ([Aleksey Myasnikov](https://github.com/asmyasnikov)).
* This config option propagates inside Dq internals. For Kqp it's set to 100% by default to force copying of underlying buffers. [#12520](https://github.com/ydb-platform/ydb/pull/12520) ([Ivan](https://github.com/abyss7)).
* ... [#12733](https://github.com/ydb-platform/ydb/pull/12733) ([Aleksey Myasnikov](https://github.com/asmyasnikov)).
* Added new `ydb debug latency` kind `ActorChain`. [#12917](https://github.com/ydb-platform/ydb/pull/12917) ([Evgeniy Ivanov](https://github.com/eivanov89)).
* Add log_config and better templating for ydbd_slice. [#12956](https://github.com/ydb-platform/ydb/pull/12956) ([Alexander Petrukhin](https://github.com/shmel1k)).
* Link udf function 'roaring'. [#13071](https://github.com/ydb-platform/ydb/pull/13071) ([azevaykin](https://github.com/azevaykin)).

### Bugfix
* Fixed default for --null-value in ydb import file csv/tsv commands and improved error text. [#3936](https://github.com/ydb-platform/ydb/pull/3936) ([Bulat](https://github.com/Gazizonoki)).
* Do not use write lock in ICB when read lock is enough. Use swap to prevent read-check-write races. [#5289](https://github.com/ydb-platform/ydb/pull/5289) ([Cthulhu](https://github.com/the-ancient-1)).
* Implement a deadline for patching request stages to facilitate a rapid fallback process. [#5677](https://github.com/ydb-platform/ydb/pull/5677) ([kruall](https://github.com/kruall)).
* ... [#6152](https://github.com/ydb-platform/ydb/pull/6152) ([yumkam](https://github.com/yumkam)).
* `TDecompressionTask` stores a weak reference to `TDataDecompressionInfo` and if the Parent has already been deleted, it does nothing. [#6249](https://github.com/ydb-platform/ydb/pull/6249) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fill change exchange split & activation lists just before commit. [#6281](https://github.com/ydb-platform/ydb/pull/6281) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Fix HMAC secret key loading for OAuth 2.0 token exchange config HMAC key is binary data, so it must be loaded from json in base64 encoding (in Go SDK it is already done properly). [#6290](https://github.com/ydb-platform/ydb/pull/6290) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Fix build after removing generate_patch.sh. [#6331](https://github.com/ydb-platform/ydb/pull/6331) ([Andrey Neporada](https://github.com/nepal)).
* Temporarily disable FilterPushdownEnableMultiusage. [#6347](https://github.com/ydb-platform/ydb/pull/6347) ([Andrey Neporada](https://github.com/nepal)).
* ... [#6355](https://github.com/ydb-platform/ydb/pull/6355) ([kruall](https://github.com/kruall)).
* Build only postgresql sources in verify.sh. [#6361](https://github.com/ydb-platform/ydb/pull/6361) ([Andrey Neporada](https://github.com/nepal)).
* Fix unpatched global vars. [#6362](https://github.com/ydb-platform/ydb/pull/6362) ([Andrey Neporada](https://github.com/nepal)).
* Proper (de)serialization of structs, optionals and variants. [#6396](https://github.com/ydb-platform/ydb/pull/6396) ([Vadim Averin](https://github.com/avevad)).
* Handle empty GC commands correctly. [#6398](https://github.com/ydb-platform/ydb/pull/6398) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fix bugs in coordinator state migration. [#6401](https://github.com/ydb-platform/ydb/pull/6401) ([Aleksei Borzenkov](https://github.com/snaury)).
* Fix VDisk replication stuck sensor bug. [#6405](https://github.com/ydb-platform/ydb/pull/6405) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#6409](https://github.com/ydb-platform/ydb/pull/6409) ([vporyadke](https://github.com/vporyadke)).
* ... [#6414](https://github.com/ydb-platform/ydb/pull/6414) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#6432](https://github.com/ydb-platform/ydb/pull/6432) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix problem with empty errors in http handlers. [#6441](https://github.com/ydb-platform/ydb/pull/6441) ([Alexey Efimov](https://github.com/adameat)).
* The PQ tablet sent a response to the SS. At that moment, `Hive' was running it on another node. The tablet was restored to the WAIT_RS state and waited for predicates from other participants. [#6449](https://github.com/ydb-platform/ydb/pull/6449) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Previously, errors from spilling caused a deadlock. Error handling has now been added. [#6454](https://github.com/ydb-platform/ydb/pull/6454) ([Filitov Mikhail](https://github.com/lll-phill-lll)).
* Fix a bug where tablets could get stuck in boot queue. [#6491](https://github.com/ydb-platform/ydb/pull/6491) ([vporyadke](https://github.com/vporyadke)).
* Fix a bug where tablets total counter was not updated on followers deletion. [#6492](https://github.com/ydb-platform/ydb/pull/6492) ([vporyadke](https://github.com/vporyadke)).
* ... [#6497](https://github.com/ydb-platform/ydb/pull/6497) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Fix null pointer dereference during node registration in `Node Broker`. [#6516](https://github.com/ydb-platform/ydb/pull/6516) ([Ilia Shakhov](https://github.com/pixcc)).
* ... [#6521](https://github.com/ydb-platform/ydb/pull/6521) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix getting oauth2 key file credentials from environment. Silly error. [#6550](https://github.com/ydb-platform/ydb/pull/6550) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#6585](https://github.com/ydb-platform/ydb/pull/6585) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#6586](https://github.com/ydb-platform/ydb/pull/6586) ([vporyadke](https://github.com/vporyadke)).
* Continue to emit resolved timestamp after table merge. [#6594](https://github.com/ydb-platform/ydb/pull/6594) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Fix a bug where some nodes could remain down after a downgrade. [#6613](https://github.com/ydb-platform/ydb/pull/6613) ([vporyadke](https://github.com/vporyadke)).
* Changed memory calculation for TEvFreeItems. [#6625](https://github.com/ydb-platform/ydb/pull/6625) ([mregrock](https://github.com/mregrock)).
* Fixed endless retries for external error. [#6626](https://github.com/ydb-platform/ydb/pull/6626) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#6634](https://github.com/ydb-platform/ydb/pull/6634) ([Roman Udovichenko](https://github.com/rvu1024)).
* YDB FQ: distinguish dedicated and serverless YDBs via 'storageConfig' section. [#6703](https://github.com/ydb-platform/ydb/pull/6703) ([Vitaly Isaev](https://github.com/vitalyisaev2)).
* ... [#6711](https://github.com/ydb-platform/ydb/pull/6711) ([yumkam](https://github.com/yumkam)).
* Fixed error failed to execute callable ResWrite. [#6752](https://github.com/ydb-platform/ydb/pull/6752) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix handling of backups of too massive databases (in terms of number of tables and number of table partitions). [#6760](https://github.com/ydb-platform/ydb/pull/6760) ([ijon](https://github.com/ijon)).
* Disable outgoing cache for mvp meta. [#6806](https://github.com/ydb-platform/ydb/pull/6806) ([Alexey Efimov](https://github.com/adameat)).
* ... [#6821](https://github.com/ydb-platform/ydb/pull/6821) ([Anton Martsenyuk](https://github.com/antoniox)).
* The PQ tablet performed the transaction. I received the value of the predicate from the partition and waited for RS from other tablets. At this time, Hive was restarting it on another node. After the restart, the tablet restored the transaction and continued to execute it. I received all RS and sent the message `TEvTxCommit` to the partition. As a result, the program crashed, since the partition did not know anything about this transaction after the restart. [#6831](https://github.com/ydb-platform/ydb/pull/6831) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* ... [#6846](https://github.com/ydb-platform/ydb/pull/6846) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#6881](https://github.com/ydb-platform/ydb/pull/6881) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#6894](https://github.com/ydb-platform/ydb/pull/6894) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix for dead nodes always passing filter fixes [#6608](https://github.com/ydb-platform/ydb/issues/6608). [#6912](https://github.com/ydb-platform/ydb/pull/6912) ([Alexey Efimov](https://github.com/adameat)).
* Don't make a lock on zero memory change. [#6926](https://github.com/ydb-platform/ydb/pull/6926) ([Vitalii Gridnev](https://github.com/gridnevvvit)).
* ... [#6930](https://github.com/ydb-platform/ydb/pull/6930) ([Innokentii Mokin](https://github.com/Enjection)).
* ... [#6941](https://github.com/ydb-platform/ydb/pull/6941) ([Andrey Molotkov](https://github.com/molotkov-and)).
* YDB FQ: avoid outdated syntax "SELECT * FROM cluster.db.table" (now database name is always within cluster). [#6945](https://github.com/ydb-platform/ydb/pull/6945) ([Grigorii Papashvili](https://github.com/lifthelm)).
* ... [#6946](https://github.com/ydb-platform/ydb/pull/6946) ([Oleg Doronin](https://github.com/dorooleg)).
* Fixed requests starts for queue size zero. [#6949](https://github.com/ydb-platform/ydb/pull/6949) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix storage info. [#6960](https://github.com/ydb-platform/ydb/pull/6960) ([Alexey Efimov](https://github.com/adameat)).
* ... [#6978](https://github.com/ydb-platform/ydb/pull/6978) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fixed resource pools permissions validation: * https://github.com/ydb-platform/ydb/pull/6989/files#diff-c22bfd9bf5593c8954ffe6e0c48529572eeaf460d44dc7bfece7ea6859b19ff5L395-R397 * https://github.com/ydb-platform/ydb/pull/6989/files#diff-acbe24321404698ebde9ee88b975c07511a9ef7ee29393ba47cf4024d3385ec8R494-R497. [#6989](https://github.com/ydb-platform/ydb/pull/6989) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Replace HTTP control characters with alternative ones while displaying exceptions. [#7014](https://github.com/ydb-platform/ydb/pull/7014) ([Cthulhu](https://github.com/the-ancient-1)).
* The partitioning predicate is not saved for the transaction. After recovery, the tablet resends commands to the partitions to calculate the predicate. [#7015](https://github.com/ydb-platform/ydb/pull/7015) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fix unit tests counters validation. [#7030](https://github.com/ydb-platform/ydb/pull/7030) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#7044](https://github.com/ydb-platform/ydb/pull/7044) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* ... [#7051](https://github.com/ydb-platform/ydb/pull/7051) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Fix for sls feature flag. [#7057](https://github.com/ydb-platform/ydb/pull/7057) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#7060](https://github.com/ydb-platform/ydb/pull/7060) ([Andrey Molotkov](https://github.com/molotkov-and)).
* ... [#7076](https://github.com/ydb-platform/ydb/pull/7076) ([Innokentii Mokin](https://github.com/Enjection)).
* Fix incompatibility bug. [#7079](https://github.com/ydb-platform/ydb/pull/7079) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fix distconf startup bug. [#7094](https://github.com/ydb-platform/ydb/pull/7094) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#7097](https://github.com/ydb-platform/ydb/pull/7097) ([Oleg Doronin](https://github.com/dorooleg)).
* Fix viewer redirects when we make a call to newer node via older one. [#7103](https://github.com/ydb-platform/ydb/pull/7103) ([Alexey Efimov](https://github.com/adameat)).
* ... [#7109](https://github.com/ydb-platform/ydb/pull/7109) ([Innokentii Mokin](https://github.com/Enjection)).
* The user's token may be empty. The program did not take this into account and the call to `AddOffsetToTransaction` failed with an error. [#7117](https://github.com/ydb-platform/ydb/pull/7117) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Due to the fact that the field force_io_pool_threads could be unassigned, the generation of the dynamic config was interrupted with an error. [#7138](https://github.com/ydb-platform/ydb/pull/7138) ([kruall](https://github.com/kruall)).
* Fix distconf IC session subscription state machine. [#7143](https://github.com/ydb-platform/ydb/pull/7143) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Correct temporary PDisk start sequence. [#7156](https://github.com/ydb-platform/ydb/pull/7156) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fix PDisk distconf metadata storage. [#7175](https://github.com/ydb-platform/ydb/pull/7175) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fixed logs in local docker container. [#7185](https://github.com/ydb-platform/ydb/pull/7185) ([Nikita-Levuskin](https://github.com/Nikita-Levuskin)).
* Fix a bug where static group issues could not appear in healthcheck. [#7212](https://github.com/ydb-platform/ydb/pull/7212) ([vporyadke](https://github.com/vporyadke)).
* Mvp - disable offload merge. [#7228](https://github.com/ydb-platform/ydb/pull/7228) ([Alexey Efimov](https://github.com/adameat)).
* Fix ORDER BY missing column. [#7240](https://github.com/ydb-platform/ydb/pull/7240) ([Andrey Neporada](https://github.com/nepal)).
* Fir for https://st.yandex-team.ru/yq-3427. [#7259](https://github.com/ydb-platform/ydb/pull/7259) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* ... [#7268](https://github.com/ydb-platform/ydb/pull/7268) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix AS_TABLE with ORDER BY missing column. [#7274](https://github.com/ydb-platform/ydb/pull/7274) ([Andrey Neporada](https://github.com/nepal)).
* Fix some distconf protocol and metadata storage issues. [#7279](https://github.com/ydb-platform/ydb/pull/7279) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fix block device size calculcation code. [#7341](https://github.com/ydb-platform/ydb/pull/7341) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Now inferring column datatypes from .csv file produces optional (nullable) types. [#7358](https://github.com/ydb-platform/ydb/pull/7358) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fixed bugs: 1. In the `TEvDeletePartitionDone` message handler of the PQ tablet, the `TEvPoison` message was not sent to the partition actor. 2. In the `TEvPoison` handler of the actor of the service partition, the `TEvPoison` message was not sent to the actor of the read quoter. [#7375](https://github.com/ydb-platform/ydb/pull/7375) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* ... [#7384](https://github.com/ydb-platform/ydb/pull/7384) ([yumkam](https://github.com/yumkam)).
* Issue [#7402](https://github.com/ydb-platform/ydb/issues/7402) added initialization of isajaxrequest for nebius. [#7401](https://github.com/ydb-platform/ydb/pull/7401) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* ... [#7409](https://github.com/ydb-platform/ydb/pull/7409) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#7421](https://github.com/ydb-platform/ydb/pull/7421) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix flaky Aggregation_ResultCountAll_Filter test. [#7423](https://github.com/ydb-platform/ydb/pull/7423) ([Artem Alekseev](https://github.com/fexolm)).
* ... [#7427](https://github.com/ydb-platform/ydb/pull/7427) ([Alexey Ozeritskiy](https://github.com/resetius)).
* Fix passing of configuration to ticket parser. It expects cert path instead of cert data. [#7445](https://github.com/ydb-platform/ydb/pull/7445) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Fix for https://st.yandex-team.ru/yq-3428. [#7450](https://github.com/ydb-platform/ydb/pull/7450) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* ... [#7452](https://github.com/ydb-platform/ydb/pull/7452) ([Vitaly Stoyan](https://github.com/vitstn)).
* Treat inactive pdisks as alive in healthcheck. [#7466](https://github.com/ydb-platform/ydb/pull/7466) ([vporyadke](https://github.com/vporyadke)).
* Incremental optimizer for Wide&Block channels. [#7479](https://github.com/ydb-platform/ydb/pull/7479) ([Andrey Neporada](https://github.com/nepal)).
* Error in transitions between transaction states. [#7482](https://github.com/ydb-platform/ydb/pull/7482) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fix DQ input union/merge values with zero input channels. [#7515](https://github.com/ydb-platform/ydb/pull/7515) ([Andrey Neporada](https://github.com/nepal)).
* Correctly check wb requests requirement, improve swagger description. [#7521](https://github.com/ydb-platform/ydb/pull/7521) ([Alexey Efimov](https://github.com/adameat)).
* The `KV` tablet can respond to the `ReadRange` request with `OVERRUN`. In this case, the `PQ` tablet makes a repeat request. Requests the range from the last received key. [#7549](https://github.com/ydb-platform/ydb/pull/7549) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Revert local grpc peer value. [#7555](https://github.com/ydb-platform/ydb/pull/7555) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Normalized path when loading metadata for type inferring files. [#7561](https://github.com/ydb-platform/ydb/pull/7561) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Get queryIt.second' in kqp_compile_service.cpp:44 error if: 1) make request with user sid (it will be saved in queryId) 2) change table scheme 3) make the same request (it will be with recompilation, queryId with sid will be removed from cache and make new queryId without sid) 4) make the same request (it will be with sid and it doesn't find it in cache, then in cache will be 2 query Id with and without sid) 5) change table scheme 6) make the same request (it will be with recompilation, queryId with sid will be removed from cache and make new queryId without sid, then it will be compiled and try to put it in cache, but this queryId without sid is already in cache). [#7562](https://github.com/ydb-platform/ydb/pull/7562) ([VPolka](https://github.com/VPolka)).
* Fix for https://st.yandex-team.ru/yq-3529. [#7569](https://github.com/ydb-platform/ydb/pull/7569) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* ... [#7592](https://github.com/ydb-platform/ydb/pull/7592) ([yumkam](https://github.com/yumkam)).
* YDB FQ: add missing types of connections to cloud audit. [#7607](https://github.com/ydb-platform/ydb/pull/7607) ([Vitaly Isaev](https://github.com/vitalyisaev2)).
* ... [#7643](https://github.com/ydb-platform/ydb/pull/7643) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#7651](https://github.com/ydb-platform/ydb/pull/7651) ([Sergey Belyakov](https://github.com/serbel324)).
* Fixed a bug where a transaction with a read from a topic does not send a TEvReadSetAck. [#7676](https://github.com/ydb-platform/ydb/pull/7676) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* The value of the constant in the code was different from the value in the proto-file. [#7695](https://github.com/ydb-platform/ydb/pull/7695) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fixed an issue where a SELECT query could produce unexpected duplicate rows. [#7697](https://github.com/ydb-platform/ydb/pull/7697) ([Aleksei Borzenkov](https://github.com/snaury)).
* ... [#7727](https://github.com/ydb-platform/ydb/pull/7727) ([yumkam](https://github.com/yumkam)).
* ... [#7798](https://github.com/ydb-platform/ydb/pull/7798) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix segfault that appeared after https://github.com/ydb-platform/ydb/commit/6576464d6b8dca046c27847c1ff60fc6748f329d (https://github.com/ydb-platform/ydb/pull/5982). [#7808](https://github.com/ydb-platform/ydb/pull/7808) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#7809](https://github.com/ydb-platform/ydb/pull/7809) ([Oleg Doronin](https://github.com/dorooleg)).
* ... [#7815](https://github.com/ydb-platform/ydb/pull/7815) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Fixed unit test KqpLimits::ComputeActorMemoryAllocationFailureQueryService with resource pools. [#7873](https://github.com/ydb-platform/ydb/pull/7873) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Improve s3 url escape. [#7881](https://github.com/ydb-platform/ydb/pull/7881) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix error attempt to read after eof. [#7889](https://github.com/ydb-platform/ydb/pull/7889) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix [#7790](https://github.com/ydb-platform/ydb/issues/7790). [#7897](https://github.com/ydb-platform/ydb/pull/7897) ([Nikita Vasilev](https://github.com/nikvas0)).
* ... [#7925](https://github.com/ydb-platform/ydb/pull/7925) ([Roman Udovichenko](https://github.com/rvu1024)).
* Fixed Acceleration in mirror-3-dc and UT environment. [#7931](https://github.com/ydb-platform/ydb/pull/7931) ([Sergey Belyakov](https://github.com/serbel324)).
* Do not use -Oz on windows. [#7960](https://github.com/ydb-platform/ydb/pull/7960) ([Andrey Neporada](https://github.com/nepal)).
* Fixed '\\' escaping. [#7984](https://github.com/ydb-platform/ydb/pull/7984) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix FilterPushdownEnableMultiusage on dependent predicates. [#8033](https://github.com/ydb-platform/ydb/pull/8033) ([Andrey Neporada](https://github.com/nepal)).
* Fixed error sent large get operation. [#8035](https://github.com/ydb-platform/ydb/pull/8035) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Needed for compatibility. [#8065](https://github.com/ydb-platform/ydb/pull/8065) ([VPolka](https://github.com/VPolka)).
* Fixed internal error for insert without params. [#8074](https://github.com/ydb-platform/ydb/pull/8074) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#8109](https://github.com/ydb-platform/ydb/pull/8109) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#8136](https://github.com/ydb-platform/ydb/pull/8136) ([azevaykin](https://github.com/azevaykin)).
* Changes from PR [#8116](https://github.com/ydb-platform/ydb/issues/8116). [#8142](https://github.com/ydb-platform/ydb/pull/8142) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fix RebuildCalcOverWindowGroup failing with PercentRank/CumeDist/Ntile. [#8148](https://github.com/ydb-platform/ydb/pull/8148) ([Mark Ziganshin](https://github.com/loochek)).
* Treat initial vdisk status as ok in healthcheck. [#8150](https://github.com/ydb-platform/ydb/pull/8150) ([vporyadke](https://github.com/vporyadke)).
* ... [#8153](https://github.com/ydb-platform/ydb/pull/8153) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#8157](https://github.com/ydb-platform/ydb/pull/8157) ([Innokentii Mokin](https://github.com/Enjection)).
* Query float test asan. [#8161](https://github.com/ydb-platform/ydb/pull/8161) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* ... [#8175](https://github.com/ydb-platform/ydb/pull/8175) ([Vitaly Stoyan](https://github.com/vitstn)).
* Allow append to a table with same column groups. [#8176](https://github.com/ydb-platform/ydb/pull/8176) ([Roman Udovichenko](https://github.com/rvu1024)).
* Fixes that an unset feature flags in dynamic config overrides a feature flags in static config for CMS. [#8238](https://github.com/ydb-platform/ydb/pull/8238) ([Ilia Shakhov](https://github.com/pixcc)).
* Fixed database checking. [#8251](https://github.com/ydb-platform/ydb/pull/8251) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#8277](https://github.com/ydb-platform/ydb/pull/8277) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#8285](https://github.com/ydb-platform/ydb/pull/8285) ([Filitov Mikhail](https://github.com/lll-phill-lll)).
* Fix for false-postives in storage healthcheck. [#8291](https://github.com/ydb-platform/ydb/pull/8291) ([vporyadke](https://github.com/vporyadke)).
* Fixed sessions leak in metadata service. [#8312](https://github.com/ydb-platform/ydb/pull/8312) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* To reflect cors headers fix. [#8315](https://github.com/ydb-platform/ydb/pull/8315) ([Alexey Efimov](https://github.com/adameat)).
* ... [#8333](https://github.com/ydb-platform/ydb/pull/8333) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix segfault in autocomplete handler when redirecting to a database closes [#8345](https://github.com/ydb-platform/ydb/issues/8345). [#8367](https://github.com/ydb-platform/ydb/pull/8367) ([Alexey Efimov](https://github.com/adameat)).
* Fixed cleanup table retries. [#8369](https://github.com/ydb-platform/ydb/pull/8369) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#8408](https://github.com/ydb-platform/ydb/pull/8408) ([Oleg Doronin](https://github.com/dorooleg)).
* Fix aggregation of table stats for OLAP tables. [#8417](https://github.com/ydb-platform/ydb/pull/8417) ([Semyon](https://github.com/swalrus1)).
* ... [#8422](https://github.com/ydb-platform/ydb/pull/8422) ([yumkam](https://github.com/yumkam)).
* Fix segfault in tenantinfo handler closes [#8448](https://github.com/ydb-platform/ydb/issues/8448). [#8449](https://github.com/ydb-platform/ydb/pull/8449) ([Alexey Efimov](https://github.com/adameat)).
* Fix segfault for heap iterator test. [#8473](https://github.com/ydb-platform/ydb/pull/8473) ([mregrock](https://github.com/mregrock)).
* Add optional to feature flags to reflect absence of values. [#8510](https://github.com/ydb-platform/ydb/pull/8510) ([Alexey Efimov](https://github.com/adameat)).
* The entry for `WriteId` was not saved if there was an empty list of partitions in `TTxWriteInfo`. As a result, after restoring the tablet, `Y_VERIFY` was triggered. [#8517](https://github.com/ydb-platform/ydb/pull/8517) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Clickhouse is now always able to parse timestamp data parsed by arrow library. [#8547](https://github.com/ydb-platform/ydb/pull/8547) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fill final stats only once at the end of execution. [#8553](https://github.com/ydb-platform/ydb/pull/8553) ([Ivan](https://github.com/abyss7)).
* ... [#8592](https://github.com/ydb-platform/ydb/pull/8592) ([Aleksei Borzenkov](https://github.com/snaury)).
* ... [#8598](https://github.com/ydb-platform/ydb/pull/8598) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* YDB FQ: fix use of Greenplum as an external datasource. [#8604](https://github.com/ydb-platform/ydb/pull/8604) ([Vitaly Isaev](https://github.com/vitalyisaev2)).
* ... [#8622](https://github.com/ydb-platform/ydb/pull/8622) ([yumkam](https://github.com/yumkam)).
* YDB FQ: add Greenplum to federated `JOIN` test. [#8649](https://github.com/ydb-platform/ydb/pull/8649) ([Vitaly Isaev](https://github.com/vitalyisaev2)).
* Fixes for [YQ-3484](https://st.yandex-team.ru/YQ-3484), [YQ-3532](https://st.yandex-team.ru/YQ-3532), [YQ-2912](https://st.yandex-team.ru/YQ-2912). [#8676](https://github.com/ydb-platform/ydb/pull/8676) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Another fix for feature flags. [#8690](https://github.com/ydb-platform/ydb/pull/8690) ([Alexey Efimov](https://github.com/adameat)).
* Currently PDisk write a lot of excessive information about chunks into log with INFO priority, so this PR reduces level to DEBUG and condenses chunks list. [#8699](https://github.com/ydb-platform/ydb/pull/8699) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* ... [#8712](https://github.com/ydb-platform/ydb/pull/8712) ([Aleksei Borzenkov](https://github.com/snaury)).
* Fix false-positive assertion in RecoverLostData mode. [#8736](https://github.com/ydb-platform/ydb/pull/8736) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Closes https://github.com/ydb-platform/ydb-embedded-ui/issues/1023. [#8738](https://github.com/ydb-platform/ydb/pull/8738) ([Alexey Efimov](https://github.com/adameat)).
* ... [#8745](https://github.com/ydb-platform/ydb/pull/8745) ([Nikolay Shestakov](https://github.com/nshestakov)).
* Do not ask hive for tablet info unless it's a database node list do not merge whiteboard info in viewer service by default. [#8790](https://github.com/ydb-platform/ydb/pull/8790) ([Alexey Efimov](https://github.com/adameat)).
* Disable metadata objects on serverless. [#8806](https://github.com/ydb-platform/ydb/pull/8806) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* After restarting, the PQ tablet can re-send the message `TEvTxCalcPredicate` to the partition. Currently, the actor of the partition does not check the `PlanStep` messages. This is a mistake. Since if he has already completed this transaction before, the predicate will be calculated incorrectly. As a result, the transaction may be partially completed. [#8809](https://github.com/ydb-platform/ydb/pull/8809) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* ... [#8827](https://github.com/ydb-platform/ydb/pull/8827) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix erroneous finish on TDqInputMergeBlockStreamValue. [#8834](https://github.com/ydb-platform/ydb/pull/8834) ([Andrey Neporada](https://github.com/nepal)).
* Fix resolved timestamp emitted too early for some displaced upserts. [#8847](https://github.com/ydb-platform/ydb/pull/8847) ([Aleksei Borzenkov](https://github.com/snaury)).
* Fix reporting of initial VDisk status to SysView. [#8853](https://github.com/ydb-platform/ydb/pull/8853) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#8894](https://github.com/ydb-platform/ydb/pull/8894) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix wrong YQL_ENSURE in PushdownComplexFiltersOverAggregate. [#8899](https://github.com/ydb-platform/ydb/pull/8899) ([Andrey Neporada](https://github.com/nepal)).
* Do not try to call IsComplete() on Arguments. [#8901](https://github.com/ydb-platform/ydb/pull/8901) ([Andrey Neporada](https://github.com/nepal)).
* ... [#8903](https://github.com/ydb-platform/ydb/pull/8903) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix cluster tablets grouping. [#8904](https://github.com/ydb-platform/ydb/pull/8904) ([Alexey Efimov](https://github.com/adameat)).
* Fix empty table name error. [#8907](https://github.com/ydb-platform/ydb/pull/8907) ([Vadim Averin](https://github.com/avevad)).
* During the commit of a transaction with an entry in the topic, the blob offset is incorrectly calculated. Fixed the condition, added tests for all possible combinations of blocks when writing to the topic. [#8916](https://github.com/ydb-platform/ydb/pull/8916) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Return 0 when field is zero closes [#8953](https://github.com/ydb-platform/ydb/issues/8953). [#8955](https://github.com/ydb-platform/ydb/pull/8955) ([Alexey Efimov](https://github.com/adameat)).
* Fix for [yq-3286](https://st.yandex-team.ru/yq-3286). [#8965](https://github.com/ydb-platform/ydb/pull/8965) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fix for [yq-3287](https://st.yandex-team.ru/yq-3287). [#8970](https://github.com/ydb-platform/ydb/pull/8970) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fix restore data option in YDB CLI. [#9009](https://github.com/ydb-platform/ydb/pull/9009) ([Ilia Shakhov](https://github.com/pixcc)).
* Temporarily removed assert in a peephole optimisation. Now SELECTs without `HOP_START()` and `HOP_END()` can be used. [#9027](https://github.com/ydb-platform/ydb/pull/9027) ([Alexey Pozdniakov](https://github.com/APozdniakov)).
* ... [#9038](https://github.com/ydb-platform/ydb/pull/9038) ([kruall](https://github.com/kruall)).
* ... [#9069](https://github.com/ydb-platform/ydb/pull/9069) ([kruall](https://github.com/kruall)).
* ... [#9072](https://github.com/ydb-platform/ydb/pull/9072) ([yumkam](https://github.com/yumkam)).
* ... [#9083](https://github.com/ydb-platform/ydb/pull/9083) ([Vitaly Stoyan](https://github.com/vitstn)).
* YDB CLI build fails due to this bug. [#9089](https://github.com/ydb-platform/ydb/pull/9089) ([Bulat](https://github.com/Gazizonoki)).
* YDB FQ: handle exception in YQL Generic Provider when IAM service is not available. [#9092](https://github.com/ydb-platform/ydb/pull/9092) ([Vitaly Isaev](https://github.com/vitalyisaev2)).
* Fixed `resolved` message emitter (Change Data Capture). [#9104](https://github.com/ydb-platform/ydb/pull/9104) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#9116](https://github.com/ydb-platform/ydb/pull/9116) ([Bulat](https://github.com/Gazizonoki)).
* ... [#9118](https://github.com/ydb-platform/ydb/pull/9118) ([Oleg Doronin](https://github.com/dorooleg)).
* NodeBroker now sends deltas when listing recently added nodes. [#9122](https://github.com/ydb-platform/ydb/pull/9122) ([Aleksei Borzenkov](https://github.com/snaury)).
* Fix some bugs in jsonpath. [#9146](https://github.com/ydb-platform/ydb/pull/9146) ([Vadim Averin](https://github.com/avevad)).
* Fix disabled use virtual addressing option for import from S3. [#9162](https://github.com/ydb-platform/ydb/pull/9162) ([Ilia Shakhov](https://github.com/pixcc)).
* Limit inflight coordination service session requests. [#9168](https://github.com/ydb-platform/ydb/pull/9168) ([Aleksei Borzenkov](https://github.com/snaury)).
* YDB FQ: mitigate DNS server misbehaving error in Docker-based YDB Connector test. [#9172](https://github.com/ydb-platform/ydb/pull/9172) ([Vitaly Isaev](https://github.com/vitalyisaev2)).
* Another yet antlr build fix for windows. [#9173](https://github.com/ydb-platform/ydb/pull/9173) ([Bulat](https://github.com/Gazizonoki)).
* ... [#9177](https://github.com/ydb-platform/ydb/pull/9177) ([yumkam](https://github.com/yumkam)).
* Make sure we have properly aligned arrow buffers after deserialization. [#9179](https://github.com/ydb-platform/ydb/pull/9179) ([Andrey Neporada](https://github.com/nepal)).
* CTAS fixed for script executions. [#9228](https://github.com/ydb-platform/ydb/pull/9228) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#9229](https://github.com/ydb-platform/ydb/pull/9229) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#9231](https://github.com/ydb-platform/ydb/pull/9231) ([VPolka](https://github.com/VPolka)).
* There is an extra check in the code. [#9281](https://github.com/ydb-platform/ydb/pull/9281) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fix CopyToChunked for empty batch. [#9288](https://github.com/ydb-platform/ydb/pull/9288) ([Nikita Vasilev](https://github.com/nikvas0)).
* Corrected the iterator validation for the VDiskState.find(). [#9309](https://github.com/ydb-platform/ydb/pull/9309) ([mregrock](https://github.com/mregrock)).
* ... [#9316](https://github.com/ydb-platform/ydb/pull/9316) ([Vitaly Stoyan](https://github.com/vitstn)).
* Commit with removal of tests - https://github.com/ydb-platform/ydb/pull/6439. [#9326](https://github.com/ydb-platform/ydb/pull/9326) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Highlight YQL comments in YDB CLI interactive mode. [#9359](https://github.com/ydb-platform/ydb/pull/9359) ([Victor Smirnov](https://github.com/vityaman)).
* Fixed a bug where an invariant could be violated in SchemeShard after the CDC initial scan. [#9360](https://github.com/ydb-platform/ydb/pull/9360) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#9384](https://github.com/ydb-platform/ydb/pull/9384) ([kruall](https://github.com/kruall)).
* The value of `PartitionsInited` changed for all partitions. As a result, after the first entry in the transaction, the `DescripeTopic` operation hung with the `IncludeStats` flag. [#9392](https://github.com/ydb-platform/ydb/pull/9392) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* When creating a topic or a consumer, if the user does not specify the `--supported-codecs` option, then the `Codecs__` field remains empty. [#9419](https://github.com/ydb-platform/ydb/pull/9419) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Scheme operations (e.g. AlterTable) are now forbidden on backup tables. [#9431](https://github.com/ydb-platform/ydb/pull/9431) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#9456](https://github.com/ydb-platform/ydb/pull/9456) ([Roman Udovichenko](https://github.com/rvu1024)).
* Cleanup and fix antlr make files. Fixes win build. [#9459](https://github.com/ydb-platform/ydb/pull/9459) ([Andrey Neporada](https://github.com/nepal)).
* There are many places where the field "remote_address" is empty. Fix this for these cases. [#9460](https://github.com/ydb-platform/ydb/pull/9460) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Deleted an unnecessary function call in the `TSendMessageBatchReplyCallback` code. [#9476](https://github.com/ydb-platform/ydb/pull/9476) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* ... [#9499](https://github.com/ydb-platform/ydb/pull/9499) ([Oleg Doronin](https://github.com/dorooleg)).
* Fixed screts not found error handling. [#9501](https://github.com/ydb-platform/ydb/pull/9501) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fixed a bug that sometimes caused the CDC initial scan to freeze. [#9507](https://github.com/ydb-platform/ydb/pull/9507) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Fix incorrect constraints clear in ClearSortness. [#9532](https://github.com/ydb-platform/ydb/pull/9532) ([Roman Udovichenko](https://github.com/rvu1024)).
* Fix segfault, closes [#9549](https://github.com/ydb-platform/ydb/issues/9549). [#9551](https://github.com/ydb-platform/ydb/pull/9551) ([Alexey Efimov](https://github.com/adameat)).
* Fix maximum pdisks per node calculation. [#9563](https://github.com/ydb-platform/ydb/pull/9563) ([Alexey Efimov](https://github.com/adameat)).
* Fix sorting of inner elements in viewer/nodes handler. [#9565](https://github.com/ydb-platform/ydb/pull/9565) ([Alexey Efimov](https://github.com/adameat)).
* Fixed error duplicate session. [#9583](https://github.com/ydb-platform/ydb/pull/9583) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* The consumer's generation number is not stored in the transaction. Because of this, the consumer's reading position may be reset. [#9590](https://github.com/ydb-platform/ydb/pull/9590) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Recompilation with query from request can affect compile cache. [#9593](https://github.com/ydb-platform/ydb/pull/9593) ([VPolka](https://github.com/VPolka)).
* Service parties do not need to process the config update. The PQ tablet should only send a message to the main partitions. [#9599](https://github.com/ydb-platform/ydb/pull/9599) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fix handling of uncorrelated column name in ORDER BY. [#9602](https://github.com/ydb-platform/ydb/pull/9602) ([Andrey Neporada](https://github.com/nepal)).
* Ydb/core/kqp/ut/olap/kqpolapsysview.statssysviewbytesdictstatactualization. [#9605](https://github.com/ydb-platform/ydb/pull/9605) ([Andrey Neporada](https://github.com/nepal)).
* ... [#9625](https://github.com/ydb-platform/ydb/pull/9625) ([azevaykin](https://github.com/azevaykin)).
* YQ kqprun fix win build. [#9652](https://github.com/ydb-platform/ydb/pull/9652) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Several fixes for groups and nodes handlers: 1. Fixed the filter for node_id + pdisk_id (previously, it operated on an OR principle). 2. Adjusted so that node_id + pdisk_id, node_id, pdisk_id, group_id, and storage_pool_name (for future use) are all considered pre-filters and affect the Total. 3. Fixed AllocationUnits—there was a race condition, and sometimes we didn't wait for the Hive's response. 4. Corrected the combination of node_id + group_id in /viewer/nodes (although, in my opinion, this is strange). [#9681](https://github.com/ydb-platform/ydb/pull/9681) ([Alexey Efimov](https://github.com/adameat)).
* Prepare to disable blob header by default in VDisk. [#9683](https://github.com/ydb-platform/ydb/pull/9683) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fixed a bug when reading from an asynchronous replica may cause a crash. [#9723](https://github.com/ydb-platform/ydb/pull/9723) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Fix uptime filter. [#9752](https://github.com/ydb-platform/ydb/pull/9752) ([Alexey Efimov](https://github.com/adameat)).
* ... [#9769](https://github.com/ydb-platform/ydb/pull/9769) ([Innokentii Mokin](https://github.com/Enjection)).
* ... [#9809](https://github.com/ydb-platform/ydb/pull/9809) ([Aleksei Borzenkov](https://github.com/snaury)).
* ... [#9818](https://github.com/ydb-platform/ydb/pull/9818) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* ... [#9819](https://github.com/ydb-platform/ydb/pull/9819) ([Bulat](https://github.com/Gazizonoki)).
* ... [#9847](https://github.com/ydb-platform/ydb/pull/9847) ([yumkam](https://github.com/yumkam)).
* ... [#9848](https://github.com/ydb-platform/ydb/pull/9848) ([Aleksei Borzenkov](https://github.com/snaury)).
* Intersect node filters for tabletinfo handler closes [#9845](https://github.com/ydb-platform/ydb/issues/9845). [#9850](https://github.com/ydb-platform/ydb/pull/9850) ([Alexey Efimov](https://github.com/adameat)).
* Closes [#9851](https://github.com/ydb-platform/ydb/issues/9851). [#9867](https://github.com/ydb-platform/ydb/pull/9867) ([Alexey Efimov](https://github.com/adameat)).
* ... [#9869](https://github.com/ydb-platform/ydb/pull/9869) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Fix for [yq-3706](https://st.yandex-team.ru/yq-3706). [#9873](https://github.com/ydb-platform/ydb/pull/9873) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fix segfault when called from older version. [#9880](https://github.com/ydb-platform/ydb/pull/9880) ([Alexey Efimov](https://github.com/adameat)).
* ... [#9917](https://github.com/ydb-platform/ydb/pull/9917) ([Innokentii Mokin](https://github.com/Enjection)).
* Exclude dropped indexes from limits. [#9932](https://github.com/ydb-platform/ydb/pull/9932) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#9945](https://github.com/ydb-platform/ydb/pull/9945) ([Oleg Doronin](https://github.com/dorooleg)).
* Disable row_dispatcher tests during export CMake. [#9949](https://github.com/ydb-platform/ydb/pull/9949) ([Dmitrii Dmitriev](https://github.com/dimdim1177)).
* Temporarily fix data race in PDisk. [#9988](https://github.com/ydb-platform/ydb/pull/9988) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Deadlock can occur only if BufferPoolSize is 4, so maxEnqueuedCompletionActions is 2. This is almost impossible configuration of PDisk, so it's not important in real life. [#9991](https://github.com/ydb-platform/ydb/pull/9991) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* ... [#9996](https://github.com/ydb-platform/ydb/pull/9996) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#10009](https://github.com/ydb-platform/ydb/pull/10009) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* ... [#10035](https://github.com/ydb-platform/ydb/pull/10035) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix alter-extsubdomain behaviour that could prevent some database alters from executing when `enable_alter_database_create_hive_first` feature flag is enabled. [#10074](https://github.com/ydb-platform/ydb/pull/10074) ([ijon](https://github.com/ijon)).
* ... [#10084](https://github.com/ydb-platform/ydb/pull/10084) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#10095](https://github.com/ydb-platform/ydb/pull/10095) ([Vadim Averin](https://github.com/avevad)).
* ... [#10114](https://github.com/ydb-platform/ydb/pull/10114) ([Vitaly Stoyan](https://github.com/vitstn)).
* Do not add ticket to refresh queue when perform immediate refresh. Fix delay time for refresh queue ... [#10188](https://github.com/ydb-platform/ydb/pull/10188) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Date, timestamp or time interval types are currently not supported with `json_list` format. [#10208](https://github.com/ydb-platform/ydb/pull/10208) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fix tablets switch in cluster handler. [#10212](https://github.com/ydb-platform/ydb/pull/10212) ([Alexey Efimov](https://github.com/adameat)).
* ... [#10219](https://github.com/ydb-platform/ydb/pull/10219) ([Vadim Averin](https://github.com/avevad)).
* Force precompute on returning effect input. [#10231](https://github.com/ydb-platform/ydb/pull/10231) ([Mikhail Surin](https://github.com/ssmike)).
* ... [#10241](https://github.com/ydb-platform/ydb/pull/10241) ([azevaykin](https://github.com/azevaykin)).
* ... [#10260](https://github.com/ydb-platform/ydb/pull/10260) ([mregrock](https://github.com/mregrock)).
* ... [#10261](https://github.com/ydb-platform/ydb/pull/10261) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix filter handling in nodes and groups, closes https://github.com/ydb-platform/ydb-embedded-ui/issues/909. [#10277](https://github.com/ydb-platform/ydb/pull/10277) ([Alexey Efimov](https://github.com/adameat)).
* ... [#10278](https://github.com/ydb-platform/ydb/pull/10278) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Fix generating proto files in CMake. [#10296](https://github.com/ydb-platform/ydb/pull/10296) ([Dmitrii Dmitriev](https://github.com/dimdim1177)).
* Fixed nested type parsing. [#10300](https://github.com/ydb-platform/ydb/pull/10300) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Remove cerr debug output. [#10321](https://github.com/ydb-platform/ydb/pull/10321) ([Alexey Efimov](https://github.com/adameat)).
* Fix `There were headers present in the request which were not signed` error returned from MinIO during multipart uploading in S3 exports. [#10333](https://github.com/ydb-platform/ydb/pull/10333) ([Ilia Shakhov](https://github.com/pixcc)).
* Fix wrong columns order in sinks. [#10338](https://github.com/ydb-platform/ydb/pull/10338) ([Nikita Vasilev](https://github.com/nikvas0)).
* ... [#10348](https://github.com/ydb-platform/ydb/pull/10348) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fixed verify failed on empty fields. [#10351](https://github.com/ydb-platform/ydb/pull/10351) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix VDisk replication token handling, add some extra checks and log points. [#10371](https://github.com/ydb-platform/ydb/pull/10371) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fix sql flags for module resolver in query replay. [#10405](https://github.com/ydb-platform/ydb/pull/10405) ([Andrey Neporada](https://github.com/nepal)).
* Do not try to collect extra sort columns if ORDER BY is ignored. [#10417](https://github.com/ydb-platform/ydb/pull/10417) ([Andrey Neporada](https://github.com/nepal)).
* ... [#10441](https://github.com/ydb-platform/ydb/pull/10441) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#10442](https://github.com/ydb-platform/ydb/pull/10442) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* You cannot simultaneously commit offsets in a transaction and out of a transaction. [#10460](https://github.com/ydb-platform/ydb/pull/10460) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fix sink empty batch. [#10463](https://github.com/ydb-platform/ydb/pull/10463) ([Nikita Vasilev](https://github.com/nikvas0)).
* Do not retry `CLIENT_UNAUTHENTICATED` & `CLIENT_CALL_UNIMPLEMENTED`. [#10465](https://github.com/ydb-platform/ydb/pull/10465) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Fix stucking donor queries. [#10470](https://github.com/ydb-platform/ydb/pull/10470) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#10484](https://github.com/ydb-platform/ydb/pull/10484) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Do not convert google datetime to string in schema. [#10487](https://github.com/ydb-platform/ydb/pull/10487) ([Alexey Efimov](https://github.com/adameat)).
* Because of unhandled double-notification the `IntrusiveList` external size became wrong, which leads to crashes and asserts. [#10499](https://github.com/ydb-platform/ydb/pull/10499) ([Ivan](https://github.com/abyss7)).
* ... [#10522](https://github.com/ydb-platform/ydb/pull/10522) ([kruall](https://github.com/kruall)).
* EntropyPool().Read() can generate data partially, and it returns read bytes, so it should be read inside while loop. [#10534](https://github.com/ydb-platform/ydb/pull/10534) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Stabilize table order in test. [#10539](https://github.com/ydb-platform/ydb/pull/10539) ([Andrey Neporada](https://github.com/nepal)).
* Fix replication bug. [#10560](https://github.com/ydb-platform/ydb/pull/10560) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#10593](https://github.com/ydb-platform/ydb/pull/10593) ([Nikolay Shestakov](https://github.com/nshestakov)).
* Correctly pass, merge and check body parameters in local-rpc calls closes [#10588](https://github.com/ydb-platform/ydb/issues/10588). [#10601](https://github.com/ydb-platform/ydb/pull/10601) ([Alexey Efimov](https://github.com/adameat)).
* Fix slots per disk not returned without a filter. [#10607](https://github.com/ydb-platform/ydb/pull/10607) ([Alexey Efimov](https://github.com/adameat)).
* ... [#10612](https://github.com/ydb-platform/ydb/pull/10612) ([Oleg Doronin](https://github.com/dorooleg)).
* The default value for the `--codec` option of the `ydb topic write` command. [#10651](https://github.com/ydb-platform/ydb/pull/10651) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fix volatile transactions getting stuck after a restart. [#10679](https://github.com/ydb-platform/ydb/pull/10679) ([Aleksei Borzenkov](https://github.com/snaury)).
* ... [#10696](https://github.com/ydb-platform/ydb/pull/10696) ([azevaykin](https://github.com/azevaykin)).
* This unreverts https://github.com/ydb-platform/ydb/pull/9979 after https://github.com/ydb-platform/ydb/pull/10575. And fixes missed case when finalize is turn off, that was caught with yql tests. [#10707](https://github.com/ydb-platform/ydb/pull/10707) ([Vladluk](https://github.com/vladl2802)).
* ... [#10712](https://github.com/ydb-platform/ydb/pull/10712) ([Nikolay Shestakov](https://github.com/nshestakov)).
* Fix memory consumption restriction in stream RPC calls: execute scan query, execute query and yql script. [#10758](https://github.com/ydb-platform/ydb/pull/10758) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#10795](https://github.com/ydb-platform/ydb/pull/10795) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#10815](https://github.com/ydb-platform/ydb/pull/10815) ([azevaykin](https://github.com/azevaykin)).
* Correct counting of resources in cluster and tenantinfo handlers. [#10819](https://github.com/ydb-platform/ydb/pull/10819) ([Alexey Efimov](https://github.com/adameat)).
* Fixed a bug where restoring from a backup using `--import-data` could fail if the partitioning of the table was changed. [#10864](https://github.com/ydb-platform/ydb/pull/10864) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Fix exporting CMake for darwin. [#10865](https://github.com/ydb-platform/ydb/pull/10865) ([Dmitrii Dmitriev](https://github.com/dimdim1177)).
* ... [#10873](https://github.com/ydb-platform/ydb/pull/10873) ([azevaykin](https://github.com/azevaykin)).
* Fix container label in vdisk metrics for grafana dashboard. [#10881](https://github.com/ydb-platform/ydb/pull/10881) ([Aleksei Kobzev](https://github.com/kobzonega)).
* It's needed to correctly check capabilities through cluster backend before issuing commands on a database. [#10893](https://github.com/ydb-platform/ydb/pull/10893) ([Alexey Efimov](https://github.com/adameat)).
* ... [#10912](https://github.com/ydb-platform/ydb/pull/10912) ([azevaykin](https://github.com/azevaykin)).
* ... [#10914](https://github.com/ydb-platform/ydb/pull/10914) ([Vitaly Stoyan](https://github.com/vitstn)).
* The test expects to read N messages from the topic. In the `asan` read configuration, the test cannot read N messages in one request. Added the `Read_Exactly_N_Messages_From_Topic` method. [#10937](https://github.com/ydb-platform/ydb/pull/10937) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* ... [#10944](https://github.com/ydb-platform/ydb/pull/10944) ([Roman Udovichenko](https://github.com/rvu1024)).
* Fixed use after free. [#10978](https://github.com/ydb-platform/ydb/pull/10978) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* In rare cases we can receive error and response together. closes [#10979](https://github.com/ydb-platform/ydb/issues/10979). [#10985](https://github.com/ydb-platform/ydb/pull/10985) ([Alexey Efimov](https://github.com/adameat)).
* ... [#11017](https://github.com/ydb-platform/ydb/pull/11017) ([Vitaly Stoyan](https://github.com/vitstn)).
* Fix possible race with NodeDisconnected and incoming messages. [#11024](https://github.com/ydb-platform/ydb/pull/11024) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fix block device size calculation. [#11028](https://github.com/ydb-platform/ydb/pull/11028) ([Alexander Rutkovsky](https://github.com/alexvru)).
* YT block input fix for dynamic tables. [#11040](https://github.com/ydb-platform/ydb/pull/11040) ([Mark Ziganshin](https://github.com/loochek)).
* Fix crash when consumer reads simultaneously with its deleting. [#11043](https://github.com/ydb-platform/ydb/pull/11043) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#11054](https://github.com/ydb-platform/ydb/pull/11054) ([Vitaly Stoyan](https://github.com/vitstn)).
* ... [#11055](https://github.com/ydb-platform/ydb/pull/11055) ([Anton Martsenyuk](https://github.com/antoniox)).
* Fixed excessive read latency during and after some shard splits. [#11059](https://github.com/ydb-platform/ydb/pull/11059) ([Aleksei Borzenkov](https://github.com/snaury)).
* ... [#11071](https://github.com/ydb-platform/ydb/pull/11071) ([yumkam](https://github.com/yumkam)).
* ... [#11075](https://github.com/ydb-platform/ydb/pull/11075) ([Vitaly Stoyan](https://github.com/vitstn)).
* Added row id validation. [#11080](https://github.com/ydb-platform/ydb/pull/11080) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix double PassAway call in Healthcheck actor. [#11096](https://github.com/ydb-platform/ydb/pull/11096) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Fix PDisk drive size estimation code. [#11098](https://github.com/ydb-platform/ydb/pull/11098) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fix tenant info tablets. [#11111](https://github.com/ydb-platform/ydb/pull/11111) ([Alexey Efimov](https://github.com/adameat)).
* ... [#11113](https://github.com/ydb-platform/ydb/pull/11113) ([Nikolay Shestakov](https://github.com/nshestakov)).
* Now when request fails in ydb fq proxy doesnt send it back with the same execution ttl. [#11145](https://github.com/ydb-platform/ydb/pull/11145) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fixed import into contrib build errors. [#11162](https://github.com/ydb-platform/ydb/pull/11162) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix PhysicalOptimizer-BypassMerge with key ranges. [#11203](https://github.com/ydb-platform/ydb/pull/11203) ([Andrey Neporada](https://github.com/nepal)).
* YDB nodes have different time counting. May occured situations when ticket cannot verify and get error "token verification failed: token expired" ... [#11212](https://github.com/ydb-platform/ydb/pull/11212) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Support ANSI SQL syntax highlighting. [#11233](https://github.com/ydb-platform/ydb/pull/11233) ([Victor Smirnov](https://github.com/vityaman)).
* Control memory consumption in run script actor. Unify memory consumption in execute query RPC and run script actor. [#11241](https://github.com/ydb-platform/ydb/pull/11241) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* Fix shard ranges sort. [#11257](https://github.com/ydb-platform/ydb/pull/11257) ([Nikita Vasilev](https://github.com/nikvas0)).
* Fix crash in storage/groups - access of already released memory closes [#11263](https://github.com/ydb-platform/ydb/issues/11263). [#11268](https://github.com/ydb-platform/ydb/pull/11268) ([Alexey Efimov](https://github.com/adameat)).
* Fix for [yq-3747](https://st.yandex-team.ru/yq-3747). [#11271](https://github.com/ydb-platform/ydb/pull/11271) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fix bootstrapper being unable to boot tablets in certain cases. [#11284](https://github.com/ydb-platform/ydb/pull/11284) ([Aleksei Borzenkov](https://github.com/snaury)).
* Adding the ability to register dynamic nodes by certificate. We wont to know how node was registered in node broker. Flag AuthorizeByCertificate is used for this goal. [#11315](https://github.com/ydb-platform/ydb/pull/11315) ([Andrey Molotkov](https://github.com/molotkov-and)).
* Ensure nodes manually set as up do not revert to down. [#11349](https://github.com/ydb-platform/ydb/pull/11349) ([vporyadke](https://github.com/vporyadke)).
* ... [#11384](https://github.com/ydb-platform/ydb/pull/11384) ([Alexey Efimov](https://github.com/adameat)).
* There was wrong name of YDB CLI option in doc. Fix it. [#11391](https://github.com/ydb-platform/ydb/pull/11391) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* The label name for the `RequestsBigLatency` metric is incorrect. [#11410](https://github.com/ydb-platform/ydb/pull/11410) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Appears in REDUCE with multiple inputs if all of them are empty. [#11417](https://github.com/ydb-platform/ydb/pull/11417) ([Roman Udovichenko](https://github.com/rvu1024)).
* Objects with thread storage duration are guaranteed to be destroyed **only** for the thread which calls exit. Therefore there is no guarantee that destruction will happen for objects associated with other threads. This may cause the [blockstore-server](https://github.com/ydb-platform/nbs/tree/main/cloud/blockstore/apps/server) to crash as described below: ``` VERIFY failed (2024-11-06T16:40:28.177019Z):. [#11422](https://github.com/ydb-platform/ydb/pull/11422) ([Mikhail Montsev](https://github.com/SvartMetal)).
* Enforce equal groups in YtCopy and leading operation. [#11435](https://github.com/ydb-platform/ydb/pull/11435) ([Roman Udovichenko](https://github.com/rvu1024)).
* Fix audit log not recording unsuccessful ldap logins. [#11438](https://github.com/ydb-platform/ydb/pull/11438) ([ijon](https://github.com/ijon)).
* I guess it was added accidentally and so it need to be removed. [#11441](https://github.com/ydb-platform/ydb/pull/11441) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* EvWrite: add mvcc snapshot. [#11474](https://github.com/ydb-platform/ydb/pull/11474) ([Nikita Vasilev](https://github.com/nikvas0)).
* A datashard could catch VERIFY during restart with scheme transaction inflight. [#11483](https://github.com/ydb-platform/ydb/pull/11483) ([azevaykin](https://github.com/azevaykin)).
* Added column types validation. [#11487](https://github.com/ydb-platform/ydb/pull/11487) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Performing rw-transactions concurrently with schema operations can lead to disruption of persistent locks and loss of a schema snapshot used for serialization of CDC records. [#11493](https://github.com/ydb-platform/ydb/pull/11493) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#11501](https://github.com/ydb-platform/ydb/pull/11501) ([Alexey Efimov](https://github.com/adameat)).
* ... [#11507](https://github.com/ydb-platform/ydb/pull/11507) ([yumkam](https://github.com/yumkam)).
* Performing rw-transactions concurrently with schema operations can lead to disruption of persistent locks and loss of a schema snapshot used for serialization of CDC records. [#11517](https://github.com/ydb-platform/ydb/pull/11517) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* ... [#11530](https://github.com/ydb-platform/ydb/pull/11530) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* ... [#11548](https://github.com/ydb-platform/ydb/pull/11548) ([yumkam](https://github.com/yumkam)).
* Don't recreate snapshots in transaction. [#11553](https://github.com/ydb-platform/ydb/pull/11553) ([Nikita Vasilev](https://github.com/nikvas0)).
* Fix reads from many shards. [#11569](https://github.com/ydb-platform/ydb/pull/11569) ([Nikita Vasilev](https://github.com/nikvas0)).
* Error appears during column groups calculation, when YtMerge! operation is used only in Left! (as result of empty join optimization for example). [#11575](https://github.com/ydb-platform/ydb/pull/11575) ([Roman Udovichenko](https://github.com/rvu1024)).
* Fixed race with actor context. [#11576](https://github.com/ydb-platform/ydb/pull/11576) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Error appears at YtCopy execution preparation phase, just after SubstTables() call. [#11602](https://github.com/ydb-platform/ydb/pull/11602) ([Roman Udovichenko](https://github.com/rvu1024)).
* YT block input fix for empty input. [#11605](https://github.com/ydb-platform/ydb/pull/11605) ([Mark Ziganshin](https://github.com/loochek)).
* Use async transform for ctas. [#11656](https://github.com/ydb-platform/ydb/pull/11656) ([Nikita Vasilev](https://github.com/nikvas0)).
* ... [#11665](https://github.com/ydb-platform/ydb/pull/11665) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Update yqlrun UI script after YQL move. [#11690](https://github.com/ydb-platform/ydb/pull/11690) ([Andrey Neporada](https://github.com/nepal)).
* Fix excessive memory usage during index-only non-restoring TEvRange query execution. [#11692](https://github.com/ydb-platform/ydb/pull/11692) ([Alexander Rutkovsky](https://github.com/alexvru)).
* GetStorageChannelStatus incremented inline inflight counter but decremented common inflight counter. Now it uses only common inflight counter. [#11702](https://github.com/ydb-platform/ydb/pull/11702) ([kruall](https://github.com/kruall)).
* Preserve suid bit for docker that uses buildkit version < 0.13.0 (https://github.com/moby/buildkit/issues/3920). [#11714](https://github.com/ydb-platform/ydb/pull/11714) ([Aleksei Kobzev](https://github.com/kobzonega)).
* YT block input fix for empty input (second attempt). [#11730](https://github.com/ydb-platform/ydb/pull/11730) ([Mark Ziganshin](https://github.com/loochek)).
* Added brackets during pushdown. [#11742](https://github.com/ydb-platform/ydb/pull/11742) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#11784](https://github.com/ydb-platform/ydb/pull/11784) ([Alexey Efimov](https://github.com/adameat)).
* ... [#11810](https://github.com/ydb-platform/ydb/pull/11810) ([yumkam](https://github.com/yumkam)).
* Fixed data race in json filters. [#11827](https://github.com/ydb-platform/ydb/pull/11827) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix blob recovery actor bug. [#11857](https://github.com/ydb-platform/ydb/pull/11857) ([Alexander Rutkovsky](https://github.com/alexvru)).
* ... [#11865](https://github.com/ydb-platform/ydb/pull/11865) ([yumkam](https://github.com/yumkam)).
* ... [#11869](https://github.com/ydb-platform/ydb/pull/11869) ([Innokentii Mokin](https://github.com/Enjection)).
* ... [#11886](https://github.com/ydb-platform/ydb/pull/11886) ([azevaykin](https://github.com/azevaykin)).
* ... [#11900](https://github.com/ydb-platform/ydb/pull/11900) ([Nikolay Shestakov](https://github.com/nshestakov)).
* Fix [#11193](https://github.com/ydb-platform/ydb/issues/11193). [#11906](https://github.com/ydb-platform/ydb/pull/11906) ([flown4qqqq](https://github.com/flown4qqqq)).
* A race between actors. The actor of the KP session is transferred to the `FinalCleanupState`. In this composition, he does not respond to the `TEvQueryRequest` message from the `TPartitionWriter` actor. [#11920](https://github.com/ydb-platform/ydb/pull/11920) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Add param --explain-ast for ydb sql query. [#11928](https://github.com/ydb-platform/ydb/pull/11928) ([Daniil Timizhev](https://github.com/dahbka-lis)).
* ... [#11947](https://github.com/ydb-platform/ydb/pull/11947) ([Roman Udovichenko](https://github.com/rvu1024)).
* Relaxed memory order that was before allows the effects of constructor of TSamplingThrottlingImpl in UpdateImpl be observed after reading of ImplUpdate in another thread that calls HandleTracing. [#11949](https://github.com/ydb-platform/ydb/pull/11949) ([Vasily Gerasimov](https://github.com/UgnineSirdis)).
* ... [#11975](https://github.com/ydb-platform/ydb/pull/11975) ([Alexey Efimov](https://github.com/adameat)).
* ... [#11978](https://github.com/ydb-platform/ydb/pull/11978) ([Alexey Efimov](https://github.com/adameat)).
* Fix bulk operations potentially breaking frozen locks later causing non-serializable commits. [#12008](https://github.com/ydb-platform/ydb/pull/12008) ([Aleksei Borzenkov](https://github.com/snaury)).
* Missing bits from Arcadia (YQL embedded and YT provider). [#12023](https://github.com/ydb-platform/ydb/pull/12023) ([Andrey Neporada](https://github.com/nepal)).
* ... [#12041](https://github.com/ydb-platform/ydb/pull/12041) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Fix Ranges Compare. [#12043](https://github.com/ydb-platform/ydb/pull/12043) ([Nikita Vasilev](https://github.com/nikvas0)).
* ... [#12068](https://github.com/ydb-platform/ydb/pull/12068) ([yumkam](https://github.com/yumkam)).
* Fixed rope creation. [#12073](https://github.com/ydb-platform/ydb/pull/12073) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#12084](https://github.com/ydb-platform/ydb/pull/12084) ([kruall](https://github.com/kruall)).
* Fix issue that could lead to locked tablets not booting after unlock. [#12109](https://github.com/ydb-platform/ydb/pull/12109) ([vporyadke](https://github.com/vporyadke)).
* Choose automatically only ready indices. [#12146](https://github.com/ydb-platform/ydb/pull/12146) ([Mikhail Surin](https://github.com/ssmike)).
* Fix follower reads sometimes crashing during split. [#12151](https://github.com/ydb-platform/ydb/pull/12151) ([Aleksei Borzenkov](https://github.com/snaury)).
* [YQL-19342][CBO] Use proper error codes. [#12159](https://github.com/ydb-platform/ydb/pull/12159) ([Andrey Neporada](https://github.com/nepal)).
* Fixed a bug where `ydb tools restore` was failing with `Too much data` if `--upload-batch-bytes` option value was set exactly to it's maximum possible value (16MiB). [#12216](https://github.com/ydb-platform/ydb/pull/12216) ([Ilia Shakhov](https://github.com/pixcc)).
* When a transaction is committed, the value of the AvgWriteBytes metric changes. This, in turn, can lead to a split of the partition. [#12220](https://github.com/ydb-platform/ydb/pull/12220) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Add missing tsan.supp file (copy from ydb/library/actors/core). [#12230](https://github.com/ydb-platform/ydb/pull/12230) ([Andrey Neporada](https://github.com/nepal)).
* A typo in audit log. [#12239](https://github.com/ydb-platform/ydb/pull/12239) ([azevaykin](https://github.com/azevaykin)).
* ... [#12265](https://github.com/ydb-platform/ydb/pull/12265) ([Innokentii Mokin](https://github.com/Enjection)).
* ... [#12266](https://github.com/ydb-platform/ydb/pull/12266) ([Innokentii Mokin](https://github.com/Enjection)).
* ... [#12267](https://github.com/ydb-platform/ydb/pull/12267) ([Innokentii Mokin](https://github.com/Enjection)).
* Fixed commit for possible RW tx without writes (like 'update ... set .. where ...' touched no rows) - Fixed Volatile conditions. [#12279](https://github.com/ydb-platform/ydb/pull/12279) ([Nikita Vasilev](https://github.com/nikvas0)).
* When a user tries to connect without the necessary permissions, this error is returned:. [#12287](https://github.com/ydb-platform/ydb/pull/12287) ([azevaykin](https://github.com/azevaykin)).
* Fix PDisk didn't check TEvChunkWrite's offset and wrote data to with an unexpected offset. Add UT for that case. [#12298](https://github.com/ydb-platform/ydb/pull/12298) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Dont consider indices with all pk fields in key. [#12315](https://github.com/ydb-platform/ydb/pull/12315) ([Mikhail Surin](https://github.com/ssmike)).
* CBO at Level 2 was activated when some tables in the queries were not Data Shard tables, and this included AS_Table constructs and parameters. [#12322](https://github.com/ydb-platform/ydb/pull/12322) ([Pavel Velikhov](https://github.com/pavelvelikhov)).
* Sometime PDisk looses replies, so add more debug assertions. [#12331](https://github.com/ydb-platform/ydb/pull/12331) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* The partition periodically transmits a set of `PQ/*` indicators to the PQ tablet. This is also done by the service partition for writing to the transaction. If the duration of the transaction is less than the period of transfer of indicators, then part of the data was lost. Now, the service partition transmits the accumulated indicators to the PQ tablet before deletion. [#12337](https://github.com/ydb-platform/ydb/pull/12337) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* In the `linux-x86_64-release-asan` configuration, the `ReadFromTopic` function does not have time to return the expected number of messages. Replaced with calls `Read_Exactly_N_Messages_From_Topic`. [#12364](https://github.com/ydb-platform/ydb/pull/12364) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* ... [#12391](https://github.com/ydb-platform/ydb/pull/12391) ([Alexey Efimov](https://github.com/adameat)).
* MovedPatch uses some vectors that were allocated only during VPatch. Now they are also allocated during MovedPatch if they were not initially allocated. [#12418](https://github.com/ydb-platform/ydb/pull/12418) ([kruall](https://github.com/kruall)).
* During the previous refactoring, the template argument was omitted in the function call to GetAvgPartForLastSeconds. However, the method contained a bug when WithTail=false, causing incorrect calculations. Fixed this issue and added tests for TValueHistory. [#12422](https://github.com/ydb-platform/ydb/pull/12422) ([kruall](https://github.com/kruall)).
* ... [#12446](https://github.com/ydb-platform/ydb/pull/12446) ([Alexey Efimov](https://github.com/adameat)).
* ... [#12447](https://github.com/ydb-platform/ydb/pull/12447) ([Nikolay Shestakov](https://github.com/nshestakov)).
* Fixed uncaught exception error. [#12465](https://github.com/ydb-platform/ydb/pull/12465) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Changed `GetOperationResponse` parsing so that `/operation/get` start to return stats if paramater `stats_mode` is passed. [#12478](https://github.com/ydb-platform/ydb/pull/12478) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* ... [#12479](https://github.com/ydb-platform/ydb/pull/12479) ([Nikolay Shestakov](https://github.com/nshestakov)).
* ... [#12516](https://github.com/ydb-platform/ydb/pull/12516) ([Vlad Kuznetsov](https://github.com/va-kuznecov)).
* Fix GetBlock for BlobDepot. [#12525](https://github.com/ydb-platform/ydb/pull/12525) ([mregrock](https://github.com/mregrock)).
* ... [#12568](https://github.com/ydb-platform/ydb/pull/12568) ([zverevgeny](https://github.com/zverevgeny)).
* Bugfix in PQRB (potential loss of metrics for new consumers). [#12613](https://github.com/ydb-platform/ydb/pull/12613) ([FloatingCrowbar](https://github.com/FloatingCrowbar)).
* Fix not working balancing command in some cases. [#12668](https://github.com/ydb-platform/ydb/pull/12668) ([kruall](https://github.com/kruall)).
* Https://github.com/ydb-platform/ydb/issues/11923. [#12678](https://github.com/ydb-platform/ydb/pull/12678) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Fixed `SCHEMESHARD_CDC_STREAM_SCAN_FINALIZER` actor leak. [#12679](https://github.com/ydb-platform/ydb/pull/12679) ([Ilnaz Nizametdinov](https://github.com/CyberROFL)).
* Rollback some changes from [#12403](https://github.com/ydb-platform/ydb/issues/12403). [#12690](https://github.com/ydb-platform/ydb/pull/12690) ([Aleksey Myasnikov](https://github.com/asmyasnikov)).
* Fix error message [#10853](https://github.com/ydb-platform/ydb/issues/10853). [#12701](https://github.com/ydb-platform/ydb/pull/12701) ([Mikhail Surin](https://github.com/ssmike)).
* Fixed fault for parsing errors without filter. [#12707](https://github.com/ydb-platform/ydb/pull/12707) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fixed memory leak in filters. [#12739](https://github.com/ydb-platform/ydb/pull/12739) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fixed missing historical data. [#12757](https://github.com/ydb-platform/ydb/pull/12757) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* ... [#12777](https://github.com/ydb-platform/ydb/pull/12777) ([Alexey Efimov](https://github.com/adameat)).
* Fix disconnected proxies unexpectedly registering in coordination service. [#12782](https://github.com/ydb-platform/ydb/pull/12782) ([Aleksei Borzenkov](https://github.com/snaury)).
* Fix a bug where restart count was returned on the wrong window. [#12789](https://github.com/ydb-platform/ydb/pull/12789) ([vporyadke](https://github.com/vporyadke)).
* ... [#12805](https://github.com/ydb-platform/ydb/pull/12805) ([Alexey Efimov](https://github.com/adameat)).
* Canonize storage path in CS Tiers. [#12833](https://github.com/ydb-platform/ydb/pull/12833) ([Semyon](https://github.com/swalrus1)).
* The function returns an empty view that does not point to local memory on the stack, which makes it difficult to track the lifetime of string buffers. It is also requires less time to directly construct the view. [#12835](https://github.com/ydb-platform/ydb/pull/12835) ([ubyte](https://github.com/ubyte)).
* Fix parsing S3 settings on CS. [#12856](https://github.com/ydb-platform/ydb/pull/12856) ([Semyon](https://github.com/swalrus1)).
* In some proxy responses, CORS headers were missing. [#12877](https://github.com/ydb-platform/ydb/pull/12877) ([Andrei Rykov](https://github.com/StekPerepolnen)).
* Fixed the errors: 1. The program did not take into account that it can receive a `TEvReadSet` more times than the number of senders in `TEvProposeTransaction`. Deleted the check from `Y_ABORT_UNLESS'. 2. Replaced the `Y_ABORT_UNLESS` checks with the `ForceFalse` flag. Instead of an abnormal termination, the program returns `ABORTED`. [#12905](https://github.com/ydb-platform/ydb/pull/12905) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fix `ydb_configure` generation for section `host_configs` in static config. [#12920](https://github.com/ydb-platform/ydb/pull/12920) ([Aleksei Kobzev](https://github.com/kobzonega)).
* ... [#12927](https://github.com/ydb-platform/ydb/pull/12927) ([Innokentii Mokin](https://github.com/Enjection)).
* Avoid creating forever-running thread pools for each S3 client instance. [#12963](https://github.com/ydb-platform/ydb/pull/12963) ([Maksim Zinal](https://github.com/zinal)).
* Fixed empty error from CMS create tenant request (issue [#12973](https://github.com/ydb-platform/ydb/issues/12973)). [#12977](https://github.com/ydb-platform/ydb/pull/12977) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix for [YQ-3956](https://st.yandex-team.ru/YQ-3956). [#12985](https://github.com/ydb-platform/ydb/pull/12985) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fix for [YQ-3919](https://st.yandex-team.ru/YQ-3919). [#12987](https://github.com/ydb-platform/ydb/pull/12987) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fix BufferActor termination - Don't wait for last ack in FwdActor - More metrics - Fixed errors. [#12999](https://github.com/ydb-platform/ydb/pull/12999) ([Nikita Vasilev](https://github.com/nikvas0)).
* Rename muted sinks ut for topics. [#13000](https://github.com/ydb-platform/ydb/pull/13000) ([Daniil Timizhev](https://github.com/dahbka-lis)).
* Fix parsing input path in ydbd cli commands (`ydbd schema` subcommands). [#13001](https://github.com/ydb-platform/ydb/pull/13001) ([ijon](https://github.com/ijon)).
* Fix ub with std::optional *nullopt for immediate commit with topic. [#13006](https://github.com/ydb-platform/ydb/pull/13006) ([Daniil Timizhev](https://github.com/dahbka-lis)).
* ... [#13019](https://github.com/ydb-platform/ydb/pull/13019) ([Alexey Efimov](https://github.com/adameat)).
* ... [#13021](https://github.com/ydb-platform/ydb/pull/13021) ([Alexey Efimov](https://github.com/adameat)).
* ... [#13024](https://github.com/ydb-platform/ydb/pull/13024) ([Alexey Efimov](https://github.com/adameat)).
* ... [#13034](https://github.com/ydb-platform/ydb/pull/13034) ([Alexey Efimov](https://github.com/adameat)).
* Rename gcc_version to version. [#13053](https://github.com/ydb-platform/ydb/pull/13053) ([Dmitrii Dmitriev](https://github.com/dimdim1177)).
* The service partition can receive the `TEvGetWriteInfoRequest` message in the `StateInit` state. In this case, it postpones the message to the `PendingEvents` queue. When the service partition switches to the `StateIdle` state she sends herself all the accumulated messages. The service partition may receive a `TEvGetWriteInfoRequest` message with an empty sender address in the `StateIdle` state. As a result, the responses `TEvGetWriteInfoResponse` and `TEvGetWriteInfoError` are lost. [#13066](https://github.com/ydb-platform/ydb/pull/13066) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Fixes creating unrestorable S3 backups when splitting and merging the table. [#13067](https://github.com/ydb-platform/ydb/pull/13067) ([Ilia Shakhov](https://github.com/pixcc)).
* Fix deferred PDisk start logic with distconf. [#13082](https://github.com/ydb-platform/ydb/pull/13082) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fix SelfManagement section absence check. [#13087](https://github.com/ydb-platform/ydb/pull/13087) ([mregrock](https://github.com/mregrock)).
* Fixed pq source sensors names. [#13088](https://github.com/ydb-platform/ydb/pull/13088) ([Pisarenko Grigoriy](https://github.com/GrigoriyPA)).
* Fix linking in nodewarden. [#13105](https://github.com/ydb-platform/ydb/pull/13105) ([mregrock](https://github.com/mregrock)).
* ... [#13118](https://github.com/ydb-platform/ydb/pull/13118) ([yumkam](https://github.com/yumkam)).
* After the transaction is completed, the program pushes forward the `ExecStep`. The transaction itself is not deleted until it receives a `TEvReadSetAck` from other tablets. After restarting, the tablet excludes transactions with `Step < ExecStep`. As a result, the transaction may hang in other tablets. [#13134](https://github.com/ydb-platform/ydb/pull/13134) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* [ydbd_slice] fixed Namespace error on ydbd_slice update. [#13171](https://github.com/ydb-platform/ydb/pull/13171) ([Alexander Petrukhin](https://github.com/shmel1k)).
* Fix ColumnShardArbiter shard sets. [#13214](https://github.com/ydb-platform/ydb/pull/13214) ([Nikita Vasilev](https://github.com/nikvas0)).
* ... [#13229](https://github.com/ydb-platform/ydb/pull/13229) ([Alexey Efimov](https://github.com/adameat)).
* ... [#13243](https://github.com/ydb-platform/ydb/pull/13243) ([yumkam](https://github.com/yumkam)).
* The test breaks if you run all the tests in the `ydb/core/persqueue/ut` subdirectory. If you run it separately, it completes without an error. [#13271](https://github.com/ydb-platform/ydb/pull/13271) ([Alek5andr-Kotov](https://github.com/Alek5andr-Kotov)).
* Depending on the version of STL used, its configuration, and the distribution of sortable elements, the std::sort algorithm may compare some element with itself (for example, libcxx can do this). In that case, the sorting predicate is obliged to return the value `false`, and not lead to an abortion. [#13296](https://github.com/ydb-platform/ydb/pull/13296) ([ubyte](https://github.com/ubyte)).
* Fix UB caused by comparator not defining a valid strict-weak ordering. [#13303](https://github.com/ydb-platform/ydb/pull/13303) ([ubyte](https://github.com/ubyte)).
* Fix typo. [#13311](https://github.com/ydb-platform/ydb/pull/13311) ([Alexander Rutkovsky](https://github.com/alexvru)).
* Fix network filter any. [#13360](https://github.com/ydb-platform/ydb/pull/13360) ([Alexey Efimov](https://github.com/adameat)).
* исправление для [YQ-3957](https://st.yandex-team.ru/YQ-3957). [#13391](https://github.com/ydb-platform/ydb/pull/13391) ([Ivan Sukhov](https://github.com/evanevanevanevannnn)).
* Fix possible node crash in HTML rendering code. [#13408](https://github.com/ydb-platform/ydb/pull/13408) ([AlexSm](https://github.com/alexv-smirnov)).
* Handle multiple streamlookup joins in query. [#13426](https://github.com/ydb-platform/ydb/pull/13426) ([yumkam](https://github.com/yumkam)).
* Avoid underflow on requests count. [#13433](https://github.com/ydb-platform/ydb/pull/13433) ([Alexey Efimov](https://github.com/adameat)).
* Fix uncommitted changes leak and clean them up on startup. [#13444](https://github.com/ydb-platform/ydb/pull/13444) ([Aleksei Borzenkov](https://github.com/snaury)).
* Fix buffer actor leak. [#13551](https://github.com/ydb-platform/ydb/pull/13551) ([Nikita Vasilev](https://github.com/nikvas0)).
* Scheme proto propagation could be slow in some races and new code can return old proto. In this case we should not throw exception. [#13555](https://github.com/ydb-platform/ydb/pull/13555) ([azevaykin](https://github.com/azevaykin)).
* Use smart pointers in unit tests for harmonizer. [#13560](https://github.com/ydb-platform/ydb/pull/13560) ([Sergey Belyakov](https://github.com/serbel324)).
* ... [#13572](https://github.com/ydb-platform/ydb/pull/13572) ([Alexey Efimov](https://github.com/adameat)).
* Fix cfg tool. [#13582](https://github.com/ydb-platform/ydb/pull/13582) ([mregrock](https://github.com/mregrock)).
* ... [#13628](https://github.com/ydb-platform/ydb/pull/13628) ([Alexey Efimov](https://github.com/adameat)).
* Fixed a bug where arm64 YDB CLI binary was downloading amd64 binary to replace itself during `ydb update`. To update already installed binaries to the latest arm64 version, YDB CLI should be re-installed ... [#13669](https://github.com/ydb-platform/ydb/pull/13669) ([Nikolay Perfilov](https://github.com/pnv1)).
* TYdbErrorException constructor uses moved value, that leads to segfault. [#13736](https://github.com/ydb-platform/ydb/pull/13736) ([Bulat](https://github.com/Gazizonoki)).
* Fix metadata handling in configs. [#13741](https://github.com/ydb-platform/ydb/pull/13741) ([Innokentii Mokin](https://github.com/Enjection)).
* Fix baremetal none-1-node template. [#13742](https://github.com/ydb-platform/ydb/pull/13742) ([Konstantin Nikiforov](https://github.com/melazyk)).
* Original PR: https://github.com/ydb-platform/ydb/pull/13658. [#13761](https://github.com/ydb-platform/ydb/pull/13761) ([Bulat](https://github.com/Gazizonoki)).
* Allow to work without volatile - Don't create a lot of actors at one mailbox - Wait for all shards to commit - Changed error for undelivered message to buffer actor. [#13786](https://github.com/ydb-platform/ydb/pull/13786) ([Nikita Vasilev](https://github.com/nikvas0)).
* Fix getting max pk in a portion as eviction border on CS. [#13806](https://github.com/ydb-platform/ydb/pull/13806) ([Semyon](https://github.com/swalrus1)).
* Fix weight actualization delay in CS optimizer. [#13812](https://github.com/ydb-platform/ydb/pull/13812) ([Semyon](https://github.com/swalrus1)).
* Fix unexpected message. [#13813](https://github.com/ydb-platform/ydb/pull/13813) ([Nikita Vasilev](https://github.com/nikvas0)).
* When loading metadata from the YDB side, optional type was no longer added to the data type. [#13815](https://github.com/ydb-platform/ydb/pull/13815) ([azevaykin](https://github.com/azevaykin)).