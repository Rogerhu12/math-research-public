# R371：actual164 r2 完成原二十档试探但全部拒绝，完整摘要因148101字节而未传出

作者：OpenAI ChatGPT（amplitude 协作代理）。日期：2026-11-15。

## 1. 已知结论与严格未读范围

[actual164 r2](https://github.com/Rogerhu12/math-research-public/actions/runs/43742275745)已完成。科学producer退出码为0，原phase为diagnostic-completed；原stop_reason明确为：

    All original20 real trials rejected; initial independent ten-state retained

accepted_point_count为0。因此，这次已越过[R364](R364-actual164-literal-binding-type-failure-before-tracked-model-calls.md)的类型比较故障，实际走过原二十档真实试探，没有接受新点。这里“全部拒绝”来自保存的原stop字符串和原producer控制流；不是把workflow failure直接解释成数学拒绝。

compute job最终failure的直接原因是metadata reader退出70：构造出的原紧凑摘要仍为148101B，超过90000B硬界限。reader没有强行截断或分块搬运，而是输出诚实的over-budget摘要。report job成功只证明这份小fallback被传出。

本次尚未读到所选候选index、六个响应/分数的实际正文、二十档逐档merit和域/Armijo理由、初末FD的实际误差与有效标志，以及Arb/圆场的实际门值。原status和科学临时文件已按原owned cleanup删除，没有artifact/Release或Git数据副本。不能把148101B的身份当作其正文已核，也不能从各section的字节数反推原数值。

这意味着本次能确认“完整流程返回且二十档全拒、没有新父点”，但不能判定每一档究竟由域还是merit阻挡，也不能据此证明六个宽形状均无下降方向、准确驻点、秩亏或新局部形状必会成功。

## 2. 运行与原读回身份

| 项目 | 真实值 |
|---|---|
| run | 43742275745 |
| source | bab76df48309984c2b78d898bdc84dc4019ca51f |
| 创建时间 | 2026-11-15T17:38:50Z |
| compute | 132897836261，failure |
| report | 132898181128，success |
| compute完整原日志 | 80969B / SHA256 48e3e4a059f0f863f83a3b609c534da04635c91bdff54f2c69ac5e4d0e946fbb |
| report完整原日志 | 15189B / SHA256 8b5222394bf6e8e355a84ad0bdecb0b8a58e637a2f2f09d8d3ebb68469465119 |
| 最终fallback，含wrapper元数据 | 5243B / SHA256 d7de8945e492caeb91713ec00709cdce687a8c1e4cd3fe5cb92bc3aad258e24a |
| reader原fallback，尚未加wrapper | 3847B / SHA256 0e0da6a12ceef29a488c05e433395958b4f139132ae0889eab13b578bd78b556 |
| 未传出的原summary | 148101B / SHA256 6733294343997e17bb9f57fce4b5822778b6c52c457d8350afb8844d18114856 |
| 原scientific status | 565694B / SHA256 7cbba62b0db919a4d15c0b5dd609932a0ef01a4ae57b36d582f660461a0824e0 |
| reader完整stdout | 7739B / SHA256 ba3a4be0d1b2de235d7a806cc627b145b18570f8be2bd795ea61b7d5c484cee8 |

摘要字节身份不含日志分隔LF。两job的BEGIN_VISIBLE164_COMPACT_SUMMARY正文按原文字提取；完整compute、report和reader错误通道原文均由同一代理读取，未重复科学计算。原reader stdout通过工程错误通道完整保留，其内容是section字节计数与小fallback，不包含未传出的科学大表。

producer stderr和reader stderr均为0B，SHA256均是e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855。producer stdout身份为405B/f82482257c48d3eced3f5fd7ae4c7bd6f8761358f5bb3e7ce92ef032d92e579f；因producer退出0，原always错误步骤没有另传其完整正文。本报告不假称从该405B正文取得了额外字段。

## 3. 已完成流程与返回值

原科学producer和外层工程状态必须分别读：

| 字段 | 原保存值 |
|---|---|
| phase | diagnostic-completed |
| accepted_point_count | 0 |
| child_exit_code | 0 |
| scientific_diagnostic_completed | true |
| started_experiments / completed_experiments | 1 / 1 |
| reader_exit_code | 70 |
| actual_scientific_step_outcome | failure |
| wrapper partial | true |
| wrapper_exception / traceback | null / null |
| explicit_wall_termination | false |
| received_signal | null |
| wrapper_wall_seconds | 28.020946971 |
| complete_original_readback_not_transported | true |
| scientific_failure_not_inferred_from_summary_size | true |

actual_scientific_step_outcome记录的是整个Actions步骤的结果；该步骤包含producer和reader。它不能覆盖child_exit_code=0与scientific_diagnostic_completed=true。wrapper partial=true在这里反映读回没有完整输出，不是producer2400秒预算中断。

producer固定源码中，diagnostic-completed只在实际试探之后的两次末端description、binary64投影、scalar域消费者及原circle消费者返回后设置。因此可以按源码顺序确认本流程到达并返回这些消费者；但description可以原样记录FD无效，域消费者也可返回不通过，返回不等于所有门通过。由于正文未传，本报告不填任何具体FD、Arb或circle通过值。

stop字符串位于原20次循环的else分支。该循环在每档记录真实evaluate、merit/域及接受判断，只有接受时break。本次该else与accepted=0一致。它不能给出每档被拒的具体原因；这些仍在已经清理的原status中，现只能保其身份。

原先六候选、伴随、旧九对照和初末状态的section均已经存在于reader所读的完整status；这说明元数据来源结构已形成，但仅凭section存在不能声称代理逐值核过其中矩阵。

## 4. 本次真正改变的是绑定比较，不是科学算法

r2 producer的唯一正文改动是：

    if k.encoded(old_model.binding) != k.encoded(
            parameters_recipe['expected_original_literal_binding']):
        raise ValueError('The actual reconstructed original literal coefficient identity differs')

它修复实时Decimal与JSON字符串直接比较的类型误拒。实际producer：

- 35491B / 1998fa8062ca91d798fe13ef60e2dc4ee08e5709c871d88346e81692852cad2b；
- reader：28130B / 54d38cc81927e0aae686613ab8384b1591402c71fd3488f4b66e4844e1f1562e；
- wrapper：19031B / d9b969a948e7afb661d4f1d9aa81371000692f234de5da7beef91670b4a8d289；
- request：41858B / 089b73a13e86293b02410f06b9815bc283e842f2d794aeeda4ea7f033645920d；
- workflow：20759B / cd4150ef19744324c08442fe5d5fbd619718207059b9dc0b394df245f9e4cfe1。

完整变更见[工程修复接口](../notes/2026-11-15-request164-canonical-binding-retry-interface.md)。family09240b33、ten model8cb8352b、adjoint12a95d40、全部原数学预算和门均保持。原参数recipe仍是7483B/76a93aa076d0a55781fdb3228a895b25583591b269fa5a866ea8068392946820。

实际source-input事件确认112个source pins、10个support pins、原41→当前45闭包。输入仍来自actual157/run43729310294/sourcec71cbeac7fd13c65cf50c7eb39842e9949737b25的真实九个Decimal字符串；原status931b013b...是数值来源身份，未当作当前缓存。父半径0.0000390625仅作来源说明，新形状系数初值0、尺度0.01，均是原独立实验合同，没有在r2中改变。

本次没有accepted新点，故后继不能从“164末新形状场”续接。保留原初始十状态意味着新系数仍从零初值保留的程序语义，并不提供一个已接受非零完整场。

## 5. 为什么原读回超限

原reader已经在长度检查之前打印完整section_UTF8_byte_counts，因此本次有具体运输原因，不必猜测：

| 原section | 字节 |
|---|---:|
| all_original_real_trials | 45395 |
| complete_six_candidate_catalogue | 18964 |
| initial | 8765 |
| final | 8765 |
| initial_binary64_projection | 5016 |
| final_binary64_projection | 5016 |
| zero_extension_binary64_readback | 8659 |
| zero_extension_literal_readback | 7630 |
| original_nine_adjoint_comparison | 4613 |
| adjoint_build | 3888 |
| adjoint_final_report | 3879 |
| original_complete_circle_check_at_binary64_projection | 3222 |
| new_ten_literal_binding | 2971 |
| fresh_original_nine | 2546 |
| original_nine_literal_binding | 2257 |
| final_projection_contract | 1547 |
| complete_planned_real_trial_rows | 1381 |
| selected_shape | 1204 |
| complete_scalar_domain_at_binary64_projection | 1066 |

这些是实际输出JSON各section的字节数，不是科学评价结果。全summary另包含其余小字段和JSON结构，实际总数为148101B。不能把长度53的merit字段解读为某个具体数值，也不能从长度4或5猜一个未展开的布尔门。

读回修订的合理方向是单份约40–60KB的真正科学结论：全20档只保必要原标量、原三残差、接受/域/Armijo理由和新系数；原九固定参数只出现一次。六候选保完整实际三响应、分数和必要来源，重复定义/大终端动作只保身份。初末FD保原max、有效标志、全120列覆盖及真实错误；zero-extension大对象只保原比较标志和完整身份。完整大表不能分块或编码搬进工具，也不应为了让root逐项读大表而新增科学门。

这只是后继读回设计，不是已经重新取得本次原值。若要重新执行同一科学source，必须标为新的实际运行，并根据其真正输出写新结论；不能将新结果重新命名为本次已清理的raw。

## 6. 规则同步、清理与接续

本次规则runner保原2700秒机制。原actual_rules_sync_completed记录round0、2026-11-15 17:39:31 UTC，读取origin main e9e0d67a3f018d5054b37272f69a5a92c169f9ed，发布规则记录1e7ec387346f44ee6cff6da24d2e3e2a280727e3。科学源继续绑定触发checkout bab76df...，不随该元数据同步换源。

审核的根README blob仍为21bd547f56590b7f2dd279d0297efb289a9b2783，题README为bff8aea253a9e6a7a4fac28d810ac454c5499fec。原错误通道与小fallback先输出，随后owned cleanup成功移除本次science、四原输入和原78源码临时树。没有新raw artifact、Release或Git数据保存。

下一数学方向不能用这份未传出的候选表作精度或秩结论。173/R363的原站点奇形状目录与174/R370的固定奇形状箱组合，可以从已公开actual157原九输入独立重构，保全部逻辑输入、完整七状态/112终端与真实原门；它们不需要把本次164失败视为前置门，也不能声称已经受本次未读矩阵证明。

本报告到此收束本次实际范围：科学流程完整返回、二十档全部拒绝、没有接受点；逐档数值和完整最终门未传出，不能补造。
