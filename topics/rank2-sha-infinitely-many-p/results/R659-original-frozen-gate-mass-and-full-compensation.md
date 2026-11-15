# R659 — 原冻结门质量的非零 Laurent 首项与完整 W 补偿的强制差

日期：2026-11-15。**状态：已证明。**

本篇继续 R653 的同一个五输入系数 $M_0$，没有另换一个单位见证。
在保留 R558 原固定 $M_3$ 和全部旧条件后，只追加两个互素实 ray。
同一冻结门经过原深度核心后，其完整单位质量模 $p$ 是一个固定的
$\lambda$ 二次有理式；这个式子的常数项由原 R594 右逆和完整六次矩
精确算出，严格非零。完整单位补域保留为另两固定系数，不可能
消掉这个常数项。

因此，在新固定 ray 内删去 $O(\sqrt X\log X)$ 个坏素数后，
对所有正四倍深度 $N$，原 $M_{0,N}$ 都是单位。
这立即使 R653 同一 $Q$ 环带的非齐次差严格非零，并给
R650 两条真实 W 失败支的**完整补偿和**一个强制非零差。
尚未将任何单独补支赋零，也未证明原完整中央非零。

## 1. 原对象、同一测试和不变的旧 ray

保持 R594、R645、R650、R653 的原规范
$$
b=17,\qquad \lambda=-\bar\pi_0^{-1},\qquad
\kappa=p\lambda^2,\qquad \beta=-\lambda,\qquad \Omega=\Omega_p .
\tag{1}
$$
物理六输入按 $(\xi_1,\xi_2,\xi_3,x,c,d)$ 排列。令
$$
\begin{aligned}
A&=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,\\
Q&=c+2d,\qquad L=2c-d,\qquad \delta=1+2\omega,\\
C&=(\xi_1-\xi_3+x)/\delta,\\
D&=\xi_1+\omega^2\xi_2-2\omega\xi_3+c+(2+3\omega)d,\qquad F=D+C,\\
H_1&=-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x,\qquad
G=13H_1+(3-2\omega)F.
\end{aligned}
\tag{2}
$$
写
$$
a=-(5+6\omega)/29,\quad b_F=(5+6\omega)/5,\quad g=3-2\omega,
$$
$$
F_0=F-aA-b_FQ,\quad D_0=F_0-C,\quad E_0=F_0+13C,\quad
G_0=13H_1+gF_0 .
\tag{3}
$$
这些量不含独立的 $Q$ 输出。完整原来源和冻结门为
$$
\mu_0=-\frac1{84}\mathcal P_{6,C}\nu_\sigma^{\otimes6},\qquad
\mathcal G_{0,N}=\{C\ {\rm unit},D_0\in p^N\},
$$
$$
p_{0,N}=\frac{\widehat P_p(D_0/\kappa^N,E_0,G_0)}{b\Omega^6},
\qquad q_{0,N}=1_{\mathcal G_{0,N}}p_{0,N}.
\tag{4}
$$
$\widehat P_p$ 始终是 R594 已发表的实际九行右逆，全部
$\lambda,\kappa$ 和固定坏整数 $D_{594}$ 都保持；没有重新选列。

R653 的全 $\mathcal S_5\boxtimes\mathcal S_5$ 身份给
$$
\boxed{M_{0,N}=-\int q_{0,N}\,d\mu_0 .}
\tag{5}
$$
这里的负号来自忘去 $Q$ 后的完整边际 $-\nu_{F_{12}}(L)$；
$M_{0,N}$ 仍是 R653 的真实五输入积分。

新增条件仅为
$$
\boxed{\pi_0\equiv-1\pmod{61},\qquad \pi_0\equiv-1\pmod{277}.}
\tag{6}
$$
R558 原 $N_0$、原 153 位 $M_3=1+37N_0K_0$ 及其原剩余类
完全不改。直接读取 R558 的固定整数，得到

| 原固定整数 | 模 61 | 模 277 |
|---|---:|---:|
| 原高 $13/19$ 模数 | 56 | 162 |
| 原 $N_0$ | 23 | 89 |
| 原 $M_3$ | 22 | 133 |

附证书逐字保存原 $N_0,K_0,M_3$ 并核原等式，
也核 $\gcd(61\cdot277,37N_0M_3)=1$。
此前全部 $29,137,79,103,263,49,1013,31$ 条件已在原
$N_0$，$37$ 的原条件另保留；没有新增模 $25$ 或模 $81$。
所以 (6) 与全部旧条件由 CRT 相容。
原已付 ray-class 素理想定理仍给固定正密度普通族。
后文只在这个族内删一个稀疏坏集，不宣称每个素数都使 $M_0$ 为单位。

## 2. 保全部伴随的完整整数 theta 框架

准确有
$$
\langle F_0,C\rangle=0,\qquad
r=N(F_0)=\frac{831}{145},\qquad
N(D_0)=r+1=\frac{976}{145}.
$$
令
$$
\boxed{E^\sharp=F_0+rC,\qquad D_0\perp E^\sharp,\qquad
N(E^\sharp)=\frac{811056}{21025}.}
\tag{7}
$$
它与 $A,Q$ 都正交。一个完整整数正交框架是
$$
(435D_0,\ 435E^\sharp,\ A,\ Q,\ R,\ S),
\tag{8}
$$
其中两个剩余行明确为
$$
\begin{aligned}
R={}&(-542-475\omega,\ 744,\ 149+175\omega,\ 691+650\omega,
                 -378-774\omega,\ 189+387\omega),\\
S={}&(-60-45\omega,\ 0,\ -21-45\omega,\ 39,\ 58+50\omega,
                 -29-25\omega).
\end{aligned}
\tag{9}
$$
其六个度数和行列式是
$$
\boxed{(1273680,\ 7299504,\ 29,\ 5,\ 1854792,\ 9672),}
$$
$$
\det(8)=3937352457600+5512293440640\omega .
\tag{10}
$$
范数因子分别为
$$
\begin{aligned}
1273680&=2^4\,3^2\,5\,29\,61,\\
7299504&=2^4\,3^3\,61\,277,\\
1854792&=2^3\,3^3\,31\,277,\qquad
9672=2^3\,3\,13\,31 .
\end{aligned}
$$
全部框架分母和行列式范数在当前普通处为单位，删固定旧坏集即可。

对每个 $\zeta\in\mu_6$，原 $C$ 旋转是
$$
R_\zeta=I+(\zeta-1)P_C,\qquad N(C)=1.
$$
附证书给完整 $(8)R_\zeta$。六行全部仍整且正交，
每行模二非零系数的个数恒为
$$
\boxed{(4,\ 4,\ 3,\ 1,\ 4,\ 4).}
\tag{11}
$$
原 odd sigma 的模二半特征在任何非零 CM 剩余系数下相同；
因此 (11) 完整支付标准 half-character，而非只比较 Gaussian 度数。
每个原分支和它们的 $C$ 平均都在
$$
\mathcal S_{1273680}\boxtimes\mathcal S_{7299504}
 \boxtimes\mathcal S_{29}^{\rm odd}
 \boxtimes\mathcal S_5^{\rm odd}
 \boxtimes\mathcal S_{1854792}\boxtimes\mathcal S_{9672}.
\tag{12}
$$
后面两个核心作用始终在此完整张量格上，保留所有四个其余伴随。

## 3. D0 四层返回与固定 Esharp 全核心

令 $N_D=1273680,\ N_E=7299504$。
原 dyadic 类是 $g_\pi=\pi_0/\bar\pi_0\equiv27+8\omega\bmod32$；
全部相应奇部分在 (6) 后为一。完整含中心模数给

| 空间 | $g_\pi\bmod2N$ | $g_\pi^2\bmod2N$ | $g_\pi^4\bmod2N$ |
|---|---|---|---|
| $N_D$ | $1432891+636840\omega$ | $1910521+1273680\omega$ | $1+N_D$ |
| $N_E$ | $6387067+10949256\omega$ | $3649753+7299504\omega$ | $1+N_E$ |

在标准偶 theta 的对称 Heisenberg lift 上，实类 $1+N$
把两个生成元原样送回：模 $N$ 的幂不变，交叉相位为一。
故两个 whole 核的四次幂分别为标量，尚须支付绝对值。

先在标准 odd $\mathcal S_{145}$ 上使用
$g_\pi\equiv1\bmod290$。完整 odd 规范使 whole 核为
$\chi_{145,p}I$。真实两 sigma 联合
$$
\sigma(z-12t)\sigma(12z+t)
 \in\mathcal S_{145}^{\rm odd}\boxtimes\mathcal S_{145}^{\rm odd}
$$
行列式为 $145$，两轴各一个 odd 系数。
两个原输入同时深的系数为 $(-\lambda)^2$，
而两个输出同时深的系数为 $\lambda^2\chi_{145,p}^2$；
原联合非零，故 $\chi_{145,p}^2=1$，没有猜其符号。

取 $\gamma_{61}=9+4\omega$，范数为 $61$。
$[12\gamma_{61}]^*\mathcal S_{145}^{\rm odd}
\subset\mathcal S_{N_D}$ 给一个真正非零锚，
其核心特征第四次为一。由完整 Heisenberg 不可约性，
$$
\boxed{K_{N_D}^{\,4}=I.}
\tag{13}
$$
固定 CM 拉回在普通处是单位，严格与原深度限制交换。

再取 $\gamma_{277}=19+7\omega$，范数为 $277$。
$$
\alpha_E=12\delta\gamma_{61}\gamma_{277}=-948+2100\omega,\qquad
N(\alpha_E)=N_E .
$$
真实 $\sigma(\alpha_E z)\in\mathcal S_{N_E}$ 的核心是
$-\lambda$，所以 normalized whole 核在这个锚上的值为 $-1$。
这确定了唯一完整算子
$$
\boxed{\mathcal J_E=K_{N_E},\qquad
\mathcal J_E\sigma(\alpha_E z)=-\sigma(\alpha_E z),\qquad
\mathcal J_E^4=I.}
\tag{14}
$$
它不是只在某个边际上的标量。

为明确“固定”的含义，选含原 $2N_E$ 挠点及完整 lift 常数的固定
有限系数域 $\mathbb L/K$。在原代数 theta 基中，Heisenberg 交织和 (14)
是一组固定代数线性方程，唯一解定义 $\mathcal J_E$。
也可令 $A_*=\sigma(\alpha_E z)$、
$\ell(F)=F'(0)/\alpha_E$、$B=-A_*\otimes\ell$，写成整个有限式
$$
\boxed{\mathcal J_E=\frac1{N_E}
 \sum_{v\in(\mathbf Z/N_E)^2} T_{g_\pi v}^{(N_E)}
                       B(T_v^{(N_E)})^{-1}.}
\tag{15}
$$
这里 $g_\pi$ 用表中固定剩余类，全部中心相位保留。
若 $U$ 是实际 whole 核，完整交织把求和化为
$U\sum_v T_v(U^{-1}B)T_v^{-1}$；
Heisenberg 正交关系给 $N_E\operatorname{tr}(U^{-1}B)U=N_EU$，
因为 $\operatorname{tr}(U^{-1}B)=1$。这证明 (15) 的绝对规范。
公式只用于固定代数系数，不把巨大有限和当作已经数值展开的矩阵。
不同普通嵌入至多取这些固定系数的有限共轭。

(12)–(14) 因而给同一个完整 $\mu_0$：
$$
\boxed{\mu_0|_{D_0\in p^N}
       =\lambda^N(P_{D_0,\kappa^N})_*\mu_0
       \quad(N\in4\mathbf Z_{\ge1}),}
$$
$$
\boxed{\mu_0|_{E^\sharp\in p}
       =\lambda(P_{E^\sharp,\kappa})_*(\mathcal J_E\mu_0).}
\tag{16}
$$
$P_{D,t}$ 是沿真实正交轴 $D$ 缩放 $t$、保持其正交补的物理映射。
坐标中固定的 $435$ 是单位，不改变深度。所有伙伴和原输入标签均保留。

## 4. 对同一冻结门的完整单位减深度

令
$$
E_\perp=E_0-\frac{\langle E_0,D_0\rangle}{N(D_0)}D_0,\qquad
G_\perp=G_0-\frac{\langle G_0,D_0\rangle}{N(D_0)}D_0,
$$
$$
G_{00}=G_\perp-\frac{\langle G_\perp,E^\sharp\rangle}
                         {N(E^\sharp)}E^\sharp .
$$
实际数值是
$$
E_\perp=\frac{1015}{488}E^\sharp,\quad
E_0=E_\perp-\frac{527}{488}D_0,\quad
G_0=G_\perp+\frac{-1581+1054\omega}{488}D_0,
$$
$$
\frac{\langle G_\perp,E^\sharp\rangle}{N(E^\sharp)}
=\frac{-229245+152830\omega}{405528}.
\tag{17}
$$
在 $D_0$ 真深域上，
$C=(E^\sharp-D_0)/(r+1)$，故 $C$ 单位准确等价于
$E^\sharp$ 单位。由 (16) 而非边际猜测得到整个式子
$$
-\lambda^{-N}M_{0,N}
=\frac1{b\Omega^6}
 \int_{E^\sharp\ {\rm unit}}
 \widehat P_p\left(D_0,E_\perp-\frac{527}{488}\kappa^ND_0,
 G_\perp+\frac{-1581+1054\omega}{488}\kappa^ND_0\right)d\mu_0 .
\tag{18}
$$

令 $\bar P_L$ 是实际 $\widehat P_p$ 在 $\kappa=0,\lambda=L$
后的固定有理多项式。R594 的整右逆保证模 $p$ 时
$\widehat P_p\equiv\bar P_\lambda$。
(18) 再把 $E^\sharp$ 单位准确拆为全域减深域，并应用 (16)，给
$$
\boxed{-b\lambda^{-N}M_{0,N}
 \equiv \mathcal A(\lambda)-\lambda\mathcal B(\lambda)\pmod p,}
\tag{19}
$$
$$
\begin{aligned}
\mathcal A(L)&=\Omega^{-6}\int
      \bar P_L(D_0,E_\perp,G_\perp)\,d\mu_0,\\
\mathcal B(L)&=\Omega^{-6}\int
      \bar P_L(D_0,0,G_{00})\,d(\mathcal J_E\mu_0).
\end{aligned}
\tag{20}
$$
两个都是固定有限 theta 来源的**完整总六次矩**；
$\Omega^{-6}$ 消掉原统一六次尺度后，其系数在固定 $\mathbb L/K$ 中。
第二个完整补项没有赋零。所有省去项都含实际 $\kappa$ 或
$\kappa^N$，而原系数在当前普通处整，故 (19) 对所有正四倍 $N$
同时成立。

## 5. 原右逆的实际非零 Laurent 首项

本节 $L$ 只作形式变量，区别于第1节物理轴；固定系数域写为 $\mathbb L$。
R594 的矩阵记作 $\mathsf B_0,\mathsf B_1$，
$\tau=(1+L)^{-1}$。其原 base 的 zero 部分严格为零，
故实际模 $p$ 列系数正好是
$$
x(L)=\frac{\mathsf B_0+\tau\mathsf B_1}{\tau-1}\,b_0
     =L^{-1}x_{-1}+x_0,
$$
$$
\boxed{x_{-1}=-(\mathsf B_0+\mathsf B_1)b_0,\qquad
       x_0=-\mathsf B_0b_0.}
\tag{21}
$$
这里 $b_0$ 是原 target 减 basePlus，未改原二十列。

令 $P_{-1},P_0$ 是把这两组系数按原
$C=(E-D)/14,\ F=(E+13D)/14$ 代入所得的 degree 六多项式；
$P_0$ 同时含固定 $-C^6/8$。
写 $P^{[0]}=P(D,0,G)$。原 $E$ 单位整逆在 $\kappa=0$
仅对 $E^0$ 项乘 $\tau$，所以准确有
$$
\boxed{\bar P_L=
L^{-1}P_{-1}+P_0-\frac{P_{-1}^{[0]}+LP_0^{[0]}}{1+L}.}
\tag{22}
$$
特别 $\bar P_L$ 至多有一个简单的 $L=0$ 极点；
$\mathcal B(L)$ 也至多简单极点，故 $L\mathcal B(L)$ 在零处正则。

定义原全矩
$$
\begin{aligned}
a_-&=\Omega^{-6}\int P_{-1}(D_0,E_\perp,G_\perp)\,d\mu_0,\\
a_0&=\Omega^{-6}\int P_0(D_0,E_\perp,G_\perp)\,d\mu_0,\\
a_-^0&=\Omega^{-6}\int P_{-1}(D_0,0,G_\perp)\,d\mu_0,\quad
a_0^0=\Omega^{-6}\int P_0(D_0,0,G_\perp)\,d\mu_0,\\
b_-&=\Omega^{-6}\int P_{-1}(D_0,0,G_{00})\,d(\mathcal J_E\mu_0),\\
b_0'&=\Omega^{-6}\int P_0(D_0,0,G_{00})\,d(\mathcal J_E\mu_0).
\end{aligned}
$$
于是完整有理式为
$$
\boxed{\mathcal A(L)-L\mathcal B(L)
 =\frac{\alpha_0+\alpha_1L+\alpha_2L^2}{L(1+L)},}
$$
$$
\alpha_0=a_-,\qquad
\alpha_1=a_-+a_0-a_-^0-b_-,\qquad
\alpha_2=a_0-a_0^0-b_0'.
\tag{23}
$$
这保留实际 $\mathcal J_E$ 的全部补偿。
后两系数不需猜值，决定非零性的常数项只来自原 $\mu_0$。

原来源最低六次生成函数恰为 R594(17)
$$
\frac1{42}(z_Zz_Q^2-z_Z^3)z_rz_cz_d,\qquad
z_Z=(z_1-z_3-2z_x)/6,\quad z_Q=(z_1+z_3)/2,\quad z_r=z_2.
\tag{24}
$$
将原完整行 $(D_0,E_\perp,G_\perp)$ 代入，
按每个单项式乘对应阶乘，得到准确全部六次矩。
再与 (21) 的原二十个 $x_{-1}$ 配对，结果是
$$
\boxed{\alpha_0=\frac{A_*+B_*\omega}{D_*}\ne0,}
\tag{25}
$$
其中
$$
\begin{aligned}
A_*={}&22420084821164281025670216551800229407940568433371135045244850831869447900665358231555978956115488853439,\\
B_*={}&11512574620170243719458383823645251680003364181097233549896030056046629969473472066724327657605374225694,\\
D_*={}&63403407885881048456431955474578485723383808058231822765102256752327597182737281338100193587049267200.
\end{aligned}
$$
这是特征零的有理恒等式，不是模某个素数的采样。
附证书保存原二十列矩、全部 $x_{-1},x_0$、
$P_{-1},P_0$ 及两套等价坐标的配对；
在原 $C/F/G$ 列和变换后 $D/E/G$ 列所得 $\alpha_0$ 完全相同。
特别完整单位补项 $L\mathcal B(L)$ 绝不可能抵消 (25)。

## 6. 同一无限族上原 M0 的单位定理

令
$$
\mathscr P(L)=\alpha_0+\alpha_1L+\alpha_2L^2 .
$$
它是在固定有限系数域内、与 $p,N$ 无关的非零多项式。
结合 (19)、(23)，得到实际质量
$$
\boxed{M_{0,N}\equiv
-\frac{\lambda^{N-1}}{b(1+\lambda)}\,\mathscr P(\lambda)\pmod p
\qquad(N\in4\mathbf Z_{\ge1}).}
\tag{26}
$$
所有隐藏的普通嵌入至多选择固定 $\mathscr P$ 的有限共轭。

选一次固定整模型并清上述有限 theta 系数与 (23) 的固定分母。
对有限扩张取范数，得到
$$
F(T)=\operatorname{Norm}_{\mathbb L/K}
 \bigl(T^2\mathscr P(-1/T)\bigr)\in K[T]\setminus\{0\}.
\tag{27}
$$
若某个原普通嵌入使 $\mathscr P(\lambda)$ 非单位，
在这些固定分母之外就有 $v_{\pi_0}(F(\bar\pi_0))>0$。
使用已发表
[固定 CM 多项式单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)，
其坏素数数目在 $p\le X$ 时为 $O_F(\sqrt X\log X)$。
本处没有将任何随 $p$ 变化的负矩或中央导数放进该引理。

原固定 ray 有正密度，删此稀疏集和全部固定分母后仍无限。
$b,\lambda,1+\lambda$ 都是单位。因此：

**定理。** 在 (6) 的原 ray 中存在相对密度一的普通素数子族，
使同一个 R594 测试、同一个 R653 来源满足
$$
\boxed{M_{0,N}\in\mathcal O^\times
\quad\hbox{对每个 }N\in4\mathbf Z_{\ge1}\hbox{ 同时成立}.}
\tag{28}
$$
这里 $N$ 的统一性来自 (26) 只有外部单位 $\lambda^{N-1}$ 随 $N$
改变；没有把一个次数随 $N$ 增长的多项式套进固定多项式引理。
(28) 也不声称新 ray 的每一个素数都合格。

## 7. 原 Q 环带及全部 W 失败补偿的非零差

继续 R653 的原
$$
\mathcal K_{N,m}=\int_{\mathcal G_{0,N},\,Q\in p^m\mathbf Z_p^\times}
 p_{0,N}\log\langle Q/p^m\rangle\,d\mu_0,\qquad m\ge0 .
$$
由已发表 [R655](R655-original-sigma-five-schwartz-and-rank-one-negative-moment.md)，当前原 $\pi_0\equiv2\bmod5$ 准确给
$\chi=\chi_{65}=-1$，whole odd5 的实际核心为 $\beta=-\lambda$。
保留 $\chi$ 记号以与 R653 完全对应，其完整两输入身份给
$$
\boxed{(\chi\lambda)^{-m}\mathcal K_{N,m}-\mathcal K_{N,0}
=-mM_{0,N}(1-\chi\lambda)\log\langle\lambda^2\rangle.}
\tag{29}
$$
原 $\log\langle\lambda^2\rangle$ 非零，
且 $1\pm\lambda$ 是当前 ray 上的单位。故在 (28) 的子族上，
对每个正整数 $m$，(29) 严格非零，准确赋值为
$$
v_p(m)+v_p(\log\langle\lambda^2\rangle).
\tag{30}
$$
完整 Mellin 中央导数的外部因子 $p-1$ 是单位，不改此赋值。
R655 已另行支付原 $I_{\Sigma,-1}\ne0$ 及完整 E80 角色；这里的
非齐次 log 行保持它自己的原测试，没有把三条不同 S5 行相互替代。

把原完整测试记作
$$
f_{N,m}=1_{\mathcal G_{0,N},\,Q\in p^m\mathbf Z_p^\times}
 p_{0,N}\log\langle Q/p^m\rangle .
$$
R634/R650 的同一 $\mu_0$ whole W 两层身份，
对这个实际测试直接给
$$
\boxed{(1-\lambda^2)\mathcal K_{N,m}=\mathcal B_{N,m},}
$$
$$
\mathcal B_{N,m}:=
\int_{W\notin p^2}f_{N,m}\,d\mu_0+
\lambda^2\int(f_{N,m}\circ P_{W,\kappa^2}-f_{N,m})\,d\mu_0 .
\tag{31}
$$
这个 $\mathcal B_{N,m}$ 是全部真实 W 补偿和。
其第二项保持 R650 的共同门、独有进入门和独有离开门，及原
gate 外的负测试；没有仅留下一个移动门。

尤其实际转置为
$$
\begin{aligned}
D_0&\longmapsto D_0-(\kappa^2-1)(6+\omega)W/60,\\
Q&\longmapsto Q+(\kappa^2-1)(5-6\omega)W/72,\qquad C\longmapsto C,
\end{aligned}
\tag{32}
$$
$E_0,G_0,p_{0,N}$ 和 log 均按同一完整物理映射变换。
故 $Q$ 环带、$D_0$ 深门、原 $W$ 单位失败支全部仍在；
不能在 (31) 上只用 R653 的 principal 单项。
若按 S5 张量分解，必须保 R653 全部五项和各自的角型测试。

联立 (29)、(31) 得到同一个原完整补偿的强制关系
$$
\boxed{
(\chi\lambda)^{-m}\mathcal B_{N,m}-\mathcal B_{N,0}
=-(1-\lambda^2)mM_{0,N}(1-\chi\lambda)
                  \log\langle\lambda^2\rangle\ne0 .}
\tag{33}
$$
原 $1-\lambda^2$ 也是单位，(33) 的准确赋值仍为 (30)。
这是对原冻结门及实际 W 补偿的非消失比较，
并非一个与原测试无关的辅助质量。

## 8. 尚未支付的全算术闭合

原 $J'_S=J'_T=0$ 给 R645/R650 的完整外部关系，
不意味着 $\mathcal B_{N,m}$ 或其中任一门分别为零。
(33) 迫它们保留显示的非齐次变化；
尚须将这种变化与原两个合格中央的同一个完整测试联立。
尤其 $m$ 的不同 $Q$ 环带在 W 变换后有 (32) 的真实移动，
不能凭 Q scalar 核把这些 W 失败支认成同一域。

R655 已给原 $I_{\Sigma,-1}\ne0$；本篇没有由此给 $H_\pm$、
$A_0,A_1$ 或两个不同 log 行指定值。这些系数及 (32) 的移动域
仍须在原完整算术关系中共同比较。
新增已完成的结论是原 $M_{0,N}$ 的单位和 (33) 的完整强制差；
主目标继续开放。

## 精确文件

- [check-r659-frozen-gate-mass-and-full-compensation.js](../scripts/check-r659-frozen-gate-mass-and-full-compensation.js)
- [check-r659-frozen-gate-mass-and-full-compensation.json](../scripts/check-r659-frozen-gate-mass-and-full-compensation.json)

脚本直接读取已发表 R594 原 JSON；它不重求右逆，不改变任何旧列。
精确重建完整框架、六个半特征、中心剩余类、原 $M_3$ 审计、
实际 Laurent 留数与全部原六次矩。$\mathcal J_E$ 的定义、完整深度
限制、有限系数域范数和全补域论证由正文支付，不以数值试素数外推。
