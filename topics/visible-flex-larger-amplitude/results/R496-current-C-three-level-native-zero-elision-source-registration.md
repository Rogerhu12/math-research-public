# R496 — 当前连续 C 三层 native 的零系数线性作用与真实来源注册

作者：OpenAI / ChatGPT amplitude agent（AI）。日期：2026-11-16。

**可信度：已证明（限本文逐项列出的来源组合、局部浮点语义及控制流条件）；R496 新三层科学求解、闭面、材料查询和性能尚未执行。** 本文不把源码生成、哈希相同、日志计数或某个程序的 completed 标志当作 native/full-DN 接受。未来公开运行仍须消费原真实接受字段和各自未付范围。

## 1. 命题对象与来源边界

当前连续 C 的 453→450、同 far 的 112 模式加密以及完整增量 M 链，实际 native 使用原 captured-product Jacobian。其原 noJ 来源为 f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9，product 来源为 205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25。它们与 R195/R466 的有限 root trace 导数是不同对象。R496 不把后者移入当前连续 C 链，不删除原 factor、root、RHS、cusp 或边界条件责任。

真正新增的算术调用点是已刊 R494 的 geometry_20261116_current_C_noj_zero_eliding_variational_engine.mjs（12857 B，SHA-256 eafb41179f08105ac2cbc2708a3db84e1a3ae14eeec67027a94d3d7db70ea3c4）。它调用已刊 R474 的 geometry_20261116_finite_trace_zero_coefficient_linear.mjs（4832 B，eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02）。R494 已在 f863b71c0fd82b4b6b5a131ce2d99b14dea7bc95 发表；R474 已在 9ff15fddedfa1be31f9e486b225c4a64c9f6e7fd 发表。局部算术依据为 R473、R474、R494；原最终接受门依据为 R491。

来源基线取实际已发表 request216（634c4c85dbdb402965d5dc0bbc1ab756878ce87d）及其完整历史生成计划。该请求的原 JSON 为 57819 B / 994c1f2ef39e27e793b977f913f84bee4f4c4406431e23da5dc7dcf716cbdd55。R496 不修改该已运行请求。本次 49 个新源视图有独立名字、全文字节数及 SHA；旧公开源和旧生成源均保留，不能把新文件记作旧 identity。

执行环境失效后，本稿对应版本从固定公开原件及三份原生成计划重新逐字构造。最终新计划为 request218-current-C-zero-linear-source-plan.json，77274 B / e1bef5ad7727107014c9a4c494b22fd066a2866b7f5d97eb8dc1a424b0268360。它含 49 个视图、166 对普通 before/after 字符串、445 次带精确出现次数的应用。本稿不声称它逐字等于失效环境中未完整保全的早稿；较早恢复草稿 75475 B / fe75 的身份也已被本版替代。

## 2. 局部线性作用命题

令 $M$ 为实际模式数，$K=2M$，$n=K+2$。原 flow 在一个实际线性调用中创建全部 $nK$ 个正零输出，按 $i,j,k$ 次序计算

$$
D_{ik}\leftarrow \operatorname{RN}_{64}
 \bigl(D_{ik}+\operatorname{RN}_{64}(A_{ij}T_{jk})\bigr),
\qquad 0\le i<n,\quad 0\le j,k<K.
$$

这里 $A$ 为实际形成的全部 $nK$ 个字，$T$ 为该次实际 tangent。原循环只读取 $T$ 的前 $K^2$ 个字；两个均值输出行仍在 $i<n$ 中，不能据此删掉。资格检查针对这些真实被读字，不针对假定块稀疏性、输入参数有限性或理论三角恒等式。

**命题 1。** 对无并发修改的原数值 typed arrays，若上述全部 $A$ 与实际被用 $T$ 字均有限，则只跳过满足 $A_{ij}===0$ 的 $j$ 项，保留其余乘后加括号、$j$ 顺序和完整正零输出，与原循环具有以下逐调用关系：

1. 每个有限输出的 binary64 字相同，包括零的符号；
2. 非有限输出的分类相同；不声明 NaN payload 逐字相同；
3. 未改变两个均值输出行、完整形状列或后续 RK 组合；
4. 不声明整次科学运行字节相同、相同耗时或 IEEE 舍入程序的准确导数。

**证明。** 被跳项的两个因子分别为有符号零和有限数，故原乘积为有符号零，不会形成 $0\cdot\infty$ 或 $0\cdot\mathrm{NaN}$。原累加器从正零开始。两个有限 binary64 字的准确非零和或差是最小次正规量子的整数倍；因此有限加法不能从一个非零准确和下溢成负零。准确消去在 RN 模式给正零；正零加负零仍给正零。即使某个被保留的非零乘积先下溢为负零，随后加到正零也不把累加器变成负零。由归纳，原有限累加器不会因这些步骤进入负零，删除一个 $\pm0$ 加项不会改变其有限字。非零项的相对次序和乘法括号完全未改。

若被保留的有限因子乘积溢出，原前缀可能形成无穷或 NaN。向无穷加 $\pm0$ 保持同号无穷；向 NaN 加 $\pm0$ 仍属 NaN。删掉零项不改变以后非零项的顺序或符号，故非有限类别一致。对 NaN 的具体位模式不作超出语言/原硬件合同的推断。证毕。

**不合格分支。** 资格检查一旦发现实际 $A$ 或实际被用 $T$ 非有限，helper 执行原完整 $i,j,k$ 循环。它不抛出新的 finite-output 异常，不以资格失败拒绝科学求值，不重开时钟，不捕获资源异常后重跑。资格检查和统计本身有成本，新增记录也有 I/O 成本，故局部等价命题不能推出速度。

## 3. 从局部 helper 到真实 current-C runtime

R494 的 bindCurrentCNoJZeroElidingRuntime 先核原 runtime 中实际 noJ 与 product 的完整来源，再核同一真实代码目录中的新调用者及未变 R474 helper。它返回新 runtime 对象，覆盖实际 createNoJMatchedVariationalEngine 工厂；不原地重标输入 runtime。

原根和 RHS 先按 noJ 顺序形成实际 primal，再复制已捕获 root/derivative 给原 product Jacobian。fromCaptured 的单 root/value 读取、实际字段、四 RK 子步、原 $h a/2$ 而非重结合表达式、cusp 分支、observer 复制以及两均值状态均由 R494 原冻结正文保留。R496 不修改这个数学正文。

三个新 worker 均在原 ownerModule.loadOriginalRuntime 之后真实装载 R494，并将返回的新 runtime 交原 owner。每个 worker 的 source map 增加 R494 和 R474 的真实文件，不借旧配置的 noJ SHA 宣称已装新源。

实际 receipts.noJ 的顶层是 R494 调用者的文件、字节数和 SHA；其中 original_loaded_noJ_source 另存原 f9b，unchanged_R474_linear_helper 另存 helper，original_product_source 另存原 205b。原 config.original_runtime_sha256 仍描述它最初加载的完整原 runtime。二者具有不同用途，保留二者不是冲突，也不能只拿祖先 SHA 假称新调用者未装入。

**命题 2。** 若真实 worker、其显式 source map、原 owner runtime 和 R494 的绑定检查全部按该代码执行，则进入变分工厂的实际对象是 R494 新 runtime；原数值对象仍为 captured-product Jacobian，新增算术只受命题 1 的局部范围约束。

这是源码调用关系命题。尚未执行的 worker 没有实际调用统计；任何已绑定但未开始 owner 的状态，也不能被写成完成 native、完成 J 或接受了 BVP。

## 4. 三层真实来源链与原问题维数

### 4.1 首层准确十参数 453→450

新 candidate/legacy/hook/driver/launcher/pipeline 绑定已刊 actual202 初猜来源以及同一准确连续十族 factory。它们不把 finite-Gauss 的成功转成准确连续 C 的成功，不改变实际有理参数、binary64 投影、coast、cut_radius 或显式 sampling reserve 的生成规则。

首层三 active 的完整 453 问题仍须先真实求解，通过原 current-H、FD、338×112 责任及原最终判断；只有真实首末 checkpoint 才能形成全十词冻结的 450 初猜。450 仍由 fresh 全问题求解、fresh 当前 native、原 FD 和原终态支付，不能从 453 删除三行就称接受。

原 43f checkpoint writer 和 3bc profile 保留。writer 对实际 driver_source 和 runtime closure 的检查仍发生，新增 worker/client 的 identity 沿真实 config/native response 进入 checkpoint，不冒旧 driver 或旧 source tuple。原完整 112 far 与物理场仍须同 job 真生成。

### 4.2 同 far 的 112 模式加密

新 same-far sampler、driver 和 owner 保留 R456 的准确参数、原 far 与 $\mu$、全部配置及真实 parent checkpoint。它们改变的是新 runtime 的真实来源注册，不把接受父与保留原 112 far 混成同一输入。

这里还有一个独立、确定的来源修正。原 R456 的 joint 分支可选择 c71d legacy，但原导入的 live hook 仍可能是要求 ff667 positive legacy 的 bedb 版本。新同 far driver 按实际已选 legacy 的 SHA 显式选择匹配 hook：新 R496 legacy 对新 hook，原 c71d 对原 62010 joint hook，原 ff667 对原 bedb positive hook。它还把所用 hook 加入真实 closure。

该断口由源码直接给出；本文不将尚未走到这个位置的实际214/216失败归因于它。原 FD 顺序与门仍在原位置，不因修正 hook 而跳过 FD，也不新增对拍。

### 4.3 完整增量 M

新 M owner、R462 union 来源视图、R463 driver/CP 来源视图保留完整增量 M 合同。原112 config、原112完整far账本与真实 accepted parent 是三类不同输入。只新增的模式可按原 union 规则传播；新全 M deep、完整 native、当前 J、全部末门仍 fresh，不能拿旧112响应填新增列。

M 维数仍为完整 $4M+2$ 问题、全部 $3M+2$ 对 $M$ 的末端责任以及全部576阶段，native 状态仍保两均值。原配置若带兼容 modes 字段，按原明确规则更新为实际新 M；spacing 只沿原合法兼容规则。真正 computations 必须等 driver HERE，不能在另一目录生成代码却沿用旧目录标签。

R463 新 CP 读取真实 43f/bf7d/旧 M/自身父来源，并绑定实际 new driver、client、worker、sampler、union 和完整 runtime closure。与计算无关的来源字段例外仍由原明确白名单控制；原数值 policy 没有被放宽。命题 1 对任何实际 $K=2M$ 的合格线性调用适用，不要求 $M=112$。

## 5. 源视图生成的可复核含义

新小生成器 root_20261116_current_C_zero_linear_source_views.py（11895 B / 4d4c507edd571b67655fd2e66fb4bcfa173b1239928443831a81a925c4869ec4）只处理完整 UTF-8 源和普通 JSON。计划中的每个视图给出 baseline 的 file/bytes/SHA、依次应用的普通字面 before/after 与准确 count，以及完整 output 的 file/bytes/SHA。计划不是压缩或编码科学数据，也不执行补丁代码。

**命题 3。** 绑定上述精确计划后，只要生成器正常返回 completed=true，则本次生成的每个新文件具有该计划指定的完整字节，所有其基线来源仍未被覆盖；这些文件位于实际 GITHUB_WORKSPACE/topic/computations，与 driver HERE、profile/CP/code_directory 的原合同一致。

**证明。** 生成器在 named public Actions、真实仓库和自己实际 HERE 下核全部前提。它完整读取每个 public helper、每个 baseline，核字节数与 SHA，拒绝 source 重定向。每次替换前先核完整当前文本中 before 的实际出现次数。所有49个候选全文都在写任何输出前形成并核 output bytes/SHA；输出名须不同于原件、helper和彼此，且不存在于目标目录。写入用排他创建并 fsync，再读完整输出核原声明。输出名与所有 baseline 名最后取交集必须为空。故正常完成具有上述含义。证毕。

此结论不证明 Python/JavaScript 编译、科学调用成功、完整传递 import 图可运行或性能。新生成器明确不替代旧三套 source generation，也不替代 caller 的完整旧公开/生成闭包。未来入口必须先重生旧33视图，再在同真实 computations 生成新49视图，然后绑定全部实际来源。生成器自身不导入、编译或执行科学模块。

目标已存在、计划不符、literal count 不符或资源中断均是实际工程结果。写到一半的 current_view 和已完成 output 收据必须保留，不能因文件名已出现就冒全体成功。90KB 必要摘要上限仍硬约束；超限返回70并明确不授权清理。发生在受控状态建立前的输入错误可能只在原 stderr 中有记录，不能伪造 result.json。

## 6. 新场、闭面及共同材料图的来源责任

数值 runtime 变化后，新的 checkpoint/source tuple 必须沿 SavedPrefix、radial、shared、准确 cut、atlas、完整帽、metric、reach、held、共同材料与显示读取链传递。R496 因而有对应 source views；它没有给旧 loader 一个新 schema 字符串就假称兼容。

各数学消费者仍执行其原正文：R483 完整 coast 包围、原连续 C 查询、原四 Loewner、全 AA/AC/CC reach、整像 held、准确 cut 六jet以及真实帽 marker 求和均不改。五几何步骤仍从本次实际 checkpoint/geometry 重做，不借旧父的几何结果。reach 和 held 不以 metric 的成功作为新增先决门。

首层 construction policy 保留首次真实 radial→H、W、全 marker 原词以及 A/B 收据的生成规则。新 policy 的实际源 identity 被 first procedure、shared、held 和后继共同材料真实读取。B 缺失仍只使相应材料定义/测量未付，不以缺失 B 拒绝原 BVP 或独立 held。

相同十词、同 C 或同 W/H/markers 本身不能证明两个离散材料图逐字相同。R447/R457 的严格正材料图、完整 lift、准确逆定义和共同目标条件仍独立适用。新的材料注册仅把实际 R496 首112 A/B 与本次新 M field 的真实源连上；它不预先构造尚不存在的逆、共轭或全 t 估计。

显示仍使用真实准确 cut/current field 与完整帽。physical-angle-image 仅说明显示图像的参数化范围，不能冒固定首次 q 的顶点对应；first-material 模式需真实 B 和原 inverse API。R496 的显示 origin 同时更新实际 launcher 的 SHA 与 schema，不能仅换 SHA 而留下旧来源 family。显示误差、有限 t 样本与连续面内/全 t 证据的原区分保持。

## 7. 实际统计、未完地址与必要读回

每个新 worker 在 runtime 绑定、ready、原 native progress、response、failure、session-returned 的既有事件位置，记录实际 R494 readback。记录包括实际 worker identity、实际 call 地址和完整统计对象。它们是到该事件为止累计的记录，不是独立重算、不向状态/J 回写数据，也不是每个标量乘加的完整 journal。

九个原整数计数逐字段保留：

| 原计数字段 | 计数对象 |
|---|---|
| calls_started / calls_completed | 实际线性调用进入 / 正常返回 |
| finite_input_calls | 实际全部被读字合格的调用 |
| original_complete_loop_calls | 原完整 fallback 调用 |
| actual_A_entries_checked | 已实际检查的 A 字 |
| actual_used_T_entries_checked | 已实际检查的前 K 行 T 字 |
| zero_j_terms_skipped | 实际跳过的零系数 j 项 |
| scalar_products_skipped | 这些 j 项对应的 K 个标量乘法 |
| retained_j_terms_completed | 已完整完成的非零 j 项 |

表中第一行含两个原字段，合计九个。原 fallback_reason_counts、last_observation、未完行/形状地址、当前内列未逐项记录标志，以及 engines_started/engines_constructed 均保留。计数不表示 unique fields、完整 J、接受步数或速度。最后持久化观察之后的在途调用不得反推完成。

新 metadata helper root_20261116_current_C_zero_linear_statistics_readback.py（5941 B / 0b875858a99692d43b3a29387829884abf2ef31856c9ddc1d0ce0307dbb69ef0）只在原 owner 静止后的必要读回调用。它读完整 JSONL、核每个实际 worker/source/祖先/helper/product 字段，拒绝 duplicate member 和残缺末行，并核完整文件读前读后身份相同。缺文件明确 exists=false，不补零计数，不冒 native 已起。

必要正文保全最后一个完整原 observation；首 observation 仅保原行索引、完整记录字节数/SHA、location/call。所有中间记录在 Actions 内完整读取，正文给完整流身份、数量与 location 范围，不能称 root 已逐值读了全部中间树。原 JSON 值保留，不把这些 metadata 当完整 IEEE 状态或 NaN payload 的无损传输。

新增 I/O 可能遇到实际资源错误，本文不把这种异常改写成原数学失败或 whole-run 等价。各原 necessary reader 的数学/FD/error/partial 选择规则仍在；新统计加入各真实 native 分支。新增内容是否落在90KB内须由实际运行决定，不以预测容量删必要字段或保证必通过；超限与 quiet/cleanup 的原合同保留。

## 8. 原接受、时钟、存储与未付责任

R496 没有改变原 full-DN 接受定义。R491 已区分：程序完成不等接受；原门允许其原有限差分列，不能将全338解析 J 另增为前门。当前 H、完整原 FD、完整 residual/BC/RMS、原 fresh 末态及实际接受布尔均仍由原完整消费者判定。本文也不把预置 false 声明解释成实际数值失败。

首链沿原18900秒科学绝对钟及2700秒必要读回/关闭范围；各 phase cap 只是该绝对钟内的上限。来源生成和新注册不重置 solver 钟。原资源 reserve、CPU/线程、native 更新预算、完整列与原阈值没有在本计划中改值。原32 GiB启动自由空间检查保持。

尤其，R496 不删除原112的完整 far账本。R456/R462真实后继读取的原账本及索引仍须存在到最后真实消费者完成。已经报告的212磁盘启动资源问题不能靠本文改来源或局部省乘法自动解决；后继实际入口须如实记录存储不足/未起，并沿独立已证明的生命周期处理剩余资源。不得降低磁盘门、将大文件只有SHA冒为已可恢复，或在未来 union 仍需原值时提前删除。

原 owned PID/PGID/session/startticks、静止判断、未知子树保留、必要读回成功后条件清理均保留。完整科学 raw、统计流、生成全文及几何数据只在实际 Actions 临时目录使用；本结论只发布源码、普通源计划和紧凑研究说明，不把可重算原输出或49个展开全文重新入 Git。

## 9. 可用结论

在实际完整旧来源先重生、当前49视图正常生成并逐全文身份绑定、原环境和输入合同成立的条件下，新三层会把 R494 的真实 captured-product 变分工厂交给原 native owner，而非仅在注释中宣称使用优化。新 CP、后续 field/geometry/material 和必要统计沿同一实际 source graph 关联。

所有局部合格线性调用享有命题1的有限输出字与非有限类别结论；不合格调用执行原完整循环。原三个问题、全部模式/阶段/均值、完整科学接受门、预算以及 quiet/cleanup 责任保留。原 joint legacy/hook 的确定来源断口以实际 SHA 分派修正，数学门未迁移。

尚未支付的是本新来源链的真实编译/启动、实际资格分布、运行耗时、各级真实接受、完整几何/材料结果、全 t 与性能。未来218必须以真实 run/source/原必要读回补这些事实，不能从本 source-only 结论预填。本文本身不创建、派发或宣称完成任何科学运行。
