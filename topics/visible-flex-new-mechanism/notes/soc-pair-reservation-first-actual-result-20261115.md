# SOC 配对机会预留：首次公开实际结果

日期：2026-11-15。责任：tail_cost 读取一次已完成公共 Actions 原日志、逐模型消费；root 独立核读并负责发布。本文没有运行本地人工、求解、科学计算或旧阶段复验。原日志、完整状态、矩阵和可重算 payload 不写入仓库或 Release。

## 1. 本轮完成了什么

本轮从上一真正最优 checkpoint 出发，执行一次新策略 continuation：

- run **43758666042**，job **132948276657**。
- 计算 source **aca67097b60b7eacdcf20798395ce6d4d1ab2845**。
- workflow：.github/workflows/visible-soc-pair-reservation.yml。
- policy：same159-twelve-LP-primary-SOC-pair-reservation-v1。
- 最终状态：complete-two-grid-primary-SOC-pair-reservation-audit。
- stage：new-pair-reservation-stopped-before-unpaired-primary；没有 error 或预算异常。

七个主模型各有一个实际 full-step trial，全部接受，未回溯。两网最大真实 \(\eta\) 从 **0.26632415509189855** 降到 **0.2663015219132816**，报告下降 **0.00002263317861694869**。最终两网最大绝对主曲率 **57.999987361173226**，原采样硬门、旧 metric 资格、原精确物理盒及独立末两网复核均通过。

实际启动 **11 个 primary LP，0 个 SOC LP，0 个 nonlinear optimizer**。新策略最后保留 **1 个未用 LP**，随后不启动没有配对余量的新 primary。原共享总额12并未耗尽。七次 trial 都有资源意义的 SOC 机会，但普通步均已直接满足真实验收，故没有进入 SOC。不能据本轮宣称预留带来了 SOC 接受、半径保持或收敛改善。

第七模型确实触及新的 primary 局部配额，返回一个按冻结原逻辑修正 \(\rho\)、重新检查全部最终 cuts 的 inexact incumbent。它没有被标成 gap 收敛，却通过实际两网验收。这是本轮实际走到的新配额分支。

公开入口：[run](https://github.com/Rogerhu12/math-research-public/actions/runs/43758666042)、[job](https://github.com/Rogerhu12/math-research-public/actions/runs/43758666042/job/132948276657)。

## 2. 真正最优输入与未重复工作

输入来自 run **43753280651** / job **132931742484** / source **52a48854e30ddc3d2351ec24274dbe222ef05d9a** 的完整 future_direct_checkpoint：

| 输入身份 | 本轮准确恢复 |
|---|---|
| physical state SHA256 | 1275ae1da1bdf0779ff143e90b7177613b8011aa56a1781e3c31363ba1996be7 |
| 原 reference163、independent159、physical163 | 原精确有理文本；不重建 reference、不裁剪、不投影、不舍入九个从属 height 系数 |
| coordinate SHA256 | b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580 |
| source configuration SHA256 | b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6 |
| 完整 coarse/fine 有序行池 | 4419 / 4277 |
| norm bank | 22 个原有序 entries |
| bank state SHA256 | c952c53a45396f3cdfef89853eb856ffa26f45089703a884e63c1a57956d97f9 |
| 终端 controller | \(B=0.000125\)，success streak 0 |

来源原日志3,366,573 bytes / SHA256 **5215dbbd84e122f445ad188168b8a72f7316e0cd31e4b5bfdcfb1f42f1b25b3a**；来源 COMPLETE JSON+LF 895,932 bytes / **834cd800038c9d93f5619f17b2c901ee2085633e4393591cd41ebf3e915aef9c**。

原125脚本 closure 逐项匹配。本轮没有调用旧 optimizer、任何旧恢复 prefix、历史 m10 trial 或旧开发套件。旧 expanded10、m10七例、cache正负两例、上一4组26checks按已付日志及源SHA复用，执行次数均为零。已有 cache 证据从来源日志 receipt 读取，没有另取旧 m10 大日志。

完整有序 bank 直接恢复，**不重播插入事件、不重算原normal、不携带旧numeric A/b**。首次 current complete model 建成、原context真正绑定后，entries=22及原bank hash再次核对通过。原 \(g,b_0,H\)、reference和source cfg未变。

同一精确状态重新普通评价时，初始coarse/fine \(\eta\) 差均为零；coarse曲率差为零，fine曲率差为 \(2.1316282072803006\times10^{-14}\)。不能写成所有普通浮点量逐bit相同；精确坐标和reference的恢复仍完全相同。

## 3. 仅新增的四组开发检查

SOC_PAIR_DEVELOPMENT 的 all_passed=true、passed=true，四组共有 **19条命名检查**：

| 新组 | checks | 实际结果 |
|---|---:|---|
| deterministic_twelve_LP_allocation | 5 | 全真；其中遍历remaining=0…12的13个整数预算 |
| scoped_frozen_repaired_incumbent_driver | 6 | 全真 |
| reserved_SOC_charge_and_exception_scope | 4 | 全真 |
| twenty_two_entry_checkpoint_and_explicit_entry | 4 | 全真 |

仅支付新allocation、局部cfg scope、原incumbent修正／strict-tie行为、SOC启动前收费／异常scope、22-entry输入和显式接线。人工回调成功不是HiGHS或科学成功。开发报告准确记 geometry_calls=0、optimizer_calls=0、scientific_inputs=0、old_developer_suite_executions=0。

随后实际科学只启动一次，保原共享 **12 LP / 40 values / 120 active seconds / 单LP至多10 seconds**。新策略未修改原gates、容差、物理盒、metric/curvature RHS或旧controller fallback。

## 4. 七个真实模型

\(\eta,\kappa\) 均取实际两网最大值；“新增行”是实际learning的coarse/fine行数。全部是首个 \(\alpha=1\) 普通步，全部接受，omitted hard rows两网全为0。\(B\) 始终0.000125。

| 模型 | primary授予上限 | 实际primary LP | primary后共享余量 | 实际最大\(\eta\) | 实际最大\(\kappa\) | 完整模型实际／预测比 | 新增行C/F | 返回candidate gap达标 |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 3 | 2 | 10 | 0.2663204237346921 | 57.99998579746462 | 0.988581909 | 5/1 | 是 |
| 2 | 3 | 2 | 8 | 0.2663174850983704 | 57.999992670799976 | 0.863831201 | 5/0 | 是 |
| 3 | 3 | 3 | 5 | 0.26631415789537666 | 57.99999283820269 | 0.896660822 | 1/0 | 是 |
| 4 | 3 | 1 | 4 | 0.2663110542028495 | 57.99998709342469 | 0.901982680 | 0/0 | 是 |
| 5 | 2 | 1 | 3 | 0.2663079209427961 | 57.99998540895771 | 0.883829538 | 1/0 | 是 |
| 6 | 1 | 1 | 2 | 0.2663043726732029 | 57.99998616638334 | 0.997710827 | 1/0 | 是 |
| 7 | 1 | 1 | 1 | 0.2663015219132816 | 57.999987361173226 | 0.926571850 | 0/0 | 否；原修正候选 |

每个primary使用scoped cfg copy；所有模型记录scope关闭、source cfg hash不变、outer/SOC全局limit仍12。没有虚拟收费或重置shared ledger。

模型1—6停止标签为 evaluated-affine-epigraph-gap-met。模型7准确标为 new-pair-allocation-primary-ceiling-reached，同时保留冻结solver的 original-shared-LP-budget-after-inner-call 作为inherited记录，并明确**它是在新局部上限中返回，不是原12额度耗尽**。

模型7关键值：

- 第11个共享LP；原HiGHS status0、finite primal success。
- evaluated affine slack / repaired \(\rho=0.006301295998768608\)。
- 原LP relaxation slack \(0.00630087697620446\)。
- raw epigraph gap \(4.1902256414823313\times10^{-7}\)，tolerance \(3.8458430429849644\times10^{-7}\)，所以gap=false。
- repaired objective \(0.006301420998768608\)，returned_inexact_cut_model=true。
- 全部最终原单位row violation \(2.4669834588781497\times10^{-20}\)，bound violation0。
- 实际两网最大 \(\eta=0.2663015219132816\)，full step真接受。

\(\rho\)、repaired objective和真实\(\eta\)是不同量，不能互换。这些浮点核不授区间证书或严格凸最优性。

## 5. 额度、SOC和继承hold

primary实际消耗 **2,2,3,1,1,1,1**。启动前余量 **12,10,8,5,4,3,2**，授予上限 **3,3,3,3,2,1,1**，primary后余量 **10,8,5,4,3,2,1**。

七个trial的 original_may_SOC_resource_and_no_prior_arc_condition=true，仅表示资源和无prior arc条件满足。它不表示原失败种类或接受逻辑要求启动SOC；这里普通trial均先接受。

| 观察 | 数量 |
|---|---:|
| 资源意义SOC机会 | 7 |
| SOC LP真启动 | 0 |
| accepted corrected / parabolic trial | 0 / 0 |
| accepted expanded-pool SOC | 0 |
| 继承covered-layout hold获准 | 0 |
| hold后B被下模型使用 | 0 |
| 最后未用LP | 1 |
| 因新no-unpaired规则未用 | 1 |

本轮有配额执行证据，尤其m7的inexact incumbent和末端停机；没有SOC收益证据。停止后不重跑本阶段等待SOC，不为用满第12个LP修改已冻规则。

## 6. 行池与bank完整分账

来源完整行池4419/4277保留。原初始化后的首主模型池是 **4419/4357**，fine比输入多80；这是已报告初始化后布局与seed布局的区别，不能写成丢失或替换输入行。七步后续实际增加coarse13、fine1，终态 **4432/4358**。

最终原pool metadata的行序hash：

- coarse row_indices_sha256 **2960646cf6cb902c0bd7a7169b969289d2b2209b88405c517df5998f5da938b4**，version6。
- fine row_indices_sha256 **75752f6b96a268594f2cd7312d57c8c801e5ef0fa4b2245bf34c6433070ccb1d**，version3。

这是原行序hash域，不与checkpoint JSON序列化hash混称。新runtime版本由真实set_pool调用产生；来源终端版本2/5继续作为来源保留。容量及原全部gates未变。

bank首次准确恢复22个，最终 **59个**；eviction0，报告insertion120、binary64 inward adjustment47。insertion包含真实更新，不能等同于新增独立entry。最终bank hash：

**24cc1f35aca23a584999ff7544b4e961a0fad24e78270fa13aac3f65c9053c50**。

各模型在新current center重建的memory支撑行分别 **22,56,59,59,59,59,59**，合计373次行装配。本轮真正新增supporting cuts是 **45,4,8,1**，共58条，分布在m1、m2、m3。原total_new_cut_rows合计431，**其中含373条重建memory行**，不能全称为新学习cuts。没有复用旧numeric A/b。

最后checkpoint完整保reference163、exact159、physical163、两完整有序池、59个有序bank entries/context、\(B=0.000125\)、streak1。最终physical SHA：

**0c1d344dab070999d503e79243f2b946662f590f76f9dbffea8b97cbf56a9ad2**。

## 7. 独立末两网门及未完成目标

| 末态量 | coarse384 | fine768 |
|---|---:|---:|
| 真实\(\eta_{\max}\) | 0.2663015219132816 | 0.2663015217864424 |
| 绝对主曲率最大值 | 57.99996709608351 | 57.999987361173226 |
| inner strip绝对余量 | 1.7794566598006156e−7 | 4.011143595050726e−8 |
| ball归一半径平方最大值 | 0.9905480867122076 | 0.9905480867569343 |
| finite mirror半径最小值 | 0.10056269375392417 | 0.10056269375438749 |
| 最小signed height | 0.02 | 0.02 |
| 原硬门及旧metric资格 | 通过 | 通过 |

原163 coupled physical box精确核，violation=0，不以159坐标外包替代。exact total cap integral change=0，物理height \(c_4,c_5\)完全不变。fixed support仍按原两网replay。

cap affine margin \(-2.7755575615628914\times10^{-17}\)，reconstructed margin \(-5.551115123125783\times10^{-17}\)，在原height tolerance \(10^{-9}\)、reconstruction consistency tolerance \(10^{-10}\)下通过；不能写成两个margin在浮点中均非负。

曲率四条scaled PSD行、固定curvature auxiliary \(\lambda\simeq58,\zeta=0.58\)、独立direct curvature、signed height、inner/outer strip、ball、mirror、regularity和旧metric budget按原判据通过。旧metric auxiliary不改作曲率变量。

新\(\eta\)目标 \(13/50=0.26\)未达，末最大超额约0.00630152。目标局部曲率 \(1/(61/1000)=16.39344262295082\)也未达。本结果仅原384/768采样上的continuation，不授连续metric、embedding或whole-surface reach证书。

## 8. 真实费用与计时边界

| 原报告边界 | 秒 |
|---|---:|
| 输入读取／精确转移prepare | 9.947075298999998 |
| audit elapsed | 162.276634749 |
| process total elapsed | 172.223713764 |
| 初始ordinary audit、进入recovery wall前 | 112.61073857199999 |
| recovery wall，含active clock前首J | 48.46838217200002 |
| 原共享optimization active | 29.468092885000004 |
| 独立末coarse/fine/comparison | 0.259811805 / 0.485277241 / 0.065970980 |

边界不同且部分嵌套，不能加总成另一种总费用，也不能把112.61秒全部归到未经单独计时的函数。原共享active未触120秒。

报告full-value计数：共享初始化／trial **16**，独立末同态两网 **2**，合计计数 **18**；没有SOC值调用或旧optimizer，shared cap40不变。

- 11个inner LP entry的elapsed合计 **3.7141171970000073秒**，不是含所有建模/oracle费用的总时长。
- selected J：coarse **6.992661596999994秒**、fine **19.42456353299994秒**，各7次refresh；新selected路径原full163 J batch仍为0。
- complete affine direction：18次新方向评价、36次单网扫描、25次缓存复用；报告 **10.000441811999906秒**。
- 新增原metric row-J请求24次，报告 **0.3953049429999851秒**。
- RSS peak **2,343,720 KiB = 2288.7890625 MiB**。

只描述本轮已经发生的工作；未作旧策略反事实重跑，未宣称跨run因果加速。

## 9. 源、规则读取与输出身份

请求原文 **33,631 bytes** / SHA256 **4ac9b699a252931fe29a209b17ba579055a9ad401d0af88a5b95a65b4caf02fb**。

134项source binding=130脚本＋4 workflow。DEV和actual均报告130脚本；按topic/scripts前缀规范化后，全部与请求相同，DEV与actual也全部相同。五新源：

| 文件 | SHA256 |
|---|---|
| scripts/frame_metric_soc_pair_reservation.py | 1b89f9a36a2ca9ec6cc3b85d907b6cf899300d9629c53eb3fe880fa10562c27b |
| scripts/frame_metric_soc_pair_reservation_recovery.py | 25e64f68c506829b19a37f44a0581a06f16b4886cd0acfee433fcadbe460e6aa |
| scripts/frame_metric_soc_pair_reservation_development.py | 17b3021ece71250e95e272f6e2264a1a1d16b1436ea6425b4d44294c50a4080c |
| scripts/frame_metric_soc_pair_reservation_transfer.py | 70830e4e2d0d22055c7a0236c9f5132a8dd270f7aaa79dd3ff8c3ffdbfb90bdf |
| scripts/frame_metric_soc_pair_reservation_audit.py | ad997754683659231e4f8a1ae378f53d1077a77158bf63c635c25a5c516e9aad |

新workflow SHA256 **a43d55b3ce131921fa33647388f6f185a8ac2f1e03f81731212f0cddc1a273a1**；旧三个workflow按请求原值绑定。唯一push触发，没有额外dispatch、rerun或备用科学。

public actualpull完成 **2026-11-15 20:32:58.355408 UTC**，readSHA同source aca67097…。根README blob **21bd547f56590b7f2dd279d0297efb289a9b2783**，topicREADME blob **d0432faff569c8e9af7ed4809847e12880976c11**，两diff空。

private actualpull完成 **20:33:02.572077 UTC**，readSHA **43dbc0b185aad941d3d59218dd4f505c24d4c818**；规则与已记录值一致，QUEUE为本会话唯一ongoing。没有公开private内容。

JSON行去GitHub timestamp/tag后保原JSON字符再接LF；下表不是重新排序JSON后的hash。

| 已付对象 | bytes | SHA256 |
|---|---:|---|
| 完整原job log，含BOM/timestamps | 3729117 | 0260f3a8d1233afbdad4227ae5260ae5956bcd58c0cea6dd53e2f399ea3409c9 |
| SOC_PAIR_PRIOR_WORK_REUSED JSON+LF | 8606 | afbea311356d9b476f5fe0fabf511d6634a1bfbb3e8dc854938de7b9b4ae8d32 |
| SOC_PAIR_DEVELOPMENT JSON+LF | 45342 | f8eab10dd3840abfe7883647d643cc6dd9f17eba893b5d1e6e382b73795e5da4 |
| SOC_PAIR_COMPLETE JSON+LF | 951619 | b12af5a0b05735260db68162a3f6879d151ca939afca5abed1ea7e4505b168c8 |
| runner临时audit-summary.json | 1454240 | de4a83949be64d72478abd17acc6fbf7b7073d8e2415721c21959caad7ff72d8 |
| runner临时audit.json | 15627227 | 90f83097002e3d5c1b219ca15503d35aab25102cd82893834a7548edc68941af |

临时文件两行来自真实SOC_PAIR_OUTPUT_METADATA，payload_committed_or_uploaded=false。本文仅人类结论、源／参数／run／hash；可重算数据未保存到仓库或Release。

## 10. 下一真正新子问题

本轮没有失败trial供新SOC处理，不能为观察预留效果重播七模型或增加预算。

原报告已有另一条准确限制：m1、m2、m3、m5、m6的旧conservative-growth检查中，**唯一false都是no_new_coarse_or_fine_rows**。新增均soft metric witness；omitted hard rows两网全0。实际用原半径、first full primary接受、全两网门、无SOC/回溯、无shrink、高完整模型比值，其余条件全部true。m4/m7没有新行，均合格但各只积到streak1；m5的soft学习重置中间streak，最后B仍0.000125。

下一可研究的对象是：原完整两网affine-\(e/f\)模型已覆盖这些soft函数、实际新行仅soft时，建立**另一个明确记录的新普通步growth资格**，保真实学习，不把soft pool插入自动等同于未覆盖hard约束。必须绑定同center、实际总步、complete模型及非零预测分母，保原收缩优先、新hard行reset、全部实际容差和12/40/120/10资源。这是待设计的新规则，不是本轮已实现或已验证的结论。

后继输入只能是本轮59-entry、4432/4358、B0.000125/streak1的真正最优checkpoint。单纯延长或重跑同阶段等SOC、重算旧checks、放宽hard门或扩大预算，均不是本稿结论。
