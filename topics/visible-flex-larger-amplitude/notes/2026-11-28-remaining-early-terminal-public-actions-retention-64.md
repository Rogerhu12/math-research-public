# 第 64 批：其余早期终态运行的完整发布记录恢复

2026-11-28，UTC。本批按根 README 第 15 条和 root 明确的旧生成输出整理指令，保全后退出现树；不运行科学，不改 source、参数、活队列或 refs。此前 ret62/63 的删除对象不重复。

## 1. 唯一范围

固定恢复提交 `43a5d2a100a8a74a57d9527a6bab51afb1f16faf`。本批只包括下表 14 个完整 index/parts，毛退 323489 字节；每个原文件均小于 51000 字节，已取得完整文本与真实 SHA-256/Git blob/字节数。

| 请求标签 | 实际 run/attempt | 文件数 | 字节 | 已刊实际返回 | 官方终态 |
|---|---|---:|---:|---:|---|
| 03 | 45811843606/1 | 2 | 40656 | 6 | completed/failure |
| 07 | 45909290354/1 | 2 | 35672 | 3 | completed/cancelled |
| 08 | 45929088658/1 | 3 | 101026 | 10 | completed/cancelled |
| 09 | 45943410994/1 | 3 | 80376 | 7 | completed/cancelled |
| 10 | 45972294636/1 | 2 | 46537 | 4 | completed/cancelled |
| 11 | 46000835895/1 | 2 | 19222 | 1 | completed/failure |

这里只退原控制器生成的公开小输出。六个原完整 terminal notes、全部 source、request、queue、参数 archives、完整历史输入与准备好的后继都留树。19 以后活输入及返回不动。没有读取任何大于等于 100000 字节正文或二进制正文。

完整文件：

- [source/parameter registry](../computations/remaining-early-terminal-public-actions-retention-64-source-parameter-registry.json)；
- [complete provenance](../computations/remaining-early-terminal-public-actions-retention-64-complete-provenance.json)；
- [complete delivery](../computations/remaining-early-terminal-public-actions-retention-64-complete-delivery.json)。

三份 JSON 和本说明均为完整小文件；交付表列全新增/删除项及净字节，root 逐项按最新树中的精确 path/blob/size 普通提交。

## 2. 完整原记录和参数

31 个已公开 stage JSON 均有原完整分卷、one-based fence 位置、原字段集合、原 seconds 字面和完整原 JSON 文本 SHA。25 个 followup 的全 argv/entrypoint 与至少一个现存完整 step 逐词相等；对照只逆回原 `{repo}`/`{work}` 路径替换，没有改动任何数值、顺序或数量。六份 warm 返回按原完整 warm recipe 和全部输入来源恢复。

15 个实际队列版本和 25 个实际 entry source 版本分别保原 commit/path/SHA。后来同名文件不被视为旧版本。完整现有 07 stages2–3 参数归档、08四份返回归档、09四份返回档及旧 header、10完整 returned-input queue、11完整16词/10输出/36选择器的 ready 均保持原字。没有把未返回的科学/纯读/费用对象归档成完成，也没有删其预算和未知历史声明。

共有 45 个仍在现树的完整小文件身份直接登记。共用的原 warm、accepted099 输入、原 followup/compact-followup 全源及完整参数由 [ret63 registry](../computations/early-terminal-public-actions-retention-63-source-parameter-registry.json) 精确 whole reference 复用。该复用只涉及来源与恢复合同，不把不同 run 的 warm、chart、固定目标、点、物理值或证书等同。

## 3. 原 03 请求不能被后来 03b 同名文件替代

原 03 index 内完整 request JSON，加其原文件末换行，真实 SHA 为 `73c79a654916390ccc38f2716b67d073a1cd8752b3e101b9e122feb9d17cd2be`，1480 字节。按该全字生成的 Git blob `11823bb03d7638b3856c153c20f166cd9d2508e3` 已从远端完整取回并逐字吻合。

其原恢复位置是初始执行 commit `4d8fbb0322308ed6849b64f8a92d6bd1215b7bfd` 的 `computations/resume-20261126-actions-request-03.json`。当前同名 request 已改为03b，完整 SHA为 b33c…；后者照旧留树，但不能覆盖前者实际执行身份。此项是完整旧请求恢复，不是构造新的数值输入。

原 03 控制器的 render 全文与原 parallel02 一致，07/08/09 compact render 与已留 compact03b 一致；10/11 有真实有界 progress 发布，二者对应 render 全文一致。所有六份实际 controller SHA 均与原 index 中实际加载值相等。

10/11 progress helper 只在明示参数下读小 scalar 文件，两次有界完整读取必须同字；95000 文件字节界、8000 公开字节界、原最多48个selector及实际错误均保留。它不完成 child，也不替代 report/final/root packet。最后 progress 可以说明当时观察到什么，不能证明 accepted 或完整科学结束。

## 4. 两类发布失败不能混为一谈

### 原03：子进程自然退出，科学结果仍未知

[原出版失败及完整恢复说明](2026-11-26-actual-publication-failure-and-complete-recovery.md) 全文留树。原 stage6 v2参考确实成功。stage7 科学 child 后来已经自然退出，但原控制器在 `finish_record → publish → render` 的58000字节 compact 界限处失败，返回 event 原来排在 publish 之后。因此没有公开该 child 的 returncode、report、final 或 Phi；成功与失败都不能推定。官方 failure 不能代替缺失的科学退出码。随后03b是明确新run/新请求，不回填03未知结果。

### 原11：输入真实 exit1，随后才发生发布失败

[run11 输入拒绝及发布失败说明](2026-11-27-run11-fixed-reference-word-mismatch-and-publication-failure.md) 与 [完整已备 solver 及失败说明](2026-11-27-same-run10-complete-solver-prepared-and-run11-input-failure.md) 都留树。公开 part 只有 warm1，但终态原日志另有真实 input2 返回事件：6.170325379000019 秒、code1、5149字节报告 SHA `3a5506df1182aa292aa1ecb28a5ea07e14ccd0bbc163e195fe4b68afa5902d2e`。实际 error 为完整 mesh/chart-word 合同不满足；physicalF/J/roots均0。之后 HANDOFF10000字节 guard 才阻止提交新分卷。

provenance 完整保该真实 event 的原 JSON 文本身份和全部 event 字段，并明确它不是补造的已刊第二分卷。5149字节完整报告没有在本批读取；event 的 scalar 选择器不能冒充全文。复合 word guard 没指出哪一子句失败，因此不能记成已观测的某一个 chart 系数差或某个新完整 chart hash。没有 same-g bridge 成功、完整 reference、final 或 typed 重建。

## 5. 07–10 原科学未知边界继续有效

- [07完整终态说明](2026-11-27-run07-terminal-cancellation-and-unreturned-full-normal-field.md) 保留必要输入1–3真实0及旧dc5 carrier完整再生；cc0a科学4与后继pure/费用/M320未返。05:02:15是终态观察时间，05:00:28是API updated_at，都不冒科学结束时刻。
- [08完整终态说明](2026-11-27-run08-terminal-cancelled-with-unreturned-complete-field.md) 保留先前全部真实失败，以及9投影读取/10独立7c目标冻结成功。95559科学11、pure12未返；旧90、独立7c和actual09各自身份不迁。
- [09完整终态说明](2026-11-27-run09-terminal-cancelled-with-unreturned-complete-field.md) 保留输入1–3、原科学4/pure5失败、trace6–7。ff544修后科学8与aee22及所有后继费用未返。当前1995叶与旧2397 carrier责任分别保持。
- [10完整终态说明](2026-11-27-run10-actual-terminal-cancelled-with-unreturned-science.md) 保留四个必要返回、actual2218及tolerance_reached=false、旧2397、全部43条原末次progress和149/7/32全argv。c3dc科学5、2efa和all-batch费用没有完整自然返回。进度点、缓存计数与零记录failure不推出最终13成员、accepted方向或连续证明。

所有最后点、根、控制词、完整 report/final、typed首发现顺序、保护晋升和取消原因，未返回的仍未知。它们不是空集，也不会因官方cancelled失去适用历史责任。不同目标的后来Fejér研究不冒这些旧分支的完成。

## 6. 同一路径的不同历史分卷

旧科学输入和纯读者有时绑定的是一个分卷的早期版本，而不是最后发布版本。本批 registry 逐项保留11个这样的原参数记录及其原文件位置，例如：

- run08 `part-002` 的 a145bbec… 版本为37303字节、blob `eb0fab203d187e4498983eb30a08c574827311d1`、SHA f3a69d…；最后现树版本为45797字节。
- run09 `part-001` 的 ed58d589… 输入版本为33693字节、SHA837901…；最后现树版本为47299字节。
- run10 returned-bootstrap 记录保自己的原 input-stage分卷/queue提交；原11完整argv还读取原run05历史公开记录，该记录的版本按ret63固定合同恢复。

不得把这些身份替成最新退存分卷或仅说“同路径所以相同”。需要恢复哪个版本，取决于该原 consumer 的 complete source/parameter/binding；现树删除不修改此规则。归档中旧index不同时间的SHA也不被最新index覆盖。

## 7. 恢复及适用范围

对交付表每个删除项，直接 `git show <fixed_restore_commit>:<exact_path>` 或按明确 Git blob 取整字，核同表内完整 bytes/SHA-256/Git身份。历史科学 source 用其 actual_checkout_commit:path；队列用 actual_path_commit:path；原输入使用它自身绑定的历史whole版本。旧读者先 materialize 所需整文件，不能把新摘要放回旧路径冒原体。

原始 public JSON 的完整数值字面、全部 inputs/outputs/scalars/errors/cleanup 和参数通过原整分卷及 fence 定位保全。原来仅在runner的NPZ/大报告/全日志，不能由hash反造，也不宣称仍存在。重新科学计算产生的是新实际返回；本批不重跑、不设置新fixture/重放门，不用重跑来恢复旧时间或身份。

root 只对本批14项作普通现树删除；其他当前旧完整source/params/proofs/真实结论留树。本批净容量见完整交付表，不是科学进展、认证、收敛或问题完成声明。
