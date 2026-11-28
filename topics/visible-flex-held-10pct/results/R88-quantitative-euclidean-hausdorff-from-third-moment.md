# R88 — 从三阶中心矩到完整欧氏群的定量 Hausdorff 下界

会话：Astra-held10-7c4e33ee-20261128。状态：**已证明**。

对 [R82/R84 原标记族](R84-actual-endpoint-third-tensor-separation.md)，以及 [R86 完整圆盘新标记族](R86-full-disk-marker-with-unchanged-geometry-budget.md)，现在把指定端点的三阶张量差转成包含全部平移、旋转和反射的明确距离下界：

| 实际族 | 端点最小对齐表面 Hausdorff 距离 | 全族 $\delta_E/D$ |
|---|---:|---:|
| R82/R84 canonical 帽 | $>4\times10^{-23}$ | $>5/(3\times10^{23})$ |
| R86 完整圆盘新帽 | $>2\times10^{-18}$ | $>5/(6\times10^{18})$ |

这些是保守的、严格的**下界**，不是实际最优对齐距离或已达到的最大比例。R86 的准确51200倍张量增益不会被冒充成 Hausdorff 距离的倍数。这里也没有重算 R83 的积分。

## 1. 本条所用实际前提

记所选同一族的两个端点闭面为 $S_0,S_1$，有界内部为 $\Omega_0,\Omega_1$。R82 或 R86 已分别付清每个完整闭面的 C² 嵌入性、球面拓扑以及外法向正支撑界。两族都有同一组更强的实际界，因而都满足以下简化有理预算：
$$
|X|\le R:=\frac65,\qquad X\cdot n\ge\sigma:=\frac35.
$$
所有点都在同一原点坐标中。上式没有使用尚未付清的全尾度量、完整 DN 收敛或准确 $\lambda=1$ 输入。

R84 的准确三重旋转及 $z$ 反射、R86 对这两项对称的保持，说明每个体积的质心准确为零。因此
$$
T_i=\int_{\Omega_i}x^{\otimes3}\,dx,\qquad I_i=\|T_i\|_F^2
$$
就是中心体积矩及其欧氏不变量。张量范数是全部27个有序分量的 Frobenius 范数。

令
$$
d_E(S_0,S_1)=\inf_{Q\in O(3),\,a\in\mathbb R^3}
d_H(S_0,Q S_1+a).
$$
下面证明一般估计
$$
d_E(S_0,S_1)\ge
\min\left\{\frac1{100},\frac{|I_0-I_1|}{16640}\right\}.
\tag{1}
$$
其中 $d_H$ 明确作用于两个**表面集合**，不是只比较体积或凸包。

## 2. 用凸包支撑函数控制任意平移

对任一紧凸集 $K$，定义
$$
s(K)=\frac3{4\pi}\int_{\mathbb S^2}u\,h_K(u)\,d\omega(u),
\qquad h_K(u)=\max_{x\in K}x\cdot u.
$$
这里直接使用该积分定义，不另假设原体积凸。由球面的旋转不变测度，
$s(QK)=Qs(K)$ 对每个 $Q\in O(3)$ 成立。由
$$
\int_{\mathbb S^2}uu^\top\,d\omega=\frac{4\pi}3 I
$$
又有 $s(K+a)=s(K)+a$。

$S_i$ 的凸包同时被非平凡三重旋转和 $z$ 反射保持，所以 $s(\operatorname{conv}S_i)$ 也被这两变换固定。三重旋转的不动空间是竖轴，$z$ 反射再消去该轴，故两个积分点都准确为零。这与质心为零是两个分别由对称性得出的结论，并未假设任意物体的质心等于此积分点。

固定任意 $Q,a$，令
$$
S'=QS_1+a,\qquad d=d_H(S_0,S').
$$
表面 Hausdorff 界直接给
$$
|h_{\operatorname{conv}S_0}(u)
-h_{\operatorname{conv}S'}(u)|\le d
\quad(u\in\mathbb S^2).
$$
于是
$$
|a|
=\left|s(\operatorname{conv}S')-s(\operatorname{conv}S_0)\right|
\le\frac3{4\pi}\int_{\mathbb S^2}d\,d\omega
=3d.
\tag{2}
$$
这一步允许全部 $O(3)$，没有预先固定平移、轴线、反射或最佳对齐参数。

## 3. 小表面距离给体积对称差的线性界

先设 $d\le1/100$。已证正支撑球面是以原点为中心的径向图，且其每条径向半径至少为 $\sigma$，所以 $\Omega_1$ 包含 $B_\sigma(0)$。因此
$\Omega'=Q\Omega_1+a$ 包含 $B_\sigma(a)$；由 $|a|\le3/100<\sigma$，原点仍在 $\Omega'$ 内部。

在 $S'$ 上，变换后的外法向满足
$$
x\cdot n'=y\cdot n+(a\cdot Qn)
\ge\sigma-|a|>0,\qquad x=Qy+a.
$$
故它也为相对于原点的正径向图。具体地，沿射线每次穿过边界都因正支撑而从内向外穿出，不能出现第二次穿入；结合原点在内部、边界紧致和径向导数非零，得到唯一光滑径向函数。记两者为 $\rho_0,\rho'$。其统一上界为
$$
\rho_0,\rho'\le R+3d\le\frac{123}{100}<\frac54=:M.
\tag{3}
$$

对原图 $x=\rho_0(u)u$，外单位法向的标准表达式可直接由两个切导数的正交性得到：
$$
n=\frac{\rho_0u-\nabla_{\mathbb S^2}\rho_0}
{\sqrt{\rho_0^2+|\nabla_{\mathbb S^2}\rho_0|^2}}.
$$
所以
$$
x\cdot n
=\frac{\rho_0^2}{\sqrt{\rho_0^2+|\nabla\rho_0|^2}}
\ge\sigma
\quad\Longrightarrow\quad
|\nabla_{\mathbb S^2}\rho_0|\le\frac{R^2}{\sigma}=\frac{12}5.
\tag{4}
$$

给定 $u$，取 $y=\rho'(u)u\in S'$。表面 Hausdorff 界提供
$x=\rho_0(v)v\in S_0$，使 $|x-y|\le d$。由反三角不等式和 $|x|\ge\sigma$，
$$
\big||x|-|y|\big|\le d,\qquad
|u-v|\le\frac{2d}{|x|}\le\frac{10}3d.
$$
单位球面测地距离满足
$\operatorname{dist}_{\mathbb S^2}(u,v)\le(\pi/2)|u-v|$。沿最短大圆积分(4)，得到
$$
|\rho'(u)-\rho_0(u)|
\le d+\frac{12}5\,\frac{5\pi}3d
=(1+4\pi)d<14d.
\tag{5}
$$
这里并未假设最近点沿同一条射线。

两个体积都是同原点的径向体，故(3)—(5)给
$$
\begin{aligned}
\operatorname{Vol}(\Omega_0\mathbin{\triangle}\Omega')
&=\frac13\int_{\mathbb S^2}|\rho_0^3-(\rho')^3|\,d\omega\\
&\le M^2\int_{\mathbb S^2}|\rho_0-\rho'|\,d\omega\\
&<\frac{25}{16}\,4\pi\,14\,d
<275d.
\end{aligned}
\tag{6}
$$
最后使用 $\pi<22/7$。这是真实非凸体积的对称差控制，不是以凸包体积差代替它。

## 4. 中心三阶张量的差

原两个体积包含在 $B_R(0)$，所以
$$
\operatorname{Vol}(\Omega_i)\le V:=\frac{4\pi}3R^3
<\frac{19008}{2625},
\qquad
\|T_i\|_F\le VR^3<13.
\tag{7}
$$
秩一张量的 Frobenius 范数为
$\|x^{\otimes3}\|_F=|x|^3$。

在 $\Omega'$ 中，中心化的变换张量是
$$
Q^{\otimes3}T_1=\int_{\Omega'}(x-a)^{\otimes3}\,dx.
$$
先在同一原点比较两个积分域，再付真实平移项：
$$
\begin{aligned}
\|T_0-Q^{\otimes3}T_1\|_F
\le&
\left\|\int_{\Omega_0}x^{\otimes3}\,dx
-\int_{\Omega'}x^{\otimes3}\,dx\right\|_F\\
&+\int_{\Omega'}\|x^{\otimes3}-(x-a)^{\otimes3}\|_F\,dx.
\end{aligned}
$$
第一项由(3)、(6)小于 $M^3\,275d$。第二项使用逐因子相减的三项恒等式；因 $|x|,|x-a|\le M$，
$$
\|x^{\otimes3}-(x-a)^{\otimes3}\|_F\le3M^2|a|.
$$
结合(2)、(7)，第二项小于
$$
9M^2\frac{19008}{2625}d<102d.
$$
因此
$$
\|T_0-Q^{\otimes3}T_1\|_F
<\left(\frac{125}{64}\,275+102\right)d<640d.
\tag{8}
$$

$Q^{\otimes3}$ 是 Frobenius 等距，故
$$
|I_0-I_1|
\le(\|T_0\|_F+\|T_1\|_F)
  \|T_0-Q^{\otimes3}T_1\|_F
<16640d
\tag{9}
$$
对 $0<d\le1/100$ 成立。若 $d=0$，两嵌入闭面及其有界内部在此欧氏变换下相同，直接有 $I_0=I_1$。若 $d>1/100$，则已得到(1)需要的另一项。故对每个 $Q,a$ 都有(1)的右端下界，取下确界即证(1)，不要求最优刚体变换先存在。

## 5. 两个实际族的严格数值后果

R84 已对实际准确参数证明
$$
\Delta I_{\rm old}=I_3(0)-I_3(9/20)>\frac7{10^{19}}.
$$
而
$$
16640\,\frac4{10^{23}}<\frac7{10^{19}}.
$$
由(1)，原指定端点满足 $d_E>4\times10^{-23}$。

R86 则已对其新的准确 Fraction 双帽证明
$$
\Delta I_{\rm new}>\frac{359}{10^{16}},\qquad
16640\,\frac2{10^{18}}<\frac{359}{10^{16}}.
$$
所以新指定端点满足 $d_E>2\times10^{-18}$。两者的角端点都是实际声明的 $0$ 与 $9/20$，不是尚未确定的存在性相位。

全族 $\delta_E$ 至少是这对端点相对于初始面的最小对齐距离；共同实际直径界又严格小于 $2R=12/5$。因此得到开头表中的归一化下界。若随后对曲面逐时作刚体重握持，这些完整欧氏不变量与最小对齐距离保持不变。

本条的估计相当保守，不能据此判断实际变形幅度小、最优比值已求出、R86 的真实距离为旧场的51200倍，或任何其他尚未做的配准结果。

## 6. 精确标量执行及复现

小入口 [centered_moment_hausdorff_bound.py](../scripts/resume_20261128/analytic/centered_moment_hausdorff_bound.py) 读取已发布 R82、R84、R86 小记录，核同实际query/geometry/bundle及两族几何预算，用 Fraction 实算(2)—(9)所有常数和两组下界。实际执行记录见 [2026-11-28-quantitative-euclidean-hausdorff.json](../notes/2026-11-28-quantitative-euclidean-hausdorff.json)，包含源及输入SHA-256。

复现命令在课题目录下为：

~~~bash
python scripts/resume_20261128/analytic/centered_moment_hausdorff_bound.py \
  --out /tmp/held10-r88-quantitative-hausdorff.json
~~~

程序核的是本条几何证明的准确标量后果与真实来源，未进行网格配准、重积分或新的BVP。它没有把原记录的历史“尚无定量Hausdorff界”改成当时已经有本结论；新证明单独登记。准确 $\lambda=1$、10% 握持、整尾连续metric、最终physical-H和固定完整问题精化仍继续。
