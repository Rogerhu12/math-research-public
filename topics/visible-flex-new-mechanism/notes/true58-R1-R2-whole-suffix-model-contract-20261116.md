# 原 R0 平面内的整个后缀 R1/R2 minimax：模型合同

日期：2026-11-16。政策：`true58-R1-R2-whole-suffix-v1`。
实现：`scripts/frame_metric_current168_R1_R2_whole_suffix.py`。

本文件和模块只作纸面/源码构造；本地没有导入、执行、编译、测试、
数值/符号计算或开发验证。实际科学调用只能由本公开仓库的新 Actions
scope 计费执行。这里没有打开旧 free36 或固定后缀 prefix102 的求解器。

## 1. 必须改变的几何问题

R514 §11 证明：前 102 个原 B3…B8 的 u/v 系数，在
`s >= 153/200` 的完整原二 jet 准确为零。固定 free36 的一次舍入
向量 q_R 后，该 prefix102 纤维无法修复后缀的 metric 违约。

本次固定后缀判定来自公开 run `43891282963`、research job
`133382836465`、report job `133384250992`，source commit
`30136a383796ea3a255c00e10e482c358b4e822b`。21 个原径向行、
coarse384/fine768 两个完整角网上，已付最大 η 分别为
`0.5451750803995812` 与 `0.5451744553138167`，均在 `s=.765`；
保留的严格预算为 `0.26600531463999305`。直接主曲率约
`50.65482 < 58`，四个原 PSD 门和 area 门均过。因此旧 scope 是
`0 solver / 0 J / 0 actual` 的真实必要门失败，已经关闭。

该次新增 `72.51349122599999` 科学秒，祖账变为
`3047.102915103` 秒 / `147` 个原 full 值，实际接受索引仍为 58。
这些是原回执读数，不是在本合同中重算得到的数值。

新问题重新放开原末 51 个系数内的 34 个 R1/R2 控制，但仍保原
R0 准确平面、原完整 172 物理盒、同一固定 g、同一高度及所有其他
系数。约束从终端单环提升为整个后缀的共同 metric/曲率。

依据：[R514](../results/R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)、
[free36 合同](true58-free-R1-R2-125-generator-model-contract-20261116.md)、
[prefix102 合同](true58-fixed-ring-prefix102-model-contract-20261116.md)、
[已付后缀失败回执](true58-prefix102-fixed-suffix-metric-failure-zero-solver-20261116.md)。

## 2. 原准确平面、唯一初点和一次舍入

直接读取 free36 完整 MODEL 的 `exact_physical_coordinate_maps.P`
及其已付浮点伴随、`physical_coordinate_definition`，并读取
RING_SOLUTION 的真实 `candidate_record.actual_backend_raw36`。
不重求原三 jet 矩阵、不重算旧逆、不重做其旧秩或同一性证明。

令 P 为该已付 `172 x 34` 准确有理映射，z_R 为原 free36 返回的
前 34 个 binary64 值的准确有理数。新后端顺序固定为

`delta_z[34], K, h`。

每次解码先作准确和 `Q(z_R) + Q(delta_z)`，再按原 P 合成相对
真正 q58 的完整物理增量。独立 168 坐标只在最后各舍入一次：

\[
q(\delta z)=\operatorname{RN}\bigl(q_{58}+P(z_R+\delta z)\bigr).
\]

这里按原精确物理/独立嵌入理解 P；其非零项只落在 u 的
54…80、v 的 129…152。不能先浮点相加 `z_R+delta_z`，也不能
改成 `RN(q_R+P delta_z)`。后者只保相对已舍入 q_R 的另一个平面。
准确 R0 结论只属于未舍入完整增量；不谎称舍入后的实际 q 仍在
该准确平面中。

唯一初点固定为逐项取负的 `delta_z0=-z_R, K0=58, h0=0`。
两个 binary64 相反数的准确有理和为零，因此它恰好是原 q58。
`delta_z=0` 恰好重现 q_R。构建时只作这两个新的参数化接口一致性
核对，不运行旧科学。

初点在新后缀模型中的严格 metric 余量由唯一的新初始值实际给出。
原全域 η 的峰在后缀外，不足以单独证明这里有 `1e-7` 余量。
即使初点在新数值门下不可行，也只运行同一个已声明的 SLSQP 问题；
不临时改目标、不添加 phase-I、不重启或另选种子。

## 3. 36 维目标与原盒

目标固定为

\[
\min (K+10^{-6}h),\qquad 1000/61\le K\le58.
\]

准确目标的后端下界取不低于 `1000/61` 的最小 binary64；共同用于
SLSQP bounds 和线性 K 行。准确目标、浮点下界及其准确 binary64
有理值分别记入 binding/summary。不会因下界向下舍入而让返回 K
落在准确允许区间之外。

所有原 172 盒行都保留。以 z_R 平移后的上下界为新的线性右端，
其法向仍为已付原 P。h 的线性行是

\[
h\ge4\|P(z_R+\delta z)\|_\infty.
\]

h 上限直接读已付的原盒充分上界。没有旧 `1/128` 小步长门、
新信赖半径或未声明的小 h 门。保留未缩放的原 `LP_ROW_TOLERANCE`
筛完整线性残差；独立用准确有理数检查舍入前/后的原物理盒、K/h
区间和原充分 h 上界。

`backend_norm_epigraph_exact_pass` 和准确 `h-norm` 单独报告。
容差通过不能写成后端 h 在准确意义下覆盖 norm；不偷偷修补 raw h。
该语义与已审 free36 相同。

## 4. 全部后缀门与实际基本形式

径向集合由已付原径向向量的准确 binary64 值与 `153/200` 比较，
必须得到原 21 行并含原 ring 行 141。完整 coarse384、fine768
角网保留原顺序及字节，分别使用各自完整圆周的 Pi_N。
两网不是抽样替代关系，也不以 fine 的限制冒充 coarse 的原 Pi_N。

每个点都进入 2 个原平滑 metric 行和 4 个原未平方曲率 PSD 行。
总计 `21*(384+768)*6=145152` 个非线性行，另加完整线性盒/norm/K/h
行。没有 active-row 减行、attainer-only 筛行或小网替代。

沿用原 `a,a_s,a_ss,b,b_s` 和完整位置二 jet：

\[
X_s=a_s\Pi T+a\Pi T_s+b e_3,\quad X_t=aT,
\]
\[
X_{ss}=a_{ss}\Pi T+2a_s\Pi T_s+a\Pi T_{ss}+b_s e_3,
\quad X_{st}=a_sT+aT_s,\quad X_{tt}=aT_\theta.
\]

原 metric 误差是 `e=|X_s|^2-1, f=X_s·T`，
`eta=(abs(e)+hypot(e,2*f))/2`；原 epsilon 的两个平滑提议行
保留。最终后缀资格另查未平滑 η 不超过上述严格预算。

曲率继续用原 `curvature_values` / `curvature_parameter_jacobian`
定义的实际第一基本形式 I、叉积法向面积 q 和分子二次形式 N。
实际 G 不替换成 1。对于共同 K，矩阵为

\[
H_\pm=(KqI\pm N)/c,
\]

其中 c 是原 `curvature_scale`。每个符号都保 trace 和 determinant
两个原单位缩放行。没有通过平方去掉符号门。

后端成功之后，两个完整后缀网还必须各自通过：未平滑 η、返回 K
下四个未平方 PSD 行、独立直接主曲率不超过返回 K（原容差）、原
hard cap 58（原容差）、独立 area 严格大于原 floor。
退化或非有限试点按真实异常保存；没有伪造正常曲率或临时降低门槛。

R514 的 L17/H125 多项式只在固定 R0 的原单环成立。
离开 ring 后 R1/R2 值不为零，T 本身非线性；本模型不把那套单环
多项式外推到整个后缀。

## 5. 已付输入的严格边界

读取 prefix102 原 stdout 的完整 MODEL，而不是报告中的数组元数据。
该原 MODEL 的 JSON+LF 为 42,929,879 bytes，SHA256
`64d1fdd63d339b102d0ce73f92e1f042110bc2fbe11ce95a92ec59d443663921`。
root transfer 负责 run/job/source/log 行的固定身份与完整 JSON 读取；
模块逐数组核 dtype、shape、bytes、SHA，以及已有 exact_binary64。

直接复用内容：

| 原路径 | 实际用途 |
|---|---|
| `new_paid_input.radial/theta` | 原 21 行选择和原两套全角网 |
| `fixed_metric.a/a_s/a_ss` | 固定 g 的后缀三 jet |
| `fixed_height_derivatives.b/b_s` | 固定高度导数；不再查 height |
| `source_scalar_fields` | q_R 全 160 行的 u/v value/s/ss/theta，取后缀 |
| `original_families.*.angular/angular_first` | 原 u9/v8 角基和角导数 |
| `fixed_suffix_full_arrays` | q_R 的 T、五个位置二 jet、e/f/eta、PSD、area、直接主曲率 |
| free36 完整 MODEL | 原准确 P、浮点 P、原盒充分 h 上界和原目标 |
| free36 RING_SOLUTION | 原 raw36、z_R、完整准确及舍入后的 q_R |

prefix MODEL 只存了前 102 的原径向基，不含后缀末三基；因此新付
项之一是原 B9/B10/B11 的 value/s/ss。直接从原 clamped quintic
对象的同一 knot/c 系数中取 full indices 9/10/11，只评这三列，
保原 zero extension。后缀已在 entry 过渡之外，原 u/v entry weights
准确为 1。没有在 `.765` 人工截断全体扰动；最终原 q168 的场仍
使用末三样条各自完整原支持。

另外，对原末三样条准确支持右端以后的径向行，采用逐行的真实
固定几何复用。分类同时要求：该行保持原已付 binary64 径向身份，
其准确有理值不小于已付原 `knots_exact` 的末端 `423/500`，且不小于
原 BSpline 实际 binary64 右端的准确有理值。不是以样本近零、
阈值、显示小数或新舍入的 `.846` 认定固定。若准确支持和浮点
端点的比较有一侧不满足，该行保留在新求值部分。

新 frame/Pi/位置二 jet/metric/曲率和物理 J 只在真正可变的径向
部分形成；固定行的 T、五 jet、e/f/eta、原 K58 PSD、area 和直接
主曲率从原 q_R 字节数组拼入。此前未存的固定 I/II 输入只新付
一次并缓存；固定 metric 提议行由已付 e/f 首次形成后也缓存。
固定行仍完整进入两网的全部约束。返回 K 不等于 58 时，其 PSD
行按缓存的实际 I/II 与当前 K 重组；其 K 导数同样按当前 K 求值。
只有前 34 个物理控制的导数由原准确零二 jet 给出零，不能把
整行 PSD 或 K 列冻结在旧 58。

原 MODEL 明确没有保存全 160 行的 frame/Pi/曲率派生数组。
本模型不宣称那些未存数组能免费恢复。q_R 后缀已存的
T/jets/e/f/eta/PSD/area/principal 原样只读；若新后端真的请求 q_R，
只为新模型需要形成此前未存的 I/II 或导数输入，另记新计费事件。
不会以这项工作重算已存的 q_R 旧数值门。

## 6. 增量求值的浮点语义

任一实际 q168 先按 §2 准确合成并舍入。再由实际 binary64 的
`q-q_R`，在原末三基和原角基中组成 u/v 的四种标量 jet 增量，
加到已付 q_R 标量数组上。原 tangent_frame 的 T/Ts/Tss/Ttheta
公式和原完整 Pi_N、位置二 jet、metric/曲率链随后仅在可变径向
行的新值上执行；固定 a/b 从已付数组读取，准确支持之外的行按
§5 原字节拼入。所保存的 frame/Pi 数组同时带有其径向关联；
完整位置 jet 和资格门仍覆盖全部 21 行。

数学上这仍是原线性标量场和同一个固定 g。浮点加法的分组与原
`field.scalar_frame(q,...)` 逐项重建不同，不能声称二者按位相同。
这一边界明记 definition、binding、summary 和每个 grid summary。
whole-suffix 合格只授权外部一次 canonical whole-body prediction。
最终原 q168 与原实际十四门才有资格改变 accepted index。

在 q_R 身份本身，不重做增量 frame/Pi/metric/曲率；直接使用已付
后缀数组。小的浮点分组差不是对任何主课题连续门的证明。

## 7. 解析 Jacobian 与缓存键

新增 J 沿用完整 `angular_kernels`、`virtual_selected_jets`、原平滑
metric 导数和 `curvature_parameter_jacobian` 的完整解析链；把
该链的 K 无关部分单独保存，不在新 K 下重求这些物理导数。
每次只拥有至多 4 个可变径向行；每个 u/v 角核至多 27/24 个虚拟方向，先缩到原末三
径向块，再乘已付 P 的相应物理行。不会形成完整网格乘 34 的位置
二 jet 张量。K 的列按 `H_±` 对 K 的真实导数解析形成，h 在非线性
行中为零，完整线性 J 固定为 `-A`。

导数含义是该实际 binary64 场状态处连续原场对 P 方向的导数，
不是对量化舍入映射求导。首次显式请求初始 J 后，固定行尺度为
`max(1,abs(initial value),max(abs(initial J row)))`，此后不变。
初始缩放请求在新 solver scope 内计费；其他 J 只在后端需要时
请求，iteration callback 不添科学调用。

缓存明确分三层。几何键为实际 q168 字节；K 无关的物理导数键为
q168 字节、拥有径向块及 u/v 族；最终 36 列 J 键为 q168 字节加
binary64 K 字节。物理导数层保留两条 metric J 和
`dq,dE,dF,dG,dN11,dN12,dN22` 经原径向/P 映射后的真实方向导数。
同 q 的新 K 只重组 trace/determinant 最终 J，不重做角核、位置
虚拟导数或这些物理导数。h 只进入固定线性项。
不能因 q 相同就把不同 K 的整张最终 PSD J 混用。
`new_full_angle_J_kernels` / `new_virtual_position_J_inputs`、
`K_independent_derivative_input_counts`、`new_K_dependent_PSD_J_assembly`
和 `new_J_counts` 分别记录实际输入生成、读取和最终组装。

初/末完整 J 大约各 42 MB 的 binary64 内存，不能把数百份常驻
内存。完整已算 value/J 数组在该次公开 Actions 的临时目录按
原字节保存，重访只读取。写/读、失败和输出时间都属于原同一总钟；
不用 actions/cache、artifact、Release 或仓库储存这些中间数组。
进程结束后未发原 stdout 的中间缓存不属于后继免费来源。

## 8. 唯一求解、返回与输出

新总 scope 建议上限 600 秒；其中唯一 solver 上限 180 秒、
`maxiter=120`、至多 240 个不同的完整 backend36 字节输入。
同一实际 q 的新 K 或 h 也计入此上限；`new_geometry_counts`
单列实际新 q 的几何调用，实际新 q 数不超过该上限。缓存读取和
K/h 新行组装仍在同一总钟内计费。上限只能缩小。
使用一次 `scipy.optimize.minimize(method='SLSQP')`，`ftol=1e-9`。
没有调用旧 ring solver、旧 prefix solver、旧普通 geometry、
旧开发校验或二次解算。大单次库调用的时限检查非抢占；实际超时
与已做工作原样记账，不宣称硬抢占保证。

必须先保存真实 OptimizeResult 全字段、raw36、status/success、
message/nit/nfev/njev、原返回 multipliers、后端耗时，随后才解码、
判断资格或检查下一阶段时钟。未返回字段不虚构。若后端没有返回，
保存真实最后 callback 输入、已完成值/J 以及实际失败部分，不捏造
status0 或替代返回。失败 callback 点不升级为候选。

模块内部 `emit` 只发 `NONLINEAR_RESULT`。caller 唯一负责
`SOLVE_TRACE`、`BODY_SOLUTION`、`MODEL`，以及异常时
`MODEL_PARTIAL` / `SOLVE_PARTIAL`，避免同 tag 重复。
只保存初/末已算完整值和初/末实际 J，相同者用明确引用去重。
若完整 `SOLVE_TRACE` 已成功输出，之后 prediction 或 actual 失败时
不再以 `SOLVE_PARTIAL` 重发同一批大数组；后续失败留在其原捕获
记录及 COMPLETE 中，已经输出的完整 solver trace 仍为原依据。
未完成 `np.empty` 的 J 仅输出已经填入的行列块和实际完成核数组，
绝不把未填内存、补零或伪截断片段当成科学输出。

完整 stdout 上限由 wrapper 明示为 512 MiB，报告 raw 上限
640 MiB；不能拆块绕限。捕获函数仅序列化已经存在的值，不运行
新科学、不复原未存值。

## 9. 固定 API

```python
build_R1_R2_whole_suffix_model(
    field, accepted_state168, ring_candidate168,
    paid_free_model, paid_free_solution, paid_prefix_model,
    cfg, lower172, upper172, source_receipt, wall, capture=None,
    *, metric_budget, charge_prepare)

solve_R1_R2_whole_suffix_once(
    model, *, wall, charge_solve, emit=None, capture=None,
    solver_seconds=180., maxiter=120, max_evaluations=240)

R1_R2_whole_suffix_capture_record(capture, *, include_arrays=False)
```

三个 `paid_*` 都是原 stdout 的完整字典。builder 的
`charge_prepare(record)` 恰调用一次；solver 的
`charge_solve(record)` 恰调用一次。builder 不做初值 geometry/J；
必要的新初值在 solver 的首次值/J 请求中形成。
`model.summary()` / `model.full_record()` 只输出已存记录。

solution 返回 `status`、`report`、`qualified`、`qualified_candidate`、
`candidate168`/`candidate`、`candidate_record`、
`actual_backend_raw36`、`backend_success`、`backend_status`。
合格候选只来自真实 status0 且 success 的后端返回，并同时过
所有 §3/§4 门。未合格时 `candidate168` 为 None；已构造的返回
向量记录仍原样保留供审阅。

## 10. 可接 prefix102 的准确范围

若得到合格的新后缀，R514 §11 才允许把它作为另一个新的固定后缀
纤维，讨论前 102 对剩余区域的恢复。原 B9…B11 与前 B3…B8 在
`.36 < s < .765` 的重叠几何全非线性；后缀合格不保证该前缀可解。

本 scope 不运行新的 prefix102 求解；root 可在后缀合格后先对
这个实际 q 作唯一原全域预测。此前 q_R 全160行标量输入不会因为
新 q 的后缀合格就自动成为新 q 的全域输入；新 q 改变的全支持
区域必须按新工作计费。剩余原十四门、全时全域 reach、embedded、
metric/端点/包络等主课题完成门不因本后缀数值问题而删减。
