# 已付 p32 的新标量线包络方法：直接 first-jet 缓存与实际验收设计

2026-11-16。本文是未执行的新方法设计。它不续 cone33、不重开 HiGHS64、不重试旧 MaxTime31 三个已失败尺度。原 p32 的全步尚无物理 trial。本设计配套[凸性与下降判据纸证](paid-p32-complete-grid-line-envelope-convexity-20261116.md)；实际 p32 是否有下降子段仍未知。

## 1. 为什么另立这个方法

[cone32 实际结果](final-cone32-first-actual-and-complete-grid-separation-20261116.md) 已给出全步完整 affine 包络比基点更大，且剩余 cone 调用为0。原输出同时留下完整新161、缩放后p159、原rho/norm与source binding，足以确定一条新标量线。

新任务只在固定第52点和固定p32上建一次完整两网线系数，随后用同一缓存做有限次数标量求解。若找到足够模型下降，再把未试候选交原真实几何门。新方法有独立身份和标量调用账；“没有新159维求解”不等于“0solver”。

普通 position 几何同时给 $X,X_s,X_{ss}$ 等字段，并计算固定高度原函数。但线包络只需要 $T,X_s$ 和它们沿p32的导数。因此，新的只读 first-jet 模块直接使用原式，不为了旧 oracle 的完整ordinary外壳计算不需要的 $X$、center或固定原函数。实际trial仍调用原完整几何，所需冷前缀届时全额收费。

## 2. 原源码接口与独立身份

依据冻结 source `8dfe5272b6d4f4fb752c8962689b22a95c61f78a`：

1. [SingleQProblem](../scripts/frame_entry_single_q.py) 的 `metric`、`height_jets` 直接委托原 bounded reference；`geometry` 的 $X_s$ 组装完全显示如下。
2. [FiveHeightField](../scripts/frame_five_height_field.py) 的 `coordinates.reference_evaluation_state` 保当前154个切向列与原九高度参考；随后只在原开支撑内加5个null-height增量。
3. [DirectReferenceFiveHeightField](../scripts/frame_direct_reference_geometry159.py) 保同一 SingleQ/Bounded 对象和原加法次序。其 `_single_geometry` 中 center只进入 $X$，不进入 $X_s,T$。
4. [BoundedEntryHeightProblem](../scripts/frame_entry_bounded_height.py) 的 `height_baseline` 和 `height_jets` 只生成密度及其径向jet；固定 `fixed_primitive` 在普通 `geometry` 路径才使用。密度计算本身仍有真实成本。
5. [direction_frame_jets](../scripts/frame_complete_affine_metric_oracle.py) 已给单方向 $(\delta T,\delta T_s)$；它使用 `SelectedRadialJacobian._families` 的原radial-major/mode-minor展开，没有调用完整basis Jacobian或selected159 J。

新模块不会修改这些旧文件，不冒其旧evaluation SHA。它应保存自己的实现definition，并引用同一物理、metric、b0、reference163、null basis、原两grid和源码SHA。它只承诺生成原模型需要的first jets，不返回伪造的完整ordinary dictionary，也不将缺失X/center填零来绕 `bind_ordinary`。

原 `CompleteDirectionalMetricOracle` 的constructor确要求完整bound ordinary缓存；它的 `evaluate` 又只保存四个argmax。因此不能原封调用它来实现“一次全线缓存”，也不能把其private contract削弱。新模块只复用其独立方向收缩函数和原谱函数，保新的缓存身份。

## 3. 基点 $T,U=X_s$ 的完全公式与运算顺序

令独立当前状态 $q\in\mathbb R^{159}$，原物理参考评价状态为

$$
q_{\rm ref}=\operatorname{reference\_evaluation\_state}(q)\in\mathbb R^{163}.
$$

它保留当前154个切向系数，九高度按原固定参考进入；canonical物理163仍由原exact affine map决定，绝不把九个有理物理系数round成新的参考模型。

在每个完整原角网格上，用原 `single.source.grid_for(r,theta)`、`grid.fields(q_ref)` 与 `target_frame(fields)` 得 $T,T_s$。所有角点先进入原离散周期算子 $\Pi_N$，包括原zero/Nyquist处理；不使用 $\partial_\theta\Pi_N=\mathrm{id}$ 这样的替代。

原metric只用其实际 $a,a_s$；原九高度参考密度记为 $b_{\rm ref}$。保SingleQ原运算顺序：

$$
U_0=a_s\Pi_N T+a\Pi_N T_s,
\qquad
(U_0)_z\leftarrow(U_0)_z+b_{\rm ref}.
\tag{1}
$$

令 $C(r)$ 为原 `null_basis.values(r)`，$\xi=q_{154:159}$，原active mask为

$$
\mathcal A=\{r:\mathrm{null\_basis.left}<r<\mathrm{null\_basis.right}\}.
$$

如 $\xi$ 不全为零，按原 FiveHeight 更新顺序计算 $\Delta b=C\xi$，只对active行执行

$$
U_z\leftarrow (U_0)_z+\Delta b,
\tag{2}
$$

其余元素逐值保留。零增量和外区按原分支处理；不先把 $b_{\rm ref}+\Delta b$ 合并再一次加入U，以免无必要改变加法舍入次序。$T$ 不受高度增量影响。

于是

$$
e=U\cdot U-1,\qquad f=U\cdot T.
\tag{3}
$$

式(1)(2)就是原 ordinary geometry 的 $X_s$；没有截去物理项。center与固定原函数不在这个式子里，所以此处不计算它们。metric/b0/reference/null都仍为原对象，不更换锚、积分定义或参数空间。

注意 `field.height_jets(q,r)` 的数学结果可写成参考密度加null，但新实现应按上面的两次加法构造U，直接调用 `single.height_jets(q_ref,r)` 取得参考部分，再用原active/null更新。这样保持最接近实际普通几何的运算顺序。

## 4. 同一p32的真实单方向导数

$p$ 必须来自cone32原
`actual_complete_solver_vector_record.exact_binary64_independent_step159`。
记录的161和step-scale可作来源一致性核；不重新求解、不从旧MaxTime31猜p，也不拿raw solver前159列当物理方向。

原g固定，$\delta a=\delta a_s=0$。对u、v、Q三类切向族，令原径向/角向basis为 $R_l,A_m$，方向系数按原radial-major重组：

$$
\delta q=\sum_{l,m}p_{lm}R_lA_m,
\qquad
\delta q_s=\sum_{l,m}p_{lm}R_l'A_m.
$$

原 `direction_frame_jets` 精确给出

$$
\delta T=\sum_{q=u,v}T_q\,\delta q,
\qquad
\delta T_s=\sum_{q=u,v}
\big((T_s)_{q,\mathrm{value}}\delta q+T_q\delta q_s\big).
\tag{4}
$$

其中Q是v的原第153列，仍由原families单列承接；没有省掉它或更改列序。154列后为5个null-height方向。按原单方向oracle：

$$
\delta U=a_s\Pi_N\delta T+a\Pi_N\delta T_s,
\qquad
\delta U_z\leftarrow\delta U_z+C\,p_{154:159}.
\tag{5}
$$

再依原运算式

$$
d=2U\cdot\delta U,
\qquad h=T\cdot\delta U+U\cdot\delta T.
\tag{6}
$$

式(4)–(6)不含完整159参数轴；不调用 `SelectedMetricObservables.evaluate`、`original_row`、selected-J refresh或任何primary factory。只有一条既定参数方向。实际实现仍保finite、形状、原列layout、完整角网格、identity与owned覆盖检查。

这里不需要空间二阶position jets。原 `target_frame` 或scalar grid若本身同时生成更多scalar字段，仍使用原库并如实计成本；不能因为数学上只需一阶就声称原库的额外工作已经消失。

## 5. 一次完整线缓存：内容、覆盖与先输出

每个原grid保存同序四个binary64阵列 $(e,f,d,h)$，以及160个原径向节点和完整384/768角定义。总点数184320；四阵列约5.625 MiB的裸float64存量，不含来源对象/临时frame/JSON。实际峰值内存须由运行记录，不把该裸大小冒总RSS。

可逐原径向batch生成，但对每个batch必须使用全部角点完成 $\Pi_N$，之后按owned行写入缓存。相邻batch不得漏行/重复行；原首尾query保留，原basis和其全局参考不因batch而重建为另一空间。也可按原完整r一次生成每个grid；具体实现选定后写入definition，不在运行中静默切换。

缓存metadata包括：

- 当前159/原reference163/真实physical163及其来源；
- 原坐标、g/b0、height/null、cfg、grid与新first-jet definition；
- p32原精确向量、其记录指纹、原cone32 binding和source raw/tag指纹；
- 原行展平顺序、每grid点数与覆盖receipt；
- 四数组各自float64字节SHA、形状、全体finite；
- 每个真实子调用的冷/命中时间与累计科学钟；
- 新缓存的complete/failed状态，不以“开始”冒“完成”。

**完整缓存必须在任何多alpha优化之前写入本次原stdout和临时runner文件，随后同一进程只读复用。** JSON number以可round-trip的binary64格式输出，不删除数组、不只留hash而声称可恢复。原full cache tag与后续小semantic tag分开；以后只读observer可以消费原缓存而不重复first-jet。repo/Release/artifact/跨run文件cache都不保存这些可重算数组；Git只存source、参数、run/hash和人类结论。

原stdout会显著大于当前3.5 MB。四个finite float64数组共737280个数；若按紧凑JSON的每数至多24字符加逗号估算，系数正文保守约18.5 MB，再加checkpoint/metadata仍应按20–30 MiB级设计，不能假定connector的8 MiB读取限制可承接。不得编码、分块经API转送或把payload分片提交Git。

因此本方法采用同一workflow的后置只读report job（needs research）：只读取该次已完成research job的原stdout，核run/job/head/request与完整raw/tag指纹，提取小semantic summary、原clock、所有实际trial159/163和完整cache的元数据供根阅读。完整系数留在research原stdout，未来Actions可原样消费；report job不import科学模块、不重建cache、不求解，单列读取费用。research异常但已有cache时也不得重跑；只读job如因日志/API失败，修的只能是读取接口。其实现必须允许当前workflow尚在运行、但唯一research job已completed的真实状态，不错误要求整个run已经success。

## 6. 标量求解的边界与建议有限配额

冻结缓存后，每次alpha查询只执行原
$\phi_\pm(e+\alpha d,f+\alpha h;\epsilon)$
并取四分支与全网最大值。可同时按原解析式计算全部行的斜率；这些仍计同一次完整标量oracle查询。不得通过在每个alpha调用旧 `evaluate(alpha*p)` 来重复整个JVP。

根已明确授予这个独立新标量方法以下有限资源；唯一request必须逐项写定：

| 类别 | 建议上限/范围 |
|---|---|
| 新独立线缓存建造 | 1次 |
| 原grid系数覆盖 | 2次：coarse、fine各1 |
| 新标量优化会话 | 1次；不能记0solver |
| 完整包络查询 | 至多64次，包含端点、导数与重复实际算值；每次对全部原行计算值/导数算一次query |
| 新selected159 J / primary factories | 0 / 0 |
| 新HiGHS / cone / SOC | 0 / 0 / 0 |
| 原新旧开发suite重跑 | 0 |
| 真实trial | 最多3个真正未试alpha；每点粗细各1，共最多6个完整值 |
| 独立新科学墙钟 | 600秒，从输入读取/prepare前开始；所有新模块/序列化/优化/trial都计入 |
| 新development子额度 | 最多30秒，phase单列但包含在600秒新科学总钟内 |

对精确凸函数，可用活动斜率区间进行有界二分，或用有限次有界凸标量搜索。实际浮点实现必须记录每次alpha、全四max、全max、active/tie规则、斜率摘要和停止理由。以浮点近active集合执行的搜索，不得声称已证明精确全active判据或得到精确全线最优。

无论标量器如何停止，只把实际算出的、同模型基点下达到原下降floor的候选交真实验收；未发现候选不自动授整线不可能。不能从未知精确tie推无下降，也不能因为查询次数用尽重新开一个未计账“辅助”优化。

源科学终值为旧cone-family 968.6757049859999秒、原总1324.8055252469999秒。旧1200/1800以及96/160是已封存方法的cap，不改写；32cone/64HiGHS也永久封存。根此次另外明确授予600秒独立新方法与最多3个真实试点，不是借原剩余槽。总科学费用必须报告1324.8055252469999加本方法全部delta，旧cone-family968.6757049859999另作来源，不能两次加到同一祖先总量。

科学钟在任何本方法source log/input读取和新development之前启动；development最多30秒，是600秒总科学钟内的子额度，phase单列但不重复相加。总process另报；后置report-only日志读取费用单列，不混入科学。单次不可抢占计算若返回时已超600，保真实超额并停止后续动作，不能裁成600。若本方法只完成诊断或没有足够模型下降，实际trial可以为0，不能为填满3槽试无改善点。

根README的持续授权支持推进新问题，具体600/64query/3trial是此次明确的方法级合同。它没有修改旧32/64或旧96/160的账，不能以“计算很小”隐藏标量求解。

## 7. 真实试点的唯一验收路径

若标量选择产生新 $0<\alpha\le1$，实际参数用原同rounding/subspace apply构造 $q_\alpha$，记录原alpha、scaled159、实际差159、当前159和exact physical163。不要把理想 $\alpha p$ 与实际 $q_\alpha-q$ 混为一项。

原第52点的两网完整实际门可按physicalSHA引用，因其点未变；新first-jet基点不是新的全14门收据。每个新候选则必须实际调用原完整几何和两网全部14门、原精确163盒和原严格下降规则。位置center、固定高度原函数、空间二阶jets、曲率与ball/strip等此时全部回来，实际冷费用从同clock扣除。

原value-only学习函数若发现新actual row，必须保其ID、pool version与真实学习事实；固定方向失败时按原逻辑停止或执行已冻结的有限二分规则，不能无限继续。没有当前J的曲率defect学习、bank方向学习、covered/growth反馈不能伪造；它们保持来源状态，或仅记录确实由新线数据合法支持的独立新信息。

本方法不使用p32旧rho/norm为缩放alpha补资格；完整161只是来源，不是新candidate批准证书。原0.26目标、曲率58、g、b0、盒、height/strip/ball/reach相关原门均不放宽。

## 8. 最小首次接口证据与新scalar检查

新first-jet模块的科学系数只建一次，不另外重跑旧geometry/JVP或旧开发集来比较。使用已有p32日志中四个真实attainer的 $e,f,d,h$ 与原 $\Phi$ 四分支在0/1的最大值作这次**唯一真实adapter核对**：新cache建造后，端点0/1的两次完整查询计入64query，指定四行直接读取cache系数。按原公开value/J replay容差逐量比较，保actual/expected/difference与原来源；不声称恢复了旧全数组或逐位相同。失败就保完整已生成cache/费用并停止，不重新建造或再跑一遍源模块。

只有标量器需要新的小人工检查，拟一个组、3个case，在公共Actions首次执行且共受30秒development钟约束：

1. 原 $\phi$ 产生的光滑内部最小值；
2. 两条真实凸分支max切换/tie最小值；
3. 单调无下降的端点例。

这些只用固定小数组与原谱函数，核有限查询计数、候选判定、保存/停止字段。不调用Clarabel、旧人工工厂、真实geometry/J/JVP或任何old suite。不得把次数耗尽当精确最优证书；新开发失败保已执行case与真实成本，后续不能机械重做已通过部分。

源9/12/11/6以及原全部科学只读传递收据；没有“再验一次”的免费调用。生产里发生的first-jet/端点比较是本新方法的唯一建造与有偿接口核对，不能藏到development账。

## 9. 当前可复用输入与下一源码分工

唯一科学输入应来自刚完成cone32原日志，含p32/当前52/完整末checkpoint/最新bank与两pool。无需再下旧MaxTime31日志或旧actual-only日志；transitive证据沿该完成日志消费。原24输入仍按原98 CLI参数恢复一次，原g/b0/anchor/159→163全不变。

新文件可分为：

- 独立first-jet线系数与标量缓存/查询模块；
- 只针对上节3 case的新development；
- 一次最新原日志transfer与独立标量账audit；
- 原value-only实际验收的显式接线；
- 唯一workflow/request，明确完整cache原stdout、0旧solve、所有新scalar调用与科学clock。

这只是可实施的新机制设计。它不承诺p32有下降，不预报真实接受，也不把时间不足作为课题收尾；若该固定线被准确排除，应保本次信息并转下一真正未做问题，而非重复相同方向/模型。
