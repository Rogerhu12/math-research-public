# R236 附录：同一正常商上删池真右逆的有限总度估计及物理源分解

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：以下实际条件估计已经逐项核验。它精确使用原零式 pi(X)=0 和全部高位 carry，把上一稿的指定真右源在同一个商上的逆成本降到总度 r 的有限公式。没有由商像费用推物理来源费用，完整原 rho 及两种泄漏保留。

依赖：[原相对辅助系数及联合逆](R236-appendix-polynomial-relative-auxiliary-quadratic-exclusion.md)、[指定真右源、完整导子弱单位和正常商泄漏](R236-appendix-actual-right-sources-and-normal-quotient-leakage.md)。

## 1. 原系数、原旗和选中相邻尺度池

沿相对辅助稿的 a_i、b_i、A、a_-、c，保原高位条件 |a_i|≤A(i+1)^(-2)、|a_i|≥a_-(i+1)^(-2)、|b_i/a_i|≥c(i+1)^(-2)，并保 Σ|b_i|<∞；原 X_i 逐位为 N_i 或 Y_i。令 pi 是固定物理旗 N⊂M⊂H^(d) 的正常契约表示，E=M orthogonal-minus N。假设
$$
\pi(X)=0,\qquad X=\sum_i a_iX_i.
$$
本节只需这一条准确零式；若再有 pi(Y)=0，上一稿完整导子余额亦可同时使用。

固定整数 P 充分高，使系数下界均成立。取
$$
F\subseteq\{P,P+1,\ldots,2P-1\},\qquad |F|=r\le P.
$$
写 C_i=pi(X_i)，并令
$$
Z_F=\sum_{i\in F}a_iC_i.
$$
完整原右源为
$$
R_F=\prod_{j\in F}(b_j+2a_jX_F)^{-2}\in\mathcal A,
\qquad X_F=\sum_{i\notin F}a_iX_i.
$$
同一个零式给 pi(X_F)=-Z_F。因此
$$
\boxed{
\pi(R_F)=\left(\prod_{j\in F}b_j^{-2}\right)p_F(Z_F)^{-1},
\qquad
p_F(z)=\prod_{j\in F}(1-\lambda_jz)^2,
\quad\lambda_j=2a_j/b_j.
}
\tag{1.1}
$$
这不是选取一个新的代表；R_F 正是原共同 Laplace 构造的真右源。

## 2. 超过所选位数后每一单项都有真实重复位

由原 N/Y 幂关系和 pi 的契约性，
$$
\|C_i\|\le3,\qquad \|C_i^2\|\le9\eta_i\le9\eta_P.
$$
所有 C_i 交换。令
$$
w_F=3\sum_{i\in F}|a_i|\le\frac{3Ar}{P^2}.
$$
任意 n≥r+1 的 Z_F^n 单项必有一个重复位，交换后提取该位的平方；其范数比普通 3^n 界多一个 eta_P。故
$$
\boxed{\|Z_F^n\|\le\eta_Pw_F^n\qquad(n\ge r+1).}
\tag{2.1}
$$
这里从未令 C_i²=0。有限放大或同一个商不改变这个实际范数界。

又由相对辅助下界，
$$
\lambda_*:=\max_F|\lambda_j|\le\frac{8P^2}{c},
\qquad h_F=\lambda_*w_F\le\frac{24A}{c}r.
\tag{2.2}
$$
记 H_r=max(1,24Ar/c)。

## 3. 整个逆乘积只截一次到总度 r

令 g_r(z) 是 p_F(z)^(-1) 在0处的 r 阶 Taylor 多项式。这个定义只取有限标量系数，随后每一步都有实际余项控制。由
$$
\prod_{j\in F}(1-\lambda_jz)^{-2}
$$
的几何级数系数，
$$
|[z^n]g_r|\le\binom{2r+n-1}{n}\lambda_*^n\quad(0\le n\le r).
$$
于是
$$
\|g_r(Z_F)\|
\le G_r:=(r+1)8^rH_r^r.
\tag{3.1}
$$
p_Fg_r-I 的次数在 r+1 到3r之间。结合 (2.1) 以及标量绝对系数乘积，得到
$$
\boxed{
\|p_F(Z_F)g_r(Z_F)-I\|
\le\eta_P(1+24Ar/c)^{2r}G_r=:e_{P,r}.
}
\tag{3.2}
$$
若显式条件 e_(P,r)≤1/2 成立，实际 Neumann 逆给
$$
\boxed{
\|p_F(Z_F)^{-1}\|\le2G_r.
}
\tag{3.3}
$$
确切地，p_F(Z_F)g_r(Z_F)=I+E，||E||≤1/2；各项同为 Z_F 多项式，故 g_r(Z_F)(I+E)^(-1) 是两侧逆。它必等于 (1.1) 的原单位像的逆，不是形式级数所定义的另一个对象。

由 |b_j|≥a_-c/(2P)^4，最终得到
$$
\boxed{
\|\pi(R_F)\|
\le2(r+1)8^rH_r^r
\frac{(2P)^{8r}}{(a_-c)^{2r}}.
}
\tag{3.4}
$$
对固定原常数，log 右端只有 O(r log r+r log P)。它控制整个 r 元逆平方乘积；逐个使用 r+1 阶几何逆再相乘会多付 O(r² log r)。

条件 (3.2) 是实可检查的原 carry 条件。特别对 r≤P、固定 A/c，足够高 P 时它成立：其正对数为 O(r log(r+1))，而 -log eta_P≥770·16^P。

## 4. 与全域导子弱单位的同一参数兼容

若要把本估计接入前稿的完整实际右源导子，令 r=2^j，并取
$$
\sigma=\min(1/4,\sqrt{c/A}/32),\qquad
P=\lceil\sigma r^2\rceil,
\qquad I_j=\{P,\ldots,2P-1\}.
$$
物理 carry 截断仍在第 j 位；所选高池改放在相邻尺度 [P,2P)，充分高 j 时 P≥j、P≥r。平均池大小为 q=P，故相同 Boolean 平均范数≤exp(1/σ)，WOT趋I。

原真实 R_F 的共同 Laplace 主费为
$$
\frac{256A}{c}(2P)^2.
$$
高 j 时 P≤2σr²，故主费≤4096Aσ²r⁴/c≤4r⁴。原截断 carry 仍给 (770/16)r⁴；所有其余费用仍为 O(r log r)。因此前稿全部实际右源导子结论、同一正常 rho 的非零余额继续有效。

同时 (3.4) 给这个确切源家族在同一商 E 上的明显较小像费用。没有改旗、换 rho 或把原右源换成另一条便宜提升。

## 5. 两种物理源的准确分解

仍将真右算子 R_F 写成原旗三角块
$$
R_F=\begin{pmatrix}
R_N&B_R&D_R\\0&R_E&F_R\\0&0&R_L
\end{pmatrix},\qquad R_E=\pi(R_F).
$$
对同一个固定 rho≥0、tau=Tr rho，有准确 Hilbert–Schmidt 分解
$$
\boxed{
\|R_F\rho^{1/2}\|_{\rm HS}^2
=\|R_E\rho^{1/2}\|_{\rm HS}^2+
 \|B_R\rho^{1/2}\|_{\rm HS}^2,
}
\tag{5.1}
$$
$$
\boxed{
\|R_F^*\rho^{1/2}\|_{\rm HS}^2
=\|R_E^*\rho^{1/2}\|_{\rm HS}^2+
 \|F_R^*\rho^{1/2}\|_{\rm HS}^2.
}
\tag{5.2}
$$
(3.4) 只支付各式第一个平方。实际右源落入 N 的 B_R 分量，及反向落入 M^perp 的 F_R* 分量，均保留在原源列中。

原 X 的商块为0；写其块 A_X、B_X、F_X、G_X。R_F 与 X 真正交换，给
$$
\boxed{
A_XB_R=R_NB_X-B_XR_E,
\qquad
F_RG_X=F_XR_L-R_EF_X.
}
\tag{5.3}
$$
若也有 pi(Y)=0，则同样有 Y 的两条准确式。它们是实际两行来源约束；本文没有除以 A_X 或 G_X，因为未知限制上的相应逆费用仍未支付。

对于前稿中 T=X²+Y，所有中段来源
$$
P_LE_F^*R_FT^s\rho^{1/2}\quad(s\ge1)
$$
中的 T^s rho^(1/2) 落在 N，故实际使用的是 R_N，而非 (3.4) 的 R_E。这是原非零导子余额中尚未控制的明确部分。

本稿用原 pi(X)=0 把指定商像的完整逆预算算清；仍没有把它提升成物理同源范数界，没有推出一般正正常两行湮灭者不存在。
