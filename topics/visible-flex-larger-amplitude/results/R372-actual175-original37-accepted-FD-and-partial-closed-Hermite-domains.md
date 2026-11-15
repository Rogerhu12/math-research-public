# R372：实际175原37模型与新点FD通过，完整闭段Hermite诊断在5400秒预算后保留部分域结论

作者：ChatGPT /root/exact_refinement  
日期：2026-11-15  
状态：实际公开Actions终态读回；只读原JSON、日志、字面字段和字节身份，没有本地矩阵、区间、多项式或科学重算。

## 372.1 实际结果与原接受门

实际request175从真实actual98的原warm/status重新形成一次原37查询模型。原模型实际访问四档alpha，前三档因原域拒绝，第四档alpha=1/8被原条件接受；随后对这个新warm重新付原FD并通过。后置R354诊断保留完整453分量、29个真实端点variant、37查询及17个声明步长，已形成全部629个全453闭段Hermite gap包围；继续计算查询角域时用尽5400秒诊断预算，明确退出3。

因此compute作业的failure不能写成原模型或FD失败。原诊断没有改接受门，没有给出全37查询、全17闭段的完整域证书，也没有调用新的native/fullDN。它不是整条原IEEE执行误差证书。

主要原结果：

| 范围 | 实际原值 |
|---|---|
| 原模型 / 新warm FD退出码 | 0 / 0 |
| 原接受alpha | 0.125 |
| 固定权merit初值 | 43.363003729098274 |
| 原接受后merit | 43.33605694766103 |
| 原记录实际merit下降 | 0.02694678143724616 |
| 原记录预测下降 | 0.026877973010679432 |
| 原记录实际/预测比 | 1.0025600303467597 |
| 后置诊断elapsed_seconds | 5400.00465502 |
| 后置diagnostic退出码 | 3 |
| scientific_exception / pipeline.exception | null / null |
| resource_partial | true |
| 完整全453 uniform gap对数 | 629 / 629 |
| 完整全部闭段query域 | false |
| native/fullDN接受 | false |

## 372.2 真实运行、日志和必要摘要身份

[实际公开运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43747437442)：

- run43747437442，source81bf71ae214da94b01ebff4870fb4ee3ecd8782b。
- compute job132913733402终态failure；原step7一次原37/FD和独立闭段诊断的合并步骤退出3。
- 没有重新派发或下载其他运行输出；原日志只取一次。

原compute日志114898字节，SHA 9f70788962ed798e3f517229d8580c0c1a1d0159cda4d0c5dbdc68bda8f80189。解析视图仅去每物理行的单个行首BOM和锚定时间戳，原日志身份不改。共501物理行、一个行首BOM；必要摘要帧无未闭合或JSON错误。

BEGIN_REQUEST175_NECESSARY_SCALAR_SUMMARY原body为66886字节，SHA 1690de83c9b5d0abb5db16f6fe43c25e63675e8a32ac66c1e716aa3ce5e1379b，不含分隔LF；连同原分隔LF为66887字节，SHA b435ef73c226a320ccb17232c3be81f5176617a86ff054a252b1e2df8c49e265。原readback_complete、summary_complete、transport_complete均true。没有用大科学表拆包补齐摘要，也没有新科学计算。

关键临时原件的原记录身份：

| 原件 | 字节 | SHA-256 |
|---|---:|---|
| pipeline.json | 11587 | 6d3cc3b7aaa5072311064efcbaa5ee7a66a58ca721a8ec080bd01ff2ecdbfe76 |
| original-pair-summary.json | 442677 | e0753bcfccf6c112ff407fd53b7264b4ead195e8146e5d62065a34981ef2de52 |
| 诊断result.json | 6762200 | b6f69798999a054eeeaa00f50fddfa5bd92dc98918392262688c09d9600f7408 |
| 诊断summary.json | 2743 | 8a7eeae5aede5733e0aa20970dc4fa1ea1c149fd3450550066d393b1ab760507 |
| 诊断summary-complete.json | 2487 | e0e653006ba391c3c6f53929aea029a9ea1d9e022dc13c60cb03732f7ff622ae |
| capture.json | 767326 | 64ef1276c1be469c19988808c8cbdb8a574e5626ff1644b8876f6b94cd94c083 |

这些大原件只在Actions内读取并形成必要字段；本文没有将它们逐字传出、逐数值重新验证或由SHA制造未来续接现场。

## 372.3 原父、新warm、完整查询身份

输入仍是真实actual98原pair：

- warm-001.json.gz：4927052字节，SHA b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67。
- driver-status.json：3379453字节，SHA b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff。
- 原恢复字段JSON_reserialized=false；本job实际materialized=true。

新接受warm是4943009字节、SHA a979561852bc0d1fca788b77ac71e5f5fe341fc3e9826d3664347a71815500b2；新status3647546字节、SHA a488f097a5f1a085c96736ff94d50c9931b76a98dc1ae15a8e1de8e45cef86dc。它不是父件改名。原status保持：

- accepted_warm_steps=1，optimization_progress=true；
- phase=actual-full-angle-projection-merit-decreased-unaccepted-warm-saved；
- schema=exact-constraint-thirty-seven-query-condensed-complete-H-warm-v1；
- selected_angle_row_count=75776；
- success=false、new_coupled_finite_acceptance=false。

原模型model-000.json为814496字节、SHA ebec5600fa83b6ddc4d3264365e1d39a772ab3fb543d35a55a3b7f4a4a95d183；原QP摘要128733字节、SHA b2e753a74a486980c33f5ac5af041fe6bbcd3d00c0130b58eba3e857949e8f61。必要QP读回只保其原schema和另存大数组范围，本文不补写未展示的最优性指标或声称QP已获最优证明。

37个查询顺序完全保留：

- query0–20为LEFT-RMS，fraction=0.17267316464601146，对应interval 463,464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487。
- query21–36为collocation-midpoint，fraction=0.5，对应interval 471,472,473,475,477,479,480,481,482,483,484,485,486,487,489,490。
- 每查询2048个声明角；原全部节点、698中点及两组各698个RMS点的真实原门没有缩成这37个查询。

观察器返回185次实际angular returns、12次实际evaluate、1次domain和1个实际final direction；observation_complete=true，errors=[]，original_exception=null。29个端点节点为463至491，所有不同原chunk的词保其独立来源。完整scalar cache、b/C和调用表只在Actions内使用；没有从rounded scalar倒推b，没有把同站不同调用合并为一个假输入。

## 372.4 全部原四档试步及实际FD

原模型访问的trial index为0–3（含两端），未访问4–16。下面只抄原试探值；诊断随后处理17个声明alpha，不会把未访问档变成原nonlinear trial。

| 原trial | alpha | 接受 | 原中点域拒绝 | 原最小beta² |
|---|---:|---|---|---:|
| 0 | 1 | false | MID487 | -0.07787348001852168 |
| 1 | 0.5 | false | MID471 | -0.042792191869085006 |
| 2 | 0.25 | false | MID471 | -0.19167001275188889 |
| 3 | 0.125 | true | 无 | 不以单个最小值替全部原域检查 |

前三次都有原complete_trial_RHS_recomputed=true、节点失败0，原RMS阶段尚未进入。所有选中角的线性reserve slack均非负，不能据此把真实非线性域拒绝改写成通过。

最近拒绝trial2还有两条原selected失败：

| 查询 | 原位置 | 原beta²最小 | 负角数量 |
|---|---|---:|---:|
| query1 | LEFT464 | -0.2683086899521916 | 4 |
| query21 | MID471 | -0.19167001275188889 | 8 |

这两条都已在37集合内，不能称为遗漏query。原query1角index54、phi0.16566992509164924；query21角index44、phi0.1349903093339364。最近拒绝的原线性beta²最小值仍是0.0007427224110553854、negative_count=0，显示原线性候选与实际非线性试步必须分责。

接受trial3中原两组RMS各698点、invalid_count=0，节点/中点失败均0，37组selected_negative_angle_counts及nonfinite counts全0。原完整边界最大值6.857449986338445e-9，constant_collocation_max=0，physical_collocation_max=0.007107481419522546。物理最坏原行155819在interval461，原signed_value=-0.007107481419522546；其固定原权199.00690823502174来自原base weight，没有由trial RHS重算权。

该点的新FD真实执行，response-check.json为2839007字节，SHA 2b00e97490343f163b5c8862a32712752f1e1fee5b2e6e6d29abdbd02d6976db。原implementation_check_passed=true、complete_current_warm_boundary_FD_actually_recomputed=true；四阶最大相对误差8.81884772255149e-10，二阶最大相对误差0.00000988344249574147，原threshold0.00005。direct/separated二阶收缩true，left_right_jacobian_offblock_max=0。该FD没有付当前H的非线性native或完整BVP，相关原字段均false。

## 372.5 新准确有限参考已经形成的范围

后置源为[完整闭段consumer](../computations/exact_20261115_R354_thirty_seven_closed_query_domain.py)，SHA cf4fa7b33bfcc13cd68193c3abc9b2da8edae4b90e64c16bcfbcce863a095d89；capture源SHA 0a8f4920d5f4c080c64f5e9ea6aedd203c90a475d99c4e73d5ddce6e7a9d5a90；same-job pipeline源SHA 825caec6efc3fa7fca5daf9d70a9bed907bb0fe91b3fb39858b9d0da3a66d516。实际request SHA a6b9cf0aadb43d89ac072cb2c650a8b125005aabf99322434c108a6983b85419。

原正sin投影的准确端点基线SHA84af1e250b8a52d9b1691dd5dbeea4ff674ee79949fd72737e16c3f1b2fa018a保持；没有引用旧负sin审稿源。原FFT身份973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401，原augmented身份f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e。[R354](R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md)原证明SHA b6e293c20ffb6584f316b3e38877b7e3d4fb61cbad1f008718ab034f605cb183。

实际准确运算用384bit Arb三角函数与320bit向外整数网格。完整输入绑定gzip为194999字节、SHA8821193dd9ba5f5c92d630e70b8dea9c20f6a9b97f8e7a3456150caca02cf289；其原解压对象1311893字节、SHA d671a1e7d6688ac4bc9de84e68f81d09d8758fc840ffa6edb857cd4255eb9f6c。本文只读绑定receipt和必要字段，不重新解包原大件。

已付原字段：

- complete_actual_input_binding_paid=true；
- declared_actual_endpoint_variant_count=29；
- 全453=338物理+112core+3设计参数，115个常数RHS分量保留；
- 所有629个query/step的全453 uniform gap均available且completed；
- pending_endpoint_reference_rows=[]，pending_JP_variant_ranges=[]；
- pending_Hermite_formation_query_ranges=[]；
- 每个原pointwise transfer步的pending query ranges=[]；
- all_declared_accurate_Hermite_bounds_available=true；
- scalar cache binding complete，准确scalar是原A chunk的literal b+C乘完整参数；
- complete_P_coefficient_count=15，highest_P_degree=14；
- every_possible_endpoint_A_chunk_kept=true。

原点态alpha gap与175新闭段uniform gap同时保留，不能混称同一个范围。新的系数族包围每个真实路径点，但不把Hermite余项当成固定多项式系数，也不宣称真实路径是固定二次式。原准确DFT是准确有限参考，不是原FFT每步舍入顺序；整条IEEE执行误差仍未证。

## 372.6 全17步的实际已证、未决与未访查询

原诊断按query和angle事务推进，完整提交43910个query-angle记录，对应原报告746470个query-angle-step评价。其中strictly_proved=702379、unresolved=44091、rigorously_refuted=0。这是原计数字段，未在本地重算区间不等式。

原最后未提交事务为query21、angle902、next_trial_index6，whole_angle_record_committed=false。因此：

- query0–20的2048个角均完整提交17步；
- query21仅角[0,901]的902个完整记录提交；[902,2047]仍未完成提交，不能把当前angle已部分算过的前几步计入完整事务；
- query22–36的全部角未访；
- 所有37×17 gap本身已经形成；“gap available”不等于该query全部角域已证。

以下集合全为原query index，范围含两端；k表示诊断声明alpha=2^-k。每一行的未访query都是22–36，refuted集合均空：

| k | 全2048角域已证的query | 已访但尚未取得完整query证书 |
|---|---|---|
| 0–2 | 空 | 0–21 |
| 3 | 0,18,20 | 1–17,19,21 |
| 4 | 0–1,17–20 | 2–16,21 |
| 5 | 0–6,10–11,17–20 | 7–9,12–16,21 |
| 6 | 0–7,10–13,15,17–20 | 8–9,14,16,21 |
| 7–8 | 0–13,15,17–20 | 14,16,21 |
| 9–16 | 0–20 | 21 |

query21的“未获完整证书”从k4起仅就已提交902角而言全部已证，仍因剩余角未访不能晋级为完整query。k3时已提交902角中898已证、4未决；k0/1/2分别289/439/835已证，613/463/67未决。没有将宽区间未决称为严格反证。

原all_requested_scopes_explicitly_accounted_for=true，但all_requested_new_computations_visited=false；complete_accurate_query_domain_on_all_closed_steps=false，any_accurate_query_angle_rigorously_refuted=false。对原accepted alpha=1/8，也不能把三个已证LEFT查询推广成完整37查询或全角、全站域证书。

## 372.7 实际成本、临时账与后继边界

原模型child耗时732.9240634839999秒，新点FD child19.262818014000004秒，诊断child5400.282564667秒；pipeline elapsed6172.57280894秒。全局上限10800秒，cleanup/readback预留300秒。本次是诊断自身5400秒截止；外部deadline_triggered=false，没有signal或异常。原停止文字为“explicit post-model scientific wall budget exhausted”。原必要错误数组保唯一诊断log receipt，未记新增异常文字。

诊断临时账未压缩总7716913453字节，保原完整精确值及身份。必要概要包括：

| 原临时账 | 完整记录数 | 压缩字节 | 原SHA-256 |
|---|---:|---:|---|
| complete453-formation-and-JP-actions | 66 | 1277750 | dc0dde1e24f09541c5c4accd1e0b8ea8465020eb503654f628164f6e2b99cdcc |
| complete453-accurate-endpoint-vectors | 29 | 2637693 | cd184bdc8c851b8dbcfb78b2ed761d9a6bf165db234c670298cd6d804c09378b |
| all17-closed-endpoint-angle-bounds | 59392 | 126797685 | ef511eb009ecde96872b181029e51b931a03abc8bd4f3ed4572d80d243128da9 |
| all453-Hermite-reference-gap-and-pointwise-eta | 629 | 25166058 | 36e97e10452f6576d745633e82c40f5b7b42cf3ea54800c2b15c73a441a13374 |
| complete453-closed-query-families | 666 | 47869793 | 7f722a02b15ef085724d236553bb368c0d97fbf5f6a1da0783c6087238e6e9e8 |
| complete17-closed-query-domain-angles | 43910 | 1489379711 | 17f9f248b66dab69e5c2efee62d2ba26a836ecdaa49945e59ff3e22277a131cd |

另有29份endpoint angle-jet账，每份2048条，原各自size/SHA在必要摘要中。这里只声明实际完整范围与原记录身份，不把未返回的区间大表写成已逐值审计。

本轮原模型的最近失败已发生在选中LEFT464/MID471；加重同一线性reserve不自动排除这种非线性域拒绝。新诊断则已有所有闭段gap，但粗闭段Bernstein域包围仍在大量已访角上未决，且最后15个查询没有访问。这两项后继责任应分开：真实原模型继续按原门推进；诊断可以针对宽包围和后缀成本作独立改进，不能仅因剩余预算或未决计数宣称原域失败、同场无解或步长已得到全域保证。

原extra_original_RHS_J_QR_FD_or_trial_calls=0，original_model_FD_or_native_gate_changed=false；whole699_node698_midpoint_RMS_checks_paid=false指新严格闭段consumer未支付该全局证书，不抹去原accepted点真实两组RMS检查。complete_IEEE_query_execution_error_on_closed_steps_certified=false、continuous_angle_or_station_certificate=false、native_fullDN_final338_or_physical_audit_paid=false。实际原日志随后记录request175_owned_cleanup_begin、complete_readback_marker_present=true，再记录request175_owned_cleanup_complete，真正删除visible-R354-175；规则镜像亦有request175_rule_mirror_removed原事件。Git_raw_publication、Release_uploads及recomputable_raw_artifact_uploads均0。所有可重算raw仅本job临时存在；本结论不凭已删除文件的SHA伪造未来warm续接。
