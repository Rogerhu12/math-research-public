# 公开 request22：工厂完成，首次实际深侧传播下溢仍在原生检查之前

[run 43604874829](https://github.com/Rogerhu12/math-research-public/actions/runs/43604874829)，固定源 `fb32e240ba4bb4dee5c07cd5e78cb92a56c57d65`，zerorkprobev2 job `132477286262`。本条只读其真实 artifact `14118131680`；ZIP 为 11,017,527 字节，SHA256 `f885ff4fde0458a30ac86671f78905d0c616974b43da016c3212dcb07435c0e8`。数值步骤失败发生在私有初猜预测，和本轮另一个发布步骤的失败分开记录。

## 1. 原先 determinant 分支获得真实值

[v2 接线](2026-11-14-zero-rk-native-probe-v2-interface.md)在 stage 12、第 93 模（零基 index92，频率186）实际记录：

$$
T=\begin{pmatrix}
45160816.08029442&0.0045217131900511555\\
-752083800798933400&-75302165.40042144
\end{pmatrix}.
$$

本次两个 binary64 乘积均为 `-3400707242096343`，相减为零；四项、乘积和 determinant 均有限。因此本次明确命中 **finite-rounded-zero**，并非非有限分支。两乘积本身非零。逐 RK 子步的尺度化消去指标从 `2.1865673341262448e-4` 降到倒数第二步的 `4.9729398238078094e-15`，末步为零。这是本次浮点观测，不是精确流奇异或矩阵不可逆的证明，也不回填 v1 当时没有保留的位模式。

v2 工厂随后完整完成 576 个 stage、6943 个 RK 子步和 20829 次 geometry 查询，产生全部 576 行私有图。有限 rounded determinant 为零共 41 处；最小实际 $|u|$ 为 `9.623769292033124e-5`，最大块元素绝对值约 `1.0007950021979336e29`。这些量证明本次构造没有触发非有限或零分母拒绝，不证明块或图具有足够数值精度。

## 2. 新的实际失败：node261 到262、第112模

末个事件 `sequence=1426` 为：

```text
kind: prediction-height-rejected
source_node: 261
target_node: 262
mode: 112
Q: -5e-324
denominator: 275.8821411118115
next_Q: 0
nonzero_underflow: true
```

对应 rawCell3、rawSegment3、portRatio1，profile 没有内部 cusp。这里 $Q$ 是最小负 binary64 subnormal；除以一个大于2的正数后，精确商非零但 binary64 结果舍入到零。原 JSON 的 `next_Q=0` 不保符号零位；不能据 JSON 冒称已保存该位模式。

因此现在确实观察到了预测传播下溢，且它属于新增初猜器的保护分支。原 native `initial`/`solve` 没有“每个内部模必须保持非零”的接受门。完整 H/cut 输入没有被阈值化，所需后继是单独说明和保全这个有限表示的舍入行为，不能改原问题或删掉第112模。

## 3. 本次完成与尚未发生的部分

`factory_constructed=true`，但 `candidate_constructed=false`、`evaluate_calls=0`、原 native solve calls 为零。已经保留全部 blocks/图、节点0至260的完整预测状态和失败操作数；完整577节点候选尚未生成。没有新线性 norm、原 native 非线性 norm、J 或审计结果。request19 的 `13414069.968482966` 仍只是冷初猜基线。

全部 46 件 construction 分块的 SHA、行数及1427个连续事件序号已核对。事件含576个 stage-blocks、12个指定 RK trace、1个原 far graph、576个 candidate-graph-row、261个 completed-prediction-node 和1个真实失败。结束后原 methods/graphs/gains/far/layout 的身份仍为 unchanged。

后继独立 v3 只处理已观察到的私有预测乘除下溢：保真实操作数、结果位模式、符号零、节点/模态及原 scale 的 binary64 身份，使精确局部舍入损失可重建；不将极小浮点数当作完整误差界。原完整 H、原入口转换、全模式、所有非有限/零分母拒绝和 native 边界/缩放/域/容差保持。只有完整候选生成后，才运行一次原无 J 残差检查；不自动 Newton，也不预设它能通过。

原件 SHA256：

- `summary.json`：`4d09183f4afd7838d80ad707042e52bd2212d8ae846ad15ce2c25a1754634ea7`。
- `candidate-factory-identity.json`：`fa1eb084321af8dc60b83f28d8ebd80b564c40d21f2a285d5b13111aafe5f015`。
- `launcher-result.json`：`e19cdc494ed6c36fca02340c06fcf551dbc055ff22dd1400fa3ba8185159d78d`。

本地仅解包、读取和核对已产生的记录，没有重算工厂、预测或原生尾。
