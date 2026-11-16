# 已成九块输入清单的原字历史恢复

状态：完整小摘要与原收集脚本已读；本次只清理既成衍生清单，不计算科学结果。

## 删除对象与完整身份

根README规矩15适用于既成数据及其衍生档案；旧源中永久保存的措辞不构成现行例外。为后续新数学consumer保留完整输出预算，本次普通删除当前副本：

- 路径：`topics/visible-flex-exact-nearby/notes/2026-11-12-missing-complete-input-archive-files.json.gz`。
- Git blob：`fe069a3e65f468d73ea017d189fb27096a1414fa`。
- 压缩文件原长度：327445 B。
- 压缩文件原 SHA-256：`9f7bb67ed6177bb4c6f57356ccb26e30a75fdaccbee9e85f01c761a531c61914`。
- 可精确恢复提交：`dae38ffc6458849cd79a9c99b146b7f3114c6e2b`。

本次只读Git-tree元数据及下述完整小文本。没有经connector取gzip内容、解码二进制，亦没有调用原collector、ODE、密度或任何科学程序。Git blob和长度取自上述不可变提交的元数据；SHA-256取自完整原摘要，不冒称在本机重算了gzip哈希。运行中的WPS36 current/19历史、已成WSM20及WRP所需五个完整actual均不以这个清单的当前副本为输入。

## 原始收集的确切范围

原摘要 `notes/2026-11-12-missing-complete-input-archive.json`：415 B，Git `d6d7b7832f52e8470334ed1fe177bc9bf63598f1`，SHA-256 `a4f7bc2f0adcd7bad8b261cf67b1ca5250dd809cc1953feabc246a563ab232e3`，保留当前副本。摘要原文给 `complete=true`、九块、6794个文件、原收集总字节241928707、上述inventory path/hash、`no_density_or_ODE_recomputed=true`、`no_reference_cache_added=true`。这些是2026-11-12原收集的范围，不是当前topic容量或当前仍存在文件数。

原脚本 `scripts/fourfold_ci_archive_missing_inputs_v1.py`：4203 B，Git `abf9107b1a3dbcd8a726a59364c7cabc9ac0e95b`，SHA-256 `78677ba1ed88e0aed6ff12d8c8218cdd80b24623adedf3f13c001c9b41db2a71`，与完整摘要的source SHA一致，保留当前副本。原程序从固定 `ARTIFACTS[5:]` 收集缺少的九块，前五个density块已有；用原intake核source/report/files清单，对块目录下各原文件检查长度和SHA，并保整个block manifest和原inventory。大可重构reference cache与已等同的tracked文件不重复添加。压缩清单保完整 `original_artifact_intakes` 和排序后的原文件记录；它是既成输入的索引，不是新算的density/ODE结论。

415 B摘要没有原run号，本页不猜测。具体原artifact/run入口以历史清单内完整intakes和原收集证据为准；必要时在公开Actions临时读取完整原清单。不把小摘要替代完整6794条身份或任一原block资格。

## 精确恢复及后续义务

只在确实需要时用 `git show dae38ffc6458849cd79a9c99b146b7f3114c6e2b:topics/visible-flex-exact-nearby/notes/2026-11-12-missing-complete-input-archive-files.json.gz` 取回原压缩字节，在公开Actions临时验证327445 B、Git blob和完整SHA-256，再按原格式读取。禁止重跑原collector或重算既成科学以替代原字恢复；禁止把解码后的大表或二进制放入对话，禁止为了传送而切块/编码。

本次只删上述单一衍生清单的当前副本，不删它引用的6794个对象，不改变原block成功/失败、域、边界、mean、参数或任何旧失败记录。未来若清理其中某一原对象，须记录该对象自己的不可变历史身份。原题全部未付数学门保持，当前工作继续，不添加批准或复算流程。
