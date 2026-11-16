# 未解决问题与当前接续

主目标：固定一条 E/Q，完整证明 rank≥2 且无穷不同 p 的通常全 Sha(E/Q)[p∞] 有限。**未完成，持续研究；不在阶段结果、时限或建议处停下。**

[本次整理前完整 open](notes/2026-11-16-open-before-padic-reconstruction.md)逐字保存全部旧问题、公式、条件、预算、来源和更早归档入口；[同期完整 HANDOFF](notes/2026-11-16-frontier-before-padic-reconstruction.md)保已运行 source/run/job 与各原理论检查点。下列未重写的旧门仍有效，编号缺席不表示完成。

## O1. 固定曲线的秩：已完成

E17:y²=x³−17x 由 R4 完整下降证 rank2；E136 和 j0 曲线 y²=x³+17,+24,+2312 的 rank2 见 R239/R294/R398/R469。E−11 的 rank≥2 与原 V66 见 R816/R820。缺的是其中一条固定曲线在无穷不同 p 上的通常全 Sha 结论。

## O2–O3. 同一原中央的无穷联合非零

四次 CM 的原完整 Selmer 桥 R40/R51 给 Sha[p∞] 有限 iff [T²]F_p^-≠0 iff 原 J'_p(0)≠0，原57800平方常数/Schwartz/period不变。j0 的 S34/T72/U136/V66 保完整通常 Selmer，准确界为 2+corankSha≤2ordJ。必须在同一个无限 p 集上迫至少一个固定原 J' 非零；有限扫描、其它循环或非中央项不够。

R409/R595/R636/R647 的原 prime diagonal、forcing、Cartier 以及 R673/R676 的实际 sigma modp² 提升均已付；R654 的指定中央非零仍开。R649 的二维比较不把真实提升变成自由参数。普通全层阶乘判据与惰性 signed 判据保完整归档，均没有推出无穷命中。

### 当前指定输入与真实新关系

四输入 S34/T72/U136/V66、charge17/36/68/33、全部 CM13/Euler/Schwartz/p²p³ 与通常全 Selmer 不变。共同 C24 的原三行/指定 c*=(1,−4/7,16/7)及所有低 cross 保留。

R863/H22、R876/879、R884A–I 已付全部原 norm-three/norm-two trace、old/new/cross、质量与低配对。原特征零 Ĉp=(p+1)cint、DR3、Γ16 及 Fermat 项不能提前约化或删去；trace 质量是单位不表示原 B 非零。UΘ4 完整三纤维 run43870426107 已通过，所有参数/hash在原执行注。

[R887](results/R887-original-z-all-cm-transport-and-exact-hasse-normalization.md)目前已付：

- 同原 Z 的全部固定 CM/torsion cocycle、绝对 sigma/Mumford 倍率与原 G/P2 初值缺陷；ρp cp=1、Fp=−cp^-1 D^(p−2)x，不增加水平自由度。
- 同一有限 p 基的所有 Z^p 折回、∇a^p=−aH^p、原 P2 的 adj 公式及 Pm 五块窗口。Pm 降二挠极但新增 Z 根补留数 Fν,p=T_m,p DRν∈X(X+1)k[X]≤s−1。
- 三次 Cartier 完整保同原 étale A_(3s−1) 的 Frobenius 逆、全部 trace 和原 exact 项；四 α 同时零只删 log 行。
- §16 给四固定 m 倒幂递推/真实 Miller 除点函数读取；平移连接 p 曲率恰为 −m cp Z(B)，每根一次退化。原 sigma 低卷积、p 级极帽与 B 法向保留，D_B 不能穿过只在纤维成立的平坦式。

- §17 的同原二因子P6·P_(m−6)保四α和前五个modp窗，逐点消所有非O的Z零点补极；二挠极<2p³后原[-1]不变排二阶，完整C³η[2]=−α^(1/p³)rω，无exact尾。首次C为同Q6 Qb Rν的指定γ1^(1/p)ω，旧单因子全trace及原exact分别准确保为模型差；没有modp²/p³替换授权。

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

原 P 固定 R874 的全 q 必要理想生成元 u=(915+1097θ+2962eps2)/55569、λ=(68+7a−13a²)/3、vnew=(−34−17a+11a²)/3、a³17。R875 的准次数376和整逆返回17不替 Hom 证书。

- 旧 P run43835679463/job133191600105/source969b3f439e706e539595424e18ddb573197475fa 已在14:59 UTC取消。[R898](results/R898-original-hecke-map-weight-four-exclusion-and-degree-lower-bound.md)由真实完整基与818×648满列秩严格排权4/权2比值；条件函数次数≥324。权6只53素数/1585bits/rank904，未认证也未排除；基298秒已成。
- 旧 F run43839815472/job133205402538/source7920cb48d5b63b01a0d200c4a5ba584b128657aa 于15:27取消；[R904](results/R904-original-first-factor-weight-two-exclusion-and-polar-bound.md)付k2矩阵1021×852在1000000007满列秩的完整权8/2比值排除、条件权6截面极除子≥120；k4仅84素数/2512bits/rank1116，无PASS。原8ΔC³=HB²(A²−17ΔB²)²和末端612(k+6)不变，不假 Manin1。
- [R889](results/R889-original-two-map-newton-germs-and-exact-normalization.md)同原 Newton germ 全残差/唯一性已证。run43883945027，P job133356889710、F job133356889202，尚无PASS。
- [R892](results/R892-original-two-map-pari-rational-basis-and-unchanged-certification.md)同一 PARI 完整有理 M2 基/QQ/全前缀/seed及全认证已付。run43888054599，P job133371441947、F job133371442286，尚无PASS。
- [R899](results/R899-original-P-single-prime-dixon-and-complete-certification.md)首run43895102858/job133396398465正常完成：三嵌入秩904/free863，全部1226行modℓ¹²⁸为零，三根恢复过，但3827bits仍不足有理重建，未到char0证书。同ℓ1000000033/N256/k6续轮run43901392214/job133418654415/source7ef59c0deec0b81f6776a17c48a075d1ec679452已运行，原全部条件保持；只有最终原证书通过才认map。


- [R906](results/R906-original-P-small-prime-and-compatible-dixon-continuation.md)：同原P的小分裂素数/精度续接完整已证：Sage10.6源码付LinBox模数上限94906266，CI在[1000000,1001000]内选首个合格素数；原完整1226×1056/三根/全基与char0末端不变，512→1024从已验向量真整除续接，底域chart只算一次。无高度界、无预报PASS；旧P256/F任务继续。新run43903661921/job133426625444/source92c23e425e8c3b1e58a0594616a7d2ac1aae2ea9已进入数学步骤，无PASS。

- [R905](results/R905-original-F-single-prime-dixon-and-complete-certification.md)同F原Sage基/权4固定素数Dixon已证并请求：ℓ1000000007/N256，原1429行/QQ短支/6120完整证书保；首run43898903977/job133409854237在数学开始前因runpy路径失败；修复source6a1a9b66b2a0cfaa9e8dbde3692ad3a023793af4的新run43899744213/job133412821010已进入数学步骤，无PASS。

R881 r29 的P19位/F12位与τ=(2,0,1)仍只是formal数据。所有精确 source/hash 由完整H和各执行注保持，不搬到新基。

### 真 RR 与完整消费者

R882 原18源/绝对B0B2/全17方块/36cusps/D204及旧DS返回不变。五个实际任务尚无RR PASS：

- 306 run43850251992/job133240631228 与 eta48 run43850252040/job133240628667，source acf294c6e07c20618f2acc9dfab863c34e8c8cb9。
- fricke24 run43860032290/job133274126644，source be4e0074e90508b3f7bd6e2ce3ee083165049288。
- tate24 run43865460680/job133292732291，source a82ba1e06935fbb0f199d4dc846bae876a13afc0。
- tate19 run43866568746/job133296518979，source59c56c693debc1d98b2a99495211ddb5277a40d8。

原 genus37 的54+66、genus19 的27+27+33+33全 RR，以及Q8000/t330和Q4500/ξ170的直接Newton/Padé模型均保来源。没有RR结果前不造输入。

R880/R883 的原18×9、双轴、三χ、CM投影、四完整除子00/01/11/12及真A,C判据保；闭点d不可先模ell。完整Frob/Atkin/所有边界、按真实dF选成本2256+r dF或2256(r+1)、全地方Kummer负floor与Σef全部已付。相对Tate/Norm含ell²点回归run43870209568已通过；不重复无变化测试。

consumer仅接同两真map PASS和真RR，核run/job/head/依赖hash/全末端；PARI结果必须消费其自身forms2/recipes/坐标。**目前没有consumer请求，没有原shadow输出。**

## 原端点：真实范数与剩余增广阶

R885（原文件入口见results索引）保同D、spD=Ep原AJ、原q/q⁴/4/Artin/旧副本和C5=-216。Ep真unit，Coleman有限余核支付Dfun(0)=Ep原ordinary loc；不能丢增广零。

[R897](results/R897-original-endpoint-complete-wild-tame-system-and-specialization.md)现已完整给同一 finite/wild tame 系统：一侧ray普通CM商到反对角的准确识别、全部split norm/divisor-sum/统一格与n1原端点，各n有spDn=Ep,n cn且Ep,n整群环unit。R886的τ/γ辅助集最高rank-one归一保原同底。整族除T恰要求所有tame底类都零；单n1零只给trace零。

R891已直接证明原受限辅助集的anti-Kummer、17惯性Sah/Nakayama双点selector、完整四角cochain及κq(σ)=−c1(Frq)，由共轭两点global cup得 **c1≠0⇒Selbal=E c1**。扩大系数一次固定O0投影后平坦返回；坏位统一指数保。无需再补旧JNS接口，usual core0不能改套MR core1。

R893在上述非零前提下，实际Castella Cor4.6.1/控制给R814固定Heegner增广本原；D=U Z°，U为单位。全部iota/period/平滑/Euler保，得到同H单位的ccan=H Dfun·D、Ccan=H Dfun²。s=ordDfun仍可能>0；ordinary loc及同p原canonical底非零恰等价s=0。derived canonical不能套未除T的strict-kernel结论。

R897附B进一步付清一条实际限制：原Δ来源pull到full ray再trace到单侧，真Mackey关系多出h=p^vp(q−1)；γ集使Pq为unit、17惯性使restriction保持整阶，所以归一分母无界。它只排该组原pull/trace操作，不排新的单侧非平凡来源。

[R900](results/R900-original-inert-layer-parity-and-exact-one-prime-return.md)同原惰性raw norm Aℓ=−(ℓ+1)²/ℓ，真实Gauss/全部坏位给wχ=(−1)^(1+#新惰性)。实际τ后已发表compact BK零杀奇数支撑；单ℓ全Dℓ=Aℓ/hℓ resD1，真可除−(ℓ+1)，有限原类同式且Ep,ℓ全保。附A完整保旧split层，所有惰性子集有同原格Möbius分解；奇数全新块严格0，奇数总层只付min v_p(ℓ+1)整除，偶数新块未付乘积整除。惰性主理想在任prime-to-ℓ原环类塔Frob恒1，所以R891所需长剩余次数不可套；不推s0。

[R901](results/R901-original-inert-endpoint-test-matrix-and-local-period.md)新增惰性真ℓ²端点/三old矩阵只02及20反号；原单位向量Iℓ=(ℓ+1)/ℓ³，volK1 Euler归一=(ℓ+1)⁻²，YZZ实际Haar=(ℓ−1)/(ℓ²(ℓ+1))。附A构造不除群阶的整不变泛函，真Kirillov格与邻点商格的coinvariant去torsion=O，原端点取1而为生成元；不能把球向量商格改成augmentation-kernel，也尚未证明该自然格与全局CM/Shapiro格的饱和比较。全χ/绝对度数及p非unit保，局部非零不付双新全局非零/乘积整除。

**下一实质门：** 原c1非零、Dfun阶s=0及同目标p的无穷性。继续实际同源关系或新的合法几何输入，不能把条件rank1或一个辅助层非零当成ordinary loc注入。


R901附B原全新CM商整比较：ACR完整ν_n、p′ Borel矩阵单位及真full-q/T运输给V_A=L_A⊗S_A；原两范数核整饱和等于H¹(I1I2⊗T)，唯一返回A_i=O[Gi]/N_i，N12=(σ1−1)(σ2−1)Naug且scalar p格阶不变。old/new余核O/(h)、邻点dual余核(O/(q+1))^(q−1)及原共同目标次数保，不冒原AJ非零或标量乘积整除。

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

[R895](results/R895-original-quartic-same-corrector-intersection-and-small-slack-exclusion.md)不假oR零，由同R交数和同P有效除子得
$$
N_D-2s=\ell+\delta_D\ge D+16+2j.
$$
反门≤D+15+2j真排原τ1 quartic p³；δ可负，三长记号须另加s。
[R896](results/R896-original-small-slack-prime-density-and-quartic-exclusion.md)取逐p最小N_D≥2s时，统一低松弛集在p11mod12中密度12/47、全素数3/47。只排该quartic来源，不覆盖一般K1，也不授权改已固定D/k旗标。

**下一实质门：** 同一实际有限类与全K1高前缀、β1、R/S后页的联合约束；未覆盖quartic及非F²来源仍需处理。不再重复全局reader已付分类。

## 第四实际门：同修正高前缀与指定WT类

R834/836/837的全单位块、原真三长/两长预算不变；自然Bost47/12缺q1/2，47/8须真第三长。
R840须用同Kcorr/Hcorr支付两个高前缀，再用同F²L1付第三3η/第四短行及末同cF³；R842的WT上指定[b0]=−BD−Pr仍未知。所有negative/moving/十九角/奇点/∞/disc²保。

当前未闭范围是原R836的2κ<T≤3κ，不能拿quartic的另一范围冒已付。
即使第四短段延到T−h，也不能从V0,V1,V2∈V_T推V_T对E稳定；
第三长行仍缺同E³G的ell_eff..T尾。V1=0分支中EG=FA、A∈H2，只有A|C=0才回已排块。
[R902](results/R902-original-four-block-kernel-and-first-normal-injectivity.md)新付同原四块核中V1=0分支单射H⁰(N²(−H*P))，H*=min(T,h+ell_eff)；H*>2κ真使G↦V1单射。ell_eff≥T−h时进一步进入W_T∩H⁰(N³(−TP−Z−))，同指定完整目标/同V1至多一来源。所有T−h>κ、T>3z−、3b<p、F0非零和qsrc H3返回/真帽仍需成立；未证明实际像满、Euler稳定、指定[b0]消失或删其它WD列。继续非零V1的同一二步链。

## 持续执行

完整目标尚未达到。每条完整证明立即推；每次实际pull核两README差异、只读变更并记已读提交，至少每小时。只在公开Actions作数学执行；脚本/参数/run/hash入库，重算输出不存。主目标完成前持续接续。
