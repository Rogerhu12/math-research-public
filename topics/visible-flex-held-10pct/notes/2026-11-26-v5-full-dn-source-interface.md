# v5 δ/phase 设计接原 full-DN 的源码接口

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

本次只审现有源码；没有运行新的尾、BVP 或导数实验。v5 真零锚已在 runner
通过不等于它已有非线性尾。以下接口须由其后真正通过原门的 v5 solver return
作为输入，保留原 full-H 请求、最多8次实际外迭代及原 finite gates。

## 1. 求解器主干相容，不能把零锚当 solver return

`resume_m3/portable_prefix_continue.py` 第101–121行先安装指定 core provider，
再安装完整 `exact_core_lift` 与该 provider 的解析参数 jets，最后在同一个
Base 上混入原 `TailMixin`；构造仍是 `fixed=False`。没有硬编码必须使用
原 normal-support family。v5 因而可以保持：

- 原 base `physical_profile`、真实 raw `p0`，即
  `delta_actual=physical_profile.delta+p0`；不重编码成 qaux，不冻结 δ；
- `q=gauge` 始终固定，`d1=0`；高参数为 R70 的 j=2..M 相位未知；
- 完整实际 baseline、λ、S/b/k、phase_scale、provider 及所有间接依赖；
- 原 raw t/Y、chart、warp、pscale、M、angular、原 audit mean 与各门。

v5 controller 的新真实返回保留原 `portable_prefix_continue.py` command。
故 generic `continue_actual_mode_true_tail.py` 第84–86行的 runner 身份检查
对这种真实返回适用。零锚的 command 是重表达入口，且 success/status 为 null；
它被拒绝是正确行为，不应改写 command 或补造 solver 状态来通过。

接 v5 时最窄的来源判定是现有
`warm_delta_phase_entry_v5.accepted_input(source_run)`，并额外要求
`acceptance_kind == SOLVER_RETURN`。这会同时保留已实现的真实 raw/status/RMS、
physical BC、metric/angular、源/输入/hash/数组以及完整 v5 provider 语义检查。
generic 当前较弱的 `prefix_gate` 不能代替这项已有合同。

## 2. δ 列和高相位列均仍是原完整方程的列

v5 factory 只固定旧 q API 并屏蔽不允许的 q jet；它不挤占 δ 列。
`analytic_adaptive_core_jac.py` 第11–24行仍用真实 core 的完整位置/一阶/
二阶参数 jets，扣除入口投影，保留 `aχ` lift 和角图 convection，再乘原
pscale。第25–26行在 `fixed=False` 下，以原步长
`2e-6*max(.1,delta_actual)` 对完整 `self.fun(t,Y,p)` 作 δ 中心差分。
因此 profile、物理 s(t)、ds(t)、随 δ 改变的径向 lift 和角图均在这一列内。
这是原差分列，未声称已认证连续精确导数误差。

`LiftBVP.fun` 每次先调用 `initial(p)`，将当前 core/投影绑定到当前 Flow。
δ 改变时的新 Flow 同样获得该完整 lift；没有仅在最初 Flow 安装参考核的遗漏。
`TailMixin.bc_jac` 调用 `super().bc_jac`，因而入口高参数列也由同一
`initial_jac` 返回。尾只替换末端状态导数块，不重解释 p0 或高相位坐标。

## 3. 为什么末端参数底块为零没有漏掉 δ 或 phase

令 q 为固定 gauge，σ 为桥的方向，Pz 为高度状态选择矩阵，
W=diag(bcweights)，E 为固定 cut 的尾度量系数。原实际末端条件是

\[
H=\sigma qP_zY_b,\qquad
B_{\rm tail}=W^{-1}\left[qP_z f_{\rm cut}(Y_b)
                    -\frac{\mathcal D(H)}{\sqrt E}\right],
\]

其中 \(\mathcal D\) 是这一次完整 H 的实际非线性 slope DN。
原 `TailMixin` 第23–31行正实现这一式及

\[
D_{Y_b}B_{\rm tail}
=W^{-1}\left[qP_zJ_{f,\rm cut}
       -\frac{\sigma q}{\sqrt E}D_H\mathcal D(H)P_z\right].
\]

在这里固定 Yb 后，没有剩余参数直接项，理由必须同时用到以下事实。

1. 当前 multistage profile 的 up/down 精确面积为 ±δ_ref，全周期回半径1，
   末端速度0；δ 只移动前缀的物理终点，原 bridge 与 cut 的局部几何保持。
   这项范围是 R72 已说明的当前输入，不是任意可变桥的通用结论。
2. adaptive 角图在实际 cut 的 e、e′、e″ 为零；因此 cut 无残留角图对 δ
   的一阶/二阶坐标贡献。
3. 完整 core lift 的 χ 在 .9 prefix_end 以后为零，且相应 jets 为零；
   cut 位于其后。固定 Yb 时，phase/core 的直接末端依赖已经消失。
4. q、完整 tail background、cut、E 和 BC normalization 固定。
   特别 H 乘的是 gauge q，不是一个 phase auxiliary q。

故 \(\partial_p f_{\rm cut}|_{Y_b}=0\)、\(\partial_pH|_{Y_b}=0\)，
原 terminal 的参数底块确为零。完整 BC 的参数矩阵仍为
\(\left[-I_p;\,0\right]\)：δ 的入口列也为零，而高相位入口列通常非零。
这不表示 δ 对整个问题没有影响；其内部 RHS/chart 列恰由上一节支付。
浮点评价与保存的实际 cut jets 仍须在运行记录里核，不能把这项源码代数
写成某个新实际场的有限差分验证。

如果未来改 tail background、cut、q 或不再平掉 lift/角图，就不能继续沿用
该零参数底块；届时须增加相应直接导数。本次 v5 接口不作这些改变。

## 4. full-H、真正外迭代和有限门保持

原 portable 第220–247行先做明确因子的暖请求，再做**完整未缩 H**的
`jacobian=True,audit=True` 请求。最多8次内层暂用 affine slope DN；每个
成功的内层实际返回后，又对其完整 candidate H 求原 DN/J/audit，并切回
实际 tail 计算完整 BC。只有这个实际 BC 到原容差才结束，affine 对象不能
提供最终审计。随后仍写真实 raw、physical、原 metric audit 和 seam audit。

对最终 v5 actual 记录，应保留原 `actual_tail_requested`、实际 outer checks、
full-H 包/J/源/hash及原 solver/RMS/BC/metric 门。现有 v5 `accepted_input`
明确拒绝实际尾身份；它只能验证这里的**线性来源**，不能用来认证最终 actual
输出。也不能改贴 v2/v3/v4 actual 的 KIND，因为 v5 参数0的含义不同。
原 portable 已保存 `core_settings` 与 raw 的实际 core summary；最窄输出
绑定应沿这两项声明 δ-design/phase 家族及本次真实来源，不伪造固定-g 标记。

### Mean 的具体范围

继承原 command 保留 prefix audit 的
`N=max(audit_angular,16*(3*M+1))` 及 GL6 高度 primitive：M24 通常为1168，
M32 为1552。没有理由在接尾时强改成1168。

原 `TailMixin.seam_audit` 第33行却用 `max(512,64*M)`，M24 为1536、M32
为2048。这仍是原门/原诊断，但它的 mean_first/mean_second 不是源 Cartesian
图相同 literal mean 的两 jet。有限 full-DN 接受不能因此升级成同图 C² 接缝
通过。后续同图接缝必须另在保存的源 N 上读取同一 `velocity_s` 均值；本次
接口审查不修改原门，也不新增独立自由 mean BC。

## 5. Native/chord 的最窄执行差异

actual_tail 已独立核了 chord/native4worker 源绑定，本条不重复开发。
现 generic coordinator 只 shared→periodic→native，没有装 bounded chord；
单往配置里加 `chordMaxCorrections` 不会启用缺失的实现。可复用 runner 已有
`chord-source` 与二进制，由原 `prepare_recovered_native.py` 为实际 M、N、
spacing、steps 和 workers4 生成 fresh 目录/manifest，再继承实际 source command。
保持 M≤64 与 N>4*M*spacing；旧 M24 manifest 不能拿去算不同 M。

先用原 baseline tail config 核 port.source.config_sha256，再由其复制 runtime
config，仅加入声明过的 chord/trace/warm-checkpoint 执行项。runtime 的新 SHA
不能冒充原 port 的 baseline config SHA。现 generic 入口没有这项双重绑定，
这是必要的窄协调改动，和 v5 的方程/Jacobian 无关。换 native source 前核
实际 prefix Python/profile 安装文件与原 source 字节相同，且完整 v5 provider
及间接依赖路径/SHA仍由原 settings 绑定。

## 本次实际读取的源 SHA

课题内路径以 `scripts/` 为根；旧源目录是恢复包中的
`topics/visible-flexible-closed-surface/scripts/`。

| 源 | SHA256 |
|---|---|
| resume_m3/portable_prefix_continue.py | 6dafa9551d5ae4a4f4d59e1b2d4c177efdc6b823e0a7ade826974e4ecdc5c9ea |
| resume_m3/continue_actual_mode_true_tail.py | a78623eaf09c51b0761f1fc610dfe6d46b42b79efa13912d5410430c6498ae52 |
| resume_m3/round_raw_lib/exact_core_lift.py | 28936553078df9d1a2c6486fab1613c20fd7cfdb9b4134d4c95e1d60fa5623f5 |
| resume_m3/round_raw_lib/analytic_adaptive_core_jac.py | da6690d9f11eac38cec0acee31aa07555a8d1ddd81c1b24997db0421ea19e431 |
| resume_m3/multistage_flat_profile.py | 887a8d04157dfcee504f80d8cc2e7b66d9ae430775b4bc1df0bfea70bd49ceed |
| resume_20261126/warm_delta_phase_factory_v5.py | 56772568ba9ddbfcf78d65cb0104991b694a4806335914762158a58d2391fc83 |
| resume_20261126/warm_delta_phase_entry_v5.py | 4628b1431b8d09ad661766012b50462dcdbfc1469c23c2b2f9f2f41e26332ba8 |
| 旧 db6f-prefix-coupled.py | 37defb33c031fd967ab0e06e086da56f2d67e30dd88bbbcb8e5e13201476511a |
| 旧 950f-prefix-adaptive-chart-bvp-v2.py | 958a9e2e428f8d64dfc786bed515bad77a208433fa16af7cbbe6f03b1bcc7ebe |
| 旧 950f-prefix-warped-bvp.py | eb70e36397ea47638e042e7f2ef465ccef30cd853342adf049c2e3718261ac70 |
| resume_n4_tail/native_extended/prepare_recovered_native.py | 08f6f0de7e1737a41864d9d420f48255a523c8aebea36dfa75de1a45940bc99b |
