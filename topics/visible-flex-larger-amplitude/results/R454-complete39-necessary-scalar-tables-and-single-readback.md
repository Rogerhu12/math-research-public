# R454 — 完整39八批必要标量的固定语义表与单份读回

作者：ChatGPT（AI，exact_refinement）；2026-11-16。  
范围：R432所定位的必要读回表示修复，独立source/recipe/worker；不改变原科学、域、FD、接受条件或资源预算。未在本地执行、导入、AST解析、编译、fixture或数值测试。

## 454.1 实际缺口与本修订的范围

[R432](R432-actual200-eight-complete39-pairs-and-single-summary-overflow.md)已经记录actual200的真实结局：八次原模型和八次新warm FD完成，原事件足以结合固定源码确认八次实际父交接；但一份必要摘要148,732字节，always恢复稿149,082字节，均超过90,000界而返回70。两份正文没有输出。不能从它们的SHA恢复末参数或全部20条原trial，也不能把另一run的输出补到actual200。

R454沿原必要选择器完整读取源码，处理的是已经选出的少量必要量在多批、多trial之间重复写字段名、身份口径和相同方向计划的问题。本修订没有声称知道148KB各字段的实际占比，也没有用合成科学结果拟合一个目标尺寸。新run的实际错误文本、失败行数和返回范围仍可能使摘要超限；90KB与70保持。

新的单文档把有明确科学含义的原标量放进有完整地址的表：

- model/status及QP实际选择；
- 所有实际trial原标量和三种原linear/directional子报告；
- base、candidate、complete RMS三类真实求值的域标量；
- 全部原RMS返回失败样本、中点失败、选中query失败和物理argmax；
- FD顶层原误差/阈值/判定、两组原判定、全部原失败contraction；
- 原观察器异常、真实输入/输出身份、实际末三参数、未返回地址及清理范围。

这是对[R428](R428-complete39-necessary-chain-readout-and-original-science-contract.md)必要集合的固定语义布局；完整field、H/J/B/C向量或矩阵、全部FD逐层数字历史、QP迭代数组仍只在原Actions临时文件中，保原文件身份。没有递归JSON树codec、字典压缩科学数据、stdout分段、数组编码或额外发布的数据档案。

## 454.2 明确的原源码与新身份

本修订的唯一实际基线是actual200发布commit `cb597d3c3d66f9787a712ffa7ca9dc3d52bd57de`：

| 原角色 | 字节数 | SHA256 |
|---|---:|---|
| necessary helper `root_20261115_thirty_nine_necessary_chain_readout.py` | 62,855 | `abf42d92c980566e20a4c8a7fbd90976669240bf8cc8bed06d3b6e1705fa79b8` |
| worker `geometry_20261115_thirty_nine_necessary_batches.py` | 29,611 | `68d53286565c892cdcebd131fb73c2c32b25d6ff865a6da706bec03dbfdbe8e5` |
| recipe `public-thirty-nine-necessary-model-recipe.json` | 31,236 | `2b9c71c067dfb8a7ff9fcd7111e4eff884a68e197504c38e14b128b6ecb8692f` |

新独立文件：

| 角色 | 文件 | 字节数 | SHA256 |
|---|---|---:|---|
| 必要reader/原恢复helper | `root_20261116_thirty_nine_tabular_chain_readout.py` | 75482 | `9840e9ae7c1219b9b3bbef45d4bacb7110f639e980f76a6d592eb9f96c9bb68f` |
| 八批orchestrator | `geometry_20261116_thirty_nine_tabular_batches.py` | 29658 | `59276c9eae96071211d8990a1b260faf0cc534e7efea3c4e9fd49a59213d7643` |
| 原科学recipe及新reader绑定 | `public-thirty-nine-tabular-model-recipe.json` | 34102 | `2353548631ab0b7a6a67e25b2f1360c4b78066448df6b85cd0bff56e2b7868ab` |

新recipe逐项保留原105-entry recipe映射，另保原200 worker的实际SHA，故106个既有来源都保留；再添新helper为107个recipe来源。独立新worker在request显式绑定，总108件。旧source没有覆盖，新helper不会被旧200实例误用。

实际数学producer仍是原39四源和[R407的非连续支持实现](../computations/root_20261115_noncontiguous_local_qp_condensation.py)。新reader没有模型或角场求值入口；新worker只派生当前request/source/namespace标识，原模型、FD命令和控制流不变。

## 454.3 原必要选择范围不缩减

本修订保留原helper以下选择函数的实质正文：

- `primitive_fields`：选择原必要标量，并保留完整已返回错误字符串；
- `necessary_point`：物理地址、原值和原冻结权重的必要字段；
- `necessary_QP`：实际选择、完整原模型证据、原slack、预算、失败、原QP文件身份；
- `domain_record`：完整域必要标量、原RMS失败样本、原中点失败与所有实际观察器错误；
- `fd_record`：原顶层误差/阈值/原判定，两组原判定、方向/层数及所有 `contracts is False` 的原记录；
- `summarize`：完整实际trial列表、未返回索引、真实文件、参数、原schema和原status/model对应关系。

尤其保留R428最终修订的三项责任：

1. 失败的second-order contraction按原group、direction index/name、record index定位，保原coarse/fine step、observed ratio、applies和contracts，不重算门。
2. `angular_observer_exception`、`observer_export_exception`遍历**所有已返回midpoint point**，不限于bad index列表；完整错误字符串保留，traceback只保完整原身份。
3. `collocation_weight_observer_error`保原observer_exception、diagnostic/unchanged booleans和traceback/entry身份，透传到最终单文档。

原RMS producer每fraction最多保存first24失败样本，这是原producer边界。新reader把这些已返回行全部保留，不再加任何截断，也不把未采样的其余失败点冒成已读。所有原域/merit/FD门都先执行；reader不决定一个科学候选是否接受。

## 454.4 固定语义表和原地址

`NecessaryScalarTables`只接受调用点明确给出的必要标量对象，不遍历任意原科学树。每张表分为：

- `address_columns`：实际记录定位；
- `value_columns`：明确原字段名，一次列出；
- `rows`：地址随后接这些字段的原值。

`batch_record`是单文档 `batches` 中的记录序号；每个batch对象仍保真实 `batch_index`、namespace或恢复carrier地址，因此中断读回时不会把 `batch_index=None` 的残留parent混成一个成功模型。trial仍用原 `original_trial_index`。值列缺项为null，与原200同列必要表的缺项语义一致；它不表示数值0或科学通过。

主要表的责任如下。

| 表/集合 | 定位和内容 |
|---|---|
| `model_scalar_results` | batch记录；原merit-before、damping、accepted |
| `original_status` | batch记录；原phase/progress/warm identity/退出相关错误 |
| `all_original_trials` | batch记录+原trial索引；全部原已选primitive，包括α、预测/实际merit、ratio、accepted/reason及返回范围 |
| 三种linear/directional表 | 同trial地址；原selected linear beta、reserve slack、independent directional check全部原已选值 |
| `domain_returns` | batch记录+base/candidate/complete_RMS+trial；原域标量和实际报告presence |
| `original_RMS_checks` | 同域地址+原check索引；每个原RMS check已选标量 |
| `original_RMS_returned_failure_samples` | 再加原返回sample索引；interval/s/left/right/beta/phi/a/ap/app/曲率原值 |
| `original_midpoint_failure_records` | 同域地址+原返回failure序号；完整原必要地址与beta报告 |
| `all_original_failed_selected_queries` | batch+trial+原failure序号；query/kind/interval/fraction/station和完整原失败角必要值 |
| `original_physical_argmax`等三表 | 同域地址；原物理argmax、component、frozen weight |
| `FD_original_report` | batch记录；原全部已选顶层误差、阈值、判定和输入/source SHA |
| `FD_original_groups` | batch记录+direct/separated；原两组判定与方向记录数 |
| `FD_all_original_failed_contractions` | batch+group+direction索引/name+原contraction索引；完整原失败标量 |
| `QP_...`各表 | batch记录；原比较/选择、final actual evidence/slack、local report/last stage |
| `status_standalone_model_field_relation` | batch+原model字段；原present/equal布尔，非新科学门 |

失败地址的整数连续区间仅用于原bad-midpoint或已评价selected-query索引集合；没有把科学向量变成区间编码。原观察器错误保存在 `all_actual_original_observer_errors`，有batch、求值角色、trial、原字段路径及完整已选原错误对象。错误不随正常点是否进入失败集合而丢失。

所有节点、query和角分量仍由原producer产生。表的形成只有JSON字段选择、位置索引、字节身份及字符串操作，不调用RHS/J/FD，不替数据作正负、可行性、范数、merit或接受判断。

### 原写入者的类型合同

本次只对实际200固定source作文本核对，没有运行一个科学样本。`necessary_point.original_vector_value`的名称不表示整向量：39 observer 的 `_physical_row`实际赋值为 `scalar(state["vector"][row])`，其中 `scalar`先执行 `float(value)`，再返回有限浮点或null。该函数其余已选地址和值也由int/同一scalar形成；右边界分支的行号仍是int。`component`和冻结权重的必要子对象分别进入两张有名表；未选择的 `original_array_components`没有进入标量表。

QP的比较与选择字段沿原写入点核定：原39 warm的两个目标值由 `float`形成，`final_actual_full_A_AT_B_BT_readback`明确为True，耗时是原单个elapsed值；原完整方向选择的 `selection`是两条字符串分支，`segment_parameter`、下降量和方向导数是原浮点，两个责任字段是bool。原local QP的 `final_selection`也是两条字符串分支，stage/count/budget为整数，停止原因为字符串，分段参数/一阶值/曲率为浮点；实际working-row列表只取原已选条数。最后完整证据经过原 `primitive_fields`，唯一另选的 `all_original_linear_slack`对象单独成表。可选优化失败保原错误对象及traceback身份，不塞入标量表。

失败FD contraction的原写入函数 `refined_directional_check`只产生五个字段：`coarse_step`、`fine_step`取原默认三步浮点，`observed_error_ratio`为原浮点或null，`contraction_test_applies`、`contracts`为bool。它不含逐层数组或嵌套报告。组、方向名和两个原索引是读回地址，原记录五值全部保留。原 `primitive_fields`的其他选择本来限定标量及明确 `original_nonfinite_JSON_token`表示；没有用一个更窄formatter偷偷丢掉此前已选嵌套科学字段。

对应的固定实际producer来源如下；全部仍是新recipe保留的原科学来源。

| 实际写入者 | SHA256 |
|---|---|
| `geometry_20261115_thirty_nine_query_collocation_observer_warm.py` | `59fa547d08f01f43b9000f8f58bb2c3eb03cc06a3a6f92dbeeedf728b08b19ea` |
| `geometry_20261115_thirty_nine_query_condensed_warm.py` | `568d1f22ef9de4fe31d1a9e570ed66b3b91fb51525fc5dd5eb27f99c4901d3a9` |
| `geometry_20261114_full_angle_projection_warm.py` | `7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152` |
| `geometry_20261114_condensed_local_inequality_qp.py` | `ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173` |
| `geometry_20261114_full_dn_response.py` | `38d21971b3b0d462f8cf1b8f0a1cd174a28db3dcba450e89d0d0baecc5e26e74` |

## 454.5 只在明确相等时共用的四类必要信息

本修订不假定不同求值相同，也不按近似数值合并行。需要共用的少量明确元数据使用 `same_necessary_json`，比较两份选定对象的原 `canonical` ASCII JSON字节（含一LF）。因此不同类型的整数/浮点文字及 `-0.0`/`0.0`不会因Python普通数值相等而被合并；这仍是解析后必要JSON的比较，不声称恢复原文件JSON排版。

**第一类：同一trial的candidate与complete RMS必要记录。** 只有两份完整选定域记录的canonical字节相同，complete_RMS角色才写 `same_original_necessary_record_as_candidate=true`，引用同trial的candidate记录。两次实际求值的返回角色仍分别存在。若有任一原选定字段不同，完整新角色的值和失败地址分别写出。不从这个相等性推出两次求值未发生，也不省任何原RMS求值。

**第二类：FD方向/层数计划。** 每组第一次真实返回的 `direction_columns` 与 `direction_rows` 保存一次。它只包括方向名和原centered/Richardson/contraction记录数，不包括FD值或误差历史。后续同组计划只有canonical完全相同时注明相同；不同或部分计划完整输出。每个batch的真实FD顶层误差、原门、原全部失败contraction、完整方向历史原身份仍独立保留。没有复用上一warm的FD成功或数值。

**第三类：最后参数的重复副本。** 最后链状态的真实pair对象与某个实际batch的produced pair、必要参数记录都canonical完全相同时，链状态只注明对应batch记录。真实三参数、完整scalar-profile和native-height身份仍在该batch对象内。没有单凭hash相同构造参数，也不把未返回参数设成上一组参数；不一致就保两份。

**第四类：固定身份口径句。** 两句已有canonical identity说明只在总文档中表述一次；每个对象原 `canonical_bytes` 与 `canonical_sha256`仍独立保留，未知不同口径也不删。原文件bytes/SHA与解析JSON canonical身份继续明确分开。

以上共用分支都只影响表示；比较false不会拒绝科学候选，不增加solver/FD/域门。

## 454.6 不变的原科学和生命周期

独立206仍从actual98的真实原artifact恢复两份原父文件；actual200仅是修读回的证据，不是可取回的新warm。原39集合、真实459/460及462至491支持、自由461的完整仿射QR、所有外变量、全H/B/C、全部112边界责任保留。

原科学参数仍为每model最多1接受、damping270、LSMR200、projection200、17档、1200秒；condensed600秒、trial reserve90秒、recovery reserve30秒、max-working512、dual-sweeps200。每个原新warm后全原FD，原5e−5阈值与Richardson/收缩门均不变。八批上限与10,500秒批间钟、175分钟science、195分钟job和10分钟必要读回不变。

`run_batch`、`validate_completed_pair`、真实pair搬移与SHA核对、各原模型/FD命令和eligible判断保留；新worker只改独立来源/schema/namespace/recipe绑定和必要输出说明。原model的 `success=false`、`new_coupled_finite_acceptance=false`以及原affine-zero-J范围不能改称native/full-DN接受。

原3b8 rules runner不变。独立206仍先记录实际PID/PGID/SID/start_ticks/boot_id，再运行继承该session的原子子进程。Always读回先对已确认当前自有group作实际静止处理；不识别的进程不发信号、不读删可能正在写的payload。清理仍要求必要读回和规则读回success，并再作fresh non-signalling quiescence核对。

每批必要对象仍先durable保存，才搬移真实两文件、退休已消费batch大数据。整链输出成功后才主动删除namespace；错误或超限仍保残留到always读回/runner销毁。没有新raw artifact、Release或Git数据发布。程序不承诺未来仍有可下载原末pair。

## 454.7 单份限制、partial与科学独立

新helper仍只有一份whole-chain必要JSON。它先形成完整内容和真实bytes/SHA，再检查90,000。超过界限时：

- `summary_complete=false`；
- `transport_exit_code=70`；
- 不打印BEGIN/正文，不切片、不打包重构、不截断；
- 保原science结果独立，不能把transport70改成数学拒绝；
- 原未读必要记录和仍存raw按原生命周期保留。

未知错误、未返回FD、缺失报告、部分batch或未证明进程静止也分别按原地址和原因读回；缺失不能改为成功、未启动或数学失败。原 `not_recorded_original_trial_indices`、未表示batch和可由原终态明确的未启动后缀继续保留。

本修订没有用实际200丢失的正文验证压缩后的字节数。源级能证明的是：明列的必要量全部仍有地址和值，重复字段名和已证相同元数据不再展开；不能无条件证明任何未来科学失败文本都小于90KB。正常Actions的原源码语法检查仍在原流程中，不另造fixture、科学验收或审计门。

## 454.8 可执行后继

R454给出独立206的reader/worker/recipe来源。完整request/workflow沿原200仅替换真实新source/schema和必要格式绑定，保所有旧数学pin与原预算；最终差异、全文文件和manifest由主控读后单独发布，作者不移动Git ref或派发科学。

Actual206以后必须使用自己的run/source/输入/原事件作结论。它既不能填补R432未输出的20条数值，也不能续接actual200已消失的末场。其科学责任仍是原八组新完整模型及每组真实新warm FD；必要读回是把已发生的事实完整、有限地交付，不是额外科学前门。
