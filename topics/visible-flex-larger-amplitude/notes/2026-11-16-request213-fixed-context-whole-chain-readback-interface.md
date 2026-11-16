# Request213：完整39查询固定语义上下文与单份必要读回接口

作者：OpenAI ChatGPT（AI 协作研究助手）  
日期：2026-11-16 UTC  
性质：独立公开Actions接线；不含本地科学、import、AST、编译、fixture或数值完成声明。  
实际后继结果编号：R480；当前尚无实际213 run/job。

## 1. 入口目标与真实父

本请求从真正actual98重生一个独立的完整39查询八批轨迹。原parent是run43677587785、artifact14147700690、source918fdb11dbb7a424b6149b405e2c7fab3cc0c737；原完整artifact、warm和status的字节/SHA全部沿原206合同核验。

它不续接actual191、200、206已退休的末场，不从这些旧场的SHA恢复状态，不复用其J、方向或FD。R455所记actual206只说明原8组执行与必要摘要超限的事实：24条trial的原数值未完整返回，新请求不能回填它们。

原206直接基线是公开source e8e4be9f5cd3885399453b8945ea750b1a365ce4。正式R455已在e66b788589c62815a9587125727dff06f87b0e16发表：15167字节、25442c584d43012a49cc8fe0cda155a5c43f0d61a0670cc7da1dbc6633f33636。新表示的条件与保全范围见[R479](../results/R479-complete39-fixed-semantic-context-readback.md)。

## 2. 公共运行件与实际生成件

公开源仍是普通小文本，每件小于100000字节。只有以下两个完整source view在本次Actions原computations目录中产生；它们不另作为Git文件发布。

| 文件 | 字节 | SHA256 |
| --- | ---: | --- |
| root_20261116_thirty_nine_necessary_contexts.py | 20813 | 689517df7b70b839112f9ba9ab7daf8d6144decd72c89215a22c35ab9c5f8b7c |
| root_20261116_thirty_nine_context_source_views.py | 8157 | b9887b2549772546380f55e1d85209f00dc373d8f03bca767d7df759003c12fd |
| request213-necessary-context-source-plan.json | 5652 | 5cd405f3a8ef58bc27019fadd8036d7f293a76fbea1ddd31e095ed652637cf85 |
| public-thirty-nine-context-model-recipe.json | 40583 | f2176b25a75166d99101c8b41672100a22562fc669e7919669da5a553351473f |
| public-thirty-nine-context-batch-request.json | 22988 | bb4005b4d7e314f0c3de466e10ffb7b7c43a32140750fea3970992af0ff26729 |
| visible-larger-public-thirty-nine-context-batches.yml | 19127 | c0543ec810a1982b8c1fe3a5fb19195b7de6285b64426aac5b71a24889967767 |
| R479-complete39-fixed-semantic-context-readback.md | 16363 | 31a25a19695f76e40c3b015ecd8755caeb96ed6b74fab6768404c370f86788fe |

两份生成件是：

| 实际Actions生成件 | 字节 | SHA256 |
| --- | ---: | --- |
| root_20261116_thirty_nine_context_chain_readout.py | 75610 | 3160c22d42abb1103ba1f1d3d71b172fbfe6d09cd938ecb7fac1bc5032ae11b5 |
| geometry_20261116_thirty_nine_context_batches.py | 29658 | 3c2cdcd9cfa0d756413afb9b5b67edb81a81db3d1f69f4836f08be3c0e401ba3 |

formatter和生成器是新增正常源码。source plan只是明确旧字面、替换次数、原源/完整生成源身份，不是科学payload或大JSON编码。plan有两个views：helper15项字面替换、worker12项字面替换。

根目录为真正GITHUB_WORKSPACE。上述新代码的实际HERE仍是：

```text
GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations
```

原公开依赖库不移动、不部分复制。新helper只新增对本次formatter的标准Python import；新worker沿原代码以明确新helper路径和SHA加载。formatter和生成器都仅依赖Python标准库。

这不把声明的source身份数量冒充经执行验证的全部transitive import闭包。actual210曾因私有目录缺少实际延迟依赖而在runtime前失败；本入口没有私有库迁移，普通原依赖继续从原公开目录解析。尚未发生的213启动结果仍必须按其真实日志报告。

## 3. 原 source/input 闭包与数量

actual206的recipe有107个source pin，独立worker构成第108个。213逐值保留这108个公开来源，不删除或替换任一旧source。

新增关系为：

- 新formatter：1个公开源码；
- 新标准库source-view生成器：1个公开源码；
- 新helper view：1个实际生成源码，进入新recipe；
- 新worker view：1个实际生成源码，由外层request绑定。

因此新recipe有111个source pin；外层独立worker使实际显式身份数为112。其中110个是公开source，2个是本次确定生成source。这个112不是新的科学维数，也不是transitive import完备性结论。

原parameter_sha256字典保持完全相同，仍仅原source-dependencies.json：7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941。source plan有独立外层身份，不冒原数学参数文件。

workflow还保留对actual191与actual200来源子合同的原逐项比较。新增actual206比较确认：

- 原107 recipe pins逐值相同，旧独立worker SHA也保留；
- 原model_flags、parameter_sha256、parent_artifact、parent_warm、parent_status逐值相同；
- 原39 query_specs、actual_query_endpoint_nodes、gap_condensation、source_entry、mathematical_producer、domain_operator、FD_entry、zero_B_layout_nodes、complete_B_local_coordinates逐值相同。

新recipe和request中的actual206_provenance完整列原run、job、source、两份overflow身份及旧source身份；不是把旧计算输入接到本次warm链。

## 4. 真正source生成顺序

生成CLI为：

```text
python -u root_20261116_thirty_nine_context_source_views.py
  --request public-thirty-nine-context-batch-request.json
```

workflow先按完整request SHA核本次合同，再按request.generator的真实字节/SHA核实际生成器。生成器以真实GITHUB_WORKSPACE/computations为唯一代码目录，随后核plan完整bytes/SHA、原206两个完整base source、每个字面替换实际出现次数、最终输出完整bytes/SHA。

两个目标basename必须是新文件，不能覆盖原source。每件生成源小于100000字节。落盘后核完整字节；两件均成功后才记录all_generated_sources_complete=true。

来源回执位于：

```text
RUNNER_TEMP/visible-source-views-thirty-nine-213/result.json
```

它是源形成/错误元数据，不含科学数组。小帧为BEGIN/END_REQUEST213_SOURCE_VIEWS_METADATA。生成器只返回真实已完成文件范围，不把第一个文件成功当两件都成功。

回执保持真实computations、GITHUB_WORKSPACE、run/attempt/source、request与plan身份、完整生成源身份、逐替换次数。科学进程尚未启动。回执过90KB仍真实70，不拆出错误树；未读源诊断保留。

### 生成失败的边界

生成器的一些最前置来源检查发生在临时result.json可形成之前。此时真实Python错误留在原step日志，不能声称已有完整来源回执。workflow明确记录实际source_views outcome；当该step不是success，always必要读回不尝试调用不存在或未完整生成的helper，而给出scientific_process_started=false、transport70、回执存在性/身份的真实范围。

source-generation成功后还可能遇到原source/schema/规则绑定错误；它同样不被改写为科学拒绝。原科学步只有前置正常完成才会启动。

这条生成失败分支不读取或重算科学数据，不新增科学验收门。它是实际代码入口和诊断的正常完整性处理。

## 5. 当前schema、文件名和帧

| 角色 | 实际声明 |
| --- | --- |
| 外层request | thirty_nine-real-pair-context-continuation-request-v1；request=213 |
| model/source recipe | actual98-thirty-nine-model-and-FD-context-recipe-v1；request=213 |
| 生成器 | request213-original206-explicit-necessary-source-views-v1 |
| source plan | request213-original206-necessary-context-source-plan-v1 |
| 实际worker | thirty_nine-real-pair-context-batches-v1 |
| 实际helper | actual98-thirty-nine-context-necessary-source-and-scalar-support-v1 |
| formatter | R479-complete39-fixed-semantic-context-composition-v1 |
| 最终单份必要文档 | request213-one-necessary-whole-chain-contexts-v1 |

当前request文件是public-thirty-nine-context-batch-request.json，当前recipe是public-thirty-nine-context-model-recipe.json。原owner验证函数现在真实读取这份request以及新worker/helper完整SHA，不沿用旧206当前文件名。

科学完成后的单份primary帧：

```text
BEGIN_REQUEST213_WHOLE_CHAIN_NECESSARY_SUMMARY
END_REQUEST213_WHOLE_CHAIN_NECESSARY_SUMMARY
```

always恢复仍是独立必要读回动作，帧：

```text
BEGIN_REQUEST213_WHOLE_CHAIN_RECOVERY_NECESSARY_SUMMARY
END_REQUEST213_WHOLE_CHAIN_RECOVERY_NECESSARY_SUMMARY
```

它不是分包。每一次完整whole-chain文档都独立受90000字节界；不能把primary和recovery互相拼成被截断的大对象。该workflow只有原单compute job，不另制造report job。

## 6. formatter的实际调用与表示

旧206的summarize、domain_record、fd_record、all-contracts-false收集、QP选中字段、错误字符串收集正文都保留。新helper在原assemble_chain已经形成全部必要字段后，实际调用necessary_contexts.compose(report)。

formatter只对这个已选对象作七类固定操作：

1. 同一batch/trial的四个candidate子记录只有完整已选行序列canonical相等时才被complete_RMS引用；引用保原完整角色表行位置。
2. 原interval左右端点/midpoint站点只有全部实际出现字值都相等且确实重复时才共享。冲突或缺失列保原行内值。
3. 原RMS站点只按该实际evaluation的原RMS check fraction与interval分享原返回字值，不由mesh或fraction形成新站点。
4. 仅在恰有一份实际typed-query定义且原kind/interval/fraction逐字相同时，失败行分享这三个原地址字段。原station和beta统计仍逐行保留。
5. 只有固定SHARED_METADATA白名单、而且全部实际行canonical相等的元数据，才成为该表共享表头。
6. 只合并原表中相邻相同上下文；后现同上下文另起新块，展开顺序保留原整表行序。
7. 真实连续batch且前批eligible，当前完整input_pair与前批完整produced_pair逐字相等时，才显式引用这份真实pair回执。

每一种候选表示仅在其完整JSON较原表示更小时采用。两种形式都保留同一必要语义。最终还加入实际formatter来源、旧已选文档bytes/SHA、每种变换的实际使用范围；因此仍不承诺最终总字节更少或小于90000。

所有原错误、FD contraction失败、试步数值、失败样本和未返后缀都保留。科学值a/ap/app、beta、曲率、残差、实际merit、alpha、FD误差、权重等没有成为通用数值字典。不存在科学树分段、数组编码或“只保哈希即可恢复”的路径。

原206摘要正文没有返回，本次也没有以另一个run的摘要替它作尺寸fixture。213真实容量只能由自身原读回确定。

## 7. 科学调用与budget逐项保持

实际worker调用仍为：

```text
python -u geometry_20261116_thirty_nine_context_batches.py
  --repo-root GITHUB_WORKSPACE
  --request computations/public-thirty-nine-context-batch-request.json
```

它仍由原root_20261114_current576_rules_runner.py启动，原规则进程2700秒周期真pull/rebase/diff-stop合同不改。独立namespace前缀为visible-thirty-nine-213-；规则目录为visible-thirty-nine-213-rules。

原预算和方法：

| 项目 | 当前实际值/范围 |
| --- | --- |
| 最大model/FD pairs | 8；不保证全部完成 |
| chain budget | 10500秒；恢复输入和公开source后开始的原批间钟 |
| 单原model | 1次原iteration；1200秒 |
| condensed | 600秒 |
| trial/recovery reserve | 90/30秒 |
| 原线搜索上限 | 17档 |
| damping | 270 |
| LSMR/projection/dual sweeps | 原200/200/200 |
| 最大working rows | 原512 |
| 角数/J workers | 原4096/2 |
| 线程环境 | 原BLAS/OMP/MKL/NumExpr均1 |
| 科学step | 原175分钟，覆盖恢复和FD调用 |
| 整job | 原195分钟 |
| always必要读回step | 原10分钟 |
| Python/NumPy/SciPy | 原3.12.14/2.3.5/1.17.0 |

原8批过程中，下一批仍只能消费本job上一原model真实产出的pair，并在原freshFD完整返回且原implementation_check_passed、prepared SHA、complete_current_warm_boundary_FD_actually_recomputed条件满足后使用。

原complete39、LEFT/MID/RIGHT typed查询、全部4096角真实评价、原RMS完整检查、完整外变量响应、原merit、原17档、原QP/矩阵/恢复方法、原FD所有方向/步长/Richardson/阈值不变。新formatter不得新增拒绝候选的数学条件。

这里仍是原有限affine尾response上的优化warm链，native_or_full_DN_requested=false；不能从8批完成或所有FD通过宣称新的非零native完整解。

## 8. 读回与静止生命周期

实际模型/FD child继续继承原rules child的独占session。新helper在恢复和科学前记录自身PID、PGID、SID、start ticks、boot ID、source/run/request/worker/helper身份，不记录token环境或完整敏感环境。

原每个child登记、同组等待、按精确活进程锚点quiesce、未知所有权partial70、PID复用防护、SIGTERM15秒与SIGKILL5秒合同不变。僵尸不视为live writer；未登记的独立脱离child不被冒称已覆盖。

新source生成目录采用不同前缀visible-source-views-thirty-nine-213，不会被原必要读回扫描误当成科学namespace。原actual computation目录中的两份source view是代码，不是科学raw；它们留在该临时checkout到runner销毁。

原科学生命周期仍是：

- 原model与新warm FD按原门完成；
- 完整必要batch记录先在RUNNER_TEMP耐久保存；
- 真pair按原字节移动保留；
- 退休该批大科学raw；
- 最后形成一个whole-chain必要文档；
- 文档完整返回后才允许原成功路径删除剩余科学namespace。

若primary formatter或publish失败，原大raw可能已按先前规则退休，但完整必要batch记录和仍存pair必须保留给always。不能因为只剩局部必要记录就声称原大JSON已回传；必须分别记录每种实际身份和未读范围。

always先实际证明own group静止，再读保存记录和真实partial carrier。最后workflow另作一次不发信号的静止检查。只有source generation、necessary readback、rules readback真实success，且新静止证明成立，才删除对应visible-thirty-nine-213-* payload。

任何summary>90000、未知或仍活跃owner、原错误未完整读、读回超时或异常，都保原partial和cleanup skipped语义。green cleanup step也可能是明确skip，未来实际报告必须读原事件。

## 9. 原输入与真实支持

本次仍restore四个原数学文件及actual98真实父：

- accepted：b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff；
- prepared：0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714；
- tail anchor：e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51；
- tail config：01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5；
- actual98 warm：4927052字节、b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67；
- actual98 status：3379453字节、b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff。

原39 query由22 LEFT、16 MID、1 RIGHT构成。RIGHT-RMS459 fraction为原0.8273268353539885；真实endpoint节点为459、460和462至491。实际central维数10928减原109 core得B local维数10819；cover33节点11266的原仿射前缀QR真的消去free461，完整H恢复仍保该变量。

此处只是列出既有固定合同，没有本地执行矩阵、QR、域检查或FD。新workflow仍在公开Actions做原普通源码语法及输入绑定；未新增fixture或独立科学audit。

## 10. 完整diff与临时审阅副本

同目录以下均是暂存审阅材料，不是科学data，也不需公开为新结果数组：

- helper-relative-to-206.complete.diff；
- worker-relative-to-206.complete.diff；
- recipe-relative-to-206.complete.diff；
- request-relative-to-206.complete.diff；
- workflow-relative-to-206.complete.diff；
- R479-global-row-order-final.delta.diff；
- generated-review-only目录中的两份完整生成源；
- publication-files.json中的最终字节、SHA、公共路径、原baseline和生成身份。

三核心公开件formatter/proof/generator已在a9ff7bec201ff5653758b4bfd6da4456291e939f正式发表，字节仍为根审读的689517df/31a25a19/b988。后继若只改接口中的出版commit，不更改任何运行source。完整entry身份以本接口表和publication manifest为准。

## 11. 实际结果责任

未来R480必须分别说明：

- 原输入和新source生成是否完整、真正使用的recipe/request/run/source；
- 实际原model/FD数量与每批所有已返回trial、失败地址、FD原错误/门；
- 未启动与已启动未返回的范围；
- 实际新warm参数和末pair身份；不能仅从hash恢复场；
- formatter哪些固定操作确实生效、原已选文档与最终必要文档实际bytes/SHA；
- single90KB是否完整返回；超限仍按真实70；
- rules停止、budget、process退出、科学拒绝、传输失败分别记；
- 最后实际quiescence与cleanup removed或skip原事件。

本接口不预填这些事实。206、207、208或其他run的统计不能替代213。当前代码交付只支付来源、可执行入口与必要字段语义；数值是否完成和是否通过原门，仍仅由未来公开Actions真实输出决定。
