# Request83：唯一原试步与完整精确分解工作流草稿

日期：2026-11-15 UTC。作者：geometry。类型：可执行接线；只做源级静态核，尚未 dispatch 或产生本次科学结果。

## 文件与来源

本目录仅供 root 统一审读、复制和正常 Git 发布，不写共享工作树，也不派发第二请求。

- 工作流目标：`.github/workflows/visible-larger-public-native-realized-trial.yml`。
- 唯一 trigger：`topics/visible-flex-larger-amplitude/computations/public-native-realized-trial-request.json`。
- job/lane 保原 `modelresponse`，只是现有输出路由；科学输出有独立 actual73-realized schema。
- 已有 69 工作流是比较基线，完整工作流和 request diff 均在本目录。
- 20 个实际源 pin，包含新三份 probe/fetch、exact 新完整分解源、原 R276/整数核及其 source-receipts 所需旧 73/factor/byte/flow 源、原 client/runtime/transport/resume/publisher。
- publisher 保当前实际 `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`；没有新增 publisher lane。

四个新运行源分别来自：

1. `/tmp/native-realized-trial83-source/geometry_20261115_native_realized_trial_probe.py`，`305f5db2…`。
2. 同目录 `geometry_20261115_native_realized_trial_probe_hook.mjs`，`c03f59e4…`。
3. 同目录 `geometry_20261115_fetch_actual73_realized_selected.py`，`51f86528…`。
4. `/tmp/native-realized-step83/exact_20261115_native_realized_step_affine_decomposition.py`，`3570aa9f…`。

完整 SHA 位于 request 的 `source_sha256`；`source-locations.json` 只是 root 复制用的本地路径表，不是未来 Actions 数值输入。

## 一次取件与顺序

同一 job 只取一次固定 actual73 ZIP：run `43657001633` / artifact `14141540502`，1,752,742,419 B，SHA `3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9`。固定取件器保原冻结 512 transport 的 **全部五个显式 tuple flags 和 `--out`**；该原 parser 不接受只有 `--out` 的调用。新科学源码没有为这个接线遗漏作任何修改。

只提最后 snapshot、完整方向及原 signed-e 所需原件。probe 与 exact 阶段共享同一 `actual73-selected/`，不重复下载、不重新生成 J、不取 factor/constants。原 78 公开源恢复仍使用原 `prepare_public_source`。

随后：

1. 固定末轮原状态与方向，在 Node 中逐字执行原 `v+lambda*delta`，固定 `k=9`。
2. 一次原完整 `evaluate(false)`，保全实际 trial state、完整返回 out/r/cut/far、mean 及原 root 返回观察。
3. 从刚产生的真实 `actual73-realized-trial/result.json` 生成 SHA；这个值不在 request 中预填。
4. exact 消费上述实际结果、同一保存 J 和已付 signed-e，计算完整 `h=trial-base` 的精确作用及逐行分解。不重算 Jδ、不重跑 no-J。

已付 R276 小 gzip 从公开 Git 精确 sparse 取入：

`topics/visible-flex-larger-amplitude/notes/2026-11-15-actual73-r276-iteration002-original.json.gz`

12,153 B，SHA `b7812e06716bb1d22d4d32ff6ca12c62cb926dd9df12f41c199988f933ccd029`。本地静态核用 root 已下载 reader 中该相同原 gzip，只读取长度和 SHA，没有重算科学。

## 环境、预算与保全

Python 3.12.14、Node 24.22.1、numpy 2.3.5、scipy 1.17.0 和原 setup/upload action SHAs 保持 69 原值；Node heap 6,144 MiB。取件 25 分钟、原 no-J 35 分钟、exact step 35 分钟且内部预算 1,800 秒 / workers 2；job 120 分钟，为两独立科学阶段及 transport/upload 留出真实总时间。这个资源预算不改变任何原容差、32 轮、10 步或科学门；本次本来就只请求一个诊断试步。

最低可用存储 8 GiB，日志明确完整 ZIP、选择性最后一轮 J、输入/方向和输出范围；不声称原完整 native 多轮容量保障，不删除科学现场。

token 只在固定取件和原 publisher 环境出现。probe 和 exact step 都没有 token。`upload-artifact` 和 publisher 均 `always()`，完整 `large-arrays/` 与全部部分失败保留在 artifact；Git 仅沿既有 bounded publisher 规则。

当 probe 本身未完整返回时，后续 exact step 按默认成功依赖不执行，原失败证据仍由 always artifact 保存。没有以 exact 缺陷、范数重现或原 root 读数新添科学接受条件。

## 已做静态核及明确未做

[原静态回执](2026-11-15-request83-workflow-source-static.json)：56 项通过，20 个文件 pin 实际逐 SHA 核，10 个 shell block 仅 `bash -n`，6 个 Python heredoc 仅 AST（具体计数以该冻结 JSON 为准），全部必要 `.mjs` 仅 `node --check`。完整 transport CLI 参数已按原 parser 源逐项核。真实 source-only producer 往返另有 22 项检查。

未设置假 `GITHUB_ACTIONS`，未导入任何科学 producer，未构造 native、未形成 trial、未调用 root/RHS/J/ODE/QR/no-J，未做 exact 点积。未生成未来 run/actual probe result SHA、未宣称科学成功。

主控全文读四新源/两接口/实际workflow/request，核20源/10shell/6inline与原R276gzip：[主控回执](2026-11-15-request83-root-static-check.json)。冻结科学源/工作流/请求字节不变，未来结果SHA只在实际运行产生。
