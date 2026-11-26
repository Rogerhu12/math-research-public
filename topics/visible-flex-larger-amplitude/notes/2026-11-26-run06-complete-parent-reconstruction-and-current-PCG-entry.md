# 第六次公开运行：完整再生父点与历史，再接当前八列PCG

本入口的目的，是在原run04被取消且第四方向未完整返回后，继续原完整归一化SO3问题，并启用已刊的当前八列全空间PCG机制。课题未完成；本次重建、job结束或单方向接受都不构成完成。提交请求和workflow后由push事件触发，本文不预填尚未取得的run编号或实际新结果。

## 1. 原运行的实际边界

[run04终态完整记录](2026-11-26-run04-terminal-job-with-admitted-pair-unreturned.md)保留job140038237351在22:07:10 UTC实际completed/cancelled、科学step5 cancelled，以及21:49:59索引明确已启动原完整pair的事实。根另实际读取steps API得到同一取消状态。最后完整科学父仍是实际48的a801，实际49为其完整纯归因；没有第50项完整返回、没有新Phi/地点/末场或pure已执行证据。无完整返回不等于无文件或无地点，未从旧a801捏造第四方向结论。

## 2. 公开执行及完整输入重建

公开workflow为 `.github/workflows/visible-larger-normalized-parent-20261126-06.yml`；这是根README授权所需的题目外工作流编辑，已记入本题log。只在本题request06路径push时触发，另保workflow_dispatch；350分钟原job边界、独立concurrency组、CPU float64 torch2.5.1、Python3.12.14、NumPy2.3.5、SciPy1.17.0和单BLAS线程。workflow字节身份为 2241B / `6b85966301eeb5065e139f4da6a6f3f02f0ea88963a201393408619e9de5951c`。

原完整 `rebuild_a04_chain.py --stop-after continue`先再生原28阶段，源SHA256 `8f68c4995535420e269760cd709178ca0d618eac1dc743c1f076399a6a30660d`。随后执行独立queue06的完整十二对象，覆盖原run04实际29–40，不能从输出SHA恢复raw。queue的`finish_when_done=false`，因此父点重建结束后继续消费明确追加的新工作。所有科学数组、报告、缓存和完整日志只留runner临时目录；本次无旧raw跨run传递，也不存Git/Release/artifact。

新controller19006B相对原parallel04的完整源码只把04 HANDOFF槽与可见标签改为06；原分卷58/60KB界、索引95KB、H10KB、题200MB、规则变化即停止继续计算并报告完整diff，以及非快进立即pull/rebase循环全部保留。完整followup控制器SHA256 `3cb1e706ab43dac6e952ce00b41e83055112d2ee65edb37682d1f05e94f2ee3f`；新入口不削减任何已有检查或科学步骤。

## 3. 十二对象逐项完整对应

[全对象对应元数据](../computations/resume-20261126-run06-bootstrap-twelve-object-correspondence.json)给准确原queue blob939929d、93272B及SHA86c0bfbf、每个完整原/新对象SHA与上游02来源。根独立读取已知小于100KB的该blob，逐JSON值比较全部十二对象：仅`id`、`scope`与新增`reconstruction_source`有变化，`script`、全部args、父输入、output、summary、cleanup和原`reconstruction_origin`全部相同。没有只比较数量或参数子集。

| 新queue索引 | 原04实际阶段 | 完整步骤 |
|---|---:|---|
| 0 | 29 | 全witness manifest整理 |
| 1 | 30 | R671完整角目标与实际μ |
| 2 | 31 | 原v3完整角续算 |
| 3 | 32 | R684完整新physical mean目标 |
| 4 | 33 | R688原face PCG |
| 5 | 34 | 完整幅度观察 |
| 6 | 35 | 原幅度保护首入口及其实际失败责任 |
| 7 | 36 | 完整v2幅度保护 |
| 8 | 37 | 原固定deep scalar准备 |
| 9 | 38 | 完整deep scalar首方向 |
| 10 | 39 | 完整原SO3 actual profile |
| 11 | 40 | 完整SO3内部可行父恢复 |

第35阶段的既有失败路径没有因结果已知而被删；其恢复依赖及原continue策略完整保留。本次重建是获得当前runner可实际读的输入，不重复登记旧结论，不预称逐字与旧run相同。

## 4. 当前PCG的后续责任

已刊[完整五源接线](2026-11-26-current-SO3-eight-column-PCG-complete-source-integration.md)保全1333370自由变量、当前8A+8A*、全部曲率/半径约束、原μ²I、原Phase I、完整后退SOC和最终永久memory复读。新的预条件器只作用于原同一QP的推进，不改变目标、范数、有限几何筛或停止规则。

完整历史续算准备包含原44、46、48与完整第四方向的源/参数，须在该runner实际完成父上运行。新第四report是新run自身的实际记录，不能冒原50成功或其raw副本。相同命令、网格规模或计数不证明跨run选择和地点逐字相同；全部适用原历史、typed/protected角色和最终memory重读仍必须保留。新PCG入口在当前runner实际完整第四父、真实输出身份和其实际最终μ上绑定，不从旧a801候选直接跳过责任。

本次初始queue只装载已完整核对的十二父重建对象；完成返回后按完整实际证据归档该run已完成对象，追加完整历史再生和新PCG对象，活动queue仍低于95KB。未返回步骤不归档冒完成，不以长期重建本身替代新的科学推进。

## 5. 时间元数据与限制

[原实际时长元数据](../computations/resume-20261126-run06-actual-duration-metadata.json)逐项引用原run04五个小卷与全部40子进程时长。原1–40合计8693.365913540001秒；再计原44/46/48为14736.616238907001秒。若新第四方向耗时仅类似原48，说明性合计为16780.945279242秒。这里没有包括启动、发布、空闲等待或新预条件器准备费用，也没有任何时长或及时返回保证。控制器新准入预算20000秒与job21000秒边界均不延长，不当作研究停止理由。

## 6. 完整提交文件

| 文件 | UTF8字节 | SHA256 |
|---|---:|---|
| `scripts/resume_20261126/public_actions_controller_parallel06_compact_metadata.py` | 19006 | `acff1a861a5e080fc014627b8021ff40c4fa9848e36ebfec91c4e5b49e1b256f` |
| `computations/resume-20261126-actions-request-06.json` | 2860 | `7c3772c745bd1349d735aef42b344fe42f48a00b5a41ffdc3d47be68a3189700` |
| `computations/resume-20261126-followups-06.json` | 76950 | `88681682ff4865d4f15d6585f312314a4d48acf044b970b9c6d768c258e9a8c9` |
| `computations/resume-20261126-run06-bootstrap-twelve-object-correspondence.json` | 15599 | `87cb13247941a744861d904bc774d2accd2f0557f320727c5ca28c01d67ada2f` |
| `computations/resume-20261126-run06-actual-duration-metadata.json` | 6604 | `ae56adbf2e4e4c457a240067d642cc51807cb9389694e32a4177f286d7fe3ec3` |

全部新源只作静态编译、文件身份和完整JSON/argv对应核查；未在本地执行科学模块。真实新run编号、源码提交、实际报告SHA与紧凑结果由独立06槽和公开分卷持续登记。准确连续度量、全t几何及同固定问题真实精化仍待完成。
