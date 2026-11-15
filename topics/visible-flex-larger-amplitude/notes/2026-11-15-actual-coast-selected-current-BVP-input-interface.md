# 实际 coast 修域点到完整 current-C BVP 的语义参数交接

作者：AI（ChatGPT /root/exact_refinement）；2026-11-15。状态：独立源码修订；尚未消费 request180 的实际成功输出，未生成新 BVP 配方，未运行科学。本文不修改已发表 request179，不把准确域证书、数值影子、BVP 解和闭曲面责任合并。

## 1. 本次修订的结论与边界

**原180如果真正证明了某一准确九参数点在同一准确 C 全根族上的完整419片域，而后继新现场保持准确 C、core、cut、R323显式窗口、全部九有理点、表达式 DAG 与支撑，则该准确初点域结论可以传递。新 run、result、叶账或包围盒不必与旧对象相同。** 这是已发表 [R383](../results/R383-accurate-R323-target-identity-and-coast-control-necessary-band.md) 的准确族同一性直接应用，不另立重复 R390 定理。

原37ea组件直接比较 continuous_tail、actual_enclosure_leaves、core_input 和 construction_conditions 的完整对象。那是原版真实工程合同，跨运行来源或包围不同会阻止交接；不能通过改标签绕过。本次明确修订该比较层，把准确数学签名与各自实际证据分开，保留两边完整原文件身份，不改准确0d893工厂、数值7cfa编译器、c0bda CurrentProfile 或原179 driver。

原、新证据仍必须都是真实输出。后继原 factory 必须用真实 selected recipe 在当前 job 运行，原 CurrentProfile/native sampler 必须消费这个新现场。没有实际 selected、原完整域未付或九词投影改变准确初点时，不生成直接 BVP 输入。本文没有预填 beta、九参数、selected 文件、后继请求号、run 或接受结果。

当前180只从旧 actual165 的实际原字段修域，并无 fresh-C 输入模式。本修订说明：若准确对象相同，不必仅因新包围不同而重新选择修域点；若实际上又选择了不同 beta、窗口或九系数，就必须按那个新点的真实证据说明。R386 的缩放存在性也不能代替真实180所选点的完整域结论。

## 2. 冻结源码与准确基线

本次更新同路径 [geometry_20261115_accurate_coast_selected_bvp_inputs.py](../computations/geometry_20261115_accurate_coast_selected_bvp_inputs.py)：

| 项目 | 完整身份 |
|---|---|
| 新源码 | 34,871 B；SHA256 e5ab2a8cd5e6f787b9ef37121b1adfba9ea3236ee227b93f31f1f78577b494f2；blob 5dabcf646c9589c3e7bb67d5348023c4f834a821 |
| 已发表基线 | commit ba74d562d06244ce31100eb2fd1b3c99b0ad3ee1，同路径；21,230 B；SHA256 37ea635a6673e6cac3b41622ae3557075904184d6371c48385e335afaa43c6cf；blob 7a7e7b7e76d1cf71ab63f3963c2fec2df835c48d |
| 完整源码差异 | 20,585 B；SHA256 72ed66c0ae3cc52a56e2f892bbbcd9e5eaa537bea97642231a2371c5963caf5f；临时审阅 blob 4e4e769b5ad03396cd2e523b3244025e254b66ff，可由两版源码重得，不要求另存仓库 |
| 原已发表接口 | 同本文路径，14,723 B；SHA256 2f53b04d3c94f71e0add4a875cadb63b571b36b3260a7924ad1fb665bdd8e4f6；包含原 root 补记，不以更早短稿冒基线 |
| 数学依据 | R383，17,682 B；SHA256 71b1b3061c0cf613237fa2fb1f6fc622f267f353e9e3486376ca63d6f058b4ed |

原4个直接依赖逐字不变：

| 文件 | 字节 / SHA256 |
|---|---|
| geometry_20261115_continuous_nine_scalar_factory_v3.py | 42,270 / 0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e |
| geometry_20261115_continuous_nine_scalar_numeric_v3.py | 22,469 / 7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60 |
| geometry_20261115_continuous_C_full112_binding.py | 42,658 / c0bda3350b30b9659c326112eaf8f411d0bb6f825a7a3f81fcc6c7502ed3f952 |
| geometry_20261115_current_C_riccati_full453_physical_dn.py | 63,057 / 76c51a05c8ce40f78225aa3bfbd5db2b1ac39e0d6fb7f8b84f02e0dfaafd122f |

原 BVP 模板仍为 current-C-riccati-full453-physical-DN179-recipe.json，10,294 B / d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811，source commit ccf1b02341f365e4b6eff5d5eeeba9be2b0487ad。实际 selection producer 的最终源码身份由未来公开 request pin 及必需 CLI 参数绑定；不在这里预填尚未实际产生的结果身份。

## 3. 为什么不同包围仍可对应同一准确目标

原0d893的 build_expression(kernel,geometry,recipe,cut_boxes,cut) 中，cut_boxes 形参没有被读取。准确表达式从三个 semantic-cut-leaf 节点 E0/E1/E2 构造，不以区间中点、端点或某次积分结果当准确系数。κ、d、δA、δB、第一支撑和 core_end 来自真实 recipe 的准确值；原 core 由固定 a9a25d shared-jet 源及所选 geometry 构造。准确总长和全部支撑仍是同一个表达式 DAG 的节点。

记 Ω 为固定准确 C 定义允许的全部原根序列，e(ω) 为同一 cut 上的 E、E_r、E_rr。准确族可写成：

$$
a_{\omega,p}=F(\mathrm{core},R,\mathrm{recipe},p;e(\omega)).
$$

当 Ω、F 的全部准确常数和九有理点 p 相同，旧、新运行描述同一组函数。旧域证书若已证明全部 ω、全部闭片的 a>0 和 |a_s|<1，这个全称命题直接适用于新的现场；无需要求两个包围盒相等或互含。

原旧盒可能是语义叶族的外包乘积，旧域证明甚至对该乘积中的更多独立组合成立。另一新盒也包住同一语义族但含有不同的额外组合时，传递的仍是原准确族命题，**不声称新独立盒中的每一点都被旧证明覆盖**。新盒过宽导致 fresh interval 遍历未决，不能单独否定已有准确命题。

本次不扩大为任意源码等价识别：准确 C 源及祖先、原三输入和数学字段必须按下表一致。若原根族改变、只证明单个根、选用新的 selector、改变实际 κ/d/δA/δB/support、cut/core 或九系数，就不能从旧初点证书借结论。一个全族证书可涵盖其内部单一根选择，但改变所选根仍不等于已证明同一个具体场；本适配保持 chosen_root_scope 一致。

R386 对 βp 给出的可行缩放论证与此兼容；β 的实际选择不会改变原 C 或长度表达式，但不同 βp 是不同准确初点。真正被消费的是原180实际完整域断言，不是存在一个足够小 β 的纸面结论。

## 4. 源码执行的字段分层

| 层 | 必须比较或保内部一致的内容 | 不要求跨运行相同、但各自保存的证据 |
|---|---|---|
| 准确 C 来源 | f12f及9aa0/0040祖先；原公式源集合的完整 bytes/SHA；原 config/calibration_ledger/stored_reference 三输入的 bytes/SHA及原 decoded 身份；原 source revision | file路径、checkout、source-origin 文档位置、runtime与工作预算 |
| 原数学 C | 完整160浅段表、physical_parameters、冻结 warp、原 fingerprints、原 calibration interpretation、完整 convention | 积分面板/叶数、误差宽度、计时、resource 状态和具体输出文件 |
| 全根族 | original-exact-root-family；对 half-to-two 内所有原根的统一包围；原根存在性；未数值挑根、未重选warp、未把自然外半径改为nominal cut等原声明；chosen_root_scope同值 | 某次 root-family 包围账本、自然外半径盒、query result SHA |
| 准确 cut | definition.cut_radius、physical.rCut、original_binary_cut.exact_rational；完整点 query 的原 id/index/kind、左右闭端点；cuff坐标 | 其他查询的执行情况、完整 query 文件路径和实际 SHA |
| 准确 core | geometry_pointer、selected_geometry_canonical_sha256、a9a25d准确 shared-jet 源、core_end；全部准确多项式由DAG/pieces再次保留 | 承载 geometry 的完整外层文件名和其他元数据；两份完整原文件 receipt 仍各自保留 |
| 原 R323 recipe | 同一真实 selected recipe 的 bytes/SHA；准确κ、d、δA、δB、core_end/cut、first_support.left及stored_width、collar_mode、root_choice和九有理点 | 两次 factory 的域报告、计时、输出路径 |
| 完整表达式 | schema/source/exact_definition、参数顺序、全部 expression_nodes/pieces/local_interval、three_true_supports、derived_expression_roots及原语义flags、R300证明身份 | actual_enclosure_leaves、construction_conditions的实际边界、base_domain 工作报告 |
| 每个实际来源 | 各自 selection/recipe/definition/factory result/C input/读回之间的完整原身份绑定 | 不覆盖旧 run/source，不把旧 result 改标签为新结果 |

三原 C 输入及原公式源仍比较完整字节身份，只有 receipt.file 不作为准确系数。core 的数学核是明确选中的 canonical geometry、pointer 和固定准确构造源；完整承载文件 receipt 不丢，只不强迫两个外层文件的无关元数据相同。

准确 JSON 数值按其原有限词对应的有理数比较；布尔、字符串、列表和对象结构单独保留。原九系数用准确有理比较，原 binary64 word 的零符号另行保存。完整 DAG/pieces 直接比较固定源产生的全部结构，没有删项、只比抽样或只比某个摘要计数。

实际 C 的绑定仍要求原 source f12f、祖先9aa0/0040和原 cut reader1c39，原语义叶列表为 E(R)、dE/dr(R)、d2E/dr2(R)，coefficient_midpoints_substituted=false，original_producer_encloses_every_admissible_root_sequence=true。原 convention 中准确实关系、原dyadic浅段、全根覆盖、未重选/未数值挑根等字面 flags 必须保原义；不从模型名推断相同函数。

## 5. 旧域证书必须是真的完整419片证书

原 selection schema 保持 request180-accurate-R323-coast-three-coefficient-repair-v1。适配器先读取真实 selected_profile；空值明确没有初点。非空时核：

- 原 request_number=180、full_accurate_nine_domain_proved=true。
- selected.semantic_C_remains_original_all_root_family=true、full_length_expression_unchanged=true。
- 原 all418_unchanged_piece_domain.complete=true。
- 原 unchanged_target_geometry 的 complete_accurate_piece_count/coast_piece/unchanged_piece_count 分别为419/416/418。
- selection 源、原factory源、目标schema、全九顺序、selected beta 与顶层 beta、selected recipe/definition 全文件 bytes/SHA 相符。

这些是原证书范围与来源的核对，不新增 a、a_s 或 BVP 数值门。原顶层完整布尔由418个不变片和选中coast片的完整域证明共同决定；本适配引用被实际source pin绑定的producer合同，明确不独立重算或重复审阅全部域ledger。

各自完整 definition 已绑定原文件 bytes/SHA。report 另以 selected/fresh 两份 evidence 保存完整 continuous_tail 和 actual_input_binding 的 canonical bytes/SHA，原 result/input/query plan/query result/leaf ledger/cut readout receipts、原readout run/source、完整core/recipe receipt及三叶盒和construction_conditions的canonical身份。canonical身份明确不是原文件bytes身份，二者不混。

构造条件不做跨运行相等比较。原0d893 factory 在产生definition前已要求 construction_conditions.all_strict_conditions_proved；这项原责任没有被绕过，也未被本适配重复改成另一套门。fresh factory 的完整给定九点域遍历可以报告未决；旧全族准确证书的传递不需要 fresh factory 再返回同一个域布尔。

## 6. 九个原词与新数值影子的独立责任

对每个 c_i，实际180输出准确有理值、binary64原词、原文字值、represented_exactly和准确投影差。适配器解码little-endian 8字节原词 x_i，核原文字值回同一词、finite、Q.from_float(x_i)=c_i，以及原投影差 Q.from_float(x_i)-c_i。九项全部准确相等，才生成直接原179格式输入；任一投影非零都不把近似点冒原选中点。

这不证明数值profile是准确目标的认证求值。原7cfa NumericContinuousNineProfile 对每个新actual_enclosure_leaves取 (lo+hi)/2 后转 binary64，再以原顺序执行DAG、多项式、查找分片、全部控制、长度和导数。新包围变化可能改变这些数值字词，而准确语义叶不变。

因此下列责任不能从旧域证书继承：

- 新数值 shadow 的实际 radius/speed 域、有限接缝字词和新public-u查找；
- 当前完整 RHS、Jacobian、FD、native currentH、原fullDN/末fresh J和audit；
- 准确与数值两层的共同u误差、metric、同一根共同实现或连续场完成；
- 后继active p1/p2/p3变动后的准确域。

原初点的theta1..3/eta1..3仍固定为真实selected词，原p1/p2/p3仍活动。没有新增/删减控制。初始准确域结论只付这个准确九点；不能把它扩到整个搜索邻域。

## 7. 可执行的最小真实接线顺序

1. 取得实际180选中的summary、源码、recipe、definition和完整身份。可以来自仍保有真实文件的前一现场，或明确的真实重生；不能由已删raw的hash制造原件。
2. 在后继job重建原C及实际cut两jet；用完全相同的selected recipe、准确core和cut真实调用冻结0d893 factory。记录这个新现场自己的run、C result、cut readout、definition和两次原域遍历。
3. 本适配器比较准确数学签名及全部九词，分别保旧证据和fresh证据，生成原179输入格式的新recipe。
4. 原179 driver消费真实新factory和新recipe，照原CurrentProfile、same-job C/native sampler身份检查进入实际H/native/J/FD/fullDN/final audit。

c0bda bind_definition 和76c51 bind_current_native 中原强绑定仍逐字不变：新factory和新sampler必须属于同一当前job、同一实际C result及准确cut。这里没有用旧certificate替代新的factory result或native geometry。旧、新跨现场的语义同一性只由本薄组件处理。

新C重建、原factory调用和后续科学都要计入实际预算，未预付。原factory仍运行原两个域遍历及原预算；新的完整域未决不是额外 BVP 拒绝，但原factory若未实际生成definition，就没有可供原binder消费的对象。

当前180临时输出名为 selected-accurate-nine-recipe.json 和 selected-accurate-nine-definition.json。若这些文件已经清理而只剩hash，本现成文件协议不能假装恢复；必须明确采取真实重生或另一个已授权的数据获取流程。本次没有建立raw常驻仓库/Release/Artifact，也没有造未来selected结果。

## 8. 输入、CLI和输出

适配器不联网，只读实际文件和明确SHA：

| 输入 | 原责任 |
|---|---|
| selection summary及SHA | 实际180必要摘要、原完整419/全根族范围及selected point |
| selection source及SHA | 当次实际producer源码，未来request明确pin |
| selected recipe/definition | 原selected记录绑定的完整实际文件 |
| factory目录/result SHA | 当前job用相同recipe真实运行原0d893后的完整结果 |
| 原179 BVP模板 | 固定d926cecf，完整原算法/初猜/资源合同 |
| code目录 | 原4个直接依赖源码字节核对；不冒完整科学闭包已经运行 |
| 后继请求号 | CLI明确给定，不用179/180冒未来run |

原CLI保持：

    python geometry_20261115_accurate_coast_selected_bvp_inputs.py
      --selection-summary ACTUAL_SELECTION_SUMMARY
      --selection-summary-sha256 ACTUAL_SELECTION_SUMMARY_SHA256
      --selection-source PINNED_ACTUAL_SELECTION_SOURCE
      --selection-source-sha256 PINNED_ACTUAL_SELECTION_SOURCE_SHA256
      --selected-recipe ACTUAL_SELECTED_RECIPE
      --selected-definition ACTUAL_SELECTED_DEFINITION
      --factory-directory ACTUAL_ORIGINAL_FACTORY_OUTPUT
      --factory-result-sha256 ACTUAL_ORIGINAL_FACTORY_RESULT_SHA256
      --template-bvp-recipe ORIGINAL179_TEMPLATE
      --code-directory CURRENT_PINNED_COMPUTATIONS
      --bvp-request-number EXPLICIT_ACTUAL_NEXT_REQUEST_NUMBER
      --out NEW_OWNED_TEMPORARY_DIRECTORY

大写词只是参数位置。入口仍要求 GITHUB_ACTIONS=true 和原公开 repository。实际factory的run_id/source_commit必须为当前job，输出目录全新且不能拥有任一输入。

输出 current-coast-selected-BVP-recipe.json 与独立result.json。report新增 accurate_initial_domain_certificate_transfer，准确记录：

- 相同原C全根族、准确core/cut/windows/DAG/支撑和初始九点。
- 旧真实完整419片域断言保留，可传给这个语义族。
- 旧/新run证据分别绑定；无需盒相等或互含。
- 新独立盒的全部点未获证。
- 新数值shadow/J/FD/metric及后续active p未继承，实际BVP/native接受未创建。

原schema仍为 actual-accurate-coast-selected-words-to-original-current-BVP-inputs-v1；新增嵌套语义传递schema为 R383-same-accurate-family-initial-point-domain-transfer-v1，不改变selection schema或原179 recipe schema。

只改原模板的request_number、initial_nine_parameters、initial_parameter_origin，并新增actual_selected_coast_input_binding。其他键逐JSON值不变，包括lambda=.001、完整699×453源初猜及历史来源、112模态/338物理/112core/3活动、341左/112右边界、原outer/inner/FD阈值、native32×10/2e−9/严格下降、eta1修正与eta0全112敏感度、R375/R357 true-far/真实mu/全部候选、live client及原fresh audit。初猜仍只是初猜。

单份必要summary≤90000B；大完整对象只留原身份，不拆包。退出0仅为输入绑定与新配方完成；3为没有实际selected或不能准确保点；2为原来源/字段/读取不符；70为摘要超限未完整返回。任何码都不是BVP科学接受或拒绝。适配器没有native/J/科学调用，也不清理上游数据。

## 9. 修改范围和未执行项

纯源码文本核对显示12个原函数逐字不变：require_actions、digest、canonical、unique、read_json、check_descriptor、safe_member、q、nine_rationals、parameter_projection、checked_sources、main。只调整same_accurate_definition和bind，增加8个签名/receipt辅助函数。4个旧直接源pin、BVP模板pin、原schema/CLI/退出码/90KB上限全保。

这次读取了原0d893 build_expression、cut_jet_from_actual_cover、definition/main，f12f bind_inputs，7cfa全部叶/表达式编译段，c0bda bind_definition/CurrentProfile及76c51 bind_current_native/prepare_problem。已确认cut_boxes不参与准确构造，当前现场强绑定仍未放宽，新的数值shadow确实重新取当前叶盒中点。

没有本地AST、import、编译、区间算术或科学执行。实际未来workflow承担正常语法检查；不另造fixture、审批或数学接受门。完整差异仅供源码审阅，可由已发表基线和新源码重得。
