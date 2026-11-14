# 待解：同一个最终精确闭嵌入族

更新：2026-11-13。**主目标未完成，持续研究。**
旧的完整逐项历史、旧计算断线状态与接口记录保存于
[本次归档](notes/2026-11-13-open-before-linear-degeneracy.md)。
其中“待恢复/未执行”的旧时态须由下面已实际恢复的状态覆盖，不能重复冒算。
执行、最新运行ID、规则读取SHA与复现入口以 HANDOFF 为准。

## 0. 完成标准及两条实际路线

根和本题 README 的标准不变：同一连通闭面、一个公共度量、C²连续的
精确等距嵌入族；固定有内点的 H 且 diam(H)≥.2D、held≥.05D、
含反射的非全等、每时 reach≥.03D。所有结论必须落在同一最终族。
每个子问题完成后接下一缺口，不以报告、时间、计算等待或单一路线失败结束。

[R3 相位降维](results/R3-free-metric-finite-fourier-equations.md) 的实际用途是：先构造一张
真正非轴对称的闭嵌入，其角向非零度量分量全部消失，再用材料相位作用形成
公共度量族，并在同一个固定 H 和几何预算内加四个不同非共面标记。
相位辅助像若仍仅刚体旋转，则 δE=0，不能当作最终非全等族。

当前两路都未闭合。旧 P_hat 路线已有真实参数返回共轭和若干完整线性块，
仍欠整个高低/帽/普通源/无限尾相对邻域强逆。新 Codazzi 路线直接产生同一
原腰的真实局部精确浸入，仍欠跨根、正帽及平尾的实际闭合匹配。
两条路线的背景、目标、源空间及证书不可不付比较费就互换。

## 1. 新分支：真实主体、全物理两迹和regular匹配

R125/R126给原腰完整周期GC重建；目标E仍原候选|Fr|²完整角平均，δ*=−7789843107295549/4611686018427387904及wholeη±1e−9。改变δ/ν/腰profile是不同最终候选。
旧全部短段、充分门失败、935盒正帽推进和求解恢复细节已归档于[前次完整记录](notes/2026-11-13-open-history-before-physical-tail-matching.md)，再链before-full-r02；不重做已完成结论。

[完整五分之一正权延拓](results/R131-supplement-full-r02-positive-weight-continuation-and-saved-rows.md)同原腰/目标全部579闭盒、4096角、原全权/BC/mean/尾，best1/200真误差<.003887037041、gap>.21117001608、真角导<7561.596192。原exit137报告false不改，v4仅消费已保存完整行并用新6行补齐，z/真梯度连续不重置。
[同一五分之一精确嵌入](results/R131-supplement-one-fifth-exact-embedded-annulus.md)由真实p/q及frame积分给[-.2,.2] φθ>.14711768015、J>.09095483284、κmax<8.099019；部分异号未证用一般界。仍是有边环带，须真正跨根及主体匹配。
原浮点.235/.239问题和正型高谱增长不能以候选残差替换PDE。R119真正Dirichlet端在r=25/8；body germ只[-3,3]，不能外插到尾。

[真实旋转正帽](results/R133-actual-rotational-positive-cap-and-Codazzi-Jacobi-graph.md)、[完整源/contact](results/R133-supplement-full-Codazzi-source-contact-on-actual-cap.md)、[A0/平移正则](results/R133-supplement-A0-contraction-and-translation-regularity.md)保全全部m/两mean/四端口及无穷尾。
[真实非零中心帽](results/R133-supplement-complete-nonzero-centred-cap-with-interface-jumps.md)全935盒/92接口11868非零dyadic jump，真[1,25/8]误差<.000054079035、Cgap>.1690329008、θθ<.183600040。分片修正抵消jump后由原积分恢复连续真解。
[全频开放曲率端口](results/R133-supplement-open-nonlinear-curvature-port-graph.md)内c A0球1e−5、全非零频率逆<1.212135；实际全M128内c差<3.691e−9入球，真帽对finite body B残差<5.941e−6、mean c<7.485e−7未消。不是raw-height DN。
[真实帽至九成及开放端口](results/R133-supplement-centred-cap-to-nine-tenths-and-open-ports.md)全1988闭盒/101接口13029jump；[.9,25/8]误差<.000258811、Cgap>.1684294403，内c球1e−5/全频逆<2.514346。全M128内c差<2.431e−10，B<2.291e−5/mean c<6.130e−6未消；改变内端固定数据的新驱动解不免费等同旧r1解。
当前正帽外d与两mean独立，必须接入真正周期regular尾并同时消掉主体两迹；不能把zero外端驱动数据当已满足尾关系。
[同一真帽外端解析衰减](results/R133-supplement-true-cap-radial-decay-and-growing-analytic-width.md)在μ3/2、τ1/128半径权上全收缩并经未加权唯一性识别原解；R处角宽>.06901529、全部B+c解析范数<7.035e−10。两mean完整，当前zero外d/mean成员尚须用真正R119非线性C逆和B Robin/mean关系联立。
[完整物理匹配与腰反射](results/R133-supplement-full-physical-trace-matching-and-waist-reflection.md)证明实际周期帽全B,C含mean匹配后，GC重建自动继承全位置/框架周期与holonomy；腰B全零及a′=E′=0给C²反射。实际tail height/两mean/Γ移动切口齐保，嵌入和reach另证，当前整体未据此授予。

[M128完整有限主体](results/R133-supplement-complete-M128-persisted-candidate-review.md) α=.65、ν=−6837290349363917/288230376151711744、651节点finite门通过；compact metric只改(.05,.18)，新ν不能转授原腰PDE。
[small-height几何v3](notes/2026-11-13-R133-m128-alpha065-small-height-frame.md)全角模的实际曲率采样4.117097272、held采样.04169097不足；未证连续Hausdorff/reach。α.70只是中间，必须继续增幅及精确几何。
[α.70资源恢复](notes/2026-11-13-R133-m128-alpha070-address-space-recovery.md)和[v9/v10拒绝](notes/2026-11-13-R133-m128-alpha070-v9-v10-rejections.md)保全850节点真实失败及完整输入。
[v11主动中断与v12](notes/2026-11-13-R133-m128-alpha070-v11-to-v12.md)原v11主动exit130/零accepted，后续只改预条件/可观察性，全部FFT/Jacobian/ν列/后向残差/原非线性门不变；有限失败不能断言完整J奇异。

[真正正帽与周期长段全曲率接合](results/R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md)由完整C_R→真实f*逆及两mean/外d联合收缩，在R准确匹配全B,C并继承实际周期框架；右迹像<9.155536e−10、L<.764594。fB≤2^-60仍独立，非零反射不删，远端F(a,f*)和主体未完成。

[真正周期整帽的r1开放内图](results/R133-supplement-actual-periodic-cap-open-inner-graph.md)已付c(1.5)变化和全部外反馈，后缀像<.000399129169<.0004；内B导数−q余列<.117940568/全频逆<1.212136，mean与fB列保留。旧M128.65 B残差<5.941e−6/mean c<7.485e−7仍未消；未来更大幅度不可免费入同r1小邻域，可验证r1.5任意数据预算。

[v12 ILU原拒绝](notes/2026-11-13-R133-m128-alpha070-v12-ILU-rejection.md)实际finite false/零accepted，异常属于丢弃型预条件分解，非完整Jacobian奇异；小过程/输入身份完整保留。

[v13两种预条件实际拒绝](notes/2026-11-13-R133-m128-alpha070-v13-block-preconditioner-rejections.md)两次LU成功但完整768步GMRES真残差1.001950438/.895710179失败，均零accepted。原false和完整源保留，有限问题继续。

[完整块QR及α=.70实际有限成功](results/R133-supplement-full-block-QR-and-alpha070-finite-branch.md)全部218451维/849块、原FFT后向1.57133e−12，一次完整Newton通过850节点原RMS/边界门；准确新ν和全三shards已保存。全物理B采样残差.00129582仍保，未冒连续PDE。继续.75及真实几何/帽入口。

[真实long非线性筛选及角增宽](results/R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md)固定fB时远端slope变化<25e^(−7L/4)||f*||；fB=0真incoming获物理角宽>10724906和dotA1输出<18||f*||/导数<24。非零fB混合、mean跨度仍保，尚须进入224标签并解全F。

[α=.75完整候选及原径向拒绝](notes/2026-11-13-R133-alpha075-radial-limit-and-complete-candidate.md)8accepted/1379节点，真实RMS2.52e−5仍超过2e−6且需更多节点，finite false保留；完整五shards及全角残差.3053294已存。增加径向节点不能自动解决角截断。

[完整QR的边界行分段重算](results/R133-supplement-complete-QR-boundary-checkpoints.md)保全部方程/频率/ν列，原FFT5e−8门和非线性门不变；每段真实重算换取较低因子存储。v15据此继续.765/maxnodes3200，实际结局见HANDOFF及原过程。

[通用r1.5真实周期帽](results/R133-supplement-universal-small-inner-periodic-cap.md)任意c_ne A0≤2e−5（另A2正则）+独立fB≤2^-60可接真正long，联合收缩<.086769709，真B+qc<1.664e−8/mean<4.637e−9、内全频逆<1.062336。完整dyadic .70和.75迹已入球；.75仍finite false，真实另一迹/mean差未消，不能据此授body。

[曲率C0管与框架残差的全几何定理](results/R133-supplement-Czero-curvature-frame-residual-and-global-geometry.md)利用真实正交传播直接积累位置/法向误差，保参考残差/接口跳/度量误差；同一闭浸入若正支撑σ且绝对曲率≤k，则星形嵌入且reach≥min(σ,1/k)。全像held必须对完整连续参考像给见证后扣两端误差；实际body/tail闭合及全部数值预算仍须完成。

[完整互逆多项式Codazzi系统](results/R133-supplement-polynomial-Codazzi-chart-and-complete-boundary.md)用u=B/C、v=1/C跨真实K=0，内部三次准确到3M；全部物理商边界、ν/均值、完整余项与接口jump保留。全旧候选变换尾仍非零，须实际重解新有限系统并支付全频后验。

[互逆坐标全非线性边界QR](results/R133-supplement-reciprocal-complete-nonlinear-boundary-QR.md)保全部有限项/实际ν列，独立完整FFT动作不再误用B,c坐标；四右端原Jac/LU核过。有限成功仍须全频/连续/真实帽后验。

[互逆α.70完整有限成功](notes/2026-11-13-R133-reciprocal-alpha070-finite-branch.md)M128/866node原RMS1.978779e−6<2e−6，ν准确dyadic与全三shards保留。采样物理B残差1.170e−4、C8.196e−5，完整未保留模仍需支付；当前.75新系统正在实际求解，不能据有限成功授闭面。

[互逆.75真实失败及全角缺陷](notes/2026-11-13-R133-reciprocal-alpha075-radial-and-angular-defects.md)三个完整Newton步后原RMS8.970311e−6>2e−6、需节点超1600，finite false保留。全五shards、真实物理B/C残差.155158/.799868与完整未保留U/V尾齐；现增至M256，不能只径向加密或放宽门。

[旧.765最后已接受状态保全](notes/2026-11-13-R133-alpha0765-last-accepted-state-without-final-outcome.md)会话28392不可用/无最终报告，原process仍未完成；真实accepted002的全部状态和导数已转存完整五shards，不猜原因或授有限成功。主体接续见当前互逆M256实际运行。

[R133完整连续互逆残差](results/R133-supplement-complete-reciprocal-continuous-residual.md)：新紧支度量γ/β/K/s三阶完整jet先消半径幂，与原完整公式192项包络相交；dyadic三次候选全部3M角频/真实接口跳/无限primitive尾均付。A0费用代数保持连续径向余项。新.70仅最前3闭片严格U<3.645e−5、V<2.330e−6、v-gap>.1927131974；全1613片/全频逆尚未完成。首版类型/初始化失败与v2较宽真结果保留。

[R119真实incoming到224并闭合帽反馈](results/R119-supplement-actual-nonlinear-incoming-reaches-224-labels.md)：固定新Γ0/好bump和同一long，完整非线性incoming经Z2074→a224逆，实际解a=D0^-1 g*(Φ(c,fB(a)))，||a||<2^-60000000·1e−8、Lip<2^-60000406且fB入2^-60真球。全部高模/mean/真实高度保留，30严格门过。完整余项准确RT−EB−MB，物理宽norm<2^-120000400仍不为0；其空间不能送Z2074逆，继续真实相对传输闭合。

[R133真实cut1.5逐模q及全频预算](results/R133-supplement-actual-cap-cut-q-vector-and-full-frequency-budget.md)：256个真实regular q经全部663闭盒有向传播，完整原参数/无限primitive/非零R74尾保留。所有m另证q<53/50；浮点q逐模ε须付（最大<.005560200378199），完整物理b/c两商尾和真帽非线性B<1.663187e−8/mean<4.636375e−9不得删除。提供实际cut producer输入，未证主体。

[R133 M256真实137及完整接续](notes/2026-11-13-R133-reciprocal-m256-exit137-and-complete-resume.md)：19:04实际Killed/exit137，原因未知，原process/日志未改。首accepted000全部1379×513状态/导数已原Hermite转存4×1378×513；原门未过不授finite成功。按规矩11不重复提交可重建大中间二进制，源/参数/hash齐。实际接真cut1.5 M256单完整接受步保存续算，另M128 cut继续。

[R46真未移位密度能量](results/R46-supplement-unshifted-density-energy-and-full-mean.md)：保独立height/mean/全源的9|u|²+μ|uθ|²+p²/μ，Hermitian交叉准确消±ν(logμ)θ且不用Fcal/μ。原全部215 native费用给log33.631533；完整原L2 amplitude双向内段Cauchy/逆<1.594617252e24、ordinary物理源<6.784778349e19。未把基能量自动转成高阶/完整R*。

[R133完整Wiener物理商](results/R133-supplement-complete-Wiener-physical-boundary.md)：有限Laurent W由全卷积||1−vW||<1给真实全部无限B/C、mean、二角导，无粗小比条件。实际.70腰/帽及M256 .75 accepted000均真过；后者全ζ<1.420305e−5入帽，保qfee/两全尾/非线性后B残差<9.571855e−8、mean<4.815042e−9。腰真实mean缺口非零，不授闭合。

[R133真cut M128原137](notes/2026-11-13-R133-capcut-m128-exit137-after-one-accepted-step.md)：首1343node完整步通过collocation/BC门，但原RMS要求1854node，下一完整factor中实际Killed/137，原因未知、无最终finite。保原process/日志及完整首步Hermite恢复参数hash；仅留M256大solver并限制Git pack并发配置，不改变方程或判据。

[R133完整径向分批作用](results/R133-supplement-complete-radial-batched-Newton-action.md)：独立径向列分批准确保全部角耦合、ν、mean和实际帽BC；375维独立全Jac/LU核最大残差<7.714e−13、作用差<3.918e−16。原84317及35049两次137/原process均保，原因未知。v4同时分批非线性和线性作用从完整检查点接续，原门未改、不提前授有限成功。

[R119真正型跨端指数传输](results/R119-supplement-actual-positive-transmission-and-weighted-affine-source.md)：在同一两端KAM角直接构造变角宽真Dirichlet解，全cross两方向半光学增益norm<32、真差<2^16 εI、全层<2^337X。含完整S_m/mean、参数导、Piola普通弱源/额外权导/裸端荷，27严格门；未倒除完整小transmission，继续全网相对逆。

[R46完整高阶密度及真scattering](results/R46-supplement-half-density-bootstrap-and-actual-strong-scattering.md)：同原215/550/全η与所有mean/head/source，C_3/2<2.273159795e31、普通源<1.214352278e25。分开初始缺陷与普通残差后真strict两窗3.656086e45/1.812562e39，完整RS<3.619623991e74；4门过，非换成模型散射。

[R46密度改进后的完整返回/全源](results/R46-supplement-complete-return-after-unshifted-density-energy.md)：同一实际word/b/β、全部head/mean/regular/source给R*<6.232408723e109，cutoff2^1125/逆<15.916848321，前一dyadic失败和未求head2^1127明留。五负源H1<3.172317e145、正普通<1.134110e85；8门过，仍未闭全inverse。

[R133真实曲率角完整主部](results/R133-supplement-exact-curvature-angle-principal-system.md)：φθ=C/<C>全圆微分同胚准确移除非对角主部角变系数；d/dφ保RC、mean且无高角导。严格负段全能量准确消vθ混合项，保参数源/PPoly接缝。浮点主射线范围缩小只作诊断，不授实际twist、turning或Diophantine。

[R133新紧支度量全域类型](results/R133-supplement-full-compact-metric-curvature-type.md)：全η/全部ν∈[-.04,-.025]，495旧真盒付[0,.2]K<−.28503058，94新盒付[.2,.238]K<−.01595314，2盒付(.238,.239)唯一简单根/K′>46.2850369，671原真帽盒付[.239,1.5]K>.030355535。根外ν准确不影响；未漏其他转向。

[R133均匀曲率角回归诊断](notes/2026-11-13-R133-uniform-curvature-angle-return-diagnostic.md)：真实.70/.75保存候选的经验ρ=.275012992304846/.274945339951982，secant约−.001353047，回归导数采样约[.979,1.022]，加密数值共轭残差1.56e−11/8.33e−10。全部仅浮点，未授真实twist/KAM或完整turning。

[R119联合KAM真实incoming与完整Newton链](results/R119-supplement-joint-KAM-incoming-and-actual-full-Newton-chain.md)：全复Γ/第四stop统一付，Γ*(a)反馈真实入a262144，非零fB long与mixed获约261921角宽。完整F所有列合法作94个全频修正，末β66624、真残差<2^-5760041760；每步宽损2080不隐藏，41门过，尚未无限收敛或消零。

[R133实际全频负前缀能量](results/R133-supplement-actual-full-frequency-curvature-energy-prefix.md)：新.70/M128与.75/M256完整中心、全η及全部Fourier/mean变分在[0,.2]双向Cauchy严格成立；.75的1192共同闭盒/751准确接缝，向外<1493.577736、向内<2408.100850、v负距>.1145864894566。完整ordinary源与真实仿射jump合同齐，不授turning或全BVP逆。

[R119实际Airy DN与网络通量shear](results/R119-supplement-actual-Airy-DN-diagonals-and-network-flux-shear.md)：真实quartic试函数给全m含mean P0<2^10，真实cross差升原Airy单位<2^385X；精确shear消对角变化，全部方向/源/endpoint荷保留，新增全层<2^240000X≤2^-22144。35门过，whole-network分母仍待真正接入。

[R133第五次真实137](notes/2026-11-13-R133-complete-batched-cut-exit137.md)：35756完整分批v4完成1342块factor后实际Killed/137，无checked solve、无新accepted或最终报告；原process/log保全，原因未知。继续完整QR磁盘检查点与减少驻留，原方程和独立门不改。

[R133完整保存主体几何诊断](notes/2026-11-13-R133-reciprocal-alpha075-full-body-geometry-diagnostic.md)：.75 M256全系数在0..25/8正常重建，采样D2.55109067、所选见证.1264804/比.04957895、实际κ8.723513/support.9086428。仅浮点且无最终尾闭面，未授held/reach；见证不足余量，继续增加实际振幅。

[R133完整QR磁盘恢复](results/R133-supplement-complete-disk-QR-checkpoints.md)：完整种子/末边界/前后代入保全部频率、mean、ν，恢复后仍独立原5e−8门。实际375维第六前向块暂停/销毁/恢复及两个全维RHS重读均核过，原Jac残差<7.714e−13、LU差<2.324e−14。新v5以全部M256向.76延拓，初始径向减半只是搜索网格，原自适应要求不改。

[R133随解曲率角完整等价](results/R133-supplement-exact-moving-curvature-chart-and-mean-energy.md)：m=<v>φ=1/D、d=−βI(u²+Kv²)，θ=m^-1∫v显式反向构造；完整非线性、mean方程、参数源和实际残差r+I(rv/v)qφ都保。局部线性矩阵仅β项，非局部与真mean另付二维正比较；真实接缝不能置0，尚无新数值逆。

[R133连续残差恢复与候选曲率](results/R133-supplement-checkpointed-continuous-residual-and-candidate-curvature.md)：原v3全有向运算逐闭片保存，v2有向读回极值；.70同3片实际首片暂停/恢复后完整通过，U<3.644477e−5/V<2.329807e−6、候选κ<5.190640。完整1613片未付，原v1部分报告保留不续，不把候选κ当reach。

[R133 .76首完整接受步](notes/2026-11-13-R133-alpha076-persistent-first-accepted-step.md)：85064正常0/672nodes、两原full solve1.409e−12/1.907e−11，cost.08509→.002286；ν≈−.03983591，当前RMS.002324/BC.001877仍finite=false。完整数组重建清单与原log/process齐，80604已从全新状态继续第二步。

## 2. 旧分支：完整返回强余项、有效cutoff与全源逆

较早全部证明、失败门、源空间和逐步数值保存在[完整历史](notes/2026-11-13-open-history-before-generic-cap-and-QR-continuation.md)，执行状态见HANDOFF。该分支仍是原p∞/原metric，不向新ν主体或新深profile免费转授。

[完整原root换架](results/R43-supplement-sharp-complete-shifted-Airy-frame-change.md)在原5050与两mean上给正逆<4.203925521；[完整相关root势](results/R43-supplement-correlated-root-potential-and-common-characteristics.md)保全部七场/两侧canonical域/whole参数/尾，|V|<22575.093446。
[原Λ的完整Bessel坐标](results/R46-supplement-Bessel-trace-density-coordinates-and-complete-mean.md)保所有坐标、逆、adjoint及mean的±2窗，原全部因子积<1.405e17、final base<3.099735。真实复域/cross-cone另付，不从实jet免费推出。

[同原完整返回](results/R46-supplement-complete-return-Bessel-rebudget-and-explicit-cutoff.md)准确半wordTg<2.282e23、全R*<5.137e165；实际cutoff2^1682、κ<.013473239、高逆<15.928899573，−4/3≤s≤0。**head复维2^1684仍未求**；全低高Schur、两mean/两regular/所有低频路径均保留。
[完整returned H1源](results/R46-supplement-Bessel-return-complete-Hone-source.md)五负源<2.391e228、正ordinary<9.347e140/weak<4.673e140/两regular<3.747e138；高逆只给规定zero-final-head的高L2 particular，不使physical低端口为零。

当前主要损失是仍保留的真实scattering误差RS≈2.9831e130。接下来须把真实root/graph和完整density相位的改进付到RS本身，再重消费全部强窗与源，而非只降低模型T或Rcalc。最终仍须真正可求的高cutoff/全head、ordinary/weak源、regular与完整相对邻域逆。

[真实同标签实jets](results/R106-supplement-same-label-real-log-jets-and-true-gap.md)全550×8控制/4096闭角盒/549接缝保留，同格比例交已证真gap后H2<31247.731109、H3<465239799.167、H4<1.351461e13。未免费扩任何复域。

[完整真实diagonal酉相位](results/R46-supplement-exact-unitary-density-phase-and-common-mean.md)base=1、G1<1.287351/G2<1.372537/G3<1.399209，公共mean、全部head/ordinary源和physical半阶重建齐；硬PH边缘O(N^-2)未删。仍需cross-branch及实际全RS。

[完整偶Taylor实际复域](results/R106-supplement-even-Taylor-complete-cross-cone-bounds.md)保原全复尾/所有mean行列，strict ReH′>0宽4.569622e−6、cross两窗费9.609883e17；final C宽2.731384e−5、费4.023839e11。实际全返回必须另行消费。

[完整真实root/graph/scattering重预算](results/R46-supplement-actual-root-cut-and-true-scattering-rebudget.md)直接消费原实际全Airy换架、七场势与全graph，真Croot<76896.424579，K/K逆的±2窗<1.442975e20/1.606283e21；两4/3窗实际RS<4.089839e102。全head/mean purification/双窗flux/ordinary源同extension均保；这是真RS改进，仍须重消费全返回及低块。

[真scattering改进后的全返回与所有源](results/R46-supplement-true-scattering-complete-return-and-all-source-rebudget.md)同原完整word/两mean/全Schur给R*<7.042043e137、cutoff2^1404、高逆<15.945812896；前一cutoff失败/实际head2^1406未求保留。所有负ordinary、正ordinary/weak、两regular的returned H1源齐，仍须可装配低块及全mixed逆。

## 3. 真实无限尾与全邻域问题

全部旧尾与新尾构造、完整局部图、失败与范围界限保存在[完整历史](notes/2026-11-13-open-history-before-generic-cap-and-QR-continuation.md)。新profile从8193后改K=2^128/ζ131，保前缀129..8192及两个全局逆幂，是新的最终候选。

强首剪切全标签图、C²平端、全mean、raw/source、重新第四stop与全模好集已经完成，不能免费沿用旧profile的完整网络逆。X≤2^-262144及a224<2^-262148首先是允许的真实输入合同，不能直接声称外端可达。
[真实根joint CK](results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)先由原实解入实段唯一性空间，再识别CK；[固定t真两端口](results/R119-supplement-actual-root-graph-to-fixed-radial-two-port.md)保两density主部、mean、raw h/p与weak端点负荷，全四根/前缀相对<2^164804X≤2^-97340。
[实际strict density](results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md)准确potential、两trueflow、高度primitive吸收一次角图差，全频状态(c,α,Z+,Z−)/两mean/源齐；Ση<2^192000X≤2^-70144。没有使用bare pullback同Hs小量。
[新actual joint KAM](results/R119-supplement-stronger-tail-joint-actual-return-KAM.md)全小窗、两全局因子、所有角模和交叉参数mean齐，在a224<2^-262148给μ<2^-261872；Γ*(a)在相位轨道不变，故可选单一最终度量。它只是准确scalar return共轭，仍须全正型双端/DN及source接合。

真正正帽—周期长段已有完整物理B,C匹配（本文件§1），真实远端方程F(a,f*)仍待解。下一步要把long产生的真实incoming角增宽送入完整224权标签空间，保非零fB混合项/两mean/移动Γ；同时完成正型双端form至实际Airy端口及ordinary/weak源，再证明全mixed网络逆和非线性收敛。不能以fB=0、a=0或只画参考尾代替F=0。

[KAM选择后的固定参考与两端真相位](results/R119-supplement-KAM-selected-fixed-reference-and-exact-endpoint-phases.md)已准确付Γ*至固定Γ0的全势费用，strict同空间相对仍<2^-70144，完整两mean/频率/左右端图不删。D_aΓ*(0)=0与二阶界保原首Jacobi方向；正型DN/source及全网络仍欠。

[真实正型双端DN至全Airy Cayley](results/R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md)保完整S_m的非对角与mean，实际density/normal shear后自伴R给全空间酉散射；全部已配KAM端角内部层的|s|≤4同宽差<2^400X≤2^-261744，ordinary/weak源/总flux/weighted mean/端荷齐。外有限未配角接口与指数小transmission的相对逆仍不得省略，继续真实224入口及全F。

## 4. 非线性收敛与同族全部几何

R112/R114 的整材料平帽修复允许构造单曲面时作轴向刚体平移，费用无
帽半径逆幂；每步固定整平面度量，最终phase族可固定最终H。
它没有授普通C²邻域对无限退化曲率的相对小扰动。需全尾普通源/regular行、
邻域右逆、全mean/输出度量选择、迭代C²收敛与完整累积费用。

R69/R78/R79 已给旧闭近似背景的固定帽、可见位移、真实reach及直径费用；
R123 另给充分校正档(.001,.01,.7)，由σ>1/2、K<12、D<2.553推出目标比例。
也可用更好的实际曲率预算；一个充分门失败不是no-go。
新Codazzi分支必须重付它自己的全域嵌入/曲率/自距离/直径以及固定H，
不能直接消费旧曲面的reach。
最后四个不同且非共面的固定标记、5% held、含反射非全等与3% reach
必须在同一最终精确族及其全部参数上同时成立，届时才完成。
