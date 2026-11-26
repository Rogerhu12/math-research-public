# Run05 实际阶段 6：完整 integral 范数首方向与本场返回

日期：2026-11-26。

本条只记录公开 Actions [45870334713/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45870334713) 的实际阶段 6：在本 runner 以完整原参数重建历史阶段 26 的独立 axisymmetric SO(3) integral 范数分支。完整方向返回为 completed/0。它产生可供后继真实续算和地点并集使用的新场；不重新宣告历史数学结论，不继承旧数组或连续证书。

证据为 [第 2 卷的完整实际阶段 6 对象](2026-11-26-public-actions-45870334713-1-part-002.md)，本次读取该公开小卷的 Git blob 为 `ef8c8f3cfcdf1b0a27a6e1c068c3c2f6ed3b7883`，实际 UTF-8 24892 B。原完整报告及数组只留 runner，没有通过连接器整读它们。

## 1. 本次真实来源与身份

步骤 ID 是
`run05-history-reconstruction-26-complete-independent-axisymmetric-SO3-integral-norm-full64-first-20261126`。

| 对象 | 完整 SHA256 / 身份 |
|---|---|
| 实际源码提交 | `7a144f6957b371eb4bf32d84038a49d54ebdc543` |
| 完整 launcher | `a94263f037dfa8535b11cf44fa93b6a4cd6df7dee1a6be35f2ea14f5abaa2690` |
| 完整 driver | `606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9` |
| 当前 reference bundle | `59027f3a144f8f0feb59e378b058178c781856803e6e704db8a6ff689b45d90f` |
| 本场 model | `9b4958325403bd74616c5875ca54f027981d2d55c9c56634dc81f8cd0d2123c7` |
| 固定 scalar profile | `e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350` |
| observation carrier | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` |
| 本次 initial-new-field NPZ | `9bf940b0d826e92c698d3ade82f80fa0ed043d4bd5cf8f52feb5dc6c3f600e76` |
| 本次 final NPZ | `c8cb4be613712282dedf4586c78d81bd86f7b9ae038c16a0f6ceced86eadd9a7` |

本次初始 NPZ 与本 runner 阶段 3 的初始 NPZ 摘要相同。它是完整新表示的真实初点，不是从阶段 4 或 5 的末自由点继续；新 integral 范数也不能与另一范数的方向、阻尼数值混作同单位比较。完整科学模型与目标来源见 [本次输入和同一数学目标记录](2026-11-26-run05-actual-input-identities-and-same-mathematical-target.md)。

本次完整报告路径为 `axisymmetric-so3-integral-norm-first/report.json`，SHA256
`7f3d9ca95e8e2010760ccd9578c467c8d00ba52ea32b5430d40f8112e31b46b1`，
10073485 B；初始和末 NPZ 均为 10720284 B。实际 command 文件
`axisymmetric-so3-integral-norm-first-command.json`
为
`ccc13e428607048354e008531e17138fda6e62860b8b74f1d9110db638328c75`，
10691 B。

队列路径提交为 `a3da90d7987144772dbaa0aa2357cf975a61f117`，
其 checkout 提交为 `5dc568747edd6ea9ea901ef957331100f22c7dc1`，
所消费队列 SHA256 为
`ff305dd23bbd56edd44ed7e53859cd4155ede021ca398749311a7c591c4e3b27`。
完整科学 argv、实际来源提交和所有输出记录保留在该公开阶段对象。

## 2. 保留的完整变量、范数和预算

实际 M=160、J=923、N=2048，全部自由量 1333370，完整正权观察行 45324288。没有删除自由 core、H、mean 或旋转变量。

完整范数 schema 为 `complete-SO3-radial-H2-positive-whitening-v1`，
kind 为 `integral`。本次真实读数：

| 范数对象 | 完整身份 / 值 |
|---|---|
| norm identity | `c06a7abc532243cc3faee0b123a4d5c7f6c109527e426dc764b1205af528c8d9` |
| band | `ba5017bbbf9e8b63a63541ca39ef6636e6f691064f5aff1b81d5e9519e00b10e` |
| lower factor | `9c04393e73929625c76514bb3b78572e949b78dddcfcfa504163484e23e22d2a` |
| diagonal equilibration | `044bdec037398e505ae5a4d9626ee24ee06b8f3c8141e44405548684ddb57be3` |
| 径向正 Gauss 阶数 | 6 |
| 径向 bandwidth | 5 |

声明的径向 norm length=.05、angular transition=24；积分阶数8、stage block64、angle block8、4 Torch threads。core inverse iterations18/tolerance2e-12。这里记录真实 integral 分支返回，没有把尚未运行的 QR 变体替换成其来源。

metric 预算为 1×64，restoration 为 4×64；两类初始 μ 都是 .01，line trials15。QP rtol1e-6、atol0、feasibility tolerance2e-11、rank tolerance2e-12。原 selector 声明上限192、active band.025、列块32768；其实际选中行数没有在本次紧凑块返回，不能把上限冒作读数。

原真筛预算完整保留：reach ratio .03、门 .992、marked diameter4.2、witness lower.9、height floor1.01、top radius2、top paired-distance4。损失 p4/epsilon.001/scale.05，legacy fraction.5，数值 target1e-9。该工作 target 没有替代题 README 的连续及精化完成标准。

本分支输入的四份完整地点来源为本 runner reference locations、实际阶段3报告、实际阶段4的359f报告、实际阶段5的R696报告。全部由原完整 walker 在当前 carrier/N 上解析并重读；原报告路径、所有参数没有仅以计数代替。初始永久集实际为1709/1709。

## 3. 本场实际数值与验收

原完整 summary 映射把 `initial_Phi` 和 `final_Phi` 明确取为
`centered_phi_normalized`；accepted 计数也分别直接映射报告的
`actual_accepted_metric_directions` 与
`actual_accepted_restoration_directions`。

| 实际量 | 初始 | 末态 |
|---|---:|---:|
| centered Phi | 213.89131075534186 | 197.584579939444 |
| 最大相对 Gram 工作残差 | 0.5170375580125983 | 0.5063653325058848 |
| metric μ | 0.01 | 0.01 |
| restoration μ | 0.01 | 0.01 |
| 全真筛最大 g | -0.024430047350427198 | -0.0246162690052385 |

实际执行 metric 方向数1、接受数1；restoration 执行数0、接受数0。停止原因为
`declared_metric_direction_budget`。紧凑对象没有返回 α、QP status、实际内层迭代数、Pg、tolerance、末 active face 或全 trial 拒因；64只是完整声明预算，不能凭 J 调用次数补出驻点或迭代终态。

末态真实数值筛通过，具体为：

| 末态真筛读数 | 值 |
|---|---:|
| 曲率直径乘积 | 0.9167359982020954 |
| body diameter g | -0.0246162690052385 |
| +p 距离 g | -0.13778012759893254 |
| -p 距离 g | -3.3090316747700292 |
| cap g | -0.06755212470592387 |
| height g | -1.0406676748550188 |

末态记忆计数为 curvature1757、radius1715；全部永久点重读和每点双符号重读均为true。这些是这个真实末场的数值筛记录，不是全域/全相位几何证书。完整报告的递归地点集合另包含方向和拒绝 trial 等地址，后继仍须消费完整来源；不能只导出这两个末态计数。

## 4. 实际成本与后继责任

实际完整阶段秒数1003.3137339000004，driver秒数1000.660423372，初始实际装配与全读88.10313481899993秒，peak RSS2080664 KiB。实际 residual calls8、J calls68、J transpose calls69、point covectors41。没有对这些时间或计数作另一个浮点科学推算。

summary_errors和missing_outputs均为空。报告显式
`continuous_metric_certified=false`、
`continuous_geometry_certified=false`、
`closed_isometry_accepted=false`。
当前最大残差仍是本表的实际值，不能以方向接受或范数返回作为完成。

已经排入的后继应以本次真实 c8cb4b…/7f3d9c… 作为其父来源，重读同一个固定目标、完整范数、所有适用永久地点和真筛。更换 SOC 策略或其它表示须有明确来源与自身 baseline；本条没有预先决定那一步的验收、家族归因或结果。
