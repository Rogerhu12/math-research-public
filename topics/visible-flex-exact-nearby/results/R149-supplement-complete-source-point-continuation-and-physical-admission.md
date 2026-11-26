# R149 补篇：真实 coercivity 成功后的四源、全 point 与 physical58 接线

2026-11-26，visible-exact-astra-198c63d-20261126 / low_inverse。

本篇提供独立 continuation owner 和必要纯 helper；其前置必须有 R142 或 PS 真正完整保存的六个 defect 球、原 $\varepsilon$ false 门和真实完成的独立 R149 $\theta<1$ 结果。前一执行若在完整六球保存后失败，保留其真实失败状态，由已发布的 R149 v2 完整来源准入证明那六球的资格。没有为当前未知输出制造 actual 文件、manifest 或可启动 workflow，没有运行新科学。此处也不把独立 R149 的一个 coercivity 目标冒充完整 source/point 证书。

## CP1. 三种独立身份和恰好五个新目标

原 R142 的 kind 为 complete_R142_low193_parent_moment_continuation_v1；原准入分支仍要求它 complete=true、proved=false、仅完成其完整 true-coefficient defect，原 saved $\varepsilon\ge1$ 及 strict-low false 原样保留。

新增 v2 来源分支只消费独立 R149 已绑定的 whole_R142_six_ball_false_branch_with_unchanged_execution_references_v2。它允许完整原 R142 false、原 R142 六球已保存而后续执行失败，以及 PS 完整155母格源积分与六球、defect target 已原子保存后失败或正常结束的 false 分支。六球覆盖、193 atoms、1424细格、全部原模型与来源均须全文通过已发布 R149 的同一纯准入；未成的 target、complete/proved、failure 和 returncode 原样保留。实际 R142 的 defect=null 不满足本分支。

独立 [R149](R149-signed-Green-loop-and-symmetric-part-coercivity.md) 的 kind 为 complete_R149_low193_signed_loop_coercivity_v1；其唯一 target 为 complete_same_weighted_body_signed_trace_and_symmetric_part。本篇要求该实际 scientific、execution、manifest 完整成功，且其原 defect、model、refinement、参数、reference identity 和最初七个 source definitions 与前一个完整对象一致。

新增 [owner](../scripts/fourfold_codazzi_low_centre_coercive_continuation_owner.py) 的 kind 为 complete_R149_low193_coercive_source_point_continuation_v1，只登记以下**五个**新目标：

1. complete_ordinary_raw_low_source_and193_atoms；
2. complete_transformed_low_source_and193_atoms；
3. complete_low_second_kind_inverse_and193_atoms；
4. complete_high0_return_source_without_CFB；
5. complete_actual_whole_interval_low_transversality。

旧 Green、旧 defect HS/atoms、新 signed trace 和 $\theta$ 都不是这五个目标。旧完整对象的实际文件与 execution receipts、manifest SHA、全部 current receipts、完整 field/module/gate/target schema 均先核对。只有上述前置实际存在，才能为这个 owner 构造 manifest；缺失或未成不是可填 dummy 的情况。

## CP2. 原全模型与保存好的 resolvent 原样消费

owner 保留原完整 readonly admission/native restoration、原 WVC 全参数族、真实根、全部155 parent、1424细格、193 moving 坐标、原97/96边界和 actual $S$。未公开的同定义 private carriers 如需再物化，只作为新 source/point 目标必需的内部数据；没有把旧 Green 成功再登记。

原 whole defect 六个 norm/HS scalar 从合格的完整 R142 或 PS readback 取得，不调用旧 complete_norm_with_shared_outputs。独立 R149 的 public symmetric_part/resolvent 原件按真实 endpoints 恢复，再绑定同一个 private model token。使用已证 [RL.1–15](R142-supplement-coercive-resolvent-complete-source-and-point-lifts.md)：

$$
 b_W=R_+g_B,\qquad a_W=g_A+e_Ab_W,\qquad
 p_J^{\rm true}\le p_J+a_JR_+b_J.
 \tag{CP.1}
$$

这里 $R_+$ 只读真正保存的 coercive resolvent。前驱必须先保存 $\theta$，再保存 $\gamma$ 并读回其 lower，按那个 lower 计算、保存和读回 $R$；后继核

$$
 \theta_+<1,\qquad
 0<\gamma_-\le1-\theta_+,\qquad
 R_+\ge1/\gamma_-.
 \tag{CP.2}
$$

$\theta,\gamma,R$ 和 comparison_defect_body_upper 四个 public records 在每条 source 输出中直接复用同一个原件，不再把 upper endpoint 反复转成新的 decimal balls。其余新 source/point bounds 则按原 scalar enclosure 写出。source 仍保 strict_low_coefficient_residual_passed=false，另标 strict_symmetric_part_gate_passed=true 和独立 basis。

## CP3. point 只需 Z；旧 defect Y 与 HS 不应重算

原 GM 的 source-moment 3-block 递推中，$Z$ 分支不依赖 $Y$。在每个短 Taylor step 上，原递推为

$$
 z_k=\frac{H_s z_{k-1}+V_s(-H_s^{\mathsf T})^{k-1}/(k-1)!}{k},
 \tag{CP.3}
$$

其 doubling 为 $Z\mapsto BZ+ZA$，最后给 source Gram integral。$Y$ 的递推从 $Z$ 接收项，却没有反向输入到 (CP.3)。

因此保留原 template、degree、normalization、完整 Taylor tail 与所有 doubling stages，只执行这一独立 $Z$ 分支，得到与原 GM 同一准确 source Gram 的有向包含；没有计算旧 defect 的 $Y$、同格 signed 两三角或完整 HS总和。原3-block的统一余项当然仍包住它的这个 subblock，省掉另一支不会缩小余项资格。

配套 [point helper](../scripts/fourfold_codazzi_low_centre_point_covariance_materialization.py) 将这个 $Z$ 用于

$$
 I_L=h\,\ell Z\ell^{\mathsf T},\qquad
 I_R=h\,\rho Z\rho^{\mathsf T},
 \tag{CP.4}
$$

并保留原同格 $O_L,O_R$。其 packet 明确是 point_only_source_covariances_complete，**不含** same_panel_complete_HS2_upper 或 same_panel_both_triangles_in_signed_complete_sum。原完整 norm accumulator 因而不能把它误作新完整 defect HS 输入。原 scalar HS/atoms 仍只读合格的 R142 或 PS 原件。

每个 parent 在同一次 four-source pass 顺带准备这个 point $Z$，共享同一个 H/Q template；各 cell 使用自己的原完整 node frames 和 true $h$。四条新 source 仍使用原完整 GM $Z,Y$ 及两个 signed triangles，没有省掉其任一项。完整 A/B/K output covariance 从 ordinary source packets 准备一次；它们是同一原 Green/S 的 source-independent 数据，并用于四源 batch 和后来的全 point 阶段。

## CP4. 完整 point 覆盖与严格完成身份

point source covariance 的原有递推仍作用于全部细格、完整 $I_L,I_R$。body output covariance 使用原 A/B，不能混入 atoms。point receiver $a_J$ 仍由实际 defect covariance 支付，绝不替换为 $\theta$。全部5696原闭盒和真实 root length 保留；其 matching lower 必须严格正。

完成四源而 point 未成时，owner 只保留那四个实际完成的前缀，complete/proved 不得成为完整低输出成功。全部五个目标、最终原输入 re-read 和完整 scope gates 均完成后，才可以给 complete=true、proved=true。全高反馈、actual-family 差、真实物理外行、七端口和两 WPN RHS仍保持各自原 false scope，待后续实际支付。

运行仍受原公共 runner/单线程/320位 admission和768位数学、内存和6小时工作流限制约束。本篇不承诺 elapsed time；Z-only只是不再支付新 point 目标不需要的旧 Y/HS 工作。某次前缀停下不构成课题完成。

## CP5. physical 三处显式增加新 kind；58/224/32算式不改

以下三个现有非active后继文件增设明确分支：

- [moment_physical_consumer_math](../scripts/fourfold_codazzi_moment_physical_consumer_math.py)：保原 R141七目标、R142六目标的 strict-$\varepsilon$ admission；新 kind 则核独立 R149成功、原false、全部五个新目标、同 saved $\theta/\gamma/R$、每个 source 的一致public records，以及原193 atoms和全point。
- [physical_chain_owner](../scripts/fourfold_codazzi_physical_chain_owner.py)：新分支额外全文消费合格的 R142/PS defect 与 R149 coercivity 各自 actual/execution/manifest，核 exact文件身份、全部原件引用、model/refinement与共同源定义。原 Green prefix仍整体保留。
- [make_physical_chain_manifest](../scripts/make_physical_chain_manifest.py)：只有上述实际成功的低结果存在，才从其 whole-file references 加入这六个真正前驱文件并生成后继 manifest。不得用未来路径或不存在的actual补齐该分支。

complete_new_scalar_closure 的58个公式和其后完整224 ports/32 WPN算式完全未改；这里只使另一条严格付费的低逆证书进入同一数学消费。58门未过或某前驱未成时，不得运行更后一级。

## CP6. 新入口实际需要的 manifest 角色

除原 R142完整准入/输入和七个 immutable definitions外，source-point owner额外绑定 low_centre_point_covariance_materialization、low_centre_resolvent_lift_math 两个纯源，及以下真正前驱：

| 角色前缀 | 完整文件 |
|---|---|
| completed_parent_moment_defect | actual、execution、manifest |
| completed_signed_loop_coercivity | actual、execution、manifest |

具体角色末尾分别为 _actual、_execution、_manifest。operation 必须取本 owner 导出的 KIND、TARGETS、SCI_FIELDS、CERTIFICATE_PARAMETERS、RUNTIME，complete_target_counts=[5]；retained_scope 显式应用 RETAINED_SCOPE_OVERRIDES，不沿用“必须旧strict defect通过”的不适用描述。

本篇没有生成包含这些尚未知实际输出的科学 manifest，也没有启动工作流。父级实际 R149结果出来后，才可读取其真的文件和 receipts完成该次绑定。

## CP7. 成功后实际消掉的 positive radial unknown

若低逆、physical58、ports224、WPN32均完整实际成功，新的直接 inverse 路线已解出整个 ordinary $L^2_r\mathbb R^{193}$ positive radial head；它不是仅认证155或1424个径向离散 unknown。R141 G.29在完整 $L^2$ 上可逆，physical 闭合保同 $DF(Q_\delta)$ 的全部低高反馈；[WPN lifting](R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md) L.5、L.7–16给一般无限径向 unknown与实际 positive BVP的双向等价以及 finite$\oplus$full-tail等距恢复。

因此旧 WHR 路线的“未知 positive radial head 尚未闭”不能机械保留为这个新逆路线额外欠项。仍必须识别 RNS/FC/BT 的 Poisson/readout 与这个同源、同物理mean/height/jump的正侧 inverse；rough natural 输入按其已经付费的 $\Phi/\Upsilon$ 观察进入 L.24，并保原 rough baseline等级（该文第7节）。完整 negative incoming 的 natural/root/waist有限项、真正参数 Schur以及非线性迭代没有因而自动完成。

32表本身是16输出乘两 Hilbert RHS类型的算子响应上界，不是某两条特定 Newton或$\nu$源大小。完整特定 RHS仍须按 L.24–25组装，才能消费它；最终同对象几何与非线性验收仍按 open 第2–7节的真实条件推进。


## CP8. v2 只扩充完整旧六球的来源，不重付数学

source-point owner、metadata generator 和 physical owner 共同复用已发布 R149 owner 的两个纯元数据函数 readonly_decimal_endpoints 与 completed_parent_defect；通过 AST 只取这两个函数及其显式 literal 常数，不导入或执行旧科学入口。被复用的完整源固定为 SHA256 46b11da5fb7430576d8a38555b12f6fa57104dc8effdf2f0b88d11e181afff0b，原始77输入 manifest 和当前全部实际输入仍逐件保留。

新增来源记录必须与真实成功的 R149 certificate 所保存的 provenance 完全相同，包括原 actual/execution 的 kind、run、complete/proved、failure、returncode、targets 和 gate 状态；它不能把原失败执行改成成功。原 six-ball epsilon false、PS 的155完整 source prefix 和真实 saved upper 严格比较均由同一准入重新核验元数据，绝不再次求值积分或矩阵。独立 R149 本身仍必须 whole complete/proved true、child0、全部唯一目标完成。

CP 的五个新数学目标、原16800秒科学资源、全部 source/point 算式和旧原分支不变。physical58 仍只在新的四源/193 atoms/whole point 全部真实成功后准入；v2 未授权跳过任何一项。另一个 NS strict-epsilon 续接入口由其独立[证明](R142-supplement-saved-Neumann-source-and-point-continuation.md)给出，不与本分支混同。
