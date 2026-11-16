# R569 同次真实 cubic / 当前准确 quintic：完整来源与调用接口

**作者：geometry agent（AI），2026-11-16。**  
**范围：已证明的条件来源与有限包含组件；没有实际执行结果。**

## 1. 本次交付与状态

本次仅新增一个源库、完整证明与本接口。原675、R553、R521、原full-DN core、当前CP、metric和任何在跑任务均未改。

- 源：computations/geometry_20261116_same_call_cubic_quintic_defect.py
- 证明：results/R569-same-call-literal-cubic-accurate-quintic-and-complete-defect.md
- 本接口：notes/2026-11-16-same-call-literal-cubic-and-accurate-quintic-interface.md

源最终为 39272 B / 6d27df22093e339fe8940bf24c57cff880d247a5f7f4fd478135adf2e4032f66。完整manifest另给三个文件的字节/SHA/blob。R570/request239/R571仅预留，没有写成当前调用者或actualrun；不能把本库已刊误写成235/238已经返回这些诊断。

本库没有独立CLI、工作流或owned process。数值函数仅允许在Rogerhu12/math-research-public公开Actions内执行。源文本形成、哈希和原源码阅读不包含科学执行、import/AST/compile或fixture。

## 2. 为什么不能只从当前CP重建原cubic

原full-DN结果有mesh、physical states/RHS、augmented states/RHS；当前675还有真实DDY并形成准确Q。它们没有原sol.sol.c。

重新拟合准确三次C*可以给Q−C*，但不能代替原三次C_lit。physical RHS与augmented RHS原本不要求相等；PPoly形成时还有真实舍入，准确右端点/一阶连接也不能凭名称假定。

新增capture必须在真实原solve_bvp返回对象还活着时复制它的全c/x/y/yp，不额外求解。没有这个同次原对象或完整捕获文件，比较只记unpaid，不从历史词、source SHA或RMS补场。

## 3. 实际依赖

| 依赖 | 精确SHA256 | 使用 |
|---|---|---|
| geometry_20261116_actual_prefix_coefficient_tube_majorants.py | 81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b | 准确Bernstein、完整角d/e、实际module绑定 |
| geometry_20261116_finite_frenet_tube_residual_majorants.py | 4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad | 通过原R553 loader加载，原四块公式不复制 |
| geometry_20261115_shared_active_interval_balls.py | 675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b | 当前真实prefix_coefficients defining method |
| geometry_20261114_full_dn_solve.py | c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162 | 真正core.solve_bvp调用者 |
| 实际SciPy callable文件 | 运行时记录完整file/bytes/SHA | 真实原求解对象来源；不把纸面v1.17.0名称当运行回执 |
| 当前checkpoint/driver/field/source closure | 实际已加载对象和完整原文件身份 | 不造新的CP，不降任何原finite接受门 |

新库和R553/R521应在真实computations同目录；原R553 actual_module按方法真正__func__.__module__找675，不选择sys.modules中第一个同路径对象。当前R416及其真实来源派生若仍继承这个675方法，可以由实际对象绑定；仅文件名相似不能通过。

原core可以来自实际恢复的source_topic路径，必须确是原basename及c6a完整SHA。当前driver的字节身份独立记录，并在稍后与真正checkpoint的actual_driver_source比较。

## 4. 透明同次capture API

构造函数：

~~~python
SameCallCubicCapture(
    core,
    actual_driver_source=...,
    field_modes=...,
    physical_size=...,
    augmented_size=...,
    budget_check=...,
    actual_clock_receipt=...
)
~~~

输入职责：

- core是本次实际原full-DN module对象，不是重新import出的另一个没有参与求解的副本。
- physical_size必须等于3*M+2；augmented_size必须是本次真实flow.dimension，不固定为450，也不删原core或scalar行。
- actual_driver_source是本次真实新caller文件，未来必须进入完整runtime source closure。
- budget_check是原owner的同一回调；本库不创建起点或加时间。
- actual_clock_receipt是原同job实际文件的file/bytes/SHA；库读完整文件核身份，但不独立解释所有旧owner deadline schema。注册caller仍须证明它是本次真正绝对钟。

上下文进入时，只把这个core.solve_bvp属性指向透明wrapper；wrapper调用所保存的原函数一次，返回原对象。上下文退出仅在该属性仍是本wrapper时恢复，不覆写别人的并行改动。不能把这种显式运行组合描述成“原source closure未增加”；未来caller必须登记本库。

每次solve开始先清空旧snapshot。原solver抛出的异常不被捕获或改名。返回后只做完整字复制；普通capture错误记录last_error后仍返回原answer。原预算、MemoryError等资源异常不被归为数学未付。

新库当前没有被任何冻结driver自动安装。下面只是未来caller所需的接点说明，不是现有入口函数名：

~~~python
capture = SameCallCubicCapture(actual_core, ...)
with capture:
    original_return_code = run_the_unchanged_original_main()
# 原BVP/FD/fullDN/final/audit照常；成功与否仍由原完整结果决定。
capture_record, capture_receipt = capture.write_for_accepted_result(
    original_result=the_actual_original_fullDN_file,
    out=fresh_owned_temporary_capture_directory)
~~~

若原主程序没有接受结果，调用者不得造一个success文件。它可保capture-unpaid或真正未启动记录；原BVP失败仍是原BVP失败，不被诊断重标。

## 5. 临时capture完整表示

capture结果schema：

~~~text
R569-same-call-literal-cubic-and-accurate-quintic-v1-capture
~~~

result.json保存实际run四键、source、actual original core/solver/driver/clock、call_count、最后调用ordinal、原fullDN身份、complete/error/capture_error及全部member身份。

每个member是原字的完整f64le文件，不压缩成摘要、不上传Git：

| member | 实际shape |
|---|---|
| mesh | [nodes] |
| augmented_states | [nodes, actual_augmented_dimension] |
| original_spline_rhs | [nodes, actual_augmented_dimension] |
| ppoly_coefficients | [4, intervals, actual_augmented_dimension] |
| original_rms_residuals | [intervals] |
| solver_parameters | [actual_parameter_count] |
| physical_states | [nodes, 3*M+2] |
| frozen_physical_rhs | [nodes, 3*M+2] |
| recomputed_augmented_rhs | [nodes, actual_augmented_dimension] |

PPoly.c的轴解释是descending_power、interval、全部augmented_columns；后续真实物理列取前3*M+2，但原全部其余列仍完整留存。

原array_record要求完整有限float64，转换为明确little-endian表示，保存shape/bytes/SHA。±0的原word保留；后续准确有理解释只把它们作为相同实数0，不混淆原字身份。

write_for_accepted_result仅当原结果source_sha256=c6a、success/status符合真实原结果，且捕获与原mesh/augmented_states逐字相同，才complete。它另外留完整physical RHS与fresh augmented RHS，并只报告它们同original_spline_rhs是否相同，不把相同当新BVP门。

out必须是RUNNER_TEMP下新目录，不能拥有原结果输入；文件用xb独占写。所有写入有完整identity。尚未绑定owned清理，不能只见complete result就删除原输入或capture。

## 6. 真正当前场绑定 API

~~~python
pair = bind_loaded_cubic_quintic(
    current,
    capture_result=...,
    capture_sha256=...,
    angular_count=...,
    sqrt_bits=...,
    budget_check=...)
binding = pair.describe()
~~~

current是已经由实际准确field loader接受的对象，必须真实提供current.field、current.Active；field.saved.checkpoint必须是本次真实CP。库不重新建准确C、不换root族、不改十词、材料或field节点。

主要绑定是：

1. capture schema/complete/error与本次run四键一致；
2. capture.source确为当前这份库的实际完整source；
3. capture.original_fullDN与current CP成员身份一致；
4. capture actual_driver_source与CP actual_driver_source一致；
5. CP的mesh、augmented、physical、physical_rhs四整数组与capture逐字一致；
6. 当前准确field的Y/DY就是上述physical数组；
7. 675实际coefficient方法来源全匹配；
8. M/列数/区间/全四幂完整，angular_count确等于实际saved.N。

这阻止把旧M的cubic、旧mesh的节点、另一个fullDN的state或原设计453对象拼进当前Q。没有重新执行BVP或为输入不匹配添加数值acceptance门：未来外层应将此诊断记unpaid，原metric仍按原真实field继续。

binding记录当前CP、target_identity、actual_current_driver、完整675表达身份和全部捕获member身份。它不根据target标签宣称新的same-g证明；跨层same-material仍按原真实合同。

## 7. 同一原闭单元的调用

~~~python
record = pair.cell(original_cell, actual_scalar_context)
~~~

original_cell原样携带piece_index/radial/angular/lower及所有rank/path字段。库不新分裂、不pop、不退休，不决定原metric是否通过。

必须是当前field.pieces中的prefix片，并且radial全闭区间位于该真实prefix_span内。非prefix记录具体unpaid，不能冒tail/collar/cap/Frenet已经付清。

actual_scalar_context必须来自同次已经求过的target return，schema：

~~~text
R553-actual-complete-prefix-coefficient-tube-majorants-v1-same-target-return
~~~

使用三个真实键：

~~~text
radius
accurate_arc_derivative
numeric_s_radial_metric
~~~

它们全部是准确闭区间。代码不再次调用target、不取区间中点；mu=sqrt(g11)、nu=accurate_arc_derivative*mu。必须保原numeric-s坐标，不能把public-u乘过Lnum²的metric混入。另从真实675.field.rho_lower读取原同core完整Phi′正下界；它已经是原field loader的条件，不新增solver门。物理角目标是diag(mu²,A²rho(phi)²)，不能把Phi′设为1。

## 8. cell输出与不同的“已付”

输出schema为：

~~~text
R569-same-call-literal-cubic-and-accurate-quintic-v1-cell
~~~

三个状态分别报告，不能压成一个原接受布尔：

- polynomial_comparison_available：真实Q/C全部系数及E0/E1/E2、所有列、完整比较线段盒已形成。
- geometric_gap_available：同target A/mu和原同core完整rho正下界及完整全角几何一阶差已形成；角项除以(A_-rho_-)²，不要求P正。
- whole_pair_tube_available：当前这个闭角单元内，两曲线及全部线段的joint P正且原R521调用已完成。

主要记录包括：

- 当前prefix span与原完整span、闭子区间和normalized区间；
- 实际C、Q、全差、准确C*、second-gap的完整数据身份；
- 每列E0/E1/E2、全列最大值与C/Q一二阶上界；
- Q−C*和C*−C_lit各自的真实界；
- 原literal cubic端点值/一阶与当前Y/DY的准确差；
- 完整两曲线segment coefficient box；
- 全物理角径向/角向导数分量界与relative derivative gap；
- 本次原target context、准确A/mu/nu闭盒；
- 本角单元全部d/e/W/P和R521原majorant；
- error、traceback、完整unpaid原因和原cell地址。

whole_pair_tube_available只表示这个原角单元，不能作为全N角点或全域完成。输出明确要求原全部角cover与完整N样点集合；需要跨叶聚合时沿原R553.8，不能把一个角盒的P下界直接作为整圈P下界。

所有普通算术/来源字段错误返回真实诊断未付；预算异常仍穿透原资源机制。已经形成的多项式差或几何差不会仅因P未隔正就被删除。

## 9. 条件 metric 组合函数

~~~python
conditional_metric_transfer(cubic_error_upper,
                            relative_derivative_gap_upper,
                            sqrt_bits)
~~~

它只实现：

$$
\epsilon_Q\le\epsilon_C+
2\sqrt{1+\epsilon_C}\,\delta+\delta^2.
$$

输入必须已是同一闭单元、同一准确target、同参数图下的严格上界。函数不建立这些上界的来源，原RMS不是cubic_error_upper。其delta必须用真实材料密度rho归一化；normalized-q的2pi因子只在分子/目标同时拉回时相消，rho不能省。原R553/R521的P仍是A²mu²W−nu²|d|⁶：真实Frenet alpha=−nu/(A*kappa)，不能把这次Gram归一化修正误写成P额外乘rho。该函数没有全域完成/accepted标志，未来caller不得凭一个任意数值把它写成证书。

源把全部Fraction输出编码为准确有理字；平方根用原R521有理向外端点。没有设置新的epsilon、gamma或原solver容差。

## 10. 原残差与FFT尚未被省掉

本次已把R521.quintic_residual_transfer所需的真实E0/E1和C/Q比较线段变成可得输入。仍没有实际生产原cubic的eta_C，不能把原collocation_rms_max填入。

至少还需同场真实sample残差、PPoly eval/derivative形成差、FFT/normalization/sqrt/projection/norm形成差、准确与nominal scalar差、全cell fill distance；需要原worker分支对应时也必须实际绑定。

即使完整有限系数ODE残差为0，还存在Pi_N V−V的非线性投影缺陷。完整有限模态不意味着除法/平方根后的速度仍带限。原R519/R459全角直接metric计算仍是其真实消费路径；本库没有新增更严格科学前门，也没有把该缺口写成已测平台。

## 11. 全闭域、材料和phase责任

本库只处理prefix。原tail E(r)、准确cut patch、collar、两帽及atlas仍由原完整field消费者执行。没有把literal cubic临时拼上原Q tail当合法比较闭面。

同次C/Q用同current core/材料/SE2/相位。共同可逆角换元同时拉回两个Gram和target后广义谱不变；共同刚转和反射保范数。全t结论仍要求实际整圈覆盖，不能只看端点t或把g自身宣称旋转对称。

跨level比较必须另用原R443/R447已证的正确材料共轭和真实first A/B receipts。库没有重选构造参数，没有为公开同g比较减弱任何原绑定。

## 12. 原钟、完整读回及未注册部分

budget_check来自原调用者，库不创建新deadline、reserve或owned child。capture复制与cell计算会花原钟；不保证原预算访问同样多cell或能完成。

未来R570要明确接下列真实位置，当前均没有假称已完成：

1. 新driver真实安装/移除capture，source closure含库；
2. 原accepted结果后写完整capture，CP字节保持原值；
3. 同job真实geometry loader后绑定capture/当前field；
4. 原DFS中只附加本cell诊断，原metric refine/retire不改；
5. 全部capture/cell ledger身份、失败和原frontier进入正常与recovery necessary；
6. 原owned quiet、单90000/超限70及全部清理条件不减。

本库不创建读回marker、不写GITHUB_OUTPUT、不删raw、不宣称90000B必够。当前全量temporary arrays要保到原已绑定必要范围完成；任何缺失或未知scope都不能被complete标签覆盖。

## 13. 交付结论

这是一个真正从同次原PPoly字到当前675准确场的有限比较内核；它补的是此前实际输入缺口及比较路径包含。完整原科学接受与最终metric仍保持原责任。

没有本地科学计算、原场重跑、测试fixture、AST/compile或新的request；不以源码生成代实际误差测量。完整证明见R569，源的最终字节与全部来源表由publication manifest绑定。
