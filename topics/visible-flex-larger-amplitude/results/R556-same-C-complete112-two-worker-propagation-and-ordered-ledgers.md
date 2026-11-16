# R556：同一准确 C 的完整112模式两进程传播与有序账本归并

**可信度：已证明（限本文列明的同源输入、原有限算术语义、完整流传输和实际事务条件）；尚无此并行源的科学执行、数值完成或加速证据。**

作者：OpenAI / ChatGPT exact_refinement agent（AI）。日期：2026-11-16。

本文交付一个实际调用原传播函数的 helper 和一个明确的新 sampler 源视图。它替换原 serial mode loop，保留原完整112深端族、所有物理远点 inverse fragments、实角 lift、正幅度、逐候选单位行及原 momentum 消费。它不改变已运行入口，不产生新 root 选择，也不把两个子进程各自变成一份新的25M工作预算或新的传播时钟。

## 556.1 已有对象与本次实际改变

原 sampler 为 geometry_20261116_current_C_joint_gzip_radial_sampling.py 的真实生成字节：71361 B，SHA256 21032e3c4fef44b022a7d91394ff0269dcfd3f94f8ee1a9cab9a0696b2530eb6。该 basename 是 R498 源计划的 Actions 输出，不因本文链接而成为预先存在的 Git 文件。原未压缩来源、原 gzip 存储核和全部祖先仍按原来源生成。

本次 helper 为 [geometry_20261116_current_C_two_worker_far_propagation.py](../computations/geometry_20261116_current_C_two_worker_far_propagation.py)，50793 B / 563022ef9b22ef547ebb800d0689ef4530345f5a728216f47b2239cb1c3eb5c8。

[单视图计划](../notes/r556-current-C-two-worker-complete112-source-plan.json) 为9553 B / 2373f6d3e574f8730a751b84cba2c83c73ff98b8100e0c114414c1adc8e7b9a8。它复用原 R496 的正常文字生成器 root_20261116_current_C_zero_linear_source_views.py（11895 B / 4d4c507edd571b67655fd2e66fb4bcfa173b1239928443831a81a925c4869ec4），由11个完整 literal 改动生成：

geometry_20261116_current_C_two_worker_joint_gzip_radial_sampling.py，73294 B / c90137cdb2da1159338838a68c04156dc24046d306798c1cada8da85df624f69。

新 sampler schema 是 R556-current-C-two-worker-joint-physical-radial-samples-and-general-far-v1。原 native geometry bundle schema 保留 current-C-native-radial-geometry-bundle-v1；这不免除后继消费者对新 sampler 来源的真实注册。

没有修改的实际数学核如下。

| 对象 | 完整来源 SHA256 | 本次用途 |
|---|---|---|
| 原同C全源与 scalar runtime f12f | f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df | 同一原 C、全部原分支、Piece.range、原 Journal |
| 正端点实角传播 c2f | c2f515aa276890da63871fe0e9e1440775950d4985465457e9d6025976d914c8 | initial_column、GeometryCache、advance_candidate、原完整 pending |
| 正端点运算 | 91dd207bc20a87a36e2d4bc13e1b88a14333b67cf47ec048f85e8d46500822ff | 原正性条件和完整 log、sqrt、倒数外包 |
| 联合数值代表形成 | 24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97 | 全112合法后原 momentum_rows 调用 |
| 完整 JSONL gzip 核 | d07d1844aaf54b5aaea550a1c0d8aea63b9306f9ce44f66bd0b1e18aa3e40089 | 每完整原行一个 gzip member；stored/decoded分账 |

R380证明仍按原 kernel 的8a51036fd130c80365284c2e4678c3aa765d177471b4d16df0f4c85add016fa9绑定；R312深端族及R357原取向单位行证明仍由原 load_runtime/bind_inputs 核对。本文只证明新的有限调度、输入传递和账本重定位，不重证这些原方程。

## 556.2 真正独立的是各 mode 的求值，不是准确根族

设 $\Omega$ 为原四件 C 输入、原 query/cut 与完整深端构造共同允许的准确函数族。令 $r_F$ 是原 InverseSampler 实际选定的 binary64 物理坐标字，$\mu_F$ 是原程序先求同一次 far sample，再由原表达式产生的正 binary64 坐标字。本文保持它们的实际字词，不由静态配置重猜 $\mu_F$。

对每个 $m\in\{2,4,\ldots,224\}$，原 point_column 使用：

1. 该 mode 的完整 far row，经 F.initial_column 形成原 R312 全盒；
2. 同一个 head、原全部 source panels、同一个 required prefix；
3. 同一个 far inverse leaf 关联 by_panel；
4. 同一个 $r_F,\mu_F$ 及原精度、Taylor项数、depth、norm/defect工作参数。

函数在每次调用内部创建自己的 state、stack、coverage、unit_hull、首合法 nominal seed、accepted计数与事务状态。进入下一个 mode 不读取前一 mode 的这些数值量。m 的作用在原平衡系数、角方程和物理行公式内，未通过另一 mode 的返回值传播。

唯一原跨 mode 数值缓存是 GeometryCache。其 key 为原 panel row 和准确有理端点 $(\ell,h)$。get 的返回由该 panel、Piece.range、原两 primitive endpoint 外包和同一正 radial speed 外包确定。base_speed 同样只是同一 whole-panel表达式的 memo；Piece.range 只枚举原可能分支并求原表达式，没有按已完成 mode 改写准确目标或 scalar 参数。

因此每个 worker 使用独立缓存、甚至因容量导致相同 key 重算，只改变 cache hits、coefficient ledger 的重复行、时间和来源地址；在同一有限运行时与相同上下文下，不把数值定义换成另一条方程。新两缓存保留数之和不超过原 max_geometry_cache_records；父进程在开始时只清自己的 coefficient LRU memo，已写原系数账本和原 far sample仍保留。

这里不假定 $\Omega$ 是各 mode 根族的直积。对任意同一个 $\omega\in\Omega$，原传播给出相应行 $\mathcal R_m(\omega)$，各 mode 包围 $\mathcal U_m$ 满足

$$
\forall\omega\in\Omega\quad
\bigl(\mathcal R_2(\omega),\ldots,\mathcal R_{224}(\omega)\bigr)
\in\prod_{m=2,4,\ldots,224}\mathcal U_m.
\tag{556.1}
$$

逐 mode 独立求包围只保守地丢失相关性，不把每个 mode 的不同 nominal 参数点宣称为同一个准确 $\omega$。原 sampler 的 exact_global_C_realization_of_numeric_representatives_certified=false 完整保留。

## 556.3 逐 mode 有限程序不变的条件归纳

固定同一个 mode，比较原调用与新 worker 内调用。假设它们在某步拥有相同的完整 state、stack、coverage，以及相同实际 scalar 运行时和上下文。

原 budget.attempt 只决定是否还获准继续；若两者均获准，则 pop得到相同准确闭段。GeometryCache取得相同数学系数盒；原 advance_candidate 顺序、positive endpoint公式、同角关系、Taylor余项、norm/barrier/defect分支完全不改。因此两者形成相同的下一分裂或候选传播值。

若该步分裂，两者在相同次序追加左右子段；若提交，两者执行相同 prepare_far_tubes、逐候选单位化、完整coverage更新、原unit hull次序和首候选seed选择。只有 ledger地址及依赖这些地址的 canonical SHA可能不同。初值相同，故归纳覆盖每个共同获准执行的有限步骤。

此结论以实际相同有限库语义为条件，不是对新运行作逐词比对的验收门。它不保证原 serial 与 parallel 在相同墙钟/总工作限额下恰好完成相同的 mode集合：两个 mode 的预算请求交错，cache miss次数、搬运工作和停止时刻也改变。新真实输出必须报告自己的实际进展，不可回填旧run。

R380的完整实角lift、正幅度、二幂换帧、所有候选和原取向来自未改函数；不通过 principal angle、删候选、缩根族或改 strict positivity换取并行完成。

## 556.4 一份原工作限额和一只原传播时钟

父 sampler 在原位置创建 OwnedBudget，保存原 started、seconds、limit、reserve。helper只引用这些实际值。共享 admission state含一个 work counter $W$，每个原 budget.attempt 在同一个文件锁保护下执行：

$$
W<L\ \Longrightarrow\ W\leftarrow W+1,
\qquad
W\ge L\ \Longrightarrow\ \text{原工作资源停止}.
\tag{556.2}
$$

初始 $W=0$。每次递增由同一个排他锁串行化，故任意执行前缀均有

$$
0\le W\le L.
\tag{556.3}
$$

它不是两个各自有 $L$ 次的局部预算，也不在开始下一波或另一 mode时重置。实际原请求若给25M，则全部112模式、两worker合计最多25M次原attempt；本文不另改这个数。

同一状态还记录check数、原disk观测和首个资源停止。每个进程分别打开同一个 flock 文件，避免继承同一 open-file-description造成假互斥。锁随进程退出由内核释放，不留下一个已死进程持有的 Python semaphore。

全部科学、传输和原序合并检查都使用父原 started和seconds。fork、子进程登记、必要字节传输、gzip重编码、SHA重定位和fsync也处于该传播阶段经过时间内。父在一波合并后再次检查原时钟。退出收尾没有新科学许可；5/10秒的合作退出及SIGTERM/SIGKILL等待只用于回收已创建子进程，不能再推进原point_column。

原采样阶段暂停传播时间的逻辑保持：只有实际linear.elapsed被原 sampling.started平移扣除；之前已用采样时间仍计入其自身预算。外层同job绝对截止钟和其预留不重启。helper不以新的局部时间重新打开已耗尽的阶段。

若一个 mode返回传播未付，记录实际原错误并请求已启动同伴停止。同伴因这一请求返回的 scope是资源/调度未完成，不冒另一个独立数学反证。对已形成数据的必要返回可忽略peer取消，但仍受原时间和真实存储限额约束。

## 556.5 显式上下文与内部 Arb球的准确传输

原 B.initialise_math明确绑定 python-flint==0.9.0并设置ctx.prec。父捕获这一实际prec以及存在的threads/cap/pretty/unicode值，每个worker在调用原point_column之前显式设置；不靠fork默认状态或新进程默认精度。c2f和正端点helper的该传播路径没有另改ctx.prec。

所有跨进程的最终单位行内部区间用

$$
(m,r)=(a\,2^e,\ b\,2^f)
\tag{556.4}
$$

的两个确切整数/指数对传输。a、b以完整整数文字保存，不先转float；e、f为完整整数。这里m来自原ball.mid().man_exp()，r来自rad().man_exp()。

python-flint0.9.0的arb tuple接口先将mid tuple设为准确arf，再由radius tuple设mag。原r本就是该mag格式可表示的值，因此回装保留原mid和rad；没有用lower/upper再union成另一只较宽球，没有十进制转换损失，也没有把两个独立中心当作非零代表行。依据为该版本src/flint/types/arb.pyx中的arb_set_python、arb.__init__、mid、rad、man_exp真实实现。

父只有在原返回row.complete为真时才恢复两只完整单位行球。未complete时保full_interval_objects=None及原完整/部分hull字段，不把合法子集提升成全族。所有候选的原外包与first committed nominal seed仍在原mode record/账本内。

## 556.6 六条完整原流的有序重定位

每个worker只写自己的完整六流：

coefficient-boxes、far-accepted-panels、far-complete-tubes、far-panel-commits、far-inverse-leaf-coverage、complete-unpaid-scope。

第k个mode合并前，令某流s已有全局行数为 $o_{k,s}$。该mode的本地行j按原顺序写到

$$
\iota_{k,s}(j)=o_{k,s}+j.
\tag{556.5}
$$

映射在本地行集上严格递增。完整半开span $[a,b)$映为 $[o+a,o+b)$，故行数、空span、未提交尾和原相邻顺序都保持。

源码只重定位明确具名的地址，不对任意整数做猜测：

| 字段 | 加的流偏移 |
|---|---|
| coefficient_row，包括seed内同名地址 | coefficient-boxes |
| prepared_panel_row | far-accepted-panels |
| panel_commit_row | far-panel-commits |
| complete_step_rows、uncommitted_written_step_span | far-accepted-panels |
| complete_far_tube_rows、committed_far_tube_rows、uncommitted_written_far_span、prepared_far_rows、far_contribution_span | far-complete-tubes |
| complete_panel_commit_rows | far-panel-commits |
| complete_far_leaf_coverage_rows、complete_original_leaf_coverage_rows | far-inverse-leaf-coverage |

原source panel row、source piece、possible leaf row、transaction_index、mode index、准确有理端点、完整角/幅度值以及因子数学链hash均不平移。它们不是此本地账本的地址。

最大的prepared-panel流只对原canonical行中唯一的coefficient_row整数token作替换。其余字节不解析重排；每行仍完整保留。其它较小流解析其原canonical JSON，按上表保全重写，未列字段和值完整返回。原canonical已禁止NaN，完整整数不经binary64转换，原null、布尔、字符串及实际binary64数词语义保留。

prepared-panel内容中的地址变化会改变其canonical SHA。因此同时形成每个原prepared row的旧SHA/新SHA对；原commit引用必须与相应旧SHA相同，写入全局commit时替换为新SHA。这个核验是实际字节传输关系，不是新增的数值对拍或数学接受门。原outgoing factor-chain SHA不含此ledger地址，不作改写。

每个私有流的原stored bytes/SHA、decoded bytes/SHA、行数均完整读到EOF核回后，才能称该流传输complete。gzip使用原level1，mtime0；global stored和decoded分别计算，不能拿原私有compressed SHA替代重定位后的全局SHA。私有流原身份仍在mode result及全局transfer receipt中保留。

原全局编码器“canonical bytes不改写”的scope是已完成显式重定位之后、交给gzip的本次canonical行；新descriptor明示这点，不声称worker本地canonical字节或本地索引未改变。

## 556.7 两层事务与有界临时payload

原point_column的panel事务正文不动：prepared step与far tubes先写，commit最后写，然后才安装下一state/coverage/hull。异步signal handler只置flag，不在该短提交段抛出异常。原未提交step/tube span、transaction_open、pending stack和last unaccepted全部保留。

外层新增“完整mode传输”事务：

1. 实际worker退出并由父join/reap；随后才读它的mode result与完整流。
2. 六条流按原流序、原行序搬运；所有原stored/decoded身份核回。
3. 全局六流flush/fsync，形成完整偏移、span和prepared SHA索引身份。
4. 写原far-all-mode-rows中的该mode记录并fsync。
5. 写独立global-mode-transfer-commit，绑定完整mode result、实际偏移、全局mode行及其canonical SHA。
6. 只有该commit成功，才将row追加到父的实际rows列表，并退休私有冗余payload。

若第4步后第5步失败，原mode行可能已经在文件中，但缺实际全局commit；父rows不包含它，不能成为完整112输入。其所有私有源、实际已写全局span和原错误仍保留。完整传输partial mode也不使它的科学complete flag转真。

每波恰有至多两个mode私有payload。下一波只在本波处理后启动。完整commit后才删除本地六流及64-byte-per-prepared-row重定位索引；小mode结果、所有权、原private stored/decoded身份和全局commit仍保留。若任何本地payload退休失败，停止开启下一波，保持已全局提交的数学结果及实际错误，不累积无限波冗余原件。

本上界是“最多两个mode payload”，不是每个mode的字节上界。一个mode本身可能很大，原free-bytes reserve及实际I/O失败仍负责。全局完整账本从未因并行被删短或换为身份-only；失败、未合并及未知存活的私有payload也不退休。

## 556.8 真实进程所有权、失败和未访范围

helper只在原公开仓库Actions/Linux fork环境执行。两个worker不另建session或process group，必须保父的实际ppid/pgid/sid。父保存pid、startticks、pgid、sid后才通过私有gate允许进入原point_column；worker另写真实child identity和scientific-entry边界。

未成功登记的child在可轮询gate等待，仍检查原共享时钟/取消flag，不会无限阻塞着等一个已失败的父登记。父的异常收尾先用实际multiprocessing child handle作join；发送signal前仍核该已登记pid/startticks/pgid/sid。不可读、重用或不匹配的identity保unknown，不向未知进程发送signal，不把未知解释为quiet。

worker只close自己继承的父journal和不使用的pipe端；不写父尚开放的流。父合并之前所有本波孩子必须实际reaped。未知quiet使helper抛出原WorkStop类并保未付，不继续数值row/native路径。外层原owned进程组与cleanup合同仍需在完整入口真实核查；本helper不会删除namespace或给予新的清理授权。

结果分列：

- 实际fork成功的mode；
- 由完整mode返回元数据确认到达科学入口的mode，未确认不冒“未进入”；
- 原序global commit完成的mode；
- 已启动但未global commit的mode；
- 从未fork成功的完整后缀；
- 每个原返回错误、完整pending/current state/未提交span和实际传输错误。

当子进程硬退出而原mode result未返，不能恢复它未提交的状态。原private路径和已形成identity/实际退出明确保留；不得以邻mode成功补上此mode。所有这些字段也不是“全部112已完成”的替代。

## 556.9 原全部112数值消费者仍为原函数

新sampler在原serial loop位置调用run_modes。返回后仍执行原条件：

$$
\#\mathrm{rows}=112
\quad\text{且}\quad
\bigwedge_{m=2,4,\ldots,224}\mathrm{row}_m.\mathrm{complete}.
\tag{556.6}
$$

还须没有实际helper/预算记录错误，并已证明孩子quiet。该条件满足后，原momentum_rows、原联合nominal选择、全部family到实际word误差、112×224 far矩阵、577节点和576stage的物理采样全部按原代码继续。本次没有选择一个成功子集、补零余模式或把full propagation与unit-row complete合并成一个宽泛标签。

若某mode原传播完整而unit-row norm未付，原函数保完整传播族与候选信息；这不许可native启用。若全部112族已合法，而后nominal代表、采样或native配置失败，必须按其真实阶段记录，不能倒填为传播失败。

新sampling/schema/source必须由后继完整caller显式登记。本文单view不替换所有旧source白名单，不宣称目前235、R456、R464 union、动态M或闭面/evidence消费者已经接受此新tuple。后继R557应保完整原来源闭包并登记真实helper/sampler/reader字段；它不是新的科学通过门。

## 556.10 组合定理与当前未付范围

**命题556.1（同族包含与有限程序组合）。** 假设实际输入满足原sampler全部同C/deep/物理远点条件；新worker用同一输入对象与明确相同算术上下文；原完整模式函数正确；本次返回的每个全局mode都有完整传输commit；相关原byte/hash/地址映射成立。则每个标成complete的全局mode包围原同一个准确C族的相应全部物理行。若(556.6)、无实际caller/预算错误与真实quiet均满足，传给原momentum_rows的mode数组保持原mode顺序、完整候选族及内部Arb单位行语义；本文没有新增任何数学root选择。

证明由556.2的共同$\omega$量词、556.3逐步归纳、556.5区间对象准确传输以及556.6—556.7完整事务组合得到。式(556.2)—(556.3)同时保证一次原全局attempt限额；各次check与原started保证没有为并行重开传播钟。未complete或未commit不满足定理前提，保其原scope即可，不作成功推断。

历史actual222/R511记录了原112传播的实际耗时6124.8677721839995秒和2044754次attempt。该记录只是明确本次优化面对的真实工作，不是新parallel性能证据。其大gzip账本还说明完整传输、解压/重压与磁盘空间是实际成本；两worker不必然减半总耗时。当前没有运行本源、没有读取任何新科学结果、没有证明某个更短wall cap足够。

本次不支付全局准确C实现性、完整BVP/native成功、closed-field metric误差、后续mesh/M/t收敛或机器精度floor。原根族、cut、112行、所有后续科学门和单90KB必要传输边界继续各自负责。完整入口若在原资源内未到某阶段，必须保该未起后缀，不能从本条件证明预填。

