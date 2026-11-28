# 22：完整成对半波、半宽基线的真实启动与续求

## RET84：终态导读与完整历史记录

**已知终态：** run 46090913581/1 的 job 在 2026-11-28 06:51:08Z 为 completed/cancelled，原因未知。两必要输入确已返回 0，科学没有观察到自然返回；最后 current 接受数为 3，下一 480be 的几何、接受和最终 report/final/typed 未知。末节保留官方对象和最后观察各自的完整历史定位。

本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。21 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。

**完整旧文件：** 65324 字节；SHA256 `ca64e480a1b6e20c00e600e678b114bc39e0e1132e9b8a49e52c091023ba1d61`；Git blob `d7a63157e3614ba573ce6b1fe638b7962306d68f`；固定提交 `a7ee59c79535235b4161da7780b77556e9760940`。[完整旧版](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md)。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET84 完整交付表](../computations/terminal-run19-24-narrative-retention-84-complete-delivery.json)。

下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。

2026-11-28 UTC；Astra-larger-e4e2a2bf-20261126。当前是完整启动包：真正run号、job、来源commit、输入返回和新场均须等公开Actions真实事件后另记。本文件不把准备当执行。

## 1. 科学选择与全部预算

完整19数值基线 b/S=1/2、delta=1/32、metric/restoration damping均.01，M160/J923/N2048/P7377、32法向阶段、全自由变量、根和回溯、QP、全角/径向/几何域全部保。新来源实现R724的成对半波：两个等长中央分别+h_delta(t/2)、−h_delta(t/2)。它有相同准确跨段均值及两角根方程，中央切向导数减半，但中间区域出现真实位移；whole Gram、D、主曲率与reach不能由这个局部结论填入。

21原五分之八初reach违反2.541916739245917，比19半宽.9684249942095058差，distance-plus则转负；完整原实测已分别刊各note。故本分支保19半宽以单独比较半波机制。早期5/8准备只是历史，未执行为22；恢复自适应阻尼与geometry-first都不混入本轮。

两个完整必要input构造器先在同runner重新生成固定g与全部参考输入，随后157词科学整步。原角2048、stage-block64、angle-block8、integration8、seed radial8/profile16；endpoint root24迭代/18backtracks、seed mean128/24及scalar64；metric方向1/QP16，restoration方向4/QP64，line-trials15、active192、near-active32，QP0/1e−6与metric目标1e−9全保。完整每一argv、selector和输出以已刊whole ready为准，下面表只是索引。

| 步骤 | 原字参数词 | 完整正式投影 | 接入条件 |
|---|---:|---:|---|
| 必要固定输入 | 6 | 14 | 新runner自身重建 |
| 完整参考 | 26 | 62 | 前步真实返回 |
| 新半波科学 | 157 | 458 | 两完整input真实返回 |
| 新半波pure | 7 | 445 | 科学真实自然返回后整步接 |

原48个live投影、清理仅已返child新生成rows-*缓存的完整范围、保同场reference cache规则都原样。全science+pure最小完整队列110351B，超过原95000B限额；初三步完整63721B，不裁字段挤入。pure完整准备已刊，只有真正返回才退休已返项并接入，队列钟和平台钟都不是数学完成。

## 2. 完整来源与参数

全部20新源、137科学角色/18runtime与三个完整源码再生器已刊于7d34ebe278826c68a9e84c32179251220bf2fc3b。相对完整19/21当前父，17对实际替换、120对原样；这个120不是此前某个历史original120的全不变断言。原source paths/whole SHA全部保。完整seed物理与Q/binder严格新模型，不从旧identity去掉不同字段后冒同场。

完整六参数件已刊于637fc22a3d9b67f62d9fd3546028d443ec869b98：[全参数总表](../computations/fixed-fejer-paired-halfwave-bhalf-complete-parameter-delivery.json)，合279148B。三ready/display与再生器/说明/总表完整，不以本文摘要替代参数。两个大历史metadata只用精确whole父+JSON pointer共享，原字段和所有旧值可完整恢复；旧源码构造器保持原历史义，不冒新家族生成器。

当前driver 095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec，launcher6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c，pure be9bb58fa612fc25ab01458a2d6e21e0fa10c7573dad37e65effb845c6e29e92；完整137对与每个整文件bytes/blob保[当前绑定](../computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json)。

## 3. 原历史、peer与新场边界

原五组受支持peer CLI逐词保留。原六external职责与真实19/20/21另外三组完整保，后三仍是其真实10fa来源，不塞入新PARENT_FAMILIES，也不改成095b。已有P0/G/typed discovery顺序、失败和unknown完整保；任何旧live或accepted点不作跨runner raw。12–17官方取消和未自然返回是分开的事实，不能造全final或空typed历史。

请求完整保全部原19顶层字段；对改变的当前字段，明确指向27133B原19whole request及准确JSON pointer，其他原字段仍inline。原workflow/controller谱系也完整保；当前控制器仅21→22槽名和索引日期2026-11-28，35原pins、同步/pull/rebase、预算及全部原执行流不改。当前工作流只新请求路径触发，独立concurrency，不取消旧runner。

## 4. 原始数据与README同步

科学只在本公开仓库Actions。完整raw、参考数组、snapshot、accepted/final、root packet、per-cell费用和mesh只在runner/scratch；不写Git/Release/artifact，不换名字跨run迁移。保完整源/配方/真实run与whole输出SHA。当前2input和新全场都必须真实返回自身身份。

350分钟工作流与20000秒controller checkpoint保原；活科学child继续按原流观察至自然返回，时长不是允许根代理停止研究的理由。每次真实pull比较两个README的diff，变更立即执行，已读commit写独立HANDOFF槽。root当前本地执行环境仍不可用，云端metadata确认不冒本地pull；各活controller真实pull继续。非快进或并发拒绝按当前可用机制鲜HEAD普通整合重推，不force覆盖。

## 5. 完整未付数学责任

准确费用链必须用新物理六片：每中央t/2、相反符号、全切点进入准确全域径向划分，跨段横向均值抵消不冒单段积分为零。辅助A仍原f848十二片。seed计划含cuts不表示原working whole-cell八Gauss及partial积分自动分片；working误差继续未付。

全部32stage/六jet/连续branch/全角1024胞/922径向加cuts/完整无限尾、R722域三残差和误差传播，以及Gram、上/下帽、mixed/allphase、R723五角色、R718 marked sigma、R716无标记管/正V/非零中心不变量必须同一新场真正完成。normal.complete不替连续分支，mean J不替Cu，旧R709 bool保真。immutable required-angle packet可为trial，但mutable progress不可作准确输入，全13final才满足same-source restart原合同。

全t闭连通C²嵌入/强C²连续、固定有内点H且diamH≥.2D、整像δhold≥.2D、含反射δE>0、reach≥.03D、整面relative metric≤1e−6仍全部未证。之后必须冻结同g/参数/t范围做真实网格、频率、时间加密至机器或原容差，输出多个各<5MB完整mesh的可复现源码及真实身份，说明严格存在缺口并继续增强比例。本次完整启动不是完成标准。

## 6. 完整启动对象身份

下面每条为实际完整对象；都已保护原bytes，不含令牌。真正发布commit与Actions状态随后根据实际事件追加。

> **原 JSON 01：完整启动对象身份。** [固定旧版完整记录，第 54–99 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L54-L99)。


## 2026-11-28 01:03:47 UTC — 官方22实际启动

公开run[46090913581/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46090913581)已于2026-11-28T01:00:48Z启动，event=push、head=18081452c5181d958bb5432c4045c067bf1d1caa；官方in_progress。job140811337445的checkout/setup/dependencies已真success，原研究步骤in_progress。下面保完整返回的job对象；此时没有读取22的新科学输入返回、模型、point、六g、接受或完整report，全部保持未知。单是job开始不证输入成功或数学进步。

原完整源/参数/请求/queue已经同提交或其祖先刊出；继续按两实际input、science真实返回、完整pure与全部准确费用的原条件接续。

> **原 JSON 02：首次官方 run。** [固定旧版完整记录，第 107–124 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L107-L124)。


> **原 JSON 03：首次官方 jobs。** [固定旧版完整记录，第 126–183 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L126-L183)。


## 2026-11-28 01:17:44 UTC — 22两个完整输入与初统计实际返回

真实run46090913581/1的两个完整输入步骤均completed/exit0：输入构造耗时5.928990263999992s，source89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60，实际commit0bfb66f595ebff65a2abf59143b93c4921f0231f；完整参考耗时481.429137124s（内部478.64331817s），sourcee7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb，实际commit3ecc2f9b472810c298b2f066637520eb4ff1b8fb。完整M160/J923/P7377/N2048、2218叶和height1.947054437068418；accuracy_reached=false、whole_tail=true，未冒精化或几何证书。完整原command/全部指标/输入与11输出/cleanup/缺项保下列固定Git原卷两个全JSON块，未以摘要替换原记录。

> **原 JSON 04：两个必要输入的完整实际记录与原分卷。** [固定旧版完整记录，第 189–274 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L189-L274)。


同一新半波science实际sourcecommit c6517a030888df2bf0ca51efade67b7693102785，launcher6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c/PID3541；完整driver095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec。新model6f3ae32a19723a91d36aa9d1157838b6977b8099bf2de178458c102f726c96ef，旧坐标身份7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47并不表示旧物理场。

01:12:40.949868初统计真实返回Phi681.6517423825409、Gram0.40616525311769985，accepted0/reportfalse。观察至01:15:12Z，初始/当前几何、六族、试步及final均未返回；相应None读取错误是字段尚无值，不补值、不当科学失败。法向进度513角根/closure failures0只是当前只读进度。继续完整几何及原预算科学步骤。

以下固定完整小索引身份与原active全对象只保原已返标量；缺值/错误原样，未取科学raw或另算场。

> **原 JSON 05：完整索引身份。** [固定旧版完整记录，第 282–290 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L282-L290)。


> **原 JSON 06：完整只读进度观察。** [固定旧版完整记录，第 292–474 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L292-L474)。


## 2026-11-28 01:28:06 UTC — 22初始完整六族几何实际返回

run46090913581/1的原science c6517a030888df2bf0ca51efade67b7693102785/launcher6fd57/PID3541、driver095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec和新半波model6f3ae32a19723a91d36aa9d1157838b6977b8099bf2de178458c102f726c96ef保持。初完整几何进度事件在01:22:55 UTC已返；01:24:50.545031的current-geometry-returned以及01:25:18Z完整小观察均绑定初7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47。initial/current_geometry_complete=true。

六族真实值：reach0.5305849371949052，body_diameter−0.03813552733778258，distance_plus0.11391238912344381，distance_minus−3.0936337267043594，cap_diameter−0.06715131487906445，height_floor−1.0411715967426867；最大正违反0.5305849371949052。Phi681.6517423825409/Gram.40616525311769985、accepted0保持。reach及distance_plus仍正，故该初值不满足有限工作约束，更不构成连续reach/嵌入/1e−6的完成证书。其余四族负不能替代未付连续费用。

与19同固定target/数值参数/初坐标下的原全波model0abfbf真实初值g.9684249942095058、distance_plus.005863061771032241、Phi3825.0583894874153/Gram.6460503011117507相比，半波初值的最大违反、Phi、Gram较小，distance_plus较大。这是两次真实初场工作数值的比较，不是R724自动推出的wholeK/reach/直径单调定理；两source/model不同，当前点SHA相同不能冒同物理场。原19完整初观测保其同名note。

此刻没有任何trial/accepted direction；latest/last trial读取None的原错误保留。完整子进程未自然返回、reportfalse，正继续原完整恢复与度量预算。没有改seed、参数、目标或运行中的源。

队列计数注：保持22完整原step值，仅按compact UTF-8 JSON+LF计数，原63721B三步，science+pure两步103752B，全四步110351B。原request同名minimal字段110351实际是四步计数；旧字节不改不重触发。两种包含pure的完整队列均>95000，因此自然返回后整接pure的责任不变。

以下固定完整小索引身份与原active全对象只保原已返标量；缺值/错误原样，未取科学raw或另算场。

> **原 JSON 07：完整索引身份。** [固定旧版完整记录，第 490–498 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L490-L498)。


> **原 JSON 08：完整只读进度观察。** [固定旧版完整记录，第 500–634 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L500-L634)。


## 2026-11-28 02:00:28 UTC — 22首个观测试点统计返回，几何与接受仍未知

同一真实科学子进程 c6517a030888df2bf0ca51efade67b7693102785 / launcher 6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c / PID3541，driver095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec，model6f3ae32a19723a91d36aa9d1157838b6977b8099bf2de178458c102f726c96ef。首观测试点97fbb982b31c713cc71b8cb0d44f255127380185bcfb68be53e29dd19d9b579c在2026-11-28T01:43:47.960927+00:00实际返回Phi681.6511710299278及max_relative_gram0.4061652579029476。截至原索引01:50:33Z，trial geometry、trial_accepted与last_completed_trial均未返，原缺值TypeError照实保完整索引；不得从统计下降推接受。current仍初7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47、Phi681.6517423825409、Gram.40616525311769985、g.5305849371949052、accepted0；原六族不变，complete_report=false、child_exit_code=null。normal进度01:50:31仍在该试点、cached_angle_roots513/closure_original_returns29014/logical_failures0；这些计数不付准确费用或连续根存在。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 09：原完整索引/分卷身份。** [固定旧版完整记录，第 642–653 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L642-L653)。


## 2026-11-28 03:09:55 UTC — 22首个试点真实接受并返回完整六族

原先仅统计的97fbb982b31c713cc71b8cb0d44f255127380185bcfb68be53e29dd19d9b579c现在真实成为current/accepted，accepted_directions=1。同sciencec6517a030888df2bf0ca51efade67b7693102785/launcher6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c/PID3541、driver095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec、model6f3ae32a19723a91d36aa9d1157838b6977b8099bf2de178458c102f726c96ef，无源/模型/点身份替换。数学current-geometry-returned事件2026-11-28T02:36:24.158961+00:00，原索引观察2026-11-28T02:41:05Z；该时间是已有数学事件，不冒精确接受时刻或child退出。

Phi=681.6511710299278、max_relative_Gram=0.4061652579029476。六族全返：reach=0.5294703284893127，body_diameter=-0.038135649309102404，distance_plus=0.11391376026366629，distance_minus=-3.0936337267606984，cap_diameter=-0.06715135970511843，height_floor=-1.0411715403912758。初reach0.5305849371949052至0.5294703284893127仍正，distance_plus0.11391238912344381至0.11391376026366629仍正且略增；不能用reach工作量下降宣完整可行。原Phi/Gram和六族初值保前文。alpha、完整线性预测、方向编号、完整typed history未返，不反推。

当前trial与last_completed_trial均为同97fbb原点，trial_accepted=true，original positive maximum family为reach；complete_report=false、child_exit_code=null、child_natural_return_not_observed=true，观察错误数组为空。normal原scope_closed记录1441角缓存、51711返回、逻辑失败0只是有限工作进度。没有完整report/final/packet或连续branch/几何证书可交后续。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 10：原完整索引/分卷身份。** [固定旧版完整记录，第 665–676 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L665-L676)。


## 2026-11-28 03:46:50 UTC — 22下一完整试步统计实际返回

第22组下一trial e906e24a5de604e0ce480aff4aa2aa0617a098621e7358cea5dcc100f26312d8在03:16:43.074825+00:00返Phi681.6473711639321/Gram.40616528955370923；03:41:38索引仍无该trial几何/接受。current97fbb/accepted1与其原六族不变。原三个NoneType缺字段保，不填0，不以统计改称接受。report=false，source c6517a、driver095bf、model6f3ae32保。

> **原 JSON 11：试点真实数学标量。** [固定旧版完整记录，第 682–724 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L682-L724)。


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 12：原完整索引/分卷身份。** [固定旧版完整记录，第 728–739 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L728-L739)。


## 2026-11-28 05:05:41 UTC — 22第二个恢复步实际接受

当前e906e24a5de604e0ce480aff4aa2aa0617a098621e7358cea5dcc100f26312d8真实accepted2，Phi681.6473711639321/Gram.40616528955370923；reachg.5237169415657044，distanceplus.11392286053783374，均仍正。下一b34824acd5f82b1540ff7c582fc0319b3311974e9e8860845f9c0d26d084846d已返Phi681.6470516175362/Gram.40616529581758637，未返几何/接受。与25部分标量相同不能替换独立完整点和运行。

完整原观察含实际source/PID/driver/model/target/initial/current/trial、全部六物理族、原normal进度和每一观察错误如下。工作几何complete仅指该有限步骤；没有whole准确界或README完成。完整全量report与child自然返回仍未观察。

> **原 JSON 13：完整只读进度观察。** [固定旧版完整记录，第 747–841 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L747-L841)。


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 14：原完整索引/分卷身份。** [固定旧版完整记录，第 845–856 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L845-L856)。


## 2026-11-28 06:00:39 UTC — 22第三个完整恢复步实际接受

05:38:09.646582Z，b34824acd5f82b1540ff7c582fc0319b3311974e9e8860845f9c0d26d084846d真实accepted3，Phi681.6470516175362/Gram.40616529581758637，reachg.5235597907246015、distance_plus .11392305204890485仍正。全六族如下；同25某组标量相等不把不同point/source当同一证据。至05:42:57完整report/自然退出未返。

> **原 JSON 15：第三接受点真实数学标量及六族。** [固定旧版完整记录，第 862–907 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L862-L907)。


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 16：原完整索引/分卷身份。** [固定旧版完整记录，第 911–922 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L911-L922)。


## 2026-11-28 06:30:01 UTC — 22下一试点480be的自身统计返回

试点480be58574d985b3f714bc2567d92adcf3e7b46366248d1722c9665afd814938的自身统计为Phi681.6450227773521、Gram.40616533555531326。当前仍b34824/accepted3；该trial的几何与接受未返。即使这两个标量与25原终点相同，也不能把25的点、g、接受或报告转移到此点；原alpha/方向号未投影，仍未知。

> **原 JSON 17：下一试点自身的实际观察。** [固定旧版完整记录，第 928–950 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L928-L950)。


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 18：原完整索引/分卷身份。** [固定旧版完整记录，第 954–965 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L954-L965)。


## 2026-11-28 07:05:57 UTC — 22官方取消及完整末次观察；真实运行边界保留

官方 jobs 原响应现为 `completed/cancelled`：run46090913581/attempt1、job140811337445，从01:00:50Z至06:51:08Z；research step 在06:51:03Z为cancelled。取消原因未返回，不能由350分钟预算或墙钟推断。最后完整控制器观察仍是06:48:45Z、科学子进程尚未自然返回；两必要输入0不等于科学完成。当前 accepted3 的 b34824、Phi681.6470516175362、Gram.40616529581758637、reach g.5235597907246015及distance_plus .11392305204890485仍不可行。480be试点只有自身Phi681.6450227773521/Gram.40616533555531326，自己的几何、接受结果、最终report/final/typed未知；不得借25的相同两数补本run。

原完整pure准备46723B继续保留，但本次没有观察到自然科学返回，故不把它标成已执行、也不向已终态runner假排新步骤。新的输入方向继续31完整R728反号构造，原22所有失败和未知保留。

### 官方完整jobs对象

> **原 JSON 19：官方取消 jobs 全对象。** [固定旧版完整记录，第 975–1073 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L975-L1073)。


### 完整末次只读观察（不是final）

> **原 JSON 20：最后完整只读观察。** [固定旧版完整记录，第 1077–1171 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L1077-L1171)。


### 移出活动区的原规则同步槽

<!-- visible-larger-parallel-22:start -->
Actions22：[run 46090913581/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46090913581)；[全阶段记录](notes/2026-11-28-public-actions-46090913581-1.md)。running；已返2，exit=未返。
并行22规则核查：2026-11-28 06:48:47 UTC，真实pull至`9b0b665ccf080e7528ad9d711ab0344b29c15082`，双README无变化。
<!-- visible-larger-parallel-22:end -->

06:47实际执行环境重置后唯一终端探测失败（No usable execution environment）；07:05收到新的environment context后再次实际探测仍失败（exec-server: No such file or directory）。这两次均没有git pull；root末真实pull仍eda95d51e82b126439d51d42185a880e6ddad3e9，当前按新HEAD云核双README及普通非强制整合，恢复终端即真pull。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 21：原完整索引/分卷身份。** [固定旧版完整记录，第 1184–1195 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-28-run22-complete-paired-halfwave-bhalf-launch-and-continuation.md#L1184-L1195)。

