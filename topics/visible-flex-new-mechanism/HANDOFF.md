# HANDOFF：大振幅新机制

**进行中，未完成；仍没有满足 README 全部条件的完整候选。**
接手会话：**Astra-new-mechanism-0105020f-20261126**（2026-11-26）。
原会话最后交接全文保存在 [继承交接](notes/HANDOFF-inherited-20261116-1809.md)；所有旧结论、条件、失败和运行成本保留，不以本次摘要撤销。

## 1. 规则与接手

已部分克隆并实际 `git pull main`，公开根 README、课题 README、HANDOFF、open、results 索引及相关 log/notes 已读。公开已读提交 **8c3cbaa1315b461278ee1c3bef11bd6d715cfd0d**（2026-11-26 06:29 UTC；本次实际pull后根/题README空差异）；私有根初读 **85fdf1853367ef25c07f3ebdb6ae25c22a3564b8**，随后逐次 pull/rebase 检查根差异，空差异。私有 QUEUE 的本题已改为本会话进行中并成功推送：**9278b28ddd4dcb9ac6ab4fd08909dfdbdd7a6ec7**；最后实际pull及规则同blob读至 **ba1cda6de426c27058a55bfa0da33aa731a55d70**（2026-11-26 05:54 UTC）。其它课题的并行认领保留。

首run两job另实际pull公开至0bed8be337a9de6da7e1167ba7583a5aaf0c3efd、私有至7d6da16a7fc29488f6e8925d92601986798860fd，三规则不变且QUEUE为本会话；原收据见首run note。

初始执行盘仅余约 11 MB，普通历史的 blob:none 部分克隆仍在对象索引阶段磁盘不足，未改变远端。随后以 `--filter=blob:none --depth=1 --sparse` 在本次临时目录成功克隆两仓；公开仅检出本课题，私有仅根文件。终端 git 已恢复；旧交接中 11-16 执行环境不可用的描述不是本次现状。令牌只在命令行临时环境使用。05:48执行环境中断且临时盘清空；期间连接器只读规则并暂存未挂ref的源码/证明blob，未冒实际pull或科学执行。05:54环境恢复后两仓再次部分克隆及实际pull；已发布结论无损，未发布数值源码按明确新修订重建。

每次 pull 后比较上次已读提交的根/题 README，差异立即读；至少每小时一次，读过 SHA 随本文件更新。root 负责 git/refs/push，子代理只写分配的独立文件。原数值运行范围不重开、不挪用失败 raw 充当前初值；本次新计算须独立说明模型、参数和实际范围。按旧 open 的运行安排，科学执行使用公开 Actions；本地作纸面推导与源码/已有日志解析。根 12 不增设冻结复跑审批，根 15 只留脚本/参数/run/哈希/结论，不保存可重算大数组。

## 2. 主完成标准

同一连通闭材料面上的连续 $C^2$ 嵌入族，全部 $F_t$ 对同一个固定 $g$ 等距。固定开握持区的像直径至少 $.2D$，整像不作刚体对齐的变化量至少 $.3D$；全时间 reach 至少 $.03D$。全域最大相对 metric 误差不超过 $10^{-6}$，且固定度量/参数/时间范围的加密下降至机器精度或求解容差。全域全时间嵌入/reach、可再生完整网格和严格存在差距都须交代。基本达标后继续 $.5D$ 或严格存在的强目标。障碍、有限阶可积、带边片和条件组装均非完成。

## 3. O2 当前真实数值状态

固定椭圆核心 $A=1,B=7/25,w_c=1/50$；$L=.9,r_c=.22,t_c=.036,t_f=.846$，六帽 $R=.274$。完整168/172表示及永久 enriched $c_0$ 不换。
固定 $g$ 身份 `fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`，$b_0$ 身份 `d61fb298989834c9eb2b4fe3bbff1fb5983d1bb3b3980cb6441f14e6c0299bb5`。

最新接受点仍为 **58**：粗/细辅助度量量 $.26600541430262403/.26600541463999305$，细曲率 $57.9997782607127$。这些数不是握持变化量。主 reach 所需局部曲率约 $1000/61$，还欠完整非局部法弦界。全域球半径1.01和条带 $.38999$ 的连续支持条件若真满足才可使用 R33/R40 的 $.3D$ 幅度预算，当前未付。

原 ring17、反射 R1、joint19、free36、prefix102、whole34、full51、full62 均已失败闭账，不重做。11-16 遗留的 `joint168-fixed-height-continuation` run **43925761699** 已实际终止：research job **133504652845** success，report job **133517748533** failure。[原 research 日志已闭账](notes/2026-11-26-geometry-continuation-agent.md)：唯一solver达时限，无OptimizeResult/候选/预测/actual；新1234.031220492秒，祖累计5018.790751846秒/147原full值。末非候选 trial 的曲率约46.2343而全域metric峰升至.7838387322；固定selected池漏新峰。report误把嵌套祖COMPLETE当current而失败。须改变全域约束覆盖/几何表示，不延长旧SLSQP，不升格末trial。

### 新几何输入：O2b 逆设计

[R565](results/R565-parallel-oval-core-exact-reach-and-amplitude-budget.md)已证平行椭圆柱reach恰r+q²/p。新固定p=17/20、q=r=3/20保持外轴A1/B.3、核心reach3/17；其周长/待设计度量与旧g不同。已发布新v2逆设计源码/请求：同时设计a,z和全角切向，C∞平坦端口、全体段metric峰交换；两lane为B=.3与.38，49×96、8×4控制、每轮60次/三轮，公开Actions run45765708829已正常终态但两lane科学失败，无新接受候选。源重建后完整解析jet与前向参数微分由两路纸面审查，未本地科学执行。[首run原观察](notes/2026-11-26-inverse-first-run-radial-fold-failure.md)：B.3/.38粗η约.083/.091，97×192同qη1.19855/3.78338，κ74208/26180，s=.421875漏径向近退化；ball>1.42、|y|>.52且h触.08。Jac差1e−9量级，主要是采样和软几何失效。仅失败trial，不沿原49圈软权重延长；下一硬不等式/径向交换并接新振荡尾。最后必须冻结新g再精化，完整连接和全闭reach仍欠。 [R566](results/R566-flat-oscillatory-cap-tail-and-graph-reach.md)另给固定有限公式的C∞全平振荡尾：rc=.22到r=.30，K无限简单变号，完整凸底域帽/尾graph片reach≥1/K0>.1832，K0=(75/8)e^(-5/2)+256e^(-4)。此片不含跨块reach，非径向分支仍须求解；下一将它实际接入新模型。

## 4. O4 两个不同母库的有效入口

**33母（保原20/cap/13与一次固定χ）**：R533–554已给真实局部正则速度、负Π、k>2、返回层、总p2零/Π负或p1/p2共同零；完整t1速度负费未消。R558真γ=0正t1弧、R560短快变高度有号面积均已计真实历史，净t1仍负。下一为同一完整F/history的长程变高度返回及正净t1，不从局部正则自动推长时存在；其余矩、T、pose、period仍欠。

**R521正交母（不继承33母的原20/cap/13）**：R544同χ真实负p1/正t1；R548–557完整历史转向、三P和其后矩清零；R559/R563用真实长快回路得到 $P_0=P_1=P_2=T_1=R_1^y=S_0^y=0$。R562/R563在原既定尺度类的完整 $R_0^y>0$ 边界保留。新[R564](results/R564-negative-coupling-crossing-and-seven-exact-moments.md)跨过B的简单零点而保持Ck>0，完整两侧补偿桥、窄带快跨越、退化四端控与全部incoming已付；同χ双回路实际端IFT再清 $R_0^y$，故七矩准确同零。新[R567](results/R567-complete-next-order-history-and-eight-exact-matrix-moments.md)保r1横列并给完整次阶组合消项；三低尾及独立两长回路在同一4+1+2端图准确清八矩，原m=A=0。真实等待、初次快费、全部incoming/桥与参数位移均在同词。[R568](results/R568-even-end-germs-and-real-second-third-return.md)将末开控制改为真恒高度、保四端rank/成本并重解八矩，完整反射唯一性付双端偶germ；同χ实际PP^R准确闭scalar/全m/A/T。下一pose/整个第四2V_P及13，反射不自动闭它们。

R555余五槽的真实Gram/有序面积身份继续有效；R526的倒行完成仍以实际M0/K0块为前提；R517周期scalar自动M0仍以真正合法周期轨道为前提。所有“尚未付”的端口不因下游条件定理自动消失。

## 5. 本次正在做的工作

1. 从已终止 run 的原日志闭 joint168 旧账；研究全域 metric 约束交换与局部空间控制，不重复已失败实例。
2. R567/R568已付同χ八矩与双端偶germ、真实scalar/第二/第三返回；继续pose/整个第四及后续闭面，保持同词完整history和联合端图。
3. 检查 O1/O3 的新可用几何：圆领相位组装允许如实 $\delta_E=0$，但非旋转完整连接仍须实际构造；T-surface/管形必须同时满足闭合、二jet、全时reach。

主要入口：[open](open.md)、[当前索引](results.md)、[早期几何索引](results-index-early.md)、[日志](log.md)。本会话分工笔记为 `notes/2026-11-26-geometry-continuation-agent.md`、`results/R564-negative-coupling-crossing-and-seven-exact-moments.md`、`notes/2026-11-26-inverse-metric-design.md`；未完成笔记不登记为已证明结果。每写完一条结论立即提交推送，接下一开放项。
