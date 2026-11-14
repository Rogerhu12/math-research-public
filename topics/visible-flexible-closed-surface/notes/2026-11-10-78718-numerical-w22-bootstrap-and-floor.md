# W22 bootstrap、几何缩幅与 projectionFloor 的范围

会话：Astra-visible-flex-78718bd0；作者：`/root/numerical_recovery`；2026-11-10。

## 实际失败与下一入口

根持有各主工具会话；以下自然出口/主动停止均引用根的真实工具回执，不从日志或 guard 推断。

| 运行 | 已发生事实 | 限定结论 |
|---|---|---|
| 旧 M15/W15 61908 | 根 `f5f4cc` 主动停止，exit 130；已有第一 inner 5345 节点，但未保存其 PP | 调度停止，不判数学失败；不能恢复其内存曲线 |
| fast-01 | 根 `22838b` 自然 exit 2，约 0.11 秒；config 省略默认 projectionFloor，adapter 错用下标读取 | 改回原 `.get(...,.05)`；没有改变实际 floor |
| fast-02，原 H bootstrap | 根 `e4eb09` 自然 exit 2，560.54 秒；M22/N512 首实际请求在 shooting iteration 2 失败 | 一笔真 DN 失败，0 inner；不证明此 H 无解 |
| fast-03，H/2 bootstrap | 根 `a5f53a` 自然 exit 2，14.35 秒；第一 evaluate 的 momentum root line search 失败，lastIteration=null | 一笔真 DN 已请求，尚无完成的 shooting iteration，0 inner；不能写成“没有调用 DN” |
| fast-04，H/2 + raw 几何缩幅 | 根 `3787e9` 实际启动/session83728，根独占观察 | 本笔记未取得自然出口或数学成功 |

本代理只读 `d1e8f7` 复核了 fast-02 的完整失败包：390,917 B，SHA `880b8fd48470ec81e87ab8dad8cc739fe10851f8ec17ce5c797ce138db85d823`，865 个恢复态；request 为 jacobian=true/audit=false。最后 norm=498.7556050275603、minA=0.0545786382637322、minD=0.9916325652237515。它们是失败状态，不是新收敛尾或 metric 上界。

该 iteration 的十个 trial 中，步长 1、1/2、1/4 在 stage32、32、33 被 D/S/A 正性域拒绝；1/8 至 1/512 在 stage34/37 是 momentum root 的 line search 失败。全部位于 physical cell0 / raw segment4。不能仅凭聚合的 shooting line-search 错误，把后七项都说成已证明 A≤.05。

## H/2 入口没有更改最终目标

`--bootstrap-height-scale 0.5` 只把 Coordinator 的首次**实际**求解目标设为原 warm seed 高度向量的一半。旧 seed packet 及其 converged/高度标签保持原样，仍只提供 warm 状态。policy 和 journal 保存原高度摘要、首次实际请求摘要、scale 以及 `external_goal_unchanged=true`。

原 Coordinator 在首目标不同于外部目标时，以 jacobian=false/audit=false 真求首目标；只有成功才进入原 1/8、最低 1/1024 的真实 H 延拓，最终仍须返回请求的原 H，并实际取得所需 Jacobian/audit。R92 可在 jacobian=false 的成功请求后保留本来已计算的全节点 Js，所以后续切线预测仍来自自己的已收敛 W22 轨道。

fast-03 没有改 worker 的旧无切线 fallback：它把 Q 和非线性动量 π 同比缩放。这**不是** R86 的物理一 jet 缩幅，因为高 π 包含非线性卷积。

fast-04 接入尾研究代理的 `78718-tail-geometric-amplitude-warm.mjs`：无可用 tangent 时先由现有 engine 取 raw Q/L，同乘真实比例，重求 mean 与全部 π；node0 先将 π 乘 portRatio 入 cell0 engine，回存时除回，其他节点沿用 R86 的 cell/profile/x 映射。然后仍执行原 `correctInitialBoundary`；真正 tangent 存在时优先用它。本次只是 warm 表示变更，g、原最终 H、floor=.05、物理 BC、残差、36 轮和所有实际成功判定都不变。实际准备/收敛以 fast-04 自己的记录为准。

## projectionFloor 不进入固定 g 的 profile 公式

这里只作源中明确函数依赖的分析，没有运行另一笔 DN 或修改当前 floor。

1. `closing_weighted_tail.mjs::createRecalibrationFactory` 只在既有径向 warp 的自由积分项乘正 weights，并由 `assemble` 取得实际 profiles。它读取 `warpWeightLevels`、valley controls 等物理参数，没有读取 projectionFloor。
2. `closing_recalibrated_tail.mjs` 的 source、cap、profileSource、integrand、积分、alpha、physicalCell 和 assemble 所用参数均明确。它们产生 `r(x), r_x(x), log w(x), (log w)_x(x)`，没有 projectionFloor 依赖。向底层 balanced source 传的是显式列出的物理参数，也没有该键。
3. 原 `f6tail_compact_controlled_tail.mjs` 同样如此。返回的 `parameters` 会用 `...input` 或 `...options` 回显额外字段，所以修改 floor 可以改变记录对象/哈希；**回显字段变化不等于 profile 或 g 变化**。
4. 真正消费该值的是 momentum/raw engine：原 `general_root_tail_momentum.mjs` 与新 `78718-tail-fourier-root-momentum.mjs` 在每个角节点要求 `D>floor, S>floor, A>floor`。旧/new shooting core 默认显式传 `.05`；独立 engine 的自身默认是 `.1`，生产不能把二者混淆。combined worker 从实际 `dn.tail.parameters.projectionFloor` 传值，当前确为 `.05`。

写作物理径向坐标时，固定目标 metric 为 `(1+w(r)^2) dr^2 + r^2 dtheta^2`；在 profile 的 x 坐标中径向项再乘 `r_x^2`。上述 profile 与归一化 μ、端口数据都不因单独改变 floor 而改变。

## 改正性余量能够、不能说明什么

在给定合法状态处，root 的 moment 方程、其 Jacobian、split RHS 和 RK4 公式没有 floor 项。floor 是额外数值域 `min(D,S,A)>gamma` 的门槛。把 gamma 从 .05 改为一个更小的正数，扩大仍为正分支的数值搜索域，不是改变固定 g 或 moment 方程。

但它可能改变 Newton 的可接受 trial、迭代路径和最终数值图；不会凭空提供新的收敛、连续正性、curvature 或 reach 证明。尤其角节点通过较小正余量不等于全连续角域通过；新图必须用自己的完整连续 metric/reach、完整高 jet 接缝和无限尾包络计算，不能复制旧 .05 图的预算。已有局部小点诊断即使找到 .04 的正根，也不能证明整条新轨道成立。

将来若明确选择新 floor，输入/输出 metadata 必须照实声明该数值改变，并在 generic 的“仅 M/N 改变”比较中明确允许 floor 这个算法参数；旧 warm 数据的来源字段仍不得改写。当前 fast-04 保持 `.05`，本笔记没有实施或授权一个隐蔽 fallback。
