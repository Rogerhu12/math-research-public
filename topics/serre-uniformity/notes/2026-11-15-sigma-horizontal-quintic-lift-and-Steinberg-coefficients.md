# 原 critical 的五次水平 lift 与 Legendre 矩阵系数

日期：2026-11-15。状态：**五次水平算子、原标签的准确 lift、旋转矩阵系数及原平方常数已证明；带筛共同非零仍开放。**

接续 FT、OP 及
notes/2026-11-15-sigma-critical-projection-curvature-obstruction.md（简称 DP）。
本篇给出一个不同于被 DP 排除的平行对角筛选的实际结构：
先用水平微分算子把原总阶 p-6 提升到 p-1，
再把原 Legendre 权实现为一个真正水平旋转的对角矩阵系数。
完整旋转与其对角部分严格分开。

## 1. 保留原双变量连接和全部边界

令 p=6N+5>=41，保留
$$
Y^2=X^3+16,\quad DX=2Y,\quad DY=3X^2,\quad P_0=(0,4),
$$
以及原 Hasse 多项式 A 与 Cartier 单位 B：
$$
D^2A=-XA/4,\qquad A(P_0)=0,\qquad DA(P_0)=B\ne0.
\tag{QS1}
$$
在 mathscr P=k(E)[z,t]/(z^p,t^p) 的八个有限值通道中，令
$$
\mathcal K=
D-\frac{\partial_z^2+\partial_t^2}{12}
-\frac{3X}{4}(z^2+t^2)
-(M_e\otimes I_2+I_4\otimes M_o).
\tag{QS2}
$$
这是 FT、DP 的原连接；未改变原 c=0 Gaussian。

写 Omega=Phi_(e,<p)(z) tensor Phi_(o,<p)(t)。
由 FT 的偶边界与 MH 的奇边界，准确有
$$
\mathcal K\Omega=\mathcal S,
$$
$$
\mathcal S=
-z^{p-1}\left(\frac A6e_H+\frac{DA}{2}e_R\right)
 \otimes\Phi_{o,<p}(t)
+\frac A{12}t^{p-2}\Phi_{e,<p}(z)\otimes e_G.
\tag{QS3}
$$
这里 e_G=(0,1)^t 属于原奇通道，e_H、e_R 属于原偶通道。
即使 A(P_0)=0，也必须先做全部 D 导数，再在 P_0 评价；
不能在 (QS3) 中预先删去 A 项。

## 2. 两个水平一阶算子

定义 k(E)-线性算子
$$
L_z=A\partial_z+6(DA)z,\qquad
L_t=A\partial_t+6(DA)t.
\tag{QS4}
$$
它们是有限 z、t 多项式空间中的算子，不含辅助 D。
由于有限矩阵部分与 z、t 算子交换，
$$
[\mathcal K,L_z]
=(DA)\partial_z+6(D^2A)z
-\left((DA)\partial_z-\frac32AXz\right)
=0
\tag{QS5}
$$
恰由 (QS1) 得到；t 方向完全一样。
两算子彼此也交换。因此
$$
\mathcal R=L_z^2L_t^3,\qquad
[\mathcal K,\mathcal R]=0.
\tag{QS6}
$$
这是一个实际的五次水平算子，不是只在 P_0 形式写出的乘法。

令 widehat Omega=mathcal R Omega。完整源方程变成
$$
\mathcal K\widehat\Omega=\mathcal R\mathcal S.
\tag{QS7}
$$
由 DP 的曲率也有
$$
\mathcal K^p\widehat\Omega
=\mathcal R\mathcal K^{p-1}\mathcal S.
\tag{QS8}
$$
没有删除任何有限矩阵通道或跨 p 边界。

## 3. 原 CM 点的准确五次 lift

由于 L_z、L_t 不含 D，(QS1) 允许直接在 P_0 对这些算子评价：
$$
L_z|_{P_0}=6Bz,\qquad L_t|_{P_0}=6Bt,
$$
$$
\boxed{\mathcal R|_{P_0}=(6B)^5z^2t^3.}
\tag{QS9}
$$
原 F tensor G 的 critical 齐次部分为
$$
\sum_{i=0}^{N-1}
f_i g_{N-1-i}\,
z^{6i+4}t^{6(N-1-i)+1}.
$$
置
$$
h=6i+7,\qquad n=h-1.
$$
(QS9) 把它准确送到总次数 p-1 的
$$
\boxed{
\widehat v=
(6B)^5\sum_{i=0}^{N-1}
f_i g_{N-1-i}\,z^{h-1}t^{p-h}.
}
\tag{QS10}
$$
两指数都小于 p；原总阶 p-6 的整个齐次空间乘 z^2t^3
也没有截断溢出。因此此 lift 在该齐次空间单射，
且严格保留同一个原 h。

若 E_n=z^n t^{p-1-n}，记
$$
\widehat c_h=[E_{h-1}]\widehat v
=(6B)^5f_i g_{N-1-i}.
\tag{QS11}
$$
总阶变成 p-1 是有实质意义的；这里不再把
Sym^(p-6) 的一般 Jacobi 型矩阵系数误认成原 Legendre 权。

## 4. 一个真正水平旋转的准确对角系数

取 s^2=-3，置 x_0=1/s，并在有限常数扩张中选 a,b，使
$$
a^2=\frac2{1+x_0}=\frac{2s}{s+1},\qquad
b^2=1-a^2=\frac{1-s}{s+1}.
\tag{QS12}
$$
a、b 均非零。这里 p>=41，所有显示分母都是单位。
令
$$
g=\begin{pmatrix}a&b\\-b&a\end{pmatrix},\qquad
(T_gP)(z,t)=P(az+bt,-bz+at).
\tag{QS13}
$$
g 保持 z^2+t^2 及 partial_z^2+partial_t^2，
且 (z^p,t^p) 在任何可逆线性变量替换下保持。
所以 T_g 是整个 mathscr P 上的可逆常数算子，并满足
$$
[\mathcal K,T_g]=0.
\tag{QS14}
$$
它不改变八个有限值通道。

对 0<=n<=p-1，展开 E_n 的对角系数：
$$
[T_g]_{n,n}
=\sum_j
\binom nj\binom{p-1-n}{j}
a^{p-1-2j}(-b^2)^j.
$$
模 p 有
binom(p-1-n,j)=(-1)^j binom(n+j,j)。
当 j 超出原第二个二项式范围时，右边也因含 p 而为零。
因此用 Legendre 的完整整数展开得到
$$
\boxed{
[T_g]_{n,n}
=a^{p-1}P_n(1+2b^2/a^2)
=a^{p-1}P_n(1/s).
}
\tag{QS15}
$$
公共相位 a^(p-1) 不可设为一。
定义准确归一化的水平算子
$$
\widehat T_g=a^{1-p}T_g.
\tag{QS16}
$$
于是
$$
\boxed{[\widehat T_g]_{n,n}=P_n(1/s).}
\tag{QS17}
$$
改变所选 a、b 的平方根符号不改变这些对角系数；
完整非对角矩阵当然仍须使用同一选择。

## 5. 与原同标签平方公式的全部常数

本节用 alpha_0 表示原 R770 的 alpha_0^3=4；
它与 FT 覆盖中的 alpha^3=-4/27 不同。
对每个原 primitive h=6i+7，R770(770.17) 是
$$
\left(\frac{p^2M_{2,h}}{\zeta}\right)^2
=\left(
1296\,\alpha_0sB^5
P_{h-1}(1/s)f_i g_{N-1-i}
\right)^2.
$$
结合 (QS11)、(QS17)，且 1296/6^5=1/6，得到
$$
\boxed{
\left(\frac{p^2M_{2,h}}{\zeta}\right)^2
=
\left(
\frac{\alpha_0s}{6}\,
[\widehat T_g]_{h-1,h-1}\,
\widehat c_h
\right)^2
\quad\bmod p.
}
\tag{QS18}
$$
这个等式保留原 toric Norm 的 Legendre 因子、原 B^5、
原正三次标签及全部单位常数。
它仍只是原准确平方公式；没有选择随 h 变化的解析平方根符号。

因此原目标等价于：对某个同一 primitive h，
(QS18) 右边的两个显示矩阵/系数因子乘积非零。
这里的矩阵因子是一个真正水平旋转的同标签矩阵系数；
并没有把它错误地换成整个旋转后向量的该坐标。

## 6. 真正水平的 Cartan 字符投影与其混合

在代数闭常数域中取 iota^2=-1，写
$$
u=z+\iota t,\qquad v=z-\iota t.
$$
正交变换 u mapsto lambda u、v mapsto lambda^(-1)v
给算子 J_lambda，并与 mathcal K 交换。
(QS6) 改变总次数的奇偶性；widehat Omega 位于总偶子空间。
因此 J_(-lambda)=J_lambda 在该子空间成立。

对 q 属于 mu_(p+1)，任选 lambda^2=q，定义
$$
\rho(q)=q^{(p+1)/2}J_{\lambda}^{-1}.
\tag{QS19}
$$
它与 lambda 的符号无关，是 mu_(p+1) 的真正表示，
且每个 rho(q) 与 mathcal K 交换。
在总阶 p-1 上，
$$
\rho(q)\,u^n v^{p-1-n}
=q^{-n-1}u^n v^{p-1-n}.
\tag{QS20}
$$
所以用原 Teichmueller 方向 q mapsto q^(-h) 可定义
$$
\mathsf E_h=\frac1{p+1}\sum_{q\in\mu_{p+1}}q^h\rho(q),
\tag{QS21}
$$
它在该齐次空间恰投到 n=h-1 的一维特征空间。
分母 p+1 为单位。对原允许的 primitive h 求和，
确实得到与 heat 连接交换的字符投影。

这里必须区分两个基：
(QS10) 的原系数在 z,t 单项式基中，
(QS20) 的特征线在 u,v 单项式基中。
二者通过完整 Krawtchouk 型变换混合。
(QS19)--(QS21) 给出准确字符方向，但本篇没有把抽象字符方向
误当成已识别的原 split vector、原 period basis 与原同标签系数。
若要把这组作用进一步与原 F_p 上 T_zeta 的具体矩阵识别，
还须把其二次型及 split vector 一并运输，不能只改 torus。

这些算子给真实的源传播式，例如
$$
\mathcal K(\mathsf E_h\widehat T_g\widehat\Omega)
=\mathsf E_h\widehat T_g\mathcal R\mathcal S.
\tag{QS22}
$$
这条式子完整保持其真正字符投影。
但目前尚未证明其指定输出等于 (QS18) 的原同标签乘积，
也未证明所需输出非零。

## 7. 为什么五次 lift 后仍不能删去混合

完整旋转不是其对角部分。
例如对每个 n，其第零行系数为
$$
[T_g]_{0,n}=b^n a^{p-1-n}\ne0.
\tag{QS23}
$$
所以一个原 h 单项式会漏出到端点及其他标签。
由 T_g 可逆、或由某个 Cartan 投影非零，
都不能直接推出 [widehat T_g]_(n,n) widehat c_h 非零。

DP 的平行对角障碍在 lift 后也能直接看见。
令 m=3N+2，写 x=z^2、y=t^2。
(QS10) 的稀疏空间在
k[x,y]/(x^(m+1),y^(m+1))
中由次数 m 的
$$
x^{3i+3}y^{3N-3i-1},\qquad0\le i<N
$$
张成。乘 (x+y)^(2N+4) 后，允许 x 次数为
2N+4,...,3N+2，共 N-1 项。
矩阵为
$$
\binom{2N+4}{2N+1+r-3i},
\qquad0\le r\le N-2.
\tag{QS24}
$$
DP 的同一 Vandermonde 证明适用：
取 L=N-2、x_i=2N+1-3i，则
x_i+L=3N-1-3i>=2、
q-x_i=3i+3、q+L=3N+2，均小于 p。
所有最大子式仍为单位，核仍是一条各坐标均非零的直线。
因此对 lift 后原稀疏空间作同样无漏出的非恒定对角权，
依然不可能是水平端同态。

本篇真正新增的是 (QS6)、(QS9)、(QS18)：
原五次移位可以水平实现，原 Legendre 权也有准确的水平矩阵系数来源。
下一步须使用完整非对角表示或原配对，而不是再次取对角后
假装仍与连接交换。原未筛共同非零及 primitive/Legendre 同标签非零均未完成。
