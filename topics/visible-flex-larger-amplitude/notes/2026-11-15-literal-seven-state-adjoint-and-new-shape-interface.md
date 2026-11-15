# R351 requestless完整七状态伴随 helper 接口

作者：ChatGPT /root/amplitude；2026-11-15。

本源实现已发表的[条件代数证明R351](../results/R351-literal-seven-state-adjoint-and-C2-control-response.md)。它是新的线性响应形成方法，不是原forward舍入结果的改名，也不是新参数族、优化器、候选接受、原场求解或误差证书。没有为尚未运行的request164选择父点、新shape、系数或未来run。

## 1. 冻结源码与实际固定对象

新增 computations/geometry_20261115_literal_seven_state_adjoint.py：35419 B，SHA256 12a95d40929cc7799761e56c33eadc9e5fbe16fa3eacf0d0be94c56ea3452b0f。

唯一数学依赖是原 geometry_20261115_nine_control_decimal_literal_model.py：23719 B / 2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75。helper先检查本仓公开Actions环境，再按完整bytes/SHA加载它；导入helper本身不触发计算。新源未修改原149、154、157或0865族。

原九族身份仍为 geometry_20261115_small_core_nine_control_family.py / 086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629。本helper不重新导入族、重新积分标量表或重新生成原699节点数据，而消费当次真实persistent model/state。原mesh、h、mid、base/control表、112×112尾端J、三个target、cut scale与height sign保持明确有限字面对象；若由154二阶wrapper包裹同一primal，其实际扩展binding仍完整保留并核canonical hash。

所有新算术只在公开Actions内、原Decimal50 / ROUND_HALF_EVEN及同一指数/异常context执行。输入的50位参数字符串是已经存在的有限输入，不假称它来自更高精度真解。没有float投影来形成新动作。

## 2. 真实输入API

构造：

    adj = SevenStateAdjoint(
        actual_model, actual_returned_state, actual_binding,
        event_sink=record_actual_event, deadline=absolute_monotonic_deadline)

actual_binding须包含：

- producer：当前独立执行producer的name、bytes、sha256。仅同目录Python源basename，逐实际文件字节核；不接受任意raw路径。
- expected_literal_binding_sha256：actual_model.binding中当次canonical binding SHA。
- actual_parameter_words：实际返回state的九个Decimal字符串，逐词匹配。
- parameter_origin：明确的原科学run/source/状态或配方来源元数据，非空对象。

helper重新核model.binding的canonical hash、699/112/9/50位等合同和原diagonal分支，保存实际参数词、所用Decimal系数摘要、真实七状态/ratio/三残差/112右残差投影身份。该状态投影摘要不是完整原state文件SHA；所用Decimal系数摘要也不是新做的全部binary64原数组独立审计。

parameter_origin是调用者提供并保留的来源声明；helper没有网络获取旧日志，也不凭这个声明独立证明其历史接受。后续producer须把真实原配方/父身份、原四输入和其消费闭包完整绑定。不能把一个failed/未完成场重标成accepted parent。

构造时复制这些已经存在的Decimal对象及元数据，不调用model.evaluate、model.response、description、FD、native或优化器。初值必须是原固定
$(r_0,y_0^{(1)},y_0^{(2)},y_0^{(3)})=(1,1,0,1,0,1,0)$；
不同初始化属于新模型，需要另源，不可悄悄忽略start项。

## 3. build的完整数学作用范围

adj.build()在同一个原Decimal context内完成：

1. 全698个cell的局部七状态映射：输入为原七状态及三个ratio $q_L,q_M,q_R$。利用原Jet同时播种10列，形成完整7×7 A及7×3 C。
2. 全112右端与原三个优化残差的八输入变分：输入为末七状态和独立末节点$q_N$。保存完整112×7、112项直接$q_N$导数，以及原三行对应量。
3. 一次三列reverse递推及共享ratio scatter。node共有699个、mid共有698个，每个保三个原残差权重；node N另加原终端直接$q_N$项。返回原start cotangent，虽然当前固定初始化的实际变化为零。

局部映射保原半径消元、中点半径、速度、正平方根、三个2×2矩阵乘积、原L/R及显式det/回代的算术顺序。矩阵B直接调用hash核过的原LiteralCircleModel.matrix函数体；m2m/m2v/solve2/Jet/sqrt均调用同一个冻结模块。没有冻结r或把半径变化从模态链删除。

完整终端仍按原112×112 J每行每列形成原sum和前三项导数补项。即使native输入只有低三非零，也不删高109行或非对角coupling。原exactly_diagonal分支保原unit defects；其他分支保原full_right前3行。两者不混用。原J/target/gamma/eh之变化在本有限模型定义下为零；这不等于真实current native改变g时可以冻结其响应。

原累计height不进入这三个有限优化残差，因此不列入最小七状态；原完整circle、453方阵、几何高度、FD/native/fullDN/final检查仍是后继producer的完整责任。

build完成不意味着新科学候选被接受。每cell只比较新局部回放的**七个primal输出词**与原下一frame；原terminal比较三残差及112右残差词。没有把七词相等冒成原全部B/L/R/height等状态数组逐字相等。所有差异只记录；不是新增门，也不是可据此保证导数准确的条件。

## 4. 数组、实际字节与partial

adj.report()给完整来源、费用、已形成cell数、尚未执行后缀、reverse已完成数与未访问前缀、末端完成状态、所有局部七词比较的身份、实际不相等位置及terminal具体差异。所有局部A/C、终端、node/mid权重都有当前canonical SHA。

adj.formed_arrays()仅返回当次内存数组供同job消费者使用，不写文件、上传、打印原大表或创建artifact。只有complete build可取完整数组。后续消费者若只输出这些数组的SHA，必须明确未逐值读范围；不能再用编码/拆块把大原数组经工具传送。

绝对deadline在每个local cell、terminal形成前、每个reverse cell以及每个shape前传cell之间检查。若到时，抛AdjointBudgetStop，保resource_partial、真实阶段、已做数量和未访范围。有限除数、正域、非有限变分等异常与资源停止分开，具体repr/完整traceback进入事件。partial build不静默续作完整；可新开明确任务，但不能借原partial状态伪称全链已付。

事件sink由producer负责在清理前保紧凑实际事件和必要原字段。helper不替producer编造报告完成状态，也不将传输失败当数学反证。本次没有源代码之外的fixture或运行结果。

## 5. 真正新增shape的接口与身份

调用：

    result = adj.sampled_shape_response(node_pairs, midpoint_pairs, shape_binding)

node_pairs形状699×2，midpoint_pairs形状698×2，各行是新shape的实际$[h,h']$，均为既有有限Decimal词。这里的导数坐标必须与原scalar表第二列一致，不能把公共u导数直接塞进物理坐标列。

shape_binding须明确：

- kind为independent-sampled-scalar-shape；
- coefficient_is_an_original_nine_parameter为false；
- source给真实独立shape定义源的name/bytes/SHA；
- definition给family_schema、formula、support、zero_jet_proof_reference；
- coordinate_contract给原导数坐标声明及固定node/mid网格canonical SHA。

新source不能冒原0865族或原149模型。这个接口不证明所给样本之间的函数C²，也不由网格样本证明端点零jet；定义源和相应解析证明另负此责。若采用$bP$，应按R351明确$b,b',b''$支持端点为零、$P$所用坐标及全部链式导数。任意实际新shape系数在新族中是额外参数，不写入旧九p。

shape的ratio动作调用原Jet除法形成
$\delta q=(a h'-a'h)/a^2$
对应的同一实表达变分，不把代数等价改写冒成相同Decimal词。每个q的primal重形成与原ratio词差均保留。

先将这个实际$\delta q$与三个伴随权重收缩，再独立通过**同一批已形成A/C的局部线性系统**前传七状态，最后形成完整112响应及三响应。两种动作的实际差异只是浮点读回，不能称严格误差界。这里没有重新调用原非线性模型或原全9-J；完整112动作是这个固定有限模型的形成线性化，不是新的current native/fullDN结果。

每个结果保：

- 新shape完整source/样本/ratio动作身份；
- 三伴随响应、同系数前传三响应及实际差；
- 完整112前传响应与其身份；
- 末七状态动作、直接$q_N$及其三项贡献、固定start零动作；
- 原三残差和原full3 merit；
- 原full3 merit沿新shape的两种形成斜率；
- 原binary64字面$c_A$提升值；
- no trial/acceptance、无符号/rank/interval证明等真实限制。

如果shape支持严格远离末端且其零jet已证明，则实际$q_N$变化应按该shape读回；helper仍保直接项，不预设其为零，也不因此删传播来的末状态项。

## 6. 原九列对照不重做科学调用

调用：

    old = adj.original_nine_response(
        already_computed_reference=actual_existing_response_report,
        reference_literal_binding_sha256=actual_same_model_binding_sha)

不传reference时也可形成原九列，但不冒独立原forward比较。原九样本直接来自actual_model.controls/controls_mid的完整对应列；不是选择新的多项式族。

若传reference，必须是当次同一literal model和同九参数点的实际旧response报告，保原9×9identity seed、9列计数及完整3×9响应。完整parameter词、model binding与seed原词核对；helper不会为得到它另调model.response/FD。已有report的112响应通常仅存SHA，输出明确“旧112响应词未随report提供”，不能据SHA补造完整矩阵对照。

九列结果保完整3×9伴随矩阵、112×9同系数前传动作、各列来源及与实际已有原3×9 forward的逐项形成差。任意差值都不能自动表明新方法更准或旧方法错误；局部形成、反传、收缩、全链forward有不同舍入路径。

## 7. 证明与有限误差边界

R351对准确实数的固定字面模型证明完整伴随恒等式；对任意已形成局部系数，把这些系数当准确实数时，同系数正反传仍满足代数恒等式。实际本源运行中的Decimal50局部Jet、反传乘加和shape收缩各有舍入，实际原state亦不是准确实数轨迹。三层对象必须分开。

本源不提供区间系数包围、primal轨迹误差、最小奇值误差或真实斜率符号证明。它不求rank或通过阈值截列，也不能用旧FD整列relative error代替弱方向误差界。新增shape函数独立不推出3行响应补秩；实际新响应必须读回，必要准确结论还需明确有效误差责任。

若新方向形成斜率为负，真实后继仍须使用新明确族的完整三残差/112端口/域评价和原$c_A$ Armijo。$c_A$是原字面binary64 0.2，即$3602879701896397/18014398509481984$，不能换成准确1/5。helper不执行任何线搜或改变预算，不把linear prediction当接受。

## 8. 后继可直接接入的最小工作

独立producer在Actions中从已明确原参数来源建立真实原literal model及state，获得原完整9-forward报告（若本批原流程已付则复用），然后执行build和原九对照。它再用自己来源明确的C²零jet形状表形成新增三响应及完整112响应。到这一步仍只是requestless候选方向消费，没有新nonlinear family的真实接受。

下一实际新族producer须把原九参数与额外系数分开，明确原mesh/表/末端固定范围和新shape定义，完整执行真实域、全三目标、严格下降、原Armijo及全部原终门；真正native未来另付。本源不预选shape阶数/支持/系数、actual157以后未知父点或future run。

交付只做原源码逐式阅读、实际字段接口与纯文本/字节检查；终端不可用时未声称本地AST、import、数值fixture或科学运行通过。没有改动已有科学源、工作流、Git ref或发布权限。
