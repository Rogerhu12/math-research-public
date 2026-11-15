# R385：实际181完整C和深尾112行已返回，Prüfer换帧正范数包围未付

作者：ChatGPT /root/exact_refinement  
日期：2026-11-15  
状态：实际公开Actions终态结论。本文只读原JSON、日志、字面字段和字节身份，没有本地积分、ODE、区间运算或矩阵重算。

## 385.1 主要结论

实际request181的原C生产器完成全部1440源片和两个请求的完整闭域包围，切点二阶jet返回，原R312深尾全部112个偶频模式也完整返回。随后R380 Prüfer头部传播只启动频率2：52个闭面板被接受，119次面板尝试后，在原source row18、piece4、深度32的首个子片报出正二幂换帧范数包围未隔正。线性阶段实际约0.519秒，资源停止字段为null；这次传播没有取得任何切点候选、单位物理Robin行或切点DN。

失败是这次区间表示和传播实现留下的未付责任。它不证明真实解向量为零、不证明共振或无解，也不把C的工作精度未全达标改写成完整域包围失败。报告作业成功只说明原必要结果已读回。

原程序已经使用同角恒等式和正二幂范数下界；问题不是源码遗漏了该恒等式。最终错误发生在严格正端点约束重新装成Arb球之后的正性检查。原日志没有导出这一失败候选的全部内部数值，不能据此补写具体比例、端点损失或唯一浮点原因。

## 385.2 实际来源和完整必要读回

唯一实际运行：

- run：43751399744；原触发source：9236fcf0a21746eef528754d567c2992ea3a12c9。
- [公开运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43751399744)。
- compute job：132925930260，终态failure；原step13完整112 Prüfer比较与全部cut候选传播失败。
- report job：132943822062，终态success。
- 没有重新派发、替换源或复用别的运行输出。

两份完整原日志各取一次。仅在解析视图按每个物理行去一个行首BOM，再去锚定的原时间戳；原字符串字节身份保持：

| 原日志 | 字节 | SHA-256 |
|---|---:|---|
| compute132925930260 | 314645 | 7d6953cfd33c59bf41d212e86dede40ee3bdec1ea909ae16bcc098a688ea166d |
| report132943822062 | 349492 | 2c7b7933ed7e00f33379b79cfe3628f7aaef03c10195c5da98c89c5e1060635e |

各原日志有一个行首BOM；compute1639个物理行、report165个。目标帧无未闭合或JSON解析错误。四个必要对象在两job中逐字相同，下表字节和SHA均不含运输分隔LF：

| 必要原对象 | 字节 | SHA-256 |
|---|---:|---|
| 原C完整标量摘要 | 27362 | 45a9e44495e4532bfb7ca730327fb884d1cff6ee5ed2005b84266b1eadb6f3f5 |
| 原cut two-jet摘要 | 5829 | 5f34dff5810157b43884c849d10affde199005ae8b46d0659bb711d95c476b46 |
| 原deep112摘要 | 10166 | d677f37bac944b7e536b515ae6ece39d75259f0c5ae6d4594341119701a6bf37 |
| 全112模式及未付范围必要读回 | 40616 | 41fe5c023a686b4847df4c60e0415bace8415e6c3f46d6419b832640edc4b55d |

另读到compute的原科学摘要15129字节、SHA f969e39b757e70770eb2ac5f7502f7d3b02670ad898c5d6fc2253faf92a48c51。它是包含实际result receipt的原摘要，不是与result.json字节相同的对象。真实result.json为14996字节、SHA d24efcd8c40c08fcc63d962323da8ff3a14980971cbd5ccb8326da9aa2421b33。

实际input-binding.json为32454字节、SHA e0a47a762aca98c0bfa3d3fdabf0d967ffcb31d25e9596588357ec5550118bb9；dispatch-request.json为28877字节、SHA dc8647bb25a7c12b6c70fa63a65b884044ffcc5dd960d9fdb0642b450555477e。必要reader源SHA为e020b7e98b190fd8fa62f0fe13dd14980117f8efe2fffbdf23d33bd479e9e257。

## 385.3 同一原C的前置责任实际付到哪里

原C使用[原v3生产器](../computations/geometry_20261115_stored_continuous_E_cover_v3.py)，SHA f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df。模型为R286-original-stored-continuous-model-convention-C-v1；全根族语义保留，没有选择深尾根中点，没有重校原根表，也没有改旧有限输出的标签。

| 原C字段 | 实际原值 |
|---|---|
| complete_original_pieces / original_piece_count | 1440 / 1440 |
| full_finite_head_complete | true |
| all_requested_closed_query_bounds_complete | true |
| all_admissible_original_root_choices_uniformly_enclosed | true |
| declared_continuous_model_family_conditions_proved | true |
| numerical_work_resolution_complete | false |
| error | null |
| elapsed_seconds | 3600.4072031130004 |
| integral_panels | 103219 |
| inverse_cover_nodes | 162523 |
| rigorous_analytic_component_integrals | 251259 |
| requested_query_count / returned_query_count | 2 / 2 |
| unvisited_source_piece_suffix / unvisited_query_suffix | null / null |

两个原查询须分别解释：

1. 实际binary cut点5404319552844595/18014398509481984：完整闭域包围true，工作宽目标true，5个refined nodes，1个原leaf，未决工作片0。
2. 整个原自然径向域：完整闭域包围true，但工作宽目标false；75365个refined nodes、90010个原leaves，2859个工作宽未决片。原停止文字为“Partial inverse-cover primitive: Declared wall-clock resource budget reached”。

全unpaid ledger有2860行：1个integral-panel记录与2859个query-resolution记录。第一个记录位于source piece1398、原cell4/segment3，闭参数片[5129/16384,41033/131072]，用途是整自然域的inverse query，原因是声明的墙钟预算到达。它们没有被当作缺失整域的后缀；原全闭域粗包围仍在。本文没有重算其宽度或单叶数值。

C原result为20746字节、SHA d09a91f06070f2bfa205c8be7e66b8f2cc1fdd3aed188e02827f4304eb307cfa；C input-binding为25648字节、SHA 695604c2034fc7374b2d9fd8481c98237893e0d2e335fc42712ea3510e5b58fd。

cut reader真实保留同一点的E、E_r、E_rr全leaf hull，point_twojet_enclosure_complete=true。它不把Er/Err的未另设宽度目标变成新的门，也不宣称原有限selector已获连续误差证书。

原R312深尾生产器为[完整深尾源](../computations/geometry_20261115_stored_continuous_C_far_graph.py)，SHA fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a。far_port159、physical_node160、频率2至224的全部112偶频模式返回，原根族全包含true；elapsed_seconds=0.021229108000170527，error=null，unpaid_mode_suffix=[]。该步骤没有做finite-head ODE，没有计算深根数值，也没有生成cut DN。

deep result为5857字节、SHA c492d218ebdf530678a904d1e959d78f76f23e4c9343c46ead881a58cf462bf4；完整112行原账494612字节、SHA d68c5547b0323dd2a2bff3fa4087ed5aad831646cabff7c7804519025aa528b9。原mode2深图为零的定理字段保持原义，不能由此推断其后finite head响应。

## 385.4 Prüfer传播的真实停止与完整后缀

实际[Prüfer科学源](../computations/geometry_20261115_stored_C_finite_head_pruefer.py)为93880字节、SHA 250474d748842d9b5423be2123460308ab16419d4b5dac1d8c9967fc208c0122；schema为R380-original-C-complete112-Pruefer-cut-family-enclosure-v1，依据已发[R380](R380-continuous-C-Pruefer-angle-lifts-and-oriented-Robin-enclosures.md)。

原参数为256bits、14400秒线性上限、25000000面板尝试、最大深度32、norm工作上限1/4、Taylor24、defect12、cache65536、临时盘保留2147483648字节。实际required source panels共14644；原完整source stream为25513827字节、SHA da2ba4cb44ad3276b147cff40fe978de9a40966780586a7efb62fc986d853a59。

实际只启动physical_frequency=2：

| 原字段 | 实际原值 |
|---|---|
| total_panel_attempts | 119 |
| accepted_closed_panels | 52 |
| coefficient_range_splits | 66 |
| coarse_valid_panels | 0 |
| uncertain_barrier_existence_splits / norm_work_splits / defect_work_splits | 0 / 0 / 0 |
| new_complete_expression_range_evaluations | 138 |
| coefficient_cache_hits | 0 |
| elapsed_seconds | 0.5186182789998384 |
| linear resource stop | null |
| last paid source coordinate | row17 / piece3 / parameter1 |
| next current source coordinate | row18 / piece4 |
| first unpaid closed subpanel | [0,1/4294967296] |
| subdivision_depth | 32 |
| cut_candidate_count / legal_cut_quotient_count | 0 / 0 |
| completed_original_cut_leaves | 0 |

原错误为：

> Complete coefficient/global-angle/small-lift enclosure unresolved: The whole positive frame norm was not isolated

类型PanelUnpaid；内部最后候选错误类型ArithmeticError，文字“The whole positive frame norm was not isolated”。最后完整候选只导出必要位置、错误、部分状态和canonical SHA，没有返回全部内在区间。该候选canonical SHA为2ec037ee63796e29fdabec5f844ce3cd88aeacb6b35968952e95fdc4c2ba9621，不能由SHA恢复未读数值。

实际资源记录有311次检查，最近原free bytes=109412319232，大于原保留值；线性elapsed_seconds=0.5186058959998263，resource stop=null。因此本次不是14400秒、25M面板或磁盘保留耗尽。

所有当前未付小片均被原程序列出：row18的33个闭区间，先为[0,2^-32]，随后按原端点依次为[2^-32,2^-31]到[1/2,1]；还有原required panel suffix [19,14644)。其余111个偶频模式4至224未启动。这里的区间连写只是对原端点列表的紧凑陈述，没有新划分或补算。

最后已接受状态的原显示为angle “[+/- 1.58]”、balance_power=-476、positive_amplitude_sign=1、log amplitude “[+/- 1.45e+2]”。这些是原display字符串，不被解释为新的准确端点或重新舍入值。全112 mode账已在Actions内逐记录解析，包含已启动模式的真实未付范围与111个未启动模式；reader首行original_started为null，是否启动依据原started_modes=[2]，不把null改成false。

## 385.5 源码定位：正下界已证明，重新成球后的正性仍未付

原reframe使用准确正二幂比例c，保持全实角lift：

$$
\|(\cos\phi,c\sin\phi)\|_2^2
=1+(c^2-1)\sin^2\phi,
\qquad
\min(1,c^2)\le\|\cdot\|_2^2\le\max(1,c^2).
$$

源中计算上述表达式后，已经调用known_range与准确上下界相交，再执行“if not norm2 > 0”。此次报错就是这一个检查，不是辅助小步small_lift中一般矩阵作用的范数，也不是物理DN除数。

原known_range经固定intersect_known实现，先选择两个包围共同的下、上端点，最后用a.union(b)重新形成一个Arb球。该球仍是合法外包，但外包表示可以比准确端点交集更宽。因而“准确交集具有已证严格正下界”与“重新形成的单球>0”不是相同命题。本文从固定源码定位了这个可能的表示损失通道；原未导出的候选端点不足以量化本次装球扩宽，不冒称已还原每次内部运算。

可直接实施的后继是保留准确正的端点约束，按log单调性分别包围两个端点的log，再形成log幅度包围；不必要求宽范数平方先重装成一个仍显正的球。角端点换帧中的正dot/atan比值也应保留同一准确正分母责任，不能用principal angle缩族。这需要独立新源和实际Actions，不修改已执行181或正在运行184的来源，也不能只增细分次数后宣布问题已解。

## 385.6 原账范围、误差读回与未完成责任

完整必要reader原字段all112_original_mode_records_complete=true、complete_scalar_readback_without_recorded_read_error=true、read_errors=[]；它没有导出大科学见证表。

| 原账 | 行数 | 字节 | SHA-256 |
|---|---:|---:|---|
| accepted-panel-tubes | 52 | 2254426 | e7ace7e5077cc390a333e25963c758709070e3ad8061653a04b35509f7905172 |
| closed-coefficient-boxes | 92 | 210434 | d68c54ae980e81f3468b1f0578516352e670aa7253206d2cea5a516efa20535e |
| complete112-mode-status-and-columns | 112 | 80930 | 3b87e133765733bb18ef3f2d480e6beebfa6f5e7bc03a311988fb63ed178baba |
| complete-unpaid-scope | 2 | 10422 | 71e0806ecea6d4c85e708a413ae4aab6817c283c88018801508286dd4e5348d8 |
| original-cut-leaf-coverage | 1 | 552 | 5e59edce489725dd94f47f128b3d2970caf298d085bb21366ed674e15fb7adf4 |
| actual-cut-tube-contributions | 0 | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| projective-panel-commits | 52 | 24056 | 2cfe3f4d71e412a84dc7305cbd1970b6ff1a35ec5f9cfcaa9d7ba9ecd48e3d68 |

mode、unpaid、cut-leaf及空candidate账在Actions内全部解析；accepted/coefficient/commit账只完成全字节SHA和行数核，没有逐科学数值复审。本文不把后一类说成完整矩阵或逐值证书验证。

原34件规则/owner receipt已读其身份与必要字段，reported errors为空；C和deep原owner均quiescent，原规则结果未记录变化错误。无需以额外取大账、重跑积分或完整数值复审作为发表本次真实失败的前门。

实际清理也已从同一原日志核到：request181_conditional_owned_cleanup中C/cut、deep、Prüfer及rules四项必要读回均success，477字节readback-complete.json的SHA为75a7c69ac5931b8f66306561cb9df2a65c97108d28ebf468c7ebeda03267b2fb，marker_matches_actual_run_and_source=true；原owner live列表与unknown scopes均空、quiescent=true，故cleanup_authorized_by_actual_readback_and_quiescence=true。紧接原事件request181_owned_raw_removed_after_complete_readback确认真正删除/home/runner/work/_temp/visible-stored-C-Pruefer181，raw_artifact_release_git_upload=false。这是已读后的实际删除，不是skip或仅声明将清理。

原最终科学字段仍为：

- all_complete112_factorized_cut_families_enclosed=false；
- all_complete112_oriented_unit_physical_Robin_families_enclosed=false；
- all_complete112_height_denominators_verified=false；
- all_complete112_cut_slope_enclosures_computed=false；
- complete112_cut_DN_diagonal=null；
- actual_nonlinear_solve=false；
- actual_nonlinear_tail_DN_existence_or_differentiability_proved=false；
- full_BVP_or_closed_surface_accepted=false。

181只承担物理(u,k)线性族，原native_Q_Pi_Robin_rows_not_claimed=true及未提供、未捏造mu的范围保持。没有完成338端点响应、原非线性native、fullDN/final audit、同场metric/reach/闭面全t责任。重现使用本run固定checkout的request181工作流和原请求参数；原大数据按本题临时数据规则处理，字节SHA不构成未来可续现场。
