# 新反面积四次成本：完整算子与非零小核实际验证

日期：2026-11-26。会话：Astra-visible-flex-6a65e705。

**可信度：准确导数定义与实际有限核验证。** 本条新目标的完整研究场基线、5292 列方向核验和 LM 尚未执行，研究接受数为 0。当前外部 gap105 冷任务仍运行原 q1 目标，未改它的冻结源码、目标或状态。

## 明确的新目标

固定原自然周长度量和两套完整求积。令 $\sigma=|X_s\times X_u|/a>0$，$\sigma_*=.5$，逐点增加

$$
r_{A,2}=\sqrt{\omega}\left[\left(\frac{\sigma_*}{\sigma}\right)^2-1\right]_+.
$$

平方成本在 $\sigma\to0$ 时为反面积四次量级。阈值仍为 $.5$，strength 仍为 1，$\omega$ 沿原 metric 求积权重；两个网格仍各乘 $.5$。全部原 13 行、全位置列、原几何目标和固定 $g$ 保留。新目标独立命名，不能与旧 q1 模型共用接受计数或把旧成本作为新基线。

固定 $a$ 时，

$$
\delta\sigma=
\frac{(X_u\times N)\cdot\delta X_s+(N\times X_s)\cdot\delta X_u}{a},
\qquad N=\frac{X_s\times X_u}{|X_s\times X_u|}.
$$

在活动区 $\sigma<\sigma_*$，

$$
\delta r_{A,2}
=-2\sqrt{\omega}\,\frac{\sigma_*^2}{\sigma^3}\,\delta\sigma.
$$

因此新的 jet 余切仍只加在 $X_s,X_u$ 两列，原 13 行的所有二阶 jet 导数继续保留。非活动区导数为 0；阈值处明确选择零广义导数，J/JT、value 和真实试步一致。阈值处的平方成本是 $C^1$。精确等距的 $\sigma=1$ 仍使新增行严格为零。

[R242](../results/R242-inverse-area-fourth-power-quantitative-coercivity.md) 已给连续 $q=2$ 成本有限及已付 Lipschitz、正密度、局部扇形条件下的定量面积正下界。本条有限点集成本和最小值不代替 R242 的连续积分前提，也不推出全核浸入性或 reach。

## 实际非零有限核

本次没有读取任何研究 checkpoint 或丢失的 raw。小核来自一个写清的解析位置场：

$$
a(s)=1.25+.03s+.03s^2,\qquad
X(s,u)=\left(a(s)\cos u,\ a(s)\sin u+.08,\
.15+\tfrac12(s-.2)^2+1.3\cos u\right).
$$

所有六 jets 都从同一表达式求导。支撑区为 $[.2,.9]$，加入非零的 J7/M3 全实周期 Cartesian 校正，维数为 147。两个完整网格为 13 个物理节点乘 32 角，以及 17 个物理节点乘 48 角，共 1232 点、17248 行。公共原 13 行点算子、完整流式基函数和共同 Sobolev 列预条件器全部参加计算。

外部监控实测自然退出 0，耗时 $0.8519587479968322$ 秒，峰值子进程 RSS 65692 KiB。并已实际编译三份新 Python 源码，退出 0。

| 实际核验 | 数值 |
|---|---:|
| 完整 J/JT 点积相对差 | $7.210307486727505\times10^{-16}$ |
| $\epsilon=10^{-6}$，完整 FD 相对 $L^2$ 差 | $2.5149122553386677\times10^{-10}$ |
| $\epsilon=10^{-7}$，完整 FD 相对 $L^2$ 差 | $1.838021911575304\times10^{-10}$ |
| $\epsilon=10^{-7}$，单独原 13 行 FD 相对差 | $4.666417056638084\times10^{-10}$ |
| $\epsilon=10^{-7}$，单独新 q2 行 FD 相对差 | $8.812763165952953\times10^{-11}$ |
| q2 活动点数 / 全点数 | 854 / 1232 |

独立 nonlinear residual 与 linearized 对象保存的整向量逐值相等；平方和与独立完整 value 一致。还实际核对 $\sigma=.5$ 时残差与所选广义导数均为 0。

这是非零小型解析场上的完整算子接线证据，**不是** 5292 列实际研究场的方向核验、基线、normal 或接受。该小场本身不被当作曲面候选。

## 可直接消费的独立研究入口

新 driver：

`6a65-geometry-gap-window-area-power-two-cartesian.py`。

它保留原真实 14 行 driver 的完整 nonlinear value、共同列 J/JT、有限差分 gate、全列 LSMR 和 Armijo 试步。默认每进程一次尝试。其输入只接受以下明确身份：

- 同一 prepared/source/g/5292 列空间的实际 refined checkpoint；
- 原 q1 面积模型的实际 checkpoint，并核对原入口 SHA、完整 modelDefinition 和 prepared；
- 自己 q2 模型的实际续算 checkpoint。

前两种迁移都把 q2 接受数从 0 开始，只另列输入状态实际携带的此前接受数。新 modelDefinition 包含新算子、driver、q2 定义、完整父源身份和可选公开 operator epoch；任何旧目标下降都不算 q2 接受。

实际调用接口为：

`python NEW_DRIVER --scripts FROZEN_SCRIPTS --base-entry FROZEN_BASE --joint-entry FROZEN_JOINT --refined-entry FROZEN_REFINED --background FROZEN_BACKGROUND --area-source NEW_Q2_OPERATOR --prepared ACTUAL_PREPARED --state ACTUAL_OWN_STATE --prefix FRESH_OUTPUT --steps 1 [--operator-epoch NEW_PUBLIC_COMMIT]`。

这只是可执行接口，尚未对实际研究状态调用。它不能通过当前只允许 q1 续算或 release 的包接口伪装成同模型续算；切换须显式建立新数学实现身份。

新算子会同时给每套网格记录最小 $\sigma$ 的真实位置 $s,u$、$E,F/a,G/a^2$、两个归一化 Gram 特征值、经线横向和切向速度、原背景与校正的经线速度，以及 $\sigma<.1,.25$ 的点数、求积权和成本。这些诊断用于区分经线速度压缩与切向近重合，不再只从一个面积最小值猜热点位置。

旧公开 q1 第二态的 $\sigma_{\min}\approx.071688482$ 仅用于公式量级判断：该点 q2/q1 的局部平方成本比约 63.59，目标对 $\sigma$ 的梯度比约 111.24。此处没有原件重算，也没有由它编造新 q2 全场成本。

## 准确文件身份

| 文件 | SHA-256 |
|---|---|
| `6a65-geometry-area-ratio-power-two.py` | `d8fb8710d4957430b66b474d79a61d3b7bf4fff9915bba1d62ecfea0f96ee97e` |
| `6a65-geometry-gap-window-area-power-two-cartesian.py` | `3dcb94971b5975a7046cfcd67bb5d57f60581527b526e8700c8cfc81fd34151f` |
| `6a65-geometry-area-power-two-fixture.py` | `16a257b21219b96dc9727682f48e6496b299d80fe196837c04adf4908bbcaa71` |
| 实际有限核 report | `7b8c44afabb3cad2c5e33bbaf19a9ec12e45d4b95222f29000cb5dde53e18404` |
| 外部 exit receipt | `d86cca453a6f395b01cdb7c373884e48f6ced1882799d24df36d628426802170` |
| 实际 stdout log | `760bbf7eff66df1764d754dc5c9b74753cf45076eac808dd4e565a2e87e8d507` |

按根规矩只提交源码、命令、标量和哈希；可重算的 report/log 不入库。完整研究态还需自己的 baseline、全部 5292 列实际方向核验、真正 normal/LM、后续独立观察和连续几何工作。
