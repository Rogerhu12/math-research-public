# R12 附录：显式全次数闭乘子没有任何非零完整交换子分母

日期：2026-11-27（台北时间，UTC+8）。作者：Astra-ISP-8542378f-20261127（AI-assisted GPT-6 Astra Pro；literature_deddens 分证，根会话复核）。

状态：以下完整交换子障碍、实际同源零交及非可闭交换映射均已证明。本稿将 R230 的任意纯有限块 coherent-symbol 估计用于任意完整交换子的高块压缩；不要求分母由分块乘积构造，也不要求它有真空原像或预先属于 UHF。这里决定的是整个交换子代数的一般可闭性与有理严格循环性；没有因此决定原普通不变子空间问题。

## 1. 固定实际来源与主结论

仍在原 Haar 空间
$$
H=L^2(\mathbb Z_2,\mu),\qquad \mathscr C=\{A\}'
$$
工作。沿用实际归一化幂及 Cayley 乘子
$$
N_j=A^{2^j}/\|A^{2^j}\|,\qquad
V_j=(I-N_j)(I+N_j)^{-1},\qquad
V_F=\prod_{j\in F}V_j.
$$
已有原关系为
$$
\|N_j-E_j\|\le\eta_j,\quad
0<\eta_j\le e^{-770\,16^j},\quad
E_j=e_{10}^{(j)},\quad
D_j=I-2E_j,
\tag{1.1}
$$
$$
V_F1=\chi_F,\qquad
\|V_j-D_j\|\le8\eta_j,\qquad
\|V_j\|,\|D_j\|\le6.
\tag{1.2}
$$
所有 $V_j$ 是 $A$ 的真实有理函数，属于 $\mathscr C$。记 $\mathcal P$
为全部有限 Walsh 柱。

取完全指定的互不交位块
$$
q_n=16^n,\qquad m_n=q_n^2,\qquad
F_n=\{m_n,m_n+1,\ldots,m_n+q_n-1\},
\qquad c_n=2^{-n-2}\quad(n\ge1),
\tag{1.3}
$$
并定义
$$
\boxed{f=1+\sum_{n\ge1}c_n\chi_{F_n}.}
\tag{1.4}
$$
因为 $\sum c_n=1/4$，该级数一致收敛，故 $f$ 连续，并有
$$
\frac34\le f\le\frac54,\qquad
\|f\|^2=1+\sum c_n^2=\frac{49}{48}.
\tag{1.5}
$$
$q_n$ 都为偶数，所以原共轭 $C h(y)=\overline{h(-1-y)}$
还满足 $Cf=f$。这些附加性质不代替后面的算子证明。

令 $X_f$ 为原最小闭轨道乘子，即
$$
X_f=\overline{\{p(A)1\longmapsto p(A)f\}}.
\tag{1.6}
$$
R34 的复双线性配对保证它稠密定义且可闭；这里取其闭包。
由于 $1$ 循环，定义没有多项式表示歧义。

**主定理。**

1. 对任意 $0\ne P\in\mathscr C$，
   $$
   \boxed{\sup_{u\in\mathcal P,\ \|u\|\le1}\|PX_fu\|=\infty.}
   \tag{1.7}
   $$
2. 不存在 $0\ne P\in\mathscr C$ 满足 $PH\subseteq\operatorname{Dom}X_f$；
   也不存在 $P,Y\in\mathscr C$、$P\ne0$ 使
   $PX_f\subseteq Y$，或者使 $X_f\subseteq P^{-1}Y$（在 $P$ 单射时取最大闭商）。
3. 两个实际代数轨道满足
   $$
   \boxed{\mathscr C1\cap\mathscr Cf=\{0\}.}
   \tag{1.8}
   $$
   因而 $\mathscr C$ 不具有可闭性性质，也没有任何有理严格循环向量。

下面逐项支付完整块范数、同一来源和真实域。

## 2. 实际闭域与纯分块有界差

每个 $\chi_G$ 属于 $\operatorname{Dom}X_f$，且
$$
X_f\chi_G=V_Gf.
\tag{2.1}
$$
确实，选 $A$ 的多项式在算子范数中逼近真实有理函数 $V_G$；
它们在 $1$ 与 $f$ 上同时收敛，使用 (1.6) 的闭性即可。

对固定 $u\in\mathcal P$，在所有充分大的 $n$，
$F_n$ 位于 $u$ 的全部位之后，故
$$
D_{F_n}u=\chi_{F_n}u,\qquad
D_{F_n}=\prod_{j\in F_n}D_j.
$$
因此下式在每个实际有限柱上按向量范数绝对收敛：
$$
Z_0u=u+\sum_{n\ge1}c_nD_{F_n}u.
\tag{2.2}
$$

逐因子 telescoping 与 (1.2) 给
$$
\|V_{F_n}-D_{F_n}\|
 \le8q_n6^{q_n-1}\eta_{m_n}
 \le\epsilon_n,\qquad
\epsilon_n:=8q_n6^{q_n}\eta_{m_n}\le e^{-q_n^2}.
\tag{2.3}
$$
最后一个预算完全由原权保证：对 $q\ge16$，
$16^{q^2}\ge q^2$ 且
$\log(8q)+q\log6\le3q$，所以
$8q6^q e^{-770\,16^{q^2}}\le e^{-q^2}$。
因而
$$
K:=\sum_{n\ge1}c_n(V_{F_n}-D_{F_n})\in B(H)
\tag{2.4}
$$
按算子范数绝对收敛。

对 $u=\chi_G$，交换性和 (2.1) 给
$$
X_f\chi_G=\chi_G+\sum_n c_nV_{F_n}\chi_G.
$$
该向量和也绝对收敛，因为它等于
$V_G(1+\sum_n c_n\chi_{F_n})$ 的展开。
由 (2.2)--(2.4) 得到准确核心等式
$$
\boxed{X_f|_{\mathcal P}=Z_0+K|_{\mathcal P}.}
\tag{2.5}
$$
这里只需纯算子在这个指定核心上的实际值，不把形式无限和擅自认作最大闭域。

另外，(1.6) 使 $A$ 保持 $\operatorname{Dom}X_f$ 并与 $X_f$ 域交换。
完整交换子的一致有界强多项式逼近随后给
$$
P\operatorname{Dom}X_f\subseteq\operatorname{Dom}X_f,\qquad
X_fPu=PX_fu
\quad(P\in\mathscr C,\ u\in\operatorname{Dom}X_f).
\tag{2.6}
$$
证明只对固定 $u,X_fu$ 同时取强极限，再用闭性；没有将未知域直接延到整个空间。

## 3. 任意完整交换子的纯高块逼近

对任意单个位 $j$，在该位与其余位的物理分解中写
$$
T=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
\Pi_j(T)=\begin{pmatrix}a&0\\c&a\end{pmatrix}.
\tag{3.1}
$$
则 $\Pi_j(T)$ 与 $E_j$ 交换，$\Pi_j^2=\Pi_j$，且
$$
\|\Pi_j\|\le2,\qquad
\|T-\Pi_j(T)\|\le2\|[T,E_j]\|.
\tag{3.2}
$$
第二个界直接由
$[T,E_j]=\left(\begin{smallmatrix}b&0\\d-a&-b\end{smallmatrix}\right)$
及 $T-\Pi_j(T)$ 的两个非零块得到。
第一界来自对角块 $\operatorname{diag}(a,a)$ 与单个下角块 $c$ 的范数和。

不同位的 $\Pi_j$ 彼此交换；它们是作用于各自有限物理矩阵因子的线性映射。
特别，$\Pi_j$ 保持与其他位 $E_i$ 的交换关系。
对有限位块 $F$ 置
$$
\Pi_F=\prod_{j\in F}\Pi_j.
$$
因此 $\Pi_F(T)$ 与全部 $E_j$（$j\in F$）交换。

若 $P\in\mathscr C$，则 $[P,N_j]=0$，由 (1.1)，
$$
\|[P,E_j]\|\le2\|P\|\eta_j.
$$
逐项展开 $\Pi_F-I$，把每个前置 $\Pi_j$ 的范数至多2保留，得到
$$
\boxed{
\|\Pi_F(P)-P\|
 \le4|F|2^{|F|}\eta_{\min F}\|P\|.
}
\tag{3.3}
$$
这是真正的全空间算子范数估计，适用于任意 $P\in\mathscr C$；
没有要求 $P$ 属于 UHF。

对 (1.3) 的块，写
$$
Q_n=\Pi_{F_n}(P),\qquad
d_n=4q_n2^{q_n}\eta_{m_n}\|P\|.
$$
由于 $\|D_{F_n}\|\le3^{q_n}$，同一个预算 (2.3) 还给
$$
\boxed{
\|Q_n-P\|\le d_n,\qquad
d_n\|D_{F_n}\|\le\frac12\epsilon_n\|P\|\longrightarrow0.
}
\tag{3.4}
$$
所以后面的整个 $2^{q_n}$ 维块乘法不丢失误差预算。

## 4. 纯有限块的 coherent 下界：非零锚已足够

本节使用 R230 已付的任意有限交换块估计，不要求该块可逆。
记
$$
E=e_{10},\quad D=I-2E,\quad
\Omega=2^{-q/2}(e_0+e_1)^{\otimes q},\quad
\Omega_t=(1+|t|^2)^{-q/2}(e_0+t e_1)^{\otimes q}.
$$
若 $R$ 与全部块内 $E_j$ 交换，则
$R=\sum_{F}r_FE_F$。定义协变多项式
$$
b_R(z)=\sum_Fr_F(z/2)^{|F|}.
$$
逐位直接计算有
$$
\langle R\Omega_t,\Omega_s\rangle
 =\frac{(1+t\bar s)^q}
 {(1+|t|^2)^{q/2}(1+|s|^2)^{q/2}}\,
 b_R\!\left(\frac{2\bar s}{1+t\bar s}\right).
\tag{4.1}
$$
取 $s=t$ 可知 $\|R\|\le1$ 蕴含 $|b_R(z)|\le1$（$|z|\le1$）。
这只是原矩阵的标量协变符号，不将 $R$ 替换为某个单变量函数演算。

令 $h=q^{-1/2}$。在 (4.1) 取
$t=1$、$s=(1-h)/(1+h)$，对 $R-aI$ 使用该恒等式，得到
$$
\boxed{
|b_R(1-h)-a|
 \le(1+h^2)^{q/2}\|R\Omega-a\Omega\|
 \le e^{1/2}\|R\Omega-a\Omega\|.
}
\tag{4.2}
$$

下面给已证 Schur 估计在此所需的完整量词。
若 $\|R\|\le1$ 且
$$
|b_R(1-q^{-1/2})|\ge\delta>0,
$$
置 $\ell=-\log|b_R(1-q^{-1/2})|\le-\log\delta$。
R230 的零点分解、Harnack 与圆平均证明给
$$
r\le32\ell\sqrt q,\qquad
\|R\Omega_{-3}\|\ge e^{-\Gamma_q},
\tag{4.3}
$$
$$
\Gamma_q
 =\frac{1862}{3}\ell\sqrt q
   +r\log(2q^{1/4})+\frac{25}{2}\sqrt q
 =O_\delta(\sqrt q\log q).
\tag{4.4}
$$
这里 $r$ 只数 $b_R$ 在 $|z|\le3/4$ 中的零点；允许这些零点落在后续所取的小圆上。

为说明本次没有增加逆源或接近单位的隐藏假设，重述使用这些界的关键步骤。
除去紧内零点的 Blaschke 因子后，在 $|z|\le8/11$ 上
$$
|b_R(z)|\ge
\exp[-(1862/3)\ell\sqrt q]\,|I_{\rm in}(z)|.
$$
在中心 $-3/5$、半径 $\rho=q^{-1/4}$ 的圆上，
对每个内零点用
$\int\log|z-\alpha|=\log\max(\rho,|-3/5-\alpha|)$，
可选一个点使
$|I_{\rm in}(z)|\ge(\rho/2)^r$。
最后在 (4.1) 取 $t=-3$、$\bar s=z/(2+3z)$。
该极化前因子的绝对平方为
$(1+25|z+3/5|^2)^{-q}$，所以其模至少
$e^{-(25/2)\sqrt q}$，得到 (4.3)--(4.4)。
充分大 $q$ 时该圆位于 $|z|\le8/11$ 内，且上述分母非零。
整个证明只用了固定 $\delta>0$；旧稿更强的 $\ell\to0$ 在这里不需要。

于是有下述直接可用的版本。

**引理 4.1。** 设 $q_n\to\infty$，
$R_n\in\operatorname{span}\{E_F:F\subseteq F_n\}$ 满足
$$
\sup_n\|R_n\|<\infty,\qquad
\|R_n\Omega-a\Omega\|\to0,\qquad a\ne0.
\tag{4.5}
$$
则
$$
\liminf_{n\to\infty}
 \frac1{q_n}\log\|R_nD_{F_n}\|
 \ge\frac{\log5}{2}>0.
\tag{4.6}
$$

证明：用一个固定 $K>\sup\|R_n\|$ 归一化，由 (4.2) 得
$|b_{R_n/K}(1-q_n^{-1/2})|\ge|a|/(2K)>0$
对充分大 $n$ 成立。
(4.3)--(4.4) 给
$\|R_n\Omega_{-3}\|\ge K e^{-O(\sqrt{q_n}\log q_n)}$。
而单位列 $\chi_{F_n}=D_{F_n}\Omega$ 满足准确恒等式
$$
D_{F_n}\chi_{F_n}=5^{q_n/2}\Omega_{-3}.
$$
因此
$\|R_nD_{F_n}\|\ge
5^{q_n/2}\|R_n\Omega_{-3}\|$，即得 (4.6)。证毕。

## 5. 固定外部来源的整个块压缩

反设某个 $0\ne P\in\mathscr C$ 使 $PX_f$ 在 $\mathcal P$ 上有界。
由 (2.5)，存在 $M<\infty$，使
$$
\|PZ_0u\|\le M\|u\|\qquad(u\in\mathcal P).
\tag{5.1}
$$

由于有限柱稠密，可以选两个固定的单位有限柱 $u,v$，使
$$
a:=\langle Pu,v\rangle\ne0.
\tag{5.2}
$$
以后不改变这两个外部来源。对所有充分大的 $n$，
$F_n$ 位于 $u,v$ 的全部位之后。将该块与其余位重排为
$H=H_{F_n}\otimes H_{\widehat F_n}$，于是
$$
u=\Omega_{F_n}\otimes u_n^{\rm out},\qquad
v=\Omega_{F_n}\otimes v_n^{\rm out}.
$$
这里 $u_n^{\rm out},v_n^{\rm out}$ 只是固定 $u,v$ 在该分解下的同一个向量，
范数始终为一；没有随 $n$ 选择新的外部锚。

定义等距输入列与收缩输出行
$$
U_n h=h\otimes u_n^{\rm out},\qquad
L_n(h\otimes z)=\langle z,v_n^{\rm out}\rangle h,
$$
并置
$$
S_n=L_n P U_n,\qquad R_n=L_n Q_n U_n.
\tag{5.3}
$$
$R_n$ 与全部 $E_j$（$j\in F_n$）交换，所以属于引理4.1的纯有限块代数。
由 (3.4)，
$$
\|R_n-S_n\|\le d_n,\qquad
\sup_n\|R_n\|<\infty.
\tag{5.4}
$$

还需验证其锚，而不能只记录一个标量矩。
因为 $U_n\Omega=u$，
$$
S_n\Omega=L_nPu.
$$
对任意 $\epsilon>0$，选一个固定有限柱 $w$ 使 $\|Pu-w\|<\epsilon$。
当 $F_n$ 高于 $w,u,v$ 的全部位时，
$$
L_nw=\langle w,v\rangle\Omega.
$$
因此
$$
\|S_n\Omega-a\Omega\|
 \le\|Pu-w\|+|\langle w-Pu,v\rangle|
 <2\epsilon.
$$
先固定 $w$ 再令 $n\to\infty$，结合 (5.4) 得
$$
\boxed{R_n\Omega\longrightarrow a\Omega,\qquad a\ne0.}
\tag{5.5}
$$

现在支付整个块乘子范数的上界。
去掉 $Z_0$ 中的第 $n$ 项后，剩余纯块都作用于
$H_{\widehat F_n}$。存在向量 $t_n\in H_{\widehat F_n}$，使对全部
$h\in H_{F_n}$ 有
$$
Z_0U_nh
 =c_nU_nD_{F_n}h+h\otimes t_n.
\tag{5.6}
$$
这是全部 $2^{q_n}$ 个输入同时成立的算子列恒等式。
其余块的真实代价满足
$$
\|t_n\|
 =\|Z_0u-c_nD_{F_n}u\|
 \le\|Z_0u\|+c_n
 \le\|Z_0u\|+\frac14=:C_u<\infty.
\tag{5.7}
$$
$Z_0u$ 在 (2.2) 已实际定义。
没有把高维块上的算子范数换成单个真空列范数。

对 (5.6) 先左乘 $P$，再用 $L_n$ 压缩。
(5.1) 控制第一列，$h\mapsto h\otimes t_n$ 的整个算子范数正好是
$\|t_n\|$。于是
$$
c_n\|S_nD_{F_n}\|
 \le M+\|P\|C_u.
\tag{5.8}
$$
再用 (3.4)、(5.4)，
$$
\|R_nD_{F_n}\|
 \le c_n^{-1}(M+\|P\|C_u)
       +d_n\|D_{F_n}\|
 \le C_P\,2^{n+2}+o(1).
\tag{5.9}
$$
这里 $C_P$ 固定，不依赖块长、块维数或 $n$。

(5.4)--(5.5) 满足引理4.1，所以左侧的对数除以 $q_n=16^n$
下极限至少为 $(\log5)/2$；
(5.9) 给其上极限至多零。矛盾。
这证明主定理 (1.7)。

## 6. 实际全域分母及同源公共倍数均不存在

若 $0\ne P\in\mathscr C$ 且
$PH\subseteq\operatorname{Dom}X_f$，
则 $Y=X_fP$ 在整个 $H$ 上闭，因而有界。
由 (2.6)，
$$
PX_fu=X_fPu=Yu\qquad(u\in\mathcal P),
$$
与 (1.7) 矛盾。
所以任意非零完整交换子都不能把全空间送入这个实际闭域。

更一般，若 $P,Y\in\mathscr C$ 满足同源等式
$$
Pf=Y1,
\tag{6.1}
$$
则对每个有限 $G$，
$$
PX_f\chi_G=PV_Gf
 =V_GPf=V_GY1=Y\chi_G.
\tag{6.2}
$$
因此 $PX_f$ 在全部 $\mathcal P$ 上具有有界延拓 $Y$。
(1.7) 迫 $P=0$，再由 $Y1=0$ 和 $1$ 循环得 $Y=0$。
这同时证明 (1.8)，以及不存在任何非零有界分母的最大闭商包含。

这也覆盖新兼容喷射稿的平坦理想
$\mathfrak I_{\infty,0}$ 和 R267 的共同全部幂理想
$\mathfrak F_0$。它们虽有强*单位球密度，却没有任何非零元素能对
本稿这个具体 $X_f$ 支付全域像包含。因此一般闭模图的分母存在性不能
从这些平坦理想的强*密度推出。

## 7. 完整交换子上的具体不可闭稠密域映射

令
$$
\mathcal M_0=\mathscr C1,\qquad
\mathcal M_f=\mathscr Cf,\qquad
\mathcal D=\mathcal M_0\mathbin{\dot+}\mathcal M_f.
$$
(1.8) 保证直和。$\mathcal M_0$ 包含全部有限柱，因而
$\mathcal D$ 稠密。定义
$$
\boxed{Z(x+y)=y,\qquad x\in\mathcal M_0,\quad y\in\mathcal M_f.}
\tag{7.1}
$$
两个分量都由整个 $\mathscr C$ 保持，故对每个 $T\in\mathscr C$，
$$
T\mathcal D\subseteq\mathcal D,\qquad
ZTh=TZh\quad(h\in\mathcal D).
\tag{7.2}
$$
这是完整真实定义域上的交换，不是仅对多项式交换。

取明确有限柱
$$
f_N=1+\sum_{n=1}^N c_n\chi_{F_n}\in\mathcal M_0.
$$
因为 $f\in\mathcal M_f$，
$$
f-f_N\in\mathcal D,\qquad
f-f_N\longrightarrow0,\qquad
Z(f-f_N)=f\ne0.
\tag{7.3}
$$
所以 $Z$ 不可闭，证明完整 $\mathscr C$ 不具有可闭性性质。
不需要预先知道 $\mathscr Cf$ 是否稠密。

## 8. 不存在任何有理严格循环向量

采用 R203 与 Bercovici--Douglas--Foias--Pearcy 的原定义：
$h_0$ 有理严格循环，是指对每个 $h\in H$，有
$A_h,B_h\in\mathscr C$、$B_h$ 单射，使 $B_hh=A_hh_0$。

这里可以直接利用 (1.8)，不必把可闭性定理反向误用。
若这样的 $h_0$ 存在，分别取 $h=1,f$：
$$
B_1 1=A_1h_0,\qquad
B_f f=A_fh_0,\qquad B_1,B_f\text{ 单射}.
$$
交换性给
$$
A_fB_1 1=A_1B_f f\in\mathscr C1\cap\mathscr Cf=\{0\}.
$$
取消单射 $B_1$，得 $A_f1=0$；$1$ 循环迫 $A_f=0$。
于是 $B_f f=0$，再由 $B_f$ 单射迫 $f=0$，与 (1.5) 矛盾。
所以
$$
\boxed{\mathscr C\text{ 没有任何有理严格循环向量，也不 confluent}.}
\tag{8.1}
$$
最后一个断言还直接来自非零向量 $1,f$ 没有非零公共交换子像。

## 9. 范围、逐尾版本与未决目标

同一证明适用于每个原尾 $\mathscr C_m=\{B_m\}'$：
其实际归一化误差满足更强的
$\eta_j^{(m)}\le e^{-770\,16^{m+j}}$，
常函数循环、完整交换子交换及有界强多项式逼近也都已逐尾证明。
因此可保同一个函数 (1.4) 与同一位块，在每个原尾上构造相应最小闭乘子，
并得到 (1.7)--(8.1) 的完整逐尾版本。

R203 的旧结论只对 UHF 内的代数给出一般 RSC/可闭性障碍，并明确留下全
$\mathscr C$。本稿的新步骤是 (3.3) 的任意全交换子高块近似、
(5.5) 的固定非零外锚以及 (5.6)--(5.9) 的完整块范数上界；
它们把已付 R230 的有限块下界用于任何完整分母。

这里可直接接入已证 R136：各 $c_n\chi_{F_n}$ 依赖互不交的有限块、均值为零，
其 $L^2$ 能量之和为 $\sum_n c_n^2<\infty$；(2.3)--(2.4) 又已经支付
$\sum_n c_n\|V_{F_n}-D_{F_n}\|<\infty$ 的真实 carry 条件。
R136 的闭实现与 (1.6) 确实相同：其有限柱图核心按 (2.1) 全部属于最小轨道闭包；反向，多项式轨道图属于该闭实现。因此两图闭包一致。R136 随即给出有限柱图核心以及
$$
\boxed{
[f]_A=H,\qquad X_f^*=CX_fC,\qquad
\ker(X_f-\lambda I)=\{0\},\qquad
\overline{\operatorname{Ran}(X_f-\lambda I)}=H
\quad(\lambda\in\mathbb C).
}
\tag{9.1}
$$
两个实际代数轨道 $\mathscr C1$ 与 $\mathscr Cf$ 因而都稠密，但交集为零。
这里 $C$ 自伴性不表示通常自伴性；空点谱与稠密值域也不表示有界逆存在。
不可闭的代数投影 (7.1) 不作为闭不变投影使用，普通 ISP 仍未解决。
一般有理严格循环分解路线已在此候选上关闭；
针对某个已给闭根或真正湮灭见证的特殊同源分母仍须利用其额外方程，
不能把本稿的全次数坏来源自动换成那些特殊来源。

## 已证来源

- [R34：原最小闭轨道乘子与真实域交换](../results/R34-closed-cyclic-module-maps.md)；
- [R88：实际有界乘法与完整交换子强闭包](../results/R88-riesz-basis-bounded-multipliers-strong-closure.md)；
- [R136：独立有限块的无次数上界循环性、完整闭图及全部参数的单射稠密值域](../results/R136-disjoint-block-carleman-cyclicity.md)；
- [R170：任意有限柱乘子的闭性与原 UHF 障碍](../results/R170-locally-finite-tail-splitting-no-uhf-regularization.md)；
- [R203：原 RSC 定义、UHF 范围及当时开放的全交换子问题](../results/R203-uhf-rational-cyclicity-and-closability-obstructions.md)；
- [R230：任意有限交换块的 coherent-symbol 下界](../results/R230-appendix-arbitrary-contractive-block-gram-and-complete-source-obstruction.md)，特别其 §§2--3；完整旧证明保于该稿所链接的原笔记；
- H. Bercovici, R. G. Douglas, C. Foias, C. Pearcy,
  *Confluent operator algebras and the closability property*,
  J. Funct. Anal. 258 (2010), 4122--4153，
  [作者全文](https://arxiv.org/pdf/0908.0729)，Definition 4.1、Theorem 4.4。
  本稿的不可闭序列及“无任何 RSC 向量”均已独立给出证明。

