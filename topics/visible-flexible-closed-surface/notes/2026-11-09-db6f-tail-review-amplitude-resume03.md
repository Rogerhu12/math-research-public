# continuation03 恢复入口：独立全文与真实元数据审查

2026-11-09，`/root/tail_theory`。审查者未参与本准备器实现；只读原控制器、client、worker 及冻结的准备器/启动文件，并另写独立元数据核查。没有导入或调用求解模块，没有新 root、RK、DN、候选、配置或启动动作。

**结论：所绑定的 continuation03 准备入口 PASS。** 这是从真实已收敛有限 warm 恢复原算法的输入审查，不是新求解成功或课题完成证明。

## 1. 冻结对象

| 文件 | SHA256 |
|---|---|
| `scripts/db6f-prefix-prepare-amplitude-resume03.py` | `c45222bf707d7a91d5d3c2bbab4e48abe8bdfe0b38e94b584eb41b81a4bac3ec` |
| `notes/2026-11-09-db6f-prefix-amplitude-resume03-launch.json` | `0e0f020b7c879790d9e6b3726f324cbde6a2c724f43b3dca5fff30d370a42e3c` |
| `notes/2026-11-09-db6f-prefix-amplitude-resume03-source-check.json` | `ba64ac7ab6098750724e992d85c562559705a2a426e787aec965fc90312f9c84` |
| `notes/2026-11-09-db6f-prefix-amplitude-resume03-interface.md` | `8293d61725a609b2f38541ab54eb3410b3ae8d11ced7f2b70dc94562c32a5034` |
| 原 continuation 控制器 | `23f75c9ecc2825e4a8314468775c40b06b6b47439edd0d0ed9a69a9fb5e298a9` |
| 原 continuation client | `cd9b25521427dcefebd5baddcf6a105c58c53f495cf8692fb725d49e4558a564` |

独立核查程序为 `scripts/db6f-tail-review-amplitude-resume03.py`，SHA `32a7006bdac244b8e6baa5b80c05f4493cf390325d66a5f9e1ce57596979680b`。实际运行 receipt `043017`，exit 0，输出 `notes/2026-11-09-db6f-tail-review-amplitude-resume03.json`，SHA `794052a0edd01765e16c9490594af6c8476cd09867a89acbc575cf2a806debba`。

## 2. 恢复数据与故障身份

恢复文件严格为旧 02 的 `..._tail_0015.json.gz`，SHA `e6ef3389c839be9f793a11d875d99c616c207acc58b680efc0bda2c005e55c1f`。原请求是 $s=31/32$，residual 为 `6.367950627222893e-10`，小于原 `2e-9`；`converged` 为真正 JSON `true`。该响应没有 Jacobian/source audit，准备器也没有将其重标为最终目标或完整前缀。

启动文件的 83 个来源逐一重新核 bytes/SHA，并核它们包含原 02 启动的 66 项、call15 已闭审的八件文件、根 ENOSPC 观察的九件文件、实际响应的八个源。原来源数组与文件哈希都是冻结输入；没有用一个未绑定的 `verified=true` 代替这些核验。

根观察绑定明确为 session `17869`、receipt `cf4fa6`、实际工具 exit 1。其 child/worker 直接退出值没有观察，仍保留 null。Python run.log 的 `OSError: [Errno 28] No space left on device` 与 call16 worker trace 的 `ENOSPC` failure 互相吻合。完整 call16 response 及 controller reproduction 不存在；陈旧 RUNNING progress 和中间 iteration 不作为恢复成功依据。本审查不将该基础设施中断归为原方程不收敛，也不推断缺失的进程退出值。

## 3. 参数、槽和物理目标

准备器以 canonical JSON 比较原 config 与真实响应 config，明确剔除且仅剔除五个 I/O 键：`initialCheckpoint`、`iterationCheckpointFile`、`traceFile`、`trialDiagnosticFile`、`trialStatePrefix`。因此 bool 不会与整数 0/1 混为相同。实际 M15、spacing3、depth12、p8、steps32、N256、maxIterations36、solveTolerance2e-9 及 .05 正性门保持原值；默认全模 initial-boundary correction 仍开启。

目标 affine prefix 的 `actual_nonlinear_tail` 明确为 false。其全部 physical-tail 参数逐键与原配置一致。按原 NumPy 表达式逐模计算

$$H_j(31/32)=H_{\mathrm{goal},j}(31/32)^{j+1},\qquad j=0,\ldots,14,$$

真实 request.height 与 checkpoint.cutHeight 逐值相同；这些是物理高度，不额外乘除 $c^4$。

自有核查实际遍历 865×30 个非 bool 有限 shape 标量。rawNode 恰为整数 $0,72,\ldots,864$，13×30 个 rawStates 与相应 shape 行作严格带类型比较相同。这里保持原 Q/Pi 槽和原 native 网格；没有插值、缩放或偷偷使用 call16 中间态。历史七个基点的整数序号也保持原 0,…,6。

## 4. 原命令的四项变更与 warm 语义

以冻结旧 launch.command 作比较，仅四个选项值改变：新 03 out-prefix、initial-step `1/64`、上述真实 call15 response、resume-scale `31/32`。Python、控制器、source-root、原 config01、原目标、maximum/minimum step、64 次尝试和 heap1536 全部 token 不变。首个新目标精确为

$$\min(1,31/32+1/64)=63/64.$$

`initial-scale=.25` 在有 resume 时不会覆盖这一首目标。准备器及本独立检查均在实际核验时确认新 O03 stem 尚未占用；准备元数据位于独立名字下，不预建 03-config 使原 controller 的拒覆盖门失效。

原 controller 运行时才复制 config、重写四条活动 I/O，并把 call15 指为 initialCheckpoint。fresh client 不保留旧 cache。worker 只把加载 CP 当 warm，仍按原逻辑缩放初猜并作全部高度模态的线性边界修正，再重新解原 nonlinear 方程；没有直接返回旧响应。worker 只在成功后更新 last，controller 还要检查原 residual 容差；失败候选不会成为下一次 warm。

当真正达到 $s=1$，原 controller 发送独立的 `goal.copy()`、`jacobian=true`、`audit=true` 请求；audit=true 不允许 client 缓存代替该计算。即使该目标 DN 成功，仍须原 prefix 外层真实边界校正及后续 N512/实际图认证。

## 5. 独立检查中的已记录小失误

本审查的第一次元数据检查 receipt `23b91c` 实际 exit 1，且没有生成报告。原因是检查器把字面 `ENOSPC` 错查在 Python run.log；该日志写 `Errno 28`，worker trace 才写 `ENOSPC`。这不是作者准备器或实际 CP 的缺陷。

首次执行源码保存为 `scripts/db6f-tail-review-amplitude-resume03-pre-log-token-fix.py`，SHA `e672655a33e8c3488d6b56d4b37b4ca2c77b759b9005f0f8fd1b7ce3fec2a9da`。只将末段日志条件改为分别核两个实际来源后，所有独立检查完整重跑通过。未修改任何作者源、旧记录或数学输入。

## 6. 最终验收仍未发生

作者接口说明中的最后门是正确且必要的：原 controller 可捕获异常后写 UNCONVERGED 并以工具 exit 0 结束，因此不能只看工具退出；必须核新运行自己的 status、target_reached、target_audited、最终原响应及 Jacobian/audit/schema、来源和真实 worker 退出。外层观察记录也不能覆盖 controller 自己的 reproduction。将来使用 03 的 final preparer 必须显式采用 03 身份，不能改旧 v2 的标签来冒充 02 已完成。

本轮 PASS 仅支付冻结的 03 恢复入口及来源一致性，零求解器调用；不宣称任何未来目标、闭图或 README 门已完成。
