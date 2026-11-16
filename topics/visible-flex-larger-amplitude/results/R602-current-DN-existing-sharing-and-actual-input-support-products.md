# R602：当前 Fourier-product DN 已有的全列共享与原调度下的实际支撑乘积

作者：ChatGPT（AI）；日期：2026-11-16。

**可信度：已证明，限本文明确的固定源码调用关系、实际输入条件和局部运算命题。新 R602 工厂尚未执行；实际支撑、全链成本、所有终态门及读回是否在90000 bytes内均未付。**

当前 R573/R594 路径没有为224个方向各重算一条相同 primal 轨迹。每次 RK field 已经只求一次 root，复用其原角向行构造原 RHS；六组局部矩一次形成，113×113 Cholesky 一次分解后解全部224右端。R532 对同次 owner 投影状态的每个 cell 只调用一次完整 flow，R534 stage 组件随后读数组做准确表示 lift，不重新求 stage。

这些是**现有共享的来源事实**，不是本结果新省下的工作。R602 的新增切点只有原717ac flow内的完整矩阵乘积 A*T：改用已刊 [R523 helper](../computations/geometry_20261116_finite_trace_actual_input_support_linear.mjs) 的同次实际T行支撑。原205b局部Jacobian、root/RHS、integrationGrid、全部RK表达式、全部输出和原门保留。没有移植R466/R471的有限root-trace导数，也没有整换R523的另一套flow。

## 602.1 实际来源和读取边界

当前来源按R573的正式240 head bce880e0037870ce0977abc5d54d0cf2bd24d2cd、完整请求及source plan核定；R594只把真实runner的owner6000改12000，并未改变本节的worker、owner、当前call或这些数学源。这里是源码结论，不从actual240未返回的科学正文推本次实际执行进度。

当前 generated caller 全文依已刊计划的完整 literal 构造核对；原恢复源码按冻结 public_resume 的source ledger核完整字节。没有本地导入、AST、编译、科学运算、fixture或benchmark，也没有再取任何科学日志。

| 当前角色或原源 | bytes | SHA-256 |
|---|---:|---|
| R573 tail client | 40476 | 3c35e7a802abdfe4857b59f6335e515207b67b312a1a08c07ff7e39ddd98e83f |
| R573 worker | 8327 | ecad08d60e9bcf668e2c5c82771627cae2c7160f806b8f2573e90dacb898f021 |
| R573 current call | 45476 | cf59d20d7fbd315b5a4250f2e691c10292030805c79430a4fa71e1755a98f0c8 |
| R573 same-call owner | 26666 | 2af373696034e49f61e6dcc49707e668ed60d600b5a4f9dbf0d71d85cd24ad17 |
| R573 call pipeline | 43286 | 1ad21f183fb98e859086d96048063a25aaa749803d68bfa67801a4df665ab666 |
| 原prefix-tail-tangent-fourier-worker | 12294 | 36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a |
| 原fourier-root-split-engine | 2045 | a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372 |
| 原fourier-product-flow | 2400 | 717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f |
| 原fourier-product-jacobian | 3948 | 205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25 |
| 原fourier-root-momentum | 13809 | cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88 |
| 原f6tail_momentum_split_flux | 2420 | 5d77ca058adb634547c91998002eeffb9de5395a9e1e130f7edd4fa65014f578 |
| 原f6tail_cusp_grid | 1805 | b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f |
| R532 same-DN projected stages | 32316 | 2279a605df5ee41c5400c658018722fd52e6add40ee35ff38dbca1a31b2bb76a |
| R534 projected-model components | 38561 | c4b3a5eb05fc4d4ae6767c2c08f75ea38a5a5538366fcd3264ff59cec17bb04e |

原worker及78718数学文件的完整路径为 topics/visible-flexible-closed-surface/scripts/ 下对应basename；f6两文件在同题 repro/source-root/topics/large-amplitude-twist-flex/scripts/。当前caller完整basename和生成身份均在[R573计划](../notes/r573-live128-synthesis-product-projected-model-complete-source-plan.json)；它们不是假定存在于Git主树的展开源文件。

原 public_resume 为 exact_20261114_public_resume.py，13907 bytes，SHA-256 11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5。其实际ledger选择原78源码逐bytes/SHA恢复；旧代码中某些文件的raw modes上限为64，当前112通过原capacity loader的显式内存来源变换支付，不能把raw常量误判为当前不能运行112。

该loader为 exact_20261114_tail_capacity_loader.mjs，4499 bytes，SHA-256 07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395。它在真实Node24 --import下绑定三原constructor的raw SHA、唯一literal及实际加载后的变换身份，不修改源文件；本文不另造capacity变体。

## 602.2 已有的实际全列共享

### 602.2.1 当前backend不是旧逐方向有限trace

R573 client显式设置 VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND="fourier-root"、VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND="tangent"、COMPACT_POINT_CACHE_LIMIT="8"及真实MODE_CAPACITY。原36cf worker按此选择a47df工厂，并将返回函数安装到实际cell.engine；它不把同名backend自动映射成R466 finite-trace。

原tail_resumable_engine（4193 bytes / 1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8）只保原stable graph factory与accepted-trial recovery callback插入，不能被当作另一种局部Jacobian。R593记录的last=tangentPredictor、success更新和geometricAmplitudeWarm回退也已存在，不应再声称缺少跨H初猜复用。

### 602.2.2 每个RK field只求一次当前root

原205b的rhsWithJacobian先执行：

~~~javascript
const rt=base.root(state,profile,x),g=rt.g,
 derivative=base.rhs(state,profile,x,false,rt);
~~~

a47df的rhs用knownRoot??rootBase.root，并把同一rt传给originalSplit.rhs；5d77的rhs同样用knownRoot??base.root。这里真实提供了rt，所以这条原RHS不重复求root。原root可能在自己的Newton迭代上访问多个不同L；该必要工作不属于“每方向重复同一root”。

完整rt.e.rows、rt.e.B及geometry由该次实际root返回。新的R602不更改其计算、选择branch、tolerance或任何line trial。

### 602.2.3 六组角矩和Cholesky已经共享

205b在一个n角循环中，从同一rt.e.rows依原表达式形成FPm、FTm、CKm、CUm、CPm、bmM。之后组成完整right矩阵，再调用一次：

~~~javascript
const dL=solveMany(rt.e.B,right);
~~~

solveMany分配一份J×J的L，J=M+1=113；先按原i/j/k顺序做一次Cholesky。完整K=2M=224右端随后在同一L上逐列做forward/back substitution。不存在外层224列反复调用root或重新分解同一B的结构。

这不证明所求局部Jacobian等于128浮点程序导数。它只是确定当前formal model的真实实现；其原数学与误差责任继续保留。

### 602.2.4 当前轨迹已经批量推进全部列

717ac的field一次得到完整f，再形成完整dt=A*T。RK4的a/b/c/d各有自己当时的状态、T、profile和x，不能仅凭同一H就把四个field合并。每个field的所有224方向已经共同消费一个局部A。

R532保持同一个实际DN、cell、engine和profile函数引用，记录before/after身份；对每个n=0…575，构造该cell当前投影状态并调用一次flowStateWithJacobian。完整before-port226×224、after-port224×224、mean2×224及原primal/residual数组均写出。

R534的stages分支接收这六份真实数组，核完整形状和来源，逐有限binary64字做准确binary128表示lift。该分支没有执行旧paired stage C++，也没有再求一次当前stage轨迹。原owner入口的--matched-trace none、--final-stage-columns 0与真实deferred_current_model_handoff明确了这条执行分工；旧stage代码作为祖先保留不等于它已被执行。

### 602.2.5 本文没有排除所有偶然重复输入

不同RK点、不同cell、初始capture与最终owner投影状态可能在特定数据下碰巧相同；本文没有证明它们在当前实际调用中相同，也不新增跨这些点的cache。初始capture与最终投影模型通常是两个不同状态的责任。现有sharing事实足以排除“224方向每列重算一整条相同primal”这一具体前提，不产生更强的无重复工作命题。

## 602.3 真正保留的大循环及新调用位置

原717ac在每个field中从正零数组形成：

~~~javascript
for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
 const z=f.jacobian[i*Kdim+j];
 for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*t[j*Kdim+k];
}
~~~

这里size=K+2。每个field已取得的A和当前T是普通Float64Array；A完整为size×K，T完整同形，但原乘法只使用其前K行。两mean输出行属于A的全部size行，不能删除。

新[R602源](../computations/geometry_20261116_current_DN_input_support_fourier_product_flow.mjs)为5625 bytes / f37bee075251957649c9ee5dc25582fac5c17fc3d3b804219cb537abf35f24f0。它导入原R523 helper（6246 bytes / e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3），没有复制或修改helper。

新工厂仍导出createFourierRootSplitFluxEngine(options={})。它先真实调用原a47df工厂一次，直接取得其M、size及同一个rhsWithJacobian函数引用，保留原root、rhs、rk4、statistics和cusp wrapper。它不重新构造一套205b角表，不另求profile/root，也不执行原withJ closure后再重复一次。

只有替代的flow闭包内两处literal改变：

1. const f=rhsWithJacobian(s,p,x),dt=new Float64Array(size*Kdim);改成先原样取得f；
2. 原完整i/j/k乘积行改成completeInputSupportLinear(f.jacobian,t,size,Kdim,linearStatistics)，由helper分配完整dt。

原flow函数跨度1538 bytes，替代跨度1456 bytes；逐个逆替换这两处文字后与原跨度逐字一致。这是文本身份事实，没有通过运行生成数值对拍。其余完整source prefix负责真实依赖绑定和工厂导出。

原minA、minD、maxRootRelative表达式仍原序位于局部J之后、矩阵乘积之前。dt的分配现在在helper内，故若分配失败，其相对于这些纯局部诊断更新的瞬间可与旧源不同；本文明确不承诺资源中断前沿相同。

## 602.4 局部运算命题

令R=K+2，A为R×K，T为R×K，原只用T前K行。假设这些是原相容的普通数值typed arrays，调用期间无并发修改，输出和输入不别名；实际R532/current cell同步flow满足这一结构。helper先读A全部RK项和实际使用的T前K²项。

若任一被使用输入非有限，执行原完整三循环，不拒收该输入，不把部分索引应用到原计算，也不插入新的finite-output门。扫描仅决定实现分支。

若全部被使用输入有限，helper保存每行实际非零支撑：

$$
S_j=\{k:0\le k<K,\ T_{jk}\ne0\}.
\tag{602.1}
$$

正零、负零均被判为零；任意非零次正常词保留。每次field重新形成该地址表，不缓存数值，不按容差删项，不依赖零H或预定分块。

**命题602.1。** 在上述输入条件下，新乘积正常返回时，非有限输入走原完整循环；合格分支的每个最终有限输出词与原乘积相同，非有限输出的正无穷/负无穷/NaN分类相同。所有R×K槽和两mean输出行完整保留；不声明NaN payload、浮点状态标志或整个运行轨迹同词。

**证明。** 固定一个输出槽(i,k)。原从+0开始，按j递推：

$$
p_j=\operatorname{RN}_{64}(A_{ij}T_{jk}),\qquad
x_{j+1}=\operatorname{RN}_{64}(x_j+p_j).
\tag{602.2}
$$

合格分支只省Aij=0或Tjk=0的项。它们的另一因子真实有限，因此被省乘积只能为±0，不能是0×Infinity或0×NaN。每个保留项仍计算原乘后加，原j序不变；不同k输出槽互不别名。

原累计器从+0开始，在有限期间不会成为−0。任意两个有限binary64数均是最小次正常量的整数倍，准确非零和不能处在0与最小次正常之间；准确抵消在RN下为+0，+0加−0也为+0。因此删除±0加项不改有限累计字。

非零输入形成的乘积即使下溢为−0，仍被原样执行。有限输入也不保证乘积或累加有限：首次overflow或NaN发生在相同保留项，之前累计字相同；随后零加项不改变无穷符号或NaN分类，且全部非零项仍原序执行。非有限状态不能由再加原乘积恢复为有限，故末分类相同；NaN编码不在承诺内。原完整fallback则直接执行原正文。证毕。

这使用了[R523](R523-actual-tangent-row-support-and-complete-linear-products.md)已证明的同一个helper，不重定义其算术规则。新接点的责任在于确定实际A/T、原循环、调用环境与原输出完整性，均在本节逐项给出。

## 602.5 原调度和完整flow的保留

下列原717ac代码全部保原字：

- stepsPerSegment??64；
- Float64Array.from(initial)及完整tangent正零数组、前K对角1；
- 原profiles顺序、integrationBreakpoints、integrationGrid(steps,cuts)、去重/排序后的原grid；
- 无cut时ordinaryH=1/steps，原x=n*ordinaryH；
- 原a→ab→b→bc→c→cd→d调用和每个h/2、x+h/2、x+h；
- 原state与tangent的四项RK组合，包括乘法与除法括号；
- 全部size状态与size*K切向槽、shapeDimension、minA/minD/maxRootRelative返回。

R523另一flow的splitIntegrationInterval和noJ-capture/replay逻辑没有移入。R466/R471有限root-trace代码没有被导入。原局部Jacobian仍为205b的同一个函数对象，variationalEvaluation仍继承其原Fourier-product范围；新linearEvaluation才明确标注R602。

noJ路径仍使用原a47df的rhs/rk4以及原cuspAware wrapper。这里没有因noJ名称删除内部初始化、predictor、两mean或完整局部J责任。是否由特定上游调用withJ完全沿实际调用者，未另添门。

对共同完成且中间相关值均有限的同一flow，命题602.1可沿原RK调用顺序逐field归纳，得到相同有限state/tangent及原诊断值。若途中出现NaN、资源异常、内存分配失败、时钟到期或其它异常，只保原局部分类与无吞错事实；不把局部命题扩大为全程序同异常文本、同停止地址或同resource frontier。

## 602.6 真实统计与中断

每个新工厂产生一个独立linearInputSupportStatistics，整个engine生命周期使用该对象；原statistics对象保持原引用，不覆盖root/RHS计数。该对象的完整14计数为：

| 名称 | 实际含义 |
|---|---|
| calls_started | helper已进入并完成输出分配后的调用数 |
| calls_completed | helper正常返回的调用数 |
| finite_input_calls | 完整实际资格通过的调用数 |
| original_complete_loop_calls | 实际选择原完整fallback的调用数 |
| actual_A_entries_checked | 已实际检查的A输入数 |
| actual_used_T_entries_checked | 已实际检查的T前K²输入数 |
| zero_j_terms_skipped | 实际零Aij导致跳过的j段 |
| scalar_products_skipped | 两类真实省略乘积总数 |
| retained_j_terms_completed | 非零A段的全部保留支撑循环已返回数 |
| actual_nonzero_T_words_indexed | 已实际索引的非零T字数 |
| actual_zero_T_words_seen | 已实际见到的零T字数 |
| T_rows_indexed | 完整索引的T行数 |
| zero_T_products_skipped_after_nonzero_A | 非零A段内实际零T乘积省略数 |
| retained_scalar_products_completed | 完整返回支撑段中的保留乘积数 |

fallback_reason_counts、schema、全部scope布尔和full last_observation一并保留，不能只传14数而删last或资格null。资格尚未判定、已判非有限、完整合格分别为null/false/true。

原helper对合格段只在其完整内层返回后提交保留项数；中断记录当前i/j、支撑大小及内部k未逐项记录，不伪造精确k前缀。原fallback也没有逐k observer。错误和ResourceStop不被此组件捕获重试；分配失败同样向上传递。未完成地址只能按真实last和外层原stage/partial/suffix解释。

linearInputSupportSourceBinding保当前source、原helper、原工厂、原flow祖先、205b及原grid的真实路径、bytes/SHA。它声明的是实际来源，不证明本次任何算术已执行。旧statistics与这些新字段应由后续R603真实reader完整消费；本组件未修改已跑240、227、243或任何现有reader。

## 602.7 成本范围与不能宣称的收益

设A第j列的实际非零数为a_j，s_j=|S_j|。原每次field完整乘积项数为RK²，新合格分支实际保留项数为：

$$
\sum_{j=0}^{K-1}a_js_j.
\tag{602.3}
$$

这只是乘后加的实际条数，不是运行时间。新实现还做完整A/T扫描、R×K选择循环和地址索引/分配；稠密T时可能没有可观收益。资源时钟不延长，原输出finite门和所有数学门不改变，完成前沿可能不同。

如果原T某次实际具有很多零，这是本调用真实扫描确认的事实，而不是从零H、旧run计数或理论分块补定。若本调用稠密，也保全部非零项。本文不调用benchmark、不预填速度、不少算列，不把旧root/Cholesky共享作为新增收益。

## 602.8 当前交付与实际后继边界

本次交付一个独立小工厂、本文完整条件说明和接口。已刊R523 helper及原数值源均不复制不修改。发布该组件不等于实际worker已经选择它。

后继R603必须真实将当前fourier-root factory导入注册成新source，保原backend含义、原capacity loader与source ledger；实际engine/model/current_call/必要reader保新source及完整统计。初始capture和owner后同DN模型须一致使用所记录的真实engine，不能只在report改标签。原576、全部226×224与两mean、原338×112、原FD/fullDN/所有cap及samecall128 authority均保持。

任何正在跑的run都保持原source，不能将其结果归给R602。组件没有request、workflow或新run，也没有新增科学验收条件。

## 602.9 来源链接

- [R573完整当前计划](../notes/r573-live128-synthesis-product-projected-model-complete-source-plan.json)及[当前请求](../computations/public-live128-root-synthesis-product-projected-model-original-full112-FD-fullDN-request.json)：真实caller、source map和原资源合同。
- [原717ac flow固定源码](https://github.com/Rogerhu12/math-research-public/blob/bce880e0037870ce0977abc5d54d0cf2bd24d2cd/topics/visible-flexible-closed-surface/scripts/78718-tail-fourier-product-flow.mjs)和[205b局部J](https://github.com/Rogerhu12/math-research-public/blob/bce880e0037870ce0977abc5d54d0cf2bd24d2cd/topics/visible-flexible-closed-surface/scripts/78718-tail-fourier-product-jacobian.mjs)。
- [原a47df工厂](https://github.com/Rogerhu12/math-research-public/blob/bce880e0037870ce0977abc5d54d0cf2bd24d2cd/topics/visible-flexible-closed-surface/scripts/78718-tail-fourier-root-split-engine.mjs)和[原knownRoot RHS](https://github.com/Rogerhu12/math-research-public/blob/bce880e0037870ce0977abc5d54d0cf2bd24d2cd/topics/visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_momentum_split_flux.mjs)。
- [R523完整helper命题](R523-actual-tangent-row-support-and-complete-linear-products.md)及其[实际接口](../notes/2026-11-16-finite-trace-actual-input-support-interface.md)。
- [R574实际240终态范围](R574-actual240-source-and-science-readback-overflow.md)：本次源码研究未借未返回的科学正文补推实际数值。
