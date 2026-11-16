# R596：实际保存 RHS、完整有限 DFT 与真实 cubic/quintic 单元缺陷接口

作者：geometry agent（AI）  
日期：2026-11-16  
可信度：**已证明（限同场来源、准确区间与完整覆盖的下述条件合同）**

本文是独立源码库的完整接口。它直接读取已有当前场与原数组，实际计算完整有限参考；没有新的请求、Actions 工作流、owned launcher、数值结果或 accepted450。后继 R597 / request249 / R598 已协调但未在本次注册。现行 238、241、247 及其它冻结任务不变。

数学证明见 [R596 完整证明](../results/R596-actual-saved-RHS-and-complete-finite-DFT-defect.md)。本接口不重定义原解、原目标、原物理行序或原门。

## 1　交付与实际入口

源码：

- computations/geometry_20261116_actual_saved_RHS_reference_defect.py
- 56627 bytes；
- SHA256：8a242686845844df64d248b7b9fd47096ff2c7a8c2044346c85fc9b7425afb3f；
- authored source blob：af9a17fbd7d8fd17d13a72a4a262f934fa8b51d7；
- schema：R596-actual-saved-RHS-complete-finite-DFT-and-cell-defect-v1。

本库没有 CLI，不启动 subprocess，不读取一个 future recipe 来制造当前场。唯一公开构造函数为：

~~~python
observer = R596.bind_loaded_saved_RHS_defect(
    actual_R575,
    original_job_deadline=actual_deadline_receipt,
)
~~~

actual_R575 必须是原已加载 R575 的真实 BoundProjectionDefect 对象。它已经连接当前 R553、完整系数 owner、准确 target、675 有限表达式、实际 CP、原 M/N 和原 Budget callback。参数不是一组可任意填写的系数上界，也不是只有路径和名字的 descriptor。

其余方法：

~~~python
binding = observer.describe()

cell_record = observer.inspect(
    original_cell,
    actual_same_R553_return,
)

retirement = observer.commit_original_retirement(
    original_cell,
    cell_record,
    split=original_already_decided_split,
)

necessary = observer.summary(
    original_coverage=actual_original_coverage,
    complete_cell_ledger=actual_closed_ledger_receipt,
    original_error=actual_original_error,
    original_stop=actual_original_stop,
    close_errors=actual_original_close_errors,
    actual_projection_summary=actual_R575_summary_or_None,
)
~~~

这些是本次已实现的方法。不存在另一个自动 runner、接受门、独立 clock、隐式 source 注册或 cleanup。

## 2　真实数学来源与完整依赖

下表列本库实际逐字绑定的来源；完整当前场自身的 loader 闭包仍由原 caller 保留，不能只下载表中几件就宣称整个科学链齐备。

| 文件 | SHA256 | 本库实际用途 |
|---|---|---|
| geometry_20261116_same_evaluation_full_angle_projection_defect.py | d2cfc1e35509486dd77f5f2ae4aecba3c0527b2e16b910be69540a73f3c2d6b7 | 实际 R575 对象、原 grid 合同、M/N、原 Budget、R553/current/field |
| geometry_20261116_actual_prefix_coefficient_tube_majorants.py | 81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b | R575 已核的真实 R553 类、原 scalar 返回、准确 polynomial/interval 工具 |
| geometry_20261116_finite_frenet_tube_residual_majorants.py | 4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad | 真实四块 Lipschitz、cubic power、sample fill distance、quintic transfer |
| geometry_20261116_same_call_cubic_quintic_defect.py | 6d27df22093e339fe8940bf24c57cff880d247a5f7f4fd478135adf2e4032f66 | 同次完整 PPoly binder、全部准确 cubic 系数及 Q−C 差 |
| geometry_20261116_current_C_same_call_cubic_bridge.py | 861a7d7b9125df75cc233627d664419183163080677b5b90c96905ca69490eeb | 原 phase capture status 与真实捕获来源；本库不修改它 |
| geometry_20261114_r225_free_core_bvp.py | a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08 | 原 irfft/d/dd/normal/binormal/rfft 完整物理流 |
| geometry_20261114_full_dn_augmented.py | f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e | 原逐节点增广 RHS、物理块与完整常数块 |
| geometry_20261115_continuous_ten_fixed_power_augmented_v3.py | a248e9577bf6f522b86c7c9b32d3fd51cc49dc9468760ef1d3e78e33062f9e0f | 当前 raw scalar jets 的真实适配 |
| geometry_20261114_full_dn_solve.py | c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162 | 原保存 DY、DU、完整结果和实际 fullDN 字段 |

675 的真实 prefix_coefficients、准确 field class、当前 R416/R441/动态 M bundle 及 CP 来源，不由本库改名泛化。它们来自已经被 R575/R553 实际绑定的 field，并保完整来源记录。R553 原 class/method owner 核定仍执行。特别是现有 generated evidence 必须显式传入自己的实际 R575 对象，不能在请求表中写一个“R596 enabled”就算接通。

原 43f writer 的 LiveCheckpointWriter.__init__ 实际要求 complete_source_sha256 包含 original_core_module.FROZEN_SOURCES 与 owner.consumed_source_sha256 的完整并集，并将 source_closure 写入 CP。当前 profile 的 consumed 集合实际包含 a1e/f76/a248；原 c6a 另被 writer 明确要求。本库再次核四件实际文件 SHA 与 manifest.actual_runtime_source_closure 对应值。它没有用一个旧 fingerprint 替代原完整 source closure。

额外 Python 依赖为标准库；NumPy、Arb/flint 与 interval 工具取自当前已加载的原 field/Active/runtime。没有新增 FFT 实现或包版本选择。

## 3　类与路径：必须绑定真实 owner

构造函数从 type(actual_R575).__module__ 找到实际模块，要求：

1. 实际模块 __file__ 位于本库的 HERE；
2. 实际 basename 和 SHA 恰为冻结 R575；
3. 实际 schema 相同；
4. module.BoundProjectionDefect is type(actual_R575)。

不从 sys.modules 选“第一个同路径 module”，不把独立导入的同名 class 当成实际 owner。

当前 checkpoint 必须满足：

- field.saved.checkpoint 是原已经加载的真正 fully frozen 场；
- cp.k==0；
- field.M、saved.N 和实际 R575 M/N 相同；
- 实际物理维数 3M+2、增广维数 4M+2；
- current_target_identity 与当前 CP 相同；
- repository、run_id、source_commit 对应当前公开 Actions；
- cp.directory 位于本 job 的 RUNNER_TEMP；
- descriptor 指定的 basename 为 checkpoint.json。

真实路径是 cp.directory/checkpoint.json。库只读该文件，核完整 bytes/SHA，核 decoded manifest 与已经加载的 cp.manifest 相同。它没有基于 cwd 猜路径，也不把原 receipt.file 改成新字段。

旧 R570 BoundComparison 对 basename 的 cwd resolve 已在证明中说明。这里只是新库的真实路径修复；旧 861a 字节、已运行任务与原错误记录保持。本源码事实不预填 241/247 的任何实际结果。

## 4　原绝对钟与调用条件

original_job_deadline 是实际文件 receipt，至少包含 file、bytes、sha256。库完整读取、核 bytes/SHA，并要求当前 repository/run_id/source_commit 与实际 CP 相同。当前明确接受的原 schema 为：

- request193-owned-job-science-deadline-v1；
- request203-owned-job-science-deadline-v1；
- request205-owned-job-science-deadline-v1。

这些是已存在的绝对 deadline 语义，不由本库重写。未来新 caller 使用现行 R576 的原 request205 deadline 即可，不另造一个 R596 起点。

实际预算检查函数直接取 actual_R575.budget_check。网格/频率/全部残差行/真实多项式平移/参考合成均在该 callback 下。源码没有自己的 seconds、reserve、max_nodes、M、N 或 tolerance CLI。实际 sqrt_bits 和 interval precision 也沿当前已加载对象。

构造或观察期间的原 ResourceStop、信号及 MemoryError 不被普通异常降格。本库 ORDINARY 仅为 ArithmeticError、ValueError、TypeError、KeyError、IndexError、AttributeError、OSError。当前真实 Budget.check 的 ResourceStop 继承 RuntimeError，因而穿透至原 owner。未来 caller 不得用宽 BaseException catch 把它变成“诊断成功”。

## 5　原数组与同次 PPoly 的来源合同

库读取 CP arrays 中六件完整原数组，逐件核 shape、float64 类型、有限性、little-endian raw SHA、arrays.array_identity 和 manifest.complete_arrays：

| CP arrays 键 | 原 complete_arrays 键 | 全部 shape |
|---|---|---|
| mesh | mesh | [nodes] |
| physical | physical_states | [nodes,3M+2] |
| physical_rhs | physical_rhs | [nodes,3M+2] |
| augmented | augmented_states | [nodes,4M+2] |
| augmented_rhs | augmented_rhs | [nodes,4M+2] |
| core | core | [M] |

所有节点的物理 Y 字必须与 U 的物理块逐字相同。675 nodal[0]、nodal[1] 的全部字必须与 Y、DY 相同。全部 mesh 字的准确提升必须等于原 field.x。

库**不要求 DY 与 DU 相同**。它保真实逐字相等真假、准确物理 DY−DU 最大差以及整个 DU 的 constant/core 块身份。k=0 只说明 active-control 列为空，不能把两次浮点调用的输出合成一个来源。

同次 cubic 从以下原目录读取：

~~~text
actual phase/
  accepted-checkpoint/checkpoint.json
  same-call-cubic-status.json
  same-call-cubic/result.json
  same-call-cubic/<全部原数组成员>
~~~

这里的 phase 是实际 cp.directory.parent；文件名是原 R570 合同，并不靠搜索其他 phase 的成功文件替代。

绑定顺序：

1. 核原 bridge 源身份；
2. 读取真实 status，要求原 phase-capture schema、当前 run 四元组、source_capture_available、实际 source 和原 deadline；
3. 按 status.capture_result 核完整 result bytes/SHA；
4. 核 capture.source_scope.actual_clock 与当前原 deadline 相同；
5. 调原 R569.bind_loaded_cubic_quintic，保它的完整 current field、原 fullDN、driver、Y/DY/U/mesh、完整 PPoly 原字绑定；
6. 额外要求 captured recomputed_augmented_rhs 的全部字恰为当前 CP DU。

capture 缺失或普通绑定错误仅使 actual_same_call_cubic.available=false，并保存完整异常。原 Q 的完整 residual 与原节点直接差仍可独立执行；不能因此声明 literal cubic 已付。

## 6　准确有限参考究竟是什么

当前物理次序严格为 r0..rM、t1..tM、z0..zM。库使用实际 M、实际 N 和全部 3M+2 行。N 为原合法偶数，N≥4M+4；retained bins 严格低于 Nyquist。

参考网格完整为 phi_l=2*pi*l/N，l=0..N−1。库重新用准确有理状态盒、Arb π 和 sin/cos 包围定义上的有限函数，不运行浮点 irfft/rfft，也不继承一个未说明的 twiddle 表。

全部旋转柱坐标 d/e 包含框架导数项。准确物理速度为：

$$
V=\frac{\sqrt{A^2\mu^2|d\times e|^2-\nu^2|d|^6}\,(d\times e)
-\nu|d|^2\bigl(|d|^2e-(d\cdot e)d\bigr)}
{A|d\times e|^2},
$$

其中 A、nu、mu 来自同次 R553 scalar 返回；mu 是原准确 Ltrue/Lnumeric，nu=a_s*mu。正平方根是原有限物理 RHS 的 real normal/binormal 分支，不借此识别 native root/sigma。

每个参考角都要对整个输入盒实际证明 A_lower>0、mu_lower>0、P_lower>0，然后才能计算该项。原一个角叶的正域不能替代这 N 次责任。全部 N 项完成后才形成完整输出：

- 两 mean 权重 1/N；
- 全部非零 cosine/sine 行权重 2/N；
- 全 retained rows 和两个 mean 均有 N 项；
- 无重复终点，无 omitted retained Nyquist；
- 不完整参考不返回 coefficient_rows。

全部完整行采用向外 Arb 累加再取准确有理端点。有限缓存只存最多三件**已完整返回**的参考；key 是全部系数盒/scalar 盒/M/N/sqrt_bits/实际 precision 的完整逐值对象，而非仅 digest。部分计算永不入缓存。

## 7　inspect 的同次输入与输出

original_cell 是原 DFS 的真实对象，至少带真实 piece_index、radial、angular、lower 及原地址。库不重写 cell。非 prefix 返回 None，不冒 tail/collar/patch/cap 的本诊断覆盖。

actual_same_R553_return 必须是本 cell 的原 R553 输出，带实际 scalar_box 和 actual_same_target_return；其中 original_numeric_s_interval 必须与当前 radial 相同。即使该角叶的 R553 P 未分离，只要原 scalar 返回真实存在，本库仍可独立尝试全部 N 个有限参考角；成功与否不影响原 metric 判定。

prefix 返回 schema 为 R596 基 schema 加 -cell，包含：

| 字段组 | 必要含义 |
|---|---|
| original_cell、actual_R553_return_identity | 原真实地址与同次完整输入身份 |
| same_actual_scalar_return、actual_scalar_box | A、nu、mu 和准确二阶 scalar 来源 |
| actual_cubic_record | 原 R569 完整同次返回或明确缺失 |
| actual_polynomial_input | Q、C_lit、全 powers/boxes/导数的完整身份 |
| complete_reference | 当前闭单元整个状态盒的全 N 点参考或完整首失败/未访 |
| direct_quintic_residual、direct_literal_cubic_residual | 全部逐行差区间、最大列和完整行身份 |
| whole_pair_majorants | 实际原 R521 四块常数及整个 pair/domain 责任 |
| actual_node_formation | 当前闭单元内全部实际原 mesh 端点的真实形成差 |
| actual_R521_sample_extension | 实际节点、fill distance、scalar derivative、cubic derivative 上界 |
| actual_R521_quintic_transfer | 同一 E0/E1/Ky 的原 transfer 实际调用 |
| eta_Q_upper、eta_C_upper | 只有相应已完成责任才为准确有理上界 |
| pending、error、unpaid | 完整实际未付、异常栈和当前 grid/column 游标 |

所有准确有理输出编码为分数字符串；原负零和字节来源另由原 raw 身份保存。该编码是准确算术值表示，不是为运输任意 JSON 引入通用压缩。

如果某个 grid 点未分离 P，complete_reference 保实际 index、q、完整 d/e/domain 盒、全部 N 的地址与未访后缀；部分 sums 不给任何完整 DFT 上界。若发生普通错误，record.error 保完整 type/message/traceback。ResourceStop/MemoryError 不在此降格。

## 8　节点直接差与完整闭单元分别支付

每个真实 mesh 节点的 record 保：

- 原 node_index、mesh 原 word、准确 s；
- 完整 Y、DY、DU、core/constant block 的原身份；
- 原全十 word 与 active-control 空列表的真实语义；
- DY/DU 逐字相等真假、准确差；
- 全 N accurate reference 和全 3M+2 差区间；
- 对原 actual DY 以及物理 DU 各自的直接差；
- 若真实 C_lit 已绑定，准确 C_lit(s_i)−Y_i、C_lit'(s_i)−DY_i 与原 R521 sample。

这项差是保存字与准确参考的总差，含 numerical-shadow/scalar/chart 影响。没有将它单独称作 FFT 舍入，也没有从原 RMS 推导它。

闭单元上另用实际 Q/C_lit 的全部准确 Bernstein 包围，先完成整个 pair 盒的全部 N 点参考，然后直接逐行相减。该直接盒上界不依赖节点存在。

节点向整单元的另一条路径严格经过原 R521：

- 用同一个完整 pair 盒和全 N 正域生成四块真实常数；
- 直接计算 literal C'−DY，而不是浮点 residual norm；
- 把准确参考直接差作为 formation_error_upper；
- 保实际 C_lit(s_i)−Y_i 的 state_gap_upper；
- scalar gaps 为零仅因两参考使用同一个准确 scalar 函数；
- A'=nu，nu'=a_ss*mu^2，mu'=0；
- 原 cubic_power_bounds 和 closed_cell_residual 计算真实 fill distance；
- 缺样点明确 available=false，不能借当前 cell 外的端点。

随后原 quintic_residual_transfer 用实际 R569 E0/E1。两个已付上界可取 min；未付的一条路径不能补成另一条的数值。

## 9　原退休与 complete 标志

caller 必须先形成原 metric 结论和原 split 决定，再调用 commit_original_retirement。它不能让本库 record 中任何大小、正域真假或错误改变原 split、accept、max_depth、eta 或 solver 状态。

分裂父将责任完整传给原 children。仅原终端退休可登记全域 maxima 和节点已完成索引；不会拿一个未写回的中间父结果装作全域已覆盖。

summary 的全域标志要求：

- 原 completed_all_DFS_work；
- 完整 ledger 实际 identity；
- 原 stop/error/close errors 为空；
- 本库 observed/committed/split/terminal 与原 R553 全部计数对应；
- 当前 inflight 为空，retirement_errors 为零；
- 对应所有终端 prefix 都实际支付该类上界。

complete_prefix_finite_quintic_residual 与 complete_prefix_finite_literal_cubic_residual 分开。all_original_mesh_node_formation_bounds_complete 还要求索引集合准确等于全部原 mesh 的集合，不只比较 count。节点最优包围只在原终端提交时更新。

各范围独立：先完成的合法直接 Q 残差可保留，即使之后可选 cubic 样点失败；错误仍完整保留。不能以 Q 完成替代 cubic、节点形成差或连续角投影完成。

partial 最大值只在 observed_partial_extrema，明确不是未付全域上界。all_unpaid_terminal_cells、actual_current_inflight_work、原 coverage/stack/unvisited 和错误均保。

## 10　与 R575 合成的真实调用边界

summary 的 actual_projection_summary 可省略。若给出，库要求：

- schema 为原 R575 必要 summary；
- binding 等于该实际 projection.describe()；
- 完整 cell ledger bytes/SHA 与本次同一 ledger 相同；
- M/N 相同。

只有双方完整标志均真，库才实际形成：

$$
C_M\eta_Q+\Delta_N,\qquad
C_M=\sqrt{2(M+1)^2+M^2}.
$$

C_M 包含两个 mean。原平方根上界在初始化时受预算计算并保留。最后这一次合成仍调用原 Budget，不在 deadline 后补做科学。

若 summary 合成时 ResourceStop 触发，future caller 应按原 finish 的 recovery 处理：保原 stop 和完整 source/error，随后只生成标为 partial 的必要元数据，不重开钟，不传入虚构 completed=true。当 original_stop 已存在时，库不会进入该全域合成路径。

未完成 R575 只保有限参考结果，绝不填 Delta_N=0。全 N 有限点正域不替代全角连续正域。该合成仍未支付边界锚和完整闭面 relative-metric floor。

## 11　必要读回、raw 与输出上限

库不自行发 stdout frame、写 GITHUB_OUTPUT 或创建 cleanup marker。它只返回字典；实际 caller 必须把新 cell record 写入原完整临时 cell ledger，并把新 summary 纳入正常、compare 与 recovery 的真实必要选择。

原数组、PPoly、全参考行和 cell records 留同 job 临时空间，不放 Git、artifact、detached raw blob 或 report 大副本。summary 的完整 ledger identity 不等于所有 ledger 行已经回传，这一点在源码中显式记录。

后继 caller 保原单必要正文 90000 字节和 honest 70。不能分包、编码整个 raw、删全部失败、用 identity 代替已经规定必须返的未付值，也不能声称本库任意失败数量下必然 fit。当前没有执行该运输层，所以本次不预填它的 bytes、exit 或 marker。

本库不会删除任何原文件。原 owned process quiet、现有每一必要 marker、完整 raw 生命周期和 cleanup 条件仍由真实外层负责。

## 12　异常、预算与未访责任表

| 发生处 | 本库行为 | 原科学行为 |
|---|---|---|
| 当前 CP/source/数组硬来源不相同 | 构造抛出实际来源错误；caller 应保绑定失败 | 不凭此改变原已付 BVP/metric 结果 |
| 原 cubic capsule 缺失/普通来源错误 | binding.available=false，完整错误；Q/节点可独立继续 | 原 metric/DFS 继续原规则 |
| 当前全 N 参考某一点 P 未分离 | complete_reference unavailable，保当前点/未访 suffix | 不加拒收门 |
| whole pair 不合法而节点参考合法 | 只给已付节点差，不声明 whole-cell sample transfer | 原科学不变 |
| 可选节点/transfer 普通错误发生在合法直接上界之后 | 已付范围独立保留，错误完整记录 | 原科学不变 |
| ResourceStop、外部信号、MemoryError | 原异常穿透，保 inflight/原 DFS frontier | 原 owned stop/TERM/KILL/quiet 不变 |
| 必要 summary 超限 | 后继 caller 依原 70/保 raw | 无成功 marker 或 cleanup 推断 |

完整未访含两层：本库当前 N-grid/频率/行游标，以及原 DFS 完整 cell stack/root suffix。前者不能取代后者，后者也不能抹去一个正在形成的 N 点参考尚未完成。

## 13　真实接线位置与尚未实施的 caller

原 R576 same-C evidence 中：

- self.prefix_tubes 是实际 R553 对象；
- self.reference_projection 是实际 R575 对象；
- base_once 已拿到当前 target/evaluate/norm 返回，并调用 prefix_tubes.inspect；
- 原 refinement 决定已在后续路径确定；
- 原 ledger append 和 finish/必要选择各有真实控制流。

因此后继最薄独立派生可以在该真实 slot 创建本库 observer，把同一 R553 return 传给 inspect，在原决定之后提交退休，再保所有 summary/异常。必须独立 source/schema/hash 级联、实际生成当前 caller，保持原 current-C/capture/材料/所有来源。不能只把 R596 文件加入下载列表却不调用。

本次**未实施**该派生、source plan、workflow、new recipe、owned role、reader selector 或 cleanup 注册，也未将 R581/243 的独立 R580 source 自动混入。R597 应选择并明确绑定一个真实已冻祖先，继续相同原绝对钟，不改现有 run。

## 14　数学和实绩的准确范围

本库实际源码已包含：

- 原完整 DY/DU/mesh/state/capture 的真实来源；
- 完整有限 DFT 全 N 点全行向外参考；
- 节点总保存字差；
- 当前 Q 与实际 C_lit 的 whole-cell 直接残差；
- 原 R521 常数、fill distance 与原 R569 transfer 的真实调用；
- 原全闭 DFS 退休与完整未付/partial 汇总；
- 与同一 R575 全角投影界的条件合成。

尚未返回或不在本次范围的责任：

- 任一实际当前 accepted450、具体运行完成或任何数值上界；
- 分离 NumPy FFT、twiddle、scalar compiler 各自的内部舍入预算；
- tail/collar/准确 cut patch/caps 的本有限 Fourier ODE；
- native root/sigma 与本有限正分支的额外关系；
- 原边界锚、完整误差传播、闭面 relative-metric floor 或精确连续解；
- 后继 owned/reader/workflow 的实际注册与执行。

原 R529/R514/R521 的条件推导与原 solver 容差不会因此变成一个未测的全域误差门。本库提供可执行的实际缺陷来源，未付项如实保留并允许原链继续。
