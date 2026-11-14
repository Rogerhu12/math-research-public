# 交接：可见振幅附近的精确等距解

visible-exact-astra-ac0d，2026-11-13 19:36（台北）。**持续进行，主目标未完成。**

## 授权、规则和执行

同一连通闭面、一个公共度量、C²连续精确等距嵌入族；固定有内点H，
diam(H)≥.2D、held≥.05D、含反射δE>0、每时reach≥.03D，全部同族成立才收尾。
根README授权及全部规则、本题README全文已读；已读规则提交 **384ec17e50802fed390b03a0c28ed6b3268b60e5**。
每次pull --rebase后立刻diff两README，若有变只读差异并立刻遵守、改SHA；
至少每小时pull。每条完成结论独立commit/push，推前pull；目前规则差异均为空。
非FF立刻pull --rebase再正常push循环，不force；令牌仅瞬时命令环境，不入文件。
根LOG不写；本题log每轮≤5行；H<10KB、md<100KB、>1MB压缩、单件≤5MB。
repo=/workspace/scratch/ac0d699811ad/math-research；python-deps在同scratch父目录，
PYTHONPATH须设它（flint0.9.0），OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1。
scratch/push_ready_conclusions.py及sync_push_native.py无令牌；队列1–21已成功（21由resume脚本恢复，勿重跑）勿重跑。
最近main=2707925ff63c7659f2cd058e4a6c7217d308972a。root独占共享索引/H/open/log/git；
三代理只写自己新文件。明确逐件add，巨大可再生缓存不得整目录提交。

## 当前真实腰分支

R125–R132为同一原始腰Cauchy分支，完整周期frame与原固定目标。
δ*=−7789843107295549/4611686018427387904，η∈[−10^-9,10^-9]；
不同δ可对应不同目标E，不能称此辅助参数为公共度量flex。
R129/R130全部原生恢复、原失败及高目标jets已推，详见既有结果/归档。
R131（f9018dffe9c）：d=p−q,U=dpθ,V=dqθ准确线性输运，C0管+gap
即可支付真实C1有限性，候选C1误差Riccati不再是必要延拓门。
R132（ce478374f96）四边不变矩形给[-.05,.05]精确嵌入。
R132精细补充（322a3bc9323）：300闭盒C0误差<.027567044、gap>.19312757486，
曲率<10.366510、φθ>.2696679160/J>.2902050414。曲率界只覆盖.05局部。

新R132 v2已实算169闭盒至[-.07,.07]：M<3.056754、m>.0018396089，
φθ>.24920909/J>.25763534；全角/全η/原primitive无限尾，已推594c70aa7bf。
外层只有粗曲率界478.527539，不能挪用.05的10.366510。
新target-only [0,.2]493真germ闭盒已完整完成750.715秒；不授.2存在。
target-only及v2完整source/native在R132 .07补充逐项列SHA。
它只读真系数/初始腰，不读候选或残差；末盒仅取交并保原完整界。

R134 root新定理：w=1/(q−p)消去能量中的实际速度角导数；E0只需候选
(P+Q)θ，加权梯度差EW三角线性增长，再以完整含mean Sobolev门闭合C0管。
phase_inverse独立核§1–5全部通过，10项symbolic原生全过；尚无长区间门实算。
定理已推535199c0582。新清分母producer先形成完整有限三次Fourier/径向多项式，
保target二阶余项后除C；3盒pilot已过，首盒rho0<3.12e−5/rho1<.006060。
phase_inverse已独立审全部清分母/余项/导数恒等式与degree7展开，无漏项。
新scripts/fourfold_codazzi_cleared_polynomial_residual.py冻结，完整150盒.05在跑；
3盒weighted门已过e0<.000109335031；独立R131最大值门更紧e0<6.16721e−8。

root长native session33750，输出notes/2026-11-13-Codazzi-cleared-polynomial-r05-v1-native.json.gz，
log=scratch/Codazzi-cleared-polynomial-r05-v1.log；source冻结，勿改。
磁盘满曾令queue21 amend失败；只删git明确garbage的7个tmp_pack释放3.04GB，
关闭本地auto-gc，未删真实对象/报告。resume后queue21全推成功；仍需注意磁盘。
3盒native/两种consumer已保存notes，正随R134清分母补充推；
.2新512角完整候选已完成（session39324），284片15.74MB在scratch，待无损分片入库；
前sessions25294/67935/91728/41457/89800/98695/4879已完成。新完整门尚未通过，不能预报.05成功。
.05候选/全部SHA/重跑参数在R130与H归档；成功source/report冻结。
旧150盒C0失败和新300盒C0成功均保留；后者无rho1，不能免费替R134输入。

## 并行任务与待推冻结文件

**newton_source / R133。** session54539运行真实旋转正帽[.239,25/8]，
原body公共germ及真[3,25/8] graft；wholeη/16模m4..64严格Riccati上下流，
另全m≥4共同区间。最近566盒到r≈1.275，无失败。
用R74真regular指数fee，保独立mean高度；不是非线性帽匹配。
同g0旋转Cref(.239)≈−.895112，候选sup|C−Cref|≈1.951，不能叫小扰动。
真regular回传Jacobi浮点q4≈1.05618等仅诊断。
真body+graft长BVP保腰低4/外端缺低4，首方向~4e198、24降步失败；
下一步全regular外端行，再于.239实际回传图付低4缺口。
旧31件失败bundle已推23172a9b508，23.3MB，manifest
notes/2026-11-13-Codazzi-two-end-failed-diagnostics-manifest.json，全部SHA已核。
旧body evaluator只在[-3,3]有效，绝不可外插25/8；全部未投影残差须保留。

**phase_inverse / R43,R46。** 全strict native完成215闭盒/168common spans，
准确[0,268136140016943/1125899906842624]，4503.07秒，failure=[]。
完整native/source/全部SHA在R46 complete-actual-strict-operator补充。
consumer16858已完成：全shifted Cauchy |s|≤10.5 <1.139199e251，
R2:E_s→E_(s+2), |s|≤8 <6.177244e502，ordinary源<5.598468e339。
五件已审并独立全consumer复跑，已推e5964b63b00；全强窗口极粗，非实用cutoff。
R43特征取消/大逆图已推6ce20026f71，δ2^-129强4/3<4.319813e41。
全实图至ρ=.00026/physical curved cut三件已推02934bbed3f，χ∈(.0002401600,.0002481884)，
|√ξχ′|<.024656888，完整两行/source/mean；不是constant ξ cut。
新全七场root→cut native得完整|V|<752814、|V−5050|<757864；
固定ξ复product halo/真实L2 Volterra<.023683236五件已审、独立复跑待推；
root纠正Vξ的域只在实ξ∈[0,1/4000]（V仍整个halo），轻consumer已重跑。
代理正在付完整高阶/两行/普通源及cutoff-scaled范数，不冒全返回。
L2不能代全Hs强余项；随后cutoff权(1+|lag|/N)^S保完整head来收紧常数。

**tail_connector / R119。** balanced充分标签域224，state<2^-447X224，
物理C²<2^-428X224；真实hodograph主项(bI+cB0)∂ξ，c−1二阶非零。
真divergence/density转向额外平方能量费<2^-427X已推；真regular→Codazzi
已推30ce0808065，有限L反射/mean/高度输出全保。真正型两端弱DN/ordinary源
已推0dc35493297，更新相对费<2^-430X；全层强Airy迹/源比较仍欠。
新负band度量参数三件42门已审推ec33329c7a3：每层两下降ramp各γ，|γ|≤2^-16，
明确新最终度量族gΓ；κ_j=2^-25 sqrt(η_j/Δ_j)，真实Θ′正，非径向误差/κ_j²
余量δ_j^(59/256)可和。旧regular第四轴/R11/R74/connector/双bump需重调。
统一chart三件28门已独立审，root所提深层uniform需规范指数已在(U.24)补全：复|γ|<2^-15保R72/R115全频/ordinary源，
DΓXβ<2^18||a||β，全X/C²连续，不免费转移旧regular线。
实际内部负段的联立KAM三件42门已完成；newton独立核全参数/全模/mean，
补齐当前h处参数导数复合后通过，待逐条推。Γ*(a)相位轨道不变；不冒mixed逆。
代理继续新Γ下真实第四regular轴、connector/双bump共同选择和正型强端口。

## 全局缺口与历史

旧P_hat已有R101真返回共轭、R102全频算术、R104除数>7/(110j)；
完整b−β/强R*/有效cutoff、全低高Schur/Airy/ports/ordinary源Kwire及邻域逆仍欠。
P_hat为type-fixed修改，真P_hat−P/ω必须保留；边界高逆不是全体源强逆。
R105/R121真帽、R106全550forward及原source下界均已恢复，详见results/open。
新Cauchy须自己付跨根/正帽/尾/mean/regular全matching，不能借旧帽证书。
两路线均需最终公共度量、C²收敛/连续选择及同族全部几何。
R112平帽轴向平移/R114修复/R115chart/R117重建不授任意普通C²邻域。
R69/R78/R79/R123几何及四个不同非共面标记须同一最终族；整像相位若仅
刚体旋转则δE=0，不能冒含反射非全等。做完子问题接open下一项。
完整历史/重做命令/收据在results/log和H归档：最新
notes/2026-11-13-handoff-before-cleared-polynomial-run.md，之前before-r07-and-full-strict、before-r132-refinement、
before-r132、before-long-Taylor-run、before-joint-Taylor、before-r005-complete等。
open旧全文在notes/2026-11-13-open-before-linear-degeneracy.md。
不能以时间、阶段报告、失败诊断或等待计算结束主任务。

## 本轮后续已完成结论

- 旧31件两端失败bundle已按manifest逐件SHA核并推，完整未投影源/mean/低4输出与NaN错误撤销保留。

- R133旋转参考/真regular帽线/腰返回8件浮点包已核全部依赖并推；m4近临界只作诊断，native与非线性帽继续。

- R119统一Γ尾chart已审推；root追问的深层全m规范费已显式补齐，28门复跑通过；不移植旧regular轴。

- R119内部负段全参数/全模KAM已两路审推，当前h处复合已明确，42门复跑；Γ*(a)相位不变，外cut/Airy幅度/regular重调仍欠。

- R134清分母完整代数/真目标余项及3盒两种误差门已审推，R131 e0<6.16721e−8；完整150盒.05 session33750继续。

- R43完整根势/固定canonical复域及全频height收缩已审推；Vξ域经root校正后独立复跑，完整强frame下一条。

- R43全根两行/ordinary源及不变原B的scaled强4/3已审推、独立全consumer复跑；非恒定physical graph与strict同尺度接线继续。
