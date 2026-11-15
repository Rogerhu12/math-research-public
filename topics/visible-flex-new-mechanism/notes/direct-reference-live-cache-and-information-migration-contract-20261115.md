# 新直接 reference 任务：同进程消费、信息迁移与独立预算

日期：2026-11-15。关联已发布设计：direct-reference-cold-path-elimination-design-20261115.md；新核心源码 frame_direct_reference_geometry159.py，blob 30efdbf813c4716d08deddd2fb1ff141d5a2e4a1。

这是独立新求值方法的任务合同，不是原已耗尽 m7 的恢复请求。根已据原研究授权明确本次1800秒新科学墙钟、64次新LP、160次新真实value，详见第8节；旧epoch不继续。后继constructor/outer/transfer/audit仍在接线，源码与请求全部绑定后才触发唯一公开首次执行。

## 1. 新开发模块及精确工作量

新增：

topics/visible-flex-new-mechanism/scripts/frame_direct_reference_geometry159_development.py

静态源码 blob：4da72140d16034b5e61054142eba7f6d8757e113；20,642字节；SHA-256 af63965826364efee0e96e12663a77d520d28f246b957ce1cb3e7b4e8fb9cc12。未执行。

入口为 developer_check()，或公开Actions中的：

~~~text
python .../frame_direct_reference_geometry159_development.py \
  --check-only --out @OUT@/direct-reference-development.json
~~~

输出tag为 DIRECT_REFERENCE_DEVELOPMENT。入口要求原公开研究环境；没有本地运行或科学入口。

精确三组，每组3个case，每个case给一个由其必要断言合成的Boolean，合计9个新check。case的内部数值、键集合、shape和最大差仍逐项保留，不用一个“通过”抹掉差异。

| 组 | 三个case |
|---|---|
| reference_and_Jacobian_branches | 零null普通8角；非零Q/null基本J8角；非零Q/null完整二阶J16角 |
| deleted_calls_cache_and_failure_cost | 两个被弃geometry禁止调用；同进程原缓存命中并保真实null变化；一次受控component失败仍计时 |
| new_identity_and_selected_binding | 原物理身份与新路线SHA；原SelectedRadialJacobian构造和bind；frozen_metric_copy不重建对象 |

人工输入只用原 artificial_problem(1) 工厂，复制原工厂实现或重新调用旧 developer_check 均不需要。明确的径向数组含12点，最大16角，原163列与独立159列完整保留。这里没有真实课题候选或新的求积结果。

在所有case完成的正常开发结果中，预定顶层调用数为：

| 调用 | 次数 |
|---|---:|
| 原人工输入工厂 | 2 |
| 原field人工geometry comparator | 3 |
| 上述comparator中的J请求 | 2，分别basic/full |
| 新adapter人工geometry | 6 |
| 新adapter正常完成 | 5 |
| 新adapter受控失败 | 1 |
| 新adapter中的J请求 | 2，分别basic/full |
| SelectedRadialJacobian构造 / bind_ordinary | 1 / 1 |
| selected-J evaluate / 全方向JVP / LP / optimizer | 全部0 |
| 旧developer suites / 真实研究geometry | 全部0 |

这些是顶层计数，不把 comparator 内部调用 SingleQ、Bounded、Independent 再重复累加为新的顶层求值。若某case未到达其必要调用，报告按真实已经开始的数量记账；不能拿预定数当已经执行数。

### 1.1 唯一受控失败

第三个缓存case在原小人工数据上临时令新模块的 target_frame 抛明确的人工错误，故只失败一个已开始的新adapter geometry。它验证 finally 中 geometry总时间、component时间和failed计数均保留，随后_direct_call释放。该失败本身是预定测试输入，不是科学失败。

旧 Bounded.geometry / IndependentHeight.geometry 的临时禁止调用哨兵也只存在于人工context manager中，退出后恢复。生产代码不monkeypatch任何旧对象。

### 1.2 不重跑已付开发

开发模块没有调用旧套件。原16 paid-attainer、18 guard及更早开发只能按完整原receipt复用。若本次只有某组失败，后继必须精确保留已经执行的case和源闭包，不能为简单恢复入口重新执行已付组。

## 2. 唯一初始物理状态与完整历史

新方法的物理起点仍是原 guard 当前best的真实checkpoint：

- 原run 43767357527 / job 132975354666 / source 6f886c385bdc12c8963d451369c9250fa19a45a0；
- 当前独立159、精确物理163与固定reference不变；
- physical SHA：e0ab278d1525c90a2be30db12c78e6faac369a8b8d01f0236f4fe6fd02e79f83；
- norm bank 438条，原state SHA 1a1d55857ed7ae7734054126cec38c9d99e72ce144ab321152c3f5fab8fd10fd；
- 原coarse/fine pools 4432/4525，versions 1/2，原顺序保留；
- 原B=1/4000，两streak均0；
- 两个经验guard系数为原完整committed值：
  coarse 17.022353404161095，fine 18.064283125328743；
- 旧learning有8事件、7次有内容的commit、pending0。

最终159状态、reference、完整原网格、source cfg、M/width、pool与bank条目均来自已经付费的原记录，按记录的精确binary64/有理身份恢复，不凭上述小摘要猜数组。

原m7缺少旧提案159向量。新任务既不重建它，也不重放原第十次LP。其四个真实attainer只提供有效单位球支持方向的来源。

历史成本必须单独保留：

1. 原guard任务已付优化和值费用；
2. 首paid-attainer身份失败的已付prepare和active；
3. run43773136836的单次205.448292651秒coarse冷求值，以及最终active241.3142038439999秒。

原epoch已经关闭。新资源账与旧累计历史同时输出，禁止把旧超时改成“原初始化”，或重新继承耗尽前的35.6287秒。

## 3. 一次进程中的固定阶段顺序

以下顺序规定数据、身份依赖及第8节已明确的新任务范围。

### 阶段A：只读输入与新开发

只读恢复原24个必要输入和当前checkpoint、原日志中的已付开发/科学证据。旧optimizer、旧developer、旧base/J及旧LP重放数均为0。公开只执行第1节这9个新人工check。

建立原Field一次，再安装一个 DirectReferenceFiveHeightField。不运行 evaluation_variant；若以后任务确实需要不同variant，必须对新variant显式再wrap并重新记录其新定义，不能静默退回旧求值器。

### 阶段B：两个必要完整普通网格

调用方一开始就拥有将继续使用的新objective及其普通cache。由它的原 evaluate/fine_decision 路径调用新adapter，取得两个必要完整网格，同时生成原decision、原rows与真实cache绑定。

不得先单独调用adapter做“基准”再由objective重复求同一状态。若入口选择先取得普通数据，必须有已经明确验证的cache安装接口；本草案优先选择让objective直接拥有首次调用，省去第二套安装协议。

必须读取：

- 真实current159与reference163、精确物理身份；
- 固定g、b0、共同锚、quad、完整网格和M/width等不变量；
- 两份ordinary数据的全部原实际门，以及对应已付同状态收据的eta、curvature和必要位置/高度标量；
- 原独立末验与新普通值的来源区别；
- prepare、adapter构造、两个必要ordinary、各component冷/命中及总体费用。

原收据没有完整场数组，故这里不称核过旧全部数组的SHA。全函数等价性来自原数据流证明；本次新数值比较只覆盖确实保存在旧收据中的值。

### 阶段C：需要后继算法时，立即消费同cache

第8节已明确本次后继方法与预算，完成相应新源码绑定后进入此阶段。所有必要J、complete模型及试验继续使用阶段B的同objective、Field和cache，不新建runner、不重建同中心普通值。

若根决定首次任务只做求值验证，结束后这些内存会消失；不能再声称以后某个run可以免费复用它们。避免重复冷恢复的办法是首次启动前把确实允许的后继分支接全，而不是跨run保存数组。

## 4. 438条法向的数学迁移定理

原bank只保存：

- 原grid/branch/flat row ID；
- 单位球内法向n；
- 原source-center binding作为来源。

它不保存旧数值A/b。

对原正epsilon和两个分支sigma，令：

$$
\phi_\sigma(e,f)=\frac{\sigma e+\sqrt{e^2+4f^2+\epsilon^2}}2.
$$

只要法向n满足精确binary64有理意义下的 $\|n\|^2\le1$，就有全局下支持：

$$
\ell_{\sigma,n}(e,f)
=\frac{\sigma+n_1}{2}e+n_2 f+\frac{n_3\epsilon}{2}
\le\phi_\sigma(e,f).
$$

这个不等式不依赖生成n时的中心、旧p或旧ordinary实现。故在同原网格和同坐标下，只要新模型提供新的真实e/f/de/df与step scale，就可重新构建合法支持行：

$$
A_{\rm phys}=
\left(\frac{\sigma+n_1}{2}\,de+n_2\,df\right)\odot{\rm step\_scale},
\qquad A_\rho=-1,
$$

$$
b={\rm target}
-\frac{\sigma+n_1}{2}e_0-n_2 f_0-\frac{n_3\epsilon}{2}.
$$

这正是原 frame_metric_norm_direction_memory.support_row 的原式。数学迁移不授予旧A/b复用，也不要求旧法向仍在某个未知旧p处接触。

### 4.1 必须检查的原输入

逐条检查438个记录的：

- grid标签只能为原coarse/fine；
- ID、group必须是真整数，拒绝bool与浮点强转；
- 原point count、flat ID范围及group=flat//point_count；
- normal三分量均有限，作为原binary64的精确有理平方和不超过1；
- 原条目顺序、原法向、原来源字段保持逐项不变。

另外严格核同coordinate、reference、固定g/b0、epsilon、原完整grid的定义和点数。不能只凭“同163/159维数”放过不同物理空间。

原counter、旧statehash与来源分别保留为历史事实。新导入条目不算新的方向发现；不得用重新调用remember改变原法向舍入或旧顺序。

### 4.2 Fresh bank context，不伪造旧hash

原memory_context含factorization_definition_sha256。新adapter改变ordinary evaluation身份，因此该SHA必然相应改变；原bank statehash不能冒充新的statehash。

新导入步骤必须：

1. 根据新坐标/reference、新factorizer、新完整grid和epsilon构建fresh context；
2. 原context全部物理字段与新context严格一致，允许的实现域差异逐字段列出，并记录旧、新完整定义；
3. 在fresh context中导入逐条核过的原ordered entries；
4. 生成新的bank statehash，保原statehash作来源；
5. 首次真正complete model仍调用原bank.bind(model)，严格核所生成context与当前factory相同；未到该点只能标pending。

不能先将旧context对象的SHA字段替换，再宣旧statehash匹配。迁移receipt必须同时列旧context、fresh context、原entries digest及新的statehash。

### 4.3 guard先于factory的依赖

原guarded_primary在两个observable factory之前就调用_immutable_context，其中包括digest(direction_bank.context)。因此有一个真实顺序约束：

- 可以从新factorizer、row-grid、coordinate、reference、epsilon这些纯结构对象预构造expected fresh memory_context；
- 该字典必须逐项采用原memory_context的定义，不含任何猜测的A/J/e/f或旧center值；
- learning据这个expected新context建立；
- 真正complete factory建立后，再由原bank.bind(model)逐项验证。此时才标factory-bound。

这样无需为了context先构造一个多余model或多算一遍J，也没有将旧context填进新对象。若expected与factory实际不符，应在LP前停止，不放宽原绑定。

## 5. 四个旧attainer只作新的法向来源

原m7唯一已付direction event包含四个全网attainer。必要原指纹为：

- center b1cdea784c2e85779174d7ab90532dc6677893b44ab84dadb208e2c7b8b0077d；
- direction 4ece9d67a3f29d901c4e27d4880f8cc56283cbda474b8c76e65f003bfbe60634；
- attainers canonical JSON无LF：1744字节，SHA 5dc115ca8583b98b842050ee7227f6f46f9f9d4b85896d2513c850d443556bc7。

按原unit_ball_direction，从其真实affine_e、affine_f和同epsilon得到严格单位球内n，然后用第4节原式在新模型重建支持。这一步不声称恢复原159提案、旧接触点、旧全部分离过程或原selected-separation。

若某个attainer与bank的原行相同但法向不同，必须保原438行并把新法向作为额外局部支持，不能通过更新同row bank而把原约束替换掉。准确重复的支持可以注明并省去；不冒新方向数。

这些四行仍属于公开原输出的只读消费，不重新执行旧JVP来寻找它们。

## 6. 只重算新模型真正需要的行

新ordinary两网完成后：

- 原selected pools中的完整hard/soft主行，按原selected-J路径在新current cache上求J；
- 438条旧法向若对应point已在新selected observable中，直接使用同一个新e/f/de/df；
- 不在selected中的point，由新oracle.original_row仅请求该原point的必要metric导数；
- 四个额外attainer同理，按(grid,point)共享导数，不能因plus/minus或多个法向重复算同point；
- 不形成原163列完整全网geometry Jacobian，不重算旧selected-J套件；
- 新主模型的A/J/targets/RHS、pool顺序/version、step scale、原盒、M/width和两个factory的最终binding全部新生成并严格绑定。

旧的A/J数值hash保作来源或可比观察，不能以旧数据缺失为由宣称复制过它们。新模型不沿用旧complete-model或ordinary-cache签名。

即使数学上的行等价已证，浮点新矩阵是否逐位相同仍只按实际可比输出报告；不能用数学等价免掉原残差、box或实际gate。

## 7. 已commit经验gamma的迁移

原guard系数定义为已观察的原单位group8负defect，除以真实159总位移的共同块范数平方。新adapter不改：

- group8 PSD determinant 的原单位与curvature scale；
- 同一物理159→163 map及M；
- 原physical widths；
- 原两grid及epsilon；
- fixed curvature cap、fixed zeta及真实gate容差。

因此原gamma仍是同一物理问题、同一单位中的经验信息。它没有因普通实现的路线变化变成跨中心误差上界；原binary64观察的来源也仍是原实现，不能写成在新adapter下重新测量过。

迁移应复制已commit的两个精确binary64系数及各自原maximizing event的来源，不重新计算旧x/y/J，不再queue或“训练”旧八事件。

### 7.1 旧历史与新context明确分开

原learning _immutable_context同时含cfg SHA和norm-context SHA，因此新初始化要产生独立迁移receipt，包含：

- 原完整learning checkpoint/state SHA与旧context；
- 原8事件和7个commit的原始来源指纹，原commit中的before/after SHA保持原样；
- 两个导入系数的精确binary64值和原maximizer索引；
- fresh context和新state SHA；
- 原pending为空，本次没有旧事件重放；
- 哪些差异仅是实现/资源域，哪些物理/scale/width/grid字段完全相同。

如果根的新任务改变资源参数，必须逐项列出已声明的资源键差异；不能以“cfg只是metadata”为由忽略其他参数。凡影响物理、row units、width、epsilon或算法数学量的差异都不在本证明范围内。

可以让新memory内部保历史event前缀供索引查询，但输出必须明确该前缀和旧commits属于祖先context。不能把旧commits改写成它们当时就在新context发生。新的live观察及commit只能在新的实际模型与真实y−x、两factory最终binding下追加。

本合同规定迁移义务；新的migration/objective构造器正在实现，发布合同时尚未执行。不能直接调用硬编码375的旧constructor，也不能用PaidAttainerResumeObjective来绕过旧context检查。

## 8. 物理验收、预算与停止行为

普通geometry的新路线不是新的验收标准。原full-grid14门、精确物理盒、原行容差、shared-value计数、SOC原RHS、原学习事实和fallback都不得因求值简化而改变。

根后续若选择消费cache进行优化，必须在启动前定义：

- 新任务本身的scope与资源上限；
- 本次独立账与全部旧历史账的关系；
- 允许的主LP/SOC/真实trial数；
- 未完成分离模型、无下降、超时、不可行和新行的原停止/回退路径；
- 结果只能归因于实际发生的机制，不把预留或迁移当已产生增益。

### 8.1 已明确的首次独立任务

| 项目 | 本次新任务 |
|---|---:|
| 新科学墙钟上限 | 1800秒 |
| 所有实际开始的主LP与SOC总数 | 64 |
| 完整真实value总数（coarse/fine均记） | 160 |
| 每次LP上限 | 10秒，且受剩余总墙钟约束 |
| 初始B及最大body提案半径 | 1/4000，沿原值 |
| 初始原两success streak | 0 / 0 |
| 原metric目标 / 硬curvature cap | 13/50 / 58，均不变 |
| 原尾/body与height/body比例 | 1/8 与 4，均不变 |

新科学钟从本次必要来源读取与prepare之前开始，包含原日志读取、必要输入构造、metadata迁移、两次冷ordinary、所有J/factory/LP/真实trial；不能把冷费放到免费initialization。新人工单独报告实际墙钟与RSS，总process也完整报告，两个子费用不可重复加总。旧241.3142038439999秒active、293.5427817930001秒initialization、10LP、15values作为祖先历史保留，不装入新的起点计数冒旧轮恢复。

新cfg的资源差异明确是max_seconds、max_linear_models、max_physical_evaluations；计时语义字段optimization_seconds_exclude_declared_initialization须改为false并单列。其余物理、scale、width、epsilon、所有原14实际门与验收参数不改。旧阶段中描述“预算不变”的遗留标签不能冒称本次64等于原12。

原primary_allocation硬编码原总额12，因此新独立入口只更换共享总额范围为64，并使用独立policy名；原每主模型最多3次inner LP、剩余额度3/2/1与SOC至少留1的分配逻辑继续完整保留。实际开始前才计一次LP；预留不冒已经付费的调用。

两份必要ordinary直接由最终objective拥有，同过程继续selectedJ、两个factory、完整新支持与实际试步。初始原438法向和4个额外attainer不互相替换；当前4432/4525池的顺序和versions1/2先原样恢复。旧outer首次无条件expand_pool/initialize_fine_pool不能被暗中重跑，后继新行分离按真实新模型明确记录。

新任务会保持完整原assess、SOC、rebound、backtracking、hold和growth的实际路径；达到本次资源上限或一个算法停止条件，仍只算本子任务结局，不意味着主课题完成。此后根据新的完整事实继续open中的问题，不自动重复本次开发或同一计算。

原m7已超时的事实永远保留。新任务即使使用同一物理点，也不能表述为在原剩余active预算中完成。一次新的必需cache/J求值也必须实际记账；跨任务只保小来源记录，不保存数组。

若新模型只生成支持但没有开始LP，按真实status报告；若新模型与预算没有提前冻结，就不把“以后可能消费缓存”写成已经发生的继续。

## 9. 小输出与首实际读取清单

公开输出限于必要小语义报告及hash；所有完整数组仅runner临时内存。

首实际需分别读取：

1. 三组9case的逐case真实verdict、人工顶层调用数和唯一受控失败计时；
2. source/adapter两evaluation SHA、同物理g/b0/coordinate/reference证明及精确状态；
3. 两个必要ordinary的真实值、全部门和分项冷/命中费用；
4. 438条输入逐条验证与fresh bank context的pending/bound状态、原entries是否完整保留；
5. 四个attainer实际新增/重复支持数，是否只复用同point新导数；
6. learning历史receipt、导入gamma、新context和新live事件范围；
7. 如根已授权后继模型，所有J/支持/LP/JVP/实际trial成本和最终binding；
8. 全部旧历史费用、新任务费用、真实终态checkpoint及没有完成的门。

任何组或阶段未执行不得预报通过。开发源码及本合同交付时，没有执行新人工、普通几何、J、JVP、LP或optimizer。
