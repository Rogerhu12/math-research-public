# R310 九控制直接方向响应：最小调用与后继接线接口

**日期：2026-11-15。作者：ChatGPT / amplitude（AI）。**

完整条件证明见 [R310](../results/R310-complete-nine-directional-response-basis-and-finite-error.md)。本接口对应一个独立 callable helper，不是请求文件，也不是已经运行的独立算法。它不修改 request138，不选未来参数、父状态、run 或 trust radius；没有本地数值 fixture。

## 1. 冻结源码及原责任

拟发布路径：computations/geometry_20261115_nine_control_directional_complex_response.py。

- 新 helper：20172 B；SHA256 50044473f14b34c9451360debaa1ec9189f0a7924957098cafc37df3f849643f。
- schema：nine-control-complete-directional-complex-response-model-v1。
- 原 family：geometry_20261115_small_core_nine_control_family.py，SHA256 086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629。
- 原 direction/curve 数值基线：geometry_20261115_small_core_nine_control_curved_recipe.py，SHA256 824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf。
- 后续若保留 R299 selector，仍须原样绑定其 helper d4c9cd448b81e3c506984a273cb0e050cf806ebc109ad4d2b140cec9fa8d2cbf，不能借此重标当前138 source。

checked_sources(directory=None) 只核原两件及自身原字节，返回 source SHA 映射。它不验证传入 model 的构造身份；独立 producer 必须把真实当前 model 与原输入、九参数族、trace、父元数据和全部实际 source 闭包绑定。helper 没有未来 parent 常量，也没有可把不相关 model 认成原 family 的 schema 捷径。

所有科学调用入口要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public。源码只导入标准库；np、qr、solve_triangular 由原 producer 的固定运行时传入，不另装一套科学库。无 CLI，不能把它当 standalone fixture 或审批步骤运行。

## 2. 作用点：换形成路径，不改原方程

原 family 没有被复制、变换或 monkey patch。每一次新响应都走传入 model.evaluate；若 model 已由原 observed_model_class 包装，原 real/complex evaluation ledger 和原异常记录仍会捕获它。可选 trace.context(label) 只增加实际调用上下文。

原完整方程仍是原三残差，原 full112 尾输入、scalar/circle/传递公式不变。原 jacobian 仍可形成并保存九个轴列作为 pilot 和原 description/FD 的责任。新 helper 不把它覆盖成另一数组，也不把新响应冒称原 jacobian 返回值。

完整 QR 基底取自原 pilot 的相对参数缩放和三行平衡，只用于选择九个探测方向；不把非线性三个残差重加权。完整九列都重新调用原 evaluate。仅旋转旧 pilot 没有此作用，R310 已证明这个区别。

## 3. 单个真实方向动作

调用：

    action, report = directional_action(
        np, model, parameters, direction,
        trace=trace, label="outer-model/direct-actual-direction")

parameters、direction 是完整九维实向量；caller 已对真实实基点评价原域。该函数形成原步长 h=1e-25 的复参数 p+i*h*d，调用一次原 evaluate，取原 equation 的虚部除以 h。

返回 action 长度3。report 保留原 p/d、实际复种子实部和虚部、原复 equation、实际动作、步长和原 evaluate 调用数。真实零方向直接返回零动作并明确该例没有域证明或 evaluate 调用。非零方向分量形成零虚种子的位置只记录，不增加一个隐藏阈值门。

它不归一化 d，不扩大 h，不做 real FD，不求新的实候选，也不改 merit。有限溢出、非有限方程或不能形成真实方向仍是实际异常；调用者沿原 producer 的异常路径保存它。

## 4. 完整九列重新形成

调用：

    response = complete_basis_response(
        np, qr, model, parameters, pilot_jacobian,
        trace=trace, label="outer-model/complete-basis")

pilot_jacobian 为原真实当前3×9轴响应。S=max(1,abs(p))，原 pilot 缩放矩阵 A=pilot*S。对行平衡 A 的转置做完整带列主元 QR，Q 是9×9，R 是9×3，主元表示三行顺序。零 pilot 行的 basis-only 平衡因子用1；不以 R 的对角作秩阈值，也不删除任何 Q 列。

实际物理基底 V=S*Q，原相对参数度量矩阵 G=V/S。逐列实际评价原 F(p+i*h*V[:,j])，得到完整 K（3×9）。response 含参数、S、pilot、A、Q、V、G、K 和全部9个 probe 记录。

原 pilot@V、重新形成 K 与该乘积的差、QᵀQ-I 都只是读回，不是新 gate。G 的有限形成和实际 direction/S 也不冒精确恒等；证明只在其明示实数模型条件下成立。

## 5. 完整原度量的正阻尼模型求解

调用：

    direction, formed_action, solve_report = solve_complete_metric_model(
        np, qr, solve_triangular, residual, radius, response)

residual 是当前真实三项 equation，radius 是实际原 relative radius。使用完整12×9增广系统 [K; mu*G]，完整列主元 QR 和九维三角回代，不解 normal equations，不以奇异值 cutoff 删除弱列。

保留原 positive floor 形式：机器 epsilon×max(1,原 pilot 的 A Frobenius读回)。64 次正阻尼 bracket 和64次几何细化保留原形式。实际半径来自形成后的 d=V*w、d/S，绝不因 Q 来自有限 QR 便默认||w||等于原 relative norm。

solve_report 保存全部小模型、正阻尼搜索和所选 index、完整 Q/R/permutation、w/d/d/S、K*w、G*w、两种 relative 形成值的差以及 stationarity 读回。实际完整求解失败、非有限方向或有限 bracket 找不到可用方向如实返回异常；没有额外“condition number合格”门。

R310 的严格等价只适用于 K=JV、G=S⁻¹V 的精确算术。实际 K 由复探测形成，是新近似模型。即使完整列主元 QR 成功，也不证明原弱方向或新的真实非线性步精确。

## 6. 可直接用于新 producer 的完整 predictor

调用：

    direction, direct_action, direction_report = full3_trust_direction(
        np, qr, solve_triangular,
        current_parameters, current_equation, current_pilot_J, current_radius,
        model=model, trace=trace, label="outer-direction-000")

它先重新形成全部9个基响应，再完整求解该模型，最后沿实际形成的物理 direction 直接 complex-step 一次。返回的 direct_action 才是这个新接口声明供外层 slope/target 使用的动作。

direction_report 将三种对象分开：

1. 原 pilot 轴列与 direction 相乘的动作，仅作旧形成路径比较；
2. 新 K 与实际 w 的模型动作，仅作本次线性模型读回；
3. 原 evaluate 沿实际 direction 的直接动作，明确为本接口建议的外层动作。

它们的差只保存，不设置一致性阈值、不做隐藏回退或修正。非负/非有限 slope 的原停止责任仍在独立 producer 的原逻辑中。原完整三项 merit、.2 Armijo、所有真实域检查与全部候选失败仍由原 nonlinear trial 付清。

这不是可以不改身份便赋给旧824c或138的匿名函数替换。独立 producer 应有独立 source/schema，把新增 helper 加入 consumed_source 闭包；原 numerical helpers、实际八方向/20外档、12内方向/20内档以及所有 final 原责任继续保持。当前没有创建此 producer 或请求。

## 7. 法向响应与原曲线接线的精确限制

调用：

    full_response, report = normal_directional_response(
        np, model, actual_inner_parameters, physical_normal,
        trace=trace, label="normal-iteration-000")

physical_normal 为该外层曲线固定的9×2物理法向 P。两列分别调用原 evaluate，返回完整3×2响应；原两约束的投影是其最后两行。完整第一残差响应也保存，不能只保2×2而丢掉 full merit 责任。

若后续独立 R299 normal 变体调用它，应保留原 fresh3×9 J 及其 trace，改变的仅是 projected=J[1:]@P 这一响应形成路径，使用实际直接形成的两列。原 normal QR、缩放、内层 merit、步长序列、异常和同轨迹候选选择仍按原合同。额外两次 complex evaluate 要记入真实调用账；它们不是新的 real trial，也不删减原试探上限。

当前 helper 没有改 curve_frame。一个完整后继接线必须明确其 plane 仍来自哪个 pilot，以及原点导数读回使用哪一个动作。不能把新 direct_action 传进旧函数后，仍把它写为旧 J@direction。

最小诚实衔接是把原 frame 的基底选择与 pilot 读回明确标成 pilot-only，同时记录当前 direct_action 和直接形成的 CP；如要给新目标曲线的原点导数读回，使用 R310 的公式分别形成，不能以旧 origin_action 字段替代。这些是小模型读回，不是新增一致性门。当前源没有默默重写或执行这个后继 frame 变体。

内层目标误差不被设零。对有限 direct_action，近似 a_c 与真实 C*v 的差仍影响理想曲线的原点导数；未付的精确根/IFT条件不能用“小复步长”代替。R299 选实际已评价低merit点的定理依然成立，但它不保证内根或导数准确。

## 8. 真实成本、完整末端检查与输出

新完整 predictor 额外形成9列 response，加1次实际方向响应；零实际方向例的调用数以真实 report 为准。采用 normal helper 时，每个实际内方向额外2次复评价。原当前轴J本来就要形成；这里不把它称为已节省的计算。

所有这些都走原 family 的完整有限传递，尚无实测耗时。下一独立科学配置必须给足墙钟并按原 failure/partial语义报告，不可从原8×20/12×20试探预算中扣除这些形成工作，也不可因超时冒“数学失败”。

原初末完整九列FD、Arb scalar 域、453圆、full112/unit/final gates 沿原 source 执行，不由本 helper 代付。它不生成 accepted warm，不宣称 continuous ODE/BVP 解，不改 native/finalJ/audit门。

完整小矩阵和 probes 可放到原每方向分段科学日志，由新 reader 保留实际字段和全部失败。90KB 只是每段输出界限，不是删除试探或 normal 信息的理由；也不能把多个实际方向重标为一个平均记录。

## 9. 源码层验证与下一实际决策

本地只做 AST 解析与文件身份，未导入 numpy/scipy、未调用任何方程、复探测、QR、FD或Arb。helper 当前不是实验结果；没有为之创建独立 fixture、测试门、未来 run、真实父参数或工作流。

138 已冻结并独立运行其 full-merit selector。实际138结果应先判断同轨迹选择能否给出真实改进，再决定后继采用哪一部分响应重形成。若使用此 helper，须明确发布独立 producer 与来源；不能将当前138输出或原135响应重写成“直接 complex-step 已改善”。

换基等价证明解决的是保持完整九参数与原度量的责任；精度改善仍取决于真正原评价的内部有限误差。若新方向依然被内部传递或终端差值限制，本 helper 会保留这些实际结果，不能以新的模型标签掩盖。
