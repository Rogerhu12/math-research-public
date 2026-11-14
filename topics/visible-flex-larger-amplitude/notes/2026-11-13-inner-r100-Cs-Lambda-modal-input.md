# 同一 R100 内头的 C_S 与 Λd 逐模实际输入

作者：`/root/geometry_audit`（GPT-6 Astra Pro，AI 辅助），2026-11-13。

**已实际消费全部213胞元、全部46条真实低模式列，1051门通过。** 本条给同一 R100 参数域内辅助低场 C_S 和真实齐次低提升 Λd 的逐模、共同强范数输入。它供原全频内头的后续源代入使用，尚不认证新的高频头或高源；完整未知纠正 e、mean、逆及 far 仍须原消费者完整支付。

## 1. 同一对象与规范

使用 R74/R100 的同一旧固定背景及胞元12至224。R100 的前六个 S 轴保留原 R74 复积盒，余40个 T 轴共用

\[
\sum_{m\in T}|d_m|/v_m\le1/32.
\]

C_S 是六个 S 轴变化、其余原参考浅高度固定的真实 low46 辅助解；其域包含在 R121 已使用的完整 R74 二十轴域内。Λd 是同一真实高度图的齐次提升，只有低2至92模式。二者都不是外胞元的 C_L，不能借外 R101 帽代替。

原 R42 正包络记 V_s，R74/R100 使用

\[
V'=S V_s,\qquad S=257/256.
\]

本包所有场帽均在 V' 单位，B 和原 q 的整个连续条带 τ(r) 保持不变。需要原 V_s 单位时，给场帽统一乘 S；far 高度评价不除 S。

对正偶模式 m，帽控制

\[
(1+m)\left(\sup_{I_n}\frac{e^{m\tau(r)}|B_np_m|}{V'}
 +\sup_{I_n}\frac{e^{m\tau(r)}|\kappa_{\perp,m}|}{V'}\right).
\]

这是完整 sine/cosine 幅，即相应正负 Fourier pair 的质量。分量分别先取径向 sup；没有额外因子2，没有交换 sup 与模态和。

## 2. Canonical 谱到同一物理谱

R33(33.51) 的原 V_s 由准确固定 Xbar_n 定义。设参考常宽下某模式的 canonical pair 质量为 c_m，R33(33.52) 的逐模证明直接给

\[
\|Z_m\|_{V',\tau(r)}
\le \frac{c_m}{S\,\mathrm{Xbar}_n}
 e^{-m(\tau_{n,\mathrm{ref}}-\tau_{n,\mathrm{inner}})}.
\tag{1}
\]

因为整个原连续条带不超过进入该胞元的 `tau_inner`。Q 两个物理分量的系数和由 `(Bm+m²)/(a(1+m)²)≤1` 支付，Ξ 的系数由原 μ/μbar≤1 支付。所有原 B、a、Xbar 和连续条带身份从 R42 density 与强提升主包核对；这不是新流积分。

程序以原参考常宽的下端及 `tau_inner` 的上端计算差，故指数方向保守。`exp_negative_upper` 用正 Taylor 部分和 T_32(y)≤exp(y)，对 y≤1/2 取其倒数，再逐次向上平方恢复缩放；因此返回值严格上包 exp(-x)，没有浮点超越函数接受判据。所有正极小项继续以任意指数 dyadic 保存。

cell12 使用 R121 全32次有限代入的最终逐模 complete 和 correction pair 帽。R121 `reference_x12` 经160bit向上记录，略大于原参考192bit的准确 x；本消费者在(1)中明确乘这个更大的保存上界，避免将两个精度的保存值误认相等。原 reference 文件 SHA 和 R121 中的同一引用同时核对。

其它212胞元使用 R74 的完整 canonical 辅助纠正半径 `nonlinear_radius_multiple*x_n`。每个模式可各用此共同帽，另保留共同模式和帽；不会把46份单模上包之和说成原共同半径。

## 3. 使用实际物理线性列进一步交集

原 `closure-strong-parameter-lifts-r1.json.gz` 的 A_upper[n][m] 已经控制每单位浅 canonical Q 的完整真实物理强范数，包括两个分量的独立径向 sup、全 cosine pair 和原连续 τ(r)。原强包络与原 q 包络的精确重权也已经在该包中支付。

令 a_m^S 为 C_S 的浅模态模长帽：前六模式用 `abs(q_m*)+chosen_axis_m`，其余有参考的模式只用 `abs(q_m*)`，26个原零参考保持零。于是线性场的物理逐模帽为

\[
L_{nm}=A_{nm}^{s}a_m^S/S.
\tag{2}
\]

将(2)加上(1)给出的非线性辅助纠正帽。在 cell12，再与 R121 完整场的(1)帽逐模取最小；两条界是同一对象、同一规范，交集合法。共同 C_S 帽另取以下各合法上界的最小：逐模 complete 帽之和、真实线性帽之和加共同纠正帽、R74 完整包络给出的1。全部213个 `alpha_L+rho` 与 Xbar 的准确包络关系均另行核对。

实际 cell12 的共同 C_S 帽显示为 `0.0017090015109056994`，使用的单位是 V'，不是绝对物理振幅。

## 4. 共享横轴预算

令 `t_nm=A_nm^s v_m/S`，m∈T。每个真模式提升满足

\[
\|(\Lambda d)_m\|_{n,V'}\le t_{nm}|d_m|/v_m.
\tag{3}
\]

所以每个模式可保存满半径帽 `t_nm/32`，但共同强质量必须使用

\[
\|\Lambda d\|_{n,V'}\le\frac1{32}\max_{m\in T}t_{nm}.
\tag{4}
\]

本包同时保存(3)的全部列和(4)的共同帽，明确禁止把40轴当作同时取满。若后续正卷积同时用逐模帽和共同帽，可以取有效较小界；不能将单模满半径帽的和认作相同的精确共享质量。

程序也保存全部46个原 R59 单位轴的提升供身份核查；只有后40列参与 Λd。每个 R100 T 轴逐一与原 `R59_exponent` 的准确2幂比较，前六则逐一与 R74 half_axis 比较。far_E 列独立保留，只乘实际轴和共同1/32半径，不做物理目标包络重权。

cell12 的 Λd 共同帽显示为 `3.457823273608309e-33`。C_S+Λd 的每模帽由两份逐模上界相加，共同帽另按两共同上界相加；未包含原完整解纠正 e。

## 5. 可加载结构与实际记录

完整包 `2026-11-13-inner-r100-Cs-Lambda-input-all213.json.gz` SHA256：

`28161832153c4f0b3e632f4c4fba2741b9b90d198a4d75ff5761a18a72c8fa8f`。

小包 `2026-11-13-inner-r100-Cs-Lambda-input-cell12.json` SHA256：

`d85cb3e424a16eff9cee7071483332a1b56bdec2ba6d33b69443838da067c706`。

`rows` 顺序固定为胞元12至224，模态数组固定2、4、…、92。所有场帽的元素均为准确 `[integer_mantissa,binary_exponent]`：

| 字段 | 含义 |
| --- | --- |
| `Cs_complete_pair_caps` | 各真实辅助模式的完整 pair 帽 |
| `Cs_common_cap` | 同一辅助场的共同模式和帽 |
| `Cs_correction_pair_caps` / `Cs_correction_common_cap` | 已包含真实 far 的辅助纠正帽 |
| `all46_R59_unit_axis_lift_pairs` | 原46个 R59 单位浅高度列，在 V' 单位 |
| `transverse_unit_axis_pairs` | 后40列，前六个坐标准确零 |
| `Lambda_pair_caps_at_radius1over32` | 每个模式各自的满半径上包 |
| `Lambda_common_cap_at_radius1over32` | 共享 l1 的最大列上包 |
| `Cs_plus_Lambda_pair_caps` / `Cs_plus_Lambda_common_cap` | 后续完整头源的已知低中心输入 |

正式 r2 运行 exit 0、无 signal，6.563871622 秒，峰58948 KiB，1051门全真。只用原材料、严格有理正运算及输入 SHA；没有新 ODE、Green、Node、径向积分或求解器。

首次 r1 在 `R121_same_reference_x12` 的过强相等检查处正式 exit 1，未产生输出包；原因是 R121 的160bit向上记录与原192bit准确参考略有差异。r1源和正式资源都保留。r2 改成显式向外规范桥，使用更大的保存参考乘回物理单位；没有改原数学输入、R100域或任何原验收阈值。

后续仍必须消费 F=C_S+Λd+e 的全频源，保持原 mean、完整逆、R18 far、旧纠正共同质量以及全部模态支持。此处没有从 R123 的低 cut β 推断任何高头谱，也没有把旧 g 的谱换给新强幅候选。
