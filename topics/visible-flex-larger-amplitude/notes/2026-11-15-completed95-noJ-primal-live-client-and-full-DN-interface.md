# 真正完成的 95 尾结果：独立 noJ-primal live client 与 full-DN 衔接

类型：独立源码实现与条件接口；没有新科学运行或接受结论。

作者：`amplitude`。日期：2026-11-15 UTC。

## 1. 当前完成范围与使用前提

本批亲读了原 noJ-primal live 五源及[总接口](2026-11-15-noJ-primal-live-client-and-full-DN-interface.md)、[逐请求适配器与 QR 接口](2026-11-15-noJ-primal-live-current576-adapter-and-QR-interface.md)。原 client 并非通用成功锚读取器：它硬锁第 73 轮 result schema、`938f…` producer、`0997…` hook、`completed-native73-…` 锚/种子身份，以及第七件 `original-live-identity-before-failed61-seed.json`。原 hook 和 system 也核这些身份，QR 硬锁 system，full-DN 硬锁四配套源。因此只改输入路径不能合法消费未来的第 95 轮结果。

本批新建五个独立来源适配文件，完整保留原 client 生命周期、原逐请求 native loop、原 R273、原实际 H/J 绑定、原边界 FD 以及原 full-DN 入口。旧五源与第 95 轮七源均未修改。本次没有创建 workflow/request，没有派发、下载、实例化 native client、构造成功锚或运行科学函数。

**第 95 轮尚未被本接口认作成功。** 只有将来提供其真实 `result.json`、完整实际 SHA256 和同目录八件原始证据，且原结果的 native 成功、完整 J 与 audit 责任全部通过，才可使用本入口。失败的 73、83 试步、91 固定矩阵报告、95 单个 candidate/QR 文件或待生成结果都不能替代这个输入。

实际前缀 warm 是另一个独立输入。即使未来 95 native 成功，前缀仍须从真实 warm/status pair 进入实际 H/J、FD、完整 BVP 和最终 fresh audit；它不自动成为已接受前缀或闭面。

## 2. 五个独立来源与冻结哈希

| 新文件 | 字节 | SHA256 |
|---|---:|---|
| `geometry_20261115_completed95_noj_primal_live_tail_client.py` | 35,376 | `867bbd75e6f5a9859bc3bfb48cff40f12916b4a470a97b051c99cacbd38c4038` |
| `geometry_20261115_completed95_noj_primal_live_tail_client_hook.mjs` | 51,410 | `583514abde5ce47b56be3b628fec66907f86ccc34c51266fb1e9011370c7278c` |
| `exact_20261115_completed95_noj_primal_live_current576_damped_system.py` | 33,578 | `e621f9aefc29c030dbcbd4e70d2ce19198d58cc740c9091145c11c3f595a114c` |
| `exact_20261115_completed95_noj_primal_live_current576_damped_chain_qr.py` | 22,434 | `94e5691a59936a7f3fdbc60fec69bcf0b6791c0688e717fd3424629a390ae31e` |
| `geometry_20261115_completed95_noj_primal_live_full_dn.py` | 32,654 | `814e2ca1d8da16fb5f47c45dc6600b16fb34988ad8a1e6132da3ad149e969a2c` |

完整基线是以下已付五源，分别由新文件的完整 `.diff` 保留全部变化：

| 原文件角色 | 原 SHA256 |
|---|---|
| client | `7aa2aba10e44f0a0fd0e6eee47e9239a2f2244bb9663b8ec5ede294edc71bb64` |
| hook | `0e802785329c73d5a951ca69942414ca5dcc40a9284dae9d31c4ca6cb819daa1` |
| system | `e30e53e635f84ae4762ef045e6510c20d63524efd604ba617cec3a849bdfb3d3` |
| QR | `c3284d556e76f389d084bc612579c485697f15aeb4c5b7a5caa49567a9920909` |
| full-DN | `bb8ad207c5b85fb10e0a5ee83b36eed4317c757646055eaec58b2bc3c8945c14` |

五个新 basename、环境变量 namespace、runtime Symbol 和自产 schema 都明确属于本次 `completed95` 接口。adapter 依旧把 snapshot 里的 launcher/hook SHA 与运行目录中这两个固定新 basename 的实际字节比较，避免双向 SHA 循环；client 和 driver 继续硬锁其子源。

## 3. 原 95 成功结果与八件证据

### 3.1 顶层真实结果

`--anchor-result` 指向未来实际 `native-word-first-current576/result.json`，`--anchor-result-sha256` 必须为那份真实文件的完整 SHA256。本批没有给出未来结果 SHA、run、artifact 或成功状态。

读取器要求原 result schema 为 `native-word-first-current576-damped-solve-result-v1`，并核：`success/native_accepted/original_complete_client_response_returned/actual_original_converged_flag=true`，`actual_worker_exit_code=0`，`original_native_requests=1`，请求的完整 DN Jacobian 与 finite audit 均为真，且没有 `actual_error` 或原失败消息。仍要求真正的原 response `converged=true`、无 failed、完整有限 J 和原 audit。

硬锁的父来源为：

| 父 95 原源码 | SHA256 |
|---|---|
| `geometry_20261115_native_word_first_current576_solve.py` | `69c9a8d5cccfcfdcdda35c475b089609c789747803a7b363a17fb67c5bae28d0` |
| `geometry_20261115_native_word_first_current576_solve_hook.mjs` | `932961ef9f267f95f5de6bb28791ed43ef2c66d15b18b55823bc3f2384545bc3` |
| `exact_20261115_native_word_first_current576_system.py` | `2c6c012d9f2306f2ac13d240510eb8086b74d2b60ff318aa9e359dd72c05a3a8` |
| `exact_20261115_native_word_first_current576_chain_qr.py` | `4c887fbb4a16e0d2219969043e708c2d49c446f0ac75ba1dc3e6e17f7d2ee314` |
| `exact_20261115_native_word_first_candidate.py` | `d9692107d197dcb4478fc2027beec21e3e611e67109af9d4b13ae09fb506e226` |
| `exact_20261115_native_word_first_parent.py` | `8cd7027df2f7039302dbdc1ed15068c6cf48d6645bc236d74e6e5b1e7dd387e8` |

95 的 transport helper 属于原件取得来源；它不进入本 live 数学 source 闭包。本接口不再取 91 大包，也不重载 95 的旧 J、因子或方向。上述六个 producer 身份由 result/spec 自身字段闭合；新运行还核自己的完整源闭包。它们不是对缺失父大数组作独立字节审计的声明。

### 3.2 同目录八件原件

每件都先从真实 result 的 `small_output_files` 唯一清单取得文件名、bytes、SHA256，再核本地普通文件、安全相对路径及完整原始字节。清单不能凭手工复制新造：

| 原件 | 实际读取和身份责任 |
|---|---|
| `current-solve-spec.json.gz` | 与顶层 `specification`、`spec_sha256` 逐项一致；schema 必须为 `native-word-first-current576-damped-solve-spec-v1`；核真实 producer/hook、原完整 loop/十试步/final J/audit、95 bridge/first-word 源身份 |
| `current-input-config.json` | 保留原字节；仅按已有 `numerical_configuration` 规则剔除 IO 字段后与真实 response/spec/新 client 数学配置比较 |
| `native_0001.json.gz` | 必须是顶层 `original_response` 的同一文件；取其原 request、response、完整 H、J、checkpoint 和原源图 |
| `native_intent.json` | 与 response/spec 的原数学 source map 一致；不能将新 ready 当响应或 Jacobian |
| `native_ready.json.gz` | 只保留原构造 ready 身份，新 client 自己运行构造并按原 ready semantics 比较 |
| `native_capacity.json` | 原 capacity 原件；新构造的指定 capacity/adapter/版本/文件字段继续与它比较 |
| `original-live-identity-before-failed73-seed.json` | 这是 95 实际导出的正确第七件；记录其原 parameters/rawNode/graphs/gains/far/公开方法来源。它不是随后 live 的种子状态 |
| `primal-flow-installation.json` | 原 schema 仍为 `noj-primal-current576-live-flow-installation-v1`；核 95 producer/hook/spec、576 stages、原 noJ 函数引用保留、新 flow 没有复用 saved J 或执行安装期 RHS/ODE |

父配置为 M112、spacing2；J 仍需 `(3*112+2)*112=37856` 个完整有限条目。原 response 残差必须通过自身原 `solveTolerance`；顶层 residual/audit、spec/result 的原 tolerance/maxIterations 还与同一 response/config 逐值对应。这些是同一原返回的来源一致性，不另加数值容差。

95 的 `parent_failed73` 与 `parent_binding` 在 result/spec 两处必须一致，且历史 `native_accepted=false` 原样保留。本入口不读取那条历史链的状态作为 live 种子，也不要求 95 首词候选曾被选择：若 95 通过完整 R273 后成功，真正的最终 response 才决定其可用性。

## 4. 成功锚、字面种子与新 bootstrap

通过上述原件绑定后，新 client 才在新输出目录生成：

- `completed-native95-word-first-noj-primal-literal-JSON-anchor-v1`；
- `completed-native95-word-first-noj-primal-literal-JSON-seed-v1`；
- `anchor-literal-checkpoint.json.gz` 与 `large-arrays/anchor-literal-state.f64le`。

唯一状态来源是**完成的 95 原响应 `response.checkpoint.states`**，完整 577×224，九个原物理边界 `rawNode=[0,72,144,216,288,360,432,504,576]` 不变。literal seed 保存原 JSON 解码后的 binary64 字、实际可见负零 sidecar，以及整 raw SHA；不声称恢复 JSON 序列化前未导出的符号零。父的 cutHeight 必须与其原完整 request H 一致。

新 parent 还保八件 `original_parent_evidence`、六个 `completed_parent_source_sha256` 和历史 `parent_failed73_provenance`；显式记录：

```
completed_parent_result_schema = native-word-first-current576-damped-solve-result-v1
parent_failed73_state_used_as_live_seed = false
parent_first_word_algorithm_repeated_in_live_worker = false
```

新 bootstrap 必须是新 worker 的实际 call1、完整父 H、`jacobian=true/audit=false`。没有导入旧 response cache、last 或 tangent predictor；原 worker 通过自己的真实调用建立它们。只有 call1 的 initial 设置为 literal seed。后续请求使用自己的 H/target/σ 和原 predictor/fallback，不能重置为父 H 或父状态。

**95 的首词候选不被复制到 live 算法。** 本 live hook 每次 correction 都仍走原完整 R273 子求解；它仅把实际成功95的终态作为新 bootstrap 的初猜。首步原 solver 若已收敛，也仍由其原收敛逻辑决定，而非本接口伪造返回。

## 5. 逐请求 fresh-J 与原 native 责任

新 hook 完整保留原 `beginNativeRequest/captureCurrent/checkedCurrentDirection/currentCorrection` 结构，只将自产 schema、Symbol 和 reciprocal basename 改为独立 `completed95` 身份。当前 J 仍由当前原 with-J evaluate 真正返回；完整 base/r/out/cut/far/σ/H/target 和全部 576×224×224 J 进入对应 call/iteration 的 snapshot。

noJ-primal flow 仍是 `geometry_20261114_noj_matched_variational_engine.mjs`，SHA `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9`；原 product-J `205b28…` 和 cusp splitter `b12f36…` 身份不变。其 226 维 primal、224 维 shape 和 captured-root feed 责任不变。原 evaluate 正文和十次 noJ trial 正文逐字保留；原 with-J 实现被独立识别，不能误写“全部 flow 未改”。

R273 使用原因子 `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` 与完整 exact-row kernel `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f`。原所有 cut/576stage/far 行、577个 η 罚块、全部纯常数、回代和 129248 个原行精确读回保留。每个 child 的 `native_accepted=false` 仍不能替代原 native 真接受。

本批不改 η 默认值1、原 config 的 maxIterations32、十档试步、tol2e−9、原 domain guards、原 ∞ norm、原 endpoint J 与 audit。模型 L2/梯度/精确线性缺陷继续只作报告；minA/minD 继续按原 IEEE 元数据保存，没有添加有限阈值或新的 native 验收门。

## 6. 实际 warm H、原 FD 与 same-client full-DN

full-DN orchestration 的当前 warm/status 校验结构不变：消费实际 pair 的原字节和完整 producer 字典；`success/new_coupled_finite_acceptance=false` 诚实保留。它验证原完整 scalar/port、M112/N2048、全453坐标、真实全 mesh/RHS 及历史 accepted96/config/zero-H 来源，但不会把旧零 H affine FD 当当前真正尾解。

顺序仍为：

1. 启动唯一新 client，执行上述真实 bootstrap；
2. 从实际 warm/原边界算完整当前 H，向**同一** worker 求真正 H/J；原相等 H unaudited cache 只可在该新进程自身已经完成的请求间生效；
3. 原 `actual_response_binding` 绑定真实 response file、完整 H/J 和该实例的原 cache；
4. 在这个真正当前 H/J 所定义的明确 affine 图上运行原边界 FD；
5. FD 通过才把同一 Python 实例、同一 PID、同一 last/tangent predictor 和原缓存交给原 `geometry_20261114_physical_test_full_dn.main`；
6. 原 full-DN 决定新 H 请求、inner/outer、RMS/BC 与最终 fresh audit。audit=true 必须新增真正 protocol call，不能命中旧 cache。

FD 数学没有减少为新的小检查。原 `make_directions` 保三 core 方向、四物理方向和三 control 方向，direct/augmented 各10项；原三步长、两组 fourth-order Richardson 与 `5e-5` 实现阈值不变。三处原 endpoint-height 扰动 `1e-5/1e-9/1e-10` 原样保留。FD 期间没有 native 请求，不能冒非线性尾在所有扰动点已真解。

原 RMS `1e-6`、BC `1e-11`、maxnodes1200、默认8 outer、Rφ 完整边界及真尾/最终 audit 均保留。`response_check/full_argv/actual_response_binding` 的函数正文逐字同旧 live 源。worker ownership 不变：异常/FD失败关闭唯一 client；成功由原 full-DN finally 关闭后，orchestrator 的重复 close 保持原幂等行为。观察 handoff 只记录当前 H 是否等于 FD 锚；不能把不同 H 换回旧锚。

## 7. 最小 CLI 与未来输入

未来真正完成95、已提供实际 warm/status 后，在原 public Actions 环境运行如下模板。大写参数位置只是 CLI 输入位置说明，**没有为未来结果填写任何 SHA**：

```bash
python computations/geometry_20261115_completed95_noj_primal_live_full_dn.py \
  --accepted ORIGINAL_ACCEPTED96_FILE \
  --warm ACTUAL_COMPLETE_WARM_FILE --warm-sha256 ACTUAL_WARM_SHA256 \
  --warm-status ACTUAL_COMPLETE_STATUS_FILE --warm-status-sha256 ACTUAL_STATUS_SHA256 \
  --port ORIGINAL_COMPLETE_PORT_FILE --tail-config ORIGINAL_T112_CONFIG_FILE \
  --tail-source-root ORIGINAL_PUBLIC_SOURCE_ROOT \
  --anchor-result ACTUAL_SUCCESSFUL95_RESULT_FILE \
  --anchor-result-sha256 ACTUAL_SUCCESSFUL95_RESULT_SHA256 \
  --out NEW_FULL_OUTPUT_DIRECTORY --work INDEPENDENT_PREFIX_WORK_DIRECTORY \
  --node-heap 6144 --jac-workers 2 --max-nodes 1200 \
  --material-angles 4096 --physical-angles 4096 --outer-iterations 8 \
  --native-eta 1 --native-exact-workers 2 --native-max-factor-bytes 2147483648
```

CLI 接受 SHA 的对象是实际传入文件的字节。若公开 status 为透明 gzip，传其 gzip 路径就应传 gzip 原 SHA；若工作流先恢复 decoded 原 JSON，就传 decoded 原 SHA。禁止重新序列化 status 后沿用原 hash。

独立 client 也可由原 `load_client` 加载；其环境 namespace 全部为 `VISIBLE_FLEX_COMPLETED95_NOJ_PRIMAL_…`。必需的两项是 `CURRENT576_ANCHOR_RESULT` 与 `CURRENT576_ANCHOR_RESULT_SHA256`；可选 live 算法/资源项仍是 `CURRENT576_LIVE_ETA/EXACT_WORKERS/FACTOR_BYTES/OUTPUT`。hook spec 环境名为 `VISIBLE_FLEX_COMPLETED95_NOJ_PRIMAL_LIVE_CURRENT576_SPEC`。通常由上述 driver 设置，不由外部新造 spec。

本批没有更改实际原 config SHA `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`、accepted96 SHA `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` 或历史 zero SHA `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51`。parent95 的 current-input-config 原文件仍保其自身字节身份，数学字段与这个原 config 比较，不能把两份不同序列化文件说成逐字同。

## 8. 输出身份与保全

关键自产身份如下；完整文件名和输出树沿原 live 链保留：

| 对象 | 新 schema |
|---|---|
| client spec | `completed95-noj-primal-live-current576-tail-client-spec-v1` |
| 每个 native request | `completed95-noj-primal-live-current576-native-request-context-v1` |
| snapshot result | `completed95-noj-primal-live-current-native576-withJ-snapshot-result-v1` |
| snapshot context / arrays | 上述 `…withJ-snapshot-context-v1` / `…withJ-snapshot-arrays-v1` |
| complete linear binding | `completed95-noj-primal-live-current-native576-complete-linear-system-binding-v1` |
| QR result | `complete-native-completed95-noj-primal-live-current576-damped-square-root-direction-v1` |
| full-DN orchestration | `completed95-noj-primal-live-current576-actual-H-FD-and-original-full-DN-v1` |

output 中仍保 `actual-response/{actual-anchor-tail.json.gz,response-check.json}`、`same-live-client-handoff.json`、`orchestration-status.json`、原 `full-dn/true-tail_*` 和逐 call/iteration 的完整 snapshot/QR/report/arrays。source ledger 包含新的真实 client/hook/system/QR/driver，不把它们伪标为旧 `7aa2/0e80/e30/c328/bb8a`。

父八件证据、result、literal seed 和每轮 source/context/manifest/完整数组都有独立职责；本接口不删除因子、常数或大 payload，不宣称有缺失 raw 因子的独立审计。原4.9MB单 metadata 文件约束保留；大数组按原 artifact 路径输出，没有减少原矩阵规模。

每个完整 correction 的固定二进制声明仍为704387088B。默认8 outer 的保守19 protocol calls、每个最多32 correction，总声明428267349504B，另有 variable JSON/log/前缀工作文件；这沿旧 driver 的资源公式，不是未来实际用量。单次32GiB安排不能当作整个 full-DN 的容量保证。已有 storage SDK/supervisor 源不在本批适配范围；若后续使用其 hook/source/schema 绑定，须明确绑定本批新五源，而不能仍宣称它们是旧源码。该工程接线不改原 native/FD/BVP 门。

## 9. 已付静态核的准确范围

本批仅本地执行源码/字节操作：

- 五个原 live 源与六个95数学 producer 源原 SHA 逐字匹配；未写这些原文件；
- 五份完整 source-only inverse-edit 往返恢复原源全文；
- 四份 Python AST、Node `--check`；
- 241项来源、对子源 SHA、八件文件名、schema、原模型scope、原factor/kernel和受保护函数正文合同；
- 原 core/worker 的纯字符串加载器变换往返，确认唯一 correction 调用替换、evaluate SHA `9725…` 与十 trial SHA `6039…` 正文逐字同，request context 插入可精确还原。

`source-static-check.json`、`complete-source-contract-check.json`、`pure-source-roundtrip.json` 与五个 `.diff` 保留这些范围。Node 的 source fixture 只生成/核源字符串，没有导入或执行原数学程序、bootstrap、worker、RHS/J/ODE/QR/native 或 FD。没有运行 synthetic success fixture，也没有把静态核当成第95或后续 full-DN 成功证据。

下一执行所缺的是**真实完成95的结果和实际所选 warm/status 输入及相应运行资源**，不是本批增设的数学批准条件。若95未通过，读取器应按原失败事实拒绝成为锚；本批来源适配不改变该事实。
