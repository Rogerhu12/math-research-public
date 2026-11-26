# Run05 实际阶段 8–11：第二 integral 方向、完整真实拒因与历史指纹

日期：2026-11-26。

本次完整第二 integral 方向真实接受 α=1/32；更大的四个下降步都由 reach 家族拒绝，幅度各家族均通过。最坏曲率地点已经移到 cell295/291/252/237，不能继承旧节点范数方向的 cell0/1 归因。QP仍在64次advance预算处返回，未达到其实际Pg容差。

这些是公开 Actions [45870334713/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45870334713) **本次实际阶段8–11**的结果。阶段8是历史30分支的完整必要重建；其余三项只读取本runner已有完整报告/NPZ和地址，不重算科学。没有用旧03b数值补本次缺项。

## 1. 完整公开证据与实际身份

- [第2卷，实际阶段8](2026-11-26-public-actions-45870334713-1-part-002.md)：本次读取 Git blob `a5ebf2076e2991a4a5f3d5ad1e3f4b1625b5ad49`，UTF-8 36212 B。
- [第3卷，实际阶段9–11](2026-11-26-public-actions-45870334713-1-part-003.md)：Git blob `3ad8a15fce9c20dbcfbc941c4063b5604302c5c9`，UTF-8 55729 B。

这些大小由保存的公开小卷实际字节计数得到，字符数与UTF-8字节数不混用。12967197 B的科学原报告只在runner由完整纯reader读取，没有经连接器整读。

| 实际阶段 | 完整入口来源 SHA256 | 实际源码提交 | 返回 |
|---|---|---|---|
| 8 第二integral launcher | `a94263f037dfa8535b11cf44fa93b6a4cd6df7dee1a6be35f2ea14f5abaa2690` | `abe329aa212255c0a3a104ce7aeb801b0d6320ac` | completed/0，1076.5428759919996 s |
| 9 原完整606 pure reader | `6d54cbba7ff998bc98b0f39c6a26ae33c16957fb0b9dc0fffced1037212455eb` | `41ab63d869f000db9562938830161a28a602b75a` | completed/0，5.785304030000589 s |
| 10 全历史/初点指纹 | `e54cad5e7e78f3576412fef82701a3b276fb9af8795ca16d3e016cb9bc0382e7` | `0bdc6e95471047cd0e9f6f4782b5057529b6b331` | completed/0，10.782665079999788 s |
| 11 动态全部trial家族reader | `625317b44fd3610903b395d6e8fd5374a4764d6930ef08fb92c33f45e15c7cd3` | `74951d16b2390aef45507bde5272bd26b5171a6f` | completed/0，5.793373509999583 s |

科学driver为完整
`606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9`。
实际reference
`59027f3a144f8f0feb59e378b058178c781856803e6e704db8a6ff689b45d90f`，
固定profile
`e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350`，
model
`9b4958325403bd74616c5875ca54f027981d2d55c9c56634dc81f8cd0d2123c7`，
carrier
`dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`，
均由本次实际来源绑定。

实际父与initial-new-field均是
`c8cb4be613712282dedf4586c78d81bd86f7b9ae038c16a0f6ceced86eadd9a7`；
实际末bundle为
`f1e504f8a2fab97b564efb11c8aca27dc319e207e28006c8b3f24e87f0eb3c30`。
它们是完整真实读数，不是从旧hash生成的数据。本次完整报告
`axisymmetric-so3-integral-norm-second/report.json`
为
`18257406f36e68f7401a3a87c8f0f4f34866f774688a90e30eaa9354c90368b7`，
12967197 B。两NPZ均10720284 B。实际command文件
`e2d038488f2615236ad0ee9a1d59287db3bb91eb171d86cf507c166bfdcf09d3`，
11913 B。完整argv及输入/输出记录保留在阶段8对象。

## 2. 同一完整积分范数、实际方向和末面

M160、J923、N2048、1333370原自由量、45324288完整正权观察行保留。完整积分范数及各工作因子与实际阶段6相同：

| 对象 | 实际身份 |
|---|---|
| kind/schema | integral / complete-SO3-radial-H2-positive-whitening-v1 |
| norm identity | `c06a7abc532243cc3faee0b123a4d5c7f6c109527e426dc764b1205af528c8d9` |
| band | `ba5017bbbf9e8b63a63541ca39ef6636e6f691064f5aff1b81d5e9519e00b10e` |
| lower factor | `9c04393e73929625c76514bb3b78572e949b78dddcfcfa504163484e23e22d2a` |
| diagonal equilibration | `044bdec037398e505ae5a4d9626ee24ee06b8f3c8141e44405548684ddb57be3` |
| 正Gauss阶数 / bandwidth | 6 / 5 |

声明radial norm length.05、angular transition24；同p4/epsilon.001/scale.05、legacy fraction.5。metric预算1×64，restoration4×64，15ray；metric/restoration初末μ均.01。原所有变量、正权、完整原selector和幅度筛不缩减。

| 实际科学读数 | 初始 | 末态 |
|---|---:|---:|
| centered Phi | 197.584579939444 | 189.96270214659762 |
| 最大相对Gram工作残差 | 0.5063653325058848 | 0.5012784948500237 |
| 全真筛最大g | -0.0246162690052385 | -0.024924090597260973 |
| 曲率直径乘积 | — | 0.9311196669821497 |

同一数学Phi的变化由真实pure reader返回
-7.621877792846391；没有跨不同Phi、范数或初点相减。实际metric方向1、接受1；restoration方向0、接受0。停止原因
`declared_metric_direction_budget`。

完整实际QP归因：

| 实际量 | 返回值 |
|---|---:|
| status | iteration_limit |
| advances | 64 |
| 末面Pg | 1814.47103555099 |
| gradient tolerance | 0.0026797628909626422 |
| active face rows | 4 |
| 最大原线性违约 | 2.964615315390051e-21 |
| 原geometry rows | 39 |
| appended amplitude rows | 6 |
| 总C行 | 45 |
| C缓存字节 | 480013200 |
| QP秒数 | 843.255424252 |
| QP J/Jtranspose calls | 67 / 68 |
| 接受α | 0.03125 |

实际Pg没有达到容差；很小的线性违约不替代驻点，也不替代非线性几何。45是该真实方向的实际C行数，不是删去192上限中的行：完整selector的声明上限与其实际输出不同。后继在新父必须完整重建自己的原selector/幅度前缀；只有在同一父、同一方向冻结后才要求该字面前缀不改，不能拿旧父的45行数冒新方向的已读C。

## 3. 六个真实ray的完整家族归因

阶段11由完整6253 reader绑定同一个182574…原报告，并先调用未改的完整6d54 reader作来源核。它动态遍历实际全部方向和全部trial，返回 actual_trial_count=6、all_trials_retained=true、failed_family_assumed=false、missing_values_zeroed=false。

| trial | α | 同Phi实际值 | 真筛最大g | 真实结果 | K最坏cell/branch |
|---|---:|---:|---:|---|---|
| 0 | 1 | 293.6163727458347 | 未读 | same_objective_descent | 未读 |
| 1 | 0.5 | 125.21916647189587 | 6.960628223861761 | positive_reach | 295/0 |
| 2 | 0.25 | 145.0541146713789 | 1.9193414562844122 | positive_reach | 291/0 |
| 3 | 0.125 | 168.70428141099026 | 0.7567135551931865 | positive_reach | 252/1 |
| 4 | 0.0625 | 182.6001234466509 | 0.18635382498788267 | positive_reach | 237/1 |
| 5 | 0.03125 | 189.96270214659762 | -0.024924090597260973 | 接受 | 210/1 |

六个trial的domain均为true。全步Phi不降，所以按原控制流没有执行完整几何；它的g、K地点和各几何家族为未读，不填零。α=1/2、1/4、1/8、1/16均已完整读真几何，missing列表为空，唯一正家族是reach。α=1/32完整通过。

全部已真读trial的幅度家族值如下，保留实际符号与数值：

| α | body diameter | distance + | distance - | cap diameter | height floor |
|---|---:|---:|---:|---:|---:|
| 0.5 | -0.029311011805290166 | -0.13777974582173402 | -3.309035112406911 | -0.07388303672870766 | -1.0326924459777451 |
| 0.25 | -0.027010250543553216 | -0.13777993671032496 | -3.309033393588299 | -0.07072050410532571 | -1.036680060416382 |
| 0.125 | -0.025843613587762215 | -0.1377800321546263 | -3.3090325341791207 | -0.06913704525262732 | -1.0386738676357004 |
| 0.0625 | -0.02523062946779553 | -0.13778007987677898 | -3.3090321044745634 | -0.06834476769102626 | -1.0396707712453597 |
| 0.03125 | -0.024924090597260973 | -0.13778010373785565 | -3.309031889622293 | -0.06794849187641294 | -1.040169223050189 |

旧6d54摘要的 `actual_positive_physical_g` 在最后接受trial返回0，表示正违约部分；阶段11的g为真正maximum_physical_g，返回-0.024924090597260973。这两字段的定义不同，不能把0误作末态正好压在约束边界。

## 4. 最坏地点与完整D partner责任

全部已读K最坏地点的原binary64字：

| α | cell | branch | u hex | phi hex |
|---|---:|---:|---|---|
| 0.5 | 295 | 0 | `0x1.a94504b2ae4afp-1` | `0x1.5fdbbe9bba775p-4` |
| 0.25 | 291 | 0 | `0x1.eeb652740500ep-1` | `0x1.5fdbbe9bba775p-4` |
| 0.125 | 252 | 1 | `0x1.85d3b4bf2628fp-2` | `0x1.a4f931c375f35p-3` |
| 0.0625 | 237 | 1 | `0x1.0000000000000p-1` | `0x1.a4f931c375f35p-3` |
| 0.03125 | 210 | 1 | `0x1.a94504b2ae4afp-1` | `0x0.0p+0` |

特别是最近的较大拒绝ray α=1/16，在cell237、u=1/2、
phi=`0x1.a4f931c375f35p-3`、branch1有真reach正违约。
它与最后接受ray之间的差异有真实报告依据；不能把旧cell0/1瓶颈作为这次读数。

完整reader还保留每个trial的farthest-radius witness、body候选、paired-distance候选及Dlower、current height、maximum radius。其角色有明确范围：farthest-radius witness本身不自动等于
max(2,2|H|,2r)的活动支路；实际行构造须依同一次真实几何选择，再在固定父重新读取该地址的完整g/J。paired-distance候选来自原±p合并候选池，不冒两个独立符号各自argmax。

本次已读的最近拒绝ray记录Dlower=4.1447025791775，
current H=1.9457036941208237，maximum radius=2.07235128958875；
farthest-radius地址为cell880、
u=`0x1.5aebed3546d44p-3`、
phi=`0x1.ea16a4eb316f5p-4`。
完整其余地址均在公开动态JSON字符串和runner完整pure结果中，没有以这一个地点替代完整集合。

## 5. 真实末场与完整历史并集

科学末态记忆计数curvature1843、radius1771；
全永久点和每点双符号重读均为true。它们属于f1e504…末场。

阶段10的e54c纯入口另外消费六份**完整**来源：
reference locations，以及本run历史3、17、21、26、30对应的完整真实报告。
其最终递归集合为curvature1851、radius1851、protected39，pending0；
不能用1843/1771替代这个完整来源集合。

| 完整through30指纹 | 实际SHA256 |
|---|---|
| curvature | `cb5d24cd71cf0103d38a2367945820aca18745d3bd4e10f61dd5a64c3a6b1939` |
| radius | `cb5d24cd71cf0103d38a2367945820aca18745d3bd4e10f61dd5a64c3a6b1939` |
| protected | `afcf874a83df360834b6b339e00837ea2dd000b6ad3e2ef3377387e537116a5b` |
| combined | `667b8189ca1489ae1126521b8f09cacebe1f0c77eddf2d0e4228c101ad4db630` |

前五输入和每个through26前缀的实际摘要仍与阶段7相同。
第六输入是本次完整182574…报告；该输入自身的完整c/r/protected指纹也由纯入口逐项返回。
初点free-array再次真实读得
`cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3`，
初core/chart、H字、omega正零及original scalar参数/warm摘要均与本run阶段7返回一致。
这没有生成一个从未运行的旧03b集合hash，也没有因新文件摘要而豁免同目标永久地点。

阶段10输出
`postprocess/complete-location-and-initial-fingerprints-v2-05-through30.json`
为
`fbee1a8b7a778e6ce645aa88b8a96e8a996eca5337cc4da564ca47d7c341c9a4`，
31263 B。全部field/J/JT/root/scan/QP调用0；
summary_errors与missing_outputs均为空。

## 6. 纯归因的缺项边界和实际成本

阶段9的旧完整pure结果为
`c8223bf156245abfd2b0b77d11c6a1cc9fa8540564369be18b367b832ebabea7`，
54778 B。该入口完整返回，科学绑定与final bundle核均通过；
队列固定枚举15个trial和4个restoration方向，实际只有6trial、0restoration，
所以其summary产生86个 `list index out of range`。
这些仅对应不存在的trial6–14或restoration0–3字段，
不是科学子进程失败，不是已执行方向缺失，也不能补造其数值。

阶段11的动态全trial入口消除了这项摘要歧义；
其输出
`postprocess/axisymmetric-so3-integral-norm-second-all-trial-families.json`
为
`f7eec25fd67e751c4c378d0d2d61e60a4a2654c8f4e9ac84b702d320bcab5738`，
67319 B。公开结果完整保留6trial的家族、地点和全部QP方向JSON字符串；
summary_errors与missing_outputs均为空，所有科学调用0。

科学driver秒数1069.9878263070004、初始全读91.47128217400041秒，
peak RSS2113184 KiB。完整方向实际J/Jtranspose为68/69，point covectors44；
整个report计数residual9。方向内统计与整个report统计的口径不混用。

## 7. 由本次事实支持的后继范围

本次事实支持在真实f1e504…父上使用完整prior-separation：
把所有已发现reach拒点、双主曲率分支与其D partner带回该父真实读取并线性化；
保持新父完整原C/幅度前缀、完整原自由空间、同integral范数、同Phi和真实μ。
不能仅因为Pg尚大而把全部障碍解释为预算，也不能只延续旧core点。

已备359f入口的完整源码合同允许该606/integral父；
但其政策是第一个Phi下降而几何拒绝的ray作锚，本次旧方向的对应ray为α=.5。
它没有已经继承892f的最近拒绝ray加真可行fallback政策。
更贴合这次完整数据的后继政策是：先按完整原ray获得真实可行fallback，
再选紧邻的较大、Phi下降、完整几何拒绝ray作固定锚；
纠正始终同父同锚，所有新增行追加而不替换原前缀，
每个纠正候选重算完整Az、Phi和真几何。
所有新增永久地址也必须加入fallback的最终真重读后才能选接受。
那需要独立完整direct来源绑定，不能冒用normalized/cached模型身份。

本段只说明选择依据和责任，没有声称已排、已执行或已成功的后继。
现有完整原359f候选参数仍保存；不因它已经准备好就假定其差别较大的锚会成功。
本次continuous metric、continuous geometry、closed isometry三旗仍为false；
剩余全域、全相位几何、固定目标精化与题目完成标准继续由后续实际研究支付。
