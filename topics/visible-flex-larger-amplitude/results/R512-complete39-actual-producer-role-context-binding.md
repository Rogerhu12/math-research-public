# R512：完整39必要摘要的真实表角色接线与原语义保持

作者：OpenAI ChatGPT /root（AI 协作研究助手）  
日期：2026-11-16 UTC  
**可信度：已证明，限固定原组装器与必要字段表示。没有新科学运行、容量保证或原213未返数值恢复。**

## 512.1 已定位的具体缺口

[R480](R480-actual213-eight-original39-pairs-and-necessary-readback-overflow.md)记录 actual213：八次原warm接受和各自fresh FD的续算条件已由真实事件及唯一控制流确认；完整必要文档115134 B和恢复文档115484 B都超过原90000 B，原正文没有返回。其run为43812359001、source为fe0a0d737440bcad59d5af9cb9d08b24131204f4、compute为133116630470。本次不重新获取这份终态日志，不用其他轨迹代替其未返正文，不推测失败样本数、某字段字节占比或能节省的实际总量。

从真实source可直接证明：213实际调用的R454组装器与R479 formatter有五类表名和一个地址列名失接。该缺口不依赖未取得的实际数值。

| 角色 | 原组装器真实输出名 | R479查询的不同名称 | 本次处理 |
|---|---|---|---|
| RMS返回失败样本 | original_RMS_returned_failure_samples | original_RMS_failure_samples | 所有对应lookup和固定角色声明使用真实输出名 |
| midpoint返回失败记录 | original_midpoint_failure_records | original_midpoint_failure_points | 同上 |
| 物理argmax | original_physical_argmax | physical_argmax | 同上 |
| argmax分量 | original_physical_argmax_component | physical_argmax_component | 同上 |
| argmax冻结权重 | original_physical_argmax_frozen_weight | physical_argmax_frozen_weight | 同上 |
| 原RMS检查索引列 | original_check_index | original_RMS_check_index | 两处固定前缀使用真实索引列 |

这里“处理”只改新formatter所查的准确名字，不重命名原组装器输出，不改变一项原科学字段、值、地址、行序、错误或选择范围。

原组装器的add_domain_tables直接向NecessaryScalarTables.add使用上表左列字面；finish原样以该name作结果键。assemble_chain不建立右列别名。213 source plan只接入R479的compose并更换自身来源/请求标签，没有更名这些表或索引。因此对该固定producer的真实已选对象，R479的上述错误lookup得到None，table_parts返回None；相应分支跳过。RMS站点共享还要求固定四列前缀完全相等，原original_check_index与旧错误前缀也不相等。

这是可由完整来源直接得出的不可达分支结论，不是由115134 B这个总量猜测。它不说明R479所有变换都未发生：selected-query地址、其他固定metadata、其余context与pair共享各有独立真实条件。原未返operations正文不能从本次源码分析补出。

## 512.2 全部来源和新文件

| 来源 | bytes | SHA-256 |
|---|---:|---|
| 原206/213真实基线reader：root_20261116_thirty_nine_tabular_chain_readout.py | 75482 | 9840e9ae7c1219b9b3bbef45d4bacb7110f639e980f76a6d592eb9f96c9bb68f |
| 原213 plan：request213-necessary-context-source-plan.json | 5652 | 5cd405f3a8ef58bc27019fadd8036d7f293a76fbea1ddd31e095ed652637cf85 |
| 原213实际生成reader | 75610 | 3160c22d42abb1103ba1f1d3d71b172fbfe6d09cd938ecb7fac1bc5032ae11b5 |
| 原R479 formatter：root_20261116_thirty_nine_necessary_contexts.py | 20813 | 689517df7b70b839112f9ba9ab7daf8d6144decd72c89215a22c35ab9c5f8b7c |
| 原R479完整条件论证 | 16363 | 31a25a19695f76e40c3b015ecd8755caeb96ed6b74fab6768404c370f86788fe |
| 新formatter：root_20261116_thirty_nine_actual_role_contexts.py | 20883 | f79328ed83fee9757de1f5987067a0187b5cba53d7daf5b82a610149540ebd54 |

原213实际生成reader的来源仍是同一原206 reader按已刊plan明确替换。其输出身份来自R480已返回的source receipt；本次只读公开小源码/plan与既有结果，未执行/import/AST/compile科学代码，未做容量fixture。

新formatter在完整旧20813 B文本上作以下全部修改，除此之外字节保持：

| 旧字面 | 新字面 | 出现次数 |
|---|---|---:|
| "original_RMS_failure_samples" | "original_RMS_returned_failure_samples" | 4 |
| "original_midpoint_failure_points" | "original_midpoint_failure_records" | 4 |
| "physical_argmax" | "original_physical_argmax" | 2 |
| "physical_argmax_component" | "original_physical_argmax_component" | 1 |
| "physical_argmax_frozen_weight" | "original_physical_argmax_frozen_weight" | 1 |
| "original_RMS_check_index" | "original_check_index" | 2 |
| 模块第一行R479说明 | R512 actual-producer说明 | 1 |
| SCHEMA原R479标识 | R512-complete39-actual-producer-context-composition-v1 | 1 |
| RESULT_SCHEMA原request213标识 | request223-one-necessary-whole-chain-contexts-v1 | 1 |

前六项只是明确的schema符号接线；后三项只如实登记当前模块/新请求身份。新公开文件完整小于100000 B，不是编码、切分或另存科学payload。旧formatter、旧plan、原213执行件及已发生run均不追改。

## 512.3 精确主张

令$S$为上述固定原选择器和R454 assembler形成的一份必要对象。原表语义是明确字段名、全部实际地址、全部已选标量与原全局行序；缺失标量仍按原R454规则为null，不由新方法改为零、false或完成。

令$T$是新formatter的compose，且比较相等仍严格采用原排序ASCII canonical JSON字节：
$$
x\equiv y\quad\Longleftrightarrow\quad
\operatorname{canonical}(x)=\operatorname{canonical}(y).
$$
这不是浮点容差，不把整数和浮点、正零和负零或非finite原token混为相同。

**命题。** 对$S$中每个被原选择器选中的必要角色，新$T(S)$保留该角色的全部上述语义，且可按其明示的固定表头/地址引用展开为同一已选值和行序。格式自己的schema、来源与操作记录会如实改变；命题不把新旧整JSON全文或来源SHA说成相同。$T$不增删科学调用，不重算原数值、FD或判断。

命题成立于原受支持的JSON/table schema；未知表或不满足原完整形状/相等条件的表保留原样。若原值不满足原canonical输出规则，仍沿原错误路径处理，不新增“修复为成功”的分支。

## 512.4 证明

首先，六个符号修改使每一项固定角色及其索引精确对应原producer，未改变任何变换的算法、调用顺序或条件。因而可逐项沿原实际变换建立语义保持，并在其原相等条件成立时使用。

**同一trial的candidate子记录。** 新名称对应原四种已选子角色。share_candidate_components仍只比较同batch与同trial的candidate和complete_RMS；比较对象是其完整剩余地址与全部已选值的有序行列。相等才删重复complete_RMS行，并保完整角色名、原父角色和被删行在原整表中的位置。按这些位置插回父角色的完整行，可恢复原全局顺序及值。非同一trial、任何值/索引/顺序不等、缺父或形状不符均保原行。独立observer错误没有进入该删行路径。

**实际interval地址。** share_interval_addresses只在三类固定表的原integer interval上收集left/right/midpoint地址。每个interval、每个固定地址字段所有观察值必须canonical完全相同且至少出现两次；整列所有行都可由该实际观察值复原，才把列提升到明确的地址表。插回该表对应原值即恢复每行。任何冲突、非整数或缺映射使该列保原行内值。没有从mesh、interval或其他坐标计算新站点；beta、a、ap、app、曲率、误差、merit和权重不进入这个坐标共享表。

**原RMS站点。** 更正后固定前缀为batch_record/evaluation_role/original_trial_index/original_check_index，与producer完全一致。检查索引仍取同一次实际evaluation的原RMS check，关联实际fraction，再用实际interval和返回的s。fraction归属必须无歧义，原返回站点必须完全相等，所有原行均匹配；否则整体不变。引用展开时通过原检查行取原fraction，通过(fraction,interval)取实际原s，故无一项站点值重算、近似、丢弃或跨trial偷换。

**其余typed-query地址。** 原share_selected_query_addresses完全未改。只有一份实际完整query定义、各原query_index有效且kind/interval/fraction逐项相等，才分享这三个原字段；站点、有限性和beta统计留在原行，因而可按明确query引用恢复。

**固定metadata表头。** 白名单及相等条件不变，仅midpoint角色查找名纠正。一个字段只有在全部实际行原值都相等时才升为表头；向每行插回该明确值恢复原列。没有对任意科学数值或错误字符串作递归字典。完整原错误仍在原独立字段。

**相邻context。** 更正角色名和RMS检查索引后，group_fixed_contexts仍只合并原表中相邻且前缀完全相等的行，保剩余原索引与数值；后面再出现同context时另起块。逐块按原顺序展开前缀，得到同一原表。六项修改没有删掉original_returned_sample_index、original_returned_failure_index或任一实际记录地址。

**真实pair共享。** 原share_actual_pair_handoffs完全未改：批次索引连续、前批eligible为true，且当前input_pair与前批完整produced_pair相等才共享；按原前批batch_record恢复该同一回执。不从旧run、hash或单个warm猜status，原下一批仍实际消费移动的文件。

以上每项都保同一必要语义。try_smaller仍将当前表示与这一忠实候选作原完整JSON字节长度比较；无eligible重复或候选不更短时保原表示。无论选哪一支，语义均相同，故按固定顺序有限复合仍保持全部原必要语义。最后仅加入真实formatter来源、原已选文档身份和操作元数据，不覆写原试步、错误或判定。因此命题成立。$\square$

该证明支付的是现在真实producer角色上的实际调用，不依赖“通常存在别名”或之后的独立试跑。R479原条件证明作为固定操作的论证继续有效，但它原源码中的这六处接线不能被称为已经在actual213实际生效；本条明确补正其范围。

## 512.5 原科学、运输和清理责任

新formatter没有读取原场数组/RHS/J/完整FD历史，不调用科学模块，不改变原trial选择。它只接在原assemble_chain完成全部必要选择之后，不能成为原求解前的新科学门。下面全部原合同保持：

- 原actual98真实初父与原accepted/prepared/config/anchor字节；不复用已删213末pair；
- 全39 typed查询、完整H响应、非连续32节点、自由461原QR恢复、三控制与109core；
- 每批原一次model及本次新warm fresh FD，全部实际方向/步长/Richardson/阈值和eligible条件；
- 原最多8批、17档、damping270、4096角、两J worker、1200/600/90/30秒与10500秒原批间钟；
- 原175分钟科学步、195分钟job、10分钟always必要读回与原2700秒规则同步；
- 单份whole-chain及单份独立recovery各自原90000 B界，超限仍70，不互相拼成一个大对象；
- 全部原错误、failed contraction、试步值、失败地址、未返/未访后缀和末参数；
- 原每批必要记录耐久保存后退raw、实际pair交接、读回前owner静止与最终再次quiet后条件清理。

新文件只给223实际来源接线使用；本次发表没有自动声称新workflow已运行、输入已恢复、八批将完成或读回将小于90KB。当前未返213值仍未返，不能从源码或原SHA恢复。本支仍是原有限affine尾优化，不请求当前H非线性native/fullDN，不能据此填完整非零112/338/450接受。

## 512.6 原90KB边界及后继的实际责任

纠正角色可使原本因名字失接而跳过的固定变换检查真实表，但重复是否存在、何种操作更短、最终新增元数据后总长多少，均依赖未来真实输出。源文没有提供某个未见数据的定长上界；一个错误字符串本身也可能很大。因此本条**不保证**新摘要能装入90000 B，不以扩大上限、丢行、分包、通用数值编码或新raw artifact规避。

后继223须把当前formatter的真实文件/完整SHA接进新helper与worker、request/recipe/workflow和实际HERE；保留祖先来源与自身新身份，不能用新文件字节冒原689517df。正式run只用公开仓库Actions，实际结果R513须记录各操作真正生效范围、原selected与输出bytes/SHA、所有原试步/FD/失败地址和真实清理。完整来源实现就直接登记执行，不附加fixture、独立审查或机械重跑前门。

本条来源链接：[R479](R479-complete39-fixed-semantic-context-readback.md)、[R480](R480-actual213-eight-original39-pairs-and-necessary-readback-overflow.md)、[213原接口](../notes/2026-11-16-request213-fixed-context-whole-chain-readback-interface.md)。这些是已刊固定证据；没有进行外部文献推断或新数值计算。
