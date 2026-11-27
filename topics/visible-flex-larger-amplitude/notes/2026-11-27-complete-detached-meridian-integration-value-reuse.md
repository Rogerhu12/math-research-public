# 完整 Fejér 场的无梯度积分值复用：源码、等式与实际边界

日期：2026-11-27。

## 1. 本交付的实际内容

本交付提供一套独立、完整的工作实现：新增 `fixed_fejer_detached_meridian_values.py`，由新 normal 的两处场入口调用；完整 closure、解析 J3、解析 frame、C1、stage-matrix、adjacent-matrix、reference calibration 和 root-packet 源按实际依赖独立派生。所有源均保留完整正文，每件小于 100,000 字节。原来源及原 120 个角色与完整 SHA 对另列在来源表中，不用新文件给旧角色改名。

本次复用的对象是同一完整当前点、同一真实载体、同一有序角批次、同一导数阶下已经计算的数值积分数据。校正积分层另要求全部实际控制角 jet 的词相等。直接查询点的切向量和查询点部分积分仍执行原公式。每次场调用仍执行原 `_implicit_jet_value` 接口。因此既有根读取、必要的根或角 jet 升级、每一实际 normal 阶段、所有原残差复读及最终闭合复读继续由原实现负责。

源码和参数准备不表示新场已返回、已收敛或较快。本交付没有运行本地 F、J、J*、root、数值样例、AST、编译或 benchmark，也没有增加科学运行前的 fixture 门。已完成的机械核查是完整文本、长度、SHA，以及同一再生算法的正向生成和逆向恢复。

## 2. 固定数学对象与新增工作身份

原 base 仍为 `fixed_fejer_supported_so3_meridian_operator.py`，完整 SHA 为
`552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3`。固定 Fejér 图、参考原函数、标量定义、原 J923 网格、M160 的参考图与全部当前自由量不因缓存改变。seed 的实际完整定义照当前 base/provider 读取；本 helper 不把某次旧 seed 的边层宽度或 profile 参数硬填给新调用。

新 normal 的 schema 为

`complete-fixed-fejer-detached-meridian-values-normal-layer-v1`。

新模型在计算 canonical identity 前加入 `detached_meridian_value_reuse` 的完整 definition。随后依次绑定 reference calibration、原各 normal helper，以及新的积分值 helper。新模型身份和新来源身份诚实改变；不能据固定数学对象相同而把旧模型 SHA、旧诊断、旧误差证或旧工作场词冒作新结果。

本实现保留完整固定 normal 分割，其实际节点仍由原模型决定。本计划没有降低原 32 阶段、全部控制维数、任何角或径向域、外层变量、范数、阈值、迭代/回溯预算、原本的准确误差责任。

这套来源限定于上述完整 Fejér base。J1845、N4096 或 M320 若采用它，需要各自诚实、完整的来源适配；这里没有用宽松 schema 检查自动接受那些模型。

## 3. 真实旧调用的重复在哪里

原 normal `fields_torch` 在取得有序角列表后调用 `_meridian_data`。它从完整 x 重建当前 core、全径向 omega jets 和角向 node jets，计算整个 integration query 的 meridian 数据，同时计算当前 query 的直接 meridian 数据，求 core/cap 三个角 jet，读完整参考 integration 三 jet，再构造全部 W。

即使同一点的同一 literal φ 已存在完整 normal 根，上述 integration 数据仍先被构造，随后 `_implicit_jet_value` 才通过 `_get_roots` 读取已有根。原场函数还重新计算完整 integration 上的 `_corrected_jets`、每一阶的 cell totals/cumsum，以及 reference-centred total。几何的不同径向 query 可以具有相同 φ；这些 query 的直接项不同，整域积分项则有严格相同输入的机会。

这是一项实际源码依赖观察。它不把局部计时当完整运行时间，不推断平台何时结束，也不保证某个真实几何 union 的有序批次会重复。新的有序批次 key 不从别的批次切出角，不声称不同批形的浮点归约逐字相同。

## 4. 完整积分数据的公开接口

数值属性和接口为：

```python
q.detached_meridian_values.integration_data(x, phi, *, curvature=True)
```

返回原 data 字典：

```text
meridians
core
cap
reference
reference_core
reference_cap
W
order
```

它不构造 dummy query，不计算无用的 query direct，也不隐式替调用方求 normal 根。调用方若需要真正新角的根，仍明确使用原

```python
q._get_roots(data, phi, 2, need_linearization=False)
```

本接口自身执行原 `_select_point` 与完整有限一维角列表检查。它可以在不可复用条件下返回原完整 data；不能把“没有 cache 命中”当科学输入失败。geometry 的批处理与本 helper 的存储寿命解耦：调用方只依赖当前返回的数据，不要求预解时的 data 永久常驻。

新 normal 的构造器新增必填的真实模块参数 `meridian_value_module`，并核其完整文件 SHA、definition 和类构造函数来源。原变量、原 base 和原其他 helper 的完整守卫继续存在。

## 5. 可复用条件不是一个 no_grad 开关

只有已固定完整来源、模型与载体，并且满足全部 plain-detached 条件时，才尝试复用。

原完整 closure helper 的 `_environment_reason` 与 `_plain_tensor` 用于识别环境。出现 reverse gradient mode、inference mode、tracing、scripting、compilation、functorch、forward AD level、dual tangent、torch dispatch/function mode、autocast 或探针不可用时，均旁路缓存。x 必须是普通 CPU float64 strided Tensor，没有 requires_grad、grad_fn、functional/wrapped 状态或 forward tangent。

query 树另外逐项检查普通张量/数组及已知容器。带跟踪的或未知的 query 对象也旁路。缓存不会从 detached 数据给 active J/J* 借数值，更不会把这些数值当上游图。

以下三类情况有不同含义：

| 情况 | 行为 |
|---|---|
| 真实完整源、模型或方法被替换 | 明确来源错误，不能用回退掩盖 |
| plain/owner/完整缓存键不可用，或可选存储/clone/容量失败 | 用完整原公式，记录实际旁路或可选失败 |
| 原科学公式、域、根或有限性检查失败 | 按实际原路径传播失败，不置零、不伪命中 |

定义中的可选回退指本 helper 的明确缓存操作。它不承诺整个 Python/Torch 进程在任意全局内存耗尽后仍能成功；原计算本身也可能真实失败。

## 6. 完整点与 signed-zero 边界

原 `_select_point` 正文保留。它使用原 `np.array_equal` 判断是否切点，并用 immutable bytes 作为当前点 ndarray 的 owner。

新缓存没有从该数值相等判断直接推出词相等。每次可复用公开调用还检查：

1. 选中点是准确长度、完整 contiguous native float64、readonly、non-owning ndarray；
2. 它直接覆盖同一 built-in immutable bytes owner；
3. 当前调用 x 的全部 uint64 词与该点的全部 uint64 词相等；
4. 进入一个新 owner 时，完整 array SHA 与原选点摘要相等；
5. 点退出时再读取完整摘要，记录该旧点自己的身份。

因此 +0 与 -0 即使被原数值相等规则视为同点，也不会被新缓存视作同一词输入。遇到这种差异只旁路原计算；本实现没有暗改原根缓存的数值相等规则。

每个可复用调用确实支付完整 caller-word 比较。此处没有“只读 O(1) 元数据就证明一个新的 x Tensor 的全部词”的声称。原不可写 owner 可避免重复制造独立的完整点快照；caller 仍可由原 point_fields 每次新建，因此这个完整比较不能省略。

当选中点对象变化时，旧点值缓存被释放；active 调用也不会让旧点缓存被当成当前点诊断。若元数据尚无实际点，own point 为 null。纯读 matches-current 必须先有非 null own point，不能因为两个 null 相等就报同一点。

## 7. 完整 carrier 与 ordered-phi 键

输入缓存 key 固定同一 source/model 和当前点 owner，并包含实际完整载体的字面树：

- mesh、Gauss u/weights、全部 integration query；
- 固定前三 core、完整固定 chart、全部频率与径向自由槽；
- 实际 frozen Q 张量、bubble/gamma 有理定义、normal 节点；
- S、R、M、J、n、free_size、integration order 和 core inverse 的原迭代/阈值。

载体树包含数组/张量 dtype、shape、stride、必要 offset 和全部实际二进制词。完整 canonical base/provider/model identity 与实际对象和方法来源也被重核。载体变化会清除旧值，而不是在相同点名下继续命中。

角 key 保留原 ordered φ 全部词、shape、stride 和精确请求阶 order。没有排序、模 $2\pi$ 合并、重复角删除或从多角块切片冒作原单角计算。order 1 与 order 2 不共享同一个数据条目。

这些 key 只控制可选工作复用。它们不是新的连续角域证明，也不改变每个实际 query 仍须读取的直接项。

## 8. 输入 data 的构造与私有所有权

miss 路径保留原顺序：完整 unpack 与 angular nodes，完整 integration meridians，若有实际 query 则计算其 direct meridians，core/cap 与有限性核，完整 reference，再 W。

无 query 的公开 integration-data 接口只省去 query-specific 分支。active 或未知跟踪状态不会查 detached cache。

缓存保存完整私有副本；返回给 caller 的对象不与私有 tensor 存储共用可写引用。命中时再次检查私有对象/version token 并 clone。clone 必须保持原 tensor stride；不能保持时旁路。所有 retained 张量是完整有限的 detached float64 值，没有 graph。

私有 cache 对象没有暴露给 normal stage。原 stage 可以在自己的临时 enable_grad 中求全部控制导数，但这些导数是对本次完整 control 的原公式求导；它不把 data 的值缓存误作外参数导数图。外参数 active 路径完全走原始场函数。

reference calibration 原来记录的 frozen endpoint/defect 对象仍由同一个 source-bound calibration 拥有。cache 输入来自完整真实 reference_data 返回。它不从另一 run、另一 field schema、另一模型或另一 cache 文件名导入数据。

## 9. 校正积分层的额外控制键

令本次真实 normal 返回的控制为

$$
U=(u,u_\phi,u_{\phi\phi}).
$$

在原 order 1 路径实际返回三个槽时，本缓存仍保存、比较全部三个槽的全部六列；没有把第三槽丢弃或补零。key 包含实际 shape、stride、storage offset 和全部字。

每次 `fields_torch` 均先执行

```python
controls = q._implicit_jet_value(data, phi, order, x)
```

之后才查校正积分缓存。于是一个原根缺失、一次原角 jet 升级或原源判定的失败不能因为旧 integration 值条目而被越过。相同 φ 的根选择和其完整 32-stage record 仍由原 `_get_roots` / `_run_chain` 负责。

原 `_corrected_jets` 接受的 meridians、W、全部 controls 和 order 相同，故准确算术下其 integration 三 jet 完全相同。新实现只复用曾真正返回的完整值。它没有以“控制接近零”替代全词 key，也没有由两个 control 的数值接近推论同分支。

## 10. 原顺序 prefix/total 的逐项等式

令每个径向胞上的 Gauss 点数为 $Q$，角数为 $A$。对 $V$ 为某一完整 integration 三向量 jet，原 base 首先按原形状重排

$$
V\longmapsto V_{c,q,a,j},\qquad
c=0,\ldots,J-2,\quad q=0,\ldots,Q-1.
$$

原每胞增量和 prefix 为

$$
B_{c,a,j}
 = (s_{c+1}-s_c)\sum_q w_qV_{c,q,a,j},
\qquad
P_0=0,\quad P_{c+1}=\sum_{r=0}^{c}B_r.
$$

本实现保留同一 reshape、逐项权重乘法、`sum(1)`、宽度乘法及 `torch.cumsum` 次序；没有用另一组 Gauss 点、另一 reduce 维度、pairwise sum 或分析近似替代。保存的是实际原形状 block、完整 prefix 和末端 total。

给定真实 query，原 `partial` 和原 `cells_torch` 仍用于

```python
partial = torch.einsum('pq,pqaj->paj', query['partial'],
                      block[query['cells_torch']])
integral = prefix[query['cells_torch']] + partial
```

即 query-dependent 收缩与最后相加逐式保留。query 不进被复用的 whole integration prefix；它每次实际计算自己的 partial。未使用缓存时直接调用原 `base._integrate`。

reference-centred total 同样由原

```python
q._total(integrated[name] - data['reference'][name])
```

真正计算，然后在完全相同输入/control key 下复用。没有把 raw defect 或 centred residual 强置零。

这里证明的是原公式、完整输入和归约次序得到保留，并且返回的是此前实际计算的值。没有宣称跨线程调度、不同角批形或一次未执行的 fresh 运算必与旧运行逐位相同。新 source 与工作 policy 正是为这一实际复用行为建立独立身份。

## 11. 六个 physical jets 全保

记当前 core/cap 的角 jet 为 $C_j,P_j$，完整校正切向量的角 jet 为 $T_j$，整域总积分为 $L_j$，到查询点的积分为 $I_j$。原完整闭合 lift 为

$$
F_j=hC_j+(1-h)P_j+I_j-(1-h)L_j,\qquad j=0,1,2.
$$

定义实际 raw defect

$$
\Delta_j=C_j-P_j+L_j.
$$

本实现保留全部六项

$$
F,\quad F_\phi,\quad F_{\phi\phi},\qquad
F_s=T_0+h'\Delta_0,\quad
F_{s\phi}=T_1+h'\Delta_1,\quad
F_{ss}=T_s+h''\Delta_0.
$$

在这些式子里，query 上的 $T_0,T_1,T_s$ 来自当次原 direct meridians 和原 `_corrected_jets(...,need_s=curvature)`。core/cap、$\rho_0$、各 raw defect 和 centred residual 都完整返回；field finite 检查、calibration.observe_field 与原 evaluated_field_points 更新继续执行。

因为直接项不被整域 cache 替代，这一分离不会把一个查询点的径向导数拿给另一个查询点。因为 active J/J* 完全旁路，六 jet 关于所有当前自由变量的完整隐式链也未被常数化。

## 12. 原 normal 数学、求解与强制复读

新 normal 源中有 53 个缩进 method 定义，其中 2 个属于原 EndpointPolicy，51 个属于 ZeroClosureOperator。后者仅四个方法改变：构造器、metadata，以及两个短入口 `_meridian_data` / `fields_torch`。其余 47 个完整方法正文逐字保留。

特别保留：

- `_select_point`、`_get_roots`、`_run_chain`；
- `_implicit_jet_value`、`_corrected_jets`、`_total`；
- `_stage_constraints`、`_stage_control_jets`、原 J3/J6/J9 与原 solve；
- 所有原 root 接受、域、回溯、每阶段角 solve、最终 residual 和 forced reread；
- 旧 active frame/C1、全上游 previous/data/zero-target 依赖；
- 全原 checkpoint 变量、原六 jet query、J/J* 接口。

这不是由 cache 名称推出的声明。完整 source-only 再生器保存原全文 SHA，按有限显式变换生成独立完整新源，再逐项反向恢复原全文；normal 方法文本比较也明确列出上述四个改动。

原 closure constructor 对整个 normal class 的 method AST 守卫继续保留。新 closure 的显式替换表仅增加两个完整短入口，未把整类检查关闭或改成允许未知方法。构造器和 metadata 原本就按完整实际 source/model 绑定；新的 helper 也单独核完整文件与真实代码来源。

## 13. 内存边界、失败和实际计数

可选 LRU 的上限固定为 256 MiB，计的是 retained 私有 tensor storage 字节。该上限不包含原完整科学计算本来需要的内存、返回 caller 的当次副本、Python key/record 开销或临时 clone。说明中不把这个上限冒作整个进程 RSS 上界。

input 与 corrected 条目共享这一存储预算。超限时淘汰旧条目；单条超限时不保存。删除 cache 条目从不删除根、变量、角、径向 query、阶段 record 或真实拒绝记忆。未来同一 key 未命中就再运行完整原公式。

存储、clone、完整可选 key、tracker 及容量不足均有明确原路径。若原科学运算本身失败，原错误照实传播。保存在元数据中的 last_call / last_point_exit 保留自己的点、完成或失败状态、原计算来源 ordinal、完整 key/值摘要和可选失败说明。

计数区分：公开调用 started/returned/failed；eligible/bypass；input/corrected 的逻辑请求、命中、未命中；实际原 data、校正切向量、prefix 或 base integral 返回；query partial 次数；存储、淘汰、实际私有存储峰值；完整点比较与 entry/exit word hash。不是每次逻辑请求都宣称再次执行原公式。

已有 base 的 inverse_chart_solves/reference_jet_evaluations 等计数只在真正原函数执行时增长。新的逻辑命中另记，不能据旧计数减少断言一个未实测的加速比例。现有 normal 的所有实际 stage/matrix/closure 计数也仍是原路径计数。

## 14. 纯读与 root packet 的精确合同

normal.model 与 normal.metadata 的新增键同为：

`detached_meridian_value_reuse`。

纯读接口是完整 source-bound helper 的

```python
validate_metadata(value, *, model, source_by_role,
                  current_full_point_sha256)
```

返回完整核后的独立 JSON 副本。顶层仅导入 stdlib；NumPy/Torch 只在数值构造器内导入。pure consumer 应先核整个 helper 的真实 SHA，再调用该接口。其 definition、canonical identity、actual model、operator source、完整 counter keys、计数等式、实际容量和 own-point 边界都真实核读。

这一诊断存在于完整 OPERATOR metadata 和相应 latest record。原 ROOT_SNAPSHOT 没有被改写成伪有 cache 诊断；纯读不能向旧或子 snapshot 回填字段。原 root-packet producer 只新增一个完整 normal/source registry 项，旧 registry 全部原样保留。捕获仍只拷已经存在的完整根值、原 stage records、既有矩阵和点，不触发任何 F/J/root 升级。

候选初稿的两个 matches-current 布尔曾把两个 null 判为相等。终稿仅要求两者先有实际非 null own point；数值 class 完全未改。三个必要 SHA 级联和未执行候选身份在完整锁表中保存。不能把候选当一次已运行科学失败。

## 15. 与几何批处理的分工

本 helper 本身不决定 geometry union 的角批处理策略。另一个完整 geometry 源可以先使用 integration_data 对真正缺失的角调用原 `_get_roots`。它必须保原 union 顺序、原 angle_block、原所有地点与六 jet、原聚合次序，以及已有低阶根的原升级路径。

本包不需要这些批次常驻缓存；输入和值缓存只根据真实等键机会复用。预解记录中的 planned batch、returned batch、原阶段记录、partial failure 和全点 identity 均应来自实际调用。也不允许用这一接口捏造未返回的父 checkpoint 或 accepted point。

本次独立 lower 的数学复用证明与 geometry 的批处理浮点定义应分别说明。两者组合后仍需真实执行完整 science、读原物理项并付全部连续误差责任。

## 16. 完整可逆再生与交付边界

完整再生器为 `reproduce_fixed_fejer_detached_meridian_lower_sources.mjs`。它只用 Node stdlib 的文件、路径与 SHA 功能；读取每个完整原 Python 源并核 bytes/SHA，生成全部十个完整新文件，核新 bytes/SHA，并逆向还原每个派生原源。新 helper 全文包含在再生器中。它不会导入任何科学 Python 模块，不执行 AST/compile、torch、numpy 或数学求值。

调用形态为：

```text
node reproduce_fixed_fejer_detached_meridian_lower_sources.mjs
  --parent-dir /absolute/path/to/original/complete/sources
  --output-dir /absolute/path/to/new/source-only/directory
```

`--verify-existing` 只核已经完整存在的新源；这不是科学准入门。我们在 V8 中对同一个文本再生算法使用内存文件/SHA适配器，实际得到全部十个相同全文和原父逆向恢复；没有声称本地 Node 或 Python 执行。

本交付不产生新的 science ready，也不改活跃 queue。根端将以完整新 lower、独立批处理 geometry、真实上层 source binder、纯读、观测器和完整原参数接成独立新族。全部旧 120 个 source pair 保留为原来源；新 runtime 以独立角色和真实 SHA 登记。真实未来 field、normal model、point、accepted trial、checkpoint、packet、命中率和耗时均不可预填。

同一准确固定 $g$ 不意味着新工作 source/model 具有旧工作场的逐字身份。R717/R719/R720 的条件性 core 几何、R709 的当前 mean 存在性、全 normal branch/IFT、整域六 jet、Gram/K/support、闭面及幅度/距离费用，仍各自按真实完整场支付。这个工作值复用不把任何一项未付证据改成已付。

## 17. 完整锁源与直接来源

以下是本包全部运行体的完整来源；上层组合必须使用这些真实 SHA，不能只因方法名相同而混入旧 helper。

| 完整运行体 | 字节 | SHA-256 | Git blob |
|---|---:|---|---|
| fixed_fejer_meridian_closure_values.py | 59440 | 2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0 | 2383f9c4bad43635e43fe409b048d3f74d2b9b8c |
| fixed_fejer_meridian_analytic_stage_jacobian.py | 25697 | 223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811 | 7525e1f076c90b877d7574c8aea85dc12e02d973 |
| fixed_fejer_meridian_analytic_normal_frame.py | 47244 | ab282ea02ce774b6f2aa044c700389369d05d1ff6105cdc9a0dbdae33a4db544 | abfa338ddea26f149a337a14882121505ba1af96 |
| fixed_fejer_meridian_normal_frame_c1.py | 37361 | c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246 | 5daa46fca67d3e90985fed092c37ec4eefd20421 |
| fixed_fejer_meridian_stage_matrices.py | 61280 | f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791 | 57e215d6bd28e7df8d7172106df5caa209ebc78c |
| fixed_fejer_meridian_adjacent_matrices.py | 36766 | bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564 | 641da23cdb76029f343ab441d03625e190cc4ae1 |
| fixed_fejer_meridian_reference_calibration.py | 11872 | aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3 | 2f816e1e3e617a1c8bf85bea8067f5aedd8e773e |
| fixed_fejer_detached_meridian_normal_lift.py | 96276 | 388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4 | 8a22b31dcc36d3160d4c968f9645600961a22abc |
| fixed_fejer_meridian_root_packets.py | 73723 | 910f131c9f7024cdd7866f913f3211247327098bdae2735442619f397d3a9e15 | e347b156b0b4bec87871fc07809a40a3bbda4ddd |
| fixed_fejer_detached_meridian_values.py | 41030 | 7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd | 6ab29473b0d549539de69a064efb19af4227a867 |

完整原 120 个角色与 SHA 对、未执行候选身份、接口和全部运行源路径保存在 `computations/fixed-fejer-detached-meridian-value-lower-source-locks.json`，18,987 字节，SHA-256 `969a1e676eab85c7497072d6a92f34dc037230da7aebf6227b0f343eded6aba3`，Git blob `4903cf3479cd6be661ec1b2734d8a52be0b4b308`。其中“53 methods”指整个源文件的缩进 method 定义；本说明第 12 节给出准确 class 分解：2 个 EndpointPolicy + 51 个 ZeroClosureOperator，后者 47 个完整正文未变。

原完整 normal 是 `scripts/resume_20261126/fixed_fejer_stage_point_normal_lift.py`，98,490 字节，SHA-256 `42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10`，blob `ffdaf4a094c7a0363bd6bc3ed316ba1e7e8ec25c`；原完整 base 为第 2 节所列 40,840 字节的 `552f75dd...`，blob `1d9e435bb68374b71c3d7361771c28f47838d59e`。完整实际 `_integrate`、`_meridian_data`、`fields_torch`、`_select_point`、`_get_roots`、`_run_chain` 和 active implicit 接口均按这些全文核读。当前没有实际新运行结果用来支持命中率、节省时间或几何可行性。
