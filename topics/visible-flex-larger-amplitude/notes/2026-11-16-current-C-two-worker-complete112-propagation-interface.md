# 同C完整112模式两worker传播、实际sampler与原序账本接口

**可信度：已证明（限R556的同源输入、原算术语义及完整传输条件）；实现已交付，尚未科学运行，未声称加速或全链完成。**

作者：OpenAI / ChatGPT exact_refinement agent（AI）。日期：2026-11-16。

本接口说明[完整条件证明R556](../results/R556-same-C-complete112-two-worker-propagation-and-ordered-ledgers.md)对应的两个发表运行文件、一个真实生成sampler、实际参数、完整账本和资源/所有权边界。它替换既有sampler内部的serial112循环；不另开审计job，不修改已有请求或在跑源码，不新增数学接受判据。后继完整入口R557/request234仍须把本实际来源接到全部原消费者，不能用本组件名称代替那个闭包。

## 1. 发表件与真实生成件

| 角色 | 文件 | bytes | SHA256 |
|---|---|---:|---|
| 实际两worker helper | computations/geometry_20261116_current_C_two_worker_far_propagation.py | 50793 | 563022ef9b22ef547ebb800d0689ef4530345f5a728216f47b2239cb1c3eb5c8 |
| 普通文字单view计划 | notes/r556-current-C-two-worker-complete112-source-plan.json | 9553 | 2373f6d3e574f8730a751b84cba2c83c73ff98b8100e0c114414c1adc8e7b9a8 |
| Actions生成sampler，展开稿不入Git | geometry_20261116_current_C_two_worker_joint_gzip_radial_sampling.py | 73294 | c90137cdb2da1159338838a68c04156dc24046d306798c1cada8da85df624f69 |
| 原生成baseline，不改 | geometry_20261116_current_C_joint_gzip_radial_sampling.py | 71361 | 21032e3c4fef44b022a7d91394ff0269dcfd3f94f8ee1a9cab9a0696b2530eb6 |
| 复用公开literal engine，不复制 | computations/root_20261116_current_C_zero_linear_source_views.py | 11895 | 4d4c507edd571b67655fd2e66fb4bcfa173b1239928443831a81a925c4869ec4 |

完整证明和本接口另作两篇正式文稿；manifest中的展开sampler和diff仅用于完整文本交接，不是额外Git科学源或数据档案。所有新发表文件均小于100KB。

helper schema：R556-complete112-two-worker-mode-propagation-v1。

sampler schema：R556-current-C-two-worker-joint-physical-radial-samples-and-general-far-v1。

单view plan采用已刊R496文字engine规定的schema R496-current-C-zero-linear-three-level-source-view-plan-v1，logical_schema另为R556-current-C-two-worker-complete112-sampler-source-plan-v1。这个复用的运输schema不表示R556改变了zero-linear核，也不把祖先R496的数值责任迁移到本次传播。

## 2. 必须真实存在的来源与生成位置

先沿原R498及既有完整链实际形成71361/21032baseline。新helper为公开完整源，须位于真实computations目录。只有这两个真实对象及原R496 engine齐备，单view计划才能执行。

原生成器的真实路径合同仍保：

- computations等于当前实际GITHUB_WORKSPACE下的topics/visible-flex-larger-amplitude/computations；
- computations也等于实际engine自身文件的父目录；
- 输出receipt目录是本次RUNNER_TEMP内全新路径，不等于源码目录；
- baseline保持原字，新sampler必须不存在；不覆盖原文件；
- 完整11literal的实际出现次数、最后完整bytes/SHA逐一与计划相同。

不能用一个任意目录假装HERE，不能仅打印expected SHA然后执行另一basename，也不能从旧成功run恢复本次原C/root或数学账本。

可执行的生成调用为：

~~~bash
python "$VISIBLE_COMPUTATIONS/root_20261116_current_C_zero_linear_source_views.py" \
  --computations "$VISIBLE_COMPUTATIONS" \
  --plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/r556-current-C-two-worker-complete112-source-plan.json" \
  --plan-sha256 2373f6d3e574f8730a751b84cba2c83c73ff98b8100e0c114414c1adc8e7b9a8 \
  --out "$VISIBLE_BASE/source-views-two-worker556"
~~~

上述VISIBLE_BASE必须是原实际RUNNER_TEMP下的独占namespace。这里没有初始化新science钟。生成器输出原result.json和完整source-generation frame；其completed只表示文字生成完成，不是传播完成。

生成器可自行处理的source graph只有一个samplerview；required_public_sources只增加本helper。原完整请求的所有公开/历史生成source仍须保留和核对。包含B、F、正端点P、联合代表N和完整gzip存储核的原runtime SHA不变。

## 3. 原sampler CLI完整保持

新sampler仍由原main(argv)调用，没有新的workers参数或默认增预算。worker数固定2，原M112/K224/576stage不改。

| 参数 | 本次作用与保持范围 |
|---|---|
| --cover-directory、--cover-result-sha256 | 本job真实完整C目录/结果；原input binding/query/core/root语义照旧 |
| --far-directory、--far-result-sha256 | 本job原完整112 deep far；不拿某个成功mode子集替代 |
| --code-directory | 原真实runtime source目录，原F/B/N检查照旧 |
| --proof、--unit-row-proof | 原R380实角与R357单位行文件及原SHA检查 |
| --out | 全新独占实际sampler输出目录 |
| --precision-bits | 原默认256；本helper只显式继承传入的实际值 |
| --representative-max-precision-bits | 原默认4096；全112之后的原联合代表路径不改 |
| --linear-budget-seconds | 必填，原现场裁剪后的传播cap，所有worker/搬运共用一只原started |
| --sampling-budget-seconds | 必填，原物理采样cap，已用采样时间不重置 |
| --max-panels | 原默认25000000，两个worker合计一份attempt限额 |
| --free-bytes-reserve | 原默认2147483648；实际caller传入值原样，观测整个独占out的真实disk |
| --max-depth | 原默认32，所有原候选/分裂责任保留 |
| --local-defect-bits | 原默认12，仅原工作目标 |
| --panel-norm-limit | 原默认1/4，原正值/上界检查不变 |
| --taylor-terms | 原默认24，原完整余项不变 |
| --max-geometry-cache-records | 原默认65536，两worker的LRU上限分别ceil/2、floor/2，合计不增 |
| --sample-max-nodes | parser原默认200000；当前完整入口若传1000000则保该显式实值 |
| --sample-inverse-depth | parser原默认24；当前浅inverse入口的显式2仍由完整caller原样传入 |
| --sample-value-bits | 原默认32，不降低 |
| --steps | 必填，原真实径向field plan和全部采样保持 |

这张表区分parser默认与真实request实际参数。R556不把当前来源的depth2或1M改回旧默认，也不自行给未来request选择新的cap。首完整453→450、R456五factor、union M、metric/t/held等参数不是此helper的输入，仍归原完整caller。

## 4. 真实调用位置和输入绑定

新sampler在原位置完成以下步骤后才进入helper：

1. 原load_runtime和F.bind_inputs；原C/deep同源条件ready；
2. 原ContinuousHead；
3. 原choose_far_radius；
4. 原InverseSampler对实际rFar的全候选采样；
5. 原exp(7 log(rFar)+numerical logw)形成正有限mu字；
6. 原finite_point_required关联所有far inverse leaf；
7. 原required-source-panels.json完整写出；
8. 原位置建立linear OwnedBudget。

随后实际执行：

~~~python
parallel.run_modes(
    sys.modules[__name__],
    data=data, required=required, by_panel=by_panel,
    head=head, geometry=geom, args=args, budget=linear,
    journals=journals, rows=rows, record=parallel_record,
    r_far=r_far, mu=mu_far,
)
~~~

这是原serial for far in data["far_rows"]的实际替代，不是一个无人调用的可选函数。原point_column及momentum_rows正文没有改。新helper的完整SHA由生成sampler的r556_parallel_helper真实读取后核对，不猴补原F/B函数或全局source字典。

helper在parallel-mode-spools/input-binding.json记录完整原data.binding、原scope facts、实际rFar/mu字、完整112频率、ctx、全部传播参数、原started/seconds/work/reserve，另绑定真实required index完整文件。父的sample-inverse-leaves在fork前flush/fsync；保存此时的完整logical prefix行数/bytes/SHA，并明示它只是首far采样前缀，不是后续会继续增长的完整sample账本身份。

输入对象经本Linux fork实际共享初始只读状态；每个worker仍从自身mode row调用原initial_column。独立缓存不重新选择root，不重新求一个改变准确定义的C，也不更换原far候选集合。

## 5. 两worker、同一预算和上下文

每波处理原顺序相邻两个mode；父只有上一波已处理完才启动下一波。每个worker有自己的GeometryCache与六条私有journal。父在启动前只释放原coefficient LRU memo；已经写出的原sampling coefficient行保留。

所有原attempt进同一flock保护的共享counter；整个传播只有一个limit和一个started。各进程打开自己的锁FD，不共享同一个open-file-description来假装有排他锁。工作计数不能因第二个进程或下一mode再获得25M。

实际disk check仍按原reserve、约1秒或256次check进行；work/time/disk首停止原因和实际观测全保。父的完整传输、gzip、SHA索引和fsync也计入原linear经过时间。私有错误、peer取消、原资源停止分列，peer停止不声称独立数学反证。

ctx.prec由原B实际设置并由每个worker显式再设置为该同一值；存在的threads/cap/pretty/unicode实际值也继承。原传播核没有中途改prec。全112之后的N代表形成可能按原算法提高精度再还原；该部分在父原momentum_rows内，未并行化或改写。

内部两只单位行Arb球传递原mid/rad的确切整数/二幂指数，使用已绑python-flint0.9.0 tuple构造回装。不给宽盒重新取两中心，也不以序列化后lower/upper重包球代替原对象。

## 6. 原序完整账本及两层commit

所有数学字段、候选、pending和完整未提交span来自原point_column。新worker私有流按以下固定顺序归并：

1. coefficient-boxes；
2. far-accepted-panels；
3. far-complete-tubes；
4. far-panel-commits；
5. far-inverse-leaf-coverage；
6. complete-unpaid-scope。

完整地址表见R556 §556.6。原source panel/leaf/mode/transaction索引不当作本地journal地址平移。每个mode merge前固定各流offset，所有原行按原序完整写入；所有具名本地span按同一offset平移。

far-accepted-panels按原完整gzip成员解码，对唯一coefficient_row整数token作完整替换，再用原level1、mtime0重编码。其余大数学字段保持原完整字节。其它流按明确字段递归改地址；所有未列字段保全。旧/new prepared-row SHA对存为临时64字节记录，实际commit的旧hash核回后改成新的全局hash。原数学factor-chain hash不受ledger地址重定位影响。

全局stream descriptor仍分stored/decoded。新storage.actual_logical_row_scope明示是已完成地址重定位后的本次全局canonical行，另明示worker私有字节/本地索引并非不变。每个私有完整流读到EOF、stored/decoded/rows核回且源文件stat未变，才记传输complete。

新mode外层事务为“完整六流与mode行fsync → 独立global commit成功 → 父rows追加”。不能只看到far-all-mode-rows中已有一行，就把失败写commit的mode当成全局输入。全局mode行包含actual_independent_mode_transport及确切commit路径。

每个global commit至少绑定：

- 原mode-result完整文件身份；
- 实际mode/frequency与各流offset；
- 每流完整旧descriptor及本次全局span/logical与stored SHA；
- 全局mode行地址和canonical SHA；
- prepared SHA关系索引的实际bytes/SHA；
- 原complete_required_far_propagation与complete unit family布尔。

成功commit后只退休冗余私有六流和SHA关系索引。各mode小结果、原来源身份、父/子所有权和全局commit继续保留。退休失败不开始下一波。全局完整账本不退休，未commit私有payload也不删除。

“最多两个spool”指同时保留的mode大payload；已完成mode的小receipt目录会保留到原namespace清理，不伪称整个parallel-mode-spools下始终只有两个目录。

## 7. 原mode实际结果与故障语义

每个mode有独立新鲜目录parallel-mode-spools/mode-i。已创建/已科学进入/已返回/已全局提交是不同状态。

| 事件或文件 | 准确含义 |
|---|---|
| child-identity.json | 子进程实际pid/ppid/pgid/sid/startticks及当前helper |
| parent-registration.json | 父实际读到同组孩子并登记；之后才发gate许可 |
| scientific-entry.json | 已到原point_column调用边界，不等于任何panel完成 |
| mode-result.json | 原mode返回、内部球传输、完整私有ledger身份、错误/finalization errors |
| parent-close.json | 实际退出/是否reaped/所发signal/unknown与登记错误 |
| mode-i-global-commit.json | 六流及mode行完整传输后真实外层commit |
| parallel-mode-spools/result.json | 完整调度/模式进展/所有权/资源与归并scope |

子进程不创建新session/group。父只能对同pid/startticks/pgid/sid仍吻合的已登记孩子发SIGTERM/SIGKILL；未知或不可读保unknown。实际Process.join用于本父创建的孩子，不能把扫描到的外部同uid进程误认作自己的后代。尚未登记的孩子在poll gate期间仍看原stop/clock；父登记失败不让它永远等待或先科学执行。

若原point_column返回partial，保其原pending、last_paid、完整当前state、last_unaccepted、transaction_open和两个uncommitted span。若process硬退出而没有mode result，保真实未返/退出/原private路径，不猜当前state，不从相邻mode移植。

父result的核心字段为：

- actual_started_modes：实际fork成功的mode；
- actual_worker_scientific_entry_modes：由完整返回metadata确认到达边界的mode；worker_entry_list_scope明确缺确认不等于未起；
- actual_globally_committed_modes：真实全局commit的原序列表；
- actual_not_started_modes：从未fork成功的mode；
- actual_started_but_not_globally_committed_modes：实际启动但缺global commit；
- all_required_modes_returned：全部112原序返回均已提交，不等于每行数学complete；
- all_required_mode_families_complete：还需每原row.complete；
- process_quiet、mode_tasks、owned_child_events、error、budget_record_error和spool_retirement_stop。

mode_tasks完整保每个真实模式的ownership、实际return/control消息、offset、全局stream spans、transfer_error、retirement错误和原件身份。未合并mode的完整科学pending在complete-unpaid-scope和原mode-result中保留；不以计数替代地址。

## 8. sampler顶层返回及原下游条件

原sampler仍输出result.json、geometry.json、large-arrays及原全部采样/行账本。仅在真实完整条件满足时，native_geometry_ready和completed才能按原主程序置true。

新增顶层字段：

| 字段 | 用途 |
|---|---|
| actual_two_worker_source | helper真实file/bytes/SHA |
| original_serial_sampler_source_sha256 | 未修改祖先21032 |
| actual_mode_parallelism | 上节完整真实调度记录 |
| actual_far_mode_row_scope | 标明actual_far_modes_attempted现为原序全局提交返回行 |
| actual_far_worker_started_modes | 实际子进程启动集合 |
| actual_far_worker_entry_modes | 实际有完整确认的科学入口集合 |
| actual_started_uncommitted_far_modes | 已启动但未globally committed集合 |

原actual_far_modes_completed、complete_factorized_far_modes、complete_unit_far_row_modes、actual_not_started_far_modes、linear_phase_attempts/resource_receipt及sampling_phase_resource_receipt仍保。unstarted集合不能再用len(global rows)推导，因为同一波的后一mode可能已实际运行而未提交；新sampler使用helper的真实集合。

数学行完成后仍须原112行全部complete，再调用原momentum_rows。该函数、联合representative cap、原112×224矩阵、真实mu字验证、577nodes/576stages以及全部point误差receipt不改。native、453/450、后续fullJ/FD和closed-field证书没有被helper代付。

本helper退出0不是独立top-level CLI；它由sampler调用并返回，或在caller/budget/quiet未付时用原WorkStop。sampler保持原返回0/2语义。source生成器仍用其原0/1/70运输语义。无新benchmark或数值比较前门。

## 9. 完整入口必须继续真实接的范围

R556组件已可生成并调用新sampler，但此时没有改原完整request/workflow/consumer白名单。后继R557应至少显式处理：

1. 实际pipeline选择本sampler及其新SHA/schema；同jobC、cut、全部112deep原inputs不变。
2. 原native config、driver/checkpoint读取sampler来源的真实字段，不能把c901输出报为21032。
3. 之后R456 same-far及R462/R464 union若使用此first112真实结果，须在它们的原source/input约束中登记本新tuple；不能仅换外层label。
4. 必要reader保新的实际worker/global集合、全部原失败/未访地址、shared资源、完整stream和source身份。mode大数据不因为新helper而自动准许发布或拆成多份90KB。
5. 所有实际孩子已reaped、原outer owned范围quiet及所有原必要marker齐，才可由原cleanup删除namespace。

旧source作为祖先全部保留；current role另有真实新身份，不覆盖历史字段。当前235和任何正在运行源码均不变。新schema或来源注册不能冒此前某run已验证了本并行程序。

R556不提供独立必要reader，也不写“90KB必要全部完成”的marker。完整report可能大于90KB，它是本job临时原件；未来完整入口必须按原必要scope选择并独立返回，达到上限仍真实partial/70，不抬限、不分包同body、不截失败字段。上述注册尚未形成前，不声称全链可派发。

## 10. 资源事实、语义边界与当前交付状态

历史R511 actual222记录原传播6124.8677721839995秒、2044754次attempt、4053992次check；原phase cap11079.289409213596秒、共享work cap25000000。该记录来自唯一既有必要读回，不是新并行测试。

同次far-accepted-panels真实stored20359322057 B / 623e90653b1270505579c774f4b2d86fd28ca5ff6d933ce1b3ea917cb01ba27a；decoded95028212980 B / aba486e649d354a61857e03de6927a300ed1373b34bc41676c36025354af177c，共1604049行，gzip1。旧必要读回parsed_rows=0，只支持这些真实身份/计数；本文没有重取旧log或逐行读旧科学账本。

两worker可重叠独立mode算术，但整个新程序还要支付cache重复、原序完整解码/地址搬运/gzip重编码、fsync以及原free-space责任。没有在paper中假定2×加速，没有把某个更短cap或临时spool容量当成已够。原complete ledger不能因较大而换为科学identity-only。

当前已付的是原有限函数的独立性、共享budget/clock不重开、准确区间传输、完整ledger地址/commit关系，以及实际sampler调用实现。未付的是本新源的实际数值返回、所有下游来源组合、完整native/BVP、metric与mesh/M/t结果。它们保原门和真实未起范围，不能从本条件定理回填。

