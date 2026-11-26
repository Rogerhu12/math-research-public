# R713 准确 profile 三 moment 与同批次两角费用消费者：完整接口

2026-11-26。对应完整证明为 [R713](../results/R713-exact-smooth-triangle-moments-and-actual-fees.md)。这份独立下游只消费已经实际返回的 R711 新 profile batch；它不会启动 solver、重算当前 F/J、改变固定目标或成为首跑前门。当前尚无该下游的科学执行。

## 1. 完整来源与唯一前驱

完整源码：supported_smooth_triangle_seed_angular_jet_error_bounds.py，41994 B，SHA256：

82e6f1a714c241b1e445304017613cc0fab8874520ef7d6904acf3ae62904f76

完整纯再生器：derive_smooth_triangle_error_consumer.py，15931 B，SHA256：

62e5bd2c49b737ed8f0cd37685160838fd8fa516dae57095fbd41e685127949a

前驱是已刊 R710 完整 85e90f67a588f886f068532d76d678aa9fd8e24c1283f73e24d4f5e00ac172b9。没有修改它。新来源严格绑定：

| 角色 | 完整 SHA256 |
|---|---|
| R711 provider | 0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b |
| R711 mean kernel | f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917 |
| R711 complete driver | fd95d91abe9525cbfa34d55bd576be7dfba1fe25fcafb73bdaaea40e003ad65f |
| R711 pure reader | 3914004ac39b838c33411bd11660bb8fbec1372630c3569f3ea4ad5ae16c0f97 |

新输出 schema 为 complete-supported-smooth-triangle-seed-angular-and-node-error-bounds-v1；输入请求 schema 为 actual-supported-smooth-triangle-seed-accurate-fee-request-v1。原五段请求、旧报告、不同 profile/模型/批次不能冒充。

纯再生器用 --repo 指向完整 source checkout、--output 指向仓库外的完整新源文件。它只执行 stdlib 文本替换、准确前驱 SHA、AST 和 compile；不导入或执行科学代码。实际科学消费直接使用完整新源，不要求先运行再生器。

## 2. 已完成的纯源码核对

本次实际只做了两份源码的 AST、compile、py_compile、重复 literal key/keyword、尾空白检查。没有导入科学模块、没有执行有理矩、区间评价、均值、F/J、积分或任何科学 fixture。

与85e90相比，27个原 top-level函数/类的AST完全相同，包括全部有向区间、平方根、Machin π、sin/cos Taylor、向量与normalization两jet工具。改动的是：

- actual batch binder 的四个完整新源 pin 与 pure reader 路径；
- 新 profile/branch 的准确相对参数；
- 新三个准确 moment 包围和直接工作字差额；
- 新 $(0,\pi)$ 分支的导数地板与lambda盒范围；
- 中央节点用准确 t/长度求 h、h_s 的完整分片包围；
- 对应的新CLI、输出身份和费用范围。

原单快照绑定责任保持：先捕获report bytes/SHA，pure reader必须返回同SHA；完整raw批metadata与捕获快照相等；NPZ保存的全部真实数组与literal phi逐项读；数组和report在读后仍须同SHA。费用请求也只捕获一次bytes并由同bytes取SHA，不把两个快照拼成一个来源。

## 3. 新增准确 profile API

complete_profile_moment_enclosures(seed, lambda_word, bits=160, series_order=48)：

- seed必须是完整R711新模型及上述provider/kernel来源，12片与 $(0,\pi)$ 声明一致；
- lambda_word必须是实际有限canonical binary64 hex字符串；
- series_order是偶数 $L\ge2$。该参数改变评价算法，不改变profile或g；
- 一次准确有理矩递推至 $L+1$，返回A、A′、A″在同工作lambda处的三个完整盒；
- 输出含全部矩定义的canonical摘要、准确质量、共同余项矩、三个准确Taylor余项、真实lambda字和精度；
- 全部十二片都进入精确Fraction矩；多项式评价逐步dyadic向外。它不假定原192点规则或原trig计算准确。

消费者另外读取同实际batch的 profile_moment / profile_moment_first_derivative / profile_moment_second_derivative 三个工作字，逐个与准确盒取最大距离。这项差额支付原profile积分/width/trig/求和等全内部误差。输出明确 external_profile_moment_error_inputs_used=False；不读取某个外部零fee来代替它。

返回盒位于同一个工作lambda。准确根与两角jet的移动通过 R713 式(10)(11)单独支付，不能把这两个责任混同。

## 4. mean_jet_bounds 的完整输入与新结果

签名：

mean_jet_bounds(seed, working, fees, bits=160, taylor_order=48, profile_series_order=48)

原working九个三向量、lambda三jet及三个工作moment字全部保持。实际完整binder从已保存NPZ读取这些15项；没有另跑工作求积。

仍必须提供的外部准确输入如下；它们没有0默认：

| fees键 | 准确含义 |
|---|---|
| accurate_S_enclosure | 同固定符号域S的正区间 |
| K_norm_lower / K_norm_upper / K_vertical_lower | 同一准确K的完整界 |
| accurate_reference_unit_and_nonnegative_vertical_on_complete_boundary | 已付完整端层参考性质的明确声明 |
| accurate_centered_total_equation_residual_norms | 三个准确总方程零/一/二阶残差范数上界 |
| boundary_reference_phi_norm_upper / boundary_reference_phiphi_norm_upper | 全端层原参考两角导界 |
| accurate_fixed_chart_radial_jets.e / ep / epp | 同固定材料角径向架的三个准确向量盒 |
| fixed_chart_e_is_the_accurate_horizontal_unit_radial_vector | 该完整架性质的明确声明 |

这些外部对象的真实性不是本模块自动认证的。root存在条件、正性或包围不一致时会保留实际不完整输出并失败；不会解释成物理不存在。

旧 accurate_profile_moment_absolute_errors 不再需要也不用于计算。profile三moment已由本模块准确求出。旧epsilon、旧r/4平台条件及旧lambda<pi/2没有残留。

输出完整保留 R710 的 v/d/w/lambda三jet盒、各实际工作词差额、完整R709常数、准确radius范围、lambda三项移动费用。新增：

- complete_central_profile_moment_proof：三个准确盒与完整真实工作moment误差；
- central_profile_moment_errors_certified_by_this_module=True；
- accurate_S_interval 和各准确相对中央区间；
- profile_series_order；
- 新的全分支导数地板，不沿用旧平台系数。

与此同时 input_fees_certified_by_this_module=False 与 continuous_uniform_field_certificate=False 保留。它们指仍需外部提供的准确均值/参考输入及全域责任，并不抹去本模块已完成的profile积分费用。

## 5. 中央节点的准确 profile 评价

central_profile_enclosures(t, delta, physical_length) 接受准确 Interval 位置和正长度，逐一处理所有相交的十二片，返回完整 h、归一化导数和物理 h_s 的盒。S5/I5是准确多项式；反射符号、参数方向和真实物理长度都保留。

bound_reference_node(mean, node) 保持全部四向量 T/Tp/Tpp/Ts 与实际字的完整比较。中央节点改为提供：

- central_interval_index：准确的0或1；
- accurate_normalized_central_coordinate：同实际地址的准确 t 盒。

物理长度由mean中的准确S和同seed的中央相对端点构成。中央 h/h_s不再直接取外部任意盒。边层和外补集仍消费原R710的准确原参考四向量、chi/chi_s等完整输入。

same_field_node_binding仍必须匹配完整seed identity、providerSHA和原literal phi；address中的literal phi也必须相同。所有四个实际工作向量仍须提供。但准确t盒与cell/u物理地址、实际工作向量字自身的外部来源没有因字段相等就被自动证明，结果明确 external_node_address_to_coordinate_association_verified=False / external_node_values_and_accurate_input_enclosures_verified_by_this_module=False。该组件不能把尚未关联的任意坐标盒升级为节点证书。

## 6. 完整实际请求与CLI

新请求包含原完整 binding：report SHA、seed identity、actual raw batch SHA、fixed scalar identity、fixed chart core SHA；angles数组顺序必须与实际batch literal phi逐字一致。每一角有上述完整fees和可选请求nodes。external_fee_provenance必须保留外部费用来源与范围，不能用小打印残差充准确producer。

CLI保原 --repo / --report / --batch-index / --batch-arrays可选 / --fees / --output / --precision-bits / --taylor-order，另加 --profile-series-order，默认48。科学入口强制 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public；所有raw输出留runner仓库外。

本次没有构造带假fee数值的ready。真实R711batch和外部准确输入都存在后，才可填实际路径调用。源允许完整命令，但不会以虚构费用或旧batch预演“通过”。

每个角成功后自然写完整进度；缺项/不一致或某角包围失败保留已经完成的角及真实failure，不丢角、不补成功值。complete仅表示这个输入batch与所请求节点的条件算术完整返回。全连续角、外层normal链、六jet/Gram、全局几何与README最终标准均不由此自动完成。
