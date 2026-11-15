# R133 补充：固定内窗局部第一修正的完整实角二阶预算

**状态：解析预算已证，实际改进数值须由公开 Actions 消费。** 本条只更新 [内窗 actual](R133-supplement-actual-fixed-inner-first-Airy-complete-sources.md) 的局部项。原 w1、η0、|δ|≤10^-8、固定物理 I、输入 |j|≥97、两 Airy 分支、全部输出和 mean 不变。

## K1. 完整 raw 局部量

记 W=(a1,b1)，ρ=r*−r。沿用原 [完整 Taylor 递推](R133-supplement-old-radial-first-Airy-Taylor-and-complete-Fourier-root-recurrence.md) 的局部系数；在 ε=+1 的分支，完整未归一化量为

$$
N_1=W_{\rho\rho}+2dW_{\rho\phi}
 +(d_\rho+d d_\phi)W_\phi
 +(d^2+\eta^2K)W_{\phi\phi}
 +T_0(W_\rho+dW_\phi)+V_0W
 +i\epsilon\vartheta Q
 \begin{pmatrix}0&T\\1&0\end{pmatrix}W.
\tag{K1}
$$

它是 μ L0w1，μ=Q²B+，并非 μ^-1N1。两分支用同复参数的准确奇偶恒等式，取绝对值后的预算相同。这里的 ρ 导和旧物理 r 导只在完整有符号公式中转换；majorant 均取相应真实导数绝对值。

## K2. 旧表与唯一缺失的导数

原 run43653825736 已逐完整 Fourier 系数证明

$$
W_{p,q}^{(h)}\ge
 \sup_{\rho\in I-r_*,\ \phi\in\mathbb R}
 |\partial_\rho^p\partial_\phi^qW_h|,
\qquad 0\le p\le2,\quad0\le q\le3.
\tag{K2}
$$

同时在原宽 σ=1/512 已保存同样的 strip sup 表，分别标记 strip sup 与 Wiener；本条只消费前者，完整 Fourier 尾已包含。

为给 K1 两次角导，唯一缺失的是 p=0,q=4。Cauchy 对任一已存 q=0,1,2,3 给

$$
W_{0,4}^{(h)}
 \le (4-q)!\,\sigma^{-(4-q)}
       W_{0,q;\sigma}^{(h)}.
\tag{K3}
$$

故可取这四个真实上界的最小值。全周期带在每个实点包含半径趋于 σ 的圆盘；先取较小圆盘再取极限，K3 合法。这里没有用实角 sup 代复带界，也没有从缺失表项补零。

## K3. 完整系数角 jets

使用原已证明小辅助域 R=3/40000、角宽 Σc=1/32 的 complete_coefficient_majorants。其 D0..D3 与 Dr0..Dr2 分别控制 d 的前三阶角导及 dρ 的前二阶角导；ρ/r 符号不改变绝对值。

由于 η、K 真实径向，令 A=d²+η²K、B=dρ+d dφ，合法 majorant 为

$$
\begin{aligned}
A_0&=D_0^2+\eta_+^2|K|_+,&
A_1&=2D_0D_1,&
A_2&=2D_0D_2+2D_1^2,\\
B_0&=Dr_0+D_0D_1,&
B_1&=Dr_1+D_1^2+D_0D_2,&
B_2&=Dr_2+3D_1D_2+D_0D_3.
\end{aligned}
\tag{K4}
$$

T0、V0、vartheta 原表是在完整 Σc 带的 sup，故每个 C∈{T0,V0,vartheta} 有

$$
C_q\le q!\,\Sigma_c^{-q}C_0,\qquad q=0,1,2.
\tag{K5}
$$

两种已知导数费用各按其真实来源使用。整个固定 I 在该辅助域中；本条不扩张它。

原内窗 stage 已保存

$$
P_Q=Q\begin{pmatrix}0&T\\1&0\end{pmatrix},
\qquad (P_Q)_{12}=-a\rho A^{1/3},\
(P_Q)_{21}=aA^{-1/3}
\tag{K6}
$$

的完整角 jets 至三阶。直接复用其 q=0,1,2；不重新求 fold、PQ 或 profile。

## K4. 完整乘积递推

对标量 jets c 与向量 jets v，定义普通导数的完整二项乘积

$$
(c\star v)_q=\sum_{\ell=0}^q
 {q\choose\ell}c_\ell v_{q-\ell};
\tag{K7}
$$

矩阵 jets 用有序矩阵乘法的相同式。每分量均是非负 upper，不跨矩阵调换次序。

令 Wp 的第 q 项为 Wp,q，Wφ 的第 q 项为 W0,q+1，Wρφ 为 W1,q+1，Wφφ 为 W0,q+2。K1 的完整 q=0,1,2 majorant 是

$$
\mathcal N=
 W_{\rho\rho}
 +2(D\star W_{\rho\phi})
 +(B\star W_\phi)+(A\star W_{\phi\phi})
 +T_0\star(W_\rho+D\star W_\phi)
 +V_0\star W
 +\vartheta\star(P_Q\star W).
\tag{K8}
$$

所有 q≤2 的指标都由 K2–K6 支付。尤其 T0 的角导、dρ 的角导、真实 η²K、vartheta 与 PQ 的全部交叉，以及第二分量中的 Q a1 都未删除。

## K5. 复用完整实 Airy 转换

沿用原内窗 stage 的 m、F2、composition、near、far 和每侧完整 profiles (pa,pb)。对每一个 profile 令

$$
s_q=\sum_{\ell=0}^q{q\choose\ell}
 \{p_{a,\ell}\mathcal N_{q-\ell,1}
   +p_{b,\ell}\mathcal N_{q-\ell,2}\},
\quad
b_2=s_2/m^2+s_1F_2/m^3 .
\tag{K9}
$$

原完整实角二阶 Airy 定理授

$$
C_{\mathrm{real}}
 =\sum_{\mathrm{profiles}}
 C_{\mathrm{composition}}
 \left[C_{\mathrm{near}}
   (s_0+\pi^2 b_2/48)+C_{\mathrm{far}}b_2\right].
\tag{K10}
$$

负侧全部三个 profile 和正侧原 profile 依原 stage 保留。mean 与双向全部角输出仍在原 near/far 证明内，不以有限 band 截断。

原局部解析 Airy bound C_old 已由 run43657933806 实际通过完整身份/覆盖门。两个界对应同一个 N1 和相同空间，因此本条可用 min(C_real,C_old)。这是新真实候选与旧候选的最小值；旧计算无需重复执行，也不预先保证改进。

## K6. 只更新真正改变的径向项

对旧四行中的每个非零径向半侧，完整复制原 interval、radial_weight_integral、final J window、非局部九项、独立 mean 五项及其分项积分。只新算

$$
l_{\mathrm{new}}=C_J\min(C_{\mathrm{real}},C_{\mathrm{old}}),
\quad
E_{\mathrm{new}}=(n_{\mathrm{old}}+l_{\mathrm{new}})^2
                 +m_{\mathrm{old}}^2 .
\tag{K11}
$$

按原真实径向权积分，再对所有原四行求和及平方根。n 与 l 在同一分量，必须先 triangle 再平方；mean 保留为原独立第二行。两原成功 stage、四矩阵转换、非局部/mean 积分与原 exact-zero 半侧全部原样保。

## K7. 身份与使用范围

新 consumer 须校验 run43657933806 的17门、完整 native/process/source/manifest、两个 stage payload、全部四行覆盖以及原 Taylor20门与辅助小域13门。全部原64 pins 不变，新文件另加 pin。实际新角 jets、Airy bound 和 changed-local 积分保存在新的 natural stage 和逐行 native，失败与成功前缀均保；不重做旧数学。

本条只证明 K1–K11 给有效完整局部上界。真实 numerical gate、改进幅度及是否足以收缩均由实际公开 run 决定。leading 源、严格外段、原 physical seams、正侧加权端口、全强返回、充分 cutoff 和最终 ν/非线性/闭合仍按各自合同继续。
