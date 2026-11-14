# R302：指定非零 Selmer 类与实际 CM 中心值的平方整除

日期：2026-11-13。状态：**已证明；全局必要条件，主要目标仍未完成。**

R301 为实际双同域分支找到无限阶点，并把它所在曲线的整个 $p$-Selmer 群传到指定 CM 曲线。本篇补上两个精确接口：先给该点在 Mordell–Weil 自由部分中的可除性一个绝对有效上界，从而在大 $p$ 时传送该点本身的非零 Kummer 类；再用已发表的 CM 秩零 BSD 定理处理实际参考曲线在 $p$ 处的加性约化，得到中心值为零或极小周期归一化值被 $p^2$ 整除的二择一。

下文的绝对数值只控制一个点的可除性，不是 Serre 一致性的绝对素数界。

## 1. 保持实际同余的参数和符号

沿用 R289、R301 的实际范围：$p>37$，$K=\mathbb Q(\sqrt{-3})$、$\sigma=1$、整 $j$，实际二除域和三除法 $S_3$ 商域分别与指定 CM 参考相同。于是
$$
\begin{gathered}
a,b\in\mathbb Z,\qquad a^3+db^3=1,\qquad b\ne0,\qquad
d>0\text{ 立方自由},\\
a\ne0,1,\qquad
r=1-a^3=db^3,\qquad
\varepsilon=
\begin{cases}
-1,&4\mid a,\\
1,&a\equiv1\pmod {16}.
\end{cases}
\end{gathered}
\tag{302.1}
$$
令
$$
\begin{aligned}
H_a&:\ y^2=x^3+3ar\,x-r(2a^3-1),\\
B_a&:\ y^2=x^3-\varepsilon r
       =A_d^{(-\varepsilon b)},\\
P_a&=(a^2,1)\in H_a(\mathbb Q).
\end{aligned}
\tag{302.2}
$$
R301 给出实际 $G_{\mathbb Q}$-模同构
$$
\phi:H_a[p]\xrightarrow{\sim}B_a[p],
\tag{302.3}
$$
并证明 $P_a$ 为无限阶以及
$$
\phi_*\operatorname{Sel}_p(H_a/\mathbb Q)
=\operatorname{Sel}_p(B_a/\mathbb Q)\ne0.
\tag{302.4}
$$
两条曲线的 $p$ 挠点表示均不可约，所以
$H_a(\mathbb Q)[p]=B_a(\mathbb Q)[p]=0$。

这里总有 $|a|\ge2$。事实上，(302.1) 也排除了 $a=-1$。两个实际符号不能自由更换：

| 实际分支 | 指定 CM 曲线 $B_a$ |
|---|---|
| $4\mid a$ | $y^2=x^3+1-a^3$ |
| $a\equiv1\bmod16$ | $y^2=x^3+a^3-1$ |

## 2. 整 $j$ 的显式高度下界

使用标准规范化
$$
\widehat h(Q)=\frac12\lim_{n\to\infty}
4^{-n}h\bigl(x([2^n]Q)\bigr),
\tag{302.5}
$$
其中有理数的对数高度为
$h(u/v)=\log\max\{|u|,|v|\}$，$u,v$ 互素。
设
$$
C_0=24\cdot44^4\cdot12^6
=268\,602\,112\,475\,136.
\tag{302.6}
$$

**引理 302.1。** 若 $C/\mathbb Q$ 满足 $j(C)\in\mathbb Z$，
$h(j(C))>0$，且 $Q\in C(\mathbb Q)$ 为无限阶，则
$$
\widehat h(Q)\ge \frac{h(j(C))}{C_0}.
\tag{302.7}
$$

**证明。** 在全局极小模型上，令 $D$ 为极小判别式，并令
$$
M=\operatorname{lcm}_q
\operatorname{ord}\bigl(Q\bmod C^0(\mathbb Q_q)\bigr).
\tag{302.8}
$$
这里 $C^0(\mathbb Q_q)$ 是 Néron 模型恒等分支的逆像。

整 $j$ 使所有坏位置潜在好约化。加性约化的几何分支群阶为
$1,2,3$ 或 $4$，包括剩余特征二、三；好位置的分支群平凡。
因此每个 (302.8) 中的阶数整除十二，从而 $M\mid12$。

采用 Ingram, Lemma 5 的证明中明确使用的局部高度估计：
存在整数 $1\le u\le(44M)^2$，使阿基米德局部高度满足
$$
\lambda_\infty([uM]Q)\ge
\frac1{24}h(j(C)).
\tag{302.9}
$$
这是该证明在 $j=\alpha/\beta$、$\beta=1$ 时的特化；
其输入为 Hindry–Silverman 的阿基米德局部高度估计。
由于 $[uM]Q$ 在每个有限位置都属于恒等分支，
同一标准局部高度规范化给
$$
\sum_{q<\infty}\lambda_q([uM]Q)
\ge\frac1{12}\log|D|\ge0.
\tag{302.10}
$$
把局部高度相加、使用二次性，得到
$$
\widehat h(Q)\ge
\frac{h(j(C))+2\log|D|}{24u^2M^2}
\ge\frac{h(j(C))}{24\cdot44^4M^6}
\ge\frac{h(j(C))}{C_0}.
\tag{302.11}
$$
高度及 (302.8) 的群不依赖所选有理 Weierstrass 模型，故结论适用于任意给定模型。$\square$

这里特意直接从 $u\le(44M)^2$ 使用
$u^2M^2\le44^4M^6$。不使用 Ingram 同页稍后写出的较小分母
$24\cdot44^2M^6$；因此不依赖该后续常数简化。

## 3. 显式点的高度上界和饱和指数

**引理 302.2。** 对 (302.1) 的每一个允许参数，
$$
\widehat h(P_a)<h(j(H_a)).
\tag{302.12}
$$

**证明。** 记 $T=|a|\ge2$，把 $H_a$ 的短模型系数写作
$A=3ar$、$B=-r(2a^3-1)$。由 $|r|\le T^3+1$ 可得
$$
|A|<4T^4,\qquad |B|<3T^6.
\tag{302.13}
$$
对任一无限阶有理点 $Q$，倍点的 $x$ 坐标由次数四齐次式给出：
$$
x([2]Q)=
\frac{X^4-2AX^2Z^2-8BXZ^3+A^2Z^4}
{4X^3Z+4AXZ^3+4BZ^4},
\qquad x(Q)=X/Z.
\tag{302.14}
$$
取互素整数 $X,Z$。分子和分母的绝对值分别至多为
$$
\begin{aligned}
&(1+2|A|+8|B|+A^2)\max\{|X|,|Z|\}^4,\\
&(4+4|A|+4|B|)\max\{|X|,|Z|\}^4.
\end{aligned}
$$
利用 (302.13) 及 $T\ge2$，两个系数和均小于 $32T^8$。
约去公因子只会降低有理高度，所以
$$
h(x([2]Q))\le4h(x(Q))+\log(32T^8).
\tag{302.15}
$$
对 $Q=P_a,[2]P_a,\ldots$ 迭代；这些点均非挠，分母不会因倍到原点而产生例外。由 $h(x(P_a))=2\log T$ 和 (302.5)，
$$
\widehat h(P_a)
\le\log T+\frac16\log(32T^8)
=\frac73\log T+\frac56\log2.
\tag{302.16}
$$
另一方面，
$$
\begin{aligned}
j(H_a)&=6912a^3(1-a^3)\in\mathbb Z,\\
|j(H_a)|&\ge6912T^3(T^3-1)\ge6048T^6.
\end{aligned}
\tag{302.17}
$$
故 $h(j(H_a))\ge6\log T+\log6048$，严格大于
(302.16) 的右端，证明所需结论。$\square$

**定理 302.3。** 若
$$
P_a=[n]Q+T_0,\qquad
Q\in H_a(\mathbb Q),\quad
T_0\in H_a(\mathbb Q)_{\mathrm{tors}},\quad n\ge1,
\tag{302.18}
$$
则
$$
n^2<C_0,\qquad n\le16\,389\,085.
\tag{302.19}
$$
特别，若素数 $p>16\,389\,085$，则
$$
P_a\notin pH_a(\mathbb Q)+H_a(\mathbb Q)_{\mathrm{tors}}.
\tag{302.20}
$$

**证明。** $P_a$ 无限阶，故 (302.18) 中 $Q$ 也无限阶。
规范高度不受加挠点影响，由两引理得
$$
n^2\frac{h(j(H_a))}{C_0}
\le n^2\widehat h(Q)
=\widehat h(P_a)
<h(j(H_a)).
\tag{302.21}
$$
消去正数 $h(j(H_a))$，得到 (302.19)。数值为
$\lfloor\sqrt{C_0}\rfloor=16\,389\,085$。
取 $n=p$ 即得 (302.20)。$\square$

## 4. 同一个点给出的非零 CM Selmer 类

令 $\delta_{H_a,p}$ 为通常全局 Kummer 映射。定理 302.3 和 R301 的局部条件运输给出以下明确类：
$$
\boxed{
\xi_a=\phi_*\delta_{H_a,p}(P_a)
\in\operatorname{Sel}_p(B_a/\mathbb Q)\setminus\{0\},
\qquad p>16\,389\,085.}
\tag{302.22}
$$
这里给定的是 (302.3) 的实际同构；没有先选择别的 CM 曲线或事后改变扭曲符号。
对 $37<p\le16\,389\,085$，R301 的 Selmer 非零结论仍然成立；
只是本篇不保证特定 $P_a$ 的 Kummer 像非零。

再令 $K=\mathbb Q(\sqrt{-3})$。限制到 $K$ 在全局 $H^1$ 上为单射，
因为 $[K:\mathbb Q]=2$ 素于 $p$，限制后再 corestriction 为乘二。
在 $K$ 上，$B_a$ 的 CM 环
$\mathcal O_K=\mathbb Z[\zeta_3]$ 保持所有局部 Kummer 条件，且
$p\equiv2\bmod3$ 给
$\mathcal O_K/(p)=\mathbb F_{p^2}$。因此
$$
\boxed{
\mathbb F_{p^2}\cdot\operatorname{res}_{K/\mathbb Q}(\xi_a)
\subseteq\operatorname{Sel}_p(B_a/K)
\text{ 是一条非零 }\mathbb F_{p^2}\text{ 直线}.}
\tag{302.23}
$$
它作为 $\mathbb F_p$ 空间恰有维数二。这里的 CM 标量作用在 Selmer 群上；
不产生 $H_a$ 的代数端同态，也不自动保留其中来自有理点的子空间。

## 5. CM 秩零 BSD 输入，包含在 $p$ 处坏约化

对 $B=B_a$，取全局极小 Néron 微分 $\omega_{\min}$，定义
$$
\Omega_B=\int_{B(\mathbb R)}|\omega_{\min}|,\qquad
\Lambda_B=\frac{L(B/\mathbb Q,1)}{\Omega_B}.
\tag{302.24}
$$
$L$ 是完整的 Hasse–Weil $L$ 函数，不删去坏素数处 Euler 因子。
周期使用极小模型，不能直接用 (302.2) 的微分代替而不追踪缩放。
对 $j=0$ 的曲线，实判别式为负，$B(\mathbb R)$ 连通；因此 (302.24)
也就是极小微分的正实基本周期。

使用 Burungale–Flach 已发表的 Theorem 1.1、Corollary 2：
对 CM 椭圆曲线 $B/\mathbb Q$，若 $L(B/\mathbb Q,1)\ne0$，
则 $B(\mathbb Q)$ 和 $\Sha(B/\mathbb Q)$ 均有限，并且
$$
\boxed{
\Lambda_B=
\frac{\#\Sha(B/\mathbb Q)\prod_q c_q(B)}
{\#B(\mathbb Q)_{\mathrm{tors}}^2}.}
\tag{302.25}
$$
此定理不要求所考察素数处好约化。

为核准本篇的全部假设：$B_a$ 在 $K$ 上的端同态环为整个
$\mathcal O_K$，且端同态全在 $K$ 上定义。每一 $n$ 挠点上的
$G_K$ 作用与 $\mathcal O_K$ 相容，像包含于交换群
$(\mathcal O_K/n)^\times$，故 $K(B_{a,\mathrm{tors}})/K$ 为阿贝尔扩张。
$B_a$ 定义在复共轭的固定域 $\mathbb Q$ 上。
此外 $B_a^{(-3)}$ 与 $B_a$ 通过标准三次 CM 同源相连，因而
$L(B_a/K,s)=L(B_a/\mathbb Q,s)^2$。
所以 $L(B_a/\mathbb Q,1)\ne0$ 满足该定理在 $K$ 上的非消失前提及
Corollary 2 的下降前提。原文亦明确指出每条这样的 CM 曲线
$B/\mathbb Q$ 均在该推论范围。

这一步使用 2024 年已发表版本，而非从只涵盖好约化素数的
Selmer 或主猜想陈述中遗漏一个局部前提。

## 6. 正偶数的 $p$ 赋值与秩零下的实际 $\Sha[p]$ 类

**定理 302.4。** 对全部 (302.1) 的实际参数与全部 $p>37$，
有严格二择一：
$$
\boxed{
L(B_a/\mathbb Q,1)=0
\quad\text{或}\quad
\Lambda_{B_a}\in\mathbb Q_{>0},\
v_p(\Lambda_{B_a})\in2\mathbb Z_{\ge1}.}
\tag{302.26}
$$
若第二种情形成立，则
$$
\dim_{\mathbb F_p}\operatorname{Sel}_p(B_a/\mathbb Q)
=\dim_{\mathbb F_p}\Sha(B_a/\mathbb Q)[p]
\in2\mathbb Z_{\ge1}.
\tag{302.27}
$$
若还满足 $p>16\,389\,085$，则 (302.22) 的指定类
$\xi_a$ 给出一个明确非零的 $\Sha(B_a/\mathbb Q)[p]$ 类。

**证明。** 假设中心值非零。由 (302.25)，曲线秩零且 $\Sha$ 有限。
由 $B_a(\mathbb Q)[p]=0$，有限群 $B_a(\mathbb Q)$ 的乘 $p$ 为自同构。
所以 Selmer 正合列给
$$
\operatorname{Sel}_p(B_a/\mathbb Q)
\xrightarrow{\sim}\Sha(B_a/\mathbb Q)[p].
\tag{302.28}
$$
R301 使其非零。

有限的椭圆曲线 $\Sha$ 具有非退化交替 Cassels–Tate 配对。
有限阿贝尔 $p$ 群上这种配对使群的循环因子成对：
取最大阶元素，用非退化性取一个与它配出同阶值的元素，二者生成
非退化的等阶循环群之积，再对其正交补归纳。
因此
$$
v_p\bigl(\#\Sha(B_a/\mathbb Q)\bigr)
\in2\mathbb Z_{\ge1},\qquad
\dim_{\mathbb F_p}\Sha(B_a/\mathbb Q)[p]
\in2\mathbb Z_{\ge1}.
\tag{302.29}
$$
非零性排除了零。

$B_a$ 的 $j$ 为整数，故所有坏有限位置均为加性潜在好约化。
每个 Tamagawa 数 $c_q(B_a)$ 整除相应几何分支群阶，后者至多四；
因此 $p>37$ 不整除任何 $c_q(B_a)$。
同样 $p$ 不整除 $\#B_a(\mathbb Q)_{\mathrm{tors}}$。
在 (302.25) 取 $p$ 赋值，得到
$$
v_p(\Lambda_{B_a})
=v_p\bigl(\#\Sha(B_a/\mathbb Q)\bigr),
\tag{302.30}
$$
从而证明 (302.26)、(302.27)。
当 (302.22) 可用时，通过同构 (302.28) 的像仍然非零。$\square$

因此可以使用以下准确排除条件：
$$
L(B_a/\mathbb Q,1)\ne0,\qquad
v_p\!\left(\frac{L(B_a/\mathbb Q,1)}{\Omega_{B_a}}\right)=0
\quad\Longrightarrow\quad
a\text{ 不来自当前实际异常分支}.
\tag{302.31}
$$
只证中心值非零仍不够；(302.26) 中的正偶数赋值分支必须继续控制。
也不能把其中的 $B_a$ 换成 $X^3+dY^3=Z^3$ 的 Jacobian。

## 7. 来源、精确输入及未闭合部分

- P. Ingram，*Multiples of integral points on elliptic curves*，
  Journal of Number Theory **129** (2009), 182–208，
  DOI [10.1016/j.jnt.2008.08.001](https://doi.org/10.1016/j.jnt.2008.08.001)，
  [作者终稿](https://arxiv.org/pdf/0802.2651)，Lemma 5 及其证明，作者 PDF 第 8 页。
  本篇只使用该页的 $u\le(44M)^2$、阿基米德局部高度下界和恒等分支上的有限局部高度下界；
  随后保守地逐式计算 $44^4$ 常数，不使用同页稍后的 $44^2$ 简化。
  其引用输入为 M. Hindry、J. H. Silverman，
  *The canonical height and integral points on elliptic curves*，
  Inventiones Math. **93** (1988), 419–450。
- A. Burungale、M. Flach，*The conjecture of Birch and Swinnerton-Dyer for certain elliptic curves with complex multiplication*，
  Cambridge Journal of Mathematics **12** (2024), 357–415，
  DOI [10.4310/CJM.2024.v12.n2.a2](https://doi.org/10.4310/CJM.2024.v12.n2.a2)，
  [期刊全文](https://par.nsf.gov/servlets/purl/10609724)、
  [作者终稿](https://arxiv.org/pdf/2206.09874)，Theorem 1.1、Corollary 2 及其证明，
  期刊第 359、362 页，作者 PDF 第 2、4–5 页。这里使用其对全部 CM $B/\mathbb Q$ 的秩零 BSD 公式，
  并在第 5 节核准阿贝尔挠点扩张、复共轭下降和 $L$ 值非消失的假设。
- B. Poonen、M. Stoll，*The Cassels–Tate pairing on polarized abelian varieties*，
  Annals of Mathematics **150** (1999), 1109–1149，
  [作者文本](https://math.stanford.edu/~conrad/BSDseminar/refs/PoonenStoll.pdf)，
  Introduction，作者 PDF 第 2 页；椭圆曲线 $\Sha$ 的配对交替，除去最大可除子群后非退化。
  本篇应用时 $\Sha$ 已由 CM 秩零定理证明有限，故没有剩余可除子群。
- [R301](R301-universal-selmer-transport-and-canonical-cm-obstruction.md)
  提供实际模 $p$ 同构下的局部 Kummer 条件和全局 Selmer 运输、
  $P_a$ 无限阶、准确 CM 扭曲符号及全部 $p>37$ 的 Selmer 非零性。

这些条件还不能给出变化导子 $c$ 的上界，也未对随 $a,d,b$ 变化的指定 CM 曲线
统一排除中心值为零或 $\Sha[p]\ne0$。绝对界 $16\,389\,085$ 只保证显式点的
Kummer 类不消失，不声称其以上的实际异常素数已经不存在。后续必须对同一个
$B_a$ 的中心值或 Selmer 类加入真正的全局输入。

本文为纯证明产物，无数值扫描、数据证书或验证脚本。主要目标仍为 OPEN。
