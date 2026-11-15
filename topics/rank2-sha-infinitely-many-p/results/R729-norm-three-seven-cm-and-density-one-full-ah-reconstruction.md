# R729 — 范数三、七的原小 CM 来源与密度一全 Artin–Hasse 恢复

日期：2026-11-15。**状态：以下准确小同源分布、共同阶的密度一界及原整个高度二窗的唯一恢复已证明。**

本篇以原范数3和范数7同源替换 R723 的31、43输入。
原 sigma、Gaussian 规范、Fermat 商、Artin–Hasse 坐标和全部指定行不变。
只需原 $X(w)$ 与一个固定的线性 division 多项式；
实际同源的次数为3和7，不把其 pullback 认作旧预算的免费自映射。

## 1. 两个准确的原 sigma 恒等式

保持
$$
E:y^2=x^3+b,\quad b=17,\quad
K=\mathbf Q(\delta),\quad \delta^2=-3,\quad
\omega=(-1+\delta)/2,
$$
$$
p=6s-1>101,\quad q=p^2,\quad L=(q-1)/6=s(p-1),
\quad w=z^6,\quad X(w)=z^2x(z),
$$
$$
c=[w^s]\log(\sigma/z),\qquad
U(w)=(\sigma(z)/z)e^{-cw^s},\qquad [w^s]\log U=0.
\tag{1}
$$
第三原来源仍另保 $p>136$。
取同一 K 中固定元素
$$
\alpha_3=\delta,\qquad
\alpha_7=\gamma=3+\omega=(5+\delta)/2,
\qquad N(\alpha_3)=3,\quad N(\alpha_7)=7.
\tag{2}
$$
全部剩余域约化在原 $k=\mathbf F_{p^2}$，好 p 自动不除3、7、b。

准确的 division 身份是
$$
\boxed{\quad
\frac{\sigma(\delta z)}{\sigma(z)^3}=\delta x(z),
\qquad
\frac{\sigma(\gamma z)}{\sigma(z)^7}
 =\gamma\left(x(z)^3+a_7b\right),
\quad a_7=\frac{-2+6\delta}{7}.
\quad}
\tag{3}
$$
第二式是 R297(5) 的原已付 CM7 函数，完整 leading constant 和共轭方向不变。

为支付第一式，在原 equianharmonic 格上，
准周期的反线性形式和 $\delta\bar\delta=3$
使分子与分母的指数准周期相消。
奇范数的原半特征亦相同；或者用
$\delta=1+2\omega\equiv1\bmod2$ 直接核半特征。
比值为偶椭圆函数，只在 O 有二阶极，故属于 $Kx+K$。
原 $\mu_3$ 作用下其型与 x 相同，常数项必须为零；
首项是 $\delta z^{-2}$，于是第一式成立。
这里没有额外的二次指数、待定 Weil 相位或新平坦特征。

## 2. 原 Gaussian 与全部有限指数

对 $i=3,7$，写 $N_3=3,N_7=7$，并定义
$$
\tau_i=\bar\alpha_i^6,\qquad
R_3(w)=X(w),\qquad
R_7(w)=X(w)^3+a_7bw,
$$
$$
t_i=c\{N_i-\alpha_i^{p+1}\}.
\tag{4}
$$
上横线在 $\tau_i$ 中表示模 p 约化，不表示复共轭；
复共轭将显式写为 $\alpha_i^{\mathrm{conj}}$。
由 (3) 除去实际首因子 $\alpha_i z$，得到特征零的准确式
$$
\boxed{\quad
U(\alpha_i^6w)=U(w)^{N_i}R_i(w)\exp(t_iw^s).
\quad}
\tag{5}
$$
例如范数3的有理因子正是
$z^2x(z)=X(w)$，不要求 $N_i\equiv1\bmod6$；
范数7则是 $z^6(x^3+a_7b)=X^3+a_7bw$。
两种指数和首项归一都已在 (5) 中显示。

p 惰性给
$\alpha_i^p\equiv\alpha_i^{\mathrm{conj}}\bmod p$，
所以 $N_i-\alpha_i^{p+1}$ 被 p 整除。
原 $v_p(c)=-1$ 因而保证 $t_i$ 整。
又因原 $[w^s]\log U=0$，比较 (5) 的同一对数行，精确有
$$
\boxed{\quad t_i=-[w^s]\log R_i.\quad}
\tag{6}
$$
$s<p$，所以此有限对数只除单位。
(6) 保留完整的实际 Fermat 商，并不是将其设成零或另选提升。

在 R717 的完整原整窗口中，约化 (5) 得
$$
\boxed{\quad
\bar U(\tau_iw)
 =\bar U(w)^{N_i}\bar R_i(w)
       \mathcal E_{\bar t_i}(w)\pmod{w^L},
\qquad
\mathcal E_t(w)=\sum_{j=0}^{p-2}\frac{t^jw^{sj}}{j!}.
\quad}
\tag{7}
$$
这里只使用 $sj<L$ 的项，所以恰到 $j=p-2$，
全部阶乘为单位。
整数幂3、7的全部交叉项仍保留。
不存在隐藏的 $N_i\bmod p^2$ 输入，因为 $N_i$ 是这两个实际固定小整数；
也没有将通用 Artin–Hasse 级数改成普通有限指数。

准确有
$$
\tau_i^s=N_i\in\mathbf F_p^\times.
\tag{8}
$$
定义本篇共同六次群的真实阶
$$
e_{3,7}(p)=
 |\langle\tau_3,\tau_7\rangle|
 \quad\text{于 }\mathbf F_{p^2}^\times.
\tag{9}
$$
它整除 L。

## 3. 一个秩二范数群和一个反范数方向已经足够

置
$$
\rho=\gamma/\gamma^{\mathrm{conj}}\in K^\times.
$$
它不是单位根。
事实上 $(\gamma)$ 和 $(\gamma^{\mathrm{conj}})$ 是7上不同的素理想：
若相同，该素理想也整除
$\gamma-\gamma^{\mathrm{conj}}=\delta$，
与 $N(\delta)=3$ 矛盾。
故 $\rho$ 在这两个素理想的赋值分别为1、−1。

对好惰性 p，记
$$
n_p=|\langle3,7\rangle\subset\mathbf F_p^\times|,
\qquad
a_p=\operatorname{ord}_p(\rho).
\tag{10}
$$
$a_p\mid p+1$，因为 $\rho$ 的范数为一。

以下直接证明所需的两个初等小阶计数。
取区间 $X\le p\le2X$，X 充分大。

### 3.1 范数群的小阶例外

若 $n_p\le X^{3/5}$，
取 $Y=\lfloor X^{3/10}\rfloor+1$。
$(Y+1)^2>X^{3/5}$ 个元素
$3^i7^j$（$0\le i,j\le Y$）
在该群中必有碰撞。
因此存在不全为零的整数 a、b_0，满足
$|a|,|b_0|\le Y$ 且
$$
3^a7^{b_0}\equiv1\bmod p.
$$
p 整除固定非零整数
$$
A_{a,b_0}
 =3^{a_+}7^{(b_0)_+}-3^{a_-}7^{(b_0)_-}.
$$
它非零由3、7的乘法独立性给出。
这些整数的数量为 $O(Y^2)$，
每个 $\log\max(1,|A_{a,b_0}|)=O(Y)$。
将全部非零因子相乘，所得整数的对数为 $O(Y^3)$。
每个坏 p 至少贡献 $\log X$，故
$$
\boxed{\quad
\#\{X\le p\le2X:n_p\le X^{3/5}\}
 =O(X^{9/10}/\log X).
\quad}
\tag{11}
$$
常数绝对依赖于固定3、7；没有用原根猜想。

### 3.2 单个反范数方向的小阶例外

若 $a_p\le X^{9/20}$，
则某个 $1\le j\le\lfloor X^{9/20}\rfloor$ 满足
$$
\gamma^j\equiv(\gamma^{\mathrm{conj}})^j\bmod(p).
$$
每个差都是非零代数整数，其绝对范数是非零整数，且
$$
\log\left|N_{K/\mathbf Q}
       \bigl(\gamma^j-(\gamma^{\mathrm{conj}})^j\bigr)\right|
 =O(j).
$$
这是因为两个复嵌入下 $|\gamma|=\sqrt7$；
非零性由 $\rho$ 不是单位根保证。
全部 $j\le X^{9/20}$ 的这些范数的乘积，
对数为 $O(X^{9/10})$。
每个坏惰性 p 整除其中某个范数，
所以
$$
\boxed{\quad
\#\{X\le p\le2X:a_p\le X^{9/20}\}
 =O(X^{9/10}/\log X).
\quad}
\tag{12}
$$
惰性时范数实际上含 $p^2$，但证明只使用较弱的 $\log X$ 下界。

### 3.3 两个像的准确合并

令
$$
G_p=\langle\bar\delta,\bar\gamma\rangle
       \subset\mathbf F_{p^2}^\times,\qquad g_p=|G_p|.
$$
其范数像正是 $\langle3,7\rangle$，阶为 $n_p$。
其反范数像由 $-1$ 和 $\rho$ 或 $\rho^{-1}$ 生成，
阶至少为 $a_p$，并整除 $p+1$。
两像的阶都整除 $g_p$，彼此的最大公因子至多二。
所以
$$
g_p\ge n_pa_p/2.
$$
(9) 是 $G_p$ 的六次幂像，核至多六。
因此有准确的统一下界
$$
\boxed{\quad e_{3,7}(p)\ge n_pa_p/12.\quad}
\tag{13}
$$
不能在这一步把两个像的阶无条件相乘；因子12已支付其交与六次幂核。

由 (11)–(13)，除区间内
$O(X^{9/10}/\log X)$ 个素数外，
所有惰性 p 都满足
$$
\boxed{\quad
e_{3,7}(p)>X^{21/20}/12.
\quad}
\tag{14}
$$
特别对充分大的 X，
$e_{3,7}(p)\ge(p+1)/6=s$。
惰性素数的通常算术级数素数定理
与 $X^{9/10}/\log X=o(X/\log X)$
表明这个集合在惰性素数中密度一，因而无穷。
可沿用 R720 的同一 dyadic 合并，
有限原坏集不改变该结论。

较一般地，范数秩二的阈值可取任意 $\beta<2/3$，
单个反范数方向可取任意 $\gamma_0<1/2$。
只要 $\beta+\gamma_0>1$ 即够本篇全窗恢复。
显示的 $3/5,9/20$ 只为了使两类例外具有同一个 $9/10$ 幂。

## 4. 两个真实二位族的共同共振

R717 的完整原分解仍是
$$
U(w)=\prod_{1\le n<L}\mathscr E_p(a_nw^n)\pmod{w^L}.
\tag{15}
$$
原第一位 $\bar X_n$ 已经确定除以下两族外的全部坐标：
$$
\mathcal A_p=\{pk:1\le k<s\},\qquad
\mathcal B_p=\{s+pk:1\le k<s\},
$$
并确定原 gauge 坐标 $\bar a_s=0$。
确定行仍使用
$\bar a_n=-\bar X_n/[6n(6n-1)]$，
不改变原除商。

(8) 与 Frobenius 给
$$
\boxed{
\begin{aligned}
\tau_3^{pk}=3,\quad\tau_7^{pk}=7
 &\iff e_{3,7}(p)\mid k-s,\\
\tau_3^{s+pk}=3,\quad\tau_7^{s+pk}=7
 &\iff e_{3,7}(p)\mid k.
\end{aligned}}
\tag{16}
$$
第一式对原两等式取 p 次幂：
$\tau_i^{p^2k}=\tau_i^k$，而 $N_i^p=N_i=\tau_i^s$。
第二式先消去 $\tau_i^s=N_i$，再用 Frobenius。
这与 R723 是同一真实共振判据，不是改了未知坐标。

因为 $1\le k<s$，
$$
\boxed{\quad
e_{3,7}(p)\ge s
\ \Longrightarrow\
\mathcal A_p\cup\mathcal B_p
\text{ 中每行至少一个实际 CM 分母 }\tau_i^n-N_i\ne0.
\quad}
\tag{17}
$$
其它行即使共振，也已经由原 AH 坐标确定。

## 5. 整个原高度二窗的唯一恢复

**定理。** 在 (17) 的范围，同一原
$$
\bar X\bmod w^L,\qquad
\bar a_s=0,\qquad
\text{全部原已确定 AH 行},
$$
连同准确的两条小分布式
$$
\bar U(\bar\delta^6w)
 =\bar U^3\bar X\,\mathcal E_{\bar t_3},
$$
$$
\bar U(\bar\gamma^6w)
 =\bar U^7(\bar X^3+\bar a_7bw)
                   \mathcal E_{\bar t_7}\pmod{w^L}
\tag{18}
$$
唯一决定原 $\bar U\bmod w^L$。

存在性就是原 sigma 满足 (3)–(7) 及 R717；
没有对任意数据另加可解性假设。
若有两解，取首个不同 AH 坐标 n。
首个不同普通 U 系数也正好是 n。
已确定 AH 行排除其它 n，
故 n 在 $\mathcal A_p\cup\mathcal B_p$。
比较 (18) 的第 n 行给
$$
(\tau_i^n-N_i)\Delta_n=0\qquad(i=3,7).
$$
(17) 迫 $\Delta_n=0$，矛盾。

恢复算法也完全与原坐标相容：
已知 AH 行按完整 $\overline{\mathscr E}_p$ 的单位三角展开加入；
遇两未知族时，以 (17) 中某个非零分母的 CM 行
计算当前真实 U 系数，再取回当前 AH 坐标。
原解的存在确保另一条分布式和所有未选行自动相容。
全部低非线性卷积及 Frobenius 项仍在，不取高阶普通对数。

由第3节，这个全窗定理在密度一的惰性素数集合上成立。
相比 R723，额外的固定 division 输入已缩为
$$
\boxed{\quad R_3=X,\qquad R_7=X^3+a_7bw.\quad}
\tag{19}
$$
完整 Fermat 商通过 (6) 留在实际低行中；
通用 Artin–Hasse 级数仍须按其真实整数定义使用。

## 6. 回到全部原 Cartier 与原预算

R721 已给原 $\bar X\bmod w^L$ 的准确有理读取；
R725 则用同一个 $\bar U$ 定义共同平方和直接不变量模型。
因此本篇 (18) 唯一指定 R725 的全部
$Q_m(\xi)$、原完整 $\phi_m$ 的首 Cartier 行，
以及其按前 K 行缩短后的实际分子。
没有从三个不同的自由 U 分别构造模型。

实际同源 degree 从31、43降为3、7。
任何进一步把这些 pullback 或 division 比加入原角格的论证，
仍必须核其真实极点、十九角、原 Gaussian 与同一个修正。
本篇不将较小 degree 自动等同于旧 $\mathcal W_D$ 保持。

原 $j_m=0$ 到 R708 前缀、R710 的全部 carry、
指定条目的非零及固定曲线无穷 p 的全 Sha 目标，仍需继续证明。

依赖：
[R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)；
[R717](R717-original-height-two-artin-hasse-return-and-second-digit-support.md)；
[R720](R720-two-fixed-cm-sources-and-density-one-resonance-window.md)；
[R721](R721-minimal-two-torsion-poles-for-original-height-two-parameter.md)；
[R723](R723-fixed-cm-and-artin-hasse-full-height-two-reconstruction.md)；
[R725](R725-original-window-common-square-and-low-pole-return.md)。
