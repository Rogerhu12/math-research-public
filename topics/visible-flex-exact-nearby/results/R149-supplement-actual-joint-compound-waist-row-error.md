# R149 补篇：共同共轭的实际完整96行误差

2026-11-27，visible-exact-astra-fb31ed6-20261127。

**实际新增结论。** 公开运行 [45887337009/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45887337009) 已完整保存七个新标量，`complete=true, proved=true`。对 [JC](R149-supplement-joint-compound-waist-row-error.md) 定义的原96个真实 target 和原 L4096/N1024 DFT trial，整个联合行算子的误差满足
\[
 E_{\rm joint}<8.556891\times10^{-5}.
\tag{JCA.1}
\]
这是整个96维输入单位球的 operator bound，包含同一共轭复合误差、原完整 DFT alias 和无限截断尾；不是96个行误差之一，也不是已闭合的 PDE 列误差或有限矩阵逆。

## 1. 完整实际对象

- [七球整件](../notes/joint_compound_row_ci/run-45887337009-1/actual-joint-compound-waist-row-error.json)：17976 bytes，SHA256 `fec83298af0f0bacfe907f9c445cc42f0ed165129cbea18a38cb5d0214ef336e`。
- [完整执行记录](../notes/joint_compound_row_ci/run-45887337009-1/execution.json)：18470 bytes，SHA256 `425ab1174d167392f169cceac24a76e0c7580820a546302d316ba9b7db944695`。
- [输入清单](../notes/2026-11-27-joint-compound-waist-row-inputs.json)：SHA256 `516554f609356ddc801632b88605367df03edeaf0c32830d446bb1090a2a5cf5`，36个当前全件、4个完整历史 native。

Event commit 为 `75bbf6163414dc920d161d5872527bb45740f864`，实际科学 checkout 为 `f8157ea4d7ff6100ee609763ca8b8ad5da475cbb`。Python 3.12.14、python-flint 0.9.0、320 bits；一个科学 child 于2026-11-26 19:56:57 UTC完成，返回0、未超时，七目标全部保存。实际科学 source SHA256 `7c09cb33b99aed216a28ac96f2d93c831e09f543e6b697c85f1809eec63cc8e6`，纯数学 source `61d945c892c6eff232b97164243c2fe5e7edd8593ef6741859eab8b1f55ff694`。

原 W selected run43588332723/1、loss=1/250、物理 strip σ=1/128 保持不变。W、R31、K48、H 四个原 gzip 全 bytes 恢复；原完整 RW 准入检查全部来源。KAM、原 DFT96、旧行误差、PDE residual 和旧范数目标没有重算：`old_numerical_producers_called=0`、`old_completed_targets_recomputed=0`。没有新数组、artifact 或 Release。

## 2. 七个球与严格可用界

下表是整件 `new_records` 的方向界。球的全精度字符串仍以原 JSON 为准；表中十进界向外放宽，不能替代整件输入身份。

| 保存目标 | 严格可用界 | 用途 |
|---|---:|---|
| `Wiener_strip_interpolation_derivative_lower` | \(m_0>0.5559244807648\) | 完整 Wiener strip 导数下界 |
| `saved_derivative_interpolation_lower` | \(m_1>0.9836159091670\) | 已成导数球给出的下界 |
| `complete_interpolation_derivative_lower` | \(m>0.9836159091670\) | 全部同伦及物理角共用下界 |
| `joint96_composition_error_upper` | \(<8.556889341\times10^{-5}\) | 联合96维 composition error |
| `joint96_Wiener_input_operator_upper` | \(<1054.571054\) | 联合复合输入的 Wiener bound |
| `complete_joint96_DFT_tail_and_alias_upper` | \(<1.294437\times10^{-11}\) | 全部 alias 与无限截断尾 |
| `complete_joint96_scalar_row_operator_error_upper` | \(<8.556891\times10^{-5}\) | 两误差完整和 |

最后一球是
\[
[\,8.55689063480853147950215500042690386466328489554148060648647
 \times10^{-5}\ \pm4.85\times10^{-65}\,].
\tag{JCA.2}
\]

前三条保存的是 lower，后四条保存的是 upper。所有后继量都读取正式保存字符串的有向端点：\(m\) 由两个已保存 lower 取合法较大者；composition 用保存后的 \(m\)；tail 用保存后的 Wiener upper；最终和用两个已保存误差 upper。故没有用显示 midpoint 或在保存前的隐藏中间值替代证书。

## 3. 对后继真列和矩阵门的准确作用

按 JC.7–8，\(m>0\) 对 \((1-t)G_o+t\psi\) 的所有 \(t\in[0,1]\) 及全部真实物理角成立，变量替换费 \(m^{-1/2}\) 已付。真实 target 基在其自己的归一化物理角空间正交；pullback 行和 finite trial 行没有被宣称正交。实际 composition 为 \(384E_H/\sqrt m\)，完整 tail 同时包含 \(e^{-4\sigma(1025)}\) 和 \(e^{-4\sigma(3072)}\)，不只算截断而漏 DFT alias。

[JF 联合矩阵误差](R149-supplement-joint-signed-finite-matrix-error.md) 中的共同 row-error 因子可直接取 (JCA.1)。这只替换该**整个**联合 operator 上界，不能对局部行/列块择小后拼接。原真反射轴 \(a=2\mathcal H(0)\)、两 physical means、normalized measure 和 fixed \(J_s\) 不变。

对于原 TC 的 modes≤96 的 trial，\(J_s^{-1}\) 在该有限输入上是恒等，故该项不另乘全空间 \(K_W\)。对于整个 incoming row，原 \(K_W\) 必须保留；对真实 PDE 列误差的 receiver 仍按 JF 保留 \(B_H K_W\) 或 \(B_H/\sqrt2\)。不能将本篇 finite-trial 的恒等关系推广到未截断的真解。

SC 后继只消费本篇的完整七球整件和 execution，不再调用这七个目标。全 P224/TC residual、96个真列误差、signed finite matrix gate、所有高块、两 means 及真正 ν/phase Schur 仍分别待闭合。本篇实际对象中的 `signed_PDE_columns_or_finite_inverse_proved=false`、`full_nu_phase_mean_Schur_proved=false`、`topic_completion_proved=false` 保留。

## 4. 首入口失败保留

先前 run45887144152/1、commit25797fea188f8c678515ed84a8ceb15d0a8c3464 在包装器字符串替换处失败；`reserve` 是 `preserve` 的子串，导致后一个匹配失配。失败发生于 base worker main 前，没有预留新目标或启动科学。修正使用完整消息前缀，并重新生成所有 source/manifest pins。原失败提交保留；实际成功仅指本篇 run45887337009/1，不将两次运行合并成一次成功。
