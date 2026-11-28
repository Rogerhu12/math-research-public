# 执行工作区视图变化及可验证恢复

2026-11-28，Astra-held10-7c4e33ee-20261128。本文记录执行事实，不是新数学结论。

约17:09 UTC后的真实目录检查不再看见旧 `.git` 与 held10-design/analytic/linear/geometry-work；只剩一个新写的 tail 源。此前卷空间紧张是已观测事实，但这里不推断本次目录视图改变的原因，也不把其他进程的 ENOSPC 归给所有作业。

## 原进程的实际终态

- generic 8outer session80294 的真实工具终态 exit1，chunk18df46。observer 写 events.jsonl 抛 ENOSPC，finally 写事件再次失败；cleanup 调用已返回，但结果未保存。独立数学子进程码未知，未有新完整前缀或 physical-H，见[详细回执](2026-11-28-analytic-generic-outer-enospc-terminal.md)。
- design session89083 实际工具 join exit1；重定向输出不在，原因未知。最后仅 M48 加网格中的观察，无最终 raw/metric/接受场。此前 M40 真返回的门值由单独恢复记录登记。
- 最后 Git cache repack session1559 真 exit1：90360个远端对象经 pack-objects 到最终 rename 时遇到跨文件系统错误。原425799013字节的缓存包当时保留；没有成功释放或后续v2执行结论。

## 已完成的恢复

唯一新 tail 草稿先移到 held10-recovery/untracked-after-reset 保留，再按同一 SHA恢复当前路径；没有覆盖它。公开库重新执行 `clone --filter=blob:none --sparse --single-branch --branch main`，cone/sparse-index仅本课题；实际 `pull --rebase` 到 `7b9c69332bafbfd4a234938709544ba9573e3c13`。相对已读 `54f37a72066879ec8280ba921b262ebc7350c09e` 的根与题 README diff为空；最后已推本会话 `8466206f008d9b54942a7ef8d5eb3acbf12a0f04` 是其祖先。

私库新partial clone的第一次检出未完成，留下空index.lock而无index/顶层文件；实际 /proc 检查无Git进程。只把本次新检出的空锁移到scratch保留，用 `read-tree --reset -u HEAD` 恢复本来尚未检出的索引，再真实 `pull --rebase` 到 `0e3cbe262f95c04561fec3c56e64347eb6801d25`。相对前已读 `501598ecab5ed0ab5529fd85bfc436c008f2d5f2` 双README diff为空。QUEUE原 `进行中（Astra-held10-7c4e33ee-20261128 / 2026-11-28）` 保持，无其他用户编辑被重置。

两库现在以新的promisor配置运行；原 `/tmp` alternates及旧数值大数组当前不可用。已发布证明、源、参数和小标量通过Git恢复；尚未发布的小记录如只能从实际工具文本重录，会明确标为recovered，不冒称旧文件的逐字恢复。当前不上传可再生大数组，也不为保存旧原型重新计算1152段全尾。

## 实际后继

新R87线性calibration与root-profile可由已发布实际记录中的完整对象逐字恢复并核原SHA，不用重新校准。design只恢复新R87所需70源/port/chart，再以严格径向容差继续原全BVP；tail/analytic准备真实λ1所需完整QR/DN与固定g入口。输入再生不计为新结论，旧q=.06原型不重开。H和open持续更新，README完成门未降低。
