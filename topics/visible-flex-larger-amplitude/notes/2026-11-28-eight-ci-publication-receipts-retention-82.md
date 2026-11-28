# RET82：八份旧 CI 发布回执的完整保全

日期：2026-11-28。课题仍未完成；本次只处理原行政发布记录，不产生科学计算、运行成功或数学通过结论。

## 1. 精确范围

本批仅移出八个 `publication-manifest.json`，毛字节数 158317。完整路径、旧 Git blob、完整 SHA-256、字节数与各回执的 UTC、run、attempt、lane、trigger 均在 [完整台账](../computations/legacy-eight-ci-publication-receipts-retention-82-provenance.json) 中。回执全部小于 100000 B，已逐件全文读取和 whole 身份核对。

| 原 run / attempt | lane | 原回执 B | 原 files 行数 |
| --- | --- | ---: | ---: |
| 43302113873 / 1 | interval | 14940 | 7 |
| 43302113873 / 1 | sync | 13174 | 4 |
| 43303094938 / 1 | sync | 11957 | 4 |
| 43303787139 / 1 | interval | 27899 | 31 |
| 43303787139 / 1 | sync | 11481 | 4 |
| 43307481613 / 1 | interval | 12838 | 8 |
| 43307481613 / 1 | strong | 55522 | 79 |
| 43307481613 / 1 | sync | 10506 | 4 |

八个独立原 `request.json` 和八个 `runtime.json` 都留在当前树。原请求不是只保执行过的步骤：七步/三步整个对象、全部 argv、cwd、publish_sources、expected_old_blob、globs、依赖、enabled_lanes、原 log_append/HANDOFF 替换、资源限制与未知状态都由这些完整原文件保留。已核每份回执内的 request 与同目录完整请求整对象相等。没有将生成数组改称参数，没有打包或编码科学数据。

原回执总计 141 个 source/publication 路径、尺寸、SHA 与 published/reason 行完整留在固定历史 Git 对象中；台账明确给出每件 whole record 和 `/files` 入口。这一批没有删除所引用的科学输出、源、参数、日志、runtime、checkpoint 或证明。

## 2. 原生成源码与工作流确实来自当时 trigger

四个原私库 `Rogerhu12/math-research` trigger 已通过授权 API 实际读取，并取得原发布脚本的完整正文，不用当前后改的 v1 或 v2 冒充旧体：

| 原 trigger | publisher B | publisher SHA-256 |
| --- | ---: | --- |
| ee27c33fa39878244c115cfaf1f542dadaa2e35a | 14690 | bbf9370d6a0b6db936891395d299a1377aed38ff9bb5e567ff8e152fa422404b |
| 5fe279735daf2f0bc9f98dd8bc452b31424346a6 | 15438 | d4cbb1eb16218951f105d96452e4f550bd60350c4ed614926a847850270369ff |
| a394d627408c7992909be71ce1de41c90f91f574 | 15582 | 6fab99d719444c02864db5a8ba661acf82920202623746a9bc7b35159e71fbcc |
| 02207049f3272374d214fbcb77865ee13eac4254 | 16253 | c38756368a2859ece53deeb20d6e90962e844bdfb99a8b17d75f8d05263d0e3e |

共同完整路径为 `topics/visible-flex-larger-amplitude/computations/ci_recover_visible_larger_v1.py`。各自 Git blob、固定 private restore commit 和 API 路径均在台账。前三个工作流为 7897 B / `e99f451b68d8066a6048eb3face37b37c31dac55d88548cda5cba9d9c99071a5`；第四个为 8417 B / `8c3a19eee5f33278fe562ac28c2e9a96408be701fc6934e6148a056f8e0e8f88`。这两份工作流也全文读取，按各实际 trigger 绑定。

原 workflow 的启动命令为完整 publisher 加 `--repo "$GITHUB_WORKSPACE" --request topics/visible-flex-larger-amplitude/computations/ci-recovery-request.json --lane sync|strong|interval`。原 job 超时分别 25/240/90 分钟，ubuntu-24.04，单线程环境，artifact 压缩等级 1、保留 30 日。arithmetic lane 原安装 Python 3.12.14、Node 24.22.1、numpy 2.3.5、scipy 1.17.0、python-flint 0.9.0；sync 原实际 runtime 却是 Python 3.12.3、Node 22.23.4，不能从 arithmetic setup 反推其实际版本。原 workflow 全字可恢复，未删资源、阶段或完整参数。

## 3. 真正的 write / read 边界

四份原源码的 `Publisher.outputs(patterns)` 先取 out.rglob 与完整请求 globs 指向的文件，复制或压缩，再对原文件与发布文件分别计算完整 SHA 和尺寸。随后写回执的七个顶层字段：schema、utc、run_id、trigger_commit、request、files、task_complete。写回执之后才执行 git add、diff check、commit、正常 pull/rebase 和 push。

因此原 `published=true` 只表示复制出的候选满足本地小于 5000000 B 的发布阈值并进入待提交路径；回执自身早于 commit/push，不能单靠它把后来失败的网络或 Git 操作记为成功。全部八份 `task_complete=false` 原义保留。

前三版只有 size > 1000000 且非 .gz 时压缩；第四版另外无条件压缩 .log/.jsonl。第二版加入指定 HANDOFF/log 修改；第三版把明确的 server main-ref CAS 竞争纳入普通 pull/rebase 重试；第四版加入 artifact 权限、depends_on/skip、continue_independent。以上差异按原版本保，不跨版本借用。

原 `strong_ci_artifact_recovery.py` 16413 B / `6c23b91c20d17acc2e92b94d4843c1570140167109ef4d3dbc3503d0da84c113` 也全文核过：它恢复 run43302113873 的 72 个原 artifact 成员、核 original ci-stable manifest，再读 original summary/ci-terminal/resource。它不把这八份行政回执作为数学输入。原 artifact id 13983440730 与 ZIP SHA `27c0e11f6ab2c0fc45338dd186c0fdd36cfe7f2f962f1b849f509708054331fb` 是历史绑定，不承诺未来网络服务仍提供它，也未为了退存重演下载。

已发现的历史读者是 RET31 说明中对 interval43303787139 回执的链接。原 [RET31 note](2026-11-27-legacy-R90-green-checkpoints-retention-31.md) 留存，原研究结论及旧说明没有改写；今后需要该回执时先按本批固定 Git 身份恢复完整原路径到独立历史工作目录，再由旧读者读取。没有声称搜索足以证明所有未知消费者不存在。

## 4. 原结果、失败与未知完整保留

八个原 recovery-status 另从公开固定提交 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 全文取回，whole records 和完整原对象收进台账。它们早已不在当前树，不是本批新增删除，也不能拿其旧 whole 身份当当前 guard。

- 433021 interval：whole46 geometry 子步骤 exit 1，wall 1.0013440029999998 s，RSS 45308 KiB；后续阶段未由该记录证明执行。
- 433030 sync：实际 main-ref 竞争触发 RuntimeError，actual_results 为空。原完整 expected/actual Git tip 与错误文本均保留。
- 433037 interval：geometry exit 0 / 360.04765865499996 s / 46300 KiB；budget exit 0 / 392.05308925800006 s / 24636 KiB；随后 moments-recovery exit 1 / 1.0011158329999716 s / 40108 KiB。成功的前两步不覆盖第三步失败。
- 433074 interval：linear-centre 子步骤 exit 1 / 1.0022273520000056 s / 48636 KiB。
- 433074 strong：原 artifact-restoration 子步骤 exit 1 / 4.002946324999996 s / 33428 KiB；不能把目录已有恢复文件或 published 标志当成该步骤成功。
- 另外三份 sync 的原 actual_results 为空、failure 为 null；这只报告同步阶段记录，课题完成仍为 false。

原 433021 strong 子步骤实际 exit 0 / 528.232341799 s / 400668 KiB，而后续发布因原日志尾空格被 git diff --cached --check 拒绝。台账完整保该原 argv、资源、状态及失败全文，原 2534 B publication-failure 文件仍留当前树。所有 old_local_r7_terminal 原值都是 unknown，没有补造末场或题目完成。

## 5. 一处已有压缩版本差异不被掩盖

141 行中 140 行可在既有公开树元数据按 publication 路径/尺寸对应；这只是 metadata 关联，不是重新读取或全 hash 所有数据。另一行原 prefix-cache-events.jsonl.gz 记 482261 B / `2cd08f9dbd7ba7a895f58721eb7157fdfce8da9ee6b2952ebc2fe864e034364a`，而已知公共历史及私库实际 published commit 的同路径为 474562 B / Git blob `32964fcb0634884f3883e472277d93e3b2035c53`。未读或解压该大体，未把二者称为相同字节，原 482261 B 变体的独立 Git blob 仍为 null。

本批只退完整行政回执，且原回执自身从固定公开 Git 可准确恢复；这项原输出差异完整保留，不把“恢复回执”扩大成“所有数值载体恢复已经完成”，也不据此删除任何未闭合输入或重新计算科学。

## 6. 固定恢复、当前 guards 与实际实施

八回执的准确公开恢复提交为 `4a8f49da3e144e15cbbb8da433e12fb24f1f67da`。需要原字节时读取该 commit 下完整路径或台账精确 blob，按给定完整 bytes/SHA 验证；不运行当前 publisher 冒充历史 UTC、Actions 事件或 Git 发布结果。

台账 `retained_current_whole_files` 的 18 件才是本批保留对象的当前 guard：8 request、8 runtime、RET31 note、原 publication-failure。private 历史 source/workflow 和旧 public recovery-status 均是历史 whole references，不能当当前版本。root 发布前只对八个删除路径的 fresh blob/size 及这些当前 guards 做正常精确对应；原科学/参数/源码不变。

所有工作是小文本、源码与元数据读取、JSON 对应与文字哈希。没有读取 >=100000 B 或二进制正文，没有本机 science/AST/fixture/replay，也没有新增研究准入门。最终是否普通提交由 root 唯一执行，本代理没有改 ref、队列或删除文件。
