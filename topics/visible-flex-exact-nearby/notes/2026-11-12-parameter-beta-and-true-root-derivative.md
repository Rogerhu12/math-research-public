# 精确第三点参数邻域：完整相位与真实根导数

日期：2026-11-12。完整相位在
\(\Delta_8=[\delta_3-10^{-8},\delta_3+10^{-8}]\) 上已证；
真实转折根的一阶参数导数在
\(\Delta_5=[\delta_3-10^{-5},\delta_3+10^{-5}]\) 上已证。
两个区间都不是已确认的最终 KAM 区间。这里不把第三点结果转授随后产生的第四点，
也不据相位格隙断言完整 PDE 或非线性族闭合。

## 1. 精确对象与完整相位

\[
\delta_3=-\frac{7832869216826619}{4611686018427387904}.
\]

对象定义为
[type_fixed_step02_d5_exact_affine_step3_object.json](../data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json)，
SHA256 e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f。
origin 和 direction 的 SHA256 分别为

- 0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b；
- 8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab。

参数先进入准确原始 spline 控制量 \(c_0+\delta v,\alpha_0+\delta w\)，
随后才乘固定 base 权重、作显式径向对称化和无限角原函数。
没有先把每个参数点四舍五入物化为新 NPZ。

对每个 \(\delta\in\Delta_8\)，严格有

\[
\boxed{37.01422398291<\beta(\delta)<37.03580857868.}
\tag{1}
\]

完整报告为
[beta-step3-parameter-h1e8-complete-enclosure.json](2026-11-12-beta-step3-parameter-h1e8-complete-enclosure.json)，
SHA256 7a6da4745e33a4dfb05f11cd2c9391c6aeeef4f84e9e46af83de27ff513f8057。

代入 [R34](../results/R34-full-phase-quadratic-irrational-gap.md) 的 D5 奇整数范数格，

\[
52.690676212310791015625
\le \frac{2\sqrt5}{\pi}\beta(\delta)
\le 52.721402823925018310546875,
\]

故

\[
\operatorname{dist}\!\left(\frac{2\sqrt5}{\pi}\beta(\delta),
                  2\mathbb Z+1\right)>0.27859717607,
\qquad
\operatorname{dist}\!\left(\beta(\delta),
       \frac{\pi}{2\sqrt5}(2\mathbb Z+1)\right)>0.19570935465.
\tag{2}
\]

这是该完整首相位系数的危险格分离。真实主旋转、常相位/frame、高频余项、
有限低块及非线性收敛仍需各自证据。

## 2. 全积分覆盖与实际误差

固定 bulk 切口为
\(c=268136140016943/1125899906842624\)。
全参数区间的根都高于 \(c\)，且 \([c,t(\delta)]\) 位于同一个真实 scalar span。
root/collar 报告及相关 germ 方法见
[参数 germ 说明](2026-11-12-parameter-germ-collar-enclosures.md)。

两份完整 bulk 部件为

- [part00](2026-11-12-beta-step3-germ-bulk-h1e8-part00.json)，
  SHA256 d770b0b8cf4e38a61299552117091956910c7950b1456c82cba9c571bc4c2fd4；
- [part01](2026-11-12-beta-step3-germ-bulk-h1e8-part01.json)，
  SHA256 a9b159b54fc8b93d33090f6d3c9b25375f6313de944f15471f400ec388339bb4。

共有 249 个通过叶区间、167 个原始公共 knot 区间，终止失败数零。
所有正负 binary knots 都按准确 Fraction 分段，微小相邻 span 没有被合并；
局部多项式由显式 span selector 选择。腰部 \([0,2^{-20}]\) 用真实奇函数商
的连续有向包络处理。

对每个固定真实参数，径向复延拓的分母门在同一报告区间上成立；
因此验证积分同时包住全族，不要求区间参数自身是复解析变量。
角均值另有完整复角连续覆盖和 Fourier alias 费用。

实际有向加总为

\[
-1233.16984065608<I_{\rm bulk}<-1233.14804814077,
\quad
1307.19828862195<I_{\rm collar}<1307.21966529809.
\]

按同一物理角及 quarter 归一，
\(\beta=(I_{\rm bulk}+I_{\rm collar})/2\)，得到 (1)。

collector
[fourfold_phase_beta_parameter_combine.py](../scripts/fourfold_phase_beta_parameter_combine.py)，
SHA256 335c264bd5c6a4db01f9667e1a3c181cc2bb1600c9ad0480155dd613b1ea3793，
核对对象、origin/direction、参数区间、collar、全部来源 hash 和 Fraction 覆盖，
并用保存的 lower/upper Arb 球加总，不把显示用的 midpoint 字符串当严格端点。

bulk 的按根距离分配的额外精度请求 .04 只决定是否继续细分，不代付未计算误差。
每个接受叶都有实际有向积分半径和角误差；(1) 由这些实际球相加。

## 3. 真正参数 primitive 与曲率第一导数

新冻结源
[fourfold_phase_beta_parameter_derivative.py](../scripts/fourfold_phase_beta_parameter_derivative.py)，
SHA256 608c541c1469bb45f5ec556751998fc3901f8623f6cca0e7eb77062d5821ce96，
先形成同一族的完整方向 scalar germs
\((\beta_\delta,\gamma_\delta,a_\delta,Z_\delta)\)，再准确微分非线性步骤。

在旋转柱坐标基中，
\(T=(-\cos\gamma\sin\beta,\cos\gamma\cos\beta,\sin\gamma)\)，且

\[
T_\delta=
\left(
 \sin\gamma\,\gamma_\delta\sin\beta-\cos\gamma\cos\beta\,\beta_\delta,\ 
-\sin\gamma\,\gamma_\delta\cos\beta-\cos\gamma\sin\beta\,\beta_\delta,\ 
 \cos\gamma\,\gamma_\delta
\right).
\]

同一含零模/奇偶规范的线性角原函数 \(P\) 给出

\[
F_\delta=a_\delta P(T)+aP(T_\delta)+Z_\delta e_z.
\tag{3}
\]

源分别对 \(T,T_\delta\) 施用同一个 primitive 算子，随后实施 (3)。
这里没有有限差商，也没有从截断原函数免费取得无限角导数。

设复域原预算为 \((A,Z,B,G)\)，方向预算为
\((A_\delta,Z_\delta,B_\delta,G_\delta)\)。由

\[
|a_\delta T+aT_\delta|
 \le[A_\delta+A(B_\delta+G_\delta)]e^{B+G}
\]

可在同一无限 primitive 误差公式中取有效幅度
\(A_\delta+A(B_\delta+G_\delta)\) 和高度 \(Z_\delta\)。
物理角导数的 \(J_{\rm rot}\) 作用保留。这里 \(\beta\) 不含背景角，
但所有模界始终是旋转基分量；若切到固定 Cartesian 分量须另付复旋转。

设有限 \(F_r,F_{r,\delta}\) 的逐分量模界为 \(M,M_\delta\)，无限误差为
\(e,e_\delta\)。由于 \(E_\delta=2\langle F_r\cdot F_{r,\delta}\rangle\)，

\[
|E_\delta-E_{\delta,N}|
 \le6(Me_\delta+M_\delta e+ee_\delta).
\tag{4}
\]

先把 (4) 的 Cauchy 系数误差加入完整 \(E_\delta\) series，
再取径向及曲率导数。实系数投影入口显式拒绝非真实径向中心。

若 \(C=a'E'-2a''E\)，则在固定物理 \(r\) 下，

\[
C_\delta=a_\delta'E'+a'E_\delta'
             -2a_\delta''E-2a''E_\delta,
\quad
K_\delta=\frac{C_\delta}{2aE^2}
             -K\left(\frac{a_\delta}{a}+\frac{2E_\delta}{E}\right).
\tag{5}
\]

## 4. 较大参数区间的根导数实证

输入为已冻结的
[germ root h1e5](2026-11-12-beta-step3-germ-root-h1e5.json)，
其共同根存在/唯一性来自同一 R57 参数根证书。新计算收紧已知根箱，并使用

\[
t'(\delta)=-C_\delta/C_r=-K_\delta/K_r
\quad\text{于 }r=t(\delta).
\tag{6}
\]

两个有向表达式都独立包含真实导数，源码核其交非空并取交。
\(C_r>300.25460268\) 保证分母严格正。

[实际报告](2026-11-12-beta-step3-parameter-root-derivative-h1e5.json)，
SHA256 3284dfe4d3feaa5eeca5f114844c1052b381434fa1bb0c08def1c45d9b845243，
证明

\[
\boxed{
6.11078827432\cdot10^{-5}
<t'(\delta)<
6.11081247826\cdot10^{-5}
\qquad(\delta\in\Delta_5).
}
\tag{7}
\]

报告保存准确参数盒、根箱、对象和方向、512 点无限 primitive 费用与
\(E_\delta\) 费用。此项尚未支付
[物理参数相位导数公式](2026-11-12-physical-parameter-beta-derivative.md)
的完整 collar/bulk；不能把 (7) 当作 \(\beta'\) 的界。

## 5. 重放

~~~bash
OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_parameter_combine.py \
  --center-object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --collar notes/2026-11-12-beta-step3-germ-collar-h1e8.json \
  --parts notes/2026-11-12-beta-step3-germ-bulk-h1e8-part00.json \
          notes/2026-11-12-beta-step3-germ-bulk-h1e8-part01.json \
  --out notes/2026-11-12-beta-step3-parameter-h1e8-complete-enclosure.json

OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_parameter_derivative.py \
  --center-object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --root-box-report notes/2026-11-12-beta-step3-germ-root-h1e5.json \
  --out notes/2026-11-12-beta-step3-parameter-root-derivative-h1e5.json
~~~

