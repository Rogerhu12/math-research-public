# Run09 actual4–5：真实子进程已退出，首场报告未返回，原异常待双 trace 读取

本记录只登记公开 Actions 已返回的两个完整紧凑记录。科学 launcher 的实际退出码为1，只有命令记录输出；纯 reader 也退出1，未生成读回报告。当前证据没有任何新的场、目标值、几何值、接受方向、root 误差或实际耗时分解，因而不把这次返回写成解析 frame 或 normal 数学失败。具体原异常由同一 runner 的原始步骤日志确定。

## 1. 完整公开证据及真实来源

- Repository：Rogerhu12/math-research-public。
- 实际 run：45943410994/1；job：140322567209；本次 run 创建于2026-11-27T05:02:35Z。
- 实际索引：`notes/2026-11-27-public-actions-45943410994-1.md`，本次已读更新时刻06:12:11 UTC，Git blob `247ba3bad3be05b04e30dbb5acfa803d1b9e9ea6`。
- 已完整读取的公开小卷：`notes/2026-11-27-public-actions-45943410994-1-part-001.md`，Git blob `3563795bdc9f2ff2c55d8b362589f989f8d0a52a`，47299 bytes，SHA256 `f196d0efe23e5457611a23b2e0e9bd8e69e898790c41fbcb33a4a23370d9262e`。其 actual1–5 原完整紧凑记录是本记录的依据；没有读取科学大 raw。
- 原科学和纯读两个完整队列对象来源为 `computations/resume-20261127-followups-09.json`，准入提交 `53e8565c7688e1cd2b7c3d4055832ce3ebe86bb5`，实际队列 SHA256 `671d966e187e63a0897a98acd9ccb56d815ab58c6ba74f99be0b59292d5dbbee`。所有原对象和实际失败状态继续保留；新的诊断有独立 step ID，不覆盖或重试旧 ID。
- 两步共同父为实际已存在的 `axisymmetric-R690-reference-v2-first/reference.npz`，整文件 SHA256 `2ab8593585286a6c4eab78d107f83a02d8332e7ae1747253534264506b3da7f2`。没有使用不存在的 final 或首场 report 作为后继诊断的父。

这里的 source commit 是各 child 真正使用的固定来源工作树，不以队列提交代替：

| actual stage | step | 完整脚本 | 实际 source commit | source SHA256 | seconds | exit |
|---|---|---|---|---|---:|---:|
|4|complete-run09-public-reference-analytic-frame-J3-packets-first-20261127|launch_run09_public_reference_analytic_frame_actions.py|3f8725447ecab9fad13525ef233852c0df18d5df|84d453f5dbade82fd10fcbf390d49eb190c063c89cd174dc599c6004f9b46ccd|10.754519880999396|1|
|5|actual-run09-public-reference-analytic-frame-J3-packets-first-20261127|read_run09_public_reference_analytic_frame_so3_report.py|226f6bef7990aa028d43713fa2ab1de6e71abb58|47409b634fe48ffd79738d2456494fdf97db50b1ce00b3553b72f164f263b5aa|5.7503399750003155|1|

## 2. Actual4 的确切输出及未返回范围

唯一实际输出是 `run09-public-reference-analytic-frame-first-command.json`：26382 bytes，SHA256 `17b6390dd32b9e5c0387f0ed94d5db809ec82fab3f927863913fd3ee82d75c81`。它是 launcher 的完整命令记录，不是计算所得的新场。

声明的 `run09-public-reference-analytic-frame-first/report.json` 不存在。controller 的 summary_errors 逐字报告该路径的 `[Errno 2] No such file or directory`，metrics 为真实空对象。所有声明输出的存在检查都在实际 child 返回之后执行。cleanup 的 deleted 与 skipped record_count 均为0；本次没有登记任何 generated cache 删除。

不能据这些字段填入以下任何数值或状态：

- 原场或最终场 Phi、完整观测最大 Gram 残差、连续整面误差；
- 初次 root 的失败角、normal stage、残差、Jacobian、frame/J3 实际计数；
- 首次完整 F、几何、任一方向或 line trial 已完成；
- 新永久点、typed 分离记录、最终 full variable point 或被接受场；
- 解析 frame 与原 AD 的实际速度、数值误差或等价性。

这些量此时没有真实科学 report。保存 command 说明 launcher 到达其命令记录阶段，不证明 inner driver 到达第一场读取。

## 3. Actual5 的确切范围

Actual5 输出列表真实为空。`postprocess/run09-public-reference-analytic-frame-first-readout.json` 未生成，summary_errors 同样是输出文件缺失，metrics 为空，cleanup 两类记录均为0。

该步骤是 pure reader；它没有新的 F/J/root 任务。虽然其参数指向缺失的科学 report，具体触发异常仍须原 log 证实，不把静态路径关系写成已读 traceback。它的退出不提供第二次独立数值实验结论。

## 4. 完整实际命令

以下保存实际公开返回中的 argv 原值和顺序。绝对路径是该 run 真实来源/研究工作目录，不是可向另一个 runner 搬运的 raw。后续若需要重建，应使用已保存的完整参数对象并重新绑定真实输入，不以旧 SHA 造文件。

### 4.1 Actual4

```json
[
  "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
  "-u",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/followup-sources/0003-2fd878d0bca7-3f8725447eca/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_run09_public_reference_analytic_frame_actions.py",
  "--repo",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/followup-sources/0003-2fd878d0bca7-3f8725447eca",
  "--reference-bundle",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/axisymmetric-R690-reference-v2-first/reference.npz",
  "--preparation-report",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/axisymmetric-R690-reference-v2-first/report.json",
  "--carrier",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/axisymmetric-R690-reference-v2-first/observations.npz",
  "--node-report",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/fullclosed_solver/data/fullclosed-hold-warm.json",
  "--scalar-input",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/fullclosed_solver/data/pulse-a5-complete-base.json.gz",
  "--angles",
  "2048",
  "--stage-block",
  "64",
  "--angle-block",
  "8",
  "--integration-order",
  "8",
  "--norm-kind",
  "jet-sum",
  "--radial-norm-length",
  ".05",
  "--angular-transition",
  "24",
  "--torch-threads",
  "4",
  "--damping",
  ".01",
  "--directions",
  "1",
  "--maxiter",
  "16",
  "--restoration-directions",
  "4",
  "--restoration-damping",
  ".01",
  "--restoration-maxiter",
  "64",
  "--line-trials",
  "15",
  "--active-rows",
  "192",
  "--qp-atol",
  "0",
  "--qp-rtol",
  "1e-6",
  "--reach-ratio",
  ".03",
  "--reach-safety-factor",
  ".992",
  "--active-band",
  ".025",
  "--marked-diameter-budget",
  "4.2",
  "--witness-lower-budget",
  ".9",
  "--amplitude-height-floor",
  "1.01",
  "--spectral-p",
  "4",
  "--spectral-epsilon",
  ".001",
  "--spectral-scale",
  ".05",
  "--legacy-fraction",
  ".5",
  "--target",
  "1e-9",
  "--outdir",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/run09-public-reference-analytic-frame-first",
  "--panels",
  "128",
  "--endpoint-bubble-1-left",
  "1/32",
  "--endpoint-bubble-1-middle",
  "1/4",
  "--endpoint-bubble-1-right",
  "15/32",
  "--endpoint-bubble-2-left",
  "17/32",
  "--endpoint-bubble-2-middle",
  "3/4",
  "--endpoint-bubble-2-right",
  "31/32",
  "--endpoint-root-tolerance",
  "2e-12",
  "--endpoint-root-iterations",
  "24",
  "--endpoint-root-backtracks",
  "18",
  "--endpoint-root-armijo",
  "1e-4",
  "--moment-definition-sha256",
  "05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e",
  "--moment-input",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/followup-sources/0003-2fd878d0bca7-3f8725447eca/topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json",
  "--moment-input-sha256",
  "df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c",
  "--endpoint-control-radius",
  "2",
  "--gamma-left",
  "1/16",
  "--gamma-middle",
  "1/8",
  "--gamma-right",
  "3/16",
  "--moment-input-binding",
  "supported-smooth-triangle-reference",
  "--normal-stages",
  "32",
  "--seed-boundary-total-length",
  "1/16",
  "--seed-profile-delta",
  "1/128",
  "--seed-radial-quadrature-order",
  "8",
  "--seed-profile-quadrature-order",
  "16",
  "--seed-mean-maxiter",
  "128",
  "--seed-mean-tolerance",
  "2e-12",
  "--seed-mean-backtracks",
  "24",
  "--seed-mean-armijo",
  "1e-4",
  "--seed-scalar-iterations",
  "64",
  "--manifest",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/axisymmetric-R690-reference-v2-first/locations.json",
  "--material-envelope-binding",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/run09-actual-public-reference-run05-carrier/material-envelope-carrier-binding.json",
  "--envelope-near-active-rows",
  "32",
  "--independent-envelope-branch",
  "--pending-parallel-envelope-run",
  "45909290354/1",
  "--pending-parallel-envelope-source",
  "45909290354/1=cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5",
  "--pending-parallel-envelope-run",
  "45929088658/1",
  "--pending-parallel-envelope-source",
  "45929088658/1=95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9"
]
```

### 4.2 Actual5

```json
[
  "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
  "-u",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/followup-sources/0004-711d2ca6dec4-226f6bef7990/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report.py",
  "--repo",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/followup-sources/0004-711d2ca6dec4-226f6bef7990",
  "--report",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/run09-public-reference-analytic-frame-first/report.json",
  "--output",
  "/home/runner/work/_temp/visible-larger-research-45943410994-1/research/postprocess/run09-public-reference-analytic-frame-first-readout.json",
  "--verify-final-bundle"
]
```

这些命令明确保持原全空间和预算：N2048、全部 M160/current free variables、32 normal stages、完整径向/角向 carrier、jet-sum 坐标范数、metric1×16、restoration4×64、15次 ray、原192前缀加全部包络/幅度/typed 约束、完整真实几何筛。它们是这次实际请求的参数，不冒作任何已完成计算。未知 run07/08 来源仍显式在参数中，不把待处理历史写成已迁移值。

## 5. 首报告及当前 controller 的发布时序

本节是实际已刊完整源的控制流事实，不是实际失败原因。

完整 e3cb driver 在 setup 和初 report 字典构造之后先调用 `write_json(output, report)`，再进入首个 `q.residual(x)`、statistics 和完整几何 scan。首场捕获到指定数值/运行错误时通过 `save_report()` 保存实际错误；首次完整场及几何成功后也再次保存，后续完整方向及最终读取再保存。当前没有首 report，故必须读原 inner log 区分 setup、写文件以及其他真实路径，不能仅按输出缺失猜一个具体函数。

已刊 `public_actions_followups_compact_metadata.py` 的 `run_step` 在 child 存活期间仅执行 maintenance、规则/队列轮询和状态发布。其 `_summary`、声明输出哈希和 missing_outputs 检查都在 child 返回之后。因此现有心跳不会把仍在运行的 child 的中间 scientific report 内容复制进公开 compact。即使 runner 已有中间 report，公开 heartbeat 本身也不能证明或否定首次 F/几何完成。

## 6. 原日志诊断及其明确边界

Actual source worktree tag 和原 controller 的 log 命名规则共同给出真实原日志：

- 科学：`{work}/followup-logs/0003-2fd878d0bca7.log`。
- 纯读：`{work}/followup-logs/0004-711d2ca6dec4.log`。

这些是对应已返回 status record 的原 log；诊断会再次严格核 record 路径、原 source SHA、run ID 和失败退出码，不接受猜测的替代文件。

原 ef017 reader 使用最后一个 Traceback marker；84d4 launcher 的 `subprocess.run(command, check=True)` 可能再写一层 CalledProcessError，所以最后一段可能遮掉 inner driver 的原异常。这只是可直接核对的静态诊断设计原因，不是对本次原日志内容的预填。

独立完整新 reader `scripts/resume_20261126/read_actual_followup_failure_chain.py`：

- 8679 bytes，SHA256 `5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360`；
- 完整源 blob `22e64456b28a246329513397e4ebb22f5687805e`；
- 每步至多读取64000 bytes 原 log 尾；分开保留尾中第一个与最后一个 Traceback，每段至多7000字符，并明确每个剪裁、实际尾起点、是否覆盖全 log；
- whole log 只流式哈希，绝不把完整 log 公刊；status 哈希针对一次捕获字节，原 log 前后 size/mtime 核一致；
- 没有读取科学 report/数组，没有执行 F/J/root，没有推测数值原因。

完整两步参数 `resume-20261127-run09-actual4-5-first-and-last-tracebacks-ready.json`：10608 bytes，SHA256 `6cf9f3704fc05cbf0f049729af786a0d8746a1372523bf00243aeff3753047ef`，完整 blob `253cd784710f770e908557ca40c506693a6b3f9e`。两步的 parent 均为已实际存在的2ab reference，所有摘要 selector 均为标量或明确有界字符串。

本记录写作时，新 reader 仅完成 source-only AST/compile 和完整 JSON 检查，未在本地或 Actions 执行诊断。准入、真实返回及其 inner 异常应由后续实际记录另行登记，不能从本 ready 推定已经执行。

## 7. Root 完整归档及诊断准入

Root 实读全部5条实际公开紧凑记录，并逐对象核原队列四完整步骤与三个归档完全相等；全部 original queue header、argv、summary selectors、outputs、cleanup 和实际返回原记录均保，没有把失败写成成功或把未知步骤归档。固定原队列提交为53e8565c7688e1cd2b7c3d4055832ce3ebe86bb5。归档：

- `computations/run09-returned2-5-complete-archive-part-001.json`：33437 bytes，SHA256 `be0b855ed926ef4fdac3e8ab51ff15749ff1d626dd9bc55483bfe226ece6abfe`。
- `computations/run09-returned2-5-complete-archive-part-002.json`：53858 bytes，SHA256 `b4027658df3c7fabfdeca1cd86d2dfdc8cd77e1eb83c5b913b52b18d4ef49324`。
- `computations/run09-returned2-5-complete-archive-part-003.json`：41049 bytes，SHA256 `6797997423aa61f2887b4eb2bb99721c6a6715d17053ee83b3b4d3da17c1b7fa`。

Root 全文核5d25 reader并实际执行仅源码AST/compile检查；完整两诊断对象与6cf9 ready逐对象相等后排入09活动队列。两个完整源绑定、真实run/status/log路径、失败退出码与有界first/last范围均保。本节只登记准入，不预填诊断结果；原1–3输入不重跑。
