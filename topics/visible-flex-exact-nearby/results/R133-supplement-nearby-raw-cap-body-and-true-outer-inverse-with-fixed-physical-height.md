# R133：固定物理高度下的附近 raw 帽主体—真实外行解算器

2026-11-15，visible-exact-astra-0df9。

**解析组合证明；实际高度 connection、同源反馈和物理高度单位已独立核对。** 本篇将已经分别付清的保守主体差、
真实外行差和基点 residual transport 放入同一个方程。
所固定的是 T 的原实际物理高度背景，不把它缩成新的较小数据。
高背景在 $\mathfrak M_{8212}$ 中，线性方向授予 $1\le S\le8192$；
内端口采用原完整帽解算器的同一固定线性坐标。
完整 mean、相位、height 和相容性荷继续按原列读出。

本篇给附近各点的线性状态解算器，以及固定该物理高度时的完整
主体加真实外行二次余项。它没有证明目前数值中心的 residual 入球，
也没有把保持的内端口坐标误称为已经完成全体 nonlinear 内匹配。

依赖：
[C主体差](R133-supplement-finite-Sobolev-nearby-cap-body-inverse-and-same-space-remainder.md)、
[B真实外行差](R133-supplement-high-background-true-regular-row-difference-and-good-height.md)、
[R新 raw 基逆](R133-supplement-base-off-shell-outer-transport-and-raw-cap-inverse.md)、
[F物理 finite jets](R133-supplement-cap-finite-Sobolev-ball-to-physical-curvature-jets.md)、
[T原实际 long 背景](R133-supplement-full-delta-fixed-angle-regular-graph-analytic-translation.md)。

## 1. 同一基点、背景和准确源坐标

保持原 $\eta_0$、$|\delta|\le10^{-8}$、
连续修补定义440866a3…、完整方向6a71cb81…及同一 $Q_\delta$。
令 $x=\theta_0$、$\varphi=\Phi_0(x)$，帽号仅表示与这个已知图复合。
$\mathcal H_0=(D\Psi_0)^{-1}$ 仍是固定中心的完整微分逆，
包括原 primitive 和全部 mean 项。取
$$
 \widehat Y=\mathcal H_0z,\qquad Q=Q_\delta+Y,\qquad
 \rho=\|z\|_{\mathfrak M_{8212}}\le R_*:=2^{-8388608}.
 \tag{N.1}
$$
$\mathfrak M_S$ 使用 C.1 的逐 Fourier 系数径向 supremum 后求平方和，
不是任意交换后的 $L^\infty_rH^S$ 范数。

固定 T.6 中已经识别的同一个物理非mean高度 $f_{B,\delta}(\theta)$：
$$
 F_B:=\|f_{B,\delta}\|_{\dot A^2_{1/128}}<10^{-11}<1 .
 \tag{N.2}
$$
这里 $f_B$ 是归一化高度。物理高度 $g_B^{\rm ph}$ 与它的关系仍为
$f_B=P_\perp g_B^{\rm ph}/s_B$，$s_B=a_Bw_B$，不能省去 $s_B^{-1}$。
独立常高度及原 mean flux 不包含在 (N.2) 的非mean norm 中。

对真实帽角 $\tau_Q=\Theta_Q\circ\Phi_0$，定义
$$
 j_Q=\partial_x\tau_Q,\qquad
 y_B(Q)=P_{\perp,x}(f_{B,\delta}\circ\tau_Q).
 \tag{N.3}
$$
加权代表是 $J_{j_Q}y_B$。因 $f_{B,\delta}$ 的真实物理 mean 为零，
它准确等于 $f_{B,\delta}\circ\tau_Q$；其常高度仍另加原 gauge。

真实外残差采用 R.3 的完整 raw 输出，外 source 转换固定在 $\delta$
基点，包含 $P_{\perp,x}R_B^\flat$、两个真实 weighted curvature mean
及原独立端荷。不能对当前变化的 normalization factor 乘 residual，
然后漏掉该因子的导数。

内端口保持 R/C 所用的原固定线性边界坐标，作为此局部帽消元器的
独立输入列。它不被重新定义成当前未知物理角下的 nonlinear
$C_{\rm in}(Q)$；后者若在全网络中作为匹配变量，须另付其准确
非线性 readout 和相位/mean 坐标转换。

记 $\mathfrak D_S^{\rm good}$ 为原完整 source 空间：保守 divergence
以势的 $\mathfrak M_S$ norm 计，ordinary 源以原 $L^2_rH^S$ 计，
保全部 jump、固定内端口、raw 外荷、mean、相位和 height 列。
独立 good-height 方向用
$$
       J_{j_Q}|D_x|^{-2}g_B,\qquad
       \|g_B\|_{H^S},\qquad g_B\perp1                      \tag{N.4}
$$
计费。两个高度角导和当前 weighted mean 没有删除。
R.23–R.25 在回物理高度前的完整源估计，允许宽取
$$
 \|\mathcal G_{\delta,\rm raw}^{\rm state}:
       \mathfrak D_S^{\rm good}\to\mathfrak M_S\|
                 <G_*:=2^{4194304}.
 \tag{N.5}
$$
该大常数覆盖原固定 common-$x$ 源的更紧 $2^{416\cdot8212+261}$。
不在 (N.5) 中额外复合未知数据与复角。

## 2. 原物理高度的有限高范数，明确付清 connection

(N.2) 对同一个已知高度确实给所需高 norm。
对 $n\in4\mathbb Z\setminus\{0\}$ 和 $k=8198$，
$$
 \langle n\rangle^k\le2^{k/2}|n|^k,\qquad
 \|f_{B,\delta}\|_{H^k}
 \le2^{k/2}
       \sup_{t\ge4}\{t^{k-2}e^{-t/128}\}\,F_B .
$$
令 $p=k-2<2^{14}$。由完整指数级数，
$t^pe^{-t/128}\le p!\,128^p\le(128p)^p<2^{21p}$。
所以
$$
       \|f_{B,\delta}\|_{H^{8198}}<2^{262144}.
 \tag{N.6}
$$
只用 $k/2+21(k-2)<262144$ 的符号比较；这里没有新数值计算，
也没有把零宽 $\dot A^2$ 的小门当作高 Sobolev 界。

沿 (N.1) 内的真实直线 $Q_\lambda=Q_\delta+\lambda Y$，
B.21 已付两个真实实角至8198阶：
$$
 B_{\rm high}
 :=\sup_{0\le\lambda\le1}\|y_B(Q_\lambda)\|_{H^{8198}}
 \le2^{524928}\|f_{B,\delta}\|_{H^{8198}}
 <2^{787072}.                                            \tag{N.7}
$$
高 norm 可以很大，不要求它小于 $2^{-524290}$。
使用 B.23 的准确 connection，
$$
 \dot y_B=P_{\perp,x}(b_\lambda y_{B,x}),\qquad
 P_{\perp,x}(\dot y_B-b_\lambda y_{B,x})=0 .
 \tag{N.8}
$$
所以固定物理高度时 good-height 方向为零，ordinary 背景差仍须计费。
B.24 和 (N.7) 给
$$
 d_B:=\|y_B(Q)-y_{B,\delta}\|_{H^{8197}}
    \le2^{1311360}d_Q,\qquad
 d_Q:=\|\widehat Y\|_{\mathfrak M_{8212}},
$$
$$
       D=d_Q+d_B\le2^{1311361}d_Q
                  \le2^{1737347}\rho .                    \tag{N.9}
$$
最后使用 C.10 的 $d_Q<2^{425986}\rho$。
(N.1) 因而给 $D\le2^{-6651261}<2^{-4096}$，B 的真实背景域确实满足。
加权常高度的导数继续按 B.7 读取；(N.8) 不是删去其 mean 的许可。

## 3. 完整主体和真实 raw 外行在同一基逆中反馈

记 $\Delta_{\rm body}(Q)$ 为原保守主体 differential 相对于
$Q_\delta$ 的差。C.13–C.20 的源恒等式与外行选用无关；
把原基逆换成已付相同常数 (N.5) 的新 raw 基逆后，仍得
$$
 \|\mathcal G_{\delta,\rm raw}^{\rm state}
                         \Delta_{\rm body}(Q)\|
       \le2^{6291456}\rho .                                \tag{N.10}
$$
所有 $R_0$ Hessian、fixed $D\Psi_0$ 的径向导数和两 curvature mean
已留在基问题中。差源不需要未知 $Y_r$，也不新增一阶角损失。

B.22 已在固定 $\mathcal H_0$ 和原 source 坐标中付
$2^{2097152}D$，其 raw 列含真正 $b_HR_{Q,B,x}$。
结合 (N.5)、(N.9)，
$$
 \|\mathcal G_{\delta,\rm raw}^{\rm state}
                              \Delta_{\rm out}(Q)\|
 \le2^{4194304+2097152+1311361+425986}\rho
 =2^{8028803}\rho .                                      \tag{N.11}
$$
这是新的 raw 基逆与 raw 差相组合；不把旧 fixed-physical good 逆
代入，也不把原 $\delta$ 基点 transport 再算一遍。
独立 good-height 源列的背景差同样在 B.22 的完整估计中。

同一固定点方程的总反馈因此为
$$
 \varepsilon_\rho
 :=(2^{6291456}+2^{8028803})\rho
 \le2^{-2097152}+2^{-359805}
 <2^{-359804}<1/4 .                                      \tag{N.12}
$$
此处相加的是作用在同一 $\mathfrak M_S$、同一 source 模块的两个
算子；不是把两个已经求逆的因子任意相乘。

若 $\mathcal L_Q=\mathcal L_{\delta,\rm raw}+\Delta_Q$，
原完整增广方程可写为
$$
 x=\mathcal G_{\delta,\rm raw}^{\rm state}
                  (d-\Delta_Qx+\delta d_{B,Q}),           \tag{N.13}
$$
其中 $\delta d_{B,Q}$ 只是当前独立 good-height 输入列相对于基点的
准确差 $(\mathfrak B_{\delta}^{\rm height}-\mathfrak B_Q^{\rm height})g_B$，按 B.22 支付；无该输入时此项为零。
有 $\|\mathcal G_{\delta,\rm raw}^{\rm state}\delta d_{B,Q}\|
\le\varepsilon_\rho\|d\|_{\mathfrak D_S^{\rm good}}$。

完整 Neumann 级数收敛，不截断未知 Fourier 模。
由 $\varepsilon_\rho<1/4$ 和 $G_*>1$，
$$
 \frac{G_*+\varepsilon_\rho}{1-\varepsilon_\rho}<2G_*,
$$
故得到
$$
 \boxed{\quad
 \|\mathcal G_{Q,f_{B,\delta}}^{\rm state}:
       \mathfrak D_S^{\rm good}\to\mathfrak M_S\|
              <2^{4194305},\qquad1\le S\le8192 .
 \quad}                                                  \tag{N.14}
$$
背景仍是8212阶；(N.14) 不授8212阶方向或一个低正则开放球。

## 4. 当前真实物理高度方向和全部荷

若给定独立真实归一化物理高度方向 $\dot f_B(\theta)$，
实际 good chart 给
$$
 g_B=|D_x|^2P_{\perp,x}(\dot f_B\circ\tau_Q).
 \tag{N.15}
$$
角运输部分已由 (N.8) 消去，不能再将它加作独立高度源。
B.21 及 $S+2\le8194<8198$ 给
$$
 \|g_B\|_{H^S}
      \le2^{524928}\|\dot f_B\|_{H^{S+2}}.                 \tag{N.16}
$$
因此同一线性解算器在这个真实高度源单位中可以宽取
$$
 2^{4194305+524928}<2^{4800000}.                           \tag{N.17}
$$
对物理未归一高度 $\dot g_B^{\rm ph}$，右端仍准确带 $s_B^{-1}$。
固定 metric 之外的 $\dot s_B$、$\Gamma$、$\nu$、长度和形状列必须按
其原实际方程微分；(N.17) 不给它们一个免费统一常数。

(N.15) 只是各个实际背景处的准确 source 坐标转换；
本篇没有使用或声称 $\|C_{\tau_Q}-C_{\tau_\delta}\|_{H^S\to H^S}$ 小。
这样也没有把下节固定物理高度的非线性余项自动推广至任意未知
物理高度变化的二阶余项。

若原增广逆为 $(G_{\rm state},G_{\rm charge})$，
(N.13) 收敛后必须用同一完整 source
$$
 c=G_{\delta,\rm raw}^{\rm charge}
                 (d-\Delta_Qx+\delta d_{B,Q})             \tag{N.18}
$$
恢复全部原荷。两个 curvature mean、height gauge、mean flux、
角常相位与径向 principal 参数各保原身份。
$\mathfrak D_S^{\rm good}$ 的边界荷不是不相容数据可任意指定的许诺；
真正齐次物理匹配还必须满足恢复的零荷/两迹条件。
尤其不能将 (N.18) 删掉后把仅有 state 的算子称为零荷边值问题的逆。

## 5. 固定实际物理高度的完整二次余项

沿 (N.1) 的帽状态变化，继续固定同一个 $f_{B,\delta}(\theta)$。
令 $\mathcal F_\delta(z)$ 的主体为原真实 Codazzi conservative residual，
其外行取第1节的完整 raw residual，内端口用同一个固定线性坐标。
在需要径向导数时先对真实分片光滑状态写恒等式；
线性径向项在以下余项中准确消失，故余项通过 C 的 polynomial 源
和 B 的真边界图延拓到上述有限 $\mathfrak M_{8212}$ 背景。

定义准确基点余项
$$
 \mathcal R_\delta(z)=
       \mathcal F_\delta(z)-\mathcal F_\delta(0)
                           -D\mathcal F_\delta(0)z .
 \tag{N.19}
$$
$\mathcal F_\delta(0)$ 不被设为零。
主体的二次/cubic、外行非线性、raw residual transport 和真实
weighted mean 的变化全部在 (N.19) 中，固定线性内端口的余项为零。

在 $tz$ 上重复 (N.9)–(N.12)，其背景差至多乘 $t$。
沿同一真线段积分实际 differential，得到
$$
 \boxed{\quad
 \|\mathcal G_{\delta,\rm raw}^{\rm state}
                      \mathcal R_\delta(z)\|_{\mathfrak M_S}
 \le2^{8028804}\|z\|_{\mathfrak M_{8212}}
                         \|z\|_{\mathfrak M_S},
 \qquad1\le S\le8192 .
 \quad}                                                  \tag{N.20}
$$
同样，对同一8212阶半径 $R\le R_*$ 内的 $z_1,z_2$，真线段仍在球内，
$$
 \|\mathcal G_{\delta,\rm raw}^{\rm state}
       [\mathcal R_\delta(z_1)-\mathcal R_\delta(z_2)]\|_{\mathfrak M_S}
 \le2^{8028804}R\,\|z_1-z_2\|_{\mathfrak M_S}.
 \tag{N.21}
$$
这是在明确高背景域上的低方向 Lipschitz 估计。
没有把 $\mathfrak M_S$ 的一个任意低球当作可用背景域，
也没有为 raw-height 在所有变量上断言同域 $C^2$。

## 6. 已闭接口与仍须真正解决的入口

本篇付清的是同原内端口坐标、同实际物理高度背景的
“非线性主体加真实 raw 外行”局部线性消元和完整基点余项。
原 $10^{-11}$ 高度域、其巨大但有限的高 norm、真实 connection、
两 curvature mean 与全 source/charge 约定全部保留。

下一项须让真实全网络给出允许变化的内外高度与曲率迹，并支付
它们的 nonlinear readout、第一/第二 principal 参数、
径向 residual jets 和 smoothing 域。方向输出只到8192，
不能由此说每一步自动回到8212背景域。
还须给一个真正可以进入该域的中心或延续/后验门；
目前 $Q_\delta$ 本身非PDE解，极小半径不是 actual residual 证书。
同97方向合成、强返回、完整 $\nu$ Schur、holonomy/全部matching及
最终几何完成门继续保留。
