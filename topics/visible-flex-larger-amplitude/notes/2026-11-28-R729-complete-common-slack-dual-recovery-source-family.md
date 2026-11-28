# R729：完整 common-slack 对偶恢复内核及 R728 独立下一求解入口

日期：2026-11-28。准备时间以实际 clock 记录 07:39:29 UTC 为准。预定独立 run32；当前没有 run32 的实际运行、字段、QP 回合、接受点、最终报告或误差证书。

本包把已刊 [R729 完整证明](../results/R729-common-slack-all-row-dual-coercivity-and-feasible-recovery.md) §9 接到完整 R728 / demanded 科学源。它改变的是恢复 QP 在两个明确停止状态之后的有限算法，不改变曲面、均值、全部原自由变量、有限法向链、目标、所有原行、非线性接受规则或已有运行。新 family 是独立源；第31组及其他运行体未改。

## 1. 真正需要解决的原停止机制

已刊 R729 记录的是第25组**原第一段的首个**恢复方向：原 QPv3 在两次 advance 后报告 dependent_blocker_at_zero_step，原最终面投影梯度仍远高于原 tolerance。该事实不能推广成其余方向都停在同一行，也不能由未公开的 transition 推测阻挡行号或线性相关程度。本包不调 rank_tolerance，不删除该行，不将旧负乘子当作可用的新非负对偶点。

原 QPv3 总是先按原完整调用执行。只有：

- phase 恰为 restoration；
- 原 status 恰为 dependent_blocker_at_zero_step 或 dependent_blocker_after_feasible_step；
- 原 maxiter 减去原实际 advances 后仍有至少一个整数轮数；

才执行新的全行 CCD。metric QP、其他原停止状态以及没有剩余轮数的情况直接返回原方向。源码中的新定义与触发记录会如实保留“不触发”情形，不能以未触发记录冒新的求解结果。

本条沿用 R729 的准确收敛证明；这里提供的是完整实际接口、浮点边界、来源与可逐字恢复的代码。没有运行 Python、导入科学模块、AST、compile、fixture、benchmark 或任何本机科学数组。

## 2. 完整源闭包：137 个原对不改，只增加一项算法来源

原完整父是 fixed-fejer-r728-demanded-current-runtime-binding.json：

- 74756 B；
- SHA-256 4af8d6d8ca43a8bc62005e091e0b3baddb6e0e382f0ba6c6ac62247678f3c4ea；
- Git blob d79fd8c5e889f826585cd4ddaf64aeadbc0ef369。

其137个 role/path/SHA 对在新 driver 中逐对原字保留，新增 common_slack_dual_recovery 一项，故当前科学角色数为 **138**。当前 runtime 由23体变24体：20个共享体原字保留，替换 driver、reader、launcher 的完整独立新文件，并新增完整 kernel。

所有当前 seed、mean、meridian、literal Q、normal、frame、C1、stage/adjacent、closure/meridian reuse、packet、geometry/selector、输入与历史绑定体均原字。特别是：

- 原 R728 固定全局负号、R726 完整 mean、两角链及 Slerp 工作定义没有改变；
- 原32段默认法向方程、全部角序、原值/导数路线与 demanded fallback 没有改变；
- 原全部137来源包含完整 QPv3；它仍是原26947 B / fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4 / fabfcd7556a634d19e8dac788d5cb95d696b3d5d；
- 原 envelope、typed history、全部父对象及未知 peer 责任保持。没有把未知 typed 补成空，也没有新增假父 family。

下表是四个新增完整运行文件，目录均为 scripts/resume_20261126/：

| 角色 | 完整文件 | 字节 | SHA-256 | Git blob |
|---|---|---:|---|---|
| common_slack_dual_recovery | fixed_fejer_R729_common_slack_dual_recovery.py | 54333 | 2dfe85c432d91f561a5f9d413f02cbc7d939edab2ea896e7fe4b3f810bc41863 | 2877ba8d6503974b6aa84621997bdc051f523929 |
| driver | fullclosed_fixed_fejer_r728_R729_demanded_qp.py | 99884 | 501313cc50c2a877f98318193a8878242ec13c2f8a0664740a4ea8c47eb4baa7 | 34442907898f84aa99245ece5daca388b334bb34 |
| reader | read_fixed_fejer_r728_R729_demanded_report.py | 93371 | 1464b894cfe2ab2731ab82add4098b759af1ef266730a97e623b0945fda73e9b | 0bc09c5ea5618d0a9759d1f06ad3ea0aea22ca77 |
| launcher | launch_fixed_fejer_r728_R729_demanded_actions.py | 22359 | da440c59c6fbd798b0dc1711a274e5480de9a8ecb1e71d1382976180ea3bd7f3 | edb6504cf8a20b8e98acda3a3de89352ac76bb37 |

增量运行源码合计269947 B。每件小于100000 B；原 driver 99324 B 完整保留后变99884 B，没有为尺寸裁去函数、参数、检查或历史。

本包的“增量四体”以父完整闭包已材料化为前提。完整 binding 列出全部24个当前 runtime，而不声称所有父路径已经 main 可取。如果第31组某个父体尚未正式发布，发布者须同时提供其已保护的完整字节或完整父再生链。准备期 current publication 仍为 null，不能把 protected blob 伪称已执行代码。

## 3. 原实际恢复问题没有换目标或行

原 driver 的 CommonSlackRows 原全文不动。设原实际物理行缓存为 $C^{old}$，每行原记录给出 physical_g $g_i$、正 row_normalization_scale $s_i$ 及实际 gradient_coordinate_norm。准确记 $a_i=s_iC_i^{old}$，$d_i=\sqrt{\|a_i\|^2+1}$。实际代码继续使用原已经构造的 factors、slack_column、bounds 与 tau0，不用替代公式重造物理梯度。

增广变量 $x=(z,t)$，$\tau=\tau_0+t$，所有原行和最后的非负 slack 行为

$$
C_i=(a_i^T/d_i,-1/d_i),\qquad
b_i=(\tau_0-g_i)/d_i,\qquad
C_{m+1}=(0,\ldots,0,-1),\quad b_{m+1}=\tau_0.
$$

最后一列统一写为 $-\beta$，每个实际 $\beta_i>0$；原零物理梯度、重复、近相关或精确相关的行都留下。初始 tau0 的原机器 epsilon padding 是原 slack 初始化，未变成新的几何接受余量。

原完整目标是

$$
f(z,t)=\frac12(\tau_0+t)^2+
       \frac{\mu^2}{2}(\|z\|^2+t^2).
$$

因此 $H=\operatorname{diag}(\mu^2 I_n,1+\mu^2)$，$q=\tau_0e_{n+1}$。尤其**没有丢掉 $\mu^2t^2/2$**，没有换为纯最小 slack，也没有改为 metric 的 Hessian。damping 取原本次实际 used_damping；原外层拒绝后的调整仍由原 driver 执行。

kernel 在实际调用中绑定完整原 QP report、同一次完整 row metadata、原 bounds 词、实际 tau0/damping、原完整坐标方向、当前 model 与 starting_geometry 的完整 point SHA。CommonSlackRows 的实际类体来源同时保存为完整新 driver 的 file record。纯读器会把该来源再与完整 actual driver 相比。

这些是同一真实问题的接口核对，未新增独立科学门。字段仍未知时不预填值。

## 4. 完整 Gram 的构造与正象限条件

全行对偶是

$$
\min_{\lambda\ge0}\ \psi(\lambda)
 =\tfrac12\lambda^TG\lambda+r^T\lambda,\qquad
G=CH^{-1}C^T,\quad
r=b-\frac{\tau_0}{1+\mu^2}\beta.
$$

只在实际触发后建立小行空间 Gram。完整 physical 列按原 active_block_columns 连续流过：

$$
G=\frac1{\mu^2}\sum_B C_{\mathrm{phys},B}
 C_{\mathrm{phys},B}^T
 +\frac{\beta\beta^T}{1+\mu^2}.
$$

循环覆盖全部原高维坐标，最后公共列也完整支付。没有选 top rows、删 envelope、重新选几何行、低秩截断、特征值裁剪、伪逆或额外正则。原完整缓存没有被复制为第二个完整行矩阵。

工作浮点累加后使用 $.5G+.5G^T$，同时记录未平均前的最大不对称量。这在准确算术与原 Gram 同一；有限浮点字可能不同。它不是已付误差界，也不冒成严格半正定证书。任何非有限 block/product 或非正工作对角使新增算法停止，并保留原可用方向及完整异常。

R729 的关键下界来自全部同号 slack 列：

$$
\lambda^TG\lambda\ge
 \frac{\beta_{\min}^2}{1+\mu^2}\|\lambda\|_1^2
 \quad(\lambda\ge0).
$$

这使准确对偶的非负 level set 有界，允许 G 在整个空间奇异。源码没有将其转述为 G 全空间正定，也没有用它拒绝冗余行。报告中的 beta 最小值和系数是实际工作读数，仍不是有向舍入证书。

## 5. 全循环 CCD 与原预算的真实单位

新的乘子从全零开始。没有读取原 active-face signed multipliers 来构造初值。每个 full sweep 按原完整行顺序访问 $i=0,\ldots,M-1$：

$$
\lambda_i^{new}
 =\max(0,\lambda_i-(G\lambda+r)_i/G_{ii}).
$$

所有 M 行每轮都访问；零更新也计为一次 coordinate visit。非零变化另记 nonzero_coordinate_updates。每轮结束从同一个完整工作 G 重新形成梯度，保留与逐坐标累加梯度的差，不伪称两者都读过原 C。

预算表分别保留：

- original_limit：原 maxiter 数值；
- original_CG_advances：原完整 report 的实际 advances；
- remaining_full_sweeps：二者之差；
- full_sweeps_started / full_sweeps_completed；
- coordinate_visits / nonzero_coordinate_updates；
- incomplete_sweep_coordinate_visits；
- 每一完整 sweep 的全部行访问数和工作对偶诊断。

这里沿用的是同一个整数上限的**新算法分配**，不是相同计算量。原一次 CG advance、新一次 full sweep、一次 coordinate visit 是三个不同单位。新源没有把 M 次坐标更新写成一次原 advance，也没有在原64之外另加64轮。

例如，仅当未来某次原完整报告真给出 limit64、advances2时，可分配62个全 sweep；本包没有预言第32组会返回这组数。循环没有另设科学精度门，也没有凭工作 stationarity 小就声称达到原 nonlinear 目标。准确无限循环收敛只属于已刊R729，有限剩余轮数不保证收敛。

## 6. 只在末端恢复一个高维新候选

每轮 CCD 都在完整行空间执行，不在每一坐标或每一轮后额外构造高维 z。所有剩余 full sweeps 完成后，原完整 C 的转置才实际产生

$$
x_\lambda=-H^{-1}(q+C^T\lambda).
$$

然后原 C 再读，得到同一个 z 的每行 $u_i^Tz$，计算

$$
L(z)=\max_i\frac{u_i^Tz-b_i}{\beta_i},\qquad
t(z)=\max\!\left(-\frac{\tau_0}{1+\mu^2},L(z)\right).
$$

这是固定 z 下原完整目标的最优 scalar formula；最后的非负 slack 行也在这个最大值中。源码不加入额外向上 padding，不用改变原 finite tolerance 掩饰舍入。exact_optimal_scalar_formula 只标识数学公式，旁边明确 binary64_evaluation_is_not_exact_arithmetic。

原 QPv3 返回方向与零方向各实际核对，新的 repaired direction 也用原 C 重读。只在原 finite feasibility_tolerance 内且完整目标有限的候选中选最小原 regularized objective；相等时保留先出现的原候选。最终选择后再做一次完整 C 及需要的 C transpose 读取。

每个真实候选保留完整坐标词摘要、全 normalized rows/slacks、原 physical rows 的完整实际产品与 $g_i+s_i C_i^{old}z$。不会用 Gram 中的预测替代最终实际行余量。

## 7. 实际 C 重读、有限失败与原方向保全

每个完整列流都核对 shape、finite values、全部列以及实际顺序，保存明确标注为“按列块顺序”的完整词摘要。该摘要没有冒称行优先 NumPy 数组 hash。实际 original physical row 流另有整流摘要。前后原 C 或原 physical rows 的词变化会记录具体错误，不采用新的未核方向。

异常记录保 type、module、message、repr、完整 traceback 与发生阶段。新增分支不删改原 QP 的任何 error、history、transition、multiplier、replacement 或 finite stop。

失败时优先回到已完整核过的原方向或零步。若新增 final C reread 本身失败，则明确 final_original_C_reread_complete=false；保留的原 QPv3 complete-C return 具有单独标签，不能说它是一次成功的新 C 重读。没有在错误后以新 report 假造 KKT。

这种保全仍不把旧有限可行方向当作 nonlinear 可行。外层原实际 field/geometry 检查和接受式照常执行，原疑难问题与未知失败责任不会因为 kernel 新增而消失。

## 8. 新旧报告与纯读取的边界

原 record['qp'] 是**原 QPv3 尝试**的整对象，原 schema 仍正确属于它。kernel 保存该完整对象 canonical hash，并在返回前核其未被改写；原 returned coordinate words 也未被原地修改。

新增 companion 为 R729_common_slack_fallback。它记录新触发、预算、各次完整流、所有实际候选、选中来源、是否采用回退、全 lambda、实际 dual/selected-primal 诊断及错误。新 driver 顶层 schema 为 complete-fixed-fejer-r728-R729-demanded-SO3-QP-v1；新 pure schema 为 actual-fixed-fejer-r728-R729-demanded-SO3-readout-v1。

| 内容 | 原字段所指 | 新字段所指 |
|---|---|---|
| qp_status / advances | 原 QPv3 完整返回 | companion.triggered、status、budget |
| final_face_projected_gradient_norm | 原 active face 的旧 Pg | companion.final_diagnostics.actual_C_dual_projected_gradient_mapping_norm |
| 原 qp.maximum_linear_violation | 原 QPv3 方向 | companion.actual_selected_direction.maximum_linear_violation |
| 原 qp.coordinate_norm | 原 QPv3 方向 | companion.actual_selected_direction.coordinate_norm |
| driver coordinate_step_norm | 实际交外层的方向 | 与 companion 选中完整方向对应 |
| actual_QP_seconds | 调用区间包含原 QP 及新增回退 | qp.seconds 与 companion.seconds 各自仍分列 |
| 原 normal/field counts | 真实原 F/J/root 调用 | companion 的纯行代数计数独立；新增 F/J/root 为零 |

纯 reader 的原 direction 函数保留全部原行，仅追加独立 checker 结果和 original_QP_fields_scope。原 legacy selectors 继续可读，但不能把其旧 Pg、step norm、status 偷说成新的 dual KKT。新字段明确给出被原 outer trial 实际消费的来源、原 C 余量、完整 objective、slack、计数及是否采用。

新的纯绑定仅使用标准库。它从实际完整 report 读取，不打开 mutable progress、不运行 NumPy、F/J/root、积分或数组。原 source/model、全部 normal snapshots、packet、history、field、真实接受检查全部保留。

## 9. final dual、primal 与 gap 都来自实际全 C

在实际完整转置及行读取后，报告分别给出：

- $h_{\mathrm{actual}}=b-Cx_\lambda$；
- $h_{\mathrm{Gram}}=G\lambda+r$ 与二者的实际差；
- $\lambda-\max(0,\lambda-h_{\mathrm{actual}})$ 的 norm / max；
- 实际选中 y 的 $Hy+q+C^T\lambda$；
- $x_\lambda$ 的相同 stationarity；
- 两者的完整最大线性违反与互补余量；
- 原目标 $f(y)$、由原 C transpose 形成的 $D(\lambda)$；
- 数值 gap 及准确恒等式两项的浮点差。

准确恒等式是

$$
f(y)-D(\lambda)=
 \tfrac12(y-x_\lambda)^TH(y-x_\lambda)+\lambda^T(b-Cy).
$$

如果 y 只有原有限 tolerance 内的可行性，右端不能自动当作严格非负上界证书。所有现 source 数值 gap/stationarity 都明确 numerical only / exact certificate false。旧 face Pg 不用于构造其中任何一个数。

完整外层仍实际读取其自己的 selected_linear_physical_g。pure 会单独展示其与 kernel 同一完整原 physical C 重读的逐词比较和最大差；差异不会被隐藏成“缓存同值”，也不改变任何真实 nonlinear 接受阈值。

## 10. driver 只增加必要调用，未重排原数学

完整 driver 的六个精确文本改变是：

1. 新独立 report schema；
2. 原字 registry 前增加一个 kernel role；
3. 原 qp 模块旁加载新 kernel；
4. report 加 kernel 完整 definition；
5. 原 qp.solve 已完整返回且 record['qp'] 已保存之后调用 recover；
6. docstring 明示 R729 恢复算法。

原 CommonSlackRows 及其他所有函数正文、parse_args、现有 main 语句都保。新增 recover 位于原最终原 C 物理行读取、coordinate lift、direction NPZ、line trial、normal packet capture等原后续逻辑之前；原后续相对顺序不变。原 QP 的 actual_QP_seconds 计时区间因此包含新增回退，旧 qp.seconds 仍保留原尝试耗时。

reader 有九个精确来源/消费插入，launcher 有四个准确来源/声明插入。三体都能按完整反向补丁逐字回到三个完整父的原 SHA；这只是文本构造事实，不是执行或编译声明。

## 11. 工作量与真正能改善的范围

设高维物理坐标数 n、完整增广行数 M、原 column block 大小 B，剩余 full sweep 数 s。

- Gram 一次约为 $O(nM^2)$ 工作；
- 全 CCD 为 $O(sM^2)$；
- 少数完整原 C/C transpose 读取为 $O(nM)$ 每次；
- 附加存储为 $O(M^2+MB+n)$，含有界 block buffer 与少数完整方向向量；
- 没有第二份 $M\times n$ 完整行 cache。

因此本条不是免费恢复，不以原两次 advance 推测实际运行时间。它试图让原同一 QP 在近相关阻挡时继续产生合法的同问题方向，**不能据源码宣称更快收敛或一定得到更好的 nonlinear g**。新方向也可能被原 line search 全面拒绝。所有完整 budget、场评估、每试步六族、typed append-only 和准则都保。

它不优化 normal evaluation、整面 scan、mean、32stage 或 root cache，不用它解释旧整面数十分钟的耗时。相反，这些调用按原完整源等待真实返回。

## 12. 参数、历史、raw 和后继消费

本包不包含新科学参数 ready；原31完整157 scientific argv与7 pure argv语义、458/445 formal路径、64 live、所有旧预算和五个原 peer CLI均保持，后续参数包只显式接新来源/namespace并可增加独立 R729 诊断投影。没有修改现有 ref、queue、controller、running job 或根 README。

原完整13成员 final、typed 和 same-source restart 守卫没有放宽。新源不能把旧31 report 冒成自身的 complete restart。若将来需要消费跨来源父字段，仍需真实的完整来源/参数/字段合同，而非当前准备时填未来 SHA。

物理 kernels 原字相同不代表旧严格准确 reader 自动接受新 driver。现31 N/G/R723/P/U/mesh的 source pins 保持其原范围。将来若对新实际32场接准确后继，必须明示新 whole report/reader/138 roles；不得因为 model 某部分同字而把未归因的值当证据。

所有 C、方向、Gram、checkpoint、完整科学 report 和后处理 raw 都继续只在真实 runner。Git 本包仅完整源码、绑定、再生器、说明及完整交付表；未来实际字段全部 null。

## 13. 逐字再生与 whole 恢复

完整 MJS：

    scripts/resume_20261126/reproduce_fixed_fejer_R729_common_slack_family.mjs

它内嵌整个新的 kernel 正文，持有三个完整父文件的身份和全部19条精确文本补丁，完整检查正向输出与反向父字节；再整字复制其余20个当前共享 runtime。输出全部24个当前 runtime 和一个纯文本 construction record。没有启动 Python、科学模块、AST 或数值求解。

命令形式：

    node reproduce_fixed_fejer_R729_common_slack_family.mjs \
      --source-directory <完整31脚本目录> \
      --generated-directory <完整文本输出目录>

上述命令是源码恢复能力，不在新 science 队列中加一个前置步骤。父源若不在本地，可先用父完整 source delivery 中的全 blob 或其完整再生器恢复；不能截取函数拼一个简化求解器。

每个新增文件都有完整 Git blob。一般精确恢复为：

    git cat-file blob <完整git_blob_sha> > <原完整path>

再以表中完整 bytes/SHA-256 识别。不能从运行输出重命名为输入、不能把二进制数组转码入 Git，也不拆块规避文件限制。

本次实际做过的仅是完整小源/证明读取、源码字符串生成、whole hash 与精确文本反替以及 create_blob 保护。源码运行、whole field、QP候选、有限 convergence、速度与 task success 均没有被该准备替代。

## 14. 完整来源定位

当前完整绑定：

    computations/fixed-fejer-r728-R729-common-slack-current-runtime-binding.json
    50082 B
    SHA-256 dfd6c5de398fe33fcc44bb4c4d0bb3ddcbf72069ce0432836ff3d42c794c4af5
    Git blob ffc501b19d28899f3e0e0d92b4613f747768d594

完整 MJS：

    76965 B
    SHA-256 8bc71f6644fa4c4248bd4aae2ff58c034f73f661bdcf6768ca85f9c18ab442f5
    Git blob 55afa3b6ab7dd882bb350791a439ad3299d9979f

当前 R729 proof 的实际最终字节为16220 B / d6104084c6a96651e478ab4c0b7f25124ca5859ae03e49fdb4d3a35c9264c87a / a66c19196b798957a6f905c23e47b2b500b60dd8，真实 publication f687c963cbc899e211a3d083c12b2f1b7e322d4d。此前143e7f1的16278 B版本只属完整历史；本包没有把旧数学分隔符版本冒当前 whole 身份。

父 source delivery为40338 B / 5d7d7c0e8fb3c104e797ebe97c98fc6f7fc1c9efa4ce996b54b3b51ac3d35284 / 182b065be81e7f9c0e8fdc84b82d22c2da494fed；父完整 MJS为69141 B / eec4ae51b7a83ebc10b1ec3f39be24570509def85e21538d7bfc65407b84988b / e2523d56f2c5796ae2e2470c882acd6b186c4872。当前完整 binding还持有原参数6件的whole总表与精确JSON pointer，未截断其历史。

当前包只是准备成果。所有实际32数据需由真正公开 Actions 的完整返回给出。

## 15. 准备后收到的真实父执行闭包出版记录

根代理随后明确给出：第31组实际运行必需闭包已经 main 8591fc4c0ce0a3e4ec26e9e1d0728f95b5b28d48，官方 run46122200592/attempt1 于2026-11-28 07:39:20 UTC启动。此时只知道 in_progress，不推测输入返回、物理值、QP状态或最终结果。

该实际 publication 包含20个新 runtime加3个原 runtime、完整137科学角色和三个完整执行步骤。另有12个非 runtime再生/重复ready等481099 B仍待容量；**不能把这次出版说成39件全已main**。本包以完整 Git blob 和精确父引用保留那些准备附件，不把尚未发布的附件路径假装已可从main读取。

这个后到事实不回填准备时 current_scientific_source_publication=null，不改四个终运行体、旧137对、kernel目标、任何数值预算或第31组在途对象。它使本包增量四体所需的20个共享当前 runtime已有明确父运行闭包出版依据。第32组自身仍未运行；其 future actual仍全部null。

纯 readout 的实际方向列表名为 actual_metric_directions / actual_restoration_directions；新 companion 精确位于这两个列表的各项内。完整 binding 的三个 pure JSON pointer 已按真实 reader 更正为 /actual_{metric,restoration}_directions/{index}/R729_common_slack_fallback/...。科学 report 的原列表仍是 metric_directions / restoration_directions。此项只更正参数引用说明；四个完整 runtime 字节不变。
