# RET81：四份旧发布回执的历史保全

作者：/root/construction（GPT-6 Astra Pro，AI-assisted），2026-11-28。

## 1. 本批对象与性质

本批仅退存四份 2026-11-12 已生成的发布行政回执，毛字节 **288,973 B**。它们记载当年的 source/base、完整文件对象清单、owned cache 分批状态、普通 merge、实际成功和失败。所列科学文件本身、数学证明、源码、配置、原选择清单及当前活动输入均不删除。

固定公开仓库快照为 `4a8f49da3e144e15cbbb8da433e12fb24f1f67da`，课题树为 `562caeb68ebf2f87e5f3e8208fc95fe05744a796`。根代理实施前按最新树核对四个原路径、blob和字节。完整合同保存在 [RET81完整台账](../computations/legacy-four-publication-receipts-retention-81-complete-provenance.json)。

| `notes/` 下的回执 | 字节 | 原 Git blob |
|---|---:|---|
| `2026-11-12-root-corrected-r63-r73-publication.json` | 78,809 | `5361ee1247eddb52177614aa38576c84999ae1ee` |
| `2026-11-12-root-r74-r79-publication.json` | 80,999 | `cb4ad32864aeacc7c0b17707dd364256c8095652` |
| `2026-11-12-root-r81-r82-r11-publication.json` | 85,508 | `0541378b1fc2e3f39d2a155083669ff366a296ae` |
| `2026-11-12-root-r80-r83-profile-publication.json` | 43,657 | `69c3e2c8b71e7c7306c23f4221c83f5f58778033` |

四份完整文本均小于100,000 B，已按完整字节核 SHA256。台账保留各原 SHA、字节、固定提交、完整 Git blob与全部实际状态的精确定位。批内每个文件清单的所有条目仍在相应原始整回执中，可逐字恢复；不把显示的文件数或摘要当成原清单。

## 2. 真正的历史发布已由原私库元数据对应

这四次发布的目标仓库是原 `Rogerhu12/math-research`。此前只在公开镜像查询原 source/base，不能由404推断原私库的正式发布也不存在。本批使用已授权的私库 GitHub GET 接口，真实读回四个正式 merge 的提交消息、父提交、根树及课题树。

| 回执 | 实际正式发布 commit | 实际课题 tree |
|---|---|---|
| corrected R63–R73 | `ad71c069f9c0fffe05afd952464608fbe9178541` | `de9fee0aa294ff05634051e2fa28a81ebe96b75b` |
| R74–R79 | `638669d30faf1360e455a9576b1d4dfb13a5eedf` | `ac8f763f5ab30aaf12c74b70866e03784ff472f6` |
| R81/R82/r11 | `fdbb5d676c7075679d48c65df8d4ffa369a5cda3` | `e373b57d7749d5eee48759bc9a7db0a771285f8f` |
| R80/R83/profile | `551b1da3dc84ce613968b392f646cfa599c88755` | `ec316d3ba82055df150549ca8733c936496be752` |

上述实际 topic tree 逐个等于原回执记载的 `source_topic_tree`。正式提交的全部原消息、父提交、UTC及元数据端点都进入台账；其计算目录中四份相关生成源的 Git blob亦与当前公开完整源码对应。原临时 source `310da6f26ca1cc5858a776f5eabef02dc5ca211c` 的私库 commit API仍404，这一事实保留；没有把正式发布的同内容 topic tree冒作该原 source commit，也没有重造其提交时间、作者或 message。

这是历史内容和事件的读取，不是重新发布。完整回执本身按公开仓库固定 Git对象恢复，不依赖当年的临时 branch仍存在。原 owned cache后来已删除的成功记录也不要求恢复远端 branch。

## 3. 完整生成源与参数边界

以下原完整源码均保持当前文件不变，正文及其实际写入/读取点已读取。每份的原 SHA256、Git blob、字节与固定恢复提交在台账中完整列出。

- `publish_topic_object_batches_v2.py`：10,915 B，SHA256 `ee1369a8a41961cab94bb4e9101f281ca8d1777529424bd2fbe8c0fc75722977`。完整 `--active --publish --source --base --read --state`，原默认 `--topic topics/visible-flex-larger-amplitude` 和 `--batch-bytes 8000000` 均保留。它从真实 base/source 树枚举整份文件对象，保存全部分批与 push状态，只推进自己的 cache branch，并检查完整 topic内容。
- `publish_topic_verified_cache_merge.py`：8,190 B，SHA256 `804acc30ff0f97e16673e65de170b641b9c4c6e1b40aa418f9b14d36c45a3cef`。完整 `--active --publish --cache-state --state --read --message`，原普通 merges API、pull/README核对、完整来源与最终树核验、实际失败分支均保留。四份回执各自记载此原源码 SHA。
- `root_commit_manifest_tree.py`：6,616 B，SHA256 `e79c9e53fbdc17a7f42a1b2b6c3caa3bf0a93d27fc5d842bd356efcc94694177`。完整 `--repo --selection --parent --owned-ref --message --state` 与固定 topic 保留；逐文件检查原字节/SHA，在保留 HEAD/index/lock的条件下构造新的普通子提交。
- `publish_topic_checkpoint.py`：10,844 B，SHA256 `70543eb55ed6932cf18a4ebc3228524fc100fd61e4bb88837cbf7b0458eb3cc3`。前两程序只导入其中的 `update_read_marker`，本批不把该文件另一 main当成这四份回执的生成入口。

完整台账保留每次实际 source/base、branch、tip、topic、全部已记录的 selection路径/SHA/count、最终read marker、正式 merge message、完整同步及HTTP尝试、每批 commit/parent/字节/文件数、全部push状态及失败。这些参数与原选择清单分别保存。

原回执没有逐字记录某些 shell参数，例如最初的 `--read`、原active/publish绝对路径、是否显式覆盖batch默认值以及某些临时state路径。台账明确用null表示这些未记录项；**不把最终被程序修改的read marker冒作最初CLI，不把默认值冒作实际显式参数**。外层汇总回执的单独内联shell源码没有独立记录，也不虚构。完整原回执仍可按Git原字恢复。

这不是要求重新执行原网络事件的退存方案。源码和全部已记录参数用于解释当年的行政行为；精确恢复原回执使用固定Git对象。若将来另行运行这些会修改refs的工具，那是新的操作与授权范围，不由本说明启动。

## 4. 实际结果、失败与未知保持

corrected R63–R73的真实新发布完成；原353旧cache只作历史保留，其正式terminal和旧main merge仍未知，原自动审核拒绝/中断没有被写成成功。首次cache构造exit1与local commit之后元数据查询exit1仍在整回执的formal sessions中。

R74–R79保留原local index的中断：第一次session92945终态未知；第二次git add因已有index.lock返回128，整个尝试exit1。随后使用完整选择和独立tree对象构造安全source，原HEAD/index/lock保留。不能把原锁或进程状态猜成已终止，也没有在本批删除锁。

R81/R82/r11记录cache63235与merge37849都exit0，完整原结论和范围留在原选择清单及科学文稿。

R80/R83/profile的首次owned-cache push返回exit1，pack-objects报告signal9，但原因未知。随后同一immutable source改用临时pack参数 `threads=1/window=0/windowMemory=4m` 完成cache及普通merge。这不证明先前signal9是内存、磁盘或timeout导致。完整首次失败回执按固定603214提交/blob恢复，其状态与诊断在本批台账保留精确来源。

四次成功都是行政发布事实。它们不新增或加强 R63、R74、R81、R83 等科学结论，也不把原闭曲面、参数域、模式、误差或未知责任改成已完成。

## 5. 原选择清单与实际读者

本批保留四份原stable batch、后续R84–R87 stable batch、local-index恢复记录及R74–R79 recovery manifest的完整当前字节。原选择文件中的每个原路径/SHA/字节保持历史含义，不改成“现在这个输出仍在树中”。

存在真实的行政依赖链：后一stable batch选择前一完整publication回执，后续cache枚举其完整Git文件对象。cache writer恢复时也会读完整旧state，merge writer读完整cache state，source-object writer读完整selection及被选文件。台账明确给出这些源码和读点，没有宣称“回执无人使用”。

执行这些历史读取前，须先恢复原整回执或相应完整nested state。本文及台账中的批数、结果或路径列表不能替代原state。此前退存账若引用原publication整体SHA，继续按其固定历史身份读取；本次不修改旧引用的身份。

## 6. 恢复与发布责任

根代理只删除本表四个generated receipts，同时加入本次完整台账、说明和delivery。完整旧字由公开固定提交 `4a8f49da3e144e15cbbb8da433e12fb24f1f67da` 或原blob读取。私库四个published topic tree提供原科学文件集的独立历史对应，但不触发任何网络重演。

本批没有读取大于等于100,000 B或二进制本体，没有执行科学、AST、CAS、fixture、benchmark、源重放或发布命令。没有建立数值编码、数组搬运或新审核前门；所有refs/queue仍仅由根代理操作。
