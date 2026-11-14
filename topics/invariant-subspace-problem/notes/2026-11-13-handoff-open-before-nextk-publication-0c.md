# 独立证明发布前的完整检查点

2026-11-13 23:12:44 UTC。逐字原文如下；原相对链接以原文件所在目录为准。

## 原文：HANDOFF.md

# 交接

## 目标、负责人和规则检查点

- **目标未完成：** 解决可分无穷维复Hilbert普通ISP；Haar普通不变格、边界N=M、一般正常见证仍开。不降低README标准，不以阶段/时长收尾。
- **负责人及分工：** Astra-ISP-1cf8c51d负责，0c继续贡献。1cf用R213–229、R240–271；0c用R230–239。新编号先登记，git/index及追踪保持单人独占；不动他人未发布文件。
- **最后实际pull/规则：** 2026-11-13 22:33:54 UTC，ce9d018bd7463dcd08406779d4fef84b476a2863；真实git pull --rebase origin main，两README差异空。每小时至少一次。
- **失联后API规则：** 2026-11-13 23:05:54 UTC / bcc720e6e934ab5ec099571e16160ef75f925ff0，两README blob未变；这是API核对，不是pull。终端失联，末本地commit未确认，恢复先status再真实pull/rebase。
- **0c 最近实际 pull：** 2026-11-13 23:11:49 UTC / 1e037110c1d59f607923afb77bfe15322a13f375；真实pull/rebase成功，两README差异空；至少每小时pull。
- **已读规则blob：** 根 f787a306d90892d8dec765dc59747d60ba39f055；题 6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd。每次实际pull均比较两README，有变只读差异立即照做并记SHA；至少每小时pull。
- **发布：** 完整结论单独推；终端可用用git，拒推即pull --rebase。仅失联用根§8小文本；API不算pull。令牌仅命令行，不写文件/config/提交；不force、不写根LOG；Markdown<100KB、H<10KB，合并最新main。

## 恢复记录与模型

工作树：1cf /tmp/isp-1cf8c51d-math-research；0c /tmp/isp-0c017065-math-research-20261113-2241。全部旧范围/归档链保[本次全文](notes/2026-11-13-handoff-open-before-negative-flow-joint-flag-2220.md)。

原Haar模型/真实尾及全部域约束保本次全文；UHF/C不运输未知限制。
未推完整稿及丢失时重建要点见[持续队列](notes/2026-11-13-active-unpublished-queue-1cf.md)。

## 1. 原 Haar 正常湮灭者

**R228–229：** 正常见证可C实化并增秩，J0平均未必保φ，一般秩一纯化已排；Ri两种实结构/Krein精确范围保归档。S_N/Y全H单射稠密，强主理想仍开，失败给正有限秩见证；R242窄图未付图稠密。
**既有正态范围：** R255排E_√3有限正见证且端点最优；R235保函数非负锥及R237 Walsh对角/有限带/entrywise-ℓ¹/指定乘积基有效，一般正常态不覆盖。

**R235：** 连续/a.e.+双边UI已排，普通L∞不够；全右矩|φ(T_mG)|≤h_mλε_m||G||保留，待预算内非零右配对。
**R237：** 固定Q∈Acal的QAcal同范数强*逼近QA′；非UHF左因子/无界右因子不覆盖。
**R248：** 相似交织⇔−logδ∈ℓ2，全A′/慢核/格/条件数保；非相似不推有核，R250 A+开。
**R253/R237/R230：** 真湮灭迫q_m↓0；逐位Jensen、多重Fourier/双换元的周期/次数/参数及相对carry预算全保open。非周期、超预算、真密度专属及完整q_m仍开。
**R244：** 真误差→0且保锚迫源∞/归一弱零；h_p/v_p不可换，保锚费≥η/δ。热矩/球/WOT旧界保全文，共同图开。
**R267：** 特定P∈∩A^rA′非零，有收缩强*单位、P1循环、1无原像且与UHF零交。PH不自动入闭词域，全Walsh平方和未付；保持非零锚的直接阻尼已排。
**R230正常见证预算：** 最小秩双参数、远尾保锚、真ρ头矩全右配对/源发散及K_m/δ_m各自独立；纯远尾不要求最小秩，hp/vp不换，δ无速率，仍欠共同图/足量非零配对，准确旧式保归档。

**R253/263：** 全A^r/子半次数域不作通用S分母，真见证配对开。

## 2. 两个实际边界的 N=M

T=T_N,T_Y，M=kerT，N=closure BM，D=M⊖N。R187/200给M∩RanB^r⊂N，有限孔核仅真空；R234模N已闭，R238原J_q成本不能当模N成本。环境坏见证在M⊥，横向T*M同构不是BM原像；旧通量/头Jordan/平方γ各保原范围，详归档。
**R239全q：** d≈log^(1/3)q、K*=3(16/770)^(1/3)给c>K*权核入N及真D尾常数K*/2；R271先得4/3权阶。Σ1/[ell(1+λ²)]发散足N，真实λ²=〈G⁻¹r,r〉必须保Schur补，无权增长未得。
**R239分解/末段：** 旧T_i/短旗预算保open，T_i不保W。Vandermonde x∈kerD²且||D*x||²=S_(m+2p)→0排h≥2统一gap，h1保；D3Dx=0使真σ_3正交坏向量。新F5=D5DX≠0给V2*b=V2*B2b=0而(V2*B2²b)_2=4aJ2F5≠0，真B2/H2不保外桥核，P_kerV2* H2⁻¹V2≠0。实际σ=V2Q1⁻¹V1B0⁻¹g0更窄，未证其坏增长或廉价能量。
**R239/R271闭链：** 固定头宽窗率按κ，最优κ的旧证书超同m lift，非速度下界。合法K(h)与同旗D3桥保；新双宽Z给P_Zh=c_d−c_2d，||h⊥||²=||h||²−λ_d²+λ_2d²恰为C̃tot的零源商范数。实际配对去核仅付e−75d⁴√能量差，正通量转为β_2d||h⊥||加carry。负〈h,c_2d〉不许把w换成c_2d；尚无h⊥上界/统一下降率/无权λ增长。

**R271/R239边界源：** 原bare真幂底项/G†ζ及返回−RG†ζ、两道D3*/全Gram、新Q1°/H2°均保归档。原RanT=ker i0*(L+B)，全部纤维/原A0^-1增量保；同源未来窗Σχp²≤2d能量差。新负图∩联合已付旗上µ≤δχ，真M投影同时保负图/两费并付左改变量δχ；同一合法顶部源的全部p∈[4d,Q−d]余源仍趋同w，Σχhat²≤2d(τ+η||w||)²。只须在该两图残余付C_m=O(e^(d³/4)/d)，尚未付；中段/高逆/耗散仍开。

**R271纯尾：** 原m≥5、q≥16m²单位primitive真逆≥q^(19/10)，完整模型组权/Λ同源全h下界只读真幂底项。原q≥16(m+1)²同源顺次/真二步MP平方比≥3q³/(m+1)^4，h=D(D²)†f首头裸N2放大²=3+C(f)，非λflat/M图/高返回反例。新三位受限D†C*平方费~a²b²(a²−b²)²/[(a²+b²)c²]排分步统一界，只限有限权模型。相邻c1仍开；低占据/双塔/短旗保归档，cq/d末段全q消去、α<0.3420369平均e^(−d³/4+O(dlogd))及共同好q/密度一窗保，早期仍开。

## 3. 危险核、中央闭图与系数行

**R176：** 有界部分谱相交/连通、有限谱共r；实r，奇次全闭、偶次留α^(2k)。复ℓ1误差只付仿射线，跨行须共同部分。
**R147：** 实u、实居中ℓ1 v及正定R，εu^(2k+1)−R(v)全部位移幂循环；复一次保射线条件。一般正号/双无界开。
**R189/R201：** 空谱锚的快G[X,Y]及总类秩≤2范围保；慢Bell不免费。逐项支配仍不付DomX^N⊂DomY，所有固定幂/最高单位分母均有反证。
**R150剪切：** 原F²全λ,w已闭，三次全局幂/一般复二次仍开。T_h本质≤2、Gauss≤3/T3零/共同3jets保原范围；非secant内mean/本质3完整只W±、三匹配T3零，六锚q±及局部J³保归档。新原割线型尖点伴随全排，故外mean/ess3/meanCat3完整临界必rankH4，全部降秩已闭。满H四jets光滑二次/双有理、δE≤1；四不同有基点、4s、3+1、2+2全排，仅余2+1+1及无基点四不同。低Cat/本质≥4和实际逆仍开。
**R150域分类：** 正族固定词/幂/积分母行类span{bν}+J_Σb、J_w=ℓ1+ℓ2(w⁻¹)；单锚γ唯一/多锚mod J，最高单位Bell逆及各自自然域保归档。
**R150半群/混合：** heat×正预解行类span{b}+J_(a+Σb)，纯heat可选锚ℓ4/3。S H_aδ=H_a(δ+2t)、双侧预算/自然域及未知M/旗加权商/闭图可数正权core保；非ℓ1 XaS不全域。
**R268–270：** 共振F_p/快辅助/物理不交乘积保原范围，不扩普通慢Bell/有限头多atom；旧底座归R152/183。
**R236字符：** F_q+v_c−λ的早偏离全闭，否则gcd(q−λ,αq′+δ)=1足，≤p−1候选；二次单位置有真零例，late-c双池类已排。
**R236双池/二分：** 双池、指数种子/有限多行及非ℓ1全尾κ>2按open原条件；种子/比较/主零位不省，点态幂另证。
**R236普通/平滑：** 好集简单纤维、纯主二次及缩放副本各保open完整假设；无副本重根、ℓ1极快/双无界开。
**独立预算：** 固定盘|a/c|≤K、L_N=O(N^1.5)，辅助圆r_N=εN(c_N*)²/Γ_Y=O(N²)，含辅助α≤1指数和长平台；全部主尺度/子支撑假设保归档。
**R236广义核：** 有界Bell包络α>0，固定阶ad强I给全n,m的B(kerT^n,kerT^m)=0与kerT^n⊂closure RanT^m；非零闭广义核无限维真，未付实像/限制稠密/局部等向。
**R236联合见证：** 有界ℓ1迟首二次核⇒同一ζ、正秩一ρ湮灭S=X+H、T、Z=Y−G，G=B0−H²；S全H单射而M内非稠密。整函数F的全右正常配对准确替换(X,Y)→(−H,G)，H/G∈G付4/3增长与混合四次矩；不能只凭这些界排核。联合非零快证书未造，ρ不跨ζ，c=aκ仅j>j0。
**其余界：** 快类/全池预算见open；四位全等向排通用T0因式，原P距离及巨逆carry阻范数搬运。纯等权高ad有界输出k≫√(NlogN)时WOT0，只限该模型。居中late-c λ0、末段伪逆/ΓY/小X圆开，中央域/family293不外推。

## 紧接稿及持续执行

**R12/R14：** 紧夹积/S_p、紧回传成本及自伴链禁阻保。FJKP两硬截断指定子列均非紧；faithful目标投影WOT→θ²I、方差准确。外部紧交织仍开。
1cf：实际bare返回/三Gram及负图联合旗的真实两图余源比较；内mean整类及外mean降秩已闭，续满H外mean的2+1+1、无基点四不同及全局幂。
0c：四块深列/真实k双源及完整外一格松弛反例已付；续天然模型源、原bare/flat、固定第二生成元后继与实际全高度。恢复见[0c队列](notes/2026-11-13-active-unpublished-queue-0c.md)。
完整证明即推，再接open；H更新，逐pull核规，不以阶段/时长收尾。


## 原文：open.md

# 未解决的问题

## 主目标与完成标准

完整解决可分无穷维复 Hilbert 空间上有界算子的普通不变子空间问题：证明每个算子有非零真闭不变子空间，或给出完整反例。**主问题仍未解决，README 的完成标准没有降低。**

实际候选为
$$
H=L^2(\mathbb Z_2,\mu),\qquad (Af)(y)=w(y)f(y-1),
$$
$$
w(0)=0,\quad w(y)=\alpha_{v_2(y)},\quad
\alpha_j=\exp\!\left(-\frac{280}{3}16^j+90\,8^j-300\,2^j+\frac{850}{3}\right).
$$
A非零、非紧、单射、稠密像、拟幂零，C*(I,A)为二进UHF，W*(A)=B(H)，没有非平凡约化子空间。**普通非零真闭不变子空间是否存在仍未知。** 找到这样的空间只排除此候选；证明它不存在才给ISP否定答案。

旧接口见[归档](notes/2026-11-13-open-after-R262-rebase-before-condense-1cf8.md)及results.md。

## 共同适用边界

已证闭域/共同正则器只按原范围使用：全H稠密不传未知限制/有限旗，G不扩一般慢Acal，UHF不运输未知Haar格。正常态/边界奇异态、固定次数/全部向量不同；C未必保M，全等向不代局部等向，不能删域或压缩中央耦合。所有结果仍为中间结论。

并行压缩前的H/open全文、准确范围与全部旧链分别保[1cf全文](notes/2026-11-13-handoff-open-before-negative-flow-joint-flag-2220.md)及[0c全文](notes/2026-11-13-handoff-open-before-single-block-jets-and-complete-tail-metric-0c.md)。本页未列出的旧缺口并未关闭。

## 当前接口一：原 Haar 慢符号的正常湮灭者

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**已排范围与未付部分。** R235/R237/R255已排连续/a.e.+双边UI、保函数非负锥、Walsh对角/有限带/entrywise-ℓ1、合格乘积基块正态及E_√3范围；一般正常正有限秩仍开。R228的C平均可保同泛函而增秩，R229不许一般秩一纯化。真实右矩仍须ε_m||G_m||→0且φρ(T_mG_m)/h_m不消失，普通L²逼近不付此预算。完整原稿链接及端点保本次归档。

**正常源与物理度量。** R230/R244保最小秩双参数和真实保锚源发散/归一弱零，hp/vp不换；真实密度头矩保τ、||v_p||≤10^(p/2)τ，真核δ_p无速率。R236实际MP/联合高幂保同ζ/ρ、原头carry、q1全row像及高q指定目标；MP上界失败不当费用下界。真实双侧正合同不能免费跨次数，全部式与旧入口保[本次全文](notes/2026-11-13-handoff-open-before-interior-node-publication-2220.md)。

**忠实首列及修复。** 完整good列在n,q→∞、M=o16^n一致WOT0，精确单向量支持可提升为完整列；仅近支持不够。G=I、q=n/M=n⁴原坏列O(n^−1/2)、均值1，修复至少(1/(4√2)+o1)e^(n/64)−1且距good趋1。没有精确支持的实际目标、有预算修复及完整联合尾正常锚仍开，全部全树/早吸收费用保归档。

**R236完整尾商/图度量。** 真ann迫norm/uw的m_l=dist(G_l,K)→∞；[逐位cb费用](results/R236-appendix-complete-tail-quotient-metric-and-normal-fixed-target-lifts.md)精确夹max(1,m_l)与√(1+m_l²)，原有限放大图相似费√(1+||πG_l||²)在同表示下近最优。固定非标量T的远尾提升费≥固定正常锚/原两向量尾误差→∞，不以varying U_l代替。

[原翻转分支](results/R236-appendix-dyadic-flip-ideals-and-branch-lifting-cost.md)保J∩γJ=K⊕NK、uw和、精确像v−u∈2gQ及分支逆无界；全部∏η^−1、U/G−L双向h/k源及固定π费用保[本次前全文](notes/2026-11-13-handoff-open-before-single-block-jets-and-complete-tail-metric-0c.md)。特殊两行的便宜next-tail代表仍开，像范数不代商费。

[原carry稳定h迭代](results/R236-appendix-carry-stable-recursive-h-corrections-and-actual-sources.md)以q=η_j²+4η_(j+1)N_(j+2)b⁴的真Neumann逆消奇块逆；S_N/S_Y的全部实际R_j/U_j均付log type≤700/3及明确L_j。商代表距≤e^L_j，同一ρ真空目标锚1而归一锚≥e^(−L_j)/17；反向单位旧费未省，未得统一锚，续真实第二生成元k。

[正 k 枢轴/原双源](results/R236-appendix-positive-k-pivot-and-paid-original-two-row-normalization.md)从真正两条 N 线性行完整消去首两位，保 q0=ε²β²/(4α²)+εδ/(2β)>0、P=HA+KB 和廉价 A^−1。明确迟首正系数族的指定三位链只付 η_n^−2，全部 S/Z 双源、反向费用、同一 rho 真空锚已付；起点变化族的 175/16 不是固定原理想全层 type，单用后续 h 仍回 700/3。一般 gauge 的 Hζ/Q_j、完整第二生成元的后续改善及统一锚仍开。

**余正常接口。** 固定正常矩仅c0/o(m^(k/2))，不付平方和；正Walsh迹尾δ无速率，不能当新ann。远尾擦除保锚须carry×聚合费→0，非UHF强单位不付未知限制。真ann迫q_m↓0，周期r≤q/100、deg≤q³、exp参数≤q⁶指定滤波已排；非周期/超预算/真密度专属和全部q_m仍开。旧平方选择器、张量、热球、纠缠与无速率预算保本次全文，固定非ann例不外推。

[平方根次数联合关系](results/R236-appendix-square-root-degree-joint-head-relations-and-actual-tail-targets.md)保D≈√(2H)、全复系数Vandermonde/真实U,V源/carry；a_j=e^(−β(j+1)^α)、c=a^κ、1<α<7时norm1尾目标距联合理想→0。全关系族真空比≤Ce^(−cn^(1−1/α))、一致WOT0；推广degP≤C2^(dn)、d(α+1)<4含同预算两模式右因子。全部尺度和源费保本次前全文；未付任意实际尾/完整A′算子右因子及完整联合尾正常锚，不据此排核。

[算子值Walsh首列/完整尾交](results/R236-appendix-operator-valued-walsh-column-lifts-and-joint-tail-ideals.md)保M_H(B_n)→A、M_H(C_n)→A′的忠实实际首列和左模；完整tuple源费K_n=10^(n/2)，全最大子式费K_n H!M^(H−1)。S=C+ND、D单位时全尾交由G²−ηNnext,E−GF生成，范数/uw与同一正部分迹均保[本次前全文](notes/2026-11-13-handoff-open-before-three-rectangle-hessian-interface-0c.md)；单位逆及q_n统一正下界仍开。

## 当前接口二：实际边界的除法饱和

固定两个实际边界T_N/T_Y，M=kerT、N=closure BM、D=M⊖N。R187/200已给各有限稳定像及M∩RanB^r⊂N，有限孔核仅真空；真正问题是**无权核内稠密与N=M**，不将环境有限孔稠密当核内核心。

**全整数窗口和真正最小Gram。** [R239全q](results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原进位，低投影e−74d⁴/真实lift e−75d⁴；d≈log^(1/3)q、K*=3(16/770)^(1/3)。c>K*权核入N，真D尾常数K*/2，权阶先属R271。窗口ell=d+m的Σ1/[ell(1+λ²)]发散足N；真D倒能量≤8τ_Q²/||w||⁴。λ²=O(q log^(2/3)q loglogq)足但未得。

[准确Gram](results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)为G=D0P_kerS D0*，严格正；实际r=Avq自动D^d，λ²=〈G⁻¹r,r〉。Schur补不可省；窄带正/倒能量仍容慢尾。逐头单块残量/旧d核阶及Tr(ApKp)非零保原范围。

**旧成本。** 模N结论不代原J_q成本，环境坏见证在M⊥、横向T*M非BM原像；局部Θ(log^(4/3)q)、旧消元/宽窗/短旗/固定比例预算全保本次全文。T_i不保W，统一无权能量未得。

**已否环境捷径。** R239原权Vandermonde x∈kerD²且||D*x||²=S_(m+2p)→0，排h≥2的通用同旗gap；环境D*D+DD*正隙不替P_kerD²D*。原外出生σ经D3桥正交该坏族，但F5=D5DX非零使B2/H2不保外桥核。实际σ=V2Q1^-1V1B0^-1g0更窄，尚未得其低费原像。全尾D3逆还必须付J^5.5级及高次方差下界；廉价环境像不能自动入M。

[高孔/窄源范围](notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)保全部尾位置/完整旗：近核头虽小观测却有巨右费，W短核角度≤2e^(−d⁴/20)只限原方向。顺次MP、分层Pythagoras和全部指数保本次全文，旧σ不代新barf；横向非primitive/全左费仍开。

[实际头理想段移](results/R239-appendix-actual-head-ideal-shifts-and-two-sided-flux-transport.md)保同一原 ξ、原合法窗、完整 D_q⊕I 收缩和两侧逆 Gram 正亏损；同源最小原像差与 W 运输小量各按原式，不能从 N_jM⊂N 推 K_qN⊂N。[完整源 jets](results/R271-appendix-source-primitive-jets-and-sequential-right-chain.md)给 P0D^kr=(−1)^kA^(k+1)p_(q−k)、全部自由旗、S_src≥I 及 S_srcσ=−C_R* cflat；顺次右链只依原源，bare/full 是不同投影。原低部 Schur、带宽、恢复覆盖例及全部精确费用和证明入口保[本次全文](notes/2026-11-13-handoff-open-before-direct-primitive-whole-blocks-0c.md)；实际完整左费仍开。

[增长头观测](results/R239-appendix-growing-head-intertwining-and-full-short-kernel-observation.md)保整个短核：全q窗K≤d/16、半窗q≤e^(d³/8)且K≤d/4；原角度/旗/carry保全文，完整源左费仍开。

[实际二形式求和门槛](results/R271-appendix-actual-source-two-form-ratios-and-legal-window-summation-threshold.md)：真实c=<La,a>/(||a||²+µ²)迫非零W的(1/d)Σ合法q(1+c)^−1→0；实际a、同BA最小a#或已付a_two上C_m=O(e^(d³/4)/d)沿无穷头子序列足N=M，比较仍开。[回文四头](results/R271-appendix-palindromic-four-head-actual-minimal-sources-and-two-form-nonuniformity.md)的11尾/q1混合源左费1、裸费→0而比∞，但规范差liminf²≥3/68；§9完整有限规范类反有µ≤24α，独立ε/β。§10另付全部有限源µ≤49α+25λflat，即J≤3026(J Jbare^−1 J+G)；仍不外推原高孔合法窗。

[低头完整旗](results/R239-appendix-growing-low-head-flags-bare-left-control-and-short-jet-filtering.md)保H≈d^.75与C≤e^(221d³/2048)/(m²−1)，原c(C)χ²运输保[本次全文](notes/2026-11-13-handoff-open-before-paid-jets-joint-graph-normal-h-0c.md)。[单高块](results/R239-appendix-single-dyadic-block-derivative-intertwiner-and-exact-jet-anchor.md)保全q、K≤d/4及准确e0N_Kh；[真jet Schur](results/R239-appendix-sequential-jet-number-and-true-power-schur-comparison.md)最佳N3/N2常数保原稿。[原D3两下降](results/R239-appendix-two-descents-third-tail-and-paid-jet-anchor.md)给C*=1+4||Γ2½D3Γ1½||²≤2²²S_mq⁴；[全K同h裸锚](results/R239-appendix-all-order-same-source-jet-anchor-budget.md)付Θ=K²(4096q²)^K，原εΘ≤e^(−61d⁴/14)，不凭空增加ε。

[直接 primitive 整块修正](results/R239-appendix-direct-primitive-correction-and-whole-dyadic-source-flags.md)用一次双卷积付全部原右旗；p=d/4,d/2 两整块分别有 δ≤e^(−3d⁴/50)、e^(−5d⁴)，其三角强制源及完整首头的真 M 图付 µ²≤χ²/(2−δtot²)。[原深 jets 联合/物理运输](results/R239-appendix-joint-deep-strip-flag-and-same-flat-middle-transfer.md)仍保同一 cflat；余条件是 P_X Γ^{−*}M rhat=0，不能改为坐标零。物理中段未直接付强制角缩为 3d/8≤t<d/2、j>d/2+t；全部自由头及 Schur 回馈仍开，旧单块/联合旗完整范围保[本次全文](notes/2026-11-13-handoff-open-before-direct-primitive-whole-blocks-0c.md)。

[四块完整比较](results/R239-appendix-four-block-head-comparison-and-quarter-depth-source-elimination.md)将全部原 primitive 延拓差付到 ε=e^(−d⁴/20)，深度 t≥d/4+1 的所有头原右旗均付费，含最后两列、无低锚；同原 flat/裸费左 Schur 保留。物理中段全部进入 F_new，其余量准确是 T_out K_mid x，K_mid=−P_mid(I+C_F*C_F)^−1C_F*C_T；不能把最优补全置零。同仿射约束的模型最小者已付 O(ε) 物理运输，天然模型源及平坦费用继续。

[原左输出切分](results/R271-appendix-output-cut-schur-localization-and-larger-middle-band.md)保全部自由头/完整G_-≥I，付末3d/8（渐近任意<0.450155）primitive带，余实际中段放大未付。[同源截断/Riccati](results/R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)给P≤p v=E_p†r_p和完整能量递推，p+d≤q的flat/裸恰同一未来带投影，Σχp²≤2d能量差；不推出统一耗散。

[准确负源图](results/R271-appendix-exact-left-source-flow-range-and-minimal-upward-extension.md)给RanT=Np=ker i0*(L+B)，与M图不同；全部上源s=−AD†r+Ag、g非首头primitive，增费||D†r||²+||g||²，首头flat=−bare。全部后代Σ[||D†r_p||²+||A0^-1τ_(p+1)||²]=µ_q²−µ_s²保原头权/交叉。

[负源图与联合旗的同时归约](results/R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)：对任何已付λ(Qr)≤δµ(r)且含首头的闭源旗X，真正源流负图与X之交满足µ²+<Kr0,r0>≤δµλflat,Q，故µ≤δχ。沿交作真M投影同时保负图/两费用，左改变量≤δχ；余条件准确i0*(L+B)rhat=0、R_N*Mrhat=0，不是坐标零。对同一Q=floor e^(d³/4)的实际顶部最小者，全部p∈[4d,Q−d]先截断进入负图，再各自投影，余前驱一致趋同w且Σχhat²≤2d(τ+η||w||)²；不宣称投影后仍同一源流。只须在这个实际两图余族付µ²/χ²=O(e^(d³/4)/d)即可N=M，尚未付。

[最低核深度Euler源](results/R271-appendix-bare-minimizer-lowest-depth-primitive-source-and-euler-compression.md)/[真幂底项与两过滤桥](results/R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)给α²=Σ||(D^(j+1))†A^jr||²+||G†ζ||²，kerG=RanQ*、G†G=Π，返回−RG†ζ。ζ/R保相邻两道受限D3*、全孔Gram先逆后压缩和真实头旗，不并成D3²；未付S_H†RG†ζ。 [三位受限伴随失败路线](notes/2026-11-13-adjoint-third-tail-bridge-inverse-finite-obstruction-kernel-2220.md)精确给D†(C^K)*平方费~a²b²(a²−b²)²/[(a²+b²)c²]，即使平方权和固定也无统一分步界；仅有限正权模型，不认作原连续尾/实际ζ反例。

相邻序仍缺任意有限正权全出生/全高度及原高孔窄源的比较。[全矩障碍](notes/2026-11-13-1cf-established-scope-and-domain-limits.md)与[分子障碍](notes/2026-11-13-penultimate-beta-denominator-separated-roots-and-schur-obstacle-1cf.md)已排全Hankel/独立P·H正矩入口；[有限—原尾归约](results/R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md)仍须全部有限权型。

**已付尾Gram范围。** 四任意正头+池全K_s相邻Γ≤16/首降≤64，M≤3严格9/4；q−1内部Γ≤4/首降≤9，低边释放仍欠完整ZS^-1Z*与实际源控制。任意正权出生一首末边c1，原m≥46首降<2且最佳趋2；内部(h+1)δ<1付h/(h−1)乘exp[±13(h−1)δ/(1−(h+1)δ)]，原h=o(m)统一最优。全出生低占据在(2s+h−1)δ<1付真幂MP乘积夹界；原H_*(S_*+H_*)/m→0矩形最优。全部精确公式/证明入口保[本次全文](notes/2026-11-13-handoff-open-before-interior-node-publication-2220.md)，跨出生角度/原高孔窄源未付。

[原primitive真逆19/10](results/R271-appendix-full-model-source-comparison-and-original-primitive-nineteen-tenths-lower-bound.md)保m≥5、q≥16m²，完整原/模型组费与Λ付同源全h下界，单步≥q^(19/10)；只读真幂底项。[原尾顺次/真幂差距](results/R271-appendix-original-tail-cubic-sequential-power-gap-and-bare-two-jet-amplification.md)保q≥16(m+1)²、同一f的MP平方比≥3q³/(m+1)^4及h=D(D²)†f首头裸N2放大²=3+C(f)。未证这些源来自M图，不外推λflat/相邻c1/高返回；全部常数、模型组权与旧链保[本次全文](notes/2026-11-13-handoff-open-before-negative-flow-joint-flag-2220.md)。

[完整双塔](results/R271-appendix-bosonic-dual-fock-tower-and-quadratic-collision-conditioning.md)/[短规范旗](results/R271-appendix-short-canonical-fock-flags-and-q-over-d-prefix-window.md)保V=(W*)^-1、P²δ及ε=4δHP<1/2，I≤V*V≤(1−ε)/(1−2ε)。原s=⌊cq/d⌋、c<1/12全费用付末s段，早期/T_i不保W仍开。[原creation角度例](notes/2026-11-13-original-tail-creation-angle-nonperturbative-scope-kernel-continue.md)不否定H1的V=I；[两层规范旗反例](results/R271-appendix-critical-two-cluster-canonical-short-flag-obstruction.md)在δHP→1、放大量²~√p排一般权温和界，非原尾/相邻c1反例。

[固定比例实际平方平均](results/R271-appendix-fixed-fraction-repair-mean-square-decay-and-common-subsequences.md)：α<0.3420369原q窗保重叠平方和≤(d−1)||w||²及a_m=exp[−d³/4+Oα(dlogd)]。固定有限维族/正迹类有共同好q，阈值Q^−η、η<1/2好窗密度1；末αq能量及修复差→0。未付全部q/无限维单位球/早期段。

[R239首段边界先消元](results/R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md)保持原同源/完整D3；旧P=I+L的返回与P/Q比较仍开。[新中间Schur的真实差分识别](results/R271-appendix-boundary-first-middle-schur-is-the-primitive-difference-gram.md)证明零首源低出生块R0有界双射，故仅新Q1°=O GG*O*，首两项E0°=Σ_{t=2}^{d−1}||(D^t)†A^(t−1)r||²、E1°=||G†ζ||²。新末块H2°=S_HS_H*+R(I−Π)R*，同一返回σ°=−RG†ζ；ζ°=−Oζ的符号及全部自由primitive保留。不能替换旧Q1/旧强制通量费用，实际高逆仍待估计；旧完整公式保本次全文归档。


**有限权比较。** 全部旧常数/整数证书/硬端和源Gram保[本次完整归档](notes/2026-11-13-handoff-open-before-interior-node-publication-2220.md)。全Hankel、出生阶乘正矩及独立单二次残差的一般充分性已排，不否定真正完整相邻序。

- 两/三独立头+池全K_s全h、两大等权组全h、三同权头+一位+池全h已有严格c1；四独立头全出生16、整个h2严格1。二大组+一位h2/3/4严格c1，其h≥5及任意多组仍开；全部强制根、短池、饱和线和最高逆保原稿。
- Stieltjes完整源/交叉及H^-1算子凹、两核旗曲率差不自动支付固定出生相邻。三矩形Hessian保下矩形正修正/非零秩一交叉，不能删项归纳。
- [Pearson双向](results/R239-appendix-actual-binomial-pearson-bidiagonal-and-full-shear-elimination.md)保全部强制根、shear；[合并两组](results/R239-appendix-collapsed-weight-groups-and-third-gram-coupling.md)保C(w)=xy(w−1)(w−z)/[(z−1)w]及真实β。
- [曲率cap](results/R239-appendix-rectangular-turan-endpoints-and-sharp-curvature-caps.md)及[全局均值](results/R239-appendix-rectangular-global-mean-compatibility-constraints.md)保同一D/t端点/积分/四点区间交，续所有w正性；松弛样本不作实际反例或统一证明。
- [固定合并方向/Casimir](results/R239-appendix-fixed-merger-directions-and-actual-casimir-identities.md)以实际群平均和硬端给 Q(1)=μ(J−μ)、Q(z)=(D+μ)(t−μ)；[两参数递推/外一层](results/R239-appendix-casimir-phase-recurrence-and-outer-height-obstruction.md)保全部正分母及真倒易。精确非实际例满足三点 Casimir、四 cap、全部均值，却 P(1/8000)<−20000；被真实 E_->0 排除。首中系数归为正分母上的二次式，符号及完整全高度仍开。
- [第一步完整外延拓仍不足](results/R239-appendix-first-full-outer-phase-extension-is-not-sufficient.md)给五合并层、全部相容窗口、57均值及两外正约束同时成立而 P(1/40000)<−3000000 的精确非实际例；首失真在第二外步的真实上/下标量序列。不能再用一格外条件作充分分解，续原 Schur/MP 全高度结构。
- 任意头饱和线、全权倒数对偶、短池完整MP及τ的全部公式/原稿入口保[本次前全文](notes/2026-11-13-handoff-open-before-three-short-birth-two-all-height-0c.md)；不扩非饱和块，L=0含一般模型，h2一次源仍欠完整Σ逆/平衡约束/秩亏τ下界。

[R239两异权四矩返回](results/R239-appendix-two-exceptional-tail-four-moment-return-geometry.md)保同源逐孔自由末矩及准确 I≤C(Fbare+Ffull^−1) 字典；固定 A/大双尾、变 Aε/固定小尾、回文头/小尾三族的完整范围与原式保[本次全文](notes/2026-11-13-handoff-open-before-casimir-recovery-index-0c.md)及原稿。后两族不是原指定长跳头，不能反驳原高孔窄源比较。



[真实尾理想](notes/2026-11-13-actual-tail-ideal-defect-compression-and-preimage-distance-boundary.md)保X_m(c)M⊂N及||P_M D_m(c)*P_W||≤Σ|c_j|η_j；三次尾≤s3e^(−770d⁴)。实际配对还付s3 dist(原像,M)，最小范数不自动减此距离。

[双宽实际源投影](results/R239-appendix-double-width-head-flux-projection-and-exact-energy-drop.md)给P_Zh=c_d−c_2d及准确商费||h⊥||²=||h||²−λ_d²+λ_2d²，Z为同m/q零源新头旗。原lift去核只付e−75d⁴||w||√能量差；负〈h,c_2d〉不许把w换成最小链，无统一下降率/h⊥上界/超预算迭代。

**完整L核/窄通量。** 同旗合法K(h_t)支持[q+2,q+2d−2]、费≤e20d⁴且由原lift入N；真D3逆只降范数。双宽投影/e0h特例的精确范围保本次归档。

[原裸低链首段参数化](results/R271-appendix-bare-low-chain-parametrization-by-true-power-inverses.md)保整个Z与首段联合旗有界双射：后段(-1)^(t−1)(D^(t−1))†A^(t−1)x，M=T*T≥I、Jbare=D_XM^-1D_X*。真幂MP不能换顺次MP；全部自由度与高返回已由上方G/ζ/R准确消元，逆Gram费用仍开。

[首位图/横向压缩](results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)保C²=η₀N₁|L、||C||<1/√12及真缺陷两约束；[正压缩](results/R239-appendix-coercive-adjoint-and-positive-mixed-compression.md)付T*≥7/8、Re(P_MBT*|M)≥5α₀/6。它给M⊥横向同构而非BM原像，全部字典/未闭缺口保本次全文。


**[深源jets再次Schur消元](results/R271-appendix-deep-source-jet-schur-elimination-with-original-flat-cost.md)：** m≥8、k≥5d/8的整段跨界算子≤ε=e^(−d⁴/20)，无q重数；保持浅坐标的真实深补全后，µ²=〈Ŝx,x〉+Edeep且Edeep≤ε²λflat²，Ŝx=−Ĉ*cflat仍用同一源。裸项差≤ε²λflat，合法残源µ≤ελflat、λ/α≤ε²λflat；不可免费运输新源flat。阈值可取任意θ>(128/770)^(1/3)，剩余浅层须保完整Schur回馈。

## 当前接口三：一般系数行、多个模式与中央域

完整已付行类、种子/比较/最高字符条件、全部旧公式及原稿链接保[本次前全文](notes/2026-11-13-handoff-open-before-faithful-vacuum-support-0c.md)。这里列下一实际缺口，未列的旧接口保持原状态。

1. **普通慢行与未知限制。** 实u奇次全部位移/幂闭，偶次余α^(2k)；有限谱部分须共同存在才能跨行。实负正定辅助已闭，正号碰撞/双无界未闭。1<α≤3普通全部重数、居中迟首κ>2的λ0及无副本重根仍开。主/辅助尺度、种子、零位置、ΓY预算不得互换；全H单射稠密不传未知M。
2. **原双行见证。** 真迟首核给同一ζ和正秩一ρ同时湮灭SA′、TA′、ZA′，S=X+Hζ、Z=Y−B0+Hζ²。整函数全右替换(X,Y)→(−Hζ,B0−Hζ²)和快混合矩已付；这些必要增长界有固定非湮灭正态反例，仍欠实际联合非零快证书/来源特殊正常锚。不能跨ζ混用ρ。
3. **导子及实际源。** 固定阶ad强单位给全部广义核全等向及kerT^n⊂closureRanT^m；不付实际值域或限制稠密。全域高导子有强单位但不是单个导子像，短Leibniz末段/实际伪逆费用仍开。纯等权高ad WOT0只限其原模型。
4. **有限复模式。** ≤5正实log复二次全Q已闭；指定六模式F²的全部λ,w已由真实Bell逆/有理jet证书闭合。[指定六模式F³第三矩](results/R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)付16维完整Schur和17低变量加权六次R3，仍须证明有实际逆的B_r自然幂∈gradR3；普通first Bell分母次数障碍不等于非循环。一般Σ内、无池、无限模式及更高幂仍开。
5. **相对乘积与自然域。** 相对ℓ1双乘积、单慢加快、快分式和空谱锚两方向按旧条件保留；复杂相对ℓ2、三以上cocycle、双全C与非解析闭包未闭。正自然词、热/预解和共同正则子须保原域；可数全H稠密像之交不保证与未知M非零相交。

[两平面完整矩判据](results/R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)给W±支撑时F^h临界⇔Q±|T_h，原三first Bell零。[六个非零T3临界点](results/R150-appendix-six-mode-cubic-nonzero-moment-critical-points-and-anchor-necessity.md)保全33梯度、三L独立，证明任何全局S_r正幂归属必须q+=q−=0；原三r保留，必要不充分。[Gaussian全部rankH≤3分类](results/R150-appendix-all-rank-three-hankel-gaussian-critical-points.md)付临界⇔HKH=0，rank1任意点、rank2正交对或四点一阶jet、rank3仅W±；不扩rank≥4。

[有限原子族](results/R150-appendix-finite-atomic-ordinary-moment-critical-families.md)给k<h完整临界/Bell零。[两原子一般点](results/R150-appendix-six-mode-cubic-two-atom-regular-critical-point.md)的4维图稠密开集I=J，是一般约化临界分支。[碰撞锐度](results/R150-appendix-six-mode-cubic-collision-sharp-local-exponent.md)付原三r在p0最小局部幂3；[Gaussian锐度](results/R150-appendix-six-mode-cubic-gaussian-plane-exact-local-exponent-four.md)付p+最小局部幂4。所有法向Hessian、全梯度Artin障碍、普通局部环证明保完整稿/本轮归档；判别子集/全局幂/实际逆仍开。

[最高矩本质支撑](results/R150-appendix-highest-moment-essential-support-and-cubic-projection-types.md)：T_h(Kv)=0迫本质≤2时T_h全零；非零T3维3仅投影(δ,e,d)=(3,2,1),(1,2,2),(2,3,1)，低阶梯度仍须支付。[非零y且T3零分类](results/R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md)完整列尽不同两点原子族，以及y=a v(s)、H=c vvᵀ+d(vv′ᵀ+v′vᵀ)、V唯一的单点族；后者完整临界恰d=0或s=0,2,−6,∞，未假H低秩。

[外mean四jet与二次关系](results/R150-appendix-essential-cubic-conormal-and-four-jet-support-reduction.md)：mean Cat3/essT3三维/y在外时，前三矩共同支撑唯一长度四g，原λ给H=2Vλ、y=8Vλλ、λy1；同一一次梯度给Q_F²=0，满H时N≠0。其物理二次关系准确等价[原12×10矩阵](results/R150-appendix-quartic-support-quadric-pencil-and-codimension-two.md)降秩，降秩簇dim≤2；仍须全部低梯度，不能将矩阵必要性作充分性。

[满H光滑中心](results/R150-appendix-four-jet-smooth-quadric-center-and-birational-projection.md)保K:T3=−4Mp及Q2，迫Mp≠0，二次逆给W投影双有理。对任意g含重jets/∞，[单基点定理](results/R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md)给δE≤1且全基点支撑恰Δ_s q_s或Δ_s²q_s/Δ_t；满H中心除子与g互素，全部原式/Bezout和旧范围保本次全文。

[外mean降秩的尖点归约](results/R150-appendix-rank-three-outer-mean-cuspidal-support-and-smooth-center.md)先给rankH3/缺失简单点、活跃长3/光滑二次中心、三极线Ga³/Gb³/Ga²b及全部半权必要条件。[原割线型尖点伴随与降秩整类排除](results/R150-appendix-no-secant-cuspidal-companion-and-outer-mean-rank-drop-exclusion.md)进一步用重复因子L的真实Cat秩≤2：自尖点的两31次结果式mod103=16，特殊/∞逐图付；非自尖点只剩原E8判别分支，两完整Cat子式结果式mod103=29/89，所有分母/重根/∞图排尽。故非secant/essT3三维/外mean完整临界必rankH4，全部降秩余类已闭；当前只续满H的2+1+1和无基点四不同，不扩低Cat/高本质/全局幂。

[四不同点有基点整类排除](results/R150-appendix-reduced-four-point-basepoint-critical-section-is-empty.md)：保非secant/外mean/本质3/满H，前稿六候选与额外权1/2上的两真实梯度，化为conic两锚有理式。两个极点中点是中心且中心/无穷远取值相反，迫χ=2γ+β(a+b)+2αab=0；原两族整数结果式均非零，全部六个复候选遂排。准确余类为无基点五次经与支撑互素的长度2中心除子投向不可约节点三次，半权分割唯一（模补集）。重jets、H降秩/mean割线及更高本质维数仍开。

[四重jet整类排除](results/R150-appendix-quadruple-jet-supports-have-no-full-rank-outer-mean-critical-point.md)：原12×10矩阵的两真实子式与完整Bézout证明降秩仅0/∞，两处秩9；满H迫顶mean jet非零，原极线阶(4,3,2,1)使T3首项不能抵消。保非secant/外mean/essT3三维/满H，4s整类排除。

[非约化支撑的中心三次与半权条件](results/R150-appendix-nonreduced-four-jet-central-cubics-and-half-weight-conditions.md)：原λ在各局部环为单位，归一得到复Frobenius泛函τ及T3=.5τ[(X−τX)^3]，无正性假设。3+1先迫单点权a=.5，现已接下稿全部排除；2+2的节点/半权可约分支现已下稿全排；2+1+1须b=.5或c=.5或b+c=.5，恰一条件为节点三次，b=c=.5唯一可约。不可约三次全为普通节点，无尖点；conic型原四维投影必有一个基点、后续中心除子长2且与g互素。仍仅原满H外mean临界的必要条件，余2+1+1的完整低梯度未付。

[满H外mean 3+1排除](results/R150-appendix-three-plus-one-full-rank-outer-mean-critical-exclusion.md)由半权原归一的八条完整y/H/最高jet必要式迫三jet全等向；原K在0/2/−6/∞均排，含所有无穷支点。与降秩归约合并，非secant/ess3外mean整个3+1已排；满H余2+1+1及无基点四不同。

[满H外mean 2+2完整排除](results/R150-appendix-two-plus-two-full-rank-outer-mean-critical-exclusion.md)：原局部Frobenius归一保总权μ=0/1例外，c=0给两个基点而排，μ=.5二次像又需基点而排，μ0/1由完整低梯度矛盾。普通μ的三条原jet恒等式给Δ=de−f；Δ≠0迫两参数互为T(x)=(x³−6x−4)/(x(x+1))，原三次兼容的7/8次Q/J由保次数mod103 Bézout1排尽。Δ0的原切向与交叉行列式只留0/∞，极线二阶项不能由第一块≥3阶项抵消。全部有限/∞及复权退化已覆盖；此满H截面非约化只余2+1+1。

[正平面二维分支](results/R150-appendix-six-mode-cubic-positive-plane-critical-component.md)给真实不可约临界分支及普通局部J³⊂I⊂J、rad I=J；q+(r)=0在明示非空开集付Br³局部归属。未给准确指数或局部单位实际逆，其他分支/全局幂仍开，全部矩参数及系数证书保全文。

[共同长度3jets](results/R150-appendix-length-three-common-jets-and-inside-mean-critical-dichotomy.md)含三不同点和全部重jets：非secant完整临界只W±、原三r零，H/V退化保。内mean本质3余类的H/V准确同U2；mean割线/更高本质及全局幂仍开。

[非割线内mean本质三维完整分类](results/R150-appendix-inside-mean-complete-critical-support-classification.md)：mean Cat秩3、essT3=W3且y∈W的全部原临界点准确只W±，原三个匹配Bell方向的T3值全零。已付全等向/双jet/简单极线/内点奇点后，轴奇点原式迫C22=J²、C13=0；原两结果式的28/22次余因子保次数mod103互素，s=5/−1与无穷图均处理，整个两点余类为空。含H/V全部允许降秩，不留一般位置例外。完整矩判据仍为Q±|T3；外mean、mean Cat≤2、本质≥4和全局Jacobian自然幂/实际逆继续。

## 其他仍开放的路线与不可互换的极限

一般L²循环性、非标准主理想分类、完整A′核、外部紧交织继续。R12紧夹积/自伴链障碍及R14指定硬谱截断非紧与faithful弱极限已付；它们不排所有外部方法。family293仅超不变/有限因子投影范围，不是普通ISP答案。

同一物理源、原核旗、自然域和正常预算按已付范围使用；环境/有限模型不替实际来源，全部旧限制保本次全文。继续上述未闭接口，完成标准不变。


## 原文：notes/2026-11-13-active-unpublished-queue-0c.md

# 0c 未发布证明与当前工作队列

日期：2026-11-13 22:49:34 UTC。终端恢复并完成真实 pull：0590ee9d64e72c7c58dd787af2f30966b8e17851（22:43:02 UTC），两 README blob 未变。旧临时工作树丢失，当前树 `/tmp/isp-0c017065-math-research-20261113-2241`。此前 H/open/队列全文保[本次归档](2026-11-13-handoff-open-before-casimir-recovery-index-0c.md)。只以成功推送的仓库内容为恢复基准；API 写入不是 pull。

## 已核并已推的完整证明

[D3 两下降](../results/R239-appendix-two-descents-third-tail-and-paid-jet-anchor.md)、[全部 K 同源锚](../results/R239-appendix-all-order-same-source-jet-anchor-budget.md)、[单高块源旗](../results/R239-appendix-paid-single-high-block-source-graph-strip.md)、[深 jets 联合真 M 图](../results/R239-appendix-joint-deep-strip-flag-and-same-flat-middle-transfer.md)、[carry 稳定 h 原源](../results/R236-appendix-carry-stable-recursive-h-corrections-and-actual-sources.md)已推；不是待恢复稿。

终端失联期间按根 §8 分别成功推送：[实际固定合并方向及 Casimir](../results/R239-appendix-fixed-merger-directions-and-actual-casimir-identities.md)（e35bd9711cf8a5176bae1bfab6213f1047d96df6）、[两参数相位、全均值松弛反例及外一层条件](../results/R239-appendix-casimir-phase-recurrence-and-outer-height-obstruction.md)（c02c18d9150373fc1f0093392c6b593b57ade654）、[完整有理证书](2026-11-13-casimir-globalmean-relax-certificate-0c.py)（20fd597ee250a7322ae724486f62e7a680ccea84）。root 已全文读并逐式核；恢复后脚本再运行通过。正文 §4 巨大分母抄写少九个末零，本轮以脚本精确值修正，不影响证明、不改变非实际反例的范围。

## 直接 primitive 修正与多高位

[整块恢复全文](2026-11-13-direct-primitive-high-block-correction-1856-recovery.md)由 cc9f8591fcc2f0bd36dc28d42a5f3a457e219182 保存；root 已全读直接 primitive 双卷积、原四次幂预算、完整右旗和两整块三角源旗。已按独立结论发表：[直接 primitive 整块源旗](../results/R239-appendix-direct-primitive-correction-and-whole-dyadic-source-flags.md)。它没有把 M 正交余图当作坐标支撑，也没有删自由头。

四块全头稿已独立发表：[统一延拓/四分之一深度/自由反馈](../results/R239-appendix-four-block-head-comparison-and-quarter-depth-source-elimination.md)；它直接包括最后两列，无需等待双导数内部列。root 已全读并给 §9 的 O(ε) 正规方程运输。继续中的新稿扩大到模型天然自由旗 F_box，并以首右段 primitive 参数化运输 bare；尚须完整保原 flat 对偶。

## 实际双行正 k 枢轴

[完整恢复全文](2026-11-13-actual-two-row-k-correction-1856-recovery.md)由 643d708e57f8d1015ef0481954148a45677c690f 保存。root 已全文核正分母、显式 S/Z 双源、实际两次尾交、正向及反向预算和同一 rho 锚。结果限真实 N 线性行；指定三位链只付较早 eta_n^−2，未来仅沿 h 迭代时主 type 仍回 700/3。已独立发表：[正 k 枢轴与原双源正规化](../results/R236-appendix-positive-k-pivot-and-paid-original-two-row-normalization.md)。

normal_full_columns_1856 继续保第二生成元 (R²−t, C_K−R D_K) 的真实递推和一般 gauge/carry 系数，不将下一两行重命名为纯线性行，不把起点变化族当固定原理想。

## 二组加一位的全部高度

两真实固定方向为 w=z 的 (1,D)/(1,−t) 和 w=1 的 (1,0)/(1,−J)。固定源全逆给 Q(1)=mu(J−mu)、Q(z)=(D+mu)(t−mu)，同一实际族按 (R,mu) 两参数逐层有理递推。三点 Casimir、四 cap、全部一阶均值仍不足，精确证书 P(1/8000)<−20000；该非实际点被外一层 E_->0 排除。

新的[第一步完整外延拓反例](../results/R239-appendix-first-full-outer-phase-extension-is-not-sufficient.md)和独立 Fraction 证书已发表：全部第一步局部正性、五合并层、57 均值、两外条件仍容完整 P(1/40000)<−3000000；第二步真实标量条件失败。root 全文核且精确重跑。继续真实全高度 Schur/MP 结构，不再把有限外一格当充分条件；一般 h≥5 仍开。

普通 ISP 未完成。完整结果即推，继续 open 的实际下一缺口；所有后续实际 pull 立即核两 README 并在 HANDOFF 记 SHA。
