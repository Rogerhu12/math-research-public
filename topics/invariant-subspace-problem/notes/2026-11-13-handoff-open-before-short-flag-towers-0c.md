# 联合核短塔前的交接与开放问题

2026-11-13 06:45:27 UTC；固定main 3cf13a347f867887ba289cadd130423460dbe919。保完整原文，链接按notes位置调整。

## 原 HANDOFF.md

# 交接

## 目标、负责人和规则检查点

- **目标未完成：** 必须完整解决可分无穷维复Hilbert普通ISP。Haar普通不变格、边界N=M及一般正常湮灭者仍未知；规范单模式全部多项式加权输入现已循环。不降低README完成标准，不以阶段或时长收尾。
- **负责人及分工：** Astra-ISP-1cf8c51d负责，0c继续贡献。1cf用R213–229、R240–271；0c用R230–239。新编号先登记，独占git/index，不动他人未发布文件。
- **最后实际pull/规则：** 2026-11-13 01:06:52 UTC，cdb9429c93f969d1054d8e1e49643add83457c24；真实git pull --rebase origin main，两README差异空。每小时至少一次，终端恢复即补。
- **0c 最近实际 pull：** 01:06:17 UTC / bfe9f2c0b2977d4bab3d14793c3f247374e81303，两README差异空；后续含05:20:35、06:03:04的真实pull调用均执行前No usable execution environment，API非pull，恢复即补。
- **已读规则blob：** 根 f787a306d90892d8dec765dc59747d60ba39f055；题 6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd。每次实际pull均比较两README，有变只读差异立即照做并记SHA；至少每小时pull。
- **API后备检查点：** 2026-11-13 06:45:47 UTC / main c54a2789669622ada270cf76343ee0c21e56e15b，两README blob未变；1cf 06:31:47实际pull执行前无环境。API非pull，恢复即补。
- **发布：** 完整结论单独推；终端可用用git，拒推即pull --rebase。仅失联用根§8小文本；API不算pull。令牌仅命令行，不写文件/config/提交；不force、不写根LOG；Markdown<100KB、H<10KB，合并最新main。

## 恢复记录与模型

工作树：1cf /tmp/isp-1cf8c51d-math-research；0c /tmp/isp-0c017065-math-research-20261113-0030。本次压缩前全部H/open及归档链见[完整原文](../notes/2026-11-13-handoff-open-before-cross-denominator-positive-quotient-1cf.md)。

模型：H=L²(Z₂)，A为真实Haar加权odometer；Nj=A^(2^j)/dj=Ej+ηjEj*N_(j+1)、ηj≤e^(−770·16^j)，Y=N/(1+N)、V=I−2Y。A′交换/C对称，R88有界SOT多项式逼近。UHF不运输未知限制；C保核、局部等向和输入域不可免费。

## 1. 原 Haar 正常湮灭者

**R228实结构：** J0平均保湮灭但一般改φ，C平均保同φ；实密度反射两块可合为max(p,q)。最小实支撑与至少一奇偶空间零交。复Ri的商须带权Θ_Q；真Ri实才有无权Krein度量，正负指数均∞，不付共同域。
S_N/Y全H单射稠密已证，普遍强主理想仍开。失败有正有限秩正常见证；R228允许C实化，R229反例排一般秩一纯化，R242窄矩阵/垂直商图已付但不免费图稠密。
**既有正态范围：** R255排E_√3有限正见证且端点最优；R235保函数非负锥及R237 Walsh对角/有限带/entrywise-ℓ¹/指定乘积基有效，一般正常态不覆盖。

**R235：** 连续/a.e.+双边UI已排，普通L∞不够；全右矩|φ(T_mG)|≤h_mλε_m||G||保留，待预算内非零右配对。
**R237：** 固定Q∈Acal的QAcal同范数强*逼近QA′；非UHF左因子/无界右因子不覆盖。
R248阻尼不交换、R250未得A+不变，详式保归档。
**R253/R237/R230：** 真湮灭迫q_m↓0。逐位Jensen给纯正锥真空比≤e^{(m+1)/2−πk/16}；多重Fourier及双换元除法覆盖周期r≤q/100、总deg≤q³的任意复p(Uν)，实际比≤2e^{m/2+1/4−q/10}，独立exp参数≤q⁶同界。全部系数/相消/相对carry已付；旧单标量更广次数预算、完整Gram与共同次数N_B相位锥保留。非周期/更多模式/超预算及真密度专属仍开，不代完整q_m。
**R244：** 广义Ri付准确最大商/参数无关共同图，真空原像⇔无重复词域。任意秩保Pi理想湮灭；最小秩经删除/插入得各Ri在循环S零商Q0为0，Di在那里单位。全秩b_i=DiPi的正Koszul循环零商与Q0有带下界同构、G0q0=z0；不传全交域商。rank2有交替商/两层∞缺口及两分母-分子直和，所有中间比例图全C谱；原H秩一/共同域/强理想仍开。
**R267：** P∈F_A=∩A^rA′非零且PW_n收缩强*趋I；F_A同范数强*稠密、AF_A=F_A、与UHF零交。共同幂原像是闭词图核心，非PH自动入域。1∉RanP；指定配对仍需Walsh矩平方可和。
**R230既有障碍：** 固定非湮灭f排可逆块及有限完整逆源；完整矩保ρT_m交叉约化，统一定位常数发散。规范正积e^{o√q}/子半次数域非像保；真态专属/全空间右因子仍开。

**R253/263：** 全A^r不能有界除S；同一H_(1/(60e²))向量不在两RanS，规范/全域分母已排，专属仍开。

## 2. 两个实际边界的 N=M

T=T_N,T_Y，M=kerT，N=closure BM，D=M⊖N。R187/200给M∩RanB^r⊂N，有限孔核仅真空；R234模N已闭，R238原J_q成本不能当模N成本。环境坏见证在M⊥，横向T*M同构不是BM原像；旧通量/头Jordan/平方γ各保原范围，详归档。
**R239全q：** d≈log^(1/3)q、K*=3(16/770)^(1/3)给c>K*权核入N及真D尾常数K*/2；R271先得4/3权阶。Σ1/[ell(1+λ²)]发散足N，真实λ²=〈G⁻¹r,r〉必须保Schur补，无权增长未得。
**R239分解/低孔：** 受控原始源小修复、高秩及保自由坐标双宽移动窗已闭。首个三维T_i/T∞为完整I分解，分析/合成1+O(m^−1/2)，受限μ平方和与λ_h²双向等价。新canonical Fock塔准确交织D，全部层Gram误差Δ≤(3/(J+1))[32(P+1)]^P；s=floor(c logq/loglogq)、c<1、P=s+d−1、J≈2q时Δ→0。P_(q−s)整个非真空低孔源在原宽d内小修复，完整末段μ∞²+Σ_(i>q−s)μ_i²→0。早期三维支/真头通量仍开，T_i不保缺陷正交；全低输出坏能量与完整前缀指数障碍保留。
**R239/R271闭链：** 有限尾塔付固定窗闭像/Gram。新固定头相似κ给λ_d≤κλ∞、λ_[d+n(d−1)]²≤[1+(κ²−1)a_n²]λ∞²，a_n=2ρ^n/(1+ρ^(2n))、ρ=(κ−1)/(κ+1)，对所有q/源统一；极小链差平方恰为能量差。总级数带宽/Chebyshev真逆已付，κ_m及实际加宽lift仍须付；非A^d截断实际伪逆。

**R271：** 准确残量/联合链旗和完整Schur补已付；右逆C≤e^d⁴、最优双变量≤Cλ/C²λ。真缺陷迫低核头通量≈||v||²+λ²，H_t含1/4，不是小carry。ΠNexp=ΠN=ΠM=V但无有界原像子列；平方Smith只排D稠密交织。

## 3. 危险核、中央闭图与系数行

**R176：** 有界部分谱相交/连通，有限谱共用r_u；坏点态幂须q(r_u)=q(r_u−2α)。J迫实u的r_u实，全部奇次位移/幂循环，偶次只留α^(2k)；q在R单射或无实根有对应结论。复ℓ1误差只给仿射线，共同有界部分存在才许跨行加性；实碰撞仍开。
**R147：** 实u首系数符号ε、任意实ℓ1居中v及正定R(0)=0，全部[εu^(2k+1)−R(v)−λ]^m e^w循环；任意支持次序。复一次辅助c/α避负实射线也全λ；不扩正号u³+v²或无界辅助。
**R189双方向：** 一个空谱相位锚X加任意first/有界Y，快增量扰动下非零G[X,Y]最大实现单射稠密；总类秩≤2含实际空谱组合亦得。双共振全q保，普通慢修正/新子商仍不免费。
**R150 Newton：** 空谱X_u、j_u≤j_v且deg g=p>m=deg f≥1，全部[f(v)−g(u)−λ]e^w循环；v可独立全C慢行。真Bell差除A^h，结果式最高单位次数m(p−1)，X逆使消元子有界化。含普通v²−u³，无快修正；当前只r=1，幂另证。
**旧空谱锚：** R134/138/155付非ℓ1可和相位缺陷first的有界扰动/首一自然多项式；R189付G[X]普遍分式场。
**R268–270：** 非首一底座归R152/183；新增全F_p、快辅助及物理不交循环因子乘积。有限头仅单atom，普通慢Bell未全闭。
**R236字符：** F_q+v_c−λ的早偏离全闭，否则gcd(q−λ,αq′+δ)=1足，≤p−1候选；二次单位置有真零例，late-c双池类已排。
**R236双池/二分：** min位≥μN、max|a|≤C/√N、log det⁻¹=O(N^1.5)付全阶共振加一次辅助。自动池κ>1须global logρ_n⁻¹=O(n^1.5)，规则幂可双κ夹界；κ>2全尾比较只须liminf logρ_n⁻¹/n<∞，含全部非ℓ1，主零位须最终c=0。双池或小辅助尾的Sylvester逆/jets/C配对已付；普通点态幂另证，完整条件见open。
**R236双行平滑纤维：** 同一指数种子/尾比较下，F(U,V)主次数p且f_p(0)≠0，若F(μ,0)=λ各根的(F_U,F_V)不同时零，则准确混合共振ℱ_F−λ循环。混合G_rs/最高系数修正、分根偏导单位、(p,p)结果式与4dr jets全付。κ>2可放宽κ>1且存在t<κ、Σ|a|^t<∞，亦扩前线性二分；零主位规则保留。不可约U³+(1+U)V+V²全λ闭，双临界/普通点态式不外推。
**独立预算：** 固定盘|a/c|≤K、L_N=O(N^1.5)保；辅助圆r_N=εN(c_N*)²和Γ_Y=O(N²)保，含辅助α≤1指数/长平台。旧主尺度/子支撑各保假设。
**其余界：** R259/260/264–268保解析简单根/已证全重数预算。双导子投影在1<α<3余Leibniz末短和，两位校准排粗吸收；α>3及α=3大β归旧快类。中央域/运输/family293保正式稿及归档。

## 紧接稿及持续执行

1cf已推实根40cde166、双方向3bff9ad1、C范围订正73433202、实奇次减正辅助1bd43cc6；本次交叉分母正商。root续紧回传轨道预算，normal续正Koszul零商后的实际共同域，boundary续低核通量，kernel续Newton点态幂及双全C碰撞。
0c双行9fbb5e33已回读；本次周期多模式。待核短旗354186a1cff06b9b7d1e321b1f0c96253a9c1c09、真实预算9beeb63102216049585cc86bbc56ff6cf0dcf7d5；续一般真右因子/早期分支/多辅助。
完整证明即推，再接open；H更新，逐pull核规，不以阶段/时长收尾。


## 原 open.md

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

旧接口见[归档](../notes/2026-11-13-open-after-R262-rebase-before-condense-1cf8.md)及results.md。

## 共同适用边界

R125/R128/R140/R176/R184已付清真实闭域、通常伴随、自然多项式和共同正则器。全H单射稠密不自动传未知不变限制或有限放大子商；G的普遍范围不能扩成一般慢Acal。UHF只运输全空间范数，不运输未知Haar子空间。Haar正常态、边界奇异态、固定次数和实际全部向量不可混同。危险平方点态应用始终保留a_*=0；全等向不能换成局部等向，C未必保M，压缩交换子不能丢中央耦合。所有“已证明”均为中间结论。

## 当前接口一：原 Haar 慢符号的正常湮灭者

[删一预解因子](../results/R244-appendix-cofactor-input-domains-and-individual-resolvent-annihilation.md)对任意有限秩见证付P_i=∏_(k≠i)Ri的指定输入域、ΣMjP_i f_j=0及φ(P_iA′)=0；一般非最小情形不可再免费删因子。下述最小秩定理另给各Ri的理想湮灭。

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**R255范围。** [√3端点](../results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)排E_√3有限正见证，carry/最小域/正张量化已付且端点最优；一般正常有限秩不保该矩。R235另排保函数非负锥者，Hilbert正/C实不够。

**相对迹/真右矩。** [R235连续核](../results/R235-appendix-continuous-kernel-relative-tail-traces.md)及[正尾耦合](../results/R235-appendix-tail-couplings-almost-everywhere-continuity-and-bounded-obstruction.md)排连续/a.e.+双边UI类，恒模秩一反例保一般L∞缺口。[真矩](../results/R235-appendix-annihilator-tail-coupling-energy-and-right-tests.md)付尾能量下界及全G∈A′的|φ(T_mG)|/h_m≤λε_m||G||。仍须ε_m||G_m||→0而真实耦合非零；点乘相位/普通L²逼近不替代。

[R237及附录](../results/R237-actual-walsh-diagonal-normal-module-and-slow-annihilator-exclusion.md)排Walsh对角、有限翻转带、entrywise-ℓ¹及合格乘积基中的对角/有限头块正态，含无指数矩例；任意基混合及一般正常态不覆盖。复密度只给功能/迹零，C实循环秩一可无ℓ¹对角表示。

**配对仍开。** R244逐列域加非零锚足排见证；聚合全Walsh Gram往返仍需强主理想单位，逆最小性不能替代。

[预解正锚](../results/R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md)给RH⊂∩DomMi且Rg=1时矛盾Trρ>0，故秩一真见证的全部MU+F均全C谱。[广义预解](../results/R244-appendix-generalized-resolvent-unit-classes-and-vacuum-word-domains.md)付Mi=Ri⁻¹Di及Bézout；共同R主理想/像/Γ_R参数无关，Γ_R距真空≥√Trρ。真空原像⇔某个/全部排列的全部无重复自然子词合法。无广义预解或共同域缺口仍开，调参数不改变它。

[秩二链](../results/R244-appendix-rank-two-koszul-defect-and-double-common-graph-gap.md)有J²=−I、JT=T*J，非零Q无限维且无循环，两个共同图缺口均∞。[比例图](../results/R244-appendix-resolvent-minimal-cores-and-intermediate-ratio-spectra.md)对全部中间闭图给σ(T_EU+F)=C；Pg=1给逆最小性/真空图核心，不给强理想单位。[交叉正化](../results/R244-appendix-cross-denominator-positive-quotient-and-equivalent-metric.md)准确把x=(Cf1,Cf2)放入Q′=Q(R1D2,R2D1)，有界下界L及G=L*L给Gq=z_Q；Q′≃Q(R1,R2)⊕Q(D1,D2)为拓扑直和。交叉分母可非单射，正等价内积不代原H秩一/共同域。

**最小秩的逐分母零作用与全秩正商。** [完整证明](../results/R244-appendix-minimal-rank-individual-denominators-and-positive-koszul-zero-quotient.md)：若真正最小正秩为r≥2且每个Mi有广义预解，删除第i坐标/有界插入精确因式分解Ri。最小一般秩=最小正秩，故φ(RiA′)=0；低于r重放大的S稠密性更给各Ri在Q0=cyc(q)/closure S cyc(q)算子为0，Di因而为单位。一般r的b_i=DiPi有界Koszul商准确含x=(Cfi)，φ为其正向量态；diag(Di)及diag(∏k≠iDk)在真实Ri单射消因子后诱导链。两个循环S零商有带明确下界的有界同构，x不损范数、G0q0=z0。此单位性/下界仅在最小秩循环零商，不传全Q_R；x仍可满Schmidt秩r，原H正秩一与共同真空域仍未付。

[R267逆族](../results/R267-appendix-blaschke-block-strong-units-and-linear-degree-inverse-type.md)保逆线性下型κ=log(4/3)−1/4；前向族可无真空原像。[共同幂](../results/R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)给非零P∈F_A=∩A^rA′和收缩强*单位，F_A同范数强*稠密、AF_A=F_A、与UHF零交；有限旗单射稠密。共同幂原像为闭词图核心，非PH自动入域；1∉RanP。指定配对仍需全Walsh列平方可和，专属S因子未付。

**固定非湮灭态的完整块边界。** [R230完整Gram](../results/R230-appendix-arbitrary-contractive-block-gram-and-complete-source-obstruction.md)对同一非湮灭f及q_i=16^i排所有可逆收缩纯块的合格逆源，实际完整Gram比值指数log5/2，有限完整源组合亦排；负实真实粗源g∉H_√3保留。非块/无真空原像未覆盖。

**真密度完整矩与正证书。** [R230完整定理](../results/R230-appendix-positive-density-moments-dual-certificates-and-localization-obstruction.md)给m_B=L_Bρ_B、Gram=||R*m_B||、LL*=[[2,2],[2,6]]^⊗n及全部列carry。真湮灭右残量≤λε_m(K_n+d_B)，纯列另付λκ_md_B；它依赖非正Tr_(B^c)(ρT_m)/h_m，不能免费写成K_B*m_B。有限块正性对偶inf{μ:μI−ΠΩ+Re(TX_u)≥0}严格可行；理想内R=TX_v收缩且||RΩ−Ω||≤a<1/2给μ=(1+a)/(2−a)、u=v/(2−a)，故可得正余量。

[统一定位障碍](../notes/2026-11-13-first-tail-obstruction-to-uniform-full-moment-localization-normal-complex.md)对任意n物理位K_B给τ≥q²/[8√3(n+2q+1)^(3/2)]；最优统一正密度矩常数C_n≥5^(n/2)，故τC_n≥√q/144→∞。它排先范数截块再统一放大，不排全空间右因子或真湮灭密度专属消去，后二者继续开放。

R242窄图、R248不交换阻尼、R250稀疏图的限制保归档，未得撤阻尼/A+不变。

**点态实见证与准确商实结构。** [R228完整附录](../results/R228-appendix-pointwise-realification-reflection-pairing-and-weighted-quotient-real-structure.md)用J0实际共轭：J0平均保真湮灭但一般改变φ，双重平均仅与J0平均同φ；反射偶/奇实谱向量两两合并，实密度精确降至max(rankP+ρP+,rankP−ρP−)。最小实支撑至少与一个奇偶空间零交。实Mi本身只Krein对称，已有广义预解才付全伴随域；复参数的rank2商须Θ_Q=P_Qdiag(Wi)J0，Wi barWi=I。Ri真实时无权iJJ0才自伴酉，正负指数均无限；均不提供共同图核心/原空间秩一。

**实化与降秩须分开。** [R228/229范围订正](../notes/2026-11-13-r228-r229-c-realification-scope-correction.md)：(ρ+CρC)/2在整个A′保同一正泛函，但可增秩；两两配对不保迭代到秩一。R229及9维实幂零例只排一般正秩一表示，不排C实化且非本题真见证。未知子商C不变、普通TρT*保湮灭不可假定。R240固定非湮灭态排通用first配对，专属/两端可变仍开。

R210–211奇异正态/Cantor族不具Haar正常性；固定正则端、Fock及增生平滑等旧障碍保归档，不代表真实正常矩。

[R253相位消元](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)给I⊗Q_m∈S Acal及真见证必要q_m↓0。[复指数/Gram](../results/R230-appendix-complex-exponential-tail-right-filters-and-full-gram.md)保完整有限Walsh列、实际carry及共同次数相位N_B锥；[全标量Fourier](../results/R230-appendix-scalar-fourier-extraction-and-arbitrary-polynomial-filters.md)保任意系数与(q+deg p)log(q+deg p)=o(q⁴)实际预算。

**增长周期多模式亦已排。** [逐位Jensen/多元完整证明](../results/R230-appendix-entropy-tilts-and-growing-period-multivariate-filters.md)给纯正锥真空比≤exp[(m+1)/2−πk/16]。按模r分成Uν后，多重等距Fourier与完整次数求和给r≤q/100的纯高次比≤exp[m/2+1/4−q/10]。实际Q_mp(Uν)对全部总deg≤q³复多项式统一保两倍该界，无系数/相消假设；输出系数经两次线性换元、准确除(Σzν)^q才控制右因子，全部carry支付。独立周期exp参数max|zν|≤q⁶同界，全局q次投影给不依赖相位的范数分母。

复测度混合仍须实际相对输出误差ΔTV/||Q_mG||→0。非周期系数、超出模式/次数预算及密度专属一般右因子未处理；远处平顶高次有真空比趋1的反例，故不能删除慢模式和左理想结构，亦不能称完整q_m已受控。

[R253域附录](../results/R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md)：真实图carry已付，D∞不含RanS；有限first预解积非S有界右倍数，专属配对仍开。

**已排除的通用正则化。** R230/R261规范正积的累计ℓ²、完整逆e^{o√q}及共同子半次数域非像，旧Cayley方向增益、R253全A^r有界除S失败和R263同一H_(1/(60e²))向量不在两RanS，均保于[本次完整归档](../notes/2026-11-13-handoff-open-before-residual-flags-1cf8.md)及results原稿。像含该小指数域的有界分母不能除S；这些结论不排真见证专属配对。

[R237相对密度](../results/R237-appendix-asymptotically-contractive-principal-ideal-approximation.md)：固定Q∈Acal的QAcal同范数强*逼近QA′；q_m可搜尾A′，不含非UHF左因子/无界右因子。一般S分母仍开。

## 当前接口二：实际边界的除法饱和

固定两个实际边界T_N/T_Y，M=kerT、N=closure BM、D=M⊖N。R187/200已给各有限稳定像及M∩RanB^r⊂N，有限孔核仅真空；真正问题是**无权核内稠密与N=M**，不将环境有限孔稠密当核内核心。

**旧接口。** R234模N已闭；R238原J_q成本不代R239模N成本。环境Γ坏见证在M⊥、横向T*M非BM原像；真幂界保真输入、头链与未知尾。旧预算见[归档](../notes/2026-11-13-handoff-open-before-exact-boundary-gram-0c.md)。

**全整数窗口和真正最小Gram。** [R239全q](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原进位，低投影e−74d⁴/真实lift e−75d⁴；d≈log^(1/3)q、K*=3(16/770)^(1/3)。c>K*权核入N，真D尾常数K*/2，权阶先属R271。窗口ell=d+m的Σ1/[ell(1+λ²)]发散足N；真D倒能量≤8τ_Q²/||w||⁴。λ²=O(q log^(2/3)q loglogq)足但未得。

[准确Gram](../results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)为G=D0P_kerS D0*，严格正；实际r=Avq自动D^d，λ²=〈G⁻¹r,r〉。Schur补不可省；窄带正/倒能量仍容慢尾。逐头单块残量/旧d核阶及Tr(ApKp)非零保原范围。

**局部坏方向与原始块。** [局部最优](../results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)给全低输出logΛ_q=Θ(log^(4/3)q)，无限高尾仍保；[原始块消去](../results/R239-appendix-unweighted-primitive-removal-high-rank-blocks-and-full-projection-obstruction.md)给同一坏v的||P_Mv||→0。相容真空jets使受控q孔原始P的真残量小修复趋零；可取||P||→1、log rank=(2log2−o1)q。完整固定前缀原始投影仍唯一且log||P_full||≥(4log2−o1)q，不能用它作受控全覆盖。

**移动窗与双宽能量。** [完整定理](../results/R239-appendix-moving-primitive-windows-and-double-width-repair.md)把原始块移k≤d并保真实自由坐标；B=A+D_free相容展开给双宽原始分量小修复，λ̃与补块差→0。新2d窗的lift、ell̃=2d+m全整数覆盖≤2及倒数准则独立重核；所需λ̃增长未得，旧d链旗不直接搬到2d。

**完整首个三维块分解。** [完整证明](../results/R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)用相邻P_i及Q_i=I−P_i，得T_i=P_<iQ_i、T∞=ΠP_i和I=ΣT_i+T∞。首次离开正交展开只付Σ角度²；分析/合成A,B=1+O(m^−1/2)对全部分支一致。明确在RanT_i中最小化后B⁻²λ_h²≤Σμ_i²≤A²λ_h²，适用各自定义的d/2d/更宽窗。三维原正交链权α=ρs、β=s及真carry方程已付；T_iw不继承w⊥N。

**非真空低孔前缀与增长末段。** [精确Fock塔](../results/R239-appendix-low-hole-fock-tower-and-nonvacuum-primitive-prefix-removal.md)用R_p=D_p*(D_pD_p*)⁻¹构造V_p，准确D_pV_p=V_(p−1)a_p，Gram递推给全层误差Δ≤ε[32(P+1)]^P，不把单层coercivity充当相容控制。s=floor(c logq/loglogq)、0<c<1，J=m+2(q−s)、P=s+d−1时Δ≤q^{c−1+o1}→0。固定前q−s个原始配对后余尾允许s孔；按出生层重建真核，在原宽d内修复P_(q−s)r，范数≤(1+o1)τ_q+e−71d⁴||w||。全部真实未来层/初值误差及Γ_d≤e^d⁴已付。一次完整分析界给μ∞²+Σ_(i>q−s)μ_i²→0，无√s；原λ_h与补块最小值之差趋零。早期三维支总能量和真最优通量仍开。

**原完整链与固定头速率。** [R239闭链/Riccati](../results/R239-appendix-closed-repair-chain-riccati-and-terminal-leakage.md)付固定窗闭像/最优链/准确Gram及加宽极限。[R271统一相对率](../results/R271-appendix-fixed-head-condition-and-uniform-window-convergence.md)用真实零源核的总级数分块及G=P_ZS*S|Z的带宽d−1，付Chebyshev有限传播：λ_d≤κλ∞，λ_[d+n(d−1)]²−λ∞²≤4(κ²−1)((κ−1)/(κ+1))^(2n)λ∞²，对所有q/源统一；实际最优链平方距离准确等于能量差，Gram同样相对夹住。κ是原头相似条件数，m增长时须支付κ_m及宽度；不能直接塞入旧真实lift，也不降低无限窗本身的坏能量。

[R271平方局部型](../results/R271-appendix-square-head-smith-types-and-old-head-single-block-correction.md)给旧跨头Smith(2d−1,2d+1)、新4d，排稠密像D交织。固定混合核有限孔/正指数核心不传原核；上角残量可用旧d头修复，最多增2d孔但成本仍依Q。

[R271残量旗](../results/R271-appendix-orthogonal-residual-flags-and-exact-source-gram.md)准确给R=⊕e_i kerD^(d−i−1)及全部链i≤d−t/kerD^(d−i)，Gflag为完整Schur补。[联合旗能量](../results/R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)付同时右逆C≤e^d⁴、Gflag≥e⁻²d⁴、最优||y||≤Cλ/||z||≤C²λ，全部进位及删除核投影误差≤e⁻⁷⁰d⁴||w||λ。真缺陷迫Σ〈H_tw_(q+t),P_kerD^(t−1)z_t〉≈||v||²+λ²；原H_t只跨≥2头格但含1/4，不能称小进位。剩余为这条真实最优低核通量，无权N=M仍开。

[R271准确插值](../results/R271-appendix-exact-stable-range-interpolation-and-norm-defect.md)给Π(Nexp)=ΠN=ΠM=V及有界线性右逆；原像范数按真实修复能量计。插值Gram差ΠP_W在W≠0时范数趋1；没有固定w的有界原像子列，不能推N=M。

[有限尾塔直接推论](../notes/2026-11-13-finite-tail-tower-corollary-for-exact-residual-flags-boundary-resume.md)把底层下延到q−d+1，kerD^h恰为出生层s>p−h坐标；联合旗限制仍是有限矩阵列限制张量恒等，故S_flag/伴随像闭，原对偶inf取得且固定m,q有界依赖源。原始P及I−P保实际残量旗和全部可行链旗。此为R239旧有限塔法的直接推论，不是新的统一能量界。

## 当前接口三：一般系数行与多个模式

[R176共同谱](../results/R176-appendix-bounded-part-spectral-intersection-and-common-exceptional-root.md)给有界不变部分谱相交/连通、所有有限谱部分共用r_u；全部倾斜/点态幂坏值至多一个，须q(r_u)=q(r_u−2α)。[实结构附录](../results/R176-appendix-real-structure-affine-lines-and-odd-power-cyclicity.md)用逐点J给r_bar(u)=bar(r_u)，故任意实u、任意复权的全部(u^(2k+1)−λ)^m循环，无尾率条件；偶次仅留λ=α^(2k)。任意q|R单射也全λ闭合，含p(u)+iu−λ；无实根q的零位移全部幂闭合。ℓ1复误差只迫r在仿射实线，实际首位未必沿线；共同有限谱部分存在才有跨行加性。剩余实碰撞核未排，亦未构造有限谱部分。

[R147慢辅助切片](../results/R147-appendix-bounded-slow-auxiliary-slices-and-polynomial-cyclicity.md)付任意ℓ²主/权、有限ℓ¹辅助的最高字符单位与真实差商；坏值须两个首位切片碰撞。[实辅助推论](../results/R147-appendix-real-slices-odd-minus-positive-auxiliary-and-all-shifts.md)把碰撞根限实：实u、ε=sign首系数，实ℓ¹居中v与正定实R(0)=0，全部[εu^(2k+1)−R(v)−λ]^m e^w循环，任意支持次序/复权，无尾率预算；含全部u³−v²（首系数正）。复一次辅助c/α不在实射线(−∞,−α^(2k)]也全λ闭合。u³+v²的真实碰撞、最高字符零及双无界仍保。

**既有单模式。** [R236](../results/R236-appendix-all-multiplicities-of-canonical-weighted-polynomials.md)的规范、临界弱ℓ¹、σ>1幂尾及α≤1指数子序列类均已闭，全部真实域/重数证明保留；R268给更广准则。

**更多排序行。** [R268](../results/R268-entropy-budget-weak-l1-bandwidth-and-all-multiplicity-cyclicity.md)沿N满足sup_(k≥N)kρ_k≤DNρ_N、Σ_(k≤N)log(ρ_k/ρ_N)=O(N²)、logρ_N⁻¹=O(N^1.5)，则全部q(u)e^w循环。实际成本E_N+log^(4/3)ρ_N⁻¹+N²及jets/ad域已付；未满足准则的little行、1<α≤3剩余带仍开。

**旧混合范围。** R269保熵主行的解析A首一/有限头点乘及ℓ1主有限头P；R270A按最大根重数μ许c=O(|a|^max(2,μ))并保最高重根非共振，小o无需速率。R270二阶及全阶F_p的非零共振组合循环，底座和非首一最大闭包归R152/183，R184/186旧联合域已扣除；单支撑真零例与原自然域未必闭仍保。[快辅助](../results/R270-appendix-fast-auxiliary-modes-and-resonant-polynomial-modules.md)给任意ℓ²主/权的Σh_kF_k及全部mixed域，p≤1去主行ℓ1。普通慢Bell与一般慢辅助仍未全闭；原各稿链接/条件保[本次前全文](../notes/2026-11-13-handoff-open-before-newton-ordinary-two-slow-1cf.md)。

[R236零输出分类](../results/R236-appendix-resonant-polynomial-zero-output-and-leading-order.md)：a∈ℓ¹、s=a*+Σa、μ=mult_s q、L=支撑数，T_q=Σq^(r)(s)e_r(a_j(R_j−I))为零⇔L<μ；非零首阶为最早μ个位的2^j之和，μ=0为单位。无限支撑循环及二次关闭归R270C。

**全阶可和偏离与字符互素。** [R236字符定理](../results/R236-appendix-real-dyadic-factor-character-coprimality-and-all-order-deviations.md)对非零主行、任意a,b∈ℓ²/c∈ℓ¹及F_q+v_c−λ给：早偏离处理全λ；否则α=a_ja、δ=c_ja，gcd(q−λ,αq'+δ)=1足循环，至多p−1候选。实际dyadic A幂、核内字符单位和C/Fourier均付，不除G_n本体。p≥2且j_c≤j_a的F_p+v_c已全闭；二次唯一候选λ*=(δ/2α)²确有单位置零输出例。一般late-c的λ0不能由这条字符判据排除。

**全阶双池与不规则行。** [二位完整证明](../results/R236-appendix-all-order-resonant-two-site-bezout-and-derivation-budgets.md)：两池各N位、min位≥μN、max|a|≤C/√N、log跨det⁻¹=O(N^1.5)，给全部固定q/λ的(F_q+v_c−λ)e^w循环。实际ΔG_n无平方零一次项，4pr jets、绝对系数/两次r!平均及左右A四次成本全部已付。

[自动排序池](../results/R236-appendix-automatic-separated-pools-and-two-power-envelopes.md)覆盖最终κ>1双侧比较、c∈ℓ1及全局logρ_n⁻¹=O(n^1.5)，允许零主位另有无限ℓ1辅助；两侧幂主行还许κ_−/κ_+不同夹界。另[指数种子二分](../results/R236-appendix-nonsummable-main-dichotomy-and-all-order-sylvester-inverses.md)在κ>2全尾比较与liminf log⁺ρ_n⁻¹/n<∞下闭全部q/λ，含所有ℓ²\ℓ¹。有限例外任意但主零位须最终c=0；首次降幅后双池或真辅助小尾，乘积逆一次Cauchy给Γ_Y=O(N²)。两套范围不互换。

**双行非线性共振与平滑纤维。** [完整新定理](../results/R236-appendix-two-row-resonant-smooth-fibers-and-sylvester-dichotomy.md)沿上述指数种子/最终比较，对F(U,V)=Σf_k(V)U^k、主次数p≥1且f_p(0)≠0，若F(μ,0)=λ每个根均(F_U(μ,0),F_V(μ,0))≠(0,0)，则准确双行共振(ℱ_F−λ)e^w循环。全部mixed G_rs真实二阶消去，最高系数含纯V修正；分根的偏导单位/(p,p)Sylvester结果式及总次数d的4dr jets已付。未排除的双临界值至多p−1个，不断言它们真有核。不可约F=U³+(1+U)V+V²的集合为空，故全λ闭。

同稿精确扩κ>1，只需某固定0<t<κ满足Σ|a|^t<∞；真实尾付ρ_tail^{κ−t}S_t，线性F=q(U)+V亦得全部q/λ。仅有ℓ²不能免费覆盖κ≤2。全部符号保混合/纯辅助Bell修正，未变成普通点态F(u,v)。扣除既有锚/快类后，可和极快、无比较辅助、双临界纤维及独立慢多辅助仍须处理。

**其他实际预算保独立范围。** [固定盘逆](../results/R236-appendix-fixed-disk-kernel-inverses-and-sparse-linear-deviations.md)对无限S上|a/c|≤K、S辅助L_N=O(N^1.5)有效，S外任意主/辅助；[辅助尺度共同圆](../results/R236-appendix-auxiliary-scale-joint-resolvent-and-independent-tail-gaps.md)取δ_N=c_N*、r_N=εNδ_N²，双删除及一次联合Cauchy给L_N=O(N^1.5)、Γ_Y(r_N)=O(N²)充分。含任意主行配辅助双侧α≤1伸缩指数，或Σ_(n>N)c_n*=o(Nδ_N²)、L_N=O(N)长平台；明确正相位例Y∉G。旧[主尺度共同圆](../results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)/[子支撑](../results/R236-appendix-supported-deviation-arbitrary-background-and-empty-spectrum-scope.md)也保各自假设，不互换排序/半径。

**旧空谱范围。** [审计](../notes/2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)按R134/138/155：非ℓ1且可和相位缺陷first已空谱，有界A′扰动及首一自然多项式有真有界逆并保持未知限制；任意复ℓ²权/ℓ¹辅助早已覆盖。居中ℓ¹和全C慢分支仍需证，不能免费取二次分歧根。

[R257/258](../results/R258-entire-selfadjoint-kernel-transport-and-actual-tail-mobius-domains.md)整自伴运输不传原M点乘域/不变格；R224公共像/尾商障碍保留。

[R259](../results/R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)闭同幂尾p>1/2；[R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)闭排序limsup nρ_n>0的任意复行及物理重排，允许全部复first指数和有限联合解析Bell芽。其完整域导子代数无maxF成本；剩余解析分支须nρ_n→0且排序复和→Φ(0)，一般行重根另证。

[R264–266](../results/R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md)已闭α≤3/2的解析Bell/简单根及α≤1全重数；R268严格扩展后，规则1<α≤3/2的普通点态全部重数仍开。

**高阶导子及剩余短和。** [纯提升障碍](../results/R236-appendix-high-degree-raising-band-obstruction-and-range-projections.md)给r≫√Q的有界提升弱趋0；[全域双导子](../results/R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)付[ad_T^(2r)U_N](../C_Q^r)†强趋I、r=ηQ<Q/2、伪逆≤e^(Q/2)及全部carry。它不是单个导子像；核配对完整Leibniz在1<α<3尚余末O(N^((1+α)/4))项。[两位校准](../notes/2026-11-13-two-bit-pseudoinverse-calibration-central-next.md)排共同尺度粗吸收；须核内抵消或适配降阶，α=3不自动短段。

**旧快类。** [R236核查](../results/R236-appendix-existing-fast-classes-for-supercubic-sorted-rows.md)据R175：排序ρ_k≤Be^(−βk^α)、α>3已给非零q(u)e^w循环及标准主理想/普遍表示，无需下界。α=3时首阶r的β>80r⁴/3给限制稠密/强主理想，β>400r⁴给标准范数理想；均严格充分。单个四次幂界不等于G。剩余1<α≤3须扣这些旧例。

[R270第六附录](../results/R270-appendix-disjoint-slow-point-polynomial-products-and-head-masks.md)：物理不交慢模式的已知点态循环因子可相乘，故∏(uν−λν)^mν e^w循环。mixed词域/Bell已付，共享有限头仅保单atom；同模不同根、atoms之和不能这样相乘。

## 1. 一般向量的矩分离与有限二阶以上输入

R101仅有限Walsh次数两端；任意非零L²循环性、一般二阶核、gauge差在未知核上的像、双独立慢模式仍开。R130/131/143的闭域与跨核配对不许取消A^h后补域；R29/44/51和R163/165平滑/Lp/Orlicz障碍保留，有限柱近交换不是真Nj交织。

## 2. 不变限制中的一阶闭乘子值域

R125/128/140保真实闭限制、R(t)与图核心。任意复ℓ² first在未知M上dense仍开，准确等价closure S(t)M=M；全H稠密、C保核及四正分量不替代。正行/可和相位缺陷非ℓ1、G及已付四次尾型各保原范围；一般慢S(t)不自动快。C对称Volterra反例排抽象法，R176共同谱仍允许单点拟幂零部分。

## 3. 任意有界有限 chaos、范数代数及完整交换子

非零Acal/A′元素的一般排核、零锚有界二阶及无限低位行消去仍开。R32无零因子仅代数内部；R88纯/真实对应不保乘法或核；R92固定有限chaos的连续代表及非零字符可逆范围不扩。R143首位图须TBT=α₀、真实域及分母有限放大稠密，最大商图不独自排核；R124余数零字符不保可再除A，不能把首阶r>1免费降到1。

R185/188已给非标准主理想J无限余维、不含A幂、与指定G/bounded K零交；S在原H仍单射稠密，故不直接给原空间不变子空间。进一步理想分类仍开；R140强主理想与范数理想、R121根式非闭及R112/119归一化幂障碍均保。[R256](../results/R256-bounded-weighted-composition-commutants-of-the-radial-haar-model.md)分类nonsingular底映射的有界加权复合交换子只有cA^n（n普通非负整数），只需η_j→0；一般非复合交换子未闭。其余旧范围与外部Thomas/Peters/GT条件见[本次前完整原文](../notes/2026-11-13-handoff-open-before-cross-denominator-positive-quotient-1cf.md)。

## 4. 相对乘积、多项 cocycle 与混合解析芽

**普通双慢的Newton消元。** [R150完整证明](../results/R150-appendix-empty-first-anchor-newton-degree-and-ordinary-two-slow-cyclicity.md)：X_u空谱、实际首位j_u≤j_v，且deg g=p>m=deg f≥1，则全部[f(v)−g(u)−λ]e^w非零循环，任意λ/复ℓ²权/支持重叠，v可独立非可和全C行。真实慢Bell系数全留A_h，gauge差的实际A^h商给结果式最高次数m(p−1)和单位系数；X⁻¹将其有界化为保未知M的单位。普通v²−u³−λ由此闭合，无共振修正；只已证点态一次，全部括号幂、相同/反向次数及首位相反仍须另证。

[R189一个空谱锚](../results/R189-appendix-one-empty-anchor-two-additive-direction-kernel-elimination.md)给空谱相位X与任意first/有界Y的非零G[X,Y]最大实现单射稠密；总加性类秩≤2且含实际空谱组合亦得。只消Y并用旧普遍dense的ρ(X⁻¹)付跨核。全阶双共振q已付，三独立类、双全C方向及新多项式普遍限制范围仍开。

R127已闭相对ℓ¹两乘积；复杂相位相对ℓ²、三以上cocycle、非解析闭包/一般有界商仍开。R129/135单轴、R146/148单慢加快、R152有界加性及R153快分式各保原范围，超越分支未普遍限制dense。

R160慢二阶Bell不自动属G；R77/79/82临界中间参数及R83芽/轴谱仍开。R162纯虚倾斜不保乘法，指数权点态循环不扩任意H向量。

仍可寻找固定单射R∈A′使所有非例外ζ有B(RM,UζM)=0：此时closureRM非零且含于M即可用R122，无须先dense。当前辅助因子依ζ变化，可数全H稠密像之交不自动与未知M非零相交。

## 5. 一般 ISP 的独立路线与不能省略的障碍

R5缺非零拟幂零秩一扰动及任意T归约；R7双锚未普遍实现，R2/R17/R18排内部紧修正。R4/R6观察拟仿射失败，Rota须真中间空间，R8双生成提升非充分归约。R114/R164/R165排既有紧化/一致平方可积路线，实际UHF交织Calkin忠实且角谱等于本质谱。

R105/R107核对的PPP1995谱圆、MM1974、AT/AM紧化条件不满足；JKP2019完整条件及Tucci迹转Haar未付。[family293审计](../notes/2026-11-13-family293-hyperinvariant-scope-and-backward-normalization-audit.md)仅超不变结论，其纤维有普通真尾空间且交换子非交换；Domar权不同，不能借R88或反向归一改称普通反例。未重编Lean。原全部条件保[发布前全文](../notes/2026-11-13-handoff-open-before-exact-low-window-interpolation-1cf8.md)。

## 不能互换的极限

全部混合自然词域不保普通系数截断；可数first核心及固定正则子在子商单射稠密，不使原词普遍dense。非零有界交织不能把全像送入全部first域；R204重选行不代固定慢行或边界运输。实际域、carry、非零锚仍须支付。

[R239首位图](../results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)/[横向压缩](../results/R239-appendix-coercive-adjoint-and-positive-mixed-compression.md)保C²=η₀N₁|L、||C||<1/√12，真缺陷需C*Gx=0及C*x=−η₀(N₁|L)*Cx。核上T*≥7/8、Re(P_MBT*|M)≥5α₀/6，给M⊥内横向同构而非BM原像；各位压缩约束仍未排缺陷。详式和度量字典在原稿及本轮归档。
