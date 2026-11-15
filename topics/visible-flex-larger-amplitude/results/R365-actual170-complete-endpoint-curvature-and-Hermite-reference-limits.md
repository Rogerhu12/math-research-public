# R365：actual170 的完整端点曲率、629 个 Hermite 末点包围及其责任边界

日期：2026-11-15。本文只读取原公开 Actions 输出、原字面标量及源/文件身份；未在本地重算矩阵、分数、区间、范数或科学模型。依据是 [R354](R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md) 和 [request170 完整接口](../notes/2026-11-15-request170-complete-R354-endpoint-reference-interface.md)。

## 365.1 实际结论

actual170 从真实 actual98 父对独立重建一次原 37 查询模型，并在新 warm 上完成原 FD。原模型接受 $\alpha=1/8$；最近拒绝 $\alpha=1/4$ 的已选 LEFT464 和 MID471 仍有负 $\beta^2$。它不是 actual155、166 或后续171末点的恢复。

后置 R354 消费者完整访问了29个实际端点变体、各2048个准确有限角、17个闭步长区间，以及37个查询的全453分量形成差。29×17共493组端点闭段域全部严格证明，完整338行 RHS 二阶界均可用；37×17共629个准确 Hermite **末点**差包围全部可用。四个原已访问步长还各有37个逐点执行差包围，共148组。没有资源截断、科学异常或未访问后缀。

这支付的是所声明有限参考的端点域、导数及末点差额责任。原结果同时明确：

- 全真实 Hermite 查询角域证书为 false；
- 整个 IEEE 执行过程误差证书为 false；
- 统一覆盖整段的 Hermite gap 区间尚未计算；
- native、fullDN、全场/连续角/metric 接受均未付。

因此“全部独立计算访问完成”不等于原用户目标完成，也不把本次诊断加入原模型接受门。

## 365.2 真实公开身份与原参数

| 对象 | 实际身份 |
|---|---|
| Actions run | [43741803578](https://github.com/Rogerhu12/math-research-public/actions/runs/43741803578) |
| 固定科学 source | bf1880f8c2e0381223bf29fd50ffb6e205afc75b |
| 唯一 job | 132896377831，original37-and-R354-reference |
| 官方终态 | 原模型/FD、独立诊断、读回、清理全部 success |
| 原 job log UTF8 | 4443980 B；SHA256 429a69f20aecbe99dbffe13c72168243bebc4b716da000c3300c03570fb4df71 |
| 原模型父 run/source | 43677587785 / 918fdb11dbb7a424b6149b405e2c7fab3cc0c737 |
| 原父 warm | 4927052 B；b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67 |
| 原父 status | 3379453 B；b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff |

实际启动输出核100个源码pin与3个参数文件：原90源、原批次worker1件、保留158/166来源6件、新capture/consumer/samejob3件。原三参数和历史来源没有由删失 warm 的SHA反造。

完整原模型参数仍为一次迭代、damping270、LSMR200、projection200、17档回溯；凝聚最大512工作行/200 dual sweeps，原模型1200秒、凝聚600秒及90/30秒预留，angles4096、jac-workers2、保原complete-H。后置角表为每查询2048角，没有把其角数偷换成原4096 guard。

新37的实际集合为21个LEFT和16个MID。LEFT区间为463–473、475、477、479–482、484–487；MID为471、472、473、475、477、479、480、481、482、483、484、485、486、487、489、490。完整B支持、真实端点及外部变量仍在，原变量236036维，局部9805维；未把外侧节点或109个自由core模态置零。

## 365.3 原模型与四个真实试步

原固定权merit为43.363003729098274，原方向斜率为-0.21838603098375256。下表所有负角数、最小值与merit来自原记录，不是本地重算。

| 原trial | $\alpha$ | 原结果及实际失域范围 | 原线性 $\beta^2$ 最小值 |
|---:|---:|---|---:|
| 0 | 1 | 拒绝；选中LEFT463–469、LEFT486、MID487存在负角；原midpoint487 RHS非有限 | 0.00042441358125799855 |
| 1 | 0.5 | 拒绝；LEFT464有12负角，MID471有4负角；原midpoint471 RHS非有限 | 0.0006366194677895898 |
| 2 | 0.25 | 最近拒绝；LEFT464有4负角，MID471有8负角；原midpoint471 RHS非有限 | 0.0007427224110553854 |
| 3 | 0.125 | 接受；37查询所有负角/非有限角计数为0，原两套698点RMS检查全通过 | 0.0007957738826882832 |

最近拒绝的完整原定位：

- LEFT464，query_index1，station1.1553475805065636，最小 $\beta^2=-0.2683086899521916$，angle_index54，phi0.16566992509164924。
- MID471，query_index21，station1.1918702857402743，最小 $\beta^2=-0.19167001275188889$，angle_index44，phi0.1349903093339364。
- 全75776条原线性reserve在该档的minimum为0.0003183097338947949，negative_count0。这是实际线性可行与真实查询失域的差距，不能据此把Hermite效应概括成唯一原因，也不能说这两点未被模型选择。

接受档的原固定权merit为43.33605694766103，原实际降幅0.02694678143724616，原预测未正则merit降幅0.026877973010679432，原比值1.0025600303467597。物理collocation最大值由0.00710763096028075变为0.007107481419522546，仍在interval461/original_residual_row155819；该行原冻结权199.00690823502174，未用试步RHS重定权。完整boundary最大值由7.837078403973583e-9变为6.857449986338445e-9。全core/controls在各节点仍一致，constant collocation与left residual为0。

新 warm 的FD实际重算通过：最大四阶相对方向误差8.81884772255149e-10，最大二阶误差0.00000988344249574147；原阈值0.00005，second_order_truncation_contracts=true。该FD并未求当前高度的非线性native/DN；full_BVP_solved、nonlinear_DN_evaluated、full_Cartesian_closed_surface均false。

原status接受warm_steps1、optimization_progress=true，但success=false、new_coupled_finite_acceptance=false；phase为actual-full-angle-projection-merit-decreased-unaccepted-warm-saved。不能把warm优化接受改写成完整BVP接受。

原QP仍选择R270-condensed-complete-H，原C候选目标43.36288930284786，最终完整原模型目标43.24773462371635。后验原浮点gap3.626213640472997e-8、stationarity L2为0.03241534176964486；工作行512/dual200预算已用，full_QP_optimality_claimed=false。它们不是严格外包或新的接受门。

## 365.4 完整R354计算实际支付的范围

消费者实际source为 exact_20261115_R354_thirty_seven_endpoint_remainder.py，SHA25684af1e250b8a52d9b1691dd5dbeea4ff674ee79949fd72737e16c3f1b2fa018a。它沿已核原正sin的t投影；未使用先前负sin审稿。实际capture为74fc383db1b00c564ccab9709b1de5f500674914a5efef83997960c867950c4c，samejob为46f85ccec569533d8d7652d94b059dc9c8d49e926408f68dd131002ef5c71cbd。

| 责任 | 实际完整范围 | 原结果 |
|---|---|---|
| 原控制调用配对 | 实际74个原返回，37查询全部station及explicit scalar-control身份匹配；所有额外observer调用保留 | complete |
| 原端点变体 | node463–491的29个实际变体；同节点只有J/P/b/C全words相同才复用，保全部来源 | 29/29 |
| 准确端点投影 | 每变体2048个准确有限角、完整338物理行、112core和3control零RHS行，mean行0与225保留 | 29/29完整 |
| 原J/P字面作用 | 每变体全338物理列与3参数列，准确dyadic求和，完整453输出 | 29/29完整 |
| Hermite形成差 | 37查询的全部453分量 $\delta H_0,\delta H_1$，保两个mean及常数状态 | 37/37完整 |
| 端点闭段域/二阶界 | $j=0,\ldots,16$，每组区间 $[0,2^{-j}]$；493组各2048角 | 全493组严格域通过，338二阶界均可用 |
| Hermite末点差 | 37查询×17个准确末点 $2^{-j}$，完整453分量 | 全629组available |
| 实际逐点执行差 $\eta$ | 原4个已访问trial×37查询，实际query words减准确参考区间 | 全148组保453分量 |
| 未访问原试步 | $j=4,\ldots,16$ 共13档 | 明确没有原trial/query执行返回，不虚构 $\eta$ |

493组端点闭段记录中，accurate_endpoint_refuted_angle_ranges、unresolved_angle_ranges、unvisited_angle_ranges全部为空；all2048_rows_processed、full_accurate_endpoint_closed_domain_proved、complete338_RHS_second_bound_available均true，115个常数RHS二阶导数准确为0。629组的gap也均为453行；没有省略两个mean。

这不意味着每一个真实内部Hermite查询沿闭段均合法。原失败发生在内部query，其状态依赖原两端RHS；端点仿射路径合法与内部query合法是不同命题。本次complete_true_Hermite_query_angle_domain_certified明确false，629组各自all75776_original_query_domain_rows_certified也都false。

## 365.5 四个对象与末点/整段范围必须分清

准确有限参考用 $\theta_n=2\pi n/2048$ 及全部频率0,2,…,224；Arb384位生成准确有理角的三角区间，之后全部区间操作用向外320位整数网格。原记录literal_original_FFT_twiddle_identity_claimed=false：这是准确均匀有限DFT表达，不是原FFT舍入操作次序的逐bit重演。原 $a'$ 字段沿原接口使用，不把它重标成另一条profile的导数。

本次明确分开：

1. 原实际J/P矩阵words对原完整方向的准确dyadic作用；
2. 事后新形成的binary64 J/P作用及其相对1的形成差；
3. 准确有限参考的完整RHS和方向导数，相对原返回/字面作用的 $e_0,e_1$；
4. 实际已访问trial的query words，相对准确Hermite参考区间的逐点 $\eta$。

例如LEFT464的原 $\delta H_0$ 最大分量在mean行225，原准确值编码为
$$
\texttt{-0x8333aef2c4d45ad4302131082d3}\,2^{-160}.
$$
MID471的原 $\delta H_0$ 最大分量也在mean225，编码为
$$
\texttt{0xcf85ce1d42505}\,2^{-105}.
$$
这两个小原字面证据说明形成差和mean未被省略；本文没有把它们转成新的十进制近似或据此推断全部实际失败的主因。完整逐行账本只在Actions计算。

R354二阶上界 $M$ 的域覆盖整闭段 $[0,\alpha]$。本次保存的gap使用
$$
\delta H_0+\alpha\,\delta H_1
$$
与端点的 $e_0+\alpha e_1\pm\alpha^2M/2$ 在**固定准确末点** $\alpha=2^{-j}$ 组合。因此Hermite_gap_intervals_are_pointwise_at_declared_alpha=true，whole_alpha_uniform_Hermite_gap_enclosure_computed=false。不得把“闭段域给出M”改写成“这一张末点gap盒已经覆盖整段”。

148个 $\eta$ 也只是 actual word minus interval accurate Hermite reference；它们不是整个IEEE算法沿所有 $\alpha$ 的统一误差界。没有对未访问13档添加原执行返回，没有新调用原RHS/J/QR/FD/trial；extra_original_RHS_J_QR_FD_or_trial_calls=0。

## 365.6 原输入、结果与日志字节范围

完整原输入绑定已由Actions支付，原报告列307个实际packet；complete-input-binding.json.gz为179523B/8dfe8a8c5edf4a4349dc53233bba3b8c4a9ae220308330d1d9faed07ceb7032c，解压字节1089447/a9fc011504410badf1e8ea10085feb21d9be66774152068cee9fe91cea1dce8b。原完整方向236036维，其coefficient raw SHA23f95dc5a91e3e2909cc6dc3978bbabc4f35536c183f7890b3f82184a89f85b8；没有从Bz反造输入或再次缩放。

| 原对象 | 字节数 | 原SHA256 |
|---|---:|---|
| model-000.json | 814465 | adb752961d4c00d550bf7113255ffbbf4442444cf2f3cc42c8c553fcac302f43 |
| 新driver-status.json | 3647516 | dd9675db4ef02dbbd7f2d0e0ebe70e849c180c670fa4a97c8ff78847e0108be5 |
| 新warm-001.json.gz | 4943007 | 97b8195276ee82afb29cf769c95b7e7a72b24725120039fc7e6bfa6d5facd705 |
| response-check.json | 2839006 | ff00921bdba13a4f27186425d56f2e2f959f4f36151255492e02048d272285ae |
| 独立diagnostic result.json原文件 | 2742622 | 486a0b5eb977c24b9a18c5585bc2de0668beb68a049a3620747c642cbf40e7bb |
| 同result解析后sorted ASCII+LF | 2742622 | b745038d23a1bec84768616acf7fc8ad30044486063410f670a323f3550fcf18 |
| 原小diagnostic summary的canonical ASCII+LF | 1340 | 2d98ab83ec46dcd459b6110fa34b3efba8582036728d3c684cbd23085036d779 |
| 原完整model/FD摘要canonical ASCII+LF | 442609 | 3b09f70a7427e6c3193e89fc75d99acdc13d7f8d0760fee3dfc539f13c3accc9 |

原文件SHA与排序后语义SHA分列，不能互相冒充。唯一官方joblog在本次读取后，8个实际语义document和1230个member各自的canonical长度/SHA已用原数字词法核回；模型摘要两处同身份，pipeline两处同身份。只做JSON/字节工作，没有从它们再计算新的科学量。

官方拼接joblog有3个UTF8 BOM，包括某个中间timestamp之前的行首BOM。解析时只去该行首BOM再识别timestamp，原全log及原行身份保BOM；由此恢复Hermite_transfer[364]并核回完整document身份。这是日志格式处理，不是科学补行或修改原数值。

原33个临时ledger报告总解压字节1054835158，含全部角/453向量及629组原账；它们仅在Actions临时存在，未搬入Git/Release/artifact，也未在聊天逐行重做科学审计。本文只保源、参数、run、文件SHA和必要完整范围结论，不能凭账本SHA声称另一次独立全数组验证。

## 365.7 实际资源、清理与下一责任

原模型child577.098109541秒，原FD child17.391939944秒；诊断child2668.477629976秒，消费者内部elapsed2668.2603506120004秒。post_model_diagnostic_exit_code0、scientific_exception=null、resource_partial=false，stop_reason为all-declared-independent-computations-visited。

原规则监控17:34:08 UTC启动、18:29:10结束，两轮真实同步，没有README差异/规则终止，science_returncode和wrapper_returncode均0。完整读回marker存在后才清理该owned临时目录，原raw上传为0。新warm已按规则删除，后续不能只凭其SHA冒现场接续。

本次有证据的推进是：原37模型仍可产生一个真实接受步，同时R354所需端点闭段合法性与完整二阶界已实际支付；最近拒绝中原线性可行并没有保证真实内部query合法。下一独立175已设计从可恢复actual98父另付一次原37模型/FD，使用完整原scalar cache与均匀闭段gap，把这些差额推到真正查询的角域判定；其结果必须依自己的真实输出，不能预借本次629个available标签。171的真实37→38同job轨迹同样独立，不以本诊断为前置门。

当前没有原native/fullDN接受、没有连续角/全699节点与698区间域证书、没有metric或强C²结论。原最终门和容差没有放宽，科学目标仍在推进。
