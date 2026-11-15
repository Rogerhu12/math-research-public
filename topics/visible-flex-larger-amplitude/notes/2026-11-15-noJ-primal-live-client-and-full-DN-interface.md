# 新 noJ primal 的 live 多请求与实际 H→FD→fullDN 接口

作者：`/root/geometry`，GPT-6 Astra Pro（AI-assisted）  
日期：2026-11-15 UTC  
分类：**源码实现与接口说明；尚无本入口的数值结论。**

本组件只在公开仓库 Actions 执行科学计算。它将已发布的 live 客户端和实际 H→FD→fullDN driver 接到 [R275](../results/R275-original-noJ-primal-identity-and-complete-variational-chain.md) 所述独立 noJ primal flow。原第 61 轮失败不作为成功锚点。第 73 轮结果仍须真实返回完整 native 解、endpoint J 和 audit，才可提供本接口所需的成功父输入；本说明不预造其 result SHA 或接受结论。

## 1. 现有链和最小变化

此前已保存的 `geometry_20261114_current576_live_tail_client.py` / `_hook.mjs` 负责一个持久 native worker、每请求当前 576 段快照及 R273 桥；`geometry_20261114_live_current576_full_dn.py` 负责真正当前 H 的尾解/J、同一实际 anchor 的原仿射 FD，以及同一客户端向原 `geometry_20261114_physical_test_full_dn.py` 的交接。三个旧文件保持原字节。

独立新文件如下。

| 新源 | 责任 |
| --- | --- |
| `geometry_20261114_noj_primal_live_tail_client.py` | 验证真正成功的第 73 轮父结果；只把原 JSON 解码状态用作初猜；真实 bootstrap；维持同一客户端及原 cache；保存外部请求与实际响应关联。 |
| `geometry_20261114_noj_primal_live_tail_client_hook.mjs` | 第一次请求安装新 flow；每次真正协议请求建立独立上下文；每次当前 correction 保存原数组并同步调用新 QR CLI；原 trial/最终方法保留。 |
| `exact_20261114_noj_primal_live_current576_damped_system.py` | 只读并验证本请求、本轮快照及新 flow 身份；不重算 RHS/J/ODE。 |
| `exact_20261114_noj_primal_live_current576_damped_chain_qr.py` | 复用冻结 R273 完整模型和 exact 行核，输出本轮完整 577 节点原坐标方向。 |
| `geometry_20261114_noj_primal_live_full_dn.py` | 复用原实际 H、FD、fullDN driver，只换新客户端、来源和 schema。 |

新 flow 仍是已冻结的 `geometry_20261114_noj_matched_variational_engine.mjs`，SHA256 `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9`。本适配不复制或改写该算法。R273 因子源仍为 `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33`；原完整 exact 行核仍为 `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f`。

本次最终冻结身份如下；result/response 的实际 SHA 仍由运行时提供。

| 源角色 | bytes | SHA256 |
| --- | ---: | --- |
| 新 live client | 29,877 | `7aa2aba10e44f0a0fd0e6eee47e9239a2f2244bb9663b8ec5ede294edc71bb64` |
| 新 live hook | 51,076 | `0e802785329c73d5a951ca69942414ca5dcc40a9284dae9d31c4ca6cb819daa1` |
| 新 live snapshot adapter | 33,197 | `e30e53e635f84ae4762ef045e6510c20d63524efd604ba617cec3a849bdfb3d3` |
| 新 live QR CLI | 22,328 | `c3284d556e76f389d084bc612579c485697f15aeb4c5b7a5caa49567a9920909` |
| 新 actualH/FD/fullDN driver | 32,522 | `bb8ad207c5b85fb10e0a5ee83b36eed4317c757646055eaec58b2bc3c8945c14` |

最小数值变化相对于旧 live 链，是给每个唯一 `cell.engine` 安装该独立 `flowStateWithJacobian`。相对于第 73 轮，新变化是实际多请求调度、成功父来源以及请求级记录；每步 primal/tangent 算术不再改动。旧 ready 的 backend 标签只描述原 constructor；新的 flow 来源、安装记录和每个 snapshot 另行明确保存。

## 2. 真正父输入：result 加八个完整文件

调用者必须显式给出 `--anchor-result` 及其实际 `--anchor-result-sha256`。父 result 的 schema 为 `native-noj-primal-current576-damped-solve-result-v1`，producer 固定为：

- Python：`938fbec22f0733fff6ceb22e6e9b7a9e12942c12d1eae31c608d8f517702df8c`；
- hook：`099798e9c57f09b82f7532ea184d124446aeeb2cdbafe452390cb794b8db405d`。

必须实际有 `success/native_accepted/original_complete_client_response_returned/actual_original_converged_flag=True`、原 worker exit 0、完整 J/audit 请求及返回。响应仍须通过原 native 容差；不因本适配增加更小的数学阈值。

只需父 result 的下列八个完整同目录文件，逐一用其原 inventory descriptor 检查 bytes/SHA：

1. `current-solve-spec.json.gz`；
2. `current-input-config.json`；
3. `native_0001.json.gz`；
4. `native_intent.json`；
5. `native_ready.json.gz`；
6. `native_capacity.json`；
7. `original-live-identity-before-failed61-seed.json`；
8. `primal-flow-installation.json`。

第 7 个文件名保留真实父 producer 的历史名称，并非另把失败 61 的状态设为新锚。实际初猜来自成功父 `native_0001.json.gz` 的 `response.checkpoint.states`。无需为此重取 61/73 全部 J、QR 因子或迭代 ledger。

父 installation 必须由同一 73 producer/hook/spec 记录，声明同一 `f9b292…` flow、原两个依赖 SHA、576 段、原 noJ 函数未包装。成功响应里原 endpoint J 的完整 `(3×112+2)×112` 个有限值、audit、checkpoint、H、参数、rawNode 与 config/source/ready/capacity 关联均保留。

`parent_anchor.schema` 为 `completed-native73-noj-primal-literal-JSON-anchor-v1`。除既有 response/result/source/H/rawNode 等字段外，它保存 `parent_primal_flow_installation`、`primal_flow_source_sha256` 和 `original_primal_dependencies`。其 actual result SHA 由真实输入产生，不写入一个未来值。

### JSON 与负零范围

原响应 JSON 未保存的序列化前负零不能恢复。新客户端只把原 JSON 文字正常解码得到的完整 577×224 数值按 `<f8` 写出，并为解码后仍存在的负零保留 sidecar；这些原始字节和相同 checkpoint 互核。记录明确标注 `pre_JSON_negative_zero_preservation_claimed=False`。它是一个完整初猜，不声称与未导出的原内部数组逐位相同。

## 3. 一个新 worker 的实际执行次序

Python 保留原 TailClient constructor 和原协议。仅向唯一原 Node worker 命令增加本 hook 的 `--import`，其余 subprocess（包括规则同步的 Git 命令）照原执行。constructor ready/capacity/source 核完、尚无请求/cache 时写 `verified-launch-intent.json`。

第一次真正协议请求固定为父完整 H、`jacobian=True,audit=False`。在原请求 loop 的 `let initial,predicted=false` 之后，插入 `await beginNativeRequest(...)`：

- 安装每个唯一 engine 的新 withJ flow；原 root/rhs/rk4/rhsWithJacobian 函数引用不变；
- 保留实际完整 installation、engine→stage 映射、factory options 和原/新函数源码身份；
- 把上述 literal JSON 状态赋给 `initial`，只在此处设 `predicted=True`；
- 不写 `last` 或 `tangentPredictor`，不引入 `initialCheckpoint` 几何重映射。

随后必须真实调用原 native solve 和完整 endpoint J。只有其成功返回，原 worker 才建立自己的 `last` 和 tangent predictor；原 predictor 若报告不可用，也按原逻辑保留事实。旧进程响应从未导入新 cache。

后续每次真正协议请求只建立新的 `call-NNNN/` 上下文，使用当前请求全部 H 模式、原 predictor/fallback、当次 target/σ。不把非零新 H 替换为锚点 H，不按阈值截零，不强制 Q0 等于 target，不清除 soft cut/far 误差。

原同进程、相同 H、非 audit 请求的 cache 语义保持。缓存按原数值相等判断，不能称其额外提供 H 的逐位相等。外部请求记录同时保本次 H 的 raw SHA/负零 sidecar、实际调用前后编号、是否 cache hit，以及实际 `native_NNNN.json.gz` 的完整 receipt。cache hit 不伪造一个新 native 请求；`audit=True` 必须真实增加一次协议调用。

## 4. 新 flow 与原方法的精确边界

新安装沿第 73 轮原源码，以原 cfg 的 modes/spacing/quadrature/cuspAwareFlow 和各 cell 的实际 μ、原 parameters 的 orientation/projectionFloor 构建。只赋值 `engine.flowStateWithJacobian`，不修改 profile、graphs、gains、far graph、port、H、σ 或原原生 noJ 验收路径。

安装时不运行 root/RHS/ODE。所有 fresh withJ 的具体状态推进、捕获 local root 和切向形成，仍由冻结 `f9b292…` 源执行；完整226状态/两mean/仅224shape反馈及 cusp/ordinary 条件见 R275。实际跨所有 576 段的结果由后续本入口的 Actions 报告决定，不能把第 71 轮两段逐位吻合扩大成此入口已完成。

原 core 中只把唯一 `correction(ev,states,target)` 调用改成同步 R273 桥。完整 core 与内层 solve 源码可精确逆还原；原 evaluate 和十 trial body 原字节不变。这里另有独立 withJ 属性变化，故全局 `only_nonlinear_correction_call_replaced=False`，并明确 `only_core_nonlinear_correction_call_replaced=True`。

最终 endpoint sensitivity/J 和 audit 的原方法不被 η 正则化或替换。它们可能使用已明确的新 withJ flow；这不能描述为旧 J 字节或旧 sensitivity 结果重用。audit 原 noJ 数值验收保持。若最终方法真实失败，不能把先前残差较小或已完成 correction 宣称完整 native 成功。

## 5. 每次请求、每轮 snapshot 与完整方向

`call-NNNN/request.json` 保存本请求 H、jacobian/audit 原 flags、H raw SHA、负零列、本 call 是否 bootstrap、是否赋初猜等。每个 correction 的 snapshot 中复制相同文件，并以 `current_request.request_file` 本地 receipt 关联；不会引用上一请求的物理 H。

新三种 snapshot schema：

- `noj-primal-live-current-native576-withJ-snapshot-result-v1`；
- `noj-primal-live-current-native576-withJ-snapshot-arrays-v1`；
- `noj-primal-live-current-native576-withJ-snapshot-context-v1`。

每轮继续完整保存十组原数组：577×224 base states、576×224 residuals、576×224 out、577 scales、112 cut residual、112 end residual、112 far graph、112 physical H、112 target、576×224×224 fresh J。它们来自当前已返回的 `ev` 和本次原 states/target/scales，不能套用旧实际 28、61、73 的基态标签。

context 另保 `parent_anchor`、`current_request`、`primal_flow_implementation`。installation 原文件逐字复制到 snapshot 本地；身份包含原依赖和新 source。明确 `original_evaluate_and_flow_source_not_instrumented=False`、`original_evaluate_source_not_instrumented=True`、`same_original_noJ_primal_contract=True`。

只有 call 1、iteration 0 核查 literal seed raw SHA。后续状态完全以实际当前数组为准。H/target/σ/far 在一个请求内部核不变；跨请求允许完整当前 H、target、σ改变。原 rawNode 为九个物理分界 `[0,72,144,216,288,360,432,504,576]`，并非 577 个节点索引。

新 child 只消费这一当前 snapshot，schema 为 `complete-native-noj-primal-live-current576-damped-square-root-direction-v1`；binding 为 `noj-primal-live-current-native576-complete-linear-system-binding-v1`。完整 native_delta 仍是原 Q/Pi 坐标 577×224；checkpoint/array schemas分别为 `complete-native-noj-primal-live-current576-damped-direction-v1` 和 `complete-native-noj-primal-live-current576-damped-direction-arrays-v1`。

Node 按实际 child result、binding、matrix identity、当前状态/request/flow 与完整 delta/checkpoint 原字节/负零核回，原样返回所有 cut/far 分量。R273 L2、梯度、exact 线性缺陷只作诊断，不变成新的非线性通过门。原十 alpha、原 noJ evaluate、所有 guards、strict norm decrease、32 次上限与原 `2e-9` 容差仍由原 solve 决定。

每个 child 用 `spawnSync(...,shell=False)`，stdout/stderr独立落到本轮文件，不污染 worker JSON 协议。所有 snapshot、因子、常数、exact 行账与失败原件继续保存。未进入 correction 的最后 withJ 或所有 noJ 返回阵没有新增全量 observer；其保存范围以实际原 trace/response/checkpoint 为准，不声称完整全阵都已导出。

## 6. 当前真实 H→原 FD→原 fullDN

独立 driver 仍读取当前真实 warm/status 全部453状态和完整 v3 scalar，按原 `true_height` 公式构造 H，实际调用上述同一个 live client 求当前 H/J。锚点与当前 warm 无需 H 相等。若原 fullDN 重新构造后其第一个 H 与 FD anchor 不同，仍交给同 client 真求解，不替换 H，也不额外以相等性拒绝。

FD 的三个原扰动、原 directions、两层四阶 Richardson 及 `5e-5` 条件保持。FD 只对刚求得的实际当前 H/J 构造明确仿射图，不在 FD 内再调用 native。warm 的历史零 H anchor provenance 保持原值，当前 true-H/J 的 receipt 独立记录，不把原零锚 FD pass 换上新标签。

原 `physical_test_full_dn` 获得同一 Python client、同一 worker PID、同一 source/config/path/heap。原 inner 方程、物理 RMS `1e-6`、BC `1e-11`、默认八次 outer、实际 endpoint 请求和最后 `audit=True` 不变。FD pass、native pass、完整 prefix BVP pass 和闭面完成是不同事实；本 driver 只按原 actual/full-driver结果报告完整 BVP 是否接受。

这个入口仍是 v3 设计联解。接受之后固定所有 p*、释放 core/进行 v4 同一 g 精化，以及闭合、全角/全 t/reach/度量/握持量等任务由原后续接口承担；本组件不把它们核销。M112、tail112、224 shape、576 段是当前明确合同，不能改 M/T 后直接重标。

## 7. CLI 与资源

同原 live fullDN CLI，变更可执行文件与实际成功父结果：

```bash
python computations/geometry_20261114_noj_primal_live_full_dn.py \
  --accepted "$ACCEPTED96" --port "$ORIGINAL_PORT" \
  --warm "$ACTUAL_WARM" --warm-sha256 "$ACTUAL_WARM_SHA256" \
  --warm-status "$ACTUAL_STATUS" --warm-status-sha256 "$ACTUAL_STATUS_SHA256" \
  --tail-config "$ORIGINAL_CONFIG" --tail-source-root "$SOURCE_TOPIC/repro/source-root" \
  --anchor-result "$ACTUAL_SUCCESSFUL73/result.json" \
  --anchor-result-sha256 "$ACTUAL_SUCCESSFUL73_RESULT_SHA256" \
  --native-eta 1 --native-exact-workers 2 --native-max-factor-bytes 2147483648 \
  --node-heap 6144 --jac-workers 2 --max-nodes 1200 \
  --material-angles 4096 --physical-angles 4096 --outer-iterations 8 \
  --out "$VISIBLE_OUT/noj-primal-live-full-DN" --work "$RUNNER_TEMP/full-DN-work"
```

这里的变量均需由真实文件及原件 SHA 填入，不是现成的成功数据。默认前缀 max-nodes 1200 保留；未来同 g 的 699→1397 加密需要独立处理该资源参数，不能在本设计联解里悄悄声称已满足。

每个完整 correction 已识别的固定 binary 输出量为 704,387,088 B，另有可变 JSON、logs 与 prefix 工作文件。默认八 outer 对应保守协议调用数 `1 bootstrap + 1 当前 warm + 16 outer 请求 + 1 final audit = 19`；cache 可减少实际调用。全部原32轮保留时固定 binary 总额为 428,267,349,504 B。**单 call 的 32 GiB 预检不覆盖整场 fullDN。** driver 保实际资源读数与这个完整上界，不截迭代、不删现场、不为凑容量放宽任何数学门。最终 workflow 应依据实际已完成73成本与可用资源配置；若资源失败，则保完整已完成现场及真实失败范围，不冒跨进程 cache。

上述固定项已包含原 QR 的 `formed-cut-rho` 与 `formed-far-rho` 两个 112 项数组，共 1,792 B；此前未发布草稿遗漏了这一项。32 轮单请求固定量为 22,540,386,816 B。完整目录按现有布局每轮另有 1,750 个固定 binary 文件；这些数量不含可变 exact 行账、JSON、日志和 prefix 工作量。`--max-factor-bytes` 是完整因子与常数的文件预算，Node heap 参数也不是所有进程的总 RSS 上界。细分文件生命周期见 [资源账](2026-11-15-noJ-primal-live-resource-flow-and-retention.md)。

## 8. 静态检查与待真实执行的边界

本地只进行 Python AST、Node syntax、源码字符串精确往返与既有源的静态差异检查；不 import 科学模块、不运行 constructor/root/RHS/J/ODE/QR/native。

已检查原 core 唯一 correction 替换可逆、原 evaluate/十 trial 原字节相同、原 worker 插入可逆；新 installation 函数与冻结73的函数只差记录 schema。原实际响应绑定、FD、fullDN argv、同 client solve/load handoff 的 AST 保持；bootstrap实际求解方法及 literal row encoder 也与旧 live 源相同。

三份客户端/driver源码、完整相对旧 live 的 diff、`pure-source-roundtrip.json`、`unchanged-algorithm-source-check.json`、两份纯源码 checker 以及 `request-loop-source-check.mjs` 已在 `/tmp/noj-primal-live-multi/` 冻结。最后一个文件只含原 worker 源码经声明插入后的静态文本；没有运行其 constructor 或科学代码。两份 child 源独立冻结于 `/tmp/noj-primal-live-current576-source/`。由 root 普通 Git 保存这些成果，旧源不变。

尚未产生本多请求入口的 native/FD/fullDN结果。第73轮真实结果决定成功父输入是否存在，不能由本源码准备代替。
