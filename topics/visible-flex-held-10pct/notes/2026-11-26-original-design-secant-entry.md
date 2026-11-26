# 原 R53 δ-design 的完整状态 secant 初猜与独立恢复入口

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

这是求解入口，尚无该入口的实际预测包、Newton 返回或接受结果。没有改变在运行的原设计链，也没有把初猜登记为新场或固定度量精化。当前原链已经实际通过 λ=.032；新 runner 若重新通过已登记的 λ，属于恢复和算法比较，不能再记作新数学结论。

## 1. 唯一的新数值选择

设两份真正通过原门的原 R53 设计结果位于 λ_L<λ_R，且 M、完整 base profile、数值 chart、gauge、warp、线性 port、pscale、源码与其他 core 设置相同。它们的实际 δ 和原 support 参数可以不同。原 portable 参数 p₀ 是 base profile 上的**加性 δ 增量**，不是暖模型的 log(q_aux/gauge)。

使用每份实际 `inner-00.npz` 中原 `cubic_c,cubic_x` 所定义的计算坐标 t 的 SciPy `PPoly(axis=1)`，不重新拟合插值。公共网格优先取两份实际网格的并集；若并集超过原 max_nodes，则取右场原有网格，仍在这个共同 t 网格上评价左右两份完整原 PPoly。记录实际 grid_rule、union_nodes、right_nodes 和 max_nodes；没有截断状态、重新拟合或增大求解预算。令

β=(λ_target−λ_R)/(λ_R−λ_L)，

Y_pred(t)=Y_R(t)+β(Y_R(t)−Y_L(t))，

p_pred=p_R+β(p_R−p_L)。

所有 3M+1 个状态分量和全部 M 个原参数一并预测；没有丢失 inlet projection 或另行补造高度、均值或物理 s 图。共同 pscale 逐项相同，所以参数外推保留原 support 控制坐标。不同 δ 下的物理径向图可以不同；这里仅在共同的计算 t 上提供 Newton 初猜，不声称 Cartesian 两图相同或 C² 差已付。

输出仅为 `initial.npz` 的 x/y/p/pscale 和小型 `predictor.json`。没有复制原成功 RMS、没有造 `run.json`、没有生成“accepted physical”文件。预测包所有 solver/domain/BC/metric/true-tail/complete 标记均为未付或 false。后继仍由原 portable 的实际初始域检查、原 Newton、原 RMS、物理 BC 和全 metric 审计决定。

## 2. 来源与验收

`material_design_secant_predictor.py` 逐侧调用原 controller 的 `original_finite_checks` 与完整 raw/physical SHA 检查，并核 finite metric≤1e−6、真实成功/status=0、原 RMS≤tol、物理 BC≤原 physical_bc_tol。三类原容差上限仍是 1e−6、1e−7、2e−9。

入口明确只接原 `portable_prefix_continue.py` + `material_support_factory.py` 的正 λ、linear-DN 设计返回；拒绝暖 phase 模型、actual-DN、fixed-g、probe-only、skip-audit。所有已登记 source/input 文件必须仍逐项匹配 SHA。两份完整 profile/chart/gauge/warp/port/source/pscale、实际 angular/mean 档和原门相同，仅 core 设置中的 homotopy 可不同。实际 mean 节点数还必须至少是 16(3M+1)。

保存的真实 cubic、raw y/p、rms、pscale 与 physical C² 文件都检查有限性、原维数、p 同一与 SHA；原 cubic 在原节点重现原 y，只允许 32 个双精度 epsilon 的按量级求值舍入。公共网格不能超过未改变的原 max_nodes；并集过大时的右场网格后备使用真实既有网格，仍保全部分量的 secant 定义。来源 provenance 保留左右实际 λ、run/raw/physical SHA、δ、RMS、metric 和 BC。任何失败只拒绝这份预测入口，不把缺失文件或不合格输入替换成模拟结果。

## 3. 原控制流继续保留

`material_design_secant_continue.py` 从原 `material_design_continue.py`（SHA `7f85c3b422416b867a8fd19155583c1e8758fb45729ced1445c290f628360d5d`）作小范围复制。原 solver 命令、容差、port 导出、实际接受门、失败减半 λ 与仅 metric 失败升 M 的规则保持。

只有当前 seed 是真正 accepted 场，且已有两份同 M、不同 λ 的 accepted 历史，才调用 predictor。RMS/BC/domain/solver 失败场不会进入 secant 历史。仅 metric 失败但实际求解完成的完整场，仍只能按原规则作升 M 初猜。M 升阶始终调用原 `prepare_lifted_mode_restart.py`，保完整 exact lift 系数 1；没有两份同 M accepted 场时不把跨 M 参数直接相减。实际每次接受后更新 source 历史，下一步再按真实新场计算 secant。

## 4. Fresh runner 最短命令

已有 workflow 先照原样执行 `tail_recovery_setup.py --repo @REPO@ --work @WORK@`。随后：

```sh
python -u @REPO@/topics/visible-flex-held-10pct/scripts/resume_20261126/lowq_prefix_recovery_secant_design.py \
  --repo @REPO@ --work @WORK@ --outdir @WORK@/secant-design-recovery
```

新 harness 的 q=.006,.012,.02,.03,.04,.05,.06 checkpoint 链、λ0 完整 lift、λ=.002 的 M8→M16→M24 原 solve/transfer 块，保留 `lowq_prefix_recovery_design.py`（SHA `a69f5c6ca118221700b16f01645b87be94afba349ca576825c47993891c22223`）的实际执行。最后只先调用原 design `--targets .004 .008 .016`；取得本 runner 真正接受的同 M 锚后，再调用 secant controller 走 `.032 .064 .128 .256 .512 .75 1`。M 列表仍为 `24 32 40 48 64 80 96 128`，不启动暖 v1/v2/v3/v4、Newton probe、cold M16 或旧 λ.004 独立尾。

正常恢复链会给出同 M32 的 λ=.008/.016 两锚。若原门实际要求不同 M，则如实记录有没有同 M 历史，仍保原 raw / exact-lift 规则，不伪造 secant 配对。

建议 live diagnostics 读取以下三个小文件：

- `secant-design-recovery/summary.json`；
- `secant-design-recovery/original-design-to-016/summary.json`；
- `secant-design-recovery/secant-material-design/summary.json`。

每 15 秒记录实际子进程日志尾与原事件；完整数组始终留在同 runner。新 parent 和 controller 的 scalar summary 都限制为 1 MB。

## 5. 已做验证与未付范围

本次实际执行三文件 `py_compile` 与三个 `--help`，全部退出 0。独立参数/schema 审读确认原 p₀ 加性 δ、support pscale、PPoly axis=1 和同 t 预测语义一致；据该审读补了实际 mean 下限检查。根审提出并集过大不必提前停止，据独立数学核对加了上述右场原网格后备，随后重做该文件 compile/help。没有本地实际 accepted 数组，因此没有运行本 predictor、求 BVP 或证明其改善收敛。

仅 δ 标量能提供动机：用旧链的真实 .008/.016 δ 作 β=2 外推，得到约 .06413342836018932；该旧链真正 .032 δ 为 .06413339850075069，相差约 2.99e−8。此算术没有包含完整场，也不替代新 runner 的预测和验收。即使后续 λ=1 的有限线性设计通过，真正完整 DN、共同 C² 接缝、固定问题收敛极限、时间闭族和 reach 仍须分别实际完成。
