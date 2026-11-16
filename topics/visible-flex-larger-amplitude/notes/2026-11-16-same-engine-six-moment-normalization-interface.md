# R611 当前六组 Fourier moment 原归一化词：完整调用与来源接口

作者：OpenAI ChatGPT，GPT-6 Astra。日期：2026-11-16 UTC。

**状态：源码与条件证明完成；尚未为本组件执行新的 Actions 科学计算。正在运行的 request250 没有被本组件修改。本接口不声明数值通过、完整闭面、资源可达或速度改善。**

## 1. 正式文件

| 角色 | 题目录相对路径 | bytes | SHA-256 |
|---|---|---:|---|
| 执行组件 | `computations/geometry_20261116_normalized_six_moment_fourier_jacobian.mjs` | 9963 | `54a76c39befca05381f10b744c5986ac761dffb8db6d3ebe4fa0c48fa9f5d6d7` |
| 完整证明 | `results/R611-same-engine-six-moment-original-normalization-reuse.md` | 19582 | `cd4b83229b9df410790430d540dd83b9daa1146d0c1035d375ac9c9b4dae9f81` |
| 本接口 | `notes/2026-11-16-same-engine-six-moment-normalization-interface.md` | 以交付 manifest 的实际完整身份为准 | 以交付 manifest 为准 |

原数值基线为实际恢复的 `scripts/78718-tail-fourier-product-jacobian.mjs`，3948 bytes，SHA-256 `205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25`。原文件不改，新文件不冒用这个 SHA。

本组件只使用 Node 标准库读取并核来源，没有依赖新的数值包、worker、编译器、浮点格式或独立 scientific CLI。其可调用接口与原局部 J 工厂一致，实际后继必须通过完整当前 source tuple 选择它。

## 2. 模块加载与原来源绑定

模块导出：

```javascript
NORMALIZED_MOMENT_SCHEMA
createFourierProductJacobianEngine(options, base)
```

schema 为：

`R611-current-Fourier-product-six-moment-original-normalization-v1`

加载时必需存在实际 `VISIBLE_FLEX_SOURCE_TOPIC`。模块以它定位：

`scripts/78718-tail-fourier-product-jacobian.mjs`

然后完整读取该文件，核原 bytes/SHA；同时完整读取自身 `import.meta.url` 所指文件并形成实际 identity。原文件只读，未覆盖旧路径或重标旧身份。

来源绑定失败明确报原 source receipt 问题，不能记成该场的数值拒绝。未来 source generator 应在真正生成并核完本新文件后才调用它；不能先在新文件尚未存在时借旧组件的成功 receipt 宣称已绑定。

无新的仓库默认、磁盘 fallback 或未绑定 source root。没有使用“相同 schema 名称即兼容”的快捷路径。

## 3. API 参数及真实 base

函数签名不变：

```javascript
const local = createFourierProductJacobianEngine(options, actualBase);
const result = local.rhsWithJacobian(actualState, actualProfile, actualX);
```

上述只是调用形状，不是另起 fixture 或接受前置任务。

`options` 的原数学解释完整保留：

| 属性 | 原解释 |
|---|---|
| `modes` | 实际 $M$，不由本组件选取 |
| `quadrature` | 同一实际 engine 固定的 $N$ |
| `spacing` | 原默认 `2` 及真实传入值 |
| `mu` | 原实际 $\mu$ |
| `orientation` | 原默认 `1` 及真实传入方向 |

它仍使用 $J=M+1$、$K=2M$、$\mathrm{size}=2M+2$、原 literal $\sqrt2$ 与 $\sqrt{12}$。

`actualBase` 必须是真实当前 engine 的原 base，而不能只是匹配字段的伪对象。局部源码实际读取：

- `base.M`；
- `base.N`；
- `base.root(state, profile, x)`；
- `base.rhs(state, profile, x, false, rt)`。

原 source 中的维度、解析度检查逐字保留。完整上游还要按自己的来源与 options 检查真实 root/field/state/geometry/clock；本组件不替上游选择初猜、根分支、投影 floor、停止条件或原 RHS。

每次调用仍真正得到一次原 root，随后把同一 `rt` 传给原 RHS 并取得其原结果。六 moments、原右端、一次完整 Cholesky 与全部方向仍使用这个实际 `rt`。

## 4. 归一化表示的唯一选择

### 4.1 原表构造顺序

原全部 cosine 调用先按原数组顺序完成，再按原源码构造全部 sine 调用。每次 Math 调用的参数仍为原左结合表达式：

`spacing*j*2*Math.PI*n/N`

归一化发生在这两张原表已经全部构造后；没有将 `/N` 插入某个三角参数，也没有改变任何 Math 调用参数、次数或调用顺序。

### 4.2 合格分支

`normalizeActualTables` 只在以下表示条件全部满足时选 true：

1. 实际 $N$ 为有限正整数；
2. 原 cosine 表全部实际元素有限；
3. 原 sine 表全部实际元素有限。

完整扫描两表之前不修改任何元素。选择 true 后，在原私有数组逐元素执行原 `value/N` 并保存 binary64 词。原地保存不产生第二份同尺寸三角表。

这些条件不增加科学 gate。它们只决定使用已经形成的同一个商词，还是在每次原位置重新形成同一个商。

### 4.3 不合格分支

若实际 $N$ 不符合该表示条件，或首个实际表元素非有限，则资格 false；原表原字不改。原 moment 内层选择：

```javascript
cos[n][k]/N
sin[n][k]/N
```

没有异常捕获后重跑，没有从旧 engine 读 cache，也没有不完整表成功返回的声明。

### 4.4 保留的原运算

原六组累加按完整原顺序保持：

```javascript
FPm[k]+=FP*s;
CKm[k]+=CK*s;
FTm[k]+=FT*c;
CUm[k]+=CU*c;
CPm[k]+=CP*c;
bmM[k]+=bm*c;
```

保全部当前 `FP/FT/CK/CU/CP/bm` 表达式，保原 `CC/SS/CS/SC`、`right/FL/FQ`、`solveMany` 与完整 J。没有把形如 `a*b/N` 的别处代码改为 `a*(b/N)`。尤其原 root 中乘后除的 Gram、原 primal flux 和其他 kernel 完全不在此补丁。

浮点范围包括原有限正常数、次正规数、下溢及带符号零。这里没有采用仅“正常数时可替代”的近似分支。条件证明是同一原元素除法结果词被保存，不是理想实数三角恒等式或误差界。

## 5. 返回值与对象生命周期

工厂返回：

```javascript
{
  rhsWithJacobian,
  scope: 'local prototype only; no flow entry',
  normalizedMomentStatistics,
  normalizedMomentSourceBinding,
  momentEvaluation: NORMALIZED_MOMENT_SCHEMA
}
```

`rhsWithJacobian` 的原返回对象保持：

```javascript
{ derivative, jacobian, root: rt }
```

它仍完整返回 size 维 derivative、size×K 的 Jacobian 以及原 root。后继不能把新增 metadata 丢给旧 worker 然后仍声称旧 source pin 执行了新函数。

两张表未导出；没有跨 engine 全局数值 cache。每次新的 factory 调用都使用该次的实际 $N,M,\mathrm{spacing}$ 和原生成表。实际 state、profile、$x$、root 或方向变化不会重新选择表，也不会从别的 engine 借值。

当前组件没有独立 flow/RK 入口。真实 caller 必须让原完整 withJ 流程调用这里返回的 `rhsWithJacobian`。R602 的 $A T$ helper、原 root、RHS、cusp 与 fullDN 责任仍分别由实际相应源码承担。

## 6. 完整统计 schema、八计数及未完成位置

统计 schema：

`R611-current-Fourier-product-six-moment-original-normalization-v1-statistics`

全部字段应整体保存：

```text
schema
actual_N
actual_M
actual_spacing
table_elements_scanned
normalization_divisions_completed
rhs_calls_started
rhs_calls_returned
cached_moment_rows_completed
fallback_moment_rows_completed
cached_normalized_table_reads_in_complete_rows
fallback_normalization_divisions_in_complete_rows
normalization_qualified
normalization_reason
last_observation
scope
```

八个计数的完整解释见证明 §6。它们是 JavaScript Number：准确次数解释仅适用于累计更新仍在安全整数范围；源码没有 BigInt 或溢出检测，超出时保原字段并注明准确计数未付，不据它补出操作数或接受。它们计源中真实更新的位置，不能从预期总行数填值；不能把合格标志、表准备完成或 `rhs_calls_started` 当作完整 J 返回。

资格阶段的最后观察包含：

```text
phase
actual_N
actual_M
scanned_elements
first_nonfinite
normalization_complete
current_element （仅实际进入归一化元素时存在）
```

首非有限地址保 `n/k` 及 cosine/sine 的各自非有限布尔；缺失字段与已有 null 不能互换。

当前 rhs 的最后观察包含：

```text
phase
call_number
table_normalization_qualified
current_row
moment_rows_completed
inner_k_progress_recorded
```

可能 phase 的原词为：

- `original-root-and-RHS`；
- `original-row-coefficients`；
- `original-six-moment-inner-loop`；
- `original-complete-right-FL-FQ-and-Cholesky-assembly`；
- `original-complete-local-J-return`。

没有逐 $k$ 计数，`inner_k_progress_recorded=false` 必须如实保留。只有原完整 inner loop 返回后，才更新对应行和完整行的两表读取/除法次数。外部终止时只能报告真实留下的前沿；不得推断未回传的 row、$k$、J 或原后继阶段已完成。

没有包裹原数值体的 try/catch。一次非返回调用可能来自原数值异常、原资源异常或外部终止，不能只以 started−returned 的差给出具体停因。

计数不包含时间测量，也不是原数学验收的新条件。不得为得到计数另跑 fixture、重算先前 state 或把 missing 统计补成零。

## 7. 完整来源对象

`normalizedMomentSourceBinding` 以如下 schema 返回：

`R611-current-Fourier-product-six-moment-original-normalization-v1-actual-source-binding`

它保存完整 `current_source`、`original_local_J` 各自真实 path/bytes/SHA，以及：

```text
actual_engine_parameters = {M,N,spacing,size,J,K,mu,orientation}
actual_table_normalization_qualified
source_files_modified
original_trigonometric_call_order_and_argument_expressions_retained
each_cached_word_is_the_original_table_element_divided_by_actual_N
division_not_replaced_by_reciprocal_multiplication
original_six_moment_n_k_and_addition_order_retained
original_root_RHS_solveMany_assembly_and_mean_rows_retained
normalized_tables_owned_by_one_actual_engine
cross_engine_or_cross_field_value_cache
nonfinite_table_or_invalid_N_uses_original_runtime_divisions
new_scientific_acceptance_condition
resource_frontier_whole_run_or_wall_clock_equivalence_claimed
```

`cross_engine_or_cross_field_value_cache=false` 表示没有跨 engine 表共享或 field 值缓存；同一 engine 不变三角商词的复用则正是本组件职责。它不声称每次 field 的全部缓存都重新创建。

原 source guard 保完整 identity；原恢复路径以及实际本组件路径由各自 receipt 明示。以后生成视图必须保真实 HERE/code directory 与父 source 绑定，不能把同一导出名当成旧文件的字节身份。

## 8. 明确的后继接线边界

本接口不自动注册 request253 或任何科学运行。当前若做独立后继，实际最少责任如下：

| 层 | 必要真实行为 |
|---|---|
| 局部 J | import 本文件并实际调用工厂；不是只打印 schema |
| 原 flow/factory | 必须让全部 current withJ 场真正使用新 `rhsWithJacobian`，保原 integrationGrid/RK |
| R602 组合 | 原 $A T$ helper 与原完整 source/统计保持；新 moment 字段独立并列 |
| worker | 真新 factory tuple，保原 576布局/全部当前输入 |
| current-call | 每实际 engine 的新 source/统计、真实 stage/部分范围 |
| client/fullDN | 新来源闭包与实际调用文件，原 owner/模型/FD/fullDN 体不改 |
| necessary reader | 选择整个新统计/来源对象，保失败/缺失/最后观察及原全部 scope |
| job | 原单总钟、owner caps、quiet、读回与清理，不添新科学门 |

一种实际接法是派生原 flow 的 import，使其选择本组件，再给新 flow/factory 新 identity；另一种接法是在真实 base 之上显式创建本组件并供新的完整 flow 使用。两者都需真实 source 组合。若后一种仍先构造旧 local-J，必须如实记额外旧表/闭包生命周期，而不能把本组件的原地保存性质扩大成整个组合零额外构造。

这里没有为任一路线编造已完成的 consumer。source-only 结论已经完整；真正 caller 的全文与参数/统计读回应在独立来源说明中形成后再派发。

## 9. 时钟、错误与必要正文

本组件没有新 CLI 时间参数，也没有自己的钟。未来调用必须位于原当前 job/owner 的绝对截止与资源控制中，构造表和扫描也计入同一范围。

不捕获 `MemoryError`、进程资源停止、外部 signal 或原 numerical throw 来 fallback重跑。资格 false 的原表达式分支是预先确定的表示选择，不能被描述为把原数值失败重新执行一次。

源/科学必要读回仍各按原完整范围和单 90000-byte 限制执行，真实超限沿原 70。本组件不删选择字段，不通过截断 `last_observation` 或省略 engine 来达到大小。源级计数不保证未来完整汇总能装进上限，超限也不得补称已读。

正在运行的 248、250 或此前请求不因发表本组件获得新字段或新科学结果。任何未来成功都应由实际新 run/source/原门和完整必要范围负责。

## 10. 文本形成说明

作者只对原完整文本进行字面构造与 metadata bytes/SHA 计算。没有本地 import、AST、编译、数值调用、科学算术脚本、测试、fixture 或 benchmark。

独立新源在完整原 3948-byte 数值体外增加来源/观察辅助，在原表构造后插入表示准备，并以七处精确字面变更接入归一化读取与统计。六组原乘加体及原后继数学体在新源全文中直接保留，方便按实际来源阅读。

本接口与证明一起给出完整可调用责任；不要求在发表前另作独立审核流程或额外实验门。
