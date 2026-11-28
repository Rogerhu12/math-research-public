# R1207：原 CM 截面在非约化常数尾上的准确位置

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；root / global_route。

**已证明。** 对原 $a=1$ 的标准 $\mathbf Z[\zeta_3]$ 非分裂 Cartan CM 点 $c_1$，R1021 的实际模 $p$ 常数仿射尾坐标将整个 CM 截面送到 $V=0$。这是底环 $\mathcal O/(p)$ 上的恒等式，包含全部 nilpotents，不只是在特殊纤维上的 $\overline{c_1}=Q$。原六标记必须与 CM 自同构一起运输；该运输在原 $H_6$ 商中识别，不假定 framing 单独固定全六标记对象。

本篇只补原支持尾的实际截面位置。它不恢复 R575 已撤回的 CM 秩零商，不从截面位置推出完整 Čech 对数或支持尾配对为零。

## 1. 原模问题与唯一使用的既成几何

保持 $p=12g-1>37$、原 $X_1$ 及三个 $a^3=1$ CM 点。R376 §1 定义 $c_1$ 为 $j=0,a=1$、带标准 $\mathbf Z[\zeta_3]$ 非分裂 Cartan 结构的实际点。该几何定义不依赖该文后来撤回的 CM 秩断言。

在原 full-six/full-$p$ 覆盖上取该点的一个实际提升。将同一 CM 椭圆曲线在 $p$ 处的好模型、六标记和 $p$-level 基一起提升；必要的根和标记可在 R1021 的原 tame 底及未分歧系数扩张上取得。固定一个原 Weil 分支。写
$$
e=p^2-1,\qquad \varpi^e=p,\qquad
x=\varpi\alpha,\quad y=\varpi\beta.
$$
R1021 的 $x,y$ 来自真实 level 点的同一 tame 平均形式参数，且
$$
g_\xi(x)=\xi x,\qquad g_\xi(y)=\xi y
\quad(\xi\in\mu_e).
\tag{1207.1}
$$
framing 作用固定系数环；此处也固定 radial chart 的基参数 $\varpi$，并非另作惯性下降。

R1021 (1021.5) 在整个非约化基上给
$$
\mathscr R/(p)=
(\mathcal O/(p))\otimes_k
k[\alpha,\beta]/(\alpha^p\beta-\alpha\beta^p-c_0),
\qquad c_0\in k^\times.
\tag{1207.2}
$$
在这个同一模型中，全部 $p$-level 换基模 $p$ 准确是原 $\mathbf F_p$ 矩阵的线性作用。两件事都已在实际变形环中证明，不能只以特殊纤维坐标代替。

## 2. 同一 CM 自同构、六标记与 p-level 矩阵

令 $\zeta$ 是原 CM 自同构在形式参数切线上的一个本原三次单位根。它是 $\mu_e$ 中的同一个元素，并延伸为该整 CM 椭圆曲线的实际自同构。

该自同构作用于原 $E[p]$ 基的矩阵记为 $I$。由于 $c_1$ 带的正是标准 CM 非分裂 Cartan 结构，
$$
I\in C_{\mathrm{ns}}\subset N_{\mathrm{ns}},
\qquad I^3=1,\qquad I\ne1.
\tag{1207.3}
$$
其两个特征值是 $\zeta,\zeta^p=\zeta^{-1}$；二者之差是单位。

还须处理原六标记。R376 §2 的实际支满足
$$
\left.\frac{d}{da}\bigl(6912a^3(1-a^3)\bigr)\right|_{a=1}
=-20736\in\mathbf Z_p^\times.
$$
因此该六层支保留整个有效 $\mu_3$ 稳定子。具体地，将所选全六标记随上述 CM 自同构运输，得到的标记由原图子群 $H_6$ 的同一轨识别。这个事实在整 CM 提升上成立：prime-to-$p$ 标记有限 étale，CM 自同构已整延伸；其离散换标矩阵与特殊纤维的是同一个。

所以固定实际 CM 截面的，是**六标记运输、p-level 矩阵和 framing 改变的组合**。用 R1021 的右作用 convention，CM 自同构将改变后的 framing 与原 framing 识别，而同构对 $p$ 基的作用正是 $I$ 或 $I^{-1}$。在两者中统一选择与 (1207.1) 的 $g_\zeta$ 相应者，记为 $I_0$，便有在 CM 截面上
$$
\bigl(I_0-\zeta\operatorname{id}\bigr)
\binom{\alpha}{\beta}=0
\quad\text{于 }\mathcal O/(p).
\tag{1207.4}
$$
这里只用真实模对象的自同构与 R1021 的两种准确作用。逆 convention 只交换两个共轭特征线，不影响下述结论。没有把固定全六标记的一次 framing 作用单独当成 CM 截面的稳定子。

## 3. 精确锁定全部 nilpotent 方向

在 $k$ 上对角化原同一个 $C_{\mathrm{ns}}$。沿 R1197 的坐标写
$$
A_0^{p+1}-B_0^{p+1}=c,\qquad c\in k^\times,
$$
$$
V=A_0B_0,\qquad
U=\frac{A_0^{p+1}+B_0^{p+1}}2,
\qquad U^2=V^{p+1}+c^2/4.
\tag{1207.5}
$$
因为 $I_0$ 的两个特征值不同且差为单位，(1207.4) 准确迫使其中一个 Cartan eigen coordinate 为零：
$$
A_0=0\quad\text{或}\quad B_0=0
\quad\text{于 }\mathcal O/(p).
$$
另一个由 (1207.5) 必为单位。不是仅有零坐标的某个 $p$ 次幂为零；对应线性算子的非零特征值可逆，故坐标本身为零，包括全部 nilpotents。

于是
$$
\boxed{\quad
V(c_1)=0,\qquad U(c_1)=\pm c/2
\quad\text{于 }\mathcal O/(p).
\quad}
\tag{1207.6}
$$
两个符号只记录原两个 Cartan eigenline 的选择，并不改变原正规化子商点。

现在经过同一个原 Cartan、正规化子和辅助 $\mu_3$ 商。R1197 的真实坐标为
$$
x_D=V^6,\qquad y_D=UV^3,
\qquad y_D^2=x_D(x_D^{2g}+A_{\rm tail}),
\quad A_{\rm tail}=c^2/4.
$$
因此
$$
\boxed{\quad
(x_D(c_1),y_D(c_1))=(0,0)
\quad\text{在整个非约化模 }p\text{ 尾上}.
\quad}
\tag{1207.7}
$$
$A_{\rm tail}$ 为单位，所以该点是光滑的，实际局部参数可取 $t=V^3$，并且 $t(c_1)=0$。原 deck 运输将相同证明送到另外两个 $a^3=1$ 支，仍须随同原六标记一起运输。

## 4. 对原 CM primitive 的直接后果与尚待的 gluing

R1197 的实际参考函数
$$
H_k=a_{3k-3}^{-1}\Theta^{3k-3}(UV^{m-2}),
\qquad 1\le k\le n=2g-1,
$$
在 $Q$ 的展开从非零的 $t^{2g-k}$ 项开始。因此 (1207.7) 准确给
$$
H_k(c_1)=0\quad\text{于 }\mathcal O/(p)
\tag{1207.8}
$$
对同一个模 $p$ 常数函数成立；另外两个支持支亦然。这里不只代入特殊点，而是代入实际截面在非约化模型中的全部坐标。

这项消失不能独自宣称对应的支持尾对原 $\mathcal V_m$ 没有贡献。原水平 divisor、vertical twister、ordinary 中心的 $G(b_{\rm lift})^2$、节点单位及有限 log 必须仍在同一 Čech 复形中比较。特别，R1206 的 SS 原函数含实际 $W^{-p}$ 项；(1207.8) 不删除这些项，也不替代从 regularized primitive 到完整图配对的证明。

## 来源与核验

- [R376](R376-actual-cm-drinfeld-point-and-component-contraction.md) §§1–5：原 CM 标记、六层有效 $\mu_3$、Cartan 坐标及仍有效的实际局部几何。仅使用其现行更正明确保留的部分，不使用撤回的全局 CM 秩零结论。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md) §§1–3：实际 tame eigenparameters、非约化模 $p$ 常数模型及全部 level 换基的精确线性作用。
- [R1197](R1197-original-highest-packet-complete-CM-coefficient-flag.md) §§1、3：同一原支持尾、$H_k$ 及其在 $Q$ 的完整首项。
- R1018、R1196、R1199、R1206：原 twister、有限 log、全图配对与必须保留的边界。

root 与 global_route 分别核准 CM 自同构及六标记运输，再按 R1021 逐项证明全模 $p$ 锁点。全部为纸面推导，未执行数学程序，未重开旧有限窗口。主目标仍开放，继续实际支持尾与全图收缩。
