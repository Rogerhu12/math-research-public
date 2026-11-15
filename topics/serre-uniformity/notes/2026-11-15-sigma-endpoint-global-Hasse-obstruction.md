# 原末项对 DA/Delta 的全 supersingular 恒等障碍

日期：2026-11-15。状态：**下面的全 supersingular locus 不可能性已证明；固定 j=0 的 CM 专属端项恒等仍未排除。** 本篇不是新的原临界非零结论。

## 1. 原末项的全层延拓与权

固定 \(p=6N+5\ge41\)。在全层通用短 Weierstrass 模型
\[
 E_{a,b}:y^2=x^3-\frac a4x-\frac b4,\qquad
 dz=\frac{dx}{2y},\qquad \Delta=a^3-27b^2,
 \tag{EB1}
\]
中使用原 \(c=0\) sigma：
\[
 \sigma=z+O(z^5),\qquad
 (\log\sigma)''=-x,\qquad
 F=x\sigma^6,\quad G=-xy\sigma^6.
\]
这里 \(\mathrm{wt}(a)=4,\ \mathrm{wt}(b)=6,\ \mathrm{wt}(\Delta)=12\)。
定义两个原全局系数
\[
 \mathfrak f_p(a,b)=[z^{p-7}]F,\qquad
 \mathfrak g_p(a,b)=[z^{p-10}]G.
 \tag{EB2}
\]
在 \(a=0,b=4\) 时，它们准确分别为 R770 的
\(f_{N-1},g_{N-1}\)。

两个系数都在 \(\mathbf Z_{(p)}[a,b]\) 中：
所需 \(\sigma^6\) 的最高次数为 \(p-5<p\)；
原 sigma 的 Hurwitz 整性使该范围的普通系数 p 整。
由 \(-(\log\sigma)''=x\) 与 \(y=x'/2\) 得到的所需低阶 Laurent
系数也只使用小于 p 的积分/对数分母。等价地可用 R697 的原低阶整性论证。
齐次性给
\[
 \mathfrak f_p,\mathfrak g_p\in M_{p-11}
 =\mathbf F_p[a,b]_{p-11}.
 \tag{EB3}
\]
因为 F 的整体权为 \(-4\)，G 的整体权为 \(-1\)，
(EB2) 的两种次数都准确给权 \(p-11\)。
不能把两者误写成同一 z 次数。

令 A 为同一原 Hasse 多项式，归一为 R812 的
\(\sigma_p=A\) 模 p；其权为 \(p-1\)。
使用原 Serre/heat 导子
\[
 D=6b\,\partial_a+\frac{a^2}{3}\,\partial_b,
 \qquad D:M_k\longrightarrow M_{k+2}.
 \tag{EB4}
\]
在 R812 的固定判别式截面 \(a=3X,b=Y\) 上，
这就是 \(DX=2Y,DY=3X^2\)；没有换导子。

## 2. DA 的准确 Tate 常数

把全层模形式代入
\[
 a(q)=E_4(q)/12,\qquad b(q)=-E_6(q)/216 .
 \tag{EB5}
\]
Ramanujan 方程直接给，对于权 k 的任意齐次多项式 H，
\[
 (DH)(a(q),b(q))
 =\theta_q H(a(q),b(q))
  -\frac{k}{12}E_2(q)H(a(q),b(q)).
 \tag{EB6}
\]
同一 A 的 q 展开模 p 为 1；这也正是 R812(812.17)
\(A=\lambda^{p-1}\) 在去掉权因子后的归一。
因此
\[
 \boxed{(DA)(q)=E_2(q)/12\pmod p,\qquad
        \operatorname{CT}_q(DA)=1/12\ne0.}
 \tag{EB7}
\]
这里不需要给 \(E_2\) 另选一个 supersingular 值；
仅使用它的合法 q 展开和常数项。

而
\[
 \Delta(a(q),b(q))
 =(E_4^3-E_6^2)/1728
 =q+O(q^2).
 \tag{EB8}
\]
所以 \(\Delta\) 乘上任何全层 holomorphic 模形式的 q 常数都是零。

## 3. Hasse 零的简单性

为明确下面的“模 A”含义，在 p>3 的光滑模曲线栈上，A 的零
正是 supersingular locus，且都是简单零。

简单性也可在 étale 的完整二阶标记覆盖上直接核：
Legendre 模型的 Hasse 多项式只差一个单位等于
\[
 H(\lambda)=\sum_{j=0}^{m}\binom mj^2\lambda^j,
 \qquad m=(p-1)/2<p .
\]
有 \(H(0)=1,\ H(1)=\binom{p-1}{m}\ne0\)，并且模 p 满足
\[
 \lambda(1-\lambda)H''+(1-2\lambda)H'
   -\frac14 H=0 .
\]
若 H 在 \(\lambda_0\ne0,1\) 处与 H' 同时为零，
逐次微分这个方程便迫使它的全部小于 p 的导数在该点为零。
由于 \(\deg H<p\)，这与 \(H(0)=1\) 矛盾。
因此 A 在
\(\mathbf F_p[a,b,\Delta^{-1}]\) 中的主理想是 radical。
此外 \(A\) 与 \(\Delta\) 互素，因为 A 的 Tate q 常数为一。

## 4. 不可能性引理

**引理。** 对每个本篇的 p，不存在模参数无关的常数
\(\alpha,\beta,\gamma\in\mathbf F_p,\ \gamma\ne0\)，使
\[
 \boxed{
 \Delta(\alpha\mathfrak f_p+\beta\mathfrak g_p)
   =\gamma DA
 }
 \tag{EB9}
\]
在**全部几何 supersingular 曲线及非零不变微分**上成立。

这些常数可以随 p 变动；结论不要求其来自固定的有理数。
但它们必须是 \(\mathbf F_p\) 常数，不包括依赖 j 的有理函数系数。

证明。令
\[
 Z=\Delta(\alpha\mathfrak f_p+\beta\mathfrak g_p)-\gamma DA.
\]
这是 \(\mathbf F_p[a,b]\) 中权 \(p+1\) 的齐次多项式。
若 (EB9) 在全部 supersingular locus 成立，
§3 的简单性给 A 在局部化环中整除 Z。
又 \((A,\Delta)=1\)，故在 \(\mathbf F_p[a,b]\) 中已有 \(A\mid Z\)。

商的权为 \((p+1)-(p-1)=2\)。
但 \(\mathbf F_p[a,b]_2=0\)，因为 2 不能写成非负整数的
\(4u+6v\)。故 Z 必须恒为零。
取 Tate q 常数，由 (EB7)--(EB8) 得
\[
 0=\operatorname{CT}_qZ=-\gamma/12,
\]
与 \(\gamma\ne0\) 矛盾。证毕。

## 5. 对固定原 CM 点的严格边界

引理只排除了用全 supersingular locus 上的
“同权加模 A”来得到原末项 Cartier 单位的路线。
它没有排除单独在原 \(a=0,b=4\) 处的额外 CM congruence；
在该点 \(A=0,DA=B\ne0\)，同权本身仍不决定
\(\mathfrak f_p(0,4)\) 或 \(\mathfrak g_p(0,4)\)。

本篇也没有排除含额外模形式/变参数系数或额外端项的恒等式，
没有宣称 R765 的较高总指标残差已被降到 R770 临界指标，
并且没有证明任何原同一 primitive/Legendre 标签上的共同非零。

依赖：R697 的原 c=0 低阶整性；R770 的两条原系数定义；
[R812](../results/R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md)
的 A、D 与 Tate/heat 归一。
