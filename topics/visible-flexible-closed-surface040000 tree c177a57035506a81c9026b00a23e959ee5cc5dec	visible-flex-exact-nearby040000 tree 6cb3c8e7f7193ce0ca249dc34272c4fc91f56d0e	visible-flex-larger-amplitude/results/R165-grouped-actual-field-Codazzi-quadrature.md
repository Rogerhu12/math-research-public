# R165：完整实际字段的同点 Codazzi 求积、准确端点和局部 Jacobian

**状态：代数构造与证明完成；一个实际非零局部 JVP 已运行通过。**
这是对现有有限 Codazzi 目标的明确修改，不是完整强曲面解、准确积分
或连续残差证书。旧 [R152](R152-hybrid-known-lifting-Codazzi-quadrature.md)
已正确说明其混合求积定义；本结果不撤回该证明。

相关定义来自 [R146](R146-exact-lifting-endpoint-Codazzi-quadrature.md)、
[R149](R149-frozen-ruling-atlas-with-full-functional-traces.md)、
[R153](R153-positive-n-local-Gauss-parameterization.md)、
[R155](R155-positive-II-branch-from-nonnegative-flat-tail.md)。
本结果解释如何在改变有限径向求积时保留它们的完整实际场、端点、
零方向和 [R159](R159-local-normal-equations-with-exact-field-elimination.md)
的两节点局部结构。

## 1. 问题与当前真实证据

当前场在原共享 P1 节点上保存独立 raw 系数，另加完整已知 lifting。
R153 在冻结 coast 窗内把实际第二基本形式的 $l$ 分量改为

\[
 l=(1-w)l_0+wA,\qquad A=\frac{K+m^2}{n},\qquad l_0=y_l+L_l.
\]

旧有限目标在 G2 点计算 raw correction 及非线性增量
$\Delta l=w(A-l_0)$，对已知 affine lifting 单独使用 R152 的分片 G8。
这个定义本身明确且可微，但 G2 与 G8 的分项差不能忽略。

实际闭输入 23b3 的四格诊断见
`notes/2026-11-12-fd2d-metric-coast-delta-quadrature23b3.md`。
仅把 $\Delta l$ 从 G2 改为分窗 G8，cell64/73 第二条方程的样本均值
变化达 `3.389014627085828` / `2.990300689333253`，而旧完整单元峰
只有 `.4601519584595064` / `.6574084859959741`。

不能据此把“只换 Δ”称作准确积分：平台上的 $+y_l$ 与 Δ 中的
$-wy_l$，以及 $+L_l$ 与 $-wL_l$，必须在同一实际点相消。以下直接
对完整实际场求积，避免把不同代表的分项分别近似后丢失这些恒等式。

## 2. 定义：完整端点减完整物理 PDE 的有限平均

固定物理材料度量与计算图

\[
 g=ds^2+a(s,p)^2du^2,\qquad u=U(s,\xi),\qquad U_\xi>0,
\]

其中 $U$ 按 R149 冻结，不随本轮物理 profile、tail 或 raw 参数改变。
记

\[
 c=\frac{a_s}{a},\qquad v=\frac1{aU_\xi},\qquad b=\frac{U_s}{U_\xi}.
\]

对**已经施加全部实际表示变换**的 $f=(n,m,l)$ 定义

\[
 \begin{aligned}
 F_n(f,p)&=v m_\xi+c(l-n)+b n_\xi,\\
 F_m(f,p)&=v l_\xi-2cm+b m_\xi.
 \end{aligned}                                                   \tag{1}
\]

这正是固定 $\xi$ 下的两条 Codazzi 右端。特别是 $b$ 项完整保留；
本结果没有把 moving atlas 当成固定材料图。

在原 P1 单元 $I_i=[s_i,s_{i+1}]$、$h_i=s_{i+1}-s_i$ 上，取有限节点
$s_{ij}\in I_i$ 和平均权重 $\omega_{ij}$，满足

\[
 \sum_j\omega_{ij}=1.
\]

这些节点、权重与原 cell 内部的分片位置都由冻结输入确定，不依赖
本轮未知量。定义新有限残差

\[
 \boxed{\displaystyle
 C_i(\xi)=\frac{(n,m)(s_{i+1},\xi)-(n,m)(s_i,\xi)}{h_i}
       -\sum_j\omega_{ij}\,(F_n,F_m)(s_{ij},\xi).}                 \tag{2}
\]

式 (2) 的端点是完整实际函数，不是截断后另造的边界迹。若 $n,m$
在每个积分片绝对连续，微积分基本定理给出它与准确积分残差之间
仅有 PDE 右端的求积差；若尚未支付该正则性或求积余项，式 (2)
仍是明确的有限搜索目标，不因此升级为连续证书。

### 当前可执行范围

新消费者只在与冻结 coast 支持相交的原单元上应用 (2)。窗口外
调用原 R155 完整消费者，保留其原有限目标和准确非线性端点增量。
当前 coast 与 terminal 窗不相交。coast 内 R153 不改变 $n,m$，故
式 (2) 的端点就是原完整 affine lifting 加 raw P1 的 $n,m$ 迹。

片界取原明确物理 profile/bump 支持、turn 内部片界、seed/tail 窗、
冻结 atlas 片界及 coast 窗边界的并集，并加入保存的准确浮点
`gauss_plateau` 端点。每片默认 G8；子片权重乘其长度占原 cell
长度的比例。相差极少 ulp 的真实小片不被删除，沿冻结 R152
`quadrature_on_parts` 的显式窄片规则保留完整权重。

该选择是有限求积定义，不宣称全部节点构成已认证的准确 Gauss
积分，也不付无限角或径向余项。

## 3. 同点相消与表示不变性

### 命题 1

若两组有限参数在所有端点和求积点给出相同的完整实际
$n,m,l,n_\xi,m_\xi,l_\xi$，且给出相同 $a,c,U$，则式 (2) 完全相同。
若一条可微参数方向使这些实际值与角导数的一阶变化全部为零，
其有限残差 Jacobian 作用也为零。

**证明。** 两端点项及有限和的每一项都只使用上述实际函数。
逐项相等给出第一结论；逐项对有限和求导给出第二结论。这里没有
假设求积误差很小，也不需要先解出 Codazzi。证毕。

### R153 raw-l 零方向

设某 raw $l$ 帽函数的完整径向支持都在 $w=1$ 平台中，改变它只会
改变 $l_0$，不改变 $n,m,K$。由

\[
 l=(1-w)l_0+wA,\qquad
 l_\xi=(1-w)(l_0)_\xi+wA_\xi
\]

知实际值和角导数在其支持内与该 raw 帽无关；支持外帽为零。
$n,m$ 端点从未改变。因此式 (2) 和完整 Jacobian 对该列均为零。
这说明原 R153 “完整帽支持在平台内才删除”的消元条件继续有效。
它没有把仅在一个节点 $w=1$ 的邻接帽错误删除。

同一恒等式也消去已知 $L_l$ 中的平台分项。新规则先构造
$(1-w)(y_l+L_l)+wA$，不分别对 $L_l$ 和 $-wL_l$ 使用不一致的节点。

### R155 raw-trace 零方向与当前窗外分支

R155 平台的记号为

\[
 d=n_0-l_0,\quad H=\sqrt{d^2+4m^2+4K},\quad
 E=\frac{H-n_0-l_0}{2},\quad
 n=n_0+E,\quad l=l_0+E.
\]

对完整支持在该平台内的共同 trace 方向
$\delta n_0=\delta l_0=\varphi,\delta m=\delta K=0$，有
$\delta d=\delta H=0$、$\delta E=-\varphi$。故完整实际
$\delta n=\delta l=0$，角导数亦为零。完整端点项包含同一抵消，
因此任何式 (2) 的共同点有限规则都保留这个零方向。

当前实现的 terminal 部分直接调用原冻结消费者。该消费者在同一
G2 点组合原 PDE 与 E 的完整增量，并准确组合 n 的端点增量；上面
的逐点/端点抵消同样成立。R152 的已知 affine 修正与 raw trace
方向无关。因此本次仅改 coast 目标仍保留原 terminal gauge。
当前自由 trace 列采用 $J_n-J_l$、方向 $\delta l=-\delta n$；它保留
可见的 $d$ 方向，而删除的是共同 trace，不应混淆这两者。

准确 cut 的值/角/参数 bypass 沿 R155/R156 原合同。这里没有推出
$E_s=0$，也没有新增对 cut 径向 II jet 的零值承诺。

## 4. 完整状态与参数微分

以下在原表示的可微域内逐点成立；R153 的商只在其实际正 n 窗中
求值。令

\[
 A=\frac{K+m^2}{n},\qquad
 B=A_\xi=\frac{2m m_\xi-A n_\xi}{n}.
\]

由于 $K$ 仅依赖物理 $s$，在固定 $s$ 的角导数中 $K_\xi=0$。
任意参数/状态方向记作 $\delta$，则

\[
 \delta A=\frac{\delta K+2m\delta m-A\delta n}{n},
\]

\[
\begin{aligned}
 \delta B={}&\left(-\frac{B}{n}+\frac{A n_\xi}{n^2}\right)\delta n
 +\left(\frac{2m_\xi}{n}-\frac{2m n_\xi}{n^2}\right)\delta m
 -\frac{n_\xi}{n^2}\delta K\\
 &-\frac{A}{n}\delta n_\xi+\frac{2m}{n}\delta m_\xi.
\end{aligned}                                                     \tag{3}
\]

因为窗口在本轮固定，

\[
 \delta l=(1-w)\delta l_0+w\delta A,\qquad
 \delta l_\xi=(1-w)\delta(l_0)_\xi+w\delta B.                      \tag{4}
\]

这是冻结 `positive_gauss_l_delta`、`gauss_delta_direction` 和
`gauss_delta_state_columns` 的同一完整商法则。状态列中
$\delta K=\delta a=\delta c=0$；物理 profile 列中全部保留。

冻结 atlas 给出 $\delta b=0$，且

\[
 \delta v=-v\frac{\delta a}{a}.
\]

因此完整 PDE 列为

\[
\begin{aligned}
 \delta F_n={}&\delta v\,m_\xi+v\,\delta m_\xi
 +\delta c(l-n)+c(\delta l-\delta n)+b\,\delta n_\xi,\\
 \delta F_m={}&\delta v\,l_\xi+v\,\delta l_\xi
 -2\delta c\,m-2c\,\delta m+b\,\delta m_\xi.
\end{aligned}                                                     \tag{5}
\]

式 (3)–(5) 包含 tail/profile 的完整 lifting 值与角参数导数、
$a_p,c_p,K_p$。它没有把当前非零 $\delta$ 物理度量当成冻结参考度量。
参考函数本身虽冻结，当前 target/profile 的变化仍必须进入式 (5)。

在 $s_{ij}=s_i+\tau_{ij}h_i$，原 raw P1 的状态变化为

\[
 \delta y(s_{ij})=(1-\tau_{ij})\delta y_i+\tau_{ij}\delta y_{i+1}.
\]

节点和权重与参数无关，故

\[
 DC_i=\frac{\delta(n,m)_{i+1}-\delta(n,m)_i}{h_i}
          -\sum_j\omega_{ij}\,\delta(F_n,F_m)_{ij}.                \tag{6}
\]

这同时证明了完整状态、tail 和物理 profile Jacobian。端点 lifting
参数列来自同一原函数的准确已暴露参数导数；不能用旧 G2 状态列与
新 fine 参数列拼成一个并非任何同一残差导数的矩阵。

本式只需要当前 $a,a_s,K$、角一阶 jet 和它们已给定的参数导数。
它不要求新增空间 $C^3$ 门，不需要为本目标求 $K_s$，不要求径向
二阶 II 导数。

## 5. 角行、同一有限目标与舍入范围

原 retained 投影与 [R142](R142-D2-isometric-high-angular-row-compression.md)
高模行是固定线性映射，故它们与有限和、式 (6) 求导交换。n/l 偶、
m 奇及半周周期仍由原完整场的分析定义保持；没有把任意样本拟合
为 D2 对称场。

实现对高模行先去掉解析上属于 retained 空间的 raw 项，再投影，
减少大 retained 分项在高模坐标中的浮点污染。例如从第一条 PDE
去掉

\[
 a^{-1}(y_m)_\xi+c((1-w)y_l-y_n),
\]

第二条去掉

\[
 a^{-1}(1-w)(y_l)_\xi-2cy_m.
\]

这些式子在一个径向点的系数不依赖角，因此确实属于原 retained
空间。状态与参数列分别减去同一式子的相应导数。完整点值残差
同时独立保留，不把小高模行当成完整点值。

上述等价性是在准确有限线性代数中证明的。可执行求值使用
binary64；局部核验中“retained 对完整点值再投影”差
`3.90655389981287e-14`，“retained 重构加 omitted 对完整点值”差
`7.435718707426986e-14`。这些是本次实际观察，不是所有未来输入的
舍入上界，更不是连续证书。

## 6. 任意有限细求积仍只有两端点局部性

### 命题 2

无论一个原 P1 cell 被分成多少个求积子片、每片使用多少个固定
内部点，其残差与 Jacobian 只依赖原 $y_i,y_{i+1}$ 和共享参数 $p$。
应用原准确 central/cut/coast/terminal 消元后，R159 的 field-field
normal 矩阵仍为块三对角。

**证明。** 每个内部点的 raw 状态只含上述 P1 两端点；完整 lifting、
target 和 frozen atlas 只依赖共享参数或冻结输入。式 (2) 的端点也
只含同两节点。式 (6) 因而只有这两个 node block 与共享参数列。
求积细分不产生新的未知节点。

原 central 映射、coast l 删除及 terminal trace 配对都是每个节点
自身的线性映射，并可能把 central 列并入共享 p；它们没有把一个
node 的自由 field 系数扩展到远处 node。于是单行的 field 支持仍
至多是相邻两个 block。对每行取外积并累加，两个不相邻 block
之间的项恒零。这正是 R159 的块三对角结论。证毕。

因此现有流式 normal 累积可以逐 cell 消费新的 retained/high 局部
矩阵，不必存整张 tall Jacobian。目标确实改变，但数据依赖与存储
结构没有因提高求积阶数而变成全径向耦合。

## 7. 可执行接口与诊断网格合同

新冻结源：

```text
scripts/fd2d_gc_grouped_coast_codazzi.py
21332 bytes
SHA256 a0a8b934a600871bc3743c2d85c61b60f21005ef9c782499fa1e0cb064a5b4e2
```

入口：

```python
gauss_cell_positive_trace_grouped_coast(
    problem, vector,
    order=2, high_weight=1., jacobian=True,
    fine_order=8, point_batch=2,
)
```

它沿用当前 cell consumer 的 retained/high residual、CSC Jacobian、
完整点值/omitted 单元数组以及全局列布局。K31/raw 与 tail16、七个
profile 参数的切片直接读取 problem 的显式布局，没有用 K+1 猜 tail。

全部 coast cell 的 PDE 直接同点使用完整 actual R153 字段。
窗外调用冻结 `fd2d_gc_gauss_cell_frozen_operator_compatible.py` 桥，
桥调用原完整 R155 消费器；旧 strict 身份检查与旧数学源均不修改。
若一个输入 block 横跨 coast 边界，则仅按实际 cell 边界分成连续
子块，随后按原列映射拼回。共享参数列仍全局同一组。

原下游把 `point_gauss` 按每 cell 两点拼接。因此该键继续保存**原
G2 点的 actual Gauss**，`quadrature_points` 同样保留原 G2 顺序。
细求积点的 Gauss 最大值、位置、active n 最小样本以及准确节点/
权重放在 `info.grouped_coast_rules` 与独立的
`fine_sampled_interior_Gauss_maximum` 中。不能把 fine 点填进旧 G2
数组却继续使用其旧 shape/含义。

新规则不再为了报告一个分拆量而单独重积分 affine known lifting，
所以不输出一个伪造的 `known_lifting_change_maximum`。接入者应记录
新规则身份和 fine 观测，而不是沿用旧分项变化统计。

## 8. 实际局部 JVP、首个零方向 fixture 与限制

输入仍是 23b3：

```text
notes/2026-11-12-fd2d-raw-bump-reuse23-b0003-accepted-0001.npz
SHA256 a485ca86233a196223f16fc2f9c01b7cf3592ae5499d9a04fd94bd7f2511e81e
```

首个检查选择 cell64，要求 state/tail/profile 三组均有非零作用。
真实运行 `49076 / 472419 → 28f536` 退出 1，停在有限差分之前：
该 cell 的 tail 方向实际为零。原因是 tail 径向 lifting 起点
$0.42\,s_\mathrm{cut}$ 已位于左平台起点之后；在 tail 窗尚未打开处
它为零，在后续部分 frozen-reference 窗已为 1，故该段完整场确实
独立于 tail。这是一个不满足预定“非零方向”范围的 fixture，不能
冒称它验证了 tail Jacobian。失败源、report、receipt 与 console
全部保留，consumer 源没有因此改动。

另名检查 v2 改为真实出口 rim 的 cell73：

\[
 [0.8281800958020702,\;0.8478617704522428],
\]

在保存的平台端 `0.8344782316901254` 分为两片，各 G8。一次局部
Jacobian 后分别计算 state、独立 tail、物理 profile 方向的真实
作用范数，原值分别为

```text
37.31655783865025
0.03452616091003696
68.84377612687057
```

将三组各归一到作用范数 1 后相加，只对这个平衡后的非零方向做
一次中心差分，步长 `1e-6`。结果：

| 项目 | 实际结果 |
|---|---:|
| JVP 相对 L2 差 | `7.557115175724136e-9` |
| JVP 相对最大差 | `1.1045826177143869e-8` |
| JVP 绝对最大差 | `1.0640146097529168e-8` |
| fine active n 最小样本 | `0.4828180383693811` |
| 原 G2 Gauss 最大样本 | `1.5512068652407343` |
| fine Gauss 最大样本 | `1.5933554179561287` |

实际 session `16713 / 831eb6 → 097749` 退出 **0**；内部
`17.128621807001764 s`，wrapper `28.247039226000197 s`，
峰 RSS `94024 KiB`。原输入字节及 report 绑定源均未变。

完整成组规则在这个同一未收敛场上的 Codazzi 样本峰为

```text
(n, m) = (0.5083213016780026, 3.664825908821722)
```

旧规则为 `(.49740039950587184,.6574084859959741)`；只换 Δ 的反事实
为 `(.508306795106648,3.6477091753292274)`。所以保护同点相消后，
明显的有限求积敏感性仍然存在。**本结果不把新残差说成已经改善，
不把该局部 JVP 说成完整候选通过，也不把 G8 当成真积分。**

成功 report 为
`notes/2026-11-12-fd2d-metric-grouped-coast-local-02-report.json`，
SHA256 `b91afffa2636fc0704b4fa4f56bb52c937c9069e768efcebc5431aa02de909af`。
实际 witness 为同 stem 的 `-witnesses.npz`，41857 B，SHA256
`ec139a8e7ebae7c28efdfbf8e1144553e36f995d2186bb8a2ca1e3aaa7b440fe`。

## 9. 闭存与剩余数学工作

本结果的 consumer、两版检查源、失败/成功执行记录、成功 witness
及本完整证明由
`notes/2026-11-12-fd2d-metric-grouped-coast-R165-closed-manifest-01.json`
统一绑定。公共 results 索引由 root 维护。

本结果交付的是一致的新有限目标及其完整局部导数。继续求解应明确
记录此目标改变；连续角域、径向求积余项、完整 Gauss/Codazzi 及实际
闭曲面的几何条件仍需由它们自己的实际消费者支付。本结果没有为
那些尚未支付的结论新增形式审核门，也没有用一个局部实现检查代替
它们。
