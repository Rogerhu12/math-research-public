# R602 当前 DN 原调度的实际输入支撑乘积接口

作者：ChatGPT（AI）；日期：2026-11-16 UTC。

**状态：已证明本文及 R602 正文列明的来源关系和条件命题；新工厂尚未运行。** 这里交付一个可调用的小源与完整接口，不创建 workflow、request、fixture 或 benchmark。后续 R603 才负责把它真正接入当前 worker、owner 后同 DN 模型与必要 reader；任何已运行结果均不归给本源。

## 1. 唯一新增执行源与复用来源

| 角色 | 题内路径 | bytes / SHA-256 |
| --- | --- | --- |
| 新工厂 | computations/geometry_20261116_current_DN_input_support_fourier_product_flow.mjs | 5625 / f37bee075251957649c9ee5dc25582fac5c17fc3d3b804219cb537abf35f24f0 |
| 原 R523 helper，直接使用且不复制 | computations/geometry_20261116_finite_trace_actual_input_support_linear.mjs | 6246 / e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3 |
| 本次完整证明 | results/R602-current-DN-existing-sharing-and-actual-input-support-products.md | 19151 / 0c4ec094607fc5bf5e0404480bbe07636520ef24dcaf67fd52a7531c8efe1900 |

新文件是同签名的真实 factory。它保持原 Fourier-product 局部 J，不包含 R466/R471 的有限 root-trace variation。R523 的 9504 B 另一份 flow 不是本源的依赖；仅其中已单独发表的 6246 B helper 被复用。原 717ac 的 integrationGrid 和完整 RK4 表达式是当前 flow 的数学来源。

原来一次 root、一次六组角矩、一次 Cholesky 后完整 224 RHS 的共享已存在，R602 正文逐调用说明；这不是本源新获得的收益。本源只改变一次实际 A*T 的实现。

## 2. 实际环境和目录合同

运行前由已有来源恢复者真实设置：

- VISIBLE_FLEX_SOURCE_TOPIC：原公开 visible-flexible-closed-surface 题目录，其 scripts 下保存固定字节的 78718 工厂、flow、local J 和它们的实际原依赖；
- VISIBLE_FLEX_SOURCE_ROOT：原恢复目录中的 repro/source-root，含 topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs 等原数值源；
- 新工厂与 R523 helper 在同一个真实 computations 目录；相对 import 只读取该相邻 helper。

两环境变量缺失时本模块报告来源错误。路径是真正执行位置，不是假定的旧标签。新源不会覆写原 factory、flow、J、grid 或它们的源码。文件的 source-binding descriptor 记录 path.resolve 后的实际绝对路径、完整 bytes/SHA。

模块按真实路径读取并核下列依赖后才 dynamic import 原 factory 和 integrationGrid：

| 依赖 | 相对于其真实根的位置 | bytes | SHA-256 |
| --- | --- | ---: | --- |
| 原 factory | VISIBLE_FLEX_SOURCE_TOPIC/scripts/78718-tail-fourier-root-split-engine.mjs | 2045 | a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372 |
| 原 flow 祖先 | VISIBLE_FLEX_SOURCE_TOPIC/scripts/78718-tail-fourier-product-flow.mjs | 2400 | 717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f |
| 原 local J | VISIBLE_FLEX_SOURCE_TOPIC/scripts/78718-tail-fourier-product-jacobian.mjs | 3948 | 205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25 |
| 原 grid | VISIBLE_FLEX_SOURCE_ROOT/topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs | 1805 | b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f |
| helper | 当前模块相邻的 R523 helper | 6246 | e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3 |

新源在 module load 记录自身完整 identity，schema 是
`R602-original-Fourier-product-current-DN-actual-input-support-v1-actual-source-binding`。
其自身 SHA 仍必须由未来调用者的实际 source map 绑定，不能只靠 self-reported hash 证明合法来源。表中这些直接接点也不代替原 public_resume 的完整 78 件祖先 source ledger、当前生成源并集或原 capacity loader。

112 模式仍沿原 capacity loader 的真实 source-only 内存转换调用；该 loader 是 exact_20261114_tail_capacity_loader.mjs，4499 B / 07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395。R602 不修改 raw mode 常量、不绕过 loader，也不借任意其它目录补 import。

## 3. 完整调用 API

没有新的数值 CLI。导出保持原名字：

~~~javascript
export const CURRENT_DN_INPUT_SUPPORT_SCHEMA =
  'R602-original-Fourier-product-current-DN-actual-input-support-v1';

export function createFourierRootSplitFluxEngine(options = {});
~~~

后继真实 caller 只替换原 fourier-root factory 的模块来源，options 逐字沿本次真实原 engine 输入。概念上的使用位置为：

~~~javascript
const {createFourierRootSplitFluxEngine} =
  await import(actualBoundR602ModuleURL);
const engine = createFourierRootSplitFluxEngine(actualOriginalOptions);
const result = engine.flowStateWithJacobian(
  actualInitialState, actualOrderedProfiles, actualOriginalFlowOptions);
~~~

这段是接口形状，不是已执行的示例，也没有替调用者选择 M、角数、步数或初值。原 factory 被调用一次，原 rhsWithJacobian 函数引用直接继承。原 options.cuspAwareFlow 仍由原 factory 处理；原 noJ rhs/rk4/cusp wrapper 和原 statistics 对象引用保留。

新 flow 的签名仍为
`flowStateWithJacobian(initial,segments,opts={})`。
`stepsPerSegment??64`、segments 顺序、每个 profile 的 integrationBreakpoints、原 grid、全部 a/b/c/d RK 输入及括号、完整 state/tangent 初始化与返回字典都不改。原 rhsWithJacobian 自己的 root、目标/几何访问与全部四 field 运算不合并或缓存。

返回仍含 `state,tangent,shapeDimension,minA,minD,maxRootRelative`。当 M=112 时 shapeDimension=224、state 长度226、tangent 完整226×224。原 mean 行不是可省略的 padding。工厂返回的 `variationalEvaluation` 仍由原 factory 保持为 Fourier-product-moments 范围；不能因新增 linearEvaluation 把它改标成另一种导数模型。

## 4. 唯一数学调用替换

原 flow 中恰好一次：

~~~javascript
const f=rhsWithJacobian(s,p,x),dt=new Float64Array(size*Kdim);
~~~

变成：

~~~javascript
const f=rhsWithJacobian(s,p,x);
~~~

随后原完整 i/j/k 乘积的一次文本：

~~~javascript
for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
 const z=f.jacobian[i*Kdim+j];
 for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*t[j*Kdim+k];
}
~~~

由唯一真实调用代替：

~~~javascript
const dt=completeInputSupportLinear(
  f.jacobian,t,size,Kdim,linearStatistics);
~~~

原 minA/minD/maxRootRelative 仍位于 f 取得之后、该乘积之前。helper 内分配完整正零输出，原 A/T 扫描每次重新执行；没有复用上一 field、上一 cell 或上一 H 的 support。

原完整 flow 函数跨度1538 B、新跨度1456 B。将上述两处实际替换逆向恢复得到原函数逐字内容；此处只做文本恒等检查，未 import、AST、compile 或数值对拍。资源异常的发生位置未承诺相同，例如输出分配已移至原诊断更新之后。

## 5. 数值责任和非有限回退

helper 的既有内部合同是：原兼容维度的普通数值 typed arrays，调用期间不被其它线程修改，输出是新的独立数组。当前 cell 的同步 flow 按该合同使用。原 A 全部 size×K 项与原乘法实际使用的 T 前 K² 项被读取；T 两个 mean 输入行原本不被该乘积使用，故不增加其有限性条件。

全部实际使用项有限时，helper 按每行真实 T 的非零地址形成 ascending support，正负零都视为零。每个输出仍按原 j 序保留所有非零输入乘后加；非零乘积即使下溢为零也实际执行。全部输出行/列和两个 mean 输出保留。

任一已用 A/T 非有限时，原完整 i/j/k 正文真实执行；不拒收、不省部分项、不追加输出 finite throw、不捕获资源异常后重跑。有限输入并不保证中间乘积或和有限。完整证明只承诺条件内有限最终词相同和非有限分类相同，不承诺 NaN payload、fenv flags、运行时间、异常前沿或全程序停止地点相同。

qualification 只决定哪段等价实现，不是新的数学接受门。整个 root、RK、current576、original full112、两 mean、FD/full-DN、误差或 closed geometry 的接受仍由原消费者判断。

## 6. 实际新增字段和原统计的分离

工厂真实返回三个新增字段：

| 字段 | 对象与用途 |
| --- | --- |
| linearEvaluation | 固定 R602 schema 字符串，说明这个乘积实现的来源 |
| linearInputSupportStatistics | 每个实际 engine 独立的新 R523 统计对象 |
| linearInputSupportSourceBinding | module load 实际读出的当前/祖先/helper/grid 身份与限定声明 |

原 `statistics` 对象不替换不重置。它继续属于原 root/split/RHS 的统计，不能把新乘积省略条数解释成原 root 数量减少。不同 engine 的新统计也不可只用一个总数遮掉其最后未完成位置。

新统计完整 schema 为 `original64-finite-input-row-support-linear-v1`。必要 reader 必须真选全部下列14个整数计数：

| 计数 | 语义 |
| --- | --- |
| calls_started | 输出分配完成后进入 helper 的次数 |
| calls_completed | helper 正常返回次数 |
| finite_input_calls | 全部实际 A/被用 T 资格检查通过次数 |
| original_complete_loop_calls | 实际执行原非有限 fallback 的次数 |
| actual_A_entries_checked | 真已读 A 项数 |
| actual_used_T_entries_checked | 真已读 T 前 K² 项数 |
| zero_j_terms_skipped | 真零 Aij 的整 j 段数 |
| scalar_products_skipped | 两种实际零输入所省乘积数 |
| retained_j_terms_completed | 完整保留 support 段返回数 |
| actual_nonzero_T_words_indexed | 真已索引非零 T 字数 |
| actual_zero_T_words_seen | 真已见零 T 字数 |
| T_rows_indexed | 完整索引的 T 行数 |
| zero_T_products_skipped_after_nonzero_A | 非零 A 段内实际零 T 项数 |
| retained_scalar_products_completed | 完整返回段中的保留乘积数 |

同一对象中的 `fallback_reason_counts`、完整 `last_observation`、全部原 scope 布尔也必须原样保留。只拣14数而丢这些字段不是本接口的完整读回。

last_observation 初始为 null；开始后含 rows、shape_columns、phase、input_index、finite_input_qualification、first_nonfinite_input、support_rows_completed、support_entries_completed、row、shape_index、j_action、j_completed、selected_T_row_nonzero_columns、current_inner_columns_not_individually_recorded、decision、completed。qualification 的 null/false/true 三种实际状态分开，缺失与显式 null 也分开。非有限原因仅原 `actual-A-entry-nonfinite` 或 `actual-used-T-entry-nonfinite`，不改成数学失败类。

计数只按原 helper 的真实更新位置提交。保留段的 inner k 循环中没有逐项 observer，若中断，不能从 loop 声明推完成 k 数；最后 source/engine/parent cell 的未访范围仍由外层真实原记录提供。fallback 也不新增逐 k 位置。任何资源/其它异常均原路传播。

## 7. 当前来源 receipt 的完整范围

linearInputSupportSourceBinding 的直接 descriptor 字段是
`current_source,helper,original_factory,original_flow_ancestor,original_local_J,original_integration_grid`，
每个含 `file,bytes,sha256`。该对象还完整保留：

- source_files_modified=false；
- local_J_is_original_Fourier_product_moments_not_finite_root_trace=true；
- original_primal_root_RHS_and_Cholesky_sharing_already_present=true；
- original_717ac_integrationGrid_and_RK_expressions_retained=true；
- full_size_by_K_output_and_both_mean_rows_retained=true；
- helper_support_rebuilt_from_current_T_per_field=true；
- original_nonfinite_input_complete_loop_retained=true；
- nonlinear_or_output_finiteness_gate_added=false；
- resource_frontier_and_whole_run_word_equality_claimed=false；
- numerical_run_or_speedup_prepaid=false。

这些是与真依赖读取绑定的明确来源范围，不是本次调用次数或已完成断言。source check 失败就是原来源错误，不能伪装成原 nonlinear/root 数值拒绝。

## 8. R603 后续实际接线责任

后续只需透明的真实 source views 和最少调用来源变更，不再复制旧整个数值链。必须同时做到：

1. 当前 Node worker 的 fourier-root factory 真指向本文件，并保其完整 source SHA、原环境及 capacity loader；
2. initial capture 与 owner 返回后 R532 同 DN 模型消费的 engine 是记录的真实新 engine，不能只替换输出标签；
3. 原 noJ 与 withJ 选择、原 full stage/port/endpoint/audit 顺序不改，所有旧来源/输入/pins 保留为准确祖先；
4. 当前 call/model 的实际 source receipt 真选到本 source binding；必要 reader 对每个实际 engine 选全14计数/last/reasons/scope，同时保原 root/RHS/owner/compile 统计；
5. 同一次原绝对 job clock 和全部资源 cap 保持，不以本源新建计时、不造速度或完成承诺；
6. 单份90000 B、原超限70、全部未完成/失败与实际 quiet/cleanup 责任保持。若表示需要具名共享，只能在实际整对象精确相同后做完整可逆表示，不能按未来容量省字段。

这里不分配新 workflow/run，不把新 source 准备完成当作科学通过。R603 若发现实际 caller 的 source/metadata 限制，须以明确新身份修复并记录，不能假标旧 SHA 或改已冻结运行。

## 9. 交付和引用

- [R602 完整证明与已有共享来源](../results/R602-current-DN-existing-sharing-and-actual-input-support-products.md)；
- [R523 helper](../computations/geometry_20261116_finite_trace_actual_input_support_linear.mjs)与[完整命题](../results/R523-actual-tangent-row-support-and-complete-linear-products.md)；
- [固定原 flow](https://github.com/Rogerhu12/math-research-public/blob/bce880e0037870ce0977abc5d54d0cf2bd24d2cd/topics/visible-flexible-closed-surface/scripts/78718-tail-fourier-product-flow.mjs)与[原局部 J](https://github.com/Rogerhu12/math-research-public/blob/bce880e0037870ce0977abc5d54d0cf2bd24d2cd/topics/visible-flexible-closed-surface/scripts/78718-tail-fourier-product-jacobian.mjs)。

本次作者源、完整证明、接口分别保存；交接 manifest 只列这三件身份，不加入 Git。没有保存展开祖先源、完整 diff 或任何可再生 Actions raw。
