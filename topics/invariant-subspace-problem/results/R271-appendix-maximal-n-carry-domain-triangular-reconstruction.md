# N 型最大 carry 域的严格三角重构

日期：2026-11-27（Asia/Taipei）；2026-11-26（UTC）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：本稿域身份与范数估计已证明；只处理原 N 型，未证明 $W$ 的规范来源满足这些域条件。**

本稿接[真实 carry 来源范数](../results/R271-appendix-canonical-source-carry-norm-total-hole-core.md)。它加强的是该稿 N 型来源条件的必要性：若各首缺位块已在 Hilbert 空间，且**完整形式 carry 输出**在 Hilbert 空间，则加权平方和自动有限。证明不预先假设该平方和，也不将 Y 型的重叠列套入本稿。

## 1. 原正交列及保首缺位块

沿用
$$
T_N=\sum_{i\ge0}a_iN_i,\quad
D^*=\sum_{i\ge0}a_iE_i^*,\quad
K=T_N^*-D^*,\quad a_i=(i+1)^{-2},
$$
以及首缺位投影 $P_q$。第 $q$ 块仍保留其余全部物理位。

对 $i<q$，记 $V_{iq}:P_q\mathcal H\to\mathcal H$ 为真实二进位加法对应的等距，使
$$
N_i^*P_q=\frac{\alpha_q}{\alpha_i}V_{iq}P_q.
\tag{1.1}
$$
其输出前 $i$ 位占据、第 $i,\ldots,q-1$ 位真空、第 $q$ 位占据；更高位按原输入保持。不同 $(i,q)$ 的输出空间两两正交。定义
$$
c_q^2=\sum_{i<q}a_i^2(\alpha_q/\alpha_i)^2\quad(q\ge1),
\qquad c_0=0,
$$
$$
A_q=\left.\sum_{i>q}a_i(N_i^*-E_i^*)\right|_{P_q\mathcal H},
\qquad
s_q=\sum_{i>q}a_i\eta_i,
\qquad \rho_q=(c_q^2+s_q^2)^{1/2}.
\tag{1.2}
$$
每个 $A_q$ 保持 $P_q\mathcal H$，且 $\|A_q\|\le s_q$。前稿的实际权估计给
$$
c_q\ge b_q=q^{-2}\eta_{q-1},\qquad
s_q\le b_q/12\quad(q\ge1).
\tag{1.3}
$$
$s_0=\rho_0$ 是一个固定严格正数，不能除以 $c_0=0$。

对有限首缺位块的输入，原算子的准确分解是
$$
Kh=\sum_{q\ge1}\sum_{i<q}
a_i\frac{\alpha_q}{\alpha_i}V_{iq}P_qh
+\sum_{q\ge0}A_qP_qh.
\tag{1.4}
$$

## 2. 归一化等距与真正的严格下三角算子

令
$$
\mathcal U=\bigoplus_{q\ge1}P_q\mathcal H,
\qquad
U_q=\sum_{i<q}\frac{a_i\alpha_q}{c_q\alpha_i}V_{iq}.
\tag{2.1}
$$
由 (1.1) 的完整输出正交性，每个 $U_q$ 都是等距，不同 $q$ 的值域也正交。因此
$$
U:\mathcal U\to\mathcal H,\qquad
Uu=\sum_{q\ge1}U_qu_q
\tag{2.2}
$$
是等距，$U^*$ 为收缩。

另定义有界算子
$$
J:\mathcal U\to\mathcal H,\qquad
Ju=\sum_{i\ge1}A_i(u_i/c_i).
\tag{2.3}
$$
不同 $i$ 的输出在正交的 $P_i$ 块中，故 (1.3) 给
$$
\boxed{\|J\|\le1/12.}
\tag{2.4}
$$
令 $R=U^*J$，则 $\|R\|\le1/12$。

这里还需要比有界性更强的准确位置关系。$U_q$ 的输出只涉及首缺位 $i<q$，而 $A_i$ 的输出首缺位为 $i$，所以
$$
\boxed{
(Ru)_q=\sum_{i=1}^{q-1}U_q^*A_i(u_i/c_i).}
\tag{2.5}
$$
每一行确实只有有限个来源块；它不是一个需要先知道 $u\in\mathcal U$ 才能定义的无限行。此式也定义了 $R$ 对任意逐块 Hilbert 序列的形式作用。在该意义下，$R$ 严格将来源指标 $i$ 送往 $q>i$。

## 3. 不预设平方和的最大域定理

**定理。** 设形式序列 $h$ 满足
$$
h_q:=P_qh\in\mathcal H\quad\text{对每个 }q\ge0,
\qquad k:=Kh\in\mathcal H
\tag{3.1}
$$
，其中第二式是完整原 $K=T_N^*-D^*$ 的逐行形式输出。则
$$
\boxed{
\sum_{q\ge0}\rho_q^2\|h_q\|^2<\infty.}
\tag{3.2}
$$
更准确地，
$$
\boxed{
\left(\sum_{q\ge1}c_q^2\|h_q\|^2\right)^{1/2}
\le\frac{12}{11}\bigl(\|k\|+s_0\|h_0\|\bigr).}
\tag{3.3}
$$

**证明。** 先仅逐块定义 $u_q=c_qh_q$，**不假设** $u=(u_q)\in\mathcal U$。由 (3.1)，$A_0h_0\in\mathcal H$，因此
$$
g=U^*(k-A_0h_0)\in\mathcal U,\qquad
\|g\|\le\|k\|+s_0\|h_0\|.
\tag{3.4}
$$

将 (1.4) 的形式等式投到 $U_q$ 的值域再施 $U_q^*$。降首缺位项中只有来源 $q$ 留下，并且给 $u_q$；保首缺位项只留下 $i<q$。于是
$$
\boxed{
u_q+\sum_{i=1}^{q-1}U_q^*A_i(u_i/c_i)=g_q
\quad(q\ge1).}
\tag{3.5}
$$
此操作在当前假设下合法：每个 $U_q^*$ 只读取有限个首缺位块 $i<q$；每个被读取的 $A_ih_i$ 都是 Hilbert 向量。降列的输出支撑又将来源 $q$ 与其他全部来源严格分开。因此没有对一个尚未知平方可和的完整 $Kh$ 分项作无限内积；被使用的 $k$ 本身已经由 (3.1) 在 Hilbert 空间中。

另一方面，$\|R\|\le1/12$ 使
$$
v=(I+R)^{-1}g\in\mathcal U,\qquad
\|v\|\le\frac{12}{11}\|g\|.
\tag{3.6}
$$
该真实 Hilbert 解也满足逐行有限式 (3.5)。严格下三角式在**全部逐块 Hilbert 序列**中具有唯一解：第 $1$ 行强制 $u_1=g_1=v_1$；若前 $q-1$ 块已相同，第 $q$ 行只有这些有限来源，故也强制 $u_q=v_q$。逐块归纳给 $u=v$。

现在才得到 $u\in\mathcal U$，并由 (3.4)–(3.6) 得 (3.3)。最后
$$
\sum_{q\ge0}\rho_q^2\|h_q\|^2
\le s_0^2\|h_0\|^2+rac{145}{144}\|u\|^2<\infty,
\tag{3.7}
$$
其中对 $q\ge1$ 使用 $s_q/c_q\le1/12$。证毕。

反向包含已由前稿有界延拓证明。因此，在每块 $P_qh\in\mathcal H$ 的形式序列类中，本稿得到准确身份
$$
\boxed{
Kh\in\mathcal H
\iff h\in\mathcal C_{N,2}
:=\left\{h:\sum_q\rho_q^2\|P_qh\|^2<\infty\right\}.}
\tag{3.8}
$$

## 4. 作为原 S 图来源空间上的最大闭算子

置
$$
\mathcal X_1=
\left\{h:\sum_q\alpha_q^2\|P_qh\|^2<\infty\right\},
\qquad \|h\|_{\mathcal X_1}=\|Sh\|.
$$
这与 $y=Sh\in\mathcal H$、$y_0=0$ 的来源空间等距等价。每个 $P_qh$ 都在 Hilbert 空间，但不由此推出 (3.2)。

由 $\rho_q\ge q^{-2}\alpha_q/\alpha_{q-1}$（$q\ge1$），以及第零项 $\rho_0=s_0>0$，$\mathcal C_{N,2}$ 连续包含于 $\mathcal X_1$。定理 3 准确识别
$$
\boxed{
\mathcal D(K_{\max}:\mathcal X_1\to\mathcal H)
=\mathcal C_{N,2}.}
\tag{4.1}
$$
这里最大算子按原逐行形式 $K$ 定义。每个整数输出行只涉及有限个输入坐标，坐标在 $\mathcal X_1$ 上连续，所以 $K_{\max}$ 闭。

其图范数与 $\mathcal C_{N,2}$ 的来源范数等价。一个方向由前稿的 $\|Kh\|\le\sqrt2\|h\|_{\mathcal C_{N,2}}$ 和上述连续包含；另一个方向由 (3.3)、(3.7) 及
$$
\|h_0\|\le\alpha_0^{-1}\|h\|_{\mathcal X_1}
$$
直接给出。有限首缺位截断随后在该图范数中收敛，每个这样的截断都在 $\mathcal H$；再在有限个块中按整数支撑逼近，可知有限整数支撑向量也是 $K_{\max}$ 的图核心。

## 5. 同 W 来源中留下的是哪一种抵消

令 $w\in W=\ker T_N\ominus\overline{B\ker T_N}$，$h=h(w)$ 为规范形式解 $T_N^*h=w$。

若另外知道所有 $P_qh\in\mathcal H$，则本稿和总孔核心给
$$
\boxed{Kh\in\mathcal H\quad\Longrightarrow\quad w=0.}
\tag{5.1}
$$
同样，若 $D^*h\in\mathcal H$，由 $Kh=w-D^*h$ 也得到 $w=0$。尤其在已经具有 $Sh\in\mathcal H$ 的图来源中，各块条件自动成立，于是非零 $w$ 必须满足
$$
D^*h\notin\mathcal H,\qquad Kh\notin\mathcal H,
\qquad D^*h+Kh=w\in\mathcal H
\tag{5.2}
$$
这样的真实抵消。

这里没有证明 $Sh(w)\in\mathcal H$，也没有从 R238 每个总孔层在 $\mathcal H$ 推出每个首缺位块在 $\mathcal H$。如果连后一条件也未知，就不能调用本稿的逐块重构。最后，(5.2) 的抵消尚未由 $w\perp B\ker T_N$ 排除；本稿只是把这条实际未付机制与无条件 carry 域完整分开。
