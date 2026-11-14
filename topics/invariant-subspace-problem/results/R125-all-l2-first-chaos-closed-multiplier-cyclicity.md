# R125：全部平方可和第一chaos及闭加性cocycle循环性

日期：2026-11-12 UTC。作者：Astra-ISP-0c017065。
状态：完整证明。l2_moments、literature 分别逐项核验纯 Dirac 算子、图核心、A 的域交换、gauge 同域等式及值域与循环空间的双包含；critical_kernel 独核闭算子版跨核配对。本文不由稠密循环类取极限。

## 1. 定理与实际接口

在本题原 Haar 表示
$$
H=L^2(\mathbb Z_2,\mu),\qquad (Au)(y)=w(y)u(y-1)
$$
中，令 $\chi_j(y)=(-1)^{\mathrm{bit}_j(y)}$。记
$$
H_q=\overline{\operatorname{span}}\{\chi_F:|F|=q\},\qquad
H_{\le p}=\bigoplus_{q=0}^pH_q.
$$

**主定理。** 对任意复系数 $a_*\in\mathbb C$、$a=(a_j)\in\ell^2$，
$$
0\ne f=a_*+\sum_{j\ge0}a_j\chi_j
\quad\Longrightarrow\quad
\boxed{\overline{\mathbb C[A]f}=H.}
\tag{1.1}
$$
没有绝对可和、相位、排列、稀疏性或尾速度假设。同一结论对 $A^*$ 成立。

证明构造一个稠密定义的闭乘子 $X_f$，使
$$
X_f1=f,\qquad X_f^*=CX_fC,\qquad
\overline{\operatorname{Ran}X_f}=\overline{\mathbb C[A]f},
\tag{1.2}
$$
并排除它的核。这里
$$
(Cu)(y)=\overline{u(-1-y)},\qquad
B(u,v)=\langle u,Cv\rangle=\int u(y)v(-1-y)\,d\mu(y),
\tag{1.3}
$$
通常内积约定对第一变量线性。在 Walsh 基上，
$$
C\chi_F=(-1)^{|F|}\chi_F
$$
并对系数取复共轭。

复用的实际一位恒等式为
$$
N_j=A^{2^j}/d_j=E_j+\eta_j E_j^*N_{j+1},
\quad N_j^2=\eta_jN_{j+1},
\quad \|N_j\|=1,\quad \|(I+N_j)^{-1}\|<3,
\tag{1.4}
$$
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad V_j1=\chi_j.
\tag{1.5}
$$
其中 $E_j$ 是物理第 $j$ 位从0到1的矩阵单位，
$\|N_j-E_j\|\le\eta_j$，且 $\eta\in\ell^2$。$A$ 单射、拟幂零，权重 $w>0$ 几乎处处；非零有限柱对 $A$ 循环。

## 2. 纯一位算子及逐次数估计

令
$$
V_j^0=I-2E_j.
$$
在第 $j$ 位的归一化 Walsh 基 $(1,\chi_j)$ 上，
$$
V_j^0=\begin{pmatrix}0&-1\\1&2\end{pmatrix}.
\tag{2.1}
$$
定义有界的单坐标创建、删除及占据算子
$$
c_j\chi_F=
\begin{cases}\chi_{F\cup\{j\}},&j\notin F,\\0,&j\in F,\end{cases}
\quad
c_j^*\chi_F=
\begin{cases}\chi_{F\setminus\{j\}},&j\in F,\\0,&j\notin F,\end{cases}
$$
$$
P_j\chi_F=1_{\{j\in F\}}\chi_F.
$$
由 (2.1)，
$$
V_j^0=c_j-c_j^*+2P_j.
\tag{2.2}
$$

设
$$
\mathcal D=\bigcup_{p\ge0}H_{\le p}.
$$
这是稠密线性域，不仅包含有限柱，也包含任意有限次数的无限支撑向量。在 $\mathcal D$ 上定义
$$
\mathsf C(a)=\sum_j a_jc_j,\quad
\mathsf A(a)=\sum_j a_jc_j^*,\quad
\mathsf D(a)\chi_F=\left(\sum_{j\in F}a_j\right)\chi_F.
$$
这些和在每个 $H_{\le p}$ 上按算子范数收敛。准确层估计为
$$
\|\mathsf C(a):H_q\to H_{q+1}\|\le\sqrt{q+1}\|a\|_2,
\quad
\|\mathsf A(a):H_q\to H_{q-1}\|\le\sqrt q\|a\|_2,
\tag{2.3}
$$
$$
\|\mathsf D(a)|_{H_q}\|\le\sqrt q\|a\|_2.
\tag{2.4}
$$
例如创建输出在 $F$ 的系数是
$\sum_{j\in F}a_jx_{F\setminus\{j\}}$；先用 $q+1$ 项 Cauchy，再对 $F$ 求和，得到第一界。删除界由
$\mathsf A(a)=\mathsf C(\bar a)^*$ 在相邻层上的关系得到。占据界由
$|\sum_{j\in F}a_j|\le\sqrt q\|a\|_2$。把相同证明用于系数尾，即得所称算子范数收敛。

故纯乘子
$$
T_0=a_*I+\mathsf C(a)-\mathsf A(a)+2\mathsf D(a)
\quad\text{定义于 }\mathcal D
\tag{2.5}
$$
以及其形式通常伴随
$$
T_0^\dagger=\bar a_*I+\mathsf A(\bar a)-\mathsf C(\bar a)+2\mathsf D(\bar a)
=CT_0C
\quad\text{定义于 }\mathcal D
\tag{2.6}
$$
都把 $H_{\le p}$ 映入 $H_{\le p+1}$，并满足
$$
\|T_0x\|,\ \|T_0^\dagger x\|
\le K\sqrt{p+1}\|x\|,
\qquad K=|a_*|+4\|a\|_2.
\tag{2.7}
$$
层与层正交使 (2.3)—(2.4) 可直接用于整个 $H_{\le p}$。有限坐标近似或逐层求和给
$\langle T_0x,y\rangle=\langle x,T_0^\dagger y\rangle$，$x,y\in\mathcal D$。

## 3. Dirac 块的本质自伴：自含解析向量证明

在 $\mathcal D\oplus\mathcal D$ 上置
$$
\mathscr L_0=
\begin{pmatrix}0&T_0^\dagger\\T_0&0\end{pmatrix}.
\tag{3.1}
$$
它稠密定义且对称。由 (2.7)，对
$x\in H_{\le p}\oplus H_{\le p}$，
$$
\|\mathscr L_0^n x\|
\le K^n\sqrt{\frac{(p+n)!}{p!}}\|x\|.
\tag{3.2}
$$
因此对每个实数 $t$，级数
$$
U(t)x=\sum_{n=0}^\infty\frac{(it)^n}{n!}\mathscr L_0^nx
\tag{3.3}
$$
以及逐项施加一次 $\mathscr L_0$ 后的级数，均在每个有界 $t$ 区间一致范数收敛。对称算子可闭，记其闭包为 $\mathscr L$。部分和在定义域内，闭性给
$$
U(t)x\in\operatorname{Dom}\mathscr L,\qquad
\frac d{dt}U(t)x=i\mathscr L U(t)x.
$$
$\mathscr L$ 对称，故
$$
\frac d{dt}\|U(t)x\|^2
=2\operatorname{Re}\langle i\mathscr L U(t)x,U(t)x\rangle=0.
$$
于是 $\|U(t)x\|=\|x\|$。

若 $\xi\in\ker(\mathscr L_0^*-i)$，在 (3.3) 逐项配对：
$$
\langle U(t)x,\xi\rangle=e^t\langle x,\xi\rangle.
$$
左端绝对值不超过 $\|x\|\|\xi\|$；令 $t\to+\infty$，得
$\langle x,\xi\rangle=0$。稠密性给 $\xi=0$。对
$\ker(\mathscr L_0^*+i)$ 令 $t\to-\infty$ 同样得到零。

为明确最后的闭算子步骤，对称闭 $\mathscr L$ 满足
$$
\|(\mathscr L\pm i)x\|^2=\|\mathscr Lx\|^2+\|x\|^2,
$$
故两像闭；其正交补分别为上述零缺陷核，所以两像也稠密，因而等于全空间。这推出 $\mathscr L=\mathscr L^*$。例如对
$z\in\operatorname{Dom}\mathscr L^*$，选择
$y\in\operatorname{Dom}\mathscr L$ 使
$(\mathscr L-i)y=(\mathscr L^*-i)z$；差 $z-y$ 属于零缺陷核，故 $z=y$。
因此 $\mathscr L_0$ 本质自伴。整个论证无需先证明 (3.3) 的群律。

$T_0,T_0^\dagger$ 都可闭。块算子的图范数分解成两部分，因此
$$
\overline{\mathscr L_0}
=\begin{pmatrix}0&\overline{T_0^\dagger}\\\overline{T_0}&0\end{pmatrix},
\quad
\operatorname{Dom}\overline{\mathscr L_0}
=\operatorname{Dom}\overline{T_0}\oplus
\operatorname{Dom}\overline{T_0^\dagger}.
$$
由该块算子自伴，
$$
\boxed{\overline{T_0}^{\,*}=\overline{T_0^\dagger}
=C\overline{T_0}C.}
\tag{3.4}
$$

## 4. 实际进位作为有界 C 对称差；有限柱图核心

由 (1.4)，
$$
V_j-(I-2N_j)=2N_j^2(I+N_j)^{-1}.
$$
因此
$$
\|V_j-V_j^0\|
\le 2\|N_j-E_j\|+2\|N_j^2(I+N_j)^{-1}\|
\le8\eta_j.
\tag{4.1}
$$
Cauchy 给 $\sum_j|a_j|\eta_j<\infty$，所以
$$
K_a=\sum_j a_j(V_j-V_j^0)
\tag{4.2}
$$
按算子范数绝对收敛。实际 $V_j$ 与纯 $V_j^0$ 均 C 对称；故
$K_a^*=CK_aC$。

定义闭算子
$$
\boxed{
X_f=\overline{T_0}+K_a,\qquad
\operatorname{Dom}X_f=\operatorname{Dom}\overline{T_0}.
}
\tag{4.3}
$$
有界扰动保持闭性；通常伴随的有界扰动公式及 (3.4) 给
$$
X_f^*=\overline{T_0}^{\,*}+K_a^*=CX_fC.
\tag{4.4}
$$
这是包含定义域的等式。

在 $\mathcal D$ 上，有限实际乘子
$$
X_n=a_*I+\sum_{j<n}a_jV_j
\tag{4.5}
$$
满足 $X_nx\to X_fx$。这个收敛来自纯部分的 (2.3)—(2.7) 与
(4.2) 的范数收敛。特别地 $X_f1=f$。

记 $\mathcal P$ 为所有有限柱向量。它是 $X_f$ 的图核心：对任意
$x\in H_{\le p}$，取前 $m$ 位条件期望 $x_m$，则 $x_m\in\mathcal P\cap H_{\le p}$，
$x_m\to x$；(2.7) 给 $T_0x_m\to T_0x$，有界 $K_a$ 给实际图收敛。
而 $\mathcal D$ 本来是 $\overline{T_0}$ 的图核心，有界扰动不改变核心。
因此 $\mathcal P$ 同时是 $X_f$ 的图核心。由 $C\mathcal P=\mathcal P$，
它也是 $X_f^*$ 的图核心。

注意实际 $K_a$ 未必把有限次数空间映到有限次数空间。因此本证明只对纯
Dirac 算子迭代 (3.2)，随后才加入有界实际差；没有对实际算子错误地使用有限次数幂估计。

## 5. 与 A 的定义域交换，以及闭值域恰为循环空间

更强地，对每个有界交换子 $T\in\{A\}'$，
$$
T\operatorname{Dom}X_f\subseteq\operatorname{Dom}X_f,
\qquad X_fTx=TX_fx.
\tag{5.1}
$$
先取 $x,z\in\mathcal D$。每个 $X_n$ 有界、B 对称并与 $T$ 交换，所以
$$
B(Tx,X_fz)
=\lim_n B(Tx,X_nz)
=\lim_n B(TX_nx,z)
=B(TX_fx,z).
\tag{5.2}
$$
因为 $\mathcal D$ 为 $X_f$ 图核心，(5.2) 对全部
$z\in\operatorname{Dom}X_f$ 成立。由 C 自伴性 (4.4)，伴随定义恰说明
$Tx\in\operatorname{Dom}X_f$ 且 $X_fTx=TX_fx$。
最后对任意域内 $x$ 用 $\mathcal D$ 的图逼近，再用 $T$ 有界及 $X_f$ 闭性，得到 (5.1)。

这里没有假设 $Ax$ 仍有有限 chaos 次数；这是使用伴随定义的原因。

令
$$
M_f=\overline{\mathbb C[A]f}.
$$
每个有限柱 $u$ 有实际有理解析乘子 $X_u\in\mathcal A$，满足
$X_u1=u$。由有限柱乘子公式及交换性，
$$
X_nu=X_uX_n1\longrightarrow X_uf.
$$
故
$$
X_fu=X_uf\in M_f\qquad(u\in\mathcal P).
\tag{5.3}
$$
$\mathcal P$ 的图核心性质给
$\overline{\operatorname{Ran}X_f}\subseteq M_f$。

反向，$1\in\operatorname{Dom}X_f$、$X_f1=f$，而 (5.1) 取 $T=A$ 后给
$A^n1\in\operatorname{Dom}X_f$ 且 $A^nf=X_fA^n1$。所以
$$
\boxed{\overline{\operatorname{Ran}X_f}=M_f.}
\tag{5.4}
$$
不需要断言 $A^n1$ 是有限柱或有限次数向量。

## 6. 有限 dyadic gauge 给同定义域的解析差

设 $\zeta^{2^m}=1$，令
$$
(U_\zeta u)(y)=\zeta^{\,y\bmod2^m}u(y),\qquad
\gamma_\zeta(T)=U_\zeta TU_\zeta^*.
$$
实际权移满足 $\gamma_\zeta(A)=\zeta A$。乘以这个有限柱函数将
$H_{\le p}$ 送入 $H_{\le p+m}$，故
$$
U_\zeta\mathcal D=\mathcal D,\qquad U_\zeta\mathcal P=\mathcal P.
\tag{6.1}
$$
当 $n\ge m$，有限部分有精确恒等式
$$
U_\zeta X_nU_\zeta^*-X_n=F_\zeta(A),
\tag{6.2}
$$
其中右端与 $n$ 无关，来自有限解析芽
$$
F_\zeta(z)=
\sum_{j<m}a_j\left[
\frac{d_j-\zeta^{2^j}z^{2^j}}{d_j+\zeta^{2^j}z^{2^j}}
-\frac{d_j-z^{2^j}}{d_j+z^{2^j}}
\right].
\tag{6.3}
$$
先在 $\mathcal D$ 上取 $n\to\infty$。由 (6.1)，左右两个闭算子均以
$\mathcal D$ 为图核心；右侧是 $X_f$ 的有界扰动。取闭包即得包含域的等式
$$
\boxed{
U_\zeta X_fU_\zeta^*=X_f+F_\zeta(A),\qquad
U_\zeta\operatorname{Dom}X_f=\operatorname{Dom}X_f.
}
\tag{6.4}
$$
单有共同核心上的形式等式不够；(6.4) 明确由双方图核心及有界扰动导出。

若 $a$ 非零，令 $j_0=\min\{j:a_j\ne0\}$、$h=2^{j_0}$。对
$\zeta^h\ne1$，(6.3) 的首阶恰为 $h$，首系数
$$
-2a_{j_0}(\zeta^h-1)/d_{j_0}\ne0.
$$
因而
$$
F_\zeta(A)=A^hG_\zeta(A),\qquad G_\zeta(0)\ne0,
\tag{6.5}
$$
$G_\zeta$ 是真正收敛解析芽，$G_\zeta(A)$ 及其逆均属于 $\mathcal A$。

## 7. 闭算子跨核、有限 Fourier 支撑与核排除

设 $M=\ker X_f$。它闭，由 (5.1) 对 $A$ 不变。假设 $M\ne0$。
每个闭 A 不变子空间满足
$$
\overline{A^rM}=M\qquad(r\ge1).
\tag{7.1}
$$
可直接用 $N_j\to I/2$ 弱收敛：充分大 $j$ 有 $N_jM\subseteq A^rM$，
而闭线性空间弱闭，故每个 $x/2$ 属于 $\overline{A^rM}$。

由 (6.4)，
$$
M_\zeta=U_\zeta M=\ker(X_f+F_\zeta(A)).
$$
取 $v\in M$、$z\in M_\zeta$。**两向量都在 (6.4) 的同一个定义域中。**
$X_f+F_\zeta(A)$ 是 B 对称的，故
$$
B(F_\zeta(A)v,z)
=B((X_f+F_\zeta(A))v,z)
=B(v,(X_f+F_\zeta(A))z)=0.
\tag{7.2}
$$
对 $\zeta^h\ne1$，(6.5)、(7.1) 及单位保持 $M$ 给
$\overline{F_\zeta(A)M}=M$，所以
$$
B(M,U_\zeta M)=0\qquad(\zeta^h\ne1).
\tag{7.3}
$$

对任意 $v,w\in M$，函数 $q(y)=v(y)w(-1-y)$ 属于 $L^1$，且
$$
B(v,U_\zeta w)=\zeta^{-1}\int q(y)\overline{\zeta^y}\,d\mu(y).
$$
(7.3) 使 $q$ 的 Fourier 系数仅可能位于 $\zeta^h=1$ 的 $h$ 个字符上。
前 $m$ 位条件期望的有限 Fourier 展开及 $L^1$ 收敛给
$$
q\text{ 在每个 }y\bmod h\text{ 的物理柱上为常数。}
\tag{7.4}
$$

下面完整重述此有限 Fourier 结论的维数后果。取 $M$ 的可数稠密族
$(v_n)$，总本质支撑
$$
E=\bigcup_n\{v_n\ne0\}
$$
包含每个 $M$ 向量的本质支撑。由 $A$ 不变及 $w>0$ 几乎处处，
$E+1\subseteq E$ 模零；平移保 Haar 测度，故模零相等。
odometer 遍历性及 $M\ne0$ 给 $\mu(E)=1$。

于是对每个正测的物理柱 $Q_i=\{y:y\bmod h=i\}$，可从可数向量对中选
$v_i,w_i\in M$，使 $v_i(y)w_i(-1-y)$ 在柱内一个正测集上非零。
由 (7.4)，该乘积在整个柱上等于一个非零常数 $c_i$。
对任意 $u\in M$，$u(y)w_i(-1-y)$ 同样是柱常数 $d_i(u)$，所以
$$
u|_{Q_i}=\frac{d_i(u)}{c_i}\,v_i|_{Q_i}.
$$
每柱限制至多一维，共 $h$ 个柱，故 $\dim M\le h$。

但单射拟幂零 $A$ 没有非零有限维不变子空间：在这样的空间上其谱仍只有0，
有限维必有零特征向量，与单射性矛盾。故 $M=0$。

若 $a=0$，非零 $f$ 是常数，$X_f=a_*I$ 本来单射满射。因此全部非零
$f\in H_{\le1}$ 都有 $\ker X_f=0$。由 C 自伴性，
$$
\ker X_f^*=C\ker X_f=0,
$$
闭值域稠密。结合 (5.4)，主定理成立。

## 8. 直接推论与仍在开放的范围

1. 对每个固定非零 $g\in H$，
   $$
   \{f\in H_{\le1}:B(A^nf,g)=0\ \forall n\ge0\}=\{0\}.
   $$
   因此 R104 的第一层坏集现在为空；原来的有限维/无内点估计依然有效，但不再是未决边界。
2. 每个真闭 A 不变子空间与 $H_{\le1}$ 交为零。因为 $C$ 保持
   $H_{\le1}$、$A^*=CAC$，全部非零第一 chaos 也对 $A^*$ 循环；故每个非零
   A 不变子空间的正交补同样与 $H_{\le1}$ 交为零。
3. 若 $a\ne0$，对每个 $\lambda\in\mathbb C$，$X_f-\lambda I$ 正是同一域上的
   $X_{f-\lambda}$。故所有这些闭算子都单射且值域稠密。不声称它们都有有界逆；
   预解集及连续谱可随系数改变。
4. 本证明完成的是**一个受限输入对任意 H 端点**的循环性，已严格强于
   两端有限 chaos 的矩分离。它尚未证明所有有限二阶或更高次数输入循环，
   也未处理任意 $L^2$ 输入。完整普通 ISP 仍未解决。

依赖：R9/R13 的实际算子恒等式，R11 有限柱乘子及循环性，
R24 的 B 对称，R12/R23 的限制稠密幂值域（§7已重证），
R122 的有限 Fourier 核机制（§7完整重证）。

## 9. 闭加性 cocycle 的一般形式与有界非解析扰动

以下推广也已由 critical_kernel 独立核验，特别核对了“全部 gauge 固定”在无界域上的含义。

**定理 9.1。** 设 $T$ 是稠密定义的闭算子，满足：

- $T^*=CTC$；
- 有限柱空间 $\mathcal P$ 是 $T$ 的图核心；
- 每个 $D\in\{A\}'$ 保持 $\operatorname{Dom}T$ 且 $TD=DT$ 于该域；
- 对每个 dyadic $\zeta$，存在真正收敛解析芽 $F_\zeta$，使
  $$
  U_\zeta TU_\zeta^*=T+F_\zeta(A)
  \tag{9.1}
  $$
  为包含定义域的等式。

若 $T$ 非标量，则对每个 $\lambda\in\mathbb C$，
$$
\ker(T-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(T-\lambda I)}=H,\qquad
(T-\lambda I)1\text{ 对 }A\text{ 循环}.
\tag{9.2}
$$
非零标量情形同样给 $T1$ 循环，但不包含产生零算子的参数。

**证明。** 设 $G$ 为全部 dyadic 单位根，令
$$
G_T=\{\zeta\in G:U_\zeta TU_\zeta^*=T\}.
$$
这是群作用的稳定子，因而是子群。Prüfer 2 群的每个真子群均为某个有限
$\mu_h$：若子群元素的阶无界，它含每个 $\mu_{2^m}$，从而为整个 $G$。

假设 $G_T=G$。置 $g=T1\in H$。由所有有限柱字符的固定性，对每个
有限柱 $u$ 有
$$
Tu=gu.
\tag{9.3}
$$
最大点乘算子
$$
M_g:\{u\in H:gu\in H\}\to H,\qquad M_gu=gu
$$
是闭算子；可由图收敛的共同几乎处处子列直接证明。因此有限柱图核心和
(9.3) 给 $T\subseteq M_g$。这里不需要先证明 $g\in L^\infty$。

又 $A1=w$ 属于 $\operatorname{Dom}T$，并且
$$
T A1=A T1=w(y)g(y-1).
$$
由 $T\subseteq M_g$，左边同时等于 $g(y)w(y)$。因为 $w>0$ 几乎处处，
$g(y)=g(y-1)$；odometer 遍历性使 $g$ 是常数 $c$。于是
$T\subseteq cI$。$T$ 闭且定义域稠密，而 $cI$ 的图范数与通常范数等价，
故该定义域同时闭，必为全 $H$。这使 $T=cI$，与非标量假设矛盾。

所以 $G_T=\mu_h$ 有限。对 $\zeta\notin\mu_h$，(9.1) 的差不为零；
因此 $F_\zeta$ 是非零解析芽，精确分解为
$A^{r_\zeta}$ 乘 $\mathcal A$ 的解析单位。对于
$M=\ker(T-\lambda I)$，域交换保证闭 A 不变性，(9.1) 保证共轭核两端同域。
§7 的跨核证明于是逐字适用：非例外的差在 $M$ 上稠密，核乘积仅有
$\mu_h$ 的 Fourier 支撑，进而 $\dim M\le h$，故 $M=0$。
C 自伴给值域稠密。

最后，对有限柱 $u=X_u1$，域交换给
$$
(T-\lambda I)u=X_u(T-\lambda I)1.
$$
有限柱图核心与 A 域交换分别给两个包含，故
$$
\overline{\operatorname{Ran}(T-\lambda I)}
=\overline{\mathbb C[A](T-\lambda I)1}.
$$
得到循环性。证毕。

**推论 9.2。** 设 $f\in H_{\le1}$，$D\in\{A\}'$ 有界，且每个
$\gamma_\zeta(D)-D$ 都是真正解析芽作用于 $A$。则
$$
\boxed{f+D1\ne0\quad\Longrightarrow\quad f+D1\text{ 对 }A\text{ 循环}.}
\tag{9.4}
$$
若 $f$ 的第一阶系数不在 $\ell^1$，则 $f+D1-\lambda$ 对每个
$\lambda$ 都非零且循环。

事实上，取 $T=X_f+D$。有界扰动保持闭性、C 自伴及有限柱图核心；
全交换子交换性保持域交换。两个加性解析差相加，给 (9.1)。
若 $T$ 非标量，定理适用；若为非零标量，直接得到结论。
若 $T1=0$，有限柱图核心与域交换使 $T=0$，这正是 (9.4) 明确排除的情形。

当 $f$ 的系数不在 $\ell^1$ 时，$X_f$ 不可能有界，否则它将是
$f$ 的有界实际乘子，与 R88 的精确第一 chaos 判据矛盾。因此加入有界
$D$ 后 $T$ 仍无界，必非标量，最后的全参数断言成立。

R123 的局部有限有界乘子全部可作为这里的 $D$；因而可把任意复
$\ell^2$ 第一 chaos 加上这些任意高次数扰动，而保持非零时循环。
本推论没有把 $D$ 扩大为任意有界交换子：其有限 gauge 差的解析性仍是必要的已用假设。
