# 交接：可见振幅附近的精确等距解

visible-exact-astra-ac0d，2026-11-13 20:33 UTC。主目标未完成，持续研究。

## 规矩、位置与同步

根README全部授权/规矩及题README已读；已读规则提交 **0ca2069e08b0ec2fcef6173d7171506125813857**。
每次真实pull --rebase立即diff双README，有变只读差异照做并记SHA，至少每小时pull。每结论独立commit/push；非FF立刻pull/rebase/普通push直到成功，不force。PAT仅瞬时CLI，不写文件/提交。
root独占Git/H/open/results/log；代理只新文件。根LOG停写。H<10000B、md<100KB、open尽量<30KB；>1MB压缩、单件≤5MB。逐文件add，不stage恢复cache/半成品。根规矩11：可重建大中间数据不重复入库，只存源/参数/hash；最终复核真正需要的完整候选另论。规矩13不设freeze/独审/重复重跑；完整证明与必要严格运算完成即推，只查实际数学风险。
repo=/workspace/scratch/ac0d699811ad/math-research；topic=topics/visible-flex-exact-nearby。PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps；OPENBLAS/OMP=1；PYTHONDONTWRITEBYTECODE=1。
scratch push_ready_conclusions.py逐条写H/open/results/log；sync_push_native.py真实pull/rebase/diff规则/normal --no-thin push。helper活跃时勿改H/open/index；H guard失败可能先改open/results，保原已写继续。pull503要实际重试同步，再接未推queue。
部分克隆promisor/blob:none，gc.auto0/maintenance.autofalse；q44支持的MIDX资源回收已完成。勿全hydrate/删索引pack，19:04余2.7GB。
queue1–56全已推；56末abeb195c1898e555ebeea79e187124c42014e8c3。完整H链notes/2026-11-13-handoff-after-queue56-complete.md→55/54等，results旧索引notes/2026-11-13-results-history-through-queue47.md。已完成不重做。

## 同一最终目标必须区分

原对象SHA91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848，原δ*=−7789843107295549/4611686018427387904。δ/ν/腰/deep profile变化都属于新最终候选，不能转授旧g0。
原固定g0的R131全η完整[-.2,.2]局部精确嵌入已证但仍有边；κ<8.099019。所有原false/137及native见H52，不转授新ν。
新主体Eν=E exp(νh)，h=4096t^6(1−t)^6支持(.05,.18)，a不变、腰补模可变。真实全B/C与mean匹配后才转授holonomy及腰C²反射；不能提前消两迹。

## root 当前主体、实际作业与接续

互逆u=αU,v=1/Cref+αV，B=u/v,C=1/v；RHS三次准确支持3M。全部物理商BC、ν列、mean和未保留尾都须付。full_action_qr_collocation.py保完整Jac/独立FFT作用，memory/checkpoint皆门5e−8；小完整Jac/LU核已过。
旧B,c及新互逆M128 .70/.75原候选全保，详H49/52。.70 finite true866node；.75 finite false1379node，采样物理残差达.155/.800，故增M256；不把finite true当PDE。
**五次原137全保且原因未知**：82459全长M256首accepted可用；81525 M128切口首accepted可用、后mesh失败；84317/35756仅完整factor，35049仅warm-start，均无最终有限成功。完整原process/log/观察在q52–55对应记录，勿认定OOM/奇异。只运行一个大型求解。
旧完整M256输入是scratch reciprocal-m256-alpha075-accepted000-candidate.json；若丢失按notes/2026-11-13-R133-reciprocal-m256-exit137-and-complete-resume.md重做全长首接受步，原hash及完整Hermite记录在q52/57重建链。大中间不重复入Git。
**当前大型作业80604**：v5从scratch reciprocal-capcut-m256-alpha076-persistent-step01-candidate.json继续step02（prefix ...alpha076-persistent-step02），M256/2048角、α=.76、q256切1.5、meshstride1/tol2e−6/max2800/jacchunk4/qrspan8/AS1024/pause1。首步85064正常0，672nodes、ν−5740959909187403/144115188075855872，index SHA504433be48b6659ef9327a489673fdb81a91498ef785970564cd89bc910c6c0d；两full solve1.409e−12/1.907e−11、RMS.002324/BC.001877仍finite=false。原process/log/完整重建清单见...step01-reconstruction.json；若新ν越−.04须重付type。persistent完整QR与双代入存scratch/codazzi_complete_QR_state，每恢复仍原全5e−8门，原Newton规则不改。无新accepted可同输入重启；有则从新状态续。CI权限只读403，未改workflow。
完整target jets与连续残差v3已证；新residual_checkpointed_v2逐闭片原子保存/有向极值恢复，保3M/原尾/真实接缝。.70原前3片实际暂停再恢复全过，U<3.644477e−5、V<2.329807e−6，候选κ<5.190640；全1613片未完。第一版一片暂停源/报告保留不用于恢复。待实际新收敛候选完整主体。
C0曲率/skew框架残差→全几何定理q47已推，实际连续费用待付。15638完整.75 M256原accepted000浮点几何已推q55，采样D2.55109067、见证距.1264804/比例.04957895、κ8.723513、support.9086428。仍<.05；非严格、非完整闭面，不授reach。源reciprocal_frame_probe.py/原report和geometry hash已推q55，大几何中间只在scratch。需增加振幅并完整重付。

曲率角φθ=C/<C>的完整局部系统已推，含RC/mean/PPoly接缝。新moving nonlinear结构M.1–17：m=<v>φ=1/D，S=u²+Kv²，d=−βI(S)，θ=m^-1∫v显式反向恢复；完整mean与非局部线性项保留，二维正能量比较及残差r+I(rv/v)qφ已证，实际系数待付，不授全逆。全η、全ν∈[-.04,-.025]的[0,1.5]完整类型已证：0..238/1000严格负、(.238,.239)唯一简单根(K′>46.285)、.239..1.5严格正，后段不受ν bump影响。经验曲率角rotation .27501299/.27494534、secant约−.001353仅数值，不授twist/Diophantine。新.75完整1192闭盒/751接缝已证[0,.2]全频Cauchy向外<1493.577736、向内<2408.100850、v-gap>.1145864894566，含ordinary源/真jump；newton继续负段/角域，phase专攻真Airy接口。

## newton_source：真帽接口、物理商全尾与主体逆

q44/46真帽全B/C/mean：cut1.5全频偶四重ζA0≤2e−5、fB≤2^-60，663核Lip<.086769709；非线性B余<1.663187e−8/mean<4.636375e−9，另一迹仍须消。
实际q256由663闭盒×m4..1024及真R74无限尾得；输入...cap-cut-r15-q256-with-tail.json含逐模q/ε，全m界1.06、最大浮点q误差<.005560200378199，必须付Σεm|c_m|及两物理商尾。ν在帽区不变。
完整Laurent逆W及Wiener全尾/mean/二角导已证，源reciprocal_Wiener_boundary.py。.70腰/1.5 E0<9.022e−15/4.209e−15；M256 .75首accepted在1.5 E0<3.935e−15、ζA0<1.420305e−5、θ²<.000227253，真B失配<9.571855e−8/mean<4.815042e−9仍非0。新cut候选直接消费。尚无新ν主体全逆。newton当前57704 collar系数句柄未知，原64/96完片保存，显式恢复补32；先收紧root/真共同analytic germ，再消费moving二维能量。

## phase_inverse：原对象完整能量、返回与剩余主损失

旧对象完整新density能量/高阶/strong scattering/全返回及所有源已推q53/54：loggain<33.631533、R*<6.232408723e109、cutoff2^1125、high逆<15.916848321。未求head2^1127；没有全inverse，不转授新ν，完整常数/源入口见H54及q54证明。
旧67045句柄不可用且无最终native，原276/550仅日志；phase已保未知中断，33056按原550输入重做、每5段checkpoint，不授完成。之后专攻新真实fold/Airy，moving非局部算子不可经T依角坐标后免费当同T局部项。
## tail_connector：新尾真实输入与完整匹配缺口

8193后K2^128/ζ131是新最终profile，保129..8192和两全局逆幂；全标签/mean/C²平端/第四stop/source已推。原真实joint CK/固定t端口/strict密度全费用、联合KAM和固定Γ0准确相位比较、各内部已配角双端Cayley酉/完整源均已推，详H51。
q51固定Γ0真实incoming/完整帽fB反馈已解。新joint Γ*(a)接口对全复Γ盒重付有限第四stop长度，原点好t0仅用于同一D0逆，未偷授变化Γ好集；完整反馈真实进a_262144，||a||<2^-60000000 rf。非零fB真long也获约261921角宽，mixed不删。
完整F的全列导数（tail/long/mixed/Γ/stop/帽/mean）已合法构造94个全频Newton修正，每步标签宽损失2080明确保留，末β66624、真剩余<2^-5760041760，仍非0，不能当无限收敛。代理继续实际paired-port相对网络逆或任意小宽损失tame逆。
真正型cross DN已在同一KAM端角/全两端单位证明半光学指数增宽，两个方向全频norm<32、差<2^16 εI、全层<2^337X；ordinary/weak/mean/端点荷完整。不能倒除完整指数小transmission。真实quartic试函数给原Airy单位P0<2^10，精确flux shear吸收对角差，新增全层<2^240000 X≤2^-22144；此第40束已推q55，接reference Green/外Schur并保mean。深尾刷新固定宽损不能免费重用：简单L增大使固定H缩小，替代profile须新付允许Cauchy子空间。

## 真正完成标准与主线

同一公共精确度量、同一连通闭C²嵌入族、C²连续。D=diam F0(M)；闭H有内点、diam F0(H)≥.2D、逐点全t固定；全像未对齐Hausdorff held≥.05D；含反射E(3)的δE>0；全t reach≥.03D。
单相位G_t=R_(πt/4)G S_(-πt/4)的像只是刚体旋转；须同一最终族四个不同非共面固定曲率marker。R17及notes/2026-11-12-current-family-fixed-curvature-marker-budget.md可消费，但新ν/帽/尾全几何重付。
尚未在同一最终族同时完成。子题完成接open下一项，不因阶段/时长/计算失败停止，不等用户回复。

## 本轮后续已完成结论

- queue57/R133完整moving-chart非线性等价/反向构造/真mean二维能量已证；实际常数继续付。

- queue57/R133连续全残差逐片恢复实际通过同3片，原全主体未冒充完成。

- queue57/R133 .76首完整接受步正常保存但未收敛；80604完整接step02。
