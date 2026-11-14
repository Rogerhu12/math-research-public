# R97：实际根剪切的有限物理列和完整算子误差

2026-11-12。状态：本条完成；总课题、其他 frame 和完整反馈强逆未完成。

对准确 δ₅ 中心的实参数盒半宽 η=10⁻⁹，本文实际计算保留物理
Fourier 指标 |n|≤4096 的一个准确有限秩、自伴算子 F，并证明

\[
 \|\Delta-F\|_{L^2\to L^2}<0.000160744609.                 \tag{1}
\]

这里 Δ 是 [R92](R92-actual-canonical-physical-low-columns-and-complete-tails.md)
与其[常数分解补充](R92-supplement-constant-split-and-weighted-physical-tails.md)
中的**真实**根剪切差，包括物理 mean、所有低高 cross、两侧准确角图酉变换。
F 的 105 对 B/C 列存为 53 对实 binary64 列及准确反射规则；这些数视为准确
dyadic。F 只是计算参照；既不重新定义几何，也不把有限 DFT 当作真实无限 primitive。

## 1. 原对象、真根点值和所有角尾

输入为原准确 affine 后偶奇平均的无限 R33 对象。所有输入 SHA、参数区间、
root certificate 和原 common scalar spans 都记录在
`data/root_finite_grid/grid4096_h1e9/manifest.json` 及九个分片中。
该完整清单 SHA 为
`3e9e902d540bfd2cd159492af2667d32db3580cc14d0dea5c80b3d768228af0f`。

`fourfold_phase_root_finite_grid_v2.py` 在原已证 family root 内做三次区间 Newton
求交，没有换 scalar span 或缩小原外预算的适用对象。原有限 primitive 由 Arb
逆 DFT 在准确网格 θⱼ=πj/(2·4096) 上求值；随后每个径向系数仍加原完整无限
primitive Cauchy 费。角 jets 使用准确几何 ODE，而非对有限 primitive 做角导数。
因此 2049 个点上得到的是整 η 参数盒的真实 Y′、v₀ 及全部记录的 frame 点值。

D4 准确反射给位置分量奇偶为 (even,odd,even)，物理根 shear 为 odd，沿 shear
的标量导数保持 even。因此 Y′ 和 ν_phys=v₀−5050 都是 even；对半圈点值作准确
反射得到全部 4096 点。两者在原完整 strip S=1/256 上的模界分别为 M_Y、M_V。
其来源是已经完成、无 pending/failed 的实际复角证书，不是点网格最大值。

以下对任一 even 函数 f 记 N=4096、K_f=N/2、r=e^(−4S)，取各 nodal ball
的准确 dyadic 中点后做 Arb DFT，并将 resulting finite DFT ball 的准确中点定义为 cₙ。
准确有限参照为

\[
 P_f(\theta)=c_0+2\sum_{n=1}^{K_f-1}c_n\cos(4n\theta)
                       +c_{K_f}\cos(4K_f\theta).                \tag{2}
\]

设 nodal ball 半径最大值 e∞、均方根 e₂，有限 DFT 取中点造成的系数 ℓ¹/ℓ²
费为 e_D1/e_D2。完整解析 Fourier 尾与所有插值 alias 的统一界为

\[
 E_{\rm alias}=\frac{4M_f r^{K_f}}{1-r}.                         \tag{3}
\]

确实每个真实系数满足 |f̂ₙ|≤M_f r^|n|；插值把全部 |n|≥K_f 的系数折回低带，
减法的两份尾由 (3) 支配，Nyquist 的半权也包含在这个上界内。
周期 cardinal kernel 的公式
`sin(Nx/2) cot(x/2)/N`，加上离给定角最近的一个节点，给

\[
 \Lambda_N\le1+\frac4\pi\left(1+\tfrac12\log(N-1)\right).
\]

其余节点按左右距离序列排列，用 |cot(x/2)|≤2/|x| 与调和和的积分界即可；
于是统一实角误差和零均值原函数误差分别为

\[
 E_f\le\Lambda_N e_\infty+E_{\rm alias}+e_{D1},\qquad
 E_{If}\le\frac\pi{4\sqrt3}(e_2+E_{\rm alias}+e_{D2}).          \tag{4}
\]

第二式使用 Parseval：nodal 插值的 L² 范数不超过离散 RMS（Nyquist 被分成
两个半系数，只会减小范数）。零均值原函数的 evaluation norm 平方正好是
Σₙ≠₀(4n)⁻²=π²/48。even 函数的这个原函数为 odd，在 0 为零；没有另一个未付的
积分常数。真均值由全部 nodal ball 的平均加
`2 M_Y r^N/(1-r^N)` 包围，而非仅取有限 c₀。

具体完整输出见
`notes/2026-11-12-actual-root-Fourier-fit-and-H-primitive.json.gz`：

\[
 q\in[9.720962901467315,9.720962905772938],\quad
 E_Y<3.682298\,10^{-10},\quad E_V<0.000119955800.
\]

## 2. 固定准确角图参照与完整算子比较

令 q₀ 为 1/c_Y0 的准确 dyadic 中点，I 为上述零均值原函数。定义

\[
 H_0(\theta)=\theta+q_0 I(P_Y)(\theta),\qquad
 H'_0=1+q_0(P_Y-c_{Y0}),\qquad \nu_0=P_V\circ H_0^{-1}.
\]

它满足准确周期归一化 H₀(θ+π/2)=H₀(θ)+π/2。真实 H=qY 的原函数同样归一化，且

\[
 E_H:=\|H-H_0\|_\infty
 \le q_+E_{IY}+|q-q_0|\|IP_Y\|_\infty<1.573761\,10^{-10}.
\]

对角导数令

\[
 e_h=q_+E_Y+|q-q_0|\|P_Y\|_\infty+|q_0c_{Y0}-1|,\quad
 m_0=m-e_h>0.
\]

这里真实复 strip 上 Re H′≥m>0.54445389965，|H′|≤M<2.80066819210。
因而 H₀、H 皆为实圆上的 onto diffeomorphism，
U_i f=√Hᵢ′·f∘Hᵢ 是准确 onto L² unitary。
逆映射的实 Lipschitz 界给

\[
 e_\nu:=\|\nu-\nu_0\|_\infty
 \le E_V+\|P'_V\|_\infty E_H/m.                              \tag{5}
\]

所有多项式模界和导数模界都从完整有限准确系数 ℓ¹ 求和；Nyquist 半权保持。
不需要把有限参照的逆图误称为真实图。

令 L=2048、Γ_q(0)=1、Γ_q(n)=4q|n| (n≠0)，A_q=Γ_q⁻¹、
T_q=max(Γ_q,L)⁻¹。完整 canonical 剪切为

\[
 D(q,\nu)=5050(A_q^2-T_q^2)+A_qM_\nu A_q-T_qM_\nu T_q,
 \qquad\Delta=U_H D(q,\nu)U_H^*.
\]

频率误差满足（q_* 是 q 和 q₀ 的共同正下界）

\[
 d_A\le |q-q_0|/(4q_*q_0),\qquad
 d_T\le |q-q_0|/(Lq_*).
\]

mean 项与 q 无关，故常数部分使用非零频率最大 A 值 1/(4q_*)，得到

\[
 e_D\le5050\left(2d_A/(4q_*)+2d_T/L\right)
       +2V_0(d_A+d_T/L)+e_\nu(1+L^{-2}),                    \tag{6}
\]

V₀=||P_V||∞ 的上界。对 D₀=D(q₀,ν₀) 有

\[
 \|D_0\|\le5050(1-L^{-2})+V_0(1+L^{-2}),\quad
 \|\partial_\psi D_0\|\le\frac{5050}{4q_0^2}
                              +\frac{V_0}{q_0}(1+L^{-1}). \tag{7}
\]

第二式中导数落在最左 Fourier multiplier：||∂A||,||∂T||≤1/q₀。
因此没有未经支付的 ν₀ 导数。

角图的直线同伦导数至少 m₀。分开半密度差与函数复合差，变量替换和积分给

\[
 \|(U_H-U_0)w\|_2\le\frac{e_h}{2m_0}\|w\|_2
                 +\sqrt{M/m_0}\,E_H\|w'\|_2.               \tag{8}
\]

D₀ 自伴，因此两侧酉变换之差由两倍 (8) 作用于 D₀ 支配。合并 (6)–(8) 得

\[
 \|\Delta-U_0D_0U_0^*\|
 \le e_D+\frac{e_h}{m_0}\|D_0\|
       +2\sqrt{M/m_0}E_H\|\partial D_0\|
 <0.000160657865981.                                      \tag{9}
\]

完整数字报告为 `notes/2026-11-12-actual-to-nominal-root-shear.json`。
(9) 在任何 canonical/physical 投影之前证明，对整个真实参数盒有效。

## 3. 参照势的 canonical 系数与无限尾

真正 H 在 strip 内 Re H′≥m，所以为单叶映射。上、下边界的虚部分别至少
±mS，周期性使该映射 proper；边界绕数或 argument principle 给其像包含
|Im ψ|<mS。取严格子带

\[
 u=\tfrac78mS>0.0018609264148396234.
\]

于是实际 ν 的 |ν̂ₘ|≤M_Ve^(−4u|m|)。这只用真图，不假设有限 H₀ 的逆图拥有同一带。
固定 ν₀ 的系数用恒等式

\[
 \widehat\nu_{0,m}=\operatorname{avg}_\theta
 [P_V(\theta)H'_0(\theta)e^{-4imH_0(\theta)}]               \tag{10}
\]

实际计算 m=0,…,2048，物理求积点数 Q=16384。
H₀、H₀′、P_V 在原 strip 的完整有限系数模界均已计入。
若 |Im H₀|≤B_H、|H₀′|≤B_h、|P_V|≤B_V，则 (10) 的全梯形 alias 为

\[
 \frac{2B_VB_h\exp(4mB_H-4SQ)}{1-e^{-4SQ}}.                \tag{11}
\]

Arb 给每个准确有限节点值和 exp(−4iH₀) 的 ball。转 binary64 的误差由 Arb
实际包围，绝不假定系统 libm 精度。复数乘法在两个因子模小于 2 时单步误差
≤2⁻⁴⁶；dₘ≤m(e_z+2⁻⁴⁶)e^(m e_z)<1/4 的归纳同时证明此前因子仍在该范围。
相位节点转移另付 4m e_H。任意求和顺序用 γ_{2Q+2} 的前向误差界，连同
实乘法付 `2 γ_{2Q+2} avg|w_center|`。所有 underflow 的可能误差也被这个远大于
最小 subnormal 的绝对界支配。有限系数包围再与
|ν̂₀,ₘ|≤M_Ve^(−4um)+e_ν 相交。

输出 `notes/2026-11-12-nominal-root-potential-canonical-modes.json.gz`
记录准确 binary64 中点 vₘ 与半径 ρₘ。ν₀ 是 even，所有系数实；令
ν_mid=Σ_|m|≤2048 v_|m|e^(4imψ)。这是参照势的有限近似，不是实际参数势。
真实势的整个尾及参照势的尾满足

\[
 \mathcal T_{\rm true}\le\frac{\sqrt2M_Ve^{-4u(M_c+1)}}{\sqrt{1-e^{-8u}}},\qquad
 \mathcal T_0\le\mathcal T_{\rm true}+e_\nu,\quad M_c=2048. \tag{12}
\]

第二式是 L² 正交尾投影的收缩性加 (5)，没有免费丢掉参照势的无限模。

## 4. 准确有限列及其物理投影

此 η 盒的 q₀ 给 canonical 低支撑 |k|≤52。令 E 为该 105 维空间的 isometry，
d_k=A₀(k)−T₀(k)>0、κ_k=5050(A₀(k)²−T₀(k)²)，并定义

\[
 B=U_0E,\quad C=U_0T_0M_{\nu_{mid}}E,\quad
 W=E^*M_{\nu_{mid}}E.
\]

准确有限 canonical 势的剪切差严格为

\[
 \Delta_{mid}=B\kappa B^*+BdC^*+CdB^*+BdWdB^*.           \tag{13}
\]

特别是 k=0、W 的所有 off-diagonal 和两个 cross 都在，不能只留下 BκB*。
W_{ij}=v_|i−j| 是准确实对称 Toeplitz 矩阵。

物理节点仍取 Q=16384。B_k=√H₀′e^(4ikH₀) 由 Arb 算准确根和整数幂。
对 C_k，canonical 多项式

\[
 f_k(\psi)=\sum_{m=-M_c}^{M_c}T_0(m+k)v_{|m|}e^{4i(m+k)\psi}
\]

在 canonical 网格 G=8192 上计算归一化 Taylor 系数到 J=16。
半间距 R=π(1+2⁻³⁰)/(4G)，每个实际有限 H₀(θⱼ) 的最近节点都由 Arb 验证
|δ/R|<1。系数导数 `(4inR)^j/j!` 和 inverse FFT 由逐基本运算向外舍入的
`DirectedFFT` 包围；roots 本身由 Arb 包围。全有限 Taylor 余项为

\[
 \sum_n|T_0(n)v_{|n-k|}|e^{4|n|R}\frac{(4|n|R)^{J+1}}{(J+1)!}.
\]

Horner 后乘准确半密度，得到全 nodal complex boxes。每个 box 的 binary64
中心作为准确数，以实际 box 距离的离散 RMS 付误差；Parseval 使这项不需要
额外乘 √(2N+1)。中心用 native Arb DFT。保留 n=−4096,…,4096 的实 binary64
中心，其有限 DFT 取中点误差另作 ℓ² 求和。反射给所有真实列系数为实，且
`column(-k,n)=column(k,-n)`。即使有限中心 DFT 带小虚部，程序也把该虚部算入误差。

设任一 B/C 列在 S 上的完整有限复模为 M_col。每个保留物理 n 的完整 alias 是

\[
 M_{col}\frac{e^{-4S(Q-|n|)}+e^{-4S(Q+|n|)}}{1-e^{-4SQ}}.   \tag{14}
\]

B 的 M_col≤√B_h exp(4|k|B_H)；C 用整个 finite canonical sum 的
Σ|T₀(n)v_|n−k||exp(4|n|B_H)，没有截去其很大但可由求积指数压下的复带部分。
这些 alias 的 ℓ² 加 nodal RMS 和 Arb DFT rounding 是每一列的完整投影误差。

数据在 `data/root_finite_grid/physical_columns4096/`：53 个 `column_kkk.npz`
各含两个长度 8193 的实 binary64 数组（禁止 pickle）；清单记录每件 SHA 和
每列误差。负 k 按准确反射取列，得到有限矩阵 B̃、C̃。将 (13) 的 B、C 换成
B̃、C̃ 后定义 F；无需舍入构造一个 8193×8193 的稠密矩阵。

## 5. 不遗漏无限模的完整误差合成

令 δ=||d||、V_mid=Σ|v_m|，e_B、e_Bκ、e_Bd、e_Cd 为列误差分别按
1、κ、d、d 加权后的 Hilbert–Schmidt 上界（±k 都计数，mean 一次）。
因为 ||P_NB||≤1、||P_NC||≤V_mid/L，(13) 的逐项双线性差给

\[
 e_{cols}\le(2+e_B)e_{B\kappa}
 +2\{e_{Bd}V_{mid}/L+(1+e_B)e_{Cd}\}
 +e_{Bd}V_{mid}(2\delta+e_{Bd})<2.115442\,10^{-12}.         \tag{15}
\]

对 ν₀ 的有限系数求积误差，准确 Parseval 给

\[
 e_{coef}\le2\sqrt{\sum_{|k|\le52}d_k^2
           \sum_{|m|\le M_c}T_0(m+k)^2\rho_{|m|}^2}
 +\delta^2\left(\rho_0+2\sum_{m=1}^{104}\rho_m\right)
 <5.126394\,10^{-8}.                                      \tag{16}
\]

第二项是完整 W 差的 row/column sum 上界。对遗漏的全部 canonical 势尾，
|m+k|≥M_c+1−|k|，(12) 给

\[
 e_{tail}\le2\sqrt{\sum_{|k|\le52}
 \left(\frac{d_k\mathcal T_0}{4q_0(M_c+1-|k|)}\right)^2}
 <3.547615\,10^{-8}.                                      \tag{17}
\]

尾不影响 W，因为 M_c>104；它仍影响两个 B/C cross，并已全部付在 (17)。

最后先对**真实** Δ 作物理双侧投影，而非假定有限参照等于实际列。
R92 补充在原较大参数盒已证
||Δ−P_NΔP_N||<8.617708·10⁻²⁰ (N=4096)，因此也适用于本 η 子盒。
对 P_NΔP_N 依次用完整比较 (9)、(16)、(17)、(15)，投影范数均为 1。
五项相加的实际向外舍入结果为

\[
 0.00016074460817971216835823764158465108\ldots,
\]

从而得到 (1)。所有数据和公式都保 mean；有限参照的秩至多 210。
这一步没有宣称完整反馈可逆，也没有宣称已经找到非线性零解。

另以输出投影分解并使用 R92 全高输出 H^(1/3) 尾，得到

\[
 \|\Delta-F\|_{L^2\to H^{1/3}}
 \le (1+(4N)^2)^{1/6}\|\Delta-F\|_{2\to2}
 +(1+[4(N+1)]^{-2})^{1/6}\|(I-P_N)\Delta\|_{2\to\dot H^{1/3}}
 <0.004082658565.
\]

这里 H^(1/3) 的平方范数权为 `(1+(4n)^2)^(1/3)`，所以 mean 保留。
该完整输出估计由 `fourfold_phase_physical_column_output_norm.py` 聚合保存到
`notes/2026-11-12-actual-root-shear-finite-H13-error.json`。

## 6. 可复现入口

依次运行以下已保存的源码（普通 Python，Arb 精度按报告）：

```bash
python scripts/fourfold_phase_root_finite_grid_cover.py --grid 4096 --chunk 256 --directory data/root_finite_grid/grid4096_h1e9
python scripts/fourfold_phase_root_fourier_fit.py --out notes/2026-11-12-actual-root-Fourier-fit-and-H-primitive.json.gz
python scripts/fourfold_phase_nominal_root_shear.py --out notes/2026-11-12-actual-to-nominal-root-shear.json
python scripts/fourfold_phase_nominal_potential_modes.py --out notes/2026-11-12-nominal-root-potential-canonical-modes.json.gz
python scripts/fourfold_phase_nominal_physical_columns.py --out-dir data/root_finite_grid/physical_columns4096
```

第一步真 grid 已完整保存，不要求为了接受本条再机械重跑。其准确执行参数在
grid manifest、每个 shard 和源默认值中；每一步读取上一步完整清单和字节 SHA。
本条下一个实际缺口仍是其它 frame 的完整物理系数/尾以及同一个全反馈的低 Schur。
