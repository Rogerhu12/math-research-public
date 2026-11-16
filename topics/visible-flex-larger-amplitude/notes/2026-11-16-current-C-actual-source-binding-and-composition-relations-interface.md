# R544：当前 C 实际来源接线与完整 composition 关系接口

作者：OpenAI / ChatGPT exact_refinement agent（AI）  
日期：2026-11-16  
状态：独立源码/条件实现；R545 / request230 将承接真实 outer caller。本文不是实际 R546 结果。

## 1. 范围和实际祖先

本接口对应 [R544 完整结论](../results/R544-current-C-actual-source-bindings-and-lossless-composition-relations.md)，沿实际217冻结来源构成，不修改已运行217、222或其源文件。首轮 launcher 的真实 `--tail-client` argv 改到未改 driver 所要求的当前 client；独立 closed 入口的 `ENTRY` 改到真实新文件名。guard、原数值函数、原科学判断保持。

实际祖先是 request217 的 head `4a08bebb63482c34c3bb7460582772a966e25c51`：

| 原件 | bytes | SHA-256 |
| --- | ---: | --- |
| `notes/current-C-same-semantic-head-refinement217-request.json` | 26106 | `dbb6c4c6b4e8fecb955c40fa90c271733dccddef70c3bda9104829bd86a6a75c` |
| `.github/workflows/visible-current-C-same-semantic-head-refinement217.yml` | 86586 | `e361dfc2b7b932a6ec9ddbf923612c95af329ad23c2181252a9f3f8fdaf6c2a7` |
| `notes/request217-complete-same-C-source-plan.json` | 80964 | `68c284041ccb330e4d61f66161a0799643b9fd83c90016ddcdde3d9649a4b4de` |

前两条 notes 路径在本 topic 内，workflow 在仓库根。原217完整结论见 [R490](../results/R490-actual217-complete-shallow-sampling-and-source-binding-stops.md)。原222的首 client 与闭面来源错误另由实际 R511 记录；本次不重复取它的日志。

必须区别：原93236 B composition文件identity、未返回的 necessary 正文、本文未来选中正文，是三种不同责任。这里没有重新取得原科学大数据，也没有用SHA恢复未返回正文。

## 2. 本次发表文件和准确身份

| topic内路径 | bytes | SHA-256 |
| --- | ---: | --- |
| `computations/root_20261116_complete_source_composition_relations.py` | 8567 | `7bc351fe46ce6c8bf94ba067b106a0a21bd89950277910fe46006c502815b163` |
| `computations/root_20261116_current_C_bound_source_views.py` | 16140 | `78ac0c9624beaa1ea2dd660f761b8c49ef56c49794d3928233625d86faff5104` |
| `notes/r544-current-C-actual-binding-source-plan.json` | 76039 | `10002d1bacbf88792750884537ae16b0c1993049be8bb2306502339032a98a2b` |

另发表 R544 正文和本接口；两者完整身份在交付 manifest。计划中每一个 baseline/output 都有完整 bytes/SHA，95项字面定义和每个实际出现次数。没有把49个展开源或完整diff加入Git。

原字面引擎保持 `root_20261116_current_C_zero_linear_source_views.py`，11895 B / `4d4c507edd571b67655fd2e66fb4bcfa173b1239928443831a81a925c4869ec4`。新wrapper真实调用该模块的 `main(argv)`，并保其原 source-only、完整字面计数、文件不覆盖及实际 HERE 合同。其旧 R496 名字代表算法来源，不代表当前 job 是旧运行。

所有单件均小于100000 B。49个当前源码展开后共1972880 B，仅现场使用；原8个历史 same-C 视图亦仅现场形成。该展开是普通源代码生成，不是科学 raw 的编码或分包。

## 3. 真实 source-only 生成 CLI

后继必须先完成原首六层源码展开，并把原217完整计划按实际文件名复制到真实 computations。源文件身份核仍依据其公开 notes 原件。调用为：

```bash
python "$VISIBLE_COMPUTATIONS/root_20261116_current_C_bound_source_views.py" \
  --computations "$VISIBLE_COMPUTATIONS" \
  --plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/r544-current-C-actual-binding-source-plan.json" \
  --plan-sha256 10002d1bacbf88792750884537ae16b0c1993049be8bb2306502339032a98a2b \
  --out "$VISIBLE_BASE/source-views-current-binding230"
```

`VISIBLE_COMPUTATIONS` 必须是该程序的真实 `HERE`，并且位于实际 `GITHUB_WORKSPACE` 下。若继承222的临时 metadata/source 工作视图，所有这几个变量必须真实指向该视图，不能用旧 checkout 的同名文件冒充。

`VISIBLE_BASE` 必须是 `$RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205`。`--out` 是原 namespace 的新鲜直接子目录，不能已存在，也不能把输出源写入该 receipt 目录后假称 HERE。生成源码始终写到真实 computations 内独立新basename。

源码计划 format schema 为 `R496-current-C-zero-linear-three-level-source-view-plan-v1`，logical schema 为 `R544-current-C-actual-owner-and-orchestrator-source-binding-repairs-v1`。前者使未改字面引擎接受原格式，后者明确本次真实用途。完整计划中 `generator` 是新wrapper；`frozen_literal_engine` 是被调用旧引擎，两者并列且不冒同源。

## 4. 精确准备顺序和输出

准备顺序为：

1. 核实际公开Actions身份、原仓库、当前run/source、真实HERE、完整当前计划和原clock。
2. 核冻结217计划的完整身份、八个角色和全部中间/最终 output。
3. 要求原8个历史名字及49个当前名字均未存在；不覆盖任何已有源。
4. 从各已存在的真实baseline逐项应用原217字面替换，核每个中间与最终 bytes/SHA，形成八个历史祖先文本。
5. 保留原Actions内的源码语法处理，随后独占写入八个真实历史文件。
6. 在同一HERE加载未改的R496元数据生成器，使用当前计划实际形成49个新来源。source-only列表仅包含真实 Python/JavaScript来源；JSON policy/plan只作为数据原件，不加入该列表。
7. 核该引擎的实际来源、run/source、每个输出的真实路径/完整身份和完整49项覆盖，再记录原clock字节未变。

实际wrapper输出 `--out/result.json`，schema为 `R544-complete-current-C-binding-source-generation-v1`。其中：

| 字段 | 实际含义 |
| --- | --- |
| `source / plan / historical_source_plan` | 新wrapper、完整当前计划、冻结217计划的真实文件身份 |
| `actual_computations` | 真实当前源码目录 |
| `actual_original_clock` | 原job-science-deadline文件的完整身份 |
| `historical_stages` | 每个历史角色的真实baseline和全部中间stage/output |
| `outputs` | 已确认实际文件；成功时历史8加当前49，共57项 |
| `historical_unwritten_roles` | 尚未真正写出的历史角色 |
| `unconfirmed_current_roles` | 尚未核成实际输出的当前角色 |
| `current_view` | 正在处理或失败的真实来源地址 |
| `current_engine_exit / current_engine_result` | 被调用原引擎的真实退出及完整结果身份 |
| `current_engine_stdout / current_engine_stderr` | 原输出文件的完整bytes/SHA |
| `error` | 真实异常类型、文字、traceback |
| `completed` | 仅完整来源准备完成；不是科学完成 |

捕获到的中断或来源错误保留实际已写集合和未确认集合。不能由计划预期数量补造输出。最初Actions/路径/计划/clock绑定若未通过，可能尚无 `result.json`；外层必须保真实exit/stderr及“source receipt未形成”，不编造完整回执。

wrapper不删除任何raw，不创建新namespace钟，不启动科学求值。它的stdout只是一条小来源结果事件；完整元数据在现场 `result.json`。原引擎结果另保于 `--out/current/result.json`，不会把同一个大科学对象拆成这些文件回传。

## 5. 49个当前角色与原消费者

完整角色/output映射在计划的 `views`；以下分组说明其作用，不替代该全身份表。

| 组 | 数量 | role |
| --- | ---: | --- |
| 首轮及首闭面 | 7 | `first_launcher, first_reader, first_policy, first_post, first_postreader, first_held, first_post_entry` |
| 同far精化 | 9 | `same_worker, same_client, same_sampler, same_driver, same_owner, same_reader, same_post, same_postreader, same_held` |
| union-M求解与记录 | 8 | `union_worker, union_client, union_sampler, union_checkpoint, union_driver, union_owner, union_phase_reader, union_reader` |
| union-M完整几何/证据/显示 | 17 | `union_saved, union_radial, union_prefix, union_shared, union_cut, union_atlas, union_caps, union_material, union_reach, union_held_consumer, union_metric, union_block, evidence, display, union_post, union_postreader, union_held` |
| 同C重新包围消费者 | 8 | `217_head, 217_leaf, 217_bridge, 217_tail, 217_metric0, 217_metric1, 217_metric2, 217_evidence` |

最后一组role保留217祖先标签以便一一追溯，输出文件实际采用 request230。它们的独立schema/frame也明确230，不把旧217源码标签冒实际caller。

两处实质改动以完整literal表达登记。其余changes只传递当前源名/完整hash、原source descriptor大小和独立schema/frame，原计算正文不因来源级联而改。具体首轮仍要求原完整112far、真实numeric representative/native/full453后真450；same-far和union-M各保原来源、全新网格责任、新增模态、全部J/FD/末门。各层geometry、reach、held、同C及time evidence保持原合法输入依赖，来源准备成功不补这些实际责任。

## 6. 具名source-addition formatter

模块 `root_20261116_complete_source_composition_relations.py` 是纯JSON元数据模块，没有独立科学CLI。后继composition caller用真实HERE中的该完整SHA加载后调用：

```python
selected = relations.compose(full_original_composition)
record = relations.canonical(selected)
parts = relations.breakdown(selected)
```

这里的 `full_original_composition` 是原producer已经完整构成且现场校验的同一个对象；不能先截字段、重算选点或删source history。原完整文件依然保留，原 `verify_runtime` 沿完整对象工作。

只有 `exact_member_changes` 中恰好四键的source新增行可变成关系：

```text
path = "/source_sha256/" + actual_ascii_basename
before_present = false
after_present = true
after = complete_lowercase_64_character_sha256
```

实际四键成员顺序也要与该组第一条原行相同。不同顺序、额外键、非bool presence、非完整SHA、JSON-pointer转义或非限定source名均完整留literal。未知信息不会因为formatter不认识而丢失或被解释成一个hash引用。

新wrapper schema为 `R544-complete-source-composition-addition-relations-v1`。其完整根成员为：

- `original_canonical_record`：原完整canonical bytes/SHA；
- `original_member_order`：原完整根键顺序；
- `record_except_member_changes`：除change列表外所有原字段和嵌套对象；
- `exact_member_change_relations`：明确总行数、固定角色列、原四键顺序、全部source三列行和全部其余literal行。

三列固定为 `original_change_index / source_basename / after_sha256`。它们的含义就是原完整source新增事实，不是任意大JSON的通用字典。

`expand` 是这一固定关系的明确逆。按原地址恢复source行，在其他地址依次填入literal队列，再按原根键顺序复位。完整行序、键存在性、值类型、负零、null与缺键都按原对象保持。科学caller不执行一项额外逆映射数值对拍作接受门。

## 7. 90K、identity及overflow

canonical格式为 UTF-8、排序对象键、紧凑分隔、不转义普通Unicode、禁止非有限JSON常数，末尾一个LF。与其他stdout frame是否另加分隔LF必须分别记清。

formatter仅在**整个候选完整canonical正文**严格小于原完整canonical正文时采用关系，否则返回原对象。名字长度为$L$、原行地址十进制位数为$d$时，合格原行长$145+L$，三列行长$72+L+d$；共享头、完整其他对象和原identity开销由最终整份比较计入。

这保证输出不比原完整正文更大，不保证小于90K。后继必须实际检查：

```text
len(record) <= 90000
```

超过时只返回真实overflow状态、实际所选whole bytes/SHA及具名breakdown，不拆包、不截断、不增限额、不给complete marker。任何尚未返回的完整正文不能由原SHA推测其内容或大小组成。

`breakdown` 的具名部分只报告原已选对象的实际canonical字节数；它不是可重组payload。对于关系格式，返回source新增数、literal数、source新增表bytes、literal表bytes及其余完整对象bytes；whole另给完整identity。部分字节数不宣称相加恰好等于包含wrapper字段名和分隔符的whole。

原完整composition文件identity与选中necessary正文identity必须在marker里分开。例如实际caller可登记 `original_complete_record` 和 `necessary_summary` 两个各自真实receipt；不得再沿旧reader假设两者是同一文件。marker必须同时绑定当前derivedrequest、run/source及实际formatter来源。

## 8. R545需要完成的实际caller闭合

本次不改旧217/222源。后继独立caller必须实际做以下接点，不能只把本模块列在request里：

- 在原六层生成后调用本wrapper，明确确认真实57项输出及其来源准备结果；历史8与当前49分列。
- actual首launcher、closed orchestrator、原native/refinement/postsolve source role map均取本计划真实新文件；所有旧source仍保祖先pin。
- 三层field消费者及same-C head/leaf/tail/metric/evidence均通过真正caller使用当前新文件和schema，原225等不同native链不混入。
- 原same-C八角色仍是 head_recompute、level0 metric/measure、level1 metric/measure、level2 metric/measure、compare；仅来源准备与注册机制调整，不重复旧科学、不把某层未起当同C失败。
- composition读回实际调用本formatter，返回一个完整选中body；readback reader及cleanup对完整原件/选中body的两个identity采用一致合同。
- 继承222真实metadata/source工作视图时，原checkout不改；derived220/derived205的完整现场字节与旧祖先身份分开。JSON policy仍属于数据pin，不送入source-only语法列表。
- 全部必要body、原9scopes、同C新增scopes和实际owner quiet都齐才允许沿原cleanup删除同namespace；任一缺marker、unknown own、未静止或运输超限均保留raw并说明skip。

以上是调用这三个新来源的具体工程合同。完整request230/工作流/阶段参数/marker source closure由R545发表；本文没有把尚未写完的outer文件假记为当前已发布源。

## 9. 原clock和科学责任

唯一clock仍从原namespace最初建立开始，科学 allowance18900秒、readback reserve2700秒；本次全部source copying/literal generation算入该绝对钟。wrapper读原clock，不重启、不延长、不用新request号重开预算。

所有原phase budgets及实际剩余clip仍由原caller负责，包括first453→450、same-far五factor、union-M、各层geometry/held、同C head1800及其原内部1650/120/30、metric240、measure300、compare120、末900关闭/读回预留。上述数值不是彼此可叠加的总时长，也不承诺单job全完成。

本次不改变准确C的定义/root-family、R503真实十词/目标、field维度及原mesh/time合同；不将旧有限或另一次run的J/native/域证明继承为新实际计算。闭面同g仍须原first A/B、material与full construction绑定，不因source名相同而自动成立。

原source checks与原science门不同：source准备失败应返回工程未开始；科学partial可以完整返回必要结论；metadata/quiet成功不代替任何数值门。合法数学输入缺失时沿原消费者标明未付，不能因测量或闭面未成反向补成BVP成功。

## 10. 本次验证和发表范围

本次只作已冻结原源的文本阅读、literal字符串应用、完整bytes/SHA形成和条件证明。未在本地导入、AST解析、编译或执行任何科学源，也未作fixture、benchmark或新独立审计。Actions里的原source语法处理仍是其原运行准备。

本接口和R544正文给出了可解释、可逆的明确表示与两条实际source修复。未来是否完成科学、是否将完整composition压入90K、是否达到原全部field/metric/held门，均须由真正request230原事件和必要结果回答。原unknown、未访问、来源错误及cleanup skip都应如实留在对应实际结论中。
