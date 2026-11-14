# R64：实际正侧 collar 的完整源与 DN 输入

2026-11-12，independent_audit。

**状态：已证明的实际有限正环带结论。** 本篇对当前准确仿射点
$\delta_4$，支付从其真实正转折到物理切口 $r=1/4$ 的完整正侧
Dirichlet、Poisson、DN、普通源 contact 和小正角权输入。
使用的算子是 [R37](R37-fixed-type-metric-defect-newton-interface.md)
的同一固定目标型别修正，保持真实 $Y_z$ ground state；没有把它改称
原度量映射的精确导数。这里保留全部角频、均值和两个端口之间的 cross。

本篇不把这个有限正环带称为已经封闭的帽，也不把 $r=3$ 的有限 Robin
行当成真实无限外尾或固定开握持区。末节列清当前对象的实际接合状态。

## 1. 准确对象与实际常数

取

$$
\delta_4=-\frac{7789866024620307}{4611686018427387904}.
\tag{64.1}
$$

对象文件是
`data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_object.json`，
SHA256
`87566dee6e119bb4127200c2dae38f9cdf692a18475c1cde23961a56605919b5`。
其 origin 和 direction 分别为该目录下
`type_fixed_step02_d5_jet_interval_inputs.npz`、
`type_fixed_step02_d5_actual_parameter_direction.npz`，SHA256 分别为

```
0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b
8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab
```

参数在所有 raw phase 与 mean 系数中准确施加，然后才乘固定的 base
三次、二次权重。半径和 beta 显式偶，gamma 和准确积分高度显式奇。
曲面始终是 [R33](R33-exact-unit-tangent-retraction.md) 的真无限
单位切向原函数，目标度量为同一对象的
$g_0=E(r)dr^2+a(r)^2d\theta^2$，$E=\langle|F_r|^2\rangle$。
本篇所用准确公式在下一节重新列出。

真实正根 $t$ 已由同点的有向根证书隔离于

$$
0.23839687429955836\le t\le0.23839687429956505,
\qquad L=\frac14-t>0.
\tag{64.2}
$$

这里十进制展示对应证书中保存的准确 binary64 端点；严格比较使用其
Fraction 值。根文件
`type_fixed_step02_d5_exact_affine_step4_root_tight.json` 的 SHA256 是
`03a0863733b25b6c4058a39590648dda2292a2943e783021747e3bc3f27c86f4`。

在 $[t,1/4]\times S^1$ 上，本篇构造保持 $r$ 不变的真实角图，
使 ground-state 算子的正能量矩阵准确成为
$A_0^{1/2}CA_0^{1/2}$，$A_0=\operatorname{diag}(1,x)$、$x=r-t$。
可以使用下列安全常数；每行都由同一份未四舍五入的证书独立导出，
不是把各行显示上界相乘后再假装得到更紧的一行。

| 实际量 | 可使用的严格界 |
|---|---:|
| $K_0(r)/(r-t)$，按连续值延到根 | $14<K_0/(r-t)<118$ |
| 实角流 Jacobian 及其倒数 | 小于 $1.277$ |
| 归一矩阵比较 | $0.0247 I<C<46.05 I$ |
| $Y_z=F_z/|F|$ | $0.229<Y_z<0.264$ |
| trace 常数 $C_{\rm tr}$ | 小于 $1902852$ |
| 右逆延拓常数 $C_E$ | 小于 $345$ |
| 零 Dirichlet 逆 $g$ | 小于 $40.389$ |
| 完整 Poisson、完整 $V^*$ source contact | 小于 $34550$ |
| 完整 DN norm | 小于 $15875$ |
| 内部 $L^2H^{2/3}$ 能量嵌入 | 小于 $172.371$ |
| $L^2H^{-2/3}$ 普通源到完整 contact | 小于 $5955237$ |
| 物理 $L^2$ 源到最终密度 $L^2$ 源 | 小于 $0.299$ |

在两个端口均使用同一 Fourier 权 $W_s=e^{s|D_\phi|}$，可以明确取

$$
|s|\le 2^{-75}.
\tag{64.3}
$$

该范围内，后面定义的完整归一 Robin 逆 norm 不超过2，完整 Cayley
norm 不超过5。这个小正宽是实际支付的值，不将它代换成此前核心图中
更宽的角带，也不声称它已经足以支付最终所有迭代常数。

## 2. 同一曲面的准确标架与算子

所有向量分量先在旋转柱坐标基表示。令

$$
T=(-\cos\gamma\sin\beta,\ \cos\gamma\cos\beta,\ \sin\gamma),
\qquad F=a\mathcal P_\theta T+Ze_z,
\qquad F_\theta=aT.
\tag{64.4}
$$

$\mathcal P_\theta$ 是准确零均值笛卡尔原函数，以旋转基表示时其非零
频率乘子与前述 native 证书一致。不是有限 FFT 原函数的定义。

写 $X=F_r$、$c=\cos\gamma$、$s=\sin\gamma$，并引入正交标架

$$
e_h=(-\sin\beta,\cos\beta,0),\qquad
e_v=(-\cos\beta,-\sin\beta,0),\qquad
e_q=-s e_h+c e_z.
$$

定义标量

$$
h_X=X\cdot e_h,\quad v=X\cdot e_v,\quad
Q=X\cdot e_q=cX_z-sh_X,\quad R=X\cdot T=ch_X+sX_z,
$$
$$
\mathcal D=(1+\beta_\theta)cQ-\gamma_\theta v,
\qquad \mathcal M=\beta_r cQ-\gamma_rv,
\qquad \mathcal W=Q^2+v^2,
$$
$$
\mathcal H=(F\cdot e_q)v-(F\cdot e_v)Q.
\tag{64.5}
$$

由 $T\times e_q=-e_v$、$T\times e_v=e_q$ 以及真实角导数
$T_\theta=(1+\beta_\theta)T_\beta+\gamma_\theta T_\gamma$，准确得到

$$
G:=|F_\theta\times F_r|^2=a^2\mathcal W,\qquad
h:=(F_\theta\times F_r)\cdot F=a\mathcal H,
$$
$$
n_0:=(F_\theta\times F_r)\cdot F_{\theta\theta}=-a^2\mathcal D,
\qquad
m_0:=(F_\theta\times F_r)\cdot F_{r\theta}=-a^2\mathcal M.
\tag{64.6}
$$

特别是两个第二基本形式系数在这里具有相同的负号。
证明也可以直接对 (64.4) 作乘积求导；式中没有对有限 primitive
求角导来替代真 $aT$。

R37 的材料密度满足
$A=-\operatorname{cof}(II)/(\zeta^2\sqrt G)$、
$\zeta=h/(\sqrt G|F|)$。
保持 $A_{rr},A_{r\theta}$ 并把行列式改成 $K_0/\zeta^4$，得到
$\widehat A$。本篇选择与实际 beta 计算相同的全 $\ell$ 口径：
$\ell=\partial_\theta\log(F_z/r)-\partial_\theta\log|F|$
在这个正侧等于 $Y_\theta/Y$，其中 $Y=Y_z>0$。
取

$$
\widehat d=-Y^{-1}\operatorname{div}(\widehat A\nabla Y),
\qquad \widehat P=\operatorname{div}(\widehat A\nabla)+\widehat d.
\tag{64.7}
$$

于是 $Y\widehat P(YU)=\operatorname{div}(B\nabla U)$、$B=Y^2\widehat A$。
代入 (64.6)，所有 $\zeta$、$|F|$ 及多余的半径因子准确消去：

$$
\boxed{
 B=\begin{pmatrix}
 \alpha&\alpha b\\
 \alpha b&\alpha b^2+\eta K_0
 \end{pmatrix},\qquad
 b=-\frac{\mathcal M}{\mathcal D},\quad
 \alpha=\frac{F_z^2\mathcal D}{\mathcal H^2},\quad
 \eta=\frac{F_z^2\mathcal W^2}{\mathcal D\mathcal H^2}.
 }
\tag{64.8}
$$

这些是当前非径向对象的准确式子，并非径向背景近似。
真实计算支付 $F_z>0$、$\mathcal D>0$、$h>0$、$G>0$，所以 (64.7)
合法，$\alpha,\eta>0$。使用这一整体代数化简也避免极小量被无意义地
反复除乘，但并没有省去任何误差项。

## 3. 连续有向计算实际覆盖什么

源和最终报告为：

| 文件 | SHA256 |
|---|---|
| `scripts/fourfold_phase_actual_positive_cap.py` | `1e8418174f54bd1d22dd628ef7f7e6525ca6b43cbcf7a2307d29f9d467e1612b` |
| `notes/2026-11-12-step4-actual-positive-cap.json` | `44aa2dfb783b975c6904b0a57335a2b7d809e07956a484984f6ef9df02840126` |

最终重放使用160 bits、256 quarter primitive nodes、512角盒、
normalized 复角宽 $1/128$，即物理 $|\operatorname{Im}\theta|\le1/512$。
每个物理样条及其反射 knots 都参与准确 Fraction 分割；包括相距仅几个
binary64 ulp 的相邻 knots。原分割加根 collar 边界共有9段，按最大宽度
$1/4096$ 分成55个闭子区间，全部通过，无失败或待处理区间。

每个原样条 span 使用准确有理中点定位，并以同一 span 的完整多项式
计算，包括物理加权后最高二十次的相位 germ。该多项式的解析延拓只用于
这个 span 的误差预算，不要求跨 knots 的径向函数解析。
primitive 的每个运算和 FFT 都是有向区间运算，且另加入真无限 Fourier
尾和 alias 费用。$E,E',E''$ 的无限误差先加入，再形成

$$
K_0=\frac{a'E'-2a''E}{2aE^2},\qquad K_0'.
\tag{64.9}
$$

所有角盒覆盖 normalized 角 $4\theta$ 的节点及左右半间隙；计算不是
只取角节点极值。旋转基的准确反射性使 $\mathcal D,\mathcal W,\mathcal H$
及 $b_\theta$ 为偶函数，$b$ 为奇函数，故所用半圈加对称反射覆盖完整角圈，
对对称复带也成立。

在根包络左端到 $t_{\rm upper}+1/4096$ 的初始 collar 上支付 $K_0'>0$。
因为 $K_0(t)=0$，这里的 $K_0/(r-t)$ 由整个初始 collar 的 $K_0'$ 上下界
控制。其余闭子区间直接支付 $K_0>0$，再用同一准确根包络除以 $r-t$。
没有假设 $K_0'$ 在整个 $[t,1/4]$ 正，也没有在包含根的区间直接除以零。
得到整个正环带的实际界

$$
14.3212538808<\frac{K_0}{r-t}<117.260853947.
\tag{64.10}
$$

为支付角流，源码使用下列准确一阶公式：

$$
Q_\theta=a\gamma_r-(1+\beta_\theta)\sin\gamma\,v-\gamma_\theta R,
\qquad
v_\theta=a\cos\gamma\,\beta_r-(1+\beta_\theta)h_X.
$$

对 (64.5) 求导即可得到 $\mathcal D_\theta,\mathcal M_\theta$，因此
$b_\theta=-\mathcal M_\theta/\mathcal D+
\mathcal M\mathcal D_\theta/\mathcal D^2$。
实域直接区间计算；复域先认证 $\mathcal D,\mathcal H$ 无零，再使用模数式

$$
|b_\theta|\le\frac{|\mathcal M_\theta|}{|\mathcal D|}
+\frac{|\mathcal M||\mathcal D_\theta|}{|\mathcal D|^2},
\tag{64.11}
$$

而不是对宽复矩形连续取倒数后把膨胀误认为真实几何。
所有最终常数显式检查有限；被丢弃的初版宽复盒没有进入本证书。

## 4. 保持物理径向坐标的真实角流

令 $x=r-t$，在 $0\le x\le L$ 上解

$$
\Theta_x(x,\phi)=b(t+x,\Theta(x,\phi)),\qquad
\Theta(0,\phi)=\phi,\qquad J=\Theta_\phi.
\tag{64.12}
$$

系数在实角圈光滑且有界，径向连续，故全程解存在。
$J_x=b_\theta J$、$J(0)=1$ 给 $J>0$，周期性给度为1的圆微分同胚。
若 $V_r=\sup|b_\theta|$，则
$e^{-V_rL}\le J\le e^{V_rL}$。
有向计算得到 $V_r<21.021818$，从而 $J,J^{-1}<1.277$。

在正能量中准确有

$$
B(\nabla U,\nabla\overline U)
=\alpha|U_r+bU_\theta|^2+\eta K_0|U_\theta|^2.
$$

用 (64.12) 拉回，Jacobian 是 $J$，所以新密度准确为

$$
\widetilde B=\operatorname{diag}(J\alpha,\eta K_0/J),
\qquad
C=\operatorname{diag}\left(J\alpha,
                 \frac{\eta}{J}\frac{K_0}{x}\right).
\tag{64.13}
$$

$K_0/x$ 在根上的连续值来自上一节；根位于一个严格内部的共同解析
span，因此此处的所需正则没有跨 knot 的问题。其余位置也不产生任何
径向反求 $r=r(x,\phi)$，所有径向 knots 仍是固定 $x$ 值。
这是当前 $C^4\cap W^{5,\infty}$ 径向对象进入能量空间时的实际优势；
并未因此假设它在混合坐标下任意阶解析。

把全部单元的 $\alpha,\eta$、(64.10) 和 $e^{V_rL}$ 合并，准确得到

$$
m>0.0247598409245,\qquad M<46.0470750046,
\qquad mI\le C\le MI.
\tag{64.14}
$$

## 5. 完整两个端口与普通源

令

$$
\|U\|_V^2=\int_0^L\int_{S^1}
(|U|^2+|U_x|^2+x|U_\phi|^2),\qquad
\mathcal T=H^{1/3}\oplus H^{1/2},
$$

角积分取 $d\phi/(2\pi)$，两个分量分别为根端和普通切口端。
[R36](R36-moving-turning-cap-normalization.md) §6 的 trace 和右逆适用于
同一个真实矩阵 (64.13)，其常数在本篇由 $L$ 的准确区间计算。
不能在普通右端改用 $H^{1/3}$。

在零 trace 子空间，Poincaré 和 (64.14) 给

$$
g=\frac{1+L^2/\pi^2}{m},\qquad
G:(V_{00})^*\longrightarrow V_{00},\quad\|G\|\le g.
$$

[R35](R35-positive-cap-without-background-smallness.md) §§3–4 的同一
实际正 form 给

$$
\mathcal H=E-GPE,\qquad
\Lambda=E^*PE-E^*PGPE,
$$
$$
\langle\mathcal K f,h_\partial\rangle
=\mathfrak e(Gf,Eh_\partial)-\langle f,Eh_\partial\rangle,
\quad f\in V^*.
\tag{64.15}
$$

因此 $\|\mathcal H\|,\|\mathcal K\|\le\sqrt{C_E}(1+Mg)$、
$\|\Lambda\|\le MC_E$，给表中各实际值。
$\Lambda$ 是完整自伴非负 DN；它的 kernel 为共同常数，两端 cross 保留。
准确 charge 为 $\langle\mathcal Kf,(1,1)\rangle=-\langle f,1\rangle$。
只给 $V_{00}^*$ 上的源限制不足以定义 (64.15) 的第二项。

[R45](R45-positive-interior-gain-and-full-source-contact.md) 的实际内部
嵌入常数是

$$
C_I=\sqrt{1+\max\{3,4/L^2\}}.
$$

由 $\mathcal K=-\mathcal H^*$，得到同一全矩阵源增益

$$
\mathcal K:L^2_xH^{-2/3}_\phi\longrightarrow
H^{-1/3}\oplus H^{-1/2},\qquad
\|\mathcal K\|\le C_I\sqrt{C_E}(1+Mg)<5955237.
\tag{64.16}
$$

故根端相对源增益 $1/3$，普通端相对源增益 $1/6$。
这不是逐 Fourier 模的数值检查。

若原材料密度方程是 $\widehat P w=f$，置 $w=YU$ 后再作角流，最终
正号方程的源准确为

$$
\widetilde f(x,\phi)=-J(x,\phi)Y(t+x,\Theta)
                      f(t+x,\Theta).
\tag{64.17}
$$

真实变量换元给
$\|\widetilde f\|_{L^2}\le\sqrt{\sup J}\sup Y\|f\|_{L^2}<0.299\|f\|_{L^2}$。
边界 ground-state 动量为 $Yp_w-wp_Y$，随后还要按角图的对偶密度
换元；没有把它直接称为原来的 $p_w$。同样，(64.16) 的带负角阶源
是在明确写出的最终变量中，未免费转授未计费的原坐标复合范数。

## 6. 实际正角宽、有限角导数与 signed Robin

计算在物理角带 $s_c=1/512$ 上支付

$$
V_c:=\sup|b_\theta|<250.616617.
$$

将复初值轨道与同实部的实轨道比较，差的导数模至多 $V_c$ 乘差。
只要 $|\operatorname{Im}\phi|\le s_c/(2e^{V_cL})$，首次出管论证保证
整条复轨道仍在物理角带内部一半。故真实角流及 $J,J^{-1}$ 在

$$
\rho_*:=\frac{s_c}{2e^{V_cL}}>5.3308865350\cdot10^{-5}
\tag{64.18}
$$

上全纯，且 $|J|,|J^{-1}|\le e^{V_cL}$。
这是只用实径向时间的参数解析性，不要求径向跨 knot 全纯。
由实际复 $\alpha,\eta$ 界和 (64.13)，有
$\sup\|C\|<563.455$ 于这个带。
因此每个所需有限角阶都可明确取

$$
B_p\le p!\,564\left(\frac2{\rho_*}\right)^p,
\tag{64.19}
$$

支付 R45 的全部有限正、负 Sobolev 窗口；没有未命名的系数常数。

Fourier 系数满足 $\sup_x\|C_k(x)\|\le M_c e^{-\rho_*|k|}$。
在半宽上可用

$$
N_C\le\frac{2M_c e^{-\rho_*/2}}{(1-e^{-\rho_*/2})^2}
<1.587\cdot10^{12},
\tag{64.20}
$$

实际 DN 交换常数
$C_\Lambda=C_E[1+2g(M+1)]^2<4.982\cdot10^9$。
代码用 `expm1` 形成分母，且拒绝任何非有限常数，避免极窄角带下的
减法失精度成为假通过。取 (64.3)，同时满足 R35 的三个实际门

$$
|s|\le\rho_*/2,\qquad
|s|N_C\le\min\{1,(2g)^{-1}\},\qquad
|s|C_\Lambda N_C\le1/2.
$$

令 $Q_\partial=\operatorname{diag}(\langle D\rangle^{1/3},
\langle D\rangle^{1/2})$，$B_\partial=Q_\partial^{-1}\Lambda Q_\partial^{-1}$。
在当前明确 ground-state 通量 frame 中取 real shear 为零，则

$$
\|W_s(B_\partial-iI)^{-1}W_s^{-1}\|\le2,
\qquad
\|W_s(B_\partial+iI)(B_\partial-iI)^{-1}W_s^{-1}\|\le5.
\tag{64.21}
$$

正负权均被支付；非实 Robin 的满射来自同一真实自伴实现和其伴随。
普通源仍经 (64.15) 的完整 contact 进入该逆。
若改用 Airy 通量列，须再付同一高度 shear 和边界复合，不能把 (64.21)
的 frame 直接改名成未校准的 Airy frame。

## 7. 实际外段、固定开 H 与下一项具体输入

当前对象的全部冻结 scalar splines 只定义共同材料区间 $[-3,3]$。
其数值求解器在 $r=3$ 使用有限 Robin/残差行，没有保存一个已经与
当前 $a,Z,\beta,\gamma$ 完整二 jet 匹配的非线性外延。
[R22](R22-mu4-true-tail-and-source-conversion.md)、
[R23](R23-mu4-full-graft-and-marker-geometry.md) 的实际接尾是另一个
径向背景及其线性第四模；R23 的共同入口为物理 $x=20$、$u=80$。
本图的周长半径与准确高度、全部高角频两迹及 mean 都没有被这些旧结果匹配。
所以目前没有可指认的“当前 $r=3$ 切口所接的已构造完整外尾”。

本篇已经支付一个实际正环带，并把其普通右端保留为完整端口。
继续向外时需要同一对象在 $[1/4,3]$ 的真实系数以及此后明确外延；
实际外部 source/DN 必须保全部角频、mean 和切向重建项，不能只保第4模
或一个齐次斜率。旧真实无限平尾还含自己的退化层和型别结构，不能把它
自动放入本篇简单单根正模型。

固定开 $H$ 要求同一曲面族在接合处的真实差具有零二 jet，并且两个
不相连帽之间的相对 Killing 数据兼容。[R37](R37-fixed-type-metric-defect-newton-interface.md)
§8 已说明，一个全局 rotation 规范不能分别消去两帽的独立刚体迹。
本篇一个有限正组件的 Dirichlet 或 Robin 迹不提供这项结论。

根本身严格位于一个解析 scalar span 内，因此 R47/R53 所需有限高阶
根 Taylor 数据有明确可计算来源；但其真实 canonical 坐标、height、
余项强 norm 和与外端的全反射仍须实际计算。
本篇不把仅有 $C^4$ 的整个 body 转成无限混合径向正则，亦不宣称已经
构造出题目所需的闭 $C^2$ 精确等距族。

## 8. 重放

在本课题目录运行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_actual_positive_cap.py \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_root_tight.json \
  --cut 1/4 --normalized-strip 1/128 --max-cell-width 1/4096 \
  --quarter-nodes 256 --angles 512 --bits 160 \
  --out /workspace/scratch/f6a2c7886477/step4-positive-collar-replay.json
```

报告保存准确对象、根、源码和全部依赖 SHA，所有55个闭区间的真实输入界，
准确 Fraction 覆盖状态及完整算子常数。读取界时使用有向端点，
不使用仅为展示的 `mid_float`。
