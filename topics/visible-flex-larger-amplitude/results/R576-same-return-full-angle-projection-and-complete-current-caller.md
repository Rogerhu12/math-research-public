# R576：同次完整系数盒的全角投影缺陷，及 request241 的真实当前调用链

作者：OpenAI / ChatGPT geometry agent（AI）。日期：2026-11-16。  
可信度：**已证明（限本文的来源组合、覆盖传递和条件估计命题）；尚未运行本入口，没有实际接受父、数值界或收敛结论。**

## 576.1 本结论支付的责任

R575 已给出实际被投影的旋转柱坐标三分量在完整圆周上的 Fourier 尾和全部离散混叠界。其库只接受一个真实加载的 R553 完整前缀系数盒对象；独立库存在不等于当前计算已调用它。本结论把该库接到 R570 真实同次 cubic capture 后继的 same-C measurement 中，并沿原 cell 的分裂、退栈、资源中止和必要读回贯通。

当前入口是独立 request241。直接冻结祖先是 R591/request247，后者修正实际 captured239 第一 reader 的元数据身份。本文保留这项修正，保留全部 R570 的 56 个来源输出及其原数值正文，再产生一个 evidence 后继和六个具名 metadata 后继。普通全链中的原 metric、reach、held、显示及前三次 normal evidence 不因此变更。新增诊断实际进入的是重新计算同语义 C 后的 first/successors 两槽、三个 same-C measurement 和它们的 compare。

同时，来源生成的完整必要对象接已发表 R586 的具名关系表示。该对象在原全部选择完成之后才处理；仅完整关系表示严格更短时使用，否则整份保留原对象。此变化没有修改任何科学选择、科学对象或数值阈值。

本入口不声称会到达真 450，不声称预算必足，不把 finite program 成功等同连续等距解，也不把完整全角投影参考界称为实际浮点 FFT、插值、RHS 形成误差或全域 relative-metric floor。原科学接受条件一项不少；新增诊断未付不成为原 BVP、metric 或精化的拒收条件。

主要来源：

- [R575 完整柱坐标投影尾与全部 alias](R575-complete-cylindrical-projection-tail-and-alias-defect.md)，以及其 `geometry_20261116_same_evaluation_full_angle_projection_defect.py`。
- [R553 实际完整系数盒与 Frenet majorants](R553-actual-prefix-coefficient-tubes-and-Frenet-majorants.md)。
- [R570 同次实际 cubic、当前闭场和完整来源链](R570-actual-same-call-cubic-current-field-and-complete-source-chain.md)。
- [R591 实际 captured reader 来源修复](R591-actual-captured-reader-and-complete-source-chain-repair.md)。
- R586 的 [完整来源关系原库](../computations/root_20261116_complete_generation_source_relations.py)，直接使用其 `compose`/`canonical`；本文不另造一种通用对象编码。
- R489/R492/R495/R500/R504 支付的同 C 重新积分、准确 leaf/cut 和 tail 查询桥仍由真实原来源调用；本结论没有把其允许的语义包含偷换成某个新的 C realization。

## 576.2 实际对象与来源，不按旧家族名字猜绑定

新 evidence 是 `geometry_20261116_request241_same_C_projection_metric_evidence.py`，76200 字节，SHA256 `d0c91d08fa46d5bafaf69faa472780a492c3b84a7ba8adc7d9b2d10b2b72182f`。它的字面祖先是实际 R570 evidence：

`geometry_20261116_request239_same_C_cubic_metric_evidence.py`，69906 字节，SHA256 `dc03e07957d4983bd78b9299b79052c203a1e1da2dcbd75fee3a1aaf29562373`。

后继不重新派生 R570 的 head、leaf、field/cut bundle、tail query、three-family metric 源。原 actual_checkpoint、完整 definition、真实 nodal words、准确 C/root 语义、十控制词、材料 A/B、共同构造 W/H/全 marker、registration、R249 background 及所有原来源回执，仍由该实际祖先的加载链读取。本入口实际三层选择仍为 original112、resolution112、incrementalM；evidence 源同时保留原已注册的 completeM 兼容项，但本入口没有第四个计算层级，也未借此宣称新来源已自动注册。没有把原始 R504 四元组名直接用于当前 generated 源。

运行中先由原绑定生成 `self.prefix_tubes`，再将该**已加载对象本身**交给 R575：

```python
Projection, self.sources[PROJECTION_NAME] = load_source(
    actual_computations, PROJECTION_NAME, PROJECTION_SHA)
self.reference_projection = Projection.bind_loaded_projection_defect(
    self.prefix_tubes)
```

此处公共库固定为：

`geometry_20261116_same_evaluation_full_angle_projection_defect.py`，24673 字节，SHA256 `d2cfc1e35509486dd77f5f2ae4aecba3c0527b2e16b910be69540a73f3c2d6b7`。

原库实际检查 `sys.modules[type(prefix_tubes).__module__]`、模块真实路径和 SHA、schema，以及 `module.BoundPrefixTubes is type(prefix_tubes)`。这避免把重复加载同路径时的第一个模块对象当作实际 class owner。实际 R553 源固定 24412 字节、`81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b`；实际 R521 majorant 方法 owner 固定 18782 字节、`4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad`。M、N、physical_size 和全系数布局取当前对象，不靠外层 source 标签填写。

R575 还逐字绑定五个原 DFT/reference 源。原 public 闭包中已含 free_core_bvp 和 fft_frenet；另外三个旧 reference 源在本次显式加入 public pin：

|真实 basename|字节|SHA256|
|---|---:|---|
|alternative-outward-probe.py|7708|cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb|
|geometry_20261114_r225_outward_probe.py|7542|64a3fd482f6ee01f4d149971dff1212b2c2ca3bdb00f1b733c7b119b458bab5f|
|geometry_20261114_r225_high_core_bvp.py|18350|e12916dcf30dd2088ad59d2059647c8a03bed446aeee693b88f423730fa5a530|
|geometry_20261114_r225_free_core_bvp.py|23914|a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08|
|geometry_20261114_fft_frenet.py|2143|973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401|

这五个文件在此接点只作为原公式实现的完整源码字节读取。来源准备和 R575 binder 不导入、运行那些旧 probe，不启动旧实验，也不把旧 probe 的场或旧输出作为当前输入。实际场仍是当前 checkpoint 经既有完整加载链定义的准确场。

## 576.3 同次计算不变量

对原闭 cell $C$，`Measurement.base_once` 保留以下先后关系：

1. 用原 target/whole-query 桥得到同次准确 target record。
2. 用原准确场求六 jet，按原 relative operator norm 公式形成 Gram 与目标的区间比较。
3. 原 R553 `inspect(C, actual_prefix_tube_context)` 返回当前完整 coefficient tube、全频 angular box、同目标 scalar box 和正域责任。
4. 原 R570 同次 cubic/quintic 比较照常。
5. 把步骤 3 **已经返回的同一个对象**传给 R575 `inspect(C, record)`；不重算 target、场、C query 或系数重建。

新增返回保存在该原 cell 的 `actual_reference_angle_projection_defect`。它含原 cell、同次输入的准确身份、全部返回/未付原因，不取盒中心冒真值。

R575 要求：输入为真实 R553 cell schema，`original_cell` 与当前 cell 完全相同；physical_size 为 $3M+2$；radial/prefix_span 对应当前 piece；angular 地址闭区间属于 $[0,1]$；全频率列表恰为 $2,4,\ldots,2M$；A、mu、nu、P、W 和完整 d/e 来自同份实际记录。正域 A、mu、P 若未隔正，该诊断返回 available=false 及其原责任。不会因此删去当前 metric cell、改原 norm 结果或制造一个可接受父。

原 R553 是准确 quintic 的完整系数包围；原 R570 的 literal cubic 来自同次真正返回的 `sol.sol.c`。本文没有把两者认作相同多项式，也没有通过改 source 名或复述 Hermite 节点消除它们的差。已修正的 rho 归一化、物理角到材料图的 Gram 比较仍在 R569/R570 自己的责任范围内；R575 本次返回的是物理角下完整三分量速度缺陷，量纲不同，不把它直接当 relative metric error。

### 命题 576.3：同次观察保持原场、目标和数值判定

若原 measurement 在某 cell 上按其真实来源得到 target、场值及 R553 返回，则新 evidence 在该 cell 的 R575 输入恰为上述 R553 返回；它不修改原场、目标、Gram、norm、原 split 条件、原 lower/upper 更新或父接受记录。

**证明。** 源差异只新增 binder、读取已返对象的观察、原 retirement 处的统计和必要字段。原 `base_once` 中 target/evaluate/norm 表达式、原 `base_measure` 的 norm_width/max_depth 决定以及原 cell 分裂均不替换；`projection_cell` 返回独立字段。R575 只从实际对象和同次输入读取有理盒及原公式常数，不写这些对象的数值定义。因此只要原调用已发生，新增观察既不能改变它的数学输入，也不能把不同 cell 或不同加载模块冒为同一个返回。资源消耗可能使原绝对钟更早耗尽，这一点不作性能不变承诺。证毕。

## 576.4 原闭域、退栈和未访责任

原 DFS 决定 `refine` 后、向原完整 cell ledger 提交记录之前，新增：

```python
record["actual_reference_angle_projection_retirement"] = (
    self.projection_retirement(
        cell,
        report.get("actual_reference_angle_projection_defect"),
        refine))
```

内部仅对原 prefix 调用：

```python
self.reference_projection.commit_original_retirement(
    cell, diagnostic, split=refine)
```

没有第二份 root plan，没有新的角网格，也没有由诊断自行 pop、split 或退休一个 cell。原所有 prefix piece、全角闭端点、两反射片、共用 seam 与原 DFS 尚未访问后缀保持。tail/collar/cut-patch/cap 的原完整 metric 责任也保持；R575 对这些非 prefix piece 不宣称系数参考投影界。

若中止发生在新增观察内，原 ResourceStop、MemoryError 继续走原 measurement 资源通路。尚未提交的当前 cell 仍归原 frontier；不得把它计成完整 terminal leaf。已经提交的 cell 在原 gzip ledger 保留实际 R553 输入、R575 返回与原 retirement。摘要只给该完整原件身份及原 coverage/frontier 责任，不声称所有 ledger 行已经回传。

R575 的原 summary 直接读取同一个 R553 对象的退休计数。全局 flag 至少要求：

- 原 R553 的完整 prefix constant cover 为真；
- observed、committed、split、terminal 各项计数逐项相等；
- 所有 terminal leaf 的投影 ingredient 已付，没有 unpaid terminal；
- terminal 个数严格正；
- 原完整 cell cover、原错误/资源停止/close error 的条件均满足。

新 wrapper 再要求没有观察器包装错误，才报告 `complete_prefix_physical_angle_projection_bound=true`。部分已付 leaf 的 maxima/minima 保留为 observed extrema，不能在 incomplete 时升级为全域值。

### 命题 576.4：完整覆盖传递

若上述真实完整条件全部成立，原每一个闭 prefix cell 的同次投影 ingredient 参加原覆盖，故 R575 全局 $B_2$ 和其完整圆周估计覆盖当前准确 prefix 的全部径向位置、全角和两反射片。若任何条件未付，仅保原局部已付记录与全部 frontier，不得作全局推断。

**证明。** 原 split 只以其既有闭覆盖规则替换父 cell，子闭区间覆盖父闭区间；新 observer 使用完全相同的 cell 和分裂布尔。由于每个 terminal 的输入/退休都真实对应同一个 R553 owner，且计数相等、terminal 全付，没有遗漏原 domain 中的某一闭叶。全域上界是对这些真实叶上界取上包围；反射和准确刚性 registration 保欧氏范数。若中断或未付，前述完备条件不成立，原实现把 global bound 置为未付，而完整原 stack 与未访 roots 保留。证毕。

## 576.5 返回的定量界及其准确限制

原 actual field 的角网格须满足 R575 的真实 M/N 合同，特别为偶数 N、$N\ge 4M+4$。设实际旋转柱坐标速度三分量 $V(\phi)$ 对物理角 $\phi$ 的二阶导数有全圆欧氏范数上界 $B_2$，三个分量具有原 even/odd/even 奇偶性和 $\pi$ 周期，固定同一代数符号分支。保留的是 signed frequencies $-2M,-2M+2,\ldots,2M$，两 mean 均保，T mean 的消失只来自已声明奇偶性。

原 R575 完整证明给出：

$$
T_M=\frac{B_2}{2M},\qquad
A_{M,N}=(2M+1)\frac{4B_2}{(N-2M)^2},
$$

以及

$$
\|\Pi_{M,N}^{\rm ref}V-V\|_\infty
\le T_M+\min\{A_{M,N},T_M\}.
$$

这是完整三向量的欧氏范数界，包含无限尾和全部整数 alias。原网格不重复 $2\pi$ 端点；retained 频率严格低于 Nyquist。没有丢掉某个 alias、两个 mean 或向量常数。$B_2$ 的实际组成仍为原 R521 在完整 joint positive tube 上的两项：一阶角方向的二阶 majorant 加角加速度方向的一阶 majorant。$\mu,\nu,A$ 仍是同目标、同径向位置的标量，角向导数在该参考问题中为零；d/e 是原实际旋转框架分量公式，不能把 world-frame 导数偷作这些分量导数。

此式是**准确参考投影**的条件界。下列责任没有由本接线支付：

1. 实际 floating FFT、literal trig table、RHS 的形成与舍入误差。
2. nominal scalar 相对同一准确 C/target RHS 的差。
3. literal solver cubic 的原真实 residual、其与 quintic 的完整同场差及比较曲线所在 tube 的附加责任。
4. 原 worker 的 root/sigma 选择识别；两个固定代数分支的共同上界不等于证明实际分支身份。
5. tail、collar、cut patch、caps 的投影参考，边界锚定、角向 metric error 和全闭域 relative-metric floor。
6. 准确解存在、嵌入/reach/held/$\delta_E$ 的实际证书，或固定目标误差随加密降至机器精度/原 solver 容差的实际终结。

全 t 的原相位结论仍通过准确材料逆运输、全圆覆盖和同时拉回的同余成立。对本投影参考，只能拉回已经构造好的基场缺陷，或显式采用共轭投影；不声称固定离散网格投影与任意相移交换。实际 nested t 查询仍是原 4、8、16，不用有限 t 采样代全 t 定理。

## 576.6 普通失败、资源中止与原接受门

源码把新增观察器的失败分成原实现已经需要区分的两类。

普通 observer 绑定、inspect、retirement 或 summary 异常，写入具名 unpaid 记录，包括真实阶段、原 cell（若存在）、类型、消息和 traceback；计数与首末记录进入必要摘要，各已提交 cell 的完整记录留原 ledger。普通诊断未付不抛成原 metric 拒绝，不改变原 scientific acceptance 或触发新的 solver retry。

ResourceStop、MemoryError 仍原样传播，信号仍由原 owner 和 Budget 处理。原 current-cell/frontier、全部未访 roots、原 close error 与 actual elapsed 继续保存。计算诊断使用原 measurement 的预算检查；它确会耗用同一剩余时间，所以本文不承诺原测量在同一预算内完成相同数量 cell。

真实首场仍须原 full453→固定同点 full450、当前 H、全部真实 J、120 FD、full DN、final audit 等原门。后继先真实 mesh/five-factor，再真实增 M union，原旧112+新增模态完整族、deep、grid、native/J/FD/final 全部按既有合同支付。新诊断从这些真返回场读取，不能从部分源准备或 source SHA 制造 accepted checkpoint，也不能以缺少诊断反向改变原 BVP 门。

## 576.7 真正来源闭包和生成顺序

冻结 R591 为 **627=310 public+317 generated**。本结论增加 **8 个 public** 与 **7 个 generated**，实际集合为：

$$
318\ \text{public}+324\ \text{generated}=642.
$$

新增 public 是本次 composer、entry、plan，R575 库，三个先前不在闭包中的 reference 源，以及 R586 关系库。两个早已存在的 reference 文件只重申真实相同身份，不重复算新增。新增 generated 是一个 evidence 和六个 metadata caller。完整13层数量依次为：

`15, 5, 13, 49, 51, 46, 57, 6, 6, 7, 56, 6, 7`。

前12层源及原输出全部作为明确祖先保留。最后7件通过原 source-view generator 的完整 literal before/after/count 形成，实际先绑定已存在 baseline，再在当前 computations/HERE 创建新 basename，再读取实际输出完整 bytes/SHA。不得在文件未生成前拿新名进行 import 或假报其存在；不得覆盖旧来源文件。

本次 plan 是 `r576-same-return-full-angle-projection-source-plan.json`。物理执行 schema 保原 `R496-current-C-zero-linear-three-level-source-view-plan-v1`，逻辑 schema 为 `R576-same-return-full-angle-projection-and-metadata-source-plan-v1`。它含7个输出、46种完整字面 replacement、63次具名 application。所有数值源的实际内容由各 baseline 与这些全部 replacements 唯一确定；没有猴补冻结模块全局而继续冒旧 source identity。每个 view.output 仅含 file/bytes/sha256 三个身份键；schema/frame 保在 request.roles 与完整 semantic_schema_rebindings，由原 same-C composer 其后逐值严格核验。这样三身份键比较两端形状相同，不把语义字段混入文件身份对象。

same-C 的八数学角色中七项仍为真实 R570 输出，第八 evidence 是本次真实新输出。新 same_C composer 读真实 R544/R567/R570/R576 creator 回执，分别登记每个 actual_source 的真实 creator。它不是再次生成这些8件。额外 runtime 原件及 metadata 共17件，加八数学角色为25；R586 用于 public metadata 读回，不算新 scientific runtime module。

其中 first captured reader 仍是实际 R570 输出：

`root_20261116_actual202_captured239_coast_base_zero_linear_gzip_two_phase_necessary_readout.py`，32662 字节，SHA256 `508885ca68dc0500a8bd5923b2cfb90746ebb118bc4fd25a83cb5160d153a7e9`。

该完整身份直接取冻结 R591/R570 的实际请求原字段；不得用旧 bound230 reader 或仅凭同 schema 代替它。原第一、resolution、incrementalM 三个捕获 writer/phase reader 继续保存全部实际 capsule/status 与每个原成员身份，正常与 recovery 选择均继承 R570。没有新增另一份 capture 文件或填造缺失 `sol.sol.c`。

## 576.8 单一原钟、真实 namespace 和 owned 过程

独立实际 request 编号是241，真实 run/head 由之后官方绑定；不会沿用任何祖先 run。内部原完整科学子合同仍使用其实际原 namespace 和 deadline schema：

- namespace：`visible-current-C-actual202-ten450-closed-geometry205`；
- deadline schema：`request205-owned-job-science-deadline-v1`；
- 原科学窗18900秒，原必要/规则保留2700秒；总 workflow 360分钟；
- source copy/materialization 之前即记 namespace 唯一起点，没有从 same-C、mesh、M、投影观察器或临时 working view 重新起钟。

首 BVP 仍原7200最大值，sampling 留未来 BVP3600 的原政策保持；本次不降低32 GiB启动门，不删除下游还要消费的 far账。R498 首行起流式 gzip 和全部实际 decoder/后继消费仍在现行源闭包；R499 原规则具名语义读回仍保。单worker sampling 的真实 schema、depth2 work策略、完整 point/stack必要责任全部保持；未把245的双worker或新sampler schema混入。

same-C原分配逐值保留：head1800=1650+120+30；单metric240；单measurement300；compare120；metadata reader300；measurement work width为 $10^{-8}$、reference eta为 $10^{-6}$，均保持其原工作/报告含义；全局末900秒预留与原query work预算均由真实绝对deadline裁剪。新增 R575 不占独立预算、不启动子进程、不新开clock。所有 TERM→KILL、wait/reap、PID/start-time/group/session与未知scope处理继承原 OwnedChild/OwnedTree。

路径按实际 source view 分责：

- primary checkout 是冻结仓库字节；其中旧220/222/230/235/238/239/247请求及旧源不改。
- runtime view 是 `$RUNNER_TEMP/request241-runtime-metadata-workspace`，当前 GITHUB_WORKSPACE 与 computations 指向此真 view。
- 每个步骤显式 source `$RUNNER_TEMP/request241-runtime-env.sh`，恢复同一个 VISIBLE_BASE、VISIBLE_COMPUTATIONS 和原 clock。
- `$VISIBLE_SOURCE_TOPIC` 仍是 base 内恢复的原 source-topic；proof_directory 是当前 view 的 topic/results。二者不是同一路径。
- 实际241 inner 合同放在 view 中原220固定 request 路径，并写同字节 `base/refinement220-request.json`。其真实 bytes/SHA由 `source-binding241/result.json:actual_derived_request`产生。
- primary 中原220 `f6ca6387…`、repaired222 `2d1c3a7d…`、冻结247 `42547b2d…`分别作为祖先完整绑定；没有在 view 读当前文件却称它仍是原 f6ca。

## 576.9 八阶段、两槽及实际调用

same-C 原八阶段保持：

|顺序|阶段|真实输入/结果|
|---:|---|---|
|1|head_recompute|同准确 C/root 的完整1440头/six-primitives与原查询重算|
|2|level0_metric|真实首场、完整新同语义包围及原全metric|
|3|level0_measure|真实首场；新增同次 R575 诊断|
|4|level1_metric|真实 mesh/five-factor accepted 场及原metric|
|5|level1_measure|真实level1；新增同次诊断|
|6|level2_metric|真实增M union accepted 场及原metric|
|7|level2_measure|真实level2；新增同次诊断|
|8|compare|读取同一新evidence schema的实际完整 measurement|

first 槽在真实第一 shared/原必要读回之后、实际联合精化之前执行。successors 槽在原 mesh/M/几何/evidence/display 后执行；已启动的原stage不会重复。缺某个真场时，该级写 `genuine-actual-level-field-not-returned` 和完整未启动责任，不从上一场改标签补齐。head未返合法新包围时保原准确场/原粗界责任，不伪造新 C。metric失败不阻同级measure的独立尝试，普通diag未付也不阻原精化；共同材料B缺失只留下相应measurement未付。compare不会把上界改善当真实sup严格下降，也不把固定eta重复pass当完成README的误差下降要求。

R575仅在各 measurement 的原 prefix cell 出现；它并不在 head、三metric、非prefix块或独立display中暗跑。normal链已有evidence源仍原字，不因本次same-C后继将其旧结果认作新schema。三个same-C测量与compare全用新同一evidence，因此不发生系列schema混装。

## 576.10 完整必要选择与恢复路径

新 evidence 的普通 result、`necessary(result)`、compare 每级记录都明确包含 `actual_reference_angle_projection_defect`。没有依靠 generic small 对象摘要碰巧留下这个新字段。该字段包含：

- requested_source、实际 loaded source 和实际 binding attempted/error；
- 原 R575 的完整必要对象 `original_R575_summary`；
- observer_error_count、首末实际 observer error；
- 完整 cell ledger 的真实 bytes/SHA及原 coverage/pending 所在地址；
- 完整 global flag 与局部 observed extrema 的明确区别；
- 当前未提交 cell、全部未访 roots 继续归原 frontier 的说明；
- 原 ledger 所有行并未因本摘要而全部回传的准确范围。

原 R575 必要对象保全部M/N、原物理三分量/mean/频率/网格约定、原source绑定、实际正域责任、完整计数、首末未付 terminal、最后观察cell，以及全局或仅局部的界。异常消息不改造成成功标记；缺结果不填零，不以exit0或source-generation completed代数值接受。

当前 same-C reader 从本次实际角色加载新 evidence 的原 `readback`。正常路径和结果存在时的 recovery 都读取相同 result SHA 与相同完整 necessary selector。若某个 stage 不曾产生 result，返回其原未启动/未返状态和现存文件身份，不制造虚假的 R575 summary。first/successors 两槽状态、8个完整stage地址、原 stderr/errors、原quiet观察及全未访问suffix继续由原reader处理。

每份语义不同的 head、metric、measurement、compare 必要正文仍各自单90000字节上限。超限返回70，完整原件留同job临时目录；不得把新增字段摘出去分第二块以规避原上限。新 R575摘要可能使正文更长，本文不保证一定fit。没有把 raw ledger、quintic/cubic数组或大日志上传Git/公开artifact；只有作者源码、完整方案和论证进入Git。

原 normal refinement reader的body与same-C综合metadatabody也各保原90000/70。后者保 stage 必要文件与实际读回身份、原原件scope，科学每body在compute原frame完整输出；report只按原workflow传允许的旧body及same-C summary身份/stepoutcome，不把所有几何正文再塞report形成第二份近1MB副本。

## 576.11 R586具名关系只改变来源元数据表示

真实 public composer 的 `generation_readback` 先把13层的生成原件、实际source row、stderr、错误、缺失/当前未处理地址及原materialization record全部形成原 `state`。此时原 `complete_necessary_readback` 谓词已经按全部row/errors计算。随后才执行：

```python
original_body = canonical(state)
write_new(out / "original-selected-state.json", original_body)
# Actual file, byte count and SHA are bound before importing this metadata helper.
selected, transport = relation.compose(
    state, namespace=base, computations=comp)
body = relation.canonical(selected)
```

实际原库为 `root_20261116_complete_generation_source_relations.py`，13605字节，SHA256 `0ed83517eb6dd726e4e82f6b2b5f6dc391432994f7fcff93ef3b0e0692717484`。它是第318个public source中的明确一件，由原source复制和实际HERE身份绑定完成，不加入25个科学runtime对象。

这里的原选择完整保留。R586仅使用已具名的17个generation字段、6个parent字段、严格三键source identity、以及完全相等的已选parent row。每行原字段顺序/presence、key order、实际值类型、null、负零和所有unknown字段都能从同一正文恢复。实际observed identity不能替换为declared identity；异常、失败、frontier或完整stderr不是“重复成功”而被省掉。若遇reserved key或未知shape，原库返回整份literal对象。

原source identity有明确列：原file字符串或准确root+suffix、bytes、SHA和原key order。parent row只在全部原值与类型/顺序严格相等且唯一匹配时共享。具名row layout保全部原key及每个字段的值。`expand` 是已有明确定义的数学逆，不在当前入口另跑fixture或作为新gate。它不需要外部source文件或被省掉的raw即可恢复原已选对象。

### 命题 576.11：原已选必要scope不减

令 $S$ 是原完整 `state`，$T$ 为本次实际输出的 `selected`。对原库承诺的named形状，`expand(T)=S`，并保所有选定字段、顺序和类型；否则 $T=S$。关系候选只有在其完整canonical字节数严格小于原值时才使用。因此来源必要范围未减少，原90000门仍作用于最终完整 $T$。

**证明。** 同一source row用表中准确值及其原key order逐项还原；短path由原root与原suffix连接，未重新计算或推断路径；parent引用还原唯一完整原row；generation/parent layout还原全部原key和值，unknown row保持literal。按原嵌套结构递归后恢复原root key顺序，得到完整 $S$。这正是原R586 `expand` 的具名逆；未满足形状或收益条件时直接保 $S$。入口未在其前后删字段，原完整性布尔仍取 $S$ 而不取压缩后的形状。证毕。

临时文件保：

- `source-generation241-readback/original-selected-state.json`：原完整已选正文；
- `source-generation241-readback/source-transport.json`：实际helper身份、原body身份、完整transport facts；
- `source-generation241-readback/summary.json`：实际单份传输正文；
- 原shape/大小不fit时仍有真实原文件与overflow事实，返回70，无成功marker；
- 若原scope complete且最终正文未超限，原marker再绑定以上实际identity。此marker只表示immutable source scope已读，不自称processquiet，也不授权删除科学raw。

关系原文件虽保于临时目录，逆恢复正文不依赖它；不能把它当作“未回传部分”放在外部并声称正文完整。最终正文仍有完整逻辑逆。transport event单独报告原/实际字节及SHA、representation和完整来源统计，不承载拆分的科学body。

## 576.12 清理合同与真实失败边界

最外层public entry的 `guard-cleanup` 先读取当次 `source-generation241-readback/readback-complete.json`，检查真实repo/run/source、当前composer、actual_inner_request和summary bytes/SHA。缺失或unknown时，输出 `request241_cleanup_skipped_before_generated_entry`，明确实际generated cleanup未调用、upstream cleanup未调用、raw_deleted=false。

支付这项immutable scope后，才进入原same-C composition/readback/quiet与当前entry necessary，再进入原refinement reader全部原结果和quiet predicate，最终由原cleanup执行真实删除。新关系或诊断界大小不是清理门；反过来，diagnostic positivity也不能替代任何必要读回或owner quiescence。所有有真实raw的范围持续保留到原完整条件满足。

源准备失败且generated程序尚不存在时，public entry能给出实际未启动范围；它不调用不存在的reader，不伪造field/parent，不从source准备exit0推native通过。必要transport失败或未知processscope保持清理不获准。作者文稿中的“保留/可清理”均是合同，实际removed只能由未来当前run原事件判定；本文未预填任何删除事件。

## 576.13 正式文件与完整来源身份

正式发表的是下表五个运行/入口文件及本完整证明接口。生成的7件源码只由plan实际形成；展开全文可供作者交接，不另复制到main。各列SHA是文件完整UTF-8字节，不是缩短标签。

|正式相对路径|字节|SHA256|
|---|---:|---|
|computations/root_20261116_request241_sampling_refinement_composition.py|79517|7c3e82e97b2fdc1b726a619bb66b98df15be6f7d09521ed44f789091a3c1815b|
|computations/root_20261116_request241_actual_source_entry.py|38221|2619250a64f54abae0c7023b64c5e10133b1ac326ee1911396e34bb7296eba4a|
|notes/r576-same-return-full-angle-projection-source-plan.json|33755|8ed263d3aaed5ceb8ae79e4783cb7d4d5d87170ee2ee453e8eb88339a8a8a560|
|notes/current-C-full-angle-projection-refinement241-request.json|72451|35e32dafedbc04bf85c562dbec6a03b85ad81334a6fe219cbfadc5481538b5e6|
|仓库 .github/workflows/visible-current-C-full-angle-projection-refinement241.yml|92426|b66c1ce2441a2f285d3a9a64922b1bdaa3451382eaaa5ad8907888d0d3ce4d8c|

前四路径属于 `topics/visible-flex-larger-amplitude/`；workflow属于仓库根。实际7个输出如下。

|角色|实际basename|字节|SHA256|
|---|---|---:|---|
|same_evidence|geometry_20261116_request241_same_C_projection_metric_evidence.py|76200|d0c91d08fa46d5bafaf69faa472780a492c3b84a7ba8adc7d9b2d10b2b72182f|
|meta_owner|geometry_20261116_request241_owned_roles.py|25764|9825965595717288262c339c8b94d95923e520739afc330b4f93847483f543e0|
|meta_runner|geometry_20261116_request241_joint_refinement.py|48824|777052e20d6bbe1747a32cdbe02b3c66133e87fe5072f4541ba9155ee621ab1d|
|meta_reader|root_20261116_request241_refinement_necessary.py|44584|2b150e95126dae417338d8343a0882d09e6afecb0c20cdfa2f24e5e7736a00c0|
|meta_same_composer|root_20261116_request241_same_C_composition.py|35587|f7c71176aaaf0a580c108b9f17a6e65ca46728b3d8835028b239145cd69bec19|
|meta_same_runner|geometry_20261116_request241_same_C_refinement.py|45658|8cf58c531984c9829d01594fd88d973d1ce51623e8048aa472b2487cd74bef31|
|meta_same_reader|root_20261116_request241_same_C_necessary.py|35746|f11912f9babb97d119fd41f7f9e1de2154d8107a1ed27adaaf00425478501236|

生成器仍是 `root_20261116_current_C_zero_linear_source_views.py`，11895字节，SHA256 `4d4c507edd571b67655fd2e66fb4bcfa173b1239928443831a81a925c4869ec4`。所有其他祖先的完整file/bytes/SHA及recipe/rules/工参来自冻结request和原plan；本文件不把642项全部再抄一遍形成另一份可能漂移的表。完整来源集由原205 `source_sha256`、repaired222 `additional_source_sha256`、本次 `source_binding.additional_public_sources`、13层全部view输出作按basename一致并集；重复名须同一完整SHA。

源准备的metadata合同中，两处当前inner描述：

`upstream.request` 与 `source_binding.current_inner_contract`

逐结构相同，实际为318/324/642。它们的schema是 `public-current-C-bound241-coast-base-source-closure-request-v1`，request_number241，identity_from为 `source-binding241/result.json:actual_derived_request`。不能保旧641计数然后只在说明文字写642。预刊draft中的641/旧request指纹已被本表替代，没有改任何已运行入口。

## 576.14 实际CLI和输入约定

以下是已写源码的真实入口，供同job调用；不是本文执行记录。`OUTER` 是当前request241文件，`OUTER_SHA` 固定为：

`35e32dafedbc04bf85c562dbec6a03b85ad81334a6fe219cbfadc5481538b5e6`。

`INNER`/`INNER_SHA` 必须取真实 source-binding241 回执/环境，不预填未来派生文件身份。`BASE` 是上述原205 namespace，`COMP` 是当前view真实computations/HERE，`SOURCE_TOPIC` 是 `$VISIBLE_SOURCE_TOPIC`。

### 14.1 public入口及完整生成

首次初始化在primary checkout：

```bash
python -u "$COMP/root_20261116_request241_actual_source_entry.py" initialize \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP"
```

成功形成环境后，每个workflow run块显式source本次env，再在实际view调用：

```bash
python -u "$COMP/root_20261116_request241_sampling_refinement_composition.py" materialize \
  --request "$INNER" --request-sha256 "$INNER_SHA" \
  --base "$BASE" --computations "$COMP"
python -u "$COMP/root_20261116_request241_same_C_composition.py" bind \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP"
python -u "$COMP/root_20261116_request241_same_C_composition.py" preflight \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP"
python -u "$COMP/geometry_20261116_request241_owned_roles.py" prepare \
  --request "$INNER" --request-sha256 "$INNER_SHA" \
  --base "$BASE" --computations "$COMP"
python -u "$COMP/root_20261116_request241_same_C_composition.py" prepare \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP"
```

原PYPINS完整科学断言仍被保留；metadata只换真实当前request摘要、来源数、composer名和本次实际workflow路径。没有照搬245双worker的schema，也没有回退到222误检查祖先workflow路径。语法检查只在真正Actions源准备阶段按原排除合同进行，不在作者本地执行任何项目AST、compile或数值测试。

### 14.2 原科学链和两个same-C槽

原C、cut、工厂、deep、sampling、candidate、full453→450、第一closed/held/原读回全部仍由workflow原块调用；不是下面的简短命令替代它们。首槽调用为：

```bash
python -u "$COMP/geometry_20261116_request241_same_C_refinement.py" rules --phase first \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP" \
  --source-topic "$SOURCE_TOPIC" --proof-directory "$PROOF_DIRECTORY"
```

然后原完整联合精化的真实caller：

```bash
python -u "$COMP/geometry_20261116_request241_joint_refinement.py" rules \
  --request "$BASE/refinement220-request.json" --request-sha256 "$INNER_SHA" \
  --base "$BASE" --computations "$COMP" \
  --source-topic "$SOURCE_TOPIC" --proof-directory "$PROOF_DIRECTORY"
```

最后同一same-C入口 `rules --phase successors`，参数和deadline同首槽。真正workflow给外层timeout并保持原TERM/KILL保留，rules入口再按原owner启动实际exclusive session；不能把上述命令在未登记owner的任意shell裸跑冒已实现生命周期。

actual evidence内部CLI保持：

```bash
python -u "$COMP/geometry_20261116_request241_same_C_projection_metric_evidence.py" measure \
  --input "$ACTUAL_MEASUREMENT_INPUT" --input-sha256 "$ACTUAL_MEASUREMENT_SHA"
python -u "$COMP/geometry_20261116_request241_same_C_projection_metric_evidence.py" compare \
  --input "$ACTUAL_COMPARE_INPUT" --input-sha256 "$ACTUAL_COMPARE_SHA"
python -u "$COMP/geometry_20261116_request241_same_C_projection_metric_evidence.py" readback \
  --directory "$ACTUAL_EVIDENCE_DIRECTORY" --result-sha256 "$ACTUAL_RESULT_SHA" \
  --out "$ACTUAL_NECESSARY_DIRECTORY"
```

这些input由same-C原runner根据同job真回执形成，不能把旧run结果或手写success当输入。measurement schema为 `request241-same-evaluation-angle-projection-and-complete-metric-evidence-v1-measure-input-v1`；compare input为 `request241-same-evaluation-angle-projection-and-complete-metric-evidence-v1-compare-input-v1`，series result为同SCHEMA加 `-actual-series-v1`；需按当前真实input构造，不混旧evidence schema。R575不新增另一份input、phase或CLI；M/N、算术精度和全部工作值仍来自同一当前对象。

### 14.3 必要读回与清理

来源生成必要独立于任何科学成功：

```bash
python -u "$COMP/root_20261116_request241_sampling_refinement_composition.py" generation-readback \
  --request "$INNER" --request-sha256 "$INNER_SHA" \
  --base "$BASE" --computations "$COMP"
```

public composer的原 `readback` 使用同INNER；current refinement reader的 `readback` 也使用同INNER；entry的 `readback` 使用同OUTER。same_C composer的 `readback` 同OUTER，原same_C reader保持真实三个outcome参数：

```bash
python -u "$COMP/root_20261116_request241_same_C_necessary.py" \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP" \
  --prepare-outcome "$ACTUAL_PREPARE_OUTCOME" \
  --first-outcome "$ACTUAL_FIRST_OUTCOME" \
  --successors-outcome "$ACTUAL_SUCCESSORS_OUTCOME"
```

source与same-C必要frame分别是：

|scope|BEGIN/END中的完整frame名|
|---|---|
|来源生成完整单body|REQUEST241_COMPLETE_SOURCE_GENERATION_NECESSARY|
|原完整source composition关系|REQUEST241_SOURCE_COMPOSITION_NECESSARY|
|当前public source entry必要|REQUEST241_ACTUAL_SOURCE_BINDING_NECESSARY|
|same-C source composition|REQUEST241_SAME_C_SOURCE_COMPOSITION_NECESSARY|
|same-C完整必要合并metadata|REQUEST241_SAME_C_COMPLETE_NECESSARY|
|新evidence每完整必要正文|REQUEST241_FULL_ANGLE_PROJECTION_COMPLETE_METRIC_EVIDENCE|

原refinement及全部原sampler/FD/closed/held/rules必要frame仍由其真实原源保留。marker不是frame：same-C实际marker为 `same-C241-readback/readback-complete.json`，schema `request241-complete-same-C-consumer-readback-marker-v1`；来源生成marker见§576.11；source entry marker为 `request241-source-binding-readback-complete.json`。缺任何真实必要前置，原cleanup不会因新增metadatascope自动获得许可。

完整workflow最后先 public entry `guard-cleanup`，保留原 `--new-composition-outcome`/`--new-readback-outcome` 及其后完整 `--` suffix，进入原same-C cleanup；再按原entry cleanup/原refinement cleanup完成其已有条件。入口源码里 `os.execv` 的真实suffix是唯一执行合同，不能将本段概述写成删减原参数的替代workflow。

## 576.15 本文条件结论和剩余责任

在同job实际来源绑定成立、原science返回真实当前场、原R553全prefix joint positive cover完整、原R575全部退栈ingredient完整的条件下，本入口真实计算并完整报告 R575 的全圆准确参考投影界。它使用同次全系数盒、同目标、同实际M/N和原全角/两反射覆盖；不是只登记一个未来API。

条件不成立时，入口保原field/metric/DFS/solver行为、原未返或未付范围、完整原件身份与真实必要运输结果。来源generation关系有严格逆，无法适配或不省字节就回原整对象；仍可真实70。新metadata读取不清理raw，新diagnostic成功不替代科学门。原source/history和当前run源不改。

作者仅进行完整来源文本写作、字面替换与完整bytes/SHA登记，没有本地导入/AST/compile/科学计算，也没有编造fixture、actual parent、run、边界常数或误差下降。正式运行只能由公开Actions以后按这个完整入口执行；未来实际结论预留R577，必须以官方实际head/run及唯一终态必要读回为准。

R580解析带是另一个已发表的条件组件；本次明确不自动调用。其独立后继如果使用同一个R575对象，仍须给自己的真实source/参数/reader与original retirement绑定，不能修改本次冻结源或用标签宣称已覆盖。

