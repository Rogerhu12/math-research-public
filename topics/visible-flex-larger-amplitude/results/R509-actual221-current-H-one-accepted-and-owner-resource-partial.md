# R509 — actual221：真实当前 H 的 full-J/R273 与一次完整 binary128 接受；第二次试步资源未完，live response/FD/fullDN 尚未返回

作者：ChatGPT（AI 助手，exact_refinement 分工）。日期：2026-11-16 UTC。

可信度说明：本文是实际公开 Actions 的必要数值记录与执行范围结论，不是准确连续解、误差上界或完整闭面的证明。两份终态 job log 各只读取一次；只解析已经返回的必要正文、原错误及原生命周期事件，没有本地科学重算、编译、AST、fixture 或对拍。所有数值以下列实际字段为准，完整大数组只记录身份。

## 509.1 结论与实际来源

实际221已经越过219的输入恢复和清理工程阻断。在同一真实当前 $H$ 上，原 original64 full-J 捕获、原 R273 方向、literal/physical 两输入包，以及 persistent binary128 owner 都实际执行。

owner 的第一次 $\alpha=1$ 试步完整完成全部576 stage、129248个残差行，并按原严格残差下降规则接受。其原归一化范数由

$$
14074125.721549422871053526172072936
$$

降至

$$
0.00119384019932733053462024588807814309.
$$

第二方向的第一次 $\alpha=1$ 试步只完成133个 stage、30016行，随后记录原错误 `explicit-experiment-time-budget`；余下443个 stage 的地址正好是133至575。该次试步未接受，owner 保留第一次接受的完整状态，以 `resource-partial-trial` 结束。末容差 $2\times10^{-9}$ 未过，独立 fresh replay 未完成，完整 live response 尚未组装或写回协议。因此四个后置128组件、原 affine FD、原 fullDN 与其最终 fresh audit 都没有获得本次运行的完成结论。

本次必要读回完整、单份71252字节；compute/report正文逐字相同。实际 owned quiet 完成后，只删除本次临时 namespace。本文不从保存的 SHA 恢复已清状态，不将它作为可直接续接的父状态。

| 项目 | 实际值 |
|---|---|
| repository | `Rogerhu12/math-research-public` |
| request | 221 |
| workflow | `visible-larger-public-live128-scoped-original-fullDN.yml` |
| event / attempt | `workflow_dispatch` / 1 |
| source / actual head | `8b352f90b97f7c340a2fbebbb11c19080d9a5e08` |
| run | [43835161762](https://github.com/Rogerhu12/math-research-public/actions/runs/43835161762) |
| compute | [133189859163](https://github.com/Rogerhu12/math-research-public/actions/runs/43835161762/job/133189859163)，failure |
| report | [133251098161](https://github.com/Rogerhu12/math-research-public/actions/runs/43835161762/job/133251098161)，success |
| actual request | `public-live128-scoped-original-full112-FD-fullDN-request.json`，54884 B |
| request SHA256 | `0fa9fe29153913252fd569cb2b99711c85b0afe72d8bc576adf629bd3e3f789e` |
| necessary schema | `R508-live128-scoped-original-full112-necessary-v1` |
| necessary reader | `root_20261116_live128_scoped_original_fullDN_necessary.py`，35283 B / `687168ef5ec3414c79667deda4df40c233e60265c1b12605c40a891964f709a7` |

正式科学依据是该固定 head 中的[实际请求](../computations/public-live128-scoped-original-full112-FD-fullDN-request.json)、[当前 H 调用 pipeline](../computations/geometry_20261116_live128_call_pipeline.py)、[同 call owner](../computations/geometry_20261116_live128_same_call_owner.py)及[必要 reader](../computations/root_20261116_live128_scoped_original_fullDN_necessary.py)。R493 的条件组装范围仍见 [R493](R493-current-H-live128-response-projection-and-original-fullDN-interface.md)。原219/221的来源修订不改变本次有限问题，也没有将连续 C 的216链引入这里。

## 509.2 原始运输与读回范围

唯一实际帧名是：

`BEGIN_REQUEST221_SCOPED_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY`

至

`END_REQUEST221_SCOPED_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY`。

两 job 各有且仅有一个真实非 ANSI 正文帧。解析只在视图中逐物理行去单个行首 BOM，再剥锚定的 Actions timestamp；原返回字符串保留不改。正文包含其末分隔 LF，实际 ASCII 字节身份为：

- 71252 B；
- SHA256 `efd2756eb721f6c1979cf08b569e604b84c24298df5f78149438987377858358`；
- compute 与 report 正文字节完全一致；
- 原 compute transport `actual_reader_exit=0`；
- `necessary_readback_complete=true`；
- `metadata_read_errors=[]`；
- 没有 overflow70、分块或大科学树编码。

终态 log 的以下身份是**连接器解码所得字符串再编码 UTF-8**的身份，不冒 GitHub HTTP 原响应字节身份：

| job | UTF-8 字节数 | SHA256 |
|---|---:|---|
| compute133189859163 | 127265 | `2471fd0b50a8bc3b7c0892c46788a6b8fe92bd5419ce032baaab67388c163288` |
| report133251098161 | 147503 | `7b7aa61a7cd6330ec9ef7d2c6f13e3ce3217e3ca67577649e598543a903ee799` |

reader返回了本次一条实际call的选中原请求、捕获/QR/包身份、owner全8条选中事件、全部未完stage地址、末状态/原门、post-component未起范围、外层错误、三次rules、真实quiet与各必要原文件身份。原owner `summary.json` 本身166132 B，SHA256 `3653b88f3bbb6e9b4cdde67bcf161714c6695a4381dec4ff9a4c18e3218cb667`，未整体搬回；本文的“完整必要”不等于完整owner对象或全部原日志科学数组。

## 509.3 原父恢复、输入与真实准备

前九步实际全部 success，包括336个显式源码身份与原普通语法检查、临时容量、原63/78/91准备。源绑定事件在08:55:35.3940061Z记录实际source与336计数；其检查不等于后续数学成功。

准备事件在08:56:01.4641731Z返回 `phase=complete, complete=true, error=null`。必要正文保留：

- actual63只作 prefix 初猜，不是已完成fullDN；
- actual91只作本次 tail 初猜；
- 原63 producer来源46件；
- 没有导入 completed61 父或旧native cache；
- status gzip 解码后原JSON字节保留，没有JSON重序列化；
- 原port由实际warm的 `/complete_scalar_profile/complete_original_port` 提取完整对象，明确不冒原port文件逐字身份。

主要输入身份：

| 真实输入 | bytes | SHA256 |
|---|---:|---|
| actual63 warm gzip | 4799943 | `6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a` |
| actual63 status gzip | 231286 | `6443fce5e818ff20fd36075f6038ee60630d0b77e8ed2304d41e4d072ea6a005` |
| 解码后的原status | 1810333 | `8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46` |
| historical accepted prefix | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| original112 tail config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| frozen-ledger-ready | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| frozen-stored-ready | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |
| 实际91派生初猜 `seed.json` | 26376 | `6ec8af420270d9decd2ec405a4bcf21ef99e18b26a7637c63b2cf0f8448720a9` |

ledger-ready在本次declared与actual均为上述完整64字符SHA，原219的63字符误述没有继续阻断221。准备文件66130 B / `eacaebbf03daba9ae044121bb69081a1fa74ddea7cf4959838d1ed1176713f3c`，只记录其真实完成范围；没有借准备成功支付当前H的残差或导数门。

实际启动前空闲92007010304 B，要求68719476736 B；未删任何SDK或科学payload。结束时空闲91199254528 B。本次停止没有磁盘不足事件。

## 509.4 当前 H、full-J、R273 与两个真正输入包

本次只有 `call-0001`，请求为 `jacobian=true, audit=false, bootstrap_request=true`。实际112列 $H$ 的 little-endian binary64原字节SHA为

`bdf50c9af8b41f206c00a076358b32016b8a7c3bb2e377be7d5e74b08c8a8fa7`，

shape为[112]，无负零列。初始化记录 `cold_initialization_selected=true, first_seed_available=true, original_initial_argument_supplied=false, original_tangent_prediction_selected=false`；seed真实分配，不把历史tail状态冒同H响应。

原full-J捕获返回 `fresh_original_withJ_returned=true`。其当前original64 norm为14074125.721559538，原word `070417b721d86a41`。这是该original64捕获的值；下一节binary128重评价的初始norm另列，不能把两者当逐词相同。

原R273实际返回：

- `original_current_R273_returned=true`；
- `diagnostic_completed=true, linear_direction_computed=true, actual_error=null`；
- native_call1、nonlinear_iteration0、snapshot_sequence0；
- 原QR内部elapsed30.045098330999963秒，pipeline factor elapsed30.53680068299991秒；
- QR子进程return0，stderr0 B；
- 完整QR结果gzip4543 B / `81b4ded39e86cef1e9e0e57b746a4d46c454a2201248dbed2b6627bebc3849cf`。

同call身份为：

| 成员 | bytes | SHA256 |
|---|---:|---|
| snapshot/result.json | 1312 | `fbf60156591ddde14f361aa9654640c912e8e562d7e6dfcd94b69e1687db5e54` |
| literal-packet/complete-input.bin | 10348368 | `de5bf97b4d9ee6d0c4d3162612fe4eda343ca4358484f384bc337cd189b2ff67` |
| physical-packet/physical-input.packet | 5104360 | `1c9fab18574bb130f905daef5fcff66163a0fe987528ace2d9bc81829fc52151` |

`literal_packets_returned=true`；owner记录原cuspAwareFlow、eta文字`1`、实际H和snapshot、完整current R273 delta SHA `6b9c834fb9c153289568379526e5d3ffa61ef70d3b4c8c3037bb822ada2f8b6f`。其state_point明确是 `actual-current-H-fresh-original64-full-J-initial-guess`。

这里的global shooting状态是577节点×224列；局部RK状态226列含两个mean。后置要求的576×224全stage敏感度以及338×112物理J是不同对象。本次有原original64全J/原R273，不意味着后置binary128 stage maps或338×112 live J已经返回。

## 509.5 全部实际 owner 事件与数值

必要正文中的 `owner.records` 有8条，来源是 `actual-full-owner-summary`，原序如下。

| 原序 | 事件 | 真实范围 |
|---:|---|---|
| 0 | persistent128_initial | 全576 stage、129248行，完整初始评价 |
| 1 | persistent128_direction_lifted，iteration0 | 完整577节点、224列方向恢复 |
| 2 | persistent128_trial，iteration0/trial0 | $\alpha=1$，完整评价，接受 |
| 3 | persistent128_iteration_closed，iteration0 | 保存第一次接受后的完整current |
| 4 | persistent128_direction_lifted，iteration1 | 完整577节点、224列第二方向恢复 |
| 5 | persistent128_trial，iteration1/trial0 | $\alpha=1$，133 stage/30016行，资源未完，未接受 |
| 6 | persistent128_iteration_closed，iteration1 | current仍为前一次接受的完整状态 |
| 7 | persistent128_owner_final | 2方向、2试步、1接受，resource-partial-trial |

### 完整初始评价

`complete=true, rows_completed=expected_rows=129248, stages_completed=576, budget_exhausted=false, evaluation_error=null, failed_stages=[]`。

norm的原两种表示：

- decimal `14074125.721549422871053526172072936`；
- binary128 hex `0x1.ad821b716eed0b5b92235867a8ddp+23`。

其worst row为stage11、global_row2763、component `Pi`、mode_one_based76、input_node12、output_node11、sigma_index11：

- 原signed normalized值为上述正norm；
- residual `0.000152003159643027520143284928307209879`；
- sigma `1.08001848676319388951550307751079132e-11`；
- mean_height_sum `0.0226842463487103007644065167348694512`。

### 两次完整方向恢复

| 字段 | iteration0 | iteration1 |
|---|---:|---:|
| complete_nodes | 577 | 577 |
| complete_columns | 224 | 224 |
| different_from_R273_delta64_entries | 129213 | 129248 |
| nonzero128_from_zero64_recovery_entries | 0 | 0 |
| maximum_scaled_recovery_difference | `5.74892381705579145651981466360999603e-21` | `1.70948705981031582991517702728200214e-22` |
| worst_recovery_difference_index | 2536 | 26544 |
| scaled_z_infinity_norm | `9.08574562946894929288399467282033584e-05` | `2.22873200671778355167200642850122705e-06` |

这些是当前有限恢复记录，不是对准确无穷维导数的证书，也不是原浮点路径的逐词等价主张。

### 第一次真实试步完整接受

地址 `iteration-000/trial-00`，alpha原decimal`1` / hex`0x1p+0`；elapsed2039.190185931秒，改变128状态word共128483个，其中6249个改变后仍有相同binary64 cast值。完整576 stage/129248行，全原评价完成，`accepted=true`、原reason `strict-original-norm-decrease`。

接受后norm：

- decimal `0.00119384019932733053462024588807814309`；
- hex `0x1.38f54273779f0179f468e42e9411p-10`。

worst row变为stage12、global_row3006、component `Pi`、mode_one_based95、input_node13、output_node12、sigma_index12：

- signed normalized `-0.00119384019932733053462024588807814309`；
- residual `-1.29116318219691310066796755836131238e-14`；
- sigma `1.0815209463749161885007626203368357e-11`；
- mean_height_sum `0.0226842463487103007644175740389572401`。

两个全局最大值的位置不同，不能把原worst-row变化当同一行的完整误差分解。

### 第二次真实试步资源未完

地址 `iteration-001/trial-00`，仍alpha1；elapsed690.415820611秒，改变128状态word129186个，其中11995个改变后仍有相同binary64 cast值。

该次评价原字段是：

- `complete=false, budget_exhausted=true`；
- `rows_completed=30016, expected_rows=129248`；
- `stages_completed=133`；
- `norm=null, worst_row=null, mean_height_sum=null, below_original_tolerance=null`；
- `evaluation_error=null`；
- `accepted=false, reason=resource-partial`。

原 `failed_stages` 全443条逐条核对为 `{stage:i,error:"explicit-experiment-time-budget"}`，恰好 $i=133,\ldots,575$，无别的地址或错误类型。这里用闭区间表示这份已经完整返回的同值地址列，不是把未返回数值填零。null范数不能解释成不下降或数学拒绝。

末记录 `attempted_trial_addresses=[[0,0],[1,0]]`；requested_direction_indices为[0,1]；unvisited_direction_indices为2至31；最后请求方向的未访trial为1至9。第一次方向在trial0接受后正常结束本轮，没有证据称其余档位被拒绝。

## 509.6 末状态、原容差、replay 与预算层次

末保存状态仍是第一次接受后的**完整**current。因此末 `final.complete=true, final.budget_exhausted=false` 与最后一个试步 `complete=false, budget_exhausted=true` 同时成立；二者对象不同，不能只看末complete字段便称整个owner任务完成。

末原norm为0.00119384019932733053462024588807814309；原outer_tolerance：

- decimal `2.00000000000000012456318291555971284e-09`；
- hex `0x1.12e0be826d695p-29`；
- `below_original_tolerance=false`。

root_stop为 `7.99999999999999999055447483647918958e-14`，root_fallback为 `4.99999999999999969748484640969905465e-12`。没有改门、降低精度或把一次下降冒成原解。

原owner末字段：

- accepted_steps1、directions_computed2、trial_evaluations2；
- stop_reason `resource-partial-trial`；
- `state_never_roundtripped_through_binary64=true`；
- owner elapsed5999.327356172秒；
- raw final-state.f128：2067968 B / `5e3d54b806fe5304be228a58e8b92c7cfa46b8ea145d7cadab3e2916d5ad4b3d`；
- replay `returncode=3, wall_timeout=false`；
- `independent_fresh_replay_complete=false`；
- `fresh_replay_full_residual_words_equal_owner=false`；
- `fresh_replay_all226_output_words_equal_owner=false`。

必要正文没有完整replay子对象，不能从这些false再推断一个未经返回的逐行不一致位置；它们明确未支付fresh replay与逐词一致责任。

请求仍是一个320分钟科学步、350分钟job、19200秒共享科学钟和120秒读回清理预留。clock在恢复完成后、rules和首native工厂前启动。每次H不重开钟。原本次call资源声明owner6000秒、fresh-replay reserve1200秒、threads4、后置stage8000秒、boundary600秒、endpoint600秒；audit请求为false，所以本call实际audit cap为0，最终新audit责任仍留在原完整流程。

实际 owner 源 `5c1d4908…` 在既有全局剩余时间内取 owner cap，再对owner绝对截止钟求最小；原pipeline源 `137cc959…` 在请求audit=false时明确将该call audit cap置0。本文没有把6000秒cap改称19200秒全任务已耗尽。源级分配公式只解释原实际停止层，不另重算科学值。

原pipeline所记剩余时间：

- clock mode开始：19049.889048561秒；
- factor开始：17884.033369282秒；
- solve-response开始：17852.22071096秒；
- owner后置记录 remaining_scientific_seconds_after11852。

外层总elapsed7228.092137483秒；orchestration elapsed7223.362019988001秒；call elapsed7197.702秒。外层 `resource_stop=null, external_signal=null`，科学return1。owner内的原resource-partial是真正停止事实，外层字段null只表示未由外层clock/信号分支终止；不能抹掉内层预算事件。原post-component尚未执行，因此本次不能用其8000/600/1800声明比较任何stage、boundary或audit吞吐。

## 509.7 实际错误传播与完整未返回责任

owner子过程原return0并不等于满足native接受合同。pipeline在同call完整原摘要上看到了末容差false、replay未完成，按原条件抛出：

`RuntimeError: Actual current-H owner final tolerance/replay has not completed`。

该pipeline solve-response返回2、`complete=false`；原记录 `resource_partial=false` 是这个RuntimeError异常类别，不能覆盖内部明确的 `resource-partial-trial`。实际错误位置为call1、mode `solve-response`、`pipeline-solve-response-result.json`。

上层JavaScript原错误：

`Error: Current-H solve-response did not complete; real child result/stderr retained`。

随后原TailClient将完整有限tail未返回作为FloatingPointError传出；其residual和lastIteration均为null。Python完整stderr1068 B / `c7425209bd8c1d7e8f26b6ca6953d00a8f593948f31d4d495fa39b18f4aaf41c`，必要正文保全文。没有将这份异常改写成一个虚构native失败norm。

实际范围：

| 原责任 | 这次实际状态 |
|---|---|
| 同H原original64 full-J、原R273 | 已返回 |
| literal/physical当前输入包 | 已形成 |
| 128完整初始评价 | 已完成 |
| 两个完整224列方向恢复 | 已完成 |
| 第一次完整试步 | 已接受 |
| 第二次试步 | 133/576 stage，资源未完 |
| 原末primal容差 | false |
| 独立fresh replay及全226/全residual一致 | 未完成 |
| 后置128 stages | started=false，summary_returned=false |
| 112 boundary response | started=false，summary_returned=false |
| mixed338×112 endpoint | started=false，summary_returned=false |
| audit组件 | started=false；本call audit=false |
| owner_response_assembled | false |
| protocol_response_returned / actual_protocol_write_completed | false / false |
| original affine FD | returned=false |
| original_full_DN_entry_called | false |
| fullDN实际result/status/RMS preflight/final-cut audit | 均未返回 |
| task_completed / fullDN_accepted | false / false |

`same_live_client.load_client_calls=0`、`full_driver_solve_calls=[]`是**后续原fullDN handoff**未发生；不意味着本次bootstrap TailClient call1没有执行。actual_native_protocol_calls确为1，实际worker exit0，只有一个真实call目录；没有把其余最多17个潜在uncached协议call写成已经求值。

## 509.8 rules、权限范围与实际清理

原rules runner本次启动三轮，同步period2700秒。三轮均实际完成普通pull/rebase/read/push，双README均为root `21bd547f56590b7f2dd279d0297efb289a9b2783`、topic `bff8aea253a9e6a7a4fac28d810ac454c5499fec`；科学checkout未改。

| round | 真实读时 UTC | attempts | origin main read | published commit |
|---:|---|---:|---|---|
| 0 | 08:56:03 | 1 | `247d0b4114f2087f52f83422692c4caba7079fc5` | `f7e9eeb6768741bcac9eccf237374319aa9c3923` |
| 1 | 09:41:09 | 2 | `c8a0d7e9182a7ac0fc4c75404debf54fb93dce2a` | `05916091fb431175a36c21bb304f3fda21418b1a` |
| 2 | 10:26:14 | 1 | `5b163a28d9df10b9d151f7a28de6a0935941c80e` | `cbc646dc86ada06eb988e26acb2f18a7b055f10d` |

`periodic_sync_failures=[]`、`failed_rounds=[]`、README_change=null、science_terminated_for_actual_rule_change=false。原rules result科学和wrapper returncode都为1；部分科学文件在该时刻尚未删除，随后由单独读回与cleanup完成。

真实quiet范围是登记的原PID/startticks/PGID/SID、已观察后代和可读namespace。登记主进程为rules PID4028/start_ticks7120、science PID4156/start_ticks7433、worker PID4157/start_ticks7643，均核静止。actual remaining_owned_processes、unknown、zombie_nonwriting均空；无需发送终止信号。

同uid外部PID1401、1409的environ PermissionError按原字段列在 `outside_scope_unreadable`，没有伪称它们可读、归为own或发送信号；真实own或疑似own不可读仍会阻止读取和删除。本次quiet结论不声称所有同uid进程都可读。

在10:56:30.3453518Z，单必要body通过原reader和transport。10:56:30.9007389Z，真实事件 `request221_cleanup` 记录：

- `removed=true`；
- namespace `/home/runner/work/_temp/visible-live128-scoped-original-fullDN221`；
- `actual_owned_processes_quiescent=true`；
- `scientific_success_not_required=true`；
- `only_owned_temporary_namespace_removed=true`；
- ownership.json 944 B / `5f17762cd644321b1652b9ddc968b791e978e616ae4b53c53e1d3accb3065131`；
- 必要summary身份正是71252 B / `efd2756e…`。

因此本次是**必要读回完整且真实清理成功**，不是cleanup_skipped。上述raw、snapshot、factor、final-state或packet SHA只剩来源身份；没有持久可续算的真实状态文件。

## 509.9 本次新增事实及尚未支付范围

221实际支付了219没有开始的同H计算：原full-J/R273、两输入包、128初始完整评价、两个全方向恢复及一次完整原接受。它同时给出具体停止层：第二试步在owner既有预算内未完，当前完整accepted状态尚未过原容差，故协议和下游未返。

该事实既不证明放宽owner预算一定收敛，也不证明另一已运行225的paired/cache后继能改变这一owner阶段；225必须由其自身实际记录判断。没有对未启动后置组件造性能数字，没有把原末状态范数、局部残差或recovery差异转成准确连续C或全闭面metric floor。原112/338、两mean、FD、fullDN、fresh audit及完整几何责任仍按各自真实返回分别保留。
