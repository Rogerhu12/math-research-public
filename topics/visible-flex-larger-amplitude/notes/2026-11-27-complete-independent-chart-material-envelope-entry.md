# Run08：独立固定 chart 的完整材料包络求解与纯读取入口

## 1. 已完成的接口与未返的科学结果

**完整源码与输入范围说明；新的数值结论尚未返回。** 本次完成全部 memory、geometry、history transfer、driver、launcher 和 pure reader，并给完整原数值参数和两个新队列对象。输入 producer 105289 已单独发表、排入真实公开运行45929088658/1；此处使用其完整独立目标定义，不以旧90 chart的错误输入继续。

目标是此前实际 run08 的全部7c chart，而不是旧90 target。全160个固定系数、准确scalar参数、923个准确affine节点、492完整reference model和eeb whole reference都先冻结。完整定义、旧输入失败、原2397叶重建、旧dc5全文件守卫和所有原材料地址责任见[完整producer说明](2026-11-27-independent-run08-fixed-chart-and-complete-old-carrier.md)。旧分支和全部原结论、未返责任均保；不声明两个完整chart已相等，也不声明已付准确坐标共轭。

本次只是接通新固定目标的完整求解，未声称新根、可行场、接受方向、驻点、连续误差或精化成功。原whole carrier实际恢复仍由105289的真实返回决定。

## 2. 完整源码

所有文件在 `scripts/resume_20261126/`，没有拆源码、嵌入大科学数组或只交接口骨架。

| 完整文件 | bytes | SHA256 |
|---|---:|---|
| `so3_reference_centred_independent_chart_material_envelope_geometry.py` | 68275 | `1bccece84925523a5a4a54b4ba021b119a10d4c90a693fe89565200f440fbbd3` |
| `transfer_material_envelope_memory_to_independent_chart.py` | 58387 | `182a4a5401c959c983ebd8c544bdae58c02d5df942c4491b14c89f83880f8590` |
| `fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py` | 75152 | `95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9` |
| `launch_reference_centred_independent_chart_material_envelope_so3_actions.py` | 20746 | `10422033f229649aa2e8237c25880670219d618d24690d429025347fd73f039b` |
| `read_reference_centred_independent_chart_material_envelope_so3_report.py` | 98389 | `f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470` |
| `complete_material_envelope_memory_independent_chart.py` | 48544 | `4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b` |

它们从公开提交 `73215fb2696fb6e921bdc8bb8ec7d559a43d0eb1` 的完整1e2c/ba980/f326/5c5c/a52e/475f父体派生；这些父文件及原guard保持原样。新producer另为61371B/`105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361`，已刊完整源，不以hash替代源。

完整五源差异台账 `computations/resume-20261127-independent-chart-entry-source-patches.json` 为18300B/`81ba3ed8a834844ce5450abe83c6b98acef04d52eb8a5c77d860948491d51231`，含每个完整父、全部精确替换、整输出身份和来源范围。新memory的完整19个文本替换包含于其下面的全再生器。

## 3. 新memory如何绑定整个目标

新的 `complete_material_envelope_memory_independent_chart.py` 使用独立memory、scan、policy和binding schema。原ORIGIN_CHART_SHA90、old warm3df、whole dc5/227202、eff mesh、原P0三类完整指纹和11个完整历史payload常量仍保留。它没有把历史90常量重写成当前7c来宣称同一个旧目标。

`load_memory` 必须收到实际完整binding，禁用历史 `identical_whole_file_directly_read` 捷径。输入步骤依次：

1. 真读当前carrier全部成员，绑定实际preparation、reference、node及scalar文件。
2. 依完整路径重读历史carrier，要求whole dc5/227202，并保原mesh/current cells/u字节关系。
3. 对top与inner独立target definition分别重算canonical identity，并要求两个完整对象相等。
4. 以105289整源SHA及真实函数codefile绑定新validator；该validator重哈希六个current文件和完整历史证据，真读prep/node/scalar及public return。
5. 要求当前完整492 reference model、eeb reference、准确e640 scalar参数、923准确节点和完整7c chart均对应同一真实输入。
6. 从实际 `q.base.context.core` 读取全部160个float64词，同时核数组SHA和逐个canonical hex词，要求与完整target的160词列表相等；不是只核shape或前三项。

新policy明确旧chart、当前chart、新target schema、冻结时点、literal旧角的新phi0解释、未知parallel历史责任和false same-old-g/旧值继承。原数学原子操作未变：完整carrier reader、原P0重建、所有known explicit角色/保护、old/current全径向并集、完整513角、每点六jet、双principal分支、两witness号、原192前缀、near32与无淘汰typed集合全部保持。

`MaterialEnvelope` 的contains、admit、separate、observe、rows、metadata和restore方法逐字保持原体；构造metadata仅加入独立target身份及false old-target声明。整target仍在 `historical_address_binding.actual_path_binding` 中完整传递。pure `validate_report_metadata` 同样要求完整binding并重新读真实输入；部分扫描/失败与fresh空typed集合仍按实际状态记录，没有把未付扫描变成完成。

## 4. history transfer与当前物理循环

新geometry仅把独立memory的整源SHA改为4d92；原完整screen和7299 appended-row数学保持。旧c79严格分支也保留，不扩大其适用目标范围。

新transfer修正原metadata中仍写8c的producer来源，明确改为实际105289。新的explicit independent branch origin记录本次target definition identity、完整reference model/bundle、全部chart身份，以及false same-original-chart/g、旧值继承；运行时和纯验证时都把这些对象与实际q/base model逐项相等。未读的07终态和typed来源依然显式pending；全格覆盖或计数不会重建未知发现顺序。

原 `_compatible_models`、`seed_from_complete_prior_final` 和 `validate_seed_metadata` 完整旧严格分支逐字不变。新ready使用explicit independent入口，初点仍由当前冻结reference的完整原free point形成，不把尚未返的07末场填为父；以后同源重启仍要求完整同model/target/全部永久typed状态。

新driver只改来源闭包、report schema及首F前的目标metadata。全部原科学后缀，从行首四空格的 `def save_report():` 到EOF，**18958 bytes**，SHA256仍为：

`3a34eeb13a52579aacafb1598c52a94a42f8db2cfab03a3fef0d64c2b88937d5`。

root用完整原、新正文比较相等。此前若从不含四空格的 `def` 起截取，会得到不同区段身份；本表严格按完整原行首。没有改初场/候选/接受/恢复循环、原Phi或J/Jstar、Phase I、SOC职责、完整变量空间、范数和阻尼。

原physical base仍6a803，normal仍d5da，reference calibration仍ccb334，adjacent matrix仍955daf，32共同阶段和所有原Newton/J3/域/回溯/角jet及上游active implicit链均保。本次尚未加入另行开发的解析J3或已有root packet；它们必须以完整独立后继源实际登记后再使用。

## 5. pure与实际报告之间的交叉等号

原pure已经核完整source/model/parameter/bundle与全部有限memory/scan/rows。新增 `independent_chart_binding` 补齐此前接口中的一个跨对象关系：memory validator真读的preparation模型，必须就是report里物理表示使用的完整reference模型。

具体要求：

- 顶层完整target等于已验证memory的actual path binding中的完整target。
- report、path binding、新memory validator返回的target identity全部相等。
- 完整target里的 `complete_current_reference_model` 等于 `representation.base_complete_model.complete_axisymmetric_reference_model`。
- 其canonical identity等于492实际reference模型以及validator实读的模型身份。
- whole reference SHA同时等于report的bundle和base的initial reference。
- target数组身份、完整reference与base固定chart身份以及validator实读7c身份均相等。
- 全160词的验证由完整新memory/producer实际执行；上述等号将该真实结果绑定到当前报告，不拿两个各自自洽但不同的对象冒同一输入。

旧strict分支不得自报新target；其新增target字段必须为None。新pure仍小于100000 bytes，完整98389B，没有把部分reader拆走或删掉原guard。

新增报告对象 `independent_fixed_target_definition`、`independent_fixed_target_validation` 和pure的 `independent_fixed_target_binding` 留完整runner报告。队列只选其中明确scalar的身份、bool和schema，不把整个dict交scalar-only summary，也不将数组编码成字符串绕过范围。

## 6. 完整数值参数与执行顺序

完整ready为：

`computations/reference-centred-independent-chart-envelope-run08-ready.json`。

它含40-role全部path/SHA、六个新完整源、三个完整再生器、实际既有输入、原完整参数来源和两整个step对象。科学argv139词、pure argv7词；数字/flag全原样，只有已声明新source/outdir/binding路径与stepID改变。原source和reference也不以新最终自由点替换。

| 类别 | 完整原设置 |
|---|---|
| 空间与积分 | M160、J923、P7377、N2048；stage block64、angle block8、integration order8、panels128、4线程 |
| 范数与方向 | jet-sum、radial length .05、angular transition24、mu .01；1 metric方向/16内迭代；4 restoration方向/.01/64内迭代 |
| 真实接受 | 15 ray trials、原192前缀、QP atol0/rtol1e-6、target1e-9；active band .025；完整E/typed永久筛 |
| 物理预算 | reach ratio .03/safety .992；diameter/witness/height为4.2/.9/1.01；p4/epsilon .001/scale .05/legacy fraction .5 |
| normal | 32共同阶段；endpoint tolerance2e-12、24iterations、18backtracks、Armijo1e-4、control radius2 |
| 固定bubble | (1/32,1/4,15/32)与(17/32,3/4,31/32)；gamma(1/16,1/8,3/16) |
| 固定seed | boundary total1/16、profile delta1/128、radialQ8/profileQ16、mean128/tol2e-12/backtracks24/Armijo1e-4、scalar64 |
| 固定Q输入 | 全原published18词，definition05dc、参数文件df11；由307完整新输入binder绑定实际supported reference，旧逆性质不继承 |

队列保原已排producer完整对象，随后完整science，再pure。science新outdir：

`{work}/reference-centred-independent-chart-envelope-normal-lift-first`。

binding来自：

`{work}/run08-independent-chart7c-run05-carrier/material-envelope-carrier-binding.json`。

纯读parent是已经存在的actual reference bundle，不是条件性的future final，以便实际失败报告仍有机会读回。原warm/preparation不重跑；不删改任何已返旧失败、已登记结论、原数值参数或待合入历史。

## 7. 完整再生与已实际做过的检查

| 完整再生器 | bytes | SHA256 |
|---|---:|---|
| `derive_run08_independent_fixed_chart_input.py` | 20113 | `657c1f5001639f44f4a9d35d7057115b6f94da05c4aecdec2e363fb525374a94` |
| `derive_independent_fixed_chart_envelope_memory.py` | 21461 | `2ea03e5db9e47f151b6c328446bc4f81df1990c072f4e8396995d653d80c8fc5` |
| `derive_independent_chart_material_envelope_entry.py` | 24325 | `8d2d944aeb40c4d24a0d71c902378b7ccace4a7203921bb118026e807d7b3229` |

root与代理实际做的是完整UTF-8文本生成、精确替换发生次数、整源SHA与字节数、全部memory及五entry全文再生、完整科学后缀相等和指定函数/输入接口核对。Python AST/compile代码已包含在全再生器，但当前exec-server不可用，**没有实际运行AST/compile，也没有本机科学import/F/J/root/fixture**。这不增设执行前门；真正source和科学错误以公开Actions的实际返回记录并修复。

全部raw、NPZ、full reports和新目标参数输出只留runner，公开只保完整小源、完整argv/参数、run/SHA与紧凑结论。没有把生成的raw改名为“输入”来保存，也没有预填新target definition SHA或future final。

## 8. 仍须实际完成的研究目标

独立新target一旦冻结，后续同一family及精化都必须保持它。07上的cc0a→M320仍属于原chart目标，不能搬作这个7c目标的同g精化。当前全部新场、完整normal分支、真实方向和其后径向/N/frequency精化仍按实际来源执行。

有限全E筛仍不是连续域证书。完整准确六jet/raw-h-Delta、闭连通C²装配、全t强C²、固定内点握持/整像变化≥.2D、含反射非全等、全t reach≥.03D和整面relative metric operator norm≤1e-6，以及固定g/参数/范围的真实精化与可复现多t网格仍须继续支付。run预算、输入失败或本次源码完成均不构成本题完成。

## 9. 2026-11-27 04:31:48 UTC：终端恢复后的真实源码再生

此前35e4提交时未运行AST的边界保持。04:27终端显式bash/root工作目录恢复后，发现旧临时检出已不存在；root重新以blob:none、single-branch main、no-checkout克隆，再仅稀疏检出本题，并真实pull/rebase至上述HANDOFF所记提交。根README完整SHA581402与课题3c1c均无变。

root现实际运行三个完整stdlib再生器，均退出0：

- producer657c以完整6cc父重建105289，原2397/7377数学段逐字同，AST/compile实际完成。
- memory2ea03以完整1e2c父重建4d92/48544B，在scratch写出同一完整源，AST/compile实际完成。
- entry8d2d以完整五父重建1bcce/182a/95559/104220/f382，逐全文SHA/bytes相等，40-role整文件闭包匹配；所有指定不变函数/声明AST和compile实际通过，旧strict三函数与18958B科学后缀3a34逐字保持。

完整命令分别是各公开再生器的--parent/--out/--verify-existing，或--repo/--outdir参数；输入均为本公开checkout中的完整已刊源，输出只作源码复现。这里未import NumPy/Torch/SciPy或执行F/J/root/数值fixture，不把语法检查当作新场实际成功。原ready的源码检查状态在本次更新为实际通过；实际数值运行仍按公开Actions真实返回记录。

恢复后的真实拉取已读commit依次为 `c45c1bb6dfe27417891c7265eb4e302773a6e12e`、`658c31092cb0995bfc4a52ec3eded7244edf9231`；本次终端推送NFF后立即真实pull/rebase至 `250450ef74f006b09628b2187a16be198e745773`，于2026-11-27 04:36:05 UTC再次核双README完整SHA无变。重推只作普通非强制更新。

真实pull/rebase规则核查：2026-11-27 04:38:09 UTC，origin/main `6bff50b25021f97899b3f3673073b44f0363d8e7`；双README整SHA无变；普通非强制推送重试1。

补记恢复阶段已实际pull/rebase并于04:39 UTC核读的完整提交 `66de8242cec51abe444d7a80013cad8a5894eddf`；双README整SHA581402/3c1c均无变。本行只补全此前终端核查记录，不冒新一次pull。

真实pull/rebase规则核查：2026-11-27 04:49:34 UTC，origin/main `46579cfb5f97c604d1025a1d1caa9ec38de59a0d`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 04:49:43 UTC，origin/main `0bf40b6537302af74fd13b0652c1317b3211db2e`；双README整SHA无变；普通非强制推送重试2。

真实pull/rebase规则核查：2026-11-27 04:52:17 UTC，origin/main `b8cc8fe52d7bd121a088c1f8efc0405e3f5ac333`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 05:02:13 UTC，origin/main `095cbcae6273d52495facc86a338c8d592b5e007`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 05:02:25 UTC，origin/main `3e139ac206cf0637fab220169f9c2d074a035023`；双README整SHA无变；普通非强制推送重试2。

真实pull/rebase规则核查：2026-11-27 05:11:40 UTC，origin/main `0827289eb329d1810acbad242d85b4937784952e`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 05:19:44 UTC，origin/main `a5825f373bb1ea15ffff675c5929391e5a17f2ba`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 05:24:52 UTC，origin/main `f73d7ab9311f92b9da34596e5317a3a66cca730c`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 05:36:48 UTC，origin/main `142888472f216dffaaec606874b57a3642e472e6`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 05:46:57 UTC，origin/main `ed58d5899f35d6c2339d38277c4ef5024241f826`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 05:48:52 UTC，origin/main `4d6d175264279a8796c6c36f615d6e886c7e5c00`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 05:51:57 UTC，origin/main `4b2334dc22a531912327d98040ce60a06a0c9538`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 05:57:41 UTC，origin/main `dafe2c5d206206c1b85bce3552fcb942a8cb515e`；双README整SHA无变；普通非强制推送重试1。

真实pull/rebase规则核查：2026-11-27 06:00:25 UTC，origin/main `1be04000608bfb3c4121466dab0acc08271d64dc`；双README整SHA无变；普通非强制推送重试1。
