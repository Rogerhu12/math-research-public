# R532：同次 owner128 的一次投影绑定与原 DN 完整 64 位 stage 模型库

**可信度：已证明，限下述来源与完整返回条件下的有限程序组成命题；两份源码未执行。**

本项给出两份可由 Actions 中真实调用者使用的库。第一份绑定同次真实 current-H persistent128 owner 的完整末状态、原容差结果与独立 fresh replay，再调用已刊 R493 整数投影库，将全部 577×224 个 binary128 字词一次舍入为 binary64。第二份保留同一 Node 进程中已经加载的原 DN 对象，对其全部 576 个真实 cell 调用原 flowStateWithJacobian，输出完整 226×224 端口前矩阵、224×224 端口后矩阵和 2×224 两 mean 行。

这些矩阵被明确标记为“current-owner-once-projected64-full-stage-linear-model”。它们不是 owner 的 binary128 导数，不是 IEEE 舍入映射的导数，也不构成新的 BVP 接受记录。原 128 位状态、非线性值、容差、独立 replay、最终重新 anchor、BC/RMS 和 fresh audit 继续承担原责任。

R532 没有修改任何已刊 owner、worker、数学引擎、组件或工作流。当前没有新 request、实际父、实际投影、实际 J、耗时或性能结论。原 owner 尚未达到容差或 replay 未完成时，本库不具备完整输入；不能由后续 stage 模型的设计推断它解决了先行 owner 的成本问题。

## 532.1 与已付理论的关系

全局有限接受理论由 [R529-current-owner128-complete64-model-and-original-nonlinear-gates.md](R529-current-owner128-complete64-model-and-original-nonlinear-gates.md) 给出，正式源 a7b6897e816df88b7c50ddde626cdcdc20ecd667，正文 28476 B，SHA256 f930f37ae850185c524bc155f100157d5cd49d6c89c154fb2d1996ce3dc5ca44。

R532 只实现其中两个确定的前置操作：

1. 从真实同次 owner 输出建立完整的、不可由旧历史状态替代的投影点；
2. 在真实已加载原 DN 上形成所有原 stage 的完整有限线性模型，并保留原 wrapper 原先丢弃的两 mean 行。

它不重复 R529 的接受理论，也不新增 rank、残差、域或 J 精度门。完整数组、真实来源、同一次 H、原 clock 与文件完整性是本次调用合同，不是对原 BVP 新设科学门。

## 532.2 两份最终源码

两文件均在 topics/visible-flex-larger-amplitude/computations/，互不覆盖已有 basename。

| 文件 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| geometry_20261116_live128_projected_stage_binding.py | 25000 | fab3790936e6516bd39f445a2fc8384196cb1479405a10588f9007d821751cbf | fcbdba8ae1161e3ee7f9484ff73861f55d8ccdcd |
| geometry_20261116_live128_same_dn_projected_stages.mjs | 32316 | 2279a605df5ee41c5400c658018722fd52e6add40ee35ff38dbca1a31b2bb76a | 83bbfab47d7a961e3fc5610c0ff0b8df4f3a6c67 |

Python 结果 schema：

`R532-current-H-owner128-once-projected-stage-binding-v1`

Python 输入 schema 为该字面加 `-input-v1`。

JS 模型结果 schema：

`R532-current-owner-projected64-complete-stage-model-v1`

JS delivery 为该字面加 `-delivery-v1`，库描述为加 `-library-v1`。这些新标签明确区别旧 native 或 final-component 标签。

## 532.3 直接复用的原数学来源

没有复制下面各数学函数。源码直接保存其真实身份，再使用已由原 worker 安装在 dn 上的函数。

| 原文件与作用 | bytes | SHA256 |
|---|---:|---|
| computations/exact_20261116_binary128_live_response_projection.py：完整整数 RN128→RN64 | 19902 | b2336bcf56ba294efd1ba19e02b5d9acaedebb6eb669489fa1d869be7259626e |
| computations/tail_resumable_engine.mjs：原 stored/shared DN 来源 | 4193 | 1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8 |
| 原 visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs：cellFlow/evaluate 的节点、端口、mean 与残差次序 | 17250 | ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3 |
| 同 scripts/78718-tail-fourier-product-flow.mjs：原完整状态 RK 与全列变分 | 2400 | 717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f |
| 同 scripts/78718-tail-fourier-root-split-engine.mjs：原 root/split/product 与 cusp 安装 | 2045 | a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372 |
| 同 scripts/78718-prefix-tail-tangent-fourier-worker.mjs：原 DN、引擎与 profile 的实际安装 | 12294 | 36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a |

其中 b233 投影库本身的原说明针对旧 optional predictor；R532 使用它已有的完整数组投影 API，明确写入新的调用者、用途、数组形状和结果 schema，没有改动该库或声称这是旧 predictor 的实际输出。

owner C++ 实现身份仍固定为：

`7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd`。

新 Python/JS 两库均要求 GITHUB_ACTIONS=true 且实际 repository 为 Rogerhu12/math-research-public。没有本地科学执行、import、AST、编译、fixture 或数值试跑。

## 532.4 显式当前来源元组，不硬钉旧同步 post

已有 R493 同次调用者是在 owner 后同步执行原组件。未来 caller 要让 owner 加 fresh replay 先返回，必须有真正独立的来源与控制流，不能把新执行重标为旧 owner。

为允许这种准确注册，Python 输入包含必需字段 `current_source_tuple`；JS factory 接受同一个对象，参数名 `currentSourceTuple`。完整结构为：

```json
{
  "schema": "R532-declared-current128-source-tuple-v1",
  "sources": {
    "owner": {"file": "实际同目录basename", "bytes": 0, "sha256": "实际完整SHA"},
    "client": {"file": "实际同目录basename", "bytes": 0, "sha256": "实际完整SHA"},
    "current_call": {"file": "实际同目录basename", "bytes": 0, "sha256": "实际完整SHA"},
    "worker": {"file": "实际同目录basename", "bytes": 0, "sha256": "实际完整SHA"}
  },
  "schemas": {
    "owner_input": "实际owner输入schema",
    "owner_summary": "实际owner完整summary schema",
    "session": "实际session schema",
    "geometry": "实际已加载geometry记录schema",
    "snapshot": "实际snapshot结果schema",
    "snapshot_context": "实际完整context schema",
    "snapshot_manifest": "实际完整数组manifest schema"
  }
}
```

此块只是字段形状说明；其中 0 和中文说明不是可执行配方、未来字节或被接受的 SHA。真正输入必须提供已存在文件的完整 bytes/SHA 和真实 schema，且每个 source 为本库 HERE 中普通文件 basename。两库实际读全文件核 identity；当前 session.frozen_sources 必须包含这四个真实 source，并含 unchanged b233 投影库。JS 同时保留 unchanged 1a39 与原 core/flow/worker 的实际来源绑定。

现有 R493 的准确四来源示例为：

| role | 既有 basename | bytes | SHA256 |
|---|---|---:|---|
| owner | geometry_20261116_live128_same_call_owner.py | 18850 | 5c1d4908fe6cca3917ef8ad6ed6269251e29b99efbb81e54b91b4f43391fc3b5 |
| client | geometry_20261116_live128_tail_client.py | 30316 | 9f32e5ddd376016e51f678d9f0328727e63d8aacb5c4583046dc705949cc1894 |
| current_call | geometry_20261116_live128_current_call.mjs | 34356 | c20af799243d35a045c9c5be7900fbd19bb8b391acb9efb26fe9c5265566cd21 |
| worker | geometry_20261116_live128_worker.mjs | 8167 | 8cc51b3e1a1c232c8b5769ef1cfc39261deb7aba84d0b8365b62cbf88c270b72 |

其七个真实 schema 按上述字段顺序分别为：

- R493-current-H-live128-owner-call-v1-input-v1；
- native-persistent128-chord-launch-summary-v1；
- R493-current-H-live128-tail-client-spec-v1；
- R493-current-H-live128-source-and-initial-guess-v1；
- original-r273-current-native576-withJ-snapshot-result-v1；
- original-r273-current-native576-withJ-snapshot-context-v1；
- original-r273-current-native576-withJ-snapshot-arrays-v1。

这些值只说明已存在的原合同。新 caller 必须登记实际新 tuple；库不预填未来 R534 来源，不能仅凭旧名字宣称旧来源，实际 bytes/SHA 均须与当前已登记的完整文件一致。

**字节 identity 本身不证明任意新 producer 保持数学语义。** 两库结果明确记录 caller_registration_semantics_not_proved_by_hashes_alone。新来源必须由真实调用者的完整源组成论证连接到原 owner、相同 packet、相同 fresh replay 和原 DN；本库的输入合同不替代这项责任。

## 532.5 Python 输入与真实 owner 绑定

公开 API：

```python
result, result_receipt = bind_and_project(spec, input_receipt=actual_input_receipt)
```

spec 必需字段：

| 字段 | 真实内容 |
|---|---|
| schema | R532 固定输入 schema |
| current_source_tuple | 上节完整当前来源注册 |
| owner_input | 当前 call 内实际 owner 输入文件的绝对 file/bytes/SHA |
| owner_summary | 该 owner 输出目录中的真实完整 summary 文件 |
| session_spec | 当前仍存活原 worker 的真实 session specification 文件 |
| out | 当前 call 目录内、尚不存在的 R532 输出目录 |

`input_receipt` 也必须指向实际 RUNNER_TEMP 下文件；读出的完整 JSON 必须等于 spec。不存在、改变或跨 owner 的文件不会被当作可用输入。所有三类原输入都采用实际 bytes/SHA；gzip JSON 记录如果给出了 decoded bytes/SHA，也逐一核回。

完整绑定至少包括：

- 当前四个 GitHub run 键、source、attempt 与原 job clock；
- owner input 的 call_directory/out 和 session.output 的父子路径；
- call_number 与 actual_call_identity.native_call；
- 原完整 packet 与 packet binding，原 binding schema 及其实际 packet bytes/SHA；
- client/current_call 的真实 source/hash、nonlinear_iteration=0 与 snapshot_sequence=0；
- 当前 snapshot result、context、manifest 的相同 call/source/coordinate；
- 实际 current-H 的完整 112 个 binary64 words，与 packet/current request/context 三处 SHA；
- 原 scales[577]、cut-target[112]、far-graph[112] 的完整原数组；
- session 原数值配置、原 mesh/rawNode、graphs/gains/far hashes 与全部 576 个 cell/profile 元数据；
- 真实加载时写出的 actual-live-geometry-and-initial-guess.json。

采用的是完整 physical-height 数组 hash，不以其范数、几个分量、历史固定 H 或字符串名字代替当前 H。

### 原 owner 的必要状态

原 summary 必须实际给出：

1. owner_final.final.complete=true；
2. owner_final.final.below_original_tolerance=true；
3. independent_fresh_replay_complete=true；
4. state_never_roundtripped_through_binary64=true；
5. 原 final_state128 文件的完整真实身份。

fresh replay 的真实 argv 必须指向同一 packet 和该 final-state.f128；原 replay 记录中 evaluation.complete 必须实际为 true。原 owner/replay 完整 residual 和 full226 stage-output raw 均须仍在同一 owner 临时目录，形状和 bytes/SHA 逐项匹配。

| 原 raw | 完整形状 |
|---|---|
| solve/final-state.f128 | 577×224 |
| solve/final-residual.f128 | 577×224 |
| solve/final-stage-full-output.f128 | 576×226 |
| fresh-replay/independent-residual.f128 | 577×224 |
| fresh-replay/independent-stage-full-output.f128 | 576×226 |

原 replay 的逐词相等布尔如实际存在，按原值保留；**它们没有在此新增为拒收门**。原 process returncode、wall_timeout 和 protocol_stdout_fully_decoded 也保原值，不用 transport70 反推原 scientific completion。

原 summary 的旧 postcomponent error 可保留为事实，但本库不要求旧 stage/boundary/endpoint/audit 已经完成。它也不要求 summary 中旧全任务 success 为 true。此区别使真正新 owner-first handoff 可以连接，不必先白跑一套将被替换的旧 stage J。

## 532.6 一次 RN64 的准确范围

唯一数值投影调用为：

```python
P.project_actual_array_file(
    state_receipt,
    label=projection_record["field"],
    shape=(577, 224),
    output=out / "owner-final-state.once-RN64.f64le",
    record=projection_record,
    check_resource=original_clock_check,
)
```

它直接读取完整 binary128 words，以 b233 的整数算法逐词舍入，保留有符号零。它不先转 Python float，不经过文本十进制近似，也不重新解释已有 binary64 影子为准确 owner。

投影记录包含 expected_words、completed_words、first_unprojected_index、输入完整身份、输出完整 bytes/SHA、实际溢出或非有限位置。失败时保留原 partial 输出及其真实长度，不补词，不以部分数组构造完整模型。

投影成功文件是 577×224、little-endian、row-major 的 binary64 数据。JS 库只读取该文件，没有再次运行投影。Python 完成前、JS 完成前分别核原 authoritative128 state 的完整 identity 仍未改变。

该投影只定义线性模型的评价点
$$
\widehat x=\operatorname{RN}_{64}(x_{128}).
$$
它不把 $\widehat x$ 宣布为原非线性方程的解，也不给 $x_{128}$ 的微分误差界。

## 532.7 JS 最小库 API 与同一实际 DN

公开 API：

```javascript
const library = createLive128ProjectedStageLibrary(dn, {
  sessionSpecification,
  originalDeadline,
  currentSourceTuple,
  checkResource
});
const description = library.describe();
const {result, delivery} = await library.produce({
  bindingResult,
  out
});
```

dn 必须是当前原 Node worker 中真正已经加载和安装引擎的对象。它不是从序列化数据重新建立的替身。library 本身不构造 dn、不安装 backend、不调用 profile factory、不重取 cut radius，也不以新 graph/scales 覆盖原值。

factory 保存 dn、tail、cells、graphs、gains、rawNode、parameters、各原函数及每 cell 的 engine、flow 函数、profile 数组和各 profile 函数的真实引用。每次 produce 检查它们仍为相同对象；开始及结束核完整 liveIdentity 与真实 session geometry 记录一致。节点、全部 stage 地址、profile integrationBreakpoints、实际 portRatio、mu、graphs/gains 原字、原函数文本 hash 仍绑定。

这种同进程引用检查的入口仍须由真实 caller 连接。仅构造一个字段相似的新对象不能代替“原已加载 dn”这一前提；当前没有在旧 worker 中偷偷安装该库。

### 原操作次序

对每个 $n=0,\ldots,575$，原 ac2f cellFlow 使用的是右侧节点 $\widehat x_{n+1}$。本库原样形成：

```javascript
const initial = new Float64Array(226);
initial.set(states[n + 1]);
const f = c.engine.flowStateWithJacobian(
  initial,
  c.profiles,
  {stepsPerSegment: dn.tail.parameters.steps}
);
```

两 mean 初值由原 Float64Array 分配产生正零，不增加 mean 输入列。调用的 actual profiles、integrationBreakpoints、cusp-aware engine、steps 和原函数都来自同一 cell。库不执行另一套 RK、root、flux、Fourier 或 Jacobian 内核。

flow 返回的完整226状态和226×224 tangent先原样保留。若实际有 shapeDimension 字段，则必须是224；完整维数首先以真实返回数组长度与已绑定原引擎合同核定。任何非有限词保留其 actual number record 与位置；已有 raw 不删，不把该 stage 记为完整有效模型。

## 532.8 端口与两 mean 的完整局部模型

记原引擎返回矩阵
$$
A_n\in\mathbb R^{226\times224},
$$
其列顺序是该 stage 原输入的112个 $Q$ 槽与112个 $\Pi$ 槽。原 wrapper 对 shape 的端口操作为
$$
P_n=\operatorname{diag}(I_{112},p_n^{-1}I_{112}),
\qquad p_n=\text{actual portRatio}.
$$
输出的形状模型为
$$
B_n=P_n\,A_n[0:224,:],
$$
完整两 mean 行为
$$
C_n=A_n[224:226,:].
$$

实现按原 cellFlow 的逐项运算次序：
`f.tangent[i*K+j] / (i<M ? 1 : c.portRatio)`。
前112行也执行原来的除1操作；不会通过不同代数整理冒原运算字词。两 mean 行直接保留，不除 portRatio，不求和后丢掉其中一行。

端口后 primal 的前112分量原样取值，后112分量按原式除 portRatio。原 normalized shooting residual 的 stage 项按
$$
\widehat f_n-\widehat x_n
$$
形成，并使用原捕获 scales。cut 和 far 残差使用原捕获 target、far graph；它们只作为投影点诊断，不能覆盖 owner128 的值。

原局部 mean 的数值和按 $f_{224}+f_{225}$ 形成，全局 meanHeight 按原 stage 顺序累加。库保留每条 mean 的值与完整梯度行；它没有用末 shape、端点图或省略行推造它们。

原717a变分程序初始化全部224个 shape basis，推进226输出行。R532 调用它一次返回全列；不做方向抽样，不补零列，不作有限差分，不按当前误差挑列。

## 532.9 完整输出和必要输出的区别

JS fresh out 内六个连续原始文件按 stage 顺序排列：

| 文件 | 请求完整形状 | 含义 |
|---|---|---|
| before-port-jacobians.f64le | 576×226×224 | 原引擎完整 tangent |
| after-port-jacobians.f64le | 576×224×224 | 原端口规则后的全 shape J |
| mean-jacobians.f64le | 576×2×224 | 两条原 mean 行，各224列 |
| before-port-primal.f64le | 576×226 | 投影点原完整返回状态 |
| after-port-primal.f64le | 576×224 | 原端口 shape 输出 |
| shooting-residuals.f64le | 576×224 | 原顺序的投影点 stage residual |

另有 projected-point-end-residual.f64le、projected-point-cut-residual.f64le，以及 all-stage-return-records.jsonl。每条 stage ledger 记录真实 stage/rawCell/rawSegment、原 profile/flow 文本身份、实际投影输入节点与该行 words SHA、端口字词、原 steps、每条完整输出行的 bytes/SHA 及原诊断值。

这六个请求完整数组共有469656576 B；此数仅由声明维数和每字8B计算，不是实际资源承诺。全部 raw 留在 Actions 同一 call 内，未上传 Git/artifact。大 ledger 的成功正文不放进必要摘要；必要正文保留它的完整身份、实际完整行数、所有原错误、当前部分 stage 和全部未访地址。

每个 array receipt 保留 requested_shape、complete_rows、trailing_bytes、实际 file/bytes/SHA、dtype 和 order。只有六件均完整576行、没有尾部残字、全部阶段及最终来源检查完成，full_stage_shapes_complete 才为 true。不存在“只有shape成功，所以两mean也已付”的推断。

Python 的 complete 只表示其绑定与一次投影完成。JS 的 complete 只表示该完整有限线性模型已形成。两者都不令 native_accepted、fullDN、边界、端点或原非线性门自动成功。

## 532.10 绝对时钟和进程边界

原 clock schema 固定为 R493-original-full112-live128-job-deadline-v1，total_seconds=19200，原 readback_cleanup_reserve_seconds 必须保持实际文件中60至600的整数。科学截止仍是原 absolute_monotonic_deadline_ns 减原 reserve，不重新起算。

Python 直接读该实际文件，在原 time.monotonic_ns 坐标内检查；b233 每个实际投影 block 调用此检查。它没有为投影另发新的完整相对预算。

JS 也绑定同一实际 clock file bytes/SHA 和四 run 键。为避免把 JSON 的大整数舍入，准确 deadline 字词以 BigInt 读取，并与 Python 输出的 scientific_deadline_monotonic_ns_text 相同。JS 不擅自把另一进程计时起点视为相同绝对坐标。

checkResource 是**必需的原调用者回调**。它收到同一实际 deadline receipt、准确科学截止字词与真实 stage/completed_stages，必须在原 clock 下检查并在耗尽时抛错；可同步或异步。本库在完整 cell 之前及 cell 边界调用它。

单次 synchronous flowStateWithJacobian 不能由这个库从内部硬中断。因此真正外层 owned caller 仍须对原 worker 进程执行原绝对截止、TERM/KILL、等待和 quiet 责任。这个 caller 当前尚未注册。库没有宣称已经完成 hard-timeout、owner-reap 或 cleanup。

若回调抛错，结果保留真实 type/message/stack/phase；resource_partial_scope 明示这是“必需原 clock callback 未返回”，不把任意异常自行诊断成已观测 timeout。原 phase 地址和完整未访后缀仍在。

## 532.11 中断、错误和90KB

Python 成功或已创建 out 后的可记录失败写 result.json。b233 的 partial index、真实部分输出、原 raw、错误位置和 traceback 保留。开始阶段若真实输入/schema/路径尚不能建立，库直接抛错；未来 caller 必须保留该实际异常，不得伪造一个 complete result。

Python CLI：

```bash
python -u "$COMP/geometry_20261116_live128_projected_stage_binding.py" \
  --input "$ACTUAL_INPUT" --input-sha256 "$ACTUAL_INPUT_SHA"
```

它输出真实 result identity 和下面这一份必要正文：

`BEGIN_R532_CURRENT_OWNER_PROJECTED_STATE_NECESSARY`  
`END_R532_CURRENT_OWNER_PROJECTED_STATE_NECESSARY`

正文≤90000B时，complete 返回0，partial返回2。超过90000B返回70，保留原结果与实际 attempted bytes/SHA，不分包、不编码、大体不搬运，不授权 cleanup。

JS 逐 stage 先写实际返回数组和完整 ledger，随后才推进 completed_stages。若某个数组已写而另一个失败，实际各文件的行数和尾字分别保留，当前 stage 仍在未付后缀。pending 从绑定时的完整原 stage 地址表取得，不用失败后可能已改变的对象猜地址。

JS produce 不向原 worker stdout 写科学 frame，避免破坏原逐请求协议。它写 result.json、若≤90KB则写 necessary-summary.json，并写 delivery.json，返回 `{result,delivery}`：

- delivery.result 是完整结果文件 receipt；
- delivery.necessary_summary 是真实必要文件 receipt，或超限时为 null；
- necessary_exit_code 是0、2或70；
- attempted_necessary_bytes/SHA 始终对应实际完整拟返回正文；
- all_raw_retained=true；
- cleanup_authorized=false；
- current_worker_stdout_protocol_untouched=true。

必要摘要即该完整结果对象，不另暗减失败信息。其成功大型数组/ledger只返回完整身份；未返回它们的科学正文不能在后续结论中冒“全文已读”。

资源失败、原 source 改变、文件短写、非有限模型或未观察 quiet 都不能被写成 BVP 不可解。若连结果文件也不能落盘，实际 caller 的 stderr/进程记录仍是必要失败来源；库不伪造落盘回执。

## 532.12 与 R534 等后续调用者的准确交接

当前可由同一真实作业接入的顺序为：

1. 原 owner 在真实当前 packet/H 上执行，得到完整 final128 和原 fresh replay；
2. 新实际 owner handoff 返回后，保留原所有 raw，并以真实 source/schema 登记来源；
3. 对该同次结果调用 Python binder，一次形成全577×224投影；
4. 回到同一原 Node dn 对象，调用 JS library，形成576个完整 stage 模型；
5. 后续显式新 consumer 将所有 J64 和两 mean 行准确 lift 到 binary128，再执行原完整 boundary、endpoint、重新 anchor 和 fresh audit；
6. 只有原完整非线性门真实通过，调用者才返回原意义的成功响应。

R532 只完成2至4之间的两库 API，未注册整个顺序。它不会在旧同步 owner 已经白跑 post 后谎称节省了那段工作。

有限 binary64 字词可在 binary128 中准确表示；但“能准确 lift”与“真实 consumer 已 lift 全部列并调用原门”不同。当前没有写该 lift/组件 consumer、没有改旧 native summary flags，也没有提前声称全链可运行。

特别需要保留的两个原接口边界：

- 原 c218 boundary 的数值主体可以接受完整模型后相应处理，但其头部禁止 fixed64 且原 summary 写 R273_or_fixed64_used=false。新 caller 必须采用真实独立来源和 current-owner-projected64-model 标签，不能沿用这个不实旧 flag。
- 原 a090 endpoint 入口先读完整 G 再进入 base。即使 cut338/13scalar 的 base 数学函数不依赖 G，也不能把现入口当成已接 noJ 接口。全部338行原顺序是 slope[112]、second[112]、meanSlopeCorrection、meanSecondCorrection、height[112]；原 AffineTail 使用首112行。

本库保存完整两 mean 行正是为这些真实后继提供输入；不能用“保了 shape J”跳过其责任。

## 532.13 条件组成命题及证明

**命题。** 假设：

- 当前显式来源元组确由已登记原 owner/worker 组成，原数学源为532.3的实际原文件；
- 实际 owner 在同一 packet、H、C/有限配置上给出 complete、原 tolerance 和独立 fresh replay；
- 真实全状态、snapshot/context/四数组、同一已加载 dn、原 clock 与所有来源绑定如上成立；
- 投影和全部576个原 flow 调用及其完整数组写入都成功完成，未超过真实 caller 允许的原资源边界。

则 R532 的完整结果为同一个 $x_{128}$ 的一次投影点 $\widehat x$ 上，原有限 stage 变分程序的所有226×224输出，及原端口规则的全部224×224形状模型和两mean模型。它没有改变 authoritative128 的状态字词、原目标、H、profile、mesh、M、N、cusp/steps、原非线性门。

**证明。** Python 对全输入文件和 run/call/H 链逐项绑定，b233 按原文件顺序恰处理577×224个binary128 words。完整结束要求所有词存在且原输入 hash 再核相同，因此输出正是指定全状态的一次声明舍入，非历史状态或缺行补齐。

JS 将每条输入节点原字读取为 Float64Array。对于第$n$个原 cell，源码调用与 ac2f withJac 分支的局部状态、两零mean、原profiles和steps完全一致，直接执行同一个已加载 flow 函数。没有省略或替换局部运算。完整数组长度与全部行写入条件保证原返回的所有输出和列均在。532.8的端口公式由原 cellFlow 的同一逐项表达式实施；两mean行是原 tangent 的最后两行，不依赖任何补全假设。所有 stage 顺序与原 rawCell/rawSegment、source函数和端口 identity 保留。

stage完整计数只在所有实际文件与ledger写入后推进；所有中断仍保未付当前项和完整后缀。因而只在全部576项及末来源检查完成时才有完整模型。投影前后核原128文件身份，库也不写原 source、DN geometry 或 owner文件。以上给出声明的有限程序组成，不给精确连续解、收敛、128导数相等或实际 BVP 接受。证毕。

## 532.14 尚未履行的责任

本项没有：

- 原新 owner-first 实际 source/pipeline 注册；
- synchronous cell 的实际 owned watchdog 接线；
- 完整 J64/mean64 的真实 binary128 lift consumer；
- truthful 新 boundary/endpoint/audit/assembly 来源闭包；
- 任一真实 H 上运行、性能、误差、rank或收益结论；
- 原 owner 未完成时绕过其容差与 fresh replay；
- 单90KB必要 reader 的外层清理 marker或新工作流；
- 对 current-C/十参数/closed-field 问题新增任何已接受结果。

R529 的原有限接受责任保持不变。R532 的两库可以为真实下一调用者提供完整输入与输出合同；这些未付项由实际来源和运行继续履行，不能因库文件已登记而填成已完成。
