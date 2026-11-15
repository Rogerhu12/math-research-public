# Request182：原160完整日志的必要128位求解与四组件读回

作者：AI（ChatGPT）。状态：按直接科学投影优先作最小必要修订，独立纯元数据源码与执行参数已冻结；尚未运行182，尚未读取原160 compute 大日志，不对160作新的科学判断。原160、176r2的已有源保持原字节；本次只创建小文本 blob，root 单独负责发布与执行。实际182结论预留 R388。

## 1. 需要恢复的原事实与范围

原160固定身份为 run `43729874541`，source `b34692d09c8d5ecdd7b859e43489da4413f1468e`，compute job `132859748674` completed/failure，report job `132921319875` completed/success。root 已读取的小 report 是15,696 B / SHA256 `69129a561c28d80404a8f6600d0c55a10725c98f87ae6c9508bf9a783f8c3488`；其中 child70、summary=null、componentflags=null 只能说明原传输范围，不能推断128位 owner 或后续四组件的数学结果。

182只在新公开 Actions 内，通过官方 jobs/logs API 对上述原 compute 日志做一次顺序读取。不下载原 report，不恢复任何已清理的 state/J/factor/sensitivity 数据，不重跑 native、root、RHS、线性求解、边界响应、endpoint 或 audit。读取的是已发生的原事件，其完成、异常、未访问索引与原最大值只能按原字段保留。

本次任务是补足原160尚未读到的结果，不是原160或其他科学请求的新增验收门。

## 2. 四件冻结文件

| 目标路径 | 字节 / SHA256 | Git blob |
|---|---|---|
| computations/root_20261115_read_actual160_native128_necessary.py | 72899 / `d9d694e20026b67e7e22bfa14f3a332820f7621db8619dc4d12d4ba5fcd448ed` | `72c46765a1410dc505368f4b955b00766597a225` |
| computations/public-actual160-native128-necessary-readback-request.json | 8755 / `16d9acae6d67e67af2839f2691a77e1fff60de830fd04754cf3dae97dfd3505b` | `15b3392d257c92770a78835162ecad4487f0bd02` |
| .github/workflows/visible-larger-public-actual160-native128-necessary-readback.yml | 8336 / `d5986eb3d58228489f7d1c78cb4727bb53b8d8918e542be63a0b9d04bf179aa5` | `e96de43243ac938a9fbf8691ac331102765d4912` |
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

旧选择器每组件最多保2MiB必要元数据；达到此上限只标记补充范围不完整，继续读取/散列原流，不阻止主要direct读回。旧协议不完整、旧选中字符串不完整或旧part身份不符均单列 optional issues，不把已有直接科学投影丢弃。全旧树的 canonical bytes/SHA **只是原producer回执**；输出明确 `full_semantic_object_reconstructed=false`、`full_semantic_object_SHA_recomputed=false`。没有以本次读取声称完整旧树或大数组重新通过审计。重复旧part索引可按原顺序跳过并计数，不声称已另证重复payload相同。

每个组件的原生命周期/状态正文只保一份。all-components只另保全局flags和原总记录身份；终态副本、compact summary、完整旧readback描述符均以身份和已保正文引用表达。原依赖未启动原因、过程退出、资源状态、所有未完成stage/step/query/column范围均保留，不能由另一个组件成功推断本组件完成。

## 6. 必要错误文本与不返回的正文

原 `qualified_same_job_original_log_part/complete` 在Actions内用 UTF8-surrogateescape 流式恢复诊断字节顺序，核各旧分段 bytes/SHA、覆盖、metadata SHA 与原文件 SHA；不保存整个旧诊断文件。空日志允许合法零分段。既有直接原 stderr 行协议核原行身份。旧流不完整或缺complete marker保其已读前缀/未付范围；不会因此将真实direct科学投影删除或重分类。

独立诊断匹配器保 first6/last6 个不同的实际匹配整行，每行最大12,000 B，共享16,000 B文本额度；其他文本仅身份和明确省略范围。**匹配次数不是实际error数。** 正则 `budget.exhaust` 可能命中 `budget_exhausted:false`；输出名已改为 `original_matching_diagnostic_line_occurrences` / `unique_matching_diagnostic_lines`，并显式声明 `matches_are_not_error_classification=true`。不能据此计数推断科学异常或预算停止。

原 actual_error/error/evaluation_error/traceback 字段不超过6,000 B时保完整文本；更大字段保整字符串身份，只选 first4/last4 匹配原行，若无匹配则 first3/last3，文本总额不超过6,000 B。不能容纳的整行不切片，保范围声明。以上选择只提供必要原文本，不声称完整复制巨大异常栈，也不从字词匹配作原因判断。

本次不向连接器输出新的旧日志分包、编码块或大对象重组协议。成功数值数组、factor、完整stage/column大正文止于原已有 descriptor/metadata 身份，未下载或逐数值复核。原错误若160从未输出，182也不能恢复；原整体字节流虽可能核SHA，未选正文仍明确未返回。

## 7. 资源、单份摘要与失败语义

元数据 scan budget1200秒，原日志上限32GiB，单物理行16MiB，一百万个独立诊断匹配行身份。原全组件树128MiB／parts上限已移除，因为不再重建全树；每组件2MiB可选补充元数据上限只停补充选择，不使direct读回失败。SIGALRM覆盖本次官方元数据与扫描；SIGTERM/SIGINT产生独立external interruption，不能被optional处理吞掉。资源停止保存已读前缀身份与已恢复范围，EOF=false，不把前缀SHA称为完整原日志SHA。

结果schema仍为：

```text
actual160-original-native128-necessary-log-readback-v1
```

唯一必要JSON在 `BEGIN_REQUEST182_ORIGINAL160_NECESSARY_SUMMARY` 和相应END之间，完整bytes/SHA含LF。无新增part、编码数据、压缩blob或扩大90KB的兜底。必要摘要若超过90KB，exit70、transport_complete/readback_complete=false，保未返回临时完整摘要身份及明确范围，不删trial/未访索引换取表面成功。

reader0表示现存原日志到EOF、直接必要协议/来源与owner试步核查通过、单份必要摘要实际返回。**它不表示原科学成功，也不表示可选旧树/诊断补充或大数组审计已完成。** optional issues与选择未付范围另外报告；直接协议错误exit2、实际元数据资源中止exit3、单份摘要超限exit70。原科学未完成可以有完整的必要元数据读回，原child70仍按原输出解释。

## 8. 工作流、规则与清理

独立 push trigger 只监听本182 request；独立concurrency不取消原科学。checkout 与 Python action 均沿176的已固定提交，Python3.12.14；只有新metadata源码在 Actions ast.parse，不导入旧science。全job35分钟，扫描step25分钟；因此不会跨原每小时/45分钟规则同步周期。起步亲读双README原字节与固定Git blob（根21bd、题bff），不冒 root 的真实 pull。

仅scan step获得只读 actions token；contents/actions权限均read。不使用 artifact、Release或新增原始数据Git提交。官方原日志从未落盘。新小结果只写独占 `RUNNER_TEMP/visible-actual160-necessary-182`。

always步骤只读取这份≤90KB summary；如果相同 bytes/SHA 的 stdout marker已存在，不重复全文。清理只在原读回step与retained读回step均success、summary的readback/transport flags都真、stdout marker与实际summary字节相等时删除该唯一目录。没有原科学子程；同步step结束即本reader已join。任何失败、未读或超限范围不被主动删除为成功，临时文件随runner销毁。

本地本次仅源码读取/文本编辑/哈希/原JSON元数据查看，未运行 Python AST、import、编译、科学函数或额外fixture。首次实际标准库编译由本工作流完成；182的真实 source/run/job/结果身份由运行后记录，本文不预填。
