# HANDOFF：大振幅新机制

**进行中，未完成；仍没有满足 README 全部条件的完整候选。**
接手会话：**Astra-new-mechanism-0105020f-20261126**（2026-11-26）。
原会话最后交接全文保存在 [继承交接](notes/HANDOFF-inherited-20261116-1809.md)；所有旧结论、条件、失败和运行成本保留，不以本次摘要撤销。

## 1. 规则与接手

已部分克隆并实际 `git pull main`，公开根 README、课题 README、HANDOFF、open、results 索引及相关 log/notes 已读。公开已读提交 **aba1c7964612cc61ffab56439886f61c70489028**（2026-11-26 07:16 UTC；本次实际pull后根/题README空差异）；私有根初读 **85fdf1853367ef25c07f3ebdb6ae25c22a3564b8**，随后逐次 pull/rebase 检查根差异，空差异。私有 QUEUE 的本题已改为本会话进行中并成功推送：**9278b28ddd4dcb9ac6ab4fd08909dfdbdd7a6ec7**；最后实际pull及规则同blob读至 **f269d5ce0269dc4eb2580f48cfcb76932f868452**（2026-11-26 06:37 UTC；实际pull/rebase后根README空差异、QUEUE仍本会话）。其它课题的并行认领保留。

历史运行的真实双仓pull、规则blob与私队回执保在各原观察note；当前已核hard首run公开到be4d8f6d/6408017f、私有到201c93af/79f66052，根/题规则均无变化，QUEUE仍本会话。早期盘满、05:48环境失联及05:54重新部分克隆的完整记录保于[本次先前HANDOFF](notes/HANDOFF-before-hard-restoration-20261126.md)和log；已推成果无损，不能把失联时API读取冒作git pull。

每次 pull 后比较上次已读提交的根/题 README，差异立即读；至少每小时一次，读过 SHA 随本文件更新。root 负责 git/refs/push，子代理只写分配的独立文件。原数值运行范围不重开、不挪用失败 raw 充当前初值；本次新计算须独立说明模型、参数和实际范围。按旧 open 的运行安排，科学执行使用公开 Actions；本地作纸面推导与源码/已有日志解析。根 12 不增设冻结复跑审批，根 15 只留脚本/参数/run/哈希/结论，不保存可重算大数组。

## 2. 主完成标准

同一连通闭材料面上的连续 $C^2$ 嵌入族，全部 $F_t$ 对同一个固定 $g$ 等距。固定开握持区的像直径至少 $.2D$，整像不作刚体对齐的变化量至少 $.3D$；全时间 reach 至少 $.03D$。全域最大相对 metric 误差不超过 $10^{-6}$，且固定度量/参数/时间范围的加密下降至机器精度或求解容差。全域全时间嵌入/reach、可再生完整网格和严格存在差距都须交代。基本达标后继续 $.5D$ 或严格存在的强目标。障碍、有限阶可积、带边片和条件组装均非完成。

## 3. O2 当前真实数值状态

固定椭圆核心 $A=1,B=7/25,w_c=1/50$；$L=.9,r_c=.22,t_c=.036,t_f=.846$，六帽 $R=.274$。完整168/172表示及永久 enriched $c_0$ 不换。
固定 $g$ 身份 `fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`，$b_0$ 身份 `d61fb298989834c9eb2b4fe3bbff1fb5983d1bb3b3980cb6441f14e6c0299bb5`。

最新接受点仍为 **58**：粗/细辅助量 .26600541430262403/.26600541463999305、细κ57.9997782607127，非握持变化量。主reach局部需κ≤1000/61且欠全点对；球1.01/条带.38999未全域成立。ring17、反射R1、joint19、free36、prefix102、whole34、full51、full62均闭账失败，不重开。[joint168原终态](notes/2026-11-26-geometry-continuation-agent.md)run43925761699 research成功但solver达时限，无返回/候选；新增1234.031220492秒、累计5018.790751846秒/147原full。末trial曲率约46.2343而metric峰.78384，不授接受；report祖COMPLETE误分类已修。

### 新几何输入：O2b 逆设计与振荡尾

[R565](results/R565-parallel-oval-core-exact-reach-and-amplitude-budget.md)给平行椭圆柱reach恰r+q²/p；新p=.85、q=r=.15保持A1/B.3而核心reach3/17，和旧g不同。[v2首run失败](notes/2026-11-26-inverse-first-run-radial-fold-failure.md)：run45765708829两个新lane，粗η约.083/.091但fine 1.19855/3.78338、κ74208/26180；s=.421875漏径向近退化，球/条带也失败。Jac正确量级，不沿原软权重/固定49圈延长。

[R566](results/R566-flat-oscillatory-cap-tail-and-graph-reach.md)的固定有限公式尾在rc=.22到r=.30全平且K无限变号；完整凸底域graph片reach>.1832，但不含跨块。[R569](results/R569-fixed-oscillatory-tail-and-flat-infinitesimal-bending.md)对同一w已实际构造角频2非零全平无穷小等距场，全部导数exp(−c/δ³)，外端真ODE；X+tV非有限等距。[首份种子原终态](notes/2026-11-26-r569-seed-first-run-receipt.md)run45771143212已成功闭账：39.905028348新科学秒、2850383次RHS；统一alpha160归一下的外端log尺度3857.13965，紧容差/M+1外端差约9.04e−9/2.73e−11。表内|f_rr|约5.05e7、单位T的|v_rr|约3.94e8，非连续上界；不能直接放大为宏观弯曲。外端f/fr均负，下一改尾/phase并实做C_core=0，不继续盲增M。

[hard首run45769777022](notes/2026-11-26-hard-exchange-first-run-restoration.md)两lane37.974705078新科学秒；16外层全恢复，0 OptimizeResult/metric阶段。B.30/.38 fine V=.0058134/.0027596、κ16.4887/16.4387，Ebar/det谷底受控但球/条带仍超。新[已识别状态续接](notes/2026-11-26-hard-exchange-identified-continuation.md)严格使用原81q/约束节点/trust，逐项与原FINAL/OUTER核对；微小漏峰完整pending、后端返回时批量交换，显著缺口才即时重启。原物理、硬门及fine验收容差不变；120外层/80步，257×768约束容量，2400秒检查点。未本地科学执行，发布后由公开Actions实际计算。原失败/条件/运行身份全文存[本次续接前交接](notes/HANDOFF-before-hard-resume-20261126.md)，不撤销。仍须冻结新g后的收敛、全闭嵌入/点对reach和宏观幅度。

## 4. O4 两个不同母库的有效入口

**33母（保原20/cap/13与一次固定χ）**：R533–554已给真实局部正则速度、负Π、k>2、返回层、总p2零/Π负或p1/p2共同零；完整t1速度负费未消。R558真γ=0正t1弧、R560短快变高度有号面积均已计真实历史，净t1仍负。下一为同一完整F/history的长程变高度返回及正净t1，不从局部正则自动推长时存在；其余矩、T、pose、period仍欠。

**R521正交母（不继承33母的原20/cap/13）**：R544同χ真实负p1/正t1；R548–557完整历史转向、三P和其后矩清零；R559/R563用真实长快回路得到 $P_0=P_1=P_2=T_1=R_1^y=S_0^y=0$。R562/R563在原既定尺度类的完整 $R_0^y>0$ 边界保留。新[R564](results/R564-negative-coupling-crossing-and-seven-exact-moments.md)跨过B的简单零点而保持Ck>0，完整两侧补偿桥、窄带快跨越、退化四端控与全部incoming已付；同χ双回路实际端IFT再清 $R_0^y$，故七矩准确同零。新[R567](results/R567-complete-next-order-history-and-eight-exact-matrix-moments.md)保r1横列并给完整次阶组合消项；三低尾及独立两长回路在同一4+1+2端图准确清八矩，原m=A=0。真实等待、初次快费、全部incoming/桥与参数位移均在同词。[R568](results/R568-even-end-germs-and-real-second-third-return.md)将末开控制改为真恒高度、保四端rank/成本并重解八矩，完整反射唯一性付双端偶germ；同χ实际PP^R准确闭scalar/全m/A/T。[R570](results/R570-neutral-residence-pose-and-real-four-piece-return.md)再用同高度总驻留恒定的有限姿态词，在真实八矩纤维支付frame/位置；实际incoming冻结成本保σ独立，末u_σ=O(δ²)。首高尾的慢图/旋转积分付横向位移主项，(PP^R)²准确闭scalar/pose/A/T。整个第四仍4V_P，13/有限闭面继续。

R555余五槽的真实Gram/有序面积身份继续有效；R526的倒行完成仍以实际M0/K0块为前提；R517周期scalar自动M0仍以真正合法周期轨道为前提。所有“尚未付”的端口不因下游条件定理自动消失。

## 5. 本次正在做的工作

1. 从已终止 run 的原日志闭 joint168 旧账；研究全域 metric 约束交换与局部空间控制，不重复已失败实例。
2. R567–R570已付同χ八矩、偶germ及scalar/pose/A/T完整返回；继续整个第四4V_P和同十三规范，不能用有限阶返回冒有限等距族。
3. [四来源本轮状态](notes/2026-11-26-current-four-source-topics.md)已按c9804f1e逐份读，尚无可直接移用的本题全门族，不跨场借metric/reach。继续检查 O1/O3 的新可用几何：圆领相位组装允许如实 $\delta_E=0$，但非旋转完整连接仍须实际构造；T-surface/管形必须同时满足闭合、二jet、全时reach。

主要入口：[open](open.md)、[当前索引](results.md)、[早期几何索引](results-index-early.md)、[日志](log.md)。本会话分工笔记为 `notes/2026-11-26-geometry-continuation-agent.md`、`results/R564-negative-coupling-crossing-and-seven-exact-moments.md`、`notes/2026-11-26-inverse-metric-design.md`；未完成笔记不登记为已证明结果。每写完一条结论立即提交推送，接下一开放项。
