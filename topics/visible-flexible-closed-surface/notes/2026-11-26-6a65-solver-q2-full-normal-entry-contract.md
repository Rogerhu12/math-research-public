# 实际 gap 支的独立全物理法矩阵入口

状态：**实现准备；完整 5292 列研究场尚未在本入口执行**。已执行的有限核是 `2026-11-26-6a65-solver-two-grid-area-full-normal-actual-check.md` 所列 126 非零列 / 10836 行检查。此入口的 Python 编译及 CLI `--help` 实际返回 0，不把它们当 nonlinear 接受步。

新入口 `6a65-geometry-gap-window-area-power-two-full-normal.py` 的 SHA-256 为 `2af9f7fac1a74b327007952e473f7498de6a1a9fee99ca6cd269222e6e5d80c4`。完整法矩阵 helper 的 SHA-256 为 `8e8d40c05ba5b5e15c49be4c7d91c882d93007567f67caa19a4a43ad39bc2084`。旧 q=2 物理目标入口保持 `3dcb94971b5975a7046cfcd67bb5d57f60581527b526e8700c8cfc81fd34151f`，没有原地修改。

## 消费与实际计数

```sh
python 6a65-geometry-gap-window-area-power-two-full-normal.py \
  --scripts /frozen/topics/visible-flexible-closed-surface/scripts \
  --prepared /same-run/actual-prepared.json \
  --state /same-run/actual-parent-state.json \
  --prefix /same-run/fresh-full-normal-step \
  --steps 1 --operator-epoch ACTUAL_FULL_COMMIT_SHA
```

实际父态允许已冻结的 refined、q=1 或 q=2 入口及自身 schema。所有分支先核相同 prepared 字节、源身份、固定目标 $g$、完整基、point config 和入口身份；q=2 父态另核原完整目标 recipe 与面积定义。自身续态核 canonical 模型摘要、入口字节及 epoch。

父态接受总数仅记 `carriedPreviousSolverAcceptedSteps`；新 solver 只递增 `fullBandAcceptedSteps` 与 `fullBandAttemptCount`。新实际 baseline 不计接受。每一步写 fresh INITIAL / step state / report 到 runner 临时区，真实拒绝仍写未接受状态并停止本批。若父态是 q=1，此处是明确 q=2 新目标；若父态已是 q=2，则物理目标、固定 $g$、双网格和全部 5292 列不变。

## 解法与验收

每次完整 LM 构造全物理 $H=J^\top J$，不丢跨 Cartesian 或角通道项。默认取 $\eta=\lambda$，依 R244，预条件后的增广法矩阵在精确算术下为单位矩阵。仍实际调用完整 $[JT;\sqrt\lambda L_S^\top T]$ 的 LSMR，`damp=0`；可显式提供固定 `--preconditioner-eta`，其数值记入新模型身份。

实际报告保留完整组装 / 带因子成本、LSMR 退出、原物理 normal 相对残差以及全 nonlinear 试步。原 q=2 Armijo 条件、所有 metric / 曲率 / 几何行、两组完整观察均保持。两组都是参与目标的网格，不把它们冒称为第三独立观察器。$\eta=\lambda$ 的代数性质不是某个真实场已经收敛的证据。

当前活动 q=1 receiver 只允许其旧模型追加或释放；它不能接本入口。必须用明确的新 controller / epoch，重新生成所需实际父态并在同 runner 直接消费，或使用另一个已经支持新模型的合法边界。不能把换入口藏在旧 `additional_area_attempts` 中，不能继承已结束 runner 的丢失数组。按根 README 第 15 条，只发布源码、参数、run、输出 SHA-256 和 Markdown 实际结论；完整状态、缓存、报告与数组均不入库或 Release。
