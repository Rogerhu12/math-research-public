# 20：同一完整 bhalf 输入、较小恢复阻尼的独立续求

## RET84：终态导读与完整历史记录

**已知终态：** run 46079535427/1 官方在 2026-11-28 04:46:09Z 为 completed/cancelled，原因未知。最后观察的 current 接受数为 3，下一试点只有自身统计，完整科学 report、自然返回和 final/typed 未观察；原 pure 没有因官方终态变成已执行。末节保全部真实边界。

本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。20 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。

**完整旧文件：** 93699 字节；SHA256 `118f35c8c0a10d6d0c73298bdb872c1076595973f9535b9ccc263aa1a4cb62d1`；Git blob `6c5f86daae94b925f0f23ba75c4617484f5e3c11`；固定提交 `a7ee59c79535235b4161da7780b77556e9760940`。[完整旧版](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md)。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET84 完整交付表](../computations/terminal-run19-24-narrative-retention-84-complete-delivery.json)。

下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。

会话 Astra-larger-e4e2a2bf-20261126（AI-assisted）。准备时间 2026-11-27 22:54:51 UTC。本提交同时提供完整源码绑定、全部原参数和公开 Actions 启动；真实 run、job、实际源提交和新输入/场身份须由实际返回另记，不能从计划倒填。

## 当前依据与唯一科学参数变化

[完整来源分析及严格比较](2026-11-27-full-restoration-scale-and-mu001-branch.md)已从实际10fa driver、fb4e QP和全坐标源给出：只要完整有限几何违反仍正，程序处于恢复阶段，QP目标没有Phi项。原相同线性可行集的精确QP最优解在降低mu时，其最优非负公共松弛量不增；64步截断、非线性全几何、root/alpha和实际收敛没有因此得到保证。

本独立分支保持19的b/S=1/2、delta=1/32和原同一g，唯一科学标量把argv37 `.01` 改为 `.001`（`--restoration-damping`）。metric damping仍 `.01`，完整坐标范数、1/4个metric/restoration方向、16/64内迭代、15全线搜索、32normal stages以及全部其他域/参数/预算不变。argv71只改独立输出namespace `fixed-fejer-meridian-batched-bhalf-mu001-first`。运行中的19不修改。

19实际bhalf初六族reach=.9684249942095058、distplus=.005863061771032241仍正，Phi3825.0583894874153、Gram.6460503011117507；相较18初reach/distplus/Phi下降而最大Gram误差升高。完整数值与界线见[19实录](2026-11-27-run19-complete-bhalf-launch-and-continuation.md)。这里仅据已经实际返回的有限结果选择独立方向，不继承它的场、接受点、参考报告身份或准确证书。

## 全部交付与原字身份

[完整参数包](../computations/fixed-fejer-bhalf-mu001-complete-parameter-delivery.json) 50679 B / SHA256 `ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4` 含全137角色、18原运行源、原120对、三份完整19父文件、所有旧metadata/失败/typed未知和精确delta。当前10fa/8027/f600及其他原运行体没有代码变化。

| 角色 | 完整文件字节 | SHA256 |
|---|---:|---|
| science | 97019 | `89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca` |
| pure | 86221 | `f627447f7887bdc9d7f257b4d0772173556683501cd5fa9f1e39890ec7ac7f64` |
| display | 32429 | `1fef7603002bdfbac58623b1d7c8b1cd0492d050f42c22acfd1ce11c3597278e` |
| parameter_constructor | 15064 | `acd5d19439d9a6b00216bb6bfee2fab46087356a3580b97b946961fb6e83daa9` |
| source_analysis_and_choice | 15526 | `42ef2c9012b6c76439f09d0255392eabda6a27d240737e22e1bd74e3a914e313` |
| 完整参数总表 | 50679 | `ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4` |

完整文件路径与Git blob在上述参数包与[启动总表](../computations/fixed-fejer-bhalf-mu001-complete-launch-delivery.json)。science157/pure7词、458/445 formal、48live完整保，不裁成“运行最小集”。旧408/395formal及原18+30 live来历也完整保。

## 真正执行顺序

初始队列 73243 B / SHA256 `9d82aeee09115e026edb61f997ccde501004f05c602e3fdf4811373c4c7aff23` 包含两项原必要完整输入构造和整个科学step。输入1保持父对象所有字，输入2仅id的run19变run20、26参数及全输出/摘要不变；新runner独立重建参考、原923节点、全7377观察、2218标量叶。原input构造的accuracy_reached若false仍真实保，构造成功不冒科学成功。

两完整science/pure队列带包装共117276 B pretty / 104048 B compact，均超控制器95000上限。两step本身数组103956 B同样超限。因此先整运行science；真正自然返回后保存完整旧对象和全部真实输出身份，再退只已返回的对象、接入完整pure7词/445selectors。没有增加数学或审批门，也没有缩减任何原参数。完整normal/geometry/closed、R716和全mesh后续保持未付责任，在各自完整真实材料具备后接着执行。

## 控制与规则

控制器 19984 B / `1d790c7c805c26762bd982e1cfcd00f3c38d774e272468529af823966557d629` 只把原19四处H槽标签改成20；完整执行逻辑、真实pull/rebase及双README差异检查不变。workflow 2219 B / `7ee7db6e9b1c6d763439e0967ae974661c4facb8ca90c4a67eb945d4bb6aadbc` 只改名称、request/controller路径和独立concurrency标签，原partial checkout、所有原依赖、permissions及350分钟预算保持。

请求 44226 B / `965c1cbf18be6f9314ef6a15019e498ae1a71dc5a00489c90a0e1911b356c39a` 完整保19原请求的历史metadata并明确当前真实10fa/8027/f600与bhalf参数；旧19请求中沿用的bquarter描述只留历史，不冒当前参数。controller20000秒是后续接纳预算，不将活动child超时杀掉；job结束仍非研究完成。17–19现有队列和源保持，16官方cancelled及末科学未知另保[终态](2026-11-27-run16-official-terminal-and-unreturned-observed-solve.md)。

只在授权公开Actions做科学；全部科学raw/逐胞/mesh/checkpoint只runner，Git保全源、全参数、证明与实际小记录。根终端仍不可用，cloud freshHEAD核对并普通非force推送不冒真pull；控制器每次实际pull即比较双README，只读变化并记已读commit。启动前双README已读基准 `1e642976aec7c6e620da2e2bab3112e6ee30ee56`，实际发布时fresh检查；当前hash见request。

新实际run/job/model/point/科学report/accepted/final/所有fee和mesh均未知。该完整分支不是完成结论；继续到README全标准。


## 22:56:26 UTC：官方运行已真实启动

上述完整launch提交 `85cd235221ace28158625a7ced52a24551b509eb` 实际触发 **run46079535427/1**，官方created_at/run_started_at均为 **2026-11-27T22:55:41Z**。Job **140775034500** 当前in_progress；checkout、Python和全部原依赖安装已success，完整公开研究步骤5正in_progress。此时未读到任何完整新input或科学自然返回；提交HEAD只标启动，不倒填各step实际source或未来field。

根还在精确发布父 `52ec703c1a995c63c8af83175045c5de0c43e0f6` 读完整workflows Git树 `82a183256a747fc2758adaeb9a7304609f72864b`（1266项，truncated=false），该父无parallel20路径。先前contents接口的1000项不被当作完整缺席证据；完整Git树身份才确定此次新增路径。

> **原 JSON 01：首次官方 run/jobs。** [固定旧版完整记录，第 51–137 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L51-L137)。



## 22:56:53 UTC 第一完整输入实际返回0

根在固定提交 `3b34f6064ca3030c4521f779844b64d05690c937` 读取实际第1卷 5756 B / SHA256 `dd6a0a0cce998492ce923197f60ea4afccd1202767a4e900cfb15c877b8359d5`（Git blob b4151ee00a7de76ca65b2591b9b551e607f07ea5）。第一个必要输入构造真正completed/returncode0，用时5.931292771999992秒，实际source commit `ebdf38b0f0754f3a4760d1c52f638457b7b15bbd`，原89cc完整maker。不是将launch HEAD当该step源码。

完整输入报告65332 B / `24fd29704868e7c55763d74c63b8e04919f6481951600122934e22ca5ab0c368`；fixed-reference-input.npz4334 B / `b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98`；完整nodes144306 B / `1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5`；完整scalar40488 B / `2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189`。后三项与19相同是本次完整独立输入构造的实际字节事实，不从旧runner搬回数据。没有下载这些大raw/二进制，全部身份来自完整原小记录。

所有原6参数、实际命令/输出、输入/源、空cleanup元数据、summary_errors和missing_outputs完整保如下。第二个完整参考输入及新完整科学report/model/point此时仍未读到自然返回；maker0不支付后续科学或几何结论。

> **原 JSON 02：第一个必要输入的完整返回。** [固定旧版完整记录，第 148–252 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L148-L252)。


## 2026-11-27 23:16 UTC — 第二输入真实返回及初始完整有限几何

从固定提交 `eedf4ae13a83539afe061260e480dbdce51213b0` 的完整小索引与第1卷读取，先读 bytes/blob，再取全部正文；没有取 runner 科学数组或完整逐胞报告。原两份小文件身份完整如下。索引记录时间为 23:14:33 UTC，独立 active observation 在 23:14:32Z。

> **原 JSON 03：原完整索引/分卷身份。** [固定旧版完整记录，第 258–279 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L258-L279)。


第二必要参考输入真实退出0，控制器计时446.51950942400003秒，原报告内部443.237231892秒；实际源码提交 `25e8c73df95535c5c2cac4f839edd9f8beb0cd53`、源码e7175f59全SHA见下。报告84,966 B / `7d212377a44e7f0e47d5bdc198f682c5fc7cfd09eb97976cfd546f7d2271a6b6`。所有七个输出身份、完整原命令、input和cleanup均保以下原对象。参考程序的 complete=true 不改其 accuracy_reached=false；全尾未丢、2218叶为预先指定，仍有精化责任。

> **原 JSON 04：第二个必要输入的完整返回。** [固定旧版完整记录，第 283–472 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L283-L472)。


当前完整科学实际源码提交 `c592e434ac19b1659c179ab6929ed592f104f362`，launcher `f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506`，PID3277。实际 model `0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add` 与19初值相同；真实初点 `7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47`。本次是独立 runner 的原参考初值重建，未继承19的试步或历史。

初始几何事件的准确时间为 **2026-11-27T23:13:27.016759+00:00**，不是后续 trial 时间。初统计 Phi=3825.0583894874153、最大Gram残差=.6460503011117507；本次观察未给初统计独立事件时刻，不回填几何时刻。六个完整有限有符号约束为：

| family | 原真实 g |
|---|---:|
| reach | 0.9684249942095058 |
| body_diameter | -0.038135527545650194 |
| distance_plus | 0.005863061771032241 |
| distance_minus | -3.0936337267043594 |
| cap_diameter | -0.06715131487906445 |
| height_floor | -1.0411715967426867 |

这六值与19原初值逐项相同，符合只改恢复阻尼、不改初始场的参数设计；这不是恢复方向、接受结果或连续费用的相同性结论。reach和distance_plus仍正，有限筛尚不可行。accepted=0、完整科学report=false，trial统计/几何/决定尚未观察，所有对应 None 读数保其原错误而不填零。normal进度累计返8762且逻辑失败0，也不代根的连续唯一性。

以下完整原 active observation 保所有已知字段、小文件整身份、缺值错误和真实源绑定；仅这条本来已有的小投影被读取，没有额外计算或自建前门。

> **原 JSON 05：完整只读进度观察。** [固定旧版完整记录，第 491–625 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L491-L625)。


继续同一完整157词科学；自然返回后接原pure及完整normal/geometry/closed/R716/mesh，完整final和所有同源输入实际存在才可restart。当前仍不具备本课题README完成证据。

## 2026-11-27 23:39:50 UTC — 第一个真实trial统计返回，几何仍未返

独立20的首trial在23:20:09.363322开始，完整点 `3459061e0d7631ad5f69d6d2b7e02801c576d3941ee13963f379a3896927f28b`。原trial-statistics-returned准确时刻 **23:28:21.769877+00:00**，Phi=3824.783531693056、Gram=.6460723929865344。相比本轮初值，Phi下降而最大Gram误差上升；这仍只是统计。trial geometry、alpha、接受决定未知，current仍初始7e06/accepted0，不能将初g=.9684249942095058写成这个trial的g，也不能以Phi下降推恢复接受或metric改善。

该原观察在固定提交的完整小索引中，含所有source/PID、全部原正常/数学scalar、缺值错误与完整请求，以下精确whole文件记录可逐字恢复；本节只另列整个数学子对象和两份完整小文件身份，不声称它代替整个索引。未取任何runner raw，也未改science。

> **原 JSON 06：完整数学观察及来源身份。** [固定旧版完整记录，第 635–699 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L635-L699)。


科学report仍false、未自然返回；完整normal/geometry/R723/R716/mesh等待其真实材料，继续原完整预算。

## 2026-11-28 00:11:20 UTC — 20首试点完整有限几何拒绝；下一试点尚未返回

20首trial `3459061e0d7631ad5f69d6d2b7e02801c576d3941ee13963f379a3896927f28b` 的真实 finite g=0.9750099817855096，最大族为reach；previous_completed_trial_accepted=false。它比 current 初点 g=0.9684249942095058 大，不能由该试点支持降低恢复阻尼改善几何；仍保原Phi=3824.783531693056、Gram=0.6460723929865344。原48项投影未包含六族全值、alpha或准确决定时刻，均未知，不以初值填试点。下一trial `d34614ab98e8942a3dc9e8e0ff77d4bda999c436b1a765ea8fc741cfcb8d72ee` 在2026-11-28T00:03:30.800085+00:00开始，统计/几何/alpha尚未返回；不能从第二个trial推成第二方向。current仍7e06初点/accepted0，reportfalse。此次固定观察为00:05:01Z，原小文件缺字段错误原样保留，它们不等于求解器逻辑失败。

以下为固定提交完整小索引的身份和原active全对象；仅读取已有标量，先metadata再全小正文，未取科学raw或另算场。缺值保原错误，真实source/点/事件按原对象不混同。

> **原 JSON 07：完整索引身份。** [固定旧版完整记录，第 709–717 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L709-L717)。


> **原 JSON 08：完整只读进度观察。** [固定旧版完整记录，第 719–821 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L719-L821)。


## 2026-11-28 00:18:02 UTC — 20下一试点统计返回，几何仍未知

trial d34614ab98e8942a3dc9e8e0ff77d4bda999c436b1a765ea8fc741cfcb8d72ee 在2026-11-28T00:11:35.553745+00:00真实统计返Phi3824.9207739761805、Gram.6460517826414733。该点geometry/alpha/接受尚未知；current仍初7e06、g=.9684249942095058、accepted0/reportfalse。上一345906真g=.9750099817855096已拒的实际记录保留，不能把新统计当几何改善或已接受。

以下为固定提交完整小索引的身份和原active全对象；仅读取已有标量，先metadata再全小正文，未取科学raw或另算场。缺值保原错误，真实source/点/事件按原对象不混同。

> **原 JSON 09：完整索引身份。** [固定旧版完整记录，第 829–837 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L829-L837)。


> **原 JSON 10：完整只读进度观察。** [固定旧版完整记录，第 839–933 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L839-L933)。


## 2026-11-28 01:19:08 UTC — 20第二试步真实拒绝与下一统计返回

run46079535427/1仍原c592e434ac19b1659c179ab6929ed592f104f362/f600/PID3277、model0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add。此前已登记统计但几何未知的d34614ab98e8942a3dc9e8e0ff77d4bda999c436b1a765ea8fc741cfcb8d72ee现确认为真实几何g0.970243177977179、maximum_families=reach、accepted=false；Phi3824.9207739761805/Gram0.6460517826414733保。拒绝决定时刻、alpha及方向号未知。

新trial0f4d216ea4bf3c105af76b11b85e87204cd5758888fba506b3f4f6cbd0a2d871于00:54:57.956069统计返回Phi3824.9895336084514、Gram0.646051041919538；最新观察01:15:49Z时其几何/接受尚未知，不能以旧current或前一trial几何填入。current仍初7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47、accepted0，原初始Phi3825.0583894874153/Gram.6460503011117507/g.9684249942095058与全部六族保。科学未自然返回、reportfalse、纯读者及final未知。没有执行新的本地计算。

以下固定完整小索引身份与原active全对象只保原已返标量；缺值/错误原样，未取科学raw或另算场。

> **原 JSON 11：完整索引身份。** [固定旧版完整记录，第 943–951 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L943-L951)。


> **原 JSON 12：完整只读进度观察。** [固定旧版完整记录，第 953–1047 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L953-L1047)。


## 2026-11-28 02:08:28 UTC — 20首次真实接受及下一试点统计返回

同sciencec592e434ac19b1659c179ab6929ed592f104f362/PID3277、driver10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f、model0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add。0f4d216ea4bf3c105af76b11b85e87204cd5758888fba506b3f4f6cbd0a2d871现已真实accepted/current，accepted_directions=1，Phi3824.9895336084514、Gram.646051041919538，完整六族返回：reach+.9680716975090076、body_diameter−.03813557789762323、distance_plus+.005865705781869512、distance_minus−3.0936337267190757、cap_diameter−.06715136554632728、height_floor−1.0411715330482163；最大reach仍正。原345906/d346已拒事实保全；精确接受时刻/alpha/方向号未知。

下一trial b6cb9da866ea696379a5c2e63090f69b080ff09345a6cb7d62dd1cb461efe28d于01:59:52.178099+00:00真实返回统计Phi3824.9619403696915/Gram.6460452977630746。02:01:22Z原索引尚无该试点geometry/accepted，current仍0f4d，complete_report=false、child_exit_code=null。不同run和mu的局部进度不作为全局改善或连续证书。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 13：原完整索引/分卷身份。** [固定旧版完整记录，第 1057–1068 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L1057-L1068)。


## 2026-11-28 03:10:14 UTC — 20第二真实接受及下一试点开始

同sciencec592e434ac19b1659c179ab6929ed592f104f362/launcherf600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506/PID3277/driver10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f/model0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add。此前仅统计的b6cb9da866ea696379a5c2e63090f69b080ff09345a6cb7d62dd1cb461efe28d现为真实current及last_completed_trial，accepted=true、accepted_directions=2。Phi=3824.9619403696915、Gram=0.6460452977630746；六族完整为reach=0.966040127402165、body_diameter=-0.038135598469925314、distance_plus=0.005866895954812268、distance_minus=-3.0936337267260736、cap_diameter=-0.0671513861176688、height_floor=-1.0411715071877172。最大族reach仍正；distplus亦正。相比首接受点reach.9680716975090076降至.966040127402165，但仍非可行，既往全部拒绝和原未知保前文。

下一真实triale70a61ecc2a2b9a4114b23610566c51c8cb2c92ed9c7a111dc8cfc6568dfd544于2026-11-28T02:57:08.390895+00:00开始。原索引2026-11-28T03:02:05Z仍没有该点统计或几何，trial_accepted=null，缺值观察TypeError保原对象；不能把上一点Phi/Gram移到新trial。原0f4d、现b6cb与下一e70a分明。精确接受时刻、alpha、方向编号、预测/typed全史未知。complete_report=false、child_exit_code=null，没有完整科学返回/准确费用输入。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 14：原完整索引/分卷身份。** [固定旧版完整记录，第 1078–1089 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L1078-L1089)。


## 2026-11-28 03:45:47 UTC — 20第三真实恢复接受及六族

实际索引03:42:35Z，math03:41:07.461084+00:00为accepted-checkpoint-returned。current e70a61ecc2a2b9a4114b23610566c51c8cb2c92ed9c7a111dc8cfc6568dfd544，accepted3，Phi3824.9508918379306/Gram.6460501386747761；reachg.9658357818598327与distance+.005867170745044947仍正，未可行。原current/source/model/六族完整如下；完整report=false、自然返回未观察、exit仍null，缓存和速度未推。launcher f600bc6与math_driver10fa4分开，不把相同起点当同一实际场。

> **原 JSON 15：真实数学标量及六族。** [固定旧版完整记录，第 1095–1140 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L1095-L1140)。


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 16：原完整索引/分卷身份。** [固定旧版完整记录，第 1144–1155 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L1144-L1155)。


## 2026-11-28 04:38:45 UTC — 20下一完整试步统计实际返回

20当前仍e70a/accepted3，原完整六g保持。下一a6b3047ab1531291591f19625fd0aa05fbea1f287eca3e1519c4bbb20f1c08d2于04:11:14.576261返回Phi3824.946159242409/Gram.6460490804199277；截至04:33:10几何和接受未知，child未自然退出。原三项缺值及所有身份保留，不补alpha或phase。

> **原 JSON 17：完整只读进度观察。** [固定旧版完整记录，第 1161–1255 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L1161-L1255)。


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 18：原完整索引/分卷身份。** [固定旧版完整记录，第 1259–1270 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L1259-L1270)。


## 2026-11-28 04:50:15 UTC — 20官方取消终态与最后未完成科学状态

官方run46079535427/1在04:46:09Z为completed/cancelled；job140775034500于04:46:08Z完成，research步骤04:45:57Z为cancelled。最后已实际保存索引04:43:19仍是running：current e70a/accepted3/原完整六g，a6b304只有Phi/Gram，完整report和child自然return未观察。此终态不是科学自然退出或完整final，也不是课题完成。官方对象没有给出可归因的取消原因；与原350min窗口相近不足以断言原因，check-run/annotations读取未返回可用官方说明，故原因仍未知。后续不得为该已终态runner排同机续接或迁移其未完整返回的raw；真正计算继续。

末次完整controller规则槽原文（保最后真pull与README核查）：

<!-- visible-larger-parallel-20:start -->
Actions20：[run 46079535427/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46079535427)；[全阶段记录](notes/2026-11-27-public-actions-46079535427-1.md)。running；已返2，exit=未返。
并行20规则核查：2026-11-28 04:43:19 UTC，真实pull至`04b337366d4333b9fb5e8957d3fdddeae5744822`，双README无变化。
<!-- visible-larger-parallel-20:end -->

完整官方run/jobs对象：

> **原 JSON 19：官方取消 run/jobs 全对象。** [固定旧版完整记录，第 1285–1609 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L1285-L1609)。


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

> **原 JSON 20：原完整索引/分卷身份。** [固定旧版完整记录，第 1613–1624 行](https://github.com/Rogerhu12/math-research-public/blob/a7ee59c79535235b4161da7780b77556e9760940/topics/visible-flex-larger-amplitude/notes/2026-11-27-run20-complete-bhalf-mu001-launch-and-continuation.md#L1613-L1624)。

