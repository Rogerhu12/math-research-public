# R341 实际151完整公共坐标覆盖、节点预算停止与未付目标误差

作者：ChatGPT /root；日期：2026-11-15。状态：实际Actions报告原值与来源已读；计算job的巨量原日志尚未经连接工具返回，本文不冒完整原frontier已经由root逐项读取。

## 341.1 本次确切结论

实际151给出完整公共坐标u∈[0,1]闭覆盖，并保存原全部419数值分片及其接缝两侧。目标消费者在65535个已评价节点处停止，因为下一次替父操作需要同时支付两个子节点，而声明上限是65536。原实际elapsed_seconds_including_binding为127.38605653900004秒，没有耗尽900秒科学时限；resource_stop_reason恰为maximum-evaluated-node-budget-before-two-child-transaction。

最终current cover有32977叶，refinement queue有10468项，complete_pending_or_refuted_rows也是10468。完整粗覆盖尚未访问数为0，interrupted_transaction=null，error=null；原controlled exit code为3。它是有效覆盖下的未完成包围，不是严格域反证。原rigorously_refuted=0、at_least_one_accurate_domain_interval_rigorously_refuted=false。

完整准确九参数域、严格半单位速度域、全域半径正性、有限全域目标相对界及comparison work goal均未完成。global_delta_upper=null，whole_prefix_relative_delta_below_one=false；同一场metric/native/fullDN/闭场/全t/reach/held均未付。不能以procedure_complete或transport_complete=true将这些字段改成已证明。

## 341.2 实际运行和读取边界

| 项目 | 原值 |
|---|---|
| repository | Rogerhu12/math-research-public |
| 请求 / run | 151 / 43724306509 |
| 固定科学source | 618a9369d2bd45210767e294726cec10be1cd2df |
| compute | 132842781513，failure |
| report | 132859348081，success |
| target消费者 | root_20261115_continuous_nine_target_enclosures.py，69431 B / 6dfb79be9b77e85ffff496e4349b9c6b01c1ab74f28d0a64bf76d4dc8cadb768 |
| request | public-continuous-nine-target-enclosures-request.json，13405 B / a4894d6bc0388121c07e6b4b47d019d1004a14f5a44878415ba9f1f7e9cfffe3 |
| workflow | visible-larger-public-continuous-nine-target-enclosures.yml，50748 B / 3995b487f98f3c61cf28cc0418f666c9cb1ae6748156930718fb889f4ed5a9e9 |

前13步骤完成来源、同C、cut两jet、原147原子构造和中断metadata保全。第14步目标包围返回failure，第15–17步原输出恢复/范围读回/清理均success；report四个报告步骤success。这里的failure具体由上述controlled exit3解释，不把report绿色当目标达到1e−7或课题1e−6。

root通过官方GitHub工具一次取得report完整文本：399002 B，SHA-256 `6b1e76bec961ba7d8581a7e4e70b7767bd1587a345bbbc47b61e410fcdea7b3b`。其中包含四个实际原JSON块；去日志时间戳后，按原LF约定逐字核得：

| 原块schema简写 | 字节 | SHA-256 | LF约定 |
|---|---:|---|---|
| request147-original-continuous-E-actual-scalar-summary-v1 | 38183 | `961c6101dca1555b367c87deecd37008b27ddee86809976057a9ab745b93bc5d` | 不含分隔LF |
| R286-v3-original-binary-cut-complete-twojet-hull-v1 | 5831 | `877124bba63e7e474292b1cb093da67b6f098cd9611499e69281a515e4bd3c07` | 含末LF |
| request147-actual-v3-continuous-nine-construction-v1 | 27187 | `7cc2fd4f4801d9ca5b632f81dedbc4948c763a8e9ac8a1c7d641467409b1703c` | 含末LF |
| request151-common-u-complete-nine-target-enclosures-v1 | 5137 | `7319fbe3dbbd5d11d9e802a285ba53f649bc49603805ab84a0427e0966bd6eb2` | 含末LF |

compute大日志读取一次返回Transport closed，没有取得正文。该错误不是原科学程序报错，不能据它猜测输出缺失或日志被删除。本文没有拿到完整原节点/队列/事务流，也没有核两个job的完整块逐字相等；report中的complete_cover_and_all_pending_records_printed_before_cleanup=true及transport_complete=true是原producer/reader字段，保留其来源语义，不改写成root已经独立全读。独立163只读日志恢复继续支付这一传输责任，不作新的科学接受门。

## 341.3 同C上游及原cut两jet

本job重新执行原同C生产器f12f7470…，科学结果32114 B / `3e76f50299df2e06085c137159cbf58b06e58c9059a03ff1a2b2302caeff2d8f`，实际2758.3906046959996秒。完整1440原片、六primitive、有限接缝、protected join及两query闭域完成；没有未访source或query后缀，原deep根序列仍未选择。

same-C原ledger身份与[R339实际156](R339-actual156-complete-C-head-and-partial112-cut-transfer.md)中的对应定义相同：六primitive2079629833 B/30336b8a…，原径向源25513827 B/da2ba4cb…，全部query逆像197572200 B/98188fa6…，未付分辨率5209016 B/9964a6e6…；这些原值是在本job报告中再次声明的字节身份，不以此前raw替代本次输入。原whole query仍2609个合法粗叶、E显示[1e+0 +/- 0.161]，不冒全域工作精度。

名义cut保原binary64 word333333333333d33f，即5404319552844595/18014398509481984；自然Rout显示[0.30000000000000715908123386 +/- 6.75e-27]，与cut的差显示[7.1701834641e-15 +/- 1.01e-26]。原cut反像恰一个head叶，span[0,1)，工作分辨率未决数0。原两jet读数5685 B / `5603642192276aebc735c600d2b3b41bc6c7efd27152fb04a45ba39fbc9fd01a`。

| 原cut量 | 准确闭dyadic端点 | 原full width |
|---|---|---|
| E | [297036851754023534385, 297036860731551973169] × 2^(-68) | 8977528438784 × 2^(-68) |
| E_r | [-1377364570695686333, -1377334639942752445] × 2^(-62) | 29930752933888 × 2^(-62) |
| E_rr | [-18506607869532518095, 3541147354781501745] × 2^(-57) | 22047755224314019840 × 2^(-57) |

这支付同一个cut叶的E、E_r、E_rr闭包围；原v3工作目标只要求E值宽度，没有给Er/Err加新接受门，也没有由此给出DN或准确同场metric。

## 341.4 原147原子构造和明确九参数

151保留的原147构造仍按[R323](R323-finite-cut-boxes-and-explicit-uniform-dyadic-windows.md)选择κ=1/2、collar d=1/524288、首末transition宽1/1024；全部十一严格条件true。准确新模型定义377789 B / `9ac99b2722d7a6f4d02cd51420d6428c878a9712763bc679f07f6d2a8154d235`已经创建。

父参数只取实际146/R320末值，不转成149、154或157末值；状态、J、merit、旧radius和旧tail结果未继承。

| 参数 | 原binary64文字 | 原little-endian word |
|---|---|---|
| p1 | 0.3055213835477326 | 5c3ca48fa98dd33f |
| p2 | 0.21645013203050154 | eb97244fa3b4cb3f |
| p3 | 0.34270051957744246 | 9511fa28ceeed53f |
| theta1 | -0.06322334619266512 | 28be3dbc672fb0bf |
| theta2 | -0.01747451701873286 | 2d776ffcd6e491bf |
| theta3 | 0.9376115689625685 | 937421fae900ee3f |
| eta1 | 1.0751306255033548 | 5d70b72bbc33f13f |
| eta2 | 0.6886900390922872 | 4a6f5fb1bf09e63f |
| eta3 | 0.9385431607625546 | 3182abaa8b08ee3f |

基础无控制域原452叶全部受证、processed485；原九参数域pass单独耗时301.86709364599983秒，1735 passed leaves、23975 processed nodes、10454 unresolved terminal leaves、16未访栈项，complete=false。其345150413 B ledger SHA为 `3afe3fab7487f2ba3641e764fc65cebe43dd5fab787acd55d53d5e4f67b92749`。这组旧原子域记录与151后置公共u目标消费者是不同算法/不同责任，不能互换计数。

数值profile编译完整419片和418接缝；207对三jet逐word相同，另外的接缝不因此被称为准确C²。数值规范270229 B / `6be4c7ded4cc64743a8ba43782830422cb616a44a83e24db9854832fed94c64a`，编译canonical SHA `064c694ac84f6d432f70bcdc6f24ab4cb47d16bedfca3fc50a87576328109e90`。其数值长度2.723563252110879及cut代表来自自己的编译叶，不冒准确目标的共同真实C成员。

## 341.5 后置公共u消费者的全部已报状态

消费者使用原同九p、全部支撑、所有可能准确piece/控制、数值lookup两侧与不clip的原数值局部变量。先保419个完整粗盖，再以两个子节点同时替换一个父叶；源定义/公共坐标和原数值长度的区分沿[R326](R326-common-coordinate-target-enclosures-and-same-field-metric-transfer.md)、[R330](R330-centred-common-coordinate-difference-and-target-coefficient-bounds.md)。

| 原范围/状态 | 原值 |
|---|---|
| current_cover_counts.domain_proved | 32780 |
| current_cover_counts.leaves | 32977 |
| current_cover_counts.radius_proved | 32879 |
| current_cover_counts.relative_goal_met | 22514 |
| current_cover_counts.rigorously_refuted | 0 |
| current_cover_counts.speed_proved | 32780 |
| current_cover_counts.unresolved | 10468 |
| completed_node_records | 65535 |
| evaluated_node_attempts | 65535 |
| current_refinement_queue_count | 10468 |
| complete_pending_or_refuted_rows | 10468 |
| complete_unvisited_coarse_count | 0 |
| full_public_u_closed_cover | true |
| full_accurate_radius_positivity_proved | false |
| full_accurate_open_unit_speed_domain_proved | false |
| full_accurate_nine_parameter_domain_proved | false |
| at_least_one_accurate_domain_interval_rigorously_refuted | false |
| full_target_relative_bound_finite | false |
| comparison_work_goal_complete | false |
| global_delta_upper | null |
| interrupted_transaction | null |
| scientific_controlled_exit_code | 3 |

上表是各自原字段，不能把这些有重叠定义的计数擅自当成互斥分区。没有完整frontier正文时，本文不猜10468项各自落在哪个支撑、哪种谓词、哪个闭区间，也不猜单一主因。全部原定义和记录由source/完整流SHA绑定，163继续读取。

原target policy为900秒、grid_bits320、原tree sqrt bits256、最大深度32、最大评价节点65536、比较工作目标1/10000000。停止记录明确是两子事务前的节点预算；没有丢一个已替出的父叶或记录半个子事务。本文只依据原算法与实际summary说明这一保持闭覆盖的语义，没有声称重新运行区间树。

## 341.6 已给出的准确长度和径向系数差

原literal总长是准确有理数

$$
L_{\mathrm{literal}}=6132919223663265/2251799813685248.
$$

准确新目标总长的原完整包围为

$$
L_{\mathrm{true}}\in[
5817495797978587951600625954867948311841826001286377790825445872266120557367955447600226036870001,
5817495798060272125493160855109471965123506575147906484289958839671069018287975799464298896827070
]\,2^{-320}.
$$

原公共u径向相对目标系数差闭包围为

$$
\Delta_{\mathrm{radial}}\in[
-29991427844989880973945738594146434624155381050836170410860236025662184032800175485685,
29991885433470724853527855143664892931431252586027647993413842198112339333113577211684
]\,2^{-320}.
$$

这些整数原字直接抄自report，没有在本地转换为浮点估计或再作科学四则。accurate_target_never_replaced_by_numeric_length=true；原angular/域责任未付，所以不能以这一径向界单独构造全域operator相对δ。global_delta_upper=null必须保留，也不能把空值当成0、无穷或严格反例。

R330的η+δ+ηδ转移仍要求同一个实际场的参考metric界和完整准确目标δ；本次没有该场或完整δ，不能用此定理替未付前提。

## 341.7 原文件身份及未取回内容

| 原临时文件/流 | 字节 | SHA-256 |
|---|---:|---|
| complete_cover_transactions | 18137631 | `b1a68bc1390908d0e0cb57d7b950b3ab779322e0fa04998256d9d3a465aca27a` |
| complete_frontier | 88905408 | `a8a87f59c96e92106ca774cdf892b7e1743f089b9a8ba30e648402d3ad9cb9bd` |
| current_cover | 267198234 | `61350c911aae16e5a17000ecc1d94f724d5bce10c11a1a0e95e49c4c8d07f247` |
| evaluated_nodes | 526666191 | `242f9dcf852bc76aca516a87e2d3e1702c79e407ac7ef56aea4c5aaed88d65da` |
| original_query_plan | 52193 | `d413d4f414199d842e6f7800fc0753f4edc1ad30e9a3e427cd62075c4faedcb4` |
| complete_result | 101961 | `95fa1e1104cf5dcfbf154bbba1b55e27bd1afb685dd82a51cec255d67ba08f94` |
| input_binding | 62020 | `6ed65011f5235f923123ccbcc529b8011bb0389aa3a6c155388ee7373d21c4cb` |
| grid_conversion | 1533021 | `12794fb7e461a421b20c29e1383f26c867242feecf2b2dc599872f71eb13c9fc` |

完整result101961 B超过单一小文本的100KB范围，原consumer声明已按9个数据段输出；input binding62020 B按6段，grid conversion1533021 B按128段。这里的segment计数和SHA来自实际report，不表示root已收齐原compute段或可从hash恢复原文件。

原current cover约267 MB、frontier约89 MB、evaluated nodes约527 MB，都是可重算的临时记录，未写入Git、Release或新artifact。原cleanup步骤成功；若需要再次取得输出，先读取仍存在的原Actions日志，只有日志确实不可用时才按原source/recipe重算。163的日志读取不产生新模型/FD/ODE，也不重新排序数值结果。

## 341.8 规则与后继实际工作

原C runner从2026-11-15 14:26:22 UTC到15:12:21 UTC，science/wrapper return0，sync rounds2；原构造runner从15:12:25到15:17:28，science/wrapper return0，sync rounds1。两报告均README_change=null、periodic_sync_failures=[]、scientific_checkout_modified=false。本地API读取与日志核SHA不是git pull，H保留另行实际pull记录。

后继先从完整未决记录区分域隔零、角系数工作精度、准确输入盒宽度和树调度的责任。若改变节点预算或包围算法，使用独立明确请求，保全部九p/419片/两侧/原目标以及完整原未付范围；不把一次预算停止称为根不存在或目标违反1e−6。159的真实新profile→H→FD/full453实验继续，不把这份充分区间域证书当它新增的前置门。完成标准仍按README，不能在本报告收尾。
