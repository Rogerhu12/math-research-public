# R683 — 全原十九角线性系的双 jet 满射与更低的短三块门

日期：2026-11-15。**状态：以下原实际像的统一充分范围已证明。主课题仍未完成。**

本篇把 R680 的准确 forcing 极帽用于整条真实弧的连续近点。
不限制 charge 的同余支持，直接在整个原 $\mathcal W_D$ 上证明两个长 jet 的满射。
原十九个角的固定余量足以容纳一个显示的 klt 边界；
由已核过假设的 ABL Lemma 2.10，得到同一原线性系的完整上同调消失。

再用真正的模十二来源乘子和原低行右逆返回旧三块。
对于 $1\le\ell\le3$，一个准确充分条件是
$$
D-17>
3\left\{\frac{48}{47}
+\sqrt{\left(\frac{48}{47}\right)^2+\frac{36(s-3)}{47}}\right\}.
$$
于是原 $J$ 整满射，完整 $M$ 仅有原二十六个 $p$ 因子及十三个自由目标方向。
渐近门为
$$
D>\left(\sqrt{\frac{54}{47}}+o(1)\right)\sqrt p
\approx1.072\sqrt p.
$$
这严格缩小 R637 约 $3.943\sqrt p$ 以下仍可能有双侧缺陷的窗口，
并非拿 full $C$ 的高 Smith 因子代替旧 $M$。
约 $0.413\sqrt p$ 的真实维数临界尚未覆盖；原指定 forcing 在该范围仍开。

## 1. 原来源、曲面和统一常数

保持
$$
p=6s-1>101,\qquad f_D=\lfloor9D/2\rfloor+4<p,
$$
以及 R672/R680 的同一
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\quad
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},
$$
$$
h_7=7+4t+16t^2,\quad d=1+8t,\quad
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
e_{n+1}=f_n-3A_n-B_n+C_n,\qquad
\mathcal E=Y\partial_Y.
\tag{1}
$$
目标轴仍是原 $g\equiv\rho=(1+8t)\Theta^{17}\pmod{t^s}$。
只在长度不超过 $s$ 内使用原 ODE。

用 R495/R555/R680 的十九角面 $X$ 和全来源类 $\mathcal B_D$：
$$
H^0(X,\mathcal O_X(\mathcal B_D))
=d^{C_D}\overline{\mathcal W}_D.
\tag{2}
$$
R680 已证 $\mathcal B_D$ nef。记其固定主类为
$$
B_\infty=S_0+5F_0
-\frac14\sum_{\text{三条四步链}}E_{\alpha,j}^*
-\frac13\sum_{\text{三步链}}E_{1,j}^*
-\frac12\sum_{\text{两条两步链}}E_{\alpha,j}^*,
\qquad
\beta=B_\infty^2=\frac{47}{12}.
\tag{3}
$$
所有例外符号在交数式中均为全变换；表示边界支撑时另明确使用严格变换。

$B_\infty$ 本身 nef：
它在六条固定严格纤维、严格 $S_0$ 及各非末例外上交数为零，
在末例外上分别为 $1/4,1/3,1/2$，
在一般纤维上为一，在严格正截面上为 $\beta$；
其余曲线由 R680 的原 Gauss 式给非负交数。
因 $\beta>0$，它也是 big。

若 $C$ 为非垂直、非两截面的几何整曲线，
取 primitive 方程 $F=\sum_{i=0}^b f_i(t)Y^i$，
$f_0\ne0$，置
$$
b=\deg_YF,\quad
u=\max_i(\deg f_i-4i),\quad
a=B_\infty C,\quad
\kappa=C^2,\quad\chi=-K_XC.
$$
R680 已付
$$
a\ge\beta b,\qquad \chi\ge2b,\qquad \kappa\ge0.
\tag{4}
$$
Hodge 指数定理给
$$
\boxed{\kappa\le a^2/\beta.}
\tag{5}
$$
另外，每条固定链的累计末重数都不超过 $b$。
有限负权角及 $d$ 角由 primitive 系数中的角单位得到；
无穷角则选达到 $u=\deg f_i-4i$ 的那一项，
其累计末值至多为该 $i\le b$。
所以
$$
\boxed{a\ge u+\frac{35}{12}b.}
\tag{6}
$$
这些是整个原曲面的曲线不等式，不涉及评价像的饱和猜测。

## 2. 原弧前 N 个近点的完整重数界

取 $1\le N\le s$，在未被十九次吹起触及的
$P=(0,1)$ 上，沿原轴 $Y=g(t)$ 依次吹起 $N$ 个自由近点。
记一条 $C$ 在这些点的严格变换重数为
$m_1,\ldots,m_N$；离开该链后置零。
写
$$
S_N(C)=\sum_i m_i,\qquad T_N(C)=\sum_i m_i^2.
$$

**引理 1（目标素数上的全曲线界）。** 对每条上述 $C$，准确有
$$
\boxed{
S_N(C)\le R_N\,a,\qquad
R_N=\frac{48}{47}
+\sqrt{\left(\frac{48}{47}\right)^2+\frac{36N}{47}}.}
\tag{7}
$$
该式包括 $b\ge p$ 的不可分情形，不只检低次数测试曲线。

**证明。** 先设 $b<p$ 且 $C$ 经过 $P$。
以 $z=Y-g_{<N}(t)$ 为局部坐标，
完整 Hensel 因子各 tame 根与原轴的接触为 $h_j$。
普通自由链的累计重数公式给
$$
S_N=\sum_j\min(h_j,N).
\tag{8}
$$
这也可由逐次代入 $z=tz_1$ 证明：
每一步提取的总 $t$ 阶恰为该中心的真实重数，
已离开的分支不再贡献。未读的 $g$ 尾不改变该簇。

令 $\Delta_C$ 为这个完整 Hensel 因子的判别式赋值。
它满足
$$
\Delta_C\ge2\delta_P(C)
\ge\sum_i m_i(m_i-1)=T_N-S_N.
\tag{9}
$$
第一项可直接从有限自由局部环看出：
其归一化为各 tame 分支 $k[[u_j]]$ 的直和，
迹配对的格指数贡献 $2\delta_P$，
归一化的不同理想贡献 $\sum_j(e_j-1)\ge0$。
第二项是每次普通吹起的准确亏格下降。
因此没有忽略切向分支的 different 或奇异点重数。

R680 的同一个 Euler 三次 forcing 给
$$
S_N+3\Delta_C\le3\kappa+L C\le3\kappa+8b.
\tag{10}
$$
这里使用 $\min(h_j,N)\le\min(h_j,s)$；
forcing 非零由 R467 的 tame 共振支付，不将方程延长过 $s$。
由 (9)–(10)，
$$
T_N\le S_N+\Delta_C\le3\kappa+8b
\le\frac3\beta a^2+\frac8\beta a.
\tag{11}
$$
不经过 $P$ 的曲线有 $S_N=T_N=0$，同式仍成立。

置
$$
d_0=3/\beta=36/47,\qquad c_0=8/\beta=96/47.
$$
整数重数给 $S_N\le T_N$，Cauchy 不等式给 $S_N^2\le NT_N$。
若 $R=S_N/a>c_0$，从
$R\le d_0a+c_0$ 得 $a\ge(R-c_0)/d_0$，再代入
$$
R^2\le N(d_0+c_0/a)
$$
便得 $R(R-c_0)\le Nd_0$。
若 $R\le c_0$，所需上界自动成立。
两种情况都给
$$
R\le\frac{c_0+\sqrt{c_0^2+4d_0N}}2=R_N.
$$

现在完整支付 $b\ge p$，不假设局部分裂 tame。
逐次亏格下降及 (4) 给
$$
T_N-S_N\le\kappa-\chi+2\le\kappa.
$$
故
$$
S_N^2\le N(\kappa+S_N)\le N(a^2/\beta+S_N),
$$
从而
$$
\frac{S_N}{a}
\le\sqrt{\frac N\beta}+\frac Na
\le\sqrt{\frac N\beta}+\frac N{\beta p}.
\tag{12}
$$
因 $N\le s<p$，最后第二项小于 $1/\beta$。
而
$$
R_N\ge\sqrt{3N/\beta}+4/\beta,
$$
所以 (12) 严格不超过 (7)。
该情形只用整曲线亏格，没有对被 $p$ 整除的导数首项作任何假设。证毕。

## 3. 原固定角的显示 klt 边界

本节在 $X$ 上先构造一个与 $D,N$ 无关的有理边界 $\Delta_0$。
所有下面的曲线均取在 $X$ 上的**严格变换**。
写 $F_0,F_{h_1},F_{h_2},F_1,F_d,F_\infty$ 为六条固定纤维，
$E_{\alpha,j}^{\rm str}$ 为严格例外。

置 $\varepsilon=1/192$，定义
$$
\begin{aligned}
\Delta_0={}&
\frac14 S_0^{\rm str}
+\frac56F_0+\frac1{12}(F_{h_1}+F_{h_2})
+\frac19F_1+\frac1{48}(F_d+F_\infty)\\
&+\frac16(E_{d,1}^{\rm str}+E_{\infty,1}^{\rm str})\\
&+\varepsilon
\sum_{\substack{\text{三条四步链及一条三步链}\\1\le j<e_\alpha}}
j(e_\alpha-j)E_{\alpha,j}^{\rm str}.
\end{aligned}
\tag{13}
$$
其支撑简单正规交叉，全部系数严格小于一。

**引理 2。** 对所有 $D\ge3$，
$$
A_0(D)=\mathcal B_D-K_X-\Delta_0
$$
满足
$$
\boxed{A_0(D)-(D-5)B_\infty\ \text{为 nef}.}
\tag{14}
$$
此外，$A_0(D)$ 在全部固定边界曲线上交数严格为正，且
$$
\boxed{A_0(D)F_0=37/12.}
\tag{15}
$$

**证明。** 对非边界曲线，R680 的准确重数表已给
$$
(\mathcal B_D-D B_\infty)C\ge23b/12.
$$
由 (4)，再加 $-K_XC\ge2b$。
严格纤维和严格例外与 $C$ 的交数均不超过 $b$；
严格 $S_0$ 的交数不超过 $u$。
(13) 中除 $S_0$ 外的系数总和为
$$
\frac{83}{72}+\frac13+\frac{17}{96}=\frac{479}{288}.
$$
因此由 (4)、(6)，
$$
\Delta_0C
\le\frac14u+\frac{479}{288}b
\le\left(\frac14+\frac{479}{1128}\right)a
=\frac{761}{1128}a<a.
$$
故
$$
A_0(D)C\ge(D-1)a+\frac{47}{12}b>(D-5)a.
\tag{16}
$$

固定边界必须另检，不能由 (16) 略去。
原重数表及严格曲线的自交给：

| 边界 | $A_0(D)$ 的交数 |
|---|---|
| 严格 $S_0$ | $1/18$ |
| $F_0$ | $37/12$ |
| $F_{h_1},F_{h_2},F_1$ | $1/12$ |
| $F_d,F_\infty$ | $D-2C_D+1/24$ |
| 四步、三步链的非末例外 | $\mu_j(D)-\mu_{j+1}(D)+2\varepsilon$ |
| 两步链的第一例外 | $1/12$ |

这些曲线上 $B_\infty$ 的交数均为零。
在四步链末例外上，按 $D\bmod4$ 直接代入原表，
$$
\{A_0(D)-(D-5)B_\infty\}E_{\alpha,4}^{\rm str}
\ge1-\frac56-3\varepsilon=\frac{29}{192}>0.
$$
其中 $F_0$ 的系数最大，其余两条更强。
三步链末例外的同一差至少
$5/3-1/9-2\varepsilon>0$。
两步链末例外至少 $45/16>0$。
严格正截面的同一差至少
$$
5\beta+47/12-19/192>0,
$$
一般纤维的同一差为 $27/4$。
所以所有边界均已覆盖，得 (14)–(15)。证毕。

这里的正截面和两步链第一例外都不可略去。
它们正是采用原完整角类而不是一个自由双次数矩形时需要检查的固定曲线。

## 4. 沿原轴的双重簇与完整正性

记 $\pi_N:X_N\to X$ 为第2节的 $N$ 次普通吹起，
新例外的全变换为 $E_i^*$、严格变换为 $E_i^{\rm str}$。
定义整除子
$$
\mathcal L_{D,N}=\pi_N^*\mathcal B_D-2\sum_{i=1}^N E_i^*.
\tag{17}
$$
第一个中心只位于 $\Delta_0$ 的 $F_0$ 上，
其余中心沿原轴自由前进，均避开旧边界。

令
$$
c_*=\frac56,\qquad \epsilon_*=\frac1{12},\qquad
c_i=c_*\frac{N+1-i}{N+1}
+\epsilon_*\frac{i(N+1-i)}{(N+1)^2}\quad(1\le i\le N),
$$
并置 $c_0=c_*$。这些数严格递减，$0<c_i<c_*<1$。
取
$$
\Delta_N=(\Delta_0)^{\rm str}+\sum_{i=1}^N c_iE_i^{\rm str}.
\tag{18}
$$
它仍为系数小于一的简单正规交叉边界。
在全变换基中，
$$
\Delta_N=\pi_N^*\Delta_0+\sum_i(c_i-c_{i-1})E_i^*.
$$
因此
$$
\boxed{
A_{D,N}:=\mathcal L_{D,N}-(K_{X_N}+\Delta_N)
=\pi_N^*A_0(D)-\sum_i a_iE_i^*,\qquad
a_i=3+c_i-c_{i-1},\quad2<a_i<3.}
\tag{19}
$$

**引理 3。** 若
$$
\boxed{D-5>3R_N,}
\tag{20}
$$
则 $A_{D,N}$ ample。

**证明。** 先取非旧边界曲线 $C$ 的严格变换。
(7)、(14) 与 $a_i<3$ 给
$$
A_{D,N}\widetilde C
\ge(D-5)a-3S_N(C)
\ge(D-5-3R_N)a>0.
\tag{21}
$$
其中 $b\ge p$ 的情形已在 (12) 支付。

除 $F_0$ 外的旧边界不经过新中心，继续使用引理2的严格正交数。
$F_0$ 只经过第一个中心，所以
$$
A_{D,N}F_0^{\rm str}
=37/12-a_1>1/12.
$$
新例外则满足
$$
A_{D,N}E_i^{\rm str}
=a_i-a_{i+1}
=\frac{2\epsilon_*}{(N+1)^2}>0\quad(i<N),
$$
$$
A_{D,N}E_N^{\rm str}=a_N>2.
\tag{22}
$$
$N=1$ 时只有最后一式。

由 (14) 和 $D>5$，两个 nef 类的交数非负，故
$$
A_0(D)^2\ge\beta(D-5)^2.
$$
(19) 因而给
$$
A_{D,N}^2
=A_0(D)^2-\sum_i a_i^2
>\beta(D-5)^2-9N>0.
\tag{23}
$$
最后用 $R_N\ge\sqrt{3N/\beta}$ 及 (20) 即可；
实际上右边有充分余量。
全部曲线的严格正性及 (23) 满足曲面 Nakai–Moishezon 判别，
得到 ample。证毕。

(22) 的显式边界使真正的第一固定纤维也为正，
不是在原 $F_0$ 上留下负交数后仅声称“可加一个小边界”。

## 5. 正特征消失与原两个 N-jet 的整满射

**定理 4。** 若 $1\le N\le s$、$D\ge3$、
$f_D<p$ 且 (20) 成立，则
$$
\boxed{
\overline{\mathcal W}_D\longrightarrow
(k[t]/t^N)^2,\qquad
P\longmapsto(P(t,g),(\mathcal EP)(t,g))
\quad\text{满射}.}
\tag{24}
$$
同一有限整矩阵因此整满射。

**证明。** 使用与 R637 完全同一份已发表原定理：

E. Arvidsson, F. Bernasconi, J. Lacini,
*On the Kawamata–Viehweg vanishing theorem for log del Pezzo surfaces in positive characteristic*,
Compositio Math. **158** (2022), 750–763，
**Lemma 2.10，印刷页754**，
[官方正文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/24893DF316D4A83FE7DAFFBF9873B6D3/S0010437X22007394a.pdf/on_the_kawamataviehweg_vanishing_theorem_for_log_del_pezzo_surfaces_in_positive_characteristic.pdf)。

这里重新核对新增曲面的全部假设。
先在代数闭完美剩余域工作，最后按忠实平坦性下降矩阵秩。
$p>2$，$X_N$ 光滑射影，$\Delta_N$ 系数小于一且支撑简单正规交叉，
所以是 klt 对，恒等映射即为 log resolution。
$\mathbb F_4$、原十九次固定吹起及全部边界支撑都能一同提升到 $W_2(k)$；
两个 $h_7$ 根可先在有限非分歧扩张中 Hensel 提升。
新增自由链只使用原弧前 $N$ 个系数，也可逐次提升其中心截面并吹起。
第一中心在 $F_0$ 上，之后中心避开旧交点，
故 (18) 的全部支撑同时保持简单正规交叉。
不要求把原无限 ODE 解提升到特征零。

整除子 (17) 减去 $K+\Delta_N$ 已由引理3证明 ample。
ABL Lemma 2.10 因此给
$$
H^1(X_N,\mathcal O_{X_N}(\mathcal L_{D,N}))=0.
\tag{25}
$$
没有使用“有理曲面自动消失”的错误概括。

令 $z=Y-g_{<N}(t)$。
原自由链上每点重数二的完整簇理想为
$$
I_{\rm cl}=(z^2,t^Nz,t^{2N}).
\tag{26}
$$
逐次异常赋值给 (26)；
并有
$$
(\pi_N)_*\mathcal O_{X_N}(\mathcal L_{D,N})
=I_{\rm cl}\mathcal O_X(\mathcal B_D).
$$
Leray 的低次正合列将其 $H^1$ 嵌入 (25)，故也为零。
所以整个 $H^0(X,\mathcal O_X(\mathcal B_D))$
满射到 (26) 的完整长度 $3N$ 商。
指定两个 jet 的理想是
$$
I_2=(z^2,t^N),\qquad I_{\rm cl}\subset I_2.
$$
复合即得长度 $2N$ 的满射。
(2) 只差原点单位 $d^{C_D}$；
用 $\mathcal E$ 代替 $\partial_Y$ 也只乘原轴单位 $g$。
这证明 (24)。
原显示来源有限自由、目标有限自由，约化满秩给一个真正单位子式，
所以同一整评价满射。证毕。

## 6. 真正模十二乘子支付旧三块的高行

现在回原
$$
J(P)\bmod p=
\left(
P(t,g)_{<s},\
a(\mathcal EP)(t,g)_{<s},\
\frac{a^2}{2}(\mathcal E^2P)(t,g)_{<\ell}
\right),
\tag{27}
$$
其中 $a$ 为原 Gaussian 单位，$1\le\ell<s-13$。
原 $w$ 与 $t$ 是单位换参，所有截断长度在此意义下相同。

取整数 $m\ge1,a_*\ge1$，满足
$$
\boxed{
3m\le a_*\le50m,\qquad
\ell\le a_*<s,\qquad
D_0=D-12m\ge3,\qquad b_{D-2}\ge a_*-1,
}
\tag{28}
$$
其中 $b_n=A_n+e_{n+1}$ 为原列的最高普通 $t$ 阶。
定义实际来源乘子
$$
\boxed{
G_m=Y^{12m}q_{12m}(t)\,t^{a_*-3m}.}
\tag{29}
$$
模十二周期给准确恒等
$$
q_{n+12m}=q_nq_{12m},\qquad
e_{n+12m+1}=e_{n+1}+47m.
\tag{30}
$$
因为 $0\le a_*-3m\le47m$，逐原基列有
$$
\boxed{G_m\mathcal W_{D_0}\subset\mathcal W_D.}
\tag{31}
$$
这支付真实 charge 成本 $12m$、所有有限角、$d$ 分母和无穷次数帽；
没有把乘子当免费来源。
在原轴上，$G_m(t,g)=t^{a_*}$ 乘整单位，而且
$\mathcal EG_m=12mG_m$。

原完整低行
$$
P,\mathcal EP\bmod t^{a_*},\qquad
\mathcal E^2P\bmod t^\ell
$$
有一个只用原基列的整右逆：
对每个 $0\le R<a_*$，
取 $n=\min\{n:b_n\ge R\}$ 及 $n+1,n+2$，
使用
$$
Y^{n+i}q_{n+i}t^{R-A_{n+i}}\quad(i=0,1,2).
\tag{32}
$$
$R=0$ 用 $n=0,1,2$；$R\ge1$ 的帽及 $A_{n+2}\le R$
按 R651 的原证明。
(28) 保全部 $n+i\le D$。
其首块是三条相邻 charge 的 $1,n,n^2$ 单位 Vandermonde，
按 $R$ 排列为块三角，所有低列产生的高尾完整保留。
先解三个 $a_*$-jet 再投影第三块至 $\ell$ 即得所需右逆。

从任意目标减去这个低行原像后，剩余恰是
$$
(t^{a_*}k[t]/t^s,\ t^{a_*}k[t]/t^s,\ 0).
$$
(29)–(31) 在前两个 jet 上的作用是 $t^{a_*}$
乘一个完整可逆二乘二三角单位；
第三短块因 $a_*\ge\ell$ 恒零。
因此定理4应用于
$$
N=s-a_*,\qquad D_0=D-12m
$$
便支付全部剩余高行。

**定理 5（旧短矩阵的实际整满射）。**
在 (28) 下，如果
$$
\boxed{D-12m-5>3R_{s-a_*},}
\tag{33}
$$
则整个原 $J$ 整满射。

这不是只证明两个不相容子空间各自有像：
先用 (32) 解低行，保其全部高尾，再用同一来源中的 (31) 消去那个实际余项。
得到的是整个原目标的一个真正整右逆。

## 7. 低 ell 的显式门与完整 M

对 $1\le\ell\le3$，取 $m=1,a_*=3$。
(28) 的原帽在 (33) 的 $D$ 范围自动满足。
于是
$$
\boxed{
D-17>
3\left\{\frac{48}{47}
+\sqrt{\left(\frac{48}{47}\right)^2+\frac{36(s-3)}{47}}\right\}
}
\tag{34}
$$
就给旧 $J$ 整满射。
由于 $s=(p+1)/6$，它的主阶是
$$
\boxed{D>\left(\sqrt{54/47}+o(1)\right)\sqrt p.}
\tag{35}
$$
更一般，任意固定 $\ell$ 都可在 (28) 中取固定的 $m,a_*$，
所以同一主常数仍成立；有限参数使用 (28)、(33) 而非略去固定成本。

恢复完整原矩阵时仍是
$$
M=c_*U_0m_{13}J.
$$
整个 $c_*U_0$ 为原整目标单位，$m_{13}$ 保留原两条十三行 carry。
因 $J$ 整满射，其实际像准确等于 $m_{13}$ 的像。
若 $L=2s+\ell$，原非零 Smith 因子因此为
$$
\boxed{
L-26\text{ 个单位},\qquad26\text{ 个 }p,
}
\tag{36}
$$
且目标仍有十三个原自由方向。
故在这个范围，没有额外有限 $C_2$ 或需要由独立的同 $R$ 第二 forcing
解决的非零有限方向；原各阶修正可由同一个整右逆连续选取。

(36) 没有把某个预先固定的坐标代表认作字面为零，
也没有使用 full $C$ 的高阶 Smith 计算。
这是旧目标上整个实际 $J$ 的满射，经原完整基变换运输而得。

## 8. 对剩余窗口的准确影响

R637 通过平面子空间返回原帽，给约 $3.943\sqrt p$ 的充分范围。
本篇直接使用整个原角线性系，将低 $\ell$ 的统一门降至 (35)。
它覆盖任意稠密混合 charge，不需要 R680 的同余对称。

但 $\sqrt{54/47}$ 仍大于维数临界 $\sqrt{8/47}$。
因此本文没有消掉临界旧矩阵中的实际左右缺陷，
也没有判断 R651 的 $\mathcal G_P$、$Y^+$、$Z^+$、$\Psi_R$
在尚存窗口中的同源像。
原两或三条完整中央没有传播给 (29)；
这里使用它的唯一理由是 (31) 的原来源包含与满射定理。

后续须集中于 (34) 以下的真实矩阵，
保原 $P_{134}/U_0$、两个十三行带、同一个 $R$ 和完整下一精度。
本文不增加目标素数扫描，不把仅有单位首 regular 系数或源端基变换
冒作指定余类的非零证书。

## 依赖

- [R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)：
  原 Euler forcing 的完整十九角极帽、nef 原线性系和曲线交数。
- [R467](R467-tame-branch-contact-and-all-factor-degree-barrier.md)：
  原截止内 tame 共振和完整 Hensel 判别式。
- [R555](R555-whole-original-linear-system-and-nonzero-high-contact-forcing.md)：
  全原来源 $\mathcal B_D$ 及精确十九重数。
- [R637](R637-original-short-three-block-square-root-surjectivity.md)：
  已核的 ABL 原定理、自由链完整簇理想和实际短矩阵运输。
- [R651](R651-original-higher-critical-branch-lift-and-complete-second-forcing.md)：
  全原列低行右逆及同一个修正的边界范围。

本篇为全参数曲面和原有限矩阵证明，无新增数值证书。
