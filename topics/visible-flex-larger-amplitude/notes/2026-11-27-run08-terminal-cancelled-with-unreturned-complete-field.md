# Run08 终态：公开 job 已取消，第11个完整科学子步没有返回

2026-11-27，Astra-larger-e4e2a2bf-20261126。本文只登记实际 API 与公开分卷边界；没有重新执行科学入口，也没有读取或转存 runner 的大型科学报告。

## 1. 实际观察与准确终态

在实际时钟 **2026-11-27 08:25:18 UTC**，GitHub jobs API 返回 run `45929088658/1` 的 job `140277268174` 为 `status=completed, conclusion=cancelled`。其中第5个执行步骤“Execute public research and publish independent compact records”同为 `completed/cancelled`。随后读取 run API 也得到 `completed/cancelled`；其 `updated_at` 是 `2026-11-27T08:24:27Z`，这只是 API 的实际更新时间，不擅自改称精确科学子进程结束时间。

实际 run 创建/开始时间均为 `2026-11-27T02:34:05Z`，push head 为 `291adcd2b2f4de1dac4c7118dbce69b471dc5813`，workflow 为 `.github/workflows/visible-larger-adjacent-frame-20261127-08.yml`，workflow ID `432280277`。完整运行入口见 [Actions run45929088658](https://github.com/Rogerhu12/math-research-public/actions/runs/45929088658)。

这次 API 观察没有给出取消原因的 annotation。虽然运行位于工作流预算边界附近，本文不把这一时间关系写成已经核实的取消因果，也不把基础设施取消解释为数学不可达、Newton 失败、QP 失败或度量失败。

## 2. 最后公开科学记录仍只有1–10返回

最后读到的公开索引是 [run08实际索引](2026-11-27-public-actions-45929088658-1.md)，原 Git blob `28aef15fd9a5abbcfc5534d57863bed70b724040`，完整 UTF-8 4784 字节，SHA256 `f98f2bb93bb36a9a5b98de9505c0ac48f4654ee7e3fd1675964253f53999ac4c`。其记录时钟为 **08:08:18 UTC**，最后阶段明确写为：

`followup:complete-independent-fixed-chart7c-full-envelope-20261127-08`，`running`，实际子进程“尚未退出”。

已返回分卷仍仅为：

- [第1卷1–5](2026-11-27-public-actions-45929088658-1-part-001.md)；
- [第2卷6–10](2026-11-27-public-actions-45929088658-1-part-002.md)。

这给出明确的执行边界：第11个完整独立7c固定目标科学子步确实已经开始，然而没有公开返回它的退出码、完整 report、最终 checkpoint、首次完整场、方向或真实几何筛结果。第12个纯读步骤也没有公开返回。索引在 job 取消后仍保留旧 `running` 字样，不能据此把 job 说成仍活动；同样不能用 job 的 `cancelled` 补造科学子进程的退出码。

第10步实际冻结当前7c目标与完整旧 carrier 的结论保持原值；它只是必要输入成功，不能晋升为第11步已经产生可接受物理场。

## 3. 原完整科学源、参数和未返输出责任

实际第11步的完整 source 保持：

| 源文件 | 字节数 | SHA256 |
|---|---:|---|
| `fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py` | 75152 | `95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9` |
| `launch_reference_centred_independent_chart_material_envelope_so3_actions.py` | 20746 | `10422033f229649aa2e8237c25880670219d618d24690d429025347fd73f039b` |
| `read_reference_centred_independent_chart_material_envelope_so3_report.py` | 98389 | `f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470` |

这些入口来自原已刊独立7c家族；本次终态登记没有换成随后 actual09 的解析 frame/J3 家族。完整科学后缀、全部变量、32个 normal 阶段、完整 P0、旧/当前两套材料格、typed 责任以及真实几何筛均由原入口保留。

完整活动参数仍在 [run08完整队列](../computations/resume-20261127-followups-08.json)，原 Git blob `5bd35d6a1b12becc5ac5378d3db291d8ccd75d48`，54743 字节、SHA256 `7df46214e1aaa4414050e20bf1be759d20f398eaf229bef47a88e9f561201559`。该文件保第10步的16个 argv 字、第11步的139个 argv 字及第12步的7个 argv 字，并保全部原 headers、summary 选择器、清理范围和历史归档指针。第11/12步 parent 均是本 run 已实际存在的 `axisymmetric-R690-reference-v2-first/reference.npz`。

第11步约定的输出为：

- `reference-centred-independent-chart-envelope-normal-lift-first/report.json`；
- `reference-centred-independent-chart-envelope-normal-lift-first-command.json`。

纯读约定输出为 `postprocess/reference-centred-independent-chart-envelope-normal-lift-first-readout.json`。这些是完整参数约定的路径，**不是本文已取到的文件**。本文不填它们的未知 SHA，也不把未取得的 checkpoint、root packet、frame/矩阵计数或 typed 记忆冒作空对象。

## 4. 后继历史责任与研究状态

独立7c目标仍与历史90目标及 actual09 冻结目标严格区分。第11步运行中可能形成的物理地址属于原 source 定义的完整材料包络；然而它的实际 typed 首发现来源、保护角色和选择顺序没有返回，不能自动视为已经逐项继承。已有完整来源闭包及后继独立策略中的未知并行历史义务继续保留。没有把 job 取消变成删除这些责任的授权。

本记录可以让状态页把 run08 的活动槽改为终态并指向完整证据；它不要求继续占用活动 heartbeat。原完整 source、参数、输入冻结成功、先前实际失败及已返分卷都保留。没有取消/重跑其它正在活动的 job，没有新科学 fixture，没有本机科学执行。

## 5. 这次真实 API 与源身份小记录

下列 JSON 是从实际 API 返回中选取的完整相关元数据；其 `run_api_returned_json_text` 明确指向原返回 JSON 文本的 SHA/字节数，不声称下列排版是原 HTTP 字节。job 的全部实际步骤按原结构保留。这里没有科学数组或大型原始日志。

```json
{"schema":"actual-run08-terminal-api-observation-v1","observed_at_utc":"2026-11-27 08:25:18 UTC","run_api_url":"https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/45929088658","run_api_returned_json_text":{"sha256":"566f6c71c063cbdcd9bb13f17e26936ad060604932a51ec902a2f3de31a47f75","bytes":13467},"run":{"id":45929088658,"status":"completed","conclusion":"cancelled","run_attempt":1,"head_sha":"291adcd2b2f4de1dac4c7118dbce69b471dc5813","workflow_id":432280277,"path":".github/workflows/visible-larger-adjacent-frame-20261127-08.yml","created_at":"2026-11-27T02:34:05Z","run_started_at":"2026-11-27T02:34:05Z","updated_at":"2026-11-27T08:24:27Z","event":"push"},"jobs":{"jobs":[{"id":140277268174,"name":"Continue full adjacent-frame normal research with actual complete inputs","status":"completed","conclusion":"cancelled","run_id":45929088658,"logs_url":null,"steps":[{"name":"Set up job","status":"completed","conclusion":"success","number":1},{"name":"Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","status":"completed","conclusion":"success","number":2},{"name":"Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","status":"completed","conclusion":"success","number":3},{"name":"Install the recorded numerical and automatic differentiation dependencies","status":"completed","conclusion":"success","number":4},{"name":"Execute public research and publish independent compact records","status":"completed","conclusion":"cancelled","number":5},{"name":"Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065","status":"completed","conclusion":"skipped","number":9},{"name":"Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262","status":"completed","conclusion":"success","number":10},{"name":"Complete job","status":"completed","conclusion":"success","number":11}]}]},"public_index":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-45929088658-1.md","git_blob":"28aef15fd9a5abbcfc5534d57863bed70b724040","sha256":"f98f2bb93bb36a9a5b98de9505c0ac48f4654ee7e3fd1675964253f53999ac4c","bytes":4784,"recorded_at_utc":"2026-11-27 08:08:18 UTC","last_public_stage":"followup:complete-independent-fixed-chart7c-full-envelope-20261127-08","last_public_stage_state":"running","last_returned_stage":10},"complete_active_parameter_queue":{"path":"topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-08.json","git_blob":"5bd35d6a1b12becc5ac5378d3db291d8ccd75d48","sha256":"7df46214e1aaa4414050e20bf1be759d20f398eaf229bef47a88e9f561201559","bytes":54743},"source_records":[{"name":"fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py","git_blob":"74b94de90794b10aaa628789ed6ee2d958b58bce","sha256":"95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9","bytes":75152},{"name":"launch_reference_centred_independent_chart_material_envelope_so3_actions.py","git_blob":"701ea523e04a426974206e1168416f68a82bdaf3","sha256":"10422033f229649aa2e8237c25880670219d618d24690d429025347fd73f039b","bytes":20746},{"name":"read_reference_centred_independent_chart_material_envelope_so3_report.py","git_blob":"67e9e6de5091367410ebc1cf9fd109e96ada6858","sha256":"f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470","bytes":98389}],"scientific_child_result_for_stage11":null,"scientific_child_exit_code_for_stage11":null,"stage11_report_or_final_returned":false,"stage12_pure_readout_returned":false,"cancellation_cause_from_actual_annotation":null,"unreturned_typed_memory_is_empty":false,"unreturned_field_or_root_failure_inferred":false}
```

## 6. root实际复核

root在2026-11-27 08:28:27 UTC另行读公开run API、专用jobs API及完整4784B最后索引，确认上述job/全部八个step记录和只返1–10的边界。API普通fetch不支持的job细项没有作为证据，改用实际专用jobs结果。原run08完整队列继续保留，未将11/12归档为完成；未改09科学或把取消原因写成已知。
