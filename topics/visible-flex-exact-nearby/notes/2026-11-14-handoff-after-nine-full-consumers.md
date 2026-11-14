# 交接：同一个可见振幅的精确闭等距族

visible-exact-astra-ac0d，2026-11-14 05:42 UTC。主目标未完成；持续执行，不因时长、阶段或等待收尾。

## 规则与同步

根/题README早已全部读。2026-11-14 05:40真实pull --rebase成功，SHA c79f0f7702ddb354f57109162ccc171c5a1580cd；根README新blob 1d1ee2806f115f3206920d178a21c31047d5a60a，仅新增14已读并立即执行；题README仍84b6d9fc74ed90ab725aa230cdf348f325505396。每次pull检查，只读变化；至少每小时真pull并记SHA。
新14：长计算走公开Rogerhu12/math-research-ci。推根ci-queue/visible-flex-exact-nearby--<name>.json，含topic/command/timeout_minutes≤350；默认Python3.12/Node24，ubuntu4核16GB、≤20并行，每5min取队列，通常5–15min启动。检出README+本题，依赖command自装，额外目录用sparse；$OUT_DIR或题目录输出自动push，ci-runs/<name>-<run>-1下log.txt/status.json；>45MBgzip/>95MB丢弃。command公开勿放未公开结论或秘密；GH_TOKEN可pull/push。新长任务走runner，规则前已启动作业保其有效检查点，不重复计算。
每结论独立commit/push；非FF立刻真pull --rebase再推到成功，不force。root独占Git/H/open/results/log；代理仅专属新文件。PAT仅瞬时CLI/env，不入文件、配置、提交。H<10000B、md<100KB、open尽量<30KB、件≤5MB/>1MB压缩，不推大可重建中间；不freeze/独审/冗余核验，不动根LOG，binary用正常Git。
repo=/workspace/scratch/ac0d699811ad/math-research；上层无凭据git_checked_publish.py已接新root blob及本题ci-queue路径。ν已推3e94fdd17c4e96eb48e9143ec70b86faa39c585e；tail64已推293a3f。下一逐条队列all_ready_after_rule14_publication.json。
完整上版H已保notes/2026-11-14-handoff-before-public-runner-transition.md；完整早期身份、旧失联/API/计费失败和各归档链见其中，不改写旧记录。新notes须加入sparse patterns。

## 完成标准与恢复对象

同一公共精确度量的连通闭C²嵌入族、C²连续。D=diamF0；闭H有内点、diamF0H≥.2D且逐点固定；未对齐全像held≥.05D；含反射E(3)非全等δE>0；每时reach≥.03D。纯phase是刚体旋转，须同族四个不同非共面静态曲率marker。
Eν=Eexp(νw)，w支(.05,.18)、a不变；任何ν/腰/deep/profile/marker变更须同对象支付全部费用，不搬旧g0/91040c/R131有边环带。
原六步stage01–06均重做并分别推，最终五gzip/payload、16科学字段、65初值uint64、[4,6144,65] Hermite全字节同。candidate SHA ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413；6145nodes/M32/N512/[0,25/8]；α=6890507429876859/9007199254740992，ν=−2572625729470897/72057594037927936。
本地candidate=/workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json。tol2e−9有限BVP正常0，不是精确PDE。Python3.12.14/numpy2.3.5/scipy1.17；Flint.9/SymPy1.14在/workspace/scratch/ac0d699811ad/runtime-deps，PYTHONPATH加入，数值单线程。
newton正封通用全六步CI入口，复用已推final_replay_stage.py/first_accept及完整历史metadata/Hermite重构规则；大中间只RUNNER_TEMP、最终ac1同字节门不可弱化。root几何将调用同入口，不另造近似seed。

## 主体已完成与当前算子缺口

已推：完整mean7721闭盒/6143接口，Γ<1.013237，全L2非mean回填<.103384、mean源<.538112、完整ν列<.002935584；完整8MBnative使用direct bin.gz五片+索引，lossless_parts.py已推，不删行。actualR13同ac1：Z<2.532986e−13、Robin<1.258388e−15、mean<2.048004e−19。
已推strict3071/2549跳：完整四态正向H1初值<10.124885/源<10.240174；grouped reverse12为404.222565/408.729241，原粗1e26不改。rootpiece15/fold27已真实恢复同ac1，root H1源<.028915503、graph<.001826455，mean/physical桥齐。
wholepositive4650已推：N97 order0含外反射反馈<.303291679，order1内部<.788277736（右高port独立）。完整negative-height窗已成待推：feedback<.711062297、逆<3.460954/源<.436563951，n(r)仅逐点换范数，head160/mean/外背景全保。
完整ν5M1156闭盒/864跳、全η已正常0/994.33s：源<1.964956，G核+跳<625.523019（更粗，仅供signed pairing），native281fa7c17d16b8f6823883df7ff61fc12f9c846c6b98bdd6951eed928d480848。正待继续推送。

newton：旧b4-output193 response87572/adjoint44334首次全FFT门真实失败8.69e13/2.65e14，原refine1仍跑、失败不改。原端tiny近纯m4。已推全regular补算子：保所有外Robin含m4、腰幅作唯一ν scalar；D h=+Fνδν，完整Gram/mean/双残差齐。新response94122/adjoint82632全6144 QR完，cond2=34.615681/7.384309，仅有限诊断，前后代入及全FFT门仍待。新allregular物理边界转置两件已读待推，旧schema禁止改名。
连续193 regular子空间proposal37169已跑首8段[3.1225,R]、小原生正常0，现约r2.91/Gram<2.07e−15；只是proposal。新完整Green判据以投影defect E及C=2P Sym(A)(I−P)−E*保两Volterra全部源/边界/跳，连续st<1还未实付。proof(source修正两quad)/脚本/first-eight与reconstruction四小件待root读后推。agent准备公开runner长任务。
phase新全模physical-cap已成且root全文读：同ac1 [.9,25/8]/原全η/1346闭交/全Fourier/两mean，χ<.820523、逆<5.571744；ordinary B/C源<12.725633/22.179140、内Cne<13.316116。物理角逆Lip<.015212，旧/当前外q差另付，v2 native ad6efc2a226131245ff4197a0b5da2843578224368a340f7a50d383c03a1819b，待推。
phase正在支付moving→physical真H″残差ordinary/divergence桥。极小PPoly值跳导致bare composition不能按L2小删；正独立定义精确连续修复Qbar（减全部此前dyadic值跳），不改ac1。必须付累积差/右端/mean/ν/所有native中心差再接连续图。负侧完整return算术仍真缺口；新两ray仅诊断mean lift .43186248774、非恒定半range .00429761161、rotation约.27492243..46，不能授Diophantine或搬旧R104。

## 原全残差与几何计算

原残差源98eb7034…未改。首8合法复用+新8joins已推；余段8–3647(session35006)、3648–7295(89994)每8闭盒原子保存continuous-final-20261114。右段η0在首graft7271会因“parameter half width must be positive”保存域拒绝，之前成功body行全部保。
独立graft7271–7295在原η±1e−9完整25闭盒/24内跳、23.612s complete true/failure null；native882a7540f473bd0156c5dcd2f4868b80d25fd227b66d773ede33e6866de0a6a8，RU<5.392561e−13/RV<3.147043e−12/vgap>5.8423654349，待推。全段交集仍η0。
新merge_complete_moving_residual.py已写未跑：只接受上述明确末端域拒绝，逐行/原源/12依赖/candidate/partition全齐，复用7296行及已有joins，仅新算缺失接口，必须6143全齐。目标continuous-final-20261114/complete-merged.json.gz；[.9,R]齐后立即告phase，不重算primitive。
原geometry probe8967rows/141blocks正常0已推，geometry-final-20261114/report.json；max|G|1.275559740657、support .905420600389、形式|κ|11.0825641仅有限诊断，大blocks只scratch。
新directed geometry grid脚本/jet核未推：原block uint64核对、精确有理选片、每个真实germ单侧Taylor和skew误差传播。attempt01零半宽域拒，02浮点中点选错片0块，03首块成但Wiener norm粗；全源/报告保geometry-verified-20261114。attempt04改exact角grid operator norm，首127步正常0/eQ<1.381e−6；resume01 session19425现6/141/eQ约1.856e−5。scope仅exactφ_k、model anchor；连续角、真帽锚和精确PDE修正未授。规则前已开始，保其检查点；新长分块交公开runner。

## 全尾与最终几何

53–62全部源/mean/weak/两physical图/Γ*两列保。原N_M=Cζe^-τ∞M×有限幂，τ∞∈(5921/16,2961/8)，幂夹−33024/−30960，Cζ=εδ8192^-485/4。完整两行26门已推：Y_j=N_M aΛ^(b−j)(1+θ)(1,s)，|θ|<1/254、物理范数255/272至272/255、真高前缀齐，仅径向零背景。
63全Sym2 70门已推。64尺度正确117门已推293a3f：完整generator>2^-2200000 M^-30697，r/N/补偿/Hessian全付，旧29767未使用。root新公共网络31门待推：一次θ_M且P_M固定，完整端口逆<2^2200007M^30700、同角宽有限阶损失，保双侧W/good-t，好集>1−147/16384；原label仅比较余260幂，physical source/nonradial不自动得。
tail65 59门已成并root全文读：M无关ψ以32次导数准确消原两phase，光学material/两行WKB/真端框架全付；M≥2^4096ρ^-64√B时局部全band generator>2^-52000M^-182。bandθ不自动等于全网θ_M（P′保）；同ψ仍r/N分配可安全M^-184。待推。
tail66新40门已成待root读：真实局部wave平方根/Sylvester完整高锥，diag无order−2但chronological硬切口项保，只有≥2N两侧另付order−4；两physical图、mean/weak源齐。局部Lorentz坐标不能免费同时固定两端slice/period/return。低scaled middle/nonradial簇、真source→port仍未成；改对象备选未启用。
完整model连接/state→geometry恒等式已证，true θr−τ和所有残差/mean/跳保。仍须同精确闭G全域|G|≤511/400、σ>4/49、|κ|≤12、κ+≤196/27、真腰ρ=.01、真平帽a≤7e−6/z±[.9,1]、p5峰145..148四marker。腰Δc=.129705423092539…、2ρ/15与外tube已有条件预算；所有真输入成才授held/D>.05024347、reach/D>.03195015、H及含反射δE。
全补逆、真ν Schur非零、非线性F=0、精确闭族及全几何均未完成，持续执行open下一项直至README完成。










最新已单推实际结论：results/R119-supplement-actual-local-wave-square-root-and-complete-high-cone.md。
