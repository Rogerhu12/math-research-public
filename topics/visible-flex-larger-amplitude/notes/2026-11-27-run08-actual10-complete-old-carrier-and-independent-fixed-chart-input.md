# Run08 实际第10步：完整旧载体重建与新7c固定目标的实际登记

本条只登记已经返回的独立输入生产。公开 Actions run `45929088658/1` 的第10步于控制器记录时间 **2026-11-27 04:27:31 UTC** 返回 `completed / 0`，外层实耗 **555.1088718759993 秒**，生产器内部实耗 **551.5498447010004 秒**。它没有执行场、Jacobian、根或优化方向。后继完整 normal 求解已经另行排队；本条不把准入当作求解返回，也不把输入生产成功当作全题完成。

## 1. 本条所读的完整公开证据

原始公开索引为 [run08 索引](2026-11-27-public-actions-45929088658-1.md)。完整第6–10步紧凑卷为 [run08 第2卷](2026-11-27-public-actions-45929088658-1-part-002.md)。本条读取的是该卷 Git blob `bcecc57ae25fbd86f1fc52e49d796e9fd2ee88a3`，**45797 bytes**，SHA256 `30cf41dcd4b5ee162e7a9c1e25e71c6f479b66ad9b76435a537ab30395fa10ba`，其中第10条完整 JSON 对象。

本条没有下载 716379-byte 原科学报告、406354-byte 输入绑定或原 NPZ 来转存。下面的真实身份、状态和耗时来自这一完整小卷，不从缺失文件或旧索引推测。

| 项目 | 实际值 |
|---|---|
| 完整步骤 ID | `freeze-independent-actual-run08-chart7c-and-restore-full-run05-carrier-20261127` |
| 实际源码提交 | `2edbc6d2b471e74fa60960fc9b2c780d30392c0f` |
| 实际生产器 | `scripts/resume_20261126/freeze_run08_fixed_chart_and_restore_run05_carrier.py` |
| 完整生产器 SHA256 | `105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361` |
| 入口父 reference NPZ SHA256 | `eeb55084744c60a5ed2e2bbb4343b01c73028a6ab61b1216142e4b3bf57dd6b4` |
| 运行时队列路径提交 | `72c29bbf0173a00e235c0e32476101bdf357c368` |
| 运行时完整队列 SHA256 | `d882f5e76e311054362254d008a9f121f4bf7ac1f886e3ec8851a97820d15f80` |
| 完整报告 schema | `independent-run08-fixed-current-chart-and-complete-run05-carrier-input-v1` |
| 报告 complete | `true` |
| 缺失已声明输出 | 空列表 |
| 科学场 / Jacobian / root 调用 | `0 / 0 / 0` |

生产器的完整已刊源与独立推导保留了旧完整2397叶积分表再生、原节点/标量参数投影与 whole-file 门槛。当前完整输入被独立冻结；旧固定图身份没有被改名充作当前目标。

## 2. 完整旧载体已真实命中；地址与当前载体相同

实际旧观测 NPZ 是 **227202 bytes**，完整 SHA256 为

`dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`。

本次 `old_carrier_verified=true`，同时 `old_current_addresses_identical=true`。这是真实完整生产器检查后的读数。当前观测 NPZ 的完整 SHA 仍为 `56b143f1ac7031b5cbeb12d02240fca28a67a57eba9938d5f134e4a1e7094d44`，并未被冒称与旧 whole-file SHA 相同。它们的完整数值/标量或序列化身份可以不同，而本次生产器实际核得材料地址相同。

独立新包络入口仍须读取这两份完整载体及原 P0，用自己的完整数组与位置检查建立有限责任集合；生产器的一个布尔值不替代消费者实际读取。未知旧运行的 typed 首次发现来源、保护角色晋升与选择顺序也没有由这个地址等号“恢复”。已刊独立包络策略明确承担全部原 P0、旧/当前 G、全部曲率分支和双号幅度，并分别说明未知历史角色责任。

## 3. 当前完整实际输入与独立固定目标

| 当前输入或定义 | 完整 SHA256 / 身份 |
|---|---|
| warm NPZ | `4c34e0889a40e67a3a0a38abce030bb0358f74333fc1d8c95f669d5beefd9a0f` |
| 节点报告 | `d7cac2c479defda89980c916f967353f5d1ac27f1c85cb93b37268972a4876d3` |
| 标量输入 | `87bd2a4668638dbd49ec4523b33941c554b06471d1cf0ba522d3ea2a9a36ddb5` |
| reference NPZ | `eeb55084744c60a5ed2e2bbb4343b01c73028a6ab61b1216142e4b3bf57dd6b4` |
| 完整 reference model | `492456a67601cac752dc8e5cb79c14eaccc7339b2d3206f0d570bb60b02c5c5e` |
| 当前 observation carrier | `56b143f1ac7031b5cbeb12d02240fca28a67a57eba9938d5f134e4a1e7094d44` |
| 当前工作 mesh | `eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262` |
| 完整准确节点定义 | `ba5a3188e048f69b6602b4b784640c70932fbc1f53cfbf13b0857ba25e6b4b02` |
| 完整标量参数定义 | `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa` |
| 当前完整160字固定图 | `7c4c9b736c0c8081e9f00a131db5fb63af224aa64fb476c07c78c09b5288bb48` |
| 旧历史固定图 | `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e` |

旧图 `90e6…` 与当前图 `7c4c…` 是不同实际输入。标量参数相同并不能推出整个固定度量相同，因为固定材料角图也是目标定义的一部分。当前独立定义的真实身份为

`d4690aedff83db48c7c14ccf7f25d926ab1f9d30be03777ed473379b27626e57`。

它的完整序列化文件为 `independent-fixed-target-definition.json`，90432 bytes，文件 SHA256 `485aa2726bb403c7e6829bd8f9204b75e181af6ea2a84b4261e2c20c078f9940`。定义的 canonical identity 与文件 bytes SHA 是不同字段，不能互换。

当前完整输入绑定的 canonical identity 为 `7991584eaf9d061a1c0a612a013eb096e3d526f62fff2cbb188c0cce30da1c38`，文件 `material-envelope-carrier-binding.json` 为406354 bytes，whole-file SHA256 `d25db222d015ce24932828297c1156156b596913757ba28a43f467cad74a49c9`。后继源保留“完整目标 == 实际 report/base/reference 整对象”、whole reference NPZ、完整160字图、标量参数和准确节点的交叉等号，并且每次真实 F 前固定该目标。

本次实际返回以下边界均为 `false`：

- `same_original_chart`；
- `same_mathematical_g`；
- `exact_chart_conjugacy`；
- `old_values_inherited`；
- `original_branch_finished`；
- `unread_history_claimed_read`。

因此本条没有宣称旧90图问题已完成，没有用新档案 SHA 清除旧实际历史，也没有把旧场值、旧 Phi 或证书迁给当前新目标。这个分支的用途是让完整新机制在一个真实明确、随后保持固定的目标上继续求解；全变量、32段 normal 链、H² 范数、所有原历史地址、完整真实几何筛查与仓库完成标准均不因此删减。

## 4. 全部实际输出记录

| 原 runner 输出 | bytes | SHA256 |
|---|---:|---|
| `run08-independent-chart7c-run05-carrier/report.json` | 716379 | `2a785c173e3104d8670c52d8ee22346465f0a580129db10f6dbb0457b92c11fc` |
| `run08-independent-chart7c-run05-carrier/run05-observations-restored.npz` | 227202 | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` |
| `run08-independent-chart7c-run05-carrier/independent-fixed-target-definition.json` | 90432 | `485aa2726bb403c7e6829bd8f9204b75e181af6ea2a84b4261e2c20c078f9940` |
| `run08-independent-chart7c-run05-carrier/material-envelope-carrier-binding.json` | 406354 | `d25db222d015ce24932828297c1156156b596913757ba28a43f467cad74a49c9` |

完整文件仍只在原 runner。这里保留实际路径与身份，未把任何大 raw 重包成参数或公开复制。完整原源码、请求、输入恢复链及下面全部 argv 保持公开。

## 5. 实际完整命令

以下逐项保留原小卷的完整实际 argv，包含当时真实 source checkout 和工作路径；没有把当前 main 路径替换成当时已运行源码。

```json
[
  "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
  "-u",
  "/home/runner/work/_temp/visible-larger-research-45929088658-1/followup-sources/0009-4e2385e1d6d9-2edbc6d2b471/topics/visible-flex-larger-amplitude/scripts/resume_20261126/freeze_run08_fixed_chart_and_restore_run05_carrier.py",
  "--repo",
  "/home/runner/work/_temp/visible-larger-research-45929088658-1/followup-sources/0009-4e2385e1d6d9-2edbc6d2b471",
  "--warm-bundle",
  "/home/runner/work/_temp/visible-larger-research-45929088658-1/research/fullclosed_solver/data/fullclosed-hold-warm.npz",
  "--node-report",
  "/home/runner/work/_temp/visible-larger-research-45929088658-1/research/fullclosed_solver/data/fullclosed-hold-warm.json",
  "--scalar-input",
  "/home/runner/work/_temp/visible-larger-research-45929088658-1/research/fullclosed_solver/data/pulse-a5-complete-base.json.gz",
  "--current-carrier",
  "/home/runner/work/_temp/visible-larger-research-45929088658-1/research/axisymmetric-R690-reference-v2-first/observations.npz",
  "--current-reference-report",
  "/home/runner/work/_temp/visible-larger-research-45929088658-1/research/axisymmetric-R690-reference-v2-first/report.json",
  "--historical-public-record",
  "/home/runner/work/_temp/visible-larger-research-45929088658-1/followup-sources/0009-4e2385e1d6d9-2edbc6d2b471/topics/visible-flex-larger-amplitude/notes/2026-11-26-public-actions-45870334713-1-part-001.md",
  "--outdir",
  "/home/runner/work/_temp/visible-larger-research-45929088658-1/research/run08-independent-chart7c-run05-carrier"
]
```

历史公共记录参数明确指向 run05 第1卷；它不是 seed19 的未知原报告。完整当前输入则来自本次 warm 和完整 R690 reference 生产。

## 6. 摘要错误、清理与后继边界

本次 `summary_errors` 恰有两项：

```json
[
  {
    "report": "run08-independent-chart7c-run05-carrier/report.json",
    "field": "failure.type",
    "error": "'failure'"
  },
  {
    "report": "run08-independent-chart7c-run05-carrier/report.json",
    "field": "failure.message",
    "error": "'failure'"
  }
]
```

它们来自成功报告没有 `failure` 对象，而配置仍尝试读取 `failure.type` 和 `failure.message`。实际生产器退出码仍为0，四个已声明输出均真实存在，原完整报告 `complete=true`。不把这两个可选失败字段的摘要缺项改称输入生产失败，也不把它们静默删除于历史。

控制器实际清理记录中 `deleted` 和 `skipped` 都是0项、0已记录bytes；完整空列表 canonical SHA 为 `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`。本步没有删除输入或输出。

截至本条指定索引快照，第10步是最后已返回项。后继95559完整求解与f382纯读已单独公开并排在此生产器之后，是否已开始或返回以更新后的实际索引与完整紧凑卷为准。本条不预填初始场、metric/Phi、QP、normal 成功、连续根支、积分误差或几何认证。输入准备本身的0次 F/J/root 也不意味着后继完整场已可定义或已通过真实筛查。
