# 完整 b/S=5/8 独立输入参数：同源、同预算、两项阻尼 .01

2026-11-27，UTC。**完整准备状态，尚无 run21 实际运行、输入或场结果。** 本包从已刊 19 的完整 science/pure/display 文件派生，把科学 seed 的边界总长从 1/2 改为 5/8；profile δ 保持 1/32，metric damping 与 restoration damping 均保持 .01。新 runner namespace 为 `fixed-fejer-meridian-batched-bfiveeighths-first`。没有改动任何 runtime、137 源注册、当前运行的 19/20、队列或 ref。

这是同一个固定 Fejér/R690 目标度量下的新完整 seed/field model，不能声称与 19 具有同一 mean、root、场或费用。选择理由已全文发表于 [宽度与原观测分析](2026-11-27-supported-seed-five-eighths-three-quarters-and-existing-geometry-observations.md)，20,086 B / SHA256 26b8f9ccce6f208f8ac5e09f13a12a543d6be5b258ad061efb8ed11ddcb5950f，Git blob 18bd23b13cf2cee74fca29cf5b774cbd6adc16e1，固定公开提交 a02b2766d2ec89852a4ac8f584b3f5fe772426f5。该分析不是新执行门。

## 1. 完整父文件及可恢复历史

三完整父文件都固定在已刊提交 543cfdf281c9bcd0f9b13197721b003a275c5967：

| 角色 | 完整父路径 | 字节 | SHA256 | Git blob |
|---|---|---:|---|---|
| science | `topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json` | 90652 | `242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67` | `9c4c28ef3c5b189e094c65f51038fafeef48bc48` |
| pure | `topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json` | 80254 | `8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7` | `202b6ca81c72c009c34c04094ef234db2e337328` |
| display | `topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-complete-display-correspondence.json` | 25057 | `cc564e5c273367242aae226913a0dd82ae5b88b3e166fbcbb8da68d6c04edb2d` | `fac08bdbafbefd0e599687e2b7f0a5c6e71382e7` |

新 ready 保留父文件所有原 top-level 键、全部历史嵌套对象、原完整 source 和参数合同。少数“当前”元数据键改写为新分支语义，其旧完整值通过 `bfiveeighths_parent_current_metadata_recovery` 的固定父文件和原 JSON 键精确恢复；没有把科学 argv、formal selector 或 live selector 改成摘要/引用。display 同样保留所有旧历史映射，并将原当前映射完整固定在上述父文件。

再生器先读父文件原字节、核 whole SHA，再作明确 JSON 文本变换。构造后的每个完整 step 可以逆命名空间、还原一个 width 词和原 scope 后恢复成父 step 的逐字段相等对象。所有 runtime 文件复用原件，无新科学实现。

## 2. 科学 argv 的全部变化

原科学 157 个 argv 词仍全部存在，顺序不变；零基索引只有两处变化：

| argv 索引 | 原值 | 新值 | 意义 |
|---|---|---|---|
| 71 | {work}/fixed-fejer-meridian-batched-bhalf-first | {work}/fixed-fejer-meridian-batched-bfiveeighths-first | 本次完整输出目录 |
| 113 | 1/2 | 5/8 | --seed-boundary-total-length 的唯一数值变化 |

纯读仍 7 个 argv 词，只将报告路径与输出 readout 路径换为本次 namespace。其余内容完整保留。所有摘要的值路径原字不变，只有当前 runner 文件名空间重映射。

| 完整步骤 | argv 词数 | 正式 scalar 投影 | 活 scalar 投影 |
|---|---:|---:|---:|
| science | 157 | 458 | 48 |
| pure | 7 | 445 | 0 |

48 活投影保持原 6 项 normal、42 项数学观察，不加入 K/D/alpha 字段。完整老映射的历史记录也未删。当前控制器的 48 上限没有通过本包绕开。

原数值预算逐词保留，包括 M160/J923/N2048、全 32 normal stages、integration8、stage block64、angle block8、全部 192 行选择前缀和额外永久 typed 行、metric directions1/maxiter16、restoration directions4/maxiter64、line trials15、mean maxiter128/backtracks24、profile scalar iterations64、endpoint iterations24/backtracks18，以及原容差/谱参数/范数/全部两见证和六族 geometry 规则。这里的 metric maxiter16 是原 19 实际完整 argv，不擅改成其他历史分支的64。

完整157词和全部投影在 ready 的 `steps[0]`，不是由本段预算举例代替。恢复目标、真正非线性接受规则、F/J/J*、全变量、完整域与所有原限制均未变。

## 3. 两步必要参考输入保持固定 g 的原合同

原 maker 89cc 与 reference e717 的数学合同、全部参数和来源不变，且它们不接收 seed width CLI。本次 width 只在完整10fa科学 argv中改变，不能误写为固定目标图或 R690 scalar 变化。

新独立 runner 仍须真实生成：

- `{work}/fixed-fejer-r690-inputs/fixed-affine-nodes.json`、`fixed-scalar-input.json` 及原完整 maker 输出；
- `{work}/fixed-fejer-reference/reference.npz`、`report.json`、`observations.npz`、`locations.json`、`material-envelope-carrier-binding.json` 及原完整 reference 输出。

新 science 仍逐项读取原固定路径，唯一新 namespace 是自己的科学/纯读/观察输出。每个 runner 的 work 彼此独立；这些路径不能被解释为跨 runner 沿用原 raw 字节。maker/reference 实际 whole SHA、当前完整 reference/field model、point、report、final、typed、root packet 和所有费用身份均保 null，直到原公开入口真返回。固定配方相同不替代本次真实输入读取。

## 4. 准确 seed 定义与未知量

原两个支持仍为 [1/32,15/32]S 和 [17/32,31/32]S，原总长 7S/8。新 b/S=5/8 给：

| 预定准确有理定义 | 值 |
|---|---|
| 每个端层相对长度 | 5/32 |
| 中央总相对长度 | 1/4 |
| 每个中央相对长度 | 1/8 |
| 第一中央区间 | [3/16,5/16] |
| 第二中央区间 | [11/16,13/16] |
| profile δ | 1/32 |

这些是预定参数代数，不是实际 floating carrier、mean 或 λ 读数。新参数满足原定义开域，但没有宣称 mean、projected frame、normal branch、metric 或几何可行性成立。相对 bhalf 的端层显式 4/5 系数与中央 (3/2)λ 比只是已说明条件下的尺度，不是实际 K、reach 或 accepted 的保证。

本包直接以 19 为父，所以与其隔离比较 width；没有把 20 的 .001 恢复阻尼带入。19/20 的在途参数不动。即使 19 后来有 accepted 观察，该点也不作为新分支输入；没有自然 final 时更不能造一个 parent checkpoint。

## 5. 独立 peer 模式与未知历史

原 b8af.load_memory 明确要求：

- independent 模式不能混入 restart、完整父final或另一 seed；
- 五个原已支持的 pending run/source CLI 对必须使用原 PARENT_FAMILIES；
- 新的实际同源 peer 不能仅凭 source 标签被塞进该旧支持家族，或被伪装成已读 typed 列表；
- 未返完整历史、失败后未返回部分与平台终止后的未知记录都不能填成空。

本包保留原五个 CLI 对，逐词未改：

| 原 CLI run/attempt | 原完整 driver SHA256 |
|---|---|
| 45909290354/1 | cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5 |
| 45929088658/1 | 95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9 |
| 45943410994/1 | ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5 |
| 45972294636/1 | c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1 |
| 46011377225/1 | 477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd |

原六个 external 对完整保留，追加两个已有真实官方运行身份的19/20，共八个：

| external run/attempt | 已登记完整 driver SHA256 |
|---|---|
| 46028002241/1 | `2ccf1d251e83850428c577fd522eeadbadd53df79c6f234848ad1eb8b94ccae4` |
| 46028184571/1 | `fff956cc086c8f69c7de87c2d9117792b6b1d5e1de853e59a992fb67e04b4e51` |
| 46031953783/1 | `97ae6ab8a2a19a07b134efc611b442d9e9113ca0b68c0cd322a45ec175d0f8fd` |
| 46037017666/1 | `8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d` |
| 46053911348/1 | `8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d` |
| 46062343475/1 | `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f` |
| 46076669320/1 | `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f` |
| 46079535427/1 | `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f` |

新增19的官方 head 为543cfdf281c9bcd0f9b13197721b003a275c5967，run_started_at=2026-11-27T22:26:37Z；新增20为85cd235221ace28158625a7ced52a24551b509eb，run_started_at=2026-11-27T22:55:41Z。23:21:13 UTC 原API读取时二者均in_progress、conclusion=null。这是启动身份与当时官方状态，不能代替 scientific final 或完整typed历史。新 ready 还给出二者各自已刊完整科学参数文件的精确记录；旧文件中已有的其他版本/失败/来源仍保。

外部责任与实际 transfer 输入分开，已读/未读均不改名。原16终态等事实见其正式记录；官方取消不意味科学历史为空。拟议run21没有runID、head、启动时刻或结果，完整包全部留空。

## 6. 运行源完整复用

当前18 runtime原字，137个完整scientific source path/SHA注册原字。driver10fa、reader8027、launcherf600仍是原完整文件；同一完整source同时可读取不同合法seed参数，来源没有假换名。

- driver SHA256：10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f；
- reader SHA256：8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49；
- launcher SHA256：f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506。

完整总表另列18件与全部137注册，原120历史source pair仍完整保留。这里157指argv词数，137指科学source角色，18指当前runtime，三者不混。

## 7. 参数再生、队列容量和实际执行边界

可选纯文本再生器完整CLI：

`node scripts/resume_20261126/reproduce_fixed_fejer_bfiveeighths_complete_parameters.mjs --repo REPO --output-directory FRESH_DIRECTORY`

它只使用Node标准库读三个完整父JSON，生成三份完整当前JSON并核其预定whole身份，拒绝覆盖不同内容。它不调用科学程序，不下载raw、不改ref，不触发workflow，不是准入步骤。构造时已经做了当前step到完整父step的精确JSON逆映射，运行体不曾被导入或编译。

仅两步的 `{"steps":[science,pure]}` 紧凑对象仍有104,029 B，SHA256 36f7208c1931aed8347a1383a4460ec8476ee40e4997ef3287b9484a17d3cc3e。它不是新队列文件。不能为适应95KB活动队列删掉参数或selector；由root沿已有完整whole-step分期装载方式承接。每份本包单件都小于100KB。

所有大报告、原数组、13成员checkpoint、root packets、rowcache及实际后续mesh/fees只留runner；Git保完整源码、全部参数、真实紧凑证据和恢复责任。本包没有以raw输出重命名为参数。

## 8. 完整参数附件身份

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| [fixed-fejer-meridian-bfiveeighths-science-complete-ready.json](../computations/fixed-fejer-meridian-bfiveeighths-science-complete-ready.json) | 97307 | `6838b79823f398d930982b2d10fd28baf5a6a2f60eb866403331bfd34eb67d9d` | `6da95445b088f8593ff0f5fb14d76167b26a7a21` |
| [fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json](../computations/fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json) | 86702 | `b750fd865256366a5fcf6b020570a74c053ad853d4b34d0ff983ad3895388822` | `5b2b58e75572b75ce499c8983adf3ba20278211b` |
| [fixed-fejer-meridian-bfiveeighths-complete-display-correspondence.json](../computations/fixed-fejer-meridian-bfiveeighths-complete-display-correspondence.json) | 29575 | `ef7739227cd03e9a09329d32d144f8fd57235105c02ba470ce6da5ba51619040` | `5a183254da8fcd3d5c523bd6d767440712ef1d61` |
| [reproduce_fixed_fejer_bfiveeighths_complete_parameters.mjs](../scripts/resume_20261126/reproduce_fixed_fejer_bfiveeighths_complete_parameters.mjs) | 21283 | `8e98642cc9383510fe195e83ef87938639bb42f0b2fbac4bde35e9893b0e8d3a` | `60c4407b2b1661d51932177e745a52778e18d676` |

本说明及另附总表组成完整交付。此时 prepared 不等于 dispatched、started、accepted、complete 或任何准确费用已付；后继具体实际返回仍由原完整入口给出。
