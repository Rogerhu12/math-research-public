# R293：同一整三次族内的任意有限局部 CM 匹配与无界共同导子

日期：2026-11-13。

**状态：已证明。** 本篇严格检验 R289/R290 之后“叠加有限个局部条件，再推出变化导子上界”这条路线的适用边界。结论是在同一个

$$a^3+db^3=1,\qquad a\equiv1\pmod{16}$$

整数族内，任意有限素数集上的完整局部 $p$ 挠点 CM 同构，都与全局模 $p$ 满像及无界共同导子相容；并且可以同时保留相同的全局极小判别式、导子、实际二挠点域和三挠点 $S_3$ 商域。

这些构造出的曲线**不是 Serre 一致性的反例**：其模 $p$ 表示被证明满射。它们证明目前得到的有限局部与整数条件，不能单独推出一般变化 $c$ 的绝对上界。实际坏像曲线满足的那个**全局**
$E_0[p]\simeq A_d[p]$ 仍是必须进一步利用的关键输入。

## 1. 精确命题

固定素数 $p>37$，满足 $p\equiv2$ 或 $5\pmod9$，并置

$$
m=\begin{cases}
2,&p\equiv2\pmod9,\\
1,&p\equiv5\pmod9.
\end{cases}
\tag{293.1}
$$

设 $S$ 是包含 $2,3,p$ 的任意有限有理素数集。另选任意素数

$$
q_\ast\notin S,\qquad q_\ast\equiv1\pmod3.
\tag{293.2}
$$

允许 $S$ 随 $p$ 变化，例如取所有不超过 $p^2$ 的素数。

**定理 293.1。** 存在无穷多个不同整数 $a$，以及相应的整数 $b\ne0$、正立方自由整数 $d$，满足以下全部性质。记

$$
F_{a,b}:y^2=x^3+3abd\,x+d(2a^3-1),\qquad
A_d:y^2=x^3+d.
\tag{293.3}
$$

1. 参数满足
   $$
   a^3+db^3=1,\quad
   a\equiv1\pmod{16},\quad
   2p\mid b,\quad v_p(d)=m,
   $$
   $$
   v_\ell(d)=0\quad(\ell\in S\setminus\{p\}),\qquad
   v_{q_\ast}(d)=1.
   \tag{293.4}
   $$
   特别
   $$
   v_p(a-1)=m+3v_p(b)\ge m+3.
   $$
2. 对每个 $\ell\in S$，有真正的局部 Galois 模同构
   $$
   F_{a,b}[p]\simeq A_d[p]
   \quad\text{作为 }G_{\mathbb Q_\ell}\text{-模}.
   \tag{293.5}
   $$
   这比只要求若干 Frobenius 迹相同强，并包括表示素数 $\ell=p$。
3. 全局有
   $$
   \overline\rho_{F_{a,b},p}(G_{\mathbb Q})
       =\operatorname{GL}_2(\mathbb F_p),\qquad
   \overline\rho_{A_d,p}(G_{\mathbb Q})=N_{\rm ns}(p).
   \tag{293.6}
   $$
   故 $F_{a,b}$ 无 CM，且两者的全局 $p$ 挠点模不同构。
4. 两曲线的全局极小判别式准确相等，且全局导子相等：
   $$
   \Delta_{\min}(F_{a,b})=\Delta_{\min}(A_d)=-432d^2,
   \qquad N(F_{a,b})=N(A_d).
   \tag{293.7}
   $$
   其 $j$ 为同一个整数
   $$
   j(F_{a,b})=6912a^3(1-a^3)<0.
   \tag{293.8}
   $$
5. 两条实际小除法域均相同：
   $$
   \mathbb Q(F_{a,b}[2])=\mathbb Q(A_d[2]),\qquad
   \mathcal L_3(F_{a,b})=\mathcal L_3(A_d).
   \tag{293.9}
   $$
   其中 $\mathcal L_3$ 仍是 $\operatorname{GL}_2(\mathbb F_3)/Q_8\simeq S_3$
   的实际商域。

令 $c(d)$ 为这个实际 CM 参考的 prime-to-$p$ 三次环类导子。构造中有

$$
c(d)=2\!\!\prod_{\substack{q\mid d\\q\ne p}}q,
\qquad q_\ast\mid c(d),\qquad c(d)\ge2q_\ast.
\tag{293.10}
$$

因为 (293.2) 中 $q_\ast$ 可以任意大，固定 $p,S$ 后，这些条件也与无界 $c(d)$ 相容。此处仅把 $c(d)$ 用作 CM 参考的真实导子；没有给满像曲线 $F_{a,b}$ 虚构一个全局 Cartan 商角色或 $\sigma$。

## 2. 在固定局部域中接近 CM 曲线

先给完整局部构造。令 $k=\mathbb Q_\ell$，固定任意 $d_\ell\in k^\times$。
在 $b=0$ 附近取唯一的解析分支

$$
a(b)=(1-d_\ell b^3)^{1/3},\qquad a(0)=1.
\tag{293.11}
$$

因为 $k$ 的特征为零，隐函数定理适用；在 $\ell=3$ 时只需把邻域取小，不要求导数三是整数单位。所得曲线族

$$
\mathcal F_b:\quad
y^2=x^3+3a(b)b d_\ell\,x+d_\ell(1-2d_\ell b^3)
\tag{293.12}
$$

满足

$$
\mathcal F_0=A_{d_\ell},\qquad
\Delta(\mathcal F_b)=-432d_\ell^2\ne0.
\tag{293.13}
$$

因此这是 $b=0$ 附近的光滑解析椭圆曲线族，中心曲线没有退化。

### 2.1 完整局部 $p$ 挠点模的局部常值性

对任意固定 $p$，当 $b$ 充分接近零时，

$$
\mathcal F_b[p]\simeq A_{d_\ell}[p]
\quad\text{作为 }G_k\text{-模}.
\tag{293.14}
$$

这里允许 $\ell=p$。原因是底域为特征零，整个 $p$ 挠点仍是有限 étale 群概形，不是只比较整模型的特殊纤维。

为明确这个局部常值断言，取有限 Galois 扩张 $M/k$，包含中心曲线的全部 $p$ 挠点。每个 $p$ 挠点都是 $[p]$ 的单根，因为 $d[p]=p$ 在 $k$ 可逆。对每个点应用 $M$ 上的隐函数定理，在充分小的共同邻域中得到唯一的解析挠点分支。缩小邻域，使不同挠点的分支留在两两不交的邻域内。

$\operatorname{Gal}(M/k)$ 的作用由唯一性给出与中心纤维相同的置换；群加法的解析连续性和分支唯一性说明点的逐个对应保持加法。每条分支都取值于 $M$，故 $G_M$ 在新纤维全部挠点上仍平凡。这样得到 (293.14) 的 Galois 模同构。

这也正是 Serre，*Topics in Galois Theory*，Proposition 8.4.1 的局部有限 étale 覆盖常值性；本文解释了其如何保留挠点群结构，而不只是一个未标记的分裂域。

### 2.2 回到 R289 的同一个一参数模型

记

$$
G_a:\quad
y^2=x^3+3a(1-a^3)x+(1-a^3)(2a^3-1).
\tag{293.15}
$$

只要 $b\ne0$，$a=a(b)$，就有准确恒等式

$$
G_a=\mathcal F_b^{(b)},\qquad
A_{1-a^3}=A_{d_\ell}^{(b)}.
\tag{293.16}
$$

这里右边采用二次扭曲的通常短模型；系数等式直接来自 $1-a^3=d_\ell b^3$。
所以对同一 $b$ 同时扭曲 (293.14)，得

$$
G_a[p]\simeq A_{1-a^3}[p]\quad\text{作为 }G_k\text{-模}.
\tag{293.17}
$$

选一个足够小但非零的 $b_0$，置 $a_0=a(b_0)\ne1$。在 $b_0$ 处

$$a'(b_0)=-d_\ell b_0^2/a_0^2\ne0,$$

所以 $b\mapsto a(b)$ 是一个局部解析同构。于是存在 $a_0$ 的非空开邻域
$U_\ell\subset k$，其中每个 $a$ 都来自相邻的 $b$，且 (293.17) 成立。
还能缩小 $U_\ell$，使 $v_\ell(1-a^3)$ 和其立方类保持固定。

## 3. 各处局部开集与整数同余类

现在同时为有限集合 $S$ 选择这些开集。

### 3.1 表示素数

在 $\ell=p$ 取

$$d_p=p^m,\qquad b_0=p^B,$$

其中整数 $B\ge1$ 取充分大，使第 2 节的局部同构成立。由

$$1-a_0^3=p^{m+3B}$$

且 $a_0$ 近于一，$p>3$ 给

$$v_p(a_0-1)=m+3B.$$

缩小 $U_p$，使每个 $a\in U_p$ 满足

$$
v_p(1-a^3)=m+3B,\quad
1-a^3\in p^m\mathbb Q_p^{\times3},
\quad a\equiv1\pmod{p^{m+3B}}.
\tag{293.18}
$$

这既固定实际立方自由指数 $m$，也保证后面提取出的整数 $b$ 被 $p$ 整除。

### 3.2 集合内其余素数

对 $\ell\in S\setminus\{p\}$，取

$$d_\ell=1,\qquad b_0=\ell^{B_\ell}$$

且 $B_\ell$ 足够大。缩小 $U_\ell$，保证

$$
1-a^3\in\mathbb Q_\ell^{\times3},\qquad
v_\ell(1-a^3)=3B_\ell.
\tag{293.19}
$$

在二处另取 $B_2\ge2$，从而 $a\equiv1\pmod{16}$。所有 $a_0$ 都在
$\mathbb Z_\ell$，所以可以在 $U_\ell$ 内选取一个完整的整数同余类
$a_\ell+\ell^{n_\ell}\mathbb Z_\ell$。

### 3.3 一个任意大的新分裂素数

由于 $q_\ast\equiv1\pmod3$，模 $q_\ast$ 存在非平凡三次单位根
$\zeta\ne1$。选取它的一个模 $q_\ast^2$ 提升 $\widetilde\zeta$，使

$$v_{q_\ast}(1-\widetilde\zeta^3)=1. \tag{293.20}$$

这样的提升存在：$3\zeta^2\ne0$，所以在全部 $q_\ast$ 个提升中，准确一个
满足立方同余于一模 $q_\ast^2$，其余均满足 (293.20)。
加入同余

$$a\equiv\widetilde\zeta\pmod{q_\ast^2}.$$

中国剩余定理给一个非空整数等差数列

$$a=A+Mn,\qquad n\in\mathbb Z, \tag{293.21}$$

使其全部元素同时位于各 $U_\ell$、满足 (293.18)–(293.20)。
目前只构造了局部同构；下一节在这同一个等差数列中保证全局满像。

## 4. 一参数族的全局泛型模 $p$ 像

**引理 293.2。** 对 $p>37$，曲线 $G_T/\mathbb Q(T)$ 的模 $p$ Galois 像
为 $\operatorname{GL}_2(\mathbb F_p)$，几何像为 $\operatorname{SL}_2(\mathbb F_p)$。

**证明。** 它的 $j$ 为次数六的多项式

$$J(T)=6912T^3(1-T^3), \tag{293.22}$$

故

$$[\overline{\mathbb Q}(T):\overline{\mathbb Q}(J)]=6.$$

令 $\mathcal E/\mathbb Q(J)$ 是 $j$ 恰为变量 $J$ 的通用模型。经典模曲线理论给其几何模 $p$ 像为 $\operatorname{SL}_2(\mathbb F_p)$；准确见 Serre 上述书 §5.1 开头，印刷页 47。它的射影像因而为

$$P=\operatorname{PSL}_2(\mathbb F_p).$$

把射影表示限制到次数六的函数域扩张，所得子群 $P'$ 的指数至多六；这是对应的 Galois 扩张与 $\overline{\mathbb Q}(T)$ 的交域次数。若 $P'\ne P$，$P$ 在至多六个陪集上的作用，由 $P$ 的单纯性给忠实嵌入

$$P\hookrightarrow S_6.$$

然而

$$|P|=p(p^2-1)/2>6!,$$

不可能。故限制后的射影像仍为 $P$。

$G_T$ 与 $\mathcal E$ 的拉回具有相同的非特殊泛型 $j$，相差至多一个二次扭曲；射影表示不受这个扭曲影响。因此 $G_T$ 的几何像
$H\subset\operatorname{SL}_2(\mathbb F_p)$ 满射到 $P$。

若 $H$ 不包含中心 $\{\pm I\}$，则它是 $\operatorname{SL}_2(\mathbb F_p)$ 的指数二子群，矛盾于这个群在 $p\ge5$ 时完美。这个完美性也可直接检验：取 $r\in\mathbb F_p^\times$、$r^2\ne1$，与
$\operatorname{diag}(r,r^{-1})$ 的交换子产生所有上三角初等幺幂矩阵，同理产生所有下三角初等幺幂矩阵；这些矩阵生成整个 $\operatorname{SL}_2$。
所以 $H=\operatorname{SL}_2(\mathbb F_p)$。

算术表示的行列式是圆分角色，在 $G_{\mathbb Q(T)}$ 上满射到
$\mathbb F_p^\times$。结合几何像，算术像为整个 $\operatorname{GL}_2(\mathbb F_p)$。证毕。

### 4.1 指定同余条件下的整 Hilbert 不可约性

取 $G_T[p]$ 的完整分裂域；它是 $\mathbb Q(T)$ 上 Galois 群为
$\operatorname{GL}_2(\mathbb F_p)$ 的有限扩张。它含常数域 $\mathbb Q(\zeta_p)$，
所以这里不声称该扩张为正则扩张。

Serre，Proposition 3.3.1 只要求覆盖在 $\mathbb Q$ 上不可约，并不要求几何不可约；它说明全局群降小的参数组成一个薄集。把这个薄集沿
$T=A+Mn$ 拉回，仍是 $n$ 直线上的薄集。Theorem 3.4.4 的整 Hilbert 估计给

$$
\#\{n\in\mathbb Z:|n|\le X,\ \text{群降小}\}
 =O_{p,A,M}(\sqrt X\log X).
\tag{293.23}
$$

所以在 (293.21) 中有无穷多个整数 $a$，使

$$\overline\rho_{G_a,p}(G_{\mathbb Q})=\operatorname{GL}_2(\mathbb F_p). \tag{293.24}$$

删去 $a=0,1$ 及有限多个退化参数不影响此结论。这一步确实给整数
$a$，且保留全部指定局部开集；没有从仅对任意有理参数的 Hilbert 性直接跳到整数解。
式 (293.23) 的常数可依赖固定的 $p,S,q_\ast$ 与同余条件；本篇不需要其统一性。

## 5. 提取同一个立方自由参数并恢复实际局部同构

对上述每个整数 $a$，唯一写成

$$1-a^3=db^3,\qquad d>0\text{ 立方自由},\quad b\in\mathbb Z\setminus\{0\}. \tag{293.25}$$

负号吸收到 $b^3$ 中。对每个素数，把 $v_q(1-a^3)$ 除以三取余数，
余数即 $v_q(d)\in\{0,1,2\}$，商即 $v_q(b)$。因此 (293.18)–(293.20)
准确给出 (293.4)，而非仅给一个未追踪的局部立方类。又有

$$
G_a=F_{a,b}^{(b)},\qquad A_{1-a^3}=A_d^{(b)}.
\tag{293.26}
$$

对每个 $\ell\in S$，第 2–3 节已经得到同一个
$G_a[p]\simeq A_{1-a^3}[p]$。两边再同时二次扭曲 $b$，因为 $b^2$
为有理平方，(293.26) 恢复准确的

$$F_{a,b}[p]\simeq A_d[p]\quad\text{于 }G_{\mathbb Q_\ell}.$$

因此局部选择的 $d_\ell$ 仅用于产生非空开集；最后比较的全部局部同构，
都属于 (293.25) 中**同一个全局正立方自由 $d$** 和同一个全局曲线 $F_{a,b}$。

二次扭曲还保持满像结论 (293.24)。为核准这一点，设
$\rho:G_{\mathbb Q}\twoheadrightarrow\operatorname{GL}_2(\mathbb F_p)$、
$\chi$ 为二次角色。若 $\chi$ 不经 $\rho$ 因子化，$(\rho,\chi)$ 的像为
$\operatorname{GL}_2(\mathbb F_p)\times\{\pm1\}$，乘积仍满。若经 $\rho$
因子化，因 $\operatorname{SL}_2(\mathbb F_p)$ 完美，$\chi$ 经行列式因子化；
映射 $g\mapsto\chi(g)g$ 的核只能含标量 $\pm I$，但
$\chi(-I)=\chi(\det(-I))=1$，所以它是单射，从而是有限群的自同构。
故 $F_{a,b}$ 的模 $p$ 像也满射。

## 6. 实际 CM 参考的完整正规化子像

$A_d$ 有 $\mathbb Q(\sqrt{-3})$ 复乘，且 $p\equiv2\pmod3$，所以其模 $p$
像包含于 $N_{\rm ns}(p)$。由 (293.1)、$v_p(d)=m$ 及 R258 §5 的直接局部惯性公式，其表示素数处的像准确为

$$\rho_{A_d,p}(I_p)=C^3.$$

这里 $|C|=p^2-1$ 的三进赋值为一，因为 $p\equiv2,5\pmod9$。
在另一个实际素数 $q_\ast$，$v_{q_\ast}(d)=1$，潜在好约化有限惯性阶为六。
$q_\ast\ne p$ 且 $p>37$，故这个惯性在 $A_d[p]$ 上忠实，像含一个三阶元。
而 $q_\ast\ne3$，CM 域在该处不分歧，所以此惯性落在 $C$ 内。

$C^3$ 与一个三阶元生成整个 $C$。复共轭不属于 $C$，因此全局像准确为
$N_{\rm ns}(p)$，证明 (293.6) 的第二项。特别 CM 参考没有落入需要另排除的指数三正规化子子群。

## 7. 判别式、全部局部导子和两个实际小除法域

### 7.1 全局极小判别式

直接计算 (293.3)：

$$\Delta(F_{a,b})=-432d^2=\Delta(A_d). \tag{293.27}$$

两条短模型均整。构造给 $2,3\nmid d$，所以在二、三的判别式赋值分别为
四、三；在 $q\ge5$ 的赋值是 $2v_q(d)\in\{0,2,4\}$。这些值都小于十二。
任何两个有理 Weierstrass 模型的判别式赋值之差被十二整除，而整模型的判别式赋值非负。因此每处上述模型都已经极小，证明 (293.7) 的判别式等式。

### 7.2 二、三处不遗漏野导子

对 $\ell=2,3$，(293.5) 是实际 $G_{\mathbb Q_\ell}$-模同构，且两曲线的
$j$ 都在 $\mathbb Z_\ell$，故有限惯性像的阶只含二、三素因子，至多为
$24$。因 $p>37$，模 $p$ 约化在有限惯性像上忠实。

两边因而有相同惯性核，并可在同一个有限 Galois 惯性商中比较全部高阶分歧群。
对其任意分歧子群 $J$，$|J|$ 在 $\mathbb Z_p$ 可逆，平均幂等元

$$\frac1{|J|}\sum_{g\in J}g$$

说明取不变量与模 $p$ 约化交换。给定同构遂使每个 $J$ 的不变量余维都相同，
所以 Artin 惯性项及全部 Swan 项逐项相等。因此两条曲线在二、三的导子指数完全相同。这一步没有以“坏素数支撑相同”代替野导子比较。

### 7.3 其余素数

对 $q\ge5$，若 $q\nmid d$，两条曲线的判别式均为单位，所以都好约化。
若 $v_q(d)=r\in\{1,2\}$，则 $a^3\equiv1\pmod q$，$2a^3-1\equiv1\pmod q$。
两条极小判别式赋值均为 $2r$，潜在好约化惯性分别为六阶或三阶，均温和且无不变量，
所以导子指数均为二。这也直接包括 $q=p$，并不把模 $p$ Artin 导子误作
表示素数处椭圆曲线的导子。

由此得到 $N(F_{a,b})=N(A_d)$。更具体地，R258 的实际二、三处计算给

$$
N(A_d)=2^\alpha3^2p^2
\left(\prod_{\substack{q\mid d\\q\ne p}}q\right)^2,\qquad
\alpha=\begin{cases}2,&d\equiv1\pmod4,\\4,&d\equiv3\pmod4.\end{cases}
\tag{293.28}
$$

三处指数二是因为 (293.19)、(293.25) 使 $d\in\mathbb Q_3^{\times3}$，
等价于这里的 $d\equiv\pm1\pmod9$。
相应三次环类导子在二的指数一、三的指数零，在其他 $q\ne p$ 的指数恰为
一当且仅当 $q\mid d$，即得 (293.10)。

### 7.4 小除法域与整 $j$

$p$ 在 $d$ 中的指数为一或二，所以 $X^3+d$ 不可约。令 $\theta^3=-d$，
则 $a\theta+b\theta^2$ 是 $F_{a,b}$ 的二分多项式的根。它不属于 $\mathbb Q$，
因为 $1,\theta,\theta^2$ 线性无关且 $(a,b)\ne(0,0)$。其三个共轭根给
R263 的精确系数式；因此两个完整二挠点域都是 $\mathbb Q(\theta,\zeta_3)$。

三挠点 $S_3$ 商域由 R261/R96 的直接 resolvent 计算给
$H(\sqrt[3]{\Delta})$。两条判别式在 (293.27) 中准确相同，且其 $p$ 赋值
$2m$ 非三的倍数，故是同一个非平凡 $S_3$ 域。这证明 (293.9)。

最后

$$j(F_{a,b})=6912d a^3b^3=6912a^3(1-a^3)$$

为整数。$a\equiv1\pmod{16}$ 且已删去 $a=1$，故 $a\le-15$ 或 $a\ge17$，
所以 $j<0$。全局模 $p$ 满像也保证这些曲线无 CM：CM 曲线在其至多二次的
端同态定义域上有交换的 Tate 模 Galois 像，而
$\operatorname{GL}_2(\mathbb F_p)$ 没有交换的指数至多二子群。完成定理证明。

## 8. 对当前开放问题的准确含义

固定 $p$ 后，先给任何有限素数集 $S$，再给任何大的分裂素数 $q_\ast\notin S$，
上面的构造都成立。尤其可以同时要求：

- 全部 $q<p^2$ 的局部 $p$ 挠点模与同一个变化 CM 参考一致；
- R289 的整数族、奇数参数分支及原始性；
- R290 的真实表示素数处 Hasse 深度，乃至把 $v_p(b)$ 预先取得任意大；
- 同全局极小判别式、同全局导子和两个实际小除法域；
- 共同 CM 导子具有预先指定的任意大的新分裂素因子。

尽管如此，$F_{a,b}$ 的全局模 $p$ 像仍可以是整个 $\operatorname{GL}_2(\mathbb F_p)$。
因此这些有限条件本身既不强迫全局 CM 同余，也不强迫 $c(d)$ 有上界。
这没有排除继续使用**全局** $E_0[p]\simeq A_d[p]$ 的方法；
它准确标出了不能用局部匹配替换的那一项。O4 的实际全局非消失、完整模 $p$
表示或另一个全局高度输入仍须继续推进。

## 来源与产物

- **Jean-Pierre Serre**，*Topics in Galois Theory*，第 2 版，2007，A K Peters：
  Proposition 3.3.1（印刷页 23）给非正则 Galois 覆盖的薄异常集；
  Theorem 3.4.4（页 27，S. D. Cohen）给薄集的整点估计；
  §5.1 开头（页 47）给 $j$ 为变量的椭圆曲线全部 $n$ 挠点泛型及几何像；
  Proposition 8.4.1（页 89）给局部 Galois 模的常值性。
  [已核第二版原文 PDF](https://indico.math.cnrs.fr/event/11410/attachments/4760/7351/SerreTopicsGaloisTheory.pdf)。
  这里准确使用整版本，并在正文单独处理了指定等差数列和泛型域中的圆分常数。
- **R258**：同一 CM 参数的 $p$ 惯性公式及二、三处导子表；
  **R261/R263**：实际小除法域的显式代数描述；
  **R289/R290**：本文所检验的整数正规式和局部深度条件。
  本文不把这些条件的满足说成全局坏像假设的满足。

本文为纯证明产物，没有数据或脚本。Hilbert 不可约性证明无穷多满像曲线的存在，
并不是对有限参数范围的扫描。
