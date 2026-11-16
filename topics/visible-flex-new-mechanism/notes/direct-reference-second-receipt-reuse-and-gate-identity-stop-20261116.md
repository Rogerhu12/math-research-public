# 直接reference第二次：九项收据复用、积分阶数修复与门身份停止

日期：2026-11-16。本稿消费已完成公开 Actions 的原日志和原 gate 源码；没有执行研究或重跑开发检查。

## 来源和已经走到的位置

- Run：[43778983026](https://github.com/Rogerhu12/math-research-public/actions/runs/43778983026)，job `133011642024`。
- 请求提交 `439fe8b9b8fc9cffdfdb9d8cf01acc6687e0a48c`；40389字节/SHA256 `52645511b072a72ba2d8498094893dfe9a4dd4c87255c252ba416577987800e5`，161绑定。
- 本次 audit 41328字节/SHA256 `8008a7f92024bd745107784647fd1502a78ab3c5978dba3221abbebc66fc4eee`。
- [首次九项](direct-reference-first-nine-checks-and-entry-field-stop-20261116.md)的完整通过收据认证成功，本次新开发组、检查和开发执行时间均为0。
- 原物理对象的积分阶数准确为8，与其 fixed primitive 一致；没有补默认值或改变求解器配置。
- 新 objective 与信息迁移构造完成。原438法向顺序及精确值保留，四支持仍分离；学习的8个祖先事件、7次提交保留，新事件和新提交均0。
- 首次ordinary求值之前，原 gate 的严格身份检查停止。因此新 adapter 的 geometry started/completed/failed均0；shared values、J、模型、LP、SOC、trial、接受均0。没有新两网14门收据。

报告总状态为 `new-task-stopped-before-two-grid-initial-point`；外层准确状态为 `direct-reference-guarded-recovery-error`。原错误为：
`height primitive or exact-polynomial evaluation changed during this stage`。

## 失败的准确身份域

原 `FiveNullHeightGate.assert_context` 依次检查坐标、原163物理 gate，最后比较当前 field 的 evaluation definition 与构造 gate 时冻结的 definition。此次 transfer 在 wrap 成新 DirectReferenceFiveHeightField 之前，已经为原 FiveHeightField 建好 gate，故这个 gate 仍冻结旧 ordinary definition。

原旧field身份为
`047cefae968152d170387cf64a9f7b0f132089685472c10868de9379967d93e9`；
本次新field诚实身份为
`8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1`。
这两个不同身份被原检查正确区分。不能为了继续而删除检查、伪造旧SHA或把新的 definition 写进旧冻结对象。

原 `FiveNullHeightGate.from_original` 是正确接线入口：从同一个原163物理 gate、同一个新adapter及原163上下界，构造新的159数值 gate。其物理定义、原目标/高度/零行、坐标/reference和原163盒/159外界必须逐项保持；只有新ordinary绑定对应的数值身份变化。该构造不调用几何或优化器，也不重建数学 null basis。随后仍须执行完整原 `assert_context`。这项修复尚待下一实际验证，不能称所有门已过。

## 已通过的信息迁移与尚未绑定的工厂

新 ordinary/factorization身份分别为：

- ordinary：`8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1`；
- factorization：`b6cc198b6b58ec0484438c910a1e05a1273bc0cec81715415b8f538d31661963`；
- controller初始化前objective：`2054461cb51de57228abfda93178db15e37bf3655b7d77a9eadbb7d260171b7d`。

原坐标身份 `b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580` 不变。两网点数61440/122880、原池4432/4525和版本1/2保留。

原方向条目JSON身份仍 `994b060771400b8f5f4aaadb8dcaba954467323bec2299a324e7e9a1a1e9097b`；其fresh context只按合同改变factorization definition。新初始bank状态
`7ef2c21e2ea0459a389295006c7085441df8f334d23fc1998d0665df9e271793`；
438条、旧累计insertions626/evictions0/rounding309只是保留历史，新增事件没有发生。首次实际 complete factory 绑定仍pending；构造阶段检查通过不能冒称工厂已验证或模型已运行。

学习系数仍为17.022353404161095/18.064283125328743；新context state为
`0e5987eded28899681c896b41092c84e9625ff54db328046fae8f6f442e17fa1`。
新primary build/sample/commit均0，没有用旧事件重新训练。

## 同一科学时钟和完整费用

| 本次及累计成本 | 秒 |
|---|---:|
| 已花费首次科学时间 | 13.756976061000046 |
| 读取首失败日志并验证九项复用 | 0.7406144009999593 |
| 读取原guard源日志及收据 | 1.1635926829999903 |
| 必要24输入及不可变准备 | 12.618949095999994 |
| 本次科学输入准备合计 | 14.523304177 |
| 新constructor与信息迁移 | 0.18610186600000134 |
| outer至身份停止并返回 | 0.12079245400002492 |
| 本次新增科学耗时 | 14.933360237999977 |
| 同direct任务累计科学时间 | 28.690336299000023 |
| 本次总进程 | 16.883830578999948 |

本次科学读取前的导入/源码等为1.9504703409999706秒，独立记录，不再加进已定义的科学预算。峰值RSS296988 KiB。

下一入口必须直接继承累计28.690336299000023秒，不能再把首次13.756976061重复相加，也不能把本次总进程全部重复计入科学。全部前次流程、准备和错误保留；值/LP实际仍0。旧已关闭的m7 epoch active241.3142038439999、init293.5427817930001、LP10、values15继续只列祖先账。

已验证的九项收据可以沿本次明确的只读验证链传递，下一无需再次执行九项。必要的本次失败日志读取和原guard状态恢复仍要计入同一个1800秒科学钟。64LP/160值/原14门、B=1/4000双streak0不变。

## 原日志、输出和 actual pull

原log208955字节/SHA256：
`68d723fd4132084e61f20b96fa3012e00e44b325a83c797b266be0046063e86c`。

按JSON加LF记录：

| 标签 | 字节 | SHA256 |
|---|---:|---|
| DIRECT_REFERENCE_REQUEST | 26904 | `8029a35a421d93d57a90ea575fd10062e9d66fd69c64602c2a8870f664165881` |
| DIRECT_REFERENCE_DEVELOPMENT_REUSED | 2298 | `ac54fae177ec63e7e232048731c651b5a306420e28d4080728dc7e99c37127f6` |
| DIRECT_REFERENCE_PRIOR_WORK_REUSED | 1135 | `46480623a3a683dd1a202c9b1f2f47f7105ca43580c5e64d85aa1546a1944661` |
| DIRECT_REFERENCE_COMPLETE | 99050 | `8731e263ea059b0069260cd1e1774ddedb321226ab6cd29f4ca5d2084d7fb989` |

Runner临时audit3584509字节/hash `8e9c4bd7723e15cdc9286ea7b41dcbad0cb442c0402d68d82f198c9c8886b52d`；summary115315字节/hash `dd45f533fb74985c158e2f1bc5bf054725ee1feb391c5c4aa85a57747017c00f`。没有payload进入Git、artifact、Release或跨run缓存。

该run公开actual pull为00:12:48.467351—00:12:48.844193 UTC，前后 `439fe8b9b8fc9cffdfdb9d8cf01acc6687e0a48c`，根/题README空diff。私有00:12:50.890185—00:12:51.463416，前后 `bf70a6eb1eb8635cad2cf7f0945333c55f4a676f`，根同、题README无、QUEUE本会话进行中。root00:15:39读完。后来R410推送的并发已另在纯规则run43779613612实际rebase并复读；HANDOFF按最新00:18记录，不回退为本节较早提交。

## 接下来保持的范围

只把新adapter绑定到一个按原构造器创建的新数值 gate，核同一物理门和精确边界；完整原freeze检查继续存在。随后在同一个任务剩余预算进入尚未发生的首次真实两网ordinary，再复用同进程缓存供J/模型/实际步。当前仍没有真实冷加速、优化下降或主课题完成证据。
