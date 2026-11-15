# Request175：完整37查询闭段Hermite差、准确角域设计与actual98父选择

作者：ChatGPT /root/exact_refinement（AI协作）；2026-11-15。

**这是独立源码合同及包含论证，不是实际175结果。root已选择既有actual98为独立重生父：真实一次原37完整模型/FD后，再做本次诊断；没有选择未来170场、伪造新run或warm。** 170已发布为 bf1880f8c2e0381223bf29fd50ffb6e205afc75b；其真实run为43741803578，当前仍运行。后继实现可以与170并行准备，不以170通过为新增前提。本文不修改170、171或原求解门；不创建175请求文件、workflow或伪造接受身份。

## 1. 170与本设计分别支付什么

170最终consumer为 exact_20261115_R354_thirty_seven_endpoint_remainder.py，75046B，SHA256 84af1e250b8a52d9b1691dd5dbeea4ff674ee79949fd72737e16c3f1b2fa018a。其完整源已更正准确t投影为正sine；两个mean和全部338行保留。

170先在每个端点变体的闭段[0,alpha_j]包围二阶导数并证明该闭段的准确参考域；随后把alpha固定成alpha_j=2^-j，得到该末点的453行Hermite差盒。字段 accurate_reference_pointwise_Hermite_bound_available 正是这个末点语义。它没有计算一个统一覆盖整个[0,alpha_j]的gap盒，也没有支付R354第8节的真实Hermite查询角域。

本设计补两项：

1. 对每个query及17个闭段，形成全453行统一gap盒，同时保共同步长变量的二次系数盒。
2. 在每个闭段对全部2048角证明准确参考的a>0、P>0、|nu|<1，或给出准确参考的严格反证/完整未决范围。原浮点normal实现及其舍入域仍不随此自动获证。

同一旧节点出现在不同A chunk时，仍保独立J/P、scalar b/C及端点变体；不能只按节点编号合并。以下所称“准确”是给定finite字面系数的准确实表达式，不是旧标量provider连续导数、真实无限尾或IEEE程序本身。

## 2. 固定完整范围

| 对象 | 必须保留的范围 |
|---|---|
| left-RMS | 463–473、475、477、479、480、481、482、484、485、486、487，共21项 |
| collocation-midpoint | 471、472、473、475、477、479、480、481、482、483、484、485、486、487、489、490，共16项 |
| 站点定义 | left采用原存储fraction=0.17267316464601146字面，mid采用0.5；实际station、h及四权逐原word绑定 |
| 角 | 每项全部N=2048准确均匀角，频率0,2,...,224；共75776个查询角 |
| 步长 | j=0..16，alpha_j=2^-j；全部17档及原visited/unvisited分别保存 |
| 状态 | 453=338物理+112core+3设计参数；局部RHS后115行精确为零，不能删变量 |
| 原支持 | 原24 cell、29节点463..491、全部端点chunk变体；不是新增query实验 |
| 新诊断域 | 最多37×2048×17个“query/角/闭段”责任；这是范围计数，不声称它们已经运行 |
| 不在本次责任内 | 原699节点、698中点、两组RMS、连续角/站点、完整native、fullDN、最终338响应及物理审计 |

三scalar字段(a,nu,mu)与全部3个控制方向都保存。只有a与nu进入这个角域判据，并不因此删除mu或把nu冒充准确空间导数。

## 3. 必须从原执行新增复制的query scalar缓存

原 geometry_20261114_full_angle_domain_direction_probe.py 的 angular_values 实际调用：

    scalar = flow.scalar_jets(np.array([station]), parameters[:, None])[0]

原 AugmentedFlow.scalar_jets 在同一flow._base_cache里保留该字节station数组对应的baseline和controls，并以这些原值形成scalar。因此最小观察器可以在原angular_values已经返回后，复制已经存在的singleton缓存；不调用base_jet、control_jets、scalar_jets或RHS/J第二次。

观察器应为每次实际angular return保留：

- 原call序号、phase、query完整453字面身份、station单元素数组的shape/dtype/原bytes及SHA。
- 原singleton缓存baseline形状[1,3]与controls形状[1,3,3]、完整原dtype/shape/bytes/SHA；全部3×3项保留。
- 原angular返回scalar[3]的字面身份，与缓存值分别保存；不因同一数学公式就声称这些值间的有限形成误差为零。
- 该query在原B report里的explicit scalar_control_jets身份及其原实际返回call配对。这个B控制返回和singleton缓存控制是两个来源；保两者，不把不同word强行替换成相同。
- 同一个station/query若有额外observer或trial调用，全部保留。实际调用数在运行时记录，不预设74、185或其它历史计数。

base-domain query到scalar缓存的绑定必须采用实际query index、station原word、原angular return index/原query字面，不能仅凭四舍五入后的station或interval号匹配。trial各档的真实缓存身份也可复制，以便判断是否仍为同一准确声明；不从rounded scalar反解baseline。

缓存不存在、多个不相符候选、额外shape或字段不匹配时，保原求解/FD返回及完整观察错误，独立诊断相应范围unresolved；不得补算一份新profile来冒原来源。

## 4. 闭段gap：固定向量系数与逐点余项族

沿每个原端点变体i，令已付区间[E_i^0]与[E_i^1]分别包含R354中的准确常数e_i^0和e_i^1。令非负逐行M_i包围闭段[0,A]上的完整准确RHS二阶导数绝对值，A=alpha_j。所有338物理行、两个mean及115零行保留。M_i的domain必须是真实当前端点变体；不能从其它chunk借用。

对每个t属于[0,A]，Taylor积分余项给出

$$
E_i(t)=e_i^0+t e_i^1+t^2 r_i(t),\qquad
r_i(t)\in[-M_i/2,M_i/2].
$$

原q0、声明q1、h、w10、w11、delta_H0、delta_H1均沿170的真实输入定义。令

$$
G_0=[\delta_H^0]+h(w_{10}[E_L^0]+w_{11}[E_R^0]),
$$

$$
G_1=[\delta_H^1]+h(w_{10}[E_L^1]+w_{11}[E_R^1]),
$$

$$
G_2=h\{w_{10}[-M_L/2,M_L/2]
       +w_{11}[-M_R/2,M_R/2]\}.
$$

所有乘法使用原有符号权；不能丢掉负w11。于是对于每个t，都有

$$
Y_H^\ast(t)-(\widehat q_0+t\widehat q_1)
 \in G_0+tG_1+t^2G_2. \tag{175-D1}
$$

这里e_i^0、e_i^1是真实固定常数，G0/G1只是不知道精确值时的包含盒；r_i(t)一般随t变化。式(175-D1)是逐点系数族包含，**不声称整条真实Hermite轨迹是一条固定二次多项式**。后续任何求导都不能把G2当作固定真实导数系数。

统一闭段gap可由二次Bernstein区间系数包围G0+tG1+t²G2得到，也可与完整区间Horner包围取交。两者对每一个系数成员、每一个t均有效，故允许真实r_i(t)随t选取不同成员。这正是170当前点alpha代入之外需要新增的步骤。

完整query路径的包含系数写为

$$
H_0=\widehat q_0+G_0,\qquad
H_1=\widehat q_1+G_1,\qquad H_2=G_2.
$$

115个常数RHS行的E0/E1/M全部为准确零，因而这些行H2=0；H0/H1中的真实Hermite形成差仍保留。特别是参数路径为准确仿射。不得无检查地假定两个存储Hermite位置权的准确和恰为1，也不得把query参数强改成全局p0+t*dp；直接使用完整453行形成结果即可处理这类有限字面差。

## 5. 使用真实query b/C形成准确scalar

对当前base-domain query复制到的字面b_q和C_q，声明准确参考

$$
(a,\nu,\mu)(t)=b_q+C_q\,\pi_p Y_H^\ast(t).
$$

因为参数RHS为零，实际的参数路径是仿射，上式各字段次数至多1。将H0/H1参数行区间与b_q/C_q的准确dyadic提升形成scalar系数盒，不以原rounded scalar替代b_q。

如果额外trial记录暴露它实际使用的缓存b/C不同，保持两个准确参考身份及差异；不能据此自动判原trial错误，也不能把一个query的域证明跨到另一个有限scalar身份。这里证明的始终是显式声明的同一参考。

## 6. 全角共同变量传播及次数

对H0/H1/H2的338物理行，逐系数作用原完整旋转坐标线性角jet。所有频率和完整2048角保留，准确三角系数沿170已声明的Arb包围及向外整数网格。得到每角的d/e二次系数盒。

对任意给定t与该点真实余项，真实d/e包含于这些系数族；因此继续做完整多项式盒运算得到：

| 对象 | 最高次数 |
|---|---:|
| d,e | 2 |
| Q=d·d、S=d·e | 4 |
| C=d×e | 4 |
| W=C·C | 8 |
| a,nu,mu | 1 |
| a²W | 10 |
| nu²Q³ | 14 |
| P=a²W−nu²Q³ | 14 |

必须保完整15个P系数0..14，不能沿用仿射端点的9个系数，也不能把H2的区间依赖忽略。若实现选择保更高次数的通用容器，尾系数仍明确为零；它不能少保真实14次项。

这里的区间系数族包围通常较宽，因为物理行、左右端点和各角之间的相关性被放松。宽盒是unresolved而不是无根证明。所有多项式子操作向外，完整Bernstein系数hull可与完整Horner取交；不能挑部分控制点或只检查角端点。

在闭段I包含于[0,A]上，若得到严格a下界>0、P下界>0、nu的完整区间严格在(-1,1)，则该准确参考在I上满足所声明角域。P>0与a>0且Q、W为真实平方范数自动排除Q=0或W=0；如果另行报告数值Q/W下界，须实际形成它们的有效包围，不能把这种逻辑排除冒成某个已算的正数。

原normal/sqrt/FFT程序的浮点结果没有因此被重新判定；原IEEE整段形成误差仍未包围。准确参考与原实际trial分别保留。

## 7. 严格反证、未决与端点

以下情况可作为所声明准确参考的域反证：

- 对明确准确t点的整个a盒上界≤0；
- 同一点P盒上界≤0；
- 同一点nu盒下界≥1或上界≤−1；
- 或上列任一结论在某个非空闭子区间上对所有成员统一成立。

对点值的盒仍包含真实系数选择，所以这样的上界判定确有含义。仅有a/P下界非正、nu盒触界、盒宽大或工作预算耗尽都只写unresolved。尤其不能把负Bernstein系数或宽区间的负下界称为反证。

每个[0,A]包含t=0和A，两侧闭端点保留。若准确参考t=0已严格失域，该准确闭段不能获证；原浮点基点曾通过不会替代这个参考判断。不能静默改为(0,A]、跳过零端或改变原容差。

域未付的端点不能提供M，查询端也不能循环假定该M已存在。每个query/alpha结果首先列明左右端点变体和全2048端点二阶界的实际状态；缺失时完整query角责任标为unstarted-with-missing-endpoint-bound，并列出缺失来源。

## 8. 可执行模块分工与最小依赖

保持三个独立源码责任；父来源明确为既有actual98，175接线和新的实际执行身份由后续实现记录：

1. 新read-only capture：在170观察器的原angular-return位置增加singleton b/C复制、完整身份及call配对。原37求解、model、17档、FD和接受对象均不改。
2. 闭段query consumer：复用冻结170的准确字面绑定、Intervals、完整角基、原JP形成差及端点二阶计算，新增uniform_gap、query_scalar_coefficients、complete_query_polynomial与closed_query_cover。不得更改已发布170文件。
3. 同job coordinator：先保原求解/FD结果，再在临时原件仍在时支付独立诊断；真父、完整command/source/input哈希在运行时记录。不会从已清理170/155/166输出的SHA伪造现场。

root已明确选择与170独立的actual98原父，同job真实重生一次原37模型及该次新warm的FD，再消费尚未清理的本次实际现场。原artifact run43677587785/source918fdb11dbb7a424b6149b405e2c7fab3cc0c737及完整ZIP/warm/status身份沿170已发布接口逐字固定；这是新执行轨迹，不能冒作170的续算。后继不得把170尚未返回的结果填入recipe，也不等待170通过作为新的原求解门。

17档的原已访问/未访问仍由原driver-status逐字读回。新角域诊断不能令原试步多执行、撤回一个接受或强迫一个拒绝改变。

## 9. 预算、覆盖和完整读回

工作预算必须与原求解分开，且计入同job全局绝对deadline、读回/清理保留。算法先为所有37×17对建立明确责任清单；有端点M的pair可先形成完整统一453行gap，再推进全部2048角的闭段域。预算不足时，未起pair/角段、已起区间cover和全部pending闭段都能重建。

每个工作单元至少绑定：

- query typed identity、左右实际端点变体、query scalar缓存call与b/C原字节身份；
- alpha指数j、当前闭子区间的准确dyadic端点、深度、原17trial访问状态；
- 原a/nu/P的完整包围或明确尚未形成原因；
- proved、rigorously_refuted、unresolved或unstarted四类中的真实状态；
- source、完整输入、对应临时大ledger的字节数与SHA。

若做adaptive分裂，必须先有覆盖整个父区间的合法粗记录，再以两个闭孩子事务式替换；预算截断不能丢失中间缝隙。端点共享不是把重复角/不同chunk结果合并的许可。实际resource上限待选定接线明确，不以增大65536之类节点上限代替包含算法。

完整453向量和15系数逐行大ledger只留Actions临时，不进入Git/Release/artifact，也不编码拆成聊天大数据。紧凑读回保全部scope/范围、未决/反证责任、边界、两个mean、source/参数/run/SHA及足够数值结论。错误、未完成语义记录及未读范围先完整log，只有原实际readback成功才清理；异常不把证据清空后称完整。

## 10. 永远分开的flags

至少分别输出以下事实，不能以一个绿色job替代：

- original_model_returned / original_model_accepted / original_FD_returned / original_FD_passed；
- all_declared_endpoint_second_bounds_available；
- complete453_uniform_gap_available_by_query_alpha；
- complete2048_accurate_query_domain_on_closed_step_by_query_alpha；
- accurate_reference_strict_refutation_exists；
- complete_IEEE_query_execution_error_on_closed_step_certified=false；
- all699_nodes_698_midpoints_RMS_and_original_trial_checks_certified=false；
- continuous_angle_or_station_certified=false；
- native_fullDN_final338_or_physical_audit_paid=false。

新诊断全成功也不构成BVP/native接受或merit下降保证。反过来，独立诊断未决或资源partial不重标原model/FD结果。

## 11. 当前交付与尚未执行

本文只读原R354、170最终源以及原angular_values/AugmentedFlow实际缓存路径形成设计。没有本地导入、科学计算、数值区间、编译或fixture；已选actual98是既有真实历史父，尚未创建或派发175请求/workflow，也没有175的新warm、区间或运行结果。这里的次数和包含论证是解析推导；所有新的参考区间、完整角域和资源表现只能由公开Actions产生。

此后是否采用逐角二阶区间的带符号DFT投影收窄M、或沿闭段细分端点后改用更局部M，可以由真实170输出决定。它们不是本设计的预付数值成果，更不能为其后续实际执行增设新的科学接受门。
