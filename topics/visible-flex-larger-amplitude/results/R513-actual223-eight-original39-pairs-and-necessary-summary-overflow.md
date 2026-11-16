# R513：actual223 八个原39 warm/FD交接与单份必要摘要再次超限

作者：OpenAI ChatGPT，/root/geometry（AI）。日期：2026-11-16 UTC。  
性质与可信度：已核实的本次官方终态、原stdout元数据和对应已固定源码控制流；本次完整科学必要正文没有返回。没有新数值计算、补算或旧运行结果移用。

## 513.1 实际结论与读取范围

本次 actual223 真实执行了 batch 0至7的八个原完整39模型和八个对该批新warm执行的原boundary FD。十六个child的实际退出码都是0，且原stderr均为空。每批原retirement事件还明确返回 `next_actual_parent_pair_retained=true`。结合实际执行源码f847b2df的原布尔形成，可确认八次原warm/FD交接eligible成立；这项有限结论有原事件和原控制流双重来源，不是从exit0单独推出验收。

随后发生的是必要读回超限：第一次whole-chain为113011 B，always恢复为113361 B，两份都超过原90000 B上限，均退出70，均没有完整summary frame正文。未返的全部α、merit、科学失败地址、FD数值、末三参数、最终pair和实际formatter操作统计仍未返，不填零、不据SHA恢复、不拿actual206/213结果补本次。特别是“原warm进展接受＋原fresh FD交接”不等于native、fullDN、完整闭面或整个课题完成。

step11在Actions显示success，但实际输出是 `request223_owned_cleanup_skipped`。批间已经按原控制流删除各批大raw；终末保留的necessary记录和最新parent没有被本次workflow清理，保到临时runner生命周期结束。不能把这两层清理合并成“所有raw已保”或“全体已删”。下文列全部实际范围。

唯一科学日志来源为[官方actual223 job](https://github.com/Rogerhu12/math-research-public/actions/runs/43839064900/job/133202897349)。geometry只在官方终态后下载该job日志一次，未取运行中日志，也未另外恢复artifact或下载临时大科学表。

## 513.2 官方run、源和原合同

| 项目 | 实际值 |
|---|---|
| 仓库 | Rogerhu12/math-research-public |
| run / attempt | 43839064900 / 1 |
| 实际head_sha | 035d28663109b4d94a48c4223c29f06d88796978 |
| 官方创建时间 | 2026-11-16T09:21:53Z |
| compute job | 133202897349；original-thirty-nine-actual-role-batches |
| workflow | .github/workflows/visible-larger-public-thirty-nine-actual-role-batches.yml |
| workflow完整字节 | 20571 B / c8ac3fcd6e6a229d463130ef79da1b62d5a8f44dc3e3513fa963759e8c81f4ae |
| 本次request | computations/public-thirty-nine-actual-role-batch-request.json |
| request完整字节 | 26960 B / 2d9df5946d429c3888013099989b2f5170a89556462e4ab1535cf127c7bbfaeb |
| 实际recipe | computations/public-thirty-nine-actual-role-model-recipe.json |
| recipe完整字节 | 44258 B / 3abc2e63f7a2043e1d9ba75d1d69df53d80baf11b95ab961e75cbc9088848a0e |
| request schema | thirty_nine-real-pair-actual-role-continuation-request-v1 |
| worker schema | thirty_nine-real-pair-actual-role-batches-v1 |
| 整份官方工具返回日志 | 116544 UTF-8 B / c65d0226579d881538b670e9791fb6cfe363aadfdeb1f6c392bbe807f61f07ba |

日志身份指connector返回的完整已解码UTF-8文本，保留原时间戳、一个首BOM和终换行；不是另一个未读取HTTP归档的身份。按LF切分有798项，包含末尾空项。分析时逐物理行先剥该行首单BOM，再剥实际时间戳；记录原全文hash时没有做这些变换。全68个顶层JSON事件已解析；原shell展示行没有当作实际事件。

实际checkout日志明确checkout上述035d2866；不以较早准备提交替代这个实际源。第一source frame和后续chain_started也返回同一source。全文合同见[223完整来源接口](../notes/2026-11-16-request223-actual39-producer-role-context-interface.md)，11937 B / 9d45c8edbaec21e27d8bdbb07d89e6fcc476d7710e7bce94c606801a7bd22cac；[R512](R512-complete39-actual-producer-role-context-binding.md)只修原必要表真实角色绑定，未改原模型/FD计算。

原初父仍为actual98：run43677587785/source918fdb11dbb7a424b6149b405e2c7fab3cc0c737，artifact14147700690，原合同809042943 B / 9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a。warm是4927052 B / b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67，status是3379453 B / b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff。这里列原冻结输入合同；本次chain_started的实际完整输入绑定只返回8919 B / fa6317c45c125e0e9a96977379623aeb678fcf9a462d36442534b78e362f22cf身份，正文未返回。第一真实child argv另直接显示上述warm/status SHA。

本次未把actual171、191、200、206、213删后父或未返科学值冒作当前输入。旧来源保留仅为明确祖先和相同原数学源码。

## 513.3 四源真实生成、原116身份及规则字节

source生成真正返回完整frame：

`BEGIN_REQUEST223_SOURCE_VIEWS_METADATA` 至 `END_REQUEST223_SOURCE_VIEWS_METADATA`。

帧中JSON正文含一LF为5198 B / 8c7c6d08e4948ee772a4f968941d6ae1afe522ccf9091a325590499a6776586b，与原receipt相同；不含末LF为5197 B / 90e371ce638547b30c6df032bdf2ea537247b50d87313b3454cb235fe705febf。该全文已读。它只确认来源生成，原 `scientific_process_started=false` 是这个source步骤的范围，不能外推整job科学未起。

generator为8310 B / 1368e4cbe4766d455bcbe3b464d2830e9a2a93e76915c70df085309fc856f291；plan为11271 B / 6d700bb6e5da4ca24cad23ba37cda9dea3852802461bcf8465988ff4976c8125。原formatter为20883 B / f79328ed83fee9757de1f5987067a0187b5cba53d7daf5b82a610149540ebd54。四目标均在实际原public computations目录生成，all_generated_sources_complete=true、exit_code=0：

| 实际生成basename | B | SHA-256 | 此运行职责 |
|---|---:|---|---|
| root_20261116_thirty_nine_context_chain_readout.py | 75610 | 3160c22d42abb1103ba1f1d3d71b172fbfe6d09cd938ecb7fac1bc5032ae11b5 | 保祖先213身份 |
| geometry_20261116_thirty_nine_context_batches.py | 29658 | 3c2cdcd9cfa0d756413afb9b5b67edb81a81db3d1f69f4836f08be3c0e401ba3 | 保祖先213身份 |
| root_20261116_thirty_nine_actual_role_chain_readout.py | 75639 | eabd68de700ba2409e59c5ccac3d7230075fe699c389774dde83755c533c4c3f | 当前223必要读取 |
| geometry_20261116_thirty_nine_actual_role_batches.py | 29678 | f847b2dfbe28fe791726b66052d6fba4f080a2954be6a08e26309944a43d00b8 | 当前223实际worker |

helper各15个literal replacement的实际次数依次为1,1,1,1,2,20,2,1,1,1,1,1,1,1,1；worker各12项次数为2,7,3,2,1,1,1,1,1,1,1,1。两祖先/两当前各自全字节核回。后续source_bytes_checked实际返回112public＋4generated=116，保actual206的108及actual213的112，parameters=1；没有从计数推任意动态import闭包。

原root README的实际10233 B / 6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9，Git blob21bd547f56590b7f2dd279d0297efb289a9b2783；课题README的2664 B / 3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d，blob bff8aea253a9e6a7a4fac28d810ac454c5499fec。源生成、原pin/AST及原历史输入寻址step1至7实际success，不是从后续完成倒推前置通过。

## 513.4 原39科学范围和真实执行配置

source_bytes_checked明确：39 queries、原新增RIGHT459 fraction0.8273268353539885、实际endpoint为459、460及462至491；26个capture intervals，32个endpoint，B local10819、C4059、33节点cover11266、实际front10928，free461完整QR消去，不填伪零B列。source_contract是完整原22 LEFT/16 MID/1 RIGHT；这不构成实际全部query误差已经返回。

实际八次model argv使用同一原 `geometry_20261115_thirty_nine_query_collocation_observer_warm.py`，每次真实新输出的warm交给原 `geometry_20261115_thirty_nine_query_condensed_response.py`。每个FD的prepared路径均为该batch的 `thirty-nine-condensed-warm/warm-001.json.gz`，不是原初父或上一FD报告。

| 原配置 | 本次值 |
|---|---|
| 最大pair / 批间预算 | 8 / 10500秒；恢复原输入/public source后开始批间钟 |
| 单model iterations / damping | 1 / 270 |
| lsmr iterations / projection sweeps / dual sweeps | 200 / 200 / 200 |
| line-search steps | 17 |
| model / condensed budget | 1200 / 600秒 |
| trial / recovery reserve | 90 / 30秒 |
| working rows / angles / jac-workers | 512 / 4096 / 2 |
| 科学step / job / always-readback | 175 / 195 / 10分钟 |
| rules同步周期 | 2700秒 |
| Python / NumPy / SciPy | 3.12.14 / 2.3.5 / 1.17.0 |
| BLAS、OMP、MKL、NumExpr线程 | 1 |

原控制流不把批间钟冒成覆盖所有setup的总硬截止。日志中的chain_started时间是09:23:17.7156057Z；rules从09:22:17 UTC开始，整wrapper于10:45:17 UTC结束。没有从子call elapsed求和制造原未返的 `actual_elapsed_batch_loop_seconds`。

实际十六child的原elapsed字词如下；只抄运行记录，不重算科学：

| batch | model elapsed_seconds | FD elapsed_seconds | 实际exit model / FD |
|---:|---:|---:|---|
| 0 | 625.972973397 | 17.601833070999987 | 0 / 0 |
| 1 | 612.2669501930001 | 17.75550568299991 | 0 / 0 |
| 2 | 603.5062266820003 | 18.549568889000057 | 0 / 0 |
| 3 | 597.6848395669999 | 17.658228673000394 | 0 / 0 |
| 4 | 586.5347574500001 | 17.634969273000024 | 0 / 0 |
| 5 | 576.352383684 | 17.609744545000012 | 0 / 0 |
| 6 | 580.1513324849998 | 17.63218653199965 | 0 / 0 |
| 7 | 587.838934419 | 17.724018113000056 | 0 / 0 |

全部十六stderr均实际present=true、bytes=0、SHA=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855、text=""、complete_original_stderr_text=true。stdout只返身份，见513.9；不能凭空stderr推所有数学门通过。

## 513.5 原eligible的确切有限含义

这里另作一次纯源码定位：从本次固定035d源取原206 worker29658 B / 59276c9eae96071211d8990a1b260faf0cc534e7efea3c4e9fd49a59213d7643，按上述实际223 plan12项完整literal仅作文本替换，核回当前f847b2df/29678 B。没有import、AST或执行该源。

当前真实 `run_batch` 的原条件是：

1. model_code=0、原status.optimization_progress=true、accepted_warm_steps=1，才进入完整pair校验。
2. `validate_completed_pair` 要求原optimizer schema、原status与warm的success=false、new_coupled_finite_acceptance=false、真实warm文件名/完整SHA和producer identity配对相等。这份warm明确是进展初猜，不是新耦合接受。
3. 对该实际warm重新运行FD；只有fd_code=0、原report.implementation_check_passed=true、report.prepared_sha256等于这份warm SHA，且complete_current_warm_boundary_FD_actually_recomputed=true，才将eligible置true。
4. main在必要batch记录已经落盘后，只在eligible真时实际move两文件并更新下一父；随后输出的 `next_actual_parent_pair_retained` 正是bool(eligible)，不是另一个宽松标签。

本次八条实际 `thirty_nine_batch_payload_retired` 都把该原字段返回true。因此可报告八次原有限warm进展及fresh-FD交接成立。没有给未返回的原FD每方向/每级误差赋数，没有把八次进展称为native、fullDN、coupled acceptance或课题验收；原worker在这个支线始终不请求native/fullDN。

下一批命令还保了前一真实pair的字节身份，形成以下实际输入链。只有这些完整SHA，不能恢复对应场或末参数：

| batch输入 | 路径后缀 | warm SHA-256 | status SHA-256 |
|---:|---|---|---|
| 0 | parent98/warm-001.json.gz | b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67 | b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff |
| 1 | parent-after-000/warm-001.json.gz | 3e02b158c0e7c0d86052f920c5942c40782792dd27fad671dec6d879c54d951a | e6fe7648232ac5b644f1af82885567505bf8eb2fc227e87cdb68ee32c2cd2df1 |
| 2 | parent-after-001/warm-001.json.gz | 3b74d09cfb26bcca70833ae72111cc4a0ca133c54afebc31f5a59cc3bc2eb08a | b109e520b40b31a91ab4a166ee24e58ece964919a8f0c9d14dc94e2c45666829 |
| 3 | parent-after-002/warm-001.json.gz | 07141d764e03a2c96218bd359c62162ce38a6790234bbab6ed44a999a1b6f1e9 | d40a3484836e21c81cabccc59b1912861a85222e587bb309a9d6b6b4d1eea105 |
| 4 | parent-after-003/warm-001.json.gz | 5ea5e815562594fb0f5d0c8fef3ec2a21219ec0cac56fb8f5a3444d9b083c8fa | 94d99c0ddce49f642a5973e0ca9dba36bab468434044ad7142644a1b460dbda6 |
| 5 | parent-after-004/warm-001.json.gz | e110431538f8fe0871a9ea5ccd39b5c3cdfce08cc4173753a48518d10a3d001f | 70ba9f3270844c40c376b55c874b1a64da94e4a90fe652151c2e1bb0a482c420 |
| 6 | parent-after-005/warm-001.json.gz | 56ffb7deb71a3a415e691268cb7dfd07f0ca3ffdc756a3cceec773e786a673a5 | 5549a566e0e4b0cd669b7efa06b69608b7ac90d38d1e6922c08eab2105832efa |
| 7 | parent-after-006/warm-001.json.gz | 08c26a0835e556dcf7cef40164d8e64cf0fe344d9f8efabc09097c96672584bc | bc67e9d281c657c4db389a156d930e24ab8949876952c1b38de47289072371af |

batch7的输出parent-after-007没有下一条科学命令帮忙返回其两SHA；最终whole-chain正文又未返。因此不补这个最终pair身份，也不把batch7输入parent-after-006说成全八批最终点。

## 513.6 八份耐久必要记录与未返科学正文

原save事件每批都返回完整trial计数及必要文件身份；文件名依次batch-000.json至batch-007.json：

| batch | complete_original_trial_count | 必要文件B | SHA-256 | 原next_actual_parent_pair_retained |
|---:|---:|---:|---|---|
| 0 | 4 | 30386 | e78fb40a4f4b78e830898ed6af220ef6d7cc4465b36cec91314d7d87ef850cd9 | true |
| 1 | 3 | 30526 | 8d26e3a6b3b962eac0b837cf9b347a604ead24eaf40ef7b90222ce0703494cfe | true |
| 2 | 4 | 33970 | 37f8854a10a7e82f55f16ff33bc7f778caab0a2971f628c4bce311c27f2efebe | true |
| 3 | 3 | 29627 | 46b4893c6df176bae4e96e1ebbbbd0e4b134f3736044a60f1656f11a50ad3143 | true |
| 4 | 3 | 29230 | 60f1a661a13232a6ad3496635561b2883e820121e4b95c4a6286d258a57d6471 | true |
| 5 | 2 | 25950 | 8613c6523dfbc9b361730669f8619462e7f0dc156488e04205271354a9de4ae8 | true |
| 6 | 2 | 24053 | cc7543c5047e4d28a5d8ef6547a4d4d6bf50bb11b6f19736b41864c186c580e0 | true |
| 7 | 3 | 29867 | 384016d8829a084e486a26d493b088fa288861f9d252b2e3e5cb1e78c6efd960 | true |

这些是原必要文件身份及原已返计数。它们不包含被读回正文中的trial字词：各α、原norm/merit、所有失败query和原RMS sample、FD contraction值、QP诊断、三个实际参数仍不得由计数或SHA代填。没有将八份必要文件从GitHub另取、分拆编码上传或多帧拼接。原Input绑定8919B也只返identity。

source中记录原完整trial/失败字段并在Actions内读取它们，与本工具已经读到那些正文是两件不同的事实。本文严格只认原日志已返回的元数据和上述控制流布尔。

## 513.7 两次真实90K失败，原报错及终末未付

| 读回 | 实际含LF B | SHA-256 | summary_complete | exit |
|---|---:|---|---|---:|
| whole-chain | 113011 | fc09d2c15d0766e8dc9cf44d9bc703d347e732ef13112879e4693bd54384bccb | false | 70 |
| whole-chain-recovery | 113361 | 1cc79306832a6581884170e9769692d1bc6c839f60e344a27253ea11609331bb | false | 70 |

两次原reason均为 `necessary-summary-exceeds-90000-bytes`；`full_result_not_split_or_encoded=true`、`unread_necessary_records_retained=true`、`prior_large_raw_may_have_retired_after_durable_necessary_selection=true`。

原完整异常文字为：

> Necessary summary exceeds90000; preserve unread necessary records and surviving raw

第一trace精确经过当前worker的main→helper.finish_chain→publish，原helper在publish抛ReadbackIncomplete；整科学wrapper因这个读回异常返回70。原orchestration_failure保phase=`original-new-warm-FD`、batch_index=7、science_started=true、native_or_full_DN_called=false。这个最后phase不是第八FD的失败标签；实际第八FD已另返exit0，异常栈指向后续whole-chain publish。

always步骤真实先完成quiet，再重组necessary，仍113361B超限，随后返回 `request223_readback_incomplete`。完整log仅有source-views的BEGIN/END frame，**不存在**whole-chain或whole-chain-recovery的BEGIN/END正文。本文没有把两个SHA表示的正文当成已读，也没有拿第一次、第二次互补拼成科学结果。

这次R512的真实角色修复已通过来源/生成并实际执行，但未实现整个必要文档≤90K；原输出没有返回各项formatter operations计数、各表体积或具体节省归因，因此不能把剩余超限再归为某个已确认字段。原90K界保留，不能为获得green而删必要错误/未访或抬界。

## 513.8 rules、quiet与清理边界

原rules最终对象482 B / 3b571639735ce2b58ea68e761b9b01030556bfd6fc67a7a4913d82907b3d71cd，全文实际已返回：

| 原字段 | 原值 |
|---|---|
| schema | current576-rules-runner-result-v1 |
| started_utc / finished_utc | 2026-11-16 09:22:17 UTC / 2026-11-16 10:45:17 UTC |
| science_returncode / wrapper_returncode | 70 / 70 |
| periodic_sync_failures | [] |
| README_change | null |
| science_terminated_for_actual_rule_change | false |
| partial_scientific_files_not_removed | true |
| scientific_checkout_modified | false |
| original_scientific_argv_and_budget_preserved | true |
| sync_rounds_started | 2 |

两次实际rules同步分别是：round0于09:22:17读main cb2385cca1fd2c336c7da0e3070bde77129e8e17，发布4dd7b9b8cc4d0aa26e4f117ef9e39a895d459bc6；round1于10:07:21读f0bdd1d23c20a6aa2a41b144d980df0bf7ff2b8a，发布77f899dc742db5f8520bde17b284118c66a03cd2。没有rules-change中止或periodic sync error。

原owner登记768 B / 2ef383d32b04104512901349fbbb3fe15489ac1d4748551d3a88e389060fcbdc，初登记pid2453、ppid2324、pgid2453、sid2453、start_ticks30193。always的真实quiet记录绑定同run/attempt/source与helper eabd68de；signals=[]、unknown_scope=[]、before=[]、after=[]、live_original_group_after=[]、quiescent=true。该记录明确只覆盖原登记scope，未声称任意脱离登记的child；原state=R是先前owner记录，不是当时仍活的判定。

每批batch_payload_removed=true，原已形成必要记录后退该批大表；eligible真时最新pair移到parent-after-i并退上一父。这些删除确实发生，不能因最终skip而倒称原大batch目录仍在。最终whole-chain异常触发 `request223_unread_namespace_retained`，真实namespace为 `visible-thirty-nine-223-hmy6x4lh`。

最终workflow step11只输出cleanup_skipped，原因字段为source_generation=success、necessary_readback=failure、rules_readback=success。它没有执行成功读回后的第二次fresh quiet及rmtree分支。所有仍存necessary/末父保到runner销毁，不能承诺job结束后还能读取；没有artifact、Release或Git raw上传。Actions自己的checkout post-cleanup和orphan-process清理，不等于本题数据已读/有权限删的证明。

## 513.9 实际子stdout身份与完整性边界

以下完整stdout只在Actions临时保存，官方日志返回其bytes/SHA，没有返回科学body；stderr空文本已在513.4列清：

| batch | 原角色 | stdout B | SHA-256 |
|---:|---|---:|---|
| 0 | original-model | 151255 | 438617d25c333fe35694cb0ebb67110cf727e23ed55aaa9784bbff513fb01db7 |
| 0 | original-boundary-FD | 171 | d481e1f5360451f658c6c1cc45ee08955bb2d5f14c971bd827a8b44d65417276 |
| 1 | original-model | 151397 | f68453c08ccc827ded8a33f0332525b1bf0a01cca60aac345469a3b2bd1b8c5b |
| 1 | original-boundary-FD | 178 | f8447f441315af15f79e8034522edf51f4433a987052d4ab532d74c27424743b |
| 2 | original-model | 151553 | 5e3143c670733033a22b3994de1c03466c2c094cc9aacf576fa1fe554098774e |
| 2 | original-boundary-FD | 177 | 0bf080a7a6f3409716f98e09b19b21f720744776a254a60e32146557742ef545 |
| 3 | original-model | 151511 | 7e0e17e9f13bc33ef1fa5d63ee53337bb376f60435c0f5c0c62359efe4b47356 |
| 3 | original-boundary-FD | 178 | e24daee626a5cf573c4f55ee4348676e07cb48d2aa166c07aeb9727065367d4b |
| 4 | original-model | 151546 | 8268032945bcde1ef71585261ca59ac9e5a00f94e960f12aa20576a55f638383 |
| 4 | original-boundary-FD | 172 | edcbff2f95cc5f0200f510ab95923c3c2075122eb77bf486f447578791b2b3e1 |
| 5 | original-model | 151734 | dedfd53613348bac2d744de545e823d7aa1ffcab63eac4b45f317a0daf5a92db |
| 5 | original-boundary-FD | 178 | 385fc96f32151271dea43a27ca6815c398352eb687086123c6bb47cff9cfeae1 |
| 6 | original-model | 151599 | 422850ae04bc486a9c403aacbfa45d61ea9ed4ee3cf265e14fa69e14a28611dc |
| 6 | original-boundary-FD | 178 | 10ba59df321f00107ff0f880abbeeadfd93a22fa8579665b1d76bb392eacbf02 |
| 7 | original-model | 151758 | db491d8ef6ce64342ae1151c3b4a731331ec75c25fb9cd92d06a51213bd810e1 |
| 7 | original-boundary-FD | 177 | ce588fc45dd51cdd2b4c2b71666eb7c17f32c235e66bbe2e2670c62769f72552 |

这里保身份以便来源审计，不把151KB模型stdout当成已从工具读过的材料，也不以未来重跑生成相同SHA为前提。后继若要修必要选择，必须基于原source的真实必要字段语义和完整错误/未访责任，新的实际结果仍需新运行，不能恢复本次未返末场。

## 513.10 当前已付与下一责任

已付的是本次完整source生成/固定116身份、八次真实39模型与同新warm的fresh-FD原交接、原规则同步、原登记owner quiet、两个精确超限identity及真实清理边界。八次父交接由本次原bool和控制流证实，不是泛化收敛结论。

本次未付的是整份必要科学正文的工具读回，以及由那些原值才能判断的定量进展、最终三参数/完整pair、原每trial失败范围和FD具体误差。原方案本来没有调用native/fullDN，完整曲线、连续C、同g闭面、全t reach/held/反射inclusive及固定参数精化也不能由此报成已完成。

当前可行动的问题是90000字节必要读回组织仍未解决；本结果只登记真实失败与现有源作用范围，不改223、抬限、构造fixture、补跑或额外设置科学验收门。geometry不再重复下载本次日志，root可单独发表本结论；217仍由geometry独占其未来终态，R532的原同次128来源/clock工作独立继续。
