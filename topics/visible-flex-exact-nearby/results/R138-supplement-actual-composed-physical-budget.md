# R138 补篇：完整复合物理预算的实际结果

2026-11-20，维护会话 `visible-exact-astra-ac637-20261120`。

## 1. 新预算已完整完成，所选充分门仍未通过

公开 [44740320925/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44740320925)
执行 [Y 完整复合公式](R138-supplement-composed-physical-Hessian-and-smoothing-budget.md)
和 [对应消费合同](../notes/2026-11-20-R138-composed-physical-energy-budget-contract.md)，
完成全部4651个共同闭格，保存5个新 supremum、2个新积分和10个
顺序 derived scalar。数值 child 返回0、actual `complete/proved=true`。

这是新预算的成功完成；其 body-only 三个充分比较均为 false。
后者不表示真实算子有核，不证明真实范数达到所用上界，也不排除
更紧的完整能量估计。独立根型常数尚未加入，不能以本条授完整正侧逆。

## 2. 已保存完整球的短显示

下表仅为已保存 integer-midpoint/radius/exponent 球的十进制短显示，
不作为后继数值输入。每项完整75位有向球在
[whole actual](../notes/composed_physical_energy_budget_ci/run-44740320925-1/composed-physical-energy-conclusion.json)
相应键中保留；后继须消费整条球的 upper。

| actual 路径组 | 量 | 中点短显示 |
|---|---|---:|
| `new_scalar_suprema` | `E_0` | 0.00138679802537 |
| 同上 | `E_1` | 2.71940564737 |
| 同上 | `k_0` | 0.000116097738194 |
| 同上 | `k_minus_one_third` | 0.000249559283603 |
| 同上 | `k_minus_one_half` | 0.000373512741419 |
| `new_scalar_integrals` | `composed_k0_squared_integral` | 1.42894180508e−9 |
| 同上 | `composed_kminus_squared_integral` | 6.76397252468e−9 |
| `complete_derived_energy_bounds` | `Volterra_J0` | 3.49457878363e−6 |
| 同上 | `root_Kminus` | 8.22433737433e−5 |
| 同上 | `h_E` | 0.00186937927488 |
| 同上 | `w_E` | 216.851251477 |
| 同上 | `z_E` | 307.040596625 |
| 同上 | `r_E` | 0.0178347324949 |
| 同上 | `r_B` | 0.0197662067258 |
| 同上 | `a_EE` | 66.3158207195 |
| 同上 | `a_EB` | 145.456226275 |
| 同上 | `a_BB` | 79.7552828144 |

actual 中三条实际比较准确为

`E_coefficient_less_than_2=false`、
`B_coefficient_less_than_1=false`、
`cross_discriminant_positive=false`。
其明确诊断假定为 `C*=0; actual root constant remains independent`。
这些标志与完整球相符，未把浮点中点或隐藏的更窄内部值用作判门依据。

## 3. 精确对象与旧成功输入

同一 candidate `ac1d5b98…`、连续 repair `440866a3…`、
`α=6890507429876859/9007199254740992`、
`ν0=−2572625729470897/72057594037927936`、
`η0=−7789843107295549/4611686018427387904` 保持不变。
真实根仍在
`[1191984371497/5000000000000,2383968743003/10000000000000]`；
积分以整个保守左界至 `25/8`，未把未知真根替换为中点。

本条逐原 positive4650行、angular7722行及真正 root germ 组成的
4651闭格消费系数上界，保原3594/6143接口 metadata。
准确共同分割 hash 是
`b86e1b057e14b61d09364dc8dc0969a2650c727104abcdf8d39e67cc9dcd14a6`。
完整 mean、真实物理角和 `DF(Qrepair)` 资格保留；
WVC hybrid 的额外主部差仍独立待付。

[原 X actual](R138-supplement-actual-physical-budget-and-false-absorption.md)
44737045152/1 的 whole scientific SHA
`1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec`
和 whole execution SHA
`999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92`
为完整只读输入，包括其原三条 false 门。
旧根 `Z,Z_theta,P,P_theta` 的单调 majorant 控全正区，旧
`C_E,C_H,A_Theta,C_W,Gamma,E_epsilon,h_B,w_B,z_B` 与
根 density qualification 只读复用，没有重新传播 frame、位置，
没有重新求旧几何常数，也没有重算轴或 mean 分母。

新计算先完整相乘 Hessian 与坐标逆，保 `s,t` 的局部三角项、
全部独立均值秩项以及真实 primitive。`I:H^(-τ)→L²` 的
`17^(τ/2)/4` 和真实 `IC` 小界只用于有资格的 fourfold scalar，
不误授环境向量 `1/4` 的 primitive norm。
每个 derived ball 保存并读回后才参与后继 derived 和判门。

## 4. 公开身份与维护核验

入口 commit：
`6a6e0d39d514ea6a9bb86f78f374c268533cfdf5`。
实际数值 checkout：
`2db09695e67df56afa00a836d02669c49b698cdf`。
数学 wall `3.221159022000002` 秒；
child wall `3.357561271999998` 秒、返回0。

| 完整原件 | bytes | SHA256 |
|---|---:|---|
| [复合预算 actual](../notes/composed_physical_energy_budget_ci/run-44740320925-1/composed-physical-energy-conclusion.json) | 8482 | `19b489ce0b8b85d4223ea334f7e2397188755d42605bf7613d2023ac69cb2cf3` |
| [完整执行回执](../notes/composed_physical_energy_budget_ci/run-44740320925-1/execution.json) | 15211 | `2e4cea611a229dbf894bae1fb2478ebc2219f9c0282a84cae1abd32ceb54f084` |
| [执行说明](../notes/composed_physical_energy_budget_ci/run-44740320925-1/report.md) | 838 | `22ff76468328ec41a296c69a7210fd4aae8104272cde87ced96f0cddd9fbbc81` |
| [输入清单](../notes/2026-11-20-R138-composed-physical-energy-budget-inputs.json) | 12584 | `c12794d7b0e817332ad57395ebbf206582b2779a02ee38292dec1e622fc8c197` |

维护会话已核19 current 原件 bytes/SHA256/Git blob，与 execution
完整 receipt 列表逐项相同；全22顶层字段、完整 scope、17个
scalar records、9原件恢复回执及原接口/参数/partition身份整读通过。
9历史清单与已审 X 原清单相同，恢复后只读原字节，不调用原 producer。
5次实际 pull 的规则摘要链及首条/末三条完整回执保留，
所存四条根/课题 README diff 皆空。

实际保存的 `old_scientific_target_calls`、
`old_primitive_calls`、`old_geometry_ODE_calls`、
`old_frame_propagation_steps`、
`old_energy_constant_targets_recomputed` 均为0；
没有新数组、Artifact 或 Release。此预算成功冻结，不重算。

后续只为真正更紧的估计定义新目标；根有限型/无限尾、
非齐次根常数、体吸收、真实全频逆和最终固定度量可见族均继续未付。
