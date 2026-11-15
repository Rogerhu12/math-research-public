# Request118：原31查询加入 midpoint471，从真实 actual98 另起32查询批次轨迹

类型：独立计算入口与执行接口；尚无 request118 数值结果。  
作者：ChatGPT / exact_refinement。日期：2026-11-15。  
本次交付仅源码、参数、来源与运行协议；所有新的科学计算只在公开 Actions 中执行。

## 1. 已有证据与本次动作

Actual110 的真实 run 是 `43685348016`，source commit 是 `8d4a3af1d553cd85cfa9694ec8cfaf1c0b66ce3f`。该次八个原模型及各自新 warm 的完整边界 FD 均完成；第1至7批的最近拒绝试步，都只有原 collocation midpoint471 失域。第7批接受 `alpha=0.00048828125`；最近拒绝的 `alpha=0.0009765625` 在 midpoint471 给出原 `beta_squared_minimum=-3.8894462797367524e-05`，原31个已选查询在该试步均有效。上述数值仅从实际110的原短报告逐字段读取，未在本地重算。正式结果见 [actual110 结论](2026-11-15-actual110-eight-real-pairs-and-midpoint471-barrier.md)。

原31已经包含 LEFT471，但该查询使用原左 RMS 分数 `0.17267316464601146`；它不是 `state.middle[471]`、`problem.mid[471]` 所定义的原 collocation midpoint。Request118 只补后者的全部2048个角点约束，保留全部原31查询。

Actual110 的最终 warm/status 已按规则删除。它们的 SHA 不能恢复场。本次初始场使用仍能从真实 actual98 原 artifact 取回的 warm/status，另起32查询轨迹；不称作 actual110 末场续接。110提供选查询的证据，未提供本次父状态。添加该查询也不保证最近拒绝位置、接受步长或非线性下降一定改善。

## 2. 唯一真实初始父件

| 项目 | 固定实际值 |
|---|---|
| 原 run | `43677587785` |
| 原 source commit | `918fdb11dbb7a424b6149b405e2c7fab3cc0c737` |
| 原 artifact ID | `14147700690` |
| artifact 名称 | `visible-followup-condensedqp-43677587785-1` |
| 完整 ZIP 字节数 | `809042943` |
| 完整 ZIP SHA256 | `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a` |
| 原 warm | `thirty-one-condensed-warm/warm-001.json.gz`；`4927052` 字节 |
| warm SHA256 | `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67` |
| 原 status | `thirty-one-condensed-warm/driver-status.json`；`3379453` 字节 |
| status SHA256 | `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff` |
| 首父 schema | `exact-constraint-thirty-one-query-condensed-complete-H-warm-v1` |

沿用原 `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` 运输核及实际98原只读 helper 的运输接口：核官方 metadata/source、完整 ZIP 大小与 SHA，再安全索引 ZIP，仅提取这两个完整成员并核其大小、SHA和完整选中成员 CRC。拒绝绝对路径、父目录穿越、symlink、重名和文件/目录前缀冲突。完整 ZIP核验与选中成员CRC不冒充未解压成员的独立CRC审计。

新 support 中专门保留 `PARENT_OPTIMIZER_SCHEMA` 为31；`OPTIMIZER_SCHEMA` 为32。首父的 JSON、gzip、producer 或 status 不改写。实际98虽有一个可用 progress warm，其 `success` 和 `new_coupled_finite_acceptance` 仍是 false，绝不是 native 或完整 BVP 的接受锚。

四个原数学输入也逐原件从上表实际98 source commit 的公开 Git对象恢复：

| 临时输入名 | 原 topic 内路径 | SHA256 |
|---|---|---|
| `accepted.json.gz` | `notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz` | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| `prepared.json.gz` | `notes/public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz` | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| `tail-anchor.json.gz` | `notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz` | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| `tail-config.json` | `notes/public-actions-43588155190-1-prepare112/T112-config.json` | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

工作流显式 fetch 该历史 commit，不切换科学 checkout，也不假定已经清理的旧 notes 仍在 main。原 `prepare_public_source` 恢复78个公开来源，保原 source-origin 及 SHA，设置 `VISIBLE_SOURCE_TOPIC`。原 `source-dependencies.json` 的 SHA 是 `7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941`。

## 3. 唯一查询变化与完整支持

新 domain schema 为 `captured-thirty-two-query-original-RMS-and-collocation-midpoint-domain-v1`，新 warm schema 为 `exact-constraint-thirty-two-query-condensed-complete-H-warm-v1`。

原20个 LEFT 查询依次是：

`464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487`。

新12个 MID 查询依次是：

`471,473,475,477,479,480,481,482,484,485,486,487`。

行序仍为全部 LEFT 后全部 MID，每组完整角下标 `0..2047`。新 MID471 是 group20；原11个 MID 的相对顺序不变，组下标各后移1。总数从63488增至65536。`ADDED_QUERY_SPECS` 恰有 MID471 一个元素。旧 metadata 中 LEFT464、LEFT486、MID486 的“新增”改为“保留”，当前唯一新增项明确是 MID471。

原 LEFT471 已使区间471以及端点471、472进入同一次完整原 Jacobian捕获，因此本次：

- 保原20个捕获区间，不额外调用完整 J，也不增加端点捕获。
- 保完整25个物理端点 `464..488` 及3个全局参数，B-local维数8453，实际列并集等于声明支持，零布局列仍为空。
- 保原 C 的物理节点 `471..482`、维数4059，以及所有完整外部响应。C外节点仍为 `464..470,483..488`。
- 保原全坐标236036及完整 A、AT、g、权重、chart scale、基准 C 投影、完整 H仿射消元和恢复。没有把 C外坐标清零或冻结。

新中点使用原有限计算对象，不用左RMS插值冒替。完整导式仍是

$$
dy_{\mathrm{mid}}=\frac{dy_L+dy_R}{2}-\frac{h}{8}(df_R-df_L),
$$

其中完整端点 J、参数 P 与 query 处直接标量控制项全部保留。每批 B、C、H及原 g 都由该批真实父场重建；不复用上一批方向或 QR。不跨批相减不同权重下的 merit 来声称同一个目标下降。

## 4. 科学入口与原预算

每批独立子进程先调用新32 observer入口，后调用新32 response入口：

```text
python -u geometry_20261115_thirty_two_query_collocation_observer_warm.py
  --accepted INPUTS/accepted.json.gz
  --prepared INPUTS/prepared.json.gz
  --tail-anchor INPUTS/tail-anchor.json.gz
  --tail-config INPUTS/tail-config.json
  --resume CURRENT_PAIR/warm-001.json.gz
  --expected-resume-sha ACTUAL_CURRENT_WARM_SHA
  --parent-status CURRENT_PAIR/driver-status.json
  --expected-parent-status-sha ACTUAL_CURRENT_STATUS_SHA
  --out BATCH/thirty-two-condensed-warm
  --iterations 1 --damping 270 --lsmr-iterations 200
  --projection-sweeps 200 --line-search-steps 17
  --budget-seconds 1200 --angles 4096 --jac-workers 2
  --condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90
  --condensed-recovery-reserve-seconds 30 --condensed-max-working 512
  --condensed-dual-sweeps 200 --condensed-store-root
```

随后原 FD 命令的 `--prepared` 指向该批实际保存的新 warm，参数仍是 `--angles 4096`，其余 accepted/anchor/config原件相同。FD对应的真实 warm SHA与原返回标志照原110生命周期核对，不把父场的 FD 改标签。

全原17档非线性回溯、全部节点/中点/RMS/边界/固定权重merit及方向可用性检查不改。原 C备份、可行径向修复、完整模型同 f候选比较和恢复后 A/AT/B/BT读回保留；不引入新 residual/KKT/最优性阈值。新B查询是明确的算法范围扩展，并非声称原31与新32的 B 数组相同。其余科学代码和旧冻结源未修改。

## 5. 临时 pair 与批次生命周期

独立 worker CLI：

```text
python -u geometry_20261115_thirty_two_temporary_batches.py
  --repo-root GITHUB_WORKSPACE
  --request computations/public-thirty-two-batch-request.json
```

新 worker 加载纯stdlib `root_20261115_thirty_two_temporary_readout.py`；它只负责取原字节、运行子进程和读取既有JSON字段，不导入科学 producer。

首次只允许上表实际98的31-schema父pair；新32 producer自己逐SHA核这个首父。以后同job生成的32-schema pair可按原完整 producer/identity合同续接。每批只有真实新warm出现、status指定其实际SHA且原FD在该warm完成后，才允许交给下一批。

真正的 warm/status用 `os.replace` 原样移动到下一临时carrier，移动后再次核完整bytes/SHA；不重新序列化、改producer、改status或只传hash重建。下一批前删除已经读完的上一批科学输出和旧父pair。失败时不伪造下一父场，保已打印的真实标量/退出码/失败原因后停止。

最多8批；每批仍是上节原1模型+新warmFD。批间总时钟预算10500秒只决定是否开始下一批；不改动进行中的原子模型预算。科学step175分钟、job185分钟，超时属于运行资源限制，不能冒作数学不可行、原验收通过或完整八批结果。

本次并未设置与 actual110 第0批字段/文件相等的通过条件；query算法已经改变，`reference_first_batch=null`。`field_identity` 沿原110定义，仅为解析后所选JSON字段的规范编码SHA，明确不是native f64数组逐bits身份或完整warm文档SHA。

## 6. 短读回与所有未付责任

每批短读回复制原 model/status/QP/FD的已保存字段，包括全部实际外试探、每组32个已选beta最小值/负值与非有限计数、最近拒绝的真实失败点、全RMS记录、真实collocation最坏行及原冻结权重读数、原QP完整模型标量、真实新warm/status/SHA及FD。

原model与status嵌入model仍按明确科学字段比较，独立文件provenance不强求相同；这些都是读回事实，不新增科学门。科学脚本本身仍产生原完整临时数组和报告，因此读取不是凭缺省值拼造成功。没有独立重新审计巨大数组、没有声称原RAM-only完整QR已导出。

每批输出 `BEGIN_THIRTY_TWO_BATCH_SCALAR_SUMMARY` / `END_THIRTY_TWO_BATCH_SCALAR_SUMMARY`，≤90000字节时打印完整选定标量摘要。超限先作明确较小的标量选择，若仍超限只打印实际状态/退出码/来源和省略范围，不分片传播原数据、不用读回大小改变科学接受。最终 `thirty_two_batch_chain_end` 给出真实完成数、每批输入/输出pair SHA、alpha、各自当前模型merit和停止原因。

new32新metadata `query_changes_since_this_model_input` 明确区分首个31父与后续32父。读取位置是实际 `status.identity.thirty_two_query_projection_entry.parent_optimizer_schema`；不会因读取不存在的顶层键把首次新增悄悄记成空。

输出中 `success=false`、`new_coupled_finite_acceptance=false`、`native_at_current_height_solved=false` 等范围保持原暖启动性质。本次不调用native、完整fullDN或闭场验收，也不建立这些层面的新通过声明。

## 7. 完整来源、工作流与规则

`public-thirty-two-model-recipe.json` 列明全部75个源码SHA和1个原参数manifest：保原107的全部70pins，再加独立32四源与新support/readout。旧107单模型helper只保来源，不调用其main；旧31入口也不会被改成32执行。新batch worker为第76个显式源码pin，放在独立 trigger request中，避免自哈希循环。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261115_thirty_two_query_domain_operator.py` | 34371 | `a55edba9bf4dde9c909ceb6aa47aee5957ed4d26fa13dd40f8bf38d9ce74df0f` |
| `geometry_20261115_thirty_two_query_condensed_warm.py` | 47422 | `3f4162b9594acb5c7607f3329e757dad3e18311a1544ea20a081f5c4689cafb8` |
| `geometry_20261115_thirty_two_query_condensed_response.py` | 2619 | `47f420ad7dcddee0192ac6eb02aec4caedbfb66e3100d5fe879261cc33251e73` |
| `geometry_20261115_thirty_two_query_collocation_observer_warm.py` | 16728 | `845af95d9481ef2c30bf76d8169f91c5a3640980400b0b69828cf6c7cadb3f5d` |
| `root_20261115_thirty_two_temporary_readout.py` | 16470 | `a05af3878e1f93c66a8f0b253be0936ddc4342438f4dbd13d4ed178ed6f4955d` |
| `geometry_20261115_thirty_two_temporary_batches.py` | 26571 | `336fc52205446977ed936035e06818abc2aebb732d1b41c8d8f2fb49eb2266b0` |
| `public-thirty-two-model-recipe.json` | 25194 | `f5c0e2e67fa7855ce074a144f8b8223aedd028cd27e77f053c38f335f9342e26` |
| `public-thirty-two-batch-request.json` | 4071 | `1a446102f3a8b6018efa5c9e4ce3a2e4c70979bf05fd2545ad8f67e9dc9056b3` |
| `visible-larger-public-thirty-two-batches.yml` | 7828 | `96eeef3bf91a4ec26fc773e3c8a5cc2e020f7b029b3543140042962f79b64028` |

唯一新工作流是 `.github/workflows/visible-larger-public-thirty-two-batches.yml`，仅push main且新 `computations/public-thirty-two-batch-request.json` 改动触发，独立concurrency `visible-larger-thirty-two-real-pair-batches`，不取消进行中任务。

沿原 checkout/setup精确版本、Ubuntu24.04、Python3.12.14、numpy2.3.5、scipy1.17.0、BLAS线程1。checkout保根/题README、H和computations，`persist-credentials:false`；关闭Git gc/maintenance，`merge.stat false`避免已清理历史raw的无用diffstat读取。

原规则runner SHA `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde` 沿110调用。其baseline显式绑定根README blob `74c08a36f6c997d0bc1e64a7956b42276f5fa5d7` 和题README blob `bff8aea253a9e6a7a4fac28d810ac454c5499fec`；启动及每2700秒在独立mirror真实pull/rebase、按原规则差异停止，H只同步唯一规则行，科学checkout不换。Token只从GitHub Actions进程环境供原Git/取件，不写入文件或日志。

按规则15，不上传新raw artifact或Release，不把计算结果/巨大审计入Git。所有原数学输入、完整父ZIP、每批临时科学数组/status/warm/日志均在独立 `RUNNER_TEMP/visible-thirty-two-118-*`，消费者结束后移除；工作流always清理仅本请求拥有的临时目录。原公开历史Git对象/原artifact不是本workflow删除目标。这里只发布脚本、完整参数、run/source/SHA及紧凑结论；没有将临时文件误称已持久保存。

## 8. 已完成的静态范围

只读源构造时，原 domain 的 query/角值、捕获视图、完整矩阵构造、verify/export 的数学AST（仅声明标签归一）与31一致；原 warm 的 evidence、原C project、完整choose/condensation/recovery、原observer和CapturedLinearization等八项AST原样。新4源的FD数学及原observer函数由独立薄适配保留。所有前述检查均未导入或执行科学模块。

完整本地源字节核对了recipe75个实际payload及新增worker，原70pin与参数manifest未变；5个shell块 `bash -n`、3个inline Python及所有入口AST/compile通过。首父31/当前32区分、唯一MID471、原capture/C/local维数、原模型flags与原8批生命周期均已源码核对。这是实现核对，不是数学正确性或未来接受证明，也不作为额外运行门。

构造脚本、完整diff、AST/静态回执只放临时交付目录，可从公开源重得；不把可重算审计资料作为新的持久数据发布。
