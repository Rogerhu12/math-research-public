# R480：actual213 八次原39-query接受与fresh FD完成；单份必要读回仍超限

作者：OpenAI ChatGPT（AI，exact_refinement）。日期：2026-11-16 UTC。

## 480.1 结论及证据层次

实际 request213 从真实 actual98 父重新生成39-query轨迹，完成了八次原模型调用和八次针对当次新warm的原完整边界FD调用。八个实际批次退休事件均记录 `next_actual_parent_pair_retained=true`。结合这次准确执行的worker控制流，可确认每批通过原“一个新warm被接受、实际pair校验、fresh FD implementation check和当次warm身份匹配”的续算条件。此结论不是由workflow绿色或单个子进程exit0推得；本次workflow最终为failure。

本次直接失败点是必要信息运输：主链形成的单份必要文档为 **115134 B**，always恢复读回为 **115484 B**，都超过原 **90000 B** 上限。两条路径均明确return70，未输出完整必要正文、未拆包、未编码大科学对象、未截断后标成功。原24条trial的具体数值、失败query地址、每批FD误差值及最终pair参数未从本次日志完整取回，不能以这次八批成功控制流补填这些缺项。

因而本次同时成立：

1. 原八次模型接受及八次真实新warm FD的续算判定已由实际事件和固定源码控制流确认；
2. 单份必要读回没有完成，R479的固定语义context表示未把本次实际文档压到90 KB以内；
3. 213没有调用当前H的非线性native/fullDN，也没有产生新的完整耦合BVP接受；
4. 原批次大payload在各自必要记录已实际持久保存后退休；最终namespace清理因必要读回失败而明确跳过。留下的临时记录没有上传为artifact/Release/Git科学数据，也不能在runner生命周期结束后由其SHA重建。

本文件是实际数值过程与元数据证据的范围记录，不是对未读数值的证明，也不是新求解器、域审计或接受门。

## 480.2 唯一实际运行和读取来源

| 项目 | 实际身份 |
|---|---|
| repository | Rogerhu12/math-research-public |
| source commit | fe0a0d737440bcad59d5af9cb9d08b24131204f4 |
| request / attempt | 213 / 1 |
| run | 43812359001 |
| compute job | 133116630470 |
| 创建 | 2026-11-16T05:46:04Z |
| 原rules runner开始 | 2026-11-16 05:46:31 UTC |
| 原rules runner结束 | 2026-11-16 07:36:28 UTC |
| job终态 | completed / failure |

本次入口是单compute job；本结论没有虚构独立report job。官方jobs元数据中，步骤1–7成功，步骤8“八组原model/FD”及步骤9“静止后单份必要读回”失败；步骤10原rules metadata成功；步骤11条件清理步骤自身成功，但其**实际事件是跳过删除**，不是删除成功。随后普通Actions post-job步骤结束。

唯一终态日志通过官方GitHub connector取得一次。保存的是connector解码后的完整日志文本，其UTF-8编码身份为：

- bytes：112672；
- SHA-256：`75e66e94d0c279fec49e84dfbddfe61e540b1cb54264402ad0fc6fc557389bee`。

这不是另一次CLI下载的HTTP原响应字节SHA。解析仅对每物理行的运输前缀处理：可证明的单个行首BOM及锚定UTC timestamp；原日志文本与身份保留。实际JSON事件和Actions打印的ANSI脚本文本分开，未把脚本内的事件字符串当成执行证据。本次没有再次下载任何原科学stdout、科学数组或原artifact以补填未读值。

官方原入口与记录：

- [actual213 run](https://github.com/Rogerhu12/math-research-public/actions/runs/43812359001)；
- [actual213 compute](https://github.com/Rogerhu12/math-research-public/actions/runs/43812359001/job/133116630470)；
- [固定request原文](https://github.com/Rogerhu12/math-research-public/blob/fe0a0d737440bcad59d5af9cb9d08b24131204f4/topics/visible-flex-larger-amplitude/computations/public-thirty-nine-context-batch-request.json)；
- [固定source-view plan](https://github.com/Rogerhu12/math-research-public/blob/fe0a0d737440bcad59d5af9cb9d08b24131204f4/topics/visible-flex-larger-amplitude/computations/request213-necessary-context-source-plan.json)。

## 480.3 原有限问题、真实父与本次source views

初始父仍是实际98的真实原件，不是171、191、200或206的已删除末场：

| 父件 | 原值 |
|---|---|
| actual98 run / source | 43677587785 / 918fdb11dbb7a424b6149b405e2c7fab3cc0c737 |
| artifact id / name | 14147700690 / visible-followup-condensedqp-43677587785-1 |
| artifact bytes / SHA | 809042943 / 9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a |
| warm-001.json.gz | 4927052 B / b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67 |
| driver-status.json | 3379453 B / b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff |

这里artifact是原声明的恢复来源；本次结论作者没有重新下载其大数据。真正首批命令的resume/status SHA与这对声明一致。后面每批命令明确使用本job上一批的 `parent-after-XXX` 原warm/status，未复用旧run的末场。

39 queries保留原38全集，新增真实RIGHT-RMS459，fraction为原声明的 `0.8273268353539885`。实际source-binding事件记录：

- capture intervals：26；
- endpoint nodes：`[459,460,462,463,...,491]`，共32；
- actual B local coordinates：10819；
- cover nodes：33，cover front dimension：11266；
- actual front dimension：10928；
- C coordinates：4059；
- node461作为原完整H的自由变量经过前缀QR消去，不伪造B461，不填零列；
- 原39的typed query、完整H/J/响应、原accepted域/merit/17档门及原FD数学源码未改。

本次resource合同继续为最多8批、between-batches clock10500秒、science step175分钟、job195分钟、readback10分钟。每批命令仍 `iterations=1`、damping270、lsmr/projection200、line-search17、model1200秒、condensed600秒、trial reserve90秒、recovery reserve30秒、max-working512、dual-sweeps200、angles4096、jac-workers2；FD在当次新warm上独立执行，angles4096。没有以formatter修改这些原门或预算。

原完整public dependency目录未迁移。R479仅生成两个具有独立身份的普通源码view，source preparation在科学之前实际成功：

| 文件 | bytes | SHA-256 |
|---|---:|---|
| public-thirty-nine-context-batch-request.json | 22988 | bb4005b4d7e314f0c3de466e10ffb7b7c43a32140750fea3970992af0ff26729 |
| request213-necessary-context-source-plan.json | 5652 | 5cd405f3a8ef58bc27019fadd8036d7f293a76fbea1ddd31e095ed652637cf85 |
| root_20261116_thirty_nine_context_source_views.py | 8157 | b9887b2549772546380f55e1d85209f00dc373d8f03bca767d7df759003c12fd |
| root_20261116_thirty_nine_necessary_contexts.py | 20813 | 689517df7b70b839112f9ba9ab7daf8d6144decd72c89215a22c35ab9c5f8b7c |
| 真实生成readout | 75610 | 3160c22d42abb1103ba1f1d3d71b172fbfe6d09cd938ecb7fac1bc5032ae11b5 |
| 真实生成worker | 29658 | 3c2cdcd9cfa0d756413afb9b5b67edb81a81db3d1f69f4836f08be3c0e401ba3 |
| model recipe | 原完整文件由request绑定 | f2176b25a75166d99101c8b41672100a22562fc669e7919669da5a553351473f |

生成readout basename为 `root_20261116_thirty_nine_context_chain_readout.py`，worker为 `geometry_20261116_thirty_nine_context_batches.py`。实际source-view receipt为3160 B / `bbb14d53e95f36f9aa9ecd968a93f7b1ea6e2164862d5227f0a5e7a2ecf9fc60`。其全部literal replacement计数与两件完整输出身份已返回。

实际binding计数为110 public +2 generated =112显式身份，原108public身份保留。这个计数没有被当成完整transitive import闭包证明。原目录仍真实保留，本次两view科学运行已经开始；它们不是公开Git源，也不是对科学数据作编码。

为核控制流，作者仅从固定source公开取原两基线和计划，逐literal替换重建文本，并核回日志中的上述两个输出SHA；没有执行/import/AST/compile任何科学或新fixture。

## 480.4 八批真实完成范围

原日志提供以下完整小元数据。时间均为原子进程实际elapsed_seconds；最后一列是各批 `complete_original_trial_count`。

| batch | 原model秒 | model exit | fresh FD秒 | FD exit | trial数 |
|---:|---:|---:|---:|---:|---:|
| 0 | 788.877837041 | 0 | 18.779309308999927 | 0 | 4 |
| 1 | 806.702627827 | 0 | 18.911112870999887 | 0 | 3 |
| 2 | 798.4296762520003 | 0 | 18.939636914999937 | 0 | 4 |
| 3 | 796.8205489170005 | 0 | 18.24778210400018 | 0 | 3 |
| 4 | 796.5331375420001 | 0 | 18.13496503999977 | 0 | 3 |
| 5 | 803.9115111390001 | 0 | 18.159778696999638 | 0 | 2 |
| 6 | 798.5821277129999 | 0 | 18.09093388600013 | 0 | 2 |
| 7 | 802.5617832920007 | 0 | 17.91429136700026 | 0 | 3 |

所有16子进程stderr均实际0 B，其SHA为标准空文件SHA。model stdout的实际bytes为151080、151389、151467、151483、151533、151720、151579、151719；对应FD stdout为177、178、178、178、177、178、177、177 B。它们都保原身份但未把科学stdout全文公开；不能从这些长度推出其中具体数值。

八批的完整必要字段各先写入本地记录并fsync/原子替换、核byte/SHA，随后才退休该批大payload：

| batch | 必要记录bytes | 必要记录SHA-256 |
|---:|---:|---|
| 0 | 30396 | c84b758e4ae053928d8141deff4de78b70feeae1f8dc353136c0471a60f01c91 |
| 1 | 30527 | 2c0c66a2f7050e2a58cfa5d2dc763359342ded197442de65f6223470e1d0274f |
| 2 | 33967 | 501c588c0e8bd61a282b73b022ad8d2679c50653274c132214e5f8b722b60d2e |
| 3 | 29628 | 98e4f92f8484bd4171bf2cfd4848fb0ccc177c8f372b5d868f711816b19aed54 |
| 4 | 29234 | 0007a663bb8ae9bf898a194d5ded286929eda5a4a20f07ed40b9601cb992f2dc |
| 5 | 25943 | ec7ab64ed454605d7dc078f8d6bd6cab16ca84719317bf91a270a3d355b014c9 |
| 6 | 24042 | 34d57b6cda0acced894b8ff27ceabcefa39d5d0ad20bf98fe1a8e87fad497220 |
| 7 | 29862 | 1f2e0d0f362b5e5319be7a57efc56228126aaf4aa2cac6ceb312705153a353e4 |

实际返回的24条trial计数是上述八个原count之和。这里没有重构24条正文，没有按trial数反造alpha、拒绝原因或失败query。每批原17档的其余地址也不在本次必要正文中；只由计数不能把它们统一写成“已经算过失败”或“资源未访”。

### 480.4.1 为什么能确认八次原接受和FD门

实际worker `run_batch` 只有在以下原状态同时成立时才设置 `eligible=true`：

- model_code为0；
- 原driver-status的 `optimization_progress is True`；
- 原 `accepted_warm_steps == 1`；
- `validate_completed_pair` 对实际新warm/status成功；
- 新warm上的FD进程return0；
- 实际FD对象存在，`implementation_check_passed is True`；
- FD的 `prepared_sha256` 等于该次真实warm SHA；
- `complete_current_warm_boundary_FD_actually_recomputed is True`。

主循环只有 `eligible` 才移动该对原件并设置下一真实parent。每批实际退休事件中的 `next_actual_parent_pair_retained=bool(eligible)` 都是true。这个实际字段与当前固定源码的唯一赋值路径，支付的是八个原续算判定；不是推测未读浮点值。最后batch7同样有true，不能只说前七批有下一条命令、最后一批未知。

同时，续算判定本身不是“整个全域问题已解”。它不替原未选query的全部最终几何责任，不付非线性尾、当前H native、最终fullDN/338返回或全部闭面metric/reach。每批必要记录原本含更细的失败地址与FD门值，但本次全链读回失败，这些实际值仍未刊出。

## 480.5 两次明确运输失败

主循环到batch7后进入 `helper.finish_chain(work, final)`。该函数先写 `necessary-chain-state.json`，读取八份必要记录及输入绑定，形成formatter结果，保存 `necessary-whole-chain.json`，最后调用单份 `publish("whole-chain",report)`。

原输出为：

| 路径 | bytes（含canonical末LF） | SHA-256 | 原判断 |
|---|---:|---|---|
| whole-chain | 115134 | 3b27adee8e132650e5783a8e52913e55e7ad087505aea03edcbda994b3af77ef | summary_complete=false，70 |
| whole-chain-recovery | 115484 | 72ae354a0e0fa113f7f14df456fa840bbbbaf98d2e473b2d95c61d6956e30600 | summary_complete=false，70 |

实际reason均为 `necessary-summary-exceeds-90000-bytes`。主链于07:36:28.2599096Z报告，always恢复于07:36:28.5937048Z再次报告。原异常是：

> Necessary summary exceeds90000; preserve unread necessary records and surviving raw

相应traceback指向生成worker的 `main -> helper.finish_chain -> publish`。这里是公开原执行输出，不是根据源码预言的异常。原 `publish` 在超过上限时先输出身份和明确未完，再抛 `ReadbackIncomplete`；它在这条分支不会打印BEGIN/END完整必要摘要帧。完整日志中确无 `BEGIN_REQUEST213_WHOLE_CHAIN_NECESSARY_SUMMARY` 或恢复帧正文。

原8批已形成且退休，不是“第8次模型/FD由于readback被中断”。失败事件保留的progress.phase为 `original-new-warm-FD`、batch_index7，是主循环最后活动标签；实际FD7 finished事件已在07:36:28.1007252Z返回，随后必要batch7已保存、payload已退休，之后才发生全链115134B超限。

R479条件性语义保持结论没有声称任何未知实际摘要必小于90KB。本次实际结果说明其指定表示仍不足。不能从119KB或其他旧run与本次115134B的长度差，推算同一对象的压缩率；不同run的实际数值、错误、完整表和选择内容并未取得逐字相同关系。也不能把115134B搬为两份小于90KB的文档来规避本入口合同。

本次完整115134B/115484B正文没有通过日志返回；这里只保存其真实byte/SHA及实际失败原文。作者没有从SHA恢复这些对象，也没有重新执行formatter或科学来冒充这次原值。

## 480.6 规则、静止与真实清理

本次启动实际核的两README为：

| path | blob | bytes / SHA-256 |
|---|---|---|
| README.md | 21bd547f56590b7f2dd279d0297efb289a9b2783 | 10233 / 6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9 |
| topic README.md | bff8aea253a9e6a7a4fac28d810ac454c5499fec | 2664 / 3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d |

真实rules-result 482B / `93ca0459529f28ddfa65fc9f2da6fc385948ba5d830c75b5a2e6df0b5e16e8be` 记录：

- science_returncode=70，wrapper_returncode=70；
- periodic_sync_failures=[]，README_change=null；
- science_terminated_for_actual_rule_change=false；
- scientific_checkout_modified=false；
- original_scientific_argv_and_budget_preserved=true；
- sync_rounds_started=3；
- partial_scientific_files_not_removed=true。

没有证据把这次失败归为规则变更、175分钟耗尽、单模型1200秒耗尽或科学FD拒绝。

07:36:28.5422343Z的实际owner静止记录标识pid/pgid/sid2481、start_ticks25156；`signals=[]`，`unknown_scope=[]`，`before=[]`，`after=[]`，`live_original_group_after=[]`，`quiescent=true`。它支付所登记原session的静止，不声称未登记脱离进程不存在。原owner记录767B / `b57891f97f56fd704712d7f5d2b99a0ea2c2d70d2914ed4b344f4c7886ca5d88`。

最终07:36:28.8040297Z真正执行的事件是 `request213_owned_cleanup_skipped`，理由字段给：

- source generation outcome=success；
- necessary readback outcome=failure；
- rules readback outcome=success；
- unread_surviving_raw_and_necessary_records_retained_until_runner_destruction=true。

因此不能将step11的success记为namespace已按readback合同删除。另一方面，八次 `thirty_nine_batch_payload_retired` 都已实际发生；最后skip并不会恢复这些已退的大批次数据。保留的是尚存必要记录、末pair与其他未删除原件，未上传作为跨run续算载体。当前H/native状态更从未生成。

## 480.7 已付与未付清单

| 范围 | 本次证据 |
|---|---|
| 原真实98输入和39-query source准备 | 实际完成 |
| 两必要source views生成、实际HERE身份 | 完成，完整byte/SHA对应 |
| 非连续32节点/自由461完整QR入口 | 原源与actual binding保持 |
| 8个原模型调用 | 全实际return0 |
| 每批原一个新warm接受与实际pair校验 | 8个eligible事件及唯一控制流确认 |
| 8个当次新warm fresh FD | 全实际return0，原implementation gate/同warm身份路径确认 |
| 原trial实际数量 | 全8count已返，共24 |
| 24条trial具体alpha、merit、域失败地址和门值 | 完整正文未读回 |
| FD各方向/层的具体误差、失败contraction条目 | 必要正文未读回；不由gate=true补数 |
| 最终batch7末pair完整数值/参数和完整新identity正文 | 未完整返回；不可由SHA复原 |
| 单90KB必要全链文档 | 两条路径都超限，70 |
| 全链数学失败或未选query已修复 | 没有本次完整字段支持这种归因/声称 |
| 当前H非线性native/fullDN | 未调用 |
| 全域准确连续C、完整closed metric/reach或README最终交付 | 未由本次承担/完成 |
| 最终条件namespace删除 | 明确跳过；批次中间raw已按原顺序退休 |

R480保留这次实质科学推进及读回缺口。后继若改表示，仍须基于真实必要语义与固定schema，保留全部实际trial、原错误、失败地址、未返范围及末参数，不能以字典编码大数据、拆包、扩大90KB或复算旧值替代本次未读记录。本文件不自动派发新的昂贵八批重算，也不把新的表示研究变成原数学接受门。

## 480.8 相关已付来源

R479的固定语义context包含证明与formatter保持有效的条件范围；本次只否定“该实际摘要已经落入90000B”这个完成事实。[R479](R479-complete39-fixed-semantic-context-readback.md)保留了canonical完全相等才共享context、相邻块原顺序及不删必要失败记录的责任。本次正文亦不把source-view准备成功泛化为任意transitive闭包已审。

本次所有求解、FD和formatter实际科学/读回运算均在公开Actions。本文仅读取既有终态日志、固定源码和必要元数据，进行文本绑定、SHA与范围整理；没有本地科学、import、AST、编译、fixture或新审计运行。
