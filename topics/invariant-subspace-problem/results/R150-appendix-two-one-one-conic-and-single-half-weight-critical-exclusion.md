# R150 附录：双点加两单点中的全部单点半权分支排除

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明。** 在原非 secant、外 mean、$T_3$ 本质三维且 $H$ 秩四的完整临界截面中，若共同支撑为 $2s+t+u$，三个点不同，则两个单点的任何一个都不能具有归一权 $1/2$。本条同时排除了两个单点各为 $1/2$ 的二次曲线分支，以及恰一个单点为 $1/2$ 的全部节点三次分支，包括所有零交叉值和例外复权。

结合[非约化中心三次分类](R150-appendix-nonreduced-four-jet-central-cubics-and-half-weight-conditions.md)，此支撑类型只剩**双点块总权为 $1/2$、两个非零单点权之和为 $1/2$**。本文不将这一剩余条件称为存在性结论。

## 1. 原支撑与梯度记号

仍按原 $\lambda$ 作单位归一，并把双点的最高 nilpotent 权缩放为一。在基 $u_0,u_1,v,w$ 中，前三者的下标 $0,1$ 属于双点，另两个基向量为单点。原核的限制形如
$$
\overline K=
\begin{pmatrix}
0&0&a&b\\
0&h&c&d\\
a&c&0&e\\
b&d&e&0
\end{pmatrix}.
\tag{1.1}
$$
所有归一都是支撑块内的可逆三角变换。原矩仍准确由有限代数泛函给出
$$
y(r)=\tau(X),\qquad H(r,r)=\tfrac14\tau(X^2),\qquad
V(r,r,r)=\tfrac18\tau(X^3).
\tag{1.2}
$$
所有权为复数，不加正性假设。

沿用[三重加单点稿](R150-appendix-three-plus-one-full-rank-outer-mean-critical-exclusion.md)的完整 $G,N$ 公式，记 $\mathcal G_i=128G_i$。对双点局部曲线 $\rho(z)=(1,z,0,0)^{\mathsf T}$，记
$$
\mathcal H_j=32[z^j]\rho(z)^{\mathsf T}\overline KN\overline K\rho(z),
\qquad
\mathcal V_j=8[z^j]T_3(\overline K\rho(z)),
\quad j=0,1.
$$
两个单点的相应常数项记为 $\mathcal H_2,\mathcal H_3,\mathcal V_2,\mathcal V_3$。全部 $\mathcal G,\mathcal H,\mathcal V$ 都是原完整临界点的必要零式。

[整数多项式重构器](../notes/2026-11-13-two-one-one-single-half-critical-exclusion-verify.js)从 (1.1)–(1.2) 重建全部原张量和本条使用的恒等式，检查完整消元及分母例外；[实际输出](../notes/2026-11-13-two-one-one-single-half-critical-exclusion-certificate.json)为 all_pass: true。该计算只核验有限恒等式，以下仍逐项给出复数域排除证明。

后面多次使用[原长度三等向 jet 分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)：原全等向长度三曲线 jet 空间只有三不同支点的 $W_\pm$，所以**双点加另一单点的三维 jet 空间不可能全等向**。该定理覆盖有限与无穷远支点。

## 2. 先排两个单点各为一半的二次分支

此时双点总权为零，
$$
\tau(1_s)=0,\quad\tau(\varepsilon)=1,\quad
\tau(1_t)=\tau(1_u)=\tfrac12.
$$
在四个对偶坐标 $r_0,r_1,r_2,r_3$ 中，中心三次式准确分解为
$$
T_3=\tfrac12r_1 Q,\qquad
Q=3(r_2-r_0)(r_3-r_0)+3r_1(r_2+r_3-2r_0)+2r_1^2.
\tag{2.1}
$$
原物理像不可约且张成平面，故必须落在光滑二次因子 $Q$ 上。

由[光滑二次中心定理](R150-appendix-four-jet-smooth-quadric-center-and-birational-projection.md)，该二次像迫四维物理投影存在基点；由[长度四基点定理](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md)，基点只能是支撑中的 $s,t,u$，且至多一个简单基点。

在双点处，$Q(\overline Ku_0)=3ab$，所以 $ab=0$；第一 jet 系数是
$$
3\{ad+bc+h(a+b)\}=0.
\tag{2.2}
$$
若 $a=0,b\ne0$，唯一可能的四维基点只能是 $t$，于是 (1.1) 的第三列必须为零，即 $c=e=0$。(2.2) 再迫 $h=0$。于是 $\operatorname{span}(u_0,u_1,v)$ 全等向，违反原长度三分类。$b=0,a\ne0$ 的情形交换两个单点后相同。

只剩 $a=b=0$。完整 $y$ 梯度给
$$
\mathcal G_2=16h(h+2d),\qquad
\mathcal G_3=16h(h+2c),
$$
$$
\mathcal G_1=32h^2+32eh+64(c+d)h+64cd.
\tag{2.3}
$$
若 $h\ne0$，前两式迫 $c=d=-h/2$，后一式迫 $e=h/2$。但单点最高梯度此时为
$$
\mathcal V_2=8c^3+12c^2e=\tfrac12h^3\ne0,
$$
矛盾。因此 $h=0$；(2.3) 再给 $cd=0$。$c=0$ 或 $d=0$ 又分别产生双点加一个单点的全等向三维空间，同样不可能。二次分支全部排除。

## 3. 恰一个单点权为一半时的最高分裂

交换两个单点后可设
$$
\tau(1_t)=\tfrac12,\qquad
\tau(1_u)=\tfrac{\theta}{2},\qquad
\tau(1_s)=\tfrac{1-\theta}{2},\qquad
\tau(\varepsilon)=1.
\tag{3.1}
$$
单点权非零使 $\theta\ne0$；$\theta=1$ 已在 §2 排除，所以以后
$$
\theta\notin\{0,1\}.
\tag{3.2}
$$
原最高梯度在双点处准确分解为
$$
\boxed{\mathcal V_0
=\theta(\theta-1)b^2\{3a+(\theta-2)b\}.}
\tag{3.3}
$$
因此分为 $b=0$ 与 $b\ne0$ 两类，不使用稠密图代替零边界。

## 4. $b=0$：节点位于双点的分支全部排除

当 $b=0$，完整梯度给
$$
\frac{\mathcal G_2}{16}
=h^2+2\theta dh+\theta(\theta-1)d^2,
\tag{4.1}
$$
$$
\frac{\mathcal H_1}{8}
=a\{2h^2+3\theta dh+\theta(\theta-1)d^2\}.
\tag{4.2}
$$
若 $a\ne0$，用 (4.2) 减去两倍 (4.1)，得到
$$
d\{h+(\theta-1)d\}=0.
$$
若 $d\ne0$，代回 (4.1) 会得到 $-(\theta-1)d^2=0$，违反 (3.2)。所以 $d=0$，再由 (4.1) 得 $h=0$。此时 $b=d=h=0$，$\operatorname{span}(u_0,u_1,w)$ 全等向，不可能。

若 $a=0$，仍有 (4.1)。$d=0$ 会同样迫 $h=0$ 并产生全等向三维空间，因此只须考虑 $d\ne0$。由
$$
\mathcal V_3=4d^2(3e+2d)=0
$$
得到 $e=-2d/3$。利用必要方程关于 $\overline K$ 的齐次性，可取 $d=3,e=-2$。

(4.1) 变成 $(h+3\theta)^2=9\theta$。可选 $r$ 使
$$
\theta=r^2,\qquad h=3r(1-r),\qquad r\ne0,\ \pm1.
$$
此时 $\mathcal G_1=0$ 对 $c$ 的系数非零，准确给
$$
c=r(r-1).
$$
最后一个完整梯度为
$$
\boxed{\mathcal G_0=96r^2(r-1)\ne0,}
$$
矛盾。因此 $b=0$ 的全部分支都已排除。

## 5. $b\ne0$：先支付线性梯度与所有分母

由 (3.3) 及齐次性，可固定
$$
b=3,\qquad a=2-\theta.
\tag{5.1}
$$
两个原梯度的完整展开为
$$
\mathcal V_1
=9\theta\{2(\theta+1)h+(\theta-1)(\theta-2)d+3(\theta-1)c\},
$$
$$
3\mathcal H_0-2\mathcal V_1
=18\theta(\theta-1)\{3(\theta-2)e+(\theta-2)d+3c\}.
$$
故
$$
\boxed{3c=-(\theta-2)(3e+d),\qquad
2(\theta+1)h=3(\theta-1)(\theta-2)e.}
\tag{5.2}
$$
若 $\theta=2$，这立即给 $a=c=h=0$，产生
$\operatorname{span}(u_0,u_1,v)$ 全等向，矛盾。因而
$$
\theta\notin\{0,1,2\}.
\tag{5.3}
$$
此后可合法用
$$
e=\frac{2(\theta+1)h}{3(\theta-1)(\theta-2)},\qquad
c=-\frac{\theta-2}{3}d-\frac{2(\theta+1)}{3(\theta-1)}h.
\tag{5.4}
$$
注意没有除以 $\theta+1$；$\theta=-1$ 仍完整保留。

## 6. 剩余二次梯度的锥参数化

在 (5.1) 上，另一个原梯度准确为
$$
\boxed{\mathcal G_2=
16\left\{\left(h+\theta d-\tfrac32\theta(\theta+1)\right)^2
-\theta(d-3\theta)^2\right\}.}
\tag{6.1}
$$
因此可取 $r,u$ 使
$$
\theta=r^2,\qquad
d=3r^2+u,\qquad
h=(r-r^2)u+\tfrac32r^2(1-r^2).
\tag{6.2}
$$
这覆盖整个零锥：当 $d-3\theta=0$ 时，两边第一平方也为零；否则选择两个平方根之一。没有除以 $u$。由 (5.3)，
$$
r\ne0,\ \pm1,\qquad r^2\ne2.
\tag{6.3}
$$

为了逐项展示分母均已支付，置
$$
q=3(r^2-1)(r^2-2)\ne0,\qquad
D=6r^2+2u,\qquad
H=2(r-r^2)u+3r^2(1-r^2).
$$
将 (5.4)、(6.2) 的矩阵整体乘以 $2q$，得到无分母的同一齐次必要条件矩阵 $\widetilde K$，其六个条目为
$$
\begin{aligned}
\widetilde a&=2(2-r^2)q,&\widetilde b&=6q,\\
\widetilde d&=qD,&\widetilde h&=qH,\\
\widetilde e&=2(r^2+1)H,\\
\widetilde c&=-(r^2-1)(r^2-2)^2D
             -2(r^2+1)(r^2-2)H.
\end{aligned}
\tag{6.4}
$$
$\mathcal G$ 关于 $K$ 是二次齐次式，所以此非零整体缩放保留其零条件。

直接代入原完整梯度，准确有
$$
\boxed{\begin{aligned}
\mathcal G_3(\widetilde K)
={}&192r^2(r^2-1)(r^2-2)(r-1)^2(r^2+1)\\
&\quad\cdot\{2u+3r(r+1)\}^2.
\end{aligned}}
\tag{6.5}
$$
重构器从完整原张量验证 (6.1)、(6.4)–(6.5)，不使用数值拟合或有限采样外推。

## 7. 非例外锥点与 $\theta=-1$ 均给矛盾

若 $r^2+1\ne0$，(6.3)、(6.5) 迫
$$
u=-\tfrac32r(r+1).
$$
此时 $h=0$，$D=3r(r-1)$。在同一已清分母矩阵上，另一个完整梯度准确为
$$
\boxed{\mathcal G_1(\widetilde K)
=1728r^3(r^2-1)^2(r^2-2)^2(r^2+1).}
\tag{7.1}
$$
右边所有因子都非零，矛盾。

若 $r^2+1=0$，则 $\theta=-1$。回到 (5.1)–(5.2) 的原规范矩阵，不需作任何除法：
$$
a=b=3,\qquad e=0,\qquad c=d.
$$
原梯度准确给
$$
\mathcal G_0=-32h^2,\qquad \mathcal V_2=8d^3.
$$
故 $h=d=0$；但此时 $\mathcal G_2=144$，仍矛盾。至此包含 $\theta=-1$ 在内的所有非零 $b$ 分支都已排除。

## 8. 结论与尚未处理的半权结构

两个单点各为 $1/2$ 的二次像由 §2 排除；恰一个单点为 $1/2$ 的节点三次像由 §§3–7 排除。全部步骤均保留原核、原 $\lambda$、完整梯度与复权边界。

因此本文支撑类型若仍有完整临界点，只能满足
$$
\boxed{\tau(1_s)=\tfrac12,\qquad
\tau(1_t)+\tau(1_u)=\tfrac12,\qquad
\tau(1_t)\tau(1_u)\ne0.}
$$
这是双点块本身承担半权的剩余结构，本文尚未排除。其他本质维数、低 mean Hankel 秩、全局自然幂成员关系及实际算子逆也仍须处理；普通复 Hilbert 空间 ISP 的完成标准尚未达到。

本条在执行环境失联期间通过代码模式精确整数运算完成并以仓库小文本后备保存。API 同步不记作真实 git pull；终端恢复后仍须实际同步。
