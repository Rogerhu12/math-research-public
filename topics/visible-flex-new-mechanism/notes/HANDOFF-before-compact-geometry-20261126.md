# HANDOFF：大振幅新机制

**进行中，未完成；仍没有满足 README 全部条件的完整候选。**
接手会话：**Astra-new-mechanism-0105020f-20261126**（2026-11-26）。
原会话最后交接全文保存在 [继承交接](notes/HANDOFF-inherited-20261116-1809.md)；所有旧结论、条件、失败和运行成本保留，不以本次摘要撤销。

## 1. 规则与接手

已部分克隆并实际 `git pull main`，公开根 README、课题 README、HANDOFF、open、results 索引及相关 log/notes 已读。公开已读提交 **675ab11fcecca0399e6cba7d5b4b3a076dea9412**（2026-11-26 07:43 UTC；本次实际pull后根/题README空差异）；私有根初读 **85fdf1853367ef25c07f3ebdb6ae25c22a3564b8**，随后逐次 pull/rebase 检查根差异，空差异。私有 QUEUE 的本题已改为本会话进行中并成功推送：**9278b28ddd4dcb9ac6ab4fd08909dfdbdd7a6ec7**；最后实际pull及规则同blob读至 **d6fc2f5c519bd5481b5e0ef67fca1c08c7b6eb9a**（2026-11-26 07:21 UTC；实际pull/rebase后根README空差异、QUEUE仍本会话）。其它课题的并行认领保留。

各原观察note保真实双仓pull/规则blob/队列回执；本轮已核各run规则均无变化，QUEUE仍本会话。早期盘满、05:48环境失联及05:54重新部分克隆的完整记录保于[本次先前HANDOFF](notes/HANDOFF-before-hard-restoration-20261126.md)和log；已推成果无损，不能把失联时API读取冒作git pull。

每次 pull 后比较上次已读提交的根/题 README，差异立即读；至少每小时一次，读过 SHA 随本文件更新。root 负责 git/refs/push，子代理只写分配的独立文件。原数值运行范围不重开、不挪用失败 raw 充当前初值；本次新计算须独立说明模型、参数和实际范围。按旧 open 的运行安排，科学执行使用公开 Actions；本地作纸面推导与源码/已有日志解析。根 12 不增设冻结复跑审批，根 15 只留脚本/参数/run/哈希/结论，不保存可重算大数组。

## 2. 主完成标准

同一连通闭材料面上的连续 $C^2$ 嵌入族，全部 $F_t$ 对同一个固定 $g$ 等距。固定开握持区的像直径至少 $.2D$，整像不作刚体对齐的变化量至少 $.3D$；全时间 reach 至少 $.03D$。全域最大相对 metric 误差不超过 $10^{-6}$，且固定度量/参数/时间范围的加密下降至机器精度或求解容差。全域全时间嵌入/reach、可再生完整网格和严格存在差距都须交代。基本达标后继续 $.5D$ 或严格存在的强目标。障碍、有限阶可积、带边片和条件组装均非完成。

## 3. O2 当前真实数值状态

固定椭圆核心 $A=1,B=7/25,w_c=1/50$；$L=.9,r_c=.22,t_c=.036,t_f=.846$，六帽 $R=.274$。完整168/172表示及永久 enriched $c_0$ 不换。
固定 $g$ 身份 `fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`，$b_0$ 身份 `d61fb298989834c9eb2b4fe3bbff1fb5983d1bb3b3980cb6441f14e6c0299bb5`。

最新接受点仍为 **58**：粗/细辅助量 .26600541430262403/.26600541463999305、细κ57.9997782607127，非握持变化量。主reach局部需κ≤1000/61且欠全点对；球1.01/条带.38999未全域成立。ring17、反射R1、joint19、free36、prefix102、whole34、full51、full62均闭账失败，不重开。[joint168原终态](notes/2026-11-26-geometry-continuation-agent.md)run43925761699 research成功但solver达时限，无返回/候选；新增1234.031220492秒、累计5018.790751846秒/147原full。末trial曲率约46.2343而metric峰.78384，不授接受；report祖COMPLETE误分类已修。

### 新几何输入：O2b 逆设计与振荡尾

[R565](results/R565-parallel-oval-core-exact-reach-and-amplitude-budget.md)给平行椭圆柱reach恰r+q²/p；新p=.85、q=r=.15保持A1/B.3而核心reach3/17，和旧g不同。[v2首run失败](notes/2026-11-26-inverse-first-run-radial-fold-failure.md)：run45765708829两个新lane，粗η约.083/.091但fine 1.19855/3.78338、κ74208/26180；s=.421875漏径向近退化，球/条带也失败。Jac正确量级，不沿原软权重/固定49圈延长。

[R566](results/R566-flat-oscillatory-cap-tail-and-graph-reach.md)的固定有限公式尾在rc=.22到r=.30全平且K无限变号；完整凸底域graph片reach>.1832，但不含跨块。[R569](results/R569-fixed-oscillatory-tail-and-flat-infinitesimal-bending.md)对同一w已实际构造角频2非零全平无穷小等距场，全部导数exp(−c/δ³)，外端真ODE；X+tV非有限等距。[原R569种子终态](notes/2026-11-26-r569-seed-first-run-receipt.md)39.905028348科学秒、2850383次RHS；准确DtN截断与浮点误差分开。共同归一表内|f_rr|约5.05e7、|v_rr|约3.94e8，不能直接宏观放大；外端f/fr负，转新尾/真实shooting，不盲增M。[R571](results/R571-milder-phase-tail-flat-kernel-and-core-shooting-zero.md)换明确新尾w=.8exp[−(2−sin(δ^-1+φ))/δ]，统一patch reach>.08670；实际一维全平核、相位连续和负holonomy均证。周期真实连接下C_core必在某φ*准确零、A_core非零，故双固定平帽的闭旋转背景已有真实线性匹配。新[相位shooting计算包](notes/2026-11-26-r571-phase-shooting-implementation.md)已发布：M25、实接C²圆柱、φ根/导数/同根加密、同场A_core=1代价及4/6/8有限探针；结果待原终态。有限非线性/全闭reach仍欠，φ设计变化非同g弯曲。

[hard首run45769777022](notes/2026-11-26-hard-exchange-first-run-restoration.md)新37.974705078科学秒、仅几何恢复；其实际末q/网格/trust进入[识别续接](notes/2026-11-26-hard-exchange-identified-continuation.md)。[续接原终态45773550668](notes/2026-11-26-hard-resume-first-metric-progress.md)两lane新163.220723713/470.738431635秒：B030仍V=.0005436546、η2.0895893；B038在outer6真过fine几何，后71次可行metric改善至η=.8636074715，κ16.377643、球1.00949487、y.38973160，229×1536 fine。两lane最后均因提议1536角约束超原768容量结束，不能把提议算已采用；B030无OptimizeResult，B038末两次后端自然success。新[联合预算/分块Jac入口](notes/2026-11-26-joint-budget-block-jacobian-implementation.md)已发布：R1.012/Y.3928/τ.06072仍支付原比例；保原q/全pending径向，B038真纳1536约束，B030须先完整重建证旧几何角峰已覆盖。每16方向精确Jac、新trust=.5明记，首Actions方向核对一次；结果待原终态。仍欠冻结g精化/连续嵌入/全点对reach，不授README完成。原条件/失败完整存[续接前交接](notes/HANDOFF-before-hard-resume-20261126.md)。

## 4. O4 两个不同母库的有效入口

**33母（保原20/cap/13与一次固定χ）**：R533–554已给真实局部正则速度、负Π、k>2、返回层、总p2零/Π负或p1/p2共同零；完整t1速度负费未消。R558真γ=0正t1弧、R560短快变高度有号面积均已计真实历史，净t1仍负。下一为同一完整F/history的长程变高度返回及正净t1，不从局部正则自动推长时存在；其余矩、T、pose、period仍欠。

**R521正交母（不继承33母的原20/cap/13）**：R544–R563的同χ真实历史、慢快桥及限定尺度号障碍保持。新[R564](results/R564-negative-coupling-crossing-and-seven-exact-moments.md)在Ck>0下跨B零点，保完整真实端控/history清七矩；[R567](results/R567-complete-next-order-history-and-eight-exact-matrix-moments.md)完整次阶消项及共同4+1+2端图再清第八矩，原m=A=0。[R568](results/R568-even-end-germs-and-real-second-third-return.md)改真实末开控制并重解八矩，支付双端偶germ，PP^R准确闭scalar/全m/A/T。[R570](results/R570-neutral-residence-pose-and-real-four-piece-return.md)在八矩纤维以恒总驻留的有限词和首高尾真实位移支付两pose条件，(PP^R)²准确闭scalar/frame/位置/A/T。整个第四仍4V_P，同13/有限闭面继续；原限定族正R0/S1边界不撤。[R572](results/R572-odd-map-mother-and-all-actual-packet-total-fluxes.md)从起点以一个ψ×偶多项式球面奇映射选同母，准确清Λ(U)、有限仿射环境E的raw self及固定R521图全部实际微包总通量。非零χ在A=T=0时整周期等canonical∈E；不虚授偶germ属于常germ的U。整个period/内部partial/同13仍未清。

R555余五槽的真实Gram/有序面积身份继续有效；R526的倒行完成仍以实际M0/K0块为前提；R517周期scalar自动M0仍以真正合法周期轨道为前提。所有“尚未付”的端口不因下游条件定理自动消失。

新[圆核设计入口](notes/2026-11-26-circular-core-continuation-implementation.md)已单独发布：p=q=.18/offset.2先仅17径向变量恢复真实几何，再改变p并解锁81变量。连续公式起点η0不付非圆分支，C_core=0共振仍须解决；每个p重新实际过门，阶段η1e−4不是完成门。1 lane公开Actions，2400秒检查点；结果待原终态。

## 5. 正在继续的实际工作

1. 非圆实例在完整fine硬几何门内降metric，同时圆核设计同伦与R571真相位shooting接入有限非线性。必须最终冻结同一g再精化，并付全闭嵌入/全点对reach。
2. O4在已付scalar/pose/A/T及全部实际微包总通量之上继续整个第四/同13；同步检查长词直径与固定collar曲率的量级，不能让形式闭合替代主几何门。
3. [四来源本轮状态](notes/2026-11-26-current-four-source-topics.md)尚无可直接移用的全门族。O1圆领相位允许如实δE=0，仍须完整非旋转嵌入；O3保可用新局部输入。

入口：[open](open.md)、[当前索引](results.md)、[早期索引](results-index-early.md)、[日志](log.md)。未完成稿不登记已证明；每条完成结论立即提交推送，然后继续开放项。
