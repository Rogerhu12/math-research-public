# R60：实际外头 cell11 的完整 mean 导数与连续 Darboux 缺陷界

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**已证明，含实际 cell11 的全角全径向区间账本。** 本结果认证一个明确兼容候选的完整残差上界，不宣称外头精确解已经存在。 本文在
[R44](R44-compatible-outer-height-and-continuous-defect.md) 的同一个兼容高度上，
用准确连接平均恒等式恢复 mean 径向导数。计算不把候选的径向导数替换成 ODE 右端，
不截断完整 mean，也不删去有理非线性源生成的高频。
它给候选的真实连续残差上界；非零的上界本身不证明候选已经是等距面。

## 1. 对象、正分支与范数

在一个真实 source 光滑片上，令 $r_x>0$、$0<w\le1/2$，并记

$$
s=\frac{r_x}{r},\qquad \ell=\frac{w_x}{w},\qquad z=w^2,
\qquad E=1+z.
$$

取 [R48](R48-weighted-compatible-outer-interpolation.md) 的同一个非均值高度
$\widehat h_\perp$，即其端点、四个 Hermite 项、正权 bubble 及五个积分均来自同一个
真实背景和同一组实际积分。定义

$$
P=\frac{\widehat h_{\perp,\theta}}{rw},\qquad
\bar K=\frac{\widehat h_{\perp,r}}{w},\qquad
K=c+\bar K,\qquad T=P_\theta,
$$

其中 $c$ 是 [R33 第 2 节](R33-full-head-forcing-on-a-variable-analytic-strip.md)
的**完整**连接 mean 小根。特别地，$\bar K_x$ 是这个高度的实际导数。
第一行兼容式精确成立：

$$
P_x=sK_\theta-(s+\ell)P.
\tag{60.1}
$$

下文固定 $\tau\ge0$。对一个真实径向面板 $I$，使用

$$
\|f\|_{\tau,1;I}
=\sum_{m\in\mathbb Z}(1+|m|)e^{\tau|m|}
\sup_{x\in I}|f_m(x)|.
\tag{60.2}
$$

这是先逐模取径向 supremum 再求和的范数。它具有乘法代数性质，
去 mean 投影范数不超过一，mean 的绝对值也不超过此范数。
证明只使用
$(1+|a+b|)e^{\tau|a+b|}\le(1+|a|)(1+|b|)e^{\tau|a|+\tau|b|}$
和卷积三角不等式，因此包含全部输出频率。

设有严格包络

$$
p_*\ge\|P\|_{\tau,1;I},\quad
k_*\ge\|\bar K\|_{\tau,1;I},\quad
k_{x,*}\ge\|\bar K_x\|_{\tau,1;I},\qquad
R_*=p_*+k_*<\frac1{32}.
$$

R33 的全纯小根定理给同一 mean 函数满足

$$
|c(x)|\le c_*:=4R_*^2\qquad(x\in I).
\tag{60.3}
$$

这不是用有限角采样或有限投影近似求出的 mean。
固定宽度的范数上界只使该定理的输入更强。
在每个光滑片上，由小根的隐函数定理，$c$ 随同一个候选光滑变化。
在原 source 接口处，若背景与候选满足 R44 所列连续两阶接缝条件，
由小根唯一性及下面正分母公式得到同一 mean 的两侧连续导数；不能逐片另选 mean。

记

$$
L=1+K+ET,\qquad
D=1-z(2K+K^2+EP^2),\qquad U=K_\theta-P.
\tag{60.4}
$$

令 $\lambda_*\ge\|\bar K+ET\|_{\tau,1;I}$，并要求

$$
a_L:=1-c_*-\lambda_*>0.
\tag{60.5}
$$

于是 $L$ 在真实角上严格为正，且完整 Wiener 逆满足
$\|L^{-1}\|_{\tau,1;I}\le a_L^{-1}$。
取 $z_*\ge\sup_I z$、$E_*\ge\sup_I E$，令

$$
\kappa_*=k_*+c_*,\qquad
u_*=z_*(2\kappa_*+\kappa_*^2+E_*p_*^2)<1.
\tag{60.6}
$$

则 $D\in[1-u_*,1+u_*]$，其正平方根分支和 $D^{-3/2}$ 的完整 Wiener
展开均有效。所有分母门都是连续面板上的门。

## 2. 完整非均值残差与 mean 的准确恢复

定义完整有理源

$$
N(P,K)=\frac{EsU^2+\ell\{(K+T)^2+z(2KT+T^2-P^2)\}}{L}
\tag{60.7}
$$

及实际非均值第二行残差

$$
R_\perp=\bar K_x+\ell(2\bar K+T)-\Pi_\perp N(P,K).
\tag{60.8}
$$

其中 $\Pi_\perp$ 保留**全部**非零频率。
有限线性部分确实由已定义高度的实际导数计算；$N$ 使用完整 $c$ 与完整 $L^{-1}$。
由 R44 的恒等式，

$$
\frac{\mathcal J}{L}=c_x+\bar K_x+\ell(2c+2\bar K+T)-N
=a+R_\perp,
\qquad
a=c_x+2\ell c-\langle N\rangle.
\tag{60.9}
$$

R44 证明，(60.1) 与完整 mean 根恰给

$$
\left\langle\frac{\mathcal J}{D^{3/2}}\right\rangle=0.
\tag{60.10}
$$

置 $W=LD^{-3/2}$。由于 $\langle R_\perp\rangle=0$，(60.9)–(60.10) 得到

$$
\boxed{
a=-\frac{\langle(W-1)R_\perp\rangle}{\langle W\rangle},
\qquad
c_x=a-2\ell c+\langle N\rangle.
}
\tag{60.11}
$$

这就是本工具的完整 mean 导数公式。它没有另设 mean 边界条件，
没有假设候选已经满足第二行方程，也没有把 $c_x$ 置零。
相反，非零的实际残差通过准确正权影响 mean 导数。

## 3. 可计算的完整范数上界

再取

$$
t_*\ge\|T\|_{\tau,1;I},\quad
v_*\ge\|U\|_{\tau,1;I},\quad
b_*\ge\|\bar K_x+\ell(2\bar K+T)\|_{\tau,1;I},
$$

以及 $s_*\ge\sup_I s$、$\ell_*\ge\sup_I|\ell|$。
若有限 Fourier 端点固定，则 $t_*,v_*,b_*$ 可以直接对实际有限系数取区间上界，
保留线性项内部的抵消，而不先将三个范数分开。
乘法代数与 (60.5) 给

$$
n_*=\frac{E_*s_*v_*^2+\ell_*\{(\kappa_*+t_*)^2+
 z_*(2\kappa_*t_*+t_*^2+p_*^2)\}}{a_L},
\qquad
r_*=b_*+n_*.
\tag{60.12}
$$

于是 $\|N\|_{\tau,1;I}\le n_*$、
$\|R_\perp\|_{\tau,1;I}\le r_*$。
第一项中的 $K_\theta$ 没有 mean 贡献；第二项的 $\kappa_*$ 已保留完整 mean。
对 $D^{-3/2}$ 的正系数二项展开给

$$
F_*=(1-u_*)^{-3/2},\qquad
w_*=(c_*+\lambda_*)F_*+(F_*-1)
\ge\|W-1\|_{\tau,1;I}.
\tag{60.13}
$$

另一方面，真实角上 $L\ge a_L$、$D\le1+u_*$，故

$$
\langle W\rangle\ge m_*:=\frac{a_L}{(1+u_*)^{3/2}}>0.
\tag{60.14}
$$

代入 (60.11)，得到

$$
|a|\le a_*:=\frac{w_*r_*}{m_*},\qquad
|c_x|\le c_{x,*}:=a_*+2\ell_*c_*+n_*,
$$

$$
\boxed{\quad
\|\mathcal J\|_{\tau,1;I}
\le (1+c_*+\lambda_*)(r_*+a_*).
\quad}
\tag{60.15}
$$

所有上界均适用于整个真实面板。$N$ 与 $R_\perp$ 可以具有无穷频谱；
上述估计不需要先截断它们。由于候选非均值高度本身只有有限频率，
R44 的原多项式 $\mathcal J$ 仍只有至多双倍最高频率，
这里通过准确有理恒等式为它给界。

## 4. 物理缺陷、实际二阶导数与认证范围

R44 给实际内蕴 Darboux 缺陷

$$
\mathscr D(\widehat h)=\frac{w^2}{r r_x E^2}\mathcal J.
$$

因此

$$
\sup_{I,\theta}|\mathscr D(\widehat h)|
\le \left(\sup_I\frac{w^2}{r r_x E^2}\right)
 (1+c_*+\lambda_*)(r_*+a_*).
\tag{60.16}
$$

第二行物理非均值源残差及候选二阶导数同时满足

$$
\left\|\frac{w}{r_x}R_\perp\right\|_{\tau,1;I}
\le\left(\sup_I\frac{w}{r_x}\right)r_*,
$$

$$
\|\widehat h_{\perp,rr}\|_{\tau,1;I}
\le\left(\sup_I\frac{w}{r_x}\right)(k_{x,*}+\ell_*k_*),
$$

$$
|\widehat h_{0,rr}-w_r|
\le\left(\sup_I\frac{w}{r_x}\right)(c_{x,*}+\ell_*c_*).
\tag{60.17}
$$

这里 $\widehat h_0$ 是统一积分 $w(1+c)$ 得到的真实 mean 高度。
这些量具有不同归一化，不能拿很小的 $\mathscr D$ 直接当成很小的解析 Green 源：
在极小 $w$ 处，两者的几何因子差异很大。
本结果也不把非零缺陷高度的 Hessian 借称为某个已存在等距嵌入的第二基本形式。
要得到精确面，仍需在实际外头完整边值问题中支付残差响应与收缩门，
并与 node12 的**全部**真实连接迹接合。

## 5. 实现身份与实际执行

[完整 mean 残差辅助函数](../computations/tail_outer_full_mean_residual_bounds.py)
逐面板实现 (60.3)–(60.17)。
[只读残差 adapter](../computations/tail_outer_candidate_defect.py)
只向已经实际执行的
[候选连续域扫描](../computations/tail_outer_candidate_domain.py)
加入该辅助函数和输出记录。
它首先检查域扫描源 SHA，再逐个检查唯一插入锚点；移除全部插入后，
必须逐字恢复原域扫描源码。因此候选、端点、真实五积分、同一源函数及原有门均保持。
每个输出同时记录原域扫描及新两个辅助文件 SHA。

cell11 的输入是完整强 M20 已存 response 的两个真实端点、同源 13port 完整 Q/L、
9 个 source 段的 5545 个实际正权积分面板，以及同一个 R26 背景。
旧 partial 积分记录中，42 个区间的浮点球表示下端略小于零；
原记录完整保留，评估仅用已证明的非负真实积分域与该区间相交后的外包。
这没有修改五个真实积分，亦没有按面板另选不同候选。

当前执行使用固定 $\tau=1/64$、192 bit Arb、显式端点逆多项式次数 8、
120 MiB 监测门；端点二阶 jet 是该有限多项式所**定义**的候选数据，
不是未知精确径向解的二阶 jet。
完整执行 session `23908` 正式退出码为 0：42.395 秒，峰 RSS 32052 KiB。
三个原始域门全为真。新输出与此前 session `57646` 的 cell、5545 面板、角宽、
全部模式、端点定义、bubble 系数、原域极值、分段极值、门、leading 下界及完整输入
SHA 字段逐字相同；增加残差计算没有改动候选。

向上留有余量的简明界为

| 同一个实际候选上的量 | 全 cell11、全角上界 |
|---|---:|
| $\|P\|_{\tau,1}+\|\bar K\|_{\tau,1}$ | $3.429795\cdot10^{-18}$ |
| $|c|$ | $4.705397\cdot10^{-35}$ |
| $|c_x|$，各 source 段自身的 $x$ 坐标 | $8.963303\cdot10^{-34}$ |
| $\|R_\perp\|_{\tau,1}$ | $4.606415\cdot10^{-17}$ |
| $\|\mathcal J\|_{\tau,1}$ | $4.606415\cdot10^{-17}$ |
| $|\mathscr D(\widehat h)|$ | $7.845182\cdot10^{-25}$ |
| $\|(w/r_x)R_\perp\|_{\tau,1}$ | $9.406824\cdot10^{-22}$ |
| $\|\widehat h_{\perp,rr}\|_{\tau,1}$ | $4.703485\cdot10^{-22}$ |
| $|\widehat h_{0,rr}-w_r|$ | $6.017306\cdot10^{-42}$ |

$\mathcal J$ 的最坏已包围面板是 source 段 5、面板 10，
$x\in[618485199019/4398046511104,1305689461097/8796093022208]$。
物理 Darboux 缺陷及物理第二源的最坏已包围面板是 source 段 3、面板 0，
$x\in[0,1/16]$。这两个定位不同，具体体现了几何归一化不能被省略。
完整有理源的范数仅为 $2.240843\cdot10^{-34}$ 以下；当前 $R_\perp$ 界主要来自
实际线性候选残差，并非非线性源过大。

完整数据与实际资源：

- [原连续域](../notes/2026-11-12-tail-outer-cell11-candidate-domain-r1.json) 与
  [原正式资源](../notes/2026-11-12-tail-outer-cell11-candidate-domain-r1-resource.json)。
- [完整 mean/缺陷结果](../notes/2026-11-12-tail-outer-cell11-candidate-defect-r1.json) 与
  [正式资源](../notes/2026-11-12-tail-outer-cell11-candidate-defect-r1-resource.json)。
- [稳定源与数据清单](../notes/2026-11-12-tail-outer-cell11-candidate-executed-manifest.json)。

这只支付 cell11 的一个明确候选。cells0–10 的连续域/残差、完整径向 Green/Schur
响应、与 R58 新全频头的真正 node12 slope 及高频高度输出匹配仍分别需要支付。
固定 node12 的 M20 保存值定义了本候选；它不把旧有限 worker 的 Pi 自动升级成
R58 精确头的 Dirichlet-to-Neumann 值。

本文从已冻结的[完整证明执行笔记](../notes/2026-11-12-tail-outer-complete-mean-defect.md)精确转写，仅调整结果编号与相对链接。原源/数据清单及其 SHA 保持不变。
