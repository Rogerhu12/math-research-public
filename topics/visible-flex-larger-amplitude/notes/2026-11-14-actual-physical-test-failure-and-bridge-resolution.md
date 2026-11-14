# 实际 R252 物理角有限边界：FD 通过而完整联解仍失败

状态：**数值证据／失败尝试；没有新的接受场。** 本记录直接消费公开 Actions 的实际文件，不把准备、线性分解完成或小 normwise backward error 当作非线性成功。

## 1. 实际运行与可复现身份

- 仓库：Rogerhu12/math-research-public。
- request13，lane coupling112physical；[run 43594985550](https://github.com/Rogerhu12/math-research-public/actions/runs/43594985550)，source commit 821fded1d0289cc542072646061a46504155c26f。
- job 132447496553；创建 2026-11-14T12:28:21Z。真实 FD 步成功，全 DN 步 exit 2；readout/closure/R249 因没有接受场而跳过。
- artifact 14113948667，30 件，23,886,772 bytes；ZIP SHA256 5f6f2912178ca9afcf4d8609dc1a974a69abba66ff797fcbd9dad6df25030712。
- publisher 成功，以 e61dbf4 普通推回 main；限额内文件在 [原始输出目录](public-actions-43594985550-1-coupling112physical/)。超过 5 MB 的失败 pending 只保完整 artifact 与 publication 清单，未作为接受场入库。
- 输入仍为真实 .99/M96 场、699 节点 M112/N2048 准备、自己的真实 T112 零锚及完整 338×112 J。原 scalar/338 物理/112 core/3 参数、原非线性容差和 17 次回溯全部保留；只有已明确说明的 R252 有限边界替换旧材料角有限测试。

原始依据：[response-check](public-actions-43594985550-1-coupling112physical/physical-response/response-check.json)、[small-condition](public-actions-43594985550-1-coupling112physical/physical-response/physical-test-small-condition.json)、[factor](public-actions-43594985550-1-coupling112physical/full-DN112/banded-linear/factor-001.json)、[solve](public-actions-43594985550-1-coupling112physical/full-DN112/banded-linear/factor-001-solve-001.json)、[driver-status](public-actions-43594985550-1-coupling112physical/full-DN112/driver-status.json)、[domain evaluations](public-actions-43594985550-1-coupling112physical/full-DN112/original-newton-domain-evaluations.jsonl)、[tail diagnostics](public-actions-43594985550-1-coupling112physical/full-DN112-tail-diagnostics.json.gz)。

## 2. 完整真实 J 的边界 FD 与小矩阵

同一实际 T112 全 J 显式保持仿射，用非零高度输入同时覆盖两个 core 链式项；这不是用 ready 参考替代真 J。17.774226811 秒完成，三步 Richardson 最大误差 9.650162479919298e−10，二阶最大误差 9.883443236591561e−6，原 5e−5 标准通过，收缩检查通过。输入 accepted、prepared、config、anchor、旧 Uend 的身份检查全部通过。response-check 文件 SHA256 为 672b9942e4692de429f1d4b209859c6ec4caffadb517e8223961797785f148e4。

| 实际矩阵 | 原始 2-条件数 | 行列均衡后 |
|---|---:|---:|
| 新右 BC，112×453 | 621945.4092794692 | 2956.892618357605 |
| 新右 BC × 同一旧 Uend，112×112 | 119589.80909759151 | 162720.9454968406 |
| 旧右 BC | 827045542847224.1 | 165451678202484.22 |

新矩阵在所报 1e−8 至 1e−16 阈值均保全部 112 秩；旧 reduced 复现差 0，原 left Jacobian 差 0。新 seed BC 9.607979083759376e−8，旧 seed BC 1.337840693499054e−8。这里只证实际有限切口块明显改善；不能推出全局离散 BVP 条件良好或邻近非线性解存在。

## 3. 完整带 LU：线性误差改善但方向仍大

原完整 453×699 系统，316647 维，kl=793、ku=564，2151×316647 带存储共 5,448,861,576 bytes。LAPACK info=0，原地/共享内存检查通过，LU 5.994546696 秒，构造 129.73187952 秒，峰 RSS 5,733,092 KiB。

初次线性残差 2.1413271449403146e−7，相对原 RHS 为 3.0114598307566014e−5，方向最大 352.5244116611899。第一次同因子校正被保留：

- 原矩阵残差 5.849105862342715e−9；
- 相对原 RHS 残差 8.225902049534334e−7；
- 方向最大 352.4392787582113；
- 校正最大 .08513290297863857。

第二次残差变差为 6.068003609992949e−9／相对 8.533749346781458e−7，没有保留。normwise backward 8.869419516549448e−20 **不替代**上述相对 RHS 残差；记录的 1e−10 线性目标没有达到，但它也不是新增的非线性否决门。

保留方向的物理行残差 5.849105862342715e−9，core 6.253151039233972e−13，参数行 0，左 BC 1.21454e−14，右 BC 8.76851e−10。完整 step 2,353,321 bytes／SHA d7f6c5ec07990f2fc8948eb1371d54503d2ecaded978d7d7282a7640b487d2a2；原 RHS 2,298,044 bytes／SHA ebc3c2343eced8c9c21c51a1519c124e6c120ed02b6e609fec5f9e32771c9560。

## 4. 原全部回溯与随后自适应均没有接受

17 次 trial 全部有非有限量，最后原 alpha=2^-16 仍有 78 个坏节点、124 个坏中点和非有限右 BC。随后 SciPy 原插值到 966 节点：节点域均有限，但 19 个中点坏；新右 BC 约 9.607979435481746e−8，与 warm 同量级。phase=inner-newton-not-accepted，status=2，RMS=None，elapsed=170.394544553 秒，**零接受更新**。

末态 pending 的旧材料残差约 1.3378388679289559e−8 仍只是该未更新初猜在旧仿射边界的读数，不能写成新进展。真实 T112 零响应严格复用一次；worker 已启动，但新高度请求为 0，stderr 0 bytes。失败发生在第一次内部解之前，不能归咎于一次并未发生的非零高度 tail 求解。

## 5. 由实际结果选择下一项

R252 物理角测试已经减轻实际切口的近核，但全场方向与域失败仍存在。因此下一次不得原样重复 request13，也不得只抬 max_nodes 或放宽原门。

目前待检验的是末端短 bridge 的径向分辨率和局部传播。共同材料角的精确圆参照具有很强非正规性；Jacobian 条目的 k² 尺度不能直接当作 k² 特征增长。在随 meridian 旋转的二变量参照中，高模尺度含 k*sqrt(|a''|/(a*(1-a'^2)))，还需控制局部坐标旋转。它只是选择待检网格的参照，**不是当前截频物理角 Jacobian 的恒等式**。应报告实际 scalar、原局部 L/R 与所用步长，并与实际方向比较后检验这个假说。

最小可执行延续保留所有 699 旧节点，只在末 bridge 加点；新点由同一 p=0 原解析圆初猜及完整 z0/均值表达重新评价，不能插值本次失败的 966 点场。端点、metric 设计、真 T112 锚不变；完整真实 J 的 17 秒 FD 可重做，随后用全部原方程/原门实际求解。若该分辨率改变不能改善实际方向，则记录失败并进一步检查全局非正规传播或采用保持原方程的全局化策略；没有预设一定成功。

## 6. 执行现场中断与保全

2026-11-14T12:35:50Z 平台把共享执行环境标为 unavailable，终端实际返回 No usable execution environment is available。公开 Actions 独立完成，且上述 publisher 成功，原计算没有丢失。GitHub 小文本接口随后核实远端 HANDOFF 已含 12:30 的运行状态及 12:33:44 的实际 pull 记录，说明此前未决状态推送已进入远端。

按根 README Rule8 改用已连接 GitHub 的小文本接口读取/提交，不把该途径记作本地 git pull，不经接口传递 PAT 或二进制。新提交均基于刚读取的 main、核对双 README 并仅普通快进；远端变动立即重新基于新头提交。恢复终端后先核已有 checkout/未推文件，再恢复普通 git pull --rebase；旧未推代码依照 HANDOFF 重建，不冒成功保存。
