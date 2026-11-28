# 第 65 批保全：旧生成 adapter 描述的完整字节重建

日期：2026-11-28。状态：完整材料已制成并保护为未引用 Git blobs，实际主线删除由 root 另行完成。本文件不把准备材料当作已实施提交。

## 1. 本批实际做什么

本批覆盖 36 份旧生成 JSON 描述，原大小合计 **2,292,948 字节**。保留另外 7 份完整原文件作为 canonical，用三个完整差分卷加一个纯文本恢复程序，逐字重建这 36 份描述。七份 canonical 都按原路径、原字节留在当前树；本批没有把一个运行的内容当成另一个运行的输入。

这不是只保摘要的清理。描述中包含的数学参数、原网格字面值、源文件 SHA、源代码替换文本、原命令、路径、worker 资源诊断、恢复来源和 prepared-only 状态都在重建结果中逐字保留。差分操作也保留空白、换行、浮点十进制拼写及字符串转义；不经 JSON 重新序列化。其与原完整文件的 SHA-256、Git blob SHA 和大小全部相同。

固定恢复提交是 `529e8ba2da541a95c62056a78e422504263c6f89`。这次读取以该提交的完整 topic tree 元数据为删除身份基准。36 个待删对象和 7 个保留对象均已按路径、blob 和大小匹配。发布时，root 只对清单中的 36 个旧路径做 fresh metadata 匹配后删除；未列出的文件不属本批。

本批不删除科学源码、证明、原配置或 spec、数值状态、原始数组、检查点、accepted099、parent91、当前运行材料或唯一未恢复输入。端口和 Nelder 的未闭合来源也不在本批。三份较大的旧 Hermite、curvature24、current-control 数值结果没有因文件名相似被纳入。

## 2. 完整新增材料及容量口径

本批三份 `legacy-generated-adapters-retention-65-complete-byte-deltas-01/02/03.json` 分别为 30,043、41,662、69,627 字节，合计 141,332 字节。完整恢复程序 `restore_legacy_generated_adapters_retention65.mjs` 为 5,883 字节。另保完整 provenance、此说明和交付总表。最终总表列出所有新增文件的完整身份及精确净释放数。

provenance 的 30 个完整源码记录、140 个完整配置/资源/结论记录和 33 个 case 映射，都是完整原文件的引用。这些原文件仍原字留树；不是只保存本说明挑出的几个字段。完整原 argv、resource、输入身份及失败责任因而不需再复制成第二套不一致的大表。

三个差分卷的内容按完整文件分组，每一成员都带：

- 完整原路径、字节数、SHA-256、Git blob SHA 和固定恢复提交；
- 所用完整 canonical 的相同五项身份；
- 该成员所有字节替换操作，不省略任何插入字串。

当前树减少的是重复的生成描述实体；原内容仍可由当前树内的完整 canonical 与完整差分材料确定性还原。历史提交的完整原 blob 同时继续存在。

## 3. 实际生成来源

### 3.1 stored tail 描述

完整 `computations/tail_stored_client.py` 的 `WeightedTailPort.__init__` 先构造原 client，读取真实 ready 回复并核 endpoint、stored metric、stable graph 和来源身份，然后写 `record_prefix + '_adapter.json'`。完整源码第 83–88 行是实际写入处。后续 solve/close 委派原 client；该描述不是用来替代真实 tail solve 输出或数值检查点。

本批完整保留该 ready 描述，包括 worker 资源状态和原引用路径。不同进程的内存计数、路径及字串都通过精确差分保留，没有假称它们是跨机器稳定的物理输入。

### 3.2 full-tangent 描述

完整 `strong_full_tangent_tail_client.py` 第 133–144 行写 `_full-tangent-adapter.json`。其内容来自实际原 source 修改、source hash、完整 ready 和 snapshot 恢复记录。它可以记录数值 snapshot 的身份，但不是把 snapshot 的数组正文放在本批替换掉。

本批每个历史文件仍独立绑定原 worker/source 和原恢复路径。相同字节的 observed 副本也保其原名字；原路径仍是历史 manifest 的一部分。

### 3.3 actual-three-control 描述

完整 `strong_actual_three_control_bvp.py` 先核实际原 source，再构造完整 wrapper/provenance。第 255–294 行范围包括实际 provenance 及三份生成文件的写入；其中 `-actual-three-control-adapter.json` 的原状态是 `prepared-only`。它保留 target core、gauge、未知数个数、完整原节点、command arguments、batch、tail IO、warm/reuse 记录及源代码变换。

多个完整 wrapper 会添加各自的 source transform、精确替换文本、原 source hash 或调用关系。这些不是可删的“冗余字段”；本批在完整 canonical 与差分中保留全部字节。准备描述的状态也没有因另外一个进程后来退出 0 而改写。

provenance 同时登记了完整的 full-tangent、cached-prefix、fresh-resource、disk、exact-raw、physical-merit、initial-laws、same-g refinement 和资源包装源码。每个旧 case 的完整命令与参数仍在其原 resource/config/plan 文件中。本文没有从 basename 反推参数。

## 4. 七个完整 canonical 及其含义

七个原文件均在 `notes/`，完整长路径和三个全字身份见 provenance 的 `canonical_files_kept`：

| 完整原文件尾部 | 字节 | 保留理由 |
|---|---:|---|
| q122-m32-sameg-actual-r1-tail-response_adapter.json | 95,504 | stored-tail 描述的完整原件 |
| q122-m32-sameg-actual-r1-tail-response_full-tangent-adapter.json | 41,740 | full-tangent 完整原件，兼容此前别名链 |
| a32-gap-release-size099-actual-r3-actual-three-control-adapter.json | 88,194 | 完整较大 source-transform 家族原件 |
| q096-combined-m24-tol7-prefixcache-heap96-r4-actual-three-control-adapter.json | 47,374 | prefix-cache 完整原件 |
| q105-freeq4-m24-tol7-exactraw-r1-actual-three-control-adapter.json | 13,579 | exact-raw 完整原件 |
| q122-m28-pure-secant-actual-r1-actual-three-control-adapter.json | 66,678 | pure-secant 完整原件 |
| q105-freeq4-m24-tol7-physical-merit-r4-actual-three-control-adapter.json | 40,012 | physical-merit 完整原件 |

“canonical”只指本次字节压缩所取的底本。它不赋予较高科学资格，也不把 r4 当作 r3、M32 当作 M28、一个 point 当作另一个 point。任何历史消费者仍须取得其原文件的完整字节；不能直接把底本路径替换进原科学命令。

## 5. 精确重建及其已完成边界

原件与 canonical 的全部 43 个正文均小于 100,000 字节，并且全部为 ASCII。此次实际整读了这些小正文，没有读取任何大于等于 100,000 字节的 raw、二进制、压缩包或数组。

每个替换项为：

```text
[原 canonical 的零基字节偏移, 删除字节数, 完整 ASCII 插入字串]
```

所有偏移都相对于没有改动的 canonical。按偏移从大到小应用全部替换即可取得原成员。此次仅做文本处理：对全部 36 个成员，重建的完整字符串与已整读的完整原字符串逐字相等。原件的大小、SHA-256 和 Git blob 身份也完整登记。没有运行旧科学 producer、导入数学模块、构造模型、解根、计算导数、做 AST 检查或新增数值算例。

独立 Node 恢复器只导入 `node:fs`、`node:path`、`node:crypto`。它先核三个完整差分卷，再核实际读取的完整 canonical，检查 ASCII 与非重叠替换，重建并再次核目标的大小、SHA-256 与 Git blob。它拒绝覆盖已有不同字节的目标文件；已有相同字节则保留。它不访问网络、不运行 Git 或旧 producer，也不声明任何数值结果已被重算。

该程序的完整源码已保护；没有在本地执行此 Node 文件。已完成的是上述字节构造与原全文对照，不能写成一次科学复算或新的科学准入条件。

从仓库根使用全部原字恢复：

```sh
node topics/visible-flex-larger-amplitude/computations/restore_legacy_generated_adapters_retention65.mjs --repo REPOSITORY_ROOT --output-root RESTORE_ROOT
```

若只恢复一个旧文件，追加 `--only FULL_REPOSITORY_RELATIVE_PATH`。程序保留完整仓库相对路径，防止同名不同 run 的文件被放错。

独立的历史恢复方式是：

```sh
git -C REPOSITORY_ROOT show 529e8ba2da541a95c62056a78e422504263c6f89:FULL_REPOSITORY_RELATIVE_PATH
```

每个原 blob 也可按其精确 Git SHA 读取。两种路线都只解决原字恢复；原科学所需的其它输入仍按其既有完整恢复合同处理。

## 6. 实际读取者：不能把“删描述”理解成没有输入义务

本批已完整读取下列实际消费者，provenance 给出它们的全字身份：

1. `strong_archive_accepted_fullflow_actual_v2.py`、`strong_tail_recovery_freeze.py`、`strong_tail_resource_retry_prepare.py` 及 `archive_current_gap_release_warm.py` 会复制、哈希或收录原 adapter 文件。旧 archive 的部分路径使用 `if path.is_file()`；因此恢复历史 archive 前必须恢复其所需原路径，不能依赖文件缺失后被跳过而宣称 archive 完整。
2. `strong_archive_sameg_first_tail_trial_v2.py` 实际核 full-tangent adapter 的 source 身份，并把其完整字节复制为 `full-tangent-adapter-observed.json`。即使字节与一个保留原件相同，历史 observed 名字仍应恢复。
3. `strong_physical_merit_first_request_check.py` 真的接受 `--failed-r3-adapter`，哈希该文件并读取 `explicit_same_H_tail_warm_recovery`。本批保留该诊断的完整 resource 命令；运行它必须先恢复 r3 原件，不能用保留的 r4 canonical 代替。
4. `strong_m28_saved_reference.py` 读取 q096 actual28 的 stored_metric 描述。那个文件不是本批 36 个成员，仍原字留树。不能由这里的描述压缩范围推广到未列出的真实数学输入。

这些原消费者没有被修改。恢复义务已写入总表和 provenance；本次不声称全仓库不存在其它历史引用。完整 old command 中请求哪个文件，就恢复那个文件的原路径和原全字身份。

## 7. 与既有别名保全的连接

已刊 `notes/2026-11-17-parallel-duplicate-plan-retention.md` 的完整 32,502 字节说明仍保留并被引用。本批特别保住其两个方向：

- 较早 a32-r3 和 q098-bootstrap 的 full-tangent 重复别名指向本次仍保留的 q122-M32 same-g full-tangent 原件，目的文件没有退役。
- 较早 q098-independent 别名指向 q106-M28-r2 full-tangent；后者这次属于 36 个可重建成员。因此先用本批完整差分恢复 q106 原件，再按旧别名合同恢复旧请求路径。两级恢复不会把 source/运行身份合并。

另一个 61,152 字节 q098 new-J canonical 不在本批，也没有被改动。总表枚举的成员范围是唯一删除范围，旧别名链不扩大它。

## 8. 原运行结论与失败责任

完整 33 个 case 的资源字段和证据文件在 provenance 中逐项登记。下表概括容易被误读的边界；它不取代原完整报告：

| 原分支 | 本批保留的实际边界 |
|---|---|
| q126 M32 tail2 | 原 resource 退出 0；独立完整 accepted-recovery manifest 记原接受，但明确不声称无限闭合、握持闭面或 reach |
| q106 M28、q122 M28、q122 M32、q098 new-J | 保原实际 resource 和完整配置；本次字节存储不增加任何数学结论 |
| q098 independent startup | 退出 0 是启动/恢复；完整 manifest 记零 nonlinear requests，没有新 H 接受 |
| q098 bootstrap、current-H audit | 保实际审计范围与原输入身份，不把审计扩写成新完整求解 |
| CI 43302113873 | 原 terminal 分列 supervisor 退出 0、solver_success=true、audit_pending=false；较早 r7 session 的 terminal 状态仍 unknown |
| a32 gap r1/r2 | 原实际退出 1，保持失败 |
| a32 gap r3 | 原 session-loss 明确未观察正式 exit，exit 为 null，没有完整新 Jacobian或新 accepted full BVP |
| a32 gap r4、q096 fresh r2、radial8 r6 | 仅所保 launch/command/config，不补未来或缺失的 terminal |
| q096 fresh r1 | 中断时正式工具返回、resource/summary 未齐，已有检查点不自动升级为接受 |
| q096 fresh r3、prefixcache r4/r5 | 原退出 −9；原失败与已完成缓存调用数量原样保，不推断原因或完整 Jacobian |
| q105 disk/exactraw/physical-merit r4 | 原退出 −9；exactraw cause 仍 unknown |
| q105 physical-merit r3 | 原退出 1；其失败描述仍是旧 first-request 检查的真实输入 |
| 各 prepare-only 分支 | 原完整命令含 `--prepare-only` 的退出 0，只证准备阶段；无新数值接受 |
| same-g first-tail observed 副本 | 保原复制关系和完整 manifest，复制不等于新 root 或新 Newton 步 |

原 elapsed、resource、hash、worker 路径和输入参数都留在原完整文件或可逐字重建的成员中。这里没有把 signal 9 归因为未经原记录证实的原因，也没有把未知旧末点填空。

## 9. “可恢复描述”与“重跑旧科学”分开

本批的重建算法完全不依赖旧科学 runtime：七个完整原件、三个完整差分卷和恢复器就给出全部 36 个原文件字节。

原科学重执行还依赖完整原 source、输入、外部 worker/client 版本和 runtime 状态。相关已知恢复义务仍保留；例如旧 4,752 字节 client 与后来同名较长版本不得混同。本次没有把后来版本充当旧版本，也不因字节恢复完备而声称原数值链已在当前机器重跑通过。

原 source 文件本身、原配置和输入恢复记录继续留树。所有原描述中的 source-transform 也是原字，没有删掉难恢复的部分来满足容量目标。

## 10. 发布和后续读取边界

本 agent 只创建完整未引用 blobs，没有写 ref、排科学队列或删除文件。root 的实际发布提交须另行记录。总表的删除列表含每条完整路径、大小、SHA-256、Git blob 和固定恢复提交；新清单中的 canonical 全部保留。

没有新增科学测试、benchmark、重放、AST 或审核门。原科学与当前正在运行的目标、变量、预算和证据均不变。需要历史内容的读者可先按本说明恢复完整原路径；当前数值源不能把这些旧描述作为新目标或新实际场的证据。

精确新增体积及净容量以配套完整交付总表为准。本说明只报告保存与恢复关系，不报告新的数值收敛、几何证书或原题完成。
