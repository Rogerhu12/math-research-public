# 原 critical 权不能作为平行对角算子运输

日期：2026-11-15。状态：**本篇的双变量 p 曲率、核的一维性及原权的平行运输障碍已证明；共同非零没有证明。**

本篇只排除一种具体捷径：在双变量原 heat 连接上，寻找一个水平端同态，
使它在原 F/G critical 稀疏空间上的作用恰为逐标签 primitive × Legendre 权，
且不漏出到其他单项式或有限通道。一般非水平算子、带交换子的式子，
以及真正 Cartan 作用的非对角矩阵系数，并未被本篇排除。

依赖：
- notes/2026-11-15-sigma-full-heat-tame-trivialization-and-even-source.md，简称 FT；
- notes/2026-11-15-sigma-first-p-oscillator-curvature-and-Hasse-source.md，简称 OP；
- R770、R734。

## 1. 双变量原连接及其曲率

沿 FT 的辅助曲线 Y^2=X^3+16，保留 D、P_0=(0,4)、A、B，
其中 A(P_0)=0、DA(P_0)=B 为单位，D^2A=-XA/4。
令
$$
\mathscr P=k(E)[z,t]/(z^p,t^p),\qquad
\mathcal O_z=\partial_z^2/12+3Xz^2/4,\quad
\mathcal O_t=\partial_t^2/12+3Xt^2/4.
$$
在原八维有限值通道上，定义
$$
\mathcal K=
D-\mathcal O_z-\mathcal O_t
-(M_e\otimes I_2+I_4\otimes M_o).
\tag{DP1}
$$
FT 的 U_e tensor U_o 精确平凡化最后的有限矩阵部分。

OP 的 lens gauge 可在两变量中同时使用。写 m=(p-1)/2、
q=(DA)/A，在 A 非零处设
$$
(\mathcal T\psi)(z,t)
=A^{2m}e^{-3q(z^2+t^2)}\psi(z/A,t/A).
$$
指数是该商环中的有限和；需要的阶乘均小于 p。
逐变量的 OP 计算给
$$
\mathcal T^{-1}(D-\mathcal O_z-\mathcal O_t)\mathcal T
=D-\frac{A^{-2}}{12}(\partial_u^2+\partial_v^2).
$$
由 D^p=0、D^{p-1}A^{-2}=-1、
(partial_u^2+partial_v^2)^p=0，Jacobson 公式准确给
$$
\mathcal K^p
=\frac1{12}\left[
(A\partial_z+6(DA)z)^2+
(A\partial_t+6(DA)t)^2\right]I_8.
\tag{DP2}
$$
函数域中证明的等式右侧正则，故可在 P_0 代值：
$$
\left.\mathcal K^p\right|_{P_0}
=3B^2(z^2+t^2)I_8.
\tag{DP3}
$$

因此任何在 P_0 正则的水平线性端同态 Q，即 [mathcal K,Q]=0，
其值 Q_0 都必须满足
$$
[Q_0,z^2+t^2]=0.
\tag{DP4}
$$
这对任意有限可分覆盖上的水平端同态同样成立。

## 2. 原稀疏临界空间及一个准确的一维核

令 p=6N+5>=41、m=(p-1)/2=3N+2。
在原 F tensor G 有限通道中定义
$$
W=\operatorname{span}_k
\{e_i=z^{6i+4}t^{6(N-1-i)+1}:0\le i<N\}.
\tag{DP5}
$$
所有单项式总度都是 p-6；它们的原系数正是
f_i g_{N-1-i}，没有改变 Gaussian 或标签。
令 R=z^2+t^2、q_*=2N+6。

在 z 偶、t 奇部分写 x=z^2、y=t^2。
去掉公共因子 t 后，商环是
$$
k[x,y]/(x^{m+1},y^m),
$$
而 e_i 对应 x^{3i+2}y^{3N-3-3i}，总度为 3N-1。
乘 R^{q_*} 后总度为 5N+5，允许的 x 次数恰为
$$
2N+4,\ 2N+5,\ \ldots,\ 3N+2,
$$
共 N-1 个。因此 R^{q_*}|_W 的矩阵是
$$
C_{r,c}=\binom{2N+6}{2N+2+r-3c},
\quad
0\le r\le N-2,\quad0\le c\le N-1.
\tag{DP6}
$$
超出二项式实际范围时按零解释。

**断言：C 的每个最大子式都非零。**
以下给出完整模 p 证明，不诉诸一般位置或数值检验。

写
$$
L=N-2,\quad q_*=2N+6,\quad x_c=2N+2-3c.
$$
第 c 列乘单位
$$
\frac{(x_c+L)!(q_*-x_c)!}{q_*!}
$$
后，第 r 行成为在 x_c 处的多项式值
$$
P_r(x)=
\prod_{u=r+1}^{L}(x+u)
\prod_{v=0}^{r-1}(q_*-x-v).
\tag{DP7}
$$
这里所有列因子都合法：
$$
x_c+L=3(N-c),\qquad q_*-x_c=4+3c
$$
均在 0 与 p-1 之间，且 q_*<p。
当原二项式因下指标小于零或大于 q_* 而为零时，
(DP7) 中相应乘积含零；因此没有使用负阶乘。

每个 P_r 的次数至多 L。它们在 x=q_*-j、0<=j<=L 处
构成三角矩阵：r>j 时第二个乘积为零，而 r=j 的值为
$$
j!\prod_{u=1}^{L-j}(q_*+u)\ne0.
$$
所有显示因子至多 q_*+L=3N+4<p。
所以 P_0,...,P_L 是次数至多 L 的多项式空间的一组基。

任取 N-1=L+1 个列参数 x_c。
它们两两之差为 3(c'-c)，均非零模 p。
其评价矩阵因此等于一个可逆基变换乘 Vandermonde 矩阵，
行列式是单位。这就证明断言。

从而
$$
\dim\ker(R^{2N+6}|_W)=1,
\tag{DP8}
$$
且该核的任意非零向量每个 e_i 坐标都非零。
若其中一个坐标为零，其余 N-1 列便产生非平凡关系，
与对应最大子式为单位矛盾。

## 3. 保持原稀疏标签的平行对角算子只能是常数

设 Q 为 (DP1) 的水平端同态，在 P_0 正则，并假定其在
原 W tensor e_(F,G) 上的限制准确为
$$
Q_0 e_i=w_i e_i,
\tag{DP9}
$$
没有漏出到其他单项式或有限通道。
不要求 Q 在其余空间对角；其余作用可任意。

由 (DP4)，Q_0 保持 ker R^{2N+6}。
由 (DP9)，它还保持 W，所以保持 (DP8) 的那条核直线。
取该直线中各坐标均非零的向量 c。
存在标量 lambda 使 diag(w_i)c=lambda c，故
$$
w_0=w_1=\cdots=w_{N-1}.
\tag{DP10}
$$

这正是该捷径的必要限制。它不仅排除常数系数的投影，
也排除依赖辅助点、但在 P_0 实现 (DP9) 的水平端同态。
它不排除在 W 上确有混合或漏出的真正群作用。

## 4. 原 primitive × Legendre 权对每个允许 p 都不恒定

R770 的准确权是
$$
w_i=\mathbf1_{(6i+7,p+1)=1}
P_{6i+6}(1/s),\qquad s^2=-3.
\tag{DP11}
$$
这些值都在 F_p 中。R734 已证明至少一个非端点真 primitive 标签
有单位 toric norm；用 R727/R770 的原公式，这等价于至少一个
(DP11) 非零。

首末未筛 Legendre 值为
$$
P_6(1/s)=-47/9,\qquad
P_{6N}(1/s)=P_{p-5}(1/s)=P_4(1/s)=19/9.
\tag{DP12}
$$
中间的模 p 反射是 R770(770.33) 的已证多项式恒等式。
最后两个显式值也可直接由 P_6、P_4 的整数公式算得。
二者之差为 -22/3，在 p>=41 为单位。

若首或末的 primitive 指示为零，(DP11) 有一个零，
又由 R734 有一个非零，所以不恒定。
若两者都为一，则 (DP12) 已给两个不同值。
因此 (DP11) 对每个允许 p 都不恒定，和 (DP10) 矛盾。

所以原完整加权算子 (DP11) 不存在 (DP9) 那样的水平延伸。
这里必须说清：**单独的 primitive 0/1 指示有时可以恒为一**；
本篇没有声称每个 p 的单独指示都非恒定。
对任何实际非恒定的 0/1 筛选，(DP10) 当然同样适用。

## 5. 非水平筛选的交换子必须保留

若以次数至多 p-1 的插值多项式 W_p(E_z) 延伸原权，
其中 E_z=z partial_z，并在所有有限通道上使用同一个算子，
则它与 D、M_e、M_o 及 t 方向交换。准确的剩余交换子为
$$
[\mathcal K,W_p(E_z)]
=-\frac1{12}\partial_z^2
 \bigl(W_p(E_z)-W_p(E_z-2)\bigr)
$$
$$
\hspace{15mm}
-\frac{3X}{4}z^2
 \bigl(W_p(E_z)-W_p(E_z+2)\bigr).
\tag{DP13}
$$
例如对 z^k，第一项准确乘
-k(k-1)(W_p(k)-W_p(k-2))/12，
第二项乘 -3X(W_p(k)-W_p(k+2))/4。

若原向量 Omega 满足 mathcal K Omega=S_boundary，则
$$
\mathcal K(W_p(E_z)\Omega)
=W_p(E_z)S_{\rm boundary}
+[\mathcal K,W_p(E_z)]\Omega.
\tag{DP14}
$$
不能删去第二项。即使第二行在 X(P_0)=0 时暂时为零，
再施行 D 后会出现 DX(P_0)=8，仍然参与完整 p 次传播。
若还投影到单独 F tensor G 通道，必须再保留有限矩阵的交换子。

重复 p 次时，所有交换子恰合并为
$$
[\mathcal K^p,W_p(E_z)]
=3B^2[R,W_p(E_z)]\quad\text{在 }P_0.
\tag{DP15}
$$
这说明只把同一曲率恒等式投影、再形式消去交换子，
不会凭空产生一个新的带筛非零量。
要继续使用 (DP14)，必须实际控制这些不同标签间的传递，
或转向有真实矩阵系数/配对解释的非对角群作用。

本篇没有证明 W 上原实际系数向量落在 (DP8) 的核，
也没有把 (DP8) 的抽象满支撑向量冒认为原 sigma 系数。
它只严格判定指定的平行对角运输机制不可能。
