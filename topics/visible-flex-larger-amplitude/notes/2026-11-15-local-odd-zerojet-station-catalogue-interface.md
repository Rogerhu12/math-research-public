# 173：原七状态伴随上的局部奇形状站点目录接口

作者：OpenAI ChatGPT（amplitude 协作代理）。日期：2026-11-15。

本页对应独立源码 computations/geometry_20261115_literal_local_zerojet_station_catalogue.py，39740 B / SHA256 2d2d84eb1602b681d2f37b08a484c00f992c3d295ed45ad7624be678e2aba74a，Git blob155fa07c2b005b1ec894078c4018f5d7c78a0a98。它是 requestless helper，没有运行请求、父参数选择、实际候选、未来run或接受结果。全部算术方法均只能在本公开仓库的Actions中调用；导入本文件不执行科学计算。

其证明依据是[R351](../results/R351-literal-seven-state-adjoint-and-C2-control-response.md)、[R363](../results/R363-local-C2-shapes-and-complete-finite-sample-response-rank.md)和[R366](../results/R366-coincident-inputs-complete-value-and-slope-shape-response.md)。173只实现R363的奇七次函数。R366的值jet方向没有被偷偷加入本源码。[R370](../results/R370-disjoint-local-shape-box-descent-and-uniform-C2-bounds.md)的有限奇形状箱组合属于另一个独立producer的责任；下面明确的固定函数接口可供其使用。

## 1. 固定输入与真正消费范围

构造器为：

~~~python
catalogue = LocalZeroJetCatalogue(
    completed_adjoint,
    original_nine_profile,
    explicit_binding,
    event_sink=event_sink,
    deadline=absolute_monotonic_deadline,
)
catalogue.build()
~~~

它消费的不是一个只有数值类似的矩阵包，而是实际已完整完成的冻结R351对象与原九族profile：

| 输入源 | 精确固定 SHA256 |
|---|---|
| geometry_20261115_literal_seven_state_adjoint.py，35419 B | 12a95d40929cc7799761e56c33eadc9e5fbe16fa3eacf0d0be94c56ea3452b0f |
| geometry_20261115_small_core_nine_control_family.py | 086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629 |
| geometry_20261115_nine_control_decimal_literal_model.py | 2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75 |

构造器核实际class文件、source bytes/hash、R351 complete/failure、698个reverse cell、原九族source和parameter_count=9。它不接受把一个新十坐标state删掉最后一维后重标为原九点。以后若要从真正十族继续，需要另有显式支持该族的trace source/schema。

explicit_binding包含：

- producer_source：实际调用者文件的name/bytes/SHA；
- expected_adjoint_binding_sha256：当前R351完整binding的canonical_sha256；
- expected_literal_model_binding_sha256：该次实际原literal model的canonical binding；
- actual_parameter_words：当前实际九个Decimal字符串；
- expected_original_profile_description_sha256：当前原profile description的完整规范身份。

这些短身份全部逐字段核对，不能从父参数“看起来相同”替代实际当前对象。当前R351绑定本身也按原digest重新检查。这里只重做元数据编码，不重新执行primal或J。

原 formed_arrays 的 node_weights 为699×3，midpoint_weights为698×3；原state的 scalar_nodes/scalar_middle分别699×2、698×2，列名始终是$a,b$。另保留实际node/mid坐标、原ratio/ratio_mid、原全三方程、完整112右残差身份、R351完整输入及当前run/source身份。所有这些量来自已经形成的实际对象；helper不重新求全场、RHS、J或尾部。

这仍是有限字面模型的形成权。源码没有证明这些Decimal权等于准确实数导数，没有把原binary64表变成连续准确系数，也没有支付完整新g的非线性native责任。

## 2. 先计逻辑变量，再按准确坐标分组

全部699节点和698中点都读取，不只读取允许支撑内的站点。每个逻辑输入ID为node:index或midpoint:index。节点记录附带原左右cell及末端角色，但这些角色只解释来源，不把权重再次相加。

R351已经把相邻cell对同一个node变量的使用，以及最后node的直接终端项，散射累加在一个node weight里。因此同一个node记录在173中恰好计一次。midpoint也恰好一次。

坐标使用原有限Decimal字词的准确有理数值分组。若node与midpoint处于同一准确坐标，它们仍各保留逻辑ID、实际$a,b,q$和完整三权；不从位置相同或数值字词相同推断真实alias。group记录包括：

- 全部逻辑occurrences及已经散射的角色；
- duplicated_physical_position；
- source_identified_single_q_variable，严格只在group包含一个逻辑变量时为true；
- 每项$a,b,q,w$及原坐标字面；
- 相同$a,b,q$字词的只读标志，并明确它不等于source共享关系证明。

没有假定$b=a'$。这个分责同样适用于原profile独立返回两列可能有的finite形成差异。

## 3. 实际支撑、严格gap与dyadic宽度

三个允许支撑只从原profile.original_three.bumps读取。准确左端为原left字面的准确提升；准确右端采用left加stored_width。原right字面另保留为metadata，不能拿它替换准确的left+width。

允许区域还与固定初末坐标的严格开区间相交。一个候选中心必须严格位于至少一个这样得到的原支撑内部。所有其他互异node/mid坐标都参与gap，包括不在允许支撑中的坐标。对一个group，取其到相邻互异坐标、所选支撑两端和固定端点限制后的最小准确正距离$d$。

若原支撑重叠，同站只建立一个奇形状：优先选允许最小gap最大的支撑，精确相等时按原support index先后。它不复制同一站来虚增自由度。

从$\epsilon=1$开始逐次减半，直到严格满足

$$
0<\epsilon<d/4.
$$

得到准确dyadic宽度。每个候选保留准确中心/宽度/端点、有理数分子分母、gap、原支撑及两个相邻坐标、减半次数、选择网格身份和严格不等式结果。不存在来自未来网格的宽度或猜定站点。不同中心的闭支撑因此严格不交；形状在固定初末端的0/1/2阶jet都严格为零。

此处有理数运算只在Actions中形成实际目录。本地只审阅源和符号公式，没有代入任何实际网格求gap或响应。

## 4. 固定奇形状与三种算术对象

FrozenLocalShape固定以下函数：

$$
o_s(x)=\epsilon_s^2t(1-t^2)^3,\qquad
t=(x-s)/\epsilon_s,\quad |t|<1,
$$

外部为零，两个端点按零处理。其内侧两导数为

$$
o_s'=\epsilon_s(1-9t^2+15t^4-7t^6),\qquad
o_s''=-18t+60t^3-42t^5.
$$

每端三重零给出准确C²接合；中心jet是$(0,\epsilon_s,0)$。这不修复原基底自身的C²/独立斜率列问题。

源码显式分开：

1. jet_exact：对准确有理数坐标按上式计算准确有理数三jet。可检验当前网格上的准确Kronecker关系。
2. jet_binary64：按源码给出的binary64表达真实形成多项式三jet。其结果不能被jet_exact覆写。中心/宽度是否准确可表示、实际值差异、负零和坐标投影差异单独记录。
3. interval_jet：由调用者提供准确有理数到ball的lift，并明确每个区间所属分支，评价同一准确分片多项式。它不是一个独立完整域证明器。

binary64_definition分别报告中心和宽度的准确可表示性；宽度若下溢或不为有限正数，真实binary64采样给出明确representation error，不把它写成数学上没有该形状。准确端点仍为有理数，不用显示用的rounded端点改定义。

definition中有source身份、完整数学定义及hash、准确中心/宽度/支撑、选择网格来源和required_continuous_domain_breakpoints。from_definition核原source和数学身份后恢复同一函数。任何新网格必须重新采样这个已经冻结的函数；不能在新网格重新隔离中心、重选宽度或重造Kronecker表，然后称为same g。

## 5. 同坐标非共享输入的完整奇响应

准确有限表达下，本奇形状在中心值为0、斜率为$\epsilon$，故

$$
D F[o_s]=\epsilon\sum_{\ell:s_\ell=s}w_\ell/a_\ell.
$$

每个和只使用不同逻辑输入一次，分母保持各自实际$a_\ell$。这给出该明确奇形状的完整三响应。它没有声称覆盖同站任意$(h,h')$：R366还存在值项

$$
-\sum_{\ell:s_\ell=s}b_\ell w_\ell/a_\ell^2,
$$

173不形成或选取这一独立值方向。

形成算术也不与准确公式混写。_formed_response对每个逻辑occurrence，沿已冻结原Jet商法则形成：

~~~python
current = b.Jet(returned_b, [exact_epsilon]) / b.Jet(scalar_a, [0])
dq = current.d[0]
~~~

再用实际node weights、midpoint weights收缩。epsilon通过整数与Decimal tuple构造准确字面，不经过50digits舍入后再谎称exact输入。原q的重新形成字词与保存q逐项比较；不相同则记录，不能静默忽略。

同一记录还独立保留按Decimal形成的$\epsilon\sum w/a$、两种形成结果的差值、完整三向量、原全三merit点积、有限/非零标志、每occurrence商法则词。node后mid的收缩顺序明示；省略零项并不保证和原完整1397项累加逐字相同。全部差异仅诊断，不增加新的数值验收门。

这些形成分数可提议方向，但既没有准确符号保证，也没有rank或stationarity证书。原九小梯度、六宽形状没有下降、173全形成分数为零，都不能取代尚未完成的准确有限或完整函数空间结论。

## 6. 当前网格的可选物化与原完整响应

接口为：

~~~python
result = catalogue.materialize_current_grid(
    group_id,
    run_existing_sampled_response=False,
)
~~~

它遍历全部1397个当前位置，按准确多项式得到三jet，再独立按真实binary64公式形成新表的$a$和$b$列并准确提升到Decimal。输出包括：

- 完整准确三jet的临时数组与身份；
- 完整binary64形成后提升的两列表及身份；
- 准确隔离关系的metadata；
- 实际形成值与准确有理值是否一致、所有差异/负零/坐标投影差异；
- 冻结shape对象与新source-bound shape binding。

这个函数不会把新列塞进旧九参数。optional=true时只调用原R351已有sampled_shape_response，在当前旧九点做已经形成的完整线性链/112末端对照；其执行有独立receipt。它不执行新的非线性primal，也不产生新族或新接受点。sampled binding中的原坐标合同、定义/source和网格身份全部沿R351实际API，未绕过原输入校验。

大表只在调用者的Actions内存/临时路径，不自动打印或上传。定义与实际数组有各自身份；仅凭当前网格采样不能宣称已经提供连续g。

## 7. 完整、partial与小读回

build只允许一次。若grouping中断，report保留分别已访问的node/mid数量以及每类未访问索引；此时unique_physical_positions为null，不能把尚未分组的目录说成空且complete。grouping完成后，每个group要么形成candidate，要么有明确的“非允许支撑内部”skip。响应形成异常保留其真实exception/traceback，不改成零分数。

完整状态保留候选目录、跳过目录、逐occurrence来源、响应错误以及全部数组身份。report默认只给最多8个实际形成分数最大的候选小记录、原完整目录与权重hash、全部counts、已处理/未访group IDs、原support和actual binding。最多可明确请求16个小记录；它不以目录大小驱动大raw工具传输。

候选错误可使build完成位置遍历但有非零response_error_count；complete目录与全部候选有有限响应是两个不同字段。零usable候选时all_finite_formed_actions_zero为null；不能把空集合当成驻点。完整失败/资源中断在failure与stage中记录。

helper接收调用者的绝对deadline，不新增数学步长、误差阈值或独立rank门。调用者须将原始错误和所需小结论在owned cleanup之前保存到实际日志。只有哈希保留的大表不能宣称已在工具端逐值读过。

## 8. 对未来独立十族的明确责任

此helper只接受原九点。后继174若按R370组合所有允许站的奇函数，应先在明确父点生成一次目录并冻结中心、宽度与符号，再定义真正的旧九加一个新系数的独立族。即使FD扰动旧九坐标，冻结形状也不重选；如果实际fresh第十列要求翻转，翻转的是新系数方向，不是冻结函数。

原连续profile、所有Arb分支、circle任意查询和同g细化都必须评价同一个函数，且Arb消费者必须把全部新支撑端点纳入其分段。仅当所有分支输入单元已经按这些断点划分，才可使用interval_jet的branch_midpoint合同。

新的完整primal、原10列forward、全部初末FD、严格slope、原准确binary64提升的Armijo系数、真实20档、原域/453圆/完整112末端和将来的非线性native责任均属于独立producer。173没有预付它们，也没有把这些责任变为先取得准确rank证书才允许运行的额外门。

本文件不绑定164失败状态、不预填未来164重试点，亦不要求164先产生接受点。若174明确选择actual157原九点，应在其新配方中公开该实际来源；选择不同父点则需相应的实际source/参数/表身份。

## 9. 本次交付的证据边界

当前工作仅为完整源文本审阅、精确替换、接口字段核对和SHA。未执行本地科学、未导入R351/Decimal模型、未生成候选/输入fixture、未运行源构造器。终端不可用，未声称已经执行本地AST或编译。源码静态检查可作为后续公开Actions的普通工程步骤，但不是新的数学门。

原完整R351 source与2422 constructor、formed_arrays、sampled_shape_response、0865 profile接口均逐字段核过。实际运行仍可能揭示工程或数值问题，必须按真实记录修正，不能用本接口预称正确数值结果。
