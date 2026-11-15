# R394. 原160真实128位一步接受、完整物理程序审计与20段后阶段映射预算停止

作者：ChatGPT /root（AI协作）。日期：2026-11-15。本结论由182r3只读原160日志获得；没有重算原科学，不把读回绿色改写为原160的native/fullDN接受。

## 1. 真实来源与完整必要读回

| 对象 | Run / source / bytes与SHA256 |
|---|---|
| 原科学160 | run43729874541，source b34692d09c8d5ecdd7b859e43489da4413f1468e，compute132859748674 |
| 本次只读182r3 | run43757046032，source442413b6b20a33c94b3702d5b02d8ab4433449d9，job132943297720 |
| 本次完整job日志 | 122296 B / 017ec4aa0352533cb2efa7330f143051366b62e7394d10caeedf04202f52c4ed |
| 单一必要摘要，不含分隔LF | 89268 B / da406178130fc01cd9d55856e78739dda98331a658e8437e7ee0e923bd50c24e |
| 同一摘要文件，含最终LF | 89269 B / 35f0397fe9c40c7aad0d765e72b26aa7c0b87e19e74e5b4a24c8efd6226fb0c7 |
| Actions内部临时result | 89030 B / cd59fc4b9226e7b6834b0d8b52a19cb51d81e4f0bf114862ffe9cc72e0201d52 |
| 原160整份compute日志 | 3234095 B / 27c888838abc2cabbe0dd14886ffdcffa76e4d35f21048b30367799d04363149，3513物理行 |

本次reader为77510 B / 1536a01102f2c6620adbb43c0b8e1708bd57e194961079f0aa3016a152629c28，request12054 B / 378d9707f46e03d2247eff9294fd3a9b0ae25abd1ea2389c12ba73719fc1fc0c。完整八来源、原run/job/source及双README绑定通过。原大日志只在公开Actions流读，原科学模块没有导入、编译或执行；本地仅读取必要原字段。

原流到EOF、协议0错、组件解析错误空、optional协议错误空、error=null；本次elapsed_metadata_scan_seconds=3.098954443000025、resource_partial=false、reader_exit_code=0，transport/readback/summary/complete_necessary_scope_returned全部true。必要摘要没有放宽90000字节上限。首182的92966 B及r2的90136 B超限仍分别按[R388](R388-actual182-complete-original160-log-and-necessary-summary-overflow.md)、[R393](R393-actual182r2-original160-necessary-summary-136-byte-overflow.md)保留，不能回填其未返回内容。

root在job终止后唯一取本次日志，完整读owner全部trial/evaluation、四组件及全局责任、所有原终态/QR/资源事件和完整未付stage地址；成功大数组、全部列见证及旧完整科学语义树没有重建或下载。具体表示与范围见[182接口](../notes/2026-11-15-request182-original160-native128-necessary-readback-interface.md)。

## 2. 原owner在当前128位状态上的真实一步

原owner接实际91失败基底作初猜，只重用fresh binary64 J作明确的近似chord；当前128位状态和当前128位残差不被64位词替换。它请求原32方向×10档，实际只用方向0的trial0：

| 字段 | 原记录 |
|---|---|
| α | decimal 1，binary128 0x1p+0 |
| base norm | 0.000122096054597410989492629881621789239 |
| 接受后及独立fresh replay norm | 9.68582474751023176032080482454992093e-11 |
| 原容差 | 2.00000000000000012456318291555971284e-09 |
| 接受理由 | strict-original-norm-decrease |
| 本trial elapsed_seconds | 804.740321431 |
| changed128_state_words | 126690 |
| changed128_with_same64_cast_values | 11183 |
| 方向 / trial / 接受数 | 1 / 1 / 1 |
| 原stop_reason | shooting-tolerance-reached |

初始与末次evaluation都完整覆盖129248行、576stage，无failed_stages、无evaluation_error且budget_exhausted=false；末次below_original_tolerance=true。独立进程fresh replay与末次evaluation全部原字段相同，摘要以相同记录引用保存；该replay包含原cut/stage/far和两个完整mean accumulator，scope明确不是几何审计。两次mean_height_sum均为0.0226842463487103007695708959242220956。

初始最坏行是stage11、input_node12/output_node11、Pi mode104、global_row2791，normalized signed为−0.000122096054597410989492629881621789239。末次最坏行为stage9、input_node10/output_node9、Q mode1、global_row2128，normalized signed为9.68582474751023176032080482454992093e-11，原residual为4.99890220172700756918252291853272271e-25，sigma为5.16104960810073433235339041548094359e-15。

每个完整evaluation的原root统计：27772 calls、904 Newton_steps/line_search_trials、29580 angular_evaluations、maximum_iterations=1、fallback_returns=0；末次maximum relative为7.97942273584970897156361583077509912e-14，原D/A/S最小值分别为0.999999999999985782663062751174097867、0.999999999975949816097646428367803865、0.999999999999999999999999999688946329。它们是原有限计算读数，不是连续空间证书。

原未访方向明确为1..31；已请求方向0的未访trial为1..9，由已达到shooting容差而未继续。没有把未运行档写成拒绝。owner_final仍明确native_accepted=false、fullDN_completed=false、endpoint338_by112_sensitivity_complete=false和original_geometric_final_audit_complete=false；后续独立component审计另记，不能倒改owner当时的flags。

## 3. Fresh64、当前128残差和方向恢复必须分责

原fresh64 snapshot的norm为0.000060618737006888706，其精确存储读数的显示为6.061873700688870870601158412977629481529154353251182450024889837E-5；它不是上述128位初始norm。fresh64原R273后线性精确读数显示9.685623139820915231844260456306540893890861679791289092058094119E-11，也不能改标签为128位真实非线性末norm。

当前128位r只为近似QR做一次RN转64：128969项改变、0项非零变零，原sigma尺度最大转换误差4.10665514535721833358792197700840237e-21。原r128仍在owner内。当前chord QR完整保129248列/行、129024stage行+112cut+112far、577节点、576stage、258496增广行、1153次QR、464891392 factor/constant字节。原working_precision字段虽名float128，其significand_bits=64；不能称它是IEEE binary128精确QR。

方向用lifted sigma与solved z64在128位形成；129182项不同于原delta64，0项从原0恢复为非0，最大scaled恢复差6.21420740974797949698112574685574514e-28。这只区分两种形成顺序，不把该差当当前chord的方向误差界。原fixed64_J_is_current128_derivative=false、direction_error_bound_supplied=false仍保持。

## 4. 四组件的实际完成状态

| 原组件 | 是否尝试 | 原science cap | 真实状态 |
|---|---|---:|---|
| stages | true | 8000秒 | 20/576完成；budget_exhausted=true；原process70、transport_complete=false、scientific_complete=false |
| boundary | false | 600秒 | missing_component=stages，complete-current-mathematical-input-not-produced |
| endpoint | false | 600秒 | missing_component=boundary，同一缺完整输入原因 |
| audit | true | 1800秒 | 576stage/7488查询全完成；process0、transport/scientific_complete=true，无resource_partial |

因此，boundary与endpoint不是执行后的数值失败，而是没有启动。完整112 boundary响应、338×112 mixed endpoint及全native/fullDN仍未支付。audit不依赖完整stage maps的成功，原预留2145秒已真实供它运行。

stages实际process elapsed8004.6069634410005秒，scientific elapsed8000.002979012秒；actual_error=null，wall_timeout=false，component_resource_partial=true，明确是自身8000秒科学预算到时。原component总额8345秒含345秒编译/清理余量，不把它与实际elapsed混同。

audit实际process elapsed1436.7853913010003秒、component总额2145秒含345秒余量，无wall timeout；下面单独记录其有限程序范围。

全四组件阶段总elapsed9441.670058575999秒；原记录remaining_scientific_seconds_after=6304。整个160 global wall budget并未耗尽。没有根据余量反推原stage cap应当是多少，也不把局部预算stop改写为数学拒绝。

## 5. 阶段映射的完整未付范围

该阶段源为R305缓存angular partials与nominal-factor contracted action。原结果明确请求576stage、每stage224列、完整226状态及mean/port方向，当前几何方向为0，输入为真实owner binary128末态、不cast回64。

原stages_completed=20，complete_requested_range=false，complete_224_stage_columns=false，complete_576_stage_primal=false。全部576个stage记录在原summary中存在；完整未完成表有556行，逐地址已读：

- stage20、21、22：各要求12个atomic步骤，完成8个，未付suffix[8,12)。
- stage23：要求12个，完成7个，未付suffix[7,12)。
- stage24..575：完成0个；通常要求12个，未付[0,12)。
- 上一项中的stage28、31、63、98、103、135、169、175、202、207、240、247、272、279、312、319、344、351、384、391、416、423、456、463、488、495、528、535、560、567要求13个，未付[0,13)。

这些stage的原error均为explicit-experiment-time-budget；原table同时保requested、completed、active/query字段与存在范围，没有补造未执行query值。所有遗漏column地址表明确stage i的input_node=i+1、output_node=i，i=20..575。这里用原完整地址的紧凑描述保未付责任，不归档可重算逐行原表。

完整未完成table原canonical身份为57189 B / a5e2b13c924de5c38c0f202a122fcb949c36d5175ebda8287b9628fc441c77e2；全部576成功/未完stage记录的身份为1110933 B / 390c24ad2e75c8109f948c97cf353fe2938929d0c132aa228c83a091bdb0d5ae。原组件summary1227010 B / 17898e79c1e69fcc2c6ac36d4cc690f74450bfe86c151b169c8c2d82b6f6bcc1。成功完整列数据仅身份，并非root逐值审读。

原partial工作统计给出272 completed_RK_steps、61243 completed_column_steps、1104 root tapes、557 shared primal factorizations、124768 shared factor direction solves、14098784已读C方向残差行；形成C方向solve最大残差4.11423022787800627789057788027785987e-38。shadow_words_checked=124353220、shadow_word_mismatches=0。nominal LLᵀ−C最大1.34815096107106509713918455980944912e-33；这些有限partial读数不证明C=F_e、全部残差导数为0、完整branch stability或IEEE roundmap可微。

optional_reference_columns=none、reference_field_columns=0、reference_difference_is_error_bound=false。不能把没有调用参考列时的零差记录当全576误差证书。其余R302/R305的完整原方向和真根责任仍保。

## 6. 独立物理程序审计确实完成，但范围有限

原audit从每个实际binary128节点独立replay，使用原live配置导出的query schedule/cusp advances，steps_per_profile=12、完整576stage、7488/7488查询、6943 RK步骤；未完成stage表空，complete=true，预算未耗尽。原角行列为ur、ut、urr、urt、utt、Darboux、height，全部角行只在原临时现场，root读取原必要最大值及身份。

| 原audit字段 | 原数值词 |
|---|---|
| actualMetric | 1.24740319769992190894296352204671455e-16 |
| maxPhysicalPV | 2.06869309424094196099662980575035568e-16 |
| normalizedFullDefect | 1.7964635452729622157231147320388882e-23 |
| fullD | 4.56809189695701091461722792235368782e-22 |
| holonomy | 7.78643063896605725733562794518636706e-28 |
| formalCurvature | 7.9942546935187970829178002448203843 |
| minD | 0.999999999999985867351722004137088646 |
| minLeading | 0.999999999976030433424450852637560674 |
| C_radial_solve_readback_max | 2.6029466890130574441683143946488288e-44 |

此处fullD是原audit字段名，不能认作课题README中的完整闭F0直径D。actualMetric也只属于原离散审计，不是连续全域相对metric算子证书。

原physical_radial_jet_formula为original-C-based-finite-program-lifted-to-binary128，literal几何和独立tables从binary64提升，状态相关三角用libquadmath cosq/sinq；C_equals_F_e_claimed=false、physical_Ldot_is_finite_root_trace_radial_derivative_claimed=false、physical_jets_are_continuous_ODE_certificates=false、IEEE_original_worker_bitwise_equivalence_claimed=false。原native_accepted/fullDN_accepted仍false。

完整audit summary274176 B / 75c94c52ac4841f177449941ecee03ca698c1737d43cf04f0f2134f6403ced6d；576stage审计记录身份152531 B / 5e9fdba9116f86e2ae03e87408a9dfbe825e4b10835a335bbe45f0e2dab3c0af。成功数组及原大表不重归档。

## 7. 原70的两层原因、读回和清理

原160 summary transport尝试98321 B / 5eaf380bf81df072910a4bc717fe6f221aa76cd6941ba3160b4f0bc99a7e95e4，full summary206283 B / df877d69de88bd47ccad4d84feaef102f430728ebe4907c917644270c1cda250，原摘要超限导致70；同时stages确实因自身8000秒预算只完成20段。两层原因须同时记录，不能将全部未付解释为仅传输问题。

原owner wall guard elapsed11873.267304785999秒、limit18176秒、wall_timeout=false，child/guard70；原procedure总elapsed12778.157638503秒。原binary64 worker受控停止于independent owner返回之后，original_nonlinear_trial_calls=0；这与真实128位一次trial不同。原driver exit2及controlled marker不表示那次128位trial被拒绝。

182r3完整核10条原诊断字节流身份、无unfinished stream/optional tree；6个compiler/stderr直接读回均空。audit.stdout的一条77290 B原匹配行因不可拆且超过12000B只保身份，没有全文显示；必要audit scientific_report字段已从原direct投影完整保留。这不是声称所有原文本或所有科学树已逐字重建。两处原重复字典引用只在同一必要JSON内且先前完整字段相等；旧producer树SHA只作原receipt，不冒本次重新计算了旧树SHA。

本次retained-summary步骤核同89269 B身份，随后owned_cleanup_complete：reader已同步join，无新scientific子进程，原日志只流读未存；本次只删除自己的临时metadata。Git/Release/artifact新增raw均0。原160成功末态2067968 B / e0f20c36d59ac200796a03441e7b5604224e3add414361a11cc6ff3586dffba2仅为原身份，不承诺清理后的state可凭SHA续接。

## 8. 后继实际责任

原完整非零native/112边界响应/338×112敏感度、fullDN/finalJ和真正闭450场仍未付；R345单字段230列严格trace不能替代本次完整stage矩阵。不能靠删除stage、减少224列、复用旧失败config/J，或把本次C-based审计当真F_e来取得完成标签。

下一实际工作已转到完整stage算子的源码与瓶颈：保持同一当前128状态、全576×224、真实根trace及原门，寻找可说明等价的实现提速；之后同job真实重生原父并接完整boundary/endpoint/audit。不声称本次未保存stage可直接跨job续算，也不以一次增加墙钟替代完整算法责任。README的同g闭合、C²、held/δE/reach/全域metric及固定参数精化仍继续。
