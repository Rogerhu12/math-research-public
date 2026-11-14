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

**前一父actual56完成**：run43636630003/source b8a19c16fc1363ffa1a66f39b9403e0dfa93e169；[完整实际结论](notes/2026-11-14-actual-request56-left468-and-collocation-location.md)。16query/32768行/B5073，512工作行末slack−7.66609e−14，最终全slack非负，完整原H恢复relative1.0766691e−15；浮点KKT/rawgap非认证。

实际alpha1/32接受，本轮merit44.10538196200878→44.084143195501056，col.007109940451957601/BC5.989189850450424e−8/FD6.957649122839063e−10。最近1/16及1/8/1/4全部16真实网格、nodes/mids合法且merit降，仅原left-RMS468拒；最近β²−.009420476255991517/phi0。不能凭literal max512再抬预算。

新observer实际定位最大col为interval461/radial m1/component1/row155819，原W199.0763850424081非零。B支持外仍有完整H外部条件响应/原方程，不能解释为遗漏/零权重或改方程。17原evaluate/1weights/0error；尾六为原有方向差分。全colraw未导出，不冒独立原阵审。

145domain936NPY/88凝聚38全向量/17colJSON/46源/父53与FD链、14raw217496448B全byte核，三个audit已推。当前父warm5a5b9620cec8c48e6ca60d71b2a9db28d00b7112f04bde1fa7d6d4c7245cc5ae；原status e644ee2adf52f8b7684c2f4360672e627f2a19135aa889cb6df4afb898b1247b，1350695B/publicgzip169659B，须透明解压核SHA。原零锚FD仍非新H native。

**58已完成：run43638348140/source ba8bc4f4acd547fd5219826da4f6e35f859bca56/job132580074075**：仅加left-RMS468全2048角→34816，B完整468..483+p/5411；C4059保外部468/469/470/483 offset。保512/dual200/600s/1200s/λ270/全部原门+新FD/只读colobserver，四新seventeen源冻结接线。[actual53](notes/2026-11-14-actual-request53-working512-and-midpoint481-limit.md)、51及更早完整存证不重跑。

**最新58/下一60**：实际alpha1/4接受，本轮固定merit44.08450062286488→43.925384505081816，col.00710961172228531/BC4.4918924725999154e−8/FD7.108999873259166e−10。最近1/2失败的mid473/475/481均已建模，不能据较远alpha1的mid480盲加第18查询。60已运行43640358327/source da346d172715761d7da23da84c92d97a92b438de，从58 warm3911b642…/原status64140c9f…（1276068B，gzip163444B）沿17 own-schema重线性化单个完整模型，保原λ/512/全部门。[最新58全文](notes/2026-11-14-actual-request58-quarter-step-existing-domain-limit.md)及prefix/observer/root14raw三审计已保存；完整新父SHA见H。

[58最大col行的原保存方向](notes/2026-11-14-actual58-stored-final-direction-at-largest-collocation-row.md)：原row155819 b=-1.4154122374775011，最终完整H的已保存Az=.00026246452261009833，原W=199.07511842631416非零。完整模型本身对此行修正很小，不是漏行/零权重；已给对应精确代数预测式，不本地重算矩阵动作/贡献，也不凭此认定唯一λ原因或盲改模型。

### 1B. Native：先分清保存矩阵、传播与求解误差

[23完整seed](notes/2026-11-14-public-same-RK-candidate-v3-actual23.md) 原noJ通过全部576 stage guard，norm.04177307820740199仍高于原2e−9；全部112H、51内部下溢和9546负零保全。25的原十trial全在stage13/raw0/seg7被guard拒，不能绕到新H fullDN。原linearSteps还定义graphs/gains/far/scales，不能整体更换后冒仅换初猜。

原28全29数组、41全部868原步/3472field与3999文件已经完整字节审。41保72原出口和mean逐位同28，得到1372stage/1373node/307552行新系统。34、36、39、42、43方向失败均有实际note；LUinfo0、行列均衡或有限大条目不等于原系统准确、条件数或奇异性证明，不重同坏方向或将其派trial。

[actual43完整G结果](notes/2026-11-14-actual-request43-node-gauge-direction-failed.md)：原矩阵e929e642…，869形成块/503原块，全部307552行exact为7.0998783e21→3.2580670e21→3.7694419e21，保1；最坏new519=旧43/step11/Pi112，输入node520。实际longdouble64有效位不是binary128；真正LU RHS无下溢，辅助2^-2048 RHS从未送solve。没有独立大阵审计，不夸范围。

[R269](results/R269-native-zero-reference-height-slope-gauge.md)、[R271](results/R271-discrete-RK-stage-gauge-covariance.md) 与 [R272](results/R272-native-RK-reference-and-propagation-error-split.md) 已完整证明登记。实际四field w随级改变、两个中间field geometry同但状态及A不同；常w零参考不能直接判实际谱。R271改变原RK级坐标须保全部G_iG_j^-1和原port，连续变换重RK是另一个有限算法。

[actual47原捕获](notes/2026-11-14-actual-request47-original-step-capture.md) run43630351235，仅原旧43/step11四次RHS-J。四完整226state/geometry/root与41同，最终226state/224×224 shortJ/两mean行逐位同，复现差为零映射；四A现首次完整保存，旧41未保存A，不能冒其字节比较。全21数组与27小件已审。

[actual47精确作用及new519账](notes/2026-11-14-actual47-stage43-exact-action-and-new519-attribution.md)：固定同δ519/520/r/σ，old=observed平方1.1148576429598753e43；四A精确有理RK平方6.7408926442427e49。传播差平方与负交叉项强烈相消，因此“更准确形成这个块就使旧方向有效”没有成立。原43 exact oracle直接精确累加未预缩放J/r后除原σ，和此账一致。root17原exact输出包另核全部SHA；未本地重算norm/action。

**50完整参考已完成**：run43632067148/source d843fb1dcc8cb4b80e54956d98f8076a9c1398c5。[完整结论](notes/2026-11-14-actual50-complete-rational-RK-reference-and-covariant-comparison.md)给全部226×224 exact/RN、两个实际候选及三原方向。完整诱导∞误差old.015556918699475、direct-LD7.16812143047472e−6、R271-LD9.19526116149051e−6、RN3.36115669446251e−6；direct完整∞/F²优于R271，R271在特定旧43方向反而较小，不混指标。RN原σ下map差仍3.97095e21，这不是新stage residual。所有三prior action精确记录一致，21原输出完整SHA/CRC审计保范围；working实际64有效位非binary128。[候选完整原件](notes/2026-11-14-actual-request50-candidate-precision-and-bytes.md)另核49数组22767392B、全部x87填充和52处descriptor/原切片。输入只固定47原artifact，没有新RHS/J/ODE/native。

**54完成868新块和1372求解，原trial入口路径错而未执行**：run43634889730/source7eb383af1ca2bb04c7eaef9c65578dbc124269d8。[完整捕获](notes/2026-11-14-actual-request54-complete868-direct-LD-capture.md)保144array/1736chunks/868完整226×224 maps/3472原field及4221文件回执；[完整solver原读回](notes/2026-11-14-actual54-direct-LD1372-solver-and-exact-readback.md)保55输出/四轮全307552行及完整方向。新matrix76f30d775c0255dd127b08fa279e59fcaaa4a79a50b72bc7adc8231e436f6999；exact保iter2仍2.552304460257547558335607736e22，不能声称可用方向。原trial因root将旧28真实result.json误写成.gz触发FileNotFoundError，尚无任何十档试探或数学拒绝。

**55已真实完成并全拒**：[完整原十试步结论与byte审计](notes/2026-11-14-actual55-original-ten-trial-rejection.md)，run43636504089/source6b7e9846ab9062614618856d4d6772c847a303c2。10个fresh noJ、0新baseline/J：九D/S/A拒、一个stage23内部momentum Newton失败；最小1/512仍stage28/raw0/seg5拒。没有完整trial norm或selected状态，不能宣称十个范数都不降。

**57实际完成，原十norm全同**：[完整原试探](notes/2026-11-14-actual57-original-ten-trial-no-decrease.md)与[完整QR/exact行账](notes/2026-11-14-actual57-damped-chain-QR-and-original-exact-readback.md)及两组独立byte审计已保存。R273 eta1在54新1372矩阵上全部307552行exact最大4.062019449255373658…e−9；1373因子/1106785792B/全部常数与行账已完整审。原十noJ均完整返回、0guard，却十个norm bits全同base .04177307820740199；selected=null/native=false。577δ非零，不可由norm相同推所有trial state/r不变或唯一原因。

**59已完成并接受首个完整步长**：[真实原结果与61续接决定](notes/2026-11-14-actual59-first-full-step-and-continuation.md)。alpha1使原norm .04177307820740199→.0001289424025918576；真实selected已保全，但仍高于原2e−9，最终J/audit未做。61正实现每轮真实新J/原576完整R273eta1及原完整native循环，不能在此收尾。已冻结的本轮接口：[原576方向合同](notes/2026-11-14-original576-damped-chain-and-actual57-comparison-interface.md)、[原十与完整观察](notes/2026-11-14-original576-damped-native-trial-and-readonly-residual-interface.md)、[57五件取入](notes/2026-11-14-actual57-selected-five-transport-interface.md)。用同actual28原576完整J/r/σ/H/cut/far直接R273 η1，独立target/schema及完整129248行exact；同时计算57实际577限制δ在该原576目标的完整exact，均不是trial gate。原十loop/guard/strictnorm和cached28单次保，新增只读真实trial全state及返回r/cut/end/max定位，无额外RHS/J，不重复57。只取28和57五件实际方向文件，不再取41/54大包。未来若接受仍需真实新状态继续完整native/fresh audit。

原step与G的十trial组件已完成：直接消费正确producer的保存方向，保原十alpha/完整evaluate(false)/原guard/原σ严格下降，首接受保全state后STOP。它们不重形成G/J，当前未派43坏方向，也不冒native完成。

[R273完整原σ块链平方根阻尼LS](results/R273-complete-native-damped-square-root-chain.md)已证明：保全部cut/stage/far、每nodeηI、carry与纯常数能量，不形成normal matrix；也给严格L2下降不推出原∞下降的精确反例。独立完整源码与接口已保存，root已全文读；57实际线性与原试探已完成，范围分开记录。55已全拒，57首次取原σ坐标的[eta=1](notes/2026-11-14-native-damped-eta-one-trial-contract.md)，保持全部cut/far/模式与原试探；不把L2模型下降当原∞下降。

[当前原576迭代接R273的源码可行性](notes/2026-11-14-current-native576-R273-synchronous-interface-feasibility.md)已明确：可只接原with-J/tol后的cor调用，使用本次完整ev/J/r/cut/far/σ，原十trial/fresh audit不变；动态QR类可用但当前1372 main/context身份不可改标签。59首步接受后已选同步桥作61续接，独立当前snapshot/完整原native循环正在实现。

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
