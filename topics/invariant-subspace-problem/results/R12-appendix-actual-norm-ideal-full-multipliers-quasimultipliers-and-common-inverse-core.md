# R12 后续：原交换子的实际范数 Banach 理想、全部乘子及共同逆核心

日期：2026-11-29（Asia/Taipei）。作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。

本稿把原同分母问题放进一个已经付清范数稠密主理想的具体 Banach 代数。这里的稠密是代数自身的算子范数稠密，不以 Hilbert 空间中的准亲和代替。没有从 quasimultiplier 记号自动取得原平方根。

## 1. 同一原代数及真实近似单位

固定原 Haar 尾 $C=A^{(m_0)}$，$\mathscr A=\{C\}'$，沿用同一
$$
Z=I+\sum_{j\ge0}(j+1)^{-1}V_j,\qquad L=Z^{-1},\qquad
P_\theta=Z^{-\theta}\quad(\Re\theta>0).
$$
定义
$$
\boxed{\mathscr B=\overline{L\mathscr A}^{\,\|\cdot\|}.}
\tag{1}
$$
这是原算子范数中的非零闭理想，不作等价范数改造。记
$\mathfrak F=\bigcap_{k\ge1}C^k\mathscr A$。

[实际共同幂范数逼近](R12-appendix-accretive-sources-norm-approximated-by-common-power-quasiaffinities.md)已经构造收缩 $F_N=C U_N$、$U_N$ 为有界单位，以及收缩 $R_n\in\mathfrak F$，满足
$$
\|(I-F_N)L\|\to0,\qquad
\|(I-R_n)L\|\to0.
\tag{2}
$$
该稿还给每个固定 $n$ 的真实强*单位
$$
R_nW_{n,\nu}\to I,\quad
\|R_nW_{n,\nu}\|\le1,\quad
\|(I-R_nW_{n,\nu})L\|\to0.
\tag{3}
$$
最后的范数式直接由该稿 $R_nW=T_kF_M^k$ 得到：固定 $k$ 用
$\|(I-F_M^k)L\|\le k\|(I-F_M)L\|$，再令尾积 $T_k$ 在 $L$ 后的误差趋零。可以用同一对角子列兼顾两个拓扑。

另置
$$
E_t=t(Z+tI)^{-1}=tL(I+tL)^{-1}\qquad(t>0).
$$
则 $E_t\in\mathscr B$，$\|E_t\|\le t/(1+t)<1$，且
$$
\|(I-E_t)L\|=\|(Z+tI)^{-1}\|\le(1+t)^{-1}.
\tag{4}
$$
由 $L\mathscr A$ 在 $\mathscr B$ 中稠密，(4) 给
$$
\boxed{E_tb\to b\text{ 于 }\mathscr B\text{ 的范数，}\quad b\in\mathscr B.}
\tag{5}
$$
所以 $\mathscr B$ 具有真正的收缩有界近似单位。它在原 $H$ 上同时强*趋于 $I$。

同理，(2)、(3) 的所有统一有界乘子在 $\mathscr B$ 上逐元素范数趋于恒等。没有声称它们在 $\mathcal B(\mathscr B)$ 的算子范数中趋于恒等。

$\mathscr B$ 是根基 Banach 代数。因为 $L$ 拟幂零且 $\mathscr A$ 交换，$L\mathscr A$ 包含于 $\operatorname{rad}\mathscr A$，该根基范数闭。对 $b\in\mathscr B$ 及 $\lambda\ne0$，
$$
(\lambda I-b)^{-1}=\lambda^{-1}I+
\lambda^{-1}b(\lambda I-b)^{-1}
$$
的后一项在 $\mathscr B$ 中，故同样在 $\mathscr B$ 的单位化中可逆。这支付其自身根基性。又 $\mathscr B^\perp=\{b:b\mathscr B=0\}=\{0\}$，由 (5) 即得。

## 2. 全部有界乘子仍是原完整交换子

采用通常乘子定义
$$
M(\mathscr B)=\{T\in\mathcal B(\mathscr B):
T(ab)=aT(b)\quad(a,b\in\mathscr B)\}.
$$
每个 $X\in\mathscr A$ 都以左乘作用于 $\mathscr B$，且乘子范数不超过 $\|X\|$。反向，取 $T\in M(\mathscr B)$。序列 $T(E_n)$ 在原 $\mathcal B(H)$ 中有界，故取弱算子聚点 $X$。它属于弱算子闭的 $\mathscr A$。对 $b\in\mathscr B$，
$$
T(E_n)b=T(E_nb)\longrightarrow T(b)
$$
在算子范数中成立；沿该聚点取弱极限便得 $Xb=T(b)$。

又 $E_n\to I$ 强，故
$$
\|X\|\le\liminf_n\|XE_n\|\le\|T\|.
$$
结合反向上界，得到
$$
\boxed{M(\mathscr B)=\mathscr A\quad\text{等距，作用就是原左乘。}}
\tag{6}
$$
聚点因此唯一。对固定有限矩阵的乘子作用，使用 $\operatorname{diag}(E_n,\ldots,E_n)$ 得同一范数等号，所以该识别也保留实际有限矩阵放大的算子范数。没有引入另一 Hilbert 表示来代替原 $C$。

## 3. 真实范数稠密主理想

定义
$$
\Omega(\mathscr B)=
\{v\in\mathscr B:\overline{v\mathscr B}^{\,\|\cdot\|}=\mathscr B\}.
\tag{7}
$$
首先 $L\in\Omega(\mathscr B)$。事实上 $E_tL\in L\mathscr B$，并由 (4) 在范数中趋于 $L$，再乘任意 $\mathscr A$ 元素、取闭包即得结论。

由 (2)，$F_Nb\to b$ 对每个 $b\in\mathscr B$ 范数成立，而
$F_Nb=CU_Nb\in C\mathscr B$。因此
$$
\boxed{\overline{C\mathscr B}^{\,\|\cdot\|}=\mathscr B,\qquad
CL\in\Omega(\mathscr B).}
\tag{8}
$$
第二式使用 $L\mathscr B$ 与 $C\mathscr B$ 都稠密。这里 $C$ 是乘子，未说 $C\in\mathscr B$；实际 $\mathscr B\subseteq\overline{\mathfrak F}$ 已由前稿支付。

每个 $P_\theta$ 也在 $\Omega(\mathscr B)$。当 $0<\Re\alpha<1$ 时，
$$
P_\alpha=\frac{\sin\pi\alpha}{\pi}
\int_0^\infty t^{-\alpha}L(I+tL)^{-1}\,dt
\in\mathscr B
$$
是范数绝对收敛积分；任意 $\theta$ 由同源幂律延拓此包含。选整数 $k>\Re\theta$，有
$P_\theta P_{k-\theta}=L^k$，而 $L^k\mathscr B$ 稠密，故
$$
P_\theta\in\Omega(\mathscr B).
\tag{9}
$$

(3) 又给 $\overline{R_n\mathscr B}=\mathscr B$。从而得到真实共同全部幂的范数稠密分母：
$$
\boxed{R_nP_\theta\in\mathfrak F\cap\Omega(\mathscr B),\qquad
R_nP_\theta\to P_\theta\text{ 于算子范数}.}
\tag{10}
$$
$R_n$ 自身是否属于 $\mathscr B$ 并非 (10) 的前提；其作为 $\mathscr B$ 乘子的稠密像与 $P_\theta\in\Omega(\mathscr B)$ 足够。

## 4. 全部整数逆的共同实际核心

在 Banach 空间 $\mathscr B$ 上，乘 $C$ 是单射、有稠密非闭像的有界算子。其第 $k$ 次逆的自然定义域和作用准确为
$$
D_k=C^k\mathscr B,\qquad T_k(C^kb)=b.
$$
$T_k$ 闭：若 $C^kb_n\to x$ 且 $b_n\to b$，则 $x=C^kb$。

置
$$
\mathscr D_\infty=\bigcap_{k\ge1}C^k\mathscr B.
\tag{11}
$$
对每个 $x\in\mathscr B$，$R_nx\in\mathscr D_\infty$，因为前稿的每个实际有界除商 $C^{-k}R_n\in\mathscr A$ 保持 $\mathscr B$。又 $R_nx\to x$ 于 $\mathscr B$ 范数，故 $\mathscr D_\infty$ 稠密。

若 $x\in D_k$，则
$$
R_nx\to x,\qquad
T_jR_nx=R_nT_jx\to T_jx
\quad(0\le j\le k)
\tag{12}
$$
都是原算子范数收敛。于是 $\mathscr D_\infty$ 是每个 $T_k$ 的实际图核心，并且同一列逼近同时支付任意固定有限组整数逆图范数。这里只断言每个固定有限组，不添全阶一致界或半次逆。

## 5. Norm 稠密分母确实给原 Hilbert 全旗来源

任取 $v\in\Omega(\mathscr B)$。由 (7)，为整数 $n$ 选择 $b_n\in\mathscr B$，使
$$
\|vb_n-E_n\|<1/n.
$$
则
$$
vb_n=b_nv\to I\quad\mathrm{strong*},\qquad
\sup_n\|vb_n\|<\infty.
\tag{13}
$$
这证明原 $v$ 单射且稠密像。所有 $v,b_n$ 属于 $\mathscr A$，由原 R88 保持每个普通 $C$ 不变旗；(13) 在固定 Hilbert 商代表中压缩后仍成立。因此 $v$ 在这些真实旗及有限放大旗上均准亲和。

对 $u\in\mathscr B$，定义最大 Hilbert 商
$$
S_{u/v}x=y\quad\Longleftrightarrow\quad ux=vy.
\tag{14}
$$
$v$ 单射给唯一性，图由有界方程定义所以闭，且定义域包含稠密的 $\operatorname{Ran}v$。分式的代数等价与 (14) 的最大闭实现一致：若 $uv'=u'v$，把 $ux=vy$ 乘 $v'$ 并取消单射 $v$，即得 $u'x=v'y$；反向同理。

(13) 还支付真正核心。对 $(x,S_{u/v}x)$，
$$
vb_nx\to x,\qquad
S_{u/v}(vb_nx)=vb_nS_{u/v}x\to S_{u/v}x.
\tag{15}
$$
所以 $\operatorname{Ran}v$ 是该最大闭商的图核心。此处不只是取参数像的闭包。

## 6. Quasimultiplier 中的原逆与真实平方目标

采用 Isabelle Chalendar、Jean Esterle、Jonathan R. Partington，
*Boundary values of analytic semigroups and associated norm estimates*，
Banach Center Publications **91** (2010), 87–103，
[DOI 10.4064/bc91-0-5](https://doi.org/10.4064/bc91-0-5)
（[出版方书目与全文](https://impan.pl/pl/wydawnictwa/banach-center-publications/all/91/0/86357/boundary-values-of-analytic-semigroups-and-associated-norm-estimates)，
[作者全文](https://www.math.u-bordeaux.fr/~jesterle/boundary-ba09v9.pdf)），
§2 Definitions 2.2–2.3 的记号：$QM(\mathscr B)=\mathscr B/\Omega(\mathscr B)$；
正规 quasimultiplier 要求在同一个 $\Omega(\mathscr B)$ 锚上，适当几何缩放的全部正幂范数有界。该范数和锚在这里已经具体确定。

由 (8)，
$$
C=(CL)/L,\qquad C^{-1}=L/(CL)
\tag{16}
$$
是实际代数分式。后一式的最大 Hilbert 实现正是原 $C^{-1}$，定义域为 $\operatorname{Ran}C$：由 $Lx=CLy$ 及 $L$ 单射可准确消去为 $x=Cy$。

但 $C^{-1}$ 不是正规 quasimultiplier。若有非零锚 $a$ 和 $K,M<\infty$，使全部实际 $C^{-n}a\in\mathscr B$ 且
$\|C^{-n}a\|\le MK^n$，则
$$
\|a\|\le\|C^n\|MK^n\longrightarrow0,
$$
与 $a\ne0$ 矛盾。因此没有以 (16) 偷得双向幂预算。

另一方面，若能构造真正 $u\in\mathscr B$、$v\in\Omega(\mathscr B)$，使
$$
\boxed{u^2=Cv^2,}
\tag{17}
$$
则 $S_{u/v}$ 在其最大自然域上满足
$D(S_{u/v}^2)=D(S_{u/v})$、$S_{u/v}^2=C|_{D(S_{u/v})}$。
直接核域：从 $ux=vy$ 得
$vuy=u^2x=Cv^2x$，取消 $v$ 得 $uy=vCx$，所以 $y$ 再次入域且 $Sy=Cx$。
$u$ 由 (17)、$C,v$ 的准亲和性也准亲和，故 $S$ 单射且像稠密。

任何这样的平方根在 $QM(\mathscr B)$ 中自动正规：同一个合法锚 $v$ 给
$$
S^{2n}v=C^nv,\qquad S^{2n+1}v=C^nu,
$$
其范数一致有界。这里的正规性是对一个已经构造的根的结论，不能倒置为存在定理。

## 7. 真正仍待支付的接口

本稿已给 $\Omega(\mathscr B)\ne\varnothing$、具体 $L,CL,R_nP_\theta$ 的范数稠密主理想、完整原乘子识别及共同整数逆核心。因而后续使用 $QM(\mathscr B)$ 时，不能再用只有 Hilbert 稠密像的假替代来解释本稿这些分母。

仍未构造 (17)。也未证明任意原全旗准亲和 $P\in\mathscr A$ 都在 $\mathscr B$ 上有范数稠密乘子像，或能用本稿的 $\Omega(\mathscr B)$ 分母表示任意未知闭根。原 $Q_*$ 的此类范数来源需要另证。既有正规 quasimultiplier 文献的半群和增长假设仍须实际核实，不能从 (16) 自动定义 $C^{1/2}$。
