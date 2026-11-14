# 同一 live current576 进程上的实际 H/J、原 FD 与完整 fullDN

日期：2026-11-14。作者：geometry 工作代理。分类：独立可执行接线；尚无本入口的科学回执。

本组件把已冻结的多请求尾客户端与已冻结的 `geometry_20261114_physical_test_full_dn.py` 接通。数值工作只允许在 `Rogerhu12/math-research-public` 的 Actions 中执行。它不修改既有数学源，不把旧零高度导数检查改成新高度检查，也不产生新的完整曲面接受结论。

## 1. 唯一新增入口与已冻结依赖

新增 `computations/geometry_20261114_live_current576_full_dn.py`。它只负责真实输入绑定、建立当前边界上下文、调用原 FD 函数、把同一个客户端交给原 fullDN 入口和保全结果。

它使用以下四个已冻结 live 组件：

| 文件 | SHA256 |
|---|---|
| `geometry_20261114_current576_live_tail_client.py` | `c9f3377748480d4905a32f7f858e2b9a5bcb8a697b7b7806ffc409e635ed1189` |
| `geometry_20261114_current576_live_tail_client_hook.mjs` | `7e83b398fe0f8a8801700d50c640b1e97bc185ec07627468f94fc54de61a58f5` |
| `exact_20261114_live_current576_damped_system.py` | `9346c0a7e7c7f562d20b02126b82c8819c687a7575aea38258e9796cabb8db4a` |
| `exact_20261114_live_current576_damped_chain_qr.py` | `ee174e8283f3b5454a8b3dbe751dbd4f41f4f0dba1bd9d240b627bd2748f889f` |

多请求的 native 范围、bootstrap、每个 call 的 H/target/σ/J/状态身份、原 ten-trial 与最终敏感性范围，沿用 [live 客户端总接口](2026-11-14-current576-live-client-multirequest-extension-contract.md) 和 [逐请求 adapter 接口](2026-11-14-live-current576-per-request-adapter-interface.md)。本入口不改这四源。

原 fullDN 入口固定为 `geometry_20261114_physical_test_full_dn.py`，SHA256 `abbf1a53cb454effc7e90e97166a469b84eb61cd7d75832dc3c2ab0f81add10b`。它仍依次使用原 physical φ 边界、完整带状前缀求解器和原 lifted/fullDN 源。

## 2. 真实输入：不用旧大包填空

本入口需要：

1. 实际已接受的原 M96/N1024 前缀文件。既有身份 `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` 不变。
2. 一份最新真实、明确未接受的完整 M112/N2048 warm 及其同次 `driver-status`。两个文件各自的实际 SHA256 必须由 CLI 提供。status 的 `latest_warm_sha256` 必须指向所给 warm，status 的完整共同 `identity` 必须与 warm 的 `optimization_warm` 相符；原当前 producer 的每个记录来源也逐文件核 SHA。
3. 原完整 port 及原 native config。port 必须与 warm 的完整 scalar specification 一致；config 固定原 `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`，未改 modes、RK、shooting、远端图、32 迭代、求解容差或最终审计参数。
4. **实际完成的第 61 轮 native 结果**，其 `result.json` SHA256 由 CLI 提供。不能填写未来结果或把仅第 59 轮一步接受当成该结果。
5. 从公开仓库原恢复工具得到的完整 78 件 native 原源；没有另一个仓库或旧私有源输入。

第 61 轮父包仅需以下八个文件，目录结构和字节由已冻结 live client 核验：

```text
result.json
current-solve-spec.json.gz
current-input-config.json
native_0001.json.gz
native_intent.json
native_ready.json.gz
native_capacity.json
original-live-identity-before-selected-seed.json
```

不需要第 17–59 轮的全 J/factor 大包，也不需要额外导入零 H 响应。warm 保留的旧零 H SHA 是历史来源，不是本次 FD 的实际尾响应。

本接口编写时最新已知前缀是 actual63 的 `warm-001.json.gz`，SHA256 `6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a`。其未压缩 status SHA256 为 `8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46`。若公开存储采用 status 的 gzip 文件，CLI 必须绑定实际压缩文件的 SHA；解码对象仍由 `original.read` 读取。这里没有把这两个参考值预编为未来唯一输入。新的真实 warm/status 可以由后续 request 提供，但完整原字段和 producer 仍须绑定。

## 3. 为什么不能只覆盖旧 FD 的 EXPECTED

冻结 `geometry_20261114_constrained_trust_response.py` 同时使用 `EXPECTED['tail_anchor']` 核对 CLI 尾响应文件，以及 warm 历史上的 `actual_zero_anchor_sha256`。其 setup 又明确要求该 anchor 的 H 恰为零、residual 恰为零。因此把一个真实新 H 的响应 SHA 填入该字典会错配原历史；改 warm 的历史字段则会造假。

新入口不调用那个带零 H 限制的 `main`。它直接调用原已冻结的：

- `make_directions`，保原全部 core、物理末端和三个 scalar-control 方向；
- `refined_directional_check`，保 `2e-6, 1e-6, 5e-7` 三个中心差分步长、两级 Richardson 外推、原 contraction 判据与 `5e-5` 阈值；
- 原 `PhysicalTestBoundary`、`SeparatedBoundary` 与完整 Jacobian；
- 原三项显式局部扰动：`yb[iz+1] += 1e-5`、`yb[iz+32] += 1e-9`、`yb[iz+M] += 1e-10`。

原 `constrained_trust_response` 没有改写 `yb` 的 core 段，本入口也不另加这一步。所有原 states/rhs/controls/mean 均完整保留，局部扰动只是 FD 的代码检查点，既不是新的 native 请求，也不是保存 warm 的修改。

新 FD 有两份独立来源：原 warm 的历史零 H provenance 完整不变；本次真实 H/J 则单独绑定当前 live worker 的完整请求与返回文件。没有沿用旧 pass 的 SHA 或标签。

## 4. 实际执行次序与 H 的身份

`build_context` 用原 `LiftedModesPrefixProfile`、完整相同 scalar/port/supports、原全 453 行状态、原 Frenet RHS 和当前边界构造上下文。当前 H 由原 `true_height(boundary, states[-1])` 计算；不做阈值化、截频、归零、逐 mode 筛选或重投影换图。

随后：

1. 新进程的原 `TailClient` 完成 ready/source/config/capacity 验证，cache、last、tangent predictor 都由该新进程实际建立。
2. 已冻结 live 客户端先把第 61 轮完成响应的 **literal JSON 解码状态** 仅作初猜，对 bootstrap H 真实调用原 solve 和完整 endpoint J。没有把旧 response 放入 cache。原 JSON 未导出的负零不冒称恢复。
3. 同一客户端对当前 warm 的完整 H 调用 `solve(H, jacobian=True, audit=False)`。如果它与刚完成的 bootstrap H 满足原相等判断，可以命中该新进程自己的原 cache；否则必须真实求新 H。此处不强制 H 非零，也不把一个确实为零的 H 改成伪非零试验。
4. 返回结果通过原 native 容差、完整 J、checkpoint H 和该 live cache 的身份核对后，保存 `actual-response/actual-anchor-tail.json.gz`。随后创建 `AffineTail(H, response)`，只在原 FD 检查中保持该映射为 affine。
5. FD 期间无 native 调用；前后实际 call count、cache key 和 response 对象身份保留。如果原 FD 失败，保存实报并关闭 worker，不进入 fullDN。
6. FD 真通过后，原 `physical_test_full_dn.main()` 读取这份新报告。原 `load_client` 唯一一次调用被一个薄转交函数接住，核同 module/config/source-root/prefix/heap，返回**同一个仍存活的 Python client 与 worker**。
7. 原 fullDN 的完整 preflight、inner Newton、外循环、当前 H/末端 H 两类真实 native 请求和 final audit 继续执行。相同 H 的非 audit cache 仍由原 client 决定；audit 请求保持原 fresh 调用。

原 fullDN 原本在 preflight 保留已保存端点。即使实际首个 fullDN H 与 FD 的 H 在数值或字节上不同，本入口也只记录差异，让原 client 对那个实际 H 正常求解；它不会用旧锚点替换新 H，也不增加“首 H 必须完全相等”的科学接受门。

原 client 使用数值相等判断 cache，原 worker JSON 输出会折叠部分负零。因此报告分别保 current H 的 raw identity、literal response H 的 raw identity、数值是否相等、字节是否相等。原相等 cache 不被更严格的负零条件替换；所有实际 native request/snapshot 的原 bits 仍由 live hook 保留。

## 5. 保留的原科学门

前缀端保持原完整内层方程、17 个 Newton 回溯、RMS `1e-6`、完整 BC `1e-11`、默认 8 次 outer、固定最终 scalar 后的物理 RMS 检查及最终真实 native audit。原 material Rθ 与完整角 cut audit 仍作为原入口的独立测量，不冒称 Rφ 接受就是 Rθ 接受。

尾部仅沿已发布 live hook 的范围，把每轮非线性 solve 的唯一 correction 调用换成当前完整 576 链的 R273 η=1。原 fresh-withJ、10 个 noJ α、全部原 guard、严格原 σ 范数下降、native `2e-9`、32 次迭代和最终敏感性/J/audit 仍保留。尤其**最终 endpoint sensitivity 没有套 η 阻尼**。

本 driver 不对 L2、exact 线性缺陷、原 condition 数、首 H 字节一致性或 full-angle cut 测量添加新接受阈值。输入字节/来源/维数核对用于保证运行指定对象。

如果原 fullDN `main()` 返回失败，原状态、失败请求与 trace 都保留，顶层状态如实记录该原 return code。只有原 `actual.json.gz` 的 `success=True` 且原 return code 为 0，顶层才写 `full_BVP_accepted=True`。即便如此，`full_Cartesian_closed_surface` 和 `task_completed` 仍为 false：闭面、同 g 精化、reach、整像位移等工作另付。

## 6. CLI

下列 SHA 必须替换成所选实际文件的完整 64 位值；参数不是预造回执：

```bash
python -u "$COMP/geometry_20261114_live_current576_full_dn.py" \
  --accepted "$ACCEPTED96" \
  --warm "$ACTUAL_WARM" --warm-sha256 "$ACTUAL_WARM_SHA" \
  --warm-status "$ACTUAL_WARM_STATUS" --warm-status-sha256 "$ACTUAL_STATUS_SHA" \
  --port "$ORIGINAL_PORT" --tail-config "$ORIGINAL_CONFIG" \
  --tail-source-root "$RESTORED_PUBLIC_SOURCE_TOPIC" \
  --anchor-result "$ACTUAL61_DIR/result.json" \
  --anchor-result-sha256 "$ACTUAL61_RESULT_SHA" \
  --material-angles 4096 --physical-angles 4096 \
  --node-heap 6144 --jac-workers 2 --max-nodes 1200 \
  --outer-iterations 8 --native-eta 1 --native-exact-workers 2 \
  --native-max-factor-bytes 2147483648 \
  --out "$VISIBLE_OUT/live-full-dn" \
  --work "$RUNNER_TEMP/live-full-dn-prefix-work"
```

其余原 CLI 参数是 `--extension-step .005` 与 `--taper-fraction .4`，均原样传给原入口。原 peak curvature 从所给真实 warm 的完整 scalar specification 读取。RMS/BC 等科学门没有新的可放宽选项。

建议由既有 `root_20261114_current576_rules_runner.py --out ... --command <上述 argv>` 包住，真实 pull 后检查两 README，并按既定规则处理新规或同步失败。只恢复公开原源；token 只由 Actions 的同步/发布权限供应，源码、结果及命令记录中不含 PAT。

## 7. 输出与完整资源账

```text
orchestration-status.json
input-binding.json
same-live-client-handoff.json
actual-response/actual-anchor-tail.json.gz
actual-response/response-check.json
full-dn/                         # 原 fullDN 输出原名
full-dn/true-tail_*.json.gz       # 同一实际 client 的所有请求/响应
full-dn/true-tail-current576-bridge/
  bootstrap-result.json
  external-call-*.json
  call-0001/iteration-000/...    # 原 live snapshot/QR/output 全文件
  call-0002/...
  live-client-summary.json
```

所有大原阵与 factor 继续在各轮 `large-arrays/` 下，只入 Actions artifact；不删轮次、不裁 mode、不覆盖输入、不只保存最优小报告。原未导出的 noJ 全残差不冒称已导出。外层只加请求/H/真实 call count 的元数据记录。

默认 8 次 outer 的实际协议请求数保守上界为：1 次 bootstrap + 1 次当前 warm anchor + 16 次 outer anchor/end + 1 次最终 audit = **19 次**。原同 H cache 可以减少实数，但不能事先假定每次都命中。

每个 native call 仍保原 32 次迭代。仅固定 binary snapshot/factor payload 的既有账为每 correction `704,385,296` bytes，故 19×32 的保守固定部分为 `428,266,259,968` bytes；可变 ledger、JSON、日志、前缀工作区和压缩 artifact 另外占空间。这是容量上界，不是预测会运行所有 608 轮。**第 61 轮单 call 的 32 GiB 预检不覆盖完整 fullDN 多 call。**

工作流草稿把运行前最小可用空间作为本次 request 的明确资源计划；实际值应依据第 61 轮真实轮数、可用 runner 容量和所选 outer 预算制定。driver 记录开头/结尾空间、全部 call 数、每次 cache/请求结果，不用删除现场或降低科学容差解决空间不足。跨进程资源续接不能冒 cache；当前 live bootstrap binder 仍明确只接受第 61 轮父对象，其他完成响应若要成为新父需独立诚实接口。

## 8. 已做与未做

本地仅写源码、读取实际 warm/status 的 JSON/SHA、解析 Python AST 和比较源码。actual63 的共同 status identity 与 warm identity 逐项一致，46 个已记录当前来源文件 SHA 一致；没有本地重新计算 H/RHS/FD/native/fullDN。

第 61 轮实际成功、当前 H 尾解成功、FD 通过以及完整 fullDN 接受，都必须由后续公开 Actions 真回执说明。本接口不把这些未来条件写成事实。

## 9. 参数化工作流草稿

附独立草稿 `visible-larger-public-live-current576-full-dn.yml`，建议最终位于 `.github/workflows/`。唯一 push trigger 是 `computations/public-native-live-full-dn-request.json`；lane 为 `livecurrent576fulldn`，实际启用前由 root 将该 lane 加入既有 publisher 白名单。草稿没有填写一个未来的第 61 轮 SHA，也没有预建空壳 request。

request 的 schema 为 `public-live-current576-full-DN-request-v1`，固定仓库名与单一 lane，包含：

- `source_sha256`：全部本轮实际源 basename→SHA。包括新入口、live 四件、原 QR/kernel/byte reader、原 fullDN/FD/边界、worker/engine、公开恢复/规则同步/publisher 等；草稿逐件核 SHA、只做 Python compile 和 Node syntax check。
- `inputs`：`accepted`、`warm`、`warm_status`、`port`、`tail_config`、`anchor_result` 各为 `{file,bytes,sha256}`，`file` 是公开 topic 内的仓库相对路径；`anchor_files` 为上述八件第 61 轮同目录原件的描述器。草稿只窄检出这些明确文件，不全检出 notes。
- `runtime`：`node_heap`、`jac_workers`、`max_nodes`、`material_angles`、`physical_angles`、`outer_iterations`、`extension_step`、`taper_fraction`、`native_eta`、`native_exact_workers`、`native_max_factor_bytes`，逐项转成正常 argv，不拼接 shell 字符串。
- `resource_plan`：本次明确的 `minimum_free_bytes` 及可附依据。它是运行资源计划，不是数学容差；不能只把上一单 call 的 32 GiB 当成这里的多 call 全程预算。预检只可能清理 runner 上列明且未用的 SDK，不删任何科学原件。

Node/Python/NumPy/SciPy 与前次版本完全相同：24.22.1、3.12.14、2.3.5、1.17.0。科学 step 经原规则 helper 包裹，输出和全部部分现场 always 上传；publisher 仅发布有界小件。草稿仍采用 350 分钟 job/320 分钟科学 step 的运行资源上限，不把它改写为原 native 迭代或精度上限，不声称一次 job 必然完成所有 outer。

新增入口最终源码 SHA256 为 `7ba3fd5f183a7772e8f4d5a7b23073610dece4fdd5ba8c1ccbf7d05052597502`，32,084 bytes。纯 AST 比较确认两处原 `refined_directional_check` 调用、`make_directions` 调用和三项 `yb` 扰动与冻结 constrained response 对应代码一致。工作流 YAML 已纯语法解析；未导入或执行任何数学模块。
