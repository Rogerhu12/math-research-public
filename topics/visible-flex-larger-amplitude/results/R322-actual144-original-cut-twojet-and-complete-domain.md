# R322 实际144：原 binary cut 的完整连续 C 两 jet 与全自然域包围

**作者：AI（ChatGPT，geometry）。日期：2026-11-15。分类：真实公开 Actions 读回。**

实际 request144 已完成原 160 胞、1440 段、全部六 primitive，以及原 binary cut 点和完整自然径向域的两个闭查询。**cut 点的完整两 jet 已由全部原叶包围并实际读出；cut 的原 E 值宽度工作目标也完成。** 整个自然域仍有 2891 个有效粗叶的工作精度未付，并在后续 inverse-query 积分中真实触发一次时间预算停止；没有丢弃整个径向域，没有缺失原 source/query 后缀。

这份结果属于已明示的连续约定 C 根族。它没有执行旧 finite48 selector、没有替旧有限输出证明连续误差，没有形成有限头 DN/J、非零尾或被接受的闭场，也没有支付同场相对 metric 阈值。

## 322.1 真实执行与本次读取范围

- 公开运行：[run 43715729122](https://github.com/Rogerhu12/math-research-public/actions/runs/43715729122)。
- dispatch source：ad4a4345dbdaf477b84fe5c6158d308af2dadb27。
- compute job：132816731637；report job：132824742430；官方元数据均为 completed/success。
- 原 workflow：[visible-larger-public-stored-continuous-E.yml](../../../.github/workflows/visible-larger-public-stored-continuous-E.yml)。
- 原请求：[public-original-stored-continuous-E-request.json](../computations/public-original-stored-continuous-E-request.json)，该 dispatch 原 SHA256 为 dcd4a892c8b38bf5f3f1923ea530a58095e76fd52ccdfeed4962370f5ff21e1f。
- 两 jet reader：[geometry_20261115_stored_C_v3_cut_twojet_readout.py](../computations/geometry_20261115_stored_C_v3_cut_twojet_readout.py)，19023 B，SHA256 1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed。
- 几何生产器仍为 [geometry_20261115_stored_continuous_E_cover_v3.py](../computations/geometry_20261115_stored_continuous_E_cover_v3.py)，89307 B，SHA256 f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df。

本次从官方 job-log 工具完整读取 compute/report 两份解码日志，提取原标记之间的完整 JSON 文本，并分别逐字比较两 job 的 scalar 与 cut 两 jet 块。两对原文本均相同。未重新运行积分、根、ODE、Jacobian 或任何科学包；也未把原 dyadic 端点在本地换算成新的十进制科学读数。

本次取得的是日志中保存的完整实际摘要和原身份。大型六 primitive/source/query ledger 只在原 Actions job 中存在；不能把读到其完整哈希等同本地重新审核其每个数值。reader 在 Actions 内确实读取完整原 query leaf stream 并核字节、行数、SHA，再取出全部 cut 叶；这项实际执行与本地日志读回分开记录。

工具返回的 UTF8 解码日志身份为：

| 对象 | bytes | SHA256 |
|---|---:|---|
| compute 工具返回完整文本 | 151916 | 180663a37601a96d6d596417d9efd0c28e917d7b1e5fdc38d119c98df0270626 |
| report 工具返回完整文本 | 111572 | f69850a6e750ffa4695ee2a665f8a4ba490aec565fa601e93914fd26181b49c8 |

这些是工具解码文本的身份，不是 GitHub 日志 ZIP 的身份；没有下载原大型科学包。

## 322.2 原对象、源码和实际输入没有变更

运行沿 [R286](R286-original-stored-continuous-integral-and-metric-bridge.md) 的约定 C、[R297](R297-continuous-E-unit-panel-and-piecewise-enclosure.md) 的归一化积分包含及 [R306](R306-complete-cap-endpoint-primitives-and-budget-preserving-integration.md) 的完整 $w$ 端点 primitive。三份原证明和全部 11 个运行 source pins 均在 Actions 的预检中实际核对；本次没有引入另一个 $g$，也没有把 $R_{\rm out}$ 强制重归一到名义 cut。

原三输入从历史 commit 8bd267107cc8710d371f3b62c02986655ac965b0 按实际原 blob 恢复到该 job 自有目录：

| 原输入 | bytes | SHA256 |
|---|---:|---|
| 原完整 T112 config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| 原 calibration ledger-ready | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| 原 stored-reference-ready | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |

对应 Git blob 分别为 543d8364593985305438dda6a0c89b4b1a9c7ec5、4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3 和 b6c44fe237750f13c8b10366f15525b481a74e09。没有重序列化这些原输入，没有消费一个被冒称接受的 field/tail。

查询参数文件 original-stored-continuous-E144-queries.json 为 1303 B，SHA256 4e59c69fae54045e100180e2d7576b848423a503394ff0b4dd87f6e219b7fd59。其顺序真实为：

1. original-binary-config-cut-point，原 config.rCut 的闭点查询；
2. whole-original-source-natural-continuous-domain，从原 cuff 到真实自然 $R_{\rm out}$ 的完整闭查询。

第一项不是准确分数 $3/10$ 的另一个 cut。实际 binary64 原词为 333333333333d33f，对应原报告准确有理数

$$
r_{\rm cut}=\frac{5404319552844595}{18014398509481984}.
$$

Actions 在恢复原 config 后实际比较了该原词与 query 的两个端点。原末端、warp 与 query 均未因此改写。

运行环境为 Python 3.12.14、python-flint 0.9.0、256-bit Arb。原工作参数完整保留：absolute bits 96、relative bits 80、analytic guard bits 8、单 integral evaluation limit 100000、E value-width bits 24、max depth 48、query depth 12、max panels 200000、max query nodes 200000、总内部预算 1800 s。guard bits 本身没有被当作误差证书。

## 322.3 原 source、六 primitive 和自然外端已完成

实际原报告给出：

| 字段 | 原值 |
|---|---|
| full_finite_head_complete | true |
| complete_original_pieces / original_piece_count | 1440 / 1440 |
| declared_continuous_model_family_conditions_proved | true |
| protected_join.proved | true |
| finite_joins.proved | true |
| original_exact_deep_root_existence_proved | true |
| all_admissible_original_root_choices_uniformly_enclosed | true |
| original_exact_deep_root_choice_resolved | false |
| deep_root_values_computed | 0 |
| finite_root_table_recalibrated | false |
| partial_finite_head_prefix | null |
| unvisited_source_piece_suffix | null |
| error | null |

原胞完成事件最后为 original_cell=0、completed_pieces=1440、elapsed_seconds=1524.62497088。这里是完整有限头的实际完成时点。最终生产器总 elapsed_seconds 为 1800.9322301759998；后面的工作用于 query/inverse-cover，不能用末次 query 停止的位置否认先前已完成的 1440 段。

原六 primitive 的显示值如下，逐字取自实际报告；完整 dyadic 端点在原 scalar 摘要中：

| 分量 | 原显示值 |
|---|---|
| A | [0.153108624575236913660813795 +/- 6.04e-28] |
| B | [0.0006007753386900131932393033 +/- 6.76e-29] |
| sqrtE_A | [0.155428043739402048155120789 +/- 5.82e-28] |
| sqrtE_B | [0.0006038258763311991045034738 +/- 8.20e-29] |
| w_A | [0.0193506687326223318482260558 +/- 2.49e-29] |
| w_B | [2.06702624761192542912554e-5 +/- 7.14e-29] |

“完整”指这些实积分获得有效包围，不等于每一个被保留的粗 integral panel 都达到了原工作宽度。诊断中仍有 coarse_valid_panels_at_maximum_depth=3；本文不把它们抹掉。

自然外端及其相对原 binary cut 的差，实际报告显示为

$$
R_{\rm out}\in
[0.30000000000000715908123386\ \mathord{+/-}\ 6.75\cdot10^{-27}],
$$

$$
R_{\rm out}-r_{\rm cut}\in
[7.1701834641\cdot10^{-15}\ \mathord{+/-}\ 1.01\cdot10^{-26}].
$$

原 reader 进一步用准确 dyadic 下端点完成 cut 域包含比较，original_point_domain_certificate_exact_bounds_cross_checked=true。该结论不将 cut 与自然外端声明为同一点。

无限深尾仍是对所有允许原准确根的统一包围；原显示包括 $E_r$ 的 [+/- 3.22e-84] 和 $E_{rr}$ 的 [+/- 0.0446]。它没有因此选择一条唯一根序列，也没有用某个粗深盒声称可任意精化的唯一实数名称已经生成。

## 322.4 原 binary cut 的完整两 jet：全部原 dyadic 词

点查询实际结果：

- complete_closed_domain_bound=true；
- domain_containment_proved=true；
- continuous_model_family_conditions_proved=true；
- work_resolution_complete=true；
- refined_nodes=5；
- unresolved_resolution_fragments=0；
- budget_or_refinement_stop=null；
- leaf_ledger_rows 为 [0,1)，只有一个完整 head 叶。

新 reader 将实际全部叶纳入同一点的 $E,E_r,E_{rr}$ 包围。selected_leaf_kind_counts={"head":1}、selected_original_leaf_count=1、selected_original_work_resolution_unmet_count=0、all_point_leaf_rows_retained_in_hull=true、point_twojet_enclosure_complete=true、unpaid_reason=null。

以下是原输出的完整 dyadic 端点与实际 Actions 已算出的全宽；没有本地转换或重新作差：

| 分量 | lower | upper | exact_full_width |
|---|---|---|---|
| E | 297036851754023534385 × 2^-68 | 297036860731551973169 × 2^-68 | 8977528438784 × 2^-68 |
| E_r | -1377364570695686333 × 2^-62 | -1377334639942752445 × 2^-62 | 29930752933888 × 2^-62 |
| E_rr | -18506607869532518095 × 2^-57 | 3541147354781501745 × 2^-57 | 22047755224314019840 × 2^-57 |

原 point E 显示为 [1.0064000 +/- 3.04e-8]。$E_r$ 的整个报告盒严格为负；$E_{rr}$ 的报告盒跨零。后者是同一准确导数的有效包围，不能拿中点作其准确值，也不能从跨零推导真实二阶导数为零或非零。

原 v3 的 point work_resolution 只检查 E 的值宽度。它**没有**请求或通过一个 $E_r/E_{rr}$ 宽度门；新 reader 保留 no_derivative_tolerance_gate_added=true 和 derivative_work_resolution_requested_by_original_v3=false。因此点工作目标 true 与二阶盒仍较宽完全相容。

reader 所执行的新算术仅是实际原端点比较、原域下界比较、全部点叶的 hull、准确全宽。new_integrals_or_ODEs_or_J_or_nonlinear_solves=0。不能因这份读回而把一次新的精确整数比较冒作原生产器早已输出的显示，也不能因没有新积分就称全部读回仅为字符串复制。

$E,E_r,E_{rr}$ 属于同一真实点、同一来源对象的包含；三盒的笛卡尔积仍可能大于真实相关集合。后继准确工厂可以把它们作为共同有来源的语义参数包围，不能假设任取三个 midpoint 就构成该 C 的已认证准确 jet。

## 322.5 完整自然域也有界；工作精度及真实停止位置未付

第二查询仍保完整从原 cuff 到自然 $R_{\rm out}$ 的闭域，其实际原字段为：

| 字段 | 原值 |
|---|---|
| complete_closed_domain_bound | true |
| domain_containment_proved | true |
| continuous_model_family_conditions_proved | true |
| work_resolution_complete | false |
| refined_nodes | 57032 |
| leaf_ledger_rows | [1,71678) |
| unresolved_resolution_fragments | 2891 |
| 原 E 显示 | [1e+0 +/- 0.161] |
| unvisited_query_suffix | null |

原 budget_or_refinement_stop 是：

> Partial inverse-cover primitive: Declared wall-clock resource budget reached

这里没有遗漏全域范围。原已有粗片完整保留，所有 query leaves 仍包住整闭域；未完成的是原工作细化，而不是域不存在、整个 query 失败或原 C 已被改动。总 numerical_work_resolution_complete=false 应按这个范围保留。

未付 ledger 共有 2892 行，实际逐类计数是 integral-panel 1 行、query-resolution 2891 行。没有 source suffix，也没有 query suffix。

唯一原 integral-panel 记录：

- source_piece=1398；
- original_cell=4、original_segment=3；
- purpose=inverse-query:whole-original-source-natural-continuous-domain；
- depth=0；
- closed_parameter_interval=[30523/131072,61047/262144]；
- included_in_complete_primitive=false；
- reason=Declared wall-clock resource budget reached。

它是全域查询细化时的新子积分，不是原有限头首次构建的一段缺口，也不是已完成 cut 点的失败。原 partial_finite_head_prefix 仍为 null、完整1440标志仍为 true。

实际 callback 发生于 sqrtE_B，analytic requested=true、type=ResourceStop、transport_exception_type=ValueError；inferred_from_elapsed_or_SystemError=false。源按 R306 保存真实异常后恢复预算语义，未把任意 SystemError 猜成预算。最终 error=null。

这个末片的原 cap 分支为 transition-low，闭片 $w_x$ 原显示为 [-0.0647 +/- 7.02e-5]，proved_sign=-1，原 $\chi$ 恒1。完整 $w$ 端点规则实际给 A、sqrtE_A、w_A 包围；这三个分量均已有完整工作目标而没有调用 Acb。B 随后实际获得有限包围，sqrtE_B 的 callback 到达时间预算。不能从这个最后现场反推唯一性能根因，也不能把末片在 transition-low 误写成“端点公式要求 raw 分支”。

## 322.6 原诊断计数的确切范围

以下只复制原生产器统计，不重新运行或根据时间猜测：

| 原计数 | 值 |
|---|---:|
| integral_panels | 84886 |
| inverse_cover_nodes | 125825 |
| rigorous_analytic_component_integrals | 196261 |
| analytic_components_attempted | 196262 |
| analytic_components_finite | 196261 |
| analytic_components_skipped_by_existing_complete_goal | 197696 |
| analytic_panels_attempted | 65660 |
| endpoint_panels_considered | 69919 |
| endpoint_panels_proved | 69008 |
| endpoint_panels_cross_possible_cap_branches | 306 |
| endpoint_components_enclosed | 207024 |
| endpoint_components_work_goal_met | 207024 |
| endpoint_whole_derivative_sign_unresolved | 894 |
| endpoint_chi_transition_panels_kept | 17 |
| endpoint_zero_derivative_panels | 31 |
| complete_accepted_panels | 71681 |
| coarse_valid_panels_at_maximum_depth | 3 |
| real_range_failures | 12988 |
| callback_resource_stops_captured / restored | 1 / 1 |

原 failed_component_full_width_goals 按 A、B、sqrtE_A、sqrtE_B、w_A、w_B 顺序为 [96,99,96,102,77,126]。这些是原内部尝试计数，不能简单相加当成最终未付片数，也不能据此把某个分量删去。

analytic_cap_nonholomorphic_callbacks=1542770、analytic_absolute_value_nonholomorphic_callbacks=643742。它们反映回调实际按非解析分支合同工作，不是接受点失败数；没有据此取消原 cap/cusp 或将全部回调硬称解析。

## 322.7 完整原件和读回身份

| 对象 | bytes / rows | SHA256 |
|---|---|---|
| actual result.json | 24892 B | d851976101cf315c8c8f6f550b649659825ca1431b1219b5eaba4223c4e9cf46 |
| input-binding.json | 25648 B | 6d0f956c4c2642608323da8497605f8b9abd03396104c56d6970b41707d7b5e4 |
| query-plan.json | 599 B | f67422c56bd98ebff12fadf844d69adcd230ec393cdb6d574c6fdd141fe05052 |
| query-results.json | 1922 B | bf8f7dff25116e1571bacafaa6b670dba6a476a7c3825ea643221a206c994eab |
| cut-twojet-readout.json | 5684 B | 8d7f730cb33aedc3424db5e46a14e3c988568a9e6c6233db7e34afad0be5a708 |
| source-piece-index.json | 899790 B | f3df610600d867671224281d475d021206036ac788a4ac2350888de249dab5db |
| complete-source-radial-panels.jsonl | 25513827 B / 14644 rows | da2ba4cb44ad3276b147cff40fe978de9a40966780586a7efb62fc986d853a59 |
| six-primitive-panels.jsonl | 1356067275 B / 71681 rows | 0e3246aa1950b6a6c8df81f05c1579ff1038a65296ba61d8da8122a77318b681 |
| query-closed-inverse-cover.jsonl | 130679735 B / 71678 rows | f85767980b80e6908a1b42677e09a1ff1014d7111837782b5442541bbe5d1e7b |
| unpaid-complete-scope.jsonl | 5845076 B / 2892 rows | 437d4918d496a16eea0abfa6d0315996e89e3f22084bb68b17bca64eab216c93 |

实际输出还有三个不同用途的 compact 块，不能混用其 SHA：

| 输出块 | bytes | SHA256 / 换行范围 |
|---|---:|---|
| 原 v3 scientific summary | 25026 | dcb37eec29cedc4a42835289ea4bc9a620b277afa5255e2d2a16d1e1c6930809；原生产器报告口径 |
| workflow actual scalar | 28670 | 6327f0e2b329e380e356375303fff70518ff3e4b562afcb5e6867906e78fb55e；compact UTF8 JSON，不含分隔 LF |
| 原 cut twojet summary | 5830 | fee0436dbfc881041d6a552990c376aca835109c035af23543b15d1e1f19a007；canonical UTF8 JSON，含最终 LF |

compute/report 的后两块逐字相同；不存在 report 重新计算科学值或把 failed flag 改为 success 的环节。前述 5684 B 的原 readout 文件与 5830 B 的 summary 不是同一个文件，summary 另含实际文件 receipt。

原自有 raw 和恢复输入已在两次读回后清理，日志实际给出 request144_owned_temporary_payload_removed，raw_outputs_or_recovered_inputs_not_uploaded=true。没有 artifact、Release 或 raw Git 上传。依据根 Rule15，后继必须在自有 job 中重新生成并即时消费必要原件，不能把这里的 compact 摘要拼成伪造原完整 ledger/input-binding。

## 322.8 规则同步与进程结束

原 rules runner 在 2026-11-15 12:49:09 UTC 实际完成 round0 同步：

- origin_main_read：ad4a4345dbdaf477b84fe5c6158d308af2dadb27；
- published_commit：dae5ab2fe2b30bf6bc48e96b6257b88a5807c6f4。

这是真实 runner 的同步记录，不是本地 API 查询被改称 git pull。

runner-result.json 为 480 B，SHA256 524c25303e18f601ff2c29a45224a6d7646d392a57c3f8268d9f98ed4912d880；started_utc=2026-11-15 12:49:09 UTC，finished_utc=2026-11-15 13:19:11 UTC。science_returncode=0、wrapper_returncode=0、periodic_sync_failures=[]、README_change=null、science_terminated_for_actual_rule_change=false、scientific_checkout_modified=false、original_scientific_argv_and_budget_preserved=true。

本次看到的成功属于源执行、完整闭域包含和实际点两 jet 的范围；它没有取消上文明确的 coarse work 精度责任。

## 322.9 已付的后继接口与仍未付的科学目标

本次新增的实际成果是：**原 binary cut 在连续 C 自然域中的包含、全部原点叶的真实 $E,E_r,E_{rr}$ 包围，以及它们的原来源和完整叶 stream 身份。**

因此：

- R300/R323 的连续九标量工厂可以在同 job 的真实完整输入上使用这类 cut 盒，执行其真实结构条件与显式短窗选择；本次没有执行该工厂，也没有预付其参数域或数值 profile。
- R312/R324 的新 C 有限头推进可以在同 job 重新获得原 source/point 叶后形成新的全112物理列；本次没有做该传播、没有证明任何 cut 高度分母非零、没有输出 cut DN。
- a601 或其九450适配仍需真实同场表达、完整原目标 atlas/所有闭 cell/帽和原相对 metric 条件。本次只有连续目标点 jet 与全域粗包围，actual_accepted_field_or_same_field_metric_threshold_paid 仍为 false。
- 原 finite 数值目标与约定 C 的对象差异继续保留；actual_finite_selector_or_old_point_derivatives_certified=false。
- 未进行非零 tail/native、全前缀 fullDN、BC/RMS/最终 audit、完整闭场 C²/embedding/reach 验收。

这份结果实际支付了前述点输入缺口；剩余责任以原对象和实际范围继续推进，不增一项额外人工或 fixture 门。
