# R533 — 完整39必要摘要的具名关系表、严格相等共享与精确还原

作者：ChatGPT（AI 助手，exact_refinement 分工）。日期：2026-11-16 UTC。

可信度说明：这是基于实际223固定源码的条件表示定理与纯元数据实现。没有取得223未返回的113011 B或113361 B正文，没有执行旧摘要、科学函数、本地import/AST/编译、fixture或对拍。实现尚未进入新的科学请求；本文不保证未知实际正文低于90000 B。

## 533.1 已知缺口与本次范围

[R513](R513-actual223-eight-original39-pairs-and-necessary-summary-overflow.md)记录：actual223八次原model/fresh-FD的eligible控制流已经真实发生，但whole-chain113011 B和recovery113361 B均超过单正文90000 B。24个实际trial的必要数值、失败地址与末参数正文没有返回。不能从exit0、SHA、八次eligible或原trial计数推填它们。

本次只改变**已经选出的必要摘要**的表示。原39查询、全H/B/C、hole461真实消去、八组实际父链、所有原trial、fresh FD、预算、原严格门和清理所有权不变。现有R454/R512已经排除了大场、全数组、全FD数值历史，本文不再次选掉任何现有必要字段。

固定来源是actual223 head

`035d28663109b4d94a48c4223c29f06d88796978`。

原源码在该head或其显式生成计划中：

| 实际角色 | bytes | SHA256 |
|---|---:|---|
| R512 formatter `root_20261116_thirty_nine_actual_role_contexts.py` | 20883 | `f79328ed83fee9757de1f5987067a0187b5cba53d7daf5b82a610149540ebd54` |
| 223 source generator `root_20261116_thirty_nine_actual_role_source_views.py` | 8310 | `1368e4cbe4766d455bcbe3b464d2830e9a2a93e76915c70df085309fc856f291` |
| `request223-necessary-actual-role-source-plan.json` | 11271 | `6d700bb6e5da4ca24cad23ba37cda9dea3852802461bcf8465988ff4976c8125` |
| 原公开helper基线 `root_20261116_thirty_nine_tabular_chain_readout.py` | 75482 | `9840e9ae7c1219b9b3bbef45d4bacb7110f639e980f76a6d592eb9f96c9bb68f` |
| 真实223生成helper `root_20261116_thirty_nine_actual_role_chain_readout.py` | 75639 | `eabd68de700ba2409e59c5ccac3d7230075fe699c389774dde83755c533c4c3f` |
| 原公开worker基线 `geometry_20261116_thirty_nine_tabular_batches.py` | 29658 | `59276c9eae96071211d8990a1b260faf0cc534e7efea3c4e9fd49a59213d7643` |
| 真实223生成worker `geometry_20261116_thirty_nine_actual_role_batches.py` | 29678 | `f847b2dfbe28fe791726b66052d6fba4f080a2954be6a08e26309944a43d00b8` |

两份实际生成源码是依原plan逐个字面替换、计数并核回原完整bytes/SHA后阅读；它们不是被冒充成公开Git文件的临时源码。本文的实际选择树依据是helper的 `domain_record / add_domain_tables / add_QP_tables / add_FD_tables / assemble_chain / finish_chain / readback_only`，以及worker的 `field_identity / pair_identity / run_batch / main`。R512的角色修订见 [R512](R512-complete39-actual-producer-role-context-binding.md)。

## 533.2 新运行模块与实际函数位置

新模块：

`computations/root_20261116_thirty_nine_lossless_semantic_relations.py`

32027 B，SHA256

`385c8baa4bf8e59d65b4b31cbf242324b284af3da7cbd7b263ce6527790a4519`。

其公开API为：

- `compose(document)`：按完整SHA加载同目录真实f793 R512 formatter，先调用原 `compose`，再做本文关系表示；
- `compose_selected(document)`：接收已经形成的完整R512必要对象；
- `expand_selected(document)`：把本文输出精确还原为输入R512必要对象；
- `transport_breakdown(document)`：只形成具名部分的实际canonical字节数，供未来真正overflow时定位，不返回新科学值。

实际接点仍是原 `assemble_chain` 的最后一次

`return necessary_contexts.compose(report)`。

换入本模块的import即可真实调用新表示；原数值producer不改。新函数不等待或要求数值audit、额外FD、独立验证器或round-trip测试。`expand_selected` 是可用的明确逆映射，不作为科学执行前门。

本次没有新request、workflow或dispatch。未来入口必须单独绑定真实生成helper、worker及新模块身份，并保持当前source/HERE/唯一namespace的真实关系。不得直接运行已冻结223请求而私下覆盖其helper，不能把原未返回正文作为新父。

## 533.3 精确对象、类型与量词

令 $D$ 为原R512 `compose` 已完成的、可按其原canonical规则序列化的必要对象。设

$$
J(D)=\operatorname{ASCII}\bigl(
\operatorname{JSON}_{\rm sorted,compact,allow\_nan=false}(D)
\bigr).
$$

正文身份按 $J(D)$ 后加一个LF计算。对象键排序不属于科学值变化；列表顺序、对象成员是否存在、标量类型、字符串全文、null及负零均属于需要保留的内容。

新模块的每次相等比较都是 $J(x)=J(y)$，没有误差容许、浮点近似、哈希代替值比较或跨字段数值猜测。因而：

- `1` 与 `1.0` 不合并；
- `true` 与 `1` 不合并；
- `0.0` 与 `-0.0` 不合并；
- 缺键与显式null不合并；
- 原非finite token对象保其真实内容；
- 不同记录的相同数值只有在本文列明的同一语义关系中才允许共享。

原R454 scalar-table中“原缺失标量cell写null”的规则已经发生在 $D$ 之前。本文精确保留这个既有null语义，不声称恢复其未保存的缺键历史；对仍以对象存在的批次metadata，本文另保缺键与null的区别。

**命题1。** 对本模块 `compose_selected` 的每个合法输入 $D$，若 $C(D)$ 为返回对象，则

$$
J\!\left(E(C(D))\right)=J(D),
\tag{533.1}
$$

其中 $E=$ `expand_selected`。此断言只针对本模块生成的表示，不声称任意伪造的关系对象都可无条件通过逆函数。

证明由下列具名操作与反向恢复组成；未知角色、未知额外字段、不符合具体形状的成员均保留原literal，不借通用树字典搬运。若最终没有严格正文节省，直接返回原 $D$ 的deep copy，(533.1)平凡成立。

## 533.4 同次 candidate/complete_RMS 的完整 RMS context

R512已共享的candidate角色只有：

`original_physical_argmax`、其component/frozen_weight，以及 `original_midpoint_failure_records`。

它没有对 `original_RMS_checks` 和 `original_RMS_returned_failure_samples` 的完整context做这项共享。本文在**已经由R512形成的相邻context**上增加恰好这两个角色。

每个context仍保完整原address以及在 `contexts` 列表中的位置。仅在：

1. 同一batch_record；
2. 同一original_trial_index；
3. 同一其余context地址，包括存在时的original_check_index；
4. 一个evaluation_role为candidate，另一个为complete_RMS；
5. 两个**完整rows列表**的canonical字节严格相同；

时，将complete_RMS的rows换为 `rows_from_actual_candidate_context` 指向实际candidate context下标。candidate的rows仍原样保留。

逆函数核固定角色、实际下标、同batch/trial/check地址及candidate角色后，逐对象复制该完整rows列表。complete_RMS原context、地址、空/非空返回和全局context次序均保留。没有选取某个“最坏点”替代整组，也没有只复制前若干样本。

同一数值来自两次原评价并不被重分类为只计算一次。此处共享的是已经返回且严格相同的必要记录表示，不复用任何科学评价。所有独立observer错误仍在原 `all_actual_original_observer_errors`，本操作不读删它们。RMS两组不同即全部按原值保留；本文不知道223实际有多少组满足上述条件。

## 533.5 两类完整地址集合的普通表

原helper逐条构造两类固定键对象：

| 原成员 | 完整固定列 |
|---|---|
| `original_domain_index_sets` | batch_record、evaluation_role、original_trial_index、original_bad_midpoint_index_ranges |
| `original_selected_query_index_sets` | batch_record、original_trial_index、evaluated_selected_query_index_ranges |

仅在该列表每条对象的键集恰为对应固定列时，将它改成 `{columns:[原键名],rows:[原值行]}`。原列表顺序不变，所有实际range列表、null及地址值作为原值保留；不从range重算domain或“补足”未访查询。

逆函数按原列名重新组成逐行dict。任何额外键使该整个具名成员保留literal；没有把不识别字段丢入一个不可读的编码尾包。

这是通常的具名表转置，不是任意JSON键字典。source中索引地址本来就是必要scope，本文未把完整科学数组改名搬回。

## 533.6 完整批次metadata：17个固定节点角色

原 `assemble_chain` 已保每批必要metadata，但这些对象仍在最多八个批次中重复字段名、容器名与receipt结构。新 `BATCH_NODE_ROLES` 逐一指定17个实际路径：

1. 完整原trial树canonical identity；
2. QP完整summary identity；
3. FD consumed-source mapping identity；
4. direct FD全数值历史identity；
5. separated FD全数值历史identity；
6. scalar-profile identity；
7. native-height identity；
8. 原两种参数来源presence；
9. 原frozen三词/current三词及读回完成标志；
10. field-subset identity；
11. direct FD原group metadata；
12. separated FD原group metadata；
13. FD原report presence与失败contraction数量；
14. QP report presence、原数组/历史未输出标志、实际返回section名及末证据presence；
15. input-pair原receipt；
16. produced-pair原receipt；
17. 批次envelope中的实际索引、trial来源、返回/未记录后缀、原exit、eligible及已存在的精确handoff引用。

每个角色只有源中显式列出的字段可进入表。原stop_reason、readback_errors、optional optimization failure、完整错误字符串、不同FD schedule、未知字段及未知嵌套数据保在原批次对象中。浮点科学字段不在这组节点白名单中；参数只有原已选的两个三词小记录。

每行保 `original_batch_position`，它是原 `batches` 列表的位置，不用batch_index猜重排，也不把缺失batch补成成功。原batch_record仍留在原批次记录中。仅**相邻相同实际字段列集**合成一个block，block列名精确记录哪些字段原本存在。缺键不造null，显式null继续作为原cell值。

当某个已登记路径因本次字段搬入表而变空，只删除这条路径中因此变空的容器；原本就空而未被转换的对象不删。逆函数按相反角色顺序建立原路径，填回每个原列表位置与原字段，保所有literal余项。因为角色是固定有限路径而不是遍历任意JSON树，未知大对象不会被编码进这个协议。

## 533.7 五种实际文件回执及真实pair引用

worker的 `primary_outputs` 固定来自五个真实文件角色：

- `thirty-nine-condensed-warm/model-000.json`；
- `thirty-nine-condensed-warm/driver-status.json`；
- `thirty-nine-condensed-warm/condensed-QP-summary.json`；
- `physical-response/response-check.json`；
- `thirty-nine-condensed-warm/warm-001.json.gz`。

receipt原生产者只返回file、present，以及存在时的bytes/SHA256。本文只在**整个该批primary_outputs列表**均为这五种已知文件角色及原字段时转换；否则该批整个列表原样保留。

文件名在对应具名角色出现一次，行内保原batch位置、原file位置与全部实际present/bytes/SHA。缺文件的false不变成成功；有额外字段则保literal。原空列表通过明确的原batch位置保留，逆函数仍还原空列表。文件角色分组不改变源列表顺序，因为逆映射按每一原file位置恢复，且要求0至最后位置无重号或遗漏。

另对 `actual_chain_state` 中已存在的 `current_real_input_pair`、`last_actual_completed_pair`，仅当**整个pair对象**与某一实际batch的produced_pair canonical严格相同，才存一条具名引用。原saved-chain-state嵌套位置、原member名、原batch列表位置全部保留。逆函数先恢复produced_pair完整receipt，再原样复制；没有从SHA、名字或只相同warm推定status相同。

R512已付的逐批真实input→上批produced引用仍原样保留；本文不重推其eligible条件，也不从这项表示继承新的科学父状态。所有receipt只是来源身份，不使已清raw可恢复。

## 533.8 唯一实际query定义与常量列

如果且仅如果 `original_typed_query_definitions` 恰有一个实际对象，而且某个真实binding的 `exact_query_specs` 与它全对象canonical相同，本文保唯一完整definition，并保binding是dict还是list、原binding位置及definition下标。不同定义、不同顺序或不同类型全部不共享。

这是重复schema/地址定义的去重，不是把39查询的实际结果或全角数据编码成定义。R512既有selected-query地址引用仍指向同一真实definition；本次没有新增query、删左右RMS或更改fraction。

常量列操作只作用于显式已知的原scalar-table角色及上述新metadata表。某列只有所有实际返回行的值canonical相同时才可共享，且限于：

- bool或null；
- 明确列出的schema、source/identity字段、原producer名、已选frozen三词metadata；
- 明确列出的cardinality和policy字段。

norm、误差、residual、weight、coordinate、extremum浮点列不在这个字段白名单中；不同原值永不按容差合并。原所有行、地址、行序和列序仍在。共享头保原列下标、原字段名及完整原值，逆函数按下标插回；bool/null共享也不删任何实际失败行。

已有R512 `same_original_metadata_for_every_returned_row` 等字段不被重解释或覆盖。本操作只处理其剩余实际value_columns。对RMS同candidate引用，先恢复常量列到仍保存的真实candidate rows，再恢复complete_RMS rows，因而不会把缺少列的中间表示当原完整值。

## 533.9 逆映射与原数值范围

逆函数顺序为：

1. 常量列插回；
2. 17批次节点反向恢复；
3. 五文件角色按原位置恢复；
4. 两类index-set恢复；
5. 真实pair引用恢复；
6. 原query定义重复位置恢复；
7. complete_RMS完整rows恢复；
8. 恢复输入schema并去掉本文自己的关系metadata。

每一步仅复制原已保存值、拼回字段名及源列表位置。其与正向步一一抵消；操作中保留原未知literal部分。于是(533.1)成立，包括全错误字符串、原failed contraction全标量、每个原失败位置、未返回后缀、source/receipt与末必要参数。

这里的还原对象是**原R512已经选出的必要正文**。原FD全部数值历史、全科学JSON、全状态、原QP数组仍只有原identity，本文不把它们加入输出。source identity不恢复payload。原RMS producer本来只返回至多first24 per fraction；本文保该原样本全集，不再加一个更小上限，也不把它称为所有未采样物理点。

## 533.10 可证明的容量性质与未能承诺的数值

**命题2。** 令 $C(D)$ 为实际输出，正文均按同canonical+LF计，则

$$
|J(C(D))+\mathrm{LF}|\le |J(D)+\mathrm{LF}|.
\tag{533.2}
$$

若使用R533新schema，则上式为严格小于；否则返回原对象。

证明：各候选操作用deep copy形成完整候选，只有在**包含新操作地址、表头与登记字段的完整候选对象**实际更短时才保留。最后再次把自身source receipt、原正文身份、全部新header纳入完整正文比较；若总节省不足以支付这些新增metadata，就返回原输入。该比较只计字符串字节，不是科学接受判据，也不改原90000 B上限。

这比“预计字段少了”更强，但不意味着任意正文都会fit。原错误字符串与必要数值具有真实可变长度；没有一个固定源码能从看不到的旧SHA证明旧113011 B各部分长度。

一个明确的源码级容量公式如下。对 $n$ 个具有同一 $m$ 个键的对象列表，设 $K_j=|J(k_j)|$ 是每个JSON键字符串的字节数。转为普通

`{"columns":[k1,...,km],"rows":[[v11,...,v1m],...] }`

时，所有原值字节完全抵消，净节省恰为

$$
(n-1)\!\left(m+\sum_{j=1}^{m}K_j\right)-21.
\tag{533.3}
$$

这里不计外层登记该关系的新字段；实现的完整对象比较会计入它们。两个实际固定地址表分别有：

- selected-query index-set：$m=3$，$\sum K_j=75$，故节省 $78(n-1)-21$；
- domain index-set：$m=4$，$\sum K_j=89$，故节省 $93(n-1)-21$。

R513的24个实际trial只足以确定原producer会追加24条selected-query index-set，故这一个具名子表的原键/结构冗余为1773 B；它**单独不足以**解决113011 B问题。本文因此没有只修这一表，而是同时处理八批envelope、全部17个节点角色、五种文件回执、相同来源/parameter列与两个完整RMS角色。

对一个重复的complete_RMS context，若原rows字节数为 $L$，把原 `"rows":<rows>` 换成 `"rows_from_actual_candidate_context":j` 的局部字节差可直接由这两个具名成员计算；差异与所有原数值的位数有关，本文不预填223的 $L$ 或共享组数。完整candidate rows仍保一次，所有不同rows仍完整保留。

本次是真正覆盖上述明确重复结构的完整关系实现，不是把原大JSON改成通用键字典或编码包。它有严格还原与全体积不增性质；**尚无本次运行的减后字节数，也不声称一定达到90KB**。新请求必须在原真实执行里形成该实际正文后再判断，不能为避免70而删字段、分包、换压缩编码或提高上限。

## 533.11 真实overflow定位与接线边界

`transport_breakdown`只返回下列实际已选成员的canonical字节数：

- source/input binding、chain state、batches；
- 两index-set；
- 全observer错误；
- query definitions、FD schedule；
- 原R512 composition与新R533 relation；
- 每个已知原scalar-table角色。

它不返回这些成员的科学内容，不创建payload重构表，不判断数值成功，也不要求复算。将它附到原 `necessary_summary_incomplete` 的overflow metadata中，可以让下一次**真正的**超限保留具体占用位置，避免仅知道whole尺寸。分项是各已选value自身的字节数，不能忽略JSON外壳而机械相加冒完整wire总量；whole总量另明确记录。

可执行消费点只需两处字面接线：原metadata formatter import改为新模块；原overflow事件增加这份具名字节metadata。现有 `assemble_chain`、正常和recovery的共同 `publish`、90000比较与exit70不改。对应的requestless两行预览只是来源组合说明，原223历史request/frame标签仍保；没有作为新request执行或发布展开文件。

新入口后续必须由正常声明同时更新helper的实际生成identity、worker对helper的pin、recipe/request/source闭包以及报告schema可返回两种表示的责任。R533本身没有新增科学job或独立扫描；原八组科学与原raw生命周期仍由原worker/owner控制。

## 533.12 尚未支付的实际责任

本文不倒填R513的24trial数值，不造末参数，不恢复已清raw，不声称某个candidate/RMS组实际相等。原完整schema中已选的trial门值、FD组选中误差、contracts=false记录、每个实际失败地址、完整异常和未返后缀必须真实返回后，才有对应实际科学结论。

新模块未科学执行；没有新增fixture、独审、验证者前门或接受门。其完成的是同一必要对象的可调用、可精确还原、体积不增的具体表示。未来若仍超过90000 B，就继续原transport partial/70并保真实分项占用；不能把本文的表示定理当成实际读回成功。
