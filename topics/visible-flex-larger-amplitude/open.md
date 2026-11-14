# 当前未解决的问题

完成条件以本题 [README](README.md) 为准，执行与规则同步见 [HANDOFF](HANDOFF.md)。只在公开 `Rogerhu12/math-research-public` 工作，科学计算只用本仓 Actions。每条结论即时 pull/check/push；任一子问题做完继续下项，不能把阶段报告当完成。

完整旧状态与逐次请求保留在 [截至request34的open检查点](open-checkpoint-through-request34-2026-11-14.md) 及 [更早open](notes/2026-11-14-open-before-current-continuations.md)。当前只有大幅开放前缀被接受，尚无满足全部标准的完整闭场。

## 1. 先打通同一大核的完整物理边值问题

唯一接受起点是M96/N1024的 .99 大核开放前缀，材料三分量误差5.77368e−7不等于operator证书；完整核G约.96000098、rho>.16385011989。后续 .996/.9975 的metric超限、.997875失败已保存，不重跑。现M112/T112/N2048、699节点、完整453状态及236036自由坐标，以旧M96只作初猜；原完整scalar/3控制、112材料H及全部physical/constant行保留。

真正T112零锚、338×112完整J、577×224原状态和audit已付1351.74s，不重复。严格七件身份相同的exact零H首请求可复用；新H、最后audit仍须真worker。旧ready或T96不能替代T112。所有warm目前仍明确未解完整BVP，不把极小H阈值归零，也不把仿射零锚边界FD冒充新H原生响应。

### 1A. 前缀可行下降：保原全域门，按真实拒绝点扩充方向模型

旧10–15的完整QR/band/bridge均无接受，盲增节点无效；17之后的实际下降与失败见对应notes。原26全角方向引擎与B源冻结，所有λ270/LSMR200、C-Hildreth200、原17试步、两完整RMS与rho/merit门保留。线性角不等式只约束优化方向，不替代真实非线性域检查，不声称完整QP最优。

| 已完成分支 | 实际结论 | 当前意义 |
| --- | --- | --- |
| 26五RMS与27七RMS | 实际合法下降；最近限制逐步移出原选定网格 | 已完成，保完整新warm/FD及原失败，勿重跑 |
| [29原中点观察](notes/2026-11-14-actual-request29-observed-seven-query-warm.md) | 七RMS全部正时，最近1/32在原mid473失败，更大步另有mid477；1/64真下降 | 给新增中点的实际依据，完整原returned middle/fm与2048角数组已保存 |
| [30完整H与C比较](notes/2026-11-14-actual-request30-complete-H-comparison-and-warm.md) | 同f中H44.35849607633413劣于C43.905058168501064，保C；1200H/18基/16工作行，17CG均未达原残差目标 | 有限H尝试确实执行；不据此盲增预算或声称QP收敛 |
| 30原非线性回溯 | α1/256真降.002933782783976824；最近1/128节点/中点全finite，但原left-RMS471失败 | 新warm8a91f696…/FD9.143364336e−10；仍col.0071104373/BC8.832e−8/native0 |
| [32九query](notes/2026-11-14-actual-request32-nine-query-warm-and-RMS471.md) | 1/16..1/128全部node/mid转finite，但原left-RMS471全拒；仍1/256真降.002631130390312819 | 新warm7f5e8d5f…/FD9.143364336e−10；85 B文件/536数组与全部父链已核，仍非BVP |
| [35十query](notes/2026-11-14-actual-request35-ten-query-step-and-midpoint475.md) | RMS471保护后α1/16真降.040416810520135016；最近1/8仅原mid475坏，全部十query正 | warm24ca673e…/FD9.255484210e−10，94 B NPZ594数组及原父链全核；下一只加mid475 |
| [37十一query](notes/2026-11-14-actual-request37-eleven-query-warm-and-RMS470.md) | α1/16真降.037699755252447176；1/8、1/4全node/mid及十一query过，完整left-RMS唯一470拒 | warmdd837483…/FD8.381607559e−10；39已完成固定局部支持的十二query |
| [39十二query固定S](notes/2026-11-14-actual-request39-fixed-support-projection-and-full-step.md) | C局部200sweeps仍272负slack；全向量radial .0026450024与原segment重组后α1真降.0022286119614634003，全原域过 | warm451e7ef1…/status51122351…/FD7.528714322e−10；col仍.0071103173，无新坏query支持扩组 |
| [40完整QR-H](notes/2026-11-14-actual-request40-complete-QR-H-working-row-limit.md) | 同父37的完整QR逆残差约1e−10；67.452s到16工作行上限，未修复全stationarity4.93e−9但1804负slack；repair .009590后H优C，α1真降.01201340937 | warmc62a7f12…/status30f19320…/FD7.157355711e−10；全部B/H/inverse数组核，col仍.007110308，下一同入口32行 |

30最佳R267浮点下界表达式43.11565368239749来自原raw LSMR零乘子证据点，非后续H改善；跨点给C的gap表达式.7894044861，没有严格舍入包络。不同轮会刷新原权重，不能把不同轮merit相减。R262/263/265/267是有限优化工具，不新增原BVP门。

[actual37十一query](notes/2026-11-14-actual-request37-eleven-query-warm-and-RMS470.md) 全字节核验已完成，新warm/status为当前父。新增mid475在较近档有效，实际限制移到470。[request39十二query接口](notes/2026-11-14-twelve-query-fixed-support-RMS470-interface.md) 已接完整RMS470和同次原nodal J/P，但把局部投影可改节点固定在既有471–482+p；外部raw LSMR方向通过完整B_out z0_out进入affine offset。之后全向量radial仍会缩放外部，必须如实记录。保原λ270/LSMR200/17trial/全域/FD，无性能或QP收敛预断。原engine仅单模型iterations=1，不盲串旧十一query。

[request40完整QR入口](notes/2026-11-14-twelve-query-complete-QR-warm-interface.md) 已实际完成同父37比较，完整事实见[actual40](notes/2026-11-14-actual-request40-complete-QR-H-working-row-limit.md)及[QR inverse字节审计](notes/2026-11-14-actual40-complete-QR-inverse-byte-audit.md)。唯一原A/weights及全部338链+112border，原同f选择/17trial/全域/FD保留。完整逆作用已准确到原H读回约1e−10；剩余直接限制是16工作行上限时全B仍1804负slack，故下一从实际40新warm/status继续同冻结入口、active32，保原时间/H预算和所有验收。不是从39新warm续，也不复用旧weights或跨轮减merit。无新坏query，不扩第13组。

[damping、坐标尺度和col读数解释](notes/2026-11-14-warm-damping-scales-and-collocation-readouts.md) 已按源和实际记录说明：λ270只定义当前步正则且冻结入口硬锁，S与Wr也不改变物理方程；真实merit无damping项，unweighted integrated col max与weighted L2不是同一量。现存报告未保存col argmax，不能猜其所在单元或模式。该分析没有改源或新增数值。


### 1B. Native：修复保存完整系统的原尺度线性缺陷

[23完整初猜](notes/2026-11-14-public-same-RK-candidate-v3-actual23.md) 的577×224全状态原noJ通过576个stage guard，norm.04177307820740199仍大于原2e−9；全部112H、51真实内部下溢与9546负零保全。原linearSteps定义far/graphs/gains/scales，不能整体改它冒仅更换初猜。

[25实际完整solve](notes/2026-11-14-public-native-seeded-full-actual25.md) 中，同seed基态withJac合法，但原correction后十档试步全部在stage13/raw0/seg7被D/S/A拒；无新cut J/fresh audit。不能直接绕入fullDN的新H。

[28完整捕获](notes/2026-11-14-actual-request28-native-linear-defect.md) 已保全部J/r/δ/原σ/cut/far及全29数组/116chunks。原σ浮点缺陷最大7.3718085303337e40在stage43/Pi110，cut/far0；原delta有限但巨大。极大chart condition不是全A条件数或全A奇异证明；普通float缺陷也不是保存binary数组的精确实数缺陷。

[原band接口](notes/2026-11-14-native-captured-band-correction-interface.md) 直接消费同保存A，原σ显式行列尺度、129248维/kl112/ku335带主元分解，恢复后回原方程读取全部旧/新缺陷，并在Actions对原/新最坏行算精确有理见证。31/33只在输入发布失败，没有科学执行，事实分别见 [31](notes/2026-11-14-actual-request31-artifact-publication-failure.md)、[33](notes/2026-11-14-actual-request33-read-only-publication-order.md)。[34实际带状重解](notes/2026-11-14-actual-request34-native-band-exact-defect.md) 完成同原矩阵LU，info0而新原σ浮点缺陷仍4.1558709373255425e30；同stage43/Pi110精确原数组值5.2938027944720597e30给严格full-model下界。此巨大δ暂不派trial；下一同J幂二行列均衡及精确原误差修正，保原尺度/方程与每次实际改善。

[actual36幂二均衡](notes/2026-11-14-actual-request36-native-equilibration-failed-direction.md) 实际完成但方向失败：同28 A，所有形成/恢复无损，行列max已在[1,2)，初全行exact原σnorm3.727905535e31，第一次修正反增4.510783064e31，停保初解。两次完整129248行/35数组/3checkpoint/原operand全字节核；无新J/native/trial，不盲加同种修正或派坏δ。下一38在原43/58同profile、原12步/各自原x/h顺序分6+6，实际保存4短块J及全中间state/原输出/mean对照；request38已接[实际短块probe入口](notes/2026-11-14-native-same-schedule-split-probe-interface.md)，原28 PIN输入，4短J+4独立noJ窗口，逐schedule/完整mean/原出口对照，计划STOP不做Newton/trial/audit；其余574原J/原σ/far/H不动。[actual38](notes/2026-11-14-actual-request38-native-short-blocks.md) 已实际完成：两段原出口/检查量/mean逐bit保持，4短J全finite；完整系统改善仍未证。request39/nativesplitband接[新578段消费者](notes/2026-11-14-native-split-equilibrated-interface.md)，保574旧块和4真实短块、全部原边界/旧节点σ，显式新节点σ；全行exact择新系统方向并保577 restriction，旧long-J缺陷仅诊断不作门。原完整nonlinear trial仍待真实方向。

[原十试步重放接口](notes/2026-11-14-native-band-trial-replay-interface.md) 已备，明确缓存28真实基态非新withJac；原十档alpha、完整evaluate/guard/严格下降原样且不重复J。接受一步也仅保存全state后STOP，不冒native/J/audit。当前不调度34坏δ。[全行exact dyadic接口](notes/2026-11-14-native-allrows-exact-dyadic-residual-interface.md) 用于原保存系统读回/误差修正，不新增README门。

[原stage J生成链诊断](notes/2026-11-14-native-stage-J-generation-and-propagation-scope.md) 已按actual28十层源码SHA核：stage导数是解析implicit/Fourier矩加RK变分，端点中心FD尚未执行。43/58各原12步无cusp；大条目、原缺陷最坏行与trial失败stage分别定位，不混作同一故障。保存A求解缺陷、J表示误差、连续流截断分开。后继最小分组保原每步x/h/profile和出口portRatio，withJac/noJ浮点网格及mean加法分别对照，不先增加ODE步或改g；尚未实际执行。

[原schedule6+6薄接口](notes/2026-11-14-native-same-schedule-windows-interface.md) 已冻结源2973c144…：仅对原无cusp43/58做可逆范围化，分别保withJac/noJ的原x/h算式、同profile/原出口port、全226中间state及mean。新映射579节点/578stage，旧节点σ保留、内节点取parentσ明示；只是尚未执行的可接组件，不能当新J改善。

### 1C. 保留的替代设计与真正fullDN衔接

R257严格有限恒速平面Fourier只能是圆；非圆core不能简单重命名成有限θ单位速入口。换θ需支付入口投影或完整analytic lift、core响应及证书成本。R259给小核心缩幅的实际有限系统共振与条件IFT；简单缩小初猜不自动消除设计核，不同λ次幂路径不得混用。[备用诊断接口](notes/2026-11-14-small-core-resonance-diagnostic-interface.md) 已冻结未调度，当前已有实际证据的主线先继续。

取得真实新H原生响应后，仍须原完整outer/inner、RMS1e−6、BC1e−11、native原容差及fresh audit全过。所有新H原尺度和完整物理cut数据须随响应保存，非零跨进程缓存不能冒同live predictor。

## 2. 同一接受场的闭合与固定g精化

完整联解接受后保存全部physical/constant状态和本场真实尾，核core/球排除、完整材料角cut谱/mean/九jet、唯一SE2与高度偏移，完成R249有限C²入口修补、上下尾与固定帽。新场已有z0，不加旧A mean；有限φ一般有无限θ谱，不能有限DFT同值冒连续接缝为零。R239连续定理仍需实际分支、turning number和全jet输入。

共享quintic背景及 [严格闭面wrapper](notes/2026-11-14-shared-background-closed-wrapper-interface.md) 已冻结：全部共享节点定义同一B、保帽高/marker、重建完整cut角差，原A.height/w/E目标g不覆写为B′。旧loader拒新包；[新cover/held接口](notes/2026-11-14-shared-background-cover-held-interfaces.md) 保完整空间与整面像公式。规范形/renderer差与原finiteGauss真导、返回ap/app、角投影和径向残差按R260分账，不据非恒等自行宣布超限。

定型后冻结全部scalar控制p*、尾帽g、区间、参数与t范围；按R240释放全部core取K0/k0/T=M，升频率/径向/积分。新 [same-g live-client接口](notes/2026-11-14-same-g-physical-DN-live-client-interface.md) 保同一TailClient/predictor依次新H/J→原FD→fullmain→fresh audit，严格绑定实际scalar sidecar。原699二分需1397点，不能误用1200。README要求等距误差精化到机器或原solver容差，不新增六/九jet全体机器收敛门；有限场及全t族仍必须C²，帽中心用固定图册。

旧A RK24/RK48、三闭mesh、全部2157568空间对及GW局部f8/16/48已完成封存。其幅度不足本题标准，不能继承其数值到新场，也不重复旧全场GW/Q或追任务外机器六jet门。

## 3. 全t嵌入、reach、固定区与整面像幅度

沿R248全相位强C²和metric/operator上确界归约，准确接缝前提必须已付。新场自己的R241全部参数块/正常锥条件须覆盖自交与double-normal瓶颈；marked整族不当刚体。R249修补仍保完整cut/mean/H，实际metric/曲率代价由新场消费。

D用完整闭F0直径；固定有内点H可取两固定帽并实算直径。须同时达到diamH≥.2D、整面像Hausdorff δhold≥.2D、全t reach≥.03D，以及含反射δE>0。材料点位移、仅core到core距离、core直径都不能替整面指标。旧A实际幅度约.063明确不达标。held可独立于尚未完成的reach点对状态读完整活动块/两帽盘见证，不设reach先通过的额外门。

R238/254/258给同场平面胚/非平面活动块/标记的刚性排除链，精确四点或四角行列式必须消费本场全部模式、shared节点、材料mean和完整尾。R242角解析精确等距定理不自动适用于有限metric缺陷或仅C²极限。数值包络的严格程度如实陈述，不能暗换区间证明。

## 4. 全域operator与最终交付的严格差距

R251四Loewner/完整Gram消费者已在request16通过三个解析例，但尚未消费新接受场；不重跑fixtures或加新验收门。实际完整prefix、finite48/64Gauss scalar、两尾帽和C²修补的相对metric operator需≤1e−6，不能把三分量≤1e−6直接改称operator≤1e−6。

完成全部数值标准后，给数个各<5MB网格、同g精化数据、全t/完整几何证据，明确无限尾或精确等距极限仍欠的严格存在论证。完整证明直接入results及索引，无额外独审/审批。必要旧未推依赖按HANDOFF幸存源重做，已恢复的43提交/R235–237及真RK24/RK48勿重复。只有全部README标准真实完成才收尾。

### 最新native41读回与request42双分支

[actual39完整结论](notes/2026-11-14-actual-request39-native-split-direction-failed.md) 已证保存的新578系统方向本身失败：全行exact1.902947232e31→2.570129142e32更坏，51块大缺陷全在rawCell0、余504块较小。故第41次保原每步schedule/RK/profile/完整226state，逐原步重置tangent，未增加ODE步或改g。

[actual41完整捕获](notes/2026-11-14-actual-request41-rawcell0-step-capture.md) 已实际完成：868原步/3472field，72原出口与[minA,minD,原mean和]全逐位同28；四cusp各13、其余12。新布局1372stage/1373node/N307552；所有3999文件、新289数组3545chunks、72原geometry包、原28完整数组、旧577映射和明确σ均字节核。新J最大已报条目1.573959534e13不等于新系统改善；0native/trial/endpoint/audit。

request42并行两条：前缀从真实40继续冻结QR入口active32；native按[逐原步新系统与完整exact接口](notes/2026-11-14-rawcell0-original-step-system-interface.md)消费原504 J和868新局部J，一次LU/3次幂二均衡/最多3严格改善精确残差修正，完整cut/所有stage/far行读回及577restriction。原28与41以真实public artifact PIN取入，见[41取入合同](notes/2026-11-14-pinned-actual41-artifact-fetch-interface.md)。旧long-J残差仅诊断，不用它增门；真正后继仍是原nonlinear完整noJ/原十alpha/原guard及严格原σ下降。前缀结果仍待；native实际失败见下列actual42记录。

[R269](results/R269-native-zero-reference-height-slope-gauge.md) 已完整证明原native零形状参考的可逆u/k坐标、可变w完整方程与常w精确仿射传播，及任意保存shooting矩阵的完整节点G/边界/原缺陷恢复式。尚未在actual28/41实施；实际非零H、port和节点geometry不能以理想参考替代，连续变换再RK也不冒原离散映射。下一G节点合同只读真实已存root.g，不阻塞42实际读回。


[实际41节点G合同](notes/2026-11-14-rawcell0-height-slope-node-gauge-contract.md) 已只读绑定：节点0..868取唯一首field0、cut末field3几何及原port，之后I；6个内部及3个旧边界两侧r/w bits不同，禁止混用同节点G。全dense模间条目、stage72左G右I、cut target/far/原σ恢复和原1372矩阵exact读回保全。尚未形成G或求解；终端失联后重建新SHA d24b6ee7…不冒未推e658c7原文。


### actual42 native：新1372系统自身仍失败

[实际42完整失败记录](notes/2026-11-14-actual-request42-native-original-step-direction-failed.md) 亲读公开小报告：307552行exact初1.220667068e22→修正1.256277542e22更坏，最坏new518＝旧42/step0/Pi112。行列max[1,2)、69149136形成项无所报尺度丢失、LUinfo0并不足够；保初delta ed6a8027…，不是旧long-J门拒绝。artifact14124997721/64948461B/ZIP4b48e8dc…、result741fb34e…保全，终端失联未独立审全部大阵，不能夸审计范围。不盲加同修正或派坏方向；下一独立节点G形成/恢复后仍原1372全行exact，原ODE/J/g/验收不变。


[R270完整局部约化](results/R270-exact-local-support-damped-QP-condensation.md) 已给完整证明：B仅支撑13节点+p时，完整236036维正阻尼QP精确等价于4397维Schur问题，外部physical和109freecore仍按唯一仿射最优响应恢复。平方根消元保Rᵀh=g、全部pure-global和原线性项，不把近似center当精确；原外部gradient给恢复误差界，全部24576行及原真实验收保持。当前只是等价表示与源接口，尚未执行新QP，不据此判42失败。


### request43：同原1372矩阵的实际节点G表示

[完整G消费者接口](notes/2026-11-14-rawcell0-gauge-band-consumer-interface.md) 已冻结，源24a51a4e…/16fca40e…。唯一实际G、869完整变换块含旧72接口、503原块逐字复用，保全部cut/target/H/far和原σ；方向恢复原Q/Pi后全307552 exact，改进RHS从原整数ledger经保存dyadic G最终一次舍入。longdouble实际精度/形成cast误差与后续均衡损失分账，不宣称有限形成严格相似或已改善。43先在同公开Actions读取已完42七个原报告薄摘要（不重科学），再一次LU/原exact有限改进；不派42坏δ、无新ODE/J/native/trial，全部大阵artifact-only。R270完整局部QP另行实现中，未修改旧冻源或验收。


[R271原RK逐级坐标协变](results/R271-discrete-RK-stage-gauge-covariance.md) 已完整证明，未来若需在原RK级内改变表示须保G_iG_j⁻¹全部输运、原port和唯一共享节点；不能把连续换元重新RK冒成同一离散映射。当前43仍仅保存的一步J两端形成，不为此证明额外采RHS/J。43已编译并完成42只读summary，等待实际G读回。
