# 新 gamma 六控制 / 九维 KKT 的实际初根失败与 03b 自然退出

日期：2026-11-26。第 36 步已真正执行新控制族，返回完整科学失败报告；第 37 步纯 reader 没有获得准入。GitHub job 的 completed/success 是控制器正常保存后退出，不是科学研究完成。

证据：[公开 part-009](2026-11-26-public-actions-45820592817-1-part-009.md) 第 36 条，读取时 Git blob `46399b57c9dda80c265dd9a503f73d91b946928b`。另独立读取 GitHub job `139911515943` 的实际终态和完整公开 job log；仅在本文保留必要紧凑事实，未上传完整日志或逐角报告。

## 1. 完整实际输入

run `45820592817/1` 的实际第 36 步：
`complete-added-gamma-nine-KKT-strict-same-reference-first-20261126-03b`，
source commit `29bd4c0b94a9f777e2e40248fe911cf8bb51d9b7`。

| 角色 | 完整源码 SHA256 |
|---|---|
| launcher | `e0925d2628bf88760042dcdc3d998ec3a4ff51977d49a4568f6a543bf5fa4bb0` |
| driver | `5134d34d4f4393fc57d86eed329bd107b631b693668d1d04d602af5f286dc3f5` |
| gamma/KKT endpoint operator | `b712a24a0c0223356b4a53e6aa1fa78ba9cea66e4be39c7ee39931be99cb782a` |
| 完整几何 | `0c4886237d642382a1ae329d36517d5752ba717f0fa1471993bb98769e828f17` |
| 独立 new-input binder（本次未选其 new-reference 模式） | `ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39` |
| 完整 base operator | `7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf` |

本次 input_mode=same-reference。固定 g 为 `6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb`，Q definition 为 `05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e`，实际 reference 初点仍为 `cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3`。H-only 的报告作为完整地点来源，不把其 efe120 初点当本次初值。

新模型身份 `ba1cae53201a88c1574c89d05af88455b2a4550633ac755261f4a604bb6f71c7`。全部 1,333,370 个原自由量、45,324,288 个完整 metric 行保留；局部控制维数 6，KKT 维数 9，二阶角 jet 隐式系统维数 27。代价为
$$
\frac12\bigl(|z/S|^2+|v|^2\bigr).
$$
gamma 支撑三节点是 (1/16,1/8,3/16)。数值 control radius=2、multiplier radius=64、physical endpoint tolerance=dimensionless KKT tolerance=2e−12；旧三控制球或 IFT 证书没有转移。SOSC_verified=false、global_minimum_verified=false。完整 scientific argv 和所有八个 manifest 逐项保存在公开第 36 条。

## 2. 确实进入 KKT 科学计算，未达到最终方程

第 36 步实际 236.806650368002 s，exit 1。科学报告
`zero-closure-added-gamma-KKT-first/report.json` 为 1,301,127 bytes，SHA256：
`b154a2399af7c2b36273c853c3b0eecab03bfb60e22ee47a87f24b23820eca9e`。
完整命令记录 16,675 bytes，SHA256
`0742e2ae5a88cb4f13e1728f959466d18c1b4b48eeef1a05373d57a5457e5d1b`。

stop=`actual_initial_zero_closure_field_read_failed`；
真实 failure_reason=`Continuation step exhausted before the original endpoint equation was reached`。

| 实际量 | 返回值 |
|---|---:|
| 最小最后接受 continuation 参数 | .8610908091068268 |
| 最大最后接受 continuation 参数 | .8611559867858887 |
| rejected stages | 140 |
| KKT angle evaluations | 42200 |
| KKT matrix angle evaluations | 3712 |
| nine-dimensional solve angle attempts | 3294 |
| implicit_matrix_angle_rows 原计数 | 33408 |
| 成功缓存 root 数 | 0 |
| 初始曲率 / 半径永久地址 | 1851 / 1851 |

最后参数均未达到 1，final_original_KKT_reread=false。当前 endpoint / KKT / stationarity residual、controls、multipliers、最小 KKT 奇异值均 null。矩阵计数包含实际工作中的 KKT Jacobian 行，不能把字段名 implicit_matrix_angle_rows 改写为“成功完成了自由点的隐式 J/J*”。

这个结果不是未读 setup 异常的猜测：完整科学报告的 KKT 计数、延拓参数和失败原因都已返回。终态 job log 的 bounded failed tail 也含 `actual-added-gamma-nine-KKT-root-failure-v1`、九维 state component order 和外层 launcher CalledProcessError。但该 tail 只有最后 6000 字符，开头截在策略字段中，没有额外保留实际失败角、控制或残差数值。因此不能用外层 traceback 补造原始 KKT 数值失败细节。

## 3. 原始数值与实现责任的边界

新控制族确实把原固定两 bubble 控制严格包含在更大族中；数值延拓在该次执行未达到最终 KKT。一次驻点分支跟踪失败不证明可行控制不存在，也不证明端点约束秩失败、SOSC 失败、全局不可行或课题无解。当前没有最终 KKT 奇异值或失败完整状态可用于支持那些判断。

本次 5 个摘要缺项是 strict same-reference 模式下不存在的两个 new-reference 专用 provenance 键，以及未产生的 final bundle/两末位置字段。它们不是科学原因。纯 reader 第 37 步没有运行，不能声称它已验证每个快照，也不能把未读失败角填为 0。

后继必须保全实际 30、H-only 34 和 gamma 36 的报告地点责任。若换新 runner，完整同目标重建须用实际返回的身份和地址并集，不由同命令自动宣称原逐字集合已恢复；旧 b154 报告没有被压缩为控制输入，也不能从 SHA 生成它。

## 4. 已核真实退出时间线

完整 job log 确认：

- 18:03:08 UTC：第 36 步 child 启动；
- 18:06:38 UTC：准入关闭，当前 child 继续自然执行；
- 18:07:03 UTC：第 36 步返回 exit 1，并发出原 failed log tail；
- 18:07:06–08 UTC：真实第 36 条和 budget checkpoint 被普通提交并推送；
- 18:07:08 UTC：控制器记录 reason=budget_checkpoint，actual_returned_steps=35，research_complete=false，然后正常 job cleanup。

35 是 followup 数，另有 1 个 warm，故公开总阶段为 36，并不矛盾。GitHub API 对 job139911515943 返回 completed/success，科学执行 step5 也 success；表示控制器正常完成记录。索引的 followup_budget_checkpoint/failed 是持久状态标签，既不是用户研究完成，也不是一个后来启动的第 37 科学阶段。第 37 pure 和未准入的 fingerprint 不能记为已运行。

本题完成责任继续未付；新的全变量机制和固定 g 精化研究在后续活跃 runner 继续。
