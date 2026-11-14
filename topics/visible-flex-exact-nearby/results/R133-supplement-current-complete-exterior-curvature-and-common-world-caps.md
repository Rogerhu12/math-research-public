# R133 补篇：当前完整外部的真实曲率及同世界坐标中的平帽

2026-11-14，visible-exact-astra-ac0d。

**状态：已证明当前外部模块的统一几何界及其准确匹配合同。**
本篇使用当前两个 bump、深层平移及形状控制的同一真实度量族，
保全部非零 Fourier 模、holonomy mean 和唯一整体高度常数。
在已证明的真实尾图、有限 connector 和长径向 Dirichlet 球中，
完整外部的主曲率绝对值小于2。若这些模块与主体的完整两迹和
mean 实际匹配，则每个外部点距离同角主体端点小于
$8\cdot10^{-6}$。这个距离只用目标度量，因而在主体使用的同一个
世界坐标中成立，不允许分别重设两个平帽的高度。

本篇没有解尚未完成的无限尾外接口、主体逆或非线性闭合方程。
平帽高度落在固定区间也不等于沿一个尚未构造的参数族逐点固定。
这些范围分别在最后一节保留。

## 1. 当前对象及本篇实际使用的球

取[当前完整 controlled profile 图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
的实参数 $\Pi=(\Gamma,s,\Xi)$。其第129至8192层是同一个
[完整双 bump 图](R119-supplement-two-parameter-full-tail-chart-reconstructed.md)
的前缀。第8193层起才使用 $2^{128}$ 首剪切、下降坡平移和
$C^4$ 形状控制。这里不把旧单 bump 或零标签几何直接转授。

用 $\mathbf a$ 记内部标签，用 $a$ 记物理半径。令
$$
 X=\|X_\Pi(\mathbf a)\|_{\mathcal X_{224}},
 \qquad \|\mathbf a\|_{\ell^1_{224}}<1/64,
 \qquad X<16\|\mathbf a\|_{\ell^1_{224}}<1/4.
 \tag{E.1}
$$
有限 connector 和两个真实 bump 使用
[balanced 续接](R119-supplement-balanced-connector-label-domain-224.md)
及其在
[当前 fixed-stop 的重新实例](R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md)
第4节。长径向段使用
[真实全频非线性 Dirichlet 定理](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
的实际两个非mean输入，并要求
$$
 \|(f_B,f_*)\|_{\partial,\sigma}\le2^{-25}.
 \tag{E.2}
$$
于是该段真实解满足 $\|h\|_{\mathcal Y_\sigma}\le2^{-20}$。
它包含完整 mean 小根，不能把内端 $f_B$ 设为0后外推到一般匹配。

整个外部参考度量在真实物理半径上准确是
$$
 g=(1+w(a)^2)\,da^2+a^2d\theta^2,\qquad
                 0<a\le a_R,\qquad 0<a_R<7\cdot10^{-6}.
 \tag{E.3}
$$
这里 $R=25/8$ 是主体端点坐标，$a_R$ 是该点的圆半径。
当前紧支集 $\nu$ 控制只在 $(1/20,9/50)$，因而不改变这个外部
目标。原 $a_R$ 盒涵盖当前完整 $\eta_0\pm10^{-9}$。
所有受控深尾与 connector 的几何变量仍依当前参数重建。

## 2. 当前整个参考无限尾的物理二阶界

先重新支付前缀。双 bump 的支集相离，其完整复盒已给
$$
 |(\log p_\Gamma)_x|<(15/8)\Delta,\qquad
 |(\log p_\Gamma)_{xx}|<6\Delta,
 \tag{E.4}
$$
且实 profile 在原平台端值之间严格单调；见双 bump 篇
(U.5)--(U.6)。这恰是
[R69 的实际 log-quintic 计算](R69-actual-closed-approximate-exterior-and-two-held-disks.md)
(69.24)--(69.26) 使用的全部 profile 输入。第129至4096层的
$\mu_j=\epsilon\delta_j^6$、$\eta_j$、端值、cut128 安装尺度
均未改变。因此在当前整个双 bump 盒上逐式重新实例，得到
$$
 \sup_{129\le j\le4096}
      \max\{|w/a|,|w_a|\}
 <\frac{9375}{131072}<\frac18.
 \tag{E.5}
$$
这里用的是当前 profile 的单调端值和真实导数门，没有用旧
$p_0$ 的未经支付逐点比较。

其余层可直接用当前的宽而统一的导数门。写参考半径
$1\le r\le2$，物理缩放 $a=\rho r$。当前安装准确仍有
$$
 \frac{\epsilon}{\rho}
   =\frac b{4\omega_e\bar W_b}<2^{440}.
 \tag{E.6}
$$
这是当前 cut128 的未变端值及实际 fixed-stop 安装关系，
所需的 $b<2$、$\omega_e>(4/5)2^{360}$、
$\bar W_b>2^{-799}$ 均在原安装盒中。参见
[R115](R115-actual-tail-holomorphic-neighborhood-and-strong-extension.md)
(115.4)，而非把 $1/\rho$ 单独当作免费因子。

对 $j\ge4097$，令 $J=j+5$、$\mathsf K=2^{128}$。当前 (C.7)
在8193以后的真实新 profile 上给
$$
 |w|<2\mathsf K\mu_j\delta_j^{-1},\qquad
 |w_r|<2^{10}\mathsf K\mu_jJ\delta_j^{-5/2},\qquad
 \frac{\mu_j}{\epsilon}
       =\delta_{4096}^{3/2}\delta_j^{9/2}.
 \tag{E.7}
$$
在4097至8192的前缀，同一宽式也直接成立：其首剪切至多64，
由(E.4)、原 $1/\eta_j$ 及 $1\le r\le2$ 对
$\mu_jp_\Gamma/r^7$ 求一次导，费用小于(E.7)；没有新增形状支集。
于是整个这些层的物理界被
$$
 |w/a|<2^{569}\delta_{4096}^{3/2}\delta_j^{7/2},
 \qquad
 |w_a|<2^{578}J\delta_{4096}^{3/2}\delta_j^2
                                                        \tag{E.8}
$$
控制。用 $\delta_{4096}<2^{-4099}$、
$\delta_{4097}<2^{-4100}$、$4097+5<2^{13}$，右侧在首层均小于
$2^{-9000}$。以后的层比严格小于 $1/2$，所以这不是有限层扫描。
(E.5)--(E.8)证明当前整个参考混合尾
$$
       \max\{|w/a|,|w_a|\}<1/8.
 \tag{E.9}
$$
故其参考旋转图的两个主曲率绝对值小于 $1/8$，直至真正平端。

## 3. 当前完整非径向尾的二阶费用及唯一高度常数

当前局部二 jet 使用的是(C.23)的 $2^{200}$，不是更早的
$2^{52}$ 或 $2^{184}$。前缀的已付常数也小于这个统一数。因此
$$
 \|\mathcal J_{j,\Pi}(U_j)\|_{C^2_{r,\theta},A_\sigma}
       <2^{200}\delta_j^{-4}h_j^{-5}\|U_j\|,
 \qquad \|U_j\|\le\zeta_j X .
 \tag{E.10}
$$
这里包括 mean 的一、二阶导。当前真实权准确满足
$$
 \zeta_j\le\epsilon\delta_j^{39/4},\qquad
 h_j^{-5}\le2^{18}\delta_j^{-5/256},
 \qquad b_*=\frac{1467}{256}.
 \tag{E.11}
$$
对于 $j>8192$，第一式使用
$\zeta_j=\epsilon\delta_{8192}^{-485/4}\delta_j^{131}$ 和
$\delta_j\le\delta_{8192}$，并未用旧权替换新构造。

每个胞元的参考径向长度小于 $4\delta_j$。下降坡平移不改变
胞元总长度。将 mean 一阶导从真正的累积圆积分回来，所有后续胞元
构成一个收敛几何和；其总费用小于 $2^4$。因此只有一个整体
高度常数 $\lambda$，并有
$$
 \|v-\lambda\|_{C^2_{r,\theta}(I_j)}
        <2^{222}\epsilon\delta_j^{b_*}X.
 \tag{E.12}
$$
没有把未知 mean 设成0，也没有给每个接缝增加一个平移自由度。

在同一完整 holonomy-one 方程上，R115 (115.14)--(115.20) 的
水平 coframe 直接以当前 $w,E$ 重建。反射固定角规范，四重旋转
消去水平平移周期；$(\partial_\theta+i)^{-1}$ 在
$4\mathbb Z$ 上没有核。这一步的全部二阶水平费用至多 $2^{16}$，
固定 Cartesian 实二阶费用再至多 $2^6$。它只需高度二 jet，
没有偷加三阶径向导数。结合真实物理缩放(E.6)，
$$
 \|F_\Pi-F_{\Pi,0}-\lambda_{\rm phys}e_z\|_{C^2(I_j^{\rm phys})}
       <2^{684}\delta_j^{b_*}X .
 \tag{E.13}
$$
此处 $F_{\Pi,0}$ 是同一个当前 $\Pi$ 的旋转参考图。
因为 $\delta_{129}<2^{-132}$ 且
$132b_*-684=4635/64>64$，得到整个真实无限混合尾的统一界
$$
 \boxed{\quad
 \|F_\Pi-F_{\Pi,0}-\lambda_{\rm phys}e_z\|_{C^2}
                       <2^{-64}X<2^{-66}.
 \quad}                                                    \tag{E.14}
$$
同时逐胞二 jet 趋0。真实接缝的完整 PDE 已匹配二 jet，故该
真向量图在累积圆上 $C^2$ 接到整个水平圆盘。
所有非零模以及 mean 均包含在此延拓中。

为把(E.14)变成曲率界，在 Cartesian 平面坐标上写
$F_{\Pi,0}(x)=(x,Z_\Pi(x))$。其度量最小特征值至少1，且
$\|D^2Z_\Pi\|<1/8$。若两个同度量图的完整二 jet 差小于
$e\le2^{-10}$，对两切向量的叉积先作差再归一化，得
$|n-n_0|\le16e$。因此第二基本形式以及同度量形算子的差
均小于 $32e$。用(E.14)，真实整个无限尾满足
$$
               |\kappa_i|<\frac18+32\,2^{-66}<\frac14 .
 \tag{E.15}
$$
轴向常数不进入导数或曲率。

## 4. 有限 connector、两个 bump 与长段的完整曲率

有限 connector 和两个 bump 已给
$$
 \sup N_b<2^{-447}X,\qquad
 \|F_\Pi-F_{\Pi,0}-\lambda e_z\|_{C^2}<2^{-430}X.
 \tag{E.16}
$$
当前 fixed-stop 篇(D.16)重新支付整段而非只有端口。另一方面，
长段的完整强 norm 直接给
$$
 N:=\|P\|+\|K\|+\|U\|+\|V\|
     <4\|h\|_{\mathcal Y_\sigma}\le2^{-18},
 \qquad |K_0|\le256\|h\|_{\mathcal Y_\sigma}^2.
 \tag{E.17}
$$
在两种段上，均有 $N\le2^{-18}$、$0<w/a<5/18$、
$|A|\le7$，其中
$$
 P=\frac{v_\theta}{aw},\quad K=\frac{v_a}{w},
 \quad U=P_\theta,\quad V=K_\theta,\quad A=\frac{aw_a}{w},
 \quad t=\log a,\quad E=1+w^2 .
 \tag{E.18}
$$
所有 norm 在各自已付完整角宽上取；真实角上的绝对值由同一个
Wiener norm 控制。$K$ 包括 mean。准确方程给
$$
 K_t=-AU-2AK+\mathcal R,\qquad
 \mathcal R=
 \frac{E(V-P)^2+A(K^2+2EKU+EU^2-w^2P^2)}
      {1+K+EU},\qquad |\mathcal R|\le64N^2 .
 \tag{E.19}
$$
故不用对极小物理半径单独付一个 $a^{-1}$ 大常数。

以下直接算真实形算子。先用正高度约定 $z_a=w(1+K)$、
$z_\theta=awP$；北帽整体竖直反射只改变统一的法向符号。
由目标度量的 Christoffel 符号和
$\operatorname{Hess}_g z=(n\cdot e_z)II$，在正交极坐标切向基中
$$
 \mathsf S=\frac{w/a}{n_z}
 \begin{pmatrix}
 \big(A(1+K)/E+K_t\big)/E & (V-P)/\sqrt E\\
 (V-P)/\sqrt E & U+(1+K)/E
 \end{pmatrix},
 \quad
 n_z=\sqrt{D/E},\quad
 D=1-w^2(2K+K^2+EP^2).
 \tag{E.20}
$$
这是实际非径向曲率公式，不能用参考端点的 $A=-7$ 代替整段。

由 $a\le7\cdot10^{-6}$ 和(E.17)--(E.18)，
$$
 E<1+2^{-37},\qquad D>1-2^{-50}.
 \tag{E.21}
$$
对(E.20)的实对称矩阵逐行取绝对值并使用(E.19)，
$$
 \|\mathsf S\|
 \le\frac5{18}\sqrt{\frac{1+2^{-37}}{1-2^{-50}}}
             (7+24N+64N^2)<2.
 \tag{E.22}
$$
最后一步只涉及准确有理数的平方比较。本界涵盖全部角模、两个
真实 bump、短 connector 和整条极长径向段。特别段的长度没有
作为指数放大因子出现。

由(E.15)、(E.22)以及平盘的零曲率，整个实际外部统一满足
$$
                 \boxed{|\kappa_i|<2.}                    \tag{E.23}
$$

## 5. 由同一度量取得同世界坐标的位置及支持预算

现在只在这一节假定完整模块的两迹、mean 和真实角图已与主体在
$R=25/8$ 匹配。这个假定是尚须由外接口方程证明的准确输入。
对每个外部点沿固定实际物理角走向 $a_R$。有限段的(E.18)、
无限尾的(E.9)和平盘的 $w=0$ 给
$$
 \begin{aligned}
 L_{\rm ext}
 &=\int_0^{a_R}\sqrt{1+w(a)^2}\,da\\
 &\le a_R\sqrt{1+(5a_R/18)^2}
                      <8\cdot10^{-6}=:\ell_* .
 \end{aligned}                                             \tag{E.24}
$$
非径向解精确诱导同一 $g$，所以沿该材料径线的像长准确就是
这个度量长度。特别，无论唯一 mean 常数为何，
$$
             |F(a,\theta)-F(R,\theta)|<\ell_* .
 \tag{E.25}
$$
在盘心取径线极限。没有在此步骤重新选择轴移或世界原点。

(E.23)同样给沿径线的真实单位法向差
$$
                 |n(a,\theta)-n(R,\theta)|<2\ell_* .
 \tag{E.26}
$$
若主体端点半径至多 $R_B$、支持量至少 $s_B$，则
$$
 \begin{aligned}
 \sup_{\rm ext}|F|&<R_B+\ell_*,\\
 \inf_{\rm ext}F\cdot n
      &>s_B-\ell_*(1+2R_B).
 \end{aligned}                                             \tag{E.27}
$$
例如 $R_B\le13/10$ 时，只需从主体支持下界扣
$2.88\cdot10^{-5}$。这与四阶径向核验、全角插值、真实 C0 状态修正
使用同一个原点和同一个真正单位法向。

用于最终几何的一个直接合同是
$$
 R_B\le\frac{511}{400}-\ell_*,
 \qquad
 s_B>\frac4{49}+\ell_*(1+2R_B).
 \tag{E.28}
$$
它使全部外部达到相同的半径、支持与曲率门。主体的整个连续
几何以及最终 marker 修改仍须独立按它们的真实费用完成。

## 6. 真平帽高度、轴心及固定材料条件

主体模型的世界高度固定为
$$
 H_*=\frac{4347844570122155}{4503599627370496}.
 \tag{E.29}
$$
取上侧。若真实主体端点在同一个世界坐标中满足
$$
              |F_z(R,\theta)-H_*|\le1/100,               \tag{E.30}
$$
则(E.25)直接给平帽轴心高度 $Z_{\rm flat}$ 满足
$$
 H_*-\frac1{100}-\ell_*<Z_{\rm flat}
       <H_*+\frac1{100}+\ell_*,
 \qquad                 \frac9{10}<Z_{\rm flat}<1.
 \tag{E.31}
$$
四重旋转的准确水平规范把盘心固定在共同轴上。
真平盘半径满足 $0<a_{\rm flat}\le a_R<7\cdot10^{-6}$。
对在腰平面准确反射匹配的下侧，同一证明给
$-1<Z_{\rm flat,-}<-9/10$，不另外重设平移。
这是两个实际平子盘的轴心间距，而不是用一个很小圆盘的
半径代替握持区的直径。

在每个平盘上，完整重建准确是
$$
 F(a,\theta)=(a\cos\theta,a\sin\theta,Z_{\rm flat}).
 \tag{E.32}
$$
若一个最终族的 $Z_{\rm flat}$ 确实固定，其材料圆盘就逐点固定。
相位平移后的解图在作相同水平反旋转时亦保持(E.32)，但其
mean 高度必须由同一实际族的方程或对称性证明恒定。不能仅从
(E.31)的区间界推出这个结论。

两个半径为 $a_{\rm flat,\pm}/2$ 的闭子盘均有内点，其并集
包含两个轴心，故直径大于 $9/5$。在最终全曲面半径门成立时
$D\le511/200$，于是握持集合的尺寸门满足
$(9/5)/(511/200)>1/5$。逐点固定、非全等和最终全部参数的
reach 仍必须在同一真正闭族上检查。

## 7. 本篇支付与尚未支付的边界

已经支付的是当前 $\Pi$ 全实盒的参考尾几何、含 mean 的真正
无限尾物理二阶费、全部有限段真实曲率，以及在准确匹配后
同世界坐标中的完整位置/法向/平帽合同。所用小有理预算没有
重新计算原 target 或已经完成的几何数组。

还须完成的实际输入是：完整非径向外接口及所有独立 mean 条件、
主体与尾的同一全频逆、非线性精确解，以及最终族上固定帽
高度和四个独特非共面 marker 的条件。本文没有以几何裕量
替代其中任何一个方程。

[准确预算源](../scripts/fourfold_codazzi_current_exterior_geometry_budget.py)
和[实际运行记录](../notes/2026-11-14-R133-current-exterior-geometry-budget.json)
保存所有新常数门与已读依赖身份。
