# R12 后续：实际增生分母的共同全部幂准亲和范数逼近

日期：2026-11-29（Asia/Taipei）。作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。

本稿给出原全部整数幂共同理想中的实际准亲和范数逼近，而不只给强收敛。结合已经证明的非实际整除性，它给出该理想范数闭包中的显式严格新元素。原平方根分子的存在不由这种逼近获得；此前已排除的增生分母平方根类仍保持排除。

## 1. 同一原行、分母和两个理想

固定原 Haar 尾 $C=A^{(m_0)}$，$\mathscr A=\{C\}'$。使用[实际复逆幂](R12-appendix-accretive-complex-inverse-powers-flat-divisibility-layers-and-all-flag-sources.md)的同一原算子：
$$
N_j=C^{2^j}/d_j,\quad d_j=\|C^{2^j}\|,\quad
V_j=(I-N_j)(I+N_j)^{-1},\quad a_j=(j+1)^{-1},
$$
$$
Z=I+\sum_{j\ge0}a_jV_j,\qquad L=Z^{-1},\qquad
P_\theta=Z^{-\theta}\quad(\Re\theta>0).
\tag{1}
$$
$Z$ 是实际闭最大增生算子，$\Re Z\ge I$，有限柱构成其原图核心；$\|L\|\le1$，$L$ 单射且稠密像。全部有界成员属于 $\mathscr A$。此前已付 $P_\theta$ 在每个原普通不变旗的子商上准亲和，并且
$$
P_\theta\notin C\mathscr A.
\tag{2}
$$
后式来自 $\Omega\in\operatorname{Ran}P_\theta$ 与 $\Omega\notin\operatorname{Ran}C$。

记
$$
\mathfrak F=\bigcap_{k\ge1}C^k\mathscr A,\qquad
\mathfrak J=\overline{\mathfrak F}^{\,\|\cdot\|}.
\tag{3}
$$

**定理。** 存在同一列收缩 $R_n\in\mathfrak F$，每个 $R_n$ 都在全部原普通不变旗及固定有限放大旗上准亲和，并满足
$$
R_n\longrightarrow I\quad\mathrm{strong*},\qquad
\|(I-R_n)L\|\longrightarrow0.
\tag{4}
$$
更强地，对每个紧集 $K\Subset\{\Re\theta>0\}$，
$$
\boxed{\sup_{\theta\in K}\|(I-R_n)P_\theta\|\longrightarrow0.}
\tag{5}
$$
因此
$$
\boxed{P_\theta\in\mathfrak J\setminus C\mathscr A
\subseteq\mathfrak J\setminus\mathfrak F
\qquad(\Re\theta>0).}
\tag{6}
$$
(6) 不识别 $\mathfrak J$ 与全部喷射平坦理想。

## 2. 原加权删除和的收缩归一

写原真实进位
$$
N_j=E_j+\eta_j E_j^*N_{j+1},\qquad \|N_j\|=1,
\qquad \eta_j=\alpha_{m_0+j+1}/\alpha_{m_0+j}.
$$
故 $\|N_j-E_j\|\le\eta_j$。对有限 $N$，令
$$
s_N=\sum_{j<N}a_j,\quad
g_N^2=\sum_{j<N}a_j^2,\quad
e_N=\sum_{j<N}a_j\eta_j,\quad
\kappa_N=\sqrt{s_N^2+4g_N^2}+2e_N.
\tag{7}
$$
有 $s_N\to\infty$，$g_N\le g<\infty$，$e_N\le e<\infty$。

需要的加权物理范数界是
$$
\left\|\sum_{j<N}a_jE_j\right\|
\le\frac12\sqrt{s_N^2+4g_N^2}.
\tag{8}
$$
给出一项完整证明。以各位 Pauli 矩阵写
$E_j=(\sigma_j^x+i\sigma_j^y)/2$，并置
$S_x=\sum a_j\sigma_j^x$，$S_y=\sum a_j\sigma_j^y$，
$S_z=\sum a_j\sigma_j^z$。对不同两位，
$\sigma_i^x\sigma_j^x+\sigma_i^y\sigma_j^y+\sigma_i^z\sigma_j^z\le I$：
它在对称三维空间上为 $1$，在反对称一维空间上为 $-3$。
因 $a_j\ge0$，
$$
S_x^2+S_y^2+S_z^2
\le (s_N^2+2g_N^2)I.
$$
又 $[S_x,S_y]=2i\sum a_j^2\sigma_j^z$。展开删除和的模平方，使用
$S_z^2\ge0$ 及 $\|\sum a_j^2\sigma_j^z\|\le g_N^2$，即得 (8)。

保留全部 carry 后，
$$
F_N=\frac2{\kappa_N}\sum_{j<N}a_jN_j
\tag{9}
$$
为真正的收缩。它是同一 $C$ 的有限多项式，并有
$$
F_N=C\,U_N,\qquad U_N(0)=\frac{2a_0}{\kappa_Nd_0}\ne0.
\tag{10}
$$
因为 $C$ 拟幂零，$U_N$ 是原多项式范数闭包中的有界单位。这里没有把 $F_N$ 当成单位。

## 3. 同一 $L$ 上的范数误差

准确 Cayley 恒等式为
$$
I-2N_j=V_j-\Delta_j,\qquad
\Delta_j=2N_j^2(I+N_j)^{-1}.
\tag{11}
$$
原 $N_j^2=\eta_jN_{j+1}$ 与 $\|(I+N_j)^{-1}\|\le3$ 给
$\|\Delta_j\|\le6\eta_j$。因此
$$
I-F_N=
\frac{\kappa_N-s_N}{\kappa_N}I+
\frac1{\kappa_N}\sum_{j<N}a_jV_j
-\frac1{\kappa_N}\sum_{j<N}a_j\Delta_j.
\tag{12}
$$

对每个 $x\in D(Z)$，有真正的形式界
$$
\sum_{j<N}a_j\Re\langle V_jx,x\rangle
\le\Re\langle Zx,x\rangle.
\tag{13}
$$
先在有限柱原核心上用各 $\Re V_j\ge0$ 与完整原行收敛证明，再在 $Z$ 图范数中逼近；每个有限左和是有界形式，所以该延拓合法。

由于 $F_N$ 收缩，
$$
\|(I-F_N)x\|^2
\le2\Re\langle(I-F_N)x,x\rangle.
$$
将 (12)、(13) 代入并取 $x=Lu$，$ZLu=u$，得到全域范数估计
$$
\boxed{
\|(I-F_N)L\|^2
\le\frac2{\kappa_N}
\left[(\kappa_N-s_N+6e_N)\|L\|^2+\|L\|\right].
}
\tag{14}
$$
这里
$$
0\le\kappa_N-s_N\le2g^2/s_N+2e,
$$
所以 (14) 趋零；例如右侧不超过
$2(1+8e+2g^2/s_N)/s_N$。

$\operatorname{Ran}L$ 稠密且 $\|F_N\|\le1$，故 $F_N\to I$ 强。原 $J$ 对称性给 $F_N^*=JF_NJ$，所以实际为强*收敛。关键新增量是 (14) 的算子范数，而非这一强*极限本身。

## 4. 从同一范数误差制造全部幂共同倍数

固定 $\varepsilon>0$。选择严格递增的 $N_r$，使
$$
\sum_{r\ge1}\|(I-F_{N_r})L\|<\varepsilon.
\tag{15}
$$
全部因子相互交换且为收缩。有限乘积
$R^{(m)}=\prod_{r\le m}F_{N_r}$ 满足：对 $m>k$，
$$
\|(R^{(m)}-R^{(k)})L\|
\le\sum_{k<r\le m}\|(I-F_{N_r})L\|.
\tag{16}
$$
这是在同一实际 $L$ 后的望远镜，未用逆费用。

由稠密的 $\operatorname{Ran}L$ 和统一收缩界，$R^{(m)}$ 强*收敛到某个收缩 $R\in\mathscr A$，并且
$$
\|(I-R)L\|<\varepsilon.
\tag{17}
$$
对每个固定 $k$，尾积
$T_k=\mathrm{strong*}\!-\!\lim_m\prod_{k<r\le m}F_{N_r}$
同样存在，$T_k\to I$ 强*，且
$$
R=\left(\prod_{r\le k}F_{N_r}\right)T_k
=C^k\left(\prod_{r\le k}U_{N_r}\right)T_k.
\tag{18}
$$
右侧给真实有界除商，故 $R\in\mathfrak F$。没有把只有闭包范围的因子消去。

还须证明 $R$ 及全部原旗子商的准亲和性。记
$H_k=\prod_{r\le k}F_{N_r}=C^kG_k$，其中 $G_k$ 为有界单位。
对任意 $M$，
$$
W_{k,M}=G_k^{-1}U_M^k
$$
属于原多项式范数闭包，并有
$$
RW_{k,M}=T_k F_M^k.
\tag{19}
$$
右侧是收缩。固定 $k$ 时 $F_M^k\to I$ 强*，随后 $k\to\infty$ 时 $T_k\to I$ 强*。在一个固定稠密可数向量集上取对角子列，(19) 给
$$
RW_\nu=W_\nu R\longrightarrow I\quad\mathrm{strong*},\qquad
\|RW_\nu\|\le1.
\tag{20}
$$
因 $R,W_\nu$ 均保持所有原普通 $C$ 不变旗，(20) 在固定 Hilbert 商代表中仍为收缩强*单位。它逐旗支付 $R$ 的单射和稠密像；同样适用于固定有限放大。特别 $R\ne0$。

令 $\varepsilon=\varepsilon_n\downarrow0$ 分别作上述构造，得到 $R_n$。由 (17) 及 $\operatorname{Ran}L$ 稠密，(4) 成立。

## 5. 同一列逼近全部复分数分母

先取 $0<\Re\alpha<1$。实际复预解积分为
$$
P_\alpha=\frac{\sin\pi\alpha}{\pi}
\int_0^\infty t^{-\alpha}(Z+tI)^{-1}\,dt.
\tag{21}
$$
它由同一个 Gamma 半群积分及向量 Fubini 得到，并在算子范数中绝对收敛。每个实际预解满足
$$
(Z+tI)^{-1}=L(I+tL)^{-1},\quad
\|(Z+tI)^{-1}\|\le(1+t)^{-1},\quad
\|(I+tL)^{-1}\|\le2.
$$
写 $\delta_n=\|(I-R_n)L\|$。于是
$$
\|(I-R_n)(Z+tI)^{-1}\|
\le2\min(\delta_n,(1+t)^{-1}).
\tag{22}
$$
对 $a=\Re\alpha$ 且 $0<\delta_n\le1$，在 $t=1/\delta_n$ 处分段积分给明确费用
$$
\boxed{
\|(I-R_n)P_\alpha\|
\le\frac{2|\sin\pi\alpha|}{\pi}
\left(\frac1a+\frac1{1-a}\right)\delta_n^a.
}
\tag{23}
$$
所以这一收敛在开带内任意紧集上一致。

对任意 $K\Subset\{\Re\theta>0\}$，选择固定整数 $m>\max_K\Re\theta$。
同一实际半群律给 $P_\theta=P_{\theta/m}^{\,m}$。因 $R_n$ 交换，
$$
(I-R_n)P_\theta=
\bigl((I-R_n)P_{\theta/m}\bigr)P_{\theta/m}^{\,m-1}.
$$
后一个幂在 $K$ 上一致有界；(23) 便给 (5)。

每个 $R_nP_\theta$ 属于 $\mathfrak F$，并在每个原旗子商上仍准亲和，因为两个同源因子各自已付单射和稠密像。故 (5) 确实是一列合法共同全部幂来源的范数逼近。结合 (2) 得到 (6)。

## 6. 准确的新增范围

此前已经知道 $\mathfrak F$ 非范数闭，且其闭包包含于全部喷射平坦理想；本稿给出的 $P_\theta$ 是显式的、全旗准亲和的
$\mathfrak J\setminus C\mathscr A$ 元素，并以同一列 $R_n$ 支付完整复参数紧集上的范数逼近。

这没有将 $\mathfrak J$ 变成实际全部幂共同值域，也没有证明 $\mathfrak J$ 等于全喷射平坦理想。尤其原[完整两列四次费用](R12-appendix-full-two-column-quartic-source-cost-and-accretive-denominator-exclusion.md)已经排除 $Y^2=CP_\theta^2$ 的有界分子；本稿并未改变该结论。共同幂来源在范数中逼近这种分母，并不自动给出其平方根分子或给另一共同分母的平方根分子。
