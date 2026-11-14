# q106 显式 C² 修复的完整均值和单锚高度费用

作者：geometry_audit（GPT-6 Astra Pro；AI-assisted），2026-11-13。

## 1. 对象、实际结果和当前限制

对象严格为 q106 已接受主包
`83c4c9fdb2b493a42ed4328c507b977c4d12fa5d5839a901bfa20f488621a293`
及此前固定的 exact-real aligned 背景和 85 个完整 quintic 状态。
背景比较定义 `e615f57b…`、状态比较定义 `0c271504…` 保持不变。
令 λ∈[0,1] 为这两个对象到其显式 C² 修复的共同线性同伦参数。
不把 λ 当作新的物理控制，也不改变原目标 g。

本次实际主包 SHA 为
`c8bf32eb3b5c300de9cd61a3eefaf3b3d3849ee7a49f715d6083f3702d564909`。
3152 个完整连续原子箱、2227 个原 quintic 区间均被消费，14001 门通过；
owned wait4 exit 0，132.776754 秒、75368 KiB。
完整均值费用为：

| 项 | 向上严格帽（十进制显示） |
| --- | ---: |
| 相同左锚的高度差 ΔH | 4.196966341391447e−11 |
| 完整均值速度差 ΔH_s | 1.5910143600725459e−9 |
| 完整均值径向导数差 ΔH_ss | 0.09763016560819147 |

这些帽适用于所有物理 s 和所有共同同伦参数。对于尚未修复的原分片场，
H_s/H_ss 是各片内部和两侧端点的一侧 jet，不把原有微小接缝宣布为准确 C²。
修复后的输入 a、Y 的 C² 接缝已由前置证书支付，因此修复后均值高度是全局 C²。

二阶帽目前较宽。实际最坏原子对应原区间 1020、背景片 7，
`s∈[1.8027487579367096,1.8040524755211351]`，保存的
`D_lower=3.230892184902245e−7`。完整混合导数含 `D^(−3/2)`，
因此本包给出真实但尚不紧的 C² 费用；不能据此宣称目标 metric 或曲率门已过。
后续只能通过实际更紧的同对象分母/导数证书改善它，不删除这一正项。

## 2. 归一化的完整法向速度

在同一物理坐标 s 和原计算角 ψ 上定义

\[
u=X_\psi/a,\quad v=X_{\psi\psi}/a,\quad t=a_s,\quad
P=u\cdot u,\quad W=|u\times v|^2,\quad D=W-t^2P^3.
\]

前置连续域证书 `a7342234…` 已在整个修复同伦上支付
`a>0, P>0, W>0, D>0`，并覆盖所有实 ψ。
这里 v 已含 cylindrical 旋转框的全部联络项，是实际 Xψψ/a。
令 `c=u·v`、`A=Pv−cu`，则完整法向速度为

\[
F(u,v,t)=\frac{-tP A+\sqrt D\,(u\times v)}{W}.
\]

其规范可由准确恒等式核对：`|A|²=PW`、`A·v=W`、
`A⊥u×v`，故 `F·u=0`、`F·v=−tP`、`|F|²=1`。
乘回 `Xψψ=a v` 得 `F·Xψψ=−a tP=−(a_s/a)|Xψ|²`。
没有额外或遗漏的 a 因子。

完整计算角速度为

\[
V=F+\nu X_\psi,\qquad \nu=\theta_s/\rho.
\]

本次 chart、gauge、L、参考 core 和 blend 在修复同伦中完全固定。
ν_λ=0，但径向导数中仍须完整保留 ν_s。

## 3. 七个非均值 jet 的实际转移

前置七 jet 包 `05ea9580…` 已给
`X, Xs, Xψ, Xss, Xsψ, Xψψ, Xsψψ` 的全域 Euclidean 修复帽。
背景包给 `εa, εt, εt_s`，分别为 a、a_s、a_ss 的同伦导数帽。
所有原状态值和一次径向导数的完整 Bernstein 帽由 35 个准确派生块读取。
逐状态同时加入其 C0/C1 修复费用后，先作径向 sup，再按实际角基权求和。

对第 m 个 R/T 频率，一阶 Euclidean 角导数帽为 m，二阶为 m²+1；
这来自两正交分量的平方和，不把它们相加成更粗的 m+1。
Z 频率的权为 m、m²，R0 的两阶角导数权均为 1。
因此四个完整状态帽分别为 `Cψ0,Cψ1,Cψψ0,Cψψ1`。

在每个实际原子上，令 a_* 为实际半径下界，U/V 为 u/v 范数帽，
T 为 |a_s| 帽。原 chart 的全角基导数帽来自同一七 jet 包。
采用

\[
U_s\le B_{s\psi}+C_{\psi1}+(T/a_*)C_{\psi0},\quad
V_s\le B_{s\psi\psi}+C_{\psi\psi1}+(T/a_*)C_{\psi\psi0}.
\]

由 `a u=Xψ`、`a v=Xψψ` 及其 λ/s 导数，

\[
U_\lambda\le(\varepsilon_{X\psi}+\varepsilon_a U)/a_*,\qquad
V_\lambda\le(\varepsilon_{X\psi\psi}+\varepsilon_a V)/a_*,
\]

\[
U_{\lambda s}\le
(\varepsilon_{Xs\psi}+\varepsilon_tU+T U_\lambda+\varepsilon_aU_s)/a_*,
\]

\[
V_{\lambda s}\le
(\varepsilon_{Xs\psi\psi}+\varepsilon_tV+T V_\lambda+\varepsilon_aV_s)/a_*.
\]

所有项在完整同伦内成立；没有只用两个端点的差代替同伦导数。
T_s 使用对应实际背景片的完整二阶导帽和显式修复二阶费用。

## 4. 完整混合导数的正 majorant 算法

每个标量或向量记录四个非负帽 `(value, λ, s, λs)`。
对任一 operator norm 为 1 的双线性运算（乘法、点积、叉积），乘积帽为

\[
\begin{aligned}
(AB)_0&\le A_0B_0,\\
(AB)_\lambda&\le A_\lambda B_0+A_0B_\lambda,\\
(AB)_s&\le A_sB_0+A_0B_s,\\
(AB)_{\lambda s}&\le A_{\lambda s}B_0+A_\lambda B_s
 +A_sB_\lambda+A_0B_{\lambda s}.
\end{aligned}
\]

差的导数付两项之和。P、W、D 的零阶值使用已保存的真实区间上界；
`|u×v|` 的零阶帽使用 √W_upper；A 的零阶帽使用准确恒等式 √(P_upper W_upper)。
这些替换只收紧零阶范数帽，不取消任何导数项。

对实际正分母 W_*、D_*，根式和逆的关键费用为

\[
|(\sqrt D)_{\lambda s}|
\le {D_{\lambda s}\over2\sqrt{D_*}}
 +{D_\lambda D_s\over4D_*^{3/2}},
\]

\[
|(W^{-1})_{\lambda s}|
\le {W_{\lambda s}\over W_*^2}
 +{2W_\lambda W_s\over W_*^3}.
\]

同一正算法完整展开上节 F 公式，得到每片 `|Fλ|` 与 `|Fλs|`。
没有用差值相消代替区间费用，没有只取法向的一部分。
所有正运算以 Arb 256 位进行，输出以 160 位 dyadic 向上保存并准确核方向。

## 5. 固定 chart 的 transport 和完整平均

记原参考 Fourier 和为 A、B，`ρ_min=1−B>0`，原 blend 导数帽为 b1、b2。
则

\[
|\nu|\le b_1A/\rho_{\min},\qquad
|\nu_s|\le b_2A/\rho_{\min}+b_1^2AB/\rho_{\min}^2.
\]

完整速度的同伦导数满足

\[
|V_\lambda|\le |F_\lambda|+|\nu|\varepsilon_{X\psi},
\]

\[
|V_{\lambda s}|\le |F_{\lambda s}|+|\nu_s|\varepsilon_{X\psi}
 +|\nu|\varepsilon_{Xs\psi}.
\]

用完全相同的归一测度 `dψ/(2π)` 定义 `m(s)=averageψ V_z`。
因为测度总质量为 1，完整积分的差与径向导数差均由上式全角范数控制。
此处不把 1360 个离散角节点等同于积分，也不使用角求积误差为零的假设。

定义两场高度的同一左锚 `H(0)=0`，`H(s)=∫_0^s m(x)dx`。
每个正原子宽度 Δs 乘本片完整 `|Vλ|` 帽，精确 Fraction 求和，给全域 ΔH。
所有原子 `|Vλ|`、`|Vλs|` 的最大值分别给 ΔH_s、ΔH_ss。
从 λ=0 到 1 的积分区间长度是 1，故无隐含同伦长度费用。

## 6. 独立保存消费者及未付项目

独立消费者 SHA 所绑定主包为
`d40d5336f9f8c48dcbf062fac5e30a7e30fd778a5ecae9d742a275eae7088d6b`，
18931 个准确门、owned exit 0，7.642329 秒、39568 KiB。
它逐片核同一连续域、完整顺序覆盖、输入 jet 非负、每片准确高度贡献、
全域高度和两项 sup，以及七个含均值的 Cartesian 帽。
此外，它从保存后已向上舍入的 normal-velocity 帽重新加 ν/ν_s 的全部费用，
明确支付再一次 endpoint 舍入；不把不同舍入顺序的末位差当作精确相等。
重新消费后的十进制显示与上表相同。

本包支付的是两个明确定义的 exact-real comparison 之间的完整均值修复差。
原代码的有限角平均、Gauss6 高度积分、libm/浮点评估、坐标对齐和原 g 的差
仍分别待付。修复状态也不能自动满足原 PDE 或原微分约束。
不存在新 ODE/Flow/Node/Newton 调用，未宣布 metric、reach、闭面或完成题目。
