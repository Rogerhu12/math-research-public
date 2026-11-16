# R534：同次 binary128 owner、原 DN 的完整 binary64 线性模型与原非线性接受条件

可信度：**已证明，限下述来源、完整返回及有限算术条件命题。** 同时给出可执行的独立源码组合；本节没有执行科学代码，没有创建 request229，没有实际 owner、stage、FD、fullDN 或闭场结果。

## 534.1 本节承担的责任

R529 已经说明：用一个近似线性模型构造候选方向，与用原非线性问题的实际值、残差、独立回放和末端检查决定接受，是不同的责任。其条件结论不要求线性模型先被证明等于准确导数。本节将该结论接到真实程序对象，而不重新证明 R529 的全部接受理论。

基线为 R527/request225 的实际 11 个派生 caller 和 R522 的完整组件。R515 的物理径向缓存继续由该原组件使用。新增的投影及同 DN stage 库是已刊 R532 的两件原字节。R535 的 owner primal 缓存不在本组合内，也不自动加入。

真正的操作顺序为：原当前 H 的 snapshot 和原 R273 方向形成原初猜；实际 persistent binary128 owner 及独立 fresh replay 返回；只在其原完成和容差条件成立后，投影同次完整状态；仍在原 Node 进程的同一个 dn 对象上形成全部 stage 的 binary64 模型；准确提升这些有限字到 binary128 表示；再运行全 boundary、全 endpoint、独立 audit 和原响应组装。旧同步 post-stage 不先执行一遍。

所有权威 primal 值仍来自该次 binary128 owner 及其实际物理后处理。投影状态、投影点的 primal 诊断和 binary64 Jacobian 均不成为一个新的已收敛状态。若 owner 尚未到达原容差或独立回放未完，本方案保留其实际停止记录并不启动模型阶段。特别地，实际 R509 的早期 owner 资源停止不是本节已经解决的问题。

## 534.2 不覆盖原来源的生成关系

本节只刊一个标准库源码生成器和两个完整字面计划；展开的 13 个新源只在 Actions 的真实 computations 目录生成。每一个计划条目记录原文件名、完整 bytes/SHA、字面 before/after、精确出现次数和新文件的完整 bytes/SHA。生成器先恢复已刊 request225 的全部实际源，再在内存形成所有本节目标文本，最后以独占创建方式写入新的 basename。原文件不覆盖。

有限来源集合的实际并集为

$$
342+14+2+1+13=372.
$$

这里依次是原 225 的 public 源、原 225 的生成源、两件 R532 库、本节生成器和 13 个新 view。此等式只描述列出的实际来源集合；不将它误写成对未列动态 import 的自动证明。原 14 个生成源继续作为逐字祖先保留，新完整 source map 同时记录原 14 件和新 13 件。

两个计划分开承载不同角色，均小于单文件 100 KB：

| 计划 | 实际角色 |
|---|---|
| core plan | boundary、owner、components、assembly、current_call |
| complete plan | system、QR、pipeline、worker、client、fullDN、owned runner、necessary reader，并绑定 core plan |

原源的数值主体只在本节明确列出的地方发生变化。源码准备不调用 root、RHS、RK、J、求解器、编译器或科学计时起点。它是可再生源码的生成，不是科学预检试验。失败时保存实际错误和尚未生成的角色后缀；已有输出不冒完整 source map。

## 534.3 先真实返回 owner，再移交后处理

新 owner 保留实际 225 build_view 和 source_scope 对原 persistent128 程序的构造。进入本次私有 scope 后，核明其原 _precleanup_final_components 确为被声明的原 hook，再把这一私有入口换为本节显式的 deferred_current_model_handoff。它不修改已刊源、不修改全局共享模块，也不改变 persistent128 数值 main、原 line search、原容差和独立 fresh replay。

新 hook 的唯一职责是保存同次 precleanup owner summary 和原完整状态的真实身份。它如实记录原四个 post component 尚未执行。不存在把 deferred 写成四项成功的路径。原同步 owner 退出、完整原 raw 保留及源记录继续执行。

后继消费至少绑定以下实际事实：

1. owner summary 的原 native-persistent128 schema、实际 owner Python 源和原 persistent CPP 源；
2. 本 run 的 repository、run id、attempt、source commit；
3. actual_call_identity 中的 native_call、snapshot 身份及完整 physical-height 数组身份；
4. 原 packet、packet binding、全部 $577\times224$ binary128 state 字；
5. 实际 final complete、原 below_original_tolerance 以及 independent_fresh_replay_complete；
6. 同一次保存的 state 文件、hand-off 和 summary 的真实 bytes/SHA。

这些条件原本决定该 owner 是否具备后继输入。新程序没有以一个较松 residual、旧响应或仅有 SHA 的占位文件替代。若条件不成立，当前模型和响应保持未付。

## 534.4 一次 RN64 投影的准确对象

R532 的 Python 绑定库直接接受本节实际四件 owner/client/current_call/worker 来源及其明确 schema，不借旧组件专用的 load_projection 函数。这样既保全原 R493 的逐字 RN64 投影实现，又不把本节新 caller 冒充 R493 原 caller。

设实际 owner 返回的完整状态为 $Y^{128}$，本节形成

$$
\widehat Y=\operatorname{RN}_{64}(Y^{128}),
\qquad
\widehat Y\in(\mathbb F_{64})^{577\times224}.
$$

投影包括所有节点、所有 Q 和 Pi 分量及有符号零。投影结果有完整原件、形状、顺序和字节身份；响应组装消费同一份投影，不能在后面另选历史点或重新投影一个不同状态。

RN64 的用途是确定线性模型的求值点。除非另付误差证明，本节不声称 $\widehat Y$ 满足原 binary128 方程，也不声称它与 $Y^{128}$ 的导数完全相同。投影误差、binary64 运算误差和模型质量仍是 R529 所说明的模型责任，原非线性接受条件不被这种来源绑定替代。

## 534.5 同一个 dn 对象、全 576 段与两条 mean

R532 Node 库拿到的 dn 就是当前 worker 已加载、用于该次真实请求的对象。实际 profiles、cusp 分割、steps、完整配置、当前 H 和 snapshot 都在同一上下文中绑定。本节没有从只含旧 checkpoint 的另一个进程重建一个貌似相同的 dn。

对每一段 $n=0,\ldots,575$，库实际调用该段的 engine.flowStateWithJacobian。初始完整局部状态有 226 个槽：前 224 个为该节点的投影 Q/Pi，另两个为该局部流的 mean 累计槽。局部变分使用全部 224 列，不丢任一频率、不只取对角块、不复用原 snapshot 中的 J。

原 core.cellFlow wrapper 对返回 tangent 截去两条 mean 的行为不是本库的输出界限。本库直接读取真实 engine 返回值，分别保存：

- port 之前的完整 $226\times224$ tangent；
- port 之后的完整 $224\times224$ 状态映射；
- 两条 $2\times224$ mean tangent；
- 相应完整 primal 状态、port 后状态及 mean 诊断。

Pi 的 port 变换使用该段实际 portRatio，位置和顺序沿原 core。新库还绑定当前下一节点用于完整诊断，但这些 binary64 primal 诊断不是 owner 的权威 binary128 值。

因此，本节对完整性的声明包含 mean、全部列和 port 的实际变换。它不把仅有 $224\times224$ 切片的返回重新命名为完整 $226\times224$ 输出。

## 534.6 有限 binary64 字准确提升到 binary128

模型输出保存为 little-endian binary64 raw。新组件逐字读取并只用整数位操作提升到 little-endian binary128；没有经 Python float 或十进制文本再次舍入。

设输入符号位为 $s$，11 位指数域为 $e$，52 位小数域为 $f$。对 $1\le e\le2046$，

$$
x=(-1)^s(1+f2^{-52})2^{e-1023}.
$$

输出的指数域取 $e+15360$，112 位小数域取 $f2^{60}$，于是减去 binary128 偏置 16383 后指数仍为 $e-1023$，小数仍为 $f2^{-52}$。因此该映射表示同一个实数。

对 $e=0,f>0$，令 $\ell=\lfloor\log_2 f\rfloor$，则

$$
x=(-1)^s f2^{-1074}
 =(-1)^s\left(1+(f-2^\ell)2^{-\ell}\right)2^{\ell-1074}.
$$

输出指数域为 $\ell-1074+16383$，小数域为 $(f-2^\ell)2^{112-\ell}$。binary64 的最小正次正规数仍处在 binary128 正规范围内，因此此步骤没有下溢或舍入。

对 $e=f=0$，输出仅保留原符号位，故正零和负零逐位区分。对 $e=2047$，输入为 NaN 或无穷，程序如实拒绝当前模型的有限提升，而非把它变成零、null 或一个有限默认值。

由此，对每一个实际有限输出字，提升是准确嵌入 $\mathbb F_{64}\hookrightarrow\mathbb F_{128}$。该命题证明的是字的表示准确性，不把一个 binary64 近似导数变成准确导数。

## 534.7 全数组完成条件和中断地址

六类数组均按实际 stage、shape、row 顺序读取并提升。原 bytes/SHA、实际 raw 文件、完整列数、输出 bytes/SHA 和提升后的目录全部绑定。只有所有 576 段、每种所需数组、每行每列完整返回后，stage component 才能声明 scientific_complete。

任何错误或资源停止都保存当前 stage、数组、字位置以及完整未访后缀。一个已经写出前缀的大文件不因为其存在或 SHA 可得而被称作完整矩阵。源库在被强制中止前未能写出的 completion 标记也不会由后继猜补。

完整 binary64 模型 raw 的理论字节数为 469656576，全部准确提升输出的理论字节数为 939313152；这是既定维数的文件容量合同，并非本节已经生成了这些数据。两份表示在同一 Actions 任务中保留给真实下游，既不入 Git，也不通过 necessary 文本分包回传。

## 534.8 同一原绝对钟与同步 Node 流的外部守卫

本节不重开原 19200 秒科学总钟。原 120 秒收尾预留及各 cap 保持：owner 6000、fresh replay 1200、stage 8000、boundary 600、endpoint 600、audit 1800；原 factor cap 和全部线程资源亦沿原合同。

模型窗口在 owner 已真实返回之后建立，其终点取原 job deadline 剩余时间和原 stage allowance 的交集，并按原规则保留下游 audit 与收尾费用。一次投影、全部 576 段 binary64 flow 和全部准确提升共同使用这个窗口。投影完毕、每段完成或提升开始都不能重置 8000 秒。

原同步 Node 调用可能长时间停留在单个 engine flow 内，单靠 JavaScript 段间检查不能在段内响应截止。因此新 caller 启动一个独立 Python guard，使用原 owned-process helper 登记真实 pid、pgid、sid、uid、start ticks 和本 namespace。Node 必须观察 guard 的真实 ready 后才开始模型计算。

guard 在模型 deadline 到达时对已登记的真实 worker 进程组实施原 TERM→KILL 关闭次序。正常结束则通过真实 stop 记录和 wait/reap 收回 guard。完整 command、来源、deadline、ready、exit、signal、stderr、reaped 和 timeout 进入必要读回。没有裸的无钟第二条模型执行路径。

来源或 guard 生命周期错误会使当前模型保持未付，并阻止 boundary/endpoint/响应接受。若原请求要求独立 audit，且该独立分支仍有原预算，它仍可如实执行并单独记录；audit 成功不能补齐失败的模型矩阵。原 worker namespace 的 quiet 检查显式纳入新 guard 登记地址。

## 534.9 boundary 数值主体与模型名称

新 boundary 源沿原 c218 的全部数值主体：完整薄 QR、全部 112 个边界输入列、原 cut/far 条件、forcing 和两 mean 的传播保持。输入的 stage 数组由本节真实完整模型供给。

旧源头注释和旧 R273_or_fixed64_used=false 标记不适合这条实际路径。本节使用独立 source/schema，并显式记录使用 current-owner-projected64 model、未复用旧 R273 矩阵。不能仅更改一个数组文件却继续返回旧的“没有 fixed64”来源声明。

准确 lift 后的矩阵元素能被原 binary128 boundary 程序无损读取；其后的 QR、回代和端口运算仍由该实际 binary128 程序执行。由于矩阵来自投影点的 finite64 模型，本节不声明这些运算等于在 owner 点上重算的全部 binary128 tangent，也不以这种相等作为新增科学门。

## 534.10 五个原物理源码的实际输入目录

文本追踪发现一个独立的来源路径问题。原 physical packet exporter 接收的是 sourceReceipts；原 ddbe 组件则对其中每一项用 original_source_root 加相对文件名打开文件，并要求五个 ORIGINAL_PHYSICAL 来源。因此，把 HERE 中整个 session 的 basename 列表直接交给另一个 restored root，不会自动给出这五个真实数学文件。

本节在每次 call 的新 physical-source-inputs 目录创建五个逐字副本：

| 原文件 | 原实际位置 | 原 SHA256 |
|---|---|---|
| 78718-tail-tangent-core.mjs | original_source_topic/scripts | ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3 |
| f6tail_momentum_physical_jets.mjs | original_source_root/topics/large-amplitude-twist-flex/scripts | 2b96df25211c5d6ebfc7faf689ea7035704bf0bf7c1ea3aa50b1c137fbe39ea8 |
| f6tail_actual_metric.mjs | 同上 | 36e4e642014d5afd733ed3fecc13267d23c40927e1bd2113e53abcdbb588dcb4 |
| f6tail_cusp_grid.mjs | 同上 | b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f |
| numerical-tail-slope-jacobian.mjs | 当前真实 HERE | 206d82d3b41e6b9ce24b26447a2026c19c1c7126765107c23d58e55da25639e2 |

每个原件先核完整 SHA，副本独占写入后再核 bytes/SHA。physical-source-input-binding 保存实际 call、原绝对路径、实际副本路径、完整身份和完成/部分状态。后继 --original-source-root 明确指向这个真实目录。原文件及 Git ref 不变。

这不是把整条 source closure 缩成五件。完整 session、snapshot、owner、worker、packet exporter 和 component 来源仍分别按原合同绑定。五件只是原物理 binder 明确消费的数学输入目录。

原 824b exporter 中 sourceReceipts 仅参与合法性检查和 binding 的来源字段；形成二进制数值 chunk 的代码不读此数组。原 dn、查询点、原 Fourier/FFT 字表、profiles、geometry/root/RHS/RK 函数身份及 audit schedule 均未因该路径修复而改变。给定同一个实际 dn 和相同调用参数，其 packet 数值生成次序和算术不变；binding 的来源文字与完整 SHA 则如实成为新值，不能冒旧 binding。

## 534.11 endpoint、独立 audit 与 338 行真实次序

新 components 保留原物理 binder 的完整 packet、call、owner 和状态检查；实际物理程序继续由 R515 的已刊径向缓存 qualifier 形成。该 qualifier 的数学责任与原 audit 独立，未替换为本节的 binary64 模型。

原 a090 endpoint 入口先读取完整 G，随后形成 base 与响应。本节没有将这个入口误作一个无需 G 的 noJ base producer。真实 $338\times112$ 端点响应按以下顺序输出：

$$
\bigl[
\operatorname{slope}_{112},\
\operatorname{second}_{112},\
\operatorname{meanSlopeCorrection},\
\operatorname{meanSecondCorrection},\
\operatorname{height}_{112}
\bigr].
$$

完整 13 个端点标量、原两个 mean 条件和按请求执行的独立原 C 物理 audit 均继续保留。不能用只读首 112 行的 AffineTail 行为解释为只需首 112 行完成。

响应 assembly 的来源分开记录：实际 owner 的 binary128 primal/final/replay；本节准确提升后的 stage 模型；完整 boundary；完整 mixed endpoint；独立 audit。它要求模型生命周期实际完成，并保留模型错误字段。任何一项缺失都不以另一个组件的 success 补上。

原当前 H 请求、原 affine FD、fullDN、BC、RMS 和 final fresh audit 仍由其原消费者实际执行。新响应只提供一个诚实标识的当前模型，不能自行给整条 BVP 或闭场授予接受。

## 534.12 组合条件命题

**命题。** 假设所有列明来源和输入均由实际同 run 字节绑定；原 owner 与独立回放真实满足原完成及容差条件；本节一次投影和全部 stage 模型在原窗口内完整返回；每个待提升字有限；全 boundary、endpoint、按请求的 audit 和响应组装均依上述真实数据完成。则新 caller 向原 fullDN 提供的是同次原 H 的实际 binary128 值和一个完整、来源可追溯的 projected64 线性模型；原 fullDN 对候选的非线性接受条件保持。

**证明。** 534.3 给出同次 owner、状态、H、run 和 replay 的唯一输入关联；534.4 确定模型点；534.5 给出全部 stage、列、mean 和 port 的实际调用；534.6–7 给出有限模型字向组件格式的准确完整嵌入；534.8 排除重开资源钟和未收回 guard 冒完整；534.9–11 给出真实模型标识、完整原物理输入和原末端消费者。因此传给原 fullDN 的值与模型各有明确来源，没有把 projected primal 代替 owner，也没有用缺行矩阵代替完整模型。原接受条件的保留再由 R529 的条件框架及本节未改的实际 fullDN 调用体得到。证毕。

命题不含模型足够好、必有下降方向、有限预算必完成、原 solver 必接受或误差达到机器精度的结论。模型差时，原 line search、域、FD、BC/RMS 或 final audit 可以如实拒绝；有限资源可以如实中断。本节不添加一个先验“模型准确度达到某数”的新 BVP 前门。

## 534.13 原必要读回、部分结果与清理

新 reader 保留原 225 必要范围，增加本节真正新出现的 owner-deferred、projection、model/lift、guard/window、物理源码输入目录及其错误/未访地址。它不把完整成功大数组转为文字。实际下游已经消费的 raw 仍保存在同 job 内，必要正文只携带约定的科学选择、完整身份和未付范围。

每次成功的 clock-check 序列可按明确的 stage 地址范围、次数、完整原顺序身份及实际 remaining 极值呈现；所有失败的检查和异常正文保留。若 stage 库在被关闭前没有完成其 result，不从目录已有文件推断已完成段数。

本节维持单份必要正文的 90000 bytes 限制。超限返回 70，保留原完整必要对象的 bytes/SHA 和临时路径，且不准 cleanup；不增限、不分包、不改成通用编码。源码准备有自己的明确非科学必要范围，不能被当成科学结果。

原 cleanup 同时要求实际读回、原规则范围和 namespace quiet。新 guard 也属于这一范围。未取得完整必要、未知 owner、未收回 child 或 cleanup 条件不满足时，raw 保持未清理。科学 partial 本身不被升格为成功；若其完整必要范围已真实读回且所有原清理条件成立，原 cleanup 仍可如实清理失败科学的自有临时目录，并返回实际 removed 记录。程序没有为了省磁盘而提前删除仍被 boundary/endpoint/audit 或 reader 消费的数组。

## 534.14 仍然未付的实际责任

本节交付的是完整 source/plan/接口与条件命题。request229/R542、实际229/R543仍是协调预留，没有本节的实际 run、owner末点、模型、FD 或接受数据。未来入口须真正下载/生成本表全部来源、绑定其实际 request 与原绝对钟，并使用新 schema、frame 和 reader；不能把原 request225 运行改名为229。

R509 已有的先行 owner6000资源停止、本组合在实际 runner 上的成本、完整模型的方向质量、fullDN 原接受、后继闭场与全域几何都仍须由各自真实调用支付。原19200与各 cap 未放大，R535 未自动混入。发布源码和数学证明不代表这些实际事项已经完成。

## 534.15 原依据与精确源码位置

- [R529：原 nonlinear gates 与当前 owner 投影模型](R529-current-owner128-complete64-model-and-original-nonlinear-gates.md)：线性模型和实际非线性接受的条件分责。
- R532 两库：geometry_20261116_live128_projected_stage_binding.py 与 geometry_20261116_live128_same_dn_projected_stages.mjs，完整最终身份在配套接口；同次来源、一次 RN64 和原 DN 直接 stage 输出。
- 原 geometry_20261115_native_final128_components.py 的 ORIGINAL_PHYSICAL、bind、validate_prior：同 owner/packet、五个原物理源和完整前置组件的真实要求。
- 原 geometry_20261115_native_final128_packet.mjs 的 writeNativeFinal128PhysicalPacket：全部 query/FFT/physical 字表及 source_receipts 的真实使用范围。
- 原 geometry_20261115_native_boundary128.cpp 与 geometry_20261115_native_physical_final128.cpp：完整边界、端点、mean、物理 audit 及其数组次序。
- 已刊 R527/request225 的 build_view/source_scope、current_call.runPipeline、完整 fullDN 与 R522/R515 组件：本节字面计划的实际祖先，原全文 identity 均列于两份计划。
- 本节两个 plan 和 generator：全部 13 个新源、精确 literal 变更次数、输出 SHA、完整来源并集及原钟/部分读回接线，配套接口给出可直接使用的 CLI 与所有真实文件名。
