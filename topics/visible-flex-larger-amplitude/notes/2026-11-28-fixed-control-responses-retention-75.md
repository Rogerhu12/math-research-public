# RET75：旧 q122/q126 固定场控制响应及两个派生读数的完整来源保全

AI-assisted research，ChatGPT construction，2026-11-28 UTC。仅准备完整退存记录与未引用 Git blobs；主线提交和删除由 root 实施。

本批按根 README §15 退下四份可由已保留脚本、完整参数和原始输入再生的旧生成报告，合计 **286,334 B**。候选锁定在公开提交 `693d9e3bf30f1822e735bf1aa15c3aca4838340b`。这四份文件是两次有限固定场线性响应，以及 q126 响应的两个代数读数；它们不代表新的非线性解。所有完整原报告仍由下表所列固定 Git 对象恢复。

完整机器记录分为 [来源与输入恢复表](../computations/legacy-fixed-control-responses-retention-75-source-input-registry.json) 和 [参数、实际结果及消费者台账](../computations/legacy-fixed-control-responses-retention-75-complete-provenance.json)。前者为 96329 B，SHA-256 `216e793b2e3709113505a3d210fe11a37408da2b04e6335ca1e90519eb419f79`；后者为 46808 B，SHA-256 `109174880b47a1333212c6bf6bafe1e5e55b71149348212d0d6698d0b9e1ae8d`。两者不包含新数值数组、数值字节差分或编码替代物。

## 1. 精确删除范围

以下路径均相对于本 topic 的 `notes/`。实施时仍须以 fresh HEAD 的 path、Git blob 与字节数逐项匹配；不匹配的路径不在本批删除范围内。

| 原文件 | 字节 | Whole SHA-256 | Git blob |
|---|---:|---|---|
| 2026-11-13-strong-q122-m28-missing-frontload-vd-response-r2.json | 95885 | 35a06db06cb03d93edacbf024aa748a1b33149795d3a5702e104c2aa9780bca5 | 4d61a0b90ac0eaa6a48f538a13d0e3ad47d5ef01 |
| 2026-11-13-strong-q126-m32-nine-control-response-r1.json | 89971 | 1b4349d08079b77314329f41ef70546cdd61b4ebaa922f3cd6fc935c0f3cf34d | 880c7c61a0a91bcddced9989d8612850c398ce93 |
| 2026-11-13-strong-q126-m32-nine-full-core-budget-r1.json | 47504 | 22816b8cac25e3f2d14f1f967bd6d841d4df771fd3cf13bc8fdd9b9cce87ed57 | 5e8b420bb594184a2387817f5ff0394ef98c3fc1 |
| 2026-11-13-strong-q126-m32-nine-initial-law-tail-pair-r1.json | 52974 | 4476bf812b9377bdce8608a48c1ebcf3f16c5b3a450782a34a6b5c8959609f04 | ecaf374d7bdcd4ea23b67ea4d5f4b6e2d1f611d8 |

源码、完整资源记录、原始配置、port、请求、计划、spec、证明、原始 checkpoint 和切向量数组均不在删除列表中。当前 Fejér 科学族、活队列及全部后处理输入不改。

## 2. 两次真实响应的范围不同

q122 是 M28、1024 个角、2587 个节点的原固定场。更早的八列工作失败后，完整恢复包保留了已完成六列。今回候选 r2 只真正计算两个缺失方向 `initial_speed_frontload` 和 `vd`；原六列未重算。两新列保留全步、半步和对应 forcing，共八个完整数组。实际原 owned resource 为退出码 0，墙钟 1012.5800117710023 秒，峰值 RSS 207464 KiB；报告自身计时 1004.3816365560015 秒是另一字段，不能混写。

q126 是另一真实固定场：M32、1280 个角、2590 个节点，九个物理方向按原顺序完整计算：

`delta, boost_length, boost_speed, vu, descending_turn_curvature, start_acceleration, initial_speed_frontload, vd, descending_sync_curvature`。

该工作保留全部 45 个数组、原全步/半步 forcing、完整矩阵数值反向误差检查，以及所有 prescribed/core-held 组合。真实 owned resource 为退出码 0，墙钟 2086.144046303998 秒，峰值 RSS 282660 KiB；报告自身计时为 2081.053402275 秒。原低三模/物理控制的 3×3 响应条件数是 14054.475612162703，**只属于这个 3×3 交换矩阵**，不是完整 BVP Jacobian 的条件数。

两份报告都记 `inspections=1`、`tail_start_attempts=0`。存储的有限 D–N 导数只在原完整 H 上使用。有限步仍需原完整非线性尾部/BVP与物理审计，不能由这些局部导数免除。

全部标量结果和限制在完整参数台账中逐组保留，全部原行、原向量和原检查仍可从固定 Git 报告恢复。本说明没有重新执行任何数值计算。

## 3. 两个派生读数的准确含义

`strong_current_full_response_core_budget.py` 重新读取真实 q126 九列报告、原资源退出状态、原 accepted 输入和九份完整方向数组，核对全部 32 个 core 导数词。原 62 个检查为真。其准确有理运算只针对保存的二进制系数，不把数值切向量升级成连续 BVP 证明。

原完整轴差公式是 $2\sum c_m$，其中求和包含所有 $m\equiv2\pmod4$ 的已表示模式。原读数为轴差约 0.2506381129076958、短轴处 $\rho$ 约 1.5026607568385948、原 R7 乘积约 0.232735389837827。台账保留全部九方向的轴差、短轴 $\rho$、R7 一阶读数及原数值误差观测；完整精确分数和全部模式在原报告中保全。

`strong_initial_laws_core_tail_pair.py` 只消费该完整预算及其退出码 0 的资源记录。它用保存的全 32 模系数，在频率下限 16、24、32、40、48 上，求
$\Delta\mathrm{frontload}=t$、$\Delta k_0=-rt$
这一维保存线性模型的加权中位数最优配对。原 20 个检查为真，五组结果全部保留。这里没有选择实际有限步、没有生成 warm field、没有证明新几何或新 BVP 合格。

完整原解释还保存在 [旧下一幅度设计说明](2026-11-14-strong-next-amplitude-design-offline.md)。该说明明确区分原 q126 实际核心与理想设计，并保留 outward-turn 标签更正，不能用理想核心覆盖原实际字段。

## 4. 完整源码及导入关系

来源表列出 **46 份本 topic 完整源**与 **28 份外 topic 完整 Python 源**。20 个直接实际 report-source 身份与本次完整读取的源码全字相等。额外导入源按完整字节、SHA 和 Git blob 保留；旧报告未单独记录某导入源版本时，不制造该历史观察。

实际链为：

- anchor/samechart 入口保留原 fixed-response、disk、pulse、monotone/anchor 的完整源与明确变换。
- bounded/fixed/actual/dual 层读取原完整 checkpoint、raw x/y/p、完整 H、tail J、全部 core 与原容差；batch 仍为 48/24。
- 原 disk backend、完整 block QR、径向分批与原 raw reader 保留。
- prefix loader 使用原 numerical-m2、warped/adaptive、flat、Fourier 和完整 Python 导入关系；provider 的 flatturn/excursion/plateau/direct/scan 及明确 hooks 均保留。
- 预算及配对两个消费者保留原完整实现；原 resource wrapper 同样保留。

外源历史标签 `869436630c99aa5a68afb55bd8877c826034d117` 是原源码仓库标签，不能当成本公开仓库的可用提交。公开精确恢复使用 `922382c228b1c8449cf3119a1cd5447185dc512b` 下逐 SHA 对应的完整源；完整 91 条原来源 catalog 仍保留。共同 Python 链与此前完整 q090 来源记录逐项对应，本批只复用这些源身份，不借用 q090 的数值结果。

旧 4,752 B `78718-prefix-tail-geometric-client.py` 的缺口没有被后来的 8,274 B 文件冒充修复。本次响应原源码将 `ensure_tail` 换为禁止启动的 guard，并在实际记录中计数零次 tail start。被加载的 stored client 模块只有在 `WeightedTailPort` 构造时才导入那个外部 client、启动 Node；这个构造不属于这两次完成响应。两种可能的 stored client 及必要 hash-read worker/engine 文件仍登记，绝不把本批来源范围扩成原完整非线性尾求解重建。

## 5. 原始输入与全部数组恢复

来源表完整登记 **109 条原科学输入/切向量身份**。每条都有原 whole SHA、字节数，以及固定公开 Git 对象或既有完整恢复配方。没有读取 gzip、NPY、NPZ 或其他 binary 正文；这些身份来自原小记录并与历史树元数据对应。

原 q122/q126 accepted x/y 文件在公开镜像中以相同完整压缩 payload 的 outer-00 名保留。两份原
`exact-raw-gzip-recovery.json`
配方与原 `strong_gzip_chunk_recovery.py`（SHA-256 `c4b96e8c2d3c401eb7cfe24f6a90d091426a3618623fea045580f179e51daa4f`）均完整保留。13 个源分块都在固定公开提交 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 有精确 path/blob/size。原配方保留原压缩头/尾及原 target SHA；本批只引用既有完整配方，不新造编码数据。

恢复时先按表取回全部源分块，再用原 helper 的四个参数：

`--recipe`、`--archive-topic`、`--output-directory`、`--report`。

原 helper 自己核完整 source 字节、DEFLATE、原 payload 与目标 SHA；它既不重求数组，也不改原 raw metadata。原 q126 实际恢复读回记录仍单独保留。本次只阅读来源和既有恢复记录，没有执行该 helper。

fixed-view 的 p 与 accepted 的 p 是不同的原对象，不能互换。全部旧六列切向量、两新列的八个数组、q126 全 45 个数组以及原 physical coefficient 分块均保留恢复责任。原 tail config 的全部控制数组、数值设置及旧 scratch 字符串不删改。

## 6. 全参数、实际失败与未知

完整参数台账原样保存四份真实 resource JSON 的全部内容，因此全部原 argv、启动/结束 UTC、退出码、信号、wait4、峰值内存、CPU/系统时间、PID与 wrapper SHA 都在。q122 原 owned supervisor argv 和两次响应的单线程环境设置另保全；源中默认值不删。

下列边界继续成立：

1. 最早 q122 八列工作退出码 1，六列的真正完成状态与两个缺列责任保持。
2. 第一次 missing-two 的 tool session 退出码 130，但无最终 owned-child wait4；原因和数值结论仍未知。r2 的成功不会回填这次未知。
3. 原 merger 因 provenance dictionary 额外字段而退出码 1。后继明确 identity bridge 完整核对后退出码 0；两次原状态均保留。
4. 旧六列未保存的 full/half forcing 与直接 combined-half 测量仍缺。后继合并不能声称它们存在。
5. q126 九列及预算/配对都只是局部或保存线性模型结果，不证明有限步、全闭面幅度、reach 或无限尾。
6. 旧 NumPy/SciPy/BLAS 精确版本没有记录。本批不承诺跨机器数值重算产生相同字节，也不新增任何重跑验收门。

## 7. 消费者与恢复顺序

这些文件有真实历史消费者，本批不声称它们无人读取。q122 merger、identity bridge、followup collector 会读两列报告和全部原数组；q126 budget 会读九列报告与原资源；pair 会读 budget；旧设计说明引用两个派生结论。源码和参数引用不静默改写。

重用历史流程前，先从固定 Git 提交恢复被删除的完整 JSON 到原相对路径，再按来源表恢复全部 companions。恢复旧完整结果可直接使用：

`git show 693d9e3bf30f1822e735bf1aa15c3aca4838340b:<完整仓库路径>`

原文件身份按本说明第 1 节全字记录。任何旧路径的新重算输出须有自己的实际字节、时间和来源，不能贴上旧 SHA。这里提供的是恢复与完整再生合同；本批没有运行它，也没有把它设成新科学入口的门。

## 8. 实施边界

本批仅保护未引用完整文本 blobs。未写 ref、未改队列、未执行科学/AST/fixture/benchmark，未读取任何 binary 或大于等于 100,000 B 的正文。此前 RET59–74 的删除不重复；缺原 writer/参数的 phase/segment、Nelder 旧驱动差异、唯一 port、parent91、保留 canonical 与活材料均继续保留。最终新增字节与净释放量以完整 delivery manifest 为准。
