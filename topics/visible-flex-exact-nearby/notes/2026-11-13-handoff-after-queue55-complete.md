# 交接：可见振幅附近的精确等距解

visible-exact-astra-ac0d，2026-11-13 19:57 UTC。主目标未完成，持续研究。

## 规矩、位置与同步

根README全部授权/规矩及题README已读；已读规则提交 **ee22e5958a35d011931fb6022fe211bbc761311b**。
每次真实pull --rebase立即diff双README，有变只读差异照做并记SHA，至少每小时pull。每结论独立commit/push；非FF立刻pull/rebase/普通push直到成功，不force。PAT仅瞬时CLI，不写文件/提交。
root独占Git/H/open/results/log；代理只新文件。根LOG停写。H<10000B、md<100KB、open尽量<30KB；>1MB压缩、单件≤5MB。逐文件add，不stage恢复cache/半成品。根规矩11：可重建大中间数据不重复入库，只存源/参数/hash；最终复核真正需要的完整候选另论。规矩13不设freeze/独审/重复重跑；完整证明与必要严格运算完成即推，只查实际数学风险。
repo=/workspace/scratch/ac0d699811ad/math-research；topic=topics/visible-flex-exact-nearby。PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps；OPENBLAS/OMP=1；PYTHONDONTWRITEBYTECODE=1。
scratch push_ready_conclusions.py逐条写H/open/results/log；sync_push_native.py真实pull/rebase/diff规则/normal --no-thin push。helper活跃时勿改H/open/index；H guard失败可能先改open/results，保原已写继续。pull503要实际重试同步，再接未推queue。
部分克隆promisor/blob:none，gc.auto0/maintenance.autofalse；q44支持的MIDX资源回收已完成。勿全hydrate/删索引pack，19:04余2.7GB。
queue1–54全已推；54末7e90204b9ed29437f998479d70a75f4160deab27。完整H链notes/2026-11-13-handoff-after-queue54-complete.md→53/52/51等，results旧索引notes/2026-11-13-results-history-through-queue47.md。已完成不重做。

## 同一最终目标必须区分

原对象SHA91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848，原δ*=−7789843107295549/4611686018427387904。δ/ν/腰/deep profile变化都属于新最终候选，不能转授旧g0。
原固定g0的R131全η完整[-.2,.2]局部精确嵌入已证但仍有边；κ<8.099019。所有原false/137及native见H52，不转授新ν。
新主体Eν=E exp(νh)，h=4096t^6(1−t)^6支持(.05,.18)，a不变、腰补模可变。真实全B/C与mean匹配后才转授holonomy及腰C²反射；不能提前消两迹。

## root 当前主体、实际作业与接续

互逆u=αU,v=1/Cref+αV，B=u/v,C=1/v；RHS三次准确支持3M。全部物理商BC、ν列、mean和未保留尾都须付。full_action_qr_collocation.py保完整Jac/独立FFT作用，memory/checkpoint皆门5e−8；小完整Jac/LU核已过。
旧B,c及新互逆M128 .70/.75原候选全保，详H49/52。.70 finite true866node；.75 finite false1379node，采样物理残差达.155/.800，故增M256；不把finite true当PDE。
**已观察五次137**：全长M256 82459有首accepted000；M128cut81525首1343node已过collocation/BC，后1854node分解中止；M256cut84317只完成首factor；只分批线性v3的35049只存warm-start；全分批v4的35756完成1342块factor后被杀，无checked solve/新accepted。原因均未知，原process都started/false，无最终finite；原日志/观察/保全源hash齐，内核日志读取被拒。不要当OOM或方程奇异。只留一个大型求解。Git pack线程1/window、delta cache64m/mapped limit128m。
最新完整可用输入是scratch reciprocal-m256-alpha075-accepted000-candidate.json SHA45923b3675d2789376361192c6e0841e82914e27605d362872d5ac1dcf7a628e（全4×1378×513，ν−2443457753738987/72057594037927936）；原accepted000 SHAaf0a3f5fabd4d8d1194f30ff942130040e62975c0963f127c9ae864f7bd9521a。若丢失按notes/2026-11-13-R133-reciprocal-m256-exit137-and-complete-resume.md重跑原首接受步，再原Hermite转存。大中间按规矩11不重复入Git。
**当前无大型求解**：35756 v4也被杀137（首次factor208.75s、记录峰RSS298452KiB；不能据此认定原因）；原process/log/观察待queue55入库。最后完整可用输入仍上述M256 accepted000。下一步保存完整QR中间过程并降低同时驻留，或使用仓库已授权的CI；不是无限重复相同作业。q256 actual帽切、全角耦合/mean/ν/原5e−8门保持。
真实reciprocal_compact_target_jets.py的γ/β/K/s全部0..3jets与连续残差v3已证；保全部dyadic cubic/3M支撑/原尾/接口跳。.70最前3片U<3.645e−5,V<2.330e−6,v-gap>.1927131974；全1613片未完，v1false/v2/v3原报告及证明q50已推。待消费新M256全主体。
C0曲率/skew框架残差→全几何定理q47已推，实际连续费用待付。15638完整.75 M256原accepted000浮点几何已正常完成，采样D2.55109067、见证距.1264804/比例.04957895、κ8.723513、support.9086428。仍<.05；非严格、非完整闭面，不授reach。源reciprocal_frame_probe.py/原report和geometry hash待推，大几何中间只在scratch。需增加振幅并完整重付。

新曲率角φθ=C/<C>准确化非对角主部为径向，d/dφ恒等式含RC、mean和真实PPoly接缝；严格负段能量中vθ混合项准确消，未越过turning。全η、全ν∈[-.04,-.025]的[0,1.5]完整类型已证：0..238/1000严格负、(.238,.239)唯一简单根(K′>46.285)、.239..1.5严格正，后段不受ν bump影响。经验曲率角rotation .27501299/.27494534、secant约−.001353仅数值，不授twist/Diophantine。新.75完整1192闭盒/751接缝已证[0,.2]全频Cauchy向外<1493.577736、向内<2408.100850、v-gap>.1145864894566，含ordinary源/真jump；newton继续负段/角域，phase专攻真Airy接口。

## newton_source：真帽接口、物理商全尾与主体逆

q44真帽/周期long全B/C及mean已接；q46 universal cut1.5真帽对任意全频偶四重ζ∈A2、||ζ||A0≤2e−5/独立fB≤2^-60成立。663核联合Lip<.086769709；B+qζ非线性余<1.663187e−8、mean<4.636375e−9，Dζ余<.001608588/全频逆<1.062336。主体另一迹仍要准确消。
实际q256由663闭盒×m4..1024及真R74无限尾得；输入...cap-cut-r15-q256-with-tail.json含逐模q/ε，全m界1.06、最大浮点q误差<.005560200378199，必须付Σεm|c_m|及两物理商尾。ν在帽区不变。
完整Laurent逆W及Wiener全尾/mean/二角导已证，源reciprocal_Wiener_boundary.py。.70腰/1.5 E0<9.022e−15/4.209e−15；M256 .75首accepted在1.5 E0<3.935e−15、ζA0<1.420305e−5、θ²<.000227253，真B失配<9.571855e−8/mean<4.815042e−9仍非0。新cut候选直接消费。尚无新ν主体全逆。

## phase_inverse：原对象完整能量、返回与剩余主损失

旧对象完整新density能量/高阶/strong scattering/全返回及所有源已推q53/54：loggain<33.631533、R*<6.232408723e109、cutoff2^1125、high逆<15.916848321。未求head2^1127；没有全inverse，不转授新ν，完整常数/源入口见H54及q54证明。
phase收完原550×8同标签局部时间半密度Jac真实运算后，转新曲率角根邻域的完整Airy/source合同；不转授旧常数。
## tail_connector：新尾真实输入与完整匹配缺口

8193后K2^128/ζ131是新最终profile，保129..8192和两全局逆幂；全标签/mean/C²平端/第四stop/source已推。原真实joint CK/固定t端口/strict密度全费用、联合KAM和固定Γ0准确相位比较、各内部已配角双端Cayley酉/完整源均已推，详H51。
q51固定Γ0真实incoming/完整帽fB反馈已解。新joint Γ*(a)接口对全复Γ盒重付有限第四stop长度，原点好t0仅用于同一D0逆，未偷授变化Γ好集；完整反馈真实进a_262144，||a||<2^-60000000 rf。非零fB真long也获约261921角宽，mixed不删。
完整F的全列导数（tail/long/mixed/Γ/stop/帽/mean）已合法构造94个全频Newton修正，每步标签宽损失2080明确保留，末β66624、真剩余<2^-5760041760，仍非0，不能当无限收敛。代理继续实际paired-port相对网络逆或任意小宽损失tame逆。
真正型cross DN已在同一KAM端角/全两端单位证明半光学指数增宽，两个方向全频norm<32、差<2^16 εI、全层<2^337X；ordinary/weak/mean/端点荷完整。不能倒除完整指数小transmission。真实quartic试函数给原Airy单位P0<2^10，精确flux shear吸收对角差，新增全层<2^240000 X≤2^-22144；此第40束待推，接reference Green/外Schur并保mean。深尾刷新固定宽损不能免费重用：简单L增大使固定H缩小，替代profile须新付允许Cauchy子空间。

## 真正完成标准与主线

同一公共精确度量、同一连通闭C²嵌入族、C²连续。D=diam F0(M)；闭H有内点、diam F0(H)≥.2D、逐点全t固定；全像未对齐Hausdorff held≥.05D；含反射E(3)的δE>0；全t reach≥.03D。
单相位G_t=R_(πt/4)G S_(-πt/4)的像只是刚体旋转；须同一最终族四个不同非共面固定曲率marker。R17及notes/2026-11-12-current-family-fixed-curvature-marker-budget.md可消费，但新ν/帽/尾全几何重付。
尚未在同一最终族同时完成。子题完成接open下一项，不因阶段/时长/计算失败停止，不等用户回复。

## 本轮后续已完成结论

- queue55/R133两真实新ν中心负前缀全频Cauchy/ordinary源/准确接缝已付，继续turning与完整主体。

- queue55/R119原Airy单位完整DN与真flux shear已付；保mean，继续reference Green/外Schur。

- queue55/R133第五次137原观察/原process/log已保；最后完整M256仍为全长accepted000。

- queue55/R133 .75全主体浮点几何正常完成，所选位移比.04958；继续.76延拓并重付。
