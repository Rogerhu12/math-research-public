# Request206 — 原39八组科学与单份固定语义必要表接口

作者：ChatGPT（AI，exact_refinement）；2026-11-16。  
状态：独立完整源/recipe/request/workflow文本；未本地导入、AST解析、编译、科学计算或fixture。主控唯一Git发布和Actions派发。本接口不预填未来run/job/source或科学结果。

## 1. 实际起因和此次执行对象

Actual200来源 `cb597d3c3d66f9787a712ffa7ca9dc3d52bd57de`、run `43780457519`、compute `133016222219` 的必要结论已刊为[R432](../results/R432-actual200-eight-complete39-pairs-and-single-summary-overflow.md)，发布commit `af8d11654013b0bf488f9c4ccc083cf82893a5b3`。R432正文15,908字节/SHA256 `7a3d905f5e980edfd1c83a9413ba2ba437e58c68454acd1dc618dd5bbfeed1b2`。

Actual200的八次原模型和八次新warm FD都返回0，八次原父交接为真；必要记录的trial计数为4、4、3、3、2、2、1、1。单份主摘要148,732字节、always摘要149,082字节，均在90,000界处明确70。其正文和末参数未输出，不能恢复或补值。具体科学层次、文件生命周期和真正cleanup skipped在R432，206不修改其结论。

206从**actual98原artifact的真实原warm/status**恢复，重新执行原39-query八批协议。它不是actual200末点续接，也不重放actual171的37→38前缀。Actual200仅作为必要读回修订的来源和证据。

此次新source只改变已经选出的必要标量的表达：字段名按明确角色只写一次，原值仍在完整地址的表行中；完整错误、失败地址、FD选中误差、末参数和未返回范围保留。原科学的所有门、方法、参数和预算不变。[R454](../results/R454-complete39-necessary-scalar-tables-and-single-readback.md)给出完整来源和选择语义。

## 2. 七件发布映射和冻结身份

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| helper | `root_20261116_thirty_nine_tabular_chain_readout.py` | 75482 | `9840e9ae7c1219b9b3bbef45d4bacb7110f639e980f76a6d592eb9f96c9bb68f` |
| worker | `geometry_20261116_thirty_nine_tabular_batches.py` | 29658 | `59276c9eae96071211d8990a1b260faf0cc534e7efea3c4e9fd49a59213d7643` |
| recipe | `public-thirty-nine-tabular-model-recipe.json` | 34102 | `2353548631ab0b7a6a67e25b2f1360c4b78066448df6b85cd0bff56e2b7868ab` |
| request | `public-thirty-nine-tabular-batch-request.json` | 17310 | `056fc24b4eae26bf36dbc37f67b9c75ca79cdacc99617cbeb101e0990fae79ca` |
| workflow | `visible-larger-public-thirty-nine-tabular-batches.yml` | 14363 | `9a3b52bc27ea1b50af1997dbc9ad451f705b10802aec7a059275e8438668ad0e` |
| proof | `R454-complete39-necessary-scalar-tables-and-single-readback.md` | 16863 | `1693b163d0658a7d395a78ce95c09af874eec4303def479d8e0c84c51df94598` |

本接口是第七件，最终身份在publication manifest中，不在正文自引用自己的SHA。helper、worker、recipe、request发布到 `topics/visible-flex-larger-amplitude/computations/`；workflow到 `.github/workflows/`；R454到topic的 `results/`；本接口到topic的 `notes/`。

`publication-manifest.json`、完整baseline diffs、source evidence缓存只是本地可重得的文字核对材料，不要求入Git。没有数据artifact、fixture或大表需要发布。

真实基线是actual200的五运行件，原SHA分别为helper `abf42d92...`、worker `68d53286...`、recipe `2b9c71c0...`、request `30508867...`、workflow `0de9e717...`。完整64位值、原路径、基线commit与每件diff的bytes/SHA在manifest；不是与未运行草稿比较。

## 3. 闭包和原参数的保留

新recipe有107个显式source pins：

1. 原200 recipe的105个名字/SHA逐项保留，包括actual191的104件及原200 helper；
2. 明确加入原200 worker `geometry_20261115_thirty_nine_necessary_batches.py` 的 `68d53286565c892cdcebd131fb73c2c32b25d6ff865a6da706bec03dbfdbe8e5`，把原200完整106来源作为历史身份保留；
3. 加入本次独立新helper。新orchestrator另在request pin，因此本次总108件。

原参数manifest `source-dependencies.json` 的完整SHA `7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941`不变。workflow保原source hash与正常AST语法步骤，新增的只是当前107/108身份数量及原200字典的逐项保留核对，不执行合成数学fixture。

原39四数学源保持：

| 角色 | 文件 | SHA256 |
|---|---|---|
| 全39域/响应 | `geometry_20261115_thirty_nine_query_domain_operator.py` | `0dc60f8a43da0eed700e9e70235759b42890c038121c1f5a973fc6a417bf038d` |
| 原condensed warm | `geometry_20261115_thirty_nine_query_condensed_warm.py` | `568d1f22ef9de4fe31d1a9e570ed66b3b91fb51525fc5dd5eb27f99c4901d3a9` |
| 原实际warm FD | `geometry_20261115_thirty_nine_query_condensed_response.py` | `fc92e7d900b0ccc24f6d6a162443112122f0e724c1e6b235914d23c593b4754c` |
| 原collocation observer | `geometry_20261115_thirty_nine_query_collocation_observer_warm.py` | `59fa547d08f01f43b9000f8f58bb2c3eb03cc06a3a6f92dbeeedf728b08b19ea` |

非连续支持适配仍为R407已刊 `b7a5f7e6d699a2ed9c9d4068c3f831d633b76a1df457630ca536fd5207186ce4`，原8479完整仿射消元源不改。

全部38旧查询及新增RIGHT-RMS459 fraction `0.8273268353539885`保持，完整端点集合459、460、462至491，32端点、26capture intervals、79,872个已选角约束。自由461仍在原完整H里；cover33前沿11,266维先完整QR消去461的338物理量，然后才得到真实前沿10,928维/local10,819维。不得用零B461代替自由变量。原C支持4,059维、所有外变量与全控制响应保留。

## 4. 真实恢复和同job接续

起始artifact原run `43677587785`、artifact ID `14147700690`，来源commit `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`。原809,042,943字节ZIP/SHA和两个成员原字节身份沿200保持。暖场与status原SHA为 `b59f40c0...`、`b7ad389f...`，完整值在新recipe。

四数学输入仍从同固定历史Git对象恢复原bytes并核SHA；当前science checkout不切ref，不把新参数、旧FD或虚构native结果写进原输入。原public source restoration和source-dependencies保持。若原artifact或输入实际不可取，程序按真实错误partial，不由哈希制造原件。

各batch仍：

1. 从真实当前pair运行一次原完整模型；
2. 原model已产生单个progress warm且真实warm/status identity核对通过，才运行该warm的全原FD；
3. 只有原FD的实际 `implementation_check_passed`、实际prepared SHA和 `complete_current_warm_boundary_FD_actually_recomputed`均满足原合同，才允许下一批；
4. 必要字段先durable存于本namespace，之后原两文件不重序列化地搬移并核bytes/SHA，再退休已消费大batch；
5. 原next pair与下一model输入一一对应，旧方向/weights/J/FD不会冒下一批fresh结果。

这还是原unaccepted progress方法。原native当前H、完整full-DN和新coupled finite acceptance没有被请求；source flags保持原false，不能因读回完整或batch eligible改名。

## 5. 不变的资源和原接受门

| 项 | 206仍用原值 |
|---|---|
| 最大model/FD pairs | 8 |
| 批间clock预算 | 10,500秒，仍从原输入/public source恢复之后起 |
| 每原model | iterations1、1200秒 |
| 原damping/LSMR/projection | 270 /200 /200 |
| 原回溯档数 | 17 |
| Condensed factor/optimization | 600秒 |
| 原trial/recovery reserve | 90秒/30秒 |
| 原max working / dual sweeps | 512/200 |
| FD角网格 | 4096 |
| 原模型jac_workers / BLAS | 2 /1 |
| science步骤 | 175分钟，覆盖恢复和逐批FD |
| 整job | 195分钟 |
| always必要读回 | 10分钟 |
| 单份必要JSON | 90,000字节，含末LF |
| 超限传输退出 | 70 |

原完整域、RMS、rho、merit、实际下降/预测ratio及FD全部原判定不改。原 `64*eps*max(1,base_merit)` floor由原producer计算，reader不重新算一个数作为门。原5e−5 FD阈值、所有centered/Richardson层及原contraction规则保持。不同model有不同固定weights，reader不跨model相减merit。

预算不保证未来八批均完成。未开始、原数学拒绝、原时间停止、规则停止、源/进程/读回失败分别保留，不归为一种数学结论。

## 6. 新必要摘要的稳定字段合同

新helper schema：

`actual98-thirty-nine-tabular-necessary-source-and-scalar-support-v1`。

新worker schema：

`thirty_nine-real-pair-tabular-batches-v1`。

新request schema：

`thirty_nine-real-pair-tabular-continuation-request-v1`，`request=206`。

新全链必要输出schema：

`request206-one-necessary-whole-chain-tables-v1`。

顶层保：

- `source_and_actual_input_binding`：原完整来源/输入共同身份一次；
- `actual_chain_state`：实际停止、batch覆盖、真实末pair、原elapsed及清理范围；
- `batches`：每个实际记录的batch_index、真实pair/文件身份、退出和eligible、完整原trial索引与未返回后缀、原参数；
- `necessary_scalar_tables`：固定语义角色表；
- `original_domain_index_sets`、`original_selected_query_index_sets`：原索引元数据；
- `all_actual_original_observer_errors`：所有实际异常的原路径/完整字符串；
- `original_FD_first_actual_direction_schedules`：原方向名/层数计划，不是数值历史；
- `readback_errors`、`summary_complete`及全部原scope false flags。

各表都有 `address_columns`、`value_columns`和 `rows`。读取一行时前面是明确地址，后面逐列对应原字段名；没有“字典码”或藏在编码里的科学大树。

`batch_record`指 `batches` 中实际记录序号；`batch_index`、namespace、partial carrier仍直接保在对应batch。跨恢复路径可能出现非完整模型记录，不能把序号当科学batch完成证明。原trial地址不重排或补全；未返回索引只是未返回，不默认已试或未试。

### 6.1 Trial和域

`all_original_trials`表保每条返回trial全部原已选primitive；三种原linear/directional子报告各有语义表。每个trial另有实际candidate、complete_RMS两角色，base有独立角色。

`domain_returns`保完整原DOMAIN_COLUMNS、报告presence、RMS检查存在性、midpoint返回计数等。每个RMS check、每个原first-invalid sample、中点失败及选中query失败分别按真实序号带全地址和原值。失败样本数量不再截断；原producer first24的本来限制明确声明。

原中点观察器错误遍历所有实际返回points，不依赖bad集合。权重观察器和其他原observer error完整字符串保留；大traceback仅原完整身份。所有这些诊断仍不改变原模型判断。

原物理argmax的地址/值、component及frozen row weight分三张语义表，原数值不重算，未定义不替成有限子集最大值。

### 6.2 FD和QP

FD原顶层误差、阈值、门值和各输入SHA在 `FD_original_report`；两组各自原布尔与记录数在 `FD_original_groups`。所有 `contracts is False` 原记录在 `FD_all_original_failed_contractions`，保group、direction index/name、contraction index和原全部标量。

第一次实际direction/层数计划存一次；以后只在其必要canonical JSON字节完全相同时写“same”，不同计划完整保。每个batch原完整方向numeric history身份仍保，所需top误差仍是该batch原值。没有复用旧FD。

QP comparison、两种selection、final actual full model evidence/linear slack、local report及last saved stage各有固定表。原优化失败对象完整保，原大QP数组/迭代历史只身份，不从QP报告重造z或原科学输入。

### 6.3 精确共享的边界

允许共用的内容只有明确的重复必要信息：

1. 候选与complete_RMS的完整选定域记录canonical相等；
2. FD同组方向名/层数计划canonical相等；
3. 最后实际pair和必要参数对象与某batch记录共同canonical相等；
4. 两句固定canonical identity口径说明一次。

所有比较都基于原选定对象的完整canonical ASCII字节，保正负零和整数/浮点表示差异；不以容差或只看hash替代值比较。共享false不会拒绝候选，仅保各自实际记录。原文件bytes/SHA与解析后canonical JSON身份明确分开。

## 7. 原单文档传输与异常分责

新reader完整形成必要文档后，仍调用原 `publish`。它先报整个JSON的真实bytes/SHA，90,000以内才打印一个BEGIN/正文/END帧。主帧为：

`BEGIN_REQUEST206_WHOLE_CHAIN_NECESSARY_SUMMARY`  
`END_REQUEST206_WHOLE_CHAIN_NECESSARY_SUMMARY`。

Always恢复帧为：

`BEGIN_REQUEST206_WHOLE_CHAIN_RECOVERY_NECESSARY_SUMMARY`  
`END_REQUEST206_WHOLE_CHAIN_RECOVERY_NECESSARY_SUMMARY`。

两者是同job执行/恢复的必要路径，不把一个大摘要拆成多个小摘要。正常主读回成功并完成namespace清理时，always不会伪造另一个科学结果。

超限仍70、`summary_complete=false`；不输出正文、不拆包、不压缩科学数组、不把bytes/SHA写成已读全文。原stderr≤64,000字节时完整必要文本保留；更大文本沿200如实未读/70，不借编码绕界。该错误上界是传输边界，不是科学接受规则。

原200正文已不可取，本次没有对其做“压缩后通过”的本地演示或fixture。完整必要数据天然可能超过90KB；新格式减少确定的重复表达，不能无条件保证任何未来错误/失败范围都能装下。

## 8. 进程所有权、quiet和清理

206独立namespace为 `visible-thirty-nine-206-*`，规则目录 `visible-thirty-nine-206-rules`。原3b8 runner的 `start_new_session=True`不改；新worker在任何恢复或科学child之前记录当前run/attempt/source/request/helper、PID/PGID/SID/start_ticks/boot_id。不输出token或环境。

原model/FD子进程仍 `start_new_session=False`，真实pid/group/start-time被记录。Always必要读回先确认当前自有group，只对原记录匹配的活跃组作原TERM15秒/KILL5秒的受控处理；不明group或PID复用绝不发送信号。

静止未证时，返回70，不读可变科学文件，不删payload。Cleanup只在必要和规则读回都成功后执行，并重新作一次non-signalling quiet核对；否则输出真实skip理由并保残留到runner销毁。文件与目录兼容枚举保持原200，owner前缀文件不会被误当batch目录。

主worker仍先保存每批必要记录、再搬pair/退休batch；整链完整读回后才删namespace。原Git历史对象缓存不由wrapper伪称已擦除，没有raw上传或持久数据恢复服务。

## 9. Workflow和权限

独立workflow只由新request路径push触发，`cancel-in-progress=false`，不会取消旧run。保原pinned checkout/setup-python、ubuntu24.04、Python3.12.14、numpy2.3.5/scipy1.17.0和BLAS1。

workflow沿200逐步执行：源/recipe/原参数身份与正常语法、固定历史输入恢复、原rules runner包装的八组、always必要读回、规则结果、条件cleanup。没有新科学步骤、fixture或预审核门。

权限仍 `contents:write` 和 `actions:read`：前者服务原规则同步合同，后者服务真实artifact/metadata恢复；当前科学checkout不由新reader修改。根README `21bd547f56590b7f2dd279d0297efb289a9b2783`和topicREADME `bff8aea253a9e6a7a4fac28d810ac454c5499fec`沿200已读pin保留，若主控后来实读规则变化须显式更新request，不伪装运行期live ack。

## 10. 未来实际结论的最小读法

未来唯一必要读者应先核实际run/source/job、必要帧完整性/bytes/SHA、原退出与quiet/cleanup。然后逐batch按表地址读全部实际trial、原失败query/中点/RMS地址、原FD误差/收缩失败和真实末参数，保未返回后缀。

即使所有八组eligible，仍是原unaccepted progress warm；不得声称native/full-DN/finalJ/audit或闭曲面完成。不同batch的固定weights不共用，不能由merit差编造整个链的统一目标下降量。

如果传输未完整，未来结论应像R432一样分清：实际子进程/父交接证据、已输出必要量、没有输出的数值范围。不能由本接口或source希望填actual值，也不能再取已销毁科学数据的SHA冒恢复。

## 11. 源码检查和提交边界

本地只完成源码与已发布基线的逐文本差异、JSON元数据组装、字节长度/SHA和必要原写入者只读；没有导入新旧helper、没有AST/编译、没有科学或mock/fixture。正常Actions原语法步骤承担实际解析，不新增人为验收项。

完整五个运行差异与两新说明文件在独立工作目录；主控可先发表R454/core+recipe，再发表request/workflow/interface。所有七件发布后由新request触发自己的真实科学；作者不自行Git/ref/dispatch。原200、191及其他进行中科学保持冻结。

206实际结论编号预留R455；本接口和R454不预付R455的任何数字或完成标志。
