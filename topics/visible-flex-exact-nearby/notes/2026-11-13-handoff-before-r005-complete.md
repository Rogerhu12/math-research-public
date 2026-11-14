# 交接：可见振幅附近的精确等距解

visible-exact-astra-ac0d，2026-11-13 17:37（台北UTC+8）。**持续进行，主目标未完成。**

## 授权、规矩和执行

同一连通闭面/公共度量/C²连续精确等距嵌入族；固定有内点H，diam(H)≥.2D、
held≥.05D、含反射δE>0、每时reach≥.03D，全部在同一最终族成立才收尾。
根README授权及1–13、本题README全文已读；已读规则提交 **e4cbc7b7f32b3a094f3c61fde8f0da9870257fb2**。
每次真实pull --rebase后立刻diff两README，只读新差异并马上遵守、改SHA；
至少每小时pull。每条结论独立commit并push前均pull；所有已见规则差异为空。
正常push，非FF立刻pull --rebase重推循环，不force。令牌仅瞬时终端环境。
根LOG不写；本题log每轮≤5行；H<10KB、md<100KB、文件>1MB压缩、单件≤5MB。
repo=/workspace/scratch/ac0d699811ad/math-research；python-deps在同scratch父目录，
PYTHONPATH须设它（flint0.9.0）；OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1。
提交脚本scratch/push_ready_conclusions.py、sync_push_native.py不含令牌。
旧完整检查点本次归档notes/2026-11-13-handoff-before-explicit-waist-validation.md；
更早恢复命令/域/收据见handoff-before-cauchy-continuation与handoff-before-ac0d-native-resume。

## 本次完成的明确区间：R127

R125已给未知ε的真局部分支；R126已证准确Codazzi、完整周期frame/位置重建、
Riemann C0/C1比较和一阶延拓。R127现在对原wholeη、全部实角、原无限primitive
真实通过[0,.001]的64个闭径向盒。Y0<.039455783、Y1<6.607184，
candidate gap>.2436020565、实际gap>.1646904909、k>.9248968679。
反射给[-.001,.001]准确C²等距浸入；R128已另付该明确宽度的全局单射。
R12817门核真实frame，水平support>.36759、柱Jacobian>1/5，得到同一真实C²嵌入环带；仍不冒闭面/同度量flex。
成功报告notes/2026-11-13-Codazzi-continuation-r001-v3-native.json；
validator SHA ea61a2d27273352b65951900359301df41e9a29a2a9c2ef62836809de4981acc，
provider SHA4a37d58640b54b091fab9bfd677b55e3392c30405d08073a2ad90f13205cf9f1。
v3两确切版本已随R127推7108adcf66d；v2完整覆盖但屏障false，旧C分母失败同存。
21段degree7/1024角候选已推18f2c35，gzip SHA a3e43fc8ee7ab8b6a0e080edccb107ac1e2d92634b0325783f7a99711cf6842f。
所有binary64视准确dyadic、共享端点、负频准确共轭、mean保留、Nyquist0；
原目标固定E=<|F_old,r|²>，δ是辅助参数，不冒同度量弯曲参数。

## 活跃计算与恢复次序

root v4正在session19408（已过.003，逐盒barrier前缀诊断通过，未授完整）：--right1/200 --subdivide8，共21候选段，
log=scratch/codazzi-r005-v4.log，报告notes/2026-11-13-Codazzi-continuation-r005-v4-native.json。
v4以原FF的准确零频卷积和真尾计算E/E1/E2；角格改局部二阶Taylor+全三阶余项。
v3/v4版本分开：v3已随R127永久main，当前两个脚本已恢复v4，
分别与运行报告记录SHA准确匹配；scratch仍保留两份v4备份，不能混报版本。
当前v4尚未通过完整屏障；继续看原报告，失败就真实收紧，不从部分行宣告通过。
R128明确腰宽单射已成；继续更宽实际连续验证。
新scripts/fourfold_codazzi_piecewise_barrier.py已写，逐盒传播真实误差，
每盒仿射屏障显式核正margin，拒收不完整native报告；尚未运行完整.005证书。

newton_source：正帽诊断已冻结，notes/2026-11-13-R126-positive-cap-boundary-and-form-diagnostics.md
及diagnostic-manifest列11文件894005B已推9d526bf5901。
.235浮点metric<7.92e−12、Cmin>.345；.239旧新grounded相对form差>5.23，
.25正侧高谱急增，512投影双倍格q≈.098，不能认作连续精解。
R128明确腰宽嵌入已推e4cbc7b7f32；代理正做两端Codazzi候选，M12首试未收敛已保失败。

phase_inverse：R43实际负canonical图/完整potential已推e6dc717；
δ2^-224局部全|s|≤8强R4/3<1.229e61、源gain<20.962，非全R*。
R46实际leaf60整数energy10+简化真实残差已推3a4857df654；
只第一characteristic导数进指数、高阶入三角源；实际P10<2.903e24仍粗。
代理继续全strict domain的s+2、真实F及frames/source，不以单叶代全传播。

tail_connector：实际tail角漂移/密度共轭29门已推d22463e54f3；
双counterterm圆KAM不能直接用于无限混合型层，须全两通道scattering/Airy。
联合标签1850权Schur17门已推8c4b181e9be；原forcing只给ell1_128，
已有非线性尾chart需ell1_8192，域不匹配未解。代理继续真全谱flow，不漏m²归一化。
三代理只写自己新文件，root统一审/索引/H/open/log/逐条提交。

## 已推恢复及可消费证书

R105原五入口175叶/wholeη切口/40行strongGram/六块完全恢复；
R121全1309 body+322 graft，整帽ε≤1/500已推b09557222；六块逆<90.583064，
余绝对费>.01103959129。有限core未付的高通道/无限Schur仍不能删除。
R110完整九场leaf60、连续energy、两层kernel、density96、exact-time强Gram已恢复；
所选三源上界113.023699、真实e4源下界>31.55765385827514已推bdfa4080ea。
只约束这份弱通量源表示，不是PDE逆/精解不可能；不得加叶期待其norm变小。

R106整root FP<8822,J<1.009；654闭复bulk叶+550真ray完整forward<13205。
全ηmoving-root/degree80/±650真系数均main，H误差<.000694547、transport<7.646e−7。
两腿几何phase<26410、最终KAM标签已推a04341146，尚未等同完整算子b，强R*仍欠。
550历史forward已全部恢复b85451fd8：35raw+23UL+12Q的70个旧SHA逐一吻合。
规范缓存可重生不推；manifest与原命令已保存，session54693结束。
全550/884片phase两分辨率诊断已推5766f926：half mean18.5125225223，
非mean sup≈1.04149；nominal两腿mean37.0250450446、非mean sup≈1.79095。
依然未付真实reference ray/连续积分余项/全参数/完整算子强phase。

R119原混合尾/真实connector已推51f6b1168/2d65ec3e8；完整主锥全频原标签<e^(391m)，
raw充分e^(404m)，8192权余量e^-33513532已推ab0156b5。
长正段全频同宽BVP Green<32、边界2^-25/解球2^-20/收缩1/16已推4c28d0a97；
双bump至实际u=B，raw宽τ+1968、真联合两迹横截≥2^-40已推e6a3f955c。
nonlinear外列筛选已推c86f0856d：内Neumann<17e^-L/2；
新真内端DN差<2^-8390及完整continuous scalar Jacobi源已推5109b8d97。
匹配F(a,f*)=kB+C_L fB−S_L f*−E_D；混合尾相对邻域逆/ordinary源范围仍欠。

R120整个腰非mean源>.604740；小改E/G(.01)仍>.590232635；
连续[0,1e−4]源<.703693，完整复盘/角尾均付。原目标未换。
R122真实Newton二次source各向异性two-jet式已推feee87ca68，无纯H11²/H22²，
近似应变兼容/连接等项不能删。R124真实腰jet使q+恒0已推deafcfae0，
原gF梯度<1.205161e−5、Hessian<.406443414，仅腰。
R123几何充分档(.001,.01,.7)已推3c6a6e19，原σ>1/2,K<12,D<2.553，
给reach/D>.03与held>.05；可以直接支付更好真实曲率，不因参考Hessian档失败就判no-go。

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

- R127已通过真实连续[0,.001]全部八门，Y0<.039455783、Y1<6.607184；反射得双侧真等距浸入。明确宽度单射及全局完成仍欠。

- R119实际尾角流/密度共轭已闭，漂移Wiener<2^-280；真实principal型根、退化k权及mean/regular全保，高频return未冒免费。

- R46实际leaf60全角/wholeη整数energy10已付，P10<2.9021e24；准确WKB残差消去独立hθθ，完整strict域/frames/source仍欠。

- R119联合Schur1850角宽费已实付，真实outer列到ell1_128<2e^-L/2；现有ell1_8192域差明确，未声称完整非线性逆。

- R128已给同一R127真实环带的全局单射：水平支撑>.36759、柱坐标Jacobian>1/5，17门全过；明确[-.001,.001]为C²嵌入。

- 正帽有限续算/投影/双倍格诊断全部保存；新旧相对form约5.23，准确强制帽接口保二次应变、改型源、regular/mean，未冒无源DN或正帽真解。
