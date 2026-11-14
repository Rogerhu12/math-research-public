# R23. 椭圆有理函数在乘法形式坐标中的超越性

**状态：已证明。** 日期：2026-11-12。会话：Astra-rank2-Sha。

固定 $\Phi$ 的 Coleman 幂级数在椭圆参数 $t$ 中有理，但在使用
乘法形式群的 Mellin 变换时必须换成 $t=\beta_p(w)$。本文证明：
对任意非常数椭圆有理函数，这个换元后的级数甚至不代数于 $k(w)$。
结论在特征零和普通约化的特征 $p$ 中都成立，因此不能把这里的
测度输入直接当成乘法坐标中的有理函数。

## 1. 一般定理

设 $k$ 是代数闭域，特征任意，$E/k$ 为椭圆曲线。设
$$
\beta:\widehat{\mathbb G}_m\longrightarrow\widehat E
$$
为非零形式群同态。用 $w$ 表示 $\mathbb G_m$ 在 $1$ 处的参数，
其群律为 $w_1+w_2+w_1w_2$。对每个非常数 $R\in k(E)$，都有
$$
\boxed{\quad R(\beta(w))\text{ 超越于 }k(w).\quad}\tag{1}
$$
这里在 $E$ 的单位元处展开 $R$；若有极点，值属于 $k((w))$。
形式同态非零保证展开的替换是单射。

### 1.1 从一个函数的代数性得到代数图像

假设 $R(\beta(w))$ 代数于 $k(w)$。非恒定有理函数
$R:E\to\mathbb P^1$ 是有限态射，所以 $k(E)/k(R)$ 有限；
这个结论允许不可分扩张。故将 $E$ 的任意有限组有理坐标沿 $\beta$
代入后，它们都代数于 $k(w)$。

考虑 $\mathbb G_m\times E$ 中形式图像
$$
\bigl(1+w,\beta(w)\bigr),
$$
并令 $H$ 为其约化 Zariski 闭包。上述代数性说明 $\dim H=1$：
其函数域是 $k(w)$ 的有限扩张，而第一投影非常值。
闭包不可约，且包含单位元。

### 1.2 形式群关系使这个闭包成为代数子群

这里不能仅用“图像是群”代替论证，因为输入是形式点。
取 $H$ 在单位元附近的一个仿射开集。由闭包的定义，其坐标环嵌入
$k[[w]]$；必要时对不消于单位元的分母作局部化。
两个独立形式参数给出单射
$$
A\otimes_k A\longrightarrow k[[w_1,w_2]].\tag{2}
$$
为核对单射，只需看一个有限和 $\sum_j f_j(w_1)g_j(w_2)$：
先把 $f_j$ 化为 $k$ 线性无关的一组，再选择有限多个 $w_1$ 的系数，
使其系数矩阵列满秩；逐系数比较便迫使所有 $g_j$ 为零。
因此形式图像的二重积在 $H\times H$ 中 Zariski 稠密。

由于 $\beta$ 是形式群同态，两个形式图像相乘的结果仍在同一形式图像中。
任意在 $H$ 上消失的局部正则函数，沿环境群乘法拉回后，在这个形式
二重积上消失；由 (2) 的稠密性，它在 $H\times H$ 上消失。
环境群乘法因而把 $H\times H$ 映入 $H$。同样的论证适用于逆元。
闭性又使在单位元附近验证的包含延伸到整个不可约的 $H\times H$。

故 $H$ 是约化、连通的一维代数子群。$k$ 完美，约化代数群光滑。
两个投影
$$
H\longrightarrow\mathbb G_m,\qquad H\longrightarrow E
$$
都是非恒定群同态：第一投影在形式图像上是 $1+w$，第二个是非零的
$\beta$。

### 1.3 一维代数群不存在这样的两个投影

由完美域上的 Chevalley 结构定理，$H$ 有光滑连通仿射正规子群 $N$，
商 $H/N$ 为阿贝尔簇；而任何从 $H$ 到阿贝尔簇的群同态都经这个商
分解（Milne 2017，Theorem 8.27 及 §8.33）。因 $\dim H=1$，只可能有
$N=H$ 或 $N=0$。前一种情形强迫 $H\to E$ 为常值。后一种情形使
$H$ 本身为 proper 的阿贝尔曲线，所有到仿射群 $\mathbb G_m$ 的态射
都是常值。两种情况都与上述两个投影非恒定矛盾。

式 (1) 得证。证明没有把特征零的微分或可分性假设带到特征 $p$ 中。

## 2. 特征零下的独立微分证明

在特征零时还可直接看到障碍。取非零不变微分 $\omega_E$，并令
$c\ne0$ 为 $\beta$ 的线性系数。形式群同态给出
$$
\beta^*\omega_E=c\frac{dw}{1+w}.\tag{3}
$$
这可由形式群关系对第二变量在零处求导得到。

若 $R(\beta(w))$ 代数，则 §1.1 构造一个光滑射影曲线 $C$，带有
非恒定态射 $f:C\to E$ 以及由函数 $w$ 给出的有限态射
$g:C\to\mathbb P^1$。式 (3) 在对应形式分支成立，故作为 $C$ 上的
有理微分恒等式成立：
$$
f^*\omega_E=c\,d\log(1+w).\tag{4}
$$
左边处处正则。右边在任一 $w=-1$ 上方的点有留数 $ce$，其中
$e\ge1$ 为该点的分歧指数；在特征零中 $ce\ne0$。
因此右边存在真极点，矛盾。

这一证明不能不加修改地用于特征 $p$，因为分歧指数可能被 $p$ 整除。
§1 的代数群证明正是处理该情形的独立论证。

## 3. 本题中在特征零和模 p 的具体应用

Schneps 1987 §1 的普通形式群同构为
$$
\beta_p:\widehat{\mathbb G}_m\longrightarrow\widehat E,
\qquad\beta_p(w)\in w\mathcal D[[w]],
$$
其中 $\mathcal D$ 是相应完备不分歧整数环，首项为 $p$ 进单位。
其约化仍是形式群同构。先分别扩底到特征零及特征 $p$ 的代数闭域，
即可在两种情形使用式 (1)。

R19 的 $\Phi$ 非常数。对每个目标好素数，它的约化也非常数：
其零极点来自互不相交的两组素于 $p$ 的固定导子挠点；好约化下
素于 $p$ 的挠点约化单射，所以这些简单零极点仍存在。
同理，$S=\frac12\delta\log\Phi$ 的约化在相同点仍有真简单极点。
因此
$$
\Phi(\beta_p(w)),\qquad S(\beta_p(w))
$$
在特征零中都不代数；它们的模 $p$ 级数也都不代数于
$\overline{\mathbb F}_p(w)$。

Coleman 塔笔记的整 Frobenius 对数差导数为
$$
R_p=2S-2\bar\pi_E^{-1}S\circ[\pi_E].\tag{5}
$$
特征零下其至少有 $512(p-1)$ 个简单极点，故非恒定。
约化后有
$$
\overline R_p=2\overline S-2\overline{\bar\pi_E}^{-1}\overline S^p.
\tag{6}
$$
在 $\overline S$ 的每个简单极点，第二项的极点阶是 $p$，第一项仅为一，
无法相消。因此 (6) 也非恒定。再用式 (1)，$R_p(\beta_p(w))$
及其约化同样不代数。

## 4. 这排除的用法与保留的问题

因此，下列直接调用不能成立：先说“$\Phi$ 或其对数导数是椭圆曲线上的
固定有理函数”，再把其乘法坐标测度当成 $w$ 的有理函数，套用
有理函数 $\Gamma$-transform 的 $\lambda$ 上界。缺的并非一个未计算的
次数界；在这里所需的有理性本身不成立，模 $p$ 后也不成立。

Schneps 的椭圆函数版本不作这种替换，其 $\mu=0$ 定理仍然适用。
本结果也不排除对实际 Mellin 变换证明新的 $\lambda$ 界，不排除
取字符、去掉 Frobenius 后的特殊组合有额外结构。它没有证明或反驳
$\lambda(h_p)\le3$ 或 $\nu_p\le3$ 对无穷多个 $p$ 成立。

## 来源与依赖

- M. Brion, *Rational actions of algebraic groups, Lecture 2: Algebraic groups
  and their actions*，2024-10-30，[作者讲义](https://www-fourier.univ-grenoble-alpes.fr/~mbrion/RAAG2.pdf)，
  “The neutral component”：约化代数群的光滑性。
- J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type
  over a Field*，Cambridge University Press，2017，
  [作者全文](https://www.jmilne.org/math/Books/iAG2017.pdf)，
  Theorem 8.27、§8.33：Chevalley 结构定理及其到阿贝尔簇的普遍性质。
- L. Schneps, *On the μ-invariant of p-adic L-functions attached to elliptic
  curves with complex multiplication*, J. Number Theory **25** (1987), 20–33，
  [作者全文](https://webusers.imj-prg.fr/~leila.schneps/Schnepsmu.pdf)，§1–2。
- R19 与 `notes/2026-11-12-phi-coleman-tower.md`：固定零极点、范数系统及式 (5)。
- §1–2 给出了本次所用的超越性论证；不以 Rosenberg 上界的未读全文为输入。
