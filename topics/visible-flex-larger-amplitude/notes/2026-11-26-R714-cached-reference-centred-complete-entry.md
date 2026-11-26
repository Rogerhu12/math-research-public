# R714 同图完整一阶 frame 复用：R715 中心化新场的完整独立入口

## 1. 本次交付及未发生的事项

本次交付包含完整独立的 R715 中心化 R711 单位参考场求解入口、全部源码再生器和两步公开 Actions 参数。新增的是同一次调用内的 frame 计算复用。原外层全部自由变量、共同的 32 个法向提升阶段、各阶段完整根方程和隐式矩阵、完整物理六 jet、全部正权 Gram/均值/交叉行、原 192 行选择器、幅度约束、Phase I、真值线筛及永久位置记忆均保留。

数学依据为 [R714](../results/R714-normal-frame-exact-zero-and-C1-reuse.md) 及其[完整实施附录](2026-11-26-R714-complete-frame-cache-and-zero-template-implementation.md)。中心化的实际物理六 jet 仍按 [R715](../results/R715-reference-centred-normal-sixjets-and-error-ledger.md)；固定参考场的中央轮廓仍按 [R711](../results/R711-smooth-triangle-central-profile-and-geometric-comparison.md)。这里不重新认领这些结论，也没有把缓存当成新的存在证明。

本次实际完成了完整源码派生、逐文件 SHA-256、完整函数 AST 对照、stdlib 编译和完整参数解析。没有在本地 import 科学模块，没有运行场、Jacobian、根、积分或数值试验。完整新入口尚未在本说明中执行，未声明重复率、提速、内存改善、舍入误差证书、闭合成功或任何几何结果。

本入口有自己的 schema、完整来源及模型身份。它不要求先执行未准入的 plain R711 或 plain centered 方向。原父源码是实现与参数来源，不是需要补跑的科学前驱。

## 2. 完整来源闭包

新增七份完整源码的锁定身份如下。实际发布目录为同题的 scripts/resume_20261126；每份均小于 100,000 bytes。

| 完整源码 | Bytes | SHA-256 |
|---|---:|---|
| normal_frame_c1_reuse.py | 34,905 | ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9 |
| reference_centred_c1_smooth_triangle_calibration.py | 11,893 | 3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991 |
| so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py | 95,491 | a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd |
| so3_reference_centred_c1_smooth_triangle_normal_lift_geometry.py | 58,473 | 353196a4faadc7537d04d6be139c9d9d8f47ee7e25e1f007e33588ac48cfa0ff |
| fullclosed_reference_centred_c1_smooth_triangle_normal_lift_so3_qp.py | 69,350 | f075257aaea0930f60d905c9b02ac5cfcff61bc42d7daf337912c8a287d0f347 |
| launch_reference_centred_c1_smooth_triangle_normal_lift_so3_actions.py | 17,526 | 509daaab85537ae1a905eaab9f18e51b2b10a008eaf0a93714bbbe95e8782de5 |
| read_reference_centred_c1_smooth_triangle_normal_lift_so3_report.py | 77,266 | 8b5a638bbd8e5ec90489a512e0c734985c845d64d8de4745268d7ebc91639f2d |

完整纯再生器为 derive_reference_centred_c1_entry.py，33,537 bytes，SHA-256 为 88ba5b3c8475e2eeaa9de04dd7469dc13f0c1ba151a70a2256aa87e3bd5c1dd7。它先逐字核六份原完整入口源码、ba3d helper 和原完整 ready，然后按明确出现次数替换、写出全部新源码，最后强制七份输出的完整 SHA 字典等于上表。任何来源或输出漂移均停止，不能通过改一个来源标签绕过完整绑定。

原六份来源分别为：

| 原完整来源 | SHA-256 |
|---|---|
| calibration a8e | a8e849068b12ffe2876c07ec2518947890c9f09614da2a9882b53e268e3ba873 |
| centered operator b259 | b2597012ec8ee063fabbb49a758b592d10f607de55ded3becaa8b62b6a50118d |
| centered geometry 6536 | 6536a71b9db5858d258ecdf71ada39611772f4ff28fe857887fef142386376cf |
| centered driver 92233 | 92233b4ffb0aaff1644e0c4bc9e7357a8eae37bd68e6d02ef0c6e0dcfbb31b81 |
| centered launcher 68a69 | 68a6979d35fe7a953975c5a191928668765ddde7b4018fc7a8dee353138475dc |
| centered reader 7fc2 | 7fc213c108245cb2c555d573a52961fd07f1b941d85411e8e6e8d8c22f20a5bb |

原完整参数 db99d87e07974848ac61b6b93bb294cb1fbeb28faf7187edc8f072ce6d8b8934 只作为保持全部数值参数与历史路径的来源。

三项新 schema 为：

- operator：complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1；
- driver report：complete-R711-reference-centred-C1-reuse-fixed-normal-plane-SO3-QP-v1；
- 当前点根 snapshot：actual-reference-centred-C1-normal-current-point-snapshot-v1。

源码角色名严格为 frame_C1。模型键 normal_frame_C1_reuse 存 helper 的完整 definition。它在 q.identity 计算及 reference_calibration.bind_field 之前进入模型，之后才构造实际 Kernel。新的 calibration 完整体只变其 ENDPOINT_SCHEMA；原 callback codefile、caller schema、helper 完整 SHA 与完整模型守卫均保留，未将新 operator 冒作 b259。

仍使用完整 R711 provider 0d09ca45、均值核 f8487dfe、base 6a80361a、12-key Q binder 307ebae3、真实 reference 4e65577d 和 scalar e091f675。完整 driver 的 28 个 runtime role 均显式记录并核真实文件 SHA。新 reference/profile/core/H 身份由本次真实输入产生，不把旧 run 的字节身份或旧几何证书迁入。

## 3. 两类调用严格分开

Kernel 只存来源、策略及实际计数，不在不同调用间保留 active graph。它提供两个不同 scope。

### 3.1 原始根链中的 no-grad 数值 scope

原 _run_chain 仍运行在 torch.no_grad 下，data 已完整 detached。新增 value_scope 仅包住这一次根链。它绑定完整当前点摘要、完整模型、实际 data 容器及各 Tensor 的对象和版本、完整 phi 顺序、角导数阶数及每个角的全部 3×6 控制 jet 字。

第一次遇到一个键，仍调用原完整 _normal_frame_jets。只有真实有限的完整结果才复制缓存；随后同一次调用中完全相同的键返回克隆值。第一、二角阶分开；全部 18 字始终进入键，包含 signed zero，绝不以近似相等、根容差或“初点应当为零”代替字节相等。

原每个 stage 的根迭代、各 3×3/6×6/9×9 矩阵、实际残差、终点方程复读及 trace 全部照常执行。本 scope 不复用根，不删除阶段，不由 frame 值相同推出控制敏感度相同。缓存未命中时就是原公式；可选 clone 的 RuntimeError/MemoryError 只使该键退回已算原值或重新调用原完整 frame，并记录该次回退。身份、形状及输入错误不被吞掉。

value scope 结束时清除所有持有 data 和缓存数值的引用。其结果不能借给下面的 active scope，更不能把 detached frame 当成外参数导数。

### 3.2 完整隐式导数中的 active C1 scope

原 _implicit_jet_value 已取得全部已选根及其角 jet 后，新 scope 一次性绑定同一个 x/data/phi/order 图和完整 stage 顺序。x Tensor 的对象、版本、dtype、device、shape、stride、storage offset 与当前全部自由字的摘要均核；递归 data 也按对象和版本核。其缓存只在此次调用有效。

设完整 frame 为 F(x,U)，U 包含每角全部控制角 jet。对同图同字的独立局部叶 U*，构造

$$
\widetilde F(x,U_i)
 =F(x,U_*)+\operatorname{stopgrad}(D_UF(x,U_*))(U_i-U_*).
$$

仅在 U_i 与 U* 的全部实际字相同时使用，因此前向差值为零，且完整一次外参数导数为

$$
d\widetilde F
 =F_x(x,U_*)\,dx+D_UF(x,U_*)\,dU_i
 =dF(x,U_i).
$$

F(x,U*) 仍保持全部当前 x/data 路径。只 detach 局部偏导系数，不 detach Fstar，不 detach 各 stage 的上游控制。原逐 stage 的 frame_hat+(computed−computed.detach()) 和 control_hat 同型值锚完整保留；原 zero-target、上游 frame、增量变量、全部隐式 solve 也保留。

当前外层接口只需完整物理六 jet 及一次参数 J/J*。原法方程的 J* H_res J 没有变成完整外参数 Hessian。本 C1 替换不支持再求真实外参数二阶导，也不以 functional.jvp 内部的辅助反向过程为由省略一次完整 J。

一般非零控制键只有在计划的同完整字批次至少出现八次时，才尝试构造额外完整偏导模板；八是明确的新计算策略，未宣称是实测盈亏阈值。没有匹配、模板非有限或可选模板 RuntimeError/MemoryError 时都走原完整 frame 路径，保留本次真实失败计数。源码/图/形状违规仍停止。

## 4. 零控制完整模板及算术范围

完整 18 控制 jet 真为零时，可以不做 54 次输出反向乘积，而按实际左作用

$$
T=\exp([Bu]_\times)q
$$

计算同一个 frame 的零控制局部偏导。这里 B 包含旧两 bubble、固定十八 Q 字、准确共同长度在当前工作表示中的载体及新增 gamma；q 为当前全部 outer omega 作用后的参考 meridian，保留其 x 图。它不是只在整个物理初点成立的公式。

用原完整工作 _total、所有原积分节点及权、原 S 载体，有

$$
A_i=S^{-1}I(B_i\times q),\qquad
H_{ik}=(2S)^{-1}I\{B_i\times(B_k\times q)+B_k\times(B_i\times q)\}.
$$

A/H 的零、一、二角 jet 使用 B、q 的全部零至二角 jet 和完整 Leibniz 系数。固定 reference、core、cap 不依内部 u，故没有漏掉其 u 偏导；它们仍在完整 closure、上游 x 图和最终物理六 jet 中。

在全部控制角 jet 为零的同点，完整局部块为

$$
D_UF=
\begin{pmatrix}
H_0&0&0\\
H_1&H_0&0\\
H_2&2H_1&H_0
\end{pmatrix}.
$$

二角 frame 的实际 shape 为 (A,3,3,6)，偏导 shape 为 (A,3,3,6,3,6)，即每角 54×18。一角 frame 保完整 18 字键，实际偏导是 36×18，其中无需的末角块为零；没有将另一阶缓存或未读 u2 人为归零后冒相同输入。

零模板 Fstar 仍保持当前 B/q 的完整 x 图，H 只用于上述零差 C1 重接。最初 previous 真不需要梯度时，先复用 Fstar，后续出现 active 上游时再补 H，不删这些后续阶段。所有列、节点、角 jet 与积分权均保留。

上述解析重排在准确算术中相同，但工作乘加、cross、求和和原 AD 的算术次序不同。因此：

- 原 stage frame_hat 是前向锚，不声称解析 frame 的工作字逐位等于原 AD；
- 不把全零控制当成工作 closure 为零；
- 未支付本次重排、模板、积分、solve、triangular-chain 的浮点误差；
- 未声称命中率或提速，也不保证零模板会覆盖全部实际 stage。

其原始公式、全系数、同图一阶证明和具体工作责任见完整实施附录。

## 5. 物理模型、根与外层算法仍完整

此实现只替换两处 frame 读法，所有物理函数保持原 AST。中心化目标仍使用完整 nodewise reference 差：

$$
E=(\Gamma-\Gamma_0)-(P-P_0)+Q(T-T_{\rm ref}).
$$

物理重建仍是 R715 在 corrected T 上的完整原 hDelta 六 jet。设 h=1-S5，D=\Gamma-P+Q_ST，则

$$
F=(1-h)P+h\Gamma+Q_sT-(1-h)Q_ST,
\quad F_s=T+h'D,\quad F_{ss}=T_s+h''D,
$$

且 F_phi、F_sphi、F_phiphi 保留完整 reference/endpoint/积分的对应角 jet。缓存没有只改根残差而遗漏物理场中的校准项。工作径向 Gram 误差仍标 identically_zero=False，准确单位参考的结论不冒作工作场或已选外层场的证书。

全部原 core 自由量、有限谱 omega 自由槽、H 及其原 packing/transpose 不变。六控制及每 stage 三增量是内部隐式量，完整一角系统为 6m，二角为 9m；m=32 为所有角、所有候选共同固定分段。没有逐角 adaptive partition，也没有把辅助 tau 当 README 的物理弯曲参数。

根失败仍由原完整方程与原实际容差报告。缓存不是根存在、路径可逆、对称同支、全角连续性或几何充分条件。未完成 stage、未获得场、未发生 QP 的情形不由 reader 升级成成功。

## 6. 完整来源与函数对照

纯再生器的实际整函数 AST 结果如下：

| 完整体 | 原函数保持 | 允许改变的函数 |
|---|---:|---|
| calibration | 7 | 无；仅顶层 ENDPOINT_SCHEMA |
| normal operator | 46 | __init__、_run_chain、_implicit_jet_value、metadata |
| geometry | 24 | __init__ 的新来源/策略守卫 |
| driver | 11 | main 的来源加载、constructor 参数与报告头 |
| launcher | 2 | main 的完整 driver 名及 SHA |
| reader | 16 | endpoint_metadata、read_report；另增加 3 个纯读数函数 |

normal 的完整 _normal_frame_jets、_closure_jets、_corrected_jets、_total、_stage_jacobian、_stage_jet_jacobian、_solve_stage、_stage_control_jets、_stage_constraints 均与 b259 对应方法完整 AST 相等。helper 也在运行时对这些九个实际函数的完整 AST、codefile、globals、whole source 与模型绑定，不以同名函数代替真实来源。

driver 从内部 save_report 定义起至 EOF 的完整字节 SHA-256 仍为

9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee。

因此原初始真读、Phase I、QP、真目标、完整 domain、全 grid 与两套永久地址筛、原全部 C、幅度两分支、接受和拒绝后的记忆、最终保存等完整主循环没有因缓存派生改变。

原范数仍由本次真实 base 和全部自由槽构造；不复用别的 norm 的 C，不重标物理 J/Hessian。新 field/source 身份不继承旧场 Phi、旧方向或旧几何证书。

## 7. 读数合同与真实成本

完整 reader 首先核新 driver 全体及全部 runtime role，随后只从已绑定 ba3d 源的 AST 抽出三个明确的 stdlib policy/计数函数。它不 import helper 的 NumPy/Torch 部分，不重算任何场或根。

read_frame_reuse_policy、frame_reuse_binding、frame_reuse_metadata 核：

- 模型及 report 的完整 helper definition 相同；
- helper 实际完整 source、operator 实际 source 与完整 model identity；
- 每项实际非负整数计数都存在，不能缺项补零；
- 当前/上一 scope 各自的完整点、phi、order、shape、共同阶段数；
- started/closed 和实际完成阶段计数合法，但 partial scope 不推出场成功；
- 上一 scope 若属于 rejected trial 或另一个调用，记录自己的 point 与 current-point-match flag，不回填成最终点；
- 没有 active graph 跨调用保留、没有完整外参数 Hessian、没有误差或加速证书。

ready 的 scalar-only selectors 包含 helper 全部 23 个实际计数，以及 active/value scopes started/closed 和 scope_seconds。计数覆盖原 frame 调用、计划字不匹配、通用模板、额外 reverse products、零模板/零 H、完整积分与 cross 的次数/规模、C1 重接、constant-upstream 读取、数值缓存命中/失败及峰值 detached payload bytes。

这些峰值只计已列缓存 payload，不能当全部 Torch graph 或进程 RSS。scope_seconds 包含拥有 scope 的 stage 链，不包含之后外部 backward；不能把它标成纯模板耗时或节省时间。原全场/root/operator 成本和完整 main 用时照常由原报告记录。

失败可以在初始 mean、reference、normal stage 或几何之前发生。新读数保持这些不同层的空值与失败点身份，不用最终 metadata 的另一个点填补初始 snapshot，也不因缓存计数正值推断完整 J/J* 已成功。

## 8. 完整参数、实际历史与准入顺序

完整两步参数为：

[reference-centred-c1-smooth-triangle-normal-full-history-run05-ready.json](../computations/reference-centred-c1-smooth-triangle-normal-full-history-run05-ready.json)。

该文件 38,380 bytes，SHA-256 为 6e077b6757177548b7247a9a440542b0941d7bf8f63255fad4864ffbfe63496d。第一步完整科学入口，第二步完整纯读数。输出目录为 reference-centred-c1-smooth-triangle-normal-lift-first；纯读数保存于 postprocess/reference-centred-c1-smooth-triangle-normal-lift-first-readout.json。两步都以本次实际 reference.npz 作 controller 的 parent_bundle，故失败时不要求不存在的 final 先存在才能读报告。

数值参数沿完整原计划逐值保留：

| 参数 | 本次完整值 |
|---|---|
| 场尺寸 | M=160、原固定三 core、N=2048、全部实际径向节点/正权观测 |
| 角块/径向 stage block | 8 / 64 |
| outer 积分阶 | 8 |
| seed 径向/中央片积分阶 | 8 / 16；明确区别 provider 的默认值 |
| seed 边层总长 / triangle delta | 1/16 / 1/128 |
| normal stages | 32，共同准确 Fraction(i,32) 分段 |
| endpoint 实际物理容差 | 2e-12 |
| stage 根迭代/回溯/Armijo | 24 / 18 / 1e-4 |
| 原两 bubble | (1/32,1/4,15/32)、(17/32,3/4,31/32) |
| 新 gamma | (1/16,1/8,3/16) |
| 六控制域 | 2，保原维数和归一化定义 |
| metric | 1 个完整方向、最多 16 advances、mu=.01 |
| restoration | 最多 4 个方向、各 64 advances、mu=.01 |
| 真回溯 | 15 |
| norm | jet-sum；径向长度 .05；角 transition 24 |
| 谱目标 | p=4、epsilon=.001、scale=.05、原 legacy fraction=.5 |
| 工作 C | 原 selector 192 上界，完整幅度行另加；无删除 prefix |
| 几何/幅度 | reach .03、安全 .992、marked D=4.2、L=.9、Hfloor=1.01 |

target=1e-9 只是这份算法参数，不是把尚未返回的场声明为达到 README 的误差与实际精化要求。没有借小预算宣称算法能力上限。

完整十项历史路径依次保留：

1. axisymmetric-R690-reference-v2-first/locations.json；
2. axisymmetric-so3-complete-v2-first/report.json；
3. axisymmetric-so3-prior-separation-SOC-first/report.json；
4. angular-unit-complete-first/report.json；
5. axisymmetric-so3-integral-norm-first/report.json；
6. axisymmetric-so3-integral-norm-second/report.json；
7. zero-closure-added-gamma-KKT-explicit-H-first/report.json；
8. zero-closure-fixed-normal-lift-first/report.json；
9. zero-closure-fixed-normal-lift-explicit-H-first/report.json；
10. supported-unit-fixed-normal-lift-first/report.json。

这是一份完整路径计划，不把尚未取得的第十个原科学报告伪造成空集或成功返回。准入时必须消费届时真实存在且身份有效的完整地址来源。公开状态未返回时不能凭长运行推断失败，也不能从 SHA 重造未获得的地址。如果 direct 后继或其他同目标分支先实际执行并返回，应在准入本入口前显式追加它的真实报告；一个这样的后继使本计划成为十一项。这里没有增加“先运行 plain centered”的前置科学任务。

所有历史按照原完整 walker 解析，完整 grid/准确地址、保护标记和永久并集责任不因新 source 或 new-reference 标签消失；不能通过改变微小数学输入清掉应保地址。raw 报告、数组、cache 和 journal 仅留 runner，不入 Git 或公开 artifact。

## 9. 可复现的纯源码构造

发布后的完整纯再生调用为：

~~~sh
python3 topics/visible-flex-larger-amplitude/scripts/resume_20261126/derive_reference_centred_c1_entry.py \
  --repo /absolute/path/to/repo \
  --outdir /absolute/scratch/path/cached-centred-complete
~~~

再生器也允许显式指向已核完整父目录、helper 和原 ready，以便发布前在 scratch 复现；它仍逐字核同一组完整 SHA，不能据这些参数换父。输出目录必须在 repo 外。完整源码输出身份强制等于 §2；参数中记录本再生器自身实际 SHA。

临时 reference-centred-c1-source-lock-table.json 只是本地完整派生审计，含函数对照及来源表，不另入库。仓库保留完整源、完整参数与本说明的真实 SHA 即可，不把 manifest 当成代替全文的实现。

本轮实际静态核已经包括七份输出和再生器 AST/compile/py_compile、重复 literal dict key/explicit keyword 与尾空白检查、六父整函数对照、完整 driver 后缀、全部 runtime roles 真 SHA、constructor 关键字及真实 ready 的完整 parse_args。所有独立已审边界与这次检查都是源码证据，不是科学运行结果。

本实现可以立即被完整公开科学入口消费。它的有效收益、实际根链成本、初场是否成功、全 C 和目标变化、连续积分及浮点费用、全域几何和后续精化，均须由本身真实返回与后续完整同场证据承担。


根另全文核88ba完整纯再生器及三项新pure reader函数、实际完整_get_roots/_run_chain/_implicit_jet_value，纯文本再生七输出逐字匹配，全28runtime角色SHA和完整有序150字argv（仅新outdir）、十历史顺序均核同。临时来源输出表为 3807B，SHA256 `9a478da731d89f2a227fc663ef8713b5ca0cb27384b5f7de4e8f321d6c049c30`，只留摘要，不入Git/Release。未import科学模块或执行F/J/根/积分。
