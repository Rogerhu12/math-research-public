# 中央对角在 ordinary 素数处的准确半径与系数预算

日期：2026-11-12。**状态：以下完整 ordinary 估计已证明。**

接续中央 theta 对角和中央对角整函数两篇笔记，令
\[
\mathscr D(Z)=\sum_{m\ge0}e_mZ^m,\qquad
e_m=\frac{d_m}{f^{2m+1}}\in\mathbb Q,\qquad f=34(1+i).
\]
已知 \(e_0=0\)，而 \(\mathscr D\) 不是多项式。
本篇证明 ordinary 处的完整二变量整性同时造成一个无法被中心零阶消去的
非目标 tame 系数列：

> 固定任意 \(m_0\ge1\) 使 \(d_{m_0}\ne0\)。
> 对几乎所有 \(p\equiv1\pmod4\)，
> \[
> v_p(e_{p-1+m_0})=-2.
> \]
> 更强地，在这些 \(p\) 处，\(\mathscr D\) 的准确收敛半径及其形式图形的
> size 都为 \(p^{-2/(p-1)}\)。
> 因此 ordinary 处的截断系数缩放预算准确为
> \[
> \mathcal B_{\mathrm{ord}}(k)=\log k+O(1).
> \]

这与该图像的 Herblot 充分门槛 \(\alpha<1/2\) 比较，
排除的是**直接用这套 size/系数预算**达到该门槛。
它不等于 Herblot 真正评价映射的最优 \(\alpha\) 下界，
不排除另一种整格、另一种对象或更精细的评价映射估计。

## 1. 两变量整级数及全部边界项

固定一个目标 ordinary 素数 \(p\)，令 \(\mathcal O\) 为
最大非分歧扩张的整数环完备化，包含导子 torsion 点的坐标。
沿用固定 theta 笔记的 \(256\) 点轨道 \(\mathcal S\)。

BK Corollary 2.17 的精确断言是
\[
\widehat\Theta_{z_0,w_0}(s,t)
-\langle w_0,z_0\rangle\delta(z_0)s^{-1}
-\delta(w_0)t^{-1}\in\mathcal O[[s,t]],
\tag{1.1}
\]
其中
\[
\widehat\Theta_{z_0,w_0}(s,t)
=\Theta_{z_0,w_0}(\log_E(s),\log_E(t)).
\]
本题每个 \(z_S\notin\Gamma\)，而 \(w_0=0\in\Gamma\)。
因此 \(\delta(z_S)=0,\delta(0)=1\)，只有第二坐标的极点项：
\[
H_p(s,t)=
\sum_{S\in\mathcal S}
\Theta_{z_S,0}(\log_E(s),\log_E(t))
-\frac{256}{t}
\in\mathcal O[[s,t]].
\tag{1.2}
\]
没有遗漏一个第一坐标的 \(s^{-1}\) 边界项。

BK 的 Weierstrass 模型记为
\(Y^2=4x^3-g_2x-g_3\)、参数 \(-2x/Y\)。
代入 \(Y=2y,g_2=68,g_3=0\)，恰是本题的
\(t=-x/y\) 和 \(\omega=dx/(2y)\)。
所以这里的参数、微分与 \(\Omega_p\) 均不需要再插入一个未追踪的 \(2\)。

取固定的整形式群同构
\[
\eta_p(t)=
\exp(\Omega_p^{-1}\log_E(t))-1:
\widehat E\simeq\widehat{\mathbb G}_m,\qquad
\Omega_p\in\mathcal O^\times,
\]
记其整逆为 \(\iota_p\)。
则
\[
J_p(S,T)=H_p(\iota_p(S),\iota_p(T))
\in\mathcal O[[S,T]].
\tag{1.3}
\]
以下对该**完整**级数取矩，不先限制到
\(\mathbb Z_p^\times\times\mathbb Z_p^\times\)，
也不先选 R40 的中心 tame 分支。

## 2. 全部混合矩的准确规范

令
\[
\partial_{S,\log}=(1+S)\frac{\partial}{\partial S},
\qquad
\partial_{T,\log}=(1+T)\frac{\partial}{\partial T}.
\]
对任意 \(a,b\ge1\)，定义
\[
A_{a,b}
=
\left.
\partial_{S,\log}^a\partial_{T,\log}^b
J_p(S,T)\right|_{S=T=0}.
\]
由于 (1.3) 是整级数，
\[
A_{a,b}\in\mathcal O.
\tag{2.1}
\]

现在精确比较原来的 additive theta 坐标。
有
\[
\log_E(\iota_p(S))=\Omega_p\log(1+S),
\]
故链式法则给
\[
\partial_{S,\log}=\Omega_p\partial_z,\qquad
\partial_{T,\log}=\Omega_p\partial_w.
\]
(1.2) 中的 \(256/\iota_p(T)\) 只依赖 \(T\)，
被任意正次的第一坐标导数消去。
而 \(\mathscr K(z,w)\) 的 \(256/w\) 也只依赖第二坐标。
所以在 \(a,b\ge1\) 的混合矩中，两种极点减法都不留下修正项：

\[
\boxed{\quad
A_{a,b}
=
\Omega_p^{a+b}a!b!\,[z^aw^b]\mathscr K(z,w).
\quad}
\tag{2.2}
\]
特别地，写
\[
A_m=A_{m,m}
=\Omega_p^{2m}(m!)^2d_m,\qquad m\ge1,
\]
得到
\[
\boxed{\quad A_m\in\mathcal O\quad(m\ge1).\quad}
\tag{2.3}
\]

这里的两个阶乘都保留了。
由于 \(p\nmid f\)，(2.3) 对有理下降系数给出
\[
v_p(e_m)\ge-2v_p(m!)\qquad(m\ge1).
\tag{2.4}
\]
这是对**所有权**的结论，不仅是 \(p-1\mid m\)。

也可通过 BK Proposition 3.1 解释 (2.2)：
\(J_p\) 对应一个 \(\mathcal O\)-值 \(\mathbb Z_p^2\) 测度，
\(A_m\) 是其 \((xy)^m\) 矩。
但下面的同余可以直接从整导子证明，无需额外使用测度规范。

## 3. 保留低权的精确模 \(p\) 周期

在特征 \(p\) 中，
\[
\partial_{S,\log}^{\,p}=\partial_{S,\log},
\qquad
\partial_{T,\log}^{\,p}=\partial_{T,\log}.
\tag{3.1}
\]
例如左边的 \(p\) 次幂仍是导子，且在生成元 \(S\) 上与右边相同；
或在多项式 \((1+S)^n\) 上直接使用 \(n^p=n\)。
对形式级数，任意给定系数只涉及有限截断，所以恒等式仍成立。

因为两个导子交换，(3.1) 应用于同一个整级数 \(J_p\)，给
\[
\boxed{\quad
A_{m+p-1}\equiv A_m\pmod p,\qquad m\ge1.
\quad}
\tag{3.2}
\]
更一般地，只要 \(m,m'\ge1\) 且 \(m\equiv m'\pmod{p-1}\)，
就有 \(A_m\equiv A_{m'}\pmod p\)。

周期式指的是 \(A_m\)，不能删除 \(\Omega_p^{2m}\) 或两个阶乘。
它也不能用于 \(m=0\) 而不另处理被减去的边界项。
本篇恰只需要一个正的固定 \(m_0\)。

## 4. 一个固定非零系数强制无穷的分母列

从中央整函数的非多项式性，固定任意
\[
m_0\ge1,\qquad d_{m_0}\ne0.
\]
\(m_0\) 不随 \(p\) 变化。
因为 \(e_{m_0}\in\mathbb Q^\times\)，除去有限个素数以后，
\[
v_p(e_{m_0})=v_p(d_{m_0})=0,\qquad p>m_0,
\]
且 \(m_0!\)、\(\Omega_p\) 都是单位。
于是 \(A_{m_0}\) 为单位。

(3.2) 因而对这些 \(p\) 的全部正整数
\(m\equiv m_0\pmod{p-1}\) 给出
\[
v_p(A_m)=0,\qquad
\boxed{\quad v_p(e_m)=-2v_p(m!).\quad}
\tag{4.1}
\]
尤其取 \(m=p-1+m_0\)。
当 \(p>m_0\) 时，\(p\le m<2p\)，所以
\[
\boxed{\quad v_p(e_{p-1+m_0})=-2.\quad}
\tag{4.2}
\]

这条分母列是完整 theta 测度的另一条 tame 权。
对于充分大的 \(p\)，固定的 \(m_0\) 既不等于零也不被 \(p-1\) 整除。
因此 R40 中心对应的 \(m\equiv0\pmod{p-1}\) 即使有额外高阶消失，
也不改变 (4.1) 的模 \(p\) 单位矩。

## 5. 准确收敛半径与完整 graph size

固定满足第 4 节条件的 ordinary \(p\)。
由 (2.4) 和 Legendre 公式，
\[
v_p(m!)=\frac{m-s_p(m)}{p-1},
\]
有
\[
\liminf_{m\to\infty}\frac{v_p(e_m)}m
\ge-\frac2{p-1}.
\]
沿 (4.1) 的无穷同余类，\(s_p(m)=O_p(\log m)\)，达到同一极限。
因此 Cauchy–Hadamard 公式给出准确半径
\[
\boxed{\quad R_p(\mathscr D)=p^{-2/(p-1)}.\quad}
\tag{5.1}
\]

在有限个素数之外，线性系数 \(e_1\) 为整。
先作整线性坐标变换减去 \(e_1Z\)，再加回 \(Z\)，
可以把图像变成首项为 \(Z\) 的标准图像，且不改变 \(m\ge2\) 系数。
Bost–Chambert-Loir Proposition 3.5(2) 的图像 Newton 公式于是为
\[
S_p(\widehat{\operatorname{graph}}\mathscr D)
=
\min\left(1,\inf_{m\ge2}|e_m|_p^{-1/(m-1)}\right).
\tag{5.2}
\]
Legendre 公式中的 \(s_p(m)\ge1\) 给
\[
\frac{2v_p(m!)}{m-1}\le\frac2{p-1}.
\]
结合 (2.4)，(5.2) 至少为 \(p^{-2/(p-1)}\)。
沿 (4.1) 的无穷同余类达到这个下确界，
所以
\[
\boxed{\quad
S_p(\widehat{\operatorname{graph}}\mathscr D)
=p^{-2/(p-1)}
\quad\text{对几乎所有 ordinary }p.
\quad}
\tag{5.3}
\]
因此这一固定图像在这些 places 的 size 逆乘积已经发散；
不能称它为 A-analytic。

(5.3) 是 graph size 的结论。
它本身不把所有可能的 Arakelov 评价映射估计都归约为这个 size。

## 6. 截断系数预算准确为 \(\log k\)

去掉上述固定有限例外集合，对 \(k\ge2\) 定义
\[
s_p(k)=
\max_{2\le m\le k}
\left(0,-\frac{v_p(e_m)}{m-1}\right),
\qquad
\mathcal B_{\rm ord}(k)
=\sum_{\substack{p\equiv1\ (4)\\p\text{ good}}}
s_p(k)\log p.
\tag{6.1}
\]
该有限例外集合的加入或删去只改变 \(O(1)\)：
(2.4) 本身给每个目标 ordinary 处的正半径及一致的系数线性界；
其它固定模型坏位可在定义中直接留在删去集合内。

上界方面，由 (2.4)，
\[
s_p(k)\le\frac2{p-1}.
\]
若 \(p>k\)，所有涉及的阶乘都是单位，所以 \(s_p(k)=0\)。
下界由 (4.2) 给出。因此
\[
2\sum_{\substack{p\le k-m_0+1\\p\equiv1\ (4)\\p\notin S}}
\frac{\log p}{p+m_0-2}
\le \mathcal B_{\rm ord}(k)
\le
2\sum_{\substack{p\le k\\p\equiv1\ (4)\\p\notin S}}
\frac{\log p}{p-1}+O(1).
\tag{6.2}
\]
这里 \(S\) 为固定有限集合。

两种分母与 \(p\) 的差只贡献收敛的
\(O(\sum_p\log p/p^2)\)，固定长度的截断差也有界。
与 R38 相同，模 \(4\) 素数定理及分部求和给
\[
\sum_{\substack{p\le k\\p\equiv1\ (4)}}\frac{\log p}{p}
=\frac12\log k+O(1).
\]
所以
\[
\boxed{\quad
\mathcal B_{\rm ord}(k)=\log k+O(1).
\quad}
\tag{6.3}
\]

这是所有 ordinary 系数的完整上下界，不是只展示一个反例素数，
也没有把一个随 \(p\) 改变的固定低权当作真正固定的 \(m_0\)。

## 7. 对 Herblot 尝试的确切影响

中央整函数笔记已得到一个固定 \(\mathbb Q\)-有理非代数 graph，
复增长阶至多一。
Herblot Theorem 6.1 对单一有理点、闭包维数二的充分算术门槛是
\(\alpha<1/2\)。

本篇的 ordinary 预算已经是 \(\log k+O(1)\)，
尚未加上 inert places。
所以仅用先前“把第 \(k\) 阶截断缩放到整”的充分条件，
不会因为假定几乎全部目标 \(p\) 的中心零阶至少四，
就得到所需的 \(\alpha<1/2\)。
第 4 节明确指出了中心假设没有控制、但仍为单位矩的另一个固定 tame 权。

这项结论仍然没有证明以下更强说法：

- 不证明 graph 的最优 \(\alpha\)-arithmetic 常数至少为一；
- 不证明所有评价映射的整格都不能改善；
- 不排除一个固定的导出对象或新的 theta 平方根改变整个权结构；
- 不把对本图像的 size 障碍扩张为主课题的不可能性。

Herblot 真正使用的是所有截面、所有 jet 的评价映射高度。
若要绕过 (6.3)，必须直接研究该整格或改变对象，
不能仍把相同的截断系数最大值称作已经下降的算术预算。

## 来源与规范核查

- Bannai–Kobayashi，*Algebraic theta functions and the p-adic interpolation
  of Eisenstein–Kronecker numbers*，Duke Math. J. 153 (2010)，229–295：
  [作者原文](https://arxiv.org/abs/math/0610163)，
  印刷页 29–30 的 Corollaries 2.16–2.17，
  印刷页 35–36 的 Proposition 3.1、Definition 3.2 和
  \(\eta_p,\Omega_p\) 规范。
  Corollary 2.17 的 ordinary 假设已保留；没有用于 inert places。
  本文混合矩直接消去了该文随后特别提醒的 \(s^{-1},t^{-1}\) 边界问题。
- 本课题中央 theta 对角笔记：固定 \(256\) 点轨道、\(d_m\in K\)、
  及 \(\mathscr K\) 的定义。
- 本课题中央对角整函数笔记：\(e_m\in\mathbb Q\)、非多项式性。
  本篇只需由此固定一个正权非零系数，没有预设任何 Sha 有限性。
- Bost–Chambert-Loir，*Analytic curves in algebraic varieties over number fields*，
  *Algebra, Arithmetic, and Geometry: In Honor of Yu. I. Manin* (2009)，
  Proposition 3.5(2)，
  [作者原文](https://arxiv.org/abs/math/0702593)。
  所用 graph 公式也在 R38 §4 已逐项核对。
