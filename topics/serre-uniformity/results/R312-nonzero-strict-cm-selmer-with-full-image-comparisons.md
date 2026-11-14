# R312：变化 CM 严格 Selmer 非零与满像比较曲线的同时实现

日期：2026-11-13。状态：**已证明；排除一条过强的全局消失路线，主要目标仍未完成。**

R306 把实际较深参数送进指定 CM 曲线的严格 $p$-Selmer 群。但不能期待该群仅由整三次参数、准确小惯性以及有限处局部匹配就统一为零。本篇构造无限多参数，使这个 CM 严格群含一个明确的非零 Mordell–Weil 类，同时比较曲线在任意指定有限集上具有相同完整局部 $p$ 挠点，却在全局具有完整 $\mathrm{GL}_2$ 像。

构造的比较曲线不是一致性猜想的反例。真正的全局模 $p$ 同构仍然缺失；本篇证明必须继续利用该同构及其传送的特定类，不能只证明变化 CM 严格 Selmer 群的普遍消失。

## 1. 完整构造定理

固定素数
$$
p>37,\qquad p\equiv2,5\pmod9,\qquad
m=
\begin{cases}
2,&p\equiv2\pmod9,\\
1,&p\equiv5\pmod9.
\end{cases}
\tag{312.1}
$$
给定任意有限有理素数集 $S\supseteq\{2,3,p\}$、
任意深度下界 $D\ge2$、任意 $\eta\in\{0,1\}$，
以及任意实数 $R>0$。

**定理 312.1。** 存在整数 $k\ge D$、$k\equiv\eta\bmod2$，
以及无穷多个整数 $a$，使以下全部性质同时成立。唯一写成
$$
r=1-a^3=db^3,\qquad
d>0\text{ 立方自由},\quad b\in\mathbb Z\setminus\{0\},
\tag{312.2}
$$
并令
$$
\begin{aligned}
H_a&:\ y^2=x^3+3ar\,x-r(2a^3-1),\\
C_a&:\ y^2=x^3+r,\qquad Q_a=(a,1)\in C_a(\mathbb Q).
\end{aligned}
\tag{312.3}
$$
则：

1. $4\mid a$、$a\ne0,1$、$\gcd(a,db)=1$，
   $v_p(d)=m$、$v_p(b)=k$，且
   $v_p(a-1)=m+3k$。
2. 对每个 $q\in S$，存在完整的实际局部同构
   $$
   H_a[p]\simeq C_a[p]\quad\text{于 }G_{\mathbb Q_q}.
   \tag{312.4}
   $$
3. 全局像不同：
   $$
   \rho_{H_a,p}(G_{\mathbb Q})=\mathrm{GL}_2(\mathbb F_p),
   \qquad
   \rho_{C_a,p}(G_{\mathbb Q})=N_{\mathrm{ns}}(p),
   \tag{312.5}
   $$
   而两条曲线在 $p$ 的惯性像均为 $C_{\mathrm{ns}}(p)^3$。
4. 它们的完整二除域相同，三除法的 $\mathrm{GL}_2(\mathbb F_3)/Q_8$
   商域也相同；这里不声称全部三挠点模同构。
5. 两条曲线的导子相同，而且有一个
   $q_\ast>R$、$q_\ast\equiv1\bmod3$ 满足
   $v_{q_\ast}(r)=v_{q_\ast}(d)=1$。特别共同导子至少为 $q_\ast^2$。
6. CM 曲线的严格 Selmer 群含明确非零类：
   $$
   \boxed{
   0\ne\delta_{C_a,p}(Q_a)
   \in\operatorname{Sel}_p^{\,0}(C_a/\mathbb Q).}
   \tag{312.6}
   $$
   这里严格条件恰为 $p$ 处的局部 $H^1$ 像为零，
   其余位置仍为通常 Kummer 条件。

所有量词都对固定的 $p,S,D,\eta,R$ 成立。
局部邻域和 Hilbert 估计的常数可以依赖这些数据；本篇不需要它们对 $p$ 一致。
这里的 $C_a$ 正是 R306 偶分支的指定符号，而不是另一条方便的 CM Jacobian。

## 2. 用一个辅助素数保证点在全局不是 $p$ 倍

**引理 312.2。** 存在素数 $\ell\notin S$、$\ell>3$ 以及
$a_\ell\in\mathbb F_\ell$，使
$$
\ell\equiv2\pmod3,\qquad
v_p(\ell+1)=1,\qquad
1-a_\ell^3\ne0,
\tag{312.7}
$$
且在
$C_\ell:y^2=x^3+1-a_\ell^3$ 上，
$(a_\ell,1)\notin pC_\ell(\mathbb F_\ell)$。

**证明。** 用中国剩余定理指定
$$
\ell\equiv p-1\pmod {p^2},\qquad
\ell\equiv2\pmod3,\qquad
\ell\equiv1\pmod2.
\tag{312.8}
$$
这个模 $6p^2$ 的类与模数互素。
Dirichlet 的等差数列素数定理给无穷多个这样的素数，
所以可避开 $S$ 及 $2,3$。
第一项使 $v_p(\ell+1)=1$。

在 $A_1:y^2=x^3+1$ 上，立方映射是
$\mathbb F_\ell$ 的双射，所以每个 $y\in\mathbb F_\ell$
恰对应一个 $x$。于是
$$
\#A_1(\mathbb F_\ell)=\ell+1.
\tag{312.9}
$$
取一个 $p$ 阶点 $T=(x_0,y_0)$。
它不在 $pA_1(\mathbb F_\ell)$ 中：
该有限群的 $p$-Sylow 群阶准确为 $p$，乘 $p$ 将这个因子杀掉。
又因 $p>3$，$T$ 既不是二挠点，也不是 $x=0$ 的三挠点，
所以 $y_0\ne0$、$x_0\ne0$。

立方双射给唯一 $u\in\mathbb F_\ell^\times$ 满足 $u^3=y_0$。
把坐标除以 $u^2,u^3$，得到同构
$$
A_1\simeq A_{u^{-6}},
\qquad T\longmapsto(a_\ell,1),
\qquad a_\ell=x_0/u^2.
\tag{312.10}
$$
原方程给 $1-a_\ell^3=u^{-6}\ne0$。
同构保持是否为 $p$ 倍，故所需结论成立。$\square$

此后强制整数参数满足
$$
a\equiv a_\ell\pmod\ell.
\tag{312.11}
$$
对任何这样的 $a$，$C_a$ 在 $\ell$ 好约化，且
$$
Q_a\notin pC_a(\mathbb Q).
\tag{312.12}
$$
否则把一个有理 $p$ 次原像在 $\ell$ 约化，
会与引理 312.2 矛盾。这里使用的是好约化的整个局部群约化映射，
不要求原像的仿射坐标预先为整。

## 3. $p$ 处任意深的同一个局部 $p$ 挠点模

先说明两个固定 CM 极限之间的真实局部同构。对任意
$s\in\mathbb Q_p^\times$，
$$
A_s[p]\simeq A_{-s}[p]\quad\text{于 }G_{\mathbb Q_p},
\qquad p\equiv2\bmod3,\ p>3.
\tag{312.13}
$$
确实，若 $p\equiv5\bmod12$，则 $-1$ 是 $\mathbb Q_p$ 中的平方，
二次扭曲 $-1$ 已平凡。
若 $p\equiv11\bmod12$，则 $3$ 是 $\mathbb Q_p$ 中的平方；
二次扭曲 $-1$ 与 $-3$ 在 $\mathbb Q_p$ 中相同。
标准的有理三同源 $A_s\to A_{-27s}=A_s^{(-3)}$
在 $p$ 挠点上为同构，因为 $p\ne3$。
这证明 (312.13)，不只比较迹或行列式。

固定所需奇偶 $\eta$，令
$$
e=m+3\eta\in\{1,2,4,5\},\qquad
a_j=1+p^{e+6j},\quad j=1,2,\ldots .
\tag{312.14}
$$
记
$$
u_j=\frac{1-a_j^3}{p^{e+6j}},
\qquad u_j\longrightarrow-3\quad\text{于 }\mathbb Q_p.
\tag{312.15}
$$
对 $H_{a_j}$、$C_{a_j}$ 都作
$x=p^{2j}X,y=p^{3j}Y$。缩放后的模型分别为
$$
\begin{aligned}
H_{a_j}^{\min}:\
Y^2&=X^3+3a_jp^{e+2j}u_jX
           -p^eu_j(2a_j^3-1),\\
C_{a_j}^{\min}:\
Y^2&=X^3+p^eu_j.
\end{aligned}
\tag{312.16}
$$
在 $\mathbb Q_p$ 的系数拓扑中，它们分别趋于光滑曲线
$$
A_{3p^e},\qquad A_{-3p^e}.
\tag{312.17}
$$
由 (312.13)，这两个极限的完整 $p$ 挠点模同构。

完整有限挠点模在局部域上的光滑曲线族中局部常值，
这里即使挠点素数与剩余特征相同也适用，因为底域特征为零。
具体地，取包含中心曲线所有 $p$ 挠点的有限 Galois 扩张。
乘 $p$ 的微分在底域可逆，每个挠点是单根；
隐函数定理在充分小且两两不交的邻域内唯一延拓各个挠点。
群运算与 Galois 作用都保持这些唯一分支，故给出完整 Galois 模同构。
R293 §2.1 已展开同一论证。

因此充分大 $j$ 时，(312.16) 的两个曲线有同一个局部 $p$ 挠点模。
增大 $j$，使
$$
k=2j+\eta\ge D.
\tag{312.18}
$$
再取一个足够小的完整整数同余邻域
$$
a\equiv a_j\pmod {p^M},\qquad M>e+6j,
\tag{312.19}
$$
使 (312.16) 对变动 $a$ 仍留在上述局部常值邻域。
对每个这样的 $a$，准确有
$$
v_p(a-1)=v_p(1-a^3)=e+6j=m+3k,
\qquad H_a[p]\simeq C_a[p]\text{ 于 }G_{\mathbb Q_p}.
\tag{312.20}
$$
没有把“$j$ 很接近零”单独当作挠点模同构的证明；
同构来自两个固定光滑极限及完整有限 étale 群的局部常值性。

## 4. 其余有限处、额外分裂素数和一个整数等差数列

对每个 $q\in S\setminus\{p\}$，在参数 $a=0$ 处两条曲线都为
$$
H_0=C_0=A_1.
\tag{312.21}
$$
它们作为 $\mathbb Q_q$ 上的曲线均光滑，
包括 $q=2,3$ 时的坏约化情形。
同一局部常值性给整数 $M_q$，
使 $a\equiv0\bmod q^{M_q}$ 保证完整局部同构 (312.4)。
把 $M_2$ 增大至至少二，便同时保证 $4\mid a$。

另取
$$
q_\ast>R,\qquad
q_\ast\equiv1\pmod3,\qquad
q_\ast\notin S\cup\{\ell\},\qquad q_\ast>3
\tag{312.22}
$$
为素数，并加上条件
$$
a\equiv1+q_\ast\pmod {q_\ast^2}.
\tag{312.23}
$$
则 $v_{q_\ast}(1-a^3)=1$。
条件 (312.11)、(312.19)、(312.23) 与
各 $a\equiv0\bmod q^{M_q}$ 的模数两两互素。
所以中国剩余定理给一个非空整数等差数列
$$
a\equiv A\pmod M
\tag{312.24}
$$
使全部局部条件和辅助非 $p$ 倍约化同时成立。

每个 $a\ne1$ 唯一写成 (312.2)：
对 $v_q(r)$ 除以三取余数得到 $v_q(d)\in\{0,1,2\}$，
商为 $v_q(b)$，负号吸收到 $b$。
因此 (312.20)、(312.23) 给
$$
v_p(d)=m,\quad v_p(b)=k,\quad
v_{q_\ast}(d)=1,\quad v_{q_\ast}(b)=0.
\tag{312.25}
$$
又因 $r=1-a^3$，有 $\gcd(a,r)=1$，
所以 $\gcd(a,db)=1$。

## 5. 全局 $\mathrm{GL}_2$ 像保留所有指定同余

族 $H_T$ 的 $j$ 为
$$
J(T)=6912T^3(1-T^3),
\tag{312.26}
$$
在 $\overline{\mathbb Q}(T)/\overline{\mathbb Q}(J)$ 的次数为六。
通用 $j$ 曲线的几何模 $p$ 像为
$\mathrm{SL}_2(\mathbb F_p)$，几何射影像为
$P=\mathrm{PSL}_2(\mathbb F_p)$。
把射影表示限制到这个六次函数域扩张，所得子群指数至多六。
若它是真子群，由 $P$ 的单纯性，
$P$ 在陪集上的作用给忠实嵌入 $P\hookrightarrow S_6$，
但 $p>37$ 整除 $|P|$、不整除 $6!$，矛盾。
所以射影像仍为全部 $P$。

$H_T$ 与通用 $j$ 曲线的拉回相差一个二次扭曲，
故具有同一射影像。几何像包含于 $\mathrm{SL}_2$，
且满射到 $P$；若不含 $-I$，则为 $\mathrm{SL}_2$ 的指数二子群，
与 $\mathrm{SL}_2(\mathbb F_p)$ 在 $p\ge5$ 时完美矛盾。
因此几何像为全部 $\mathrm{SL}_2$。
算术行列式为满射的圆分角色，所以算术像为全部 $\mathrm{GL}_2$。
这也是 R293 引理 293.2 对固定二次扭曲 $H_T=G_T^{(-1)}$ 的同一证明。

对这个有限算术 Galois 覆盖，群降小的参数构成薄集。
沿 $T=A+Mn$ 拉回，Serre 的整 Hilbert 不可约估计给
$$
\#\{n\in\mathbb Z:|n|\le X,\ 
\rho_{H_{A+Mn},p}(G_{\mathbb Q})\ne\mathrm{GL}_2(\mathbb F_p)\}
=O_{p,A,M}(\sqrt X\log X).
\tag{312.27}
$$
所以 (312.24) 中仍有无穷多个整数 $a$ 给完整像。
这里不要求挠点分裂域对 $\mathbb Q$ 正则；
它事实上含有圆分常数域。
删去 $a=0,1$ 等有限退化参数不影响结论。

## 6. CM 的完整正规化子像、共同导子和小除法域

由 $p\equiv2\bmod3$，$\mathcal O_K/(p)=\mathbb F_{p^2}$，
其中 $K=\mathbb Q(\sqrt{-3})$。
全部 CM 端同态定义在 $K$ 上，
所以 $C_a[p]$ 的 $G_K$ 像包含于非分裂 Cartan
$C=\mathbb F_{p^2}^\times$。
写 $N=p^2-1$。由 (312.1)，$v_3(N)=1$，且
$$
mN/6\equiv1\pmod3.
\tag{312.28}
$$
因为 $v_p(r)\equiv m\bmod3$，R258 的准确惯性公式
$\omega_2^{\,1-v_p(r)N/6}$ 及其 $p$ 次幂给
$$
\rho_{C_a,p}(I_p)=C^3.
\tag{312.29}
$$
在 $q_\ast$，$v_{q_\ast}(r)=1$ 且 $q_\ast>3$。
该 CM 曲线的温和好约化分歧指数为六；
其 $p$ 挠点惯性作用忠实，因而含三阶子群 $\mu_3\subset C$。
由于 $v_3(N)=1$，$C^3$ 和这个 $\mu_3$ 生成全部 $C$。
再加入复共轭，它在 CM 环上非平凡共轭，落在正规化子的外陪集，
便得到 $C_a$ 的全局像恰为 $N_{\mathrm{ns}}(p)$。
在 $p$ 的局部同构 (312.4) 同时给 $H_a$ 的惯性像为 $C^3$。

两条给定短模型的判别式准确相同：
$$
\Delta(H_a)=\Delta(C_a)=-432r^2.
\tag{312.30}
$$
对 $q\ge5$，若 $q\nmid r$，两者均好约化。
若 $n=v_q(r)>0$，则 $a$ 和 $2a^3-1$ 都是 $q$ 进单位。
取 $u=\lfloor n/6\rfloor$ 并同时缩放 $x=q^{2u}X,y=q^{3u}Y$，
两条极小短模型的判别式赋值均为
$2(n-6u)$。
若 $n-6u=0$，两者好约化；否则均为温和加性潜在好约化，导子指数二。
这也处理 $q=p$，因为两曲线在该处的最小指数已由同样的短模型计算确定。

在二、三处，(312.4) 是完整局部 $p$ 挠点同构。
两曲线的 $j$ 均为整数，故 $T_p$ 的惯性像有限、阶仅含二、三素因子。
模 $p$ 约化在这些有限群上忠实；
对每个高阶分歧子群取不变量与模 $p$ 约化交换。
因此 Artin 导子和 Swan 项逐项相同，
包括野分歧，而不只是坏素数支撑相同。
从而
$$
N(H_a)=N(C_a),\qquad q_\ast^2\mid N(C_a).
\tag{312.31}
$$
这里没有由有限局部同构声称两条曲线的全部全局最小模型相同。

最后验证两个小除法域。令 $\theta^3=-d$。
$p$ 在 $d$ 中的指数为一或二，所以 $\theta$ 的极小多项式
$X^3+d$ 不可约。$C_a$ 的二除域为
$K(\theta)$，其三个非零二挠点 $x$ 坐标是 $b\theta$ 的共轭。
R263 的模型
$$
F_{a,b}:y^2=x^3+3abd\,x+d(2a^3-1)
\tag{312.32}
$$
的一个二挠点 $x$ 坐标为 $a\theta+b\theta^2$；
它不是有理数，因而生成同一个三次域。
又有 $H_a=F_{a,b}^{(-b)}$，
二次扭曲不改变二除域，故完整二除域相同。
R261 的三除法 $S_3$ 商域公式为
$K(\sqrt[3]{\Delta})$；由 (312.30) 两边也相同。

## 7. 严格 CM 类非零，并且确实来自全局点

由 (312.12)，全局 Kummer 类
$$
\kappa_a=\delta_{C_a,p}(Q_a)
\tag{312.33}
$$
非零。作为一个有理点的 Kummer 像，它自动满足每个位置的通常
Selmer 条件。
而 (312.25) 给 $v_p(b)=k\ge2$。
定理 306.2 的局部群计算在这里只用
$v_p(r)=m+3k$ 和准确的 $C^3$ 惯性，故直接适用：
$$
Q_a\in p^{\lfloor k/2\rfloor}C_a(\mathbb Q_p)
\subseteq pC_a(\mathbb Q_p).
\tag{312.34}
$$
因此 $\operatorname{res}_p(\kappa_a)=0$，证明 (312.6)。

这说明存在的是严格群中的明确 Mordell–Weil 类，
不是从可能无限的 $\Sha$ 中假设出来的类，也不是纯数值 Selmer 下界。
由 $4\mid a$ 且 $a\ne0$，R306 §2 的二进点计算直接证明 $Q_a$ 无限阶；
该计算不使用全局模 $p$ 同构。故这些 CM 曲线还全部满足 $L(C_a,1)=0$。

## 8. 结果的实际限制和下一项全局信息

以上构造同时满足：整数正规形、准确的 $m$ 方向、任意深的 $p$ 进接近、
任意指定有限集上的完整局部 $p$ 挠点匹配、
共同二除域和三除法 $S_3$ 商域、同一无界导子、
以及 CM 严格 $p$-Selmer 群中的明确非零类。
比较曲线的全局模 $p$ 像仍被严格证明为全部 $\mathrm{GL}_2$。

因此，不能只凭这些条件证明
$\operatorname{Sel}_p^{\,0}(C_a/\mathbb Q)=0$。
在真正异常分支中，R306 的特定类
$\phi_*\delta_{H_a,p}(P_a)$ 还来自一个单一的全局同构 $\phi$；
本篇的满像比较曲线没有这样的 $\phi$。
下一步必须追踪该传送类与已有 CM 点类
$\delta_{C_a,p}(Q_a)$ 的关系，或引入其他只能由全局同构提供的条件。
非零严格群、正秩和局部匹配本身都不闭合这个缺口。

## 9. 来源和依赖

- J.-P. Serre，*Topics in Galois Theory*，2nd ed., 2007，
  Proposition 3.3.1、Theorem 3.4.4、§5.1 及 Proposition 8.4.1，
  印刷页 23、27、47、89；
  [全文](https://indico.math.cnrs.fr/event/11410/attachments/4760/7351/SerreTopicsGaloisTheory.pdf)。
  具体使用的是通用椭圆曲线挠点像、群降小参数的薄集性以及整数等差数列上的 Hilbert 不可约性；
  局部常值性在第 3 节已直接展开。
- [R258](R258-sextic-cm-normal-form-and-exact-integral-j-level.md)，
  六次 CM 曲线的准确惯性方向与有理三同源；
  [R261](R261-three-division-cm-field-dichotomy-and-mod-nine-traces.md) 的三除法商域公式、
  [R263](R263-two-division-parity-and-common-cubic-normal-form.md) 的二除域参数化。
- [R293](R293-local-cm-matching-with-full-global-image-and-unbounded-conductor.md)，
  完整局部挠点模的常值性及该次数六 $j$ 族的全局泛型满像证明。
  本篇新增辅助素数处的实际非 $p$ 倍约化，
  因而在保留这些局部条件时同时证明全局严格 CM Selmer 非零。
- [R306](R306-forced-cm-zeros-local-depth-and-strict-selmer.md)，
  $E_0/E_1$ 的 $p$ 阶及准确深度
  $\lfloor v_p(b)/2\rfloor$；本篇没有将形式群深度减一。
- Dirichlet 的等差数列素数定理只用于选择辅助 $\ell$ 和额外的分裂素数
  $q_\ast$；其余有限域点计数、非 $p$ 倍判别和参数整化均在文中证明。

本文为纯证明产物，证明不依赖数值搜索；无数据证书或验证脚本。主要目标仍为 OPEN。
