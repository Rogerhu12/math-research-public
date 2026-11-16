# R533：完整39必要语义关系表的实际调用接口

作者：ChatGPT（AI 助手，exact_refinement 分工）。日期：2026-11-16 UTC。

## 1. 状态、目标与边界

本件交付一个可直接由现有 `assemble_chain` 调用的纯metadata模块、完整精确还原证明，以及两个实际接线点。没有新科学执行、没有读取223未返回的raw、没有把旧SHA恢复成参数、没有改八组原39 model/fresh-FD或原门/预算。

实际223的known缺口是whole113011 B、recovery113361 B均超过90000 B；原八批eligible和trial计数仅说明相应控制流已发生，全部必要数字仍未返。本模块针对这份**已经选出的必要对象**的具名重复，而不是重复扫描全科学数据或重选必要字段。

request228 / R540入口 / R541实际仅为协调预留；本件不是已经发布、派发或完成的228请求。新workflow、request、source closure、运行身份和结果必须另据真实最终文件绑定，不在本件预填。

证明见 [R533](../results/R533-complete39-lossless-necessary-semantic-relations.md)。实际旧scope见 [R513](../results/R513-actual223-eight-original39-pairs-and-necessary-summary-overflow.md) 与 [R512](../results/R512-complete39-actual-producer-role-context-binding.md)。

## 2. 本件正式文件与身份

| 角色 | 路径 | bytes | SHA256 |
|---|---|---:|---|
| 新模块 | `computations/root_20261116_thirty_nine_lossless_semantic_relations.py` | 32027 | `385c8baa4bf8e59d65b4b31cbf242324b284af3da7cbd7b263ce6527790a4519` |
| 条件证明 | `results/R533-complete39-lossless-necessary-semantic-relations.md` | 19750 | `07baa615c9caf333a3acb4afd4254112146f030088da489be213f509533932cf` |

本接口自身身份由外部publication manifest记录，避免自引用。所有新正文和单源小于100KB，不发表可再生完整helper/worker展开，不在Git存科学payload或旧未返回摘要。

源的常量：

| 字段 | 实际值 |
|---|---|
| `SCHEMA` | `R533-complete39-lossless-necessary-semantic-relations-v1` |
| `RESULT_SCHEMA` | `R533-one-complete39-necessary-whole-chain-v1` |
| `RELATIONS` | `necessary_semantic_relations` |
| `PREVIOUS_FILE` | `root_20261116_thirty_nine_actual_role_contexts.py` |
| `PREVIOUS_SHA` | `f79328ed83fee9757de1f5987067a0187b5cba53d7daf5b82a610149540ebd54` |
| `PREVIOUS_RESULT_SCHEMA` | `request223-one-necessary-whole-chain-contexts-v1` |

最后一项是已刊R512 formatter的原格式标签，不授权把未来run改标成actual223。未来调用者的request number、run_id、source_commit、源身份仍必须来自真实新调用者；这些原selected字段不被R533改写。

## 3. 实际基线与读取合同

基线固定actual223 source：

`035d28663109b4d94a48c4223c29f06d88796978`。

原计划 `computations/request223-necessary-actual-role-source-plan.json` 为11271 B / `6d700bb6e5da4ca24cad23ba37cda9dea3852802461bcf8465988ff4976c8125`。它从已刊公开基线形成实际223 helper和worker；本次已按全plan字面替换计数、核回完整输出身份并读实际选择树，没有执行源码。

| 成员 | bytes | SHA256 |
|---|---:|---|
| 公开helper75482 | 75482 | `9840e9ae7c1219b9b3bbef45d4bacb7110f639e980f76a6d592eb9f96c9bb68f` |
| 真实223生成helper | 75639 | `eabd68de700ba2409e59c5ccac3d7230075fe699c389774dde83755c533c4c3f` |
| 公开worker29658 | 29658 | `59276c9eae96071211d8990a1b260faf0cc534e7efea3c4e9fd49a59213d7643` |
| 真实223生成worker | 29678 | `f847b2dfbe28fe791726b66052d6fba4f080a2954be6a08e26309944a43d00b8` |

新模块不读model、warm、QP或FD科学文件。原helper仍先做 `summarize`、`add_domain_tables`、`add_QP_tables`、`add_FD_tables`、`assemble_chain`；原已选内容完整交给新formatter。新formatter按真实同目录文件SHA加载f793原formatter，不替换旧全局，不调用另一个数值producer。

新模块无需重新复制全部旧transitive目录。未来source plan应从原公开基线+原223既有变换组成新helper，保全旧公开/历史生成来源，新增本模块的真正源码pin，然后正常级联helper→worker→recipe/request/workflow身份。不能只把旧helper的SHA表改成新SHA却仍运行旧import。

## 4. API与返回类型

### 4.1 `compose(document)`

输入是原 `assemble_chain` 最后形成、尚未经过R512的完整必要对象。

实际步骤：

1. 只加载同 `Path(__file__).resolve().parent` 中实际f793源，核完整SHA和非symlink；
2. 调用原R512 `compose(document)`；
3. 调用 `compose_selected`；
4. 返回一个完整Python必要对象。

这个源身份检查属于普通声明依赖绑定，不是新的数值门。原模型/FD及原选中科学值均已在调用之前形成。模块没有科学CLI或另起进程，没有独立audit/scanner。

### 4.2 `compose_selected(document)`

输入是原R512已经形成的完整必要对象。如果schema不匹配、已有本文保留key，或者全部真实转换计入所有表头后没有严格总字节节省，返回其deep copy，不删减任何字段。

成功采用关系表示时，返回schema为R533的对象，保真实request/run/source等所有原值，只把固定具名结构改成关系形式，并增加 `necessary_semantic_relations`。其source字段是真实R533文件字节身份；`original_selected_body`保存**完整输入canonical ASCII+LF**的bytes/SHA与scope。

因此正常调用可能返回：

- 原 `request223-one-necessary-whole-chain-contexts-v1` 格式；
- 新 `R533-one-complete39-necessary-whole-chain-v1` 格式。

未来report guard应明确接受这两种实际格式并独立核真实新request/run/source，不能为了固定新schema而强制一个更大的表示，也不能把历史format字符串当当前run来源。

### 4.3 `expand_selected(document)`

仅还原本文关系表示；对原格式返回deep copy。它精确恢复输入R512 canonical对象，包括字符串、null、负零、数字类型、缺键、字段值、列表顺序与全部必要错误/地址。

逆映射只对本模块生成的具名关系成立。对碰撞、错列宽、无效原位置等损坏表示会报ValueError。正常科学/传输路径**不执行这个逆函数作额外通过门**，没有新fixture或数值对拍。读者可按需要使用它查看完整必要对象；不能用它恢复原科学全树。

### 4.4 `transport_breakdown(document)`

输出schema `R533-necessary-semantic-section-byte-counts-v1`，保：

- 实际完整canonical正文+LF字节数；
- 明确的两列名 `actual_selected_semantic_member / canonical_value_bytes_without_LF`；
- 10种原已选根成员存在时的value字节数；
- 源中列明的全部已知scalar-table角色存在时的value字节数；
- “这些是大小，不是数值成功或payload重构”标志。

不读取raw，不复算gate，不返回该成员的科学值。各部分大小不是忽略JSON外壳后的可随意相加总量；完整正文大小另列。字段数固定，未知大字段不会被递归搬成表。

## 5. 正向转换与全部保留责任

转换顺序固定：

1. 两个完整RMS context的同candidate共享；
2. binding中的唯一真实query定义共享；
3. chain-state中的完整真实produced-pair引用；
4. 两个固定键index-set表；
5. 五种原primary file receipts；
6. 17个已列名batch节点；
7. bool/null与具名metadata常量列。

每一步在完整候选对象上计bytes，只有确实更短才保留。最后再与完整原body比较，包括所有source/表头/操作登记；没有整体严格下降就返回原body。

不允许的变化包括：截断错误字符串、减少任何原trial、只返最坏query、丢 `contracts is False` 的完整原失败记录、把missing当null而抹掉原对象presence、推填未访范围、降低FD层数、提高90KB、把一个必要大body拆成多个body或换通用编码。

### 5.1 RMS context

只处理 `original_RMS_checks` 和 `original_RMS_returned_failure_samples`。同一batch/trial/check的candidate和complete_RMS **完整rows**必须canonical严格相等。原context地址及次序原样保，complete_RMS改为指向真实candidate context。不同rows全留；observer错误完全独立，绝不因RMS相等被删。

### 5.2 原范围地址

两个index-set列表只有每条键集恰为原producer固定列时才表格化。原range、null、数值和行序全保；unknown字段导致该成员原样保留。

### 5.3 批次节点与缺键

每个新表按实际 `original_batch_position` 返回原值。相邻同列集才共享列名；列只列实际存在的原字段，显式null照常存。未知字段、stop_reason、readback_errors、不同schedule及完整失败消息留在原batch literal中。

原global/current参数仍是原producer已经返回的两组三词小记录；其精确值没有从warm/profile重算。完整profile和native-height仍只有原canonical identity，未引入大数组。

### 5.4 文件和pair

五文件角色依原固定相对文件名共享header，每行原batch/file位置完整保。present=false不改，额外字段保literal。实际input/produced pair全receipt按原对象保；chain-state只有整个对象与某真实produced pair完全相等才引用，不以单SHA猜其余字段。

### 5.5 常量列

共享仅发生于所有实际行canonical值相同且字段为bool/null或源中列明的metadata/计数字段。原norm、误差、residual、weight、坐标和极值浮点列不在metadata白名单；原数值差异全部留在原cell中。

共享头明确给出原列位置、原字段名及原值，所有原行仍在。因此将 `contracts=false` 或某presence常量上提也不减少任何失败地址或原判断，不能把一个constant header解释为重新计算的新门。

## 6. 两个实际字面接点

以下是基于真实eabd生成helper的**requestless最小预览**，只是现有实际调用点的明确说明。没有发布这个展开文件，也没有用它运行冻结223请求。

第一处，唯一import：

~~~python
# 原
import root_20261116_thirty_nine_actual_role_contexts as necessary_contexts
# 新
import root_20261116_thirty_nine_lossless_semantic_relations as necessary_contexts
~~~

原 `assemble_chain` 的最后一句保持原样：

~~~python
return necessary_contexts.compose(report)
~~~

第二处，在原 `publish` 的len(raw)>SUMMARY_LIMIT分支里，只增加具名大小metadata：

~~~python
emit("request223_necessary_summary_incomplete", dict(**receipt,
    transport_exit_code=70, reason="necessary-summary-exceeds-90000-bytes",
    semantic_section_byte_counts=necessary_contexts.transport_breakdown(value),
    full_result_not_split_or_encoded=True,
    unread_necessary_records_retained=True,
    prior_large_raw_may_have_retired_after_durable_necessary_selection=True))
~~~

这里保留 `request223` 字面是为了忠实展示原模板中的两个位置，不代表未来228应沿用历史event来源。未来独立入口还必须逐项改为其真实request/schema/frame/namespace/source计划；这些身份接线属于R540，当前不预造。

对eabd模板只做这两处计数各1的文本替换，预览75734 B / `133f4466be57717f04e1d33b31ca2b85f32b0c26d62b88f43c3c4adfb8c7591f`。这个身份是**源码文本组合预览**，不是新科学入口或actual结果，不收入Git作为完整重复源。

正常finish_chain与always recovery均调用同一 `assemble_chain / publish`，所以未来接入后两条路径会使用同一新formatter，不存在只改正常readback而遗漏recovery的假完成。原worker各批必要记录先写盘再退批raw、真实eligible后才移交末pair的顺序不改；新表示位于最终一份whole-chain组装处。

## 7. 单90KB与精确scope

原 `SUMMARY_LIMIT=90000`、canonical+LF、原identity事件、单BEGIN/END帧、超限70均不改变。原主body成功与科学门成功仍是不同命题。

R533没有 universal fit保证。已知223 trial计数给出selected-query index-set有24行，普通表转置仅这一项可省1773 B原结构字节，不能单靠它支付23011 B超限。因此模块同时处理多个已确认仍重复的具名部分；两RMS组是否相等和各部分实际大小必须由新真实执行返回。

完整source容量性质是：任何新输出schema都比完整R512输入body短，所有新header/身份费用计入；否则原body保留。该严格字节选择是表示选择，不是新增科学判据。旧113011/113361正文未取，不宣称已经知道某角色贡献或新输出大小。

若未来还超限，原不完整body不分包、不截断成功，新增的具名字节记录只说明实际何处占用。它不能恢复原科学数字，也不能被当作全部必要正文。

## 8. 源、实际与生命周期分责

本模块和原f793 formatter均为元数据层。原39数学源、全部97祖先科学pins、其后R407 hole消去和全部原预算仍由未来完整原request声明核回；本件不修改它们，也不以一个小模块pin冒全transitive闭包完成。

未来request228实际接线至少要明确：

- 真实原223基线、历史生成计划和原公开base；
- 新R533实际源pin及原f793源保留；
- 真生成helper/worker的完整内容身份和实际HERE；
- 单份normal/recovery必要schema的两个合法格式；
- 真实request/run/source、同job原父、八批实际试步/FD与未访范围；
- 原owned-process registry/quiet、所有既有readback markers和清理条件；
- 源准备错误时不能伪造科学receipt或读删mutable现场。

不得让源码只生成而无调用，也不得私下猴补旧模块全局。该接口已经给出原最后compose和原overflow两个真实callee点，未来完整请求的其余来源/namespace/报告绑定单独显式派生。

本件不新增独立job、fixture、benchmark、validator、数值验收门或raw保存档案。未构造新的科学结果，不宣布新的fullDN/native/完整闭面成功。
