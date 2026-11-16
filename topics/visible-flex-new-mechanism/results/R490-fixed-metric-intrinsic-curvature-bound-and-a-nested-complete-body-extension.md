# R490：当前固定度量的全域内在曲率界与九个完整新增体段自由度

2026-11-16。**纸面结论与新表示定义；没有执行几何、积分、Jacobian、求解或检查。** 所有已付159维实际任务与其接受点均保持原样。本文先核固定目标度量是否已被 reach 的 Gaussian 必要界排除，再给当前159坐标的一个严格嵌套扩展。后者没有被实际优化，也不预告可行下降。

## 1. 当前固定 g 的准确来源

当前 O2 的完整目标为

$$
g=ds^2+a(s)^2d\theta^2,\qquad
a=a_*\exp h,
\qquad h=w f,
\tag{1}
$$

其中 $a_*$ 是原三段 S5/S5/S11 种子，$f$ 是五次夹持样条，$w=16x^2(1-x)^2$。这里只用已公开原
[167维首次实际的完整源](../notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json)
之 selected metric；不评价其几何。该文件425422字节、SHA256
`c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46`。
完整数学身份为

`fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`。

定义由 `BodyLogRadius` 和 `NegativeKRadialSeed` 原源码给出，不把原种子单独冒充当前 g。永久 $b_0$、原 enriched $c_0$ 与当前 selected/accepted 系数仍为不同对象。

种子参数为

$$
L=\frac9{10},\quad r_c=\frac{11}{50},\quad
c_0=\frac1{25},\quad c_f=\frac3{50},\quad
(f_1,f_2,f_3)=\left(\frac14,\frac7{20},\frac25\right),
\quad \mu-\nu=\frac3{10}.
\tag{2}
$$

body 对数扰动支撑是

$$
[s_c,s_b]=\left[\frac9{250},\frac{373}{500}\right],
\qquad \ell_b=\frac{71}{100},\quad
\delta_b=\frac{\ell_b}{6}=\frac{71}{600},
\qquad x=\frac{s-s_c}{\ell_b}.
\tag{3}
$$

区间外 $h=0$。五次样条全系数为
$(0,0,0,c_3,c_4,c_5,c_6,c_7,0,0,0)$，两端各六重结点、六个等长 span。原五个准确有理系数及足够本文用的有理包围为：

| 全编号 | 原准确系数 | 严格区间 |
| --- | --- | --- |
| $c_3$ | $2186981172006301/9007199254740992$ | $(6/25,1/4)$ |
| $c_4$ | $987499536248303/9007199254740992$ | $(1/10,3/25)$ |
| $c_5$ | $2326157400936351/9007199254740992$ | $(1/4,13/50)$ |
| $c_6$ | $1786333982871343/72057594037927936$ | $(1/50,3/100)$ |
| $c_7$ | $3629607443551657/18014398509481984$ | $(1/5,21/100)$ |

这些包围只需整数交叉相乘，不是新数值采样。

## 2. 全域 Gaussian 曲率的纸面上界

### 2.1 原种子的统一界

准确椭圆核心 $A=1,B=7/25$ 的周长平均满足 Cauchy–Schwarz 给出的

$$
a_0=\frac{1}{2\pi}\int_0^{2\pi}
\sqrt{\sin^2t+\frac{49}{625}\cos^2t}\,dt
\le\frac{\sqrt{337}}{25}<\frac34.
\tag{4}
$$

代原种子的线性斜率公式，得到 $0<\nu<9/20$、$\mu<3/4$；原正性见
[R33](R33-elliptic-core-reach-and-reflected-phase-budget.md)。
因此全区 $a_*\ge11/50$、$|a_*'|\le1$。

三个活动段的物理长度依次为 $81/400,567/2000,81/250$。
由

$$
0\le S_5'\le\frac{15}{8},\qquad
0\le S_{11}'\le\frac{693}{256},
$$

逐段直接得到

$$
|K_*|=\left|\frac{-a_*''}{a_*}\right|
<\max\left\{32,10,\frac{21875}{576}\right\}<38.
\tag{5}
$$

开核心和开平尾的 $K_*$ 为零。这里保完整三段，不用某个网格极值代替连续界。

### 2.2 body 样条的两阶导数界

由非负 B 样条分割，$0\le f\le13/50$。记 $d_i$ 为 $\delta_b f'$ 的导数样条系数，非零部分是

$$
\begin{split}
d_2&=5c_3/3,\quad d_3=5(c_4-c_3)/4,\quad
d_4=c_5-c_4,\\
d_5&=c_6-c_5,\quad d_6=5(c_7-c_6)/4,\quad d_7=-5c_7/3.
\end{split}
\tag{6}
$$

其余为零，故 $|d_i|<5/12$。$\delta_b^2f''$ 的非零系数依次为

$$
2d_2,\quad\frac43(d_3-d_2),\quad d_4-d_3,\quad
d_5-d_4,\quad d_6-d_5,\quad\frac43(d_7-d_6),\quad-2d_7.
\tag{7}
$$

中央分母是 $4\delta_b$，故第四项没有额外 $4/5$。
用第1节五个区间，每项绝对值小于 $5/6$。再次用导数样条凸包，得到

$$
\|f'\|_\infty\le\frac{250}{71},\qquad
\|f''\|_\infty\le\frac{300000}{5041}.
\tag{8}
$$

准确权重满足
$0\le w\le1$、$\|w_x\|_\infty=16/(3\sqrt3)<16/5$、
$\|w_{xx}\|_\infty=32$。从 $h=wf$ 的完整乘积法则，

$$
\begin{split}
\|h'\|_\infty
&<\frac{16}{5\ell_b}\frac{13}{50}+\frac{250}{71}
=\frac{1666}{355}<5,\\
\|h''\|_\infty
&\le\frac{32}{\ell_b^2}\frac{13}{50}
 +\frac{32}{5\ell_b}\frac{250}{71}
 +\frac{300000}{5041}
=\frac{543200}{5041}<108.
\end{split}
\tag{9}
$$

原样条保留列在端点三阶消失，权重另给二阶；所以零延拓的 $h$ 至少四阶连续，以上界也覆盖支撑端点。

### 2.3 对 reach 必要界的准确含义

固定目标的完整曲率是

$$
K_g=K_*-2\frac{a_*'}{a_*}h'-h''-(h')^2.
\tag{10}
$$

结合 (5)、(9)，全域严格有

$$
\boxed{\ |K_g|<
38+\frac{100}{11}\,5+108+25
=\frac{2381}{11}<217<225<
\left(\frac{1000}{61}\right)^2.\ }
\tag{11}
$$

这里“全域”指当前 O2 **整个抽象闭面上的固定目标度量**。上面的计算覆盖两侧连接区 $s\in[0,L]$；负侧为同一度量的反射，中央椭圆柱的内在度量准确平坦。余下的六弓帽也准确平坦：$R=137/500$ 是材料圆盘外半径，不是球半径。[R44 §3–4(6)–(9)](R44-S9-six-cap-exact-embedding-and-normal-chord.md) 的有限 S9 圆弓在材料盘内互不交，完整帽映射拉回度量恰为 $dp_1^2+dp_2^2=dr^2+r^2d\theta^2$；因此 $K_g=0$，弦及顶点由其 $C^5$ 正则性延续。它在开放尾领按 $r=r_c+L-s$ 与 (1) 相接，中心使用 Cartesian 盘图。[R55 §1](R55-saturated-heat-third-Cauchy-jet-analytic-space-obstruction.md) 及现有 `PolygonalFlatTail`/自然帽源码沿用的正是这同一个物理帽，没有另加球帽或新度量过渡片。故 (11) 覆盖完整目标 g；这不是对尚未等距的当前实际候选之诱导 Gaussian 曲率作界。

若一个准确等距实现具有 reach 至少 $61/1000$，其主曲率必须满足
$|\kappa_i|\le1000/61$，从 Gauss 方程便必须有
$|K_g|=|\kappa_1\kappa_2|\le(1000/61)^2$。
(11) 说明**当前固定 g 不违反这个 Gaussian 乘积必要条件**。
因此不能从 $K_g=-a''/a$ 推出当前约58的外在曲率峰是不可降低的内在下界。

这没有构造主曲率、解 Gauss–Codazzi、证明给定端口可延拓或认证 reach。特别是 $\sqrt{|K_g|}$ 是主曲率最大值的必要下界，不是主曲率最大值的上界。当前非等距状态的曲率来自它的实际第一、第二基本形式；不能把当前诱导曲率直接替换为 $K_g$。原核心本身仍有 $A/B^2=625/49$ 的固定外在曲率，未被本文改动。非局部法弦、整面嵌入、连续度量误差与全时间条件均继续保留。

## 3. 一个完整嵌套的九列 body 扩展

当前159独立坐标的原场记为

$$
u_q(s,\theta),\quad v_q(s,\theta),\quad
b_q(s),\quad
z_q(s)=z_q(0)+\int_0^s b_q(t)\,dt,
\qquad q\in\mathbb R^{159}.
\tag{12}
$$

这里包括原159到163的准确高度坐标、全部原自然帽/入口修正、单Q、五高度及永久 reference。原 $a,b_0,c_0$ 全部保留；(12) 不以某次 accepted 场重新定义 reference。

令

$$
s_c=\frac9{250},\quad s_f=\frac{423}{500},\quad
\ell=s_f-s_c=\frac{81}{100},\qquad
\xi=\frac{s-s_c}{\ell}.
$$

对整数 $m\ge5$ 定义准确函数

$$
P_m(\xi)=
\begin{cases}
\xi^m\exp\!\left(-\dfrac{\xi}{1-\xi}\right),&0<\xi<1,\\
0,&\xi\le0\text{ 或 }\xi\ge1.
\end{cases}
\tag{13}
$$

它在右端平坦，在左端只具有有限阶消失：
$P_m\in C^{m-1}(\mathbb R)$，且 $P_m(\xi)=\xi^m+O(\xi^{m+1})$。
不能把指数因子在左端的零延拓说成连续，也不能把 $P_5$ 说成全端 $C^\infty$；实际使用的是 (13) 的乘积及其连续极限。

新增参数
$\alpha=(\alpha_1,\ldots,\alpha_4)$、
$\beta=(\beta_1,\ldots,\beta_4)$ 和 $\gamma$，定义

$$
\begin{aligned}
\widetilde u&=u_q+P_5(\xi)\sum_{j=1}^4\alpha_j\sin(2j\theta),\\
\widetilde v&=v_q+P_8(\xi)\sum_{j=1}^4\beta_j\sin(2j\theta),\\
\widetilde z&=z_q+\ell\gamma P_8(\xi),\qquad
\widetilde b=b_q+\gamma P_8'(\xi).
\end{aligned}
\tag{14}
$$

撇号在 (13)–(15) 指 $\xi$ 导数。故

$$
\Delta b_s=\frac\gamma\ell P_8''(\xi),\qquad
\Delta b_{ss}=\frac\gamma{\ell^2}P_8'''(\xi),\qquad
\int_0^L\Delta b\,ds=0.
\tag{15}
$$

新空间为168独立坐标，嵌入是
$q\mapsto(q,0_4,0_4,0)$。这不是把原163家族重新命名；它是一个新空间，原物理场在新增九列为零时准确包含。

(14) 在入口分别从 $u_5,v_8,b_7$ 起；准确首系数为
$\ell^{-5}\sum\alpha_j\sin2j\theta$、
$\ell^{-8}\sum\beta_j\sin2j\theta$、
$8\gamma\ell^{-7}$。
原已知 $u_4/v_7/b_6$ 保持。这里没有声称任意这些高阶系数组合都满足 Cauchy 方程：完整度量仍须求解。与只在入口截取 leading 不同，(13)–(15) 是整个活动 body 的完整定义，全部导数和转接项进入真实几何。

## 4. 全部新增径向项与原角闭合

在 $0<\xi<1$ 写 $\chi=\exp(-\xi/(1-\xi))$、
$Q=(1-\xi)^{-2}$、$R=(1-\xi)^{-3}$。需要的前三导数为

$$
\begin{aligned}
P_m'={}&\chi[m\xi^{m-1}-Q\xi^m],\\
P_m''={}&\chi[m(m-1)\xi^{m-2}
 -2mQ\xi^{m-1}+(Q^2-2R)\xi^m],\\
P_m'''={}&\chi[m(m-1)(m-2)\xi^{m-3}
 -3m(m-1)Q\xi^{m-2}
 +3m(Q^2-2R)\xi^{m-1}\\
&\hspace{29mm}+\{-(1-\xi)^{-6}
 +6(1-\xi)^{-5}-6(1-\xi)^{-4}\}\xi^m].
\end{aligned}
\tag{16}
$$

端点按实际连续极限取零，外部取零；径向导数再乘相应 $\ell^{-j}$。角导数使用完整
$\partial_\theta\sin(2j\theta)=2j\cos(2j\theta)$，不裁成别的角族。

令 $\psi=\theta+\widetilde u$，
$c=(1+\widetilde v^2)^{-1/2}$，则完整单位切向为

$$
T=cH+\widetilde v c\,e_z,\qquad
H=(-\sin\psi,\cos\psi,0).
\tag{17}
$$

新增 $u,v$ 都为 $\pi$ 周期反射奇函数，保持原场对称。水平部分在
$\theta\mapsto\theta+\pi$ 下反号，竖直部分对 $\theta\mapsto-\theta$ 为奇。因此
$\int_0^{2\pi}T\,d\theta=0$。不能把整个三维 $T$ 误说成半转反周期。

以原零均值周期原函数 $\Pi$，完整位置仍为

$$
X=a\Pi T+\widetilde z\,e_z.
\tag{18}
$$

于是 $X_\theta=aT$、$G=a^2$ 恒成立，目标 g 没有改变。$\Pi$ 逐圈作用，不产生径向传播；高度则用 (14) 的同一个准确原函数，不重新划分旧 $b_0$ 的求积，也不对不同角圈重设中心。

## 5. 完整 ordinary 六jet与全部新增一阶列

普通几何必须用 (17) 的完整非线性 $T$，以及

$$
\begin{aligned}
X_s&=a'\Pi T+a\Pi T_s+\widetilde b e_z,\\
X_{ss}&=a''\Pi T+2a'\Pi T_s+a\Pi T_{ss}+\widetilde b_s e_z,\\
X_\theta&=aT,\quad
X_{s\theta}=a'T+aT_s,\quad
X_{\theta\theta}=aT_\theta.
\end{aligned}
\tag{19}
$$

没有省略 $a'\Pi T,a''\Pi T,2a'\Pi T_s$ 或高度项。全 fixed-body metric 在这些系数中原样保留。

下面给无需九次 finite difference 的完整参数导数。把 $T$ 看作
$T(\psi,v)$，下标 $i,j,k\in\{1,2\}$ 对这两个变量求导。记
$Y=(\psi,v)$；任一新列的变化为
$\dot Y=(\dot u,\dot v)$，由 (14)、(16) 直接给出。
对径向和角向分别有

$$
\begin{aligned}
\dot T&=T_i\dot Y_i,\\
\dot T_s&=T_i\dot Y_{i,s}+T_{ij}Y_{j,s}\dot Y_i,\\
\dot T_{ss}&=T_i\dot Y_{i,ss}
 +2T_{ij}Y_{j,s}\dot Y_{i,s}
 +\{T_{ij}Y_{j,ss}+T_{ijk}Y_{j,s}Y_{k,s}\}\dot Y_i,\\
\dot T_\theta&=T_i\dot Y_{i,\theta}+T_{ij}Y_{j,\theta}\dot Y_i,
\qquad Y_\theta=(1+\widetilde u_\theta,\widetilde v_\theta).
\end{aligned}
\tag{20}
$$

所有 $T$ 导数都在当前完整新场求值。可直接用原
`complete_tangent_parameter_jets` 的同一链式法则，也可由下表实现。
令 $N=(\cos\psi,\sin\psi,0)$、$d=vc$，则

$$
\begin{array}{lll}
T_1=-cN,&T_2=c'H+d'e_z,\\
T_{11}=-cH,&T_{12}=-c'N,&T_{22}=c''H+d''e_z,\\
T_{111}=cN,&T_{112}=-c'H,&T_{122}=-c''N,\quad
T_{222}=c'''H+d'''e_z,
\end{array}
\tag{21}
$$

其中这里只对 $v$ 求导，

$$
\begin{gathered}
c'=-vc^3,\quad c''=(2v^2-1)c^5,\quad
c'''=3v(3-2v^2)c^7,\\
d'=c^3,\quad d''=-3vc^5,\quad
d'''=3(4v^2-1)c^7.
\end{gathered}
$$

完整位置列为

$$
\begin{aligned}
\dot X&=a\Pi\dot T+\dot z e_z,\\
\dot X_s&=a'\Pi\dot T+a\Pi\dot T_s+\dot b e_z,\\
\dot X_{ss}&=a''\Pi\dot T+2a'\Pi\dot T_s+a\Pi\dot T_{ss}+\dot b_s e_z,\\
\dot X_\theta&=a\dot T,\quad
\dot X_{s\theta}=a'\dot T+a\dot T_s,\quad
\dot X_{\theta\theta}=a\dot T_\theta.
\end{aligned}
\tag{22}
$$

高度列准确是 $\dot z=\ell P_8,\dot b=P_8',\dot b_s=P_8''/\ell$，所有 $\dot T$ 为零；八个角场列的高度变化为零。

例如原直接 metric 变量 $e=|X_s|^2-1$、$f=X_s\cdot T$ 的新列是

$$
\dot e=2X_s\cdot\dot X_s,\qquad
\dot f=T\cdot\dot X_s+X_s\cdot\dot T.
\tag{23}
$$

对全部曲率行必须继续用实际第一、第二基本形式。在 $J=|X_s\times X_\theta|>0$ 处，

$$
\dot n=\frac{(I-nn^\top)
 (\dot X_s\times X_\theta+X_s\times\dot X_\theta)}J,\qquad
\dot{II}_{ab}=\dot n\cdot X_{ab}+n\cdot\dot X_{ab}.
\tag{24}
$$

配完整 $\dot I$ 给原曲率谱/半正定行的导数，不冻结法向或把目标 g 代替实际 I。球、条带、镜像法弦及其他实际门也使用同一 (22)，不只观察 metric 的 leading。

## 6. 真支持、正则性与严格新增性

$P_5$ 在入口为 $C^4$，$P_8$ 为 $C^7$；新增高度速度 $P_8'$ 为 $C^6$。它们在右端都平坦。故所有位置二jet在 $s=s_c,s_f$ 连续，原开核心和整个开尾帽的六jet准确保持。原中心锚及帽高也准确保持，因为新增高度原函数在两端都为零。

这些结论对任意有限新参数成立，不只线性化。包含 body 内点的跨区域法弦可能改变，不能据支撑保外部便继承整体 reach。新参数过大也可能破正则性、度量、形状或原 guard；没有预授任何系数盒。

新九列严格不在旧159列的函数像中。证明只需原最后一个五次结点片
$(153/200,423/500)$：原入口权在此为1，单Q列已经为零，旧 $u/v$ 变化和旧高度速度变化均为径向五次多项式，角系数或五高度线性组合保持原定义。

若一个旧列组合等于新增 $P_5 A(\theta)$，则右端全部径向导数的极限为零。该五次多项式的六个端jet均为零，因而在整个末片为零。$P_5>0$ 于内部，所以 $A=0$；四个 $\sin(2j\theta)$ 的准确线性独立迫四个 $\alpha_j=0$。$P_8$ 的同一论证给全部 $\beta_j=0$。若旧高度速度等于 $\gamma P_8'$，同理该旧多项式先为零，而 $P_8'$ 不恒零，故 $\gamma=0$。

这不仅是 scalar 标签的区别。若新位置的一阶列落旧位置列像，先对角求导得 $a\dot T=0$。有限 $v$ 下 $T_1,T_2$ 处处独立，迫 $\dot u=\dot v=0$；上述论证消去八个新系数，剩下 $\dot z=0$ 再消高度系数。因此新物理一阶函数像相对旧像严格增加九维。它不等于某个有限采样矩阵的数值 rank，也不证明这些列对当前最大行给出下降。

与旧34列的关系准确：旧34列保 $s\le.198$ 和 $s\ge.765$ 的全部六jet；本族作用于整个 $(.036,.846)$，可改变旧34列根本触不到的入口及临尾 body，同时在真正接口保二jet和帽高。本文没有重算旧34或旧103列的秩。

## 7. 新身份与下一模型的可复用边界

新完整身份至少记录：

1. 原 fixed-g 和 fixed-$b_0$ 身份、永久 enriched reference 与原159到163坐标定义；
2. 原159字段族和所有固定自然帽/入口/单Q定义；
3. (13) 的完整分段、$s_c,s_f$ 准确有理数，角列顺序 $\sin2\theta,\ldots,\sin8\theta$；
4. 新状态顺序 $(q_{0:159},\alpha_{1:4},\beta_{1:4},\gamma)$ 及精确系数字符串；
5. 新零列嵌入、唯一高度原函数 (14) 和全角 $\Pi$ 规则。

这个 identity 属于168维新族，不能沿用原163/159族的 objective/model/方向缓存身份。零新增点的**物理场**等于选定原点，不意味着旧有限问题已经包含九个新梯度。

若下一实际从某个已完成的54或更新接受点启动，应先唯一确定那个原点及其原 ordinary/J 收据。在新增系数为零处，旧159个 ordinary/J 列可以按完全相同基线消费；新成本只是 (16)、(20)–(24) 的九列及必须新增的原完整约束模型。若原缓存缺少所需真实二jet，则必须如实计必要恢复，不能假设缓存存在。第一次非零新步后全部场/旧列也随当前 $T$ 改变，须按原完整门重建，不永久沿用零新增点的旧 Jacobian。

未来源码应保零新增分支直接返回原物理评价，以免用新的加零顺序声称与已付 binary64 缓存逐位相同。本文尚未实现该 adapter、选择新参数盒、运行任何行或修改既有实际任务。下一阶段目标仍为 README 的完整 metric/reach/连续门；$.26$ 与约58仅是已有阶段指标。

## 8. 准确来源与范围

- [R55](R55-saturated-heat-third-Cauchy-jet-analytic-space-obstruction.md) 的有限表示障碍不授一般 $C^2$ 不可能，也不自动适用于直接 metric 的全部表示。
- [R63](R63-horizontal-angular-tangent-C2-strip-classification.md) 要求非圆到圆的准确连接保真正空间角场；本族保全部旧 $v$ 并增加四个空间方向。
- [R64](R64-convex-core-entry-seventh-tangent-and-sixth-center-jets.md) 与
  [原成套设计](../notes/elliptic-entry-paired-base-repair-design-20261114.md)
  给已知 $u_4/v_7/b_6$；当前权重和单Q已实际存在，本文没有把这些旧 leading 再计为新列。
- [现有34列完整局域证明](../notes/same-g-body-tangent-columns-and-locality-20261115.md)
  给原逐圈重构及末片结构；本文的平坦末端全body九列和零高度 primitive 是新的具体嵌套定义。
- 原源码：
  `scripts/frame_body_metric_design.py`、
  `scripts/cosine_connector_radial_seed.py`、
  `scripts/frame_entry_paired_repair.py`、
  `scripts/frame_entry_single_q.py`、
  `scripts/frame_direct_reference_geometry159.py`、
  `scripts/frame_five_height_field.py`。

新结论是 (11) 的全域固定-g Gaussian 上界，以及 (13)–(24) 的九个完整、独立、零暖嵌入方向。没有给出准确等距实现、可行优化步、曲率降至主门、非局部 reach 或完整闭面族。所有这些原任务继续保留。
