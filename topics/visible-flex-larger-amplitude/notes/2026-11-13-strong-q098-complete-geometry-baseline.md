# 已接受 q098 的完整均值几何基线

## 对象与身份

本记录仅是新的**有限几何设计基线**。实际已接受解为
`2026-11-13-strong-q098-m28-newjac-actual-r1.json.gz`，SHA256
`88175797998edbbe6d7ed18065fb8786cc58cec5e255b0efb95da9d08c728699`。
固定设计 view 的 SHA256 为
`3696f145fdab26526a74010ebacd1c2a4925be9b57884301ffdcf3c47d4cd891`。
二者不是两个不同的物理解。

原固定 view 转换报告保持完整物理 quintic、全部原 raw 节点、状态与
cubic、28 项尾高度、core、profile、物理度量和材料坐标相同。新的
[`root_geometry_fixed_view_witness_bridge.py`](../computations/root_geometry_fixed_view_witness_bridge.py)
实际核对了这条链的 123 项条件，逐文件重核物理 quintic 和 raw 分块的
字节 SHA，逐 binary64 比较 x/y/cubic/RMS 及保留参数，并核对完整 H。
其输出
[`2026-11-13-strong-q098-fixed-view-geometry-witness-bridge.json`](2026-11-13-strong-q098-fixed-view-geometry-witness-bridge.json)
保留原 physical-interior audit 的 input SHA；没有把原 audit 改标成
fixed view 的文件身份。

原完整均值 physical-quintic audit 的最大已采样曲率是
`8.255857363716027`，位置为
`s=0.9694668898968043`、`psi=1.988039101099791`。其角是 768 网格的
index 243，不属于 384 网格。新几何共同网格显式包含这个点：

- `t=0.30420152408437534`，径向 index 533；
- 3387 个径点，包括全部 2212 个原 raw 节点、原全部物理分段锚和补充比较点；
- 完整 768 个角；均值高度及其一、二阶径向导数使用原规则 1360 角；
- 均值高度保持 Gauss 6 阶，独立批量为 8；所有 28 模保持。

## 实际正式完成的基线

零控制步场由原完整 raw 状态的 physical-s C2 cubic 计算。它没有重新
解 BVP，也没有调用新 H 的尾工人。完整 finite-domain 检查和全部
`3387 × 768 × 3` 浮点值已完成，16 个无损分块全部核验；正式退出为 0，
wall `213.3412208557129` 秒，峰 RSS `158948 KiB`。

| 有限样本量 | 实际数值 |
| --- | ---: |
| 单一固定原点的 `S = max 2‖X‖` | 3.925501732144566 |
| raw-cubic 最大绝对主曲率 | 8.255881544533366 |
| 上述曲率与 S 的乘积 | 32.408477303446084 |
| 原 physical-quintic 曲率见证与同一 S 的乘积 | 32.40838238160573 |
| 全 28 core 的轴相位差 `2 Σ a_(2j+1)` | 0.19512909318712157 |
| 该轴差 / S | 0.049708064472186425 |
| 最大绝对高度样本 | 1.934709360708688 |
| 最大水平半径样本 | 1.3468361575111159 |
| 最小切平面面积样本 | 0.22014462957348777 |
| 最小 Frenet 域余量样本 | 0.005135041049744493 |

在原 physical-quintic 见证点，raw-cubic 场给出的两个有符号主曲率为
`-8.255853791176339` 和 `0.3250813617997048`。其全网格最大值略大于
原 quintic 见证值。后续局部设计预算应同时保留两种记录；raw cubic
不取代物理 quintic，任何一个样本最大值也不构成连续曲率上界。

原 `q098-m28-newjac-warm-r1-screen.json` 的 `κ=8.17821223055157`
使用 386 个径点、384 个角，且保存的 mean-height angular 为 384，
曲率见证在 `s≈2.60004`。它与这里的共同网格和完整均值规则不同，
所以两者曲率差不能直接归因于 Newton 的非线性修正。新的六控比较和
组合场将使用本次统一的 3387×768 网格及 1360 均值角数。

S 是有限点上距固定原点范数的两倍；这里没有认证它是整个闭曲面的
直径。轴相位差没有被认作模去欧氏刚体运动后的 `δ_E`。本记录也没有
给出连续曲率、reach、完整闭曲面或 README 振幅阈值证书。

## 保存与后续输入

基线的 screen、resource、field-manifest、execution 和 archive 是
`2026-11-13-geometry-m28-q098-r1-baseline-*.json` 的五份冻结文件。
大分块保存在 `geometry-work/m28-q098-r1`，由已存计划逐字节重新生成；
它们没有被删减或平均成较小的场。

共同网格和 baseline-only 计划分别存于
[`2026-11-13-strong-q098-geometry-grid.json`](2026-11-13-strong-q098-geometry-grid.json)
与
[`2026-11-13-strong-q098-geometry-baseline-plan.json`](2026-11-13-strong-q098-geometry-baseline-plan.json)。
六个真实控制导数完成后，只补十二个方向场；这个基线不重算。

下一批程序已复制到独立 scratch 源目录，保留原命令路径拼写与文件
SHA。全部 25 项已有基线必要源以及原计划输入再次核验一致。快照共有
669 个文件，完整清单见
[`2026-11-13-strong-q098-geometry-private-source-manifest.json`](2026-11-13-strong-q098-geometry-private-source-manifest.json)。
这只防止并发 Git rebase 短暂移走源文件；没有修改任何算子、积分规则、
验收门或既有成功结果。
