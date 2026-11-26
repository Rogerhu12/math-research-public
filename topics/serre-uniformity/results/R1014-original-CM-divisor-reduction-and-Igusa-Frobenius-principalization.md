# R1014：原 CM 点差在 compact-type 纤维上的显式主化

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明：对 \(p>37,\ p\equiv11\pmod{12}\)，原 \(X_1\) 的指定 CM 点差 \(D_0\) 在实际良好约化 Jacobian 中的约化被 \(p-1\) 杀掉。** 证明保留唯一 Igusa 中心与全部三个实际 Drinfeld 尾上的类，特别保留 exotic Igusa 遗忘映射的不可分 Frobenius。该结论为 R1011 的实际非 CM 点提供一个无需除以 \(p\) 的形式零邻域来源；首个非零提升及商投影后的单位性仍未证明。

## 1. 同一曲线、点差与底环

设
\[
X_1=\operatorname{Norm}\left(
 X_{\rm ns}^+(p)\times_{\mathbf P^1_j}\mathbf P^1_a\right),
\qquad j=6912a^3(1-a^3),
\]
\[
c_\xi=\delta^i c_1\quad(\xi=\zeta^i,\ i=0,1,2),\qquad
D_0=2[c_1]-[c_\zeta]-[c_{\zeta^2}].
\tag{1014.1}
\]
这里是 R376/R1010/R1011 的原标准非分裂 CM 项链，不换成任意 \(j=0\) 点。\(D_0\) 在 \(\mathbf Q\) 上定义。

令 \(K_0\) 为最大未分歧 \(\mathbf Q_p\) 扩张的完备化，剩余域为
\(k=\overline{\mathbf F}_p\)。先取分歧指数
\[
e_0=(p^2-1)/2
\]
的 tame 扩张，必要时再作 tame 扩张和正则化；记底环为 \(R\)。
这些扩张不改变以下几何约化类。因 \(p\equiv2\pmod3\)，四在
\(\mathbf Q_p\) 中有唯一立方根，故原 \(\kappa_4\) 三次扭曲在此已平凡。

**结论。** 在 \(R\) 上 \(J_1=\operatorname{Jac}(X_1)\) 有好约化，且
\[
\boxed{\quad \operatorname{red}\bigl((p-1)D_0\bigr)=0.\quad}
\tag{1014.2}
\]
任一实际同态 \(q:J_1\to C\) 的 abelian quotient 也有好约化，并满足
\[
\operatorname{red}\bigl((p-1)\beta\bigr)=0,\qquad \beta=q(D_0).
\tag{1014.3}
\]
对 R1011 的 \(C,\beta\)，仍须加该篇的非挠范围；在当前同余类可用 \(p\ge431\)。本篇约化命题本身对全部所述 \(p>37\) 成立。

## 2. 原辅助六层的实际特殊纤维是树

先加 full level six，使辅助模问题 representable、有限 étale，并在每个几何连通分量上使用 Edixhoven–Parent (2021), Theorem 3.3。因 \(p\equiv-1\pmod4\)，其模型有一个 Igusa vertical part，每个 supersingular 辅助点接一个 Drinfeld 分量；原细节点的局部式为 \(uv=\pi_0\)。

这里不能直接假设该 Igusa part 连通。对一个细 supersingular 点，标准 Igusa cover 的局部式由 Hasse 简单零给出
\[
z^{p-1}=t\cdot\text{单位}.
\tag{1014.4}
\]
其 inertia 已是全部 \(\mathbf F_p^\times\)。因此在这个辅助连通分量上的 Igusa cover 连通，除去 \(\{\pm1\}\) 后仍连通。只需选一个 \(j=0\) 的细提升即可；原 Hasse 的单位一次系数已在 R378 (378.18) 核准。

再取实际 \(H_6\) 商。它的阶只含二和三，与 \(p\) 互素；vertical locus 与 horizontal locus 分别被保持。原星形图的商仍是星形图。节点处的 tame 商和随后正则化只使边细分；有理链不产生回路，光滑点的 tame 商也不产生新的回路。辅助几何分量间的置换不改变所选连通商的这个结论。

所以原 \(X_1\) 有 compact-type 半稳定模型 \(\mathcal X/R\)：其对偶图为树。记唯一 Igusa 中心为 \(I\)。每个其余正亏格分量只在一个点与中心连接，允许中间有正则化的有理链。

对一条树形 nodal 曲线，标准 normalization 精确列给
\[
1\longrightarrow\mathbf G_m^{\,b_1(\Gamma)}
 \longrightarrow\operatorname{Pic}^0(\mathcal X_k)
 \longrightarrow\prod_T\operatorname{Jac}(T)
 \longrightarrow0.
\]
这里 \(b_1(\Gamma)=0\)。具体地，每个节点的 gluing 标量可以沿树逐叶重新规范，最后没有剩余标量。因此
\[
\operatorname{Pic}^0(\mathcal X_k)
 \simeq\prod_T\operatorname{Jac}(T).
\tag{1014.5}
\]
半稳定 Jacobian 的相对 Picard/Néron 描述于是给 \(J_1\) 好约化，其特殊纤维正是这个乘积。不能把只有 Drinfeld 部分的类当成整个 Jacobian 的约化。

## 3. 遗忘映射的真实 Frobenius 与 Igusa 主函数

置
\[
m=(p-1)/2.
\]
标准 Igusa 对象是 \((E,P)\)，其中 \(P\) 是
\(\ker V_E\subset E^{(p)}\) 的生成元；原 full-\(p\) 模型的 vertical 对象则是 exotic Igusa。Edixhoven–Parent §2.1、Theorem 2.1 给实际同构
\[
(E,P)\longmapsto(E^{(p)},(0,P)).
\tag{1014.6}
\]
故这不是两个具有相同原遗忘映射的抽象曲线。

prime-to-\(p\) 的六标记沿相对 Frobenius 唯一运输，且实际 \(H_6\) 在
\(\mathbf F_p\) 上定义。因而在稠密 ordinary locus 上，若 \(b\) 表示标准 Igusa 所在辅助 \(\mathbf P^1\) 的原参数，\(a\) 表示 (1014.1) 的实际遗忘参数，则
\[
\boxed{\quad a=b^p\quad\text{在 }k(I)\text{ 中}.\quad}
\tag{1014.7}
\]
取 \(H_6\) 商与 Frobenius 运输相容，故该等式在商后仍成立；
普通点上的等式已确定整个函数域中的等式。\(k\) 完美，所取 \(p\) 次根唯一。

标准 Igusa 映射
\[
I\longrightarrow\mathbf P^1_b
\tag{1014.8}
\]
可分度为 \(m\)：一般 ordinary 标记的 Igusa 生成元模 \(\pm1\) 恰有 \(m\) 个，辅助六层在一般点没有额外有效稳定子。原
\(I\to\mathbf P^1_a\) 的度则为 \(pm\)，不可分度为 \(p\)；它与原
\(X_1\to\mathbf P^1_a\) 的总次数 \(p(p-1)/2\) 相符。

在原三个附着点 \(s_\xi\in I\) 处，
\[
b(s_\xi)=\xi^{1/p}=\xi^p.
\]
映射 (1014.8) 在这些点全分歧，指数为 \(m\)。可直接检查原额外自同构：R376 §2 证明 \(a^3=1\) 的三个支都保留有效 \(\mu_3\)。在细模点，(1014.4) 除去 \(\pm1\) 后成为
\(t=q^m\cdot\text{单位}\)；辅助 \(\mu_3\) 商将底参数取 \(t^3\)，上参数取 \(q^3\)。因
\[
p\equiv11\pmod{12}\quad\Longrightarrow\quad (m,3)=1,
\]
商后仍为指数 \(m\) 的全分歧，而没有分裂成三个点。Hensel 单位调整给局部参数
\(w_\xi\) 满足 \(b-\xi^p=w_\xi^m\)。

现在定义真正的 Igusa 主函数
\[
G(b)=\frac{(b-1)^2}{(b-\zeta^p)(b-\zeta^{2p})}.
\tag{1014.9}
\]
分子分母同次，故无穷处值为一，没有遗漏的无穷极部；全部零极都来自所列三个全分歧点。因此
\[
\boxed{\quad
\operatorname{div}_I G
 =m(2s_1-s_\zeta-s_{\zeta^2}).
\quad}
\tag{1014.10}
\]

特别说明容易出错的替代：若写
\[
F(a)=\frac{(a-1)^2}{(a-\zeta)(a-\zeta^2)},
\]
则实际是 \(F(a)=G(b)^p\)，其 divisor 为 (1014.10) 的 **\(p\) 倍**。
不能把原 \(a\)-map 的一般几何点数 \(m\) 当成映射总次数。这里并非从
\(\operatorname{div}F\) 形式地除以 \(p\)，而是已在函数域内构造了真实函数 \(G\)。

## 4. 三个原 CM 尾及全部分量类

R376 §§2–5 已证明三个原 CM 点分别落在不同的 Drinfeld 尾
\(D_\xi\) 上。置
\[
g=(p+1)/12,\qquad
D_\xi:\ y_\xi^2=x_\xi(x_\xi^{2g}+A),\quad A\in k^\times.
\tag{1014.11}
\]
其原点约化和附着点为
\[
Q_\xi=\operatorname{red}(c_\xi)=(0,0),\qquad
\infty_\xi=D_\xi\cap I
\]
（若正则化有有理链，\(\infty_\xi\) 表示朝向该链的同一端点）。
右侧多项式次数 \(2g+1\) 为奇数，故无穷点唯一。仿射部分光滑，连接点在仿射图外。因此
\[
\boxed{\quad
\operatorname{div}_{D_\xi}(x_\xi)=2Q_\xi-2\infty_\xi.
\quad}
\tag{1014.12}
\]
这里的 \(Q_\xi\) 是原 CM 标记确定的点，不是任意 Weierstrass 点。

令 \(a_1=2,\ a_\zeta=a_{\zeta^2}=-1\)。
将 \(D_0\) 的多度沿树转移到中心，实际零多度类的分量是
\[
\begin{cases}
a_\xi[Q_\xi-\infty_\xi],&\text{在 }D_\xi,\\
[2s_1-s_\zeta-s_{\zeta^2}],&\text{在 }I,\\
0,&\text{在其它分量}.
\end{cases}
\tag{1014.13}
\]
可逐边用 vertical twister 核准这个式子。每条有理链的
\(\operatorname{Pic}^0\) 为零，且由 (1014.5) 没有遗漏的图 Jacobian 或 gluing torus，所以 (1014.13) 精确决定整个约化类。

乘以 \(p-1=2m\)，在每个 \(D_\xi\) 使用实际函数
\[
x_\xi^{m a_\xi},
\]
其 divisor 由 (1014.12) 恰为所需 \(2m a_\xi(Q_\xi-\infty_\xi)\)；
在中心 \(I\) 使用 \(G^2\)，由 (1014.10) 也恰为所需 divisor。
其它分量使用一。所有分量类都为零，(1014.5) 遂给出 (1014.2)。

注意只用三个尾上的二挠会漏掉 (1014.13) 的中心项；反之，只主化中心也会漏掉尾。两部分在本证明中同时保留。

## 5. 实际半秩商的形式群入口与仍缺的首提升

好约化的 abelian variety 的商仍有好约化，且原同态延拓到
\(R\) 上的 abelian schemes。对 (1014.2) 应用延拓的 \(q\)，得到 (1014.3)。

特别地，R1011 中的实际非 CM 点 \(\beta\) 满足
\[
(p-1)\beta\in\widehat C_0(\mathfrak m_R),\qquad
\log\beta=(p-1)^{-1}\log\bigl((p-1)\beta\bigr).
\tag{1014.14}
\]
这里 \(p-1\) 是单位，没有人为引入一个除以 \(p\) 的损失。
等价地，因 \(R\) 严格 Henselian 且 \(C[p-1]\) 有限 étale，存在唯一
\[
\tau\in C[p-1](R),\qquad \operatorname{red}(\tau)=\operatorname{red}(\beta);
\]
于是 \(\beta-\tau\) 在实际形式群中。这个 torsion lift 与
(1014.14) 给相同的对数。

本篇仅给特殊纤维上的主化函数。它们并没有被宣称为整个变形族上的全局主函数。要计算首非零 lift，仍需把全部 node gluing、Igusa 与 Drinfeld 分量的内在变形，以及实际 \(q\) 的整投影一起保留。尤其不能沿用错误的 \(a\)-map 后，将 \(F^2\) 的局部导数当成正确的 \(G^2\) 的导数。

即使在完整 Jacobian 的某个分量坐标找到两个不同方向，也不能仅凭 \(\delta\) 等变就断言 R1011 的某个指定半秩商同时保留两列：模 \(p\) 饱和和投影还需证明。实际消去微分的首项单位、统一半径与候选排除均继续 OPEN。\(p\equiv5\pmod{12}\) 的双 vertical 与图同调也不在本结论范围内。

## 6. 依赖与核准

- [R376](R376-actual-cm-drinfeld-point-and-component-contraction.md) §§2–5：原六层稳定子、扭曲在 \(p\) 处平凡、原 \(Q_\xi\) 及尾方程；只消费其仍有效的几何部分，不恢复被 R575 撤回的旧秩零商。
- [R378](R378-actual-cm-disc-parameter-and-uniform-integral-tail.md) (378.18)、§3：原 Hasse 简单零及实际盘尺度；其旧 CM 商的惯性限制没有移用到本篇新商。
- [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md)：实际 \(C,\beta\) 与半秩结论；本篇不改变其非挠范围。
- B. Edixhoven and P. Parent, [Semistable Reduction of Modular Curves Associated with Maximal Subgroups in Prime Level](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf), Documenta Mathematica 26 (2021), 231–269：§2.1 与 Theorem 2.1 保留 exotic 遗忘映射，Theorem 3.3 给任意允许 fine 辅助层模型，Theorem 3.5 的证明给额外自同构商。本篇在原 \(H_6\) 上核出连通性、树与实际三点类，而非直接套粗 \(X_{\rm ns}^+(p)\)。
- 树形 Picard 的乘积分解在 §2 由 normalization/gluing 给出；所用半稳定 Jacobian 的 Picard/Néron 描述为同文 Corollary 3.7 所引用的标准 Raynaud 描述。

global_route 与 root 独立核对实际 Frobenius 函数域、三尾/中心全部类及 \(p-1\) 主化。错误的 degree-\(m\) 原 \(a\)-map 在发布前已发现并以 (1014.7)–(1014.10) 修正。无数学程序执行，无旧窗口重算。
