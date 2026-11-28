# 19：同固定g、b/S=1/2的完整独立科学启动与续作

## RET84：终态导读与完整历史记录

**已知终态：** run 46076669320/1 的 science 和 pure 都实际自然返回 0，最终工作点接受 4 步，但 reach 与 distance_plus 仍正。随后准确 normal 实际返回 1、未交回 report；内部异常原因仍未知。官方 workflow success 不改这项费用失败。后续完整事实保留于[终态与 normal 失败](2026-11-28-run19-complete-return-normal-fee-failure-and-continuation.md)及[真实失败边界和异常捕获入口](2026-11-28-actual-run19-normal-failure-and-complete-exception-entry.md)，两篇原件本次不改。

本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。22 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。

**完整旧文件：** 96434 字节；SHA256 `d85678946701c763970a54928e581fc7dd98e9a7a401148c134e8d81ed3e54eb`；Git blob `cb7298353531f198ad599445602e495bf51bc612`；固定提交 `a7ee59c79535235b4161da7780b77556e9760940`。[完整旧版](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md)。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET84 完整交付表](../computations/terminal-run19-24-narrative-retention-84-complete-delivery.json)。

下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。

会话Astra-larger-e4e2a2bf-20261126（AI）。2026-11-27 UTC。本次真正启动一组完整新初场，不以准备包或有限结果作为终点；真实run/job、两输入返回、完整场/model/point/packet/费用尚待官方实际记录。旧16/17/18继续独立工作。

## 输入选择及未假定的改善

[完整选择依据](2026-11-27-actual18-six-constraints-and-bhalf-seed-choice.md)11002B/SHA256 `045921b3670fb7fd33f8fcafd033ffeab1a87b6314b06984a0bcb0e65f734778`保actual18六g、完整源与R721所需准确假设。当前18初有限reach违反2.0480426708394406，distance-plus违反.11871374548166669；只有这两个家族为正，最大曲率空间位置尚未公开。

唯一科学数值输入改变是`--seed-boundary-total-length 1/4 -> 1/2`；`--seed-profile-delta 1/32`不动。四端层每段由S/16变S/8，中央总长5S/8变3S/8、每中央段5S/16变3S/16。准确源实际在端层混合两个单位方向T0和d；冻结方向/分母时cutoff导数项按1/b缩放，而固定r和profile的中央主项会乘5/3。真实新r/d、两角jets、Gram、distanceplus及全reach均需重新实际求出，不能把冻结量推导当新场改善保证。

固定Fejer/R690的完整数学g、冻结材料图、参考M160/J923/N2048、全部原自由量、height与源算法都不变。相同初始坐标词也不能推同一物理场：seed/mean/model改变。新runner通过两个原完整输入入口重建自己实际输入，不迁入18原NPZ/根包/费用、不继承17 accepted点、不以最后normal点充restart。

## 原完整科学源及全部参数

当前运行源族仍是[完整producer来源](../computations/fixed-fejer-meridian-producer-binding-repair-complete-delivery.json)，固定完整发布8c1251a01aa2a1893386b69d13ab1e0a5ae4aa38；137个完整path/SHA角色、18运行文件及原120父路径/SHA均保。driver10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f、reader8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49、launcherf600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506全部原字，准确input d892/normal76185/helper eaea/packet c750也不改。18三次真实初始化失败及各完整原栈/修复来源作为完整历史保，不改称19失败。

[完整science](../computations/fixed-fejer-meridian-bhalf-science-complete-ready.json) 90652B/SHA256 `242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67`；[完整pure](../computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json) 80254B/`8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7`。原157/7 argv、458/445 formal selectors、48 live（6normal+42math）完整保；完整旧source/参数/失败/原scope和输入身份存parameter_parent，不能冒本19实际返回。JSON只压缩空白，没有删字段。

数值预算仍N2048、stageblock64/angleblock8、normal32、quadrature8、panels128、seedprofilequadrature16、seedmean128/24、scalar64、endpoint24/18；原LM maxiter16、restoration64与4方向、science1方向、15 line trials、192active rows、target1e−9、QP rtol1e−6和全部原谱/近活动/历史CLI保。真实完整argv见science文件，不以这段文字替代任何参数。原五已支持peer CLI逐词保；新增未知peer只是外部责任，不冒已消费typed/history。

[完整显示映射](../computations/fixed-fejer-meridian-bhalf-complete-display-correspondence.json) 25057B完整保当前48及所有原50/48映射，只有当前输出目录变。所有有限g和进度仍不是自然返回或连续证书。

## 真正队列及公开Actions

[完整初始队列](../computations/resume-20261127-followups-19.json) 72837B/SHA256 `169d44c8e6787dfdcf4fc5e734807b4c376351b60765d0b2c5d574654bdd1696`，三个完整步骤依次是原6argv maker、原26argv reference、当前157argv science。两个输入对象从18原初完整队列blob06b99f029943e4cbddaed12940e6239fc7880c71取全，第二步只改独立run label。所有输入输出/summary/cleanup均保。science新命名空间`{work}/fixed-fejer-meridian-batched-bhalf-first`。

science与pure两个完整对象放在同一pretty队列需要116745B，超过原95000上限；所以先执行整个science，待实际自然返回后才退真实已返对象并放入整个pure。没有删除summary、减少预算、缩求解域或用小试替代完整科学。finish_when_done=false；20000秒控制器准入预算不冒数学终点，350分钟job配置也不解除研究责任。

[完整请求](../computations/resume-20261127-actions-request-19.json) 27133B/SHA256 `445c39271bb2a87c96357c3db9ce965b19ea6776338c2f7ad2e940f75f1d3d18`与独立workflow19一起发布即触发公开Actions。控制器是原18的完整19984B正文，仅四个HANDOFF槽标签改19；SHA256 `536ce99e205816552f59bf1066da5e3ba451aff561048115984034b54fe56c37`。完整workflow保原partial/sparse checkout、依赖锁定、token隔离、350分钟与原permission，只改独立名称和请求/controller路径。主程序和科学工作树原有隔离、真实pull后双README diff、普通push/NFF rebase循环均原字保持。身份与每项准确替换列在请求和交付表；没有新增AST/fixture/审查门。

## 下游实际责任

当前完整R722 normal/连续geometry/closed/R716/mesh的运行体均通用地读取实际command/model/seed；本19只派生完整参数与新output归属。前三后处理路径为bhalf-first-R722-normal-root-and-sixjet-fees-v1、bhalf-first-R722-continuous-gram-curvature-support-v1、bhalf-first-R722-complete-closed-phase-grip-v1。完整posterior与旧R709真实bool、全1024圆胞/922径向+cuts/32stage/六jet/全tail/working费用、上下帽/mixed/allphase、完整唯一主副件/晚失败、无标记管/正V/非零中心矩均仍须本场支付。

final模式须实际完整13成员；packet须完整required-angle不可变同点快照，可以是trial但不冒accepted/final。全5t与三级空间/频率/时间实际精化、完整网格和机器/原容差责任不减，M320零包含仍不是新解。所有raw数组/逐点结果/网格只runner；Git保完整源码、全参数及紧凑实际事实。

## 完整文本复现

[参数再生器](../scripts/resume_20261126/reproduce_fixed_fejer_bhalf_complete_parameters.mjs) 10522B/SHA256 `8570320f61c5def522512553c2627a7abf551005f06d750ea872b2fb821cda00`读取已刊三个完整不可变父文件，生成上述science/pure/display整件，保所有显式改动及输出完整SHA/bytes。它只操作完整文本/JSON，不导入科学或执行AST/数值，不加入队列。原父参数仍按精确Git字节可读；新两输入的真实重建发生在公开Actions，而非此再生器。

本发布准备时没有19 actual run ID、input/model/field/result，相关字段都为null；之后在本说明续写真实来源/返回。README真正完成标准未达到，继续求解及所有未付证明和实际精化。


## 官方启动及首个必要输入实际返回

官方run为[46076669320/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46076669320)，job140765886020，created/run_started均2026-11-27T22:26:37Z，head543cfdf281c9bcd0f9b13197721b003a275c5967。下面列官方完整run响应中用于定位本次任务的字段；不把workflow head冒实际科学工作树提交。22:28:27查询的完整jobs/steps显示依赖安装已success、research step5为in_progress。

> **原 JSON 01：首次官方 run。** [固定旧版完整记录，第 48–63 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L48-L63)。


> **原 JSON 02：首次官方 jobs。** [固定旧版完整记录，第 65–122 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L65-L122)。


根按确切远端提交`a95cf377859a88397a29f85b41dee8add43786e4`读取当前完整index28510B/SHA256 `f9b206661022cfd11619f96e42262cc9c6bde0a26055b1d0acf268aa51322171`/blob `a6b272d94fdd1254872bcfd50dc9131f1c302377`与第一卷5756B/`e86ad28c2b8499cc90149da6f1b44aba34852042681057e0a118434845732c24`/blob `a9499ef2285e9de320c515f9f816bacf1d896b12`。index真实记录时刻22:27:39 UTC；controller实际source SHA536ce99e205816552f59bf1066da5e3ba451aff561048115984034b54fe56c37和请求445c3927…对应本完整发布。

maker真实source commit `f001ca62c1081b7e542c842d14c198ce16b6bee5`、原源89cc6c07…，5.843130817000031秒自然返回0，无missing或summary error。当前report65326B/519ab0688ba80a1c20104d4073ee1d6c8e5836813451bc5f8d38aefbb90e3aa1；fixed-reference-input4334B/b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98；完整nodes与scalar身份见下方原阶段对象。只读取发布的有界metadata，没有读取144306B节点体或NPZ。

这只完成第一个必要输入。第二个完整reference、真正科学及纯读尚未自然返回，当前model/完整field/accepted/费用仍未知；不从输入成功推数值求解成功。全部完整原command、source、output与cleanup metadata如下；fullraw仍在本runner。

> **原 JSON 03：第一个必要输入的完整返回。** [固定旧版完整记录，第 130–234 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L130-L234)。



## 22:37:51 UTC 实际第二输入返回与初始科学统计

根在固定提交 `0c51ba4b8d4e82f345cb23106c29b952ab931c57` 读取总索引（37219 B / SHA256 `b02a205acd903a0571af15784ec205a9ea783ce6191e12d2aae82a1ca8964bd4`）及第1卷（16602 B / SHA256 `9252cd8595593bbf2d19f8cf02e668f0f90bccea0d624ef5d6939209c2c7c9dd`）。两输入均真实 returncode=0，随后完整科学子进程已运行；不是根据队列计划倒填 actual source。第二输入实际 source `1c081a1001d1c59902d8cdb3a1ed325245bb9fb4`，e717 完整原源，303.653668384 秒；全部原 26 参数、7 输出及身份见下方完整返回对象。参考数值文件 `212eb5…` 与载体 `840604…` 的身份和18相同来自本次独立重建结果，报告、历史与路径归因有本次自己的 whole identity；不继承旧科学场或旧证书。

当前科学实际提交 `36304a0df074fcacc324d9c8eda79a5620b6a897`，启动器 `f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506`，PID 3240。真正统计事件在 `2026-11-27T22:34:17.427979+00:00`：model `0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add`，初点及当前点 `7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47`；Phi=3825.0583894874153，max_relative_gram=0.6460503011117507，accepted_directions=0，complete_report=false。与18原初 Phi=4954.71485872585/Gram=0.6374168330977955 比，Phi更低而最大Gram误差更高；二者都是有限计算，不能宣告度量成功或全域几何改善。初始几何六族、真实root费用、接受步骤及终态均尚未返回；这些 null 被观察器逐项记为未能下标访问的缺值，不能把它们当零或当科学异常退出。

22:37:50 原 normal 记录仍处于同一初点，cached_angle_roots=1001，closure_original_returns=6782，closure_logical_failures=0。这只是既有自然调用的记录，不添加 root/J/F/积分调用，也不是全部 root 成功的连续证书。所有 source/argv/输出/失败未知仍由完整准备文件、下列实际对象和原索引共同保存；继续完整科学自然返回，之后整接 pure 和后继。

### 第二输入实际完整紧凑返回（无科学数组）

> **原 JSON 04：第二个必要输入的完整返回。** [固定旧版完整记录，第 247–436 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L247-L436)。


### 此次完整有界科学进度（含所有缺值错误）

> **原 JSON 05：完整只读进度观察。** [固定旧版完整记录，第 440–622 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L440-L622)。



## 22:47:54 UTC 原索引：初始全部六族几何已真返回，首 trial 开始

在固定提交 `17561514e3a4b718bc1a0dd7ad084c82e5a0406f`，原总索引 34784 B / SHA256 `b652b0221ca9ea1c620f5cee63d6d9a90500f6a68081e8f76b77b3f54de88e3b` 明确 initial_geometry_complete=true，初/current geometry点均 `7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47`，same model `0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add`。此次当前数学事件已为trial-start，不能把它的22:45:05.409023+00:00倒填成初始几何完成的精确时间；初几何准确事件时刻在本投影中未公开。

| 有符号有限几何家族 | 18同g、b/S=1/4原初 | 19同g、b/S=1/2真初 |
|---|---:|---:|
| reach | 2.0480426708394406 | 0.9684249942095058 |
| body_diameter | -0.04304843011978521 | -0.038135527545650194 |
| distance_plus | 0.11871374548166669 | 0.005863061771032241 |
| distance_minus | -3.0936337267043594 | -3.0936337267043594 |
| cap_diameter | -0.06715131487906445 | -0.06715131487906445 |
| height_floor | -1.0411715967426867 | -1.0411715967426867 |

最大正违反为0.9684249942095058，reach 与 distance_plus 两族仍正，其余四族负。实际初Phi3825.0583894874153低于18原初4954.71485872585，但最大Gram误差0.6460503011117507高于18原初0.6374168330977955。故这是真实完整有限几何的改善证据，同时明确没有达到有限可行性，更没有连续reach/全域metric/闭面振幅完成证书。相同三项标量不构成两model同一场；全target一致来自完整原参考与模型合同。

第一已观察新trial点为 `d761b5f4d54d681b81d3ad56297f2858b65022dd8416a783efda6a8afc7f10ec`，开始时间22:45:05.409023+00:00。至此观察其统计、几何、接受决定尚未返回；accepted_directions仍0、current仍原初点、complete_report=false。22:47:52 normal_chain_enter 对应该trial，cached_angle_roots=256、closure_original_returns=19999、closure_logical_failures=0，仅原自然调用观察，不能从新point推接受。源仍36304a0d/f600/PID3240与完整10fa；下一分支20只改恢复阻尼，不回写本19活动对象。

> **原 JSON 06：完整只读进度观察。** [固定旧版完整记录，第 642–768 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L642-L768)。



## 22:50:51.653725 UTC 首 trial 的真实统计

根在固定提交 `3b34f6064ca3030c4521f779844b64d05690c937` 读取22:57:58原总索引（34423 B / SHA256 `06998f6baa471edafe489ada038ea15fb67461de7da64c795172e368a62b84d4`）。同model0abfbf、首trial `d761b5f4d54d681b81d3ad56297f2858b65022dd8416a783efda6a8afc7f10ec` 的真实事件为 `2026-11-27T22:50:51.653725+00:00` trial-statistics-returned：Phi=3825.0583176123996、max_relative_gram=0.6460503022350718。初/current Phi3825.0583894874153、Gram0.6460503011117507仍原字保；Phi略降而最大Gram略升。

此时trial几何和接受决定仍未返回，trial_accepted=null；current仍初7e06、accepted0、current positive_g=.9684249942095058、complete_report=false。这个g属于current初点，不填到新trial。当前为恢复阶段，单看Phi不能判断其QP有效性或接受。22:57:51normal仍同trial、cached_angle_roots513、closure_original_returns29546、failures0；仅自然调用的有界观察，不等于全域或全部root证书。下面完整保所有实际progress身份和缺值，不增加新的F/J/root调用。

> **原 JSON 07：完整只读进度观察。** [固定旧版完整记录，第 777–895 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L777-L895)。


## 2026-11-27 23:26 UTC — 第一restoration真实接受，完整有限六族同点返回

固定提交 `436b33d16ef2c4b2fb5ed8b54955a4d59242d114` 小索引记录时间23:18:04 UTC，root先核整文件metadata再读全体。完整身份为：

> **原 JSON 08：完整索引身份。** [固定旧版完整记录，第 901–909 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L901-L909)。


准确 **23:17:39.437630+00:00** 的 `current-geometry-returned` 事件已经显示 current 为 `d761b5f4d54d681b81d3ad56297f2858b65022dd8416a783efda6a8afc7f10ec`，trial_accepted=true、accepted_directions=1，状态为 accepted restoration checkpoint returned。这里是该观察事件时间，不冒充未单独捕获的决策调用瞬时。实际完整科学源提交为：`36304a0df074fcacc324d9c8eda79a5620b6a897`；launcher仍f600、PID3240，model仍0abfbfe4全SHA。

原统计Phi=3825.0583176123996、Gram=.6460503022350718；原完整有限几何的最大违反为 .9679630392005261。当前、trial与previous_completed_trial三处完整点一致，三处接受状态各照原值保。

| family | 该实际已接受点的 g |
|---|---:|
| reach | 0.9679630392005261 |
| body_diameter | -0.03813552759796779 |
| distance_plus | 0.005863064535577611 |
| distance_minus | -3.0936337267043754 |
| cap_diameter | -0.06715131493167947 |
| height_floor | -1.0411715966765438 |

reach较初值下降且仍正；distance_plus较初值略升且仍正，余四负。Phi较初略降而最大Gram残差略升，这是原物理恢复接受，不是metric可行或整面连续证书。原previous_completed_trial_maximum_families明确为reach，无须猜测并列。实际alpha、QP状态、空间曲率位置和K/D未在此48字段投影给出，仍未知。

以下完整原观察保全部48合同中实际有值者、原缺值/错误、小文件whole身份、source和返回边界；无需另跑场或读取raw。

> **原 JSON 09：完整只读进度观察。** [固定旧版完整记录，第 928–1009 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L928-L1009)。


科学完整report=false、stop_reason=null、子进程未自然返回。未从一次accepted推出full13final、全部历史或后处理完成；继续同一完整原预算，并在真正完整返回后接已刊全pure/费用/closed/R716/mesh或同源续跑。

## 2026-11-27 23:49:39 UTC — 19第二恢复试步的真实统计

原第二trial b6229603a0c389ff658e4fe062dcee5ea8d04953b89859d4411a66786092cc8d于2026-11-27T23:32:17.128107+00:00开始（此前固定观察已登记），本次原math事件于23:38:29.041545+00:00真实返回statistics：Phi=3824.6263877655356，max_relative_Gram=0.6461163467955962。当前仍是已接受d761b5/accepted_directions=1，current六族g完整保原值；trial geometry、接受决定、alpha、K、D和空间最坏位置未返回或未投影，原缺值错误完整保。Phi下降而最大Gram上升，不把聚合目标降低说成度量或reach通过。实际source36304a0df074fcacc324d9c8eda79a5620b6a897/f600、PID3240/model0abfbf，complete_report=false、stop_reason=null。固定23:43:14Z观察及其原小文件whole身份如下，继续原全科学；不把当前g填到新trial。

以下为固定提交完整小索引的身份和原active全对象；仅读取已有标量，先metadata再全小正文，未取科学raw或另算场。缺值保原错误，真实source/点/事件按原对象不混同。

> **原 JSON 10：完整索引身份。** [固定旧版完整记录，第 1019–1027 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1019-L1027)。


> **原 JSON 11：完整只读进度观察。** [固定旧版完整记录，第 1029–1123 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1029-L1123)。


## 2026-11-28 00:17:56 UTC — 19第二试点真几何拒绝及下一试点统计

19第二已完成trial b6229603a0c389ff658e4fe062dcee5ea8d04953b89859d4411a66786092cc8d 真finite g=.9817636973298995、reach最大、accepted=false；原Phi3824.6263877655356/Gram.6461163467955962保。它超过current d761b5的.9679630392005261，current仍该点/accepted1。下一trial b90dede6c3af4017aabdcb192a29db785438598d495820748d0102d4aaa599cd 在2026-11-28T00:10:54.391913+00:00统计返Phi3824.8419061258187、Gram.6460565438436483；geometry/alpha/准确开始时刻未在此次原48投影返回，不推第二或第三方向。reportfalse、observerfail0，完整原对象保所有缺字段。

以下为固定提交完整小索引的身份和原active全对象；仅读取已有标量，先metadata再全小正文，未取科学raw或另算场。缺值保原错误，真实source/点/事件按原对象不混同。

> **原 JSON 12：完整索引身份。** [固定旧版完整记录，第 1131–1139 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1131-L1139)。


> **原 JSON 13：完整只读进度观察。** [固定旧版完整记录，第 1141–1235 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1141-L1235)。


## 2026-11-28 01:18:48 UTC — 19新增真实拒绝点及下一试步开始

原run46076669320/1、science36304a0df074fcacc324d9c8eda79a5620b6a897/f600/PID3240/model0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add未变。01:13:47Z完整观察保留末已完成试步7af04a5e5747103612082704d368b3cbd584b7e49989e2375dc1563d02cb0782：Phi3824.9499945462044、Gram0.6460516172517726、真实最大违反0.9691295883291671、maximum_families=reach、accepted=false。此点与此前b622、b90d均不同；本次读到的末完成字段不提供b90d的几何/决定，旧b90d未知仍保留，不凭出现顺序补回溯alpha或方向序号。

下一b6a0615856730517089d5656c8d3cd79eeef9255b81dd9d13189925d072c98d3于01:09:47.773025事件trial-start，统计/几何/接受均未返。current仍首个实际接受d761b5f4d54d681b81d3ad56297f2858b65022dd8416a783efda6a8afc7f10ec、accepted1，Phi3825.0583176123996、Gram0.6460503022350718、g0.9679630392005261，六族原样保下方。complete_report=false、子进程自然返回未观察，原科学预算继续；未把进度或current作准确费用输入。

以下固定完整小索引身份与原active全对象只保原已返标量；缺值/错误原样，未取科学raw或另算场。

> **原 JSON 14：完整索引身份。** [固定旧版完整记录，第 1245–1253 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1245-L1253)。


> **原 JSON 15：完整只读进度观察。** [固定旧版完整记录，第 1255–1357 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1255-L1357)。


## 2026-11-28 02:08:21 UTC — 19第二次真实接受与下一观测试点开始

同science36304a0df074fcacc324d9c8eda79a5620b6a897/PID3240、driver10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f、model0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add。原01:09开始的b6a0615856730517089d5656c8d3cd79eeef9255b81dd9d13189925d072c98d3现已真实accepted/current，accepted_directions=2，完整几何已返；Phi3825.0041260383055/Gram.6460509597730772。六族为reach+.9674426000792542、body_diameter−.038135567160281214、distance_plus+.005865141983896982、distance_minus−3.093633726715951、cap_diameter−.06715135473990153、height_floor−1.041171546633114；最大reach，仍不可行。精确接受时刻/alpha/方向号没有公开返回，不由计数推造。

下一trial b0f8f2b00d00956db896777f053e196fabc60c9b961f5193e725ddad4f19abee于01:58:28.902393+00:00实际开始，02:04:12Z索引尚无其统计、几何或决定。原b622/7af04拒绝及中间b90d未知照实保前文；complete_report=false、child_exit_code=null。完整原active含六族/错误、whole小进度身份保固定索引。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 16：原完整索引/分卷身份。** [固定旧版完整记录，第 1367–1378 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1367-L1378)。


## 2026-11-28 02:37:10 UTC — 19第三次真实接受，完整六族仍不可行

同science36304a0df074fcacc324d9c8eda79a5620b6a897、launcher f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506、PID3240、driver10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f、model0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add。先前开始的trial b0f8f2b00d00956db896777f053e196fabc60c9b961f5193e725ddad4f19abee现已成为真实current/accepted，accepted_direction_count=3；当前Phi3825.0037791222376、max_relative_gram .6460510001750339。

六族全部真实返回：reach+.9666075350730359、body_diameter−.03813556741003443、distance_plus+.005865153856709826、distance_minus−3.0936337267160265、cap_diameter−.06715135499349079、height_floor−1.0411715463143238。reach最大且两族正，仍不可行。数学事件02:32:06.244621+00:00为current-geometry-returned；索引02:34:24Z时complete_report=false、child_exit_code=null。alpha/实际接受瞬间与方向序号未公开，不能从accepted计数推造；此前所有拒绝和中间未知保原文。当前尚无下一trial或完整自然返回。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 17：原完整索引/分卷身份。** [固定旧版完整记录，第 1388–1399 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1388-L1399)。


## 2026-11-28 03:10:54 UTC — 19下一真实试点统计返回，几何未返

同一实际science36304a0df074fcacc324d9c8eda79a5620b6a897/launcherf600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506/PID3240/driver10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f/model0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add，下一trial20d617114ba603edf83e02f342ae26946054cc69a6f99d5f7a9bc474981af45f于2026-11-28T02:54:16.817876+00:00真实返回Phi=3824.990529790781/max_relative_Gram=0.6460480621212836。截至原索引2026-11-28T03:04:39Z，该点geometry及accepted仍未知，所有缺值TypeError保原完整索引，不从Phi下降推接受。

current仍b0f8f2b00d00956db896777f053e196fabc60c9b961f5193e725ddad4f19abee，accepted_directions=3，Phi=3825.0037791222376、Gram=0.6460510001750339，当前六族reach=0.9666075350730359、body_diameter=-0.03813556741003443、distance_plus=0.005865153856709826、distance_minus=-3.0936337267160265、cap_diameter=-0.06715135499349079、height_floor=-1.0411715463143238均为该原current自身返回。reach和distance_plus仍正。alpha、方向编号及完整typed未知。complete_report=false、child_exit_code=null，工作统计不代完整report、全域证书或准确后继输入。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 18：原完整索引/分卷身份。** [固定旧版完整记录，第 1409–1420 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1409-L1420)。


## 2026-11-28 03:45:09 UTC — 第19组完整科学自然返回并接原完整pure

实际19/46076669320/1在原完整157词、32stage、4恢复方向等原预算下自然返回，exit0，17453.083330151秒；不是平台终态或mutable progress。完整report为63722853B/ed1ea5db4d0b8961a954ccdd31d1f4662477537a64457db3d7c9eb8875ae3856，command50552B/fe75eb24fe48b0a490ded59b78ce1418f4c7d2ab11805675185d3dc1616beaf3，仅runner，不取大body。实际source36304a0df074fcacc324d9c8eda79a5620b6a897；launcher f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506与driver10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f分开。

原stop=`declared_restoration_budget; actual_violation_remains_and_is_not_accepted`，complete=true只是原report完整。current20d617114ba603edf83e02f342ae26946054cc69a6f99d5f7a9bc474981af45f/accepted4，Phi3824.990529790781/Gram.6460480621212836；六g依次reach .9662472339877322、body −.03813557730789774、distance+ .005865730451148687、distance− −3.0936337267194034、cap −.06715136488669782、height −1.0411715338774452，仍不可行。model0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add，final bundle979986bc7b4deb2a62c5595c440f1ec73dcbf1cfde3a1fa47e15c4e520ed53fb；全13final/typed/envelope及source角色不能以这些标量替代。原返回19个summary_errors（missing None/metric direction空等）全保原分卷，不补0/成功。实际last trial alpha1及1979.7416288919994s保。

仅退已自然返的原3整step；完整原queue在固定提交逐字保留。立即整接原pure的7词/445formal，原输入report与原完整字段全保，finish_when_done=false，无新增验证门、无缩短步骤。pure未实际返，准确N/G/R723/R716/mesh及同源restart原责任继续；报告失败数值不作为停止研究理由。

> **原 JSON 19：科学自然返回及原 queue/pure 全对象。** [固定旧版完整记录，第 1430–1498 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1430-L1498)。


## 2026-11-28 03:49:16 UTC — 接既刊完整N原参数

在19已真实自然返回完整report之后，原完整pure后直接接既刊N整step，38argv/36formal原字不动：900s、1000000leaf、192bit、128panels、8192rho/mean splits、1024全角、32stage及原全部根半径/径向域/六jet齐。不是新测试或缩域；science63722853B/ed1ea5db为该同runner真实输入，pure尚未观察完成。首次--repo={repo}按原控制器解析为本step实际独立source_worktree；若同outdir续费，必须从N实际返回记录继承此绝对源路径，不能猜或用后来副本覆盖。N的whole report/complete/连续branch三者分开；N真实全域与固定wholeSHA后才接对应G/P，再R723/U。原完整mesh终场链单独继续准备，同g/五t/三级真精化义务不变。

> **原 JSON 20：准确 normal 的完整后继对象。** [固定旧版完整记录，第 1504–1535 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1504-L1535)。


## 2026-11-28 03:57:41 UTC — 19原完整pure真实返回及已付读取边界

原pure自然exit0，322.5631248630016s，实际source d854e9c2fbe289e9353e354fcfcbab162d2d8d69/reader8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49。输出8392178B/a8caef504eb7ccbabcaa02e3b6a0c736c296075e3f6adefcecc4de228b38aabd，仅runner，不整读大body。全部445原formal和22summary_errors保固定原卷；25个snapshot按本点绑定，cross_point_backfill=false，不把未做metric步骤的空列表字段补成成功。

真实0个metric方向、4个restoration方向均接受，final_geometry_passed=false。读取出的restoration_qp_status=`dependent_blocker_at_zero_step`，原Pg .967670341594262/容差9.68424994209515e-7等诊断如下；这是该readout对应的原记录，不自行推广所有方向或改算法结论。最终Gram.6460480621212836/reachg.9662472339877322仍不达标。N已完整排后继但尚未观察其自然返回；晚N的G必须新目录，P可同canonical/原physical流复用完整块，最终U仍绑定相同wholeN，不能误读为强制全部矩重算。

> **原 JSON 21：原 pure 的真实完整投影与缺项。** [固定旧版完整记录，第 1543–1612 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1543-L1612)。


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 22：原完整索引/分卷身份。** [固定旧版完整记录，第 1616–1635 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run19-complete-bhalf-launch-and-continuation.md#L1616-L1635)。

