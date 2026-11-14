# 四阶中心零与完整有界矩仍不能单独降低实际 arithmeticity

日期：2026-11-12。**状态：以下固定反例完整成立。**

R44 只排除了中央 theta 对角的直接系数预算。
为研究真正的 vanishing-jet 评价映射，必须知道哪些额外 theta 结构会被使用。
下面给出一个固定的有理系数整函数模型：
它同时具有全部有界双变量矩和每个素数的四阶中心零，
但其图像不可能是任何 \(\alpha<1\) 的 \(\alpha\)-arithmetic germ。

这是关于所列抽象条件之间逻辑关系的反例。
它不是实际 \(E_{17}\) 的 Katz 测度、中央 theta 或 Selmer 模；
不否定这些对象尚未使用的额外结构。

## 1. 固定函数、完整矩与复增长

固定整数 \(a\ge2\)，定义
\[
F_a(Z)=\sum_{m\ge0}u_mZ^m,\qquad
u_m=\frac{(a^m-1)^4}{(m!)^2}\in\mathbb Q.
\tag{1.1}
\]
\(u_0=0\)，每个 \(m\ge1\) 的系数非零，所以它不是多项式。

对任意素数 \(p\nmid a\)，在 \(\mathbb Z_p^2\) 上取真正的有界
\(\mathbb Z_p\)-值原子测度
\[
\mu_{a,p}
=
\sum_{j=0}^4(-1)^{4-j}\binom4j\,\delta_{(a^j,1)}.
\tag{1.2}
\]
所有原子都在 \((\mathbb Z_p^\times)^2\) 中。
对全部 \(m\ge0\)，有准确式
\[
\boxed{\quad
(m!)^2u_m
=
\int_{\mathbb Z_p^2}(xy)^m\,d\mu_{a,p}(x,y)
=(a^m-1)^4.
\quad}
\tag{1.3}
\]
更一般的混合矩也存在：
\(\int x^ry^s\,d\mu_{a,p}=(a^r-1)^4\) 对全部 \(r,s\ge0\) 成立。
所以这里不是只有一条稀疏插值序列。

由于 \((a^m-1)^4\le a^{4m}\)，对 \(|Z|\le R\)，
\[
|F_a(Z)|\le\sum_{m\ge0}\frac{(a^4R)^m}{(m!)^2}.
\]
利用 \(\binom{2m}{m}\le4^m\)，右边至多为
\[
\sum_{m\ge0}\frac{(4a^4R)^m}{(2m)!}
=\cosh(2a^2\sqrt R)
\le e^{2a^2\sqrt R}.
\tag{1.4}
\]
故 \(F_a\) 是增长阶至多 \(1/2\) 的整函数。

单值整函数若代数于 \(\mathbb C(Z)\)，由代数方程的根界在无穷远具有
多项式增长，因而是多项式。
所以 \(F_a\) 超越于 \(\mathbb C(Z)\)。

## 2. 每个奇素数的中心 tame 分支恰有四阶零

固定奇素数 \(p\nmid a\)，写
\[
a=\omega_p(a)\langle a\rangle_p,\qquad
\omega_p(a)^{p-1}=1,\qquad
\langle a\rangle_p\in1+p\mathbb Z_p.
\]
令
\[
\ell_p=\frac{\log\langle a\rangle_p}{\log(1+p)}\in\mathbb Z_p.
\tag{2.1}
\]
其非零性不需要非 Wieferich 假设：
\(p\)-进对数在 \(1+p\mathbb Z_p\) 上单射，
若 \(\ell_p=0\)，则 \(a=\omega_p(a)\) 是根单位；
整数 \(a\ge2\) 不可能是根单位。

把 (1.2) 的乘积坐标投影到其 principal-unit 部分，
并选平凡 tame 字符，所得 Iwasawa 级数为
\[
\begin{aligned}
\mathcal F_{a,p}(T)
&=\sum_{j=0}^4(-1)^{4-j}\binom4j(1+T)^{j\ell_p}\\
&=\boxed{\big((1+T)^{\ell_p}-1\big)^4}.
\end{aligned}
\tag{2.2}
\]
因为 \(\ell_p\in\mathbb Z_p\)，这是一个整的有界测度级数。
它的 \(T^4\) 系数为 \(\ell_p^4\ne0\)，所以
\[
\operatorname{ord}_{T=0}\mathcal F_{a,p}=4.
\tag{2.3}
\]
\(\ell_p\) 可以被 \(p\) 整除；这不会把零阶从四改成无穷，
本文也没有给它一致的赋值上界。

若 \(p-1\mid m\)，则 \(\omega_p(a)^m=1\)，因此
\[
\boxed{\quad
\mathcal F_{a,p}\big((1+p)^m-1\big)
=(a^m-1)^4=(m!)^2u_m.
\quad}
\tag{2.4}
\]
这正是清楚指定了 tame 投影的中心插值。
若 \(p-1\nmid m\)，不能把 (2.4) 当成全部矩公式；
全部权由原始测度 (1.2) 给出，而各 tame 分支必须分别读取。

## 3. 对真正 \(\alpha\)-arithmetic 的下界

取 \(X=\mathbb P^2_{\mathbb Q}\) 中的形式图像
\[
\widehat C_a:\quad Y=F_a(Z)
\]
及有理基点 \((0,0)\)。
它光滑，因为第一坐标为形式参数 \(Z\)。
其 Zariski 闭包维数为二，因为 \(F_a\) 不代数。

映射
\[
\Theta_a:\mathbb C\longrightarrow X(\mathbb C),
\qquad Z\longmapsto[1:Z:F_a(Z)]
\]
是一致化。
其拉回 \(\mathcal O(-1)\) 的全局截面 \((1,Z,F_a(Z))\)
由 (1.4) 满足 Herblot Definition 5.1 的增长界，且
\(\rho\le1/2\)。

如果这个 germ 对某个 \(\alpha<1\) 是
\(\alpha\)-arithmetic，则可先略增 \(\alpha\) 到仍小于一的正数。
Herblot Theorem 6.1 对一个有理点 \(d=1\)、闭包维数 \(r=2\) 给
\[
\frac1\alpha\le\frac2{2-1}\rho\le1,
\]
矛盾。因此
\[
\boxed{\quad
\widehat C_a\text{ 不是任何 }\alpha<1
\text{ 的 }\alpha\text{-arithmetic germ}.
\quad}
\tag{3.1}
\]
这里直接使用的是原定理的评价映射结论，
没有以单个系数赋值或 graph size 代替 \(\alpha\)。

## 4. 对本题下一步的限制

这个固定模型同时满足：

- 有理系数、非多项式整函数，增长阶甚至至多 \(1/2\)；
- 对所有 \(p\nmid a\) 有一个包含全部混合矩的原始有界双变量测度；
- 平凡 tame 分支在每个这样的奇 \(p\) 的中心恰有四阶零；
- 但真实 \(\alpha\)-arithmetic 常数不能小于一。

因此仅从“完整有界矩 + 中心四阶零 + 整函数增长阶至多一”出发，
不能推出 Herblot 所需的 \(\alpha<1/2\)。
对实际中央 theta 继续研究时，必须显式加入其更强的
Kronecker/CM 关系或实际 vanishing-jet 整格。
本模型没有证明那些更强关系不能给出改善。

### 来源

本模型的测度、中心级数及增长估计均在本文直接证明。
唯一外部代数化输入是 Herblot，
*Algebraic points on meromorphic curves*（2012），
Definitions 5.1、5.4–5.5 及 Theorem 6.1：
[作者原文](https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf)。
该定理的规范已在本课题 Herblot 阈值笔记逐项核对。
