# 匹配切口联解：只读首包与完整关闭审计器

作者：/root/coupled_prefix，2026-11-09。状态：**实现及真实负入口已关闭，完整源码待未参与实现者审查；尚未用本程序运行首包或最终成功正分支。** 这是原有限数值接受条件的来源、身份、schema 与关闭文件检查，不是重新求解或连续几何证书。

冻结程序为 `scripts/db6f-prefix-audit-matched-cut-closed.py`，SHA256：

`af5349d6ea2d7f5f3331aee245bd04b605e0cf6d006d2fb25979fd2adf312b31`。

程序只接受原匹配切口身份

`notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01`。

即使显式传 `--prefix`，解析后的绝对路径也必须等于该路径。其 input-bindings 的 SHA 固定为 `5b184918f4c5a86f10189c5433cd447af4a822856a2fe569df4439e03efdeb21`，121 个输入逐文件核对真实字节及 SHA。不会接收 continuation03、旧 affine 目标或另一个输出 stem 的正结果。

## 1. 首个真实 DN/J 包

`--mode first` 读取该 stem 的 `_tail_0001.json.gz`。原 client 每包用独占文件、一次完整 gzip 写入并关闭，之后才检查 `failed` 或 `converged`。本程序核完整 gzip/JSON 及读前、读后文件状态，并在审计结束前再次核对消费过的文件 SHA。它不读取活动 trace、trial 或 iteration 文件，不要求主求解进程已经退出，也不从首包成功推断外层成功。

原请求必须逐值等于本次已冻结 preparation 的 `actual_restart_request_height`，并且 `jacobian=true,audit=false`。这不是历史成功尾的请求高度标签：已知约 $10^{-19}$ 的重启差仍保留。配置作 typed canonical JSON 比较，避免 Python 的 `True==1` 弱比较。八源集合恰是本次 trial client/worker/core/split、subdivision、warm-remesh、weighted 与 recalibrated 源，均在 121 输入中，且包内记录逐项一致。

正常响应按原七字段 schema 检查：`converged` 严格为真，真实 residual 有限且小于原 $2\cdot10^{-9}$；705 项 Jacobian、17 项 cut-jets、865×30 states、13×30 raw 镜像全部为有限、非 bool 数值。三项 jet 数组长度均为15。原 `audit` 此时必须为 null；rawNode 必须保持原72个 stage 一 raw cell 的布局。参数只排除五个 I/O 字段后与绑定的真成功尾比较，各 I/O 字段再与本次实际配置逐项核对。由此同时支付原 M15、N256、physicalDepth12、p8/s32、guard .05 及其它冻结选项的身份。

实际 failed 响应只能保留原 `failed,lastIteration,checkpoint` schema；null 不会被补成成功数据。本程序报告已观察到的失败文字、实际 lastIteration 和 checkpoint 是否存在，不构造不存在的 residual/Jacobian。正常响应中的历史末基点与最终 residual 不强求相等，因为原 solver 在轮数耗尽后可能做一次额外真实评价。

## 2. 完整关闭的身份链

`--mode final` 必须先取得根会话的真实工具观察：

- `status=observed-process-completed`、`observer=/root`；
- 实际 `session_id=5817`，非空真实 `tool_receipt`，实际 `actual_exit_code`；
- `stem` 是本匹配切口 stem 的 basename 或完整绝对路径；
- `files` 中逐 SHA/字节绑定实际 reproduction、summary、最终 CP、最终 seam 响应及全部系数块。

根记录可以额外绑定外层 guard 的来源、child 观察和不同的 guard stem，但 child 观察本身不能代替根工具观察。实际工具非零退出独立报告为执行未成功；不把它改写为数学无解，也不要求凑齐缺失的成功文件。

随后检查原 `db6f-prefix-run-bound-command.py` 写出的 reproduction：其静态部分必须逐字段等于 121 输入绑定，原命令和 launcher SHA 不变；Python 子进程 exit 为0，summary 的真实 solver_success/error 与 reproduction 相符。Node worker 的退出并非该原接口独立保存的字段，程序不发明此门。

原 coupled 会捕获异常后正常退出，因此 exit0 不能代付 summary 成功。它也会在最终审计前先保存一次 CP，所以 CP 存在和其 solver_success=true 均不能代付最终 seam。完整模式要求 summary、最终 CP、原 collocation 容差、最后实际外层 BC 门和最终实际审计同时满足。

## 3. 原接受条件与实际表示身份

完整 CP 与 summary 除 `seconds` 和 CP 专有的 mesh/chunks/array_format 之外逐字段相同。原脚本在关闭前后分别写时间，所以不要求这两个 `seconds` 相等，也不把机器时钟的单调性作为数学门。

原 collocation residual 不超过 $2\cdot10^{-9}$；`dn_solver=outer_actual_inner_affine`，最后 `actual_outer_checks` 为真实 inner success、actual boundary residual 不超过 $10^{-8}$、实际尾 residual 小于 $2\cdot10^{-9}$。最后行的 tail_calls 指到本次保存的真 DN/J 包；可合法复用同一 H 的 cache，故不要求每个 outer 都有不同包。包内请求与其 cutHeight 自洽，残差与原 BC 记录逐值同。

这是对原源所记录 BC 评价的审计，**不重新计算 BVP 的 ODE/BC**。原外层记录没有另存内层终端完整 node-array，所以程序也不伪称从最终 PPoly 独立恢复了每一次历史内层状态。原已审源的调用与保存顺序是这条数值证据链的一部分。

冻结 profile/chart/physical-tail/cut/gauge/warp 与 warm 同一；最终自由 p、support 振幅及自适应 mesh 可以变化。每个最终系数块必须是本 stem 的原顺序 gzip NumPy float64，SHA/字节、6×(nodes−1)×分块形状、0..45 无遗漏状态分割、全系数有限以及整个递增物理 mesh 都检查。只导入 `numpy` 和 `scipy.interpolate.PPoly` 作保存多项式评价，不导入原 solver/flow 模块。

最终实际请求由该完整保存 PPoly 评价为 $H=-.1Y_Z(L)$，逐值匹配 `tail_seam.tail_record` 指向的新包。其请求必须 `jacobian=true,audit=true`，且包号严格晚于最后外层 BC 记录；原 audit 请求绕过 cache。705/17/schema/参数门同首包，另须原八项有限 audit，seam 的 jets/converged/residual 与该真实响应同值。

程序保留原 mean/nonmean 一二 jet mismatch、cut metric 及 C1 metric 诊断，但不为它们新设 $2\cdot10^{-9}$ 阈值。原 seam 角样本960、prefix audit角样本1024、tail auditSteps32 均按真实源区分。source prefix metric、source tail actualMetric 及 fullD 等分别报告，不称它们为已证明的闭图连续 metric，也不把本检查代替公共 C² 表示和后续 whole 证书。

## 4. 最小调用

在本题目录执行，输出必须是尚未存在的小 JSON；程序只新增该审计报告，绝不覆盖输入、原输出或已有报告。

```bash
python scripts/db6f-prefix-audit-matched-cut-closed.py \
  --mode first \
  --out notes/2026-11-09-db6f-prefix-matched-cut-first-dn-audit-01.json
```

最终自然关闭且根真实观察已经写完后，采用实际观察文件路径：

```bash
python scripts/db6f-prefix-audit-matched-cut-closed.py \
  --mode final \
  --observed-execution notes/2026-11-09-db6f-root-matched-cut-s63of64-observed-execution.json \
  --out notes/2026-11-09-db6f-prefix-matched-cut-final-audit-01.json
```

此处第二条的根观察路径是待实际关闭后填入的接口，本文不制造该观察或成功数据。可用 `--check-current-gate` 代替 `--out` 作零写入检查。通过返回0；缺证据、真实数值未成功、非零执行退出或身份/schema拒绝返回2，并分别命名状态。

## 5. 本次实际验证和限度

只进行了语法 AST 检查，以及以下真实负入口：

```bash
python scripts/db6f-prefix-audit-matched-cut-closed.py --mode final --check-current-gate
```

工具 receipt `7e744c` 实际 exit2，返回 `NOT_READY`，原因为缺少根实际工具退出观察；0 文件写入、0 solver/flow/RK。没有读取新首包或任何活动 trace，没有制作假 final packet 或 positive fixture。独立审查者将全文核源码；真实正分支由 root 在审查后按已关闭文件运行。

完整有限 M15/N256 通过之后，仍沿已审 N512 真校正、完整 XYZ/公共 C²、连续 metric/曲率/reach/矩及独立端到端执行路径推进。本审计不会把有限联解完成等同 README 总完成。
