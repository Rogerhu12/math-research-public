# R153：唯一有理三次谱线迫使环类判别式增长

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文将 R150 中尚未自动给出第二频率的“只有一个非零中心值特征形式”分支，转成实际三次环类判别式的有效下界：
$$
\boxed{M\,h(\mathcal O)>\frac{p(p+1)}{1296}.}
$$
进一步有
$$
\boxed{M^{3/2}(\log M+2)>\frac{\pi p(p+1)}{1296},}
$$
因而这个分支必须满足 $M\gg p^{4/3}/(\log p)^{2/3}$，常数绝对且有效。证明用真实 Brandt 周期的整性、同取向纤维装填、已发表 Mestre 范数公式，以及本文自含的 $\mathbb F_{25}$ 模参数化次数下界。不使用 Watkins 未核发表状态的次数下界。

**前提边界：** 除 $M<p$ 的独立结论外，本文始终保留至少一个三次中心值非零，即 $P_\eta\ne0$。全部中心值同时为零的变化导子分支不受本证明排除。结论不给 $M$ 上界，不证明一般三色 Fourier 理想为单位，也未完成 Serre 一致性。

## 1. 对象、谱计数及定理

设 $p>37$ 为素数，$K$ 为虚二次域，$p$ 在 $K$ 惰性。设 $\eta$ 是精确导子 $c$、阶恰为三的原始环类字符，置
$$
\mathcal O=\mathbb Z+c\mathcal O_K,\qquad
M=|D_K|c^2,\qquad
h=h(\mathcal O),\qquad p\nmid M.
\tag{153.1}
$$
固定 $K\hookrightarrow B_{p,\infty}$ 及极大序 $R$，满足 $R\cap K=\mathcal O$。使用 R76 的真实右理想类映射及三次周期
$$
\begin{aligned}
\varphi:\operatorname{Pic}(\mathcal O)&\longrightarrow\mathrm{Cls}(R),
&[\mathfrak a]&\longmapsto[\mathfrak aR],\\
P_\eta&=\sum_{[\mathfrak a]}\eta(\mathfrak a)^{-1}[\varphi(\mathfrak a)].
\end{aligned}
\tag{153.2}
$$
令 $\mathcal F_\eta$ 为水平 $p$、权二、平凡 nebentype 的全部归一化新形式中满足
$$L\!\left(\tfrac12,\pi_{f,K}\otimes\eta\right)\ne0\tag{153.3}$$
者，每个复归一化特征形式只计一次。这是酉自守归一化。

**定理 153.1。** 集合 $\mathcal F_\eta$ Galois 稳定，并有以下结论。

1. 若 $M<p$，则 $|\mathcal F_\eta|\ge2$。
2. 若 $|\mathcal F_\eta|=1$，则唯一的形式有有理 Fourier 系数，且
   $$
   M>p,\qquad
   \boxed{Mh>\frac{p(p+1)}{1296}.}
   \tag{153.4}
   $$
3. 在第 2 项的情况下，更有
   $$
   \boxed{M^{3/2}(\log M+2)>\frac{\pi p(p+1)}{1296},}
   \tag{153.5}
   $$
   以及只含 $p$ 的显式界
   $$
   \boxed{
   M>\left(\frac{\pi p(p+1)}{2592(\log p+1)}\right)^{2/3}.
   }
   \tag{153.6}
   $$

因此，如果已知 $P_\eta\ne0$，则以下任一条件足以保证至少两个非零中心值特征形式：
$$
M<p;\qquad
Mh\le\frac{p(p+1)}{1296};\qquad
M^{3/2}(\log M+2)\le\frac{\pi p(p+1)}{1296}.
\tag{153.7}
$$
第一个条件本身还保证 $P_\eta\ne0$，故不需额外非消失前提。这里的“两个”可以是同一个非有理 Galois 轨道中的两个共轭；并不声称有两个不同的 $\mathbb Q$-单因子。

## 2. 完整有理 Brandt 谱及中心值的 Galois 稳定性

记
$$
\mathscr X=\mathbb Z[\mathrm{Cls}(R)],\qquad
V_{\mathbb Q}=\mathscr X^0\otimes\mathbb Q.
$$
在标准理想类基 $[x]$ 中使用正定 Hermitian 配对
$$
\left\|\sum_x z_x[x]\right\|^2
=\sum_xw_x|z_x|^2,
\qquad
w_x=\frac{|\mathcal O_L(I_x)^\times|}{2}.
\tag{153.8}
$$
因 $p>3$，Deuring 对应下 $w_x=|\operatorname{Aut}(E_x)|/2\in\{1,2,3\}$。这是除子 Brandt 模的标准基和配对，不是把函数基的倒权直接混入范数公式。

由 $\eta\ne1$，$P_\eta\in V_{\mathbb Q}\otimes\mathbb Q(\zeta_3)$。完整素水平 Brandt–Jacquet–Langlands 分解为
$$
V_{\mathbb Q}\otimes\mathbb C=\bigoplus_fV_f,
\tag{153.9}
$$
每个 $V_f$ 为一维，$f$ 遍历全部上述归一化新形式。权二水平一尖点空间为零，故无遗漏的旧谱。Hecke 矩阵为有理矩阵，且关于 (153.8) 自伴。

记 $e_f$ 为正交投影。R76 §6 已逐项核准的 Cai–Shu–Tian (2014), Theorem 1.2，在 (153.1) 的原始性、惰性、互素性和同一最优嵌入条件下给
$$
e_fP_\eta\ne0
\quad\Longleftrightarrow\quad
L\!\left(\tfrac12,\pi_{f,K}\otimes\eta\right)\ne0.
\tag{153.10}
$$

对任意 $\sigma\in\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$，有
$$
\sigma(e_f)=e_{f^\sigma},\qquad
\sigma(P_\eta)\in\{P_\eta,P_{\eta^{-1}}\}.
$$
平凡 nebentype 的 Hecke 特征值为实数，故 $e_f$ 为实代数矩阵，而且
$$e_fP_{\eta^{-1}}=\overline{e_fP_\eta}.$$
所以非零投影的集合 Galois 稳定，证明 $\mathcal F_\eta$ 的稳定性。

若它只有一个元素 $f$，则 $f^\sigma=f$ 对所有 $\sigma$，因此 $a_n(f)\in\mathbb Q$。其特征线由有理 Hecke 矩阵的有理特征值共同核定义，在 $\mathbb Q$ 上已有维数一。于是存在原始整向量
$$
v=\sum_xv_x[x]\in\mathscr X^0,\qquad
\gcd_x(v_x)=1,
$$
使
$$P_\eta=\kappa v,\qquad0\ne\kappa\in\mathbb Q(\zeta_3).\tag{153.11}$$
这里已经使用 $P_\eta\ne0$；若全谱为零，不能选取这样的非零 $\kappa$。

## 3. 同取向纤维：单射及统一装填

R76 §§2.1–2.3 给出如下理想层面的事实。固定一个 $\varphi$ 纤维，在同一左极大序 $S$ 中，纤维内各个不同 Picard 类给出两两不被 $S^\times$ 共轭的最优嵌入 $\iota_i:\mathcal O\hookrightarrow S$，而且全部具有同一个 $p$ 剩余取向。该结论使用真实右理想类，已处理 $p$ 两边理想，不能以左序的 type 类代换。

写 $\mathcal O=\mathbb Z[\omega]$，$\omega=(t+\sqrt{-M})/2$。令
$$v_i=\iota_i(\omega)-t/2.$$
这些点在纯四元数实三维欧氏空间的同一球面上，且
$$
N(v_i)=M/4,\qquad
0<N(v_i-v_j)\in p\mathbb Z\quad(i\ne j).
\tag{153.12}
$$
后一条来自共同取向：嵌入值之差落在 $S$ 的 $p$ 两边素理想内。

若 $M<p$，两点距离的平方不超过 $M$，与 (153.12) 矛盾。因此 $\varphi$ 单射。由于阶三角色的三个值都出现，$P_\eta$ 的非零坐标同时含 $1,\zeta_3,\zeta_3^2$，并不落在任何单一有理向量的复数倍直线上。这与 (153.11) 矛盾；且单射本身证明 $P_\eta\ne0$。定理第 1 项及第 2 项的 $M>p$ 得证；$M=p$ 被 $p\nmid M$ 排除。

现在设 $r=M/p>1$。同一纤维内两点的弦长至少 $\sqrt p$，球半径为 $R_0=\sqrt M/2$。以各点为中心、角半径 $\arcsin\sqrt{p/M}$ 的开球帽两两不交。球帽面积为
$$2\pi R_0^2(1-\sqrt{1-p/M}).$$
因此任一纤维大小 $n_x$ 满足 R83 (83.17) 的界
$$
\boxed{
n_x\le2r(1+\sqrt{1-1/r})<4r=4M/p.
}
\tag{153.13}
$$
此装填结论不要求周期消失，也不要求每个纤维至少三点。

## 4. 三颜色共线的整性与范数上界

令 $n_{x,j}$ 为纤维 $x$ 中满足 $\eta(\mathfrak a)^{-1}=\zeta_3^j$ 的理想类数。则
$$
n_x=n_{x,0}+n_{x,1}+n_{x,2},\qquad
(P_\eta)_x=n_{x,0}+n_{x,1}\zeta_3+n_{x,2}\zeta_3^2.
\tag{153.14}
$$
在唯一谱线情形，这些真实三颜色计数的差向量全部满足
$$
(n_{x,0}-n_{x,2})+(n_{x,1}-n_{x,2})\zeta_3=\kappa v_x.
\tag{153.15}
$$
这正是“所有颜色向量落在同一有理直线”的精确整格含义。我们不假定 Picard 群在整个 Brandt 类集上存在可下降的置换作用。

由 $v$ 原始，存在整数 $r_x$ 使 $\sum_xr_xv_x=1$。将 (153.11) 按坐标相加，得到
$$
\kappa=\sum_xr_x(P_\eta)_x\in\mathbb Z[\zeta_3].
$$
因此
$$
|\kappa|^2=N_{\mathbb Q(\zeta_3)/\mathbb Q}(\kappa)\in\mathbb Z_{\ge1},
\qquad
\|v\|^2\le\|P_\eta\|^2.
\tag{153.16}
$$
这一步排除了任意小的有理或复缩放因子；不能只由复线性相关直接得到范数比较。

再由 $w_x\le3$、$|(P_\eta)_x|\le n_x$、$\sum_xn_x=h$ 和 (153.13)，
$$
\begin{aligned}
\|v\|^2
&\le\sum_xw_x|(P_\eta)_x|^2\\
&\le3\sum_xn_x^2\\
&<\frac{12M}{p}\sum_xn_x
=\boxed{\frac{12Mh}{p}}.
\end{aligned}
\tag{153.17}
$$
严格号来自每个非空纤维 $n_x<4M/p$。

## 5. Mestre 公式的准确方向及最优曲线

有理新形式 $f$ 对应水平 $p$ 的强 Weil 椭圆曲线 $B/\mathbb Q$。令
$$\phi_B:X_0(p)\longrightarrow B$$
为最优模参数化，$d_B=\deg\phi_B$。

在 (153.8) 的除子基配对及 (153.11) 的原始整向量规范下，已发表 Mestre 范数公式为
$$
\boxed{\langle v,v\rangle=t_Bd_B,\qquad
t_B=|B(\mathbb Q)_{\mathrm{tors}}|\in\mathbb Z_{\ge1}.}
\tag{153.18}
$$
所以所需方向确实是
$$d_B\le\|v\|^2,\tag{153.19}$$
并非有未知分母的相反比较。

准确出处为 Mestre, *La méthode des graphes. Exemples et applications*, 1986，Theorem 3；原稿公开转录本将有关公式列为 §3 Theorem 3.3。为固定基、权重和强 Weil 规范，同时核准已发表 Kazalicki–Kohen (2017), §1 Theorem 3：其前文明确 $v$ 各整坐标 gcd 为一，$w_i=|\operatorname{Aut}(E_i)|/2$，且素水平的 congruence number 等于强 Weil 曲线的最小模参数化次数。此处从一开始选该最优曲线 $B$，不把任意同源曲线的有理扭点数混入公式。

## 6. 自含的模参数化次数下界

**引理 153.2。** 对 $p>37$，任何定义于 $\mathbb Q$ 的非常值映射
$$\phi:X_0(p)\longrightarrow B$$
其中 $B/\mathbb Q$ 是导子为 $p$ 的椭圆曲线，都满足
$$\boxed{\deg\phi\ge\frac{p+1}{108}.}\tag{153.20}$$

### 6.1 在 $\mathbb F_{25}$ 上构造足够多的源点

取
$$E_0/\mathbb F_5:\quad y^2=x^3+1.$$
其判别式在特征五非零。逐一代入 $x=0,1,2,3,4$，右侧为 $1,2,4,3,0$；对应仿射点数为 $2,0,2,0,1$，加无穷远点得
$$\#E_0(\mathbb F_5)=6.$$
所以 Frobenius $\pi_5$ 的迹为零，且椭圆曲线 Frobenius 恒等式给
$$\pi_5^2=[-5].\tag{153.21}$$
因此 $\mathbb F_{25}$ Frobenius 在 $E_0[p]$ 上为标量 $-5$。全部 $p+1$ 条 $\mathbb F_p$ 直线均稳定，分别定义 $\mathbb F_{25}$ 上的循环阶 $p$ 子群方案，故给出 $X_0(p)(\mathbb F_{25})$ 的点。

在特征五，$j(E_0)=0$ 的几何自同构群阶为六；显式为 $u^6=1$ 时的 $(x,y)\mapsto(u^2x,u^3y)$。其中 $\{\pm1\}$ 保持每条 $p$ 线，所以其在这些直线上的轨道大小至多三。两对 $(E_0,C)$ 代表同一个几何粗模点，当且仅当被这样的自同构相连。因此
$$
\#X_0(p)(\mathbb F_{25})\ge\left\lceil\frac{p+1}{3}\right\rceil
\ge\frac{p+1}{3}.
\tag{153.22}
$$
这里只需构造这些点，不声称它们遍历全部 $\mathbb F_{25}$ 点。每个子群已在 $\mathbb F_{25}$ 定义，故没有另行假定“模域等于定义域”。

### 6.2 好约化后次数不变

因 $5\ne p$，$X_0(p)$ 和 $B$ 均在五处好约化。先用有理尖点 $\infty$ 作 Abel–Jacobi 映射，将 $\phi$ 写为到 $J_0(p)$ 的映射、同态 $J_0(p)\to B$ 和平移的复合。好约化的 abelian scheme 同态由 Néron 性质延拓，Abel–Jacobi 映射及平移也延拓，因此得到光滑 proper 模型上的态射。

拉回目标零截面的次数一线丛。其在源的两个纤维上的次数相同，等于泛纤维映射次数 $d=\deg\phi>0$。故特殊纤维态射仍非常值，次数仍为 $d$。即使它不可分，也是一条曲线到另一条曲线的有限次数 $d$ 映射，每个几何纤维的不同点数至多 $d$。不需无分歧或可分假设。

Hasse 界给
$$\#B(\mathbb F_{25})\le25+1+2\sqrt{25}=36.$$
结合 (153.22)，
$$
\frac{p+1}{3}\le\#X_0(p)(\mathbb F_{25})
\le d\,\#B(\mathbb F_{25})\le36d.
$$
引理得证。

将 (153.17)、(153.19)、(153.20) 相连：
$$
\frac{p+1}{108}\le d_B\le\|v\|^2<\frac{12Mh}{p}.
$$
即得 (153.4)。这个次数下界不援引任何未发表次数估计，也不要求五处 Manin constant 为单位。

## 7. 所有二次序的显式类数上界

为保留 (153.5) 的常数，给出非极大序及单位指数的全部接口。

令 $D=D_K<0$，$w_K=|\mathcal O_K^\times|$，$w_{\mathcal O}=|\mathcal O^\times|$。Voight (2021), Theorem 25.2.12 及 (25.2.17) 给已发表的域类数公式
$$h_K=\frac{w_K\sqrt{|D|}}{2\pi}L(1,\chi_D).\tag{153.23}$$
环类 exact sequence 的有限核为
$$
\mathcal O_K^\times/\mathcal O^\times
\longrightarrow
(\mathcal O_K/c\mathcal O_K)^\times/(\mathbb Z/c\mathbb Z)^\times
\longrightarrow
\operatorname{Pic}(\mathcal O)
\longrightarrow\operatorname{Pic}(\mathcal O_K)\longrightarrow1.
$$
该核可由 prime-to-$c$ 理想的延伸、收缩得到：映到主 $\mathcal O_K$ 理想的类由一个模 $c$ 可逆生成元表示；有理模 $c$ 单位及全局 $\mathcal O_K$ 单位正是等价关系。

对 $q^e\Vert c$，CRT 及分裂、惰性、分歧三种局部整数环分别给
$$
\frac{|(\mathcal O_K/q^e\mathcal O_K)^\times|}
{|(\mathbb Z/q^e\mathbb Z)^\times|}
=q^e\left(1-\frac{\chi_D(q)}q\right).
$$
因此
$$
h=h_K\frac{w_{\mathcal O}}{w_K}
c\prod_{q\mid c}\left(1-\frac{\chi_D(q)}q\right).
\tag{153.24}
$$
这是整个导子的公式，包括二、三及 $q\mid D$，没有省略单位指数。

由于 $\eta$ 阶三，$h\ge3$。有额外单位的虚二次序只能是最大序 $\mathbb Z[i]$ 或 $\mathbb Z[\zeta_3]$，两者均 Euclidean 且类数一；故这里 $w_{\mathcal O}=2$。令 $\chi_{-M}$ 为模 $M=|D|c^2$ 的 Kronecker 角色。它是将 $\chi_D$ 在 $q\mid c$ 处置零的诱导角色，且非主。由 (153.23)–(153.24)，
$$
\boxed{h=\frac{\sqrt M}{\pi}L(1,\chi_{-M}).}
\tag{153.25}
$$

这个角色以 $M$ 为周期，每一周期总和为零。置 $A(t)=\sum_{n\le t}\chi_{-M}(n)$，则 $A(M)=0$、$|A(t)|\le M$。分部求和给
$$
\left|\sum_{n>M}\frac{\chi_{-M}(n)}n\right|
\le\int_M^\infty\frac{M}{t^2}\,dt=1.
$$
又 $\sum_{n\le M}\chi_{-M}(n)/n\le H_M\le\log M+1$，故
$$
\boxed{h\le\frac{\sqrt M}{\pi}(\log M+2).}
\tag{153.26}
$$
结合 (153.4) 得 (153.5)。若 $M<p^2$，使用 $\log M+2<2\log p+2$ 即得 (153.6)。若 $M\ge p^2$，(153.6) 的右侧小于 $p^2$，所以同样成立。这也给出所述绝对有效的 $p^{4/3}/(\log p)^{2/3}$ 下界。

## 8. 接到实际秩零商及 R150 分母平方整除

现在另设 $(K,c,\eta)$ 来自 R66 的实际小惯性完整非分裂正规化子分支。按 R69，对 $\mathcal F_\eta$ 中的每个完整 Galois 轨道，已发表中心值公式、代数周期的 Galois 性和 Bertolini–Darmon 秩零定理给出实际完整水平扭曲曲线的秩零商。

把这些商取乘积，取实际 Jacobian 的像，再以连通核最优化。不同 Hecke 轨道的泛纤维微分独立；每个轨道贡献三色标准表示的两倍维数，故该商维数为
$$2|\mathcal F_\eta|.$$
其有理点有限，R72 控制最优商的饱和整微分格。因此在 (153.7) 的任一范围内，并保留那里要求的非消失前提时，R150 §8.1 的两个真实归一化形式条件成立。

沿 R137、R150 记 $J_p$ 为实圆分整数环中的实际三色共同理想、$N(J_p)$ 为其绝对范数。对任意同一模 $p$ 表示的实际曲线 $F$，写
$$\operatorname{den}(j(F))=D_F^p.$$
则
$$
\boxed{D_F^2\mid N(J_p).}
\tag{153.27}
$$
配合 R137 Parseval 界，还得
$$
\log\operatorname{den}(j(F))
\le\frac{p(p-1)}8
\log\left(\frac{2p}{9}-\frac{4}{9(p-1)}\right).
\tag{153.28}
$$
这里没有证明 $a_2$ 在非零谱上非恒定，故不擅自把平方整除加强为立方。四个已解小水平的共同理想为单位是 R92、R109 的更强独立结论，本结果不以扩大小水平计算作为证明。

## 9. 保留的缺口与准确新增部分

本结果排除的是给定真实非零三次周期只具有一个有理 Hecke 特征分量的过小判别式情形。新增内容为 (153.15) 的全颜色整格约束、(153.16) 的不可任意缩放、以及 (153.4) 的模次数增长。没有从形式三颜色计数直接断言 Mordell–Weil 秩。

若 $P_\eta=0$，所有 $\kappa$ 论证和范数下界都失去非零向量，不能使用本定理排除该分支。可先用 R76、R81、R83、R86 或 R87 的一个精确非消失范围验证前提，但不可将这些范围删去。若只有一条有理谱线且 $M$ 大于本下界，本文也未给矛盾。

本文的范围是环类判别式 $M=|D_K|c^2$，不是商二次域判别式本身。变化 $K$、变化 $c$ 的全局控制仍需新输入。

## 10. 来源与可复核位置

- R76 §§2–3、§6：真实 Picard 纤维到共同 $p$ 取向嵌入的注入；完整 Brandt 谱；Cai–Shu–Tian (2014), Theorem 1.2 的精确本题接口。
- R83 §5，式 (83.17)：不依赖周期是否为零的球帽纤维界；本文 §3 重新写出全部计算。
- J.-F. Mestre, *La méthode des graphes. Exemples et applications*, in *Proceedings of the International Conference on Class Numbers and Fundamental Units of Algebraic Number Fields*, Nagoya University, 1986, pp. 217–242，Theorem 3。公开原文转录：[mestre-fr.pdf](https://wstein.org/papers/rank4/mestre-fr.pdf)，§3 Theorem 3.3（转录编号）。
- M. Kazalicki and D. Kohen, *Supersingular zeros of divisor polynomials of elliptic curves of prime conductor*, Research in the Mathematical Sciences **4** (2017), article 10，§1 Theorem 3 及紧前的原始向量、配对、强 Weil 次数定义：[原刊全文](https://link.springer.com/article/10.1186/s40687-017-0099-8)。用于固定 (153.18) 的规范；未援引同文提到的 Watkins 次数下界。
- J. Voight, *Quaternion Algebras*, GTM 288, Springer, 2021，Theorem 25.2.12、式 (25.2.17)：[原刊第 25 章](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_25)。非极大序的单位指数及局部因子在本文 §7 另行证明。
- R69、R72、R137、R150：实际商、整微分、同一实际尖点及原始圆分根、第二频率与 Parseval 分母界。
