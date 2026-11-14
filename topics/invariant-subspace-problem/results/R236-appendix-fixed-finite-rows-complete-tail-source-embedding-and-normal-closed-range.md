# R236 附录：固定有限原行的完整远尾源嵌入、正常闭像与弱极限

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

**状态：完整纯远尾右因子类的结论。** 固定有限个原范数代数行，可以在一个固定真实头上建立完全有界左逆。所有足够远的完整尾交换子右系数均受同一源范数控制；每层源像正常闭，递减交恰为这些固定行的线性包。对于两个指定慢行，给出显式单位费和最优的柱锚指数。原低头依赖右源、完整理想及正常见证仍开放。

## 1. 原代数与定理

保持原 Haar 表示
$$H=K_n\otimes H_n,\qquad K_n=(\mathbb C^2)^{\otimes n},$$
$$\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\quad
\mathcal B_n=\overline{\mathbb C[I,\widehat N_n]}^{\|\cdot\|},\quad
\mathcal C_n=\{\widehat N_n\}' .$$
把完整尾交换子提升到原 $H$ 后记为
$$\mathcal T_P=I_{<P}\otimes\mathcal C_P.$$
全部 $\widehat N$、进位和物理度量均是原模型。

所用真实身份为：

- [R124](R124-dyadic-residue-factorization-and-order-one-kernels.md) §2：若 $q=2^n$，每个 $S\in\mathcal A$ 有准确有限余数分解
  $$S=\sum_{0\le r<q}A^r(I_{<n}\otimes b_{r,n}(S)),\quad b_{r,n}(S)\in\mathcal B_n.$$
  对物理余数基 $\varepsilon_r$，
  $$A^r(\varepsilon_0\otimes u)=W_r\varepsilon_r\otimes u,\quad W_r>0,$$
  且 $\chi_n(b_{r,n}(S))=c_r(S)$。
- [R253](R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md) §§1、3 给原 $\mathcal B_n$ 的等距识别，并明确使用 R32 的单射代数同态
  $$S\longmapsto\sum_{r\ge0}c_r(S)z^r.$$

这些身份只按原 $\mathcal A$ 范围使用，不扩到任意 $\mathcal A'$ 行。

**定理。** 对固定线性无关 $S_1,\ldots,S_d\in\mathcal A$，存在固定 $n$ 和真实
$$U\in M_d(\mathcal B_n)^\times,\qquad C_S=\|U^{-1}\|<\infty,$$
使对全部 $P\ge n$、全部 $G_i\in\mathcal T_P$，
$$\boxed{\|\operatorname{col}_iG_i\|
\le C_S\left\|\sum_iS_iG_i\right\|.}\tag{1.1}$$
同一常数对每个有限矩阵放大成立。它依赖固定原行和固定头，不声称对移动行一致。

## 2. 常数字符矩阵的非退化与真正单位

由形式同态单射，系数行
$$(c_r(S_1),\ldots,c_r(S_d)),\qquad r\ge0,$$
张成 $\mathbb C^d$。否则一个非零线性组合的全部形式系数为零，便与原行线性无关矛盾。选择互异 $r_1,\ldots,r_d$ 使
$$C=(c_{r_\ell}(S_i))_{\ell,i}$$
可逆，并取 $2^n>\max r_\ell$。

定义真实物理首列条目
$$U_{\ell i}=W_{r_\ell}b_{r_\ell,n}(S_i)\in\mathcal B_n.$$
全部实际进位在这些尾系数内，未被删除。其字符矩阵为
$$\chi_n(U)=\operatorname{diag}(W_{r_\ell})C,$$
所以 $\det\chi_n(U)\ne0$。

$\mathcal B_n$ 是由拟幂零 $\widehat N_n$ 单生成的交换幺 Banach 代数。任何字符在生成元上取零，且多项式稠密，故只有常数字符 $\chi_n$。因此 $\det U$ 是该原 $\mathcal B_n$ 中的单位，
$$U^{-1}=(\det U)^{-1}\operatorname{adj}U\in M_d(\mathcal B_n).$$
未在更大代数求逆后声称它属于 $\mathcal B_n$。若
$M=\max(1,\|S_1\|,\ldots,\|S_d\|)$，各条目是原压缩，粗估可写
$$C_S\le d!M^{d-1}\|(\det U)^{-1}\|.$$
真实 $W_r$ 的小量已经在 $\det U$ 中，不能从费用中删掉。

## 3. 完整尾右因子、完全有界费用与正常左逆

原递推
$$N_j=\begin{pmatrix}0&\eta_jN_{j+1}\\I&0\end{pmatrix}$$
说明：若 $G$ 只作用于 $\ge P$ 尾且与 $N_P$ 交换，其提升便与每个较低 $N_j$、特别与 $A$ 交换。因此
$$\mathcal T_P\subset\mathcal A',\qquad
I_{[n,P)}\otimes\mathcal C_P\subset\mathcal C_n.$$
$U,U^{-1}$ 的条目属于 $\mathcal B_n$，故与这些实际右因子交换；不同 $G_i$ 不必彼此交换。

对 $J=\sum_iS_iG_i$，从物理头 $\varepsilon_0$ 输入列抽取 $r_1,\ldots,r_d$ 输出，记为 $\mathcal L_n(J)$。因为 $G_i$ 在前 $n$ 位为恒等，准确有
$$\mathcal L_n(J)=U\operatorname{col}_iG_i,\qquad
\|\mathcal L_n(J)\|\le\|J\|.$$
乘真正 $U^{-1}$ 即得 (1.1)。抽取列完全收缩，且
$\|U^{-1}\otimes I_k\|=C_S$，所以矩阵放大常数相同。

定义固定左逆
$$\mathcal R(J)=U^{-1}\mathcal L_n(J).$$
每个分量都是固定块压缩和固定有界左乘的有限和，故对 WOT、ultraweak 均连续。相应源映射
$$\mathcal L(G)=\sum_iS_i(I_{<n}\otimes G_i)$$
也正常连续。事实上 $\mathcal R\mathcal L=I$ 对任意原 $n$ 尾算子系数成立；不需要系数彼此交换。整个左逆是实际有界算子，不是无预算的形式逆。

## 4. 每层源像闭合、递减交与全部弱极限

令
$$\mathcal W_P=\sum_iS_i\mathcal T_P,\qquad P\ge n.$$
$J\in\mathcal W_P$ 当且仅当
$$J=\mathcal L\mathcal R(J),\qquad
\mathcal R_i(J)\in I_{[n,P)}\otimes\mathcal C_P\quad\text{对每个 }i.$$
右边是正常连续等式与 WOT/ultraweak 闭子空间条件，故 $\mathcal W_P$ 同时 WOT、ultraweak、范数闭。

$\mathcal T_{P+1}\subset\mathcal T_P$ 给递减源像。若 $J$ 属于全部 $\mathcal W_P$，固定左逆给同一组唯一系数，属于全部尾的交。该交恰为 $\mathbb CI$：一个算子在每个有限头上为恒等，作用于参考真空后只能在所有有限头均为真空的一维交中；它又与全部有限头矩阵交换，而真空对这些矩阵循环，故为同一标量恒等。于是
$$\boxed{\bigcap_{P\ge n}\mathcal W_P
=\operatorname{span}_{\mathbb C}\{S_1,\ldots,S_d\}.}\tag{4.1}$$
固定 $k$ 阶放大时，右边换成该线性包张量 $M_k$。

若 $P_\ell\to\infty$ 且
$J_\ell=\sum_iS_iG_{i,\ell}$ 一致有界，(1.1) 迫各真实系数一致有界。令
$$\alpha_{i,\ell}=\langle G_{i,\ell}\Omega_{P_\ell},\Omega_{P_\ell}\rangle.$$
在有限 Walsh 头向量上，尾均值恒等准确成立；再用一致有界和稠密性，
$$G_{i,\ell}-\alpha_{i,\ell}I\longrightarrow0\quad\mathrm{WOT},$$
$$\boxed{J_\ell-\sum_i\alpha_{i,\ell}S_i\longrightarrow0\quad\mathrm{WOT}.}\tag{4.2}$$
全部 WOT 聚点因而属于固定有限线性包；均值全零时 $J_\ell\to0$。相同证明适用于有界净。

若 $\chi(S_i)=0$ 对全部 $i$，则 $I$ 不在该包中，故这类纯远尾源没有一致有界弱单位。若原行线性相关，先取固定独立基；源像和弱极限结论不变，但不能控制带冗余的每个原系数。

## 5. 零字符原行与整个尾目标的正距离

若全部 $\chi(S_i)=0$，§2 的 $r_\ell$ 可全取为正数。因此对任意完整 $n$ 尾目标
$$T\in I_{<n}\otimes B(H_n)$$
都有 $\mathcal R(T)=0$，因为所取物理 $(r_\ell,0)$ 条目全为零。

令 $C_0=\|[S_1\ \cdots\ S_d]\|C_S$。对 $J\in\mathcal W_P$，
$$\|J\|=\|\mathcal L\mathcal R(J-T)\|\le C_0\|J-T\|.$$
所以
$$\boxed{\mathcal W_P\cap(I_{<n}\otimes B(H_n))=\{0\},\qquad
\operatorname{dist}(T,\mathcal W_P)\ge\frac{\|T\|}{1+C_0}.}\tag{5.1}$$
这是实际源像和实际目标的距离，非 raw 代表范数代替商距。

进一步，若一个完整实际源
$$T=\sum_iS_iF_i\in I_{<n}\otimes B(H_n),\qquad F_i\in\mathcal A',$$
取原 dyadic 零余数平均 $\mathcal E_n(F_i)$。相位共轭保持 $\mathcal A'$；平均使物理头矩阵对角。它仍与 $A$ 交换，非零相邻头权迫全部对角块相等，最后的真实 carry 迫共同块与 $\widehat N_n$ 交换。因此
$\mathcal E_n(F_i)\in\mathcal T_n$，不需要给任意 $\mathcal A'$ 元素使用形式级数。由 (5.1)，
$$\boxed{\left\|\sum_iS_i(F_i-\mathcal E_nF_i)\right\|
\ge\frac{\|T\|}{1+C_0}.}\tag{5.2}$$
任何非零归一尾目标都必须保留一个实际固定低头源部分。

## 6. 两条原慢行的显式二位单位

每位共同选择 $X_i=N_i$ 或 $Y_i=N_i(I+N_i)^{-1}$，取
$$X=\sum_i a_iX_i,\qquad Y=\sum_i b_iX_i,\qquad
M=\begin{pmatrix}a_0&b_0\\a_1&b_1\end{pmatrix},\quad\det M\ne0.$$
对 $P\ge2$、$G,H\in\mathcal T_P$，在二位物理头抽取
$J=XG+YH$ 的 $(1,0),(2,0)$ 条目。

若 $X_0=N_0$，置 $U_0=I,V_0=0$；若 $X_0=Y_0$，置
$$U_0=(I-\eta_0^2\eta_1N_2)^{-1},\qquad V_0=-\eta_0U_0.$$
若 $X_1=N_1$，置 $U_1=I$；若 $X_1=Y_1$，置
$$U_1=(I-\eta_1N_2)^{-1}.$$
所有单位均在原 $\mathcal B_2$。由
$N_0^4=\eta_0^2\eta_1N_2$、$N_1^2=\eta_1N_2$ 和完整有限几何式
$$Y_0=(N_0-N_0^2+N_0^3-N_0^4)(I-N_0^4)^{-1},$$
$$Y_1=(N_1-N_1^2)(I-N_1^2)^{-1},$$
两条目准确为
$$L M\operatorname{col}(G,H),\qquad
L=\begin{pmatrix}U_0&0\\V_0&U_1\end{pmatrix}.$$
全部 $i\ge2$ 项在二位头上对角，不会进入这两条目，carry 已完整保留。

$L^{-1}$ 的两对角逆范数至多 $1+\eta_1$，非零下角是
$\eta_0U_1^{-1}$。因此
$$\|L^{-1}\|\le(1+\eta_0)(1+\eta_1),$$
$$\boxed{\|J\|\ge
\frac{\sigma_{\min}(M)}{(1+\eta_0)(1+\eta_1)}
\|\operatorname{col}(G,H)\|.}\tag{6.1}$$
纯 $N$ 情形 $L=I$。对指定
$a_i=(i+1)^{-2}$、$b_i=a_i^2$，
$$|\det M|=3/16,\qquad \|M\|_{\rm F}=23/16,\qquad
\sigma_{\min}(M)\ge3/23.$$
所以可取 $C_S\le(23/3)(1+\eta_0)(1+\eta_1)$，纯 $N$ 为 $23/3$。

## 7. 任意算子值、均值零远尾因子的完整柱预算

继续取 §6 的指定两行，允许全部 $G,H\in\mathcal T_P$，只要求各尾均值为零；不要求范数多项式逼近、次数界或输入一致有界。

记
$$\Pi_P=I_{<P}\otimes|\Omega_P\rangle\langle\Omega_P|,$$
$$B_a(P)^2=\sum_{i\ge P}|a_i|^2,\quad
B_b(P)^2=\sum_{i\ge P}|b_i|^2,\quad
s_a(P)=\sum_{i\ge P}|a_i|,\quad s_b(P)=\sum_{i\ge P}|b_i|.$$
原 $\|X_i-E_i\|\le4\eta_i$ 给中心化伴随真空向量的误差
$$\left\|(I-|\Omega_P\rangle\langle\Omega_P|)X_{\rm tail}^*\Omega_P
-\frac12\sum_{i\ge P}\overline{a_i}\chi_i\right\|
\le4\eta_Ps_a(P),$$
$Y$ 行同理。因此完整尾标量
$\kappa=\omega_P(X_{\rm tail}G+Y_{\rm tail}H)$ 满足
$$|\kappa|\le\left\{\frac12\sqrt{B_a(P)^2+B_b(P)^2}
+4\eta_P[s_a(P)+s_b(P)]\right\}
\|\operatorname{col}(G,H)\|.$$
低头先作真正 $P$ 位 carry 截断，每行误差至多
$18\eta_{P-1}$；截头主项因两尾均值零准确消失。两残量作为同一个算子行估计，得到
$$\boxed{\|\Pi_PJ\Pi_P\|
\le v_P\|\operatorname{col}(G,H)\|
\le C_Sv_P\|J\|,}\tag{7.1}$$
$$v_P=\frac12\sqrt{B_a(P)^2+B_b(P)^2}
+4\eta_P[s_a(P)+s_b(P)]+18\sqrt2\,\eta_{P-1}.$$
这保留整个源和整个柱压缩，不用 $\rho$ 的正常尾速度。

指定权给
$$B_a(P)^2\le1/(3P^3),\quad B_b(P)^2\le1/(7P^7),\quad
s_a(P)\le1/P,\quad s_b(P)\le1/(3P^3).$$
故 $v_P=O(P^{-3/2})$。以非零柱锚归一时，该完整纯尾右因子类的源范数费用至少为固定正倍数 $P^{3/2}$，允许 $G,H$ 增长或取完整算子值尾系数也不能绕过它。

[实际 Cayley selector](R236-appendix-polynomial-cylinder-tail-for-all-normal-positive-annihilators.md)取 $H=0$，其实际源范数有界、柱锚为固定正倍数 $P^{-3/2}$，已达到此指数。因此更换同类 selector 不能改善该指数。

## 8. 当前未付范围

所有结论针对固定有限原 $\mathcal A$ 行，以及足够远的完整实际尾交换子右系数。固定一次真实逆及其费用显式保留；未扩到任意 $\mathcal A'$ 行、移动行或移动头逆。

右因子保留低于 $P$ 的头依赖时，源列不再等于 $U\operatorname{col}(G_i)$，不能应用这个左逆。(5.2) 甚至给出该低头部分必须存在的统一下界。原一般低头协同源和完整共同正常见证仍在这个未付部分。

$\mathcal W_P$ 是指定完整尾右模块的源像，不是完整原理想，也不是原理想与尾代数的交。因此其正常闭合及 (4.1) 不宣称原理想正常闭合或普通 ISP 完成。
