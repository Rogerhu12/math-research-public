# R144：实际完整终端均值小球、唯一紧支撑小根与正密度

2026-11-26，visible-exact-astra-198c63d-20261126。

**已证明。** 公开 run 45791979634/1 对原固定 $\eta_0,\nu_0$ 对象完成
[TM](R144-supplement-terminal-mean-small-ball-controls-normalized-forward-constant.md)
的全部五个标量阶段。给定精确有理区间内存在唯一紧支撑参数根；
相同区间内的终端均值严格负，$Y$ 严格正，材料密度严格正。
原 ordinary 均值残差、全部6143个原均值接口与原初值误差均已支付。

独立的同材料角 $10^{-4}$ 距离充分门为 **false**，并完整保留。
它不推翻已通过的均值结论，也没有证明真实距离违反阈值。
完整moving状态距离、非均值方程和完整闭曲面仍须继续完成。

## 1. 同一完整实际运行

| 对象 | 完整实际身份 |
|---|---|
| run | [45791979634/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45791979634) |
| 触发提交 | d6d89679544cba1ad07d76487a153416bd0c4c74 |
| 科学实际 checkout | f1b35bbb596003ddb6767381da97d8fc14f11037 |
| manifest SHA256 | acb8c78b307d25a142b776e7fbb225172098f37c92230fc53ef7301870d1f41f |
| 科学结果 | [完整8300B](../notes/terminal_mean_small_scalar_gate_ci/run-45791979634-1/terminal-mean-small-scalar-gate.json)，blob 4e76b3bd28bace4c290d59e24ccac62fdb797f47 |
| 科学结果 SHA256 | a74d11052da41570a7588d5a79545cfb7295ccf437b3bae971390d59f2b99de6 |
| 执行记录 | [完整8971B](../notes/terminal_mean_small_scalar_gate_ci/run-45791979634-1/execution.json)，blob 87957b9b9636408bb99a0da1a3d35b17219a3ea5 |
| 执行记录 SHA256 | af0b8f547c4e4215bbfcd42f7e0546391ec247765c3a94c9634c3950acd5fe34 |

实际运行于2026-11-26 09:26:43–09:26:49 UTC；Python3.12.14、
python-flint0.9.0、320bits。一个科学子进程，返回0，无timeout；
science与execution均complete，science proved=true、failure=null。
实际完成5阶段、21个新标量球、3个精确有理参数、24次保存读回。
13个独立门的12个均值/小根/密度门为true，最后同角距离门为false。

11个当前小输入全部逐件核byte/Git blob/SHA；没有历史native恢复。
五次pull及两README检查保留完整首/末三条和全链hash，规则diff均空。
无旧科学目标、旧数值producer、native扫描、primitive、DFT、径向ODE、
forward W调用或新数组发表。

## 2. 真实前件及原初值不变

新证书消费 [C0/CP11实际](R144-supplement-actual-compact-mean-C0-receivers-and-positive-moments.md)
45787608966/1的52个完整球，覆盖全部7721正向cell、6143均值接口及
7721反向cell。其 $\overline a>0$ 已过门，所有11个有真实位置的
非线性核系数保持。

旧forward45772466407/1仅提供其已存完整初值球
`complete_new_scalars.initial_D`；它的旧有符号流目标和unknown门没有重算或改写。
原完整waist ordinary $L^2_r$ 接收字段准确为
`complete_waist_mean_gain_if_log_Gamma_below_100/ordinary_mean_source_L2_r`，
并非whole-body $L^2\to L^2$ 常数。
原第二ordinary残差取完整已成物理界 $\alpha\,8.194504\,10^{-8}$；
没有第二次乘幅度，也没有用该 $L^2$ 量吞掉独立跳跃。

对象仍是candidate
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`，
原mean native
`e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b`。
$\alpha,\nu_0,\eta_0$ 精确分数、全区间 $[0,25/8]$ 和52输入的身份
都由science与worker分别验证；没有把它替换为原selected成员。

## 3. 精确参数与已通过的依赖链

三个参数按完整保存的上端点 $(m+r)10^e$ 取精确Fraction，
包含保存半径。完整分数如下：

```text
b0 = 2041350487103749110837815890160249124517660875355345574814207691802136611809873/10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
rho = 21460056707081603122152938643711102791166498531461811749972659241455334243341969/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000
b = 13142628124696682772825015627534372899338540585644245009742038935869919279810971/50000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

这些是明确的有理半径，不是浮点显示值或重新调整后的proposal。
先以 $b_0$ 验证 $\xi=0$ 的terminal self-map、Lipschitz与负mean门，
再以同一真解的waist接收界得到 $b_w$。保存的完整上界为

$$
 b_w\le
 \big(48827090113690637980393733788594286750896474226029262379600399788326651734932761
 +1\big)10^{-87}.
$$

从准确恒等式 $\overline D=Y_f(0)-Y_t(0)$ 与原 $D_0$ 得到

$$
 |\overline D|\le
 \big(9137382049013663797868566371199477343219908865430669465782329964628968938548082
 +2\big)10^{-86}.
$$

随后同一 $\rho$ 通过 $0<\rho<1$ 及
$|\overline D|<a_-\rho(1-\rho/2)$ 的严格门。
右侧使用实际保存后读回的**下端**，不是拿一个上界比较。
由已成 $0\le\overline b\le\overline a/2$，

$$
 \overline D-\overline a\xi-\overline b\xi^2=0
$$

在 $[-\rho,\rho]$ 内有唯一精确根。
没有给根指定符号，也没有把根换为0或某个区间端点。

把同一 $\rho$ 代入完整四个profile多项式后，$b$ 通过uniform
self-map、严格Lipschitz和负mean门；独立密度门
$8\rho\sqrt{V_*}<g_*$ 也为true。
所有依赖标量与参数都由真实输出文件读回后再使用，最后全部门
保存、读回后才置complete/proved为true。

因此在这个相同区间内存在严格负的连续terminal mean，
在精确根处 $Y$ 与原指定waist初值的线性解一致。
该mean在waist等于 $-a(0)$，在outer返回原raw mean。
连续性由 $[q]_i=-[m]_i$ 实现；原nonmean接口并未由此自动修复。

## 4. 独立距离门的准确失败范围

本次计算的same-material-angle粗充分上界，保存后为

$$
 \|v_\xi-v\|_{L^\infty_rA_0}
 \le
 \big(11975924422637449552356606223762774756587899257336926292702315382723187307489117
 +2\big)10^{-83}.
$$

实际门 `same_phi_moving_C0_sufficient_1e4` 为false。
这是TM.11的全域粗接收量，不能把这一个上界超阈值说成真实距离
有一个超阈值的下界。它也不包含真实physical-angle composition。
后继需保留紧支撑 $\chi$ 的实际位置及原有限Fourier量的相关性。
原[最终几何 B.1](R133-supplement-final-geometry-from-complete-C0-ball.md)
所需的完整物理moving状态范数，按其前件
[C.1](R133-supplement-complete-C0-state-and-nu-geometry-response.md)，
准确为未除振幅的 $C^0_{r,\phi}$，保全部mean。
因此直接界定 $b\sup j_\xi+\rho\sup\chi|v-m|$ 即是这个状态门的合法入口；
本构造的same-$\phi$ 第一分量差准确为零。
固定physical-$\theta$ 的复合是另一个量，只在需要该坐标的实际端口中另付。
本次已成均值目标保持锁定，不重新选择半径重跑。

## 5. 关闭与剩余义务

本篇关闭原固定raw度量的标量mean构造：terminal small ball、
归一化forward常数的充分界、给定小区间内唯一compact root、
uniform负mean/正 $Y$、正材料密度及waist/outer两个mean值匹配。
旧whole-eta直接forward包围的unknown仍是其原结论，
本篇通过新的准确终端恒等式支付需要的数学义务。

[CS](R144-supplement-compact-centre-ordinary-and-divergence-residual.md)
的完整ordinary/divergence源现在已有真实 $\rho,b$ 输入。
两非均值方程、原nonmean jumps、完整moving距离、必要物理端口角复合、selected设计相位、
完整finite/high/mean/nu逆、径向帽jet、height、holonomy与位置周期
仍须各自实际完成。尤其outer mean回到raw值不等于全部outer物理行已解。
本证书没有构造全Codazzi解，也没有宣称最终固定度量闭嵌入族已经完成。
