# Run09 actual6–7：原 inner traceback 确认相邻帧政策键不匹配

Actual6、7 已真正返回0。它们仅读取 actual4、5 的原 status 与日志，没有执行 F/J/root，也没有重新运行科学 source。原日志明确显示 actual4 在几何检查器构造时被政策字段守卫拒绝，尚未到 driver 的首 report 写入与首次完整场读取；actual5 的原异常则是打开缺失科学 report 时的 FileNotFoundError。

## 1. 完整实际证据

公开 run：45943410994/1，job140322567209。完整已读小卷：

- `notes/2026-11-27-public-actions-45943410994-1-part-002.md`
- Git blob `a78e2b69963a175d182d61a3904f4d37c960bdbb`
- 28209 bytes，SHA256 `a9c858d0cce4e376ba429a8dbd7a930a302164b6dabdbf082063a778c92f93f4`。
- 该卷完整包含 actual6、7 的原返回对象、输出身份、两种 traceback、完整诊断 argv 和来源。不是科学大 raw。

| 实际阶段 | source commit | 诊断 source SHA256 | 实际 seconds | exit | 实际输出 bytes | 实际输出 SHA256 |
|---|---|---|---:|---:|---:|---|
|6|de2503f5935353aa499314cfb7aa9a04fe08cd70|5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360|5.753388651999558|0|10917|6ea4aa5ea8bdfc3c01f21f44898a0de65da8822c7bddde80d2c74c73e505011b|
|7|79aa4023deed17c74d2247a0e406aa7098c8f03a|5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360|5.755188058000385|0|6290|dd3027fbfe5d0aec9d10943d7c1719bb7ef61f12ca0aa381d6f980d92c205b77|

Actual6 输出 `postprocess/actual09-science-first-and-last-original-tracebacks.json`；actual7 输出 `postprocess/actual09-pure-first-and-last-original-tracebacks.json`。两步没有 summary_errors，父均为同一个实际存在的 reference 整文件 `2ab8593585286a6c4eab78d107f83a02d8332e7ae1747253534264506b3da7f2`。

## 2. Actual4 的原异常已经确定

原科学步骤身份仍是：

- `complete-run09-public-reference-analytic-frame-J3-packets-first-20261127`；
- launcher `84d453f5dbade82fd10fcbf390d49eb190c063c89cd174dc599c6004f9b46ccd`；
- source commit `3f8725447ecab9fad13525ef233852c0df18d5df`；
- 原退出1，10.754519880999396 seconds，原结果仍只有26382-byte命令记录，不能改写失败状态。

Actual6 严格核同一原步骤、run、source 和 log 路径后，读到原 log **6387 bytes**，whole SHA256 `33671079a8ece2456621239ad80e51b7b8e3ff91aa3116b016391780319671de`。本次64000-byte尾覆盖整个原 log，前后 stat 一致，两个完整 traceback 均未剪裁。第一个 marker 的全文件 offset=0，最后一个 offset=1196。

原 inner 调用链为：

```text
fullclosed_run09_public_reference_analytic_frame_so3_qp.py:598, main
    screen = geometry_module.GeometryScreen(q, args.repo, budgets, envelope=envelope, ...)
so3_run09_public_reference_analytic_frame_geometry.py:360, __init__
    raise ValueError('The adjacent-frame producer cannot replace roots, stages or the active field chain')
ValueError: The adjacent-frame producer cannot replace roots, stages or the active field chain
```

第二个 traceback 来自 launcher 的 `subprocess.run(command, env=env, cwd=args.repo, check=True)`，最后是该 inner 命令退出1所产生的 CalledProcessError。这层外包错误没有替代第一个真实来源；其完整 argv 已在原 compact 与参数档案保存。最后一行过长而单独2048字符摘录标记 clipped=true，但整个最后 traceback 的7000字符摘录没有剪裁，所以不存在把第一层异常遗漏的问题。

## 3. 完整已刊源把该错误收敛为一个具体键名缺口

独立逐源检查 actual09 的 `so3_run09_public_reference_analytic_frame_geometry.py` 与实际相邻帧 producer `analytic_frame_adjacent_normal_matrices.py`：

| 位置 | 实际完整源中的内容 |
|---|---|
| geometry 构造器 | `adjacent.definition.get('all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained') is not True` |
| 实际 producer `definition()` | `all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained=True` |
| 实际 producer whole SHA256 | `3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695` |

producer 中旧 `all_original_...` 键不存在。几何守卫仍取旧键，故 Python 的 `dict.get` 返回 None，触发原 traceback 所在条件。此次用纯 AST 读取 producer 的完整 `definition`：新键存在且是 literal True，旧键不存在；几何源码中对应旧取值恰一处。没有 import producer，没有运行数字或另造 fixture。

此处用 selected 是当前算法的准确政策声明：局部 J3 已由独立完整解析 producer 选择实现，其原阶段方程、root 求解及角向求解仍保留；不能为迎合旧 guard 增造“原 J3 实现未改变”的旧字段。真正必要的修复是独立新 geometry 将这一取值指向已存在、已绑定 whole source 的新键，再完整更新 driver、launcher、reader 的来源 pins 和再生器。其余身份、full operator、active chain、相邻 helper 本体、全变量、完整阶段和原算法参数均保持。

本次真实异常也说明先前仅 AST/整源重放并不足以发现所有跨模块字段合同错误。它验证了一个具体构造器路径失败，没有验证完整 frame 数值或时间改进。

## 4. 首场及数学结论边界

真实 stack 在 e3cb main 中的 GeometryScreen 构造处中断。driver 首 `write_json(report)`、完整 `q.residual(x)`、statistics、几何 scan 都位于其后。这次不是“首场计算出来但误差过大”，没有可归因的 Phi、Gram 最大误差、root/Jacobian、几何违反或 line-search 结果。

不得把 actual4 记为已接受或已拒绝的新场，也不得从此构造器错误宣称解析 frame 公式错误、normal 系列不可达、完整算法慢或快。参考输入重建 actual1–3 的成功事实继续成立；无需为这个键名修复重跑已实际生成的完整输入。

原运行/未返回并行来源、全 P0、old/current 全材料网格及 typed 历史责任不因这次 setup 失败减去。修复应使用独立新 source 和 fresh 输出/step ID，原失败对象与完整参数保持可追溯。

## 5. Actual5 的原异常已确定

Actual7 核到 pure 原 log **1759 bytes**，whole SHA256 `6d7c3488083fe52e2878b91976388af2a1750fcb1bc5071b502cd699fe82f7d4`。尾起点0，覆盖全原 log，只有一个 traceback，首尾段相同且未剪裁。

其实际调用为 `read_report` 首次 `json.loads(Path(report_path).read_text())`，在 reader line1120 触发：

```text
FileNotFoundError: [Errno 2] No such file or directory:
.../research/run09-public-reference-analytic-frame-first/report.json
```

因此 actual5 没有读到科学 report，更没有进入 model、normal、frame、packet、geometry、费用的后续纯验证。这是明确的输入缺失失败。实际6/7只是诊断成功，不将 actual4/5 改成成功或推定修复后的科学入口已运行。

## 6. 完整诊断命令和输入保真

Actual6：

```json
[
  "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
  "-u",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/followup-sources/0005-4f8bb7ab0524-de2503f59353/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_actual_followup_failure_chain.py",
  "--status",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/status.json",
  "--step-id",
  "complete-run09-public-reference-analytic-frame-J3-packets-first-20261127",
  "--output",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/postprocess/actual09-science-first-and-last-original-tracebacks.json",
  "--expected-run-id",
  "45943410994",
  "--expected-source-sha256",
  "84d453f5dbade82fd10fcbf390d49eb190c063c89cd174dc599c6004f9b46ccd",
  "--expected-log-path",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/followup-logs/0003-2fd878d0bca7.log",
  "--maximum-tail-bytes",
  "64000",
  "--maximum-excerpt-characters",
  "7000"
]
```

Actual7：

```json
[
  "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
  "-u",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/followup-sources/0006-9ab0aafe4b40-79aa4023deed/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_actual_followup_failure_chain.py",
  "--status",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/status.json",
  "--step-id",
  "actual-run09-public-reference-analytic-frame-J3-packets-first-20261127",
  "--output",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/postprocess/actual09-pure-first-and-last-original-tracebacks.json",
  "--expected-run-id",
  "45943410994",
  "--expected-source-sha256",
  "47409b634fe48ffd79738d2456494fdf97db50b1ce00b3553b72f164f263b5aa",
  "--expected-log-path",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/followup-logs/0004-711d2ca6dec4.log",
  "--maximum-tail-bytes",
  "64000",
  "--maximum-excerpt-characters",
  "7000"
]
```

诊断分别绑定捕获 status 的 SHA256：

- actual6：`2f7598c9a83ee015a4dd165b33415ecdcd88c6f307b0a74c4c902537f579cf66`；
- actual7：`871463a0e10fb141a485f8f3a13b3d7fd2a9c7c36dff5591bca42c10c17b3347`。

这些摘要针对真正一次捕获的字节，不将稍后 controller 更新的 mutable status 当成同一快照。两段原 log 在读取前后保持不变；完整原 log 留 runner，公开仅有限 traceback 与来源/长度/hash。两诊断记录均明确 `field_or_J_evaluations=0`、`scientific_arrays_read=false`、`scientific_reports_read=false`、`numerical_failure_cause_inferred=false`。上面的键名归因以真实 inner traceback 与已刊完整源码共同推出，而不是把诊断工具的推测标签改写成数学实测。

本记录形成时，geometry 的独立最小 source 修订正在准备；后续刊布、真实准入与计算返回应分别登记，不提前填结果。

## 7. 完整参数与实际返回归档

根已独立准备完整 `computations/run09-returned6-7-complete-archive.json`，42290 bytes，SHA256 `f37adad1661b4612e7a3433f26fe892c8803dfe29bf960f1cdde827cbb6427ed`。该小档案保留 actual6、7 两个完整原队列对象、对应实际返回及原队列 headers；根逐对象确认相等。本记录形成时该档案在 repository 待提交，后续应与本结论同步发布，不能把“待提交”写成已准入一个新计算。

原诊断完整 source `5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360` 的实际开关和摘要均已经在本次返回中读取：run45943410994/1，首/末 traceback 独立保留、actual log 全部被有界尾覆盖、log 未变、科学 report/数组均未读、F/J 计数0、无推测数学原因。归档没有删除原科学失败 actual4/5；它们仍保其先前完整参数和原返回记录。

实际缺口涉及的完整已刊 source 身份进一步明列如下，避免以短前缀代替全文件：

| source | bytes | SHA256 |
|---|---:|---|
|fullclosed_run09_public_reference_analytic_frame_so3_qp.py|80723|e3cb0f5a0d4b6e0c4771514470a4729a7042505691e5bba02a79fba789a2e141|
|so3_run09_public_reference_analytic_frame_geometry.py|68903|ef121193668791c9c7bc10e8e72314c74ab3c32eff530a4a39dc2ec61d17d409|
|analytic_frame_adjacent_normal_matrices.py|36761|3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695|
|launch_run09_public_reference_analytic_frame_actions.py|21356|84d453f5dbade82fd10fcbf390d49eb190c063c89cd174dc599c6004f9b46ccd|
|read_run09_public_reference_analytic_frame_so3_report.py|97348|47409b634fe48ffd79738d2456494fdf97db50b1ce00b3553b72f164f263b5aa|

原完整58-role source 依赖仍由该 driver 和原准入参数逐文件绑定；这张归因表不构成删除其余依赖或改变身份的替代清单。

## 8. Root 独立核读与旧入口边界

Root 已独立完整读28209-byte实际小卷，且对42290-byte归档的两原队列对象、全部返回对象和queue header再作逐对象等值核，实际验证exit0；全文逐源核ef121构造器和3788 definition，确认上述唯一旧键取值。本文与完整归档同提交发布。

同一旧键也存在已刊完整frame14的755f geometry中；该旧入口未运行通过，不将它或已刊源重放当成成功的科学入口。独立09修订保留旧父体和原失败，N4096实际09候选同步修正，未准入的旧7c及旧J3入口不因为本次归因自动变成可用。所有来源守卫、完整数学方程和参数保持，不以删除guard绕过故障。
