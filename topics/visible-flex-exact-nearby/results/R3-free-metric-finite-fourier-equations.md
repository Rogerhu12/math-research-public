# R3：自由径向度量的精确消元与有限 Fourier 构造方程

**状态：已证明的中间结论。** 本结果给出本题允许自选度量时的精确方程，以及有限 Cartesian Fourier 构造成为完整精确解的充要条件；另给一个非旋转精确环带子族的完整解。它不声称存在满足主目标的闭曲面，也不把局部环带或有限维方程的列出当成本题完成。

**正则性约定。** 区间 $I$ 上的映射至少为 $C^2$，角变量属于 $\mathbb R/(2\pi\mathbb Z)$。在要求坐标变换的地方假设映射浸入。第 3 节的分类只适用于列明的实系数 ansatz 及 $ABC\ne0$ 的区间。

以下计算均为完整 Fourier 系数恒等式，不使用采样或浮点误差。

## 1. 本题可以把径向平均度量作为输出

本题允许另选 $g$。因而对一条候选带 $F:I\times S^1\to\mathbb R^3$，可以求
$$
P_{\ne0}(F_r\cdot F_r)=P_{\ne0}(F_r\cdot F_\theta)
=P_{\ne0}(F_\theta\cdot F_\theta)=0,
\tag{1}
$$
其中 $P_{\ne0}$ 是材料角 Fourier 非零模投影。若 $F$ 是浸入，(1) 精确成立，则其诱导度量为
$$
g=E(r)\,dr^2+2B(r)\,dr\,d\theta+C(r)\,d\theta^2,\qquad C>0,\quad EC-B^2>0.
$$
这是一个精确、$S^1$ 不变的输出度量；没有理由再强迫其三个平均分量等于原数值解采用的预定平均分量。

设
$$
\psi=\theta+\chi(r),\quad \chi'=B/C,\qquad
s'=\sqrt{E-B^2/C},\qquad a(s)=\sqrt{C(r(s))}.
$$
直接代入得 $g=ds^2+a(s)^2d\psi^2$。该坐标变换在每个圆上仍为次数一映射，材料角平移在新旧坐标中都是同一个 $S^1$ 作用。若两开领圈已精确为旋转嵌入，(1) 的修正取为领圈上零，便不会改变这些领圈。两端的 $\chi$ 常数可以不同；相位作用不因此改变。

注意：把近似诱导度量取角平均并不能证明平均度量被原图实现。真正必须求解的仍是 (1)。这一消元只删除三个径向平均方程，不支付全频逆估计与两端闭合。

## 2. 有限 Cartesian Fourier 的完整方程

令
$$
F(r,\theta)=\sum_{k=-N}^N c_k(r)e^{ik\theta},\qquad
c_{-k}=\overline{c_k},\quad c_0\in\mathbb R^3.
$$
点积在复向量上作双线性延拓。令不存在的 $c_k$ 为零。则 (1) 等价于对每个 $1\le |j|\le2N$ 同时满足
$$
\sum_{k+l=j}c'_k\cdot c'_l=0,
\quad
\sum_{k+l=j}i l\,c'_k\cdot c_l=0,
\quad
\sum_{k+l=j}(-kl)c_k\cdot c_l=0.
\tag{2}
$$
证明这一等价只需逐项微分并相乘：三个度量分量的第 $j$ 个 Fourier 系数正是 (2) 的三个左边；现实条件使负模等于正模的共轭。有限 Fourier 多项式恒等为常数，当且仅当所有非零 Fourier 系数为零。这是真正有限的微分代数系统，并非只把方程投影回 $|j|\le N$。必须保留至 $2N$ 的所有模式；若 (2) 完整成立，任何更高角模都由于乘积次数而严格为零。因而该路线原则上可免除无限 Fourier 尾，但不能只解低模。

三个平均输出为
$$
E=\sum_k c'_k\cdot\overline{c'_k},\quad
B=\sum_k(-ik)c'_k\cdot\overline{c_k},\quad
C=\sum_k k^2c_k\cdot\overline{c_k}.
\tag{3}
$$
其中 $B$ 因现实条件为实数。这里双计正负模正是实际 Fourier 归一的结果。

### 最高模的固定复平面

在 $c_N\ne0$ 的区间，(2) 的 $j=2N$ 给
$$
c_N\cdot c_N=0,\qquad c'_N\cdot c'_N=0.
$$
对第一式求导亦有 $c_N\cdot c'_N=0$。在 $\mathbb C^3$ 中，一个非零零向量 $v$ 的正交补中，所有零向量均为 $v$ 的倍数：经复正交变换令 $v=(1,i,0)$，正交条件给 $w_1+iw_2=0$，零条件进一步给 $w_3=0$。因此
$$
c'_N=\lambda(r)c_N,\qquad c_N(r)=\alpha(r)v_0,
\tag{4}
$$
其中 $v_0$ 为固定复零向量。局部选择 $c_N$ 一个不为零的分量即可定义连续 $\lambda$ 并积分，故没有除以零向量的隐含步骤。其余低模仍可变化，(4) 不是一般不可能性结论。

## 3. 两个反向圆模和一个竖直模：精确消元

尝试
$$
F=(A(r)\cos(n\theta)+B(r)\cos(m\theta),\
 A(r)\sin(n\theta)-B(r)\sin(m\theta),\
 z_0(r)+C(r)\cos(p\theta)),
\tag{5}
$$
其中 $m,n\ge1$、$m\ne n$、$p=(m+n)/2\in\mathbb N$，且在所讨论区间 $ABC\ne0$。假设 $A,B,C,z_0$ 为实函数。

$G=F_\theta^2$ 的非零角模仅为 $m+n=2p$，它的系数为
$$
-2mnAB-\frac{p^2C^2}{2}.
$$
故
$$
C^2=-\frac{4mn}{p^2}AB.\tag{6}
$$
$F_r\cdot F_\theta$ 的 $p$ 模为 $-p z'_0C\sin(p\theta)$，所以 $z'_0=0$。同一张量的 $2p$ 模给
$$
m A'B+nAB'+\frac p2 CC'=0.\tag{7}
$$
用 (6) 的导数代入 (7)，由于 $m\ne n$，得到
$$
mA'B-nAB'=0.\tag{8}
$$
在 $A,B$ 不变号区间，令 $A=a\rho^n$，则 $B=b\rho^m$，而 (6) 给
$$
C=c\rho^p,\quad c^2=-\frac{4mn}{p^2}ab,
\quad ab<0.\tag{9}
$$
$F_r^2$ 的 $2p$ 模为 $2A'B'+C'^2/2$，由 (9) 自动为零。因此 (9) 连同常数 $z_0$ 是 (5) 的完整非退化精确解，并非仅有限模线性解。

全部平均度量变为
$$
F_r^2=(nA-mB)^2(\rho'/\rho)^2,
\qquad F_\theta^2=(nA-mB)^2,
\qquad F_r\cdot F_\theta=0.\tag{10}
$$
取 $u=\log\rho$ 后得到共形参数。各 Cartesian 分量分别是 $e^{nu}\cos n\theta$、$e^{mu}\cos m\theta$、$e^{pu}\cos p\theta$ 及其正弦，故
$$
F_{uu}+F_{\theta\theta}=0.
$$
结合 (10) 可直接推出该非退化解是极小曲面。$n=1,m=3$ 是 Enneper 型实例。这里的推导解释了为何该最短有限 ansatz 虽有精确非旋转周期环带，却不给固定旋转领圈：$B=b\rho^m$ 与 $C=c\rho^p$ 在正半径处不会独立消失，且不能加入变化的平均高度 $z_0$。

本题仍允许更丰富的有限 ansatz，例如至少两个竖直非零模、更多横向频率以及角相位随 $r$ 的变化。以上计算不排除它们；但不应重复把 (5) 当成新的非极小闭合机制。


## 4. 精确相位作用的接口与范围

若 (1) 成立，令 $\tau_t(r,\theta)=(r,\theta+t)$。由于 $g$ 的各分量与角变量无关，$\tau_t^*g=g$，故对任何轴旋转 $R_t$，
$$
F_t=R_{-t}\circ F\circ\tau_t
$$
均对同一 $g$ 精确等距。若某开领圈上 $F(r,\theta)=R_\theta F(r,0)$，则该领圈在所有 $t$ 下逐点固定。$F\in C^2$ 保证 $t\mapsto F_t$ 在紧子带上的 $C^2$ 拓扑连续；每个相位的浸入性、单射性由 $R_t$ 和 $\tau_t$ 的可逆性保持。

这只对单条带给相位族。单带的像满足 $F_t(I\times S^1)=R_{-t}F(I\times S^1)$，所以不能由它单独声称 $\delta_E>0$。本题仍需两模块相对相位、精确固定开领圈、闭合以及全部定量几何条件。
