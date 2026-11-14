# 当前未解决的问题

完成条件以本题README为准，实时执行、源码/结果路径及规则同步见[HANDOFF](HANDOFF.md)。本轮用户已直接授权公开仓库及本仓Actions，旧发布等待已解除；只在Rogerhu12/math-research-public工作。下列是当前实际状态，早期长列表保存在[历史open](notes/2026-11-14-open-before-current-continuations.md)，不以旧排队或中断状态替代已产生的真实结果。

## 1. 从真实大核打通物理cut和完整闭合

.99自由93核的M96/N1024真BVP已有完整接受结果，材料C²两档三归一化分量误差5.77368e−7（非算子范数）、完整核G≈.96000098/rho>.16385011989。后续公开run43582043166真接受.996和.9975，但物理metric升至4.60534e−6/8.08662e−6，不能视为已达标前缀；.997875的真实Newton因病态化、回溯失败及网格上限未接受。保全两接受点和失败checkpoint，不仅提高网格上限继续原分支。

当前使用较好的.99初场，加完整AngleConnector/coast/finitebridge和3个内支scalar控制到原r=.3物理cut。690节点完整θ圆warm的节点/中点域通过，但后来真实RMS两Lobatto点失败，残差.00711也还不是解。全部96个材料H与全部core换角导数进入389维增广BVP；固定前3核，其他93核加3scalar配96条真非均值tail-DN边界。三步/Richardson FD已在run43584222071真实通过；原Newton/BC/正性门不改。首690节点inner真实reduced condition7.153e17、linear相对残差.57657，未接受任何更新；SciPy随后插值到878节点RMS NaN。R244证明圆段控制的连续设计核，已接独立prefix3支撑。run43585737152实际在RMS域预检就停止：696节点331坏点，1027节点846坏点，全在圆形warm段；未到新QR或tail。request06/run43587375529已真完成：M96两N各25/26坏，M112/128/160所查48点全过；纯增N不治。现选M112/T112/N2048原方程，原96场只作初猜，base_prefix_M96与field/tail112分开。request08/run43588155190的M112准备已真success：699节点全节点/中点/两RMS域过，完整453行FD Richardson9.51769e−10<原5e−5；初残差.007110595仍非解。新112真zero/fullJ亦已成功：1351.74s、resid0、完整338×112 J及577×224状态，strict源/config/cache全同；request10直接复用prepared/FD与此真锚进原真DN/QR；不复用96包，不做ready代理QR，不采用未完整实现的analytic lift。R247证明coast Hermite偏差中点恰消失而原RMS点有±sqrt(3/7)/7系数；只说明域预检结构盲点，collocation残差仍非零。

request10/run43590496434真失败：首线性残差/RHS=.913332499，方向max9658；17次回溯未到finite merit、零接受更新。request11/run43592195185完整带LU info0/内存与原地分解均过，残差比例降至3.27382357e−4但方向仍5832.77；校正变差未采用，最小原α=2^-16仍52坏node/122mid/112右BC，全17trial无接受步，随后966点invalid。不能以小normwise backward2.13e−18冒准确方向，也不能只归为3控制核。request12/run43593855655已真完成方向诊断：实际P cond1.14478e17且均衡不治，真方向全θ L2=4942而保留112仅7.10；到2^-40仍1坏mid，无合法Taylor。request13/run43594985550已真失败并由e61dbf4保全30件限额内输出：真T112全J的R252非零高度FD9.65016e−10通过；新右块cond621945/均衡2956.89，同旧Uend方块119589.8，切口改善不代全局稳定。完整带LU info0，保留一次校正后原相对残差8.22590e−7/方向352.439；17trial全非finite，最小alpha仍78坏node/124mid；966插值19坏mid，零接受步、新H请求0。request15/coupling112bridge检末bridge实际传播/径向分辨率，保699旧点、新点用同p=0解析圆与完整均值，绝不插值失败场或只抬max_nodes。圆参照强非正规尺度只是选网格依据，须与实际L/R对照；原新Rφ/真尾/全部非线性门保留。另据同一旧Uend上新右块条件1.20e5，request14/run43596465579已实际失败：新小块cond1.20e5复现，但全QR回代相对残差.06731/方向352.418，原回溯无接受、966invalid、新H0；与band方向接近，不能全归band误差。request15/run43596755251也已实际失败：699旧点保留并加374至1073，原域/真J FD通过；完整带LU相对残差2.93648e−6、方向1014.925，17trial全坏，最后399坏node/496mid，status1/RMS2.12563、新H0。实际有限Jac在a二阶量为零的峰值cell仍有谱半径1.61e5；末cell拆60段宏传播范数约2.22e23，不能据理想circle公式继续盲加bridge点或只抬1200。详见[末bridge实际失败](notes/2026-11-14-actual-bridge-resolution-failure.md)。request17/coupling112trust实际run43598917532已失败：3次合法warm下降及真FD9.5171e−10通过，但原col只到.0071105473；首次真非零H约4.176e−17在native iteration0 norm1.3414e7/chartCond1.3312e60，10trial全guard拒。尚未进入prefix inner/newband，无成功新H/J、无完整接受。全部artifact已补出版，见[真实warm与极小高度尾失败](notes/2026-11-14-actual-trust-warm-and-tiny-height-native-failure.md)。下一步分别处理turn内RMS可行方向与native冷启动，不阈值归零H、不原样重跑。request18/run43602070499已完成：λ270在80步istop2（上限200），仍同473/phi0的RMS域限制，仅α2^-16通过，原col=.007110547287、新FD9.00098e−10，无native。详见[实际18与域方向决策](notes/2026-11-14-actual-request18-converged-linear-direction-domain-limit.md)。下一从新warm作完整域梯度验证及一个投影正阻尼模型，原三源和最终接受门不变。R262已完整证明该梯度、exact chart链与λP投影伴随/下降恒等式，独立接口与一模型warm/FD已全文读并接request20/trustprotected；实际run43603477207/job132473033066已完成，单点保护使原全域有效α从2^-16增为2^-10；同模型merit降.00104611，原col仍.007110545981，未接受。新warm SHA0036063f…/新FD9.07968e−10、native0；预条件normal2.61e−5不等于未预条件KKT344.921。下一从此warm保(473,0)/(480,0)/(473,11)三条实际已见查询，一模型λ270/200，全部原域不省；request22/trustmultiline已接推送请求。见[实际20](notes/2026-11-14-actual-request20-protected-query-and-next-domain-rows.md)。request22/trustmultiline现已真完成：三行rank3，α2^-9/真实merit降.00208987，新warm03ca9477…/新FD8.1733e−10；原col=.00711054337仍非解。受保护三点自身均合法，480剩余角最小值移动，2^-6有五处左RMS，≥2^-4另有mid坏点；不只加第四点，request24/angledomain锁同base20+22真方向检查五处整N2048角β/Dβ及已试步余量，源已全文读并接推送，原门保持。详见[实际22三行](notes/2026-11-14-actual-request22-multiline-tangent-and-angular-domain-limit.md)。request19/run43602823170已真完成原无J576stage：保存初值129248项严格数值相等，全部guard过，最坏stage11/raw0/seg7/Pi104归一1.3414e7，而cut/far全112行0。见[实际cold回执](notes/2026-11-14-actual-cold-tail-no-J-stage-replay.md)。下一同原RK12零态线性stage构造私有初猜，保原far/graphs/gains/scales，request21/zerorkprobe真run43603818345在stage12/index92的工厂det检查失败，evaluate_calls=0，旧合并分支未区分有限0/非finite，不能冒新native残差；见[实际21](notes/2026-11-14-public-same-RK-candidate-probe-actual21.md)。独立v2逐块留T/ad/bc/det后，只放行不被私有图公式相除的有限rounded det0；零u/非finite/下溢和全部原native门保持，request22/zerorkprobev2真工厂已成功，实际41个有限det0留证；预测261→262第112模Q=−5e−324/u275.882…→0被新增underflow veto拒，evaluate0，仍无native结果。原native初猜本允许普通下溢；独立v3只记录并允许实际深处乘除舍入零，保cut全部H和原native门，完整候选才原noJ；request23/zerorkprobev3现已真成功：完整577×224候选原noJ一次通过576stage guard，norm降至.0417730782074仍大于原2e−9；51真实内部下溢和所有符号零/原尺度完整保全，没有solve/J/audit接受。详见[实际23](notes/2026-11-14-public-same-RK-candidate-v3-actual23.md)。下一独立入口把此完整候选只注入同17 H首次原initial，进入原完整solve/J/fresh audit，所有原门不改。R264完整损失账已证，不重跑19。从原699合法warm做精确入口/常数约束的正阻尼LSMR，保全部physical collocation/112 Rφ、真实非线性midpoint与方向一致merit；任何下降只算warm，随后仍交原完整fullDN/原RMS/BC/真尾/audit，不重跑同699QR。详见 [实际物理角失败与末bridge续接](notes/2026-11-14-actual-physical-test-failure-and-bridge-resolution.md)。

R257已证明uniform材料圆的有限物理Jac具有理想块结构，同时证明非圆原core的严格单位速入口不能纯有限θ表示。换θ是有因备用，必须另付入口投影误差或完整解析lift、显式core响应及全部读出/证书成本；不能把旧phi曲线改名后令rho=1。当前request17主线不因这个参考定理自动切换。

R259已给备用直线缩幅的实际源圆/原有限collocation、完整112尾J与高块Schur必要条件，以及去退化后的条件IFT；简单缩小初猜不自动消除圆点scalar设计核。λ、λ²、λ³路径不是同一个首阶条件，均未有实际新解；当前request17继续，备用诊断源已冻结（[接口](notes/2026-11-14-small-core-resonance-diagnostic-interface.md)），尚未调度。

原T96/N1024零锚和独立J审计已付，不重算。当前T112自己的真锚、完整338×112 J及所有状态同样已付；J-second相对差1.52402e−12、ready与真J差.035157884保留。request10严格复用真零响应一次，整个anchor/J逐结构同原包；worker已启动但新request为0，故这次不是非零尾失败。同配置/数学源/精确零H首请求可继续严格复用；任何新H与最终audit仍真worker，不以零残差或ready参考冒导数精化。

实际联解接受后，立即完成以下相互依赖的内容：保存完整physical/constant状态与真实H尾；原core证书和球排除；真正cut的完整材料角谱；同一SE2及高度偏移下的六jet；明确有限C²修补对metric的影响；完整上下尾和固定帽组装。新场已经含物理z0，不加旧A mean。原背景表尚不定义连续primitive，现已给同场全部表节点的精确共享quintic背景及完整表示误差账（[说明](notes/2026-11-14-shared-background-and-representation-budget.md)）。保原帽高、同一g，完整cut Δ须重建；独立wrapper及严格新loader已冻结（[接口](notes/2026-11-14-shared-background-closed-wrapper-interface.md)），真正使用B的三导数并重建全部cut角差；旧loader拒绝新包，cover/held独立薄入口已接新loader且保原完整空间/全像公式（[接口](notes/2026-11-14-shared-background-cover-held-interfaces.md)）。原metric表不得覆写为B′，数值未执行。原φ96通常含无限θ谱，不能只投影96项便称连续接缝为零。R239是连续充分条件，仍须核其实际分支、turning number和全部高度jet输入。

R263已完整证明预条件normal=C^-1r与受限KKT r的区别、λ²强凸后验方向/模型gap界及下降比例充分条件。实际20小的zᵀr不代全r；需要改进同一模型精度时可据此调LSMR停止精度，不只增maxiter，不把它加成原BVP门或打断22三行实验。

## 2. 定型后冻结同一材料g精化

R240证明共同材料θ下g=ds²+a(s)²dθ²独立于核心c。第一次设计可调scalar；真正精化须冻结全部a(s;p*)、尾帽g、区间、参数及t范围，释放全部核心，取K0/k0/T=M，然后升频率、径向网格及积分精度。不能将不同scalar设计或不同t区间混为收敛序列。独立v4的prepare/response/full_dn与完整物理读出/尾包/闭面消费者均已准备，严格绑定首v3全部p*及同一canonical scalar SHA，尚无实际v4解。 新Rφ v4三包装已按新身份重建：同一个真实live TailClient完成新H/J、原FD和原fullmain，保predictor、最终fresh audit及原门，实际live scalar sidecar与完整cut单独绑定；尚无真实parent可启动。见[same-g live-client接口](notes/2026-11-14-same-g-physical-DN-live-client-interface.md)。README要求等距误差随精化到机器或原求解容差，并要求每个有限场及t族C²；六jet用于曲率/reach可靠性，不新增六jet全体机器收敛门。帽中心使用固定图册，非线性角变换不得硬延到中心。

旧A基准的真RK24/RK48非线性solve/J/audit、RK48真16+源节点读出、两共同网格、finitecollar和三闭mesh已经全部完成并发布，不继续列为ENOSPC中断，也不重复求解。24→48同f8二jet差7.03e−6，RK48 f8→16差.0029138，未机器稳定；原prefixcut metric平台4.77033e−8仍未重解。接缝外metric随精化下降至2.07608e−9，但不能替整闭同g频率精化。旧finitecollar全域界1.00139e−18只适用自己的H和背景。

旧post43 GW完整结果已逐SHA恢复为历史材料：不同有限GW场的f8→16二jet仍差.0017739032174，未C²稳定。R245给完整Hermite恒等式；公开run43586618658已真重现二jet差.0017739032174，有理shadow同值、消费端误差仅1e−17。Q层差反升.00204906，metric样本也变差，不扩全场替换。request07已真完成三节点，request09/run43588929803又按原49 RK步重放六已有节点；旧A/B/C字节/mean/g全同。96×1024局部metric f8→16→48从1.18359e−8降到1.25944e−9再到1.62003e−10，κmax同7.6462465。局部读出敏感已定位；封存该旧A分支，不追任务外机器六jet门，不扩全场GW/Q。新大幅field仍须自己的实际尾与同g非线性精化。

## 3. 全t嵌入、reach、固定区和真实像幅度

R248已给有限C²的全相位强连续及metric/operator/κ上确界恒等，前提是完整准确两阶接缝。R249已完成共享节点入口parity规范形及完整连续修补成本证明，只改首单元且保留整个cut九jet/mean/H；其真实metric/κ代价仍须消费新的实际接受场。独立full_state_continuous_cover已绑定同一规范形、完整实际位置/法向和记录的唯一SE2，R241空间门不变；包络仍显式条件，不继承旧A数值。未标记整面的reach/D可用一次完整空间证据，固定marker须统一R24或R11混合点对门，不能把marked整族当刚体。

D必须用完整闭F0；δhold是表面像的Hausdorff距离，不能用材料点位移。H可用两个固定帽的并集，须实算直径且含内点。旧A的实际点云δhold/D≈.0630146，明确不满足.2；它只提供已完成工具基准。新full_state_held_hausdorff已补实际position packet/完整闭包路径及全部身份绑定，沿用全活动块+两完整帽盘和原.2门，未运行新数值；它可独立于reach尚余点对的状态读幅度见证。

R241完整参数块条件同时排除自交及double-normal瓶颈。旧A的v2真实D+=3.980751407764145、Ktau=.9994116104；曲率/标记及prefix-tail/cap/self已付，只剩33712个prefix-prefix对。v3真消除31764/33712原余对，剩1948仍仅prefix-prefix；完整活动位置cover已导出。真实held消费者使用全部活动块及完整帽盘，得δhold/D+≥.05388898465、H/D+≥.996873，正像变但不达本题幅度。run43585361227/q4后余328父对；run43586618658/q8已付全部33712父对/2157568子对，uncovered=0，完整条件空间预算通过。旧A可选加密停止，不实施径向方案。覆盖假设和数值证据的严格程度照实际记录，不能暗换成已证明全域区间界。新候选必须用自己的数据重跑相关消费者。

R254已给完整物理共享节点Hermite前缀的逐cell精确有理四点证明和完备6×(4M+3)网格消费者；当前没有新接受场实际回执。必须绑定R249实际nodal SHA、完整z0和全部模式，不能移植旧尾或据prefix单独宣称δE。R238通过平面局部胚识别四个不同支持圆和仿射独立圆心，排除含反射全等；A实际前缀2589片和标记代数已过，完整tail/collar输入仍待同场消费者。R242对精确度量且角解析的活动环带给结构性排平面开片定理；有限metric缺陷或只有C²收敛的极限不能自动套用。原RK48四角共享node精确C²规范形已由公开Actions逐段全有理验证9246小段，完整定理/实例见R243；与旧rounding表示及整个接缝的差异仍要支付，不能宣布整个δE已证。

R258已把同场全部FFT/shared-node tail、内collar及完整材料角cut修补接到逐段次数≤15四角行列式判据，并完成实际marker/活动环带/R238条件链；新完整消费者已冻结，严格绑定本场实际尾及所有节点dtype/系数，待真实父场后运行。规范形与舍入renderer的表示差不能默许为零，整面C²、嵌入和实际连续像变仍需同场证据。详见[完整尾与标记链](results/R258-complete-field-tail-cardinal-marker-chain.md)。

## 4. 严格存在差距、保全与执行

R251 strict operator 消费者的重建源已在 request16/run43597596523 真编译并通过三个指定解析例（含完整z0与mixed term失败见证），实际回执见 [三解析场接口](notes/2026-11-14-actual-R251-operator-interface-check.md)。这是接口执行成功，尚未验证实际接受场、完整48/64有限Gauss scalar或全prefix；不重跑三个例子，也不把它列成新的候选验收门。

R260已把原固定finiteGauss半径的真实导数、返回ap/app、角Galerkin误差与径向残差分开，并给同g operator/二阶读出的完整误差恒等式。固定求积可能已低于原容差，不能仅凭非恒等宣布失败；R251直接同场Gram证书及共享节点C²仍有效，不改g、不加验收门。

完成数值标准后须明确无限尾、精确等距极限或其他仍欠严格证明之处；不要另加README没有要求的审批/独审门。未推的旧R179–224依赖若实际必要，按幸存源重做，不用排队记录补结论。已恢复的43提交、R235–237及真RK24/RK48不重复。

每一条完成结论实际pull、检查双README差异、记录已读SHA、普通push；非快进立即rebase重试到成功，至少每小时同步。原自动publisher因README变动保留artifact并停止发布是正确行为，root读取差异后接手。手动workflow_dispatch因PAT权限403不可用，已改仓库既有push request明确选择geometry/cardinal/coupling，不重复已完成zeroH/free3。任何分项完成都继续下一项，不将阶段报告当任务结束。


R265完整证明已登记：所有声明角行的一阶不等式模型有唯一正阻尼解，KKT/dual后验和完整Hermite B/Bᵀ均明确；只提供优化工具，不自动覆盖连续角或替代原全域/非线性门。request24真run43606770409现已全success：480首线性exit夹在接受/拒绝之间，近处四个actual负角与linear负角同集；大步475/477/479另有非线性余项失域。完整证据见[实际24全角与余项](notes/2026-11-14-actual-request24-full-angle-first-exit-and-nonlinear-remainder.md)。下一完整全角可行投影warm保原merit及全部域门，明确不冒R265最优。


request25/nativeseed独立原完整尾求解已接推送：精确恢复23完整577×224 candidate并保全部负零，只首次同17 H赋原initial；原完整solve/J/fresh audit/容差保持，失败与接受按原客户端。入口两源已全文读/静态语法，未本地科学计算。


request26/angleprojection已接公开Actions：从最新22 warm新建唯一原完整模型和全10240角约束，C度量局部Hildreth、全行径向修复、可行原射线后备与同f线段选择；原A/gdot/merit/17trial/全部域和新FD保持。只是可行优化方向构造，非R265完整QP最优，仍非true native/BVP接受。见[全角算子](notes/2026-11-14-full-angle-domain-operator-interface.md)及[可行投影warm](notes/2026-11-14-full-angle-feasible-projection-warm-interface.md)。

request25原完整solve已真实失败：run43607404925/job132484959081，iter0 norm=.04177307820740199，chartCondition8.810946110232247e59，原multiple-shooting line search failed，完整cut J/fresh audit未返回。先读取全部原试步定位，不直接接fullDN新H。

actual25完整失败点已保：[原生全部试步实录](notes/2026-11-14-public-native-seeded-full-actual25.md)。十步1..1/512均stage13/raw0/seg7动量D/S/A拒，无trialNorm；同seed完整withJ基态合法，原correction图表报告8.8109e59，尚无全J/delta可辨线性缺陷。下一单次原withJ/correction捕获完整有限模型，不盲增试步、不新H。26已真实运行43608931469/job132489481146，待实际投影与新FD。

request26已全success并逐实际包核：[全角投影实录](notes/2026-11-14-actual-request26-full-angle-projection-warm.md)。α2^-6、同新固定权重drop.0136476320，新warm4e2ee245…/新FD8.659e−10；仍col.007110525/BC9.449e−8/native0。5query全部实际正后限制移到左RMS472/481，接同一新warm七query完整角不等式；原真实全域回溯不变。Hildreth200未内收敛而已径向修到全行可行，非完整QP最优。

R266完整证明已入results：原stage/cut/far缺陷与原σ下降、computedJ/参考导数及全部算术差分开；可逆缩放保持原线性解，极大chart condition不代完整缺陷、chart失效也不等于全A奇异。用其解释下一实际25校正捕获，不额外加运行门。

request27/sevenprojection已接推送：锁actual26 warm4e2ee245…，新增实际坏RMS472/481得到七query×2048=14336行；同λ270/LSMR200/Hildreth200、完整原回溯与新FD。独立薄入口f6598a5e…/d05df1fd…不改26冻结源/父producer，详[七query接口](notes/2026-11-14-seven-query-projection-warm-interface.md)。

request28/nativecorrection独立原完整校正捕获已接推送：源0b49f142…/hookb20aee4d…，同actual25/23 H与全seed，原withJac/correction表达式保持；完整J/r/delta/所有原σ缺陷及最大图矩阵保存后在trial前计划停机。仅诊断完成，不报native/J/audit接受；全部大阵仅artifact，详[捕获接口](notes/2026-11-14-native-correction-capture-interface.md)。

R267完整证明已入results：同一固定模型可在任意证据点取Lagrangian下界，再约束另一个可行候选；最大合法下界优于只看投影后巨大梯度的单点界。完整原梯度与有符号slack仍必须实际重算，跨迭代刷新权重不可混；actual26仅形式代入，严格浮点认证另付，不新增运行门。

request27已全success，见[真实七query续步](notes/2026-11-14-actual-request27-seven-query-projection-warm.md)：α1/16、同固定权重真实降.0510362901、新warm f73dfc81…/新FD7.819e−10；完整14336行修到浮点非负，仍col.0071104568/BC8.963e−8/native0。最近拒绝1/8的七query全角正而1个原midpoint失败，位置未存。下一从此新warm保同七query/所有原门，给原evaluate返回middle/fm加只读观察，记录实际坏中点及角余量，不盲加第八RMS行。28真实run43611175099/source6bd52b44/job132496373274在原校正捕获阶段。
