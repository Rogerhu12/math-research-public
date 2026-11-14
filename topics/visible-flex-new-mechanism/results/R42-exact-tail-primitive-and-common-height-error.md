# R42：准确尾原函数、共同高度与评价误差

2026-11-14，mechanism 推导，root 全文复核，repo_sources 独立核对。本文只作解析推导，不修改已冻结的七个运行依赖，不评价真实候选。它说明如何在未来用准确尾公式评价**同一个** R28 重构，并分清当前 FFT 尾误差与整体高度求积误差。

准确物理尾和尾内法弦见 [R40](../results/R40-bent-flat-tail-normal-chord-and-ball-budget.md)。其新有限 ansatz 的局部解析条带限制见 [R41](../results/R41-bent-tail-local-flat-sector-rigidity.md)；下面恒等式不需要连接器已经解出积分性。

## 1. 零均值原函数的准确表达

令

\[
P_0(r,\theta)=
(r\cos\theta,Y(r\sin\theta),-\sigma H(r\sin\theta)),
\quad \bar H(r)=\langle H(r\sin\theta)\rangle,
\]

其中 \(Y,H\) 是固定 S11 模型的准确积分。全角平均的水平分量为零，故

\[
\langle P_0\rangle=-\sigma\bar H(r)e_z.
\]

在开放尾 \(a=r,\ r_t=-1\) 上，\(P_{0,\theta}=rT\)。R28 的 \(\Pi\) 是零均值周期原函数，因此

\[
\boxed{Q_0:=\Pi T
=\left(\cos\theta,\frac{Y(r\sin\theta)}r,
-\sigma\frac{H(r\sin\theta)-\bar H(r)}r\right).}
\tag{1}
\]

这里 \(r\ge r_c>0\)，不存在除半径零的问题。该式是原函数的准确身份，不是另设一个截面中心。它的角导数为 \(T\)，均值为零，这两条也给直接唯一性证明。

令

\[
B(r)=\bar H'(r)=\langle\sin\theta\sin\alpha(r\sin\theta)\rangle,
\]

\[
C(r)=\bar H''(r)=
\langle\sin^2\theta\cos\alpha(r\sin\theta)\alpha'(r\sin\theta)\rangle.
\tag{2}
\]

则 \(\langle V\rangle=\sigma B(r)e_z\)、
\(\langle V_t\rangle=-\sigma C(r)e_z\)。对 \(rQ_0=P_0-\langle P_0\rangle\) 逐次微分，得到

\[
\boxed{Q_1:=\Pi T_t=
\frac{V-\sigma B(r)e_z+Q_0}{r},}
\tag{3}
\]

\[
\boxed{Q_2:=\Pi T_{tt}=
\frac{P_{0,tt}+\sigma C(r)e_z+2Q_1}{r}.}
\tag{4}
\]

因此在准确尾上不必用三次 FFT 来评价 \(\Pi T,\Pi T_t,\Pi T_{tt}\)。公式 (1)–(4) 评价的是同一数学函数；原 FFT 实现仍可作为独立数值比较保留。

## 2. 共同中心积分及唯一帽高

定义全连接器的准确中心为

\[
z_c(t)=\sigma w_c+\int_0^t\langle V_z(u,\cdot)\rangle\,du.
\tag{5}
\]

开放尾开始于 \(t_f\)，其外半径为 \(r_f\)。由 (2) 与 \(r_t=-1\)，

\[
z_c(t)=z_c(t_f)+
\sigma[\bar H(r_f)-\bar H(r(t))],\qquad t\ge t_f.
\tag{6}
\]

于是全尾唯一高度为

\[
\boxed{h=\sigma z_c(t_f)+\bar H(r_f)
=\sigma z_c(L).}
\tag{7}
\]

把 (1)、(6) 代入 \(X=z_c e_z+r\Pi T\)，恰好得到

\[
X=P_\sigma(r,\theta;h).
\tag{8}
\]

这说明一个准确尾 evaluator 可以从**同一个**前缀积分 \(z_c(t_f)\) 与一个标量 \(\bar H(r_f)\) 得到整个尾，不再逐尾圈作径向求积。它不引入新的自由平移，也不要求积分性在连接器内部已为零。

在 \(t_f\) 处，右端标量场的 value/t/tt 及角导数已与准确尾完整匹配。由 (1)–(4)，R28 位置的 0、1、2 jets 与 (8) 匹配；中心的导数同时为 \(\langle V_z\rangle,\langle(V_t)_z\rangle\)。所以从这个准确位置定义切换到显式尾公式，不改变数学上的 C2 接缝。

**有限数值实现的要求不同。** 若一边用未经验证的 FFT/Gauss 近似，另一边用更准确的显式式子，两份浮点表在 \(t_f\) 仍可有小跳差。必须记录这个评价误差，或用同一有区间包围的接缝值统一评价；不能把浮点表的相等当作数学 C2 的证明，也不能强行每圈重平移来掩盖它。

## 3. 参数 Jacobian 必须使用同一个 h

当前 tail、g、\(t_f\)、\(r_f\) 都固定，234 个自由系数只改变连接器内部 field。记其中一项为 \(c_j\)。尾部 field 与这些系数无关，故

\[
\frac{\partial h}{\partial c_j}
=\sigma\int_0^{t_f}
\left\langle\frac{\partial V_z}{\partial c_j}\right\rangle dt,
\qquad
\boxed{\frac{\partial P_\sigma}{\partial c_j}
=\sigma\frac{\partial h}{\partial c_j}e_z.}
\tag{9}
\]

准确尾的 \(X_t,X_\theta,X_{tt},X_{t\theta},X_{\theta\theta}\) 对这些系数的导数都为零：它们只受这个共同竖直平移影响，平移不改变空间 jets。

更具体地，frame 的 \(V_z=-\sin\beta/\sqrt{1+v^2}\) 不含 \(u\)。因此 u 系数的 \(h_j\) 准确为零；v 与 beta 系数分别用

\[
\partial_v V_z=\sin\beta\,v(1+v^2)^{-3/2},\qquad
\partial_\beta V_z=-\cos\beta(1+v^2)^{-1/2}
\]

乘相应固定基函数积分。若未来将尾幅度或 metric 也设为变量，(9) 就需要额外端点和形状导数；当前公式不覆盖那种设计。

在浮点评价中，同一个 h 近似与它的 Jacobian 必须来自同一积分表达式。不能使用前缀公式计算位置，却无记录地用另一个分段求积的 \(z_c(L)\) 导数作为 Jacobian。准确层面两者相同，有限求积层面差异需要保留。

## 4. 当前 FFT 误差为何会集中在 Xtt

令 \(\Pi_N\) 为当前均匀角网格的 FFT 算子，定义

\[
\Delta Q_j=\Pi_N\partial_t^jT-\Pi\partial_t^jT,
\quad j=0,1,2.
\]

另外令 \(\Delta z_c\) 是中心积分误差，\(\Delta m_0\)、\(\Delta m_1\) 是所用角平均相对准确 \(\langle V_z\rangle\)、\(\langle(V_t)_z\rangle\) 的误差。忽略已可独立包围的基本浮点运算误差，准确分解为

\[
\widehat X-X=r\Delta Q_0+\Delta z_c e_z,
\]

\[
\widehat X_t-X_t=-\Delta Q_0+r\Delta Q_1+\Delta m_0e_z,
\]

\[
\boxed{\widehat X_{tt}-X_{tt}
=-2\Delta Q_1+r\Delta Q_2+\Delta m_1e_z.}
\tag{10}
\]

\(T\) 在角阈值处为 C5，\(T_t\) 为 C4，\(T_{tt}\) 为 C3。因此即便位置的有限 FFT 比较已很小，二阶径向 jet 仍可能较慢收敛。人工检查的 192/384/768 三档已显示这种区分；它不证明任一真实候选的连续误差已达标。

角向和混合空间导数目前直接使用准确 frame 链式公式，而非再对采样位置差分。因此 (10) 才是比较数学重构与其数值评价的正确位置；不能把一组采样数值表误认成已经定义了一个全域三角多项式曲面。

一个一般但往往很保守的连续界也可以写出。若零均值周期向量函数 \(f\) 有 p 阶可积弱导数、\(p>1\)，置
\(B_p=(2\pi)^{-1}\int\|f^{(p)}\|\)。则
\(\|\widehat f_k\|\le B_p/|k|^p\)。对偶数 N 的实际 FFT 原函数，均值及 Nyquist 频率在实采样值上不贡献；其余 alias 类给

\[
\|\Pi_Nf-\Pi f\|_{\text{网格最大}}
\le 2B_p\left[
\frac{(N/2-1)^{1-p}}{p-1}
+\frac{(N/2-1)^{-p}}p\right],\qquad N\ge4.
\tag{11}
\]

这是从 alias 系数的三角不等式得到的粗界：对高频 j，其低频 alias 的 \(1/|k|\le1\)，再对尾和作积分估计。它只针对网格评价；要控制全角，仍需区间/导数余项。对于窄 S11 开启，\(B_p\) 可能很大，故 (11) 并不是本方案建议采用的主要 reach 验证手段；显式 (1)–(4) 更直接。

## 5. 当前独立 P 比较消掉了什么，没消掉什么

当前输出取
\(\widehat h=\sigma\widehat z_c(L)\)，再比较原 FFT 评价与 \(P_\sigma(\widehat h)\)。这是正确的尾内评价诊断，但均匀竖直高度误差已被消掉：

\[
P_\sigma(\widehat h)-P_\sigma(h)
=\sigma(\widehat h-h)e_z.
\tag{12}
\]

所以单靠 `position_two_jet_difference_from_single_exact_P_sample` 很小，**不能认证真实帽高、球包含、帽与核心的距离或完整 reach**。未来必须另给 (7) 中前缀积分和 \(\bar H(r_f)\) 的有向区间误差。

同样地，从其他尾圈计算
\(\sigma\widehat z_c(t)+\langle H(r\sin\theta)\rangle_N\)
与 \(\widehat h\) 的差，只能发现尾内平均/积分不一致；它不能发现所有圈共有的前缀积分偏差。

## 6. 可直接用于严证的尾部接口

只需一个有向区间 \([h_-,h_+]\) 包住 (7)，加上固定有理模型身份，即可用显式 P、法向和曲率公式生成整个尾的连续盒子。

计算 \(\bar H,B,C\) 时可用反射对称缩为

\[
\langle f\rangle=\frac2\pi\int_0^{\pi/2}f(\theta)\,d\theta.
\]

对 \(r_c<r\le r_f\)，非零积分只从
\(\theta_0(r)=\arcsin(r_c/r)\) 开始。应在这个真实阈值处分段作有余项或区间包围的积分，不能跨阈值假定全解析。\(r=r_c\) 时三个量准确为零；不要通过含奇异 \(d\theta_0/dr\) 的不稳定边界公式去计算它们，直接用 (2) 的积分即可。

固定当前 \(A_b,w_b\)，R40 给

\[
0\le H\le\Delta_H=27/4000,\quad
|P_{xy}|\le r_f,
\quad\text{尾内法弦半径}\ge768/9625.
\]

若 \(h\ge\Delta_H/2\)，则 \(|h-H|\le h\)，整个帽的球半径最大值恰为

\[
\boxed{\max_{r\le r_f,\theta}|P_\sigma|^2=r_f^2+h^2,}
\tag{13}
\]

上界由水平收缩与高度界得到，等号在 \((r,\theta)=(r_f,0)\) 达到。因而有向包围满足
\(h_-\ge\Delta_H/2\)、\(r_f^2+h_+^2\le R^2\) 时，尾部球预算可直接认证；条带预算 \(|Y|\le r_f<p\) 已无需采样。若 h 跨过该条件，使用
\(r_f^2+\max_{h\in[h_-,h_+],H\in[0,\Delta_H]}(h-H)^2\)
仍是安全上界。

帽内点对已经由 R40 支付。两帽跨对和帽到连接器的点对仍要用 h 区间、全连接器连续盒子及 [R30](../results/R30-closed-surface-normal-chord-reach-certificate.md) 覆盖。准确尾 evaluator 是一个可复用的局部验证组件，不是完整闭面 reach 证书。

## 7. 本轮处理决定

已冻结的 runner 继续保留原 FFT evaluator，并输出准确 P 的独立差、同一 h 的各圈一致性及 tf 接缝审计。本笔记没有修改数值目标、物理模型或源码 SHA。

若后续实际结果值得进一步严证，可以单独加入 (1)–(9) 的准确尾评价器和区间高度接口，同时保留旧 FFT 差以供审计。任何实施都应先做人工位置/全参数 Jacobian 对照，并明确它只是评价同一固定数学对象；不能借此重选 h 或改物理尾。
