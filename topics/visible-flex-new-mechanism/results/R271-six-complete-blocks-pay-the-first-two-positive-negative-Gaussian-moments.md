# R271：六个最终完整 block 同时支付正负 Gaussian 面积的前两外矩

日期：2026-11-15。**完整纸面建设性证明；未执行 profile 求积、参数扫描、符号程序或研究计算。**

本稿接 [R270 的真实四变量分支](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、[R269 的两种真实排序](R269-reordered-real-masses-pay-a-complete-Gaussian-zero-moment.md)及 [R273 自动支付的另一第零外矩](R273-reflection-densities-pay-the-minus-one-minus-two-zero-moment.md)。新增的是 $A_{1,-3}$ 的整个第一外矩，同时保留其已经支付的整个第零外矩。

先从原算子证明一个容易误用的事实：合法复 profile 的 pure 第一外矩恒零，但完整圆仍有一个有序 even 条件。然后准确计算该条件在两种排序中的相反号。六个 block 全部在最后位置先解原四变量方程，之后仅使用正四次幅度，先清 pure 标量，再同时配平两个完整外矩。不把 span 或任意有符号系数当作实际可达。

共同物理区间在最终 profile 定义以前一次选定。下文明确需要一个能够容纳六个指定正位置的共同合法 I；不默默扩大已冻结的任意窄 I，不把改变圆及 seed 称为保持旧目标的变形。

## 1. 固定原三槽与三个外矩

写 $P=\Phi_{r_0}$、$Y=\Phi_{p_2}$，仍取同一真实右锚
$J(F)(x)=\int_x^{r_*}F(t)\,dt$。外矩 $I_0,I_1,I_2$ 完全按 [R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)，特别

$$
I_2(u,v)=\int(x^2u''v''+2u'v').
$$

对真实三矩圆

$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta
$$

定义

$$
\mathcal A_j(\theta)
=2I_j\{\phi_\theta,[P,Y](\phi_\theta;D_\theta)\},
\qquad j=0,1,2.
\tag{1}
$$

共振端芽的 $[B_1,B_{-3}]=-\zeta c[P,Y]$，其中原 $\zeta c\ne0$。所以检验 (1) 的零恰是同一个原 Gaussian 面积的零，不改系数或原问题。

以下始终保 outer $\phi_\theta$ 与 inner $D_\theta$ 的不同槽。只在明确使用合法复 profile $q=f+ig$ 的一条原恒等式时取对角。

## 2. 任意 nonlegal 单包的第一 self 矩

令 $u$ 为任意实或复紧 profile，$v=u'$、$r=u''$，并记

$$
A=J(r^2),\qquad C_2=J(x^2r^2+2v^2),\qquad
m_j=I_j(u,u).
$$

不要求 $m_j=0$。原二次输出为

$$
P(u,u)=A,\qquad
Y(u,u)=-xu^2+x^2uv-\frac{x^3v^2}{2}-\frac{x^2C_2}{4}.
\tag{2}
$$

[R257](R257-cumulative-primitive-energy-in-the-complete-positive-negative-Gaussian-area.md) 的原二导与 R259 的完整 IBP 给

$$
F_{P,1}(u)=I_1(u,P(u,u))=\frac23\int r^3,
$$

$$
\boxed{
F_{Y,1}(u)=
\int\left(
x^2ur^2-x^3vr^2+\frac{x^4r^3}{6}
+2uv^2-\frac23xv^3
\right).
}
\tag{3}
$$

(3) 也可由 R259 的原 $\mathscr V$ 递推逐项取得；末两项来自完整总导数，不能略去。

令

$$
\mathcal K=
\frac83xur^3-\frac83x^2vr^3+\frac23x^3r^4
-4uvr^2+2xv^2r^2.
$$

沿原二次方向作 local 变分并完整 IBP，准确得到

$$
DF_{P,1}[Y(u,u)]=\int(\mathcal K-C_2r^2),
$$

$$
DF_{Y,1}[P(u,u)]
=\int\{\mathcal K+A(x^2r^2+2v^2)\}.
\tag{4}
$$

因此差为

$$
-\int\{C_2r^2+A(x^2r^2+2v^2)\}
=[AC_2]_{\rm left}^{\rm right}
=-m_0m_2.
\tag{5}
$$

这里原左尾 $A=m_0,C_2=m_2$ 一直保留。

local 变分还须加原 $I_1$ Green 项。采用进入 self 的符号，其 concomitant 为

$$
x(X'''Y-X''Y'+X'Y''-XY''')+X''Y-XY''.
$$

$P$ 的左尾是 $m_0$，$Y$ 的左尾是 $-m_2x^2/4$，所以该边项准确为 $+m_0m_2/2$。结合 (5)，

$$
\boxed{
\mathsf S_{P,Y,1}(u)
:=2I_1\{u,[P,Y](u;u\odot u)\}
=-\frac12m_0m_2.
}
\tag{6}
$$

这是任意紧单包的原式，不曾把其二次输出假设为紧。它与 R259 的跨包核

$$
\boxed{
\Gamma_{P,Y,1}(\mathbf m,\mathbf n)
=-\frac12(m_0n_2+m_2n_0)
}
\tag{7}
$$

必须共同使用。

## 3. Pure 零只减少一项，不能删掉完整第一外矩

合法三矩圆的 $q=f+ig$ 满足 $I_j(q,q)=0$。式 (6) 的复多项式延拓于是给

$$
2I_1\{q,[P,Y](q;q\odot q)\}=0.
\tag{8}
$$

将同一完整三槽写成 R259 的四角系数

$$
\mathcal A_1(\theta)
=E_{31}\cos^3\theta\sin\theta
+E_{22}\cos^2\theta\sin^2\theta
+E_{13}\cos\theta\sin^3\theta
+E_{04}\sin^4\theta,
$$

原对角四次展开给

$$
\operatorname{Re}(8)=E_{22}-E_{04},\qquad
\operatorname{Im}(8)=E_{13}-E_{31}.
$$

故

$$
E_{22}=E_{04},\qquad E_{13}=E_{31},
\quad
\mathcal A_1(\theta)=E_{31}\cos\theta\sin\theta+E_{04}\sin^2\theta.
\tag{9}
$$

原十二完整副本已经清掉 odd 系数 $E_{31}$，但 $E_{04}$ 仍须支付。下文支付的正是这个完整 mixed 条件，而不是再次证明 (8)。

## 4. 两种排序的准确有序第一矩

使用 R269/R270 的同一个实际 even 母包 $u$，记

$$
m=\int(u'')^2>0,\qquad \nu=I_2(u,u)/m,\qquad n=2^{11},
$$

$$
q=\frac1{16(1-\alpha)^2},\quad
\beta=\frac{5-\alpha}{1-\alpha},\quad
a=q(1-\alpha)>0.
$$

$1/3<\alpha<1/2$。低/高宽度比为 $q,1$；实平方幅度为 $(\alpha q,q)$ 与 $(\beta,1)$。将

$$
B_i=b_i^2,\qquad R_i=a_i^2-b_i^2
$$

作为本节的质量权，便有低 $(B_i,R_i)=(q,-a)$，高 $(1,64a)$。不要把 $B_i$ 与几何 Gaussian 算子混记。

在 block 中心 $\xi_0$、主宽 $\delta>0$，第 i 个普通外包的原矩为

$$
m_{0,i}=m,\quad m_{1,i}=m(\xi_0+\delta t_i),\quad
m_{2,i}=m\{(\xi_0+\delta t_i)^2+\nu\delta^2w_i^2\},
\quad w_i\in\{q,1\}.
\tag{10}
$$

对 $\theta=\pi/2$，式 (6)—(7) 给

$$
E_{04}^{(1)}
=-\frac{m^2}{2}
\left[
\sum_iB_iR_i v_i+
\sum_{i<j}B_iR_j(v_i+v_j)
\right],
\quad
v_i=(\xi_0+\delta t_i)^2+\nu\delta^2w_i^2.
\tag{11}
$$

原 companion 必须按其真实内部子包理解。但在 $\theta=\pi/2$，outer 的 local quadratic 密度及 inner $f\odot f-g\odot g$ 都只含同源偶数次乘积；R270 的逐子包符号替换保留这些乘积。因此 (11) 对普通版与 companion 版准确相同，不能据此宣其 odd 系数相同。

两种排序的真实平方幅度、宽度和中心都在反序后保持镜像配对。真实三矩给

$$
\sum R_i=\sum R_it_i
=\sum R_i(t_i^2+\nu w_i^2)=0.
\tag{12}
$$

对任意两个序列 $R_i,B_i$，一个上三角对称核与其反序核之和是对应总矩的乘积。将此恒等式分别用于常数核和
$v_i^0=t_i^2+\nu w_i^2$，由 (12) 及镜像对称得

$$
U_{00}:=\sum B_iR_i+2\sum_{i<j}B_iR_j=0,
$$

$$
U_{02}:=\sum B_iR_i v_i^0+
\sum_{i<j}B_iR_j(v_i^0+v_j^0)=0.
\tag{13}
$$

所以 (11) 准确化为

$$
\boxed{
E_{04}^{(1)}=-m^2\xi_0\delta\,U_{01},
\quad
U_{01}=\sum B_iR_i t_i+
\sum_{i<j}B_iR_j(t_i+t_j).
}
\tag{14}
$$

宽度项 $\nu w_i^2$ 没有被删：它正是 (12)—(13) 中必须一起保留的原第二矩。

### 4.1 完整 cell 求和

写 $c=(n-1)/2$，低中心为

$$
t^L_{k,l}=64A(k-c)+A(l-31.5),\quad 0\le l<64,
$$

高中心为

$$
t^H_k=B_\rho(k-c)+\rho A\sigma_k,\quad
\rho\in\{0,20\},\quad
\sigma_k=(-1)^{\operatorname{popcount}(\lfloor k/4\rfloor)}.
$$

$B_\rho$ 是间距，不是质量权。准确方差式为

$$
B_\rho^2=
\frac{A^2((64n)^2-1)-12\nu(1-q^2)-12\rho^2A^2}{n^2-1}.
\tag{15}
$$

采用 R269 已证明的真实次序；在高点以前有
$m_k=32+\rho\sigma_k$ 个低点。令
$T_k=64A(k-c)$、
$z_k=(B_\rho-64A)(k-c)+\rho A\sigma_k$。

逐点写

$$
B_i=zR_i+w,\qquad
z=\frac{1-q}{65a},\qquad w=\frac{64q+1}{65}.
$$

$z$ 部分的完整 $U_{01}$ 为
$(\sum R_i)(\sum R_it_i)=0$。剩余部分以全局从0编号的 j 表示为

$$
w\sum_jR_j\left((j+1)t_j+\sum_{i<j}t_i\right).
$$

一个 cell 的括号和准确为

$$
65az_k(m_k+64k)
+130a\rho\sigma_k T_k
+\frac{65aA}{2}m_k(m_k-64).
\tag{16}
$$

它使用全局位置；不能提前丢掉 cell 中心项。用
$\sum\sigma_k=\sum(k-c)\sigma_k=0$、
$\sum(k-c)^2=n(n^2-1)/12$，最后得到

$$
\boxed{
U_{01}
=na(64q+1)\left\{
\frac{16}{3}(B_\rho-64A)(n^2-1)
+A\left(\frac32\rho^2-512\right)
\right\}.
}
\tag{17}
$$

这是有限正宽的准确有序和，未取连续分布或大 n 极限。

### 4.2 两种排序的严格相反号

仍有 $A>\sqrt\nu$。在 $\rho=0$，

$$
0<(B_0-64A)(n^2-1)
=\frac{4095A^2-12\nu(1-q^2)}{B_0+64A}
<\frac{4095}{128}A.
$$

故 (17) 的花括号严格小于 $-2731A/8$，所以 $U_{01}^{(0)}<0$。

在 $\rho=20$，R269 已付 $63A<B_{20}<64A$，且

$$
(B_{20}-64A)(n^2-1)
=\frac{-705A^2-12\nu(1-q^2)}{B_{20}+64A}.
$$

其负项绝对值小于 $717A/127$。于是 (17) 的花括号严格大于

$$
\left(88-\frac{3824}{127}\right)A
=\frac{7352}{127}A>0,
$$

故 $U_{01}^{(20)}>0$。由 (14)，在正中心 $\xi_0$ 上，第一 even 矩在居中排列为正、在重排排列为负。

## 5. 完整副本与最终位置的严格比值

原八层和十二层复制全部使用真实完整 base，正四次权和记作 $\mathcal W>0$。每个 base 内槽 $D_\theta$ 的三矩为零，因此不同完整副本之间的 (7) 跨项准确为零。odd 系数仍由原十二副本消去。

各层复制的四次加权中心已在主 IFT 前准确置为零。$U_{00}=0$ 使 $U_{01}$ 对共同平移不变；(14) 在一次平移以后只将 $\xi_0$ 换成新的中心。因此整个已包装 block 的准确第一 even 矩为

$$
S_1:=E_{04}^{(1)}
=-\mathcal Wm^2\xi_0\delta U_{01}.
\tag{18}
$$

这是同一母参数在实际主 IFT 解上取值。不会在求根后搬移已选 block。

记该完整 block 的第零 even 矩为 $S_0$。R269 的原式仍给

$$
\frac{S_0}{\mathcal W\delta}
=na\left[
m^2A\{10928q-(32q+1)\rho^2\}
+64(1-q^2)\mathcal B
\right],
$$

$$
\mathcal B=C\nu-\mathcal L+\Delta/4>0.
\tag{19}
$$

所以 $\rho=0$ 时 $S_0>0$；先固定母宽、再选择足够大的有限间距 A，便在 $\rho=20$ 时严格 $S_0<0$。同一个有限 A 也给 R265/R269 的两个 pure 标量严格号
$\mathscr Q_-<0<\mathscr Q_+$。这里的 $\mathscr Q$ 完全是 R257 的原泛函，不引入新的测试目标。

固定一个允许的非零小 $\kappa$ 及实际小母宽 h。在 $\delta=0$ 的准确归一方程中，R270 的母根与 $\alpha_0$ 不依赖最后中心 $\xi_0$：第一主行的 simple root 仍为原 $P(\alpha_0)=0$；其余三行准确为母 $\mathcal H,\mathcal F_\kappa,\mathcal J/h$。因此可在选定的有限多个中心使用同一基点，并分别应用原四变量 IFT。

记两种排序在此共同基点的真实常数为

$$
s_\rho=\lim_{\delta\to0}\frac{S_0}{\mathcal W\delta},
\qquad
t_\rho=\lim_{\delta\to0}\frac{S_1}{\mathcal W\delta\,\xi_0},
\qquad
k_\rho=\frac{t_\rho}{s_\rho}.
\tag{20}
$$

(17)—(19) 已证明

$$
s_0,t_0>0,\qquad s_{20},t_{20}<0,\qquad
k_0,k_{20}>0.
\tag{21}
$$

这些是由真实形状积分定义的固定数；不需要数值求积或把它们冒作自由坐标。原源给出的归一函数和 IFT 都真实连续，故在任何已固定的有限正中心集合，

$$
\frac{S_1}{S_0}\longrightarrow k_\rho\xi_0
\quad(\delta\to0)
\tag{22}
$$

且两个严格号保留到充分小的实际正 $\delta$。

普通与 companion 在同一母基点有相同的 (19)、(20)，尽管它们的 pure $\mathscr Q$ 具有相反号。真正构造时这两个 block 必须放在不同的最后区间；下节仅用其中心在一个小邻域内，绝不把两个有重叠支撑的 profile 直接相加。

## 6. 先固定六个最后位置，再解各自原方程

先选择三个互不交的小正中心区间 $J_L,J_M,J_R$，使

$$
\boxed{
k_0\sup J_L
<k_{20}\inf J_M
<k_{20}\sup J_M
<k_0\inf J_R.
}
\tag{23}
$$

L、M、R 是比值标签，不强求它们在物理 x 轴上的次序如此。由于 $k_0,k_{20}>0$，可以先选三个不同的正点满足严格夹持，再取小邻域。必须避开的中心重合只是有限个线性等式；严格条件组成的开集不会被它们覆盖。

共同正 I 须在最终 profile 定义以前已经包含这三个区间及各自的严格 collar。每个 $J_\bullet$ 中再预选两个不交的更小区间，分别放置普通与 companion 方向。总共六个最后区间，均在求任何实际主根之前固定。

L、R 两组采用 $\rho=0$，M 组采用 $\rho=20$。每组的两个方向沿 R270 原真实族，在各自最后中心，分别求解完整四式

$$
\delta^3L_c=0,\qquad
\delta(M_c+3L_c/\xi_0)=0,\qquad
\mathcal F_\kappa=0,\qquad
\mathcal E_{04}^{(1,-1)}=0.
\tag{24}
$$

全式包含八/十二副本和所有有限 $\delta$ 余项。各区间、中心、有限间距 $A$、$\kappa$、基础母函数与小母宽 $h$ 均已固定；$\alpha,\gamma,s,z$ 仍是每个 block 分别求解的四个未知量。不是先得一个根再移动或伸缩它。

只有有限六处。原 IFT 与支撑开性允许选择一个共同充分小的正主宽 $\delta$，使六个构造全部存在、各包/副本严格不交，并同时保留所有严格号和 (23) 的比值间隙。可以使用不同的实际
$\alpha,\gamma,s,z$；其共同零宽基点与连续性已足够，不假定六个有限宽解相同。

## 7. 每组只用正幅清 pure，并保比值夹持

记组 j 的两个实际完整 block 的三个观测为

$$
V_{j,-}=(Q_{j,-},S_{0,j,-},S_{1,j,-}),\qquad
V_{j,+}=(Q_{j,+},S_{0,j,+},S_{1,j,+}),
$$

其中 $Q_{j,-}<0<Q_{j,+}$。十二副本使这些 Q 为实；原 odd 条件仍保留。

取正四次权，例如

$$
w_{j,-}=Q_{j,+},\qquad w_{j,+}=-Q_{j,-}.
$$

用其正四次根作为实际共同 profile 幅度。由于两个完整 block 不交，且各自 inner 三矩为零，原全部跨 block 核准确消失。得到一个真正的二-block 组

$$
V_j=w_{j,-}V_{j,-}+w_{j,+}V_{j,+}
=(0,s_j,t_j).
\tag{25}
$$

每组两个 $S_0$ 具有相同严格号。因此

$$
s_L,s_R>0,\qquad s_M<0.
$$

比值 $r_j=t_j/s_j$ 是两个实际比值 $S_1/S_0$ 的正加权平均；即使分母都负，归一权仍为正。由 (22)—(23)，小正 $\delta$ 使

$$
\boxed{r_L<r_M<r_R.}
\tag{26}
$$

本步没有要求两个方向版本的 $S_0,S_1$ 数值相等，也没有把“各有正负号”当成自动能支付两个坐标。真正需要的二维几何信息正是 (26)。

## 8. 三个组的正幅准确同时支付两个外矩

现在只改变三个组的共同实幅度，所有最后位置保持。定义

$$
\boxed{
W_L=\frac{r_R-r_M}{s_L},\qquad
W_R=\frac{r_M-r_L}{s_R},\qquad
W_M=\frac{r_R-r_L}{-s_M}.
}
\tag{27}
$$

每个数严格正且有限。直接代入 (25) 得

$$
W_Ls_L+W_Rs_R+W_Ms_M=0,
$$

$$
W_Lt_L+W_Rt_R+W_Mt_M=0.
\tag{28}
$$

用 $W_j^{1/4}$ 作实际 profile 幅度，再将三个不交组相加，便准确有

$$
\boxed{\mathscr Q=0,\qquad S_0=0,\qquad S_1=0.}
\tag{29}
$$

两个幅度阶段均是真实正幅，不是把负元的线性 span 当路径或 profile。

R269 的完整原身份
$E_{22}^{(0)}-E_{04}^{(0)}=-\operatorname{Re}\mathscr Q$
与已付 odd 条件，使 $\mathscr Q=S_0=0$ 支付整个 $\mathcal A_0(\theta)$。式 (9) 与已付 odd 条件，使 $S_1=0$ 支付整个 $\mathcal A_1(\theta)$。因此

$$
\boxed{
I_0\{\phi_\theta,[B_1,B_{-3}](\phi_\theta;D_\theta)\}
=
I_1\{\phi_\theta,[B_1,B_{-3}](\phi_\theta;D_\theta)\}
=0
\quad\text{对全部 }\theta.
}
\tag{30}
$$

原 $I_2$ 未在这一步被置零。

所有旧零在六个最后 block 内已经分别成立。三矩圆在正幅相加后仍为三矩圆；R183/R245 的完整 block 局域范围保持原第三；六能量按其已付的真实边界与紧 inner 槽相加；R259 的 Gaussian 跨项对右方完整 inner 三矩线性，故全为零。这些事实支付了两次幅度混合的全部基准，不依赖“单微包没有尾”的错误假设。

尤其 R270 的整个 $A_{1,-1},I_0$ 和 R273 的整个 $A_{-1,-2},I_0$ 仍为零。各 block 可以有不同的两斜率参数；仅在每个 block 内使用其原相位恒等，然后相加完整零函数，不将同一 $\alpha\beta$ 强加给混合后的全圆。

## 9. 共同合法正区间的实际选择

上面的六位置不是对任意既定窄 I 的断言。这里将所需选择顺序完全固定。

[R105 §4、§8](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 区分了 universal 原式与真实物理域：原式无移动极点，不等于允许在 $x+\omega=0$ 附近使用曲面。其实际应用明确先固定有限路径、小参数族和参考几何，再选共同 I；随后才选 profile。  
[R114 §3](R114-constrained-static-costs-and-real-zero-matrix-words.md) 对有限状态、参数邻域和全部连接作同一安排，并指出重复次数不扩大 scalar 包络。  
[R223 §9.1](R223-Morse-closed-hooks-with-exact-pure-and-eight-flux-constraints.md) 进一步要求将原生成器、frame/scalar 桥和背景 hook 一起纳入紧包络，选择后保持 I、圆和右锚不动。

具体地，先固定本稿使用的真实共振端芽、有限 scalar 几何与全部所需桥/小族。对它们的一个紧包络，存在

$$
h_*>0,\qquad \omega_*>-\infty,\qquad
h\ge h_*,\quad\omega\ge\omega_*.
\tag{31}
$$

R56/R105 的物理 profile 分母是 $z=x+\omega$。任取正 $\eta$，只要

$$
x>-\omega_*+\eta
$$

便有统一 $z>\eta$。所以这一物理条件给出一条允许的右半轴；它本身不限制有限 I 的右端长度。这里不改变 scalar 路径，不越过其任何负分母零点。

在母宽和有限间距固定以后，$k_0,k_{20}$ 是两个已定义的正数。式 (23) 的严格位置条件对三个中心同时乘任意正数保持。故可在尚未定义最终 profile 时，一次把六个待选中心及其小区间选在

$$
x>\max\{0,-\omega_*+\eta\}.
$$

再取一个有限、有严格左右 collar 的共同 I 包含它们，并将真实右锚固定在右 collar。右方空区中的锚移动不改原函数的事实由 R105 §3–4 的真实右尾性质保证，不删除任何左尾。

至此固定所有最终位置，才执行第 6 节六个实际四变量 IFT。有限几何包络、I、右锚、母宽、有限 A 与这些最后中心均不再变动。取更小的正 $\delta$ 只缩小 profile 包络；第 7–8 节的正幅只改 profile 值，不改其支撑或 scalar 几何。因此 (31) 与原物理余量在整个实际构造中保持。

这不是将一个已求得的 profile 解作最终仿射变换。原算子含 x，任何求根后的平移一般会改其条件；本稿已经把所有位置依赖放在 (24) 的原方程里。若另给一个任意窄冻结 I，只有当它实际容纳所需六位置时本证明才适用，本文不作更强承诺。

同样，本文构造的是一个新的合法圆及其 seed 所定义的目标。若所选几何已有 universal 的 $M/T/$pure 身份，它们作为原函数身份保持；旧某一固定圆的 $F_8$ 或其他观测不因此迁移到新圆。基础几何设计或定义域的改变也不称为保持此前参考度量的等距变形。固定最终几何、最终圆和区间以后，本文所有方程才在这同一个实际目标上同时成立。

## 10. 完成结论与未支付部分

因此，在上述一次选定的共同合法正 I 内，存在六个有限、互不交的完整 block，以及全部严格正的真实幅度，使它们合成的非退化三矩圆同时保留：

- R270 的完整第三阶条件、原六个领先能量与共振端芽范围；
- 全部已付 odd Gaussian 系数；
- 整个 $A_{1,-1}$ 的第零外矩；
- R273 的整个 $A_{-1,-2}$ 第零外矩；
- 新的整个 $A_{1,-3}$ 第零与第一外矩，即 (30)。

每个最终 block 的内部参数先满足原完整方程，随后仅混合已经为零的真实齐次条件。共同正幅与不交支撑保持 $f,g$ 的三矩匹配，且至少一个非退化 block 使全圆非退化。如需要固定共同 $I_0$ 归一，可最后对 f、g 同乘一个正数；全部零条件齐次，故不改变上述结论。

原 R259 列表的“剩余 even 条件数”在 R273 后为18，本稿清掉其中对应整个第一外矩的两个形式条目，成为16。这里已经使用原恒等式使两个条目相同，数目仍仅是原列表的记账，**不是16个独立条件或真实 rank**。

本文没有支付 $A_{1,-3}$ 的第二外矩，也没有把其余 Gaussian 面积、完整偶 ruling membership、完整 period 或同一个合法 gauge 下的 joint 问题当成已解。新的建设性事实是：两个有序外矩可以在同一个最终物理区间，通过六个有限完整块的真实正幅同时准确支付；该结论不依赖旧有符号 span，也不依赖未做的求积或数值求解。
