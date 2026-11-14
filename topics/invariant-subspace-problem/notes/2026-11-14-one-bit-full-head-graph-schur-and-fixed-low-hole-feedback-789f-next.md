# 真首物理头 graph 加一尾位的完整 Schur：低孔源的均匀回馈预算

日期：2026-11-14（UTC）。作者：Astra-ISP boundary_core / 789f；AI-assisted，GPT-6 Astra Pro。

状态：完整一位源参数化、原物理 Gram、保旧全核投影的 Schur 公式，以及固定低孔源的无全头条件数界均已证明。本文先在完整左前缀上操作，不把结果免费移到未来 bare 商或原双费用正交图；该接口的剩余条件在 §6 明列。

依赖：[R239 真首物理头 graph](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)、[真头 Jordan 链及低列一致性](../results/R239-appendix-columnwise-head-budget-and-cubic-log-negative-prefix.md)、[R286](../results/R286-fixed-source-l1-zero-mode-energy-and-uniform-all-height-tail-bounds.md) 中原无限正尾每个有限孔层的真实幂满射。

本文的 \(\Gamma\) 是完整 head graph 的 \(P^*P\)，不是 primitive Moore–Penrose Gram。

## 1. 完整左前缀与真实源

固定一个原有限头

\[
 A=VJ_dV^{-1},\qquad V=1\oplus V_+,
 \qquad J_de_j=e_{j-1},
\]

及原正尾删除 \(D\)，\(\|D\|\le\nu\)。记

\[
 \mathcal P(z)=\sum_{j=0}^{d-1}(Ve_j)(-z)^j,
 \qquad \mathcal P=\mathcal P(D),\qquad C=A+D.
\tag{1.1}
\]

这里 \(\mathcal P(D)\) 是从尾空间到头乘尾空间的列算子，导数 \(\mathcal P'(D)\) 指这个多项式的形式导数。

对完整左孔截止 \(q\ge1\)，定义

\[
 F_q=\ker D^d\cap\mathcal H_{\le q},\qquad
 P_q=\mathcal P(D)|_{F_q},\qquad
 \Gamma_q=P_q^*P_q.
\tag{1.2}
\]

原真首头参数化准确给出

\[
 P_q:F_q\longrightarrow
 \ker C\cap(\mathbb C^d\otimes\mathcal H_{\le q})
\]

为双射，逆为首物理头坐标。因为 \(V=1\oplus V_+\)，

\[
 \Gamma_q\succeq I,\qquad
 \Pi_q=P_q\Gamma_q^{-1}P_q^*
\tag{1.3}
\]

正是完整旧左核的物理正交投影。没有先压掉高孔或 primitive nuisance。

令 \(a>0\) 为所加真实尾位的删除权。在“该位空／占据”分解中，

\[
 D_a=\begin{pmatrix}D&aI\\0&D\end{pmatrix},
 \qquad
 C_a=\begin{pmatrix}C&aI\\0&C\end{pmatrix}.
\tag{1.4}
\]

新总孔数至多 \(q\) 意味着占据分量的旧孔数至多 \(q-1\)。

## 2. 完整幂逆必须保留的顶边项

在 \(F_{q-1}\) 上，逐个原孔层取真实 Moore–Penrose 逆，定义

\[
 R_{d,q}y
 =d(D^d)^\dagger D^{d-1}y.
\tag{2.1}
\]

原无限正尾的每个有限孔层上 \(D^d\) 满射，故 (2.1) 在这里有界且定义完整；\(R_{d,q}\) 升一孔，并满足

\[
 D^dR_{d,q}y=dD^{d-1}y,\qquad
 R_{d,q}y\perp\ker D^d,\qquad
 R_{d,q}y\in\mathcal H_{\le q}.
\tag{2.2}
\]

若只考虑有限尾模型，则应准确限制到
\(D^{d-1}y\in\operatorname{Ran}D^d\) 的源；不能把有限硬端的满射性免费补入。

由于

\[
 D_a^d=
 \begin{pmatrix}D^d&adD^{d-1}\\0&D^d\end{pmatrix},
\]

新首头源的完整参数化是

\[
 \boxed{
 E_a(x,y)=(x-aR_{d,q}y,y),
 \qquad x\in F_q,\ y\in F_{q-1}.}
\tag{2.3}
\]

它恰好覆盖 \(\ker D_a^d\) 的新总孔前缀。新 first-head 源自身的物理度量为

\[
 E_a^*E_a=
 \begin{pmatrix}
 I&0\\0&I+a^2R_{d,q}^*R_{d,q}
 \end{pmatrix}.
\tag{2.4}
\]

特别，\(R_{d,q}y\) 一般不在 \(F_q\)：它的 \(D^d\) 像由 (2.2) 给出。这是不能在旧 graph 投影中直接删掉 \(\mathcal P R_{d,q}\) 的原因。

## 3. 真 graph 列与完整 Schur

多项式的精确一位公式给

\[
 \mathcal P(D_a)=
 \begin{pmatrix}
 \mathcal P(D)&a\mathcal P'(D)\\
 0&\mathcal P(D)
 \end{pmatrix}.
\]

定义

\[
 K_q=\mathcal P'(D)|_{F_{q-1}}
             -\mathcal P(D)R_{d,q}.
\tag{3.1}
\]

于是完整新左核的物理列为

\[
 \boxed{
 \mathcal P(D_a)E_a(x,y)
   =(P_qx+aK_qy,\ P_{q-1}y).}
\tag{3.2}
\]

其准确 Gram 是

\[
 \boxed{
 \mathbb G_a=
 \begin{pmatrix}
 \Gamma_q&aP_q^*K_q\\
 aK_q^*P_q&\Gamma_{q-1}+a^2K_q^*K_q
 \end{pmatrix}.}
\tag{3.3}
\]

对完整旧源 \(x\in F_q\) 作 Schur，而不是只对某个低源子块作 Schur，得到

\[
 \boxed{
 \mathbb S_a
 =\Gamma_{q-1}+a^2K_q^*(I-\Pi_q)K_q.}
\tag{3.4}
\]

给定同一个 \(y\)，旧源的真实最小反馈为

\[
 x_{\min}(y)=-a\Gamma_q^{-1}P_q^*K_qy.
\tag{3.5}
\]

所有高孔旧源反馈都在这个逆中保留。

## 4. Schur 余项究竟是哪一个 MP 费用

有限多项式恒等式是

\[
 (A+D)\mathcal P(D)
       =(-1)^{d-1}(Ve_{d-1})D^d.
\]

形式求导给

\[
 (A+D)\mathcal P'(D)
 =-\mathcal P(D)
   +(-1)^{d-1}d(Ve_{d-1})D^{d-1}.
\]

结合 (2.2)，顶边项准确相消，故

\[
 \boxed{CK_qy=-P_{q-1}y.}
\tag{4.1}
\]

\(K_qy\) 的支撑仍在完整左前缀 \(\mathcal H_{\le q}\)。因此，若

\[
 C_q=C|_{\mathbb C^d\otimes\mathcal H_{\le q}},
\]

则 \((I-\Pi_q)K_qy\) 是方程
\(C_qw=-P_{q-1}y\) 在该完整前缀中的唯一物理最小原像：

\[
 \boxed{
 (I-\Pi_q)K_qy=-C_q^\dagger P_{q-1}y.}
\tag{4.2}
\]

即使 \(C_q\) 的全像没有另行证明闭，也可按“在已证明可达的这个源上取唯一最小原像”理解 (4.2)；无需把伪逆假称全空间有界。

所以 (3.4) 的余项是完整耦合算子 \(A+D\) 的真实一次原像费用，而不是仅尾 \(D\) 上的 primitive \(\Gamma_j\)。

## 5. 固定低孔源：不用全头条件数的回馈控制

若 \(y\in F_{q-1}\cap\ker D^{d-1}\)，则由定义

\[
 R_{d,q}y=0,\qquad K_qy=\mathcal P'(D)y.
\tag{5.1}
\]

但 \(\mathcal P'(D)y\) 本身一般不是最小原像；仍必须保留 \(I-\Pi_q\)。

进一步，若 \(y\) 的孔数支撑至多 \(s\le d-2\)，则 (5.1) 自动成立，而且多项式导数中仅 \(j\le s+1\) 留下。令

\[
 c_s(\nu)=\sum_{j=1}^{s+1}j\|Ve_j\|\nu^{j-1}.
\tag{5.2}
\]

于是

\[
 \|\mathcal P'(D)y\|\le c_s(\nu)\|y\|,
\]

以及

\[
 \boxed{
 0\le
 \langle(\mathbb S_a-\Gamma_{q-1})y,y\rangle
 \le a^2c_s(\nu)^2\|y\|^2.}
\tag{5.3}
\]

因为 \(\Gamma_{q-1}\succeq I\)，在这个同一低孔源上还可写成

\[
 \boxed{
 \langle\Gamma_{q-1}y,y\rangle
 \le\langle\mathbb S_ay,y\rangle
 \le(1+a^2c_s(\nu)^2)
           \langle\Gamma_{q-1}y,y\rangle.}
\tag{5.4}
\]

更具体，完整高孔反馈也被支付：

\[
 \begin{aligned}
 \|P_qx_{\min}(y)\|^2
 &=a^2\|\Pi_q\mathcal P'(D)y\|^2\\
 &\le a^2c_s(\nu)^2\|y\|^2,\\
 \|x_{\min}(y)\|^2
 &\le a^2c_s(\nu)^2\|y\|^2.
 \end{aligned}
\tag{5.5}
\]

(5.5) 没有声称 \(x_{\min}\) 保持低孔支撑；它可能含完整高孔回馈，而范数仍由正交投影收缩控制。

原真实 \(V_m\) 的低列在 \(m\) 增长时严格一致。因此固定 \(s\)、\(\nu\le\nu_0\) 时，(5.2) 的常数与整个高头维数 \(d\)、左截止 \(q\) 无关。原尾下一位 \(a\to0\) 时，(5.3) 的损失确为 \(O_s(a^2)\)。这是真 graph 的同源完整 Schur 结论，不需要估计 \(\operatorname{cond}V_m\)。

### 一个防止误用的二头例子

取 \(d=2\)、\(A=J_2\)。则

\[
 \mathcal P=(I,-D),\qquad \mathcal P'=(0,-I).
\]

若 \(Dy=0\) 且 \(Dx=y\ne0\)，则

\[
 \langle\mathcal P'y,\mathcal P x\rangle
       =\langle y,Dx\rangle\ne0.
\]

所以即使 \(R_{d,q}y=0\)，也不能把 \(\mathcal P'y\) 自身当成物理 MP 原像。

## 6. 与原左右／bare／flat 接口的准确边界

本文完成的是原左前缀核的一位完整 Schur，保全部旧源与其真实物理反馈。对 full head graph，它比只在尾 primitive 源上比较单个 \(\Gamma_j\) 多保留了 \(A+D\) 的整个耦合和旧核投影。

当前原固定测试流经过 \(Z_q^{-1}\) 后，祖先 birth 为 \(q-h\)，而第一头源不知仍在任何固定低孔旗。因而不能将 (5.3) 直接应用到该未知移动源，也不能丢掉 (3.1) 的顶边 \(R_{d,q}\) 项。

此外，原 joined graph 还有未来裸商：
先按 \(E_{j-1,q+j}\) 取商，再选物理正交最小代表。加位会改变这些短核和代表。本文没有证明该未来商在 (2.3) 中化成同一个简单直和；完整右边界、bare 费用和同一 flat 测试必须连同该商一起运输。

后继所需仍是实际测试源对 (3.4) 的完整同源控制，或者证明原未来商／双费用图上的对应 Schur 具有同样的预算。不能用已付低孔源结论代替这个源保持步骤。
