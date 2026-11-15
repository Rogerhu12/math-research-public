# R346：actual158 的原37查询一步接受、fresh FD通过与R334后置绑定错误

维护：ChatGPT /root/exact_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-15。

实际158从固定actual98原父件重新运行了一次完整37查询模型，原非线性回溯在 α=1/8 接受，新warm的原边界FD也通过。随后独立R334诊断在输入绑定阶段报错，尚未完成任何一条75776行的精确多项式或点态Hermite诊断。作业因此为failure；不能把它写成原模型拒绝，也不能把原模型/FD通过写成R334完成或native/fullDN成功。

本结果只读官方终态、唯一原job日志及其完整语义/错误字节记录；没有本地科学运算、重新评价RHS/J/范数或从已清理raw的hash制造恢复。

## 346.1 真实运行、日志及退出范围

|项目|原身份/结果|
|---|---|
|Actions run|43731669039，attempt1|
|source commit|de638f2ab272db4dbe0a695394c126b72a56fa42|
|workflow|.github/workflows/visible-larger-public-thirty-seven-R334-diagnostic.yml|
|compute job|132865254053，original37-and-independent-R334|
|创建|2026-11-15T15:45:41Z|
|官方终态|failure|
|步骤1–6|全部success，包括94源码/3参数/规则身份及实际源码解析|
|步骤7|failure；原模型、FD、后置诊断依次执行|
|步骤8完整读回|success|
|步骤9受控清理|success|
|原完整compute log|1057172 B，SHA-256 90c5fa18f5fd9a82f9702ff8fd08e8f0763b7ead9d71922bc2366d90b4f436f7|

原runner记录：started_utc=2026-11-15 15:46:07 UTC，finished_utc=2026-11-15 15:59:12 UTC，science_returncode=2，wrapper_returncode=2。README_change=null，periodic_sync_failures为空，science_terminated_for_actual_rule_change=false，scientific_checkout_modified=false。本次不是规则变更中断，也不是全局预算截断。

三个原child记录分别为：

|child|原exit|原elapsed_seconds|原日志bytes/SHA|
|---|---:|---|---|
|original-model|0|745.1351251220001|149747 / 701aaafdf4d684efed8b2fbcada64b6e51e5943f2663615206c22e9a5c82f23c|
|original-boundary-FD|0|18.81951595999999|176 / f9d789a434e51bc08a46d2bb8412c8c2a4acba75be292ea4de931dd4cf920026|
|post-model-R334-exact-diagnostic|2|0.26472895300003074|1961 / c3bfa166c9d3da89f5bbd485c7d6388ba0b261d6b0502e1df1656802c5e66694|

每个child的external_resource_deadline_triggered=false、resource_partial=false、signals为空。pipeline.elapsed_seconds=784.7274939089999；pipeline.exception=null；global_science_seconds=6000、actual_diagnostic_seconds=1800、cleanup_readback_reserve_seconds=180。进程退出原因与数学接受分开记录。

## 346.2 来源与完整科学范围

本次实际父为actual98：

- run43677587785/source918fdb11dbb7a424b6149b405e2c7fab3cc0c737；
- artifact14147700690，visible-followup-condensedqp-43677587785-1；
- 完整ZIP809042943 B / SHA9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a；
- 原warm4927052 B / b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67；
- 原status3379453 B / b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff。

Actions原transport记录完整ZIP size/SHA相同，两个选定成员原CRC已核、原字节未重序列化；其他ZIP成员未解压，不冒全包数组独立审计。actual141/155的末warm没有被改标签作为本次输入。

四原数学输入SHA为 accepted b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff、prepared 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714、tail-anchor e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51、tail-config 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5；由明确历史commit918fdb11的原路径恢复。原78公开源码只恢复一次。

原37查询为21个LEFT和16个MID：

- LEFT：463,464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487；
- MID：471,472,473,475,477,479,480,481,482,483,484,485,486,487,489,490。

保原2048全角，共75776行；24个捕获区间、29个端点463…491，局部坐标9805，全坐标236036，699节点、338物理行、112模态、3标量、109自由core。原C及完整外部恢复范围未缩减。λ=270，LSMR200、projection200、working512、dual200、原17档回溯、原RMS/域/未加阻尼的真实merit门不变。

94份源码由原90来源、原batch worker1和本次3个新观察/诊断/编排源组成。关键身份为：

|作用|SHA-256|
|---|---|
|原37 domain|2e189fbf48ddeb5bb2ffba60047ee544bc39b22c6fe5073a91dad6bb2a1074e3|
|原37 warm|293045c6e52ef7760f3e3f275aa6d7ec63f9d38ef070178932dcb9022e717ef4|
|原37 FD|b87385e38108cbb405bcdec00fb1bc55fd241428f5ca42464679aef18f6210da|
|原37 observer|2f70133e81f235af4439a1d2b173be835532ae5e8521e3be5216ed2750bd8778|
|本次capture|01a2638409893b60711c3af0ab4d14c6f9bc4272058f2e7577dd41b2db33c59d|
|本次独立exact consumer|3ed6fbc5bed4023197afd8441287fe6ae5655c769e3cb8f2b417fbf1a02d8047|
|本次同job编排|92d1adb0e5a43f132356d0dba2310545bd01cd85235011a759f01362c7edf392|
|request|2d678acda0e17dcd716c5d42574496e586046a7add0802729aaf95ed4d677428|

源码、完整CLI与预算在公开request及 [158接口](../notes/2026-11-15-request158-thirty-seven-complete-R334-post-model-interface.md) 中。观察层只保存实际返回值，其额外时间计入原wall budget；未承诺与不带观察的155在有限时间内得到逐字相同轨迹。

## 346.3 原实际方向与完整四次回溯

原fixed_weight_merit_before=43.363003729098274。原选择为R270-condensed-complete-H；完整实际原方向的gdot=−0.21838603098375256，actual_damped_model_decrease=0.11526910538193712。

原37全行线性reserve可行：75776个finite、negative_count=0、zero_count=0，最小slack=1.609823385706477e-15。它没有保证相应有限非线性步仍在原域内；实际四档已直接区分：

|原trial|α|原结果|原主要域事实|
|---:|---:|---|---|
|0|1.0|拒绝|collocation MID487原RHS非有限；该点完整输入finite，beta²最小−0.07787348001852168；另有多项已选LEFT有限角失域|
|1|0.5|拒绝|MID471原RHS非有限，beta²最小−0.042792191869085006；已选LEFT464也出现负值|
|2|0.25|拒绝，最近拒绝|MID471原RHS非有限；已选LEFT464和MID471均负|
|3|0.125|接受|原node/midpoint/全部37选定query有限；两组698点RMS完整通过，真实未加阻尼merit下降|

最近拒绝trial2的两条原selected证据：

- query1，LEFT464，fraction=0.17267316464601146，station=1.1553475805065636；beta²最低−0.2683086899521916，angle_index54，phi=0.16566992509164924，negative_count4，nonfinite_count0；
- query21，MID471，fraction=0.5，station=1.1918702857402743；beta²最低−0.19167001275188889，angle_index44，phi=0.1349903093339364，negative_count8，nonfinite_count0。

这两query都已在37集合内，不能把它们说成本次漏建MID489/490或单纯未加入约束。也不能由全线性slack正就宣称完整非线性域必须通过；R334后置分析本来正要分解该缺口，本次尚未支付。

接受trial3原值：

- actual_fixed_weight_merit=43.33605694766103；
- actual_merit_reduction=0.02694678143724616；
- predicted_unregularized_merit_reduction=0.026877973010679432；
- actual_to_predicted_ratio=1.0025600303467597；
- selected_linear_beta_squared.minimum=0.0007957738826882832；
- all_selected_linear_reserve_slack.minimum=0.0003713612055276927；
- selected_negative_angle_counts和selected_nonfinite_angle_counts的37项全零；
- 原RMS fractions为0.17267316464601146和0.8273268353539885，各698点invalid_count0；
- complete_boundary_max=6.857449986338445e-09，constant_collocation_max=0.0。

原物理collocation最大值从0.00710763096028075到0.007107481419522546，均在interval461、原row155819，负号保留。原固定行权重199.00690823502174来自base_evaluate_call1/model_weight_call1，不是从新trial RHS反算。这里只抄原前后值，不把不同模型的merit混减。

原17档只访问索引0…3；索引4…16因原接受而未访问，不补造其结果。所有完整原trial JSON由语义流保留，最终记录accepted_warm_steps=1、optimization_progress=true，但status.success=false、new_coupled_finite_acceptance=false。

## 346.4 原QP精度和FD范围

完整实际original A/AT/B/BT读回报告为true，multipliers_nonnegative=true、all_original_rows_feasible=true；原有限预算后验值为：

- objective=43.24773462371635；
- R267_lower_bound_raw_float=43.247734587454204；
- actual_original_stationarity_L2=0.03241534176964486；
- actual_complementarity_sum=2.905532105982389e-08；
- final_cross_point_gap_raw_float=3.626213640472997e-08；
- final_cross_point_distance_bound_raw_float=9.97419666890178e-07。

原local_QP active_stop_reason=maximum-working-row-budget，maximum_working_rows512，最后保存stage511/dual200；full_QP_optimality_claimed=false。上述是ordinary-float原标量，不是向外证书。原完整因子在Actions实际使用；本次没有把RAM因子文件或未回传大数组冒成已经独立逐字核收。

新warm上的原FD实际完成：

- implementation_check_passed=true；
- maximum_fourth_order_relative_directional_error=8.81884772255149e-10；
- maximum_second_order_relative_directional_error=9.88344249574147e-06；
- second_order_truncation_contracts=true；
- left_right_jacobian_offblock_max=0.0；
- right_rows_depend_only_on_right_endpoint=true；
- 原verification_threshold=5e-05。

原actual_completed_nonlinear_J_reused=true是本次当前prefix模型J的原实现字段；它不表示当前H的非线性尾DN已经解出。原记录明确current_H_equals_affine_anchor=false、nonlinear_DN_evaluated=false、nonlinear_native_at_current_H_solved=false、full_BVP_solved=false、full_Cartesian_closed_surface=false。FD通过不能代替真正native/fullDN/final audit。

本次新原文件身份：

|文件|bytes|SHA-256|
|---|---:|---|
|model-000.json|814411|749bccf6692ecadf39959c049ca4bde8807cc726be51cc38a042fc2fc6777b2e|
|driver-status.json|3647462|b5f221471f0cdc384408d6e41a499c8d110055655544dcdf1190424c50e27314|
|warm-001.json.gz|4943008|316e51b2880647b6d6532652e92aa446dacdb8df9a3f0e2b10b15a32f24de344|
|condensed-QP-summary.json|128710|e4c0cc482c627356250077b0475fd8a6b04a44cb8a3f919d4aab13f8d6067cf5|
|response-check.json|2839006|bd719e129d29bfea4896027a03cb6eb7735b7113d72fd53bb2186ab3fd5f911c|

这些可重算原文件已经按规定清理。它们的SHA是来源记录，不是可继续读取的现场或未来warm锚。

## 346.5 后置诊断的实际失败与零已付范围

完整原错误为ValueError: All base37 returns。真实traceback指向exact consumer的bind()，在读取原数组packet之前要求：

    len(domain["queries"]) == 37
    and len(domain["controls"]) == 37
    and len(domain["angular_return_indices"]) == 37

该联合断言失败。原result记录：

- phase=binding；
- active_cursor的query_index、angle_index、trial_index均null；
- scientific_completed=false，resource_partial=false；
- stop_reason=input-or-post-model-scientific-program-error；
- affine_complete_rows=0；
- unvisited_affine_row_ranges=[[0,75775]]；
- actual_point_query_count=0，complete_Hermite_query_count=0；
- verified_original_packets为空；
- temporary_ledgers为空。

因此本次没有原17α的精确八次多项式/Bernstein新读数，也没有完整453分量的点态Hermite缺陷结论。不能把预设scope、零数量或被清理的capture SHA写成已付算术。

producer的实际小status报告actual_domain_count1、actual_final_direction_count1、actual_evaluations12、actual_angular_returns185、errors为空、observation_complete=true、original_model_returned=true。该producer布尔只表示其观察写出流程正常，不会覆盖consumer的实际绑定失败。完整capture manifest曾有522570 B/SHA2a62d37029f2f7fcd000c7625ac1f55d78e523bb1fca97081bc9ac1f59d0712b；其大正文未在最终小status导出，不能从hash反造其中每个调用计数。

### 已确认的源码合同缺陷与未观测计数

capture对profile.control_jets装返回观察器，把domain构造期间的每次实际返回都追加到controls。原angular_values本身调用flow.scalar_jets；原scalar_jets在单station缓存第一次填充时也调用profile.control_jets。随后原B构造又显式调用该函数取得scalar_control_jets。

因此“完整37个query”不等于“此层函数总共恰调用37次”。这是实际源中明确存在的两类调用路径；consumer把未区分的总调用数硬当成37，是接口错误。真实错误log只给联合断言，不给这次domain.controls的准确长度，故本结论不写“实际74次”，也不以缓存是否预热猜次数。

最小修复应保留所有原观察调用，另外按照每个原query的station字与原B构造已经记录的explicit scalar_control_jets身份准确配对。不同来源、不同chunk的端点词仍不能合并；数组必须来自本次真实返回，不能通过Bz反造。原query/角行数量与每个匹配数组的完整shape/dtype/SHA责任继续保留。

由于本次raw已按规则清理，修复后需要独立新请求从同一真实actual98来源重新产生一轮原model/FD及观察件。不能把本次未导出的控制数组想象为仍可读取，也不能改变已记录的原数学接受。

## 346.6 完整读回核收及保存范围

1057172 B原日志已唯一取得。按原JSON词法保留数值字面值，重建8个完整文档/语义流，逐成员核原canonical bytes/SHA；共138个成员事件全部相符。以下SHA均为原协议所声明的“排序ASCII紧凑JSON加一个LF”，没有与原大文件bytes混淆：

|完整读回|bytes|SHA-256|
|---|---:|---|
|original-pair-summary（两处原流一致）|442513|f5ac6366556833babee586138af39e28501bb55bd83efd5420f31e4091888034|
|pipeline（两处原流一致）|11009|b2fc361480c46af9520d3d9e02e721a7f6ee1789e90718fecd2f2d0005b8df5b|
|original-rule-monitor-result|431|ccd567f88b11c1d948342d95f2f6cdda611bc9c274e57deeed719838bda6b591|
|post-model-diagnostic/result.json|14677|4ed28bbdbbcc4521f16a2cd6b12d0881f4250c962578c3307d587a6b9cab4c4a|
|post-model-diagnostic/summary.json|1903|cc9eea2a87b83e3a9de8e12d19bb41ab953887950d2c91ae13920cbb2af98fc8|
|capture-status|8740|6fa9d1fb351e576fa274fb52ee6fdca41d15cb19276d35462ad53cd8429136fb|

原1961 B诊断error日志通过完整byte chunk还原，SHA为c3bfa166c9d3da89f5bbd485c7d6388ba0b261d6b0502e1df1656802c5e66694，无截尾。这里没有重新计算原科学数组；未返回NPZ/矩阵/逐角raw仍不冒完整payload审计。

清理前readback-complete.json为2522 B/SHAb78709820914dc095cf9b96e7a6937e9e6cfc8ab007b7aef74dc305227d31d13。原清理事件确认complete_readback_marker_present=true，之后删除本request临时树。Git_data_publication、Release_uploads、raw_artifact_uploads均为0。

公开保留脚本、参数、真实run/source/SHA及本紧凑结论；不保存可重算大原件。修复后的独立166只支付此前未完成的诊断接线，不撤销本次原α1/8接受与fresh FD事实，也不预付R334、native、完整非零112场或最终几何责任。
