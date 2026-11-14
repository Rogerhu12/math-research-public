# R85：临界周期零点恰为全部真实同源邻点

日期：2026-11-12。状态：Gauss 界、实际晶体标记、Newton 多边形、域与微分均已根端独审。
完整证明及原始来源见[临界周期映射与典范 CM 邻点](../notes/2026-11-12-critical-gauss-period-map-and-canonical-neighbors.md)。

固定惰性 $p\ge7$，$t=\lambda-1/2$，$s=1-4t^2$，
$Y=\left(\begin{smallmatrix}K&L\\K'&L'\end{smallmatrix}\right)$、
$\det Y=1/s$、$J=L/t$、$u=L/K$。
取 $\varpi^{p+1}=p$、$\rho=|\varpi|$，
$\kappa=p[t^{p+1}]K\bmod p\ne0$。

## 1. 闭临界圆上的准确约化

全部周期系数的赋值界给

$$
\overline{K(\varpi X)}=1+\kappa X^{p+1},\qquad
\overline{J(\varpi X)}=1,\qquad
\overline{u(\varpi X)/\varpi}
=\frac{X}{1+\kappa X^{p+1}}.
$$

因此闭 $\rho$ 盘恰有 $p+1$ 个 $K$ 的简单零点，全部在边界。
对单位 $U$，$u(t)=\varpi U$ 也恰有 $p+1$ 个互异边界解；
其约化多项式为
$X^{p+1}-(\kappa U)^{-1}X+\kappa^{-1}$。
根的幂和 $S_1,\ldots,S_p$ 为零，$S_{p+1}=-\kappa^{-1}$。
这只是临界分支的低层迹，不能省略后续精度。

## 2. 由真实同源证明零点的身份

在原典范 CM 纤维，对每个阶 $p$ 子群 $H$ 取 Serre 商，
运输全部级结构，并选约化为实际 Frobenius 的坐标符号。
晶体函子性和水平平凡化使全部分支的水平矩阵准确同为

$$
F_0=\begin{pmatrix}0&pa\\b&0\end{pmatrix},\qquad ab=-1.
$$

同源保持 Hodge 线，因而其目标参数 $t_H$ 满足
$K(t_H)=0$，微分因子为 $c_H=bL(t_H)$。
独立计算源及目标 $p$ 挠点的赋值，目标 Newton 多边形顶点为

$$
(1,1),\quad (p,1/(p+1)),\quad(p^2,0).
$$

Legendre 的简单 Hasse 零点遂给
$v_p(t_H)=v_p(c_H)=1/(p+1)$。
Galois 轨道及赋值分母给 $p+1$ 个互异参数，故

$$
\{t_H:H\subset E[p],\ |H|=p\}
=\{t:|t|\le\rho, K(t)=0\}.
$$

令 $B$ 为含实际级结构及 $\mathbb F_{p^2}$ 的有限非分歧基域。
约化根属于 $\mathbb F_{p^2}$，Hensel 与赋值分母共同给

$$
B(t_H)=B(\varpi).
$$

这些参数是同一个次数 $p+1$ 的驯分歧循环域中的完整轨道。
全部挠点坐标可能需要更大的域；目标局部 CM 阶准确为
$\mathbb Z_p+p\mathcal O_{\mathbb Q_{p^2}}$。

## 3. 邻近源的完整微分运输

对源 $t$ 和同一真实分支 $t_j$，

$$
M_j=Y(t_j)F_0Y(t)^{-1},\qquad
u(t_j)u(t)=pa/b,
$$
$$
c_j=\frac{bL(t_j)}{K(t)}
=\frac{paK(t_j)}{L(t)},\qquad
\frac{dt_j}{dt}=\frac{s(t_j)}{s(t)}\frac{c_j^2}{p}.
$$

这将实际同源分支、临界周期映射和微分权重逐项接合。
$K M_e$ 在这些零点为零不表示 $M_e$ 为零，
也还未证明控制 $\Sha$ 的指定中央导数非零。
