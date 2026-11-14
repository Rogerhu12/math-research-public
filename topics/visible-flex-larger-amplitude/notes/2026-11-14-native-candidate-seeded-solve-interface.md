# Actual23 完整候选进入原 native solve/J/audit：独立入口

日期：2026-11-14。对象仍是 request17 的全部 112 个非零物理高度系数、原 M112/N2048、RK12、576 个 shooting stage、原 finite tail 方程与全部原容差。

这是一次 **native-only 的新真实求解接线**。当前只有代码与已保存字节的接口核对；本 note 不报告新 solve、Jacobian、audit 已通过。初始化输入来自 [actual23 的真实完整 no-J 探针](2026-11-14-public-same-RK-candidate-v3-actual23.md)：原归一残差由 `13414069.968482966` 降到 `0.04177307820740199`，576 段原 flow guard 全过，仍高于原 `2e-9` 求解容差。

## 1. 新文件与唯一行为变化

| 独立源 | SHA256 |
| --- | --- |
| `computations/geometry_20261114_native_candidate_seeded_solve.py` | `afa2588db686ba54b3e434e0ddf40503a74061ecd5fa389dbb41ced7a0b085c7` |
| `computations/geometry_20261114_native_candidate_seeded_solve_hook.mjs` | `22fa88aaaf2385a34dc3a373138f1b7fec08c903fd7151717b1f3dfb4d707e8d` |

入口直接创建原 `exact_20261114_true_tail_client.py::TailClient`。新的 hook 在原 frozen worker 完成其既有源变换后，只在请求循环唯一的 `let initial,predicted=false;` 后插入一块首次请求代码：

1. 要求 `call===1`、原 `last===null`、原 `tangentPredictor===null`。
2. 从 actual23 的完整 candidate chunks 恢复所有 577×224 个数，包括侧表记录的 9,546 个负零；全数组以 Float64 little-endian 编码后核 SHA。
3. 将这些状态赋给原局部变量 `initial`，置 `predicted=true`，写一条原 trace 事件。
4. 继续执行原请求循环及原 `dn.solve`。插入的文本可逐字删除以恢复本次实际构造的原 compiled worker；这一事实与插入前后 SHA 写入 `instrumentation.json`。

不设置 `initialCheckpoint`，不把候选设成 `last`，不经过几何重映射、从零高度取比例的预测或额外边界修正。不会重新运行 v3 initializer、zero solve 或 no-J 探针。原循环在第一请求下不存在已有 tangent predictor；`predicted=true` 使原后续 amplitude fallback 与 boundary-correction 分支保持不进入。

唯一实际请求是原 API：

```python
client.solve(original_full_height, jacobian=True, audit=True)
```

`audit=True` 保证这次实际发送到新原 worker；没有导入旧响应缓存。原完整 solve、Newton、所有 trials、`retainIteration`、原 guard、完整 height-jet Jacobian、原 finite audit、原阈值与原客户端响应校验原样保留。原数值求解上限仍由已锁 config 提供，不能由新入口调整。

## 2. 字节、配置与历史绑定

actual23 的 `summary.json` 固定 SHA 为：

```text
aa93fb8afbd0c8ce3ec49859f3bcfae465696654f626ed1678ceb430329ec6ea
```

其完整候选的逐字节状态 SHA 为：

```text
6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8
```

其全部原物理 H、原 scaleFor 向量与原 far Robin graph 的 Float64 little-endian SHA 分别为：

```text
H      c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f
scales ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc
far    395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54
```

入口与 hook 重新核实际17/19/21/22/23的相同 H、配置、原数值源与来源链。仅可重定位 trace/iteration/trial 等 I/O 路径；`initialCheckpoint` 不属于可忽略项。旧 JSON 中的历史绝对路径原样保留，重定位文件由其原 SHA 与完整数学内容识别。

必须读取 actual23 下的十件原件：`summary.json`、`candidate-checkpoint.json`、`candidate-initializer-identity.json`、`candidate-factory-identity.json`、`original-live-identity.json`、`probe-spec.json`、`verified-launch-intent.json`、`instrumentation.json`、`candidate-states-000.json.gz`、`original-graphs-gains-000.json.gz`。chunk 的压缩 SHA、未压缩 SHA、字节数、行数与来源字段都检查；不重新生成任何状态或改写任何 H。

当前 live original constructor 的源目录、完整 ready/capacity 语义先由 Python 复核。真正注入时，hook 再比对原参数、raw-node 顺序、全部 graph/gain 的位模式、far graph、各 stage 的 rawCell/rawSegment/portRatio/mu/cusp 断点，以及原 initial/evaluate/tail.solve/dn.solve 函数的文本 SHA。原 scaleFor 仍是 `H/rCut^4` 的原起始尺度，逐段除以 `abs(original gains[n][0])`；candidate 的私有图或传递分母不进入归一化。

这些是使用同一个已探针初猜所必需的输入身份检查，不是新的科学验收条件。特别是，它们不把 actual23 的 no-J norm 当作原 solve/J/audit 已通过。

## 3. Actions CLI

`TOPIC` 是公开仓库本课题目录，`SOURCE_TOPIC` 是原 source-dependencies 已逐 SHA 恢复的 `visible-flexible-closed-surface` 源目录。大原件可按现有公开资产恢复方式先取到这些路径，不能换配置或拿其他 H 的 state。

```bash
python "$TOPIC/computations/geometry_20261114_native_candidate_seeded_solve.py" \
  --source-topic "$SOURCE_TOPIC" \
  --failed-directory "$TOPIC/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$TOPIC/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --first-candidate-summary "$TOPIC/notes/public-actions-43603818345-1-zerorkprobe/same-RK-candidate-native-probe/summary.json" \
  --v2-candidate-summary "$TOPIC/notes/public-actions-43604874829-1-zerorkprobev2/same-RK-candidate-native-probe-v2/summary.json" \
  --candidate-directory "$TOPIC/notes/public-actions-43605912092-1-zerorkprobev3/same-RK-candidate-native-probe-v3" \
  --node-heap 6144 \
  --out "$OUT/native-actual23-seeded-full"
```

`--out` 必须为空。只能在 `Rogerhu12/math-research-public` 的 GitHub Actions 运行。原 Node heap 的 6144 MB 是资源参数，未改变任何数值配置。

## 4. 成功与失败保全

原 response、iteration-recovery checkpoint、trial events、trace、stderr、runtime config、ready、capacity 与意向记录全部保留，前缀为 `native`。新增的 `seeded-solve-spec.json`、`verified-launch-intent.json`、`instrumentation.json`、`seed-binding.json` 和 `original-live-identity-before-seed.json` 描述插入来源与实际字节；若注入验证失败，则写 `seed-binding-failure.json` 并让原 worker 失败路径记录该错误。

最后 `result.json` 记录原客户端完整响应校验结果、原 worker 退出码、实际调用次数、真实响应 SHA、是否真的返回完整 J/audit、原 `failed`/最近 iteration 与实际 seed trace。退出码仅在原完整 API 校验通过、worker 正常结束且首次注入记录唯一时为 0；其余为 2。

原 native 的求解后 cutJets/J/audit 如果抛错，即使最近 iteration 的 norm 已低于容差，仍是失败。不能把这种 checkpoint 冒充完整已解响应。本入口也不声称全 prefix、同 g 精化、闭面、reach、Hausdorff 幅度或整个课题已完成。

## 5. 已做的本地范围

只对保存的 metadata/压缩原件做 SHA、行列数、精确浮点数相等与 signed-zero 恢复核验；真实恢复得到全部 577×224 状态和 9,546 个负零。Python AST、Node 源及生成的 outer-loader/唯一插入块/原 loop 合成文本均仅作语法检查。没有本地调用 native constructor、initializer、ODE、evaluate、solver、Jacobian 或 audit。新完整求解的事实以之后公开 Actions 回执为准。
