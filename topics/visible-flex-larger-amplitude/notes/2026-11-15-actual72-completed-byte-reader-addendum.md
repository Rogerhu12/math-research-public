# Actual72：完整字节读回附记

类型：数值证据的字节完整性附记。  
作者：ChatGPT / exact_refinement。  
日期：2026-11-15 UTC。

## 结论与证据来源

第 72 轮已完成的 Actions 读回通过完整原件审计。本附记再将该读回中的五份原报告副本、其中四份既有公开报告及实际新 warm 的字节身份对应起来；未重新下载 605 MB 原包，未重算矩阵、方向、范数或科学接受条件。

原科学 run 为 `43656584956`，source 为 `eff90c141df410e83e273d568e4b707903bf8df2`。其原 artifact `14138023704` 为 605047997 B。只读 run `43658612002`、job `132642663978` 全部成功，source 为 `d63c771c9f4b6e26285d3ed56d3d7b554df63d15`；根已核其 841291 B 小包的大小、SHA256 和 ZIP CRC。

原完整审计位于读回 artifact 的 `request72-readback/large-arrays/complete-original-byte-audit.json`，753435 B，SHA256 为 `b897d85315d76672f5ec9747111581cf0d6b18e7d3f4b871de72f0ce537f8327`。本地核对只使用标准库读取、哈希、字节相等及已保存的整数布局记录，结果见 [原件对应回执](actual72-completed-reader-addendum.json)。

## 22 组实际查询与 484 列

本轮保留 15 组原 left-RMS 查询及 7 组原配点中点查询，每组完整 2048 角，共 45056 行。新增项是 **left-RMS484**；本轮没有加入 midpoint484。原中点集合仍为 473、475、477、480、481、482、485。

声明的局部坐标与实际编译列并集都为 7101；21 个实际物理节点为 466 至 486，另保完整全局参数列。原先仅为连续布局保留的节点 484 现已有真实 B 列：`zero_layout_nodes=[]`，零布局列数为 0。全部 22 组各自的 679 列映射均与完整局部坐标逐项对应，实际列并集和声明布局相等。原 C 投影的 4059 维修正支持未扩张，完整 B 与全局恢复的范围单独保留。

实际 B 模型身份为 `caf431a6f00ee9429cacc37480952605b38b18abfa200e1673fe0fb888332574`。这项身份记录绑定本轮来源与布局，不替代原非线性域检验。

## 完成的字节范围

| 原件范围 | 已完成 Actions 读回 |
|---|---:|
| domain NPZ 文件 / 内含 NPY 数组 | 199 / 1284 |
| condensed NPZ 文件 / 原数组引用 / 唯一完整数组 | 108 / 42 / 38 |
| 凝聚与恢复 raw 文件 | 14 / 415120992 B |
| 实际源文件 SHA 对照 | 65，缺失来源声明 0 |
| 原 collocation observer 报告 | 13 |
| 原 midpoint observer NPZ | 13，全部有匹配原 descriptor |

14 个 raw 文件包括完整原 $g$、局部索引、完整仿射列及其线性项误差、$7101\times7101$ 局部平方根、局部仿射项/梯度/中心，以及实际恢复方向、请求右端、局部不匹配和原 $H$ 残差等。审计读取保存数组的全部组成部分和实际字节，没有在读回中重新求逆或做 $A/B/H$ 作用。

原实现检查报告仍保留：最大 normwise adjoint error 为 `1.4324486533737623e-17`，local/full action error 为 `0.0`，完整 complex-chain relative error 为 `1.09292020462697e-12`；这是原科学 run 已计算的标量，本附记仅对应原报告。

**完整链 QR 因子当时仅在原进程内存中，未由原 producer 导出。** 因此 14 个 raw 文件的审计不等于完整链 QR 因子的独立字节审计，也不等于重新形成原全矩阵。回执保持 `full_factor_files_independently_audited=false`。

## 原报告与 warm 身份没有改变

读回保存的 status、model、comparison、QP summary、FD 五份原报告副本，均与其原 descriptor 的完整文件 SHA 对应。其中 status、model、QP summary、FD 与先前公开取得的原件逐字相同；另实际 warm 的完整压缩字节也与原 descriptor 对应。

实际新 warm SHA 为 `f59e8c64399a9fed392a8f8c3976209aaa3fa662c5c6ea65d864342cca697213`，status 解压后原文件 SHA 为 `73a0c0148f6166608ce47ecd4831b6e09a013e50907bfe7aae7468b687ce857f`。父仍为实际 68 的原 warm/status 对，完整父 producer 子树和当前来源均由原读回绑定。

原 status 的 `accepted_warm_steps=1`，同时 `success=false`、`new_coupled_finite_acceptance=false` 保持。原 affine FD 最大四阶相对误差 `1.0376926981953254e-09` 已对应实际新 warm；它不声称该新高度的 native 非线性 DN 已求解。

本附记补充[第 72 轮正式数值报告](2026-11-14-actual-request72-twenty-two-query-nearest-midpoint484.md)的原件范围，保留其原试步、最近拒绝与科学结论，不增加第 74 轮或其他后继的接受门。
