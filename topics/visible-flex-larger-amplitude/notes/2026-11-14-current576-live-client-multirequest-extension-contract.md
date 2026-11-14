# 同一 live TailClient 的逐请求 current576 / R273 接口

- 作者：geometry agent。
- 日期：2026-11-14（UTC）。
- 分类：独立源码与输入/输出合同；未执行新科学计算。
- 前提：实际第 61 轮必须已经完整通过原 native solve、完整 endpoint Jacobian 和原 audit。尚未出现的结果、SHA 和收敛情况均不预填。

本接口将第 61 轮的唯一 nonlinear correction 替换推广到一个真正持续存活的 TailClient。它保留原 worker 的请求循环、每个请求的 fresh with-J、全部十个原 no-J 试探、原 norm 严格下降、原 guard、原 solve tolerance、原 maxIterations，以及原末端 sensitivity/J/audit。原 fullDN 的数学入口无需修改，通过已有 `--tail-client` 模块接口接入。

第 61 轮被冻结的两个运行源和两个 Python consumer 不在此改动。本接口有新的来源和 schema，不把第二个请求标成第一个请求，也不把旧 H 的响应或矩阵改标签后使用。

## 1. 已读原源码中的实际调用链

`geometry_20261114_physical_test_full_dn.py`（SHA `abbf1a53cb454effc7e90e97166a469b84eb61cd7d75832dc3c2ab0f81add10b`）调用原 banded/lifted 包装，最终仍执行 `geometry_20261114_full_dn_solve.py`（SHA `c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162`）的完整 outer loop。后者只构造一个 client：

1. `load_client(module_path, config, sources, prefix, heap)` 读取模块导出的 `TailClient` 或 `WeightedTailPort`。
2. 每个 outer 开始，对当前材料 H 调用 `client.solve(H, jacobian=True, audit=False)`，将真正的 native 坡度和完整 J 设为 inner affine map。
3. inner BVP 通过原门之后，对新的材料 H 再实际调用 `solve(newH, True, False)`，重新检验 true nonlinear boundary。
4. fullDN 的冻结物理 RMS 通过后，再显式调用 `solve(Hfinal, True, True)`；最终 audit 之后还重核完整 boundary，并执行原全角 cut 读出。

原 `exact_20261114_true_tail_client.py`（SHA `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09`）只对本进程已经真解、数值完全相同且 `audit=False` 的 H 使用现有缓存；若此次要求 J，缓存还必须已有完整 J。`audit=True` 总会发出新的协议请求。此行为原样保留。

原 `78718-prefix-tail-tangent-fourier-worker.mjs`（SHA `36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a`）只有在一次 `dn.solve` 真正返回 `sol.converged` 后，才执行 `last=sol` 并尝试构造 `tangentPredictor`。后续请求原样先尝试 tangent predictor，再使用原 amplitude/fallback 和原 Dirichlet 初猜修正。构造 predictor 本来就可能报告 unavailable；本接口不将该诊断伪造为成功。

## 2. 为什么不能直接拿第 61 轮 hook 接第二个请求

第 61 轮仅处理明确的一次请求，故其 scope 中有以下真实限制：

| 第 61 轮固定项 | 多请求对象必须保留的真实身份 |
|---|---|
| `native_call=1` | 原 worker 每个实际协议请求的正整数 `call` |
| 闭包抓取第一个 H，`spec.fresh_request.height` | 当前 request 的完整 112 模态 H |
| 固定 target/σ 的 SHA | 本次原 solve 实际产生的 target/σ；同 call 内不改，下一个 call 可变 |
| 全局 `iteration-000` 路径 | `call-0001/iteration-000` 等独立目录 |
| 每个 `it=0` 都核 actual59 状态 | 只首次 bootstrap 的 `it=0` 核 literal anchor 初猜；其后使用原 predictor/fallback 的实际状态 |
| actual59 选中态来源 | 真正完成的第 61 轮原 response 的显式实际 receipt |

far Robin graph、原 geometry、原 profiles、原 integration grid、gains 和原科学 source 仍随同一个 immutable native 对象固定。本接口不全局改 `linearSteps`、steps、远端门或残差尺度公式。

## 3. 真正 bootstrap；不导入旧 response cache

新模块为 `geometry_20261114_current576_live_tail_client.py`，导出原 constructor 兼容的：

```python
TailClient(config_path, source_root, record_prefix, node_heap=6144)
WeightedTailPort = TailClient
```

constructor 启动一份新的原 worker 并核 ready/source/config，但不伪造 `last`、`tangentPredictor` 或 Python response cache。第一次外部 `solve` 前，先对 anchor 的原 H 做一次真实 `solve(Hanchor, jacobian=True, audit=False)`。它采用实际第 61 轮完成 checkpoint 的完整 literal 解码状态作为初猜，并且在新的 worker 中真正经过原 solve/J。只有此实际请求成功返回，原 worker 自己才能形成其新的 `last` 和 predictor；原 Python client 自己才产生同进程缓存。

随后把调用方的原 H 和原 `jacobian/audit` flags 交给原 `TailClient.solve`。如果第一个外部 H 恰好与刚刚真实 bootstrap 的 H 相同且不要求 audit，原缓存可能命中；这属于原本存在的同进程缓存。任何新的 H 都必须实际求解；任何 `audit=True` 都必须新发协议请求。wrapper 记录 protocol call 的实际增量和缓存命中，不用猜测代替。

这次 bootstrap 只是得到当前活 worker 的合法初态/导数对象。父文件的成功不被当成新 worker 已经成功，也不被当成 fullDN 或闭面已经成功。

### 原 JSON 的负零范围

第 61 轮最终原 response 走原 JSON 协议，不能据此恢复未导出的、序列化前的负零。新模块只声称：将真实 response 中 `checkpoint.states` 的 JSON 解码数值转成完整 577×224 literal binary64 初猜，然后保存该新 literal 对象的 raw 字节和负零 sidecar。

`parent_anchor.pre_JSON_negative_zero_preservation_claimed` 明确为 `False`。不宣称 literal 对象等于旧 worker 未导出的 raw 终态。新 bootstrap 仍须原门真实重解，所以这一来源声明没有改变任何原科学容差。

## 4. 最小实际父输入和环境参数

实际父 `result.json` 的 SHA 必须显式输入；下面不预造第 61 轮的未来 result SHA。源要求父 result 声明原 native 完整成功、真实原请求数 1、原 worker exit 0、完整原 J/audit 返回，并且复核原 response 的收敛、原 residual 门、J 维度/有限性和 audit 存在。

父 result 的完整 inventory 绑定下列 7 件输入，另加 result 本身：

```text
current-solve-spec.json.gz
current-input-config.json
native_0001.json.gz
native_intent.json
native_ready.json.gz
native_capacity.json
original-live-identity-before-selected-seed.json
```

不必重取第 28 轮完整 J、不必取第 17–23 轮全部历史，也不必为初猜读取第 61 轮所有 QR 因子。原 78 个 numerical sources 和原冻结 calibration 输入仍按原 source/client 身份恢复。父文件若超过 Git 小文件规则，由真实 artifact 选择性取件处理，不能截断父 response。

通过原 fullDN `--tail-client` 指向新 Python 模块；constructor 的原四参数不变。新增显式环境参数为：

```bash
export VISIBLE_FLEX_CURRENT576_ANCHOR_RESULT="实际61目录/native-current576-damped/result.json"
export VISIBLE_FLEX_CURRENT576_ANCHOR_RESULT_SHA256="实际该文件完整64位SHA256"
export VISIBLE_FLEX_CURRENT576_LIVE_ETA="1"
export VISIBLE_FLEX_CURRENT576_LIVE_EXACT_WORKERS="2"
export VISIBLE_FLEX_CURRENT576_LIVE_FACTOR_BYTES="2147483648"
# 可选；默认由 record_prefix 生成独立的 *-current576-bridge 目录。
export VISIBLE_FLEX_CURRENT576_LIVE_OUTPUT="独立且空的新输出目录"
```

`VISIBLE_FLEX_LIVE_CURRENT576_SPEC` 是 wrapper 给自身 Node 子进程设置的内部变量，不由用户手工构造。新 wrapper 不接入旧 zero-cache 子类；只借用其纯来源比较 helper。真正继承的是原 `exact_20261114_true_tail_client.TailClient`。

## 5. 每个实际请求的身份和同步 bridge

新 hook 为 `geometry_20261114_current576_live_tail_client_hook.mjs`。原 engine 内仍只替换唯一的：

```javascript
const cor=correction(ev,states,target);
```

替换后调用当前 request context 的 synchronous bridge。原 source 的 evaluate、ten-trial body、其余 solve 源码、原 endpoint sensitivity 和 audit 均可逆比回原字节。新增的 worker 代码只在原 `let initial,predicted=false;` 后插入 request context；只有第一个 bootstrap 请求给 `initial` 赋 literal anchor 并令 `predicted=true`。第二个及以后请求不写 `initial/predicted/last/tangentPredictor`，后面的原 predictor/fallback 代码原样执行。

每个 request 在第一次实际 correction 前建立独立目录；若原 fresh with-J 直接已满足 tolerance，request 可能没有任何 correction snapshot，这仍是原逻辑。

```text
call-0001/
  request.json
  literal-seed-restored.json       # 仅首个 bootstrap
  iteration-000/
    snapshot/
      request.json                # 本 call 原 request 文件的逐字局部副本
      context.json.gz
      array-manifest.json
      core-instrumentation.json
      flow-return-metadata.json.gz
      result.json                 # 完整 snapshot 最后完成 receipt
      large-arrays/...
    qr-launch.json
    qr.stdout.log
    qr.stderr.log
    qr-exit.json
    qr/...
    returned-correction.json
  current-corrections.jsonl
  current-correction-summary.json
```

当前 request 文件保存完整 `height[112]`、`jacobian`、`audit`、实际 `native_call`、bootstrap/seed 标志及完整 H raw SHA。由于 JSON 写出本来可能丢负零，该 metadata 另保原 JS H 的 `height_negative_zero_columns`。snapshot 的 `physical-height` 仍直接来自实际当前原数组，不从 metadata 重建；sidecar 让独立 reader 能逐字对照两者。

本 call 的首次 snapshot 记录实际 target/σ/H/far SHA；后续校正只核本 call 内未改变。下一 call 的 target 和 σ 从它自己的原 fresh evaluate/solve 作用域获取，不能偷用上一 call 的常量。

## 6. 数组、consumer 和恢复方向

仍保存全部原 10 阵：`base-states[577,224]`、`stage-residuals[576,224]`、`stage-out[576,224]`、`original-scales[1,577]`、`cut-residual[1,112]`、`end-residual[1,112]`、`original-far-graph[1,112]`、`physical-height[1,112]`、`cut-target[1,112]`、`stage-jacobians[576,224,224]`。原 rawNode 为 9 项物理边界索引，不误写成 577 个 rawNode。

三个 snapshot schema 是：

```text
live-current-native576-withJ-snapshot-result-v1
live-current-native576-withJ-snapshot-context-v1
live-current-native576-withJ-snapshot-arrays-v1
```

context 保存 `parent_anchor` 和 `current_request`。前者绑定实际第 61 轮 result/response 及新 literal seed；后者绑定本次真实协议 H/flags 和 snapshot 局部 request receipt。只在 `native_call==1 && nonlinear_iteration==0` 核 literal 初猜状态；不能把后面的真实状态强迫为父状态。原 soft cut/far 误差直接保留，方向中相应分量亦不投影。

独立 live consumer 使用同 R273 QR 算法和同完整 exact 整数行核，只泛化输入来源和 request scope。输出 schema 为：

```text
live-current-native576-complete-linear-system-binding-v1
complete-native-live-current576-damped-square-root-direction-v1
complete-native-live-current576-damped-direction-arrays-v1
complete-native-live-current576-damped-direction-v1
```

每轮 child CLI 仍为 `--snapshot-directory --snapshot-result-sha256 --eta --out --max-factor-bytes --exact-workers`。Node 使用 `spawnSync(..., shell:false)`，子进程 stdout/stderr 都写独立迭代文件，不污染原 worker 的一行 JSON 协议。全 577×224 原坐标方向与 checkpoint、negative-zero sidecar、source、current snapshot、matrix identity、request identity 均逐字/逐字段绑定后才返回给原十试探。

L2 模型值、gradient、exact linear defect 和 QR 诊断全部保存；本 bridge 不用这些值增加 nonlinear acceptance 门。`maxChartCondition:null` 明示本方法没有计算原 Riccati chart condition，不伪造低 condition。

## 7. 完整响应、记录范围和资源

Python 外部 `.solve` 继续让原 client 决定真实 native response 是否通过，其余 fullDN tolerance、物理 RMS、完整 boundary 和最终全角 cut 测量均在原入口。新模块不返回完整 prefix/闭面成功旗。即使某次 native correction 成功，最终原 sensitivity/J/audit 若失败，仍保留原失败，不能把已接受中间态升级为完整响应。

本接口与第 61 轮一致，只在原 correction 入口保存完整 fresh with-J 数组。原 no-J 十试探本身没有新增完整阵 observer；其完整实际返回/guard/norm 仍沿原 trace/trial recorder。直接达到 tolerance、未进入 correction 的最终 with-J 不冒称另有完整 snapshot。独立 summary 只描述它真实观察到的 bridge 点，native 成功以原 response 为准。

每个 correction 的固定二进制部分约 704,385,296 字节；exact ledger、JSON、日志和其它输入/响应还随数据变化。第 61 轮单个请求最多 32 轮的资源预算不能宣称覆盖 fullDN 的全部 outer requests。本模块保留所有 per-call/per-iteration 输出，没有新请求数上限、没有缩小原 maxIterations、没有删因子或改变科学门。

后续工作流应依据真实第 61 轮轮数/资源回执安排计算空间。若跨进程从一个已完成 native checkpoint 继续，只能再做真实 bootstrap；不能把旧 predictor 或 response cache 假造到新进程中。

## 8. 冻结源码、已完成静态核与尚未执行的工作

四份运行源码的最终身份如下。前两份在 `/tmp/current576-live-multi/`，后两份在 `/tmp/current576-live-adapter/`，由 root 复制到本题 `computations/` 后统一提交；原第 61 轮四源不修改。

| 文件 | UTF-8 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_current576_live_tail_client.py` | 26,175 | `c9f3377748480d4905a32f7f858e2b9a5bcb8a697b7b7806ffc409e635ed1189` |
| `geometry_20261114_current576_live_tail_client_hook.mjs` | 44,032 | `7e83b398fe0f8a8801700d50c640b1e97bc185ec07627468f94fc54de61a58f5` |
| `exact_20261114_live_current576_damped_system.py` | 28,963 | `9346c0a7e7c7f562d20b02126b82c8819c687a7575aea38258e9796cabb8db4a` |
| `exact_20261114_live_current576_damped_chain_qr.py` | 21,688 | `ee174e8283f3b5454a8b3dbe751dbd4f41f4f0dba1bd9d240b627bd2748f889f` |

截至冻结，两份新运行源码只做了 AST、Node 语法和纯字符串变换检查；没有导入 numerical module、实例化 native constructor 或执行任何 RHS/J/ODE/QR/native 计算。exact agent 的两个子源只做源码/AST核；其数学 QR engine、整数 kernel 和原 raw-array 读出方法保持冻结来源。

纯源码检查确认：

- 原 core 文件 SHA `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`。
- 原 evaluate SHA `9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9` 保持。
- 原十试探 body SHA `603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99` 保持。
- engine loader 插入可逆，原 nonlinear correction 是唯一替换。
- worker loader/context 插入可逆；用于语法检查的 request fixture 是原 worker 源码字符串，并未执行其 constructor 或请求。

`parent_anchor`、局部 request receipt、完整 112 高度负零 sidecar、四个输出 schema 和完整恢复方向已对照这四份冻结源逐字段核。纯源码变换报告在同目录 `pure-source-roundtrip.json`，它只声明代码字符串身份，不声明任何实际 native 结果。

第 61 轮成功、后续 bootstrap 成功、newH 成功、fullDN 接受、全闭面几何以及课题完成均不能由本静态接口推断。
