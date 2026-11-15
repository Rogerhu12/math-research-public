# 原六维 heat 连接的显式可分平凡化与偶部首 p 边界

日期：2026-11-15。状态：**本篇的代数覆盖、原偶部张量同构、全部允许 p 的有限连接零 p 曲率及带源式已证明；critical/primitive 共同非零未证明。**

本篇接续：

- notes/2026-11-15-sigma-modular-heat-connection-and-odd-tame-trivialization.md，简称 MH；
- notes/2026-11-15-sigma-first-p-oscillator-curvature-and-Hasse-source.md，简称 OP。

全部论证为纸面恒等式。没有运行本地数学，也没有增加有限素数窗口。
这里始终区别辅助模参数导数 D 与原截面变量导数 partial_z；
平凡化有限连接，并不删除 oscillator 或首 p 截断的边界源。

## 1. 原连接与矩阵约定

沿原判别式轨道 a^3-27b^2=-432，置
$$
X=a/3,\quad Y=b,\quad Y^2=X^3+16,\quad
DX=2Y,\quad DY=3X^2.
\tag{FT1}
$$
原 CM 点为 P_0=(0,4)。原 sigma 保持 c=0，且
$$
S=\sigma^6,\quad F=x\sigma^6,\quad H=x^2\sigma^6,\quad
R=(x^3+b/2)\sigma^6,\ J=y\sigma^6,\ G=-xy\sigma^6.
$$
记偶函数列 Phi_e=(S,F,H,R)^t、奇函数列 Phi_o=(J,G)^t，
以及
$$
\mathcal O=\frac1{12}\partial_z^2+\frac{3Xz^2}{4}.
$$
MH 的准确方程为
$$
(D-\mathcal O)\Phi_e=M_e\Phi_e,\qquad
(D-\mathcal O)\Phi_o=M_o\Phi_o,
\tag{FT2}
$$
其中
$$
M_e=
\begin{pmatrix}
0&-5/2&0&0\\
-7X/8&0&-1&0\\
Y/4&-5X/4&0&-1/6\\
3X^2/2&-3Y/4&-9X/8&0
\end{pmatrix},
\qquad
M_o=\begin{pmatrix}0&1/2\\5X/8&0\end{pmatrix}.
\tag{FT3}
$$

本文水平值矩阵 U 满足 DU=MU；它平凡化值连接 D-M。
对应的行基作用矩阵为 M^t，水平系数连接是 D+M^t，
其水平矩阵为 U^{-t}。下文不交换这两个约定。

## 2. 第二个二阶连接的平方根覆盖

先在特征零的代数闭常数域上证明本节恒等式。
它们都定义在只需倒置 2、3 的代数模型上，因此随后可在所有 p>3 约化。
取三个互异常数 e_i，使
$$
e_i^3=-16,
$$
并在有限覆盖上取
$$
w_i^2=X-e_i,\qquad w_1w_2w_3=Y.
\tag{FT4}
$$
只需独立加入两个 w_i；第三个由乘积式决定。
令
$$
a_i=\frac{(X+e_i/2)w_i}{e_i^2}.
\tag{FT5}
$$
这些 e_i 都是单位，且三个 e_i 互异。

### 2.1 三个准确的对称平方解

从 (FT1)、(FT4) 直接得到
$$
Dw_i=\frac Y{w_i},\qquad
D^2w_i=(2X+e_i)w_i.
$$
写 A_i=e_i^2a_i=(X+e_i/2)w_i，则
$$
DA_i=3(X-e_i/2)\frac Y{w_i},
$$
$$
D^2A_i=(12X^2+6e_iX+9e_i^2/2)w_i.
\tag{FT6}
$$
再求一次导数：
$$
D^3A_i=
(60X^2-30e_iX-15e_i^2/2)\frac Y{w_i}
=15X\,DA_i+15Y\,A_i.
$$
所以
$$
D^3a_i-15X\,Da_i-15Y\,a_i=0.
\tag{FT7}
$$
这是二阶方程
$$
D^2u=\frac{15}{4}Xu
\tag{FT8}
$$
的对称平方方程；本篇下面直接构造其二解，而不据方程名称推断单值群。

同时
$$
a_i^2=\frac{X^3}{e_i^4}-\frac{3X}{4e_i^2}-\frac1{4e_i}.
$$
对三个三次根求和，三个倒数幂和均为零，故
$$
a_1^2+a_2^2+a_3^2=0.
\tag{FT9}
$$

### 2.2 不变量和二解

定义二次式及其极化式
$$
I(a)=2aD^2a-(Da)^2-15Xa^2,
$$
$$
I(a,b)=aD^2b+bD^2a-(Da)(Db)-15Xab.
\tag{FT10}
$$
(FT7) 与 DX=2Y 表明它们的 D 导数为零；在特征零函数域中，故为常数。
以下评价所得为特征零代数恒等式，再直接约化到 p>3；
并未在特征 p 把所有 D-常数都误认为常数域元素。

这些常数可以在 X=e_i 处准确评价。
在那里 w_i=0，a_i=D^2a_i=0，
$$
(Da_i)^2
=\frac{9(e_i/2)^2}{e_i^4}
 \left.\frac{Y^2}{w_i^2}\right|_{X=e_i}
=\frac{9}{4e_i^2}\,(3e_i^2)=\frac{27}{4}.
$$
对 j 不等于 i，w_j 非零而 Y=0，所以 Da_j=0。
于是
$$
I(a_i)=-27/4,\qquad I(a_i,a_j)=0\quad(i\ne j).
\tag{FT11}
$$
上述评价也可看成有限覆盖正规化上、以 w_i 为参数的评价；
式 (FT6) 保证各项在该点正则，没有把 Y/w_i 当作零。

取常数 iota^2=-1，再加入一个平方根，令
$$
u_1^2=a_1+\iota a_2,\qquad
u_2=\frac{\iota a_3}{u_1}.
\tag{FT12}
$$
由 (FT9)，u_2^2=a_1-\iota a_2。
由 (FT11)，I(a_1+\iota a_2)=I(a_1-\iota a_2)=0。
若 u^2=a 且 I(a)=0，则
$$
\frac{D^2u}{u}
=\frac{2aD^2a-(Da)^2}{4a^2}
=\frac{15}{4}X.
$$
因此 u_1、u_2 均满足 (FT8)。

其 Wronskian
$$
W=u_1Du_2-u_2Du_1
$$
是常数。对两个 (FT8) 的解，直接展开给
I(u_1u_2)=-W^2；而 u_1u_2=iota a_3，故
$$
W^2=-27/4.
\tag{FT13}
$$
尤其这两个解独立，在所有 p>3 都有单位 Wronskian。

令
$$
V=
\begin{pmatrix}
u_1&u_2\\
-Du_1&-Du_2
\end{pmatrix}.
$$
则
$$
DV=
\begin{pmatrix}0&-1\\-15X/4&0\end{pmatrix}V,\qquad
\det V=-W.
\tag{FT14}
$$
这就是本篇需要的第二个二阶值连接。

覆盖的几何次数至多为 8：先取两个独立平方根，再取 (FT12) 的平方根。
它在所有 p>3 都可分。P_0 上 w_i^2=-e_i 为单位，
且 a_i=w_i/(2e_i) 为单位。若 a_1+iota a_2 在 P_0 为零，
则 (FT9) 迫 a_3^2=0，矛盾。因此 u_1、u_2 在 P_0 上也是单位；
这些平方根扩张在 P_0 都不分歧，V 及其逆在那里正则。

## 3. 与原奇连接的张量积准确等于原偶连接

MH 已给出原奇连接的显式覆盖。为固定本篇常数，重列必要部分：
$$
v^6=r(r^4-1),\quad
P=r^8+14r^4+1,\quad
T=r^{12}-33r^8-33r^4+1,
$$
$$
\alpha^3=\beta^2=-4/27,\quad
X=\alpha P/v^8,\quad Y=\beta T/v^{12},\quad
c=\frac{3\beta}{2\alpha},\quad c^2=\frac{9\alpha}{4},
$$
$$
D=cv^2\partial_r.
\tag{FT15}
$$
MH 的多项式恒等式逐项证明这些式子给出 (FT1) 的有限可分覆盖。
令
$$
q_1=v^{-1},\qquad q_2=rv^{-1},\qquad
U_o=\begin{pmatrix}q_1&q_2\\2Dq_1&2Dq_2\end{pmatrix}.
$$
则
$$
D^2q_j=\frac5{16}Xq_j,\quad
DU_o=M_oU_o,\quad \det U_o=2c.
\tag{FT16}
$$
p>3 时常数 c 为单位。P_0 上 P(r)=0，且
P'(r)=8r^3(r^4+7)；共同零只能给 48=0，故不存在。
同时 r、v 非零。于是该覆盖在 P_0 不分歧，
U_o、U_o^{-1} 都在那里正则。

任取 (FT16) 的解 q 与 (FT8) 的解 u，记
$$
b=2Dq,\qquad d=-Du,\qquad
z_1=qu,\ z_2=qd,\ z_3=bu,\ z_4=bd.
$$
为免与原 Taylor 变量 z 混淆，以下 z_i 只表示这四个张量坐标。
由两个二阶系统准确得到
$$
\begin{aligned}
Dz_1&=-z_2+z_3/2,\\
Dz_2&=-15Xz_1/4+z_4/2,\\
Dz_3&=5Xz_1/8-z_4,\\
Dz_4&=5Xz_2/8-15Xz_3/4.
\end{aligned}
\tag{FT17}
$$

现在定义四个张量组合
$$
\begin{aligned}
\mathsf S&=z_2+3z_3,\\
\mathsf F&=3Xz_1/4+z_4,\\
\mathsf H&=-3Yz_1/2-3Xz_2/4+3Xz_3/4,\\
\mathsf R&=27X^2z_1/16+3Yz_2/2-3Xz_4/4.
\end{aligned}
\tag{FT18}
$$
这些是水平值向量的坐标，不是把原 sigma 截面本身与代数函数相等。

直接由 (FT17) 求导，第一、二行给
$
D\mathsf S=-5\mathsf F/2,\qquad
D\mathsf F=-\mathsf H-7X\mathsf S/8.
$
第三行的中间展开是
$$
D\mathsf H=-39X^2z_1/32+3Yz_3/4-9Xz_4/8,
$$
恰等于 $-\mathsf R/6+Y\mathsf S/4-5X\mathsf F/4$。
最后一行的完整展开为
$$
D\mathsf R=
9XYz_1/8+75X^2z_2/32+117X^2z_3/32-3Yz_4/4
$$
$$
=\frac{3X^2}{2}\mathsf S-\frac{3Y}{4}\mathsf F
-\frac{9X}{8}\mathsf H.
\tag{FT19}
$$
所以四行正是 (FT3) 的 M_e，没有残差或缺少的最后一行。

(FT18) 的转换矩阵是
$$
K=
\begin{pmatrix}
0&1&3&0\\
3X/4&0&0&1\\
-3Y/2&-3X/4&3X/4&0\\
27X^2/16&3Y/2&0&-3X/4
\end{pmatrix}.
$$
向最后一行加 3X/4 倍第二行，再沿第四列展开，得到
$$
\det K=\frac{27}{4}(X^3-Y^2)=-108.
\tag{FT20}
$$
这在所有 p>3 都是单位。因此这里是原四维连接的实际同构，
并非仅比较标量方程的局部指数，也非把偶部直接认作奇部的三次对称幂。

在两个覆盖的复合上，定义
$$
U_e=K(U_o\otimes V),
\tag{FT21}
$$
张量行次序采用 (z_1,z_2,z_3,z_4)。
由 (FT17)--(FT19)，DU_e=M_eU_e。
并且
$$
\det(U_o\otimes V)=(2c)^2W^2=-27c^2,\qquad
\det U_e=2916c^2.
\tag{FT22}
$$
这给出在所有允许 p 都为单位的原偶部完整水平矩阵。
在 P_0 的任一所选覆盖点，U_e 与 U_e^{-1} 均正则。

## 4. 所有允许 p 的有限连接零 p 曲率

设 p>=41 且 p=6N+5。
(FT1) 上的 D 是非零全局平移不变向量场。
D^p 仍是全局向量场，故 D^p=gamma D，其中 gamma 是常数。
取三次单位根 zeta。自同构
g:(X,Y) mapsto (zeta X,Y) 在函数拉回约定中满足
(g^*)D(g^*)^{-1}=zeta^{-1}D；
故对 D^p 的乘子一方面为 zeta^{-1}，另一方面为 zeta^{-p}。
因 p=2 mod 3，二者不同，迫 gamma=0，即
$$
D^p=0.
\tag{FT23}
$$
这是辅助曲线自身的导数事实，不是关于原全 sigma Taylor 级数的约化断言。

所有 (FT4)、(FT12)、(FT15) 的覆盖在 p>3 可分。
D 唯一延伸到有限可分函数域；D^p 也是导数且在基域为零，
所以由可分性它在整个复合函数域仍为零。

由 DU_e=M_eU_e 和 DU_o=M_oU_o，
$$
(D-M_e)^p=0,\qquad(D-M_o)^p=0.
\tag{FT24}
$$
这里没有未明确的有限坏素数集合：分母、覆盖分歧常数与所有行列式
只需排除 2、3。故 (FT24) 对本课题所有允许 p 都成立。
全六维值连接由 diag(U_e,U_o) 平凡化；
全六维水平系数连接则由 diag(U_e^{-t},U_o^{-t}) 平凡化。

需要强调，(FT24) 没有把 (FT2) 的 oscillator 删除。
原六截面仍满足带有 partial_z^2 与 Xz^2 的方程；
固定原曲线的六维 D_z 闭合依然不成立。

## 5. 原偶部首 p 边界不是零

以下在原 Hurwitz 整模型模 p 中使用普通导数系数，
并只截取 n<p，因此 n! 均可除。
写 c_n(U)=partial_z^n U(0)。

令
$$
A=\mathscr A_p(3X,Y),\qquad
\mathscr A_p(a,b)=[t^{p-1}]
(t^3-at/4-b/4)^{(p-1)/2}.
\tag{FT25}
$$
MH 已在原 c=0 规范证明
$$
c_p(\sigma)=A,\quad A(P_0)=0,\quad (DA)(P_0)=B\ne0,
\tag{FT26}
$$
且 OP 证明 D^2A=-XA/4。
由原 sigma heat 方程，在模 p 普通导数系数上有
c_{p+2}(sigma)=2DA；其中 az^2 sigma 项的系数含 p(p-1)，为零。

为完整核对偶部的边界，置
$$
q_\sigma=(\sigma')^2-\sigma\sigma''=x\sigma^2.
$$
则
$$
S=\sigma^6,\quad F=\sigma^4q_\sigma,\quad
H=\sigma^2q_\sigma^2,\quad
R=q_\sigma^3+(b/2)\sigma^6.
\tag{FT27}
$$
在 Hurwitz 普通导数系数模 p 中，
partial_z^p 的 Leibniz 公式仅保留两端，因而是导数。
原 c=0 初值为 sigma(0)=0、sigma'(0)=1、
sigma''(0)=sigma'''(0)=0，且 q_sigma(0)=1。
从 (FT27) 逐项得到
$$
c_p(S,F,H,R)=(0,0,0,0),
$$
$$
c_{p+1}(S,F,H,R)=(0,0,2A,6DA).
\tag{FT28}
$$
例如 partial_z^p H=2sigma(partial_z^p sigma)q_sigma^2
+2sigma^2q_sigma(partial_z^p q_sigma)，再求一次导数并在 0 评价只剩 2A。
而 c_{p+1}(q_sigma)=c_{p+2}(sigma)=2DA，
所以 R 的该系数为 3(2DA)。没有把跨 p 的普通 Taylor 分母直接约化。

对
$$
\Phi_{e,<p}=\sum_{0\le n<p}
c_n(\Phi_e)\frac{z^n}{n!}
$$
在 k(E)[z]/(z^p) 中有
$$
(D-\mathcal O-M_e)\Phi_{e,<p}
=-z^{p-1}\left(\frac A6e_H+\frac{DA}{2}e_R\right).
\tag{FT29}
$$
这里 e_H=(0,0,1,0)^t、e_R=(0,0,0,1)^t。
准确负号来自 (p-1)!=-1；二阶 z 导数遗漏的原 c_{p+1}
必须先写成 c_{p+1}/(p-1)! 再模 p。

在 P_0，(FT29) 的右侧为
$$
-\frac B2z^{p-1}e_R\ne0.
\tag{FT30}
$$
因此即使已完整平凡化偶部有限连接，
也不能把原首 p 多项式向量当作齐次 oscillator 的水平解。

令
$$
\Psi_{e,<p}=U_e^{-1}\Phi_{e,<p},\quad
V_H=U_e^{-1}e_H,\quad V_R=U_e^{-1}e_R,\quad
\nabla=D-\mathcal O.
$$
则
$$
\nabla\Psi_{e,<p}
=-z^{p-1}\left(\frac A6V_H+\frac{DA}{2}V_R\right).
\tag{FT31}
$$
V_R(P_0) 是非零向量，因为 U_e(P_0) 可逆；
本篇不声称它每一分量或任何指定 critical 系数都为单位。

## 6. 原完整连接的 p 曲率与保留源项的方程

OP 在同一空间 k(E)[z]/(z^p) 中证明
$$
\nabla^p=\frac1{12}\bigl(A\partial_z+6(DA)z\bigr)^2.
\tag{FT32}
$$
它依赖实际的全局 Cartier 等式
C(A^{-2}dX/(2Y))=dX/(2Y)，不只是形式 Gaussian 共轭。
在 P_0，右侧为 3B^2z^2。

由于 U_e、U_o 不依赖 z，它们与 (FT32) 的右侧交换。
因此 (FT24) 现在给出原值基中的完整算子等式
$$
\boxed{
(D-\mathcal O-M_e)^p
=(D-\mathcal O-M_o)^p
=\frac1{12}\bigl(A\partial_z+6(DA)z\bigr)^2 I,
}
\tag{FT33}
$$
两个等号各在相应的 4 维、2 维空间中理解。
有限矩阵部分零 p 曲率，而完整 heat 连接的 p 曲率通常非零；
二者不能互相替代。

对 (FT31) 再施行 nabla^{p-1}，得到
$$
\boxed{
\bigl(A\partial_z+6(DA)z\bigr)^2\Psi_{e,<p}
=-2\nabla^{p-1}
 \left[z^{p-1}\bigl(A V_H+3(DA)V_R\bigr)\right].
}
\tag{FT34}
$$
特别在原 CM 点：
$$
\boxed{
36B^2z^2\Psi_{e,<p}(P_0)
=-2\left.
 \nabla^{p-1}\left[
 z^{p-1}\bigl(A V_H+3(DA)V_R\bigr)\right]
 \right|_{P_0}
\quad\bmod z^p.
}
\tag{FT35}
$$
所有 D 导数必须在代入 P_0 前完成。

奇部仍是 MH、OP 已证明的原式：
$$
\nabla\Psi_{o,<p}=\frac A{12}z^{p-2}V_o,\qquad
V_o=U_o^{-1}(0,1)^t,
$$
$$
36B^2z^2\Psi_{o,<p}(P_0)
=\left.\nabla^{p-1}(Az^{p-2}V_o)\right|_{P_0}.
\tag{FT36}
$$
现在 F 与 G 均已在同一明确可分覆盖上运输，
而且各自的原截断源项完整保留。
若不想改变值基，也可直接用 (FT33) 对 (FT29)
及其奇部对应式作用；这与 (FT34)--(FT36) 等价。

## 7. 结论的实际范围

本篇补齐了一个此前没有的原结构：
偶部 M_e 通过行列式 -108 的明确矩阵，与
Lamé 5X/16 和 Lamé 15X/4 的二阶值连接张量积同构。
两个二阶连接均给出具体有限可分水平基，
从而原六维有限 heat 连接对全部允许 p 都有零 p 曲率。
原偶部首 p 边界及完整 heat p 曲率也已准确接上。

但有限覆盖的单位行列式只保持整个向量的非零。
它不保持某个指定 Taylor 系数、固定稀疏标签集，
也不禁止经过 U_e(P_0)、U_o(P_0) 的线性组合相消。
(FT34)--(FT36) 右侧还含整个辅助方向的导数，
尚未变成只由
$$
f_i g_{N-1-i}\qquad(0\le i<N,\ p=6N+5)
$$
组成的确定单位配对。

所以未筛 critical 全零仍未排除。
更严格的原目标仍须在同一个标签满足
$$
(6i+7,p+1)=1,\qquad
P_{6i+6}(1/\sqrt{-3})\,f_i g_{N-1-i}\ne0.
$$
本篇没有从不同标签拼接单位，也未删除 Legendre 权或 primitive 筛。
接下来的有效推进必须分析 (FT34)--(FT36) 的原支撑，
或构造能严格保留该筛选的算术配对；
单凭有限单值、可分覆盖或单位行列式，不能声称得到这一结论。

