# 交接：可见振幅附近的精确等距解

visible-exact-astra-ac0d，2026-11-13 17:37（台北UTC+8）。**持续进行，主目标未完成。**

## 授权、规矩和执行

同一连通闭面/公共度量/C²连续精确等距嵌入族；固定有内点H，diam(H)≥.2D、
held≥.05D、含反射δE>0、每时reach≥.03D，全部在同一最终族成立才收尾。
根README授权及1–13、本题README全文已读；已读规则提交 **7172f1050ee4f37020a0d71a76203e5ea3f10871**。
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

## 当前明确结果：R127–R129真实环带

R125真局部分支、R126准确Codazzi/完整周期重建及C0/C1继续定理已main。
R127 wholeη/完整角圆/原primitive64闭盒给[-.001,.001]真浸入已推7108adcf66d；
R128真实frame/正柱Jacobian17门给同一明确环带嵌入已推e4cbc7b7f32。
R129已推9881c9eba5e：完成[0,.005]全部168连续闭盒（21准确候选段、每段8盒）：
原单全局屏障false保留；新逐盒仿射屏障完整实际通过，e0<.026273879、
e1<4.945149，实际Riemann gap>.1929506653。沿真实特征保p<0<q，
A≤kM、|B|≤k，实际normal转角<.014399123、φθ>.3058472510、
柱Jacobian>.3307154018、主曲率<10.591899，故[-.005,.005]真C²精确嵌入。
所有门全参数1e−9/全角/原无限尾。不同δ目标可不同，绝非同度量flex完成。
三个native报告为notes/*r005-v4-native.json.gz、*r005-piecewise-native.json.gz、
*Codazzi-r005-signed-frame-embedding-native.json；完整proof R129。
旧准确候选gzip SHA a3e43fc8ee7ab8b6a0e080edccb107ac1e2d92634b0325783f7a99711cf6842f。
v3/v4验证器及provider必须按报告SHA区分，v3已随R127永久保存。
当前脚本是v4；对应SHA/尾/误差及精确重跑命令见R129，不能覆写旧报告。

## 最新R130：相关残差方法已推1bc06677895

新候选仍逼近同一个原腰真实分支；其[0,.001]仅4连续盒全角/wholeη/无限尾
给rho0<.043535832、rho1<10.648890，逐盒屏障e0<3.510082e−5、e1<.009114290。
实际signed-frame亦过，局部曲率<8.523482。完整证明R130；新source
fourfold_codazzi_high_target_jets.py真实付K二阶/E三阶，fourfold_codazzi_residual_taylor.py
以中心完整残差/一阶导取消后付全矩形二阶Taylor余项；24项独立符号混合导核对通过。
完整报告notes/*Codazzi-joint-Taylor-r001-v2-native.json及同prefix piecewise/frame。
首次int/Box零盒失败保留，未冒结果。下一修改须保成功source SHA（R130中列齐）。

## 活跃计算与恢复次序

root新compact Taylor完整[0,.05]正在session65291，75候选段×2盒；
script scripts/fourfold_codazzi_residual_taylor_compact.py（新文件，原R130源码不改），
log=scratch/codazzi-joint-Taylor-r005-compact.log；报告
notes/2026-11-13-Codazzi-joint-Taylor-r005-compact-native.json.gz。
物理闭角格4096、准确candidate FFT网1024；完整原primitive仍512节点及同一全尾。
这里不作有限Fourier乘法，网只需容纳全部准确候选support，非线性全在实际区间jet计算。
--right1/20 --subdivide2；尚未授任何.05连续解，等待完整输出及实际C0/gap门。
R131 weighted-gradient若成可省当前C1 Riccati延拓门；rho1仍完整保存不误删。

root v4 session19408已完成1133.95秒、native168盒完整，consumer77283与56629已结束。
新浮点dyadic候选已产生，随R130保存：notes/2026-11-13-codazzi-dense-r005-n512-candidate.npz.gz，
此处文件名r005指r=.05；75段、512角、4151530B、SHA
1fdb86b3f959cd3137cf06bdbb37637643a1a56143152c7e26b622d7b353dd81。
同前缀floating.json保完整参数/诊断，producer原脚本未改：
--right1/20 --angles512 --max-step.001；实际运行5.59秒，candidate仅明确有限函数。
准备进一步连续验证，并改进残差相关性以免用节点或投影代全PDE。
root仍可用scratch/codazzi_*_v4_backup.py恢复当前v4确切版本。

newton_source：正帽诊断已冻结，notes/2026-11-13-R126-positive-cap-boundary-and-form-diagnostics.md
及diagnostic-manifest列11文件894005B已推9d526bf5901。
.235浮点metric<7.92e−12、Cmin>.345；.239旧新grounded相对form差>5.23，
.25正侧高谱急增，512投影双倍格q≈.098，不能认作连续精解。
R128明确腰宽嵌入已推e4cbc7b7f32；代理已保留M12/M24/logC失败及全部真实未投影残差；正保原腰低4模、让高模BVP解耦，
不冒人工外端C为帽DN。新优先R131：d=p−q,U=dpθ,V=dqθ的真实线性退化结构，
可用C0管/gap给C1有限性，无需候选D2/Riccati；代理正在完整证明/实际初值消费。

phase_inverse：全strict真实WKB/系数jets首run session96833因人工腰分片粗界已中断，
代理合并同一实际腰germ并加积分率分片门重跑，最新session须向代理确认；
当前重跑session92283，已32叶到r=.03；checkpoint
notes/2026-11-13-R46-native-WKB-full-strict-fields.json.gz；
原入口fourfold_strict_actual_wkb_fields.py运行中冻结，约168 common spans。
完整角向ODE保相关使leaf60 Fcal复模<339，不冒完整强余项。
R43实际负canonical图/完整potential已推e6dc717；
δ2^-224局部全|s|≤8强R4/3<1.229e61、源gain<20.962，非全R*。
R46实际leaf60整数energy10+简化真实残差已推3a4857df654；
只第一characteristic导数进指数、高阶入三角源；实际P10<2.903e24仍粗。
代理继续全strict domain的s+2、真实F及frames/source，不以单叶代全传播。

tail_connector：实际tail角漂移/密度共轭29门已推d22463e54f3；
双counterterm圆KAM不能直接用于无限混合型层，须全两通道scattering/Airy。
联合标签1850权Schur17门已推8c4b181e9be；原forcing只给ell1_128，
已有非线性尾chart需ell1_8192，域不匹配未解。代理正重付真实balanced四态
connector能量，已将充分标签域实质降至ell1_224（36门），完整raw宽777/400、grounded宽377/400，
state<2^-447 X、物理C²<2^-428||a||224；仍未自动闭全尾相对逆。
三代理只写自己新文件，root统一审/索引/H/open/log/逐条提交。

## 已推恢复及可消费证书（详史见上述H归档）

R105全175叶/40行strongGram/六块及R121全1309 body+322 graft已main：
全η整帽ε≤1/500，六块逆<90.583064，余绝对费>.01103959129；高通道/无限Schur仍欠。
R110原九场/连续energy/两层kernel/density96/exact-time Gram完全恢复；
选定三源上界113.023699，实际e4源下界>31.55765385827514，只约束该弱源表示。
R106全root FP<8822、J<1.009、654闭复bulk+550真ray forward<13205；
两腿几何phase<26410及最终KAM角已付，完整算子b/强R*未因此付清。
550历史forward共70旧SHA完全恢复，native缓存规范路径在原manifest，勿推可再生大中间件。
全550相位两分辨率诊断已main：half mean18.5125225223、nominal两腿mean37.0250450446，
非mean sup约1.04149/1.79095；真reference/连续余项/完整PDE算子尚欠。
R119原尾/真实connector/main cone已付；actual raw标签费e^(404m)。长正段真BVP
Green<32、边界2^-25/球2^-20/收缩1/16；双bump至u=B真横截≥2^-40。
nonlinear外列内Neumann<17e^-L/2，真内端DN差<2^-8390及完整scalar Jacobi源已付。
联合行F=kB+C_L fB−S_L f*−E_D；mixed-tail实际相对邻域逆/ordinary源范围仍欠。
R120原腰非mean源>.604740、小改E/G(.01)仍>.590232635；原目标未换。
R122两jet真实二次源完整已付；R124腰q+恒0，原gF梯度<1.205161e−5/Hessian<.406443414。
R123充分档(.001,.01,.7)由σ>1/2,K<12,D<2.553给reach>.03D、held>.05；
也可直接用更好真实曲率，不能把充分档失败认作no-go。

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

- R130真实相关Taylor残差四盒/全角/wholeη通过，e0<3.510082e−5/e1<.009114290，24符号混合导核过；新.05准确有限候选已保存，继续更远验证。

- R119完整真一阶Jacobi框架已付32门，所有层/connector/bump低阶余项积分<2^-426 X224；ν真实主相位与退化两迹全逆仍欠。

- R104 cutoff依赖双侧高gauge已证，精确保全部有限head行列及ordinary源，不多借R的导数窗口；尚未授实际b/R*/cutoff。
