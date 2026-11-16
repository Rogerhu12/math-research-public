# R133 supplement: actual complete positive-weight mean and whole-error refinement

2026-11-16. **一次新计算完整成功，42个新记录冻结。新的整个算子上界仍不构成高门或有限逆。**

公开仓库自身 [run43840219992/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43840219992) 成功；事件 `f7f77c5fdfee28a66451d59bd519b60c711699d0`，真实科学 checkout `dfd6759e8b8b6e1d4b596391a0b56b908d7e3eb6`。一个新科学子进程，18门全通过，7完整图/42个新记录，恰2次新指数；新开方/幂/对数/求积均0，旧科学调用/重算/native恢复均0。全部69旧record和原完整限定条件、失败/成功状态保持。

## WMRA1. 完整原字文件与实际核验

| 文件 | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| [完整科学结论](../notes/positive_weight_physical_mean_refinement_ci/run-43840219992-1/actual-scientific-conclusion.json) | 5fdb01ed62008489bca34a4b6231519af4f60793 | 51030 | 39a2d96accdbe1b4a8073674cabeda97878876f11fc24a055b910ed61567b432 |
| [完整执行回执](../notes/positive_weight_physical_mean_refinement_ci/run-43840219992-1/execution.json) | f22c1de0f0afa6597122c5f31224bde85ed63ac0 | 19357 | 0c181a2011331e176b1aca734157bd9b8ef4dc909b441ae75f50b447477d0dad |
| [原运行报告](../notes/positive_weight_physical_mean_refinement_ci/run-43840219992-1/report.md) | 33db82c7343d7b78b37a3adf7e08361b049c5b78 | 457 | b299ad08f89246b45efe9f24871ab4ab9bf718c76bb893205992b7a96e6ed12e |

三件共70844B。根完整获取三件小UTF8并核字节数/SHA，逐项核32字段、18完整 gate 名称和全真值、7目标顺序/每图完整schema/42完整record槽、全部16项 actual_progress、source/manifest/parameters/actual checkout/物理 scope。没有通过 connector 获取任何 binary、gzip 或大日志，也没有重新评估数学表达式。

19 current 输入总308005B（15旧小科学件、WMR完整proof、新science、worker、reviewed-rules），2 AST只含新science和运维worker，0历史native。完整输入五键身份/次序与manifest原字相等。15个旧件是13个完整图和两个完整原index，不把引用的上游图或整个旧成功链重新执行。

根在运行前从持有的15原文独立构造以下完整对象，运行后再次与本次原对象逐项核同：

| 完整 copied 对象 | Bytes（canonical加LF） | SHA256 |
|---|---:|---|
| 69原 scalar record | 8161 | 53bb5d205aeb6ca54b773deb0b2653dadfbc1f2455970b800952847512bd6207 |
| 原scope递归投影，含669个非球叶及所有混合数组位置 | 20489 | 9ef5639d34b98ae02d341dd53026f03bb20efe67caacab812699b7e7f69e333b |
| 两原index完整准入投影 | 4623 | 38344c686485fb0e8940ff7e03d8e4fc1c8d3397c4cfbb3ff73e1fd17d525cfb |

scope投影只去掉原完整ball字符串叶及由此形成的纯球子树；原来空的容器仍保，混合数组原位置以null标出球叶，其他叶全部原字。它没有删除自由尾双符号、Bessel/integral96/HS条件、J/mean/jet或原失败资格。所有13原图的完整输入映射、科学模块映射、参数 hash、直接依赖 receipt 与原index相互核对。669专指这13图conclusion的原非球叶；共同参数、总体scope及额外续量参数另完整保留，不在该图叶计数内。

原43827705714/1继续保持 failure/27门/23完整node与原 `unpaid derivative of strict_phase_derivatives: (0, 0)`；原43831678361/1保持成功/9门/3完整node。前者的39个已成partial和后者的30个续量仍按 WEJA/WECA 原记录保全，本次不重算任何一项。

4次成功真pull的两README actual diff及相对明确已读规则diff均空。最后真实pull `2026-11-16T09:30:07.754563+00:00`，head `dfd6759e8b8b6e1d4b596391a0b56b908d7e3eb6`。根独核4步完整回执 hash chain `c409375d1b4a73205497909f209ef605c80e5830e9f5b5cd2f3654ee57d53061` 及readonly preflight原 `7134B/bf80e2a72b481f56dfe7809e2a209575cb20bfe29988173e79de1ba47d45dc3b`。preflight没有flint import；一次新science按Python3.12.14/python-flint0.9.0/320bit执行。

完整科学 stdout `2803431B/0c55e785113531b64615e7a04aefcf6f8e76a7e49523f617af54d46f33de3391` 这里只引用原执行回执；根未读取或独立重建该大日志。所有42record均先原子保存、回读原字、打印完整prefix再供下游；本次child returncode0、无timeout、无遗失新量。

## WMRA2. 与原同一算子的解析关系

采用 [WMR完整正权均值证明](R133-supplement-positive-weight-physical-mean-propagation-and-complete-error-reassembly.md) `550866c05d9a07d3e4b037e5840a4f75b66a7f3a9304c5cd0d52e4f2b7e729a6`。正weight为原 \(w=1-\alpha uIv\)，概率测度用同一 \(aJw/D_J\)，先精确取消共同角weight，再取完整界；没有把原非加权均值等同于该概率均值。

严格段与局部段分别使用事先证明的 \(U=7/4,\delta_w=79/128\) 和 \(U=1,\delta_w=3/4\)。局部三个原ball严格小于1、1/2、1/2的资格本次实核。metric Gauss恒等式给出的 \(\beta\ge0\) 只用于原实际负侧区间，没有移授到根右侧。

完整绝对均值系数与向左传播负部系数分别计算；只后者进入两个新指数。先接root初值0到local，再接strict，原ordinary-dr长度和实际root上端保持。\(z_r\) 仍用完整绝对系数，不能因指数变小省去其导数费。

随后完整重组仿射残差 \(g_1=JQf-z_rk-z((D_0-E)k+b_1)\)。\(k_r\)、\(\beta_r\)、\(J_r\)、\(e\)、\(b_1\)、\(R_0\) 和独立两mean均保。旧B/T/profile/N6、3070真接口及全部跳跃、radial powers、Bessel和dyadic输入权、PW原cut与原完整接收列均直接读，不重新生产。

四个原腰端点中三个非mean贡献保持原字，mean端点用新的同一物理mean和原完整two-mean vector。最终whole始终含完整Calg及RF；reduced只在原精确finite因子已保留的意义下比较同一个reduced算子。旧left-readout/right-input的有序整乘积只读一次，不改变输入空间或反射子空间。

## WMRA3. 七完整图的42原新记录

下表全部从本次实际SCI复制，不在本页再次计算。相近的whole/reduced球即使显示相同midpoint，也仍是两个不同算子的完整上界。

### strict_positive_weight_coefficients（9 records）

| Record | 完整原 ball |
|---|---|
| complete_Tk_upper | `[290579920106504595416115.971373941173820363633327713312087338304975360978774 +/- 3.25e-52]` |
| complete_absolute_feedback_upper | `[76.9860476622328800852603649454197992142543687863828634289647052518758618152 +/- 3.24e-74]` |
| complete_absolute_mean_coefficient_upper | `[98.3329487641492217749118930993115797456135524319806790033335403371386290730 +/- 4.95e-74]` |
| complete_backward_mean_coefficient_upper | `[75.3307636442709280316098327841007376870757120532206439662859081253666245836 +/- 1.28e-74]` |
| complete_cross_sum_upper | `[109.770164561337196536781773561488476765485407129915096095169864246836547819 +/- 3.43e-73]` |
| complete_curvature_cross_upper | `[51.3842565048370032501352202193009054000822190682544018178736233162284366618 +/- 2.55e-74]` |
| complete_drift_cross_upper | `[58.3859080565001932866465533421875713654031880616606942772962409306081111575 +/- 1.72e-74]` |
| complete_feedback_quotient_absolute_upper | `[182.817481820900774135545152099626899063064963451001674685844843336646558492 +/- 1.01e-73]` |
| complete_feedback_quotient_negative_part_upper | `[177.855456504445077933013506530006645898508001425685218989642311691076938239 +/- 6.46e-74]` |

### local_positive_weight_coefficients（9 records）

| Record | 完整原 ball |
|---|---|
| complete_Tk_upper | `[241.698502988092961457952383580744837525077517283539915120133621625136067937 +/- 2.35e-73]` |
| complete_absolute_feedback_upper | `[0.636116023439896048824370704588593524576662372274835330188940833570291692802 +/- 3.27e-76]` |
| complete_absolute_mean_coefficient_upper | `[0.972786042432533085669751276572075950465393784588497508745525780028435252330 +/- 1.88e-76]` |
| complete_backward_mean_coefficient_upper | `[0.0744182187604228076541233087552601912433290389415019968556075002369583594684 +/- 1.33e-77]` |
| complete_cross_sum_upper | `[0.132488000025011236933668171419621594548909835171390712660760376724121207538 +/- 2.08e-76]` |
| complete_curvature_cross_upper | `[0.0874641419233388896921795248228874462210098659613981318512299154062225586966 +/- 3.8e-79]` |
| complete_drift_cross_upper | `[0.0450238581016723472414886465967341483278999692099925808095304613178986488416 +/- 7.07e-78]` |
| complete_feedback_quotient_absolute_upper | `[1.50998400003334831591155756189282879273187978022852095021434716896549494338 +/- 4.28e-75]` |
| complete_feedback_quotient_negative_part_upper | `[0.176650666700014982578224228559495459398546446895187616881013835632161610051 +/- 5.61e-77]` |

### two_patch_backward_mean（6 records）

| Record | 完整原 ball |
|---|---|
| complete_local_backward_factor_upper | `[1.00000028388308288925959505585518451135900315172792465203070013567312018311 +/- 4.61e-75]` |
| complete_local_mean_derivative_upper | `[5577650099503729785262872889124336621822637370965958332677194882.26361586956 +/- 2.79e-12]` |
| complete_local_mean_upper | `[21276978686823711635921136703414754940920468769374081498449.0215928470113911 +/- 1.24e-17]` |
| complete_strict_backward_factor_upper | `[62980217.5135088039076736593556811332831932928659867020838659113923402506100 +/- 1.76e-68]` |
| complete_strict_mean_derivative_upper | `[5.11460524205457102552674702712470170192331178715199023208439135553542219212e+402 +/- 2.24e+327]` |
| complete_strict_mean_upper | `[5.20131380465118738271036448144502131575752769827881167250139784273478278159e+400 +/- 2.49e+325]` |

### complete_affine_mean_sources（4 records）

| Record | 完整原 ball |
|---|---|
| complete_local_primitive_mean_source_upper | `[4299192567577576181501537604103129676007903639803486524178634567.04037071910 +/- 1.68e-12]` |
| complete_local_raw_mean_source_upper | `[17196770270310304726006150416412518704031614559213946096714538268.1614828764 +/- 1.45e-11]` |
| complete_strict_primitive_mean_source_upper | `[3.77849337451120792846742772963730094187773488263455062205453538797659351345e+423 +/- 8.46e+347]` |
| complete_strict_raw_mean_source_upper | `[1.51139734980448317138697109185492037675109395305382024882181415519063740538e+424 +/- 3.39e+348]` |

### complete_negative_receiver（6 records）

| Record | 完整原 ball |
|---|---|
| complete_collar_ordinary_source_upper | `[3.60034789992317551329532867950316880285413816791565979668777078583723196589e+456 +/- 3.83e+381]` |
| complete_collar_raw_mean_union_upper | `[1.51139734980448317138697109185492037675109395305382024882181415519063740538e+424 +/- 3.40e+348]` |
| complete_collar_received_with_jumps_upper | `[5.18941275711413420870261515948030316341888363286867179491192589944913318308e+458 +/- 4.05e+383]` |
| complete_same_negative_error_upper | `[5.06071589111212565573367359488129891872440419410389049081025637627973793715e+458 +/- 4.65e+383]` |
| complete_strict_ordinary_source_upper | `[3.02911029418688735387366118604833520916260978329118947597771167750190612971e+449 +/- 8.13e+373]` |
| complete_strict_received_with_jumps_upper | `[5.80985852444328926609914974909315115187113196063089834938682939653897656902e+451 +/- 4.47e+375]` |

### complete_waist_endpoint（2 records）

| Record | 完整原 ball |
|---|---|
| complete_physical_mean_endpoint_upper | `[2.43924335652810735482987923994457578736594516879555199109787915822882083678e+395 +/- 2.43e+320]` |
| complete_same_waist_endpoint_upper | `[2.43924335652810735482987923994457578736594516879555199109787915822882083678e+395 +/- 2.44e+320]` |

### complete_whole_and_reduced（6 records）

| Record | 完整原 ball |
|---|---|
| complete_all_source_sum_upper | `[5.06071589111212565573367359488129891872440419410389049081025637871898129368e+458 +/- 2.77e+383]` |
| complete_nonroot_source_sum_upper | `[5.06071589111212565573367359488129891872440419410389049081025637871898129368e+458 +/- 2.76e+383]` |
| complete_reduced_received_source_upper | `[2.11631251214066700786838853877545268179558414845358793305713600692778363235e+465 +/- 2.20e+390]` |
| complete_same_reduced_error_upper | `[2.11631251214066700786838853877545268179558414845358793305713600692778363235e+465 +/- 2.21e+390]` |
| complete_same_whole_error_upper | `[2.11631251214066700786838853877545268179558414845358793305713600692778363235e+465 +/- 2.22e+390]` |
| complete_whole_received_source_upper | `[2.11631251214066700786838853877545268179558414845358793305713600692778363235e+465 +/- 2.21e+390]` |


## WMRA4. 完整候选选择与仍未通过的义务

同whole比较只在原whole与新whole之间；同reduced比较只在原reduced与新reduced之间。两次实际选择均为 `new_positive_weight`，全部旧候选记录和新记录都保留，未减两个上界。旧whole原球仍为：

`[4.34242640404715535961649286895103269030800753348757717731203810841406429941e+341224436 +/- 1.50e+341224361]`

新的whole原球是：

`[2.11631251214066700786838853877545268179558414845358793305713600692778363235e+465 +/- 2.22e+390]`

新的reduced原球是：

`[2.11631251214066700786838853877545268179558414845358793305713600692778363235e+465 +/- 2.21e+390]`

这些是保证的上界，不是误差的下界。不能由数值很大推断真算子奇异或真实误差很大，也不能由较前一上界明显减小推断充分高门通过。实际已成的主要变化是传播因子被完整正权估计控制；原完整源/N6输入费用仍按其旧球保留，后续进一步细化必须另定义新的完整目标。

本次没有证明通过的高cutoff、实际signed有限逆或full incoming inverse，也未支付正/负径向head、\(\nu\)与两mean Schur、真实physical96数值基底/\(\Theta\)全部cross、背景/tame/nonlinear matching。几何条件和最终同一闭嵌入 fixed-metric 族仍按README原验收；绝不改变固定 \(\eta_0\) 或变 \(\nu\) 冒充族IFT。

## WMRA5. 冻结包与保存范围

| 冻结件 | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| complete science | 96f8b9ba66d63876733091d00774e382c18f045a | 62958 | e8c3ca95c8ed306fa887a910c5b36ec93e25f2bdef7ad67aaebfef4ba88b4ffc |
| shared worker | f966a6a05b18794927c3674956fb617e7dbaa244 | 25584 | 7abb8783fc3ffc9f3194bb9cab8e1d8c12d28395b9e4b0981c682c879aa39d18 |
| complete manifest | c1ac2a001fc0003a2f5a78a6e6a2b8e31382b150 | 17404 | eccd4b2342dd8ce8d5977d7986e523581597a61664eb72bb755b7f8bcb2a356c |
| workflow | 5becfacc96a36a4ce556a2bd7f67d1526600e19c | 2990 | 958a452efe98a3c748afbe2e833e611101baa6c3cce879d1b8ad907587e63986 |

已消费marker `dfcf12c6fa9215b1c595af1d13e51cd08aa6b2f8/663B/e8dbca6e48aace618dbbfa98f9c84bbc44df20fc3877a775e29caa274bfbf8eb` 在原run前持久推送，阻止同目标再次执行。本次完整7图42量从此冻结；旧scope、原失败及全部完整结论不得改写。

启动前topic199693939B，完整130000B输出预算另留120000B；实际3件70844B均完整保存。新array/data/Release/artifact均0。root只作文本、身份、schema与hash核验；新算术全部来自本公开仓库Actions。未达总验收，继续后继完整任务。
