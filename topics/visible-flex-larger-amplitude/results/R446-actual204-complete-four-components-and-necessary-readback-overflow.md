# R446 — actual204：完整128求解、四组件完成与必要读回超限

AI 作者：ChatGPT（amplitude）；日期：2026-11-16。

**可信度与范围：已核实的实际运行读回及源码控制流结论。** 本文逐条区分原日志实际返回、由绑定源码解释的完成范围和未返回的数值。四个后续组件的完成标志确已返回；本次没有返回完整必要摘要，也没有得到原 native／full-DN 接受。没有本地科学重算、导入、编译、数值测试或新验收门。

## 1. 结论与实际作业

actual204 以新的 R445 单类型限定源码重生原完整链。真实 owner 返回一个方向、一次试探、一次接受；完整576阶段、129248行的最终归一化残差为原 binary128 词

$$
9.68582474751023176032080482454992093\times10^{-11},
$$

并返回原容差通过与独立 fresh replay 两项逐词相等。随后 **stage maps、112边界响应、混合338×112端点读数、独立原 C-based physical audit 四个组件均返回完成**。这次不再是 R424 的阶段编译停止。

但末端必要 reader 形成了 **111829 B** 的对象，超过90000 B硬上限，诚实返回795 B错误摘要、退出70。原四组件详细残差、物理极值、SIMD实际后端统计和逐阶段记录未随该错误摘要返回。不能由完成标志补出这些值，也不能用其哈希恢复原文。

| 项目 | 本次真实身份／状态 |
|---|---|
| repository | Rogerhu12/math-research-public |
| source | 189579b508930d99d9c2dbc481967fd972766919 |
| run／attempt | 43789310271／1 |
| workflow | visible-larger-public-native-simd-stats-qualified-final128.yml |
| compute | 133043887128，completed／failure |
| compute step14 | 原绝对期限完整科学链，success |
| compute step15 | 单份必要原metadata读回，failure，原退出70 |
| compute step16 | 条件清理步骤success；实际行为是跳过删除 |
| report | 133114084407，completed／success；保留compute_result=failure |

官方终态元数据与两份终态日志各只取一次。report成功仅表示它成功打印了真实795 B错误摘要；不改变compute失败，也不补付科学接受。

来源：[实际run](https://github.com/Rogerhu12/math-research-public/actions/runs/43789310271)、[固定source](https://github.com/Rogerhu12/math-research-public/commit/189579b508930d99d9c2dbc481967fd972766919)。

## 2. 原日志身份、读取范围与协议层次

连接器返回解码文本。以下字节数及SHA是该返回字符串的UTF-8重新编码身份，**不是HTTP原始下载字节身份**。按每个物理行先去可有的行首BOM，再去锚定UTC时间前缀；不改JSON正文中的数值词。

| job | 返回文本UTF-8字节数 | SHA256 | 物理行／时间前缀／BOM行 |
|---|---:|---|---|
| compute133043887128 | 135815 | 161a92de48ffe188f5341b605545b3c60b5d13fa6db723ad6c28bc33536210d1 | 957／953／[1] |
| report133114084407 | 6321 | 328fcf9b6bc67c855ce28c23938983426a3fd390f8688de37a6d58361c1c31be | 65／64／[1] |

compute的原bridge整行位于物理行811：10758 B，SHA256为 cd069cd83e4b6b5c6f2ee0e525a48460661b368425787cb60cc6866530bb7d4f。该整行及其全部 scientific_summary、实际四组件flag、owner final、wall_guard、child_exit 已完整读取。其余实际科学记录、四组件起止回执、规则同步、必要失败和条件清理也已读取。工作流echo出的命令与实际事件分开，不将源码里的字符串当实际结果。

两job同一 BEGIN_VISIBLE204_NECESSARY_SUMMARY 正文逐字相同：

- 不含打印分隔LF：795 B／f74e73f70e85777c3234815b0feb678b6234eaa3bca1e6f367b9c24e45a10f23。
- 连同一个打印LF：796 B／479c749f0573221912eccafcc172a55689d0f78a37cd8b308ddf916a55f33ca8。
- reader实际拟返回的必要对象：111829 B／08cf8251221727c97fc076c30f0e71a4d6bd5af452b3e1a6472d60dbe603826b；**原文未返回、未逐字段读取**。
- owner完整临时 summary.json：193588 B／cf8992567ed7c4129bde6798d595bcc0cec01f8bdf9682899ad7e1774e119a29；本文只读取已实际返回的选择，不称读过该完整文件。
- bridge所引 compact-summary.json 原receipt：5153 B／0fcd645532ea189abc258f8336f16406cb0e572f7b6442bcd6139eb63243014f。此文件receipt、bridge展开的 scientific_summary、末端必要摘要属于不同对象，不按长度或同名词合并。
- owner final完整记录只有2818 B／dc1337f83d327d6c6d7af7f782e2435c36b1071428641a98676eb374aa8b814b身份；本文已读其中实际返回的 final_scalar_flags、计数与未访地址。

没有再取旧199原数据，没有以旧包或已清理内容填本次缺项，没有把未返111829 B对象分包或编码运输。

## 3. 当前源、输入与预算

实际 source preflight 逐项返回94个来源记录并成功。它们是原199的89项加R445 stage及本次四源；94不是一次新的科学求值。两个已审README blob为根21bd547f56590b7f2dd279d0297efb289a9b2783、题bff8aea253a9e6a7a4fac28d810ac454c5499fec。

| 当前关键文件 | 字节数 | SHA256 |
|---|---:|---|
| public-native-simd-stats-qualified-final128-request.json | 76649 | 7e6f600e76ea5023c63e98fe0a3899e0eb532d7d65f672a59f5bc4411e9bd871 |
| geometry_20261116_native_simd_stats_qualified_stage128.cpp | 12691 | eca87efc267d692e401d2ed49904d3d8e73cc16cad12eb3ae24042328f81025e |
| geometry_20261116_native_simd_stats_qualified_final128.py | 31930 | e5c85e6bf5e864de39b0675f997c716466ead0dd158a6c22b73c714257e7433f |
| geometry_20261116_native_simd_stats_qualified_final128_same_job.py | 38408 | 8855ef79037bf552f44bd926e92ff5b2874fa17e8e35e1773c6344b71fd2c37c |
| geometry_20261116_native_simd_stats_qualified_final128_bridge.mjs | 15829 | 718f1c475b4722eaddeae9eb5bf610c438f2a0c221a7e26e10850fbf00126471 |
| root_20261116_native_simd_stats_qualified128_necessary.py | 37574 | 93335c21f6129b1f7ae5c62b2ae7db5e90039fcb30ccfdef1a3951985cb24ee7 |

原R423三调用限定header f82cd9504fc7396664941a76e687abd489aae8766482977c80a675c9e9a9b9ae保留。R445只将阶段的一个 BatchStats 类型显式限定为 simd_digit_trace128::BatchStats，数值正文不变；本次全链使用这些实际新身份，不把新stage称为旧b653逐字文件。R402／R405／R414既有准确实与整数点积条件不自动成为整个导数链的误差证书。

原actual91输入临时恢复成功：原artifact14145200674，run43672150224，archive10267458 B／78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6；failed73的原完整state只作初猜，非接受锚点。78个旧源和两份frozen-geometry输入按原步骤恢复，未改变原标定／几何检查。

实际新packet为10348368 B／1c9df6b2aa203d526eee11fe443ebcb474584c677b76ed3901b6a0f6c1f37aa8；原packet记录576 stages、224 shape维、226完整state维、2048角、6943 RK steps、20829 geometry calls。原geometry是binary64样本，不是新准确连续C证明。物理packet5104360 B／1c9fab18574bb130f905daef5fcff66163a0fe987528ace2d9bc81829fc52151；其计划7488 queries、6943 atomic audit advances。这里是实际packet计划字段；未把它们伪写为未返回audit报告的实际累计字段。

原预算保持：19200秒总科学钟，owner6000、fresh replay reserve1200、stages8000、boundary600、endpoint600、audit1800；组件附加额度分别345、720、345、345；cleanup reserve120秒、4线程；原32方向×10回溯档与2e−9容差。原2700秒规则流程保留。packet时真实 global_remaining_seconds=18284、remaining_scientific_seconds=18164、guard_seconds=18164；fresh64前置已计入原钟，不重启钟。

## 4. fresh64、128 owner与独立重放

### 4.1 三个不同数值不能混同

原 fresh_direction_for_trace 记录包含：

| 原字段 | 实际返回 |
|---|---|
| current_original_norm binary64 | 0.000060618737006888706，词71f299f11bc80f3f |
| complete-current R273原行读回最大值的decimal显示 | 9.685623139820915231844260456306540893890861679791289092058094119E-11 |
| 后续128 owner最终norm | 9.68582474751023176032080482454992093e-11 |

第二项是fresh64模型所选方向的原完整行读回，第三项是独立128原残差评价；不能互相替代。第二项对应原row2128、stage9、Q mode1。其显示不是比较算术；原记录还保准确有理分子分母及dyadic残差。本文不重刊可重算大表。

fresh snapshot为1316 B／2014ffce9dd83c687d77c35d551c0f7099383d78b079d028566cf34b0a0c5c31；当前state完整SHA为f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6；完整direction为4bb396b069f5c32a3d77a08531ad2cdefbd3ece7fd8f63c56baed84f13976ce6。QR记录actual_error=null、complete=true，129248列／129248原行／258496增广行，1152 formation calls、1153 QR calls，因子与常量464891392 B，eta原词1。记录的working_precision.significand_bits=64，不能因dtype名float128就称该QR为113位。

这份初始64方向只付packet来源，原标志 initial64_delta_is_packet_provenance_not_the_persistent_iteration_RHS=true。后续仅固定64 J作近似chord；不冒当前128 DF或原C准确逆。

### 4.2 实际owner停止

原返回 owner_final：

- stop_reason=shooting-tolerance-reached；
- directions_computed=1，trial_evaluations=1，accepted_steps=1；
- requested_direction_indices=[0]，attempted_trial_addresses=[[0,0]]；
- final.complete=true，budget_exhausted=false，stages_completed=576，rows_completed=129248，below_original_tolerance=true；
- 最终norm binary128 hex为0x1.a9fcb11a67aa9fdf970095730bcp-34；
- 最差原行global_row2128、stage9、input_node10、output_node9、Q mode1；原residual词0x1.356ac467a14758cd2c64p-81，sigma词0x1.73e48faf8b814p-48。

未访方向为1至31，末已请求方向未访trial为1至9。这是原实际完整地址记录，不是因为transport失败而补零。原32×10预算没有删减；达到原停止条件后不继续同点方向。完整trial/evaluation正文、初始128norm、逐trial参数／拒因表未随bridge选择返回；本文不由旧run填充，也不从地址补造原字段。

final-state.f128为2067968 B／e0f20c36d59ac200796a03441e7b5604224e3add414361a11cc6ff3586dffba2；final-residual.f128为2067968 B／18cfb3face9b286513f624003984d318bc6b6c735ed803a3cbffde15dc6be39b。它们是原临时数组身份，未把本文的小结当可恢复原数组。

### 4.3 replay及原64受控停止

实际 bridge 返回：

- independent_fresh_replay_complete=true；
- fresh_replay_full_residual_words_equal_owner=true；
- fresh_replay_all226_output_words_equal_owner=true；
- persistent128_state_was_not_written_into_original64_worker=true；
- original64_worker_controlled_stop_follows=true。

原64 worker随后记录fresh_snapshot_count=1、fresh_R273_direction_count=1、original_nonlinear_trial_calls=0，停止文字 PERSISTENT128_CONTROLLED_ORIGINAL64_STOP_AFTER_INDEPENDENT_OWNER。其最后 residual=null、task_completed=false、native_accepted=false，不是把128state强转回64并补出原native响应。owner层的elapsed_seconds=2435.072626899；这不是四后续组件全部完成的总耗时。

## 5. 四组件完成：原flag、源码条件与未读数值

原bridge的 actual_post_owner_component_flags 和 scientific_summary.post_owner_components 同时返回：

| 原字段 | 本次原值 |
|---|---|
| all_requested_components_completed | true |
| complete_stage_maps | true |
| complete_boundary112_response | true |
| complete_mixed_endpoint338x112_readout | true |
| complete_original_C_based_physical_program_audit | true |
| native_accepted／fullDN_accepted | false／false |

这些true不是仅凭job success推得。8855 helper读取同一live owner state与handoff绑定的component summary，要求其 scientific_complete=true且组件外process.returncode=0；e5c8 launcher又要求原科学report完成字段为true且原科学process.returncode=0。具体数学程序覆盖如下。

### 5.1 stages

实际固定命令请求 first-stage0、stages576、first-column0、columns224、reference-columns none。eca87源只在每个实际stage的全部原atomic RK步骤及所有请求列完成并写出primal／before-port／after-port／双mean／residual后标该stage complete。整体 complete_requested_range 要全部576；退出0还要求完整norm读回未报错。

故返回true按本次绑定源码支持“请求的完整576×224阶段传播程序已完成”，包括226输出中的双mean及原port。它没有证明原R305逐词同图、分支稳定或准确导数误差界。R402记录系数／名义因子对象、R405完整dyadic点积后一次RN113、R414可能选用的SIMD或scalar分支仍是各自范围。**本次实际后端选择、fast／wide／scalar计数、factor方向残差和完整statistics未返回**；不因标题含SIMD就声称AVX2实际用了多少次。

### 5.2 boundary112

原c218f12850e513cc58151e679c26de038f37b105dd187696e6f785ec4667fe96程序保全部112 homogeneous modes，做完整far/stage thin QR、cut square QR、完整577节点响应和129248×112原行readback，双stage mean亦保留。原字段 linear_readback_is_not_acceptance_gate=true，cut_chart_nonsingularity_proved_over_reals=false。

返回complete说明该有限数值程序完成，包含原finite readback检查；**不说明线性readback误差小于某个未给阈值，也不证明实数cut chart非奇异**。本次三种readback maxima、最差row／height column及QR数值缺陷未返回。

### 5.3 混合338×112端点

原a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415的complete条件是base完成、112个完整symmetric列、112个first-slope列全部返回、error为空。行顺序保持 slope[112]、second[112]、meanSlopeCorrection、meanSecondCorrection、height[112]。

first-slope／mean-first来自当前trace/RHS变分；second／mean-second仍是原C-based物理jet程序的对称差分。原 all338rows_are_an_exact_analytic_Jacobian_claimed=false、endpoint_matrix_does_not_itself_pay_fullDN_or_fresh_audit=true。本次不以混合矩阵“完成”宣布全338行准确解析Jacobian、full-DN接受或差分误差已经界定。

### 5.4 独立C-based physical audit

同a090源从每个真实128节点n+1独立启动原query/RK程序，保全部角jet与完整state。每stage只有全部query及每个query之后的所有primal advances完成、全部输出flush后才complete；总complete要求576stage全部complete。**它不是只数query，也不会把末query后的advance吞掉。**

其原程序会记录fullD、normalizedFullDefect、minLeading、minD、formalCurvature、maxPhysicalPV、actualMetric、holonomy与C_radial_solve_readback_max。但complete条件是遍历完成，不是这些量通过原几何／native门。它明确 native_accepted=false、fullDN_accepted=false、new_acceptance_gate=false；不能把C-based径向程序读数称为有限root分支的准确径向导数。

本次audit完整flag真实返回；其详细报告与全部极值／最差位置未返回。packet计划7488 queries与6943 advances及源码完成条件说明所要求的全部范围，没有把未返回的实际counter逐项刊成“已读原值”。

### 5.5 旧owner flags和新postowner flags不矛盾

scientific_summary另保 full_stage_J_complete=false、endpoint338_by112_sensitivity_complete=false、original_geometric_final_audit_complete=false、native_accepted=false、fullDN_completed=false。前面三项是原767a owner对象自身字段：初始化为false，且本次 final_stage_columns_requested=0，没有走该owner内部旧逐列路径；后续新四组件结果另在 post_owner_components 中返回，不覆盖这些原字段。

718f bridge显式把native／fullDN接受保false，不存在“所有组件complete后自动改为原native/full-DN接受”的合成分支。末端reader超限fallback中的false也是诚实非接受／不推断字段，不是另一份组件科学失败判定。本文同时保留所有原字段的层次。

## 6. 时间、资源、异常与原始缺失范围

四组件启动时原预算与日志UTC起止如下；UTC是运输记录时间，不能冒原未返的纯内核elapsed_seconds。

| 组件 | science cap／含额外总额度（秒） | start记录UTC | return记录UTC | start时剩余科学秒 |
|---|---|---|---|---:|
| stages | 8000／8345 | 02:54:44.4508419 | 05:04:52.2640758 | 15729 |
| boundary | 600／1320 | 05:04:52.2643890 | 05:12:08.9713956 | 7921 |
| endpoint | 600／945 | 05:12:08.9716950 | 05:14:13.9421869 | 7484 |
| audit | 1800／2145 | 05:14:13.9427057 | 05:38:08.9073760 | 7359 |

原wall_guard返回child_returncode=0、guard_returncode=0、wall_timeout=false、wall_seconds18164、elapsed_seconds12243.249840457；原global_final128_child_exit也返回actual_child_returncode=0、returncode=0、global_wall_budget_exhausted=false。科学步骤没有因本次总钟终止。

四个 component child-stderr 记录均present=true、complete=true、bytes0、lines_forwarded0、unforwarded_indivisible_lines=[]；owner-child.stderr.log也0 B。它们是已返回的外层stderr身份，不扩大为所有临时nested compiler文件都空。实际完成flags和退出0已说明本次不再是已知BatchStats编译阻断。

四个 precleanup_component_return 在compute仅保原事件身份：

| 组件 | 原完整事件bytes | 原完整事件SHA256 |
|---|---:|---|
| stages | 24450 | b6412a8ff4f20fa6218e67d6e2eb831c3293f79262057a362fa742f5bccf1b2b |
| boundary | 23516 | 044601062678cd240971f91a607db169e9123bdc18d10af31f6cc5135da580de |
| endpoint | 16849 | 693c6953f4830ecf4d96b6b4983c1c62aed25c68ae9884bf9317ac7c6fb637e4 |
| audit | 16144 | 51cc4503bb722ba4c84b9af21007448f0945a0e61845e4d7e7e41c9839e07e90 |

all-components完整事件82513 B／568d6f470192c44b5ae6b3ff36c7f46835014d32484d834496109f2d0f339471；其正文同样未打印。事件身份不是完整scientific_report身份或全文阅读证明。逐阶段误差、全部numeric arrays、完整owner QR、逐trial原行、audit的具体最终极值均没有凭这些SHA补出。

可以确认此源码／输入组合在原完整预算内完成了四程序；不能从本次运输UTC、缺失的backend统计或不同旧run的部分进度声称一个已测定的提速倍数。也不能因未发生编译停止就认为记录系数导数的全部误差责任已付。

规则同步实际round0至4成功，UTC分别01:58:53、02:44:00、03:29:04、04:14:08、04:59:16。原runner3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde的2700秒pull/rebase/diff与新规则停止责任保留，本次未返回规则退出原因。

## 7. 必要读回失败和quiet／清理

93335 reader先在本job临时树读取原owner/four-component JSON、必要stderr及quiet来源，构建选择后的对象，再经 exact_metadata_references 处理逐字相同的metadata引用。其 write_result 检测编码长度111829 B超过90000 B，替换为原错误回复，字段为：

- reason=necessary-original-metadata-over-90000-bytes；
- readback_exit_code=70；
- summary_complete=false，transport_complete=false；
- scientific_failure_not_inferred=true；
- cleanup_allowed=false；
- no_scientific_data_split_encoded_or_truncated_to_fit=true。

不能因为源码此前尝试读取原对象就说聊天中已看到完整111829 B或每个矩阵；它只支持“本job reader运行到了长度检查”，其返回范围仍仅795 B。也不猜是哪一表占了多少字节，因为完整尝试对象没有返回。

05:38:14.1494661 UTC，实际步骤报 Process completed with exit code 70。05:38:14.2797868 UTC，最终清理返回：

- event=native204_final_cleanup_skipped；
- reason=necessary-readback-or-quiet-not-complete；
- matching_processes=[]；
- no_raw_upload_follows=true；
- runner_teardown_may_reclaim_temporary_files=true；
- not_a_scientific_acceptance_gate=true。

所以清理步骤success表示条件清理脚本完成，**不是删除完成**。原child被wait/reap及wall_guard返回已观察，最后进程匹配为空；但必要摘要的完整cleanup_evidence未返回，不能补为一个已读取的全quiet收据。代码按条件不主动删除本次raw，仍不能保证已结束runner的临时文件以后可恢复。没有上传artifact／Release／Git，也不承诺靠路径或SHA恢复。

## 8. 本次已付与继续责任

本次可登记的进展是：新源真实完成完整128 owner与fresh replay、全部请求stage maps、全112边界响应、混合338×112端点程序和独立原C-based审计程序。保留原native/full-DN未接受，不把有限程序完成改写成准确连续几何证明。

当前直接缺口是**必要结果选择过大而未返回关键原数值**。后继如改reader，应对真实结构作紧凑必要选择，保原owner/trial计数与必要原值、各组件完整范围／原异常／物理与线性readback关键极值／实际backend统计，重复大表只身份与范围；不能通过分块、编码、缩科学范围或放宽数学阈值来回避90000 B限制。任何重新求取都须独立实际run、同原科学合同和原期限，不能冒本次未返raw已恢复。

本结论不创建新的验收步骤。原R402记录系数线性化、R405／R414实现边界、C与真实F导数区别、混合second差分、原full-DN与连续metric／reach／held责任继续分别列账。后续以实际返回的必要科学数值决定方向，不凭本次缺失数据预判某个原门通过或失败。
