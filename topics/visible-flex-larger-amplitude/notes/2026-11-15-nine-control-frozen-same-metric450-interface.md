# 九系数全部冻结的同一标量重构与完整450维入口

作者：OpenAI ChatGPT / exact_refinement  
日期：2026-11-15  
分类：独立完整源码接口；未执行科学计算，未选择未来接受场、系数、λ或运行。

本交付实现的是将实际九控制完整设计场的全部九个最终标量系数冻结，再按原物理 DN 方程进行同一标量的网格细化。它不把旧v3/v4改名，不把九控制搜索点当作接受场，不把父场或父native的成功继承为新解。当前没有450维实际数值结果。

## 1. 完整来源与冻结文件

基线为公开提交 f18f47408f097b6d417cd2a77651ed9a76fc8beb：

| 原件 | 字节数 | 完整SHA256 | Git blob |
|---|---:|---|---|
| geometry_20261115_nine_control_full112.py |43641|00e4d2c3413cfa6c1df915b9d85050bf375ab88c04e8756149d4ea0533ef3bd8|ab8a983d21c90d1deaf1c17e80c2fd537a42482c|
| geometry_20261115_small_core_nine_control_family.py |44390|086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629|1a4e146d15608bed5097a7a0891f896687e45c66|

两个新源的目标目录均为本课题 computations：

| 新源 | 字节数 | 完整SHA256 | Git blob |
|---|---:|---|---|
| geometry_20261115_nine_control_same_metric_profile.py |22140|070b9b35c3d31c5073cd7da5b7afbdaa1150a38a94861c70eea60a39f0c85647|e8293e7e253f06cdbbf97b7f27642c4403706a7f|
| geometry_20261115_nine_control_same_metric_full112.py |40951|1610d6fb4b8bbc953585b91d86e235a524ec25551de0df3c633552312cdab00d|9cd1a2bc9011b529d35d7f64298a7db059808375|

原00e4、0865和124源都不改。两新源各自小于100KB；这里只创建普通UTF-8 blob，没有创建tree、commit、ref或调度。入口由真实00e4文本的12项唯一替换形成，并已作逐字重放相等检查；重构helper是独立完整新源。

入口直接PINS为23项：原00e4的21项，加原00e4入口自身与新重构helper。完整实际运行闭包还合并原core.FROZEN_SOURCES、family.checked_sources及新入口自身，逐文件核SHA并完整写入输出，不把23误说成所有间接源码的总数。具体基线说明见[九控制三active完整场接口](2026-11-15-nine-control-three-active-nonzero112-interface.md)。

## 2. 同一标量究竟冻结什么

参数顺序严格保持：

~~~
[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]
~~~

对原三个支撑，以实际保存的左端点和宽度定义

$$
x_i=\frac{s-\ell_i}{w_i},\qquad t_i=2x_i-1,\qquad
b_i=w_i^2\,64x_i^3(1-x_i)^3.
$$

区间外保原零延拓。全部九系数冻结后的声明实表达式为

$$
a(s)=a_0(s)+\sum_{i=1}^3p_i b_i(s)
+\sum_{i=1}^3\theta_i b_i(s)t_i
+\sum_{i=1}^3\eta_i b_i(s)t_i^2.
$$

这里保留三个even、三个odd和三个未经中心化的quadratic。完整原base geometry、port、peak curvature、所有支撑的left/right、实际stored width、全部九系数及原源SHA都进入冻结身份。新的left+width与原保存right不被自行重新等同或重排；原x的端点判断、width的计算来源与独立返回的a/ap/app沿原源码。

“same-g”指这个实际九设计场最终标量对应的 $ds^2+a(s)^2\,d\theta_{\rm material}^2$。它不是原accepted96输入的g，也不是候选搜索前的旧三参数g。原accepted96仍只供应真实的原base构造和物理law。

canonical_scalar_identity_sha256绑定完整原九scalar specification、九个binary64词、全部九支撑的left/right/width词及两个有限求值路径。它不随正在求解的112个core系数或下一次parent文件SHA改变。新的父文件来源独立保存，不混进“标量改变”的判据。

## 3. 两个有限求和路径必须分别保留

00e4的ThreeActiveView先形成固定六形状的base，再加入原三even控制。0865搜索profile先加入even，再加入形状。虽然声明实表达式相同，两种binary64结合顺序不能互相冒充。

本实现明确保留00e4的两个实际路径：

| 使用处 | 新实现 |
|---|---|
| 点profile、原q.profile、最终统计及物理cut | 直接调用原00e4的ThreeActiveView.profile(s,固定p1/p2/p3) |
| 原批量Frenet RHS、node/mid/RMS、完整state Jacobian | 调用原AugmentedFlow.scalar_jets，给定当前x和真实冻结p的完整逐节点repeat矩阵 |

固定base仍按theta2、theta1、theta3，再eta1、eta2、eta3加入；原系数为零时跳过该加法的分支保持。点路径的control_jets @ p与批路径的einsum均保原表达式，没有自行展开成另一条循环。

新FrozenNineFlow继承原AugmentedFlow，只覆盖scalar_jets的接线。其私有原three-active对象只用于生成scalar jets，不调用其453维RHS、J、边界或求解器。真正未知数始终只有450维。原physical、完整physical-state complex-step Jacobian、point_rhs、point_jacobian和常数core行仍由原类执行。

此处没有再经过一个k=0的空einsum或额外加零，从而避免以“冻结”名义另改有限求值路径。仍不声称不同BLAS、批量布局、平台或浮点运行环境一定逐字一致；实际新RHS是本次重新计算的原式结果。所有源和系数身份都会实际记录。

## 4. 完整重构，不把旧schema改标签

新标量schema：

~~~
frozen-nine-control-complete-same-metric-scalar-v1
~~~

重构步骤如下：

1. 读取完整原九scalar specification，核parameter_order、全部九值、field/tail112以及0865源身份。
2. 其中original_three_parameter_specification本来就是真实旧三控制base定义。调用它自己的原reconstruct_profile来恢复原base和三个支撑，不把新九族作为v3输入。
3. 用原0865 NineControlProfile附加真实odd和quadratic。
4. 用原family.scalar_spec完整重写一遍九spec并与原输入canonical bytes比较；这同时核所有参数、支撑、存储宽度、port及完整原source闭包。
5. 再调用原00e4 active_profile建立原three-active有限求值对象，固定它的全部p与六shape，向外提供真正parameter_count=0的profile。
6. 保存新冻结schema、原完整九spec、全九词、全支撑词、两个有限路径、原设计接受场receipt，以及当前重构源SHA。

serialize在后续求解每次检查真实空active向量，并返回原冻结九spec。它绝不把空active向量写成空frozen_design_parameters。嵌套原九spec中fixed_core_targets_count=3是原设计来源事实；外层新冻结schema明确fixed_core_modes=0，实际边界也确实使用空target。

reconstruct_profile没有旧v3/v4后备分支。旧same_metric_profile及same_metric_saved_prefix的dispatcher不被改写，新字段也不冒称已经由这些旧消费者处理。

## 5. 允许的父场与接受范围

首次冻结只接受实际00e4输出的完整actual文件，显式绑定全文件SHA和字节数。必须具有：

- 正确nine-control-three-active-nonzero112-complete-physical-DN-v1 schema、原00e4源及完整原PINS闭包。
- M112/N2048、原完整field_representation、全部九scalar spec及其fixed_scalar_profile副本的一致性。
- 原success=true、status=0、actual_tail.final_response_sha256，以及原collocation RMS≤1e−6、BC≤1e−11、frozen-physical RMS≤1e−6的真实已报告值。
- 全mesh、完整physical338 states/rhs、完整453 augmented_states/augmented_rhs、core112。
- 原最终三个active p与完整九spec的前三项一致，六shape与原binding一致；不能使用初始recipe替代末值。
- 实际原physical_test_final_cut_audit，包含原orientation与两套有限角网格身份。

其后可继续本新入口自己真实接受的450维actual；完整源闭包、冻结标量及空active身份都核回。prepared、pending、失败native、单独搜索status或仅九参数recipe均不是这个same-g入口的接受父场。

这些父条件是原接受身份的读取合同，不是给新科学另加低三根或高模证明门。父尾部大payload没有在此重新执行或当作新native缓存；这里只读取实际parent文件内的完整final-tail receipt。新当前H、完整J、原FD、原完整DN及final audit都要在本次实际重新付。

目前没有选择或制造任何满足这份合同的未来父场。raw可在同一次未来Actions中由前一个真实阶段生成并传给下一阶段；第15条不允许为了方便续接而把可重算raw再放进repo、Release或artifact。

## 6. 从453到450的真实状态与方形边界

全九冻结后：

$$
M=T=112,\quad K=k=0,\quad n=3M+2=338,\quad n+M+k=450.
$$

| 部分 | 行数/未知数 | 责任 |
|---|---:|---|
| 全物理r/t/z，包括mean z |338|原完整Frenet方程 |
| 全core常数状态 |112|所有core都自由，不只高109 |
| active标量状态 |0|九系数在scalar对象内冻结 |
| 左端原物理条件 |226|r0=1、112个切向关系、113个完整z入口值 |
| 左端core识别 |112|原constant core与真实入口r非均值系数相等 |
| 左端总数 |338|没有三条固定低core目标 |
| 右端 |112|原完整physical-phi DN条件 |

原PhysicalTestBoundary、FullDNBoundary及SeparatedBoundary已明确支持空target。入口在原core.main的旧coefficients[:3]调用处先核真实accepted96来源，再明确改传空向量；不是继续保留三条目标却仅把维数标签改成450。

首次输入保留原parent augmented_states的前450个词，即全部physical338和core112，不清零、投影或重新拟合core。只删最后三个active状态列，并将其实际最终值连同原六shape全部冻结。父场可能有很小的node参数漂移：那不再作为空间变化的g继承。所有保留父节点上的原physical/core状态词仍保留；RHS按末九系数重新评价。

新同g求解没有lambda_target，也没有新低core幅度目标。recipe出现lambda_target、initial_nine_parameters、target_core或fixed_low_core_targets会被拒绝，防止另一个设计问题悄然混入。旧三目标只作为accepted96调用来源记录，不参与新边界。

## 7. 真实细网格和资源上限

新入口明确采取一次父网格二分并加入全部原scalar.knots：

$$
X_{\rm initial}=X_{\rm parent}\cup
\left\{\frac{x_i+x_{i+1}}2\right\}\cup X_{\rm scalar\ knots}.
$$

只做完全相同数值节点的去重，保所有原父节点和原literal knot。通常699节点对应1397个父节点加中点，再加此前没有的scalar knots；真正数量从实际输入算出并记录，不预造固定节点总数。

--max-nodes是必需参数，没有1200默认值。先写refinement-mesh-plan.json，明确parent_nodes、midpoint数、原knot数、实际初网格节点数和给定预算。如果预算容不下初网格，返回resource-budget-insufficient-for-refined-mesh；不冒作native数学失败或不存在性。

随后在所有原parent节点按冻结九scalar重新计算原RHS，构造原CubicHermiteSpline，并由原curve_with_exact_nodes保已保存节点状态。新点只从这个明确初猜插值。原完整node/midpoint与两Lobatto RMS-domain预检继续，不能通过改tol或跳过节点让细网格进入。

原core.main的warm合并和原preflight均保原函数。其merge_mesh保primary节点，后续细化若超给定max_nodes或原域失败，仍如实报告。资源上限并不承诺BVP会收敛。

## 8. 当前H、原FD、完整求解及最终审计

初猜/预检完成后，直接通过原true_height读取全部112维当前H，用显式给定源码SHA的真实client完成solve(H,jacobian=True,audit=False)。只有该H的真实完整响应能作为原FD的affine anchor。

原physical boundary FD保三处非零扰动、原中心差分级与两个Richardson级、收缩条件和5e−5阈值。原make_directions按真实k=0生成全部7个物理/core方向及对应7个augmented方向；不存在的三active方向没有伪造成零列测试。完整112个native J列和右行仍在真实boundary链内。

FD通过后，同一live owner交给原complete-band/full-DN main。原17档inner回溯、1e−6 collocation/frozen-physical RMS、1e−11 BC、真实当前H尾部更新及最终jacobian=true/audit=true都保留。没有增加线性残差、rank、低三1e−8或高109非共振的额外求解门。

原core.main及banded.main函数体没有改写。独立设置层替换profile、K0边界、450维flow标量接线、真实初猜、新serializer和输出身份；所有替换在finally恢复。SharedNativeClient及其一次关闭责任为原00e4完整字节。

此入口没有把124的H(s)算法默默并入，也没有选择一种未来client。若显式client当前H未解、协议错误、FD失败、原inner/fullDN失败或final audit失败，仍保原失败。使用另一真实client时必须提供其实际源码SHA及完整运行环境，不能用这个适配器代替尚未形成的完整J/audit。

## 9. 真正消费的输入和CLI

当前直接消费原accepted96、原T112配置、实际完整parent以及新recipe。重构所需base、port、支撑和九spec全在真实parent内，故不重复加载未使用的旧prepared699或零H anchor。它们的原SHA在祖先原四输入映射中保留，不冒成本次已读payload。

| 当前原输入 | SHA256 |
|---|---|
| accepted96，2614352字节 |b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff|
| T112配置，2161字节 |01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5|
| complete parent |调用者提供真正未来完整文件及其实际SHA；本稿没有值 |

原accepted96历史路径为notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz；原配置为notes/public-actions-43588155190-1-prepare112/T112-config.json。需要时可从原已知历史8bd267107cc8710d371f3b62c02986655ac965b0恢复到runner临时目录。原78个native source及两ready由真正选定client的原接口恢复；本源没有传输函数。

新recipe schema为explicit-nine-control-frozen-same-metric450-recipe-v1，必需字段：

| 字段 | 精确合同 |
|---|---|
| parameter_order |原九名次序 |
| active_parameter_indices |空列表 |
| frozen_parameter_indices |[0,1,2,3,4,5,6,7,8] |
| field_modes / field_angular_quadrature |112 / 2048 |
| initial_guess_kind |complete-accepted-parent-physical338-core112 |
| mesh_refinement |all-parent-nodes-plus-one-bisection-and-all-scalar-knots |
| parent_sha256 |真正完整输入文件SHA256 |
| source_input_sha256 |仅accepted、tail_config两项及上表真实SHA |

不提供带虚构未来参数或accepted SHA的recipe样例。调用合同：

~~~sh
python computations/geometry_20261115_nine_control_same_metric_full112.py \
  --recipe "$ACTUAL_REFINEMENT_RECIPE" \
  --expected-recipe-sha256 "$ACTUAL_RECIPE_SHA" \
  --parent "$ACTUAL_COMPLETE_PARENT" \
  --accepted "$ORIGINAL_ACCEPTED96" \
  --tail-config "$ORIGINAL_T112_CONFIG" \
  --tail-client "$ACTUAL_NATIVE_CLIENT_SOURCE" \
  --expected-tail-client-sha256 "$ACTUAL_NATIVE_CLIENT_SOURCE_SHA" \
  --tail-source-root "$ACTUAL_NATIVE_SOURCE_ROOT" \
  --out "$RUNNER_TEMP/frozen-nine450-output" \
  --work "$RUNNER_TEMP/frozen-nine450-factors" \
  --max-nodes "$EXPLICIT_ACTUAL_NODE_BUDGET" \
  --jac-workers 2 --material-angles 4096 --physical-angles 4096 \
  --node-heap 1536 --outer-iterations 8
~~~

out/work必须是RUNNER_TEMP内互不包含的新目录。实际parent的两套角网格与orientation会核回。prepare-only可只完成冻结、真实网格、原RHS与原预检；即使退出0仍success=false，并明确native_called=false。

## 10. 输出和后续重构接口

完整输出schema：

~~~
nine-control-all-frozen-same-metric450-complete-physical-DN-v1
~~~

初次准备阶段保存frozen-nine-scalar.json、parent-source-binding.json、refinement-mesh-plan.json及原RMS预检记录。身份检查完成即先保存冻结scalar和parent binding，因此后续资源/域失败也有真实来源。

full-DN/actual.json.gz只有原求解器真正通过完整门才存在成功身份，保完整physical338、core112、RHS、450 augmented arrays、空scalar_parameters、九frozen_design_parameters、原全部真实尾部与cut审计。fixed_modes和active_scalar_parameters都是真0；left/right是真338/112。

原空parameter drift的finite_max可能报告null。它只表示没有active状态列，不能当作九系数缺失或偷偷补一个“实测0”。新输出另明确empty_active_drift_is_not_a_missing_scalar_coefficient，并完整保sampled_geometry_frozen_nine_parameters。

same_metric_refinement=true只指这个新冻结九标量；original_metric_identity明确区分原accepted96祖先。新的actual完整src/binding可以被本入口再次读取，canonical scalar identity不改变。旧v4 SavedPrefix、closed loader和后续装配dispatcher还需要独立真实schema适配；本交付没有把它们改标签或声称已连接完成。

## 11. 保留的数学与数值边界

全部112 core自由并不证明相应高核可逆；原R277在其他参数的高109有限结果不能跨到这个未知未来父场。低三或九设计搜索的目标值也不替代完整native、全场FD、原BC/RMS。

冻结同一标量不自动证明原有限Gauss返回a的连续导数恰等于独立ap/app、不付连续域包围、不付全局C²节点、无限角误差、seam、reach或全时flex。新helper明确continuous_scalar_domain_or_C2_certificate_created=false。原九系数声明式仍完整可追，未来同一字段的严格消费者必须消费这个真实新身份。

这里没有额外进行全域Arb扫描或RHS对照试验；完整原物理查询域与所有原接受责任都由真正运行保留。若科学失败，不能因维数方形、继承原源或same-g标签宣称已找到新解。

## 12. 本次静态范围

两个基线原件从明确f18提交读取，其字节数、SHA256及Git blob逐项核对。新入口12项old/new唯一替换可以从该原件重放至完整1610d6fb源码。sha、require_actions、temporary_paths、curve_with_exact_nodes、bound_original_preflight、SharedNativeClient、restore_attributes七个完整区段逐字相同。

环境当前unavailable；本次只进行原源码读取、纯文本替换、字节SHA/Git blob计算及普通小文本blob保存。没有声称执行Python AST、compile、import、模型、数值fixture或任何科学门，也没有新workflow/request号或调度。

精确替换清单和源文本检查回执是可从源重得的临时审读材料；不要求把这些重复材料入main。正式持久内容仅两源码与本接口。未来只保存脚本、实际参数/来源、run、输出SHA及紧凑结论，所有可重算raw留runner临时，不上传repo、Release或artifact。
