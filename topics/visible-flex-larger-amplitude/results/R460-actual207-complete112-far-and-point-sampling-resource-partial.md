# R460：actual207 完成112远端族与联合数值行，物理点采样额度停止，后续联合精化未起

作者：ChatGPT / exact_refinement（AI 辅助研究）  
日期：2026-11-16

**可信度：数值证据及原执行记录。本结论依据唯一取得的实际207两份官方job日志、其中完整必要摘要和实际控制流；没有重算C、ODE、native、FD、域包围或几何。原必要读回成功不等于native、闭面或精化目标完成。**

## 1. 实际结论和来源

[实际run43801267782](https://github.com/Rogerhu12/math-research-public/actions/runs/43801267782) 在新source `1e05442404d3867fc09589a523e594202efde7c0` 执行了冻结205子合同，然后调用207新增精化编排。它不是旧205运行的恢复，也没有复用旧205数值结果。实际两个job为：

| job | ID | 官方终态 |
|---|---:|---|
| Original205 complete science then accepted mesh M128 and fixed-target evidence | 133081849462 | completed / failure |
| Repeat exact bounded primary scopes without a scientific calculation | 133153849841 | completed / failure |

本次实际完成了原C完整1440片有限头、全部六primitive与完整深族绑定；两个原查询均取得完整闭域粗包围，whole-domain查询的工作精度仍未完成。cut完整two-jet读取和全部112深远端行完成。在物理far传播阶段，所有 $m=2,4,\ldots,224$ 的完整不确定行族、单位取向行以及联合参数名义数值行全部返回。随后物理点采样以原工作数上限停止：完成3个unique point，尚有0个完整native field occurrence，未形成可供native启动的完整几何。

原错误为：

`WorkStop: declared-phase-work-unit-limit-reached`

这个错误来自physical-point sampling，不能回填为112 far传播失败、联合数值行双零、真实pole、共振或非线性求解拒绝。实际 `native_geometry_ready=false`；完整453、450、原FD/final native均未启动。207新增的R456 mesh、M128、三级metric/time-grid evidence及compare也全部未启动。报告job返回2，是如实保留compute失败；没有必要运输溢出。

## 2. 本次真正执行的合同

外层request为 `public-actual202-joint-refinement-and-fixed-target-evidence-request-v1`，request_number207，21956B / `c798f376a63d552c12ff56b51fba8f11ed46bba4d858ec95df2838cfe3575015`。工作流为 [.github/workflows/visible-current-C-actual202-joint-refinement207.yml](../../../.github/workflows/visible-current-C-actual202-joint-refinement207.yml)。

原205子合同在本次run真实执行，其原字节为97406B / `06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4`；154个旧source与75个新增source的229项来源合同保持。原job360min、namespace science18900s、readback reserve2700s没有因各phase或新role重新启动。新增两级计划是R456五factor均2，然后M=128并保真实新父的角/step/material/physical计数；max_nodes2400是容量，末900s留measurement/关闭。它们本次没有产生数值结果。

三个207实际源为：

| 作用 | 字节 | SHA-256 |
|---|---:|---|
| geometry_20261116_request207_owned_roles.py | 17026 | 304eaa41b3b9c0e1eab4e71678720f336cbd1a5e7f47ceb9ef1b6e8d2b0ddc5f |
| geometry_20261116_request207_joint_refinement.py | 44927 | 76881ec3ad75c7d33ef2ea70cafbf12cf73dcb9273f137187f73a975368f4ea8 |
| root_20261116_request207_refinement_necessary.py | 33942 | 7902848f2aac3abb880ae604aa81f7f87bdd68b7b25f6a39dd0ffa92152dde24 |

本条参数是R449从实际202末十词的明确binary64投影得到的准确有理点。其新accurate-ten model recipe为3211B / `b02790e6c81082e6c548d9a990a26fd9e88f2ce6d2f18d14e31f4c9251c922a2`；actual202 finite-Gauss接受和原180域证明都未迁移为这个新准确模型的接受。实际构造也明确 `actual_native_calls=0`、`actual_shooting_J_calls=0`、`actual_nonlinear_trials=0`。

## 3. C、cut与完整深族的实际范围

### 3.1 原C完整头与两查询

实际f12f原source未改；结果24867B / `c96c3f340fd7d77d1e3146342f5e8289dab540624a0c01c41516fe2a2c03ff4f`。记录为：

- complete_original_pieces=1440，full_finite_head_complete=true；
- 原全部六primitive及deep+head总量均返回；
- all_admissible_original_root_choices_uniformly_enclosed=true；
- 两个requested query全部returned，两个complete_closed_domain_bound均true；
- source/query未访后缀均null，error=null；
- elapsed_seconds=3600.3882934969997；
- numerical_work_resolution_complete=false。

点查询是原binary64 cut的准确有理值 $5404319552844595/18014398509481984$，没有重标为十进制0.3。该点query refined_nodes=5，leaf范围[0,1)，unresolved_resolution_fragments=0，work_resolution_complete=true。

whole-natural-domain query保持从准确rCuff到自然积分外半径的完整闭域。它的refined_nodes=60684，leaf范围[1,75330)，unresolved_resolution_fragments=2887，work_resolution_complete=false。原原因是 `Partial inverse-cover primitive: Declared wall-clock resource budget reached`。这并未取消已保留的完整闭域粗包围。

原unpaid ledger有2888行，其中1行integral-panel和2887行query-resolution。首个原未付积分地址为source_piece1398、original_cell4、original_segment3、depth0，闭参数区间[15885/65536,31771/131072]，purpose为whole-domain inverse-query。完整ledger 5836993B / `68a1d6830b481745de55a5297fe2bbb437b80eb823456414b596f67137d68547`；本次必要摘要保首地址、全kind计数和真实原件身份，未把全部2888行正文搬回或宣称逐值审完。

### 3.2 cut two-jet

原1c39读取器从同C完整query leaf流保全该点唯一head leaf，actual readout5684B / `289e59d5ee23b9578c0f4eb5e2b588c0c151e9bf2a4d183ecbc29a0b898d90e1`。point_twojet_enclosure_complete=true，unpaid_reason=null。该查询只对E值施加原工作宽度，未把Er/Err宽度另设接受门；原全域work未完仍明确保留。

这不是cut DN、finite-head ODE或非零尾解；original_exact_deep_root_choice_resolved=false。完整query原流137309009B / `e5353ebb89c003fc084bc48fbb78aab8902d93696fc8bafee959366fe370a489`、75330行仅有原身份与既定读取范围，未下载到会话重新求值。

### 3.3 深远端112

原fe667 producer complete112=true，全部偶频率2至224返回，unpaid_mode_suffix为空，error=null，elapsed_seconds=0.021532639000724885。完整112原行494612B / `d68c5547b0323dd2a2bff3fa4087ed5aad831646cabff7c7804519025aa528b9`。

该producer仍保far_port159、physical_node160、source cells160至无穷的原全根族范围。它自身不支付有限头传播、不证明全部cut高度分母非零，也不支付非零native。后续实际sampler所付的有限头责任在下一节分别记载，不能把两个producer的scope混为一个。

## 4. 新accurate-ten域：基底完成，实际参数域仍未决

实际72c factory返回精确表达式定义379213B / `64b7f8a5636e35c7dc165da0e197834f897fcbb64b98bab5ed58c934fc60cd17`。construction_conditions.all_strict_conditions_proved=true，nonempty_family_conditions_paid=true，exact_model_definition_created=true；没有用cut盒中点冒准确模型系数，也没有执行原finite root选择器。

两次原domain pass必须分开：

| 范围 | processed_nodes | passed_leaves | unresolved_terminal_leaves | unvisited_stack_entries | complete |
|---|---:|---:|---:|---:|---|
| base_domain | 485 | 452 | 0 | 0 | true |
| requested_parameter_domain | 20413 | 1810 | 8598 | 16 | false |

base用时0.2666790060002313s；requested用时301.72603643999946s，原每pass300s合同下返回partial。full_current_ten_domain_certificate_complete=false，error=null。requested ledger289672352B / `a7d731f1f25f816c09f09d13ba255ad33240dd36c147ec628df9000db52b6b26`。

这批8598终叶和16stack是原包围程序未付范围，不构成真实域失败或全搜索无解。必要报告并未返回每个域叶全部bounds/地址；本文不由总count定位唯一瓶颈，也不把R481/R483后续方法当作本次已经执行。原factory partial没有被加成sampler的新拒绝门；本次far确实继续进行了完整计算。

## 5. 全112 physical-far与联合名义行实际完成

sampler实际source为 `32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4`，schema `current-C-pruefer-joint-nominal-row-physical-radial-samples-and-general-far-v1`。其实际result44662B / `89f61bd898374e3b0652704a8c3d278725ee2324ddeae43879a979fbacf344db`，没有重用原187失败行或中点。

实际far词为f0e68a5235e3a93f，数值0.05056158669090205；实际mu词705c211ef215743c，数值1.7421589928370103e−17。far选择仍是完整原node8半径上端点之外的下一个binary64，不声称等于不确定原节点。全部实际圆周方向行采用同far/mu坐标。

必要表完整包含112个mode row及112个numeric selection row，频率顺序均为2,4,…,224。逐项原flags：

- complete、complete_required_far_propagation、unit_family_complete全部true；
- 每模式完整candidate/inverse leaf数量均为1，完整unit row数量均为1；
- all required/completed leaves对应完成，没有not_started_far_modes；
- numeric_row_status_counts中actual-finite-joint-nominal-row-formed为112；
- actual_numeric_row_failures为空，numeric_row_modes_not_started为空；
- complete_general_row_count为112，全部实际选中字词与原selection records一致；
- 没有通过高度分量除法制造单位行。

本次linear phase actual_work_units=2044754，actual_checks=4053992，actual_elapsed_seconds=7628.961588603999，phase_finished=true，stop=null。其工作上限25000000、实际秒上限10038.05418311225都没有触发。原必要mode表中零height分母不能由完整unit row推断为不可能；本文没有宣称全部cut DN图完成。

联合名义行提供的是实际数值坐标及到完整原行族的误差包络，`exact_global_C_realization_of_numeric_representatives_certified=false`、`nominal_parameter_point_is_not_selected_exact_global_C=true`仍保留。全部112名义行正常形成不等于已选定一个真实全局C根序列，亦不等于非线性DN存在。

必要读回在Actions内完整解析了far-all-mode-rows、far-complete-tubes、far-inverse-leaf-coverage、numeric-far-row-selection及general-row原件。本会话没有重新读取或计算它们的全部区间见证。far accepted-panels原流95028240860B、1604049行，以及panel-commits 798985781B、1604049行仅按原协议保全字节身份/行数，没有被新审计重算，也没有上传或分包给会话。其大小是原临时资源记录，不是新的计算门。

## 6. 真正停止：物理点逆像采样工作数

完成全far以后，physical-point sampling记录如下：

| 原字段 | 实际值 |
|---|---:|
| sampling_phase_attempts / actual_inverse_range_count | 1000000 |
| actual_point_count | 3 |
| actual_coarse_valid_point_leaves | 499929 |
| complete_native_field_occurrences_done | 0 |
| sampling phase actual_checks | 2000234 |
| sampling phase actual_elapsed_seconds | 486.5222847770001 |
| sampler elapsed_seconds | 8119.073682390999 |

原stop字段为kind `declared-phase-work-unit-limit-reached`，phase `C physical-point sampling`，actual_work_units=declared_work_units=1000000，stop时elapsed485.414287308s。实际phase秒上限1254.7567728890313尚未耗尽；最后存储观察free11824427008B大于原2147483648B reserve。不能把这次停止解释成wall、disk、README变化或far传播停止。

sampler保持completed=false、native_geometry_ready=false、nonlinear_solve_or_DN_computed=false。numeric-point-values-and-errors流为0B/0行。sample-inverse-leaves原流有499931行/900696737B，其中原coarse计数与总行数各按原字段保留；本文不把3 unique point误称为3个完整native field query，更不补全577节点/全RK与audit计划。

完整unpaid流实际2740B / `5d92947277b33117db4c61c573493b30cf2ae9c5867669f336a2b67f32cbff68`，2行。必要selector保留：

1. 原row0：kind `actual-current-C-physical-point-inverse`，原行SHA `c681eb14d82b6a457ceee7c364dddd6dd790a41e79751a3518524d7327d2c358`；
2. 原row1：kind `current-C-native-sampling-unfinished`，原WorkStop、全部completed_far_modes、unstarted_far_modes=[]、complete_native_field_occurrences_done=0、all_remaining_field_plan_preserved=true；原行SHA `190db318e8f5738109937410a0547d71bcd865f490ec02dbf5dbf27c637233ee`。

**读回边界：** frozen207沿原1987/80c2必要selector，第一行的point_index、radius_word、role、all_pending_closed_fragments、retained_original_leaf_rows没有被选择返回。必要摘要中的current_state/last_unaccepted为null不能替代这些字段，更不能证明没有pending fragment。本文明确缺失这些具体定位，不猜第几个半径/何种query，也不从原行SHA恢复已删除正文。后来独立sampling-scope reader修订不回填本次记录。

## 7. 原求解及新增12角色均未起

原candidate binding过程return2，direct_BVP_input_created=false；必要构造报告缺少：

- actual202-ten-BVP-input/adapter-result.json；
- actual202-ten-BVP-input/result.json；
- current-BVP-deadline.json。

原BVP必要报告 actual_candidate_binding_missing=true、actual_BVP_process_not_started=true、original_launch_identity=null、actual_live_client_directory_exists=false。design453与frozen450都明确exists=false/not_started_not_success=true。没有任何本次native call、当前J、FD、完整末场或已接受checkpoint可供后继使用。

R452闭面编排本身正常return3，elapsed0.008842209999784245s，upstream_stop=`actual-BVP-launch-result-absent`，unstarted_outer_roles=[postsolve,held]。它没有用模板冒actual deadline，没有产生first assembly/B/material成功，也未将缺少B另设成求解拒绝门。

207新增runner也正常return3，error=null、external_interruption=null，elapsed0.10999765400083561s，upstream_stop=`genuine-original205-contract-BVP-launch-not-returned`。全部实际未起角色为：

| 层 | 未起角色 |
|---|---|
| 原场测量 | level0_measure |
| R456新mesh层 | level1_solve、level1_geometry、level1_witness、level1_held、level1_measure |
| M128层 | level2_solve、level2_geometry、level2_witness、level2_held、level2_measure |
| 三层比较 | compare |

所以原t细分4/8/16没有执行；没有任何R459完整上包围、真实sup下降、上界改善或机器/solver metric floor结论。原R456/R457的条件实现和R458证明仍是已发表方法来源，本次未产生它们的数值后继。

## 8. 必要运输、规则与实际清理

本会话只对终态两job各取一次官方GitHub connector日志。身份口径是**connector解码文本再按UTF-8编码**，不是声称取得HTTP原字节：

| 日志 | 字节 | SHA-256 |
|---|---:|---|
| compute133081849462 | 642079 | 52d99dbb566005d07ec78b05a22b06f81e9a9d418195b3f6a1b4aad230b2ba02 |
| report133153849841 | 471692 | 540550ca17653fcf880141e546b2cd0caa418ce688b989439ea59f2630bb65f5 |

只在解析视图逐物理行去掉可证明的单行首BOM/timestamp前缀；原日志文本身份不变。下面五原primary及新增207必要body在compute/report逐字相等。各原文件含LF口径由原identity事件和body+LF核回；scalar原primary本身不含该LF。

| 必要scope | 原字节 | 原SHA-256 |
|---|---:|---|
| C scalar | 28644 | c424695e1a0bb891975bcbba59574a05f2bffa1678a81c5c0572e7ee3a37889c |
| cut two-jet | 5830 | 98a498c9b8ffc01455c5c3762de0dbcb1af34faddc68c4be0d4ac08cb56037d0 |
| deep far | 7327 | d6213ced2a07026ed24135923b3f1c3dfa569ae8d533964eb9a9788775b2176d |
| construction | 40768 | 7c5988ffbc250cb289da7e1d7ab49ddfdde8f206570965da4859b817f1a1a21e |
| original BVP | 54440 | 7b82f7893b655344a73871bbc0f9529bea4999b2300a14d46ea4b40b92377bc6 |

closed-postsolve原必要文件17593B / `2948f7d96eab18e37f20a54c10bf2f080c0f2e36fa3c17181d98ca8611799dca`；compute中的规则必要body85409B / `58ab2ae0d077f457233dc793c93fb98cc639f33661dc06e6d42a0668fed7cfc1`；207新增必要帧body15228B / `1e96c2f6e745d6db2e524cf844d4f7e0b964b92b8ae74849e16a2c8ee2df5239`。后两身份明确是帧body，不冒未验证的本地文件字节。

新增necessary.complete_necessary_readback=true、transport_complete=true，read_errors/required_error_text_unreturned均空。两份报告保留原大科学账的身份，不以“necessary complete”声称完整所有raw字段已回传。report失败也不是运输丢失：其原transport_scope.errors=[]、compute_result=failure、BVP_outcome=failure，随后真实exit2。

原sampling规则runner started05:05:28、finished07:20:47，science/wrapper return2，README_change=null、science_terminated_for_actual_rule_change=false、periodic_sync_failures=[]。新refinement规则runner真实07:28:43 pull/rebase后核根README21bd547f56590b7f2dd279d0297efb289a9b2783及课题READMEbff8aea253a9e6a7a4fac28d810ac454c5499fec；07:28:45以科学return3正常结束，不是规则kill。

在必要readback时cleanup_performed=false仅表示当时还未删除。随后compute **07:28:46.8446582Z** 出现原事件：

`request207_original205_and_refinement_raw_removed`

该事件明确八个C/cut/construction/far/BVP/rules/closed/refinement读回outcome全success、actual_quiescence_rechecked=true、source_inputs_and_large_raw_not_uploaded=true。原205 owner观察无live/unknown组，207自己的两次前读回和三次final quiet观察亦无live/unknown/错误，原rule parent已return3。故本次确实在必要读取和静止复核后删了namespace。不能把仍在GitHub日志中的原SHA当成可恢复的末场或未付逆像账；也没有可继续warm的accepted450/M128对象。

## 9. 结果对后继的实际意义

本次新的数值事实是：在本次真实C和实际202投影十词来源下，完整112 physical-far行族与R419联合名义数值行已经一起执行完成。实际阻点随后移到physical-point inverse的原工作计数。它没有为原requested-ten全域8598未决叶补证，也没有验证一个非零native响应。

后续可以依据这个具体停止位置选择已独立登记的采样策略或实现，并必须重新实际支付所需状态/几何与原门。本条没有派发新job、改变1M额度、把旧hash恢复为数组，或把没有发生的R456/M128/t测量记为科学进展。原README§5的完整同g误差精化、机器/solver误差传递、全部t闭面、reach/held等责任仍未付。

### 主要来源

- [R458：同job联合精化与固定目标证据条件组合](R458-same-job-joint-refinement-and-fixed-target-evidence.md)。
- [原207 owner](../computations/geometry_20261116_request207_owned_roles.py)、[runner](../computations/geometry_20261116_request207_joint_refinement.py)、[necessary reader](../computations/root_20261116_request207_refinement_necessary.py)，具体SHA见第2节。
- [实际compute](https://github.com/Rogerhu12/math-research-public/actions/runs/43801267782/job/133081849462)、[实际report](https://github.com/Rogerhu12/math-research-public/actions/runs/43801267782/job/133153849841)，必要body、原错误、未起角色与清理结局见第8节。
