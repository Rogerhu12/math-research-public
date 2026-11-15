# Request182：原160完整日志的必要128位求解与四组件读回

作者：AI（ChatGPT）。状态：182首次实际必要摘要92966B、r2实际90136B均仅因90KB传输限制退出70；两次原160完整流、内部reader0与protocol0已经root唯一读回，科学正文尚未回传。本稿为第三版纯元数据修订，只将reader自己19个恒定顶层范围说明归并到同一已SHA绑定的request；所有原科学/错误文字、owner试点、四组件、键集与未访字段保持。本地没有重取日志、执行Python/AST/import或科学，root单独发布及读终态；r2事实编号R393归root。

## 1. 需要恢复的原事实与范围

原160固定身份为 run `43729874541`，source `b34692d09c8d5ecdd7b859e43489da4413f1468e`，compute job `132859748674` completed/failure，report job `132921319875` completed/success。root 已读取的小 report 是15,696 B / SHA256 `69129a561c28d80404a8f6600d0c55a10725c98f87ae6c9508bf9a783f8c3488`；其中 child70、summary=null、componentflags=null 只能说明原传输范围，不能推断128位 owner 或后续四组件的数学结果。

182只在新公开 Actions 内，通过官方 jobs/logs API 对上述原 compute 日志做一次顺序读取。不下载原 report，不恢复任何已清理的 state/J/factor/sensitivity 数据，不重跑 native、root、RHS、线性求解、边界响应、endpoint 或 audit。读取的是已发生的原事件，其完成、异常、未访问索引与原最大值只能按原字段保留。

本次任务是补足原160尚未读到的结果，不是原160或其他科学请求的新增验收门。

## 2. 四件冻结文件

| 目标路径 | 字节 / SHA256 | Git blob |
|---|---|---|
| computations/root_20261115_read_actual160_native128_necessary.py | 77510 / `1536a01102f2c6620adbb43c0b8e1708bd57e194961079f0aa3016a152629c28` | `546459ea55109dc51366e955cebc5d0273964b91` |
| computations/public-actual160-native128-necessary-readback-request.json | 12054 / `378d9707f46e03d2247eff9294fd3a9b0ae25abd1ea2389c12ba73719fc1fc0c` | `a30871cc96c30da337c43c0d8987ecee72ff3ff7` |
| .github/workflows/visible-larger-public-actual160-native128-necessary-readback.yml | 8336 / `d6bf649a6e46bdaed4c07a18f7dfaec18fe2f89756ab1b8b6d7ada88ebf46ca6` | `f6f15b5f856c5f28bacb2e047949539782c8bab6` |
| notes/2026-11-15-request182-original160-native128-necessary-readback-interface.md | 本完整接口 | 交付回执给出 |

前序纯日志读回实现为 request176r2，发布 source `48e55d2e0f6f07405c216b5417ef97844654124e`。本次复用其官方 API／HTTPS redirect／只在环境中传递 token／原数值 JSON token 按字面保存的路径，改为真实160 owner 与四组件协议；不是将165结果改标签。

新入口仅标准库：

```text
python -u root_20261115_read_actual160_native128_necessary.py
  --request public-actual160-native128-necessary-readback-request.json
  --code-directory <checkout>/topics/visible-flex-larger-amplitude/computations
  --out <RUNNER_TEMP>/visible-actual160-necessary-182
```

## 3. 来源闭合与官方传输

入口固定 repository/run/job/source；先调用官方 run 和 job metadata，要求原 run 已完成、head 等于上述 source、原 job 属于该 run 且结论为 failure。这里 failure 是原工作流事实，不是本读回器新作的数学分类。随后只调用一次原 job logs 端点；若官方返回 HTTPS signed redirect，新请求不携带 bearer token，signed URL 不输出。

新 request 明列八个原小文本，全部从原160 source 亲读并核 SHA。工作流稀疏恢复新 source/request 加这八件；Actions 预检与入口分别核其 bytes/SHA，原七个程序又与原160 request 的 source map 逐项相等。它们只被读作来源证据，不被导入或编译：

| 原文本 | 字节 / SHA256 |
|---|---|
| `geometry_20261115_native_operator_qualified_v2_final128_same_job.py` | 41364 / `024a3c67ada93c908d86c68c4ba0326270d81d314a9c154439f5fc42266b8d2d` |
| `geometry_20261115_native_persistent128.py` | 43371 / `767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322` |
| `geometry_20261115_native_persistent128_probe.py` | 17879 / `2683e8e13a8d73d6c08500e9d3716d5bac5dc2e66648a17c8e1d75d246c62107` |
| `geometry_20261115_native128_qualified_json_components_v2.py` | 17484 / `5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf` |
| `geometry_20261115_native_operator_final128.py` | 21548 / `a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef` |
| `geometry_20261115_native_persistent128.cpp` | 22364 / `7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd` |
| `geometry_20261115_native_trace122_probe.py` | 26740 / `05ad668da4bec72cedb0fa2f14d4c59a7ab99a280c47b137c94a5fafcf99105f` |
| `public-native-operator-qualified-v2-final128-request.json` | 37592 / `cfa6fe343d227a98a3a755263ea7302ad7f3437f71adc82effd5a639d88ee697` |

每个官方日志原字节在解析前加入完整 SHA256；统计真实 bytes、物理行数、是否到达 EOF，以及若有 Content-Length 的全字节相等。只在解析视图中去掉每个物理行开头的一个 UTF8 BOM、时间戳和已有 `NATIVE_PERSISTENT128 ` marker。原 SHA 不去 BOM、不改 LF；原 watcher 的 `marker/record` 嵌套对象同样识别。Actions 的青色命令回显不被当作已执行错误文本。

JSON 数值使用原 token 保存。这里仅计算文件身份、JSON索引/计数与相等关系，不把原科学数值转成新浮点结果，不重新求 residual/norm/J/区间/域不等式。

## 4. 原 owner 与完整试步

原 source 已确认，C++ owner 的每条 parsed record 在 consumer 前由 `persistent128_raw_owner_record` 发出，随后具体 event 可能再次包裹同一 record。182按完整原 parsed-record canonical bytes 去重复；相同事件/iteration/trial 出现不同内容会成为明确协议错误，不静默覆盖。

必要摘要保存 initial、每个 need_direction、direction_lifted、iteration_closed、owner_final、独立 fresh replay 的原记录及身份；全部实际 trial 的 iteration/trial/directory、alpha、base_norm、accepted/reason、128位改变字数、64位 cast 不变计数、时间，以及其他实际存在的原试步字段。每次评价中的 complete/budget、stage/row计数、原 norm/tolerance/mean、evaluation_error、worst_row、failed_stages 和 root_statistics 全部按原字段进入评价表；没有重新计算任何科学量。

相同的完整原评价对象在逐字段/原数值token完全相等后才共享一行，试步、current、final 以该行索引引用。不同评价不会因为 norm 相等被合并。原 trial 与原 evaluation 分别保一张去重复键集合表，每一实际行另有对应键集索引；因此并集列中缺键的占位与原显式 null 可由该原键集合严格区分。trial 的原 event 键也在原键集合中保留，其固定事件类型由 owner 记录归属声明，不补造不存在的字段。原 failed_stages 中只有相同的原非地址字段共享正文，每个实际 list index 与 stage 仍显式保留；原错误文字超过限定大小时按第6节声明范围。每条原 owner event 的完整 parsed-object bytes/SHA 和原日志物理行身份另外保留。

owner_final 的 requested/attempted/unvisited direction/trial 列表、stop_reason、accepted_steps 与全部原责任 flags 保留在唯一正文。terminal 转发副本中已与该原对象逐字段确认相同的内容改为身份及字段引用，避免再复制同一大段。原 R273 QR计数、formed-model 原读回与方向身份保留；不把 frozen64 chord 称为 current128 导数。

所有实际 trial 行按统一列名输出，无抽样、不截行。若 owner_final 存在，逐原地址核 trial_evaluations 与 attempted_trial_addresses；若原 final 未输出，明确不能由已有 trial 推造最终未访范围。成功 matched-trace/column 的大正文只保原身份，实际失败记录按必要字段保留。

## 5. 原四组件：直接科学投影优先，旧树仅补缺

四组件固定为 `stages / boundary / endpoint / audit`。本修订首先读取真正已发出的 `precleanup_component_start`、`precleanup_component_return.actual_record` 和 `precleanup_all_components_return.actual_record`；后者核原 runtime024a、component5e68、owner767a 来源。逐组件返回与最终总记录若都存在，要求完整 parsed-object 相等。

**每个组件的主要科学正文就是原 `actual_record.scientific_report`。** 原160已经从它剥去成功 `stages/column_records` 大集合，并保留所有原全局 completion/error/resource/budget/statistics/maxima 及 `unfinished_stage_columns/unfinished_stages`。本读回不要求先重建旧576阶段/224列大树，也不把旧全树128MiB上限变成新的必要读回门。

原投影的未完成阶段表仅作无损元数据共享：相同原非地址字段共享一次，各实际投影行号、stage/input_node/output_node（若原列中存在）仍全部列出；不同原字段不合并，不从计数推导地址。原根统计、实际尺度残差、边界112响应、mixed338×112 endpoint 与 audit 的原字段均来自对应投影，缺失字段不填0或猜成false。

旧 `qualified_same_job_scalar_tree_part/complete` 按流检查原part字节/SHA、index与metadata SHA，并只选择必要小字段，尤其原直接投影未包含的 `atomic_advances_completed` 或原地址。成功列和原数值数组不存入任何完整树。若存在匹配的 direct report，只将其中确实没有的字段添加为按原key集合分组的小表；若 direct report 确实不存在，旧选择器仅返回所观察到的原字段并明确其部分范围。

旧选择器每组件最多保2MiB必要元数据；达到此上限只标记补充范围不完整，继续读取/散列原流，不阻止主要direct读回。旧协议不完整、旧选中字符串不完整或旧part身份不符均单列 optional issues，不把已有直接科学投影丢弃。全旧树的 canonical bytes/SHA **只是原producer回执**；r2在唯一 `necessary_metadata_representation` 中明确 `optional_tree_reconstructed=false`、`optional_tree_SHA_recomputed=false`，并声明其全树canonical身份仅为原producer回执；每个可选树回执仍保实际part核验、选择完整性、issues与位置。没有以本次读取声称完整旧树或大数组重新通过审计。重复旧part索引可按原顺序跳过并计数，不声称已另证重复payload相同。

每个组件的原生命周期/状态正文只保一份。all-components只另保全局flags和原总记录身份；终态副本、compact summary、完整旧readback描述符均以身份和已保正文引用表达。原依赖未启动原因、过程退出、资源状态、所有未完成stage/step/query/column范围均保留，不能由另一个组件成功推断本组件完成。

## 6. 必要错误文本与不返回的正文

原 `qualified_same_job_original_log_part/complete` 在Actions内用 UTF8-surrogateescape 流式恢复诊断字节顺序，核各旧分段 bytes/SHA、覆盖、metadata SHA 与原文件 SHA；不保存整个旧诊断文件。空日志允许合法零分段。既有直接原 stderr 行协议核原行身份。旧流不完整或缺complete marker保其已读前缀/未付范围；不会因此将真实direct科学投影删除或重分类。

独立诊断匹配器保 first6/last6 个不同的实际匹配整行，每行最大12,000 B，共享16,000 B文本额度；其他文本仅身份和明确省略范围。**匹配次数不是实际error数。** 正则 `budget.exhaust` 可能命中 `budget_exhausted:false`；输出名已改为 `original_matching_diagnostic_line_occurrences` / `unique_matching_diagnostic_lines`，并显式声明 `matches_are_not_error_classification=true`。不能据此计数推断科学异常或预算停止。

原 actual_error/error/evaluation_error/traceback 字段不超过6,000 B时保完整文本；更大字段保整字符串身份，只选 first4/last4 匹配原行，若无匹配则 first3/last3，文本总额不超过6,000 B。不能容纳的整行不切片，保范围声明。以上选择只提供必要原文本，不声称完整复制巨大异常栈，也不从字词匹配作原因判断。

本次不向连接器输出新的旧日志分包、编码块或大对象重组协议。成功数值数组、factor、完整stage/column大正文止于原已有 descriptor/metadata 身份，未下载或逐数值复核。原错误若160从未输出，182也不能恢复；原整体字节流虽可能核SHA，未选正文仍明确未返回。

## 7. 资源、单份摘要与失败语义

元数据 scan budget1200秒，原日志上限32GiB，单物理行16MiB，一百万个独立诊断匹配行身份。原全组件树128MiB／parts上限已移除，因为不再重建全树；每组件2MiB可选补充元数据上限只停补充选择，不使direct读回失败。SIGALRM覆盖本次官方元数据与扫描；SIGTERM/SIGINT产生独立external interruption，不能被optional处理吞掉。资源停止保存已读前缀身份与已恢复范围，EOF=false，不把前缀SHA称为完整原日志SHA。

r2结果schema明确更新为：

```text
actual160-original-native128-necessary-log-readback-v2
```

唯一必要JSON在 `BEGIN_REQUEST182_ORIGINAL160_NECESSARY_SUMMARY` 和相应END之间，完整bytes/SHA含LF。无新增part、编码数据、压缩blob或扩大90KB的兜底。必要摘要若超过90KB，exit70、transport_complete/readback_complete=false，保未返回临时完整摘要身份及明确范围，不删trial/未访索引换取表面成功。

reader0表示现存原日志到EOF、直接必要协议/来源与owner试步核查通过、单份必要摘要实际返回。**它不表示原科学成功，也不表示可选旧树/诊断补充或大数组审计已完成。** optional issues与选择未付范围另外报告；直接协议错误exit2、实际元数据资源中止exit3、单份摘要超限exit70。原科学未完成可以有完整的必要元数据读回，原child70仍按原输出解释。

## 8. 工作流、规则与清理

独立 push trigger 只监听本182 request；独立concurrency不取消原科学。checkout 与 Python action 均沿176的已固定提交，Python3.12.14；只有新metadata源码在 Actions ast.parse，不导入旧science。全job35分钟，扫描step25分钟；因此不会跨原每小时/45分钟规则同步周期。起步亲读双README原字节与固定Git blob（根21bd、题bff），不冒 root 的真实 pull。

仅scan step获得只读 actions token；contents/actions权限均read。不使用 artifact、Release或新增原始数据Git提交。官方原日志从未落盘。新小结果只写独占 `RUNNER_TEMP/visible-actual160-necessary-182`。

always步骤只读取这份≤90KB summary；如果相同 bytes/SHA 的 stdout marker已存在，不重复全文。清理只在原读回step与retained读回step均success、summary的readback/transport flags都真、stdout marker与实际summary字节相等时删除该唯一目录。没有原科学子程；同步step结束即本reader已join。任何失败、未读或超限范围不被主动删除为成功，临时文件随runner销毁。

本地本次仅源码读取/文本编辑/哈希/原JSON元数据查看，未运行 Python AST、import、编译、科学函数或额外fixture。r2标准库编译仍只在公开Actions执行；本接口没有运行新增Python定义，也没有假称r2实际输出已缩到90KB。原首次182实际身份和这次表示修订见下一节。

## 9. 首次182的真实体积失败与r2最小表示修订

Root已完整读首次182官方结果；本agent没有重复取得其日志。真实run43754644599，sourceee516d474479dbd07be374175dd36fb7bae53224，job132935956609。源码、AST与规则检查通过；原160日志3,234,095B / SHA27c888838abc2cabbe0dd14886ffdcffa76e4d35f21048b30367799d04363149 /3513物理行完整读到EOF，protocol_errors=[]、reader_exit0、resource_partial=false。尚未回传的必要摘要92966B /52a6a266610adf189f24edbc8d0bebe443691e91a5b2a379ca2e44ff244bc3f4超过90000；它触发传输exit70，而非原科学重算或元数据扫描失败。

原临时result92727B /6218d259613960e29f047b6433ddf6a7c459e65b1d494405e98ee6bed5f0be80。实际只回传3277B /a8b480198d60d011d69b61d5c2335e43a40736c81220c6ce74abf4a00e48ed60（含LF）的失败摘要；因此本稿不能填原160的科学状态、试步值或四组件结论。r2 request追加这份真实retry身份，原160 tuple不变。

本次只做四项表示变化。

1. 八个原源的完整file/bytes/SHA仍在本次request的original_text_sources，入口逐件读核不变。摘要中该字段改为指向**实际request原字节SHA及JSON pointer /original_text_sources**的引用，并保该原manifest完整canonical bytes/SHA和count8。正文不再重复已绑定的小文本清单。
2. 每个本读者新生成original_receipt里反复相同的UTF8/不含LF约定只在摘要唯一necessary_metadata_representation说明。每个身份原有canonical_bytes和canonical_sha256仍保留。数值token、实际key集合、null和原科学字段没有变化。
3. 可选旧树回执四项固定说明——全树没有重建、全树SHA没有重算、全树canonical仅producer回执、可选范围不是门——同样移到唯一说明。每组件实际核验、选择不完整、part范围、重复计数、issues和错误仍各自保留。
4. 只对**已经选入必要摘要**的完全相同字典共享正文。字典的完整原投影canonical bytes（包括原数值token、键集合与null）先精确相等，且单份至少256B、真实引用比正文小，才以same_necessary_metadata_at的普通JSON pointer及完整canonical身份引用该份JSON内已经保留的正文。第一次访问先保父正文再处理子对象，所以引用目标及其祖先不会被随后替换掉。所有列表、trial/evaluation行及presence键集合表保留；它不是从完整旧树重新编码或分割raw的传输协议。

字典共享保值的范围是本读者的必要投影，而非声称恢复完整旧大科学对象。引用的身份对应共享前那一份完整必要字典；如该正文子对象也引用同一JSON中已保留的元数据，按其明确pointer解释。没有压缩或base64文本、没有新part、没有另文件索引分包；返回仍是唯一不超过90000B的JSON。初始来源、四组件与错误、全部未访地址仍由前述原字段支付，不能靠字典相等新增科学结论。

r2在90000B检查之前另输出一个小计数事件request182_necessary_section_bytes_before_transport_check：完整必要摘要bytes及每个顶层section的bytes。这里只计UTF8/ASCII JSON字节，不输出原科学正文、不重算数值。实际体积若仍过限，原exit70和完整未返回身份保持；不扩大上限或裁trial/未访数据。是否实际足够由新run决定，当前源码修订不预承诺。

工作流只同步新source长度/SHA和request SHA，其运行预算、官方一次原日志stream、只读token、源/规则核验、读回和条件清理逻辑原样。request自身真实变更负责触发重试；原源码历史保留，原160数学与接受门均未更动。

## 10. r2实际仅超136B，第三版只归并固定顶层说明

r2真实run43756253033 /source3b9877749db9212f937cd79cb464554887004078 /job132940880237已由root唯一读取。原160全流仍为3234095B /27c888838abc2cabbe0dd14886ffdcffa76e4d35f21048b30367799d04363149 /3513行；内部reader0、protocol_error_count0、error=null、resource_partial=false。必要摘要90136B超90000，因而传输退出70，readback/transport/summary flags均false，cleanup skipped。实际主section字节数是components37914、QR events14492、terminals13195、owner10114、diagnostics6521；这些原科学正文全部保留不改。未回传的科学内容不以这些大小或内部成功推测。

第三版只在compact_necessary_metadata的**最外层**处理19个由本reader自身赋值的固定范围/政策说明。只有实际值与源码声明常数的类型和值完全相同才移除重复自述；任何不相同的实际值仍留原处。新唯一reader_scope_contract保实际request SHA及/necessary_scope、/parsing、/retention、/readback_complete_scope四个JSON pointer。完整约定仍在该不可混同的request原字节中，不把原owner、components、terminal、QR、诊断或错误对象的任何字段删除。

这些19个恒定字段连同JSON分隔符合计1066B；新增引用200B，已声明常数均存在时确定净减866B。这只是小文本元数据字节计数，不是运行原科学或预填新的实际摘要身份；新run的时间、source及metadata仍以真实返回为准。单份90000B、全部科学scope、全部trial/evaluation行/presence、必要失败/未访地址、旧数值token、错误原文和字典相等引用的规则一字不改。section-bytes仍在size检查前打印；若实际仍超限，原70和未返回范围保持，不增加预算、不分包、不编码raw。

source只增加这个最外层固定说明归并；request追加第二次真实工程失败及本次修订来源，workflow只传播相应source/request SHA与源码字节数。源绑定/AST/官方API/一次stream/conditional cleanup原样。本稿不替代R388或R393实际结论，也不在未回传前给出原160数学结果。
