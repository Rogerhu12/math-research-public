# R345：actual161 的单 field 全 230 列严格认证、持久 128 位末态与未付全场责任

## 345.1 实际结论

actual161 在同一公开 Actions job 内重建原输入、fresh binary64 全 J / R273 候选和持久 binary128 末态，随后对 **stage 10 / RK step 0 / field 0** 的实际保存输入，完成 **224 个 shape 方向及 6 个独立环境方向，共 230/230 列**的严格区间消费者。原报告的每一列均为 complete、all_226_rows，两个 mean 分量保留；没有未访问列、区间未决或科学预算截断。认证对象是固定实际有限 root trace 对应的准确实算法及名义计算值误差，条件是该 field 的保存输入 words 被视作准确常数。

该结果没有认证整段 RK、全部 576 段的导数、112 边界响应、338×112 endpoint sensitivity 或原物理 audit；也没有把 C 当作 F_e，没有证明实际返回值是 F 的精确根，没有证明分支稳定性或 IEEE 舍入映射的导数。native_accepted、fullDN_completed 仍为 false。

同次持久 128 位 owner 的独立事实是：一个方向、唯一一次 α=1 试步被原严格残差下降规则接受，完整 shooting 残差到达原 2e−9 阈值；独立 fresh replay 的全部 226 输出及全 residual words 与 owner 相同。这与上一段单 field 的严格证书是两项不同责任，不能合并成 native 最终接受。

## 345.2 官方来源与原文口径

| 项目 | 实际身份 |
|---|---|
| run | 43729456722，attempt 1 |
| source commit | ce2b12c0f391a008343866ed9fe649f44d91ed28 |
| compute job | 132858464847，success |
| report job | 132905673489，success |
| 原 request SHA256 | 0af82d3e294ac39e19b5712bf7bdf629c8a8abee747dd35f886dba790d8cceb4 |
| compute 原日志 | 1331742 B；9fdae9c16b7773086b4dc6fe04a51cc96c92b1ad29bfc8bb40bcd0fb2037a664 |
| report 原日志 | 90652 B；ed93bc85ac08f66a2d4c0f2fbdd6cfb08e361c5de9b2ee1887fd9e8913d59cea |
| 最终短摘要 | 42969 B；37e9f0c078c6c98bbe254768076884b2c93fb4deaca6c765b044c43a72fedb26 |

最后一行按原 BEGIN/END 帧中 JSON **不含分隔 LF** 的字节计。compute 声明的 bytes/SHA 与 report 原文本逐字相同。此次回读只做原 JSON、词法数值、字节和范围核对，没有本地重算模型、范数、区间或误差界，也没有重新下载旧大 artifact。

原报告记录 61 项请求 source pins、严格 field consumer 的 18 项源闭包。它们的来源及原执行声明保留在该 run；本结论不把这些声明写成又一次本地编译或全部科学 payload 独立复算。原可重算大输出不另存 Git、Release 或 artifact。

## 345.3 fresh 输入、R273 与持久 128 位求解

本次从原真实初猜重新得到当前完整 binary64 J、r、σ 和 R273 方向，没有用被删 packet 或 hash 伪造续接。原完整初猜 state SHA 为 f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6；fresh snapshot result 为 1316 B / d6f10e2361e0fe38ca4204b03226613060fdb71440b054e18763db0fc578d4cc。

fresh R273 原读数为 577 nodes、576 stages、129248 rows / columns、258496 augmented rows、1153 次 QR、1152 次 formation，η=1；factor 与 constant 合计 464891392 B，记录耗时 28.414936499000078 s。其全部 129248 行 exact readback 的原 affine 最大值为：

$$
9.685623139820915231844260456306540893890861679791289092058094119\,10^{-11}.
$$

这只是该完整形成模型的原读数，不是当前 binary128 映射导数或其误差上界。方向原 raw SHA 为 4bb396b069f5c32a3d77a08531ad2cdefbd3ece7fd8f63c56baed84f13976ce6。

owner 明示策略为 fixed fresh64 J chord matrix + current128 RHS；fixed64_J_is_current128_derivative=false。状态及更新保存在 binary128，没有经 binary64 回写。

| 原阶段 | 完整归一化范数原 decimal | 原责任 |
|---|---|---|
| initial | 0.000122096054597410989492629881621789239 | 576 stages / 129248 rows，未到 tol |
| direction 0、trial 0、α=1 | 9.68582474751023176032080482454992093e−11 | complete=true，strict-original-norm-decrease，accepted=true |
| 独立 fresh replay | 9.68582474751023176032080482454992093e−11 | 全 cut / stage / far，全部 226 输出和两 mean accumulator |

initial 最坏行为 stage 11、输入 node 12、输出 node 11、Pi104、global2791。末态最坏行为 stage 9、输入 node 10、输出 node 9、Q1、global2128，原 residual=4.99890220172700756918252291853272271e−25，原 σ=5.16104960810073433235339041548094359e−15。末 norm 的 binary128 hex 为 0x1.a9fcb11a67aa9fdf970095730bcp-34。

唯一试步耗时 993.596182379 s；126690 个 binary128 state words 改变，其中 11183 个改变后 cast 到 binary64 仍同值。这里只保原计数，不能据此替整段形成误差作归因。初末原 mean_height_sum 均为 0.0226842463487103007695708959242220956，两个 mean 的逐输出责任仍由完整原记录保留。

初始、试步及独立 replay 的每次完整评价均记录 27772 root calls、904 次 Newton / line-search 更新、maximum_iterations=1、fallback_returns=0。末态 max_returned_relative_decimal=7.97942273584970897156361583077509912e−14；原 root stop 保持 8e−14 的原 binary64 常数提升值，fallback 常数仍为原 5e−12。没有换成 refined policy。

owner stop_reason=shooting-tolerance-reached，directions_computed=1、accepted_steps=1、trial_evaluations=1。方向 1…31、该方向试步 1…9 未访问是前一接受与 tol stop 的实际后缀，不是把它们记作通过。原 32×10 上限和严格 σ 范数规则仍在。

final-state.f128 为 2067968 B / e0f20c36d59ac200796a03441e7b5604224e3add414361a11cc6ff3586dffba2。完整输入 packet 为 10348368 B / 1c9df6b2aa203d526eee11fe443ebcb474c677b76ed3901b6a0f6c1f37aa8；packet binding 为 3679 B / c920fea370f66d81d7a472e7b36b1543103598c3c0914bfc430e10f20772fa74。严格 field 消费的是此实际末态，非原失败初猜，也非旧 64 位末响应。

## 345.4 单 field 的准确对象与实际覆盖

选择明确为 stage=10、RK_step=0、field=0、policy=original，angles=2048、modes=112、state_dimension=226、shape_dimension=224、root_dimension=113。实际 trace 有一次接受更新，update=0、backtrack=0、fallback=false。

export 完成 230/230 列，原 independent_gram_rows=225、root_rows=113、state_rows=226，elapsed_seconds=20.642。原 packet 的全部 literal frequency/cosine/sine/Gram words 匹配；Gram 是独立表，未重新生成 literal square roots。

严格消费者沿已发表 R325 的条件链支付名义形成误差、C 区间与逆比较、准确 solve 对名义 solve 的包含、方向中 DC 对准确 solve 区间的作用及固定更新的传播。此次原 update 记录同时为：

- accurate_C_SPD_certified=true；
- inverse_comparison_certified=true；
- all_113_solve_rows_included=true；
- all_225_gram_terms_included=true；
- formation_at_actual_nominal_e_words=true；
- propagated_C_box_is_separate_from_point_formation=true。

这明确区分了在名义 words 上的形成误差与传播到的 C 盒。每列 root_updates 都保存 actual_accurate_solve_interval_used_in_DC_action=true，不能把名义线性 solve 的残差或其导数默认为零。

原 230 个 column ID 恰为 0…229，各列 complete=true、all_226_rows=true，均有两个 mean_error_uppers 和该完整 update 记录。0…223 为全部 shape 方向，224…229 为 6 个**独立**环境方向；没有把它们直接当成沿上游 RK 传播的环境响应。unvisited_column_suffix=[230,230]。

完整列对象原 canonical identity 为 118671 B / 980b8d5cb1e592352f2dc775d57891557bed2cb03130f823c502d7d11da6f132。本节只保全范围结论、原身份及必要标量，不把 230 列长整数科学表搬入仓库或要求其成为另一道接受门。

## 345.5 必要严格上界的原字面值

下列均直接取原记录；整数没有在本地转换成小数、重新取最大值或改变误差定义。每项为所列非负整数乘 2^-320。

| 原字段 | numerator |
|---|---|
| complete_226_output_error_upper | 71472161905941196696405043748288331071616520615384388662655 |
| mean_output_error_uppers[0] | 400232332461531486256974143263587189 |
| mean_output_error_uppers[1] | 0 |
| returned_accurate_F_upper | 6540573834712077252608585890559911864500480062721 |
| primal_updates[0].q_upper | 1855710191003216442337894220028345349378467697690672199264795576 |
| primal_updates[0].exact_solve_error_upper | 20694150689052633160934295714264646070114 |

前一行 226 输出误差是该固定输入、固定 trace 的 field 责任。两个 mean 的零或非零界也仅属于该对象，不能外推成全尾 mean 的精确数学消失。returned_accurate_F_upper 是返回点准确 F 的包围；recorded_returned_F_is_not_asserted_zero=true，actual_equation_root_enclosure_proved=false。它不证明精确根存在或已找到。

严格消费者原 bits=320、seconds=9000；实际 elapsed_seconds=5583.405569128001，procedure_completed=true、requested_columns_certified=true、fixed_trace_primal_field_certified=true、budget_exhausted=false、unresolved=false。完整结果中没有把有限 word 运算图与准确实轨迹作无条件同字等价；这里的条件包含依赖 R325 明确的对象与前提。

## 345.6 编译修复、实际 stderr 与传输恢复

R338 的 actual150 未进入严格算术。161 使用独立 v2 qualified shim，SHA 5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf，固定 source SHA 后仅在 Actions 临时编译副本加显式全局 quoted 的词法空白和 BatchStats 命名空间。

实际 exporter 副本 13519 B / af2f46fd754ab4282e0e79500c5a19122c30e6a352145b9bef2f686ef2d10a34；原 exporter 为 13437 B / 2aa2ad6737ca16854350967bddf49846e345ba5195d799d21dcc40a870c925bb。记录包括两处 quoted 替换、三处引用参数类型及一处局部统计类型的明确限定。operator header 副本 24653 B / 4610e1e851a1f3b51f829355f08ef4555d1dc212b61f193db2edce5bb2a13435，原 header 为 24617 B / 950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0，12 处 quoted 替换。原 Git 文件、数值表达式及预算未改；两份 inverse_whole_source_equal 的原记录均为 true。

编译实际命令保留 g++ / gnu++17 / -O3 / -fopenmp / -frounding-math / -ffp-contract=off / -fno-fast-math / -lquadmath。编译 returncode=0、4.32237853999959 s；四份严格 component / certificate / compiler / exporter stderr 均为实际 0 B，SHA 为标准空字节 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855。没有把旧编译错误改写为数学失败。

这里仍存在必须分开的传输状态：子 launcher 原 returncode=70、original_launcher_summary_complete=false、child_summary_transport_complete=false，原因是其短摘要超限。严格 consumer 原 returncode=0、summary_complete=true；完整结果已在清理前保留，并由同 job 父层读回：

| 同 job 原件 | bytes / SHA256 |
|---|---|
| certificate/result.json | 127961 / 2d66be24ea779c2f7054dcf54284c2db257f8fb53e265c27e30a6efa8fd7de6a |
| launcher/result.json | 180408 / a65b38bd4f97a6c1e1fad3f5b7122f8d6fabedccc82e7fb1ada036996d7a2a52 |
| 严格输入 binding | 97041 / 41d2ed35094f62c563bb87893bcacba3a08b81fb5fb42fcb35e34686144df607 |

原父层明确 child_transport_failure_recovered_from_actual_full_result=true、full_result_readback_complete=true、launcher_original_full_result_readback_complete=true。回读对原日志协议的 279 + 922 个成员完成词法数值保留及原整体 SHA 核对；这只是原协议的数据完整性，不是新科学计算。本结论不另传或保存这些大原件。最终 compute/report 的有界摘要 summary_complete=true、transport_complete=true，整体 actual_error=null。

整个请求 elapsed_seconds=9801.570440672；owner 实际 elapsed_seconds=2999.6484720140006，清理前 certificate component elapsed_seconds=5610.04999538。原局部耗时与总耗时保原口径，不借其推测全 576×224 证书在一个 job 内能完成。

## 345.7 尚未覆盖的责任与可复现入口

下列原 flags 均为 false：

| 尚未支付项 | 此次边界 |
|---|---|
| field_input_upstream_RK_error_certified | field 的保存输入固定；未包围前序 RK 误差 |
| complete_RK_stage_certified / complete_576_stage_columns_certified | 只一个 field，不能合成整段或全 stage |
| complete_cut_stage_far_129248_certified | 完整 shooting **数值** replay 已做，严格全行证书未做 |
| complete_112_boundary_response_certified | 未获得完整112边界响应 |
| endpoint338_by112_sensitivity_complete | 未获得真正338×112末端 sensitivity |
| original_geometric_final_audit_complete | 没有用旧64 audit贴到当前128末态 |
| actual_equation_root_enclosure_proved / dynamic_branch_stability_proved | 固定 trace 证书不证明真 F 根或实际分支稳定 |
| direction_of_IEEE_roundmap_claimed | 没有声称 IEEE 离散舍入映射的导数 |
| native_accepted / fullDN_completed | 整体目标仍未完成 |

原64 worker 在首次试步前由 PERSISTENT128_CONTROLLED_ORIGINAL64_STOP_AFTER_INDEPENDENT_OWNER 受控终止；original_driver_exit_code=2、original64_nonlinear_trial_calls=0。这不是新一次十档拒绝，也不是把128结果回填为64 native响应。

复现使用上述 source commit 中的原161 request/workflow，按其61项 pins 重新恢复原91来源、两 ready、78源，再 fresh fullJ/R273、持久128 owner及清理前证书。严格消费者为 exact_20261115_literal_root_field_certificate.py（40570 B / 659ecdc003eb54a4fc22b8b42828a2b33f576690559de14b7cde54d7efe11849），原 CLI 为 --bits 320 --seconds 9000 --first-column 0 --columns 230；export 位置参数选择 stage10 / RK_step0 / field0 / original policy，作用在本次真实 final-state.f128，不允许只凭其已删 raw 的 hash 伪造恢复。

R325 的已发表完整证明身份为 14028 B / 1caa1276575e7cb86ee151dcb15c1736bd9b2e5e5b4e5245f1d24cf0cac20081。actual161 首次把该固定输入、固定实际 trace 的 230 列消费者完整执行到证书；下一步全场责任仍须使用真实现场和对应完整输入单独实现，不能由本例的范围外推。
