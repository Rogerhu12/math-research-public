# 相邻完整 frame 的角向矩阵：完整实现、独立输入与 Actions 08 参数

状态：完整源码和可执行两步参数已经形成；此说明不声称新入口已准入、运行、提速、收敛或取得误差证书。所有本地检查限于标准库读取源码、完整哈希、AST、编译、纯文本再生和参数解析。没有在本地导入或运行科学模块，也没有增加科学 fixture。

本实现承接已经完整给出的相邻 frame 设计。它保留完整参考中心化场、全部原自由变量、共同的 32 段 normal 选枝、各段原根方程、Newton、实际三维矩阵、角导数求解和全部参数隐式链，只为随后需要的六维、九维角向隐式矩阵增加一个明确的新数值生产方式。它同时提供公开运行所需的完整输入闭包，不要求先运行未执行的 plain 或 detached 变体。

## 1. 改变的对象和没有被替换的责任

原参考仍由完整 R690 标量定义、真实初始 core/H、R708/R709 均值构造及 R711 的十二片平滑三角相位固定。当前任意自由点仍拥有全部 core、全部共享 quintic/Fourier 旋转系数以及 H；固定参考 seed 不会随当前点重选，也不会用中央 seed 覆盖或删除当前旋转变量。六个内部闭合控制和每段三个增量仍由原有限 normal 链选定，它们没有变成替代原自由变量的优化坐标。

完整参考中心化残差和实际物理场继续分别承担原定义的责任。根残差在节点层减去同一固定参考，然后完整积分；六个物理 jet 仍含当前 raw closure lift，包括 Fs 中的完整 h′Δ。工作径向 Gram 不被标为恒等于一。旧场的 Phi、可行性、连续误差、根分支或 reach 证明均不迁移。

原全角正权、spectral p/epsilon/scale、norm、阻尼、原 192 行、幅度行、包络 typed 行、完整 common-slack Phase I、独立真实场筛选和永久记忆更新保持原算法。每次真实返回报告都保存自己的初始值、终值、失败点、实际计数和来源。

## 2. 完整角向矩阵公式

设当前一个实际角的第 i 段上游控制为 p(φ)，增量为 η(φ)，上游 frame 为 B(φ)=f_u(p(φ),φ)。下标 0、1、2 表示沿已选整条角向控制的完整 total 导数，不是把控制冻结后的偏导。原控制链为

$$
u_0=p_0+B_0^T\eta_0,
$$

$$
u_1=p_1+B_1^T\eta_0+B_0^T\eta_1,
$$

$$
u_2=p_2+B_2^T\eta_0+2B_1^T\eta_1+B_0^T\eta_2.
$$

令 A(φ)=f_u(u(φ),φ) 为该段已经选定控制上的完整 frame。对本段 η 的各角 jet 求偏导时，原方程中 $(1-\tau_i)f(0,\phi)$ 是与 η 无关的右端；其实际值和各角导数仍须逐段重读。定义

$$
M_0=A_0B_0^T,
\qquad
M_1=A_1B_0^T+A_0B_1^T,
$$

$$
M_2=A_2B_0^T+2A_1B_1^T+A_0B_2^T.
$$

则准确算术下的完整矩阵为

$$
J_6=\begin{pmatrix}M_0&0\\M_1&M_0\end{pmatrix},
\qquad
J_9=\begin{pmatrix}
M_0&0&0\\
M_1&M_0&0\\
M_2&2M_1&M_0
\end{pmatrix}.
$$

这些式子保留了 A、B 的全部上游角导链。特别是 A 的一二阶角导中含 u_φ、u_φφ，不能用固定控制上的两次偏 φ 代替。对于非末段，本段最终控制就是下一段的 previous；在实际完整字、数据来源和所需阶数都匹配时，下一段已经计算的 B 正好提供本段所需 A。末段没有下一段，因此在实际末控制上调用原完整 `_normal_frame_jets` 取得 A_m。

此公式并未消去任何一段根或任何 η 未知量。32 段仍对应 metric 一角链的 192 个内部隐式量和六 jet 二角链的 288 个内部隐式量；当前实现仍使用每段局部系统和完整上游递推，不构造一个全局密集 288×288 矩阵。

## 3. 准确公式与工作数值定义分开

上述矩阵恒等式是准确算术结论。新源使用实际已选 root/frame 字及明确的矩阵乘积、加法、块装配取得 J6/J9。这是一种新工作舍入路径，不能称为对旧 fresh-AD 输出逐位相同的缓存。原三维 Newton/J3 路径没有被矩阵块公式替换。

新来源和模型写入 `adjacent_normal_frame_matrices` 定义，声明独立工作舍入、原 active 参数链保留，以及速度和误差尚未认证。源码没有把完整 AD 的计数增加到未执行的计算上。它分别记录实际装配、发布、原 AD 回退、最后 frame 读取和失败。

尚未支付的数值责任包括 block products 和原 AD 各自的浮点误差、求解误差、根误差、积分误差和后继整体场误差。R714 一次参数 J/J* 的边界保持；这不是允许对所得到的 J 再求外参数 Hessian 的声明，也不是 uniform IFT 或全角连续分支证书。

## 4. 真实来源、完整字和阶数的匹配

新 helper 严格绑定实际调用算子的完整源、模型 canonical identity、6a803 完整 base、ba3d C1 frame helper、375059 detached matrix helper，以及原九个数学方法的完整 AST。算子先将新定义加入 model，再计算 identity，再绑定完整校准 helper，最后构造 C1、detached 和 adjacent 三个独立核。不会先以旧 identity 建 cache 后再改 model。

`frame_context(data, keys, order)` 记录本次完整点字、完整有序角批、实际 mesh/width/Gauss/S 等积分载体，以及每个所需阶数的 T、reference、W、core/cap 与对应参考三 jet。角地址保留 literal binary64 字；不以相近数、相同 shape 或角索引计数替代真实来源。

`capture_frame_inputs` 在原升阶逻辑已经恢复低阶 frame 字之后记录每段的 previous 三套控制、实际 frame 三套字和每个 component 的来源。升阶保留原值、一阶字及其原产生范围，只补需要的高阶来源。当前完整三 jet 与旧 component 的所需前缀分别记录，避免把原来没有产生的 u₂ 假填为零后冒充原来源。

实际调用允许请求 order=1 时读到已经 order=2、但 `jacobian_order=0` 的 root。该情况保留完整实际高阶 root 和三套控制来源，只消费当前需要的前两阶，不强迫实际 root 降阶或重选。

每个 root 的保护摘要包含 Z、zero、每段 previous/frame/η/control/J3/record 以及来源记录；只排除本次有意写入的 `jacobian` 和 `jacobian_order`。逐段核对下一段 previous 的完整三套字确等于上一段实际 controls。不会把一次没有取得完整 root 的中间值登记为可复用 frame。

## 5. 全部匹配才装配，失败回原完整路径

`populate(data, keys, selected, order)` 只处理原 `_get_roots` 已经选定且当前需要矩阵的子批。它先核所有角、所有段、所有所用 component 与本次实际数据的匹配。任何必要数据来源不匹配都会使整批回到原完整 AD 路径；不是悄悄省掉有问题的角或段。

符合条件时，末控制上完整读取一次最后 frame，按上式生成所有段的 J6 或 J9。全部替换矩阵已经完成、有限且只读后，才写入被允许的两个矩阵字段，并前后核受保护的 root 摘要。新源不在已经写了一部分矩阵时把未完成的其它段冒称成功。

可选装配中的 MemoryError/RuntimeError 记入该实际调用后回到原完整 AD。强来源、字形状或模型错误仍明确报错，不把输入违规吞成科学可行。回退复用原完整 detached helper 的全阶段 scope：从第 0 段开始依次处理全部段，保留每段真实 η、previous、frame、zero 和共同 τ；不以挑选某些 stage 的方式破坏 scope 的顺序合同。

原 AD 或末 frame 本身失败时，记录实际已经发生的失败，并传播异常。新导数矩阵生产器的异常归类与末次调用记录不声称和旧 `_get_roots` 内部 `q._fail` 的计数逐字一致；原根 Newton/J3、已选 root 和角解记录的保持范围是明确的。一次失败的矩阵尝试不等于新物理场或完整 J 已成功。

## 6. 新算子钩子与未改完整主体

相对完整 d461 算子，只有 `__init__`、`_run_chain`、`_get_roots`、`metadata` 四个方法改变：

- 构造时绑定新完整 helper 并将实际定义纳入 model。
- `_run_chain` 为实际 frame 保存来源；原每段根、J3、角解、域与终闭合读取仍执行。
- `_get_roots` 保留缺 root/升阶/选批逻辑，用 `populate` 生产需要的角向矩阵。
- `metadata` 增加新 producer 自己的实际计数和末次调用范围。

`_normal_frame_jets`、`_stage_control_jets`、`_stage_constraints`、`_stage_jacobian`、`_stage_jet_jacobian`、`_solve_stage`、`_finish_stage_jets`、完整 `_implicit_jet_value`、core/cap、closure、corrected meridians、全部六 jet、residual、J/J*、point VJP 和保存/读入的物理主体保持父源 AST。完整 deriver 对允许变化的方法集合逐项核，而非只检查文件标签。

新校准 helper 仍是原完整体，只改准确 endpoint schema 及其来源。新 geometry 只改 constructor 的完整 source/模型核；从实际全场扫描到原前缀选择、双支幅度、永久地址、world 参数转置的主体保持父体。完整 driver 从 `save_report` 起到文件末尾逐字等于上一完整包络 driver，包含实际 envelope snapshot 刷新、Phase I、所有方向、回溯、拒绝后的记忆和终态真读。

## 7. 必要的新当前运行载体来源

旧 ef674 恢复源不仅参数路径，而且 CURRENT_RECORD_SHA、CURRENT_STEP、CURRENT_CARRIER_SHA 都明确绑定 run07 的实际记录。run08 不能只换路径后冒用该旧来源，也不能猴补模块 globals 后仍称完整 ef674。

run08 使用完整新 `restore_actual_run05_carrier_for_current_run08.py`，31102 字节，SHA256 `8c1e2d8f71bb08b33f99f9c187dbed2994776fc64b7114e1cea921a4fecff449`。该源按真正 GITHUB_RUN_ID/ATTEMPT 读取本运行已经公开的 part-001，并核本次完整 preparation report、carrier、reference 的实际路径、SHA、大小及完整来源。旧实际 dc5、2397 叶再生和原科学后缀保留。新08当前输入身份不预填为07身份。

原 c79 memory 对绑定 producer.source_sha256 有 ef674 硬守卫。因此此包新增完整 `complete_material_envelope_memory_current_restorer.py`，仅把 RESTORER_SHA 改成上述 8c1e；其余完整字节和所有函数/类方法不变。定义中的自身 source identity 如实变化，仍要求消费者重新哈希并完整读取旧、新两 NPZ 的地址字，不能只信 producer 的 true 标记。

两条输入路线严格分开：

|路线|实际完整 memory|实际报告责任|
|---|---|---|
|默认旧终态转移|原 c79，继续只接受 ef674 来源绑定|必须有由原104e完整读过的实际 cc0a terminal report；全部旧地址、保护和 typed provenance 真转移|
|显式独立新分支|新5f22，接受完整8c1e当前运行绑定|从本次真实原reference自由点和完整P0/两G开始；不声称有未读peer终态或typed优先级|
|独立分支自己的完整同源restart|该实际报告中已绑定的新5f22|保持同完整模型、实际carrier、原branch origin及其自己真实发生的全部typed记忆|

driver 的 SOURCE_PINS 同时保两枚完整 memory 来源，geometry 只接受这两个准确来源，pure reader 按实际 `material_envelope_source` 选择对应完整 validator。没有将旧 strict 路径放宽到任意 producer、任意 schema 或只按数组形状接受。

本次独立来源尚未提供“把不同 run 的不相同 reference 字节直接当成同一完整模型”的转换。以后合并 peer 报告时如实际 reference/carrier 身份不同，仍须独立支付准确地址/模型关系；此说明没有以“同 g”或“已覆盖 E”冒充该转换已做完。

## 8. 显式独立分支与未返 run07 的责任

运行参数必须同时明确：

```
--independent-envelope-branch
--pending-parallel-envelope-run 45909290354/1
```

独立模式拒绝与旧 parent-report、restart 或任何旧final/其它seed并用。它实际从 q.initial 的完整原reference自由点开始，pure reader 再核该点摘要与 calibration 中固定原reference摘要相等。没有因改变矩阵来源而替换 frozen seed，也没有未知 accepted final 的假定。

初始责任是完整已知 P0、旧 material grid G_old 和本次 G_current 的并集；二者若字不同，原完整 consumer 仍要求真实额外网格读取。所有这些点永久进入非线性六 jet 读取、两个主曲率分支及双 witness 符号。known P0 的原 protected 前缀保持，未知历史逐点保护标签和原 typed 首次发现顺序不伪造。

run07 的实际新物理地址虽然被原完整 E 限制，具体 typed family/branch/sign/partner、首次发现点摘要、顺序和晋升仍不能从 E 或 counts 反推。本次 `independent_branch_origin` 明确保存未读 run 身份、原 cc0a driver 身份、未继承旧final/typed字以及后继真实合并义务。它记录的是这个分支的来源事实，不表示未来可以丢弃 run07 实际返回的责任。

默认没有独立 flag 时，完整旧 terminal guard 仍生效。若未来取得真正 accepted final，旧严格路径保留从原完整 NPZ 提取全部相同 free-layout 字的能力；fixed reference 仍保持原initial，新来源重读自己的初始 Phi、根和六 jet。不同完整模型或不同实际carrier 不会仅因参数形状一致而通过。

## 9. 真实 Actions 08 顺序和全部数值预算

先在同一 run 真实产生必要输入，然后执行本包两步：

1. 完整 warm-only recipe，产生真实 `fullclosed-hold-warm.npz/.json` 和完整 scalar gzip，不重放旧优化方向。
2. 原完整 4e655 reference producer，产生 `axisymmetric-R690-reference-v2-first/reference.npz`、`report.json`、`observations.npz`、`locations.json`。
3. 新完整 8c1e restorer，读取本 run 已公开当前记录，真实恢复 dc5 旧carrier并生成本次 `run05-actual-observation-carrier-restored/material-envelope-carrier-binding.json`。
4. 新完整 adjacent launcher/driver；独立输出目录为 `reference-centred-adjacent-frame-envelope-normal-lift-first`。
5. 新完整 pure reader；parent 仍用实际reference而非条件存在的final，初场失败报告也可完整读取。

完整 ready 文件是 `reference-centred-adjacent-frame-independent-envelope-run08-ready.json`。其 steps 可直接加入08队列，不含未执行旧方向的假报告路径，也不把未返07 report作为先行条件。完整当前 source/ref/profile/carrier 的 SHA 在运行时从真实文件读取，ready 中没有预填未知新结果。

数值参数承接已选完整预算：N=2048、stage block64、angle block8、外场积分8阶、全变量 jet-sum 范数(.05,24)、μ=.01、1个metric方向最多16次QP迭代、最多4个restoration方向各64次、15次真实线筛、原192前缀、近活动包络候选32而实际分离typed集合无cap。保持 p=4、epsilon=.001、scale=.05、原幅度4.2/.9/1.01、reach ratio .03和safety .992。

共同 normal 节点仍准确 Fraction(i,32)，固定两个原bubble和完整γ，18个Q常量仍经当前真实 supported-input binder 绑定。seed边层总相对长1/16、平滑三角delta1/128、**实际 ready 的径向求积8阶**、十二片相位各16阶，共192个工作profile节点；均值/幅度的原次数和容差保持。不能把某provider的其它默认阶数误写成这次实际参数。

所有科学只允许在公开仓库 Actions。报告和原始场数组只留runner；公开记录按既有小型元数据政策保存来源、计数、SHA和真实返回，不上传大 raw。

## 10. 报告、费用和失败范围

新 helper 的 actual_counts 分列 provenance、矩阵请求、实际 adjacent装配/发布、完整AD回退、必要data不匹配、可选装配失败、最终frame实际读取及发布的6×6/9×9块。原normal计数只反映实际调用的原方法。相邻生产节省了哪些调用、是否有重复数据、是否加速，都须等待实际返回，不能由公式推定耗时。

pure reader 对新完整helper的纯stdlib definition/validator 按全源SHA提取，使用其真实 `__file__`，不把读数器自身当helper来源。末次调用保自己的点和角批；partial矩阵记录不填成成功root或成功field。完整report的原34个normal snapshot、seed诊断、中心化诊断、detached/C1实际计数、完整包络扫描、原+幅度+包络三项行恒等式继续读取。

新定义在任何方向开始前完整保存。一个首次场读取失败可以有准备好的输入和零次方向，但不能因此宣称达到终态、可行、驻点或不存在。矩阵生产失败、旧原方法失败与物理域/几何拒绝保其不同来源；实际旧raw closure、root残差、Phi、原physical g和Phase I的slack不混成同一判据。

## 11. 完整来源表和可重建性

此表列新九个完整runtime文件；它们均放在 `scripts/resume_20261126/`。数学 helper、normal、calibration源不会在运行中由小补丁临时伪装成旧源。

|文件|字节|SHA256|
|---|---:|---|
|adjacent_normal_frame_matrices.py|36272|955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3|
|complete_material_envelope_memory_current_restorer.py|40091|5f22ad999b33a657d5e59721f3d6459b3411faabb180a475cd3fd989b662fba0|
|reference_centred_adjacent_frame_smooth_triangle_calibration.py|11899|ccb3340e500a032943aaed084376136fd67ad81b222e1afbcc5e79d468f21ef8|
|so3_reference_centred_adjacent_frame_smooth_triangle_normal_lift_operator.py|96739|d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb|
|so3_reference_centred_adjacent_frame_material_envelope_geometry.py|68275|c253ef1559d00a2da2a961df10f47843e9f82b2c8dd17071a064b56042c5ac4e|
|transfer_material_envelope_memory_to_adjacent_frames.py|55758|eb22d711122da4e9db99a032f84560a32358f11a543b91757d9e83cc149bc2ee|
|fullclosed_reference_centred_adjacent_frame_material_envelope_so3_qp.py|74293|91c86a4fed296cda92a9ac522dace21fb7e0ab603c288226b5cc8e7c3b8f44b6|
|launch_reference_centred_adjacent_frame_material_envelope_so3_actions.py|20743|90423119843e0d4e4ab584c9476785b8b4bc3bd8fac50776571fc14711844ffa|
|read_reference_centred_adjacent_frame_material_envelope_so3_report.py|95630|c0cc0011498154a171e401d9874d34f060242180d341d6d2ea2b85eb963455dd|

完整纯再生器为 `derive_adjacent_normal_frame_entry.py`。输入是先前已锁的七个完整stage-cached父文件、完整955d helper、原c79 memory和完整8c1e restorer；父文件SHA写在再生器中。它产出上述九份完整源，不导入它们的科学模块，并核大小、完整AST、编译、重复字面key/keyword、尾空白、允许变化方法和完整driver后缀。

再生器的调用形状为：

```bash
python3 derive_adjacent_normal_frame_entry.py \
  --parent-directory /path/to/immutable-stage-matrix-revision2 \
  --helper-source /path/to/adjacent_normal_frame_matrices.py \
  --memory-parent-source /path/to/complete_material_envelope_memory.py \
  --current-restorer-source /path/to/restore_actual_run05_carrier_for_current_run08.py \
  --outdir /path/to/generated \
  --verify-existing
```

本次已实际执行完整纯再生；最终脚本的39项 runtime SOURCE_PINS 均按实际完整文件重哈希核对，所有 literal `paths[...]` 消费都有来源角色。完整driver和launcher的87个解析参数逐值相同；纯reader自身参数也通过仅stdlib解析。所有源均小于100000字节。本地没有执行科学F、J、root、integral、矩阵装配或数值fixture。实际科学返回与任何连续证书仍是公开运行和后续同场误差账的责任。


## 13. root 实际完整再生与公开准入

本节由 Astra-larger-e4e2a2bf-20261126 于 2026-11-27 添加。原完整九源及纯文本再生器先锁定；root 实际运行再生器，用七个完整旧 parent 源、完整 955daf helper、完整 c79 原 memory 以及完整 8c1e 当前 restorer 生成九个完整新源，逐个 whole SHA256 与上表相同。该运行仅使用 Python 标准库的源码/AST/compile/哈希；没有导入 NumPy/Torch/scientific helper，没有本机场、标量、根、矩阵或数值 fixture。

root 实际阅读原 `_normal_frame_jets(previous,data,order)`：它逐项计算 `j=0,...,order` 并沿第二轴 stack，因此输出确为 `(count,order+1,3,6)`；缓存中预留的三阶槽不被误当作所有请求都返回三项。最终 frame 的真实反向产品计数保留，不以矩阵乘法数冒充原 AD 数。相关实现说明不是新的执行前门；已有具体接口疑问已解决，立即进入完整公开求解。

`computations/resume-20261127-followups-08.json` 完整收入本 ready 的两个原样 step 对象，先后为完整科学入口与完整 pure reader，前面仅有必要的完整原参考重建和完整旧 carrier 重建。warm recipe 为 controller 的第1实际步骤，因此全流程依次为 warm、reference、旧 carrier、adjacent solver、pure reader。`finish_when_done=false`；完成当前预算不代表课题完成。

准备文件中的 `entry_admitted_or_executed=false` 是锁定该文件时的真实状态，保留其原 bytes 便于复核；本节及实际 followup queue 记录随后的准入。实际执行、源 commit、输入/输出 SHA 和算术结果一律以本次 Actions 自己返回的紧凑记录为准，不预填 run ID 或候选数据。

## 14. 当前运行输入的完整绑定

新 `restore_actual_run05_carrier_for_current_run08.py` 为 31102 bytes，whole SHA256 `8c1e2d8f71bb08b33f99f9c187dbed2994776fc64b7114e1cea921a4fecff449`；原完整 restorer 为 `ef67425800ae9de626a7f8f48fd89deb125fbf0e4d6af72cf79741d1e254664e`。原 `execute` 从 `if int(old['scalar_leaves']) != 2397:` 对应的完整科学恢复段到函数末尾保持原计算；实际 byte-identical suffix SHA256 为 `872f8c58b5aa90c48c39703d40ac137584177ee4d8bcb47789a567fe3624f63a`。其余旧输入、完整历史步骤、2397 live-leaf 规则、完整 `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` 载体接受条件均保留。

变化只在当前证据绑定：当前 source 从真实 `GITHUB_RUN_ID/GITHUB_RUN_ATTEMPT` 定位本次已经公开的 part-001，要求该文件小于60000 bytes，并核实际 reference step ID、run URL、完整源、实际 source commit、全 report/reference/carrier 路径、大小和 SHA。当前输出必须属于本 runner 的实际完整 work 路径。原07的 current-carrier/record SHA没有复制为08当前身份；当前 whole scalar requested-accuracy 的实际布尔值如实保留，不假定与07相同。

原 followup controller 的 `begin()` 实际以 publisher 当前 HEAD 建立 snapshot；reference 完整返回时 `finish_record()` 先保存并公开对应 record，再开始下一步。因此 restorer 读取的本次已返回 part-001 在随后的真实 snapshot 中有可复核来源，而不是从不存在的启动 commit 读未来记录。没有为此修改科学源或插入额外等待门。

新 `complete_material_envelope_memory_current_restorer.py` 只把原 c79 的 `RESTORER_SHA` 精确改绑到 8c1e；其他代码不变。新独立分支选择完整 5f22 memory，原严格 terminal-transfer 仍使用原 c79 memory。两个模式分别绑定实际 source，不能将当前输入贴上旧来源标签。完整 E、原 P0、旧/当前 G、所有实际查询地址及 typed history 的真筛义务均不变。

run07的实际终态仍未返回。本分支明确从自己原参考的完整自由点开始，未读取或继承未知07 terminal、未知全变量或未知 typed first-discovery 顺序。待07真正返回后，还须按实际固定参考/载体/角色逐项关联并迁入适用的全部新历史；本次独立起跑没有豁免该责任。

## 15. 完整运行参数与仓库范围

原 warm、完整 4e655 reference 与 8c1e restorer 的所有参数及输出/summary 字段均在 `resume-20261127-followups-08.json`，两个完整科学后继又同时原样保存在 `reference-centred-adjacent-frame-independent-envelope-run08-ready.json`。完整 source/参数文件自身为可复现记录；不以短命令代替原整对象。新 workflow 只启动本公开仓库的 Actions，科学限制350分钟；controller 为20000秒的准入预算，不能把其中任何一项叫作本课题的停止标准。实际未运行或未返回的对象保留为 pending。

依根 README 第2条的既有授权，同时添加 `.github/workflows/visible-larger-adjacent-frame-20261127-08.yml`。它保留已运行07的 checkout/setup/dependency pins、Ubuntu、Python3.12.14、NumPy2.3.5、SciPy1.17.0、CPU Torch2.5.1及单BLAS环境；仅改本次 request/controller/并发组和显示标题。完整 `public_actions_controller_parallel08_compact_metadata.py` 为19006 bytes、SHA256 `f651972c26d835e639da041736f06312b76ee0c8dd3716a970b31457960232c6`，保原3000秒真实pull/双README差异读取、60KB记录分卷和全部后继发布机制，使用独立08 HANDOFF槽，不覆盖06/07。

本结论仅为完整实现与真实准入；相邻乘积的加速、全域准确误差、完整新首场和方向尚未返回。原 all-t 连续几何/固定帽 mixed pairs、完整 metric 算子范数、A2 非零与真实 mesh/M 精化仍按 open/HANDOFF 继续，任何有限 source 审查不能替代 README 完成条件。
