# R321 — 实际 140：完整128位下降与逐字回放已完成，后继全列和物理审计停在编译

日期：2026-11-15（UTC）

## 321.1 结论与实际公开运行

本轮重新从原91输入现场生成完整64位 withJ 和 R273 方向，再进入持久 binary128 owner。owner 用当前128残差形成自己的完整阻尼修正，只实际试了一档 α=1，并严格接受。全部129248行的末范数为 9.68582474751023176032080482454992093e-11，已低于原2e-9阈值；随后独立进程重做完整576段、全部226态和 cut/stage/far 残差，原报告确认输出与残差逐word相同。

这没有完成原 native/fullDN。新增 stage 全224列组件与独立物理 audit 组件均在 g++ 编译返回1，未运行其科学命令；boundary112 和 endpoint338×112 因缺少对应完整前置而未启动。原报告所有这些责任仍为 false。两个作业 SUCCESS 表示本轮受控执行和有限报告传输完成，不能改写为原完整接受。

实际身份：

| 项目 | 原值 |
|---|---|
| run | 43713195661 |
| source commit | 242c1f0251c57f56f19e67b88b2e4dc4d5cac614 |
| compute job | 132809057379，SUCCESS |
| report job | 132824948760，SUCCESS |
| 原规则同步 | 原3b8规则监控，2700秒周期；已读根21bd547f…、课题bff8aea… |
| 独立完整summary | 38230 B，SHA256 7a66911e9eb93ddaa9f5a6f77b811f47766ed81fce3ca416fd447dd6cea39334 |
| compute解码日志文本 | 240426 B，SHA256 6feccfa56486efcb007cd209525b51542bfbce1ee4249ed9935798c8c31e23dc |
| report解码日志文本 | 81188 B，SHA256 5f5318a6320e94323e1587137a5a61cc4f5316dcf8477252c81bf2cc7757e6cd |

日志文本身份包含GitHub返回的起始BOM和LF；summary身份不含帧分隔LF。已从compute的 persistent128_final 事件提取完整内嵌summary，并与独立report的 BEGIN_VISIBLE140_SCALAR_SUMMARY 帧作逐字比较，两者相同。这里没有本地重算范数、矩阵、方向、误差或任何科学量。

来源：[公开运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43713195661)；[原140请求](../computations/public-native-operator-final128-request.json)；R308实际133及R305证明（均见[课题结果索引](../results.md)）。R308/R305的具体科学对象以各原文为准，本轮所有新数字来自上述实际140日志。

## 321.2 全部输入与当前模型的责任

原91现场 state 的 binary64 SHA 为 f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6。原输入恢复、两ready和78源均按原请求完成；本轮没有取已删除113/133/137的packet、J、delta或128状态作为输入。

本轮fresh snapshot结果SHA为 c2ffc87c1aa4362ceb7bf8aae3e9f28f5ba26d8a312f69101a72942150dce485。完整576×224×224当前64位J的raw SHA为 1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4；scales为 ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc。它在128迭代中只作为固定近似chord矩阵，原报告 fixed64_chord_not_current128_DF=true，绝不称当前128有限root映射的一致Jacobian。

| 本轮原输入/对象 | SHA256 |
|---|---|
| original-scales | ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc |
| physical-height | c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f |
| cut-target | e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d |
| original-far-graph | 395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54 |
| full packet，10348368 B | 1c9df6b2aa203d526eee11fe443ebcb474584c677b76ed3901b6a0f6c1f37aa8 |
| packet binding，3669 B | b61b5ac62b5e9745f8627337aabf8880debf841a04727be08d5a0a4854ad7911 |
| fresh64 R273 delta | 4bb396b069f5c32a3d77a08531ad2cdefbd3ece7fd8f63c56baed84f13976ce6 |
| current128 chord模型身份 | de08810d97ffdfb671201d97a176c18b88df815e8d50fdfa3fbf7fd567dc997e |

packet保6943个原子RK步、20829次原binary64 geometry取值、2048角点及全部112模态、224形状量、226完整态。geometry/table只把原literal binary64 words准确提升到binary128，不重校准标量profile。packet writer声明不调用root/RHS/J；此项是已冻结源码责任，不能冒成连续几何或误差证书。

fresh64原范数为 0.000060618737006888706；其全129248行精确仿射读回最大为 9.685623139820915231844260456306540893890861679791289092058094119E-11，位于 stage9/Q1/global2128。这是fresh64模型的原精确账，不是下一节使用当前128残差的方向读数。

## 321.3 持久128 owner：当前残差、R273与唯一原试探

原容差值保其binary64输入的准确提升：
2.00000000000000012456318291555971284e-09。
root stop为7.99999999999999999055447483647918958e-14，
fallback为4.99999999999999969748484640969905465e-12。没有改成refined root policy。

完整初次128评价：

- 576段全部返回，129248行全部保存并读范数。
- norm = 0.000122096054597410989492629881621789239，binary128 = 0x1.000dd1f7889da0c80213a1f62c65p-13。
- 最坏为 stage11/Pi104/global2791；输入node12、输出node11。原有符号残差 −6.32022287232257274964381733314263019e-19，sigma = 5.17643497421954467891015949609799199e-15。
- 27772次root，904次Newton更新、904次内部line-search trial，fallback0，maximum_iterations1；27772次均达到原stop。
- mean_height_sum = 0.0226842463487103007695708959242220956。

当前残差仅为近似QR转换一次binary64：128969项改变、非零转零0，最大原sigma归一转换差为 4.10665514535721833358792197700840237e-21，位置row2568。持久owner保留原128残差与状态，不用这个转换替代非线性评价。

当前R273方向包含577节点罚项、576段、cut112、stage129024、far112，共129248列/129248原行/258496增广行；QR1153次，formation576次，全部factor与constants为464891392 B，complete=true。新formed model SHA为 a5dc9fd64ed0f9725ec11df2b7fba3574c1fae79c139a97562ecaf365813077c。

原longdouble模型读数如下，仅为该有限形成模型的数值读回，非外向证书：

| 原字段 | 原字面值 |
|---|---|
| formed_residual_infinity_norm | 9.685824747510231713e-11 |
| formed_residual_two_norm | 1.130568575521336125e-10 |
| factor_triangular_residual_infinity | 1.0667321179483844895e-20 |
| full_unpreconditioned_model_gradient_two_norm | 1261309.1059448874298 |
| formed_energy_minus_factor_energy | 3.4966828013055790077e-33 |

全部577×224方向在128中由原sigma乘实际求出的z64形成。129182项与原R273的delta64恢复不同；最大scaled recovery差为6.21420740974797949698112574685574514e-28；非零128来自零64恢复项0。这里也没有cut/far投影或额外接受门。

唯一非线性试探是iteration0/trial0/α=1，原reason为 strict-original-norm-decrease，accepted=true，完整评价耗时825.425365817秒。126690个128状态word发生变化，其中11183个变更后仍具有相同64位cast值。这个原计数说明本轮保留了64位cast不表示的状态变化；它不单独证明此前所有拒绝的唯一原因。

末完整范数为9.68582474751023176032080482454992093e-11，
binary128 = 0x1.a9fcb11a67aa9fdf970095730bcp-34。
最坏变为stage9/Q1/global2128，输入node10、输出node9，原残差4.99890220172700756918252291853272271e-25，sigma=5.16104960810073433235339041548094359e-15。原below_original_tolerance=true。

原32方向×10试步上限没有缩减；因为实际已达shooting阈值，direction1…31、direction0的trial1…9均未访问。stop_reason明确为 shooting-tolerance-reached，非预算停止。accepted_steps=1、directions_computed=1、trial_evaluations=1。

## 321.4 独立fresh回放与状态身份

独立新进程直接读取同一final-state.f128，不经64位回写。全部576段、全部129248残差和两个完整mean累积器再次计算。原报告：

- independent_fresh_replay_complete=true；
- fresh_replay_full_residual_words_equal_owner=true；
- fresh_replay_all226_output_words_equal_owner=true；
- norm、worst row、mean_height_sum与末owner逐字相同；
- 27772 root、904 Newton、fallback0、maximum_iterations1，failed_stages=[]。

| 当前末态/回放对象 | bytes | SHA256 |
|---|---:|---|
| final-state.f128 | 2067968 | e0f20c36d59ac200796a03441e7b5604224e3add414361a11cc6ff3586dffba2 |
| final-residual.f128 | 2067968 | 18cfb3face9b286513f624003984d318bc6b6c735ed803a3cbffde15dc6be39b |
| independent-residual.f128 | 2067968 | 18cfb3face9b286513f624003984d318bc6b6c735ed803a3cbffde15dc6be39b |
| final-stage-full-output.f128 | 2082816 | 13195bbb4249c47b158399c36d173de0fc8bfc80e3b9f5ad98ed1411ff715f9e |
| independent-stage-full-output.f128 | 2082816 | 13195bbb4249c47b158399c36d173de0fc8bfc80e3b9f5ad98ed1411ff715f9e |

这些是Actions原文件的实际SHA/比较结论。本地没有这些raw的独立重审，也没有从hash伪恢复它们。按规则15，原raw在同job消费者结束后清理；后继须按同源同序fresh重做，不能声称已保留可续的128现场。

## 321.5 新后继四组件实际停在哪里

清理前hook确实执行，取得实际末state与precleanup-owner-summary。owner handoff为110602 B/SHA93db244d32cac5e3c6003425363db22aa6e0b35c26bcd712956241a1f7e28f94；输入当前state就是上表e0f20c…，没有旧64J或旧audit改标签。

| 组件 | 实际动作 | 原错误/范围 |
|---|---|---|
| stage576×224 | g++启动并return1，0.7160745859996496秒 | ValueError('Actual new stage compilation returned')；scientific_command=null |
| boundary112 | 未启动 | complete-current-mathematical-input-not-produced；缺stages |
| endpoint338×112 | 未启动 | complete-current-mathematical-input-not-produced；缺boundary |
| 独立audit | g++启动并return1，0.7158958459999667秒 | ValueError('Actual component compilation failed')；scientific_command=null |

因此没有任何本轮224列全stage报告、112边界解、338×112输出或7488query物理审计值可供引用。physical packet已生成（6943 audit原子步、7488查询），仅证明输入写出，不代表audit运行。

两个component过程返回2；它们的原wall_timeout=false、resource_partial=false。hook总耗时2.2043876380002985秒，前后remaining_scientific_seconds为15462/15460。整个入口elapsed_seconds=3620.662850021，原global wall预算19200秒未耗尽。原受控停止消息为 PERSISTENT128_CONTROLLED_ORIGINAL64_STOP_AFTER_INDEPENDENT_OWNER，原64 trial calls=0，original_driver_exit_code=2；该消息是独立实验结束后的预定协议停止，不是原64数学校正拒绝。

源码和原日志证据的边界必须保留：日志直接给出了g++ return1、上表Python异常及临时日志manifest；compiler.stderr正文没有被原140外层转发，清理后不能由hash取回。下面是对固定源码的静态确定发现，不是日志直接打印的编译诊断：

原113定义全局 JSON helper quoted(const std::string&)，同时包括 <iomanip>。在R305 header的quoted(failure)、stage源的quoted(norm_error)/quoted(errors[n])、physical-final源的quoted(error)中，实参为非const std::string。未限定调用触发std命名空间的ADL；std::quoted(string&)比全局const引用重载更匹配，返回流操纵器对象，不能与三目表达式的字符串字面量形成所写类型。显式::quoted限定原JSON helper可去掉这个确定的C++名称解析阻断，不改变任何数值式、root/RK、矩阵或门。

后继152已明确保原完整stage/all224/boundary/338/audit范围；应在独立launcher中按每个固定原源SHA生成仅限定JSON helper的临时副本，列原→执行字节身份，并在任何编译结果之后保全文stderr。不能用150的单field证书替代152全部责任，也不能凭未执行的代码预定修复后科学结果。

## 321.6 仍未付的数学和物理责任

原report的native_accepted、fullDN_completed、full_stage_J_complete、endpoint338_by112_sensitivity_complete、original_geometric_final_audit_complete均为false。新增precleanup四个complete标志也全部false。

本轮已付的是持久128原stop有限映射上的完整shooting下降与独立逐wordfresh回放。没有证明C=F_e、没有给有限word算子误差界、没有对IEEE离散roundmap求导、没有证明所有root分支在邻域稳定；没有完成原TailClient协议的当前128末态112边界响应、最终338混合灵敏度/原物理审计，也没有原fullDN真实接受。

R314/R325严格后验consumer独立作用于其实际完整输入和明确固定trace；request150首个范围仅选一个完整field的230列。它既不是本轮接受门，也不覆盖全部576段/完整边界/物理审计。R321没有把其尚未运行的结果计入140。

## 321.7 可复现脚本与保存范围

原请求固定52源，执行入口 geometry_20261115_native_operator_final128_same_job.py 的SHA为 f0ca0d4300252a7db2cb95da4ea6991605b59cea2132fa2526faafb58e120141；桥为00f1a43b95295cb29bec930b06a6418e7b5245cfb06d122fd9c1314cfa68dfd1；owner CPP为7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd；R305组件launcher为a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef。

复现资源沿原请求：fresh91输入/两ready/78源、η=1、owner6000秒、threads4、fresh replay reserve1200秒、matched-trace none、global19200秒、readback/cleanup120秒；stage8000、boundary600、endpoint600、audit1800秒各为原cap，实际全部受同一global deadline限制。引用这些参数不承诺某次run一定完成全部组件。

本结论只保存脚本/请求/run/来源和输出SHA及上述紧凑字面数值。原数组、完整factor、root trace和可重算大输出不进入Git、Release或artifact；临时读回日志不作为可恢复的科学父场。后续必须以新的实际结果判断最终责任。
