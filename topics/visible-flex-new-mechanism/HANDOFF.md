# HANDOFF：大振幅新机制

**进行中，未完成；仍没有满足 README 全部条件的完整候选。**
接手会话：**Astra-new-mechanism-0105020f-20261126**（2026-11-26）。
原会话最后交接全文保存在 [继承交接](notes/HANDOFF-inherited-20261116-1809.md)；所有旧结论、条件、失败和运行成本保留，不以本次摘要撤销。

## 1. 规则与接手

已部分克隆并实际 `git pull main`，公开根 README、课题 README、HANDOFF、open、results 索引及相关 log/notes 已读。公开已读提交 **8f0c9a4c66964287ecc8a4fdd1e34a7474d8ceb6**（2026-11-26 08:08 UTC；本次实际pull后根/题README空差异）；私有根初读 **85fdf1853367ef25c07f3ebdb6ae25c22a3564b8**，随后逐次 pull/rebase 检查根差异，空差异。私有 QUEUE 的本题已改为本会话进行中并成功推送：**9278b28ddd4dcb9ac6ab4fd08909dfdbdd7a6ec7**；最后实际pull及规则同blob读至 **4f7e1d119bd02b0b37fe4d2d409a4f88c6a96a9e**（2026-11-26 08:06 UTC；实际pull/rebase后根README空差异、QUEUE仍本会话）。其它课题的并行认领保留。

各原观察note保真实双仓pull/规则blob/QUEUE回执；根/题规则均无变化。盘满和失联恢复原记录保于[先前交接](notes/HANDOFF-before-hard-restoration-20261126.md)，本次压缩前全文保于[几何转向前交接](notes/HANDOFF-before-compact-geometry-20261126.md)。API读取不冒git pull。

每次pull核根/题README差异并立即执行，至少每小时一次，SHA随H更新；root独占git及共享索引。科学仅公开Actions，本地限纸证/源码/原日志解析；根12不加机械复跑门，根15只留源码/参数/run/SHA/小结，不留可重算raw。每条完成结论即推；NFF立即pull --rebase再推。

## 2. 主完成标准

同一连通闭材料面上的连续 $C^2$ 嵌入族，全部 $F_t$ 对同一个固定 $g$ 等距。固定开握持区的像直径至少 $.2D$，整像不作刚体对齐的变化量至少 $.3D$；全时间 reach 至少 $.03D$。全域最大相对 metric 误差不超过 $10^{-6}$，且固定度量/参数/时间范围的加密下降至机器精度或求解容差。全域全时间嵌入/reach、可再生完整网格和严格存在差距都须交代。基本达标后继续 $.5D$ 或严格存在的强目标。障碍、有限阶可积、带边片和条件组装均非完成。

## 3. O2 当前真实数值状态

固定椭圆核心 $A=1,B=7/25,w_c=1/50$；$L=.9,r_c=.22,t_c=.036,t_f=.846$，六帽 $R=.274$。完整168/172表示及永久 enriched $c_0$ 不换。
固定 $g$ 身份 `fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`，$b_0$ 身份 `d61fb298989834c9eb2b4fe3bbff1fb5983d1bb3b3980cb6441f14e6c0299bb5`。

最新接受点仍为 **58**：粗/细辅助量 .26600541430262403/.26600541463999305、细κ57.9997782607127，非握持变化量。主reach局部需κ≤1000/61且欠全点对；球1.01/条带.38999未全域成立。ring17、反射R1、joint19、free36、prefix102、whole34、full51、full62均闭账失败，不重开。[joint168原终态](notes/2026-11-26-geometry-continuation-agent.md)run43925761699 research成功但solver达时限，无返回/候选；新增1234.031220492秒、累计5018.790751846秒/147原full。末trial曲率约46.2343而metric峰.78384，不授接受；report祖COMPLETE误分类已修。

### 新几何输入：O2b 逆设计与振荡尾

[R565](results/R565-parallel-oval-core-exact-reach-and-amplitude-budget.md)证平行椭圆柱reach=r+q²/p；新p=.85、q=r=.15给A1/B.3及reach3/17，非旧g。[v2失败](notes/2026-11-26-inverse-first-run-radial-fold-failure.md)细η1.19855/3.78338、κ74208/26180，径向漏谷且球/条带失败；不再延长原软权重49圈。


[R566](results/R566-flat-oscillatory-cap-tail-and-graph-reach.md)的固定振荡尾有整片graph reach>.1832，不含跨块；[R569](results/R569-fixed-oscillatory-tail-and-flat-infinitesimal-bending.md)已给同尾非零全平真线性核。其[原种子观察](notes/2026-11-26-r569-seed-first-run-receipt.md)表内|f_rr|5.05e7/|v_rr|3.94e8，不能直接宏观放大；准确DtN与浮点误差分开，X+tV非有限等距。

[R571](results/R571-milder-phase-tail-flat-kernel-and-core-shooting-zero.md)换明确δ^-1相位尾，统一patch reach>.08670；一维真flat核及负holonomy给周期connector上的真实C_core零/A_core非零。[原run45777456573](notes/2026-11-26-r571-phase-shooting-natural-final.md)173.782205514秒，选φ1.508384770827仍有C/A=−3.4767e−5；核心归一|Vss|9.41956e9，两个相位导数未稳定。M+1差2.43e−10不足解释根残差，不盲增M。转新连接段/更慢相位输入，复用已付φ0尾，实际付增益/高度/曲率/弧长预算；不是宏观可行候选。

[R574](results/R574-exact-nonlinear-height-equation-and-core-flux-transversality.md)给准确二次Darboux式、核心通量和有限差Green身份，真实零处D=−(3/R)(C/A)′；二阶均值响应可积分。受迫高模、正定developing与退化核心C2边界、有限分支仍欠。所有φ/connector设计变化先换g，最终仍须冻结同一g。


[硬几何首run](notes/2026-11-26-hard-exchange-first-run-restoration.md)与[原门识别续接](notes/2026-11-26-hard-resume-first-metric-progress.md)完整闭账：B030末V=.00054365/η2.089589，B038首次fine可行并降η至.86360747；均止于未采用1536角超过原768容量。实际原q/网格/trust保，原资格不因新预算改判。

[联合预算/分块Jac](notes/2026-11-26-joint-budget-block-jacobian-implementation.md)改R1.012/Y.3928/τ.06072，仍支付原比例；新trust=.5及每16方向AD明确。[B030实际终态](notes/2026-11-26-joint-budget-b030-first-metric-receipt.md)run45777140827/job139763424593新增181.995016962秒、方向差3.81e−10：241×3072 fine的V=0、η=.939818940292、κ16.452596、球1.01043031、y.38901204。真实119×1536约束、3072仅末提议，12外层后容量终态，无OptimizeResult；[B038原终态](notes/2026-11-26-joint-budget-b038-metric-and-peak-cap-receipt.md)新增848.448631589秒：243×3072 fine V=0、η=.853614316555、κ16.452787；实际121×1536/trust1/64，122×3072未采用。末后端自然success46步；前五次细峰重启无接受，旧log未读coarse违约故不臆判原因。[连续角峰接口](notes/2026-11-26-continuous-theta-peak-oracle-design.md)已登记，正实现独立源：分开FFT求积/真实约束角/径向覆盖，Ebar仍完整角积分，求积误差和连续证书另付。所有点值几何可行均非全闭reach，g尚未冻结。


## 4. O4 两个不同母库的有效入口

**33母（保原20/cap/13与一次固定χ）**：R533–560已付真返回层、双保持及p1/p2端图，净t1仍负。原所有范围/失败见上述完整交接与open；下一同一完整F/history的长程变高度净正t1，余矩/pose/period仍欠，不跨接R521母。

**R521正交母（不继承33母的原20/cap/13）**：[R567](results/R567-complete-next-order-history-and-eight-exact-matrix-moments.md)保同χ真实history/跨带/完整次阶清原八矩，m=A=0；[R568](results/R568-even-end-germs-and-real-second-third-return.md)付双端偶germ，PP^R闭scalar/m/A/T。[R570](results/R570-neutral-residence-pose-and-real-four-piece-return.md)再付真实pose，使(PP^R)²闭scalar全jets/frame/位置/A/T，但第四仍4V_P。[R572](results/R572-odd-map-mother-and-all-actual-packet-total-fluxes.md)从起点奇映射选同一母，清自然Λ(U)、环境E的raw self和R521全部微包总通量；非零χ的A=T=0周期等canonical∈E。whole period/内部partial/同13未清；R573又限制原分离尺度几何。前史所有限定结论仍保于完整交接/各R原文。


R555余五槽的真实Gram/有序面积身份继续有效；R526的倒行完成仍以实际M0/K0块为前提；R517周期scalar自动M0仍以真正合法周期轨道为前提。所有“尚未付”的端口不因下游条件定理自动消失。

新[圆核设计入口](notes/2026-11-26-circular-core-continuation-implementation.md)：p=q=.18/offset.2先17径向变量，再改变p解81变量。[首启动失败](notes/2026-11-26-circular-entry-angular-guard-failure.md)run45775603393的16角违反原最小20保护，.604799秒即退、未进模型科学。现v2改32角/fine64并同步CLI guard；原物理门不变。圆核η0不授非圆分支，仍欠C_core共振；阶段η1e−4非完成门。


## 5. 正在继续的实际工作

1. 非圆实例在完整fine硬几何门内降metric，同时圆核设计同伦与R571真相位shooting接入有限非线性。必须最终冻结同一g再精化，并付全闭嵌入/全点对reach。
2. O4转紧凑/有限尺度真实返回，并继续整个第四/同13。[R573](results/R573-fixed-collar-curvature-and-separated-scale-reach-obstruction.md)已证：原固定collar给reach≤H²+(ξc+Ω)⁻²，首高尾给实际D≥c√R logR/δ−C_R；固定R最后δ→0时reach/D→0。只排该分离尺度极限，不排未核有限参数或其他输入；净位移闭合/整体缩放/增加形式阶数不能修复。新R530有界高度路径须付全程空间范围和真实端图。
3. [四来源本轮状态](notes/2026-11-26-current-four-source-topics.md)尚无可直接移用的全门族。O1圆领相位允许如实δE=0，仍须完整非旋转嵌入；O3保可用新局部输入。

入口：[open](open.md)、[当前索引](results.md)、[早期索引](results-index-early.md)、[日志](log.md)。未完成稿不登记已证明；每条完成结论立即提交推送，然后继续开放项。
