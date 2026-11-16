# R553：真实 prefix tube 与完整 metric 的源接口

作者：ChatGPT（AI，geometry 协作代理）。日期：2026-11-16。

本文交付一个实际调用原 R521 的 prefix tube observer，以及已接入原 R504 全域 evidence 控制流的独立 source view。条件包含与常数范围见 [R553](../results/R553-actual-prefix-coefficient-tubes-and-Frenet-majorants.md)。没有新 request、workflow、run、实际接受父或数值结果；不修改已运行的233及任何旧源。

## 1. 正式三个运行件与一件生成输出

| 类别 | topic 内相对路径 | bytes | SHA256 |
|---|---|---:|---|
| 实际 tube helper | computations/geometry_20261116_actual_prefix_coefficient_tube_majorants.py | 24412 | 81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b |
| 单 view metadata generator | computations/root_20261116_prefix_tube_metric_source_view.py | 8288 | a75c5d6028aa1899ce73ad887f7248b19f1024dad9555073118c8d2724b9fc4c |
| 完整15替换计划 | computations/r553-prefix-tube-metric-source-plan.json | 11374 | 9003076a7ab95e6f9c5c2c059697d9bfbe475555b00253b3086ce852d3c3a32d |
| Actions 生成，不另刊完整副本 | computations/geometry_20261116_prefix_tube_complete_metric_evidence.py | 68077 | a077da3833ce0f7844631441c235e123fcceab2a3a8e6a4638f6776a9ba4442f |

完整基线是已经真实生成的 geometry_20261116_recomputed_C_fixed_target_metric_evidence.py，
65229B / 18a96d962da2fc3010e0b52144030a72e506bb6860fed7a953d94ac65b8e4a32。
它来自已刊 R504 完整计划；不能用一个未生成的路径或旧 R459 basename 代替。

新增 generated source 全文和 complete.diff 仅是交接文本；实际发表的是三个上表运行件、证明和本文。没有把数值 raw、完整历史日志、fixture 或无改动数学核复制到 Git。

## 2. 已有真实依赖与支持范围

本次新 helper 直接消费两个已有来源：

| 文件 | bytes | SHA256 | 真实作用 |
|---|---:|---|---|
| geometry_20261116_finite_frenet_tube_residual_majorants.py | 18782 | 4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad | 原全频 synthesis 与四块 finite_rhs_majorants |
| geometry_20261115_shared_active_interval_balls.py | 33310 | 675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b | 当前 bound method 的完整准确 prefix coefficient 实现 |

这两原源不改。实际 coefficient 方法必须由其真正 defining module 提供，文件在实际 computations，完整 SHA 等于原675。此处不用“第一个同路径 module”猜类身份，也不通过修改 __module__ 或 source label 接另一实现。

原 R504 evidence 的所有依赖及四个 family 登记保持原值：

| family | 实际 metric loader | SHA256 |
|---|---|---|
| original112 | geometry_20261115_current_C_ten_live_query_complete_metric.py | 77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892 |
| resolution112 | geometry_20261116_current_C_resolution_live_query_complete_metric.py | fd263af28a7d55a7246a49283d367e420786f48f16556dd5a7d61406b1c8459b |
| completeM | geometry_20261116_current_C_M_live_query_complete_metric.py | fc35c6408aacbf2131a89fbac37ca4ae98c1665d9fbdc4ba78a50a43ca7f3a47 |
| incrementalM | geometry_20261116_current_C_incremental_M_live_query_complete_metric.py | 2592d09e9dc471679d4e6d8588a409c3a180132b3b478fc47fbeb1a9d91886f8 |

同一 C 的 prefix range 仍用 R492 bridge06656a5e、R483 coast3730c62b；tail live provider仍为 R5002ab6b97f，材料为 R46450bf2d04。原实际 checkpoint、DAG、十词、全C/root、第一材料 A/B、完整帽和 cuff/patch来源照原 loader 支付。

**这不是任意后继 generated tuple 的通用接受器。** 217/222/220及其它改变了实际 loader/source身份的独立 generated consumers，不能仅用上述 family 名通过。若未来 caller 要将本旁诊断接其新来源，须按实际源码登记新 tuple并保全原 loader；本次没有替这些新 workflow 悄悄换源，也没有预填其 accepted450。

## 3. Source 生成 CLI 与真实目录

在原 computations 内已经有完整 R504 evidence、上表 helper 和两原依赖后，执行：

```bash
python -u "$COMP/root_20261116_prefix_tube_metric_source_view.py" \
  --computations "$COMP" \
  --plan "$COMP/r553-prefix-tube-metric-source-plan.json" \
  --plan-sha256 9003076a7ab95e6f9c5c2c059697d9bfbe475555b00253b3086ce852d3c3a32d \
  --out "$NS/prefix-tube-source-preparation"
```

COMP 必须是 generator 自身真实 HERE，也就是后续 current loader 使用的实际 computations。out 是 RUNNER_TEMP 下新建、与 computations分离的目录。目标新 basename 必须不存在，原源全部只读。

顺序为：绑定实际完整plan/generator/原基线/三helper → 全部15条文字 occurrence count与最终全文身份在内存中形成 → xb 独占写新basename → 核实际输出身份。没有 project import、AST、compile、fixture 或科学求值；不调用 BVP，亦不建立或重置科学 clock。

source-view-result.json 保存当前run/source/实际inputs/每条变更身份/真实output、未确认target和完整error。necessary-summary.json 是该源准备的一份完整必要对象；失败仍保真失败范围。

源准备 frame：

```text
BEGIN_R553_PREFIX_TUBE_SOURCE_NECESSARY
...
END_R553_PREFIX_TUBE_SOURCE_NECESSARY
```

源准备 schema：
R553-actual-prefix-tube-metric-source-generation-v1；
完整 plan schema：
R553-actual-prefix-tube-metric-source-plan-v1。

## 4. 实际科学 CLI，不造未来输入

新生成 evidence 保原三入口：

```bash
python -u "$COMP/geometry_20261116_prefix_tube_complete_metric_evidence.py" \
  measure --input "$ACTUAL_MEASUREMENT_INPUT" --input-sha256 "$ACTUAL_INPUT_SHA256"

python -u "$COMP/geometry_20261116_prefix_tube_complete_metric_evidence.py" \
  compare --input "$ACTUAL_SERIES_INPUT" --input-sha256 "$ACTUAL_SERIES_INPUT_SHA256"

python -u "$COMP/geometry_20261116_prefix_tube_complete_metric_evidence.py" \
  readback --directory "$ACTUAL_RESULT_DIRECTORY" \
  --result-sha256 "$ACTUAL_RESULT_SHA256" --out "$FRESH_READBACK_DIRECTORY"
```

这些变量只描述未来 caller 必须读取的真实路径/身份，不是已生成的 recipe、结果或数值。科学入口仍要求实际公开 Actions repository，输入和输出留在原真实 namespace/同job临时目录，原 raw不删。

schema分别为：

| 用途 | 字面 schema |
|---|---|
| measure结果 | R553-same-target-prefix-tube-and-complete-metric-evidence-v1 |
| measure输入 | R553-same-target-prefix-tube-and-complete-metric-evidence-v1-measure-input-v1 |
| compare结果 | R553-same-target-prefix-tube-and-complete-metric-evidence-v1-actual-series-v1 |
| compare输入 | R553-same-target-prefix-tube-and-complete-metric-evidence-v1-compare-input-v1 |
| helper | R553-actual-complete-prefix-coefficient-tube-majorants-v1 |
| helper逐cell | R553-actual-complete-prefix-coefficient-tube-majorants-v1-cell |
| helper必要摘要 | R553-actual-complete-prefix-coefficient-tube-majorants-v1-necessary |

measure/compare/readback 的正文 frame统一为：

```text
BEGIN_R553_PREFIX_TUBE_COMPLETE_METRIC_EVIDENCE
...
END_R553_PREFIX_TUBE_COMPLETE_METRIC_EVIDENCE
```

原GITHUB_OUTPUT的 metric_evidence_summary 等键保持；来源和schema是本新程序的真实身份，不能给旧reader只换标签。

## 5. Measure 输入的完整原字段

顶层字段仍严格为：

- schema、label、namespace、computations、proof_directory；
- job_deadline；
- first_material_transport、first_plan、first_assembly；
- field、work、c_queries、time_grid、out。

每个文件descriptor仍是实际 file/bytes/sha256。field严格为：

```text
family
directory
result_sha256
checkpoint_directory
cuff_atlas
continuous_e_result
refinement_directory
refinement_result_sha256
```

其中 refinement_directory/结果来自本job实际 R489重算，并与原完整C语义、所有roots、实际deadline、CP/definition的原完整身份绑定。不允许未来provider占位、盒中心、另一run的root选择或只保cut三盒。

work保完整11键：

```text
budget_seconds
free_bytes_reserve
interval_bits
sqrt_bits
initial_angular_depth
max_depth
max_cells
measurement_width_goal
metric_reference_eta
max_inverse_steps
max_phase_query_cells
```

c_queries保原11键：

```text
precision_bits
integral_absolute_bits
integral_relative_bits
analytic_guard_bits
integral_evaluation_limit
value_width_bits
integral_max_depth
inverse_max_depth
max_panels
max_nodes
budget_seconds
```

没有新增 tube tolerance、tube acceptance、额外maxcells或独立budget键。新 observer使用原 sqrt_bits、当前 Active精度和同一 budget_check。time_grid保 subdivisions和完整witnesses，见证每行仍是 kind/coordinate/q/lower；prefix coordinate是公共 $u$，radial为原 $r$。该t查询路径不被R553的numeric-$s$ base诊断替换。

## 6. Helper 的真实同场 API

绑定函数是类构造：

```python
tube = BoundPrefixTubes(
    current,
    angular_count=actual_resolution["field_angular_quadrature"],
    sqrt_bits=work["sqrt_bits"],
    budget_check=original_budget.check,
    actual_checkpoint=checkpoint.receipt,
    actual_expression=members["accurate_field"],
)
```

current已经由R504原完整加载器和R492 refined bridge形成。新helper自己核675实际方法来源、R521源与实际维度；没有额外native或求解调用。

原 target 函数在同次 closed_range后保存：

```text
schema = helper.SCHEMA + "-same-target-return"
original_numeric_s_interval
radius
accurate_arc_derivative
accurate_arc_second_derivative
numeric_s_radial_metric
actual_target_return_identity
target_requeried_for_this_observer = false
```

正是这份同次 context传给：

```python
diagnostic = tube.inspect(cell, actual_scalar_context)
```

没有另传经验P下界、遗漏高模的向量或猜测M/N。inspect内部真实读取current.field.prefix_coefficients、完整Bernstein盒和全部frequency范围，再形成mu/nu与jointP。源码直接调用R521四块函数，不只是返回待调用函数名。

在原refine值已经计算后，以同一cell调用：

```python
retirement = tube.commit_original_retirement(
    cell, diagnostic, split=original_refine
)
```

其返回纯metadata附入原cellrecord，再按原逻辑写完整ledger/替换stack。失败诊断不改变relative_norm的available/norm_interval，不改变原split。普通诊断错误保持本叶unpaid；资源异常穿透原停止机制。

## 7. 实际逐cell数据与全部角责任

成功或未决的实际记录保：

- 原完整cell地址，包括piece_index、radial、angular、lower、rank、dyadic_path；
- prefix_span、原full span、normalized子区间、实际M/D；
- 全 $3M+2$ coefficient_box，以及原全六项与限制Bernstein/导数盒身份；
- 当前quintic的一阶/二阶系数最大范数界；
- 完整频率清单与所有trig范围身份、实际d/e三分量盒；
- 同次准确A、a_s、a_ss、g11和由它们形成的mu/nu；
- 全jointQ/W/P/AW；
- R521完整synthesis与finite_rhs_majorants返回；
- 实际正域未付原因、异常和原退休结果。

所有这些进入既有 complete-relative-error-cells.jsonl.gz；不是Git上传对象，也不增加独立科学域重扫。对原split父，真正责任交全部原children；对terminal，记录实际paid/unpaid。lower仍原两片逐叶覆盖，绝不由同一组常数的反射不变性删掉原rank。

全prefix常数需要原整个closed DFS完成，全部prefixterminal正域已付，无原error/stop/close错误。这是本诊断能否给全前缀结论的范围说明，**不是BVP、原metric或精化继续的前门**。若不满足，observed_paid_leaf_extrema只称已付叶极值；不能当作未访问区域的界。

## 8. 全域 metric、材料与帽的未变责任

原相对算子范数、正定域、lower/upper、parent fallback、closed root plan、原DFSsplit、same-C live refinement、actualphasequeries、caps targetidentity都在本次完整diff外。

新helper只处理prefix的$3M+2$有限参考。tail/native、cut patch、collar、caps仍原准确表达和全域metric；本次不把它们虚拟成同一有限Fourier状态。

all_time_transfer仍来自原完整共同材料角同余、全角圈覆盖和固定帽；不是新的tube常数或$t$端点。第一材料/同C/g/十词/构造的绑定仍按R504，不简化为parameter相等。compare要求同一新source/schema的实际measure结果，保原固定targetsignature和上下界比较；没有新增“常数必须下降”或“先证明tube才继续精化”的门。

## 9. 原钟、部分结果与必要读回

本层不启动子进程或ownedlauncher，也不重置原clock。原deadline仍必须与本job第一材料、实际R489重算相同；接受的三旧schema是：

- request193-owned-job-science-deadline-v1；
- request203-owned-job-science-deadline-v1；
- request205-owned-job-science-deadline-v1。

原namespace science18900、readback2700与measurement本地allowance的实际裁剪逻辑保持。本observer新增工作用该剩余预算；不承诺原预算仍足以完成同数量的cell。未来外层ownedcaller仍负责终止、reap与quiet；本次没有伪造新的quietmarker或cleanup授权。

必要正文新增 actual_prefix_joint_tube_constants，含实际binding、真实M/N、访问/退休/未付计数、条件全prefix常数或仅observed局部极值、首末未付和完整原ledger身份。原coverage对象仍包含完整当前frontier和所有未访问root suffix。所有退休行的输入/错误/地址在完整临时ledger；只返回其身份时明确不声称全文已回传。

原error、resource_stop、close_errors、原native/FD/final记录、same_semantic_tail_queries必要范围全部保持。summary/readback/compare各原单90000B，实际超限返回70并保全raw。没有拆分raw、通用编码、升限或凭child成功标签宣称全scope已返。

## 10. 已付量与继续使用条件

得到实际paidleaf时，可以消费：

- 当前准确quintic的完整独立系数盒；
- 同次准确A/nu/mu的真实外包；
- 本闭角cell上整个jointbox的严格P下界；
- 原R521的四块Lipschitz与state二阶majorant；
- 当前准确quintic的Qprime/Qsecond界。

若要把它们用于原R514/R521残差传递，还需真实原cubic系数/样点、FFT/RHS/norm形成误差、nominal→准确scalar差、原sigma/root和比较路径落盒。没有这些输入不能调用原literal-cubic接口冒完成，也不能把RMS=1e-6等参数当全域metricfloor。

本次任何actual-prefix完工都不等于native tail/帽/全closedBVP精确解，不证明精化数列收敛、全t嵌入、reach或deltaE。原全课题目标继续由真实同g精化与完整消费者支付。

## 11. 交付与实际执行边界

完整source-plan包含每条before/after/count和最终68077B身份；新schema/frame及两个helper真实来源都显式记录。源码/计划/本文和证明没有本地import、AST、compile、fixture或科学计算。也没有把独立复核设置为发布或后续求解前门。

这是一条已完成的实际source接线：已有supported真实父时，新evidence的每个原prefixcell会真实调用helper与R521，不需要caller另写数值循环。当前没有新的accepted父、输入recipe、workflow/run或实际常数，故不预填任何完成标志或性能收益。
