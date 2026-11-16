# R455 — Actual206 的八组真实39-query模型/FD与单份表格摘要超限

作者：ChatGPT（AI，exact_refinement）；2026-11-16。  
范围：实际公开Actions终态、原事件、冻结控制流与必要来源。没有本地科学执行、导入、AST、编译、fixture或数值重算。

## 455.1 结论：原八组已推进，必要正文仍未成功交付

Actual206 从原actual98的真实warm/status另起，执行了八组原39-query完整模型及每组新warm的原边界FD。全部16个子进程返回0；八份必要记录已写入本job临时目录；八次 `next_actual_parent_pair_retained` 都为 `true`。结合原worker实际分支，可确认八次单步optimization progress、原配对文件身份和本轮fresh FD门均已通过。

本次直接输出的原trial计数为 **4、3、4、3、3、2、2、3，共24条**。它们不是actual200的20条，也不能因总数碰巧等于另一个run就借用旧逐trial值。

全部八组之后，新的固定角色表摘要仍超过90,000字节界：

- 主 `whole-chain`：119,344字节 / `6204fe90ff336223346f6cd451a8a81c34fce76b77d949577eaf0f435274ef3e`；
- always `whole-chain-recovery`：119,694字节 / `984f24f8fe885d2fb24128d0e57efc7d1d8a325a094309a82f05b1e8965013f3`。

二者都是原ASCII JSON含末LF身份。两次都在BEGIN帧之前明确拒绝输出正文、`summary_complete=false`、返回70；没有分包、编码或截断后假成功。最后原owner已证静止，但cleanup因必要读回失败而真实跳过，保留尚存必要记录和末pair直到托管runner销毁。

所以本次支付了原八组执行及其控制流条件、24条计数、来源与失败定位；**没有支付24条trial的完整必要数值、所有失败query地址、逐组FD误差、末三参数和末pair对外可恢复性**。不能从摘要SHA补出这些值，不能把未来同方法新链回填为本次原轨迹。

## 455.2 官方运行、日志与来源

| 项 | 实际身份 |
|---|---|
| 仓库 | `Rogerhu12/math-research-public` |
| Run | `43797755759`，attempt1 |
| Source commit | `e8e4be9f5cd3885399453b8945ea750b1a365ce4` |
| Compute job | `133070353121`，completed/failure |
| Workflow | `visible-larger-public-thirty-nine-tabular-batches.yml` |
| 原规则runner区间 | 2026-11-16 03:22:28 UTC至04:59:58 UTC |
| 科学步骤 | failure，原最终exit70 |
| Always必要读回 | failure，同为exit70 |
| 原规则读回 | success |
| Cleanup步骤 | success，实际执行skip分支 |
| 独立report job | 此workflow没有该job |

官方来源：[actual206 run](https://github.com/Rogerhu12/math-research-public/actions/runs/43797755759)。

官方connector日志只取得一次。完整**解码字符串按UTF-8重编码**为96,615字节 / `38281084d8659ea74a5c11d39ef9c055e99710395296df43e7770d0546abdaf7`。这是connector返回身份，不是另行下载的HTTP原响应身份。

解析视图有619个split物理行，只剥1处真实行首BOM和614处锚定GitHub时间戳；原字符串不改。67个真实JSON事件逐原行加LF的元数据摘录是48,212字节 / `1255bfb2916397a331dfcd4b4389da79eee521f7a91d539945da9168950e1b6f`，保原数字字面。成功完整必要帧数为0；ANSI脚本回显中的BEGIN字符串不是真实帧。

本次入口和纯读回来源：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `root_20261116_thirty_nine_tabular_chain_readout.py` | 75,482 | `9840e9ae7c1219b9b3bbef45d4bacb7110f639e980f76a6d592eb9f96c9bb68f` |
| `geometry_20261116_thirty_nine_tabular_batches.py` | 29,658 | `59276c9eae96071211d8990a1b260faf0cc534e7efea3c4e9fd49a59213d7643` |
| `public-thirty-nine-tabular-model-recipe.json` | 34,102 | `2353548631ab0b7a6a67e25b2f1360c4b78066448df6b85cd0bff56e2b7868ab` |
| `public-thirty-nine-tabular-batch-request.json` | 17,310 | `056fc24b4eae26bf36dbc37f67b9c75ca79cdacc99617cbeb101e0990fae79ca` |
| workflow | 14,363 | `9a3b52bc27ea1b50af1997dbc9ad451f705b10802aec7a059275e8438668ad0e` |

[R454](R454-complete39-necessary-scalar-tables-and-single-readback.md)及[206接口](../notes/2026-11-16-request206-original39-eight-pairs-and-single-table-summary-interface.md)给出固定角色表、canonical相等才共享、原必要字段和唯一90KB合同。本次实际source-check确认106个原actual200来源保留，新增必要helper和独立worker，共108件显式源，参数manifest1件；科学阈值和原子预算未改。

## 455.3 原父、39集合、全响应支持及资源

首model真实命令使用原actual98父：

- warm SHA `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`；
- status SHA `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`；
- 当前job实际目录 `parent98`；没有从已删除的actual200末pair恢复；
- 本次 `necessary-input-binding.json` 为8,915字节 / `d3d9b457645ac1f3fda1b1908ceb671003fd04da368780ead6024020f63a77a6`，临时且不把大输入正文输出。

actual98原来源仍是request内完整冻结的run43677587785、artifact14147700690、commit `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`；本文没有重新下载该artifact或重算父场。

39集合保留原38并加入真正RIGHT-RMS459、fraction `0.8273268353539885`。实际source事件逐项记录：

- 端点集合为459、460、462至491，共32个；
- 26个唯一capture interval；
- local坐标10,819，C支持4,059；
- cover节点33，cover front维11,266，真实front维10,928；
- `free_node461_prefix_QR_not_zero_padded_B=true`。

461仍是完整原问题的自由变量，经[R407所刊适配源](../computations/root_20261115_noncontiguous_local_qp_condensation.py)的完整仿射QR责任消去；此处不从source标签声称本次读取了原大factor矩阵。

每组真实命令保留：

`iterations=1; damping=270; lsmr-iterations=200; projection-sweeps=200; line-search-steps=17; budget-seconds=1200; angles=4096; jac-workers=2; condensed-budget-seconds=600; condensed-trial-reserve-seconds=90; condensed-recovery-reserve-seconds=30; condensed-max-working=512; condensed-dual-sweeps=200; condensed-store-root`。

每次FD命令的prepared确为该批 `thirty-nine-condensed-warm/warm-001.json.gz`，angles仍4096。最多八组、原批间10,500秒、175分钟science步骤、195分钟job和10分钟必要读回没有扩大。这里本次终止原因是传输70，不是预算截止；不拿这些实耗时预测下一run速度。

## 455.4 八组真实执行范围和可推出的原条件

八组真实原事件：

| 批次 | 原trial计数 | model exit | FD exit | model原秒数 | FD原秒数 | next_actual_parent_pair_retained |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 4 | 0 | 0 | 710.965724485 | 22.627728733000026 | true |
| 1 | 3 | 0 | 0 | 699.362855127 | 22.326005956000017 | true |
| 2 | 4 | 0 | 0 | 693.2134776500002 | 22.239186233000055 | true |
| 3 | 3 | 0 | 0 | 692.5540151499999 | 22.500005836000128 | true |
| 4 | 3 | 0 | 0 | 704.8465937439996 | 22.455729041000268 | true |
| 5 | 2 | 0 | 0 | 703.1276427520002 | 22.55120098200041 | true |
| 6 | 2 | 0 | 0 | 689.11059269 | 22.552807703000326 | true |
| 7 | 3 | 0 | 0 | 717.3789065719993 | 22.504050102000292 | true |

以上24是八个原整数计数之和，时间逐值抄原事件。16个stderr均是0字节并保完整空串。model stdout各约151KB只留下原identity；FD stdout各176至178字节也只留下identity。没有转发这些正文，不能从子进程exit0单独推出它们内每个科学值。

但这里还有固定源码和原交接事件的联合证据：

1. `run_batch` 仅在model返回0、原status的 `optimization_progress is True` 且 `accepted_warm_steps == 1` 后调用真实pair验证。
2. 验证要求原optimizer schema、`success is False`、`new_coupled_finite_acceptance is False`、`latest_warm_file="warm-001.json.gz"`、SHA与status一致，以及warm producer和status身份逐键一致。
3. 之后才对这个新warm启动完整原FD。
4. `eligible` 仅在FD退出0、报告存在、原 `implementation_check_passed is True`、prepared SHA等于新warm SHA、`complete_current_warm_boundary_FD_actually_recomputed is True` 时成立。
5. 主循环先保存必要本地记录；仅当eligible才搬移真实pair并核移动前后身份相等，随后退休大batch。原 `next_actual_parent_pair_retained` 正是这个布尔值。

本次八个该值均真，故八组通过这些原progress、pair与freshFD条件。没有用读回helper另造科学门。原status的两项success=false仍保；八次进步不等于原native或新的coupled finite acceptance。

八组0至7均有完整返回事件，没有未启动的批次后缀；每组最多17档中的具体访问α、失败地址和未访后缀细节仍未对外读回。即便某组只有2条或3条，本文也不从计数推断是哪几个α。

## 455.5 保存过的必要记录与缺失正文

八份临时必要记录：

| 批次 | bytes | SHA256 |
|---:|---:|---|
| 0 | 30,390 | `4d4f2f4e1765e7567db5f32b3df945c930f1b0e26b8574258f4a624669b948fc` |
| 1 | 30,521 | `fccbf4aecc4a2548e5335637ba3bbb7412356bb08e4f2470bc66537d2e7248f3` |
| 2 | 33,966 | `d89c4b140100f3b9e4883da7b80d04188c69a8f917793b5be512820266d58728` |
| 3 | 29,623 | `7d47900abe7b9b677d0e5dc4c037543e11dc96b3cd753bf84d76157b074554c4` |
| 4 | 29,229 | `f6345f92cca754e0cb9664ffc22c1c324558e0f20db2efad5684a0b46501f934` |
| 5 | 25,942 | `7983d03719ae76705b91d4d8ee1b7fa41b5ed6a4aa312ded451b302e83bef15d` |
| 6 | 24,049 | `37302e3d0c048ab2de7c14544369a3f06c2cf2e0638b484c578b3d4da07121ae` |
| 7 | 29,863 | `dd5dc34f2ecc4dd3ad8f4ac23341a36c2ae94ab1d7983e1abf95d3d5e57df872` |

这些原事件明确 `scientific_stdout_not_emitted=true`、`whole_chain_stdout_readback_still_pending=true`。记录已在Actions本地形成，不代表已经完成对外必要读回。

所有八批的 `batch_payload_removed=true` 都发生在必要本地记录保存和真实pair搬移之后；这与整namespace主动清理是两层不同生命周期。原程序曾有这些必要正文，但本文没有取到它们，不能由上述摘要身份恢复其值。

最后主worker调用 `helper.finish_chain(work,final)`。该函数依次写state、读取八份必要记录和input binding、形成并写 `necessary-whole-chain.json`，再 `publish("whole-chain",report)`。本次实际traceback准确落在：

- worker第501行 `complete_readback=helper.finish_chain(work,final)`；
- helper第1284行 `return publish("whole-chain",report)`；
- helper第524行抛出 `ReadbackIncomplete`。

原最终错误：

> Necessary summary exceeds90000; preserve unread necessary records and surviving raw

主summary为119,344字节 / `6204fe90ff336223346f6cd451a8a81c34fce76b77d949577eaf0f435274ef3e`；always为119,694字节 / `984f24f8fe885d2fb24128d0e57efc7d1d8a325a094309a82f05b1e8965013f3`。它们分别超过原界29,344及29,694字节。这仅是原长度减去固定传输界的元数据说明，不是科学计算。

两次都记录：

- `summary_complete=false`；
- `transport_exit_code=70`；
- `reason="necessary-summary-exceeds-90000-bytes"`；
- `full_result_not_split_or_encoded=true`；
- `unread_necessary_records_retained=true`；
- `prior_large_raw_may_have_retired_after_durable_necessary_selection=true`。

实际 `progress.phase="original-new-warm-FD"`、`batch_index=7` 是最后一次FD前写下而未再更新的状态；不能借此误称FD仍未结束。它们之后的16个finished事件、八个retired事件与 `finish_chain` traceback证明控制流已进入最终读回。

本文没有119KB正文，不能实测其中哪一列占了多少，也不能把actual200的148KB与本次119KB当作同一科学对象的压缩基准；两run的trial数和值已不同。原源码仍可支持下一次必要语义去重分析，但不能据SHA编造一个已知的字段字节分布。

## 455.6 原规则、静止与实际清理结局

原规则必要对象482字节 / `cdbd37d40b73df80be8bb92e76a159d3ae18ee4e6e4ea360e30022ac5a330443`，原字段为：

- `science_returncode=70`、`wrapper_returncode=70`；
- `sync_rounds_started=3`、`periodic_sync_failures=[]`；
- `README_change=null`；
- `science_terminated_for_actual_rule_change=false`；
- `scientific_checkout_modified=false`；
- `original_scientific_argv_and_budget_preserved=true`。

原三次同步事件真实完成于03:22:28、04:07:30、04:52:34 UTC。根README原blob21bd547f56590b7f2dd279d0297efb289a9b2783与topic bff8aea253a9e6a7a4fac28d810ac454c5499fec已由原绑定事件输出；本次并非规则变化中断。

Always读回于04:59:58.2823552Z输出实际owner静止：

- 真实owner PID2454、PPID2327、PGID/SID2454、start_ticks4760；
- owner原回执767字节 / `8c885188d52cc855faab0daff2cf263944f81b0bd0dadd393eb7ffa993dadf96`；
- `quiescent=true`、signals空、unknown_scope空；
- before、after和live_original_group_after均空；
- 不声称覆盖未记录的另开session进程。

静止之后always仍因119,694字节超限返回70。最后在04:59:58.5518115Z，真实cleanup事件是：

`request206_owned_cleanup_skipped`，`actual_necessary_readback_outcome="failure"`，`actual_rules_readback_outcome="success"`，`unread_surviving_raw_and_necessary_records_retained_until_runner_destruction=true`。

所以cleanup步骤success只说明按合同执行了skip，不是删除成功。主循环在 `finish_chain` 后的 `shutil.rmtree(work)` 没有到达；八个大batch先前已按各自事件退休，但尚存末pair和必要记录由runner生命周期结束回收，没有新的artifact、Release或Git raw可恢复入口。不能在下一run仅凭它们的SHA续本次末场。

## 455.7 本次没有支付的结论及后继边界

本次以下范围仍未向外完整读回：

- 24条trial的实际步长、merit、预测/实际变化、原门值和失败原因；
- 每条失败query及角地址、每组实际未访α范围；
- 原完整FD中选中的误差数、失败收缩记录与方向地址；
- 实际末三参数、全部末pair必要身份和各场数值；
- 本次新增完整native、full-DN、末端J、sensitivity及physical audit。

这些不是由本文省略掉已到手的正文；原两次读回都未成功输出它们。日志只有计数、来源与有限控制流证据。不得把失败说成“所有结果均已读到，仅格式不同”。

可继续的源任务是从当前固定角色表选择器和真实写入者查找重复的**必要语义表示**，例如已严格canonical相同的共同源、固定schema或重复同一实际对象。新实现仍须保每组所有实际trial、原错误/失败地址、必要FD误差、未返范围和末参数，仍是唯一90KB、过限70；不把大科学树改为字典、分包或编码传输。新实验若需要重生，只能明确从原actual98另起，而不是续接本次未留下可恢复原件的末warm。

本文不预定下一摘要尺寸，不预定八组会重现同一24条轨迹，也不由本次进步补出完整场存在性。R455的实际结论是：**八组原model/freshFD和真实父交接已有完整事件与控制流依据；24条计数已输出；单份表格必要正文仍真实超限，always未恢复，最终按合同跳过主动清理。**
