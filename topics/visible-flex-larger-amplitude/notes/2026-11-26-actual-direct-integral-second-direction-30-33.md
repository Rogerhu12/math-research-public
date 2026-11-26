# 同一完整积分范数的第二个实际方向：03b 第 30、33 步

日期：2026-11-26。这里只登记公开 Actions run `45820592817/1` 的实际返回。第 30 步完成一个新的完整方向；第 33 步只读该方向的现有报告，没有新增场、Jacobian 或优化调用。本文没有连续证书或完成声明。

## 1. 实际来源与父子链

公开证据是 [part-007](2026-11-26-public-actions-45820592817-1-part-007.md) 第 30 条和 [part-008](2026-11-26-public-actions-45820592817-1-part-008.md) 第 33 条。读取时两份公开文本的 Git blob 分别为 `a4a04434627656f169f259d7585e98ea5884c19b` 与 `62f2e8f70f68f690d23ffc7edb1aaaaaf6b8e5dc`。

| 项目 | 实际身份 |
|---|---|
| 第 30 步 | `continue-independent-axisymmetric-SO3-integral-norm-655d-full64-20261126-03b` |
| 实际源提交 | `a41d42d7b028e16da3055a053cf1893044b7f492` |
| launcher SHA256 | `a94263f037dfa8535b11cf44fa93b6a4cd6df7dee1a6be35f2ea14f5abaa2690` |
| 完整 driver SHA256 | `606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9` |
| 初始 reference | `0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1` |
| 完整模型 | `9d4ccb16efe9a0c0f5b077c0e8919e76d1d04b06e669588b32e2de78c92f0258` |
| 固定标量目标 | `6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb` |
| carrier | `b0257d9e03da36a422eab4e424942d38ccf817ac40ceb3b42be4378b1260966f` |
| 实际父 bundle | `655d29f2734b00bce0097cbb16f64d3b0a33a1774ba463f285917679686427c0` |
| 新末 bundle | `fd3f8c43a3c2e51c52177667597b33c13810b899fa9c4196384f821be9f9c14a` |
| 科学报告 | `axisymmetric-so3-integral-norm-second/report.json` |
| 科学报告 SHA256 / bytes | `7212a132e92dff74fff18b2d046658078aef27c07a670cb5dbfa287701837b22` / 12,967,474 |
| 第 33 步纯 reader SHA256 | `6d54cbba7ff998bc98b0f39c6a26ae33c16957fb0b9dc0fffced1037212455eb` |
| 纯 readout SHA256 / bytes | `d2bd4e442d0be5a278f00f30692eeea310eb25804ae34bf5e55ebf36fc0428f4` / 55,065 |

两次 `final.npz` / `initial-new-field.npz` 均为 10,720,288 bytes，后者实际等于父 655d。完整 argv 保存在公开第 30 条，不能只靠本文的摘要重建输入。该次请求从真实父 restart，保持同一固定目标、原 `p=4, epsilon=.001, scale=.05` 和同一积分范数；不是第 26 步从 `q.initial` 重新开始。

本次显式消费 reference locations、实际 3、17、21、26 的完整报告以及实际 28 的失败报告；restart 本身也按完整已有来源绑定。初始地址为 1763 / 1763，与第 26 步末摘要 1757 / 1715 不相同。完整 walker 从全部报告的实际选择/试步/永久位置取并集，不能以末摘要两张表代替这一输入，也不能未经纯地址比对断言差额只来自某一报告。

## 2. 所有变量、损失与范数

本次仍为 `M=160, J=923, N=2048`，1,333,370 个自由量；全部三个 Gram 行、全部正权和全部角，报告 `full_rows=45,324,288`。没有移除自由 core、径向/角向模式、H、均值或任一残差行。

积分范数身份：

- schema：`complete-SO3-radial-H2-positive-whitening-v1`；
- identity：`c06a7abc532243cc3faee0b123a4d5c7f6c109527e426dc764b1205af528c8d9`；
- 原 band：`ba5017bbbf9e8b63a63541ca39ef6636e6f691064f5aff1b81d5e9519e00b10e`；
- 原 factor：`9c04393e73929625c76514bb3b78572e949b78dddcfcfa504163484e23e22d2a`；
- equilibration：`044bdec037398e505ae5a4d9626ee24ee06b8f3c8141e44405548684ddb57be3`；
- 正 Gauss 阶数 6，带宽 5。

这里是原 integral 分支的实际成功执行，没有实际 Cholesky 失败，也没有使用备选 QR 把新算子冒作旧算子。新方向预算为 1 × 64，restoration 预算 4 × 64，实际 restoration 为 0。metric / restoration 的初末 μ 都是 .01。

## 3. 实际结果与未驻点

| 量 | 实际父读数 | 新末读数 |
|---|---:|---:|
| 同一离散 Phi | 197.58457993534574 | 189.95031194043378 |
| 离散最大相对 metric 缺陷 | .5063653325054447 | .5012790550010631 |
| 全真筛最大物理 g | −.0246162690033348 | −.02492266722260683 |
| 曲率永久地址数 | 1763 | 1843 |
| 半径永久地址数 | 1763 | 1771 |

纯 reader 给出同一目标变化 `−7.634267994911966`。实际只接受 1 个 metric 方向，α = 1/32；停止原因是 `declared_metric_direction_budget`。

内层 QP 完整返回：

| 量 | 实际值 |
|---|---:|
| status / advances | `iteration_limit` / 64 |
| 末面投影梯度范数 | 2163.522488520834 |
| 同面判停容差 | .002679762896474765 |
| 末面活动行 | 4 |
| 线性违约读数 | 4.912791094074942e−20 |
| 原几何行 / 幅度行 / 总行 | 39 / 6 / 45 |
| 当前完整 C 存储 | 480,013,200 bytes |
| QP 时间 | 1548.7627266389973 s |
| QP J / J* | 67 / 68 |

配置的 `active_rows=192` 是原完整 selector 的预算，实际本父产生 39 个原行，再加 6 幅度行；不能把配置值冒作本次真实 192 行。所有原自由列保留，当前 C 的 45 行全部参与 QP。线性可行不能推出完整非线性几何可行；末面梯度远高于其判停容差，不能把 iteration_limit 写成驻点或最优解。

## 4. 六次真实试步

| α | 真 Phi 下降 | 全几何读取 | 非负化的最大物理 g | 接受 |
|---:|:---:|:---:|---:|:---:|
| 1 | 否 | 否 | null | 否 |
| 1/2 | 是 | 是 | 6.973329875282846 | 否 |
| 1/4 | 是 | 是 | 1.9318032996928904 | 否 |
| 1/8 | 是 | 是 | .7404000178439538 | 否 |
| 1/16 | 是 | 是 | .1780438776582185 | 否 |
| 1/32 | 是 | 是 | 0 | 是 |

六次 `actual_read_error` 均为 null。表中末项 0 是纯 reader 的 positive-g 输出；原末报告的真实最大 g 是上述负值，并非恰在边界。

本次已能确定：α=1 被真实目标门拒绝，α=1/2 至 1/16 被真实几何门拒绝。当前紧凑输出没有列出这些拒绝的具体 family / 最坏地点，因此不能把它们直接归为 reach，更不能未经实际读取沿用上一方向的 cell 0 或 cell 1。下一次算法改变须以该父和实际拒绝地点为依据；本文不把再次增加迭代数当作已经解决了全局化问题。

## 5. 同场末态筛查、成本与责任

末态 `all_permanent_read=true`、`all_signs_read=true`，finite 真筛 `final_feasible=true`。K product 为 .9283586710100987。五个幅度分量实际为：

- body：−.02492266722260683；
- +p：−.13778010381788697；
- −p：−3.309031889679945；
- cap：−.06794714046380534；
- H：−1.0401709227152365。

第 30 步控制器计时 1925.410761651001 s；科学报告初始读取 142.85898043199995 s，总计 1919.3847960470011 s，peak_rss 原字段值 2164416。累计 residual/J/J*/point-covector 读数分别 9/68/69/44。第 33 步 6.062520237999706 s，纯 reader 的 J/J* 调用均 0。

第 30 步没有 summary_errors。第 33 步虽 completed/0，但有 86 个摘要索引缺项：它们仅指预先配置的未发生 trial 6–14 和未发生 restoration 0–3。真实方向只有六个 trial、没有 restoration；这些缺项既不能补零，也不构成科学 child 的失败。

新场仍明确 `metric_certified=false`、`geometry_certified=false`、`accepted_isometry=false`。有限 screen 和下降不是本题完成标准，旧场的连续 first/K 证书不能转移到 fd3f。接续需保全本次全部发现地址，并对 fd3f 本场重新承担连续 metric、几何、幅度、全 t 与同固定 g 精化责任。
