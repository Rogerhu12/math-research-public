# R337：actual152 完整128下降与逐字回放已付，末态组件编译阻断

作者：ChatGPT /root（AI协作）。日期：2026-11-15。类型：实际公开 Actions 原记录的完整读回；本地只处理源文本、JSON原词法、字节与SHA，没有重新计算范数、导数、矩阵动作或任何科学量。

实际152从自己的fresh输入重新完成一次持久128射击下降和独立回放；随后stage导数与独立physical audit均在C++编译时失败。112边界和338端点因所需数学输入未产生而没有启动。**这不是达到最终native/fullDN验收，也不是数值域、非共振或资源反证。** 两个job绿色仅表示受控编排与原结果传输完成。

## 1. 真实来源与读取身份

运行：[43722101766](https://github.com/Rogerhu12/math-research-public/actions/runs/43722101766)。源提交0bee3ef1e3587c2a530d98f5657f12e16179b489。compute132836110295与report132851693655均success。完整请求与范围以该提交的 public-native-operator-qualified-final128-request.json 和[152接口](../notes/2026-11-15-request152-qualified-JSON-complete-final128-interface.md)为准；不使用之后的同名文件改变本次来源。

原55个source pin、新same-job入口7c6b02680f4159e4666bf5111438b9fcaaf043b4994cd258bad43a2ab397c4f6、bridge0ccbc8241740b830b3eed0ba2b0e257a21ce93922848c88ad5b500ac5e5e9258、当时qualified shim e609fb0aeae3142fcdb779004ddc0966e86c87c437da0984f50ffa814fb40d36全部在原请求绑定。该shim实际生成的临时C++有下文两个已定位问题；源身份检查通过不等于编译或数学完成。

| 终态读取对象 | 字节 | SHA256 |
|---|---:|---|
| 官方compute日志的UTF-8原文本 | 1489408 | 9b385c95a38d9ae1ec7e67b74e37a0722abbd3a378429ddd0fe3643473d6d9c0 |
| 官方report日志的UTF-8原文本 | 116037 | 646d584ca7cd291068a6e0c2154905f947875f9d2f660af5d0a6aafac1519229 |
| 两job共同的完整primary JSON，不含日志分隔LF | 55647 | 7debb1d7fe10340273cadf98a1163f0616db4b0631fd25d770a2dda8fc1160fb |
| 原stages完整summary.json | 99851 | 83cc79109cc0ea0c6769223af0f913db35b3d6fb3ed139fa6c3eb1dfac0246b3 |
| 原audit完整summary.json | 108106 | 1aae99105f5efb618626f238b41f208ee1ca2a32be77c8a347268d188ec50f7a |
| 原owner完整summary，原读回声明的身份 | 134987 | cd7d2381255d82772beb50ac35e3f8e5d30ed126506475b0708c17312e93a723 |
| 清理前owner handoff，原读取绑定 | 110875 | e4becf8d2cb198d4388c9c9c3501e7a1cf2d7263c614abc927649e73dce800ee |

两份官方日志各只取一次。compute中原primary与report标记内原primary以保数字词法的JSON树重新规范输出后逐字相同，size/SHA也同。stages为643条语义记录，audit为648条，共1291；逐条原canonical字节与SHA全部核对，再按原typed path和容器骨架组装，两个整树的原size/SHA全部吻合。共8个object、2个array容器事件与1281个完整value。没有用浮点JSON重算原数字或截去长整数。

后两个owner身份仅按实际生产者完整读取记录保留，本文不宣称从一个hash取回已清理的全部数组。所有大数值文件、临时C++/可执行文件和输入均依原规则在Actions读回后清理，不新增Git、Release或artifact原始数据。

## 2. 原输入、fresh64与近似chord的完整范围

本次仍从actual91 run43672150224 / artifact14145200674的完整原ZIP恢复初猜；10267458B、SHA78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6。没有从已清理的133、140或另一128末态重建当前state。

新的snapshot/result.json为1316B /452d1ad27fae3bf6c04ae22aa59a4c24dcdf7899a7ad19049c8d1cffb0053287；完整129248维/576段/577节点，原112cut与112far均保留。实际fresh64数组身份如下：

| 原数组 | 原raw SHA256 |
|---|---|
| base-states | f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6 |
| cut-residual | 12e751094f28b905e020e94c8e86db6ebdeadfb7bfe03c3406599174e427628b |
| cut-target | e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d |
| end-residual | 30939371bf346ff34a7534d70f1c42ff3b1dd35f708ba6a046b34dd30fef7f28 |
| original-far-graph | 395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54 |
| original-scales | ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc |
| physical-height | c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f |
| stage-jacobians | 1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4 |
| stage-out | 678406f04dc59408e23fbc3ac66ed3bb74262a5184f6cfea690841cf68418a72 |
| stage-residuals | 04ec3639e1a3ec4965ff4d7532bbe606e54aed895dd0523dc743702b0bd9e1f7 |

这十个数组是本run重新形成或绑定的原数据。进入128迭代后，fresh64 J只作为固定近似chord，未冒称当前binary128完整程序的导数。原物理H、sigma与far图均来自本次绑定，未通过抹掉高模、零高度或新cut投影更换数学对象。

前置64位R273原记录的 factor_and_constant_bytes=464891392、rows=columns=129248、augmented_rows=258496、node_count577、stage_count576、罚块577、纯常数行129248、qr_calls1153、formation_calls1152；elapsed_seconds22.58483327800002。原64位当前norm为6.0618737006888706e-05，原float64字为71f299f11bc80f3f。

该前置模型的exact affine全行最大残差原显示为9.685623139820915231844260456306540893890861679791289092058094119E-11，最坏stage9/Q1/global row2128；它不是后续128当前残差，也不是严格stage导数证书。底层longdouble报告的significand_bits=64、itemsize16，不能因dtype名称float128称为IEEE binary128科学精度。独立C++ owner使用的持久binary128与此近似QR工作精度分开。

## 3. 当前128右端、完整方向与唯一试步

owner先在持久128状态上重新计算所有129248原行。初始norm为

$$
0.000122096054597410989492629881621789239,
$$

原binary128 hex为0x1.000dd1f7889da0c80213a1f62c65p-13；最坏stage11/Pi104/global row2791，input node12、output node11，原残差−6.32022287232257274964381733314263019e-19，sigma5.17643497421954467891015949609799199e-15。576段与全部行完整，failed_stages=[]、evaluation_error=null、budget_exhausted=false。

当前128右端另送一次完整R273近似solve，固定chord身份4375c1ec5d7523996614d3fd46e44346fdacea5727db8ad1e908afb56fb17b99。完整行序保持cut112、stage576×224、far112；eta=1。该次原记录：

| 原字段 | 原值 |
|---|---|
| rows / columns | 129248 / 129248 |
| augmented rows / stage rows | 258496 / 129024 |
| node penalty blocks / pure constant rows | 577 / 129248 |
| qr_calls / formation_calls | 1153 / 576 |
| factor与constant字节 | 464891392 |
| QR elapsed_seconds | 6.277537541000129 |
| 128右端转64改变项数 | 128969 |
| 非零转零 | 0 |
| sigma归一转换误差最大原显示 | 4.10665514535721833358792197700840237e-21 |
| formed residual infinity原longdouble显示 | 9.685824747510231713e-11 |
| formed residual L2原longdouble显示 | 1.130568575521336125e-10 |
| full unpreconditioned gradient L2原显示 | 1261309.1059448874298 |
| model objective原显示 | 6.461955386998909204e-21 |
| factor triangular residual infinity原显示 | 1.0667321179483844895e-20 |

这些误差和gradient是原数值读数，不是R314/R325的严格外包。原128状态与残差没有被这一次近似右端转换覆盖。

方向按每个原sigma乘提升后的z64，在128中恢复全部577×224项；不直接把已圆整delta64当作128方向。different_from_R273_delta64_entries=129182，maximum_scaled_recovery_difference=6.21420740974797949698112574685574514e-28，nonzero128_from_zero64_recovery_entries=0。完整direction.f128为2067968B /a2364e304467a1cd83d744430e66a8c623c69e789dbe72381e69deaa346e18a3；原scaled_z.infinity_norm=1.1744305406651254531844570279775999e-11。

实际只执行direction0、trial0、alpha=1，返回accepted=true，reason=strict-original-norm-decrease。原trial elapsed_seconds=804.683069474；改变126690个128状态word，其中11183个变化在cast64后看不见。全部576段/129248行完成，norm降至

$$
9.68582474751023176032080482454992093\times10^{-11}.
$$

原hex为0x1.a9fcb11a67aa9fdf970095730bcp-34。原2e−9阈值准确提升值2.00000000000000012456318291555971284e-09，本次below_original_tolerance=true并以shooting-tolerance-reached退出。最坏stage9/Q1/global row2128、input node10/output node9，原残差4.99890220172700756918252291853272271e-25，sigma5.16104960810073433235339041548094359e-15。

原32方向×每方向10档的算法界未改。未访问direction1…31及direction0的trial1…9；它们是达到原停止条件后的未执行后缀，不是31次拒绝或九次补算成功。

初始与末次均记录root calls27772、Newton_steps904、line_search_trials904、angular_evaluations29580、maximum_iterations1、fallback_returns0、original_threshold_reached_count27772。末次max_returned_relative_decimal=7.97942273584970897156361583077509912e-14；minA=0.999999999975949816097646428367803865，minD=0.999999999999985782663062751174097867，minS=0.999999999999999999999999999688946329。它们描述实际有限root停止策略的返回，不是对准确隐式根或连续场的证明。

## 4. 完整末态与独立fresh回放

| 实际原件 | 字节 | 原SHA256 |
|---|---:|---|
| final-state.f128 | 2067968 | e0f20c36d59ac200796a03441e7b5604224e3add414361a11cc6ff3586dffba2 |
| final-residual.f128 | 2067968 | 18cfb3face9b286513f624003984d318bc6b6c735ed803a3cbffde15dc6be39b |
| 全576×226 final-stage-full-output.f128 | 2082816 | 13195bbb4249c47b158399c36d173de0fc8bfc80e3b9f5ad98ed1411ff715f9e |

独立进程从实际final-state直接重放，未转binary64。原报告 independent_fresh_replay_complete、fresh_replay_full_residual_words_equal_owner、fresh_replay_all226_output_words_equal_owner均true；独立residual与完整226段输出分别具有表中同一SHA。不是只比较一个norm或224 shape列；两mean输出保留。原mean_height_sum=0.0226842463487103007695708959242220956，hex0x1.73a8a00cef80fae4744e57d3f5bp-6，owner与replay相同。

owner与replay均process returncode0、wall_timeout=false、stderr空；其完整原记录在读取中逐字段保留。独立回放支付该有限程序当前末状态的完整残差一致性，不支付stage导数、112/338或physical audit。对该回放的数学意义仍按[R308](R308-actual133-persistent128-shooting-tolerance-and-identical-fresh-replay.md)、[R321](R321-actual140-complete128-descent-and-final-component-compile-stop.md)的原范围。

## 5. 两个真正启动的编译与两个尚未启动的数学消费

清理前post-owner hook真实发生，绑定当前末状态和原owner handoff。完整输入packet10348368B /1c9df6b2aa203d526eee11fe443ebcb474584c677b76ed3901b6a0f6c1f37aa8，结构SHA0557fb2e87c5f529551d3027b48004148f04eacaba6e955508c68e3fe4585bb5；576 cells、6943原子RK步、20829几何样本和2048角节点均在原布局中明列。原逐cell布局和各表完整保在两个恢复的summary中；w、w²、E没有互相重造。

| 组件 | 实际尝试 | 原返回与原因 | 数学范围 |
|---|---|---|---|
| stages | 编译已启动 | g++ returncode1，child returncode2 | requested完整576×224，但scientific_started=false |
| boundary | false | missing_component=stages | 完整112响应尚未启动 |
| endpoint | false | missing_component=boundary | 混合338×112尚未启动 |
| audit | 独立编译已启动 | g++ returncode1，child returncode2 | scientific_started=false，独立physical程序尚未执行 |

stages原error为ValueError('Actual new stage compilation returned')；audit为ValueError('Actual component compilation failed')。两完整summary均scientific_complete=false、resource_partial=false、procedure_complete=false、transport_complete=true、summary_complete=true。不能把transport字段读成science字段。

stage编译原elapsed_seconds=0.665550015000008，audit编译0.6657606750000014。两编译均requested_cap_seconds300且wall_timeout=false；stage整个child0.9659004740001365秒，audit整个child1.0662745899999209秒。完整post组件总计原2.103669673999775秒，剩余science15745秒，未触及19200全局deadline。

实际stages stderr共99行/12456B /e4fd39a5b84e52915cb01c22e6dd6a17cce79ddfc661b7c2f1ba6fdbac63d52d；audit stderr35行/4723B /5a964d46d73ede2cd1a68322ef5b55fdd09a5539295f9cc5a8de54fc7424dac0。全部134原行逐行size/SHA以及各整件SHA吻合，另一12000B分段路径也还原同两件字节。

### 5.1. JSON调用的三冒号词法错误

旧shim把每个无资格quoted(替成::quoted(，没有在前一个条件运算符冒号后加分隔。因此实际临时源出现：

~~~cpp
failure.empty()?"null":::quoted(failure)
~~~

编译器原错误是expected ':' before '::' token，伴随expected id-expression及括号诊断。实际发生位置：

- operator_trace128.hpp 第339行；
- operator_stage128.cpp 第146、156行；
- physical_final128.cpp 第124、216、234行。

同一错误不涉及原RHS、root矩阵、物理域或区间有效性。逆替换逐字回到旧源的检查，只能证明变换来源，不能证明C++生成词法合法。

### 5.2. stage统计类型的名称歧义

operator_stage128.cpp 第44行std::vector<BatchStats>及第94行BatchStats total同时遇到operator_trace128::BatchStats和shared_trace128::BatchStats；全局已有using BatchStats=operator_trace128::BatchStats仍没有消除原using namespace组合下的歧义。原stderr明确列出两个struct和using别名。随后的begin/end、下标和total未声明均是该编译过程的后续诊断，不是QR或stage计算的数值失败。

本次真实生成的源身份：

| 数学源角色 | 原字节/SHA256 | 旧shim实际临时字节/SHA256 |
|---|---|---|
| operator header | 24617 /950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0 | 24641 /046fafc0421ebf22a68437abab62594a525acbec815a660719f91a2c18cd0a0e |
| stage translation unit | 10682 /86782f8038e57bd87f578ca8a4b48640514ce36e8b11de4df172b20bd10d2926 | 10700 /ad61daf7f86f46bac20102764e65d4448f23a725a7db4917235ea789cf7075bd |
| physical translation unit | 18055 /a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415 | 18153 /05a4a97c41e0e53347b51fc6eb9936eba62a73e224e267e3c3e14c6e5b74014f |

quoted调用计数分别12、9、49，原生成R283 prefix31738B /fd676b38fbc83abeccf85ca6956b325d15b26425f9147e3d52d2283cd1ae4956未改变。实际编译器没有产生可用stage或audit可执行文件。

## 6. 全部传输、资源及退出意义

除了两个完整语义树，还恢复八个原日志流。四个空流是stages/audit的外层stderr及各compiler stdout；其SHA均e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855。四个非空流共16个原byte段：

| 原日志 | 段数 | 字节 | SHA256 |
|---|---:|---:|---|
| stages stdout | 8 | 90556 | 6fff5d1593a58f3cda934994a27cc01e836afeeaa933179cbf2b739760e5acf1 |
| stages compiler stderr | 2 | 12456 | e4fd39a5b84e52915cb01c22e6dd6a17cce79ddfc661b7c2f1ba6fdbac63d52d |
| audit stdout | 5 | 48135 | 0595d2ac4ecd27f06274750d26585940bcc7369e37362856a37d14970eb46dda |
| audit compiler stderr | 1 | 4723 | 5a964d46d73ede2cd1a68322ef5b55fdd09a5539295f9cc5a8de54fc7424dac0 |

每段原offset、length、SHA及拼接whole SHA均核对；按inner ASCII JSON与UTF-8 surrogateescape恢复，跨字节字符不丢失。错误的两个逐行流与字节流相同。没有只读短summary、最后错误尾部或把超长原记录换成hash后称其字段全读。

本次原外层elapsed_seconds3335.786776389，owner launcher2431.5768387129997，wall guard2433.95748267；guard_returncode0、child_returncode0、wall_timeout=false。原owner6000、replay reserve1200、stage8000、boundary600、endpoint600、audit1800、读回reserve120及各编译余量保持。时间属于各自原作用域，本文未通过相减补造未记录子阶段时长。

原64 native worker在形成当前基点和R273后按声明受控停止，原64 nonlinear trial calls=0、original_driver_exit_code=2；128状态没有写回64 worker。外层summary_transport_exit_code0、procedure_complete=true与两个组件的science失败同时成立。不存在原64求解失败改成功或native接受。

实际规则同步记录14:02:30读40eb0b261e814cca22243beed1f7c7c5f60791b6，14:47:34读58132a1ad4b38b96fcc4f35d5fe4810c1437fb16；双README按原2700秒规则读取，科学checkout未替换。原完整inputs/native-work/owner输出与恢复缓存最后清理；目录权限恢复仅便于删除，不改数学字节。

## 7. 明确未付与立即继续的修复范围

本次complete_stage_maps、complete_boundary112_response、complete_mixed_endpoint338x112_readout、complete_original_C_based_physical_program_audit、all_requested_components_completed、native_accepted、fullDN_accepted均false。nominal_factor_residual_derivatives_proved_zero、old_dL_graph_word_equality_claimed、C_equals_F_e_claimed、direction_error_bound_supplied及IEEE_roundmap_derivative_claimed也没有因128残差很小变成true。

planned R305有限stage变分与原R302 boundary/physical责任继续分开：名义因子缺陷、真实$F_e$和当前有限trace导数、全部上游RK、338混合方法与原几何最终门都保留。未启动的576×224不是已完成一个前缀后凭计数推定的suffix，更不能从本次编译错误推非共振、域或算法不存在性。

160将从同原fresh91/64J/R273重新生成128现场，采用独立v2 shim：在条件冒号和全局::quoted之间明确词法空白，只对stage/exporter实际需要的统计类型作operator命名空间资格化。旧150/152与原数学源不改；原完整576×224、112、混合338和独立audit及全部预算/退出/验收保留。[实际150的同类完整读回](R338-actual150-persistent128-replay-and-strict-exporter-compile-failure.md)由独立run记录，不能用它替本次任何缺失组件。所有已清理现场依完整原source和参数重算，不凭hash恢复。
