# R531 — 同次当前完整 576 段切向流的真实工作线程分派

作者：ChatGPT / amplitude（AI-assisted）  
日期：2026-11-16  
可信度：**已证明，限本文明确的来源组合、成功路径与条件命题；新并行程序尚未在 Actions 执行。** 本文没有实际并行耗时、数值完成、native 接受、full-DN 接受或闭面结论。

## 1. 对象与来源

本次对象是已刊 R524 / request224 的完整 binary64 流。其公开入口为 498c03a7753a6f6caf66b563b2319cd42a447aaf；官方实际运行使用 23176ac678ea92882fa38ec6ddcc09e98742ac89。R531 不更改该运行，不读取运行中日志，不从其尚未返回的场、J 或检查点取初值。

[R475](R475-actual211-zero-height-complete-positive-height-accepted-and-resource-partial.md) 的实际正高度首轮完整 J 耗时是本次工作的动机；本文不把该总时长分解为未经记录的 root、线性乘法、profile 或 I/O 比例，也不由工作量推算加速倍数。具体计算对象继续采用 [R465](R465-recorded-factor-backsolve-defect-and-complete-column-contraction.md)、[R471](R471-zero-nonlinear-split-flux-finite-trace-fast-path.md) 与 [R523](R523-actual-tangent-row-support-and-complete-linear-products.md) 的已声明范围。并行不把名义系数线性化升格为 IEEE 舍入映射导数、准确隐式根导数、邻域分支稳定证书或已付舍入误差界。

重要原源如下；完整八视图的旧/新字节、SHA、每项 before/after/count 在独立 JSON 计划中给出。

| 原对象 | SHA256 |
|---|---|
| 原 78718-tail-tangent-core.mjs | ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3 |
| 原 Fourier root | cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88 |
| 原 root split factory | a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372 |
| 原 cusp helper | b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f |
| 原 capacity loader | 07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395 |
| 实际 R523 loader | 208fae784a8922b0d2c1fd16b0740ea4580e6050f5989243942d0d40c75b7a7f |
| 实际 R523 flow | 14c691bec5ca228495027185ed642730d90d17ce65467ac76662c9407cd7d960 |
| R471 variation | d4f2f32b61c084a67615ebb26b88b62c7d18de06056f09f5f68f86efa0f143e0 |
| R523 实际 T 支撑 helper | e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3 |

原 stages=576、M=112、K=224、完整状态维数 K+2=226。它属于此有限固定 112 原生响应链，不是另一条准确连续十族 453→450 或 128-bit 组件链的自动优化。

## 2. 实际修改点

在实际 runtime core 的 evaluate 中只增加一次完整 withJ 分派，并将循环内的 withJ 取值改为该次返回的第 n 项：

- withJ=true：同次全部输入通过新 dispatcher 计算；原循环仍按 n=0,…,575 取结果。
- withJ=false：仍直接调用原 cellFlow(n,states[n+1],false)。
- 残差、除以尺度的绝对值、Math.max、minA/minD、远端 112 行及 cut 的 112 项均保留原循环和括号。
- 原 internal solve 中已有 R273 correction 调用替换保留。新增视图不再宣称整个 evaluate 的旧字节未变；分别记录旧/新完整函数文本与实际 SHA，并准确逆回两项 evaluate 改动及一项原 R273 改动。
- 原十次 noJ line search、初始化、切向 warm predictor、接受后的 recovery、末端 sensitivity、原有限差分行及 audit 不移走。
- 原 full112 入口、实际 client、height、system/QR、owner 和 reader 形成明确的新八视图。旧 224 来源完整保留，不重标为新程序。

数值源没有新增独立运行或影子求值。源绑定、尺寸与传输完整性检查只核正在消费的实际对象；它们不构成新的数值残差、秩、正性、FD 或接受条件。

## 3. 同次输入及 profile 调用责任

令本次 evaluate 的实际输入为

$$
\mathcal I=(H,\;s_0,\ldots,s_{576},\;\mathrm{target},\;\mathrm{scales},\;
\mathrm{cells},\;\mathrm{steps}),
$$

其中每个原 s_n 是 224 个 binary64 词。主线程为每段新建 226 个词的零数组，再原样复制 s_{n+1} 到前 224 项；两项初始 mean 保持原 +0。H 的完整原请求及原字节 SHA 仍在原 call 目录，本次不重新算 H；各次 evaluate 的序号不能冒充原 nonlinear iteration。

每段所需 profile 值从实际已构造的原对象读取，顺序严格是

$$
n,\quad\text{profile index},\quad k,\quad\text{cusp subindex},\quad a,b,c,d.
$$

保留 x=k/steps、h=1/steps；原 cusp helper 返回两个端点时保留 h，不用端点差替换；出现分段时保留 grid[j+1]−grid[j]。四次实际 profile 横坐标为 x、x+h/2、x+h/2、x+h，重复中点仍调用两次。没有用统一插值、数值中点或新 quadrature 代替原 profile。

这个顺序结论不能仅由四个几何数值推出。实际来源链为：

1. closing_recalibrated_tail.mjs 的 physicalCell.profile 从同一 e.point(x) 取 g,A,B,dA,dB，返回普通记录 r、drdx、logw、dlogwdx、oldR、oldDrdx、chi。
2. closing_weighted_tail.mjs 的已构造加权 integrand/总量及已冻校准值不随这次 root 调用修改。
3. closure_bounded_point_cache.mjs 对 point 的有限缓存只记录同一 x 的该原返回对象及 FIFO 状态；无数值统计计数参与后续分支。
4. 950f-tail-subdivision.mjs 的 profile wrapper 在原子区间做原 affine x 映射，再保原 h*drdx 与 h*dlogwdx。
5. 原 root.geometry 立即读取返回的普通字段并构造自己的 geometry；它不写回 profile 记录。known-root RHS 与 captured tangent 不再次调用 profile。

因此，对于完成全部段的路径，主线程真实 profile 调用次序、重复调用、命中/逐出顺序与最终该缓存状态均和原串行 evaluate 一致。这里使用的是所列固定来源没有 getter、时钟或外部状态写入的普通返回记录，**不对任意用户 callback、共享可变 profile 或任意缓存声称副作用等价**。

新的程序先完成这些 profile 读取，再分派昂贵段流；原串行程序在读取之间穿插 root/RK/J。这改变事件时间和中断前沿。若前期 profile、I/O 或资源失败，已多读的 profile 不能冒成已完成的 cellFlow，也不能说这是旧串行程序首先会遇到的数学失败。原始准备 journal 和全 576 地址在第一次 profile 调用前已落盘；未完成范围据真实记录返回。

## 4. 工作线程中的完整原计算

协调进程处于同一原 owner 的进程组和 session。它建立 2–4 个真实 worker_threads；每个实际原 engine 的编号 e 固定分到 e mod W。每个线程按原 n 序消费属于自己的段，engine 在该线程内持久保留。

每个线程依次加载原 capacity loader、实际 R523 loader，再导入原 root split factory。它不导入 tail_frozen_worker.mjs 或其它 stdin 协议循环。实际源完整 SHA、源码目录、模式容量以及已载入的 factory 方法源码身份均记录。线程用本次实际 M、spacing、quadrature、mu、orientation、projectionFloor、cuspAwareFlow 创建原 engine；原 engine 序号的后续调用逐键核同一选项值。

固定原工厂的数值状态由 immutable tables、这些选项、本次 state/profile/x 决定；root 的本路径 initial guess 参数仍 undefined，不借前段 L 热启动。可变统计只记录发生过的调用，不控制数值分支。因而 engine 在不同线程中重建不会改为另一个数学输入。

主线程送完整普通 profile 返回值和 Float64Array 词。线程每次 profile 回调核实际 x 与带中的 x 完全一致，再返回对应记录；所有 profile 带必须恰好消费完。调用的是原

    engine.flowStateWithJacobian(initial, profiles, {stepsPerSegment: steps})

而不是另写简化 RK。原每步先完成四次 primal root/RHS，然后由各次真实 tape 形成四个完整局部 J；不重算 root，不删初始化 J，不删两项 mean，不省列。R523 中每输出的 j 顺序、乘后加、finite-input 支撑选择及原非有限回退原字保留。

### 条件命题 A：完成段的值等价

固定同一 Node/硬件数值实现和上述实际字值；假设相关源加载、普通值传输及该段原计算均完整返回。在该段所有参与输出的数值词为有限的范围内，新旧该段每个原数值操作的操作数和顺序相同，故按原操作序归纳，每一步产生相同 binary64 词，包括符号零；最后完整 226 状态、226×224 tangent、minA、minD 相同。

这里没有将有限输入误写成中间量必有限。若出现 NaN/Inf，原分支与错误路径仍由原函数负责；不承诺跨 V8 序列化的 NaN payload 字节恒等，不将非有限分类等同于已付严格误差界。传输用 Node V8 ordinary-value/typed-array 序列化，不用 JSON decimal 重新组成科学数组，也不把 serialization byte 相同当数学相同的必要条件。

### 条件命题 B：完整 evaluate 的值等价

若全部 576 段按命题 A 完整返回，主线程逐 n 读取全状态与全 tangent，再使用原式

$$
\mathrm{out}_j=
\begin{cases} f_j,&j<M,\\ f_j/\mathrm{portRatio},&j\ge M,\end{cases}
\qquad
J_{ij}=T_{ij}/(i<M?1:\mathrm{portRatio}),
$$

及原两项 mean 相加 f_K+f_{K+1}。没有改写除法为乘倒数。之后原 evaluate 每项残差、norm、minA/minD 和边界 loop 继续原顺序，所以完整返回对象与旧串行对象在命题 A 的词等价范围内相同。

接着原 R273、十次 noJ 试步与其严格比较继续消费这个完整对象；此条件等价不删除任何原生当前 J、warm predictor、完整 FD、338×112 末响应或 audit 责任。资源时间可能令新旧到达不同位置，因此不推出整次受限运行的相同轨迹、接受次数或终态。

## 5. 原失败、未访与资源

分派先保存全部实际 stage/rawCell/rawSegment/engine/worker 地址。状态区分 unvisited、assigned_not_started、started_without_completed_return、completed、stage_error、interrupted_without_completed_return。assignment、准备 profile 或累计计数都不作 completed 推断。

若某个线程返回原段异常，停止给它之后的段继续分派，但其余线程可以完成更小 n 的未完成段。只有真实错误段 e 以前所有段均已 complete、并且 e 的异常确来自原 complete-cell-flow、匹配原 root 的五个固定数值错误字面且不带 source/transport/resource 标记时，才恢复该异常的完整原属性与 e 的地址，称为原段序的首个原错误。较大 n 可能已发生额外工作；它们仍按实际记录保留。五类错误是原 profile range、D/S/A、SPD、Newton line search 和 iteration limit。原函数内的内存分配错误或其它未分类异常不因发生在 flow 内就获得数学错误优先级；保完整原错误与地址，停止为未付，而不重试。

传输、线程启动、身份、容量、ENOSPC、外层信号、原资源时钟等错误不被当作数学拒绝，也不捕获后重新科学计算。中断的局部统计若没有返回，明确 last reported position/unknown，不从 profile 消费次数补 root、J 或线性乘法完成数。对于只完成准备而未分派的整次 evaluate，全部未访地址照样可列出。

主 Node 原 6144 MiB heap 选项不变。新线程每个显式 old-generation 上限至少 256 MiB，2≤W≤4，总 worker old-generation ceiling≤6144 MiB。**这个额外 worker 额度不包括仍存在的主进程 heap，不是总 RSS 或 ArrayBuffer 上限，也不是把原 6144 MiB 重新划分后宣称总内存不变。** 需要的 profile 带、消息副本、完整 J 和文件占用均为新实际资源成本；本文没有峰值内存或磁盘可行性结果。

同一原 Python owner 只设一次 18000 秒 deadline；新 client、父/协调进程和线程继承该值。新检查采用与原 R471 resourceCheck 相同的 Linux monotonic 约定；原 R273 已有 UNIX 截止副本也照实际 source receipt 保存。启动线程、profile 准备、等待、I/O、完整计算均不会刷新该科学截止。退出后的短暂 transport/quiet 等待没有变成额外科学时段。

## 6. 生命周期与必要读回

父进程记录实际 child PID、PPID、PGID、SID、/proc start ticks。协调进程验证同一原 owner 和原进程组；worker thread_id 属于该实际进程，不被当成可另发进程信号的 PID。协调进程监测原父 PID/start ticks 和原 deadline。

正常 close、信号、资源或源/传输错误均尝试停止所有实际线程；metadata 写失败仍进入 terminate 路径。若 thread exit 不可确认，不能生成已 quiet 的科学结论。父 close 的 Z/X 观察只表示该进程没有运行中的 JavaScript 线程，不冒父已完成 reap。原 owner finally 及必要 reader 的同 boot/PID/startticks/session/group 规则仍在之后完整执行；未知归属、未静止或读回失败均保留 raw。

统计分成：

- 原 main engine：原初始化、noJ、端点/audit 等实际发生的调用；
- worker engine：本程序完整 withJ 段流的累计原 R466/R471/R523 统计、全部 14 个线性计数、fallback/scopes/last_observation 和真实 last reported 位置。

没有把两组相加冒成旧单实例统计，也没有把事件数量当运行时间。每个实际 evaluation 的完整地址、状态、错误、parent consumed 与原输入/结果身份进入选定必要域；大状态、完整 J、完整 RK tape 和完整成功 payload 清单只保身份与原临时位置，不全文返回。

新 reader helper 先读所有实际 journal 字节，再只对已经命名的语义域做全值/全类型相等共享：地址、context、来源、状态、准备 trace、engine 元数据与三类完整统计。缺键不等于 null，bool/int/float/负零不混同，原行索引与全部原地址保留。主 reader 仍使用原错误文本选择规则，不声称所有 traceback 全文返回。完整成功事件的每个 timestamp/payload 路径留在已读原 journal，不纳入新的逐事件正文。

它只附加到原一份必要正文；原 ASCII 90000-byte 上限、超限返回 70、无成功 marker、raw 留存规则不变。不拆分、不做任意数字或对象编码，不根据未来容量删必要计数；也不保证任意长运行都能在 90KB 内。完整必要读回和 actual quiet 均成功之前，不清任何本程序 raw。

## 7. 来源生成与后续实际调用

四个小公开源为 dispatcher、pool、metadata helper、literal generator。八个视图为 system、QR、hook、client、height、full112、owner、necessary reader。只有公开小源、完整 literal 计划和本文/接口入 Git；八个展开文本仅在 Actions 同一实际 computations/HERE 中形成。

原 224 的 181 项来源保持，新增四公开源和八临时视图，实际并集 193。旧 31 项 generated 源须由原计划在新 job 真正生成，不能当成 Git 现成文件。generator 每个 base 核全 bytes/SHA、每个 literal 核准确次数、每个完整 output 核新 bytes/SHA；源模块不导入、不编译。这个文本生成绑定不是独立数学测试。

实际新 owner 同时核原 224 子合同 receipt 和新 R531 receipt。它用新 full112/client 文件与 SHA；新 reader quiet 也绑定该新 owner basename。旧 224 request/recipe 的全文是明确的数值/来源祖先，不能把其中旧 client 名字说成当前实际执行源。当前实际源由新 PINS、spec、receipt、owner 及 complete source identities 决定。原数值配方、六参数、lambda=0.001、全部门和原时钟逐字保留。

本文未建立 request227/workflow，也未派发任何实验。将来的完整入口必须实际声明 worker 数和每线程 heap、原 request/recipe 子合同、新 plan/receipt、新 owner/reader/marker，并沿原 rules、单90KB和quiet/cleanup接入。不能仅运行旧 224 owner 而声称它自动选择了新 driver。

## 8. 已付与仍未付

已付的是：完整段输入的独立性条件、实际 profile 顺序与固定源缓存责任、全部段成功时的原序归并、真实 source view/owner/reader 调用链，以及失败/资源/必要表示的明确范围。未付的是：新线程真实启动、性能、容量、任何新数值输出、完整响应/FD/full-DN/audit 通过、误差证书及无限维或闭面任务完成。

本地只做文本/JSON/字节/SHA和 literal source 构造；没有导入、AST、编译、科学算例、fixture 或 benchmark。未来公开 Actions 正常运行即承担实际执行，不再添加一个独立审查或小测试作为数学前门。

## 9. 运行时接口依据

[Node 24.22.1 worker_threads](https://nodejs.org/download/release/v24.22.1/docs/api/worker_threads.html) 说明 worker 的消息克隆、显式 execArgv、resourceLimits 和 terminate/exit；[Node V8 serialization](https://nodejs.org/download/release/v24.22.1/docs/api/v8.html#serialization-api) 说明普通值与 typed-array 的序列化。源码据此使用独立协调进程，避免同步等待的主事件循环阻止工作线程消息/错误处理；协调进程显式关闭继承 NODE_OPTIONS，不把主 V8 heap CLI 选项重新传给线程。JS heap 限额不覆盖外部 ArrayBuffer/RSS，已在 §5 分列。文档提供运行时 API 合同，不代替实际此次程序执行证据。
