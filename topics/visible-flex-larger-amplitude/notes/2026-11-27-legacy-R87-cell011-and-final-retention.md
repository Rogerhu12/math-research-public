# 第二十五次旧 raw 保留范围调整草案：R87 的 cell011 九段恢复点与完整 final primary

作者：Astra-larger-resume-e4e2a2bf-20261126，2026-11-27。

本草案只建议从当前树普通移出已登记 R87 的九份 `cell011` 生成恢复点与同一次完整计算的 final primary，共 **1,165,325 字节**。本代理没有修改仓库文件或 Git ref，没有删除对象，没有运行科学计算。由根会话完整审阅后作普通提交；实施状态以该实际提交记录为准。

完整小台账：`computations/resume-20261127-legacy-R87-cell011-and-final-retention.json`，77,153 bytes，SHA256 `b7cc62f356d1e712e57e2bfa01c1834c3f29c4d763da9c49235fb2b8dec2581f`。其中保留十个对象的原 SHA、固定 Git blob、准确字节数与恢复提交；全部十一份完整小源码、二十四项真实输入、原完整 argv、原资源记录、完整九 gate 与未付责任也全部保留。生成列、逐模矩阵和高度 chart 数组不在新台账重复存储。

这是第二十四次调整的另一组真实对象，不能通过更换 `cell010` 文本得到。上一台账已经保留完整源和输入闭包；本次分别核了每个新对象自己的完整 config、真实 `completed_groups` 前缀、末尾元数据，以及 final 的全部十八段和九项 gate。它不重新宣布 R87，也不改变当前本题的完成标准。

## 1. 十个准确对象与固定恢复点

下面九个 checkpoint 均位于 `notes/`，共同前缀为 `2026-11-12-closure-outer-physical-low46-r1-completed-cell011-`。最后一项位于同目录，其 basename 独立列出。

| 文件后缀或 basename | bytes | 原 SHA256 |
|---|---:|---|
| segment0.json | 79,651 | `6f65fce153c8c08f46a3869d9bfe717b0de693d07ee668ebeac50a133f26f8ae` |
| segment1.json | 81,693 | `8e7456e28a45497143d91ddb272a9774c6b5ed2be1d7f98d76b9c0fbbeb49844` |
| segment2.json | 79,405 | `8005a9c33f9a1717b3392f927e21f997c8183bf88fabfc84472452959839a573` |
| segment3.json | 78,888 | `bde7891e9880955f2058021844ee86b0653480571ca6b536e5d5e601c2f57ebe` |
| segment4.json | 79,168 | `4a24bf634b4898ad6f5f18f6921fb707c421da3cfcb860ee9bf8f853cff7a535` |
| segment5.json | 81,754 | `c1630c0bb5b85cfee35f5e8b357209fd47fecd44c40e06adff041f4efd72e150` |
| segment6.json | 79,435 | `1db370d2356c1dd3c156c8ec1b7d13c71ac7520a675e471276fd444e9d0d41e4` |
| segment7.json | 79,247 | `e556bfd006e19cd868e99f47421e9c960c0c4cc9d593182fb6cc6ea00167898d` |
| segment8.json | 221,903 | `e66cb9b98b7d94e2e0a92c5ec1d1c4959471dfa1e03a5902c98c1ff8e41fc0c0` |
| 2026-11-12-closure-outer-physical-low46-r1.json | 304,181 | `d1078b0bd4795f99aaa87c32efe7577f6aef52e8909b8ac1460f058d39b317f3` |

九个 checkpoint 合计 861,144 bytes；完整 final primary 304,181 bytes。共同准确恢复提交为：

`5990361e45dcc35c8f5b276c17719a65ebbe386f`。

每个对象的 `git ls-tree -l` 字节数与保留的原 stable manifest 及本次工作树文件大小逐项相等。新台账逐项写出实际 Git blob。final 的固定 blob 为 `cd715768c432066a87e36f156e3213ce9d503879`。本次没有整读大文件重算 SHA；SHA 来自已经保留的完整原稳定清单。固定对象恢复和科学重算是两件事，不能把一次新运行的同参数输出预填成这些历史 SHA。

此前第二十四次说明中“final 与 cell011 留在当前树”的范围是当时那次普通提交的事实。本次新调整明确把它们纳入固定历史恢复，不回改旧说明，也不冒称它们仍留在新当前树。

## 2. 实际有界读取及每段的准确完成范围

九个 checkpoint 均只读前 16,384 bytes、后 8,192 bytes，包括小于 100KB 的前八份也未整读。final primary 的正式核验只读前 16,384 bytes、后 16,384 bytes；此前定位其字段时另读过前 6,144 bytes 与后 12,288 bytes。没有读取中间生成数组，没有解码 `columns` 或完整 `cell_rows`，没有扫描生成模式数组以产生新副本。

每份 config 均在前缀中完整结束。九份 config、final config 及已刊第二十四次九份 cell010 config 的 canonical SHA 完全相等。实际逐项完成集合为：

| checkpoint | 精确 `completed_groups` | Taylor / root bracket / rejected |
|---|---|---|
| cell011 segment0 | `[[11,0]]` | 8 / 0 / 0 |
| cell011 segment1 | `[[11,0],[11,1]]` | 147 / 2 / 115 |
| cell011 segment2 | cell011 的段 0–2，连续无跳段 | 155 / 2 / 115 |
| cell011 segment3 | cell011 的段 0–3，连续无跳段 | 318 / 2 / 270 |
| cell011 segment4 | cell011 的段 0–4，连续无跳段 | 326 / 2 / 270 |
| cell011 segment5 | cell011 的段 0–5，连续无跳段 | 493 / 4 / 413 |
| cell011 segment6 | cell011 的段 0–6，连续无跳段 | 501 / 4 / 413 |
| cell011 segment7 | cell011 的段 0–7，连续无跳段 | 608 / 4 / 512 |
| cell011 segment8 | cell011 的全部段 0–8 | 616 / 4 / 512 |
| final | cell011 全部 0–8，再 cell010 全部 0–8，原顺序完整 | 1260 / 8 / 1052 |

台账保留每个准确 `completed_groups` 列表，未只保这个表的文字摘要。四十六个派生初始斜率、独立 m2/m4 比较块、final 的两份完整 source-identity 数值记录仅保字段名、原条数和本次已读小字段的 canonical 摘要；原完整值仍在固定原对象中。真正参数 `modes`、cells、精度、Taylor 阶、root/remainder bits、initial parts 和完整 argv 全保。两项全局余项区间是原紧凑标量，按原端点文字保留，不转换成未实际给出的小数。

final 的真实 `source_identity` 顺序为 cell11、cell10；两者的 `cap_strictly_inactive`、`valley_control_exact_zero`、`warp_weight_exact_one`、`chi_and_j0_exact_one` 均为 true。这只复述原准确身份结论，不把生成数组另存到小台账。

## 3. 完整 producer 与全部参数保持

主源码仍为 `computations/closure_outer_physical_trace_flow.py`，20,216 bytes，SHA256：

`d919902557b3c5c17e6e68602ba86f3b3852207057c3a2ea1468b08ecae4cc5e`。

原完整 plan 为 5,037 bytes、SHA `b4ffa91036380880475659d30b5b0141bd280f1bc9b496027d36b0cda77218f3`。原 resource 为 1,473 bytes、SHA `f3f0b1f9374b7f7f9d632f4e0a28f3f8a4578773fe2313dfeb8452f10973e725`。两者和原 5,514-byte stable manifest 原地保留；stable manifest 的 SHA 为 `c688c1a4412aa9ff55f8ce4d636cdca9adcb8eec65af16540dd8376e977ad6ed`。

原命令的完整 argv 与 shell 命令在台账逐项保存。为避免把“复原 cell011 九份”误读成缩减运行，原科学调用如下，外层仍由原 `strong_resource_run.py` 记录实际资源：

```text
/workspace/scratch/c0de65fac774/research-venv/bin/python
computations/closure_outer_physical_trace_flow.py
--ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json
--outer-flow notes/2026-11-12-closure-outer-taylor-m2m4-12to10-r1.json
--head-summary notes/2026-11-12-closure-real-linear-q003-low46-recovered-summary.json
--head-manifest notes/2026-11-12-closure-real-linear-q003-low46-recovered-raw-manifest.json
--true-slope notes/2026-11-12-closure-taylor-cut-m2m4-n16-r2.json
--out-prefix notes/2026-11-12-closure-outer-physical-low46-r1
--modes 2:92
--precision 256
--order 24
--remainder-bits 100
--root-bits 160
--initial-parts 8
--rss-kib 40960
```

这里保留全部 46 个偶模式、原两胞元十八段推进；`--resume` 原本不存在。不得替成只跑 cell011、只跑两个检查模式、跳过原临界片或改用有限 Robin 头。三项线程环境 `OPENBLAS_NUM_THREADS=1`、`OMP_NUM_THREADS=1`、`MKL_NUM_THREADS=1` 保持记录。

原会话 4951 的正式 exit 与独立 wait4 均为 0。原 resource 返回 wall 31.13652729988098 秒、峰值 31,020 KiB、exit 0；final 自身原计时为 31.046796472001006 秒、峰值 30,496 KiB。两种口径各保原字段，不混为同一个测量。它们是 2026-11-12 的历史实际值，本次没有重算。

原小记录没有精确的 Python/python-flint 版本字段。本次保留原可执行路径及完整源的 `flint` API 依赖，不从邻近任务填一个版本。若日后确需新科学运行，应在公开 Actions 记录真实版本并重新返回全部科学门，不能伪造原资源值或字节等号。

## 4. 完整十一小源与二十四真实输入的闭包

本次沿用并准确绑定已刊第二十四次完整闭包台账：

`computations/resume-20261126-legacy-R87-cell010-checkpoints-retention.json`，72,272 bytes，SHA `1804cd93cffde965a9fcb69d981c321d5755c31aa3a6151a087cb70d371aab78`。

新台账仍自含全部十一份源和二十四份输入的路径、SHA、bytes、恢复提交、Git blob、实际读取角色及 import 边，不只留一个旧台账链接。当前十一份小源的完整字节 SHA 与 stdlib AST 已再核，全部固定 Git blob/size 与上次相同；没有导入其中任何科学模块。

十一份完整源是：

1. `closure_outer_physical_trace_flow.py`；
2. `strong_resource_run.py`；
3. `closure_outer_taylor_shared_flow.py`；
4. `closure_projective_interval_column.py`；
5. `closure_real_head_source_enclosure.py`；
6. `closure_real_linear_head_enclosure.py`；
7. `closure_split_joint_io_v2.py`；
8. `closure_split_joint_io.py`；
9. `closure_taylor_cut_slope_v2.py`；
10. `tail_r33_middle_ordered_physical.py`；
11. `closure_real_head_green_enclosure.py`。

二十四个输入不是仅五个 CLI 文件。除 ready、outer-flow、head-summary、head-manifest、true-slope 外，原 source 真正读取 `head['output']` 指向的完整 head 主包，并按 outer-flow stem 读全部十八个 cell011/cell010 源段锚点。每个新 checkpoint 的完整 `input_hashes` 与上次二十四输入表逐项相等；final 后缀重复的完整 `input_hashes` 也与其 config 完全相等。源码 hash 表、原 entrypoint、六个冻结依赖和两层实际 I/O helper 身份均保持。

输入中两项 head 对象在固定公开提交 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` 恢复：105,167-byte summary，原 SHA `f305282d63a7e4b4a4208a0f85efe94d9b92788178c278c3bf682c9a1b816fb8`；112,548-byte gzip primary，原 SHA `cabdb3fca1d9176b1f2c46a2f7b2ff5b82ff1af426c4c942c7863c3c15c65f91`。其他二十二输入在 `5990361…` 完整绑定。新台账逐项保各自的实际 blob，不把不同恢复提交合并为一个假对象。

本次没有再整读四份大输入来计算 SHA。原 SHA 来自各完整 config；上一轮对二十小输入的完整核验和这次固定 Git 对象核验各自明确。两次验证范围不冒充一次新的全 raw 重算。

## 5. 移出 final 后仍保的完整结论及准确限制

完整证明 `results/R87-complete-low46-physical-trace-flow.md` 原文保持，9,718 bytes，SHA `d8e6a20662ededefbf4950bb4478be9dc8ff8365130215321f83e42011e57e43`。原 916-byte 执行说明 `notes/2026-11-12-closure-physical-low46-execution.md` 保持，SHA `9a1ab3df934e52ce4701b4824e1c22f4723b8fd0c4432f4e47a27bfb4bdd5f2f`。完整小 manifest、plan、resource 也都保持。

final 前缀的九个门已经逐键核为 true，并在台账保留完整命名：同准确 metric 且 caps 不活跃；全部声明真实低模保留；真实 head 线性边界而非有限 Robin；全部十八真实源段完成；physical trace0 身份和准确常行列式；共享 max-mode 导数主界；全部 critical root strips 与 Taylor 余项；独立 m2/m4 源和矩阵身份；全部真实端点 height charts。

原完整低窗结论仍是全部 46 个真内头列与独立基列的两胞元十八段流，92 个真实端点高度 chart 已付。最终 counts 为 1,260 Taylor、8 root brackets、1,052 局部门拒绝后同位置细分；没有通过移出 raw 抹去这些拒绝。

final 后缀同时真实写明：

- `complete_outer_PDE_or_full_frequency_fixed_point_claimed=false`；
- `whole_field_Green_profiles_for_new_modes_not_yet_paid=true`。

这些限制原样保留。R87 不因此成为全部频率、完整外部 BVP、当前 larger-amplitude 题目的连续 metric/嵌入/reach/20% 幅度/固定 g 精化证书。移出完整生成主包，只改变当前树的 raw 保留方式；准确原字节由固定对象恢复，完整数学正文与紧凑真实结论仍在当前树。

## 6. 当前任务边界和实际恢复方法

本次按完整小文本搜索实际 run04/run05/run06/run07 队列快照，条数分别为 17、9、12、2；三个检索词为本次 checkpoint 前缀、完整 final basename、旧 producer basename，全部为零。四个准确队列 SHA 在台账记录。该事实限于所读快照，不声称任意未来步骤或所有间接依赖都不会引用这些旧对象。

没有移出任何当前 SO3 新源码、新固定模型参数、P0 历史地址参数、正在运行 child 的数据、原证明或未知用途 JSON。根只应按台账十个确切路径普通删除，与完整 ledger/note 同一次常规提交；不重写历史。

恢复旧原字节时，使用指定固定 commit:path 或其 Git blob，并按保留的原 SHA/size 核验。需要科学再生时，在公开 Actions 独立恢复全部二十四输入与十一源码，保持完整原 argv 和参数，从原完整十八段入口运行。原 producer 拒绝覆盖已有 final、failure 和 checkpoint，因此新工作目录只恢复输入，不先摆入这些旧输出。必要路径变更须明确为输出路径变更，不能借此更换源、少跑胞或删模式。新 raw 留 runner，只公开完整小源、完整参数与实际紧凑返回。

本草案和 metadata builder 只用于原对象归档责任，不新增数值门，不触发科学运行，也不修改当前已排的独立新方向。

## 7. root 独立复核与本次实施

root 已完整读本说明及14430-byte纯metadata builder，再独立按同一有界首尾实际读取十个原对象；全部config、每个真实completed_groups、两项紧凑余项/资源、final十八段与九gate、实际限制字段均与小台账逐值相等。十一完整小源实际SHA/AST、二十四输入各自固定blob/size/原config SHA、完整原plan/证明/执行说明再次核同；没有导入科学模块、整读大raw或重新计算历史科学SHA。

本次普通提交实施台账十个确切对象的移出，原字节由各自固定5990361及输入8ef38046对象保持可恢复。全部完整小源、真实参数、证明与紧凑结论保留；新raw不转存Release或artifact。run06/07新的完整入口和未知输出责任不受此历史raw保留调整影响。
