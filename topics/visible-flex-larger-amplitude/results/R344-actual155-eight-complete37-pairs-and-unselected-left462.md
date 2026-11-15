# R344：actual155 完整37查询八次真实模型/FD推进，末两批最近拒绝定位到未选LEFT-RMS462

日期：2026-11-15。性质：已执行有限模型、原非线性试步和FD的原输出结论；不是完整BVP、native或闭面接受。

## 1. 结论与实际来源

actual155 从仍可取的actual98真实原父对另起37查询轨迹，完成8个 fresh 完整模型与8次独立原FD读回。全部批次有一个原接受步，alpha依次为：

`[0.125,0.25,0.125,0.25,0.25,1,0.25,0.5]`。

总共访问23个原非线性试步，8接受、15拒绝；原17档预算并未被缩减。最后是既定 maximum_batches=8 停止，原退出码0；没有把8次有限模型改善升级成完整原问题成功。

最有区分力的新结果是：batch6最近拒绝alpha=1/2、batch7最近拒绝alpha=1，37个已选查询的全部2048角都有效，原merit也下降，但完整原RMS复核分别只在未选 LEFT-RMS462 失域。它与早期若干已选查询非线性弯曲失域是两个不同责任。此次增加MID489和MID490确实扩了完整输入capture和B支持，但不能因此保证所有原RMS查询、全步或全局收敛。

- [实际run43726543241](https://github.com/Rogerhu12/math-research-public/actions/runs/43726543241)，source `0aa9dca2d8029721cd1e820948699206a7da4388`。
- compute job `132849600659` 实际success；无独立report job。所有读回均来自该job原日志。
- 完整原compute log：3294582字节，SHA256 `384cee41415ce6cb1e20bd3e429f882498a829534e7df8446ffd708df88f240f`。只取一次，没有重新下载任何大科学包。
- batch worker SHA256 `0e5ded8435cd31b7dbedb31dc15a36239ca946f80a346c0c5104cb703f86a89d`。
- request SHA256 `4349e1b343bb655b18a233cb68a0f2a8a59bcfd929b06b3ac49e073ccaa2e295`。
- base recipe SHA256 `f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea`。
- complete readout helper SHA256 `f5d598cdde4c46d2904eea2ef0d20b6009e8eb284ee9a2f6f18d20cbdfc582b7`。

## 2. 真实输入与37查询责任

本次没有采用已删actual141末warm，也没有从其哈希“恢复”状态。actual141/R333只用于选定新增MID489、MID490。当前first parent仍是actual98的原31-query父：

- run `43677587785`，artifact `14147700690`，name `visible-followup-condensedqp-43677587785-1`。
- 原ZIP809042943字节，SHA256 `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`。
- Actions完整size/SHA与457个central-directory metadata已核，只解原warm/status两成员并核其CRC；没有宣称其余成员全部解压审计。
- warm：4927052字节，SHA256 `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`。
- status：3379453字节，SHA256 `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`。
- 两文件原bytes复制，未JSON重序列化；父本身不是native/fullDN接受锚。

四数学输入在该job从历史 `918fdb11dbb7a424b6149b405e2c7fab3cc0c737` 按原SHA恢复：accepted `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`，prepared `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`，tail-anchor `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51`，config `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。它们仍分别2614352、4220043、6815、2161字节。

原启动校验有85项既有源、5项新增查询/读回源、1项独立编排源，共91项显式source pin，另有1个参数recipe。公开源未在本读回中修改；本地只处理JSON/字节，未运行科学或重算模型。

完整37查询是21个LEFT与16个MID，每项全部N=2048角，总75776个B行：

- LEFT：463,464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487；fraction原word `0.17267316464601146`。
- MID：471,472,473,475,477,479,480,481,482,483,484,485,486,487,489,490；fraction=0.5。

相对原35确切只加MID489、MID490；相对首输入actual98的原31集合，新增还含LEFT463、MID471、MID472、MID483。两种参照不能混写。

完整capture新增interval489、490以及node489、490、491；现24个unique interval、29个实际endpoint node463..491，完整B局部坐标9805。原C支持4059不变，全部236036原变量、完整原A/AT、g、W、S、H、109个free-core和外部条件恢复都保留。没有将“新增两个标签”冒作实际两端输入与导数已经捕获。

每一批重新计算本批J/权重/B/C/凝聚模型，再用实际输出warm/status原bytes作为下一父对。七个独立status/model关系字段及八次父对串联已逐字核同；未要求不同run的浮点数组或固定权重merit完全相同。

## 3. 八次实际接受与FD

表中W前/后只在各自同一冻结权重模型内比较，不对跨批W差作科学减法。physical max为原接受态全collocation报告；FD为实际本批重新支付的第四阶相对方向误差。

| batch | 已访问trial数 | 接受alpha | 本批W前 | 本批W后 | 接受physical max | 原FD第四阶误差 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 4 | 0.125 | 43.36300372909822 | 43.33605694766007 | 0.007107481419522546 | 8.7019221818232e-10 |
| 1 | 3 | 0.25 | 43.33456976744222 | 43.28585055875668 | 0.0071071852119354234 | 8.917585068991029e-10 |
| 2 | 4 | 0.125 | 43.28057984612335 | 43.259491029560984 | 0.007107038008082425 | 9.99269334313201e-10 |
| 3 | 3 | 0.25 | 43.25889304148275 | 43.225388792823836 | 0.007106742244624268 | 7.222736018938388e-10 |
| 4 | 3 | 0.25 | 43.22259857065184 | 43.19404702991091 | 0.007106427751476115 | 7.070690710851065e-10 |
| 5 | 1 | 1 | 43.19145189347684 | 43.10940853870894 | 0.007105108689841186 | 8.062709920950109e-10 |
| 6 | 3 | 0.25 | 43.10029022914125 | 43.0900111872662 | 0.007104760165716536 | 1.0465268241594862e-9 |
| 7 | 2 | 0.5 | 43.08872613662628 | 43.06902479892305 | 0.0071041184748284756 | 7.11083854306579e-10 |

所有8次FD implementation_check_passed=true，原阈值5e-5，二阶收缩检查true，left/right offblock最大0，right rows只依赖原右端。每次原模型和FD子进程均exit0。该FD检验的是原完整prefix/边界接口的本批数值实现；它没有在当前H求解真正非线性native尾，也没有做新fullDN。

初始physical max=`0.00710763096028075`，末接受值=`0.0071041184748284756`。八个基点和接受态的最大位置仍为interval461，原row155819；完整原midpoint station=`1.1420257707426757`，left/right station=`1.139533544992796`/`1.1445179964925558`。最后一批冻结行权为198.92244086337718。这是有限残差尚远未到原接受的具体读数，不由W改善替代。

所有接受态：原699节点/698midpoint域、两组各698点RMS、4096角rho guard及边界/常量责任均由原流程检查；完整常量collocation残差为0。全部37 selected negative/nonfinite计数均0。最后边界最大原值 `4.588832281213329e-14`。

## 4. 全部访问序列与最近拒绝

23个访问按批为4,3,4,3,3,1,3,2。每批从alpha=1按原减半；在接受后没有执行更小档。以下列出每个已拒绝alpha及实际域责任，不补算未访问档：

| batch | 拒绝alpha及原主要失败 | 最近拒绝 |
|---:|---|---|
| 0 | 1：MID487；1/2：MID471；1/4：LEFT464和MID471 | 1/4，两者均已选 |
| 1 | 1：MID471和MID481；1/2：LEFT463 | 1/2，已选LEFT463 |
| 2 | 1：MID471、472、475、480、484；1/2：MID471；1/4：LEFT463 | 1/4，已选LEFT463 |
| 3 | 1：MID471和484；1/2：LEFT463 | 1/2，已选LEFT463 |
| 4 | 1：MID471和484；1/2：LEFT463和464 | 1/2，两者均已选 |
| 5 | 无；alpha=1原门通过 | 无拒绝可归因 |
| 6 | 1：MID472和未选MID488；1/2：唯一LEFT462 | 1/2，未选LEFT462 |
| 7 | 1：唯一LEFT462 | 1，未选LEFT462 |

表中最早因midpoint非有限RHS返回的试步，没有声称其后未执行RMS查询也全部有效。完整原JSON试步已在compute语义流中读回；这里保最能决定后继的原具体责任，不在正文复制每个角数组。

前五批最近拒绝仍证明“所有线性reserve非负”不能自动控制已选查询的完整非线性域。例如batch0 alpha=1/4，原linear reserve最小 `0.00031830973391744344`，但LEFT464 beta²最小 `-0.26830868995975865`、MID471 beta²最小 `-0.1916700127543356`。这属于已选查询的非线性弯曲/有限输入形成责任，不能靠把同一查询重复加入解决。R353/actual166的独立同起点诊断与之相关，但两run的原数字末位不同，不称数组逐字相同。

### batch6最近拒绝

alpha=0.5时：

- 原W=`43.079868618560475`，基点W=`43.10029022914125`，原merit下降。
- 全37 selected beta²没有负/非有限角，linear reserve最小 `0.0007579393025166562`。
- 原节点和midpoint域均有效；唯一RMS失败是左组interval462，右RMS组0失败。
- 原失败station=`1.1453786775070438`，left/right=`1.1445179964925558`/`1.1495024479923157`。
- beta²=`-1.7827069382052452`，phi=`0.030679615757712823`。
- 原scalar a=`1.1943983826095326`，ap=`-0.01211130450236533`，app=`-2.499816638654787`，curve_curvature_at_minimum=`0.006078661801960125`。
- 原流程因这一完整RMS责任拒绝，随后alpha=0.25接受。

### batch7最近拒绝

alpha=1时：

- 原W=`43.05053034157587`，基点W=`43.08872613662628`。
- 原实际merit reduction=`0.038195795050405934`，predicted=`0.039017894732829926`，ratio=`0.9789301886210618`。
- 全37 selected、原nodes/midpoints、边界和rho有效；linear reserve最小 `4.440892098500626e-15`。
- 仍只有左RMS interval462失域，beta²=`-10.25057313338912`，phi=`2.9728547669223726`，同一原station。
- 原a/ap/app与上表同；curvature=`0.0030231130855458933`。
- alpha=0.5随后接受，W=`43.06902479892305`，原actual drop=`0.019701337703224908`、predicted=`0.019729892547084498`、ratio=`0.9985527116383708`。

所以本次末两批具体缺项是LEFT462，不能偷换成MID462或将既有LEFT463重复加一遍。batch6较远alpha=1还有未选MID488，但它没有阻止本批更近alpha=1/2以外的原因分离；本结论不因此自动再加MID488。

## 5. 预算内QP、完整外变量与未付最优性

原lambda=270、working rows512、dual sweeps200全部不变。八批local_QP都明确 maximum-working-row-budget，最后stage511、maximum-dual-sweeps、completed_dual_sweeps=200。完整H的条件恢复与全A/AT/B/BT实际终读都完成，未冻结局部以外变量。与此同时，不能把它们当原QP精确最优解。

下表只抄原终读的ordinary-float stationarity与posterior gap；它们不是严格外包或新的接受门。

| batch | 原完整stationarity L2 | 原cross-point gap |
|---:|---:|---:|
| 0 | 0.032415325334948446 | 3.626212219387526e-8 |
| 1 | 7.439949034715105 | 0.0003854858525969007 |
| 2 | 1284.424071954031 | 11.315948322683418 |
| 3 | 4515.913586268681 | 139.87537671279208 |
| 4 | 6276.2784409011765 | 270.17886970933705 |
| 5 | 10306.613485005833 | 728.578516327163 |
| 6 | 19349.612790547002 | 2567.9550595072765 |
| 7 | 19956.319940304562 | 2731.5159256982456 |

后段这些原诊断变大，说明“有原非线性接受步”并不自动支付模型最优性；也不能从raw-float gap直接推出实际解距离或失败根因。所有full_QP_optimality_claimed均false，原完整g保留，原final选择可能改变条件恢复，原门没有被这些诊断替换。

## 6. 真父串联、末文件及清理

八批产生的原pair身份如下。每一行warm准确等于下一批input warm；status亦按该次原字节传递，不把重序列化后的摘要当父。

| batch | 原输出warm SHA256 | 原输出status SHA256 |
|---:|---|---|
| 0 | `62efb083a975ca8664c7fdcfa7f4fbd03b897e0b2c92603051e010e217c8069f` | `de7b246045b58ca9d601a7949096d46c7c8b50a6f5315558a0f5a1618c9a9267` |
| 1 | `e6e2a7ba64fa3762c68d87dfcecf3455d2fe07445aa139d79e2229d80270f598` | `780a145035ddc43009086025145e866b8b5a18569dfd1133c478084be43a62b8` |
| 2 | `cd04ecd86215e7346e175d692e4de1d344ce66cf4cf47b2735d527522f5a922f` | `a98ae0e5aa20d6f6ec0db3f9566ebb7534f92ba972308e9bf0c9a9decabf62ce` |
| 3 | `e76ced40a3e1583cffdfae5a0ec619c2f632749a2c61404da1bc41abef544719` | `1612504b1b4fef8d19e347013a8fd9371b1bbee5989c62e558feb9687cf2b129` |
| 4 | `3b62bc5469fbd1615c14976bd16bf4c3203a7e627f0be997e0b653e68bb09786` | `d2dd75d12e92d6a560bbe1444c64776b7fef166d0730221711702c055a0d7f17` |
| 5 | `1e1788e5ab5edbbed6a95f8d40db25870ce806e8a72e755a9479f192692e72f9` | `fc11bcbae29dfb805edf78ade26db55ea776dd1d55a79f24d3f7864c1a589b01` |
| 6 | `780f99aca433cd1aca5d556fd392511a33cf910f01e892e3c1f2a8115026c0c4` | `8b727fbad8ba1d5e0b18a64d17bae210b8d6c1b14b9da8d556c465ae3bcf4ae6` |
| 7 | `9bba7205ac476aa132c81af825bea5392abd5ebbb85ec9088e85a9ae22183a3d` | `d2040b125e268e46a51405dd87b19994283a728fd8fd2c1ffda6f3d38592c659` |

末warm原5035144字节，status原4993388字节。末三项其它原输出是：

- model-000.json：686321字节，SHA `1aa279dd13e61aef8c8badc1cc7cc86bfc20e1ebcce85d65d546e30e5e980dc7`。
- condensed-QP-summary.json：128693字节，SHA `1cf1392550e9de09684a03deb8f846bda4147166823b1d7f63d2fc870da4d5cb`。
- response-check.json：4326219字节，SHA `f868f9021561902108f3add447eb5c5e75789ff1ca6f3d1bf52d50446e5ae30c`。

原partial field canonical identity `5c565c117072e1c4f7c9eaa19bfadf9d3af2d615ef4b600af9a3e074d4c8eff8` 只覆盖mesh/states/rhs/field_representation/complete_scalar_profile的原解析值，既不是所有raw数组哈希，也不是完整warm文档身份。这里没有从哈希反造数组。

完整print先于move_pair，再清该batch大payload；已搬的parent-after目录也有独立错误读回路径。本轮所有批次正常，完整读回先于清理，最终all_owned_temporary_payload_removed=true。没有raw artifact、Release或Git发布，末pair现已删除，不能把本节的SHA当可直接续接文件。

## 7. 原语义读回与字节范围

所有8份原summary超过普通单帧大小时，编排仍完整逐成员输出；本次重建八份文档的全部545成员，另结束surviving-output-readback有1成员，共546成员。其所有成员byte/SHA、容器子计数和document SHA逐项通过，数字保留原JSON词法，不通过本地浮点重新格式化改变字节。以下身份为“sorted ASCII compact parsed JSON plus LF”，不冒科学原文件的排版字节：

| batch | 语义文档字节 | 成员数 | SHA256 |
|---:|---:|---:|---|
| 0 | 433778 | 71 | `fef0527d5b8ee05c1a04c6d8f8a51c922913ba3a47d0f31488bbd8e95853ff95` |
| 1 | 385053 | 69 | `69e90b08da3ef70aa2d634ce3044153b3d9add3cc04121221e53c1fd1f051d63` |
| 2 | 501908 | 71 | `b21dbf89d49c22784d2a44010101104b6d89a1dff2cd166a4f0d7e638d2ec7ad` |
| 3 | 384993 | 69 | `5a23e09a3eeb938b7babe879dc9794af16f1e5599fca2118577b1d58d35efc34` |
| 4 | 386272 | 69 | `4cda245d1fe2811cab0a674b9cf945fabbac68b12162208bbc611f521a3f6bbe` |
| 5 | 150901 | 60 | `3179dc39d3803c5c7811ad25215c2fb525cb31402d2a2c302dfc35512cf1af35` |
| 6 | 384849 | 69 | `977a1e590431626901b4e10809f917522dd4efd2a43988253d9c4fbb8f70070f` |
| 7 | 283291 | 67 | `55618ce1386b67ee9d8a23cd2ebad347118bd8dc59bb041c58501af291dc0b1f` |

所有23个已访问trial在对应all_original_trials和complete_original_trial_JSON_records中的数量相符；8个model/FD退出码、accepted标志、原七关系字段、37 typed顺序及真实父对链已核。没有重算J、范数、矩阵动作或科学比值，也没有本地审核原NPZ、raw因子或原全部角数组payload。科学数组另存raw时仅保其原身份，不能由这种语义重建冒称已读全部NPY。

原source字段condensation_report.arrays_artifact_only来自旧库元数据；本次独立编排实际上传计数是0，不能据该旧字段写成存在artifact因子。原QR在Actions内重建，未在本地下载或还原。

原规则监控实际完成14:50:54、15:35:59、16:21:01 UTC三轮同步；原模型/FD和读回都成功。原科学子日志只记录各自bytes/SHA，本文不要求重复下载或长期保存它们。所有“绿色”均不改变8份原status的success=false、new_coupled_finite_acceptance=false、native_at_current_height_solved=false、new_full_DN_acceptance=false。

## 8. 有依据的后继

下一独立38查询实验可只加此次连续两批最近拒绝的LEFT462，保持MID集合、原17档/merit/全域/原FD和完整外变量责任。必须连同interval462的真实输入capture、node462端点和完整B局部支持一起扩展；不能只改query列表或从Bz反造输入。

由于actual155末warm已删，正确接法是在同一新job从真实actual98重生原37八批，保留该新执行的真实末warm/status，然后增加LEFT462并重新构造当前38模型与FD。该前缀是新run的真实执行，不承诺其浮点词与actual155逐字相同；若前缀未完成或未产生有效pair，就诚实保留部分范围，不制造第八末态。也可另从一个实际存在的原warm字节输入开始，但不可以仅凭本结论的SHA续接。

这条新增约束针对未选LEFT462；早期已选查询的非线性弯曲责任仍由R334/R353/R354后置分析单独处理。新的后置诊断不成为38模型或FD接受前门。新增一个查询不保证更大alpha、QP最优或原整体目标完成。
