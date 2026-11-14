# 同 RK12 候选 v3：保真实内部下溢与精确局部损失身份，原生门不变

本接口仅处理[公开 request22 已实际观察到的预测下溢](2026-11-14-public-same-RK-candidate-v2-actual22.md)。v2 工厂已完成，失败是节点261至262、第112模的有限 binary64 除法把非零精确商舍入为零；原 native `initial`/`solve` 并没有内部每个模都必须非零的门。完整原方程与舍入误差账的区别见 [R264](../results/R264-native-underflow-seed-contract-and-rounding-ledger.md)。

## 唯一数值构造变化

v3 保留 v2 的全部块、determinant 和私有图记录。只把私有预测中以下两个新增 veto 改为保留实际浮点结果并记录：

- 有限非零 $g,Q$ 的实际乘积舍入为符号零；
- 有限非零 $Q,u$ 的实际商舍入为符号零。

这些操作仍执行原先的 binary64 乘法或除法，没有另设阈值，没有置零命令，没有截频或删除数组列。已是零的分量继续正常传播，不算作新的下溢事件。所有577节点仍保224个分量，完整112个输入 $H$ 保持。

物理 $H/r^4$ 入口转换的非零下溢拒绝不动；原入口 $Q_0=H/r^4$ 仍被原式恢复。任何非有限结果、零 chart 分母、原 native far Robin、graphs/gains/scales、RK、branch guards、solve/J/audit 和容差都不变。v1/v2 源和历史原件保持独立冻结身份。

## 三个新源

| 文件 | SHA256 |
| --- | --- |
| `geometry_20261114_zero_rk_stage_initializer_v3.mjs` | `8c86a77b7f27228901c2f5f41fa22cb8fbc16feceec3f38896a495365bef5dc9` |
| `geometry_20261114_zero_rk_native_probe_v3.py` | `e7cff12390e943615f4f2624c5c52644b9f40a46d588ec7ae8bc35dbb542641a` |
| `geometry_20261114_zero_rk_native_probe_v3_hook.mjs` | `0c18213bc39568de35f1ff80c86d1f7f902f02073da4e1073daeab613df9151d` |

initializer 仍导出 `createZeroRKStageInitializer`。v3 的 `options.originalResidualScales` 必须由调用者提供原 `scaleFor` 数组；本探针传入稍后原 `evaluate` 使用的同一数组，并在 `predict` 内用未经改动的 target 和原 gains 逐 binary64 复核。它只用于身份和误差记录，不进入候选预测公式。

## 每次实际下溢的完整记录

事件记录 operation、源/目标节点、模号和频率、实际两个操作数、实际舍入结果、各数的8字节 little-endian binary64 十六进制、`negative_zero` 标记及累计乘/除计数。高度从节点 $n$ 到 $n+1$ 的事件同时保原 scale[$n$] 和 scale[$n+1$]：该 stage 的原残差使用源侧 scale[$n$]，不能误用目标尺度声称通过。

每个有限 binary64 位模式唯一确定一个精确有理数。因此记录可精确重建

$$
\eta=\operatorname{exact}(\text{stored result})-
\bigl(\operatorname{exact}(\text{left})\mathbin{\mathrm{op}}
\operatorname{exact}(\text{right})\bigr).
$$

记录中保存的是完整 operands/result bits 和这个表达式，不在 Number 中重新计算已经不可表示的损失，也不会把 $2^{-1075}$ 写成数值零冒充误差界。JSON 的数值零列即使不保符号，bit 字段及 `negative_zero` 仍保真实符号位。全部候选状态另有逐节点 `negative_zero_columns`，恢复后可核整个 binary64 SHA。

这只给出了真实触发下溢操作的局部损失身份，不是全部图舍入、全部预测误差或原非线性残差的上界。普通非零舍入误差、图关系缺陷及传播因子仍须按 R264 的完整账区分；不能因为某次局部损失很小就跳过原 residual scales 或原生检查。

## 固定真实输入与 CLI

v3 继续锁定 request17 原非零 H、request19 的原无 J 冷基线、request21 原工厂失败，并新增 request22 summary SHA `4d09183f4afd7838d80ad707042e52bd2212d8ae846ad15ce2c25a1754634ea7`。启动时还按 summary 清单校验末 construction packet 的 SHA，并核 sequence1426 的真实有限非零到零操作。没有新造 fixture 或零解重算。

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_zero_rk_native_probe_v3.py" \
  --failed-directory "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --first-candidate-summary "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43603818345-1-zerorkprobe/same-RK-candidate-native-probe/summary.json" \
  --v2-candidate-summary "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43604874829-1-zerorkprobev2/same-RK-candidate-native-probe-v2/summary.json" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --out "$VISIBLE_OUT/same-RK-candidate-native-probe-v3" \
  --node-heap 1536
```

原 worker 的构造/ready/capacity、源身份和物理配置仍逐项核对，只替换请求循环。完整候选构造后才运行一次原 `evaluate(candidate,H/r^4,false,originalScales)`。原线性块残差和非线性残差分别完整留存，所有数据按小于5 MB的文件分块。没有自动 Newton，也不会把 probe 的 exit0、较小 norm 或完整候选误标为新接受尾。

优先读取 `summary.actual_underflow_evidence`，其中包括真实事件计数、第一例和原 request22 那次操作在本次的完整 bit 记录；全部事件继续在 `initializer_construction_evidence.artifacts`。再检查 `candidate_constructed`、`evaluate_calls`、原无 J 返回状态及实际 norm。若另有失败，只按该真实记录继续处理。

交付时仅完成源码、Python AST、Node 及 hook 生成文本的语法检查；没有执行本地工厂、预测、尾或 BVP。数值结果尚待本公开仓库 Actions，不预设 v3 能完成或通过。
