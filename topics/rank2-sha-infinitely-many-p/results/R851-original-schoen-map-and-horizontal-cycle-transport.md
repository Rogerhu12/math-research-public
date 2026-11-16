# R851 — 原 Schoen 九次映射、三阶商的余三次与实际水平循环

日期：2026-11-16。**状态：以下显式函数域、次数、微分与完整原循环运输已证明。**

本篇接 [R850](R850-original-smooth-cubic-quotient-and-exact-top-cycle-transport.md) 的同一个原
$E_0^3$、最高 Chow 投影和实际模曲线映射，落实 Schoen 的模椭圆曲面纤维积对应。
所有坐标、图形对应、有限 Artin 系数和原 $q_0/q_2$ 均保留。
所得原曲线的主像是水平曲线；本篇不把它认作 CM 纤维中的指定 canonical 循环，
也不从相同的二维 $H^3$ 推出 Chow 类成比例。

## 1. 同一原模型及明确的目标坐标

取
$$
E_0:Y^2=X^3+1,\qquad A=E_0^3,\qquad
\Omega_A=\bigwedge_{i=1}^3\frac{dX_i}{2Y_i}.
\tag{1}
$$
另记 Schoen §13 的模型为
$$
E_{27}:y^2=x^3+\frac14,\qquad
a_i=y_i+\frac12,\quad b_i=y_i-\frac12=a_i-1,\quad x_i^3=a_i b_i.
\tag{2}
$$
设
$$
T=x_1x_2x_3,\qquad T^3=\prod_{i=1}^3a_i b_i.
\tag{3}
$$

目标的两个齐次坐标按以下次序固定：
$$
(r_0:r_1:r_2),\qquad(s_0:s_1:s_2).
$$
取双三次模型
$$
\begin{split}
W_9^{\rm sing}:\quad&
(r_0^2r_2+r_1^2r_0+r_2^2r_1)s_0s_1s_2\\
&-(s_0^2s_2+s_1^2s_0+s_2^2s_1)r_0r_1r_2=0.
\end{split}
\tag{4}
$$
在 $r_2=s_2=1$ 的 chart，**只在本篇**置
$$
x=r_0/r_2,\quad y=r_1/r_2,\quad r=s_0/s_2,\quad s=s_1/s_2.
$$
这里的 $x,y$ 是目标坐标，不能与 (2) 的 $x_i,y_i$ 混同。
式 (4) 成为
$$
P=(x^2+xy^2+y)rs-(r^2+rs^2+s)xy=0.
\tag{5}
$$
共同的模底参数准确为
$$
\boxed{\tau(x,y)=\frac{x}{y}+y+\frac1x,\qquad
       \tau(x,y)=\tau(r,s).}
\tag{6}
$$
循环交换齐次坐标会改写 (6)；本篇不在推导中更换这个次序。

记 $W_9$ 为这个模纤维积的光滑射影解消。它就是 Schoen 所用
$V_0(9)\times_{\mathbf P^1}V_0(9)$ 的光滑模型。
原文为 C. Schoen, *On the computation of the cycle class map for
nullhomologous cycles over the algebraic closure of a finite field*,
Ann. Sci. ENS 28 (1995), §13，printed pp.42–44，尤其 (13.1)–(13.4)：
<https://numdam.org/item/10.24033/asens.1708.pdf>。
下面所有次数及倍率均由显示式独立计算，不借用另一三维簇之间未核的次数。

## 2. Schoen 映射的同一套仿射式及共同底参数

在 (2) 的仿射 chart，原 (13.4) 的两个齐次三元组为
$$
\begin{aligned}
(r_0:r_1:r_2)
 &=(-a_1x_2^2x_3b_3:-x_1a_1b_2x_3^2:x_1^2x_2b_3),\\
(s_0:s_1:s_2)
 &=(-a_1b_3T:-T^2:a_1b_2b_3).
\end{aligned}
\tag{7}
$$
利用 $x_i^3=a_i b_i$，在 (6) 的准确坐标中化为
$$
\boxed{
x=-\frac{T}{b_1},\quad
y=-\frac{a_1a_3b_2}{T},\quad
r=-\frac{T}{b_2},\quad
s=-\frac{T^2}{a_1b_2b_3}.
}
\tag{8}
$$
这定义 $\mathcal F_{27}:E_{27}^3\dashrightarrow W_9$。

为逐式核定目标，第一对坐标给
$$
\frac{x}{y}+y+\frac1x
=\frac{a_2b_3-a_1b_2a_3-b_1}{T}.
$$
第二对给
$$
\frac r s+s+\frac1r
=\frac{a_1b_3-b_1a_2a_3-b_2}{T}.
$$
两分子的差为
$$
(a_2-a_1)b_3+a_3(-a_1b_2+b_1a_2)+(b_2-b_1)
=(a_2-a_1)(b_3-a_3+1)=0.
$$
故准确有
$$
\boxed{
\tau\circ\mathcal F_{27}
=\frac{a_2b_3-a_1b_2a_3-b_1}{T}.
}
\tag{9}
$$
这同时证明 (8) 落在 (4)，无需由维数猜测目标。

## 3. 九阶不变域及完整有理逆

令
$$
N=\ker\!\left(\mu_3^3\xrightarrow{\;\mathrm{product}\;}\mu_3\right).
\tag{10}
$$
每个 $\mu_3$ 作用于相应 $x_i$，固定 $y_i$。其阶为9；
泛型作用自由，且固定最高三微分。
不变函数域为
$$
\mathbf Q(E_{27}^3)^N
=\mathbf Q(a_1,a_2,a_3,T),\qquad
T^3=\prod a_i(a_i-1).
\tag{11}
$$
可先在含 $\omega$ 的域中按三个独立 Kummer 坐标证明，再下降群概形；
也可直接用泛型九点轨道及 (3)。
式 (8) 全在 (11) 中。

现在给出逆，因而不只证明映射 dominant。
在目标的非空开集令
$$
k=\frac{x}{r},\qquad l=\frac{y}{s}.
$$
由 (8)，$k=b_2/b_1$、$l=ka_1/a_2$，故
$$
\boxed{
a_1=\frac{l(1-k)}{k(1-l)},\qquad
a_2=\frac{1-k}{1-l},\qquad
T=-x(a_1-1),\qquad
a_3=-\frac{yT}{a_1(a_2-1)}.
}
\tag{12}
$$
这些式子在源的函数域中逐项恢复 (11) 的全部生成元。
因此 $\mathcal F_{27}$ 诱导 $E_{27}^3/N$ 与 $W_9$ 的双有理对应，且
$$
\boxed{\deg\mathcal F_{27}=9.}
\tag{13}
$$
这里是泛型次数，不是某条特定曲线推前的次数。

对角子群
$$
\Delta=\{(\zeta,\zeta,\zeta):\zeta^3=1\}\subset N
$$
阶为3；包含成立是因为 $\zeta^3=1$。
于是由函数域塔，$E_{27}^3/\Delta\dashrightarrow W_9$ 的准确次数为3。
不能把这个剩余次数省成双有理。

## 4. 回到原 $E_0$：有理下降不增加17定义域

取 $t^3=4$，则
$$
\iota:E_0\longrightarrow E_{27},\qquad
(X,Y)\longmapsto(X/t,Y/2)
\tag{14}
$$
为同构。改变 $t$ 的选择只使 $\iota$ 相差一个 $[\omega]$；
三重积中的变化是共同的 $\Delta$，已包含于 $N$。
事实上可以完全不靠这个下降口述：在原 $A$ 上置
$$
a_i=(Y_i+1)/2,\qquad b_i=(Y_i-1)/2,\qquad
T=X_1X_2X_3/4.
\tag{15}
$$
将 (15) 代入 (8)，得到原模型上全为有理函数的映射
$\mathcal F_0:A\dashrightarrow W_9$：
$$
\boxed{
\begin{aligned}
x&=-\frac{X_1X_2X_3}{2(Y_1-1)},\\
y&=-\frac{(Y_1+1)(Y_3+1)(Y_2-1)}{2X_1X_2X_3},\\
r&=-\frac{X_1X_2X_3}{2(Y_2-1)},\\
s&=-\frac{(X_1X_2X_3)^2}{2(Y_1+1)(Y_2-1)(Y_3-1)}.
\end{aligned}}
\tag{16}
$$
故 $\mathcal F_0$、其图形及所有下述对应在 $\mathbf Q$ 上定义。
没有为了 (14) 扩大原 Artin 域，更没有增加17处的角色。
仍有
$$
\deg\mathcal F_0=9.
$$

R850 的 $Z$ 是原 $A/\Delta$ 的固定光滑模型，因此 (16) 唯一诱导
$$
\boxed{\mathcal F_Z:Z\dashrightarrow W_9,\qquad
       \deg\mathcal F_Z=3.}
\tag{17}
$$
这里只比较函数域，故 R850 的27点吹起不改变次数。

## 5. 最高三微分的完整绝对倍率

令
$$
\Omega_{27}=\bigwedge_{i=1}^3\frac{dx_i}{2y_i}.
$$
由 (2) 微分，
$$
\frac{dx_i}{2y_i}=\frac{da_i}{3x_i^2},\qquad
\Omega_{27}=\frac{da_1\wedge da_2\wedge da_3}{27T^2}.
\tag{18}
$$
在目标明确选择以下 residue 约定：
$$
\boxed{\Omega_W=\frac{dx\wedge dy\wedge dr}{P_s}.}
\tag{19}
$$
式 (19) 固定符号；若使用把 $dP/P$ 放首位的另一 residue 约定，
必须同时改变符号，不能在结果中再任意选正负。
该 residue 在所选光滑解消上延拓为全纯三微分；这一点也可由下面(23)自含核定：
在同时消去 $\mathcal F_0$ 不定点的光滑模型上，其拉回是原全纯 $-18\Omega_A$ 的拉回。
若目标任一素除子上有负阶，取有限函数域扩张中支配它的赋值，
分歧指数 $e$ 给三微分阶 $e\operatorname{ord}+(e-1)<0$，与该全纯拉回矛盾。
这对目标的每个解消除子同样适用，故不依赖遗漏某个异常极。

给出完整 Jacobian 核对。将 $d\log x,d\log y,d\log r$ 按列
$da_i/(3a_i b_i)$ 表示，矩阵为
$$
M=
\begin{pmatrix}
-a_1-1&2a_2-1&2a_3-1\\
a_1-2&a_2+1&a_3-2\\
2a_1-1&-a_2-1&2a_3-1
\end{pmatrix}.
$$
设
$$
K_*=b_1a_2a_3+a_1b_3.
$$
第二行加第三行后为 $3(b_1,0,b_3)$，直接展开给
$$
\det M=-9K_*.
$$
故
$$
d\log x\wedge d\log y\wedge d\log r
=-\frac{K_*}{3\prod a_i b_i}\,
 da_1\wedge da_2\wedge da_3.
\tag{20}
$$
另一方面，(5) 在 $P=0$ 上给
$$
P_s=\frac{xyr(r-s^2)}s,\qquad
\frac{s}{r-s^2}=\frac{T}{K_*}.
\tag{21}
$$
由 (20)–(21)，
$$
\boxed{
\mathcal F_{27}^*\Omega_W
=-\frac{da_1\wedge da_2\wedge da_3}{3T^2}
=-9\Omega_{27}.
}
\tag{22}
$$
从 (14)，$\iota^*(dx/(2y))=(2/t)dX/(2Y)$，而 $(2/t)^3=2$。
所以原模型上的准确式为
$$
\boxed{\mathcal F_0^*\Omega_W=-18\Omega_A.}
\tag{23}
$$
特别，若希望与原微分完全相同，应定义
$$
\Omega_9^{\rm orig}=-\Omega_W/18.
\tag{24}
$$
这不是一个未定 period；它是已给定的有理三微分。
本篇不把 (24) 与某个另选的 normalized modular $q$-form 比较时
所需的 period 也暗中设为1。

按 R850 的 $q^*\Omega_Z=b^*\Omega_A$ 规范，(23) 等价于
$$
\boxed{\mathcal F_Z^*\Omega_W=-18\Omega_Z}
\tag{25}
$$
作为有理三微分的等式。拉回到任意消去不定点的光滑模型后，
它是正则三微分的等式。

## 6. 原循环的完整 proper graph 运输

本节不把 rational map 对曲线的严格像冒充全部 Chow 拉回。
为 (17) 选一个在 $\mathbf Q$ 上的光滑射影图形解消
$$
b_9:\mathcal T\longrightarrow Z,\qquad
f_9:\mathcal T\longrightarrow W_9.
\tag{26}
$$
选择图形解消在 $\mathcal F_Z$ 已有定义的开集上为同构。
$\mathcal T$ 可能还须吹起曲线，不是 R850 仅吹27点的 $\widetilde A$。
定义真正对应
$$
\mathscr G_*=f_{9,*}b_9^*,\qquad
\Pi_{\mathcal T}=b_9^*\Pi_Zb_{9,*}.
\tag{27}
$$
$Z,\mathcal T$ 均光滑，$b_9^*$ 是 Chow 拉回；
$b_{9,*}b_9^*=1$ 保证 $\Pi_{\mathcal T}$ 幂等。

沿 R839/R841/R850，原唯一端点已有固定有限表达
$$
\mathcal Z_{\rm orig}=\sum_i c_i\,\Pi\Phi_{i,*}[X],
\quad X=X_0(10404),
$$
以及准确式
$$
\alpha\mathcal Z_{\rm orig}
=3\sum_i c_i\,\Pi_Z\phi_{Z,i,*}[\overline X],
\qquad \overline X=X_0(3468).
\tag{28}
$$
这里 $\alpha$ 是 R850 的固定 Chow 同构；
$c_i$ 包含全部 Hom 展开、平均、polarization 及原有限角色。
定义其指定 Schoen 运输为
$$
\boxed{
\mathcal Z_9
:=\mathscr G_*\alpha\mathcal Z_{\rm orig}
=3\sum_i c_i f_{9,*}b_9^*\Pi_Z
                    \phi_{Z,i,*}[\overline X].
}
\tag{29}
$$
(29) 是完整 Chow 恒等式，不只是实现中的同构。

对第7节的非零坐标项，$\mathcal F_Z\phi_{Z,i}$ 在泛点有定义；
第7节的非常值 $\tau$ 还保证泛点避开特殊纤维的奇异点；
在此泛点 $b_9$ 为同构。由曲线的适当性判据，$\phi_{Z,i}$ 有到所选图形解消的实际提升
$\widehat\phi_i:\overline X\to\mathcal T$。
于是 (29) 也准确写成
$$
\boxed{
\mathcal Z_9
=3\sum_i c_i f_{9,*}\Pi_{\mathcal T}
                    \widehat\phi_{i,*}[\overline X].
}
\tag{30}
$$
这里始终保留 $\Pi_{\mathcal T}$。
没有宣称 $b_9^*\phi_{Z,i,*}[\overline X]$
等于严格变换，也没有丢弃异常循环。
零坐标项先由 R839 的真阿贝尔子簇结论杀掉，再使用此式。

(29)–(30) 的3来自真实 source quotient
$X_0(10404)\to X_0(3468)$；
它不是又把 ambient degree3 乘到每条曲线上。
某条曲线到其像的有限次数仍由各实际 pushforward 保持。
原 $q_0/q_2$ 从未改变。
返回 R831 的 old copy 仍保 $6^{-2}$；
返回原 $X_1$ 仍保 $12^{-2}$、$D_X=1632,D_C=816$ 的原规范。

对同调平凡的原最高类 $z=\Pi z$，Abel–Jacobi 的对应函子性与
(25) 给
$$
\boxed{
\operatorname{AJ}_{W_9}(\mathscr G_*\alpha z)(\Omega_W)
=-18\,\operatorname{AJ}_{A}(z)(\Omega_A).
}
\tag{31}
$$
用 (24) 则倍率为1。复或适用的 $p$-adic Abel–Jacobi 均按其
实际目标及原 period 理解；这不把一个 regulator 的非零
推广到其它 $p$。式 (31) 也不声称一般 Chow 类能由其 AJ 值确定。

## 7. 指定原曲线的底参数确实非常值

现在付原曲线像的性质，而非只给一个 ambient correspondence。

把 (15) 代入 (9)，得到原 $E_0^3$ 上的完整函数
$$
\boxed{
\tau=
\frac{
3-3Y_1-3Y_2+3Y_3-Y_1Y_2+Y_1Y_3+Y_2Y_3-Y_1Y_2Y_3
}{2X_1X_2X_3}.
}
\tag{32}
$$
取每份 $E_0$ 原点处由 $dX/(2Y)=dz$ 固定的形式参数。
则
$$
X_i=z_i^{-2}+O(z_i^4),\qquad
Y_i=-z_i^{-3}+O(z_i^3).
$$
式 (32) 中三次乘积是唯一最低项，故
$$
\boxed{
\tau=\frac1{2z_1z_2z_3}
\bigl(1+O(z_1^3,z_2^3,z_3^3)\bigr).
}
\tag{33}
$$

每个 R839 的实际映射均以 cusp $\infty$ 为基点：
$$
\Phi=(a_f,\ a_gq_0,\ a_hq_2),\qquad
a_f(\infty)=a_g(\infty)=a_h(\infty)=O.
$$
若某坐标恒为 $O$，其最高投影由 R839 第6节消失。
其余项三个坐标都非常值。
以 $Q=e^{2\pi iz}$ 为原源 cusp 参数，设相应原椭圆形式积分为
$$
z_1=c_fQ^{m_f}+\cdots,\quad
z_2=c_gQ^{m_g}+\cdots,\quad
z_3=c_hQ^{4m_h}+\cdots,
$$
其中 $c_f c_g c_h\ne0$，$m_f,m_g,m_h\ge1$。
准确的 $4m_h$ 来自未改动的 $q_2:z\mapsto4z$。
于是
$$
\boxed{
\operatorname{ord}_{\infty}(\tau\circ\Phi)
=-(m_f+m_g+4m_h)\le-6.
}
\tag{34}
$$
这里不存在同阶抵消： (33) 的每个其它项都乘一个正阶
$z_i^3$。不需要知道原 modular Jacobian 同态的所有坐标。

在 R841 polarization 后的实际项 $\Phi=(F,aq_0,aq_2)$ 中，
(34) 为 $-(m_f+5m_a)$。
原三阶等变还给 $m_f,m_g,m_h\equiv1\pmod3$，
所以这个极阶是3的倍数；下降至 $\overline X$ 后，
极阶恰除以3，仍至少为2。
即使某个未采用 polarization 的项只在更大的固定域上定义，
(34) 仍逐项成立。

因此每条有效原曲线的主像在
$$
W_9\longrightarrow\mathbf P^1_\tau
$$
下都是**水平曲线**。
它不是字面支撑于某个 CM 纤维的曲线。
所有原有限 Galois 共轭仍把 cusp 原点映到原点，
故这个结论对整个固定 Artin orbit 同样有效。

此结论只描述实际映射和循环的支撑来源。
它不排除水平循环的某个投影与竖直循环在 Chow 群中有关系；
(29) 的投影和异常项也完整保留。
因此不能把“水平”误写成指定 canonical 比较不可能。

## 8. 全 Artin 角色、原 period 与 canonical 比较的位置

设 $L$ 是原 R839/R841 已固定的有限 Galois 定义域，
$\mathcal E$ 是原系数域。对原实际有限角色 $\chi$，记
$$
e_\chi=\frac1{|\operatorname{Gal}(L/K)|}
\sum_{\sigma}\chi(\sigma)^{-1}\sigma
$$
（若原角色先在一个商上定义，保同一个原 trace/idempotent）。
因为 (16)、(26) 可在 $\mathbf Q$ 上定义，
$$
\boxed{
\mathscr G_*e_\chi=e_\chi\mathscr G_*,
\qquad
\mathscr G_*\alpha(e_\chi\mathcal Z_{\rm orig})
=e_\chi\mathcal Z_9.
}
\tag{35}
$$
这是真正点／循环因子的 Galois 作用；
不让系数同时作一次未指定的半线性共轭。

特别，原三个 $\lambda_j=\eta_j^{-1}\psi_0^3$
的不同17有限角色完整保留。
$N$ 的 order9 只是一组目标几何自同构；
它不准许把原 order18 Artin idempotent 变成平凡角色。
(14) 的共同三次 twist 在商上消失，
也不意味着原 $\eta_j$ 的全局 twist 消失。
原最高 $(3,0)$、$(0,3)$ 分量可按同一系数嵌入分别使用 (31)、(35)。

目前得到的是固定、显式、全有理的模纤维积载体和指定原循环 (29)。
R814 的 canonical 类来自其先于 $p$ 固定的 good pair、
CM 同源图和完整有限角色，并非本篇任意选定的一条水平曲线。
要比较二者，仍需一个保原角色、投影、level及坏位向量的
实际循环对应或 regulator 恒等式。
Schoen §14 的有限域 Griffiths-group 结论不能替代
这个特征零的指定类比较；同一个最高 $H^3$ 也不能替代。

本篇没有证明原端点或其 AJ 非零，没有给新的中央零，
也没有消除 R838 的完整 critical projector、Euler 或 period。
没有新增数值运行、目标素数扫描或可重算数据。

## 9. 来源与核验范围

- 原模型、$\Pi,\Pi_Z,\alpha$、source degree3 及固定 $\Omega_Z$：
  [R839](R839-top-cm-translation-invariance-and-original-ceresa-expression.md)、
  [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)、
  [R850](R850-original-smooth-cubic-quotient-and-exact-top-cycle-transport.md)。
- Schoen 1995，printed pp.42–44，§13、(13.1)–(13.4)、Theorem13.2：
  <https://numdam.org/item/10.24033/asens.1708.pdf>。
  本篇已读取这些原文页的全文文字；显示式 (7)–(12)、(20)–(23)
  则在固定坐标中给出自含代数核定。
- K. Kimura, *A rational map between two threefolds*,
  arXiv:math/0410259 **v3**，第1页及 references[8],[9]：
  <https://arxiv.org/pdf/math/0410259>。
  v3 明确指出 Schoen 已构造这些模纤维积与 $E^3$ 之间的对应；
  不采用早版“尚无对应”的表述。
- C. Meyer, *A dictionary of modular threefolds* (Mainz, 2005)，
  printed pp.173–174：
  <https://openscience.ub.uni-mainz.de/server/api/core/bitstreams/ee6e89a1-fa8b-4992-b316-fecb87bb8fce/content>。
  这里只用它对 Schoen 原齐次式和双三次模型的清晰转录；
  不引用该处另一 monomial correspondence 的方向或次数。
