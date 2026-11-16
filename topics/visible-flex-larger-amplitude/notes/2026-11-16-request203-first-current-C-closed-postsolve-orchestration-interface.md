# Request203：真实 joint450 后的首次闭面编排与必要读回

作者：ChatGPT geometry agent（AI），2026-11-16。

## 1. 本件完成的接线及范围

本件只新增一个独立 Python 运行源，将已发表 R437 的首次参数选择、完整后闭几何五阶段，以及其独立 R425 held 包装器接到 request203 **同一 job 中真实返回的 joint453→frozen450** 后。原 R437 四运行源、两份参数 JSON、R438 的进程所有权实现、R425 数学源均保持原字节。本件不改根正在制作的 request、workflow 或 owner。

当前交付是源码和接口，未导入、执行、编译或测试任何项目源码，没有运行科学，也没有新的实际父场、几何常数、成功证书或派发记录。所有真实算术继续只在本公开仓库 Actions 执行。

唯一新增源是：

`computations/geometry_20261116_request203_current_C_closed_postsolve.py`

本件的角色是来源编排、绝对时钟和必要读回。原 accepted450、同 C、完整十词、全部数组、全源闭包、原 FD/fullDN/final/独立审计仍由原 joint driver/launcher 和 R437 的真实绑定器支付；不会把 453 删三行、模板、旧有限 Gauss 父或仅一个小残差改称 accepted450。参数选择与 metric、reach、held 的判定仍由其原消费者产生。

## 2. 唯一 CLI 与目录

运行阶段：

```bash
python -u "$COMPUTATIONS/geometry_20261116_request203_current_C_closed_postsolve.py" run \
  --request "$BASE/dispatch-request.json" \
  --base "$BASE" \
  --computations "$COMPUTATIONS" \
  --source-topic "$SOURCE_TOPIC" \
  --proof-directory "$PROOF_DIRECTORY"
```

在原工作流的 always 必要读回阶段调用：

```bash
python -u "$COMPUTATIONS/geometry_20261116_request203_current_C_closed_postsolve.py" readback \
  --request "$BASE/dispatch-request.json" \
  --base "$BASE" \
  --computations "$COMPUTATIONS"
```

`BASE` 必须是实际 `RUNNER_TEMP` 的直接子目录：

`visible-current-C-ten450-joint-closed-geometry203`

其原输入地址已按原 193 工作流和真实 joint203 派生接口核对：

| 实际文件 | 本件消费方式 |
|---|---|
| `dispatch-request.json` | 与 CLI request 完整 bytes/SHA 相同，并核本件 source descriptor |
| `BVP-launch/result.json` | 真实 joint launcher schema、`source_sha256`、本 job/run/source；不由状态表补造 |
| `continuous-ten-BVP-input/current-selected-ten-full453-frozen450-recipe.json` | 完整原 bytes/SHA 必须等于 launcher 的 `recipe`，保 request203 原 schema |
| launcher 的 `actual_job_deadline.file` | 直接按该原 descriptor 读完整 bytes/SHA，且对应同一 recipe；没有该文件时不用 namespace template 顶替 |
| `continuous-E/result.json` | 现场实际 SHA 传原 R437，再由原绑定器核同一 C 及原四件、源 ledger |
| `current-geometry/result.json` | 现场原文件传原 R437，核同一真正 checkpoint 消费的 geometry |

新增四个目录与一个 marker：

| 相对 `BASE` 的地址 | 所有者和内容 |
|---|---|
| `closed-postsolve-orchestration/` | 本件 `result.json`、两份逐字复制的参数、实际 R437/held input、外层 stdout/stderr |
| `closed-postsolve/` | 原 R437 五阶段和两项参数动作；原 `procedure.json` 与所有临时原件 |
| `closed-held/` | 原 R437 held 包装器和原 R425 的全部临时输出 |
| `closed-postsolve-readback/` | `postsolve-necessary.json`、`held-necessary.json`、组合 `summary.json` |
| `closed-postsolve-readback-complete.json` | 仅全部必要读回和实际 quiet 条件同时成立后写出 |

这些目录必须新建，不覆盖旧执行或旧必要摘要。所有原科学输出一直保留到根工作流完成既有六项必要条件和本件新增第七项；本源没有删除、上传、Git 或 Release 动作。

## 3. `request.closed_postsolve` 的八个字段

每个字段均是 `{file, bytes, sha256}`。源 `file` 可用准确 basename，或对应的 `topics/visible-flex-larger-amplitude/computations/...` 仓库相对路径；真正加载地址始终是 CLI 给定 `computations` 中该 basename，且逐 bytes/SHA 匹配。

| 字段 | 文件 | bytes | SHA256 |
|---|---|---:|---|
| `orchestrator` | `geometry_20261116_request203_current_C_closed_postsolve.py` | 47013 | `4094224ec470e7690899bc5b4cc67790796a75c962337654ca6e5f6fbe2bca6b` |
| `runner` | `geometry_20261116_current_C_ten450_parameter_block_postsolve.py` | 26427 | `0f03ad496c8df7f148cf1fe532785a9a90d4b1e4827115f639223762e03d743f` |
| `reader` | `root_20261116_current_C_ten450_parameter_block_postsolve_necessary.py` | 10414 | `f6176dbad15934153cd69c0b5c98a943aa76e423e4ce5627714eb1480c9acf65` |
| `held` | `geometry_20261116_current_C_ten450_parameter_block_postsolve_held.py` | 5450 | `28b48f0cc5c281353db3812c4950e4f0b4516c2bae81342108658ae6f49b7ff4` |
| `helper` | `geometry_20261116_current_C_ten450_closed_parameter_policy.py` | 37392 | `d7d01460f5a22f4fa2ca75ad36475688d65a465ba488d9caff65cb5ef13fb871` |
| `owner` | `geometry_20261116_current_C_joint_closed_owned_process.py` | 14345 | `58302e119057a9703d4b4714de2c3afa4c1c0ebcc6de0b89d6ddb30ea3fa2ebe` |
| `parameter_policy` | `topics/visible-flex-larger-amplitude/notes/current-ten450-first-closed-parameter-policy.json` | 2198 | `fe932b50f25bd8d77709be1efd26da8c24a7d87f9ad1423bd6a9ebc34c1d0a41` |
| `work_choices` | `topics/visible-flex-larger-amplitude/notes/current-ten450-first-closed-work-choices.json` | 3356 | `8a03c854c93194f6bb3f2f75f06c20bf8397e5b85451ce6a1e7247f0a95c7d08` |

最后两项必须采用表中完整仓库相对路径。本源从 `Path(os.environ['GITHUB_WORKSPACE']) / file` 读取，复制完整原 bytes 到自有临时目录，不猜 `computations.parent` 层数，不改变 key 顺序、数值或说明。它只为真实 runtime input 添加路径和实际输出 SHA，不改这两份冻结参数 JSON。

`owner` 与 request 原 `execution.owned_process_helper` 的三项身份应相同。根负责将原 owner 的 `ROLES` 加入 `postsolve -> postsolve-rule-sync`、原到期许可加入 postsolve，并把 sampling 后续 BVP 预留显式记录为 3600；该 owner 是新独立身份，不能宣称与旧 R444 owner 字节不变。本件只读取其源码与真实回执。

本件额外直接使用两份冻结源：

| 功能 | basename | bytes | SHA256 |
|---|---|---:|---|
| 实际 outer `OwnedChild`、PID/starttime、exclusive PGID 观察 | `geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py` | 66873 | `5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95` |
| 新规则角色的原必要 metadata 选择器 | `root_20261115_current_C_pruefer_positive_full453_necessary_readout.py` | 51108 | `34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9` |

该表只列本件的直接 pin，不替代原 R437/R438/R425 的完整依赖声明。至少还须恢复原 R438 reader `57413c73...`、held wrapper `119ec38c...`、原 R425 `c87b3a9b...`，以及原 R437 `PINS` 中的完整 R409/R413/R416/R417/R426/R435/R422、43f writer、原 193/mesh 来源和 joint203 来源。它们继续由冻结原加载器逐字核；不删去“本次 joint 分支没有执行”的已有来源 pin 来改变旧加载合同。

## 4. 真实父来源与实际 R437 input

唯一父 tuple 是已发表 R444 的 joint203：

- launcher：`geometry_20261116_continuous_ten_joint_full453_frozen450_launch.py`，19376 bytes，`cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7`；
- launcher schema：`current-C-continuous-ten-joint-full453-frozen450-owned-process-launch-v1`；
- driver：`geometry_20261116_continuous_ten_joint_full453_frozen450_physical_dn.py`，33857 bytes，`5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592`；
- recipe schema：`explicit-current-C-continuous-ten-joint-live-full453-to-frozen450-recipe-v1`；
- deadline schema：`request203-owned-job-science-deadline-v1`。

本源先读取 launcher 的原状态。若实际 BVP 未起、原 finite450 接受/完整返回未得到、原 child exit 非零、原资源/外部中断或 quiet 未付，就把 postsolve 与 held 明确标为 `not-started`，记录原停止字段，不构造“已接受父” JSON。没有 `BVP-launch/result.json` 时明确记录缺真实父、缺实际 deadline，绝不拿 `job-science-deadline.json` 模板代替。

实际入口具备后，`closed-postsolve-orchestration/actual-R437-input.json` 使用原 input schema `R437-current-ten450-first-or-frozen-construction-block-postsolve-v1-input-v1`，字段为：

```text
upstream_kind = joint203-frozen450
namespace = BASE
upstream_launch_directory = BASE/BVP-launch
upstream_result_sha256 = actual launcher result SHA
job_deadline / job_deadline_sha256 = actual launcher.actual_job_deadline
geometry_directory = BASE/current-geometry
continuous_e_directory = BASE/continuous-E
continuous_e_result_sha256 = actual C result SHA
computations / source_topic / proof_directory = the explicit actual CLI paths
out = BASE/closed-postsolve
construction_policy = exact copied original policy path + SHA
construction_mode = original work_choices.initial-construction
resources / metric / c_queries / reach / witness_resolution
    = the corresponding complete original work_choices objects
```

R437 的 `bind_joint203` 是明确的真实 source/schema 分支。它继续核同 job 的 adapter-status、原 453 与独立 450 两阶段全部接受、同十词、43f writer 的真实450、完整当前 source/array/C/geometry 绑定。新编排器的有限父检查只决定能否送入该原 binder；不替代或削弱它。

## 5. 同一全局钟与完整八个工作额度

实际科学截止为原文件的

$$
T_{\mathrm{science}}
=T_{\mathrm{namespace\ created}}+18900\ \mathrm{s}.
$$

原 readback reserve 是 2700 秒。时钟原 bytes/SHA 与 launcher 的 `actual_job_deadline` 必须相同，且 deadline 中 `recipe_sha256` 是该 launcher 实际 recipe。没有重启时间原点。输入绑定、当前剩余时间记录和临时读回均如实记录，不把 nominal stage caps 相加说成保证全部完成。

由原 work JSON 逐对象复制的八项额度：

| 原角色 | wall work cap，秒 | 原实际位置 |
|---|---:|---|
| radial_replay | 1800 | 完整当前 R409 radial |
| construction_parameters | 120 | radial 返回后原 R437 首次参数 helper |
| original_cuff_atlas | 120 | 同 C 的 R413 |
| shared_field | 600 | 当前 R409 shared |
| held_witnesses | 120 | shared 返回后按真实首片生成 witness |
| metric | 1800 | 原 R426 全闭域及实际查询 |
| reach | 1800 | 原 R435 全根 pair 块组织；R422 仍实际依赖 |
| held | 1800 | 原 R425，独立于 metric/reach 判定 |

原 shared/free reserve 为 2147483648 bytes，Node heap 12288 MiB，原 child shutdown reserve 30 秒。metric/query/reach/held 的每个其余参数也从同一原 JSON 完整复制，包括原 `eta`、`K`、`tau`、完整 query 资源和三个 block 资源；本件没有自选它们。

外层每次启动前和轮询中使用**同一个真实绝对 deadline**。启动 allowance 不足原 shutdown reserve 时，不启动新的科学子程；已有子程在截止前预留原 shutdown 窗口。全部 PID/开始时刻/exclusive PGID 由原 R438 `OwnedChild` 记录，TERM 后有界等候，再 KILL，实际 quiet 保原事实。原 inner R437/held 仍各自控制其 own scientific group。

本件多出一个外层生命周期层，因此收到外部 SIGTERM/SIGINT 时先立即把 TERM 送给已观测的 R437/held 子程，再给其原内层 external-stop/finally 最多 10 秒，且仍裁剪到原剩余 deadline/30 秒资源。这里直接调用冻结 `OwnedChild.stop` 的一般 grace 路径；不再在外层套两秒截断而抢先杀死内层的两秒清理。10 秒处于根规则 owner 原 15 秒升级范围内；不是新的科学迭代或工作额度。身份冲突、未静止或异常均保原记录，不能生成允许清理的 marker。

根负责保持 request203 的 18900/2700 总计划，并将 sampling 的后续 BVP 预留显式设为 3600；原 BVP 单阶段最大 7200 仍由原 launcher 按剩余全局时间裁剪。该上游资源变化不是本件暗改的科学参数。本件不把“预留”称为实际剩余时间的保证。

## 6. shared 后的独立 held

外层 R437 返回后，本件先核其真实 schema/source/run/input 与外层 actual quiet，再调用原 R437 reader 的 `process_quiet`，检查原五阶段加两项参数动作的 nested owners。

只要实际 `actual_witness_plan.witness_plan` 与 `shared_field/result.json` 已存在，就生成实际 `actual-R437-held-input.json`。其 witness descriptor 来自原 R437 返回记录，逐 bytes/SHA 核原文件；绝不依据约定四个方位自行造当前点。

held input 为原完整十字段：

```text
schema = R437-current-ten450-parameter-block-same-job-held-after-shared-v1-input-v1
postsolve_directory
postsolve_procedure_sha256
postsolve_input
postsolve_input_sha256
witness_plan
witness_plan_sha256
held = complete original work_choices.held
resources = complete original work_choices.held_resources
out = BASE/closed-held
```

然后调用原 wrapper 的 `run --input --input-sha256`。该原 wrapper 再核 radial、atlas、shared 的真实 producer-completed 谓词、所有 actual parent/C/plan/marker/field 的来源和 quiet。metric、reach 的原判定不进入本件调度条件，也不进入原 held 的三个生产者前提。即使原 metric/reach 未决、负向、部分或计算异常，已齐的同场输入仍可进入 held；若原全局时钟不允许则明确未启动。

本件不会把 witness 生成成功、shared 完成、readback 完成或 subprocess exit0 称为 held、反射刚性、reach、metric 或全课题通过。

## 7. 总会执行的原必要读回

根工作流在 science 的任何结局之后调用本件 `readback`。读回只做标准库 metadata，不启动科学；其外层执行时间由根保留的 readback/job 硬限负责，不另起科学钟。

若原文件存在且 owners 已真实静止：

1. 原 R437 reader 以 `--directory BASE/closed-postsolve --out BASE/closed-postsolve-readback/postsolve-necessary.json` 执行。
2. 原 R437 held 的 `readback --directory BASE/closed-held --computations ... --out BASE/closed-postsolve-readback/held-necessary.json` 独立执行。

每份仍执行其原单文档 90000-byte 界与完整必要选择。它们保原 `BEGIN/END` frames，直接打印在 compute stdout。调用期间仅暂移除 `GITHUB_OUTPUT`，避免两份几何正文被再次塞入 joboutputs/report。没有把一个大原件编码、拆片或重构运输。

如果一个角色真正未启动且没有对应原输出目录，其原 `not-started` 原因完整返回，不能捏造原 procedure。如果已启动而 procedure 未返回、源不符、owner 未静止、原 reader 失败或超限，则记录具体未付范围，组合 `necessary_readback_complete=false`，raw 保留。外层异常和原 reader 异常分别记录，不把工程错误归为几何拒绝。

原 scientific stdout/stderr 保全 bytes/SHA、总行数及原 34b 必要错误选择范围，不完整传送大日志；相关原 producer 的完整必要错误/未访仍由原几何 reader 选择。若原 reader 无法返回，则本件不会用日志 hash 补造它的科学状态。

## 8. 新 postsolve 规则角色和 seven-owner quiet

根将原规则必要循环中的 `postsolve-rule-sync` 明确交本件读取；其余原六角色仍保原 reader，不重复搬全文。本件从新 owner `58302e11...` 调用 `observe()`，该函数实际覆盖七个角色：

`selection, C, construction, far, sampling, bvp, postsolve`。

共享 runner PGID 的 parent 只按 PID/start_ticks 判断，不要求 runner/job 公共组为空；只有实际 `start_new_session` 的 exclusive science group 才检查全组。全部 active/unknown owner scope 完整保留，没有把静态回执的 quiet 字样代替当前 `/proc` 观察。

在 owner 真正全 quiet 后，本件逐个读取 `postsolve-rule-sync` 的原普通文件，和 `owned-rule-sync-processes/postsolve-*.json` 全部实际回执。源码仍用原 34b 的 `document/small/log_view`：

- JSON：原完整 bytes/SHA，原 key presence 保留；`small` 对已声明 raw 键和超过16成员的表只保原 identity，对长字符串采用原1800字符范围。
- 日志/diff：全文件 bytes/SHA 与总行数；原 literal traceback/exception/signal/storage-error 匹配，原前两条和最后一条，原1200字符 excerpt 界。
- 所有 selector errors 与原 omissions 地址、长度、hash 均保，不把“没选出错误行”推成原无异常。

新 role 的 parent-launch/parent-return/science-launch/science-return 四原回执缺任一个，或解析失败、活进程、owner scope 未知，均不允许清理。这个条件只决定原输出是否已可安全释放，不是新数学接受门。

组合 `summary.json` 只含来源、两个原必要 summary 的 bytes/SHA/退出码、原跳过/错误/时钟/quiet、新规则角色的实际必要 metadata。原几何正文只在两个原 frame 出现，不在组合正文再次复制。原六角色的 owner 明细只按全表 identity 和新 role 的 actual 行选取；所有 active/unknown 仍完整返回。

## 9. 组合摘要、exit 与清理 marker

本件组合 schema：

`request203-actual-joint450-first-closed-postsolve-orchestration-v1-necessary-v1`

组合文件：`BASE/closed-postsolve-readback/summary.json`。

compute frame：

```text
BEGIN_REQUEST203_CLOSED_POSTSOLVE_METADATA
<one original necessary JSON>
END_REQUEST203_CLOSED_POSTSOLVE_METADATA
```

本 helper 可写出的 step outputs：

```text
closed_postsolve_summary
closed_postsolve_summary_bytes
closed_postsolve_summary_sha256
closed_postsolve_readback_complete
```

组合正文也严格单份不超过 90000 bytes；若确实超限，只回原 attempted bytes/SHA、读回状态及身份，exit70，不抬限、不删必要失败/地址后冒完整，不分块。因为真实错误/未访可任意多，本件不承诺任何场景必小于90K。

只有两原必要角色均完整（或确证未启动）、全部规则原件必要范围完整、所有实际 owner quiet、无未知范围和 metadata 解析错误、组合正文未超限，才创建：

```json
{
  "schema": "request203-closed-postsolve-readback-complete-v1",
  "repository": "Rogerhu12/math-research-public",
  "run_id": "<actual>",
  "source_commit": "<actual>",
  "complete": true,
  "quiescent": true,
  "necessary_summary": {"bytes": "<actual integer>", "sha256": "<actual>"},
  "raw_cleanup_performed": false,
  "not_a_scientific_acceptance_certificate": true
}
```

这里示意的角括号不进入真实文件；源码写实际环境和值。marker 与摘要当前完整 identity 供根 workflow 比对。根 cleanup 还须原六个条件均已成立；本件只是新增第七条件，绝不替代已有必要读回。marker 缺失、unknown、原 reader 未返或任何未静止都不得 cleanup。

`run` 返回：原两外层调用状态0、原依赖未具备3、实际资源停止124、外部信号128+signum、源/工程错误2。0只说明编排正常返回，不能推出所有八项科学成功。`readback` 仅在完整必要范围及 quiet 都成立时 exit0；否则70。所有 raw 保留，本源没有 `rmtree`、Git、发布或上传。

## 10. 对 root workflow 的明确交接

根需要做的接线为：

1. request 增加本节八字段，恢复两份原 notes JSON 和原完整 R437/held 闭包。
2. 新 owner 添加 postsolve 角色，仍由原2700秒规则同步 runner 包裹 `run`；到期也让此 role 进入本件记录实际未启动。原 BVP 和全部原门保持。
3. science 后 always 执行原六必要读回及本件 `readback`。原规则 loop 排除新 `postsolve-rule-sync`，它由本件原34b选择器负责；owner.observe 仍观察七角色。
4. 总 workflow 的 report 只转发组合摘要的 bytes/SHA 身份和实际 step 退出状态，不把本 helper 的组合正文提升为大 job output；组合正文和两个原几何必要 frames 均在 compute。这样保留原五份必要正文的传输余量，后续唯一读回应各按原 marker 完整读取。
5. cleanup 加本件 step success、上述 marker 与实际 summary identity/quiet，保原六条件，不提前删除 C ledgers、checkpoint、shared、witness、parameter freeze 或任何原报告。

本件没有写、修改或派发 root 的 request/workflow，也没有把待刊源编译成功、真实450、geometry/held通过等未来结果预填进接口。

## 11. 交付与验证边界

新增运行源的全文 new-file diff 相对 `/dev/null`，所有原 callee 保原字节。源/接口/manifest 只经文本阅读、真实接口字段对照和 byte hash/diff；没有项目 AST/import/compile、科学调用、合成 fixture 或额外审查 gate。

后续若科学返回：首次 construction/material 冻结、准确目标与当前数值影子、全 R416/R417 场、R426 查询精化、R435 全 pair universe、R425 全像 held/含反射责任，各按其原实际结果解释。尤其同十词与同 W/H/marker 仍不自动执行 R443 的共同材料映射，也不自动证明连续 C² 收敛、完整等距、embedding、reach 或总目标。
