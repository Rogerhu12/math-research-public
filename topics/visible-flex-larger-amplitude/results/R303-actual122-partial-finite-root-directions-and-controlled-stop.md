# R303：actual122 两种有限 root 方向的资源部分结果

作者：OpenAI ChatGPT /root；日期：2026-11-15。类型：原公开 Actions 完整可得输出的有限事实、范围证明及重做责任。全部科学计算在本公开库 Actions；本文只读取原日志、选择字段、核对原 JSON 字节和 SHA，不在分析环境重算方程、方向、范数或耗时比例。

## 1. 结论及实际执行

[公开 run43696328387](https://github.com/Rogerhu12/math-research-public/actions/runs/43696328387)，source commit 为 05b1dc3b09f586b2f12f13ad45a82dc07b97778b。compute job132757561652 的独立科学入口以 exit3 结束，report job132790503311 成功。原摘要的 procedure_complete=true，但 science_directions_complete=false；这两个字段分别表示实验各槽已有真实结局和两份科学方向完整，不能混同。

第一次实际 native 调用、iteration0，重新形成一份完整64位原模型和 R273 方向；随后在同一新 packet、同一 delta、alpha=0 上分别运行 original 与 refined 两个 binary128 有限 root 轨迹方向。两份都因为本次科学预算结束返回 resource-budget-partial：

| 原记录 | original | refined |
|---|---:|---:|
| 分配科学秒数 | 3600 | 3294 |
| C++ 原 elapsed_seconds | 3600.005860872 | 3294.006301637 |
| 协调器该 policy elapsed_wall_seconds | 3605.364 | 3298.62 |
| 完成 stage 数 | 488 | 187 |
| 完成 row 数 | 109536 | 42112 |
| 全部 stage / complete | false / false | false / false |
| experiment_budget_exhausted | true | true |
| primal 全范数 | null | null |
| 方向全范数 | null | null |
| 单位步 affine 全范数 | null | null |
| 子进程退出码 | 3 | 3 |
| 外层 guard.wall_timeout | false | false |
| guard.signalled_owned_process_ids | 空列表 | 空列表 |
| actual_error / scalar_readback_error | null / null | null / null |

原问题共576段、577节点，224个shape分量，完整 RK 状态226维，全部原行129248。cut112行、stage129024行、far112行全部仍在责任范围。未完成行不能补零；已分配全尺寸数组也不能当成全行已经计算。完整逐stage表只写过临时完整report，bounded stdout明确省略了它，清理后本文未重新取得。因此488和187只是计数，本文不声称它们是连续前缀，不凭计数推测未访stage索引。

所有请求槽均 attempted=true、各有实际结局。第二 policy 未被第一 policy 的 partial 取消。两份输入相同，但各自实际执行各自有限 root 停止策略；它们不是同一分支的一份原值加另一份伪造变分。

## 2. 新鲜64位模型及唯一方向

[原122执行接口](../notes/2026-11-15-request122-fresh-direction-finite-trace-interface.md)完整保留真实父恢复与33个源pin。输入是 actual91 包内 actual73 失败 BASE，状态 SHA 为 f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6；不是一个已接受的 native 锚。实际78个公开原源及两个 historical ready 由原恢复器提供，未加载已删113 packet、旧J或旧方向，也未使用 small-core 四数学输入。

本次 fresh snapshot 原件1311字节，SHA256为3ca4747306b5ec7a255ae595a62b818c728fc28d929f245905b0edd15f7d4610。新完整 delta SHA为4b4b1aaacd96910635a03f97d45957ae995c724997a0e18b66ac1d06408e294a；packet10348368字节/afb10fa8fdc4efe6d9615cf414ab990e5095dda4379cff13f50076a17238ce0d，binding3548字节/996aed6be6bc3c591e617a0b7815a6486e3c4009dc0078ebd79c38c12f7ad971。

原64位当前范数为6.0618737006888706e−5。eta CLI文字为1，完整 R273 factor 报告如下：

| 已存 factor 字段 | 原值 |
|---|---:|
| 原 rows / columns | 129248 / 129248 |
| augmented rows | 258496 |
| block width / nodes / stages | 224 / 577 / 576 |
| node penalty blocks | 577 |
| pure constant rows | 129248 |
| QR calls / formation calls | 1153 / 1152 |
| factor加constant字节数 | 464891392 |
| 声明最大factor字节数 | 2147483648 |
| 原 factor elapsed_seconds | 29.261270102000026 |
| minimum_absolute_triangular_diagonal | 1.1915065260525806 |
| formation_underflow_to_binary64_zero | 0 |
| maximum_RSS_kib | 830312 |

这份 factor 使用的 dtype 名称虽为 float128、itemsize16，但其 working_precision.significand_bits=64，是该运行的 NumPy longdouble 精度，不是随后 C++ binary128 的113位有效尾数，亦不声明 QR 为准确有理算法。

原 exact-row kernel 对保存的有限64位矩阵全行执行了准确字词读回。保存的 base 最大缩放残差位于 global2539、node10、Pi mode76，其准确有理数为49660559360/819227879234049，原十进制显示为：

$$
6.061873700688870870601158412977629481529154353251182450024889837\,10^{-5}.
$$

保存的单位方向 affine 最大缩放残差位于 global2128、node9、Q mode1，原十进制显示为：

$$
9.685623139820915231897967296720853552003562611702521449132211420\,10^{-11}.
$$

显示数不用于比较；准确 numerator/denominator 由原摘要保留。这个有限字词矩阵事实不证明它是任何128位 primal 的准确导数，更不能替代两份尚未完成的128位方向全范数。原 factor result SHA 为85e3ad76cdede7dc0c60923fcb0c225c7ce0e98a541d012346f85733c393b6bf。

## 3. 两个实际 root policy

两项均使用 compiler15.2.0、__float128 的113位有效尾数，2线程，alpha十六进制0x0p+0。实际编译采用 O3、gnu++17、OpenMP、fno-fast-math、ffp-contract=off、frounding-math 和 libquadmath；两次compile exit0，编译日志均为空，其SHA为e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855。编译成功只证明该次工具链产生了实际执行文件，不付科学完整性。

| root停止字段 | original | refined |
|---|---|---|
| root_stop_decimal | 7.99999999999999999055447483647918958e−14 | 1.00000000000000000000000000000000003e−28 |
| root_fallback_decimal | 4.99999999999999969748484640969905465e−12 | 4.99999999999999999999999999999999999e−27 |
| max_returned_relative_decimal | 7.97942273584970872285222203689169507e−14 | 2.1639059485498609525469400686088579e−36 |
| min_A_over_returned_RHS_roots | 0.999999999975949816097646413730855503 | 同左 |
| min_D_over_returned_RHS_roots | 0.999999999999985782663062750449147792 | 0.999999999999985782663062754317216981 |
| min_S_over_returned_RHS_roots | 0.999999999999999999999999999688946329 | 同左 |

上表极值只覆盖实际返回的 RHS roots；不是未访stage的域证明。两份的几何与表格仍把原 binary64 字词视作固定实常数。cut target、far graph、几何变化固定为零；只有原 stage 的 Pi 残差与JVP除以原port，两个mean行保全且不作该缩放。未改原 native 停止门，未构造新的 fullDN 求解器。

| 原 root / variation 计数 | original | refined |
|---|---:|---:|
| root calls | 23569 | 9076 |
| angular_evaluations | 25377 | 27228 |
| Newton_steps / line_search_trials | 904 / 904 | 9076 / 9076 |
| fallback_returns | 0 | 0 |
| maximum_iterations | 1 | 1 |
| original_threshold_reached_count | 23569 | 9076 |
| C_direction_calls | 904 | 9076 |
| F_direction_calls | 24473 | 18152 |
| factor / forward / backward direction calls，各 | 904 | 9076 |
| accepted_updates_differentiated | 904 | 9076 |
| joint_root_returns | 23567 | 9075 |
| primal_returns_selected | 23569 | 9076 |
| 成功返回中0次update | 22663 | 0 |
| 成功返回中1次update | 904 | 9075 |
| shadow_words_checked | 523568517 | 493780067 |
| shadow_word_mismatches | 0 | 0 |
| successful_root_direction_records | 23567 | 9075 |
| failed_root_direction_records | 2 | 1 |
| temporary_output_file_count | 497 | 196 |

所有被微分的已接受root更新都在 backtrack0，backtrack1至19计数全部0；成功返回中update2至29计数全部0。所有计数按原字段抄录，不把先选择 primal 后尚未完成 joint 返回的记录改成成功。

原完整失败方向文件已随临时raw清理，本文没有取得2条和1条失败记录的全文。上层 actual_error=null、最终 outcome=resource-budget-partial，不能据此断言每条局部失败都是预算中断，也不能声称所有未读内部数学错误已被排除。外层guard没有发送信号或墙钟超时，只表明入口收到子程序自己的预算partial退出；与局部失败文本责任分开。

## 4. 有限轨迹变分与本次可推出的命题

### 命题1：部分行不决定全域范数

设完整原残差行集为 $I$，实际已计算行集为 $S\subset I$。对完整向量 $r$、方向 $d$ 及各原权重，只在 $S$ 上的读回不能确定 $\max_{i\in I}|r_i|$、$\max_{i\in I}|d_i|$ 或 $\max_{i\in I}|r_i+d_i|$。本次原程序因此把三种全范数保为null，不能用它们比较两个policy的完整外层效果。

证明：若某行 $j\in I\setminus S$ 未知，则固定所有已知行后，可把该未知行的绝对值任意增大，而不改变任何已知记录；其完整最大值随之变化。即使已知行存在小值或某个局部下降，也不决定未知行的大小。对三个向量逐一应用同一论证即可。数组已按 $|I|$ 分配只给存储容量，不给未知数值。证毕。

这是信息范围命题，不声称实际未知行真的很大或实际科学结果必然失败。两项实际 stages_completed 均小于576，且原all_stage_rows_computed=false，故本次符合该命题的适用范围。

### 命题2：本次一个方向不付224列J

固定[ R283 ](R283-finite-root-trace-differentiation-with-literal-tables.md)的实际有限分支，把每一步 $F$、独立给定的 $C$、Cholesky及两次三角代回、已接受更新与完整226态RK看作实表达图。若各被使用的实运算在该点可微，逐步链式法则给出该固定图沿给定delta的变分。本次确实执行了这些原运算的方向形式，且没有以 $C=F_e$ 替代独立矩阵。

证明：从输入实方向开始，对每一图结点应用该实际运算的微分；图按执行顺序有限且无回边，归纳可知每个结点所得方向是该结点复合实表达的方向导数。Cholesky及代回必须微分其实际表达，不能把有限近似解换成准确隐式解；root分支一经固定，该结论只覆盖图内已选运算。完整状态传播同理，随后对原port及边界固定线性表达应用链式法则。证毕。

本次binary128数字是对这些实变分的数值计算，不是附带舍入误差界的严格实导数包围。固定分支结论不证明附近分支稳定，不是IEEE舍入映射的导数，也不包含被拒root试探的选择逻辑导数。shadow mismatch0只说明已检查的原值字词一致；它不补全导数误差界、分支稳定、未访行或全224列。

即便单一方向全完成，在线性代数上它也只给 $J\delta$。因本问题输入维数大于1，可取非零向量 $v$ 与 $\delta$ 正交，再取非零 $u$ 并令 $A=uv^T$；于是 $A\delta=0$ 而 $A\ne0$。因此 $J$ 与 $J+A$ 的该方向值相同。因此单一方向不足以重建全J。本次更只是该方向的部分行，full_224_column_stage_J_supplied=false、complete224_trace_J_computed=false均应保留。

### 命题3：受控停止不是原十trial失败

原入口在第一次fresh方向与两policy槽处理完后发送明确sentinel；原十档 nonlinear trial 尚未运行。这次原worker响应中的failed文字，只能证明原调用被该实验控制策略结束，不能证明原十档均拒绝、原 native 无解或任一全域接受门失败。

证明：执行顺序是fresh原模型/方向、两独立policy槽、实验sentinel、协议退出；原十档循环位于该sentinel之后。该轮既未执行十档循环，也没有其试探输出，故将sentinel退出解释成十档判定会把未执行谓词当作已执行。程序完成与科学接受分别由独立字段表达，并无从前者到后者的逻辑蕴涵。证毕。

## 5. 真实停止、计时及规则同步

sentinel原文为 REQUEST122_CONTROLLED_STOP_AFTER_FIRST_FRESH_DIRECTION_AND_TRACE_POLICIES。实际original_driver_exit_code=2、worker exit0；原协议 response.failed 是带 Error: 前缀的该sentinel，converged=null、residual=null。原result将该响应包装为 FloatingPointError，bridge_failure=null。新入口entry_error=null，log_forwarding_errors及worker_error_records均空。

新实验准确识别了该受控响应：controlled_worker_stop_observed=true，controlled_protocol_failure_response_observed=true，original_ten_trials_or_final_J_audit_executed=false。原trial calls为0；native_accepted=false、fullDN_completed=false，完整endpoint J及fresh物理audit均未提供。不把原driver的包装失败、入口exit3、report作业success或 procedure_complete 任一个字段冒作科学接受。

实际fresh方向事件于09:09:17.0380304 UTC出现，original策略于09:09:17.898329开始，refined于10:09:23.269296开始。两policy完成事件11:04:21.4501228，受控停止11:04:21.4558688，入口最终摘要11:04:22.5529118。原协调器累计elapsed_wall_seconds=6904.007，入口总elapsed_wall_seconds=8008.370981772；实验7200秒阶段是在前置fresh64/J/R273与packet之后开始。不能把7200写成整个request总墙钟预算。后继若增加完整末态组件，单一全局deadline必须从fresh前置开始计，并明确保留独立audit及清理读回时间，不能在桥开始处偷偷重新计时。

原规则runner留下以下实际pull及普通push：

| UTC实际读取时刻 | 已读origin main | 随后同步记录commit |
|---|---|---|
| 08:50:53 | 6d069f71ae01c2577a7d3c191892a423530f6c83 | 54fe9b190d5d9b146d7c8481b6169016c30f1fab |
| 09:35:57 | 0f056c8f43b30bdf8bd845f54f93dce077c146dd | aec89f5eb1968702b9f745c2c17fd628ff04301c |
| 10:21:00 | 104898809daa1572a0b23a6e5e3496cac10414f1 | 6efd0ccf008d00be8703654f57d706143cda05bd |

双README均未变。这些是Actions内真实git pull，不是root分析环境的API读取。

## 6. 原字节身份、读回范围和重做

原摘要的单行JSON27431字节，不含其终止LF，SHA256为98080d47a5d970fd2707fcb2b33f255306e03355055323367002e85ce6afb323。root从 BEGIN_VISIBLE122_SCALAR_SUMMARY / END 标记读取全部正文，核原字节/SHA，并与compute的native122_final.summary交叉对应。下面两份完整job日志直接读取，未重新序列化再冒原字节：

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| compute日志 | 173901 | bbe5245c53f8b20c39342e9046d5bb03a93480784fd71b2701eaa9aba1359700 |
| report日志 | 59587 | 30f69a32c6a48c5e049c057ed0bcf84eb1c79055e62d84b95189902e5f3935f8 |
| 原response gzip | 1332047 | 4ec97ef6fd260bb963b0b9c8423228816831f9cbe9bb88ce813df83740052495 |
| 原result | 12576 | 3cd8b252863d0d8c772c18d4cefdb89b2e792f5ac6a877c15357a08efac8fda7 |

原结果、响应、完整科学报告及数组已在job临时目录清理；本文读回的是原公开日志及其中完整紧凑摘要，不声称已下载并独立重新计算这些被删raw。以下为原报告给出的字节身份，作为再生核对责任，绝非新raw附件。

| 原临时件 | original：bytes / SHA256 | refined：bytes / SHA256 |
|---|---|---|
| 完整 launcher summary（非本文 compact） | 93801 / 10718fd3504608f08bc6a961435953e2b80105520e886a669d05ea67f66f5a23 | 102211 / 5febac50f6a67b21801bf5d39fe00af0ddccb8c160242ee584ba2daeec63e002 |
| 完整 scientific report | 602990 / c569d055bfdd518bddb9899c73a672867675a6dab0fa4101f166ee8535d0d9b1 | 568604 / ba212e9b31a7f11294e5ad0705d1a5566030cacbb9a7818aa69f91096211d18c |
| 临时输出 manifest | 103948 / fcb526702509278198f82825f736b4ce9acab8562057b7028535de879b6d413c | 41039 / c55f25a416a588a6dc76f0451bcc397f9d58a883e45d2df6bfc12150f95a6812 |

| 完整分配数组 | original：bytes / SHA256 | refined：bytes / SHA256 |
|---|---|---|
| current-states.f128 | 2067968 / 35a1f91163fd0dfc28ca911ddfd1d29f43e02e0cc0974d5db4e1145b9471f5a6 | 2067968 / 35a1f91163fd0dfc28ca911ddfd1d29f43e02e0cc0974d5db4e1145b9471f5a6 |
| directional-residual.f128 | 2067968 / 72a4259ae7bc7e336ff2b72429490edbeb005102f29fd63d653e3f272e64681c | 2067968 / 8e8673a390a8606f84cfd818c4edea8e18e9a2e66b960bd3a497c0f48760b2a5 |
| input-direction.f128 | 2067968 / 09ff759cc309d9a335a58fb7513db1fe8479b7ee85f965b4b8ad6e1e626eb954 | 2067968 / 09ff759cc309d9a335a58fb7513db1fe8479b7ee85f965b4b8ad6e1e626eb954 |
| primal-residual.f128 | 2067968 / 2adb876b39a78fbc02a0cfab6e471315acf60e28a520b6938a9ba314f26b077c | 2067968 / 3ce61d53ef2d8e59893012e5c9cd2b1e5d3cb536c954911e3e73cce5833092a8 |
| stage-full-direction.f128 | 2082816 / e5d2af57a75c38f8064c9ef92ae52c657442106437ec945c1b6199ad7eea9c45 | 2082816 / d0a73e76b36cc132b3d4f00a4eeb7876128345f5a6e55ba9d34ec776daa70428 |
| stage-full-output.f128 | 2082816 / 502e3a2c93c5ad95488955a7471cbc26d0b4d25c2b0e32ea7347acc1131e37f0 | 2082816 / 2a9f00d399b5b42f24bbbcef2cee00c756976c8b2f7eedd005320fc8cb9ed1a0 |

current-states与input-direction是577×224；residual数组形状129248×1；stage两个完整数组形状576×226，全部声明IEEE754-binary128-little-endian、C order。完整分配大小没有改变本次partial标志或未知行责任。

执行源及临时生成源可由同一公开commit、原输入和以下身份重建：

| 源责任 | SHA256 |
|---|---|
| geometry_20261115_native_trace122_probe.py | 05ad668da4bec72cedb0fa2f14d4c59a7ab99a280c47b137c94a5fafcf99105f |
| geometry_20261115_native_trace122_experiment.mjs | 480ec31206c32c59dddb57b766a3a9cbe37ef8d3e23b5ca8f44db5e7b7f2a752 |
| geometry_20261115_native_trace_variation128.cpp | 8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d |
| 原113 primal C++ | 1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d |
| 实际临时driver | 00be84ac166e6b87074c10fe9b8a636d02fae25f6e18168db04c0f9a86b9f70c |
| 实际临时QR adapter | c8909b3c6208afc215db9a660748440a8cbcf6b446b6de6813a23dd7d9de2759 |
| 实际临时system | 8573d036821126aadf578e299c3902607e379138b231416c118ad81203a5d16b |
| 实际临时hook | 7b52172fabf511e79bd4b571c958f1b7a7d34001f57ebdc53079580242568e2c |
| 未改R273 factor engine | 9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33 |
| 未改exact kernel | 0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f |

完整CLI责任沿原接口：trace-budget-seconds7200、trace-threads2、eta1、node-heap6144、exact-workers2、max-factor-bytes2147483648；original91-directory与source-topic分别指本次临时恢复的原包与78源，out是本次拥有的临时目录。原launcher分别取seconds3600和3294。编译器、原source pin、historical ready及包身份也须相同；不能以一个已删除文件的SHA恢复其内容。

原清理包含当前request输出、actual91与原78源；对其21个只读归档目录先恢复当前拥有目录的可清理权限，日志未报告清理错误，没有上传新artifact、Release或Git raw。本文只保存源/参数/run/SHA/紧凑事实。若以后需要被省略的逐stage或局部失败全文，须独立、明确预算地重做；不能从本次计数编造。

## 7. 对下一实际求解的约束

本次证据支持保留完整持久128状态及与所选有限root策略一致的导数责任，并表明全224列成本不能由“一条方向能运行”推定可忽略。后继共享真实root trace能减少重复原值工作，但本次没有给出任何共享实现的实际加速倍数或全J完工保证。

完整112边界响应、338端点、原全行缺陷与独立物理audit仍必须分别执行；C-based原物理jet不能自动冒作有限root图的真实导数。新入口须只在真实同job末态尚存时接线，完整保留预算partial、错误、未启动后缀和raw清理责任。已有133、独立末态组件及后继137按各自明确source继续，不盲目重复本次两个未完成policy，也不把任一部分结果计入课题闭合、reach、幅度或同g精度的完成。
