# R387：actual178r2 再次八次接受、91342字节读回超限与正确保留临时现场

作者：ChatGPT（/root/amplitude）；2026-11-15。

**可信度：已核原运行元数据、两个原job日志及其单份小fallback，属于实际计算与工程范围结论。** 本次未重新计算模型、merit、J、FD或区间。全科学原状态只在Actions内生成；缺失的初末参数/残差/逐trial值不能从计数、字节长度或哈希补出。

## 1. 真实结果

Request178r2 的科学producer退出0，再次记录8个接受点，并以原8方向预算结束。整个compute job失败的直接原因仍是reader返回70：此次形成的必要摘要为91342 B，超过保持不变的90000 B上限。新清理逻辑实际跳过了主动删除，符合r2修订合同；这没有提供跨job持久保存，也不表示已读回91342 B正文。

这与[R377的首跑](R377-actual178-eight-ten-coordinate-acceptances-and-readout-limit.md)是两次独立运行，不能混用状态SHA或把相同接受计数当成参数/轨迹逐字相同。

| 项目 | 本次actual178r2原值 |
|---|---|
| source | `01dc5cbe49e98aae5acb241564946d839b408d33` |
| run | `43751514766` |
| 创建 | 2026-11-15 19:16:44 UTC |
| compute | `132926288393`，completed/failure |
| report | `132926767769`，completed/success |
| producer child_exit_code | 0 |
| reader_exit_code | 70 |
| started_experiments / completed_experiments | 1 / 1 |
| scientific_diagnostic_completed | true |
| phase | `diagnostic-completed` |
| accepted_point_count | 8 |
| stop_reason | `Explicit eight full-ten direction budget completed` |
| wrapper_wall_seconds | 55.039101174999985 |
| explicit_wall_termination | false |
| received_signal | null |
| wrapper_exception / traceback | null / null |
| post_step_reader_exit_code / post_step_reader_exception | null / null |
| temporary_wrapper.partial | true：读回未完整，不代表数学试步失败 |

compute原前七个步骤全部success；第8步“Eight joint ten-coordinate directions and original20 full3 trials each” failure；第9必要读回、第10错误保全、第11条件清理均success。report success只表明小fallback已转发，不能解释为完整科学结果或全部final gates通过。

## 2. 两份原日志与唯一小摘要

本次由负责agent各读取一次官方完整compute/report日志，原字节身份为：

| 原件 | bytes | SHA256 |
|---|---:|---|
| compute原日志 | 77752 | `e4657db19f6017ecc99f68fd97585e81592eaff2d4503737116cf6b7a636543f` |
| report原日志 | 16157 | `e9a6954626f4faed0346295d068d6d0765163b5eaa5253729a2acaec960c1759` |
| 单份最终fallback，不含分隔LF | 5727 | `7dff7a59b93664cd3312d32a98f2b3adf0314200613d36e5aedb60e6f6632760` |
| reader自身fallback，不含分隔LF | 4347 | `6686464089ba7e513786a58d030532727c88cc71587a99e2614dff80ba26ddc7` |

解析时只从每物理行移除单个行首BOM与严格锚定GitHub时间戳，保留原日志字节另核SHA；提取
`BEGIN_VISIBLE178_COMPACT_SUMMARY` 与对应END之间原JSON。compute与report标记的5727 B摘要身份吻合，没有以重新排序JSON代替其原字节。

未运输的两个实际原对象：

| 对象 | bytes | 原报告SHA256 |
|---|---:|---|
| 科学status | 970477 | `79039666f9eb81e0f94a37784c341c1697230387faec7450909e807779a1e392` |
| 超限必要摘要 | 91342 | `260082931bd2779d97be0def3531c8bbda979980d662de5f697484d42fd0a3e1` |

这两项为Actions原报告身份，未通过小fallback运输正文。没有按大数据分片/编码方式把它们拉回，也没有重算它们的科学值。

## 3. 超限具体范围

实际fallback保留了摘要各字段原编码字节数。与研究所需数据直接相关者包括：

| 原分区 | bytes |
|---|---:|
| all_original_outer_rows | 16577 |
| all_original_real_trial_rows | 21039 |
| last_original_direction_model | 7880 |
| initial | 6409 |
| final | 6456 |
| initial_binary64_projection | 3940 |
| final_binary64_projection | 3950 |
| original_complete_circle_check_at_binary64_projection | 3021 |
| complete_scalar_domain_at_binary64_projection | 987 |
| complete_planned_outer_rows | 1463 |
| original_readback_coverage | 2049 |
| fresh_original_nine | 1352 |
| zero_extension_literal_readback | 1197 |
| selected_shape | 1125 |
| new_ten_literal_binding | 1178 |

这些都是字节计数，不是对应字段的数学内容。例如final存在6456 B不能说明其FD通过、某个奇异值有效或原unit tolerance已达。相同字节数也不能证明两个数值/对象相同。

原r2源在Actions内先处理全部原outer/trial/FD和已有shape分支，再做语义选择；本次小fallback没有带回其完整coverage对象或原FD数值。因此本文不能把“源码要求遍历120项”升级成“下游已逐值核完120项”。八次接受/原budget stop有实际小值证据，其余缺失细节必须另一次真实必要读回支付。

## 4. 进程与日志事实

原producer stdout为436 B /
`e467603c81c4fed3385cb700eda136c99d163cf0fb9c637b736cea7ca489b259`；
reader stdout为8764 B /
`6692be03696966254d785a0b6e1db2cf3bf3dec724727f1480175d02cc054cb7`。
workflow按r2合同只报告这两份stdout身份，没有把可能含科学表的stdout编码分包。
不能据此声称已读取其正文。

producer与reader stderr都为0 B，SHA均为
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`。
原完整错误步骤确认空stderr；本次不是一个stderr中被掩盖的科学异常。

已读wrapper小metadata明确：没有外部signal，没有显式wall终止，没有wrapper exception。
stop确为原8方向预算，而不是继续循环未收敛时被超时杀死。预算结束不代表研究完成；
完整native、非零场、全曲面同g/嵌入/reach等仍不由本诊断得到。

## 5. 新清理逻辑按预期跳过

第11步真实打印：

```text
event = request178-temporary-payloads-not-explicitly-deleted
necessary_summary_and_owner_quiescence_not_both_verified = true
actual_metadata_error = AssertionError()
only_current_ephemeral_runner_storage = true
no_artifact_Release_or_Git_upload = true
scientific_acceptance_not_inferred = true
```

reader metadata complete在超限分支为false，故必要摘要成功与owner静止两项不同时满足；该事件与r2源码守卫一致。旧首跑的无条件删除没有重演。

这里不把通用 `AssertionError()` 冒成单独读取了全部清理收据，也不从该skip事件单独推断某个PID仍运行或已退出。它准确说明的是**未执行显式raw清理**。这些文件仍只处于已经结束的ephemeral runner，没有artifact/Release/Git备份，runner销毁后不能承诺可恢复。下一次运行必须据原公开配方重新计算，不能以“未主动删”虚称能继承本次末状态。

## 6. 数学源、父点与规则责任未变

本次request为46521 B /
`c7ee49c60e8bc938d8a2d2e9f6b15c0f773857d0183d90de1ce1487c282a075f`。
wrapper为21817 B /
`d0fa9a4c507af63f275dc2a9792dc985a31986382a078710342ad4536e9e9590`。
reader为44505 B /
`4094e8fa2413e6fca4a0f4c64dadd0279de6772163c1cd060c73347e038ced16`。

原search `6b55a6d2…`、producer `3e5c8a34…` 与8891 B配方
`c8bb1ca8…`不变。此源从实际157末九个Decimal词、独立ξ=0重新形成完整十坐标，
固定support1/power4与物理尺度；不借首跑178的丢失末点。
8×20、全3未加权merit、strict slope、原binary64 0.2准确lift的Armijo、初末120FD、
scalar Arb/453圆/112终端责任均为原源。所有source/四输入前置步骤本次success；
不冒本地重新执行了它们的科学求值。

原规则runner实际完成一次同步：2026-11-15 19:17:23 UTC，
读 `eabcad137ef7d93dc99f4e1ca0087bdab0bd4821`，
普通推规则行commit `193100f873cb1a281bc782642caf8b2c0ddcce7c`。
reviewed root/topic仍21bd547f…/bff8aea…。本次没有根据metadata success跳过原规则监控。

## 7. 直接后继

本次再度八次接受支持继续读取完整联合十方向的真实科学量；并不能由计数判断改善有多大、最终条件数、响应精度或哪一个原最终门已满足。

下一r3仅修metadata必要结论：完整八个d/Jd/slope/接受词、全部真实trial标量、
原initial/final十p/F3/merit、120FD原覆盖/最大值/失败及全部原final flags必须返回。
末Q/R内部basis和投影描述重复可进一步只留明确身份，给90000 B上限留下实际余量；
不减少科学方向、试步或FD，不把上限改大，不在本地重算。
原静止+必要读回成功才清理的生命周期保持。

r3是沿同actual157公开配方的第三次独立运行，未来actual编号R389；
本结果R387不含其未来run、参数或接受情况。180准确R323 coast修域则是另一条明确目标线，
不将本字面有限十族的接受计数当作准确coast可行性或已接受BVP。
