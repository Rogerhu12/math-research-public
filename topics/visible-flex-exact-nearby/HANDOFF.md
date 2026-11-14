# 交接：同一个可见振幅的精确闭等距族

visible-exact-astra-ac0d，2026-11-14 07:40 UTC。主目标未完成；持续执行，不因时长、阶段或等待收尾。

## 正式迁移、规则与同步

唯一工作仓库现在是 Rogerhu12/math-research-public，路径 topics/visible-flex-exact-nearby。新根与题README均全文已读；根blob 1d05db9ebc859a5fd9a8ef773ab05ef1e9de0598，题blob 7e2b93d66ee7dc61b0962cd6f2545dceb01daf12。
最后真实pull --rebase：2026-11-14 07:41 UTC，SHA add08fd0e2839e4d7cf095da3f7c5371f8918232；根/题README blobs未变，差异检查完成。
每次push前真pull；至少每小时pull；每次检查两README，只读变更并立即执行。每结论独立commit/push；非FF立刻pull --rebase再推成功，不force。自身公开repo Actions已允许；旧math-research-ci/ci-queue停用，不再派发。PAT只瞬时CLI/env，不入文件/提交；公开输出无秘密。
自动审批曾拒公开目标；已重新核原repo6caee8bb根§14及题README首段明确授权转同owner公开repo并pull/commit/push，按用户要求立即执行新规。本条无私密数据或凭据。
root独占Git/H/open/results/log；代理只写自有新文件。H<10KB、md<100KB、open约30KB、单件≤5MB/>1MB压缩；大可重建数组留scratch；不freeze、独审、冗余核验；不动根LOG。只提交明确路径。
新repo本地 /workspace/scratch/ac0d699811ad/math-research-public。旧math-research目录只供运行中进程读取原源/依赖，不再编辑提交；旧HEAD f5e4843b含未推cap96，旧origin/main 6caee8bb正式通知迁移，根/题差异均已读。新种子480a4313逐blob比对含全部旧已推结果，仅缺cap96五件；32个待推/恢复输入原样搬入新树，未重跑已成门。旧H归档 notes/2026-11-14-handoff-before-public-migration.md。旧stash唯一κ=M²/B修订已由新69提交接续；不pop旧树。
临时发布助手 /workspace/scratch/ac0d699811ad/git_checked_publish_public.py 每push前真pull并将新SHA写H，遇README变先停助手读差异后继续；publication助手逐条四索引。旧助手禁止再用。

## 对象、完成标准与重建

同一固定精确度量的连通闭C²嵌入族，C²连续。D=diamF0；闭H有内点、diamF0H≥.2D且逐点固定；未对齐held≥.05D；含反射E(3)非全等δE>0；每时reach≥.03D。phase单独是刚体旋转，须同族四个不同非共面静态曲率marker。
Eν=Eexp(νw)，w支(.05,.18)，a不变；ν/腰/deep/profile/marker变更均付同对象全费，不搬旧g0/R131。最终可选ν，但整个flex族固定同一ν。
最终candidate SHA ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413；6145nodes/M32/N512/[0,25/8]，α=6890507429876859/9007199254740992，ν=−2572625729470897/72057594037927936，η0=−7789843107295549/4611686018427387904。六stage全部原字段/位模式忠实复原已旧54f293b迁入，完整身份/路径见open与之前H归档。candidate在scratch replay-final-20261114/stage06。连续修复旧9239cfc：6143×65精确接口，腰不变，offset A0<3.861e−18/A3<5.635e−16/mean<5.842e−21；定义SHA440866a3…，原/修复中心不混。
Python3.12.14/np2.3.5/scipy1.17；PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps含flint.9/SymPy1.14，BLAS/OMP1。

## 已成消费者与全局缺口

完整原记录及恢复方法见open §§1–7和各native。mean7721/6143 Γ<1.013237；strict3071/2549正向H1初值10.124885/源10.240174，reverse404.222565/408.729241；rootpiece15/fold27源.028915503/graph.001826455；positive4650/N97反馈order0 .303291679/order1 .788277736；negative-height反馈.711062297。ν5M1156/864全η源1.964956、signedG625.523019，仅配对非全逆。
完整physical cap [.9,R]全η/1346交/full Fourier/两mean：χ<.820523、逆5.571744，ordinaryB/C12.725633/22.179140，div18.407084/41.065564。完整moving-cap桥1341盒7门旧7153691：追加χ.00384016121<1/250，moving普通L2→physical7.220627→moving L∞L2 294.706166，mean/Hessian/repair费齐。
完整残差旧3517ca89：7296闭盒/6143接口，原producer不改；右7271零η域拒原失败保，最后25盒全η另真算成功，merge只补2617缺接口。native SHA6f52030b…三binary片；RU/RV A0<2.267544e−7/4.159086e−7，A1<8.646130e−5/1.529992e−4，L2<4.201205e−8/8.194504e−8；vgap>.0901531879/mean>1.0687328018。交集η=η0，不授整个邻域。
角完整旧a768e67：7722闭盒/6143跳/full circle/mean，native SHA7a3dd2c1…四binary片；|Fφφ|<5.970523，|Nφφ|<4.646383；512角插值位置<7.024610e−6/法向<5.466695e−6。保model anchor，不授真帽world anchor/非线性解。

## 当前原生计算与准确继续点

1. root径向directed session19425，/workspace/scratch/ac0d699811ad/geometry-verified-20261114/attempt04.json.gz；原源仍从旧目录读，勿改旧源。07:34约86/141blocks、5503/8966步；完整exact角点/operator norm/全η/真实单侧germ/三阶Taylor四阶余项；逐block原uint64回接。attempt01域拒/02float选片/03Wiener过粗全保。新树保verify_moving_geometry_grid.py SHA3347e061…与directed_jets b93fa88a…。61块/3903格准确快照SHA36f3185d…与tensor SHA706750a8…本条发表，后续仍需完整native。
2. root完整mesh实际正常0/198.985s，141块8966格×512×8，全36,724,736分离向量；native SHA5ed344a8…，mesh R<1.275559740657、框架support>.901284727159、全凸包距>.129668021172。已单推d4af39c6；新tensor消费者实际0/5.03s消费3903格，部分连续半径<1.275713423；径向理论/61块native已推a9c3a233，继续增量消费；完整C0状态/δν几何预算实际0/25.05s、7722盒已成：frame15.736315/.304809、position30.196406/.105999，曲率141.332651/3.988052；ε≤1e−3/τ≤1e−5且锚点另付。证明及native已成，本条推；未授实际解。
3. newton双regular q/ψ均全部6144块193态，完整FFT2.590797e−11/3.166507e−11已旧1c7a7ec迁入；q/ψ fullindex SHAed42a71d…/c509df40…，均含所有outer Robin及mean，不是全inverse。body v2 session56409实际exit1：7721系数及双完整均值已成，第0残差Finite/int类型拒、0残差行；原native/source/process保。v3 session11395修scalar并复用全部三前缀；477行显示宽独立包络过粗，改联合相关余项。ν双积分53534和物理边界v4 75591并行；输出regular-head-consumers-20261114/body-native-v3.json.gz。旧plain/gzip零行错误与旧b4 FFT1e14失败均保。
4. cap96原660块恢复后完整normal0/223.699s，FFT5.705156e−15。cap96五件本提交从旧未推HEAD迁入；661×193×96states及左右derivatives在/dev/shm/visible-exact-cap-DN-20261114/73c2f7cbe033dbd7c7ba789217d4bebd26f0486fb7129be898457818429c09b0/matrix-RHS。SIGBUS−7原process/175件SHA复制/预分配全保。v2首宽片ordinary weightedL2 B.048293197/C.037999149（原unweighted6.45/5.07），非全域。
5. 原宽片高j边界层λh~1.26；真正局部加密proposal session54988已normal0/680.24s：1296块/96列fullFFT6.861356e−15，source d82119aa…，scratch physical-cap-DN-refined16-20261114.json。首2闭片已真成B/C1.480231e−4/3.735972e−6；phase物理C128尾<1.757236e−14，session71138已全257态/128输入/1296块normal0/764.78s，原FFT6.475151e−15，H128×97实际12门39.71s全矩阵+mean+tail误差<6.518925e−12已推ab795771；再接完整连续残差；不把finite门当连续证书。物理coefficient jets旧202793ad全η/full∞尾首tiny/wide成功，非每盒已成。
6. phase真实完整两ray复域3071strict+root+mean+repair、10门正常0/23.959s；σ1/4输入ρ>.1639445393，P′−1<.334292688，P″<3.257207/P‴<57.403329；native SHA91f1a3e5…已单推2147abff。完整distributed adjoint phase-source proof已单推9d78f797，square Jacobian/真mean/端项齐。实际B128×193/full paired BC 11门已成，误差<1.496913e−11已推3078fefc；全Arb7阶scalar首germ6门已成，余169germ将自身Actions并行；cap6旧输出invalid不消费。不得用double拟合残差充真共轭。
phase旧817b4731/097ade1a：真response误差L2E0→C0≤1.273240，无q^-1；浮点qν Ω′≈.0202241584，direct+.0393631446/state−.0005213003/mean−.0186176859不可丢。目标二次CF根(612575−√5)/2228182、max partial7给四次单位根gap1/(36|j|)；尚无真rotation/β/j/ν Schur闭环，最终ν全族固定。

## 深尾与真正终局

旧53–68源/mean/weak/双图/Γ*列均已迁入；Nm<Cζe^-τ∞M M^-30960，τ∞∈(5921/16,2961/8)，Cζ=εδ8192^-485/4。68真实5函数补偿盒generator>2^-175000 M^-1891；root同原端口/参数网络inverse<2^175007 M^1894，好集>1−147/16384，Nm余29066幂，常数/源单位保。
69完整J0型49门已单推a25cbbb3，原native/proof SHA归档，κ=M²/B补明。70全negative pocket固定Γ型50新门已推519d4ea2；真X≤2^-1048576邻域有实际incoming，physical全部输出/两mean/两根图迹保。71真实Γ*完整fresh-support型59门已推41dd5ae2，72正保实际盒内径向补偿。随后仍有nonradial簇/ordinary source转端口/full inverse，不能静默换小球或profile。
最终同一精确闭G要|G|≤511/400、support>4/49、|κ|≤12、κ+≤196/27、真腰ρ=.01、平帽a≤7e−6且z±∈[.9,1]、p5曲率峰145..148四marker。全补逆、ν Schur非零、非线性F=0、精确闭族、全部几何均未完成，继续open下一子问题，不收尾。





最新已单推实际结论：results/R133-supplement-complete-Arb-scalar-jets-and-directed-high-Taylor-models.md。
