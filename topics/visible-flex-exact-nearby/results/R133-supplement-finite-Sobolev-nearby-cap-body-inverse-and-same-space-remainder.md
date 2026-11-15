# R133：完整正帽的有限 Sobolev 邻域、主体逆与同域二次余项

2026-11-15，visible-exact-astra-0df9。

**已证明一个明确的全频有限正则主体邻域。** 对原整个实区间
$|\delta|\le10^{-8}$、固定 $\eta_0$ 和显式 $Q_\delta=Q_0+\delta Z$，
在原固定物理角中取整数 $1\le S\le8212$。以完整固定微分
$\mathcal H=(D\Psi_0)^{-1}$ 参数化状态变化，则半径
$2^{-8388608}$ 的 $\mathfrak M_S$ 球上，主体 Jacobian 相对于同一
真实 $\delta$ 处完整帽逆的反馈小于 $2^{-2097152}$。
同一输入、输出 Sobolev 阶上的二次余项及 Lipschitz 界一并成立。

这里外端保留该 $\delta$ 处已经证明的**真实线性** long 行，
不是将它改回 $\delta=0$。未知状态改变后的非线性外图仍须另外求解；
本篇没有把它冻结所得的子问题当作完整非线性边值问题。
原独立 mean、兼容性荷、height gauge、jump 和全部频率均保留。
本篇使用已完成的解析系数和符号预算，没有新数值生产。

依赖：
[P完整保守源](R133-supplement-fixed-base-conservative-source-transport-and-nearby-cap-linearization.md)、
[N精确多项式余项](R133-supplement-complete-moving-nonlinear-flux-and-metric-remainder.md)、
[W完整固定角系数](R133-supplement-full-delta-body-shifted-Sobolev-inverse-with-fixed-ports.md)、
[X真实全外行](R133-supplement-complete-real-delta-true-outer-finite-Sobolev-cap-inverse.md)、
[Q高阶窗口](R133-supplement-high-finite-Sobolev-window-for-the-true-full-delta-cap-inverse.md)。

## 1. 同一 Fourier 模块确实具有所需有限正则乘法

在 $I=[9/10,25/8]$ 上，标量范数为
$$
 \|f\|_S^2=\sum_{n\in4\mathbb Z}\langle n\rangle^{2S}
                  \sup_{r\in I}|f_n(r)|^2,\qquad
 \langle n\rangle=(1+n^2)^{1/2}.                         \tag{C.1}
$$
两分量用范数之和。允许原修补分片的真实单侧迹；需要连续的状态
仍在连续子空间中。先取每一频率的径向 supremum，之后求平方和。

对 $S\ge1$，Cauchy--Schwarz 与
$\sum_{n\in4\mathbb Z}\langle n\rangle^{-2}<4$ 给
$$
 \|f\|_{\mathscr A_0}\le2\|f\|_S .                        \tag{C.2}
$$
从
$\langle p+q\rangle^S\le2^{S-1}
(\langle p\rangle^S+\langle q\rangle^S)$，
逐频径向 supremum、Young 卷积和 C.2 得
$$
 \|fg\|_S\le A_S\|f\|_S\|g\|_S,\qquad A_S=2^{S+1}.
                                                                  \tag{C.3}
$$
同一界适用于声明的 pair norm 和相应双线性收缩。
mean 频率始终留在这些和中。这个证明没有交换两个 supremum/sum
的顺序，也没有要求未知方向角解析或有限 Fourier 支持。

## 2. 已知系数的统一高阶乘子费用

帽号始终表示与已知的固定 $\Phi_0$ 复合。W.8 已由原完整 $Z$
消费得到
$\|\widehat{\delta Z}\|_{\mathscr A_{1/128}}<10^{-8}$。
W.11、S.20 的同一完整系数表给下列已合并系数的 joint
$\mathscr A_{1/128}$ 范数均可宽放为 $2^{32}$：
$$
 \widehat Q_\delta,\quad P,\ M,\ W_\theta,\ C,\ mC,\quad
 S',\ S'vW_\theta .                                      \tag{C.4}
$$
这里 $S'=\left(\begin{smallmatrix}v&-uv\\0&-v^2\end{smallmatrix}\right)$
仍取固定中心 $Q_0$。有序组合已合并者使用其原联合界。
$\beta,\gamma,K,m$ 是径向标量，仍使用原真实区间上的界。

若 $\|a\|_{\mathscr A_{1/128}}\le2^{32}$，则
$$
 \sum_n\langle n\rangle^S\sup_I|a_n|
 \le2^{32}\sup_{t\ge0}(1+t)^S e^{-t/128}
 \le2^{S+33}S!\,128^S .
$$
用 $S\le8212<2^{14}$ 和
$\langle p+q\rangle^S\le2^{S/2}\langle p\rangle^S\langle q\rangle^S$，
完整乘子在 $\mathfrak M_S$ 上满足
$$
 \|M_a\|\le2^{23S+34}< C_*:=2^{212992}.
                                                                  \tag{C.5}
$$
同一预算亦控制系数本身的 $\mathfrak M_S$ 范数。所有高阶费用只从
已知系数的原 joint strip 取得；没有对未知修正作复角求值。

原本征实际消费给
$$
 b_*<6,\qquad g_*<6,\qquad
        k_*=\max(1,\sup_I|K|)=1.                          \tag{C.6}
$$
这些常数来自整个帽区，非根 germ。原 compact $\nu$ bump 在该区恒零。

## 3. 原 weighted mean、primitive、完整微分和保守源

使用 P.8 的准确同角算子
$$
 \Pi_0g=m\langle Cg\rangle_\theta,\qquad
 \mathcal I_0=(1-\Pi_0)I_\theta M_{mC}(1-\Pi_0).
                                                                  \tag{C.7}
$$
原 $J=\|mC\|_{\mathscr A_0}<33/32$ 给
$\|\Pi_0:\mathfrak M_S\to\mathfrak M_S\|<2$：
输出只有零频，故不付虚假的高阶乘子费。
$I_\theta$ 在全频空间的范数不超过 $1/4$，且不作用零频。
因而
$$
 \|\mathcal I_0\|\le \tfrac94 C_*<4C_* .                 \tag{C.8}
$$

原逆微分保持完整公式
$$
 \mathcal Hx=S'x-S'vW_\theta p_c,\qquad
       p_c=I_\theta(c-mC\langle c\rangle_\theta).
                                                                  \tag{C.9}
$$
由 C.5，
$\|p_c\|_S\le C_*\|c\|_S/2$，于是
$$
 \|\mathcal Hx\|_S<2C_*^2\|x\|_S
                         <2^{425986}\|x\|_S .           \tag{C.10}
$$
这估计的是固定物理角中的完整 $\widehat h$；未宣称未知
moving $\ell^2(\sup_r)$ 角复合有界。

对原 moving 源 $\partial_\varphi a+b$，P.6 的准确变换是
$$
 D\Psi_0(\partial_\varphi a+b)
  =\partial_\theta(M\widehat a)
       +W_\theta\langle C\widehat a_2\rangle_\theta
       +P\widehat b-W_\theta E_b,\quad
 E_b=(1-\Pi_0)I_\theta(C\widehat b_2).                   \tag{C.11}
$$
特别是 divergence 的 rank mean 符号为正，两个 curvature mean
遵守 P.7；不作额外投影。
C.5、C.8 给 $\|E_b\|_S<C_*\|\widehat b\|_S$。
分别支付完整 divergence 势与 ordinary 源，再用
$\sqrt{|I|}<3/2$，得到
$$
 \|D\Psi_0(\partial_\varphi a+b)\|_{\mathfrak D_S,\rm body}
 \le4C_*^2(\|\widehat a\|_S+\|\widehat b\|_S).            \tag{C.12}
$$
此处 source norm 是 X/Q 的原列范数之和：divergence 以其势的
$\mathfrak M_S$ 范数计，ordinary 以 $L^2_rH^S$ 计。
不是将 $\partial_\theta a$ 的 ordinary 范数免费少算一角导。
所有独立端荷与 jump 在本条纯主体变化中保持原给定值。

## 4. 任意有限正则修正的完整 Jacobian 差

在 P.12--P.13 中将背景 $Q_0$ 替换成 $Q_\delta$，
但角图、$\Pi_0,\mathcal I_0,\mathcal H$ 仍固定在 $Q_0$。
这准确给出
$$
 [DF(Q_\delta+Y)-DF(Q_\delta)]h
                     =\partial_\varphi a_Y(h)+b_Y(h).
                                                                  \tag{C.13}
$$
令
$r=\|\widehat Y\|_S\le1$、$t=\|\widehat h\|_S$。
原双线性式
$\mathcal B(Q,h)=u h_1+K v h_2$、$S(Y)=Y_1^2+K Y_2^2$
满足
$$
 \|\mathcal B(Q_\delta,h)\|_S\le C_*t,\quad
 \|\mathcal B(Y,h)\|_S\le A_Srt,\quad
 \|S(Y)\|_S\le A_Sr^2.                                  \tag{C.14}
$$
四个 primitive 项在乘 $b_*$ 前，按 P.12 的原顺序至多为
$$
 8C_*^2 A_Srt,\quad 8C_*^2 A_Srt,\quad
 8C_*A_S^2r^2t,\quad
             8C_*^2A_Srt+4C_*A_S^2r^2t .
$$
两个 gamma mean 项合计在乘 $g_*$ 前不超过 $4rt$。
P.13 的全部 ordinary mean 项在乘 $b_*$ 前合计不超过
$$
                  (8C_*+4C_*A_S+6A_S)rt .
$$
因此 C.6 和 $r\le1$ 给一个统一安全界
$$
 \|\widehat{a_Y(h)}\|_S+\|\widehat{b_Y(h)}\|_S
                   <2^{11}C_*^2A_S^2rt .                \tag{C.15}
$$
包括两个方向的独立 even mean；没有用反射奇性删除应有项。
每一 primitive 均为 C.7，不替换成裸 $I_\theta$。

把 $h$ 写为 $\widehat h=\mathcal Hx$，由 C.10--C.12，
完整 fixed-angle 主体差 $\mathcal V_Y$ 满足
$$
 \|\mathcal V_Yx\|_{\mathfrak D_S,\rm body}
 <2^{15}C_*^6A_S^2r\|x\|_S
                       <2^{1572864}r\|x\|_S .          \tag{C.16}
$$
最后只需
$6\cdot212992+2(8212+1)+15<1572864$。
此式无 $Y_r$、无新 $R_Y$ Hessian；原 $R_0$ Hessian 和固定
$D\Psi_0$ 的径向导数已完整留在原基逆。

## 5. 一个可反复使用的明确主体球

Q.2 已给同一真实 $\delta$ 处
$$
 \|\mathcal G_\delta^{\rm true}:
       \mathfrak D_S\to\mathfrak M_S\|<2^{4194304}.
                                                                  \tag{C.17}
$$
这里继续保留该 $\delta$ 处完整真实外端线性行、固定内端非mean
$C$、全部 mean/height 和 jump。对主体变化定义
$$
 \mathcal K_Y=\mathcal G_\delta^{\rm true}\mathcal V_Y .
$$
由 C.16--C.17，
$$
                  \|\mathcal K_Y\|<2^{5767168}r .        \tag{C.18}
$$

将未知状态参数化为固定线性坐标
$$
 \widehat Y=\mathcal Hz,\qquad
       \|z\|_S\le R_*:=2^{-8388608}.                     \tag{C.19}
$$
C.10 保证 $r<1$，且 C.18 可统一写成
$$
 \|\mathcal K_{\mathcal Hz}\|
       <C_{\rm nl}\|z\|_S,\qquad C_{\rm nl}=2^{6291456},
 \qquad C_{\rm nl}R_*=2^{-2097152}<1/2 .                 \tag{C.20}
$$
其中 $5767168+425986<6291456$。

于是原完整 fixed-angle 主体方程，在 C.19 每一点都有同一
source/solution 阶上的解算子
$$
 (I-\mathcal K_Y)^{-1}\mathcal G_\delta^{\rm true},
 \qquad
 \|(I-\mathcal K_Y)^{-1}\mathcal G_\delta^{\rm true}\|
                                      <2^{4194305}.     \tag{C.21}
$$
这是保留原完整线性外行的主体邻域结论。
使用原完整兼容性块时，其荷变量和方程照旧保留；若指定为齐次
物理荷，仍须满足原真实兼容性条件。
这里没有把一般源的 mean 或荷投影为零来制造可解性。

为明确这个增广读出，若原完整逆写成
$(G_{\rm state},G_{\rm charge})$，先解
$x=G_{\rm state}(d+\mathcal V_Yx)$，再以**同一个完整源**
恢复 $c=G_{\rm charge}(d+\mathcal V_Yx)$。
C.17--C.23 的范数指 state 分量；原独立荷列按原合同恢复，
不是一个新无偿状态输入。真实齐次物理问题还要求恢复的 $c$
满足其原零荷或匹配行。因而本篇不把仅兼容源上的逆偷偷延拓为
删去荷的逆，也不声称扰动后的实际零荷条件可由旧条件代替。

实际反射子空间由原方程的不变性和唯一性继承。一般全四重周期
方向还须原角相位行；C.21 不将该行等同于径向 $\Gamma$。

## 6. 主体非线性余项在同一个 Banach 模块中闭合

令 $\mathcal R_\delta(z)$ 为 N.4--N.6 的**完整**
quadratic/cubic 主体余项，经同一固定 $D\Psi_0$ 写成 C.11 的
divergence 势及 ordinary 源。其自变量是
$Y$，其中 $\widehat Y=\mathcal Hz$。
原径向微分和全部保留的线性边界行在这个余项中准确消失；
没有隐藏 nonlinear boundary 项。

沿实线段积分 C.20，得到
$$
 \|\mathcal G_\delta^{\rm true}\mathcal R_\delta(z)\|_S
               \le\tfrac12 C_{\rm nl}\|z\|_S^2,          \tag{C.22}
$$
以及对 $\|z_i\|_S\le R\le R_*$，
$$
 \|\mathcal G_\delta^{\rm true}
       [\mathcal R_\delta(z_1)-\mathcal R_\delta(z_2)]\|_S
                 \le C_{\rm nl}R\|z_1-z_2\|_S .         \tag{C.23}
$$
线段始终留在同一个明确球；未知频率无需截断。
式中的完整源按原兼容性块解释，实际 mean 由 N.7/P.7 保留。
若另外消去荷，则必须先解其真实方程，不能将 C.22 作为删除荷的许可。

这补齐了原 P 第7节所缺的同域系数控制：
有限正则解输出 $\mathfrak M_S$ 自己通过 C.2--C.3 控制全部
nonlinear coefficient 产品，不再要求每一步未知输出重新具有角解析性。
angular divergence 由已付的原专用输入列消费，故 C.22--C.23
不损失角导数。

## 7. 与未完成全局问题的准确连接

C.21--C.23 是真实全实 $\delta$ 区间上的完整正帽**主体**邻域。
它同时保留 nonsolution $Q_\delta$ 的身份和原 residual Hessian。
没有在本篇证明原实际 residual、inner port 或外高度缺陷落入
如此小的可迭代球。

下一项必须为任意 C.19 状态构造同一 finite-Sobolev 的真实
nonlinear long 图，保留它的 weighted mean、holonomy 小根、
独立 height 和全部非mean 两行，并把其一阶差及二次余项加入
同一 source norm。仅有各点的有界线性外逆不足以给这项。

径向 $C_t^4$ 仍需实际 PDE、真实单侧迹及相应源 jets 重建；
ordinary $L^2_rH^S$ 数据没有自动得到该正则性。
内区全无限反馈、strong return、cutoff97、完整 $\nu$ Schur、
尾部残差域、全族 matching 和 README 几何完成标准继续保留。
本篇不宣称最终精确闭等距族。
