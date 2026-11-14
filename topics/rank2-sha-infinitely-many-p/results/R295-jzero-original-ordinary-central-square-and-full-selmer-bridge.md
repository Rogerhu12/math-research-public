# R295 — 新 j=0 原来源的完整普通中央平方及全部 Selmer 比较

日期：2026-11-13。**状态：以下同一原来源的普通整测度、全部周期和 Euler 比较、整条反圆分支平方、完整 Selmer 下界及有理有限证书均已证明。这里给出新固定曲线的充分判据，没有把 MW 秩或单个复临界值非零当作跨素数结论。**

## 1. 固定对象与结论

固定 $E:y^2=x^3+17$、$K=\mathbf Q(\delta)$，其中
$\delta=\sqrt{-3}$、$\omega=(-1+\delta)/2$。R294 已完整证明
$\operatorname{rank}E(\mathbf Q)=2$。R290 给出本曲线的实际 Hecke 特征
$\psi$、导子 $\mathfrak f=(34\delta)$、原 Schwartz 函数及全权平方。
R292、R297 识别的首项一实际来源是
$$
\begin{aligned}
S(z)&=\sigma^{34}x^2P_4(x^3)=\sum_{m\ge0}s_mz^m,\\
P_4(X)&=(X+17)(X-136)
 \left(X^2-\frac{68}{7}X+\frac{4624}{7}\right),\\
s_6&=1,\qquad s_m\in\mathbf Q,\qquad s_m=0\ \text{unless }6\mid m.
\end{aligned}\tag{1}
$$
始终使用 $x=z^{-2}+\cdots,y=-z^{-3}+\cdots,\sigma=z+\cdots$。

取 $p>7$、$p\equiv1\pmod3$，故 $p$ 是本曲线的好普通素数。
固定 CM 嵌入，令
$\pi=\psi(\mathfrak p)$、$\bar\pi=\psi(\bar{\mathfrak p})$，
$v_p(\pi)=1,v_p(\bar\pi)=0,\pi\bar\pi=p$。
取下文相容的普通周期 $\Omega_p$。同一个原来源定义整测度
$$
\mathcal A_p(Z)=S(\Omega_p\log(1+Z))
=\int_{\mathbf Z_p}(1+Z)^x\,d\nu_p(x)
\tag{2}
$$
及单位区间 principal Mellin 变换
$$
G_p(T)=\int_{\mathbf Z_p^\times}
(1+T)^{\log_p\langle x\rangle/\log_p(1+p)}\,d\nu_p(x).
\tag{3}
$$
置固定代数数 $s=(1-\omega)^{-1}$。实际 Katz 反圆分支在 §3 的晶格周期规范下满足
$$
\boxed{
\mathcal K_p(T)=\frac{\kappa_0}{s}\Omega_p
(1+T)^{-a_{34,p}}G_p(T)^2,\quad
a_{34,p}=\frac{\log_p\langle34\rangle}{\log_p(1+p)},
\quad\kappa_0=48940416.
}\tag{4}
$$
常数由 R298 的真实 Kronecker resolvent 精确确定；证明平方和下界只需
$\kappa_0$ 固定非零。这里是一个真实来源的平方，没有另设独立的共轭测度。

记 $r_p=\operatorname{corank}_{\mathbf Z_p}\Sha(E/\mathbf Q)[p^\infty]$。则
$$
\boxed{G_p\ne0,\quad G_p(0)=0,\quad
2+r_p\le\operatorname{ord}_0\mathcal K_p=2\operatorname{ord}_0G_p.}
\tag{5}
$$
因此
$$
\boxed{G_p'(0)\ne0\ \Longrightarrow\
\Sha(E/\mathbf Q)[p^\infty]\text{有限}.}\tag{6}
$$
更明确地，令 $m_n=(p-1)p^n$、$h_m=m!s_m\in\mathbf Q$，则
$$
\boxed{G_p'(0)\ne0\quad\Longleftrightarrow\quad
\exists n\ge0:\ v_p(h_{m_n})<2n+2.}\tag{7}
$$
右边是同一个固定有理级数的有限证书，不含未知周期。
本篇不声称 (6) 的逆命题，也未证明 (7) 对无穷多个素数成立。

## 2. 普通 sigma 与同一个整测度

令 $t=-x/y$、$D=d/\omega_E$、$\omega_E=dx/(2y)$。
Mazur–Tate 的普通 sigma 唯一性定理给唯一的奇级数
$\Sigma_p=t+\cdots\in t\mathbf Z_p[[t]]$ 和 $c_p\in\mathbf Z_p$，满足
$$D^2\log\Sigma_p=-x-c_p.\tag{8}$$
采用 Mazur–Stein–Tate Theorem 1.3 的明确表述即可。
因为 $\omega\in\mathbf Z_p$，真实 CM 自同构给
$t([\omega]P)=\omega t(P)$、$x([\omega]P)=\omega x(P)$、
$[\omega]^*\omega_E=\omega\omega_E$。
将 $\Sigma_p$ 换成 $\omega^{-1}\Sigma_p(\omega t)$，
链式法则使 (8) 的常数变成 $\omega^2c_p$。新级数仍奇、整且首项一，
所以唯一性迫使 $c_p=\omega^2c_p$，即 $c_p=0$。

固定 Weierstrass 级数 $\sigma(\log_Et)$ 满足同一方程及奇性、首项条件；
特征零中两个积分常数由这些条件确定。因此
$$\boxed{\Sigma_p(t)=\sigma(\log_Et)\in t\mathbf Z_p[[t]].}\tag{9}$$
没有为每个 $p$ 新加一个二次指数。由 (1)，各项
$\Sigma_p^{34}x^{2+3j}$（$0\le j\le4$）在 $t=0$ 的阶为
$30-6j\ge6$，全部 Laurent 系数整。固定分母七已排除，故
$S(\log_Et)\in t^6\mathbf Z_p[[t]]$。

在完备最大不分歧整环 $R_0$ 上取相容的高度一正式群同构
$\beta:\widehat{\mathbf G}_m\to\widehat E$，以
$\beta^*\omega_E=\Omega_p\,dZ/(1+Z)$ 定义单位 $\Omega_p$。
则 $\log_E\beta(Z)=\Omega_p\log(1+Z)$，所以 (2) 属于 $R_0[[Z]]$。
Amice 对应给出整测度及全部准确矩
$$M_{p,m}:=\int_{\mathbf Z_p}x^m\,d\nu_p
                 =\Omega_p^m m!s_m.\tag{10}$$
阶乘来自指数生成函数，不能删去。

## 3. 实际 Hermite、晶格周期和固定平方常数

令 $\Omega>0$ 为 R290/R292 的实尺度，使
$$
\operatorname{Per}(E,\omega_E)=\Omega\Lambda,\quad
\Lambda=\mathbf Z+s\mathbf Z=s\mathcal O_K.
$$
Katz 使用的晶格生成周期取
$$\Omega_\infty=s\Omega,\qquad
\operatorname{Per}(E,\omega_E)=\Omega_\infty\mathcal O_K.\tag{11}$$
$\Omega_p$ 与此 CM 数据和同一微分相容。这里使用 de Shalit 的实际晶格周期；
若使用记号 $\Omega_K=(2\pi i)^{-1}\int\omega_E$，须先换算
$\Omega_\infty=2\pi i\Omega_K$。Castella–Wan 的已出版
Remark 2.2、Theorem 2.4 明确区分两者；不能把 $2\pi i$ 当作代数单位吸收。

原 Hermite 函数准确为
$$
\mathcal B(t)=C\,S(\Omega h t),\quad
h=\frac{\sqrt{51\sqrt3}}{204\pi i},\quad C\in\mathbf R^\times.
\tag{12}
$$
这保留 R292 的完整 Gaussian 和 R297 的首项一规范。
若 $\mathcal B(t)=\sum b_mt^m/m!$，则
$b_m=Cm!s_m(\Omega h)^m$。R290 的全部范数式给
$$
L(\psi^{2m+1},m+1)
=C_{17}^{(0)}\frac{(4\pi)^m}{m!}b_m^2,\quad
C_{17}^{(0)}=
\frac{\pi\sqrt{102\sqrt3}}
 {153\sqrt3(3+\sqrt3)(17-\sqrt{17})}
\tag{13}
$$
对所有 $6\mid m$ 成立。因 $4\pi h^2=-\sqrt3/(204\pi)$，得到
$$
\frac{(2\pi/\sqrt3)^m L(\psi^{2m+1},m+1)}
 {m!\Omega^{2m+1}}
=\kappa_0\,102^{-m}s_m^2,\quad
\kappa_0=\frac{C_{17}^{(0)}C^2}{\Omega}>0.
\tag{14}
$$
$(-1)^m$ 因 $6\mid m$ 恰为一。准确地
$s^2=-\omega^2/3$，所以 $s^{2m}=3^{-m}$。因此
$$
\boxed{
\mathcal E_m:=
\frac{(2\pi/\sqrt3)^m L(\psi^{2m+1},m+1)}
 {m!\Omega_\infty^{2m+1}}
=\frac{\kappa_0}{s}\,34^{-m}s_m^2.
}\tag{15}
$$
$s^{-1}=1-\omega$ 和 $34^{-m}$ 必须同时保留。
CM 代数性及 $s_6=1$ 已给
$\kappa_0=s\,34^6\mathcal E_6\in\overline{\mathbf Q}^{\times}$；
R298 进一步用真实 48 项 Kronecker resolvent 得到 (4) 中的精确整数，
没有以数值认数确定它。

## 4. 全部插值与整条反圆平方

令
$$\epsilon_m=\psi^{m+1}\bar\psi^{-m}
             =\psi^{2m+1}\mathrm N^{-m}.\tag{16}$$
它具有 infinity type $(m+1,-m)$。对 $6\mid m$，
R290 已逐个坏位证明其导子仍为 $\mathfrak f$，包括三处统一化元相位。
由 $\psi\bar\psi=\mathrm N$ 及全部理想的复共轭换元，
$$L(\epsilon_m^{-1},0)=L(\bar\epsilon_m,1)
                     =L(\psi^{2m+1},m+1).\tag{17}$$
在晶格周期 (11) 的 Katz/de Shalit 规范下，$p-1\mid m$ 时
$$
\mathcal K_p(t_m)=\Omega_p^{2m+1}m!
\frac{(2\pi/\sqrt3)^m}{\Omega_\infty^{2m+1}}
\left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2
L(\psi^{2m+1},m+1),\qquad t_m=(1+p)^m-1.
\tag{18}
$$
这是一般插值的 $k=m+1,j=-m$ 特例：固定有限导子版本见
Agboola–Howard Theorem 2.1.1，晶格周期版本见
Castella–Wan Theorem 2.4。两个 Euler 因子准确为
$$1-\epsilon_m(\mathfrak p)/p
=1-\epsilon_m^{-1}(\bar{\mathfrak p})
=1-\pi^m/\bar\pi^{m+1}.\tag{19}$$
导子准确等于 $\mathfrak f$，故没有额外坏位删除因子；
所用代数字符在 $p$ 上未分歧，故该处 Gauss 因子为一。

同一分支也由原 ray class 测度先扭转 $\psi_{\mathfrak p}$，再沿
$\langle\psi_{\mathfrak p}/\bar\psi_{\mathfrak p}\rangle$ 推前定义。
这是实际反圆方向的非零切向参数。
若采用逆 Artin/对偶约定，须同时作
$T\mapsto(1+T)^{-1}-1$；本文固定 (16)–(18)，不逐权重重选单位。
将 (10)、(15) 代入 (18)，对正的 $p-1\mid m$ 得
$$
\boxed{\mathcal K_p(t_m)=
\frac{\kappa_0}{s}\Omega_p\,34^{-m}
\left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2M_{p,m}^2.}
\tag{20}
$$
一个 $m!$ 来自 Katz，另一个来自 (13)，恰好组成 $(m!s_m)^2$。

整测度的非单位部分满足
$$v_p\left(M_{p,m}-\int_{\mathbf Z_p^\times}x^m\,d\nu_p\right)\ge m.
\tag{21}$$
(19) 与一的差也有至少 $m$ 的赋值。固定 $p-1\mid m_0\ge0$，取
$m_j=m_0+(p-1)p^j$；它实趋于无穷、$p$-adic 趋于 $m_0$。
在 (20) 中取极限，(21) 和 Euler 误差趋于零，而单位矩趋于
$G_p(t_{m_0})$，$34^{-m_j}\to\langle34\rangle^{-m_0}$。
故 (4) 在所有这些点成立；取互异点趋于零，解析恒等定理给整条 (4)。
总质量 $S(0)=0$ 尚不单独确定 $G_p(0)$；下一节支付其真实单位质量。

## 5. 完整通常 Selmer 下界

### 5.1 真正主猜想比较的假设

$K$ 类数一：虚二次 Minkowski 界 $(2/\pi)\sqrt3<2$，
每个理想类都有范数一代表。$E/K$ 有全部最大整环 CM，$p>3$ 且好普通。
R290 的完整局部根数乘积为 $+1$。ray class 次数为
$$
[K(\mathfrak f):K]
=\frac{3468}{6}\left(1-\frac14\right)
 \left(1-\frac13\right)\left(1-\frac1{289}\right)=288.
\tag{22}
$$
只有根单位一同余于一模 $\mathfrak f$，分母确为六；故这些 $p$ 都不整除它。

Agboola–Howard Theorem 2.4.17(1)(b),(c) 适用于这个具体对象：
反圆扩张 $D_\infty/K$ 上通常单 CM 初级 Selmer 对偶 $X(D_\infty)$
为 torsion Iwasawa 模，特征理想由该 Katz 分支生成。
这里是通常 $X$，不是严格局部条件的 $X_{\rm str}$。
其 Theorem 2.1.1、Proposition 2.3.4 保留实际插值分支、对偶作用及周期。
若 Coleman 定义带辅助理想因子，可取 $(5)$：
$\psi((5))=-5$、$N(5)=25$，中心因子 $-30$ 对所有本篇素数为单位。
所以这个因子不增加中心零。

采用 (18) 的相容周期和参数后，特征生成元与 $\mathcal K_p$ 相差一个
中心非零的解析单位；若交换 CM 分量，同时进行已经说明的对偶反演。
这来自整条测度的比较，不是逐值任意单位。于是 $\mathcal K_p\ne0$。
以下只需这一已出版的通常 Selmer 特征理想比较，不需要任何未证高度非退化。

### 5.2 基层通常 Selmer 的限制单射

令 $S_K^\pi=\operatorname{Sel}_{\pi^\infty}(E/K)$，
$S_{D_\infty}^\pi$ 同理，局部条件为全部地方的 Kummer 像。
限制映射给
$$
S_K^\pi\longrightarrow
(S_{D_\infty}^\pi)^{\operatorname{Gal}(D_\infty/K)}.
\tag{23}
$$
这里核为零。全局 inflation–restriction 的核包含在
$H^1(\operatorname{Gal}(D_\infty/K),E(D_\infty)[\pi^\infty])$。
在 $\mathfrak p$ 处，CM 的 $\pi$ 分量是高度一连通正式群；
非零一阶挠点的 tame inertia 角色为模 $p$ 圆分角色，像阶 $p-1$。
pro-$p$ 扩张不能使它平凡，故
$E(D_\infty)[\pi]=0$，进而 $E(D_\infty)[\pi^\infty]=0$。
共轭分量在 $\bar{\mathfrak p}$ 处完全相同。
各局部 Kummer 像在限制下保持，所以 (23) 确为通常 Selmer 单射。

本证明只需这条单射，不把负根数附录中的高度结论用于当前正根数曲线。
取 Pontryagin 对偶及有理化，得到
$$
\operatorname{corank}_{\mathbf Z_p}S_K^\pi
\le\dim_{\mathbf Q_p}
 \left(X(D_\infty)/TX(D_\infty)\right)\otimes\mathbf Q_p
\le\operatorname{ord}_0\mathcal K_p.
\tag{24}
$$
第二个不等式是初等 Iwasawa 模论：在高度一素理想 $(T)$ 局部化，
torsion 模分解为 $\bigoplus_i A/(T^{e_i})$；中心维数为块数，
特征阶为 $\sum_i e_i$。有限模及其它支撑在此处消失。
实际反圆权参数与所选群生成元之间的导数非零，故不改变零阶。

### 5.3 准确回到全 $p$ 初级

R294 的三次同源目标是
$$E':Y^2=X^3-459=E^{(-3)}.$$
同源与对偶复合为 $[3]$。由于 $p>7$，它们在全 $p^\infty$ Galois 模、
全部局部 Kummer 像和通常 Selmer 上给同构。限制与核心限制又因 $p\ne2$ 给
$$
\operatorname{Sel}_{p^\infty}(E/K)
\simeq\operatorname{Sel}_{p^\infty}(E/\mathbf Q)
\oplus\operatorname{Sel}_{p^\infty}(E^{(-3)}/\mathbf Q).
\tag{25}
$$
两项余秩均为 $2+r_p$。另一方面
$\mathcal O_K\otimes\mathbf Z_p=\mathbf Z_p\oplus\mathbf Z_p$
将左边分解成两个 CM 初级部分，复共轭交换它们，故余秩相同。因此
$$\boxed{\operatorname{corank}S_K^\pi=2+r_p.}\tag{26}$$
没有把 $E(K)$ 的秩四当作单 CM 分量的秩，也未删任何 Sha 自由方向。

(24)、(26) 与完整平方 (4) 共同证明 (5)：
$\mathcal K_p\ne0$ 使 $G_p\ne0$，而中央阶至少二强迫 $G_p(0)=0$。
若 $G_p'(0)\ne0$，则 $\operatorname{ord}\mathcal K_p=2$，故 $r_p=0$。
通常 Selmer 有限余生成，其 Sha 商亦有限余生成；余秩零等价于有限。
这证明 (6)，不需要先假设全 Sha 有限。

## 6. 固定有理系数的完整有限证书

由 (21)，$m_n=(p-1)p^n$ 时
$$
\Omega_p^{m_n}h_{m_n}=G_p(t_{m_n})+e_n,\quad
v_p(e_n)\ge m_n,\quad v_p(t_{m_n})=n+1.
\tag{27}
$$
最后一个等式为提升指数公式。
若 $G_p'(0)=0$，由 (5) 有 $G_p\in T^2R_0[[T]]$，
故 $v_p(G_p(t_{m_n}))\ge2n+2$。
$m_n\ge2n+2$ 且 $\Omega_p$ 为单位，给
$v_p(h_{m_n})\ge2n+2$ 对全部 $n$ 成立。

反之若 $G_p'(0)\ne0$，取 $n+1>v_p(G_p'(0))$，则
$$v_p(G_p(t_{m_n}))=n+1+v_p(G_p'(0))<2n+2.$$
增大 $n$ 后 (27) 的误差不能取消首项，故得到 (7)。
同时有真实极限
$$
\boxed{G_p'(0)=\lim_{n\to\infty}
\frac{\Omega_p^{m_n}h_{m_n}}{(1+p)^{m_n}-1}.}
\tag{28}
$$
未知周期不妨碍 (7)，因为只比较赋值且该周期为单位。
又 $G_p\in TR_0[[T]]$ 已给 $v_p(h_{m_n})\ge n+1$；
首层充分证书因此简写为
$$v_p(h_{p-1})=1\quad\Longrightarrow\quad
\Sha(E/\mathbf Q)[p^\infty]\text{有限}.\tag{29}$$
例如，(1) 的前两项直接由
$ x=z^{-2}-(17/7)z^4+O(z^{10})$ 和
$\log(\sigma/z)=(17/210)z^6+O(z^{12})$ 得到
$$s_{12}=17\left(\frac{34}{210}-\frac{14}{7}-\frac{53}{7}\right)
=-\frac{988\cdot17}{105}=-\frac{4\cdot13\cdot19\cdot17}{105}.$$
故 $v_{13}(12!s_{12})=1$，(29) 无条件给出
$\Sha(E/\mathbf Q)[13^\infty]$ 有限。
这是固定低阶系数的一个有限应用，不是无穷性输入。

没有由有限素数样本声称这个条件无穷次成立。

## 7. 真实来源接口与所余问题

R297 中的同一来源满足
$$S=\frac{q^2v^2}{112\cdot17}\theta_-^{34}Q_8(q),\qquad v^3=1-q.$$
因此 R291/R299 的真实余项可用于研究 (7) 的原系数，
但须保留 $q^2,v^2,Q_8$、原参数转换及全局 Frobenius 因子。
原点恰六阶、全部固定挠点零除子、CM13 本征及分支非恒零
都不单独支付完整中央导数非零。待证的是这个同一固定来源的 (7)
对无穷不同素数命中，或另一个能控制全部 Selmer 的无穷输入。

## 已出版输入与本地证明

- A. Agboola、B. Howard，*Anticyclotomic Iwasawa theory of CM elliptic curves*，
  Ann. Inst. Fourier **56** (2006)，1001–1048，Theorem 2.1.1、
  Proposition 2.3.4、Theorem 2.4.17(1)：
  [出版全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
- F. Castella、X. Wan，*Perrin-Riou's main conjecture for elliptic curves at
  supersingular primes*，Math. Ann. **389** (2024)，2595–2636，
  Remark 2.2、Theorem 2.4：
  [出版全文](https://web.math.ucsb.edu/~castella/Perrin-Riou-print.pdf)，
  [DOI](https://doi.org/10.1007/s00208-023-02711-w)。
  本篇只用其中的 Katz 周期/插值定理，不用 supersingular 非 CM 主定理。
- E. de Shalit，*Iwasawa Theory of Elliptic Curves with Complex Multiplication*，
  Perspectives in Mathematics 3，Academic Press (1987)，II.4.14；
  上两篇出版文献所用的一般有限导子 Katz 规范。
- B. Mazur、J. Tate，*The p-adic sigma function*，Duke Math. J. **62** (1991)，
  663–688，[DOI](https://doi.org/10.1215/S0012-7094-91-06229-0)。
  唯一性用 B. Mazur、W. Stein、J. Tate，*Computation of p-Adic Heights and
  Log Convergence*，Documenta Mathematica Extra Volume Coates (2006)，
  Theorem 1.3：[作者出版稿](https://www.wstein.org/papers/pheight/pheight.pdf)。
- R288、R290、R292、R294、R297、R298：实际曲线、局部特征、全部平方常数、
  原 sigma frame、精确秩和唯一真实来源。R299 保真实参数校正。
