# 实际末端桥段加密仍未取得可接受更新

日期：2026-11-14。状态：**request15 的完整公开 Actions 运行失败，零接受更新、新 H 尾请求 0。** 699 个原节点全部保留，新增解析节点通过了原域和导数检查；失败发生在完整联解方向及其原回溯。不能把准备成功记成完整曲面接受。

## 1. 真实运行与输入身份

- run `43596755251`，attempt 1；source `d2d1aab1013aaf43ce993177732f78c48d437973`。
- job `132452818205`，lane `coupling112bridge`，终态 failure。
- artifact `14114833371`，ZIP 37,064,618 bytes，SHA256 `83c3780de8ea9f54f4855a8751060d09c084969301c93adb4ae14a8f3216b1b3`。
- always publisher 成功，日志实际推进 `3f505c7..4818868`，输出目录 [public-actions-43596755251-1-coupling112bridge](public-actions-43596755251-1-coupling112bridge/)。
- mesh adapter SHA256 `038c319dc2dce09d38b0dd94ca21281a721e6023dccd6007b68d686050be7d15`，对应已发布源码 Git blob `54522609670e4b1b20d4987b36cfac2a6c500a9f`。
- 原 accepted SHA `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`；原 699 warm SHA `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`。
- 本次 prepared SHA `bd8d3fd33e3fbfc23d621014ed3cc1c990113cb979238653d6cbad3acb6721f4`。大原件保留在完整 artifact；Git 单文件限额不意味着重新计算或分块搬运。
- 诊断消费 request13 真方向 SHA `d7f6c5ec07990f2fc8948eb1371d54503d2ecaded978d7d7282a7640b487d2a2`、RHS SHA `ebc3c2343eced8c9c21c51a1519c124e6c120ed02b6e609fec5f9e32771c9560`。

各 JSON 相对路径以下均以该输出目录为根；完整原件和 publisher manifest 是证据，下面仅摘录实际字段。

## 2. 准备和原完整 FD 的成功范围

`bridge-preparation/driver-status.json` 与 `bridge-mesh-plan.json` 记录：699 个旧点及其 453 维状态原样复制，新加 374 点，共 1073 点。新点只用同一 p=0 原解析种子、完整材料圆投影和原高度均值，不插值此前失败的 966 点场。旧桥段点重新评价解析种子的最大差为 `2.220446049250313e-16`；仍复制旧值而不覆盖其舍入。

采样参考相位预算选择 1，rho 的 2048 点采样最小值 `0.16604058243275`，最大节点仍 1200、原预检预留 24。guide 的第二项是 $|(\log w)'|=|a'a''|/(1-a'^2)$，不是子午 frame 的角速度；公式本身未改。这些是选网格参考，不是实际有限 Jacobian 的谱界或全圆 rho 证书。

全部原节点、中点和两 RMS 查询通过，初始完整 collocation 最大残差仍为 `0.0071105950777444905`。准备耗时 `86.120038819` 秒。

`physical-response/response-check.json` 重新以真正 T112 零锚的完整 Jacobian、非零 H 检验 R252 两个 core 链式项，四阶 Richardson 最大相对差为 `9.650162479919298e-10`，耗时 `26.265216469999984` 秒，通过原 `5e-5` 阈值。这一 FD 暂将真实完整 J 保持仿射；没有新的非零非线性尾求值，也没有完整 BVP 接受。

## 3. 实际局部矩阵没有遵循理想圆的简化谱

`bridge-preparation/bridge-local-block-comparison.json` 只比较实际原 collocation 的局部 L/R、真实有限 Jacobian 与旧方向的 Hermite 延拓。没有另求全局 Newton 方向、没有尾请求，也没有据此推定接受。

旧方向峰值在 node 691、$s=2.241097326439726$，物理方向最大 `352.4392787582113`。该处 scalar 的二阶量为零，参考 guide 未拆分该原 cell，但实际有限矩阵有：

| 实际量 | 原 cell 691 |
|---|---:|
| midpoint Jacobian 谱半径估计 | 160766.2470968914 |
| 首 L 条件数估计 | 1825615274701.149 |
| 首 R 条件数估计 | 1885673868210.3088 |
| 旧方向拆 2 后 Hermite defect 最大值 | 1167.3719456938868 |
| 旧方向拆 4 后 Hermite defect 最大值 | 8560.85327609721 |

这些谱和条件数是浮点估计，不是严格区间结论。原单 cell 的小线性残差不能推出它在细网格上表示稳定的连续方向。

末原 interval 697 被参考网格拆为 60 段。其首 R 条件数虽降到 `16913539.714233693`，首实际 midpoint Jacobian 谱半径仍为 `172564.8951892155`；整个原 cell 的局部传播乘积范数估计达到 `2.2198968767479164e23`。因此“局部 R 更好条件”没有给出稳定的整体传播。R255 的精确未截断材料圆结论不能直接用于这里的有限物理角 Jacobian。

## 4. 完整带 LU 与全部原试探

`full-DN112/banded-linear/factor-001.json` 记录完整维数 $453\times1073=486069$，仍为 338 physical、112 core、3 scalar 行，left341/right112；带宽 kl793/ku564，LAPACK 带数组 8,364,275,352 bytes。未删方程、未截奇异值、未改原数学表示或容差。

LU info=0，确实原地共享数组；因子耗时 `21.920194992999996` 秒，完整构造 `338.722480858` 秒，RSS `8668284` KiB。完整原块在 long double 累计的残差如下：

| 实际保留结果 | 数值 |
|---|---:|
| 原残差绝对最大值 | 2.0880106240436208e-8 |
| RHS 最大值 | 0.0071105950777444905 |
| 残差 / RHS | 2.9364780320270272e-6 |
| 方向最大值 | 1014.9245648257356 |
| normwise backward error | 2.0825648583419957e-19 |

第一次校正改善并保留；第二次变差而弃。小 normwise backward error 不能代替方向准确性，所设线性相对目标 `1e-10` 未达到。方向比原 699 点的 `352.439...` 更大。

实际 first-step 为 3,735,622 bytes、SHA `e750f31c968e8500894a81f3dcb1ce484d3e78d575f6337356cdb8d00d646781`；RHS 为 3,503,202 bytes、SHA `6ad535da9d22040cdba511d3c7678e3246fb18aa2ba6e0bfa104d3d3cf25e3c3`。

`original-newton-domain-evaluations.jsonl` 有初场及原 17 次 trial。初场节点和真实中点全部有限；17 次原 trial 全部无有限完整 collocation，故没有任何接受更新。最小原步长 $2^{-16}$ 仍有 **399 个坏节点、496 个坏中点**，右 BC 非有限。最早坏节点已在 $s=1.2392225749879933$，所以失败不局限末桥段。

最终 `driver-status.json` 为 `inner-newton-not-accepted`：1073 nodes、inner status 1（下一网格超过原上限）、RMS `2.1256299042752573`、原 affine BC `9.607979083759376e-8`，耗时 `420.177601986` 秒。没有新的完整候选、H 尾、readout、闭合或 R249 结果。

## 5. 接续决定

此次排除了“只保留全部旧点并按理想圆 bridge 尺度加密，便足以让原 Newton 成功”的具体尝试；它没有证明该完整 BVP 无解。不能只抬 max_nodes、照搬连续圆谱，或重复同一 699 点 QR。

下一计算从原合法 699 warm 出发，精确参数化常数 core/p 与左入口，剩下全部 physical collocation 和完整 112 条 Rphi。使用原完整块的矩阵乘法、转置乘法，求有正阻尼和角导权重的 LSMR 方向。必须真实重算非线性 midpoint、RMS 查询和边界，记录与该方向一致的预测下降及实际下降。

这个 warm 过程改变迭代算法，不能称仍是原 17 次 Newton 算法；它不修改最终方程和验收门。任何产生的 warm 仍须进入原完整 fullDN、RMS、BC、冻结物理检查、真正非零 H 尾和最终 audit，才能登记接受。域及正确 Armijo 的推导另见 [完整 Newton 域与 Sobolev 方向说明](2026-11-14-full-newton-domain-and-sobolev-step.md)；其中过滤 Newton 只是备选，不冒本次选择的 LSMR。
