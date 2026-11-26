# R997 — 实际 CM 图的最高 Coleman–AJ 值与具体 Picard–Fuchs 方程

2026-11-26 / Astra-rank2-Sha-0b097461-20261127。

**已证明。** R991/R995 的实际 $I_9/I_3$ 曲面及其完整34同源图有一个
不经 K3 比较的局部 AJ 求值式。最高槽是实际模形式的
$\theta^{-2}$，其中 cusp 宽度3产生一个不能省掉的9因子。
它也等于下面明确的非齐次 Picard–Fuchs 解在原 CM 点的带权值：
$$
t(1-27t)b''+(1-54t)b'-6b=-\frac3{v^2},
\qquad v^3=t(1-27t).
\tag{1}
$$
这里的解是 Frobenius 规范的 Coleman 解，不是任意选初值的解。
对一条次数 $d_\varphi$ 的同源，若
$\varphi^*\omega_b=c_\varphi\omega_E$，其最高求值恰为
$-d_\varphi b(b)/c_\varphi$。本篇同时支付全 finite trace、两个
系数嵌入及单 CM projector 的对偶方向。

这是一条针对新实际循环的局部互反公式；尚未证明该有限带权值非零，
也不将其直接命名为尚未比较的新全球 Rankin $p$-adic $L$-值。
R994 的三个复中央值及 R998 的混合 Selmer 消失不替代这个非零输入。

## 1. 固定数据、素位与不变的循环来源

保持
$$
K=\mathbf Q(\omega),\quad \delta=1+2\omega,\quad
E=E_{27}:y_0^2+y_0=x_0^3,\quad
\omega_E=\frac{dx_0}{2y_0+1},
$$
以及 R991 的真正模曲面
$$
\pi:S\longrightarrow B,\qquad
B:v^3=t(1-27t),\qquad
S_t:y^2+xy+ty=x^3.
\tag{2}
$$
$S$ 指光滑射影相对极小模型。其零截面记为 $O_B$。
原 $\Gamma\supset\Gamma(9)$、3处 simple-supercuspidal 型、
2处三个子群及17处十八个子群的完整带权组合均保持 R991 的规范。

取一个固定有限 Galois 扩张 $L/K$，包含原 $H$、所有上述级结构、
商同源和所需模型同构。令 $p>3$ 在 $K$ 分裂，素于34，并排除
$L$、固定对应和所用整模型的有限坏集。固定一个 $p$-adic 嵌入；
所有被使用的 CM 椭圆纤维均普通，因为其 CM order 的 conductor
素于 $p$。论证可先在 $L$ 的相应有限局部扩张内进行，再用
restriction/corestriction。

取一个光滑非 cusp CM 点 $b=(t_b,v_b)$ 及指定同源
$$
\varphi:E_L\longrightarrow S_b,
\qquad d_\varphi=\deg\varphi.
\tag{3}
$$
R991 初始54条图的 $d_\varphi$ 都是34。
以下也允许为 $p$-depletion 明确增加的 $\mathfrak p$、
$\mathfrak p^2$ 同源，届时次数分别是 $34p$、$34p^2$。
这些是不同的实际图；不会用删掉一部分图来替代原有限 trace。

## 2. 先把原图本身变成同调零，避免任意 projector 交换假设

在 $X=S\times E$ 中写
$$
\Gamma_\varphi=\{(\varphi(Q),Q):Q\in E\}.
$$
取 $e=\pi_1(E)=\Delta_E-E\times O_E-O_E\times E$，则严格有
$$
\Delta_\varphi
=(1_S\otimes e)_*[\Gamma_\varphi]
=[\Gamma_\varphi]-d_\varphi[S_b\times O_E]
-[O_b\times E].
\tag{4}
$$
系数 $d_\varphi$ 来自图到第一个椭圆因子的次数；另一个系数为1。

**引理。** (4)在 $X$ 上同调零。

**证明。** R991 已证明 $q(S)=g(B)=1$。由截面，
$\pi^*:H^1(B)\to H^1(S)$ 单射，维数相同，故为同构。
限制到任意纤维 $\iota_b:S_b\hookrightarrow S$ 因而为零：
$$
\iota_b^*=0:\ H^1(S)\longrightarrow H^1(S_b).
\tag{5}
$$
这里的零说的是 restriction 映射，不是 $H^1(S_b)$ 本身为零。
由 Poincaré 对偶，Gysin
$\iota_{b,*}:H^1(S_b)\to H^3(S)(1)$ 也是零映射。
(4)在 $S_b\times E$ 的 Künneth 类只剩
$H^1(S_b)\otimes H^1(E)$；推到 $X$ 后正由该 Gysin 映射给出，
所以为零。证明对 Betti 及每个 étale 实现均成立。$\square$

因此可以先对明确的 $\Delta_\varphi$ 使用 AJ。令
$P=\pi_2^{\rm tr}(S)$ 为 R995 的自对偶 refined projector，则
$$
Z_\varphi=(P\otimes e)_*[\Gamma_\varphi]
=(P\otimes e)_*\Delta_\varphi.
\tag{6}
$$
在全局二形式
$$
\Omega=\frac{dt}{v^2}\wedge\omega_t,
\qquad \omega_t=\frac{dx}{2y+x+t}
\tag{7}
$$
上有 $P\Omega=\Omega$。R995 的 $P_{\rm high}$ 自伴，且在
$\Omega\otimes\omega_E$ 上为恒等。因此
$$
\operatorname{AJ}_p(P_{\rm high}Z_\varphi)
 (\Omega\otimes\omega_E)
=\operatorname{AJ}_p(\Delta_\varphi)
 (\Omega\otimes\omega_E).
\tag{8}
$$
(8)只把对应移到一个**已经同调零**的循环的对偶微分上。
它没有把 AJ 未定义的原裸图当作同调零，也没有假定任意 KMP
projector 与全层 Scholl projector 在 Chow 层交换。

## 3. 原曲面的 Gauss–Manin 矩阵及完整推导

在 $t\ne0,1/27,\infty$ 的仿射片上，置
$$
u=x+\frac1{12},\qquad w=2y+x+t.
$$
则
$$
w^2=4u^3-g_2u-g_3,
\quad g_2=\frac{1-24t}{12},\quad
 g_3=\frac{-1+36t-216t^2}{216},
\quad \Delta=g_2^3-27g_3^2=t^3(1-27t).
\tag{9}
$$
这里 $u$ 是短 Weierstrass 坐标，不是 R991 的 Hauptmodul $u$。
以下令
$$
\omega=\frac{du}{w}=\omega_t,\qquad
\eta_0=\frac{u\,du}{w},\qquad D=t(1-27t)=v^3.
\tag{10}
$$
采用代数 de Rham trace/Tate 规范，
$$
\langle\omega,\eta_0\rangle=1,
\qquad \langle\eta_0,\omega\rangle=-1.
\tag{11}
$$
例如在无穷点取 $z$ 使 $u=z^{-2}+\cdots$、$\omega=dz+\cdots$，
则 $\eta_0=z^{-2}dz+\cdots$，局部原函数与留数公式给(11)。
等价的复比较是 $\int\omega\cup\eta_0=2\pi i$；
这里已除去该 Tate 周期，而不是另引一个未定非零常数。
这也与 [Hain, §19.3, Proposition19.7] 的同一 Weierstrass 规范一致。

直接对(9)微分并模 exact forms，得到
$$
\begin{aligned}
\nabla\omega&=(A\omega+B\eta_0)\,dt,\\
\nabla\eta_0&=(C\omega-A\eta_0)\,dt,
\end{aligned}
\qquad
A=\frac{36t-1}{4D},\quad
B=\frac3D,\quad
C=-\frac{1-24t}{48D}.
\tag{12}
$$
为支付其符号与每个系数，可先在一般 $g_2,g_3$ 下使用
$$
d\left(\frac{u^k}{w}\right)
=\left(k u^{k-1}(4u^3-g_2u-g_3)
-\tfrac12u^k(12u^2-g_2)\right)\frac{du}{w^3},
\quad k=0,1,2.
\tag{13}
$$
把 $\partial_t\omega=(g_2'u+g_3')du/(2w^3)$ 和
$\partial_t\eta_0=(g_2'u^2+g_3'u)du/(2w^3)$ 用(13)约去，给
$$
A=-\frac{\Delta'}{12\Delta},\qquad
B=\frac{3g_2g_3'-\frac92g_3g_2'}{\Delta},\qquad
C=-\frac{g_2B}{12}.
\tag{14}
$$
代入(9)，分子 $3g_2g_3'-\frac92g_3g_2'=3t^2$，即为(12)。
矩阵 trace 为零，亦符合(11)的水平性。
这是原曲面的连接；不是仅凭相同 CM 特征多项式挑选的另一连接。

## 4. Coleman 原函数与非齐次标量方程

令 $\mathcal H=R^1\pi_*\Omega^\bullet_{S/B}$。
按(7)的 Leray/微分次序，$\Omega$ 对应于
$$
\boldsymbol\Omega=\frac{\omega}{v^2}\,dt
\in H^0(B^\circ,\mathcal H\otimes\Omega^1_B).
\tag{15}
$$
采用 [BDP, §3.6] 的 Frobenius 规范，记其 Coleman 原函数为
$$
\mathcal F_p=a_p\omega+b_p\eta_0,
\qquad \nabla\mathcal F_p=\boldsymbol\Omega.
\tag{16}
$$
下标 $p$ 表示这一个系数素数的 Coleman 解，
不是新形式的第 $p$ 个 Fourier 系数。

这里并未给(16)任意局部初值。必须使用 BDP Lemma3.14 的
**全部**多项式条件：$Q(\Phi)[\boldsymbol\Omega]=0$；
$Q(\Phi)$ 在 $H^0_{\rm la}(B,\mathcal H)^\nabla$ 的局部解析
水平截面空间上为同构；并且 $Q(1)\ne0$。
仅有 $Q(1)\ne0$ 不能排除局部水平解。
这类 $Q$ 的存在来自该引理的 Frobenius 权重分离：当前 $r=1$，
parabolic $H^1$ 的权重为2，水平截面的权重为1；取 Frobenius 的
同一次幂后，两边的复绝对值仍不同。

然后要求 $Q(\Phi)\mathcal F_p$ 在适当宽开集上 rigid analytic。
BDP Theorem3.15 及 Remark3.16 先给存在、相容延拓及选择独立性，
并把剩余歧义降为**全局 rigid analytic** 水平截面。
仅到这一步才使用原 congruence monodromy：它包含两个不同固定线
的幺幂矩阵，故标准二维表示无不变量，剩余全局 rigid 水平空间为零。
这给唯一的上述 Coleman 原函数；不是单凭 monodromy 就宣布所有
局部解析水平截面为零。Remark3.17 再保证其在所需 residue disc 上解析。

由(12)，(16)等价于
$$
a_p'+Aa_p+Cb_p=v^{-2},\qquad
b_p'+Ba_p-Ab_p=0.
\tag{17}
$$
消去 $a_p=(Ab_p-b_p')/B$。用
$$
\frac{B'}B=-\frac{D'}D,\qquad
A'-A\frac{B'}B+A^2+BC=\frac6D,
$$
严格得到
$$
\boxed{D b_p''+D'b_p'-6b_p=-3v^{-2},
\qquad D'=1-54t.}
\tag{18}
$$
其齐次方程在 $z=27t$ 下为参数 $(1/3,2/3;1)$ 的 Gauss 方程。
但求 AJ 用的是(18)及(16)的 Frobenius 规范，不能只取任意一个
齐次超几何函数或把任意两条局部积分常数设为零。

## 5. 实际图的局部 AJ 残数公式

对(3)指定代数非零倍率
$$
\varphi^*\omega_{t_b}=c_\varphi\omega_E.
\tag{19}
$$
该倍率来自**实际**商同源与模型同构。它不因同源次数为34就自动等于1。

**定理。** 在以上每个好普通系数素数，有
$$
\begin{aligned}
\operatorname{AJ}_p(\Delta_\varphi)(\Omega\otimes\omega_E)
&=\langle\varphi^*\mathcal F_p(b),\omega_E\rangle_E\\
&=\frac{d_\varphi}{c_\varphi}
  \langle\mathcal F_p(b),\omega_{t_b}\rangle_{S_b}\\
&=\boxed{-\frac{d_\varphi}{c_\varphi}\,b_p(b)}.
\end{aligned}
\tag{20}
$$
它也等于(8)的最高双线求值。

**证明与局部定理的适用范围。** 可以在 full9 模曲线先拉回(2)。
$\Gamma/\Gamma(9)$ 的阶为27，$p\ne3$ 时其 cover 及有理 trace
保留 Gauss–Manin、Coleman 原函数、图和 AJ；在光滑模问题上是
有限 étale 下降，在 cusps 上只产生素于 $p$ 的 tame ramification。
也可以直接在原 $B$ 的半稳定通用族上作下面的证明。

BDP Proposition3.18 的论证只使用：纤维上的实际同调类、
$\mathcal H\otimes H^1(E)$ 的连接和 Frobenius、局部残数及
Coleman 原函数。第2节已给全局同调零所需条件。
在删去 $b$ 的基曲线上，AJ 扩张可写为 Hodge lift 与 Frobenius lift
之差。Hodge lift 在 $b$ 的残数为图的 $H^1\otimes H^1$ 类；
其它非 cusp 小圆环残数为零。在 cusps 上，(7)为 cusp form，
相应原函数乘 lift 的留数为零。

用同一个全局 Coleman 原函数代替各圆盘的任意原函数后，
Hodge lift 的残数和为
$\langle\mathcal F_p(b)\otimes\omega_E,\mathrm{cl}_b(\Delta_\varphi)\rangle$。
Frobenius lift 的残数和在 $\Phi$ 下不变；再施加(16)的
$Q(\Phi)$，rigid 留数定理给其乘 $Q(1)$ 为零，故该和为零。
这正是 BDP Lemmas3.19–3.20 的推导。

图的两个 degree 修正不与 $H^1\otimes H^1$ 配对。
图的投影公式因而把剩下的配对变成
$\langle\varphi^*\mathcal F_p(b),\omega_E\rangle$，
即其 Proposition3.21。由(19)及
$\langle\varphi^*r,\varphi^*s\rangle=d_\varphi\langle r,s\rangle$，
再用(11)、(16)，得到(20)。$\square$

本证明没有使用 BDP Theorem5.13 的全球 cyclic-ideal Heegner 假设。
事实上 $K$ 中 norm27 的理想是 $(\delta^3)$，其商的加法群为
$\mathbf Z/9\oplus\mathbf Z/3$，不是 $\mathbf Z/27$。
所以不能把该全球定理直接套到 $f_{27}$，然后省掉原3处型的比较。
局部残数证明不要求这个全球假设，所需的全部几何数据已在上面逐项给出。

## 6. 真实宽度3的模形式和负二阶算子

令 $f_{27}(q)=\sum_{n\ge1}A_nq^n$ 为
$\theta(\psi_{27}^2)$ 的首项1 newform。其完全确定的 theta 公式为
$$
f_{27}(q)=
\sum_{\substack{a,b\in\mathbf Z\\a\equiv1\ (3),\ b\equiv0\ (3)}}
(a+b\omega)^2 q^{a^2-ab+b^2}.
\tag{21}
$$
每个素于3的理想恰有一个模3等于1的生成元，因此无额外的6因子。
特别 $A_n=0$ 除非 $n\equiv1\pmod3$。

原 $\Gamma$ 的首项1 cusp form 是
$$
h_\Gamma(\tau)=f_{27}(\tau/3)
=\sum_{n\ge1}A_nq^{n/3}.
\tag{22}
$$
这也可不靠有限截断验证。$h_\Gamma|T=\omega h_\Gamma$。
$f_{27}$ 系数有理，Fricke27 把它送到一个非零倍数的自身，
故 $h_\Gamma$ 也是 $W_3$ 的特征向量。
由 $W_3^{-1}TW_3=\left(\begin{smallmatrix}1&0\\-3&1\end{smallmatrix}\right)$，
其在 $\Gamma_1(3)$ 的字符正是
$g\mapsto\omega^{b-c/3}$，核为 R991 的原 $\Gamma$。
变换自 cusp form 保证其在所有 cusp 消失；而
$\dim S_3(\Gamma)=1$，故(22)给指定的形式。

还须把(22)与原代数二形式(7)的尺度固定。沿 R991 的 cusp
$$
t=\frac1{27}-q+O(q^2),\qquad v=q^{1/3}+O(q^{4/3}).
$$
在 split Tate 参数中，$\omega_t=r(q)\omega_{\rm can}$，其中
$$
r(q)^4=\frac{E_4(q)}{1-24t(q)},\qquad r(0)=\delta.
\tag{23}
$$
$r^6$ 的符号由同一 $c_6$ 等式固定：在该 cusp
$c_4=1/9,c_6=1/27$，故 $r(0)^6=-27$。
这是 R991 已保留的非裂 cusp 的 $K$-split 规范。
(7)的模形式因而是
$$
f_\Omega(q)=r(q)\frac{\theta t}{v^2}
=\boxed{-\delta\,h_\Gamma(q)},
\qquad\theta=q\frac d{dq}.
\tag{24}
$$
两边在同一一维 cusp 空间，首项都是 $-\delta q^{1/3}$，故为严格等式。
选择相反 Tate 微分时两侧一起变号，不单独抹掉该尺度。

对任一普通三元组 $(A,\text{完整级结构},\omega_A)$，置
$$
G_{1,p}(A,\ldots,\omega_A)
=\langle\mathcal F_p(A),\omega_A\rangle.
\tag{25}
$$
其 weight 为 $-1$：把微分乘 $c$，其值乘 $c$。
令 $[p]$ 上标表示删去 Fourier 指数中被 $p$ 整除的项，
即按 BDP **右作用顺序**写的 $VU-UV$ 算子；改写成函数的
左作用顺序就是 $1-VU$，其中 $UV=1$。原 Tate Gauss–Manin 恒等式给
$\theta G_{0,p}^{[p]}=f_\Omega^{[p]}$、
$\theta G_{1,p}^{[p]}=G_{0,p}^{[p]}$；在普通 Igusa 塔上用
$q$-expansion principle，得到其 Proposition3.24 的当前特例
$$
\boxed{G_{1,p}^{[p]}=\theta^{-2}f_\Omega^{[p]}.}
\tag{26}
$$
在原宽度3的 cusp，完整展开是
$$
\boxed{
G_{1,p}^{[p]}(q)
=-9\delta\sum_{\substack{n\ge1\\(n,p)=1}}
\frac{A_n}{n^2}q^{n/3}.}
\tag{27}
$$
这是 $\theta(q^{n/3})=(n/3)q^{n/3}$ 导致的9；
不能把(27)当成 $f_{27}(q)$ 的负二阶展开。
$\theta^{-1}$ 对应与外部 unit-root 微分配对的另一个槽，
并非本篇的最高槽。

(27)定义的是可在普通 locus 上评价的 $p$-adic 模形式，
不是说每个良约化 CM 点都处于 cusp 的 $|q|_p<1$ 圆盘。
在其它 CM residue disc 上必须使用 Coleman/Frobenius 延拓，
或同一 $p$-adic 模形式的代数评价；直接把一个不收敛的 cusp
级数代入该点不构成计算。

## 7. $p$-depletion 的三个实际同源和次数

固定 CM 点上 canonical subgroup 对应的素理想 $\mathfrak p\mid p$。
理想作用始终指带微分的作用
$$
\mathfrak a*(A,\ell,\omega_A)
=(A/A[\mathfrak a],\varphi_{\mathfrak a}(\ell),\omega_{\mathfrak a}),
\qquad \varphi_{\mathfrak a}^*\omega_{\mathfrak a}=\omega_A.
\tag{28}
$$
全部9级由该同源运输。$p$ 分裂时原中心/diamond 特征在 $p$ 为1。
$G_{1,p}$ 的 Hecke 特征值是 $A_p/p^2$，weight 为 $-1$。
BDP Lemma3.23 的原 $U,V,[p]$ 几何关系因此给
$$
G_{1,p}^{[p]}(x)
=G_{1,p}(x)-\frac{A_p}{p}G_{1,p}(\mathfrak p*x)
+G_{1,p}(\mathfrak p^2*x).
\tag{29}
$$
对(3)取 $x=(S_b,\ell_b,\omega_{t_b}/c_\varphi)$，
令 $\varphi_k=\varphi_{\mathfrak p^k}\circ\varphi$。
其次数为 $d_\varphi p^k$，且(28)使拉回微分均等于 $\omega_E$。
由(20)，(29)成为实际循环的恒等式
$$
\boxed{
\operatorname{AJ}_p\left(
\Delta_\varphi-\frac{A_p}{p^2}\Delta_{\varphi_1}
+\frac1{p^2}\Delta_{\varphi_2}\right)
(\Omega\otimes\omega_E)
=d_\varphi\,\theta^{-2}f_\Omega^{[p]}(x).}
\tag{30}
$$
图的次数变化解释了(30)的 $p^{-2}$，不能直接把(29)的
$A_p/p$ 拿去作循环系数。式(30)在有理 Chow/AJ 中使用，
不把这些 $p$ 分母冒称为统一整格上的单位。
它给一个明确的后继几何算子，而不是已经消去 Euler factor 的断言。

## 8. 全部2/17权重、原 $H$ trace 和 CM 对偶方向

把 R991 的两局部向量(24)所规定的系数记为 $c_i$，
$i$ 遍历全部 $3\cdot18$ 条 degree34 图。
先在 $L$ 上组成 $Z_L=\sum_i c_i\Delta_{\varphi_i}$。
原 finite-character 算子仍是
$$
e_{\eta_j}=\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H/K)}
\eta_j(\sigma)^{-1}\sigma.
\tag{31}
$$
取 $\operatorname{Cor}_{L/H}$ 后再作(31)，不改变其角色方向。
由(20)及 AJ 对 restriction/corestriction 的自然性，最高双线的
局部值是明确的有限和
$$
\boxed{
-\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H/K)}
\eta_j(\sigma)^{-1}
\sum_{\rho\in\operatorname{Gal}(L/H)}\sum_i
c_i\,
\frac{d_{\varphi_i}}{c_{\sigma\rho\varphi_i}}
\,b_p(\sigma\rho b_i).}
\tag{32}
$$
系数域视为固定标量，Galois 只作用在几何数据；因此(32)中的
$c_i$ 不被 $\sigma\rho$ 再共轭。每项的微分倍率按(19)重新以其共轭实际图定义，
所有评价都经同一个固定 $p$-adic 嵌入。
若某个数据的稳定子导致重复，(32)仍是带该重数的原 corestriction；
不暗中除去它或把54项改成一个球向量。
(30)同样可逐项进入(32)。

现在支付单线求值时容易漏掉的对偶方向。
R995 已给
$$
P_+^{\mathrm t}=P_-,\qquad P_-^{\mathrm t}=P_+,
\qquad e_{\eta_j}^{\mathrm t}=e_{\eta_j^{-1}}.
\tag{33}
$$
转置不共轭系数。因此若一个 de Rham 分量中的
$\Omega\otimes\omega_E$ 属于 $P_+$，则
$$
\operatorname{AJ}_p(P_+Z)(\Omega\otimes\omega_E)=0,
\quad
\operatorname{AJ}_p(P_-Z)(\Omega\otimes\omega_E)
=\operatorname{AJ}_p(P_{\rm high}Z)(\Omega\otimes\omega_E).
\tag{34}
$$
不能把(34)左边的必然零误作新类消失，更不能把它称为最高非零检测。

有一个完全明确的两个素位版本。固定系数域嵌入
$\delta_{\rm coeff}\mapsto d\in\overline{\mathbf Q}_p$。
在基域的局部嵌入 $\delta_{\rm base}\mapsto d$ 处，
$f\Omega=-d\Omega$、$g\omega_E=d\omega_E$，故该微分属于 $P_+$。
在另一嵌入 $\delta_{\rm base}\mapsto-d$ 处，它属于 $P_-$。
因此检测 R995 的 $P_+$ 类要在第二个素位使用(20)/(32)，
或者先按 R811 作真实的 $G_K$ 共轭 $\tau$，同时互换素位、
CM 线与原 finite character，再在第一个素位使用同一公式。
这是基域和系数域两个因子的明确区分；不是对 $\mathbf C_p$
任意延拓一个复共轭。

若以 Artin 因子把(31)写成已下降到 $K$ 的 motive，则测试微分
也必须放在 $\eta_j^{-1}$ 的对偶 Artin 线，正如(33)。
直接使用完整有限和(32)已保留该方向；另写单线公式时不能再
把角色反一次而不同时改变测试向量。

## 9. 已付部分与尚需的实际非零

(18)、(20)、(27)、(30)、(32)给同一个新实际来源的三种相容描述：
原曲面上的 Frobenius 规范微分方程、所有同源次数/倍率的 AJ
有限和、以及完整 $p$-depletion 的负二阶模形式。
它们保原 $H^3(2)$、$\eta_j$、9级、2/17 toric 权重和两个素位。

R998 已证明，在原完整 Bloch–Kato 条件下，取 $e_E^+$ 后的混合
分量 $\widehat\beta_j^{\,c}(1)$ 全部消失。
故**同一个新类**一旦由(32)或(30)的正确对偶求值检测非零，
其最高原 $\lambda_j$ 分量也非零。
但是 R994 的 $L(\beta_j,1)>0$ 只支付伴因子，
并不证明(32)非零；本篇也未把新图与旧 canonical 图改名为同一循环。

继续需要的是这条具体有限和的实际非零/全球 theta 比较及其跨 $p$
输入。尤其从固定 $p$ 的 Coleman 解到另一个 $p$ 的解，
不能只用(18)有相同有理系数就宣布二者 realization 保真。

## 文献

- M. Bertolini, H. Darmon, K. Prasanna, *Generalized Heegner cycles and
  p-adic Rankin L-series*, Duke Math. J. **162** (2013), 1033–1148。
  本篇实际使用 §§3.6–3.8 的 Theorem3.15、Propositions3.18/3.21/3.24、
  Lemmas3.19/3.20/3.22/3.23 及(1.4.8)，并在第5节核实局部证明的下降。
  [作者全文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/51.BDP1/paper.pdf)。
  全球 Theorem5.13 的 cyclic-ideal 条件未被冒用。
- R. Hain, *Notes on the universal elliptic KZB connection*,
  arXiv:1309.0580v6，Propositions19.6–19.7。
  [原文](https://arxiv.org/pdf/1309.0580)。
  第3节独立给了原模型的 exact-form 约化，引用用以固定 de Rham/Tate 规范。
- S. Cynk, K. Hulek, *Construction and examples of higher-dimensional
  modular Calabi–Yau manifolds*, Remark3.4 的同一 $\psi^2$ theta form；
  [原文](https://arxiv.org/pdf/math/0509424)。
  (21)/(22)使用原完整 primary 角色，未靠查表数值识别。
- R991、R995：原实际模问题、全有限向量、同源图及严格最高 projector。
- R811：原两角色约定和两个素位间的真实 $\tau$ 输送。
- R994、R998：新伴因子的严格非零中央值及完整混合 Selmer 消失。

本篇没有新增数学程序运行、数值扫描或原 Artinian 大作业重算。
