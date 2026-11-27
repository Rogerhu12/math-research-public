# Run06 实际39：完整归一化父四次恢复返回，真实违约仍为正

本条只登记公开 run `45904402595/1` 的实际第39项完整返回。索引更新时间为 **2026-11-27 00:58:51 UTC**；阶段 `complete-new-SO3-actual-parent-profile-first-20261126-rebuild06` 的状态是 `completed`、子进程 `exit 0`。这表示本次声明预算与末态读取返回，不表示几何可行、达到度量目标或课题完成。

## 1. 实际原始紧凑证据与来源

完整公开原记录见[第4卷](2026-11-26-public-actions-45904402595-1-part-004.md)。本次亲读版本 Git blob 为 `a0ae3c7d63b04518f8fa74685cbdf9ce8ab0794f`，完整 **10,455 B**、SHA256 `841ceac277b94974cb15e07b57708dbe9501088172a8bc6e565a98039ba55dd5`。该小卷完整保存本项全部 argv、输入路径、源码、输出与 cleanup 元数据；未读取或转存大科学报告、数组、逐点值或完整日志。

| 项目 | 本次实际身份 |
|---|---|
| 完整 driver | `7e9095b3a765f064baae9a36e9593667d5c469686232b6095065e0c3cf22c55b` |
| launcher | `b5342ef4558d1e4da58618e308e5382eee50f9e4fab2a9dd95dc1acea8c8d826` |
| 科学源码 checkout | `1156103ea1dc9db4cd186a6ef54093fc6c2bbf42` |
| 本次队列路径来源 | `f71e5cc32fb4d2dbfcd4f176c7ebd54e56831111` |
| 本次队列完整 SHA256 | `bd9f89b6fb6476cc0c373ca6313f28df5cd3696486dccbf39c1cecd701d1b3c4` |
| 本次队列检查 checkout | `436fabfd264165e875e305d6fec5efd53b5fc97b` |
| 原实际父 checkpoint | `d466ef7605281dcb951f821fe2de08953c53eb3a021a08a436f9529c6af4de04` |
| 新表示初场 NPZ | `8c57683ba8eef0d6b92c09464321d022bd43cf5916a2a71e2544b1b0dac346c1` |
| 实际末 checkpoint | `df9252b2a2ab9902041dce47fb50be7176e3b67993b37ea16c17ca725f441a01` |
| 完整当前模型 | `b28b7f76ea615cb317b4ca98f0d4b75a67c1e2792abc47e6f86c91266773d086` |
| 固定 scalar profile | `364e73ce2ed258b923c0dff10a1c4dfdc846e143930d4c56b55944d0d2c18853` |
| 原完整坐标范数 | `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa` |
| 完整实际目标绑定 | `395d67865b3bd15bc5732eb1696f28f5637ae90722dafba57ee4e73a8892b62a` |
| context 完整来源 | `9ca39afd9f840ba89fbb75d7365220c2d85d26ddb26b2d66b6c55e611313fd55` |
| context 模型 | `4209b966f3b9a8dca99fa96fe313cf713b5a1b3c6d34ac4254e65e1f9d7ddcc0` |

实际报告 schema 为 `complete-actual-fixed-deep-parent-closed-so3-meridian-QP-v1`。完整 context 记录 `context_all_four_inputs_equal=true`，对应本 run 的实际父、carrier、node 与 scalar 来源；没有借旧 run 的目标或 checkpoint 摘要冒当前输入。

## 2. 完整输入预算与本次实际范围

完整命令保 `M=160,J=923,N=2048`、**1,333,370** 个原自由量与 **45,324,288** 个完整逻辑 metric 行，径向 block64、角 block8、径向积分阶8、CPU threads4。norm 为 `jet-sum`，radial length `.05`、angular transition `24`。声明 metric 最多1方向、内层16 advance；恢复最多4方向、每方向64 advance。两种初始阻尼均 `.01`，QP atol0/rtol1e-6，15次 ray、原192活动行及全幅度行保留。

目标为 `p=4,epsilon=.001,scale=.05,legacy-fraction=.5`，reach `.03`、安全因子 `.992`、active band `.025`、marked diameter预算4.2、witness下预算.9、height floor1.01。精确目标的 `eta-start-node=885`、scalar admission300秒、integral tolerance1e-18、tail cutoff1/8和全部原 source/argv 以公开原小卷为准。本条没有缩减变量、均值行、永久地点或接受条件。

本项是06链的必要完整输入再生。新表示从真实 d466 父构造并重新读取自己的完整初场，产生独立初场 bundle `8c57683b…`。下面只比较这一表示的初末值，不将上一步 deep 表示的 Phi 与本项新初场直接相减，也不把相同命令当作跨 run 字节同一或旧数值结论再证明。

## 3. 实际四次恢复与未满足的几何门

| 读数 | 本项新初场 | 本项末场 |
|---|---:|---:|
| 工作网格最大 relative Gram defect | 0.03692722298506464 | 0.036927383701020465 |
| 本项同一 Phi | 0.006860331032992438 | 0.006860332542218574 |
| 最大真实物理约束 g | 0.032836283485021545 | 2.432468670932053e-10 |

实际 `restoration_directions=4`、`accepted_restoration=4`；`metric_directions=0`、`accepted_metric=0`。恢复接受标准对应真实违约下降，不能由“四次接受”推成四次 metric 改善。本项初末 Phi 与最大 relative Gram defect 均略有增加，应如实保留。

末态 reach 产品为 **0.9920000002432469**，仍严格超过原 `.992` 门槛；最大物理 g 为 **2.432468670932053e-10 > 0**。报告明确 `final_geometry_feasible=false`，停止原因是 `declared_restoration_budget; actual_violation_remains_and_is_not_accepted`。因此末场是可继续真实恢复的 checkpoint，不是已可行零步或可继承的 reach 证书。

| 末态幅度约束族 | 实际 g |
|---|---:|
| body | -0.04779494868743872 |
| plus witness | -0.09059103030889948 |
| minus witness | -3.3090767674832593 |
| cap | -0.1267469839800892 |
| height | -0.9649089301951751 |

这些幅度族均为负；本次末态几何门未过来自记录中的 reach 产品。但紧凑卷未保存每个恢复 trial 的完整族/地址、alpha、末活动面、Pg/tol或各QP状态，不能据本条自行填充。声明的64 advance上限不是已经迭代64次，更不是收敛证明。

实际末 metric 与 restoration 阻尼均为 `0.01`。末永久曲率/半径点数为 **2769/2744**，`all_permanent_read=true`、`all_signs_read=true`。该记录保全本场已知位置与双witness符号的实际读取；它不把有限点集扩大为连续全域或全 t 证明，也不以数量相同代替不同 run 集合相同。

逆材料图数值 residual 为 `4.440892098500626e-16`、数值 rho 为 `0.1659034349291033`。这些仍是该报告的工作值，不能代替准确逆图/root/整体嵌入证书。

## 4. 实际成本与输出保全

| 范围 | 实际值 |
|---|---:|
| 科学 child 秒数 | 2255.5253493299997 |
| 驱动总秒数 | 2246.619742481 |
| 初始 setup 与完整首次读取秒数 | 1783.0140031360006 |
| peak RSS，KiB | 2145844 |
| residual calls | 6 |
| J calls / Jtranspose calls | 0 / 0 |
| point covectors | 784 |
| parent jet evaluations / points | 16374 / 22946658 |
| evaluated field points | 41642572 |
| inverse chart solves | 19804 |

首次 setup/full read 与总执行范围严格分开，不把全部初始时间称为缓存构建成本。0个 J/J* 与实际 metric0相符；恢复所用完整几何协向量仍实际支付，不能因此说本项没有求导。

| runner 输出 | 字节 | SHA256 |
|---|---:|---|
| so3-closed-actual-profile-first/report.json | 38760255 | `8c1003524b5c0922ab69160a086d2a4e9305aaf24f275388433e0aaafaa78b4d` |
| so3-closed-actual-profile-first/initial-new-field.npz | 10720258 | `8c57683ba8eef0d6b92c09464321d022bd43cf5916a2a71e2544b1b0dac346c1` |
| so3-closed-actual-profile-first/final.npz | 10720258 | `df9252b2a2ab9902041dce47fb50be7176e3b67993b37ea16c17ca725f441a01` |
| so3-closed-actual-profile-first-command.json | 10875 | `9c6b10476a61bb2d5e75c54a0a229dad2cb62a104428cb29ba44873acca7ee76` |

报告与两个10,720,258B科学NPZ仅留 runner。`summary_errors=[]`、`missing_outputs=[]`，本条无待补的错误字段冒通过。cleanup仅清除4项明确新生可再算行缓存，显式字节共8,405,564,480，完整cleanup元数据摘要 `6388aff791029c3fa38bb0a20f9ff94cdfd91921111c447ed483b2d7779f001f`；原输入/父/科学输出均在保留范围，原明细留状态与journal。

## 5. 后继责任

已刊06完整队列继续执行原严格内点恢复源 `0f542de9…`，以本 run 的实际 `so3-closed-actual-profile-first/{report.json,final.npz}` 为来源，随后才接已刊四段同目标历史及当前八列完整PCG。这里没有跳过真实尚为正的违约，没有预填后继输入摘要、实际阻尼或结果。阶段40尚须单独实际返回；本条不以排队状态代替执行。

整体完成标准仍是本题 README 的连续 relative metric ≤1e-6、固定目标下实际精化、全 t 幅度/reach/嵌入与完整闭合证据。报告已明确 metric_certified=false、geometry_certified=false、accepted_isometry=false。本次恢复返回没有解除这些责任，研究继续。
