# 持久 binary128 末态的共享轨迹段变分、完整边界响应与物理程序读回

类别：独立实现与完整数学接口；不是实际数值结果。  
作者：exact_refinement（AI 协作）；日期：2026-11-15。

## 1. 本次具体交付与状态

本组源码接收一份同一 Actions 作业内仍存在的、由真实 persistent128 owner 写出的完整577×224 binary128末态。它不生成初猜，不替换133，不推测133能否达到原2e−9，也不把任何旧64 Jacobian或旧audit贴到此末态。

已实现四个独立组件：

1. 每个实际有限root只选择一次原分支，并保留被接受更新的F/C/Cholesky/两次三角解中间量，供所有请求列复用。完整576段、每段226×224变分以及post-port224×224和两个mean行均有实现。
2. 从这些当前段矩阵求完整112列的cut/far边界响应，保留全部112个高低模，用全维Householder QR，不形成normal matrix、不用R273阻尼解代替物理逆。
3. 在同一末态cut上形成338×112读数：slope112、second112、meanSlopeCorrection、meanSecondCorrection、height112。第一类和meanSlope用实际有限root轨迹的RHS方向导数；second等沿用原cut程序的对称差分。
4. 独立从每个真实node n+1开始，沿原audit自己的全部profile/k查询和cusp-aware RK推进，计算完整原物理jet/周期发展程序的binary128读数，保存每个角行及实际部分完成范围。

第4项保留的是**原C-based物理jet程序**；它不证明C=F_e，不声称其Ldot等于有限root迭代轨迹的径向导数，也不冒连续ODE误差或真实无限尾证书。所有组件始终保留 native_accepted=false 和 fullDN_accepted=false。原物理程序读回完成与原native/fullDN通过是不同事实。

本地只写源码、读源及计算文本SHA。第一次g++语法检查尚未创建进程，执行环境即断连。随后依根规则8，仅用已有GitHub集成创建每件小于100KB的文本blob；未创建tree/commit/ref、未派发、未编译、未运行科学或数值fixture。下表完整blob文本为当前交付；临时盘早稿不得代替其身份。

## 2. 完整源码身份

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| geometry_20261115_native_shared_trace128.hpp | 13605 | bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b | 9f06915b4e53ed480b6ded8a0119e35f914a1029 |
| geometry_20261115_native_batched_stage128.cpp | 8642 | 7c59da157746292d89c0857e7a0fa44bb590de1ae1a2e1b9cbea8ff18e006eab | 7f1e7c6183168ccc4974b1d9a8874346a8835be5 |
| geometry_20261115_native_boundary128.cpp | 12493 | c218f12850e513cc58151e679c26de038f37b105dd187696e6f785ec4667fe96 | ec983b2b64c31a436cc084b41ff4fd56b397ac21 |
| geometry_20261115_native_final128_packet.mjs | 9051 | 824b7440d2604e828df4326b1cef1b1bf332d203eeb7e81968704d2febdcd7c2 | 23007b420e45e519122267d9010e4fd08814fd47 |
| geometry_20261115_native_physical128.hpp | 12683 | 4b0569a245147e346149d462d974a80cac853bcf9d5abf13700b743acd33af35 | 4aee233af0fe614941a13641f6994ca3398b6800 |
| geometry_20261115_native_physical_final128.cpp | 18055 | a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415 | 2ce5368fa6d6ee5aacfcc08218a844dd0d87e5c5 |
| geometry_20261115_native_final128_components.py | 25877 | ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045 | c61bbead086a77175b9610ea0efeda4ced50ba7f |

组件launcher还逐字锁定以下既有源：

| 既有文件 | SHA256 |
|---|---|
| geometry_20261115_native_trace_variation128.cpp | 8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d |
| geometry_20261115_native_trace_variation128.py | 8229212bb6804db7eee99ea661a490d3cced756e8a98471c09e22ad74cdb8b76 |
| geometry_20261115_native_trace_variation128_bridge.mjs | 61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7 |
| geometry_20261115_native_primal128.cpp | 1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d |
| geometry_20261115_native_primal128_bridge.mjs | 3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8 |
| geometry_20261115_native_persistent128.cpp | 7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd |

R283 C++的唯一换行加main锚之前全文作为生成include，31738B，SHA256 fd676b38fbc83abeccf85ca6956b325d15b26425f9147e3d52d2283cd1ae4956。只去掉独立main；F_direction、C_direction、spd_solve_taped、spd_solve_direction、rhs_from_root等定义原样保留。生成include不是另外一份数值源，也不把它标成完整R283可执行文件。

新launcher使用g++的gnu++17、O3、OpenMP、frounding-math、ffp-contract=off、fno-fast-math和libquadmath；这些与133最终编译语义一致。尚无新实际编译器回执。不得把源检查或预期编译成功写成已运行结果。

## 3. 已亲读的原末态责任

原78718-tail-tangent-core.mjs的cutJets、tangentGraphAtCut、heightJetJacobian、audit；原worker、tail_frozen_worker、numerical-tail-slope-jacobian；原physical_test_full_dn和full_dn_solve入口均已读取。

原338行顺序严格为：

| 行 | 数量 | 原作用 |
|---|---:|---|
| slope |112|物理cut高度的一阶径向Fourier响应 |
| second |112|物理cut二阶径向Fourier响应 |
| meanSlopeCorrection |1|mean的一阶修正 |
| meanSecondCorrection |1|mean的二阶修正 |
| height |112|完整物理cut高度 |

原worker的numerical-tail-slope-jacobian只替换first112行及meanSlope行，保留原second/meanSecond对称差分。这意味着即使原338×112数组完整，也不是所有338行均为解析自动微分。

原audit不是shooting残差replay。它在每个stage的每个profile上取k=0,…,auditSteps，读取physical jets及周期发展metric；k<auditSteps时按原cusp-aware RK推进，完整状态贯穿同cell的所有profile；每个stage重新从保存的node n+1开始，两个mean初始为零。不能以保存的576个stage末输出替代这些查询。

原fullDN还要求实际每个新H的native求解及J、原三个方向和各步FD、外层完整物理BVP边界及RMS判据、最终fresh native J与audit、最后同场cut检查。当前七个源只提供上述末态组件，不替代这个多请求客户端/完整fullDN适配。

## 4. 一次有限root轨迹可供全部列共享的证明

固定一份完整字面模型：原frequency、cosine、sine、Gram分别保留；w、w²、E分别保留；geometry、mu、portRatio、stop/fallback及实际原RK子步均由原packet给定。root求解变量为e=L−target，其实际有限残差为F(e,state)，而迭代矩阵为独立字面表达C(e,state)。

在某次实际成功轨迹上，将所有接受/拒绝、normal/fallback、回溯指数k视为已经选定的离散控制流。一次被接受更新是

$$
C_\ell=\mathcal C(e_\ell,y),\qquad
L_\ell=\operatorname{chol}(C_\ell),\qquad
L_\ell t_\ell=F_\ell,\qquad
L_\ell^\top s_\ell=t_\ell,\qquad
e_{\ell+1}=e_\ell-2^{-k_\ell}s_\ell.
$$

本实现保存更新前的e、F返回的全部角行、C、实际Cholesky L、前代t、回代s和k。被拒绝trial只决定离散分支，不能作为被接受e的更新，也没有被混入方向递推。若最终原fallback返回，最后未接受的solve不加入导数链。正常最多29次被接受更新，与原30轮循环成功返回范围相同。

对任一方向h，R283的逐操作链式规则给出dF和独立dC。令v为原Cholesky某元素在减去此前乘积后的中间量，则

$$
dL_{ii}=\frac{dv_{ii}}{2L_{ii}},\qquad
dL_{ij}=\frac{dv_{ij}-L_{ij}dL_{jj}}{L_{jj}}\quad(i>j).
$$

这里dv按原求和次序展开dC及每个L乘积的两个导数项。前代、回代亦逐原t、s及对角分母求导，随后

$$
de_{\ell+1}=de_\ell-2^{-k_\ell}ds_\ell,\qquad
dL_{\mathrm{returned}}=d\,target+de_{\mathrm{final}}.
$$

没有使用C=F_e，也没有以一次新的C逆求解替换原Cholesky/前代/回代的有限表达导数。direction为每个输入列独立传播；不同列之间没有数值反馈。因此保留同一primal tape，再按列依次执行R283方向函数，与分别给这些列使用相同成功trace的链式结构一致。程序仍逐列重放F/C的value shadow，并对原返回词做R283的逐字一致核。这些是实现自身的来源/结构检查，不是另加一个native线性接受门。

四个RK primal场先按原括号完整计算；再按各列的四级链式递推形成完整226方向。列的推进不反馈原primal、root选择或profile。完整返回时，先做primal再做导数与原R283交错做导数的primal路径一致；失败/超时时实际已访问前缀可不同，程序分别报告，而不声称部分执行的记录序列逐字相等。

此证明有三个边界：

- 它是固定分支的实表达链式结构与其binary128数值实现，不是IEEE舍入映射的经典导数。
- 是否存在保持同一离散分支的实邻域仍未证明；处于停止/guard边界时不得断言整个分段程序可微。
- 复用省掉的是重复root分支搜索和primal Cholesky。每列的F/C影子及Cholesky方向工作仍存在；不承诺224倍提速、350分钟完成或精度认证。

## 5. 完整段映射、方向行和原残差

第n段输入node n+1，输出node n。程序从真实binary128 node n+1复制224形状坐标，两mean置零，依原packet全部原子RK步推进。请求列j的初始方向为该node的e_j；这是局部映射列，不在其他node减identity。

完整stage输出保存：

- primal-full-output：226；
- full-columns-before-port：226×b；
- shape-columns-after-port：224×b，其中Pi输出除原portRatio；
- mean-columns：2×b；
- stage-residual：post-port shape减真实node n。

只在first_column=0、columns=224、全部576段完成时，complete_224_stage_columns才为true。任何未请求/未返回列都不是零列。数据依阶段完成写出；部分stage的完整Jacobian文件不会虚造。

完整原残差行序保留cut112、576×224 stage、far112，共129248行。sigma映射仍cut→sigma0、stage n→sigma_n、far→sigma_576。全部完成后只读回实际128规范化范数；没有新阈值。

## 6. 全112边界响应的frame QR构造与唯一性

记当前完整stage形状矩阵为T_n，原far对角图为G_D。取远端frame

$$
Z_D R_D=\begin{pmatrix}I\\G_D\end{pmatrix},
$$

并从D−1至0依次作薄QR

$$
T_n Z_{n+1}=Z_n R_n,\qquad
Z_n\in\mathbb R^{224\times112},\quad R_n\in\mathbb R^{112\times112}.
$$

这是全112列QR，未按奇异值删列。代码存全部frame、R和乘积原数组。不形成normal matrix，不取R273方向或fixed64矩阵。

令P_Q、P_\Pi为节点的Q/Pi投影。给定明确的cut forcing B_H，解

$$
(P_QZ_0)C_0=B_H,\qquad
C_{n+1}=R_n^{-1}C_n,\qquad X_n=Z_nC_n.
$$

若各R_n及P_QZ_0在精确实模型中可逆，则

$$
T_nX_{n+1}-X_n=0,\quad
P_QX_0=B_H,\quad
P_\Pi X_D-G_D P_QX_D=0.
$$

这些等式逐项来自QR身份和回代。反过来，远端任何满足far条件的向量都位于Z_D的列空间；逐段映射后位于Z_n的列空间；cut条件唯一确定C0，全部R逆唯一确定余下系数。因此解是该完整两端线性系统的唯一响应，没有忽略109个高模，也不需要每个中间Q图可逆。

实模型条件不等于数值证明。代码在实际零pivot/非有限运算时明确失败，不用SVD截秩；非零浮点pivot不能证明实非奇异。它保存完整129248×112线性缺陷，包含cut、所有stage及far；还保存每段两mean响应与总meanHeight响应。归一化缺陷、因子重构缺陷只是实际普通浮点读回，不是包围证书或新的接受门。

cut图另由同一Z0求

$$
G_0=P_\Pi Z_0(P_QZ_0)^{-1}.
$$

没有把阻尼最小二乘解冒成此图。

## 7. 物理H的局部定义必须显式

原packet已经保存了binary64的target=H/r⁴，随后被精确提升为128；重新计算它会改变原owner问题，因此本消费者不重算这个target。

响应列明确采用局部实表达延拓

$$
Q_{\rm target}(H+\delta H)
=Q_{\rm target,saved}+\delta H/r_{128}^4,\qquad
r_{128}^4=(r_{128}r_{128})(r_{128}r_{128}).
$$

forcing组件在Actions以128形成B_H=I/r128⁴。它还保留原JS的r**4 literal供读回，但不将两者默认为相同词。此局部延拓不是IEEE64或IEEE128除法舍入映射的导数；也不是声称当前近似shooting点已经是精确隐函数根。

原cut profile(1)与最后RK场自己的literal x+h保留为各自geometry。程序记录五个geometry词是否相同，不以相同作为新门。source/packet binding确保来自同一实际配置，而不是强行把两个合法有限求值路径合并。

## 8. 338×112读数的实际定义

在真实cut node0上先将Pi乘原rho=2**a，保留完整226 state与其两个mean约定。新cut程序按原公式计算slope、second、mean修正和height；每个调用的root为原stop有限算法128实现。

原second使用的Ldot由原独立C-based径向jet程序得出。此程序被完整移植，独立物理cs/sn原literal表被保留，但没有被改称R283有限root径向变分。其C solve缺陷另存读回。

沿当前图G0，对第k列按原策略取

$$
h_k=10^{-4}\max(|Q_k|,\,0.1\max(10^{-250},|Q_1|,\ldots,|Q_{112}|)).
$$

分别真实计算node0±h_k(e_k,G0e_k)的完整cutJets，以原2h_k r128⁴归一化全部338行。plus/minus实际node、338个值与h均保存。没有把偏移点重新shooting求解；这与原heightJetJacobian的图上对称差分范围相同。

第一112行及meanSlope行改用同一base cut root tape的真实方向导数。其engine方向为(e_k,rho G0e_k,0,0)。由原RHS身份读出

$$
J_{\mathrm{slope},ik}
=\frac{d\,F_{Q_i}}{dr/dx}+\frac4r\delta_{ik},\qquad
J_{\mathrm{meanSlope},k}
=\frac{d\,F_{\mathrm{mean}}}{(dr/dx)r_{128}^4}.
$$

这保留原analytic-slope adapter的行选择与物理归一化，同时将旧implicit-root局部J替换为实际有限root trace方向。原RHS slope与cutJets slope的数值身份差另外保存，未强制设零。其余行仍是对称差分。因此complete matrix表示完整338×112数值读数，绝不表示所有行均为精确解析Jacobian。

## 9. 完整物理audit实际支付及仍未支付者

新物理packet须在真实dn仍活着时导出。它不调用root/RHS/RK/solve/J/audit，只保存：

- 原cut r、dr/dx、w、w²、E及dlogw/dx、rho、差分策略literal；
- 独立物理jet frequency/cosine/sine表，不以root表别名代替；
- 原材料角literal和FFT每层正反向base twiddle；
- 原auditSteps；每stage/profile的k=0,…,auditSteps所有geometry；
- 每次k<auditSteps时原splitIntegrationInterval给出的全部子区间；无内部split时保原h，不把它改成端点相减；
- 同实际primal packet/binding、原source、当前配置和每个engine/profile函数的来源摘要。

audit组件每stage从真实128 node n+1独立起步。每个查询保存全部N×7原角字段：ur、ut、urr、urt、utt、Darboux、height；同时保存实际query state、每query的metric/holonomy/curvature/PV/C求解缺陷和所有原root日志。完整两mean推进，不使用保存stage末态跳过中间查询。

原周期发展FFT的base twiddle保持原literal；发展角psi依赖新128状态，sin/cos明确改用libquadmath的128超越函数。整数幂写成显式128乘法；它是新有限算术实现，不是原JS roundmap逐词同一。完整formula、原查询与来源均明确保留。

若时间/异常中止，报告每stage的queries_completed、active_query、active_phase、当前advance已完成/总数和未完成后缀。部分极值只描述已访问前缀；complete=false时不能当作全audit。原domain异常不会被包装成资源终止。

尚未由本组件支付：

1. 原C-based Ldot与真实有限root径向导数是否一致；代码明确不假设一致。
2. 连续径向/角向/无限尾误差及分支稳定性。
3. 将该128 owner作为真正多请求TailClient，完整执行新H、同owner FD、外层fullDN和最终fresh J/audit的接口。
4. 真实native接受。即使全部组件完整且owner原shooting范数低于2e−9，这一组独立消费者也不会自行生成原worker accepted响应。

## 10. 精确CLI与同job绑定

新Python入口为geometry_20261115_native_final128_components.py。

四种component分别是stages、boundary、endpoint、audit。每次都必须提供实际仍存在的文件与完整SHA：

~~~text
--packet PATH --packet-binding PATH
--expected-packet-sha256 SHA
--expected-packet-binding-sha256 SHA
--owner-summary PATH --expected-owner-summary-sha256 SHA
--owner-source PATH --expected-owner-source-sha256 SHA
--state PATH --expected-state-sha256 SHA
--seconds SECONDS --threads THREADS --out FRESH_RUNNER_TEMP_DIRECTORY
~~~

owner-summary必须是真实source-bound owner记录；末态receipt必须匹配完整577×224×16字节。run/repository/attempt/source必须与当前Actions作业相同。它可以是失败/partial owner留下的完整状态，身份核不要求已接受。禁止只有历史hash而没有实际文件时虚构恢复。

stages默认全部576stage/224列。明确子集参数first-stage/stages/first-column/columns只用于请求实际子集，其结果不能供完整boundary消费。

boundary、endpoint、audit另需：

~~~text
--physical-packet PATH --expected-physical-packet-sha256 SHA
--physical-binding PATH --expected-physical-binding-sha256 SHA
--original-source-root PATH
~~~

物理binding的configuration_identity须逐对象等于原packet actual_call_identity。source_receipts路径均相对original-source-root；launcher实读全部bytes，并强制原core/physical-jets/actual-metric/cusp-grid/analytic-slope五源码身份。全部physical packet chunks连续覆盖原bytes，各块SHA逐字核，不在Python重做几何或科学。

boundary另需实际stages组件输出及其summary SHA；endpoint另需实际boundary组件输出及summary SHA。此前组件的source、state、packet和完整临时manifest逐项核同。未完成全列的数据不能被读成完整矩阵，这只是缺失输入的识别。

--retain-temporary-for-same-job使输出留给下一组件。默认在manifest及紧凑读回形成后删除新数值目录和可执行文件，只留小compact-summary供父进程读取。没有artifact/Release/Git raw上传，也不支持跨run继续删失state。

所有编译/科学进程继承原rules-runner进程组；不另开detached group。受控结束只向记录的PID/starttime及其后代发信号。科学每组件seconds显式≤20000，threads≤4；另有编译300秒与退出grace。boundary还需一次物理组件编译及最多60秒forcing形成。父workflow必须按总时间支付，不能把这些额外工作藏在一个名义科学预算里。

## 11. 133清理边界的确定限制

已完整读取133 Python的finally：它先形成完整summary/compact并打印，随后遍历out目录删除全部子目录，且删除summary.json；外层bridge返回后才再删work。故在原bridge的spawnSync返回后调用这些消费者为时已晚。

最小独立后继必须显式派生一个新launcher/driver，在133原finally的数值目录删除块**之前**接入本消费者，并保存该派生源的真实SHA及逆向还原身份。冻结133本身不改。callback需要当时真实packet、binding、final-state、owner-summary及物理packet；它们不能靠历史SHA再造。

本次提供的是可调用的数值组件及其完整绑定launcher；没有偷偷给133挂callback、改变其资源配比或选择未来run。后继若把callback接入，须以新源身份和明确总预算发布。当前owner-source参数已为这类真实新派生源留出显式pin，不会把新执行源伪称767a4c4b。

## 12. 完整输出和部分范围

每组件summary包含source/run/完整CLI/input receipts、实际scientific command与进程终态、实际C++ report和完整临时file manifest。矩阵与日志只在RUNNER_TEMP；manifest仅路径、size、SHA及数量，不称误差证书。

紧凑stdout保留总科学字段以及每stage的完成/错误/未完成范围。若≤90000字节无法装下，summary_complete=false、transport_complete=false、exit70明确区分传输不完整；不会只删字段后仍宣称全部结果完整。科学完成位可以独立为true，但不掩盖传输失败。

所有新程序均保留native_accepted=false。完整边界线性缺陷不作为native步长门；physicalaudit极值不设新增阈值；旧原门没有被放宽、替换或删除。

## 13. 资源和可重现范围

批量方式省去224次重复的root分支与primal因子，但仍有全部列F/C变分及原Cholesky微分。不得由原113一次primal约873秒推算全224列必在350分钟内完成，也不得由编译O3或threads4宣称已有加速。

完整stage五类raw加完整残差约为
576×16×(226×224+224×224+2×224+224+226)+16×129248字节；
未计root JSON日志。boundary保存全部577frame、576mapped-frame/R、577系数与响应、全129248×112行账及mean响应。audit全角raw主要是
16×7×N×实际query_count字节，另有每query226-state、实际scalar/root日志。源码不截高模、不删列或纯常数来配合一个虚假的磁盘预算。

同job状态删除后，只能从公开脚本/完整参数和真实来源重新执行相同序列，不存在“按hash恢复binary128末态”。若全列在总预算内不可达，应根据实际运行的耗时与部分前缀改进实现或资源协议；本接口不预定未执行的提速或声称付完原终检。
