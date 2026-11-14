# 原首次 native correction 的完整二进制捕获接口

2026-11-14。此入口仅绑定 [actual25 的真实失败](2026-11-14-public-native-seeded-full-actual25.md) 及其 [actual23 完整初猜](2026-11-14-public-same-RK-candidate-v3-actual23.md)。它重做一次原 `evaluate(...,true,...)` 与原 `correction`，保全原线性系统和原方向，然后在第一个 trial 前有意停止。**它不求一个新 H，不修改原校正算法，也不构成 native/J/audit 接受。当前只有源码完成，尚无本入口的 Actions 数值回执。**

## 1. 独立文件与冻结身份

| 文件 | 字节数 | SHA256 |
| --- | ---: | --- |
| `computations/geometry_20261114_native_correction_capture.py` | 16,326 | `0b49f14218e4d62f0b18d77dd3fa8aee1cb6225f84d92bb81dace173cf74dcc0` |
| `computations/geometry_20261114_native_correction_capture_hook.mjs` | 45,141 | `b20aee4da9b9dd927a2d78c6691739508798c81e73501b31e14a43ad55b64d30` |

不修改 actual25 的 launcher/hook、v3 initializer/probe、原 TailClient、原 frozen worker、原 engine/core 或任何数学输入。新 Python 复用原 25 launcher 已冻结的纯身份验证函数，并逐字检查其 SHA `afa2588db686ba54b3e434e0ddf40503a74061ecd5fa389dbb41ced7a0b085c7`。

本地只完成 Python AST、Node 语法和纯源码字符串的插入/删除往返检查；没有执行 native、initializer、J、图矩阵计算或任何科学数值。三处 observer 从生成的 core 删去后，逐字恢复原 runtime core；生成后的 engine/core 均通过语法检查。全部数值必须由本公开仓库 Actions 执行。

## 2. CLI 与新增最小输入

CLI 保留 actual25 的所有参数名，新增 `--native-failure-directory`。示例在仓库根执行：

```bash
topic_path=topics/visible-flex-larger-amplitude
capture_out="$RUNNER_TEMP/native-correction-capture"
python "$topic_path/computations/geometry_20261114_native_correction_capture.py" \
  --failed-directory "$topic_path/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$topic_path/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --first-candidate-summary "$topic_path/notes/public-actions-43603818345-1-zerorkprobe/same-RK-candidate-native-probe/summary.json" \
  --v2-candidate-summary "$topic_path/notes/public-actions-43604874829-1-zerorkprobev2/same-RK-candidate-native-probe-v2/summary.json" \
  --candidate-directory "$topic_path/notes/public-actions-43605912092-1-zerorkprobev3/same-RK-candidate-native-probe-v3" \
  --native-failure-directory "$topic_path/notes/public-actions-43607404925-1-nativeseed/native-actual23-seeded-full" \
  --source-topic topics/visible-flexible-closed-surface \
  --node-heap 6144 \
  --out "$capture_out"
```

输出目录必须为空。原 17/19/21/22/23 输入集合与 actual25 相同，包括 actual22 最后 underflow event 包、actual23 完整 states/graphs/gains/scale chunks。新增 actual25 目录只需以下 10 件，每件已在 launcher 内硬锁真实 SHA：

1. `result.json`
2. `native_0001.json.gz`
3. `native_iteration.json.gz`
4. `native_trace.jsonl`
5. `native_trials.jsonl`
6. `seed-binding.json`
7. `instrumentation.json`
8. `seeded-solve-spec.json`
9. `verified-launch-intent.json`
10. `original-live-identity-before-seed.json`

actual25 的 `result.json` 必须是 SHA `f5f4acdb055c6964fd591ac2da566bc581607b1d32ebc8096af557f4a3f8abbf` 的原件，继续保持失败身份。验证保留其 10 条真实 stage 13 守卫拒绝记录；这里不把它们再跑一次。

## 3. 原运行与插入范围

启动仍使用原 `exact_20261114_true_tail_client.py`，仅在唯一原 worker 的 `Popen` 加载新 hook；无关 Git 子进程照常放行。原 constructor、ready、capacity、配置和所有源身份先逐项核对，再发送一条原完整请求。全部 112 个非零 H、577×224 初猜值、9,546 个负零、原 far Robin graph、原 gains/scaleFor 与 stage layout 都按 actual23/25 核验。没有高度阈值、截频、几何重映射、零幅比例预测、初猜再生成或 zero solve。

新 hook 仍在原唯一 `let initial,predicted=false;` 后赋入该完整 seed 并设置 `predicted=true`。随后通过冻结 `tail_resumable_engine.mjs` 的内存源码，在其已有身份检查之后、编译原 core 之前加入三个只读 observer：

- 原 `correction(ev,states,target)` 调用前：原首次 `evaluate(...,true,...)` 已返回，先写完整原 J、r、states、target、far 和 scales。
- 原 backward recurrence 的 `cache[n]={Gi,t};` 之后：记录本 stage 已算出的 G、Gi、gs、bs 等摘要，并保留最大条件数处的小矩阵快照。原矩阵运算表达式和顺序不改。
- 原 `correction` 返回后、原 history 更新及 trial 循环之前：写原完整 delta，计算并保全诊断缺陷，写 manifest，抛出唯一计划停止标识。

冻结原 engine SHA 为 `1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8`，原 core 文件 SHA 为 `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`。`engine-loader-instrumentation.json`、`core-instrumentation.json` 和 worker `instrumentation.json` 分别记录各层原源码、新加载源码、插入片段及精确往返身份。磁盘上的原源文件与原 ready manifest 保留；加载后的观察源码另行记录，不将其冒称完全未插入的运行体。

## 4. 原全线性系统、尺度与诊断含义

使用原 computed stage Jacobian $J_n$、原残差 $r_n$ 与原返回方向 $\delta_n$，逐行计算

$$
 e_n=(J_n\delta_{n+1}-\delta_n)+r_n.
$$

矩阵乘法调用原 `matrixVector`。cut 先按原求值次序保全 $r_c=y_{0,Q}-\mathrm{target}$，再算 $e_c=\delta_{0,Q}+r_c$；far 使用原保存的 `ev.end`，计算

$$
 e_D=(\delta_{D,\Pi}-G_D\delta_{D,Q})+r_D.
$$

分别除以原 $\sigma_n,\sigma_0,\sigma_D$，保留全部 stage/cut/far 行，而非仅一个范数或少数模式。全 J、r、delta、边界、scale 的原二进制也全部保留，便于独立重建实数意义下的 binary-array 线性系统。每行频率、stage/rawCell/rawSegment 和最大缺陷位置会写入小摘要。

上述普通浮点诊断本身不是精确 $DR$、区间证书或严格 Newton 收敛结论。`chartCondition` 只是原局部 Riccati 图表的报告，不能直接当整个边值线性系统的条件数。完整符号与误差区分见 [R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md)。此接口不改变 README 原门，也不额外要求严格机器证明才可继续原数值研究。

## 5. 大阵保全与发布分流

所有大数组统一放入 `--out/large-arrays/`，仅进 Actions artifact；publisher 必须将这个**整个目录**排除 Git。顶层小 manifest、摘要、身份文件及原 trace/checkpoint 继续保全。不要为压缩发布包而删原物理模式、shooting 节点或 J 行。

原完整 J 有 $576\times224\times224$ 个 Float64，占 **231,211,008 B**。按每 8 stages 一块写原始 Float64LE，单块 **3,211,264 B**。数据用原 typed-array 底层字节复制，保留负零及任何实际非有限值的位模式；JSON 摘要用分类与 hex 表示非有限数，不把它们悄悄变成零或 `null` 数值证据。`null` 仅用于摘要中不能用 JSON 数字表达的数值槽，同时必须带对应分类与 bits。

完整数组包括原 stage J/out/r、基态、H/target、scales/far、原 cut/far 残差、原 delta、诊断 J-delta 乘积，以及全部 raw/scaled stage/cut/far 线性缺陷。每个 stage 只留图递推摘要；仅最大条件数处另存完整 G、Gi、H、相邻 gs/bs 和 t/u 等小矩阵，不重复保存每个 stage 的全部 Riccati 矩阵。

每块都有 shape、次序、行区间、字节数和 SHA；每个数组另有串联原字节 SHA。`large-array-chunks.jsonl` 在每块成功落盘后即时追加，即使稍后进程意外终止也能定位已完成块。若原 correction 中途失败，初始全 J/r 已先写，已观察图摘要及最大处快照保留；不会虚造尚未返回的 delta。若发生强制 kill，最终 JSON 可能未写完，应按已有块账和进程实际错误登记部分结果。

## 6. 退出语义

计划停止消息固定为

```text
Error: VISIBLE_NATIVE_CORRECTION_CAPTURE_COMPLETE_V1
```

该消息由原 worker 的原 catch 返回，原客户端仍把它作为 `failed` 拒绝；新 launcher 只把这一个已绑定的消息识别为**诊断完成**。只有 `capture-summary.capture_completed=true`、该停止消息真实出现、一个原请求、worker 正常退出且原 trial 记录数为 0 时，launcher 才以 exit 0 表示捕获成功。

`result.native_accepted=false`、`task_completed=false` 始终保持。原请求为 `jacobian=true,audit=true` 以保持原协议身份，但计划停止发生在尾 Newton 的首校正之后，因此不会到最终切口 `heightJetJacobian` 或 fresh audit；不能把请求旗当成已经完成或通过。

其它原守卫、原矩阵异常、身份错误、输出失败或不完整 capture 均 exit 2，并保留实际消息和已有产物。原 far/gains/scales、所有 guard、原 tol、原 Newton/correction 表达式不变；本入口只为下一项有证据的稳定校正选择保存原系统，不预设其病态原因或任何替代算法成功。
