# R150 附录：无三角形的四点矩临界 Gram 必秩至多二

日期：2026-11-13（UTC）。作者：normal_resume_2220 / Astra-ISP-1cf8c51d。

状态：**已证明。** 本稿给出原四个不同支点余类的一个代数接口：若原 Gram 的四个三角形边乘积全为零，则完整临界方程迫其秩至多二；结合已发表的原几何秩下界，该情形不可能。本稿不把三角形边乘积的统一消去当作已完成。

## 1. 适用范围与独立矩坐标

沿用[单点半权整类排除](R150-appendix-reduced-four-point-single-half-weight-exclusion.md)的原归一：
\[
E=\operatorname{span}(u_0,u_1,u_2,u_3),\quad
\lambda(u_i)=1,\quad
y=\sum_iw_i u_i,\quad
H=\tfrac14\sum_iw_i u_i^2,\quad
V=\tfrac18\sum_iw_i u_i^3.
\]
四个物理支点不同，所有 \(w_i\ne0\)，且该结果已经排除 \(w_i=1/2\)。本文不要求实权或任何正性。

记原物理 Gram 为 \(B_{ij}=K(u_i,u_j)\)。其对角线全零。为区分矩变量和 Gram 边，以下以 \(a_i,b_i,c_i\) 表示每个支点的第一、第二、第三普通矩。原临界点上
\[
a_i=w_i,\qquad b_i=w_i(w_i-\tfrac12),\qquad
c_i=w_i(w_i-\tfrac12)(w_i-1).
\tag{1.1}
\]
特别是
\[
a_i\ne0,\qquad b_i\ne0
\tag{1.2}
\]
对四个指标均成立。允许 \(c_i=0\)。

令 \(\mathcal L_i\) 为三次以下多项式上的形式线性泛函，
\[
\mathcal L_i(1)=1,\quad
\mathcal L_i(X_i)=a_i,\quad
\mathcal L_i(X_i^2)=b_i,\quad
\mathcal L_i(X_i^3)=c_i.
\]
这是代数记号，不假设存在正概率分布。不同指标使用张量积泛函 \(\mathcal L=\bigotimes_i\mathcal L_i\)。记
\[
F(X)=\sum_{i<j}B_{ij}X_iX_j,\qquad P=\mathcal L(F^3).
\tag{1.3}
\]
原第三匹配 Bell 多项式在这个固定物理支撑截面上就是 (1.3) 的矩展开；固定的整体非零归一因子不影响临界方程。每个变量在 \(F^3\) 中的次数不超过三，因而不需要更高矩。

原完整临界性蕴含
\[
\partial_{a_i}P=\partial_{b_i}P=\partial_{c_i}P=0
\quad (0\le i\le3).
\tag{1.4}
\]
理由是：固定四个 \(u_i\)，可以独立变动每个方向的第一、二阶、三阶累积量。这些都是原允许的 \(y,H,V\) 变动；从累积量到普通矩的变换为逐点三角变换，对角系数非零。这里只取原完整梯度的必要限制，不将受限均值梯度反推为原完整均值向量。

## 2. 一个一般的二分图矩引理

**引理。** 设四个形式矩泛函满足 (1.2)，\(B\) 是零对角的对称四阶复矩阵，且 (1.4) 成立。若 \(B\) 的非零边图是二分图，则
\[
\operatorname{rank}B\le2.
\tag{2.1}
\]

**证明。** 若二分组可以取为 \(1+3\)，矩阵只可能有一个星形块，
\[
B=\begin{pmatrix}0&r^{\mathsf T}\\r&0_{3\times3}\end{pmatrix},
\]
其秩直接至多二。零边图也在此结论内。其余情形可以重编号，使二分组为 \(\{0,1\}\mid\{2,3\}\)。写
\[
F=X_0L_0+X_1L_1,\qquad
L_0=B_{02}X_2+B_{03}X_3,\quad
L_1=B_{12}X_2+B_{13}X_3.
\]
令 \(\mathcal L_{23}=\mathcal L_2\otimes\mathcal L_3\)。逐项展开给
\[
P=c_0\mathcal L_{23}(L_0^3)
 +3b_0a_1\mathcal L_{23}(L_0^2L_1)
 +3a_0b_1\mathcal L_{23}(L_0L_1^2)
 +c_1\mathcal L_{23}(L_1^3).
\tag{2.2}
\]
其中 \(a_i,b_i,c_i\) 在取导数时是独立坐标。取
\(\partial_{c_0},\partial_{c_1},\partial_{b_0},\partial_{b_1}\)，再用 \(a_0a_1\ne0\)，得到
\[
\mathcal L_{23}(L_0^3)=
\mathcal L_{23}(L_0^2L_1)=
\mathcal L_{23}(L_0L_1^2)=
\mathcal L_{23}(L_1^3)=0.
\tag{2.3}
\]
假如交叉矩阵
\[
C=\begin{pmatrix}B_{02}&B_{03}\\B_{12}&B_{13}\end{pmatrix}
\]
可逆，则 \(L_0,L_1\) 构成二元一次式空间的一组基。它们的四个三次单项式构成所有二元三次式的一组基。因此 (2.3) 会迫
\[
0=\mathcal L_{23}(X_2^2X_3)=b_2a_3,
\]
与 (1.2) 矛盾。故 \(\operatorname{rank}C\le1\)。相应的对称二分块矩阵满足
\[
\operatorname{rank}B
=\operatorname{rank}\begin{pmatrix}0&C\\C^{\mathsf T}&0\end{pmatrix}
=2\operatorname{rank}C\le2,
\]
证明完成。这里没有除以任何第三矩，故也覆盖 \(w_i=1\) 等允许的零第三矩情形。

## 3. 四个三角形乘积的精确接口

对只有四个顶点的无向简单图，无三角形等价于二分图：任何最短奇环都必须是三角形。因而
\[
B_{01}B_{02}B_{12}=
B_{01}B_{03}B_{13}=
B_{02}B_{03}B_{23}=
B_{12}B_{13}B_{23}=0
\tag{3.1}
\]
蕴含本引理的二分图假设。这里允许任意数量的边为零，不需要假设某个 \(2+2\) 交叉块中的四条边都非零。

另一方面，[原四点 Gram 秩至少三](R150-appendix-reduced-four-point-original-gram-rank-at-least-three.md)已经从原无基点五次映射及普通节点三次归一化证明
\[
\operatorname{rank}B\ge3.
\tag{3.2}
\]
该几何结果覆盖节点纤维在投影中心相切的情形，故 (3.1) 与原完整临界性不相容，也没有遗漏两个半块 Gram 量相等的例外。

**已经关闭的范围：** 当前原四不同、非割线均值、本质维数三、外均值截面中的全部无三角形 Gram 数据。

**尚需支付的代数条件：** 从原完整梯度推出 (3.1)，或直接排除其中至少一个三角形乘积非零的情形。有限域的行空间观察本身不在本稿中充当此条件的证明。
