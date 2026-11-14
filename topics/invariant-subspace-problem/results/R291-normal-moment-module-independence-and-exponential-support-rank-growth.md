# R291：正常湮灭者的真实头矩模独立性与指数支撑秩下界

2026-11-14，normal-annihilator / 789f。**状态：以下结论已证明；一般有限秩正常见证与普通ISP仍开。**

本稿继续 [R290](R290-mixed-finite-head-product-and-physical-block-diagonal-normal-annihilator-exclusion.md)的实际混合头消元，处理一般有关联的正常密度。关键是先证明正常泛函对真实尾多项式没有挠，再只在代数意义上扩张标量。原慢符号的余数系数始终是实际代数作用，绝不当成有理函数。所有用于分离分支的单位均从原范数代数中的真实单位及其真实逆运输。

## 1. 结论与原实际对象

在原 Haar 模型或任意一个真实尾上，记当前生成元为 $T$，

$$
\mathcal B=\overline{\mathbb C[I,T]}^{\|\cdot\|}.
$$

取 $S\in\mathcal B$，其字符为零且首形式阶为一。原 $S_N,S_Y$ 以及 R253 得到的每个相容消元尾符号均属于此范围。

固定 $M\ge1$、$q=2^M$ 的物理头。原分解为 $H=\mathbb C^q\otimes H_{\rm far}$，且

$$
T=J(z)=\sum_{i=1}^{q-1}c_i e_{i,i-1}\otimes I
+\beta^{-1}e_{0,q-1}\otimes z,
\qquad \beta=\prod_{i=1}^{q-1}c_i>0,
$$

$$
T^q=I_q\otimes z.
\tag{1.1}
$$

$z$ 是远尾实际生成元的正标量倍数，远尾范数代数记为

$$
R=\overline{\mathbb C[I,z]}^{\|\cdot\|}.
$$

[R124 §2 的准确余数分解](R124-dyadic-residue-factorization-and-order-one-kernels.md)给

$$
\mathcal B=\bigoplus_{r=0}^{q-1}T^rR,
\qquad
S=\sum_{r=0}^{q-1}T^rb_r,\quad b_r\in R,
\quad b_1\in R^\times.
\tag{1.2}
$$

上式把 $R$ 识别为 $I_q\otimes R$；这是原有界算子代数的真实自由模，不是只在形式级数层面的展开。

**主定理。** 若迹类 $\rho$ 满足

$$
\operatorname{Tr}\rho\ne0,\qquad
\operatorname{Tr}(\rho SG)=0\quad(G\in\mathcal B),
\tag{1.3}
$$

则在这个固定头尾切分上，$\rho$ 的算子 Schmidt 秩至少为 $q$。这里算子 Schmidt 秩指最少需要多少项的表示

$$
\rho=\sum_{\ell=1}^{k}\sigma_\ell\otimes\nu_\ell,
\qquad \sigma_\ell\in M_q(\mathbb C),\quad
\nu_\ell\in\mathcal S_1(H_{\rm far}).
\tag{1.4}
$$

它与 $\rho$ 本身的算子秩不同。

若进一步 $\rho\ge0$、非零，头边缘秩为 $h$，尾边缘秩为 $d<\infty$，则

$$
\boxed{h^2\ge q,\qquad d^2\ge q.}
\tag{1.5}
$$

$d=\infty$ 时尾秩下界按通常方式理解。所有结论均针对真实正常湮灭密度；它们不从任意正常态的尾近似或低熵单独推出。

## 2. 正常尾泛函模对非零多项式无挠

令 $V$ 为全部迹类在 $R$ 上的限制组成的复向量空间：

$$
V=\{\varphi_\nu|_R:\nu\in\mathcal S_1(H_{\rm far})\},
\qquad \varphi_\nu(F)=\operatorname{Tr}(\nu F).
$$

只把相同限制认作同一元素。$V$ 是 $R$ 的模，作用规定为

$$
(b\varphi)(F)=\varphi(bF).
\tag{2.1}
$$

它仍由迹类 $\nu b$ 表示。$R$ 交换，因此所有这些模作用彼此交换。

实际 $z$ 非幂零且拟幂零，所以 $\mathbb C[z]$ 真正是一份多项式环。任何非零多项式都可写成

$$
p(z)=z^d u(z),\qquad u(0)\ne0.
$$

$u(z)$ 在原 $R$ 中可逆；例如将 $u$ 分解为有限个非零根对应的一次因子，再对拟幂零 $z$ 用收敛预解式即可。

**引理 2.1。** 每个 $0\ne p\in\mathbb C[z]$ 在 $V$ 上的作用都单射。

**证明。** 若 $p\varphi=0$，先用真实 $u(z)^{-1}$ 得到 $z^d\varphi=0$。固定 $F\in R$。当 $2^n\ge d$ 时，

$$
0=\varphi\left(z^d\frac{z^{2^n-d}F}{\|z^{2^n}\|}\right)
=\varphi\left(\frac{z^{2^n}}{\|z^{2^n}\|}F\right).
$$

[R12 的原归一化幂](R12-normalized-powers-and-compact-commutant.md)在这个真实尾上范数为 $1$，且 WOT 趋 $I/2$。对表示 $\varphi$ 的固定迹类取极限，得到 $\varphi(F)=0$。此处右来源可以随 $n$ 增长，但最后取极限的输出一致有界。对每个固定 $F$ 适用，故 $\varphi=0$。$\square$

因此可以无损地把标量扩成域

$$
K=\mathbb C(z),\qquad V_K=K\otimes_{\mathbb C[z]}V,
\tag{2.2}
$$

且 $V\to V_K$ 单射。这是有限分母的代数局部化；没有在 $H_{\rm far}$ 上定义一个有界的 $z^{-1}$。

## 3. 真实单位的根扩张与分支差

取

$$
L=K(\lambda),\qquad \lambda^q=z.
\tag{3.1}
$$

$x^q-z$ 在 $K[x]$ 中不可约：在 $\mathbb C[z][x]$ 对素元 $z$ 用 Eisenstein，再用 Gauss 引理即可。故 $[L:K]=q$，且 $L=\mathbb C(\lambda)$。复数域包含所有 $q$ 次单位根，Galois 作用为 $\lambda\mapsto\zeta\lambda$。

置

$$
R_L=L\otimes_{\mathbb C[z]}R,\qquad
V_L=L\otimes_KV_K.
\tag{3.2}
$$

$V_L$ 是交换环 $R_L$ 的模，也是 $L$ 向量空间。$V_K\to V_L$ 单射，例如用 $1,\lambda,\ldots,\lambda^{q-1}$ 作 $K$ 基即可看出。$b_r$ 在这里始终作为 $R_L$ 元素作用于 $V_L$；没有把它们放进 $K$ 或 $L$。

由 (1.2) 的真实唯一余数表示，有 $R$ 代数同构

$$
\mathcal B\simeq R[t]/(t^q-z),\qquad T\leftrightarrow t.
\tag{3.3}
$$

因此代入 $t=\lambda$ 定义一个真正的代数同态

$$
\Theta:\mathcal B\longrightarrow R_L.
\tag{3.4}
$$

特别，原 $\mathcal B$ 中的任意单位和它的真实逆同时被运输，像仍为 $R_L$ 的单位。$\lambda$ 只是本节的代数扩张符号；这里没有断言远尾上存在有界 $q$ 次根。

对每个 $\zeta^q=1$ 定义

$$
s_\zeta=\sum_{r=0}^{q-1}(\zeta\lambda)^r b_r\in R_L.
\tag{3.5}
$$

原 dyadic gauge 固定 $R$ 并把 $T$ 变为 $\zeta T$，所以 $s_\zeta=\Theta(\gamma_\zeta(S))$。

**引理 3.1。** 对 $\zeta\ne\xi$，$s_\zeta-s_\xi$ 是 $R_L$ 的单位。

**证明。** [R124 §3 的真实首阶一旋转差](R124-dyadic-residue-factorization-and-order-one-kernels.md)给

$$
\gamma_\zeta(S)-\gamma_\xi(S)=T U_{\zeta,\xi},
\qquad U_{\zeta,\xi}\in\mathcal B^\times.
$$

这可以直接由对 $\zeta/\xi$ 的旋转差再施 $\gamma_\xi$ 得到。经 (3.4) 运输，

$$
\boxed{s_\zeta-s_\xi=\lambda\Theta(U_{\zeta,\xi})\in R_L^\times.}
\tag{3.6}
$$

$\lambda\in L^\times$，而 $\Theta(U^{-1})$ 是第二个因子的真实代数逆。证明没有以“形式首项非零”代替可逆性。$\square$

## 4. 一般模中的核分离引理

**引理 4.1。** 在一个交换环 $\mathfrak R$ 的模 $\mathfrak V$ 中，设 $s_1,\ldots,s_q\in\mathfrak R$，所有差 $s_i-s_j$ 都为单位。若 $v_i\in\ker s_i$，则这些核的和为直和：

$$
v_1+\cdots+v_q=0\quad\Longrightarrow\quad v_i=0\ (1\le i\le q).
\tag{4.1}
$$

**证明。** 固定 $i$，对零和作用 $\prod_{j\ne i}s_j$。每个 $v_j$（$j\ne i$）被其中的 $s_j$ 杀掉，而在 $v_i$ 上，乘积等于 $\prod_{j\ne i}(s_j-s_i)$。这是一串单位的乘积，所以 $v_i=0$。$\square$

特别可以用于 $\mathfrak R=R_L$、$\mathfrak V=V_L$，且允许各 $v_i$ 先乘任意非零的 $L$ 标量。

## 5. 原 q 个头矩泛函在 K 上必须线性独立

对 (1.3) 的原 $\rho$ 定义，$0\le k<q$，

$$
\psi_k(F)=\operatorname{Tr}\bigl[\rho T^k(I_q\otimes F)\bigr]
\qquad(F\in R).
\tag{5.1}
$$

它们属于 $V$，因为 $\rho T^k$ 的有限头部分迹是迹类。延拓指标时，原 $T^q=I_q\otimes z$ 给

$$
\psi_{k+q}=z\psi_k.
\tag{5.2}
$$

令 $C_q$ 是此矩递推的 companion 矩阵：

$$
(C_q v)_k=v_{k+1}\quad(0\le k<q-1),\qquad
(C_qv)_{q-1}=zv_0.
$$

它满足 $C_q^q=zI$。它仅组织矩递推；不是把物理头换成另一个 Hilbert 度量。

原右源 $G=T^k(I_q\otimes F)$ 全部属于 $\mathcal B$。用 (1.2)、(5.1)、(5.2)，湮灭条件正是

$$
\boxed{\left(\sum_{r=0}^{q-1}b_r C_q^r\right)\psi=0,
\qquad \psi=(\psi_0,\ldots,\psi_{q-1})^{\mathsf T}.}
\tag{5.3}
$$

$C_q$ 的 $K$ 系数与各 $b_r$ 的模作用交换，但 $b_r$ 不被当作 $K$ 标量。

**定理 5.1。** $\psi_0,\ldots,\psi_{q-1}$ 在 $V_K$ 中 $K$ 线性独立。

**证明。** 反设存在不全为零的 $a_0,\ldots,a_{q-1}\in K$ 使

$$
\sum_{k=0}^{q-1}a_k\psi_k=0.
\tag{5.4}
$$

在 $L$ 中，$C_q$ 的特征向量为

$$
e_\zeta=(1,\zeta\lambda,\ldots,(\zeta\lambda)^{q-1})^{\mathsf T},
\qquad \zeta^q=1.
$$

这些向量组成可逆 Vandermonde 矩阵，所以在 $V_L$ 上可唯一写

$$
\psi=\sum_{\zeta^q=1}e_\zeta\,v_\zeta.
$$

(5.3) 精确给 $s_\zeta v_\zeta=0$。把它代入 (5.4)，得到

$$
\sum_{\zeta^q=1}c_\zeta v_\zeta=0,
\qquad
c_\zeta=\sum_{k=0}^{q-1}a_k(\zeta\lambda)^k.
\tag{5.5}
$$

每个 $c_\zeta$ 都非零：否则一个次数小于 $q$ 的非零 $K$ 多项式在 $\zeta\lambda$ 取零，违反其最小多项式 $x^q-z$ 的不可约性。等价地，一个 $K$ 上的真子空间不能包含一条 companion 特征线，否则其全部 Galois 共轭特征线都落入其中并张成 $q$ 维。

现在 $c_\zeta v_\zeta\in\ker s_\zeta$。由引理 3.1、4.1，(5.5) 迫所有 $c_\zeta v_\zeta=0$；因 $c_\zeta\in L^\times$，所有 $v_\zeta=0$。故 $\psi=0$ 于 $V_L$。两次标量扩张都单射，所以 $\psi_0=0$ 于原 $V$。但

$$
\psi_0(I)=\operatorname{Tr}\rho\ne0,
$$

矛盾。$\square$

整个证明只作固定 $q$ 的有限个代数操作。局部化可以有增长的分母，但其合法性来自第 2 节的原正常无挠性；没有对未知正常向量直接作用无界 $z^{-1}$，也没有把抽象根 $\lambda$ 当成尾上的新有界来源。

## 6. 算子 Schmidt 秩与正边缘的真实支撑下界

若有 (1.4) 的 $k$ 项表示，则原物理头矩给

$$
\psi_j=\sum_{\ell=1}^k m_{\ell,j}(z)\varphi_{\nu_\ell},
\qquad m_{\ell,j}(z)=\operatorname{Tr}(\sigma_\ell J(z)^j)\in\mathbb C[z].
\tag{6.1}
$$

这里保留 (1.1) 的全部原头权，未作未运输的头相似。于是这 $q$ 个 $\psi_j$ 在 $V_K$ 中落在至多 $k$ 维的 $K$ 线性包内。由定理 5.1，必须 $k\ge q$，主定理第一部分得证。

现在设 $\rho\ge0$。若远尾边缘的支撑为 $d$ 维子空间 $E$，正性给

$$
\rho=(I_q\otimes P_E)\rho(I_q\otimes P_E).
$$

这是因为 $\operatorname{Tr}\rho(I_q\otimes(I-P_E))=0$，故该投影乘 $\rho^{1/2}$ 为零。取 $E$ 的一组正交基 $u_1,\ldots,u_d$，即可准确写成

$$
\rho=\sum_{a,b=1}^d\sigma_{ab}\otimes|u_a\rangle\langle u_b|.
$$

因此 $k\le d^2$，给 $d^2\ge q$。头边缘的支撑若维数为 $h$，同一个正性论证后按头支撑矩阵单位展开给 $k\le h^2$，所以 $h^2\ge q$。这个论证没有把普通密度秩 $\operatorname{rank}\rho$ 误当成算子 Schmidt 秩。

## 7. 同一正相容链的指数秩增长

设原非零正正常密度 $\rho$ 湮灭 $S_N\mathcal B$ 或 $S_Y\mathcal B$。[R253](R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)沿同一密度给实际相容尾链

$$
\nu_j=\operatorname{Tr}_{<j}\rho,
\qquad \operatorname{Tr}(\nu_j Q_jR)=0\quad(R\in\mathcal B_j),
$$

且每个 $Q_j$ 在当前真实尾上首形式阶为一。对任意 $j\ge0$、任意块长 $M\ge1$，将主定理用于 $\nu_j$ 的前 $M$ 位，得到

$$
\boxed{
\operatorname{rank}\rho_{[j,j+M)}\ge\left\lceil2^{M/2}\right\rceil,
\qquad
\operatorname{rank}\nu_{j+M}\ge\left\lceil2^{M/2}\right\rceil.}
\tag{7.1}
$$

$\rho_{[j,j+M)}$ 是原密度的真实连续块约化态。特别，取 $j=0$，

$$
\boxed{\operatorname{rank}\nu_m\ge\left\lceil2^{m/2}\right\rceil.}
\tag{7.2}
$$

对原纯态 $\rho=|f\rangle\langle f|$，这就是每次切分的实际 Schmidt 秩下界。因而排除所有沿无穷深切分具有统一有限 Schmidt 秩的向量作为正秩一湮灭见证；更一般，任何切分尾秩增长指数严格低于 $(\log2)/2$ 的候选链都被排除。

[R289](R289-finite-rank-tail-entropy-density-and-compatible-arbitrarily-slow-rank-two-chains.md)的字符串向量 $f=\sum b_n\chi_{[0,n)}$ 在每次切分的 Schmidt 秩至多二，所以取 $m=3$（$q=8$）已经违反 (7.2)，明确不是实际正秩一湮灭者。这里用的是新证明的真实右零式后果，不是仅凭该向量低熵而下结论。

若原 $\rho$ 的秩为 $r<\infty$，旧上界与本稿下界合起来仍只给

$$
\left\lceil2^{m/2}\right\rceil\le\operatorname{rank}\nu_m\le r2^m.
$$

二者不矛盾。很小的正特征值可以使支撑秩很大而熵很小；所以本稿没有推出熵正密度，仍与 R289 的一般 $\mathsf S(\nu_m)=o(m)$ 相容。要继续排除全部有限秩见证，还需来自真实方程的定量谱质量约束。

## 8. 量词与来源预算

R290 的张量乘积态结论作为算子 Schmidt 秩一的特例被包含；R290 另保留了明确的头矩行列式阶和实际 adjugate 消元。本稿的新范围是一般有关联的密度及其指数支撑下界，不重新计数旧纯头或混合乘积情况。

本稿不假定 $b_r\in\mathbb C(z)$，不把不变限制、UHF 比较或纯模型的范数搬入实际正常见证；没有把有限支撑压缩当成乘法表示，也没有用有限维 Cayley–Hamilton 代替原全右测试。抽象扩域只用于固定 $q$ 的模恒等式，实际单位来源、它们的逆以及正常无挠性的统一有界输出均已分别支付。普通 Hilbert ISP 与一般有限秩正常见证仍未完成。
