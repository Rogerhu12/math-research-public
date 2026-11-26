# v5：原 δ 设计变量与 R70 高阶相位控制的最小接续

本记录只交付可执行入口及一次小型合成接口检查。没有在本地执行真实
零锚重表达或 BVP，没有 λ 推进成功、原非线性尾成功、固定 g 收敛或闭面完成结论。
不改已部署的 v2/v3/v4、原 portable driver 或原升 M 脚本。

## 1. 参数与完整问题

沿用 R70 的完整相位族

\[
\phi_\lambda(u)+\sum_{j\ge1}d_j\Psi_j^\lambda(u).
\]

当前设计入口取切片 `d1=0`，未知数为原来的 `p0` 与 `p1,...,p_(M-1)`：

* `p0` 是 **原 physical_profile.delta 上的加性 δ 偏移**；不改 base δ，
  不把真实 raw p0 重设为零，不重设原径向 chart_reference_prefix。
* `q` 固定为原 gauge，只作为旧 API 值；改变 q 的调用会拒绝。
  它不是正数相位坐标，也不编码 p0。
* `j=2,...,M` 的真实 phase 控制由旧 legacy 输入经相同已声明比例映射。
  旧输入是 `c_j=p_(j-1)*max(q**j,1e-9)`；实际 provider 计算
  `d_j=phase_scale*c_j/max(q**j,1e-9)`。
  理想实数公式为 `d_j=phase_scale*p_(j-1)`，浮点实际值以 `core.controls` 为准。
* 完整原 support 向量、S/b/k、原 anchor_core_settings 全部保存在 config；
  升 M 不截掉该 baseline，不把旧 support 高模当新 phase 高模。

原 fixed=False BVP 的高阶解析参数链仍由原 `analytic_adaptive_core_jac.py`
处理；q 槽在 fixed=False 本来被屏蔽，v5 也将这个不允许的 API jet 设为零。
δ 列仍由原代码对完整 `self.fun` 作域内中心差分，包含径向坐标、参考 lift
与 convection；没有把它换成只有入口变化的列。
λ 是一轮求解外的设计参数；改变 λ 时重新构造完整 baseline 和 R70 混合基。
非零 d 下的 λ 交叉项仍由 v4 的真实公式包含，没有将 λ 当作本轮 BVP 未知列。

这一步用 δ 选择 g，故全过程明确 `fixed_metric=false`。真正原 full-H 与
8-outer 门通过后，才能冻结最终 δ 和该源自己的 mean 规则，再在**同一完整
R70 族**释放 d1 作为未知解变量做固定 g 精化；d1=0 不是必须永久冻结的物理参数。
这些后续步骤不在本入口中冒称已付。

## 2. 零锚身份

`warm_delta_phase_entry_v5.py` 只接受实际原 R53 portable linear-DN 返回：
真实 solver/raw 状态、RMS、物理 BC、原角下限/metric、完整 raw/physical SHA、
source/input SHA 及真实参数/尺度/数组形状都先核验。

从原 raw 复制 x/y/cubic/pscale 与原 physical quintic，仅把高 p 设零；
保原 p0 和原 physical_profile。新 core 直接委托同一个完整 live baseline。
实际重算旧/新 RHS、中点 RHS、collocation residual、原离中点 RMS、BC，
以及原 RMS 全部所用点的 s/ds；它们必须逐位相同。
完整 core 三个 jet、七个物理 s 点的六个 Cartesian jet（含原 literal-node
mean 及 mean 导数）也必须逐位相同。位置比较中的共同垂直均值原函数以同一
原点和同一积分规则定义，故在该差中抵消；没有另造一个高度插值图。
之后用原 adaptive.audit 和**源自己的原 mean 节点数**实际复审；metric 标量
也要与原记录逐位相同并过原门。

该记录明确 `solver_invoked=false`、`solver_success=null`、raw
`success/status=null`。原真实 solver provenance 单列。`geometry_command`
只记录构造方式，明确没有执行；实际 `command` 是这个只读/重表达入口。
controller 只通过专用 `accepted_input` 识别该身份作已核初猜，绝不向原
prefix_gate 喂一个伪造的 solver success。

## 3. 真实接续与升 M

`warm_delta_phase_continue_v5.py` 复制**真实源的原 portable command**，
保留 `portable_prefix_continue.py`、verbose、原 RMS domain guard 和所有
容差，只替换 core module/config、raw restart、目标 M/angular/port/outdir。
删除互斥的旧 checkpoint/control-record。默认最多三次实际 BVP 尝试。

每轮以原实际 status0、RMS、物理 BC、角下限与 metric≤1e-6、完整 raw/physical
SHA 共同决定晋锚。失败不覆盖最后已接受场。若 driver 在初域/求解前就失败且无
真实 raw 返回，只记 `driver_invoked=true`、`solver_invoked=null` 和独立未返回
身份；不称 solver 已返回。已收敛且仅 metric 未门的真实场可作升 M 初猜。

原 `prepare_lifted_mode_restart.py` 需要真实 solver_success，因此不接零锚
重表达。可用时完整保留原系数 1 的
`embed(Y)+a*chi*(I_new-embed(I_old))` 转移和原六 jet 数值检查。
新 port 由原 exporter 在相同物理 tail 参数上生成，数值 quadrature 可随 M 增加。

v5 额外只读实际 `core.controls`，保存升 M 前后 phase 向量 NPZ/hash 与
共同分量的 l1/linf 差；完整 baseline/λ/尺度/新增零列保持。原
`p*scale/scale` 的浮点 roundtrip 不新增停止门。整个结果始终只是
`unaccepted_nodal_initializer`，不称精确同图或已接受解；其后仍须真实 BVP 全门。

设计升 M 沿用原 audit 规则，其实际 mean 通常是 `16*(3*M+1)`：M24 为1168，
M32 为1552。记录真实值；不把改 mean 的设计步称为同 Cartesian 图的固定 g 精化。

## 4. 调用

从同 runner 的实际原 R53 `run.json` 调用；若手头是 v3 零锚记录，取其经核
绑定的 `origin_design_run`，不能把 warm run 直接冒成原 source。

```text
python scripts/resume_20261126/warm_delta_phase_continue_v5.py \
  --repo /actual/repo --work /actual/work \
  --source-run /actual/work/original-r53/run.json \
  --outdir /actual/work/v5-first-three \
  --targets .004 .008 .016 --max-attempts 3
```

若 `work/m24-tail-settings.json` 不是原设置位置，显式传 `--tail-settings`。
零锚也可单独调用 entry 的 `--repo --source-run --outdir`。所有数组写在 repo 外。
summary 只投影必要状态、残差、门与 hash，不复制完整参数向量。

## 5. 本次实际小检查及边界

四个 Python 文件的 AST/编译与两个公开 CLI `--help` 已实际执行通过。
`check_warm_delta_phase_v5.py` 在实际原 support 源上合成 M24 核，
λ=.002/.5/1、phase_scale=.5。三档均实际核过：零控制 F/Ft/Ftt 逐位同一，
固定 q 的拒绝规则、禁用首 API 列、高阶 j=2/8/9/24 的两个 jet 参数中心差分，
以及 M24→M32 的共同基/实际 phase 控制零扩展。最高绝对 FD 差
`4.111982698784544e-10`；本次零扩展三个 jet 差均为0。
具体执行和 source SHA 在 `v5_synthetic_check.json`。

这不是实际原场重表达的成功记录。真实 source 只在 runner，需按上述入口
实际核 identity，再进行真实新 BVP。没有由 R70/R71/R72 或该小检查推出
完整 BVP 可逆、λ 推进成功、准确等距、全尾闭合或题目完成。
