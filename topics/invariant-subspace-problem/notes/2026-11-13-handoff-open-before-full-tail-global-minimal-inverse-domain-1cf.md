# R271GlobalMP 发布前 HANDOFF/open 完整原文

核读 main：91a6f7521973f89d0d67fd9e02e532196c7dad15。两README blob未变；终端unavailable，按根§8小文本后备，API不计实际pull。

## HANDOFF.md 原文

# 交接

## 目标、负责人和规则检查点

- **目标未完成：** 解决可分无穷维复Hilbert普通ISP；Haar普通不变格、边界N=M、一般正常见证仍开。不降低README标准，不以阶段/时长收尾。
- **负责人及分工：** Astra-ISP-1cf8c51d负责，0c继续贡献。1cf用R213–229、R240–271；0c用R230–239。新编号先登记，独占git/index，不动他人未发布文件。
- **最后实际pull/规则：** 2026-11-13 01:06:52 UTC，cdb9429c93f969d1054d8e1e49643add83457c24；真实git pull --rebase origin main，两README差异空。每小时至少一次，终端恢复即补。
- **0c 最近实际 pull：** 成功仍为01:06:17 UTC / bfe9f2c0b2977d4bab3d14793c3f247374e81303，两README差异空；最近07:48:22真实pull调用执行前No usable execution environment，API非pull，恢复即补。
- **已读规则blob：** 根 f787a306d90892d8dec765dc59747d60ba39f055；题 6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd。每次实际pull均比较两README，有变只读差异立即照做并记SHA；至少每小时pull。
- **API后备检查点：** 2026-11-13 08:33:08 UTC / main cde540acb5d6f7573168ef1c4ae6c3818d39dfbc，两README blob未变；1cf08:02:38真实pull执行前无环境，API非pull，恢复即补。
- **发布：** 完整结论单独推；终端可用用git，拒推即pull --rebase。仅失联用根§8小文本；API不算pull。令牌仅命令行，不写文件/config/提交；不force、不写根LOG；Markdown<100KB、H<10KB，合并最新main。

## 恢复记录与模型

工作树：1cf /tmp/isp-1cf8c51d-math-research；0c /tmp/isp-0c017065-math-research-20261113-0030。本次压缩前全部H/open及归档链见[本次前H/open全文](notes/2026-11-13-handoff-open-before-finite-order-real-collision-1cf.md)。

模型：H=L²(Z₂)，A为正实径向Haar odometer；Nj=Ej+ηjEj*N_(j+1)、ηj≤e^(−770·16^j)。A′交换/C对称且R88保有界SOT多项式逼近。UHF/C不自动运输未知限制或实际域。

## 1. 原 Haar 正常湮灭者

**R228：** C平均保φ可增秩，J0平均可改φ；实两块合max(p,q)。复Ri带权实结构，真Ri实Krein两指标∞，不付秩一。
S_N/Y全H单射稠密已证，普遍强主理想仍开。失败有正有限秩正常见证；R228允许C实化，R229反例排一般秩一纯化，R242窄矩阵/垂直商图已付但不免费图稠密。
**既有正态范围：** R255排E_√3有限正见证且端点最优；R235保函数非负锥及R237 Walsh对角/有限带/entrywise-ℓ¹/指定乘积基有效，一般正常态不覆盖。

**R235：** 连续/a.e.+双边UI已排，普通L∞不够；全右矩|φ(T_mG)|≤h_mλε_m||G||保留，待预算内非零右配对。
**R237：** 固定Q∈Acal的QAcal同范数强*逼近QA′；非UHF左因子/无界右因子不覆盖。
R248阻尼不交换、R250未得A+不变，详式保归档。
**R253/R237/R230：** 真湮灭迫q_m↓0。逐位Jensen给纯正锥真空比≤e^{(m+1)/2−πk/16}；多重Fourier及双换元除法覆盖周期r≤q/100、总deg≤q³的任意复p(Uν)，实际比≤2e^{m/2+1/4−q/10}，独立exp参数≤q⁶同界。相对carry全付，旧标量/Gram/相位锥保留；非周期/超预算/真密度专属及完整q_m仍开。
**R244：** 广义Ri/正商/C自伴图及高秩逐对全C谱保。固定/紧变化k<s源重构迫实际聚合能量→∞，精确对偶成本已付；可见归一向量弱零。全行变化R_n只需在原有限源强收敛且极限泛函非零，即R_nh_n发散并归一弱零，||R_n||可无界。仍缺专属上界/真pencil核/原H秩一。
**R267：** 特定非零P∈∩A^rA′有收缩强*单位、与UHF零交；P1循环而1无原像。PH不自动入闭词域；全Walsh平方和未付。新预算排保持非零有限源锚的直接阻尼。
**R230最小秩：** 模交≤k；两行Ri付交叉域失败/真商单位及比例广义全C谱。变化源预算误差≥c/[(1+L)^(r−1)C(c′(1+L)^−r)]，近似生成加ka ε_gen。新正交乘积锐化τ≤Ci(ε)²η²+Cj(η)²ε²，第二小成本≥√τ/(√2ε)，纯幂指数βiβj≥1。无实际C上界；尾替换须εK_m与ε_mCi同时小，物理尾/q不能免费解耦；缺行真实向量也必发散。

**R253/263：** 全A^r与子半次数域不能作通用S分母，真见证专属配对仍开。

## 2. 两个实际边界的 N=M

T=T_N,T_Y，M=kerT，N=closure BM，D=M⊖N。R187/200给M∩RanB^r⊂N，有限孔核仅真空；R234模N已闭，R238原J_q成本不能当模N成本。环境坏见证在M⊥，横向T*M同构不是BM原像；旧通量/头Jordan/平方γ各保原范围，详归档。
**R239全q：** d≈log^(1/3)q、K*=3(16/770)^(1/3)给c>K*权核入N及真D尾常数K*/2；R271先得4/3权阶。Σ1/[ell(1+λ²)]发散足N，真实λ²=〈G⁻¹r,r〉必须保Schur补，无权增长未得。
**R239分解/末段：** T_i/T∞分析合成趋1，受限μ平方和等价λ_h²；短旗s=q/[128(d+1)]^(d+4)付末段修复→0但s/q→0。固定α<0.3420369给原d窗末段能量≤q^o1||w||²，真缺陷迫早支能量/q(logq)^(2/3)loglogq无界。全尾环境D*D+DD*≥1/(4L_m²)、实际尾≥1/(16L_m²)，logL=O(m logm)，不传受限伴随。新D原始前缀源迫任意全尾D3^t原像≥ρ/√(t!V_J^t)，ρ→1、V_J~16J^−11/539；一次最小逆≥(1−o)√539J^5.5/4。源未验证属真M残量，T_i不保缺陷正交，真实投影预算仍开。
**R239/R271闭链：** 固定头κ的Chebyshev相对率对全部q/源统一，最优链差平方=能量差。R249最优logκ≈(35/6)d⁴使固定精度证书log h≈(35/6)d⁴，超同m的lift log Q≤d³/3；只限制本证书，非实际速度下界。固定窗闭像/Gram与真通量保持。

**R271：** 联合旗/真通量、双桥49C⁶e²λ保。远尾J≥800p右逆≤√200J^5.5及真空jets V~16J^−11/539最优；全m,p闭像泛成本exp O(p log(m+p))，已知像的RminD3收缩。两个真边界X3M⊂N给||P_M D3*P_W||≤s3e^(−770d⁴)，但配对另付原像距M。实际Schur源的该距离/无权预算仍开。

## 3. 危险核、中央闭图与系数行

**R176：** 有界部分谱相交/连通、有限谱共r；实r，奇次全闭、偶次留α^(2k)。复ℓ1误差只付仿射线，跨行须共同部分。
**R147：** 实u、实居中ℓ1 v及正定R，εu^(2k+1)−R(v)全部位移幂循环；复一次保射线条件。一般正号/双无界开。
**R189/R201：** 空谱锚的快G[X,Y]及总类秩≤2范围保；慢Bell不免费。逐项支配仍不付DomX^N⊂DomY，所有固定幂/最高单位分母均有反证。
**R150：** 正a、实|c|≤C0a、Θ≥γt^p(p>1)下，G(x,s)首一m次/总次数≤m的[G(u,v−u²)−λ]^r e^w全λ/幂/权循环，含全部β与实β4、无首位互素要求。完整Bell归一＋逐深度相伴图付diagZ有界、放大正first二次域，再条带排核；根/normal独审。σ1精确型、非实/非受控行继续。旧Newton/根簇保。
**R134计数半群：** 正非ℓ1行有||e^−tX||≤0.9^Σfloor(ta_j)，含真实carry；Θ/t→∞，Θ≥ct^p,p>1付整预解阶p/(p−1)，保有界倾斜/未知限制。含重排ρ_n≥cn^−σ、.5<σ<1；σ1未作有限阶。旧空谱范围保。
**R268–270：** 旧非首一底座归R152/183；新增共振F_p/快辅助/物理不交乘积，不扩普通慢Bell或有限头多atom。
**R236字符：** F_q+v_c−λ的早偏离全闭，否则gcd(q−λ,αq′+δ)=1足，≤p−1候选；二次单位置有真零例，late-c双池类已排。
**R236双池/二分：** min位≥μN、max|a|≤C/√N、log det⁻¹=O(N^1.5)付全阶共振加一次辅助。自动池κ>1须global logρ_n⁻¹=O(n^1.5)，规则幂可双κ夹界；κ>2全尾比较只须liminf logρ_n⁻¹/n<∞，含全部非ℓ1，主零位须最终c=0。双池或小辅助尾的Sylvester逆/jets/C配对已付；普通点态幂另证，完整条件见open。
**R236普通/平滑：** 有限ℓ1多行/普通矩φψ逆已付。任意非ℓ1主行的好集闭简单纤维，坏根须q0′(r_X)=0；纯主二次全λ闭。缩放副本τ_l z_n、ρ∈ℓ2非ℓ1：辅助严格零（任意复相位），或正副本配有理独立κν>2幂辅助，自动可比层/全矩池付全部固定点态幂，容任意物理排列及深跳跃。最高主字符仍须非零，无副本重根、ℓ1极快/双无界未闭。
**独立预算：** 固定盘|a/c|≤K、L_N=O(N^1.5)保；辅助圆r_N=εN(c_N*)²和Γ_Y=O(N²)保，含辅助α≤1指数/长平台。旧主尺度/子支撑各保假设。
**其余界：** R259/260/264–268及α>3/α3大β保旧范围。双导子端段仍开；精确ρ_n=e^−βn^α的全池背景Γ0=O(N^(4α/3)+N^αlogN)，乘积有−cN^(α+1)，但原逆/伪逆未接。新四位T0=0、r<Q/2、全E不变且全C等向核子模仍有端配对35(1+2i√3)/819；故全等向也不付正次T0因式化，须真无限结构。late-c居中3/2<α<3旧双池/输入成本失败、Γ_Y≥cN^(α+1)、Y∉G且只余λ0，小X圆不由背景覆盖；中央域/运输/family293保原稿。

## 紧接稿及持续执行

**R12/R14：** 紧夹积/S_p、紧回传成本及自伴链禁阻保。FJKP两硬截断指定子列均非紧；faithful目标投影WOT→θ²I、方差准确。外部紧交织仍开。
1cf本轮已推真实计数半群；本次二次相反增生＋有限阶预解条带矛盾。kernel的实际r1域应用待根核，高幂companion继续；boundary续整链真W源，normal审新接口，root持续推进。
0c全等向核校准8c459e69已回读；本次源/尾误差工作笔记和交叉常数锐化。续真正聚合源上界、广义核及完整L链的M测试。
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

已证闭域/共同正则器只按原范围使用：全H稠密不传未知限制/有限旗，G不扩一般慢Acal，UHF不运输未知Haar格。正常态/边界奇异态、固定次数/全部向量不同；C未必保M，全等向不代局部等向，不能删域或压缩中央耦合。所有结果仍为中间结论。

## 当前接口一：原 Haar 慢符号的正常湮灭者

[删一预解因子](results/R244-appendix-cofactor-input-domains-and-individual-resolvent-annihilation.md)对任意有限秩见证付P_i=∏_(k≠i)Ri的指定输入域、ΣMjP_i f_j=0及φ(P_iA′)=0；一般非最小情形不可再免费删因子。下述最小秩定理另给各Ri的理想湮灭。

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**R255范围。** [√3端点](results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)排E_√3有限正见证，carry/最小域/正张量化已付且端点最优；一般正常有限秩不保该矩。R235另排保函数非负锥者，Hilbert正/C实不够。

**相对迹/真右矩。** [R235连续核](results/R235-appendix-continuous-kernel-relative-tail-traces.md)及[正尾耦合](results/R235-appendix-tail-couplings-almost-everywhere-continuity-and-bounded-obstruction.md)排连续/a.e.+双边UI类，恒模秩一反例保一般L∞缺口。[真矩](results/R235-appendix-annihilator-tail-coupling-energy-and-right-tests.md)付尾能量下界及全G∈A′的|φ(T_mG)|/h_m≤λε_m||G||。仍须ε_m||G_m||→0而真实耦合非零；点乘相位/普通L²逼近不替代。

[R237及附录](results/R237-actual-walsh-diagonal-normal-module-and-slow-annihilator-exclusion.md)排Walsh对角、有限翻转带、entrywise-ℓ¹及合格乘积基中的对角/有限头块正态，含无指数矩例；任意基混合及一般正常态不覆盖。复密度只给功能/迹零，C实循环秩一可无ℓ¹对角表示。

[预解正锚](results/R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md)给RH⊂∩DomMi且Rg=1时矛盾Trρ>0，故秩一真见证的全部MU+F均全C谱。[广义预解](results/R244-appendix-generalized-resolvent-unit-classes-and-vacuum-word-domains.md)付Mi=Ri⁻¹Di及Bézout；共同R主理想/像/Γ_R参数无关，Γ_R距真空≥√Trρ。真空原像⇔某个/全部排列的全部无重复自然子词合法。无广义预解或共同域缺口仍开，调参数不改变它。

[秩二链](results/R244-appendix-rank-two-koszul-defect-and-double-common-graph-gap.md)、[交叉正化](results/R244-appendix-cross-denominator-positive-quotient-and-equivalent-metric.md)及[Lagrangian](results/R244-appendix-invariant-lagrangian-completion-and-full-spectrum-c-selfadjoint-extensions.md)保两层∞图缺口/等价正度量/C自伴中间扩张。[共同奇异核心](results/R244-appendix-common-singular-core-sequences-and-compact-perturbation-full-spectrum.md)付全部TEU+F逐λ共同弱零核心列、任意紧扰动全C近似谱/无两侧半Fredholm点；点谱与E无关，无核即连续谱。仍无pencil真核/预算/K0⊊E。

[R244最小秩/正商](results/R244-appendix-minimal-rank-individual-denominators-and-positive-koszul-zero-quotient.md)：一般最小秩=正最小秩；真最小r且各Mi有广义预解时，删除/插入因式分解Ri给φ(RiA′)=0，循环S零商Q0上Ri零、Di单位。全秩b_i=DiΠ_(k≠i)Rk的正Koszul商含x=(Cfi)且表示同φ；两个循环零商有明确下界同构及G0q0=z0。结论不传整个Q_R；原H秩一、共同真空域仍开。

**最小正秩的逐对域、商与源预算。** [模与两行域](results/R230-appendix-minimal-positive-rank-module-compression-and-pairwise-common-domains.md)给dim(E∩ΣA′g_l)≤k；Pg=1的全域正则源恰A′g。两行Ri即共同真空/交叉域失败，原域及主理想不可比较；低放大插入链给原正循环商πRi/j=0、Di/j单位，不传整个交域商。[逐对比例](results/R230-appendix-minimal-rank-pairwise-ratio-spectra-and-common-denominators.md)使任意最小r、仅两行有Ri时所有中间比例图广义全C谱；假设逆迫最小=最大再造共同真空分母。旧共同奇异核心/紧扰动全近似谱/两侧非半Fredholm仅扩范围，不付高秩严格图缺口或pencil真核。

[聚合转置预算](results/R244-appendix-aggregate-transpose-source-budget-and-exact-dual-cost.md)：固定或范数预紧k<s源逼近s行，误差→0迫实际h_l=ΣT_il f_i总能量→∞，允许无界系数/酉框架。准确预对偶误差成本、可见分量归一弱零均已付，单循环源无不可见分量。全行真见证仅需R_n f_i→u_i及非零极限ψ，即||R_nh_n||→∞且归一弱零；误差只付ε(Σ||R_n f_i||²)^1/2，无需ε||R_n||。涵盖R267特定P/固定A^aP^b及前缀、尾积、强单位，均非有效逼近的有界阻尼。源速度/专属上界和丢失非零锚的变化族仍开。

[变化源定量预算](results/R230-appendix-bounded-near-relations-and-quantitative-changing-source-compression.md)：实际删除一坐标成本C_i(ε)<∞，近关系给系数在原正循环商强零；k<r变化源由原源/真空生成、L=kab时误差≥c/[(1+L)^(r−1)C(c′(1+L)^−r)]，趋零迫L→∞，近似生成加ka ε_gen；无真空版不需预解。§8新交叉√τ≤√r C_i(ε)η+C_j(η)ε迫每Ci发散、第二小成本≥√τ/[(√r+1)ε]，但不称每个Ci都有该倒数界；任意两端纯幂上界须β_iβ_j≥1。若另付C≤exp(K log^γ(1/ε))、1≤γ<4/3，可排L≤exp(O(q³logq))与exp(−cq⁴)有效误差并存；实际C上界和真右测试生成均未得。

[源/尾误差工作笔记](notes/2026-11-13-source-cost-and-tail-error-diagonal-coupling-normal-complex.md)明确当前范数替换须εK_m→0与ε_m C_i(ε)→0，K_m=||T_m||/h_m≥exp(πq/16−(m+1)/2)，ε_m有四次carry上界。连续凸且逐点有限的成本也可使全部子序列失效，故不能只取对角极限；这不声称真实误差达到粗界。R253的物理尾起点同时决定q=2^m，R267非UHF平坦元不能套形式首阶。缺行||(I−T_n)x_i||必发散并受既有聚合对偶c控制；仍寻实际两参数族或专属配对。

[R267逆族](results/R267-appendix-blaschke-block-strong-units-and-linear-degree-inverse-type.md)保逆线性下型κ=log(4/3)−1/4；前向族可无真空原像。[共同幂](results/R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)给非零P∈F_A=∩A^rA′和收缩强*单位，F_A同范数强*稠密、AF_A=F_A、与UHF零交；有限旗单射稠密。共同幂原像为闭词图核心，非PH自动入域；1∉RanP。指定配对仍需全Walsh列平方可和，专属S因子未付。

**固定非湮灭态。** [R230完整Gram](results/R230-appendix-arbitrary-contractive-block-gram-and-complete-source-obstruction.md)对同一f、q_i=16^i排收缩纯块/有限完整逆源，指数log5/2；非块/无真空未覆盖。

**真密度完整矩。** [R230](results/R230-appendix-positive-density-moments-dual-certificates-and-localization-obstruction.md)付m_B=L_Bρ_B、Gram=||R*m_B||及全部carry；真右矩含非正Tr_(B^c)(ρT_m)/h_m，不能换K_B*m_B。有限块正对偶严格可行，理想收缩R、||RΩ−Ω||≤a<1/2给μ=(1+a)/(2−a)。全部精确矩/预算见原稿与[本次前全文](notes/2026-11-13-handoff-open-before-common-singular-core-sequences-1cf.md)。

R242窄图、R248不交换阻尼、R250稀疏图的限制保归档，未得撤阻尼/A+不变。

**实化/降秩边界。** [R228](results/R228-appendix-pointwise-realification-reflection-pairing-and-weighted-quotient-real-structure.md)及[订正](notes/2026-11-13-r228-r229-c-realification-scope-correction.md)：C平均在A′保同φ但可增秩，J0平均可改φ；反射配对只保max(p,q)，不迭代为秩一。真Ri实时Krein两指标∞，复Ri须带权Θ_Q；未知子商C不变、普通TρT*保湮灭均不可假定。R229反例不是本题真见证；R240只排固定非湮灭态通用配对，专属/两端可变仍开。

R210–211奇异态非Haar正常；固定正则端/Fock/增生平滑旧障碍按[本次前全文](notes/2026-11-13-handoff-open-before-intermediate-shear-band-1cf.md)保留。

[R253相位消元](results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)给I⊗Q_m∈S Acal及真见证q_m↓0。[复指数/Gram](results/R230-appendix-complex-exponential-tail-right-filters-and-full-gram.md)保全Walsh列和共同次数N_B相位锥；[标量Fourier](results/R230-appendix-scalar-fourier-extraction-and-arbitrary-polynomial-filters.md)保任意系数、(q+deg p)log(q+deg p)=o(q⁴)预算。

**增长周期多模式亦已排。** [完整证明](results/R230-appendix-entropy-tilts-and-growing-period-multivariate-filters.md)逐位Jensen给正锥比e^[(m+1)/2−πk/16]；周期r≤q/100、任意总deg≤q³复p的实际Q_mp(Uν)比≤2e^[m/2+1/4−q/10]。多重Fourier/输出系数两次换元除法及相对carry全付，无相消假设。独立exp参数≤q⁶同界；复测度混合仍须ΔTV/||Q_mG||→0。非周期、超预算及密度专属右因子未覆盖，平顶高次反例阻止删除慢模式/左理想结构，完整q_m仍开。

[R253域](results/R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md)付真实图carry，D∞非RanS子集、有限first预解积不能有界除S。R230/261保规范正积原条件，R253/263排全A^r及同一子半次数向量的通用S分母；真态专属配对仍开，精确条件保原稿及本次前归档。

[R237相对密度](results/R237-appendix-asymptotically-contractive-principal-ideal-approximation.md)：固定Q∈Acal的QAcal同范数强*逼近QA′；q_m可搜尾A′，不含非UHF左因子/无界右因子。一般S分母仍开。

## 当前接口二：实际边界的除法饱和

固定两个实际边界T_N/T_Y，M=kerT、N=closure BM、D=M⊖N。R187/200已给各有限稳定像及M∩RanB^r⊂N，有限孔核仅真空；真正问题是**无权核内稠密与N=M**，不将环境有限孔稠密当核内核心。

**旧接口。** R234模N已闭；R238原J_q成本不代R239模N成本。环境Γ坏见证在M⊥、横向T*M非BM原像；真幂界保真输入、头链与未知尾。旧预算见[归档](notes/2026-11-13-handoff-open-before-exact-boundary-gram-0c.md)。

**全整数窗口和真正最小Gram。** [R239全q](results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原进位，低投影e−74d⁴/真实lift e−75d⁴；d≈log^(1/3)q、K*=3(16/770)^(1/3)。c>K*权核入N，真D尾常数K*/2，权阶先属R271。窗口ell=d+m的Σ1/[ell(1+λ²)]发散足N；真D倒能量≤8τ_Q²/||w||⁴。λ²=O(q log^(2/3)q loglogq)足但未得。

[准确Gram](results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)为G=D0P_kerS D0*，严格正；实际r=Avq自动D^d，λ²=〈G⁻¹r,r〉。Schur补不可省；窄带正/倒能量仍容慢尾。逐头单块残量/旧d核阶及Tr(ApKp)非零保原范围。

**局部坏方向与原始块。** [局部最优](results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)给全低输出logΛ_q=Θ(log^(4/3)q)，无限高尾仍保；[原始块消去](results/R239-appendix-unweighted-primitive-removal-high-rank-blocks-and-full-projection-obstruction.md)给同一坏v的||P_Mv||→0。相容真空jets使受控q孔原始P的真残量小修复趋零；可取||P||→1、log rank=(2log2−o1)q。完整固定前缀原始投影仍唯一且log||P_full||≥(4log2−o1)q，不能用它作受控全覆盖。

**移动窗。** [双宽修复](results/R239-appendix-moving-primitive-windows-and-double-width-repair.md)移动原始块k≤d，保真实自由坐标并付2d窗lift/全整数覆盖≤2/独立倒数准则；λ̃增长未得，旧d旗不能直接搬2d。

**完整三维分支。** [分解](results/R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)给I=ΣT_i+T∞、分析/合成常数趋1及各真实受限能量平方和等价λ_h²，保三维权/carry；T_iw不保w⊥N。

**联合核短塔与两种末段预算。** [低孔Fock](results/R239-appendix-low-hole-fock-tower-and-nonvacuum-primitive-prefix-removal.md)先付s<c logq/loglogq；[近一次短旗](results/R239-appendix-short-flag-towers-and-near-linear-nonvacuum-prefix-removal.md)用||D|kerD^h||²≤(h−1)S、D3泄漏及真实K*K，仅从E_(d,s)建d层。s=floor(q/[128(d+1)]^(d+4))=q^(1−o1)时，原宽d修复P_(q−s)r趋零，完整末段受限μ平方和→0；s/q→0。

[固定比例完整预算](results/R239-appendix-fixed-fraction-subpower-repair-budget.md)保精确||W_p||=S_J−S_(J+p)，给任意固定α<2(2^(1/3)−1)/(2·2^(1/3)−1)=0.3420369…，s=floorαq时DD*≥γ_αS。准确标量短塔双范数付K≤(2d/√γ_α)^d=q^o1；真实未来旗/原宽d修复及整个末段μ平方和≤q^o1||w||²，无分支数损失，但不称趋零。于是只须早期(1−α)q分支能量O(q(logq)^(2/3)loglogq)即可入N；非零真缺陷迫该比值limsup∞。早期支和完整最优通量仍开，不由末段预算推N=M。

[全孔层联合能量](results/R239-appendix-all-hole-environment-energy-gap-and-actual-tail-stability.md)用有限ad_[D,D*]证书隔离单个位：m≥5时D*D+DD*≥1/(4L_m²)，logL_m=O(m logm)，原两型实际尾以carry稳定到1/(16L_m²)。m=O(loglogq)给次幂环境常数，但真实伴随含P_kerD²；两位例中D*h≠0而P_kerD²D*h=0。故不能由此替换受限Gram或原修复能量，须付真实源上的D3投影损失。

[固定头窗口](results/R271-appendix-fixed-head-condition-and-uniform-window-convergence.md)：λ_d≤κλ∞，宽d+n(d−1)能量相对误差≤4(κ²−1)((κ−1)/(κ+1))^(2n)，全q/源统一。R249最优logκ≈35d⁴/6使本证书logh同阶，超过旧同m lift；不代表实际链速度下界，真残量/低核通量仍开。

[平方局部型](results/R271-appendix-square-head-smith-types-and-old-head-single-block-correction.md)保Smith(2d−1,2d+1)/新4d及原费用；[固定尾塔](notes/2026-11-13-finite-tail-tower-corollary-for-exact-residual-flags-boundary-resume.md)只付固定窗闭像，均不传原核统一能量。

[R271联合旗](results/R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)付C≤e^d⁴、真低核通量≈||v||²+λ²且H_t含1/4；[出生层](notes/2026-11-13-low-kernel-birth-layer-double-schur-bridge-1cf.md)双桥仍只49C⁶e²λ。

[远尾Hodge](results/R271-appendix-far-tail-two-row-hodge-inverse-and-optimal-joint-vacuum-jets.md)付J≥800p右逆≤√200J^5.5及相容真空jets最优V_J~16J^−11/539；[全尾固定层](results/R271-appendix-full-tail-two-row-fixed-layer-range-and-contractive-known-images.md)付任意m,p双行闭源可解、D3|kerD满射/闭像，泛成本exp O(p log(m+p))，RminD3对已知像收缩。

[真实尾理想](notes/2026-11-13-actual-tail-ideal-defect-compression-and-preimage-distance-boundary.md)核两边界同一B：X_m(c)M⊂N，||P_M D_m(c)*P_W||≤Σ|c_j|η_j。三次尾≤s3e^(−770d⁴)。准确配对另有s3 dist(原像,M)，最小原像只降范数、不自动降该距离；真低核/Schur后源仍须付此距离与无权能量。

[R271准确插值](results/R271-appendix-exact-stable-range-interpolation-and-norm-defect.md)给ΠNexp=ΠN=ΠM=V及线性右逆，范数按真实λ计；W≠0时插值Gram差范数趋1。未得固定w的有界原像子列，不推N=M。

[全尾D3下界](results/R239-appendix-full-tail-d3-kernel-preserving-inverse-variance-lower-bound.md)用q个相邻位的D原始源h_(m,q)，配C=D3−μD（μ=S4/S2）的前缀共原始g，重叠ρ≥e^−20/(m+1)。任意整个尾上的v∈kerD、D3^t v=h都须||v||≥ρ/√(t!V_J^t)，J=m+2q、V_J~16J^−11/539；一次全尾最小逆≥(1−o)√539J^5.5/4，全部短链能量逐层相加。它不限制原像只能远尾创建，也不反驳RminD3的已知像收缩；h尚未验证来自实际M残量，真源预算仍开。

## 当前接口三：一般系数行与多个模式

[R176共同谱](results/R176-appendix-bounded-part-spectral-intersection-and-common-exceptional-root.md)付有界部分谱相交/连通及有限谱共用r_u；[实结构](results/R176-appendix-real-structure-affine-lines-and-odd-power-cyclicity.md)给r_bar(u)=bar r_u。实u的奇次位移/幂全循环，偶次只余α^(2k)；q在实轴单射也全闭，无实根q的零位移幂闭。ℓ1复误差只付仿射线，首位未必沿线；跨行加性须共同有限谱部分，未证明该部分存在。

[R147实切片](results/R147-appendix-real-slices-odd-minus-positive-auxiliary-and-all-shifts.md)付实u首位符号ε、实居中ℓ1 v与正定R下全部[εu^(2k+1)−R(v)−λ]^m e^w；复一次辅助保避负射线条件。u³+v²碰撞、最高字符零及双无界仍开，完整真实差商/切片条件见原稿。

**既有单模式。** [R236](results/R236-appendix-all-multiplicities-of-canonical-weighted-polynomials.md)的规范、临界弱ℓ¹、σ>1幂尾及α≤1指数子序列类均已闭，全部真实域/重数证明保留；R268给更广准则。

**更多排序行。** [R268](results/R268-entropy-budget-weak-l1-bandwidth-and-all-multiplicity-cyclicity.md)沿N满足sup_(k≥N)kρ_k≤DNρ_N、Σ_(k≤N)log(ρ_k/ρ_N)=O(N²)、logρ_N⁻¹=O(N^1.5)，则全部q(u)e^w循环。实际成本E_N+log^(4/3)ρ_N⁻¹+N²及jets/ad域已付；未满足准则的little行、1<α≤3剩余带仍开。

**旧混合范围。** R269/270保原共振、快辅助、物理不交及单atom条件；非首一底座归R152/183，联合域归R184/186，不宣称原自然域闭。一般慢Bell/多atom仍开，精确旧条件及链接保[本次前全文](notes/2026-11-13-handoff-open-before-fixed-anchor-power-domain-audit-1cf.md)。

[R236零输出分类](results/R236-appendix-resonant-polynomial-zero-output-and-leading-order.md)：a∈ℓ¹、s=a*+Σa、μ=mult_s q、L=支撑数，T_q=Σq^(r)(s)e_r(a_j(R_j−I))为零⇔L<μ；非零首阶为最早μ个位的2^j之和，μ=0为单位。无限支撑循环及二次关闭归R270C。

**全阶可和偏离与字符互素。** [R236字符定理](results/R236-appendix-real-dyadic-factor-character-coprimality-and-all-order-deviations.md)对非零主行、任意a,b∈ℓ²/c∈ℓ¹及F_q+v_c−λ给：早偏离处理全λ；否则α=a_ja、δ=c_ja，gcd(q−λ,αq'+δ)=1足循环，至多p−1候选。实际dyadic A幂、核内字符单位和C/Fourier均付，不除G_n本体。p≥2且j_c≤j_a的F_p+v_c已全闭；二次唯一候选λ*=(δ/2α)²确有单位置零输出例。一般late-c的λ0不能由这条字符判据排除。

**全阶双池与不规则行。** [二位证明](results/R236-appendix-all-order-resonant-two-site-bezout-and-derivation-budgets.md)：两N池、min位≥μN、max|a|≤C/√N、log跨det⁻¹=O(N^1.5)付全部(F_q+v_c−λ)e^w，真实jets/系数/阶乘/双边A四次成本已付。[自动池](results/R236-appendix-automatic-separated-pools-and-two-power-envelopes.md)需κ>1比较、c∈ℓ1及global logρ_n⁻¹=O(n^1.5)，允许主零位另有辅助，规则幂还许不同κ夹界。[指数种子二分](results/R236-appendix-nonsummable-main-dichotomy-and-all-order-sylvester-inverses.md)只须liminf log⁺ρ_n⁻¹/n<∞，含全部非ℓ1；需κ>2全尾比较，主零位最终c=0，有限例外任意。双池或小辅助尾的一次Cauchy给Γ_Y=O(N²)。

**平滑纤维与有限多行池。** [双行](results/R236-appendix-two-row-resonant-smooth-fibers-and-sylvester-dichotomy.md)保指数种子/比较，κ>1且某t<κ有Σ|a|^t<∞足；单有ℓ²不覆盖κ≤2。[固定多辅助](results/R236-appendix-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages.md)保d个ℓ1辅助、d+1个N池及实际位/幅度/跨det预算。主最高字符非零、相关根梯度非零足准确ℱ_F−λ循环；至多p−1个候选不表示真核。完整域、mixed最高单位及池归一化见原稿。

**任意非可和主行的简单纤维。** [完整好集证明](results/R236-appendix-nonsummable-main-good-sets-and-simple-character-fibers.md)对任意a∈ℓ2\ℓ1、有限ℓ1辅助、任意复权/物理排列，若F(U,0)−λ全为简单根，则普通F(u,v)−λ及准确ℱ_F−λ均循环。辅助相对大集合只带有限主质量，好集仍有任意大N^−s种子；双删后所有矩行/a→0，真实核主偏导有固定Neumann逆，成本O(√N logN)。实际坏根须q0′(r_X)=0，即使别的标量根有重数。结合旧首位互素，纯主全部普通二次/λ闭；不外推一般点态幂、ℓ1行或主最高字符零。

**普通点态矩消元。** [完整证明](results/R236-appendix-ordinary-pointwise-moment-expansion-and-veronese-pools.md)以有限φ/ψ逆将普通F准确变为带常数最高矩偏导的共振式；高阶矩ℓ1。兼容矩池付(F−λ)e^w，含原全梯度零；规则交替主行配无理幂辅助，或零辅助规则幂保留位，重构G=(F−λ)^h付全部点态幂。一般D阶池仍须另付Dh，主最高字符须非零。

[非可和缩放副本](results/R236-appendix-nonsummable-comparable-layers-scaled-copies-and-all-pointwise-powers.md)再去掉全局规则幅度：ρ∈ℓ2非ℓ1有无穷多层ρ_(2N)≥δρ_N且≥(2N)^−s；有限个固定分离缩放副本经双删仍留N级物理高位池。辅助在副本严格零时任意复相位可用a..a^p池；正副本配κν>2、有理独立的幂辅助时全部有限矩幂构成Chebyshev矩阵。两型均付全部普通固定点态幂和原完整域，含深排序跳跃、nρ_n→0及原cusp共同切片；不把任意单行视为满矩阵，也未覆盖居中ℓ1超指数临界族。

**其他预算仍独立。** [固定盘](results/R236-appendix-fixed-disk-kernel-inverses-and-sparse-linear-deviations.md)保无限S上|a/c|≤K、L_N=O(N^1.5)、S外任意行；[辅助尺度](results/R236-appendix-auxiliary-scale-joint-resolvent-and-independent-tail-gaps.md)保r_N=εN(c_N*)²、L_N=O(N^1.5)、Γ_Y=O(N²)，含α≤1指数/长平台，存在Y∉G正相位例。旧主尺度/子支撑按各自排序半径，详见[本次前全文](notes/2026-11-13-handoff-open-before-disjoint-leading-root-kernels-1cf.md)，不得互换。

[R134计数半群](results/R134-appendix-positive-counting-semigroup-and-finite-order-entire-resolvent.md)对正非ℓ1行给真实||e^−tX||≤0.9^Θ，Θ=Σfloor(ta_j)、Θ/t→∞，全C Laplace积分准确为逆。Θ≥ct^p,p>1付整预解有限阶q=p/(p−1)，保任意有界交换扰动/复倾斜/未知限制。重排ρ_n≥c n^−σ、.5<σ<1已满足；σ1与任意稀慢非ℓ1行尚不免费有限阶。

**旧空谱范围。** [核查](notes/2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)保R134/138/155的非ℓ1可和相位缺陷first、有界扰动/首一自然多项式，任意复权/ℓ1辅助已覆盖。居中ℓ1及无空谱慢分支不在内，二次分歧根不能免费选取。

[R257/258](results/R258-entire-selfadjoint-kernel-transport-and-actual-tail-mobius-domains.md)整自伴运输不传原M点乘域/不变格；R224公共像/尾商障碍保留。

[R259](results/R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)闭同幂尾p>1/2；[R260](results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)闭排序limsup nρ_n>0的任意复行及物理重排，允许全部复first指数和有限联合解析Bell芽。其完整域导子代数无maxF成本；剩余解析分支须nρ_n→0且排序复和→Φ(0)，一般行重根另证。

[R264–266](results/R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md)已闭α≤3/2的解析Bell/简单根及α≤1全重数；R268严格扩展后，规则1<α≤3/2的普通点态全部重数仍开。

**高阶导子及剩余短和。** [纯提升障碍](results/R236-appendix-high-degree-raising-band-obstruction-and-range-projections.md)给r≫√Q有界提升弱趋0；[全域双导子](results/R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)付[ad_T^(2r)U_N](C_Q^r)†强趋I、r=ηQ<Q/2、伪逆≤e^(Q/2)及carry。它不是单个导子像；1<α<3尚余Leibniz末O(N^((1+α)/4))项，两位校准排共同尺度粗吸收，α3不自动短段。

[全池删除背景](results/R236-appendix-deleted-pool-bell-background-resolvents-and-exact-product-gain.md)：精确ρ_n=e^−βn^α、1<α<3普通Bell，仅删O(logN)物理头，真实共同圆R_n=ερ_N^n付Γ0=O(N^(4α/3)+N^αlogN)。准确背景乘积有−cN^(α+1)+mβell N^α，合局部四次项足付；原L_j与正交伪逆端项仍未接。迟首c≈a^κ所需X圆a_N^(κ−1)过小，不能外推。

[真实核及全等向校准](results/R236-appendix-finite-isotropic-kernel-endpoint-calibrations.md)：两位Tf=0、T0=0时原端配对仍为(a−b)²/[2(a²+b²)]。四位a=(1,2,3,4)、r1<Q4/2中，M=span{E_F(f1+ζf2)}⊂kerT在全部E_i下不变且B(M,M)=0；原正交投影端项仍为35(1+2i√3)/819。故即保全等向，也不能普遍把端项写成正次T0乘积；P不保M，仍须实际无限结构。有限模型不是原Haar核，背景估计保持有效。

**旧快类须扣除。** [范围核查](results/R236-appendix-existing-fast-classes-for-supercubic-sorted-rows.md)已闭α>3的普通多项式/主理想及普遍表示；α=3保首阶r对应β>80r⁴/3与β>400r⁴两种充分范围。单个四次幂界不等于G。

**实际超指数临界余族。** [真实成本边界](results/R236-appendix-summable-superexponential-critical-budget-obstructions.md)：居中a_j=e^−β(j+1)^α、b=0、c0=0/cj=a_j^κ，3/2<α<3、κ>2，非零F2+v_c只余λ0。任意双N池d_N≤Cρ_2N，原平均实际绝对coeff≥(8ρ_N)^−r亦超预算。正锥半群/快carry给Y∉G、Γ_Y(R)≥c(log1/R)^(1+1/α)，原R=ερ_N^D须≥cN^(α+1)>N²。未证核存在、不循环或核内逆同价；须真核关系/新输入。

[R270第六附录](results/R270-appendix-disjoint-slow-point-polynomial-products-and-head-masks.md)：物理不交慢模式的已知点态循环因子可相乘，故∏(uν−λν)^mν e^w循环。mixed词域/Bell已付，共享有限头仅保单atom；同模不同根、atoms之和不能这样相乘。

## 1–3. 一般向量、限制值域与有界交换子的开放接口

旧完整范围及原稿链接保[本次前全文](notes/2026-11-13-handoff-open-before-faithful-hard-projection-limits-1cf.md)：R101只有限Walsh次数两端；任意L²循环性、未知核的gauge差像、双独立慢模式仍开。R125/128/140的全H共同正则/核心不传未知限制，R176仍许单点拟幂零部分。R32代数无零因子、R88有界逼近不付纯乘法；R143最大商图仍需实际域及分母有限放大稠密，R124零余数不付再除A。非标准主理想分类及一般A′核仍开；R256仅分类有界加权复合交换子。其余Lp/Orlicz、平滑/非零交织和各例外不变。

## 4. 相对乘积、多项 cocycle 与混合解析芽

**Newton点态幂。** [首一](results/R150-appendix-nondegenerate-newton-edge-all-point-powers-and-one-empty-anchor.md)及[非首一](results/R150-appendix-nonmonic-second-variable-fixed-sylvester-and-point-powers.md)已付空谱X、非退化顶边与逐支横截下全部[F(u,v)−λ]^r e^w，含uv−u³。完整Bell/固定补零Sylvester与真实域保留，形式首项逆不代入原算子；准确权/次数条件见原稿。重复/零根、切向及双全C仍开，P_(F^r)不等于P_F自然幂。

**剪切及中间带。** [低权剪切](results/R150-appendix-nonlinear-scalar-shears-degenerate-newton-edges-and-point-powers.md)付空谱X、j_u≤j_v、H与H(·+2kcα)互素的全部点态幂；含q(v−Ψ(u))、−u项及β≠4的−βu²族。[中间带](results/R150-appendix-intermediate-shear-degree-band-and-all-point-powers.md)在m(k−1)<p<mk、G权顶边简单时付全部点态幂，含[(v−u²)²−u³−λ]^r；完整分支微分/Bell/结果式成本见原稿。范围外β4及等号边仍另付；下文正计数/实受控辅助已闭全部总剪切次数点态幂，无须最高边互素。v−Ψ(u)仍不能当first。

**实结构真碰撞。** [最高根簇](results/R150-appendix-disjoint-leading-roots-cross-kernel-exclusion-and-real-structure.md)：空谱X_u、权(1,k)首一F/G的最高边互素⇒两核不共存，保完整不同复倾斜/Bell/域。实u,v且gcd(H,bar H)=1给全部λ/幂/权；非实中心q(v−Ψ(u))−g(u)、deg g<k degq全闭，含[(v−iu²)²+4u²−λ]^r。k1含q(v−cu),c非实，但非新空谱断言。正计数主行/实受控辅助的β4全部点态幂已由下文相伴图关闭；范围外β4及一般共轭成对根仍另付。

[实β4二维头审计](notes/2026-11-13-real-beta4-exact-head-determinant-and-persistent-zero-root-kernel.md)：首位矩阵为P+I+τP−N0，真实自然行列式D=P+²−τ²η0N1P−²。R186深域付排核归约；尾空谱及首系数β≠±α仅付P±各自循环。D的首商为2H+q+−kH−²，仍保共同零根0；不能换点态四次Bell或无证除慢B20。接两层头兼容性，尚未排原核。

[实碰撞有界剩余支](results/R150-appendix-real-collision-noncritical-branch-and-bounded-tail-normalization.md)已付r1普通F=(v−u²)²−4α²u²−λ：W=(Y−X²−B20)_can X⁻¹，真实有界根χE=2α；非临界W−E通过P_E首商排核，严格kerP=ker(W+E)，W|M=−E且非零M上谱{−2α}。每个有限头删除给Wt|M有界、谱{−2α+2Σ_(j<n)a_j}。正非ℓ1时谱点发散，仍缺可比较的统一真实尾界；不以tailℓ2小或一般截断图收敛代替，不扩F^r点态幂。

[二次增生条带引理](results/R150-appendix-opposite-quadratic-accretivity-and-finite-order-resolvent-strip.md)已证：空谱最大增生X且整预解有限阶，不容DomX²上两个相反二次符号同时最大增生；两真实因式及cosh矩形障碍完整。

[实β4 r1已闭](results/R150-appendix-finite-order-positive-anchor-real-quadratic-shear-collision.md)：a≥0、a0=α>0，实|c_j|≤C0a_j，Θ_a≥γt^p(p>1)时全部[(v−u²)²−4α²u²−λ]e^w循环。真实剩余有界支给DomY_M=DomX_M²；去全部复倾斜后两个正first限制的准确二次域与最大增生性已付，套计数/条带排核。含任意物理排列的ρ_n≥c n^−σ、.5<σ<1与实交替例。全部点态幂及更广G类已由下文相伴图另付；σ1、无计数、非实/不受控辅助仍另证。

[全部剪切点态幂已闭](results/R150-appendix-finite-order-positive-anchor-companion-graphs-and-all-shear-powers.md)：同一正a/实|c|≤C0a/Θ≥γt^p条件，G(x,s)对s首一m次且总次数≤m，则[G(u,v−u²)−λ]^r e^w全λ/幂/复权循环，含所有β和实β4；无首位互素或a0非零要求。完整Bell归一首一Q(Z)，逐深度相伴图闭包一致；闭diagZ给非零放大图有界限制，只用diagA′不变付first预解/平方域/两正增生，再条带矛盾。σ1精确双指数型、一般弱计数、非实/非受控辅助和超总剪切次数仍开。

[R189空谱锚](results/R189-appendix-one-empty-anchor-two-additive-direction-kernel-elimination.md)付快系数G[X,Y]单射稠密及总增量类秩≤2含空谱组合的情形；双共振全q保，三独立类/双全C及新子商范围仍开。

[固定锚幂域审计](notes/2026-11-13-r201-r181-all-fixed-anchor-powers-relative-domain-obstruction-kernel.md)：R201/R181同一真实乘积态给全部固定N的X_vX_u^−N闭稠定无界、非全域，虽|v_j|=u_j；任意有界交换倾斜/最高单位多项式分母仍如此。不能靠高固定锚幂绕开普通剪切混合域。

R127已闭相对ℓ¹两乘积；复杂相位相对ℓ²、三以上cocycle、非解析闭包/一般有界商仍开。R129/135单轴、R146/148单慢加快、R152有界加性及R153快分式各保原范围，超越分支未普遍限制dense。

R160慢二阶Bell不自动属G；R77/79/82临界中间参数及R83芽/轴谱仍开。R162纯虚倾斜不保乘法，指数权点态循环不扩任意H向量。

仍可寻找固定单射R∈A′使所有非例外ζ有B(RM,UζM)=0：此时closureRM非零且含于M即可用R122，无须先dense。当前辅助因子依ζ变化，可数全H稠密像之交不自动与未知M非零相交。

## 5. 一般 ISP 的独立路线与不能省略的障碍

R5/7及Rota一般归约、R2/17/18紧修正、R4/6观察拟仿射、R8/114/164/165旧紧化各保原缺口。R105/107已核PPP/MM/AT/AM原条件，未得到本候选普通不变空间；JKP2019完整正文及Tucci迹转Haar仍未核实。

[R12紧回传](results/R12-appendix-compact-sandwich-limit-and-backward-orbit-cost.md)付全部有限旗紧夹积/S_p极限||K||/2及liminfηj||J_(2^j)||≥||J0||/2；[自伴链](results/R12-appendix-schatten-sandwich-and-selfadjoint-backward-chains.md)酉等范数，紧起点不可能。FJKP2004有界链失败、Thm3.7仍须全整数；外部紧交织开。

[R14硬谱截断](results/R14-appendix-hard-spectral-cutoffs-adjacent-quantiles-and-noncompactness.md)核FJKP2005指定强收敛入口：任意固定f/非退化θ的s_n全指数有正强距离；相邻λ比零时t_n亦如此。[精确弱极限](results/R14-appendix-adjacent-hard-projections-faithful-weak-limits-and-exact-variance.md)给该子列任意f上(P_(n+1)−R_n)f→0、低谱质量→θ²；faithful f再得两投影WOT→θ²I、s⇀(1−θ²)f/t⇀θ²A*f及精确正方差。保开闭端点及满支撑边界；有正测度零集者全空间弱标量极限仍未付，逃逸目标/退化θ/其他方法仍开。

[family293审计](notes/2026-11-13-family293-hyperinvariant-scope-and-backward-normalization-audit.md)仅超不变结论，纤维有普通真尾空间且交换子非交换；Domar不同权不能借R88或反向归一改成普通反例，未重编Lean。旧完整条件保历次归档。

## 不能互换的极限

全部混合自然词域不保普通系数截断；可数first核心及固定正则子在子商单射稠密，不使原词普遍dense。非零有界交织不能把全像送入全部first域；R204重选行不代固定慢行或边界运输。实际域、carry、非零锚仍须支付。

[R239首位图](results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)/[横向压缩](results/R239-appendix-coercive-adjoint-and-positive-mixed-compression.md)保C²=η₀N₁|L、||C||<1/√12，真缺陷需C*Gx=0及C*x=−η₀(N₁|L)*Cx。核上T*≥7/8、Re(P_MBT*|M)≥5α₀/6，给M⊥内横向同构而非BM原像；各位压缩约束仍未排缺陷。详式和度量字典在原稿及本轮归档。
