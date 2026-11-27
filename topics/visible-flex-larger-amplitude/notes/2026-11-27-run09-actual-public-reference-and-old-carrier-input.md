# 09 真实公开输入、固定目标与完整旧地址载体的独立生产入口

## 1. 状态与范围

这是完整可执行的输入生产与来源绑定，**尚无这次生产器的 Actions 返回**。源代码和全参数已经写成；本文所列 warm/reference 值来自真实 run `45943410994/1` 的阶段 1、2。程序只在公开仓库 Actions 执行原 scalar/观测载体重建，不调用物理场、全局 Jacobian、normal 根或优化方向。

旧 `freeze_run08_fixed_chart_and_restore_run05_carrier.py`（完整 SHA `105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361`）不改。新文件按明确的 run09 返回建立独立来源，不将 run08 的 7c4c 图、4924 模型、eeb5 参考或 56b1 观测载体换个标签继续使用。

这也不从元数据 SHA 改变推出数学度量不同。独立绑定的是完整当前定义和实际工作字；是否与历史数学目标相同，要按完整准确 scalar、材料图和定义判断。输出 `same_mathematical_g_claimed=False` 只表示这里没有作出该主张，**不是“不相等”的数学结论**。不继承历史度量数值、几何证书或缺失分支的成功状态。

## 2. 已真实返回的全部输入

公开小卷为：

`notes/2026-11-27-public-actions-45943410994-1-part-001.md`

整文件 **22456 B**，SHA256：

`5e3732096b95ccc65f7fc70cc2b4e5ba4ffc67023c444ce4f93762c7d765a1be`。

其中 warm 为 completed/0，185.562061473 秒；完整4e reference 为 completed/0，313.366331495 秒，实际源提交 `db0249db862102b92705227688a035ffde46b41a`。这些是紧凑公开原记录的值，未在本机重算。

| 角色 | 完整字节数 | 实际 SHA256 |
|---|---:|---|
| `current_warm_bundle` | 8767118 | `3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c` |
| `current_node_report` | 554141 | `918ccdf1a132ca4ba50e0fa97cbb53f7aeabac8f63dc24e7eada64a18fb80269` |
| `current_scalar_input` | 14227850 | `83e65252955298326934ee371ace2391ea9161b69a9289ce4a3c5bd74c67c986` |
| `current_carrier` | 227205 | `792a132357861684ae01b15b2276c0259583ef27c44387288f424e08d6b488bb` |
| `current_preparation_report` | 29802 | `4cc93d406cc1882771d2ebabb34856e7ed195fb6cdb6b361e1b213e504193ad2` |
| `current_reference_bundle` | 866176 | `2ab8593585286a6c4eab78d107f83a02d8332e7ae1747253534264506b3da7f2` |

实际 reference model 是 `d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75`；实际 scalar profile 身份是 `5de7dcbb0fd1daacad7c20b276120dfc52b9d1f2eb67890300c9afc56242b3ed`。准确 scalar 参数投影仍为完整 `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`。

当前 reference 的 scalar 实际返回 1995 个活叶、requested tolerance=false、complete tail=true。旧载体重建使用的是历史**2397**活叶及其原准确运算；两者不混称同一数值积分表，也不把未达当前 requested tolerance 改成通过。

当前完整 warm SHA 实际等于原 `3df37dd...`。原完整 envelope 来源保存其全160图投影 `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e`。新程序仍从当前 warm 的完整 `qjets[0,0,1:161]` 和当前 reference 的完整 `initial_core` 分别读出全部160个 binary64 词，与实际模型逐字核对，不能仅用文件名、相同形状或相同命令代替。实际完整 mesh 仍要求原 `eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262`，全部923个准确 affine 节点仍须原 bee5 公式一致。

## 3. 两个完整新执行体

### 3.1 纯输入绑定器

`actual_public_reference_input_binding.py`，44907 B：

`306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a`。

它仅使用 Python 标准库。独立合同固定 run09/1、实际 reference step ID、完整公开卷 SHA、真实六文件 record、d449 模型和5de7 profile；不会接受一个任意自报 complete=true 的新模型。

它依次核验：

1. 显式选择的完整 public warm/reference 文本、唯一实际记录、completed/0、原 bee5/5613/067b 与4e source/commit、完整真实输出及原参数。
2. 全部六文件的完整 SHA/bytes/path，以及真实 preparation 内的全部输入关系。
3. preparation 的全部七个 source roles、完整当前模型 canonical 身份、scalar profile、全部 scalar 参数投影。
4. 完整 warm NPZ 的成员表与实际 mesh/core/前三词/width/H 字；完整 reference NPZ 的14成员、嵌入模型、全部160 core 字、mesh/width/H/radius 和完整 scalar cache。
5. 当前 observation carrier 的完整文件、原 mesh/前三词/width/radius/正 a 载体及其真实摘要。
6. 完整923节点报告、准确首末点、原宽度、scalar来源和实际 supplied locations/provenance 两个整体文件。

NPZ 读取只解析已有 NPY 的 primitive dtype、shape、完整字及有限性，不构造物理场或重新积分。旧同径向材料网格是否相同仍由生产器/后继 memory 真读全数组比较，不由这一层预填。

### 3.2 完整生产器

`freeze_run09_public_reference_and_restore_run05_carrier.py`，47041 B：

`9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18`。

它硬钉上述完整纯绑定器；从105289完整派生，不导入或改变旧场优化源。原 `read_public_step`、`verify_projection_origin`、`exact_node_definitions`、`counted_tail_class`、`compare_member`、`array_record` 六函数 AST 全同。更强地，从取得 `deep_module` 到全部 old/current plan 比较结束的**整个原重建块逐字相同**：

- 原深尾准确定义、固定优先级、序号及拆叶次序；
- 原历史2397活叶控制、原不确定度/完整profile身份和radius工作字核验；
- 全7377个原正观察值及误差、1845 legacy + 5532 Gauss；
- 原 `make_plan(...,order=6)`；
- 原 `np.savez_compressed` 关键字次序、dtype和全部数组；
- 只有整文件 `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`、**227202 B** 一起命中才建立旧载体身份；
- 完整旧/新 plan 数组、Gauss词、cells/u全字读取与比较。

失败仍保实际失败 report，不降为少量旧节点样本，不从已知 SHA 造 raw，也不声称旧 warm/节点 JSON 被重建。准确数学 projection 可以由当前真实 scalar 读取，但原记录的文件身份仍在旧 deep 定义中如实保留。

## 4. 公共卷追加与不可变证据

生产器执行后，控制器会向同名公开分卷追加新阶段。因此新合同不要求后来的 HEAD 同名文件永远保持旧 SHA。

CLI 显式传入 warm/reference 公开文件和各自 SHA。生产时先核整22456 B/5e373，再将**整份原文本**复制到 fresh runner 输出：

- `actual-public-warm-immutable.md`；
- `actual-public-reference-immutable.md`。

两份当前来自同一小卷，但合同允许分别核对角色；每份保完整原 repository relative path、生产 checkout commit、原完整 file record 和实际 snapshot record。复制前后原文件再次核等。后继读取实际不可变 snapshot，并重核完整文本 SHA、run标题、唯一记录及其全部当前文件关系。原公开文件的后续追加不撤销已绑定的真实旧记录，也不替代该固定 snapshot。

这些副本、原始NPZ和生成目标/绑定 JSON 全部只留 runner，不入 Git/Release。元数据里同一路径若出现两个不完全一致的 SHA/bytes record，会拒绝；后继不能用“最后一次覆盖”消掉较早来源责任。

## 5. 固定目标的完整定义

新 target schema：

`independently-frozen-actual-public-run09-scalar-and-material-chart-v1`。

在任何新场或方向之前，固定：

- 完整实际 public 输入证据及其身份；
- 完整当前 reference model、整 reference bundle SHA；
- 原准确 scalar 参数和完整当前 scalar profile 定义；
- 全160材料图 binary64 词及原数组 SHA；
- 全923准确 affine 节点及完整身份；
- 原精确宽度、S/domain和来源。

数学表达仍为固定准确 $ds^2+a(s)^2\,d\Theta_0^2$，当前自由 core/H 不重新定义它。独立“定义身份”包含真实输入来源，不将文件元数据的变化等同于数学对象的变化。

`same_original_fixed_chart` 在这次新合同中是**完整词的实际相等结果**；`current_and_historical_fixed_chart_words_sha_equal` 同时明确这一范围。整个数学 g 是否继承不由这个单字段代替。输出另保 `historical_metric_relation`，明确未作历史数学同一/不同主张。旧场值、证书、分支完成状态均不转移。

## 6. 完整材料地点与未来入口

新路径绑定 schema：

`material-envelope-actual-public-run09-fixed-target-binding-v1`；

内部兼容记录 schema：

`actual-public-run09-fixed-target-and-historical-carrier-binding-v1`。

主要键继续是 `fixed_target_definition`、`independent_fixed_target_binding` 及各完整 canonical 身份；新增完整实际 public evidence和来源绑定器身份。纯 validator API 保原全部五个实际 solver 文件 record参数，同时重读其记录中的第六个 warm 文件。

此生产器只付输入，不代替完整材料包络消费者。后继仍须真读所有原 P0、全部旧/新 carrier × quarter grid、当前 supplied locations、两曲率分支/半径/两见证符号和全部 typed 行。历史 literal 角重新解释为当前固定材料图 phi0 的地址，不能自动称跨表示同一物理点或迁旧几何值。

run07/1 已 completed/cancelled，step4 未返回；未知历史不是空集。run08/1 原95559还须按真正返回情况消费；这里不预填其 final、typed优先级或报告 SHA。完整新解析 frame/J3 家族将另以这份实际输入作来源绑定；原32段、全部自由量、原范数、全C、真实筛和全局隐式链不因输入生产缩减。

## 7. 完整再生、实际静态核与 Actions 参数

纯标准库再生器：

`derive_run09_public_reference_input_sources.py`，64621 B，

`cc46e9b8bcaaddce8640443abcb780ba3e46985c281966671c940ee508604d0e`。

它消费完整105289父源，核全部字节/完整 SHA，用24个明确原byte区间和每区间原SHA生成整个新生产器，并输出内嵌的整个44907B绑定器。实际已经执行这个**source-only**再生器，exit0，两个输出精确得到上述完整 SHA。实际 AST/compile、重复 literal dict key、尾空白、六保留函数和完整重建块检查通过。没有科学导入、数值fixture、F/J/root或本机scalar计算。

完整单步参数文件：

`computations/run09-actual-public-reference-input-ready.json`。

它包含已实际存在的六输入 record、原/新 source身份、所有28个argv词、6个runner输出和45个标量读数选择器。原2397/全部观测/准确尾参数未变。没有 cleanup，不删除真实输入、reference缓存、public证据或未知分支。

新输出目录为 `{work}/run09-actual-public-reference-run05-carrier`。controller的 parent_bundle是确实存在的本run reference。生产器实际返回前，不填该目录中的任何 generated SHA，不假称已命中旧 dc5。产生真实返回后，完整新 memory/科学入口才能读取这份真正绑定；这属于必要输入构造，不是额外求解前置 fixture 或新的题目完成标准。

## 8. 后续实际责任

本次不声称准确参考所有误差已包围，不声称任何 normal 根、连续同支、全域度量、完整全t嵌入/reach、握持或非全等证书已经完成。R709/R711/R713/R715 的条件误差与物理六jet责任保持；新工作target/profile差额仍须同场读取。

输入来源完备后，继续实际完整解析 frame/J3 求解、原永久几何筛和后继精化；不因本次生产或静态核成功把科学任务结案。

## 9. root复核与实际单步准入

root实际运行完整标准库再生器exit0，六个原函数AST与整段2397/原save/完整dc5比较正文逐字保留，两个完整输出分别306b/9e3d。root已完整读实际第2条返回的全部argv、输入/输出身份与无missing/summary_error记录；单步完整原对象追加09队列，原reference步骤逐对象保持，未删任何pending。此处只登记已排入的完整执行参数，生产器完成与目标身份仍以未来真实返回为准。

完整生产器保留已锁字节的末EOF空行；默认Git检查报告这一样式项。为保9e3d及全部再生/后继pin不变，源码不作无数学作用的重排；仅排除blank-at-eof后的其余空白检查通过，科学guard和完整原算法未变。

## 10. 实际第3项已返回：完整载体与当前固定目标

root 在真实 pull 后逐项完整读取 [实际第1卷（阶段1–3）](2026-11-27-public-actions-45943410994-1-part-001.md) 的第3个完整 JSON：该卷33693 bytes，whole SHA256 `837901528194ed8b23f5fca8b45d95520d5e490b5420d7b3772de5d3027d7e62`。这不是原输入快照5e373的替代；两个5e373原卷快照仍在本runner作为后继完整输入。

实际步骤 `freeze-actual-run09-public-reference-and-restore-whole-run05-carrier-20261127` 为 completed/exit0，外层368.9653335570001秒、内层366.9169047739997秒。完整source为9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18，实际源码checkout `ba42fd2819a2ee9638d3044539076ff3e39de67f`。完整原28词用户参数及Python实际argv逐项仍在实际小卷；队列path_commit为 `1f102dc8df41ada504a9d30e56bad92be01bde90`、whole队列SHA `927dcb2afd9198c86a8f1e17920dea3e641ff841ef5f1ed32a2d8235a85b336f`。没有推测未返父SHA。

实际报告确认完整旧载体dc5/227202精确命中；全部old/current材料地址相同，当前与历史完整160 chart词均为90e6且逐字相同。原2397叶重建完成，旧/重建scalar profile均为 `e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350`。这2397指旧载体重建分支，不能改写为当前09参考生成时的1995叶。

实际固定目标canonical身份为 `7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a`；input binding canonical身份为 `21a44bdb4ab28c00b57256094075499e2434c30af6db4b788ff94a6f691cfa53`，canonical与whole-file SHA分列，不混用。实际输入证据canonical身份为 `3a0c2d8e7a99a5c2cfeb61e24ae4c5e249ceb4badb88dfa4034f3188a9414794`。完整实际输出如下，路径均在09 runner的 `research/run09-actual-public-reference-run05-carrier/`，raw不进入Git或artifact。

| 输出 | bytes | whole SHA256 |
|---|---:|---|
| `report.json` | 769358 | `f857e675af324fd9e0b540f4d2746e293879bbdb5ab3fe57e41688efa0fd5a2e` |
| `run05-observations-restored.npz` | 227202 | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` |
| `independent-fixed-target-definition.json` | 97334 | `68d76e31e685995a3245a824d3fedf7a44cf862002ae60be4d541b6c64fbef99` |
| `material-envelope-carrier-binding.json` | 430906 | `2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d` |
| `actual-public-warm-immutable.md` | 22456 | `5e3732096b95ccc65f7fc70cc2b4e5ba4ffc67023c444ce4f93762c7d765a1be` |
| `actual-public-reference-immutable.md` | 22456 | `5e3732096b95ccc65f7fc70cc2b4e5ba4ffc67023c444ce4f93762c7d765a1be` |

当前六文件whole身份、d449模型、e640标量参数、eff967网格、90e6完整chart及ba5a准确节点都由真实文件核入；不是源常量或文件名充当读回。`same_mathematical_g_claimed=false` 表示未主张新旧数学目标相同，且报告明确 different metadata SHA is not mathematical target inequality；这也不是声称二者数学不等。旧Phi/场值未继承，exact_chart_conjugacy未主张，旧分支未完成，未读历史未冒已读。

F/J/root实际调用均为0，故本项完成的是必要完整输入生产，尚不是新物理场、收敛、全时reach或完成标准。六个输出全部存在，missing_outputs为空；两条summary_errors仅为成功报告没有可选 `failure.type`/`failure.message`，不能解释成生产失败。cleanup删除/跳过均0。后继须完整读取430906-byte绑定、97334-byte固定目标及六真实文件和原载体，由新的完整解析frame/J3入口实际求值；07/08未知typed责任继续保留。
