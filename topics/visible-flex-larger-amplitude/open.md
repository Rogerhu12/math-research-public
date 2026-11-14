# 当前未解决的问题

完成条件以本题 [README](README.md) 为准，执行、原件身份与规则同步见 [HANDOFF](HANDOFF.md)。仅公开 `Rogerhu12/math-research-public`，科学计算只本仓 Actions；每条结论即时 pull/check/push，子问题完成继续下一项，不能把阶段报告当完成。当前只有大幅开放前缀被接受，尚无符合全部标准的完整闭场。

完整逐次历史保存在 [截至request49的原open](open-checkpoint-through-request49-2026-11-14.md)、[截至34的检查点](open-checkpoint-through-request34-2026-11-14.md) 与各实际note；这里去除已完成请求的旧“待运行”措辞，不重跑旧结果。

## 1. 打通同一大核的完整物理边值问题

唯一接受起点为 M96/N1024 的 .99 大核开放前缀；其材料三分量误差5.77368e−7不是operator证书，G约.96000098、rho>.16385011989。后续 .996/.9975 的metric超限及 .997875失败已保存。现有 M112/T112/N2048、699节点、完整453状态与236036自由坐标，M96只作初猜，原scalar/3控制、112材料H及全部physical/constant行保持。

真T112零锚、完整338×112 J、577×224原状态及audit已实际付费完成。只有七件身份相同且exact零H首请求可复用，新H与最终audit仍用真worker；不将微小H归零，不拿T96代T112。当前全部warm明确未解完整BVP，仿射零锚FD不冒新H原生响应。

### 1A. 前缀：按真实非线性拒绝点补齐方向模型

原完整原子模型、λ270/LSMR200、C-Hildreth200、17档alpha、原node/mid/两RMS、rho/merit门保持。线性角不等式只约束方向，不替代真实全域检查。原权重每轮刷新，禁止跨轮merit相减；unweighted col与weighted L2不同，原报告未给col argmax不能猜位置。

[R270完整局部凝聚](results/R270-exact-local-support-damped-QP-condensation.md) 保完整236036维模型的原g、pure-global仿射列和全部外部physical/109freecore条件响应。平方根消元不以近似center替g，局部QP可行修复后一次完整原H恢复；同原C和全部真实门比较。原库可动态选局部节点，没有固定4397维限制。完整QR factor没有导出，不能因派生数组审计齐全而称独立完整factor审计。

| 实际工作 | 已保存结论 | 下一用途 |
| --- | --- | --- |
| [actual40完整QR](notes/2026-11-14-actual-request40-complete-QR-H-working-row-limit.md) | 原H逆读回约1e−10；16工作行后仍1804负约束，修复后真实α1下降 | 已完成，不重同预算 |
| [actual42前缀](notes/2026-11-14-actual-request42-complete-QR-32-row-warm.md) 与 [46原内部回执](notes/2026-11-14-actual-request46-request42-working-row-and-radial-readback.md) | 32工作行预算停止；未修复1668负slack、内部radial .0078912695；外层1不能称无修复 | 完整原报告已回读，不重科学 |
| [actual45完整局部QP](notes/2026-11-14-actual-request45-condensed-QP-and-midpoint482-limit.md) | 12query/24576行、局部4397；同f H43.8582164优C44.2768871，α1/32真下降；最近拒绝仅mid482 | 完整数组/父链与14root raw已审，已接48 |
| [actual48](notes/2026-11-14-actual-request48-thirteen-query-and-left-RMS482-limit.md) | 加mid482→13query/26624行/4735局部；H43.8445468优C44.2514049，α1/256才真下降 | 最近五档13选定网格/node/mid均好，完整left-RMS482拒；据此接49 |

[actual49完整14-query](notes/2026-11-14-actual-request49-fourteen-query-and-left-RMS469-limit.md)接受α1/16，最近仅left469拒，已据此派51，原件/完整audit保留。

**当前父actual53完成**：run43634517255/source dd3156cfe7e5197029ce45fff5beb53115de3680；[完整实际结论](notes/2026-11-14-actual-request53-working512-and-midpoint481-limit.md)。同15查询/30720行/5073支持，512工作行的最终完整stationarity9.59012e−7，修复radial.9999999999987809，rawgap1.42109e−14仅浮点诊断非认证。最近1/32的十五真实网格均合法，唯一坏原中点481；1/64才接受，merit44.11665947585927→44.105521474605546，col.007109981682135472/BC6.1823900322767e−8/FD7.165083799852089e−10，仍非完整BVP/native。父场和权重变更，不跨轮相减目标。

全部137domain/880NPY、88凝聚/38完整向量、9observer/44源/父51链与14raw217496448B已byte核，未导出fullfactor不冒审。新父warm e71a5fec344326df3b6c69ec6d298f5079034fb86eb2fa505008c35682010d32；原status6170aba505c2eeb5db9411f13ad502363fe1593a7d4d63faa5f0d0a37fb34938，公开gzip须透明还原1251975B原件。

**56准备中**：只新增原mid481全2048角成16查询，完整5073支持已有所需端点；保512/dual200/600s/1200s/λ270/LSMR200/C200/17trial/全部真实门和FD。只读col observer记录完整原col最大项及原baseline权重，不增加科学调用。1/4另坏mid483，更大步已建模网格也会坏，不能预言16即可α1。旧51及更早完整结果保notes，不重跑。

### 1B. Native：先分清保存矩阵、传播与求解误差

[23完整seed](notes/2026-11-14-public-same-RK-candidate-v3-actual23.md) 原noJ通过全部576 stage guard，norm.04177307820740199仍高于原2e−9；全部112H、51内部下溢和9546负零保全。25的原十trial全在stage13/raw0/seg7被guard拒，不能绕到新H fullDN。原linearSteps还定义graphs/gains/far/scales，不能整体更换后冒仅换初猜。

原28全29数组、41全部868原步/3472field与3999文件已经完整字节审。41保72原出口和mean逐位同28，得到1372stage/1373node/307552行新系统。34、36、39、42、43方向失败均有实际note；LUinfo0、行列均衡或有限大条目不等于原系统准确、条件数或奇异性证明，不重同坏方向或将其派trial。

[actual43完整G结果](notes/2026-11-14-actual-request43-node-gauge-direction-failed.md)：原矩阵e929e642…，869形成块/503原块，全部307552行exact为7.0998783e21→3.2580670e21→3.7694419e21，保1；最坏new519=旧43/step11/Pi112，输入node520。实际longdouble64有效位不是binary128；真正LU RHS无下溢，辅助2^-2048 RHS从未送solve。没有独立大阵审计，不夸范围。

[R269](results/R269-native-zero-reference-height-slope-gauge.md)、[R271](results/R271-discrete-RK-stage-gauge-covariance.md) 与 [R272](results/R272-native-RK-reference-and-propagation-error-split.md) 已完整证明登记。实际四field w随级改变、两个中间field geometry同但状态及A不同；常w零参考不能直接判实际谱。R271改变原RK级坐标须保全部G_iG_j^-1和原port，连续变换重RK是另一个有限算法。

[actual47原捕获](notes/2026-11-14-actual-request47-original-step-capture.md) run43630351235，仅原旧43/step11四次RHS-J。四完整226state/geometry/root与41同，最终226state/224×224 shortJ/两mean行逐位同，复现差为零映射；四A现首次完整保存，旧41未保存A，不能冒其字节比较。全21数组与27小件已审。

[actual47精确作用及new519账](notes/2026-11-14-actual47-stage43-exact-action-and-new519-attribution.md)：固定同δ519/520/r/σ，old=observed平方1.1148576429598753e43；四A精确有理RK平方6.7408926442427e49。传播差平方与负交叉项强烈相消，因此“更准确形成这个块就使旧方向有效”没有成立。原43 exact oracle直接精确累加未预缩放J/r后除原σ，和此账一致。root17原exact输出包另核全部SHA；未本地重算norm/action。

**50完整参考已完成**：run43632067148/source d843fb1dcc8cb4b80e54956d98f8076a9c1398c5。[完整结论](notes/2026-11-14-actual50-complete-rational-RK-reference-and-covariant-comparison.md)给全部226×224 exact/RN、两个实际候选及三原方向。完整诱导∞误差old.015556918699475、direct-LD7.16812143047472e−6、R271-LD9.19526116149051e−6、RN3.36115669446251e−6；direct完整∞/F²优于R271，R271在特定旧43方向反而较小，不混指标。RN原σ下map差仍3.97095e21，这不是新stage residual。所有三prior action精确记录一致，21原输出完整SHA/CRC审计保范围；working实际64有效位非binary128。[候选完整原件](notes/2026-11-14-actual-request50-candidate-precision-and-bytes.md)另核49数组22767392B、全部x87填充和52处descriptor/原切片。输入只固定47原artifact，没有新RHS/J/ODE/native。

**54完成868新块和1372求解，原trial入口路径错而未执行**：run43634889730/source7eb383af1ca2bb04c7eaef9c65578dbc124269d8。[完整捕获](notes/2026-11-14-actual-request54-complete868-direct-LD-capture.md)保144array/1736chunks/868完整226×224 maps/3472原field及4221文件回执；[完整solver原读回](notes/2026-11-14-actual54-direct-LD1372-solver-and-exact-readback.md)保55输出/四轮全307552行及完整方向。新matrix76f30d775c0255dd127b08fa279e59fcaaa4a79a50b72bc7adc8231e436f6999；exact保iter2仍2.552304460257547558335607736e22，不能声称可用方向。原trial因root将旧28真实result.json误写成.gz触发FileNotFoundError，尚无任何十档试探或数学拒绝。

**55复用54，run待回读**：只修旧28一处路径，新54方向.gz保持。独立trial-only workflow完整固定取28/41/54+78公开源，直接实际完整方向的577限制跑原十alpha/noJ/全部guard/严格原σ norm下降；不增线性门、不重868capture/1372solve。详[原trial接口](notes/2026-11-14-direct-LD-original-ten-trial-interface.md)及[路径修复记录](notes/2026-11-14-actual54-completed-direction-and-original28-path-repair.md)。接受后仍须继续原native最终门；全拒后据实际证据选R273。52 spec运输失败和54 gzip修复已经完成保存，不再待办。

原step与G的十trial组件已完成：直接消费正确producer的保存方向，保原十alpha/完整evaluate(false)/原guard/原σ严格下降，首接受保全state后STOP。它们不重形成G/J，当前未派43坏方向，也不冒native完成。

[R273完整原σ块链平方根阻尼LS](results/R273-complete-native-damped-square-root-chain.md)已证明：保全部cut/stage/far、每nodeηI、carry与纯常数能量，不形成normal matrix；也给严格L2下降不推出原∞下降的精确反例。独立源码及接口已准备，尚未数值运行或选η；55直接读取实际54完整方向跑原trial，失败后按真实尺度选择显式阻尼。

### 1C. 真fullDN衔接与备选

取得本场H真实原生响应后，仍须原完整outer/inner、RMS1e−6、BC1e−11、native原容差和fresh audit全部过。非零跨进程缓存不能冒同live predictor。R257有限恒速平面Fourier只能为圆，重参数化需完整analytic lift及core响应；R259小核心共振/条件IFT备选接口已冻未调度，简单缩初猜不能消除设计核。

## 2. 同一接受场的闭合、固定g和全t精化

完整联解接受后保存全部physical/constant与本场真实尾，核core/球排除、完整材料cut角差/mean/九jet、唯一SE2与高度偏移，完成R249有限C²入口修补、上下尾及固定帽。新场已有z0，不加旧A mean。有限φ一般有无限θ谱，有限DFT同值不能冒连续接缝为零；R239仍需实际分支/turning number/全jet。

共享quintic B、严格closed wrapper/new loader/cover/held接口已冻；原A.height/w/E定义的目标g不覆写为B′。renderer差、finiteGauss真导与返回ap/app、角投影、径向残差按R260分账，不凭非恒等自行宣布超限。

定型后冻结全部scalar p*、g、尾帽、区间/参数/t范围，释放全core为K=k=0、T=M，同g v4维450/514。沿同一live TailClient/predictor依次新H/J→原FD→fullmain→fresh audit。699二分需1397，不能用max1200。README只要求等距误差精化到机器或原solver容差，不增六/九jet机器门；全t族本身仍须强C²。

## 3. 全t嵌入、reach、固定区与整面幅度

R248归约依赖准确接缝前提；新场R241全部参数块/法锥须覆盖自交与double-normal瓶颈，marked整族不当刚体。D取完整闭F0直径；固定有内点H可取两固定帽且实算diamH。必须同时diamH≥.2D、**整面像**Hausdorff δhold≥.2D、全t reach≥.03D、含反射δE>0。材料点位移/core到core/core直径不能代替整面指标。held可独立于尚未完成的reach点对读取全部活动块与两帽盘见证，不增前置门。

R238/254/258刚性排除链须消费同场完整模式/shared节点/材料mean/真尾；R242角解析精确等距定理不自动适用于有限metric缺陷或仅C²极限。数值包络按实际严谨程度陈述，不暗换区间证明。

## 4. 全域operator与最终交付

R251四Loewner/完整Gram接口的16号解析fixture已通过，不重fixture；尚需真正新接受场的完整prefix/finiteGauss scalar/两尾帽/C²修补，全域相对metric operator≤1e−6。三分量数值不能直接改称operator界。

旧小幅A只有约.063D，其RK24/RK48、三mesh、2157568空间对及GW已封存，不继承到新场或重做。真正完成后提供数个各<5MB网格、固定g精化证据、全t完整几何与数值到严格存在的真实差距。完整证明直接results及索引；旧未推成果按HANDOFF重做，已恢复部分不重复。达到全部README条件并继续推进更强目标，才可收尾。
