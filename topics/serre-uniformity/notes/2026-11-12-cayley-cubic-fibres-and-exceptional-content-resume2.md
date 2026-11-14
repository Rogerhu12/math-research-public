# 三次 Cayley 纤维与 exceptional 内容：全素数恒等式及其准确边界

日期：2026-11-12。状态：**完整的有限域恒等式和一个有效范数界；尚未排除 exceptional 共同零点。**

本篇接续 [共同 Fourier 零点笔记](2026-11-12-exceptional-fourier-arithmetic-resume2.md)。这里的推导对所有素数 $p>3$、$p\equiv2\pmod3$ 成立；实际小惯性还要求 $p\equiv2,5\pmod9$。本篇不使用 Studnia 的 submitted 论文中的非消失断言，也不把 Rédei 映射的迭代复杂度结果套到不同的加法周期序列上。

## 1. 参数与需要排除的理想

固定非平方 $z\in\mathbb F_p^\times$，$\tau^2=z$，以及三阶字符
$$\chi:\mathbb F_{p^2}^{\times}\longrightarrow\mu_3.$$
因为 $3\nmid p-1$，$\chi$ 在 $\mathbb F_p^\times$ 上平凡；又因 $\tau^2\in\mathbb F_p^\times$，有 $\chi(\tau)=1$。令
$$B_j=\{b\in\mathbb F_p:\chi(1+b\tau)=\omega^j\},\qquad
P_j(X)=\sum_{b\in B_j}X^b.$$
指数采用 $0,\ldots,p-1$ 的代表。设 $\zeta=\zeta_p$，所研究的理想为
$$I_p=(P_0(\zeta),P_1(\zeta),P_2(\zeta))
\subset\mathbb Z[\zeta].$$

本题实际分母素数满足 $\ell\equiv\pm1\pmod p$，因而 $\ell>p+1$、$\ell\nmid3p$。需要排除的是同一 $\ell$ 上方素理想内三个生成元同时为零。以下任何单一和的估计，都不能替代这一条件。

## 2. 在射影直线上的三次方映射

把 $t\in\mathbb F_p$ 识别为 $\mathbb F_{p^2}$ 中直线 $[1+t\tau]$，把 $\infty$ 识别为 $[\tau]$。这给
$$\mathbb P^1(\mathbb F_p)
\simeq \mathbb F_{p^2}^{\times}/\mathbb F_p^\times=:C,$$
右边为阶 $p+1$ 的循环群。字符 $\chi$ 降到 $C$，且 $\infty$ 属于颜色零。

等价的 Cayley 坐标是
$$r(t)=\frac{1+t\tau}{1-t\tau},\qquad r(\infty)=-1,$$
它把 $C$ 同构到范数一群
$$U=\{u\in\mathbb F_{p^2}^{\times}:u^{p+1}=1\}.$$
此处 $r$ 与前一笔记的坐标互逆，只改变三次角色的取向。

展开立方给
$$
(1+t\tau)^3=(1+3zt^2)+(3t+zt^3)\tau.
$$
因此射影群上的立方映射恰为
$$\boxed{J(t)=\frac{3t+zt^3}{1+3zt^2},\qquad r(J(t))=r(t)^3.}\tag{2.1}$$
因为 $3\mid p+1$，它在 $\mathbb P^1(\mathbb F_p)$ 上三对一地映到 $B_0\cup\{\infty\}$。这是群同态的准确纤维数，不是某种渐近等分布。

在有限点，
$$J'(t)=\frac{3(1-zt^2)^2}{(1+3zt^2)^2}.$$
两个几何分歧点是 $t=\pm\tau^{-1}$，均不属于 $\mathbb F_p$；其分歧指数为三，像仍为 $\pm\tau^{-1}$。所以每个有理纤维中的三个点彼此不同。

### 2.1 颜色零的三个极点

$\infty$ 的原像为 $\infty$ 和
$$t^2=-\frac1{3z}.$$
两个有限根确实在 $\mathbb F_p$：由 $p\equiv2\pmod3$，有
$$\left(\frac{-3}{p}\right)=-1,\qquad
\left(\frac{-1/(3z)}p\right)
=\left(\frac{-3z}p\right)=1.$$
在有限极点，分子为 $8t/3\ne0$；因此它们是两个简单极点，不能把它们当成可约掉的假极点。第三个简单极点是 $\infty$。

于是，对任意 $a\in\mathbb F_p^\times$、任意特征不为 $p$ 的域内阶恰为 $p$ 的 $\xi$，都有
$$\boxed{
3P_0(\xi^a)=
\sum_{\substack{t\in\mathbb F_p\\1+3zt^2\ne0}}
\xi^{aJ(t)}.
}\tag{2.2}$$
右边准确有 $p-2=3|B_0|$ 项。

## 3. 另外两色：无有理极点的三次有理函数

对 $j=1,2$ 选 $a_j=x_j+y_j\tau$，使 $\chi(a_j)=\omega^j$。必有 $x_jy_j\ne0$：若任一坐标为零，则 $a_j$ 是 $\mathbb F_p^\times$ 中元素或它乘以 $\tau$，字符值只能为一。

乘以 $a_j$ 的射影作用为
$$g_{a_j}(u)=\frac{y_j+x_ju}{x_j+zy_ju}.$$
令 $G_j=g_{a_j}\circ J$。显式写成
$$\boxed{
G_j(t)=
\frac{y_j+3x_jt+3zy_jt^2+zx_jt^3}
{x_j+3zy_jt+3zx_jt^2+z^2y_jt^3}.
}\tag{3.1}$$
这来自 $a_j(1+t\tau)^3$ 的虚部与实部之比。故所有像点的颜色为 $j$，并且
$$G_j:\mathbb P^1(\mathbb F_p)\longrightarrow B_j$$
严格三对一。相同的群论还给 $|B_1|=|B_2|=(p+1)/3$。

因为 $\infty$ 与 $0$ 都属于颜色零，$G_j$ 在 $\mathbb P^1(\mathbb F_p)$ 上既没有极点，也不取零。它在 (3.1) 中的分子、分母均为三次，且均在 $\mathbb F_p[T]$ 中不可约：若某个三次式可约，就有一个 $\mathbb F_p$ 根，与刚才的像集合矛盾。两式在代数闭包中也无公因子，因为 $g_{a_j}$ 可逆且 $J$ 是次数三的态射。

特别，原来 $J$ 的两个有限极点在复合式中变成普通点，并与 $t=\infty$ 一同取值
$$G_j(\infty)=\frac{x_j}{zy_j}.$$
三者都必须计入求和，不能沿用 (2.2) 的删项规则。因此准确公式是
$$\boxed{
3P_j(\xi^a)=\sum_{t\in\mathbb P^1(\mathbb F_p)}
\xi^{aG_j(t)},\qquad j=1,2.
}\tag{3.2}$$
右边有 $p+1$ 项。

三个覆盖的几何分歧值相同，均为 $\pm\tau^{-1}$；$g_{a_j}$ 固定这两点。这是同一个三次循环覆盖的三个有限域扭曲，而不是三个独立选择的有理函数。

## 4. 为什么纤维公式还没有给共同非零

令 $Q_j(X)$ 表示 (2.2)、(3.2) 右端的形式群环和，指数在 $\mathbb Z/p\mathbb Z$ 中解释。上面的证明实际上给出
$$Q_j(X)=3P_j(X)\quad\text{于 }\mathbb Z[X]/(X^p-1).$$
故在特征不为三时，$Q_j(\xi)$ 所生成的理想与 $P_j(\xi)$ 所生成的理想完全相同。三对一参数化本身没有增加一个 Bézout 关系；它只是把需要证明的共同非零改写为三个相容的三次有理指数和的共同非零。

两个容易误用的转换在这里均不成立。

1. **不能把 $g_{a_j}$ 当作 Fourier 频率的线性代换。** 因 $y_j\ne0$，它的分母非恒定，所以它不是仿射变换。有限域上的恒等式 $g_{a_j}\circ J=G_j$ 不会给 $\xi^{aG_j(t)}$ 与某个固定线性频率 $\xi^{a't}$ 的逐项等价。映射 $t\mapsto\xi^t$ 保持加法，却不是 $\mathbb F_p$ 到特征 $\ell$ 的域同态。
2. **复数绝对值估计不排除模 $\ell$ 消失。** 即便一个指数和很小、或项数小于 $\ell$，它也可以在 $\ell$ 上方素理想为零。前一笔记 §7 给出 $p=41,\ell=19433\equiv-1\pmod{123}$ 时 $P_0(\xi)=0$ 的精确例子。该例没有三色共同零，但已排除“每个三次和都是单位”的更强断言。

Rédei 映射的循环结构与乘法映射的联系确为已发表主题；例如 Qureshi–Panario 的 2015 年论文研究该映射在有限群中的迭代图。本篇 (2.1)–(3.2) 已直接证明所需的全部部分。那些迭代序列的周期或复杂度结论并不等于本题按加法变元 $b=0,\ldots,p-1$ 排列的三条颜色序列的联合线性复杂度。

也不能只保留三色的大小和反演对称。一个抽象反例是 $p=41,\ell=83,\xi=4$，取
$$B_0'=\{0,1,2,3,4,8,19,22,33,37,38,39,40\},$$
$$B_1'=\{5,16,20,23,24,26,27,28,29,30,31,32,34,35\},\qquad B_2'=-B_1'.$$
这三个集合分割 $\mathbb F_{41}$，大小为 $13,14,14$，且 $B_0'=-B_0'$；直接整数模幂给 $4^{41}=1\ne4$ 于 $\mathbb F_{83}$，以及 $\sum_{b\in B_j'}4^b=0$ 对全部三色成立。它**不是本题的 Cartan 三色集**，不是 exceptional 反例；它严格否定只使用这些抽象对称、项数和 $\ell\nmid p(p^2-1)$ 的证明策略。后续必须保留真正的 Cartan/Cayley 结构。

## 5. 一个全 $p$ 的内容范数上界

三次纤维之外，还可直接求出有用的二次迹恒等式。现在把 $\omega$、$\zeta$ 视为复根，令
$$f(b)=\chi(1+b\tau),\qquad
S(a)=\sum_{b\in\mathbb F_p}f(b)\zeta^{ab},\qquad W=S(1).$$
由 $f(-b)=f(b)^{-1}$，每个 $S(a)$ 都是实数。颜色大小给
$$S(0)=-1,\qquad f(0)=1.$$
加法字符正交性直接推出
$$
\sum_{a=0}^{p-1}S(a)=p,\qquad
\sum_{a=0}^{p-1}S(a)^2
=p\sum_b f(b)f(-b)=p^2.
$$

令
$$F=\mathbb Q(\zeta_{3p})^+,\qquad
F_0=\mathbb Q(\zeta_p)^+.$$
则 $[F:\mathbb Q]=p-1$，$F/F_0$ 二次；$W$ 在 $F$ 的全部共轭，计重数，恰为 $S(a)$，$a\ne0$。因此
$$\boxed{
\operatorname{Tr}_{F/\mathbb Q}(W)=p+1,\qquad
\operatorname{Tr}_{F/\mathbb Q}(W^2)=p^2-1.
}\tag{5.1}$$
这里 $W\ne0$：否则 $\sum_bf(b)X^b$ 在 $\mathbb Q(\omega)[X]$ 中被 $\Phi_p$ 整除。二者次数均为 $p-1$，而 $\Phi_p$ 在 $\mathbb Q(\omega)$ 上仍不可约，便迫使所有 $f(b)$ 相同，与三个颜色均非空矛盾。

对全部 $p-1$ 个非负实数 $S(a)^2$ 使用算术—几何平均，得
$$
0<|N_{F/\mathbb Q}(W)|
\le(p+1)^{(p-1)/2}.
$$
事实上不等号严格。若等号成立，全部 $S(a)$ 均为 $\pm\sqrt{p+1}$；由第一条迹恒等式，$\sqrt{p+1}$ 必为整数。素数 $p>3$ 不可能满足这一点，因为 $p=r^2-1=(r-1)(r+1)$。

设 $\ell\ne3,p$ 为 exceptional，取其共同零素理想，并在 $F_0$ 中记下面的素理想为 $\mathfrak q$。二次扩张 $F/F_0$ 的非平凡自同构把 $W$ 送到 $S(-1)$；三色共同零等价于这两个元素同时约化为零。因此
$$W\in\mathfrak q\mathcal O_F.$$
详细地，若 $\mathfrak q$ 分裂，两支都必须整除 $W$；若惰性，唯一一支整除 $W$ 即可。由于 $\ell\nmid3p$，没有分歧情形。写
$$f_0=\min\{n\ge1:\ell^n\equiv\pm1\pmod p\},$$
则 $N_{F_0/\mathbb Q}\mathfrak q=\ell^{f_0}$，从而
$$\ell^{2f_0}\mid N_{F/\mathbb Q}(W).$$
结合上界，得到全素数的有效必要条件
$$\boxed{
\ell^{f_0}<(p+1)^{(p-1)/4}.
}\tag{5.2}$$
对本题 Tate 分母，$f_0=1$，故
$$\boxed{
p+1<\ell<(p+1)^{(p-1)/4}.
}\tag{5.3}$$
这只界定每个固定 $p$ 的有限支撑；上界随 $p$ 快速增长，不能推出统一整性，也没有界定分母赋值。它不取代尚未完成的共同零点排除。

## 6. 保留的准确缺口

若要由本方向得到实际整性，仍须证明对所有相关 $p$、$\ell\equiv\pm1\pmod p$，(2.2) 与两个 (3.2) 不会同时为零。可以等价使用前一笔记的 $\gcd(\Psi_p,A_p,B_p)$、联合线性复杂度或二次内容理想。Cayley 参数化确认了三个和来自同一覆盖的相容扭曲；目前尚未从这种相容性导出排除共同零点的整系数恒等式。

当前结果不能称为 exceptional 猜想的证明，更不能称为 Serre uniformity 的证明。它提供可逐项核查的全 $p$ 输入，和后续尝试必须保留的极点、取向与模特征条件。

## 来源与内部接口

- [前一有限域笔记](2026-11-12-exceptional-fourier-arithmetic-resume2.md)：三色定义、共同零点等价、实多项式版本与单色消失反例。本篇的纤维公式和迹界均已自含证明。
- E. Studnia，[arXiv:2507.20801v2, §3.1](https://arxiv.org/html/2507.20801v2)：explicit exceptional 定义。按作者状态页，该稿为 submitted；本篇没有以其未发表定理为输入。
- C. Qureshi and D. Panario, *Rédei Actions on Finite Fields and Multiplication Map in Cyclic Group*, SIAM Journal on Discrete Mathematics **29** (2015), 1486–1503，[期刊原文页面](https://doi.org/10.1137/140993338)：这里仅说明准确的映射背景，不使用其迭代复杂度替代本题的 Fourier 非消失。
- [R72](../results/R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)：在已有非零三次周期的实际分支，非 exceptional 如何给尖点浸入及分母排除。该几何接口已经完成，剩余问题是本篇明确写出的有限域共同非零。
