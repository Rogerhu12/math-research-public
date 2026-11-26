# R150 附录：非退化二重加单点 H 的非零 Hp 层两个 V 值在重节点必非零且不同

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明的必要归约。** 在原完整临界点的 rankH3、H 为 $2+1$、rankV2、本质六维反设中，若 $Hp\ne0$，则下述完整规范中的两个重节点配对 $C_0,D_0$ 满足 $C_0D_0(C_0-D_0)\ne0$。其零值及相等边界全部由原 H 与最高梯度的一次系数排除；并给出剩余两个 V 行的一次坐标的唯一仿射公式。没有新增计算门，也不声明整个非零 Hp 层为空。

## 1. 原规范与完整 Gaussian 约束

[退化 Gram 全排除](R150-appendix-rank-three-double-plus-single-second-cumulant-degenerate-gram-essential-six-exclusion.md)及[非约化 V 全排除](R150-appendix-rank-three-double-plus-single-second-cumulant-nonreduced-third-cumulant-essential-six-exclusion.md)已使本质六维反设只余 $F\ne0$、非退化 H Gram、约化 V 及 $e\ne0$。用前稿显示的可逆加权、局部参数及非零平凡化尺度，取
$$
F=h=g=1,\qquad H=z_0z_1+z_1z_0+\frac12w^2,
$$
$$
K_R=
\begin{pmatrix}0&0&1\\0&b&c\\1&c&0\end{pmatrix},
\quad b\ne0,\qquad
V=\frac12(u^3+v^3),\quad e=uKv\ne0,\quad p(u)=p(v)=e.
\tag{1.1}
$$
六列 $(y,z_0,z_1,w,u,v)$ 始终为原整个六空间的一组基；$z_0,z_1$ 为同一实际物理源的值和一阶 Taylor 列，w 为不同物理值。

设 $p_i=p(z_i)$、$r=p(w)$。本稿假设 $Hp\ne0$。完整 Gaussian 向量式 $(2HK-I)Hp=0$ 给
$$
p_0=r,\quad p_1=(2b+c)r,\quad b+c=\frac14.
$$
若 r 为零，则三个均值都为零，反而 $Hp=0$，所以 $r\ne0$。完整 Gaussian 标量式与原最高/Euler 式分别给
$$
(3-4c)r^2=1+4c,\qquad
4e^3=1+12c-12b.
$$
置 $\chi=e^3$，得到全部准确公式
$$
\boxed{
b=\frac{1-\chi}{6},\qquad
c=\frac{2\chi+1}{12},\qquad
r^2=\frac{\chi+2}{4-\chi},\qquad
p_1=\frac{5-2\chi}{12}r.
}
\tag{1.2}
$$
各除法边界已由原式排除：
$$
\boxed{\chi\notin\{0,1,-2,4\}.}
\tag{1.3}
$$
其中 $\chi=0$ 与 $e\ne0$ 矛盾，$\chi=1$ 与 $b\ne0$ 矛盾，$\chi=-2$ 将迫 $r=0$，而 $\chi=4$ 使原 Gaussian 标量式成为 $0=6$。本稿保留 r 的两个平方根符号。

## 2. 重节点的四个完整矩

令
$$
C_i=K(z_i,u),\qquad D_i=K(z_i,v).
$$
定义
$$
A=C_0^2+D_0^2,\quad B=C_0^3+D_0^3,\quad
M=C_0C_1+D_0D_1,\quad
T=C_0^2C_1+D_0^2D_1.
$$
完整原 H 张量仍是
$$
N=yy^{\mathsf T}-2H
-2\bigl(y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\bigr)
+4HKH+2e(u^2+v^2),
\qquad k_x^{\mathsf T}Nk_x=0.
$$
完整最高式仍是
$$
p(x)^3-6p(x)H(k_x,k_x)
+2\bigl(K(x,u)^3+K(x,v)^3\bigr)=0.
$$
在 H 的实际重节点取常数、一次 Taylor 系数，准确有
$$
2eA=p_0^2+1,\qquad
2B=3p_0-p_0^3,
$$
$$
2eM=p_0p_1+c-2b,\qquad
2T=(1-p_0^2)p_1+2p_0c.
\tag{2.1}
$$
第三式的 $-2b$ 来自完整 $4HKH$，不能删除；最后两式只除去了实际一次 Taylor 系数的共同非零常数，不把 N 作为零矩阵。

将 (1.2) 代入并约分，得到
$$
\boxed{
A=\frac{3}{e(4-\chi)},\quad
B=\frac{r(5-2\chi)}{4-\chi},
}
$$
$$
\boxed{
M=\frac{-4\chi^2+14\chi-1}{12e(4-\chi)},\quad
T=\frac{3r}{4(4-\chi)}.
}
\tag{2.2}
$$
特别 $A\ne0$、$T\ne0$。所有 V 项、符号和原重节点权均保留在这些式子中。

## 3. 所有零值及相等边界给同一个矛盾

假设 $C_0D_0(C_0-D_0)=0$。因为 $A\ne0$，可能的情形恰是：一个值为零、另一个非零；或者两个值相等且非零。

在每种情形中，存在同一个非零的活跃值 $\rho$，使
$$
\rho=\frac BA,\qquad T=\rho M.
\tag{3.1}
$$
例如 $D_0=0$ 时取 $\rho=C_0$；两个值相等时也取其共同值。这个论证不除以 M，因此保留了可能的 $M=0$ 边界。

由 (2.2)，
$$
\rho=\frac{er(5-2\chi)}3.
$$
将其代入 (3.1)，再只除以已经非零的 $r,e,4-\chi$，得到
$$
(5-2\chi)(-4\chi^2+14\chi-1)=27.
$$
然而准确多项式身份为
$$
(5-2\chi)(-4\chi^2+14\chi-1)-27
=8(\chi-1)^2(\chi-4).
$$
因此 $\chi=1$ 或 $\chi=4$，均违反 (1.3)。故
$$
\boxed{C_0D_0(C_0-D_0)\ne0.}
\tag{3.2}
$$
特别两个 V 值都不与 H 重节点正交，并且在 (1.1) 的完整保 V 规范下二者配对不相等。该论证对所有有限、无穷远 V 点成立，因为未使用其仿射坐标。

## 4. 剩余两行的唯一仿射坐标

为了明确下一步的低度输入，作非零尺度
$$
a_1=C_0/(er),\quad a_2=D_0/(er),\qquad
b_1=C_1/(er),\quad b_2=D_1/(er).
$$
令
$$
d=\chi(\chi+2),\quad k=5-2\chi,\quad
n=-4\chi^2+14\chi-1,\quad \sigma=a_1+a_2.
$$
(2.2) 等价于
$$
a_1^2+a_2^2=3/d,\qquad a_1^3+a_2^3=k/d,
$$
$$
a_1b_1+a_2b_2=n/(12d),\qquad
a_1^2b_1+a_2^2b_2=3/(4d).
\tag{4.1}
$$
因此
$$
\boxed{d\sigma^3-9\sigma+2k=0.}
\tag{4.2}
$$
定义
$$
J=9-dk\sigma.
$$
由 (4.1)，有原精确身份
$$
J=-d^2a_1a_2(a_1-a_2)^2\ne0.
\tag{4.3}
$$
故两个一次坐标唯一写成
$$
\boxed{b_i=\alpha a_i+\beta\quad(i=1,2),}
$$
其中
$$
\boxed{
\alpha=\frac{n-3d\sigma}{4J},\qquad
\beta=\frac{2(\chi-1)^2(4-\chi)}{3J}\ne0.
}
\tag{4.4}
$$
这只是 (4.1) 中一个非奇异二乘二线性系统的准确解，没有新增支撑假设。它为非零 Hp 的继续消元支付了全部零行、相等行以及 J 分母边界。

本稿没有处理其余完整 H/最高系数与原物理实现，也不关闭本质四五维或 ISP 完成标准。


后续完整非零Hp排除已完成，见[整层证明](R150-appendix-rank-three-double-plus-single-second-cumulant-nonzero-hp-essential-six-exclusion.md)。
