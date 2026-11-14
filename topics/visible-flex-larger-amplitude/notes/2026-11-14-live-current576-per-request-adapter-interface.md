# 同一 live client 内逐请求 current576 snapshot 与 R273 子程序

分类：完整原方程的独立接线；数学算法沿用 R273。  
作者：ChatGPT / exact_refinement。  
日期：2026-11-14 UTC。

## 1. 两个新源

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `computations/exact_20261114_live_current576_damped_system.py` | 28963 | `9346c0a7e7c7f562d20b02126b82c8819c687a7575aea38258e9796cabb8db4a` |
| `computations/exact_20261114_live_current576_damped_chain_qr.py` | 21688 | `ee174e8283f3b5454a8b3dbe751dbd4f41f4f0dba1bd9d240b627bd2748f889f` |

前者公开 `LiveCurrent576System(snapshot_directory, expected_result_sha256, B=None)` 和 `LiveCurrent576ExactContext(system, kernel)`；后者是同步子程序。它们沿用第 61 轮 `695c2a56…` / `ac04842b…` 的全部科学路径，仅把固定 call1/旧 H/selected59 身份改为本次真实 protocol call 的身份。

完整 factor 仍直接调用 `exact_20261114_native_damped_chain_qr.py` 的 `9b951f95…` 类，精确行核仍是 `0bc8f978…`。没有改动这两个源；也没有改第 61 轮四个冻结源。

本次只进行了 AST 解析和源码结构核对。八个阵读取方法 `_json/_verify_array/raw/all/stages/stage_bytes/stage_raw/export_inputs` 的 AST 与第 61 轮原方法完全相同；精确核 dispatch、完整 exact-readback 和 checkpoint 的 AST 除声明的类名/schema 字符串外相同。没有 import 或执行科学模块，没有新数值结果。

## 2. 原 completed61 只作为明确的 literal 初猜

live client 由 `geometry_20261114_current576_live_tail_client.py` 和对应 hook 拥有；它在启动时验证实际 completed61 result/response。新 snapshot context 的 `parent_anchor` schema 为 `completed-native61-literal-JSON-anchor-v1`，包含真实 result/response 收据、原 61 producer/hook SHA、完整 J/audit 已返回的原验收字段，以及两个新导出的 literal seed 文件收据。

`source_state_encoding` 必须为 `original-response-JSON-decoded-binary64-v1`，`pre_JSON_negative_zero_preservation_claimed=false`。原 JSON 协议可能已丢失序列化前的负零；新实现只把实际收到的 JSON 数值解码为 binary64，明确保存该 literal state 的 raw 文件与负零 sidecar，不声称恢复了不可见的旧内存位。

没有预填未来 result、response、checkpoint 或状态 SHA。它们由真实父文件给出，必须是完整合法 SHA；父的原 source SHA 固定为 `06b8c44c…` / `0933ee81…`。子程序不反复加载父大文件，只核启动 producer 已绑定的完整收据及本轮 snapshot 来源。

只有 `native_call=1` 且原 `nonlinear_iteration=0` 时，当前 state SHA 必须等于 `literal_seed_state_float64le_sha256`。只在 call1 要求请求 H 等于实际 anchor H。以后每个请求按原 live worker 的 predictor/fallback 和其真正 H 运行，不重置为 parent state，也不把后来 H 截成旧值或零。

## 3. 本次 protocol request 的完整身份

`native_call` 必须为正整数；it 和 snapshot sequence 在每个 call 内各从 0 顺序开始。目录为 `call-0001/iteration-000/snapshot` 与独立的同轮 `qr`。

snapshot 的三 schema 是：

- `live-current-native576-withJ-snapshot-result-v1`
- `live-current-native576-withJ-snapshot-context-v1`
- `live-current-native576-withJ-snapshot-arrays-v1`

每轮仍保全部十个原数组和原尺寸：577×224 states，576×224 residuals/out，576×224×224 J，577 sigma，以及各112个 cut、far、far graph、physical H、target。原 nine-node `rawNode` 和576个 cells、原 sources/config/graphs/gains 身份全保。新的 snapshot 不改变原 flow、J 或 mean 运算。

context 增加 `current_request`，schema 为 `live-current576-native-request-context-v1`，包含：

- 实际 `native_call` 与原 `request={height,jacobian,audit}`；height 恰112项，flags 保原 boolean。
- `request_height_float64le_sha256` 与原请求真实 `height_negative_zero_columns`。子程序用该 sidecar 复原 request JSON 的112个 f64 words，并逐字核 snapshot 的 physical-height；不会因 JSON 的负零表示丢失而误归成新数值。
- `bootstrap_request`、`seed_assigned` 仅 call1 为 true；以后原 predictor/fallback 保留。
- snapshot 目录内逐字复制的 `request.json` 收据。其完整 JSON body 必须等于 context 的 current_request 去掉 `request_file` 后的字典。

新 adapter 不使用旧 anchor 的 sigma 或 target。每个 call 的真实 sigma/target/current H 都从本次原 evaluate snapshot 读取；far graph 与原 geometry 身份保持本次 immutable config。实际 cut 和 far 残差允许非零。

## 4. CLI 与输出合同

```bash
python exact_20261114_live_current576_damped_chain_qr.py \
  --snapshot-directory "$CALL/iteration-000/snapshot" \
  --snapshot-result-sha256 "$ACTUAL_SNAPSHOT_RESULT_SHA256" \
  --eta 1 --exact-workers 2 --max-factor-bytes 2147483648 \
  --out "$CALL/iteration-000/qr"
```

只允许在本公开仓库 Actions 执行。桥使用 `spawnSync`、独立 per-call/per-iteration 目录、独立 stdout/stderr 文件；不能把子程序输出写到 worker 的 JSON 协议 stdout。这里没有改变原 maxNewton、十个 no-J trial、严格原 infinity-norm decrease、原 tolerance、最终 endpoint J 或 fresh audit。

四个新输出 schema 是：

| 对象 | schema |
|---|---|
| result | `complete-native-live-current576-damped-square-root-direction-v1` |
| input binding | `live-current-native576-complete-linear-system-binding-v1` |
| 完整 direction checkpoint | `complete-native-live-current576-damped-direction-v1` |
| array manifest | `complete-native-live-current576-damped-direction-arrays-v1` |

原 `native_delta/native_direction_checkpoint/input_binding/array_manifest` 等 descriptor 字段和完整577方向仍保留。binding 明确含 `parent_anchor/current_request` 两字典、真实 snapshot result/context/manifest SHA、current state SHA、raw-array SHA、call/it/sequence、request H SHA。matrix identity definition 也包含本次 request/call，不把另一 call 的来源改标签复用。

所有 exact 最大值和最坏 witness 都另带实际 call、request H SHA；完整129248行仍由原未缩放 J/r/方向形成，再按原 sigma 精确读回。原577个 node penalty 和全部纯常数因子不变。子程序不把 exact 线性缺陷、L2 模型或梯度作为原 nonlinear trial 新门。

## 5. 数学、审计与资源范围

R273 的完整模型、行权重、列坐标、QR 消元与常数保留见 [R273](../results/R273-complete-native-damped-square-root-chain.md)。新文件没有重新实现 factor 或另加 ridge、截秩、normal matrix、Riccati inverse。

每个实际 correction 仍有约704385296 B主要固定 raw snapshot/子程序/factor payload，另有真实 ledger、checkpoint 和日志。该成本按实际 correction 次数累计；多个 protocol call 不能沿单 call 的32轮估算总量。原 live client 的 cache/predictor 和 bootstrap 后的实际请求行为由独立 wrapper 保留；cache 命中时没有新的 protocol call，也不伪造一个 snapshot。

这里没有完成新的 tail solve，也没有宣称任意后继 H 已接受。最终是否接受，仍由真实原 worker 在同一 live 对象中执行原流程得出；已经保存的 completed61 只提供严格标注的 literal 初猜和来源。
