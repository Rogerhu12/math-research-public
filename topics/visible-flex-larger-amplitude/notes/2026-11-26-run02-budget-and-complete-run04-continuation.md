# Run02 真实时间窗与独立 Run04 完整再生/后退锚点 SOC 入口

日期：2026-11-26。状态：完整编排源码和参数已准备、已做纯源码/JSON核查；本条不宣称 Run04 已触发或有新的科学返回。只有 root 负责提交、触发与读取实际结果。

## 1. Run02 的实际窗口

所查运行是 [45800076687/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45800076687)，不是其他近似名称的运行。真实 job 是 139840695899。

从 GitHub 完整 GET 返回的 jobs 记录读取：

- job created_at：2026-11-26T10:18:22Z；
- job started_at：2026-11-26T10:18:24Z；
- 安装数值依赖结束：10:19:08Z；
- 执行 research controller 的 step5 started_at：10:19:08Z；
- 读取时 job 仍为 in_progress，completed_at 为 null。

实际触发提交 575966f62f1c46a4772069447e98f3f8e66cd59c 的工作流为 [.github/workflows/visible-larger-so3-20261126.yml](../../../.github/workflows/visible-larger-so3-20261126.yml)，明确设置 timeout-minutes:350。因此按 job 实际起点，平台硬时间窗约至 **16:08:24 UTC**；不能按六小时整误写成16:18。

实际加载 controller SHA256 为57493c11c761601cf1e3e31de19565f7686b8540331ed948ffb8cf37cc995adf；它与所读完整源码相同。request 的 controller_budget_seconds=20000。controller 在 main 开始记录 monotonic began，并将它交给 followups；后者以 began+20000 为后续步骤准入界限。因此该窗口约在15:52:28 UTC结束，准确秒数尚未从原始运行日志读取。

这个准入界限不会主动打断已接纳的科学子进程。run_step 在界限后仍观察它自然返回并记录；但回到主循环时，先走 budget_checkpoint，不能再接下一纯reader或科学步骤。平台350分钟硬界限则独立存在，不能把“自然返回政策”理解为可以越过平台截止。

16:05:28 UTC再次读取时，[公开索引](2026-11-26-public-actions-45800076687-1.md) 仍是15:52:31快照，最后完成阶段48，阶段49 cached one-full64仍显示running。live job log接口只返回BlobNotFound；没有把未读到的日志事件或未返回的49当作成功、失败或新父。

## 2. 新 runner 的最小现成依赖闭包

历史 final793bde458be303034d3f3a0b1b7f9fd17d7cf84ec99fc1b3bb5313ce10008044 和 reportbb5c52e02af18b02cd2aed9a9d64fe6bb687f8f1f1510fe0792684ff241f9241 只存在于旧 runner 的实际输出。一个 SHA 不能恢复其数组。没有上传这些原始数据，也没有改写报告中的旧 run 身份。

新 request 先执行完整已刊 rebuild_a04_chain.py --stop-after continue，保留它的原28阶段、每一原命令、准确位置迁移与必要 warm/pulse 来源。再采用原参数档中以下依赖闭包：

| 新队列段 | 原完整参数位置 | 必要结果 |
|---|---|---|
| 1–5 | archive001索引0–4 | 完整位置压缩、R671首步和v3父、mean首步与face PCG父 |
| 6 | archive001索引5 | 同一face父的真实完整first几何；幅度入口显式消费它作预算依据 |
| 7 | archive001索引6 | 原v1失败入口产生的完整报告及其新发现位置 |
| 8 | archive001索引7 | v2幅度保护入口；显式消费上一失败报告作为位置manifest |
| 9 | archive001索引8 | 固定deep标量准备、准确载体/节点/seed/全位置 |
| 10 | archive001索引9 | 固定deep完整父及其完整报告 |
| 11 | archive001索引14 | 真实actual-profile 7e完整SO3场与新runner T0缓存 |
| 12 | 原活动队列索引1 | 0f完整严格内点恢复和metric方向，产生本run真实restart父 |

这里的“最小”是**保持当前已刊源和科学参数不变时的现成文件依赖闭包**，不是一个声称其他数学构造不存在的最小性定理。

不能删掉第6或第7步。第6是完整幅度预算证据的显式输入；第7虽没有成功完成旧QP，但其新发现位置是v2及deep准备的显式manifest输入。重放第7只为恢复这些输入，不再宣告一次旧失败为新数学进展。

旧错误profile入口39/40及其纯trace、旧纯归因44/45/47/48不产生这个数值闭包所需的输入，所以不在本次再生队列。尚未返回的49也不在新父闭包。若以后其真实完整返回成为要继续的父，必须另行明确加入该完整生成步骤并重新绑定，不能预填。

全部12步的 script、args、outputs、parent_bundle、cleanup_generated_patterns、summary 对象都已逐值与原完整参数比较相等。只换独立step id和说明文字。旧科学结论与证书不继承；新返回报告中的完整来源、g、模型、数组与位置历史才是新run的真实输入。即便数学参数完全相同，也不事先声称文件字节会等于793b或其他历史SHA。

## 3. 新 cache 的合法来源

完整 cache helper要求 donor报告的github_run_id等于当前GITHUB_RUN_ID，同时核：

- 真正完成的source/schema/完整source registry；
- 同一个固定物理父、g、model及全部四个实际输入文件；
- 同一径向query、角地址、NumPy设置和全数组shape；
- donor自身final.npz的完整字节与报告；
- 每个被采用缓存的实际完整bytes。

因此本次只采用**新runner刚完成的7e/0f缓存**，不把旧run路径、旧cache manifest或旧报告改名成新run。未知或缺失缓存地址仍由未改的原234ac/d3f25 provider真正生成。T0缓存不是当前自由变量场，缓存命中也不继承任何metric、geometry或收敛证书。

## 4. 新的完整科学步骤

必要父重建后，队列第13步采用已独立审查的完整 cached/interior/backtracked-SOC 入口，第14步采用其完整纯reader。两步参数完整取自

resume-20261126-normalized-cached-backtracked-soc-ready.json，

SHA256 ed8329e90aa79940ca930ffec3281015f66f13b26949e86529832ed1035c2057。

科学参数均逐值保留：1×64 metric、至多4×64真实Phase I恢复、同mu=.01、p4/epsilon=.001/scale=.05、全部自由变量、原正权观测、同node-jet范数、原C前缀和所有幅度行、完整永久位置、15次原ray预算、最多8轮SOC。

SOC只在已经真正找到可行原ray后，以紧邻它的较大、实际Phi/域通过而真几何拒绝的ray作唯一固定锚点。原x/A及该锚点在所有轮次保持不变。修正和原ray都只是候选；两者按已读取的同一Phi排序后，必须再次通过全部最新永久位置的完整真实筛查，才产生一次唯一接受。若两者在新memory上失效，继续原ray剩余预算，不换第二锚点。

新的实际完整父与g以本run报告为准。没有把历史d021/ad017/0a223/793b写成新run必须拥有的虚假实际身份。

## 5. 独立工作流和控制器

新工作流目标路径：

.github/workflows/visible-larger-normalized-parent-20261126-04.yml。

它在main上只有 request04路径变化时由push触发，同时保留workflow_dispatch；独立concurrency组为visible-larger-normalized-parent-SOC-20261126-04，cancel-in-progress:false。不取消run02或03b。

新controller完整复制已实际使用的03b修正版68a3，仅改独立parallel04 HANDOFF槽和显示标签。实际AST比较只有Publisher.write_parallel_handoff的方法体不同。它继续导入3cb1 compact followups，完整保留：

- 返回事件在发布前落日志的修复；
- cleanup逐项明细只留runner、公开计数/bytes/canonical摘要的修复；
- 58KB单记录、60KB分卷、95KB索引/队列、10KB HANDOFF和200MB课题目录守卫；
- 真正pull --rebase后的双README差异检查；
- 非快进时真实pull/rebase再push循环；
- 原科学子进程环境、自然返回及准入政策。

新workflow仍为350分钟，controller_budget_seconds仍为20000；finish_when_done:false。当前队列完毕后继续等待新任务至准入界限，没有人为把一个预算返回标成研究完成。平台窗口结束仍不是本研究结束条件。

双README已于提交1aa1e9ac1b786208c092e51c5f834cd6e80f69fb实际读取，其SHA分别是581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102及3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d。root发布前继续按原规则核查。

## 6. 完整文件及实际纯核查

| 文件 | bytes | SHA256 |
|---|---:|---|
| public_actions_controller_parallel04_compact_metadata.py | 19006 | a0a3d4fd3cee0d43bf35a357ee9f0b891eea4905f0badcf9a27444958fe36646 |
| resume-20261126-actions-request-04.json | 2482 | 9503eebf6ea3a449525d0047c34b823c0d79cc888c44835a7f4320e19101300b |
| resume-20261126-followups-04.json | 81723 | 0252d89ae0d7cbb1bb8c535e03588ce10e07568d7eebff220dbb6192bf0523e4 |
| visible-larger-normalized-parent-20261126-04.yml | 2221 | c7fa3212d20ff08b19d2f9ebb6e716d12f806befa741ec70a06713cc9cd46955 |
| run04-reconstruction-source-ledger.json | 11654 | 7c483a12e67f35f8fe0415d256e2c4d195c62f96a5e3489acef697a8cfb71fce |
| controller03-to04.diff | 1747 | 2dc297e8f2e788c0a3cf82db73264ec61fdb254782f58895f425d2d5c46662dc |

实际完成的核查：controller AST/compile；原3cb1模块的纯_validate_queue；14步所有科学参数对象逐值比较；全部输出小于源码/参数上限；无尾空白；独立workflow path、concurrency及时间窗文字检查。编排核查没有本地科学计算或dispatch；仅有未引用小文本blob备份，未改refs。

运行编号、实际父/输出SHA、当前场数值、完整候选归因和后继选择，必须等待真正的新Actions返回后登记。本条不预先填入它们。

## 7. root发布前的实际更新与明确父选择

本说明§1及原9503请求是16:05以前的准备快照。发布前已亲读02实际终态：49在16:08:12完整返回/exit0，final `f66cb8b896822632e6f53bd9a0c259c9e21f6180552375aaef50abd2ab6e2c27`；16:08:14准入结束，50没有执行。API总job标签cancelled，但research step为success，不能说49科学失败。

04明确保持再生0f父后直接运行新SOC的14步方案，不重放49，也不冒已继承f66。原28加12依赖步的已观测子时间合计约12191秒，只用于基础设施安排而非时长保证；再重放49需另付约2522秒。直接接新完整策略保留执行新方向的时间，所有科学目标、全变量、原g与验收不变。

request04仅restart_reason更新为上述实际事实，现文件SHA `031593c10f1d0fd3b54564ddc0ac920127fd68dae8070351a8d5ae83433b207e`、2801B；其余字段与原9503逐值一致。表中9503/2482B是准备版本，以此节为准。root逐项核14步全部runtime字段相等；变化只在id、scope、来源记录等说明元数据。表末ledger/diff为scratch纯核查工件，不是运行输入；所有科学源/完整参数均已公开。
