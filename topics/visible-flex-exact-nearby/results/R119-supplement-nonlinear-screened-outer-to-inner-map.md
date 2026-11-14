# R119 续篇：实际长正段的非线性外输入筛选与内端全高角宽

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 固定已经延到 $u=B$ 的真实非线性尾的内端高度，
在 R74 同一个长正段改变外端的全部非mean Dirichlet 数据。
本篇构造真实非线性响应，并证明内端完整 Neumann 响应有
$17e^{-L/2}$ 的强算子界，同时从外端物理角宽 $1/512$ 获得内端已经
支付的宽度 $\tau+1968$。所有 Fourier 模和 mean 小根保留。

这个结论支付的是实际 nonlinear outer forcing 到内端匹配式的部分，
不是混合尾自身的非线性相对高输入逆。它不把尾标签的绝对小余项
除以一个未控制的高模幅度。

## 1. 固定实际两端、真实尾高度和已有非线性解

沿用 [双 bump 续篇](R119-supplement-two-bumps-and-exact-nonlinear-matching.md)
的同一个已选双 bump 及同一个 exact-tail chart。记
$$
 \sigma_o=1/512,\qquad \sigma_i=\tau+1968,
 \quad \tau=5177/400,\qquad
 L=\omega(2^{24}-25/8),\quad 7/5<\omega<3/2.
 \tag{N.1}
$$
固定任意真实/复标签 $a$，$\|a\|_{\ell^1_{8192}}<1/4$。
其内端非mean相对高度 $f_B(a)$ 满足
$$
 \|f_B(a)\|_{\sigma_i,2}<2^{-8423}X_\beta<2^{-8423}.
 \tag{N.2}
$$
先以外端高度0解 [长段非线性 Dirichlet 问题](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)，
使用同一个常角宽 $\sigma_i$。记所得真实完整非mean解为 $h^0$。
由该篇 $\|h^0\|\le16\|f_B\|+2^{14}\|h^0\|^2$ 和解球 $2^{-20}$，
$$
 \|h^0\|_{\mathcal Y_{\sigma_i}}
 \le\frac{1024}{63}\|f_B\|_{\sigma_i,2}
 <17\|f_B\|_{\sigma_i,2}<2^{-8418}=:r_0.
 \tag{N.3}
$$
全部 mean 沿其完整 holonomy-one 小根重建，内端平均高度取真实尾给出的
$\lambda_B$。这里的 $h^0$ 已经存在，不是一个未证背景假设。

## 2. 支付实际可用的变化角宽与径向权

取准确参数
$$
 \eta=\frac14,\quad \alpha=\frac12,\quad
 S=4(\sigma_i-\sigma_o),\qquad
 \sigma(t)=\sigma_o+\frac14\min\{L-t,S\},
 \qquad q(t)=e^{(L-t)/2}.
 \tag{N.4}
$$
实际 $S<8000<L$，故 $\sigma(0)=\sigma_i$、$\sigma(L)=\sigma_o$。
没有调用比真实 $f_B$ 更宽的输入；$\sigma(t)\le\sigma_i$ 始终成立。
宽度在一个点折角无害，因为下面直接比较权比，不微分宽度。

令 $M=|m|\ge4$，定义完整强 norm
$$
 \|z\|_{\mathcal Y_W}
 =\sum_{m\ne0}\bigg[
 M^2\sup_t q(t)e^{\sigma(t)M}|z_m(t)|
 +M\sup_t q(t)e^{\sigma(t)M}|z_m'(t)|
 +\sup_t q(t)e^{\sigma(t)M}|z_m''(t)|\bigg].
 \tag{N.5}
$$
源 norm 为
$\|F\|_{\mathcal F_W}=\sum_{m\ne0}\sup_tq(t)e^{\sigma(t)M}|F_m(t)|$。
mean 分量使用相同 $q(t)$，不乘一个非零 Fourier 频率因子。

去掉 $q$ 得到 $\mathcal Y_{W_0}$；它被 $\mathcal Y_W$ 连续嵌入，
而已构造的 $h^0$ 在 $\mathcal Y_{W_0}$ 中 norm 小于 $r_0$。
同一时刻的 Fourier 乘法满足准确的理想估计
$$
 \|fg\|_{W}\le\|f\|_{W_0}\|g\|_{W},\qquad
 \|fg\|_W\le\|f\|_W\|g\|_W,
 \tag{N.6}
$$
其中先每模取径向 sup，再求和。第一式把增长的径向权放在一个指定的
扰动因子上；它没有错误地让固定内端背景也乘 $e^{L/2}$。

## 3. 同一有限区间 Green 的全频带权界

继续使用前篇的准确有限区间核
$$
 G_M(t,s)=-e^{2(s-t)}
 \frac{\sinh(M\min(t,s))\sinh(M(L-\max(t,s)))}{M\sinh(ML)}.
 \tag{N.7}
$$
未加权的核及一阶导分别小于
$M^{-1}e^{-M|t-s|+2(s-t)}$ 和
$3e^{-M|t-s|+2(s-t)}$。

若 $t\ge s$，由 $\sigma$ 单调不增，乘权比后该指数核至多
$e^{-(M+5/2)(t-s)}\le e^{-M(t-s)}$。
若 $t<s$，由 $\sigma(t)-\sigma(s)\le(s-t)/4$，该核至多
$$
 e^{-[(3/4)M-5/2](s-t)}\le e^{-(M/8)(s-t)},
 \tag{N.8}
$$
因为 $M\ge4$。

两个半核分别积分，得到
$$
 M^2\|\mathcal G_DF\|_{W,m}\le9\|F_m\|_W,
 \qquad M\|\partial_t\mathcal G_DF\|_{W,m}\le27\|F_m\|_W.
$$
再由准确 ODE $H''=F-4H'+(M^2-4)H$，二阶项至多
$1+4\cdot27/4+9=37$ 倍源 norm。于是
$$
 \boxed{\quad
 \|\mathcal G_D\|_{\mathcal F_W\to\mathcal Y_W}<128,
 \quad}                                                     \tag{N.9}
$$
因为 $9+27+37=73<128$。这个界不依赖真实 $L$ 的巨大数值。

只有外端数据 $f$、内端为0的准确 lift 是
$$
 (z_D)_m(t)=e^{2(L-t)}\frac{\sinh(Mt)}{\sinh(ML)}f_m.
$$
由 $\sigma(t)-\sigma_o\le(L-t)/4$，同一指数比较仍给
$$
 \|z_D\|_{\mathcal Y_W}\le16\|f\|_{\sigma_o,2}.
 \tag{N.10}
$$
全部有限长度反射项保留，没有换成半线核。

## 4. 完整 mean 的带权差分，避免假用普通全纯界

为使 (N.6) 可以用于真非线性，而非只用于多项式近似，说明完整小根
及源的差分常数。仍用
$$
 P=h_\theta,\quad U=h_{\theta\theta},\quad
 K_\perp=2h+h_t,\quad V=2h_\theta+h_{t\theta},
 \quad K=K_\perp+K_0(h).
$$
记归一化 mean 方程为 $\mathfrak M(K_0,h)=0$，其完整公式见源 R25
(2.3)。令 $T=2K+K^2+EP^2$、$J=(1-w^2T)^{-1/2}$、$S_0=1-w^2P^2$。
该式可写成
$$
 \mathfrak M=\left\langle
 (J-1)/w^2+(1+K)UJ/S_0\right\rangle.
 \tag{N.11}
$$
$(J-1)/w^2$ 使用无 $w^{-2}$ 损失的幂级数，在 $w=0$ 也有极限。

若完整四状态和 norm 为 $N\le1/64$，则
$\|T\|<3N\le3/64<1/16$、$\|J\|<2$、$\|S_0^{-1}\|<2$。
展开第一项并保留线性 $K$，次数至少2的余项的导数至多
$11N\|\dot{(P,K,U)}\|$：平方项至多 $2N$，其余项使用
$$
 \sum_{n\ge2}n c_n x^{n-1}
 \le\frac38\frac{x(2-x)}{(1-x)^2}\le x,
 \qquad 0\le x\le1/16,
$$
以及 $\|\dot T\|\le3\|\dot{(P,K,U)}\|$。
这里 $c_n=\binom{2n}{n}/4^n\le3/8$（$n\ge2$）。

写 $B=(1+K)J/S_0-1$，则 $\|B\|\le11N$、
$\|\dot B\|\le17\|\dot{(P,K,U)}\|$。第二项的零线性平均是
$\langle U\rangle=0$，所以其导数余项至多 $28N\|\dot{(P,K,U)}\|$。
合计为 $39N$。R25 已付
$|\mathfrak M_{K_0}-1|\le9\mathcal R\le9/64$，因而
$$
 |\dot K_0|
 \le46N\big(\|\dot P\|+\|\dot U\|+\|\dot K_\perp\|\big).
 \tag{N.12}
$$
这些是完整的系数绝对和与逆级数界；用 (N.6) 把 $W$ 权放在每个
带点的因子上即可，未带点因子在 $W_0$ 估计。所以 (N.12) 在当前
变角宽、径向强 norm 中同样成立，不靠一个忽略理想结构的抽象 Cauchy 界。

若 $\|h\|_{\mathcal Y_{W_0}}\le s\le1/2048$，则
$N<4s$，且三项非mean变分的和至多 $13\|\dot h\|_{\mathcal Y_W}/8$。
所以
$$
 \|\dot K_0\|_W\le299s\|\dot h\|_{\mathcal Y_W}
 <512s\|\dot h\|_{\mathcal Y_W},\qquad
 \|\dot{(P,K,U,V)}\|_W<4\|\dot h\|_{\mathcal Y_W}.
 \tag{N.13}
$$
完整非mean二次源仍为
$$
 \mathcal Q(h)=\Pi_\perp
 \frac{E(V-P)^2+K^2+2EKU+EU^2-w^2P^2}{1+K+EU}.
$$
分子导数至多 $16N\|\dot{(P,K,U,V)}\|$，分子本身可宽松取
$16N^2$，分母逆小于2；微分逆后总费至多 $34N$，更可取 $64N$。
因此在任意同一个 $s$ 球中，完整源有足够的带权差分界
$$
 \boxed{\quad
 \|\mathcal Q(h)-\mathcal Q(g)\|_{\mathcal F_W}
 \le2048s\|h-g\|_{\mathcal Y_W}.
 \quad}                                                     \tag{N.14}
$$
mean 投影、小根和非mean投影全包含，未使用 Fourier 截断。

## 5. 固定真尾内端后的实际非线性响应

取准确数
$$
 r=2^{-24},\qquad \|f\|_{\sigma_o,2}\le r/32=2^{-29}.
 \tag{N.15}
$$
求 $h=h^0+z$，其中 $z(0)=0,z(L)=f$。完整方程等价于
$$
 z=z_D+\mathcal G_D\{\mathcal Q(h^0+z)-\mathcal Q(h^0)\}.
 \tag{N.16}
$$
在 $\|z\|_{\mathcal Y_W}\le r$ 中，
$\|h^0+z\|_{\mathcal Y_{W_0}}<2r\le1/2048$。
由 (N.9)、(N.14)，右侧非线性部分的 Lipschitz 常数至多
$$
 128\cdot2048\cdot2r=1/32.
 \tag{N.17}
$$
齐次部分至多 $r/2$，非线性部分至多 $r/32$，所以自映且收缩。
所得真实全频 $z$ 满足
$$
 \|z\|_{\mathcal Y_W}
 \le\frac{512}{31}\|f\|_{\sigma_o,2}<17\|f\|_{\sigma_o,2}.
 \tag{N.18}
$$
与前篇无权/同宽解的唯一性比较，得到它正是同一实际非线性 Dirichlet
解，不是另一个加权近似。实性、偶反射、完整 mean PDE 及水平 coframe
由相同的已证重建保留。

对两组允许的外数据 $f,g$，相减后的同一收缩给
$$
 \|z[f]-z[g]\|_{\mathcal Y_W}<17\|f-g\|_{\sigma_o,2}.
 \tag{N.19}
$$
这是同一个 nonlinear map 的全高输入强差分，不只估某条单模解。

## 6. 内端完整两迹及 mean 的实际筛选

在 $t=0$，$q=e^{L/2}$、$\sigma=\sigma_i$，且 $z(0)=0$。
所以完整非mean高度差为0，而实际相对 Neumann 差满足
$$
 \boxed{\quad
 \|K_\perp[h^0+z](0)-K_\perp[h^0](0)\|_{\sigma_i,1}
 =\|z_t(0)\|_{\sigma_i,1}
 <17e^{-L/2}\|f\|_{\sigma_o,2}.
 \quad}                                                     \tag{N.20}
$$
同一式对任意两组允许的 $f,g$ 的差成立。物理径向导数还须乘实际
$w_B$；这里保留的是前篇匹配式使用的准确相对单位。

平均高度在内端保持同一 $\lambda_B$。mean 斜率不是设成0：由 (N.12)
在端点使用同一权，以及 $h^0,h^0+z$ 的局部小球，可宽松取
$$
 |K_0[h^0+z](0)-K_0[h^0](0)|
 <2^{11}r\,e^{-L/2}\|z\|_{\mathcal Y_W}
 <e^{-L/2}\|f\|_{\sigma_o,2}.
 \tag{N.21}
$$
最后一步用 $17\cdot2^{11}r<1$。完整外端平均高度差仍是准确输出
$$
 \int_0^L aw\,[K_0(h^0+z)-K_0(h^0)]\,dt,
 \tag{N.22}
$$
不能把这个外端量也误乘内端的 $e^{-L/2}$。
真实 grounded/normal 输出仍使用同一水平位移与 shear 公式；本篇没有
把高度导数重命名为动量。

## 7. 已付与仍缺的算子部分

令 $\mathcal F(a,f)$ 为双 bump 续篇 (B.14) 的实际非线性匹配算子。
本篇证明，在固定任意已许尾标签 $a$ 时，
$$
 \|\mathcal F(a,f)-\mathcal F(a,g)\|_{\sigma_i,1}
 <17e^{-L/2}\|f-g\|_{\sigma_o,2},
 \tag{N.23}
$$
并保留 (N.21)–(N.22) 的 mean 负荷。
所以真实 nonlinear outer forcing 已有明确的强角宽与径向筛选费用。

仍需解的是 $\mathcal F(a,f)=0$ 对尾标签 $a$ 的全高相对逆。
本篇控制的列是外数据 $f$，不把它混同于尚未支付的 $D_a\mathcal F$。
ordinary metric-source 列若加入，也须按真实两迹和 mean 接线另证，
不能由本篇齐次精确度量结论删除源行。

[准确门程序](../scripts/fourfold_nonlinear_screening_20261113.py) 与
[完整报告](../notes/2026-11-13-R119-nonlinear-screening-budget.json)
核实际角宽、全 Green 常数、完整 mean 差分、收缩及真实筛选门。
