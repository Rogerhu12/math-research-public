# Run28：完整实际 final 向独立 R729 源的同 runner 续跑

日期：2026-11-28 UTC。状态：完整源码和参数准备，尚未执行；不修改第33组独立初值包，不修改原28或任何在途源码、ref、request 或队列。

## 1. 要继续的实际对象

本包只接受原 Actions **46108296054/attempt1** 的真实完整返回。原 science source commit 是 `b1a8554a9d88dc176f7295eab4bed9f73f65e3f2`，原 driver 是 `d1c99f555e480a0b37fcefee98e1261033bed0b4bb6a7f681f8da345e5ae46ab`，原 pure reader 是 `8631ae6ba1b20480465b96d2c4b71c419253a736e24ecba9cae967d01cb955d2`。原 science 自然返回0，用时10456.962818394999秒；原 pure 自然返回0，用时348.8245757200002秒。两份完整小分卷分别保留439个实际science字段及19个原投影错误、423个实际pure字段及22个原投影错误。它们不是把错误删掉后的替代报告。

实际完整原报告为51908815 B，SHA-256 `53af35f6e91a6d4021d40fcf7b5a091fa74fd9d49b645b9c5c89c2f2d47cb1fa`；完整原命令为50753 B，SHA-256 `9eb6d59cd611a58e244eb5c4de132c38bbd35dadcf7369fe41a336c94b5ccbcf`。两者都在原 runner 的 `fixed-fejer-paired-halfwave-demanded-bhalf-first` 输出邻域。此处没有读取大 raw，也不把原自由词或NPZ搬入Git。

原物理模型为 `61c6542b3cfe39dea9fbf8c002c8ea204f5dad193ddaffe94bc7c908822682d7`，final point 为 `a28ae9998fb54207f0ccccd1a9abdf0e89beff1025f5e01334b856b21d3da3cf`，完整13成员final的SHA-256为 `25d9e9a7868e51d0e96509ee61606fdb068ef58fd63513b1fe294c380b3317fb`。原typed记录共13条，完整数组SHA-256为 `b0f7d5a2346b27ada6e6619877da8d2c3ad05ab1f6345dfd00405356d3f86ed3`。这些是实际旧身份，绝不改名为新报告身份。

原段接受4个restoration、0个metric方向。final Phi为681.6450227773521，Gram为0.40616533555531326，有限几何g为0.5225620087197518，仍不可行。原首恢复QP完整pure返出 dependent_blocker_at_zero_step、2 advances、face Pg=0.529460169023458、容差5.305849371949155e-7。本包只据原明确阻挡状态调用已经另立的R729算法；没有据首方向结论猜测所有旧方向的阻挡行、乘子或alpha。

完整旧证据：

- `topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46108296054-1-part-001.md`，54607 B，cc7459afedbf3343c6f3c0e94cc608379a2ebfbd042408f729adcbfa87e55340，blob cf58c9ce632ef210c5351dbfdcc997f49bbe9e8c，固定提交 48ce66d0585eacc472027355e9674100aebb41a5，第三个完整JSON。
- `topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46108296054-1-part-002.md`，32987 B，208937df3fc07468949757e57960eca6f3549f9c40ebd0670b623eb3a0db8017，blob 68a8ad5d6c64d0ed835f3b1bb74c8694f44b6773，固定提交 62de25c019a922ec661de5da59f5fbd9b69d0087，唯一完整JSON。

## 2. 新入口与原入口的边界

新namespace是 `fixed-fejer-halfwave-demanded-run28-R729-continuation-01`，仍接原active ID `visible-larger-resume-20261128-28`。本包不产生新workflow，不改原parent_request_id，不重建reference或maker输入。它使用原28同runner的同一套reference、observations、node/scalar、preparation、locations及完整binding文件。

原same-source恢复分支要求报告schema、driver源码、complete、完整final、模型、固定标量和carrier全部相符。该分支的整个772字符块原字保留，新driver的全部function正文与第33组R729 driver原字相同。不会把28报告source/schema改成R729，也不会调用原same-source入口假装通过其源码守卫。

实际采用已有明确CLI：`--material-envelope-parent-report`、`--material-envelope-seed-report`、`--material-envelope-seed-checkpoint`。新完整transfer增加一个准确28父族和一个整物理模型相等分支；原历史父族、原完整历史walker、原same-source restore与原模型关系函数都保留。当前138个科学角色相对原137只有行政 `envelope_transfer` 换为新完整文件，另增加原已锁R729 kernel；其余136个当前原角色逐对不变。原137对全部仍作为原driver的完整独立来源表真实读取。不能把这个计数写成“当前全部原137对原样”，也不把行政source替换说成物理方程变化。

新当前21个runtime包括原完整科学构造、三个新upper、一个新transfer、共享R729核及原33的独立pure frame reader helper。pure-only helper不冒科学SOURCE_PINS角色。若它尚未被33发布，发布本入口时必须同时材料化该完整共享文件。完整记录见本包binding；不存在依赖未明未来源码的运行许可。

## 3. 同一个物理场的完整根据

这里不是从两个运行数值相等推物理相同。新transfer先按原28完整driver whole SHA读取其完整SOURCE_PINS，并确认恰137个原角色。每一原路径的完整bytes都真实读取并核SHA；当前136个非transfer原pair必须逐一等于原pair，额外solver pair必须精确等于R729已锁核。

原28 source-bound reader完整验证原报告、原normal、完整base、固定reference、标量图、seed、Q、所有working政策及原源闭包。随后原完整analytic model validator验证当前模型，并要求 **old representation == current q.model**，且整对象canonical SHA为原真实61c6542…。没有剥schema、source、policy、target、模型字段或数值词后再比较。

因此所有物理构造与表达都不变：M160、J923、N2048、1333370个自由变量、全部原三个omega块与完整core/H、旧S5端层和R724正负半波、全部32法向阶段、真实六jet lift、完整固定Q、固定标量与Fejér图均沿原完整数学源。R728反号、R725新cutoff、R726 Slerp、adaptive恢复阻尼均未混入。R729只在原恢复QP返回后选择候选方向，它不定义新的q.model或新的g。

新模型关系record中的源码记录使用**relative path、完整bytes、SHA**，所以后继pure可以从自己的完整checkout核同whole文件。每次仍实际读取完整当前副本，并末次重核原source文件；不会把某次科学checkout绝对路径误当跨checkout模型等号。原报告、命令、checkpoint与历史输入的真实绝对路径保留在各自actual file record，按原路径逐字复读，没有将其改指新文件。

## 4. 全变量、13成员与原typed责任

原已有 `seed_from_complete_prior_final` 数值读回主体保留。它先要求原完整pure以verify_final_bundle=True读原final；要求原report complete、final statistics存在、final geometry complete。并不要求旧场可行，因此真实未通过几何的旧final可作为明确的新数值起点。

NPZ必须恰好保留13个成员：schema、omega_jets、core、Hcap、mesh、fixed_parent_core、zero_closure_model_json、zero_closure_model_identity_sha256、base_so3_model_identity_sha256、fixed_scalar_metric_identity_sha256、endpoint_root_policy_json、working_integration_order、working_full_angles。额外或缺少成员都不自动补齐。

五个物理数组必须有原finite float64 dtype、全部实际shape；mesh、固定parent core及前三固定core词逐字相同。由完整core自由段、全部omega自由行和H重建完整自由向量，再用原q.unpack重构全部core/omega/H并逐字比较。最终point必须同时等于原final geometry与latest operator point。冻结reference/base.initial不改变，固定initial seed不会改成旧final。

原load_memory完整函数继续读取所有inbound histories，保全三类显式role数组、implicit radial/angle grid、全部protected地址与原typed完整顺序。旧13条typed的原记录原样放在complete_original_typed_rows中；当前新typed记录只附加已有source-bound origin，不继承旧数值、J、root或证书。旧首次发现point、原driver/model、source row ordinal、type各分量全部保留。完整初始typed前缀仍须是新末尾memory的不变前缀，不能evict、截数或伪造未返peer顺序。

原五组pending CLI从**新调用**移除，是原strict-final模式与independent模式互斥的实际接口要求。其完整实际run/source对应表仍在旧完整报告的independent origin与inherited transfer中逐字保留；新binding另以整文件和精确JSON pointer保全33完整外部peer记录。没有因未传五组独立模式CLI就把未返历史置空。

## 5. 完整参数与实际最后阻尼

原launcher写出的50753 B完整命令是本次实际输入，按whole SHA强核。它记录展开后的全部CLI参数，包括没有在157词上显式出现的默认项。新launcher同样写完整展开命令。新transfer核其driver whole SHA、原run ID、当前实际parsed namespace与完整命令一致，并逐完整参数map比较新旧数值、domain、预算及普通输入。

唯一允许的普通参数差别为source checkout、fresh outdir、明确final父/seed模式与原pending声明的归属变化。仓库中的literal moment input路径随checkout变化，但必须通过各自actual_input_record的完整bytes/SHA比较。其余实际输入路径原字保留。所有原预算仍为metric方向1/每方向16、restoration方向4/每方向64、line trials15、原192行、完整近活动/envelope、全部quad/root/normal与精度参数。本包不把旧已经用完的4个方向写成还有余额；这是从真实final开始的**新完整预算**。

两个下一初始阻尼直接由旧完整报告的 `final_damping` 与 `final_restoration_damping` 分别读取，要求有限且严格正。旧CLI两个.01词和新CLI两个.01词都保留在完整actual command，并与原参数核同；真正进入新report/外循环之前，赋成各自实际最后状态。这样既不会把未投影的restoration final当默认，也不会把最后metric阻尼误用为restoration阻尼。

公开旧pure只投影了final metric mu=.01。此准备没有为未投影的旧final restoration填值；该字段在新绑定的actual future中仍null。真实source直接读取原whole report，随后pure从完整parent command/report再核两种实际值，并要求新报告initial_damping/restoration_damping分别相等。当前新source还没实际开始，不能称该读取已经成功。

## 6. 新数值流程与报告含义

全变量复制后，原driver继续完整构造weights、norm、geometry screen和packet recorder，并从新source真正调用原完整residual、statistics和geometry。没有载入旧normal root cache、旧J、旧field rows或旧accepted数。新accepted起始0，旧4个接受只作原parent证据。

R729原核2dfe85c4…保持原字。原QP先运行并保完整report；只对两个明确dependent_blocker恢复状态尝试全行dual CCD。每行正beta、全部物理列、原mu²与slack二次项、原剩余64减advances的完整sweep单位、原C最后读回和完整失败/旧候选/零步规则均保。原face Pg与原step norm继续只描述原QP；新方向、全行余量、gap、stationarity与采用来源独立读数。有限CCD不冒准确KKT，不改变外层真实line search/完整六族/接受。

若任何旧真实文件缺失或改变、完整13成员不合、旧或新源不符、参数map不同、模型对象不同、final阻尼缺失或typed责任不全，则此明确输入关系失败，不能降级为独立reference初点或只复制部分变量。失败保原信息，不合成checkpoint或future typed。

## 7. 完整运行步骤与容量

科学ready保全部原575 formal，再加12个真实续接归因投影，总587；原64个live全部保。完整argv为142词：原157中去独立标记与五对pending run/source共21词，再加3对明确final参数共6词。纯读为原7词、原564 formal再加4个归因投影，总568。所有output、cleanup与完整原step其它字段保留。

单science队列对象为74381 B，单pure为63168 B；均小于95000 B。两步不需强塞同一队列，只有原science真实自然返回后再按根的实际流程接pure。父request仍是visible-larger-resume-20261128-28；本包未操作任何queue/ref。

四新运行体共311363 B；加完整binding和两ready为524909 B。完整文件分别为：

- `topics/visible-flex-larger-amplitude/scripts/resume_20261126/run28_R729_transfer.py`：94589 B / 72846bb85fbaddb92741ce83910afd24b3d664ac6256ac24a5b5037df48db266 / blob 7a0fa509f7c4481ee2e9b020f634648e91d50bb5
- `topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_run28_R729_qp.py`：99916 B / 7599dda1a80450556f152d261479e70bc48599d4b8e20950919bb896ea89e186 / blob 7db95b4f7c431829d50836e9b78c8778d70ef145
- `topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_run28_R729_report.py`：94515 B / b26d3391aa21a6154f2afcd8aff7f9035f780f7262840814ebc89ed74dd6cb26 / blob 23046b928fd4906370d44e5f8836037163a21437
- `topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_run28_R729_actions.py`：22343 B / a0f1cbca2a5734963a189d8493fd1e04d633d96f397c0af2b17c7f588812450b / blob 5ee54a225a3c5bd7dea80422648d5c12fb632fb0

- binding：`topics/visible-flex-larger-amplitude/computations/run28-R729-explicit-final-complete-binding.json`，71091 B / b7919829e4212559fe1f58a7f5294c47ad92a1aba342acd818c8aa2e49d39fb2 / blob bb88b878ca200cae040beb8eff64a72766785a1a。
- science：`topics/visible-flex-larger-amplitude/computations/run28-R729-explicit-final-science-complete-ready.json`，76837 B / 579e76a6fd5c5e933beaef2e8eda28ea70038ba279bd6a9a0d60af2f9009512f / blob 81ad741c498e6e9c157e5d0e2fde8d96070482f0。
- pure：`topics/visible-flex-larger-amplitude/computations/run28-R729-explicit-final-pure-complete-ready.json`，65618 B / 13084996b64d7e6e823249fa006e3c3a598f08cb7dd55191a20f34621bbbadb0 / blob 87ebbd2d920e5f0113f5701c63e1db903288d3b9。

## 8. 整文件再生和当前未付范围

配套MJS仅作文本读取、完整SHA核验、唯一位置patch和整逆回原父；不import Python、Torch、NumPy，不做AST、fixture、benchmark或科学实验。输入是完整旧transfer、33三upper、完整当前binding定义及33两完整ready。原33完整source delivery与参数所有metadata保whole记录和精确pointer，不复制或裁切祖先历史。

再生器重建四完整运行体、复制完整当前binding定义，并从整父step生成两整新ready。所有源/ready输出必须逐whole SHA与终锁相同，单件小于100KB。该可选文字恢复能力不是新科学前置步骤，也不是要求用户先通过独立审查。

当前发布commit、实际新source commit、读取成功、两有效初mu、R729触发/采用、新初值、新几何、新typed与完整final全部未返回。即使同一数学模型、同一全变量词，数值求根和求积仍须由本次真实计算给出；没有从旧数值相同或原完成状态宣新完成。原28的不可行结论与原33独立初点运行继续各自保留。

## 2026-11-28 09:19:13 UTC — 已观察控制器路径拒绝及完整队列修正

初次完整发布bc3c666d081fcc8213910c3cc0eb92d7367e44a6的science step.script漏了课题目录前缀。原28控制器在09:13:43Z、科学进程开始前返回原文：`Followup queue: Step script must be a Python file inside the declared topic`；仍只有既存6个已完成阶段，没有第7阶段scientific source/PID/新model或新结果可宣称。

完整公开索引固定f020f0a86ce3bce9d15f3cc1ab10edf45f3b2c13，路径topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46108296054-1.md，34763B/SHA25672ee2484c27d7db0da841ad9d66984ae7aa31b01735d177273205c50f0ef53fd/Git blobe928f61c9d2356507d2fdb9d4baba29151bcae7c，保全部原请求/六阶段与错误。完整原helper scripts/resume_20261126/public_actions_followups_with_geometry_location_progress.py 为32763B/SHA256444f57b28c695fbcd0fbfc03237b8c7a56dedccc97a64873b7dae083de5dbb12/blob4b72d0565d3f3fd797dd8bf45e48310cad8226d2，既有规则要求script以topics/visible-flex-larger-amplitude/起首并位于课题内。守卫未改。

此次只把science完整script改为topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_run28_R729_actions.py；其余142个参数词、587正式/64live、完整scope/parent/outputs/cleanup/cache与finishfalse全部保。新整个队列74418B/SHA256065274258571ceb8821556880ad9cafe7905b8c1f699c7b15d67c5681df416fb/blobe48dbad5b0be71cfdf98285e66ab1d0a5e852e2d，原错误队列74381B/SHA2563d161b59f79d1c650d462fea4021c5b615f4d0f321563a9ccd38820657c7518d/blobc22ab7f3362261d76b19a1b6f8eecf06ac74ce15在bc3c完整保。原ID/step ID保持，因原queue整体拒绝未记为实际科学attempt。

下一whole pure对应script同样加完整前缀，63205B/SHA256477e7a1ed6ee1b78ec69634955df168e28f3d91f977c1c369d265f0b03ccb1ed；完整7参数词/568字段全保，仍只在真实science自然返回后排。源代码和计算预算完全不变。参数ready/binding/再生器/交付表的相同修正由完整后继表续记，旧版本作为实际错误父保留，未把修复声明冒新运行成功。

## 9. 2026-11-28 完整参数与文字恢复的路径修正终表

上面 §1–8 是首次准备时的原记录，连同根于 09:19:13 UTC 追加的实际拒绝与队列修复全文，均逐字保留。其旧参数文件身份、原队列字节数和当时未出版标签仅作为该时点历史；本节给出修后当前完整参数出处，不将控制器拒绝记作科学计算失败。

原四运行体和共享纯读 helper 已由 bc3c666d081fcc8213910c3cc0eb92d7367e44a6 出版，字节完全不变。根在 f891be9b43ae881d26a1c3dbe2e836aff00406d2 只为两队列补上课题前缀；本次把同一修正贯穿 ready、binding、完整再生器与总表。两 step 的唯一变化是 `/steps/0/script` 新增 37 字节 `topics/visible-flex-larger-amplitude/`，没有修改 args、scope、outputs、cleanup、summary、progress_summary、step ID 或 parent ID。科学仍 142 词 / 587 formal / 64 live，纯读仍 7 词 / 568 formal。单步队列分别为 74418 B 与 63205 B，均保完整对象。

当前脚本路径为：

- science：`topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_run28_R729_actions.py`。
- pure：`topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_run28_R729_report.py`。

- binding：`topics/visible-flex-larger-amplitude/computations/run28-R729-explicit-final-complete-binding.json`，75204 B / SHA256 3849cd8710b4709ec8b5b2d80a81c6ee9d8e9213c460300c5859b7779d60be4c / Git blob a5daf1566e96b25298205e5e40728d9c2ddc2da5。
- science：`topics/visible-flex-larger-amplitude/computations/run28-R729-explicit-final-science-complete-ready.json`，77280 B / SHA256 bb652ea758fe707441ff1e73b7d40c6c26d75a226e5c036c92cdc30cf1da7e63 / Git blob be2b245fecd32b45d29fc65f32a2f063120e7114。
- pure：`topics/visible-flex-larger-amplitude/computations/run28-R729-explicit-final-pure-complete-ready.json`，66061 B / SHA256 2070ca359113c779263c69b41ef507cff5c18407cd5fa11eddbc22f0736ab2cf / Git blob 2514e788f5e971bdfc00b5147e24e9ec738128a1。
- 完整文字再生器：`topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_run28_R729_explicit_final_continuation.mjs`，34667 B / SHA256 fb166954b4069bd7f49952fb0bc2839775aeaed13b2269e30f06ac44ea13cef6 / Git blob c3eaa4b8ce62d8d3e3aa746dfe2f45b7f275af07。

新的 binding `/post_publication_script_path_correction` 全部保留原 10 件交付总表、旧 binding、两原 ready、旧再生器与说明的准确 whole 记录，连同正式出版提交、原守卫身份、完整已观察错误 note 和根的真实队列修复提交。新 ready 以 whole record + JSON pointer 引用该记录；没有裁掉旧参数或 peer 责任。新再生器在相同四完整父源和完整 33 参数上采用这一精确脚本路径，四运行体整段补丁原样。

已完整读 33 的 science blob 8631722f6367d98f4515adce383f49226f69c3cd 和 pure blob 86116e5b0605b3fc5d24cf8b998695bf65939401：其 `/steps/0/script` 原本已有完整 topic 前缀，因此 33 不需要这项修正，原 157/7 词不动。R730 后续计划也将采用完整 repo 相对路径。这是对已发生接口错误的直接修复，没有更改控制器守卫，没有新增数值、AST、fixture、benchmark 或审核前门；修后科学启动、父场读取和新结果仍须等真实 Actions 返回。
