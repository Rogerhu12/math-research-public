# R356 — 实际165的完整正半径、有限相对目标界与38条严格速度域反证

作者：ChatGPT /root/exact_refinement（AI协作）；2026-11-15。

**实际165在同一准确九参数目标上取得完整闭覆盖、全覆盖正半径和一个小于1的有限相对目标上界；同时原consumer记录38条严格域反证。** 科学步骤以受控exit4结束，error及interrupted_transaction均为null。它也用尽65536节点预算允许的65535个实际节点，仍有32488个未决叶。严格反证、宽度未决和资源停止是三项同时存在的事实，不能只把这次failure写成“算得还不够”。

本文完整读取官方report job中的四份原摘要并核原帧字节及SHA；没有重算任何区间、范数、多项式或模型。原compute中的大逐节点/cover/frontier科学表没有通过连接器搬回，也没有声称逐项读取38条反证的u位置。第8节明确区分报告已证明的范围与这条未读边界。

## 1. 官方身份与真实输入

- 请求：165。
- 原run：[43736208020](https://github.com/Rogerhu12/math-research-public/actions/runs/43736208020)。
- source commit：1f2ec637430e5c6b27b1a93720e106539281a156。
- compute job：132879253906，failure；target enclosure步骤failure。
- report job：132897872239，success。
- 新consumer：root_20261115_continuous_nine_shared_target_enclosures.py，94125B，SHA256 61b98b3e853b31535ac31b66d4cf4513f1271d9852acfb09b948990a30acb205。
- 原151 consumer：root_20261115_continuous_nine_target_enclosures.py，SHA256 6dfb79be9b77e85ffff496e4349b9c6b01c1ab74f28d0a64bf76d4dc8cadb768，仅作为已绑定来源，不导入执行第二次。
- 接线固定21个source/依赖条目；原147原子请求17398B/SHA256 4b6f78bb25e0d87354e2ad786637fc9e4db5c7c34774d3cad4716638552ba707，保其来源身份。实际C重建预算已显式为3600秒，不冒原147的1800秒。

本次运算保持[R326](R326-common-coordinate-target-enclosures-and-same-field-metric-transfer.md)、[R330](R330-centred-common-coordinate-difference-and-target-coefficient-bounds.md)的共同u目标，采用[R352](R352-shared-calibration-normal-forms-and-complete-Bernstein-target-enclosures.md)的共享校准表达式和完整Bernstein。没有用数值长度ell替代准确长度L，没有丢掉任一九控制支撑，也没有把当前九参数自动改为零。

真实参数来自实际146末参数，原recipe顺序为

    [p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]

原字面为

    [0.3055213835477326,
     0.21645013203050154,
     0.34270051957744246,
     -0.06322334619266512,
     -0.01747451701873286,
     0.9376115689625685,
     1.0751306255033548,
     0.6886900390922872,
     0.9385431607625546]

来源run43716274591、commit69765fcd81ca84819cdeb09c4fe14c55fdb5fb80。只传这些真实参数和provenance；未导入旧状态、旧残差、旧J或旧尾结果，亦未声称旧设计目标的接受可跨到新连续目标。

## 2. 四个原摘要及LF口径

官方report日志共417817字节，SHA256：

    82b5a074e953159c069d8a7886319be97e0b37a81aeab7b9d14a7c2d3e6cf64d

这是包含GitHub时间戳/BOM的原下载文本身份。剥离运输时间戳后，四个BEGIN/END帧逐原文本保存于临时会话记录，身份如下；没有先把JSON数字解析再重新格式化。

| 原帧 | 校验字节 | SHA256 | 最后LF |
|---|---:|---|---|
| 原C/E scalar summary | 38183 | c20a79ed9336a2eda8e4f1e1969113d52c784b5bca2ac8f5753ad9f1274f75d8 | 不含 |
| 原cut twojet summary | 5831 | 140f907da871ed693ab9826640d4c84c8cab05bfedb96efd4f2c43b4b8b8f24b | 含 |
| 原construction summary | 27207 | 6ff7fb33455be8dbc4eef1eb819a8f7b90329c8575c442dc810c83db13117fb8 | 含 |
| 新target summary | 8876 | 24bcda5bba76001c187c14d7b145e3607255c1e75e55b6bde9ea272bb123277f | 含 |

新target原完整result身份为105512B/SHA256 e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619；它的完整分段与原大科学表在compute日志中。本文没有把报告中的这个SHA当作已经亲读完整result的替代证明。

target summary的summary_complete、transport_complete、procedure_complete均为true。这里procedure_complete表示本次受控过程返回并保全声明的状态，不表示所有数学要求已通过。

## 3. 前置C、cut与原两域构造确实执行

原C生产者仍为geometry_20261115_stored_continuous_E_cover_v3.py，SHA256 f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df。

实际耗时2591.6873325710003秒。完整1440个原piece已付，full_finite_head_complete、all_requested_closed_query_bounds_complete、continuous_convention_C_query_enclosures_complete均为true；error=null，源与query未访问后缀均null。原计数为121832 integral_panels、200000 inverse_cover_nodes、307101 rigorous_analytic_component_integrals。

因此这次3600秒预算实际避免了“1800秒前置未完成就没有cut”的那种范围缺口；不能把这次耗时改写成所有重跑都需要或都只需要同样时间。

两原query的结论分别为：

| 原query | 完整闭域包围 | 原工作分辨率 | 原范围 |
|---|---|---|---|
| 原binary cut点 | true | true | selected point leaf 1，refined_nodes=5 |
| 完整natural-domain | true | false | 原inverse-cover节点资源停止，2609个工作分辨率未决片段，未省略域后缀 |

原自然外半径显示为[0.30000000000000715908123386 +/- 6.75e-27]；与原binary cut之差显示为[7.1701834641e-15 +/- 1.01e-26]。这些是原显示字段，不是本文另算的数值。

原cut三项E、E_r、E_rr均有完整保留的有理/二进制包围；point_twojet_enclosure_complete=true。原E显示[1.0064000 +/- 3.04e-8]。没有把E_r/E_rr的宽度另加为接受门，也没有因自然全域的工作宽度未达标而抛掉有效粗包围。

准确构造仍使用原core输入accepted.json.gz，2614352B/SHA256 b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff；新的选定geometry canonical SHA256为bf7b3c997d12599d08e2415cb41392a9dc72ffd33993aa169f1c146796858706。

R323选宽原recipe明确为：

- first/last transition width均1/1024；
- collar width=1/524288；
- kappa=1/2；
- cut仍5404319552844595/18014398509481984。

原factory两个域pass的状态：

| pass | 完整 | 原节点/叶计数 | 耗时 |
|---|---|---|---:|
| 零控制基底域 | true | 485 processed，452 passed，0终叶未决、0stack未访 | 0.19245074700029363秒 |
| 保全部当前九参数域 | false | 24476 processed，1735 passed，10705终叶未决、15stack未访 | 301.97585668099964秒 |

这两个原factory pass只提供它们自己的结果。165后置target consumer没有把九参数pass的false自动当成数学反证；它独立使用同一完整定义及原九参数进行了下面的包围。

## 4. R352后置consumer的实际全覆盖与严格域状态

target实际耗时581.166182384秒，包括binding。资源设置原样为：

- grid_bits=320；原Tree sqrt bits=256；
- 最大65536 evaluated nodes，最大depth=32；
- 最大900秒；
- 比较工作目标1/10000000；
- 原419个numeric piece，每一接缝保两侧闭表达式。

实际停止：

    resource_stop_reason =
    "maximum-evaluated-node-budget-before-two-child-transaction"

    evaluated_node_attempts = 65535
    completed_node_records = 65535
    interrupted_transaction = null
    error = null
    complete_unvisited_coarse_count = 0

这说明两子事务之前的节点资源限额被真实触发；未发生“删掉父盒后没有两个孩子”的覆盖缝隙。完整闭覆盖仍为true。

| 当前完整cover计数 | 原值 |
|---|---:|
| leaves | 32977 |
| radius_proved | 32977 |
| speed_proved | 32935 |
| domain_proved | 32935 |
| rigorously_refuted | 38 |
| relative_goal_met | 481 |
| unresolved | 32488 |
| current_refinement_queue_count | 32488 |
| complete_pending_or_refuted_rows | 32526 |

严格反证字段的源码含义已经亲读：

    radius_refuted = true_a.upper <= 0
    speed_refuted = true_as.lower >= 1 or true_as.upper <= -1

它没有把负下界、跨边界或普通区间过宽称为反证。全cover radius_proved=leaves，加上这两个互斥的严格条件，说明报告的38条反证属于准确速度域，而不是半径非正。这个判断是由原布尔语义及计数作出的逻辑推论；本文还没有逐条取得38个u区间、所属piece及具体as界。

controlled_exit_code=4的源码优先级是：若无程序error且存在严格域反证，则返回4；否则才按未完成的域/工作目标返回3。因此本次failure不能仅解释成65535节点资源partial，也不能误写成程序异常或native失败。原全部域与资源状态应同时保留。

这些反证只针对当前准确连续family的真实九参数与已绑定输入。它们不是“整个九参数family无可行点”、不是原搜索方程无根，更不是对尚未运行的native/fullDN作否定。

## 5. 已取得有限相对目标上界，但工作宽度目标未全付

原结果字段：

    full_public_u_closed_cover = true
    full_accurate_radius_positivity_proved = true
    full_target_relative_bound_finite = true
    whole_prefix_relative_delta_below_one = true

    full_accurate_open_unit_speed_domain_proved = false
    full_accurate_nine_parameter_domain_proved = false
    comparison_work_goal_complete = false

当前global_delta_upper是如下准确记录的上界数，不是误差等于该数的声明：

$$
\delta_{\rm upper}=
1439147673201427889014321102767032317508782960538102084933843480473202723375201762604878418
\;2^{-320}.
$$

本文没有将这个原整数重新除以2^320生成新的小数近似。其小于1由原result的whole_prefix_relative_delta_below_one=true给出。这个有限共同上界覆盖原声明的整个public-u分片目标；它并不证明所有叶都达到1/10000000工作宽度，也不消除速度域反证。

原准确总长L的320-bit网格包围为：

$$
L\in
[5817495797978587951600625954867948311841826001286377790825445872266120557367955447600226036870001,
5817495798060272125493160855109471965123506575147906484289958839671069018287975799464298896827070]
\,2^{-320}.
$$

原literal总长精确值仍为6132919223663265/2251799813685248。准确L没有替换成literal ell。

原径向相对目标差包围为：

$$
[-29991427844989880973945738594146434624155381050836170410860236025662184032800175485685,
29991885433470724853527855143664892931431252586027647993413842198112339333113577211684]
\,2^{-320}.
$$

不能仅由这些全局L/径向记录推断所有未决叶的主因。原节点d0/d1/a/as等尚需针对已保存日志读取；不能把global bound或未决数量反推出具体局部数值。

## 6. 本次共享依赖和字面参考的责任

原binding实际报告以下事实：

- 准确长度恒等式L=S3+d被使用。
- 三个支撑上的全部九项按各组至多8次多项式合并，all_Bernstein_coefficients_used=true。
- accurate_support_zero_jet_scope为core support0、first transition support1、coast support2，last/collar zero。
- literal_collar_calibration_defect_exact="0"。
- literal末collar局部坐标仍为1+(ell*(u-1)+literal_defect)/literal_stored_width。
- stored coefficients没有被替换成准确cut jet；numeric local variable没有clip。
- support右边界仍取left+storedwidth的准确和，未假定literal支撑不重叠。
- 原R330中心差和直接差取交仍保留。
- exact_root_leaf_correlation_not_fully_eliminated=true；没有声称本次上游C数值更准确。

新的input-binding为62398B/SHA256 996593f3a615c3694596463c949990a4967cc5c5a1bf48b100fbc4e149e73e48。原Q到320-bit外网格转换记录1533021B/SHA256 12794fb7e461a421b20c29e1383f26c867242feecf2b2dc599872f71eb13c9fc。本文知道它们由原运行绑定并在compute完整读回，但没有把这两个SHA当成本文重新逐节点核过所有转换的声明。

数值参考仍为419个原piece、418个接缝；207个finite jet word pairs完全相同。未相同word不自动证明准确目标不C²；相同word也不替代准确跨缝证明。literal参考的两个闭接缝表达式在共同u覆盖中均保留。

## 7. 为什么这还不是同场接受

原target与construction摘要均明确：

    actual_field_created = false
    native_success = false
    fullDN_success = false
    same_field_metric_certificate_paid = false
    true_IEEE_evaluator_error_bound_supplied = false
    new_native_acceptance_gate = false

连续目标与数值参考的系数比较是独立责任。即使得到有限delta<1，仍没有一个已接受的同场几何结果、当前C尾J、真实非线性尾、全部原终检或reach/held。当前九参数还存在原报告的严格速度域反证，不能把“正半径/目标比较”改名为“完整几何域通过”。

原C的准确root choice是对全部保留语义族的包含；并没有把某一深尾root的唯一数值选定、旧finite selector误差或某个旧J自动补齐。

## 8. 原字节范围与未读界

本次唯一下载的是report job原日志。四个完整小摘要已按原帧逐字读取，LF口径及其运输身份核对如第2节。全部新的算术发生在原公开Actions；本地只做文本、JSON、字节和SHA工作。

原target报告其大件身份：

| 原临时记录 | 字节 | SHA256 |
|---|---:|---|
| all-evaluated-nodes.jsonl | 725095854 | ca115681a0c51171335b24cba0d74c4bb360d6c61c837a3c9849190b61af5c4b |
| complete-current-cover.jsonl | 368023457 | 9cb05032524c188d01588580d122e25d61fe90adcd4e6e28dd4ff16608ced1c8 |
| complete-unresolved-frontier.jsonl | 373644653 | 97ddbb465ad8a839b72267d33ed88e94d8f2325fbdfb505853ed20b9409f94b4 |
| cover-transactions.jsonl | 19588091 | c086bfeeed645466821d493eb0f151f8083d5d89b7e52e459c27d2ab46072aba |
| complete-public-query-plan.json | 52203 | 63ac9529e48106bde0fb85e25620f8865eb43b23b28466746f9d5d0c35905b28 |

这些是**原运行报告的字节收据**，不是本文重新下载、重构并独立审完这些大件的收据。本文没有通过连接器取整份大compute日志，也没有编码拆传大科学表或保存raw到Git/Release/artifact。

因此这里已能正式记录原完整scope和严格反证计数，但不能补出38条的piece/u/as具体值，也不能断言32488未决叶分别由哪种依赖、曲率或目标宽度造成。若下一动作需要这些具体定位，可在独立Actions对原compute日志只抽取这38条已保存的反证及必要未决摘要；只解析旧JSON即可，不需重跑C、工厂或区间。

接线仅在cut_twojet、construction_readback、target_readback、scalar四个实际outcome均success后才允许清理。report中的complete_cover_and_all_pending_records_printed_before_cleanup=true是原consumer声明的读回事实；本文尚未亲取compute清理步骤原文，故不另称自己验证了其每个清理动作。目标科学failure不应被清理/运输success掩盖。

## 9. 对后继动作的具体意义

首先应把“当前九参数已有严格速度域反证”保留为真实科学约束。继续增加同一参数的区间节点，最多可以收窄其它未决叶或目标差；它不能使一个有效的严格反证因为多算而变成域通过。

若要继续构造这一新连续family的实际几何，下一实质变化应在明确的新family中调整参数并重新付完整域；零控制基底的本次完整域通过只说明已有一个可行基底，不能把当前九参数自动替换成零或冒成原搜索继续。具体参数/方向应由真实方程及后继实验选择，而非本文预定。

目标比较的1/10000000工作目标是另一条责任：在选定的真实可行参数点上，可以继续利用R352共享依赖、原上游C包围或更有针对性的分片收窄。它仍不能替代native/fullDN、同场绑定及原所有终检。

本结论先发布，不以搬回大表、额外数值fixture或另一轮审核作为新门。原源码、请求、run与上述输出身份足以明确重现路径；未读取、未执行或未证明的部分继续保留为未付。
