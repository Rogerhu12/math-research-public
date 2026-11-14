# R244MinimalRank 发布前 HANDOFF/open 完整原文

核读 main：9fbb5e33cf96f88f8f3142552513fdf83291d852。两README blob未变；终端unavailable，按根§8小文本后备，API不计实际pull。

## HANDOFF.md 原文

# 交接

## 目标、负责人和规则检查点

- **目标未完成：** 必须完整解决可分无穷维复Hilbert普通ISP。Haar普通不变格、边界N=M及一般正常湮灭者仍未知；规范单模式全部多项式加权输入现已循环。不降低README完成标准，不以阶段或时长收尾。
- **负责人及分工：** Astra-ISP-1cf8c51d负责，0c继续贡献。1cf用R213–229、R240–271；0c用R230–239。新编号先登记，独占git/index，不动他人未发布文件。
- **最后实际pull/规则：** 2026-11-13 01:06:52 UTC，cdb9429c93f969d1054d8e1e49643add83457c24；真实git pull --rebase origin main，两README差异空。每小时至少一次，终端恢复即补。
- **0c 最近实际 pull：** 01:06:17 UTC / bfe9f2c0b2977d4bab3d14793c3f247374e81303，两README差异空；后续含05:20:35、06:03:04的真实pull调用均执行前No usable execution environment，API非pull，恢复即补。
- **已读规则blob：** 根 f787a306d90892d8dec765dc59747d60ba39f055；题 6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd。每次实际pull均比较两README，有变只读差异立即照做并记SHA；至少每小时pull。
- **API后备检查点：** 2026-11-13 06:35:13 UTC / main 078e9507c419b4e047d96f293c75648c03c1d383，两README blob未变；0c 06:03:04、1cf 06:31:47真实pull执行前无环境，API非pull。
- **发布：** 完整结论单独推；终端可用用git，拒推即pull --rebase。仅失联用根§8小文本；API不算pull。令牌仅命令行，不写文件/config/提交；不force、不写根LOG；Markdown<100KB、H<10KB，合并最新main。

## 恢复记录与模型

工作树：1cf /tmp/isp-1cf8c51d-math-research；0c /tmp/isp-0c017065-math-research-20261113-0030。本次压缩前全部H/open及归档链见[完整原文](notes/2026-11-13-handoff-open-before-cross-denominator-positive-quotient-1cf.md)。

模型：H=L²(Z₂)，A为真实Haar加权odometer；Nj=A^(2^j)/dj=Ej+ηjEj*N_(j+1)、ηj≤e^(−770·16^j)，Y=N/(1+N)、V=I−2Y。A′交换/C对称，R88有界SOT多项式逼近。UHF不运输未知限制；C保核、局部等向和输入域不可免费。

## 1. 原 Haar 正常湮灭者

**R228实结构：** J0平均保S真湮灭但一般改φ；C平均保同φ。J0实密度的反射两块秩p,q可精确合并至max(p,q)，最小实支撑至少与一个奇偶空间零交。实Mi仅先得Krein对称；复预解参数在rank2商须带权Θ_Q=P_Qdiag(Wi)J0，平方I。真Ri实才有无权Krein度量，正负指数均∞，不代共同域。
S_N/Y全H单射稠密已证，普遍强主理想仍开。失败有正有限秩正常见证；R228允许C实化，R229反例排一般秩一纯化，R242窄矩阵/垂直商图已付但不免费图稠密。
**既有正态范围：** R255排E_√3有限正见证且端点最优；R235保函数非负锥及R237 Walsh对角/有限带/entrywise-ℓ¹/指定乘积基有效，一般正常态不覆盖。

**R235：** 连续/a.e.+双边UI已排，普通L∞不够；全右矩|φ(T_mG)|≤h_mλε_m||G||保留，待预算内非零右配对。
**R237：** 固定Q∈Acal的QAcal同范数强*逼近QA′；非UHF左因子/无界右因子不覆盖。
R248阻尼不交换、R250未得A+不变，详式保归档。
**R253/R237/R230：** 真湮灭迫q_m↓0。纯标量闭理想D_m^q alg(D_m)真空比≤Γ_q=O(q^(1/3)e^−cq^(2/3))；实际任意复p(U_m)在(q+deg p)log(q+deg p)=o(q⁴)内统一衰减，含deg≤q³，自动付相对carry。exp/Gram、共同次数相位锥保；指数混合保相对输出条件。多坐标/超预算/真密度专属仍开，不代完整q_m。
**R244：** 广义Ri付Mi=Ri⁻¹Di；共同R理想/像/图参数无关，真空原像⇔全部无重复词域。删一因子P_i付指定域/φ(P_iA′)=0。rank2 Q有J²=−I、无循环向量，两层图商∞；全部中间比例图TU+F全C谱。新交叉链Q′=Q(R1D2,R2D1)准确含x=(Cf1,Cf2)，φ(F)=〈F_Q′x,x〉；L:Q→Q′有有界左逆，G=L*L>0可逆且Gq=z_Q。Q′有界直和Q(R1,R2)与Q(D1,D2)，x在前支。正化为等价内积，不给原H秩一见证/共同域；Pg=1不代强理想单位。
**R267：** P∈F_A=∩A^rA′非零且PW_n收缩强*趋I；F_A同范数强*稠密、AF_A=F_A、与UHF零交。共同幂原像是闭词图核心，非PH自动入域。1∉RanP；指定配对仍需Walsh矩平方可和。
**R230固定态：** q_i=16^i排可逆纯收缩块及有限完整逆源组合，Gram指数log5/2；非块/无真空仍开。
**R230真密度：** 全矩/全列carry/Slater付清，右列保ρT_m交叉约化；统一正定位常数≥√(2^m)/144，真态专属仍开。
**R230/261：** 规范正积完整逆e^{o√q}、β<1/2共同域非像，通用配对/分母已排。

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
**旧空谱锚：** R134/138/155付非ℓ1可和相位缺陷first的有界扰动/首一自然多项式；R189付G[X]普遍分式场。
**R268–270：** 非首一底座归R152/183；新增全F_p、快辅助及物理不交循环因子乘积。有限头仅单atom，普通慢Bell未全闭。
**R236字符：** F_q+v_c−λ的早偏离全闭，否则gcd(q−λ,αq′+δ)=1足，≤p−1候选；二次单位置有真零例，late-c双池类已排。
**R236全阶双池/二分：** 双池min位≥μN、max|a|≤C/√N、log det⁻¹=O(N^1.5)足；自动池保κ>1/global logρ_n⁻¹=O(n^1.5)，零主位可另ℓ1辅助，规则幂可双κ夹界。新κ>2全尾比较只需liminf log⁺ρ_n⁻¹/n<∞，含全部ℓ²\ℓ¹；降幅后双池或极小辅助尾，Sylvester乘积分母一次Cauchy给Γ_Y=O(N²)，jets/C配对已付。新二分主零位须最终c=0，有限例外入头。任意相位/排列、固定q/全λ保，普通点态幂另证。
**R236双行平滑纤维：** 同一指数种子/尾比较下，F(U,V)主次数p且f_p(0)≠0，若F(μ,0)=λ各根的(F_U,F_V)不同时零，则准确混合共振ℱ_F−λ循环。混合G_rs/最高系数修正、分根偏导单位、(p,p)结果式与4dr jets全付。κ>2可放宽κ>1且存在t<κ、Σ|a|^t<∞，亦扩前线性二分；零主位规则保留。不可约U³+(1+U)V+V²全λ闭，双临界/普通点态式不外推。
**独立预算：** 固定盘|a/c|≤K、L_N=O(N^1.5)保；辅助圆r_N=εN(c_N*)²和Γ_Y=O(N²)保，含辅助α≤1指数/长平台。旧主尺度/子支撑各保假设。
**其余界：** R259/260/264–268保解析简单根/已证全重数预算。双导子投影在1<α<3余Leibniz末短和，两位校准排粗吸收；α>3及α=3大β归旧快类。中央域/运输/family293保正式稿及归档。

## 紧接稿及持续执行

1cf已推实根40cde166、双方向3bff9ad1、C范围订正73433202、实奇次减正辅助1bd43cc6；本次交叉分母正商。root续紧回传轨道预算，normal续最小秩全因子/Koszul域，boundary续低核通量，kernel核Newton消元；固定头窗率本次已推。
0c低孔a7346bed已回读；本次双行平滑纤维/ℓ^t。周期多模式完整源4efb54f658bc9090a27c896e08884d5835350178待核；代理续真实预算边界、早期三维支与一般右因子。
完整证明即推，再接open；H更新，逐pull核规，不以阶段/时长收尾。


## open.md 原文

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

R125/R128/R140/R176/R184已付清真实闭域、通常伴随、自然多项式和共同正则器。全H单射稠密不自动传未知不变限制或有限放大子商；G的普遍范围不能扩成一般慢Acal。UHF只运输全空间范数，不运输未知Haar子空间。Haar正常态、边界奇异态、固定次数和实际全部向量不可混同。危险平方点态应用始终保留a_*=0；全等向不能换成局部等向，C未必保M，压缩交换子不能丢中央耦合。所有“已证明”均为中间结论。

## 当前接口一：原 Haar 慢符号的正常湮灭者

[删一预解因子](results/R244-appendix-cofactor-input-domains-and-individual-resolvent-annihilation.md)：真有限秩矩迫每个P_i=∏_(k≠i)Ri满足P_i f_j∈DomMj、ΣMjP_i f_j=0及φ(P_i A′)=0。rank2即单Ri理想湮灭，并有准确商向量配对；未得Cf交叉域，不能再删第二因子。

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**R255范围。** [√3端点](results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)排E_√3有限正见证，carry/最小域/正张量化已付且端点最优；一般正常有限秩不保该矩。R235另排保函数非负锥者，Hilbert正/C实不够。

**相对迹/真右矩。** [R235连续核](results/R235-appendix-continuous-kernel-relative-tail-traces.md)及[正尾耦合](results/R235-appendix-tail-couplings-almost-everywhere-continuity-and-bounded-obstruction.md)排连续/a.e.+双边UI类，恒模秩一反例保一般L∞缺口。[真矩](results/R235-appendix-annihilator-tail-coupling-energy-and-right-tests.md)付尾能量下界及全G∈A′的|φ(T_mG)|/h_m≤λε_m||G||。仍须ε_m||G_m||→0而真实耦合非零；点乘相位/普通L²逼近不替代。

[R237及附录](results/R237-actual-walsh-diagonal-normal-module-and-slow-annihilator-exclusion.md)排Walsh对角、有限翻转带、entrywise-ℓ¹及合格乘积基中的对角/有限头块正态，含无指数矩例；任意基混合及一般正常态不覆盖。复密度只给功能/迹零，C实循环秩一可无ℓ¹对角表示。

**配对仍开。** R244逐列域加非零锚足排见证；聚合全Walsh Gram往返仍需强主理想单位，逆最小性不能替代。

[预解图与正真空锚](results/R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md)给RH⊂∩DomMi、Rg=1时正锚Trρ，秩一真湮灭必σ(MU+F)=C。[广义预解与有限词域](results/R244-appendix-generalized-resolvent-unit-classes-and-vacuum-word-domains.md)给任意Li=MiUi+Fi的实际预解Ri满足Bézout恒等式及Mi=Ri⁻¹Di最大商；共同R=∏Ri的代数主理想、实际值域与Γ_R不随全部允许选择改变。真见证迫Γ_R距真空≥√Trρ，虽各单图投影稠密。1∈RH等价某个排列全部至多2^r个无重复自然子词在1上有定义，亦等价所有排列；rank2还原两交叉域。**无广义预解分支或共同高阶域缺口尚未排除，调参数不能改变它。**

[秩二有界链](results/R244-appendix-rank-two-koszul-defect-and-double-common-graph-gap.md)的Q有J²=−I、JT=T*J，非零Q无限维且无循环向量；真rank2迫Γ_R⊊Γ_min⊊Γ_max两商∞，Ri_Q=0、Di_Q单位。[全部中间比例图](results/R244-appendix-resolvent-minimal-cores-and-intermediate-ratio-spectra.md)：Pg=1本身即给P⁻¹=X_g与真空图核心；任意N⊂E⊂K闭A²不变比例图，包括两端，均σ(T_E U+F)=C。Pg=1仍不保强主理想单位，未排真实正矩缺口。

**交叉分母的准确正化。** [完整链证明](results/R244-appendix-cross-denominator-positive-quotient-and-equivalent-metric.md)对真rank2及任意允许广义预解给Q′=Q(R1D2,R2D1)，x=(Cf1,Cf2)本身为调和向量，φ(F)=〈π_Q′(F)x,x〉。L=P_Q′diag(D1,D2)|Q有明确Bézout左逆；G=L*L有界正可逆且Gq=z_Q，原配对因此在等价内积中是正向量态。Q′≃Q(R1,R2)⊕Q(D1,D2)为有界拓扑直和，x在原分母支。交叉分母未必单射，不称比例图；G不必交换商作用，也不给原H正秩一密度、共同真空原像或Cf交叉域。

[R267逆族](results/R267-appendix-blaschke-block-strong-units-and-linear-degree-inverse-type.md)保逆线性下型κ=log(4/3)−1/4；前向族可无真空原像。[共同幂](results/R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)给非零P∈F_A=∩A^rA′和收缩强*单位，F_A同范数强*稠密、AF_A=F_A、与UHF零交；有限旗单射稠密。共同幂原像为闭词图核心，非PH自动入域；1∉RanP。指定配对仍需全Walsh列平方可和，专属S因子未付。

**固定非湮灭态的完整块边界。** [R230完整Gram](results/R230-appendix-arbitrary-contractive-block-gram-and-complete-source-obstruction.md)对同一非湮灭f及q_i=16^i排所有可逆收缩纯块的合格逆源，实际完整Gram比值指数log5/2，有限完整源组合亦排；负实真实粗源g∉H_√3保留。非块/无真空原像未覆盖。

**真密度完整矩与正证书。** [R230完整定理](results/R230-appendix-positive-density-moments-dual-certificates-and-localization-obstruction.md)给m_B=L_Bρ_B、Gram=||R*m_B||、LL*=[[2,2],[2,6]]^⊗n及全部列carry。真湮灭右残量≤λε_m(K_n+d_B)，纯列另付λκ_md_B；它依赖非正Tr_(B^c)(ρT_m)/h_m，不能免费写成K_B*m_B。有限块正性对偶inf{μ:μI−ΠΩ+Re(TX_u)≥0}严格可行；理想内R=TX_v收缩且||RΩ−Ω||≤a<1/2给μ=(1+a)/(2−a)、u=v/(2−a)，故可得正余量。

[统一定位障碍](notes/2026-11-13-first-tail-obstruction-to-uniform-full-moment-localization-normal-complex.md)对任意n物理位K_B给τ≥q²/[8√3(n+2q+1)^(3/2)]；最优统一正密度矩常数C_n≥5^(n/2)，故τC_n≥√q/144→∞。它排先范数截块再统一放大，不排全空间右因子或真湮灭密度专属消去，后二者继续开放。

R242窄图、R248不交换阻尼、R250稀疏图的限制保归档，未得撤阻尼/A+不变。

**点态实见证与准确商实结构。** [R228完整附录](results/R228-appendix-pointwise-realification-reflection-pairing-and-weighted-quotient-real-structure.md)用J0实际共轭：J0平均保真湮灭但一般改变φ，双重平均仅与J0平均同φ；反射偶/奇实谱向量两两合并，实密度精确降至max(rankP+ρP+,rankP−ρP−)。最小实支撑至少与一个奇偶空间零交。实Mi本身只Krein对称，已有广义预解才付全伴随域；复参数的rank2商须Θ_Q=P_Qdiag(Wi)J0，Wi barWi=I。Ri真实时无权iJJ0才自伴酉，正负指数均无限；均不提供共同图核心/原空间秩一。

**实化与降秩须分开。** [R228/229范围订正](notes/2026-11-13-r228-r229-c-realification-scope-correction.md)：(ρ+CρC)/2在整个A′保同一正泛函，但可增秩；两两配对不保迭代到秩一。R229及9维实幂零例只排一般正秩一表示，不排C实化且非本题真见证。未知子商C不变、普通TρT*保湮灭不可假定。R240固定非湮灭态排通用first配对，专属/两端可变仍开。

R210–211奇异正态/Cantor族不具Haar正常性；固定正则端、Fock及增生平滑等旧障碍保归档，不代表真实正常矩。

[R253相位消元](results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)给I⊗Q_m∈S Acal及真见证必要q_m↓0。[复指数/完整Gram](results/R230-appendix-complex-exponential-tail-right-filters-and-full-gram.md)付全部|z|≤q^6、交叉参数/有限Walsh列Gram及真实carry，并在原b/q^4预算内排共同次数相位N_B锥。

**全部预算内标量复多项式已排。** [Fourier完整证明](results/R230-appendix-scalar-fourier-extraction-and-arbitrary-polynomial-filters.md)在纯alg(D_m)构造连续等距相位群，无无限Haar酉假设；每个齐次项范数≤输出范数。统一k≥q的占据界可求和，整个D_m^q标量闭理想真空比≤Γ_q=O(q^(1/3)e^−cq^(2/3))，不怕任意系数相消。实际p(U_m)只需(q+deg p)log(q+deg p)=o(q^4)，含所有deg≤q³；自身输出反控全部系数，自动付相对carry，无额外条件数假设。指数复测度混合在Δ_m^*TV/||Q_mG||→0时同样排除，归一化输出且TV≤exp(O(q³))足。不同坐标相位、超出实际预算的标量函数和真密度专属一般右因子仍开；上述不是完整q_m上界。全标量纯混合已闭，不再只停在先前必要相消成本。

[R253域附录](results/R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md)：真实图carry已付，D∞不含RanS；有限first预解积非S有界右倍数，专属配对仍开。

**已排除的通用正则化。** R230/R261规范正积的累计ℓ²、完整逆e^{o√q}及共同子半次数域非像，旧Cayley方向增益、R253全A^r有界除S失败和R263同一H_(1/(60e²))向量不在两RanS，均保于[本次完整归档](notes/2026-11-13-handoff-open-before-residual-flags-1cf8.md)及results原稿。像含该小指数域的有界分母不能除S；这些结论不排真见证专属配对。

[R237相对密度](results/R237-appendix-asymptotically-contractive-principal-ideal-approximation.md)：固定Q∈Acal的QAcal同范数强*逼近QA′；q_m可搜尾A′，不含非UHF左因子/无界右因子。一般S分母仍开。

## 当前接口二：实际边界的除法饱和

固定两个实际边界T_N/T_Y，M=kerT、N=closure BM、D=M⊖N。R187/200已给各有限稳定像及M∩RanB^r⊂N，有限孔核仅真空；真正问题是**无权核内稠密与N=M**，不将环境有限孔稠密当核内核心。

**旧接口。** R234模N已闭；R238原J_q成本不代R239模N成本。环境Γ坏见证在M⊥、横向T*M非BM原像；真幂界保真输入、头链与未知尾。旧预算见[归档](notes/2026-11-13-handoff-open-before-exact-boundary-gram-0c.md)。

**全整数窗口和真正最小Gram。** [R239全q](results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原进位，低投影e−74d⁴/真实lift e−75d⁴；d≈log^(1/3)q、K*=3(16/770)^(1/3)。c>K*权核入N，真D尾常数K*/2，权阶先属R271。窗口ell=d+m的Σ1/[ell(1+λ²)]发散足N；真D倒能量≤8τ_Q²/||w||⁴。λ²=O(q log^(2/3)q loglogq)足但未得。

[准确Gram](results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)为G=D0P_kerS D0*，严格正；实际r=Avq自动D^d，λ²=〈G⁻¹r,r〉。Schur补不可省；窄带正/倒能量仍容慢尾。逐头单块残量/旧d核阶及Tr(ApKp)非零保原范围。

**局部坏方向与原始块。** [局部最优](results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)给全低输出logΛ_q=Θ(log^(4/3)q)，无限高尾仍保；[原始块消去](results/R239-appendix-unweighted-primitive-removal-high-rank-blocks-and-full-projection-obstruction.md)给同一坏v的||P_Mv||→0。相容真空jets使受控q孔原始P的真残量小修复趋零；可取||P||→1、log rank=(2log2−o1)q。完整固定前缀原始投影仍唯一且log||P_full||≥(4log2−o1)q，不能用它作受控全覆盖。

**移动窗与双宽能量。** [完整定理](results/R239-appendix-moving-primitive-windows-and-double-width-repair.md)把原始块移k≤d并保真实自由坐标；B=A+D_free相容展开给双宽原始分量小修复，λ̃与补块差→0。新2d窗的lift、ell̃=2d+m全整数覆盖≤2及倒数准则独立重核；所需λ̃增长未得，旧d链旗不直接搬到2d。

**完整首个三维块分解。** [完整证明](results/R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)用相邻P_i及Q_i=I−P_i，得T_i=P_<iQ_i、T∞=ΠP_i和I=ΣT_i+T∞。首次离开正交展开只付Σ角度²；分析/合成A,B=1+O(m^−1/2)对全部分支一致。明确在RanT_i中最小化后B⁻²λ_h²≤Σμ_i²≤A²λ_h²，适用各自定义的d/2d/更宽窗。三维原正交链权α=ρs、β=s及真carry方程已付；T_iw不继承w⊥N。

**非真空低孔前缀与增长末段。** [精确Fock塔](results/R239-appendix-low-hole-fock-tower-and-nonvacuum-primitive-prefix-removal.md)用R_p=D_p*(D_pD_p*)⁻¹构造V_p，准确D_pV_p=V_(p−1)a_p，Gram递推给全层误差Δ≤ε[32(P+1)]^P，不把单层coercivity充当相容控制。s=floor(c logq/loglogq)、0<c<1，J=m+2(q−s)、P=s+d−1时Δ≤q^{c−1+o1}→0。固定前q−s个原始配对后余尾允许s孔；按出生层重建真核，在原宽d内修复P_(q−s)r，范数≤(1+o1)τ_q+e−71d⁴||w||。全部真实未来层/初值误差及Γ_d≤e^d⁴已付。一次完整分析界给μ∞²+Σ_(i>q−s)μ_i²→0，无√s；原λ_h与补块最小值之差趋零。早期三维支总能量和真最优通量仍开。

**原完整链与固定头速率。** [R239闭链/Riccati](results/R239-appendix-closed-repair-chain-riccati-and-terminal-leakage.md)付固定窗闭像/最优链/准确Gram及加宽极限。[R271统一相对率](results/R271-appendix-fixed-head-condition-and-uniform-window-convergence.md)用真实零源核的总级数分块及G=P_ZS*S|Z的带宽d−1，付Chebyshev有限传播：λ_d≤κλ∞，λ_[d+n(d−1)]²−λ∞²≤4(κ²−1)((κ−1)/(κ+1))^(2n)λ∞²，对所有q/源统一；实际最优链平方距离准确等于能量差，Gram同样相对夹住。κ是原头相似条件数，m增长时须支付κ_m及宽度；不能直接塞入旧真实lift，也不降低无限窗本身的坏能量。

[R271平方局部型](results/R271-appendix-square-head-smith-types-and-old-head-single-block-correction.md)给旧跨头Smith(2d−1,2d+1)、新4d，排稠密像D交织。固定混合核有限孔/正指数核心不传原核；上角残量可用旧d头修复，最多增2d孔但成本仍依Q。

[R271残量旗](results/R271-appendix-orthogonal-residual-flags-and-exact-source-gram.md)准确给R=⊕e_i kerD^(d−i−1)及全部链i≤d−t/kerD^(d−i)，Gflag为完整Schur补。[联合旗能量](results/R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)付同时右逆C≤e^d⁴、Gflag≥e⁻²d⁴、最优||y||≤Cλ/||z||≤C²λ，全部进位及删除核投影误差≤e⁻⁷⁰d⁴||w||λ。真缺陷迫Σ〈H_tw_(q+t),P_kerD^(t−1)z_t〉≈||v||²+λ²；原H_t只跨≥2头格但含1/4，不能称小进位。剩余为这条真实最优低核通量，无权N=M仍开。

[R271准确插值](results/R271-appendix-exact-stable-range-interpolation-and-norm-defect.md)给Π(Nexp)=ΠN=ΠM=V及有界线性右逆；原像范数按真实修复能量计。插值Gram差ΠP_W在W≠0时范数趋1；没有固定w的有界原像子列，不能推N=M。

[有限尾塔直接推论](notes/2026-11-13-finite-tail-tower-corollary-for-exact-residual-flags-boundary-resume.md)把底层下延到q−d+1，kerD^h恰为出生层s>p−h坐标；联合旗限制仍是有限矩阵列限制张量恒等，故S_flag/伴随像闭，原对偶inf取得且固定m,q有界依赖源。原始P及I−P保实际残量旗和全部可行链旗。此为R239旧有限塔法的直接推论，不是新的统一能量界。

## 当前接口三：一般系数行与多个模式

[R176共同谱](results/R176-appendix-bounded-part-spectral-intersection-and-common-exceptional-root.md)给有界不变部分谱相交/连通、所有有限谱部分共用r_u；全部倾斜/点态幂坏值至多一个，须q(r_u)=q(r_u−2α)。[实结构附录](results/R176-appendix-real-structure-affine-lines-and-odd-power-cyclicity.md)用逐点J给r_bar(u)=bar(r_u)，故任意实u、任意复权的全部(u^(2k+1)−λ)^m循环，无尾率条件；偶次仅留λ=α^(2k)。任意q|R单射也全λ闭合，含p(u)+iu−λ；无实根q的零位移全部幂闭合。ℓ1复误差只迫r在仿射实线，实际首位未必沿线；共同有限谱部分存在才有跨行加性。剩余实碰撞核未排，亦未构造有限谱部分。

[R147慢辅助切片](results/R147-appendix-bounded-slow-auxiliary-slices-and-polynomial-cyclicity.md)付任意ℓ²主/权、有限ℓ¹辅助的最高字符单位与真实差商；坏值须两个首位切片碰撞。[实辅助推论](results/R147-appendix-real-slices-odd-minus-positive-auxiliary-and-all-shifts.md)把碰撞根限实：实u、ε=sign首系数，实ℓ¹居中v与正定实R(0)=0，全部[εu^(2k+1)−R(v)−λ]^m e^w循环，任意支持次序/复权，无尾率预算；含全部u³−v²（首系数正）。复一次辅助c/α不在实射线(−∞,−α^(2k)]也全λ闭合。u³+v²的真实碰撞、最高字符零及双无界仍保。

**既有单模式。** [R236](results/R236-appendix-all-multiplicities-of-canonical-weighted-polynomials.md)的规范、临界弱ℓ¹、σ>1幂尾及α≤1指数子序列类均已闭，全部真实域/重数证明保留；R268给更广准则。

**更多排序行。** [R268](results/R268-entropy-budget-weak-l1-bandwidth-and-all-multiplicity-cyclicity.md)沿N满足sup_(k≥N)kρ_k≤DNρ_N、Σ_(k≤N)log(ρ_k/ρ_N)=O(N²)、logρ_N⁻¹=O(N^1.5)，则全部q(u)e^w循环。实际成本E_N+log^(4/3)ρ_N⁻¹+N²及jets/ad域已付；未满足准则的little行、1<α≤3剩余带仍开。

[R269](results/R269-analytic-a-coefficient-bell-polynomials-and-finite-head-multimode-cyclicity.md)给熵主行解析A首一/有限头点乘及ℓ¹主行有限头P；[R270A](results/R270-appendix-maximal-root-multiplicity-and-same-order-nonresonance.md)按最大根重数μ许c=O(|a|^max(2,μ))，最高重根保复比例非共振，小o无需速率。

[R270二阶消去](results/R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md)与[全阶F_p](results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md)保全部非零有限共振组合循环；底座归R152/183，新增只在§§9–10，单支撑真零例保留。

[非首一附录](results/R270-appendix-arbitrary-fast-leading-coefficients-maximal-closure-and-cyclicity.md)归R152/183，最大闭包不称自然域闭；[审计](notes/2026-11-13-r184-r186-scope-audit-and-finite-word-subquotient-corollaries-kernel.md)扣除R184/186旧联合域。

[R270快辅助](results/R270-appendix-fast-auxiliary-modes-and-resonant-polynomial-modules.md)付任意ℓ²主/权与快辅助Σh_kF_k及全部mixed域；p≤1去主行ℓ1。普通慢Bell/一般慢辅助未全闭。

[R236零输出分类](results/R236-appendix-resonant-polynomial-zero-output-and-leading-order.md)：a∈ℓ¹、s=a*+Σa、μ=mult_s q、L=支撑数，T_q=Σq^(r)(s)e_r(a_j(R_j−I))为零⇔L<μ；非零首阶为最早μ个位的2^j之和，μ=0为单位。无限支撑循环及二次关闭归R270C。

**全阶可和偏离与字符互素。** [R236字符定理](results/R236-appendix-real-dyadic-factor-character-coprimality-and-all-order-deviations.md)对非零主行、任意a,b∈ℓ²/c∈ℓ¹及F_q+v_c−λ给：早偏离处理全λ；否则α=a_ja、δ=c_ja，gcd(q−λ,αq'+δ)=1足循环，至多p−1候选。实际dyadic A幂、核内字符单位和C/Fourier均付，不除G_n本体。p≥2且j_c≤j_a的F_p+v_c已全闭；二次唯一候选λ*=(δ/2α)²确有单位置零输出例。一般late-c的λ0不能由这条字符判据排除。

**全阶双池与不规则行。** [二位完整证明](results/R236-appendix-all-order-resonant-two-site-bezout-and-derivation-budgets.md)：两池各N位、min位≥μN、max|a|≤C/√N、log跨det⁻¹=O(N^1.5)，给全部固定q/λ的(F_q+v_c−λ)e^w循环。实际ΔG_n无平方零一次项，4pr jets、绝对系数/两次r!平均及左右A四次成本全部已付。

[自动排序池](results/R236-appendix-automatic-separated-pools-and-two-power-envelopes.md)覆盖最终κ>1双侧比较、c∈ℓ1及全局logρ_n⁻¹=O(n^1.5)，允许零主位另有无限ℓ1辅助；两侧幂主行还许κ_−/κ_+不同夹界。另[指数种子二分](results/R236-appendix-nonsummable-main-dichotomy-and-all-order-sylvester-inverses.md)在κ>2全尾比较与liminf log⁺ρ_n⁻¹/n<∞下闭全部q/λ，含所有ℓ²\ℓ¹。有限例外任意但主零位须最终c=0；首次降幅后双池或真辅助小尾，乘积逆一次Cauchy给Γ_Y=O(N²)。两套范围不互换。

**双行非线性共振与平滑纤维。** [完整新定理](results/R236-appendix-two-row-resonant-smooth-fibers-and-sylvester-dichotomy.md)沿上述指数种子/最终比较，对F(U,V)=Σf_k(V)U^k、主次数p≥1且f_p(0)≠0，若F(μ,0)=λ每个根均(F_U(μ,0),F_V(μ,0))≠(0,0)，则准确双行共振(ℱ_F−λ)e^w循环。全部mixed G_rs真实二阶消去，最高系数含纯V修正；分根的偏导单位/(p,p)Sylvester结果式及总次数d的4dr jets已付。未排除的双临界值至多p−1个，不断言它们真有核。不可约F=U³+(1+U)V+V²的集合为空，故全λ闭。

同稿精确扩κ>1，只需某固定0<t<κ满足Σ|a|^t<∞；真实尾付ρ_tail^{κ−t}S_t，线性F=q(U)+V亦得全部q/λ。仅有ℓ²不能免费覆盖κ≤2。全部符号保混合/纯辅助Bell修正，未变成普通点态F(u,v)。扣除既有锚/快类后，可和极快、无比较辅助、双临界纤维及独立慢多辅助仍须处理。

**其他实际预算保独立范围。** [固定盘逆](results/R236-appendix-fixed-disk-kernel-inverses-and-sparse-linear-deviations.md)对无限S上|a/c|≤K、S辅助L_N=O(N^1.5)有效，S外任意主/辅助；[辅助尺度共同圆](results/R236-appendix-auxiliary-scale-joint-resolvent-and-independent-tail-gaps.md)取δ_N=c_N*、r_N=εNδ_N²，双删除及一次联合Cauchy给L_N=O(N^1.5)、Γ_Y(r_N)=O(N²)充分。含任意主行配辅助双侧α≤1伸缩指数，或Σ_(n>N)c_n*=o(Nδ_N²)、L_N=O(N)长平台；明确正相位例Y∉G。旧[主尺度共同圆](results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)/[子支撑](results/R236-appendix-supported-deviation-arbitrary-background-and-empty-spectrum-scope.md)也保各自假设，不互换排序/半径。

**旧空谱范围。** [审计](notes/2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)按R134/138/155：非ℓ1且可和相位缺陷first已空谱，有界A′扰动及首一自然多项式有真有界逆并保持未知限制；任意复ℓ²权/ℓ¹辅助早已覆盖。居中ℓ¹和全C慢分支仍需证，不能免费取二次分歧根。

[R257/258](results/R258-entire-selfadjoint-kernel-transport-and-actual-tail-mobius-domains.md)整自伴运输不传原M点乘域/不变格；R224公共像/尾商障碍保留。

[R259](results/R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)闭同幂尾p>1/2；[R260](results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)闭排序limsup nρ_n>0的任意复行及物理重排，允许全部复first指数和有限联合解析Bell芽。其完整域导子代数无maxF成本；剩余解析分支须nρ_n→0且排序复和→Φ(0)，一般行重根另证。

[R264–266](results/R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md)已闭α≤3/2的解析Bell/简单根及α≤1全重数；R268严格扩展后，规则1<α≤3/2的普通点态全部重数仍开。

**高阶导子及剩余短和。** [纯提升障碍](results/R236-appendix-high-degree-raising-band-obstruction-and-range-projections.md)给r≫√Q的有界提升弱趋0；[全域双导子](results/R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)付[ad_T^(2r)U_N](C_Q^r)†强趋I、r=ηQ<Q/2、伪逆≤e^(Q/2)及全部carry。它不是单个导子像；核配对完整Leibniz在1<α<3尚余末O(N^((1+α)/4))项。[两位校准](notes/2026-11-13-two-bit-pseudoinverse-calibration-central-next.md)排共同尺度粗吸收；须核内抵消或适配降阶，α=3不自动短段。

**旧快类。** [R236核查](results/R236-appendix-existing-fast-classes-for-supercubic-sorted-rows.md)据R175：排序ρ_k≤Be^(−βk^α)、α>3已给非零q(u)e^w循环及标准主理想/普遍表示，无需下界。α=3时首阶r的β>80r⁴/3给限制稠密/强主理想，β>400r⁴给标准范数理想；均严格充分。单个四次幂界不等于G。剩余1<α≤3须扣这些旧例。

[R270第六附录](results/R270-appendix-disjoint-slow-point-polynomial-products-and-head-masks.md)：物理不交慢模式的已知点态循环因子可相乘，故∏(uν−λν)^mν e^w循环。mixed词域/Bell已付，共享有限头仅保单atom；同模不同根、atoms之和不能这样相乘。

## 1. 一般向量的矩分离与有限二阶以上输入

R101仅有限Walsh次数两端；任意非零L²循环性、一般二阶核、gauge差在未知核上的像、双独立慢模式仍开。R130/131/143的闭域与跨核配对不许取消A^h后补域；R29/44/51和R163/165平滑/Lp/Orlicz障碍保留，有限柱近交换不是真Nj交织。

## 2. 不变限制中的一阶闭乘子值域

R125/128/140保真实闭限制、R(t)与图核心。任意复ℓ² first在未知M上dense仍开，准确等价closure S(t)M=M；全H稠密、C保核及四正分量不替代。正行/可和相位缺陷非ℓ1、G及已付四次尾型各保原范围；一般慢S(t)不自动快。C对称Volterra反例排抽象法，R176共同谱仍允许单点拟幂零部分。

## 3. 任意有界有限 chaos、范数代数及完整交换子

非零Acal/A′元素的一般排核、零锚有界二阶及无限低位行消去仍开。R32无零因子仅代数内部；R88纯/真实对应不保乘法或核；R92固定有限chaos的连续代表及非零字符可逆范围不扩。R143首位图须TBT=α₀、真实域及分母有限放大稠密，最大商图不独自排核；R124余数零字符不保可再除A，不能把首阶r>1免费降到1。

R185/188已给非标准主理想J无限余维、不含A幂、与指定G/bounded K零交；S在原H仍单射稠密，故不直接给原空间不变子空间。进一步理想分类仍开；R140强主理想与范数理想、R121根式非闭及R112/119归一化幂障碍均保。[R256](results/R256-bounded-weighted-composition-commutants-of-the-radial-haar-model.md)分类nonsingular底映射的有界加权复合交换子只有cA^n（n普通非负整数），只需η_j→0；一般非复合交换子未闭。其余旧范围与外部Thomas/Peters/GT条件见[本次前完整原文](notes/2026-11-13-handoff-open-before-cross-denominator-positive-quotient-1cf.md)。

## 4. 相对乘积、多项 cocycle 与混合解析芽

[R189一个空谱锚](results/R189-appendix-one-empty-anchor-two-additive-direction-kernel-elimination.md)：X为可和相位缺陷非ℓ1first、Y为任意第二first/有界加性模式，允许Acal快gauge增量扰动；所有实际非零G[X,Y]最大实现单射稠密。只消Y后把E(X)用L=X⁻¹变为旧R189普遍dense分子ρ(L)，真实深域跨核排除单核；有限多模式总类秩≤2且含实际空谱组合也得。全阶双共振q及正慢u/交替慢v的[v²−u³+(2−6u)s₂−8s₃−λ]e^w已循环；普通v²−u³、三独立类/双全C方向及新多项式普遍限制范围仍未付。

R127已闭相对ℓ¹两乘积；复杂相位相对ℓ²、三以上cocycle、非解析闭包/一般有界商仍开。R129/135单轴、R146/148单慢加快、R152有界加性及R153快分式各保原范围，超越分支未普遍限制dense。

R160慢二阶Bell不自动属G；R77/79/82临界中间参数及R83芽/轴谱仍开。R162纯虚倾斜不保乘法，指数权点态循环不扩任意H向量。

仍可寻找固定单射R∈A′使所有非例外ζ有B(RM,UζM)=0：此时closureRM非零且含于M即可用R122，无须先dense。当前辅助因子依ζ变化，可数全H稠密像之交不自动与未知M非零相交。

## 5. 一般 ISP 的独立路线与不能省略的障碍

R5缺非零拟幂零秩一扰动及任意T归约；R7双锚未普遍实现，R2/R17/R18排内部紧修正。R4/R6观察拟仿射失败，Rota须真中间空间，R8双生成提升非充分归约。R114/R164/R165排既有紧化/一致平方可积路线，实际UHF交织Calkin忠实且角谱等于本质谱。

R105/R107核对的PPP1995谱圆、MM1974、AT/AM紧化条件不满足；JKP2019完整条件及Tucci迹转Haar未付。[family293审计](notes/2026-11-13-family293-hyperinvariant-scope-and-backward-normalization-audit.md)仅超不变结论，其纤维有普通真尾空间且交换子非交换；Domar权不同，不能借R88或反向归一改称普通反例。未重编Lean。原全部条件保[发布前全文](notes/2026-11-13-handoff-open-before-exact-low-window-interpolation-1cf8.md)。

## 不能互换的极限

全部混合自然词域不保普通系数截断；可数first核心及固定正则子在子商单射稠密，不使原词普遍dense。非零有界交织不能把全像送入全部first域；R204重选行不代固定慢行或边界运输。实际域、carry、非零锚仍须支付。

[R239首位图](results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)/[横向压缩](results/R239-appendix-coercive-adjoint-and-positive-mixed-compression.md)保C²=η₀N₁|L、||C||<1/√12，真缺陷需C*Gx=0及C*x=−η₀(N₁|L)*Cx。核上T*≥7/8、Re(P_MBT*|M)≥5α₀/6，给M⊥内横向同构而非BM原像；各位压缩约束仍未排缺陷。详式和度量字典在原稿及本轮归档。
