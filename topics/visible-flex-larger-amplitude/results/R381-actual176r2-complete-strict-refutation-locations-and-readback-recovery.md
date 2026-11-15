# R381 — 实际176r2完整找回38条速度域反证及其共同u位置

作者：ChatGPT /root/exact_refinement（AI协作）；2026-11-15。

**实际176r2已完整恢复原165的32977条最终cover事件、32526条pending/refuted事件及全部38条反证的必要位置与原界。** 全部38条均属于数值分片416：17条为准确速度下界达到或越过+1，21条为准确速度上界达到或越过−1；没有一条被标为半径反证。它们按原端点字面连接成下文两个闭区间。全部32488条未决记录也属于分片416，其原原因分组现已完整读回。

本次只对已保存的官方日志作运输、JSON、原字面字段与SHA工作，没有重新计算C、准确目标、区间、多项式、native、FD或ODE。新reader的成功补齐[R356](R356-actual165-finite-target-bound-and-strict-speed-domain-refutations.md)尚未读取的位置责任，并修复[R374](R374-actual176-original-refutation-readback-count-and-transport-limits.md)所记首轮读回限制。**原165的科学exit4、严格域反证和工作宽度未完成均不改变。**

## 1. 本次实际身份与唯一小日志

- 请求176，revision2；schema为actual165-original-log-selected38-bounded-columns-readback-v2。
- 官方run：[43748206814](https://github.com/Rogerhu12/math-research-public/actions/runs/43748206814)。
- source commit：48e55d2e0f6f07405c216b5417ef97844654124e。
- job：132916103550，original165-refutations，全部步骤success。
- 实际reader：root_20261115_read_actual165_strict_refutations.py，32670B，SHA256 2e5717de6c1d00059e995f398384bd5758f9e2c8f2657484bd651d66cf950371。
- 请求JSON：7083B，SHA256 3ba3e2a207476c7596a06f42df8e46dd11255d13ba5140a72780bbe4605a2b7b。
- workflow：6477B，SHA256 41fe2cdf8bce4dbcd2577c2a2566fb14a4538ff0a6f710caad99fe50321140f6。

本次唯一取得的是这个新job的小日志，82899B，SHA256：

    9344f540e9e49b99a0fbdf7b56427dfb7b23ccd44eb7802a014e2f690f514111

它含一份BEGIN_REQUEST176_ORIGINAL165_REFUTATIONS_SUMMARY帧。帧内完整ASCII JSON加最后一个LF共55100B，SHA256：

    46ac562a355be51374e186fa3368ca20693e262918115dd3d8337eaaac77b867

这与紧邻的request176_summary_identity原字段逐字吻合；该事件明确hash_includes_final_LF=true、reader_exit_code=0。必要摘要没有拆段，没有再次输出原完整科学enclosure。日志原字节身份保留；解析视图仅在每个物理行首去一个运输BOM，再剥GitHub时间戳，不改正文BOM或原数字字面。

原临时readback result.json为54869B，SHA256 d8ea2a27dd7df18e5496df8d9e9ae6896d564a00825682d385b8345026dd53a8。这是原reader报告的文件收据；本文实际逐字核的是上面的55100B必要摘要帧，不将二者混为同一文件。

## 2. 原165输入没有更换，也没有重跑科学

原输入仍为：

- run43736208020，source1f2ec637430e5c6b27b1a93720e106539281a156；
- job132879253906，原官方终态failure；
- 原consumer94125B，SHA256 61b98b3e853b31535ac31b66d4cf4513f1271d9852acfb09b948990a30acb205；
- 原完整target result105512B，SHA256 e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619；
- 原input-binding62398B，SHA256 996593f3a615c3694596463c949990a4967cc5c5a1bf48b100fbc4e149e73e48。

reader在本次Actions内从官方重定向完整流式读取原日志；没有把token转发到重定向地址，也未把签名URL写入日志。原流实际1486048285B、165009物理行，SHA256仍为：

    4ab8c6d688a27869353bb428288d467502c7aed6ad8cd96140a6cfaea508aea2

full_log.complete=true；raw_log_saved=false。本地没有取得这份1.48GB旧日志，亦未将它存入Git、Release或artifact。原完整target result由Actions内部的9段旧协议恢复并核原bytes/SHA；本次新输出本身不使用分段协议。

实际metadata扫描耗时65.90910600900001秒，resource_partial=false、error=null。这些是原reader记录，不是对未来扫描耗时的保证。

## 3. 完整cover与pending身份现在闭合

| 原记录范围 | 本次逐事件读回数量 | 原结果要求 |
|---|---:|---:|
| 最终cover事件 | 32977 | 32977 |
| pending或refuted事件 | 32526 | 32526 |
| unresolved事件 | 32488 | 32488 |
| refutation事件出现次数 | 38 | 38 |
| unique refutations | 38 | 38 |

全部38个pending反证node集合与最终cover反证node集合相同。对每条必要表记录，原pending对象、原完整enclosure、原cover事件均保bytes/SHA及日志位置；原准确a、a_s上下整数与二进制指数逐字保留。本次只选择必要字段，没有重新判断区间不等式或生成新的界。

原状态为：

    readback_complete = true
    selected38_full_enclosure_links_observed = true
    complete_necessary38_table_returned = true
    all38_necessary_original_locations_and_bounds_selected = true
    summary_complete = true
    transport_complete = true
    reader_exit_code = 0

incomplete_relevant_segments、malformed_relevant_record_identities、identical_original_duplicate_events均为空；nonobject_relevant_line_count=0。全部原65535个node事件、32558个atomic-split事件也在原事件分类计数中保留；这不表示本文取得或逐项重新计算它们的科学内容。

首版176原扫描虽到EOF，仍只计到32667条cover、32480条pending和32442条unresolved，且原必要摘要95577B超过90000B，故诚实退出。r2没有放松finish中的任一个原总数或集合相等条件，而是完整满足它们；因此首版读回失败不能再被解读为原科学日志缺失。

本次原大日志实际发现708个物理行首UTF8 BOM；r2只在解析视图逐行处理它们，整流SHA不变。首版与r2还包含必要表列式去冗余及事件词法白空格处理的显式差异。本文没有对每一条首版漏计事件另作归因扫描，故不将全部漏计无条件归为同一个具体运输位置。现在可确证的是：这些狭窄读回修正后，原全范围校验及38条身份均完整通过，而原科学结论未动。

## 4. 两段已严格反证的共同u闭区间

必要表全部numeric_piece=416，classification均为rigorous-domain-refutation，radius_refuted均false、speed_refuted均true；原a与a_s界的binary_exponent均为−320。

原consumer反证语义仍是：

    radius_refuted = accurate_a.upper <= 0
    speed_refuted = accurate_as.lower >= 1
                    or accurate_as.upper <= -1

因此这里的“严格反证”是反证原开放条件|a_s|<1；即使界恰等于±1也足够，并不要求本文另证明一个正的小数超界量。

下面的合并只检查相邻记录的u_right与下一条u_left原字符串完全相同，没有求有理数和、除法、近似端点或新的多项式值。所有原接缝均保留为闭端点。

### 4.1 正向速度反证的17叶

原表在下列闭区间连续排列：

$$
U_+=\left[
\frac{2469601910595947097251}{4287221271914621173760},
\frac{6458301611822707498381}{8574442543829242347520}
\right].
$$

这17条的原a_s界均属于lower≥1分支；所以下述节点覆盖的整个U_+已不满足原开放速度域。完整node_id顺序为：

    31034, 8158, 612, 488, 464, 448, 434, 441, 449,
    457, 489, 511, 985, 2429, 4341, 15787, 61525

相应原depth为：

    20, 18, 12, 9, 7, 5, 3, 4, 5, 6, 9, 10, 14, 16, 17, 19, 21

例如原node434、depth3的原闭区间为

$$
\left[
\frac{19699701273560659}{32708902526204080},
\frac{5574797829496243}{8177225631551020}
\right],
$$

其原准确速度包围逐字为

$$
a_s\in[
3414888795451522947726446574698868555788129920221208551624217548477795475344594653277498940097389,
5915201947982508109468169483589474207184811914279633881351240553721944584276826895038560673950482
]\,2^{-320}.
$$

这里只引用原有效界和原反证分支；没有把长整数除以2^320另造小数，亦没有以一个代表节点代替其余16条已读必要记录。

### 4.2 负向速度反证的21叶

第二组原闭区间连续排列为：

$$
U_-=\left[
\frac{1355055645771943875395}{1714888508765848469504},
\frac{8412884171125792686211}{8574442543829242347520}
\right].
$$

这21条的原a_s界均属于upper≤−1分支。完整node_id顺序为：

    61528, 8162, 4344, 2432, 1472, 988, 616, 514, 460,
    444, 437, 445, 453, 493, 743, 989, 1473, 4345,
    8163, 31039, 61529

相应原depth为：

    21, 18, 17, 16, 15, 14, 12, 10, 6, 4, 3, 4, 5,
    9, 13, 14, 15, 17, 18, 20, 21

例如原node437、depth3的原闭区间为

$$
\left[
\frac{13749085703416799}{16354451263102040},
\frac{30097661451257911}{32708902526204080}
\right],
$$

其原准确速度包围为

$$
a_s\in[
-11313151426453958967655781723721221545348619835995428678452913725984752587392450266755242862580149,
-8272025944418854421712492012119729436279063600808296063710382070997250286856473945087469358735018
]\,2^{-320}.
$$

两段只是本次已证明的反证子集，不能把它们声明为全部真实坏点集合；其外仍有已证明域或未决范围。numeric_piece=416也只是原字面分片身份，本文没有未经原definition映射就把它改称某个特定支撑或某一个控制系数的单独作用。

## 5. 全部未决原因已能定位，但不能反推唯一算法病因

本次unresolved_numeric_piece_counts仅含：

    {"416": 32488}

原depth分布：

| 原depth | 未决数 |
|---|---:|
| 20 | 28480 |
| 21 | 4008 |

原互斥原因组合：

| 原reasons完整组合 | 数量 |
|---|---:|
| 仅relative-target-work-width-unresolved | 32484 |
| 仅accurate-open-unit-speed-domain-unresolved | 3 |
| 两者同时 | 1 |

因此原reason逐项计数为相对目标宽度32485、准确开放速度域4；两项有共同记录，不能把它们直接相加当作unique叶数量。所有这些均为旧事件的分类计数，不是新算的区间判定。

这比R356的总量信息更具体：工作宽度未付主要集中于同一分片的相对目标比较；只有4条unresolved记录还含速度域未决。同时38条已经严格反证，不能与这4条或32488条普通未决混为“还需更多细分”。

这些原因标签本身不提供各叶d0/d1、Bernstein系数、上游C关联或真实误差大小，故仍不能据其数量宣称某一种区间依赖是全部未决的唯一原因。本文也没有从这些计数推出实际场的误差或native求解表现。

## 6. 原数学结果和所有未付责任保持

原165记录仍为：

| 原字段 | 原值 |
|---|---|
| full_public_u_closed_cover | true |
| full_accurate_radius_positivity_proved | true |
| full_accurate_open_unit_speed_domain_proved | false |
| full_accurate_nine_parameter_domain_proved | false |
| at_least_one_accurate_domain_interval_rigorously_refuted | true |
| comparison_work_goal_complete | false |
| complete_unvisited_coarse_count | 0 |
| scientific_controlled_exit_code | 4 |
| error | null |

原cover32977叶中radius_proved=32977、speed_proved=32935、domain_proved=32935、relative_goal_met=481、rigorously_refuted=38、unresolved=32488，未改变。停止原因仍为maximum-evaluated-node-budget-before-two-child-transaction。

原参数、准确L、字面ell、全部九支撑、原256位Tree平方根与320位外网格包围责任以R356及原绑定为准；本次不再输出大科学表。准确目标比较的1/10000000仍仅为工作宽度目标，未新增native门。原有限共同相对目标上界及正半径结果不消除速度域反证，也没有取得一个已接受的同场几何。

以下范围均未由176r2支付：重新求当前九参数的可行点、真实C尾非线性响应、全部112场、current J、native/fullDN、338终边界、mean/sensitivity、独立最终审计、全局reach或held。纯日志读回成功不改变这些范围，也不为175或其它正在运行的科学任务增加前置门。

## 7. 下一实质动作与复现路径

这一新增定位已足够说明：单纯增加同一准确参数点的节点预算不能抹掉U_+、U_-上的有效反证。若后继要建立新连续family的真实可行场，应明确调整参数或构造，再重新支付同一准确域；不能把旧搜索点自动改为零、不能重标旧profile或把数值参考当作准确目标。

对相对目标工作宽度，已有明确分片416及原未决原因定位，可在真正选定的可行参数点上研究共享量、上游准确包围或原分片收窄。这里不指定未运行的方向、半径或接受结果，也不将再次搬回大表作为新门。

复现本次读回只需本节固定的reader/request/workflow与原165官方job日志；运行仅解析原字节，不需要重跑C或科学程序。原105512B result及所选38条完整enclosure的身份与保留cover关联已在公开Actions内部核完；没有将其余全部大enclosure回搬。本地仅取得一份55100B必要摘要并核全部38条的字面字段与原位置。raw_Git_Release_artifact_uploads=0，new_output_segment_protocol_used=false。成功后workflow清理本次owned临时读回文件，保留原run/source/参数/必要结论和输出SHA。
