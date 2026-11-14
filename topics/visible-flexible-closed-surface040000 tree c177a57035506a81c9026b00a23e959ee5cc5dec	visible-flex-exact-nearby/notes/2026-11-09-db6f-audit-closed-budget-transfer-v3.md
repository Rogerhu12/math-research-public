# 闭图账本的成对转包接口 v3

作者：`/root/independent_geometry`，2026-11-09。**状态：接口实现、静态数学保持、真实参数预检已完成；独立审查通过。正式新图转包及新图几何账本尚未执行。**

## 1. 文件与保持的数学

新文件 `scripts/db6f-audit-closed-budget-transfer-v3.py`，SHA256 `5ef8d229e0a19bc83381a2cdcaef8b24309e00a1fdc6b9409b20d7ca34092e49`，另存自已审 `db6f-root-closed-budget-v2.py`（`0d68b718a43a69b24a865b1932e2700a47190724a3be4ea3f1202b56d1a59641`）。旧文件保持原字节。

这次不改变支撑、球包络、位移、帽、体积矩或 metric 目标转移不等式。从原正归一化检查到函数末尾，删除新报告唯一增加的 `base_closed_budget_script_sha256` 字段后，全部原代码与报告字段逐字相同。五个原有数值辅助函数也保持相同 AST。特别地，源目标的前缀误差仍只经过一次精确桥转移；没有把已经转移的字段再转移，也没有把尾部旧图的数值用于新图。

## 2. 显式身份与参数门

新账本只接受明确 pin 的 producer `db6f-tail-transfer-background-v3.py`（`bdf6307fd93328b1ae70923caac2687fa19b0187ca9c723fe5d7072d7799a47b`）、原 base transfer（`35aa82514ec2be4b78cf3670e97343d0ba50085a7a6a687273108fbb6eb09705`）及策略 `visible-flat17-bookkeeping-keys-v2`（canonical SHA `2b4fd1d141d9116157037d05748ab2a019c9033441453ee8e6ab917eb355eae3`）。它核磁盘实际源码，不把新入口伪装为旧 SHA，不进行 monkeypatch。

允许集合独立列出后与导入的新 producer 集合严格比较。相对旧集合仅新增 `iterationCheckpointFile / sharedEngines / trialDiagnosticFile / trialStatePrefix`；三路径项限字符串或 `null`，共享开关限布尔或 `null`。键存在性及严格 canonical JSON 值都参与比较，未知改变、未知新增/删除 `null`、布尔/数值及嵌套类型别名均不获许可。

六项背景定义采用固定、已审 SHA，逐一读文件核对。还连接：旧 manifest 的实际 checkpoint、旧 checkpoint 与其参数、原包与原 data、height 与 positive-alpha 的相同 checkpoint/calibration、positive-alpha 引用的 height 文件、tight-alpha 引用的 A/B 文件以及共同 bookkeeping。`verified=True` 不替代这些实际核验。

正式模式另核真正的新 manifest、其实际 checkpoint 和参数、原图定义中的 tail manifest SHA、旧新精确径向域、跨度数及转包后完整分区。到这一步成功后，才运行原闭图数值账本。它仍不自动生成新图的 tail-first、prefix metric、moment 或全尾 metric/曲率证书。

## 3. 只读参数入口

为在最终图尚不存在时核成对接口，新增：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-audit-closed-budget-transfer-v3.py \
  --check-transfer-policy-only topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-transfer-v3-quarter-policy-preflight.json \
  --height topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-background-height-rigorous.json \
  --positive-alpha topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-audit-positive-radial-alpha.json \
  --out <新的参数预检JSON路径>
```

该分支拒绝 geometry、metric、moment、tail-first 及正式 transfer 参数；不调用 `grid`、`ExactHermite` 或旧数值账本。它也拒绝混入 `finished`、新 manifest SHA 或新数据输出字段的伪预检。输出仅表示参数与来源兼容，明确 `radial_grid_was_evaluated=False`、`geometry_metric_curvature_were_evaluated=False`、未创建图、未转包和 `README_complete=False`。输出路径已存在时拒绝覆盖。

正式模式沿用旧账本的七个证书输入，加 `--background-transfer` 指向**正式**新 producer 报告。此时应沿用旧账本对其真实文件路径的调用约定；并非把上述参数预检文件改名即可使用。

## 4. 实际执行与独审

作者自己的真实参数调用实际 exit 0，用时约 0.218 秒，峰值子进程 RSS 28,020,736 bytes。输出 `notes/2026-11-09-db6f-audit-closed-budget-v3-quarter-preflight.json`，SHA256 `f91bcfe5969d0ffaeec2a9951fe92535b2c8def9f17a49fd12beca55e10d517f`；同 stem 的 log/execution 记录已关闭。源、六背景身份与十二个允许差异键全部通过。

`tail_theory` 未参与该 consumer 实现，已全文独审参数/身份门、两种模式隔离及旧账本 AST 保持，并独立重放参数模式 exit 0。正式审稿为 `notes/2026-11-09-db6f-tail-review-closed-budget-transfer-v3.md`（`be9d4e9253fe719033c8d1a18bd6b85ea777171249b780bfe604802a5be13c51`），机器记录为同 stem `.json`（`78224cdc7a6780bc95f3f8fd8c982b7db8b23348a6ebea70522c7b3bfcf4c617`）。producer 本身则由本人另行独审，范围和证据见 `db6f-audit-transfer-v3-review.md`；没有循环宣称自审独立。

此时正式 transfer 与新图 budget 两条几何分支均未执行。后续必须先有最终解及其真实有限图，并按该图自身的 source/manifest/两 jet 接口重新认证。接口完成不代付 G5，也不把 $s=.25$ 的有限 warm 检查点视作最终曲面。
