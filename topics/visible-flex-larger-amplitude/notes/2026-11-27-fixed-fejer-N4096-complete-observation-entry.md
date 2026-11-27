# 固定 Fejér 目标的完整 N4096 观察精化入口：原参考、全变量、全历史与三种执行计划

本交付把已经实际生成的固定 Fejér 输入族的当前观察层从 full N2048 增至 N4096。固定参考仍为 M160、J923、N2048，原七项 RN-even binary64 系数作为准确 dyadic 的材料图、完整 scalar、准确 affine 节点、支持 seed、18字 Q、gamma、32段 normal、全部外自由变量和规定范数不变。它没有重建另一个数学目标，也没有同时做 M320 或 J1845。

全部19份 runtime、4份完整来源／参数再生器和3份完整 science＋pure 参数计划均已保存为完整远端未引用 Git blob，每件小于100000字节。runtime 合计960410字节，再生器合计202236字节，参数计划合计294852字节。本文与总表另列完整身份。原源、原参数和旧 N2048 路径保留。

本轮完成的是完整源码、输入接口、参数对象和精确文本正逆派生。没有运行 Python AST／compile、科学 import、F、J、root、求积或数值 fixture。源码就绪不表示已经执行新 N4096，不表示任何方向接受、收敛、连续场证书或研究目标完成；科学运行只限公开 Actions。root 负责真实发布与队列，本交付不写 refs。

## 1. 实际来源、已返回输入与尚未返回的父场

完整观察精化及历史搬运的前驱是已刊 [run10 N4096 说明](2026-11-27-actual-run10-N4096-complete-closure-entry.md)，固定提交 `d840013b9861e02f2e35350c0896cefefc6a2ea5`，其完整源总表 blob 为 `212c423a43e6fb537631ef500f0ba17dfba9a2c9`。本次复用该完整算法结构及 [R679](../results/R679-dyadic-angular-refinement-and-common-grid-attribution.md) 的精化合同；旧 run10 target、warm、field 和证书不成为当前输入。

当前父是已刊 fixed Fejér immutable-point 入口，driver whole SHA `477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd`，reader `274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b`，normal `1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778`。完整110角色来源在本次128角色中逐一保留原 path／whole SHA。当前父原完整参数计划92380字节，SHA `ab5c00086e21faaa5017ea469c4a63e7d389ecc3019b03a28e46b9daaa129578`，blob `13eea0c110a7d98bef3736d1585aa57584402ac3`。

公开 run12 `46011377225/1` 已真实返回 maker 与 reference。以下是输入身份，不是一个已完成的父场：

| 对象 | 已返回的完整身份 |
|---|---|
| 数学 recipe canonical | `957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9` |
| 完整 fixed target canonical | `50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319` |
| reference model canonical | `ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac` |
| 全160 fixed chart 数组摘要 | `af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103` |
| 全923 mesh 数组摘要 | `ca4b5c626e0e5cf1687c40c25a68a76c4e8fbde391bd8c853399400c784dddfc` |
| reference NPZ whole SHA | `212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb` |
| 当前 observation carrier whole SHA | `84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e` |
| reference preparation report whole SHA | `a35e7ed22d3453d69cc746ff6b706735717bb74131d43ece0b7ddda440403900` |
| 完整输入 binding whole SHA | `a6992516e83b53e153bf5d2b9ef8985f7542bff615e2b3edd6e467a2d105f52b` |

完整原标量参数投影 identity 为 `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`；实际 fixed scalar definition identity 为 `d492e4ad97245a8474f1a73a8787aac2fc5691b1f928d0b8ea72224cabd55160`。两者是分别核对的身份。当前2218叶完整 scalar metadata 中 accuracy_reached=false 如实保留，叶数不替代误差已付。当前 reference 与大 carrier 的二进制正文未为本次源码工作读取或另存。

在本交付冻结时没有拿到 run12 科学步骤的完整 terminal report／accepted final。所有新运行、父场点、父场模型、父报告 whole SHA、父 checkpoint whole SHA、accepted direction 数与 typed count 都是 null；ready 中预定路径不是文件存在的证据。进度上的 normal_chain_enter、输入 reference 或 command.json 均不能替代这些父证据。

## 2. 同一准确目标与当前观察层的边界

[ R717 的固定 Fejér 配方 ](../results/R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) 以原7个有理设计数的预定 RN-even binary64 词作为准确 dyadic 参数。理想 Fejér 公式只用于带完整舍入差的解析比较。N4096 不改变这些词，也不以 ideal rational 替换它们。

| 项目 | 冻结参考 | 当前 N4096 读取 |
|---|---:|---:|
| full N | 2048 | 4096 |
| quarter 角数 | 513 | 1025 |
| M | 160 | 160 |
| J | 923 | 923 |
| 径向 legacy carrier | 原完整7377 | 同一载体及完整额外记忆 |
| outer 每胞 Gauss | 8 | 8 |
| 共同 normal 分割 | 全部 i/32 | 同一32段 |
| core、三 omega、H 自由变量 | 原完整布局 | 全部保留 |
| scalar、chart、seed、Q、gamma | 原完整模型 | 整对象相等 |

driver 仍调用原 context 的 `create_problem(N=2048,...)`。新 base 分开保存 `reference_full_N` 与当前 `full_N`，只构造当前4096 observer。固定参考 provider、完整均值积分计划、原 initial core／H 与准确 scalar 不从当前 outer point 或旧 final 重造。原 domain 的固定 core 检查密度继续由 reference N2048 得出16384；本次不把该检查默改成另一项。

准确表示与自由坐标未改变；新旧观察只决定哪些角被实际读取及如何组成当前离散目标。同场解释须沿同一准确 normal 根分支，有限工作根成功不自动证明全角同支。批形、求值次序、浮点归约和工作隐式根可能改变，不能由同 g 推出工作 sixjet、旧 Phi、扫描极值或可行性逐位相等。原连续费用和证书仍须绑定实际新场另付。

## 3. 原输入的完整接线

旧 N10 的三个泛用模块中，observer 硬钉旧4e reference，base／Q也绑定旧 schema。因此本包没有把它们原样换名字冒作 Fejér：observer、base、Q 都有完整独立新体。新的 reference 仍逐字复用实际 `e7175f59…`，seed 逐字复用 `ad52a217…`；base 从实际 `552f75dd…`、Q 从 `ca4fef40…` 完整体派生。

原 `fixed_fejer_reference_input_binding.py` whole SHA `3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f` 继续逐字消费。新 source binding 保原 `bind_fixed_fejer_input` 与 `independent_chart_binding` 的完整实际逻辑，六角色为：

- current_fixed_input_bundle
- current_node_report
- current_scalar_input
- current_carrier
- current_reference_bundle
- current_preparation_report

每个 file record 的真实路径、大小、whole SHA，maker preparation、实际来源、完整 scalar projection、923个准确 affine 节点、160 chart词、完整 reference／target／recipe 的 canonical 关系仍读回验证。模型实际字段是 `fixed_input_bundle_sha256`，不是旧 `original_warm_bundle_sha256`；preparation schema 是 `R690-fixed-fejer-axisymmetric-SO3-preparation-v1`。e717 的实际 `counted_tail_class` 返回 `ReconstructedTail`；完整 `true_scalar=deep.metadata()` 保留，预定叶数及不由时钟选择的记录另在外层 `deterministic_scalar_work`，没有名为 `DeterministicLeafTail` 的实际类。N 变更不重演 scalar producer，更不只检查2218或e640而丢完整 metadata。

输入目录保持 `{work}/fixed-fejer-r690-inputs` 与 `{work}/fixed-fejer-reference`。本源没有读取旧 warm／旧90 chart 来定义当前目标，也不把旧 dc5 当当前 Fejér reference 的 carrier。旧来源在历史归属中保留，等号的范围仅是这个已冻结 Fejér target 的 N2048 与 N4096。

## 4. literal 角嵌入、正权与同 buffer 归属

原513个 binary64角字直接复制到新角数组偶数槽。新奇数槽按明确工作公式 $\pi j/2048$ 构造，$j=1,3,\ldots,1023$。偶数槽不通过重算同一三角公式代替原词复制。完整旧／新 hex 词表、shape、顺序、数组摘要与 source／definition canonical 都保存并重核。

新 orbit multiplicity 两端为2、内点全部为4，总质量4096；even与odd各2048。全部新旧行均为正权，没有删除难角或以候选 cap 限制真实几何扫描。原 radial weights、完整 raw 三 Gram buffer 与全部 spectral／centered 参数保留。

driver 只在原 statistics 的同一个当前 raw buffer 上增加 all／old_even／new_odd 归属，不为该归属额外调用 F。reader 保各组当前统计和实际浮点归约 gap；这个 gap 没有被称作向外舍入界。旧父统计不是当前 even 统计的替代品。准确归属沿用R679，增加有限观察本身不支付非多项式 SO3 的连续带宽、全角误差或 branch glue。

## 5. 全 normal 链、缓存及 packet

新 normal 的整个 `ZeroClosureOperator` class 文本逐字等于实际1aa父。变化仅在模块头的真实来源、schema和依赖身份；没有删改32段求根、每段域、完整目标、回溯、J3／J6／J9、六jet或外参数 J/J*。

完整保留：

- 原 working-Horner 解析 J3与六列 frame 的两角jet，以及全部活动链导数。
- C1 frame、detached stage matrix与相邻 frame 组装的原完整条件、计数和失败回退。
- immutable full-point 所有者、整字缓存 key、transform bypass，以及每段和整链最终强制 fresh closure 积分。
- reference calibration 的冻结原参考、完整 raw defect与 h／h′／h″物理 lift。
- 每个已有 order、全部阶段及角字的 immutable packet，真实 partial／failed counters和mutable progress。

closure 的完整方法父锚保持实际原3d8来源；本轮不借旧N10的目标模型。源守卫仍区分 bound method 与 staticmethod，完整来源记录不把旧 hash 冒作新模块。calibration 的 BASE、BASE_SCHEMA 和 ENDPOINT_SCHEMA 都明确新身份，SEED／MEAN仍原实际来源。

packet registry 只增加当前完整 source 组合，原历史 registry 不删除。packet只复制已有缓存，不补根、不升级order，不把进度点当完整父场。当前 packet point 与外报告 point 分列，源与实际角顺序、所有32段矩阵归属继续保留。

geometry 的物理扫描体保留。constructor 绑定本次真实 C1 `bbeda3ed…`，并读取实际 adjacent policy 的 `all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained`。曾导致旧入口早退的 obsolete all_original key 没有回引。完整 principal-curvature 两支、reach正负号、全幅度、半径／protected责任、原192前缀与无上限真实分离 typed 后缀均保。

## 6. P0、完整网格与 typed 归属

原11份已知历史 payload 的来源、原地址、发现次序和角色保留。Fejér输入已经明确对更早不同目标做 literal material-address 重解释；本次不把那层关系改称同 physical point，不迁旧值、旧可行性或旧证书。

在当前 Fejér 同目标的 N2048→4096 内，旧 tagged角索引必须先按它自己的 declared N2048 解成 literal phi，再并入新1025角域。新 source self-restart 的地址按自己的N4096解；prepared locations仍是原N2048。既不凭 J相同宣称旧不同目标径向物理点相同，也不把 index/1024 当旧 index/512 来静默改变角位置。

完整当前与已知历史径向字集合先按原 code 读取，再与全部新旧角并集；额外显式点和三种原角色也全读。near-active候选数32只限制新候选选择，实际已经拒绝而产生的 typed separation memory无此上限。其 family、branch、curvature_sign、partner、ordinal、first-discovery provenance、原完整行和祖先报告归属均保留。迁移只带地址／类型／发现来源；新场必须重新读取物理值。

unknown peer声明意味着科学历史尚未取得，不等同workflow仍活动。run07曾在05:02:15观察到cancelled，这不是已知的子科学终止时刻或原因。未知typed不能写成空集合，也不能因已知完整网格包含可能地址而伪造未知发现顺序／source／protected晋升。独立模式明确保留原07、08、09、10及尚未读出的当前12 N2048分支责任；后续若取得真实报告再按完整来源迁移。

## 7. 完整模型比较与三种执行模式

新 `compatible_legacy_model` 先逐一验证旧完整3b3模型和新完整策略，随后只规范化明确的 source/schema、当前 observer描述及各自已验证的base canonical。它去除新base的三个观察描述字段后，剩余reference、scalar、chart、seed、mesh、全部Q／gamma／tau和自由布局必须整对象相等。

每个Q自身的base identity与Q canonical先核，再规范化；每个reference-centering定义自身的base identity先核，再处理两项source；缓存／解析工作策略都先按其完整新旧源码验证，再作明确差异比较。不是通过删除任意未知字段制造兼容。

三份完整计划的模式与证据责任为：

| 模式 | 初始变量 | 必要父输入 | science / pure argv词数 |
|---|---|---|---:|
| independent | 原冻结 reference 全自由点 | 不要求未来父报告；完整已知输入与unknown责任保留 | 157 / 7 |
| terminal | 原冻结 reference 全自由点 | 真正完整477499 terminal report，全history与typed迁入 | 138 / 7 |
| final | 真正父末点的全部原free词 | 真正完整report、final.npz、原reader及全部13成员 | 142 / 7 |

independent可单独运行；它不是假称已读父场的续跑。terminal允许原完整合同里的初场失败正式报告或预算终态报告，command-only／progress／缺失report不满足。final还要求原reader完整终态与final bundle验证；terminal合格不自动使final合格。同源restart仍走这个新driver／model／observer的原严格恢复路径，不与跨N的final变量复制混同。

真实父预定目录是 `{work}/fixed-fejer-immutable-point-first`，末点文件精确为 `final.npz`，不是其他前驱的 final-new-field.npz。两个有父计划的report路径是该目录的report.json。三计划的 controller parent_bundle仍指真实输入 `fixed-fejer-reference/reference.npz`，只是执行输入关系，不冒称它是终态父。

## 8. final的全部13成员与完整变量搬运

科学装配先调用完整旧274d reader（verify_final_bundle=true），捕获并重核whole parent report与whole checkpoint，再核完整旧／新模型关系、旧点与旧final geometry两个点摘要。

必须完整读取13个NPZ成员：

`schema, omega_jets, core, Hcap, mesh, fixed_parent_core, zero_closure_model_json, zero_closure_model_identity_sha256, base_so3_model_identity_sha256, fixed_scalar_metric_identity_sha256, endpoint_root_policy_json, working_integration_order, working_full_angles`。

全部数组dtype、shape、有限性、mesh／fixed chart／固定前三词、原N2048及integration_order8等都按实际对象检查。原radial free mask生成旧完整free向量；新q.unpack必须逐词还原全部core、H和三块omega。三omega块有各自真实布局，不能套用旧R/T/Z等长块或只搬前几个坐标。没有删除新旧任一自由量、变更固定seed或用旧final重定义reference。

pure不伪造数值重算：它调用已whole-pin的transfer validator，重新读父reader、whole report／checkpoint、完整装配metadata和来源关系。真正13成员的数值装配发生在科学入口。新模型自己的初始Phi、根、sixjet和全geometry仍全部重读；旧root/cache/Phi及证书不迁移。

## 9. 原预算、全部参数和报告保留

完整ready含全部argv，不依赖下表补足参数。核心预算逐字保留如下：

| 类别 | 保留值 |
|---|---|
| 批形／计算 | stage-block64，angle-block8，torch-threads4，panels128 |
| 规定范数 | jet-sum，radial-norm-length .05，angular-transition24 |
| QP／方向 | damping .01，directions1，maxiter16，active-rows192，qp-atol0，qp-rtol1e-6 |
| 恢复／线搜 | restoration-directions4，damping .01，maxiter64，line-trials15 |
| 几何／幅度 | reach .03，safety .992，active-band .025，diameter4.2，witness .9，height-floor1.01 |
| 目标 | p4，epsilon .001，scale .05，legacy-fraction .5，target1e-9 |
| 根／normal | 32段，root-tolerance2e-12，iterations24，backtracks18，armijo1e-4，control-radius2 |
| Q／gamma | 原完整18字输入及whole SHA；两bubble端点全保；gamma1/16,1/8,3/16 |
| seed | boundary-total-length1/16，profile-delta1/128，radial-order8，profile-order16 |
| mean | maxiter128，tolerance2e-12，backtracks24，armijo1e-4，scalar-iterations64 |
| 当前观察 | 唯一数值变化是angles2048→4096；outer integration-order8保留 |

从实际477499的 `save_report` 至EOF的原完整后缀为20121字节，SHA `eb1d8813bd161358c451b06b47b570cdfdb9173b12f2661ee7ec37344dbf5254`。移去新statistics中的恰两行同buffer observer归属后，新driver后缀逐字恢复该原体。全QP、PhaseI、线搜、真实候选重读、fresh envelope snapshot、packet与progress的原执行顺序保持。

原383个science summary与370个pure summary选择器逐值保留，新增后分别396与380；原48个progress选择器全部保留。新pure同时返回 reference_full_N、current_full_N、quarter_angle_count与完整angular_observation绑定及实际同buffer归属，不把mutable progress作为immutable数学输入。所有失败／partial字段保留实际范围，不以新N将缺项补成功。

三份完整ready均小于100KB，采用紧凑JSON仅为省去无意义空白，没有删键、参数、输出、selector或清理范围。independent两步紧凑队列88319字节，terminal87584字节，final87716字节；三份模式应由实际执行选择，不作为三个已运行结果写入历史。

## 10. 可逆来源再生与已完成的检查

三个源码再生器包含全部19个输出的完整精确行patch、父文件whole记录及完整输出whole记录。读取真实父后正向派生，核全SHA与大小；再逐字逆向恢复父。它们不import任何generated模块，不运行科学，不修改repo或refs，输出目录须在repo外。

参数再生器从原92380字节完整父ready作完整JSON词法块patch。它保留所有未改数字token和顺序，避免Python／JS浮点重新序列化改变已锁参数字；每个新ready均有全正向／逆向恢复以及全原argv、summary、progress保留检查。不是裁剪的模板或只剩变化参数的补丁计划。

本轮已实际完成全部19源的JavaScript纯文本正逆重放及全SHA一致；全部原110个path／SHA对在128角色中保留；normal整class相同；driver后缀关系、三份完整参数及所有原selector保留关系均作源级核对。没有把这些检查称作执行Python或数值验证，也没有额外设置AST／fixture／独立复跑前门。

只读来源重放命令是：

```text
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/derive_fixed_fejer_N4096_complete_lower.py --repo REPO --output-dir SCRATCH
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/derive_fixed_fejer_N4096_complete_binding_and_history.py --repo REPO --output-dir SCRATCH
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/derive_fixed_fejer_N4096_complete_upper.py --repo REPO --output-dir SCRATCH
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_N4096_complete_parameter_plans.py --repo REPO --output-dir PARAMETER_SCRATCH
```

四者均另支持 `--verify-existing`，但本轮没有本地执行这些Python命令。

## 11. 全部19个runtime的完整身份

路径均在 `topics/visible-flex-larger-amplitude/scripts/resume_20261126/`。旧父各完整文件保留；以下全部为独立新basename。


| role | 完整文件名 | 字节 | SHA256 | Git blob |
|---|---|---:|---|---|
| angular_observation | fixed_fejer_angular_observation_refinement.py | 11051 | `52b13e57f058001a5f1640809ae09995c793aadb2ab8eaa54e9c5ab9619d2b21` | `f5945f8375c9f5eeb2b76b7fd8d2194c87140ea6` |
| base | fixed_fejer_angular_refined_meridian_operator.py | 41645 | `3f4d5c0ec5b03eba9e93660e1341c32f1bd4872e0d1250d489894dd4ba6ed915` | `29724c475bfd8c7f15719d5a3761b51d135f6276` |
| Q | fixed_fejer_angular_refined_literal_Q.py | 31363 | `242c31ee2981b9fe64eb0bd25fe5efc76382841e01b31d912b91f57ea0473a03` | `d584dd477b370280e58fd61cb5d6698e8a9d7d4a` |
| closure_values | fixed_fejer_angular_refined_closure_values.py | 59028 | `dc1072bfb384a91950f0ab0df5d04a58c5f6c3d9062e72aa4f6e879d79dc5e49` | `2a0d31594a9286f58dc696a58a749388d36dcb9b` |
| analytic_J3 | fixed_fejer_angular_refined_stage_jacobian.py | 25719 | `272b129c52a3d3ee66a5320da41c5fce16f66c213722d3d9a4d9b708ac116552` | `9abfe9a7f984d40b5088909e20ed8cfcd0383251` |
| analytic_frame | fixed_fejer_angular_refined_normal_frame.py | 47266 | `6cff4f7d99a0b991b3f2737e374b5ec2aa0ca347a9d1cc12b374bd474741af18` | `dd24366c089965f4b43a178808634f3f6c128d0a` |
| frame_C1 | fixed_fejer_angular_refined_frame_c1.py | 37361 | `bbeda3ed59bf5f4af5577e43422af6e8058bd48b41767154c36ee0b8a1c58241` | `5921d15bd92aa5a5b3a05ffe68f69031c08b0365` |
| stage_matrices | fixed_fejer_angular_refined_stage_matrices.py | 47791 | `3ae2c7fc2392881dff88f2fc5ba69b7b31ef3eb2102203076cef170e3df7014f` | `be017bcea84362e5fef4a21849081f90fbd01f1a` |
| adjacent_matrices | fixed_fejer_angular_refined_adjacent_matrices.py | 36766 | `6c8be90344961fc6fef3d8b73a10c49975b5cc6127de2aa47b05452f0f2142b1` | `d926aeed6e68e0bca24b70d6789924254476e755` |
| reference_calibration | fixed_fejer_angular_refined_calibration.py | 11879 | `9eadf599825400b85712591fc27758fb8a5ae21dc9b004cad3691cca45c93f64` | `6a1c6e1eb20ced209d27c7657850f4b771530626` |
| endpoint | fixed_fejer_angular_refined_normal_lift.py | 98437 | `2db038574bb13e226b61826949cc66d917f0186fe5b9156a50eb7180da3d4bda` | `c65014dcebbcc5ccc8949aec47daf50dfbfd99ed` |
| root_packets | fixed_fejer_angular_refined_root_packets.py | 73024 | `fc1c35ff4e3b89e8702c3ce5ddf8ac8f665361624058974ac2b60e26635ff5d0` | `bcdc4344363520db40155fa90a7bceb73233a853` |
| independent_envelope_memory | fixed_fejer_angular_refined_material_memory.py | 48897 | `53ed8f314c1ed20bf618aeb61457b183a6997f0ba36aee58f40ba7c3e5196b82` | `13d8ed6170ae8d05d7816eade56d5eb675f727dc` |
| binding | fixed_fejer_angular_refined_source_binding.py | 27208 | `dddfc5d0476c58c25cac37f5a6ceada612b55de465e91c08c58b098761a7c982` | `6d2ba0513548132ffa4e13f9bfdf1a8ba5eb3fdc` |
| transfer | fixed_fejer_angular_refined_history_transfer.py | 76719 | `4dfdaabe6335b0691d68c9ec25ca516f2d775c30b0653ec93a22117935a0a395` | `e103bb20b9d39bd4f2ca737c1d3a448311d71a7e` |
| geometry | fixed_fejer_angular_refined_geometry.py | 70630 | `9d48b21bd66ba234ebb4b8a1ab42454b9ab63e71abfa9c2eca68aa0d272ee1f9` | `bb8f415d032203bfff29804f19066934bf2fe00c` |
| driver | fullclosed_fixed_fejer_angular_refined_so3_qp.py | 95387 | `c64d2340fb51d67af98f56e3f6bec136048a43ceb9f7d9bc3ff12dc0b0488d25` | `726c884ccfa214d62c6846e651ded5beb811ca40` |
| launcher | launch_fixed_fejer_angular_refined_actions.py | 22014 | `e93b1ef25a24a3f925a33b4c323a7b31dc93b42bd2bda1aca887d8f89aa73e52` | `c1cc488a584631743ff464ba1b6852a29362c5d8` |
| reader | read_fixed_fejer_angular_refined_so3_report.py | 98225 | `7ffea5bfda0108af0276e60a16c29e15669e3ad5996331cf35bdf369d9659507` | `d7885f86f934344bdacb67e1af76f93b3637cfb9` |


## 12. 四个完整再生器与三份完整参数计划

再生器与runtime同脚本目录；ready在 `topics/visible-flex-larger-amplitude/computations/`。完整对象及源表由总manifest给出。

| 完整文件名 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| derive_fixed_fejer_N4096_complete_lower.py | 23644 | `1f67cc21baaf37c5b3e900b2a43fdb7e2bb6f3e4d09fd4510786b27a6bbd38e7` | `fe7f2ea50a3362208f17659863be25b52229d593` |
| derive_fixed_fejer_N4096_complete_binding_and_history.py | 54990 | `6232a46a229bc628c0c9b2925c8ab259b4d63a366a108fe0152c645863cc5ce3` | `fe6ec8d9356a202318599216bbd8c68af124af3e` |
| derive_fixed_fejer_N4096_complete_upper.py | 61425 | `666e052151730ca180ead57d29e829347aee70ace8ed500543154acfa332c4cc` | `ffe423e2cbd54df7b5c2725ad2d68738da36877d` |
| reproduce_fixed_fejer_N4096_complete_parameter_plans.py | 62177 | `17f76eddb6aecc6585ed22d17f6601b3894fad3ebaa66054f4e4bbe4bf8782d6` | `eb0b3172779561e0ca4b35a2fb06c38b7130b71e` |
| fixed-fejer-N4096-independent-complete-ready.json | 98689 | `c043123ffbfe5ba9c1a66bd0d4065383a5a55b67701eedf422b132f0a2efc2dd` | `36d2248cbb62df828ba8f6779b86ec222c7a836e` |
| fixed-fejer-N4096-terminal-complete-ready.json | 97998 | `3e1edf444c218fe1572d3625af78f03c1e171d37d3e5bcf310aaca255e361fa4` | `4fae84544d51a164dd569ef082a6399c873ef47d` |
| fixed-fejer-N4096-final-complete-ready.json | 98165 | `a4d8177de83db5b132167ddd4260cdca0dbcf4f6bb7c6b1d5bb8d7d19e3ff5a0` | `e8630b0847583a9e4a4dd11748cf4534429f462d` |


三份science输出目录分别是：

- `{work}/fixed-fejer-angular-N4096-independent`
- `{work}/fixed-fejer-angular-N4096-from-terminal`
- `{work}/fixed-fejer-angular-N4096-from-final`

每份完整science输出report与command，随后原完整pure读取同report并验证任何真实final bundle，输出相应postprocess JSON。全部原输出／清理规则／进度字段在ready中完整保留；未预填任何未来runner文件。

## 13. 未付范围及后续证据责任

这是一项同固定Fejér目标的完整角向观察精化，不是径向mesh精化，也不是自由模数增加。它没有证明N4096离散目标已下降、某个方向已接受、首场已经存在、全域Gram正定、whole-angle根唯一／同支、曲率／reach／支持费用、全相位闭面／握持／非全等幅度目标已满足。

当前Fejér mean、whole normal32、连续六jet、Gram/K/support、闭面与R716消费者都各自绑定完整source／model／snapshot。新N源不能直接冒用旧来源的完成标志；后续费用如要读取本族，必须以真实新point、packet、全部角与source关系明确适配。这是实际数学输入范围，不是为本次求解另增行政准入门。

新N独立模式可在真实N2048父未返回时从原固定参考初点执行，完整unknown义务保留。终态／末点模式则只能读取真正返回的完整父材料。三者均不会把未知父写成零、把旧分支进度当可用末点、把来源准备当研究完成。
