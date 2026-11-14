# 前向真实密度流水线独立审查

日期：2026-11-12。审查者：constructive-route 子代理。

本审查逐项读核主连接及其有限 Fourier、time-circle、真实场和参考域接口；没有重复运行已经完成的 turn0 大型采样，也没有把仍在运行的后续 leaf 视为已通过。

## 1. 精确绑定和实际范围

第一版冻结源为 `scripts/fourfold_forward_density_pipeline_turn0_v1.py`，SHA256：

`6fcfe5ff8c4e3ffb9c79f9a613c6bacc244b3a6b707fa78f558cd8933b16342f`。

实际完成报告为 `data/phase_ring_continuation/step5_forward_density_pipeline_pilot0/forward_0000_ef134f2a18.json.gz`，SHA256：

`a6c8560ac4b34a53bb4636c55d4e9672c875156df95f3e975b46947bab15be15`。

它只证明准确 delta5 对象、前向第 0 段、单个 root germ 的完整连续真实密度。这一段没有相邻 spline cap，因而 v1 尚未显式核验跨 cap 所需 C4/C5 的代码缺项不影响这个实际报告。不能仅以 v1 的 raw cap 调用向其他跨 germ 段转授。

第二版审查时的 `scripts/fourfold_forward_density_pipeline.py` SHA256：

`a977d79a16ea06f0683ffcd304e10234f60e6d005048ebbd7dee3c3be13e384d`。

本审查确认其新增完整有限矩形删尾、公开真实 cap API 接口和 root-nodes 默认值更新；不预先断言它的任何新运行成功。

## 2. 真实场到有限密度的连接

`run_leaf` 先独立核对参考与真实场的准确 PiTime 端点、归一子段、delta 分数、object/root SHA 和分支符号。共同径向根虽以不同 Arb 球计算，表示的是同一准确 root；没有将旧浮点镜像图作为这个对象。

参考的实时像门及 `Re Y_x>0` 门覆盖整个工作标签带。由浮点 `ceil` 提议更宽有理物理角带之后，源立即用有向比较验证 `image < physical_strip < true_field_strip`；浮点只提出候选，不参与包含结论。

有限场 P 在真实物理带的误差先由真实场 time/Fourier 双补集、采样球、DFT 与 dyadic 选择费用支付。随后只有在实时参考像中使用

\[
 |g-g_P|\le |h|\,\|f-P\|/\inf|Y_x|.
\]

这个费用没有作为宽复时间参考采样的白噪声反复放大。宽参考 bidisk 上只计算完整有限 P 的模数，P 是整函数，不要求真实场在该更大像中延拓。有限代理

\[
g_P=(hP(Y)-Y_u)/Y_x
\]

的外域界确为 `(|h| MP + MYu)/m_q`，再支付独立 time/Fourier 补集。`h` 在这一行出现一次，后面的归一时间积分不再次乘它。

`circle_time_coefficients` 的共轭半圆复用成立：实际 scalar、root-deflated 分支、准确实系数有限参考均满足 Schwarz 实性。实标签上的 time-alias 系数因此为实数。`choose_fourier` 将它们取实中心，并将节点半径的平均付给每个角 DFT 系数；这是单位化 DFT 的三角不等式。另将 DFT 舍入及 dyadic 选择的最大误差付给每个保留系数。负模由正模共轭定义，均值保留。没有把非零小系数当作零。

## 3. 有序积分及余项

设准确选取的有限密度为 `sum_i a_i(x) u^i`。源完整保留

\[
G=2\sum_{i\text{ even}}\frac{a_i}{i+1}.
\]

局部二次有序积分的偶偶项准确合成 `G'G/2`，奇奇项积分为零；每个偶 e、奇 o 的剩余项准确为

\[
\frac{2}{(e+o+2)(e+1)}(a_o'a_e-a_e'a_o).
\]

源用这条完整恒等式的 Wiener 范数界支付被省略的全部局部二次积分。没有省去均值、最高频或奇偶交叉项。

跨段累计为 `C2 += G_new' * C1_old`，次序与 R72 一致。多项式卷积保留全部新频率，分配长度足以容纳已有 C2 及旧/新一阶积。准确参考各段使用同一初始标签，接缝以准确时间比较；局部 `u` 重参数化由已包含的 h 支付。

`A = sum_i 2||a_i||/(i+1) + E` 确实给真/近似两场的共同积分上界；统一误差是 `2 * base_error + integrated_cap`。最终 R72 费用 `E(1+A/R)+A^3/(2(R-A)^2)` 之外另加局部二次项上界，跨段二次项则实际保留。第一积分涉及除以奇整数，保存为包含球并在重载时验证包含，未冒称这些数仍全是 dyadic。

实际 turn0 完成报告的大小可作为该单段证书使用；完整前腿、平方返回、参数源、KAM 和 PDE 逆仍各自欠真实输入。

## 4. v2 完整有限矩形删尾

`compress_rectangle` 先删去高时间行的全部角模，再从剩余时间行删去高角模。两个被删集合互不重叠，且正好覆盖原矩形与保留矩形的差。因此对于 `|u|<=1`、角带 s，确有

\[
\|P-P_{\mathrm{keep}}\|_{A_s}
\le \sum_{\text{discarded }(i,k)}w_k|c_{ik}|,
\qquad w_0=1,\quad w_k=2e^{\nu ks}\ (k>0),
\]

其中真实物理角场用 `nu=4`，初始标签密度用 `nu=1`。源用每项有向上界，time-tail 和 angle-tail 分别控制在 allowance/2 内，末尾再检查总费用。这个范数只负责有限删除，原来的无限解析双补集仍独立支付。

场删尾后，`actual.total` 加完整删除费，再构造新的完整 P；每个宽参考域的 `MP` 都从新 P 重新求值。故不能误以为在工作带小的删尾也在宽域小，源实际上没有作这种转授。密度删尾后同样先加完整费用，再从保留矩形重新计算 A、一阶积分和局部 J 费用。这些步骤相容。

v2 的 `real_time_reference_cap` 检查同对象、同时间/分支、工作带和实际 C4/C5 provenance。它先在固定物理角证明三重零商界，再仅在真实 cap 的实时间代入参考；公开 API 返回的费用已包含一次 `|h|/m_q`，v2 没有再次相乘。

## 5. 审查结论

在上述明确作用域内，未发现实质数学或连接错误。v1 的实际第 0 段证书可以保留；其跨 cap 泛化不能绕过 v2 的连续性与身份门。v2 新增有限删尾和 cap 连接通过本次源码审查，后续实际运行仍须分别归档真实成功/失败。root-nodes 由 512 改为 1024 是同一真实对象的计算精度选择，不产生对旧对象或未跑 leaf 的证书转授。
