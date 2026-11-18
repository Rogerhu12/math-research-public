# HANDOFF — Astra-held10-7322d0de-20261118

维护会话：**Astra-held10-7322d0de-20261118**（AI）。前会话 Astra-held10-f00f08c9-20261117。**进行中，尚无满足全部完成标准的候选。** 不重做已登记结论；完整历史见log及归档索引，源/失败/命令见notes/results。

## 目标与同步

连通闭 C² 嵌入连续族；固定有内点 H、diamH≥.2D；整像δhold≥.1D，含全部O(3)取商δE>0；全时reach≥.03D。固定同一g/物理参数/时间范围，metric≤1e−6且空间/频率/时间精化下降至求解/机器地板。有限接受、条件比例窗或材料位移不替代全验收；达到后继续增大比例。

- 已部分克隆并真实pull，全文读根README授权/全部规则及本题README、旧交接/全部记录。
- 已读规则提交：`dac021c7e7a1a21d6d48dd72cf908ff893aa1532`。2026-11-18 08:21:35（UTC+8）独立稀疏发布worktree真实pull后双README无变化；至少每小时pull，变化只读diff并立即执行。
- 每条结论更新H/log后立即发布；至少每小时实际pull，检查双README，相对已读提交只读diff并立即执行。ref拒绝立即真实pull --rebase后非force重发至成功。
- 终端无可用认证，按根§8使用已连接GitHub小文本原子提交；真实终端pull仍执行。agent只写源，root独占publication Git。
- 可再生mesh/场/checkpoint/逐盒谱表不入Git、Release或CI；留源/参数/命令/hash/紧凑标量。单文件<100KB、H<10KB；无根LOG。旧scratch只读，运行副本隔离，不在运行中改源。无返回码不推断OOM或数学失败。

## 1. n4：新raw核与真正尾

**新主b=.16/λ=.02/M20**：2282点/18步，有限前缀metric8.91017947e−7过门；全19c/free c8/qactual=.012488347919833637，仍linear DN/新核非精化，见n4-primary-width-b016-m20。真尾.2H冷起/单峰/多峰及.5H均失败；.5H parts16为1.01243477e−8，Jac具名输入ULP灵敏度最高2.706倍原门，非误差界，见halfheight-tail-stage-sensitivity。仅parts32同20H仍失败1.521185788e−8（1.50倍），见halfheight-parts32-terminal。新态2304×40原state-only/full-Jac数值差全0（不含mean），不能归因两路径不一。全局主行175/c20为mode4动量−1ULP；只局部再读该行/174，元数据仅含1个已证全局峰，见n4-parts32-map-consistency-and-one-ulp-peak。唯一具名邻数后原DN继续，尚无接受尾/fullH/联立prefix。

同19c/e=.1875主b探针使M20外二阶谱降7.94倍、未表示参考二阶降8.54倍，见n4-actual-core-primary-width-probe。旧b.08 raw λ.02/M16 metric2.41705e−6，固定g/M20升3.43423e−6/tensor.0160166；峰s=.066873/频84，实际cond1≈4.278e12且H²白化无改善。M24在4460点欲加4906超6000、RMS.0032079，未完整metric/接受；见n4-raw-lambda002-fixed-m24-terminal、localization、parameter-and-collocation-scales，不重白化或盲升M28。

全19c整核法向角图使M20外二阶参考尾增46.25倍；低通K2只改善6.6%（λ1约.77%），两字面图正性已Fraction核。见n4-full-normal-angle-chart-probe、n4-low-normal-chart-filter；保持现图，不另开图BVP。核心rho数字仅原guard，有限FFT不作连续metric。

**旧actual固定g** eta.1/q*.01：M20 metric1.950429e−9；M24/shared/parts16完整1930点/4尾接受、最终9.82471e−10/A.942545，metric8.15575e−9升4.18倍、Darboux2.46911e−6降29.7%。λ0/非单调收敛或闭合，见n4-actual-fixed-m24-parts16。旧parts8的worker−9与原门5.41094e−9失败分开，不猜OOM；mode96非1ULP，见n4-m24-tail-residual-location。

R30共享engine的576段/990760标量逐位同、576→8。旧q.0175/.015及低幅λ失败不重跑；R19/19A与q.049的10%仍条件预算，见n4 notes。

## 2. m3：精确圆弧端点与高幅支

**λ1端点** q=.03991248545080898/a=.21/bp=.32/bc=.4/M16。首轮3729点/RMS12.9543/metric.421880失败；参考重投影无收益、共用C²窗仅改善初猜。实际Jac右坐标未改善原J线性误差，不装生产。单改窗36328已完整终止：4196点触6000节点门，RMS6.33003565/metric.346343328/Darboux10678.9，156域拒/0merit拒/7步；最终原尾1.375309609e−9/800有限Jac/audit通过不能补前缀。真实launcher/worker退出0；失败快照到最终物理metadata/mesh和解压系数全同。见m3-circle-endpoint-c2-seed-complete-failure，仍无λ1 accepted prefix。该失败physical quintic重建的原J方向21α全core拒：全步负样本/20缩步grid下界不能证，未到Frenet/merit。RMS逐值同但非失存raw cubic重放，见m3-endpoint-domain-rejection-is-grid-bound；新增全域解析ρ″的Bh²/8数值充分界、保原双界/1e−5/32768；原入口及失败态各14组几何/参数jets逐字节同。原20缩步仅guard过、负样本全步仍拒，未验Frenet/merit；见m3-raw-core-second-order-guard，14903单改guard入口已启动，初p/c/H/profile/repair同旧C²入口，cfg仅trace变；δ仍未知，非固定g精化。见m3-endpoint-second-order-guard-entry。初p/H同首轮及gauge−1ULP见entry。

原raw λ.02/M8四尾接受但metric8.30078e−5；固定g M16原tail一ULP失败后可选邻数初值获4尾/1143点/800Jac接受，metric却升9.35726e−5（tensor.209949）。七项g身份同，非收敛/闭合，见m3-raw-m16-complete-coupled-metric-failure、m3-one-ulp-initial-candidate-passes-original-tail。canonical各λ及parts16 metric3.97036e−4也失败；一次exact lift/free c6未补角谱，旧λ.02弧缺陷>.01255549非λ1。

**R41新核证书**：旧M16全15c改λ1/bp.32/bc.4，真积分/低2×2投影给||b+b″||<.024265039000279、rho∈(.6212861459223527,1.337031616589919)。17点真逆误差仅点态，q≈.04不在R38窗，失败终态c已变不能继承；见R41-general-width-raw-core-true-integral-oracle。actual-raw-integral-terminal-binding保实际宽度/λ及全c，new-design用自身δ/Lbin，fixed-refinement锁原atlas/family；目前只执行M16→M8元数据，无未来λ1端到端。

**R42/R43坐标定理**：W²正交后固定两列消矩，Gram=I+CᵀC且与原λ1 raw finite span相同。R43复用R41固定a=.21/bc=.4真矩，仅新增χ²三积分，精确2×2 Sylvester给所有M谱[1,13.92415)，不借浮点正交系数。有限M16新Gram条件2.061/旧5.788e11不等于C²/实际Jac界，原生产核未改。见R42、R43-fixed-supported-window-strict-gram-constant。

**严格条件窗** R32(bp.08)/R38(bp.32)：n3/eta0/a=.21/q∈[.0849,.0851]、相位.7046/H角[.3521,.3525]。R38重算圆心与真实三阶矩，在even C4保护弧零控制且||b+b″||≤.08时rho>.1642566、平面m3>.0948878、柱D<2.3181；完整未标记图若D≤2.6498/支撑≥.0801/|κ|≤12.5等全部成立，三重帽可得held/D>.105514、reach/D>.03018及全O(3)非全等。柱长.54/.5401须按实际全图矩选。全图假设尚未兑现。R40对原flat ramp、q∈[.039,.041]/δ≥.060严格给χ/R>.21088277799>.21；宽度无关且实际binary参数也过，但不证λ1解存在。

**已登记障碍**：R33/34只排冻结旧七矩/mean/主频路径，非自由actual；R35无限raw Tλ在λ<1仍双射、λ1才有无限核，须验实际弧缺陷。旧幅值初始化/七次失败、root瓶颈及径向精化见m3相应notes，不重跑或当不存在结论。

**q060高幅支** beta4.625：旧parts8三版候选失败/inner cubic未存已封存。parts16新H的stage86/mode3仅+1ULP后原worker接受1.818205542e−9/208有限Jac/audit，850f81a…，见q060-parts16-named-neighbor-original-acceptance。自动恢复尚未成功E2E。33116独立H_old原iter3失败3.671459625e−9，adf477…已存；外部候选明确V8 heap-limit/−6，未进inner，见q060-parts16-warmup-and-candidate-heap-terminal。v3只传同heap3072；补完93784真exit0，3实际试步0改善/fullreplay同，原状态未改/无DN重试。row86 c8/c11并列峰由依赖式推出，见q060-warmup-resource-candidate-tied-peak；下一项仅两具名邻数，不扩大搜索。仍无新prefix/闭面。

## 3. 全闭表示与严格连续metric

R21/R23有限C²闭图和完整mean接缝、R24固定帽排全O(3)。R28新M16/64图自身D≤2.301491469394、reach≥.1、H径比>.69794、held/D>.005462656及δE>0，不能搬旧M8矩。R29尾operator≤9.996591e−7、R31前缀<8.253e−7，真积分/舍入/唯一atlas已付。**低幅全闭全时metric<1e−6已证，held不足.1，仍无精确无限解证明。** 同checkpoint尾32→64真实R metric降12.66倍，但二阶层差.00629485未证C²极限。

R36旧actual raw M8真积分/反函数oracle；R37全角G/G′/T/T′余项<5.820e−12/2.330e−9/1.823e−9/4.184e−6；R39全1003径向段及固定真实atlas给微分余项ε<5.940838571e−9。仅若同图有限主部metric≤9.88118311e−7才推出真图<1e−6；该门未算且旧M8坏，不再为它全域分盒。新终态须自己的全角证书/有限主部/尾闭合，不继承旧数值界。

有限主部接口已执行：R39完整P按精确Fraction编译到R31全部metric卷积，保留q_gauge及中心/一次lift抵消；11关键span六jet共198有理比较、中心宽度1059个C²系数恒等式全0。仅a5=1单点消费接口核对，不是物理metric；拒绝未提供有限cut lift系数的包。见integral-principal-polynomial-interface；旧坏M8不再全域分盒。

## 4. 其他登记结论与分工

R12/14/15/16/17/18/20/22/25/26及m2 R11/R13已登记，详见对应notes/results。第三物理核与m2实际尾仍未付；旧m2循环根/n4第三核有限搜索不重跑，均非全不存在证明。

m3_true_coupling推进λ1实际联合，n4_round_core推进新b16实际尾；closed_geometry处理q060及独审，root核对并逐条发布。源树`/workspace/scratch/7322d0dee069/math-research-public`，发布树`/workspace/scratch/7322d0dee069/publication`。按open接着做，不以阶段报告、时间或等待回复收尾。
