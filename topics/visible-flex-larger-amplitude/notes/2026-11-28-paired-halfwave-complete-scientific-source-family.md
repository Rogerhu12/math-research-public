# 完整成对半波科学家族：从19半宽对照独立生成22

2026-11-28 UTC，Astra-larger-e4e2a2bf-20261126。**源码与参数接口准备，不是实际新场或连续证书。** 数学新结论见[R724](../results/R724-paired-halfwave-central-seed-and-complete-source-identity.md)。当前原17–21继续各自实际工作，不修改其来源、缓存或接受历史。

## 1. 具体改动及输入选择

每个旧中央区间各走完整正负波；新种子第一段取 +h_delta(t/2)，第二段取 −h_delta(t/2)。两个中央必须准确等长。两段合起来保原全三均值 Lc*v，因此同准确幅度根及两角根方程保留；每段同长度的最大径向切向变化率减半。中间区域增加真实横向位移，不能以总闭合不变推出位置、Gram、D或principal curvature不变。R724给完整位置、两角jet和统一位移界，未支付新场的几何。

早期准备拟沿21宽度5/8。21真实初有限reach值2.541916739245917比19半宽0.9684249942095058差，但distance-plus转负，已经在各原实际note完整登记。最终22以完整19参数为唯一数值基线：b/S=1/2、delta=1/32、metric/restoration damping=.01、M160/J923/N2048、全部32法向阶段及原所有角/径向/求积/方向/内步/回溯/停止预算。没有通过减角、减阶段或删约束换时间。新namespace为 fixed-fejer-paired-halfwave-bhalf-first。

两原完整固定目标构造器仍重新在本runner生成全部真实输入，原固定g/材料图/无限尾不变。旧输入文件SHA不预填为新返回。新完整seed/cache/校准/model/field/report全部自己的身份，旧trial/accepted/final不作跨run输入。原严格全物理模型比较保留，不允许从旧seed剥去不同字段后冒同场。

## 2. 二十个完整新运行源码

每一文件都实际完整保存，小于100000B。全部完整路径、父字节/SHA、Git blob和原137角色在[完整当前绑定](../computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json)中，下面SHA是整文件，不是片段。

| 角色 | 源码文件 | 字节 | SHA256 |
|---|---|---:|---|
| seed_reference | `fixed_fejer_paired_halfwave_meridian_reference.py` | 43697 | `cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0` |
| meridian | `fixed_fejer_paired_halfwave_meridian_operator.py` | 40803 | `b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6` |
| new_moment_input | `fixed_fejer_paired_halfwave_literal_zero_moment_input.py` | 34886 | `53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333` |
| reference_calibration | `fixed_fejer_paired_halfwave_reference_calibration.py` | 11872 | `c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106` |
| closure_values | `fixed_fejer_paired_halfwave_closure_values.py` | 59449 | `3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73` |
| analytic_J3 | `fixed_fejer_paired_halfwave_analytic_stage_jacobian.py` | 25706 | `617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247` |
| analytic_frame | `fixed_fejer_paired_halfwave_analytic_normal_frame.py` | 47440 | `5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e` |
| frame_C1 | `fixed_fejer_paired_halfwave_normal_frame_c1.py` | 37361 | `edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b` |
| stage_matrices | `fixed_fejer_paired_halfwave_stage_matrices.py` | 61280 | `6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2` |
| adjacent_matrices | `fixed_fejer_paired_halfwave_adjacent_matrices.py` | 36766 | `ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657` |
| detached_meridian_values | `fixed_fejer_paired_halfwave_detached_meridian_values.py` | 41135 | `f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e` |
| endpoint | `fixed_fejer_paired_halfwave_normal_lift.py` | 96271 | `c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac` |
| geometry | `so3_fixed_fejer_halfwave_geometry.py` | 88164 | `494c5fc9daffac2417842c7e4619429e5b5370acfc909b206e1d1c8dc02e865b` |
| batched_geometry_binding | `fixed_fejer_halfwave_geometry_binding.py` | 12118 | `45aedd26f59920938f6a6245dca48a06293f6cf1593124762a77063e4d0e5102` |
| root_packets | `fixed_fejer_paired_halfwave_root_packets.py` | 74385 | `8bf66692d39950c1e7c3a2b48812b686ed27a51068316ca7a786dbeaa08aee4a` |
| analytic_J3_binding | `fixed_fejer_paired_halfwave_source_binding.py` | 41966 | `1a510efc3e5285bd3359229d739cecbcfc853d48dfe58b7f9c848343d6827384` |
| envelope_transfer | `fixed_fejer_halfwave_memory_transfer.py` | 78920 | `64a7c4380bb7150cf6738dc3102c7a33bf87dd32ed093f606a1d9b0d369a6bef` |
| driver | `fullclosed_fixed_fejer_halfwave_so3_qp.py` | 99375 | `095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec` |
| launcher | `launch_fixed_fejer_halfwave_actions.py` | 22120 | `6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c` |
| reader | `read_fixed_fejer_halfwave_so3_report.py` | 99816 | `be9bb58fa612fc25ab01458a2d6e21e0fa10c7573dad37e65effb845c6e29e92` |

原 current runtime表的18个职责全部保留，其中scalar_progress完整321be原字共享；再加seed/base/Q三个实际新物理来源，得到21个配套文件中的20个新文件。driver的完整137角色保持137；相对完整19/21父族，17个当前role/path/SHA明确替换，120对逐项原样。原137父表与全部旧源码仍在原路径/原提交，不能把“120不变”冒更早名为original120的集合全部未改。

完整来源传播顺序是seed→base/Q/校准→closure/J3/frame/C1/stage/adjacent/meridian→endpoint→packet/binder→transfer/geometry/batch-binding→driver→launcher/pure。它只是来源依赖顺序；没有新增运行前AST、fixture、benchmark或独立重跑。原完整运行体已有的source/model/实际字段检查照原保留。

## 3. 旧数学及真实工作规则的范围

新seed中的_means、_radial与evaluate主公式原字保留；只有声明的physical profile、完整精确切点、source/schema和分段元数据改变。辅助f848仍完整十二片，求原A_delta及两导数，不把每个物理半波冒完整odd周期。

新base从initial到EOF的全部方法原字：原全cell八点Gauss、cumsum与部分Lagrange规则、全omega/core/H坐标保留。seed计划中的新增六片切点不自动改变外层积分查询。准确根同一性不表示工作字逐位同，所有working积分/三角/归一化/root误差继续待付。

校准完整class原字但绑定真实新base/seed，必须实际重新构建reference defect。全32阶段、原六控制与两泡Q十八字、全参数导数/J/J*、每阶段与末端重读、唯一point/scope缓存键和所有失败路径保留。原callable解包修复和_meridian_data方法来源检查保留。新packet增加c290实际family，旧family记录一个不删。

geometry保原整网格、永久typed集合、两符号distance、曲率、D、全部原prefix行与接受含义；只消费真实新物理源。batch纯绑定更新实际geometry的完整文件名、88164字节和494c整SHA，不用上一轮geometry常量冒充新文件。driver保原statistics/geometry/真实line search顺序与原restoration规则，不混合geometry-first或新自适应阻尼策略。

纯读取器保全部原snapshot、完整输入/模型/校准/source/几何/历史/十三final检查。它明确读新seed六片/跨段抵消和新的radial-plan schema，并将plan的完整physical definition与seed相等比较；辅助均值的all_twelve_profile_pieces_used仍按原辅助规则解释。这个读取器与science准备属于一个新家族，不能替旧源报告背书。

## 4. 全文字再生与真实原始来源

[首四再生器](../scripts/resume_20261126/reproduce_fixed_fejer_paired_halfwave_seed_sources.py)完整记录seed/base/Q/calibration的父与逐字变化；
[九下层再生器](../scripts/resume_20261126/reproduce_fixed_fejer_paired_halfwave_lower_sources.py)保完整各父/当前源码及每处变化；
[七上层再生器](../scripts/resume_20261126/reproduce_fixed_fejer_paired_halfwave_upper_sources.py)保endpoint、geometry、batch、transfer、driver、launcher、reader全部变化。

三者只读写完整源码文本与元数据；不导入、编译、AST解析或执行科学模块，不作新准入门。首两个接受--repo与--output-directory，七上层接受--repo与--out。运行目录须有完整已声明父源码；原父路径与字节留存。真实科学运行直接使用已刊完整新源码，不靠动态重建或隐藏源替代物。

[十三源完整总表](../computations/fixed-fejer-paired-halfwave-seed-and-lower-complete-delivery.json)与[七下层准备表](../computations/fixed-fejer-paired-halfwave-first-seven-lower-source-locks.json)保全部原记录。早期5/8准备不是新实际执行，最终bhalf选择在本记录与完整参数中明确；通用源码都读取实际参数，没有5/8硬钉。

## 5. 下一实际执行与完整未付项

22必须先真实完成自己的两输入，再使用完整157词科学步和原458正式/48live字段。7词/445正式字段的完整pure在科学真实自然返回后接入，95KB队列上限不通过删除argv或selector绕过。实际模型/点/六g/接受/final以新原对象为准，mutable progress不是不可变科学输入。完整required-angle packet与全13final保持原不同合同。

准确消费链另行传播全新137源：物理半波叶必须将t/2、正负号和全部六片切点纳入完整包围，不能只更换旧physical oracle的source标签。原辅助mean费用数学可共享；全角分支、normal32/六jet/全径向尾/working、Gram、上下帽及mixed/allphase、R723和R716仍须同一新场完整支付。旧纯/费用源保持独立可用于旧报告，不强行接受不同新seed。

当前没有新run号、输入返回、reference defect、初场统计、几何、accepted点、final或连续证书。完整family/parameter准备与真正README完成严格区分。root继续接公开Actions真求解、全部费用与固定参数精化，直到原完成标准满足。
