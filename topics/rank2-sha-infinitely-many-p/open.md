# 未解决问题与当前接续

主目标：固定一条 E/Q，完整证明 rank≥2 且无穷不同 p 的通常全 Sha(E/Q)[p∞] 有限。**未完成，持续研究；不在阶段结果、时限或建议处停下。**

[本次整理前完整 open](notes/2026-11-20-open-before-complete-low-P-reader.md)逐字保存全部旧问题、公式、条件、预算、来源和更早归档入口；[同期完整 HANDOFF](notes/2026-11-16-frontier-before-padic-reconstruction.md)保已运行 source/run/job 与各原理论检查点。下列未重写的旧门仍有效，编号缺席不表示完成。

## O1. 固定曲线的秩：已完成

E17:y²=x³−17x 由 R4 完整下降证 rank2；E136 和 j0 曲线 y²=x³+17,+24,+2312 的 rank2 见 R239/R294/R398/R469。E−11 的 rank≥2 与原 V66 见 R816/R820。缺的是其中一条固定曲线在无穷不同 p 上的通常全 Sha 结论。

## O2–O3. 同一原中央的无穷联合非零

四次 CM 的原完整 Selmer 桥 R40/R51 给 Sha[p∞] 有限 iff [T²]F_p^-≠0 iff 原 J'_p(0)≠0，原57800平方常数/Schwartz/period不变。j0 的 S34/T72/U136/V66 保完整通常 Selmer，准确界为 2+corankSha≤2ordJ。必须在同一个无限 p 集上迫至少一个固定原 J' 非零；有限扫描、其它循环或非中央项不够。

R409/R595/R636/R647 的原 prime diagonal、forcing、Cartier 以及 R673/R676 的实际 sigma modp² 提升均已付；R654 的指定中央非零仍开。R649 的二维比较不把真实提升变成自由参数。普通全层阶乘判据与惰性 signed 判据保完整归档，均没有推出无穷命中。

### 当前指定输入与真实新关系

四输入 S34/T72/U136/V66、charge17/36/68/33、全部 CM13/Euler/Schwartz/p²p³ 与通常全 Selmer 不变。共同 C24 的原三行/指定 c*=(1,−4/7,16/7)及所有低 cross 保留。

R863/H22、R876/879、R884A–I 已付全部原 norm-three/norm-two trace、old/new/cross、质量与低配对。原特征零 Ĉp=(p+1)cint、DR3、Γ16 及 Fermat 项不能提前约化或删去；trace 质量是单位不表示原 B 非零。UΘ4 完整三纤维 run43870426107 已通过，所有参数/hash在原执行注。

R887目前已付：

- 同原 Z 的全部固定 CM/torsion cocycle、绝对 sigma/Mumford 倍率与原 G/P2 初值缺陷；ρp cp=1、Fp=−cp^-1 D^(p−2)x，不增加水平自由度。
- 同一有限 p 基的所有 Z^p 折回、∇a^p=−aH^p、原 P2 的 adj 公式及 Pm 五块窗口。Pm 降二挠极但新增 Z 根补留数 Fν,p=T_m,p DRν∈X(X+1)k[X]≤s−1。
- 三次 Cartier 完整保同原 étale A_(3s−1) 的 Frobenius 逆、全部 trace 和原 exact 项；四 α 同时零只删 log 行。
- §16 给四固定 m 倒幂递推/真实 Miller 除点函数读取；平移连接 p 曲率恰为 −m cp Z(B)，每根一次退化。原 sigma 低卷积、p 级极帽与 B 法向保留，D_B 不能穿过只在纤维成立的平坦式。

- §17 的同原二因子P6·P_(m−6)保四α和前五个modp窗，逐点消所有非O的Z零点补极；二挠极<2p³后原[-1]不变排二阶，完整C³η[2]=−α^(1/p³)rω，无exact尾。首次C为同Q6 Qb Rν的指定γ1^(1/p)ω，旧单因子全trace及原exact分别准确保为模型差；没有modp²/p³替换授权。

R887§18原四负幂的全Hurwitz顶边∂v^p F_m=−m cp(Fp(B)+v)F_m已证，Jp=−mcpFp/Jp+1=−mcp；唯一原r相位改常数为Z而保全部低卷积。真实T_m,p由原a_(p−1)和同非零cpFp作固定m−1步逆链读出，不能删顶值、跨Z零纤维微分或认四α非零。

R887§19首个第六Gaussian块准确由同f_<p的L3/L(n−3)与κ5的s行卷积给出；原Taylor及完整连接误差求和支付e_a,p，共同c2(p)严格消去。此处只付modp首乘法缺陷；R912另以原[p]除点数据支付完整两位输入，中央零到边界零的蕴涵仍未证明。

**下一实质门：** 同一Q6与四个指定Q_(m−6)Rν方向的实际双线性关系及最终两次Cartier联合非零。四个实际 Fν,p、同一 trace 与原 P2 幂−Pm 的联合关系继续保留。不能由 adj 可逆、simple Smith 退化或 trace 配对非退化推四个指定 α 非零；不再逐个扩大已付运输家族。

## O4/O6/O7. 其它原全群路线仍开

[早期 O4/O6 完整档](notes/2026-11-14-open-before-r549.md)保原16域/82中心/全Hilbert迹、两整Bockstein及完整单位格。

- O4：真实 O 格 Q=δ^a εw 须 a≤1 在无穷普通/nonanomalous p 成立。E17 的 a 偶、E389 的 lengthShaA=2(a+1) 不变；指定 β(Q)=f(0)P_- 非零及变化 q 的全 Hilbert 迹早项仍缺。MW 高度、辅助原始或有限证书不代此门。
- O6：Dp=A_p/(T−p)、s∞,p=q_p+1、q_p 正奇，需 q_p=1 对无穷 p。固定两点饱和 λ:Dp→Zp 的核 Np 保全 Sha，需 Np 有限。R286 的真实 Tor、R293 两行 p^(2d) 损及所有 norm/参考不删。
- O7：R639 同解内盘、R660 闭盘共振理想、R663 真实 LT 余数/同 Y 闭盘充要已付，但未迫所有余数零。R632/635 的 z/u 半径分清，不把内盘收敛或其它 tame 支升成原闭边界结论。
- R364/R561/R654/R712 均未关闭，原 quartic 的 F/H/Theta/P/B/W、全 Laurent 二行、非恒定 Y 权、13/19 全覆盖和216真管差继续按归档。

## O5. 外部强声称核查：已付范围

R5 已反证 arXiv:1703.02215 所用统一有限 lifting 引理；否定该论证不否定主问题。R240 的原 polyquadratic plectic 输入不能直接用于 rank≥2 的平凡特征投影。
新检索的Wang2026完成声称，在Definition6.1/Proposition6.3/Theorem10.1所需K条件处矛盾：全部坏位split使w(E/K)=−1，并在原解析秩二时强制扭曲中心值0，见[完整符号反证](notes/2026-11-16-wang-rank-two-definite-sign-obstruction.md)。不据该外部声称关闭主目标。

新 Do 双二次 CM 预稿正文 Theorem6.8.5 和证明仍要求指定底类非挠；导言省略不消除此门，见[原核查注](notes/2026-11-16-selfdual-hecke-preprint-rank-two-hypothesis-check.md)。

## 第一实际门：同原映射、真 RR 与完整 shadow

原 Z 的 R804/806/811/814 角色、Euler、period、端点及 R831 的 Z02=Z/Z20=−Z 不变；7993 仅检测 canonical。R858 的三垂直χ零/generic单射、R859 的整 shadow/Chow 逆与5/11无挠 H1 已付。固定 ell 的原 AJ 非零等价某惯性 shadow 非零/阶无界，仍不能跨到无穷系数 p 或 ordinary loc。

### 原 P/F 的当前实际运行

接手前所有精确source/run/job见[完整旧open](notes/2026-11-20-open-before-v66-trace-and-run-recovery.md)；全部原u、λ、vnew、整返回17与认证界保持。

- 原F已由R909完整认证：run43906594646/job133436977753/source135b50ff04a12c51dd1b9de583a20b2bed19cbed；ℓ1000003/N512、1429行/QQ/原短支/0..6120，结果hash5193c929a0369e957a0495f12c5af244243f2b4ed444ba305bba963dfdc4831f。
- 原P现由R906§8完整认证：run44714703201/job136215000168/sourceb688d6ac703fec422a7c864bcdc997cc553185fd，原1226行/QQ/短支/同基高展开和全部0..4284恒等式均过；u、λ、原微分、∞→O及整返回17保持。结果hashd3371b55fbdbf8999f2ed6da76cc004a78eba733ff5e7977bce4149e4ecb8915，坐标仍358238d2…e7be67。此前失败和新等价算术见[续接注](notes/2026-11-20-old-job-outcomes-and-exact-P-certificate.md)。

### 真 RR、完整原函数环与消费者

[本次全量归档](notes/2026-11-20-open-after-consumer-and-long-connection.md)逐字保此前全部旧运行、公式与未闭门；只收拢当前实际接口，不删除其它前沿。R882原18源/绝对B0B2/全17方块/36cusps/D204与R880/883全18×9/双轴/原A,C、四完整除子00/01/11/12保。闭点d不可先模ell；完整Frob/Atkin/边界、真dF成本2256+r*dF或2256(r+1)、全地方Kummer负floor和Σef不变。Norm含ell²点回归run43870209568已过，不重复无变化测试。

旧306/eta48/fricke24/tate24/tate19/R910/R919/R922路线仍未全末端PASS；实际卡点/source/run/job见[续接注](notes/2026-11-20-old-job-outcomes-and-exact-P-certificate.md)。quotient-only run44713040079/job136209307176仍运行，原D完整正规化/九cusp/Au/Av/branch/D0尚待。t-adic U已在4096精度上限结束无全局候选，不能作不存在结论，不盲目重跑。

[R924](results/R924-original-section-divisor-algebras-and-shadow-interface.md)的同原截面路径已有实际成果：§11–12的run44720444485付完整TUV分式、全204维DS及51二次双点、全36cusp与120原射影标号；§13 run44721065286/job136236619274付Y完整666格、三真实退化和原ys全核360；§14 run44721641472/job136238600337付全非约化DS上的TUV值；§15 run44723394686/job136244599223付真F/P全PASS鉴定后的原vF/三Yi截面（F核144、P两核152及第三原QY），全部原u/常数嵌入/Artin保持。完整hash逐节存，不冒旧degree48函数域RR接口。

[R925](results/R925-original-ys-affine-rings-and-complete-divisor-ideals.md)由J=SY/(ys²+3)²建立原306完整过滤自由基和两张正规化图表；完整多项式核保原共零，六cusp含289重分支；§12 r29完整环实际PASS：run44724912327/job136249752863/sourcefea36d7d8，h0..4=1,2,68,360,666，全部46971乘积/两图表/单位过；14个权4元保完整W8，不复制r41。§13完整闭点/真实κ与q\q²参数、任意阶共零首项读者已独审；§16原Fp²两π/π²及八原点共零值run44730598782运行；§17–18原桥/trace及同进程紧缩→maps请求已接，三退化、全HNF理想/局部值各须实际门。

[R926§8–11](results/R926-original-cube-roots-in-sections-and-complete-identities.md)原cube全6941/4287及紧缩/完整maps均实际PASS：run44732115204/source192c28161保原M2/ω/Artin，低核84/76/74/74、1633/1429交叉及七原椭圆/全部W反射齐。原根极度240/452/454/454、同L最小权2/3；[R927§9](results/R927-original-yF-pole-degree-from-mixed-kernel-and-cusps.md)实际e=0、z=96、dF=1296，F_first及每E全度39840已付。完整pole/四E/trace及shadow仍须实际计算，固定ell不替ordinary/无穷p。

## 原端点：真实范数与剩余增广阶

R885（原文件入口见results索引）保同D、spD=Ep原AJ、原q/q⁴/4/Artin/旧副本和C5=-216。Ep真unit，Coleman有限余核支付Dfun(0)=Ep原ordinary loc；不能丢增广零。

R897现已完整给同一 finite/wild tame 系统：一侧ray普通CM商到反对角的准确识别、全部split norm/divisor-sum/统一格与n1原端点，各n有spDn=Ep,n cn且Ep,n整群环unit。R886的τ/γ辅助集最高rank-one归一保原同底。整族除T恰要求所有tame底类都零；单n1零只给trace零。

R891已直接证明原受限辅助集的anti-Kummer、17惯性Sah/Nakayama双点selector、完整四角cochain及κq(σ)=−c1(Frq)，由共轭两点global cup得 **c1≠0⇒Selbal=E c1**。扩大系数一次固定O0投影后平坦返回；坏位统一指数保。无需再补旧JNS接口，usual core0不能改套MR core1。

R893在上述非零前提下，实际Castella Cor4.6.1/控制给R814固定Heegner增广本原；D=U Z°，U为单位。全部iota/period/平滑/Euler保，得到同H单位的ccan=H Dfun·D、Ccan=H Dfun²。s=ordDfun仍可能>0；ordinary loc及同p原canonical底非零恰等价s=0。derived canonical不能套未除T的strict-kernel结论。

R897附B进一步付清一条实际限制：原Δ来源pull到full ray再trace到单侧，真Mackey关系多出h=p^vp(q−1)；γ集使Pq为unit、17惯性使restriction保持整阶，所以归一分母无界。它只排该组原pull/trace操作，不排新的单侧非平凡来源。

R900同原惰性raw norm Aℓ=−(ℓ+1)²/ℓ，真实Gauss/全部坏位给wχ=(−1)^(1+#新惰性)。实际τ后已发表compact BK零杀奇数支撑；单ℓ全Dℓ=Aℓ/hℓ resD1，真可除−(ℓ+1)，有限原类同式且Ep,ℓ全保。附A完整保旧split层，所有惰性子集有同原格Möbius分解；奇数全新块严格0，奇数总层只付min v_p(ℓ+1)整除，偶数新块未付乘积整除。惰性主理想在任prime-to-ℓ原环类塔Frob恒1，所以R891所需长剩余次数不可套；不推s0。

R901新增惰性真ℓ²端点/三old矩阵只02及20反号；原单位向量Iℓ=(ℓ+1)/ℓ³，volK1 Euler归一=(ℓ+1)⁻²，YZZ实际Haar=(ℓ−1)/(ℓ²(ℓ+1))。附A构造不除群阶的整不变泛函，真Kirillov格与邻点商格的coinvariant去torsion=O，原端点取1而为生成元；不能把球向量商格改成augmentation-kernel，也尚未证明该自然格与全局CM/Shapiro格的饱和比较。全χ/绝对度数及p非unit保，局部非零不付双新全局非零/乘积整除。

**下一实质门：** 原c1非零、Dfun阶s=0及同目标p的无穷性。继续实际同源关系或新的合法几何输入，不能把条件rank1或一个辅助层非零当成ordinary loc注入。


R901附B原全新CM商整比较：ACR完整ν_n、p′ Borel矩阵单位及真full-q/T运输给V_A=L_A⊗S_A；原两范数核整饱和等于H¹(I1I2⊗T)，唯一返回A_i=O[Gi]/N_i，N12=(σ1−1)(σ2−1)Naug且scalar p格阶不变。old/new余核O/(h)、邻点dual余核(O/(q+1))^(q−1)及原共同目标次数保，不冒原AJ非零或标量乘积整除。

R908及附A原双增loc_all N12=u₁(σ₂−1)a12及全CM/finite-wild/原D尺度均保；附A真实Igusa/Drinfeld全求和已付固定D的tame新增位局部零。R913继续覆盖完整finite wild，见下；不再从该新增位索非零，转同原global/ordinary底。旧完整式、常数及所有当时限制存本次完整归档。

## 第三实际门：同P/R/S与实际有限类

原P134/十九角/charge40/conductor10980/39carry/全WD及M=c*U0w13J不变；TM=s−r−13、TJ=s−r不混。四中央零才给H−Hc∈p³，全Λ0三carry及真实原R/S必须联立。

R872原τ1/2/3第三carry、第二页baseline与同Qc完整保留；调整口是实际K1第二长块末三尾联合像，非三个自由轴。严格f0成本3、ER首−11、E²完整短段和E³同ξ不删。全同R迫d=BD·C≥s+2。

J3=(E+40)^−1V3、J3∩V1=V4与ΠJ=0已付，但native首Bocksteinλ(J)=a^-1[w^s](5042W0−246W1+3W2)保第s值；τ1还须原normal项同页补偿。W0≥s+1仍不杀其余β1。因子层的两个strict反门与真finite/H¹按原档；不把有限目标维数认作K1满像。

R888付合法R491因子提升不变完整o(R)与整[t]R；R890付全finite reader（TF伴随模π、固定十九角/∞/非monic、同R Cech）。没有新增M零行，forcing未迫全reader零，实际o(K2)仍开。

quartic余j≤2：j0 H¹0，j1/2≤3/14；固定纤维/十九角额外零不能把A4换成整O_H−。唯一零纤维退化Y²(Y−1)与ρ−重合一行，其余秩2；全Gauss/G1/K1仍保。4z−≤1+6j与z3的Y²/t³返回已付。

同R零类反门：
$$
o(R)=0\ \Longrightarrow\ 14s\le3B_D^2+8D-26-12j.
$$
所以p/D²>141/28（含47/8）迫o(R)非零，仍未排完整p³。第二核在d<κ+s+2时零类返V2+J3且含t²，同P的完整o类固定整[t]R；不能借不同来源重选有限类。

R895不假oR零，由同R交数和同P有效除子得
$$
N_D-2s=\ell+\delta_D\ge D+16+2j.
$$
反门≤D+15+2j真排原τ1 quartic p³；δ可负，三长记号须另加s。
R896取逐p最小N_D≥2s时，统一低松弛集在p11mod12中密度12/47、全素数3/47。只排该quartic来源，不覆盖一般K1，也不授权改已固定D/k旗标。

**下一实质门：** 同一实际有限类与全K1高前缀、β1、R/S后页的联合约束；未覆盖quartic及非F²来源仍需处理。不再重复全局reader已付分类。

## 第四实际门：同修正高前缀与指定WT类

R834/836/837的全单位块、原真三长/两长预算不变；自然Bost47/12缺q1/2，47/8须真第三长。
R840须用同Kcorr/Hcorr支付两个高前缀，再用同F²L1付第三3η/第四短行及末同cF³；R842的WT上指定[b0]=−BD−Pr仍未知。所有negative/moving/十九角/奇点/∞/disc²保。

当前未闭范围是原R836的2κ<T≤3κ，不能拿quartic的另一范围冒已付。
即使第四短段延到T−h，也不能从V0,V1,V2∈V_T推V_T对E稳定；
第三长行仍缺同E³G的ell_eff..T尾。V1=0分支中EG=FA、A∈H2，只有A|C=0才回已排块。
R902新付同原四块核中V1=0分支单射H⁰(N²(−H*P))，H*=min(T,h+ell_eff)；H*>2κ真使G↦V1单射。ell_eff≥T−h时进一步进入W_T∩H⁰(N³(−TP−Z−))，同指定完整目标/同V1至多一来源。所有T−h>κ、T>3z−、3b<p、F0非零和qsrc H3返回/真帽仍需成立；未证明实际像满、Euler稳定、指定[b0]消失或删其它WD列。继续非零V1的同一二步链。


R903：原全四块核的正水平值V1−3bV0单射已证：最高charge真帽ord0 a≤3(e_++μ01)、全局L=E−3b除F及最高系数逼c0。原r2/m0=3/b≥5时κ≥(b−3)e_++3b自动付帽门，非零核必要T+e_+≤3κ；同U±保共同V2与D3(U−−U+)=3b res U−，不相加独立秩或认实际像满。

R907：原全四块核内V0(H)=V1(G)唯一迫H=TG=EG−a(G)F³，a由原第四短行固定；两条完整native尾仍须共同通过。r2/m3所有纯charge真帽给稳定部分零纤维单射，明确六维Tf/Qf并以3b+7步原四块测试精确读K∞；未认全K稳定或指定forcing已解。 原L≤h时等价V3高T及V4−6ae³的同L尾；L>h真迫a0。下一步仍是实际非稳定部分与同指定目标。

## 持续执行

完整目标尚未达到。每条完整证明立即推；每次实际pull核两README差异、只读变更并记已读提交，至少每小时。只在公开Actions作数学执行；脚本/参数/run/hash入库，重算输出不存。主目标完成前持续接续。

R907§6.1：若第四短窗L>h，实际相邻后继先迫a(G)=0；原全charge单位投影给K∞=0及∩_{j=0}^{3b}T^{-j}K=0。只排完整共同测试，不排单个非稳定K元素，仍需原forcing提供真实后继。

R910：保持全次数的一个无重根特化严格认证泛型可分；原两Phi17的线性子结式经非零首项唯一恢复同U，整eta分母求值后复核两完整关系。新同tate19 producer保全四RR块/两Atkin/205行及DS返回，仅替换已定位gcd卡点；实际新run尚未取得PASS。

R910首run43912835484/job133459031944/source d622da0c在子结式多元回转中触发RecursionError；已改直接k[x,v][Z]系数向量读取原线性项，完整数学门不变并重请求；无RR PASS。

R907§8把真实反馈接到原GRes：m0..3=0，m4/m5为完整Jacobian乘法迹；同Qf(T)公式保两实际原点jet及−45项，不除Ft/f2、不删非稳定来源的左边或边界。

R887§20同原Fa的共同有限p算子满足L^p=V^pL；全部Fa的A加权Cartier质量为同非零H，原四行仍保Wν。显式Y=(Fb−1)/b−(Fa−1)/a给真实exact差与十二阶零，四η准确归到同F6²及全部−Yνd(WνF6)伴随；未付四中央联合非零或p²边界。

R887(116a)进一步准确给C(Hω)=0及C²(𝔄Faω)=0：rω=(1/3)dlog y与[G]_(p−1)=−r^p严格相消。共同非零质量不传到最终中央；继续同Wν和全部带权伴随。

- R911：固定五/六长行的完整重复根能量给13(T−vG)≤27κ+312b及16(T−vG)≤27κ+384b；保十九角/真实3C。L>h时实际三/四项后继链反门给整K维数≤2dimVT/3或3dimVT/4；同F且余因子unit的当前quartic强制L≤h，不能借此补它的forcing。

- R912：原[p]除点函数/首一Φp给完整𝒯^p²=𝒯(pv−v^p²)S/Sc；全2p²−p−9窗代入误差p⁵，规范根除p²后保p³。原多项式modp⁵严格恢复LT坐标modp⁴和原根modp²，完整V⁶Vc^(−m)R^(−m)P(bv⁶V⁶)支付全部两位输入/首层因子；中央零⇒全部边界零仍开。

- R914：在原T−h≤L<T（含L≤h）的真实窗口，Qf(T)先把同源合成送入全零纤维，再准确使T=E；R911五/六长反门给K∞=∩₀⁸T^(−j)K或∩₀⁹，故9dimK≤8dimVT+d∞或10dimK≤9dimVT+d∞，d∞≤6。全部反馈a_i/实际GRes左边保，不判指定forcing。

- R917：原X0(867)全尖点线束deg204的204m+1个jet给整饱和像；任一已认证QQ模形式基经严格终止的逐ℓ饱和，准确恢复全部M2m/ℓ及原L(mDS)。固定子式赋值逐步下降，无高度猜测；完整全局q格不冒现有degree48坐标/闭点/全部RR前端PASS。

- R916：实际f=λY²(Y−1)、1≤ord_tF(t,0)≤2时，原F³的0..5六系数至多一个恒零；故真实K∞≤1，全非零则0。唯一可能方向Bn+c(t)Yn由完整十九角纯charge格Pn·k[t]≤Mn及同T前缀准确判定，εF0/1给R914联合秩加强；原Λ只缩到一条实际GRes，未判其非零或forcing。

- R917 §8：公开run43919854829/job133483895189/source4519983a已完整认证原ℓ29的120×205全局RR格；固定子式为单位、原QQ变换/全约化秩/同S全部通过，2.549秒，结果hash5a1d6494…eb663b。只付全局L(DS)及忠实jets，未提供degree48坐标/闭点或现有四块接口。

原fricke24 run43860032290/job133274126644/sourcebe4e0074已于17:33 exit137；完整24次原支已选，最后阶段是原U恢复，未到正规化/RR。全部阶段/hash见[实际卡点](notes/2026-11-16-original-rr-stopped-before-normalization.md)；不能将此终止当数学反证或确定OOM。

- R919：原多项式环内逐系数真除法/复乘与次数严格下降，余式在一次处停止而不造无用S0；所得仅作候选，仍由原eta域的两完整Phi/绝对支/两Atkin及全四RR末端认证。新独立公开路径已请求，尚无PASS，不猜当前R910实际卡点。


重读已发表 R708 后的接续校准：原 m34/72/136 已有非零迹赋值≤3/4+o(1)，故大p边界零等价于约3p/4个原 Gaussian 块 g_m,h 的模p前缀零；不必将两位门当唯一途径。这些指标读 z^(dh)=w^(sh)，实际最高次数仍是 O(p²)，不能借 R887 仅前五块的替换免费延长。原中央零只给含真实除p商的部分和，不自动给逐行零；V66此门已由R923补齐。此处更新既有门的优先级，不登记新定理。

## R918：原首 Bockstein 对稳定方向的实际新约束

R918真实三首十三带完整读取：δ=r+2h−s∈[−13,−1]时同q卷积行给单位·a(G)，完整β1在R916实际K∞单射。δ≥0三带零iff值深到J=T+13；若q(0,Y)=cY，native给(3n²−1)vG+9a(G)u0²e0·1δ0=0，δ0首值非零、δ>0再深1。完整U0/实际高轴/q导数/同R,S保，未排非稳定核。

继续同一 K′=K∩ker(完整β1) 的真实后继链与指定 forcing，不以稳定部分单射替全核排除；δ≥0仍用同一个候选继续 native/其它行。

- R919 §6：原四块RR及正规化只依赖同一D,s,L和u/v/at，可先执行再做U；新geometry-first路径在完整原U/两Phi/两Atkin之后才返context。仅重排依赖，未删接受门，尚无新PASS。

## R915：实际连接整窗与原中央核的第二位

R915附B将原a_j连续整窗准确推到j<N=p(p−1)，首a_N赋值−2且p²a_N≡−pc；全C_r,k/两位反馈保原Vc，长输入p³−p须重付。旧全i单位核1+p²及binom(i+2,2)a1/(mc²)不变；四来源/regular/真除p商均保，中央→边界仍开。

## R913：完整finite wild惰性局部零及同格除T

R913同一finite wild全层新增惰性位D_p loc raw=0，D_p=p^c_pD只固定每p且不随n/q/b。原diamond表/完整det/half-norm/sf/整CM-Shapiro全保，不作p角色平均；先回原局部T/(q+1)才取零。全部Möbius新项同杀，若实际同格可除T则局部零保持；不推s0/global/ordinary，未付c_p=0或跨p统一尺度。

## R920：完整首 Bockstein 核的真实三／四来源链

R920一般原零纤维的K′=K∩ker完整β1：三首13带使前三实际行深J=T+13。δ∈[−13,−1]的真实相邻后继由2h<J迫a=0、H=EG；V0/V1同入VJ，K′∞=0。S=min(J,s−4)=T+11为原R821已付窗；五/六反门给真实三/四源链单射，3dimK′≤2nJ或4dimK′≤3nJ。全部q/U0/19角/同R,S保，固定P首修正差仍K1、不能自动换K′。

- R920 附A同固定P的两完整p³解有β1(ΔR)=0；若ΔR真在j(H3)，四块等价才给ΔR∈j(K′)。固定一解且S在全原源格自由时，该R陪集内可延p³的类准确为R+j(K′)；S受限时只保必要式，未判p⁴。

## R921：真实残余连接线与全局Bockstein读数

R921m≤e=v_p(q+1)时完整残余H¹有原整提升线L和H0连接线C。原j_*到Shapiro(U,S)矩阵diag(u,0)，corestriction为diag(0,1)；β_m(C)=−u p^(e−m) modh同构到整H²[p^m]，kerβ=BL。完整全局Bockstein的q定位准确读C坐标，原ordinary两p位H0=0；全素点/其它群环/wild均保。几何loc零只控L，未判原derived C/global/ordinary/s0。

R915附A完整Vc/Sc两位与Lconn=2p²−2/ψp/Φp modp⁵输入均保于原节，未增加中央零。

- R922原对称Phi17差先真除x−v，各伪余式立即消系数content并全式复乘；次数严格降、一次即停。仅候选，仍须同eta48域两完整Phi/绝对支/两Atkin才认原U。新独立公开运行只付U，不冒正规化/RR/shadow，无PASS。

## R923：第四来源原全迹接口已补齐

R923：原V66在共同E17模型的完整因式给固定分母D66=154224，保−17/11物理缩放、原绝对根与全部Hall/Galois相位。完整全迹有3/4+o(1)高度，非零赋值同界；原首边界零恰等价约3p/4个Gaussian块的模p前缀全零。四来源的全迹接口均有，中央零到边界零及无穷p联合非零仍开。


## R928：固定原P的实际仿射类

R928/R934保真除p商与B给固定P全局coker类；同H1只付选定行，受限S全p³门独立。R936已给正水平实际左行及其完整B偏移，仍须定位实际陪集。

## R929：原系数后两位与完整 Gaussian 前缀

[R929](results/R929-original-hypergeometric-two-digit-blocks-and-gaussian-prefix.md)原r_n精确三带与单位积付整个n<p²的p logΘ modp³，p倍指标保额外一位；原F/κ与R614直接U/W整性给严格n<(p²−1)/6内原g modp²，四源全J≤p−2前缀/物理缩放及第一真carry均保。不是中央⇒边界或联合非零；下一门直接用这些同源实际系数判断原部分和。 附A由真实duplication/两负块反射给g_p≡2Q_p+p(Q_p²+L_p^U/2) modp²，保Q_p的第二位及原全块倒数商，完整D0列逐项返回。

## R930：同一真实首核的联合尾像

[R930](results/R930-original-quartic-native-tail-joint-right-inverse.md)同原quartic的Y_j=t^{−(τ+j)}P在σ_t≥τ+m、ell≤s−h−m时给原K1末m尾三角右逆；同q返回qt²H3及负fringe自动σ=τ−δ−1，δ≤−4付全末三尾。它们β1非零，只可按准确页数同调S或较早R；其它normal响应/受限S差格/固定R928类仍须真付。

## R931：完整厚代数的原Tate求迹

R931§1–10完整厚范数方法、基础和上层均已独审接源；原六类全长度/曲线/双aux双chart/每line单位/原k所有π层及18×9保。独立run44747799006/source632cef5af先核两原图1530与非Fp范数，后付四E/trace；仍在运行，无新PASS。

## R932：同源尾调整的完整normal回传

[R932](results/R932-original-quartic-complete-normal-tail-adjustment.md)同R930全部方向以d-primitive因子同提升再撤回原规范，完整四块β1代表保ξ/C1/C2与真尾移位；同A_b(t)逆全部末m尾并返回所有normal。非零尾目标有ε² normal首单位(2u0/3ae0)b_v，严格在原窗；这不是whole-coker左行。仅需旧m0的<s轴，受限S仍核整差格；下一步同P固定偏移/真实左行值。

## R933：原首Frobenius系数的严格低读取

R933附A已完整付原W五块p^(7−h)、γ p6及r0真除p端点，恢复L5 modp7和实际E_p=4γ^6jS−(4γ)^6jU。规范2的K6真carry相消，−9/35不能单独迫非零。

R925§22三个已审优化已接完整Tate与closed/local公开运行44744769424/44744769326，31源全等，旧作业保来源继续；无新增PASS。

R934保同P全J双jet及B真除p偏移，完整式见原节；R936/937继续实际陪集及同H1，受限S全p³仍独立。

R925§23/25已写原P152完整低核两图零极读者，原recipes/j³与所有余行/完整boundary保，分别全度2256；尚待运行。§24全分母HNF逐306源行完整返回gI；两个实现均未接现有消费者。

## R935：同一原全部修正的准确预算排除

[R935](results/R935-original-negative-fringe-all-correctors-budget-exclusion.md)：全原R/S的首法向与严格f0给d_D≥s+2；§7第二法向在d0+2≤τ<min(h,ell)读28首项并分C重数0/1/2。但当前2κ<T≤3κ的共同预算已被原P的d_D≥4κ+3r_src蕴含，不是新排除；真实H1/全余核及受限S继续。

R931§11/11.1同原单位HNF认证全商循环或这次真h=c·1 mod I，完整R-module给原k Res(detI,c)，全厚度/omega/gcd保；值miss回全π层，独立helper仍未接运行。

## R936：同P正水平真左行的实际评价

[R936](results/R936-original-positive-horizontal-dual-and-fixed-quartic-value.md)：原正水平全H⁰(N³(−Z+))在K+e+>3κ时给确定λ+及完整Z商的唯一ν，真杀原T_J。2≤τ≤d0+1的同P评价为−11U*(0)/a−λ+((EB−3bB)|C)；已指定B∈H3才得单位非零、排该原陪集全p³。可进入旧T cutoff后≤12位条带，不排其它WD陪集。

## R937：双jet之后的同H1真实非零行

[R937](results/R937-original-quadratic-horizontal-dual-and-same-H1-obstruction.md)：原Q+=(E−3b)(E−3b+1)沿完整2H+消失，n=h+τ−2且n+2e+>3κ给真四行左行。指定B∈H3、d0+2≤τ<min(h+2,ell)时值为原单位28ζ0^(−s)uhat0³e0/a；每个兼容G0后同ρ2杀全F²H1而残差不变。双jet已零仍排该陪集，τ=h/h+1精度保，一般B偏移不删。

R937附A/B：同q全部合法native尾方向对两条固定行零响应；给定H3加该族的陪集在J>3κ，或高τ的J+e₊>3κ且n+e₊>2κ时，完整实际列与相继除F给非零单位左行，且每个兼容G₀后的同H1残差不变。β₁/一般B/其它WD及受限S保。
