# R150JetEndpoint 发布前 HANDOFF/open 完整原文

核读 main：876b4dc66f2466f37452db1ca537fddbf7af0361。两README blob未变；终端unavailable，按根§8小文本后备，API不计实际pull。

## HANDOFF.md 原文

# 交接

## 目标、负责人和规则检查点

- **目标未完成：** 解决可分无穷维复Hilbert普通ISP；Haar普通不变格、边界N=M、一般正常见证仍开。不降低README标准，不以阶段/时长收尾。
- **负责人及分工：** Astra-ISP-1cf8c51d负责，0c继续贡献。1cf用R213–229、R240–271；0c用R230–239。新编号先登记，独占git/index，不动他人未发布文件。
- **最后实际pull/规则：** 2026-11-13 01:06:52 UTC，cdb9429c93f969d1054d8e1e49643add83457c24；真实git pull --rebase origin main，两README差异空。每小时至少一次，终端恢复即补。
- **0c 最近实际 pull：** 成功仍为01:06:17 UTC / bfe9f2c0b2977d4bab3d14793c3f247374e81303，两README差异空；最近13:18:13真实pull调用执行前No usable execution environment，API非pull，恢复即补。
- **已读规则blob：** 根 f787a306d90892d8dec765dc59747d60ba39f055；题 6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd。每次实际pull均比较两README，有变只读差异立即照做并记SHA；至少每小时pull。
- **API后备检查点：** 2026-11-13 13:13:24 UTC / main 1adba75368df9dea3afe7e797b4fbd88545ac950，两README blob未变；1cf13:10:54真实pull执行前无环境，API非pull，恢复即补。
- **发布：** 完整结论单独推；终端可用用git，拒推即pull --rebase。仅失联用根§8小文本；API不算pull。令牌仅命令行，不写文件/config/提交；不force、不写根LOG；Markdown<100KB、H<10KB，合并最新main。

## 恢复记录与模型

工作树：1cf /tmp/isp-1cf8c51d-math-research；0c /tmp/isp-0c017065-math-research-20261113-0030。本次压缩前全部H/open及归档链见[本次前H/open全文](notes/2026-11-13-handoff-open-before-boundary-first-elimination-0c.md)。

模型：H=L²(Z₂)，A为正实径向Haar odometer；Nj=Ej+ηjEj*N_(j+1)、ηj≤e^(−770·16^j)。A′交换/C对称且R88保有界SOT多项式逼近。UHF/C不自动运输未知限制或实际域。

## 1. 原 Haar 正常湮灭者

**R228：** C平均保φ可增秩，J0平均可改φ；实两块合max(p,q)。复Ri带权实结构，真Ri实Krein两指标∞，不付秩一。
S_N/Y全H单射稠密已证，普遍强主理想仍开。失败有正有限秩正常见证；R228允许C实化，R229反例排一般秩一纯化，R242窄矩阵/垂直商图已付但不免费图稠密。
**既有正态范围：** R255排E_√3有限正见证且端点最优；R235保函数非负锥及R237 Walsh对角/有限带/entrywise-ℓ¹/指定乘积基有效，一般正常态不覆盖。

**R235：** 连续/a.e.+双边UI已排，普通L∞不够；全右矩|φ(T_mG)|≤h_mλε_m||G||保留，待预算内非零右配对。
**R237：** 固定Q∈Acal的QAcal同范数强*逼近QA′；非UHF左因子/无界右因子不覆盖。
**R248：** 相似交织⇔−logδ∈ℓ2，全A′/慢核/格及poly条件数保；一般延拓不免费，非相似≠有核，R250 A+开。
**R253/R237/R230：** 真湮灭迫q_m↓0。逐位Jensen给纯正锥真空比≤e^{(m+1)/2−πk/16}；多重Fourier及双换元除法覆盖周期r≤q/100、总deg≤q³的任意复p(Uν)，实际比≤2e^{m/2+1/4−q/10}，独立exp参数≤q⁶同界。相对carry全付，旧标量/Gram/相位锥保留；非周期/超预算/真密度专属及完整q_m仍开。
**R244：** 实际误差→0且保固定右锚迫聚合源∞/归一弱零。精确h_p误差≤√δ·尾像≤δ||R||；压源保锚迫||R||≥η/δ，不替v_p。热矩/球发散/WOT闭包保；巨大尾放大/共同图开。
**R267：** 特定P∈∩A^rA′非零，有收缩强*单位、P1循环、1无原像且与UHF零交。PH不自动入闭词域，全Walsh平方和未付；保持非零锚的直接阻尼已排。
**R230最小秩：** 模交/逐对域、商单位及比例全C谱保。k<r变化源误差≥c/[(1+L)^(r−1)C(c′(1+L)^−r)]；正交乘积τ≤Ci(ε)²η²+Cj(η)²ε²，第二小≥√τ/(√2ε)，纯幂βiβj≥1。无C上界，εK_m与ε_mCi仍须同时付。
**R230远尾：** 纯远尾/固定有限Walsh头可准确擦除到真空，乘积预算H→∞；若前缀carry×H→0，擦除向量也发散/归一弱零且保锚τ。无最小秩要求，近似分解另付聚合残量。
**R230头矩：** 真ρ的v_p范数∞/归一弱零、均值τ；reset密度付Φ_vp→φ于全A′_*。全部ann Z同时||Zv_p||≤τ(2Kp d_p+||Z||Dp)；S/T与Z分付a/c尾。真核cross h_p另有||Th_p||≤Γp√τδp，源不同。固定k c0/小o、组合费及端点秩预算保open；δ无速率，源费未闭。

**R253/263：** 全A^r与子半次数域不能作通用S分母，真见证专属配对仍开。

## 2. 两个实际边界的 N=M

T=T_N,T_Y，M=kerT，N=closure BM，D=M⊖N。R187/200给M∩RanB^r⊂N，有限孔核仅真空；R234模N已闭，R238原J_q成本不能当模N成本。环境坏见证在M⊥，横向T*M同构不是BM原像；旧通量/头Jordan/平方γ各保原范围，详归档。
**R239全q：** d≈log^(1/3)q、K*=3(16/770)^(1/3)给c>K*权核入N及真D尾常数K*/2；R271先得4/3权阶。Σ1/[ell(1+λ²)]发散足N，真实λ²=〈G⁻¹r,r〉必须保Schur补，无权增长未得。
**R239分解/末段：** 旧T_i/短旗预算保open，T_i不保W。Vandermonde x∈kerD²且||D*x||²=S_(m+2p)→0排h≥2统一gap，h1保；D3Dx=0使真σ_3正交坏向量。新F5=D5DX≠0给V2*b=V2*B2b=0而(V2*B2²b)_2=4aJ2F5≠0，真B2/H2不保外桥核，P_kerV2* H2⁻¹V2≠0。实际σ=V2Q1⁻¹V1B0⁻¹g0更窄，未证其坏增长或廉价能量。
**R239/R271闭链：** 固定头宽窗率按κ，最优κ的旧证书超同m lift，非速度下界。合法K(h)与同旗D3桥保；新双宽Z给P_Zh=c_d−c_2d，||h⊥||²=||h||²−λ_d²+λ_2d²恰为C̃tot的零源商范数。实际配对去核仅付e−75d⁴√能量差，正通量转为β_2d||h⊥||加carry。负〈h,c_2d〉不许把w换成c_2d；尚无h⊥上界/统一下降率/无权λ增长。

**R271/R239边界源：** 旧LDU/增广对偶运输保。先消F得同z及新H2°=AH+B PkerF B*；低链a由真实未来β付，完整D3差源有同窗kerF原像，σ°对实际X3w∈N的相邻运输≤s3β+carry。旧H2−H2°的正差恰裸返回费，旧σ在新逆度量另付λret²，不能以新E2°≤λ²代旧E2。无权/返回费仍开，全h必要平方下界保。

## 3. 危险核、中央闭图与系数行

**R176：** 有界部分谱相交/连通、有限谱共r；实r，奇次全闭、偶次留α^(2k)。复ℓ1误差只付仿射线，跨行须共同部分。
**R147：** 实u、实居中ℓ1 v及正定R，εu^(2k+1)−R(v)全部位移幂循环；复一次保射线条件。一般正号/双无界开。
**R189/R201：** 空谱锚的快G[X,Y]及总类秩≤2范围保；慢Bell不免费。逐项支配仍不付DomX^N⊂DomY，所有固定幂/最高单位分母均有反证。
**R150剪切：** 旧正锚/列/多尺度保。原log幂有限jet第r尾S^−r/√n；D−d0<ν_D付全Q(F)（d0=0限Q(c0)≠0），全相消D<ν_D付Q0≠0。任意R阶简单零点族已付；D=2m统一外盘，弱端点/盘内零参续。
**R150域分类：** 正族固定词/幂/积分母行类span{bν}+J_Σb，J_w=ℓ1+ℓ2(w⁻¹)；不同域不混同。单锚γ唯一，多锚mod J；最高单位Bell逆保。
**R150半群/混合：** heat×正预解行类span{b}+J_(a+Σb)，纯heat可选锚ℓ4/3。S H_aδ=H_a(δ+2t)、双侧预算/自然域及未知M/旗加权商/闭图可数正权core保；非ℓ1 XaS不全域。
**R134：** 正计数半群/全C Laplace/有限阶预解保原范围。
**R268–270：** 旧非首一底座归R152/183；新增共振F_p/快辅助/物理不交乘积，不扩普通慢Bell或有限头多atom。
**R236字符：** F_q+v_c−λ的早偏离全闭，否则gcd(q−λ,αq′+δ)=1足，≤p−1候选；二次单位置有真零例，late-c双池类已排。
**R236双池/二分：** 双池、指数种子/有限多行及非ℓ1全尾κ>2按open原条件；种子/比较/主零位不省，点态幂另证。
**R236普通/平滑：** 非ℓ1好集简单纤维/纯主二次保；缩放副本按open完整零辅助或正主/独立κν>2条件。无副本重根、ℓ1极快/双无界开。
**独立预算：** 固定盘|a/c|≤K、L_N=O(N^1.5)保；辅助圆r_N=εN(c_N*)²和Γ_Y=O(N²)保，含辅助α≤1指数/长平台。旧主尺度/子支撑各保假设。
**R236广义核：** 有界Bell包络α>0，固定阶ad强I给全n,m的B(kerT^n,kerT^m)=0与kerT^n⊂closure RanT^m；非零闭广义核无限维真，未付实像/限制稠密/局部等向。
**R236联合见证：** 有界ℓ1迟首二次核⇒同一ζ、正秩一ρ湮灭S=X+H、T、Z=Y−G，G=B0−H²；S全H单射而M内非稠密。整函数F的全右正常配对准确替换(X,Y)→(−H,G)，H/G∈G付4/3增长与混合四次矩；不能只凭这些界排核。联合非零快证书未造，ρ不跨ζ，c=aκ仅j>j0。
**其余界：** 快类/全池预算见open；四位全等向排通用T0因式，原P距离及巨逆carry阻范数搬运。纯等权高ad有界输出k≫√(NlogN)时WOT0，只限该模型。居中late-c λ0、末段伪逆/ΓY/小X圆开，中央域/family293不外推。

## 紧接稿及持续执行

**R12/R14：** 紧夹积/S_p、紧回传成本及自伴链禁阻保。FJKP两硬截断指定子列均非紧；faithful目标投影WOT→θ²I、方差准确。外部紧交织仍开。
1cf已推端点47f515e6；本次实际有限jet及任意高阶简单零点族。续弱端点单位、实际返回费及4比较。
0c MP型35/6/carry245/3已扩有限P；纯ℓ1 first及至少一行无限支撑的纯二次核已排（局部ad精确零）。实际慢尾/返回费仍开，续近似列与L/future；Gram精细猜想已反例。
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

[聚合转置预算及统一阻尼](results/R244-appendix-aggregate-transpose-source-budget-and-exact-dual-cost.md)：真慢湮灭的正ℓ2负权/heat预算发散及WOT闭包已付。误差→0且保锚迫聚合源∞/归一弱零；真h_p误差≤√δ·尾像≤δ||R||，压源保锚费η/δ。仍欠共同图或巨大尾放大下专属有效源，不替v_p。

[正热过滤工作补充](notes/2026-11-13-positive-heat-normal-filters-and-uniform-vacuum-source-cost-normal-complex.md)：复用R240完整弱闭包后，整个有界ℓ²球的过滤正常泛函弱闭包准确为λφ(R(b)·)，λ>0且不含零。正ρ用真实D_m(b)和有限头网付统一检测，范数≤exp(3B√m)，保δ_m/carry。任何近似真空源u若逼近这个变化过滤族，其成本c_B(ε)随ε↓0一致发散；这是全族/任意源量词，原hp负权为旧判据推论，不重复登记。仍未由同一二次核三零式造所需有界源。

[纯远尾与固定Walsh头](results/R230-appendix-pure-tail-source-erasure-and-carry-controlled-aggregate-growth.md)：源Ω_<m⊗z可任意移远/弱零；尾秩一擦除先给固定真空配对，故H=Σ||z||||h||→∞，不要求最小秩。准确carry a_car=d0∏_{j<m}η_j≤d0e^{−770(16^m−1)/15}；a_car H→0又迫擦除向量v发散且归一弱零，〈v,Ω〉→τ。允许可变有限源数；固定有限Walsh头经真实V_FΩ=χ_F准确合并，须计其乘子范数。近纯尾另付Σ||h||||d||→0。未把一般纠缠源当纯尾，未给H上界或解决源/尾耦合。

[原正密度的全头矩](results/R230-appendix-first-walsh-observability-and-canonical-positive-head-moments.md)：v_m=Σ_(F⊂m)(−1)^|F|φ(V_F^[m])χ_F准确代表整个头代数，K_m(v_m)=τ、||v_m||≤10^(m/2)τ。真慢理想湮灭迫范数∞/归一弱零，固定实际p的头差全付；真实全行擦除与v_m范数差→0。旧145/73稳健观测保持有效，且被下列平方估计加强；未把头测试直接放进ann。

[同一规范头源的全部强残量](notes/2026-11-13-canonical-head-positive-normal-sources-and-simultaneous-strong-annihilation-central-review.md)与[真核交叉源](notes/2026-11-13-kernel-supported-positive-density-and-strong-truncated-source-residual-normal-complex.md)：正reset密度使完整v_p的Φ_vp在全A′_*范数趋φρ，误差≤τD_p+2δ_p+2√τδ_p且均值恰τ。若φρ(ZA′)=0，实际/局部C配对付||Zv_p||≤τ(2K_p||Z−Z_p||+||Z||D_p)，无需ρ支持kerZ。同一个联合ρ的S/T残量≤C10^(p/2)(e^(−βp^α)+pη̄_(p−1))，Z=Y−B0+H²残量保更快κβ指数；B0真carry与H解析头差已付。真核cross h_p另有||Th_p||≤Γ_p√τδ_p、Φ误差恰δ_p；不混同两个源，不由小残量推出距核、有界源或理想证书。

[混合高阶强残量与正密度HS幂](notes/2026-11-13-canonical-positive-sources-mixed-power-residuals-and-polynomial-budgets-normal-complex.md)：实际头与真实尾分开后，同一v_p满足||S^kZ^l v_p||≤τ10^(p/2)[C^(k+l)e^(−β(k+κl)p^α)+C(p+k+l)B^(k+l)η̄_(p−1)]；全部变化多项式另保绝对系数/导数费用。T=(X−H)S+Z给二次混合幂，不把其余项当纯尾。真Tρ½=0还给||T_p^n ρhat_p½||HS=||T_p^nρ½||HS≤√τ(r_Tp^n+nM^(n−1)εp)，εp纯carry；n p^α=o(16^p)仍保完整指数。准确阈值投影Pp=1_[0,sp](|T_p^n|)有Trρ(I−Pp)≤τ(b_p/sp)²，仍须付b_p=o(sp)且Pp在原表示强零，不能以维数或相似替代。

[R236精确真空MP列](results/R236-appendix-exact-head-vacuum-column-and-carry-cost.md)（[源稿](notes/2026-11-13-actual-head-moore-penrose-vacuum-column-and-carry-cost-normal-complex.md)）在原Haar前移头给全部幂的完整加权卷积，目标顶部误差√(rq/2^p)与解底部自由核分清。稀有最高进位坐标保q=1最高辅助修正；§4.2用临界系数圆及同位置权比夹逼任意rq_p/2^p→0时16^(−p)log||ξ_pq||→35/6。准确η的175/2指数支付全部actual低头比较，That_p^q近真空误差≤√(rq/2^p)+exp[−(245/3+o1)16^p]；全rq≤2^(p−1)也保905/12余量。含完整慢尾的T仍须另付：现有明确HS上界budget b_pq与exact列不能同时满足b/s→0和s||ξ||→0，未将上界当实际残量下界。同一A_p删稀有目标可低费逼近，故T_p^q的允许误差原像/真空ridge仍开，不能由exact成本判定它失败。 同稿§4.3把35/6与245/3扩至有限条Σ(aN+bQ+eQ²)、a/b/e∈ℓ1的固定P(0)=0，明确假设形式首阶有限非零；最高位一次系数仅Σ∂P(0)(a−2b)，一般ℓ1尾不附速率。

[实际平方选择器](results/R230-appendix-actual-cayley-selectors-and-sparse-walsh-escape.md)：任意v有||P1v||²≤80K(v)||v||。真实V_j增生及不交块±εσ_B V_B修正给大小≤d的任意不交族能量≤A_dK(v)||v||，A_d=256·9^d(d+1)^(3/2)，不要求其他次数为零。真ρ v_m的≤1层及任何变化有界大小/有界相交费用族的归一质量→0，高于一次比例→1；h着色须付hA_d。完整k次层仍付binom(m,k)/floor(m/k)，全≤d消失另须||v_m||≫m^(d−1)，未证明此增长。一般密集交叠高矩仍开。

[完整二次矩谱范数](results/R230-appendix-complete-quadratic-moment-spectral-norm-and-effective-rank.md)：真实L=Σw_jV_j的三次真空列≤40||w||₂³，两个Cayley收缩消一次项，付完整零对角复矩阵B_ij=v̂({i,j})的||B||op≤690K^(1/3)||v||^(2/3)；含实际对角的二阶矩付699。允许全部交叠/复相位，无纯化carry误差。真ρ v_m的相对谱范数→0，任意变化秩r=o((||v_m||/τ)^(2/3))的左右矩阵投影相对HS质量消失；二次层若占比δ，有效秩≥2δ²(||v_m||/τ)^(2/3)/690²。原正密度有限秩不推出矩阵低秩，完整HS组合费用仍未消除；继续密集高秩及高次。

[所有固定阶实际矩张量](results/R230-appendix-all-fixed-order-actual-moment-tensors-and-injective-norm.md)：准确V_FΩ=χ_F及||V_j||≤3给||L(w)^nΩ||≤3^(n+1)n!，仅需有限w的ℓ2权。k阶Cayley有限差分、复多线性极化及集合分割Möbius去重，付任意完整无重复k张量||T_k(v)||ε≤Λ_k K(v)^(1/(k+1))||v||^(k/(k+1))，Λ_k明确且与指标数无关。真ρ每个固定k的归一注入范数→0，允许所有指标交叠及变化复纯张量；有预算射影范数/正交纯张量子空间同有准确消失阈值。HS²=k!||P_kv||²，不能由ε界推整个k层消失；一般张量秩不替代分解预算，增长k_m另须付Λ_k。

[正密度截断与小迹尾](results/R230-appendix-positive-density-walsh-truncation-and-small-trace-tail-improvement.md)：任意有限Walsh投影P_Λ使ρ−σ_Λ（σ_Λ=(I−P_Λ)ρ(I−P_Λ)≥0）在全部A′上精确等于Φ_hΛ，||h_Λ||≤2τK_Λ、K_Λ²=Σ_(F∈Λ)9^|F|；头代表差同界且固定Λ时强趋h_Λ，完整保纠缠/全迹类求和。δ_Λ=Trσ_Λ→0，小迹尾承担全部头矩发散。对任何统一线性观测O((Trθ)^α||v_mθ||^(1−α))，显式p_m=floor[(1−α)log(V_m/τ)/log10]支付变化头费用，升级为o(τ^α V_m^(1−α))。因此一次/着色/完整k层平方均改小o但保组合因子，二次op=o(τ^(1/3)V^(2/3))，固定k注入范数同改小o；原端点O秩/射影预算也消失。二次若保占比须V=o(τm)，未证明增长与之冲突。

同稿§6.4–6.5补固定次数：任意正常ψ的实际ψ(V_F)在1≤|F|≤k中为c0（真实列χ_F及统一3^k付WOT/正常极限）；实际头carry给||P_kv_m(ψ)||=o(m^(k/2))。真正ρ若k层保占比则V_m=o(τm^(k/2))，k≥3改进旧组合门槛；固定d≥2只需另证V_m≳τm^(d/2)即可排≤d比例，但未证明该增长。旧完整块Gram的同一连续正秩一非湮灭f在一次层已有Σ|φ(V_j)|²=∞，实际carry为ℓ²差，故c0不等于平方和上界。

同稿§4.1给实际固定真空源：||φρ−Φ_hp||_(A′)*=δ_p、〈hp,Ω〉=τ−δ_p、||hp||≤2τ10^(p/2)。真湮灭迫||hp||→∞/归一弱零；明确成本c_(Ω,φ)(δ_p)≤2τ10^(p/2)，但δ_p无额外速度，且这不是删除原源C_i的上界。正尾准确φ_σp(SR)=−Φ_(S hp)(R)，不冒充新的零湮灭者；继续真正S递推及完整高重叠预算。

[变化源定量预算](results/R230-appendix-bounded-near-relations-and-quantitative-changing-source-compression.md)：k<r候选由原源/真空生成、L=kab时误差≥c/[(1+L)^(r−1)C(c′(1+L)^−r)]，趋零迫L→∞；近似生成加ka ε_gen，无真空版不需预解。Ci有限但各自发散，§8.5锐化τ≤Ci(ε)²η²+Cj(η)²ε²，第二小成本≥√τ/(√2ε)；纯幂上界须βiβj≥1。条件1≤γ<4/3的对数幂上界可配合四次误差排超预算压缩，但真实Ci上界/右测试生成均未得。

[源/尾误差工作笔记](notes/2026-11-13-source-cost-and-tail-error-diagonal-coupling-normal-complex.md)：当前须εK_m与ε_mCi同时小，K_m≥exp(πq/16−(m+1)/2)；连续凸逐点有限成本也不足保证任何子列。R253物理尾与q=2^m共用参数，R267非UHF不能套形式首阶。缺行真实向量也须发散；只定位既有范数方案，仍寻实际两参数族/专属配对。

**固定非湮灭态。** [R230完整Gram](results/R230-appendix-arbitrary-contractive-block-gram-and-complete-source-obstruction.md)对同一f、q_i=16^i排收缩纯块/有限完整逆源，指数log5/2；非块/无真空未覆盖。

**真密度完整矩。** [R230](results/R230-appendix-positive-density-moments-dual-certificates-and-localization-obstruction.md)付m_B=L_Bρ_B、Gram=||R*m_B||及全部carry；真右矩含非正Tr_(B^c)(ρT_m)/h_m，不能换K_B*m_B。有限块正对偶严格可行，理想收缩R、||RΩ−Ω||≤a<1/2给μ=(1+a)/(2−a)。全部精确矩/预算见原稿与[本次前全文](notes/2026-11-13-handoff-open-before-common-singular-core-sequences-1cf.md)。

R242窄图、R250稀疏图的限制保归档，未得A+不变。

[1cf已付范围索引](notes/2026-11-13-1cf-established-scope-and-domain-limits.md)：噪声相似、共同幂、正锚域/heat、超线性Newton与原列中心的完整范围及限制见索引。仍欠指定见证负权/first域、一般非柱低边与唯一根的新实际测试；非相似/强单位不赠核或域。

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

**联合核短塔与两种末段预算。** [低孔Fock](results/R239-appendix-low-hole-fock-tower-and-nonvacuum-primitive-prefix-removal.md)保s<c logq/loglogq；[近一次短旗](results/R239-appendix-short-flag-towers-and-near-linear-nonvacuum-prefix-removal.md)用||D|kerD^h||²≤(h−1)S、D3泄漏与真实K*K，只从E_(d,s)建d层。s=floor(q/[128(d+1)]^(d+4))时原宽d末段修复及受限能量平方和→0，但s/q→0。

[固定比例完整预算](results/R239-appendix-fixed-fraction-subpower-repair-budget.md)：准确尾W与短塔双范数付α<0.3420369时K≤(2d/√γ_α)^d=q^o1，整个原宽d末段受限能量≤q^o1||w||²，无分支损失但未趋零。真缺陷迫早期(1−α)q分支能量/[q(logq)^(2/3)loglogq]的limsup∞；一般最优通量仍开。

[全孔层联合能量](results/R239-appendix-all-hole-environment-energy-gap-and-actual-tail-stability.md)用有限ad_[D,D*]证书隔离单个位：m≥5时D*D+DD*≥1/(4L_m²)，logL_m=O(m logm)，原两型实际尾以carry稳定到1/(16L_m²)。m=O(loglogq)给次幂环境常数，但真实伴随含P_kerD²；两位例中D*h≠0而P_kerD²D*h=0。故不能由此替换受限Gram或原修复能量，须付真实源上的D3投影损失。

[原权Vandermonde反例](results/R239-appendix-vandermonde-coprimitive-short-kernel-counterexamples.md)已关闭一条环境候选路线：任意偶数2p互异正权，x_S=(∏_S a_i)ε(S,Sᶜ)Δ(a_S²)Δ(a_Sᶜ²)准确满足D_prefix*x=0、D_prefix²x=0。原尾归一张量真空得x_(m,p)∈kerD_m²、||D_m*x||²=S_(m+2p)~1/[3(m+2p)³]。所以固定h≥2也没有全孔层统一D*下界，实际D*限制单射但像非闭；固定层下界与h1联合gap仍成立。未证明该族来自真实W/Schur源，不能推出N≠M；继续真正源结构及C̃tot预算。

[实际外出生源排除](results/R239-appendix-actual-outer-birth-source-factorization-and-vandermonde-orthogonality.md)：上述x还准确D3Dx=0。保σ=V2Q1⁻¹ζ、V2=S1S0*，σ仅在出生q+2；对每段J_t*σ_t=−t(t−1)C_q*K_t*ρ_(t+1)，C_q=D3:kerD_(q+2)→kerD_(q+1)，伴随含真投影，Q1⁻¹未交换。故第3段σ准确正交允许头⊗x_(m,q+3)，环境坏方向不自动成为真实源坏方向。真实z2=H2⁻¹σ仅满足z2⊥B2kerV2*；下稿已证整个外桥核不被真实B2/H2保持，不能把源正交传到最优链或将C_q*替为已有C_q能量收缩。

[真实高出生块混合](results/R239-appendix-true-high-birth-block-failure-to-preserve-outer-bridge-kernel.md)：原Vandermonde X的F5=D5DX逐系数非零，C²X=−2F5。取高块b仅第3段e0X，保a=P_≤d−3 A*e0及全部头/尾旗，前两轮B2b=Gb、B2²b=G²b准确。V2*b=V2*B2b=0，而(V2*B2²b)_2=4aJ_(2,q+2)F5≠0。因此真B2及H2均不保持kerV2*，进而P_kerV2* H2⁻¹V2≠0，即某些外桥像源经Schur逆确进入外桥核。未证明这种源来自更窄的V2Q1⁻¹V1B0⁻¹g0或实际w，未给其能量增长；继续真源度量及C̃tot预算。

[固定头窗口](results/R271-appendix-fixed-head-condition-and-uniform-window-convergence.md)：λ_d≤κλ∞，宽d+n(d−1)能量相对误差≤4(κ²−1)((κ−1)/(κ+1))^(2n)，全q/源统一。R249最优logκ≈35d⁴/6使本证书logh同阶，超过旧同m lift；不代表实际链速度下界，真残量/低核通量仍开。

[平方局部型](results/R271-appendix-square-head-smith-types-and-old-head-single-block-correction.md)保Smith(2d−1,2d+1)/新4d及原费用；[固定尾塔](notes/2026-11-13-finite-tail-tower-corollary-for-exact-residual-flags-boundary-resume.md)只付固定窗闭像，均不传原核统一能量。

[窄头移段接口](notes/2026-11-13-actual-narrow-head-flux-shifts-and-paid-last-source-1cf.md)：同头真h移至q+k，J_kc是−Ac_k可行链，完整零源投影能量=||Jc||²−λ_new(−Ac_k)²≤λ²（扣旧双宽限制）。剩余恰(I−PkerS)h及ρ_k=G_new z_k−Ac_k的完整修复两正交项，均未上界；末段恰−c_d。ρ_k与rret/同w源仍未匹配，不穿Schur逆。

[真实返回源工作笔记](notes/2026-11-13-actual-last-block-return-source-and-complete-low-chain-projection-1cf.md)：E2≤λ·λq(FKcL)，真Q修复仍开；完整C缺陷、primitive与对偶λ接口已付，旧r′未识别。[首段先消元](results/R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md)现付真实小a、同一z与X3w源；新E2°≤λ²，而旧E2−新E2°=||𝔉†rret||²仍欠。一般primitive比较不能替实际窄H_t/返回费。

[R239首段边界先消元](results/R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md)（[源稿](notes/2026-11-13-boundary-first-elimination-small-source-and-exact-return-energy-boundary-resume.md)）保持同一最优对偶z，G°=S PkerF S*仅改首出生块。整个低链裸最小源a=𝔉†r由真实未来带β+e−72d⁴||w||控制，新H2°=AH+B Pker𝔉 B*、σ°=Ba，E2°=λ²−||a||²且前两正能量≤β²+carry。完整D3给差源的同窗kerF校正(n,C_Ha)，新逆能量≤s3²||a_next||²−||a(Cr)||²；准确接到实际X3w∈N的相邻源，误差≤s3β+18s3e−73d⁴||w||。原强制通量仍使用旧H2；其正能量差恰||𝔉†r_ret||²，任意旧高源f的新逆能量另加λq(F S*G⁻¹f)²，特别旧σ额外付完整λq(r_ret)²。因此两处源匹配和旧||b||成本已在新消元中付清，原返回费用仍未获上界。 同稿§9令L=B_A*(H2°)⁻¹B_A≥0，λ²=||a||²+〈La,a〉、旧E2=〈La,a〉+||La||²、λret²=||La||²+〈L²a,La〉。完整C的U/J正缺陷给真实对偶误差≤s3√(λ²−||a||²)，实际A_q交织的carry亦付；X_M* A_q*L A_q w不能由w⊥N杀掉。真实future去共同低源g=u+ahat∈kerF后，得到保正部和全部carry的短化Cauchy；原W直接使||PkerR g||≤(e−74d⁴+e−75d⁴)||w||，故g到真正内部最小像的距离及平方能量损失都已付。仍没有La或返回费上界。

[R239七位精确反例](results/R239-appendix-seven-site-counterexample-to-refined-primitive-gram-comparison.md)已否定此前精细有限N/s Gram上界：权(3,3,3,3,3,1,1)、s=2,n=2的对称primitive f=90v0−6v1+v2满足γ2²/(γ3γ1)=10201/22987>2/5，原差二次型恰−1118/127。三个完整3维Gram先逆再压，组基度量/全部逆像乘回均有BigInt证书；[原候选记录](notes/2026-11-13-primitive-gram-finite-newton-comparison-probe-0c.md)已改为失败路线，五组正例不再支持一般上界。此反例未否定更弱归一常数1，也未识别原边界窄Schur源；真实返回费及无权N=M仍开。

[边界恢复笔记§7–8](notes/2026-11-13-boundary-variation-checkpoint-0c.md)：r=e0h的完整最小链只首段e0D†h，与其余头源正交，λ²精确分块且E2/返回源为零。此分块不能递归：原两型A02=1/4或1/4−η0非零；取primitive k、D3k非零，h=−2D3k使P_kerD(DD*)⁻¹D†h非零。头1/2两条合法零源补链迫仅头0/1的候选不可能全局最小，故更高头严格降能。源是合法V_mq向量的Av且在原D3像内；显式两头试探给λ²≤(m⁻⁴+m⁻²)||k||²，对q一致，所以严格高头改善不等于大能量下界。仍未识别为真实M/W投影或取得E2增长界。

[真实尾理想](notes/2026-11-13-actual-tail-ideal-defect-compression-and-preimage-distance-boundary.md)核两边界同一B：X_m(c)M⊂N，||P_M D_m(c)*P_W||≤Σ|c_j|η_j。三次尾≤s3e^(−770d⁴)。准确配对另有s3 dist(原像,M)，最小原像只降范数、不自动降该距离；真低核/Schur后源仍须付此距离与无权能量。

[完整L核及合法M测试](results/R239-appendix-full-l-kernel-completion-and-legal-m-tests.md)：D3在每个固定短纯核旗满射，真最小像对同旗已知像收缩；一致头右移与相容R_j把真实低核源h_t拼成完整K(h_t)，支撑[q+2,q+2d−2]且范数≤e20d⁴，原逐头lift入N。定义C̃tot=Σ(K(h_t)−h_t)，真实正通量给||v||²+λ²≤β_q||C̃tot||+e−51d⁴||w||√(||v||²+λ²)。该最终误差不需D3原像成本；所有非中央项按真实层相加。若从D3原像拼链，Z=Σ(−A)^j[D3,R_j]u仍是完整高尾核，不能省略/据旧宽d最小性消掉。未给C̃tot的Schur后预算，不把e20d⁴当q^o1。

[双宽实际源投影](results/R239-appendix-double-width-head-flux-projection-and-exact-energy-drop.md)：同一m,q,r，宽d/2d真极小链满足P_Zh=c_d−c_2d，Z=kerL∩H_[q+1,q+2d]；靠准确新头旗P_C2d g=c_d−h、g⊥Z证明。C̃tot模Z的最小范数恰||h⊥||=√(||h||²−λ_d²+λ_2d²)。原lift去P_Zh只付e−75d⁴||w||√(λ_d²−λ_2d²)，给E≤β_2d||h⊥||+4e−70d⁴||w||√E。〈h,c_2d〉负不允许把w替换为c_2d；未给h⊥上界、能量下降率或越已付lift的迭代。

[完整修复链/真Schur](results/R271-appendix-complete-repair-chain-lowering-defects-and-true-schur-contraction.md)：同头下C R_(q+1)−R_q C∈有限kerL，W投影≤2s e^−74d⁴，准确Pythagoras给C*G_q^−1C≤s²G_(q+1)^−1。内部完整Gram经保持的Y_a子空间得到H_a=[P_aG^−1P_a]^−1真Schur收缩与结合律；不能换旧高块普通压缩。实际Cr_(q+1)(u)修复的W投影≤sτ+ε+8s e^−74d⁴，两次降孔/相邻整数同头均付。下一缺口是新消元后的实际两桥有效源能否属该C像；尚无一般无权能量界。

同稿§7已将旧两出生桥改成低先消元的真实σ=V2Q1⁻¹V1B0⁻¹g0、z2=H2⁻¹σ。准确三正项能量分解及实际未来投影Su=−F给E2≥(E−小量)²/(β+小量)²；强制能量定位到末块，旧总投影损失比例不重计。尚无σ廉价C像或E2反向上界，接R239完整L核后的Ctilde_tot真实合成预算。

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

**已闭的多行与普通点态范围。** [双行](results/R236-appendix-two-row-resonant-smooth-fibers-and-sylvester-dichotomy.md)及[多辅助矩阵](results/R236-appendix-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages.md)仅在各自指数种子/比较或完整物理池预算下闭平滑纤维；主最高字符须非零。双行κ≤2仍须另有Σ|a|^t<∞（t<κ），单有ℓ2不够。

[任意非可和好集](results/R236-appendix-nonsummable-main-good-sets-and-simple-character-fibers.md)对a∈ℓ2非ℓ1、有限ℓ1辅助、任意相位/物理排列闭普通及共振简单主纤维；实际坏根须q0′(r_X)=0，纯主二次全λ闭。它不付一般重根幂。

[普通有限矩逆](results/R236-appendix-ordinary-pointwise-moment-expansion-and-veronese-pools.md)以φ/ψ保最高矩常数与真实域；规则保留位两族全点态幂闭。[缩放副本](results/R236-appendix-nonsummable-comparable-layers-scaled-copies-and-all-pointwise-powers.md)再容任意非可和ρ及深排序跳跃：零辅助副本任意复相位，或正副本配κν>2有理独立幂辅助，均有全有限矩池/全部固定点态幂。一般D阶池不免费给Dh阶；最高主字符零、无副本重根及ℓ1极快余族仍开。

**其他预算仍独立。** [固定盘](results/R236-appendix-fixed-disk-kernel-inverses-and-sparse-linear-deviations.md)保无限S上|a/c|≤K、L_N=O(N^1.5)、S外任意行；[辅助尺度](results/R236-appendix-auxiliary-scale-joint-resolvent-and-independent-tail-gaps.md)保r_N=εN(c_N*)²、L_N=O(N^1.5)、Γ_Y=O(N²)，含α≤1指数/长平台，存在Y∉G正相位例。旧主尺度/子支撑按各自排序半径，详见[本次前全文](notes/2026-11-13-handoff-open-before-disjoint-leading-root-kernels-1cf.md)，不得互换。

[R134计数半群](results/R134-appendix-positive-counting-semigroup-and-finite-order-entire-resolvent.md)对正非ℓ1行给真实||e^−tX||≤0.9^Θ，Θ=Σfloor(ta_j)、Θ/t→∞，全C Laplace积分准确为逆。Θ≥ct^p,p>1付整预解有限阶q=p/(p−1)，保任意有界交换扰动/复倾斜/未知限制。重排ρ_n≥c n^−σ、.5<σ<1已满足；σ1与任意稀慢非ℓ1行尚不免费有限阶。

**旧空谱范围。** [核查](notes/2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)保R134/138/155的非ℓ1可和相位缺陷first、有界扰动/首一自然多项式，任意复权/ℓ1辅助已覆盖。居中ℓ1及无空谱慢分支不在内，二次分歧根不能免费选取。

[R257/258](results/R258-entire-selfadjoint-kernel-transport-and-actual-tail-mobius-domains.md)整自伴运输不传原M点乘域/不变格；R224公共像/尾商障碍保留。

[R259](results/R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)闭同幂尾p>1/2；[R260](results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)闭排序limsup nρ_n>0的任意复行及物理重排，允许全部复first指数和有限联合解析Bell芽。其完整域导子代数无maxF成本；剩余解析分支须nρ_n→0且排序复和→Φ(0)，一般行重根另证。

[R264–266](results/R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md)已闭α≤3/2的解析Bell/简单根及α≤1全重数；R268严格扩展后，规则1<α≤3/2的普通点态全部重数仍开。

[全部广义核的实际约束](results/R236-appendix-fixed-order-double-commutators-and-generalized-kernel-isotropy.md)：仅原有界普通Bell伸缩指数上下界分支、α>0，固定阶ad_T^(2r)U_N→I强，给全部n,m的B(kerT^n,kerT^m)=0及kerT^n⊂closure RanT^m。闭广义核R全等向并在每个有限闭像中；非零必无限维真A不变空间，但未证非零/为零。这里是真实算子幂，不是点态幂；不付实像、R上限制稠密或局部等向。

**高阶导子及剩余短和。** [纯提升障碍](results/R236-appendix-high-degree-raising-band-obstruction-and-range-projections.md)给r≫√Q有界提升弱趋0；[全域双导子](results/R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)付[ad_T^(2r)U_N](C_Q^r)†强趋I、r=ηQ<Q/2、伪逆≤e^(Q/2)及carry。它不是单个导子像；1<α<3尚余Leibniz末O(N^((1+α)/4))项，两位校准排共同尺度粗吸收，α3不自动短段。

[纯等权整个高ad像](results/R236-appendix-pure-equal-weight-high-commutator-images-and-vacuum-decay.md)：C_N=ΣE_j，任意Q=ad_C^kU（不限制U/提升度）有|〈QΩ,Ω〉|≤√(N+1)||Q||√[(N!)²/((N−L)!(N+L)!)], L=ceil(k/2)。有限sl2/Casimir分解及Vandermonde自含证明；只付N+1维，外坐标系数同界。k≫√(NlogN)、池移远、有界输出⇒WOT0，排该纯模型将右伪逆吸入整体高ad后还强I的办法。未传异权/真实carry/仅未知核上的界，不声称原Bell核存在。

[全池删除背景](results/R236-appendix-deleted-pool-bell-background-resolvents-and-exact-product-gain.md)：精确ρ_n=e^−βn^α、1<α<3普通Bell，仅删O(logN)物理头，真实共同圆R_n=ερ_N^n付Γ0=O(N^(4α/3)+N^αlogN)。准确背景乘积有−cN^(α+1)+mβell N^α，合局部四次项足付；原L_j与正交伪逆端项仍未接。迟首c≈a^κ所需X圆a_N^(κ−1)过小，不能外推。

[真实核及全等向校准](results/R236-appendix-finite-isotropic-kernel-endpoint-calibrations.md)：两位Tf=0、T0=0原端配对非零；四位a=(1,2,3,4)、r1<Q4/2有全E不变全B等向核子模，端配对仍35(1+2i√3)/819。故全等向也不付通用正次T0因式，P不保核子模；必须用额外实际无限结构，有限模型不是原Haar核。

[原P的真实距离/共轭](results/R236-appendix-orthogonal-range-projection-distance-and-dyadic-conjugation-cost.md)：任意复加权不交creation块，P=Proj RanL^r到完整A′的距离≥√p(1−p)/(1+κ)，p为第一块r层占据概率、κ为准确carry乘积；等模p=r/N。A^−2^ell P A^2^ell对固定块先证全域有界，再给连续等权池log范数≥770(16^(m+N−r)−16^m)/15+½log(r/N)−½log binom(N,r)。固定比例时不可并入exp(polyN)，多位打包不消除此成本；有界实现的小扰动同有准确下界。N→∞且池移远可强I，与范数障碍相容。不排核内新配对/其他预处理。

**旧快类须扣除。** [范围核查](results/R236-appendix-existing-fast-classes-for-supercubic-sorted-rows.md)已闭α>3的普通多项式/主理想及普遍表示；α=3保首阶r对应β>80r⁴/3与β>400r⁴两种充分范围。单个四次幂界不等于G。

**实际超指数临界余族。** [真实成本边界](results/R236-appendix-summable-superexponential-critical-budget-obstructions.md)：居中a_j=e^−β(j+1)^α、b=0、c0=0/cj=a_j^κ，3/2<α<3、κ>2，非零F2+v_c只余λ0。任意双N池d_N≤Cρ_2N，原平均实际绝对coeff≥(8ρ_N)^−r亦超预算。正锥半群/快carry给Y∉G、Γ_Y(R)≥c(log1/R)^(1+1/α)，原R=ερ_N^D须≥cN^(α+1)>N²。未证核存在、不循环或核内逆同价；须真核关系/新输入。

[迟首核的同一正两行见证](results/R236-appendix-late-support-quadratic-kernels-and-positive-joint-first-annihilators.md)：对有界未倾斜a,c∈ℓ1、j0=min supp a、c_j=0(j≤j0)，T=X²−B0+Y≠0若kerT=M非零，则存在某dyadicζ、真解析Hζ(0)=0，使S=X+Hζ全H单射稠密但N=closure SM真小于M。同一h∈M⊖N、ρ=h⊗h准确湮灭SA′、TA′和(Y−B0+Hζ²)A′，真商πX=−πHζ、πY=π(B0−Hζ²)。真实gauge差=2DζS，Dζ解析A幂因子才可删；有限稳定子/全支撑向量/Fourier注入完整付。若能造联合理想中的非零G快证书即矛盾，尚未构造。首翻ζ0只在额外配对非零时化S为主尾，不能从存在ζ指定ζ0。近共振B0=Σa²Q²已快，不重造a²慢尾；c=aκ只在j>j0，全j写法须加有限首项。新正ρ固定阶/小迹尾工具可用，但同一ρ不能跨不同ζ。

同稿§6.1–6.2补准确全右接口：G=B0−H²、Z=Y−G，T=S(X−H)+Z给SA′+TA′=SA′+ZA′；任意整F有F(X,Y)−F(−H,G)=S U_F+Z W_F，实际范数积分U_F/W_F∈Acal。故同一φρ对全部R∈A′精确替换，尤其||φρ(e^(zX+wY)·)||≤τ||e^(−zH+wG)||。R151零字符G类的正τ4付exp O(log^(4/3))及混合矩e^(−c_Hp⁴−c_Gq⁴)。G不被误称真解析芽，未提升商逆/删左反射源；下述固定正态反例说明这些必要增长界仍不足以替代准确零式。

[实际全右测试的增长障碍](results/R230-appendix-fixed-positive-normal-state-and-fast-entire-growth-for-all-commutant-tests.md)：对3/2<α<3，有同一个固定h∈L∞、h>0 a.e.、Ch=h、||h||₂=1，使任意有限族系数O(e^(−βj^α))的u_jN_j+v_jQ_j+w_jQ_j²，在全部actual A′单位右测试上联合整指数泛函范数≤exp[C log(2+Σ|zν|)^(4/3)]；固定零常数多项式亦同。因此同时覆盖P_a/X/Y/B0/二次组合，只凭正正常/秩一/full support不能迫更高增长。软数目窗固定，实际全尾近交换投影距≤6e^(−77016^m)||R||，m≈loglog参数的早头及Duhamel全部付费；纯窗旗不属实际A旗。仅有限4/3 type，未证任意小type；此态未构造任何联合湮灭式，准确三零式/真核结构仍是剩余接口。

[R270第六附录](results/R270-appendix-disjoint-slow-point-polynomial-products-and-head-masks.md)：物理不交慢模式的已知点态循环因子可相乘，故∏(uν−λν)^mν e^w循环。mixed词域/Bell已付，共享有限头仅保单atom；同模不同根、atoms之和不能这样相乘。

## 1–3. 一般向量、限制值域与有界交换子的开放接口

旧完整范围及原稿链接保[本次前全文](notes/2026-11-13-handoff-open-before-faithful-hard-projection-limits-1cf.md)：R101只有限Walsh次数两端；任意L²循环性、未知核的gauge差像、双独立慢模式仍开。R125/128/140的全H共同正则/核心不传未知限制，R176仍许单点拟幂零部分。R32代数无零因子、R88有界逼近不付纯乘法；R143最大商图仍需实际域及分母有限放大稠密，R124零余数不付再除A。非标准主理想分类及一般A′核仍开；R256仅分类有界加权复合交换子。其余Lp/Orlicz、平滑/非零交织和各例外不变。

## 4. 相对乘积、多项 cocycle 与混合解析芽

**R150 已闭范围与下一缺口。** 原 Newton/剪切全部中间条件与直链保[本次前全文](notes/2026-11-13-handoff-open-before-positive-heat-anchor-threshold-and-strong-units-1cf.md)。[首一 Newton](results/R150-appendix-nondegenerate-newton-edge-all-point-powers-and-one-empty-anchor.md)、[非首一](results/R150-appendix-nonmonic-second-variable-fixed-sylvester-and-point-powers.md)及[中间带](results/R150-appendix-intermediate-shear-degree-band-and-all-point-powers.md)保各自空谱锚/横截/权次条件；[跨根簇](results/R150-appendix-disjoint-leading-roots-cross-kernel-exclusion-and-real-structure.md)保最高边互素和实结构，非实仿射直线方向已在内。未覆盖的重复/零根、切向、双全C继续。

[实际有限jet/Bell](results/R150-appendix-finite-logarithmic-jets-vandermonde-tail-cancellation-and-polynomial-cyclicity.md)：原log幂的M逆第r行尾S^−r/√n；权分量D−d0<ν_D给Q(F)e^w（d0>0全非零Q，d0=0限Q(c0)≠0），全相消D<ν_D付Q0≠0。Lagrange族普通简单零点可有任意R阶jet、允许D<R；旧多尺度/高重/临界Newton范围保。[端点外盘](results/R150-appendix-critical-contact-endpoints-real-middle-head-exponentials-and-uniform-exterior-disks.md)给D=2m统一R_G外全部Q/幂/w。弱jet端点单位、盘内/λ0、一般行与无限模式仍待；非线性余项不得当first。

[R189空谱锚](results/R189-appendix-one-empty-anchor-two-additive-direction-kernel-elimination.md)付快系数G[X,Y]单射稠密及总增量类秩≤2含空谱组合的情形；双共振全q保，三独立类/双全C及新子商范围仍开。

R127已闭相对ℓ¹两乘积；复杂相位相对ℓ²、三以上cocycle、非解析闭包/一般有界商仍开。R129/135单轴、R146/148单慢加快、R152有界加性及R153快分式各保原范围，超越分支未普遍限制dense。

R160慢二阶Bell不自动属G；R77/79/82临界中间参数及R83芽/轴谱仍开。R162纯虚倾斜不保乘法，指数权点态循环不扩任意H向量。

仍可寻找固定单射R∈A′使所有非例外ζ有B(RM,UζM)=0：此时closureRM非零且含于M即可用R122，无须先dense。当前辅助因子依ζ变化，可数全H稠密像之交不自动与未知M非零相交。

## 5. 一般 ISP 的独立路线与不能省略的障碍

R5/7及Rota一般归约、R2/17/18紧修正、R4/6观察拟仿射、R8/114/164/165旧紧化各保原缺口。R105/107已核PPP/MM/AT/AM原条件，未得到本候选普通不变空间；JKP2019完整正文仍未核实，Tucci迹结论也不自动转到Haar；下面的纯子类另有直接证明。

[R113](results/R113-pure-tail-dominance-and-carry-obstructions.md)的相对尾≤1/2及端点/几何旧范围已扣重。[R236纯模型补全](results/R236-appendix-pure-summable-row-kernel-exclusion-by-local-nilpotent-derivations.md)与[张量笔记§15](notes/2026-11-12-tensor-kernel-0c-agent.md)现证明任意无限支撑复ℓ1纯first单射稠密；T=4P_a²−2P_c、a/c∈ℓ1且至少一行无限支撑亦然，覆盖纯κ>2及全部α,β,κ>0指数例。无限c时谱单位偏导给固定阶强ad单位、有限头ad精确幂零，非交换因子有序Leibniz与局部全配对完整支付；有限c用尾平方及有限三角回传。实际局部导子不为零，巨逆与carry仍须同付，R113两类carry反例保留；原实际迟首κ>2及普通ISP未闭。

[R12紧回传](results/R12-appendix-compact-sandwich-limit-and-backward-orbit-cost.md)付全部有限旗紧夹积/S_p极限||K||/2及liminfηj||J_(2^j)||≥||J0||/2；[自伴链](results/R12-appendix-schatten-sandwich-and-selfadjoint-backward-chains.md)酉等范数，紧起点不可能。FJKP2004有界链失败、Thm3.7仍须全整数；外部紧交织开。

[R14硬谱截断](results/R14-appendix-hard-spectral-cutoffs-adjacent-quantiles-and-noncompactness.md)核FJKP2005指定强收敛入口：任意固定f/非退化θ的s_n全指数有正强距离；相邻λ比零时t_n亦如此。[精确弱极限](results/R14-appendix-adjacent-hard-projections-faithful-weak-limits-and-exact-variance.md)给该子列任意f上(P_(n+1)−R_n)f→0、低谱质量→θ²；faithful f再得两投影WOT→θ²I、s⇀(1−θ²)f/t⇀θ²A*f及精确正方差。保开闭端点及满支撑边界；有正测度零集者全空间弱标量极限仍未付，逃逸目标/退化θ/其他方法仍开。

[family293审计](notes/2026-11-13-family293-hyperinvariant-scope-and-backward-normalization-audit.md)仅超不变结论，纤维有普通真尾空间且交换子非交换；Domar不同权不能借R88或反向归一改成普通反例，未重编Lean。旧完整条件保历次归档。

## 不能互换的极限

全部混合自然词域不保普通系数截断；可数first核心及固定正则子在子商单射稠密，不使原词普遍dense。非零有界交织不能把全像送入全部first域；R204重选行不代固定慢行或边界运输。实际域、carry、非零锚仍须支付。

[R239首位图](results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)/[横向压缩](results/R239-appendix-coercive-adjoint-and-positive-mixed-compression.md)保C²=η₀N₁|L、||C||<1/√12，真缺陷需C*Gx=0及C*x=−η₀(N₁|L)*Cx。核上T*≥7/8、Re(P_MBT*|M)≥5α₀/6，给M⊥内横向同构而非BM原像；各位压缩约束仍未排缺陷。详式和度量字典在原稿及本轮归档。
