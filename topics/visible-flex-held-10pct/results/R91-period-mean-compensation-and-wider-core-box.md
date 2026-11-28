# R91. 用扇区总曲率约束补偿量，扩大 R87 原支持控制盒

2026-11-28；`analytic_construction`。

**本条将 R87 核心层的充分输入条件从加权支持系数和 $A\le2/3$ 扩大为
$A\le8/9$。** 对原 R53 精确材料曲率圆化定义、R87 的
$k=1/2,S=27/40,b=3/10$，整个 $0\le\lambda\le1$ 满足

$$
\boxed{\frac12\le\kappa_\lambda(u)<\frac{3723}{314}
<\frac{123}{10},\qquad
\frac{123}{10}-\frac{3723}{314}=\frac{348}{785}>0.}
\tag{1}
$$

改进使用每扇区的完整总曲率，而不再把保护窗内每个点的旧曲率都估成同一个最大值。
这没有改变 R53 核心、R87 的物理 profile、窗口或目标曲率，也没有改任何实际 BVP 门。
它不是完整曲面的曲率、reach、握持、非线性 DN 或固定 g 精化结论。

## 1. 精确对象和扩大后的原支持盒

沿 [R53](R53-material-flattening-homotopy-and-positive-domain.md) 的同一个三重、反射对称原支持核心，写

$$
h(\phi)=1+\sum_{j\ge1}a_j\cos(3j\phi),\qquad
A=\sum_{j\ge1}(9j^2-1)|a_j|\le\frac89.
\tag{2}
$$

实际有限模式是其特例；若使用无限和，须有足以定义原曲率和 R53 正则性的相应收敛。
这里 $\phi$ 为法向角，$u$ 为原材料弧长，不能交换两者的积分。
原曲率半径

$$
\rho_0=h+h''=1-\sum_{j\ge1}(9j^2-1)a_j\cos(3j\phi)
$$

有全角界

$$
\frac19\le\rho_0\le\frac{17}{9},\qquad
\frac9{17}\le\kappa_0=\rho_0^{-1}\le9.
\tag{3}
$$

令 $T=2\pi/3$、$L=T/2$。归一化常数项为1，故每个法向扇区的材料长度也是 $T$；
由 $du=\rho_0\,d\phi$，精确地

$$
\int_0^T\kappa_0(u)\,du=T.
\tag{4}
$$

这正是 R53 的 $\phi_0(u+T)=\phi_0(u)+T$，不是有限角采样或求积近似。

## 2. 同一窗口和总曲率给出的补偿上界

保留 [R87](R87-single-gentle-ramp-half-curvature-held-window.md) 的精确参数

$$
k=\frac12,\qquad S=\frac{27}{40},\qquad b=\frac3{10}.
$$

其中 `curvature_blend=1`，所以 $k$ 是这个固定常数。
R53 原窗口满足 $0\le W\le1$，令 $\chi=1-W$，并有

$$
J=\int_0^T\chi(u)\,du=2S+b=\frac{33}{20},\qquad
S+b=\frac{39}{40}<\frac\pi3.
\tag{5}
$$

原定义的补偿为

$$
\beta=\frac{\int_0^T\chi(u)(\kappa_0(u)-k)\,du}{T-J}.
\tag{6}
$$

由 (3)，$\kappa_0-k\ge 9/17-1/2=1/34>0$，故 $\beta\ge0$。
另一方面，$0\le\chi\le1$、$\kappa_0>0$ 和 (4) 给

$$
\int_0^T\chi\kappa_0\,du\le T,
\qquad
\boxed{0\le\beta\le\frac{T-kJ}{T-J}.}
\tag{7}
$$

对固定 $J>0$、$k=1/2$，右侧写成
$1+(1-k)J/(T-J)$，在 $T>J$ 上严格递减。
用精确夹逼 $\pi>333/106$，有 $T>111/53>J$，因而

$$
\beta<
\frac{111/53-(1/2)(33/20)}{111/53-33/20}
=\frac{897}{314}.
\tag{8}
$$

这里严格性已由 $T>111/53$ 支付，不需假设旧曲率在某个网格点达到极值。
窗口可容纳的有理余量为
$111/106-39/40=153/2120>0$，补偿分母的有理下界为
$111/53-33/20=471/1060>0$。

## 3. 全部同伦参数上的核心曲率

保留 R53 原公式

$$
\kappa_\lambda
=(1-\lambda)\kappa_0
+\lambda\{\chi k+W(\kappa_0+\beta)\}.
\tag{9}
$$

因为 $\chi+W=1$，各混合权重均非负，(3)、$\beta\ge0$ 给
$\kappa_\lambda\ge k=1/2$。同样，

$$
\kappa_\lambda\le9+\beta<9+\frac{897}{314}
=\frac{3723}{314}.
$$

这证明 (1)，并保留 R53 的严格凸性、旋转闭合、完整材料参数变分及精确总长定义。
在 $\lambda=1$ 的保护弧仍准确为
$\Gamma(L+x)=O+2e^{i(L+x/2)}$；没有更改 R87 的握持扫窗。
低于 $\lambda=1$ 时，本条仍不把曲率插值误称为准确圆弧。

## 4. 与实际源码和数值范围的关系

`resume_transfer/material_flattened_support_core.py` 的 `_window` 使用同一
九次 step，导数为 $630t^4(1-t)^4$，积分为 $1/2$；
`_beta_all` 由右半扇区加权积分除以 $L-S-b/2$ 得到，反射对称后正是 (6)。
`_phase_fields` 实施 (9) 的等价形式，`_set_curvature_guard` 保留原混合界。
这些已绑定源均未修改。

本条验证的是 R53 的**精确定义**。具体 binary64 的 $S,b$、有限 Gauss 积分、
实际完整支持参数及后续曲面仍须由自身误差和来源合同验收；不能把有理标量证书
直接贴到任意有限实现上。特别是，旧已接受场不因本条自动获得新几何证书，
离开 $A\le8/9$ 的新参数也不能仅凭本条放行。

扩大的是 R87 第1节的核心输入充分条件；其余完整非圆前缀、桥、真正非线性尾、
全图 C² 接合、物理 mean、固定最终 g 精化、完整几何及 held 前提均保持原状。

## 5. 精确小证书

独立入口
`scripts/resume_20261128/analytic/certify_core_mean_compensation_box.py`
只用 `Fraction`。它核原窗口多项式的积分、上述有理界与严格余量，并绑定原定义来源 SHA。
其中 $\pi>333/106$ 还由 Machin 恒等式
$\pi=16\arctan(1/5)-4\arctan(1/239)$ 的四项交错下界直接核验；
没有把浮点 `pi` 充当精确输入。

实际执行状态与完整分数记录见
`../notes/2026-11-28-analytic-core-mean-compensation-box.json`。
没有重算任何旧字段、完整 Jacobian、BVP 或尾响应。
