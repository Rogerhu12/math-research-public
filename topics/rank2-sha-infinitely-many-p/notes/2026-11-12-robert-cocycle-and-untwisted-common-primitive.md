# Robert cocycle 与两个无 twist 差分通道：实系数共同 germ 的代数性

日期：2026-11-12。

**后续加强。** [R42](../results/R42-coprime-cm-difference-primitives.md)
已用有限 principal-parts 模去掉实系数假设，并把结论加强为属于原来的
$\mathbb C(E)$；[R43](../results/R43-twisted-cm-primitive-classification.md)
又分类了带固定常数 twist 的标量差分幂。本篇保留 de Shalit 已发表版本的
准确范围及 Robert cocycle 核查；下文提到的单个 $K$-germ 缺口现由 R42 解决。

本篇考察 R41 的两个固定乘子
\[
b_1=2+i,\qquad b_2=3+2i
\]
是否能通过**兼容的有理右端**作用于同一个非代数 germ，从而真正取得
R41 已证明可求和的共同惰性深度。

得到一个比“原来那个差分逆像不能再用第二乘子”更一般的结论：

> 若同一个实系数形式 Laurent germ \(F\) 同时满足
> \[
> (\sigma_{b_1}-1)^mF\in\mathbb C(E),\qquad
> (\sigma_{b_2}-1)^mF\in\mathbb C(E),
> \]
> 则 \(F\) 在 \(E\) 的某个有限 isogeny 覆盖上是有理函数，因而在
> \(\mathbb C(E)\) 上代数。
>
> 特别地，不能用两个这样的有理右端构造所需的非代数 **\(\mathbb Q\)-germ**。
> 本结论不假定两个右端相同，也不假定它们来自原来固定的 \(\Phi\)。

证明只调用 de Shalit 已发表定理的**互素正整数**版本。
不把文献未在正文展开的 CM 扩张当作已可引用定理。
对不由复共轭固定的单个 \(K=\mathbb Q(i)\)-germ，下面的降到范数步骤失效；
本篇不声称已经排除该情形。

## 1. 符号与已核原始定理

取
\[
E:y^2=x^3-17x,\qquad
\Lambda=\Omega\mathbb Z[i],\quad \Omega>0,
\qquad (\sigma_b f)(z)=f(bz).
\]
这里 \(z=\log_E(t)\)，\(t=-x/y\)。
形式换元 \(t\leftrightarrow z\) 的系数都在 \(\mathbb Q\)，
故 \(\mathbb Q((t))\) 中的 germ 在 \(z\) 坐标仍由复共轭固定。

令
\[
\mathcal K=\bigcup_{\Lambda'\subset\Lambda}\mathbb C(E_{\Lambda'})
\]
为所有有限无分歧椭圆覆盖的函数域之并，嵌入 \(\mathbb C((z))\)。

所用来源是 Ehud de Shalit,
*Elliptic \((p,q)\)-difference modules*,
**Algebra & Number Theory 15 (2021), 1303–1342**,
DOI [10.2140/ant.2021.15.1303](https://doi.org/10.2140/ant.2021.15.1303)。
已直接逐项核对作者原文
[arXiv:2007.09508v2](https://arxiv.org/abs/2007.09508v2)，
§6.2 **Theorem 37** 及 **Remark 38(ii)**：

若 \(p,q>1\) 是互素正整数，且一个形式 Laurent 级数分别满足
关于 \(f(pz)\) 和 \(f(qz)\) 的非零线性差分方程，系数在 \(\mathcal K\)，则
\[
f\in \mathcal K[z,z^{-1},\zeta(z,\Lambda)].
\tag{1.1}
\]
作者先以 \(z/p,z/q\) 记号陈述，Remark 38(ii) 明确给出上述逆方向等价形式。
同节还证明，加入任一个有限指数子格的 \(\zeta\) 得到相同的环。

原文开头说明 CM 情形可考虑独立的 endomorphisms，但明确没有在文中展开。
本篇不用这一句话扩大 Theorem 37 的适用范围。
也不把“乘法独立”替换正文要求的“互素”：下面实际使用 \(p=5,q=13\)。

## 2. 共轭与二项式把两个 CM 通道降为整数通道

假定 \(\overline F=F\) 且
\[
D_{b_j}^mF=h_j,\qquad
D_b=\sigma_b-1,\qquad h_j\in\mathbb C(E).
\tag{2.1}
\]
因为 \(\bar\Lambda=\Lambda\)，对形式级数逐系数共轭给出
\[
D_{\bar b_j}^mF=\bar h_j\in\mathbb C(E).
\tag{2.2}
\]
对 \(N=b\bar b\)，有交换算子恒等式
\[
D_N=D_b+\sigma_bD_{\bar b}.
\tag{2.3}
\]
展开 \(D_N^{2m-1}\)。
每一项或者含 \(D_b\) 至少 \(m\) 次，或者含 \(D_{\bar b}\) 至少 \(m\) 次。
因此每一项作用于 \(F\) 都是椭圆有理函数，且
\[
D_5^{\,2m-1}F\in\mathbb C(E),\qquad
D_{13}^{\,2m-1}F\in\mathbb C(E).
\tag{2.4}
\]
这里 \([b]\) 保持 \(\Lambda\)，故作用于有理函数不会离开
\(\mathbb C(E)\)。

若 \(D_N^MF=h\ne0\)，再左乘
\[
\sigma_N-\frac{\sigma_Nh}{h}
\]
便得到一个非零齐次线性差分方程；若 \(h=0\)，已有齐次方程。
其首项和末项都非零，故没有把零算子当作方程。
对 \(N=5,13\) 应用 (1.1)，得到
\[
F\in\mathcal K[z,z^{-1},\zeta(z,\Lambda)].
\tag{2.5}
\]

这一步中 \(\bar F=F\) 是实际使用的条件。
若仅 \(F\in K((z))\)，共轭得到的是 \(D_{\bar b}^m\bar F=\bar h\)，
并没有得到 \(D_{\bar b}^mF\in\mathcal K\)。
对 \(F+\bar F\) 只能直接写出含两种因子的混合算子；
不能把它误写成 (2.4)。

## 3. 环中两个形式变量的独立性

把 (2.5) 中有限多个椭圆系数的周期格同时缩小到 \(N\Lambda\)。
可以取整数 \(N\ge1\)，所以新的格仍由 \(\mathbb Z[i]\) 保持。
由原文的换格关系，可把 (2.5) 写为
\[
F=\sum_{n=0}^{n_0}\sum_{r=r_-}^{r_+}
a_{n,r}(z)\,z^r Z(z)^n,\qquad
Z(z)=\zeta(z,N\Lambda),\quad
a_{n,r}\in\mathbb C(E_{N\Lambda}).
\tag{3.1}
\]

这里 \(z,Z\) 在椭圆函数域上代数独立。
给一个直接证明以保证下面比较系数合法。
若它们满足多项式关系，固定一个不落在各系数或 \(Z\) 极点上的一般 \(z_0\)。
对任意 \(\lambda\in N\Lambda\)，系数在 \(z_0+\lambda\) 不变，而
\[
z_0+\lambda,\qquad Z(z_0)+\eta(\lambda)
\]
仍满足同一个复多项式。
取格基 \(\omega_1,\omega_2\)。
Legendre 关系使
\[
\det
\begin{pmatrix}
\omega_1&\omega_2\\
\eta(\omega_1)&\eta(\omega_2)
\end{pmatrix}\ne0.
\]
因此这些点是一个可逆复线性变换下的 \(\mathbb Z^2\) 网格，
在 \(\mathbb C^2\) 中 Zariski 稠密。
该多项式必须为零，多项式系数在一般 \(z_0\) 全为零，
从而原关系为零。对 Laurent 表达式先乘以足够的 \(z\) 次幂即可。

由于格为方格，
\[
Z(iz)=-iZ(z),\qquad \eta(i\lambda)=-i\eta(\lambda).
\]
若 \(b\in\mathbb Z[i]\)，于是
\[
\sigma_bZ=\bar b\,Z+r_b,\qquad
r_b\in\mathbb C(E_{N\Lambda}).
\tag{3.2}
\]
这是直接由两边在格平移下具有相同增量得到的椭圆性，
不是把 \(\zeta\) 本身当作椭圆函数。

## 4. 椭圆系数的有限极点引理

**引理。** 设 \(a\in\mathbb C(E_{N\Lambda})\)，\(c\in\mathbb C^\times\)，
\(b\in\mathbb Z[i]\) 且 \(N b>1\)。
若
\[
(c\sigma_b-1)^m a=0,
\tag{4.1}
\]
则 \(a\) 为常数；若这个常数非零，还必须 \(c=1\)。

**证明。**
(4.1) 的首项系数非零，故
\[
W=\operatorname{span}_{\mathbb C}
\{a,\sigma_ba,\ldots,\sigma_b^{m-1}a\}
\]
为有限维的 \(\sigma_b\)-稳定空间。
令 \(S\) 是 \(W\) 中所有函数极点支持的并。
选一组基便知 \(S\) 有限。
若 \(s\in S\)，某个 \(w\in W\) 在 \(s\) 有极点；
\(\sigma_bw\in W\) 在 \([b]^{-1}s\) 的每个点都有极点，因为
\([b]\) 是特征零的 étale isogeny。因此
\[
[b]^{-1}S\subseteq S.
\]
若 \(S\ne\varnothing\)，左边有 \(N b\cdot |S|>|S|\) 个点，矛盾。
所以所有 \(W\) 中的函数无极点，因紧性都是常数。
代回 (4.1) 得 \((c-1)^m a=0\)。\(\square\)

这个证明只用极点支持，不需要高度估计或任何跨素数结论。

## 5. 排除 \(z\) 与 \(\zeta\) 部分

现在只用第一个原始通道
\[
(\sigma_{2+i}-1)^mF\in\mathbb C(E).
\tag{5.1}
\]
记 \(b=2+i\)。若 (3.1) 中最大的 \(Z\) 次数 \(n_0>0\)，
由 (3.2) 取 \(Z^{n_0}z^r\) 的系数，得到
\[
\bigl(b^r\bar b^{\,n_0}\sigma_b-1\bigr)^m a_{n_0,r}=0.
\tag{5.2}
\]
右端 (5.1) 的 \(Z\) 次数为零，且较低次数不会贡献到最高次数。
第 4 节引理表明，每个非零 \(a_{n_0,r}\) 为常数，并要求
\[
b^r\bar b^{\,n_0}=1.
\tag{5.3}
\]
取复绝对值得 \(r=-n_0\)。
再代回，要求 \((\bar b/b)^{n_0}=1\)，不可能：
\(b\) 与 \(\bar b\) 生成不同的 Gaussian 素理想，
所以 \(b/\bar b\) 不是根单位。
故 \(n_0=0\)。

因此 \(F=\sum_ra_rz^r\)。
对 (5.1) 中每个 \(r\ne0\) 比较系数，有
\[
(b^r\sigma_b-1)^ma_r=0.
\]
同一引理要求非零项满足 \(b^r=1\)，又不可能。
最终只剩
\[
F=a_0\in\mathbb C(E_{N\Lambda}).
\tag{5.4}
\]
这完成开头的代数性结论。

若 \(F\in\mathbb Q((t))\)，还可以把结论下降到 \(\mathbb Q(t)\) 上代数：
清除一个复系数代数关系的分母后，有限多个 \(t^jF^r\) 的
Taylor 系数构成有理系数线性系统。
其复解空间非零，有限维秩由有限多行实现，故存在非零有理解。
不过排除所需非代数参数曲线已经只需 (5.4)。

## 6. 兼容右端的实际含义

若希望从两个有理函数 \(h_1,h_2\) 出发，需要
\[
D_{b_2}^m h_1=D_{b_1}^m h_2.
\tag{6.1}
\]
假定两者在 \(O\) 正则且常数项为零。
因 \(|b_j|>1\)，所有正权的 \(b_j^k-1\) 都非零。
(6.1) 逐系数保证
\[
\frac{(h_1)_k}{(b_1^k-1)^m}
=
\frac{(h_2)_k}{(b_2^k-1)^m}.
\tag{6.2}
\]
故存在唯一常数项为零的共同形式解。
若这个共同解具有实系数，前面的定理就已经迫使它代数。

因此单纯要求 (6.1) 并寻找两个复杂的 Robert 有理右端，
不会自动产生同时满足以下三点的对象：

- 同一个 \(\mathbb Q\)-germ；
- 两个无 twist 的 \(D_{b_j}^m\) 有理右端通道；
- 对 Herblot 应用所需的非代数性。

这与 R41 的纯算术定理完全相容。
R41 证明的是一个给定共同深度的收敛性，未断言存在上述 germ。
也不排除算子右端不为椭圆有理函数、非实共同 germ、
非标量系统或更一般局部整性渠道。

## 7. Robert 的可用 cocycle 为什么带有 norm twist

这一段只指出算子区别，不重复另一个分支的显式 division-polynomial 计算。

对奇度 \(b\in\mathbb Z[i]\)，标准 Robert 函数的除子按本仓库规范为
\[
\operatorname{div}\Theta_b
=
12\bigl(Nb[O]-[b]^*[O]\bigr).
\tag{7.1}
\]
其常数归一化不影响对数导数。
记 \(\delta=d/dz\)。在方格上有
\[
\boxed{\quad
\delta\log\Theta_b
=
12\{Nb\,\zeta(z)-b\,\zeta(bz)\}
=
-12b(\sigma_b-\bar b)\zeta.
\quad}
\tag{7.2}
\]

可不借助 sigma 函数的规范直接验证 (7.2)：
右边由 \(\eta(b\lambda)=\bar b\eta(\lambda)\) 是椭圆函数；
它在 \(O\) 的留数为 \(12(Nb-1)\)，在其余 \(b\)-division 点的留数为
\(-12\)，正好等于左边。
两边的差为常数；标准对称的 Robert 函数使左边为奇函数，
右边也为奇函数，故常数为零。

于是辅助理想 cocycle 在对数导数层提供的是
\[
\sigma_b-\bar b,
\tag{7.3}
\]
不是 R41 需要的 \(\sigma_b-1\)。
在 sigma 的对数层相应出现 \(\sigma_b-Nb\)。
对惰性 \(p\)，Frobenius 恰给
\[
b^p\equiv\bar b\pmod p,\qquad
b^{p+1}\equiv Nb\pmod p.
\tag{7.4}
\]
这是所有固定 \(b\) 在同一首权上的共同共振，
与 R41 的 \(b_j^k-1\) 共同阶数不同。

另一个可直接验证的范围限制是：
有限个非零代数 torsion 平移的 zeta 线性组合
\[
Z_S(z)=\sum_s w_s\{\zeta(z+z_s)-\zeta(z_s)\}
\]
在格平移下的增量为 \((\sum_sw_s)\eta(\lambda)\)。
权重和为零时，它已经是有限椭圆覆盖上的有理函数；
权重和非零时，它保留 (7.3) 的反 CM 准周期字符。
仅靠抵消这些准周期不能留下一个既非代数、又带无 twist cocycle 的共同原函数。

## 8. 未被本篇处理的具体出口

1. **非实 \(K\)-germ。**
   不能把共轭作用在 \(F\) 上略去；若要排除或构造这一情形，
   需要额外的 CM 两差分分类证明，或新的兼容 cocycle。

2. **非有理右端或向量系统。**
   第 6 节的代数性定理是标量、有理右端结论。
   一个向量的两种局部整性渠道未必要求各坐标都满足 (2.1)。

3. **算术整性本身。**
   即使找到超出上述范围的共同对象，仍须证明实际 graph 大小，
   并处理 ordinary 处的目标 tame 块及额外共振；
   R41 的可求和惰性预算不等于这些条件。

本篇新增的实质边界是完整的实系数共同 germ 代数性证明，
不是把尚未构造出的跨素数工具列为已排除。
