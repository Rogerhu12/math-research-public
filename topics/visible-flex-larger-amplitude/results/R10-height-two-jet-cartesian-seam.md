# R10. 完整高度二 jet 与共同度量确定笛卡尔接缝二 jet

2026-11-10，geometric_amplification。**状态：已证明，条件接缝引理。** 本文不证明尾解存在、不消除无限尾残差，也不把小的采样高度误差自动升级成严格笛卡尔接缝证书。

## 1. 假设与结论

在一条连通 $C^1$ 正则接缝 $\Gamma$ 两侧，采用相同局部坐标 $u=(u^1,u^2)$。设

$$
F^{\pm}=(X^{\pm},Z^{\pm})\in\mathbb R^2\times\mathbb R
$$

为直到接缝的 $C^2$ 局部浸入。假定：

1. 两侧诱导同一个 $C^1$ 度量 $g$，或其 $g$ 与全部一阶导数在 $\Gamma$ 的迹相同；
2. 平面投影 $DX^{\pm}$ 在接缝处均可逆，并具有相同定向；
3. 在 $\Gamma$ 上，$Z^+$ 与 $Z^-$ 的**完整**零、一、二 jet 相同，即 $Z$、$Z_i$、$Z_{ij}$ 全部相同，包括横向和混合导数。

**定理 1.** 存在一个与接缝点无关的平面保向刚体运动 $x\mapsto Qx+b$，使

$$
j^2_\Gamma X^+=j^2_\Gamma(QX^-+b). \tag{1}
$$

这个运动由任意一个接缝点的平面位置与框架对齐唯一确定。若位置和框架在一点已经对齐，则 $Q=I,b=0$，两侧全部笛卡尔二 jet 沿整条接缝相同。因此，在共同接缝坐标下把这两个已有片接起来，满足通常的分片 $C^2$ 匹配条件。

这里 $g\in C^1$ 足够，不需要 $g\in C^2$。若不要求同定向，结论中的 $Q$ 可属于 $O(2)$，即允许一个平面反射。

## 2. 证明：投影度量与框架运输

令

$$
h_{ij}=g_{ij}-Z_iZ_j. \tag{2}
$$

由于 $DX$ 可逆，$h=(DX)^T DX$ 正定。又

$$
\partial_kh_{ij}
=\partial_kg_{ij}-Z_{ik}Z_j-Z_iZ_{jk}. \tag{3}
$$

因此共同 $C^1$ 度量与完整高度二 jet 精确给出两侧共同的 $h$ 及 $\partial h$ 的接缝迹。$h$ 是 $C^1$，其 Levi–Civita 系数

$$
\Gamma^k_{ij}(h)=\frac12h^{k\ell}
(\partial_i h_{j\ell}+\partial_j h_{i\ell}-\partial_\ell h_{ij}) \tag{4}
$$

连续，并且两侧在接缝相同。

先说明平面投影满足

$$
\boxed{X_{ij}=\sum_k\Gamma^k_{ij}(h)X_k.} \tag{5}
$$

因为 $X_1,X_2$ 构成 $\mathbb R^2$ 的基，可把 $X_{ij}$ 唯一写成
$C^k_{ij}X_k$。由混合偏导对称，$C^k_{ij}=C^k_{ji}$。对
$h_{ij}=X_i\cdot X_j$ 求一次导数并作 Koszul 组合，得到

$$
2C^k_{ij}h_{k\ell}
=\partial_i h_{j\ell}+\partial_j h_{i\ell}-\partial_\ell h_{ij}.
$$

于是 $C^k_{ij}=\Gamma^k_{ij}$，证明 (5)。这里只用了 $X\in C^2$ 和 $h\in C^1$；平面维数与参数维数相同，所以没有另一个未控制的法向二阶项。

取任意接缝参数弧 $u=\gamma(t)$。令 $E^{\pm}(t)=DX^{\pm}(\gamma(t))$，其第 $j$ 列为 $X_j^{\pm}$。由 (5)，

$$
\frac{dE^{\pm}}{dt}=E^{\pm}A(t),\qquad
A^k{}_j(t)=\sum_i\Gamma^k_{ij}(h)(\gamma(t))\,\gamma_i'(t). \tag{6}
$$

系数矩阵 $A$ 连续，且两侧相同。取一点 $t_0$，定义

$$
Q=E^+(t_0)(E^-(t_0))^{-1},\qquad
b=X^+(\gamma(t_0))-QX^-(\gamma(t_0)). \tag{7}
$$

由于 $(E^+)^TE^+=(E^-)^TE^-=h$，直接计算得 $Q^TQ=I$；同定向再给 $\det Q=1$。连续系数线性 ODE 的初值唯一性应用于
$E^+-QE^-$，得到它沿这条接缝弧恒为零。随后

$$
\frac d{dt}(X^+-QX^--b)
=(E^+-QE^-)\gamma'=0
$$

且初值为零，所以位置也沿弧相同。再用 (5) 与共同的 $\Gamma(h)$，得到所有二阶偏导相同。

连通的一维正则接缝由相互重叠的参数弧连接，故这个相同的 $Q,b$ 传播到整条接缝。闭接缝的情形也如此：这里已经假设两侧实际投影存在，其框架与位置本来就是单值；证明不靠忽略 holonomy 或位置闭合残差来制造投影。结合已相同的 $Z$ 二 jet，即得 (1) 及完整笛卡尔二 jet 匹配。证毕。

## 3. 径向度量下的接缝角公式

对 $g=ds^2+a(s)^2d\theta^2$，在接缝上记

$$
E=1-Z_s^2,\qquad B=-Z_sZ_\theta,\qquad
G=a^2-Z_\theta^2,\qquad
\Delta=EG-B^2=a^2(1-Z_s^2)-Z_\theta^2>0. \tag{8}
$$

令 $e_\varphi=(\cos\varphi,\sin\varphi)$，
$e_\varphi^\perp=(-\sin\varphi,\cos\varphi)$。在固定投影定向 $\varepsilon\in\{\pm1\}$ 下，可写

$$
U=X_\theta=\sqrt G\,e_\varphi,
\qquad
V=X_s=\frac B{\sqrt G}e_\varphi
 +\varepsilon\frac{\sqrt\Delta}{\sqrt G}e_\varphi^\perp. \tag{9}
$$

这里 $\varepsilon=\operatorname{sign}\det(U,V)$，所以它是
$\operatorname{sign}\det(X_s,X_\theta)$ 的相反数。由 $U_s=V_\theta$ 的 $e_\varphi$ 分量，

$$
\varphi_\theta
=\frac{B_\theta-BG_\theta/(2G)-G_s/2}{\varepsilon\sqrt\Delta}
=\boxed{\frac{-aa_s-a^2Z_sZ_{\theta\theta}/G}
 {\varepsilon\sqrt\Delta}}. \tag{10}
$$

最后一个等式只需代入
$B_\theta=-Z_{s\theta}Z_\theta-Z_sZ_{\theta\theta}$、
$G_\theta=-2Z_\theta Z_{\theta\theta}$、
$G_s=2aa_s-2Z_\theta Z_{s\theta}$；混合导数项准确抵消。它与 root 的接缝重建公式相同。

对于由数值高度数据重新构造的候选，沿圆周积分 (10) 后仍须保留并检查角 holonomy 与 $\int U\,d\theta$ 的位置闭合量；不能把它们按周期强制抹零。即使这些圆周量很小，仍须检查 (8) 的正性、原高度数据对应的实际局部浸入、度量误差及全部笛卡尔 jet。

若高度用 Fourier 模式表示，完整二 jet 条件包含平均项 $\overline Z(s)$、$\overline Z'(s)$、$\overline Z''(s)$。非零角模式匹配不能替代它们。平均一阶项进入 (8) 和 (10)，平均二阶项进入 (3) 以及 $X_{ss}$ 的重建；平均零阶项则决定真实的竖直位置。最后，一点处的框架和位置对齐只允许使用同一个常数刚体运动，不能沿接缝逐点重新对齐。
