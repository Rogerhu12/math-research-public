# R584：request244 把完整循环舍入观察接入原 full112 实际调用链

作者：OpenAI ChatGPT（AI），2026-11-16。

**可信度：已证明（限下述冻结源码、实际来源绑定及 R583 的循环内舍入模式条件）。** 本文给出完整、可执行的来源组合与条件有限程序结论，不是一次数值实验报告。request244 的实际 source、run、逐 H 结果、FD、fullDN、资源停止与必要传输必须由其真实公开 Actions 返回；实际结论预留 R585。没有从正在运行的248、已结束的225或任何旧摘要填入本次科学值。

## 584.1　明确基线与唯一数值程序变化

基线是已经发表的 R593/R594 request248，入口提交
`b38a46a6d0f34f250cff6d13c64ffafa65931ef8`。其原63完整 prefix 初猜、原78来源、原91仅作首尾初猜、全部112维和原有限问题都保留。248已明确将 owner cap 从6000秒改为12000秒；244沿用这项已声明政策，**不再修改任何资源整数**。特别是原19200秒总科学钟、350分钟作业、320分钟科学步骤、replay1200、stage8000、boundary600、endpoint600、audit1800与读回清理120全部保持。

本次只把原 R573/R572 root product 实际安装点换为已发表 R583。R583四件提交
`7c16a9e89d8ec9d2630825f2bedbfd4f44fbd352`；完整条件论证见
[R583](R583-complete-inner-loop-rounding-observation-and-original-product-words.md)。
新 header 不变更原乘积资格、完整整数乘法、RN128舍入或 fallback，只使四个完整原循环各在入口读取一次本线程舍入模式。十个实际调用者随后绑定新文件和新 schema，避免仅在请求里列一个不被执行的 helper。

本次不采用 request242 的实际98或三参数初猜，也不移植任何旧 run 的 state、H、J、native 接受或审计。旧63用于恢复的 prefix 与旧91尾初猜的用途并不相同；本次当前 prefix、H、全部尾响应与原完整门仍要重新形成。

## 584.2　继承结论与新增责任的界面

本文使用以下已经明确的责任划分：

- R493/R501/R508：同一当前 H 的逐 call 来源、完整状态与 response、进程所有权和必要读回。
- R515/R518、R522/R527：已明确的 physical radial cache、paired-digit 来源及完整组件调用。
- R529/R532/R534：owner128 的实际值和 fresh replay 保持权威，当前 state 一次投影所得64位线性模型只承担原允许的近似 Newton/J 责任；没有把 projected point 宣称为已接受的 native state。
- R535/R550/R561/R564/R572：有限固定词、接受的完整 RootEval、准确 dyadic average、完整 lifted product 与五条 synthesis product 路径。它们在本次是完整实际 source-only 祖先。
- R588/R589：具名来源与完整 RootStats 的同一必要对象表示及严格逆；只在整个同一 body 真实缩短时使用。
- [R593](R593-one-clock-native-owner-resource-window-and-existing-continuation.md)：现有跨 H 初猜选择与12000秒资源政策；本次没有再“新增”已经存在的 last/predictor。

新增责任恰为：保持这些原有限计算与原输入不变，把 R583 两份真实 include、一个直接 installer 和完整24项编译依赖接到当前 caller；同时让 source 与 science 两个原必要 scope 都能保留新增 binding 的全部原字段。没有新增科学接受条件、独立对拍、fixture 或额外审计。

## 584.3　有限循环等价的准确条件

设某个原完整循环的实际乘积输入序列为 $(x_i,c_i)$，入口观察的模式为 $m_0$。原 R564 在该乘积的布局分支支持、实际走到模式检查时读取当前线程模式 $m_i$；不支持布局时先走原 fallback。R583把这一资格谓词的来源改为 $m_0$。在 R583 已陈述的条件

$ m_i=m_0 $

对该完整循环所有实际乘积成立时，两者每次乘积走相同资格分支。该条件只作用于当前实际线程与当前一次循环，不是在多循环、多 H 或多个线程之间缓存模式。

每个乘积仍各自执行原 layout、finite、normal、53-bit factor、结果指数范围与 signed-zero 检查。若模式不是最近偶舍入或观察返回未知值，则仍在每个乘积地址执行原 Q 乘法 fallback；并未要求 FE_TONEAREST 作为新的运行接受门。原结果为准确零、正常数、发生进位或必须 fallback 的区别都保留。该条件下，原完整整数构造给同一 RN128 结果词，原 fallback 给同一实际 Q 表达式，原求和顺序也不变。

四个入口及八条统计路径为：

| 原函数与完整循环 | 新模式局部变量 | 原路径 |
|---|---|---|
| root_evaluate，$j=0,\ldots,M-1$ | r583_synthesis_rounding | fixed_fallback_P、fixed_fallback_Pt、L、evaluation_u_words、evaluation_u_fallback |
| root_evaluate，$i=0,\ldots,J-1$ | r583_residual_rounding | root_residual |
| root_matrix，$k=0,\ldots,2M$ | r583_gram_rounding | root_gram |
| rhs，$j=0,\ldots,M-1$ | r583_flux_rounding | primal_flux |

这四类循环会在实际轨迹中多次出现；“四次”只指四个源码位置，不是整条运行总计四次系统调用。原 complete loop 内没有设置舍入模式或引入 callback，R583也没有模式 setter；外部异步模式修改不属于上述等价结论。

八条路径各自的17个原计数全部保留：

`terms`、`exact_normal`、`exact_signed_zero`、`original_multiply`、
`fallback_layout`、`fallback_rounding`、`fallback_left_nonfinite`、
`fallback_factor_nonfinite`、`fallback_left_subnormal`、
`fallback_factor_subnormal`、`fallback_factor_precision`、
`fallback_result_range`、`rounding_below_half`、`rounding_exact_half`、
`rounding_above_half`、`rounded_up`、`carry_to_next_exponent`。

完整 last、last_present 和所有实际存在的额外原 RootStats 字段也保留。没有增加一个虚构的“R583成功计数”替代原统计。

逐乘积等价与原累加顺序结合，按实际循环索引归纳得到完整循环出口的同一有限结果；按原 root evaluation、选中分支、原 RK 与 caller 的顺序继续归纳，可在两程序执行到相同有限前缀时保持这些数值词与分支。**不由此断言实际墙钟停止地址相同、运行更快或整条一定完成。** 也不声称浮点异常标志、系统调用次数或全部机器环境可观察行为相等。完整条件限定由 R583 原文承担；244不扩大该数学结论。

## 584.4　三层实际请求与原454个来源

本入口公开的244 JSON 是小型组合合同，不是伪造的完整科学请求。它固定：

1. 原248公开小请求的完整 file/bytes/SHA；
2. 原248 generator 与 plan；
3. 已刊 R583 adapter/header/plan 与完整祖先计划；
4. 本次十个 caller 的完整 literal plan 与目标身份；
5. 原248完整资源政策、原输入责任及当前真实 namespace。

实际 prepare 先调用原 R593：

`prepare --request 原248公开小请求 --request-sha256 原SHA --computations 真实HERE --out request248-source-preparation`。

原 R593 在同一作业中先生成全454来源，再产生自己的临时完整248请求。新 generator 必须从该原 source-views.json 所给 file/bytes/SHA 读取此完整请求；它不能把248公开小请求误当包含全部 scientific fields 的对象，也不能用一个旧 run 的请求身份替代当前实际字节。

所有454个实际文件逐一保原 basename/SHA，91个原 generated 文件同样保留。新来源清单为：

$454+3+2+10=469,\qquad 469=366+103.$

其中3个 public source 是 R583 header、R583 adapter与当前 generator；2个 generated source 是 R583 primal/trace include；10个是实际 caller view。原3层旧来源表仍作为来源祖先完整存在，不会因为当前实际 source 改名而删除旧条目。正文中的469是这份确定组合的显式源清单，**不外推成任意动态导入都已封闭的全局定理**。

新的完整244请求对原248实际完整请求作深复制。lanes、两README身份、六个原输入、actual63、actual91_artifact、runtime、resources、live_call_resources、original_scientific_contract、retention和R593_resource_strategy逐字段、逐JSON类型保持。只替换当前 schema/namespace/实际 caller 与当前来源映射，并给真实 R583条件、完整祖先 arithmetic合同和新来源收据独立字段。原所有科学数词不由新 outer 重算。

实际当前请求由 prepare 写入临时目录，运行时SHA由实际字节形成并传入后续所有命令与 report。公开请求不能预写该含当前 run、绝对路径和来源收据的动态 SHA。源准备阶段不产生科学时钟，也没有复制旧科学输出。

## 584.5　完整同目录 literal 生成与事务边界

所有源在真实 checkout 的 topic/computations 内，且

`HERE = GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations`。

新源与原 source 都在这一真实目录被调用；没有仅报告假 HERE 的私有科学目录。原公开 JSON、原源文件和 Git checkout 头保持。prepare核实际 HEAD=GITHUB_SHA；原 source-only 子进程继承会话、同步等待返回，不新建独立 session。

顺序为：

1. 写当前 source-views.json，列出2个 R583 include及10个 caller 的全部未生成角色。
2. 原 R593 source-only 返回，并核实际原248 receipt、完整临时请求及全部454文件。
3. 使用 R583六参数CLI形成 R583/source-binding.json；R572→R564→R561→R550→R535只做来源形成与校验。已存在的原匹配 include只能按真实完整字节复用，不能默认为已科学执行。
4. 记录两个实际 R583输出：文件存在、完整 bytes/SHA、是否匹配、各真实未完成地址。即使 child 返回非零，也尽可能保留真实存在的 partial binding和源文件身份。
5. 按十角色原序读冻结 baseline，对每条完整 before/after literal核实际 occurrence count，形成每份完整新文件后核最终 bytes/SHA，再写其“已生成”记录并移出该明确角色的待办。
6. 形成469来源映射与实际完整244请求，最后才记 complete=true，并输出当前请求路径与真实SHA。

失败时保留已经写出的 source与当前phase/error/traceback、完整未生成角色；没有用“前几件生成成功”替换整链 complete。源级 file/identity/唯一 literal 检查是声明的来源约束，未新增任何数值比较或科学门。

## 584.6　十个调用角色是真正执行闭包

下表的字节身份是本次实际 generated source，不是已提交的独立展开文件。完整 baseline、每条 literal与输出身份都在当前 plan。

| 角色 | 当前完整 basename | UTF-8 B | SHA-256 |
|---|---|---:|---|
| 实际逐 H owner | `geometry_20261116_live128_loop_rounding_observed_same_call_owner.py` | 27053 | `502f3115a9dcf04edf61f1673ef6712fb451367d64a76ddba4352b853d3c2988` |
| 当前576系统调用 | `exact_20261116_live128_loop_rounding_observed_current576_system.py` | 29067 | `bb84f3cc892f8e62978c560c939605643b0b4f7f72293f6184e5c86a6dd88120` |
| 完整链 QR | `exact_20261116_live128_loop_rounding_observed_current576_chain_qr.py` | 21853 | `d0b969e736f2d5a72509cc009cd31b2e36e34db5b0504a6f9aa198459556528c` |
| 同 call pipeline | `geometry_20261116_live128_loop_rounding_observed_call_pipeline.py` | 43271 | `b63fd14f991dca9e90c1af62deda228f7288e687c8f7bc1ebc3c24235e096533` |
| Node 当前 call | `geometry_20261116_live128_loop_rounding_observed_current_call.mjs` | 45451 | `2aef695f6e7a5fbae43873a20d384c2ccddb42cefde4b748e029dc210d0cd3f5` |
| 完整协议 worker | `geometry_20261116_live128_loop_rounding_observed_worker.mjs` | 8322 | `19d11706b57e6db3371893a840c25aac7f4bb22074554e553de8084015f59e51` |
| 真实 tail client | `geometry_20261116_live128_loop_rounding_observed_tail_client.py` | 41888 | `1147c22f5c860c62a41d5782d54b0f739d54adf32236f10d7f5d55013a3a32f6` |
| 原 full112 / FD / fullDN | `geometry_20261116_live128_loop_rounding_observed_original_full_dn.py` | 48155 | `2dfe9885b91c0db9a41099065a6c336eb589c310fc2e0d25d28e6ca11d3e43e5` |
| 资源与生命周期 | `geometry_20261116_live128_loop_rounding_observed_owned_run.py` | 39343 | `35072e528edb63d1d7c2b28f1e87e11539680cb07734dfae58196bc4a605f1e1` |
| 完整必要读回 | `root_20261116_live128_loop_rounding_observed_necessary.py` | 66607 | `e3d2869e86374d5ee3b01272f757bf8e5a74c7e71f90ed88cbabc369d556323a` |

实际拓扑为：runner调用新fullDN；fullDN选择新client；client给Node worker、current call、pipeline、system与QR实际新来源；pipeline先调用新owner再按原合同形成当前投影模型；system与QR的 hook也指向新current call。所有硬绑定源名、SHA、schema与policy同步更新，原数值正文保持。

新client保全部旧 LIVE_SOURCE_PINS，只追加本次实际 tuple，实际命令与source_file改为新文件；新fullDN同样保 SOURCE_PINS祖先并绑定实际client。其参数维数、初猜、原FD流程、原17档prefix试步、域门和最终 fresh audit没有替换。system/QR只改变真实调用源身份；QR数值式与原数据布局不变。

完整维数保持：

- 原112 field/tail modes、spacing2、576 stages；
- 577个径向节点上的224维shooting state；
- 原226维局部RK状态，包括两个mean；
- 全224方向，stage责任仍完整576×224×224；
- 输出338行按原实际顺序：slope112、second112、meanSlopeCorrection1、meanSecondCorrection1、height112；
- 请求完整338×112 J，保原混合导数合同，不声称全部338行解析。

R273恢复、owner128真实值、全当前模型与真实FD/fullDN都仍须按原控制流付清。源生成没有给任何一项写入科学完成。

## 584.7　唯一 R583 installer 与真实编译

新owner在原同call工程视图中取得实际原 persistent owner_scope。它读取当前244 source-views.json，核：

- 当前schema、request244、run/source与真实HERE；
- 当前owner完整身份确实出现在本次已生成角色中；
- R583 source-only child已真实返回0；
- child记录的实际binding文件恰为当前 R583/source-binding.json；
- 实际完整binding与child中原source_result逐字段一致；
- R583 adapter完整22648B与SHA。

随后只调用一次 R583.install_owner_compiler(owner_scope,binding)。原 R583 installer要求该scope中没有已有R583/R572/R564/R561/R550/R535安装hook；它作用于真实原 compile_owner及其真实 globals，并用完整声明的compiler函数与24项实际依赖。没有先安装五个祖先再覆盖，也没有把来源准备称编译。

真正的owner main之后才按原流程编译和执行。编译记录保留在原
`root_finite_word_cache_compilation_source_binding` 字段，内容现为完整R583 binding加实际compiler command、实际include、stdout/stderr、executable、exit与原来源身份。该历史字段名不等于仍执行R535；实际schema和actual_adapter才区分当前来源。

两新 include 的字节由 R583计划约束：primal28149B/dc8a2394…，trace36388B/37e54b04…，trace实际include新primal；原 persistent C++主程序22364B/7789007e…仍完整。原owner正常solve、fresh replay与其实际输出流程未改，原后置组件由R534明确deferred而非虚称已完成；新pipeline按原同call继续其原责任。

## 584.8　同一个全局钟与未知资源前沿

记当前全局deadline为 $T$，当前时刻为 $t$，去掉原120秒末 reserve后的整秒余量为

$R=\max(0,\lfloor(T-t)/10^9\rfloor-120).$

原requested audit时 $A=1800+345$，否则 $A=0$。本次与248相同：

$B=\min(12000,\max(0,R-A-330)),$

$P=\min(1200,\max(0,B-301)).$

原已有启动责任仍要求实际 $B\ge600$、$P\ge60$；不是新加门。owner实际deadline还与原全局deadline及audit/末reserve相交。原solve_until从owner直到时刻再扣实际replay $P$。因此12000是上限，replay包含其中，并非每H新增12000秒、更不是19200+12000。

原stage8000位于owner与replay完成之后，按那时真实余量裁剪；它不是owner之前另一个8000共同上限。boundary/endpoint/audit和factor等原阶段仍按同一个T裁剪；没有跨H、FD、trial或后继重开钟。原32 native迭代、原10尾试步、原两组FD及原全部层数和接受阈值保持。owner12000提高了可用局部窗口，也可能压缩后续阶段余量；本文不承诺完成更长链。

临时容量仍原64GiB startup/2GiB resource stop，原最多18个uncached protocol call只是原控制流上限，不是容量可全部容纳的证明。原raw只留当前作业临时空间，原末必要读回与所有权静止后才能清理。

## 584.9　原科学门、现有初猜与返回责任

当前同H缓存仍只可在该H实际调用已返回后使用。跨H已有last、切向/幅度/边界初猜逻辑完全保留；新入口没有把旧last改名当新优化，也没有用旧H的已接受status免除本次当前H求解。

原native solve_tolerance $2\times10^{-9}$、prefix RMS $10^{-6}$、边界 $10^{-11}$、FD相对阈值 $5\times10^{-5}$、全部适用contraction、physical/domain门与原final same-current-H fresh audit不动。FD仍direct_boundary与separated_boundary两组，各10方向、原3步长层及2层Richardson；完整原失败地址、实际档位与未返后缀由原reader承担。

R583只关系原有限product实现；它不把128状态变成连续尾的数学存在证明，不把64模型投影变成native接受，不把有限prefix问题变成完整闭面，更不声称原RMS就是relative-metric floor。

## 584.10　两个原必要scope与完整新binding

source必要与science必要是两种原来就独立的语义scope；每种仍只有一个完整body且各不得超过90000B。本次不把同一个超限对象拆成若干包。

source reader实际执行原R593 readback。若原transport70，则只从仍在同job的原完整临时necessary文件读取其全部字节，并核原bytes/SHA；不是从SHA恢复不存在的raw。原完整body、其全部来源与自己的逆定义完整保留在当前source必要对象中。当前部分另含当前source-views.json全部值、R583 child完整binding、全部新模式合同、实际partial/source_pending及完整当前stderr。当前stdout仅保其原完整身份；不是宣称全文科学日志已回传。

R588仅对当前source记录施加既有具名关系。原父必要对象可能已带自己的关系，故整块保持，不再递归重编码；当前逆明确只应用于current_source_record。未知R583 schema、完整actual_loop_mode_source_contract及其它新字段必须原样保留。候选连同关系与逆说明后只有在**同一完整body**真实更短时采用，否则返回完整原值。表示失败增加真实metadata错误，原值继续保留；不设新科学门。

science reader沿原完整RootStats catalogue、source记录、所有实际trial/残差/FD/fullDN/错误/未返选择；新owner的六个明确source合同标志和实际R584声明加到必要选择。原 compiler/source binding取整个原对象，R588不认识R583也不能丢字段。八路径17计数和完整last仍通过原完整对象/具名逆回传，不将缺键、null、未执行或partial填成零或成功。原dict序列化顺序不冒称与raw逐字同；明确类型、值、缺键、负零、原数组顺序的语义责任仍沿原定义。

任何完整body大于90000B，均保原真实尝试bytes/SHA与70，完整对象仅同job暂留；不截断、不抬限、不预言本次必fit。不能把reportjob成功或preparation成功当科学完成。所有输出后才由唯一终态读者依据真实scope写R585。

## 584.11　所有权、失败路径与清理

source准备不生成science namespace所有权，也不伪造科学receipt。若新source准备或原输入恢复失败，后续正常科学步骤不运行，always读回仍尝试返回实际来源/错误；若实际完整请求或reader未生成，则如实返回必要未返，不能构造一个看似完整receipt。

科学进程仍由原 scoped PID/startticks/PGID/SID与真实后代登记管理。真正own或可疑own不可读时保持unknown，禁止读删；不把外部同uid进程env不可读普遍认作本namespace，也不普遍忽略PermissionError。原requested审计与所有数学门并不由quiet替代。

workflow只有 source必要complete与science必要complete同时为true才调用原cleanup；原cleanup再核真实source/request/run/summary及实际quiescence。科学partial可以在所有原必要范围已经完整读回、真实静止时按原合同清理；科学success本身也不能豁免必要传输或quiet。任何超限、必要未返、unknown或signal都保原停止/不清责任。临时source目录与生成文件不作为科学成果上传。

## 584.12　发表清单与可检验的实际后继

正式发表的是小generator、完整literal plan、小outer、workflow、本文与完整CLI接口。十caller展开及两个R583 include只在Actions真实形成；作者为了来源交接形成的全文不作为Git主树科学数据。

当前sourcegenerator为37130B/5057de1e663103be71df6ab6e611079aae3cd33ed1820fd5ea1e41d2280b4e91；
plan52014B/07440c18dc532b8f49029f1615b60394e331845d5e1e469c07d87559da8ec5cd；
outer19999B/f7b39ebf453dce5f899a9f2a9a72753370d33249198a1bfe5c1ee23226c4d1b0。
完整CLI、每份identity、两个frame及当前动态请求路径见
[request244接口](../notes/2026-11-16-request244-loop-rounding-observation-original-full112-interface.md)。

本次结论支付完整调用与条件来源责任。实际root轨迹、原门值、每阶段耗时、编译返回、eight-path统计和完整末必要仍只能由request244本身付清。正式入口由根唯一Git发表后单次workflow_dispatch，官方run/head再绑定；旧248标签或R583已刊身份都不能代替本次运行结果。
