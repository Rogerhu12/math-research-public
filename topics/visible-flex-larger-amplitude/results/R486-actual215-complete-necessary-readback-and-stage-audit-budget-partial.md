# R486：actual215 完整必要读回成功，owner 原阈值一步接受，stage／audit 原预算部分完成

作者：ChatGPT / amplitude（AI 辅助研究）  
日期：2026-11-16

**可信度：已完成真实运行的必要范围读取；本文登记原官方终态、实际返回值及已核源码的控制流。没有重算科学值，没有由工作流 success 宣称 native/fullDN 接受，也没有把未返回的大数组视为已读取。**

## 1. 主要结论

独立 request215 已终态。两份官方 job 日志返回同一份 **85438 B** 必要 JSON 正文，SHA-256 为 `5923ad0ed6d161eb99494de5cf4ff613071cf0c699034a7db472a8af1e6b0d77`；原单份 90000 B 读回上限本次满足。原 R485 的固定语义共享保留本次实际选中的 owner、trial、evaluation、stage／audit 地址、错误、原字段类型、缺键／null 区别和来源；没有把大树编码或分块运输。

科学结果必须独立叙述：

- 持久 binary128 owner 实际只需 **1 个方向、1 个 trial，alpha=1**，按原严格 norm 下降接受；完整129248行／576段 residual norm 从 `0.000122096054597410989492629881621789239` 降至 `9.68582474751023176056740816374984163e-11`，实际原阈值判定为 true。独立进程 fresh replay 的完整残差及全部226输出逐词与 owner 相同。
- 后置 stage 程序实际请求全 **576×224**，在原8000秒科学预算内完整结束 **478 段**；stage478完成7/12原子步，stage479完成1/12，stage480至575没有完成原子步。未完组原错误均为 `explicit-experiment-time-budget`。
- boundary112 因完整 stages 未产生而未启动；endpoint338×112 因完整 boundary 未产生而未启动。它们不是已经数值计算后拒绝的结果。
- 独立原 C-based physical audit 按其保留预算运行，完整结束 **574 段、7479/7488 queries**。stage574停在query12的物理求值，stage575停在query5的物理求值；后一query之后的1个advance尚未完成。原错误同为 `explicit-experiment-time-budget`。
- 原64 worker 仍按冻结204科学入口在独立128程序返回后受控停止；本次没有接成正常 live native 响应，也没有运行原完整外场 fullDN。实际 `native_accepted=false`、`fullDN_completed=false` 和后置四组件的全部完成flag为 false，不能改写。
- 必要读回、真实 child reap／quiet 及三棵原临时目录清理完成。raw 已清，不能据本文 SHA 恢复或续用本次末态。

本次不同于 R446 的 actual204。R446曾读到后置四组件完整的 bridge flags，但其111829 B必要正文未返回；R486是独立同父重生，实际 stage 和 audit 均预算未完。不能拿204的完成flag补215缺失数据，也不能用215这份85438 B正文冒充204未返正文。两份摘要的大小对应不同真实内容，不能据此把字节差当同一对象压缩率或科学提速量。

## 2. 官方来源与唯一读取身份

| 项目 | 实际值 |
|---|---|
| 仓库 | `Rogerhu12/math-research-public` |
| request215 source/head | `b952df814c98ef5927a4f5013364d2eed6002d74` |
| workflow | `visible-larger-public-native-simd-shared-metadata-final128.yml` |
| run / attempt | `43816406919 / 1` |
| compute job | `133129348123`，success |
| report job | `133231387864`，success |
| 原 request | `public-native-simd-shared-metadata-final128-request.json`，84775 B / `2bceb3ea2e955e6e69293b718e7ad5b4ad05542190cf6b8bfd3f3f03b7ea0437` |
| 新必要 reader | `root_20261116_native_simd_shared_metadata_necessary.py`，46653 B / `d2f2b000310f3e04f3a60e51e74000bcf32516ac50b1f1fac97a4534c06d028b` |
| compute 返回日志文本 | 222042 B / `6b19bb04e15764f4513fb050e31f03e43d26486b3ae0c993b69461575d302836` |
| report 返回日志文本 | 175615 B / `5a47e61211bb27d3fe655d51f51e64619e709e2cb8d24efaf53c58f2e7ef8017` |
| 两 job 同一必要正文，不含分隔 LF | 85438 B / `5923ad0ed6d161eb99494de5cf4ff613071cf0c699034a7db472a8af1e6b0d77` |
| 同正文加一个 LF | 85439 B / `6f1725b1518eecbce47b75a2987b49728b0663e98d9c50cea2d14923d1ab6c72` |

日志身份是连接器返回的**已解码文本再以 UTF-8 编码**的身份，不是 HTTP 原始响应字节。每份终态日志仅下载一次；解析视图逐物理行先移除至多一个行首 BOM，再移除官方 timestamp。原返回文本及其身份没有因解析而改写。报告正文位于 `BEGIN_VISIBLE215_NECESSARY_SUMMARY` 与 `END_VISIBLE215_NECESSARY_SUMMARY` 之间；compute在10:17:37.1345264Z开始该frame，10:17:37.2342731Z返回完整身份，report在10:17:47.8324317Z记录相同身份与compute_result=success。

已完整读取85438 B所选必要正文，包括全部 owner trial/evaluation、所有 stage／audit accounting 组及其实际地址、shared semantic reference、错误、lifecycle、quiet和清理。没有重取运行中日志，没有读取原成功列大矩阵、全部角jets或全部128状态数组正文。那些对象只保原producer身份／计数；“完整必要读回”不等于“完整科学raw搬回”。

官方 steps 14、15、16 分别为原科学编排、必要读回、清理，均success。这里step14的success是外层协议完成；它允许诚实承载内部组件返回2及未完科学范围，不改变第1节的科学事实。

## 3. 冻结原科学与本次真实输入

215保留204全部94项source pins，再加入1个R485必要reader，共95项。实际四个科学执行源仍是：

| 源 | SHA-256 |
|---|---|
| `geometry_20261116_native_simd_stats_qualified_final128_same_job.py` | `8855ef79037bf552f44bd926e92ff5b2874fa17e8e35e1773c6344b71fd2c37c` |
| `geometry_20261116_native_simd_stats_qualified_final128_bridge.mjs` | `718f1c475b4722eaddeae9eb5bf610c438f2a0c221a7e26e10850fbf00126471` |
| `geometry_20261116_native_simd_stats_qualified_final128.py` | `e5c85e6bf5e864de39b0675f997c716466ead0dd158a6c22b73c714257e7433f` |
| `geometry_20261116_native_simd_stats_qualified_stage128.cpp` | `eca87efc267d692e401d2ed49904d3d8e73cc16cad12eb3ae24042328f81025e` |

原输入来自actual91真实failed73 BASE，而不是任何后来已删除的128末点。实际actual91／fresh64 base-states SHA为 `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6`。原78份source及两个真实构造几何输入按冻结合同恢复。fresh64 snapshot实际结果身份是1316 B / `de17af9d287bf6a7a32bbd5cccfaf5508de5973619f326e63b9f47a794746adf`；完整 packet 是10348368 B / `afb10fa8fdc4efe6d9615cf414ab990e5095dda4379cff13f50076a17238ce0d`，绑定3681 B / `a8e1cb1e74ca442254469df63d1210168abf25a542d4863eb72de25253eff392`。

packet完整包含576段、577节点、224形状分量、226完整状态分量、129248 residual行、2048角、实际6943原子RK步及字面 sine/cosine/Gram 表；没有减列、删mean或改变原profile。physical query packet有7488 queries、6943 atomic audit steps；原两种packet的来源与用途分别保留。

原资源合同仍是19200秒共同绝对钟，fresh64/H/J/R273与编译均收费于同钟；owner请求6000秒，fresh replay reserve1200秒，四component科学caps为8000/600/600/1800秒，overhead caps为345/720/345/345秒，readback/cleanup reserve120秒；4线程，原32方向×10档、原root30×20及字面8e-14／5e-12规则均保留。330分钟science step、350分钟job、2700秒规则轮询不变。全局剩余时间并非必须被某个已达到自身cap的组件继续消耗：本次stage停在其8000cap，audit停在其1800cap，编排末仍记录5085秒scientific remaining。

本次stage真实编译成功，原R423三处namespace视图及R445 `BatchStats`限定都已实际使用；没有复现R424的类型编译阻断。compiled header仍29035 B / `b183eeecf4f3009bf202dd0f465c8d4fdb17d8cc0ce14bb90d1ed5e6ecf485ac`；f82旧include视图24775 B / `f82cd9504fc7396664941a76e687abd489aae8766482977c80a675c9e9a9b9ae`只改变已明确的三调用名称。audit实际编译a090源18055 B / `a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415`。

## 4. owner：实际接受与独立 replay

### 4.1 原完整 norm 与唯一试探

| 项目 | 原返回值 |
|---|---|
| 初始 norm decimal | `0.000122096054597410989492629881621789239` |
| 初始 norm binary128 hex | `0x1.000dd1f7889da0c80213a1f62c65p-13` |
| 最终 norm decimal | `9.68582474751023176056740816374984163e-11` |
| 最终 norm binary128 hex | `0x1.a9fcb11a67aa9fe05f1217f1302ap-34` |
| 原 outer tolerance lift | `2.00000000000000012456318291555971284e-09` |
| complete / rows / stages | true / 129248 / 576，两次evaluation均完整 |
| 方向／trial／alpha | 0 / 0 / `1`，hex `0x1p+0` |
| 原接受原因 | `strict-original-norm-decrease` |
| 原停止原因 | `shooting-tolerance-reached` |
| changed128 state words | 126838 |
| 改变128而64 cast相同的words | 11239 |
| trial elapsed seconds | `1014.157854104` |
| owner elapsed seconds | `3069.196728829` |
| mean height sum，两次evaluation | `0.0226842463487103007695708959242220956` |

初始最坏行是global2791，stage11/input12/output11、Pi mode104；最终最坏行是global2128，stage9/input10/output9、Q mode1。最终该行 residual为 `4.99890220172700756930979612524613054e-25`，sigma为 `5.16104960810073433235339041548094359e-15`。完整failed_stages均空，evaluation_error为null，budget_exhausted=false。

方向索引仅实际请求0；原final逐项列明未访1至31，最后该方向未访trial1至9。它们是原容差已达到后的未访，不是被隐藏的拒绝或预算不足。本文没有另外尝试这些方向或alpha。

本次完整owner evaluation root统计每次27772 calls、904 Newton steps、904 line_search_trials、fallback_returns=0、maximum_iterations=1。最终maximum returned relative为 `7.97942273584970897156361583077219799e-14`，27772次均原threshold reached。初始对应值为 `7.97942273584970872285222203689169507e-14`；不把两组近似显示混成同一原词。

### 4.2 QR与恢复的真实精度边界

方向是固定fresh64 chord matrix与本次128 residual组成的原R273问题，不是fresh128 DF。完整129248列／129248行、577节点penalties、576 stage rows与112 cut/far均保留。原QR factor/constants实际464891392 B、1153 QR calls；本次方向QR报告 complete=true，elapsed7.938604366000163秒。

本次residual仅为近似QR作一次binary128→binary64 RN投影：128969项改变、nonzero_to_zero=0，最大sigma-scaled转换差 `4.10665514535721833358792197700840237e-21`。末state从未通过binary64往返。恢复 `delta128=sigma128*z64_lift` 覆盖577×224，与旧rounded_delta64有129182项不同；最大scaled恢复差 `9.94166392917834227785107527013571685e-28`。这些是原实际记录，不是准确导数或后验误差证书。

形成模型的longdouble读回仍明确为64-bit significand而非binary128有效113位：formed residual infinity `9.685824747510231713e-11`，model drop `2.1310995861557109647e-08`，完整model gradient two norm `1997706.5878711008485`。其对象是形成的f64系数模型，不替代真正128 nonlinear trial接受。

### 4.3 同一末态的独立全范围 replay

| 同次对象 | 字节 / SHA-256 |
|---|---|
| final-state.f128 | 2067968 / `8fa0eaedacf050e7584a1dee047e97229ca3ec79bcb09eb742ff44e34c1445bc` |
| final-residual.f128 | 2067968 / `e7061ce086de8a5cbb7b457703381631114ee740d65949770e3d2b8c20ce7892` |
| final-stage-full-output.f128 | 2082816 / `79e3a26a8eef01ba008f957d64c1bf4ec0e41290c772872acde0f6fecd43d16e` |

fresh replay独立进程返回0、wall_timeout=false，完整residual及全部226输出的SHA和逐词比较都与owner相同；其evaluation引用同一实际完整final记录。该replay包括所有cut/stage/far与两个mean累加器，明确不是physical audit，也不是stage Jacobian的准确性证明。

## 5. stage 完整请求及全部未付地址

stage main实际returncode=2、wall_timeout=false，elapsed `8000.089360956001` 秒；scientific report elapsed `8000.010199285` 秒，父组件含绑定／编译共 `8009.784193263` 秒。原report的budget_exhausted=true，component.resource_partial=true，scientific_complete=false，procedure_complete／summary_complete／transport_complete=true。没有stage scientific70，也没有reader协议70。

完整stage记录576项。每个地址为原 `[row_index,stage,input_node,output_node]`，本次均为 `[n,n,n+1,n]`。下表是**从实际全组地址逐项读出**的覆盖，不从完成计数推造连续范围。

| 实际stage地址 | 原子步范围 | 原状态 |
|---|---|---|
| 0至477 | 完成全部各自12或13步 | completed=true，error=null |
| 478/input479/output478 | 完成7/12，unfinished=[7,12] | `explicit-experiment-time-budget` |
| 479/input480/output479 | 完成1/12，unfinished=[1,12] | 同上 |
| 480至575 | 完成0步；各自unfinished=[0,12]或[0,13] | 同上 |

完成组的13步stage明确为
`[11,28,31,63,98,103,135,169,175,202,207,240,247,272,279,312,319,344,351,384,391,416,423,456,463]`；
其余0至477是12步组。未完零推进组的13步stage为
`[488,495,528,535,560,567]`；
其余480至575是12步组。这里“0个完成原子步”不声称程序没访问该stage的time_check／错误记录分支。

所有224状态列同批，完整输出维数226，两个mean／port方向没有省略。实际complete_224_stage_columns、complete_576_stage_primal、complete_requested_range均false；原stage primal norm、worst_row为null而norm_readback_error=null，不能据此填一个完整stage norm。

原成功stage逐列大记录仅identity返回；全原stage rows canonical身份为2917438 B / `c1af2f63c5b5ee490e689612fc27c5780bad1e3542f04636258b836225034faf`。完整component summary为3044814 B / `7d60ebbfe531fcb1861e09cd53f1cf530bf627e7375b2159e5e48ba1521d45a0`，内部scientific summary为2926466 B / `0d76909cac1e558ef94acb0f33fbbd72a5a8e101efc4bfd91deb518c638e663d`。这些大正文不在远端本次必要返回中，不能声称逐列读取。

### 5.1 实际完整统计的必要数值与边界

必要正文保留原所有backend/方向统计；本结论选取说明计算范围及未付项的数值，不把计数变为速度比例。

| 原统计 | 实际值 |
|---|---|
| complete_rhs_column_batches | 23079 |
| full_rhs_columns | 5169696 |
| root_tapes / primal.calls | 23087 / 23087 |
| shared primal factorizations | 904 |
| completed_RK_steps / completed_column_steps | 5769 / 1292256 |
| state_only_RK_batches | 5773 |
| root_operator_returns / original_small_input_columns | 5169920 / 5169920 |
| accepted_operator_updates / shared_factor_direction_solves | 202496 / 202496 |
| full original C-direction residual rows read | 22882048 |
| complete preassembled entries checked | 11475840848 |
| preassembly root builds started/completed | 904 / 904 |
| preassembly flux builds started/completed | 23087 / 23084 |

这些计数处于不同调用层；有已开始未完成的batch，不能据一个计数补另一个complete或给缺失stage填列。原aggregated completed_preassembly_seconds为 `15796.738988724002`，不是单线程wall time，也不是独立测速。

原reported残差为：

- computed C-direction solve max abs：`1.20370621524202240815998621411557957e-34`；
- nominal `LL^T-C` max abs：`1.34815096107106509713918455980944912e-33`；
- nominal `C*step-F` max abs：`3.82342058671788546486931295464250833e-57`；
- nominal `L*tmp-F` max abs：`1.27447352890596182162310431821416944e-57`；
- nominal `L^T*step-tmp` max abs：`0`。

原reference_columns为none。reference_complete226_difference_max_abs虽记录0，但reference_field_columns=0且independent_runtime_word_comparison_performed=false；这个0不能宣称独立逐词对拍通过。

实际CPU backend为 `gnu-x86-avx2-signed-even-and-odd`，avx2_body_compiled=true；exact_dot_calls=2017700583、packed_dot_calls=1797680353、wide_dot_calls=207723078、zero_dot_calls=12297152。实际max_observed_limb_count=15、max_observed_span_bits=290，fast_limb_limit=12；宽指数分支真实使用，没有六limb截尾。integer_partial_sums=137409158655，digit_products=73127166538316，avx2_even_products与odd_products各36533349340928，scalar_tail_products=60467856460。negative_zero_input_words=12076655，nonfinite_input_failures=0、overflow_outputs=0、rounded_zero_outputs=0、subnormal_inputs/outputs=0。所有这些是原未完stage范围内的实际统计，不扩为全576完整结果。

原scope仍明确：complete dyadic dot之后一次RN113；小H／权系数依然binary128形成且相对190重关联；名义因子不被当作准确C；direction_error_bound_supplied=false，nominal_factor_residual_derivatives_proved_zero=false，accurate_finite_root_derivative_certified=false，branch_stability_proved=false，whole-stage逐词比较未做。原有限请求没有因此新增门。

## 6. boundary／endpoint未起与独立audit部分结果

### 6.1 依赖不是推测

boundary实际父记录为requested=true、attempted=false、scientific_complete=false、missing_component=`stages`，reason=`complete-current-mathematical-input-not-produced`。endpoint对应missing_component=`boundary`。两者original_summary_present=false；没有真实边界112响应、完整338×112端点矩阵或其数值极值可报告。

冻结component launcher的preceding检查要求真实同来源前置component scientific_complete=true；本次依赖停是原合同。不能用owner residual合格绕过该完整输入要求，也不能把这条缺输入解释为boundary/endpoint数值拒绝。

### 6.2 audit实际覆盖、活动query及advance

audit独立于stage完整性，实际main returncode=2、wall_timeout=false，elapsed `1800.0776108560003` 秒；父含编译／必要内部读回 `1808.0171138329988` 秒。全报告complete=false，stages_completed=574，queries_completed=7479，queries_requested=7488，all_angular_rows_saved=false。

全576原地址逐项保留，完整0至573。剩余原记录为：

| stage | active_phase / query | 已完queries | 已完atomic advances | 当前query之后advance | 原unfinished_query_suffix |
|---|---|---:|---:|---|---|
| 574 | physical-query / 12 | 12/13 | 12 | completed0 / count0 | [12,13] |
| 575 | physical-query / 5 | 5/13 | 5 | completed0 / count1 | [5,13] |

两行原error均为 `explicit-experiment-time-budget`。a090实际代码在capture_field、physical_jets、physical_metric和该query的完整角／state／scalar写出后，才递增queries并进入primal-advance；完成advance才递增advances。因此：

- stage574的query12已进入物理求值但尚未完成其原query写出责任；其全部query之前推进已记12；
- stage575的query5同样未完成，后接1个advance未开始完成；query6至12及其后续推进仍未付；
- 原缺9个完成query包含两个当前活动query，不能全部称从未尝试；也不能只说“差9个query”而吞掉query5后的advance。

原 audit summary **没有顶层**budget_exhausted／resource_partial字段；component launcher只是从process.wall_timeout及报告这两个可选布尔汇总resource_partial，所以本次父 `resource_partial=false` 与逐stage原预算错误同时存在。本文保留两者原值，按原error及覆盖解释为预算部分完成，不把false改成“未超预算”或另造新flag。此为已核源码字段口径，非额外科学运行。

### 6.3 所返极值只属于实际已计算范围

| 原字段 | 原词 |
|---|---|
| fullD | `4.56809189695701091463570460409905198e-22` |
| normalizedFullDefect | `1.79646354527296221572400805980989501e-23` |
| minLeading | `0.999999999976030433424450852637560674` |
| minD | `0.999999999999985867351722004137088646` |
| formalCurvature | `7.9942546935187970829178002448203843` |
| maxPhysicalPV | `2.06869309424094196099662980575035568e-16` |
| actualMetric | `1.24740319769992190894296352204671455e-16` |
| holonomy | `7.78643063896605725733473256900848618e-28` |
| C_radial_solve_readback_max | `2.60294668883439455108061545901388858e-44` |

原报告明确 `extrema_are_partial_if_complete_false=true`。某活动query可能已进行部分中间求值／更新，不能把上述极值严格重标为仅7479个已完整写出query的函数；可以且只可以称原未完audit实际累计读回。它们不是未访问范围的外包，不是连续ODE/完整闭面metric证书。

audit原root_tapes/calls=35225，Newton_steps=1146，line_search_trials=1146，fallback0，completed_RK_steps=6936；实际root阈值口径仍同owner。完整component summary为277865 B / `88837374959e6ed0fd3b020334ea65296c0b9cd8c4043d06009aa8953b6ab379`，内部scientific summary155289 B / `cb8833cd86ba7df72cfa94cbd0efcb6b2f1595cca62b5b19a903a778193bd90b`。完整stage rows canonical152597 B / `0a07b06f8aad6fe8a57b960ad23f97db11f27ac6675008fbbd13a177e7b04638`，返回的是其必要分组／地址，非全部角raw。

## 7. 原接受责任：哪些付了，哪些尚未实际消费

按已刊[R491](R491-original-native-fullDN-gates-and-complete128-response-consumption.md)，原native协议允许338×112混合Jacobian，不要求所有338行解析微分。本文不把全解析、branch证明或导数误差证书添为原有限接受门。

215真正付的是同次128射击norm、完整实际一步接受、全部原 residual／226输出的独立replay，以及第5、6节已完成部分的实际范围。没有付完整后置stage、boundary和endpoint；独立audit尚缺明确后缀。原64 controlled stop仍返回：

`PERSISTENT128_CONTROLLED_ORIGINAL64_STOP_AFTER_INDEPENDENT_OWNER`。

其original_driver_exit_code=2，original64_nonlinear_trial_calls=0；response.converged与residual为null，failed是上述受控协议文字。fresh-original64 wrapper实际_error=null、procedure_complete=true、summary_transport_exit_code=0；它记录controlled_protocol_failure_not_math_rejection=true。不把该包装层成功改成原native响应。

本次没有真实live H→正常native响应的消费路径，没有原当前H FD、完整外场collocation/BC/RMS、非线性outer回算或末cut/seam接受。post-owner flags是另层对象，实际全false；owner旧full_stage_J_complete等false仍按原owner内部口径保留。R491指出的正向live消费路径由其他独立后继负责，本次没有把215已删数组转交未来run。

此处没有从“完整但未接”或“预算未完”推出数学不可行；也没有借其他run已完成的component来支付本次缺项。全t强C²、准确共同metric、reach、held及连续误差责任仍未由本次有限程序结果承担。

## 8. 必要表示、错误、quiet与真实清理

新reader只重排原已选元数据。实际 `equal_selected_dictionary_reference_count=7`；两个component_budget还用相同原payload引用。共享前逐原canonical完全相等，缺失键不补null，原trial/evaluation各自key-set保持。两实际components共用一个源／算术scope组；stages/audit的统计、错误和地址各自独立。没有把相同schema当作数值对象相同。

12个实际诊断文件均存在、完整读取且为空；表逐项保原listindex/path/file/bytes/SHA，空共同text为真实空串，不把未生成文件冒空。other_original_records=[]，metadata_read_errors=[]，显式16KB非空错误选择规则未放宽。预算错误在原科学JSON中，不因stderr为空而消失。

最终字段为summary_complete=true、transport_complete=true、explicit_incomplete_error_reply_delivered=false、cleanup_allowed=true；没有90000超限、没有metadata协议70。原stage/audit scientific exits均2，launcher_protocol_exit70_observed=false、main_scientific_exit70_observed=false。原二者资源口径差异已在§6说明，未被success覆盖。

fresh child实际pid3484、child_reaped=true、child_returncode=0，global_wall_budget_exhausted=false。原wall guard实际elapsed12890.064950605、cap17973、wall_timeout=false；只控制matching PID/starttime owned descendants。必要reader确认owner_quiet_observed=true，matching_owned_path_processes=[]、unreadable_same_user_processes=[]。该quiet范围是原同用户cmdline所属路径检查及记录的fresh child reap，不被扩成未提供的系统全进程证明。

在必要摘要之后，compute日志实际记录：

| UTC时间 | 实际操作 |
|---|---|
| 10:17:38.1685175 | 删除 `visible-native-simd-shared-metadata-final215` |
| 10:17:38.1696690 | 原actual91自有归档目录权限恢复，21个目录；follow_symlinks=false，文件字节／科学结果未改 |
| 10:17:38.1768203 | 删除 `actual91-shared-metadata-final215-parent` |
| 10:17:38.1848358 | 删除 `native-simd-shared-metadata-final215-public-original-source` |

三次原removed事件均写necessary_summary_and_owned_quiet_observed=true、no_raw_upload_followed=true。不能在后继声称复原这些已清raw。发表保留必要结论、来源、实际接受／未付范围，不把85KB选定摘要或大stage表再作为结果文件整份入库。

## 9. 此次实际推进与后继边界

R485表示修订已在真实完整链付了单份必要读回与清理；原scientific范围诚实返回，不再只有bridge简旗。真实需要继续处理的计算成本是stage8000秒仍不足576段、audit1800秒仍缺最后活动query/advance。这里没有对预算直接提额，没有为缺项再开小benchmark或添加原门以外的检查。

owner达原容差与replay逐词相等是本次确定进展；科学全链尚未完成。未来如使用既有独立数学等价优化或live响应入口，须以其实际新source和同次真实数据执行原全部范围，不能继承本次partial作完整组件，也不能从已清状态SHA续接。本文只登记本次run，不修改其他在跑入口。

## 10. 复现与引用

实际入口、源表、参数、预算和必要reader以本次source `b952df814c98ef5927a4f5013364d2eed6002d74` 固定。本文另按该head读取了component launcher e5c85、stage eca87及physical a090全文，核§5、6的时间／query／advance与resource_partial口径；没有执行它们。

- [actual215官方run](https://github.com/Rogerhu12/math-research-public/actions/runs/43816406919)
- [compute133129348123](https://github.com/Rogerhu12/math-research-public/actions/runs/43816406919/job/133129348123)
- [report133231387864](https://github.com/Rogerhu12/math-research-public/actions/runs/43816406919/job/133231387864)
- [本次request](../computations/public-native-simd-shared-metadata-final128-request.json)
- [R485必要reader](../computations/root_20261116_native_simd_shared_metadata_necessary.py)
- [原component launcher](../computations/geometry_20261116_native_simd_stats_qualified_final128.py)
- [原physical audit程序](../computations/geometry_20261115_native_physical_final128.cpp)
- [R491原native/fullDN门与正向消费合同](R491-original-native-fullDN-gates-and-complete128-response-consumption.md)

本次没有本地科学运算、模块import、AST/编译、fixture或独立测试；只有原官方已执行日志的必要读取、原字节/JSON元数据核对和确定源码控制流解释。
