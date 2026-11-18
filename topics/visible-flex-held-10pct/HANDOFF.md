# HANDOFF — Astra-held10-7322d0de-20261118

维护会话：**Astra-held10-7322d0de-20261118**（AI）。前会话 Astra-held10-f00f08c9-20261117。**进行中，尚无满足全部完成标准的候选。** 不重做已登记结论；完整历史见log及归档索引，源/失败/命令见notes/results。

## 目标与同步

连通闭 C² 嵌入连续族；固定有内点 H、diamH≥.2D；整像δhold≥.1D，含全部O(3)取商δE>0；全时reach≥.03D。固定同一g/物理参数/时间范围，metric≤1e−6且空间/频率/时间精化下降至求解/机器地板。有限接受、条件比例窗或材料位移不替代全验收；达到后继续增大比例。

- 已部分克隆并真实pull，全文读根README授权/全部规则及本题README、旧交接/全部记录。
- 已读规则提交：`071194c0b9e3cc41b377b68df83c2b8965d7edb7`。2026-11-18 08:29:29（UTC+8）独立稀疏发布worktree真实pull后双README无变化；至少每小时pull，变化只读diff并立即执行。
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

**λ1端点** q=.03991248545080898/a=.21/bp=.32/bc=.4/M16：首轮metric.421880失败，参考重投影/实际Jac右坐标无收益。仅C²窗36328仍4196点触6000门/RMS6.33004/metric.346343328；最终真尾通过不补前缀，见m3-circle-endpoint-c2-seed-complete-failure。失败physical quintic重建方向21α全core拒，非失存raw cubic或历史全部拒绝，见endpoint-domain-rejection-is-grid-bound。新全域ρ″的Bh²/8充分界保原双界/1e−5/32768，28组几何jets逐位同；20缩步仅guard过，见raw-core-second-order-guard。14903同初p/c/H只改guard仍失败：3469点触6000门/RMS3.70555，165域拒/34merit拒/16步；完整失败quintic d95ed7…先存，后prefix/seam审计抛Frenet −6.34619e−7，具体子调用无traceback不可定。未保存metric/接缝报告，无新H尾，只有2次初H接受；见m3-endpoint-second-order-guard-terminal。δ未知、非固定g精化，仍无λ1接受前缀。

五半宽a=.01/.05/.10/.15/.21、同271点/全15c/C²/λ1初猜RMS=.4228/.7022/1.1744/1.9491/3.0015；原初域过/H同锚，W_a/低矩投影随a变且basis身份锁定，见m3-circle-halfwidth-initializer-probe。据此新19739从原accepted λ.02启动a.01；与14903初16p/15c/16H/profile/C²元数据逐位同，实际1157初点，cfg只trace变。只有a改变，原模型/二阶guard/全部门保持，见m3-small-halfwidth-circle-entry；仍需新H/完整metric/接缝，短a无10%继承，通过后扩a.21。

原raw增幅初猜新增线性物理控制c_new=(qnew/qold_actual)c_old；只改原ratio幂，保共用C²窗/材料回拉/门。q.045、271点有限探针H及窗外场不变、控制式差1.32349e−23，无BVP/尾；见m3-raw-linear-amplitude-initializer。取得合格圆端点后才用于实际增幅。

原raw λ.02/M8四尾接受但metric8.30078e−5；固定g M16原tail一ULP失败后可选邻数初值获4尾/1143点/800Jac接受，metric却升9.35726e−5（tensor.209949）。七项g身份同，非收敛/闭合，见m3-raw-m16-complete-coupled-metric-failure、m3-one-ulp-initial-candidate-passes-original-tail。canonical各λ及parts16 metric3.97036e−4也失败；一次exact lift/free c6未补角谱，旧λ.02弧缺陷>.01255549非λ1。

**R41新核证书**：旧M16全15c改λ1/bp.32/bc.4，真积分/低2×2投影给||b+b″||<.024265039000279、rho∈(.6212861459223527,1.337031616589919)。17点真逆误差仅点态，q≈.04不在R38窗，失败终态c已变不能继承；见R41-general-width-raw-core-true-integral-oracle。actual-raw-integral-terminal-binding保实际宽度/λ及全c，new-design用自身δ/Lbin，fixed-refinement锁原atlas/family；目前只执行M16→M8元数据，无未来λ1端到端。

**R42/R43坐标定理**：W²正交后固定两列消矩，Gram=I+CᵀC且与原λ1 raw finite span相同。R43复用R41固定a=.21/bc=.4真矩，仅新增χ²三积分，精确2×2 Sylvester给所有M谱[1,13.92415)，不借浮点正交系数。有限M16新Gram条件2.061/旧5.788e11不等于C²/实际Jac界，原生产核未改。见R42、R43-fixed-supported-window-strict-gram-constant。

**严格条件窗** R32(bp.08)/R38(bp.32)：n3/eta0/a=.21/q∈[.0849,.0851]。R38在even C4弧上零控制且||b+b″||≤.08时给rho>.1642566、平面m3>.0948878、柱D<2.3181；若完整未标记图D≤2.6498/支撑≥.0801/|κ|≤12.5及原文全部C²/对称/帽等假设成立，则held/D>.105514、reach/D>.03018及全O(3)非全等。相位/H角与柱长按实际全图矩选，全部图假设未付，不能继承给改变后的控制。R40对q∈[.039,.041]/δ≥.060原flat ramp严格给χ/R>.21088277799>.21；宽度无关但不证λ1存在。

**已登记障碍**：R33/34只排冻结旧七矩/mean/主频路径，非自由actual；R35无限raw Tλ在λ<1仍双射、λ1才有无限核，须验实际弧缺陷。旧幅值初始化/七次失败、root瓶颈及径向精化见m3相应notes，不重跑或当不存在结论。

**q060高幅支** beta4.625：旧parts8三版失败/未存inner封存；parts16 H_new单邻数原接受1.818205542e−9，见q060-parts16-named-neighbor-original-acceptance。33116独立H_old失败3.671459625e−9、外部V8 heap-limit/−6；v3只传heap3072，补完3试步0改善。row86 c8/c11局部均负邻数/并列峰，唯一两项初值原全replay1.8357298125e−9；首loader schema错误0请求，v2只修错误字符串核对。51467原worker迭0接受同H_old/208Jac/audit，1153状态逐位同候选，c57fe4…，见q060-warmup-two-neighbors-original-acceptance。两H不可互借；正接回原prefix/raw-inner/DN锚保存，自动恢复成功E2E未付，无新闭面。

## 3. 全闭表示与严格连续metric

R21/R23全mean接缝、R24固定帽排全O(3)。R28/29/31低幅全C²闭图全时metric<1e−6已证：自身D≤2.301491469394/reach≥.1/H径比>.69794/δE>0，但held/D>.005462656，远未.1。同CP尾32→64真实metric降12.66倍，二阶层差.00629485未证C²极限；不能宣称精确无限解。

R36/37/39仅旧raw M8的真积分/真反函数/全1003径向span固定atlas，微分余项ε<5.940838571e−9；同图有限主部若≤9.88118311e−7才给真metric<1e−6。旧M8未过门，不重做全域分盒；新终态须自身全角证书/有限主部/尾闭合。

R39→R31完整主部Fraction编译已核11span六jet共198恒等式及中心1059个C²系数全0，保q_gauge/中心/lift抵消；仅a5=1单点接口，非物理metric。未知cut lift仍拒绝，见integral-principal-polynomial-interface。

## 4. 其他登记结论与分工

R12/14/15/16/17/18/20/22/25/26及m2 R11/R13已登记，详见对应notes/results。第三物理核与m2实际尾仍未付；旧m2循环根/n4第三核有限搜索不重跑，均非全不存在证明。

m3_true_coupling推进λ1实际联合，n4_round_core推进新b16实际尾；closed_geometry处理q060及独审，root核对并逐条发布。源树`/workspace/scratch/7322d0dee069/math-research-public`，发布树`/workspace/scratch/7322d0dee069/publication`。按open接着做，不以阶段报告、时间或等待回复收尾。
