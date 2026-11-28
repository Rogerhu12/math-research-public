# R677：真实二阶无穷小转动场与零角速分支的全余核条件

2026-11-28。对 [R673](R673-thick-bowed-tilted-endpoint-metric-with-strict-intrinsic-chord-slack.md) 正端的固定度量，推导真实等距族的二阶边界倾角矩。另给零一阶转角分支的有限空间诊断：一条投影能确定候选二阶角加速度，其余全部余核方向仍需同时满足。本文没有将 [R675](R675-central-bending-moment-for-an-infinitesimal-bowed-endpoint-tilt.md) 的有限 QR 矩阵提升为无穷维算子的值域，亦未重算任何已付矩阵。

## 1. 真等距族的二阶转动场

设 $X(t)$ 是同一固定材料度量的等距族，以下对参数二阶可微至 $C^2$ 空间，外刚帽锚定。取 $t=0$ 为 R673 正端。在每个 $t$ 有无穷小转动场 $Y(t)$ 满足 $\partial_t X_i=Y\times X_i,~\partial_t n=Y\times n$。记 $Y=Y(0)$、$Z=\partial_tY(0)$，而 $b,\dot b,\ddot b$ 是材料坐标内的第二基本形式及两阶时间导数。于是
$$
 \partial_t^2X_i|_0=Z\times X_i+Y\times(Y\times X_i),\qquad
 \dot b_{ij}=n\cdot(Y_i\times X_j).
$$
对第二式微分。刚性角速度 $Y$ 同时作用于三重积的三个向量时，其总变化为零，得
$$
 \ddot b_{ij}=n\cdot[(Z_i-Y\times Y_i)\times X_j].               \tag{1}
$$
$Y_i(t)\cdot n(t)=0$ 是每一时刻的准确兼容关系，微分给 $(Z_i-Y\times Y_i)\cdot n=0$；故 (1) 中的新向量仍严格切向。

在固定材料基 $(\partial_r,r^{-1}\partial_\varphi)$，Gauss 方程右端 $K\det g$ 与 $t$ 无关，两次微分给
$$
 b_{22}\ddot b_{11}-2b_{12}\ddot b_{12}+b_{11}\ddot b_{22}
      =-2(\dot b_{11}\dot b_{22}-\dot b_{12}^2).                  \tag{2}
$$
沿 R675 的材料 $\varphi=\pi/2$，以 $N=R_y(\omega)e_z-H'\cos\omega\,e_y$ 为未归一面积向量。如 R675 对任意切向 $v$ 的恒等式，$n\cdot[v\times(X_\varphi/r)]=|N|v\cdot e_y$。取 $v=Z_r-Y\times Y_r$，(1) 变为 $\ddot b_{12}=|N|(Z_r-Y\times Y_r)\cdot e_y$。代回 (2)，得
$$
\begin{split}
 Z_y(b)-Z_y(a)={}&
 \int_l^u\frac{\cos\omega}{2\omega'|N|}
       \left[\frac{H'}{r}\ddot b_{11}+H''\ddot b_{22}\right]dr\\
 &+\int_a^b\left[
    \frac{\dot b_{11}\dot b_{22}-\dot b_{12}^2}{\omega'}
           +(Y\times Y_r)\cdot e_y\right]dr .                     \tag{3}
\end{split}
$$
首项只在真正弓形支撑积分，那里 $\omega'=-M/r$ 有正的绝对值下界。第二项中的商对**满足二阶 Gauss 的真族**沿弓外满足
$$
 (\dot b_{11}\dot b_{22}-\dot b_{12}^2)/\omega'=\ddot b_{12}/|N|,
$$
因此平接圈上的两端由上述连续右端延拓，毋须在 $\omega'=0$ 直接取商。对任一未验证的数值近核没有这个延拓承诺。内帽绕同一 $y$ 轴以真实角 $\theta(t)$ 运动时左端为 $-\theta''(0)$，不受内平移影响。若允许任意轴的二阶刚体运动，则使用左端真实角速度导数的 $y$ 分量。

## 2. 零角速起步的必要全空间行

考虑 $\theta'(0)=0$，并允许两刚件间有真实零倾角的一阶形变 $V$。必须先有 $Dg(V)=0$ 和相应零倾角边界；对反射破缺模式也应使用其真实奇偶扇区。取零二阶倾角的自由场 $U$（可含自由内平移）及单位倾角的固定提升 $P$。若其余刚体转角一阶也为零，则二阶位移可写成 $U+\Theta P$，$\Theta=\theta''(0)$。二阶同度量条件为
$$
 A U+\Theta d+h=0,\quad A=Dg|_{\rm free},\quad d=Dg(P),\quad
 h_{ij}=2\,\partial_i V\cdot\partial_j V .                        \tag{4}
$$
假如放宽一阶刚帽角轴，还须加一阶刚姿的二次加速度，不可在 (4) 中漏掉。取所声明应变 Hilbert 空间中对 $\overline{\operatorname{ran} A}$ 正交补的投影 $\Pi$。若 $e=\Pi d\ne0$，必要的转角和所有剩余正交分量是
$$
 \Theta=-\langle e,\Pi h\rangle/\|e\|^2,\qquad
 \Pi h-\frac{\langle e,\Pi h\rangle}{\|e\|^2}e=0.               \tag{5}
$$
后式是完整向量条件。若 $e=0$，这个方法只要求 $\Pi h=0$，未确定 $\Theta$。即便满足 (5)，若真实值域不闭或要求更强空间正则性，仍须解 (4) 取得有控制的 $U$。一组确切零角速核的任意线性组合还会给 $h$ 的交叉二次项，不能只查每个候选方向的独立平方。

在一个指定加权离散矩阵 $A_N$ 上，同一公式对**该矩阵**的准确列空间和完整左正交补成立。实际应使用完整分解、各方向原始残差和独立自然细网。$\operatorname{dist}(d_N,\operatorname{ran}A_N)>0$ 不是无限维余核的证明；最小奇异向量只是有限基坐标归一的方向，也不自动是物理 $C^2$ 归一后仍非零的真核。只有这些量跨空间稳定并获得适当紧性及一致误差后，才有资格联系真族。本文的精确二阶恒等式 (3) 与有限矩阵诊断 (5) 各自适用其前提。
