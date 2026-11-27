# Run16 全闭面、全相位与握持消费者：完整来源适配及 R718 可选距离下界

本说明对应独立完整源 `fixed_fejer_stage_observed_closed_phase_grip_evidence.py`。它从已刊 `fixed_fejer_complete_closed_phase_grip_evidence.py` 全体派生，将来源严格接到实际 run16 的 stage-point-observed 完整场及六个准确费用源，并在原有全目标盒距离之外增加 R718 的同场闭面流距离下界。它不改变物理场、自由变量、32 个 normal 阶段、全圆/全径向覆盖、原支持参数选择或原闭面证明。新下界只在原共同正支撑及闭面条件全部成立之后计算，最终距离取原盒界和新流界的最大值。

本文件是被运行源严格 pin 的完整数学与实施说明；新运行源、完整参数、逐字再生器的最终 whole SHA 与 Git blob 另记在同批交付总表，避免说明与运行源互相包含 whole SHA 的循环。所有执行只在公开 Actions；此交付只有 V8 完整源文本构造与定向数学推导，未执行 Python、科学模块、F、J、根、积分或科学算例。

## 1. 完整父体与来源范围

唯一完整算法父体为：

- 路径：`topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_closed_phase_grip_evidence.py`；
- 71,420 bytes；
- SHA-256：`d606055d1b247d8354ac320bc28a0f40f4b00cbf1ff530a9b6bb2e80dec80bb9`；
- Git blob：`33d9ee5b22c3e8bb5a92262ca7af7b89f20bb78b`；
- 已刊提交：`cbfd5619d12fe4a7c66cb0f2eba76adfa7e7049b`。

保留它的全原输入读取、全部 journal/stream 重读、32 阶段与全周期同支核验、全准确六jet、source-specific 端口与下片反射、两完整 p4 帽、所有相位、原八个 beta 证据角色与单独径向延拓角色、原 `e0b44` 有理消费者、共同支持参数两分支、两遍全支持行、独立无标记 reach/外管解释、握持区、全目标盒距离以及末次全部输入/输出字节复验。

当前 field、point、snapshot、目标、完整模型均从原完整准确几何输入读取；不把 prepared reference、实时数学进度、cache 计数、旧 point 或旧场费用替换成新场证据。原未返/未知历史责任不因消费准确上片而消失。

## 2. Run16 的真实完整科学与费用来源

本消费者通过下表六源和其原严格 source closure 接入完整 run16：

| 角色 | 完整 basename | SHA-256 |
|---|---|---|
| accurate input | `fixed_fejer_stage_observed_normal_packet_accurate_field_input.py` | `720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3` |
| whole radial/control boxes | `fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py` | `03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd` |
| normal32/sixjet producer | `fixed_fejer_stage_observed_complete_normal_root_and_sixjet_fees.py` | `24765a9049f38e6b68f1e1d457d514054557b17731ac390dade82605682d2673` |
| physical leaf binding | `fixed_fejer_stage_observed_complete_physical_leaf_binding.py` | `280bc1cf1d91bfd60b7d905045c07ccefd901833c9734e1b3c3496f5d4afd652` |
| continuous Gram/K/support | `fixed_fejer_stage_observed_continuous_gram_curvature_support.py` | `3f383d692711d180d0f7fd24e78ce67973c85b8c231e28deb135122664dd3560` |
| complete beta bridge | `fixed_fejer_stage_observed_complete_geometry_support_beta_bridge.py` | `35493133665555aecf40eb85d213d53fb2b4fbf4acf949b403c258cbb24787a0` |

这六源已完整刊于 `e8412068e813c54780299a2596262e1075613e6d`。它们的原数学正文保留，包含原共享 `29eed` interval/SO3 核、全部准确 scalar/whole reference 与支持拼接费用；本适配不重抄、截断或放宽这些核。

实际科学来源为完整 driver `8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d`、pure reader `c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f`、normal `42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10`、immutable packet `140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf`、source binder `9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f`，共 120 个完整科学 source roles。

`actual_mathematical_observation` 是运行中的只读标量观察，不是 immutable packet 或准确费用。消费者只接受完整同点 packet 及其全部原 journal、实际模型/全部 source、固定 reference 和精确目标绑定；不能把进度里的 Phi、Gram、g 或 point 当作上述对象。

## 3. 真实必要输入与未来场的边界

Run16 是 `46037017666/1`。其真实阶段 1–2 完整小卷为：

- `notes/2026-11-27-public-actions-46037017666-1-part-001.md`；
- 16,596 bytes；
- SHA-256 `a17878d025623ae6280d6b1afa42d9be36288f72c93b3802659453d205ed5b17`；
- Git blob `8d49505495b777f7cc84c73c15fee4247ff76ff9`。

它记录当前完整参考模型 `ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac`、数学配方 `957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`、完整目标定义 `50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319`，并分别保留六个真实文件以及真实 producer/source commit。完整 reference binding 的 whole SHA 是 `9edf8a4dd6edec259f615362f1155a811dff79e257de8d1a7579be924fe6a0eb`，preparation whole SHA 是 `ff41237c4b6caf4eac6fd82f90212ff44c54930ba00c24a923a1ddc8b9cbc373`。

当前 scalar 是完整 2218 叶，实际 `accuracy_reached=false` 原样保留。历史 2397 叶属于旧 carrier 恢复责任，不替代当前准确 scalar/reference。已完成必要输入不表示物理场、normal 费用或几何证书已完成。

完整 ready 明列上述真实输入出处，但运行源仍重读实际 geometry/normal 上游与 120 roles，不以 ready 内一个相同数学 hash 省略文件、模型、point 或 source 关系。未返回的 geometry report、current point、snapshot 与本消费者结果 SHA 一律为 null；实际同点 complete-required-angle immutable packet 可以作为费用输入，不强加 accepted/final 前提，也不以 partial cache 冒完整点。

## 4. 原闭面、相位、帽与混合 pair 责任全部保留

当前 M160/J923、3×923×482 的 SO3 控制布局和完整 free-height 未变。固定 material chart 来自完整 Fejér reference；当前 157 个自由核心系数必须从真实完整点重新读取，不能替成固定参考的七项配方。

准确物理表示仍是 R715 完整校准形式：

\[
U=(1-h)P+h\Gamma+\int_0^sT-(1-h)\int_0^ST,
\qquad
h=1-10(s/S)^3+15(s/S)^4-6(s/S)^5 .
\]

全 \(h,h',h''\) 项和 raw closure defect 都保留。由完整零端口掩码与支持远离端点，核心端口为 \(\Gamma\in\{z=0\}\)、\(U_s=e_z\)、\(U_{ss}\) 水平；帽端口为 \(R e_r(\Theta_0)+He_z\)，\(U_s=-e_r(\Theta_0)\)、\(U_{ss}=0\)。下片用 signed radial chart \(J_zU(-u,\phi)\)，交叉项符号按原全六jet 保留；帽用 Cartesian disk chart。严格帽 cuff、全上片 immersion 与全圆分支/接缝证明仍由原完整输入付。

物理相位仍为
\[
U_t(s,\phi)=R_{\alpha(t)}
U(s,\Theta_0^{-1}(\Theta_0(\phi)-\alpha(t))),
\qquad \alpha(t)=\pi t/2,
\]
并保固定 Cartesian p4 帽。相位一的全像包含核心旋转点；不是将原 material \(\phi\) 误当物理转角。

一个共同 \(A_\beta=\operatorname{diag}(1,1,\beta)\) 必须同时覆盖全部活动相位、反射下片及固定 p4 帽；原两遍支持行与帽正分子条件不变。R650 的 embedding/outwardness 与全部 mixed pairs 的 reach 来自这一共同条件，不能由 core-only 支撑、半转或某个局部帽推代。

## 5. 原盒距不变

原 `CompleteTargetDistance` 仍读取四个准确相位一核心点，对每个完整上片 position box、每个下片反射 box、两完整固定 marked caps 求距离下界，再对源点取最大值。wide box 只能给较弱或未付界，不允许删除该目标组成部分或用同 material 点位移替代整像距离。

原三维盒界、原径向/帽 hull、R717 同叶全三维 norm 的完整 D 上界、所有真实 IDs/数量/最弱位置都保留。新报告还明确保存 `original_complete_box_distance_lower`。添加 R718 后的 `rigorous_delta_hold_lower` 是原已付盒界与新已付流界的最大值。原 formal compact-image 计算字段不被重新解释成新流结果。

\(\delta_{\rm hold}\) 按原题是 \(\max_t d_H(F_t(M),F_0(M))\)，不做刚体对齐。握持区的四仿射独立点仍是原附加几何事实，不构成 \(\delta_{\rm hold}\) 的商空间或前置条件。涉及任意刚体、含反射的 \(\delta_E\) 仍单独未付。

## 6. R718 的完整前提与来源

新增强严格引用已刊：

- `results/R718-positive-definite-flow-distance-and-whole-image-held-witness.md`；
- 18,614 bytes，SHA-256 `fd92e569e7d793367f96a0748be5cfc54670a6333c18f413f8cce27da1083feb`；
- blob `eac02006003d157dca1db3e49192316da7d4b311`；
- 提交 `0f43c0f05b8f33b828034b9b5b99f875fa2ca959`。

源中增强调用放在原 `evidence_package` 已完整写入/验证原八角色，并且主报告已获得 all-phase embedding/outwardness 之后。调用再次要求原完整闭 C² sphere immersion、连续全局法向、共同中心 \(0\)、正 \(\beta,\sigma\)、准确 \(A=\operatorname{diag}(1,1,\beta)\)、全支持行数和全部相位关系。若这些前提缺失，R718 字段保持 null/未付，不能反向用本下界补这些前提。

R650/R718 给目标闭面 \(S_0\) 的唯一全流横截。在外部写 \(x=e^{TA}p\)，\(T\ge0\)，令 \(m=\min(1,\beta)\)：

\[
W(x)=\frac{e^{mT(x)}-1}{m},\qquad W=0\ \text{于内域}.
\]

R718 证明 \(W\) 全空间 \(1/\sigma\)-Lipschitz，故

\[
\operatorname{dist}(e^{sA}p,S_0)
 \ge \frac{\sigma}{m}(e^{ms}-1),\quad s\ge0.
\]

此距离针对整个同一 marked 目标闭面，包括活动片、反射下片、两完整固定帽；这里不采用 core-only 目标或忽略 p4 的距离。

## 7. 准确核心轴与真实零高度

原 `current_core` 从完整 x 读取全部 160 个实际系数。设
\[
p(\theta)=1+\sum_{j=1}^{160}c_j\cos(2j\theta),\quad
X=p(0)=1+\sum c_j,\quad
Y=p(\pi/2)=1+\sum(-1)^j c_j.
\]

这些是以实际 binary64 词为精确 dyadic 有理数得到的量；不调用浮点三角函数或浮点除法来声称准确轴比。原完整 current-rho 证明与原固定 chart 身份仍逐对象核验。

R715 原准确物理端口给核心 \(z=0\)；\(H\) 是帽高度，不能混成核心高度。实际源的 `_core_and_cap` 和全 raw-lift 六jet端值保留这个关系。因此当 \(X\ge Y>0\) 时，取
\(p_0=(0,Y,0)\in S_0\)、\(q_1=(0,X,0)\in S_1\)；当 \(Y>X>0\) 时，取
\(p_0=(-X,0,0)\in S_0\)、\(q_1=(-Y,0,0)\in S_1\)。
两者都满足
\[
q_1=e^{(\log r)A_\beta}p_0,\qquad
r=\max(X/Y,Y/X)\ge1.
\]

所以
\[
\delta_{\rm hold}\ge
\operatorname{dist}(q_1,S_0)\ge
\frac{\sigma}{m}(r^m-1).
\]

这里只使用已付的同一个 marked-surface \(\sigma\)；没有把 R716 无标记支撑直接冒 marked 支撑，没有漏一次 mark-height 费用。本实现不需要另做 mark-height 三角扣减，因为两完整 marked caps 已在共同 \(\sigma\) 内。R718 的一般非零高度/近流点公式仍保留在证明中，但本源没有把未知高度自动置零。

## 8. R719 的可选统一轴比，仅在实际前提齐时记录

已刊 R719 为：

- `results/R719-fixed-first-three-fejer-modes-preserve-current-axis-gap.md`；
- 9,212 bytes；
- SHA-256 `f043c75457173c9cfa5bbf7b0b9710049edfcb075d31d474231554285768cff7`；
- blob `7d36e880635aa92c5853703391f8bdd326bcc40c`；
- 提交 `5c546ca968372159773fcc6e7d93d15bb7138d6e`。

其前提是全当前有限 M、完整连续 \(\rho=p+p''>0\)，以及当前首三项确为固定 Fejér 前三项：\(c_1=7/16\)、\(c_2=\mathrm{RN}_{64}(-3/40)\)、\(c_3=\mathrm{RN}_{64}(3/112)\)。源先核实际全 point、完整 fixed-input/模型首三项相同，再以精确有理数核这三项及后二项误差不超过 \(2^{-53}\)，并保留全 current-rho 证据对象。完整 source-bound fixed-input 配方已经核 RN-even 关系；这里不会用一组仅数值近似首三项替代该来源。

R719 允许所有后续自由模式非零，仍给 \(X/Y>7/3\)。本消费者始终计算并使用全部实际系数的准确比；统一 \(7/3\) 只作为已满足定理前提的附加结论，不覆盖真实比、不拿初始七项代替当前核心。当定理前提未齐时不记录该统一界，R718 仍可使用其自身已付条件下的真实正轴比。若前提齐而准确全系数比违反已证结论，作为完整来源/算术不一致报错，不伪造改善结果。

未刊的新三矩强化、其他未来轴比常数或预期优化结果均不接入本源。

## 9. 可执行的定向有理幂下界

本增强不需要调用 transcendental libm，也不把浮点 \(\mathrm{pow}\) 当准确包围。若 \(m=1\)，直接取准确 \(\Lambda=r\)，完全无幂近似。

若 \(0<m<1\)，令 \(z=(r-1)/(r+1)\in[0,1)\)。利用
\[
\log r=2\sum_{j=0}^\infty\frac{z^{2j+1}}{2j+1}.
\]
所有项非负，前 32 项是下界。以 \(Q=2^{96}\) 定义
\[
\mathcal D(v)=\lfloor Qv\rfloor/Q\quad(v\ge0).
\]
源使用准确 Fraction 整数除法向下量化 \(z\)、\(z^2\)、各次幂、各项及部分和，每个中间量仍非负且不大于相应准确值。所得 \(\ell\le\log r\)。

再令 \(u=\mathcal D(m\ell)\ge0\)，用 \(\exp u\) 的常数项 1 加前 32 个正 Taylor 项。各递推
\(t_j=\mathcal D(t_{j-1}u/j)\)、
\(E_j=\mathcal D(E_{j-1}+t_j)\)，初值 \(t_0=E_0=1\)，保证
\[
1\le\Lambda=E_{32}\le e^u\le e^{m\log r}=r^m.
\]
其中常数 1 精确保留；\(r=1\) 如实只得零距离。

最后向下量化
\[
B_{\rm flow}=\mathcal D\!\left(\frac{\sigma}{m}(\Lambda-1)\right)\ge0.
\]
因此它是 R718 严格允许的完整距离下界。所有量化误差都朝削弱下界的方向，已包含在输出值里；无需额外浮点舍入预算。32+32 项是这一个可选单点纯有理后处理的固定精度，不是删减物理阶段、角胞、support rows 或积分范围。

当 \(m=a/b\) 为正有理数时，上述证明也蕴含 \(\Lambda^b\le r^a\)。源不执行可能含巨大分母指数的整数幂比较，明确记录 `integer_power_comparison_executed=False`；不能把一个未执行的幂比较冒作已返回检验。输出保留 \(m,a,b,r,\ell,u,\Lambda\)、项数和向下量化位数，以完整 source/proof 关系恢复该界。完整准确 \(r,\sigma,m\) 的来源始终保留。

如果此可选有理增强单独遇到 MemoryError，仅保持原完整盒距并记录可选增强没有产值；输入、source、point、journal、数学前提或一致性错误不会被吞掉。原闭面/支持流程仍是完整执行，不以本增强作为新门。

## 10. 报告与晚失败语义

主报告新增：

- 原 `original_complete_box_distance_lower`；
- `R718_flow_distance_lower` 与完整 `R718_flow_distance_evidence`；
- `R718_optional_bound_status` 和 `R718_flow_distance_used`；
- `R719_uniform_axis_ratio_proved`；
- 原 holding/grip 摘要中的两界与最大值归属。

R718 完整证据明确同一 point/model/target/snapshot、原 geometry binding、实际核心词身份、共同支持、两个定理全文来源以及源点/目标点所属相位。它仍要求本消费者最终主报告 complete、状态为 `complete-same-field-consumption`、末次全部输入及生成文件字节复验为 True。主报告失败时，新数值及新推广字段与原数值一起清为 null，保留的 provisional 内容只能诊断，不能独立消费。

原 R716 副文件的严格合同不变：必须通过最终完整主报告与其中唯一准确 whole record 读取；副件自带“需要最终报告”的标签不能代替主报告。不同 followup 可位于不同 checkout 绝对路径，原输入/源码记录按原实际路径完整重读；合法当前模块副本仅经完整 SHA/bytes 相等关联，不能改名省略来源。

## 11. 全部原阈值、参数和未付责任

原完整参数仍为 8 个 argv：
`--repo`、`--geometry-report`、`--outdir`、`--support-chunk-rows 4096`。
仅独立 source、geometry 路径和 fresh 输出目录改变；4096 是写出支持片段的大小，不改变任一数学域。全部旧 57 个 scalar selectors 原键/字段保持，另加真实 R718/R719 结果读数；没有删减旧输出、输入、帽、相位、预算或证据角色。

保原 \(0.03D\) reach、\(10^{-6}\) relative Gram operator norm、\(0.2D\) 握持尺寸、\(0.05D\) 原握持幅度与 \(0.2D\) 强幅度目标。新 flow 界只更新原 \(\delta_{\rm hold}\) 最大下界及由此得到的两个幅度判据；不声称 Gram、曲率、reach、握持区尺寸或 \(\delta_E\) 自动成立。R717 完整三维 D 上界沿既有 geometry 正常传入，没有用 core diameter 替换全像 D。

本源不产生全十二通道体矩、mesh、同 g 收敛或准确解存在证明；相应字段和 remaining 原样保留。完整 consumption 可以成功而研究目标仍未完成。没有当前实际 complete immutable snapshot/费用输入时不能预填任何新结果；live progress 仅作为实际运行状态，不能升级。

## 12. 完整复现与保存

配套再生器只读取固定已刊 d606 全体和本批完整说明/准确依赖，要求父文件 whole SHA/bytes 后按显式完整替换列表产生全新完整 source。它逐项核出现次数，核最终输出 whole SHA/bytes，逆向逐项还原同一个完整父体；源码文件不是摘要或运行时 patch wrapper。依赖的原 proof/source 不改。

交付包括完整运行体、完整说明、完整 stdlib 再生器、完整 ready 与小总表。全部 raw support chunks、beta 证据、geometry/normal journals、point/packet、输出报告留在真实 runner；Git 只保全源、完整参数、数学证明、恢复与公开运行身份。root 独占 refs/queue，本交付不修改现有运行源、活队列或已返历史。
