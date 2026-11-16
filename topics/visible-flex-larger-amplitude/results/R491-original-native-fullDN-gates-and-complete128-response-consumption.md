# R491：原有限 native/fullDN 主门、混合端点 Jacobian 与 binary128 四组件的正向消费合同

作者：ChatGPT / amplitude（AI 辅助研究）  
日期：2026-11-16

**可信度：已证明（限本文逐源控制流、所列有限线性代数条件与来源组合命题）；没有新增科学运行，没有宣称 request215、原 native/fullDN 或闭面任务已经接受。**

## 1. 结论与实际范围

原 native 响应从来没有“全部 338 行必须解析微分”的接受条件。原 worker 对完整端点矩阵先作对称差分，再替换 112 行 slope 和一行 meanSlopeCorrection；second、meanSecondCorrection、height 行仍保留原对称差分。原 TailClient 要求这些完整行存在且有限，没有对“全解析”作判定。原 fullDN 的 AffineTail 只取完整矩阵的前 M 行作为内层非均值 DN Jacobian。因此 a090 实现的混合结构不能单独解释 native/fullDN 未接受，更不能把全解析化添为原门。[S1–S5]

实际204已有一项独立的有限计算进展：R446读到 owner 原阈值内末态、独立全残差/全226输出逐词 replay，以及四组件完整返回。R446没有读到溢出的 111829 B 必要摘要正文，不能补写其中的线性残差、端点数值、audit 极值或 backend 统计。request215 保留原科学实现，改必要元数据表示，预期可返回的字段在第6节按源码列出；这些是读取合同，不是215未来实数结果。[R446、R485]

204/215 的 bridge 在源代码中明确检查 owner 的 native_accepted 为 false，然后受控停止原64 worker；没有把新128末态组装为原 worker 的正常响应，也没有调用后续完整 fullDN 主程序。这是**未接的响应/消费者路径**，不能从该 false 反推出某个数值主门已经失败。[S6–S9]

下一可执行方向是：在一个明确声明算术实现的新 live native client 中，消费同次真实 owner、全部状态、完整端点 jets/J 和独立 audit；保留原当前 H、完整配置、阈值及失败语义；随后真正调用原 FD/fullDN 消费链。它不要求先把 second 行改为解析式。本文只证明该接口的必要内容与原消费者怎样使用它，未实现或预付新 client，也没有把215临时数组的 SHA 当成可恢复正文。

## 2. 三个不能混同的对象

本文使用以下来源范围。

1. **原有限 native 协议**：原 tangent-core、recording worker、frozen worker、TailClient；物理函数与原接受判定由实际配置及完整来源约束。[S1–S4]
2. **原完整 physical-phi fullDN 门**：c6a 主程序正文，通过557f 的真实112适配使用338物理行、112常值 core 行和3个活动控制，共453行；原 c6a 直接入口的96模式文字不被冒充成112入口。557f 的 original_full_solve 保留 c6a/main、原 Newton 和 banded 数学正文，只明确替换当前 profile、完整物理 boundary、实际 live client 与记录。[S5、S10–S13]
3. **204/215 独立 binary128 有限实现**：原字面 binary64 参数/表准确 lift；新128持久状态、原阈值与完整行范围；R402/R405/R414 recorded 算子、完整 QR、混合 endpoint 和 C-based physical audit。[S6–S9、S14–S19]

第2项用来识别必须实际调用的原消费者，不声称204固定尾状态已给出该453前缀场，更不声称它与当前另一 continuous-ten/453→450 分支是同一个参数点或同一场。第3项既不被重标为第1项原 IEEE binary64 的逐词结果，也不因算术身份不同而被额外要求通过一套新阈值。

这里的“原门”包含真正执行函数已有的输入/有限性、物理域、完整维数、残差、FD、当前 H 和末端 audit 合同。元数据来源核、预算、错误、quiet/清理是各自程序责任，不以增加数学容差的方式替代它们。

## 3. 原 native 接受究竟检查什么

### 3.1 非线性射击与响应

原 tangent-core 的 solve 对实际状态完整求值，使用所有 cut/stage/far 残差及原 scales；实际试探只有完整求值返回且 norm 严格下降才接受。原 solve 的 converged 由最后完整 norm 严格小于调用 tolerance 决定。若末次已接受更新后尚未得到相应完整求值，它会再 evaluate。root/ODE 的实际有限性与域异常沿原调用传播；本文没有另设更强的 root 容差或 branch-stability 判定。[S1]

具体默认数不能脱离实际配置使用。原 core、worker 的默认值和本次配置值不完全相同；204源绑定明确要求 maxIterations=32 与 solveTolerance=2e-9。持久128 owner 使用的是该 binary64 字面阈值的 lift，不把它替换为十进制的另一个准确实数。[S6、S18]

原 TailClient.solve 的返回前检查是：

| 已有责任 | 实际判定/消费 |
|---|---|
| 完整输入 | 当前 H 有 M 个有限分量 |
| 真响应 | response.failed 不成立，converged 必须为 true |
| 原残差 | residual 有限且严格小于实际 config.solveTolerance |
| 物理 jets | height、slope、second 各为完整 M 向量且有限 |
| 均值 | meanSlope、meanSecond、meanSlopeCorrection、meanSecondCorrection 都为有限标量 |
| 请求 J | heightJetJacobian 有完整 (3M+2)M 个有限值 |
| 请求 audit | audit 不是缺失或 null |
| 当前调用 | 请求/响应与实际 config/source 保存；非 audit 同 H 可按原缓存合同使用，audit 请求不走该缓存捷径 |

TailClient 在保存真实返回后才检查，不把失败记录丢掉。仅该函数的 audit 非空检查不是连续几何证明，也不是对 audit 所有极值另加阈值。[S3]

69c 单次 native 驱动的最终 native_accepted 还要求响应对象真实存在、原请求数恰为1、worker 退出码0且无实际错误。它没有“若四组件完成则置 native_accepted”的分支。[S9]

### 3.2 原混合 Jacobian 是有意实现

原 tangent-core.heightJetJacobian 在当前非线性末点的实际 tangent graph G 上，对每个 k 形成

$$
x^\pm=x\pm h_k
\begin{pmatrix}e_k\\G e_k\end{pmatrix},
\qquad
h_k=d\,\max(|Q_k|,0.1\,s),
$$

其中 d 为原 differenceStep，s 为原规定的完整 Q scale 下界/最大值。它对完整输出顺序

$$
(\mathrm{slope},\ \mathrm{second},\
 \mathrm{meanSlopeCorrection},\ \mathrm{meanSecondCorrection},\
 \mathrm{height})
$$

作对称差分，并按物理高度系数的 r^4 因子换算。frozen worker 之后只替换 first-slope 与 meanSlopeCorrection 行，方法标签明确把另外三组保留为 source symmetric difference。[S1、S2]

这件事实的两个直接后果是：

- 保留完整338×112矩阵是原协议要求；不能因内层只用前112行就省略其余行。
- “all338rows_are_an_exact_analytic_Jacobian_claimed=false”与原协议并不矛盾。它不能被读成原 native 数值拒绝，也不能被提升成阻止 fullDN 的新条件。

### 3.3 内层实际只用 slope J，末端责任仍完整

c6a.AffineTail.set 从 native jets.slope 取 M 向量，并从完整矩阵取前 M 行。其内层映射为

$$
D_{\rm aff}(H)=D(H_0)+J_{\rm slope}(H-H_0).
$$

FullDNBoundary.data、PhysicalTestBoundary.__call__/jacobian 消费此完整 M 向量及 M×M slope 矩阵，分别执行已声明的材料/物理角有限测试。原 physical-phi 形式是

$$
R_\phi=Z_{\rm nonmean}f-\gamma\,S(c)\,D(H),
\qquad H=\epsilon_h P(c)z.
$$

其 Jacobian 同时保留完整 S、P 的 core 依赖、实际 RHS 对状态/控制的导数和完整 native slope J。没有使用 second-J 来组成这个一阶非均值 boundary。[S5、S11、S12]

原 FD 对这个**显式 affine 内层模型与完整边界链式法则**作检查；因此它不是对真实非线性 DN Jacobian 精度的独立证书。即使某个 native J 作为近似矩阵被提供，不能仅由该 affine FD 通过就声称它等于准确非线性导数；同样，也不能因此增加原程序没有的导数误差阈值。

## 4. 原完整 fullDN 的实际接受链

以下顺序由 c6a.main 与557f 的真实112调用保留。[S5、S10]

1. **完整准备与原域**。实际453场、原节点/中点/RMS preflight、完整参数/core/物理源；当前 native 配置、cut 与 profile 的原绑定检查。有限 native 末点本身不是此前缀场。
2. **当前 H 与完整响应**。先按当前完整 endpoint 形成 H，真实 native.solve(H,jacobian=True,audit=False)，再设置 affine anchor。
3. **原响应 FD**。557f 在真实当前 H 回算之后，用原三个扰动、原方向与步长检查直接和 separated 边界；原第四阶 Richardson 最大相对误差有限且不大于5e-5，并保 second_order_truncation_contracts。此原门没有被四组件代做。
4. **完整内层原 Newton**。原 released_newton 保20次迭代框架、最多8次 Jacobian重算、17个试探档；原条件为有限残差及形成的 Newton 代价下降规则。原完整 QR/边界/维数保留；本文不改变这些原常数。[S13]
5. **内层原终态**。solve_bvp 的 success 成立，完整 collocation RMS 有限且不大于1e-6，完整 affine boundary 最大值有限且不大于1e-11。
6. **实际非线性尾回算**。用内层新 endpoint 得到的新 H 再真实 solve，更新 affine anchor，重新计算完整 BC。只有 true_bc 有限且不大于1e-11 才进入下段；否则按原外迭代继续，原耗尽分支保持。
7. **真正冻结参数的物理 RMS**。用端点活动参数固定整个物理 RHS，保节点残差修正，physical_frozen_control_RMS_max 有限且不大于1e-6。常值增广行不能替代此检查。
8. **新鲜最终 native J/audit**。同一实际末 H 调用 jacobian=True,audit=True；重新设置 affine anchor并计算 audited BC，仍要求有限且不大于1e-11。
9. **原 seam/cut 及实际结果**。执行 original final_height_seam、physical-test-final-cut-audit 和冻结参数的原统计，然后才写实际 success/status0 与 new_coupled_finite_acceptance。不能由一个旧 native summary 的 true/false 代替这个写出路径。

第9步中的7a54 audit_cut已有具体合法性检查，不能遗漏：完整 endpoint/338/112；实际 nonlinear/converged 响应；原模式/spacing；残差严格低于该响应的实际 tolerance；cut五字段按原 rtol=2e-11、atol=2e-13；原 MaterialTrace 输入 H 与 checkpoint.cutHeight 的最大差不超过1e-12；原 scalar cut 0/1/2-jet 最大差不超过5e-12；所有原角层完整且材料逆图/正向图在采样处严格正。557f.SharedNativeClient 还明确核对请求 H 与 checkpoint.cutHeight 的原数值列表相同。[S10、S14]

这些 cut 数字是已有输入身份/有限图合法性合同，本文没有新增它们。原 mean/second seam 差、材料与物理投影差以及高频/角度比较按原函数真实记录；主程序没有把所有这些报告值另设成一个“全 seam 小于某新阈值”的接受门。有限 physical-phi 接受尤其不证明旧材料残差、Cartesian C² seam、连续 Fourier 误差、reach、held 或全 t 目标。

## 5. 四组件已经实际提供哪一层工作

### 5.1 完整线性边界的条件代数

设 d=576、M=112、K=224。Q、Π分别取状态的前/后 M 个分量，A_n 是本次实际形成的完整 K×K stage map，D_far 是原完整 far 对角图。指定物理高度方向 B_H 后，边界组件求解

$$
Q\,X_0=B_H,\qquad
A_n X_{n+1}-X_n=0\quad(0\le n<d),\qquad
(\Pi-D_{\rm far}Q)X_d=0.
\tag{491.1}
$$

c218 从完整 far frame 开始，逐 stage inward thin QR，在 cut 的完整 Q 块上作 square QR，再向外回代全部112列。它没有 SVD截断、选少量模式或删均值；所有577节点的224×112响应和两个 stage mean 行保留。若准确实矩阵下各要求的 QR/chart 可逆，逐式代回证明式(491.1)。实际实现还对完整129248×112行、cut/far与每段形成 readback；那是实际浮点残差记录，不是自动外包误差界。[S15]

因此无需重新猜一套少模式 transfer；同次真实边界输出可以成为端点响应的完整来源。但是 A_n 在204/215属于明确的 recorded-coefficient binary128实现。其与准确有限根导数、旧R305逐词值或连续 DN 的关系不能由覆盖计数证明；原源码已保留相应 false/未证标志。本文不以补一个线性残差阈值来改变原接受。

### 5.2 端点矩阵的正向链

a090 实际读取本次 cut-Pi-graph-per-Q；用独立物理表/原cut，完整计算基础 jets、每列 plus/minus jets，并覆盖完整338×112矩阵。前112 slope行使用原 RHS 恒等式及实际根trace方向：

$$
S=r^4 f_Q/r'+4r^3Q,
\qquad
J_S=\frac{D f_Q\,[I;\rho G]}{r'}+\frac4r I,
\tag{491.2}
$$

其 meanSlopeCorrection 行为对应完整 mean RHS 方向除以 r'r^4。这里 r' 是实际cut dr，ρ是原动量归一化转换；(491.2)说明取数和局部高度换算，不宣称不同括号的浮点值相同。a090事实上把 RHS 恒等式差保存在临时数组中，没有据恒等式把它强设为0。[S16、S17]

其余行沿原差分路线。每个方向有实际正步长、plus/minus完整root/physical求值和有限性检查；任何失败保实际列地址/错误。完整并不需要把差分变成解析式。该组件已足以作为原混合响应**形状和数值内容的候选来源**，真正接入还需第7节的 current-H/protocol/source生命周期，不可只发一个 matrix_shape。

### 5.3 独立 audit 的范围

a090.audit 从每个真实128节点独立开始，执行原全部 query 与每个 query 之后原 primal advance；stage只有整段query、advance和写出都完成才算complete。它返回原 fullD、normalizedFullDefect、minLeading、minD、formalCurvature、maxPhysicalPV、actualMetric、holonomy，以及 C radial solve readback。不能只数 query 而漏最后正在推进的状态，也不能把这些有限采样 extrema 当连续外包。[S16、S17]

audit 中的 C-based 径向公式是原程序公式的新128实现；不是“F_e 已等于 C”的证明。原 audit 完成要求实际物理求值/开发公式合法、数组有限及覆盖完成，未规定一个新 fullD 或 actualMetric 阈值来决定 native/fullDN。

## 6. request215 必要字段能直接判什么

本节列的是 d2f2 reader 的**逻辑原字段**：读取时按R485实际同值共享组、引用和 key-set还原语义，保 absent/null、全部数字原词、数组原序与负零；不把固定 schema/source 共享解释成科学复算。若215仍因90KB或错误返回70，本节未返回内容仍必须写“未读”。[S19、R485]

| 来源/逻辑字段 | 原实际可判范围 | 不能据此宣称 |
|---|---|---|
| owner.records 中 persistent128_owner_final；evaluation_columns、all_distinct_original_evaluation_rows、原 key sets | 真末 residual norm、complete、stages/rows、below_original_tolerance、stop_reason；全部实际trial/接受/未访原记录 | 215预定成功；fullDN已有prefix解 |
| owner.original_selected_fields 的 final_state128、packet/input/call identity、fresh replay两逐词比较和 independent_fresh_replay_complete | 实际128末态/原调用与独立原primal replay的关系 | 新stage J就是准确DF；等于原64末态 |
| stages.scientific_report | 完整请求stage/224列/226含mean范围、实际 primal norm/root/方向/backend统计、原error/未付地址 | 覆盖计数等于导数误差证书或测速保证 |
| boundary.scientific_report 及 forcing_report | 完整112响应、全129248×112线性readback极值与最坏行列、cut forcing/归一化合同 | 为这些诊断私设阈值；cut chart已严格非奇异 |
| endpoint.scientific_report | base jet scalars、完整338×112形状、symmetric与first-slope各完成列数、原步长/方法/错误/后缀 | 摘要含完整jets/J数组；全部338解析；physical Ldot是有限root trace径向导数 |
| audit.scientific_report 及所有原stage accounting | 原完整query/advance覆盖、全部列明的全段极值、真实未完成phase/query/advance/错误 | 连续角度/径向误差界，闭面metric/reach/held通过 |
| 各 component.input_identity、原summary/source/temporary manifests及父record | 同真实owner末态和来源，实际临时产物身份及覆盖；reader在Actions核state receipt | 仅凭SHA恢复已删矩阵/状态或远端已逐值读大数组 |
| fresh_original64_procedure、bridge/owner记录 | 真受控停止、原响应是否实际产生、原64是否执行终端J/audit、是否强转128state | 把控制流false当数学拒绝 |
| lifecycle、error、cleanup_evidence | 真process/transport70分责，原错误选择、owner quiet、实际cleanup是否获准 | quiet或summarycomplete就是科学接受 |

endpoint临时基础338输出的数组不是必要摘要全部展开的对象；它还不等于可直接传给 Python TailClient 的完整响应字典。成功stage的逐列大数组、完整J、所有角jets只在本次Actions保留，必要reader明确不读取或不返其数值正文。故“215完整必要字段能判断组件完成与报告值”与“215在聊天传回全nativepayload”不同，后者未被要求，也未实现。

同样，owner旧 full_stage_J_complete、endpoint338_by112_sensitivity_complete、original_geometric_final_audit_complete 指向原owner内部预留路径；post_owner_components 的新四组件是另一明确调用层。阅读时应按各自来源解释，不能将前者的旧 false 覆盖新组件事实，也不能把新组件true自动传播成旧native/fullDNtrue。[S6–S8、S19]

## 7. 不增加新门的最小实际消费路径

**命题491.1（有限响应接入条件）。** 对一个实际调用 H，若新实现真实完成同配置的全尾非线性求解，返回的残差/完整物理jets/完整混合J/audit及checkpoint都来自该次当前状态，并经原输入、有限性、当前 H、残差和请求项检查，则全338解析化不是把该响应交给原 fullDN 数学体的额外前提。完整 fullDN 是否接受，仍由第4节实际计算决定。

**证明。** TailClient 与 SharedNativeClient 的返回前分支见第3节；AffineTail取前M行；boundary/FD消费完整有限slope和该矩阵；第4节每个新 H、BC、RMS和最终audit均实际调用。所有这些分支都没有“second行必须解析”的条件。由函数调用顺序归纳可得响应可被消费与最终接受的不同条件。此为接口/控制流命题，不能反推某个尚未执行的新client已经满足前提。证毕。

落实这一命题的最小独立后继必须实际做以下工作，不能只改布尔字段：

- **一个 live H→response 入口。** 当前原64在bridge后受控停止，必须由独立、明确新source接线替换这个未接的返回路径。真实绑定H/config/shape/cut/far/scales/几何与字面表；每个新H重新走实际非线性求解，原warm仅为初猜，不能用204或215固定末点应答别的H。
- **从本次临时文件组装真正payload。** 使用实际 final-state、全基础jets、完整338×112混合J及本次独立audit；保height/slope/second与全部mean、checkpoint.cutHeight/完整states/parameters、actual_nonlinear_solve与精确来源。全文件必须仍在同job、实际字节与producer receipt匹配；不能从summary/hash造数组。原已有读取/shape/finite检查随消费执行，不另办fixture或“验收审计”。
- **明确数值接口。** 当前 Python fullDN 数值数组是binary64；若采用128计算的新client，必须明确输出投影与其真实来源，仍保原128状态而不把它重标为原64worker末态。若要声称原64worker已经接受，则必须真正调用那个原worker及其原门，不能由128残差替代。新client沿原门并不意味着原IEEE字节等价。
- **完整当前外场与原 FD/fullDN。** 实际建立对应profile、core和453场，在原预算/owner生命周期中执行第4节；所有新H的尾求解仍真实。tail单点达到阈值不支付prefix collocation或非线性outer recheck。
- **在实际消费者结束后读回/quiet/清理。** 响应与末态大数组只在Actions临时供科学消费者使用；必要摘要保原接受条件值/来源/失败/未访，不为传输复制全矩阵或编码大raw。当前215未接此路径，按其冻结原cleanup责任结束；未来不能声称恢复被销毁的215现场。

该后继所需改动首先是响应和外求解接线；不是先增加一个解析J门。它仍可能在任一原物理、有限性、FD、非线性或资源分支失败，本文没有预判。若只有错误/partial，则按实际范围记录，不通过改flag使它成为接受。

## 8. 何时才确实需要改导数实现

下面是不同研究声明的技术责任，不是给原有限接受另加的前门。

| 想声明的对象 | 现有源已做/尚未做 | 如要得到该更强声明的真实实现责任 |
|---|---|---|
| 原有限混合338×112响应 | 已明确保留原second/meanSecond/height差分；新first行沿真实trace/G | 不必为了原门改全解析；保实际误差读回/原门即可 |
| 当前C-based physical program 的完整形式方向导数 | second等行目前有限差分，不是其完整AD | 沿实际roottrace、C形成、实际Cholesky和两回代、physical_jets、cut_readout的全部依赖作AD；新实现单独身份 |
| 准确代数模型 Cℓ=b 的导数 | 该模型与已舍入factor程序要分开 | 在准确可逆条件下用式(491.3)；不能将实际浮点因子残差自动置0 |
| 有限root trace的真正径向导数及其对H的导数 | 当前physical Ldot仍原C-based公式，源未宣称等于该径向导数 | 对实际径向状态/几何输入及固定执行trace传播；若要其H导数，保所需混合二阶依赖、选分支与误差责任 |
| 准确物理隐式根/连续ODE几何导数 | C=F_e未证，有限停止不等准确根，有限RK/模式仍在 | 准确根与实际F_e、根族/分支、相应误差外包及连续离散误差；不能由解析列数或SIMD准确点积直接支付 |

为说明其中一个严格边界，若只定义准确实可逆系统 C(x)ℓ(x)=b(x)，对方向v求导得

$$
D\ell[v]=C^{-1}\bigl(Db[v]-DC[v]\ell\bigr).
\tag{491.3}
$$

证明只用乘积法则和准确逆。现有physical128实算先形成C，再执行有限 Cholesky/两次回代；其已返回数值因子并不由式(491.3)自动获得原算法逐词导数。要保有限程序的形式方向图，必须传播实际factor/两回代依赖；要换准确C系统则须明确对象/误差身份。此处也完全不需要、且不能悄悄引入 C=F_e。

R402/R405/R414 对 recorded 系数线性图、完整dyadic点积和整数backend的结论各有范围；它们没有补上上述完整导数误差、branch stability或连续几何责任。新研究可沿这些已明确对象推进，但不得把它们变为原native/fullDN接受的额外条件。

## 9. 当前可登记的进展与下一行动边界

本结论修正一种容易造成停滞的错误解释：**原四组件完成而native/fullDNfalse，不是“因为还有若干行采用差分所以原门不允许接受”。** 原门允许该混合响应；当前源未接live正常响应、没有完整前缀fullDN调用，才是源码可直接确认的未付调用责任。

215终态必要字段若成功返回，应先登记真实末态/残差、同状态四组件完整范围、线性与audit数值、错误/quiet/原flag的来源。原门里尚未执行的当前H FD、完整外场RMS、真实outer recheck及最终cut审读保持未付；不能根据大摘要未返回而把它们标为数值失败，也不能根据四complete标为已接受。

R491没有修改204/215、没有调用新科学程序、没有新增阈值或请求。已完成的是可直接落实为独立live响应/fullDN后继的来源和消费合同；原连续closed-surface、全t强C²、metric/reach/held等目标仍按各自原责任真实完成。

## 10. 精确来源与阅读范围

下表是本次按实际204发布头189579b508930d99d9c2dbc481967fd972766919读取的源；S7/S8是215按原SHA继续引用的204同job、bridge、component launcher和科学stage；S6仍是原owner，S19是已刊R485的新必要reader。原tangent三件同时核对source-dependencies.json中的原字节，不把同名另一root/split文件作替身。长源码仅用于源码/纸证，本结论未执行或导入它们。

| 标识 | 完整文件与阅读接点 | 字节 / SHA-256 |
|---|---|---|
| S1 | [78718-tail-tangent-core.mjs](../../visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs)；solve / evaluate / heightJetJacobian / audit | 17250 / ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3 |
| S2.1 | [tail_frozen_worker.mjs](../computations/tail_frozen_worker.mjs)；原两行组替换、原成功路径与受控来源适配 | 5149 / 3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054 |
| S2.2 | [tail_resumable_engine.mjs](../computations/tail_resumable_engine.mjs)；原两行组替换、原成功路径与受控来源适配 | 4193 / 1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8 |
| S3 | [exact_20261114_true_tail_client.py](../computations/exact_20261114_true_tail_client.py)；TailClient.solve / close | 19526 / 1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09 |
| S4.1 | [78718-prefix-tail-tangent-fourier-worker.mjs](../../visible-flexible-closed-surface/scripts/78718-prefix-tail-tangent-fourier-worker.mjs)；原请求、真实checkpoint与完整worker返回 | 12294 / 36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a |
| S4.2 | [78718-tail-tangent-split.mjs](../../visible-flexible-closed-surface/scripts/78718-tail-tangent-split.mjs)；原请求、真实checkpoint与完整worker返回 | 1948 / bacb4f2d57d75fa648ae880ef029152263052d6a15030154082732b8a89e1089 |
| S5 | [geometry_20261114_full_dn_solve.py](../computations/geometry_20261114_full_dn_solve.py)；AffineTail / frozen_physical_residual / main / final_height_seam | 30017 / c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162 |
| S6.1 | [geometry_20261115_native_persistent128.py](../computations/geometry_20261115_native_persistent128.py)；真实配置、owner、trial、final与fresh replay | 43371 / 767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322 |
| S6.2 | [geometry_20261115_native_persistent128.cpp](../computations/geometry_20261115_native_persistent128.cpp)；真实配置、owner、trial、final与fresh replay | 22364 / 7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd |
| S7.1 | [geometry_20261116_native_simd_stats_qualified_final128_same_job.py](../computations/geometry_20261116_native_simd_stats_qualified_final128_same_job.py)；precleanup_components、post-owner flags与受控原64停止 | 38408 / 8855ef79037bf552f44bd926e92ff5b2874fa17e8e35e1773c6344b71fd2c37c |
| S7.2 | [geometry_20261116_native_simd_stats_qualified_final128_bridge.mjs](../computations/geometry_20261116_native_simd_stats_qualified_final128_bridge.mjs)；precleanup_components、post-owner flags与受控原64停止 | 15829 / 718f1c475b4722eaddeae9eb5bf610c438f2a0c221a7e26e10850fbf00126471 |
| S8.1 | [geometry_20261116_native_simd_stats_qualified_final128.py](../computations/geometry_20261116_native_simd_stats_qualified_final128.py)；四组件启动/完成与完整stage范围 | 31930 / e5c85e6bf5e864de39b0675f997c716466ead0dd158a6c22b73c714257e7433f |
| S8.2 | [geometry_20261116_native_simd_stats_qualified_stage128.cpp](../computations/geometry_20261116_native_simd_stats_qualified_stage128.cpp)；四组件启动/完成与完整stage范围 | 12691 / eca87efc267d692e401d2ed49904d3d8e73cc16cad12eb3ae24042328f81025e |
| S9.1 | [geometry_20261115_native_word_first_current576_solve.py](../computations/geometry_20261115_native_word_first_current576_solve.py)；原native_accepted分支与原64no-response范围 | 20966 / 69c9a8d5cccfcfdcdda35c475b089609c789747803a7b363a17fb67c5bae28d0 |
| S9.2 | [geometry_20261115_native_persistent128_probe.py](../computations/geometry_20261115_native_persistent128_probe.py)；原native_accepted分支与原64no-response范围 | 17879 / 2683e8e13a8d73d6c08500e9d3716d5bac5dc2e66648a17c8e1d75d246c62107 |
| S10 | [geometry_20261115_six_control_height_continuation_full112.py](../computations/geometry_20261115_six_control_height_continuation_full112.py)；actual_boundary_fd / SharedNativeClient / original_full_solve | 45097 / 557f3aab83116c1d8eef83e4c83306e8058749ccdb56b2ec8808effd2e16bf21 |
| S11 | [geometry_20261114_full_dn_boundary.py](../computations/geometry_20261114_full_dn_boundary.py)；data与实际完整tail-map消费 | 10619 / 4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2 |
| S12 | [geometry_20261114_physical_test_boundary.py](../computations/geometry_20261114_physical_test_boundary.py)；PhysicalTestBoundary / pullback / jacobian | 6269 / 3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681 |
| S13 | [geometry_20261114_projected_core_bvp.py](../computations/geometry_20261114_projected_core_bvp.py)；仅本文所用released_newton与finite_second_derivative调用合同；不执行其独立main | 25181 / 2326720f124d2edc40e63089f8e07d6671e053ff108281efb59091d919f15c5b |
| S14 | [geometry_20261114_physical_test_cut_audit.py](../computations/geometry_20261114_physical_test_cut_audit.py)；audit_cut的已有合法性/来源检查与报告范围 | 19257 / 7a548961ff0bd3e5171db18f1133d42f606be19e65e5d2e919432514042ba420 |
| S15 | [geometry_20261115_native_boundary128.cpp](../computations/geometry_20261115_native_boundary128.cpp)；完整QR/所有原行readback/双mean | 12493 / c218f12850e513cc58151e679c26de038f37b105dd187696e6f785ec4667fe96 |
| S16 | [geometry_20261115_native_physical_final128.cpp](../computations/geometry_20261115_native_physical_final128.cpp)；forcing / endpoint / audit | 18055 / a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415 |
| S17.1 | [geometry_20261115_native_physical128.hpp](../computations/geometry_20261115_native_physical128.hpp)；cut_readout / physical_jets / physical_metric / rhs_direction / replay_root | 12683 / 4b0569a245147e346149d462d974a80cac853bcf9d5abf13700b743acd33af35 |
| S17.2 | [geometry_20261115_native_shared_trace128.hpp](../computations/geometry_20261115_native_shared_trace128.hpp)；cut_readout / physical_jets / physical_metric / rhs_direction / replay_root | 13605 / bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b |
| S18.1 | [public-native-simd-stats-qualified-final128-request.json](../computations/public-native-simd-stats-qualified-final128-request.json)；本次原参数与94pin合同；78旧源的实际恢复/哈希来源 | 76649 / 7e6f600e76ea5023c63e98fe0a3899e0eb532d7d65f672a59f5bc4411e9bd871 |
| S18.2 | [source-dependencies.json](../computations/source-dependencies.json)；本次原参数与94pin合同；78旧源的实际恢复/哈希来源 | 24057 / 7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941 |
| S18.3 | [exact_20261114_public_resume.py](../computations/exact_20261114_public_resume.py)；本次原参数与94pin合同；78旧源的实际恢复/哈希来源 | 13907 / 11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5 |
| S19 | [root_20261116_native_simd_shared_metadata_necessary.py](../computations/root_20261116_native_simd_shared_metadata_necessary.py)；component_view / owner_records_view / build / fixed_semantic_sharing / write_result | 46653 / d2f2b000310f3e04f3a60e51e74000bcf32516ac50b1f1fac97a4534c06d028b |


结果引用：

- [R446](R446-actual204-complete-four-components-and-necessary-readback-overflow.md)：21458 B，SHA-256 96d5775cc6aaf0c5a5ad1b0be3d55b27b1975690fd4c56ca651f70438f7884e3；发表于 fedcc67e9a96ccf67145cd61540209ea1f5dcaf8。本文不重取204日志。
- [R485](R485-fixed-semantic-sharing-of-native128-necessary-metadata.md)：11765 B，SHA-256 936a5403b61cd318b7589610d47d0ca9a4c1f25d834aa367ad37c99453946fc5；发表于915f148bb4e5f50d2d1226bd50661c1d617bd4d5。
- request215 正式source b952df814c98ef5927a4f5013364d2eed6002d74，run43816406919/attempt1，compute133129348123。本文写作时未读215运行中日志，也未预填其终态。
- R402/R405/R414只用于说明第8节已存在的算术声明范围；本文结论直接对照S8/S16/S17中对应作用、方法与未证字段，不借那些理论覆盖未实现的完整解析J。

本稿只包含可发布的必要研究结论与源码身份。实际状态/J/角数组均未复制到本文或新Git对象；未进行本地科学、import、AST、compile、test、fixture或benchmark。
