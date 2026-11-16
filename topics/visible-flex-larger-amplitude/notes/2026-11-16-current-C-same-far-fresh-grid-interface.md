# R450：同 job 完整 far 原件复用、fresh 网格和独立 native 来源接口

作者：geometry agent（AI），2026-11-16。

状态：源码与完整条件证明交付，未执行科学，未有新 parent、recipe、request、run、steps 或成功结果。root 唯一发布。当前三运行源不修改 R441/R448 或正在运行的203。完整理论见 [R450](../results/R450-same-family-finite-far-reuse-and-fresh-native-sampling.md)。

## 1. 本次真正实现及调用边界

新增独立 sampler 的三个子命令是 `sample`、`configure`、`readback`。第一项在公开 Actions 中调用原准确 C 区间函数；后二者只读取实际元数据/生成明确 config，不调用数学求解。另有独立 worker/client，保原 native/bridge/QR/root/RK 数学，只识别新 sampler 的真实 schema/source。

`sample` 使用同 job 中已经完整返回的原 positive965c 或 joint32b sampler。原112远端行族、全部候选和误差、原 far 点样本、原 $\mu_f$ 字及原数值边界矩阵不重算。新 `steps` 的其余实际点用原准确 C 表达式重新包围并形成新数值字。旧 node_mu、field_geometry、响应、Jacobian、状态、QR 因子和接受结论不复用；唯一旧点样本是明确冻结的 far anchor。

本次输入范围与 R441/R448 的真实 accepted450 父范围相配：其原 native geometry 已完整生成。仅有“原远端传播完成，但旧网格随后失败”的结果可能没有原 geometry/矩阵文件，本版不把这种 partial 伪造为完整旧对象。这个窄范围是实际接口范围，不把失败点认作无解，也不是对 BVP 另加数值门。

原 R441/R448 的 owner、driver 和 source maps 没有被改。它们本来硬锁旧 client/sampler来源，不能直接接受本次独立结果。root后继须明确注册下列三源、schema、配置 provenance 和原父来源，仍执行原完整450流程；本接口不以修改旧模块全局变量绕过这些绑定。

## 2. 发布文件和最终身份

<!-- FINAL_IDENTITIES -->

| 发布文件 | bytes | SHA-256 |
|---|---:|---|
| `geometry_20261116_current_C_same_far_resampling.py` | 50142 | `0cb327b6fdd5f1dbf550719fef5f1f865781a983302d3b69ae97ffa85e7ce06e` |
| `geometry_20261116_current_C_same_far_native_worker.mjs` | 18758 | `bbbca0cb031ff5f2ca33f675d2c0d3e8135866a33962649e2d551e1d683b7c03` |
| `geometry_20261116_current_C_same_far_tail_client.py` | 23228 | `4328caeb0c2dde4e0d7df70058e793a042ee8202dd47eca376d441071d6d81de` |
| `R450-same-family-finite-far-reuse-and-fresh-native-sampling.md` | 15989 | `974a5dccd2adc063e22da5d8cb997c279984200c9c1b06edf95a5ab7040a62d6` |


<!-- END_FINAL_IDENTITIES -->

临时 `publication-files.json`、源码构建脚本、完整 `.diff` 只作文本交付/审阅，不是要写入仓库的可重算结果。源码文件均小于100KB。

源职责如下：

| 文件 | 职责 |
|---|---|
| `geometry_20261116_current_C_same_far_resampling.py` | 同 job 原件绑定；原 far 家族及字保留；fresh grid；独立 config；单份必要读回 |
| `geometry_20261116_current_C_same_far_native_worker.mjs` | 真正新 worker 来源和 ready schema；原完整 native 全字段/数组/请求协议 |
| `geometry_20261116_current_C_same_far_tail_client.py` | 原四参数 TailClient API；新 worker/sampler来源；新 owner 内的原全部响应/全J/audit |

worker/client 完整差异分别见同名 `.diff`。sampler 是新文件，其完整 `/dev/null` unified diff 见 `new-sampler-complete.diff`。没有把一个几万行旧 proof kernel 的源作新标签复制；数学 helpers 在 Actions 中从各自冻结原模块加载。

## 3. Schema与原保持对象

新sampler/result：

`R450-current-C-same-complete-far-family-fresh-radial-sampling-v1`

必要summary：

`R450-same-far-fresh-grid-one-necessary-readback-v1`

新worker协议：

`R450-current-C-complete112-live-native-worker-v1`

新client自身记录：

`R450-current-C-complete112-live-tail-client-v1`

以下原结构schema仍是原定义，并由实际source map分辨实现来源：

- `current-C-complete112-client-config-v1`；
- `current-C-complete112-native-runtime-spec-v1`；
- `current-C-native-radial-geometry-bundle-v1`；
- 目标 `R286-original-stored-continuous-model-convention-C-v1`。

保持 $M=112$、间隔2、orientation=1、576 stage、全部577节点、完整112×224 far矩阵、完整native切向112 RHS与双mean。新 `steps` 只改变原stage内实际字集合；native角数只由后继config明确传入。当前没有 M 参数，不支持把112行改标签为更大系统。

## 4. 明确输入与同原钟

`sample` 的实际输入必须都是本 job 可读原文件：

| CLI | 实际内容 |
|---|---|
| `--cover-directory`、`--cover-result-sha256` | 原 f12f C result和全部1440头/六primitive/查询等原依赖 |
| `--far-directory`、`--far-result-sha256` | 原 fe667 全112深端 result及完整原行流 |
| `--original-sampling-directory`、`--original-sampling-result-sha256` | 原965c或32b完整 sampler 输出；原source/run保持真实 |
| `--original-family` | 恰为 `positive` 或 `joint`，必须与实际原result相符 |
| `--code-directory` | 全部真实冻结 computations；原 helpers 按完整SHA读取 |
| `--proof` | 原 R380 proof SHA `8a51036fd130c80365284c2e4678c3aa765d177471b4d16df0f4c85add016fa9` |
| `--unit-row-proof` | R357 proof SHA `286f17eeab74b44716985fd199d5085cde667fb2626a9eb508ef72d35bc29140` |
| `--origin-launch-directory`、`--origin-launch-result-sha256` | 实际原193或joint203的 BVP-launch result，用于绑定实际原钟；不由新模板补写 |
| `--job-deadline`、`--job-deadline-sha256` | 上述原launcher实际消费的原deadline文件 |
| `--out` | RUNNER_TEMP下独占fresh目录，不覆盖或包含任一输入 |

两个已注册原钟来源：

| 来源 | launcher schema | launcher SHA | deadline schema |
|---|---|---|---|
| 原193 | `current-C-continuous-ten-full453-frozen450-owned-process-launch-v1` | `6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` | `request193-owned-job-science-deadline-v1` |
| joint203 | `current-C-continuous-ten-joint-full453-frozen450-owned-process-launch-v1` | `cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7` | `request203-owned-job-science-deadline-v1` |

原deadline的实际 bytes/SHA 必须等于原launcher `actual_job_deadline`；recipe SHA、repository/run/source也逐值相同。科学截止仍原 `namespace_created_unix_seconds + 18900`，读回预留2700。不会产生新的起始时刻或补造原launcher接受。

该复用producer不以原 BVP accepted 作为自己的数学门；它只需要已完整far/native geometry原件及真实原钟。真正 refinement owner 仍须核自己的真实 accepted450父。两个责任分开。

## 5. 显式工作参数和实际CLI

以下都必须传入，没有暗设未来预算或分辨率：

- `--steps`：原正整数native步数；
- `--precision-bits`：64至4096；
- `--sample-max-nodes`：本次新 inverse range work-unit 上限；
- `--sample-inverse-depth`：0至60；
- `--sample-value-bits`：0至1024；
- `--max-geometry-cache-records`：正整数；
- `--free-bytes-reserve`：非负整数；
- `--budget-seconds`：正有限数，覆盖本次source/runtime绑定、原账读取与新采样全部时间。

原远端不重传播，因此本命令没有 `--linear-budget-seconds`、`--max-panels`、原far深度或Taylor work参数，也不把它们的旧值伪称本次执行值。原far使用了什么工作范围，由原件和原source完整保留。

调用模板只表示参数形状，所有变量须来自实际同job配方/回执：

```bash
python -u "$COMPUTATIONS/geometry_20261116_current_C_same_far_resampling.py" sample \
  --cover-directory "$ACTUAL_C_DIRECTORY" --cover-result-sha256 "$ACTUAL_C_SHA" \
  --far-directory "$ACTUAL_DEEP_DIRECTORY" --far-result-sha256 "$ACTUAL_DEEP_SHA" \
  --original-sampling-directory "$ACTUAL_PARENT_GEOMETRY_DIRECTORY" \
  --original-sampling-result-sha256 "$ACTUAL_PARENT_GEOMETRY_RESULT_SHA" \
  --original-family "$ACTUAL_ORIGINAL_FAMILY" --code-directory "$COMPUTATIONS" \
  --proof "$ACTUAL_R380_PROOF" --unit-row-proof "$ACTUAL_R357_PROOF" \
  --origin-launch-directory "$ACTUAL_ORIGIN_LAUNCH_DIRECTORY" \
  --origin-launch-result-sha256 "$ACTUAL_ORIGIN_LAUNCH_RESULT_SHA" \
  --job-deadline "$ACTUAL_ORIGINAL_DEADLINE_FILE" \
  --job-deadline-sha256 "$ACTUAL_ORIGINAL_DEADLINE_SHA" \
  --precision-bits "$PRECISION_BITS" --steps "$NEW_STEPS" \
  --sample-max-nodes "$FRESH_SAMPLE_WORK_LIMIT" \
  --sample-inverse-depth "$FRESH_INVERSE_DEPTH" --sample-value-bits "$FRESH_VALUE_BITS" \
  --max-geometry-cache-records "$GEOMETRY_CACHE_RECORDS" \
  --free-bytes-reserve "$FREE_BYTES_RESERVE" --budget-seconds "$REMAINING_OWNED_SECONDS" \
  --out "$FRESH_R450_DIRECTORY"
```

这些参数不意味着保证完成。资源不足会保原完整未付范围。`sample-max-nodes`名称沿原producer，实际计的是 `complete_box` 新范围工作次数，而不是一定等于distinct物理点数。

## 6. 原件完整绑定

### 6.1 C与深族

原 `c2f515aa.bind_inputs` 仍真实读取/核：实际f12f cover及输入绑定、原fe667完整深行、同C原物理参数/根族、完整1440源流、cut实际binary词、原query和全部闭反像叶、深端/自然域/保护拼接条件。新的 `actual_original_input_binding` 必须与原sampler绑定全对象相同，不只比较fingerprint、completed或三个cut盒。

同一实际C但不同运行/不同原cover盒的潜在语义复用没有在本版放宽；本API明确要求同job原件。R426/R447等别的对象传递职责也不由此代付。

### 6.2 远端与表示

原 `geometry.finite_far_radius`、原far点word、原row中每个radius word和原required-prefix radius一致；cut保持原准确binary值。原far点四个数值代表和其各自误差记录完整保。

原 `actual_far_coordinate_mu_word` 既与每个行相同，也必须与原完整node_mu数组最后8字节相同。它直接成为本次最后节点的$\mu$字。不会重新取far盒中点或重新做`exp`后仍暗用旧Q/Π边界。

112 mode记录按实际索引0至111及频率2至224检查。原mode完整flags、全候选数量、全部叶数量、0个未证norm、没有pending/transaction、原candidate unit hull和数值行完整误差一致。每个mode所有四种ledger span连续无缺并到原流末尾；原未提交span必须为空。

原矩阵必须逐bytes等于所有原行两个系数字构成的112×224矩阵，包括实际负零；原数组descriptor shape/dtype/order/bytes/SHA完整检查。输出矩阵直接拷原字节，不重新归一、选中点或评估新的参数点。

### 6.3 大账保留边界

`far-all-mode-rows`和远端在`sample-inverse-leaves`中的全部原span正文按实际JSON行读取。far完整管/覆盖/commit/prepared/coefficient账及joint选择账都全流读取bytes/行数/SHA，但其全部数值正文不在本消费者再证明。原程序的正确性、原实际完整运行和记录的范围是复用前提。

所有这些原大账仍在原Actions临时目录。新result明确保存原目录+全部descriptor+实际完整读入身份，完整全族候选误差不删。只要下游/最终必要读回仍需要它们，原目录不能主动清理。不会将大账写入Git、Release或artifact，也不把它们拆为编码消息。

## 7. 输出结构与完成/未完成

新输出包含：

- `result.json`：本producer完整实际范围；
- `geometry.json`：同原结构的真实新数组与独立R450 provenance；
- `actual-radial-field-plan.json`：全部节点、stage和实际field字；
- `retained-general-far-row-intervals-and-representatives.json`：原完整行文档逐字拷贝，保原schema并外层明确原来源；
- `large-arrays/node-radii.f64le`、`node-mu.f64le`、`full-stage-field-geometry.f64le`：新原算法实际形成；
- `large-arrays/complete-general-far-matrix.f64le`：原完整矩阵逐字拷贝；
- 新 `coefficient-boxes.jsonl`、`sample-inverse-leaves.jsonl`、`numeric-point-values-and-errors.jsonl`、`complete-unpaid-scope.jsonl`。

`same_original_far_family_reuse`记录完整原远端出处和112模式摘要，`complete=true`只表示该原完整对象已按合同核入。它不是新BVP接受。`actual_far_modes_attempted=[]`与`actual_far_modes_completed=[]`明确本次没有新线性传播；`reused_complete_far_modes`才记录原112模式。

`completed`和`native_geometry_ready`只有全部新格/数组形成后才true。`numerical_sample_work_resolution_complete`可为false而有效粗包围仍完整；不把工作分辨率没达到冒域失败。

点索引0明确保留原far anchor，并加原账路径/span来源。新的其他点从1开始。`actual_fresh_point_count`不含far anchor，`actual_inverse_range_count`只计本次新范围计算。

## 8. 完整pending与资源中断

`native_plan_address`始终给当前phase：

- source绑定尚未完成：全部577节点/576stage未开始，实际steps已知但完整field计划尚未形成；
- nodes：`next_node`到577的完整后缀，同时所有fields未开始；
- fields：当前`next_stage`、`next_field`和当前field数，完整plan保每个未访地址；
- array_materialization：所有field已算，但数组/最终结果仍未完整；
- complete：全部实际形成。

具体inverse异常由原 `InverseSampler` 把全部当前闭栈写入同一个unpaid ledger。source复用中断时，`reuse_binding_progress`保当前账的已读bytes/行数、每个已完整账identity和所有未访账名；不把hash未读完的旧流标complete。

`ResourceStop`继承RuntimeError，原仅捕获ArithmeticError的区间细分不会吞掉它。TERM/INT记录外部中断，在下一个资源检查停止。返回75是资源partial；其余异常/原条件未齐返回2；0仅为本次完整geometry。源绑定/异常保存失败导致无result时，外层必须保持未知/未读，不能制造成功回执。

whole-call预算是协作检查，包含setup但不承诺异步打断底层库调用。原外层OwnedChild、同一绝对deadline、TERM→KILL、child PID/start ticks/PGID和quiet责任仍须实际调用方保留；本source不生成新规则runner或隐藏子进程。

## 9. 新 native configuration

接口：

```bash
python -u "$COMPUTATIONS/geometry_20261116_current_C_same_far_resampling.py" configure \
  --directory "$FRESH_R450_DIRECTORY" --result-sha256 "$ACTUAL_R450_RESULT_SHA" \
  --original-config "$ACTUAL_PARENT_NATIVE_CONFIGURATION" \
  --original-config-sha256 "$ACTUAL_PARENT_NATIVE_CONFIGURATION_SHA" \
  --computations "$COMPUTATIONS" --quadrature "$NEW_NATIVE_N" \
  --out "$FRESH_R450_NATIVE_CONFIG"
```

原config必须实际指向本次复用的原sampling result。全部原source map文件按原SHA读取，原非几何字段保留。新cfg更新：

- 本次真实 `geometry_directory`及`geometry_result_sha256`；
- 新明确native `quadrature`和真实新geometry的`steps_per_stage`；
- 三个新来源及原native/bridge/QR/capacity/nominal依赖source map；
- `R450_same_far_fresh_grid_origin`透明记录原config、原sampling、新result、独立client与尚未注册旧caller的边界。

原$N>896$且为偶数的全角条件保留。这个config工厂不自行检查“新N必须大于父N”；那是原refinement recipe的显式因子合同，必须由注册后的caller原样保持。R450本身是一份合法来源的sampling/config组件，不私自更改哪种refinement被请求。

新TailClient API保持：

```python
client = TailClient(actual_new_config, actual_source_topic, fresh_native_prefix, node_heap=...)
answer = client.solve(actual_H112, jacobian=True, audit=False)
fresh = client.solve(actual_same_H112, jacobian=True, audit=True)
client.close()
```

这里仅说明接口，不是已发生的调用。原32iterations/10trials、2e−9、η0完整112敏感度、全577节点、完整physical jets/338响应、mean和原全部错误分支保持。完整FD/fullDN/450 writer等还由真正caller执行，不能把两次示例方法调用当成完整接受流程。

## 10. 必要读回、单90KB与清理

接口：

```bash
python -u "$COMPUTATIONS/geometry_20261116_current_C_same_far_resampling.py" readback \
  --directory "$FRESH_R450_DIRECTORY" --result-sha256 "$ACTUAL_R450_RESULT_SHA" \
  --out "$FRESH_R450_READBACK_DIRECTORY"
```

标准库reader真实读取result及新ledger/数组完整bytes和SHA。必要正文包含源/run/clock、所有完成flag、原错误、全部unpaid记录、当前plan后缀、完整112模式的原两个系数字、候选数量与相关原span；原大candidate/factor/point正文只保原件身份和范围，不声称读者已逐值独立复核其数学。

原完整far样本作为result成员，其必要identity明确写“canonical member bytes/SHA”，不冒单独文件。原大账在producer阶段已完整hash读取；reader的原ledgerdescriptor是对这个实际动作的回执，不冒自己再次读取所有旧大账。

输出 `summary.json`，stdout完整一份：

```text
BEGIN_R450_SAME_FAR_FRESH_GRID_NECESSARY
<one complete JSON document>
END_R450_SAME_FAR_FRESH_GRID_NECESSARY
```

另打印bytes/SHA身份事件。若有GITHUB_OUTPUT，只写 `same_far_summary_bytes`、`same_far_summary_sha256`，不把完整正文再塞到report；完整必要正文留compute日志。

超过90000 bytes时返回70，只回传明确oversize身份，不切块/编码、不提高限额、不删除完整必要失败或未访地址后声称成功。资源/科学partial的完整必要读回可以正常返回0；它表示读回完成，不能重标科学完成。

本source不产生cleanup许可marker、不删除任何raw、不执行native owner quiet检查。调用方必须先真正确认相关生产进程停止，再调用完整必要读回，并继续保持原全部其他读回/quiet条件，最后才可删自有临时目录。原far目录与新geometry都必须活到实际下游及所有必要读回完成。

## 11. 完整依赖与真实来源

采样实际加载原positive或joint模块之一，且旧数学模块原名字/字节不变。主依赖：

| 原文件 | 完整SHA |
|---|---|
| `geometry_20261115_current_C_pruefer_positive_radial_sampling.py` | `965c277c5aad5a3b5c8c817600d4c435186d9ce1b267b0b59f6e7a8fa69de390` |
| `geometry_20261115_current_C_pruefer_joint_radial_sampling.py` | `32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4` |
| `geometry_20261115_stored_C_finite_head_pruefer_positive.py` | `c2f515aa276890da63871fe0e9e1440775950d4985465457e9d6025976d914c8` |
| `geometry_20261115_stored_continuous_E_cover_v3.py` | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| `geometry_20261115_stored_continuous_E_cover_v2.py` | `004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea` |
| `geometry_20261115_stored_continuous_E_cover.py` | `9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed` |
| `geometry_20261115_stored_continuous_C_far_graph.py` | `fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a` |
| `geometry_20261115_stored_C_finite_head_flux.py` | `4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d` |
| `geometry_20261115_stored_C_finite_head_projective.py` | `5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216` |
| `geometry_20261115_stored_C_finite_head_riccati.py` | `34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124` |
| `geometry_20261115_stored_C_finite_head_pruefer.py` | `250474d748842d9b5423be2123460308ab16419d4b5dac1d8c9967fc208c0122` |
| `geometry_20261115_pruefer_positive_endpoints.py` | `91dd207bc20a87a36e2d4bc13e1b88a14333b67cf47ec048f85e8d46500822ff` |
| `geometry_20261115_pruefer_joint_row_representative.py` | `24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97` |
| `geometry_20261115_current_C_general_robin_native.mjs` | `fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349` |
| `geometry_20261115_current_C_synchronous_linear_bridge.mjs` | `67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286` |
| `exact_20261115_current_C_general_robin_chain.py` | `946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5` |
| `exact_20261114_tail_capacity_loader.mjs` | `07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395` |

native原root/product/cusp/physicalJet/metric/noJ仍来自实际原config的`original_runtime_sha256`和同一restored source_topic。newclient核原声明source文件；原owner的`loadOriginalRuntime`继续核实际runtime。后继完整450 driver还须保原全source closure与其固定原runtime pins；此三源不放宽原驱动的该项合同。

只选择positive时其原采样无joint形成步骤；已有原矩阵逐字保留。不过新独立worker/client共有来源清单包含joint nominal文件，须作为明确依赖恢复，即使本次不调用它重形成任何行。

## 12. 给后继owner/driver注册的准确改动范围

root后继要接R441/R448时，需要独立来源分支，而不是在旧源上全局改名字：

1. owner把fresh samplercall换为本 `sample`，从真实原父config定位原sampling目录/result SHA，并传同一原origin/deadline。实际新budget由原剩余时间裁剪。
2. 绑定本新result schema/source；保 `actual_original_input_binding`逐原C/深族相同，切点和far字相同。
3. 用 `configure` 的真实新config、独立client/worker及完整new source map；该source tuple是唯一明确变化，其他native方法/阈值参数不能随之放宽。
4. 原family source仍写入reuse provenance。新geometry不再被称由965c/32b重新传播；原parent真实来源不改。
5. 真正完整450再执行原fresh RHS、currentH、全部338×112J/FD/fullDN/final/fresh audit，实际新writer/runtimeclosure要包含新来源。
6. 下游接受新checkpoint/owner来源时也要显式注册。没有注册的旧caller保持拒未知source，不补旧成功标签。

本版没有实现root尚未给出的owner/driver新文件，也不宣称已可直接作为冻结R448的同名替代。这是最小三来源组件的明确边界；新增source注册不改变数学接受条件。

## 13. 不支付的责任与实际验证范围

没有本地import/AST/compile/fixture/科学运行。只读原源、逐文本生成两个薄来源视图和独立consumer、计算文件字节SHA/完整diff并完成纸面推导。没有新request/workflow或未来run。

本文不证明新采样/原far误差小到足够；不保证新的steps或N使BVP收敛；不把数值代表视为单一准确C；不支付准确同g atlas、共同材料拉回、全域metric、reach、held、δE或连续极限。变M必须有新真实模式来源；已有模式的条件复用理论见R450末节，当前源码固定112。
