# 加一尾位后的完整左加 bare 商：真实度量、联合 graph Gram 与同源 Schur

日期：2026-11-14（UTC）。作者：Astra-ISP boundary_core / 789f；AI-assisted，GPT-6 Astra Pro。

状态：本文给出原短旗商的精确一位参数化，将其接成整个 joined 左加 bare graph 的 Gram、边界源与 Schur，并证明固定低孔下分支的均匀费用界。普通完整右链和原 flat 费用的进一步比较未由本文完成。

依赖：[原首物理头 graph](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)；
[一位完整左 graph](2026-11-14-one-bit-full-head-graph-schur-and-fixed-low-hole-feedback-789f-next.md)。
所有 \(D^h\) 的伪逆都先在完整原孔层中取；原无限正尾在这些有限孔层上的满射已由 R286 证明。

本文中“bare”是按原短核取商后的物理最小代表范数，不是普通完整右链范数。

## 1. 一层短旗的原物理商

固定旧尾 \(D\)，记

\[
 E_h^{(p)}=\ker D^h\cap\mathcal H_p,\quad
 P_h^{(p)}=P_{E_h^{(p)}},\quad Q_h^{(p)}=I-P_h^{(p)}.
\]

取 \(E_0^{(p)}=0\)。加一位权 \(a>0\) 后，新总孔层 \(p\) 为
\(\mathcal H_p\oplus\mathcal H_{p-1}\)，且

\[
 D_a=\begin{pmatrix}D&aI\\0&D\end{pmatrix}.
\]

对 \(h\ge1\)，定义完整层最小提升

\[
 R_{h,p}
 =h(D^h:\mathcal H_p\to\mathcal H_{p-h})^\dagger
                   D^{h-1}|_{E_h^{(p-1)}}.
\tag{1.1}
\]

不存在的负孔层取零。记 \(R_{0,p}=0\)。准确有

\[
 D^hR_{h,p}v=hD^{h-1}v,\qquad
 \operatorname{Ran}R_{h,p}
 \subset E_{h+1}^{(p)}\ominus E_h^{(p)}.
\tag{1.2}
\]

因而

\[
 E_{a,h}^{(p)}
 =\{(u-aR_{h,p}v,v):
       u\in E_h^{(p)},\ v\in E_h^{(p-1)}\}.
\tag{1.3}
\]

对任意原向量 \((u,v)\)，其模 \(E_{a,h}^{(p)}\) 的商坐标恰为

\[
 \boxed{
 z=Q_h^{(p)}u+aR_{h,p}P_h^{(p-1)}v,\qquad
 w=Q_h^{(p-1)}v.}
\tag{1.4}
\]

这个坐标对加上 (1.3) 的任一向量不变，并双射到
\(Q_h^{(p)}\mathcal H_p\oplus Q_h^{(p-1)}\mathcal H_{p-1}\)。

令

\[
 G_{h,p}(a)=(I+a^2R_{h,p}R_{h,p}^*)^{-1}
          \quad\hbox{于 }Q_h^{(p)}\mathcal H_p.
\]

原物理最小代表的范数准确为

\[
 \boxed{
 \|[(u,v)]\|_{\mathrm{bare}}^2
   =\langle G_{h,p}(a)z,z\rangle+\|w\|^2.}
\tag{1.5}
\]

证明是对 \(E_h^{(p)}\) 先正交消去，再对图
\(\{(-aR_{h,p}v,v)\}\) 作完整最小二乘。这里的新商度量一般不是单位矩阵。

## 2. 商中的真实删除项与一个已付共同抵消

设 \(h\ge1\)，从总孔层 \(p\) 的 \(h\) 商下降到 \(p-1\) 的 \(h-1\) 商。在 (1.4) 坐标中，可以选代表 \((u,v)=(z,w)\)，故准确得到

\[
 \boxed{
 \begin{pmatrix}z\\w\end{pmatrix}
 \longmapsto
 \begin{pmatrix}
 Q_{h-1}^{(p-1)}Dz+a\mathcal A_{h,p}w\\
 Q_{h-1}^{(p-2)}Dw
 \end{pmatrix},}
\tag{2.1}
\]

其中

\[
 \boxed{
 \mathcal A_{h,p}w
 =w+R_{h-1,p-1}P_{h-1}^{(p-2)}Dw.}
\tag{2.2}
\]

对 \(h=1\)，\(R_0=0\)，所以 \(\mathcal A_{1,p}=I\)。左前缀中没有短旗商时，交叉项也准确是 \(aI\)。

(2.2) 的两个项在旧物理范数中正交：输入
\(w\in(E_h^{(p-1)})^\perp\)，而 \(\operatorname{Ran}R_{h-1,p-1}\subset E_h^{(p-1)}\)。记
\(R=R_{h-1,p-1}\)、\(P=P_{h-1}^{(p-2)}\)。由
\(a^2R^*(I+a^2RR^*)^{-1}R=I-(I+a^2R^*R)^{-1}\)，得到精确等式

\[
 \boxed{
 \begin{aligned}
 &a^2\|G_{h-1,p-1}(a)^{1/2}\mathcal A_{h,p}w\|^2
       +\|Q_{h-1}^{(p-2)}Dw\|^2\\
 &=a^2\|w\|^2+\|Dw\|^2
   -\|(I+a^2R^*R)^{-1/2}PDw\|^2\\
 &\le(a^2+\|D\|^2)\|w\|^2 .
 \end{aligned}}
\tag{2.3}
\]

这是实际商度量中的共同预算。即使 \(R\) 的旧物理范数很大，其占据分支交叉费用仍被 (2.3) 支付。不能先把 (1.5) 换成欧氏范数，再把 (2.2) 的两项分别估计。

## 3. 两个真正切口 \(q\) 与 \(q-1\)

固定头维数 \(d\)。对旧切口 \(q\)，定义尾商空间

\[
 \mathfrak X_q=
 \bigoplus_{p=0}^{q}\mathcal H_p
 \ \oplus\
 \bigoplus_{j=1}^{d}
    (E_{j-1}^{(q+j)})^\perp.
\tag{3.1}
\]

用 \(\mathsf Q_q\) 表示从物理层
\(\bigoplus_{p\le q+d}\mathcal H_p\) 到 (3.1) 的正交最小代表投影。
令

\[
 \delta_q=\mathsf Q_qD|_{\mathfrak X_q},\qquad
 F_q=\ker\delta_q^d= \ker D^d\cap\mathfrak X_q.
\tag{3.2}
\]

短旗满足 \(DE_h\subset E_{h-1}\)，所以删除确实下降到这些商；并且
\(\delta_q^d=D^d\)，其输出已经落在无商的左前缀。

新切口 \(q\) 按该位空／占据拆分时，旧切口必须分别取 \(q\) 与 \(q-1\)。
逐层使用 (1.4)，新真实尾商同构为

\[
 \mathfrak X_q\oplus\mathfrak X_{q-1}.
\]

其准确物理度量是

\[
 \boxed{\mathsf W_a=
 \begin{pmatrix}\mathsf G_q(a)&0\\0&I\end{pmatrix},}
\tag{3.3}
\]

其中 \(\mathsf G_q(a)\) 在左前缀上为 \(I\)，在未来 \(p=q+j\) 层上为
\(G_{j-1,p}(a)\)。每个固定 \(q,d\) 上它严格正且有有界逆，但不声称逆界与 \(q\) 无关。

删除在同一坐标中的准确矩阵为

\[
 \boxed{
 \Delta_a=
 \begin{pmatrix}
 \delta_q&a\mathsf A_q\\0&\delta_{q-1}
 \end{pmatrix}.}
\tag{3.4}
\]

这里 \(\mathsf A_q\) 在无商部分为自然同层包含，在未来层为 (2.2)。
它一般不等于 \(I\)，也一般不与 \(\delta_q,\delta_{q-1}\) 交换。

## 4. 整个 joined graph 的显式可行列

取原真实头 \(A=VJ_dV^{-1}\)、\(V=1\oplus V_+\)，并记

\[
 \mathcal P(z)=\sum_{j=0}^{d-1}(Ve_j)(-z)^j,\qquad
 T_q=\mathcal P(\delta_q)|_{F_q}
       =\mathsf Q_q^{\rm head}\mathcal P(D)|_{F_q}.
\tag{4.1}
\]

旧 joined 核完整地由 \(T_qF_q=\ker(A+\delta_q)\) 参数化，其旧 Gram 为
\(\Gamma_q=T_q^*T_q\succeq I\)。

对 \(f\in F_{q-1}\)，逐个完整物理孔层取

\[
 R_df=d(D^d)^\dagger D^{d-1}f.
\tag{4.2}
\]

其最高孔数至多 \(q+d\)。令

\[
 K^{\rm raw}f=\mathcal P'(D)f-\mathcal P(D)R_df.
\tag{4.3}
\]

此外定义 \(\mathsf B_q\) 从旧占据物理层到新空分支商：在新总层
\(p=q+j\) 上，它为
\(R_{j-1,p}P_{j-1}^{(p-1)}\)，在左前缀上为零；它逐头坐标作用。
完整可行列为

\[
 \boxed{
 \mathsf K_q f
 =\mathsf Q_q^{\rm head}K^{\rm raw}f
       +\mathsf B_q^{\rm head}\mathcal P(D)f.}
\tag{4.4}
\]

最后一项正是未来 bare 商的真实改坐标项，不能从 (4.3) 中略去。

把完整物理新核
\(\mathcal P(D_a)(x-aR_df,f)\)
按 (1.4) 逐层取商，即得

\[
 \boxed{
 (x,f)\longmapsto
 (T_qx+a\mathsf K_qf,\ T_{q-1}f),
 \qquad x\in F_q,\ f\in F_{q-1}.}
\tag{4.5}
\]

它覆盖整个新 joined 核。确切地，

\[
 (A+\delta_q)\mathsf K_q
        =-\mathsf A_qT_{q-1};
\tag{4.6}
\]

给定下分支，(4.4) 提供一个上分支解，其余全部解相差 \(T_qF_q\)。
这证明满射性，也保留全部旧自由源。

## 5. 真联合 Gram、Schur 与边界源

记

\[
 \Gamma_{q,a}=T_q^*\mathsf G_q(a)T_q,\qquad
 \widetilde T_q=\mathsf G_q(a)^{1/2}T_q,\qquad
 \Pi_{q,a}=\widetilde T_q\Gamma_{q,a}^{-1}\widetilde T_q^*.
\]

(4.5) 在原物理 left+bare 范数中的准确 Gram 为

\[
 \boxed{
 \mathbb G_a^{\rm joined}=
 \begin{pmatrix}
 \Gamma_{q,a}
 &aT_q^*\mathsf G_q(a)\mathsf K_q\\
 a\mathsf K_q^*\mathsf G_q(a)T_q
 &\Gamma_{q-1}
      +a^2\mathsf K_q^*\mathsf G_q(a)\mathsf K_q
 \end{pmatrix}.}
\tag{5.1}
\]

对完整旧上源作 Schur 得

\[
 \boxed{
 \mathbb S_a^{\rm joined}
 =\Gamma_{q-1}
   +a^2\mathsf K_q^*\mathsf G_q(a)^{1/2}
          (I-\Pi_{q,a})
       \mathsf G_q(a)^{1/2}\mathsf K_q.}
\tag{5.2}
\]

两个变化必须同时保留：上源 Gram 从 \(\Gamma_q\) 变为
\(\Gamma_{q,a}\)，可行列从原物理导数列变为 (4.4)。
只保其中一项并不是新的完整 joined Schur。

原边界源在左切口读取，因此不存在未来商改坐标。定义

\[
 \mathcal B_qx=A(T_qx)_q,\qquad
 \mathcal C_qf=A(\mathsf K_qf)_q.
\]

同一个实际新源在空／占据两部分的准确读取是

\[
 \boxed{
 \mathcal B_a(x,f)
  =\bigl(\mathcal B_qx+a\mathcal C_qf,\ 
                \mathcal B_{q-1}f\bigr).}
\tag{5.3}
\]

这里以 \(\operatorname{Ran}\mathcal B_a\) 为实际新源空间，不把它未经证明地替换成两个旧源空间的正交直和。

因为整个 joined kernel 同时参数化全部合法左链与全部 bare 右链，
在这个实际源上有

\[
 \boxed{
 (L_a+B_a)^{-1}
   =\mathcal B_a
      (\mathbb G_a^{\rm joined})^{-1}\mathcal B_a^*.}
\tag{5.4}
\]

若实际源像未另证闭，(5.4) 按其自然最小能量闭二次型及在像闭包上的逆理解；不额外宣称源像闭或最小能量算子全域有界。

等价地，右端是固定实际源时对 (5.1) 的真实最小二乘压缩。
因此本文保存的不只是一个孤立的右旗范数，而是完整联合度量和它的实际边界源。

## 6. 固定低孔下源的真正 joined 预算

假设 \(f\in F_{q-1}\) 的物理孔数支撑至多

\[
 s\le\min(q-1,d-2).
\]

则 \(R_df=0\)，\(\mathcal P(D)f\) 与 \(\mathcal P'(D)f\) 全在无商的左前缀；故

\[
 \mathsf K_qf=\mathcal P'(D)f,\qquad
 \mathsf G_q(a)\mathsf K_qf=\mathsf K_qf.
\]

令
\[
 c_s(\nu)=\sum_{j=1}^{s+1}j\|Ve_j\|\nu^{j-1},
 \qquad \|D\|\le\nu.
\]
由 (5.2) 的完整投影收缩，

\[
 \boxed{
 0\le
 \langle(\mathbb S_a^{\rm joined}-\Gamma_{q-1})f,f\rangle
 \le a^2c_s(\nu)^2\|f\|^2.}
\tag{6.1}
\]

完整最小上源为
\[
 x_{\min}
   =-a\Gamma_{q,a}^{-1}
          T_q^*\mathsf G_q(a)\mathsf K_qf,
\]
且它的真正新 left+bare 能量满足

\[
 \boxed{
 \|\mathsf G_q(a)^{1/2}T_qx_{\min}\|^2
 \le a^2c_s(\nu)^2\|f\|^2.}
\tag{6.2}
\]

其左物理范数与未来新 bare 范数都被 (6.2) 支付。
\(x_{\min}\) 可以有高孔回馈；本文没有将其截掉。
由于 \(\mathsf G_q(a)\) 未有统一下界，不能从 (6.2) 免费推出旧欧氏源范数
\(\|x_{\min}\|\) 的同一界。

真实 \(V_m\) 的低列一致，所以固定 \(s\) 时 (6.1)--(6.2) 的常数与高头维数和整个孔截止无关。它把前稿固定低孔结论准确扩到整个 left+bare joined graph。

## 7. 仍须支付的原接口

原 \(Z_q^{-1}\) 测试流是否落在 §6 的源类尚未证明；祖先 birth 可为 \(q-h\)，不能因固定物理测试就把其 first-head 源当成固定低孔。

(5.4) 支付的是 \(L+B\)。原第二费用为 \(B+LGL\)，其中 \(G\) 来自普通完整右链；将其接回仍须在同一个实际边界源 (5.3) 上保留普通右链的全部旗与当前商改坐标。本文没有把 \(B\) 与 \(G^{-1}\) 等同，也没有由各自 Loewner 界相乘推出 flat 界。

这些公式把未付项集中到真正的 \(\mathsf K_q,\mathsf G_q\)、实际源 \(\mathcal B_a\) 和同一完整右 Gram；没有把原负前缀 graph 变成坐标为零。
