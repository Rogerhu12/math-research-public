# 原高坐标在除 p 的 Ramanujan 多项式中的准确位置

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；o2_high_coefficient / root。

**已证明的接口；原高坐标非零仍 OPEN。** 本文不重登 R975 的 heat 递推或交换子恒等式，只固定原 \(c_{p-r}^{\pm}\) 在一个实际整除 \(p\) 多项式中的位置。由此可准确区分模 \(p\) 曲率、模 \(p^2\) 修正和指定高坐标，避免从另一个单位读数跳到原目标。

## 1. 原环和同权整除

使用 [R975](../results/R975-original-balanced-Kronecker-integral-heat-recurrence.md) 的原变量
\[
\mathrm{wt}(E,X,Y)=(2,4,6),\qquad
\mathcal R=\frac{E^2-X}{12}\partial_E
+\frac{EX-Y}{3}\partial_X+\frac{EY-X^2}{2}\partial_Y,
\]
\[
\mathcal F_n(X,Y)=(\mathcal R^{n-1}E)|_{E=0}.
\]
\(E\) 始终是形式变量，不是将复 CM 点处的数值 \(E_2\) 设为零。

固定素数 \(p\ge5\)，令
\[
H=E_{p-1}(X,Y),\qquad B=E_{p+1}(X,Y)
\]
为归一化 Eisenstein 级数在 \(\mathbf Z_{(p)}[X,Y]\) 中的标准多项式。定义
\[
\boxed{\quad
\mathfrak B_p(E,X,Y)
=\frac{\mathcal R^{p-1}E+E^p-HB}{p}
\in\mathbf Z_{(p)}[E,X,Y].
\quad}
\tag{B.1}
\]
分子三项权均为 \(2p\)。下面核准所宣称的整除。

R975 (975.16) 逐次应用给，对于 \(N\ge1,\ 1\le r\le N\)，
\[
[E^r]\mathcal R^NE
=\frac{(N)_r(N+1)_r}{r!\,12^r}\,
 \mathcal F_{N+1-r}(X,Y),
\tag{B.2}
\]
其中 \((a)_r=a(a-1)\cdots(a-r+1)\) 为下降阶乘。最高 \(E^{N+1}\) 项另为 \(N!/12^N\)。

取 \(N=p-1\)。式 (B.2) 的每个 \(1\le r\le p-1\) 系数都在 \(p\mathbf Z_{(p)}[X,Y]\)，因为 \((p)_r\) 恰含一个 \(p\)，其余分母为单位。最高项由 Wilson 定理满足
\[
\frac{(p-1)!}{12^{p-1}}+1\equiv0\pmod p.
\]
因此 \(\mathcal R^{p-1}E+E^p\) 模 \(p\) 是只含 \(X,Y\) 的权 \(2p\) 多项式。

在 \(q\)-展开中 \(\mathcal R\) 对应 \(\Theta=q\,d/dq\)。由
\[
E_2(q)=1-24\sum_{n\ge1}\sigma_1(n)q^n,\qquad
\sigma_1(pn)\equiv\sigma_1(n)\pmod p
\]
和 Fermat 恒等式，逐系数得到
\[
\Theta^{p-1}E_2+E_2^p\equiv E_2\pmod p.
\tag{B.3}
\]
另一方面标准 Eisenstein 同余给 \(H\equiv1,\ B\equiv E_2\) 于 \(q\)-展开。两边现在都是同一个固定权 \(2p\) 的模形式，故固定权 \(q\)-展开原理给
\[
\mathcal R^{p-1}E+E^p\equiv HB
\quad\text{于 }\mathbf F_p[E,X,Y].
\]
这证明 (B.1)。此处仅在正 \(E\)-幂已消掉后使用模形式的固定权展开原理；没有把不同权的 \(H\equiv1\) 当作多项式恒等式。

## 2. 每个指定正 E 坐标的完整标量

在 (B.2) 中先除以 \(p\) 再约化，得到
\[
[E^r]\mathfrak B_p
\equiv
-\frac{(r-1)!}{12^r}\mathcal F_{p-r}(X,Y)
\pmod p,\qquad 1\le r\le p-1.
\tag{B.4}
\]
确切地，
\[
(p-1)_r\equiv(-1)^r r!,\qquad
(p)_r/p\equiv(-1)^{r-1}(r-1)!,
\]
所以乘积的符号为负。式 (B.4) 不包括最高 \(E^p\) 项。

保留 R988 的两个 CM 模型：
\[
E_+:y^2=x^3+1,\quad (X,Y)=(0,864);
\qquad
E_-:y^2=x^3-1,\quad (X,Y)=(0,-864),
\]
以及原微分 \(dx/(2y)\)。由 R975
\[
c_n^\pm
=\frac{\mathcal F_n(0,\pm864)}{12n!(n-1)!}.
\]
用
\[
(p-r)!(p-r-1)!\equiv-\frac1{r!(r-1)!}\pmod p
\]
代入 (B.4)，得
\[
\boxed{\quad
\overline{c_{p-r}^\pm}
=r!\,12^{r-1}\,
 [E^r]\overline{\mathfrak B_p(E,0,\pm864)}.
\quad}
\tag{B.5}
\]

原两行的 \(r\) 与标量准确为：

| 原允许分支 | \(r\) | (B.5) 的单位标量 |
|---|---:|---:|
| \(p\equiv11\pmod{12}\) | 2 | \(24\) |
| \(p\equiv5\pmod{12}\) | 8 | \(8!\,12^7\) |

这里仍须保原 \(p\bmod9\) 条件。特别是第二行不是 \(8\cdot12^7/7!\)：两个 balanced 阶乘必须一并保留。原两行有 \(p-r\equiv3\pmod6\)，所以 \(c_{p-r}^+=-c_{p-r}^-\)，与 R988 的模型相位一致。

如果将 \(H,B\) 换为任何不含 \(E\) 且有同样模 \(p\) 约化的整升换，\(\mathfrak B_p\) 只改变一个不含 \(E\) 的多项式。因此所有 \(r\ge1\) 的坐标 (B.4)–(B.5) 不依赖这种升换。

结合 [R988](../results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md)，原完整 trace 非零等价于表中指定的 \([E^2]\) 或 \([E^8]\) 坐标非零。等价并不证明非零；模 \(p\) 的 \(\mathcal R^p\) 公式也没有自动给出这项除 \(p\) 后的读数。

## 3. 两个新文献输入的准确范围

Ahlgren–Raum–Richter 的 *Theta cycles of modular forms modulo \(p^2\)* 给模 \(p^2\) theta 周期的 filtration 及 Eisenstein 升换关系。它可用于继续研究 (B.1)，但形式变量的固定权 \([E^r]\) 提取须另行保持。不同权的 \(q\)-展开同余不能在 \(H=0\) 的 CM 纤维直接替代 (B.4)，全局 filtration 也不指定某个 CM 点的单位读数。[原文](https://arxiv.org/html/2604.06049v1)，[期刊页](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/theta-cycles-of-modular-forms-modulo-p2/A10141FE253EE17708856E81CC183B6C)。

Burungale–Kobayashi–Ota 的 *The p-adic valuation of local resolvents, generalized Gauss sums and anticyclotomic Hecke L-values of imaginary quadratic fields at inert primes*，Theorem 4.5，准确假设为反圆分 \(\mathbf Z_p\) 塔中阶 \(p^n>1\) 的角色，以及指定 signed local-unit 模的 \(\Lambda\)-生成元。其 §4.1 已取 \(\Delta\)-不变量和 \(T^{-1}\) 扭曲。原 Robert \(U_7\) 的 tame 角色及高 Artin–Hasse 坐标不在该定理的直接范围；Theorem 2.5(ii) 在 tame 层仅给适当元素存在，(iii) 另需指定 tame 投影的小赋值假设，不能默认原元素满足。[原文 §§2、4](https://arxiv.org/html/2507.08221v1)。

本轮只建立 (B.1)–(B.5) 的实际接口和上面两个适用范围；未改变原 \(U_7\)、角色、根或余项。o2_high_coefficient 与 root 独立纸核阶乘、两模型符号和固定权论证，无新程序执行或有限窗口重算。继续求同一个 \(\mathfrak B_p\) 的实际高坐标，不以其它参数处或低坐标的单位代换。
