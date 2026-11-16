# 固定 f93 的完整引用审计与九件历史行政记录保留方案

作者：amplitude（GPT-6 Astra Pro，AI 辅助）。日期：2026-11-16（UTC）。

**可信度：已核实的行政源码、文件身份与固定提交的完整字面引用结论；没有新增数学或数值结论。本文记录可移出 main 的精确集合及恢复方式，不充当已执行删除的收据。**

## 1. 结论与范围

在固定提交 [`f93b079e400c336f12751728ba388d6a9e769779`](https://github.com/Rogerhu12/math-research-public/tree/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/)，可以将下表的 **九件历史行政记录作为同一集合从当前 main 移出，原字节由固定 Git 历史保留**。其中四份旧 inventory 与一份 relocation receipt 合计 1,215,494 字节；四份与它们配套的 archive manifest 合计 8,396 字节；九件共 **1,223,890 字节**。新增本文这份小索引后，净释放量为该总量减去本文及实际提交的其他小型索引增量。

完整字面扫描中，五份大记录的唯一外部引用均在这四份配套 manifest 内；四份 manifest 自身没有其他路径、basename、blob 或 SHA256 的字面引用。一起移出九件可避免在 main 留下这五份文件的配套 manifest 路径引用。四份历史行政 producer、仍存在的小型 resource／说明文件，以及全部科学输入和源码均保留。十一份另查的历史研究 log／results-index 本轮不选，合计 993,753 字节也不计入上述释放量。

这不是改写历史、重新生成科学输出或删除真实运行输入。九件仍能从同一固定提交逐字取回；不需要重新运行任何旧清理脚本。固定 f93 之后新增的真实消费者不在本次扫描的量词范围内；实际普通提交时应保持对当前路径身份和已知新引用的真实绑定，不能把固定旧扫描说成对所有未来提交的保证。

## 2. 实际行政运行与完整读回

首次临时行政运行 [43864989681](https://github.com/Rogerhu12/math-research-public/actions/runs/43864989681)，job `133291129942`，在调用 `rg` 时出现 `FileNotFoundError: [Errno 2] No such file or directory: 'rg'`。该次没有完成引用扫描，也没有删除文件。其 connector 返回文本经 UTF-8 重编码的身份为 35,205 字节／`0e16c970f6e09f5e09eb9210e61707c21f40a0d9ff05b268abf94d8c5ca9bac4`；这不是 HTTP 原始响应字节身份。

第二次临时行政运行 [43865360393](https://github.com/Rogerhu12/math-research-public/actions/runs/43865360393)，job `133292401375`，**实际完成并成功退出**。工作流来源为 `a74562c9cc2a9f9ca2cba3e0f0e7d6243900bbdf`，临时分支为 `visible-flex-larger-amplitude-retention-audit-r2-20261116`；工作流 14,579 字节／`f2c9705af10e43cf3583b6e2ec8b2baa348b65709dac1fd649179b6b681edb88`。工作流只在临时行政分支，未将这份审计执行文件加入 main。

本次实际扫描对象始终为 f93，不是临时工作流分支的代码状态。其根树为 `a16124cc7655d2a6671818480cf7002256e2cb98`，topic 树为 `d896258eb83f0935c8a592d0277ff01ee22a1aea`；此前从官方未截断 tree 读取的 topic 规模为 9,411 blobs／199,531,170 字节。实际完整仓库跟踪文件数 **55,367**。

扫描程序先检查 `rg`。实际环境缺少该可执行文件，故按明示后备执行：

```text
git grep -a -l -z -F -f <RUNNER_TEMP>/historical-retention-audit/literal-patterns.txt -- .
```

随后对所有候选命中文件按原字节提取每个模式的全部行与字节地址。模式共 **88 个**：20 个候选各自的完整仓库路径、basename、Git blob、实际 SHA256，共 80 个；另加四个行政 inventory schema 与四个 producer basename。返回 **30 个匹配文件、47 个匹配行**，包括所有原文件/行身份、匹配模式及原字节偏移。全部代码匹配的必要上下文也返回；不把每个大原行正文整体复制进摘要。

唯一终态读者已完整读取本次必要 JSON，**32,263 字节／`087ae414463a87927807144dcd2df02e7ae1135c58770a166c5dc3a825750087`**，包含末 LF；没有超过单份 90,000 字节，也没有把超限正文拆开返回。BEGIN 与 END 帧位于该次日志物理行 320 与 322，正文完整一行。返回日志文本经 UTF-8 重编码的身份为 **66,665 字节／`510b3b7cfb4caf72bce114809435048a78cae5e5da01e76a437356fff98bad20`**，同样不声称 HTTP 原始压缩字节身份。两个实际终态日志均只取过一次。

原摘要的以下事实均为真：`checkout_unchanged`、`complete_literal_match_addresses_returned`；以下事实均为假：`scientific_commands_executed`、`scientific_logs_fetched`、`files_deleted`。这里读取的是行政审计日志，没有重新读取任何科学运行日志。没有运行题中科学源码、数学值计算、import、AST、编译、fixture 或 benchmark。

### 2.1 双 README 来源

固定 f93 实读根 README：10,233 字节，Git blob `21bd547f56590b7f2dd279d0297efb289a9b2783`，SHA256 `6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9`。topic README：2,664 字节，Git blob `bff8aea253a9e6a7a4fac28d810ac454c5499fec`，SHA256 `3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d`。本次只读审计没有更改它们。

## 3. 精确九件集合及固定历史地址

以下路径相对于 `topics/visible-flex-larger-amplitude/`；每个链接均固定到完整 f93 commit，不能替换成浮动 main。

| 路径及固定历史链接 | 字节 | Git blob | SHA256 |
|---|---:|---|---|
| [notes/2026-11-13-strong-current19-readonly-relocation-r1-inventory.json](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-current19-readonly-relocation-r1-inventory.json) | 398006 | `79058a799741ae0657ac8e868bcab419a8b4dd6b` | `576c1241bf6223f0b121fe279e4e0743e6796a0303aae9fcbf521b88bbb2a2a8` |
| [notes/2026-11-13-geometry-old-derived-array-cleanup-r1-inventory.json](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/notes/2026-11-13-geometry-old-derived-array-cleanup-r1-inventory.json) | 217969 | `160ea730247cd2d9f9fa4fd83dcfabdfaecb0f49` | `32a5d39a35966823a3635c336889ab0db26f4735bd8af37c5f801439406f7627` |
| [notes/2026-11-13-strong-old17-derived-geometry-cleanup-r1-inventory.json](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-old17-derived-geometry-cleanup-r1-inventory.json) | 215431 | `0601d83451884067ded17cddcd66c0e2d5bcbc68` | `c6ebab4327f3510a6d2162aae5b9f3aabb38a626b330cf53c6d4aae4a6817aa3` |
| [notes/2026-11-13-strong-old-m32-q122-derived-retirement-r1-inventory.json](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-old-m32-q122-derived-retirement-r1-inventory.json) | 183331 | `33a90988abb73bcb02149844955d6e0ba8187b07` | `27df4591b1f19ec2b9a5372fd21b60e537feec8f432a0e3df5a3e904d55b1d91` |
| [notes/2026-11-13-strong-current19-readonly-relocation-r1-receipt.jsonl](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-current19-readonly-relocation-r1-receipt.jsonl) | 200757 | `e0fe5574ec660960b8a440d30d8bdb44723db8b0` | `87a31137ec0e101cc38e5654ab8ace64261caaf8a004464ee1c88ff05fa58f1b` |
| [notes/2026-11-13-strong-current19-readonly-relocation-r1-manifest.json](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-current19-readonly-relocation-r1-manifest.json) | 2459 | `6c4473854198b74e05328a5a6b100c29aa36031c` | `fc401944be504f51543c03b01614494104da9ab569859aa8333db3bfc5f33d89` |
| [notes/2026-11-13-geometry-old-derived-array-cleanup-r1-manifest.json](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/notes/2026-11-13-geometry-old-derived-array-cleanup-r1-manifest.json) | 1258 | `d6a24079271b0ceea14b2165ae23f1144d2ca033` | `09805be24bb057013abae69f1a8da7c5f8bd9d6bd906152772524ff1afb59123` |
| [notes/2026-11-13-strong-old17-derived-geometry-cleanup-r1-manifest.json](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-old17-derived-geometry-cleanup-r1-manifest.json) | 3133 | `79a9f073e101258743bbe0aaf86997f0dc223f6d` | `77ee4d2802f23f8e9b1e93b81c62738bd0f1374c47b93acf245a0f2e1133dfd8` |
| [notes/2026-11-13-strong-old-m32-q122-derived-retirement-r1-manifest.json](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-old-m32-q122-derived-retirement-r1-manifest.json) | 1546 | `7001ebd7f1f46613d97d15f8b07ffff1acc98936` | `9c631abb36bc58e7f14a652e06df4fd9c7af266b78109a329fcbb123bbd7548c` |

表中每件的 actual bytes、Git blob、SHA256 均由本次 Actions 实读原文件形成，并与固定 tree 的文件对象核对。receipt 与四份 manifest 在最初候选表没有预填 SHA256；它们的上表 SHA256 来自本次实读，不是推测或把 `null` 改成预期值。

### 3.1 五份大记录的所有外部字面引用

下面行号为对应原 manifest 中的真实一基行号。每对行分别是文件 basename 路径与完整 SHA256。没有其他候选路径/blob/SHA 命中，也没有代码或工作流消费点命中。

| 被引用记录 | 引用它的配套文件 | 原行号 | 实际内容类型 |
|---|---|---|---|
| current19 inventory | current19 archive manifest | 11、12 | 完整 basename 与 SHA256 |
| current19 receipt | current19 archive manifest | 17、18 | 完整 basename 与 SHA256 |
| old-derived inventory | old-derived archive manifest | 13、14 | 完整 basename 与 SHA256 |
| old17 inventory | old17 archive manifest | 12、13 | 完整 basename 与 SHA256 |
| m32-q122 inventory | m32-q122 archive manifest | 11、12 | 完整 basename 与 SHA256 |

这五份记录的全部十个外部匹配行均在表中四份 manifest 中。四份 manifest 自身的四类模式各为零外部匹配，因而九件组成闭合的当前字面引用集合。这里的“闭合”仅指该明确集合的固定提交字面引用，不扩张成任意动态路径、外部未见脚本或未来提交的无引用定理。

### 3.2 manifest 的真实含义

四份 manifest 的完整 schema 分别为：

- `current19-readonly-relocation-compact-archive-v1`
- `approved-old-derived-geometry-cleanup-archive-v1`
- `authorized-old17-regenerable-array-cleanup-archive-v1`
- `old-derived-chunks-retirement-compact-archive-v1`

它们记录已发生的 scratch 迁移／退役行政操作：原 producer、inventory、receipt、resource、说明和旧结果路径等。它们**不是**下文保护的 request41／54 科学 array manifest，不是现行 solver/native/FD 的输入清单。旧 manifest 中仍可包含历史 scratch 路径或已不在 f93 中的其他旧文件记录；本文只承诺上表九件的 f93 原字节恢复，不把 manifest 的所有旧路径虚构成当前仍存在的文件。

## 4. 行政 producer 的实际源码责任

下列四份源码已按固定 f93 全文读取并保留，**不列入删除集合**：

| 源码及固定历史链接 | 字节 | SHA256 |
|---|---:|---|
| [computations/prune_verified_old_geometry_arrays.py](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/computations/prune_verified_old_geometry_arrays.py) | 5225 | `575f8770441ce4bd30bdf790328265a97efacd1b1915f590e8274cb9578a73d9` |
| [computations/relocate_completed_current19_arrays_readonly.py](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/computations/relocate_completed_current19_arrays_readonly.py) | 12023 | `49a37ac232c86ccda5432185c6c86f277b8cbc6323babfaf39f4e63493a156a6` |
| [computations/remove_completed_old_m28_geometry_arrays.py](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/computations/remove_completed_old_m28_geometry_arrays.py) | 9740 | `0d972990a379071a31ae5083779d6107d6a7abd3c607714cb849993da8ecbbec` |
| [computations/retire_completed_m32_q122_geometry_chunks.py](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/computations/retire_completed_m32_q122_geometry_chunks.py) | 5866 | `57949f7f4ee0dfd4af4127f644ddbfe5295c35b27fcb104e70db706be62bcc34` |

`prune_verified_old_geometry_arrays.py`、`remove_completed_old_m28_geometry_arrays.py` 与 `retire_completed_m32_q122_geometry_chunks.py` 在各自明确旧 scratch 目录生成 inventory／移除收据；本次未执行它们。当前字面 schema 匹配定位到这些 writer 的构造字段，并未出现一个将上表已出版 inventory 路径作为当前数学输入的 reader。

`relocate_completed_current19_arrays_readonly.py` 的 `main` 确实有“若原 scratch inventory 已存在，则读取它核对恢复迁移”的分支，不能笼统说它从不读取 inventory。该程序同时硬核原工作目录 `/workspace/scratch/d1aa462cfc02/geometry-work`，其输入 `args.inventory` 为当时明确 CLI 的 scratch 位置；已出版 archive manifest 记录的 original_path 亦为该旧目录。它没有把本次 main 中的 `notes/2026-11-13-...` 路径硬接为当前 solver 消费者。保留原源码与九件固定历史，可以恢复旧行政证据；无需也不应通过重新运行这份迁移／清理程序来恢复 Git 记录。

补充 schema／producer basename 搜索还命中了保留的旧 first-validation 源和 resource 元数据。这些命中全部按原地址返回，不被称为当前科学入口；它们仍保留在 main。代码里可能接受任意调用者提供的动态路径，这一点不由字面扫描排除；本结论不把未见的任意外部调用当成已证明不存在。

## 5. 保留边界

以下明确保护对象不在本次九件中，且未作任何删除或内容替换：

- `notes/public-actions-43622149326-1-rawcell0steps/native-rawcell0-step-capture/rawcell0-step-array-manifest.json`
- `notes/public-actions-43634889730-1-directld/native-rawcell0-direct-ld/direct-ld-array-manifest.json`
- `notes/2026-11-14-handoff-public-migration-checkpoint.md`
- `notes/2026-11-14-handoff-legacy-recovery-checkpoint.md`
- `notes/2026-11-16-open-checkpoint-before-R456.md`
- `notes/2026-11-12-HANDOFF-before-r68-space-checkpoint.md`
- `notes/2026-11-12-root-r67-r69-stable-batch.json`

同时保留所有正在用的 inputs、source、recipe、必要 source-view plan、migration／legacy／R456 来源，及此前因 JSON 实际引用而保留的 HANDOFF。原先已经完成的 95 份历史 H/open 迁移不重复执行；其 [历史索引](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/topics/visible-flex-larger-amplitude/notes/2026-11-16-historical-checkpoints-index.md)保持原状态。

本次另查十一份历史 log／results-index 的结果如下，**仅作为尚未采用的备选证据，全部保留**。它们无非 Markdown 字面引用，但有表中真实 Markdown 引用；本方案不修改这些引用、不把这些文件计入释放量。

| 保留的历史 Markdown | 字节 | 非 Markdown 引用文件数 | 实际 Markdown 引用文件 |
|---|---:|---:|---|
| `log-checkpoint-before-R431.md` | 99074 | 0 | `log-through-R478-2026-11-16.md`；`notes/2026-11-16-historical-checkpoints-index.md` |
| `results-index-through-actual120.md` | 97869 | 0 | `open-checkpoint-through-request134-2026-11-15.md`；`open-checkpoint-through-request155-2026-11-15.md`；`results-index-before-request195.md`；`results-index-through-request212.md` |
| `results-index-through-request212.md` | 96775 | 0 | `log-through-R478-2026-11-16.md` |
| `results-index-before-request195.md` | 96703 | 0 | `results-index-through-request212.md` |
| `notes/2026-11-13-root-log-history-through-8ed411c73e21.md` | 96493 | 0 | `notes/log-through-2026-11-14-pre-resume.md` |
| `log-checkpoint-through-request109-2026-11-15.md` | 96186 | 0 | `log-checkpoint-through-request151-target-2026-11-15.md` |
| `log-checkpoint-through-request151-target-2026-11-15.md` | 93093 | 0 | `log-checkpoint-before-R431.md` |
| `log-through-R478-2026-11-16.md` | 92604 | 0 | `log.md`；`notes/2026-11-16-historical-checkpoints-index.md` |
| `notes/log-through-2026-11-14-pre-resume.md` | 92292 | 0 | `log-archive-before-1930-2026-11-14.md`；`log-archive-before-request17-2026-11-14.md` |
| `log-archive-before-request17-2026-11-14.md` | 67527 | 0 | `log-archive-before-1930-2026-11-14.md` |
| `log-archive-before-1930-2026-11-14.md` | 65137 | 0 | `log-checkpoint-through-request109-2026-11-15.md` |

上述十一份合计 993,753 字节；若将来另作迁移，必须按其真实引用单独处理，而不能由本次九件集合代替。当前没有这种必要，本次只选择九件行政记录。

## 6. 实际移出与恢复合同

执行方可用普通新 Git 提交删除第 3 节精确九个路径并加入本文。保留 Git 历史，不 force push、不 prune 历史 blob，也不改任何科学源码。当前 main 若已前进，应保留当前文件对象的真实身份及后续新增引用事实；发现新的实际消费者就保留其所依赖记录，不以固定 f93 旧扫描覆写新事实。这是本次删除动作的来源范围，不是新增数学 gate 或独立实验。

本文已给出每件完整固定 URL、blob、SHA256、bytes。单件无损读取命令例如：

```sh
git show f93b079e400c336f12751728ba388d6a9e769779:topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-current19-readonly-relocation-r1-inventory.json
```

恢复其它八件只使用第 3 节对应原路径；可把输出写到独立恢复目录并核表中 bytes/SHA256。读取时若本地是 partial clone，须先通过正常 Git 对象获取取得固定历史 blob，不能把缺失对象当成空文件。恢复这九件不需要重算曾经的科学数组，不把库存中的 SHA 倒推成已丢失的数组正文，也不赋予历史数值新的当前接受状态。

本次审计完整原必要 JSON 作为小型行政交接正文留给 root；不要求再将 32KB 全表加入 topic。供 root 实际删路径使用的小型 handoff manifest 也只是交接件。main 只需本文这种固定链接和完整身份索引，最终实际删除提交／容量回执由执行发布者另行记录。

## 7. 已完成与未作出的声明

已完成：固定 f93 全跟踪仓库的 88 字面模式扫描、20 候选的原文件身份、全部 47 匹配行地址、四份 manifest 与四份 producer 的必要完整源码范围、九件可恢复历史集合的明确选择及恢复合同。

未声称：对任意外部动态消费者或未来提交不存在引用；科学数值／BVP／几何／接受门得到新的支付；九件已经删除；删除后 main 容量已实测；额外十一份 Markdown 已经迁移。本文只有行政保留结论，所有正在运行科学入口和其原数学责任保持不变。
