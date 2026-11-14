# 交接：可见振幅附近的精确等距解

visible-exact-astra-ac0d，2026-11-13 19:17（台北）。**持续进行，主目标未完成。**

## 授权、规则和执行

同一连通闭面、一个公共度量、C²连续精确等距嵌入族；固定有内点H，
diam(H)≥.2D、held≥.05D、含反射δE>0、每时reach≥.03D，全部同族成立才收尾。
根README授权及全部规则、本题README全文已读；已读规则提交 **e5964b63b00be0ddb2bc49f6906f7b696d355750**。
每次pull --rebase后立刻diff两README，若有变只读差异并立刻遵守、改SHA；
至少每小时pull。每条完成结论独立commit/push，推前pull；目前规则差异均为空。
非FF立刻pull --rebase再正常push循环，不force；令牌仅瞬时命令环境，不入文件。
根LOG不写；本题log每轮≤5行；H<10KB、md<100KB、>1MB压缩、单件≤5MB。
repo=/workspace/scratch/ac0d699811ad/math-research；python-deps在同scratch父目录，
PYTHONPATH须设它（flint0.9.0），OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1。
scratch/push_ready_conclusions.py及sync_push_native.py无令牌；队列1–18已成功勿重跑。
最近main=6ce20026f7124d6122f8b335d43697ededc0aa70。root独占共享索引/H/open/log/git；
三代理只写自己新文件。明确逐件add，巨大可再生缓存不得整目录提交。

## 当前真实腰分支

R125–R132为同一原始腰Cauchy分支，完整周期frame与原固定目标。
δ*=−7789843107295549/4611686018427387904，η∈[−10^-9,10^-9]；
不同δ可对应不同目标E，不能称此辅助参数为公共度量flex。
R129原[-.005,.005]168闭盒、全部恢复收据及原失败屏障已分别推。
R130高目标jets/相关混合Taylor残差和完整.05有限候选已推。
R131（f9018dffe9c）：d=p−q,U=dpθ,V=dqθ准确线性输运，C0管+gap
即可支付真实C1有限性，候选C1误差Riccati不再是必要延拓门。
R132（ce478374f96）四边不变矩形给[-.05,.05]精确嵌入。
R132精细补充（322a3bc9323）：300闭盒C0误差<.027567044、gap>.19312757486，
曲率<10.366510、φθ>.2696679160/J>.2902050414。曲率界只覆盖.05局部。

新R132 v2已实算169闭盒至[-.07,.07]：M<3.056754、m>.0018396089，
φθ>.24920909/J>.25763534；全角/全η/原primitive无限尾，正逐条推。
外层只有粗曲率界478.527539，不能挪用.05的10.366510。
新target-only [0,.2]493真germ闭盒已完整完成750.715秒；不授.2存在。
source fourfold_codazzi_target_coefficient_cover.py已推；新native
notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz；consumer
scripts/fourfold_codazzi_invariant_rectangle_v2.py，报告
notes/2026-11-13-R132-invariant-horizontal-r07-native.json.gz。
它只读真系数/初始腰，不读候选或残差；末盒仅取交并保原完整界。

R134 root新定理：w=1/(q−p)消去能量中的实际速度角导数；E0只需候选
(P+Q)θ，加权梯度差EW三角线性增长，再以完整含mean Sobolev门闭合C0管。
phase_inverse独立核§1–5全部通过，10项symbolic原生全过；尚无长区间门实算。
proof results/R134-weighted-error-energy-and-Sobolev-continuation.md；
source fourfold_codazzi_weighted_error_identities.py/native同日R134-weighted-error-identities。
下一步付直接S1/W0/W1/加权残差并实际跑屏障；不能停在方法。

root sessions25294/67935/91728均已完成，无长native在跑。
.05候选notes/2026-11-13-codazzi-dense-r005-n512-candidate.npz.gz，75片/512角，
SHA 1fdb86b3f959cd3137cf06bdbb37637643a1a56143152c7e26b622d7b353dd81。
文件名r005实际.05；producer --right1/20 --angles512 --max-step.001。
完整compact150报告有rho0/rho1；旧C0门在row111约.038失败已保存。
成功C0-only300报告没有rho1，不能免费消费为R134源。旧v4备份在scratch；
所有成功source/report冻结，完整目标/原primitive/候选尾/germ逐项核SHA。

## 并行任务与待推冻结文件

**newton_source / R133。** session54539运行真实旋转正帽[.239,25/8]，
原body公共germ及真[3,25/8] graft；wholeη/16模m4..64严格Riccati上下流，
另全m≥4共同区间。最近566盒到r≈1.275，无失败。
用R74真regular指数fee，保独立mean高度；不是非线性帽匹配。
同g0旋转Cref(.239)≈−.895112，候选sup|C−Cref|≈1.951，不能叫小扰动。
真regular回传Jacobi浮点q4≈1.05618等仅诊断。
真body+graft长BVP保腰低4/外端缺低4，首方向~4e198、24降步失败；
下一步全regular外端行，再于.239实际回传图付低4缺口。
旧31件失败bundle已冻结，23.3MB，manifest
notes/2026-11-13-Codazzi-two-end-failed-diagnostics-manifest.json，待显式逐件推。
旧body evaluator只在[-3,3]有效，绝不可外插25/8；全部未投影残差须保留。

**phase_inverse / R43,R46。** 全strict native完成215闭盒/168common spans，
准确[0,268136140016943/1125899906842624]，4503.07秒，failure=[]。
notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz，SHA
8a97d6780955b94f3f96ab7cd8c8d4e518f291cd04e0903505c03e2abe176788。
consumer16858已完成：全shifted Cauchy |s|≤10.5 <1.139199e251，
R2:E_s→E_(s+2), |s|≤8 <6.177244e502，ordinary源<5.598468e339。
五件冻结待审推；全强窗口极粗，非实用cutoff。
R43特征取消/大逆图已推6ce20026f71，δ2^-129强4/3<4.319813e41。
全实图至ρ=.00026/physical curved cut三件已审复跑待推，χ∈(.0002401600,.0002481884)，
|√ξχ′|<.024656888，完整两行/source/mean；不是constant ξ cut。
新全七场root→cut native得完整|V|<752814、|V−5050|<757864；
5050 shifted-Airy真参考给L2 Volterra有望<.024，正付固定ξ复域和全部源/两行。
L2不能代全Hs强余项；随后cutoff权(1+|lag|/N)^S保完整head来收紧常数。

**tail_connector / R119。** balanced充分标签域224，state<2^-447X224，
物理C²<2^-428X224；真实hodograph主项(bI+cB0)∂ξ，c−1二阶非零。
真divergence/density转向额外平方能量费<2^-427X已推；真regular→Codazzi
已推30ce0808065，有限L反射/mean/高度输出全保。真正型两端弱DN/ordinary源
已推0dc35493297，更新相对费<2^-430X；全层强Airy迹/源比较仍欠。
新负band度量参数三件42门冻结待审：每层两下降ramp各γ，|γ|≤2^-16，
明确新最终度量族gΓ；κ_j=2^-25 sqrt(η_j/Δ_j)，真实Θ′正，非径向误差/κ_j²
余量δ_j^(59/256)可和。旧regular第四轴/R11/R74/connector/双bump需重调。
统一chart三件28门亦冻结：复|γ|<2^-15保R72/R115全频/ordinary源，
DΓXβ<2^18||a||β，全X/C²连续，不免费转移旧regular线。
代理继续所有负型分量和Γ同时的真实return/KAM，不逐层假定其余Γ固定。

## 全局缺口与历史

旧P_hat已有R101真返回共轭、R102全频算术、R104除数>7/(110j)；
完整b−β/强R*/有效cutoff、全低高Schur/Airy/ports/ordinary源Kwire及邻域逆仍欠。
P_hat为type-fixed修改，真P_hat−P/ω必须保留；边界高逆不是全体源强逆。
R105/R121真整帽六块逆<90.583064，R106全550forward已恢复推；
R110选定源下界>31.557、R120原腰非mean源>.604740，不能默换对象/源。
新Cauchy须自己付跨根/正帽/尾/mean/regular全matching，不能借旧帽证书。
两路线均需最终公共度量、C²收敛/连续选择及同族全部几何。
R112平帽轴向平移/R114修复/R115chart/R117重建不授任意普通C²邻域。
R69/R78/R79/R123几何及四个不同非共面标记须同一最终族；整像相位若仅
刚体旋转则δE=0，不能冒含反射非全等。做完子问题接open下一项。
完整历史/重做命令/收据在results/log和H归档：最新
notes/2026-11-13-handoff-before-r07-and-full-strict.md，之前before-r132-refinement、
before-r132、before-long-Taylor-run、before-joint-Taylor、before-r005-complete等。
open旧全文在notes/2026-11-13-open-before-linear-degeneracy.md。
不能以时间、阶段报告、失败诊断或等待计算结束主任务。

## 本轮后续已完成结论

- R132 v2 的[-.07,.07]真实嵌入及493盒[0,.2]独立目标覆盖已审推；外层仅粗曲率478.527539，继续实际C0管与帽匹配。

- R43完整实根图及physical curved cut已审、独立复跑并推，保全部两行/源/mean；root→cut强传播继续。

- R134完整加权能量/C0合同已推，独立审与10项准确符号复跑通过；不冒新长区间认证，继续实际相关残差输入。

- R46完整215盒strict字段及全强算子已审推，root独立consumer一致；R2<6.177244e502极粗，root/Airy/全返回与有效cutoff仍欠。

- R119新最终度量参数族/零标签真旋转导数已审推，42门独立复跑；统一chart及联立非径向KAM继续，旧regular/connector/双bump须重选。
