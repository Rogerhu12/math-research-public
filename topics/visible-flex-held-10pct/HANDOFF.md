# HANDOFF — Astra-held10-7322d0de-20261118

维护会话：**Astra-held10-7322d0de-20261118**（AI）。前会话 Astra-held10-f00f08c9-20261117。**进行中，尚无满足全部完成标准的候选。** 不重做已登记结论；源、完整历史/失败/命令见 results、notes、log。

## 目标与同步

连通闭 C² 嵌入连续族；固定有内点 H、diamH≥.2D；整像δhold≥.1D，含全部O(3)取商δE>0；全时reach≥.03D。固定同一g/物理参数/时间范围，metric≤1e−6且空间/频率/时间精化下降至求解/机器地板。有限接受、条件比例窗或材料位移不替代全验收；达到后继续增大比例。

- 已部分克隆并真实pull，全文读根README授权/全部规则及本题README、旧交接/全部记录。
- 已读规则提交：`ecc1466c0a358409a44a5a0bd05a76d0b7e71f7b`。2026-11-18 07:47:30（UTC+8）独立稀疏发布worktree真实pull后双README无变化；至少每小时pull，变化只读diff并立即执行。
- 每条结论更新H/log后立即发布；至少每小时实际pull，检查双README，相对已读提交只读diff并立即执行。ref拒绝立即真实pull --rebase后非force重发至成功。
- 终端无可用认证，按根§8使用已连接GitHub小文本原子提交；真实终端pull仍执行。agent只写源，root独占publication Git。
- 可再生mesh/场/checkpoint/逐盒谱表不入Git、Release或CI；留源/参数/命令/hash/紧凑标量。单文件<100KB、H<10KB；无根LOG。旧scratch只读，运行副本隔离，不在运行中改源。无返回码不推断OOM或数学失败。

## 1. n4：新raw核与真正尾

**新主b=.16/λ=.02/M20有限前缀metric过门**：2282点/18个α1步/无域或merit拒绝，metric8.91017947e−7/flow8.88822e−6/Darboux.00415666；qactual=.012488347919833637，全19c/free c8/J16/eta.1/wCut.16。改核非精化、仍linear DN/非精确圆弧，见n4-primary-width-b016-m20。原parts16/N512真尾：.2H冷起失败1.13915e−8；单峰+3ULP后原DN仍失败8.02443e−9；多峰8候选无改善/未重调DN，见n4-raw-b016的actual-parts16、single-relaxation、multipeak及两locator notes。该失败态续到.5H（55129真实terminal）iter4失败1.01243477e−8/A.9807524，完整20H及物理配置不变；0接受尾、fullH未执行/未入prefix，见n4-raw-b016-halfheight-tail-terminal。只对新态定位，不沿用旧.2H峰位。

同19c/e=.1875主b探针使M20外二阶谱降7.94倍、未表示参考二阶降8.54倍，见n4-actual-core-primary-width-probe。旧b.08 raw λ.02/M16 metric2.41705e−6，固定g/M20升3.43423e−6/tensor.0160166；峰s=.066873/频84，实际cond1≈4.278e12且H²白化无改善。M24在4460点欲加4906超6000、RMS.0032079，未完整metric/接受；见n4-raw-lambda002-fixed-m24-terminal、localization、parameter-and-collocation-scales，不重白化或盲升M28。

全19c整核法向角图使M20外二阶参考尾增46.25倍；低通K2只改善6.6%（λ1约.77%），两字面图正性已Fraction核。见n4-full-normal-angle-chart-probe、n4-low-normal-chart-filter；保持现图，不另开图BVP。核心rho数字仅原guard，有限FFT不作连续metric。

**旧actual固定g** eta.1/q*.01/δ=.030027177128250468/vd=.2483630655929876：M20/1913点metric1.950429e−9；M24/shared/parts16完整1930点/4尾接受、最终9.82471e−10/A.942545，metric8.15575e−9升4.18倍、Darboux2.46911e−6降29.7%。λ0，非单调收敛/闭合，见n4-actual-fixed-m24-parts16。旧parts8的worker−9与原门5.41094e−9失败分开，mode96非1ULP；见n4-m24-tail-residual-location。不猜OOM。

R30共享engine原576段/990760标量逐位同值、576→8。旧q.0175/q.015及低幅λ各失败见n4 notes，不重跑。R19/19A/eta.1-q.049的10%仍条件预算。

## 2. m3：精确圆弧端点与高幅支

**λ1端点** q=.03991248545080898/a=.21/bp=.32/bc=.4/M16。首轮3729点/RMS12.9543/metric.421880失败；参考重投影无收益、共用C²窗仅改善初猜。实际Jac右坐标未改善原J线性误差，不装生产。单改窗36328已完整终止：4196点触6000节点门，RMS6.33003565/metric.346343328/Darboux10678.9，156域拒/0merit拒/7步；最终原尾1.375309609e−9/800有限Jac/audit通过不能补前缀。真实launcher/worker退出0；失败快照到最终物理metadata/mesh和解压系数全同。见m3-circle-endpoint-c2-seed-complete-failure，仍无λ1 accepted prefix。原rho数值下界2.31933e−5已用32768格、样本.626637；继续单状态域诊断，不能归因所有历史拒绝。初p/H同首轮、旧gauge首c−1ULP和三项初始化/Jac诊断见entry及相关notes。

原raw λ.02/M8四真尾接受但metric8.30078e−5；冻整g M16首次call3因stage86/mode3一ULP失败。共享engine/可选单邻数初猜保留原门，重试完整1143点/4尾/800有限Jac接受，最终尾1.37847e−9，prefix metric却升9.35726e−5/tensor.209949。七项固定g身份全同，非收敛/闭合；见m3-raw-m16-complete-coupled-metric-failure、m3-one-ulp-initial-candidate-passes-original-tail。canonical各λ及parts16完整metric3.97036e−4失败；一次exact lift/自由c6并不能补未表示角谱。旧λ.02中心弧缺陷>.01255549，不等于λ1。

**R41新核证书**：旧M16全15c改λ1/bp.32/bc.4，真积分/低2×2投影给||b+b″||<.024265039000279、rho∈(.6212861459223527,1.337031616589919)。17点真逆误差仅点态，q≈.04不在R38窗，失败终态c已变不能继承；见R41-general-width-raw-core-true-integral-oracle。actual-raw-integral-terminal-binding保实际宽度/λ及全c，new-design用自身δ/Lbin，fixed-refinement锁原atlas/family；目前只执行M16→M8元数据，无未来λ1端到端。

**R42/R43坐标定理**：W²正交后固定两列消矩，Gram=I+CᵀC且与原λ1 raw finite span相同。R43复用R41固定a=.21/bc=.4真矩，仅新增χ²三积分，精确2×2 Sylvester给所有M谱[1,13.92415)，不借浮点正交系数。有限M16新Gram条件2.061/旧5.788e11不等于C²/实际Jac界，原生产核未改。见R42、R43-fixed-supported-window-strict-gram-constant。

**严格条件窗** R32(bp.08)/R38(bp.32)：n3/eta0/a=.21/q∈[.0849,.0851]、相位.7046/H角[.3521,.3525]。R38重算圆心与真实三阶矩，在even C4保护弧零控制且||b+b″||≤.08时rho>.1642566、平面m3>.0948878、柱D<2.3181；完整未标记图若D≤2.6498/支撑≥.0801/|κ|≤12.5等全部成立，三重帽可得held/D>.105514、reach/D>.03018及全O(3)非全等。柱长.54/.5401须按实际全图矩选。全图假设尚未兑现。R40对原flat ramp、q∈[.039,.041]/δ≥.060严格给χ/R>.21088277799>.21；宽度无关且实际binary参数也过，但不证λ1解存在。

**已登记障碍**：R33/34只排冻结旧七矩/mean/主频路径，非自由actual；R35无限raw Tλ在λ<1仍双射、λ1才有无限核，须验实际弧缺陷。旧幅值初始化/七次失败、root瓶颈及径向精化见m3相应notes，不重跑或当不存在结论。

**q060高幅支**：beta4.625/q.040联合metric6.91e−9；q.060旧H局部初值获原尾1.993008435e−9/208Jac。36748新H call3原门失败3.2413445e−9，stage45/mode12=70ULP、stage43/mode15=3ULP；临时inner success但未存p/sol，无最终prefix。见m3-q060-resumed-prefix-new-height-tail-failure。三版内部候选23/27/72次均0改善、未重调DN；最小1ULP仍推高邻行，二节点最好3.76014e−9。原worker恢复/原cubic及DN锚点保存入口已备，尚无成功恢复E2E，见q060-original-worker-recovery-and-local-candidate-failures。停止该局部变体族；同H原生parts8→16的68353仅观察缺口、无原响应/退出码，不判数学失败；19362同源新前缀续跑。见q060-nested-parts-observation-gap，不改门或反推失场。

## 3. 全闭表示与严格连续metric

R21/R23有限C²闭图和完整mean接缝、R24固定帽排全O(3)。R28新M16/64图自身D≤2.301491469394、reach≥.1、H径比>.69794、held/D>.005462656及δE>0，不能搬旧M8矩。R29尾operator≤9.996591e−7、R31前缀<8.253e−7，真积分/舍入/唯一atlas已付。**低幅全闭全时metric<1e−6已证，held不足.1，仍无精确无限解证明。** 同checkpoint尾32→64真实R metric降12.66倍，但二阶层差.00629485未证C²极限。

R36旧actual raw M8真积分/反函数oracle；R37全角G/G′/T/T′余项<5.820e−12/2.330e−9/1.823e−9/4.184e−6；R39全1003径向段及固定真实atlas给微分余项ε<5.940838571e−9。仅若同图有限主部metric≤9.88118311e−7才推出真图<1e−6；该门未算且旧M8坏，不再为它全域分盒。新终态须自己的全角证书/有限主部/尾闭合，不继承旧数值界。

有限主部接口已执行：R39完整P按精确Fraction编译到R31全部metric卷积，保留q_gauge及中心/一次lift抵消；11关键span六jet共198有理比较、中心宽度1059个C²系数恒等式全0。仅a5=1单点消费接口核对，不是物理metric；拒绝未提供有限cut lift系数的包。见integral-principal-polynomial-interface；旧坏M8不再全域分盒。

## 4. 其他登记结论与分工

R12/14接缝、R15轴曲率、R16过零权逆、R17对称、R18混合DAE已证；R20/22有限/条件障碍不等于全不存在，R25正A动量唯一根不推出shoot存在，R26三谐波仍缺第三物理核。m2 R11开放held>.1076/R13条件闭合>.10338，实际尾未付；旧m2循环根和n4第三核有限搜索不重跑，不当容量证明。

m3_true_coupling负责λ1真联合/坐标；n4_round_core负责新b16实际尾；closed_geometry负责真积分/有限主部/连续证明；root独立核对、具体残差初始化及逐条发布。源树`/workspace/scratch/7322d0dee069/math-research-public`，发布树`/workspace/scratch/7322d0dee069/publication`。按open接着做，不以阶段报告、时间或等待回复收尾。
