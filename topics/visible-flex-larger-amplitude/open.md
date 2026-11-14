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

30最佳R267浮点下界表达式43.11565368239749来自原raw LSMR零乘子证据点，非后续H改善；跨点给C的gap表达式.7894044861，没有严格舍入包络。不同轮会刷新原权重，不能把不同轮merit相减。R262/263/265/267是有限优化工具，不新增原BVP门。

[actual37十一query](notes/2026-11-14-actual-request37-eleven-query-warm-and-RMS470.md) 全字节核验已完成，新warm/status为当前父。新增mid475在较近档有效，实际限制移到470。[request39十二query接口](notes/2026-11-14-twelve-query-fixed-support-RMS470-interface.md) 已接完整RMS470和同次原nodal J/P，但把局部投影可改节点固定在既有471–482+p；外部raw LSMR方向通过完整B_out z0_out进入affine offset。之后全向量radial仍会缩放外部，必须如实记录。保原λ270/LSMR200/17trial/全域/FD，无性能或QP收敛预断。原engine仅单模型iterations=1，不盲串旧十一query。

[request40完整QR入口](notes/2026-11-14-twelve-query-complete-QR-warm-interface.md) 已接同actual37父场，保十二query C baseline及完整global H候选；唯一原A/weights，300s/16active/1200H预算内以一次QR替内解，无旧PCG重试。原同f选择正文/原17trial/全域/新FD保持，失败保C；[R268](results/R268-complete-regularized-chain-border-QR.md)完整证明已发布。39前缀完整原包已核：111 B NPZ708数组、13端点/完整fixed-S/当前27与FD联集31源及全部父身份；其整步应用的是已强缩的方向，不能据α1自动优于37，也不跨轮减merit。40实际run43621054216同父37比较正在执行。

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

### 最新native39读回

新578系统本身全行exact初范数1.902947232e31，修正后2.570129142e32更坏，最坏new45对应旧44；[actual39完整结论](notes/2026-11-14-actual-request39-native-split-direction-failed.md) 已全文读并全字节核：49 manifest项、全部新旧J流/完整映射/两ledger/4checkpoint/原operand均过。既有逐块记录的大缺陷集中rawCell0多个segment，余504块远小。下一保原真实RK/grid（包括cusp）对首raw cell每步重置局部tangent，流式捕获全部短J/state；不机械只加44，不改g/ODE步/原门。动态depth consumer保旧边界/节点σ、实际mapping及577restriction，所有科学计算仅公开Actions。
