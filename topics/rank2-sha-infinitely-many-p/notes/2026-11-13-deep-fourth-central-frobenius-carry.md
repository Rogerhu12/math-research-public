# 第四中央权的实际 Frobenius carry 与非齐次有限条件

日期：2026-11-13。**状态：本篇第四权的整混合参考、准确负层与原有限中央聚合同余已证明。所出现的单位是完整中央零强迫的有限关系中的非齐次项，不是中央非零证书。**

本篇接续 [R247](../results/R247-three-original-central-weights-mixed-reference-and-cartier.md)。
保留其中原三来源、$p=4r-1\ge19$、$F,G,L,\ell$、
$\alpha=p\ell$、$t=s^rF$，以及
$$
\mathbf S=(P,Q,s\sqrt{1-s}\,Q_{15}),\qquad
\mathbf e=(1,1,1).
$$
现在只把所读窗口扩到第四中央权 $4r=p+1$。需要的 theta 参考系数到
$s^p$ 为止；这一步首次遇到 $p!$，不能继续使用“全部阶乘可逆”。

## 1. 原混合参考在第 p 项仍整，但理由是一次真实抵消

写原特征零递推
$$
L(s)=\sum_{n\ge1}\frac{d_n}{n}s^n,\qquad
d_1=\frac{17}{3},\qquad
d_{n+1}=\frac{4n+1}{4n+3}d_n.
\tag{1}
$$
置 $M=L-\ell t$。R247 的整性证明可直接延长到次数 $<p$：
原 $w$ 对数在 $n<p$ 只有 $n=r$ 的非整项，而 (6) 中
$t(F^p-1)$ 只读取 $F^p-1$ 的次数 $<p$。故
$$
M_j\in O\quad(j<p),\qquad M_1=17/3.
\tag{2}
$$
第 $p$ 项则不能按这个理由处理。

从 (1) 的准确有限积看，分母中唯一的 $p$ 因子来自
$m=r-1$，分子中唯一的 $p$ 因子来自 $m=3r-1$，后者实际为 $3p$。
去掉它们，分子、分母的非零模 $p$ 剩余分别遍历
$\mathbf F_p^\times\setminus\{1\}$、
$\mathbf F_p^\times\setminus\{3\}$。所以
$$
\bar d_p=\frac{17}{3}\cdot
 3\frac{(-1)/1}{(-1)/3}=51.
\tag{3}
$$
R247 的第三权几何 carry 是
$$
\bar F_{3r-1}=\frac2{3\kappa},\qquad
\bar\alpha=68\kappa.
$$
由于 $p-r=3r-1$，得到
$$
\boxed{
pM_p=d_p-\alpha F_{3r-1}
\equiv51-\frac{136}{3}=\frac{17}{3}=M_1\pmod p.}
\tag{4}
$$

现在展开 $\widetilde\Gamma=\exp M$ 到第 $p$ 项。除
$M_p$ 与 $M_1^p/p!$ 外，所有其他贡献均整：它们只使用 $M_j$、
$j<p$ 及少于 $p$ 个正次因子。Wilson 定理给
$p/p!\equiv-1$，故
$$
p[s^p]\widetilde\Gamma
\equiv pM_p-M_1^p=0.
$$
因此
$$
\boxed{\widetilde\Gamma=\exp(L-\ell t)\in O[s]/(s^{p+1}).}
\tag{5}
$$
第 $p$ 项的模 $p$ 值本身仍含原下一位；(4) 只证明其整性。
不能把有限域里的截断普通指数一直写到 $p!$ 并假定它有意义。

这也说明 R247 的 $\bar F_{3r-1}$ 不是可选的几何修正：
若在 (4) 中漏掉它，原混合 theta 参考的第一个 Frobenius 整性条件就错了。

## 2. 椭圆对数因子的第一个分母

$F$ 到所读次数整，且 $F_1=1/10$。令 $B=\log F$。
其次数 $<p$ 的系数整；在第 $p$ 项中，形式对数的唯一非整贡献是
第 $p$ 次幂的首项，故
$$
\boxed{
[s^p]B=\frac{F_1^p}{p}+O
      =\frac{(1/10)^p}{p}+O.}
\tag{6}
$$
这里的 $F_1^p$ 是原有理数；对模 $p$ 系数可以再用
$\overline{F_1^p}=1/10$，但不能在需要高精度时无证替换它。

对 $1\le n\le4$ 定义原整参考行
$$
D_n=[s^{nr}]\widetilde\Gamma\mathbf S\,G/F^{n+1}\in O^3,
$$
并仍记
$$
D_{n,k}=[s^{nr}]\widetilde\Gamma\mathbf S\,G/F^{n+1}B^k.
\tag{7}
$$
新出现的唯一负层是
$$
\boxed{
D_{4,1}=\frac{F_1^p}{p}\mathbf e+O^3.}
\tag{8}
$$
确实 $4r=p+1$，(6) 只能乘 $\mathbf S$ 的一次首项和其余单位的
常数项。$k\ge2$ 时，任何含 $B_p$ 的项次数至少
$p+(k-1)+1>p+1$，所以 $D_{4,k}$ 整；$n\le3$ 的所有相关 $D_{n,k}$
也仍整。因此 (8) 没有未知方向：它准确位于三原来源的共同首项向量。

## 3. 原第四归一行的准确负层

保留 R247 的实际系数行 $R_j$，并定义
$$
\tau_n=\frac1p\sum_{j=1}^n
 \frac{(-\ell)^{n-j}}{j(n-j)!}R_j,\qquad
\sigma_n=\frac1{pn!}\sum_{l=1}^n
 (-\ell)^{n-l}(l-1)!D_l.
\tag{9}
$$
这些定义对 $n=4$ 仍是准确的特征零行。

R247 的差分公式依旧适用。$m=n-l$，$k\ge1$ 的系数为
$$
\frac{\ell^m(-p)^k}{p\,k!}
 \sum_{j=l}^n\frac{(-1)^{n-j}j^{k-1}}{(n-j)!(j-l)!}.
\tag{10}
$$
$1\le k\le m$ 的项准确为零。$m+1\le k<p$ 的系数整；
而唯一新可能 $k=p$ 时，其赋值至少 $p-m-2\ge p-5>0$。
因此 $p!$ 在这些高次项中有足够的显式 $p$ 支付，不能一概省略，
但它们不产生新的负层。

结合 (8)，惟一剩余负层来自 $l=4,k=1$，系数为 $-1$。准确得到
$$
\boxed{
\tau_4-\sigma_4+\frac{F_1^p}{p}\mathbf e\in O^3.}
\tag{11}
$$
这里没有将 R247 的 $\tau_n-\sigma_n\in O^3$ 无证延伸到 $n=4$。

## 4. 真实第四有限条件是非齐次的

$\tau_n$ 与原 Cartan 归一行仍由同一个
$\operatorname{GL}_4(O)$ 下三角矩阵相连，因为 $b-\ell\in O$，
且所用 $1!,2!,3!$ 是单位。R203 的真实 Stokes 尾精度适用于
$4\le(p+1)/2$，所以完整三中央零仍只提供有限前缀必要条件
$\tau_1,\ldots,\tau_4\in O^3$。

假设前三权的有限条件已满足，故 $\sigma_1,\sigma_2,\sigma_3$ 整。
式 (9) 给准确递推
$$
D_n=pn\,\sigma_n+\alpha\sigma_{n-1},\qquad \sigma_0=0.
\tag{12}
$$
由 (11)，第四个原有限条件因而准确等价于
$$
\boxed{
D_4-\alpha\sigma_3-4F_1^p\mathbf e\in pO^3.}
\tag{13}
$$
其模 $p$ 形式是
$$
\boxed{
\bar D_4-\bar\alpha\,\bar\sigma_3
   =\frac25(1,1,1)\quad\hbox{于 }\mathbf F_p^3.}
\tag{14}
$$
右侧是单位方向。它是全零假设下要求相消的非齐次项，
没有理由把左侧预先置零再以右侧单位推出矛盾。

也可以不逐行除数，写成同一个第四权聚合：
$$
\boxed{
-\alpha^3D_1+\alpha^2pD_2-2\alpha p^2D_3+6p^3D_4
-24p^3F_1^p\mathbf e\in p^4O^3.}
\tag{15}
$$
式 (15) 的前三个逐精度条件与 R247 的 (28) 相容。
它读取 $D_1\bmod p^4$、$D_2\bmod p^3$、$D_3\bmod p^2$、
$D_4\bmod p$；同一原参考的下一位仍不能被其模 $p$ 多项式代表代替。

更直接地，令 $V_n=[w^{nr}]e^{-\ell w^r}(A,B,H)$，则
$$
\begin{aligned}
&V_1-\frac p\alpha V_2+\frac{2p^2}{\alpha^2}V_3
                    -\frac{6p^3}{\alpha^3}V_4\\
&\quad\equiv
D_1-\frac p\alpha D_2+\frac{2p^2}{\alpha^2}D_3
                    -\frac{6p^3}{\alpha^3}D_4
+\frac{24p^3F_1^p}{\alpha^3}\mathbf e
\pmod{p^4O^3}.
\end{aligned}
\tag{16}
$$
这就是首次跨过普通 log 积分分母后，对三权聚合 (27) 的准确修正。

## 5. 对原第三来源的含义

R244 的首角权 $1,2,3$ 列变换是
$$
(A,B,H)\longmapsto
\left(A,\ C=B-A,\ T=H-A-\frac{691}{484}(B-A)\right).
$$
其行列式为一，固定分母在当前惰性素数处均为单位。
它把 $\mathbf e$ 变为 $(1,0,0)$，所以第四权单位 carry 只落在
首角权一列。对 $C,T$ 两列，$D_{4,1}$ 整，仍有
$\tau_4-\sigma_4\in O$，相应条件是齐次的。

因此第四权首次 Frobenius carry 没有凭自身制造第三独立方向。
它给出了真实的非齐次目标和下一位要求，并排除了把原四权
有限测试统一写成零右端的做法。要由它证明中央非零，
仍需用原 $P,Q,Q_{15}$ 与同一 theta 参考证明 (13) 的某个坐标
无法达到；这里没有声称这个剩余算术比较已经完成。

依赖：R247 的全部原规范、第三权 carry 与差分证明；R162/R211 的
原特征零 theta 递推；R203/R244 的真实三来源有限 Stokes 目标格。
本篇的两个单位系数 $17/3$、$2/5$ 均由统一代数计算得出，无素数扫描。

