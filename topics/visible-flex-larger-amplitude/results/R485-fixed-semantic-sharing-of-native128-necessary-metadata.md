# R485 — 原128四组件必要读回的固定语义共享

AI 作者：ChatGPT（amplitude）；日期：2026-11-16。

**可信度：已证明（限本文有限JSON表示与已列来源、控制流条件）；新reader与request215尚未实际执行。** 本结论不增加数学接受门，不证明原native／full-DN接受，也不把完整组件执行等同于连续几何证书。

## 1. 实际动机与范围

R446记录actual204真实owner达到原容差、fresh replay逐词一致、四个后续组件均完成；最终必要reader拟返回111829 B，因90000 B硬上限退出70，仅795 B错误摘要实际返回。111829 B原对象没有返回，本文没有读到、恢复或拿它作fixture，也没有对实际省下的字节数或新run容量作预测。

本源只改变**已有必要metadata中固定语义重复的表示**。原reader选中的科学数值、全部trial／evaluation、QR必要字段、四组件原scientific report标量与statistics、原失败文字选择、完整阶段地址和未访范围保留。编译、数值数组、原root／RK、完整576×224、112边界、338×112及独立physical audit均不由本reader执行或改变。

独立新源：

- computations/root_20261116_native_simd_shared_metadata_necessary.py；
- 46653 B／SHA256 d2f2b000310f3e04f3a60e51e74000bcf32516ac50b1f1fac97a4534c06d028b；
- 新schema：native-simd-digit128-stats-qualified-semantic-shared-necessary-readback-v1；
- 明确request_number=215、BEGIN_VISIBLE215_NECESSARY_SUMMARY；
- 原直接编辑基线37574 B／93335c21f6129b1f7ae5c62b2ae7db5e90039fcb30ccfdef1a3951985cb24ee7；
- 原选择器历史基线182r3的77510 B／1536a01102f2c6620adbb43c0b8e1708bd57e194961079f0aa3016a152629c28继续按原字段保留。

源码相对93335的完整diff随交付提供。没有本地执行新reader、import项目模块、AST、编译、数值测试或新增fixture。文本、JSON与字节身份处理不称科学验证。

## 2. 要保存的对象与字面相等

令 $V$ 为原选择器从本job真实文件选出的有限JSON对象。它已按原规则省去科学大数组全文，保其身份；原有错误文字选择和行表范围不变。本文不宣称 $V$ 是全部raw的可逆表示。

原parser将每个JSON数值token保为 LiteralNumber，encoded在该类型分支直接输出原词；普通JSON字符串仍加引号。original_canonical固定对象键顺序，但不改变数组顺序、数值词、字符串、null或布尔值。因此：

- 数值 $0$、$-0$、$0.0$、$-0.0$不会因数值转换而合并；
- JSON数字与内容相同的JSON字符串不同；
- 缺失键与显式null不同；
- 数组的行顺序、原地址和嵌套值保持；
- 非标准NaN／Infinity仍沿原parser规则处理，不新增finite科学判定。

这里的“相等”一律指所选值的完整 original_canonical 字节相等，不从同一来源名、完成flag或数学上相等推得。SHA只作所选对象身份；实际共享条件比较完整字节，不仅比较SHA。

## 3. 四组件来源／算术字段的有限共享

### 命题485.1

对每个存在的 components[name].original_fields，仅考虑源码中固定 SHARED_COMPONENT_HEADER_FIELDS 列表。该列表包含真实schema／source SHA、native／full-DN声明、记录系数与原C关系、完整dyadic与SIMD范围、保留的三调用限定与单Stats类型限定等来源／算术声明。它不递归处理任意数值对象，不进入scientific_report、statistics、trial／evaluation或地址表。

对某一固定字段 $k$，只从**实际含该键**的组件取得值，以完整字节分组。一个值在至少两个组件实际相同时，把其一份原值存入 shared_component_source_and_arithmetic_fields 中，并明确列出所有适用component；从这些组件的original_fields移去该字段，记录各component的 original_fields_shared_groups。未参与的值或缺失字段不变。

从表示中按component的group列表重新插入每组原字段，即唯一恢复各component原original_fields。

**证明。** 对固定 $k$，各字节类不交；component至多属于其中一个类。只有真实存在且属于同一字节类的component才列为成员，所以每次删除都有唯一同值来源。不同字段分别处理，不改变各字段内部的对象或数组。由组的完整成员表可把每次删除反向恢复；缺失字段未成为组成员，显式null则作为实际值参加字节比较。故既不增加缺失键，也不混同null，原值全部保留。组件原字段对象在共享前的canonical bytes／SHA亦保为 original_fields_before_sharing_identity。证毕。

此共享不把四组件的科学完成标志合并成新的接受判断。scientific_complete、procedure_complete、resource_partial、actual_error、预算及科学process仍留在各自原语义位置；原native／full-DN声明只在实际相等时按上法共享其原值。

## 4. 固定来源描述符的引用

### 命题485.2

新函数只对以下明确关系考虑 same_necessary_metadata_at 引用：

| 原重复位置 | 候选同值来源 |
|---|---|
| component.actual_parent_return.summary | 同component.original_summary |
| actual_parent_return.temporary_file_manifest | 同component.original_fields.temporary_file_manifest |
| actual_parent_return.temporary_file_count | 同component.original_fields.temporary_file_count |
| actual_parent_return.temporary_total_bytes | 同component.original_fields.temporary_total_bytes |
| actual_parent_return.component_budget | 同component.original_fields.budget |
| post_owner_component_lifecycle.actual_final_state | owner.original_selected_fields.final_state128 |
| post_owner_component_lifecycle.actual_packet | owner.original_selected_fields.input_packet |
| post_owner_component_lifecycle.actual_packet_binding | owner.original_selected_fields.packet_binding |

两侧都实际存在且完整canonical字节相等，且引用正文更短，才替换。引用保原selected value的canonical bytes／SHA与明确路径。否则原值逐字保留。不存在的post字段不会因候选表而制造出来。

**证明。** 替换前已比较完整原值。引用指向的已存在来源给出同一值，附带身份可核其范围。目标字段不在命题485.1移走的header集合中，且两个表作用位置不重叠；引用不删除目标。以引用目标展开即可恢复原重复值。较短条件只决定是否采用等价表达，不选择科学字段，不改变90KB限制，也不决定任何数学门。证毕。

原 exact_metadata_references 全函数仍保留，在上述固定处理之后按原规则共享完全相等的已选字典。解析必要表示时，先按其明确JSON路径展开原引用，再应用固定header组即可恢复原selected字段。引用与组是同一份必要JSON内的可读结构，不是分包、压缩数字或跨工具隐藏大数据。

## 5. 实际空工程日志的固定文件表

actual_error_files原算法未改：逐实际临时文件取receipt，保原错误文本选择及总16000 B限制。空文件是已经完整读得空哈希、实际bytes为原数值词0的文件，不是“尚未生成”。

只有同时满足下列条件的原record才参加固定empty-file表：

- 顶层键恰为 path、original_file、whole_original_text_returned、text；
- 原descriptor键恰为 file、bytes、sha256，path／file均为实际字符串；
- 原bytes的canonical恰为数字0，SHA为实际空内容SHA；
- whole_original_text_returned实际为true，text实际为空字符串。

每行保 original_list_index、原path、原file、原bytes、原SHA。公共字段只保一次 whole_original_text_returned=true与text=""。所有其他record逐个保原list index及原完整selected record；含任何额外键、缺字段、不同字面或非空文本的记录不强行放进空表。原完整列表identity和原条数保留。只有整张表示确实更短才使用。

### 命题485.3

从empty rows逐行复原四键dict，再与other_original_records按原index归位，唯一恢复原工程诊断选择列表及其行顺序。

**证明。** 每个原index恰进入empty或remaining之一。empty的五列保存其全部非公共字段，公共两字段经实际资格逐行验证；两个内层descriptor的键集也经实际判定，所以反向结构明确且完整。remaining不改record。所有原index均保，排序归位恢复原序列；未知／不存在文件未进入列表，不能被反向生成为空文件。证毕。

此处不改任何非空错误行截取、不增加错误字节额度，也不从空stderr推断没有科学错误。全部原读回失败、未访与资源状态继续由其原字段承担。

## 6. 保留范围与控制流

相对93335，下列函数完整正文保持：

- parsed／encoded／unique_pairs／original_canonical／canonical与LiteralNumber处理；
- actual_error／actual_error_files及原每条6000 B、诊断总16000 B选择；
- ordinary、failed_stage_projection、direct_scientific_projection；
- owner_records_view与原trial／evaluation key-set处理；
- stored_stage_table／scientific_report_view；
- lifecycle_view／component_view；
- owned_quiet与原child-reaped／同用户process范围；
- 原精确metadata引用函数。

build只改当前请求号／scope版本并增加真实直接基线身份；所有原科学文件读取、source／state绑定、owner与四组件选择、error来源、原地址和summary_complete形成条件保持。新 fixed_semantic_sharing 在cleanup_allowed按原条件形成之后、原 exact_metadata_references 之前运行，不读取数值数组，不调用科学程序。

因此，命题485.1–3的恢复结果与原选择的必要字段相同（当前请求/schema/新增解释身份除外）；它们没有证明未被原选择器返回的大科学对象，也没有改变任何原判断。

## 7. request215的独立来源合同

215重生完整204科学合同；不声称读取结束runner里未返回的111829 B对象。原94公开source pins逐项保留，加新reader为95项实际并集。原stage、component launcher、same-job helper、bridge与所有数值核逐字复用，不为改号另复制科学正文。

原helper内部 native204 事件名和 native204-child-close.json 是该冻结producer的来源协议，在新run中保留。新顶层request／workflow／三个独占215临时目录、新必要reader与VISIBLE215帧使用当前215身份；GITHUB_RUN_ID／GITHUB_SHA是真实新job。不得把旧事件文字当旧实际run，亦不冒改过科学producer。

19200总科学钟、6000 owner、1200 replay reserve、8000／600／600／1800组件预算、345／720／345／345额度、120 cleanup reserve、4线程、32×10与2e−9原门保持；2700规则流程、330／350分钟workflow边界及原quiet条件保持。原命令仍在Actions中真实编译／运行；本结论不增加fixture、独立audit或短跑。

215正式request/workflow与实际source/run由唯一发布者绑定。本文发布时没有215结果；R486留作独立实际读回，不预填成功或失败。

## 8. 硬上限、失败与完成边界

MAX_BYTES仍90000。旧 write_result两次长度判定、退出70、attempted bytes／SHA、不分段／不编码／不truncate科学对象、cleanup_allowed=false及原错误表示不变。新共享不保证任何未来实例小于90000 B；若仍超限，诚实返回实际70，不删除科学字段以求装下。

所有原数学值及其类型／位词保留并不等于数学正确性证书。owner达到容差、四组件complete、线性readback数值、native/full-DN接受以及连续C²／metric／reach／held分别承担原责任。R485只支付有限必要表示的来源与可逆性范围。
