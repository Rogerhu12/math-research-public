# 2026-11-26：Run02 第49步的完整实际返回、缓存成本与终态边界

## 1. 本条结论及实际证据

公开 [Actions 45800076687/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45800076687) 的第49步于 **2026-11-26 16:08:12 UTC** 真实返回，状态 completed、退出码0；这是一条同固定标量目标、同原完整有限表示、同 jet-sum 范数的缓存复用后续。真实重启点793b经一个接受的度量方向得到f66c；重新读取的有限曲率/幅度/全部永久点筛通过。它尚未满足本课题的全域度量、全时刻几何及固定参数精化完成标准。

紧凑实际来源是[第5卷第49步](2026-11-26-public-actions-45800076687-1-part-005.md)；[终态总索引](2026-11-26-public-actions-45800076687-1.md)完整保留阶段46–49的相互关系。原完整科学报告、数组、缓存清单与子日志留在runner，本条只登记实际必要身份、参数、归因边界和标量，不转存raw。

总 job 139840695899 在API显示 completed/cancelled，结束于16:08:25 UTC；其执行控制器的第5个workflow step却显示 **success**，结束于16:08:14 UTC。这两层状态必须分开。第49步已经自然返回且被发布，不能依据job总状态将它改称失败；同样不能因第49步成功而将整个研究改称完成。

## 2. 预算、返回与未执行的第50步

终态完整job日志给出以下实际事件：

| UTC | 实际事件 |
|---|---|
| 15:26:08 | 第49步子进程启动，PID15050 |
| 15:52:34.0799656 | followup_budget_admission_closed；同一第49步仍在运行 |
| 16:08:12.5770220 | followup_returned；completed/0，耗时2521.706654018999秒 |
| 16:08:14.8504097 | followup_controller_checkpoint；reason=budget_checkpoint，实际返回followup数21，research_complete=false |
| 16:08:25 | 总job终态cancelled |

本workflow的真实job时限是350分钟，job起点为10:18:24 UTC，并非以10:18创建时间机械加6小时推断16:18。实际控制器step于10:19:08开始。20000秒准入预算在已有活动子进程尚未返回时只关闭新任务准入；第49步仍完成了自然返回和发布。

第49步发布提交为75b65a1bc7b932f9c942687eae8e2b802348d943；最后总索引/交接预算checkpoint提交为ed4092768969b5fbfb859355cc4f8a1e3897c9d2。已排的第50步纯读取 **没有获准启动、没有实际结果**。因此第49步的实际接受alpha、各trial、QP停止标签、实际advance数、末面Pg/tolerance及比值尚无公开返回；不能把配置maxiter=64写成“已驻点”，也不能从J/J*调用计数倒推出这些缺字段。

## 3. 完整输入、来源、物理父与重启父

本次科学子进程实际源码提交为5100a2e3709d592429cf9f4e651463afd3eee206。

| 角色 | 完整SHA256 |
|---|---|
| 完整launcher：launch_so3_cached_interior_restore_actions.py | 9b87e0e42c310464a369e8a1e09225c939910cab3a7bcd7c053ac3e6ace12159 |
| 完整driver：fullclosed_so3_cached_interior_restore_qp.py | 174b79f4b2393a719e7ddee70f59fe5c500e89d41e8d181497f1b4329f8b015f |
| 实际原物理算子：so3_closed_meridian_operator.py | 234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42 |
| 原全jet provider：so3_parent_meridian_jet.py | d3f25bb74e179865b20f7759bc1ee8dcdf2c2771f062ac096ee4d5398a8be4b9 |
| 完整缓存helper：so3_frozen_parent_cache.py | 4e9ed6949bf42f8ef103b06d0e15dbfa1a8f7d21317a9492f71dca33195824cd |
| 同实际父固定目标binder | 9ca39afd9f840ba89fbb75d7365220c2d85d26ddb26b2d66b6c55e611313fd55 |
| 本次实际目标/四输入绑定 | c6fb362652de15bfdaef13ce71e3b5cce472cc61debe6510969d06142619c432 |

下列“父”并不是同一角色：

- 冻结原 meridian 与固定标量目标的 deep 物理父文件是 deep-fixed-scalar-amplitude-first/final.npz，SHA256 d021a50a492b941004ee75f5cba138d5b5bc07092073a642a027bde4f97bb478。
- 固定标量目标身份是0a223b986f35263c168e26d30295fd84048e134c6b053ba90c7cd39beaf1f5cb；当前完整SO3模型身份是ad01742ce5051188bafddf8e93046468788eb27e7ec948c26903578742f5bb92。
- 完整context身份是2ac30303c248e5f9f430ff16d567897a7795d485484970ea6380f3e9b9eb8af4；actual context_all_four_inputs_equal=true。固定目标未从当前SO3场重新拟合。
- 真正继续的当前自由量文件是 so3-closed-actual-profile-interior-restore-first/final.npz，SHA256 **793bde458be303034d3f3a0b1b7f9fd17d7cf84ec99fc1b3bb5313ce10008044**；其完整报告SHA256 **bb5c52e02af18b02cd2aed9a9d64fe6bb687f8f1f1510fe0792684ff241f9241**，实际来源为0f542de9ab1f91f5ca27a0efe315b0ee96beddd3e3972ba12fbc5140221623a6。
- jet-sum范数身份仍是c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa。它没有被改称原径向积分H²范数。

驱动的完整重启检查保留真实来源/schema、上述四个原输入、当前完整物理模型、固定目标、范数、完整终文件hash；没有把缓存身份替代当前场身份。

## 4. 完整参数与实际预算

本次保留全部 **1,333,370** 个自由量，M=160、J=923、N=2048；完整正权观测行数 **45,324,288**。原192几何工作行选择、所有幅度行、两套永久位置、两距离符号、完整非线性几何筛与原acceptance均保留。当前表示仍包括完整 h-prime Delta 径向Gram项，不能将其称为径向误差恒零的zero-endpoint表示。

实际命令完整见第5卷第49步，其关键配置如下：

| 项目 | 配置 |
|---|---|
| 新度量方向预算 / 内层预算 | 1 / 64 |
| 恢复方向上限 / 内层预算 | 4 / 64 |
| 初始度量、恢复阻尼 | 0.01 / 0.01 |
| Phase I 搜索内缩量 | 1e-8；原真实物理g<=0验收不变 |
| 原ray回溯上限 | 15 |
| QP atol / rtol | 0 / 1e-6 |
| 损失 | p=4、epsilon=0.001、scale=0.05；centered_phi_normalized |
| 完整观测混合比例 | legacy_fraction=0.5，原正权全保留 |
| 径向工作积分阶数 / angle_block / stage_block | 8 / 8 / 64 |
| 范数长度 / 角向过渡参数 | 0.05 / 24，norm_kind=jet-sum |
| eta起点 | 原node885 |
| 数值reach比例 / 安全系数 | 0.03 / 0.992 |
| 标记直径预算 / 见证下界预算 / H下限 | 4.2 / 0.9 / 1.01 |
| active band / 原几何行预算 | 0.025 / 192 |
| Torch CPU线程 | 4 |
| 同scalar准备预算 / 积分容差 / 尾截断 | 300秒 / 1e-18 / 1/8 |
| solver target | 1e-9，仅数值方向参数，并非README完成证书 |

实际返回是 **1个度量方向、1个接受；0个恢复方向、0个恢复接受**。末阻尼仍为0.01/0.01。驱动停止原因是declared_metric_direction_budget。

## 5. 本次真实初读与末态

同一新执行内部的初值与末值是：

| 实际量 | 本次新初读 | 本次末态 |
|---|---:|---:|
| finite max relative Gram | 0.03677022561576172 | 0.03662269652001199 |
| centered Phi | 0.0067327958799266755 | 0.006640209697890763 |
| maximum physical g | -6.229264548629487e-9 | -4.0351764152291025e-9 |
| 数值K乘积 | 本卷未单列 | 0.9919999959648236 |

末态complete=true、final_geometry_feasible=true，all_permanent_read=true，all_signs_read=true；永久curvature位置2856、radius位置2821。末态五种幅度约束值分别为：

| 家族 | 实际g |
|---|---:|
| body diameter | -0.0478153145908794 |
| distance plus | -0.09045738519919455 |
| distance minus | -3.3090759484028496 |
| cap diameter | -0.12674458207439843 |
| H floor | -0.9649120599891324 |

工作逆图的root_residual为4.440892098500626e-16，工作采样root_rho为0.16590034653773367。它们不是全角连续root误差或rho正下界证书。报告明确metric_certified=false、geometry_certified=false、accepted_isometry=false。

### 同一checkpoint的新baseline存在微小浮点差异

本次initial-new-field.npz逐字SHA等于旧793b文件；但本次全场新初读的标量不能强行替换为旧0f末报告值：

| 量 | 旧0f末报告 | 本次174b初报告 |
|---|---:|---:|
| max | 0.0367702256157602 | 0.03677022561576172 |
| centered Phi | 0.006732795879926417 | 0.0067327958799266755 |
| g | -6.229263438406463e-9 | -6.229264548629487e-9 |

完整源/模型/目标/四输入/自由点身份都已明确绑定；缓存复用不授权直接继承旧标量。这里应以 **本次真实初读** 比较本次最终Phi和max。现有返回没有足够证据把这些末位差异唯一归因于缓存、执行顺序或某一具体浮点操作；本条不推测其唯一原因。

## 6. 缓存究竟复用了什么、实际花了多少

本次缓存是原固定T0 meridian工作值的复用，不是当前场残差、J、约束或证书的复用。完整原operator/provider方法保持真实原source，缺失或无法识别的键仍走原provider。

| 实际缓存量 | 返回值 |
|---|---:|
| adopted files | 2216 |
| adopted points | 22954625 |
| adopted bytes | 2205842272 |
| hardlinked / copied files | 2216 / 0 |
| missing planned files | 13 |
| unidentified legacy files not used | 0 |
| fresh files / fresh points | 3 / 22128 |
| final complete manifest entries | 2219 |
| setup seconds | 9.948729793999519 |
| fresh-file validation seconds | 0.8788728139988962 |
| final-byte audit seconds | 1.642414584999642 |

缓存绑定身份为983e73e94a6d088a512161af38fb79c06bd8961b81879d20196ddcf8eaed1208；最终完整manifest SHA256为b873741c45792097d3dc04246b7464583c5014285ca0b503e8e206718cd0b034，大小4052407字节，仅留runner。

实际 legacy_adoption_without_historical_checksums=true。旧producer没有历史checksum/queryhash，本次采用的是明确记录的首次新绑定，不能倒写为旧报告已经具有这些校验。same-run实际producer/完整物理父与四输入/模型/source/query设置等检查仍适用；未来完整manifest复用与首次legacy绑定也不能混称。

| 实际成本 | 秒 |
|---|---:|
| 初始化、缓存采用后完整首场读取 | 400.9209956880004 |
| driver实际total_seconds | 2515.198085983 |
| 包括缓存manifest的total | 2517.1932090869996 |
| 控制器测得完整子进程 | 2521.706654018999 |

峰值RSS为3291096 KiB。前0f实际initial_seconds为1812.1884115920002；可以并列记录两次实际成本，但两次当前场、永久地址/读取条件并不构成只改缓存的配对试验，故不能由这两个值直接宣称严格加速倍数或把其全部差额归于缓存。

本次实际计数：residual_calls=10，J_calls=68，Jtranspose_calls=69，point_covectors=196，parent_jet_evaluations=21602，parent_jet_points=43727，evaluated_field_points=582819353，inverse_chart_solves=100601。这些是报告的实际口径；它们不能替代尚未返回的逐QP、逐trial记录。

## 7. 完整输出身份

所有下列文件前缀均为当前runner research/so3-closed-actual-profile-cached-interior-next/：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| report.json | 24434262 | d2d0ec295fcb4af7eba6b9bf7528a8b79d88d2c1eda70797abf911eaf90895fe |
| initial-new-field.npz | 10720258 | 793bde458be303034d3f3a0b1b7f9fd17d7cf84ec99fc1b3bb5313ce10008044 |
| final.npz | 10720258 | f66cb8b896822632e6f53bd9a0c259c9e21f6180552375aaef50abd2ab6e2c27 |

同runner research/so3-closed-actual-profile-cached-interior-next-command.json为13962字节，SHA256 2593be3a15a2fc4087f919d10d759422a62bd438fb137987d6fc2759b72462f4。全部命令和输入文件身份已在实际第49步紧凑记录公开；本条不复制完整raw报告、cache manifest或NPZ。

## 8. 下一独立runner的明确父选择与未完成责任

已准备的Run04仍按原完整必要重建链到 **本run实际0f内点父**，直接接完整后退锚分离/SOC的新策略；不额外重放本条2521.706654018999秒的第49步。该选择把有限runner时间用于同固定目标、实际可行内点上的新方向，不意味着旧49没有返回，也不冒称旧f66c就是新Run04的父文件。

新runner必须由自己的真实报告冻结其物理父、目标、当前自由点与同run缓存，不能继承旧runner-only NPZ/cache或强行要求新重建hash等于旧值。旧49是完整实际进展，已登记；本次Run04父选择是一项明确不同的后续算法选择。

待完成责任仍包括：下一实际方向的完整逐QP与逐trial归因；可推进至README所需度量精度的完整输入/算法；同一最终固定g的真实精化；新末场自身连续度量与几何消费。单次有限通过、缓存复用、一次预算结束和job终态均不能代替这些责任。

## 9. root核验与后续实际启动

2026-11-26 16:21:38 UTC：root亲读第5卷实际49完整紧凑对象，逐项核完整参数/输入/输出/标量、summary_errors和missing_outputs均空；未读取不存在的50结果，未从计数推填alpha或QP类别。独立04已由提交 `6501653312a0d8ca18b8cebd85f6ce0c84f7f6cf` 的push触发：[run45857104277/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45857104277)，16:15:49Z创建，job140038237351已在执行完整必要再生。其完整14步源/参数与明确0f父选择见[接续说明](2026-11-26-run02-budget-and-complete-run04-continuation.md)。
