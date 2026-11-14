# 从实际59状态继续：当前576完整快照与 R273 同步子求解接口

分类：计算接口与源码条件说明；尚未执行本入口，不是新的数值接受结果。  
作者：ChatGPT（exact_refinement，AI 辅助）。  
日期：2026-11-14。

## 1. 已有证据与本次接口的范围

实际59已经在原576段对象上接受一次原生试步：原 `noJ` 无穷范数从
`0.04177307820740199` 降到 `0.0001289424025918576`。它还不是完整
native 收敛响应。完整 QR、原方程双向精确读回及字节审计见
[实际59 QR说明](2026-11-14-actual59-original576-QR-and-two-exact-readbacks.md)；
选定状态和实际试步见
[实际59首步说明](2026-11-14-actual59-original576-first-native-step-and-state-audit.md)。

本接口从实际59的完整选定状态继续。原 native 循环每次先执行原来的
`evaluate(states,target,true,scales)`，随后只在原来计算 `correction`
的位置调用同步 Python 子进程。子进程读取刚返回的完整数组，产生
一个 R273 阻尼方向；父进程随后继续原十个 `noJ` 试步、原 guards、
严格无穷范数下降、原迭代上限与最终容差。最终 endpoint J 和完整
audit 仍由原实现实际执行。

因此，实际59的 `noJ` 范数不是下一轮 `withJ` 的缓存值；本接口不要求
两条浮点执行路径在同一状态给出逐位相同的范数。本次 child 也不读取
actual28 的基态或 Jacobian，不把57的方向或1372段对象更名为当前576对象。

完整数学模型和平方根消元证明见 [R273](../results/R273-complete-native-damped-square-root-chain.md)。
本接口实现只复用下列已冻结类，不重新实现其数学。

## 2. 冻结源码与借用边界

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `computations/exact_20261114_current576_damped_system.py` | 22749 | `695c2a564ada2bfc3cac251dfb5bd46bf99f6d16b696c64b75d9f90703a6ed90` |
| `computations/exact_20261114_current576_damped_chain_qr.py` | 21013 | `ac04842bb9c42b9f29c8209d0d5f523c83744aa548e5615267521d8bf2c3141f` |

子进程只借用以下冻结组件。

| 组件 | SHA256 | 使用范围 |
|---|---|---|
| `exact_20261114_native_damped_chain_qr.py` | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` | 动态 `NativeDampedChainQR` 类；不调用该历史文件的1372段 `main` 或固定 exact context |
| `exact_20261114_native_allrows_dyadic_residual.py` | `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f` | 原576维数的完整整数 cut/stage/far 行核、行序和原始 operand 选择器 |
| `geometry_20261114_native_captured_band_correction.py` | `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390` | JSON/gzip、原始数组输出、SHA和相等性工具；不实例化旧 `CapturedArrays`，不调用旧 band solver |

新 adapter 的 `Current576System` 只核当前快照及来源。其构造不执行
RHS、ODE、J、QR或原 native solve。当前主入口的所有科学计算必须在
`GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`
的本公开仓库 Actions 环境内运行。本文建立时只做源码阅读和 Python AST
解析，没有本地 import 或数学执行。

launcher/hook 的固定文件名为
`geometry_20261114_native_current576_damped_solve.py` 和同名 `_hook.mjs`。
为避免两侧源码 SHA 循环依赖，adapter 按当前 checkout 的这两个精确文件
核快照里的 producer SHA；launcher 则钉住本节两份新 Python 的最终 SHA。
发布 workflow 再钉住全部最终源。当前来源因此具有两侧字节绑定，不能
通过改一个快照字段静默切换执行代码。

## 3. 唯一实际父状态

父来源固定为公开 run `43640772654` 的实际选定状态，而不是其线性方向。

| 父文件 | 字节数 | SHA256 |
|---|---:|---|
| `result.json` | 10047 | `c0a9b191e843e9036e84707ffa1855d5881dce13e4b71bf94812e9526b59d00e` |
| `trial-replay-summary.json` | 5762 | `770b97e62eda7cbcc10b045c42298b95ef2c55a0f2dd5ac1930690175a156709` |
| `selected-state-checkpoint.json.gz` | 1255992 | `7659016c0218b8c2e9ba220ca81a0b410b7e38005ea609e417b9b534d76c3556` |
| `selected-state.f64le.gz` | 954571 | `8ade070f746caed9a45c582c7485a060e55ee589858f5f88255d8ffd0d9112cb` |

完整577×224选定状态的解压后1033984B SHA为
`384de298d6274ef7a6f5bdbc4e6cf6ef9dee5fb9bffd020b7b60001463940e03`。
完整物理 H 的原始字节 SHA 为
`c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f`。
首次当前快照必须保留该状态的全部字节，包括负零；后续迭代则绑定自己
真实的当前状态 SHA。父文件由 launcher 启动时完整核验，不在每轮子进程
重复解压数MB父状态；每轮 context 仍保存这四个准确来源收据。

`rawNode=[0,72,144,216,288,360,432,504,576]` 是原9个物理分段边界索引。
它不是完整 shooting 状态的577个节点列表。新 adapter 明确核这9项原值，
同时另保 `node_count=577`。原 cut 高度 H、target、far graph 与全部577个
sigma 维持原值。R273 方向中的 cut 和 far 分量不投影、不清零；启动状态
也不再被错误要求满足逐位 `Q0==target`。

## 4. 每次真实 `withJ` 返回值的快照

建议路径由父进程唯一创建，不能复用上轮目录。

```text
iteration-000/snapshot/result.json
iteration-000/snapshot/context.json.gz
iteration-000/snapshot/array-manifest.json
iteration-000/snapshot/core-instrumentation.json
iteration-000/snapshot/large-arrays/...
iteration-000/qr/...
iteration-000/qr.stdout.log
iteration-000/qr.stderr.log
```

`result.json` 最后写入，schema 为
`current-native576-withJ-snapshot-result-v1`，含 `snapshot_completed:true`、
producer/hook SHA、`native_call`、`nonlinear_iteration`、`snapshot_sequence`、
M112/K224/depth576，以及 context/manifest 的 `{file,bytes,sha256}` 收据。
它与 context 逐位绑定实际 `norm/minA/minD` numberRecord。

本请求只有一次 worker protocol `call=1`。原源码的最终 `audit(sol)` 只遍历
profile/physical jet/RK，`heightJetJacobian` 只计算 tangent graph 和 cut jets，
最多额外调用 `evaluate(withJ)`，都不再调用 `solve/correction`。
`numerical-tail-slope-jacobian.mjs` 的 analytic slope 替换也不调用 solve。
所以 `native_call=1` 没有跳过第二次原非线性求解；若未来增加第二个独立
worker 请求，必须定义新的启动和多请求合同，不能复用本次首请求标签。

当前 `minA/minD` 由原 with-J 四字段路径归约，它们不是 no-J 的 Infinity
占位。不过，原 guard 没有给这些元数据另加 finite 条件。新 adapter 因而
只验证它们的实际16位 little-endian hex、IEEE classification 与 JSON value，
保留 NaN/±Infinity/negative-zero 的原记录，不把额外 finite 断言变成科学门。
原 residual norm 和进入 QR 的完整 J/r/状态/边界/sigma 数组另按有限输入
合同核验；所有 sigma 必须是原严格正值。

### 完整10数组

| 数组名 | 形状 | 数据来源 |
|---|---|---|
| `base-states` | 577×224 | 该次原 `evaluate` 的完整输入 states |
| `stage-jacobians` | 576×224×224 | 原 `ev.flows[n].J`，每4个stage一个chunk |
| `stage-out` | 576×224 | 原 `ev.flows[n].out` |
| `stage-residuals` | 576×224 | 原已保存 `ev.residuals[n]`，不重新相减定义另一舍入对象 |
| `original-scales` | 1×577 | 本次原 scaleFor 结果 |
| `cut-residual` | 1×112 | 原表达式 `states[0][j]-target[j]` 的当前结果 |
| `end-residual` | 1×112 | 原 `ev.end` |
| `original-far-graph` | 1×112 | 原 diagonal far graph |
| `physical-height` | 1×112 | 请求的完整原 H |
| `cut-target` | 1×112 | 原 solve 的 target |

manifest schema 是 `current-native576-withJ-snapshot-arrays-v1`。每阵保
`dtype:<f8/order:C/shape/total_bytes/raw_sha256/completed/chunks`；每chunk保
名字、顺序、覆盖行区间、文件、bytes、原raw SHA。所有原字节完整保留。
adapter 流读全J并逐块核 SHA，不在内存再持有一份整231MB J。

context schema 是 `current-native576-withJ-snapshot-context-v1`，包含完整
当前原数值 sources、去IO的 configuration/parameters、9项rawNode、全部
576个 `rawCell/rawSegment/portRatio/mu/profiles`、graphs/gains/far SHA、
10阵raw SHA及实际59父收据。core instrumentation 保存唯一 correction 调用
替换的精确逆变换证明；原 core 文件 SHA为
`ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`。
原 evaluate 与十试步正文保持原字节。

## 5. 同步子进程 CLI 与返回合同

```bash
python topics/visible-flex-larger-amplitude/computations/exact_20261114_current576_damped_chain_qr.py \
  --snapshot-directory "$ITER/snapshot" \
  --snapshot-result-sha256 "$ACTUAL_SNAPSHOT_RESULT_SHA" \
  --eta 1 \
  --max-factor-bytes 2147483648 \
  --exact-workers 2 \
  --out "$ITER/qr"
```

snapshot result SHA 必须从本轮真正完成的文件取得，不能预写一个未来 SHA。
可选 `--factor-budget-seconds` 是明确资源预算；默认无额外子预算。原 native
迭代上限、容差和十个alpha不由本 CLI 更改。`--exact-workers` 只选择1至4个
原整数行核进程。输出必须是全新且与 snapshot 独立的目录。

父进程使用无shell的 `spawnSync`，把 child stdout/stderr 直接写入本迭代
专用日志文件。child 的进度JSON不能进入父 Node worker 的请求/响应 stdout。
失败保完整 snapshot、已生成的因子/常数/方向和错误回执；未完成方向不冒
完整方向返回。完成结构校验后，父进程再从完整原坐标delta原bytes及CP恢复
所有577×224分量和负零，并检查 live states/target/scales 未被桥改动。

主要输出 schema 和字段为：

| 对象 | schema / 主要字段 |
|---|---|
| `result.json.gz` | `complete-native-current576-damped-square-root-direction-v1`；`native_delta/native_direction_checkpoint/input_binding/factor_summary/factor_report/factor_index/formed_stage_inventory/formed_model_diagnostic/original_exact_readback/array_manifest` |
| `native-direction-checkpoint.json.gz` | `complete-native-current576-damped-direction-v1`；完整577行、显式负零列、原坐标raw SHA、完整input binding |
| `output-array-manifest.json.gz` | `complete-native-current576-damped-direction-arrays-v1`；全部因子、纯常数、输入副本、z、delta及exact ledger收据 |
| `input-binding.json.gz` | `current-native576-complete-linear-system-binding-v1`；完整当前矩阵来源 |
| `summary.json` | `native-current576-damped-chain-small-summary-v1`；小于95000B，否则给明确compact指针，不裁剪完整result |

result、CP、manifest和关键报告统一保存当前 `snapshot_result`、
`native_call/nonlinear_iteration/snapshot_sequence/current_state_sha256` 和
`new_matrix_identity_sha256`。binding 明确保留
`snapshot_result_sha256/snapshot_context_sha256/snapshot_manifest_sha256/`
`raw_array_sha256/adapter_source_sha256`。没有1372 restriction字段。

科学调用计数特意使用 `*_in_this_child`：本child没有new RHS/J/ODE或nonlinear
trial；它读取的是父进程刚完成的真实 fresh withJ。这些零计数绝不表示父
native 没有发生新的数学计算。

## 6. 完整模型、精确读回与原验收分开

仍用原 sigma 坐标 `delta_n=sigma_n*z_n`，每个577节点的完整224维恰添一次
`eta*I`。原576个stage、112个cut和112个far行全保，全部非零模式和coupling
全保。factor类用两个局部Householder QR消元、完整纯常数累计及三角回代；
不形成正规矩阵、不做Riccati图逆、不截秩、不加另一个ridge。

形成到binary64的加权系数是一个单独记录的有限模型：采用原冻结class的
longdouble表达式再cast，不能称该权重形成是精确有理数的正确舍入。
`formed_stage_inventory`、同系数完整A/AT的gradient、model energy与factor
energy差都如实保存；若gradient很大，不能用小三角残差隐藏它。

另一个独立读回直接对保存的完整当前原J、实际原r和最终恢复的binary64
delta做exact dyadic运算，再精确除以原sigma：

$$
e_{0,Q}=\delta_{0,Q}+r_{\mathrm{cut}},\qquad
e_n=J_n\delta_{n+1}-\delta_n+r_n,\qquad
e_{N,\Pi}=\delta_{N,\Pi}-G_N\delta_{N,Q}+r_{\mathrm{far}}.
$$

总129248行全存为 `large-arrays/current576-all-exact-rows.jsonl.gz`；每个block
的全部整数行、原sigma、精确极大值、原J SHA、最终direction SHA和当前snapshot
身份都保存。全局见证另存完整原始operand hex。这个读回不使用已经舍入的
`J*sigma_next/sigma_n` 矩阵，且不把eta罚行算入原方程。

两者都不增加非线性门。原保存数组的精确线性残差不是数学 flow 的精确
导数证明；L2阻尼下降也不保证原无穷范数下降。父进程仍必须实际执行原
十个 noJ 试步、原 guards、原 strictnorm；若全拒、后续withJ失败、最终J或audit
失败，都保留真实失败。本文没有宣称这些未来结果已经发生。

## 7. 全产物保留与磁盘预算

每轮固定二进制存储可直接由维数与冻结class格式计算，和本次求得的数值无关。

| 固定部分 | 字节数 |
|---|---:|
| snapshot完整576×224×224 J | 231211008 |
| snapshot另外9阵 | 3107464 |
| child保留的9阵原输入副本 | 3107464 |
| child完整z与完整delta | 2067968 |
| 全577节点三角因子/下一块/affine及全部纯常数 | 464891392 |
| 每轮固定部分合计 | 704385296 |

32轮固定部分合计22540329472B。以上尚未包含精确整数ledger、CP/JSON/gzip、
进度日志、流返回均值/guard元数据、原worker较小checkpoint以及初始输入原件。
实际59完整exact ledger压缩后约6.2MB，故26GB在类似实际ledger大小下是有
余量的工程预算；它不是任意有限binary64输入的严格全部输出上界。

保守来源界也解释这个区别：224项有限binary64乘积及两项有限binary64
加减，在统一 `2^-2148` 整数单位下，最大整数所需位数不超过4204位。
十进制系数采用不超过1280字符的宽松上界后，129248个完整行记录加上
逐block分数/索引/见证及gzip开销，可比上述实际6.2MB大很多，约180MB级
原文本预算才覆盖极端记录。这个是表示容量估计，不是新的数学通过门。

因此若要在无中途删除的条件下覆盖32轮，建议至少32GiB可用空间，并另
保初始原件、runner工具与上传暂存的真实余量。所有因子与纯常数仍是完整
artifact；不得为了省空间删除常数、跳过某轮J或丢弃不利残差。工作流资源
不足应如实停止并保已生成原件，而不是改原数学或把不完整结果叫完成。

目前两新Python仅完成AST和源码合同核验；实际循环、每轮产物大小、原
native最终tol/J/audit与闭曲面完成标准，均等待公开Actions真实回执。
