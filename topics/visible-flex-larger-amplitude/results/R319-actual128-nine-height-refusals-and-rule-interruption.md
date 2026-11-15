# R319：actual128 九控制完整高度路径的六次正高度拒绝与真实规则中断

作者：ChatGPT /root（GPT-6 Astra Pro，AI-assisted）  
日期：2026-11-15  
类型：公开 Actions 原结果完整读回；非新科学计算；未取得非零完整场。

## 319.1 实际结论

[Request128 的公开运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43702058809)已结束。原零高度请求收敛，六个已经返回的正高度请求各用尽原十档回溯，全部在 stage0/rawCell0/rawSegment8 被原 D/S/A 域判断拒绝。第八个请求已经启动但没有响应；原规则 runner 真实 pull 后发现 README 改变，于 12:17:44 UTC 终止科学子进程。该未返回请求不能记成第七次数学拒绝。

这一次九参数初点来自实际127第八批，和 [R315 的实际124](R315-actual124-complete-height-path-refusals-and-rules-interruption.md)六参数初点不同。两者观察到相同类型的首段域拒绝，不构成“增加三个控制没有作用”的同初点因果实验，更不证明不存在非零解。正高度已经返回的完整 withJ 基点评价都成功形成，失败发生在其后的实际 Newton 试探。

本次没有到达 $s=1$，没有 endpoint 338×112 完整响应，没有 boundary FD/full-DN 及非零最终审计。原 adapter 的 success、new_coupled_finite_acceptance、full_Cartesian_closed_surface 均为 false，accepted_result 为 null。compute job failure 与 report job success 均不能代替数学接受。

## 319.2 公开身份与已实际读取的范围

| 对象 | 实际身份 |
| --- | --- |
| source commit | 3ee6c53840032444b2b88bb4ff98d69f038239d3 |
| compute job | 132775124928，failure |
| report job | 132808787425，success |
| request SHA-256 | 2ef24cc239f609131dc1692557bd20be02a1236bb765a4df0e3c8c480537c0e5 |
| 参数 recipe SHA-256 | 739a2a00be77cdcc0c4596393da55335c16a07a361cf0a635b5b2f9228fdcff8 |
| 原紧凑摘要 | 33756 B / aa9f9c0fa2e7eb2888afaede56e51a53d41b8490311c62ff9bb4c574e4c6c0d1 |
| compute 工具解码 UTF-8 日志 | 190153 B / 8c896907af0107825849eefbf7fb34f72409928b158692e24eb81307c2396ba9 |
| report 工具解码 UTF-8 日志 | 72264 B / 14c609ad286cd13a57cdb13f93ebc153eb1616459eaa9588e31d2cfea86bc8b9 |

本地终端不可用，本次按根 README 第8条读取 GitHub 原日志。上述日志 SHA 仅指工具返回的完整带时间戳 UTF-8 文本，不冒某个服务器日志 ZIP 或未经读取的 CLI 文件。对摘要只剥离行首原时间戳及可选 BOM，并取原 BEGIN/END 之间正文；两个 job 的正文逐字一致，33756 B/SHA 完整匹配，长度不包括分隔 LF。

此外，本地完整读取 compute 中七条 request_returned 事件，包括其原 trace、全部60条 trial、warm 和失败位置；没有执行科学函数、数值范数、矩阵运算、模块导入或数值重放。原摘要 summary_complete=false 是科学中断范围，不表示其已保存字段缺失。readback_errors 为空，尚未执行的 phase 均未被记为通过。

原科学 stdout/stderr 文件为 79265 B / d9f79d1eb12a79d0f13d9b73ca93684029d11ac13e41b6756885fd0ece47c2da；该身份由原 reader 记录。本地读的是上述外层 compute 日志所传事件，没有重新取得已清理的内层整文件。原输出中 large sections 另以完整 count/SHA 表示，也不将其身份冒成已经下载和重验全部 payload。

## 319.3 真正的参数、完整目标和原问题范围

参数顺序为 $(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3)$。实际初点为：

[0.32187323564609926, 0.21204423511345535, 0.3992005008064338, -0.08290967451783622, -0.021154050830509367, 0.8576496337449642, 0.9744108740349993, 0.6297613969180598, 0.43487814523197305]

来源为 actual127/run43700393105/source47bda30230e7aea8a85b5ecd039832c023249f87 的真实第八批终点。原 status 为1812905 B / 1c4e24d005620ec08e87bf4450cd69e8d5d2f1203922a73cf122b1c9c859ab74，原紧凑摘要62531 B / bc100938dfdc657560e84d52b49f5432cfb94c7b4e2d251bd1147ced09033bd5。这里只转录实际参数作为新实验初点，不重载旧 J/merit 或把未接受的 circle 参数称作非零场。

实验明确 $\lambda=0.001$，前三参数活动、后六参数冻结，699个原节点、112 core/tail 模态、2048角点、453状态和完整原方程均保留。初猜是原 fresh-circle-low-three-linear；high109 初值为零但仍是原自由未知量，不构成 Schur 消去或高模非共振证明。

完整目标 $H_*$ 的原文件为896 B / ce496ad1df2509d3ef94410e20a3352d5fa9eb2459fbd872f43d511f86648eee，形状[112]、dtype <f8、无负零列；其第一分量原值为 0.00009935495691535073，后三低模以外的109分量也没有从本次请求删除。真实路径为原 helper 对全部112目标共同取 $H(s)$；零请求不代表把目标 $H_*$ 改成零问题。到 $s=1$ 时必须复制原 $H_*$ 字而非另算近似；本次没有达到该处。

原 first-order 初猜低三缺陷为 [-2.1789887195141673, 0.00010959361946247565, -1.3735900620895742e-7]，不等于非线性已解。原初始 collocation max 为 1.9713889644924298e-7；这也不支付原完整边界条件。

## 319.4 全部八个实际请求

下表逐字转录原已保存标量。最后一行只有 request-in-flight，没有填充响应数值。

| call | $s$ | 原返回 | 原 iteration0 norm | 原 minA | 原 minD | 请求秒数 |
| ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 1 | 0 | converged | 0 | 1 | 1 | 895.1974098029999 |
| 2 | 0.015625 | 原十档全拒 | 21602.4460937367 | 0.9926403044120727 | 0.9999960854405683 | 1066.6148453 |
| 3 | 0.0078125 | 原十档全拒 | 10800.745651920744 | 0.9963269473979037 | 0.9999980429062515 | 1064.516339047 |
| 4 | 0.00390625 | 原十档全拒 | 5400.0206658558 | 0.9981651631082217 | 0.9999990214996142 | 1063.7221462370003 |
| 5 | 0.001953125 | 原十档全拒 | 2699.420576294654 | 0.9990830027422822 | 0.9999995107614288 | 1065.336943763 |
| 6 | 0.0009765625 | 原十档全拒 | 1351.0918895837697 | 0.9995416065232501 | 0.9999997553836197 | 1067.5332838610002 |
| 7 | 0.00048828125 | 原十档全拒 | 677.0568077768113 | 0.9997708295315719 | 0.9999998776925362 | 1064.894805075999 |
| 8 | 0.000244140625 | 未返回时规则中断 | 未知 | 未知 | 未知 | 未知 |

call1有5条 trace、没有 trial，真正 converged=true/residual0，并保存有限 checkpoint；没有完整 endpoint J 或 audit。原 meanSlope=0.08000000000000027、meanSecond=-1.866666666666673，两 mean corrections 为0。

call2至7各有6条已返回 trace：request、tangent_warm_predictor、GC、iteration、iteration:correction、failure。每次 correction 前完整基点 norm/minA/minD 已返回；接着十档全部原试探均失败，没有实际接受的 Newton 更新。原参数 requested_jacobian=false 控制的是返回 endpoint 响应需求，不代表求解内部省掉完整 withJ 基点。原源及记录明确保持该内部评价。

六个已返回请求的原 correction chartCondition 依次是：

| call | 原 chartCondition |
| ---: | ---: |
| 2 | 5.438385335052805e+38 |
| 3 | 6.332803662011075e+39 |
| 4 | 8.539925727143798e+39 |
| 5 | 5.3451023077393584e+42 |
| 6 | 6.382721432895355e+40 |
| 7 | 1.3286751539205313e+40 |

这些是当前原局部图形成的浮点读数，不是准确矩阵条件数的证明或完整两端系统的秩证书。

## 319.5 全部60条原试探与定位的边界

六个正高度返回的每个原 trial 编号都完整为0–9，原 step 顺序都为：

[1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125]

全部60条均为 momentum-guard-rejection，原错误是 Error: momentum branch D/S/A rejected，全部位置都是 stage=0、rawCell=0、rawSegment=8。原 baseNorm 分别保持上表对应请求的 iteration0 norm，未把不同高度模型的 norm 相减作下降量。

原事件没有给出该失败角点的实际半径、角度和单独 D/S/A 值，不能从 stage或原件名字推算后填。本文既没有把“首段域拒”说成入口初值未能形成，也没有把浮点误差、warm、局部图逆或某一种域量唯一认定为原因。真实事实是：完整基点评价有限，原校正后的全部十个候选在同一被定位的首段失域。

整个原 trace 文件报告45条，trial文件报告60条；七个已返回事件完整带出了本节所用的对应记录。未返回call8的后续行为没有从这些总数中补造，未取得其完整响应就不宣称该请求最终 norm、接受或数学拒绝。

## 319.6 warm指标、接受父与不能作出的归因

六个正高度返回都记录使用 full-nonlinear-shooting-tangent-warm，没有对应 fallback 事件。其原 maxChartCondition 都是 3.8563941311926324e20；原 maxRelativeCorrection 依次为：

[4.265683037870289e251, 2.1328415189351446e251, 1.0664207594675723e251, 5.3321037973378615e250, 2.6660518986689307e250, 1.3330259493344654e250]

这些数不能被称为绝对坐标位移。与 R315 相同的固定原源用 $\max(10^{-250},\max_j|\mathrm{oldnode}_j|)$ 作相对分母；零父状态可使分母极小。小分母与数值巨大同时成立，既不证明绝对状态爆炸，也不证明候选有效。

原 worker 只在 sol.converged 后更新 last。六次返回均未收敛，原Python cache未变，last_converged_s始终为0、last_converged_call为1；失败 checkpoint 不被晋升为接受父。因而这些请求仍围绕原真实零高度接受父继续，不是沿六个失败状态构成了新的接受链。

这并不让warm自动免于数值责任。只是warm与后续原局部图校正共处同一调用，在没有独立改变其中一项的实际实验前，不能唯一归因。保当前完整 H/states/fresh J 后改完整 cut+stage+far 的 R273 链QR候选，是针对校正形成的明确下一实验；145将先保原warm与124六参数配方，保全部原十档 noJ、D/S/A、严格范数下降及最终阈值，不把本次九参数换入该不同身份。

## 319.7 原前置域、完整最终门与未启动范围

原 RMS preflight 对两个原 fraction 0.17267316464601146、0.8273268353539885 各检查698点，无 invalid，没有添加节点，原699节点全部保留。原 node/midpoint/两fraction minimum beta squared 分别为：

- node：0.00480519514864175；
- midpoint：0.004807080968456279；
- fraction0.17267316464601146：0.004808265275812018；
- fraction0.8273268353539885：0.00480589332770498。

这些是原已有有限检查，不能外推成全域正性、全部空间/相位的严格界或闭面reach。原preflight完整通过没有覆盖随后新的native试探。

原 outer_iterations=8，原内层17试探，native max_iterations=32、每次10试探；collocation tolerance为1e-6、boundary tolerance为1e-11、native tolerance为2e-9、boundary FD tolerance为5e-5。本次没有改这些阈值，也没有到达非零场验收入口：boundary_FD、original_full_DN、accepted_result均null，outer Newton及banded solve返回列表均空。

原有限尾 checkpoint 的 scope 本身说明远端Robin不是准确旋转collar；因此连零高度收敛都不单独给出原连续无限尾、准确闭合或最终几何审计。所有README指标继续未完成。

## 319.8 中断来自实际规则变化

原process记录：

- phase=external-interruption-partial；
- elapsed_seconds=8124.568825915；
- scientific_wall_clock_seconds=18000；
- scientific_child_returncode=-15，wrapper_returncode=143；
- external_signal=15，budget_exhausted=false。

原规则runner从10:02:19 UTC到12:17:44 UTC，science_returncode=143、wrapper_returncode=77，science_terminated_for_actual_rule_change=true。它启动4轮同步、前三轮完成，最后一轮实际pull后检测README变化；不是300分钟预算耗尽，也不是把墙钟停止改成数学拒绝。

| 已完成规则轮 | 实际读取main | 记录提交 |
| --- | --- | --- |
| 0 / 10:02:19 UTC | ff7a87e52618f9bc12c59a9f9a410343dfacde99 | 457cfe15e14e7a176629fc2bf2e22d17d003e979 |
| 1 / 10:47:22 UTC | c9fab81cb3b0d02016a9df4a28651d0f96377df9 | e953335cc49c282de46bbaa832e6872b6c65188c |
| 2 / 11:32:25 UTC | ecb7a94ef80b0d3593b5306d507778a0ded938bc | d830399a8fe7c918745debd8ed6f320974775ff5 |

第3轮12:17:44 UTC原error为 Root/topic README changed after actual pull; coordinator must read retained diff。其结果560 B / 84135ef1c5920f707594d4233736223b8624431dda63f832a49a67baef6a2feb。原scientific_checkout_modified=false，原argv和预算保持；没有绕过监控或代写确认。

这里叙述的是Actions真实pull，不是root故障期间的API读取。root已在后继工作中依新README继续；没有因此修改已完成的128身份。

## 319.9 来源与临时原件身份

原请求绑定110项source；记录的source manifest为12078 B / 78ed424d4fd1f222e1801adacb6ecaac44a5cd6adf7603a6117bdf1ad5b4a783。关键入口如下；这只是原Actions来源读回，不声称本地又独立遍历全部110源。

| 固定源 | 字节 | SHA-256 |
| --- | ---: | --- |
| exact_20261114_true_tail_client.py | 19526 | 1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09 |
| geometry_20261115_nine_control_height_continuation_full112.py | 46089 | 0433e1014a4d55ca52554ec5b17e9afa1d01a3b8e376d2afda890b26c35aa924 |
| geometry_20261115_original_tail_height_path.py | 23078 | e830a1679908cdc0cdd8c1ecd5663bbf6b82b24a3d52e44cf678aedc227eee48 |
| geometry_20261115_small_core_nine_control_family.py | 44390 | 086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629 |
| root_20261114_current576_rules_runner.py | 32654 | 3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde |
| root_20261115_nine_control_height_path_run.py | 9687 | d075af46b0dc57aafa4b484eee292e309fcd83adcd95e7c0a30a2a534e770d5e |
| root_20261115_nine_control_height_path_scalar_readout.py | 26840 | c756ede79cba7a4490f97801e8afe31e51e373a5e0946df89c7ab0f489ec2427 |

原 accepted96、prepared112、zero anchor、config依次保持 b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff、0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714、e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51、01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5。

原client来源描述14376 B / 76b08ee5b86bc08a850c5ac1239420d0d508fd4e90c60e1a793e8bbca08d9b53，配置描述1493 B / 1be36732a1cab0ff4d93be6d1a10b016628599ac2a123cd51b1aefcf087299c7；七次返回均保存同一身份。原context canonical JSON7151 B / f4f5dbcfbdcfbf483a2c8e6bb2184eeb0aaf19028bc247435d3b20610149b770。JSON身份和原二进制数组身份是不同对象，不混称逐字浮点checkpoint相同。

下表是原reader已经记录的文件身份。本地没有下载这些已清理原件或独立重算其完整数值：

| job内原件 | 原字节 | 原SHA-256 |
| --- | ---: | --- |
| process-status.json | 2847 | 375844b59743a453c53f64a59753a71c9efdcfda0ea800b490c0adb7e3be02ab |
| science/adapter-status.json | 16693 | 0dd2fe82d78c39f4548914e562826ee04da807e42ecb4c70c1383c9e90ba12af |
| science/initial-guess/prepared.json.gz | 2472318 | a2def5fa61f37352860c5969234b73beec97cc77fe45f89e664555cff84a0be3 |
| science/height-path/height-path-status.json | 74744 | f60739ad11a025991fcfccbd8ec474ec128ca736161370eb7c4d3b994de932a0 |
| science/height-path/height-path-input-binding.json | 47993 | 69261ced18ff46499239608b7be2de963c8092eb1552c4b5fed302a4590431d6 |
| science/initial-guess/RMS-domain-preflight.json | 1515 | 9026db4165475a76068d8ac291deae75fdb918b5619ca5a8980b9b21e3df09af |
| science-stdout-stderr.log | 79265 | d9f79d1eb12a79d0f13d9b73ca93684029d11ac13e41b6756885fd0ece47c2da |
| science/full-DN/true-tail_0001.json.gz | 9218 | 94e6787b8547c3c71d45311e3c678cc8b5d05b5aff9f61661ede1aeb55d5f0e0 |
| science/full-DN/true-tail_0002.json.gz | 1197273 | fd217ed8ad8e7450a5507fd8638e55b8885447e6a720b7beb01b30c7e588531d |
| science/full-DN/true-tail_0003.json.gz | 1196717 | ed24b21655dd19f1eb649dfbcf4fea1d8dee2f41215a8a631b5e89fc9a19a68a |
| science/full-DN/true-tail_0004.json.gz | 1195910 | 273bb2a48fdf259ff12bb68c61acb462748fb374e35d996b5c917ea57bd6d725 |
| science/full-DN/true-tail_0005.json.gz | 1195573 | 474bfbf9436ca355d55081c02bf05f3db582e38b53dfe7690346db1ef9db11d2 |
| science/full-DN/true-tail_0006.json.gz | 1195388 | 70fde32d3562b01795d45e75abeb3fd5ce70da124c4cfd2f019bfaf5c39be055 |
| science/full-DN/true-tail_0007.json.gz | 1194530 | b4f05d035c00b3542609d7ede2dd67cb9a522f0a3fa4312319d9f6cdf65a1fef |
| science/full-DN/true-tail_ready.json.gz | 6857 | 821483d479921c2c7fb244aed63b73d3d937362e4ac64ff9d2479db533505c1a |
| science/full-DN/true-tail_trace.jsonl | 27725 | 83e16e3046ca98b320c3783084e156402e2581d528d5649c292fdbc2aefa9591 |
| science/full-DN/true-tail_trials.jsonl | 13874 | b72405a418ea4ccaf19c37f73a85cdaa6b5c5e275b8079465e11ba55388c0f68 |

原最后事件为 request128_owned_temporary_payload_removed，no_artifact_release_or_git_raw_upload=true。规则runner自己保留partial现场供readout与workflow随后清理并不矛盾。后继需要数据时须按真实来源重做，不能将这里的SHA当成仍可恢复的场。

## 319.10 对当前后继的具体影响

本结果结清了128已经观察到的全部路径请求、六份完整原试探轨迹及真实中断。它支持对校正形成作独立且完整的修改，不能支持继续盲目二分相同失域步骤，也不支持降低模态、去掉高109/两mean、换零H或放宽原门。

145以其明确六参数来源形成当前H下的全576段、577节点、全部129248行R273两端系统，原有限J可作为该候选的实际输入；当前完整非线性函数与原十档接受必须重新实测。140的真实128现场、全224方向、112边界及338/final audit另行继续。连续C有限头与新连续标量模型仍是独立数学对象；本次旧有限族失败不自动消除或支付它们的责任。
