# R996 — 两条原 norm7 真零来源、去掉两个七挠基点及完整新整数格

日期：2026-11-26 UTC。**已证明：同一原 sigma 给两条首六阶归一的完整来源，degree 为42、70。二者在所有好惰性素数处无条件中央二重零；在已经固定的普通射线上也无条件二重零。它们在原 $h_7=7+4t+16t^2$ 的两个角点均为单位，因而真实来源环的完整规范化从四基点变为两基点。**

新 Hilbert 斜率为 $62/195$，累积主项为 $31/195$。本文支付全部195个剩余权、自由整数基、固定乘法、实际有成本整返回及同一个六位中央窗口。导子直接取原 $c_6S^{16}$，权69615；没有另引一个尚未求出的巨大最小式。乘积的中央值不由各因子的中央零推出。

## 1. 两条来源与原绝对 norm7 相位

在原 $E_1:y^2=x^3+1$、$dz=dx/(2y)$、原 sigma 上置

$$
X=x^3,\quad w=z^6,\quad
\delta^2=-3,\quad\omega=(-1+\delta)/2,\quad
\gamma=3+\omega=(5+\delta)/2,\quad N\gamma=7.
\tag{1}
$$

仍取准确 raw pull $D_\alpha f(z)=f(\alpha z)$。两个下层来源是

$$
f_6=\sigma^6=z^6+O(z^{12}),\qquad
f_{10}=\sigma^{10}x^2=z^6+O(z^{12}).
\tag{2}
$$

它们是原 standard even theta 截面、principal $\mu_6$ 型，且质量都是零。定义

$$
\boxed{
\mathcal X_{42}=
\frac{D_\gamma f_6-D_{\bar\gamma}f_6}{360\delta},\qquad
\mathcal X_{70}=
\frac{D_\gamma f_{10}-D_{\bar\gamma}f_{10}}{360\delta}.}
\tag{3}
$$

由 $\gamma^3=10+9\delta$，有
$\gamma^6=-143+180\delta$、$\gamma^6-\bar\gamma^6=360\delta$。因此两者都准确从 $z^6$ 起、首系数一，不是零函数。共轭同时交换两个 raw pull 并使 $\delta$ 变号，故(3)的全部系数有理。

R983 已付同一个 norm7 除法及有理映射：

$$
R_\gamma(X)=X+\frac{-2+6\delta}{7},\quad
A_\gamma(X)=X^2+(20-24\delta)X-8-24\delta,
\tag{4}
$$

$$
\sigma(\gamma z)=\gamma\sigma(z)^7R_\gamma(X),\qquad
x(\gamma z)=\frac{xA_\gamma(X)}{\gamma^2R_\gamma(X)^2}.
\tag{5}
$$

这些是完整原相位，尤其没有把 $\gamma$ 改成另一个相伴元。记
$q_\gamma=\gamma R_\gamma=\gamma X-2+2\delta$。于是

$$
\mathcal X_{42}=\sigma^{42}P_{42}(X),\qquad
P_{42}=\frac{q_\gamma^6-\bar q_\gamma^6}{360\delta},
\tag{6}
$$

$$
\mathcal X_{70}=\sigma^{70}x^2P_{70}(X),\qquad
\boxed{P_{70}=
\frac{A_\gamma^2q_\gamma^6-\bar A_\gamma^2\bar q_\gamma^6}{360\delta}.}
\tag{7}
$$

式(7)保全部11个系数，$\deg P_{70}=10$ 且首系数一。因
$R_\gamma\in7^{-1}\mathcal O_K[X]$、$A_\gamma\in\mathcal O_K[X]$，可以统一用

$$
P_{70}\in(360\cdot7^6)^{-1}\mathbf Z[X].
\tag{8}
$$

这里用 $(u-\bar u)/\delta\in\mathbf Z$，$u\in\mathcal O_K$；(8)是充分分母，不声称最小。固定坏素数只有 $2,3,5,7$。

### 1.1 degree42 的完整手因式分解

有

$$
q_\gamma-\bar q_\gamma=\delta(X+4),\quad
q_\gamma+\bar q_\gamma=5X-4,
$$

$$
q_\gamma^2+q_\gamma\bar q_\gamma+\bar q_\gamma^2=18X(X-2),
\quad
q_\gamma^2-q_\gamma\bar q_\gamma+\bar q_\gamma^2=4(X-8)(X+1).
$$

将 $u^6-v^6$ 按这四个因子分解，准确得到

$$
\boxed{P_{42}(X)=\frac15X(X+1)(X-2)(X-8)(X+4)(5X-4).}
\tag{9}
$$

展开也就是

$$
P_{42}=X^6-\frac{29}{5}X^5-26X^4+64X^3+32X^2-\frac{256}{5}X.
\tag{10}
$$

所以这条新来源的全部固定分母只需5。未对生成系数作有限 jet 拟合。

## 2. 两种中央的准确无条件二重零

### 2.1 所有当前好惰性素数

固定 $p=6s-1>211$，$d=p+1$、$c=[z^d]\log(\sigma/z)$。置

$$
u_\gamma=\gamma^d/7,\qquad u_{\bar\gamma}=\bar\gamma^d/7.
\tag{11}
$$

惰性 Frobenius 交换 $\gamma,\bar\gamma$，故两数均属于 $1+p\mathcal O$。对 $m=6,10$，同一完整 Newton 插值给

$$
J_{7m,D_\gamma f_m}(k)
=k!(7mc)^{-k}\gamma^{dk}[z^{dk}]f_m
=u_\gamma^kJ_{m,f_m}(k).
$$

R602 的整 Hurwitz 及限制 Tate 证明适用于这两个完整来源；它们的 regularized inner 分别为 $f^{-3}$、$f^{-5}W^2$，和 R989 用的是同一 sigma。稠密非负整数上的准确插值遂给

$$
\boxed{
J_{\mathcal X_{7m},p}(v)
=\frac{u_\gamma^v-u_{\bar\gamma}^v}{360\delta}
       J_{m,f_m,p}(v),\qquad m=6,10.}
\tag{12}
$$

第一个因子在零处消失，而 $J_{m,f_m,p}(0)=f_m(0)=0$。所以

$$
\boxed{J_{\mathcal X_{42},p},J_{\mathcal X_{70},p}
\in v^2\mathcal O\langle v\rangle.}
\tag{13}
$$

这两个零不依赖任何 rank、Selmer 或其它中央失败假设。它们是新完整来源的实际线性身份，不能传给任意 Hecke 像或乘积。

### 2.2 已固定普通射线上的 whole 核亦足够

R529 §2、R533 §3 已准确证明当前普通射线上整个标准 even $\mathcal S_6$ 的 core 为 $\beta$：其实际非零锚是 $\Theta(\delta z)$，同一个空间中明确包含 $h_6=\sigma^6$。R968 §2 则付整个标准 even $\mathcal S_{10}$ 的 core $\upsilon_p=\chi_{10}\lambda_p$。因此分别有

$$
\nu_{f_6}|_{p\mathbf Z_p}=\beta[\kappa_p]_*\nu_{f_6},\qquad
\nu_{f_{10}}|_{p\mathbf Z_p}=\upsilon_p[\kappa_p]_*\nu_{f_{10}}.
\tag{14}
$$

总质量均为零，(14)使两个完整单位质量也均为零。原 raw pull 对应真正的 $[\gamma]_*$、$[\bar\gamma]_*$；二者保持单位域。于是对指数 $(p-1)v$，

$$
\mathcal L_p^{\rm ord}(\mathcal X_{7m};v)
=\frac{\langle\gamma\rangle^{(p-1)v}
       -\langle\bar\gamma\rangle^{(p-1)v}}{360\delta}
       \mathcal L_p^{\rm ord}(f_m;v).
\tag{15}
$$

两因子仍在零处各消失，故(15)准确属于 $v^2\mathcal O\langle v\rangle$。这里只用既有原射线；没有因 $\sigma^6$ 是乘积而猜它的 core。

共同 $b=17$ 的返回为
$\mathcal X_{N,b}(z)=b^{-1}\mathcal X_{N,1}(\vartheta_bz)$，
$\vartheta_b^6=b$。这保首六阶归一、完整单位域和两个中央零。

## 3. 全部角、七挠单位及两个新余因子的完整互素

置

$$
t=-X^{-1},\quad\Theta=x\sigma^2,\quad
q=t(t-1),\quad h=7+4t+16t^2,\quad d_0=1+8t.
\tag{16}
$$

写 $\mathcal X_{42}=\Theta^{21}f_{42}$、
$\mathcal X_{70}=\Theta^{35}f_{70}$。式(9)给完整角

$$
\boxed{f_{42}=\frac q5 H_{42},\qquad
H_{42}=(1+2t)(1+8t)(1-4t)(5+4t)
=5+34t-96t^2-416t^3-256t^4.}
\tag{17}
$$

对(7)按完整定义取

$$
f_{70}(t)=(-t)^{11}P_{70}(-1/t),\qquad H_{70}=f_{70}/q.
\tag{18}
$$

下面同时证明这个除法及全部必要的精确阶。

### 3.1 $0,1,\infty$ 的准确 profile

两个原首项给 $\operatorname{ord}_0f_{42}=
\operatorname{ord}_0f_{70}=1$。由(17)，

$$
\deg f_{42}=6,\qquad f_{42}'(1)=-3^6/5.
\tag{19}
$$

在 $X=-1$，原 norm7 公式给

$$
q_\gamma=-3\delta\omega^2,\quad
\bar q_\gamma=3\delta\omega,\quad
A_\gamma=\bar A_\gamma=-27.
$$

所以(7)的两个分子项相等，$P_{70}(-1)=0$。它们的对数导数分别为

$$
2\frac{A_\gamma'}{A_\gamma}
 +6\frac{R_\gamma'}{R_\gamma}
=-\frac{10}{3}+\frac49\delta,\qquad
-\frac{10}{3}-\frac49\delta.
$$

共同值为 $-3^{15}$，故

$$
P_{70}'(-1)=-3^{11}/5,\qquad
f_{70}'(1)=3^{11}/5.
\tag{20}
$$

此外直接在(7)代 $X=0$ 得
$P_{70}(0)=2^{17}/15$。因此

$$
\boxed{\deg f_{70}=11,\quad\deg H_{70}=9,\quad
\operatorname{ord}_1f_{42}=
\operatorname{ord}_1f_{70}=1.}
\tag{21}
$$

这些首项和导数在当前全部 $p>211$ 为单位。

### 3.2 两个七挠角都真实非零

式(17)有显式整 Bézout 身份

$$
\boxed{(107-36t-240t^2-128t^3)h-(8t+4)H_{42}=729.}
\tag{22}
$$

例如先用
$H_{42}=h(-16t^2-22t+13/2)+(81/2)(4t-1)$、
$h=(4t-1)(4t+2)+9$ 即得。又 $h$ 与 $q$ 的 resultant 为189，故(22)证明 $f_{42}$ 在整个 $R[t]/h$ 中为单位，而不止某一个几何点非零。

对 $f_{70}$，在非零 $T\in\ker\gamma$ 上，$D_\gamma f_{10}(T)=0$；$\bar\gamma T=5T$ 是非零七挠点，既非原点也不满足 $x=0$，故另一 pull 非零。共轭核相同。完整(7)还给固定 resultant：

$$
\operatorname{Res}_X(7X^2-4X+16,P_{70})
=\frac{2^{34}3^{25}}{25},
$$

$$
\boxed{\operatorname{Res}_t(h,f_{70})
=\frac{7\cdot2^{34}3^{25}}{25}.}
\tag{23}
$$

为核其尺度，令 $r$ 为 $R_\gamma$ 的根，则
$\bar\gamma\bar R_\gamma(r)=-12\delta/\gamma$、
$\bar A_\gamma(r)=\omega^2(\bar\gamma\bar R_\gamma(r))^2$。
所以 $P_{70}(r)=-\omega(-12\delta/\gamma)^{10}/(360\delta)$，其二次范数是
$(432/7)^{10}/388800$。乘首项 $7^{10}$，再按(18)返回负角，正好是(23)。这同时保两个根、全部相位与固定坏集。

### 3.3 两个新来源在原两基点之外没有共同零

这是下一节真正无基点参数的输入，不能只由(22)推断。由

$$
A_\gamma-\bar A_\gamma=-48\delta(X+1),\quad
A_\gamma+\bar A_\gamma=2(X^2+20X-8),
$$

在 $P_{42}$ 的根且 $q_\gamma^6=\bar q_\gamma^6=B$ 处，有

$$
P_{70}=-\frac4{15}B(X+1)(X^2+20X-8).
\tag{24}
$$

对 $H_{42}$ 的全部四根，(24)逐一给

| $t$ | $H_{70}(t)$ |
|---|---|
| $-1/2$ | $-2\cdot3^7/5$ |
| $-1/8$ | $3^{11}/(2^{10}5)$ |
| $1/4$ | $-3^7/(2\cdot5)$ |
| $-5/4$ | $3^{11}/2$ |

这里使用的准确返回是
$H_{70}(-1/r)=P_{70}(r)/(r^9(r+1))$，没有删除因子或换根。四值均为当前单位，且 $\operatorname{lc}H_{42}=-256$，故

$$
\boxed{\operatorname{Res}(H_{42},H_{70})
=-\frac{2^{61}3^{36}}{5^3}\ne0.}
\tag{25}
$$

所以两条新角的完整 gcd 准确为 $q=t(t-1)$。所有真实 resultant 只引入已经排除的 $2,3,5,7$；本节不需要读取或保存任何生成矩阵。

## 4. 同一函数域中的两基点规范化

沿 R960 取原完整六源环
$A^{(6)}=R[S,T,U,V_{66},W_{178},Z]$、同一原整环 $R$，并保其全部固定坏集与实际 $\Delta_Z$。新环取

$$
A^{(8)}=A^{(6)}[\mathcal X_{42},\mathcal X_{70}].
\tag{26}
$$

式(8)、(25)所需的固定整数已在原 $R$ 中可逆。R960 的全函数域已经是 $\mathbf Q(t,\vartheta)$，新来源仍在这个域，所以
$\operatorname{Frac}A^{(8)}=\mathbf Q(t,\vartheta)$。

旧六源的准确极比是 $64/195$，四个原有限基点的最小零比都是 $1/195$。由(19)–(23)，加入两源以后 $0,1$ 的最小零比不变，两个 $h$ 根的最小零比降到零。没有其它共同基点；原六源自身已排除它们。又
$6/21<64/195$、$11/35<64/195$，故无穷远极比不增。因此准确候选规范化是

$$
\boxed{D_8=\frac{64[\infty]-[0]-[1]}{195},\qquad
B^{(8)}_m=\vartheta^m q^{\lceil m/195\rceil}
 R[t]_{\le b_m},\quad
b_m=\left\lfloor\frac{64m}{195}\right\rfloor
-2\left\lceil\frac m{195}\right\rceil.}
\tag{27}
$$

负上界表示零空间。这个完整分次环是 $R[t,\vartheta]$ 与各实际 Gauss 赋值环的交，故正规。以下证明真正有限整性，从而确证(27)为规范化。

### 4.1 同权1365的三个真实无基点参数

R960 已有原完整 $f_Z=qhG$、$\deg G=60$、$\gcd(qh,G)=1$，其首项及对应 resultant 在 $R$ 上为单位。置

$$
L=1365=7\cdot195=65\cdot21=39\cdot35,\qquad
M=434=7\cdot62,\qquad\rho=\vartheta^Lq^7.
\tag{28}
$$

三条实际原来源的同权幂为

$$
\boxed{
\mathcal X_{42}^{65}=\rho\,q^{58}(H_{42}/5)^{65},\quad
\mathcal X_{70}^{39}=\rho\,q^{32}H_{70}^{39},\quad
Z^7=\rho\,h^7G^7.}
\tag{29}
$$

三个括号的次数分别为376、415、434。它们作为 $\mathcal O_{\mathbf P^1}(434)$ 的截面在整个 $\mathbf P^1_R$ 上无共同零：

- 在 $q=0$，第三个由原 $\gcd(qh,G)=1$ 为单位；
- 在 $q\ne0$ 的有限部分，前两个由完整(25)不同时为零；
- 在无穷远，第三个的434次首项为单位。

这是固定同来源、同剩余域的完整无基点结论。没有随机挑参数或把七挠两根压成一个点。

### 4.2 全部剩余权及固定生成权2733

对 $0\le r<L$ 置

$$
Q_r=q^{\lceil r/195\rceil},\qquad
q_r=\lfloor64r/195\rfloor-2\lceil r/195\rceil.
$$

准确有

$$
B^{(8)}_{Ln+r}
=\vartheta^rQ_r\rho^nR[t]_{\le Mn+q_r}.
\tag{30}
$$

全部 $q_r\ge-2$；$q_r=-2$ 恰为 $r=1,2,3$，其它 $q_r\ge-1$。这由写 $r=195a+u$ 得 $q_r=62a+q_u$ 后直接逐区间核定。

对(29)的三个无基点截面，用完整三元 Koszul 复形。其第一段给

$$
0\longrightarrow\mathcal O(d-3M)
\longrightarrow\mathcal O(d-2M)^3
\longrightarrow\mathcal K_d\longrightarrow0,
$$

$$
0\longrightarrow\mathcal K_d
\longrightarrow\mathcal O(d-M)^3
\longrightarrow\mathcal O(d)\longrightarrow0.
\tag{31}
$$

取 $d=Mn+q_r$。当 $d\ge2M-1$，$H^1(\mathcal O(d-2M))=0$，且 $\mathbf P^1_R$ 上 $H^2$ 为零，所以 $H^1(\mathcal K_d)=0$。于是三条实际参数的乘法在完整整格上满射。

因此 $q_r\ge-1$ 时只需保 $n=0,1$，而 $r=1,2,3$ 另保 $n=2$。这给固定有限模生成集，最高原权准确可取

$$
\boxed{M_{\rm gen}=2L+3=2733.}
\tag{32}
$$

故 $B^{(8)}$ 在原子环
$R[\mathcal X_{42}^{65},\mathcal X_{70}^{39},Z^7]$ 上有限，从而在 $A^{(8)}$ 上有限。结合完整函数域与正规性，(27)是整个环的规范化，不只是某个 Veronese 的描述。

## 5. 直接使用旧导子的真实整返回

R960 已付非零齐次 $c_6\in A^{(6)}$，权69343，并有
$c_6B^{(6)}_m\subset A^{(6)}_{m+69343}$；其完整允许剩余域中 $\bar c_6\ne0$。

对(32)内任一个固定生成元 $g\in B^{(8)}_m$，有 $m\le2733$。乘原
$S^{16}=\vartheta^{272}(qhd_0/7)^{16}$ 后，

$$
\boxed{S^{16}g\in B^{(6)}_{m+272}.}
\tag{33}
$$

全部四角和次数可直接核：$h$ 的次数16至少为
$\lceil(m+272)/195\rceil\le16$；$0,1$ 的次数更大；而角次数增加80，不超过帽的增加
$\lfloor64(m+272)/195\rfloor-\lfloor64m/195\rfloor\ge89$。

因此可固定取

$$
\boxed{c_8=c_6S^{16},\qquad C_8=\operatorname{wt}c_8=69615=17\cdot4095,}
\tag{34}
$$

并由(29)的完整有限模生成得到对所有权的真实导子

$$
\boxed{c_8B^{(8)}_m\subset A^{(8)}_{m+C_8}.}
\tag{35}
$$

式(35)不是将任意大权先乘固定 $S^{16}$ 直接放回旧帽；(33)只对2733内的固定生成元使用。任意大权先经(29)的实际来源参数返回，再逐个使用(33)，所以原所有来源和权均被保留。

在每个允许好 $p$，$\bar c_8\ne0$ 于完整整环 $B^{(8)}/pB^{(8)}$。若 $c_8b=pa$、$a\in A^{(8)}$，约化先给 $b=pb_1$，继而 $a=c_8b_1$。所以导子像在原来源环中 $p$-饱和；不由此推断任何截断 jet 像饱和。

固定选择(32)生成集、三参数乘法返回及(33)的原整表达，给

$$
\deg_{\rm sources}\operatorname{return}(c_8b)
\le\left\lfloor\frac{m+69615}{17}\right\rfloor,\qquad
\|\operatorname{return}(c_8b)\|_1
\le C^{m+1}\|b\|_{\rm basis}.
\tag{36}
$$

这是一次固定有限表的迭代，分母素数不随 $m$ 改变。按 R957/R960 的同一整数像格及真正商范数，固定清分母 $D_{\rm ret}^{m+1}$ 给实际整单射，实位费用 $O(m+1)$，有限位只在同一固定坏集累计。没有为有理补空间另定标准整数格。

### 5.1 原六块导子位移的完整成本

若原 $c_6=\Theta^{69343}q_6(t)$ 的原点阶为 $r_c$，则

$$
r_8=r_c+16,\qquad372\le r_8\le22774,
\qquad\mathcal E_{\rm tot}=\mathcal E+4095.
\tag{37}
$$

原整首项单位不变，因为 $S$ 的首六阶系数为一。R960(50)–(53)按这些准确量返回：完整因子包含
$\exp(4095a_p\epsilon)$，整个五次高轴展开仍保留；乘 $w^{r_8}$ 有 $5r_8$ 个 Smith 指数一及 $r_8$ 个自由余目标方向。相比旧导子只新增80个固定跨界费用和272的来源权。要求仍为原完整 $L+r_8<p$、$\ell+r_8\le s-5$ 等实际窗，不能删最后短块。

## 6. 全195余权的同一个饱和整数格

定义

$$
\Lambda^{(8)}_m=\vartheta^m q^{\lceil m/195\rceil}
\mathbf Z[t]_{\le b_m},\qquad
\Lambda^{(8)}=\bigoplus_{m\ge0}\Lambda^{(8)}_m.
\tag{38}
$$

$q$ primitive，Gauss 引理给
$\Lambda_m^{(8)}=B_m^{(8)}(\mathbf Q)\cap\vartheta^m\mathbf Z[t]$。
这是同一实际整数格，在所有素数的显示基中均独立。原六源及新两源统一乘
$\operatorname{lcm}(2275,5,360\cdot7^6)$ 后都在其对应权空间；固定缩放不改变中央零。

令

$$
\rho_8=\vartheta^{195}q,\qquad g=62,\qquad
P_0=\mathbf Z[\rho_8,\rho_8t^{62}].
$$

对 $0\le r<195$ 用同一 $Q_r,q_r$，$0\le i<62$，置

$$
h_{r,i}=\left\lceil\frac{i-q_r}{62}\right\rceil,
\qquad b_{r,i}=\vartheta^rQ_r\rho_8^{h_{r,i}}t^i.
\tag{39}
$$

全部 $h_{r,i}\in\{0,1,2\}$。值2仅出现在 $r=1,2,3$、$i=61$，所以完整基权不超过393。准确自由模身份是

$$
\boxed{\Lambda^{(8)}=
\bigoplus_{\substack{0\le r<195\\0\le i<62}}P_0b_{r,i},
\qquad\operatorname{rank}_{P_0}\Lambda^{(8)}=12090.}
\tag{40}
$$

证明固定总权 $m=195n+r$，把真实角指数唯一写成 $j=62v+i$。原帽 $j\le62n+q_r$ 等价于 $n-v\ge h_{r,i}$，并准确有

$$
\vartheta^rQ_r\rho_8^nt^{62v+i}
=b_{r,i}\rho_8^{n-v-h_{r,i}}(\rho_8t^{62})^v.
\tag{41}
$$

这是全部整单项式基的置换，系数一；独立性在同总权约共同非零因子后比较角单项式即得。

若 $r+s=195\delta_0+r'$，则完整乘法只多一个因子

$$
\frac{Q_rQ_s}{q^{\delta_0}Q_{r'}}=q^\varepsilon,\qquad
\varepsilon=\lceil r/195\rceil+\lceil s/195\rceil
-\lceil(r+s)/195\rceil\in\{0,1\}.
\tag{42}
$$

其次数不超过2，系数绝对值和不超过2。先乘(39)，再按(41)返回，故每个完整乘法行最多两项，$P_0$ 系数的总次数不超过5，整数系数绝对值和不超过2。所有指数非负由原 floor/ceiling 帽保证，未忽略任何余权或 carry。

$P_0$ 的两参数首先属于规范化；将它们用于原来源时仍支付(35)，不能把它们另赋为中央零的算术来源。

## 7. 实际 Hilbert 改善及全部位的同源含义

由(27)、(35)，

$$
\operatorname{rank}B^{(8)}_m=\frac{62}{195}m+O(1),\qquad
\boxed{\sum_{j\le M}\dim A^{(8)}_j
=\frac{31}{195}M^2+O(M).}
\tag{43}
$$

原累积系数为 $2/13=30/195$，所以真实增量是 $1/195$。该增量来自同一函数域内两个七挠基点的移除；$0,1$ 仍是基点，规范化并未成为任意多项式环。

每个显示单项式的 $t$ 次数仍不超过 $\lfloor64m/195\rfloor<m/3$，因而代入 $\Theta,t$ 后全部是无极的原 theta 来源。R960 的实增长证明逐项适用，指数仍为 $\exp(O(m|w|^{1/3}))$，并保持(36)的整返回费用。新的有限评价仍先在(38)的完整整数格中取像，再用真实商范数；普通测度仍先原加法卷积后切完整单位域。

上述结论尚不构造一个受迫的全深核。即便若干生成元的中央导数全零，也不能由此给 $\mathcal X_{42}^a\mathcal X_{70}^bS^c$ 的中央导数赋零。新格的全部后页和原仿射 forcing 必须在实际同一个矩阵中检验。

## 8. 两条真零同时进入原完整六位必要系统

仍用 R989 的原 $W=z^2x$、$f=\exp(-2(F-cw^s))$、
$\kappa=34c$、$a=p\kappa\in\mathcal O^\times$、五个原高轴 $x$。
新 charge 分别为21、35，$q_{42}=21/17$、$q_{70}=35/17$。完整 regularized inner 为

$$
B_{42}=w^{-1}\mathcal X_{42}e^{-q_{42}\kappa w^s}
=f^{-21}\sum_{j=0}^{5}b_jw^jW^{18-3j},\quad b_0=1,
$$

$$
B_{70}=w^{-1}\mathcal X_{70}e^{-q_{70}\kappa w^s}
=f^{-35}\sum_{j=0}^{10}c_jw^jW^{32-3j},\quad c_0=1.
\tag{44}
$$

(10)、(7)分别唯一指定全部固定系数。$W$ 最低幂分别为3、2，所以 R989 的整个 Hurwitz 尾、$h=7,8$ 的真实整端点和全部 $h\ge9$ 界均以同一半径成立。最高输入仍是 $W,f$ 到 $w^p$，保原两次真实除 $p$ 与八位初始精度。

对 $\nu=42,70$ 定义同一六项表达

$$
F_\nu^{[6]}(x)=\sum_{h=1}^6
\frac{(-1)^{h-1}(h-1)!p^{h-1}}{q_\nu^ha^{h-1}}
[w^{hs-1}]B_\nu e^{q_\nu\eta_x}.
\tag{45}
$$

则 $F_\nu^{[6]}(0)\equiv(a/p)J'_\nu(0)=0\pmod{p^6}$ 无条件成立。在原五 canonical 坏中央的假设下，R989 唯一必要点 $x^{\dagger,[6]}$ 等于实际点模 $p^6$。两条新增准确余式是

$$
\boxed{\mathfrak r_{\nu|5,p}^{[6]}
=F_\nu^{[6]}(x_5)-b_\nu B_5^{-1}
 F_{\mathrm{old5}}^{[6]}(x_5)=0\pmod{p^6},
\quad\nu=42,70.}
\tag{46}
$$

这里 $b_\nu$ 是这条完整来源的原前五系数行，$x_5$ 是旧五位点任意整提升；原五项仍各读至第六位。连同 R992 的第十一来源，这给同一个五参数系统两条进一步的真行，不增加第七长块。

新整数格仍用 R960 的同一完整
$\Gamma_L^{(6)}=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^6,w^\ell\epsilon^5)$。
其评价是实际代入
$P(t(w),h_x(w)\exp(a\epsilon/17))$，对每个真实权分别使用 Euler 算子。由 $x^{\dagger,[6]}\equiv0\pmod{p^6}$，这个完整评价在模 $p^6$ 的目标中逐列逐行不动，包括全部低权及每个有序物理前缀。若经过导子，则另保(37)的整个长目标与 $5r_8$ 固定跨界。

这一精确同点比较不声称无限精度核相同，也不把十三条来源的低 jet 数目变成十三个深块。原 $a+2b<3$、每个真正低卷积、全部 $P_2/Z$ 平移缺陷及完整强迫项均继续在后续同格预算中。

## 依赖与证明范围

- R529 §2、R533 §3：原 whole degree6 的绝对 ordinary core；R968 §2：原 whole degree10 core。
- R983：原 norm7 的完整 $R_\gamma,A_\gamma$ 及 sigma 相位。
- R602/R614/R989：同一整 Hurwitz、完整除 $p$ 输入及六位中央尾。
- R960：原六源全函数域、$f_Z=qhG$ 的真实 profile/全部 resultant、旧 $c_6$、来源像格与完整六块。
- R992：同原 mass-zero raw pull 差的完整中央机制；本篇的新 norm7 两源另以(3)–(15)直接证明。

所有新多项式、值、resultant 和整模恒等均由本文有限显示公式手证；没有调用新增数学执行或存放生成数据。实际进展是两条新真零、两个基点的移除以及带固定全成本的新格；无穷素数主目标尚须真实 forcing。
