# 请求113：完整有限原生尾的 binary128 原始映射实验

作者：ChatGPT `/root/amplitude`，GPT-6 Astra Pro（AI-assisted）；`/root`完成原公式对照及发布。分类：独立有限数值实验的源码与接线接口。本文没有记录一次已执行的113计算，没有新的成功原生锚，也没有新的最终 Jacobian 或审计证书。

## 1. 本次要回答的问题

实际103在同一个完整新线性化上取得 R273 方向，其原129248行仿射残差读回很小，但原十档完整 noJ 非线性评价均未接受；相邻一词的完整 noJ 试探也没有改善。既有50/54只改变部分切向形成，原始 root、完整 RHS 和 RK 状态传播仍是 binary64。现有 split RHS 已经分离线性角积分，113继续保留这一数学表达式。

113从同一真实初猜重新执行原 fresh withJ 和完整 R273，只在第一次 correction 得到并核验完整方向以后暂停原回溯，做两套明确不同的 binary128 原始映射评价。每套均评价基点及原十档 alpha：1、1/2、…、1/512。随后返回原方向，继续原64位 native 流程。128读数不参与原接受判据，不代替原 residual、方向、native32×10、eta=1、tol=2e-9、最终敏感度或审计。

实际103依据见同题说明 [actual103](2026-11-15-actual103-neighbor-rejection-and-complete-R273-trials.md)。其 run=43681829913，source=301d0b6429ae273cf745fdb7fe8e4696f9786e89，job=132713895446。113不会使用失败103或95作为已接受锚。

## 2. 冻结源码及责任

| 新文件 | 字节数 | SHA256 | 责任 |
|---|---:|---|---|
| geometry_20261115_native_primal128.cpp | 23890 | 1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d | 全部 root、split RHS、226态 RK4、129248原残差行的 binary128 实验 |
| geometry_20261115_native_primal128_bridge.mjs | 12045 | 3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8 | 从实际原实例导出输入、调独立可执行文件、流式输出和临时文件回收 |
| geometry_20261115_native_primal128_probe.py | 10291 | ba3564ca6ef5329326861a66a948292280e2ab9e311eb8912c11d4e24d7d8409 | 从冻结103源按明确文本位置生成113运行时身份与观察调用，保留原 native 流程 |

接线文件为独立 workflow visible-larger-public-native-primal128.yml 和 computations/public-native-primal128-request.json；后者是唯一 push 触发路径。原103及95科学源不改。新请求完整保留原103的25项源 pin，再加这3项，共28项。原 R273 factor 源仍为9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33；原全行精确核仍为0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f。

Python只生成有新名称的运行时 adapter、QR、hook，并把完整实际文本 SHA 写入本次身份；旧源名称不会被冒充为新128模型。原 adjacent-word proposal 整段在新 hook 中关闭；旧 proposal pin仅保祖先生成源闭包，不执行该候选。

## 3. 真实输入、网格与浮点口径

本次仍临时读取实际91完整 artifact14145200674，run43672150224，sourceb78f0dd1471a118d2ed21467602509d188c2ab67，10267458B，ZIP SHA78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6。它只提供已钉的原始初猜及来源，不提供113的实际 J 或方向。初猜是failed73的BASE，而非83拒绝的trial；完整577×224状态SHA为f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6。

原78个公开源按冻结恢复器临时恢复；原配置、目标 H、target、scales、far graph、当前576个cell及所有profile均由实际构造器取得。第一次 correction 必须是真实本次 fresh withJ，随后原完整 R273产生本次delta。新packet保存原base、delta、target、577个sigma、far系数、cell.mu、portRatio、angular表和每个实际RK子步所需的几何字面值。

导出采用原 **noJ cellFlow** 的 x=k/steps、h=1/steps及原 cusp splitter。没有分裂的两点网格保留原h，不改为浮点差值 (x+h)-x；真正分裂区间按原网格相邻差构造子步。每个子步保留实际 x、x+h/2、x+h 查询所得的 r、drdx、w、w2、E。原withJ帮助函数可能采用 n*h；本接口不预称两种binary64坐标构造逐位等。单独完整原64 noJ base控制才是noJ比较口径；其maxnorm恰与freshwithJ相等也不构成全部残差数组或网格的逐字等同性证明。

运行前输出真实总RK子步数、geometry调用数、576cell逐段计数构成的schedule SHA，以及完整packet字节数/SHA。总数取自实际cell.profiles和cusp分裂，不使用576×12推算。每个cell内所有profile按原顺序执行，不省略tail端口变换。

所有角表按原Node表达式和顺序在binary64重建，再打印其实际SHA。C++将有限binary64字面值准确提升为binary128；不声称重新计算了高精度三角表或几何函数。特别地，原w、w2、E作为各自独立的binary64样本提升，不在C++中把它们替换为某个理想连续恒等式。完整实验针对该固定有限系数映射；不等同精确连续ODE，也不附带舍入误差上界。

## 4. 完整128运算范围

使用GNU __float128、libquadmath的sqrtq等，静态要求16字节存储和113位有效位，运行时要求FE_TONEAREST。它不是本平台只有64位有效位的long double。依据为GNU官方 [浮点扩展类型](https://gcc.gnu.org/onlinedocs/gcc/Floating-Types.html)、[libquadmath类型与常量](https://gcc.gnu.org/onlinedocs/libquadmath/Typedef-and-constants.html) 和 [quadmath格式化](https://gcc.gnu.org/onlinedocs/libquadmath/quadmath_005fsnprintf.html)。Actions会打印实际g++版本及可执行文件SHA，不预填编译器版本。

完整链为：节点base和delta提升；在128内形成每个base+alpha·delta；隐式动量root及其全部角积分；完整split RHS；每个RK4的四个中间态；所有226状态分量的传播；端口Pi除portRatio；cut、所有stage和far残差；原sigma归一化和最大范数。中间状态和残差不折回binary64。基点评价直接提升原base，保原signed-zero词；alpha均为准确二进制二分。

root改用未知量e=L-target，以F(e)=e+quad(target+e,Q)计算残差。这是同一有限方程的代数坐标改变，避免先形成fl(L+quad)后再减target。全部113个L分量（含mean）保留；原branch的D/S/A及projectionFloor保留。root的Gram/product-moment表达式也在128内求值，用已计算的同一角行，不重跑另一份物理场；因角表是冻结64位字面量，这里不把理想三角恒等式说成有限表下的精确恒等或新128映射的已证明精确Jacobian。

split RHS保原解析线性Fourier项和非线性角积分项，完整Q、Pi及两个mean状态一起进入RK4。每个shooting cell从其原right node开始，两个mean状态按原cellFlow初始化；结束后按原portRatio处理Pi并与left node相减。另记录所有cell的mean高度总和，但mean读数不被新增为射击残差行。

原129248行的顺序与尺度是：112个cut行；576×224个完整stage行；112个far行。stage n使用原sigma[n]，cut用sigma[0]，far用sigma[576]。每次完整评价输出原全行最大值及其行号、带符号原残差，既非仅四行，也非仅stage10。

## 5. 两个root停止配置必须区分

| 配置 | 普通停止 | 原回溯不接受时的fallback | 内部上限 |
|---|---|---|---|
| binary128-e-original-inner-stop | 原binary64字面8e-14准确提升 | 原binary64字面5e-12准确提升 | 原30次Newton、每次20档 |
| binary128-e-refined-inner-stop | binary128十进制1e-28 | binary128十进制5e-27 | 同30×20 |

scale保原target幅度、当前quad幅度及原1e-300底数。两套都遵守真实D/S/A域与原内部严格下降或达到对应stop的回溯。后者是明确另列的严格root精化算法配置，不能把其结果改名为前者原映射。

每套均记录root调用、角评价、Newton步、回溯trial、fallback、最大迭代、返回相对残差，以及第一次达到原8e-14阈值时的读数。全合法root评价上的minD/S/A和真正返回给RHS的root上的minD/S/A分列；不把试探域最小值冒充最终返回轨迹域最小值。域失败/非SPD/iteration-limit等保持明确实际错误。

顺序固定为两个base，然后同alpha的两套配置，再下一个alpha：最多22次完整评价。每次完整129248行评价完成立即输出，不等待22次全部完成。某套base不完整时，该套后续“相对base严格下降”字段为null，不能以未完成base推断下降。

## 6. 原64控制与接受责任

packet形成后，额外调用一次原args.evaluate(states,target,false,scales)，保存完整noJ base的原norm、stage/far数组SHA及真实失败信息。这个调用不选择新方向、不消耗原十档trial、不改变原state。原noJ evaluate本身不追踪minA/minD，输出明确这一范围，不捏造相应域数字。

实验完成、部分完成或错误以后，hook仍把**同一个已核验的完整本次R273 delta**返回原流程。两套128结果不会替换该delta，也不会设置原native accepted。原32次外迭代、每次10档、eta=1、原2e-9、原domain、原final sensitivity及final audit仍由冻结流程决定。原主native如失败，顶层仍如实非零退出；128部分完成不另作为一个新的native否决门。

原64 J只对原有限实现给出方向。它不是两套128映射的已付一致Jacobian；113也未实现128最终Jacobian或audit。即使某128全行范数较小或低于2e-9，也只是一项实验读数，不能直接称完整native已接受、得到真新H/J、可给fullDN当live锚或获得闭面幅度结论。

## 7. 超时链与成本范围

| 层级 | 本次实际设置/源码行为 | 范围 |
|---|---|---|
| C++128子进程 | 7200秒，原root/角循环定期检查 | 从子进程内deadline建立开始，包含packet读取及两配置评价 |
| JS对C++的硬超时 | 7200+120秒 | 额外120秒只容纳协作退出/工程异常，不增加数值评价次数 |
| packet导出、额外64base | 子进程7200之外的额外实验墙钟 | 不从原native32×10次数扣除；纳入外层step/job总时间 |
| 原Python TailClient | ready和response为阻塞stdout.readline | 没有另一个短in-flight请求deadline |
| 原client.close | wait15秒，必要时terminate/kill | 只在返回/错误后的退出清理，不是运行中native超时 |
| 原R273 child | 原spawnSync，无新短timeout | 方向数学及其原预算未改 |
| 原rules runner | 每2700秒同步规则 | 无固定science lifetime；真实README变化仍按原责任终止进程组 |
| Actions科学step / job | 320分钟 / 350分钟 | 统筹初freshJ/R273、导出、额外64base、128实验、原后续trial及清理 |

7200秒不是整个请求的唯一墙钟。任何有限Actions时限都不保证原最大32×10一定能跑完；全局超时或规则变更停机只可记为未完成，不可冒成原科学门拒绝。子进程自身到期会打印实际完成的行/阶段、已完成评价和budget标志，原64控制仍恢复执行。CPP异常或硬终止也不替换原delta；外壳先记录错误，再沿原流程继续。没有为了这次实验缩小原十档或原迭代上限。

二线程仅并行相互独立的576个stage；每个stage内部角循环和RK顺序固定。尚无实际113子步数或单次完整128耗时，因此不宣称7200秒必能完成22次。粗估耗时或仅少数成功stage不能代替完整评价。

## 8. 输出、清理和可重跑范围

stdout采用NATIVE113紧凑事件：实际输入/源/packet/SHA与子步计划；binary128实现；每次全行评价；各临时完整残差SHA；实验返回摘要；随后原64每档trial和最终原响应摘要。128范数和最坏残差用36位十进制字符串与十六进制Q格式，避免JSON Number回落到53位。

部分评价没有全范数：norm为null，报告完整行数、实际完成行数、所有失败stage索引及前8个详细错误；不得称前8个是全部失败。临时残差向量完整保留未算行的NaN字节，实际读回SHA后删除。所有input、schedule、full residual、snapshot、QR factor、checkpoint只在本job自己的RUNNER_TEMP生命周期中存在，不上传Git、Release或新artifact。

当前完整方向先读入内存、身份核完，再临时做128；实验的独立mkdtemp仅在子进程返回和摘要/数组SHA消费后删除。原correction目录的删除仍在原103finally。原outer driver后续只消费已在内存的direction/记录和顶层native最终响应；不重新打开已消费的snapshot/QR文件。最后原client关闭、原response/result/trials读完并打印紧凑结果后，才清理本次原native输出。源文件生成后实际SHA绑定，结束只删除本次生成且hash相符的文件。

可重跑责任由冻结source、输入artifact tuple、request参数、真实run、编译器/可执行文件SHA及完整输出SHA承担。哈希不是128误差界；原raw不保留也不冒称已有独立后续原字节复核。最终若原64意外接受，stdout摘要仍不是持久live锚，本请求没有为fullDN保留成功worker实例。

## 9. Actions接线与本地完成范围

新增CLI：--quad-executable（本run临时编译路径）、--quad-budget-seconds7200、--quad-threads2；其余沿原103：--original91-directory、--source-topic、--eta1、--node-heap6144、--exact-workers2、--max-factor-bytes2147483648、--out。Python3.12.14、Node24.22.1、numpy2.3.5、scipy1.17.0保持原方向和reader环境。

编译采用g++，-O3、-std=gnu++17、-fopenmp、-fno-fast-math、-ffp-contract=off、-frounding-math、-lquadmath；实际可执行文件只在public Actions运行。原规则runner3b8不改，仅注入当前已读两个README全文及blob；每45分钟同步、规则变更停止、唯一HANDOFF规则行均保留。git merge.stat=false仅避免普通pull输出读取已删除的历史raw，不是科学门。

本地只完成文件字节/SHA、文本生成、Python AST、Node --check、C++ -fsyntax-only、workflow shell与inline Python语法核。未导入或执行原科学模块、未运行C++评价、未使用新fixture。新旧workflow/request差异可从已提交源直接重得，静态回执仅临时保留，不作为可重算输出提交Git或Release；没有未来run或accepted结果。根主控独占最终Git发布和Actions调度。
