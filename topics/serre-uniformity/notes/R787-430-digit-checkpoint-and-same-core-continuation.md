# R787 — 实际430位断点与原核立即续算

日期：2026-11-15。状态：实际完整Dixon提升至430位，原特征零A/B关系尚未恢复。只延续原同一个自由列1186；未换函数或重算旧模阶段。

## 真实退出原因与最新已完成阶段

公开run **43708449812**、job **132794639922**、source **ac5998f333ab49c4747874e2e44b7ca4ccfa3acf** 的原core receipt准确记录 **BudgetStop: All completed R787 stages remain available for exact resumption.**，process_exit_code为1。末次完整提升是430位；随后第431位的residual内触发预算检查，未把部分阶段当作完整输出。原core SHA256 **93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04**、wrapper **42157e0d95eb5d9aed28ef828a86dc5e7bec89e806e3e0a92aa0bcb1a36988b6** 保持不变。

- 真prime 1000000753、Schur rank1186、自由列1186；原14分支、原chart/selection保持旧字节。
- 最新文件 R787-prime-1000000753-dixon-00000430.json.gz，**60765868B**，SHA256 **00855d88fec4c18ec7cbfd4927dd72042d8e0372d1ac95498a0e5fcd9f118029**。
- previous_completed_checkpoint_sha256为 **b3112803e06aeee282cb4b7074d67dac8d4f186b7cb61cf66811365c1ac15685**，准确指向历史中的429位；完整name/bytes/SHA/prime/digits历史保留430条。
- 最新lift的complete、原configuration、chart SHA与full_original_modular_relations_verified均真。没有成功关系证书，不把这些模提升写成特征零A=yB。

## 新产物与最小来源读取

原artifact **14170087848**，名称 serre-global-R787-original-power5-function-relation-43708449812-1，ZIP **438780485B**，平台SHA256 **b6ec1bf53540cd59e69309e445ef15a44e0dc64e9f298d2a065609647ea82340**，到2026-11-16 16:25:10 UTC有效。

full-outputs-manifest.json为 **430709B**、**1262**条，SHA256 **1b92c4e594f4d1d14cfd4b62fda8513511dc879a7c6e2c7d9f60de52dd5ca689**；ZIP有1264个常规成员。原输入续接包为 **123713383B**、SHA256 **2f4371c94e36372b2eeb9291d75479ccbe2432abe741dc9ecbebab78e9046e92**。

最小纯IO run **43737168117**、job **132882214571**、source **2ed145250f20b789242ef64fc2d5ccb9ee876c7f** 已success。脚本 **c2d47380fd8d5012db5e9fdf6054bb0145329ac242ecb25f075af8dc19c4b3e8**，请求 **450026eeae7f89a049d7f99a4e1659d259d0ba2150376f9b06c507768998511c**。实际73次HTTP Range传输60987636B，核manifest、真实run/core receipt、原日志尾、chart/selection、历史和唯一最新完整lift的字节/hash。它没有重新哈希整个ZIP或14个旧大分支，未执行数学。

小IO产物 **14170623079** 为624249B，平台ZIP SHA256 **4a9e50831b901103760c85c52b58a0d9ba6e613a86754eb2deaeacb77f857725**，到2026-11-16 16:44:59 UTC；原60.77MB完整lift只在IO临时目录读取，未复制进该小产物。raw、manifest和机器证书全部留一日活跃artifact，不入Git/Release。

首IO run43737007567仅在错误比较历史和当前root README时停止；历史source ac5998f3的根README为c6db597c，当前根6979d793是已读合法更新。修复分别固定历史两README与当前规则，不改任何数学对象或来源。此失败不被计作数学失败。

## 同核续算

当前R787请求只把resume换成上述新原产物及真实manifest，其余原retained_artifacts、proof、method、core、wrapper、每8位重构和300分钟预算保持。原workflow只读规则基准更新为最近已读 **506de085110d7249a7641b13e0b8cd715ad3cab9**。新运行先实际partial clone/pull --rebase并比较两README；恢复新包的全部来源字节后，从430位继续，不回退旧259位祖先。

一旦实际129×280原关系终验成立，接原R792/804与R809 A/B正规坐标；当前不预填beta、极除子、eta或高度。完整正规化子全p主目标仍OPEN。
