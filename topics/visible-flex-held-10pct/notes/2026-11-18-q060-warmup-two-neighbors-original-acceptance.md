# q060：旧高度尾部的两个具名邻数及原生接受

本条接续 `2026-11-18-q060-warmup-resource-candidate-tied-peak.md`。
同一份新 `H_old` 的 parts16 失败态，经一次预先具名的两标量替换，
由未改动的原 worker 在原 `2e-9` 门槛下真实接受。
这是原生尾部有限离散结论；尚未得到新的前缀联立终态或全闭曲面证书。

## 1. 只读局部检查与唯一候选

完整原失败输入为
`closed_work/q060-coupled-parts16-v1/seed_tail_0001.json.gz`，
SHA-256 `adf477252c1dc707ce4fe8975aa9c911aca2f9d4c5113ba300d11b82023c4535`。
此前资源补完已经保存完整残差重放和未受节点 86 影响的最大残差；
本条复用那些记录，没有重新做全域定位，也没有追加 alpha/beta 搜索。

`inspect_named_tail_row.mjs` 仅在原 full-Jacobian flow 上检查行 85、86
的两个具名分量。行 86 的分量 8（物理模 3）和 11（物理模 12）均为
`flow − state = -1.1368683772161603e-13`，并且 flow 恰好是 state
朝负方向的下一个 binary64 数。二者的归一残差同为
`3.671459625080514e-9`，故只改第一个分量会留下另一个同高峰。

唯一候选是下表两项，索引均从 0 开始：

| 节点 | 分量 | 原值 | 新值 |
|---|---|---|---|
| 86 | 8 | `-956.9067795430643` | `-956.9067795430644` |
| 86 | 11 | `588.2616784608559` | `588.2616784608558` |

`propose_tail_two_named_neighbors.mjs` 硬锁原失败输入、已有 baseline
和局部检查的 SHA-256，硬锁上述两个坐标；分别检查定向邻数与原 flow
完全相同，并逐标量核对没有第三项变化。完整高度、物理参数、rawNode、
原网格和两端状态均保持不变。该脚本没有调用 `dn.solve`。

原残差行满足

$$
R_i=\Phi_i(X_{i+1})-X_i.
$$

只改变节点 86 的任意分量，影响行恰为 85、86。原 flow 的动量输出与
切向矩阵均除以原 `portRatio`，归一尺度仍由原 `gains` 构造。
两行重新求值后分别得到
`6.117678421052487e-10`、`1.835729812540257e-9`；
行 86 的新最大分量为 9，两个被替换分量的残差均为零。
已有 baseline 中未动部分（包括边界）的最大值为
`1.8199376260757712e-9`。随后仅对这个唯一候选做一次完整原
full-Jacobian 残差重放，结果与两行依赖预测逐位相同：

$$
\|R\|_{\mathrm{original}}
=1.835729812540257\times10^{-9}<2\times10^{-9}.
$$

完整候选仍明确标记 `candidate_only=true, solver_success=false`。
其 SHA-256 为
`4ca8d5b6d1328b8e386caf4e891b371e71c0df904b6ace7b21ab918a771c7b84`。

## 2. 双项加载器与首个接口错误

独立入口 `solve_original_tail_two_named_neighbors.py` 只允许
`[(86,8),(86,11)]`，用 Python `math.nextafter(value,-inf)` 独立核查
两项，拒绝其他坐标变化。它保留原输入、完整 H、配置和来源核对，
仅通过原 `initialCheckpoint` 接口加载候选。

第一次入口在构造 worker 之前终止：新增校验把原响应中的 `failed`
误当成布尔 `true`，而原 worker 实际保存的是非空错误字符串。
会话 7701 的真实退出码为 1，未构造 worker、未发送 DN 请求。
这属于接口 schema 错误，不是第二次数学求解失败。首源和日志保留。

独立 `solve_original_tail_two_named_neighbors_v2.py` 只改该 admission
校验：核对已经由完整文件哈希锁定的原错误字符串和 `lastIteration.norm`。
双项 allowlist、负邻数核对、全部物理身份和原门保持不变。
未执行过的通用多项加载器原型不用于本条；实际入口始终只允许这两个坐标。

原 ready 的 `parameters` 包含配置中的输入/trace 元数据。
复用已审的 v2 映射：先分别核对新旧 ready 中 IO 字段与各自配置完全对应，
再要求所有非 IO 参数逐项相同。本次仅 `initialCheckpoint` 和
`traceFile` 改变。原 reload 算术核查得到第一高度比例严格为 1、
`H/r^4-state[0]` 逐项为正零；same-parts 加载因此保持候选节点。

## 3. 原 worker 的实际接受

会话 51467 由 observer 记录真实退出码 0。原 worker 收到同一完整
`H_old`，要求 `jacobian=true,audit=true`；M8、N128、depth8、
parts16、RK16、原 `2e-9` 门和原 native sources 均不变。
它在迭代 0 返回 `converged=true`，归一残差仍为
`1.835729812540257e-9`，同时返回 208 个有限高度到二阶 jet 的 Jacobian
标量以及原 audit。1153 个完整状态节点与候选逐位相同。

原生记录为
`closed_work/q060-warmup-two-neighbors-native-v2/seed_tail_0001.json.gz`，
SHA-256 `c57fe4ea23e90de71502666a40d5b0ccaa12c18f788e62e003ba5e2393e5f249`。
原有限 audit 中 `actualMetric=3.9926804085155254e-8`，
`fullD=2.822015101564466e-4`，`minLeading=0.529333104523161`。
这些是原离散 audit 的输出，不解释为连续全尾或全闭面的新严格界。

这次接受属于当前 prefix 初猜的 `H_old`。此前另有已登记的
`H_new` 原生接受，二者完整高度不同，不能互借响应。
后续原前缀流程可用本条真实尾状态作 initializer；每个实际新 H
仍须由原 worker 单独验收，原 raw inner cubic 与其 DN 锚会先落盘。

## 4. 来源与保存范围

紧凑执行记录为
`scripts/resume_transfer/q060_warmup_two_neighbors_native_execution.json`。
它保存完整物理高度、命令、source/runtime hashes、原始日志与输出的
路径/哈希、两个具名变化、局部与完整残差和真实 native 响应身份。
完整状态、Jacobian 数组、可再生逐场输出仅在 scratch 保存，不提交。
本条不修改已登记的候选家族，也不把候选重放代替原生接受。
