# 尚未完成的构造任务

进行中；无满足 README 的完整解。优先推进下面 O2 与 O4，子问题结束即接下一项。历史任务、失败实例和准确排除范围保存在 [截至 R72 的完整 open](notes/open-before-short-entry-result-20261114.md) 与各结果中；本次压缩只整理任务，不取消未完成条件。

## O2：准确强核心接完整闭帽（当前几何主线）

核心为 $A=1,B=7/25,w_c=1/50$ 的准确椭圆柱；固定端口和六帽见 R33、R44。同一旋转不变度量 $g=ds^2+a(s)^2d\theta^2$ 的非轴对称完整连接若成功，可通过角相位形成连续等距族。最大的未解问题仍是这段完整连接，不是单独的核心幅度。

### 当前证据与立即动作

原独立高度设计、长/短入口、九高度一步与接触quartic的完整失败均已保留在notes/log；永久原c0不可换成selected或accepted。固定g与线性共同帽高行的来源见HANDOFF及[设计](notes/fixed-metric-linear-cap-height-constrained-solve-design-20261114.md)。九高度状态f198仍是新B局部分支的162维来源。

旧g一次joint resume43635770962的81a状态细η.8882/κ354/镜像.01571，已停止盲续L2。minimax43637739532唯一54trial物理门全过、辅助δ仅初点过，原最终仍81a；保存完整5d383918试探态。独立七输入只读actual43639240317已完成：work100×192 η.26528，fine160×384/768 η.367912/.368054、κ87.5702，峰在帽patch s=.7875；镜像样本.102711906>.061、正z/帽高/盒/球1.01/strip.39三网都过。原δ=.2651667069仍全失败，保原未接受事实；这不是完整metric或reach解。[实际证据](notes/metric-epigraph-saved-trial-first-fine-result-20261114.md)保全部身份、区域值与同态精化。

dense actual43640503728已完成：旧100⊂160工作并集消原径向漏峰，14个实际评价后budget退出；新028c8954同g/b0/163的fineη.268197874、κ73.102607，误差峰移body s=.21，曲率仍patch .7875。镜像.101055731>.061，但细strip .390000019476 超硬门0.39及容差；rawδ.2659538765工作/细均失败，未抬高。工作物理best与aux best（仍初态）分别保留。[实际证据](notes/dense-mirror-minimax-first-actual-result-20261114.md)给全部身份和门。

exchange actual43642966285已找到e407a214全网内条带物理合格态：384/768 eta .266411174/.267146532、κ73.359843/73.359830；fine strip.389989992779、镜像.1016723303。rawδ.26640845723仍两网失败，不抬；六轮/12major后轮数限退出，最后16池外违反，不是收敛。总127.514s，初始化96.095/优化15.623s，选行矩阵仅2.823MB但RSS约3GiB；[完整实际证据](notes/full-grid-exchange-first-actual-result-20261114.md)保全部门与身份。

公开continuation run43645177423/source2f1b809c的曲率人工/actual已成，run43646786908只恢复六原文件并按gzip提交。最终仍e407、κ73.35984/η.2671465，目标曲率未改善；20轮每轮2major便换池，优化113.733s而非300s耗尽，RSS约1.5GiB/二jet批导有效。[完整实际说明](notes/curvature-epigraph-first-actual-and-recovery-20261114.md)已登记；只读43647629532已查明20轮交换时当前池也仍违反，末次216池内行/24池外metric行；只有初点物理及固定metric合格。下一复用learned3866池，仅当前池按实际tol1e−9恢复可行后交换，否则让同次SLSQP继续；出口仍严格检查遗漏，不盲加轮数。以下保原运行定义。按[R103](results/R103-actual-metric-curvature-semidefinite-gates.md)和[分批交换接口](notes/curvature-PSD-row-exchange-integration-plan-20261114.md)固定同g/e407的eta预算167/625，最小化独立曲率上界lambda，仍保内strip/镜像/帽高/盒。全部五jet/二阶参数列按16径向行+0/L分批，11组全值门筛，不能用目标g冒实际I；先由真实报告给新lambda裕量，旧delta失败不改。20轮仍共享80major/120phys/300s；最终.061局部目标与非局部reach另算。

[R74](results/R74-near-isometric-mirror-and-speed-linear-height-gates.md)的近等距镜像/速度必要式仍保；当前η不小，不能先用其小ε前提。随u/v变化的逐点门必须由当前几何/Jacobian重建，不能复用冻结T的高度多面体。帽高是同一个共同原函数的硬线性行；所有采样通过仍需最后连续与非局部reach支付。

### 仍须支付的几何内容

1. 入口与自然patch都要降残差，包含足够非解析/高阶角场与径向自由度；有限首jet修复不证明完整Cauchy问题可解。R64的下一 $u_5/v_8/b_7$ 项须用完整g的body项、扣旧参考，配套改自由基。
2. R63表明非圆到圆的准确连接必须有 $T_z\ne0$；不能删除空间角列以换更简单的平面模型。R55/R64仅排明确有限表示，不能外推一般 $C^2$ 不存在。
3. 当前 $\tau=.061$ 是强于README必要值的设计筛，R66只给帽高必要条件；同场采样的帽高或局部帽法弦不等于全曲面reach。曲率及跨片点对仍须覆盖。
4. 球1.01、strip .38的充分幅度预算尚未全域通过；放宽条带至.394会换objective且无该边界余量，必须显式记账。
5. 若改核心B=.36/.37或g，须新建完整core/端口/c0/角场/度量身份，不得混作当前固定g精化。新B=.37实际43634358250已完成：语义抄系数初态η67.0064、曲率加密恶化至1.31e6、负z与条带/帽高/镜像门全失败，无优化/entry/Q；不是新B一般排除。新g/b0身份及同态384/768见实际note。局部collar actual43636741138已complete：新g211c1b19/物理5f036761，外域六jet和gjet差0；新η1.185449、κ270.727仍失败，镜像.01426及strip.39351均在未改外域。新R66高度必要裕量.07274，但不授reach。另识别新core的U4/V7/B6被旧自由基锁错；成套leading actual43638423274已complete245.363s：新g保持、b0df1a升级、物理8d9d；细η1.174996/κ263.3758仅有限改善，外域镜像/strip失败仍同，紧支撑共同中心保帽高。修复不冒完整Cauchy；实际证据见notes/localized-core-leading-repair-actual-result-20261114.md。后续仍须开放失败外域，不能只延长局部入口。设计稿在 notes/elliptic-core-design-coefficient-transport-20261114.md。

## O4：真实零算子带的完整高阶与有限连续族

R37/R45已真实实现有限零二阶算子与准确四块闭合；R52给真正重叠profile平面的完整三阶圆；这些不是有限等距族或完整嵌入闭面。R56完整变系数编译已运行成功，保留一个全局右锚。旧R52冻结profile的full-fourth及独立profile诊断已失败，不重跑原实例。

R62/R65的理想互反bulk仍有非零纯第四漂移，不能忽略真实桥。R67给全部phase $P_0+NP_1+N^2P_2+N^3P_3$；R70真实零矩阵桥已消高两次，仅余 $P_0+NP_1$。R71准确实现28个候选第三交换子方向，任意有限系数用有限小loop实现，不把局部参数区间无限外推。R72同scalar任意frame可用 $M=T=0$ 桥。

[R73](results/R73-pointwise-eight-matrix-and-local-third-bridge.md) 进一步证明：R56的二阶密度逐s点就在同一八矩空间；真实变量profile有不可丢的链式项 $\Psi$。任意零矩阵桥第三响应精确分成八矩迭代history与明确局部三次密度 $\int\mathcal C_s$；history因端矩阵零而为反对称交换子组合，R71可准确消。**当前基准桥问题只剩局部项，而非已证明全部第三响应可清零。**

立即推进：

1. `p1_bulk_exact` run43628716304/sourcee42c78ff已完整完成（2.121s）；28响应形式代表秩18，target473→59项，余76项，无关系，非资源退出。[实际说明](notes/p1-bulk-whole-function-actual-result-20261114.md)保准确范围。R75明确局部IBP余型与word递归终止。新actual43630157008完成：word余95项、10个原式依赖给真实span维数至多18；局部形式54列给fresh原式余0的阳性关系，仍须真实实现5个local系数；没有关系不作函数非成员证明。它没有包括不同scalar基准桥T、其他phase、$P_0$或ruling。
2. R76已准确实现任意scalar闭路径的2∫C，并以真实长度变化给2t C3[path]及严格非零面积例。R77已证明实际有限path签名张成全部面积/三次速度系数空间，并用真实线性loop准确合成，含当前阳性的两C3列；C1实际43631537869检出14未消项，simple/extended三profile均未成；完整R模R71已形如A(k,ω)+B(k,ω)/h且L+有fresh真关系。R79已证明闭C1真实有限可达及端点势；新endpoint actual43632772378已完整验证101行端点商，加入真实端点势后pure P1找到18有理R71响应且fresh原式余0，已登记R82。旧三profile假设失败仍保；不能把特定端点组合等价外推为完整变量一形式等价。不要用常态Ψ=0冒充变量桥。
3. R78的完整P1与R80真实第三仿射集合已完整处理；R87原式36/37子式排单pair的泛profile，R89–R94建立全状态真实仿射协变与整权分块。**R98 actual43638896281已完成全部正states的universal否定**：权2可付/权1零，权0真实14维、14/15非零子式给Λ(b_Hd)=1，任意正组合4Σℓ>0。R96把该障碍搬到同一合法C∞三矩圆及无统一导数盒时相对开稠密类。此子问题已结束，不再跑低权、增加同类states或重跑72/252列。旧失败与精确模板均保在对应results/notes。

   接下来只研究未排方向：特殊profile圆，或固定有限N的完整P0+NP1。R99已核R83真实t1×W0四列：完整Jacobi两列准确零，τ_p1t1和h-shape(k)在R98明确扩展查询下非零，给保持M/T/P1的P0切向。R101已支付共同I与真实基准：固定小M族重复不扩scalar包络，真M0第三环n次复制使V=E(t)+n(2v+tK)。在有限扩展空间应用R96得到同一合法圆/固定查询ℓ，再选有限±T、n，由介值可匹配任意ℓ(V)。R102进一步以有限切向基/真实串联及Brouwer，保E(t)+n(2Σv+Kt)全部基准，支付同一合法圆上至少15个独立查询的任意共同值，可包含R98正字符；真B_E8(W)维数现由R126提高到50≤r≤288。R105进一步付完整canonical成本共同有限模板及真实span U4的端口独立/仿射不变，R8⊂U4；R96可在同一合法圆忠实表示整个U4，但R118现已证明U4/R8非零，不能再试图证明两空间相等。R109进一步给逐点n−N′∈W的真实局部势与完整公式V=∫(v−B_mN)−∫B_mH−(1/6)∫B_A[A,m]，后两项准确落R8；N(0)只靠总矩阵0消，不能先置零。故下一研究不含累计二/三history的局部密度积分商：v先真s微分后置累计值0，按原式消费，不把形式非零余项当真非成员。该非零商的额外方向和ruling仍须真实支付，R102单独不授完整period控制。R84倒行V同号/加法半群及frame长度门保持。

   [R112](results/R112-local-fourth-geometric-derivative-weights.md)已证明局部密度几何导数权恰只可能0/2/4；这三个有限片可分别消费，不能把改时长公式当独立真实成本控制。公开run43645177423的local_fourth_quotient先处理导数权0、完整−4/−2及仿射权2/1/0；W36完整原式先导出给完整m8纯尾投影，随后局部原式完整导出供后继直接消费。任何资源退出或形式余项都不冒真实成本非成员；若需实际可达性，须保M0/frame条件和所有连接基准。

   pure尾方面R85/R88已消4m−9及4m−8；R92给真实三primitive action。R95 actual43639240317七短系数、端势与原DAG全0，将m8 D25压至1605项5组，const/linear完整保留；c10/c9准确零端势，所以period关于c次数≤8。R100 actual43640085842已把c8完整端势/短action与23真history/参数族/原DAG全部核零，保p/ell/zeta三个真实零端ODE，单块符号仍未判。R104现用B σB Bᴿ (σB)ᴿ的真实闭合词支付c8：同端口、共同正I、真实位移/frame闭合且M=T0，c8倒行偶/反射奇相消，使该D25 period次数≤7。R106已从完整R56原递归和移动尾端锚证明D_j^σ(c)=(-1)^jD_j(-c)，因此四块D25只余c7/c5/c3/c1；全偶参数项已消。R107的真实全场协变给A_Hd(c)=H⁻⁷A(Hc+d)，所以a8=0后a7正仿射不变，不能再靠整体h缩放或ω平移清掉；这不是正性或消R8证明。R108 actual43642966285已付c7完整五history余action与全部14组/96项（零端Phi7、mu/nu真实ODE及十新差式全0），常数线性项不可删，五history受同一h/k/omega驱动。R110 actual43643100132另证真实K=B_t1(τ_p1t1)的D25=−(153664/75)c7；R101保基准/连接的有限复制可准确付a7，随后四块只余c5/c3/c1。不能将这项非零响应外推全R8满秩或完整period已零。R111随后已付四真实平移方向的奇查询满秩：d=0/1/2/3给κ(c+d)^7，Vandermonde(d²)非零；保全部v_j/E/连接后有限Brouwer同时消四奇项，反射再消偶项，故同一有限闭浸入环带的整个m8 pure D25(c)恒0。该尾层子问题结束，转其他r幂、完整mixed与局部U4/R8商，不重跑已付四方向。完整V=2V_B+2V_σB与固定全带右锚ruling缺陷仍保，余下其他r幂/mixed/完整range继续，不把D25一层全零冒完整V或全函数反号。必须使用R93/R97的真实驱动约束：∫kh=0，K2=L+E，∫hkω=K2，K2=−∫(F/h)kρ，故非恒h、S>1且(S²−1)E≥L。不得把primitive独立化、把这些积分式逐点置零，或将非零密度当非零period。

   [R116](results/R116-full-m8-tail-response-rank-and-finite-query-control.md)已完成完整m8响应31/四块15准确秩；真实R8维数至少31，同一合法圆31查询可共同任意支付。四块15查询保原D25全部奇项，再加11尾行；一般基准仍可能有响应像之外的商。[R123](results/R123-static-pure-tail-three-dimensional-graded-quotient-and-G-blindness.md)已实际消费197个pure静态原根、254分权目标：分权系数尾商rank3（w−1一/w0二），全部余项在原45行内；G完整九项尾恰原列10/128，不能检测R118完整障碍。此时M0未施加，未分权/实际成本秩未认。[R124](results/R124-zero-matrix-static-tail-payment-and-remaining-derivative-costs.md)的actual43649160345现已付这一规范化：154静态系数全入像、原未分权商3，诱导Δ2 rank2/even1。任意真实M0路径的pure商只剩∫Π8(L2+Δ2+L4)，固定桥的常态bulk复制不改此商。下一新增完整原N0/N2和两mode v2/v4，组成L2=v2−B_m0N2−B_m2N0、L4=v4−B_m2N2；N2未证在W不能删，Δ2不是完整L2。复用旧接口/已存原式，不重编W或静态目标。

   [R113](results/R113-full-m8-tail-response-dimension-bounds-and-orbit-coupling.md)已付完整E8×W36纯m8响应的46维上界/四块22维上界；单R110方向平移四块像仅4维，其他r层被D25四查询准确耦合。新fullm8消费器必须保全部原输出，不能预删违反结构界的项；基准U4未被限制到这些响应的54/29行。[R115](results/R115-static-local-fourth-top-weight-payment-and-unresolved-next-block.md)记录local actual43645177423已导出36W及完整局部静态密度，最高仿射权+2一项原式可付，+1两项未决；主报告超过95KB而output_limit，不是数学非成员。R114已用20常态正锥、八个有理基准、真实整数圈/连接IFT补上此约束门；配平值非零才可导出实际有限成本非零，单个形式余项不够。[R117](results/R117-static-weight-one-reduction-and-reciprocal-costs.md)进一步将完整权+1约束商化为h(k³−k)G；不再重复已有206项NF。[R118](results/R118-static-G-exact-separation-and-nonzero-fourth-cost-quotient.md)的actual43647225907已给真有理7/8非零子式，证明G∉R8、U4/R8非零、dimU4≥32。k2/−1/2正整数互反圈及反号对的leading/桥/IVT已激活单个额外查询任意支付；[R121](results/R121-central-baseline-correction-and-joint-fourth-query-control.md)现已用中央修正和乘积盒Brouwer支付31+1共同可达，剩余完整商仍欠。后继直接读完整gzip，先按[R114](results/R114-constrained-static-costs-and-real-zero-matrix-words.md)处理M0约束的8个m0几何函数，再判断受约束积分成本。

   [R119](results/R119-positive-static-cone-and-linear-multipliers.md)已给静态正锥的准确乘子门：所有正配平静态成本非负恰有固定八矩μ使λL0−μm0≥0；完整真实成本正泛函须先杀R8再满足此门。该门对完整路径仅必要，导数权2/4、全部桥成本及非零泛函存在仍未付。[R120](results/R120-G-lineality-of-the-closed-fourth-cost-cone.md)已进一步证明所有完整真实成本非负泛函杀G，并杀其有限仿射轨道；universal成本闭锥lineality包含R8+RG、维至少32。证明先在准确零矩表消乘子，再做真实H→∞，未把mixed权直接当单权。R121已另付实际32查询共同控制：先修正各prototype的λv，t盒/m先固定、中央N次之、响应n最后，完整E和所有N²/N³附加Q成本均保。[R122](results/R122-affine-G-orbit-and-real-joint-query-control.md)已付整个有限G仿射轨道商的r+s真实查询：有限H先压低权，再N吸收商基准，最后响应n，完整N²/N³仍保。轨道商维s未知，下一仅对原NG与完整权零响应做真成员/非成员门；首次NˢG属R8后链终止。若U4=R8+orbitG才可升级整函数，此前提未证；其余商与ruling继续，不把闭锥当实际半群。[R125](results/R125-complete-response-dimension-at-least-48-and-cost-49.md)已结合旧完整块证书与pure投影核，得dimR8≥48、dimU4≥49，R121真实联合查询至少49；没有额外研究编译，不把pure尾rank31当完整维数。

4. 得完整第四后继续高阶/收敛/有限族与宏观几何；本题完成标准不接受阶数截断或只靠N压低缺陷。

旧不交profile、普通双简单有限幂外尾及明确窄packet类已被R29/R34/R35/R49/R50排除；保留其准确范围，不重复同类预算。全平/退化外尾与其他真实几何仍可研究。

## O1：双圆领相位机制（保留备选）

本题没有 $\delta_E$ 正下限，同轴双圆领也可先行。若非轴对称环带与两端开圆领相接且度量旋转不变，相位可固定材料握持区而改变整像；允许如实 $\delta_E=0$。偏心/非平行端口也可研究，但末帽材料刚体位移并非自动的整体Hausdorff下界。R17已处理旋转参考的 $m\ge2$ 线性端口；$m=1$ 或真实非旋转参考须有自己的边界方程。继续存在/完整非线性BVP、同g精化、全时嵌入和reach。

## O3：其他精确局部机制与闭合（保留备选）

T-surface、可弯管或变换共轭网须同时解端口位置、切平面、二阶jet、周期单值及非自交。标准T网直接双周期化的符号问题未解决；Bonnet对不是连续族。空间星核心的零framing是必要门；被R23/R24排除的旧奇高度封口目标不重做，偶余弦核心仍须新的全角曲率、有限宽和幅度预算。

## 完成时必须一并支付

闭连通材料面；每时刻 $C^2$ 嵌入且时间在 $C^2$ 拓扑连续；固定材料H有内点与直径至少 $.2D$；无刚体对齐整像 $\delta_{hold}\ge.3D$，另报 $\delta_E$；全域全时reach至少 $.03D$；同一准确g、参数和时间范围内最大相对误差至 $10^{-6}$ 并在空间/频率/时间加密下继续下降；全时嵌入与非局部法球；若干完整网格每件<5MB，大数据按规则压缩；复现脚本和严格存在差距。达到后继续 $.5D$ 或严格存在。

HANDOFF保最新参数、输入、实际run与规则SHA；所有研究几何/积分/优化/完整编译在本公开Actions，论文推导与公开输出解析可本地。按根规则12不设重复冻结、审查或重跑门槛；每个完整证明直接登记，每个有意义步骤及时push。

### R126后的最小新增门

R126已严格证明完整权零响应16维、NG真非成员，2≤s≤10；真实完整响应至少50维、U4及可联合支付查询至少52维。旧G/NG门均结束。下一独立目标只检N²G与完整权−1的36原列；若原式阳性立即s=2停链，阴性仍须真实依赖上界和匹配原有理增广子式。R127的正泛函缩减纸证已成，紧接独立登记。完整导数因子与曲率只读试探消费者正在部署，不等待阶段反馈。
