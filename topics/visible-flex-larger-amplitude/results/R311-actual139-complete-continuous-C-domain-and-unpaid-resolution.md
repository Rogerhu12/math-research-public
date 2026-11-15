# R311：actual139完成原连续C的全部六primitive与自然闭域包围

- 作者：AI（geometry）。
- 日期：2026-11-15。
- 分类：公开Actions实际结果、来源和未付范围。
- 状态：本次实际有限头及全自然闭域包围完成；请求的数值细分分辨率未完成。未生成或接受非零场，未支付同场相对metric阈值。
- 科学源：geometry_20261115_stored_continuous_E_cover_v3.py，89,307 B/SHA256 f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df。
- 对象依据：[R286](R286-original-stored-continuous-integral-and-metric-bridge.md)；本次算法改进：[R306](R306-complete-cap-endpoint-primitives-and-budget-preserving-integration.md)。此前实际partial见[R304](R304-actual136-cap-callback-budget-and-unpaid-domain.md)。

## 311.1 实际结论及准确范围

actual139已完成原160胞元、每胞元9段的全部1440片。有限头的六个准确实积分包围齐全，原深尾准确根族的统一包围保留，有限片拼接和保护端结构条件均由实际输入通过。原唯一查询是从准确冻结rCuff到本次真实积分自然外端 $R_{\rm out}$ 的完整闭域。

实际原字段为：

| 字段 | 原值 |
|---|---|
| complete_original_pieces | 1440 |
| original_piece_count | 1440 |
| full_finite_head_complete | true |
| declared_continuous_model_family_conditions_proved | true |
| all_requested_closed_query_bounds_complete | true |
| continuous_convention_C_query_enclosures_complete | true |
| numerical_work_resolution_complete | false |
| unvisited_source_piece_suffix | null |
| unvisited_query_suffix | null |
| error | null |

这里两个完成结论不可混淆：**全部原源及整个闭查询已有合法区间包围**；**不是每个查询叶都达到了请求的窄度**。原程序在时间预算结束后保留了已有父片粗包围，完整覆盖剩余反像范围，未删除闭端点或未决分支。因此分辨率false不等于domain失败；反过来，domain完成也不等于 $10^{-6}$ 相对metric标准已通过。

本次仍未付的对象标志保持原样：

- original_exact_deep_root_choice_resolved=false，deep_root_values_computed=0；
- original_finite_output_certified_as_continuous_solution=false；
- original_continuous_g_model_choice_automatically_discharged=false；
- original_numeric_factory_or_48_selector_executed=false；
- nonlinear_tail_or_ODE_or_shooting_J_run=false；
- actual_accepted_field_created=false；
- a601_same_field_binding_or_relative_metric_threshold_paid=false；
- R26_numerical_certificate_or_rational_deep_target_used=false。

声明C仍是R286显式规定的连续模型族，不把旧有限Gauss/selector字节输出改称这个对象的已认证解。准确根族的存在和统一包围也不等于已经选定了唯一可计算深根序列。

## 311.2 真实运行、日志和摘要身份

| 项目 | 实际身份 |
|---|---|
| request | 139 |
| run | 43710988676 |
| dispatch source | 431ec67492ab99b63b42a9a1d962bea0a2cdaf0b |
| compute job | 132802263809 |
| report job | 132810057213 |
| compute全部steps | success |
| report全部steps | success |
| 原science_returncode / wrapper_returncode | 0 / 0 |
| 原entry elapsed_seconds | 1800.8219652040002 |

公开运行：[Actions run43710988676](https://github.com/Rogerhu12/math-research-public/actions/runs/43710988676)。

本次亲读两份完整官方job-log工具返回文本。按其返回字符串直接UTF8编码、保留BOM和原时间戳的身份为：

| 原decoded log | UTF8 bytes | SHA256 |
|---|---:|---|
| compute132802263809 | 132991 | 65adf3d0d44cd3c767beb850bd278699b777f8275b152e05f03886a3cbb1f10d |
| report132810057213 | 56628 | 96023447d90383e3455effd31dc6e6685ad5117acfb8e3da99aa4e6b943f07ef |

这是**工具实际返回的decoded日志文本**身份，不冒原GitHub ZIP或服务器字节流身份。

两份日志中BEGIN_REQUEST139_ACTUAL_CONTINUOUS_E_SCALAR_SUMMARY与END边界内的实际JSON逐字相同：26,052 B，SHA256 8ed43445ca84981899c68da46615e9a3781ce4b327e0116faab44dd6bedf7cb3。该SHA不含打印分隔LF，并与原实际scalar identity事件完全一致。

实际result文件的原receipt为：

- continuous-E/result.json：23,086 B，74ecaa93eed9f3ec0f78edb777f858e5b13fbdad916551ca116a976de5ad9c38；
- input-binding.json：25,646 B，9798f56441bdd9130b52ee39ee618f2f2e62c544119dc08f6041c79f10e03771；
- query-results.json：1,111 B，ec3f25037ccd490484732e99a69405de10f012a11eb607d44ad538184f682478。

本次不是只从job success推科学结局：上述完成/partial字段、原区间和最后预算现场均来自完整实际summary。没有本地导入科学源或重做任何积分。

## 311.3 同一来源、参数和原输入

科学源保留的先前来源为：

| 原来源 | bytes | SHA256 |
|---|---:|---|
| geometry_20261115_stored_continuous_E_cover.py | 66415 | 9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed |
| geometry_20261115_stored_continuous_E_cover_v2.py | 77697 | 004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea |

原request SHA为3c210929e574d912014ed47f5ca7b09e14139f920d3fe7f8e1747d5e8fde9257；原whole-domain查询recipe为782 B/4fa2baa15518ee5045d4a21305ff3f727ef594f966e8a95f9bc6f89eaac3b979。没有将全域查询偷换成只查已完成区间的局部请求。

三个实际输入从同一历史commit 8bd267107cc8710d371f3b62c02986655ac965b0恢复，日志完整记录原blob、大小和SHA：

| 原输入 | bytes | SHA256 |
|---|---:|---|
| 原T112 config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| 原calibration ledger ready | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| 原stored reference ready | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |

原blob依次为543d8364593985305438dda6a0c89b4b1a9c7ec5、4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3、b6c44fe237750f13c8b10366f15525b481a74e09。运行没有重写这些原输入，也没有读取实际已接受tail/field。

科学参数保持原预算：

| 参数 | 原值 |
|---|---:|
| precision_bits | 256 |
| integral_absolute_bits | 96 |
| integral_relative_bits | 80 |
| analytic_guard_bits | 8 |
| integral_evaluation_limit | 100000 |
| value_width_bits | 24 |
| max_depth | 48 |
| query_depth | 12 |
| max_panels | 200000 |
| max_query_nodes | 200000 |
| budget_seconds | 1800 |

runtime原记录是Python3.12.14、python-flint0.9.0。原global warp、rCut和连续模型未重归一，六primitive完整保留。guard bits仍只作工作余量，决定窄度的是恢复原单位后的完整全宽检查。

规则同步的原记录：

- started_utc：2026-11-15 11:52:39 UTC；
- finished_utc：2026-11-15 12:22:40 UTC；
- 实际initial rules sync读origin_main为431ec67492ab99b63b42a9a1d962bea0a2cdaf0b；
- 实际同步事件published_commit为dcd7350fa74a286b2bc95b9dce7cd30cdf58ee81；
- README_change=null，periodic_sync_failures=[]；
- science_terminated_for_actual_rule_change=false；
- 原同步周期2700s，sync_rounds_started=1；
- 原科学checkout未被改写、原argv和预算保留。

本次root README baseline确为21bd547f56590b7f2dd279d0297efb289a9b2783，topic为bff8aea253a9e6a7a4fac28d810ac454c5499fec。这里记录实际runner行为，不把主控断开终端期间的API阅读冒称为主控发生过git pull。

## 311.4 全部有限头、六primitive和真实自然外端

最后几个原cell-complete事件直接为：

| original_cell | completed_pieces | 原elapsed_seconds |
|---:|---:|---:|
| 4 | 1404 | 632.650424259 |
| 3 | 1413 | 702.348087773 |
| 2 | 1422 | 1144.057027115 |
| 1 | 1431 | 1236.88933447 |
| 0 | 1440 | 1552.8056291300002 |

这说明整有限头在原总预算内先完成，后续才在逆像查询细分中耗尽时间。最后预算现场不能被倒写成“source cell4以前没有完成”。

原有限头六primitive显示值如下，次序完全沿源SIX_NAMES。此处复制原Arb display用于读数；严格身份和界值是实际result内的dyadic lower/upper，不是重新解析显示十进制当准确常数。

| primitive | 原finite_head显示 |
|---|---|
| A | [0.153108624575236913660813795 +/- 6.04e-28] |
| B | [0.0006007753386900131932393033 +/- 6.76e-29] |
| sqrtE_A | [0.155428043739402048155120789 +/- 5.82e-28] |
| sqrtE_B | [0.0006038258763311991045034738 +/- 8.20e-29] |
| w_A | [0.0193506687326223318482260558 +/- 2.49e-29] |
| w_B | [2.06702624761192542912554e-5 +/- 7.14e-29] |

full_deep_plus_head_all_six_primitives也六项完整。其display与上表相同，但部分dyadic端点不同；不能因为显示位数相同就把deep contribution认作准确零或把两组原字节视为相同。

本次真实自然外端原显示为

$$
R_{\rm out}\in
[0.30000000000000715908123386\ \text{+/-}\ 6.75\cdot10^{-27}].
$$

它的原准确dyadic界为：

- lower：17368813385597843796022191517437274564535897052532984933024799223639370151891乘 $2^{-255}$；
- upper：17368813385597843796022192128669356061985455117119621161292984810204620175315乘 $2^{-255}$。

原结果另直接保存了与原名义binary cut的差：

$$
R_{\rm out}-r_{\rm cut,bin}
\in[7.1701834641\cdot10^{-15}\ \text{+/-}\ 1.01\cdot10^{-26}].
$$

这个差的lower与upper mantissa分别是415125261761469730198603330236289151941335987359135569534826451、415125261762080962280100779794353738577564255544722134784849875，指数均为−255。lower本身严格正，因此本次自然外端确在原名义cut之外。没有把两者强行设相等，没有改warp、旧参数或半径定义。

这项实际包含关系足以支持后续对原binary cut提出独立点查询；它本身还没有提供该点的 $E,E_r,E_{rr}$。

## 311.5 完整深尾、保护端和有限拼接

原deep_cover报告同时包含全部n≥160和准确cuff，all_original_root_choices=true。原显示为：

| 量 | 原display |
|---|---|
| deep E | [1.000000000000000000000000000000000000000000000000000000000000000000000000000 +/- 4.75e-77] |
| deep E_r | [+/- 3.22e-84] |
| deep E_rr | [+/- 0.0446] |
| deep radial_right | [0.04999999999999998889776975374843459576368331909179723053517628596091414439645 +/- 4.30e-78] |

这些是同一根族的统一包围；尤其不能把最后二阶宽界看成已经选择某个实际根或某一函数的点导数。准确cuff值来自R286的结构证明，而非把上述小区间舍入成0或1。

finite_joins.proved=true，原active_flat_transition_index_is_an_original_segment=true，flat_start_segment=2；原raw端口关系、quintic二阶端点和cap/weight端口条件保留，finite_source_schema_used_as_seam_proof=false。

protected_join.proved=true。其具体实际结构字段为cap_is_structurally_raw_at_protect_endpoint=true、full_flat_override_absent=true、chi_value_and_first_derivative_zero_by_original_quintic=true。原三项log-slope二jet差的display是[+/-3.39e-74]、[+/-1.39e-150]、0。这里的准确拼接依据是上述源表达式结构；不会从前两个小区间宽度本身推出准确相等。

这些条件支付的是本次声明C源自身的指定连接。它们不自动支付新九标量前缀、切口、活动片、collar、两帽的全部同场atlas或最终曲面C²责任；这些仍按R294和各实际field构造另行绑定。

## 311.6 全自然闭域查询及剩余精细分辨率

原唯一query：

- id：whole-original-source-natural-continuous-domain；
- kind：whole-natural-domain；
- 左端：original-exact-dyadic-rCuff，closed；
- 右端：natural-real-integral-R_out，closed；
- domain_containment_proved=true；
- complete_closed_domain_bound=true；
- continuous_model_family_conditions_proved=true。

全域E原display为[1e+0 +/- 0.161]。它的实际严格界是：

- lower：3618502403473478672065033740480078332807929321849378244760175859205827623587乘 $2^{-251}$；
- upper：4197463552000370261790993616342594657794432831767239702667552627595819776675乘 $2^{-251}$。

本文不把这个显示转换成某个未经原输出给定的新小数端点，也不把全域E的振幅当作有限场与g的相对metric误差。相对metric还需要同一真实有限场的Gram矩阵、材料坐标pullback与完整闭格责任。

查询保66162条叶账，leaf_ledger_rows=[0,66162)。refined_nodes=51517，unresolved_resolution_fragments=2900，work_resolution_complete=false。原budget_or_refinement_stop明确为：

~~~text
Partial inverse-cover primitive: Declared wall-clock resource budget reached
~~~

这时已有合法父片的完整区间被保留。unvisited_source_piece_suffix=null、unvisited_query_suffix=null，读回未发现任何被删除的源或query后缀。不能把它改写成仍有2900个“未覆盖域”：它们是**已有合法粗包围但未满足工作分辨率**的query片。

## 311.7 最后真实预算现场与R306效果范围

完整原unpaid账有2901行：

| 原kind | 行数 |
|---|---:|
| integral-panel | 1 |
| query-resolution | 2900 |

唯一integral-panel来自**反像查询细分**：

- source_piece=1398，original_cell=4，original_segment=3；
- purpose=inverse-query:whole-original-source-natural-continuous-domain；
- 闭参数区间[14571/65536,29143/131072]；
- depth=0；
- included_in_complete_primitive=false；
- reason=Declared wall-clock resource budget reached。

这里depth=0是该次对局部区间启动integrator的计数，不是整个源或query树只有零层。原head已完成；这个未完成的追加积分没有被塞入完整primitive之中，query保父包围继续覆盖。

实际预算异常发生在分量B，callback_analytic_requested=false。程序确实捕获了原ResourceStop，以ValueError传过C回调边界并还原原异常：captured=1，restored=1。记录明确inferred_from_elapsed_or_SystemError=false，没有从一个未识别SystemError猜预算原因。result.error=null与合法partial query语义一致。

该原panel的complete-w端点均在transition-low分支，原全panel的w导数范围display为[-0.059 +/-9.33e-5]、proved_sign=−1。R306端点规则已启用，A、sqrtE_A、w_A由完整cap后的w给定；A的原actual attempt显示原full-width目标已满足，Acb_callback_not_needed=true。最后B仍需原完整积分，不能由另三项已经精确积分而删除。

实际诊断计数直接为：

| 原计数 | 值 |
|---|---:|
| integral_panels | 79366 |
| inverse_cover_nodes | 114780 |
| rigorous_analytic_component_integrals | 179685 |
| endpoint_panels_considered | 64399 |
| endpoint_panels_proved | 63493 |
| endpoint_components_enclosed | 190479 |
| endpoint_components_work_goal_met | 190479 |
| endpoint_panels_cross_possible_cap_branches | 306 |
| endpoint_zero_derivative_panels | 31 |
| endpoint_whole_derivative_sign_unresolved | 894 |
| endpoint_chi_transition_panels_kept | 12 |
| endpoint_range_fallbacks | 0 |
| analytic_components_skipped_by_existing_complete_goal | 181150 |
| analytic_components_attempted / finite | 179686 / 179685 |
| analytic_components_fallback | 0 |
| analytic_cap_nonholomorphic_callbacks | 1542770 |
| analytic_absolute_value_nonholomorphic_callbacks | 643742 |
| real_range_failures | 12988 |
| real_range_goal_passes | 1979 |
| complete_accepted_panels | 66161 |
| coarse_valid_panels_at_maximum_depth | 3 |

原六分量failed_component_full_width_goals为[96,99,96,102,77,126]，顺序仍A、B、sqrtE_A、sqrtE_B、w_A、w_B。此计数包含工作中的尝试失败，不表示这些分量最终缺失；三个达到最大深度的panel仍保合法粗包围。

本次原件实证支持：R306端点恒等式实际大量使用，完整head首次在本次给定预算内完成，回调预算能够完整保存场景。但它不支持把先前132或136的所有成本唯一归因为cap，也不支持声称其余分量、反像细分或参数不确定性没有剩余成本。源码和原报告继续保actual132_unique_numerical_cause_not_claimed及actual136_unique_numerical_cause_not_claimed=true。

## 311.8 大账范围、临时清理和已读证据边界

原producer记录以下完整临时账身份：

| 账 | rows | bytes | SHA256 |
|---|---:|---:|---|
| six-primitive-panels.jsonl | 66161 | 1247798976 | 18a57c5b2992888cc74b507de9315f90b99dde829c23393036f7161a38fae0b9 |
| complete-source-radial-panels.jsonl | 14644 | 25513827 | da2ba4cb44ad3276b147cff40fe978de9a40966780586a7efb62fc986d853a59 |
| query-closed-inverse-cover.jsonl | 66162 | 120666610 | d60140b9f25c734c7e308ef6c4ffb38158c600f5d110fd490bf08e8513999f06 |
| unpaid-complete-scope.jsonl | 2901 | 5863254 | 814215533e8b9216cab653e64e091f10e1df26817864af43c55f2235b36e979b |

source-piece-index.json为899790 B/f3df610600d867671224281d475d021206036ac788a4ac2350888de249dab5db。query-plan.json为378 B/e749933cfaab55d23d2895fd70d1d404977e46d1af4f3bd986fc7c3137f406ff。

本地没有下载或独立解析上述大账。已亲读的是两份完整原job日志、原summary、source/request身份事件与实际收尾事件。Actions只读阶段完整核query-results及unpaid账的bytes/SHA，并逐行统计unpaid的2901行、首个原现场和全部suffix；其他大账SHA来自原producer写流记录。这个证据范围不能被扩写成“本地重审全部1.2GB账”或“重新积分通过”。

原job随后打印request139_owned_temporary_payload_removed，raw_outputs_or_recovered_inputs_not_uploaded=true。没有raw artifact、Release或Git数据归档。规则runner的partial_scientific_files_not_removed=true只描述runner自身不删science现场；其后独立always清理步骤确实删除了本请求owned临时根，两者并不矛盾。

按Rule15，后继若需要cut点的叶账或同C有限头传播，必须用冻结源/输入/参数重新实际生成所需输出，不能把已经清理的raw描述器冒作仍可读取的文件。

## 311.9 由本次原值直接决定的下一步

当前全自然域查询已完成的核心责任不需要再重复证明。实际缺口是原binary cut处的准确两jet包围，以及同一实际有限场的比较。

下一独立request144应保持同f12f7470源、同三原输入、同256bit/全六primitive/1800s等原预算，明确先查询原config字面rCut，再保whole-natural-domain。原cut必须作为原binary数的准确有理值解释；本次已实证自然Rout在其外侧，仍应在新运行中用实际积分域核包含。不能令名义cut等于Rout或重新选择warp。

点查询需要完整可能逆像叶上的 $E,E_r,E_{rr}$，并区分合法粗界与可收敛工作窗口。原v3查询result顶层只给E总包围，derivative在完整叶账中；下游必须读取并绑定真实叶账，不能把全域display或deep二阶宽界当cut两jet。

R300新九factory当前冻结入口只认004010b6/v2。因此若使用新的v3输出，必须有独立明确v3来源和schema接线；本实际结论不修改旧入口或重标已有数值。完整112新C尾图及有限头Robin责任则按R312独立推进，不从本次E成功推出已经得到cut DN，更不从linear far图推出非零BVP或闭场通过。

