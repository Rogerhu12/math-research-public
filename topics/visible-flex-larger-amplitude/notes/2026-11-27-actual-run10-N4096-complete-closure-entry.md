# 实际 run10 固定目标的完整 N4096 观察入口：闭合值缓存、全历史与原变量续接

本说明对应一个尚未科学执行的完整新入口。它从实际 run10 的完整 `c3dc77f4…` driver、`2efa4b1d…` reader 和 `6d2b8e59…` normal 出发，只把当前观察层的 full N 从2048增至4096。固定参考仍为 N2048、M160、J923；完整 scalar、原固定材料图、支持、seed、18字 Q、gamma、32段 normal 选择、全部原外自由变量及原规定范数不变。该入口没有预填未来父报告、最终变量、root packet、场模型或扫描结果的 SHA。

全部19份 runtime 均完整存在，其中3份已刊泛用 source 逐字共享，16份为独立新 basename。16新体共869028字节，每份小于100000字节；它们均已保存完整远端 blob。另给4份完整 stdlib 来源／参数再生器、3份完整参数计划。本轮只做完整文本、SHA、精确逐字正逆派生和参数对象校核；没有执行 Python AST／compile、科学 import、F、J、root、求积、有理区间算例或任何数值 fixture。源码与参数可独立发表，科学执行仅限公开 Actions。分支和队列由 root 处理。

## 1. 原始来源及本次目标范围

已刊 [run09 N4096 完整说明](2026-11-27-actual-public09-N4096-full-frame-packet-entry.md) 是本次 N 分层、角载体、全部地址及变量转移接口的原来源。其 whole SHA 为 `b7225b3a1c497e013022d755078999c343869a098cd36a39adbe0dd308282ed1`，24850字节，固定原提交 `f59ea5b83562d92df10b2ac4d0a50a2a271a5c32`。本次不把该旧 run09 目标改标签：只逐字复用不绑定该目标的 observer/base/Q binder；其余输入与父关系明确绑定 actual run10。

当前父完整入口已刊提交 `5cd30d41213993d3d9278d29ce93e855ffcd756f`。其完整 target canonical 为：

`e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049`。

当前原参考模型 canonical 为：

`081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5`。

完整 material binding 文件为430908字节，whole SHA：

`4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf`。

这些是已经实际返回的输入身份。完整 target 文件 whole SHA `b2408044…` 与上述 target canonical 不混用。当前 frozen reference 的完整2218叶 scalar 表与旧 dc5 carrier 恢复所用2397叶属于不同责任，不能互换。旧 carrier 恢复仅支付历史地址；不提供本次参考精度、当前场值或证书。

新 binding 的 `bind_actual_run10_input`、`independent_chart_binding` 两个完整函数逐字等于 actual `dc3b4064…`。新 N memory 的 `validate_public_binding`、`_validate_independent_target_binding`、`read_carrier`、`_original_p0` 四函数逐字等于 actual `f1c6629f…`。完整 run／attempt／step、immutable public snapshot、六个 whole input、全部160 fixed-chart词、准确 affine mesh、完整 target/model/reference/bundle、实际调用路径仍由原代码读回验证。没有以 metadata=true 代替这些完整文件。

六个原输入的 whole 身份继续由 actual run10 完整 binding 绑定：warm `3df37dd3…`、node `1fed8f9b…`、scalar `aa7af21d…`、reference `512f1314…`、carrier `71f0048e…`、preparation `35fdae48…`。原完整六 SHA、大小和路径保存在已刊父 ready／provenance、真实 binding 与新94角色来源闭包中，不为 N 变更重新生成或假改这些字节。

原 target 的 `same_original_fixed_chart=true` 与 `same_mathematical_g_claimed=false` 同时保留。后者表示没有对其他历史冻结目标声称数学相等，不表示已经证明数学不等。本次“同 g”仅指新旧 N 观察入口对这个实际 run10 完整已冻结 target 的逐对象等号；该等号由严格模型关系验证，不由 chart SHA 单独推出。

## 2. 参考层与当前观察层严格拆开

| 项目 | 固定参考／模型输入 | 当前 N4096 外场观察 |
|---|---:|---:|
| full N | 2048 | 4096 |
| quarter literal angles | 513 | 1025 |
| M | 160 | 160 |
| J | 923 | 923 |
| 径向 legacy／Gauss 载体 | 原完整7377 | 原完整7377及原记忆额外地址 |
| outer radial Gauss | 原每胞8点 | 原每胞8点 |
| 精确 normal partition | 全部 `i/32` | 同一完整32段 |
| 自由变量 | 原 core、三 omega 通道、H | 全部保留，没有新删减或零化 |
| 固定 seed / Q / gamma | 原完整定义 | 同一完整定义 |

新 driver 仍用 `context.create_problem(N=2048,...)` 重建真实固定参考。泛用 base 独立接收 `angular_observation_module`，只把自身当前 observer 设为4096。其 `reference_full_N` 仍2048。固定 seed 对象、全部参考均值积分计划及原 initial core/H 不依赖当前 observer。原 domain 中参考 core 检查密度继续从 `reference_full_N` 得到原16384载体，不随观察 N 改成另一项检查。

原 norm 的完整函数逐字共享，依赖同 M、mesh、radial free mask、径向长度、角过渡参数及全部 core/H，而不依赖观察角数。三份计划保原 `jet-sum, .05, 24` 与两个 damping `.01` 等全部数值参数；旧父 norm 由旧完整 reader 按自己的报告读取和 canonical 验证，不能从新 N 的统计反推旧 norm。当前新 norm、每个角的 roots、全六jet、完整 Gram 和物理扫描仍实际读取，旧 Phi 不当 baseline。

本次没有同做 M320、J1845、改变 quadrature order 或改变 normal partition。那些独立入口不在本包中被暗中组合。

## 3. 原角字嵌入及全部正权行

泛用 `angular_observation_refinement.py` 逐字复用，SHA `8506eb86…`。新角数组的偶数槽直接复制原513个实际 binary64词，不以同公式重算代替逐字复制。奇数槽按已声明的 binary64 $\pi j/2048$ 构造，$j=1,3,\ldots,1023$。完整旧／新 hex 词表、摘要、倍率数组和 source/definition canonical 均保存、重核。

当前 multiplicity 两端为2、内点全部为4，总质量4096。旧偶数槽质量2048、新奇数槽质量2048。因此完整旧载体无损包含于新载体，所有新旧行都有正权；没有采样 cap、依据误差删角或更换原径向观测。

driver 的原 `statistics` 在同一当前 raw 三 Gram buffer 中追加 all／old_even／new_odd 统计。这不产生额外 F。三组均用原完整 radial weights、同损失参数和原 centered/spectral 实现。新 pure 保全部三组并给实际工作归约 gap，明确浮点归约误差未包围，不能把不同批形的旧字段字或旧保存统计假作同一当前 raw buffer。

准确平均关系与连续责任沿用 [R679](../results/R679-dyadic-angular-refinement-and-common-grid-attribution.md)。本交付不重复证明该定理，也不由加倍有限网格声称连续角误差、非多项式 SO3 带宽界或全角分支已经支付。

## 4. 九个完整数值下层与 packet

本次 normal 的完整所有 class 文本逐字等于实际 `6d2b8e59…`；共53个缩进方法定义，改变仅发生在其前面的来源／schema／base／binder／依赖常量。并未用早期没有 closure cache 的 N09 normal 顶替当前数学体。

当前新链保留：

- 每段完整 centred residual、tau目标、域、Newton J3、全部回溯和失败 trace。
- 完整 working-Horner 解析 J3、六列解析 frame 的两角 jet，以及全参数一次 J/J* 活动图。
- C1 frame、detached stage matrix、相邻 frame 的 J6/J9 来源与回退。
- 同一 detached chain 的 closure value cache；每段最终及整链最终仍强制原积分读回。
- reference calibration 的固定原参考字、完整当前 raw defect 与全部 h/h′/h″ 物理 lift。
- 原全部成功／失败／partial 计数、真实 mutable progress 与 immutable root packet。

新的 closure helper 把其完整原方法父来源明确钉为已刊泛用 N normal `ceaaab5f…`。该文件的原方法体与当前 closure 父方法一致，作用仅是完整 AST／原方法来源锚；没有从该文件接受 run09 的 target、场或报告。原 `3d8d…` closure parent 和全部实际 `6d2b…` 来源仍在 `angular_parent_*`／原历史角色中完整保留。

packet registry 新增这一完整 normal/source/schema/base/calibration/analytic/closure 组合，原六个历史 registry 条目原字保留。它仍只复制实际已有缓存，不补根、不升级未算二阶、不用进度文件作 immutable 输入。角次序、order、全部32阶段、已有 J3/J6/J9、frame来源、当前完整点与外报告点分别保留。

增大 observer 会改变读取顺序和批形。准确同场关系必须在同一完整 implicit 分支上解释；新工作场字不被声称与父逐位相同。数值根成功、同节点字或缓存命中都不替代连续 root branch 和误差证书。

## 5. 几何与来源闭包

新 geometry 从 actual `6c676d43…` 全体派生。34个完整 class 方法中，只有 constructor 内来源与 schema 常量对应新真实模型；其余33个方法全文不变。完整 world 六jet、principal curvature两支、reach两号、全部幅度、protected／radius责任、prefix192与append型 typed 行、全部扫描和 pullback均保。

constructor 继续读取实际 adjacent policy 的 `all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained`，没有重新引入曾导致实际早退的旧 `all_original` 键。C1 source 明确钉新 `12a62f4f…`，完整 closure source、actual codefile、policy/model与 active-chain 守卫均保留。

94角色完整 SOURCE_PINS 从 actual75角色派生：59角色保持原键／原path／原SHA；16个替换角色的原记录全部保为 `angular_parent_*`，另补完整 observer和实际父 driver／reader。没有把旧历史 source 在原角色下静默改成当前 source；原08／09／07 parent records继续是各自的完整历史身份。

新 source-binding 仍保原纯解析加载所需的 `METHOD_SOURCE_OVERRIDES`、`complete_method_ast`、`_ast_value`、`canonical`、ast/textwrap namespace，以及 closure metadata validator 的完整常量／函数闭包。它同时返回完整 closure诊断和 angular_observation，不以整函数替换漏掉任一归属。

## 6. 原 P0、完整网格与 typed 历史

当前 memory 从已刊 N09 完整载体策略派生，但其 actual target四个验证函数逐字等于 f1c actual10。原 P0十一来源、whole dc5、当前 carrier、当前 preparation全部 new_locations、每个显式 manifest和历史 extra层均保。

任何 tagged grid先按它自身真实 N 解释为 literal cell/u/phi。固定 reference与旧父是2048，新 same-source restart是4096。旧／当前径向字并集乘上完整1025角，再并全部显式永久点；偶数词包含核完整保留原两 G。不得靠坐标数量相等代替词表相等。

终态转移会递归读取父 history.sources 的全部实际文件。全部 curvature／radius／protected三角色、每个 typed family／branch／sign／partner、原 ordinal、首次发现点和已有 ancestry都按实际记录进入新 memory。原 typed prefix不截、不按近活动 cap剪掉。数值值、可行性、旧root或证书不被继承。尚未读回的07／08／09甚至当前10 peer报告继续作为明确未知责任，不把 workflow取消解释成没有新地址。

## 7. 严格 actual10 父与完整13成员

新 transfer 明确接受 actual c3dc driver／2efa reader／6d2 normal／f1c memory作为 N2048同目标父。旧四 parent family原记录保留，但本次 strict terminal/final资格要求原 f1c actual10 memory。旧 cc0a、95559、0dfb、ff544不能因相似 chart或维数通过本次父关系。

模型关系先用 actual dc3b完整 pure政策验证父，再用新 binding验证当前链；只规范化明列 source/schema、observer三字段、六个分别验证的数值policy以及各自依赖 base identity 的 Q/calibration。每个 Q和calibration先核自身原base归属，再规范化。其余整 base/reference/seed/scalar/chart/radial mesh/Q18字/gamma/tau/free layout逐对象相等。没有删除整个 base/model来获得“相容”。

final模式首先消费真实 complete父report，核其全文件并由原2efa读取。科学装配逐个验证全部13个 NPZ成员，原omega/core/H/mesh/fixed_parent_core的finite、dtype、shape与完整字；完整自由mask packing后，新 q.unpack必须重建所有原变量词。旧 checkpoint的base身份与其真实父比较，新current model独立保留自身身份。

纯读又重新读取相同父报告和 checkpoint whole记录、原全部source，并核原reader返回的真实 final摘要。这里的纯读whole身份重核不被描述成重新执行变量装配；13成员及逐词重建发生在完整科学输入构造，二者通过同一whole checkpoint和完整装配记录绑定。源报告读取前后及完整checkpoint再次核字。旧root/cache不作为新self checkpoint载入。

参考 seed仍从固定原 core/H建立。只有 current outer初点在final模式采用父完整free point；原 frozen reference/model/Q不被父 final重新定义。新统计、roots、geometry、finitePhi仍全部读取。

## 8. 全科学后缀与三种完整计划

actual c3dc的 `save_report` 至EOF后缀为20121字节，whole SHA：

`eb1d8813bd161358c451b06b47b570cdfdb9173b12f2661ee7ec37344dbf5254`。

它已包含当前 closure进度记录与packet钩子。新N仅在该后缀的同buffer统计中增加两行 observer归属；移去恰这两行后全文回到上述父字节。没有把更早19574字节的无新增进度后缀冒作当前 c3dc全体。

三份计划均含完整science+pure两步，不写队列、不篡改实际pending对象：

| 模式 | 父要求与初点 | science / pure argv词数 |
|---|---|---:|
| independent | 原冻结参考自由点；完整07／08／09／10未读peer来源责任 | 153 / 7 |
| terminal | 真正完整c3dc terminal report，全历史转入；初点仍原参考 | 138 / 7 |
| final | 真正complete c3dc report＋`final.npz`，全部13成员和free词转入 | 142 / 7 |

只有 command元数据不满足terminal。formal initial-field-failure report可满足原terminal合同但不满足final。没有返回的子科学状态不被造为任一种。三份计划的 future parent report/final SHA及新field/model SHA全为null，来源合法性由实际读取时验证。

原parent实际149个science argv词中的数值选项仅 `--angles 2048`→`4096`；路径、source/mode/history参数另明列。全部norm、μ、p、epsilon、scale、方向数、QP迭代数、Phase I、line search、reach阈值、幅度预算、Gauss order、seed预算、32normal与所有root域／回溯参数均保留。原373／357摘要选择器逐值保留，新增后为386／363；原43项progress选择器完整保留，仍是mutable观察而非科学输入。每份完整两步紧凑queue为85KB左右；整份ready小于100000字节，未因容量删参数、选择器或责任。

same-source restart仍由原完整guard处理，仅接受这个新driver/model/observer的真实同源checkpoint。它与上述旧2048 final→新4096的显式完整变量转移不同，不互换标签。

## 9. 完整再生与实际校核范围

两份分体再生器从固定whole父源执行显式精确文本patch，逐输出核全SHA、大小与逐字逆向恢复。第三份总再生器共享三泛用原件，并验证完整19输出及94源角色。参数再生器读取whole actual10父ready，通过明确N／模式／路径变更生成三份完整输出，逐字核输出SHA和全部原selector值。

本轮确实完成的是JavaScript纯文本正逆重放：16新源码全部正向匹配完整输出，再逆向恢复完整父字节；两actual-input函数、四memory输入函数与实际10父逐字相等；normal整class文本相等；geometry只有constructor不同；所有373／357原selector保留；三个参数对象及确定键序独立重建匹配全SHA。本轮环境不可用，没有宣称执行Python再生器、AST／compile或数值测试。

独立审读由construction定点检查完整新binding和transfer：actual c3dc/2efa/f1c父、完整model归一范围、closure与angular双诊断、pure父whole字节及13成员科学装配归属未发现所读接口阻断。该范围不被扩大为全部数值场或完整包科学验证，也不是新的准入门。

建议来源重放命令（只stdlib／字节；不启动科学）：

```text
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_run10_N4096_complete_sources.py --repo REPO --outdir SCRATCH
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_run10_N4096_complete_parameter_plans.py --repo REPO --outdir PARAMETER_SCRATCH
```

## 10. 当前未付的连续责任

此包是同准确目标上的完整数值观察精化入口，不是连续闭合／等距／reach／全phase证书。完整root同支、whole-angle glue、工作参数逆和quadrature／舍入费用仍须实际同场证据；N4096有限扫描不会自动填充这些费用。当前09／10既有费用消费者均严格绑定自己的完整source/model/packet；本包的新source身份不能不经独立完整适配直接借用旧费用或其完成标志。

同目标的全自由点可被准确数学表示包含，不承诺父子工作字、旧Phi、旧扫描极值或几何可行性相同。所有新的当前场结果和未来证书字段仍由公开Actions真实返回决定。

## 11. 全部 runtime whole身份

| 完整源 | 字节 | SHA256 |
|---|---:|---|
| run10_angular_refined_closure_values.py | 54103 | `c3ce1e6bdca28ab9b0e8977112e1bdd903d9684c3bd68ae18c3ec41b98c8c538` |
| run10_angular_refined_stage_jacobian.py | 25710 | `cd8a39091f595be0df159310712008a8d764024169b0ead9a14c3abcf8013dde` |
| run10_angular_refined_normal_frame.py | 47257 | `ab62ad2878bb26eb55e5365cec0bb9ae53db10bf494189a291da582251e3a642` |
| run10_angular_refined_frame_c1.py | 37361 | `12a62f4f90fe6bf5d2d0b3e8a9658e08219fdfbe37f046c7ecfef641f0ee874b` |
| run10_angular_refined_stage_matrices.py | 47791 | `db4c677a3389c8768319b7d98c229c7781f7a5235d2a75ba93b04c37734fdd93` |
| run10_angular_refined_adjacent_matrices.py | 36766 | `bcc71ec7e59fa8f0e57305937c26afb3a08a008a7c85b053548033a515232b51` |
| run10_angular_refined_calibration.py | 11884 | `c0d140b33ec730f994662cc529022e3658a73e70325ee72c94f9d97bf53970a9` |
| so3_run10_angular_refined_closure_normal_lift.py | 98399 | `e8a3d757046a408fa8d3322b7523d26944c4b8db8bc4a2f5acb4ca0f88ef6e16` |
| immutable_run10_angular_refined_closure_root_packets.py | 71634 | `1ed82d5aed5003af62eb69ec77224a886475ddaa0c9b0574600c7545fe51bf8e` |
| run10_angular_refined_material_envelope_memory.py | 52209 | `c94ef9c04bacb624a150295da004062d7b48aa677c8072f07825f5aeb970a2b5` |
| run10_angular_refined_source_binding.py | 29320 | `86e2227e289c3fe800388207ee0cd8c8d0e62b4b13bf5289e8266f623e1357c4` |
| run10_angular_refined_history_transfer.py | 77212 | `4fb8b134a6fec410fac6e42e5bdaccd96a6ddfdf927aa2913fb874953a020603` |
| so3_run10_angular_refined_closure_geometry.py | 70666 | `4114e913ea7e8eead503198c1eb7f53229257517dca8555a593504a5cb39fafa` |
| fullclosed_run10_angular_refined_closure_so3_qp.py | 89049 | `e2ced68895635c4075ce5a30dd54d7056eb093cd55b0f5a59c0f49f5ff36cd4b` |
| launch_run10_angular_refined_closure_actions.py | 22014 | `a2dc7cb6f6786ef84deb15a23d383a6c2a8aaf062b6e0f4af15b9bab77f09123` |
| read_run10_angular_refined_closure_so3_report.py | 97653 | `74622f7f07164b907700177b5ce5e3b8271ebd12305dd38b0a04030c0154c77a` |
| so3_angular_refined_smooth_triangle_meridian_operator.py | 41592 | `1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529` |
| angular_refined_smooth_triangle_literal_zero_moment_input.py | 30940 | `a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d` |
| angular_observation_refinement.py | 11045 | `8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3` |

上述三份泛用共享原件不另写同名修改。其余16新源全部有独立完整未引用blob。完整闭包还保留原94角色中的历史源码，不复制删除任何历史输入。

## 12. 完整再生器及参数身份

| 完整再生器 | 字节 | SHA256 |
|---|---:|---|
| derive_run10_N4096_complete_lower_and_binding.py | 50832 | `5d76b83888100221dc37964a95fd82f9afa4a548e787033ec233ae90715c1f38` |
| derive_run10_N4096_complete_upper.py | 50279 | `df20b4db9ec3ac80bf314a6ffe77a9a5a373408fb41415731af0046fd3b3dd60` |
| reproduce_run10_N4096_complete_sources.py | 28619 | `9b7f25d91f698ce19db316db05b2b767d7b4a9015c0f1c4b6d10e49f6c710ac7` |
| reproduce_run10_N4096_complete_parameter_plans.py | 33914 | `84fe2e624af801fcafb64d6b762deb66cbe13c7c31af72b671d5f1e35ba8cb75` |

| 模式 | 完整参数文件 | 字节 | SHA256 |
|---|---|---:|---|
| independent | run10-angular-N4096-detached-closure-independent-ready.json | 92595 | `76d4f9f1eebc2da58272d9a7543852e278fd275a75814a1cb4e1872624ae7e47` |
| terminal | run10-angular-N4096-detached-closure-terminal-ready.json | 92166 | `1aa8c96a9b2120aeec012bd42f1e8048e09207e99a2f0104350cbc6fae5b0607` |
| final | run10-angular-N4096-detached-closure-final-ready.json | 92391 | `c1750f66758bdab1f4137653db1b58768419af5ff5536bd25af106d47154e904` |
