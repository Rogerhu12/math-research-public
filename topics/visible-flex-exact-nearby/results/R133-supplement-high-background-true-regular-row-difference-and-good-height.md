# R133：有限高正则背景上的真实 regular 外行差与良切向源

2026-11-15，visible-exact-astra-0df9。

**结论范围。** 本篇只证明真实 regular 外边界微分的有限阶背景差。
固定原 $\eta_0$、实 $|\delta|\le10^{-8}$，基点同时固定为原
$\mathcal G_\delta^{\rm true}$ 已使用的 $(Q_\delta,y_{B,\delta})$：
$Q_\delta$ 是原显式连续修补族，$y_{B,\delta}$ 是
[T](R133-supplement-full-delta-fixed-angle-regular-graph-analytic-translation.md)
实际构造并识别的已知解析 long 背景的外高度迹。不能只指定
$Q_\delta$，再把任意未知高度下的线性逆命名为原
$\mathcal G_\delta^{\rm true}$；也不在本篇擅自令 $y_{B,\delta}=0$。

未知帽背景在固定角中有 $\mathfrak M_{8212}$ 正则性。对方向和源只授予
整数 $1\le S\le8192$ 的完整外行，保留 $H^{S+2}$ good-height 输入、
两个曲率 mean、常高度和原相容性荷。安全的背景差系数为
$2^{2097152}$，见 (B.22)。这不是 $\mathfrak M_{8212}$ 未知的同域闭合，
不是 raw-height 的同域二阶可微结论，也不以一个极小邻域本身证明实际
残差已落入该邻域。

本篇只推导原完整方程的符号估计；没有重算任何 target、long 解、
原帽格、矩阵传播子或 Actions 数值。

依赖另包括 [C的完整主体邻域](R133-supplement-finite-Sobolev-nearby-cap-body-inverse-and-same-space-remainder.md)、
[F的真实曲率有限 jets](R133-supplement-cap-finite-Sobolev-ball-to-physical-curvature-jets.md)
与 [Q的真实帽逆高阶窗口](R133-supplement-high-finite-Sobolev-window-for-the-true-full-delta-cap-inverse.md)。

## 1. 固定角、基点与高背景距离

写 $x=\theta_0$，固定 $\varphi=\Phi_0(R,x)$，$R=25/8$，
$\omega_0=\partial_x\Phi_0(R,x)$。所有帽场先在同一个 $\Phi_0$ 下拉回：
$\widehat Q=(\widehat u,\widehat v)$。定义
$$
 \Pi_{\varphi,0}f=\langle\omega_0f\rangle_x,\qquad
 m=\Pi_{\varphi,0}\widehat v<0,\qquad
 \tau(x)=\Theta_Q(R,\Phi_0(R,x)),\qquad
 j=\tau_x=\frac{\omega_0\widehat v}{m},\qquad \langle j\rangle_x=1 .
 \tag{B.1}
$$
原角相位由原 $I_\varphi$ 规范决定，不能另挑一个方便的常数。
令 $I_{\varphi,0}=C_{\Phi_0}I_\varphi C_{\Theta_0}$；它的准确系数、完整
$\Pi_{\varphi,0}$ 和 primitive 费用来自固定基点 P、C 及 U，而非裸复合
在未知复方向上的延拓。

沿用 T 的
$$
 M_jf=\langle jf\rangle_x,\qquad J_jf=f-M_jf,\qquad
 D_j=j^{-1}\partial_x,\qquad
 I_jf=I_x\{j(f-M_jf)\}-M_jI_x\{j(f-M_jf)\}.
 \tag{B.2}
$$
ordinary chart 始终使用 $P_{\perp,x}$。例如
$J_jP_{\perp,x}c=c-M_jc$；不能将 $M_j$ 换成 ordinary mean。

写
$$
 \widehat Q=\widehat Q_\delta+\widehat Y,\qquad
 d_Q=\|\widehat Y\|_{\mathfrak M_{8212}},\qquad
 d_B=\|y_B-y_{B,\delta}\|_{H^{8197}},\qquad
 D=d_Q+d_B .
 \tag{B.3}
$$
这里 $y_B=P_{\perp,x}(f_B\circ\tau)$ 是实际 ordinary 高度背景；
常高度另列。主结论先在 $D\le2^{-4096}$ 的真实连通邻域证明。
帽 C 的 $z$ 球通过已付 $\widehat Y=\mathcal H z$ 给
$d_Q\le2^{425986}\|z\|_{\mathfrak M_{8212}}$，但不自动给 $d_B$。
未知 tail 高度变化必须作为独立背景费保留。

基点高度和其曲率、小根、完整 $C_R$ 反演、真实有限长反射，均是 T
已经构造的同一对象。T 给原已知背景的 joint 强 Wiener 界
$30F<2^{-24}$，$F=111/10^{11}$，在宽 $1/512$ 一致成立。
本篇使用这个实际已付基点界，不把 T 中允许的高度球
$\bar b=10^{-11}$ 偷换成更小的 $2^{-60}$ 球。

## 2. 原方程的 good differential 和 off-shell 行

令 $W_Q^\flat=(B_Q^\flat,C_Q^\flat)$。帽方向
$\widehat h=(\widehat h_1,\widehat h_2)$ 在固定 $\Phi_0$ 下给
$$
 \dot m=\Pi_{\varphi,0}\widehat h_2,\qquad
 \eta_H=I_{\varphi,0}
 \left(\frac{\widehat h_2}{m}
             -\frac{\widehat v\,\dot m}{m^2}\right),\qquad
 b_H=\eta_H/j,\qquad \dot j=(\eta_H)_x .
 \tag{B.4}
$$
$\Pi_{\varphi,0}\eta_H=0$ 是原 phase 规范；它一般不是
$\langle\eta_H\rangle_x=0$。完整 good curvature 方向为
$$
 \mathcal G_Q\widehat h
 =P_Q\widehat h-\eta_HD_jW_Q^\flat,\qquad
 P_Q=
 \begin{pmatrix}C_Q^\flat&-B_Q^\flat C_Q^\flat\\
                 0&-(C_Q^\flat)^2\end{pmatrix}.
 \tag{B.5}
$$
这是
[U的完整未知角良切向恒等式](R133-supplement-exact-unknown-outer-angle-good-tangent-and-full-means.md)
的同一两个均值、同一 primitive 规范和同一物理角导数。

令 $\Gamma_j$ 表示拉回后的真实 nonlinear regular graph：
给定 ordinary 非mean 曲率输入和 ordinary 高度输入，求解完整 long
方程、holonomy-one 小根和真正 $C_R$ inverse，再读出全 $B_R$、
$C_0=M_jC_R$ 及 $B_0=M_jB_R$。记实际背景残差
$$
 R_{Q,B}=B_Q^\flat-\Gamma_{j,B}(P_{\perp,x}C_Q^\flat,y_B).
 \tag{B.6}
$$
完整 mean 匹配还有
$M_jC_Q^\flat-\Gamma_{j,C_0}$；常高度、metric/label affine 荷继续独立。

定义 good derivative $\nabla_H=\dot{\ }-b_H\partial_x$。准确恒等式为
$$
 \nabla_HD_j=D_j\nabla_H,\qquad
 \delta M_jf=M_j(\nabla_Hf),\qquad
 \nabla_HI_jf=I_j\nabla_Hf .
 \tag{B.7}
$$
第二式由 $\dot j=(j b_H)_x$ 在整个圆周分部积分得到；第三式还使用
完整 weighted mean 规范。没有丢弃小根 $\dot\kappa$ 或 mean 高度。

令 $c=(\mathcal G_Q\widehat h)_C$、
$b=(\mathcal G_Q\widehat h)_B$。用规范化 good-height 源
$$
 k_B=J_j|D_x|^{-2}g_B,\qquad g_B\in H^S_\perp
 \tag{B.8}
$$
表示物理高度方向；常高度另列。在同一个 $j$ 方程上微分
$\Gamma_j$，good 非mean 行和两个 mean 行为
$$
 \begin{split}
 {\cal R}_{Q,B}^{\rm good}[\widehat h,g_B]
   &=b-D\Gamma_{j,B}
           [P_{\perp,x}c,\ |D_x|^{-2}g_B],\\
 {\cal R}_{Q,B_0}[\widehat h,g_B]
   &=M_jb-D\Gamma_{j,B_0}
           [P_{\perp,x}c,\ |D_x|^{-2}g_B],\\
 {\cal R}_{Q,C_0}[\widehat h,g_B]
   &=M_jc-D\Gamma_{j,C_0}
           [P_{\perp,x}c,\ |D_x|^{-2}g_B].
 \end{split}
 \tag{B.9}
$$
$D\Gamma_j$ 在这里对同一固定 $j$ 的 good 数据求导；由 (B.7) 和真实
坐标协变性，所有 $\dot j$ 项已经准确转入 good 方向，不能又在右侧
重复加入一个不相关的 chart 导数。

实际 nonlinear boundary 使用的坐标可取
$(P_{\perp,x}R_{Q,B},\,M_jR_{Q,B},\,M_jC_Q^\flat-\Gamma_{j,C_0})$。
它的真正 raw 微分是
$$
 \begin{split}
 \delta P_{\perp,x}R_{Q,B}
 &=P_{\perp,x}
       \{ {\cal R}_{Q,B}^{\rm good}+b_H\partial_xR_{Q,B}\},\\
 \delta M_jR_{Q,B}&={\cal R}_{Q,B_0},\\
 \delta(M_jC_Q^\flat-\Gamma_{j,C_0})&={\cal R}_{Q,C_0}.
 \end{split}
 \tag{B.10}
$$
所以 off-shell 项 $b_HR_{Q,B,x}$ 必须保留在非mean raw 行。
物理 scalar mean 已由 (B.7) 完整微分，不能再加一份该 transport。
在反射类 $B_0$ 准确消失时才可限制；本证明先保全 $4\mathbb Z$。

本篇最终使用的 source 坐标固定于基点 $(Q_\delta,y_{B,\delta})$：
令 $\mathcal K_{\partial,\delta}$ 为原完整基逆的准确边界荷转换，
$\mathcal H_0=(D\Psi_0)^{-1}$。定义
$
 \mathfrak B_{Q,y_B}(x,g_B)
  =\mathcal K_{\partial,\delta}\,
        D_{\rm actual}{\cal F}_{\partial,Q,y_B}
                  [\,\widehat h=\mathcal H_0x,\ g_B\,] .
 \tag{B.10a}
$
这里 $D_{\rm actual}{\cal F}_\partial$ 就是 (B.10) 的完整非mean和
两个 weighted mean 行。$\mathcal K_{\partial,\delta}$ 是原
[O的完整 affine 行转换](R133-supplement-true-full-delta-outer-rows-in-fixed-base-cap-inverse.md)
及 Q source block 使用的固定变换；它保留原 source 单位和全部荷，
不重新取当前 $Q$ 的 nonlinear normalization factor。
因此对附近背景是固定输出变换后的真实 boundary differential。
若另用当前 $p_Q=q_*/(-m)$ 的 Robin 表示，必须保留其全部准确 chart；
若还对一个当前因子乘 nonlinear residual 后求导，其
factor-derivative times residual 也必须另保。

## 3. 在零宽 Banach 代数上的真实局部全纯性

这里用 $\ell^1$ Fourier 系数及原逐 mode 径向 sup 的强 Wiener
$\mathcal Y_A,\mathcal F_A$，不是未知函数的 complex angle composition。
原 constant-coefficient Green 的每 mode 绝对核、卷积和 weighted mean
给与 T 相同的 $32$、$9$、$4$ 门；这些核首先作用于完整
$\ell^1(C_t)$，不交换 $\sup_t$ 和频率和。

需要的方程正是 T.10、T.12、T.15、T.20：
$D_j$ 与 $J_j$ 形成 $P,U,K_\perp,V$，同一个可去 holonomy 商给
$\kappa$，再用完整 nonlinear 曲率 $C_R$ 解右端数据。
在已知基点及其 $|a|\le1/1024$ 平移上，有以下余量：

| 对象 | 已付统一门 |
| --- | --- |
| 强背景 | $\|y_\delta\|_{\mathcal Y_A}<30F<2^{-24}$ |
| 坐标 | $\|j_\delta-1\|<2^{-26}$、$\|(j_\delta)_x\|<2^{-18}$ |
| Dirichlet 线性化 | inverse $<64$，两 lift $<8,4$ |
| 单端 ordinary Green 导数 | $<4$，使用原 constant Green |
| 真实 $C_R$ derivative inverse | $<18$ |
| 基点 endpoint | $5.8<|m_\delta|<8$，完整 even chart inverse $<1/8$ |

例如把坐标邻域宽放至
$\|j-1\|_{A^0}<2^{-20}$、$\|j_x\|_{A^0}<2^{-14}$，
就有 $\|{\cal V}_j\|<2^{-14}$，从而
$$
 32(2^{-11}+2^{-14})<1/32,\qquad
 9\{16(2^{-11}+2^{-14})+4\,2^{-8}+2^{-14}\}<1/2 .
 \tag{B.11}
$$
这仍给真实两个 inverse 的 $64$ 和 $18$；不是将旧裸 Fourier
reference 的 inverse 重命名。

为明确局部全纯量词，取数据范数
$A^1(\widehat Q)\oplus\dot A^2(y_B)$。在基点状态的
$2^{-30}$ 强 Wiener 邻域及相应数据邻域上，所有 reciprocal、平方根
和 holonomy 可去商的分母都离零，$|m|>3$，
$\|y\|_{\mathcal Y_A}<2^{-20}$。原绝对级数逐项给原方程和曲率 map
的统一界 $2^{32}$。对这一个 Banach 球作 Cauchy，两阶微分可统一
取 $2^{128}$；完整基点 block inverse 可宽放为 $2^{32}$。
因此在状态半径 $2^{-256}$、数据半径 $2^{-512}$ 上，Newton 固定点的
导数界小于 $2^{32+128-256}<1/2$；数据一阶费用可取 $2^{64}$，
所以初始状态位移小于 $2^{32+64-512}=2^{-416}<2^{-256}/2$。
这里使用的是有限数据曲线的复参数，不要求未知背景有复角延拓。

这构造同一个真实 nonlinear long 解、其 holonomy 小根及 $C_R$
inverse；实重叠域由原唯一性识别。所有 first derivatives 对输入的
归一化都是 $A^0$ 曲率和 $|D_x|^{-2}A^0$ 高度。完整两个 mean、
constant-height gauge 和 original affine source block 均保留。
在下面的 row family 中，**先**预合 (B.10a) 的固定
$\mathcal H_0$ 和 $\mathcal K_{\partial,\delta}$，再做有限 jets。
$\mathcal H_0$ 的准确式是 C.9 的
$S'x-S'vW_\theta I_\theta(c-mC\langle c\rangle)$；
C.4 的已合并系数都有 joint $A_{1/128}$ 界 $2^{32}$，
所以其零宽平移族可宽放为 $2^{80}$。
固定原 source 转换只取 O 的端点 affine right-inverse、固定
$D\Psi_0$ 端点式及 T 的 mean/Hilbert 行，不包含任何 cap Green inverse；
这些端点乘法、primitive、Fourier multiplier 和有限秩读取在
$|a|\le1/1024$ 上有粗界 $2^{128}$。不能在这里调用只在
$2^{-128}$ strip 上已付的完整 $G_0$ 平移族。
这些已知系数也随共同 $a$ 平移，
不能在 commutator 中冻结。完整预合以后，所有 finite chart、
primitive、真实 even inverse、两个 mean 和输出读取仍可合并为
$
 K_{\rm row}<2^{4096}
 \tag{B.12}
$$
的 uniform bounded holomorphic good-row family。下面给出其中
Hilbert 项的独立 $A^0$ 门，避免以一个 $L^2$ 结论冒充 Wiener 门。

T 的固定 $\Phi_0$ Hilbert 共轭只在真正端点 $R$ 使用。
对消极点后的差核，同时允许 $x,y$ 各有 $2^{-14}$ 的独立虚部，
并允许共同已知平移 $|a|\le1/1024$。两域之和仍严格落在原
$1/512$ 条带内。T 的 $\|e'\|,\|e''\|<1/16$ 与准确 pole cancellation
在 complex diagonal 可去；同一积分式给差核绝对值小于2。
其双 Fourier 系数因而由
$2\exp[-2^{-14}(|m|+|n|)]$ 支配。对输出频率求全和给
$A^0\to A^0$ norm 小于 $2^{18}$；加原 Hilbert 的1仍可取
$2^{32}$。这里只延拓已知核，不单独延拓 $C_\tau$。
其余因子由 (B.1)–(B.9)、T 的完整 even chart 和有限次有界代数复合
得到，(B.12) 保留很大余量。

## 4. 有限 translation jets 与完整 signed Schur

固定整数 $1\le S\le8192$，令 $N=S+2\le8194$。
对未知差只构造有限多项式
$$
 {\cal Y}(a)=\sum_{k=0}^{N}\frac{a^k}{k!}\partial_x^k\widehat Y,\qquad
 {\cal B}(a)=\sum_{k=0}^{N}\frac{a^k}{k!}
                         \partial_x^k(y_B-y_{B,\delta}) .
 \tag{B.13}
$$
基点 $Q_\delta$、$y_{B,\delta}$、$\omega_0$ 和已知核仍使用其已付
解析平移。令
$m(a)=\langle\omega_0(\cdot+a)v(a)\rangle_x$ 并
$j(a)=\omega_0(\cdot+a)v(a)/m(a)$，使
$\langle j(a)\rangle=1$ 在整个复参数圆盘准确成立。

一维 Fourier Cauchy–Schwarz 给
$\|f\|_{A^0}\le2\|f\|_{H^1}$。所以
$$
 \sup_{|a|\le1/1024}
  \bigl(\|{\cal Y}(a)\|_{A^1}
           +\|{\cal B}(a)\|_{\dot A^2}\bigr)<8D .
 \tag{B.14}
$$
所需最高背景导数分别是 $N+2\le8196$ 和
$N+3\le8197$，正好由 (B.3) 支付。
这里没有计算 $Y(x+ia)$ 或未知 $f_B(x+ia)$；有限 Taylor polynomial
只是具有正确有限 jets 的 Banach 数据曲线。

由 (B.12)、数据半径 $2^{-512}$ 内的 Cauchy 差估计、(B.14) 及
真实平移协变性，完整 good-row difference 满足
$$
 \|\operatorname{ad}_{\partial_x}^q
       (\mathfrak B^{\rm good}_Q-\mathfrak B^{\rm good}_\delta)\|_{A^0\to A^0}
 \le q!\,1024^q\,2^{8192}D,\qquad 0\le q\le S+2 .
 \tag{B.15}
$$
这里两个状态输入分量是 $x$，不是未经转换的 $\widehat h$；
规范化高度列和两 mean 输出均使用这个同一界。固定 $\mathcal H_0$
已经预合，后文不得又免费漏掉它，也不得再重复收费。
这里 $\operatorname{ad}$ 是输入输出同时平移的 commutator。
它只由有限链式法则识别，不能反过来推论未知背景解析。

将 (B.15) 的 $q=0$ 与 $q=S+2$ 同时用于完整 signed Fourier
矩阵条目，使用
$\langle m\rangle^S/\langle n\rangle^S
 \le2^{S/2}(1+|m-n|)^S$。两个 Schur 和都由完整
$(1+|m-n|)^{-2}$ 和支配；scalar mean 视为输出频率0，
输入 mean 的权也准确为1。采用 $q!\le2^{14q}$、
$q\le8194$ 后，
$$
 \|\mathfrak B^{\rm good}_Q-\mathfrak B^{\rm good}_\delta\|
 _{H^S_{x_B}\oplus H^S_{x_C}\oplus H^S_{g_B}\to H^S_\perp\oplus\mathbb C^2}
 <2^{262144}D .
 \tag{B.16}
$$
$g_B$ 的归一化意味着实际 good-height 是 $H^{S+2}$；
$|D|^{-2}$ 只作用非mean，不改变独立常高度。
本步骤没有 Hilbert 方向之积，也没有频率截断。

## 5. off-shell transport 单独收费，避免多失一角

(B.10) 中的 $b_HR_{Q,B,x}$ 不放进 (B.15) 再取 $S+2$ 次
commutator。它是一个真实 zeroth-order 乘法列，直接在已完成的
$H^S$ 空间用 Sobolev 乘法。

由同一个有限数据曲线和真实 background output map，只需
$q\le S+1$ 的有限 jets，便有安全界
$$
 \|R_{\delta,B,x}\|_{H^S}<2^{262144},\qquad
 \|R_{Q,B,x}-R_{\delta,B,x}\|_{H^S}<2^{262144}D .
 \tag{B.17}
$$
此处 $R_{\delta,B}$ 不被设为0；显式帽中心未必与真实 outer 图准确匹配。
(B.4) 的完整 primitive 与 mean 同样给
$$
 \|b_Q\|_{H^S_x\to H^S}<2^{262144},\qquad
 \|b_Q-b_\delta\|_{H^S_x\to H^S}<2^{262144}D .
 \tag{B.18}
$$
这里 $b_Q$ 也先预合 $\widehat h=\mathcal H_0x$。不预合的原
$\widehat h\mapsto b_H$ 还满足同一宽放界，供第7节的实际背景路径使用。
对 $b_Q$ 单独使用相同有限曲线即可：它不依赖高度背景，故其
$S$ 窗口可扩到 $8197$；最高 $S+4\le8201$ 阶帽背景仍在 $8212$ 内。
primitive 实际还多给一角，但本界无需借用一个未支付的 raw-height
方向导数。

准确差是
$$
 b_QR_{Q,B,x}-b_\delta R_{\delta,B,x}
 =(b_Q-b_\delta)R_{\delta,B,x}
                   +b_Q(R_{Q,B,x}-R_{\delta,B,x}) .
 \tag{B.19}
$$
$H^S$ 的乘法费可取 $2^{S+1}$。将 (B.16)–(B.19) 与两个真 mean
合并，完整 fixed-$x$ raw boundary differential difference，已在
(B.10a) 的原 state/source 坐标中，因而有
$$
 \|\mathfrak B_{Q,y_B}^{\,x}-\mathfrak B_{\delta,y_{B,\delta}}^{\,x}\|
       <2^{786432}D,\qquad 1\le S\le8192 .
 \tag{B.20}
$$
所有未知高度背景差仍在 $D$ 内。这里归一化的是当前准确 differential；
若使用 nonlinear normalized residual，须把它自身的 factor-derivative
residual 列放回同一个普通源 block。

## 6. 真实实角与原物理源单位

从 $\mathfrak M_{8212}$、已知基点 joint $A_{1/128}$ 和极小低阶
邻域，原 finite-jet 递推给
$j^{[k]}=\partial_x^kj/k!$ 的界
$|j^{[k]}|<64\,256^k$，在本节所需 $k\le8200$ 内成立；
同一 reciprocal 递推给 $(j^{-1})^{[k]}<2\,2^{16k}$。
这只是有限 jets；并未赋予未知 $j$ 正条带。

可在每个真实点用这些有限 jets 的 Taylor polynomial 做局部 inverse：
在半径 $2^{-20}$ 上，常数线性系数 $j_0>1/2$ 主导其余项，
inverse image 含半径 $2^{-22}$。该 polynomial inverse 的有限 jets
准确等于真实 $\tau^{-1}$ 的 jets。Cauchy 因而给两个真实图的安全界
$|\vartheta^{(k)}|/k!<2^{24(k+1)}$，只取已支付的有限 $k$。
Faà di Bruno 的完整 partitions、真实 Jacobian $1/2<j<2$ 以及
$k!<2^{14k}$ 给
$$
 \|C_\tau\|_{H^s\to H^s},\
 \|C_{\tau^{-1}}\|_{H^s\to H^s}
 <2^{64(s+4)},\qquad 0\le s\le8198 .
 \tag{B.21}
$$
取负密度或 conormal 源时使用
[D的准确密度伴随](R133-supplement-real-angle-full-weak-DN-and-good-density.md)，
不把 scalar composition 当 density transformation。本篇主阶 $S$ 为正。

因此把 (B.20) 的输入和输出统一读回原真实物理单位，包括
good-height 的 $S+2$ 和准确实际实角。固定 $\mathcal H_0$ 与原
source 行转换已经预合并保其平移 jets，不在这里漏计或重复计入，两个实角转换的总费可取 $2^{128(S+6)}$。
$786432+128(8192+6)=1835776<2097152$，故
$$
 \boxed{\ 
 \|\mathfrak B_{Q,y_B}^{\rm true}
       -\mathfrak B_{\delta,y_{B,\delta}}^{\rm true}\|
 <2^{2097152}
       \bigl(\|\widehat Y\|_{\mathfrak M_{8212}}
                   +\|y_B-y_{B,\delta}\|_{H^{8197}}\bigr),
 \quad1\le S\le8192 .\ }
 \tag{B.22}
$$
(B.22) 的状态输入是固定 $x$，输出是原 $\mathfrak D_S$ 的完整边界荷；
其两个实际方向仍用 (B.4)–(B.9) 的同一 good chart 识别。
这不是估计 $\|C_\tau-I\|_{H^S\to H^S}$；该差一般不小。

源输入还须保持其原几何单位：若原高度变量为真实高度 $g$，
$f_B=P_\perp g/(a_Bw_B)$，则该 $1/(a_Bw_B)$ 明确随高度列保留；
本篇不把它吸收入一个与长段尺度无关的1。常高度、mean flux、
两曲率 mean、label 和其他原 affine 荷不投影。

## 7. 固定物理高度时的真实 connection 费用

若沿帽背景曲线固定的是同一个物理 $f_B(\theta)$，则
$y_B(\lambda)=P_{\perp,x}(f_B\circ\tau_\lambda)$。准确有
$$
 \dot y_B=P_{\perp,x}(b_\lambda y_{B,x}),\qquad
 P_{\perp,x}(\dot y_B-b_\lambda y_{B,x})=0 .
 \tag{B.23}
$$
所以 good-height direction 为0，而 ordinary chart 的背景差一般不为0。
完整 weighted 常高度的导数也按 (B.7) 读取，不能另删一个 mean。

定义实际有限高阶背景量
$B_{\rm high}=\sup_{0\le\lambda\le1}\|y_B(\lambda)\|_{H^{8198}}$。
(B.4) 的 finite-jet/primitive 估计与 $H^{8197}$ 乘法给
$$
 \|y_B-y_{B,\delta}\|_{H^{8197}}
 \le2^{524288}B_{\rm high}\,
                 \|\widehat Y\|_{\mathfrak M_{8212}} .
 \tag{B.24}
$$
若只有物理 $H^{8198}$ 高度界，须先用 (B.21) 的实际实角费用；
安全地 $B_{\rm high}\le2^{524928}
\sup_\lambda\|f_B\|_{H^{8198}_\theta}$。这是明确入口，
不是把旧低阶 $Y_{64}$ 或 $\dot A^2$ 上界冒为高阶范数。

只有在另已证明 $B_{\rm high}\le2^{-524290}$ 时，才能把 (B.3)
收为 $D<2d_Q$；这时 (B.22) 仍有足够指数余量保持常数
$2^{2097152}$。否则完整因子
$1+2^{524288}B_{\rm high}$ 必须保留。未知 tail 高度变化还要另加
它自己的 ordinary-chart 背景差，不能借“物理高度固定”的特例消去。

## 8. 与帽基逆和存在性问题的准确接口

(B.1)–(B.24) 是完整外行**差**的结论。这里必须区别两个已经写明的
输出约定：原 S.23、O.9–O.10 的边界行是在固定 physical $\theta$
中对 nonlinear graph residual 微分，再以准确 $D\Psi_\delta$ 拉回；
它对应 (B.9) 的 good 行。若 nonlinear map 选择 (B.10) 随 $Q$ 改变
的 raw $x$ 输出，基点还有
$b_{H,\delta}R_{Q_\delta,B,x}$。目前没有在本篇将这个非零项暗中
包含进旧 $\mathcal G_\delta^{\rm true}$，也不因名称带 true 就认同
两个不同的 boundary differential。

因此下式是一个**条件化的组合接口**。先须证明具有 (B.10a) 同一
raw 输出、同一 $(Q_\delta,y_{B,\delta})$ 和全部源的基逆
$\mathcal G_{\delta,\rm raw}$，并给出其常数
$C_{\rm raw}$。可以单独支付上述基点 residual transport 后建立它；
也可以明确定义固定 physical 输出的另一张 nonlinear map，但后一
选择必须从头保持其准确源坐标，不能与 (B.10) 混用。

因为 (B.10a) 已将方向 $\widehat h=\mathcal H_0x$ 和原准确完整
边界 source 坐标预合进 (B.15)–(B.22)，这里只再收背景
$\widehat Y=\mathcal H_0z$ 的费用。纯帽部分
$d_Q\le2^{425986}\|z\|$ 给
$$
 C_{\rm raw}\,2^{2097152+425986}\|z\| .
 \tag{B.25}
$$
**若另已证明** $C_{\rm raw}\le2^{4194304}$，此式成为
$2^{6717442}\|z\|$，在 $\|z\|\le2^{-8388608}$ 时小于
$2^{-1671166}$。这段算术不反过来证明基点 raw inverse。

组合时还必须同时加入 (B.24) 或独立 $d_B$、帽主体 C 的完整
源 block、全部 mean/height/相容性荷，并保持同一基点，才能得附近
实际线性逆。本篇不把不相容数据免费变成解。

本篇的方向窗口最高 $8192$，背景为 $8212$。因此可在固定高背景处
与 C 组合较低窗口的真实逆，不能声称 $\mathfrak M_{8212}$ 未知
同域闭合，亦不能从 good tangent 推出 raw-height 的同域 $C^2$。

极小球半径不是 actual residual 的证书。即使真实附近线性逆已闭合，
完整 PDE 存在仍需一个确实可进入该球的中心、延续构造或可用低阶
后验常数，以及尚未付的完整 inner/high、参数 Schur、非线性
remainder 和全部 matching。已知显式族、有限193方向误差和一个
粗大全频逆均不能替代这些步骤。
