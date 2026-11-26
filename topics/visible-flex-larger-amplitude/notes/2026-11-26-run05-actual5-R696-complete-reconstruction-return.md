# Run05 实际阶段 5：完整 R696 输入重建返回

日期：2026-11-26。

本条记录公开 Actions [45870334713/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45870334713) 的**实际阶段 5**。它执行历史阶段 21 的完整 R696 分支，用于在本 runner 重新产生真实报告和全部适用永久地点。这里的阶段编号是本次运行的 5；“21”仅是完整重建步骤名称中的历史来源编号。

截至本次索引的 2026-11-26 19:13:34 UTC 记录，该阶段已经 completed，子进程退出码 0。完整科学参数、源码和预算按已刊重建请求执行；旧运行的数值、数组身份、几何证明和研究结论没有被当成本次返回。单方向返回与报告 complete 均不构成本题 README 的完成。

## 1. 实际来源与可恢复记录

实际步骤 ID：

`run05-history-reconstruction-21-complete-R696-angular-unit-first-20261126`

公开紧凑记录是
[`2026-11-26-public-actions-45870334713-1-part-001.md`](2026-11-26-public-actions-45870334713-1-part-001.md)
中的完整阶段 5 对象。本次读取该完整小卷的 Git blob 为
`9312e79a842c8416923345eca13282c18d50123a`，UTF-8 大小 53029 B。
这里只读取公开小卷，没有通过连接器读取 21 MB 的原始报告或科学数组。

| 实际对象 | 完整身份 |
|---|---|
| 运行与尝试 | 45870334713 / 1 |
| 实际源码提交 | `5a58d7c4d2d969e2e4236a8d53cbff34cc1cf30b` |
| launcher | `365409de518385acbebfbc3cf1d6cacd14de178e37b683e364324393fdaa718d` |
| 完整 driver | `7b7cc0c9b27a0339debab0319c6854323dfc6c21f3e92c64946cbffc70824c7d` |
| R696 operator | `d2f8a93c3356fc172e5c6ac365b0bff65660fea2bb3bf8350ab124537a0f4a14` |
| 本表示 geometry | `8fa941feb48f9c7a8a180a14d7f3ead9df00decb63e287531bf773b27285a6a5` |
| reference producer | `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3` |
| 实际 reference bundle | `59027f3a144f8f0feb59e378b058178c781856803e6e704db8a6ff689b45d90f` |
| 实际 observation carrier | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` |
| 实际固定 profile 身份 | `e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350` |
| 实际 R696 model 身份 | `464af04eaf6686d55f97f2cda6b95575e497683d5e0ec87b5c28c2fb79fce25b` |
| 本次坐标范数身份 | `93e50f57208d79c1715b9d16e2ca0bcbb5a92cddd77bdc953f064610e25c5557` |

实际 command 文件 SHA256 为
`cb2fb3cf50d18837a79738fd0940fc4002785ab9d0f0551807fa3a890d06c7db`，
10061 B。实际完整报告
`angular-unit-complete-first/report.json`
的 SHA256 为
`de556b4bb006d6add0014d710a6032a7551ca2030d06920ad24c76e336e27db7`，
21086392 B；完整报告和科学数组保留在 runner。

实际初始 bundle
`angular-unit-complete-first/initial-new-field.npz`
为
`5ee1dbc63c1d10f374417720534aee656f6b9915a1ee9873700cf4999b1b7ab2`，
10751590 B。实际末 bundle
`angular-unit-complete-first/final.npz`
为
`75b28559f1867841e50fa1e5621212a747560c4af473444ab803a5ca2a76ebe9`，
同为 10751590 B。NPZ 文件摘要、完整物理自由点摘要及模型身份是不同对象；本次紧凑块没有返回另一个独立的全自由点数组摘要。

本次队列路径提交为
`4b892504f20ea409eea9159f558887d4db3a247d`，
实际 checkout 提交与上表源码提交一致，
所消费队列 SHA256 为
`b44f25794924300157c1cf30533e789805972436c780b1bec288db125360afa6`。
完整 argv 在同一个公开阶段对象中逐项保存，没有用摘要表替代完整参数。

## 2. 本次真正执行的完整空间与预算

本次表示保留 1334847 个自由量，实际读数为：

| 自由量 | 数量 |
|---|---:|
| core | 157 |
| rotation | 1331926 |
| 径向 profile | 2763 |
| 高度 | 1 |
| 总计 | 1334847 |

实际 N=2048；径向积分阶数 8；angular cells=128，angular integration order=8，field stage block=16；主 stage block=64，angle block=8。core inverse 使用 18 次声明预算、容差 2e-12。

本次使用完整 node-jet H² 型 `jet-sum` 范数，径向长度 0.05、angular transition 24。metric 预算为 1 个方向、每方向 QP 最多 32 次；restoration 声明预算为 2 个方向、每方向最多 32 次；metric/restoration 初始 μ 均为 0.01。line trials=15，QP rtol=1e-6，atol=0，feasibility tolerance=2e-11，rank tolerance=2e-12。

真实命令保留 active rows 声明上限 192、active band 0.025、完整 active block columns 32768、reach ratio 0.03、安全乘积门 0.992，以及 marked diameter 4.2、witness lower 0.9、height floor 1.01、top radius 2、top distance 4。这里的 active rows 参数是选择器上限；紧凑结果没有返回本次实际选中行数，不能把 192 写成已经读取的实际行数。

原完整 summary 中，`initial_Phi` 与 `final_Phi` 分别映射 `initial.spectral.centered_phi_normalized` 和 `final_statistics.spectral.centered_phi_normalized`；`metric_directions` 映射 `actual_metric_directions`。下表据此使用 centered Phi，保原梯度、Hessian 与 μ 的单位。

同次损失参数为 p=4、epsilon=0.001、scale=0.05，legacy fraction=0.5，数值 target=5e-7。该 target 参数不是本题连续完成证书。

本重建分支的完整历史输入按原步骤保留为本 runner 的 reference locations 和实际阶段 3 完整报告。后继新机制需要继续消费各已返回分支的适用地点并集；本阶段的原始重建依赖与最终并集责任是两件分别记录的事。固定数学目标的来源已在
[Run05 实际输入与同一数学目标记录](2026-11-26-run05-actual-input-identities-and-same-mathematical-target.md)
中逐项说明；这里不把变化的文件摘要自行解释成新目标或历史豁免。

## 3. 实际方向与本场末态

| 实际读数 | 初始 | 末态 |
|---|---:|---:|
| centered Phi | 1156.1555250698154 | 1156.1339456379355 |
| 最大相对 Gram 工作残差 | 0.515133818848609 | 0.5151228968972323 |
| 实际 metric 方向数 | — | 1 |
| 已执行 restoration 方向数 | — | 0 |
| metric μ | 0.01 | 0.01 |
| restoration μ | 0.01 | 0.01 |

实际停止原因是 `declared_metric_direction_budget`。这一报告有完整返回和一个 metric 方向，但该紧凑对象没有直接返回 accepted 计数，也没有 QP status、projected-gradient、tolerance、active-face advances、步长 α 或完整 trial 表。因而本条不判断内层驻点，不推定 QP 收敛，也不从 J 调用次数反推这些字段。若后继决策需要这些字段，应由本 runner 纯报告读取入口消费该真实完整报告。

**接受与直接读数的区别。** 完整 7b7c 源码在末态分别保存 `actual_metric_directions` 与 `actual_accepted_metric_directions`；本次紧凑映射只公开前者。该源码的唯一 metric 方向若未接受，必在 `if not record['accepted']` 分支把 damping 乘 4；一个方向、零 restoration 下没有其它复位路径。本次实际初始与末态 μ 同为 0.01，因此按完整控制流可推出该唯一 metric 方向接受。这是由源码和实际标量得到的推论，不能把它标成直接读取的 accepted 计数；也不能用它补出具体 α 或 QP 驻点状态。

末态实际真几何工作筛为 true，工作值如下：

| 末态读数 | 实际值 |
|---|---:|
| 全部真筛最大 g | -0.02374763684032244 |
| reach 曲率直径乘积 | 0.9653816635333305 |
| H | 1.9470544311278353 |
| body diameter g | -0.02374763684032244 |
| +p 距离 g | -0.13778020157737703 |
| -p 距离 g | -3.3090312531674613 |
| cap g | -0.06715132012970448 |
| height g | -1.041171590142039 |

这些数值只属于末 bundle 75b285… 的完整数值筛。它们不等于连续全域、全相位 reach 或幅度证明，也不继承别的场的连续证明。

永久地点实际计数为 curvature 1615、radius 1550；`all_permanent_read=true`。后继必须消费真实报告中的完整地址；计数没有证明与旧运行集合逐字相同，也没有证明两个不同分支的集合相等。

## 4. 实际成本、工作积分字与尚未返回的归因

| 实际计数/时间 | 值 |
|---|---:|
| 完整 residual calls（公开别名 F_calls） | 17 |
| J calls | 35 |
| J transpose calls | 36 |
| point covectors | 34 |
| grid reads | 15 |
| field points | 386028688 |
| angular integrand points | 790773760 |
| 完整 launcher 阶段秒数 | 2398.7252022549997 |
| driver 秒数 | 2394.776656716 |
| initial setup 秒数 | 41.430390565999915 |
| peak RSS KiB | 2919276 |

core inverse 工作残差为 1.9975132659055816e-12，工作 rho 读数为 0.166018238399251。这不是全角 rho 连续下界。

本次实际保存的工作字：

- Istar：`0x1.f27228dabd93ep+0`；
- Jstar：`0x1.ec0bc59b655d2p+0`。

它们属于当前执行路径；R696 的该工作积分与其它表示中的 normalized-c / raw-c / 不同归约路径不能仅凭接近就互换为准确端点值。

阶段的 `summary_errors=[]`、`missing_outputs=[]`。报告显式 `isometry=false`。本条没有 α、末面、Pg、完整 ray 拒因、连续误差费用、全相位几何或最终完成证明的实际返回。公开源码与完整参数保持可复现；下一科学步骤按控制器真实记录继续，不能把运行重建结束作为课题结束。
