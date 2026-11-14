# R253 第四附录：边界核的正序推论与慢符号的全空间有界除法障碍

日期：2026-11-13（UTC）。作者：normal_states / Astra-ISP-1cf。

状态：已证明的中间结论。主证明是 R174、R185、R188 已有真实边界核的全空间正序推论；补充一组独立的实际 Haar 定量见证。它不运输未知不变子空间或一般非 UHF 交换子到边界，也不排除全部非平凡尾乘子。

## 1. 结论和与既有结果的区别

取
$$
S=S_N=\sum_{j\ge0}\frac{N_j}{(j+1)^2}
\quad\text{或}\quad
S=S_Y=\sum_{j\ge0}\frac{Y_j}{(j+1)^2}.
$$
两者在原 Haar 空间上单射且像稠密。

**定理。** 对每个整数 $r\ge0$，
$$
\boxed{
A^r\notin S B(H),\qquad
\operatorname{Ran}A^r\not\subseteq\operatorname{Ran}S.
}
\tag{1.1}
$$
这里右因子允许为任意 $B(H)$ 算子，无须事先属于 $\mathcal A$ 或 $A'$。

对每个固定 $r\ge1$，还存在原 Haar 单位向量 $z_m$ 及常数 $c_r>0$，使所有充分大的 $m$ 满足
$$
\boxed{
\frac{\|A^rz_m\|}{\|Sz_m\|}\ge c_r m.
}
\tag{1.2}
$$
$z_m$ 可取 R253 第二附录的真实有限头链校正，链长仅为固定的 $r+1$。

[R185](R185-slow-additive-boundary-kernel-and-nonstandard-closed-ideal.md) 与 [R188](R188-critical-first-chaos-nonstandard-closed-principal-ideal.md) 的正文已经证明
$A^r\notin\overline{S\mathcal A}^{\|\cdot\|}$。本文明确抽出更强的全空间有界因式及像包含结论；其简短证明使用同一已证边界核，但不需要给未知右因子定义边界表示。

## 2. 只运输全空间正序，不运输右因子

[R174](R174-last-column-boundary-state-and-negative-integer-shift.md) 的物理全 1 乘积表示是实际 UHF 代数
$$
\mathfrak U=C^*(I,A)
$$
的等距含幺 $*$ 表示
$$
\pi_-:\mathfrak U\longrightarrow B(\ell^2(\mathbb N_0)).
$$
确切地，局部矩阵按通常张量作用，保持乘法和伴随，然后按范数延拓。记 $B=\pi_-(A)$；它满足
$$
Be_0=0,\qquad
Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1).
$$

R185 和 R188 分别给出对应 $S$ 的一个向量 $g$，满足
$$
Tg=0,\qquad T=\pi_-(S),\qquad
B^rg\ne0\quad\text{对全部 }r\ge0.
\tag{2.1}
$$
后一句由 $g$ 有无限支持及所有后移权非零得到。

反设有 $R\in B(H)$ 使 $SR=A^r$。由于 $A^rS=SA^r$，
$$
S(RS-A^r)=SRS-SA^r=A^rS-SA^r=0.
$$
由原 $S$ 的单射性，
$$
RS=A^r.
\tag{2.2}
$$
于是原全空间上有正算子不等式
$$
\boxed{
(A^r)^*A^r=(RS)^*(RS)
\le\|R\|^2S^*S.
}
\tag{2.3}
$$
(2.3) 的两边都在 $\mathfrak U$，尽管 $R$ 本身未必在其中。$C^*$ 子代数的正锥由原忠实表示的正算子锥确定，所以差
$\|R\|^2S^*S-(A^r)^*A^r$
是 $\mathfrak U$ 的正元。对它应用 $\pi_-$，得到
$$
(B^r)^*B^r\le\|R\|^2T^*T.
$$
在 (2.1) 的 $g$ 上取二次型，右边为零而左边严格正，矛盾。这证明 (1.1) 的第一式。

整个论证没有使用 $\pi_-(R)$；该符号不必有定义。这里只把完全位于已知 $C^*$ 代数中的全空间正序送入另一个 $*$ 表示，不涉及未知不变限制的表示迁移。

若反设 $\operatorname{Ran}A^r\subseteq\operatorname{Ran}S$，则
$$
R=S^{-1}A^r:H\longrightarrow H
$$
处处定义，且因 $S$ 有界单射而图闭：$x_n\to x$、$Rx_n\to y$ 蕴含 $Sy=A^rx$，即 $y=Rx$。闭图定理给 $R$ 有界，与已证第一式矛盾。于是 (1.1) 全部成立。

同理，若 $f$ 在零点附近全纯且非零，则
$$
f(A)=A^rU,\qquad U\in\mathcal A\ \text{可逆}
$$
对某个 $r\ge0$ 成立，所以 $f(A)\notin SB(H)$。这里说的是通常的全纯函数演算，不将一般范数闭慢符号当作收敛解析芽。

## 3. 真实有限头及固定长度链

以下独立证明 (1.2)，不用边界核向量 $g$。

沿用 [R253 第二附录](R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md) 的记号。令
$$
a_j=(j+1)^{-2},\qquad
\beta_m=\sum_{j\ge m}a_j,\qquad
\frac1{m+1}\le\beta_m\le\frac1m,
$$
$$
\varepsilon_m=e^{-77016^{m-1}}\qquad(m\ge1).
$$
在前 $m$ 位的真实有限头上，令 $B_m$ 为截断 $A$，$T_m$ 为对应 $S$ 的截断。实际尾为
$$
U_m=\sum_{j\ge m}a_jN_j
\quad\text{或}\quad
U_m=\sum_{j\ge m}a_jY_j,
$$
在张量分解中只写其尾作用。真实 carry 展开及 Cayley 逆差给
$$
\left\|S-(T_m\otimes I+I\otimes U_m)\right\|
\le9a_\Sigma\varepsilon_m,\qquad
\|U_m\|\le3\beta_m.
\tag{3.1}
$$
同一物理截断有
$$
\|A-B_m\otimes I\|=\alpha_m\le\alpha_0\varepsilon_m,
\qquad \|A\|,\|B_m\|\le\alpha_0.
\tag{3.2}
$$

令 $d=2^m$，将头基倒序记为
$\epsilon_n^{(m)}=e_{d-1-n}^{(m)}$。准确有
$$
B_m\epsilon_n^{(m)}
=\alpha_{v_2(n)}\epsilon_{n-1}^{(m)}\quad(n\ge1),
\qquad B_m\epsilon_0^{(m)}=0.
$$
每个固定长度末端块不随充分大的 $m$ 改变，并且
$$
T_m=c_1B_m+\sum_{k=2}^{d-1}c_kB_m^k,
\qquad c_1=a_0/d_0\ne0.
\tag{3.3}
$$
不要求这个形式标量级数在任何圆盘收敛，只使用有限头的准确多项式恒等式。

固定 $r\ge1$。依次解有限三角系统，可选择
$$
\xi_0=\epsilon_0,\qquad
\operatorname{supp}\xi_k\subseteq\{0,\ldots,k\},\qquad
T_mJ_m\xi_k=J_m\xi_{k-1}\quad(1\le k\le r),
\tag{3.4}
$$
其中 $J_m$ 是相容末端嵌入。$\xi_k$ 及其范数只依赖固定 $k$，不依赖充分大的 $m$。具体地，$T$ 从
$\operatorname{span}\{\epsilon_1,\ldots,\epsilon_k\}$
到
$\operatorname{span}\{\epsilon_0,\ldots,\epsilon_{k-1}\}$
的对角元是 $c_1\alpha_{v_2(n)}\ne0$，因此递归可解。

在 $\operatorname{span}\{\epsilon_0^{(m)},\ldots,\epsilon_r^{(m)}\}$ 上，
$B_m^{r+1}=0$，所以 (3.3) 直接给
$$
T_m^r=c_1^rB_m^r.
$$
结合 (3.4)，得到
$$
\boxed{
B_m^rJ_m\xi_k=0\ (k<r),\qquad
B_m^rJ_m\xi_r=c_1^{-r}J_m\xi_0.
}
\tag{3.5}
$$
这只需要一个固定有限链，不使用任何无界形式逆级数。

## 4. 尾的固定幂有多项式真空下界

置 $D_m=\sum_{j\ge m}a_jE_j$。实际局部误差给
$$
\|U_m-D_m\|\le4\beta_m\eta_m,\qquad
\eta_m\le e^{-77016^m}.
$$
故对固定 $r$，
$$
\|U_m^r-D_m^r\|
\le4r3^{r-1}\beta_m^r\eta_m.
\tag{4.1}
$$

令 $p_j=a_j/\beta_m$。从 $\beta_m\ge1/(m+1)$ 得
$$
\max_{j\ge m}p_j\le\frac1{m+1}.
$$
对按分布 $(p_j)$ 独立抽取的 $r$ 个位置，任一指定两次碰撞的概率为
$\sum_jp_j^2\le1/(m+1)$。并集界给全部互异的概率至少
$$
1-\binom r2/(m+1).
$$
纯生成元不同位交换、同位平方为零，且真空单点矩为 $1/2$，所以
$$
\omega_m(D_m^r)
=2^{-r}\beta_m^r
\,\mathbb P(\text{$r$ 次抽取全部互异})
\ge2^{-r-1}\beta_m^r
$$
对充分大的 $m$ 成立。再用 (4.1)，得
$$
\boxed{
\|U_m^r\Omega_m\|
\ge|\omega_m(U_m^r)|
\ge2^{-r-2}\beta_m^r.
}
\tag{4.2}
$$
$Y$ 情形不需要假定整个算子保正；只有比较用的纯 $D_m$ 展开为正，实际误差已独立扣除。

## 5. 同一向量上的精确首行与线性比率

令
$$
v_m=\sum_{k=0}^r(-1)^kJ_m\xi_k\otimes U_m^k\Omega_m.
\tag{5.1}
$$
由 $\|U_m\|\to0$，有 $\|v_m\|\to1$。真实模型望远镜给
$$
(T_m\otimes I+I\otimes U_m)v_m
=(-1)^rJ_m\xi_r\otimes U_m^{r+1}\Omega_m.
$$
结合 (3.1)，对固定 $r$ 有
$$
\|Sv_m\|
\le\|\xi_r\|(3\beta_m)^{r+1}
+9a_\Sigma\varepsilon_m\|v_m\|
\le C_r\beta_m^{r+1}
\tag{5.2}
$$
对充分大的 $m$ 成立。

另一方面，(3.5) 使所有 $k<r$ 项准确消失：
$$
\boxed{
(B_m^r\otimes I)v_m
=(-1)^rc_1^{-r}J_m\xi_0\otimes U_m^r\Omega_m.
}
\tag{5.3}
$$
由 (3.2) 的幂差望远镜，
$$
\|A^r-B_m^r\otimes I\|
\le r\alpha_0^{r-1}\alpha_m
\le r\alpha_0^r\varepsilon_m.
$$
用 (4.2)、$\|v_m\|\to1$，并支付双指数小于任何固定 $\beta_m$ 幂的误差，得到
$$
\|A^rv_m\|\ge c'_r\beta_m^r
\tag{5.4}
$$
对某个 $c'_r>0$ 及所有充分大的 $m$ 成立。

$S$ 单射且 $v_m\ne0$，故分母非零。(5.2)–(5.4) 给
$$
\frac{\|A^rv_m\|}{\|Sv_m\|}
\ge\frac{c'_r}{C_r\beta_m}
\ge c_rm.
$$
取 $z_m=v_m/\|v_m\|$ 即得 (1.2)。这也独立排除任意可能的估计
$\|A^rx\|\le C\|Sx\|$。

## 6. 排除 R253 中造尾幂或单个 Cayley 因子的捷径

固定 R253 的 $m$，写
$$
P_m=\prod_{\zeta^{2^m}=1}\gamma_\zeta(S)
=S\,R_m=I_{<m}\otimes Q_m,
\qquad
R_m=\prod_{\substack{\zeta^{2^m}=1\\\zeta\ne1}}\gamma_\zeta(S)
\in\mathcal A.
$$
若存在任意有界尾算子 $F$ 使
$$
Q_mF=\widehat N_m^{\,r}\qquad(r\ge1),
$$
将其张量提升到原空间，利用
$I_{<m}\otimes\widehat N_m=A^{2^m}/d_m$，得到
$$
A^{r2^m}
=S\bigl[d_m^rR_m(I_{<m}\otimes F)\bigr],
$$
与 (1.1) 矛盾。提升只需 $I\otimes F$ 有界，不必额外将它送入边界或先证明它与原 $A$ 交换。

同样，若 $j\ge m$，尾中的单个实际 Cayley 因子提升为
$$
Y_j=N_j(I+N_j)^{-1}.
$$
若 $Q_mF=\widehat Y_j$，则原空间上
$$
Y_j=S R_m(I\otimes F).
$$
右乘有界单位 $I+N_j$，再乘标量 $d_j$，给
$$
A^{2^j}
=S\bigl[d_jR_m(I\otimes F)(I+N_j)\bigr],
$$
仍与 (1.1) 矛盾。因此这些等式甚至不能通过放宽到任意 $B(H_{\ge m})$ 右因子来实现。

本节只排除造一个尾幂、单个 $Y_j$ 或通常全纯单位倍数的候选。它不排除一般 $Q_mF$，不排除无穷正预解式强单位作为另一个有界因式，也不决定
$$
q_m=\sup_{\|Q_mF\|\le1}|\omega_m(Q_mF)|
$$
的非消失下界。原正常湮灭者排除和普通 ISP 继续保持开放。
