# 交接：可见振幅附近的精确等距解

visible-exact-astra-ac0d，2026-11-13 19:01（台北UTC+8）。**持续进行，主目标未完成。**

## 授权、规矩和执行

同一连通闭面/公共度量/C²连续精确等距嵌入族；固定有内点H，diam(H)≥.2D、
held≥.05D、含反射δE>0、每时reach≥.03D，全部在同一最终族成立才收尾。
根README授权及1–13、本题README全文已读；已读规则提交 **0dc35493297705477b61c855936a593f0d69da27**。
每次真实pull --rebase后立刻diff两README，只读新差异并马上遵守、改SHA；
至少每小时pull。每条结论独立commit并push前均pull；所有已见规则差异为空。
正常push，非FF立刻pull --rebase重推循环，不force。令牌仅瞬时终端环境。
根LOG不写；本题log每轮≤5行；H<10KB、md<100KB、文件>1MB压缩、单件≤5MB。
repo=/workspace/scratch/ac0d699811ad/math-research；python-deps在同scratch父目录，
PYTHONPATH须设它（flint0.9.0）；OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1。
提交脚本scratch/push_ready_conclusions.py、sync_push_native.py不含令牌。
旧完整检查点本次归档notes/2026-11-13-handoff-before-joint-Taylor.md；
前次详细R129运行状态在handoff-before-r005-complete.md；
此前详史在handoff-before-explicit-waist-validation.md；
更早恢复命令/域/收据见handoff-before-cauchy-continuation与handoff-before-ac0d-native-resume。

## 当前明确结果：R125–R132

R125–R128同一原腰真实局部分支、准确重建与[-.001,.001]嵌入已推。
R129（9881c9eba5e）全168连续盒证明同一[-.005,.005]精确嵌入：
e0<.026273879、e1<4.945149、gap>.1929506653、φθ>.3058472510、
柱Jacobian>.3307154018、曲率<10.591899。全η±1e−9/全角/原无限尾。
不同δ的目标可不同，尚非同一公共度量flex。完整native/source/candidate
SHA、原全局屏障失败与重跑命令见R129及H归档，勿覆写已成功source/report。
R130（1bc06677895）高目标jets+相关Taylor残差：新候选[0,.001]四盒给
ρ0<.043535832、e0<3.510082e−5、e1<.009114290；24混合导准确核过。
实际signed-frame亦过。新完整.05候选随R130保存，但其远端尚非PDE解。
R131已推f9018dffe9c：d=p−q,U=dpθ,V=dqθ准确线性系统，C0管+gap即
付C1有限性；旧.005全168盒C0-only通过，真实梯度粗上界<1165.454。

## R132 最新真实范围

同一原腰分支现已全参数/全角/全目标150闭盒证明[-.05,.05]真C²精确嵌入。
脚本fourfold_codazzi_invariant_rectangle.py，报告notes/2026-11-13-R132-invariant-rectangle-r05-native.json.gz。
真实移动矩形给M<2.877618、m>.06977177014、gap>.13954354029；
R131控制实际梯度<1843.663，真实φθ>.2194231922、柱Jacobian>.1586075083、
独立曲率<14.000161；新300盒C0补充已收紧到10.366510并改善水平Jacobian。
原存在性只消费真系数/初值，原150盒C0管失败仍保留。
完整proof R132、初腰R123/R128/原primitive及全部SHA已独立审。
仍仅局部环带；不同δ目标可不同，尚无封闭公共度量flex或最终reach。

## 活跃计算与恢复次序

root完整C0-only .05 session21463已完成1060.27秒/300盒，R131v2 consumer亦完成：
末e0<.027567044、gap>.19312757486。新水平frame消费者同R132真符号接合，
实际曲率<10.366510、φθ>.2696679160、柱Jacobian>.2902050414；完整成功
报告/证明R132-supplement-refined-C0-curvature-and-horizontal-embedding待逐条推。
原150盒及row111失败保持独立；其source/旧序列化异常均已main。

当前root仅有target-only长job session25294运行：
script scripts/fourfold_codazzi_target_coefficient_cover.py，原512 primitive/全尾/全η；
--right1/5 --max-step1/2000，report notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz；
log=scratch/Codazzi-target-r02-v1.log。source冻结，正在到.2付真实系数，未授.2分支。
root后续占R134：w=1/(q−p)的加权L2误差消去实际速度梯度，只剩候选(P+Q)θ，
正在完整推导并与加权梯度误差/Sobolev-C0门接合，尚无该新门的数值认证。

新准确有限候选notes/2026-11-13-codazzi-dense-r005-n512-candidate.npz.gz
文件名r005指.05；75段/512角/4151530B，SHA
1fdb86b3f959cd3137cf06bdbb37637643a1a56143152c7e26b622d7b353dd81。
producer参数--right1/20 --angles512 --max-step.001；只授有限函数。
旧成功v4的确切版本可由scratch/codazzi_*_v4_backup.py恢复。

newton_source：正帽诊断已冻结，notes/2026-11-13-R126-positive-cap-boundary-and-form-diagnostics.md
及diagnostic-manifest列11文件894005B已推9d526bf5901。
.235浮点metric<7.92e−12、Cmin>.345；.239旧新grounded相对form差>5.23，
.25正侧高谱急增，512投影双倍格q≈.098，不能认作连续精解。
R128明确腰宽嵌入已推e4cbc7b7f32；代理已保留M12/M24/logC失败及全部真实未投影残差；正保原腰低4模的失败都已归档（31件23.3MB manifest，待独立推），
不冒人工外端C为帽DN。R131已推f9018dffe9c，R132四边/frame也独立核过。代理继续同g0精确旋转
Cref=−sqrt(E−a′²)/(a sqrtE)的body/graft/真regular Jacobi DN与非线性帽匹配。
保腰低4模M32试算失败，全部保留。代理占R133，session54539运行
真实旋转正帽[.239,25/8]的1311 body/germ+natural graft；16模m4..64的
全η真Riccati上下流及全高共同区间，保R74真实regular指数fee/mean平移，非非线性帽。

phase_inverse：全strict真实WKB/系数jets首run session96833因人工腰分片粗界已中断，
代理合并同一实际腰germ并加积分率分片门重跑，最新session须向代理确认；
当前重跑session92283，已200叶/common164到r=.233928；checkpoint
notes/2026-11-13-R46-native-WKB-full-strict-fields.json.gz；
原入口fourfold_strict_actual_wkb_fields.py运行中冻结，约168 common spans。
完整角向ODE保相关使leaf60 Fcal复模<339，不冒完整强余项。
R43实际负canonical图/完整potential已推e6dc717；
新完整root Fourier消费已独立复跑：δ2^-140、全|s|≤8强R4/3<6.193e41、
源gain<20.962，保存真实L2误差及全部解析尾。最新真C取消/大逆图已审，
δ2^-129、强4/3<4.319813e41待推；另真实physical curved cut全实图已冻结待审。
全root/strict强接线仍欠，代理正查常数5050的准确shifted-Airy参考以减粗。
R46实际leaf60整数energy10+简化真实残差已推3a4857df654；
只第一characteristic导数进指数、高阶入三角源；实际P10<2.903e24仍粗。
代理继续全strict domain的s+2、真实F及frames/source，不以单叶代全传播。

tail_connector：实际tail角漂移/密度共轭29门已推d22463e54f3；
双counterterm圆KAM不能直接用于无限混合型层，须全两通道scattering/Airy。
联合标签1850权Schur17门已推8c4b181e9be；原forcing只给ell1_128，
已有非线性尾chart需ell1_8192，域不匹配未解。代理正重付真实balanced四态
connector能量，已将充分标签域实质降至ell1_224（36门），完整raw宽777/400、grounded宽377/400，
state<2^-447 X、物理C²<2^-428||a||224；仍未自动闭全尾相对逆。
真实hodograph已推13c1c3d145a；principal为[bI+cB0]∂ξ，
c−1非恒等零：R11真cut128第四标签方向完整二阶项严格负；
尚非完整混合return旋转数结论。新divergence/density+A因子已两路审，
全频Airy扰动平方能量总费<2^-427 X待推；代理继续真正型两端变分DN/Green。
三代理只写自己新文件，root统一审/索引/H/open/log/逐条提交。

## 已推恢复及可消费证书

详细恢复、完整域、原生收据与旧source SHA见
notes/2026-11-13-handoff-before-long-Taylor-run.md及上述更早归档。
R105/R121全η整帽六块逆<90.583064；R110原源下界>31.557，仅约束选定表示。
R106全550真forward已恢复，70历史SHA一致；完整b/强R*/cutoff未付。
R119实际正段DN/ordinary scalar Jacobi源已付，mixed-tail全相对逆仍欠。
R120原腰非mean源>.604740；R122完整二次源/R124腰q+=0已付。
R123充分几何档(.001,.01,.7)，也可换成更好的真实曲率证书。
可再生巨大缓存勿推，不能以节点、有限谱、改目标或数值结果冒全原PDE。

## 尚未完成的主缺口

旧P_hat：R101真全返回共轭、R102全频算术、R104对角>7/(110j)已付；
完整b−β/强R*/有效cutoff/全低高Schur/Airy/port/source Kwire仍未闭合。
P_hat是type-fixed修改，真实P_hat−P/ω必须保留。边界高逆不是完整体源强逆。
新Cauchy分支：只能消费其自身证书；不能免费转入旧R101/R111/帽/低块。
跨根/正帽/尾/mean/regular联合matching、全域源与邻域、C²收敛/连续选择仍欠。
R112允许整材料平帽轴向平移，最终phase族H固定；R114修复、R115chart、R117重建
仍有效，但不授任意普通C²邻域。最终R69/R78/R79/R123与四个不同非共面标记
须落在同一精确族；辅助整像相位δE=0不能冒含反射非全等。
做完子问题继续open下一项；不能以时间、计算等待、阶段报告、失败诊断结束。



## 本轮后续已完成结论

- R132新300盒完整C0比较与水平frame已审推：同一[-.05,.05]曲率<10.366510，φθ>.2696679160/J>.2902050414；更远target-only计算继续。

- R119真正型两端弱DN/普通源已审推，真角图下全频相对费<2^-430 X，完整mean/平移/源flux保留；全层强Airy范数比较继续。

- R43真C取消及负canonical大逆图已审推：逆半径1/60000、完整势盘1/120000、δ2^-129全S8强4/3<4.319813e41；完整physical接线/R*仍欠。
