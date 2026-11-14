# 当前未解决的问题

完成条件以本题 [README](README.md) 为准，执行、原件身份与规则同步见 [HANDOFF](HANDOFF.md)。仅公开 `Rogerhu12/math-research-public`，科学计算只本仓 Actions；每条结论即时 pull/check/push，子问题完成继续下一项，不能把阶段报告当完成。当前只有大幅开放前缀被接受，尚无符合全部标准的完整闭场。

完整逐次历史保存在 [截至request49的原open](open-checkpoint-through-request49-2026-11-14.md)、[截至34的检查点](open-checkpoint-through-request34-2026-11-14.md) 与各实际note；这里去除已完成请求的旧“待运行”措辞，不重跑旧结果。

## 1. 打通同一大核的完整物理边值问题

唯一接受起点为 M96/N1024 的 .99 大核开放前缀；其材料三分量误差5.77368e−7不是operator证书，G约.96000098、rho>.16385011989。后续 .996/.9975 的metric超限及 .997875失败已保存。现有 M112/T112/N2048、699节点、完整453状态与236036自由坐标，M96只作初猜，原scalar/3控制、112材料H及全部physical/constant行保持。

真T112零锚、完整338×112 J、577×224原状态及audit已实际付费完成。只有七件身份相同且exact零H首请求可复用，新H与最终audit仍用真worker；不将微小H归零，不拿T96代T112。当前全部warm明确未解完整BVP，仿射零锚FD不冒新H原生响应。

### 1A. 前缀：按真实非线性证据推进完整模型

原完整原子模型、λ270/LSMR200、C-Hildreth200、512工作行/dual200、17档alpha、原node/mid/两RMS、rho/merit门保持。完整H候选600s、原trial预留90s、恢复30s、总1200s；每轮真实刷新W，禁止跨轮merit相减。线性角约束只管方向，不能替代原非线性检查。

[R270完整局部凝聚](results/R270-exact-local-support-damped-QP-condensation.md)保全部236036维原g、pure-global仿射列、109freecore与所有外部physical条件响应。平方根消元不以近似center替g；局部可行修复后恢复完整原H。原C4059维只作同模型比较，不限制完整H的外部自由度。原完整QR factor在RAM而未导出，不冒完整因子文件独审。

已完成的逐次原因和全部原件，见[45](notes/2026-11-14-actual-request45-condensed-QP-and-midpoint482-limit.md)、[48](notes/2026-11-14-actual-request48-thirteen-query-and-left-RMS482-limit.md)、[49](notes/2026-11-14-actual-request49-fourteen-query-and-left-RMS469-limit.md)、[53](notes/2026-11-14-actual-request53-working512-and-midpoint481-limit.md)、[56](notes/2026-11-14-actual-request56-left468-and-collocation-location.md)、[58](notes/2026-11-14-actual-request58-quarter-step-existing-domain-limit.md)、[60](notes/2026-11-14-actual-request60-left-RMS467-limits-seventeen-query-continuation.md)。这些科学计算和已完成byte核不重跑。60最近1/32试探只有left467失败，故62仅加该查询；58最近试探已含被建模点失败，故60采用同源重新线性化，不能从较远试探盲加查询。

**此前实际62已完成并正式保存**：[完整结论](notes/2026-11-14-actual-request62-quarter-step-and-modeled-nonlinear-domain-limit.md)。原run43642866864/sourcecc813fa7521098fdeba86b8bf8c0fe7d8c96bba0/job132594102992；原artifact14132473712/492837872B/ZIP220ad8c51a147942b663cd9196f009ecc976d1ff270b0348e494e08cf5e90730。Actions只读run43645082618实际完成原包CRC/SHA与全部导出字节检查，不重复数学。

| 同一62模型的原读数 | 实际结果 |
| --- | --- |
| 原alpha | 1/4接受；只执行3个原trial |
| 固定W merit | 43.91772416957067 → 43.80252837065667 |
| 实际下降/预测比 | .11519579891400156 / .8917561974918092 |
| 最大physical col / BC | .007109265719764634 / 3.316280272939375e−8 |
| 原新warm FD最大误差 | 7.060463202147657e−10 |
| 原domain与RMS | 全18网格/node/mid及两698RMS合法 |
| 本场native / 完整BVP | 仍未接受；FD仍仅真零锚仿射响应 |

最近被拒alpha1/2的原mid失败为473/480/484；被模型覆盖的left467、left481、mid473本身也分别实际β²负（−.48061380876825943/−.03707108422934646/−.1048827240301029）。两未覆盖mid480/484是原观察，但不能归因为唯一缺query。这一步无完整finite merit/RMS验收，不能冒称其merit下降。全18线性预测虽合法，却不保证该有限步实际非线性合法。

62的完整H同模型objective43.64341286514907优于C43.917035679229286；最终全36864线性slack合法，global radial .9999999999880521。literal512停止不等于已证明优化误差大；浮点stationarity6.6108862087657996e−6/rawgap1.2079226507921703e−13不称认证最优，不据此盲抬预算。

**63的原输入：同18自身schema重新线性化一次，实际已完成**。精确新parent为 `notes/public-actions-43642866864-1-condensedqp/eighteen-condensed-warm/`：
- warm-001.json.gz，4792420B，SHA dffaa532026e07357d5115089d968c1be4472c44d9a5f5da25ebcb3e2291ac73。
- 原driver-status.json，1466059B，SHA4f8239522cef511aca6721ddc9c4541cc9d4e65db3e7260d277b090ad226c054；公开gzip185444B，透明解出原字节，禁止解析后重序列化来冒原身份。

四18源码ec43c049/b9f7d915/5885daec/6ad75ce4不改；36864行、B支持467..483+p5749，C4059保全部outside offset467/468/469/470/483。63只改实际parent、own18 schema及记录，不增query/支持/科学门；完整H/原λ/全部预算/17trial/新warm真实FD不变。共享workflow fccbce17和request9b38956b的完整差异已读；实际运行身份取得后记H。

完成的原byte范围为163domainNPZ/1052NPY、93condensedNPZ/38全阵/42refs、14raw276059680B、53source SHA、全部midpoint描述与父/新FDproducer绑定。详细622406B审计artifact-only，small总结89402B/07671a9b；142157B trials不是小文本，不再经connector整读或拆片。完整factor/wholecolraw未导出，明确保留此范围。

最大col仍interval461/radial1/component1/row155819，原W199.06443073038736非零，完整W SHA3427705ab17ebdb900dc2eb2b3e7f94e4ec39bd6b3e750a9e35fbef6765089db。该行在B支持外但保留于完整目标和H外部条件响应，不能解释为遗漏/零权重。[58原保存b与Az](notes/2026-11-14-actual58-stored-final-direction-at-largest-collocation-row.md)只给原读数与精确代数预测，不本地重算矩阵动作，也不冒唯一λ原因。

**最新实际63与下一64**：[正式结论](notes/2026-11-14-actual-request63-nearest-midpoint480.md)。run43646179305/source db6d728f30ee2d0c9ea62c96c622d8d85d2354b2/job132604404966，原warm/FD/上传/发布全部success。完整artifact14134662698/494657224B/ZIPc90869cdcc317eef9b23a8a17755a7679ea5ce6dc41c2c143216524b481c6653已实际下载核size/SHA/CRC；[原8trial及新父读数](notes/2026-11-14-actual63-original-readout.json)不重数学。接受alpha1/128，同一W merit43.794243580548255→43.79041968996707、下降.0038238905811880386、实/预测比1.010083304813205；col.0071092556155250685/BC3.2903722327075875e−8，全18/node/mid/两698RMS合法，FD7.094809478749229e−10通过原5e−5。仍未解本场native/完整BVP。

最近1/64，原18查询和nodes均合法，仅已观测mid480原RHS非finite，β²最小−.011295551381192093/angle162/4负角；其后完整RMS未执行，亦无完整finite merit，不能冒称其全域都好或merit下降。**64只新增mid480完整2048角**，不由更远试探盲增485/486。mid480两端已在现支持内，B467..483+p5749、原C4059/全部outside offset保持；λ270/512/所有预算与原门保持。

64真正parent目录为 notes/public-actions-43646179305-1-condensedqp/eighteen-condensed-warm/：warm4799943B/SHA6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a，原status1810333B/SHA8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46，publicgzip231286B，透明解压原字节。四19独立源码94511479/63ec6bd0/6b497dde/7fee2874及[完整接口](notes/2026-11-14-nineteen-query-condensed-interface.md)已冻结；38912行，MID=(473,475,477,480,481,482)，插入后的旧mid481/482按typed query重新索引。原18不改。64 workflowe30102a1/requestdb723721绑定31源和真正63父对，随本提交触发；实际run43648987661/source d625bb293e07541b4bf717524e14a45392be03aa/job132613023557，原warm/新FD/upload/publisher全部success。完整artifact14134942742/510988971B/ZIP0aa58b074c86abce6db146dea32d7d28664b290dc1bc7e2cd5e132ce479de478；原alpha/nearest待读，不由文件名猜。63原完整H objective43.54719205984342优C43.79357494676784，final36864slack正、globalradial.9999999999684314；浮点KKT不称认证。最大col仍461/radial1/row155819，W199.05455376436257非零，不漏行、不归因唯一λ。新完整byte reader e3810833在run43647823666完成；[完整原件读取范围](notes/2026-11-14-actual63-complete-original-byte-readback.md)记录163domain/1052NPY、93condensed/38arrays/42refs、14raw276059680B和53sourceSHA全部通过。summary46059B/b138fdaa已公开，详细630140B账只artifact；完整factor未导出，不能冒独立因子文件审。后续数值工作未等待这项读取形成额外门。

[actual63最大col原保存响应](notes/2026-11-14-actual63-stored-row155819-response.md)：原b=-1.4151317154400291，完整条件恢复Az=.00025747182097217506，最终选择Az=.0002574718209640469。该小响应在selector之前已存在；full center从未导出，尚不能区分中心本小或条件校正相消。下一独立Actions诊断固定63父62、原完整A/Wr/S/g/λ270与factor SHA，分中心/局部力/RHS舍入/恢复/selector；不重新优化、不增科学门。

**65固定63模型诊断已接线**：[完整接口](notes/2026-11-14-actual63-fixed-model-response-decomposition-interface.md)与57KB独立源10aeaa14，workflowa5ce807b/request36596d2e/51pins。只从实际63 ZIP及其父62原state重建一次原完整A/Wr/S/b/g/λ270和QR，分中心/原局部力/精确RHS加法/重放/selector；row155819及interval461全338行保完整作用。完整原数学数组逐SHA绑定，factor摘要差异如实报告、未导出旧因子不冒审。无新QP/LSMR/native/trial/参数扫描或新科学门。fetch令牌与科学analyze分开，全部新大件large-arrays。

**实际64正式结论**：[完整原回执](notes/2026-11-14-actual-request64-nineteen-query-nearest-midpoint485.md)、[原数值读回](notes/2026-11-14-actual64-original-readout.json)、[15原文件/11身份事实](notes/2026-11-14-actual64-primary-identity-readback.json)已保存。原6trial接受1/32：same-W merit43.79040176025459→43.78409880606567，col.00710921522417158/BC3.1875470774840915e−8，双698RMS均有效，新FD7.082003137747323e−10。最近1/16全19/node合法，唯原mid485 β²−.009685047003464398、RMS未执行；更远1/8 node/mid全合法却真实目标增加.0072998566163775536、RMS也未执行。不得把全部限制归一query或宣称域/目标沿方向单调。

66从真实64 newpair 3b25ea84/037fb9ee继续，只增mid485全角成20query/40960行；完整B支持必须由467..483+p5749显式扩为连续467..486+p6763，含布局零列484，C4059及所有outside offset保留。原预算/λ270/512/17trial/FD不变；四新独立源在做。完整factor原未导出；64 byte读回43649956424已job success，详细范围另读，不成66新门。65独立fixed63诊断初次run43650386882/source949d7056在任何evaluate/J/QR前因一个SHA漏字符停止；[真实失败与一字节修复](notes/2026-11-14-actual65-input-digest-typo-and-exact-retry.md)保全。新source5033b886仅补该字符，12个原FILE_PINS全部纯字节核同；revision2立即重调，科学/预算/模型不变。

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

[59完整原试探/状态审计](notes/2026-11-14-actual59-original576-first-native-step-and-state-audit.md)已通过：34件/26清单、实际input及全部r/cut/far、原源码精确逆还原、selected checkpoint/raw全部逐字核同；118878 changed words分布在全部577节点，31零含8负零。原argmax witness operands逐字核实，不本地重算norm/候选/最大值；QR因子审计单列。

[59原576完整QR与同矩阵双exact账](notes/2026-11-14-actual59-original576-QR-and-two-exact-readbacks.md)正式保存：1183文件/1170阵/全部577因子常数464891392B及两份129248行整数账、完整原28输入/J与57五件全byte审PASS；不在本地再算残差。新方向9.686175843…e−11与旧57限制.041773078…仅在同原576目标比较，不能转移1372的小缺陷；原formed gradient24888563.660…仍大，完整保留且不增gate/认证。

原step与G的十trial组件已完成：直接消费正确producer的保存方向，保原十alpha/完整evaluate(false)/原guard/原σ严格下降，首接受保全state后STOP。它们不重形成G/J，当前未派43坏方向，也不冒native完成。

[R273完整原σ块链平方根阻尼LS](results/R273-complete-native-damped-square-root-chain.md)已证明：保全部cut/stage/far、每nodeηI、carry与纯常数能量，不形成normal matrix；也给严格L2下降不推出原∞下降的精确反例。独立完整源码与接口已保存，root已全文读；57实际线性与原试探已完成，范围分开记录。55已全拒，57首次取原σ坐标的[eta=1](notes/2026-11-14-native-damped-eta-one-trial-contract.md)，保持全部cut/far/模式与原试探；不把L2模型下降当原∞下降。

[当前原576迭代接R273的源码可行性](notes/2026-11-14-current-native576-R273-synchronous-interface-feasibility.md)已明确：可只接原with-J/tol后的cor调用，使用本次完整ev/J/r/cut/far/σ，原十trial/fresh audit不变；动态QR类可用但当前1372 main/context身份不可改标签。59首步接受后已选同步桥作61续接，独立当前snapshot/完整原native循环正在实现。

61完整执行源已保存：[当前576快照与QR合同](notes/2026-11-14-current576-fresh-snapshot-and-damped-QR-interface.md)、[实际59 selected到完整原native](notes/2026-11-14-current576-selected59-full-native-R273-interface.md)。四源码695c2a56/ac04842b/06b8c44c/0933ee81与断线前AST/Node核同；只换唯一非线性correction、每轮真withJ全576、全577罚块/常数、原十noJ/容差/最终J及fresh audit保。minA/D只保原bits不增finite门；无旧28缓存/softcut投影。完整逐轮大件由本仓Actions保，32GiB为资源预算不改科学门。61实际run43645948199/sourcecf6b51193255dfc713610d2919598451ccdd49e2/job132603626663已过14源/13父件/AST/Node/容量/原78源码恢复，进入完整原solve，尚无原生结果。终端失联后依根Rule8仅以<100KB小文本发布；规则runner3b8b6dd5已于22:02:58实际pull/readc383317e并推H、45分钟续查，令牌不进connector。62只读reader03a78684已在run43645082618完成原读数与完整exported byte审，不重跑原数学。

### 1C. 真fullDN衔接与备选

取得本场H真实原生响应后，仍须原完整outer/inner、RMS1e−6、BC1e−11、native原容差和fresh audit全部过。非零跨进程缓存不能冒同live predictor。R257有限恒速平面Fourier只能为圆，重参数化需完整analytic lift及core响应；R259小核心共振/条件IFT备选接口已冻未调度，简单缩初猜不能消除设计核。

已冻结[同live多请求合同](notes/2026-11-14-current576-live-client-multirequest-extension-contract.md)和[逐请求snapshot/QR合同](notes/2026-11-14-live-current576-per-request-adapter-interface.md)：clientc9f33777/hook7e83b398/adapter9346c0a7/QRee174e82，四独立源码不改61。实际completed61的literal JSON状态只作初猜（不声称序列化前负零可见），bootstrap真求解后同一原worker继续当前H/J、原FD、完整fullDN与fresh audit。每call当前H/target/sigma全绑定、全部原32轮/十trial/容差和因子保；不把32GiB单call预算冒总fullDN预算。现仅源码/AST/Node及可逆字符串变换通过；新薄[实际H/原FD/完整fullDN入口](notes/2026-11-14-live-current576-actual-H-FD-full-DN-interface.md)7ba3fd5f与workflowea98af37已冻结发表，待实际61八件父包及真实SHA后直接提交具体request；本提交未伪造未来父或触发该未具输入的科学入口。

19专用[只读原件接口](notes/2026-11-14-completed-nineteen-prefix-readback-interface.md)及readerc963f6a9已保存，typed查询明示mid480索引16/481与482为17/18，不沿旧flat行号；实际64已全部完成；共享workflowa7a55c89的prefix19请求已绑定真实artifact/父63/source d625bb29，先保原结果后完整byte，读取不成后续新科学门。

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
