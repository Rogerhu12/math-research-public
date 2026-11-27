# B030：实际 56594 / 原 2561 峰 / native H 续算的自然终态

2026-11-27。原 run 已自然结束；本稿只解析唯一原 stdout，不重新执行任何科学函数。

**这段补完原 2561 个剩余峰并真实完成一次 geometry restoration，随后有 12 次 metric 真接受。末保留物理点为 `cc117d48…`、η=`0.19917454273148172`，其已付资格属于 1630×3072 网格。当前完整库后来扩至 817 个 coarse 半径、1636 个 fine 半径、1829 条物理峰轨道和 334 条 working 行；新 coarse 余量使当前 phase 回到 geometry restoration。科学时钟停在 outer20 的新 Jacobian 中，不是算法无方向，也没有未完成的峰队列。**

后继应从该准确物理点、准确当前库、准确正几何余量和原 native checkpoint 继续。原 checkpoint 仍属于此前 metric 行函数语义；下一个 restoration 模型必须由原 helper 按语义变化重置，不得把它改标为已支付的 restoration 曲率。

## 1. 唯一运行与原件身份

| 项目 | 原记录 |
|---|---|
| workflow | `visible-r566-native56594-partial2561-20261127.yml` |
| run / attempt | [45924048811 / 1](https://github.com/Rogerhu12/math-research-public/actions/runs/45924048811) |
| job | [140261163768](https://github.com/Rogerhu12/math-research-public/actions/runs/45924048811/job/140261163768) |
| source commit | `042435b253617f260442a47fdf4c3d1a92698ae1` |
| job 时间 | 01:41:58—02:22:04 UTC，completed / success |
| 科学父启动器时间 | 01:42:27.518536—02:21:59.278413 UTC，returncode 0 |
| 原科学停止 | `EndSegment: working-row scientific clock before next atomic operation` |
| 原 FINAL reason | `cooperative_clock_or_unresolved_localizer_checkpoint`；本次具体原因是时钟 |
| 唯一 stdout | 29,097,972 B，SHA256 `6c081453125b616e15896b62e0bcbf2c199bf4470aa736274568eeb5a1923ed6` |
| 唯一 `WORKING_ROWS_FINAL` 原行 JSON | 392,448 B，SHA256 `5c5181a8cf7899c19677a02961ed903aab7b1d25fe4891531e65b4c08d96ca19` |
| 最后实际接受 checkpoint 原行 JSON | 507,607 B，SHA256 `f18c372e9180577629970d78798dccb604a33156d5dfddba4e17506d65421c8f` |

原日志由 true_history 在 metadata 明确 completed 后下载一次；此前 finite 只查 metadata，从未下载本 run 日志。没有第二次获取、活动日志、artifact 或 release。

执行源 `r566_native56594_partial2561_20261127.py` 为 66,583 B、SHA256
`c972c56133ff68705a91434d5ceeb404d5d7fe818d2cf168e2ac2b29efdfa09a`。
实际 gzip request 是 441,560 B、SHA256
`a89bb1b8886576345ef7bca4f82fd6ff8b32ba257093b719446db3e9e567d884`；
解压 JSON 2,746,505 B、SHA256
`1048c95fd2a7c4cf198256ccc11ebdbee5c1c7287bb81a164991ed62daa536a1`。
stdin 2,474,647 B、SHA256
`18ef8fbe552aaa514f28d27033e445c5b89d8ef9a22b36e5a77f357be23fc564`。
发布前根只更新规则 metadata，科学输入未变。

原 public pull 01:42:15.531455 UTC 读到 source commit；根/题 README blob 分别
`282e86b03385d3b6245ce7100ae2e2af7b103c2d`、
`d0432faff569c8e9af7ed4809847e12880976c11`，diff 均空。
private pull 01:42:20.082945 UTC 读到 `5ff8fa2797f5e227f085fc7b20c61c4cc8413726`，
根 blob `5ba164843b1f5802184178a82d786264404873a3`、进行中 QUEUE 检查通过；不发布私库内容。

环境仍为 Python 3.12.14 / NumPy 2.3.5 / SciPy 1.17.0。原 2400 秒范围、30 秒末预留和全部 20 个数值/求解参数保持。[范围说明](2026-11-27-r566-native56594-partial2561-scope-agent.md)及[上一原终态](2026-11-27-r566-native-d191-natural-final-agent.md)完整保留。

## 2. 原 9452 已付峰复用，只有 2561 剩余峰新算

入口保留原 `56594ecb1d8d94cd8463359dc2e40b4a681be6a4588296d63ae3eda3a240c7f3`，
η=`0.20868474226441153`，原 phase 为 geometry_restoration。待完成候选是
`53ed9bb6db3208246487553d2061ab4e61baaf1ba4b2159332a5686249f0dbba`，
同一 1610×3072 fine 和 oracle
`18745e500f027eaffa8178b66aafc3c9b01579e2d424b9e52367abc403ec6505`。

新范围准确复用原 9452 个已完成峰、83,830 次原目标求值和 440.78279974299994 秒原局部定位费用。只新算 2561 个剩余候选，新增 34,084 次点目标、136.35130346999995 秒；6 个批次全部完成，总 12,013 个候选已闭，unresolved=0、remaining=[]。原候选枚举、完整 coarse/fine、nested FFT 和已付前缀均未重跑；新必要 oracle/FFT 准备另计在本段总费用。

完整原定位后，最高 strip 工作余量仍为 `5.542782454369399e-9`，在原 `1e-8` tolerance 内；物理 geometry violation=0。候选 backend extra=0，原工作/完整行/nested 条件均保。它在 01:44:53.5445388 UTC 被准确记为
`source_saved_trial_completed_and_restoration_reached`，η=`0.20921004461892675`。

这次 restoration 的 η 高于入口 η 是原允许行为：不能用 metric 单调下降替换原 phase I 判据。完整 restoration 真接受后，才切入后续 metric 行选择。

原未输出的 `best_geo` 没有被伪造为 `e-.01`。实际逆舍入恢复给 33 个可能 binary64 值，区间
`[0.0004748151855267198, 0.00047481518552672155]`，两个精确实中点端点都包括。
因为本候选直接达到原 restoration tolerance，不需要这个区间中未知具体值的比较；接受后 `best_geo` 准确成为单值 `5.542782454369399e-9`。后续真正新资格及新 coarse 的原 max 更新继续产生已保存的准确单值。

## 3. 全部 13 次真实接受

下表每项都经过原完整 coarse/fine、真实峰和 nested 条件。第一项是原候选完成后的 restoration；其余 12 项是新的 metric 接受。缩步 fraction 是原 callback 的实际值，不是另一条隐含优化器路径。

| outer | 原 q SHA256 | η | fraction | 已合格 fine 半径数 |
|---:|---|---:|---:|---:|
| 来源待完成候选 | `53ed9bb6db3208246487553d2061ab4e61baaf1ba4b2159332a5686249f0dbba` | 0.20921004461892675 | 1 | 1610 |
| 3 | `827714cd90422d2bf7900b9a2ef927692ecc1030eefe9848ab186bae19c9ff18` | 0.207817664095236 | 0.5 | 1614 |
| 6 | `59331c54398c1d8afda6ed3c5cec3f911b9aa70a9aa32f21f21bc13bb7dc5c90` | 0.2064075084901812 | 1 | 1616 |
| 8 | `fd750fa744df8a8c175391af660858d5301496521f3064430565f078314b0e34` | 0.20560586053205632 | 0.5 | 1618 |
| 8 | `184c738e44cbddbaefd3495064ed745f76838c99dde4a26a9e253d0cf1c5da6a` | 0.205485331531598 | 0.5 | 1618 |
| 10 | `d6857010fed51c3a41a216fe103a7b1884dda818c320ad14503d31d5e7f2ea1c` | 0.20484315576751044 | 1 | 1620 |
| 12 | `ab2cab89899ecdc4927b2b646030165b1c12685b6f9db368d5cd9a187a0c8876` | 0.20198825518564278 | 1 | 1622 |
| 13 | `efa2d55b68201750ae4235c8e0c864b7cdfd3a903f03827a6436260756c4ad49` | 0.20092132509548524 | 0.5 | 1624 |
| 14 | `2aeadcd2da4f95c080426668bc47fc35ba0c1bac90e421f768ab81891daff78e` | 0.20026994278414217 | 0.125 | 1626 |
| 15 | `ddae52d835de2396e41fd7c61b9ee27044627b1d37509a42e16935c98537f84e` | 0.19957225422978492 | 0.125 | 1628 |
| 16 | `fc4cfd495f27d934d0e7ca6270059eef240b3050c6f13544cf707fe10c36440e` | 0.19933740979534187 | 0.0625 | 1628 |
| 17 | `0bd45b03436c832ba4486de1efcfef041bd65ca8e2def69ccf1b36772155c2ce` | 0.1992094383738086 | 0.03125 | 1630 |
| 17 | `cc117d48551e8b457bda12450e466f7e2dcff174311675b5e3445487bc9c6a30` | 0.19917454273148172 | 0.125 | 1630 |

最后接受在 02:17:53.0906692 UTC。其 backend extra=`0.19917454273148882`，working violation=0、physical box violation=0，完整 coarse 2,894,284 个标量行；完整 coarse/fine/localization 均完成。same-q nested 差分别为 metric `1.9984014443252818e-15`、relative mean-E `7.071116706047105e-16`、tau curvature `1.8926801459429042e-13`，均按原 `1e-7` 门观察。它们不是连续 Fourier 尾界。

最后保留资格的原读数还有：abs-y `0.3925954703533752`，ball radius `1.0114938450973032`，det-min `0.9054719913897016`，mean-E `[0.9982473616809218,4.473445890849071]`，z-min `.02`，采样 curvature-max `16.45162133796239`。原 fine η-grid=`0.1991728488245286`；1558 个真实峰全闭后 η 才成为上表的 `0.19917454273148172`。该定位新增目标 10,290 次、40.668994466000186 秒。保留 scan 和 observed summary 与最后接受 checkpoint 逐项相同。

## 4. 最后保留点、当前库和未付资格严格分开

| 对象 | 数量 / 原身份 |
|---|---|
| 当前保留物理 q | 81 doubles / 648 B，SHA256 `cc117d48551e8b457bda12450e466f7e2dcff174311675b5e3445487bc9c6a30` |
| 当前 coarse 半径 | 817 / 6536 B，binary64 SHA256 `5aa6b17662003fddff6f552c212d368b8af2226240ffc3c59e3fd16a8aedb849` |
| 当前必需 fine 半径 | 1636 / 13088 B，binary64 SHA256 `df0f7caa447a3f57536731360a128b9a706d15f293e9b176f33d7de68c0c7d28` |
| 保留点已经完成的 fine 半径 | 1630 / 13040 B，binary64 SHA256 `06628dc4f5a683a451c3af96e2c99f62b08f961c6614425c6de4e46f9b04c5af` |
| 当前物理峰轨道 | 1829；canonical JSON 86923 B / `bd7c8d4225aff8c05bef89b19e35ebbda7cf619201cf1c7e6e2a4a087663e093` |
| 当前 working 行 | 334；canonical JSON 103117 B / `9c74630ab5c93f5d21106acea04eeaae13e4f33e3a0031e60cd5758d709bb356` |
| 两种 unapplied 队列 | physical=0，working=0 |
| 原 coarse/fine FFT | 1536 / 3072 |
| 保留 observed summary | canonical JSON 2070 B / `068ea83fed4f211fe7b4b28e8dabf60e012f51e0f6c8e5c049a68231e0c537f4` |

后续物理行交换将 fine 依次长到 1632、1634、1636；这些都没有被最后 1630 点的保留资格自动支付。outer20 的新 coarse 在原完整库上确实发现工作几何余量
`g=0.00011692915997574185`，并按原 max 更新 `best_geo`。这不是物理 `geometry_violation_max=0` 的替代量。原算法因此切回 geometry_restoration，extra=`0.010116929159975741`，当前完整值库标记 true，已知原 phase-I scalar rows=2,261,160。

该 `best_geo` 已由输出准确保存为一个 binary64 单值，canonical margin-state 为 515 B、SHA256
`1508f53acf269470e335290cb29eba954a795d39be0c1b528135e349516f208d`；没有此前未输出标量的逆区间缺口。原 actual/proposed trust 都是 `0.45050811767578125`；post-backend decision=false，不能擅自进行 trust 更新。

最后 outer20 backend 入口已在 02:21:46.1694800 UTC 输出：上述同一 q、同一 extra、334 working 行、1636 fine 半径。时钟在它的新 J 构造中结束。此前 outer19 已退休计费部分为 24 个完整 J / 1596 blocks，加其最后 active 1 个完整 J / 84 blocks；最终总 25 个完整 J / 1701 blocks，故还支付了 outer20 的 21 个未完成方向块。该未完成 J 没有输出矩阵，不可伪造为可恢复的完整矩阵；其时间包含在总 wall clock，未冒一个完整 J 的 `jacobian_seconds`。

## 5. 最后 raw 和最后完整 trial 都不是保留点

最后 raw backend 点是
`5fc69e2cc829a14e1b85cbb5402d93d051f6c8e5b2a06891847146eaa1b8dd99`，
extra=`0.19541137526650026`。原 working 最小行中 metric-minus=`-0.0013076547304350372`、metric-plus=`-0.0009078322158360685`、curvature-plus=`-0.0005439267302909103`，所以原 raw 未通过。

同一 callback 的 fraction 1、1/2、1/4 依次检查；前两个工作违约为 `0.0013076547304350372`、`9.255392129403541e-5`，1/4 工作门通过。最后完整 trial 是
`5e199a34fe6da721628a98fcf9971d8a5864acea19a681b019dc03eff4e3a843`，
extra=`0.19823375836523635`，outer19 / metric / fraction `.25`。
其完整 1634×3072 fine、nested、1516 个局部峰都已经完成，remaining=[]，没有可续的局部峰队列。

这个 trial 的物理 box/geometry violation 都为 0，峰后 η=`0.19818589327629638`；但原 curvature-plus 工作几何余量峰=`0.0001248759423130288`，违反原 margin 门，所以准确 reason 为 `complete_fine_or_real_peak_epigraph_rejected`、accepted=false。不能因为它 η 更低而替换 `cc117d48…`。其新物理/working 证据已经进入下一库，最终 pending=0 说明已经应用，并非无新证据。

最后 raw/last-trial 字段仍指这些 outer19 点，而当前 backend anchor 已是 outer20 的保留点；三者必须分别恢复，不把旧已拒 trial 当成新的未决点。

## 6. 真实 native H 与 pending secant 的语义

原 source 的 H/pending checkpoint 完整恢复，但完成 source restoration 后，首个新 QP 已从 phase I 切入 metric。原 helper 准确执行一次 semantic reset，首个 `R566_TRUE_SECANT_INITIAL_H` 明记 `original_identity_initialization_no_unlogged_H_restored`。所以本段并未谎称把旧 restoration H 当成 metric H；后面保留/更新的是本段真实已付 metric Jacobian 和 QP 所产生的曲率。

最终 checkpoint 身份如下：

| 对象 | 原身份 |
|---|---|
| 全 checkpoint canonical | 83951 B / SHA256 `5194fe701ef8f005ec6e30a7a15e1cc3e235fbf66d8a32db8e6d54173f86c897` |
| payload-without-receipt | 83828 B / SHA256 `7df4603a509d6b1b718276b8f48df8e78c4ebecb86a1358004654a0a8d7c02f4` |
| packed LDL | 3403 doubles / 27224 B / SHA256 `6f2a9a605c4485364a5666501b7a77b13ad2ff6c3eada967a59fe460a9d132e8` |
| 原模型 identity | `8a1abe70f785c8c1d8e80b884aa58299598846c716c1be63b0d7b3e9421414a7` |
| 已存行函数 signature | `505f8cbcb0a22bc114da97754d0903cee340381ff6237c868c947f04e71452c5`，metric 语义 |
| pending 固定乘子 secant | canonical 6128 B / `c6464b1133b65a6fcb6190a0120e09f155c7802317df3cda4ab2e0b8c7a08551` |
| pending anchor | 82 doubles / `73e9fc8768c949d44e3c37add2f5a132cb10e8cfea5410a1c1a845cb66018fe6` |
| pending 固定乘子梯度 | 82 doubles / `3547277238eadddbc60eb125767293d92ee687ba843a4ce015fb6e0d2d6afab9` |

pending 含 23 个准确非零乘子；backend number=20、native major=1、mode=1、reset counter=1，原 row-order SHA256
`aa4d5d9b04d1b36552f7f0b08d0477caa9aebe8a2d788236652f38414e7ad104`。
其 bound 项仍是线性的固定乘子零 secant。

最终 `last` 是在同一已付完整 J 上准备初始 H，secant reason=`zero_unresolved_or_nonfinite_actual_secant`；当次原 eigenvalue 观察 minimum=`1.0000000020976453e-6`、maximum=`25.584497582713514`，本次 seed 未 clip。没有另跑谱诊断或新 J。

到 outer20 的 geometry_restoration，新的完整 J 尚未完成，故最终 checkpoint 仍是上述 metric 语义。这份真实状态应完整带入后继，但原 helper 必须在新 phase 识别语义变化后按原规则 reset。它不是完整原 SLSQP native workspace、不是新 geometry H、也不能把未消费的 metric pending secant跨目标使用。

## 7. 全部本段费用与旧账

本段原科学 elapsed=`2370.523698866` 秒。完整 cost 对象 canonical 29,530 B，SHA256
`3efa1236aada84335f7407b8444c2da40f1be6affc093ffc510e638cd97227cc`，包含以下当前账、native 构建账、完整上一自然终态账以及此前费用链。

| 当前计数 | 原值 |
|---|---:|
| outer started / completed | 21 / 20 |
| metric / restoration 接受 | 12 / 1 |
| backend callback / backtrack 值试步 | 25 / 59 |
| working 恢复 / backtrack exhausted | 17 / 0 |
| 缩步完整真接受 / 同 backend history 延续 | 9 / 5 |
| complete coarse / fine scans | 70 / 22 |
| complete localizations | 23 |
| 新 localizer candidates / completed / unresolved | 29818 / 29818 / 0 |
| 新 localizer 点目标 | 212450 |
| 原 9452 bracket 复用 / 原剩余 bracket 新完成 | 9452 / 2561 |
| source full fine/nested 复用 / source 定位完成 | 1 / 1 |
| source 待决候选真接受 / 达到 restoration | 1 / 1 |
| coarse required-row / fine required-row 拒绝 | 3 / 3 |
| nested 拒绝 / working value callback 拒绝 | 0 / 0 |
| physical / working exchanges | 16 / 20 |
| working / coarse / fine epigraph lifts | 13 / 14 / 13 |
| lift 后原 working rechecks | 40 |
| 已付 current complete selection 重跑避免 | 3 |
| working value keys | 125 |
| 完整 working Jacobians / paid direction blocks | 25 / 1701 |
| 完整 Jacobian seconds | 959.6854150519999 |
| backend natural returns / 新 restriction observations | 0 / 0 |
| 原 best-geo 逆舍入恢复 / seconds | 1 / 0.0001317709999852923 |

native 当前账：backend calls=21、native calls=30、实际 QP observations=25、seed preparations=20；固定乘子 updates=11，其中 damped=9；native gradient 已消费 pending=5；skipped=8；semantic resets=1、invalid identity resets=0、eigenvalue-clipped seeds=1。新增模型 value/Jacobian 均为 0。native 调用时间 `0.11155620000067756` 秒，seed 时间 `0.053480466999985765` 秒，均包含在总 elapsed。

本段官方 native 源 fetch 4/4、compile 1 次；fetch `0.7237592389998326` 秒、compile `0.8488209429999642` 秒、总 build `1.6040911909999522` 秒。实际二进制 52,080 B / SHA256 `83652093638515310571078e19b5934d1d3ec4b107373bae71c8ed15dd5664c4`；保原 SciPy BLAS/LAPACK，numeric probe calls=0。未把新 job 必需的原二进制重建漏出费用。

oracle 只按 live/retired 各计一次，原完整总数如下：

| oracle 量 | 原值 |
|---|---:|
| constructors completed / constructor seconds | 272 / 106.71543300500247 |
| FFT states / uniform geometries | 3192 / 3192 |
| primitive Fourier fields | 28728 |
| exact core arclength points | 1297221 |
| nonuniform points summed | 1376942 |
| uniform points gathered | 579214 |
| point evaluations / point values | 218002 / 1956156 |
| point parameter directions | 4326960 |
| point sets / point subsets | 212752 / 4710 |
| prepare seconds | 1108.5808292020106 |
| point seconds | 956.1193844499735 |
| point-set seconds | 76.01468654898753 |
| diagnostic uniform FFT | 0 |

这些分类时间可能包含相应调用的重叠部分，不能再相加成第二份 wall clock。未闭操作的时间已经计入 elapsed；未闭的 21 个 J 方向块不会伪记成完整 J。

此前已记录科学秒数下界为 `19470.098158644`，连本段是 `21840.621857510` 秒；仍是下界，不把更早被删失的工作恢复成准确总时长。旧 source 的 5 次接受、旧峰定位、全部旧 J/FFT/native 费用留在完整嵌套账中，没有被新计数清零抹掉。

## 8. 真正可续的当前状态

本次没有留下未处理局部峰。原 2561 范围已付完，旧 trial、旧 fine1630 和已闭峰不再重做。下一正常范围应直接消费原 `cc117d48…`、817/1636 半径、1829 物理轨道、334 working 行、准确 `best_geo` 单值和未完成 trust 决策；原最后真实资格保持在其 1630 网格。

已知当前 complete value library=true，原 phase-I extra 和 2,261,160 个标量行计数已输出，因此不须为了重新确认这些值重跑一份旧 coarse 选择。未保存的完整 working J/native workspace 可以在新真实 continuation 中必要重建并完整计费；原 21 个部分方向块的费用继续保留，不能宣称这些矩阵已经恢复。

原 H/pending 完整载入，新的 restoration 行语义按原 helper reset，随后仅用实际新 J/QP 更新。真实新 trial 仍须原完整 coarse、当前 fine、峰、nested、工作 margin 和实际接受；不把未达 fine1636 的当前点当成已达，不降低 margin、不改变 η 目标、物理盒或 reach 门。

这些是下一原正常续算的输入边界，不是新算法失败诊断或另一次旧试验。当前静态设计 metric 仍随 q 变；本收据没有授 fixed metric family、全域 reach、全时嵌入或主 README 完成。
