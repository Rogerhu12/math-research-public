# R403：actual190 的持久128接受、阶段编译阻断与独立audit未完成范围

作者：ChatGPT（OpenAI，amplitude）；日期：2026-11-15。

## 1. 本次结论

实际 request190 完成了一次从新鲜原64完整状态、完整J和R273方向到持久 binary128 owner 的真实求解。owner 的第一次方向、第一档 α=1 被原严格缩放范数门接受；完整129248行的范数由原记录的 0.000122096054597410989492629881621789239 降为 9.68582474751023176056740816374984163e−11。随后独立进程重放全部576阶段、完整226输出和全残差，原文件词与owner完全相同。

本次没有完成新预装配阶段导数的科学执行。编译器在新header第353行报告 column_environment 重载歧义，阶段程序没有启动；112边界响应和338×112端点读回因其真实数学输入缺失而未启动。独立原物理程序audit仍实际执行，完成575/576阶段、7485/7488查询，在阶段575的query9物理读回完成后、其后一个原子primal advance尚未完成时以 explicit-experiment-time-budget 停止；查询区间[10,13)也尚未访问。因此全部stage maps、boundary、endpoint、完整audit、native及fullDN接受仍未付。两个Actions job的SUCCESS表示流程及必要读回完成，不能代替这些科学结论。

本结论依据两份完整官方job日志及同一份64,310字节必要摘要；没有在本地重新求根、积分、形成矩阵、执行编译或重新计算任何科学数值。原始大数组、成功列明细和完整audit角表没有经本次读回搬出Actions。本文仅保留必要研究结论、原值、实际退出和来源身份，不重新归档可重算原输出。

## 2. 真实运行与原件身份

|项目|实际身份|
|---|---|
|仓库|Rogerhu12/math-research-public|
|run|43762998688|
|source commit|ef56f16ff3ca573fec8982754fe9d5256748317e|
|compute job|132961756447，completed / success|
|report job|132990691994，completed / success|
|请求|public-native-preassembled-final128-request.json，48,335 B，SHA256 a7dfae0668d992f89131b993b1e40915fe977f38191acc26129b319ab18a96cf|
|compute返回文本UTF-8身份|191,413 B，SHA256 aceb3c2868ed64d95753c8b73819fade19997607265d7a3488b240f9bccff13c|
|report返回文本UTF-8身份|133,344 B，SHA256 8c93b58c7a59bd7e95820c2369a29fddd7a9b48332f6087ec86127596156d256|
|单份必要ASCII体|64,310 B，不含分隔LF；SHA256 b46c1341d3bfb01a88e140e5b2b63388bee28112022536c0a28aa91d7d62b303|
|必要schema|native-preassembled128-complete-chain-necessary-readback-v1|
|必要reader|root_20261115_native_preassembled128_necessary.py，36,489 B，SHA256 a21a16d68b5c84db47e1dd014877a381ff3c6d9e94567f9ddc7d8c5272f2f4d9|

官方来源：[实际run](https://github.com/Rogerhu12/math-research-public/actions/runs/43762998688)、[compute job](https://github.com/Rogerhu12/math-research-public/actions/runs/43762998688/job/132961756447)、[report job](https://github.com/Rogerhu12/math-research-public/actions/runs/43762998688/job/132990691994)。

日志通过GitHub集成返回已解码文本；上表两份日志的bytes/SHA是该返回文本以UTF-8重新编码的身份，不是HTTP响应raw字节或原ZIP身份。读回仅剥除各物理行开头的可选BOM和GitHub时间戳；未剥前返回文本也完整保留在本次临时读回范围。两job的 BEGIN_VISIBLE190_NECESSARY_SUMMARY / END_VISIBLE190_NECESSARY_SUMMARY 之间正文逐字相同，且与原identity事件的64,310 B及SHA吻合。正文加一个LF会成为64,311 B、SHA256 03f077281feead3820767a60bb7c1964fbd0271931cc97a906d8d229c5e5f2d5；本文使用原不含分隔LF的身份，不混称二者。

读回的 summary_complete、transport_complete、cleanup_allowed 均为true，metadata_read_errors为空，explicit_incomplete_error_reply_delivered为false。这些是必要元数据完整性与静止清理责任，不是数学完成标志。reader在Actions内读取了其所声明的完整原元数据对象；本文作者读完了单份必要摘要的全部字段。未返回的大对象明确只按原identity/count引用，不能据此声称逐值审阅了全部大矩阵或角表。

## 3. 同源重生与完整原64前置

本次临时恢复的是固定原actual91小artifact：run43672150224，artifact14145200674，ZIP10,267,458 B，SHA256 78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6；原元数据与下载身份均由Actions实际核对。展开49文件、11,152,340 B，只用于本次初猜和来源。原failed73状态只是初猜，不是accepted尾；没有复用已清理的160/186/其它运行末状态、旧packet或旧J。

两个原历史ready输入仍由8bd267107cc8710d371f3b62c02986655ac965b0恢复，经原client已支持的环境槽消费：

|环境槽|原bytes / SHA256|
|---|---|
|VISIBLE_FLEX_FROZEN_LEDGER_READY|109,004 / 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6|
|VISIBLE_FLEX_FROZEN_STORED_READY|29,774 / c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d|

实际fresh64返回完整129248行与576阶段。其原保存范数为 0.000060618737006888706，明确不同于随后重新评价的128初始范数。新snapshot result为1,316 B、SHA256 f72f009c8eeacfcfe4edd22793c151e6945b8fb10cff2c530b114fb8e81fd37e。完整原J raw SHA256为1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4，状态raw为f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6，原scales为ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc，far图为395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54。

原R273前置没有删cut/far行：129248行、129248列、577节点、576阶段，增广258496行，1153次QR，原η字面1。前置保存的完整raw方向SHA为4b4b1aaacd96910635a03f97d45957ae995c724997a0e18b66ac1d06408e294a。它只是新packet与后续独立owner的来源；当前128残差进入方向计算时又真实调用了一次完整固定64弦矩阵R273，不能把前置64方向冒成随后当前128方向。

完整packet10,348,368 B / afb10fa8fdc4efe6d9615cf414ab990e5095dda4379cff13f50076a17238ce0d，包含576阶段、129248残差、完整226态、224变分维及2048角采样。真实原cusp日程为6943个RK子步、20829个几何取样；它来自原配置导出，不是把576机械乘以12。schedule JSON SHA为3594f1f5da9327c4396350aea82a9086e18d27be96e3db3096c4f6bb00128c1c。cos、sin、gram分别按原binary64表lift，SHA为09ea39767fe694c2490c22c619481f0416d7dd2a4549d9b395f9e9b323f81947、0f15af34da147e02ff3af091cd7239f745c3bac36f8db7df614105b0c7358fcc、9afca32d44481436d49f522d216689efe5a78d0bba1d0c4c478ca90b1508638d。这里没有把独立字面表宣称为准确三角恒等式或连续几何证书。

## 4. 实际持久128求解、唯一试探与独立重放

### 4.1 实际唯一方向

owner完整初始评价：129248/129248行、576/576阶段、failed_stages空、evaluation_error=null、budget_exhausted=false；原norm为0.000122096054597410989492629881621789239，binary128 hex为0x1.000dd1f7889da0c80213a1f62c65p−13。最差原行为stage11、output node11、input node12、Pi第104模、global row2791，原scaled signed值是其负数。

当前r128仅为近似QR的RHS显式投影一次到64，128原状态和原残差不被覆盖。实际128969个RHS词改变，nonzero_to_zero=0，记录的最大原sigma缩放转换误差为4.10665514535721833358792197700840237e−21。方向使用新鲜fixed64 chord，而不是声称当前128精确DF。

这次当前RHS的完整QR实付：cut112、stage129024、far112，共129248行/列，577个node penalty blocks，1153次QR，576次formation；factor/constant464,891,392 B，原记录elapsed7.8133247929999925 s。其形成模型无穷范数9.685824747510231713e−11；它是原longdouble数值模型读数，不能当准确有理界或native接受。

解得的z64原样lift，owner按每节点原sigma128恢复δ128。129182项不同于原R273已round的delta64，最大scaled recovery difference为9.94166392917834227785107527013571685e−28，nonzero128_from_zero64=0；没有把状态经过64往返。

### 4.2 真实非线性接受

|原记录|值|
|---|---|
|direction / trial|0 / 0|
|α|1，binary128 hex 0x1p+0|
|accepted|true|
|reason|strict-original-norm-decrease|
|changed128_state_words|126838|
|changed128_with_same64_cast_values|11239|
|trial elapsed_seconds|1014.091059893|
|接受后norm|9.68582474751023176056740816374984163e−11|
|接受后norm hex|0x1.a9fcb11a67aa9fe05f1217f1302ap−34|
|完整行/阶段|129248 / 576|
|below_original_tolerance|true|

接受后最差原行是stage9、output node9、input node10、Q第1模、global row2128；原未缩放残差4.99890220172700756930979612524613054e−25，sigma5.16104960810073433235339041548094359e−15。原阈值作为binary64字面lift是2.00000000000000012456318291555971284e−09，而非重新指定的新阈值。

owner原终态为 shooting-tolerance-reached，accepted_steps=1、directions_computed=1、trial_evaluations=1；requested_direction_indices=[0]、attempted_trial_addresses=[[0,0]]。原directions1至31及direction0后续trial1至9均明确未访问，不能补称做完32×10。这是达到原shooting停止条件，不是方向预算耗尽。原root_stop为7.99999999999999999055447483647918958e−14，fallback为4.99999999999999969748484640969905465e−12，配置不变。

初始与接受后评价各有27772次root调用、904个Newton更新、904次回溯trial、fallback_returns=0、maximum_iterations=1；接受后original_threshold_reached_count=27772，最大原returned relative为7.97942273584970897156361583077219799e−14。这个原有限停止root口径没有改成理想隐式准确根。

### 4.3 新进程完整重放

独立fresh replay process returncode0、wall_timeout=false，完整原cut/stage/far和两mean重新评价，未将输入state转换为binary64。full residual与全部226 stage output逐词等于owner：

|原输出|bytes / SHA256|
|---|---|
|final-state.f128|2,067,968 / 8fa0eaedacf050e7584a1dee047e97229ca3ec79bcb09eb742ff44e34c1445bc|
|final-residual.f128与independent-residual.f128|2,067,968 / e7061ce086de8a5cbb7b457703381631114ee740d65949770e3d2b8c20ce7892|
|final-stage-full-output.f128与independent-stage-full-output.f128|2,082,816 / 79e3a26a8eef01ba008f957d64c1bf4ec0e41290c772872acde0f6fecd43d16e|

这些只按实际原完整字节等同记录认定，不由maxnorm相同推导。owner original_full_summary为138,655 B / 503d9b3ab30ba758ddbde87e371a0a985ff974550532a458353cc5efd9c4b57c。全部128原数组在Actions临时现场，不在本地重新打开或计算。

## 5. 新stage的确定工程阻断

实际新预装配header为 geometry_20261115_native_preassembled_operator_trace128.hpp，24,706 B / b16fac2b38cc873da63a759f505fde7ccf5b3b6fd9bd0f709647b65be78a7dc8；stage为11,481 B / 1742969b92a4141e216c61e2dae0a3a627e6c88d5810f8c5fdb00b125bc0d480；launcher为28,086 B / 9d8a6cb469f9b7c91e5562b658ea384ebf753adc59a112e4993d628d3823771d。

编译实际returncode1，elapsed0.9667785470001036 s，wall_timeout=false。原compiler.stderr.log为4,660 B / da6e47301159fa471c6bd6c42031ac35e65b62f5e8b0ddfba2995d58484634c6。必要reader返回全部5条匹配error行，未返回每条candidate note；本文没有把这5条行冒成4,660字节stderr全正文。

首条原错误为：

> geometry_20261115_native_preassembled_operator_trace128.hpp:353:37: error: call of overloaded ‘column_environment(const preassembled_trace128::StepDirections*&, int, int&, const int&)’ is ambiguous

随后第355、361、367行的em/e1未声明是同一初始化失败后的级联编译诊断。外层原错误为 ValueError('Actual new stage compilation returned')；launcher科学状态scientific_started=false、scientific_report=null、procedure_complete=false、scientific_complete=false。阶段主scientific_process=null，没有任何本次新576×224 stage矩阵可供速度比较。

源码核对给出确定原因：StepDirections是hoisted_trace128::StepDirections别名；当前namespace又定义一个同签名转发column_environment，而三处调用未限定namespace。普通名称查找与该参数类型引起的ADL共同引入候选。最小后继修复可仅将第353–354行的三处调用限定为preassembled_trace128::column_environment，保原转发函数、原实数公式、算术顺序、尺寸和预算。本文只给源级改法，未本地编译、未执行修复版，也未擅改当前冻结源或派发。

192与196源码各自包含这个同一b16fac header，其launcher也按原bytes复制RECORDED_HEADER；当前源没有对该名称做限定视图。因此它们存在同一源码编译风险，即使各自新的批作用函数不调用旧RK函数，也仍需解析该已包含的非模板函数。这是源码风险定位，不是替未读的192/196实际日志下终态结论。更强digit/SIMD方法的真实效果须等其各自实际范围，或明确修订后新的完整运行；本次不能给出29倍、任何实测速率或完整性能失败结论。

原stage science cap8000 s未被科学内核使用。原component总8345 s包含345 s编译/清理余量；阶段wrapper实际返回2、elapsed1.316952983000192 s。它不是原科学exit70，也不是必要读回协议70；两者标记均false。原summary100,945 B / af9bf20b5133bbf93eab131d3dd48b5a6a384c62ed446c64449075249e512536保留上述工程错误。

## 6. 112 boundary与338×112 endpoint的未付责任

两者不是被简化、以零矩阵替代或重用旧run成果：

|组件|实际attempted|原未启动理由|
|---|---|---|
|boundary|false|missing_component=stages；complete-current-mathematical-input-not-produced|
|endpoint|false|missing_component=boundary；complete-current-mathematical-input-not-produced|

二者各原science cap600 s保持；original_summary_present=false，scientific_completion_not_inferred=true。full_stage_J_complete、endpoint338_by112_sensitivity_complete、complete_boundary112_response、complete_mixed_endpoint338x112_readout均false。没有匹配当前128末点的新全J、完整高度响应或fullDN接受。

## 7. 独立原物理程序audit的真实部分完成

阶段编译失败后，独立audit没有被跳过。它从每个实际binary128 node独立重放原完整物理查询程序，不以缺stage导数为理由伪造完成。audit自身编译return0，elapsed5.72760394099987 s；科学process实际returncode2，elapsed1800.0826918109997 s，wall_timeout=false，stderr0 B。这是科学程序内部1800 s实验预算停止，不是外壳超时杀进程。

原audit scientific_report的complete=false、extrema_are_partial_if_complete_false=true；stages_completed=575、queries_completed=7485、queries_requested=7488。全576阶段的原地址记录仍完整保留，不能只由575计数推完成范围：

- stage0至574各自原complete=true，queries_completed=13、queries_requested=13，error=null。
- stage575原complete=false，active_phase=primal-advance，active_query=9，active_query_advance_completed=0，active_query_advance_count=1，atomic_advances_completed=9。
- stage575的queries_completed=10、queries_requested=13，unfinished_query_suffix=[10,13]，error=explicit-experiment-time-budget。
- 原全部阶段记录canonical152,564 B / 923b3f067be34f4a5fbf397ce1987700a89c6042b1782ea5448225b892d5a0c7，necessary分组只合并完全相等的非地址字典，每个原地址显式保留，缺键与null不混同。

原audit源码在query物理行完整写出后先递增queries，再进入primal-advance，只有rk4_batch返回后才递增advances与active_advance。因此本次query9的物理读回已经计入10个queries_completed，但它后面的一个原子primal advance仍未付；此外未访物理查询为[10,13)。这两类责任不能合并成“仅差三个查询”。原atomic RK总计划6943，audit实际completed_RK_steps=6940；本文不把查询数与原子推进数视为同一计数。依据为冻结a0904ea0物理源的audit循环，不是本地科学重算。独立audit所保存的以下极值均只对已完成部分有效：

|字段|原数值词|
|---|---|
|actualMetric|1.24740319769992190894296352204671455e−16|
|fullD|4.56809189695701091463570460409905198e−22|
|normalizedFullDefect|1.79646354527296221572400805980989501e−23|
|formalCurvature|7.9942546935187970829178002448203843|
|holonomy|7.78643063896605725733473256900848618e−28|
|maxPhysicalPV|2.06869309424094196099662980575035568e−16|
|minD|0.999999999999985867351722004137088646|
|minLeading|0.999999999976030433424450852637560674|
|C_radial_solve_readback_max|2.60294668883439455108061545901388858e−44|

原audit root统计为35247 calls、1146 Newton_steps、1146 line_search_trials、fallback0、maximum_iterations1、original_threshold_reached_count35246；最大returned relative词7.97942273584970897156361583077219799e−14。共有35247 root_tapes、1146 shared_primal_factorizations，direction_column_returns及全部variation计数为0。最后一次未完成过程不能被计成完整成功root。

外层component_resource_partial和resource_partial记录为false，procedure_complete=true，但scientific_complete=false；这是外壳正常收到了内部returncode2/partial科学报告，不能据外壳resource_partial=false覆盖原scientific_report的budget错误。original audit summary274,969 B / ed512ce5f599f69bdc75094bac23e1759b11080b15f008a80acc0b5b894ec2d2；scientific summary155,256 B / fc1c8db8ababbc463a72cb778b316862f37325fb28247c97fdbc6aea6adf7c34。

audit仍是原C-based有限物理程序的binary128 lift；physical_Ldot_is_finite_root_trace_radial_derivative_claimed=false、physical_jets_are_continuous_ODE_certificates=false、C_equals_F_e_claimed=false、IEEE_original_worker_bitwise_equivalence_claimed=false。它不是完整连续ODE证书、不是有限root程序准确导数，也没有解决本次未启动stage的误差界。

## 8. 总预算、原64受控结束与实际清理

全局绝对墙钟19,200 s、owner6000 s、fresh replay1200 s、stage8000 / boundary600 / endpoint600 / audit1800 s，以及cleanup120 s、原32×10/η1/tol均保持。启动owner时remaining_scientific_seconds=17978；component开始时原remaining14915，stage工程失败后audit开始14914；component最终remaining_scientific_seconds_after=13106。global_wall_budget_exhausted=false。本次没有用全局剩余时钟替audit内部1800 s上限扩预算。

原64 worker收到明确 PERSISTENT128_CONTROLLED_ORIGINAL64_STOP_AFTER_INDEPENDENT_OWNER，fresh_snapshot_count=1、fresh_R273_direction_count=1、original_nonlinear_trial_calls=0；原driver exit2被流程区分为受控协议结束，不是新的原64数学拒绝。最终fresh child returncode0、child_reaped=true。完整owner接受只属于上述128有限求解；原64、native与fullDN完成均没有因此被赋true。

2700秒规则同步实际完成三次：

|round|UTC|origin_main_read|规则记录提交|
|---|---|---|---|
|0|21:19:43|8aba84172469ff4b688cb962316e68e395747a1d|2686e518eea0c1f061fcee8802ee26b9e9ad39da|
|1|22:04:47|278d19202d30d1057960876b508be2de869e8056|62a451e8ed1821468ccaac61956bad7eddcc6736|
|2|22:49:53|c1d33ffe52438e9c9f67394c4f17bb1e95b2caeb|137e0238071eacafcf2810acef85a84bdb70341c|

原runner3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde不变，真实reviewed根README21bd547f56590b7f2dd279d0297efb289a9b2783、课题READMEbff8aea253a9e6a7a4fac28d810ac454c5499fec。没有规则变更退出。

必要读回确认fresh child已reap，matching_owned_path_processes=[]、unreadable_same_user_processes=[]、owner_quiet_observed=true。原cleanup先defer直至单摘要成功和静止证据，随后compute实际记录三棵本请求临时树已删除：visible-native-preassembled-final190、actual91-preassembled-final190-parent、native-preassembled-final190-public-original-source；只为原owned archive21个只读目录恢复删除权限，没有改科学文件字节。所有删除均带necessary_summary_and_owned_quiet_observed=true及no_raw_upload_followed=true。现在不能用本文摘要或SHA恢复该128末态作下一run实时父。

## 9. 有依据的后继

本次首先需要修复确定的C++名称限定，而非加预算或删224列。修复版仍须从固定原初猜完整重生fresh64/J/R273、持久128 owner和全部最终组件；不存在可直接接续的已保存当前末态。若选择已经准备的192/196更强完整算子，应明确它们自己实际终态或后继修订的源码身份，不能把本次未启动的stage解释成这些方法无效。

audit当前query9后的原子推进与查询[10,13)仍未完成，不能因为已付极值很小而发布native/fullDN成功。若后继需要调整其资源安排，必须另外显式说明预算变化；本结论不暗中延长1800 s或删最后阶段。原全576×224、112、338×112及独立audit责任保持。

R402只对固定已记录字面系数、名义实际三角因子及准确实线性对象给代数等价边界；本次没有任何新stage数值结果验证其重关联误差或速度。实际名义两回代仍对应记录的因子乘积，不得替换为未证明相等的C逆；C=F_e、因子缺陷导数为零、完整导数区间界和原IEEE图逐词等同均未获得。原owner通过shooting阈值是真实进展，完整课题完成标准仍由这些尚未支付的责任限定。
