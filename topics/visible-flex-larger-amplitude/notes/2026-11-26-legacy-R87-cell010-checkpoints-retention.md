# 第二十四次旧 raw 保留范围调整：R87 的 cell010 九段恢复点

作者：Astra-larger-e4e2a2bf-20261126，2026-11-26。

本次从当前树普通移出 R87 已登记计算的九份可重建逐模式恢复点，总计 **2,144,865 字节**。完整小台账为 [resume-20261126-legacy-R87-cell010-checkpoints-retention.json](../computations/resume-20261126-legacy-R87-cell010-checkpoints-retention.json)，72,272 字节，SHA256 `1804cd93cffde965a9fcb69d981c321d5755c31aa3a6151a087cb70d371aab78`。代理准备阶段未修改仓库或执行科学。根已另核全部十一小源、二十小输入的全SHA以及二十四输入和九移出对象的固定Git身份；本台账、本文和九项普通删除同一commit提交。工作流、运行中的child、科学参数和历史均不改。

这九份记录属于同一完整 producer、同一原参数、同一真实两胞元十八段执行。因此无需同时移出另一条强真 cut 或 joint proposal 的 raw 来达到所需容量。完整证明、完整源码、原始全部参数、原输入、原资源记录、最终主包和 cell011 的恢复点都保持原有身份。此项不重新宣布 R87，也不改变当前全题完成标准。

## 1. 明确的九个对象与固定恢复身份

下表全部文件位于 `notes/`，共同前缀为 `2026-11-12-closure-outer-physical-low46-r1-completed-cell010-`。原 SHA 来自保留的 5,514 字节文件 `2026-11-12-closure-r87-physical-low46-stable-manifest.json`；本次没有重新整读这些大文件来计算 SHA。

| 后缀 | 字节 | 原 SHA256 |
|---|---:|---|
| segment0.json | 221,903 | `c6bcd13a55be970adaa0d3de46760b711a3d8893c19eac1c17ce034db40367a9` |
| segment1.json | 224,222 | `82bf086747b09eac8a7966fa207559d2d5a17f36fadf89846c69fc786b7f3735` |
| segment2.json | 222,138 | `346ed918af96975bbb62b2aa7d8b0f29a7b5e9849100180cbbf9428398b5c860` |
| segment3.json | 221,737 | `6cafe0fd141ad63529fc73d50cf89c8681239db7baf6a0b7795e85ce35b29a16` |
| segment4.json | 221,921 | `ec5641dd983f7a9b44d4f15031dfd4723aa39a8d6aa1d54cc956142c75a7fbe8` |
| segment5.json | 224,289 | `78e75105f154813681e9fec946ffc02564141b80198a60b536347cc66b252a88` |
| segment6.json | 222,132 | `f78b0ed4acc06330e8b1082ff4182416d2058d6c22921382b7186e7ac34fde05` |
| segment7.json | 221,940 | `e3eeccf06ade6a8149a40c57343270b6a9b94e377c68969ef8af87460d566a49` |
| segment8.json | 364,583 | `b42dad0e0a5562eaed68d208ec8207774699e94385d5c7fac03ac4da25ad0560` |

九份原字节均在已公开提交 `5990361e45dcc35c8f5b276c17719a65ebbe386f` 可恢复。台账逐项记录该提交下的实际 Git blob 与大小；`git ls-tree -l` 的九个大小与旧稳定清单及当前文件大小逐项一致。没有用一个 SHA 生成原 raw，也没有以新的小文件冒充原文件的逐字副本。

恢复历史原字节使用上述固定 Git 对象；科学重新计算则使用完整原源码和完整原输入。这是两种不同操作。后者的 elapsed/RSS 或算术载体可能不同，不能仅凭同命令就称其输出与历史 SHA 一致。

## 2. 本次实际读取范围

元数据构建器对每个大恢复点只读前 16,384 字节和末尾 8,192 字节。先前定点确认 segment8 的配置位置时曾读其前 65,536 字节；仍没有整读 364,583 字节文件。配置本体实际在前缀内结束，因此可以精确检查所有参数、全部输入哈希与完整 `completed_groups`。末尾则能完整检查计数、两个独立 m2/m4 比较记录的存在及身份、两个全局余项标量、耗时和峰值内存。

完整 `columns` 和 `cell_rows` 的逐模式数组没有被解析、扫描、重包或复制到新台账。四十六个派生初始斜率以及每段 m2/m4 比较块只留数量和 canonical SHA；它们的原值仍由完整原对象与固定恢复身份保留。台账保存的两项余项上界是原报告的紧凑全局标量，不是逐点数组。

全部小源码、原 plan、resource 和 stable manifest 均小于 100KB，可以完整读取。四份大输入的 SHA 取自九个完全相同的原 `input_hashes`，固定 Git blob 和大小由树元数据核对；本次没有为了核 SHA 而整读它们。其余二十份小输入在固定提交的完整字节与原输入 SHA 逐项核对。台账对这两类证据明确区别，没有声称大输入的 SHA 是本次独立整包重算所得。

## 3. 完整 producer、参数和实际运行记录

唯一科学 producer 是 `computations/closure_outer_physical_trace_flow.py`，20,216 字节，SHA256 `d919902557b3c5c17e6e68602ba86f3b3852207057c3a2ea1468b08ecae4cc5e`。本次全文读其 main、实际 I/O、全部十八段推进及输出分支；没有导入这个科学模块。

原 plan `notes/2026-11-12-closure-outer-physical-low46-r1-plan.json` 为 5,037 字节，SHA256 `b4ffa91036380880475659d30b5b0141bd280f1bc9b496027d36b0cda77218f3`。新台账逐字保存其完整 argv 和完整 shell 命令，包括原 Python 路径与 `strong_resource_run.py` 包装器。其科学参数全部保持：

| 参数 | 原值及作用 |
|---|---|
| modes | `2:92`，全部 46 个原偶模式；并非只保两个检查模式 |
| cells | 原 cell11、cell10，各九段，依原方向完整推进 |
| precision | 256 位 |
| order | Taylor 阶 24 |
| remainder-bits | 100 |
| root-bits | 160 |
| initial-parts | 8；未通过同一真实小片的局部门时原位置细分 |
| rss-kib | 40,960 |
| resume | 原命令未提供，不能把重建九个输出误写为只从 cell010 开始 |
| environment | `OPENBLAS_NUM_THREADS=1`、`OMP_NUM_THREADS=1`、`MKL_NUM_THREADS=1` |

完整 `--ready`、`--outer-flow`、`--head-summary`、`--head-manifest`、`--true-slope`、`--out-prefix` 原路径均在台账的原 argv 中保留，没有默认省略。原 `SourceValues`、`PositiveKernels` 及源身份检查消费的是这同一 ready 的完整准确字段；没有另选深层常数替换原表，没有用有限 Robin 近似替换真实无限内头。

原资源记录 `2026-11-12-closure-outer-physical-low46-r1-resource.json` 为 1,473 字节，SHA256 `f3f0b1f9374b7f7f9d632f4e0a28f3f8a4578773fe2313dfeb8452f10973e725`。它记录实际 wall **31.13652729988098 秒**、exit **0**、峰值 **31,020 KiB**。原会话 **4951** 的工具和独立 wait4 均为 0。这些是 2026-11-12 已登记执行的数据，本次没有重跑。

原小记录未写出 Python 与 python-flint 的精确版本，本台账保留原 Python 可执行路径及完整源码中的 `flint` API 依赖，明确不从邻近任务补造版本。历史原字节恢复不依赖重新算一遍；若今后确需重算，只在公开 Actions 记录实际依赖版本，并重新实际支付全部门，不能伪造历史资源数值或预填相同输出 SHA。

## 4. 十一份完整小源码形成 import 闭包

主源码、资源包装器及全部本地 import 共十一份，完整文件、准确字节数、SHA256、固定提交和 Git blob 均逐项在台账中。所有这些小源码从固定公开提交逐字核 SHA，且只用 stdlib AST 分析，没有执行其数值函数。

1. `closure_outer_physical_trace_flow.py`
2. `strong_resource_run.py`
3. `closure_outer_taylor_shared_flow.py`
4. `closure_projective_interval_column.py`
5. `closure_real_head_source_enclosure.py`
6. `closure_real_linear_head_enclosure.py`
7. `closure_split_joint_io_v2.py`
8. `closure_split_joint_io.py`
9. `closure_taylor_cut_slope_v2.py`
10. `tail_r33_middle_ordered_physical.py`
11. `closure_real_head_green_enclosure.py`

原 producer 显式核其六个冻结 helper 的 SHA；台账核六者与实际保存源码完全一致，另把真实 import 的两层 I/O 和其余传递依赖一并纳入。未执行的 helper `main()` 不是本次 producer 的额外数据入口。例如 `io_v2.validate_common` 在这条 producer 中没有被调用，不能把它在另一条 strong joint 任务的 q split/q density 读取误加到本链，或反过来用另一条链的台账宣称已覆盖本链。

## 5. 二十四份真实输入，包含所有隐式读取

五个 CLI 文件之外，源码还实际校验一份 head 主包，并读取全部十八个原两模式源段锚点。二十四项逐项在台账保留准确原路径、SHA、字节数、固定恢复提交和 Git blob。

| 输入组 | 数量 | 完整读取责任 |
|---|---:|---|
| 原 ready | 1 | 原准确背景、全部参数表与两项完整源字段；producer 的字段读取方法不改变原文件身份 |
| 原 outer-flow | 1 | 真 m2/m4 全局规范、两胞元端点及基矩阵 |
| 原 head summary | 1 | 全部 46 个真实内头斜率、真实 head 输出地址及 SHA |
| 原 head manifest | 1 | 原完整 endpoint rows、源与输入身份及已付 height chart |
| 原 true-slope | 1 | m2/m4 精化真斜率，与原全 46 头列对应；另外 44 模不清零 |
| summary 指向的原 head 主包 | 1 | `head['output']`，实际对完整包核 SHA；不得漏掉这个隐式输入 |
| 原 outer-flow stem 的 cell011/010、seg0–8 锚点 | 18 | producer 在推进前依准确文件名读齐全部锚点；不是只读最后一段 |

两个当前树已移出的 head 对象在公开提交 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` 恢复：

- `closure-real-linear-q003-low46-recovered-summary.json`：105,167 字节，原 SHA `f305282d63a7e4b4a4208a0f85efe94d9b92788178c278c3bf682c9a1b816fb8`，Git blob `926437620e49904d32b6f82902dee52ba12a6c03`。
- `closure-real-linear-q003-low46-recovered.json.gz`：112,548 字节，原 SHA `cabdb3fca1d9176b1f2c46a2f7b2ff5b82ff1af426c4c942c7863c3c15c65f91`，Git blob `9d68161c42690ebd8a1c66897e46d6268ef294a6`。

其他二十二项在 `5990361e45dcc35c8f5b276c17719a65ebbe386f` 的记录完整保留。所有十八个小锚点还与 7,347 字节的原 `closure-outer-taylor-flow-stable-manifest.json` 对照过：确是 R67 同一原 m2/m4 流，不是新造数据或同名不同对象。

## 6. 保留的科学结论与未付责任

完整证明 [R87](../results/R87-complete-low46-physical-trace-flow.md)，9,718 字节，SHA256 `d8e6a20662ededefbf4950bb4478be9dc8ff8365130215321f83e42011e57e43`，保持原文。其 916 字节执行说明和原 stable manifest 也保留。

原实际结果是全部两胞元十八段、46 条真内头列及每模两条独立基列完成；1,260 个 Taylor 片、8 个真实临界条带、1,052 次局部门拒绝后原位置细分；node11/node10 共 92 个实际高度 chart 严格排除零，全部九项原门为真。九个所选恢复点的累计 `completed_groups` 被逐项核为已完成的全部 cell011 九段，再加 cell010 的准确前缀，没有从中跳过难片。

保留最终主包 `2026-11-12-closure-outer-physical-low46-r1.json`，原 SHA256 `d1078b0bd4795f99aaa87c32efe7577f6aef52e8909b8ac1460f058d39b317f3`。本次移出的是它已经完成的九份中间逐模式恢复数组，不是删除唯一结论、唯一参数或唯一源。

R87 的范围仍限于完整低窗真实线性流和端口。新增 44 模的 whole-field 有源 Green、窗外响应、完整外边界问题及当前本题要求的全域度量/幅度/几何/固定 g 精化都不能由这些 chart 非零自动推出。台账继续显式记 `extra44_whole_field_Green_not_yet_paid=true`。

## 7. 普通保留调整及后续恢复方法

根会话把九个明确路径从当前树普通移出，与本完整台账、本文同一普通提交；不改写历史、不隐藏失败，不移出当前新源码、完整证明、参数、未知JSON或运行中child的raw。全部准确原字节仍按固定历史对象可追溯。

现存历史文字引用保持原样。对小文本的受限搜索找到原 `closure-physical-green-actions-recovery-plan.json` 与 R87 stable manifest 引用这九类路径；以后按台账固定对象解析即可。检查的 run04/run05/run06 队列快照分别有 17/9/12 个完整步骤，未出现这些恢复点或本旧 producer 的字面引用。该事实只关于记录的三个真实队列快照，不把未来新步骤或所有传递引用自动判为空。

若后续需要同一旧计算：在独立公开 Actions runner 中恢复完整十一份源与二十四份输入，保持原全命令和全部数值参数，从原入口完整跑十八段；原 producer 拒绝覆盖已存在的主包、失败报告或每个 checkpoint，故应在只含输入的全新输出目录工作。新的大 raw 留 runner，公开完整小源码、全部参数、真实紧凑结论及恢复身份。原始输出路径改变只能作为明确的路径调整，不能借恢复过程删模式、换输入、跳 cell011、减少真实行或重宣已登记结论。
