# R346：剩余 Gaussian 接口与一个正权六目标锥支付新的完整第零外矩

日期：2026-11-15。**完整纸面建设性结论。** 未执行符号程序、profile 求积、参数扫描、人工测试或研究计算。

[R343](R343-two-real-orders-and-positive-center-clusters-pay-the-third-Gaussian-second-moment.md) 已在同一个真实弱单 hook 构造中支付三个负 Gaussian 方向之间的全部九个外矩。本稿先按 [R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R263](R263-ordered-Gaussian-area-81-scalar-recursion.md) 核清其余接口，再增加正方向与 $B_{-1}$ 之间的**全部相位第零外矩**。

新门不是给旧 72 条方程另加观察数。其真实 self 由 R270 的两条原式确定，跨微包核为零；一个实际母包扰动给两号，两种真实斜率给二维正锥。它与 R343 的第一、第二外矩四维正锥合成六维严格正锥，所以新增门不会重新打开已付的九矩。完整伸缩权使新模块的正 $\Psi$ 成本任意小，最后仍由原强控制器支付三条 directed 行和 $\Psi$。

主要来源：R259、R263、[R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R270](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、[R271](R271-six-complete-blocks-pay-the-first-two-positive-negative-Gaussian-moments.md)、[R341](R341-companion-directions-and-three-centers-pay-the-third-Gaussian-first-moment.md)、R343，以及 [R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)。

## 1. 原规范与尚未支付的三对算子

保持同一真实有限几何
$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0,
$$
和已经安装的共振端芽
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad
0<t:=\kappa^2<1/100.
$$
仍取同一右锚 $Jq(x)=\int_x^{r_*}q$。定义
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},\quad
L=\Phi_{p_0},\quad U=\Phi_{s_1},\quad Y=\Phi_{p_2},
$$
$$
W_*=aR+bS,\qquad Z_*=dL+eU,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d=\frac{6\kappa t}{h_e},\quad
e=-\frac{\kappa(15t+1)}{4h_e}.
\tag{1}
$$
四个原 Gaussian 剩余方向是
$$
B_1=\zeta Y,\quad B_{-1}=Z_*,\quad B_{-2}=W_*,\quad
B_{-3}=c_P P,
$$
$$
\zeta=-\kappa h_e\ne0,\qquad
c_P=-\frac{\kappa(41t^2+27)}{216h_e^3}\ne0.
\tag{2}
$$

令 $u=f\cos\theta+g\sin\theta$、$D=f\odot f-u\odot u$。沿用
$$
\mathcal M_j=I_j\{u,[W_*,P](u;D)\},\quad
\mathcal A_j=I_j\{u,[Z_*,P](u;D)\},
$$
$$
\mathcal B_j=I_j\{u,[Z_*,W_*](u;D)\}.
\tag{3}
$$
这里
$$
I_0(v,w)=\int v''w'',\quad I_1(v,w)=\int xv''w'',\quad
I_2(v,w)=\int(x^2v''w''+2v'w').
$$
R343 的结论是 $\mathcal M_j=\mathcal A_j=\mathcal B_j=0$，$j=0,1,2$，以及原 $\Psi=F_0=F_1=F_2=0$，全部相位成立。

剩余接口准确如下；表中括号顺序只与原 Gaussian 面积相差已经列出的非零常数。

| 原 Gaussian pair | 本文使用的原括号 | 待付外矩 | R259 的真实跨微包核 |
|---|---|---|---|
| $(1,-3)$ | $[P,Y]$ | $I_0,I_1,I_2$ | $\mathbf K_1$ |
| $(1,-2)$ | $[W_*,Y]$ | $I_0,I_1,I_2$ | $b\mathbf K_3$ |
| $(1,-1)$ | $[Z_*,Y]$ | $I_0,I_1,I_2$ | $0$ |

其中
$$
\mathbf K_1(\mathbf m,\mathbf n)
=\left(-m_1n_0,-\frac{m_0n_2+m_2n_0}{2},-m_1n_2\right),
$$
$$
\mathbf K_3(\mathbf m,\mathbf n)
=\left(\frac{m_0n_2}{2}-m_1n_1,
-\frac{m_2n_1}{2},-\frac{m_2n_2}{2}\right).
\tag{4}
$$
$\mathbf m$ 来自左 outer，$\mathbf n$ 来自右 inner；不能交换这个次序。

原十二完整副本已经清掉六个 pair 的全部 36 个 odd 角位置。当前弱 base 使用 R308 已付的整相位第三 range 与原八副本平移身份；$g\mapsto-g$ 只把 $\theta$ 换为 $-\theta$，不要求补加第二 hook。R259 第9节的十一阶差分因此仍作用于当前每个完整 base 的真实第四面积平移多项式。新增强块也使用同一八／十二完整包装。

故未逐项支付的表格位置是三对、三矩、两个 even 系数，共18个。这个数不是秩。例如 R271 原恒等已经给
$$
S_{P,Y,1}(q)=-\frac12 I_0(q,q)I_2(q,q).
\tag{5}
$$
对合法复 $q=f+ig$，其右边为零，所以 $[P,Y]$ 第1矩的两个 even 系数相等，只剩一个共同 $\sin^2\theta$ 值需要支付。不能因此删掉整个外矩。

本稿新增的目标是
$$
\boxed{\mathcal C_0(\theta):=
I_0\{u,[Z_*,Y](u;D)\}=0\quad\text{对全部 }\theta.}
\tag{6}
$$
原 $A_{1,-1}$ 的第零外矩等于 $-\zeta\mathcal C_0$，因而检验的是同一个门。

## 2. 有序完整接口对弱核心与强块分别怎样使用

R263 对任意两个严格不交的 partial blocks $A<B$，给
$$
T_{X,Y}(A\star B;\theta)
=T_{X,Y}(A;\theta)+T_{X,Y}(B;\theta)
+\Gamma_{X,Y}\{O_{M_A}(\theta),D_{M_B}(\theta)\}.
\tag{7}
$$
该式不要求 partial block 内部为 rank-one。当前弱核心的原面积必须保留为其完整真实积分；本文不会将弱 rank-two 区强行代入逐 rank-one 微包的 self 表。

每一个用于最后并置的 block 都已满足三矩圆，故右方 $D_{M_B}(\theta)=0$。于是全部面积在这些**完整 blocks**之间准确相加；原有序项仍存在于各 block 内部。这也保证下文的正幅矩阵是真实 profile 并置的矩阵。

需要强调为何不直接搬用普通／伴随的 primitive 两号。对合法 $q=f+ig$，R257、R275 的完整 self 给
$$
S_{P,Y,0}(q)=-\frac12\int[J(q''^2)]^2-\mathcal L_0(q),
$$
$$
S_{Z,W,1}(q)=\mathcal L_\kappa(q)
+\frac{k_*}{2}\int[J(q''^2)]^2,\qquad
k_*=\frac{db}{2}-ea\ne0,
\tag{8}
$$
其中
$$
\mathcal L_0(q)=\int\left(x^2q''^4-\frac83xq'q''^3
+\frac43q q''^3+q'^2q''^2\right)
$$
及 $\mathcal L_\kappa$ 均是已经确定的原 local 四次量。已付 $\mathcal B_1$ 的 even 差使
$$
\operatorname{Re}S_{P,Y,0}(q)
=\operatorname{Re}\{\mathcal L_\kappa(q)/k_*-\mathcal L_0(q)\}.
\tag{9}
$$
所以原 $\int[J(q''^2)]^2$ 的正负变化不能在保留 $\mathcal B_1=0$ 后被当成一个自由支付方向。本文没有由(9)宣称这个剩余 local 值为零；选用(6)是因为它有下面的准确新控制。

## 3. 新门的完整 self：Green 尾先消，不能假单包紧

对任意实紧 $v$，写 $p=v'$、$r=v''$，并记 $J_i$ 为原三矩 primitive。R270 的原输出为
$$
L(v,v)=vp-\frac{xp^2}{2}-\frac{x^2J_0}{4}+\frac{J_2}{4},
$$
$$
U(v,v)=xp^2+xJ_1+\frac{J_2}{2},\qquad
Y(v,v)=-xv^2+x^2vp-\frac{x^3p^2}{2}-\frac{x^2J_2}{4}.
$$
这些场一般都有真实左尾。

定义 $S_{X,Y,0}(v)=2I_0\{v,[X,Y](v;v^2)\}$。完整原式为
$$
\begin{aligned}
S_{L,Y,0}(v)=\int\big[
&v^2r^2-4xvpr^2+3x^2p^2r^2+x^2vr^3\\
&-\frac43x^3pr^3+\frac5{24}x^4r^4\big],
\end{aligned}
\tag{10}
$$
$$
\begin{aligned}
S_{U,Y,0}(v)=\int\big[
&-v^2r^2+8xvpr^2-9x^2p^2r^2-3x^2vr^3\\
&+\frac{16}3x^3pr^3-\frac{25}{24}x^4r^4-\frac23p^4\big].
\end{aligned}
\tag{11}
$$
R270 的推导保留 $Y$ 左尾 $-\mu_2x^2/4$、$U$ 左尾 $\mu_1x+\mu_2/2$。进入(11)的 Green 项是 $-\mu_1\mu_2/2$；原 primitive 余项
$$
\frac12\int\{J_1(x^2r^2+2p^2)+xr^2J_2\}
=\frac{\mu_1\mu_2}{2}
$$
与它准确相消。$(L,Y)$ 的两二次尾 Green 项本来为零。这是对任意 nonlegal 单包的原式，未先令 $\mu_i=0$。

另外，R259 原尾表直接给
$$
\Gamma_{L,Y,j}=\Gamma_{U,Y,j}=0\qquad(j=0,1,2).
\tag{12}
$$
所以新门在真实不交 rank-one 微包中只需(10)、(11)的 self 和。这里“跨核零”没有删掉 self 推导中的 Green 端项。

## 4. 同一真实母包给出的中心、宽度全式

取 even 母包 $v$，辅助坐标为 $y$，并定义
$$
C=\int r^4,\quad X_2=\int y^2r^4,\quad
N=\int yp r^3,\quad W=3\int p^2r^2+\int vr^3,\quad
\mathcal J(v)=W-2N.
$$
令 $\eta_{w,\xi}(x)=w^{3/2}v((x-\xi)/w)$。由(10)、(11)，
$$
dS_{L,Y,0}(\eta_{w,\xi})+eS_{U,Y,0}(\eta_{w,\xi})
=\frac{a_4C\xi^4}{w}+w\xi^2\mathcal B_\kappa(v)
+w^3\mathcal D_\kappa(v),
\tag{13}
$$
$$
a_4=\frac{5(d-5e)}{24},\qquad
\mathcal B_\kappa=6a_4X_2-4(d-4e)N+(d-3e)W,
$$
$$
\begin{aligned}
\mathcal D_\kappa={}&
(d-e)\int v^2r^2-4(d-2e)\int yvpr^2
+(d-3e)\int y^2(3p^2r^2+vr^3)\\
&-\frac43(d-4e)\int y^3pr^3
+a_4\int y^4r^4-\frac{2e}{3}\int p^4.
\end{aligned}
\tag{14}
$$
所有常数取同一个实际母包，不是独立参数。

沿用 R267
$$
\nu(v)=I_2(v,v)/I_0(v,v),\qquad
\mathcal F_\kappa(v)=\mathcal K_\kappa(v)/C-\nu(v),
$$
$$
\lambda\mathcal K_\kappa
=\lambda X_2+\frac43(d+11e)N-\frac{8e}{3}W,\qquad
\lambda=-5(d+7e)/6.
$$
原准确关系是
$$
\boxed{\mathcal B_\kappa-6a_4C\nu
=6a_4C\mathcal F_\kappa+\Gamma_\kappa\mathcal J,\qquad
\Gamma_\kappa=\frac{d^2-e^2}{d+7e}
=\frac{\kappa(1-9t)(39t+1)}{4h_e(81t+7)}\ne0.}
\tag{15}
$$

使用原两斜率、两宽度族
$$
\frac13<\alpha<\frac12,\qquad
\beta=\frac{5-\alpha}{1-\alpha},\qquad
q_0=\frac1{16(1-\alpha)^2},\qquad n=2^{11}.
$$
低组 $64n$ 个包宽 $\delta q_0$，平方幅 $(\alpha q_0,q_0)$；
高组 $n$ 个包宽 $\delta$，平方幅 $(\beta,1)$。取 R341 的实际居中排序、真实 TM 符号和准确方差
$$
V_L-V_H=\nu(v)(1-q_0^2).
\tag{16}
$$
母包固定后可选一个足够大的有限间距；所有位置、实际支撑和八／十二副本一起放进以下全式。

逐最细包的恒等
$$
a_i^2(a_i^2-5b_i^2)=\alpha\beta\,b_i^2(a_i^2-b_i^2)
$$
与(12)给 $2\mathcal C_0$ 的两个 even 系数
$$
E_{22}=\alpha\beta E_{04}.
\tag{17}
$$
这不是 leading 关系。

令 $\mathcal W>0$ 为完整副本的四次权和，$a_c=q_0(1-\alpha)$。
以 $\xi_0>0$ 为这个宏块的最后物理中心，所有真实 copy 加权中心均值为零。R270(17)准确给
$$
\begin{aligned}
\frac{E_{04}}{64na_c\mathcal W\delta}
={}&\xi_0^2(1-q_0^2)(\mathcal B_\kappa-6a_4C\nu)\\
&+\delta^2\big[
a_4C(\overline M_{4,H}-\overline M_{4,L})
+\mathcal B_\kappa(\overline V_H-q_0^2\overline V_L)
+\mathcal D_\kappa(1-q_0^4)\big].
\end{aligned}
\tag{18}
$$
两个二次中心矩和两个四次中心矩都是有限真实放置的值，随同一母包及真实间距变化；没有删掉最后一行。

## 5. 在旧完整面积纤维上取得两个真实符号

这里只用 R270 的实际母包扰动，不要求沿它早先的最终六能量分支，也不把 $\alpha$ 固定在旧能量根。

取非零偶实紧 $v_*$，令
$$
N_0(v_*)=\int v_*'(v_*'')^3,\qquad
e_*=\operatorname{EL}(N_0)(v_*),
\quad K_*=\int e_*^2>0.
$$
原式为
$$
e_*=12r^2r'+6v_*'(r')^2+6v_*'r r'',\qquad r=v_*''.
$$
$e_*$ 为奇。严格 $K_*>0$ 的原证明是：若 $e_*=0$，则
$(v_*'rr'+r^3/3)'=0$；平端使括号零，进而
$(v_*'r^3)'=0$，再由平端得 $v_*'r^3=0$。
在 $r\ne0$ 的任何开区间会迫 $v_*'=0$，矛盾。
因此
$$
N_0(v_*+\eta e_*)=K_*\eta+O(\eta^3).
$$

固定 $L_*=1/2$，按 R270 定义真 even 三母包
$$
\begin{aligned}
v_{\gamma,s,h,z}(y)={}&
\gamma(sh)^{3/2}v_*(y/(sh))\\
&+h^{3/2}(v_*+hz e_*)((y-L_*)/h)\\
&+h^{3/2}(v_*+hz e_*)(-(y+L_*)/h).
\end{aligned}
\tag{19}
$$
宽度 $h>0$ 小且有限，三个支撑严格不交。右、左子包为镜像，整体 even。

R270 已给实际正 $h$ 的根
$(\gamma_h,s_h,z_h)$，满足 $\mathcal F_\kappa=0$、$\mathcal J=0$，并给完整母 Jacobian。现固定 $s=s_h$。在零宽归一式上，
$$
\partial_\gamma\mathcal F_\kappa=-4L_*^2/9,\quad
\partial_z\mathcal F_\kappa=0,\quad
\partial_z(\mathcal J/h)=-4L_*K_*.
$$
因而对 $(\gamma,z)$ 的两行 minor 趋于
$16L_*^3K_*/9\ne0$；固定足够小的实际正 $h$ 后仍非零。
真实有限维 IFT 给一条实际小族
$$
\boxed{\mathcal F_\kappa(v_\tau)=0,\qquad
\mathcal J(v_\tau)/h=\tau,\quad |\tau|<\tau_* .}
\tag{20}
$$
母 $\mathcal H$ 不必沿该新小族保持为零，后面的 $\Psi$ 和 directed 行另按全式支付。没有将零宽 profile 作为合法输入。

在一个固定非零小 $\tau_0$ 上取 $v_{\tau_0}$、$v_{-\tau_0}$。
选共同有限间距，使(16)的真实排序对这两个母包及小邻域都严格合法；再固定四个互不交的正中心区间。由(15)、(18)，当 $\delta\downarrow0$，
$$
\frac{E_{04}}{64na_c\mathcal W\delta}
\longrightarrow
\xi_0^2(1-q_0^2)\Gamma_\kappa h\,\tau.
\tag{21}
$$
右边对 $\tau=\pm\tau_0$ 严格异号。最后一行的有限真实系数在这些固定参数上有界，所以一个有限正 $\delta$ 就给真实异号；不需要执行求积，也没有把 $\delta=0$ 当实际构造。

取两个不同的 $\alpha_1,\alpha_2\in(1/3,1/2)$，在各自最后正区间重复上述两号选择。(17)给四个原型的真实 $\mathcal C_0$ 向量沿
$$
\pm(\alpha_1\beta_1,1),\qquad
\pm(\alpha_2\beta_2,1).
\tag{22}
$$
每条射线上有严格非零实际值。函数
$\alpha\beta=\alpha(5-\alpha)/(1-\alpha)$ 严格递增，
故四列张成 $\mathbb R^2$，并有一个全分量严格正的零关系。
因此它们的正锥准确为整个 $\mathbb R^2$。

## 6. 新原型保留哪些旧条件

每个新原型都已经是真实三矩圆，并具有原八／十二完整包装。
由(20)及 R267 的原全三 self，
$$
\mathcal M_j=\mathcal A_j=0\qquad(j=0,1,2).
\tag{23}
$$
原两斜率 quartic 张量仍是
$A_4=5C_{22}$、$E_4=C_{22}$、$B_4=D_4^{\rm tens}=0$，
因此
$$
C_\theta=J_\theta=0,\qquad
D_{4,\theta}=4C_{22}\sin^2\theta,\qquad
\Psi=\psi\sin^2\theta,\quad \psi>0.
\tag{24}
$$

居中 ordinary 排列的 $f$ 奇、$g$ 偶；整体母包在(19)中仍为偶。
R341 第7节的真实反射、原二次尾正交与十二 odd 消去于是给
$$
\boxed{\mathcal B_0=0,\qquad \mathcal R_0=\mathcal R_1=0,\qquad
\mathcal R_j:=I_j\{u,[R,S](u;D)\}.}
\tag{25}
$$
(23)、(25)保证这些零在最后实际平移与正伸缩下保持。没有假设新原型的 $\mathcal B_1,\mathcal B_2$ 为零；下一节正是同时支付它们。

同一完整新原型的 $\mathcal C_0,\mathcal B_1,\mathcal B_2$ 均记录为真实两个 even 系数。所有内部尾、自项、最后中心和副本方差都已经包含在这些值中。它们由真实有限 profiles 定义，不能独立指定。

## 7. 三种完整伸缩权，而非 principal 权

对整个实际 block 取正伸缩
$$
(f_H,g_H)(x)=(f,g)(x/H),\qquad H>0.
$$
同一最终右锚位于全部伸缩后支撑右侧，原 $J$ 的真实零 collar 给完整齐次式，不添锚常数。

原八算子中
$$
P:-3,\quad R,S:-2,\quad L,U:-1,\quad Y:+1.
$$
结合 $I_0,I_1,I_2$ 的完整外权，准确得到
$$
\boxed{
\mathcal B_1(f_H,g_H)=H^{-5}\mathcal B_1(f,g),\quad
\mathcal B_2(f_H,g_H)=H^{-4}\mathcal B_2(f,g),\quad
\mathcal C_0(f_H,g_H)=H^{-3}\mathcal C_0(f,g).
}
\tag{26}
$$
特别，$I_2$ 的两个原项同为这个权；没有只检查 $x^2u''w''$。
同时
$$
\Psi(f_H,g_H)=H^{-7}\Psi(f,g).
\tag{27}
$$

将§5四个原型作共同有限大伸缩 $H$，再令其第四幅度乘 $H^3$，它们的 $\mathcal C_0$ 列保持不变，而
$$
\mathcal B_1=O(H^{-2}),\qquad
\mathcal B_2=O(H^{-1}).
\tag{28}
$$
原型中心从起点为正，因此这些真实包络最终可以位于下面固定八个旧原型右方，且彼此保持严格分离。此处没有搬动 R341 已固定的弱块。

## 8. 六个完整目标的严格正核

R343 已给八个实际强原型，其
$$
\mathsf B:\mathbb R^8\longrightarrow\mathbb R^4,\qquad
\lambda\longmapsto(\mathcal B_1,\mathcal B_2)
$$
满秩且有严格正核。它们全有(23)、(25)，并各带有限正 $\Psi$。
按真实最后位置取它们的 $\mathcal C_0$ 列，记作 $\mathsf C_B\in\mathbb R^{2\times8}$。
这里的列均在其真实最后位置取值。

令 $C\in\mathbb R^{2\times4}$ 为§5四个原型的 $\mathcal C_0$ 列。
它满秩且有严格正核。上述十二原型的六目标矩阵，在(28)的归一后满足
$$
M_H=
\begin{pmatrix}
\mathsf B&O(H^{-1})\\
\mathsf C_B&C
\end{pmatrix}
\longrightarrow
M_\infty=
\begin{pmatrix}
\mathsf B&0\\
\mathsf C_B&C
\end{pmatrix}.
\tag{29}
$$
四维上块中的前两行实际为 $O(H^{-2})$。这只是固定有限列的准确极限，不把原积分系数设为零。

$M_\infty$ 的行秩为6。选 $b_0>0$、$\mathsf B b_0=0$。
由于 $C$ 的正锥为 $\mathbb R^2$，可解
$Cc_0=-\mathsf C_Bb_0$，并加上其严格正零关系使 $c_0>0$。
因此
$$
M_\infty(b_0,c_0)=0,\qquad (b_0,c_0)>0.
\tag{30}
$$
固定一个非零六列子式。对足够大的有限 $H$，这个子式仍非零；保持其他六个坐标不变，仅用这六列解掉
$M_H(b_0,c_0)=o(1)$。所得核向量趋于$(b_0,c_0)$，故仍严格正。

于是可固定一个有限实际 $H$，使
$$
\boxed{\operatorname{rank}M_H=6,\qquad
\ker M_H\text{ 含严格正向量，故 }\operatorname{cone}_+(M_H)=\mathbb R^6.}
\tag{31}
$$
最后的蕴含有直接证明：对任意目标先取一个实右逆解，再加足够大的严格正核向量，使全部实际第四幅度为正。负输出来自真实原型值，不来自负路径或负第四幅度。

这完整付清新增门与 $\mathcal B_1,\mathcal B_2$ 的相互作用。未使用它们“应当独立”的泛性假设。

## 9. 保留原弱块、全部旧矩，并控制真实 Ψ 成本

从 R343 构造的最后强控制器之前接入。此时原弱核心、其宽 cutoff 与三矩补偿、旧面积模块及其最终中心全部固定；准确有
$$
\mathcal M_j=\mathcal A_j=\mathcal B_j=0\quad(j=0,1,2),
\qquad
\Psi=-\Delta_0\sin^2\theta,\quad \Delta_0>0.
\tag{32}
$$
三条 directed 行取其完整有限基线；待付 $\mathcal C_0$ 的真实 even 向量记为 $c_{\rm old}$。这是同一构造在最后控制步骤前的实际状态，不是任意给定已冻结圆都具有负余量的宣称。

固定(31)的十二原型及其正核 $k>0$、实右逆 $R_M$。
再对这整组原型作共同正伸缩 $S$，第四幅度写成 $S^5c_i(S)$。
原六目标缩放因子依次为 $1,S,S^2$。可取
$$
c(S)=k+R_M(0,0,-c_{\rm old}/S^2).
\tag{33}
$$
两个零块分别是 $\mathcal B_1,\mathcal B_2$ 的二维目标。
对足够大的有限 $S$，$c(S)>0$ 且有界；由(26)，新增量准确为
$$
\Delta\mathcal B_1=0,\qquad
\Delta\mathcal B_2=0,\qquad
\Delta\mathcal C_0=-c_{\rm old}.
\tag{34}
$$
全部 $\mathcal B_0,\mathcal M_j,\mathcal A_j$ 因每列自身为零继续保持。

若十二个固定原型的正 $\Psi$ 系数为 $\psi_i$，其真实新增成本是
$$
\Delta\Psi=S^{-2}\left(\sum_i c_i(S)\psi_i\right)\sin^2\theta.
\tag{35}
$$
选一个有限 $S$ 使其小于 $\Delta_0/2$。同一更大有限 $S$ 可使所有新正支撑位于旧固定 profiles 右方；原组内部的严格不交由共同伸缩保持。所有式子均使用这个最终实际放置，不再整体移动旧圆。

现在原全部九矩和新增(6)准确为零，$\Psi$ 仍有严格负余量。按 R343 最后的同一个原控制器入口，在预选的强 rank-one 区内使用 R293/R277 的有限 $F^\star$ 纤维与有限频率正核，支付完整三条 $F_0,F_1,F_2$ 并将 $\Psi$ 准确归零。

这里初选 $F^\star$ 已包含原全部 Gaussian self 平移系数、真实三矩及所需 quartic $C$；控制器自身的全部72面积为零。其有限 $N$ 纠正保持这些实际原值，故既不改变(34)，也不重开旧九矩。只在控制器内部使用高频，弱核心的单 hook、真实 tails、原入历史全部固定。本文没有把旧三个 pair 的控制能力冒称为控制器外全部面积为零。

## 10. 选择顺序与最终范围

选择次序是：

1. 固定同一几何与共振参数，取 R343 最后控制器前的实际基线和全部已固定弱块中心；
2. 选实际小正母宽 $h$，由真两行 minor 得(20)，选两不同 $\alpha$ 与两种 $\tau$ 符号；
3. 固定四个正区间、真实有限间距及八／十二副本后，取有限正 $\delta$，保(18)全式取得(22)；
4. 固定 R343 八列和新四列的全部原函数值，再取有限 $H$ 得(31)；
5. 取有限 $S$ 和(33)的严格正第四幅度，同时完成(34)、支撑分离及(35)的小成本；
6. 固定最后强控制器及共同合法正区间，在原有限纤维中取一个有限 $N$ 精确支付剩下的三条 directed 行与 $\Psi$。

共同物理区间按 R105/R114/R271 已付的范围，从这全部有限 profiles 与几何包络选择足够右、足够宽的新正区间。没有扩大任意已冻结窄区间的承诺。所有系数在实际小邻域连续，所有选定宽度、间隙、幅度严格正有限；不存在用零宽或无限频率对象代替真实答案。

最终同一个真实弱单 hook 圆满足
$$
\boxed{
\mathcal M_j=\mathcal A_j=\mathcal B_j=0\quad(j=0,1,2),\qquad
\mathcal C_0=0,\qquad
\Psi=F_0=F_1=F_2=0.
}
\tag{36}
$$
三矩、完整第二／第三 range、全部36个 odd Gaussian 位置与原指定一层条件均保留。

在 R259 的表格中，尚未逐项支付的是：
$[P,Y]$ 的三个外矩、$[W_*,Y]$ 的三个外矩，以及 $[Z_*,Y]$ 的第1、第2外矩。
它们对应16个形式 even 位置；至少(5)给其中一条准确重复，不能据位置数宣独立秩。本文没有宣称其余面积、整个零／一层函数、完整第四 period 或同一个 gauge 的 joint ruling 已解。

本稿使用新选择的最终圆与 seed；原弱部分保其已固定真实位置，新增与纠正仅在新强完整 blocks 中进行。不把这个建设性存在结论说成任意固定圆上的免费变形。
