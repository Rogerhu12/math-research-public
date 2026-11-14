# 反圆分临界值的固定 Kronecker 对角：导子迹、周期与代数微分系统

**状态：本文中的公式与边界已证明；无穷素数非消失仍未证明。**
日期：2026-11-12。会话：Astra-rank2-Sha / cm_iwasawa_routes。

本文继续 [R40](../results/R40-anticyclotomic-second-coefficient-and-full-selmer.md)。
R40 已将 $\Sha(E/\mathbb Q)[p^\infty]$ 有限性无条件归约为
**实际反圆分 Katz 分支**的二阶系数非零，并给出高权中心临界值的有限证书。
下面把那些中心临界值接到一个与 $p$ 无关的双变量级数，写全两个阶乘、
导子范数、普通 $p$-进周期和两个 Euler 因子。

## 1. 固定的曲线、导子轨道与 Kronecker 级数

固定
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),\qquad
\omega=\frac{dx}{2y},\qquad f=34(1+i),\qquad \mathfrak f=f\mathbb Z[i].
\tag{1}
$$
令 $\psi$ 为该曲线的 Hecke 字符。取与 $\omega$ 相应的复均匀化
$$
E(\mathbb C)=\mathbb C/\Gamma,\qquad
\Gamma=\Omega_E\mathbb Z[i]=\Omega\mathfrak f,\qquad
\Omega=\Omega_E/f.
\tag{2}
$$
这里 $\Omega_E>0$，且
$x(z)=\wp(z;\Gamma),\ y(z)=\wp'(z;\Gamma)/2$。
已有 CM 导子计算给出
$$
F=K(E[\mathfrak f]),\qquad [F:K]=256,
$$
而 $P_f$ 对应 $z_f=\Omega\pmod\Gamma$。
记 $\mathcal S$ 为 $P_f$ 的 $256$ 个 $K$-Galois 共轭。

更具体地，若 $\mathfrak a$ 遍历模 $\mathfrak f$ 的 ray class 代表，
则这些点可写为
$$
z_{\mathfrak a}=\psi(\mathfrak a)\Omega\pmod\Gamma.
\tag{3}
$$
在类数一的情形，这确是 ray class 的 $256$ 个代表。
**不**把它换成 $(\mathcal O_K/\mathfrak f)^\times$ 的全部 $1024$ 个元素；
后者在这里会把每个 $\psi$-规范生成元重复四次。

令
$$
A=A(\Gamma)=\frac{\operatorname{area}(\mathbb C/\Gamma)}{\pi_{\mathbb C}},
\qquad
A(\mathfrak f)=\frac{N\mathfrak f}{\pi_{\mathbb C}},\qquad N\mathfrak f=2312.
\tag{4}
$$
下标 $\pi_{\mathbb C}$ 表示通常的实数圆周率，避免与稍后的 Frobenius
生成元 $\pi=\psi(\mathfrak p)$ 混淆。
方格周期格的 $s_2(\Gamma)=0$，所以其 reduced theta 就是
标准 Weierstrass $\sigma$，记作 $\sigma(z)$。

使用 Bannai–Kobayashi（下简称 BK）的规范
$$
\Theta_{z_0,0}(z,w)
=\exp\left(-\frac{w\bar z_0}{A}\right)
\frac{\sigma(z+z_0+w)}{\sigma(z+z_0)\sigma(w)}.
\tag{5}
$$
其在 $w=0$ 的留数为 $1$，在 $z_0$ 换一个 $\Gamma$-代表时不变。
定义**固定**双变量 Taylor 级数
$$
\mathscr K(z,w)
=\sum_{S\in\mathcal S}\Theta_{z_S,0}(z,w)-\frac{256}{w},
\qquad
d_m=[z^m w^m]\mathscr K(z,w)\quad(m\ge0).
\tag{6}
$$
所有 $S$ 均非零，所以除去显示的 $w$ 极点后，$\mathscr K$ 在 $(0,0)$ 正则。

## 2. 精确的复值公式：一次 ray-class 迹、一个 $m!$

BK Theorem 1.17 给出
$$
\Theta_{z_0,0}(z,w)
=\frac1w+
\sum_{a\ge0,\ b>0}
\frac{(-1)^{a+b-1}}{a!A^a}
e^*_{a,b}(z_0,0)\,z^{b-1}w^a.
\tag{7}
$$
取 $a=m,b=m+1$，符号为 $+1$，因此
$$
d_m=\frac{1}{m!A^m}
\sum_{S\in\mathcal S}e^*_{m,m+1}(z_S,0).
\tag{8}
$$

这里的迹可以直接核准，而不借助有时混入单位数的写法。
对每个与 $\mathfrak f$ 互素的整理想 $\mathfrak b$，
$\psi(\mathfrak b)$ 是该理想的唯一 $\psi$-规范生成元。
这些生成元恰好由 (3) 中的剩余类加上 $\mathfrak f$ 遍历一次。
于是先在绝对收敛区域加上 $|\beta|^{-2s}$，再解析延拓到 $s=0$，有
$$
\begin{aligned}
\sum_{S\in\mathcal S}e^*_{m,m+1}(z_S,0)
&=\frac{\bar\Omega^m}{\Omega^{m+1}}
\sum_{(\mathfrak b,\mathfrak f)=1}
\frac{\overline{\psi(\mathfrak b)}^{\,m}}
     {\psi(\mathfrak b)^{m+1}}\\
&=\frac{\bar\Omega^m}{\Omega^{m+1}}
L_{\mathfrak f}(\bar\psi^{\,2m+1},m+1).
\end{aligned}
\tag{9}
$$
这个推导也是 BK Proposition 1.6(i) 在本曲线上的直接版本。
因为 $A=\Omega\bar\Omega A(\mathfrak f)$，得到
$$
\boxed{\quad
m!d_m
=A(\mathfrak f)^{-m}\Omega^{-(2m+1)}
L_{\mathfrak f}(\bar\psi^{\,2m+1},m+1).
\quad}
\tag{10}
$$
复共轭理想的置换说明这里的 $L$ 值也等于
$L_{\mathfrak f}(\psi^{2m+1},m+1)$。
这是中心点 $m+1$；它与 R24 中的
$L_{\mathfrak f}(\bar\psi^{2p-1},2p-1)$ 是不同的值。

## 3. 级数及其迹属于固定代数域

为避免只凭复公式宣称 Galois 相容性，给出一个直接的代数说明。
设
$$
U_S=E_1^*(z_S)=\zeta(z_S)-\bar z_S/A.
$$
整数 $68$ 杀掉 $E[\mathfrak f]$，故 $[69]S=S$。
令 $\Psi_{69}$ 是标准奇数 division function，满足
$$
\frac{\sigma(69z)}{\sigma(z)^{69^2}}=\Psi_{69}(x(z),y(z)).
\tag{11}
$$
两边可有相同的固定规范常数；以下对数导数不依赖该常数。
因 $S$ 不是 $69$-torsion，$\Psi_{69}(S)\ne0$。
对 (11) 取导数，并用 $69z_S-z_S\in\Gamma$ 及
$\eta(\lambda)=\bar\lambda/A$，得到
$$
\boxed{\quad
U_S=-\frac{1}{69\cdot68}
\frac{\delta\Psi_{69}}{\Psi_{69}}(S),
\qquad
\delta x=2y,\quad \delta y=3x^2-17.
\quad}
\tag{12}
$$
因此 $U_S\in F$，且 $U_{S^\tau}=\tau U_S$ 对每个
$\tau\in\operatorname{Gal}(F/K)$ 成立。

定义单变量函数
$$
F_S(z)=
\exp(-z\bar z_S/A)\frac{\sigma(z_S+z)}{\sigma(z_S)},
\qquad F_S(0)=1.
\tag{13}
$$
它满足
$$
\frac{F'_S(z)}{F_S(z)}=U_S(z),\quad
U'_S(z)=-X_S(z),\quad X'_S(z)=2Y_S(z),\quad
Y'_S(z)=3X_S(z)^2-17,
\tag{14}
$$
初值为 $(U_S,x(S),y(S))$。
式 (12)、(14) 说明 $F_S\in F[[z]]$，且所有系数与 Galois 作用相容。
又有精确恒等式
$$
\Theta_{z_S,0}(z,w)=\frac{F_S(z+w)}{F_S(z)\sigma(w)}.
\tag{15}
$$
由于 $\sigma(w)\in w\mathbb Q[[w]]$，可得
$$
\mathscr K(z,w)\in K[[z,w]],\qquad d_m\in K.
\tag{16}
$$
这与 BK Corollary 2.10 的一般代数性相容，但这里还证明了精确的
$F/K$ 迹，而不是仅把系数放进一个较大的 torsion 域。

对目标素数 $p\ge13$, $p\equiv1\pmod4$, $p\ne17$，
$69\cdot68$ 是 $p$-单位。良约化和 prime-to-$p$ torsion 约化的单射性
说明 $S$ 不约化到 $O$，且不约化到 $69$-torsion。
故 $x(S),y(S),\Psi_{69}(S)$ 均 integral，最后一项是单位。
特别地，(12) 给出每个目标素位的 $U_S$ 整性。

## 4. Katz 规范：第二坐标取逆，两个 Euler 因子完全相同

固定目标素数 $p$ 及 $\mathfrak p\mid p$，写
$$
\pi=\psi(\mathfrak p),\qquad \bar\pi=\psi(\bar{\mathfrak p}),
\qquad \pi\bar\pi=p,
\qquad v_p(\pi)=1,\ v_p(\bar\pi)=0.
\tag{17}
$$

**测度规范。** 下面另记 $\mu^\Theta_{\mathfrak p}$ 为
BK §3.3，Definitions 3.8–3.9 的 theta/Katz 测度，
其中有限层求和明确采用 (3) 的 $256$ 个 ray class 代表。
其 Theorem 3.11（也可直接用 Proposition 3.10 的 lattice sum）
给出这一规范的完整插值式。
不按每个插值字符重新选择 Agboola–Howard 的 $\alpha_{\mathfrak p}$；
本节末单独证明两个**完整测度**在所需分支上相差 Iwasawa 单位。
使用与 (2) 相容的 $p$-进周期 $\Omega_p$：它按 BK pp.39–40 的
Weil pairing 条件选定，并满足
$$
\eta_p(t)=\exp(\Omega_p^{-1}\log_E(t))-1:
\widehat E\overset\sim\longrightarrow\widehat{\mathbb G}_m.
\tag{18}
$$
这里是在最大非分歧扩张的整数环完备化 $\mathcal O$ 上取同构。
因 (18) 是整形式群同构，切空间系数必须是单位，因此
$$\Omega_p\in\mathcal O^\times.$$
不是在计算完数值后任意选择一个周期来改变赋值。
改变相容的微分或 torsion 基时，必须同时改变 (2)、(18) 和测度坐标。

在这一规范中，BK Definition 3.8 的关键变换是
$$
\int f(\alpha)\,d\mu^K(\alpha)
=\Omega_p\int_{\mathbb Z_p^\times\times\mathbb Z_p^\times}
f(x,y^{-1})x^{-1}\,d\widetilde\mu(x,y),
\tag{19}
$$
而 $\widetilde\mu$ 在第二 theta 坐标中带 $[N\mathfrak f]$ 的伸缩。
因此 $(m+1,-m)$ 型的 Galois 字符在 theta 测度中给出的矩是
$x^my^m$，不是 $x^{m+1}y^{-m}$；(19) 同时解释了下面额外的一次
$\Omega_p$ 和 $(N\mathfrak f)^m$。

设 $m\ge1$ 且 $p-1\mid m$。令
$$
\varepsilon_m=\psi^{m+1}\bar\psi^{-m},
\qquad \varepsilon_m^{-1}=\bar\psi^{\,2m+1}N^{-(m+1)}.
\tag{20}
$$
其无穷型为 $(m+1,-m)$，并且有限导子仍为 $\mathfrak f$。
具体地，$4\mid m$，而 $\psi$ 的有限部分取值于 $\mu_4$，
所以其在 (20) 中的指数 $2m+1$ 同余于 $1\pmod4$。

在 $\mu^\Theta_{\mathfrak p}$ 上作与 R40 相同的 $\psi_{\mathfrak p}$
扭转及反圆分投影，记所得整级数为 $F^{\Theta,-}_p(T)$，并记
$$
V^\Theta_{p,m}=F^{\Theta,-}_p\big((1+p)^m-1\big).
\tag{21}
$$
因 $p-1\mid m$，Teichmüller 部分的 $m$ 次幂为 $1$，所以 (21)
正是 $\varepsilon_{m,p}$ 的 Katz 插值值。
BK Theorem 3.11 在 $k=m+1,l=m$、无 $p$-进有限阶角色的情形给出
$$
V^\Theta_{p,m}
=\Omega_p^{2m+1}m!\,
\frac{\pi_{\mathbb C}^{\,m}}{\Omega^{2m+1}}
\left(1-\frac{\varepsilon_m(\mathfrak p)}p\right)
L_{\mathfrak f\bar{\mathfrak p}}(\varepsilon_m^{-1},0).
\tag{22}
$$
右边按该定理的代数性规范送入 $\mathbb C_p$；
没有单独把一个普通复周期当成 $p$-进数。
这里先只断言 $\mu^\Theta$ 的精确公式，而不把它与 R40 中的数值
$V_{p,m}$ 逐值等同。

在 (22) 中，两处 Euler 因子分别为
$$
1-\frac{\varepsilon_m(\mathfrak p)}p
=1-\frac{\pi^m}{\bar\pi^{m+1}},
\qquad
1-\varepsilon_m^{-1}(\bar{\mathfrak p})
=1-\frac{\pi^m}{\bar\pi^{m+1}}.
\tag{23}
$$
第二项来自删去 $\bar{\mathfrak p}$ 的 Euler factor。
因为 $m\ge1$，它们均在 $1+p\mathcal O$ 中，特别是单位。
利用 (10)、$\pi_{\mathbb C}A(\mathfrak f)=N\mathfrak f$，(22) 成为
$$
\boxed{\quad
V^\Theta_{p,m}
=\Omega_p^{2m+1}(m!)^2(N\mathfrak f)^m
\left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2 d_m.
\quad}
\tag{24}
$$
这是固定导子轨道的实际中心值公式。两个 $m!$ 分别来自
Kronecker Taylor 系数 (7) 和 Katz 的 $\Gamma(m+1)$ 因子，不能删去。

### 4.1. 与 R40 的同一完整 Iwasawa 分支比较

下面说明为什么 (24) 的赋值门槛确实适用于 R40，而非仅适用于一个
逐值重新规范化的函数。

BK §3.2 的 Theorem 3.7 及其证明末尾（印刷页 39–40）明确将所构造的
theta 测度识别为 Yager §9 的测度。Agboola–Howard Theorem 2.2.1
则以同一 Yager 映射将局部单位模与其像理想 $J$ 同构，并将实际椭圆
单位映为 $(\sigma_{\mathfrak a}-N\mathfrak a)\mu_{\mathfrak p}$。
其 Propositions 2.3.1/2.3.4 给出所需扭转后的整版本。

这里需要处理 BK 文字中一个不影响理想、却会影响精确数值的规范问题。
Definition 3.6 先对 ray classes 求和，随后又写成对
$(\mathcal O_K/\mathfrak f)^\times$ 求和；对本曲线，后一个求和把
同一个 $\psi$-规范点重复 $|\mu_K|=4$ 次。其证明中也出现 $|\mu_K|$。
本文的 $d_m$ 与 (24) 始终使用前一个、一次的求和。
如果按后一种字面 Yager 求和读数，**整个测度**乘上固定常数 $4$。
这个比较在所有字符上是同一次乘法，而不是逐值选择。
由于 $p\ge13$，$4$ 是单位。

BK Definitions 3.8–3.9 从该 Yager theta 测度到 Katz 测度的另外几项
变化也都有完整测度的解释：

- $y\mapsto y^{-1}$ 是单位群的群自同构；
- $x^{-1}$ 是固定连续单位字符的扭转；
- 第二 theta 坐标中的 $[N\mathfrak f]$ 对单位群测度是由固定单位
  $N\mathfrak f$ 给出的平移，即乘一个 group-like Iwasawa 单位；
- $\Omega_p$ 是 (18) 的固定整切空间单位。

前两项是将 Yager 的正次数坐标 $(b-1,a)$ 转成 Katz 的型
$(k,j)=(b,-a)$ 的同一坐标识别，正由 (19) 核对。
它们在 Agboola–Howard 的角色和扭转约定中必须一并进行；
不会将本文的 $\psi_{\mathfrak p}$ 分量换成共轭的另一分量。
后两项和可能的 $4$ 倍只改变共同 Coleman/Yager 像理想的单位生成元。

为把“单位”严格放在中心，取实际二变量局部环
$$
\mathscr R=\mathcal O[[X,Y]]
$$
并先按 R40 移到 $\psi_{\mathfrak p}$ 中心。
取辅助理想 $\mathfrak a=(7)$。其 Yager 因子在中心的值为
$$
\psi((7))-N(7)=-7-49=-56\in\mathcal O^\times.
\tag{24a}
$$
因而该分支上的 $J$ 等于 $\mathscr R$。
两种上述整坐标的 Coleman/Yager 映射，都是从**同一个秩一自由局部
单位模**到 $\mathscr R$ 的同构。
取该模任一基 $e$，两个像均为 $\mathscr R$ 的单位，
故两映射的比是一个 $\mathscr R^\times$ 元素。
对同一条 $\mathfrak a=(7)$ 椭圆单位应用它们，再除去 (24a) 的
Iwasawa 单位因子，即得到
$$
\mathcal L^\Theta_{E,\mathfrak p}
=\mathcal U_p(X,Y)\,\mathcal L_{E,\mathfrak p},
\qquad \mathcal U_p\in\mathscr R^\times.
\tag{24b}
$$
其中固定 $4$ 倍、切空间单位和 group-like 因子均已吸收进
$\mathcal U_p$；不需要、也没有声称它恒为 $1$。

代入反圆分坐标 $(X,Y)=(T,(1+T)^{-1}-1)$，得
$$
F^{\Theta,-}_p(T)=U^-_p(T)F^-_p(T),
\qquad U^-_p\in\mathcal O[[T]]^\times.
\tag{24c}
$$
其中心值 $U^-_p(0)$ 是单位，且对每个
$t=(1+p)^m-1\in p\mathcal O$ 都有
$U^-_p(t)\equiv U^-_p(0)\pmod p$，仍为单位。
所以中心零阶及所有本文实际插值点的赋值都被保留：
$$
\operatorname{ord}_T F^{\Theta,-}_p=\operatorname{ord}_T F^-_p,
\qquad
v_p(V^\Theta_{p,m})=v_p(V_{p,m}).
\tag{24d}
$$
这一步使用了共同的完整 Coleman/Yager 构造及整同构，
不从“两个函数都插值某些非零复数”推断其比为单位。

## 5. 对主问题的直接后果

所有显示的周期、导子和 Euler 因子都是目标处的单位，
且完整测度比较 (24d) 保留赋值，所以 (24) 给出
$$
v_p(V_{p,m})=2v_p(m!)+v_p(d_m),
\qquad m\ge1,\quad p-1\mid m.
\tag{25}
$$
这里 $v_p(d_m)$ 用 (17) 固定的嵌入读取。
特别地，令 $m=p-1$，则
$$
\boxed{\quad v_p(V_{p,p-1})=v_p(d_{p-1}).\quad}
\tag{26}
$$
R40 的全 Selmer 主项和奇偶性因而给出：
$$
d_{p-1}\notin p^4\mathcal O
\quad\Longrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}.
\tag{27}
$$
而已知的 Mordell–Weil 秩 $2$ 强制 $d_{p-1}\in p^2\mathcal O$。
目前没有证明 (27) 对无穷多个目标 $p$ 成立。

为了包括 R40 的完整有限证书，设 $m_n=(p-1)p^n$。
Legendre 公式给出
$$
v_p(m_n!)=p^n-1.
$$
因此有无条件等价
$$
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\quad\Longleftrightarrow\quad
\exists n\ge0:\
v_p(d_{(p-1)p^n})+2(p^n-1)<4(n+1).
\quad}
\tag{28}
$$
当 $n\ge1$ 时，$d_{(p-1)p^n}$ 本身可能有 $p$-进分母。
不能把 (26) 的“阶乘是单位”沿用到这些后续权。

还有一个不依赖 (24) 的最低权整性检验。
BK Corollary 2.17 给出
$$
\Theta_{z_S,0}(\log_E(s),\log_E(t))-1/t\in\mathcal O[[s,t]].
$$
形式指数 $\exp_E(z)$ 到次数 $p-1$ 的系数均 integral：
它由整形式群微分方程递推，而这些次数只需除以 $1,\ldots,p-1$。
把它代回上式，$1/\exp_E(w)-1/w$ 这一误差与 $z$ 无关。
故 $z^{p-1}w^{p-1}$ 的系数 integral，证明 $d_{p-1}\in\mathcal O$。
这个论证没有预设待证的 Sha 有限性。

## 6. 一个固定代数微分系统及完全明确的对角递推

在固定代数
$$
\mathcal R=K[U,X,Y]/(Y^2-X^3+17X)
$$
上取导子
$$
\mathcal D U=-X,\qquad
\mathcal D X=2Y,\qquad
\mathcal D Y=3X^2-17.
\tag{29}
$$
定义
$$
C_0=1,\qquad C_{n+1}=\mathcal D C_n+UC_n.
\tag{30}
$$
例如
$$
\begin{aligned}
C_1&=U,\\
C_2&=U^2-X,\\
C_3&=U^3-3UX-2Y,\\
C_4&=U^4-6U^2X-8UY-3X^2+34.
\end{aligned}
$$
由 (14) 直接归纳，
$$
F_S(z)=\sum_{n\ge0}C_n(U_S,x(S),y(S))\frac{z^n}{n!}.
\tag{31}
$$
再定义固定有理数
$$
q_j=[w^j]\frac{w}{\sigma(w)},
\qquad q_0=1,\quad q_4=\frac{17}{60},\quad q_j=0\quad(4\nmid j).
\tag{32}
$$
令 $\operatorname{ev}_f$ 表示在 $(U_{P_f},x(P_f),y(P_f))$ 处取值。
对每个 $m\ge1$，(15)、(30) 给出可直接复算的有限式
$$
\boxed{\quad
d_m=\frac1{m!}
\sum_{j=0}^{m+1}
\frac{q_j}{(m+1-j)!}
\operatorname{Tr}_{F/K}
\left(\operatorname{ev}_f\big(\mathcal D^m C_{m+1-j}\big)\right).
\quad}
\tag{33}
$$
证明是先把 (15) 的 $w^{m+1}$ 分子系数取出，
再沿 $z$ 的流施加 $\mathcal D^m/m!$。
减去的 $256/w$ 不影响任何 $m\ge0$ 的对角系数。
当 $m=0$ 时，直接得到 $d_0=\operatorname{Tr}_{F/K}U_{P_f}=0$；
最后的零值已在 R18 用解析秩零定理严格核准。

式 (29)–(33) 是真正**与 $p$ 无关**的有限代数微分系统。
它没有声称 $d_m$ 满足固定阶数的线性递推：
$C_n$ 含首项 $U^n$，其次数随 $n$ 增长；同时 (33) 的导数阶数也增长。
把 $17$ 暂作权为 $4$ 的参数、赋予 $U,X,Y$ 权 $1,2,3$，
则 $C_n$ 的权为 $n$，$\mathcal D$ 将权提高 $1$。
这精确说明了需要随对角索引增长的多项式空间。

## 7. 为什么固定域、固定系统还不是固定有限线性 Frobenius 证书

在 $\mathcal S$ 处先取值，会把所有系数放入固定有限域 $F$，
但 $\mathcal D$ **不能**据此降成 $F$ 上的一个固定有限矩阵。
理由很直接：$\operatorname{ev}_f$ 的核并不被 $\mathcal D$ 保持。
例如在代数闭包中，某点的极大理想含 $X-x(S)$、$Y-y(S)$，
但 $\mathcal D(X-x(S))=2Y$ 在 $S$ 的值为 $2y(S)\ne0$。
所以必须保留点附近的 jet，不能先模掉点的理想再微分。
这与 R6、R29 的有限 jet 边界是同一个具体问题在新对角上的表现。

这里也不能把 $U$ 在有限个初值处的代数表达式 (12)，直接替换成
一个在整个曲线上满足 $dU=-x\omega$ 的有理函数。
后者将使非零 de Rham 类 $[x\omega]$ 变成 exact，矛盾。
式 (12) 只确定 torsion 初值，(29) 仍需保留其向量扩张方向。

可以进一步严格排除**整个双级数**的 D-finite 性。
固定一个足够小且 $w\notin\Gamma$ 的复数 $w$。
作为 $z$ 的函数，每个 $\Theta_{z_S,0}(z,w)$ 在
$z=-z_S+\lambda$、$\lambda\in\Gamma$ 有简单极点，留数为
$$
\exp\left(\frac{w(\bar\lambda-\bar z_S)}{A}\right)\ne0.
\tag{34}
$$
不同 $S$ 模 $\Gamma$ 不同，所以这些极点不会在求和时相消。
减去 $256/w$ 也不改变它们。
故 $\mathscr K(z,w)$ 对这样的 $w$ 有无穷多个 $z$-极点。

若 $\mathscr K$ 是双变量 D-finite 级数，则它关于 $z$ 满足一个
非零的 $K(z,w)$ 系数线性微分方程。
清分母后，除了有限个使所有系数同时退化的 $w$，
可将它专化为一个非零 $\mathbb C(z)$ 系数方程。
其解只能在最高阶系数的有限零点及无穷远处出现奇点，
与 (34) 矛盾。因此 $\mathscr K$ 不是双变量 D-finite。

这个结论**没有**排除对角 $\sum_m d_m Z^m$ 单独 D-finite，
没有排除 prime-diagonal 的特殊模 $p^4$ 公式，
也没有排除由其他几何对象产生的有限维 Frobenius 比较。
它只表明：从 (29)–(33) 的有限个变量或固定数域，不能直接推出
本题所需的固定有限线性递推及跨素数非零性。

## 8. 下一条实际算术问题

本笔记把待研究量明确成
$$
d_{p-1}\in p^2\mathcal O,
\qquad
\text{需要对无穷多个 split }p\text{ 证明 }d_{p-1}\notin p^4\mathcal O.
\tag{35}
$$
这是一条固定 $K$-值序列上的新中心对角，保留了反圆分角色；
它不是先前普通范数中消掉 $\chi$ 的那个固定单位。
另一方面，(24) 说明它与 R40 的二次矩完全相同，
因此仅重写成 (33) 不会自动产生非零性。
后续可研究这条具体对角的 Cartier/热方程关系或本曲线的实际 theta
平方根因式；必须保留 (24) 的周期和两个阶乘。

Rodriguez Villegas 的 *On the Taylor coefficients of theta functions of CM
elliptic curves* §§3–4 详细处理的是 Gross 曲线
$A(11),A(19),A(43),A(67),A(163)$。
其已展示的平方根测度不能不经额外证明移到 (1) 的 $K=\mathbb Q(i)$
及四次导子字符；普通中心复 $L$ 值非零也不能替代 (35)。

## 主要外部输入

- Bannai–Kobayashi，*Algebraic theta functions and the p-adic interpolation
  of Eisenstein–Kronecker numbers*，Duke Math. J. **153** (2010)。
  本文使用 Theorem 1.17、Proposition 1.6、Corollaries 2.10/2.17，
  以及 §3.3 Definitions 3.8–3.9、Theorem 3.11。
  [作者 arXiv 全文](https://arxiv.org/pdf/math/0610163)。
- Agboola–Howard，*Anticyclotomic Iwasawa theory of CM elliptic curves*，
  Ann. Inst. Fourier **56** (2006), 1001–1048，Theorem 2.1.1、
  Remark 2.1.2 以及 R40 已逐项核准的 Yager–Coleman/主猜想比较。
  [正式全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
- Rodriguez Villegas，*On the Taylor coefficients of theta functions of CM
  elliptic curves*，§§3–4，仅用于说明已核查的平方根公式范围。
  [作者全文](https://frvillegas.github.io/pdf/frv-cm-theta.pdf)。
