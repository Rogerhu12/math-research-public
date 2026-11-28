# 第 63 批：早期六组已终态公开 Actions 输出的完整来源与逐字恢复

日期：2026-11-28（UTC）。本批是旧生成输出的现树退存，适用根 README 第 15 条及 root 当前明确的容量整理指令。这里只提交完整记录与未引用 Git blobs；实际普通提交及现树移除由 root 负责。没有运行本地科学计算、导入求解模块、AST、数值算例、性能测试或科学重放，也没有增加这些前置条件。

## 1. 唯一移除范围

固定完整恢复提交为 `5358ca0c0a2e48f66af6be474ba1a202d6a935c3`。本批只含下表六个已终态运行的 6 份总索引与 37 份原分卷，共 **43 个完整文件、1,852,233 字节**。每项精确路径、原文件字节数、完整 SHA-256、Git blob SHA 都在完整交付表和返回定位表中。不得按目录或通配符扩展删除。

| 原请求标签 | 实际 run / attempt | 文件数 | 原字节 | 已公开实际返回数 | 官方终态 |
|---|---:|---:|---:|---:|---|
| 01 | 45762076394 / 1 | 10 | 480468 | 77 | completed / success |
| 02 | 45800076687 / 1 | 6 | 239361 | 49 | completed / cancelled |
| 03b | 45820592817 / 1 | 10 | 449325 | 36 | completed / success |
| 04 | 45857104277 / 1 | 6 | 250090 | 49 | completed / cancelled |
| 05 | 45870334713 / 1 | 6 | 217488 | 18 | completed / cancelled |
| 06 | 45904402595 / 1 | 5 | 215501 | 43 | completed / success |

本批不含前次 ret62 的 12–18，也不含仍有实际计算责任的 19–25 或其后新运行。旧科学源码、证明、原输入、完整请求、队列、所有参数、归档 summary 选择器、历史位置参数和各完整结论说明均留在现树。原始 accepted .99 输入不退存。先前未闭合的 ports/Nelder、唯一不可再生输入及 parent91 不在范围内。

所有 43 个候选原文件均小于 100000 字节，已逐体读完整文本。没有读取任何大于等于 100000 字节的正文，也没有读取 gzip、NPZ、ZIP 或其他二进制正文。其全字身份由真实原文件给出，没有用名字或相近来源猜测。

## 2. 五份完整交付的分工

- [完整 source / parameter registry](../computations/early-terminal-public-actions-retention-63-source-parameter-registry.json) 保留 59 个完整现存小文件记录、75 个入口路径下的 158 个实际入口来源版本，以及 6 个队列路径下的 55 个实际队列版本。来源版本中的 SHA 是原控制器实际记录，不是对当前同名文件的身份假设。
- [全部 272 个返回的定位表](../computations/early-terminal-public-actions-retention-63-complete-return-locator.json) 逐项给出原 run、阶段序号、原完整分卷、JSON fence 序号、完整原 JSON 文本的字节数与 SHA-256、原字段集合、状态、退出码、原秒数字面，以及完整参数位置和实际来源版本索引。
- [完整 provenance](../computations/early-terminal-public-actions-retention-63-complete-provenance.json) 保留六个请求的完整对象、官方终态 API 投影、请求和实际控制器的全字身份、资源 / 工作流记录、所有未返回责任与旧消费者恢复合同。
- 本说明解释生成、消费、数值结论和未知边界。
- [完整交付表](../computations/early-terminal-public-actions-retention-63-complete-delivery.json) 给 root 本批所有精确删除项、完整新增文件与毛退 / 新增 / 净退字节。每件均小于 100000 字节。

这些定位表没有缩减原科学配置。整套参数的载体仍是原完整文件和精确历史队列；没有把它们变成选择性摘录。返回定位表是检索索引，原 compact JSON 的全部内容按固定 Git 完整恢复。

## 3. 272 个实际返回的保全

43 个文件中的原 JSON 分卷对象共有 272 个。其中 158 个是 followup 返回，114 个是原输入 / 初始链重建返回。每个原 JSON fence 都给出了自己的 SHA-256；其定义是开头 `json` fence 后的换行与结尾 fence 前的换行之间的完整 UTF-8 文本，不包含这两个外侧换行。原缩进、浮点数字面和字段顺序的恢复以 Git 原文为准，不经 JSON 数值重新序列化。

定位表还保留原顶层字段集合。因此“原来没有这个字段”和“原来明确为 null”可以区分。表中的 null 绝不意味着未知子进程正常退出、未知历史为空、没有新增材料地址，或没有新的永久保护点。

每个原返回的所有输入 / 输出文件记录、完整原命令、源码提交、父来源、compact scalar、scope、cleanup、summary_errors、missing_outputs 和错误文本均通过原整文件及精确 fence 定位完整恢复。没有只留成功步骤；失败、setup 失败导致的 null returncode、有限迭代 budget、restoration_failed、纯读取失败和缺输出全部保留原义。

原索引已经明确：完整科学数组、逐点 / 逐胞报告与大日志只留 runner。因此本批不宣称可以由一个 SHA 找回已经不存在的 runner-only 数组；也不把 Git 中的小 compact object 冒称完整 NPZ 或完整场。需要重新计算时仍须用全部原 source / params / inputs，并把新输出的实际身份重新记录。

## 4. 六个真实控制器与完整读写链

原 01、02 分别使用 `public_actions_controller.py`、`public_actions_controller_parallel02.py`。03b、04、05、06 分别使用其完整 `parallel03_compact_metadata.py` 至 `parallel06_compact_metadata.py` 版本。六个原索引所写的实际加载 controller SHA，均与登记的完整 source body 相等。

01 与 02 的完整 render 正文逐字相同；四个 compact 控制器的 render 正文也逐字相同。它们消费实际完成的状态对象，将完整 compact JSON 分配到有上限的小分卷，再生成带完整请求及阶段表的总索引。原 single-object / part / index 大小界限分别保留为 58000 / 60000 / 95000 字节；这不是科学域或数值预算缩减。

原 `scripts/resume_20261120/public_actions_followups.py` 与 compact 后继 `scripts/resume_20261126/public_actions_followups_compact_metadata.py` 的完整文本都留树。前者先记录返回并发布；compact 后继进一步先保存状态及 event，再调用 publisher。因此一次 Git 发布失败不能被改写成科学子进程没有执行。原失败记录和后来的真实日志 / 结论，仍按各自来源独立保留。

原输入重建和 followup 执行读取的对象是 source、request、queue、实际 runner input/report/status；总索引与分卷是这些流程的发布产物。这里没有声称仓库中不存在其他历史读者。证明、说明或旧工具若确实读取这些发布路径，必须按第 8 节先恢复原整文件，再使用原读者；不能把新摘要或一个布尔标记放到旧路径冒充原输入。

cleanup 的边界也不放宽。01/02 在其原返回中有完整列表时保留原列表。compact 后继有时只发布删除 / 跳过数量、字节及原列表 canonical hash；该 hash 不能反推出未发布的 runner 原列表。本批不补造该列表，也不把统计记录升格成所有原字节都仍存在的证明。

## 5. 原参数和资源没有截断

全部 158 个 followup 实际命令都至少对应一份仍在现树的完整 step；162 个完整参数位置已登记。对照只把真实 runner 的 `{repo}`、`{work}` 路径代换逆回原占位符，所有参数字面、顺序、数量及 entrypoint 均相等。没有改变预算、角域、径向域、变量数、父点或目标。

这个 argv 对照不等于声称当前队列的所有描述都与旧队列相同。因此原返回中真实记录的 55 个 whole queue 版本仍逐个保留 path_commit、checkout_commit、SHA-256 和实际阶段对应关系。原 scope、summary map、输出声明、cleanup / protect 列表等全部字段，应从该精确历史队列恢复。当前和归档完整 step 是额外的可读参数载体，不能覆盖原版本身份。

01 早期 active queue 清理过 summary maps。四份 `resume-20261126-returned-summary-fields-01..04.json` 完整留树，保留阶段 29–75 的全部原选择器及其原队列身份；76/77 的完整当前选择器仍在队列中。03b 完整 archive001/002/003 及 archive ledgers、04/05/06 的全部 returned-step archives 和 05 complete-evidence 也保持原字，未被本批删除。

六份完整 workflow 记录均保留：Ubuntu runner、350 分钟平台时限、单线程 BLAS / OMP 等环境、Python 3.12.14、numpy 2.3.5、scipy 1.17.0 及各原工作流是否安装 CPU Torch 的区别。原初始执行 head 下的 workflow 可另按 commit:path 原字恢复；不将后来同名 workflow 的 whole SHA 伪作早期已执行版本。

114 个 bootstrap 返回中，有些原 compact 对象并没有完整 command 或 source_sha256 字段。它们的缺项保持缺项。完整初始 source commit、全部原重建源码及 make_plan 足以说明算法和参数来源，但不能据此给一个缺失执行字段编造实际值。原预算停止新增 admission、平台取消及子进程自然退出三个边界分别保留；本批不靠墙钟时间推测某个子步骤已经完成。

## 6. 原完整科学输入和重建责任

01/02/04/06 的完整 `rebuild_a04_chain.py` 保留 source 名单和全部 SHA、28 阶段 continue 计划、每项 argv 以及历史位置重建责任。原 `a04_historical_location_seeds.json` 63070 字节完整留树，含全部原顺序、保护和来源；它不是被删除的发布摘要。

03b/05 的 `rebuild_axisymmetric_so3_warm.py` 保留完整 21 源角色、五次真实 prefix、pulse / hold / mode warm 以及全部参数。其下游 `reproduce_and_solve.py`、`rebuild_fullclosed.py`、`rebuild_closed_warm.py` 完整留树。科学重建不读取本批退存的公开 Markdown 来代替真实 numerical state。

真实 accepted .99 输入的固定恢复为：

- 提交：`60321451c058c6a51da58c37ae5ec6f2d1145f74`；
- 路径：`topics/visible-flex-larger-amplitude/notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz`；
- 2614352 字节，Git blob `6a9dfda743c464af6ae1190208e7157fa66df30f`；
- 已刊完整 SHA-256：`b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`。

这里只核历史树 metadata 和已留 recipe 引用，未读取该大 gzip 正文，不删除它。不能将另一 runner 的 warm、模型、末点或证书冒充本次历史输入。路径、whole identity、实际 scalar、mesh/chart 和后续重解释边界仍由原源码完整负责。

## 7. 六组的实际结论与未返回边界

### 01：77 个返回

[完整 Haar 首方向与归因说明](2026-11-26-actual-frozen-Haar-first-full-direction-and-attribution.md) 及 [固定 Haar 目标说明](2026-11-26-actual-frozen-material-Haar-target.md) 均保留。76 是真实完整科学方向，77 是真实 pure attribution；一个方向被接受。原实际 summary 明确 reach_certified=false、topic_complete=false。这些有限计算不是连续 reach 或原题完成证明。

索引最后记录 11:04:30 UTC 的 budget checkpoint completed，子退出显示“尚未退出”；该显示不被改成实际 returncode 0。官方随后 completed/success 是独立事实。未准入的 78/79 仍仅是完整准备计划，没有未来实际结果。

### 02：49 个返回

[完整 stage49 与终态边界](2026-11-26-actual-run02-cached-SO3-49-and-terminal-boundary.md) 保留。49 的真实 returncode 为 0，秒数为 2521.706654018999，确有完整 actual final；其原有限 metric / geometry 结果保持明确未认证。之后官方 cancelled 不抹除已完成的 stage49。未准入的 pure50 不能由科学报告推补。

### 03b：36 个返回

[gamma-KKT 初始失败与 03b 退出说明](2026-11-26-actual-gamma-KKT-initial-failure-and-03b-exit-36.md) 保留。36 的科学尝试真实 exit1；初始 continuation 未得到所需完整场。官方 success 只表明控制器完成其发布 / 预算流程，绝不是该科学尝试成功。37 没有实际准入；null 的 final residual / controls / statistics 不填零。此前另一 03 run 的 publication failure 也不被这份 03b 台账吞并。

### 04：49 个返回，pair50 未返回

[run04 官方取消及已准入 pair 未返回说明](2026-11-26-run04-terminal-job-with-admitted-pair-unreturned.md) 保留。48/49 的真实科学与纯读返回仍在。索引最后仍是 pair50 running；官方 completed/cancelled 不给出 pair50 的科学退出码、最终点、acceptance、新 typed 地址、永久保护点、完整输出或 pure child 结果。这些未知责任不会替成空数组。

### 05：18 个返回，supported seed19 未返回

[run05 终态取消及 seed19 未返回说明](2026-11-26-run05-terminal-cancelled-with-seed19-unreturned.md) 保留。15 和 17 未完成全部 original normal stages；16/18 为真实 pure 归因，其中显式 H 尝试在 stage30、已完成29段处停止。19 后来准入但没有完整返回；取消和旧日志不允许宣称它有某种特定数学失败、完整末点或已付证书。其实际未公开历史仍属于原分支责任。

### 06：43 个返回，stage42 的纯读失败不被覆盖

[run06 actual43 完整 SOC 返回与终态 budget 边界](2026-11-27-run06-actual43-complete-SOC-return-and-terminal-budget-boundary.md) 保留。43 真实 exit0，秒数2647.705153157003，完整 final 为 `0298be406a26300a40c6e355218e473e0874f42b745a5388a61b86e757c15c56`。有限几何通过仍不等于连续目标证书。

42 的 science_child_returncode=0、pure_child_returncode=1 是原真实分列事实。未返回的 inner pure 原因不能猜；44/45 诊断没有准入。43 不清除42的不同父源、真实科学输出、未读细节或适用 typed 历史义务。

## 8. 完整恢复合同

每个删除项都能不经科学计算恢复原字。对完整交付表中的一项，以以下普通 Git 读取恢复到所需旧路径：

```bash
git show 5358ca0c0a2e48f66af6be474ba1a202d6a935c3:topics/visible-flex-larger-amplitude/notes/2026-11-26-public-actions-45762076394-1.md > restored-index.md
```

该示例仅说明读取，不由本批执行。其余 42 个文件使用各自精确 path；也可直接按列明的 Git blob 取原字。完整字节数、Git blob SHA、SHA-256 三者必须对应台账中的同一版本。不要用刚生成的 JSON 摘要、排版后的 Markdown 或新的 rerender 代替原文件。

历史源按 actual_checkout_commit:path 恢复；历史队列按 actual_path_commit:path 恢复。旧 consumer 若需要原路径，先按该恢复合同 materialize 完整原文件，再运行原 consumer。旧说明中的相对链接未被重写成另一个文件，也没有声称历史读者会自动找到新定位表。

重新运行源码可生成新的研究对象，但不会恢复旧的实际墙钟、原进程路径、随机 / 硬件数值、原 JSON 浮点字面和发布时间。原完整返回对象的逐字恢复依靠固定 Git 历史。本批没有把“可重新计算”改成“新结果等于旧结果”的声明。

## 9. 发布与范围结算

所有新增件已按完整 UTF-8 文本形成各自独立 Git blob，完整交付表提供全部记录。删除由 root 在最新 main 上逐项对原 path/blob/size 实施普通提交；原固定恢复提交不变，不改历史 refs，也不改任何活队列。这只是同一明确旧输出集合的现树操作，不是新的科学准入或计算门。

本批完整保留所有原算法、输入、参数、完整结果说明、失败和未知边界；它不改变数学目标，不迁移证书，不声称新收敛，也不以容量整理替代未付的研究步骤。
