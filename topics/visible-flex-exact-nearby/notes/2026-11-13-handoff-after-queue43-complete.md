# 交接：可见振幅附近的精确等距解

visible-exact-astra-ac0d，2026-11-13 17:18 UTC。主课题未完成，持续研究，不作阶段收尾。

## 规矩与同步

根README全部授权/规矩及题README已读；已读规则提交 **280be22459af8d11ac6e81939bdbd592d5a1f35a**。
每次真实pull --rebase立即diff双README，有变只读差异照做并记SHA，至少每小时pull。每结论独立commit/push；非FF立即pull/rebase/普通push循环成功，不force。PAT仅瞬时CLI，不写文件/提交。
root独占Git/H/open/results/log；代理只新文件。根LOG停写。H<10000B，md<100KB；open尽量<30KB，>1MB压缩，单件≤5MB。逐文件add，不能stage恢复cache/半成品。README13取消强制freeze/独立审/逐字归档/重复重跑；完整证明与必要严格运算完成即推，只为具体数学风险检查。
repo=/workspace/scratch/ac0d699811ad/math-research；topic=topics/visible-flex-exact-nearby。PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps，OPENBLAS/OMP=1，PYTHONDONTWRITEBYTECODE=1。
scratch push_ready_conclusions.py逐条写H/open/results/log；sync_push_native.py真实rebase/diff规则/normal --no-thin push。helper运行时勿改H/open/index。H guard前会先写open/results，失败须保已写内容继续同pending。
部分克隆promisor/blob:none，gc.auto=0/maintenance.autofalse/push.negotiatefalse。旧preload8083已主动exit130/隔离index清，勿重启全hydrate；陈旧重复tmp pack已确认正常副本后删，正常pack/refs未动。
queue1–42已全推；42末7402e52a5db671a6bbf873e6440199ee04f028e2。完整旧H在notes/2026-11-13-handoff-after-queue42-complete.md，再链41/40/39等；open完整历史在notes/2026-11-13-open-history-before-physical-tail-matching.md，再链before-full-r02。已完成不重做。
queue43正登记：根完整物理两迹/反射证明、tail真固定t两端口、真帽解析衰减、Bessel Q完整mean范数。随后保存v12/v13实际拒绝及继续右端联立。

## 同原腰/目标的真实五分之一已闭合

原E=完整|Fr|²角平均/a不变；δ*=−7789843107295549/4611686018427387904、wholeη±1e−9。不同δ/ν/腰数据/深profile是新最终候选，不能转授旧g0的flex。
原283盒cubic残差、完整BC及s10权原字节不变，输入已推manifest68efe2a4…。全部579闭盒/4096角：原五管1/200,1/100,1/50闭合，best真Riemann误差<.003887037041、gap>.21117001608、k>.53198969829、真角导<7561.596192；1/500 row537和1/16 row528失败保留。
完整native notes/2026-11-13-R131-positive-weight-complete-r02-C0-native.json.gz SHA0e04c11352951a00cd51c1af7e8b3c9014b9adfd6fb2432d181d7ac1ba2bb123。五片并：0..95、96..192、193..385 complete；386..578原98893在187保存行后exit137（原因未明），原false不改；新573..578六行57918正常complete。v4核实际保存生命周期/准确partition，只消费完整行，同z/真梯度从原腰连续不重置。
真几何96758也正常完成；R131-supplement-one-fifth-exact-embedded-annulus.md及sign_geometry.py全真实p/q闭盒积分frame，[-.2,.2] φθ>.14711768015、J>.09095483284、κmax<8.099019。部分p/q异号未证时只用一般界。以上均已推q40/41，不是闭面。
根新R133-supplement-full-physical-trace-matching-and-waist-reflection.md是完整条件定理：实际cap全B,C（含mean）同物理orientation匹配则GC径向重建继承全周期/holonomy；腰全部B=0及a′=E′=0给C²平面反射；嵌入/reach另证。实际tail原height至B,C公式/Γ移动切口/两mean保留。不是已构造整体。

## newton_source：真帽外接口与新ν有限主体

M128 α=.65/ν=−6837290349363917/288230376151711744的651节点完整finite BVP成功；compact metric支持(.05,.18)，属新ν度量。浮点全曲率4.117097272，held采样.04169097不足；α.70只是中间，预计需约.78及真实几何。
α.70 v7四accepted/850节点AS1536MiB exit70；v9/v10拒绝已推；v11主动Ctrl-C exit130/零accepted已推q42。v12正常exit0但ILU drop1e−5/fill4因Factor exactly singular拒绝，无GMRES/accepted，不是完整J奇异；68.03秒、RSS459908KiB。
v13 core16-b0 LU成功3.482M nnz后完整GMRES768步info12，真相对残差1.001950438失败，零accepted/RSS369524KiB/280.73秒。当前唯一新session36540：同静态v13只把高模预条件band改1，完整FFT/后向残差/ν列/非线性门不变。v12/v13重复大候选可由原v9完整输入重建，保存小索引/真实过程，不重复推大shards。
真[1,25/8]中心帽全935盒/92join/11868精确jump：误差<.000054079035、Cgap>.1690329008、θθ<.183600040。开放内c A0球1e−5、四输入列/两mean、全非零频率逆<1.212135；全M128内c差<3.691e−9，B残差<5.941e−6/mean c<7.485e−7未消。
真[.9,25/8] v5全1988盒/101join/13029jump已推q42：一次细化ρ<.000362924、L<.717868、真误差<.000258811；开放内c球1e−5/逆<2.514346，M128内c<2.431e−10、B<2.291e−5/mean c<6.130e−6。新内端固定数据所得新解不免费同旧r1解。
强解析入口：同实际r1驱动解选d_R=B0_R=c0_R=0，从L=1.5至R=25/8，W_m=(a/aL)^(μ+τ|m|)。μ3/2、τ1/128、ρ.0004全收缩<.464506，与旧真解由同未加权收缩识别；外宽>.06901529、实际Σ e^(σ|m|)(|B_m|+|c_m|)<7.035e−10。μ4/3备选宽>.13803/界3.067e−9；不是实际regular尾。
代理正在将真正R119长段C_R→f*全频非线性逆、B Robin与两mean完整联立正帽；保fB参数/另一端F(a,f*)，不把zero外端驱动解冒真实regular。full body跨根/两迹仍欠。

## phase_inverse：同原返回强界

旧原p∞/四锥两根/mean/regular完整高inverse N=2^2108、κ<.014238673、inverse<15.941269，−4/3≤s≤0；head复维2^2110未组装。ordinary/weak全源R45/46已推，zero final head高particular不等于physical低端口0。
q41全Airy换架在原5050/原B和source下给两行正逆含独立mean<4.203925521；q42同原七场/完整两侧域/wholeη/全尾保留，相关二阶及两signed对common flow给|V|<22575.093446。负侧5050完整height Volterra<.000863285，正侧仅零双Dirichletcoercivity。
新Bessel Q只用最终-v2.json：完整±2窗、两方向/adjoint和mean，physical19.5154/graph1.70308/strict1039.441/final326.441，最终base3.099735；原字数全部coordinate乘积<1.405e17（旧1.893e68）。解析cross-cone不能免费改善。
代理已实际把D25原因子数接回半word，Tg<2.282e23/R*<5.137e165，cutoff降2^1682仍巨大；proof/source/native待发后登记。完整RS≈2.9831e130保留，继续真实H1源/主相位与严格高低Schur，不称全逆。

## tail_connector：新实际尾完整网络

8193后K2^128/ζ131是新最终候选；前缀129..8192和两全局逆幂保留。全标签/mean/C²平端、raw/source/新第四stop/好集已推；条件X≤2^-262144不是已完成非线性输入。
q39真根joint CK以原实解全胞元角余宽先入实段B_R并同1/64唯一性识别CK，不循环假定径向解析；四根全mean/density/height/weak Piola齐，same-Hs合计<2^164424X。
新固定t两端口证明/源/native已齐：有序特征不除有符号位移，真density主部保两不同diffeomorphism；同Hs相对<2^256 b²n，四根全前缀<2^164804X≤2^-97340。raw h/p、branch/normal/shear/mean、弱端点负荷均保；任意各向异性源不免费升窗。
代理继续strict原t密度相对流/全返回与新KAM；比较带primitive的(C_S−C_S0)D^-1，不声称bare composition同Hs接近。

## 真正终点

D=diam F0(M)；闭H有内点、可不连通，diam F0(H)≥.2D且逐点全t固定。全像未对齐Hausdorff held≥.05D；E(3)含反射的δE>0；全t reach≥.03D。
相位G_t=R_(πt/4)G S_(-πt/4)固定旋转平盘，但像单独仅刚体旋转；须同族加四个不同非共面固定曲率marker（R17及2026-11-12-current-family-fixed-curvature-marker-budget.md）。新ν/帽/尾全几何须重付。
尚未同一精确度量、连通闭C²嵌入族及其连续性、全部mean/真实tail matching、held/δE/reach一齐闭合。做完子题接open下一项，不因阶段/时长/计算失败停。

## 本轮后续已完成结论

- queue43/R133完整物理两迹/周期GC重建/腰C²反射证明完成；实际全尾、主体和嵌入假设仍须实现。

- queue43/R119真根固定t全两端口已证/46门；四根完整相对<2^-97340，strict全返回及新KAM仍待。

- queue43/R133同一实际正帽外端解析衰减已证，宽>.06901529/全B+c<7.035e−10；真正periodic尾全迹联立继续。

- queue43/R46原全坐标密度Q的±2窗/mean/adjoint已证，积<1.405e17、final base<3.099735；完整返回另消费。
