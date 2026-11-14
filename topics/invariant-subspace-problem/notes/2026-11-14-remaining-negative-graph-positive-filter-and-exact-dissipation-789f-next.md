# 保持原联合余负图的正滤波与无误差总耗散

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明的中间结论。** 在[全源正 gap 滤波](2026-11-14-physical-gap-all-source-positive-filter-and-paid-negative-range-789f-next.md)及其[统一幂预算](2026-11-14-physical-gap-uniform-powers-and-high-spectrum-source-filter-789f-next.md)基础上，本稿构造一个真正 \(L\) 正收缩 \(\mathcal J\)。它的整个像位于原联合余负图 \(\mathscr R_{\rm rem}\)，而非先滤波再作一个未付费用的任意投影。其完整耗散式没有加性 \(\delta I\) 余项：
\[
\boxed{J M J\preceq 2J(I-J).}
\]
这里 \(J,M\) 是 \(L\) 单位坐标中的滤波与两费用矩阵。原联合旗常数 \(\delta_m\) 只在其已证明的旧合法窗口使用；新母窗口 \(e^{16d^3}\) 不自动扩大本稿原旗应用范围。

## 1. 实际源、两种伴随与原窗口

在一组固定原参数的完整源空间中，沿用
\[
\mu(r)^2=\langle Lr,r\rangle,\qquad
\Xi(r)^2=\langle\mathfrak M r,r\rangle,\qquad
\mathfrak M=B+LGL,
\]
其中 \(L,B,G\) 有界严格正，且 \(B\preceq G^{-1}\)。原正滤波为
\[
\mathcal E=(L+B)^{-1}L-(L+G^{-1})^{-1}L.
\]
它在 \(L\) 内积中为正收缩，其像位于原真实首头负图
\[
\mathscr N=\ker[P_0(L+B)]=\operatorname{Ran}T_{q+1}.
\]
实际上其像还满足全部 \(\ker(G^{-1}-B)\) 方向的共同费用负图；本稿只需 \(\operatorname{Ran}\mathcal E\subset\mathscr N\)。

取已付闭子空间
\[
\mathscr Z=\mathscr N\cap\mathscr X,
\]
并令
\[
\mathcal P=P_{\mathscr Z}^{\mathfrak M},\qquad
\mathcal Q=I-\mathcal P.
\]
这是原两费用内积中的正交投影，通常不是 \(L\) 正交投影。已付联合旗给
\[
\boxed{\mu(\mathcal Pv)\le
\delta\,\Xi(\mathcal Pv)\le\delta\,\Xi(v)
\quad\text{对全部源 }v.}
\tag{1.1}
\]
\(\mathcal P\) 的像属于 \(\mathscr N\)，故 \(\mathcal Q\) 将 \(\mathscr N\) 映入
\[
\mathscr R_{\rm rem}
=\mathscr N\cap\mathscr Z^{\perp_{\mathfrak M}}.
\]

具体原应用引用
[真正负源图与联合旗](../results/R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md) §§3–4：
\[
m\ge8,\quad d=2^m,\quad
4d\le q\le e^{d^3/4},\qquad
\delta=\delta_m\le\sqrt2e^{-d^4/20}.
\tag{1.2}
\]
以下抽象证明仅要求 \(0\le\delta\le1/2\)，因此覆盖 (1.2)。
若要在更大 \(q\) 窗使用这个具体 \(\mathscr Z\)，必须另行支付 (1.1)；母窗的有限核 lift 常数不替代该证明。

下文 \(\mathcal Q^{\dagger_L}\) 始终表示 \(L\) 伴随：
\[
\mathcal Q^{\dagger_L}=L^{-1}\mathcal Q^*L.
\]
不能把它换成物理伴随 \(\mathcal Q^*\)，也不能因 \(\mathcal Q\) 是两费用投影就把它换成 \(\mathcal Q\)。

## 2. \(L\) 单位坐标及已付耗散

为不混淆内积，统一定义
\[
E=L^{1/2}\mathcal EL^{-1/2},\qquad
M=L^{-1/2}\mathfrak M L^{-1/2},
\]
\[
P=L^{1/2}\mathcal PL^{-1/2},\qquad Q=I-P.
\]
本节以后普通 \(^{*}\) 正是这个单位坐标中的 Hilbert 伴随。已有
\[
0\preceq E\preceq I,\qquad
I-E\preceq M,\qquad
\boxed{EME\preceq2E(I-E).}
\tag{2.1}
\]
\(P\) 是 \(M\) 正交投影，故
\[
Q^*MQ\preceq M,\qquad
\|Pv\|\le\delta\|M^{1/2}v\|.
\tag{2.2}
\]

由 (2.1)，
\[
\|PEv\|^2\le
\delta^2\langle EMEv,v\rangle
\le2\delta^2\langle E(I-E)v,v\rangle.
\tag{2.3}
\]
特别 \(\|PE\|\le\delta/\sqrt2\)。
此外 (2.1) 在 \(E\) 的支撑上作平方根合同，或先以
\((E+\varepsilon I)^{-1/2}\) 合同再令 \(\varepsilon\downarrow0\)，给
\[
E^{1/2}ME^{1/2}\preceq2(I-E).
\]
因此
\[
\boxed{\|PE^{1/2}\|\le\sqrt2\delta,\qquad
\|PEP^*\|\le2\delta^2.}
\tag{2.4}
\]
该论证不要求 \(E\) 有闭值域，也没有对其零谱作有界逆假设。

## 3. 正化后仍在原余负图

置
\[
F=QEQ^*,\qquad c=1+2\delta,\qquad
J=\frac{F}{c},
\]
并回到实际源写
\[
\boxed{
\mathcal J
=\frac{\mathcal Q\mathcal E\mathcal Q^{\dagger_L}}{1+2\delta}.}
\tag{3.1}
\]
显然 \(F\succeq0\)。\(\mathcal E\mathcal Q^{\dagger_L}\) 的像属于 \(\mathscr N\)，再施加 \(\mathcal Q\) 因而给
\[
\boxed{\operatorname{Ran}\mathcal J\subset\mathscr R_{\rm rem}.}
\tag{3.2}
\]
下文证明 \(J\preceq I\)，而不是从 \(\mathcal Q\) 的 \(L\) 范数无证得出。

定义真实正算子
\[
D_Q=QE(I-E)Q^*\succeq0.
\]
由 (2.1)–(2.2)，
\[
\boxed{
FMF
=QE(Q^*MQ)EQ^*
\preceq QEMEQ^*
\preceq2D_Q.}
\tag{3.3}
\]

对任意 \(w\)，令 \(v=Q^*w\)，并记
\[
a=\|Ev\|,\qquad
D=\langle E(I-E)v,v\rangle.
\]
于是
\[
\langle Fw,w\rangle=a^2+D,\qquad Fw=QEv.
\]
(2.3) 给
\[
\|PEv\|\le\sqrt2\delta\sqrt D,
\]
故
\[
\|Fw\|^2
\le a^2+2\sqrt2\delta\,a\sqrt D+2\delta^2D.
\]
因此
\[
\begin{aligned}
c\langle Fw,w\rangle-\|Fw\|^2
&\ge2\delta a^2
 +(1+2\delta-2\delta^2)D
 -2\sqrt2\delta\,a\sqrt D\\
&\ge(1+\delta-2\delta^2)D\\
&\ge D.
\end{aligned}
\tag{3.4}
\]
中间准确使用
\(2\sqrt2\delta\,a\sqrt D\le2\delta a^2+\delta D\)；
最后使用 \(0\le\delta\le1/2\)。

对全部 \(w\) 成立，故
\[
\boxed{D_Q\preceq cF-F^2.}
\tag{3.5}
\]
特别 \(F^2\preceq cF\)，而 \(F\succeq0\)，所以 \(0\preceq F\preceq cI\)。结合 (3.3)，得到
\[
\boxed{0\preceq J\preceq I,\qquad
JMJ\preceq2J(I-J).}
\tag{3.6}
\]
耗散式本身没有 \(\delta I\) 加性损失。

## 4. 初始近似所需的真实 \(\delta\) 代价

由 \(F=E-PE-EP^*+PEP^*\) 及 (2.3)–(2.4)，
\[
\|F-E\|\le\sqrt2\delta+2\delta^2.
\]
记
\[
\beta_\delta=(2+\sqrt2)\delta.
\]
准确有
\[
I-J\preceq
\frac{I-E}{c}
+\frac{(2+\sqrt2)\delta+2\delta^2}{c}I
\preceq M+\beta_\delta I,
\]
以及
\[
\boxed{
\|J-E\|\le\beta_\delta,\qquad
I-J\preceq M+\beta_\delta I.}
\tag{4.1}
\]
这里保留的是从原 \(\mathcal E\) 改成联合余图正滤波的初始代价。
它不能被误写成耗散式 (3.6) 中的一项，也没有被免费置零。

因为 \(E,J\) 都是收缩，逐项望远镜另给
\[
\boxed{\|J^n-E^n\|\le n\beta_\delta.}
\tag{4.2}
\]
在原 (1.2) 适用域中，若选 \(n=\exp(O(d^3))\)，右端趋零。
这一数值事实不扩大 (1.2) 的 \(q\) 范围。

## 5. 保原余负图的全幂预算和精确总耗散

将 (3.6) 以 \(J^{n-1}\) 合同：
\[
J^nMJ^n\preceq2J^{2n-1}(I-J)
\preceq2(I-J).
\]
所以对所有整数 \(n\ge1\) 和原源 \(r\)，
\[
\boxed{
\Xi(\mathcal J^n r)^2
\le2\Xi(r)^2+2\beta_\delta\mu(r)^2,}
\tag{5.1}
\]
\[
\boxed{
\mu(r-\mathcal J^n r)^2
\le n\{\Xi(r)^2+\beta_\delta\mu(r)^2\}.}
\tag{5.2}
\]
后一式用标量
\((1-t^n)^2\le n(1-t)\)。
全部 \(\mathcal J^n r\) 均在同一个实际
\(\mathscr R_{\rm rem}\) 中，不需幂后再作费用或角度未知的投影。

更强地，
\[
JMJ+(I-J)^2\preceq I-J^2.
\]
依次合同并相加，得到每个 \(N\ge1\) 的完整有限总预算
\[
\boxed{
\sum_{n=1}^{N}
\left\{
\Xi(\mathcal J^n r)^2+
\mu(\mathcal J^{n-1}r-\mathcal J^n r)^2
\right\}
\le\mu(r)^2-\mu(\mathcal J^N r)^2.}
\tag{5.3}
\]
因此无限和也不超过 \(\mu(r)^2\)。
与 (5.1) 的初始 \(\delta\) 误差不同，(5.3) 不含任何累积或加性 \(\delta\) 项。

由
\[
2\max_{0\le t\le1}t^{2n-1}(1-t)
=\frac1n\left(1-\frac1{2n}\right)^{2n-1}
\le\frac1n,
\]
还得到全源平滑界
\[
\boxed{\Xi(\mathcal J^n r)^2\le\frac1n\,\mu(r)^2.}
\tag{5.4}
\]
这是源仍在完整余负图中的界，不是删除某些坐标后的新费用。

固定参数时 \(M\succeq m_0I\) 对某个 \(m_0>0\) 成立。由 (3.6)，
\((m_0+2)J^2\preceq2J\)，故
\[
J\preceq\frac{2}{m_0+2}I,\qquad J^n\longrightarrow0
\]
为算子范数收敛。\(m_0\) 的温和移动参数下界仍未证明。
该固定参数结论不能与 (5.2) 的 \(\sqrt n\) 误差交换极限。

## 6. 固定测试的同一左配对可把正滤波移到实际来源

对任意两个同切口原源 \(r,t\)，因 \(\mathcal J\) 在 \(L\) 内积中自伴，
\[
\langle Lr,t\rangle-\langle Lr,\mathcal J^n t\rangle
=\langle L(r-\mathcal J^n r),t\rangle.
\]
因此
\[
\boxed{
\left|\langle Lr,t\rangle
-\langle Lr,\mathcal J^n t\rangle\right|
\le\mu(t)
\sqrt{n\{\Xi(r)^2+\beta_\delta\mu(r)^2\}}.}
\tag{6.1}
\]
若 \(t=t_q(f)\) 来自原固定物理测试，
\(U_qt_q=P_{V_q}f-P_{\mathcal K_q}f\)，故 \(\mu(t_q)\le\|f\|\)。
同时 (5.4) 给
\[
\mathcal J^n t_q\in\mathscr R_{\rm rem},\qquad
\Xi(\mathcal J^n t_q)^2\le\|f\|^2/n.
\tag{6.2}
\]
这不要求先知道原 \(t_q\) 自己的两费用；
它保留同一个 \(f,t_q\)，并以实际来源 \(r\) 的两费用支付配对误差。

然而 (6.1) 的主项
\(\langle Lr,\mathcal J^n t_q\rangle\) 仍是左配对。
双方属于同一余负图且两费用小，不足以使该项小。
本稿没有得到一次 \(\rho^{-1}\) 级的真实头能量比较，
没有把任意振幅界平方后隐藏其代价，也没有证明原 \(N=M\)。

