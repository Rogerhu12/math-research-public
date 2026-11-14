# R236 附录：全阶精确共振族的零输出分类与实际最低阶

日期：2026-11-13。作者：Astra-ISP-0c / central_next。

[R270 第三附录](R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md) 已证明任意复 $\ell^2$ 主行、任意 first 指数权的全部阶精确共振族非零即循环。本附录不重复登记该范围；补充可和行的全部零输出、单位和最低实际阶数。逐位生成式及旧 R152/R180/R183 接口的独立证明分别见[全阶记录](../notes/2026-11-13-log-counterterms-all-orders-and-zero-output-classification-central-next.md)和[二次归约记录](../notes/2026-11-13-exact-quadratic-resonance-via-existing-fast-theorems-central-next.md)。

## 定义及结论

取
$$
u=a_*+\sum_j a_j\chi_j,\quad a\in\ell^1(\mathbb C),\qquad
w=b_*+\sum_jb_j\chi_j,\quad b\in\ell^2(\mathbb C).
$$
记 $S_n=\sum_ja_j^n(\chi_j-1)$，并定义
$$
F_p=p![t^p]\exp\left(tu+\sum_{n=2}^p\frac{2^{n-1}}n t^nS_n\right),
\quad F_0=1,\quad F_1=u.
$$
对任意非零标量多项式 $q(z)=\sum_{p=0}^dq_pz^p$，置 $F_q=\sum_pq_pF_p$。这不是普通点态 $q(u)$。令
$$
s=a_*+\sum_ja_j,\qquad L=\#\{j:a_j\ne0\},\qquad
\mu=\operatorname{mult}_s(q),
$$
其中 $q(s)\ne0$ 时 $\mu=0$，允许 $L=\infty$。

**定理。** 对原实际 Haar 模型，
$$
\boxed{F_qe^w=0\iff L<\mu.}
$$
若 $\mu=0$，相应实际有界乘子是 $\mathcal A$ 的单位。若 $1\le\mu\le L$，记最早 $\mu$ 个非零物理位为 $j_1<\cdots<j_\mu$，并令 $t_j=e^{-2b_j}$。其实际乘子 $T_q$ 的最低阶和系数为
$$
\boxed{\operatorname{ord}T_q=\sum_{\ell=1}^{\mu}2^{j_\ell},}
$$
$$
\boxed{
\gamma_{\sum_\ell2^{j_\ell}}(T_q)
=q^{(\mu)}(s)(-2)^\mu
\prod_{\ell=1}^{\mu}\frac{a_{j_\ell}t_{j_\ell}}{d_{j_\ell}}\ne0.
}
$$
全部非零输出由 R270C 循环；无限支撑时对每个非零 $q$ 自动非零。

## 证明：真实基本对称和

置
$$
R_j=V(t_jN_j),\qquad Q_j=a_j(R_j-I).
$$
真实平方进位和有限低位预解给统一 $\|Q_j\|\le C_b|a_j|$。因此在本附录的可和前提下，$\sum_jQ_j$ 按算子范数绝对收敛，$X_b=sI+\sum_jQ_j$。若
$$
C(t)=\prod_j e^{-tQ_j}(I+tQ_j),
$$
则其紧盘范数收敛由 $\sum\|Q_j\|^2<\infty$ 保证，而且准确有
$$
e^{tX_b}C(t)=e^{ts}\prod_j(I+tQ_j).
$$
全阶记录的逐位恒等式只使用真实 $N_j$：
$$
e^{-h_j(t)}(\cosh h_j(t)I+R_j\sinh h_j(t))
=I+tQ_j,\qquad h_j(t)=-\tfrac12\log(1-2ta_j).
$$
由此取有限 Taylor 系数，得到
$$
T_qe^w=F_qe^w,\qquad
\boxed{T_q=\sum_{r=0}^{d}q^{(r)}(s)e_r(Q),}
$$
$$
e_r(Q)=\sum_{j_1<\cdots<j_r}Q_{j_1}\cdots Q_{j_r},\qquad e_0=I.
$$
各和绝对范数收敛，因为
$$
\sum_{j_1<\cdots<j_r}\prod_{\ell=1}^r\|Q_{j_\ell}\|
\le\frac1{r!}\left(\sum_j\|Q_j\|\right)^r.
$$

若 $L<\mu$，所有可能非零项均消失，故 $T_q=0$。若 $\mu=0$，字符为 $q(s)\ne0$，所以 $T_q$ 是单位。

若 $1\le\mu\le L$，每个 $Q_j$ 的最低阶是 $2^j$，对应系数是 $-2a_jt_j/d_j$。上式中所有 $r<\mu$ 的标量系数为零；$r=\mu$ 的最低阶由最早 $\mu$ 位唯一取得。任何其他同大小位置组、或任何 $r>\mu$ 的组，其阶严格更高。形式系数连续性与上述绝对收敛允许取该系数，给定理公式和 $T_q\ne0$。最后，$e^w$ 循环，而 $T_q$ 有界且与 $A$ 交换，所以 $T_qe^w=0$ 当且仅当 $T_q=0$。证毕。

## 二次例与适用边界

$q(z)=z^2$ 时，若 $s=0$，$T_q=2e_2(Q)$。恰一个非零 $a_j$ 时，零例准确是 $a_*=-a_j$；至少两个非零系数时，首阶为 $2^{j_1}+2^{j_2}$、首系数为 $8a_{j_1}a_{j_2}t_{j_1}t_{j_2}/(d_{j_1}d_{j_2})$。

当 $a\notin\ell^1$ 时，不定义 $s$ 或使用这条可和展开。全阶循环结论仍由 R270C，亦可由 R180 的无界快系数秩零分支给出。本补充不处理普通 $q(u)$ 的一般慢 Bell 项、下一非零阶辅助共振、独立无限慢模式或一般 Hilbert 向量；普通 ISP 仍未解决。
