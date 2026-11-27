# Run16：完整同场网格、物理时间与固定目标精化输入

记录：2026-11-27 18:00 UTC，Astra-larger-e4e2a2bf-20261126。**本条是完整源码及参数适配；尚无本入口实际网格、精化数值或完成证书。** Run16原完整科学继续，实际Phi/Gram/几何/trial见[逐点数学记录](2026-11-27-run16-initial-mathematics-and-point-bound-progress.md)。实时观测不能充当此网格消费者的完整物理场输入。

本适配把已刊[固定Fejér全网格方案](2026-11-27-fixed-fejer-complete-same-field-phase-meshes.md)严格接到实际stage-point-observed driver、pure reader、launcher、120个科学source roles和新的完整闭面消费者。全部网格数学、原8924B构造、当前点全部坐标、32-stage法向求解、全径向/全圆/六jet、三个空间级、五个物理时刻、三个时间级、原完整参数及公开边界保留。完整标记帽与上下片仍按原合同读取。

## 1. 完整父体和新增文件

唯一直接父包为提交244906aebea68c73a74cda79f108df35953c8402，完整总表computations/fixed-fejer-complete-same-field-phase-mesh-delivery.json（52129B/SHA25667a00fce6d444eab3776c23e10f574e4e8196362fe22243ae672c9e867a98bc8，Git blob52ed2efc4b6509699a7786a94dbb8ba20854c451）。其源、完整原参数、数学说明、run10及更早来源全部留存；本条没有替换或删去旧包。

三个新运行源分别是完整input binder、完整mesh producer及完整pure reader。准确的全网格算术文件39436B/80116a4b不变，直接引用其已刊完整文件，没有重写或复制另一套算法。下表列出每个完整源码/参数的最终身份：

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| fixed_fejer_stage_observed_same_field_mesh_input.py | 73265 | b982e6d3ed8bb4e9615b5232932222bdb9298f95abfc9e3943875794f64a65d7 | a1711adb4adbf08f860da5c106c91f23d1b8267d |
| fixed_fejer_stage_observed_complete_same_field_phase_meshes.py | 50400 | 3e9a9f8fc63af7fde35442f7c5cf9d4f11c1d851fe4c8659e814e630d952b070 | d09a23ae04f618138aa05f3d7bb7846bbf927dc9 |
| read_fixed_fejer_stage_observed_same_field_phase_mesh_report.py | 22150 | cd33879cc6b0164faac661b3c79f9084db1aa0e70a27c86fe56ecef6d7c4968e | 53cafef3831afd17c218b8832ec1f7c568cde330 |
| fixed_fejer_complete_phase_mesh_arithmetic.py | 39436 | 80116a4bcfa2752274cece1148420cdce5c489faba3a8a7c0e92c0f6a8d058e4 | 57c2c563785dab3a1148645225106ca5860e2e2f |
| reproduce_fixed_fejer_stage_observed_same_field_meshes.mjs | 80726 | defeff99c572827974a811ad796b341f23853d87bccb607048fa5415949e8d45 | 9509c47f365fa53c512962486b184a225eafd26f |
| fixed-fejer-stage-observed-same-field-phase-mesh-final-ready.json | 60573 | f47e183bda69adbef11ceb640ef3f698eed8d9f0f207687b08c23117d2e36dad | c83ad722e8e576dcbfaba78b63f06b1598dc846c |
| fixed-fejer-stage-observed-same-field-phase-mesh-packet-ready.json | 60542 | 97f5d3fda19c68dec8e0d4d879438088ad6c8b6d4fec021bce3a247ac41a904f | d9469eb9c11c3c41e6d4543b4f4cdc410da76422 |

说明和总表自身的完整身份由同批manifest列出，避免相互包含全文SHA导致循环。每个文件小于100000B。源码是独立完整Python文件，未用运行时补丁包装器代替原体；再生器是完整Node文本程序，仅负责全源和全参数重建。

直接算法父体依次为：

- input：73133B/ad809cb428b7cdd6f3fe082a0057739ff191aefe4abb113e4595fe5e618f0036/blob9cfe9ac9db4760fe83775b2a51da25965670520c；
- producer：48348B/2acc9b4ee82623603d05f6a0951f01a0a3f92a4a640ca69b9f75814a45e5ab2d/blob96b9a32372704d5e58e53e72544d4abd40b4c536；
- pure reader：22120B/fde5c17f6b0a65f99d05f3ec0973571121899ce8844e93228cc68118975cb9b2/blobcd9dfc25d025350d9d175570532d4f011a951408；
- unchanged arithmetic：39436B/80116a4bcfa2752274cece1148420cdce5c489faba3a8a7c0e92c0f6a8d058e4/blob57c2c563785dab3a1148645225106ca5860e2e2f。

这四个完整父体均已按真实大小取回；新三源仅显式source/schema/count及完整来源表改变。原全数学函数由对应原体保留，全部替换列表在完整再生器中。原完整constructor在真实8dc9 driver与原477499 driver中逐字相同：8924B，SHA256d40c3b7e330ea6850997d13891dd17d95b80d3c33e99c9912aa4b5f1da0f3885。本条保留原运行时构造核验，没有另加独立AST、fixture或重跑前门。

## 2. 实际科学来源与完整参数

当前科学driver为fullclosed_fixed_fejer_stage_point_observed_so3_qp.py，95632B/SHA2568dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d；reader为read_fixed_fejer_stage_point_observed_so3_report.py，98763B/c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f；launcher为launch_fixed_fejer_stage_point_observed_actions.py，21794B/ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa。

完整科学SOURCE_PINS有120个角色，完整新网格SOURCE_PINS有127个角色：原120加mesh_input、mesh_arithmetic、实际driver/reader/launcher、完整accurate_input与可选closed source七项。当前normal42b205、packet140f639、source binding917187、meridian552f75与全部历史来源保持准确。所有120角色实际逐文件重读，不能仅从相同目标hash推定来源相同。当前科学manifest为a18da5e44c257156799a01f824079cff15dcdd0f已刊的fixed-fejer-mathematical-progress-complete-delivery.json，41188B/1231359df08d58853b32b03c62ef841127eb9c3f571fc12603b7698c12410544。

新两个完整ready均指向真正97225B/86d39c01d5a93c5a4d897a02d79bddd23a9b98daa6d6fae6940cc5d348da92f6的stage-point-observed independent完整计划。其全部157个科学argv和五项pending peer历史声明原字保留；原source/model/typed/未知责任不清空。每次真正读取原launcher记录时，继续解析**完整实际命令**与全部原source路径，保原repo/当前副本的全SHA与bytes相等关系。跨followup绝对路径不同不等于来源不同，也不能用改写路径省略原文件。

实际新launcher的command schema仍是public-actions-complete-fixed-fejer-immutable-point-SO3-command-v1。本适配直接读完整实际源码确认并保留它；仅凭新文件名猜一个新schema会拒绝真正输入，因此没有这样改写。driver、reader和launcher本身的完整SHA仍严格更新为当前值。

## 3. 同一个实际点的两种入口

完整参数有final和packet两套，每套保32个producer argv及6个pure-reader argv。

**final模式**读取实际完整科学报告与真正完整十三成员final checkpoint；原pure reader、原完整模型和全部坐标共同绑定。缺final不使用initial、progress或一个已知旧点代替。

**packet模式**从已捕获的完整科学报告中，明确选择指定或最新的完整required-angle immutable snapshot。它可以来自trial或缓存点，因此不由packet完整推接受、final或可行性。每个实际当前自由词、完整point文件、记录的全部角、每个32-stage原packet、所需导数阶和model/target/source同时保留。partial cache、单个角、可变进度或初始输入不构成此模式所需的完整对象。

两套入口都保留原完整report capture：读取实际字节两次一致，再保存不可变副本；后来的科学报告进度不能回填这个副本。已消费源码、原固定输入、原command、checkpoint/snapshot、seed、carrier、校准词和输出的完整身份持续复验。输出目录必须新建且在仓库外，防止覆盖原输入。

当前完整问题仍M160/J923/N2048、1333370个自由量、32个normal stages及原三路SO3布局。当前point、模型、固定target、reference model和material chart独立绑定；不能将reference model ea64冒为normal model8cc039。当前scalar是原2218叶、accuracy_reached=false；历史2397叶表不能替代它。six-input binder仍使用原3da43完整核，通过新的720bbfc完整accurate input接入120角色。

## 4. 完整重建与新角读取

原构造8924B完整保留：固定reference context、完整seed law及mean参数、原meridian、原literal-Q绑定、准确32个normal节点、原bubble和gamma、全normal operator、完整旋转H²坐标及原root/积分/thread参数均照原命令。

已有的固定seed、reference calibration、working carrier和全normal root词按原完整记录恢复；缺少的角或导数阶由同一全32-stage算法真实求解。已记录词不凭猜测补成缺失阶，有限root成功不升级为连续分支认证。新网格角度没有因计算成本被截断或退回原quarter角采样。

实际q.M/J/full_N、全部自由词、固定H、数学g、norm和working policy对全部空间级与时间级固定。原8924B构造已复制到新的input体，原core/omega/H同点恢复后再读场。没有再启动优化器，也没有对不同point的mesh直接相减。

## 5. 原完整空间、时间和帽参数

| 空间级 | 每原径向cell细分 | 全圆角数 | 每帽环数 |
|---|---:|---:|---:|
| 1 | 1 | 512 | 16 |
| 2 | 2 | 1024 | 32 |
| 3 | 4 | 2048 | 64 |

全部922个原径向cell、原精确节点/末尾、完整上片和反射下片、两完整p4帽均保留。源读取完整六个物理jet和原raw h/h'/h''校准项；全空间最细读取用于原嵌套比较，没有以若干见证点或预览代替科学网格。

固定物理时刻为0、1/4、1/2、3/4、1。真实相位为
\[
 F_t(s,\phi)=R_{\pi t/2}
 U(s,\Theta_0^{-1}(\Theta_0(\phi)-\pi t/2)).
\]
原固定material chart与逆变换、同一个H、两个固定Cartesian帽继续使用。时间比较分割数为4、8、16；同一个当前场上比较真实物理相位，并覆盖原帽面比较。不能将material角平移或同一material点位移当作物理整像距离。

完整原数值控制为：fixed-chart iterations64、working tolerance2e−12、field-angle-block8、export-levels all；既有root/积分精度和全科学命令全部继承。块大小仅控制完整数组的分块，不减少任何域。

全部三空间级乘五时刻给15个完整科学网格，原科学坐标64bit。另给五份完整可渲染预览：请求96个径向节点、128全圆角、32帽环、32bit坐标；每份严格少于5000000B。预览只改变显示离散，不截断科学网格，不代替全部cell的测度、曲率或误差读取。周期缝和帽接缝使用原准确source端口关系，所有working-word投影差均显式记录，不能借seam投影隐去误差。

## 6. 连续闭面证据是可选、同点且来源完整的附加输入

新mesh的可选闭面来源为已刊be3d3935ea1c4ac8f09c5f1da02d47222794b2a3的完整83826B/eddc1fb7d10cc6a24f8245920b93babbf71886e550ceb1b0293b892323548aa9消费者。主报告路径：
{work}/fixed-fejer-stage-observed-complete-closed-phase-grip-v1/report.json。

schema为actual-fixed-fejer-stage-observed-complete-closed-phase-grip-evidence-v1。完整说明17939B/1ae4af46df209bff88922a2c620ff8f2baf5e71a4001ecc745d8926c24781c6f，见[当前全闭面说明](2026-11-27-stage-observed-closed-phase-grip-r718-source-adapter.md)。

可选证据仍要求最终主报告complete、complete-same-field-consumption、全部输入及生成文件复验成功；逐个保留原全部source/proof/input/output inventories、当前完整同点model/target/snapshot、上游geometry全cover及六jet/曲率/支撑完整标志、原同点binding，以及主报告中唯一R716副件whole record。provisional sidecar不能独立消费。原source真实路径与当前字节相同副本的关系仍逐文件保留。

此合同连接到46719B/3f383d69当前continuous geometry和720bbfc当前accurate input；没有将原d606旧源允许列表放宽成任意源。当前closed新增R718整像下界，但其原全帽/混合pair/allphase/共同支持以及晚失败撤销语义均不变。

未提供可选closed报告时，原准确几何标志保持未付，mesh仍可执行；没有增加closed证书前门。即使绑定成功，准确场的闭面证书也不自动支付working mesh词误差。网格拓扑、有限取值、连续准确场与数值逼近四层责任分别保留。

## 7. 固定g频率输入与精化责任

原频率输入生成仍将当前M160完整物理系数按原三个块的准确地址注入M320，其余高模置零；固定reference chart M160与同一scalar/target保留。原三块映射为[0,161)→0、[161,322)→321、[322,482)→642。完整current M160 point和新输入每个词、来源和全部元数据保留。

这个零包含只生成同一数学输入；没有宣称新M320求解已执行、norm/damping可直接继承、隐式根必相同或精化收敛。原14号独立M320求解也不能仅凭相同g就替代本同点mesh数据。之后必须据各真实完整参数、输出和点关系判定同g/参数/t精化误差，直到原求解容差或机器水平，并如实保留严格存在缺口。

三个空间级、五t和4/8/16时间比较给实际离散证据，但有限metric readout不是整面连续operator上界，几何预览不证明嵌入、reach或强C²。连续Gram≤1e−6、全t reach≥.03D、整像δhold≥.2D、固定有内点grip尺寸以及含反射δE仍须各自同场证明。D仍取整个闭F0。

## 8. 全部读数及原参数对应

原完整producer的110个formal scalar selectors及pure-reader的58个全部保留，只有fresh输出路径重绑定。原active progress48字段全部保留，完整原50字段映射仍在ready的progress_publication_contract中；重复的complete/mesh计数字段继续存在全部正式summary与原完整映射。没有为了95KB队列限制删除参数、summary、输出或数学项。

当前两个完整step对象分别在对应ready内，完整pair compact字节为final16599、packet16587。原16科学对92522B仍运行，完整mesh pair不在当前活队列中强塞；只有真正已返回对象可以退休，完整原对象须保固定历史。normal/geometry/closed/R716及mesh的合法输入关系分别执行，不能用未返进度造完成步骤。

完整producer argv的模板为：
```json
[
  "--repo",
  "{repo}",
  "--report",
  "{work}/fixed-fejer-stage-point-observed-independent/report.json",
  "--command",
  "{work}/fixed-fejer-stage-point-observed-independent-command.json",
  "--point-source",
  "packet",
  "--outdir",
  "{work}/fixed-fejer-stage-observed-same-field-phase-mesh-packet-v1",
  "--levels",
  "1:512:16,2:1024:32,4:2048:64",
  "--times",
  "0,1/4,1/2,3/4,1",
  "--time-levels",
  "4,8,16",
  "--fixed-chart-iterations",
  "64",
  "--fixed-chart-tolerance",
  "2e-12",
  "--field-angle-block",
  "8",
  "--export-levels",
  "all",
  "--preview-radial-nodes",
  "96",
  "--preview-angles",
  "128",
  "--preview-cap-rings",
  "32",
  "--preview-byte-limit",
  "5000000"
]
```

完整pure reader argv为：
```json
[
  "--repo",
  "{repo}",
  "--report",
  "{work}/fixed-fejer-stage-observed-same-field-phase-mesh-packet-v1/report.json",
  "--output",
  "{work}/postprocess/fixed-fejer-stage-observed-same-field-phase-mesh-packet-v1-readout.json"
]
```

final模式保持同一完整参数及数值，只有point-source=final和它自己的fresh输出目录；完整两套均独立刊存，没有用上面的packet例子替代另一套参数。

## 9. 文字再生与实际执行边界

完整再生器读取三个完整父源、两个完整父ready、实际8dc9 driver、ed810 launcher、c9ce reader、完整当前97225B ready，以及准确input/可选closed/说明/未变算术的完整byte identities。它按列明的全部替换产生三个完整运行源，并生成两套完整新参数，核最终字节/SHA；它自身不调用Python、AST、科学模块、F/J/root、数值积分或mesh，不是原科学入口的新验收门。

实际driver的来源表使用Python tuple pairs。文字再生器保留带引号字符串，只将字符串外的tuple定界符转换成JSON数组，再读取全部120项。初稿把该表直接当JSON，源文字读取立即揭示此差异；已在正式再生器内修正。该未发表初稿从未运行科学，未改变三个运行源、原科学或参数。没有用eval导入实际driver来处理纯文字来源表。

完整文字重建命令：
```text
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_stage_observed_same_field_meshes.mjs --repo {repo} --outdir {scratch}/complete-stage-observed-mesh-sources
```

真实producer/pure-reader在公开Actions按对应ready的全部argv执行；源码、完整参数和未知历史的实际绑定由原运行合同保留。所有大数组、原root packets、完整日志、全部mesh、预览及精化逐点数据只留runner，不进Git、Release或artifact。公开记录仅保完整可重生源/参数、实际run、全部whole-file身份与有界数学读数。

本条没有新mesh run、没有实际导出或误差下降数据；当前未来point/snapshot/checkpoint/report/output身份保持null。后续科学自然返回及同点证据到齐后继续完整执行，持续到课题README真正标准满足。
