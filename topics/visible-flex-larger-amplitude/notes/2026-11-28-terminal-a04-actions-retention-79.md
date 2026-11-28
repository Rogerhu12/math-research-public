# RET79：三次早期终态 Actions 的完整发布输出退存

日期：2026-11-28。此项只整理已经终态的公开运行 44748103105/1、44758209061/1、44772201880/1。它不启动科学计算，不改当前求解、参数、队列、证明或输入。提交与当前树删除仍由 root 统一执行。

## 1. 本次保全对象与准确边界

候选是七个由原控制器生成的 Markdown 索引／分卷，共 **301981 字节**。每个原文件均小于100000字节，已完整读取；没有读取大型报告、数组、gzip、NPZ、二进制日志或旧runner缓存。全部原始发布字节在固定提交

`2036c522e3a44059f13887dcce01d2b72122c4de`

仍可完整取回。该提交的完整题目树元数据已逐项核对七个候选的Git blob和字节数。提交时还须按当时fresh HEAD核对；若某对象已变，不能套用这里的旧身份删除。

| 原路径（题目相对） | 字节 | 完整Git blob |
|---|---:|---|
| notes/2026-11-20-public-actions-44748103105-1.md | 90741 | `8e069726d03ca7909f2825481ce86f1b741b4ed4` |
| notes/2026-11-20-public-actions-44758209061-1.md | 4567 | `80354729c266b14264ac3eccbe3eb7cab21c5a94` |
| notes/2026-11-20-public-actions-44758209061-1-part-001.md | 54625 | `38b1a823905466a635ce153d4ad1a834129a0f8a` |
| notes/2026-11-20-public-actions-44758209061-1-part-002.md | 56899 | `65f6ad7d6461aca0d0894d8179c7bfedaaba834f` |
| notes/2026-11-20-public-actions-44758209061-1-part-003.md | 39454 | `19c2910610084df3d4a29bd69da375422273190c` |
| notes/2026-11-20-public-actions-44772201880-1.md | 3579 | `044268db9633541a710b0ec8c4c655b3a2d8ca9b` |
| notes/2026-11-20-public-actions-44772201880-1-part-001.md | 52116 | `2c01be7e02190636677884844158df95f4352694` |

两个完整JSON各有不同职责：

- [来源／完整参数登记](../computations/terminal-a04-actions-retention-79-source-parameter-registry.json)：40473字节，SHA256 `667455541a6fd9490944890ce876c054a8d059455a46b532c76d03f215e1a9c8`，blob `87cd9354085676f85ad309e2086ba887a76105d4`。
- [实际阶段、结论及恢复登记](../computations/terminal-a04-actions-retention-79-complete-provenance.json)：84839字节，SHA256 `803d2fe26084e0abc98e71dd1a80aecf46f8e6d195557a4312aa2a0aaf56c7a6`，blob `a15ae85f2ebb29a7c664724819ca37408808ade7`。

前者明确分开**41份当前题内保留文件**、**3份题外workflow**和**10份实际历史队列版本**。只有第一组是当前题目路径应保持不变的guard；历史队列不是当前同名路径的身份断言。旧队列可以有更多或更少步骤，不能拿现在的最终队列替代实际当时版本。

## 2. 完整生成来源与输入恢复

三次初始源码提交分别为：

| 运行 | 实际初始提交 | 控制器 |
|---|---|---|
| 44748103105/1 | `e2c5e4a538d47d64ba62900e4271137e2312778f` | 原 `public_actions_controller.py` |
| 44758209061/1 | `4ae162196553e6ce2ef28a6a35bea2d0d567883e` | 分卷 `public_actions_controller_v2.py` |
| 44772201880/1 | `e0d4892aabfec77f64c33a9cc34da9ff3cf39ba4` | 同一分卷控制器 |

三个完整workflow在各实际初始提交的字节均与登记原件一致。它们保留350分钟job限制、20000秒controller预算、Python3.12.14、NumPy2.3.5、SciPy1.17.0以及单BLAS线程。这里没有改变任何资源参数，也不把平台终态时间解释成科学完成。

原完整 `rebuild_a04_chain.py` 的36560字节及其全部 `SOURCE_NAMES`、`SOURCE_SHA`、`make_plan` 和28个continue阶段仍在当前树；完整63070字节位置参数也保留。嵌套 `reproduce_and_solve.py`、`rebuild_fullclosed.py`、`rebuild_closed_warm.py` 全文保留。历史接受输入是固定60321451提交内的真正accepted099 gzip，完整Git身份和既有SHA由既刊RET63来源登记复用；本批不读、不删、不复制它。

每个独立run都从自己的真实输入重建开始：accepted099 → 五段原prefix配方 → 完整pulse／hold／mode warm → 原28阶段 → 当时完整后续队列。请求中的prior_run_id仅记历史来由，不能被解释为读取了此前runner的失存raw。依赖源码完整固定在各真实执行提交；17个实际followup入口的全文SHA均与当前保留原件相符。

十份历史队列已从其实际path_commit读取完整对象，全文SHA逐一与原返回记录相符；24个已返回followup的ID全部出现在对应真实队列中。全部原argv、输出清单、摘要字段选择、父输入与清理模式保留。完整实际展开命令另原样记在实际阶段登记中；原bootstrap记录没有发布的命令／source字段保持缺失，不用配方反填“观察值”。

## 3. 七个发布文件为何可按生成输出整理

原 `Publisher.render/publish` 从本次status的完整completed记录和请求生成这些Markdown。v1采用单篇95000字节上限；v2完整保留每个record，再按原58000字节分组和60000字节卷上限写出。它们是发表层，不是新的科学方法。

完整科学入口读取原argv指定的同job父NPZ、carrier、node、profile、报告和位置manifest。已核17个入口没有把这些run的公开Markdown路径作为场输入。旧数学说明确实链接到原索引和分卷，因此不能说“无人消费”：本批为这些历史链接保留准确全文件恢复映射。九份实际数学结果说明全文留在当前树，既不删减其数值，也不抹掉失败、条件结论或未知。

阶段登记共108项，即36＋42＋30。每项定位**完整原JSON对象**，不是选取几个有利字段。所有原metrics、完整input/output身份、elapsed、source、parent、cleanup、summary_errors、missing_outputs和setup_error都由固定原卷逐字恢复；原来没有的字段仍没有。两个exit1的followup对象在新登记中另外完整保留，避免以后只看“后次成功”而丢掉它们。

恢复旧发表字节只需在隔离的历史checkout按准确路径执行：

```sh
git show 2036c522e3a44059f13887dcce01d2b72122c4de:FULL_REPOSITORY_PATH > FULL_REPOSITORY_PATH
```

也可用登记的完整blob取回同一对象。整个文件的bytes／SHA256／Git blob均已记录。此处没有要求为退存重新跑科学，也没有新AST、fixture、benchmark或重放前门。

从完整原脚本重新执行科学会生成新的实际输入和输出身份；不能许诺跨runner浮点字节或耗时相同。完整原Markdown的历史逐字恢复与新的科学再生是两个不同的合同，均未混同。

## 4. 44748103105：真实两次失败、后续pair成功、最后出版故障

官方终态为failure，updated为2026-11-20T14:57:22Z。原公开索引只保留36个已返回阶段：28个bootstrap均exit0；随后8个followup中两次exit1完整保留：

- `continue-same-parent-full-phi-margin-pair-01`；
- `continue-R671-full-phi-first-01`。

独立的新ID `continue-same-parent-full-phi-margin-pair-02` 后来真实exit0，两支各完成一个方向并接受alpha=.5。共同父为c4a3，实际mu=.0007539530259341321；.992支Phi为9.559233976874516e−8，.998支为9.41309835591355e−8。其完整比较、所有输入、两份report/final身份及QP未收敛责任保持在原第36记录和当前数学说明中。有限点通过不变成reach或README完成。

当前保留的完整结果说明还记录了真实原日志SHA `3946ad23c6a6ada7fb2e6224e7ed3a70dd6b713b12416f35314e43a1457ca09f`：最后R67102在14:51:09.886 UTC已经启动，14:57:14子进程已进入finish_record，但单篇render超95000字节而未发布新记录。这里依据已刊完整说明保留该事实，没有重新读取原大日志。

因此，该末步不是“没有启动”，也不能补成数值失败、接受或零耗时。其科学退出码、最终数组和目标仍无可核记录。本批只保留这种已知与未知的准确分界。

## 5. 44758209061：官方success不等于全域目标完成

官方updated为2026-11-20T20:29:57Z，42个已返回阶段的进程码均为0，最后控制器阶段为 `followup_budget_checkpoint`。28个必要输入加14个followup全部参数与结果链保留。

原六个全方向真实接受，但每次QP仍为iteration_limit。径向二分后共同父泛函仅小幅下降，不能把细规则Phi直接与粗规则Phi相减；实际二阶转移费用保持原报告，不因位置误差小而称整场逐字相同。

R671场7fd352的准确连续度量读取实际为 `checkpoint_unfinished`、`complete_scope=false`。已覆盖部分的严格supremum下界.011952653235030912足以排除该场1e−6目标；全域上界仍null。这个反例不证明整个模型无解。

最后固定PCG／SOC仅真实接受原ray，alpha=.0625，Phi从8.52075845296275e−8降至8.454713899420836e−8，maxGram .01204892877730308。QP256步后投影梯度5.001495924767116e−7，容差2.2660999355136002e−12，仍未满足停止条件。SOC虽构造了满秩26行修正，全部旧行复核最小slack为−.00010676790261705001，因而不可用；修正真Phi和product没有执行，保持null。原ray的实际接受不改写成SOC成功。

同模型、同profile并不使c4a3、e08、daff、97fd、7fd和3ef8成为同一场。九份当前完整科学说明保留这些区别及每个raw身份、参数、有限或连续结论。

## 6. 44772201880：独立新warm、已付半径和未返曲率

官方终态cancelled，updated为2026-11-20T22:09:40Z；取消原因没有在此证据中建立。30个阶段已经返回，原末索引仍显示完整sixjet曲率步骤running，不能从平台终态补最终曲率报告或完整reach。

本次warm的实际SHA为 `6b826d9923523f7cd61498578525be39b6b640dc5b61c926b1fe6f7e83166cb5`，与历史79c161不同。其6077阶段真实状态为restoration_failed且进程exit0，不能套成别的run的iteration_budget。相同环境声明不足以消除跨runner差异，原因未归因。

实际continue终场756936ee已支付自己的全922胞首jet和半径续化。body直径上界4.099300336920071支付body目标4.1；加原条件四marker后的4.101300336920072并不小于4.1。相应support、整像见证距离及条件held/grip下界全文保留。没有把它们移给run2，也没有据首jet和直径补完整曲率、reach、统一metric或研究完成。

## 7. 当前树保留与执行范围

本批不删除任何完整source、proof、配置、队列、原输入、位置参数、九份科学说明或活22及以后运行材料。RET63的完整来源／输入合同只用于已有a04配方，不继承其后期run的数值结果。原accepted099、parent91、缺完整来源的Nelder／port／其他排除项不动。

全部新工件只作为未引用Git blobs交root。提交前的fresh身份比对只防止删除对象发生变化，不是科学准入门；不新增研究判断、场读取或求解预算。净容量变化由最后完整delivery按实际新增四件计数，七项删除范围不扩张。
