# R35：严格 Mordell–Weil 线选择一个完整的辅助素数证书

**可信度：已证明。** 日期：2026-11-12。曲线、素数、字符和中心变量均同 R34：
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
p\ge13,\quad p\equiv1\pmod4,\quad p\ne17,
$$
$$
\Lambda=\mathbb Z_p[[T]],\quad \rho_E(\gamma)=1+p,
\quad \mathfrak P=(T-p),\quad
D_p=\mathcal A_p/\mathfrak P\mathcal A_p.
$$

本结果把 R34 的单辅助素数判据进一步具体化。由固定点
$P=(-1,4)$、$Q=(9,24)$ 构造一个满射
$$
\lambda_p:D_p\twoheadrightarrow\mathbb Z_p.
\tag{0.1}
$$
对每个有限层，Chebotarev 都给出无穷多个可选辅助素数，其类在 $\lambda_p\bmod p$ 下非零。任取这样的一个素数，其 rank $2$ Rubin–Stark **值理想**的中心评价就已经等于完整第一高阶 Fitting 理想的中心评价。这里没有假设外积泛函在基变换后全部可提升。

最后准确计算 $N_p=\ker\lambda_p$ 的对偶与 $\Sha[p^\infty]$ 之间的有限误差。跨素数仍缺的是 $N_p$ 对无穷多个 $p$ 有限；可选辅助素数的存在不解决这一点。

## 1. 从两个固定点构造整的无分歧字符

置 $T_\pi E=\varprojlim_m E[\pi^m]$、$W=E[\pi^\infty]$，固定 $T_\pi E$ 的一个 $\mathbb Z_p$ 基。所有整数系数和 $p$-进系数均通过选定的嵌入
$\mathcal O_K\hookrightarrow\mathcal O_{K,\mathfrak p}=\mathbb Z_p$ 作用。

记 $\kappa(P),\kappa(Q)\in H^1(K,T_\pi E)$ 为整 Tate–Kummer 类，并令
$$
\ell_P=\log_E(P),\qquad\ell_Q=\log_E(Q)\quad\text{于 }K_{\mathfrak p}=\mathbb Q_p.
$$
这里采用与不变微分相容、由形式群延拓的局部椭圆对数。两个值均非零：局部对数的核是有限挠子，R4 已证明两个点非挠。

取
$$
r_p=\min\{v_p(\ell_P),v_p(\ell_Q)\},\qquad
a_p=p^{-r_p}\ell_Q,\quad b_p=-p^{-r_p}\ell_P.
\tag{1.1}
$$
于是 $a_p,b_p\in\mathbb Z_p$，其中至少一个为单位，且
$$
\xi_p=a_p\kappa(P)+b_p\kappa(Q)
\tag{1.2}
$$
在 $\mathfrak p$ 处局部化为零。确实，局部 Kummer 格在本素数范围经椭圆对数单射到 $\mathbb Q_p$，而其像的对数为
$a_p\ell_P+b_p\ell_Q=0$。

$P,Q$ 在 $E(K)$ 中 $\mathcal O_K$-线性独立：若有 $K$-线性关系，连同复共轭关系分别相加、相减，就会给两个 $\mathbb Q$-线性关系，均与 R4 中的独立性矛盾。因此整 Mordell–Weil Kummer 注入保证 $\xi_p\ne0$。

### 1.1 限制到塔上并经过类群

在 $K_\infty=K(E[\pi^\infty])$ 上 $T_\pi E$ 为平凡模，故 $\xi_p$ 的限制是连续同态
$$
G_{K_\infty}\longrightarrow T_\pi E.
$$
这个同态非零。与 R34 §2.1 相同，非平凡 tame 字符给
$H^1(\Delta\times\Gamma,T_\pi E)=0$，因此全局限制映射在这里单射。

该同态处处无分歧。在 $\mathfrak p$ 处，它来自已经为零的局部类；在其余地方，它来自 usual Kummer 类。有限层取 $m\le n$ 后，$E[\pi^m]$ 已在 $K_n$ 中有理，且 CM 曲线在 $K_1$ 上远离 $\mathfrak p$ 有好约化；由于这些地方的 $\pi$-同源为 étale，Rubin Corollary 3.17 的局部 Kummer 扩张无分歧。这也包括 $\bar{\mathfrak p}$，不把它遗漏到分歧集合中。

全局类域论于是把 (1.2) 写成非零的等变同态
$$
\lambda_p^0:\mathcal A_p\longrightarrow T_\pi E\simeq\mathbb Z_p.
\tag{1.3}
$$
其 $\Delta$ 方向是直接字符 $\widetilde\chi$，且
$\lambda_p^0(\gamma x)=(1+p)\lambda_p^0(x)$；故它通过 $D_p$ 因子化。

### 1.2 必须进行的整数饱和

$D_p$ 为有限生成 $\mathbb Z_p$-模，所以非零紧像为
$$
\lambda_p^0(D_p)=p^{d_p}\mathbb Z_p
\quad\text{某个有限 }d_p\ge0.
$$
定义
$$
\boxed{\quad
\lambda_p=p^{-d_p}\lambda_p^0:D_p\twoheadrightarrow\mathbb Z_p,
\qquad N_p=\ker\lambda_p.
\quad}\tag{1.4}
$$
这一除法先在完整整数像中进行，不是在模 $p^n$ 的值中任意除以 $p$。改变 Tate 基或把严格 Mordell–Weil 线的生成元乘以单位，只把 $\lambda_p$ 乘以单位，不改变 $N_p$。

饱和指数有一个固定的有限例外控制。取正整数 $I$ 使
$$
I\bigl(E(K)/E(K)_{\rm tors}\bigr)
\subset\mathcal O_K P+\mathcal O_K Q.
\tag{1.5}
$$
这样的 $I$ 存在，因为两边都是秩二 $\mathcal O_K$-格。则
$$
d_p\le v_p(I).
\tag{1.6}
$$
证明：Mordell–Weil 可除群注入 $S_p$，而可除群作为 $\mathbb Z_p$-模是内射的，故该注入在 Tate 模上具有原始像。$\xi_p$ 在 $\kappa(P),\kappa(Q)$ 的格中至少有一个单位坐标。若它在严格 Selmer Tate 模中可除以 $p^d$，原始性使商仍属于完整 Mordell–Weil Tate 格；乘以 (1.5) 的 $I$ 后回到 $P,Q$ 的格，单位坐标强迫 $d\le v_p(I)$。R34 的整同构将这种可除性与 (1.3) 的像被 $p^d$ 整除准确识别，得到 (1.6)。

因此除固定整数 $I$ 的有限多个素因子外，(1.2) 已经给饱和的 $\lambda_p$。本文不假定已知 $I=1$，也不以未经证明的生成元声明略去这一步。

## 2. 有限层字符和 Chebotarev 选择

令
$$
A_n=(\operatorname{Cl}(K_n)\otimes\mathbb Z_p)^{\widetilde\chi},\qquad
R_n=\mathbb Z_p[\Gamma/\Gamma^{p^{n-1}}],\qquad
S_n=\mathbb Z_p/p^n.
$$
R32 的准确范数控制和 R33 给
$$
A_n\simeq\mathcal A_p/\omega_n(T)\mathcal A_p,
\quad \omega_n(T)=(1+T)^{p^{n-1}}-1,
$$
$$
D_{p,n}:=A_n/(\gamma_n-(1+p))A_n
\simeq D_p/p^nD_p.
\tag{2.1}
$$
因为 $v_p(\omega_n(p))=n$，(1.4) 的模 $p^n$ 约化因子化为满射
$$
\lambda_{p,n}:A_n\twoheadrightarrow D_{p,n}
\twoheadrightarrow S_n.
\tag{2.2}
$$
其中 $\Gamma_n$ 在 $S_n$ 上通过 $\gamma_n\mapsto1+p$ 作用；若从完整类群写起，$\Delta$ 通过 $\widetilde\chi\bmod p^n$ 作用。因此 (2.2) 的核在 $G_n=\operatorname{Gal}(K_n/K)$ 下稳定。

整数饱和不妨碍给出有限精度含义。若 $d_p>0$，可先把 $A_n$ 的类提升到 $A_{n+d_p}$，用 (1.2) 的 Kummer 字符计算模 $p^{n+d_p}$ 的值，再除以 $p^{d_p}$。两种提升之差来自 $\omega_n\mathcal A_p$，其 $\lambda_p^0$ 值在 $p^{n+d_p}\mathbb Z_p$ 中，故结果模 $p^n$ 无歧义。范数控制保证所需类提升存在。

### 2.1 所需辅助素数总能选到

将 (2.2) 与完整类群的字符投影合成。类域论给一个处处无分歧的循环扩张
$$
L_{p,n}/K_n,\qquad\operatorname{Gal}(L_{p,n}/K_n)\simeq S_n.
$$
其核 $G_n$-稳定，所以 $L_{p,n}/K$ 是 Galois 扩张。取
$h\in\operatorname{Gal}(L_{p,n}/K_n)$ 对应 $1\in S_n$。共轭作用将 $h$ 的像乘以 $\rho_E(g)\bmod p^n$，始终是单位。

Chebotarev 给无穷多个素理想 $\mathfrak q$，避开任意指定有限集合，且其在 $L_{p,n}/K$ 中的 Frobenius 共轭类为 $h$ 的共轭类。它在 $G_n$ 中的像为恒等，所以 $\mathfrak q$ 完全分裂于 $K_n/K$。对任意上方素位 $w$，令
$c_w=e_{\widetilde\chi}[w]\in A_n$，都有
$$
\boxed{\quad\lambda_{p,n}(c_w)\in S_n^\times.\quad}
\tag{2.3}
$$
只需检测模 $p$ 非零即可。换上方素位只乘一个 Galois 字符单位，所以 (2.3) 与这个选择无关。这里无穷多个的是固定 $p,n$ 的辅助素数，未改变主问题中需要变动的 $p$。

## 3. rank $2$ 元素的准确二阶行列式

沿用已证明的
[赋值矩阵笔记](../notes/2026-11-12-rubin-stark-valuation-matrix.md)
中的固定 $\mathcal T=\{(67)\}$、$z_n=e_{\widetilde\chi}\Phi(P_{\pi^n})$ 和秩一元素：
$$
\epsilon_{1,n}=u_nz_n,\qquad
u_n=\frac{4489\sigma_{67}^{-1}-1}{2g_f}\in R_n^\times,
\quad u_\infty(p)=-\frac1{1+i}.
\tag{3.1}
$$
令 $S=S_\infty\cup S_{\rm ram}(K_n/K)$，选一个满足 (2.3) 的 $\mathfrak q\notin S\cup\mathcal T$ 和上方素位 $w$。记
$$
U_0=(\mathcal O_{K_n,S,\mathcal T}^{\times}\otimes\mathbb Z_p)^{\widetilde\chi},
\quad
U_{\mathfrak q}=(\mathcal O_{K_n,S\cup\{\mathfrak q\},\mathcal T}^{\times}\otimes\mathbb Z_p)^{\widetilde\chi}.
$$
等变赋值采取直接作用约定
$$
v_w(u)=e_{\widetilde\chi}
\sum_{g\in G_n}\operatorname{ord}_{g w}(u)g.
$$
射线理想类正合列在目标字符上为
$$
0\longrightarrow U_0\longrightarrow U_{\mathfrak q}
\xrightarrow{v_w}R_n
\xrightarrow{x\mapsto xc_w}A_n
\longrightarrow A_n/R_nc_w\longrightarrow0.
\tag{3.2}
$$
R32 已消去原有 $S$-素位类及 $\mathcal T$ 的剩余单位修正，因此这里使用完整 $A_n$。

取 $h$ 为 $w$ 在完整 $\mathcal T$-射线类群中的阶，并选择
$$
w^h=(\widetilde z_w),\qquad
\widetilde z_w\equiv1\pmod v\quad(v\mid67),\qquad
z_w=e_{\widetilde\chi}\widetilde z_w.
$$
则 $v_w(z_w)=h$。在 $B_n=\mathbb Q_p[\Gamma_n]$ 上，$U_0$ 和 $U_{\mathfrak q}$ 的秩分别为一、二。

以 BKS 的位置顺序 $[\infty,\mathfrak q]$ 定义
$$
\epsilon_{2,n,w}
=\epsilon_{K_n/K,S\cup\{\mathfrak q\},\mathcal T}^{\{\infty,\mathfrak q\},\widetilde\chi}.
$$
复 regulator 中新增 Euler 零的 $\log N\mathfrak q$ 与赋值坐标的同一因子相消，得到
$$
\boxed{\quad
\epsilon_{2,n,w}=\frac{\epsilon_{1,n}\wedge z_w}{h}
=\frac{u_n}{h}z_n\wedge z_w.
\quad}\tag{3.3}
$$
符号须注意：BKS 的收缩约定为
$v(x\wedge y)=v(x)y-v(y)x$，故在本顺序下
$$
v_w(\epsilon_{2,n,w})=-\epsilon_{1,n}.
\tag{3.4}
$$
秩三笔记中两个有限位移过第一列给正号；不能把那个正号照搬到单有限位情形。

对任意 $\phi_0,\phi_1\in\operatorname{Hom}_{R_n}(U_{\mathfrak q},R_n)$，
$$
\boxed{\quad
(\phi_0\wedge\phi_1)(\epsilon_{2,n,w})
=\frac{u_n}{h}
\det\begin{pmatrix}
\phi_0(z_n)&\phi_0(z_w)\\
\phi_1(z_n)&\phi_1(z_w)
\end{pmatrix}\in R_n.
\quad}\tag{3.5}
$$
整性来自 R32 所核查的已出版 Bley–BKS 输入。两个 $\phi_i$ 都必须在完整的整 $S$-单位格上取 $R_n$ 中的值，不能从 $B_n$ 上任意指定的两行矩阵冒充它们。

把二阶行列式记为 $\mathscr D_{n,w}(\phi)$，则准确证书为
$$
e_n\bigl(\mathscr D_{n,w}(\phi)/h\bigr)\ne0\quad\text{于 }S_n.
\tag{3.6}
$$
先在 $R_n$ 中整除，再评价 $\gamma_n\mapsto1+p$。若 $s=v_p(h)$，逐个 $\mathbb Z_p$ 系数计算需要模 $p^{n+s}$ 的精度。对 (2.3) 所选的辅助素数，$c_w$ 的像在 $D_{p,n}$ 中阶恰为 $p^n$，因此
$$
v_p(h)\ge n.
\tag{3.7}
$$
所以这种明确选类方法并不同时给一个小分母；忽略主化分母会丢失所需证书。

## 4. 一个辅助素数已得到完整的中心值理想

令 $J_{n,w}$ 为固定 $w$ 时全部 (3.5) 的值生成的 $R_n$-理想。已出版 BKS Theorem 1.5(ii) 的 $i=0$ 情形，对 $S\cup\{\mathfrak q\}$、秩 $r=2$ 给出
$$
\boxed{\quad
J_{n,w}=\operatorname{Fitt}_{R_n,0}(A_n/R_nc_w).
\quad}\tag{4.1}
$$
具体地，转置 Selmer 模在本字符上是 $A_n/R_nc_w$ 与一个自由秩二模的扩张；自由商使之可裂，因此其第二 Fitting 理想就是该类群商的第零 Fitting 理想。与 rank $3$ 笔记相同，这里是在 $R_n$ 中先得到完整理想相等。

由于 (1.4) 满射而 $\mathbb Z_p$ 自由，作为整数模可取分裂
$$
D_p\simeq\mathbb Z_p\oplus N_p.
$$
约化后
$$
D_{p,n}\simeq S_n\oplus N_p/p^nN_p.
\tag{4.2}
$$
令 $\bar c_w$ 为 $c_w$ 在 $D_{p,n}$ 的像。由 (2.3)，$\lambda_{p,n}(\bar c_w)$ 是单位，所以 $S_n\bar c_w$ 自由秩一且给 $\lambda_{p,n}$ 的一个截面。因此
$$
\boxed{\quad
D_{p,n}/S_n\bar c_w\simeq N_p/p^nN_p.
\quad}\tag{4.3}
$$
一个直接的同构是把 $x$ 送到
$x-\lambda_{p,n}(x)\lambda_{p,n}(\bar c_w)^{-1}\bar c_w$，再识别到核；其核正是 $S_n\bar c_w$。

现在只使用 Fitting 理想对任意基变换的相容性，以及自由秩一因子的公式。由 (4.1)–(4.3)，
$$
\begin{aligned}
e_n(J_{n,w})
&=\operatorname{Fitt}_{S_n,0}(D_{p,n}/S_n\bar c_w)\\
&=\operatorname{Fitt}_{S_n,0}(N_p/p^nN_p)\\
&=\operatorname{Fitt}_{S_n,1}(D_{p,n})\\
&=e_n\bigl(\operatorname{Fitt}_{R_n,1}(A_n)\bigr).
\end{aligned}
\tag{4.4}
$$
再由 R32 得到
$$
\boxed{\quad
e_n(J_{n,w})
=e_n(\Theta^{\rm RS}_{1,n})
=\operatorname{ev}_{T=p}\operatorname{Fitt}_{\Lambda,1}(\mathcal A_p)
\pmod{p^n}.
\quad}\tag{4.5}
$$
这证明任何满足 (2.3) 的一个辅助素数已经实现完整的中心值理想。没有用到
$\operatorname{Hom}_{R_n}(U_{\mathfrak q},R_n)$ 在 $e_n$ 基变换后满射到所有新泛函这种未证明断言；合法的步骤是先取 (4.1) 的整值理想，再对 Fitting 理想基变换。

因此每个 $p,n$ 都能预先把辅助素数限制到一个明确的 Chebotarev 集合；在该集合中重新选择辅助素数，不会改变值理想的中心消失与否。

## 5. 剩余核与 Sha：有限饱和误差的准确公式

记
$$
\mathscr M_p
=E(K)\otimes_{\mathcal O_K}(K_{\mathfrak p}/\mathcal O_{K,\mathfrak p})
\simeq W^2,
$$
并定义
$$
\mathscr M_p^{\rm str}
=\ker(\mathscr M_p\longrightarrow H_{f,p}).
$$
R34 的非挠点论证给 $\mathscr M_p\twoheadrightarrow H_{f,p}$。把它与全局 Kummer 列及严格 Selmer 列作交换图，蛇引理给出准确正合列
$$
0\longrightarrow\mathscr M_p^{\rm str}
\longrightarrow S_p^{\rm str}
\longrightarrow\Sha(E/\mathbb Q)[p^\infty]
\longrightarrow0.
\tag{5.1}
$$
最后的识别使用 R7 的 $\mathbb Q$ 与 $K$ 的 $\pi$ 分量比较。

### 5.1 严格 Mordell–Weil 核可能含有限项

在 Tate 格上，局部化是非零映射
$$
T_p\mathscr M_p\simeq\mathbb Z_p^2
\longrightarrow T_pH_{f,p}\simeq\mathbb Z_p.
$$
令其像的指数为 $p^{e_p^{\rm MW}}$。等价地，$e_p^{\rm MW}$ 是完整 Mordell–Weil 的局部对数闭包在局部对数格中的余长度；不把 $P,Q$ 未知的有限指数混入此定义。

对这行整数矩阵作 Smith 化，得到 $[p^{e_p^{\rm MW}},0]$ 乘单位。因此
$$
\mathscr M_p^{\rm str}
\simeq W\oplus\mathbb Z/p^{e_p^{\rm MW}}\mathbb Z
\tag{5.2}
$$
非典范地成立。其最大可除子群及商却是典范的，记
$$
\mathscr M_p^0=\operatorname{Div}\mathscr M_p^{\rm str},\qquad
F_p^{\rm MW}=\mathscr M_p^{\rm str}/\mathscr M_p^0
\simeq\mathbb Z/p^{e_p^{\rm MW}}\mathbb Z.
\tag{5.3}
$$

构造 (1.2) 正好给 Tate 格局部化核的有理直线。整数饱和 (1.4) 使它成为这条直线在 $T_pS_p^{\rm str}$ 中的原始格。因为完整 Mordell–Weil Tate 格在 $T_pS_p$ 中原始，这也是 $T_p\mathscr M_p^{\rm str}$。在 R34 的
$S_p^{\rm str}=\operatorname{Hom}(D_p,W)$ 下，因而
$$
\lambda_p^*(W)=\mathscr M_p^0.
\tag{5.4}
$$
这说明为何先饱和是必要的：一个非原始字符只给 $W$ 到该直线的有限核参数化，不能直接当作这个子群的整 Tate 基。

对 $0\to N_p\to D_p\xrightarrow{\lambda_p}\mathbb Z_p\to0$ 取对偶，再将 (5.1) 商去 (5.4)，得到
$$
\boxed{\quad
0\longrightarrow F_p^{\rm MW}
\longrightarrow \mathscr H_p:=\operatorname{Hom}_{\rm cont}(N_p,W)
\longrightarrow\Sha(E/\mathbb Q)[p^\infty]
\longrightarrow0.
\quad}\tag{5.5}
$$
这就是剩余类群核与 Sha 之间的准确有限误差。

### 5.2 无限秩与有限商须分开

由 (5.5)，
$$
\boxed{\quad
\operatorname{rank}_{\mathbb Z_p}N_p
=q_p-1
=\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty].
\quad}\tag{5.6}
$$
特别地，$N_p$ 有限当且仅当目标初级群有限。

在一般情形，令
$$
F_p^{\rm sat}=F_p^{\rm MW}\cap\operatorname{Div}(\mathscr H_p),
$$
交集在 (5.5) 的中间群中取。由于
$\mathscr H_p/\operatorname{Div}\mathscr H_p
\simeq\operatorname{Hom}((N_p)_{\rm tors},W)$，商群的最大可除子群和有限商给出
$$
\boxed{\quad
0\longrightarrow F_p^{\rm MW}/F_p^{\rm sat}
\longrightarrow\operatorname{Hom}((N_p)_{\rm tors},W)
\longrightarrow
\frac{\Sha[p^\infty]}{\operatorname{Div}\Sha[p^\infty]}
\longrightarrow0.
\quad}\tag{5.7}
$$
这里有限子群的一部分可能进入更大的可除 Selmer 方向；正是 $F_p^{\rm sat}$ 记录这种现象。不能在未证明初级有限时简单用 $|N_{p,\rm tors}|/p^{e_p^{\rm MW}}$ 计算 Sha 的有限商。

若初级群有限，则 $q_p=1$、$N_p$ 有限、$F_p^{\rm sat}=0$，所以有准确阶公式
$$
\boxed{\quad
|N_p|=p^{e_p^{\rm MW}}\,|\Sha(E/\mathbb Q)[p^\infty]|.
\quad}\tag{5.8}
$$
此时 $D_p\simeq\mathbb Z_p\oplus N_p$，故 R34 中第一 Fitting 中心值的赋值为
$$
\operatorname{length}_{\mathbb Z_p}N_p
=e_p^{\rm MW}+v_p\bigl(|\Sha[p^\infty]|\bigr).
\tag{5.9}
$$
它不是一般 $p$-adic 高度 regulator 的赋值；这里出现的是 Mordell–Weil 局部化格的指数。

## 6. 已消除的选择问题与仍然开放的非零性

对于每个 $p$，严格 Mordell–Weil 线无条件给出 $\lambda_p$。对于每个 $n$，无条件能选到 (2.3) 的辅助素数。对每个这样的选择，(4.5) 说明完整 rank $2$ 证书不再需要在其他辅助素数间寻找不同的中心类群方向。

但 (4.5) 的共同值理想仍可能为零。按 (4.3)、(5.6)，这准确对应剩余核 $N_p$ 中是否还有自由 $\mathbb Z_p$ 方向。R34 的奇性说明其自由秩只能是 $0,2,4,\ldots$；没有证明它对无穷多个 $p$ 为零。

当 $N_p$ 有限时，(4.5) 的模 $p^n$ 值理想首次非零的层为
$$
n=1+\operatorname{length}_{\mathbb Z_p}N_p
=1+e_p^{\rm MW}+v_p(|\Sha[p^\infty]|).
$$
完整证书仍要求某个 (3.5) 的**整除后的**二阶行列式在该精度非零。复 regulator、固定点非挠以及辅助素数的 Chebotarev 存在性，各自都不代替这个整数非零性。

## 来源

- K. Rubin，*Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，Corollary 3.17，Theorem 5.7，§6 的 Kummer 及限制映射，§11.2 的类域论：[原文](https://swc-math.github.io/notes/files/99RubinCM.pdf)。
- D. Burns、M. Kurihara、T. Sano，*On zeta elements for $\mathbb G_m$*，Documenta Mathematica 21 (2016)，555–626，§4.1 的收缩约定和 Theorem 1.5(ii)：[原文](https://ems.press/content/serial-article-files/26320?nt=1)。其在本曲线各有限层的整性输入和完整模辨识已经在 R32 逐条核查。
- 本仓库 R4、R7、R27、R32–R34，以及 [rank 3 赋值矩阵笔记](../notes/2026-11-12-rubin-stark-valuation-matrix.md)。
