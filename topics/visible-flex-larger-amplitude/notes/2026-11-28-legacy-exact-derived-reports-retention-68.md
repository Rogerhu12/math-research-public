# 第 68 批：五份旧准确派生报告的完整来源与恢复

日期：2026-11-28；construction / GPT-6 Astra Pro（AI 辅助）。本批依据仓库 README §15，仅安排已有完整来源、参数和原输入恢复链的历史派生输出退役。根代理负责最终普通提交，本文和台账不更改 refs 或队列。

## 1. 精确范围

固定候选快照为 `2b13747323ccb6a96df5c13775edcb436fe78792`，topic tree `e8eda7764d911f7a4af22c6d5377e401fabc8e5e`。五项毛计 **394359 B**；每份原报告均小于 100000 B，已完整取回并计算字节数、SHA-256、Git blob。没有读取大 raw、gzip、NPZ、NPY 或其他二进制正文。

| 项 | 原 notes basename | 字节 | Git blob |
|---|---|---:|---|
| 1 | `2026-11-12-closure-r53-parameter-axes-r1.json` | 80777 | `b2fa371afe22106f62582918e41d9b1010e1fe9f` |
| 2 | `2026-11-12-closure-two-cell-parameter-budget-r2.json` | 86276 | `03ea82235831fd40dd6b377ed2b4f3e4b835f2a1` |
| 3 | `2026-11-12-closure-outer-source-parameter-rows-r1.json` | 90364 | `2af49d0b5c4072840adedb1569229ca57a51c9ba` |
| 4 | `2026-11-12-closure-low-spectral-wide-tail-v1.json` | 71331 | `261f0e48f023f2261514be0b386db610849a8922` |
| 5 | `2026-11-12-root-q095-complete-core-gap-r1.json` | 65611 | `c87e68c72702fc518f5850e8b710b070fcb6f9c5` |

完整输出身份、原 command/resource 对象、所有门和未付项、完整参数定义见 [参数与实际结果卷](../computations/legacy-exact-derived-reports-retention-68-complete-parameters-and-results.json)。完整 source/input/evidence/reader 恢复关系见 [来源与输入卷](../computations/legacy-exact-derived-reports-retention-68-source-input-provenance.json)。较长的逐模、逐 panel、完整有理数行以原 whole Git 对象恢复；台账中的状态摘要不是那些数组的替代输入。

## 2. R53：完整 46 轴仍是加权 l1 球的截距

原 `closure_parameter_axis_ledger.py` 完整源码 SHA-256 为 `aaa79183764e849217e33b15cf6f3a5ad401e889fcdf75a3e774f4cfbaf9e0fd`。原 192-bit 设置、四个真实输入、完整 46 个偶数模式、参数单位和真正 cut 高度转换都保留；原资源完整 12-token 命令未裁剪。原 session 84894、exit 0、wall 1.2337896823883057 s、RSS 68252 KiB 仅作为原事实。

原参数域是 $\sum_j |a_j|/u_j\le R$。所列坐标轴是这个加权 l1 球的截距，不能把每个轴最大值同时作为 product box。源码和 [R53 完整证明](../results/R53-actual-full46-head-parameter-domain.md) 均保留；原 radius、$Q$ 到物理高度的因子、legacy raw-q 的不同单位和全部原检查仍在结果卷中。原记录的 0 新径向积分、0 inverse solve 不变。

后续 `closure_balance_parameter_axes_v2.py` 确实读取 `--axes`。原 balanced-axes 完整资源继续保留；恢复该旧消费者时必须先恢复原 R53 输出的全 46 行和 whole hash。

## 3. R73：成功执行不等于全部中心落入预算

原 `closure_two_cell_parameter_budget_v2.py` 完整 SHA-256 为 `cc664a0a228ab9e7061054849ae7eb5b72c419257037df5325f620e326fd4d1e`。原 functional、recentring、moving family、far completion、18 组原 kernel 与全部 10793 panel 的输入关系保留。原 argv 没有覆盖源码的 40960 KiB 参数默认值；不为恢复新增或减少预算。

原 session 69950 / exit 0 / wall 3.9342641830444336 s / RSS 13176 KiB。原 `all_gates=true` 只覆盖其明示算术与来源责任。以下两个整体字段仍严格为 false：

- `all_original_centres_within_available_axes`；
- `all_recentred_centres_within_available_axes`。

原 mode 2 的显示比例约为 0.0000523886008873 和 0.0000560088984999，两个对应 inside 位均 true；mode 4 的原显示比例是 36.511719213860467104068503833808538，recenter 后为 3831711.9008479460289043940086248699，两个 inside 位均 false。这里只摘录原记录显示值；完整准确有理端点在原 Git 对象中，没有重算或新舍入。

原 far 项已补，不把更早 raw 端点冒充完整端点。完整外部修正及参数导数仍未付，whole outer matching/contraction 仍 false。[R73](../results/R73-two-cell-signed-source-boundary-budget.md) 保留完整解释。真实后续 `root_anisotropic_auxiliary_centre_family.py` 消费此预算，必须恢复完整 r2，不能只用这些显示比例。

## 4. R81：完整参数 source rows 的范围不升级

原 `closure_outer_source_parameter_rows.py` SHA-256 为 `93dd01f62eb9642c881640550df6253235798cb531ee439dbf29ddeaebadd10e`。完整原 20 参数 product、epsilon、sigma、全部 mean/inverse 责任、原 10793 panel、同一候选 metric/endpoints、exact Fraction 和原 outward 80-bit dyadic 算术均保留。源码默认 RSS 40960 KiB，完整原资源 argv 不变；原 exit 0、34.26776671409607 s、15688 KiB 只证明原执行。

以下原字段继续 false：true head DN derivative、unknown outer field correction、full outer Green/Schur inverse。完整 [R81](../results/R81-complete-source-parameter-rows-and-candidate-boundary-map.md) 及原 plan/manifest 都留下。

`closure_candidate_boundary_row_budget_v2.py` 真正读取 `--source-rows` 和另外三个完整输入，并记录其 whole hashes。旧消费者恢复必须恢复完整 rows/group_rows；没有把本次摘要变成其数值输入。

## 5. R96：原六份未刊中间件与完整再生路径分开说明

原 wide-tail 全报告为 71331 B / SHA-256 `0b9519dafcda5b0ae02f1191539d6054a9a0722f6207c14b96844d9520082de3`。原 `closure_outer_low_spectral_wide_tail.js`、六轮 `closure_outer_low_spectral_enclosure_v2.js`、以及原 v1 schema 失败源全部保留。

完整旧执行摘要记录：v1 Boolean/data-object guard 失败发生在完整 enclosure 前；随后原 V8 BigInt 六轮 23698 ms、26 门 true；wide-tail 32366 ms、11 门 true。没有把这些原事实改写为本批执行，也没有声称已进行 M94/M96 Arb。

原六份 split 中间数据曾创建，但**未纳入公开提交**。本批不给它们捏造 Git blob、字节数或恢复 commit，也不读取/分块传输 207334 B 的完整 spectral primary。完整来源与参数卷保留了原这项限制。

已刊的完整输入恢复器 `closure_outer_low_spectral_wide_tail_full_v2.js` 保留原 tail 算术，直接读一个完整 fresh primary，核其真实新 whole hash、六个原科学输入身份、spectral v2 源身份及全部 26 门。原完整再生命令是：

```text
node computations/closure_outer_low_spectral_enclosure_v2.js FRESH_FULL_SPECTRAL_OUTPUT.json
node computations/closure_outer_low_spectral_wide_tail_full_v2.js FRESH_WIDE_OUTPUT.json FRESH_FULL_SPECTRAL_OUTPUT.json SHA256_OF_FRESH_FULL_SPECTRAL_OUTPUT
```

新执行 metadata 会改变 fresh 文件 whole hash，不能冒原字节；准确原 wide-tail 字节另可从本批固定 Git 对象直接恢复。这个区别在原 execution-summary 和 stable-manifest 中已经明确，本批完整保留。

原 46 个 low unknowns、6 轮、230 个 source rows、57 个剩余 middle blocks、完整 mean/inverse/Neumann tail 都不减。额外 analytic width 只属于已知有限 centre，不属于未知 middle/high。actual middle Green、middle response、joint low-middle-high fixed point 和 closed surface 仍未付，[R96 完整证明](../results/R96-actual-low-spectrum-and-complete-middle-source.md) 留树。

旧 `closure_middle_r96_source_probe.py` 对原 wide-tail SHA 有真守卫，随后读取全 source rows。若运行该原旧消费者，直接恢复原 Git 文件；不能把 fresh metadata 文件改贴旧 SHA 或在旧消费者里删除守卫。

## 6. q095：全核心轴差只是有限暖场诊断

原 `root_complete_core_gap_diagnostic.py` SHA-256 为 `8cea074e933bd8f4e4bc6623d597bea19eaa60a4a0d233d81968273868d162c0`。它从原 12 份完整暖场报告读取每份 24 个 binary64 支撑系数，使用准确有理的完整轴差恒等式，并保留五个方向的有限中心差分。原 input/hash map 和 plan 全量恢复，不把一个系数代替完整核心。

原完整说明保留：基准轴差 0.18913039378072885，组合轴差 0.19112857192340826；原准确增量为 2415649148874726695583 / 1208925819614629174706176。原 finite-sample 比例约 0.048483206759296855 到 0.048897659318914724，仅属于有限前缀 origin-sphere 诊断。这个分母不是全闭面连续 $D$，轴差也未付整面遮挡、fixed-H、whole held、Euclidean separation、reach、精确等距或精化条件。

原 0 RHS / 0 Jacobian / 0 Node / 0 BVP、exit 0、wall 0.2799968719482422 s 和 RSS 11520 KiB 保持。没有借新存储工作产生额外科学结论。

## 7. 完整输入、来源与原 reader 恢复

本批直接登记 11 份完整 producer/consumer 源，并引用前批完整 source registry 中 5 份 helper/resource 源。旧 registry 的 61 份源、269 个完整输入恢复条目仍按其原边界复用，不重设审查或复跑门。

本批列出 74 个不同原 input-role 记录：68 个有精确现树或固定历史 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 的 path/blob/size；另 6 个是上述明确未公开的 R96 generated split 中间件，以完整单文件再生方案说明。原 unread binary 的 SHA 来自原小输出的完整 input_hashes，不能冒本批重新计算。

原资源中绝对 interpreter/工作目录和所有参数原字保留。未记录的环境版本仍未知。重新科学生成应产生真实的新执行/资源记录；不能承诺旧 elapsed/RSS 逐字重现。

精确历史恢复：

```text
git show 2b13747323ccb6a96df5c13775edcb436fe78792:FULL_REPOSITORY_RELATIVE_OUTPUT_PATH > DESTINATION
git cat-file blob EXACT_RECORDED_OUTPUT_BLOB > DESTINATION
git show 60321451c058c6a51da58c37ae5ec6f2d1145f74:FULL_REPOSITORY_RELATIVE_INPUT_PATH > DESTINATION
```

先按记录确认每个输入实际属于哪个固定 commit，不能把最后一条盲用于所有路径。调用旧 reader 前须恢复其完整原文件和 whole hash，所有科学代码和 hash guard 原样保留。

## 8. 交付和未做项

本批不改变 active 19–28、输入、后参或 source；不删证明、唯一不可再生输入、parent91、ports/Nelder 或前批已退项。完整源/参数/resource/结论不因容量目标裁剪。

工作只读取既有小文本、树 metadata，记录既有结论并保护完整 JSON/说明 blob；未运行科学、import、AST、compile、数值 replay、fixture 或 benchmark。根代理是唯一 refs/queue 写者，最终按 fresh path/blob/size 普通提交。完整 delivery 给出全部删除和新增字节、SHA-256 与 Git blob，净容量由最终表计算。
