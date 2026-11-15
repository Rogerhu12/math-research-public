# R352：共享校准恒等式、全九控制合并与完整 Bernstein 目标包围

维护：ChatGPT /root/exact_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-15。

本结果为 [R326](R326-common-coordinate-target-enclosures-and-same-field-metric-transfer.md) 的准确公共坐标目标提供一个独立的依赖收窄方法。它保留同一准确长度、全部准确分片、三个支撑上的九个系数及全部闭端点；不改变目标族、数值参考的字面常数或任何 native/BVP 接受条件。它不是对 R330 中心差公式的重复证明，也没有本地数值计算或已通过工作宽度的声明。

## 352.1 来源、对象与成立条件

本证明对应以下已发表源码：

- 原消费者 root_20261115_continuous_nine_target_enclosures.py，69431 B，SHA-256 6dfb79be9b77e85ffff496e4349b9c6b01c1ab74f28d0a64bf76d4dc8cadb768；
- 原准确 factory geometry_20261115_continuous_nine_scalar_factory_v3.py，42270 B，SHA-256 0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e；
- 原字面数值编译 geometry_20261115_continuous_nine_scalar_numeric_v3.py，SHA-256 7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60；
- R326 与 [R330](R330-centred-common-coordinate-difference-and-target-coefficient-bounds.md) 的同一公共坐标、全部可能分支和参考解释。

实际消费者的 CompleteTarget.accurate、controls、literal、evaluate 是本次明确改进的作用点。这里不把这些源码之外的 scalar/profile 改标签接入。

固定原准确 core、cut、recipe、九个准确系数及其语义叶联合值 e。设真实联合值属于来源绑定的有限闭盒。盒的独立坐标放宽可以包含不对应真实尾根的点；本证明只要求包含真实联合值，不宣称每个盒点都实际可实现。原准确构造条件、正宽度和同一 core 的准确接缝责任仍按 R300/R323/R326 保持。

沿原 factory 记：

- R 为准确 cut 半径，r_A、v_A、b_A 为准确 core 末端二 jet；
- κ 为显式正 coast 速度的绝对值，δ 为 cut collar 宽度；
- a 为 first transition 宽度，β 为 last transition 宽度；
- v、b、q 为准确 cut 的一、二、三阶半径导数；
- c 为准确 core 的弧长末端。

这些正宽度均与原 recipe 同一对象。v、b、q 可以依赖语义叶；不能换成区间中点。原构造写为

$$
\begin{aligned}
r_B&=R-v\delta+\frac{b\delta^2}{2}-\frac{q\delta^3}{6},\\
v_B&=v-b\delta+\frac{q\delta^2}{2},\qquad b_B=b-q\delta,\\
I_A&=\frac{a(v_A-\kappa)}2+\frac{a^2b_A}{12},\\
I_B&=\frac{\beta(-\kappa+v_B)}2-\frac{\beta^2b_B}{12},\\
C&=\frac{r_A-r_B+I_A+I_B}{\kappa}>0,\\
S_1&=c+a,\quad S_2=S_1+C,\quad S_3=S_2+\beta,\quad L=S_3+\delta.
\end{aligned}
\tag{352.1}
$$

C 在本节只表示 coast 长度，不是连续尾模型的名称。公共坐标始终为 u∈[0,1]，准确物理位置 s=Lu。准确目标仍是

$$
L^2\,du^2+a_p(Lu)^2\,d\theta^2.
$$

所有后述重写都对每个固定真实 e 成立；区间扩展只能在重写后进行，不能把同名区间端点当作同一个真实值作非法相消。

## 352.2 准确 collar 的 cut 中心形式

原最后一段在 s∈[S_3,L] 上，以 t=(s-S_3)/δ 写成

$$
r_B+\delta v_Bt+\frac{\delta^2b_B}{2}t^2+\frac{\delta^3q}{6}t^3.
$$

令

$$
z=s-L=L(u-1).
$$

则同一准确多项式及其真实 s 导数恰为

$$
\begin{aligned}
a_{\rm base}(Lu)&=R+vz+\frac b2z^2+\frac q6z^3,\\
(a_{\rm base})_s(Lu)&=v+bz+\frac q2z^2,\\
(a_{\rm base})_{ss}(Lu)&=b+qz.
\end{aligned}
\tag{352.2}
$$

证明：由 L=S_3+δ 得 z=δ(t-1)。把式 (352.1) 的 r_B、v_B、b_B 代入原多项式并按 z 展开，常数项为 R，三个非零次数系数依次为 v、b/2、q/6。对同一准确多项式求导即得其余两式。

这一步消除的是原 DAG 中的准确共享量依赖。原区间表达式

$$
([L]U-[S_3])/[\,\delta\,]
$$

把 L 与 S_3 的相关性放宽，即使 U={1} 也未必得到单点 t=1；新表达式 [L](U-1) 在该端点准确为零。因此准确末端半径直接为 R，一、二阶导数分别为 v、b。此结论不需要收窄语义叶盒。

这里没有删除九控制：三个真实支撑分别严格位于 core 内、[c,S_1]、[S_1,S_2]。因为 β>0，collar [S_3,L] 与它们的内部不交。该段所有准确控制确实为零，范围来自原支撑身份；其他段仍完整保留九项。数值参考的字面支撑须独立判断，不能仅凭此真目标事实删除数值项。

## 352.3 coast 和最后 transition 的同对象形式

### coast

原 coast 在 s∈[S_1,S_2] 上为

$$
r_A+I_A-\kappa C\,\frac{s-S_1}{C}.
$$

因为 C>0，准确恒等式给出

$$
a_{\rm base}(Lu)=r_A+I_A-\kappa(Lu-S_1),\quad
(a_{\rm base})_s=-\kappa,\quad
(a_{\rm base})_{ss}=0.
\tag{352.3}
$$

先在准确代数中消去 C，再做向外求值，避免用两个独立的 [C] 同时相乘和相除。式 (352.3) 只描述基底；coast 上第三支撑的三个非零系数必须照式 (352.6) 加回，不能把完整 a_s 错写成 −κ。

### last transition

令

$$
r=\frac{S_3-s}{\beta}=\frac{-L(u-1)-\delta}{\beta}\in[0,1],
$$

并定义

$$
H_2=-3(\kappa+v_B)+2\beta b_B,\qquad
H_3=2(\kappa+v_B)-\beta b_B.
$$

原 last transition 的速度及半径可写成

$$
\begin{aligned}
V(r)&=v_B-\beta b_Br+H_2r^2+H_3r^3,\\
a_{\rm base}(Lu)&=r_B-\beta\left(v_Br-\frac{\beta b_B}{2}r^2+
                                      \frac{H_2}{3}r^3+\frac{H_3}{4}r^4\right),\\
(a_{\rm base})_s&=V(r),\\
(a_{\rm base})_{ss}&=-V'(r)/\beta.
\end{aligned}
\tag{352.4}
$$

证明：原 factory 的左端坐标 t=(s-S_2)/β 有 r=1-t。将原速度
−κ+(3κ+3v_B−βb_B)t²+(−2κ−2v_B+βb_B)t³ 代入 t=1-r，逐次幂收集即得 V。由 ds=−β dr，以右端半径 r_B 积分得式 (352.4)。其左端积分为 I_B，且 (352.1) 给 r_A+I_A−κC=r_B−I_B，故与原左端公式完全相同，不是另设一个边界值问题。

core 与 first transition 的原多项式、实际 local_interval 和准确 core 接缝均保持。需要时它们也可只作准确多项式换元；没有理由丢弃一个 core piece。

总长度还可准确写成

$$
\begin{aligned}
L={}&S_1+\frac{\beta}{2}+\delta+\frac{r_A-R+I_A}{\kappa}\\
&+\frac{\delta+\beta/2}{\kappa}v
-\frac{\delta^2/2+\beta\delta/2+\beta^2/12}{\kappa}b\\
&+\frac{\delta^3/6+\beta\delta^2/4+\beta^2\delta/12}{\kappa}q .
\end{aligned}
\tag{352.5}
$$

这是把 (352.1) 完全代入后的恒等式，可提供另一份 [L] 包围。它仍使用同一 v、b、q，不能宣称消除了它们对同一 E0/E1/E2 的全部依赖。与原合法 [L] 取交集是允许的；空交集是来源、公式或实现错误，不能当作目标域被反证。

## 352.4 三个支撑内先准确合并全部九项

以 i=0,1,2 编号三个支撑 [l_i,l_i+w_i]，w_i>0。原九参数按
[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3] 排列，记为 p_0,…,p_8。

原 factory 的三个 bump 为
ψ_k(x)=64x³(1-x)³(2x−1)^k，k=0,1,2。对每个支撑先构造一个准确多项式

$$
\Psi_i(x)=64x^3(1-x)^3
 \left(p_i+p_{3+i}(2x-1)+p_{6+i}(2x-1)^2\right).
\tag{352.6}
$$

其次数至多为八，且全部九个系数都出现。若
x=(s-l_i)/w_i∈[0,1]，该支撑对 (a,a_s,a_ss) 的贡献恰为

$$
\left(w_i^2\Psi_i(x),\quad w_i\Psi_i'(x),\quad\Psi_i''(x)\right);
\tag{352.7}
$$

支撑外三项均为零。式 (352.7) 由有限多项式的分配律及链式法则得到。边界的三重零因子保证到二阶的零 jet，故同一个闭端点可同时属于支撑内外分支而数值一致。

这与原分别计算三项后区间相加不同：先在准确系数中保留同一 x 的代数抵消，再求区间像。原 IEEE 程序的逐次加法顺序没有被宣称为逐字等价；这里的对象是原准确表达式和 R330 已声明的字面常数实参考。

原 recipe 保第一支撑严格位于 core 内，第二支撑是 [c,S_1]，第三支撑是 [S_1,S_2]。因而不同支撑的内部不交。实现可以利用这一准确顺序，枚举“无支撑/支撑0/支撑1/支撑2”并对可能分支取 hull，避免把一个宽查询同时落在几个互斥内部的区间贡献相加。若选择不利用此顺序，保留三个完整贡献的和仍是合法但可能更宽的包围。不得以浮点中点判定某个真实支撑不存在。

## 352.5 所有可能分支与共同多项式变量

固定一个原字面 lookup 的闭片 U⊂[0,1]。实际原419片及相邻片的两个闭端点均须保留。

对每个准确 piece i，仍先用

$$
T_i=\left(([L]U-[A_i])/[W_i]\right)\cap I_i
$$

作合法的可能性测试，保原 I_i，包括非 [0,1] 的 core local interval。只有已经证明 T_i 为空才可删该 piece。新公式不能改变这一完整分支责任。

对每个保留 piece，再枚举所有可能的真实支撑分支和字面参考支撑分支。一个分支的实际可行公共坐标集合可以是复杂集合；实现只需给其闭外包 B⊂U，并证明没有丢掉该分支的真实点。例如可将 U 与 ([A_i]+[W_i]I_i)/[L]、相应支撑端点除以正 [L] 的合法外包取交。无法缩小某个分支时保留整个 U 是安全选择。支撑外分支亦须保全；不允许只保“inside”交集而丢掉 outside-zero 可能。

在非退化 B=[u_0,u_1] 上令

$$
u=u_0+(u_1-u_0)x,\qquad 0\le x\le1.
$$

对每个固定真实叶选择和固定分支，所有基底形式 (352.2)–(352.4) 及原 core/first-transition 公式都是 x 的有限多项式，系数可以依赖语义叶；控制式 (352.7) 同样如此。先按同一个 x 加上当前所有真实贡献，再形成 a、a_s、a_ss 的系数盒。次数均有限且不超过八；低次数项可准确补零以统一次数。

这里的 a_s、a_ss 从原物理位置 s 的公式形成。若实现改为先求 u 导数，必须按正真实 L 除回；不能把 Bernstein 自变量 x 的导数直接当作 a_s。公共 u 导数继续按 L a_s、L²a_ss 形成。

单点 B 不必除以 u_1-u_0：直接用该准确 u 的合法区间扩展即可。多个可能分支可以重叠；最终 hull 保留它们的全部实际值。

## 352.6 完整向外 Bernstein 包围

设某个完整分支上的准确多项式为

$$
P(x)=\sum_{k=0}^n c_kx^k,\qquad c_k\in[c_k],\quad x\in[0,1].
$$

对 j=0,…,n 形成向外区间

$$
[b_j]\supseteq\sum_{k=0}^j
 \frac{\binom jk}{\binom nk}[c_k].
\tag{352.8}
$$

则

$$
P([0,1])\subseteq
\left[\min_{0\le j\le n}\underline b_j,\ 
      \max_{0\le j\le n}\overline b_j\right].
\tag{352.9}
$$

证明：准确恒等式
x^k=Σ_{j=k}^n binom(j,k)/binom(n,k)·binom(n,j)x^j(1-x)^{n-j}
给出 P 的 Bernstein 表示。各 Bernstein 基函数非负且和为一；对每个真实系数向量，准确 b_j 被 (352.8) 包含，P(x) 是这些准确 b_j 的凸组合，所以 (352.9) 成立。区间系数之间的依赖被放宽只扩大包围。n=0 时直接用 [c_0]。

该变换使用所有 n+1 个系数，不能按只选若干节点、只看端点或删除“不重要”高次项代替。需要细分时，de Casteljau 的每次凸组合亦可向外完成；它细分同一个完整多项式，没有重新选择科学参数。

把此结论分别用于 a、a_s、a_ss 和下节的差多项式，再对全部可能分支取 hull，得到完整包围。可以与原天然 Horner 包围及 R330 包围取交。交后不会比被保留的原包围更宽，但本证明不承诺每个具体区间都严格收窄或最终达到某个工作目标。

若采用原320位整数网格，每个非准确乘、除和有理系数转换都须向外取整。原 factory 的256位 sqrt 区间及准确有理输入只能被包含，不能在换表示时缩进。所有整数舍入误差属于系数盒的一部分；这是有理闭区间包含，不是浮点采样。

## 352.7 字面参考须保全部校准缺陷

数值参考 N_j 仍按 R330 定义：实际 numeric compilation 的每个 binary64 字为准确 dyadic 常数，使用实际 lookup partition、自己的 anchor、width、系数和三个 left/stored_width。不重新运行 IEEE 算术，不以另外的末点替换支撑准确右端 left+stored_width。

帽号表示这些独立字面量。通常不能断言

$$
\ell=\widehat S_3+\widehat\delta .
$$

必须保留准确 dyadic 缺陷

$$
\varepsilon_{L3}=\ell-\widehat S_3-\widehat\delta .
$$

因此数值 collar 的准确局部位置为

$$
\widehat t
 =1+\frac{\ell(u-1)+\varepsilon_{L3}}{\widehat\delta},
\tag{352.10}
$$

而不是把 ε_L3 默置零。即使其底层系数在数学设计上来自校准，已经存储的各个系数字也只能按它们的实际值解释。

若数值片为 Σ_{k=0}^n ĉ_k t^k，可在准确有理数中改写为

$$
N_{j,\rm base}(u)=\sum_{j'=0}^n
 \widehat d_{j'}\bigl(\ell(u-1)+\varepsilon_{L3}\bigr)^{j'},
\quad
\widehat d_{j'}=\widehat\delta^{-j'}
 \sum_{k=j'}^n \binom{k}{j'}\widehat c_k .
\tag{352.11}
$$

这是字面多项式自身的换元；不能把其常数或导数系数覆盖成 R、v、b、q。同样，数值 coast 的实际 slope 是其字面一次系数除以自己的字面 width，不可自动写成 −κ。其他数值分片也只可准确重组自己的全部系数。

数值支撑上的三项可以按 (352.6) 合并，但须使用数值自己的 left、stored_width。若多个字面支撑的区间因舍入不满足准确支撑的互斥顺序，须保所有实际同时激活的组合；不可把准确对象的支撑互斥结论擅移到 N。

每个数值片继续在其实际闭 lookup 范围使用未截断的 local variable。相邻片若有字面 jet 缺陷，双方的闭值都保留，不能用准确 C² 接缝将其拼平。

## 352.8 在共同变量中先形成差，再求区间像

对一个完整的“数值片、准确片、准确支撑分支、数值支撑分支”组合，以同一个 x 写出 N_j 与准确 A_e(u)=a_p(L_eu)。将对应多项式系数先相减，形成

$$
D(x)=N_j(u(x))-A_e(u(x)).
\tag{352.12}
$$

数值系数为准确有理数，准确目标系数为合法外包；每个差系数向外形成。式 (352.9) 因而给出这个完整分支上的差值包含。这里不能分别用各自独立的 x 或把两个不同 u 处的值相减。

这保留共同变量中的多项式抵消，尤其避免先把一个大半径范围与另一个大半径范围独立相减。每个真实 u 至少属于一个被保留的组合，故对所有组合的差界取 hull 是全 U 的合法差界。可再与原 R330 的中心差和独立直接差取交；空交集依然是工程或来源错误，不是数学域拒绝。

准确半径正下界、原 |a_s|<1、字面参考半径正性、比较工作目标和完整覆盖仍是分别记录的判断。若准确半径下界 a_->0，原 R330 的
ρ=maxabs[D]/a_-、δ_angular=2ρ+ρ² 可以继续使用。径向仍按同一准确 L 与字面 ℓ 的完整正区间计算，不以任何重新标定长度代换。

## 352.9 包围层级、可消除与不可凭空消除的宽度

这个方法针对三个确切源码层级：

1. 同一准确校准变量在不同 DAG 节点出现后被独立区间化；(352.2)–(352.5) 先消去其准确重复关系。
2. 同一支撑的三个 bump、基底与控制对同一位置的贡献分别求区间再相加；(352.6)–(352.9) 先合成完整多项式。
3. 数值参考与准确目标分别求大范围再相减；(352.12) 在共同自变量内先形成差系数。

它不自动消除 E0、E1、E2 盒的真实宽度或其未表达的联合约束，也不把存储字面误差归零。若同一语义盒给出的 [L] 仍固定，则径向比较项不随 u 二分改变。若某个单点上的校准后系数盒仍宽，更多 u 节点也不能缩小那份既定系数盒。

这样的算法限制不是真实目标误差下界：给定盒可能含未实现的叶组合，天然区间也可能仍有依赖放宽。需要区分“改进同一盒的表达式传播”与“从真正的连续 C/cut 生产器重新取得更窄且绑定相同对象的联合包围”。后者必须实际重算上游，不能改窄已存端点或把一份有限盒当作任意可精化实数名字。

实际163原记录应决定哪一层值得计算：完整叶中的 possible pieces/supports、a/as、d0/d1、径向项及未决原因都可定位责任；本证明没有预填这些数值、主因或新运行预算。

## 352.10 完整消费者和未付范围

独立实现可复用151的原来源重建、逐字段 definition 比对、原419闭片计划和“两个子叶完成前保父叶”的完整覆盖事务，只替换上述区间表达式与差多项式形成。它须保：

- 同一准确 core、实际 C/cut、原 recipe、全部九参数、完整 DAG 和原字面编译身份；
- 每个准确 piece 的真实 local_interval、所有支撑 inside/outside 组合、数值两侧闭端点；
- 完整向外系数与 Bernstein 包围，严格域反证和仅过宽未决的区别；
- 已覆盖范围、未访问范围、当前事务、全部未决原因和资源停止状态；
- 原 R326/R330 的准确目标、完整公共材料角合同变换及同场误差转移责任。

可先保原粗覆盖，再用新的包围在同一范围实际收窄；不得删除尚未通过的区间后宣称全域成功。1/10000000 仍仅是原工作宽目标，不是新增 native 门。没有实际运行就不能声称获得任何 δ、准确域证书、非零场、完整尾帽、强 C²、嵌入、reach、held、直径或冻结后精化。

本结果已经证明的是：在上述完整输入和分支条件下，校准正规形式、全九项合并、完整向外 Bernstein 及共同变量差多项式都包含原准确对象；数值字面校准缺陷也被显式保留。其实际收窄程度和计算资源必须由独立公开 Actions 记录决定。
