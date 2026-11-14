# request17 原 cold-tail residual 的最小公开 Actions 重放接口

2026-11-14。**新增源码仅完成 AST / Node 语法核对，尚未执行；这里不报告新的数值或已接受尾。** 它针对 [本次实际极小非零 H 失败](2026-11-14-actual-tiny-H-native-tail-cold-start-failure.md)，不消费旧 A，不造新父场。

## 冻结入口

| 文件 | SHA256 |
|---|---|
| `computations/exact_20261114_tail_cold_residual_probe.py` | `5baf4b5505da6e124420253996630f6ebe6ecbc019f26938fa5747b147598515` |
| `computations/exact_20261114_tail_cold_residual_probe_hook.mjs` | `ad64dbc9ac33bcb51d693445649bf15164df7742587087a50dfe4ddb5dc117bd` |

在本公开仓库自己的 Actions、仓库根目录运行：

```bash
python "$C/exact_20261114_tail_cold_residual_probe.py" \
  --failed-directory "$FAILED/full-DN112" \
  --source-topic "$SOURCE_TOPIC" \
  --out "$OUT/cold-tail-residual" --node-heap 1536
```

`C` 是本课题 computations；`FAILED` 是 run43598917532、artifact14116526155 的原目录；`SOURCE_TOPIC` 使用现有公开源恢复树（含其 `repro/source-root`）；输出目录须为空。若沿用更大的真实 worker 堆预算，可显式给 `--node-heap 6144`，不改任何数学设置。

原失败目录中必须保留 `true-tail_0001.json.gz`、`true-tail_iteration.json.gz`、`true-tail_ready.json.gz`、`true-tail_intent.json`、`true-tail_capacity.json` 和 `true-tail_runtime-config.json`。前五件逐一锁本次实际 SHA，runtime 配置另由原 intent 的哈希锁定；不仅检查文件名。原完整 states/rawStates/rawNode/H、iteration0、非成功状态、原 request 和容量都核，不能放入其他失败或完成响应。

## 唯一执行的 stage pass

原 `TailClient` 的构造函数仍负责所有公开数值依赖 SHA、原 frozen calibration/profile、全部 config 和 ready/capacity。原 constructor 需要生成原 linear graphs/ready 和零切口基准；这不是重跑已完成的零高度 shooting/J/audit。独立 Node preload 只在原 frozen worker 文件 SHA 完全匹配时，把其请求循环换为一次受哈希验证的诊断协议；原 constructor、`initial`、`evaluate`、RK、root、分支门和所有数值模块均不改。

Python 在核完本次原 ready 语义、每个实际数学参数、Node/capacity 和全部已消费源之后，才发诊断许可。其唯一 stage pass 是：

```javascript
dn.tail.evaluate(savedStates, originalTarget, false, originalScales)
```

`originalTarget` 按原源码取完整 H 除以 `rCut**4`；`originalScales` 完全使用原 `scaleFor` 规则，即 `1e-250` floor 和首模 gains 的递推。传入的是原保存的失败 states，而不是重建初猜的替代数组。另调用原 `dn.tail.initial(target)` 只作逐项身份比较；保存全部非零差异，另计 JSON 无法保留的 signed-zero 差别。

原 `graphs[depth]` 也进入 far Robin 边界和原 correction，`gains[n][0]` 进入 residual scales。因此本诊断**不改** `linearSteps`、graphs、gains、深端边界或 scales。保留全部 `M112/N2048`、`RK12`、`physicalDepth8`、原 576 个 stage 及全部 112 项实际非零 H，不删模、不阈值化。

不调用 `TailClient.solve`、`dn.solve`、Newton correction、完整 variational J 或零锚 solve。源码同时保存原/替换后 worker 的代码身份以及被替换请求循环的哈希，不能把诊断 instrumentation 冒作原未改执行路径。

## 输出及解释

保留原 constructor 的 intent/ready/runtime/capacity/stderr，以及新的 `replay-spec.json`、`verified-launch-intent.json`、`instrumentation.json`、`launcher-result.json` 和 `summary.json`。完整压缩证据包括：

- 全部原 graphs、gains 和每个节点的原 scales；
- 原失败 states 与原 cold initial 的逐项比较、全部非零差异和节点量级；
- 每个 stage、每个 Q/Pi 分量的有符号 residual、绝对值及除以原 scale 后的值，原 `rawCell/rawSegment` 标签；
- 全部深端 Robin 和切口高度条件的 residual；
- 真正的最大 residual 所在 stage/模式/块，且逐分量表须严格重构这次无 J `evaluate` 自己的 scalar norm。

原失败记录的 norm 来自 with-J pass；新的无 J pass 用原独立 RK 分支，其浮点运算轨迹不先假定完全一致。报告保留两者差，不能把预期吻合写成结果。若原无 J pass 自身失败，则保原错误和 stage 定位、已有冷初猜比较和完整 graphs/gains；不编造剩余 residual 表，也不把未返回的 minA/minD 填成已验证下界。

`evaluation_completed=true` 仅表示此诊断完整返回。它不产生非零完成 anchor、实际 J、几何 audit 或新的尾接受；不预设 RK 误差、冷启动图、非线性或浮点噪声中的哪项是最终原因。只有实际回执才能决定下一次最小修正。
