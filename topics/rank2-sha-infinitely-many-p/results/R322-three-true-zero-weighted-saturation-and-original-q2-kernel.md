# R322：三个真零来源的全次数整饱和与原三块联合核

日期：2026-11-13。**状态：全部已证明。原权 $(1,3,4)$ 幂格在所有 $p\nmid42b$ 处向实际归一化的嵌入逐次 $p$-饱和；原 $q=2$ 三整数块、首次核及模 $p^2$ 提升障碍均给出准确公式。没有将归一化免费加入原来源，也没有从缩放中央零推出乘积中央零。**

## 1. 三个实际来源及固定有理参数

固定 $b=17$，沿用 R297 的原 $S(z)=z^6+\cdots$，以及 R314、R319 的完整同源规范。置
$$
A=7bS(z),\qquad B=7bS(\delta z),\qquad C=7bS(2z),
\qquad \delta^2=-3,\qquad\deg(A,B,C)=(1,3,4).
\tag{1}
$$
这些次数记录真实 theta charge 与34之比。相对于 R325 的三个生成元，(1) 仅各乘同一个固定单位 $7b$。令
$$
t=-b/x^3,\qquad \rho=\Theta^{17}(1+8t),\qquad
a=t(t-1)h_7,\quad h_7=16t^2+4t+7,\quad g_2=8t^2+20t-1.
$$
定义四个明确多项式
$$
\begin{aligned}
f_4&=512t^4-2048t^3+1344t^2-536t-1,\\
f_6&=4096t^6-33792t^5+204288t^4-47936t^3+11040t^2+84t+1,\\
f_3^\delta&=64t^3-48t^2+228t-1,\\
f_4^\delta&=1792t^4-3136t^3+2112t^2-40t+1.
\end{aligned}
\tag{2}
$$
原 carrier 全部包含在以下式子中：
$$
\boxed{A=\rho a(t),\quad B=\rho^3\beta(t),\quad C=\rho^4\gamma(t),}
\tag{3}
$$
其中
$$
\begin{aligned}
\beta&=\frac{27t(t-1)(4t-1)^2h_7f_3^\delta f_4^\delta}{1+8t},\\
\gamma&=\frac{-64t(t-1)^3h_7g_2^2f_4f_6}{(1+8t)^2}.
\end{aligned}
\tag{4}
$$
证明只需将 R314 的
$\tau_2=64t(1-t)^3/(1+8t)^3$、
$\mathcal R_2=(1+8t)^{10}((1+8t)^3+512t(1-t)^3)$，以及 R319 的
$\tau_\delta=-27t/(1-4t)^3$、
$\mathcal R_\delta=(1-4t)^{14}((1-4t)^3-216t)/(1+8t)^3$
代入 $\gamma=\mathcal R_2a(\tau_2)$、$\beta=\mathcal R_\delta a(\tau_\delta)$ 并约分。
这保留了原 sigma 同源因子，不是仅在原 $a(t)$ 中换参数。

两个实际角比为
$$
\boxed{
f=\frac{B}{A^3}=\frac{27(4t-1)^2f_3^\delta f_4^\delta}
 {t^2(t-1)^2(1+8t)h_7^2},\qquad
h=\frac{C}{A^4}=\frac{-64g_2^2f_4f_6}
 {t^3(t-1)(1+8t)^2h_7^3}.}
\tag{5}
$$
按所显示的整数分子、分母，准确 resultant 为
$$
\operatorname{Res}(n_h,d_h)=2^{288}3^{189}7,\qquad
\operatorname{Res}(n_f,d_f)=2^{90}3^{118}.
\tag{6}
$$
而有限极点支持多项式
$Q=t(t-1)(1+8t)h_7$ 满足
$$\operatorname{disc}(Q)=-2^{12}3^{19}7^2.\tag{7}$$
因此在任何特征不整除42的域上，(5) 的准确极阶仍为

| 位置 | $0$ | $\infty$ | $1$ | $-1/8$ | $h_7$ 的第一根 | $h_7$ 的第二根 |
|---|---:|---:|---:|---:|---:|---:|
| $h$ | 3 | 2 | 1 | 2 | 3 | 3 |
| $f$ | 2 | 0 | 2 | 1 | 2 | 2 |

两个映射的次数分别14、9，故对这样的任一域 $k$，
$$[k(t):k(f,h)]\mid\gcd(14,9)=1,\qquad k(f,h)=k(t).\tag{8}$$
这同时支付了特征零与所有好剩余特征的参数场；没有随次数变化的例外素数。

## 2. 原加权幂格在所有好素数处饱和

置 $R=\mathbf Z[1/(42b)]$。原幂格是 (3) 在分次函数域中的像
$$\mathcal T_R=R[A,B,C]\subset R(t)[A].$$
这里 $A$ 是次数一的分次参数；与实际 theta 截面代数的解释相同。
R325 已证明特征零的唯一关系 $F$ 的权为47。取其整系数 primitive 规范，则 Gauss 引理给
$$\boxed{\mathcal T_R=R[X,Y,Z]/(F),\qquad\deg(X,Y,Z)=(1,3,4).}\tag{9}$$

下面把原归一化写成每次都明确的整数格。记
$$
u_n=\left\lfloor\frac{3n}{4}\right\rfloor,\quad
v_n=\left\lfloor\frac n2\right\rfloor,\quad
c_n=\left\lfloor\frac{2n}{3}\right\rfloor,
$$
$$
T_n(t)=t^{u_n}(t-1)^{c_n}(1+8t)^{v_n}h_7^{u_n},\qquad
d_n=3u_n+2v_n+c_n.
$$
则
$$
\boxed{\mathcal N_{R,n}=
\frac{A^n}{T_n(t)}R[t]_{\le d_n},\qquad
\mathcal N_R=\bigoplus_{n\ge0}\mathcal N_{R,n}.}
\tag{10}
$$
它是 R325 的除子截面环在 $R$ 上的实际格。有限极点的总阶为
$3u_n+v_n+c_n$，另允许无穷处 $v_n$ 阶极，正好给分子次数 $d_n$。
各有限支持在 $R$ 上互不相交且 $h_7$ 不分歧，故 (10) 给一组自由 $R$ 基并与任意好剩余域的 base change 相容。

**定理1（全次数原格饱和）。** 对每个 $p\nmid42b$、每个次数 $n$，
$$
\boxed{\mathcal T_{R,n}/p\mathcal T_{R,n}
\longrightarrow\mathcal N_{R,n}/p\mathcal N_{R,n}
\text{ 单射}.}
\tag{11}
$$
从而
$$
\boxed{\mathcal N_R\cap\mathcal T_{\mathbf Q}=\mathcal T_R,\qquad
(\mathcal T_R:\mathcal N_R)
=\mathcal N_R\cap(\mathcal T_{\mathbf Q}:\mathcal N_{\mathbf Q}).}
\tag{12}
$$
交集均在同一原分次函数域中取。

**证明。** 由 (6)–(8)，在 $k=\mathbf F_p$ 上原三个生成元仍给完整参数场及同一极点表。逐点的最大极斜率仍是
$$
D=\tfrac34([0]+[r_+]+[r_-])+\tfrac12([\infty]+[-1/8])+\tfrac23[1].
$$
相应截面环的第 $n$ 次维数为 $d_n+1$。为核实它对原像有限，取同次数的三个截面 $A^{12},B^4,C^3$：在 $D$ 支撑以外第一项非零，在每个支撑点第二或第三项达到最大允许极阶。因此三者没有共同基点，截面环模它们生成的理想有限维，按次数提升有限基即得有限性。它与原像同分式域，所以两者 Hilbert 函数的线性主项相同，为 $47n/12$。

从三个变量到原像的核是高度一齐次素理想，故由一个加权齐次不可约多项式 $F_p$ 生成。若其权为 $e$，超曲面 Hilbert 级数的主项为 $en/12$，故 $e=47$。另一方面，primitive $F$ 模 $p$ 非零，仍齐次权47，并属于这个核。因此 $\bar F$ 与 $F_p$ 相差一个非零常数，原像核准确为 $(\bar F)$。结合 (9)、(10) 即得 (11)。

若 $x\in\mathcal N_R$ 且 $px\in\mathcal T_R$，(11) 先给 $px=py$、$y\in\mathcal T_R$；$\mathcal N_R$ 无 $p$-挠，故 $x=y$。逐个除去有理分母的所有非单位素因子，得到第一个交集等式。若 $x$ 落在 (12) 右端的第二个交集，则 $x\in\mathcal T_R$；对任意 $y\in\mathcal N_R$，有 $xy\in\mathcal N_R\cap\mathcal T_{\mathbf Q}$，仍由第一个等式得到 $xy\in\mathcal T_R$。反向包含显然。$\square$

特别，任何已经证明的有理导子，只要其实际分式属于 (10)，就已经是原整数导子，乘任意次数的 (10) 都返回原幂格。此结论没有新增随次数变化的坏素数。R326 的五个40次明确代表提供了可直接使用的构造，R329 给出全部最小导子生成元；本定理不把这些正次数乘子视为原点单位。

(11) 是**来源格向归一化的饱和**。下面的有限 Taylor 映射仍可以有非平凡 Smith 因子，二者不能混同。

## 3. 同一个物理 $q=2$ 目标及全部整数块

取
$$
p=6s-1>7,\quad p\ne17,\quad L=2s+\ell,\quad0\le\ell<s,\quad w=z^6.
$$
令 $c_p=[w^s]\log(\sigma/z)$、$\kappa=34c_p$、$a_p=p\kappa$。
R301 保证 $a_p\in\mathcal O^\times$。沿用 R309 的实际整轴
$$
g(w)=e^{-\kappa w^s}\rho(w)\pmod{w^L},\qquad
t(w)=-b x(z)^{-3}\pmod{w^L}.
\tag{13}
$$
它们全都整，$g(0)=1,t(w)=-bw+\cdots$。高轴整系数没有被任意低对数提升替换。
置
$$
\Gamma_L=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2),
\qquad e_2(v)=1+v+v^2/2.
\tag{14}
$$
对原 $\mathcal T_{R,\le D}$ 定义同一映射
$$
\boxed{\mathcal J(P)=P\left(
ga(t)e_2(a_p\epsilon),\quad
g^3\beta(t)e_2(3a_p\epsilon),\quad
g^4\gamma(t)e_2(4a_p\epsilon)\right).}
\tag{15}
$$
这里 $t=t(w)$；$1+8t$ 是同一目标中的整单位。原关系 $F$ 在 (15) 下准确为零，因而 (15) 是原商格上的映射。

令
$$
\mathcal E=X\partial_X+3Y\partial_Y+4Z\partial_Z,
\qquad W_i(P)=(\mathcal E^iP)(ga,g^3\beta,g^4\gamma).
$$
用普通系数移块算子 $\mathscr S(\sum h_rw^r)=\sum h_{r+s}w^r$。三块准确为
$$
\boxed{\begin{aligned}
J_0(P)&=[W_0]_{<s},\\
J_1(P)&=[a_pW_1+p\mathscr S W_0]_{<s},\\
J_2(P)&=[a_p^2W_2/2+pa_p\mathscr S W_1+p^2\mathscr S^2W_0]_{<\ell}.
\end{aligned}}
\tag{16}
$$
证明是按径向指数展开 $e_2$，再逐次使用 $w^s=p\epsilon$。特别第二块保留真实 $a_p$ 和第一块尾部，第三块保留两个不同来源的进位。所用 $2!$ 为单位；(13) 的所有指数计算只需次数 $L<p$。

缩放来源的物理首坏系数是 $34\alpha^{p+1}c_p$，公共 charge 系数是 $34\operatorname N(\alpha)c_p$；二者相差
$a_p(\alpha^{p+1}-\operatorname N(\alpha))/p$。R314、R319 已支付这一整修正，(3)、(13)、(15) 正是保留该修正的写法，不能将 $g(\alpha^6w)$ 直接替成 $g(w)^{\operatorname N\alpha}$。

## 4. 原首次核及真实下一位提升障碍

**定理2。** 原 (15) 的模 $p$ 核准确是
$$
\boxed{W_0(P)=W_1(P)=0\pmod{w^s},\qquad
W_2(P)=0\pmod{w^\ell}.}
\tag{17}
$$
全部等式在剩余域中读；$\ell=0$ 时最后一条为空。来源只取原权预算内的 $P$，并模掉已付的47次关系及其倍式。

对满足 (17) 的任意原整提升 $P_0$，先定义向量
$$
o(P_0)=\frac{\mathcal J(P_0)}p\bmod p\ \in\Gamma_L/p\Gamma_L.
\tag{18}
$$
真正的第一次提升障碍是这个向量在 $\operatorname{coker}(\bar{\mathcal J})$ 中的类。
使用 (16)，三个坐标分别由
$$
\boxed{\begin{aligned}
O_0&=[W_0/p]_{<s},\\
O_1&=[a_pW_1/p+\mathscr S W_0]_{<s},\\
O_2&=[a_p^2W_2/(2p)+a_p\mathscr S W_1+p\mathscr S^2W_0]_{<\ell}
\end{aligned}\pmod p}
\tag{19}
$$
给出。式中的除 $p$ 只作用于 (17) 已证明可除的相应低前缀，不能作用于任意高轴系数。
有
$$
\boxed{P_0+pP_1\in\ker(\mathcal J\bmod p^2)
\iff \bar{\mathcal J}(\bar P_1)=-o(P_0).}
\tag{20}
$$
所以提升存在当且仅当 (18) 的余核类为零。

**证明。** (17) 直接由 $a_p$ 与2为单位及 (16) 得到。更换提升 $P_0$ 为 $P_0+pQ$，(18) 改变 $\bar{\mathcal J}(\bar Q)$，故余核类与提升选择无关；线性展开给 (20)。这是同一个原来源格的完整模 $p^2$ 障碍，没有把三个中央权分别设置为零，也没有预先假定该障碍由一个二阶常系数算子产生。$\square$

这里的余核是目标除以原像，并非 $\mathcal N/\mathcal T$。为了准确比较，(15) 可延伸到 (10)：其中
$$\frac{a(t)^n}{T_n(t)}=
\frac{t^{n-u_n}(t-1)^{n-c_n}h_7^{n-u_n}}{(1+8t)^{v_n}}$$
在原点整，故同一三个整数块仍成立。记两个模 $p$ 像为 $I_T\subset I_N\subset\Gamma_L/p$，则有准确短正合列
$$0\longrightarrow I_N/I_T\longrightarrow
(\Gamma_L/p)/I_T\longrightarrow(\Gamma_L/p)/I_N\longrightarrow0.$$
整导子能返回 $I_N/I_T$ 所代表的额外来源；它不自动消掉最后一个真实有限像余核。后继必须证明 (18) 在这个最后余核中的分量为零，或另行计算其与导子相乘后的类。

## 5. 保留实际列的有限 Hermite–Padé 矩阵

这一步仅用共同目标单位清分母，不加入全角多项式来源。写
$\beta=\beta_0/(1+8t)$、$\gamma=\gamma_0/(1+8t)^2$，其中 $\beta_0,\gamma_0$ 是 (4) 的整数分子。对给定预算 $D$，置
$$
e_D=2\lfloor D/4\rfloor+\mathbf 1_{D\equiv3\ (4)}
=\max_{i+3j+4k\le D}(j+2k).
\tag{21}
$$
整个目标乘同一个单位 $(1+8t(w))^{e_D}$ 后，原单项式 $X^iY^jZ^k$ 的角列准确为
$$
\boxed{p_{ijk}(t)=a(t)^i\beta_0(t)^j\gamma_0(t)^k
\,(1+8t)^{e_D-j-2k},\quad m=i+3j+4k.}
\tag{22}
$$
其次数准确为 $4m+2k+e_D\le5D$。因此 (17) 是一个完全明确的有限 Hermite–Padé 系统：原系数 $c_{ijk}$ 满足
$$
\begin{aligned}
&\sum c_{ijk}\varrho(q)^m p_{ijk}(-bq)=0\pmod{q^s},\\
&\sum m c_{ijk}\varrho(q)^m p_{ijk}(-bq)=0\pmod{q^s},\\
&\sum m^2 c_{ijk}\varrho(q)^m p_{ijk}(-bq)=0\pmod{q^\ell},
\end{aligned}
\tag{23}
$$
其中现在 $q=x^{-3}$，而真实低轴为
$$
\varrho(q)=(1-8bq)\exp\left(
\sum_{1\le n<s}\frac{17}{3n}
\frac{(1/3)_n}{(5/6)_n}(-bq)^n\right)\pmod{q^s}.
\tag{24}
$$
式 (24) 沿用 R309 的真实低 theta 系数；首坏项从 $q^s$ 才开始。
在 (23) 中仅允许 (22) 的原列及原47次关系；不能用所有次数 $\le5D$ 的多项式替代这些列。

为避免把首次核换参用于更高精度，完整目标的角参数关系必须仍写为
$$w^s=q^s h_0(-bq)^{p+1},\qquad h_0(-bq)=z/\sqrt[6]{q}.\tag{25}$$
该因子的 $h_0^p$ 在模 $p^2$ 有真实下一位。故 (19)、(20) 仍以物理轴 (13)、(16) 为定义，不能仅从 (23) 删除 (25)。

## 6. 全部正次数原列的共同一次行移

每个正次数生成单项式在 $z=0$ 都至少零六阶。因此对原正次部分
$\mathcal T_{R,\le D}^+$，(15) 可以准确写成
$$\mathcal J(P)=w\,\widetilde{\mathcal J}(P),\tag{26}$$
其中 $\widetilde{\mathcal J}$ 通过普通系数先除去这个已知的 $w$，再进入长度 $L-1$ 的同一加权前缀格来定义。不是在零因子环中任意除以 $w$。
原列、charge 与 (16) 的全部进位保持不变。

若 $e_r=\lfloor r/s\rfloor$，这个目标映射的第 $r$ 行准确乘
$p^{e_{r+1}-e_r}$，并移至第 $r+1$ 行。只有
$$r=s-1,\ 2s-1\quad(0\le r<L-1)\tag{27}$$
可能各付一个 $p$。所以两矩阵的非零 Smith 因子截断和满足
$$
\boxed{0\le B_N(\mathcal J|_{\mathcal T^+})-
B_N(\widetilde{\mathcal J})
\le\lfloor(L-1)/s\rfloor\le2.}
\tag{28}
$$
这里 $B_N=\sum_j\min(N,v_p(d_j))$，求和只遍历非零 Smith 因子。
证明是 (26) 在特征零上单射，而两个整数目标格只相差 (27) 的有限指数。

这不是40次导子的全归一化块：它只使用所有原正次列共有的物理零。R326 的40次导子首阶为 $w^{13}$，其更大的行移不能用 (28) 代替。

还有一个原矩阵中的明确单位 minor。将 (1) 的三列分别除以
$7b,-189b,448b$，则三列都以 $w$ 开始，其径向权仍是 $1,3,4$。
若 $D\ge4$、$\ell\ge2$，读取三个块中 $w^1$ 的行，模 $p$ 得
$$
\begin{pmatrix}
1&1&1\\a_p&3a_p&4a_p\\a_p^2/2&9a_p^2/2&16a_p^2/2
\end{pmatrix},\qquad\det=3a_p^3\in\mathcal O^\times.
\tag{29}
$$
所以三个真实来源在同一原有限像中确实保留了三条径向方向。
这条局部 minor 不把完整中央观察变成一个二阶微分算子。

## 7. 与完整中央零的准确关系

在惰性规范中，两个缩放来源的完整函数满足
$$
J_{S(2z)}(u)=\lambda_2^uJ_S(u),\qquad
J_{S(\delta z)}(u)=\lambda_\delta^uJ_S(u),
$$
$$
\lambda_2=2^{p+1}/4=2^{p-1},\qquad
\lambda_\delta=\delta^{p+1}/3\in1+p\mathcal O.
\tag{30}
$$
这里分别采用真实 charge4及3；$\delta^p=-\delta$ 保证第二个同余。
由于 $S(0)=0$，原 $J'_S(0)=0$ 确实强迫三个完整中央导数同时为零。
普通测度的对应全 $p$-core、质量及尺度式已由 R314、R319 支付。

若 $J_S=\sum a_h(u)_h$，实际尺度后的 Newton 系数仍是
$$
a_h^{(\lambda)}=\sum_{i=0}^h
\lambda^i(\lambda-1)^{h-i}\frac{a_i}{(h-i)!}.
\tag{31}
$$
在 R301 已付的同一截断精度上，(31) 给与原来源相同的中央聚合条件，见 R314。
不能因为 (29) 的有限列独立，就把三个块的中央权分别置零。
同样，三个生成元的完整中央零没有给出其任意乘积的中央零。

本篇所得到的实际新输入是：原幂格在全部好素数处的全次数饱和，及无需任何环境来源的同一个原三块核和真实提升类 (18)。若要获得新的深 Smith 收益，须在 (19)、(20) 或完整高块中实际消掉该余核类；仅用缩放标量的数量不能完成这一步。

## 8. 固定精确证书

- [check-jzero-three-true-zero-weighted-q2.py](../scripts/check-jzero-three-true-zero-weighted-q2.py)
- [check-jzero-three-true-zero-weighted-q2.json](../scripts/check-jzero-three-true-zero-weighted-q2.json)

证书只核固定有理同源式、整数 resultant、原 pole 支持、三个整数块的形式恒等式、径向 minor及分母预算。所有素数、所有次数的饱和断言由第2节证明；没有目标素数扫描。

依赖：R297 原 $S$；R301 完整惰性轴和尾界；R309 原三块目标；R314、R319 真同源及全中央尺度；R325 原加权归一化；R326、R329 实际整导子与有限呈示。
