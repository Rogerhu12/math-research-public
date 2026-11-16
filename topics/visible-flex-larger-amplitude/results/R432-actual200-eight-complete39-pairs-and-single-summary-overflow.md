# R432 — Actual200 的八组完整39模型/真实FD与单摘要再次超限

作者：ChatGPT（AI，exact_refinement）；2026-11-16。  
范围：公开 Actions 的实际原日志、已冻结源码控制流及必要来源读回；本地未执行、导入、编译或重算科学模型。

## 432.1 结论和证据层次

Actual200 确实运行了八次原39-query完整模型和八次新 warm 的原边界 FD。十六个原子子进程都返回0，八份本地必要记录均真实保存，八次实际父文件交接事件的 `next_actual_parent_pair_retained` 全为 `true`。原记录给出的逐批 trial 数为4、4、3、3、2、2、1、1，共20条；这是本次记录，不能拿 actual191 的24条替代。

本次失败发生在八组之后的必要摘要传输：主读回形成的单份 ASCII JSON（含末LF）是148,732字节，超过固定90,000字节界；always读回再次形成149,082字节，同样拒绝输出正文并返回70。完整必要摘要没有一个成功的 BEGIN/END 帧，不能把其 bytes/SHA 冒成已读到全部 trials、FD 数值和末参数。

这里须区分三层事实。

1. **日志直接观察**：16个原子退出0；8次本地必要记录保存；8次真实父文件交接；上述20条计数；两次明确超限；原规则无变；已记录进程组静止；最终清理跳过。
2. **固定源码与原事件联合推出**：八组均通过原来的单步 progress、真实 warm/status 配对及本轮 fresh FD 门，才会出现八次交接为真。此结论不是仅凭进程绿色推断；§432.4给出实际分支。
3. **本次未读回的科学细节**：20条 trial 的各原始标量、实际接受步长、各拒绝 query/角地址、每组 FD 原误差、最后三参数与最终 warm/status 原件，未在外部日志正文出现。不能从SHA恢复，不能从上次轨迹补齐，也不能据八组推进声称 native、full-DN 或新的 coupled finite acceptance。

这不是新的数学拒绝、README变化或本次墙钟预算截止。它是原八批科学完成之后的必要读回缺口；下一步应修必要语义的重复表达并从仍可恢复的 actual98 原父另起同一方法的新链。不能把新计算冒充本次被清场的末父。

## 432.2 实际运行、原日志和冻结身份

| 项 | 实际身份 |
|---|---|
| 仓库 | `Rogerhu12/math-research-public` |
| Run | `43780457519` |
| Source commit | `cb597d3c3d66f9787a712ffa7ca9dc3d52bd57de` |
| Compute job | `133016222219` |
| Workflow | `visible-larger-public-thirty-nine-necessary-batches.yml` |
| 原规则 runner 时段 | 2026-11-16 00:27:42 UTC 至02:45:33 UTC |
| 科学步骤最终退出 | 70，来自必要读回超限 |
| 原规则步骤 | success，无README变化 |
| Always必要读回 | failure，第二份单摘要仍超限 |
| Cleanup步骤状态 | success；其实际事件为“跳过删除”，不是已删除 |

该 workflow 只有一个 compute job，没有另外一个 report job。唯一日志通过官方 connector 取回一次。下面是**connector 返回的已解码日志字符串重新编码为 UTF-8 的身份**，不是另行下载的原HTTP响应字节身份：

- 完整已解码日志：93,500字节，SHA256 `16b3120f745d051959c87b0312e5852581e5bb54748971211343985ccb36f06f`。
- 575个物理行；解析视图仅去掉1处真实物理行首BOM，以及570处锚定的GitHub时间戳前缀；原文身份保留。没有把任意正文中的BOM当成空白。
- 68个真实JSON事件；逐原事件行加LF保存为48,451字节，SHA256 `cba4c1ba8c2ffaa41412adb22dbf38541523f22a8974d6f991522644b14b40c8`。该元数据摘录未重新序列化其中的数字。
- 成功的完整必要摘要帧数为0。命令回显中的字符串不作为真实帧或结果。

原执行链关键来源为：

| 角色 | 字节数 | SHA256 |
|---|---:|---|
| `root_20261115_thirty_nine_necessary_chain_readout.py` | 62,855 | `abf42d92c980566e20a4c8a7fbd90976669240bf8cc8bed06d3b6e1705fa79b8` |
| `geometry_20261115_thirty_nine_necessary_batches.py` | 29,611 | `68d53286565c892cdcebd131fb73c2c32b25d6ff865a6da706bec03dbfdbe8e5` |
| `public-thirty-nine-necessary-model-recipe.json` | 31,236 | `2b9c71c067dfb8a7ff9fcd7111e4eff884a68e197504c38e14b128b6ecb8692f` |
| `public-thirty-nine-necessary-batch-request.json` | 13,428 | `305088672e8eeccb46e48931b87f5a55b9ed41ccc9b8f19d958b71711b7e1ad9` |
| `visible-larger-public-thirty-nine-necessary-batches.yml` | 13,285 | `0de9e7174a2f291481583c91f76f8f43c9aa951e2515617358d8b6e9af8d4536` |

原来源全集和各输入由[实际request](../computations/public-thirty-nine-necessary-batch-request.json)、[原recipe](../computations/public-thirty-nine-necessary-model-recipe.json)及[R428](R428-complete39-necessary-chain-readout-and-original-science-contract.md)绑定。

实际 source-check 事件核了104个保留的 actual191 来源、新必要helper和新orchestrator，共106件显式源；参数manifest1件。科学仍是原39-query、原完整H与FD，没有换成读回helper的近似模型。

## 432.3 本轮实际问题和原资源没有改变

本轮明确从 actual98 原 artifact 恢复父场，不使用已删除的 actual191 或 actual171 末pair：

- 原 artifact run `43677587785`，artifact `14147700690`，来源commit `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`。
- 原 warm `warm-001.json.gz`：4,927,052字节 / `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`。
- 原 status `driver-status.json`：3,379,453字节 / `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`。
- 本次必要 input binding：8,917字节 / `44723a5cb0a1a6b617fcca7b1b12cce762bc5f25b91b286c24d3774621090007`；原记录注明它是Actions临时文件，未把大输入内容输出。

新39集合保留完整38集合并加入真正 RIGHT-RMS459，fraction为原浮点字面 `0.8273268353539885`。完整端点支持为459、460、462至491，共32个节点；461仍是原全问题中的自由节点。它经[R407所刊适配源](../computations/root_20261115_noncontiguous_local_qp_condensation.py)实现的完整仿射前缀QR消去，不伪造零B461。实际来源事件保留：26个捕获interval、10,819个local坐标、33节点cover前沿11,266维、消去461后的真实前沿10,928维、C支持4,059维。完整方程、全角和外变量没有因必要摘要改动。

每次原模型命令仍含：

`iterations=1; damping=270; lsmr-iterations=200; projection-sweeps=200; line-search-steps=17; budget-seconds=1200; angles=4096; jac-workers=2; condensed-budget-seconds=600; condensed-trial-reserve-seconds=90; condensed-recovery-reserve-seconds=30; condensed-max-working=512; condensed-dual-sweeps=200; condensed-store-root`。

每次 FD 仍对**该批刚产生的真实 warm**调用原 response producer，`angles=4096`。批次数上限8、批间时限10,500秒、science步骤175分钟、job195分钟及必要读回10分钟是原资源合同；本次没有把资源停止当作数学证伪，也没有改任何接受阈值。已访问八组，批次集合0至7没有未启动后缀；每批17档中哪些档位未访的原明细仍在未输出摘要里，本文不从计数猜具体α。

## 432.4 八组推进为何有证据，而详细数值仍未付

实际 worker 的 `run_batch` 只有在原 model进程退出0、`optimization_progress is True`、`accepted_warm_steps == 1` 时，才进入 `validate_completed_pair` 和新的 FD。

`validate_completed_pair` 继续要求原optimizer schema、`latest_warm_file == "warm-001.json.gz"`、真实warm SHA与status一致、warm内producer identity和status identity逐键相同；它同时保留 `success is False` 和 `new_coupled_finite_acceptance is False`。这说明这里接续的是一个真实优化progress warm，不能换称已接受的完整新有限场。

进入新的 FD 后，`eligible` 由下列原条件形成：

- FD子进程退出0；
- 原 response JSON实际存在；
- `implementation_check_passed is True`；
- `prepared_sha256` 等于本批真实 warm SHA；
- `complete_current_warm_boundary_FD_actually_recomputed is True`。

主循环先保存本地必要记录，随后仅在 `eligible` 时搬移该批两份原文件、核搬移前后bytes/SHA未变，再退休已消费的大batch。实际事件 `next_actual_parent_pair_retained` 就是这个 `eligible` 的原布尔值。本次八个该字段全部为真，因此联合固定源码可以判定八组通过了这些原progress/配对/新FD条件；不是用helper自己另设了一个科学接受门。

这项推论仍不能给出未输出的 FD误差数、逐trial的merit或失败地址。日志中的子进程stdout仅保存bytes/SHA；尤其每次FD的177至179字节小stdout也没有转发正文，因此本文不假装读到了它的数值内容。所有16个stderr均为0字节，完整stderr空字符串已由原事件输出。

| 批次 | 原trial计数 | model退出 | FD退出 | model原耗时/s | FD原耗时/s | 真实父交接 |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 4 | 0 | 0 | 1014.720221113 | 25.445541021000054 | true |
| 1 | 4 | 0 | 0 | 1003.6807645049998 | 24.69023723500004 | true |
| 2 | 3 | 0 | 0 | 1000.7561591059998 | 24.817342777999784 | true |
| 3 | 3 | 0 | 0 | 1014.7847425229997 | 24.58064563700009 | true |
| 4 | 2 | 0 | 0 | 1002.9395288340002 | 24.335264680000364 | true |
| 5 | 2 | 0 | 0 | 1000.6114841150002 | 24.46939272199961 | true |
| 6 | 1 | 0 | 0 | 1000.7568657889997 | 24.38304633900043 | true |
| 7 | 1 | 0 | 0 | 997.8220853390003 | 24.362098060999415 | true |

以上时间逐值抄原事件，不借它预测另一run的预算或速度。20是八个原整数计数的汇总，不是重跑trial或复算科学量。

## 432.5 保存过的必要记录和真正丢失的读回边界

八份必要本地记录保存事件分别为：

| 批次 | bytes | SHA256 |
|---:|---:|---|
| 0 | 30,388 | `885d342e7c149359665a9f538bc63ae4fcff7b135f33c2360e4ddaff67e3a9f7` |
| 1 | 30,559 | `da6babb0099742a10cecff04c0c4f804b4777e1a29478f8522fdb0fbf127e106` |
| 2 | 27,737 | `2f860149fd487bb4d9c3a5ff007085b1c51e3603e1cb3ff3db24d7ca9ae520da` |
| 3 | 27,560 | `015b12594ba26f6cff1e90ef0a54bf849a7d7f77f2ca327c17427827320fd572` |
| 4 | 24,634 | `ff8e1af54dd5b7958d87253661b5b64e54e58464a820ed746f013db504656588` |
| 5 | 23,750 | `a9efc055f6aa177c70fc2b61fe87ad374bf476bac502c53b3f0084eeb2183915` |
| 6 | 21,993 | `071bd69bcb30ebf1cb5feab0481ab73f50462fdc736e4475eed782b6a197a78f` |
| 7 | 21,992 | `392272856fabf9fec137b5a95ca55c7dd411382a822f81a86aae1a5c22a285e1` |

保存事件明确说 `scientific_stdout_not_emitted=true` 和 `whole_chain_stdout_readback_still_pending=true`。所以“本地已持久化”与“已向外完整读回”是不同状态。上述身份只证明原程序报告这些文件真实存在并被消费，不能重建其未输出正文。

主循环八组结束后，`finish_chain` 先保存链状态、读取这八份记录与input binding、形成 `necessary-whole-chain.json`，再调用 `publish("whole-chain",report)`。原 `publish` 先计算完整JSON身份，再检查90,000；超限在打印BEGIN帧之前抛出 `ReadbackIncomplete`。

实际第一次：

- label `whole-chain`；
- 148,732字节 / `459fb8c8e2b28658970e1f2daa8c82a7f537f5aa375c71f2b4b94670007a263d`；
- `summary_complete=false`，`transport_exit_code=70`；
- `reason="necessary-summary-exceeds-90000-bytes"`；
- `full_result_not_split_or_encoded=true`。

原 traceback 定位为worker的 `helper.finish_chain(work,final)`、helper的 `publish("whole-chain",report)`，最终错误：

> ReadbackIncomplete: Necessary summary exceeds90000; preserve unread necessary records and surviving raw

Always读回在静止确认后，实际又形成：

- label `whole-chain-recovery`；
- 149,082字节 / `61e677cf4508385fd5656af22ac17876f679e30d8522405305378d15d374ebb3`；
- 同一个90,000界、同一个70、同样未打印完整必要帧。

本文没有两份JSON正文，不能把350字节差异归给某个具体科学字段，也不能断言148KB中的某一类数据占了多少。现有源码足以分析可能重复的表达结构；确定的实际事实只是完整单摘要仍超过界限。后继必须基于原写入者和选择器的语义去重，不能在没有正文时编造“已压缩到某个字节数”。

最后 `progress.phase` 仍是 `original-new-warm-FD`、batch7，这是worker在最后FD前写下而未再改的字段。不能凭该旧phase误说FD尚在运行；十六个finished事件与随后finish_chain traceback已明确它们结束了。

## 432.6 原规则、静止及实际清理结局

原规则结果为482字节 / `84b9ef15d45c3d812ffdf77b83d748eda63c1c85094b1b6492ddfae71e73e472`：

- `science_returncode=70`，`wrapper_returncode=70`；
- `sync_rounds_started=4`，`periodic_sync_failures=[]`；
- `README_change=null`；
- `science_terminated_for_actual_rule_change=false`；
- `scientific_checkout_modified=false`；
- `original_scientific_argv_and_budget_preserved=true`。

本次真实记录的owner是PID2653、PPID2525、PGID/SID2653、start_ticks4281。Always读回先核本run/source/request/helper绑定的owner记录，再输出 `request200_actual_owner_quiescence`：`quiescent=true`、signals空、unknown_scope空、before/after空、live_original_group_after空。它明确不声称识别了未记录的另开session进程。此范围内没有需要发送的信号，也没有边读边删活跃原group的证据。

八份batch大数据已经在各自本地必要记录保存、真实pair搬移后退休；这是原各 `batch_payload_removed=true` 事件所说的删除。它不等于整namespace成功清理。

整链第一次超限后，主程序中位于 `finish_chain` 之后的 `shutil.rmtree(work)` 没有执行。Always必要读回也失败，因此最后真实事件是：

`request200_owned_cleanup_skipped`，`actual_necessary_readback_outcome="failure"`，`actual_rules_readback_outcome="success"`，`unread_surviving_raw_and_necessary_records_retained_until_runner_destruction=true`。

所以workflow的cleanup步骤绿色只表示正确执行了跳过分支。本文不能写成“原必要读回完整、随后主动删除全部namespace”。未读必要记录和仍存末carrier留到托管runner销毁；没有artifact/Release/Git raw上传，不存在一个可在下一run凭SHA取回的末场入口。

## 432.7 后继范围和仍未支付的责任

本次八组原progress与fresh FD的控制流证据成立；本次具体20条必要标量和末三参数仍未读回。这两点须同时保留，不能为了把失败说成“只格式问题”而补出缺失的科学结果。

本次没有调用native或full-DN新链，原status中的 `success=false`、`new_coupled_finite_acceptance=false` 未被覆盖。完整场存在性、native/full-DN/finalJ/audit均不由本次八组推出；39-query/完整B响应的源码责任也不等于全部非线性域已获得新证书。

独立后继的最小方向是：

- 保原104旧来源、完整39集合、非连续支持QR、原全部模型/FD/域/merit门和资源预算；
- 仅删除单份必要表示中经源码证明重复的信息，保每批所有实际trial、必要FD原误差/失败收缩记录、原完整错误和未返地址、实际末三参数及真实文件身份；
- 源/输入共同身份只表达一次，不把大科学树改成字典或分片传输，不提高90KB；
- 新实验从原actual98真实恢复另起，不续接已消失的actual200末pair，也不冒本次未读字段；
- 新摘要如果仍超过界限，继续明确70和未读范围，不截断、不假成功。

这里不宣称未来摘要大小、未来八组完成或未来科学改善。R432支付的是本次实际运行的有限结论：**八次原单步progress和当前warm FD有源码可追溯证据，20条计数已输出；单份必要内容未完整交付，主读回和always读回都真实超限，最终正确跳过主动清理。**
