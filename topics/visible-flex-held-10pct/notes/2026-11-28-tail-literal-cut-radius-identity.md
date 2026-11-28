# 当前 D/E 同背景的外端半径：字面 c−Rc 精确为0

本条只读已有 D/E 同背景 profile、已保存 native metadata/input 与真实背景常数，
没有新 native 计算或尾几何导出。记录见
[`2026-11-28-tail-literal-cut-radius-identity.json`](2026-11-28-tail-literal-cut-radius-identity.json)，
SHA256 `9f49b53b5389ee5360c8dba5c83230b6613c12753022d1b9dce1560387242d20`。

以下字面 binary64 值逐项相同，均为 `0.3`：

- E 的 `predictor/original-tangent-scales.json` 中 `radius`，由原 constructor 的
  `dn.tail.cells[0].profiles.at(-1)(1).r` 实际给出。
- D 真接受 f=.5 packet 中 `response.jets.radius` 与
  `response.checkpoint.parameters.rCut`。
- D、E 原 `static-metadata.json.gz` 中 `physicalParameters.rCut`。
- 已重建并绑定 R58 的真实背景 constants 中 `parameters.rCut`。

每个值作为字面 binary real 都等于

\[
c=R_c=\frac{5404319552844595}{18014398509481984},\qquad c-R_c=0.
\]

这不是把显示相同的小数当作相等，而是对记录中的浮点字面值取精确有理数。
D0003与E0014原 native stage0 的末点均为 `profile=0,x=1`，其保存的 frozen
`r³=0.026999999999999996`、`r⁴=0.0081` 又分别逐位等于该字面半径的三、四次幂；
这是辅助交叉核验，不是以四次幂反解一个未记录的半径。

原 `general_root_tail_momentum.geometry` 保留 `profile(x).r` 原值；v2共享R导出的
`sample.radiusJS` 取同一 `a.g.r`，没有再取根、取区间中点或钳制到物理切口。
所有相关源、实际包、metadata、input 和精确来源 key 都已绑定在 JSON。

**当前完整 full-H geometry bundle 尚未返回。** 当它实际生成后，仍必须核它的
外端 literal c 与本条背景 Rc 相同，不能仅凭预检代替实际 bundle 身份。若复核成立，
nearcut 定义

\[
r(R)=R+(c-R_c)S\!\left(\frac{R-(R_c-d)}d\right)
\]

在整条带上就是准确的恒等式，且 `r′=1,r″=0`，无需支付非零重参数化扰动的数值
代价。这不替代完整尾场、各段/深盘连续 metric 与几何证书。R75 非零差转移界仍
保留给真正有非零 c−Rc 的将来输入；本条没有改变其域假设，也没有提前接受新场。
