# 增长头完整核观测前的 open 全文

日期：2026-11-13 19:24:04 UTC；main d07162b0b44a9963bf33cbf565a2e6466a617de6。保留全部精确范围与既有归档链。

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

截至本次同步的H/open全文、全部精确范围及既有归档链保存在[本次归档](notes/2026-11-13-handoff-open-before-faithful-vacuum-support-0c.md)（main 1f182bb29b562867bf23d24c9ec25bc6530ecd48）。本页压缩已付接口，未列出的旧缺口并未关闭。

## 当前接口一：原 Haar 慢符号的正常湮灭者

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**已排范围与未付部分。** R235/R237/R255已排连续/a.e.+双边UI、保函数非负锥、Walsh对角/有限带/entrywise-ℓ1、合格乘积基块正态及E_√3范围；一般正常正有限秩仍开。R228的C平均可保同泛函而增秩，R229不许一般秩一纯化。真实右矩仍须ε_m||G_m||→0且φρ(T_mG_m)/h_m不消失，普通L²逼近不付此预算。完整原稿链接及端点保本次归档。

**最小正秩的逐对域、商与源预算。** [模与两行域](results/R230-appendix-minimal-positive-rank-module-compression-and-pairwise-common-domains.md)给dim(E∩ΣA′g_l)≤k；Pg=1的全域正则源恰A′g。两行Ri即共同真空/交叉域失败，原域及主理想不可比较；低放大插入链给原正循环商πRi/j=0、Di/j单位，不传整个交域商。[逐对比例](results/R230-appendix-minimal-rank-pairwise-ratio-spectra-and-common-denominators.md)使任意最小r、仅两行有Ri时所有中间比例图广义全C谱；假设逆迫最小=最大再造共同真空分母。旧共同奇异核心/紧扰动全近似谱/两侧非半Fredholm仅扩范围，不付高秩严格图缺口或pencil真核。

[聚合转置预算及统一阻尼](results/R244-appendix-aggregate-transpose-source-budget-and-exact-dual-cost.md)：真慢湮灭的正ℓ2负权/heat预算发散及WOT闭包已付。误差→0且保锚迫聚合源∞/归一弱零；真h_p误差≤√δ·尾像≤δ||R||，压源保锚费η/δ。仍欠共同图或巨大尾放大下专属有效源，不替v_p。

**变化源/尾耦合。** R230逐对源成本Ci(ε)有限但发散，τ≤Ci(ε)²η²+Cj(η)²ε²，第二小成本≥√τ/(√2ε)；纯幂上界要求βiβj≥1。必须同付εK_m和ε_mCi，逐点有限/连续凸也不保证可选子列。k<r近似生成的完整误差下界、附加生成费、无真空版本均保原稿；尚无所需统一上界或共同图。

[原正密度的全头矩](results/R230-appendix-first-walsh-observability-and-canonical-positive-head-moments.md)：v_m=Σ_(F⊂m)(−1)^|F|φ(V_F^[m])χ_F准确代表整个头代数，K_m(v_m)=τ、||v_m||≤10^(m/2)τ。真慢理想湮灭迫范数∞/归一弱零，固定实际p的头差全付；真实全行擦除与v_m范数差→0。旧145/73稳健观测保持有效，且被下列平方估计加强；未把头测试直接放进ann。

[同一规范头源的全部强残量](notes/2026-11-13-canonical-head-positive-normal-sources-and-simultaneous-strong-annihilation-central-review.md)与[真核交叉源](notes/2026-11-13-kernel-supported-positive-density-and-strong-truncated-source-residual-normal-complex.md)：正reset密度使完整v_p的Φ_vp在全A′_*范数趋φρ，误差≤τD_p+2δ_p+2√τδ_p且均值恰τ。若φρ(ZA′)=0，实际/局部C配对付||Zv_p||≤τ(2K_p||Z−Z_p||+||Z||D_p)，无需ρ支持kerZ。同一个联合ρ的S/T残量≤C10^(p/2)(e^(−βp^α)+pη̄_(p−1))，Z=Y−B0+H²残量保更快κβ指数；B0真carry与H解析头差已付。真核cross h_p另有||Th_p||≤Γ_p√τδ_p、Φ误差恰δ_p；不混同两个源，不由小残量推出距核、有界源或理想证书。

[混合高阶强残量与正密度HS幂](notes/2026-11-13-canonical-positive-sources-mixed-power-residuals-and-polynomial-budgets-normal-complex.md)：实际头与真实尾分开后，同一v_p满足||S^kZ^l v_p||≤τ10^(p/2)[C^(k+l)e^(−β(k+κl)p^α)+C(p+k+l)B^(k+l)η̄_(p−1)]；全部变化多项式另保绝对系数/导数费用。T=(X−H)S+Z给二次混合幂，不把其余项当纯尾。真Tρ½=0还给||T_p^n ρhat_p½||HS=||T_p^nρ½||HS≤√τ(r_Tp^n+nM^(n−1)εp)，εp纯carry；n p^α=o(16^p)仍保完整指数。准确阈值投影Pp=1_[0,sp](|T_p^n|)有Trρ(I−Pp)≤τ(b_p/sp)²，仍须付b_p=o(sp)且Pp在原表示强零，不能以维数或相似替代。

[R236实际MP与容错目标](results/R236-appendix-exact-head-vacuum-column-and-carry-cost.md)：§§4.2–4.5保exact真空/固定柱的全部允许q正16^p成本，只排所选充分预算。§4.7令H=2^n,h=p−n,d=rq，删每H块末w=d+r(h+1)<H，则||GQ||≤C^(q+h)L(L+1)exp[F_n(H−1)+(d+rh)ell_n]；完整majorant/最高位付所有卷积与carry，q+h=oH给源type≤35/6·16^n。固定比例Q的非零WOT锚足排真核；有限ℓ1 N/Q/Q²行固定P亦可（首阶有限非零）。§4.8固定dyadic目标提升为统一有界实际Θ_n；C转置/Ω忠实、Kp/Dp/真tail^q全费付清则实际理想有bounded strong*单位，排一般正常ann，联合row原像同样成立。α>3/三次大β扣旧；临界便宜联合原像、非坐标目标/真见证残量仍开，上界不够付不等于成本下界。 §4.9同一ζ/ρ的T与γT给真实单层相位单位、完整Schur最小式和全目标源，q1 row MP上界type≤35/48·16^p；只删全头末r目标，低carry全付。尚不付临界tail，不自动扩q次或迭代。 [联合高幂新稿](results/R236-appendix-joint-gauge-row-powers-and-carry-corrected-targets.md)用同一D_F只付一次eF，全部rq<H保rank-r接口和剩余d−r边界的精确carry目标修正||K||≤4^q eFχ，type−245/3·16^m；q=oH源type降35/96·16^p。q1覆盖完整row像，高q只指定目标；固定dyadic锚与实际Kp/Dp/εp/tail^q全预算保。单层仍不付慢尾，多层度量续。 [周期物理度量](notes/2026-11-13-periodic-physical-metric-positive-congruence-and-fixed-normal-energy-normal-complex.md)付全H ||D_m^-1AD_m||=ρ_m且高N_j不变、C反向与同gauge；正密度须双侧合同，ann行变D_m²S♭，单位锚变D_m²。每个固定非零正正常ρ的TrρD_m^±2准确type35/6·16^m，归一锚付负同型，不能凭固定正常性省此度量费。其他源/度量仍开。

[吸收路径完整源](results/R236-appendix-absorbing-walk-full-sources-and-original-metric-target-guards.md)：精确全树保所有未剥尾、层费κ、路径面积/q!及早吸收质量≥7/16已付；两尺度仍只为条件预算。§§9–10进一步关闭整个完整首列具有首达good支持的解析目标桥：公共池后任意算子权有(4/√15)2^-q上界；任意实际good首列经完整Walsh列与dyadic前缀次数分解，得4√2e^(-q/64)(1+2M10^(M/2)ηbar_n)，纯界不含池宽。故n,q→∞、M=o16^n下全部归一目标一致WOT0，包括路径停止后仍在共同池内的任意实际A′尾权。[尾真空分离与修复费用](results/R236-appendix-faithful-vacuum-support-and-nonuniform-column-repair.md)补足精确范围：任意有限头投影P上，(I−P)GΩ=0等价于(I−P)Ge_M=0，故单向量的精确good支持已经足够。近支持仍不足：实际G=I、q=n/M=n⁴的完整坏列O(n^-1/2)，均值恒1，唯一解析修复范数≥(1/(4√2)+o1)e^(n/64)−1，距good解析空间趋1。真正仍开的是无该精确支持的算子值目标、完整联合尾理想及有预算的来源特殊修复/非零正常锚。

**高矩与迹尾。** R230已付实际平方选择器、完整二次矩谱范数和所有固定阶张量injective范数；真v_m的低层/稀疏族归一质量消失，但全低次数消失仍需额外范数增长。正常态固定次数矩只得c0和o(m^(k/2))，不免费平方和。正Walsh截断保真实小迹尾δ_Λ、源误差和均值，hp费≤2τ10^(p/2)而δ无速度；不把正尾当新湮灭者。完整有效秩、重叠组合费及相对层质量条件保归档与R230附录。

**远尾/热过滤。** 纯远尾及固定Walsh头擦除若carry×聚合费→0且保锚，所得源仍发散/归一弱零；一般纠缠另付近纯误差。正热过滤有界ℓ2球的全族真空源成本一致发散，未由联合三零式构造低费源。非UHF强单位R267、固定QAcal强*密度R237均不自动付慢分母或闭词域。

**相位路线。** R253迫真见证q_m↓0；R230多重Fourier/双除法已排周期r≤q/100、总deg≤q³及独立exp参数≤q⁶的指定复杂滤波族，费用/相对carry全付。非周期、超预算、真实密度专属配对仍开；固定非湮灭态反例不能当真湮灭者。R242窄图/R250稀疏图尚未给A+不变；R210–211奇异态不作Haar正常态。

[平方根次数联合关系](results/R236-appendix-square-root-degree-joint-head-relations-and-actual-tail-targets.md)：H维共同头给D≈√(2H)的非零P，实际U/V源、头carry及完整复系数Vandermonde下界已付。a_j=e^(−β(j+1)^α)、c=a^κ、1<α<7下，实际norm1尾目标到(S,Z)理想的距离→0，归一源费expO(H^((α+1)/2))。§§7–8用全系数恢复、相对截断宽O(k^(1+1/α))、数目窗及逐度收缩，现已无条件证明整个关系族一致WOT0，真空比≤Ce^(−c n^(1−1/α))。更一般degP≤C2^(dn)、d(α+1)<4有效，也覆盖总次数同预算的任意两模式多项式右因子。这一族不能再争取非零弱锚；不据此排核。真正未付的是任意实际尾/完整A′算子值右因子、全部最大子式及完整联合尾理想的正常锚。

[算子值Walsh首列与完整联合尾交](results/R236-appendix-operator-valued-walsh-column-lifts-and-joint-tail-ideals.md)：对任意尾向量V_F e_n=χ_F⊗I，得到M_H(B_n)→A及M_H(C_n)→A′的真实首列提升，完整tuple费用K_n=10^(n/2)，忠实列与左模性质付全算子身份。全部矩阵列源inf与实际右因子费用相差至多K_n；全部最大子式因此有合法实际源，费用K_n H! M^(H−1)，不能直接用矩阵系数测试正常态。首阶一时S=C+ND,D单位，完整尾交准确由(G²−ηNnext,E−GF)生成，范数闭包/full A′版本均付，同一正部分迹保。单位逆费用与q_n一致正下界仍开，不将每层非零当非零统一锚。

## 当前接口二：实际边界的除法饱和

固定两个实际边界T_N/T_Y，M=kerT、N=closure BM、D=M⊖N。R187/200已给各有限稳定像及M∩RanB^r⊂N，有限孔核仅真空；真正问题是**无权核内稠密与N=M**，不将环境有限孔稠密当核内核心。

**全整数窗口和真正最小Gram。** [R239全q](results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原进位，低投影e−74d⁴/真实lift e−75d⁴；d≈log^(1/3)q、K*=3(16/770)^(1/3)。c>K*权核入N，真D尾常数K*/2，权阶先属R271。窗口ell=d+m的Σ1/[ell(1+λ²)]发散足N；真D倒能量≤8τ_Q²/||w||⁴。λ²=O(q log^(2/3)q loglogq)足但未得。

[准确Gram](results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)为G=D0P_kerS D0*，严格正；实际r=Avq自动D^d，λ²=〈G⁻¹r,r〉。Schur补不可省；窄带正/倒能量仍容慢尾。逐头单块残量/旧d核阶及Tr(ApKp)非零保原范围。

**旧成本范围。** R234模N已闭，R238原J_q成本不代模N成本；环境坏见证在M⊥，横向T*M非BM原像。局部最优logΛ_q=Θ(log^(4/3)q)、原始块消去、双宽窗、三维分支、近一次短旗、固定比例q^o1预算都保原范围，未给统一无权能量；T_iw不保W。完整旧公式和链接保本次归档。

**已否环境捷径。** R239原权Vandermonde x∈kerD²且||D*x||²=S_(m+2p)→0，排h≥2的通用同旗gap；环境D*D+DD*正隙不替P_kerD²D*。原外出生σ经D3桥正交该坏族，但F5=D5DX非零使B2/H2不保外桥核。实际σ=V2Q1^-1V1B0^-1g0更窄，尚未得其低费原像。全尾D3逆还必须付J^5.5级及高次方差下界；廉价环境像不能自动入M。

[边界源接口](notes/2026-11-13-1cf-established-scope-and-domain-limits.md)与[两侧窄通量](results/R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md)保原lift窗、同BA规范/a_two已付carry及D3新Gram交织；最终仅P_W，未证Kq(N)⊂N。[高孔观测](notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)付首头零返回Γv=−a10，无D†范数；§§7–8另由既有有限核lift付1≤p≤d−1全层图核坐标，C²=1+Σ||c_j||²(p)_(j+1)S_m^(j+1)，单孔余量强至δ√(1+S_m)；增长p的头费用/高孔仍开；S_-*v_<q所在横向块未控，是[环境滤波](results/R271-appendix-finite-head-frequency-filter-and-polynomial-environment-gap.md)的全L/L*多项式gap不能替真实Schur的具体缺口。仍欠原窄barf的新费，旧σ不可替。 同[高孔note](notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)§9另付全头primitive源的K_j* cflat=PkerD^d(D*)^j v_j及真实全链C_mj；2j+1≤d方可去投影，不付高创建逆/一般µ或把flat换α。 §10以原N/Y双dyadic近核和同一primitive Vandermonde补集，在合法最大q给µ=1、指定归一观测平方exp[−(3/16−o1)d⁴]；只排这组量的温和反向重建，未给α/λflat上界或三Gram反例。 §11对同一源以远尾相容真空原像支付真完整旗链，λ(r)≤e^(−d⁴/9)，µ=1由完整Fflag配对迫λ(rflat)≥e^(d⁴/9)（渐近指数79/512）；未界裸α或认作实际W来源。 §12以完整C_T族给任意原源C_T*cflat=P_(H_T⊗K_q(I))v_q及真B_T^-1/2正投影能量≤λflat²；原近核h_m投影≤e^(−d⁴/9)λflat，未覆盖低孔bulk或随意搬动primitive投影。 §13用完整有限L核跨q切开，准确付全部左孔的prefix primitive投影P_Uv及双侧Pythagoras；同近核头投影平方≤e^(−2d⁴/9)(µ²+λflat²)，无q/T重叠费，该节保留尾位置投影。§14从同辅助头R_t减primitive输出，付顺次真单步MP的2^(t−1)L^t线性阶费用及全尾正交；现原h_m⊗kerD全部低孔投影平方≤e^(−d⁴/10)(µ²+λflat²)，已去prefix/vacuum，非primitive/其它头仍开。 §14.2.A一般kerD^s的顺次单步MP费用也只付一次核阶，未变成(D^t)†。 §14.6原完整逐头lift直接给W上同一h_m⊗kerD≤q投影≤2e^(−d⁴/20)||w||，无须v≈w，未排其它头或非primitive质量。

[实际头理想段移](results/R239-appendix-actual-head-ideal-shifts-and-two-sided-flux-transport.md)：Q=N_j^[m]、r=2^j、q+r在原合法窗，H_tQ=QH_(t−r)准确。旧右末r段全杀、旧左顶r层逐头D核旗保留；减真正左最小者后仅余与完整输入空间正交的有限L核。因此完整D_q⊕I运输收缩，Q_H*Htwo_q^-1Q_H≤Htwo_(q+r)^-1，最小物理原像差给准确正能量亏损及原lift的W投影小量。同一ξ的barf_q(N_jξ)−Q_Hbarf_(q+r)(ξ)在Htwo_q^-1度量≤e^(-71d^4)||ξ||，最终W运输≤e^(-70d^4)。N_jM⊂N不能免费推出K_qN⊂N；尚无窄源左费上界或N=M。 [全左核primitive坐标](results/R271-appendix-full-left-primitive-coordinates-and-boundary-schur.md)现给Ecan双射与Dcan=I+C_L*C_L；最后d−1个primitive孔层的准确Schur D_eff≥I，J=B1D_eff^-1B1*、µ²=<D_eff p1,p1>及D_eff p1=−C1*cflat。低部由p0=−D00^-1D01p1重建，非primitive成本未删；需界原D_eff的实际大小。 [孔带宽/Schur局部化](results/R271-appendix-primitive-bandwidth-and-far-schur-localization.md)付Dcan带宽d−2、顶q层单位块及真实J_q的primitive源正交分裂；远低部消元对最后d/8个primitive孔层的修正≤e^(−2d⁴/5)，极小低补全≤e^(−d⁴/5)。一般原源的中间边界坐标和完整bare/flat比较仍保留。 [源jets与全部自由旗](results/R271-appendix-source-primitive-jets-and-sequential-right-chain.md)进一步精确对角化约束：P0D^k r=(−1)^kA^(k+1)p_(q−k)，kerC_R=kerB为明确低孔/头旗；强制σ经一次真实Schur给S_src≥I、µ²=<S_srcσ,σ>及S_srcσ=−C_R,T*cflat。跨界链准确为同源R_seq，bare与full仍是两个不同投影；待估S_src相对这两个费用。

[实际二形式求和门槛](results/R271-appendix-actual-source-two-form-ratios-and-legal-window-summation-threshold.md)：真实c=<La,a>/(||a||²+µ²)迫非零W的(1/d)Σ合法q(1+c)^−1→0；实际a、同BA最小a#或已付a_two上C_m=O(e^(d³/4)/d)沿无穷头子序列足N=M，比较仍开。[回文四头](results/R271-appendix-palindromic-four-head-actual-minimal-sources-and-two-form-nonuniformity.md)的11尾/q1混合源左费1、裸费→0而比∞，但规范差liminf²≥3/68；§9完整有限规范类反有µ≤24α，独立ε/β。§10另付全部有限源µ≤49α+25λflat，即J≤3026(J Jbare^−1 J+G)；仍不外推原高孔合法窗。

相邻序仍缺任意有限正权全出生/全高度及原高孔窄源的比较。[全矩障碍](notes/2026-11-13-1cf-established-scope-and-domain-limits.md)与[分子障碍](notes/2026-11-13-penultimate-beta-denominator-separated-roots-and-schur-obstacle-1cf.md)已排全Hankel/独立P·H正矩入口；[有限—原尾归约](results/R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md)仍须全部有限权型。

[四异权全出生](results/R271-appendix-four-exceptional-weights-full-birth-uniform-primitive-gram-bound.md)付四任意正头+等权池的全K_s相邻Γ≤16/真实首降≤64，M≤3严格9/4并含任意五正权；不能代普遍连续尾。[q−1固定块内部](results/R271-appendix-penultimate-primitive-interior-adjacent-uniform-bound.md)有Γ≤4/下降≤9，粗端q²仍保；[低边释放](results/R271-appendix-low-edge-degree-release-schur-cost-and-exceptional-sources.md)保j=δ−n−1的C0≤q(q−j−1)/(j+2)、完整ZS^-1Z*及异常秩，Z*Δ_C^-1Z≤S和实际窄源落点仍开。

[任意正权出生一首尾](results/R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)付有限整个K1严格Γ常数1/真实首降4与倒数末边；任意正ℓ²无限行首边逐行c<1。原尾m≥46首降<2且最佳趋2。[内部稀散首稿](results/R271-appendix-dilute-birth-one-all-height-precision-and-square-root-window.md)的平方根窗已由[根交错加强](results/R271-appendix-birth-one-root-interlacing-precision-and-linear-tail-window.md)提升：仅(h+1)δ<1，实际相邻h/(h−1)乘exp[±13(h−1)δ/(1−(h+1)δ)]；原h=o(m)全窗一致最优、h/m<c<1/3统一有界。超此窗/高出生实际源仍须另付。

[全出生低占据Gram](results/R271-appendix-all-birth-low-occupation-bosonic-minimal-gram-comparison.md)：(2s+h−1)δ<1时，完整幂最小逆H_(r,s)夹1/(r!S^r)和1/(r!S^r B_(s,r))，B=∏j≤r[1−(2s+j−1)δ]。真实相邻常数夹h/(h−1)B_hB_(h−2)与h/(h−1)B_(h−1)^−2，原H_*(S_*+H_*)/m→0多出生矩形一致最优。玻色空间只用于primitive前向范数，再由全部原像对偶付真逆；该完整幂Gram本身不付跨出生夹角，原高孔源仍超范围。

[完整canonical双塔](results/R271-appendix-bosonic-dual-fock-tower-and-quadratic-collision-conditioning.md)另以真玻色不同出生正交/两项collision付W*W∈[1−ε,1]，V=(W*)^-1准确等于旧顺次MP塔，ε=(4/3)δP²<1时其整个条件数≤(1−ε)^−1/2。平方根前缀应用只属旧R239近线性q^(1−o1)范围内的另一证明；真正新增是全塔P²δ预算。继续受限短核旗的相对collision和实际高孔费用。

[R239首段边界先消元](results/R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md) 保同一对偶z，G°=S PkerF S*只改首出生；裸源a≤β+e^-72d⁴||w||，L=BA*(H2°)^−1BA≥0。准确λ²=||a||²+<La,a>、旧E2=<La,a>+||La||²、λret²=||La||²+<L²a,La>；旧σ换新逆另付完整λret²。完整D3同窗kerF校正、实际Aq交织和U/J正缺陷均保原carry，不能用X_M*w=0杀Aq*LAq w。真实g=u+ahat∈kerF到内部最小像只差e^-74+e^-75，§9.6三正交分解及§9.7左右Gram字典保真实barf与已付rsmall/rflat；原La/rret上界未得。

同稿§§9.6—9.7以实际未来向量给η=J*ubar、P=I+L、Q=f*Jleft^-1f；A*η重建w至τ_q+carry，P^-1/2η由β付，原X_M*w=0给真正相邻伴随约束。rsmall=fP^-1η与rflat=fP^-1Qa在完整λ中匹配至carry，且rsmall=−r+F S†barf、a+P^-1η=BA*H2old^-1barf；barf必须保真，不能换σ。U*PU及U*QU均≤s3²对应下一层度量；仍欠P/Q的有效比较与原返回费用。

**有限权比较的已付范围与当前目标。** [本次全文归档](notes/2026-11-13-handoff-open-before-faithful-vacuum-support-0c.md)保留各固定块的全部常数、整数证书、短池/最高逆及原稿链接。完整全Hankel、出生阶乘正矩和单个二次残差的普遍充分性均已被反例排除；这些反例不否定真正完整相邻序。

- 两异权及三异权加任意等权池的整个K_s、所有合法高度已付严格Γ_nΓ_(n+1)^−1Γ_n<Γ_(n−1)；三异权t2还给(n+2)/(n+3)。四异权全出生的统一16及四异权整个h2的严格1保留。不能外推任意多异权或连续尾。
- [两种权h2](results/R239-appendix-two-weight-groups-full-height-two-sharp-primitive-gram-bound.md)、[h3](results/R239-appendix-two-weight-groups-full-height-three-sharp-primitive-gram-bound.md)、[h4](results/R239-appendix-two-weight-groups-full-height-four-sharp-primitive-gram-bound.md)已覆盖任意两组重数的整个K_s；h2统一<1/2，h3<2/3，h4端<3/4/中<2/3，全部最优细分常数见原稿。**一般h≥5的非饱和双串仍开。**
- [任意独立头的饱和线](results/R239-appendix-saturated-primitive-two-sided-weight-count-constants.md)在所有h有准确Beta混合及按强弱权数的双侧sharp常数。该混合不自动覆盖非饱和块。[全权倒数对偶](results/R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)保真实全逆/同余，但不自行给相邻序。
- [任意短池完整MP](results/R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)§§10–11保homδ源、全部低次修正和两端非法状态；L=0也含一般有限模型。全部权/全部出生仍须真正矩阵比较。
- [方差与完整τ](results/R239-appendix-penultimate-primitive-rank-variance-and-central-unit-bound.md)保一般中段窗口、Θ精确平方分拆；h2一次源的必要充分条件仍含完整τ。§9.9已消两个端点，τ=q/(q+1)·1*[K−K(K+Σ/(q+1))^-1K]1，K=V0−B0A0†B0*；真实Σ逆、q−1平衡约束及秩亏必须保留。单二次测试失败不替完整τ的下界，当前继续实际外场结构。

[R239两异权四矩返回](results/R239-appendix-two-exceptional-tail-four-moment-return-geometry.md)：仅池出生j=q有高返回；L≥d时full/bare费准确对应同一y递推/逐孔自由末矩，保原A/旗。固定A、a=b=R→∞排普适L_eff²≤C(I+Qminus)，该族线性界仍保。§6另以Aε边[1,ε,ε]、固定小a=b=δ、池ε，得µ²=1/bare有界而full≥cε^-2，排仅维数/范数控制的任意头线性界。头随ε变；两个原指定头/真实窄源未被排，须用其结构。 §§7—8付完整逆字典I≤C(Fbare+Ffull^-1)，以及d≥8回文头/固定小尾的真反例：µ=1而α、λflat均O(t)，全费用矩阵真对角且源已规范。仅加反对角对称不足；该单步头跨格通量为零，不能代真正原长跳跃及窄barf。



[真实尾理想](notes/2026-11-13-actual-tail-ideal-defect-compression-and-preimage-distance-boundary.md)核两边界同一B：X_m(c)M⊂N，||P_M D_m(c)*P_W||≤Σ|c_j|η_j。三次尾≤s3e^(−770d⁴)。准确配对另有s3 dist(原像,M)，最小原像只降范数、不自动降该距离；真低核/Schur后源仍须付此距离与无权能量。

[双宽实际源投影](results/R239-appendix-double-width-head-flux-projection-and-exact-energy-drop.md)：同一m,q,r，宽d/2d真极小链满足P_Zh=c_d−c_2d，Z=kerL∩H_[q+1,q+2d]；靠准确新头旗P_C2d g=c_d−h、g⊥Z证明。C̃tot模Z的最小范数恰||h⊥||=√(||h||²−λ_d²+λ_2d²)。原lift去P_Zh只付e−75d⁴||w||√(λ_d²−λ_2d²)，给E≤β_2d||h⊥||+4e−70d⁴||w||√E。〈h,c_2d〉负不允许把w替换为c_2d；未给h⊥上界、能量下降率或越已付lift的迭代。

**完整L核与窄通量。** R239将各真实短核h_t拼成K(h_t)，支撑[q+2,q+2d−2]、费≤e20d⁴并由原lift入N；已知像的D3最小逆只降本身范数。实际正通量仍保Ctilde_tot全合成费用，不许将w换成最小链；同源c_d/c_2d投影只得到精确能量下降，没有统一下降率。r=e0h的首头孤立解E2=0是特例；头1/2合法零源补链使更高头真实降能，不能递归为逐头局部最小。

[R239首位图](results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)/[横向压缩](results/R239-appendix-coercive-adjoint-and-positive-mixed-compression.md)保C²=η₀N₁|L、||C||<1/√12，真缺陷需C*Gx=0及C*x=−η₀(N₁|L)*Cx。核上T*≥7/8、Re(P_MBT*|M)≥5α₀/6，给M⊥内横向同构而非BM原像；各位压缩约束仍未排缺陷。详式和度量字典在原稿及本轮归档。


## 当前接口三：一般系数行、多个模式与中央域

完整已付行类、种子/比较/最高字符条件、全部旧公式及原稿链接保[本次前全文](notes/2026-11-13-handoff-open-before-faithful-vacuum-support-0c.md)。这里列下一实际缺口，未列的旧接口保持原状态。

1. **普通慢行与未知限制。** 实u奇次全部位移/幂闭，偶次余α^(2k)；有限谱部分须共同存在才能跨行。实负正定辅助已闭，正号碰撞/双无界未闭。1<α≤3普通全部重数、居中迟首κ>2的λ0及无副本重根仍开。主/辅助尺度、种子、零位置、ΓY预算不得互换；全H单射稠密不传未知M。
2. **原双行见证。** 真迟首核给同一ζ和正秩一ρ同时湮灭SA′、TA′、ZA′，S=X+Hζ、Z=Y−B0+Hζ²。整函数全右替换(X,Y)→(−Hζ,B0−Hζ²)和快混合矩已付；这些必要增长界有固定非湮灭正态反例，仍欠实际联合非零快证书/来源特殊正常锚。不能跨ζ混用ρ。
3. **导子及实际源。** 固定阶ad强单位给全部广义核全等向及kerT^n⊂closureRanT^m；不付实际值域或限制稠密。全域高导子有强单位但不是单个导子像，短Leibniz末段/实际伪逆费用仍开。纯等权高ad WOT0只限其原模型。
4. **有限复模式。** ≤5正实log复二次全Q已闭；指定六模式F²的全部λ,w已由真实Bell逆/有理jet证书闭合。[指定六模式F³第三矩](results/R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)付16维完整Schur和17低变量加权六次R3，仍须证明有实际逆的B_r自然幂∈gradR3；普通first Bell分母次数障碍不等于非循环。一般Σ内、无池、无限模式及更高幂仍开。
5. **相对乘积与自然域。** 相对ℓ1双乘积、单慢加快、快分式和空谱锚两方向按旧条件保留；复杂相对ℓ2、三以上cocycle、双全C与非解析闭包未闭。正自然词、热/预解和共同正则子须保原域；可数全H稠密像之交不保证与未知M非零相交。

[两个等向平面的完整矩截面](results/R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)：原有理W±上的完整矩支撑给全部h≥2的精确临界条件Q±|T_h；原三组空谱first满足同一Q±(Eᵀr)=0，匹配Bell自然h次值在这些整族临界截面上全消失。对F³即T3=Q±ℓ，已超两个旧孤立点；仍欠其它临界支撑及真实全局幂理想证书，不把局部厚化/受限消失当归属。

## 其他仍开放的路线与不可互换的极限

一般L²循环性、非标准主理想分类、完整A′核、外部紧交织继续。R12紧夹积/自伴链障碍及R14指定硬谱截断非紧与faithful弱极限已付；它们不排所有外部方法。family293仅超不变/有限因子投影范围，不是普通ISP答案。

中间头自然旗不等于原A_m的像旗；有限权族常数不代全有限模型；环境高孔观测不代真实窄barf或W；最小原像的范数不代距M；WOT/SOT不代一般正常配对费用。所有精确反例与历史来源见本次全文归档。下一个子问题按上面实际缺口继续，完成标准不变。
