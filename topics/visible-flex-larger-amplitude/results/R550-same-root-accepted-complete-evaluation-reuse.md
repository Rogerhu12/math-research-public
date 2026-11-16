# R550：同一次根调用中已接受完整求值的下一迭代复用

作者：OpenAI ChatGPT（AI）。日期：2026-11-16 UTC。

**可信度：已证明，限本文的真实来源、完整有限程序及所列条件。** 本文给出完整可调用的源码准备器和实际 owner 编译接点；没有新的科学运行、速度测量、残差或接受父。源码文字、literal 替换、JSON、bytes 与 SHA 在本地处理；科学算术、import、AST、编译和运行只在公开仓库自己的 Actions 执行。本文不增设 fixture、独立审查或试跑前门。

本项承接 [R535](R535-original128-local-finite-root-words-and-real-compiler-hook.md) 的原128局部有限词，不改变其原算术表达式。新的工作仅是：原根线搜索刚接受的完整 RootEval，在同一次 root 调用的下一次迭代中输入不变，可以直接交给原消费者。所有原试步仍计算，所有方向传播仍计算，原停止、fallback、30×20 root 限制及32×10 owner限制均保持。科学计数只记录真正执行的工作，未执行求值不虚增到旧计数。

## 550.1 原程序的确切重复

R535真实 primal 是25230 bytes / 3e1cb0a416418fe56fbee889df5debdfc9ed097b797a1b8e086b563ce4fd9241。原 root 的每一迭代先执行：

~~~cpp
auto ev=root_evaluate(p,e,target,state,g,stats,&fixed_words);
~~~

若需要方向，原 root_matrix 与 spd_solve 产生 step。每个原 trial 形成原字 trial，并真执行：

~~~cpp
auto value=root_evaluate(p,trial,target,state,g,stats,&fixed_words);
if (value.err<ev.err || value.err<=policy.stop*scale) {
  e=std::move(trial); accepted=true; break;
}
~~~

下一迭代的 e 正是上次实际被接受的 trial。p、target、state、g 和该 root 的 fixed_words 都仍是同一真实对象；原 RootEval 不使用 stats 的旧值决定数值。原代码却销毁刚得到的完整 value，再用同样输入重做 angular rows 和 residual。这里的“重复”是逐操作输入相同，不是将两个不同 H、RK stage、geometry 或近似点视为相同。

R535真实 trace 为34950 bytes / 2e122e0ca6ad21e1c11ab711cc5af40a6955d3ff054f6cd445dbd885fbb98b12。其 root_variation 也在原 line search 中求出完整 primal value，接受后另对**旧** iterate 的实际 F、C 和 taped solve 求方向，更新 de，最后 e=accepted_trial。下次 root_evaluate 不接收 de 或 direction；刚求出的 accepted primal value 因而仍是下一次所需的 primal 输入。原 F_direction 必须继续使用新的 de 和相同完整 primal rows，不能把上次方向也缓存成当前方向。

本项不是取消根线搜索、缩减角点、截断列或采用前次 root 的结果。初始 e=0 的第一次求值始终实际执行；每个 trial 无论接受与否也始终原样执行。只有已经真的返回、被原条件选中、并且还存在下一次原迭代的完整结果，才有资格被下一迭代消费一次。

## 550.2 实际源码结构

公开新增三个运行/计划文件：

| 文件（topic内） | bytes | SHA256 |
|---|---:|---|
| computations/root_20261116_accepted_root_evaluation_reuse.hpp | 7311 | 8610fdd602ca3cea28a0d28af254e1929e954d7762161cc4887af5a097190f26 |
| computations/root_20261116_accepted_root_evaluation_reuse.py | 16634 | 66c2ff0d0b29c41cef00cc6a77764e4e168d2885c52b3f56c2abd961fad8f97c |
| notes/R550-accepted-root-evaluation-complete-source-plan.json | 12303 | 14b5c02071359276be2988dc273d6864df3d61e728df10df5b1bddc498134457 |

本篇是第四个发表文件，同时给出完整证明与CLI/owner/reader接口。plan自身不钉adapter hash以形成自引用循环；adapter固定完整plan身份，实际外层请求必须再绑定adapter完整SHA，实际binding也记录真实SELF。

两份展开源仅在Actions的真实computations目录生成，不作为重复完整源码加入Git：

| 角色 | 新basename | bytes | SHA256 |
|---|---|---:|---|
| primal | root_20261116_accepted_root_evaluation_reuse_primal128.cpp | 25794 | 40e89e28adc36848cf0d28b466e219065e10bdf8b37145d5e18326a6cd5eb6e1 |
| trace | root_20261116_accepted_root_evaluation_reuse_trace128.cpp | 35565 | 822488bd3ca682478939baa7df047aa614218b6724e448f01705e10c9225eb71 |

primal有6个完整唯一literal变更：包含新header、RootStats新字段与join、原主iterate求值接点、原accepted试步接点、完整统计打印。trace有5个：新primal include、显式祖先/当前完整SHA、原主iterate接点、原accepted试步接点、完整统计打印。每项旧/新文字、count=1、base与output完整身份都在plan，正向变更和按逆序复原均按完整源字节绑定。

新trace保原R535 primal祖先SHA，并另列 actual included_R550_primal_cpp_sha256；实际#include用R550新文件。旧schema/文件名若来自原基础API，只是原接口来源，不代表旧展开源逐字被执行。新compiler回执明确旧 frozen_R283_numerical_prefix_is_byte_identical=false。

## 550.3 一个root内部的一次性所有权

每个原 root 或 root_variation 函数局部各有一个 RootEval accepted_evaluation 和一个初始false的 ready。没有static、thread_local、跨root、跨state、跨RK或跨H缓存。

原accepted分支的完整 value 送入 r550_offer_accepted。仅该分支能设置ready；拒绝的trial与抛异常的partial结果都不能设置它。下一次原iterate求值接点调用 r550_original_or_accepted：

- ready=false：调用闭包内原 root_evaluate，保原参数与原调用；初次迭代属于此分支。
- ready=true：先将ready置false，再move该完整RootEval给原ev；不能重复消费。
- 原每次iterate接点先执行time_check，不产生新deadline或新的科学预算。

在primal中，被接受trial随后按原字移给e。在trace中，被接受trial先存为accepted_trial；旧F/C/taped方向传播和de更新保持原字，最后才按原代码移给e。若方向传播失败，函数按原catch写失败记录并退出，局部缓存随作用域销毁，不会被另一次root使用。

第29号迭代是原30次中的最后一次。其accepted结果仍计为实际offer，但没有下一原iterate，本helper不扫描、不保存该结果，并记no_next_iteration_results；原循环随后仍按原控制流抛 iteration-limit。没有借缓存多加第31次，亦没有从accepted trial提前改变原return选择。

## 550.4 缓存资格与原算法回退

资格只选择是否复用，不是数学接受条件。原trial已先通过原完整root_evaluate并按原误差条件接受；helper随后检查：

1. residual长度恰为原J，rows长度恰为原N；
2. err、max_quad、minD、minS、minA这五个完整返回词均finite；
3. 完整J个residual词均finite；
4. 完整N行的P、Pt、L、K、U、S、D、A、sd、quad全部十词均finite。

任何形状或finite资格不成立，就不置ready，下次继续原root_evaluate。没有将非finite改成0，也不将资格失败报告为BVP、domain或Newton拒绝。它仍是原算法路径，而不是一个新的科学门。

扫描只读取已返回词及其类型/长度，不重求F、不比较一个替代解、不求独立误差、不执行数值fixture。扫描每32个residual位置和angular行保time_check；资格扫描本身也计入原clock。新增的扫描时间、跳过的原求值、分配与调度可以改变预算内实际到达的前沿，本文不声称资源中断路径等同。

完整RootEval被move，包括两vector的完整元素和全部标量。没有只留err后重新猜rows，也不由有限计数重建未返回字。原R535的fixed_words仍限定在原root；它与本缓存是不同职责：前者共享root内部固定词，后者保已经真正计算完的整个accepted求值。

## 550.5 同输入完整有限词命题

**命题550.1。** 假定原声明的binary128编译/舍入语义保持，同次root的p、target、state、g不变，原数值表达式没有读取计数器或浮点sticky flags作输入，且所比较的计算范围完成。在上述完整finite资格成立时，被保存的accepted RootEval与原程序下一迭代重做root_evaluate应返回的每一个数值词相同，含signed zero。

**证明。** primal中e的唯一更新是把实际trial原字移入；下一求值的其他const参数均未改。root_evaluate先逐原操作形成L=target+e，momentum/pt、P/Pt、U及每行后续量都使用同一输入。R535的fixed缓存已按其完整来源和同一对象条件绑定；首次真实trial返回后，重复调用只读取已成同样固定词，或走同一个原finite回退。所有乘法、加法、sqrt、除法和累加次序不变，故逐操作输出词相同。全J residual与五个summary词由相同完整行按相同顺序形成，亦相同。完整资格确保这里没有把NaN按普通相等当成可复用对象；signed zero通过原存储和move保留，不作数值归一化。证毕。

这里不需要另外计算第二份值来“验证相等”。结论来自闭合的原调用控制流及完整输入不变。p/state/g不是按文本hash猜同一数值对象；局部变量的作用域与只在同一个root函数中消费给出来源。外层若变H/state/geometry，会进入另一个root局部对象，ready重新为false。

原函数对RootStats有实际计数和min记录副作用。计数不作为数值输入；旧minD/S/A反复吸收完全相同的已吸收正域值是幂等的，因此省略重复记录不改变这些数值极值。其他max/threshold/return统计在原root主循环中继续执行。旧angular_evaluations与R535词计数不伪造重复工作，本项将它们明确解释为实际执行调用，并另列逻辑iterate接点与真实reuse。

命题不主张两程序的wall time、资源耗尽位置、分配异常位置、浮点异常sticky flags或NaN payload相同。这些量未被该原数值算法用作接受判据；实际资源、异常和partial范围仍须如实返回。

## 550.6 原根选择、方向和外层owner

**命题550.2。** 在命题550.1范围中，primal root的原每次误差、scale、relative、stop/original-threshold/fallback判断、root_matrix输入、spd方向、每个trial字、原接受选择及返回L/rows保持；原RHS、RK4与外层owner数值门因此按原相同有限输入继续。

**证明。** 初始iterate真调用原求值。归纳假设某iterate的e、ev与原程序相同。原scale、误差判断、root_matrix与solve完全未改，故trial逐字相同；所有trial都实际执行原求值，拒绝/接受次序相同。若不接受，原fallback或错误分支原样；若接受，下一e相同，资格失败则下一原求值继续，资格成立则命题550.1给相同下一ev。原最多30iterate和20trial不改，归纳成立。return仍在原iterate检查处形成L并交完整rows；后续原RHS和RK4表达式未变。外层persistent owner源码、原方向/试步上限及fresh replay也未变。证毕。

这是条件有限程序结论，不是方程解存在、收敛速度或完整owner通过tol的证明。原同H全J/R273和每模型fresh W/J仍须实际执行，原338×112、FD/fullDN/final audit责任没有由局部复用代付。

**命题550.3。** trace_variation继续对原实际选中的同一有限轨迹作原方向传播；复用primal accepted RootEval不会复用或丢弃应重新计算的方向。

**证明。** 原root_evaluate不接收de/direction。接受trial时的新primal value仅取决于下一e与不变的原primal输入，故更新de不影响命题550.1。旧iterate上的F_direction、C_direction、spd_solve_direction全部原字保留，仍读旧ev和原tape；原accepted alpha也保持。下次iterate及最终return中的F_direction依旧使用当前de，并继续逐词same_value检查和finite_direction条件。没有缓存drows、dL、dstep或理想隐函数导数。由与命题550.2相同的归纳，原primal选择和每个实际方向更新保持。证毕。

这里沿用R283的实际有限轨迹方向合同，不把它提升为IEEE舍入函数的解析导数，也没有删除其原shadow checks或新增另一套科学对拍。


## 550.7 完整实际统计与失败地址

原RootStats新增r550_reuse，其primal与trace_variation分别完整记录下表；原统计和R535统计仍保留。两个路径不互填计数，不从primal结果推trace已执行。

| 计数 | 精确含义 |
|---|---|
| iteration_sites | 通过该原iterate入口time_check后实际进入复用选择器的次数 |
| original_main_evaluations_started | ready=false而真正开始原主iterate求值的次数 |
| original_main_evaluations_returned | 上述原求值正常返回的次数，异常未返不补 |
| reused_complete_evaluations | 真正消费一个完整ready结果的次数 |
| accepted_results_offered | 原接受分支实际送入的完整trial结果次数 |
| qualified_results | 完整资格扫描通过并已move保存的次数 |
| shape_declined_results | 完整形状不合而放弃复用的次数 |
| nonfinite_declined_results | 扫到某个非finite实际词而放弃复用的次数 |
| no_next_iteration_results | 原最后一次迭代接受、但原循环已无下一求值位置的次数 |
| summary_words_visited | 实际扫描的五summary词总数 |
| residual_words_visited | 实际扫描的原residual词总数 |
| angular_rows_visited | 已实际开始扫描的angular行总数 |
| angular_words_visited | 实际扫描的angular十词总数 |

每条路径另保last_present；尚无事件时last严格为null。已有事件时last完整保phase、零基iteration、零基row及零基component；不适用的row/component是null，不能误填0。扫描中资源中止保真正到达的地址，不把尚未扫描后缀计成资格失败；异常前已更新的计数也不“配平”为一个完整调用。因而不以这些统计的代数关系代替真正完整返回。

原RootStats::join在原stage index次序合并两个路径，只有被合并项确有last时才更新last。原每个root缓存仍是函数局部对象；本项没有为并行stage建立共享缓存。primal打印和trace打印都加入完整root_accepted_evaluation_reuse对象，schema为：

~~~text
R550-same-root-next-iteration-complete-evaluation-reuse-v1
~~~

对象包含上述两条完整路径及原实际计数语义、原join次序、原root限制保持、没有跨root缓存等明确字段。新字段不是若干计数摘要；完整路径及last必须连同原RootStats保存与读回。原scientific evaluation/iteration/line-search记录、原failure记录和R535十八项统计不能被新对象替换。

这里的“完整实际统计”限源码所捕获并由原错误路径留下的对象，不声称操作系统强杀前尚未落盘的内存必然可读。原实时guard、错误日志、missing/partial记录仍分别负责该情况；没有根据最后一个计数补出未来已返回对象。

## 550.8 公开Actions中的完整来源准备

adapter只接受GITHUB_ACTIONS=true且GITHUB_REPOSITORY为公开Rogerhu12/math-research-public，并要求GITHUB_REPOSITORY、GITHUB_RUN_ID、GITHUB_RUN_ATTEMPT、GITHUB_SHA四项实际值齐全。它不创建新科学clock，不执行owner，不执行g++，也不为根求值创建任何fixture。

先将三份新增运行/计划文件及原R535完整依赖恢复到真实source目录。调用者先建立本次独立binding输出目录，再执行：

~~~bash
python3 -u "$COMP/root_20261116_accepted_root_evaluation_reuse.py" \
  --source-plan "$TOPIC/notes/R550-accepted-root-evaluation-complete-source-plan.json" \
  --ancestor-source-plan "$TOPIC/notes/R535-native-root-finite-words-complete-source-plan.json" \
  --binding-out "$ACTUAL_CURRENT_SOURCE_PREPARATION/R550/source-binding.json"
~~~

COMP必须是本次Actions真正执行后继owner的computations目录，不是另一个校验目录；TOPIC是同一次实际topic路径。新binding文件用xb创建，不默默覆盖旧run的准备结果。环境变量只是具体运行路径，不能把示例字面值当已存在文件或本次输入。

prepare_sources首先核完整R550 plan及header，再核原R535 adapter10892/1c99623e、header7102/6706eae6和plan10232/f3b7900f。随后从该实际路径加载完整R535 adapter，仅调用其原prepare_sources。原R535 preparation可以遇到已经存在的合法生成源，此时必须完整bytes/SHA相同；不覆盖不同源，也不调用它的install_owner_compiler。

准备后的实际R535 binding必须满足：

- 原schema和source_preparation_complete=true；
- compiler_completed=false，不能把源展开声称为编译；
- actual_source_root与当前HERE一致；
- 实际adapter/header/完整plan身份一致；
- 两个原primal/trace、两个R535展开源、原persistent Python和CPP完整来源列表一致。

新primal和trace分别从真实R535展开文件执行plan中6/5个唯一literal变更。每个变更要求count=1；所有逆变更按逆序唯一复原完整原文；输出全bytes/SHA必须精确命中550.2表。若目的文件已存在，则核其完整身份；否则用xb写入。上述都是实际来源组成，不是用数值fixture“试出等价”。

成功binding schema为R550-accepted-root-evaluation-source-binding-v1，完整包括actual_source_root、四run键、真实SELF adapter、完整plan、整个actual_R535_source_binding、两个actual_headers、原R535两展开基底及原owner/CPP、两个actual_generated_sources、每view实际literal数、完整逆恢复标记，以及source_preparation_complete/ compiler_completed/未作科学求值等范围字段。只有全部来源处理成功后，source_preparation_complete才置true；compiler_completed仍false。

准备异常时返回code2，保实际异常type、message、完整traceback和实际partial_sources。该partial列出四个R535/R550应生成文件、每个实际present、expected及存在时实际完整身份/匹配值；读文件本身的错误保完整read_error。不能因为某个文件存在就说全部prepare完成，也不能只留异常名称后删除已到达的源范围。

完整binding先按原定格式落文件。若包括换行的ASCII JSON不超过90000 bytes，stdout一次返回R550_SOURCE_PREPARATION及整个对象；若超过，stdout只返回实际bytes/SHA、overflow事件、source_child_returncode和complete_necessary_body_returned=false，exit70。overflow元数据不是完整正文。外层必须同时处理真实child returncode、stderr、实际binding文件身份及必要body范围；仅文件中的source_preparation_complete=true不能替代完整运输成功。

## 550.9 直接安装在原owner_scope，随后由原main真正编译

科学调用者在加载真实原geometry_20261115_native_persistent128.py为原owner_scope后、执行其原main之前，调用：

~~~python
r550_installation = R550.install_owner_compiler(
    owner_scope, actual_R550_source_binding
)
~~~

R550是从实际、已固定完整身份的新adapter加载的module，actual_R550_source_binding必须来自本次550.8的完整文件/实际child，不是由几个摘要字段手造。该scope仍必须含原main和原compile_owner；两函数的__globals__必须恰为这个同一dict，HERE也必须指向同一实际source目录。

**不得先安装R535 compiler再装R550。** R550内部使用R535 source-only准备及完整祖先binding，但它直接替换原compile_owner。安装器明确要求scope尚无_R535_SOURCE_BINDING或_R550_SOURCE_BINDING，且CPP/ORIGINAL_CPP/TRACE_CPP仍是原名字。双装不是合法捷径；后继R551应把旧实际安装接点替换为这一次直接安装。

安装先再次核本次run/source、完整binding/plan/adapter/header、所有原与新source；再从43371 bytes / 767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322的真实原owner文件抽取完整compile_owner函数。原函数必须为：

~~~text
3860 bytes
be019045058f4616f98b07e19c0d8d3901e979ce2b1ba7d4259c65fcae4ae46d
~~~

四个plan中完整唯一literal变更产生：

~~~text
5781 bytes
4a0aeb01397968d660181e109b8f7a44e9363712f8173640d50739c19cabdc45
~~~

逆序复原必须得到完整原函数。所有原PINS保留，再加入两个header、两个R535展开源、两个R550展开源及两个实际adapter；ORIGINAL_CPP和TRACE_CPP改为本次真实R550文件，_R550_SOURCE_BINDING保存完整deepcopy。只在公开Actions中定义这一份已声明的函数，不在此时调用它。

安装receipt包含实际run、adapter、plan、原与新完整compiler-function身份、完整逆恢复、原persistent main/solve/replay/limits保持、实际persistent CPP，以及actual_compile_not_yet_called=true。这不是g++成功，也不是一个owner solve已完成。

随后原main按原逻辑调用这一个真实compile_owner。新函数先核本次R550来源目录和两个新展开源、两个header、两个R535祖先展开源、两个实际adapter，仍核原persistent CPP显式pin和完整trace pin。原standalone trace main的唯一边界仍必须存在。原full226 observer从本次实际primal完整evaluate正文形成，四个原observer变更及整个逆恢复仍执行；它只在原RK返回后复制完整226值，未改原RK运算。

实际persistent CPP保持原字：

~~~text
geometry_20261115_native_persistent128.cpp
22364 bytes
7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd
~~~

生成include仍用原接口basename native_frozen_trace_variation128.inc；名称不是“数值prefix仍原字”的断言，回执中的旧frozen旗已明确false。实际g++命令保原gnu++17、O3、OpenMP、frounding-math、ffp-contract=off、fno-fast-math、两个原include目录和quadmath；原300秒compile wall、原进程组继承和terminate_owned不变。没有另起非原owner的科学预算。

只有真实g++返回0且exe存在，才形成compiler_completed=true的编译回执。原actual command、实际include、returncode、exe、stdout/stderr完整身份均保；同时明确本次包含R535有限词和R550已接受求值复用。整个祖先source-only binding仍嵌入，里面compiler_completed=false保持其原阶段意义，不能改成一次从未发生的独立R535编译。

编译回执分别列真实included primal/trace、原primal/R283祖先、R535祖先和真实generated prefix。原evaluate observer整体身份、inverse标记、完整stage值与原PGID责任继续保留。编译失败/timeout沿原异常路径，不伪造成功receipt，不用安装成功推exe存在。

## 550.10 完整读回与后继实际入口

本项不注册request，不派发科学run，也不改已经运行中的225/226/229/231。它交付一份可直接接在真实owner_scope的完整组件；后继完整入口另由R551/request232绑定来源、调用和读回，实际终态预留R552。

R551必须同时保留：

1. 原prepared source的整个实际R535 binding和本次整个R550 binding、source child stdout/stderr/returncode/partial范围；
2. 实际直接安装receipt与原R534 deferred hook各自作用的符号和次序；一个替compile_owner，一个替原post入口，原main只运行一次；
3. 真正g++的完整root_finite_word_cache_compilation_source_binding与原compile record；
4. 原普通owner调用、失败/partial记录和独立fresh replay中的整个RootStats，包括未知新root_accepted_evaluation_reuse dict；
5. 原R535完整统计、原R534完整投影/模型/guard/未访、原完整FD/fullDN/final audit的所有旧已选必要字段。

现有R536/R547 reader采用whole RootStats并让未知字段保持literal，因而有承载该新dict的来源条件；实际新reader仍须在正常与恢复两条路径共同保完整对象，不能仅把新计数挑入一个短白名单。既有八个具名完整关系表继续使用原明确逆；新nested dict若未被专门声明，就逐值literal保留。header/所有其余字段都计入原whole90000上限，严格更小才采用关系格式，超限70且complete=false；本项不保证新完整body必然可装下。

R551还须独立修复R543已证的真实请求字段断口：system读取当前caller真正写入的same_call_complete128_value_components_and_explicit64_linear_model_required。不能添加一个旧same_call_complete128_final_components_required=true来冒充完整128线性模型；R550局部复用自身并未修复此Python来源契约。guard修复、R550复用和实际原128权威/显式64模型是三个不同职责。

完整调用链仍是原fresh全H/J/R273→同当前H真实128 owner→原tol与独立replay→同DN完整576模型/双mean/有限准确lift→原boundary/338endpoint/独立audit/assembly→原完整affine FD/fullDN/final fresh J与audit。原6000秒owner、1200秒replay、8000秒stage、600秒boundary、600秒endpoint、1800秒audit、全19200秒共享框架及120秒收尾责任不减，原32×10 owner与30×20 root限制不改。相应外层workflow/资源/90K/quiet仍由真实R551完整入口逐源绑定，不能从本组件推出已经执行。

## 550.11 已付范围与仍未付事项

本次已经完整证明同次root下一iterate的输入恒等、全有限返回词move保持、原primal选择及实际trace方向的条件保持，并交付完整源码计划、source-only准备、真正原scope compiler安装、原main实际g++接点、全部新增统计与错误/读回范围。所有用于判断的原数学表达式、原试步、方向、原停止和原全局科学门保持。

未付的是实际source准备/import/compile是否在未来入口成功、实际缓存命中、原6000秒内owner及fresh replay是否完成、完整模型质量与时间、所有FD/fullDN末门和全闭几何/精化目标。原真实withJ与每H原全J/R273成本也仍存在。本项不声称两套程序wall time相同、不会OOM/overflow、必要正文必fit或一定加速。

任何未来子过程返回、未启动后缀、预算或强杀，都必须由其本次完整必要证据判定；新统计不能补未来科学值，旧已删raw的SHA不能构造新的accepted父。完整非零112/338/450与课题README全条件尚未完成，继续沿open.md实际推进。

