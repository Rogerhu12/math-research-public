# 完整首个三维块分解前的交接与开放问题

2026-11-13 06:19:35 UTC；固定main 82cedd5195f258a31f57d3b70f4546a4298126bd。保留完整原文，链接按notes位置调整。

## 原 HANDOFF.md

# 交接

## 目标、负责人和规则检查点

- **目标未完成：** 必须完整解决可分无穷维复Hilbert普通ISP。Haar普通不变格、边界N=M及一般正常湮灭者仍未知；规范单模式全部多项式加权输入现已循环。不降低README完成标准，不以阶段或时长收尾。
- **负责人及分工：** Astra-ISP-1cf8c51d负责，0c继续贡献。1cf用R213–229、R240–271；0c用R230–239。新编号先登记，独占git/index，不动他人未发布文件。
- **最后实际pull/规则：** 2026-11-13 01:06:52 UTC，cdb9429c93f969d1054d8e1e49643add83457c24；真实git pull --rebase origin main，两README差异空。每小时至少一次，终端恢复即补。
- **0c 最近实际 pull：** 01:06:17 UTC / bfe9f2c0b2977d4bab3d14793c3f247374e81303，两README差异空；后续含05:20:35、06:03:04的真实pull调用均执行前No usable execution environment，API非pull，恢复即补。
- **已读规则blob：** 根 f787a306d90892d8dec765dc59747d60ba39f055；题 6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd。每次实际pull均比较两README，有变只读差异立即照做并记SHA；至少每小时pull。
- **API后备检查点：** 2026-11-13 06:17:03 UTC / main 252e9a45cb6916e0582163787588371a31bcf946，两README blob未变；0c 06:03:04、1cf 06:10:21真实pull执行前无环境，API非pull。
- **发布：** 完整结论单独推；终端可用用git，拒推即pull --rebase。仅失联用根§8小文本；API不算pull。令牌仅命令行，不写文件/config/提交；不force、不写根LOG；Markdown<100KB、H<10KB，合并最新main。

## 恢复记录与模型

工作树：1cf /tmp/isp-1cf8c51d-math-research；0c /tmp/isp-0c017065-math-research-20261113-0030。[本次前H/open全文](../notes/2026-11-13-handoff-open-before-nonsummable-sylvester-dichotomy-0c.md)保原文/归档链。

模型：H=L²(Z₂)，A为真实Haar加权odometer；Nj=A^(2^j)/dj=Ej+ηjEj*N_(j+1)、ηj≤e^(−770·16^j)，Y=N/(1+N)、V=I−2Y。A′交换/C对称，R88有界SOT多项式逼近。UHF不运输未知限制；C保核、局部等向和输入域不可免费。

## 1. 原 Haar 正常湮灭者

S_N/Y全H单射稠密已证，普遍强主理想仍开。失败有正有限秩正常见证；R228允许C实化，R229反例排一般秩一纯化，R242窄矩阵/垂直商图已付但不免费图稠密。
**R255：** E_√3有限正正常见证已排，端点最优；一般正常性不保此矩。
R235原保函数非负锥与R237 Walsh对角/有限带/entrywise-ℓ¹及可实现乘积基类仍有效；均不扩一般正常态。

**R235：** 连续/a.e.+双边UI等类已排，普通L∞不够。真湮灭保全G右矩|φ(T_mG)|≤h_mλε_m||G||和尾能量约束，待预算内非零配对右因子。
**R237：** 固定Q∈Acal的QAcal同范数强*逼近QA′；非UHF左因子/无界右因子不覆盖。
R248阻尼不交换、R250未得A+不变，详式保归档。
**R253/R237/R230：** 真湮灭迫q_m↓0。新exp(zU_m)、|z|≤q^6的真空比≤3β^−floor(q^(2/3)/4)，完整Gram/实际carry及复测度混合成本已付。实际N_B共同次数相位锥在原b/q^4预算内同衰减；独立坐标相位/一般混合与真密度专属仍开，不代完整q_m。
**R244：** 广义Ri付Mi=Ri⁻¹Di，共同R理想/像/Γ_R参数无关；真空原像⇔全部无重复词域。删一因子P_i付指定输入、ΣMjP_i fj=0、φ(P_i A′)=0。rank2 Q有J²=−I、无循环向量，Γ_R⊊Γ_min⊊Γ_max两商∞。新：Pg=1已足P⁻¹=X_g/C自伴图核心；所有N⊂E⊂K比例闭图的TU+F均全C谱，含两端。个别Ri理想湮灭仍不矛盾：Pg=1不代强主理想密度，未付Cf交叉域/共同真空或商正密度。
**R267：** 前向平顶积P∈F_A=∩A^rA′非零、PW_n收缩强*趋I；F_A同范数强*稠密、AF_A=F_A、F_A∩UHF=0。共同幂原像是有限闭交换域图核心，非PH自动入域。1∉RanP；指定配对⇔Σ_J|φ(PV_J)|²有限，真湮灭矩/S分母未付。
**R230固定态：** 同一非湮灭f、q_i=16^i排全部可逆纯交换收缩块及有限完整逆源组合，实际完整Gram指数log5/2；非块/无真空未覆盖。
**R230真密度/证书：** 全矩m_B=L_Bρ_B、张量Gram/全列carry及Slater对偶已付；纯右列保非正ρT_m交叉约化。理想内近真空收缩给正证书，但统一定位τ×最优正密度常数≥√(2^m)/144，排统一截断，不排真态专属。
**R230/261：** 规范正积完整逆e^{o√q}、β<1/2共同域非像，通用配对/分母已排。

**R253/263：** 全A^r不能有界除S；同一H_(1/(60e²))向量不在两RanS，规范/全域分母已排，专属仍开。

## 2. 两个实际边界的 N=M

T=T_N,T_Y，M=kerT，N=closure BM，D=M⊖N。R187/200给M∩RanB^r⊂N，有限孔核仅真空；R234模N已闭，R238原J_q成本不能当模N成本。环境坏见证在M⊥，横向T*M同构不是BM原像；旧通量/头Jordan/平方γ各保原范围，详归档。
**R239全q/最小能量：** R271先得log^(4/3)权阶；原进位/大窗低投影e−74d⁴、真实lift e−75d⁴。d≈log^(1/3)q、K*=3(16/770)^(1/3)给c>K*权核入N、真D尾常数K*/2。Σ1/[ell(1+λ²)]发散足N，所需无权增长未得。真实r自动D^d，λ²=〈G⁻¹r,r〉须保Schur补；正/倒能量仍容慢尾。
**原始块/移动窗：** 相容真空jets给受控q孔原始P小修复，范数趋1且log rank≈2qlog2。P移到[m+k,m+k+2q)、k≤d仍保真实自由坐标，仅调自由0孔；B=A+D_free原像支撑止于q+k+d−1。双宽λ̃^P≤(1+o1)τ_q+e−70d⁴||w||→0，原λ̃与补块差→0；ell=2d+m覆盖≤2，lift/倒数判据已付。全低输出logΛ=Θ(log^(4/3)q)、坏v投影趋零及完整前缀指数障碍保留，未覆盖全部。
**R239闭链：** 有限尾塔付原链/联合旗固定窗闭像；Riccati保准确Gram、加宽极限无统一速率。新R271已付特殊旗对偶预算并将末端转为原头跃迁，不能用A^d=0删实际伪逆传播。

**R271：** 残量R=⊕e_i kerD^(d−i−1)、链i≤d−t/kerD^(d−i)准确；Gflag为完整Schur补。新同时右逆Q成本C≤e^d⁴，Gflag≥C⁻²，最优||y||≤Cλ、||z||≤C²λ，全部进位/核投影误差已吸收。真缺陷迫Σ〈H_tw_(q+t),P_kerD^(t−1)z_t〉≈||v||²+λ²，H_t只跨≥2格但含固定1/4项，尚不可消去。准确插值ΠNexp=ΠN=ΠM=V与Gram差ΠP_W保留；未得有界原像子列/N=M。平方Smith旧(2d−1,2d+1)、新4d只排稠密D交织。

## 3. 危险核、中央闭图与系数行

**R176共同谱/实结构：** 有界不变部分谱相交且连通；有限谱部分若存在，共用r_u，零字符倾斜不改。点态全部权/幂坏值须q(r_u)=q(r_u−2α)。新J逐点共轭给r_bar(u)=bar(r_u)，实u迫r_u实，故全部(u^(2k+1)−λ)^m e^w循环，偶次仅留α^(2k)；任意q在R单射/无实根也给相应闭合。ℓ1复误差只给仿射实线，首位未必沿线；多行r加性仅共同有界部分成立。最后实碰撞核仍开。
**R189双方向：** X有非ℓ1可和相位缺陷、Y任意first/有界加性慢模式，允许快gauge增量Acal扰动；每个实际非零G[X,Y]最大实现单射稠密。除有限gauge互素后只消Y，L^degE(X)=ρ(L)由旧R189在未知M上dense，深域跨核排核。总类秩≤2且含实际空谱组合也得。双共振全q和V²−U³耦合已付；不删普通点态慢修正，不传新多项式全部子商。
**旧空谱锚：** R134/138/155已闭非ℓ1可和相位缺陷first的有界扰动及首一自然多项式，R189已闭非首一G[X]普遍分式场；同射线不重计。
**R268–270：** G[X_b]非首一闭包/排核归R152/183；R270新增全F_p、快辅助Σh_kF_k及物理不交已知点态因子乘积。有限头只保单atom；普通慢Bell不自动快。
**R236字符判据：** F_q+v_c−λ：早偏离全λ；否则gcd(q−λ,αq'+δ)=1足循环，≤p−1核候选。真实dyadic A幂与核内字符单位付限制密度；p≥2首支撑有序全闭。二次λ*有单位置零例，普通late-c候选λ0在双池类已排。
**R236全阶双池/二分：** 双池min位≥μN、|a|≤C/√N、log det⁻¹=O(N^1.5)足；自动池覆盖κ>1比较/global logρ_n⁻¹=O(n^1.5)（零主位可另ℓ1辅助），规则幂另许不同κ_±夹界。新κ>2且所有充分大物理位|c|≈|a|^κ时，只需liminf log⁺ρ_n⁻¹/n<∞，含全部ℓ²\ℓ¹：首次降幅后第二池可用或真辅助尾极小；全阶Sylvester乘积分母只付一次p变量Cauchy，Γ_Y=O(N²)，4pr jets/完整C配对闭合。主零位在新二分须最终c=0，有限例外全入头。任意相位/排列、固定q/全λ保留，普通点态幂另证。
**其他独立预算：** 固定盘|a/c|≤K、L_N=O(N^1.5)保；辅助圆r_N=εN(c_N*)²付一次B/Y联合逆，L_N=O(N^1.5)、Γ_Y=O(N²)足，含任意主行配辅助α≤1指数/长平台。旧主尺度、子支撑保原范围。
**其余界：** R259/260/R264–266的解析简单根/α≤1重数保原范围。R236双导子投影不直接排核，1<α<3的Leibniz末短和未控，两位校准排粗吸收。α>3及α=3大β特例属旧快类；单个四次幂界不是G。剩余1<α≤3扣除旧特例；中央旧域/运输/family293与详式保正式稿/归档。

## 紧接稿及持续执行

1cf R189双向3bff9ad1、C实化范围订正73433202已推；本次推R176实根/奇次幂。kernel续实碰撞及双全C，normal续真实正矩，boundary续低核通量。
0c复指数252e9a45已回读；本次非ℓ1/指数种子的全阶二分。完整原始分解9de9d45e9b03ec07842a5a5c5146b0e1c32e2bbd待核；代理续可和极快/无比较、三维分支真能量及真密度复混合。
完整证明即推，再接open；H更新，逐pull核规，不以阶段/时长收尾。


## 原 open.md

# 未解决的问题

## 主目标与完成标准

完整解决可分无穷维复 Hilbert 空间上有界算子的普通不变子空间问题：证明每个算子有非零真闭不变子空间，或给出完整反例。**主问题仍未解决，README 的完成标准没有降低。**

当前实际候选为
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

[删一预解因子](../results/R244-appendix-cofactor-input-domains-and-individual-resolvent-annihilation.md)：真有限秩矩迫每个P_i=∏_(k≠i)Ri满足P_i f_j∈DomMj、ΣMjP_i f_j=0及φ(P_i A′)=0。rank2即单Ri理想湮灭，并有准确商向量配对；未得Cf交叉域，不能再删第二因子。

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**R255范围。** [√3端点](../results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)排E_√3有限正见证，carry/最小域/正张量化已付且端点最优；一般正常有限秩不保该矩。R235另排保函数非负锥者，Hilbert正/C实不够。

**相对迹的范围与真湮灭约束。** [连续核](../results/R235-appendix-continuous-kernel-relative-tail-traces.md)及[正尾耦合](../results/R235-appendix-tail-couplings-almost-everywhere-continuity-and-bounded-obstruction.md)排连续核、a.e.连续有界F、双边UI无界F及g(v₂)=o(n^3/4)类；恒模正秩一负极限证明一般L∞不够。[真湮灭能量](../results/R235-appendix-annihilator-tail-coupling-energy-and-right-tests.md)无需正则性即给u_m²+v_m²≥λ_m−2λε_m、(2^(2^m)+1)δ_m≥λ(1−2ε_m)，且对全部G∈A′有|φ(T_mG)|/h_m≤λε_m||G||。下一步须从真矩方程找到预算ε_m||G_m||→0而耦合配对非零的实际右因子，不能替换为任意点乘相位或普通L²逼近。

[R237及附录](../results/R237-actual-walsh-diagonal-normal-module-and-slow-annihilator-exclusion.md)排Walsh对角、有限翻转带、entrywise-ℓ¹及可实现正交乘积基（Σ|ν_j|²<∞）中的对角/有限头块正态，含无指数次数矩例。复密度仅推出A′功能及迹零，正性才给ρ=0；任意基混合及一般正常态不自动覆盖。C实循环秩一态可无ℓ¹对角表示。

**配对仍开。** R244逐列域加非零锚足排见证；聚合逆图的全Walsh Gram准则仍需强主理想单位。新逆最小性不删去往返表示所需强单位。

[预解图与正真空锚](../results/R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md)给RH⊂∩DomMi、Rg=1时正锚Trρ，秩一真湮灭必σ(MU+F)=C。[广义预解与有限词域](../results/R244-appendix-generalized-resolvent-unit-classes-and-vacuum-word-domains.md)给任意Li=MiUi+Fi的实际预解Ri满足Bézout恒等式及Mi=Ri⁻¹Di最大商；共同R=∏Ri的代数主理想、实际值域与Γ_R不随全部允许选择改变。真见证迫Γ_R距真空≥√Trρ，虽各单图投影稠密。1∈RH等价某个排列全部至多2^r个无重复自然子词在1上有定义，亦等价所有排列；rank2还原两交叉域。**无广义预解分支或共同高阶域缺口尚未排除，调参数不能改变它。**

[秩二有界链](../results/R244-appendix-rank-two-koszul-defect-and-double-common-graph-gap.md)的Q有J²=−I、JT=T*J，非零Q无限维且无循环向量；真rank2迫Γ_R⊊Γ_min⊊Γ_max两商∞，Ri_Q=0、Di_Q单位。[全部中间比例图](../results/R244-appendix-resolvent-minimal-cores-and-intermediate-ratio-spectra.md)：Pg=1本身即给P⁻¹=X_g与真空图核心；任意N⊂E⊂K闭A²不变比例图，包括两端，均σ(T_E U+F)=C。Pg=1仍不保强主理想单位，未排真实正矩缺口。

[R267 Blaschke逆族](../results/R267-appendix-blaschke-block-strong-units-and-linear-degree-inverse-type.md)有Pg=1和收缩强单位，逆线性下型κ=log(4/3)−1/4；[前向族](../results/R267-appendix-forward-blaschke-strong-units-without-vacuum-preimage.md)则1∉RanP但全部有限旗子商单射稠密，完整逆范数carry已付。原逐列配对可用；R244聚合逆图仅适用于有真空原像者。指定全列矩及S分母仍开。

[R267第四附录](../results/R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)给同一非零收缩P∈∩A^rA′、PW_n收缩强*趋I，有限旗子商单射稠密。该理想同范数强*稠密、AF_A=F_A、F_A∩UHF=0；共同幂原像为有限闭交换域的图核心，不是PH自动入域。1∉RanP，配对⇔Σ_J|φ(PV_J)|²有限；用P1作第二向量会取消正则化。真湮灭专属全矩界及P∈SA′仍开。

**固定非湮灭态的完整块边界。** [R230完整Gram](../results/R230-appendix-arbitrary-contractive-block-gram-and-complete-source-obstruction.md)对同一非湮灭f及q_i=16^i排所有可逆收缩纯块的合格逆源，实际完整Gram比值指数log5/2，有限完整源组合亦排；负实真实粗源g∉H_√3保留。非块/无真空原像未覆盖。

**真密度完整矩与正证书。** [R230完整定理](../results/R230-appendix-positive-density-moments-dual-certificates-and-localization-obstruction.md)给m_B=L_Bρ_B、Gram=||R*m_B||、LL*=[[2,2],[2,6]]^⊗n及全部列carry。真湮灭右残量≤λε_m(K_n+d_B)，纯列另付λκ_md_B；它依赖非正Tr_(B^c)(ρT_m)/h_m，不能免费写成K_B*m_B。有限块正性对偶inf{μ:μI−ΠΩ+Re(TX_u)≥0}严格可行；理想内R=TX_v收缩且||RΩ−Ω||≤a<1/2给μ=(1+a)/(2−a)、u=v/(2−a)，故可得正余量。

[统一定位障碍](../notes/2026-11-13-first-tail-obstruction-to-uniform-full-moment-localization-normal-complex.md)对任意n物理位K_B给τ≥q²/[8√3(n+2q+1)^(3/2)]；最优统一正密度矩常数C_n≥5^(n/2)，故τC_n≥√q/144→∞。它排先范数截块再统一放大，不排全空间右因子或真湮灭密度专属消去，后二者继续开放。

R242窄图非全域；R248阻尼不交换、撤阻尼未得；R250稀疏图逆域零、余图闭像非紧且未证A+不变。详式保归档。

**实化与降秩须分开。** [R228/229范围订正](../notes/2026-11-13-r228-r229-c-realification-scope-correction.md)：(ρ+CρC)/2在整个A′保同一正泛函，但可增秩；两两配对不保迭代到秩一。R229及9维实幂零例只排一般正秩一表示，不排C实化且非本题真见证。未知子商C不变、普通TρT*保湮灭不可假定。R240固定非湮灭态排通用first配对，专属/两端可变仍开。

R210–211奇异正态/Cantor族不具Haar正常性；固定正则端、Fock及增生平滑等旧障碍保归档，不代表真实正常矩。

[R253相位消元](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)给I⊗Q_m∈S Acal及真见证必要q_m↓0。[R237非负锥](../results/R237-appendix-nonnegative-tail-right-factors-and-vacuum-ratio-obstruction.md)已付原支撑预算。[复指数/完整Gram](../results/R230-appendix-complex-exponential-tail-right-filters-and-full-gram.md)现在统一处理exp(zU_m)、所有|z|≤q^6：实际真空比≤3β^−floor(q^(2/3)/4)，β=1+1/√2。纯模型对全部复参数成立，实际Duhamel误差在q^6盘由负q^4指数支付；有限相位酉后取范数极限，无无限Haar酉假设。全部有限Walsh列的2×2局部核及其乘积/导数给完整Gram，复测度混合付总变差与实际carry，非消失比必须有至少exp(cq^(2/3))相消成本，该必要成本仍可在q^4预算内。

同稿还排实际N_B共同次数相位锥Σd_B exp(iθ|B|)N_B，d_B≥0、|B|≤b_m、limsup b_m/q^4<770/(16log2)，最高物理位不限；包括同复射线有限乘积。独立坐标相位、非线性次数相位和一般复混合仍开。上述均只为真空比，不能当完整q_m或一般ρ的下界。

[R253域附录](../results/R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md)：真实图carry已付，D∞不含RanS；有限first预解积非S有界右倍数，专属配对仍开。

**已排除的通用正则化。** R230/R261规范正积的累计ℓ²、完整逆e^{o√q}及共同子半次数域非像，旧Cayley方向增益、R253全A^r有界除S失败和R263同一H_(1/(60e²))向量不在两RanS，均保于[本次完整归档](../notes/2026-11-13-handoff-open-before-residual-flags-1cf8.md)及results原稿。像含该小指数域的有界分母不能除S；这些结论不排真见证专属配对。

[R237相对主理想密度](../results/R237-appendix-asymptotically-contractive-principal-ideal-approximation.md)对固定Q∈Acal付QAcal同范数强/强*逼近QA′，q_m可搜全部尾A′；非UHF左因子/无界右因子不覆盖。R230/R263已排规范无限正积为Q_m有界倍数，一般右因子仍开。

## 当前接口二：实际边界的除法饱和

固定两个实际边界T_N/T_Y，M=kerT、N=closure BM、D=M⊖N。R187/200已给各有限稳定像及M∩RanB^r⊂N，有限孔核仅真空；真正问题是**无权核内稠密与N=M**，不将环境有限孔稠密当核内核心。

**旧接口。** R234模N已闭；R238原J_q成本不代R239模N成本。环境Γ坏见证在M⊥、横向T*M非BM原像；真幂界保真输入、头链与未知尾。旧预算见[归档](../notes/2026-11-13-handoff-open-before-exact-boundary-gram-0c.md)。

**全整数窗口和真正最小Gram。** [R239全q](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原进位，低投影e−74d⁴/真实lift e−75d⁴；d≈log^(1/3)q、K*=3(16/770)^(1/3)。c>K*权核入N，真D尾常数K*/2，权阶先属R271。窗口ell=d+m的Σ1/[ell(1+λ²)]发散足N；真D倒能量≤8τ_Q²/||w||⁴。λ²=O(q log^(2/3)q loglogq)足但未得。

[准确Gram](../results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)为G=D0P_kerS D0*，严格正；实际r=Avq自动D^d，λ²=〈G⁻¹r,r〉。Schur补不可省；窄带正/倒能量仍容慢尾。逐头单块残量/旧d核阶及Tr(ApKp)非零保原范围。

**局部坏方向与原始块。** [局部最优](../results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)给全低输出单位球logΛ_q=Θ(log^(4/3)q)，任意有限/无限尾仍保下界；[原始块完整证明](../results/R239-appendix-unweighted-primitive-removal-high-rank-blocks-and-full-projection-obstruction.md)给同一坏v的||P_Mv||→0。相容真空Db_t=b_(t−1)、||b_t||²≤K/(t!S_J^t)、K→1，使任意范数受控前缀q孔投影P（D_IP=PD_I=0）的真实分量有小修复；原λ与补块差亦趋零。2r位原始投影实际相似/张量、r=floor(m^.25)给||P||→1、log rank=(2log2−o1)q，但完整固定前缀投影唯一且log||P_full||≥(4log2−o1)q，稳定完备覆盖仍缺。

**移动原始窗保留真实自由坐标。** [新完整定理](../results/R239-appendix-moving-primitive-windows-and-double-width-repair.md)把原始块移到I=[m+k,m+k+2q)、0≤k≤d，保留前k个纯尾位自由。u为Pw的远尾真空系数；只微调自由0孔使它等于Pv，所有正自由孔沿用真实w。B=A_m+D_free、B^(d+k)=0；同一相容真空族构造Φu∈kerL，c=Pv−Φu修复Pr。展开B^t的总孔数为q+s+j≤q+k+d−1；真实远尾t层输入相互正交，只付一次||P||。全部小分母/carry后||c||≤√K||P||[||w_(q+1..q+d+2k)||+e−71d⁴||w||]→0，不添尾率或隐藏√d/k。

为容纳移动源，明确新最小λ̃窗口[q+1,q+2d]，不混同旧λ。原逐头lift对Q0=q+2d合法；ell̃=2d+m的覆盖仍≤2，故Σ1/[ell̃(1+λ̃²)]发散足N，真D有Σ1/(ell̃λ̃²)≤8τ_Q²/||w||⁴。原λ̃与(I−P)r的最小值差≤||c||→0；λ̃²=O(q log^(2/3)q loglogq)仍为未证充分条件。旧d链旗没有被直接当作2d空间，完整真实残量和无权N=M仍开。

**原完整链。** [R239闭链/Riccati](../results/R239-appendix-closed-repair-chain-riccati-and-terminal-leakage.md)付固定窗闭像/最优链、准确Gram与加宽正末端罚项；有限窗下降到无限窗无统一速率。实际伪逆非幂零，不能按A^d截断。新R271限定特殊旗后已付对偶预算，未消真实头通量。

[R271平方局部型](../results/R271-appendix-square-head-smith-types-and-old-head-single-block-correction.md)给旧跨头Smith(2d−1,2d+1)、新4d，排稠密像D交织。固定混合核有限孔/正指数核心不传原核；上角残量可用旧d头修复，最多增2d孔但成本仍依Q。

[R271残量旗](../results/R271-appendix-orthogonal-residual-flags-and-exact-source-gram.md)准确给R=⊕e_i kerD^(d−i−1)及全部链i≤d−t/kerD^(d−i)，Gflag为完整Schur补。[联合旗能量](../results/R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)付同时右逆C≤e^d⁴、Gflag≥e⁻²d⁴、最优||y||≤Cλ/||z||≤C²λ，全部进位及删除核投影误差≤e⁻⁷⁰d⁴||w||λ。真缺陷迫Σ〈H_tw_(q+t),P_kerD^(t−1)z_t〉≈||v||²+λ²；原H_t只跨≥2头格但含1/4，不能称小进位。剩余为这条真实最优低核通量，无权N=M仍开。

[R271准确插值](../results/R271-appendix-exact-stable-range-interpolation-and-norm-defect.md)给Π(Nexp)=ΠN=ΠM=V及有界线性右逆；原像范数按真实修复能量计。插值Gram差ΠP_W在W≠0时范数趋1；没有固定w的有界原像子列，不能推N=M。

[有限尾塔直接推论](../notes/2026-11-13-finite-tail-tower-corollary-for-exact-residual-flags-boundary-resume.md)把底层下延到q−d+1，kerD^h恰为出生层s>p−h坐标；联合旗限制仍是有限矩阵列限制张量恒等，故S_flag/伴随像闭，原对偶inf取得且固定m,q有界依赖源。原始P及I−P保实际残量旗和全部可行链旗。此为R239旧有限塔法的直接推论，不是新的统一能量界。

## 当前接口三：一般系数行与多个模式

[R176共同谱](../results/R176-appendix-bounded-part-spectral-intersection-and-common-exceptional-root.md)给有界不变部分谱相交/连通、所有有限谱部分共用r_u；全部倾斜/点态幂坏值至多一个，须q(r_u)=q(r_u−2α)。[实结构附录](../results/R176-appendix-real-structure-affine-lines-and-odd-power-cyclicity.md)用逐点J给r_bar(u)=bar(r_u)，故任意实u、任意复权的全部(u^(2k+1)−λ)^m循环，无尾率条件；偶次仅留λ=α^(2k)。任意q|R单射也全λ闭合，含p(u)+iu−λ；无实根q的零位移全部幂闭合。ℓ1复误差只迫r在仿射实线，实际首位未必沿线；共同有限谱部分存在才有跨行加性。剩余实碰撞核未排，亦未构造有限谱部分。

[R147慢辅助首位切片](../results/R147-appendix-bounded-slow-auxiliary-slices-and-polynomial-cyclicity.md)：任意ℓ²主/权、有限ℓ¹辅助，最高系数r_p(β)≠0，首联合位F(z,β)与F(z−2a,β−2c)互素即循环。全部(F−λ)^m仅留有限切片碰撞值；真Bell/有界A^h差商/深域消元均付，无空谱/熵/辅助尾率。不可约慢例u³+v²仅留2±10/(3√3)。R236全阶共振加偏离判据归其原结果；最高字符零、晚首碰撞及双无界仍开。

**既有单模式。** [R236](../results/R236-appendix-all-multiplicities-of-canonical-weighted-polynomials.md)的规范、临界弱ℓ¹、σ>1幂尾及α≤1指数子序列类均已闭，全部真实域/重数证明保留；R268给更广准则。

**更多排序行。** [R268](../results/R268-entropy-budget-weak-l1-bandwidth-and-all-multiplicity-cyclicity.md)沿N满足sup_(k≥N)kρ_k≤DNρ_N、Σ_(k≤N)log(ρ_k/ρ_N)=O(N²)、logρ_N⁻¹=O(N^1.5)，则全部q(u)e^w循环。实际成本E_N+log^(4/3)ρ_N⁻¹+N²及jets/ad域已付；未满足准则的little行、1<α≤3剩余带仍开。

[R269](../results/R269-analytic-a-coefficient-bell-polynomials-and-finite-head-multimode-cyclicity.md)给熵主行解析A首一/有限头点乘及ℓ¹主行有限头P；[R270A](../results/R270-appendix-maximal-root-multiplicity-and-same-order-nonresonance.md)按最大根重数μ许c=O(|a|^max(2,μ))，最高重根保复比例非共振，小o无需速率。

[R270二阶消去](../results/R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md)付θ=2；[全阶F_p](../results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md)的新增应用在§§9–10，全部非零有限组合循环。其§§1–8底座归R152/183；单支撑保真实零例。

[非首一附录](../results/R270-appendix-arbitrary-fast-leading-coefficients-maximal-closure-and-cyclicity.md)仅重证R152/183：有限R^L核核心、最大C自伴/单射稠密，不称原自然域闭。[审计](../notes/2026-11-13-r184-r186-scope-audit-and-finite-word-subquotient-corollaries-kernel.md)亦扣除R184/186旧联合域。

[R270快辅助](../results/R270-appendix-fast-auxiliary-modes-and-resonant-polynomial-modules.md)给任意ℓ²主/权与独立超三次快辅助的Σh_kF_k；p≤1去R157主行ℓ1，不需最高字符锚。全部mixed域已付，普通q(u)慢Bell/一般慢辅助未全闭。

[R236零输出分类](../results/R236-appendix-resonant-polynomial-zero-output-and-leading-order.md)：a∈ℓ¹、s=a*+Σa、μ=mult_s q、L=支撑数，T_q=Σq^(r)(s)e_r(a_j(R_j−I))为零⇔L<μ；非零首阶为最早μ个位的2^j之和，μ=0为单位。无限支撑循环及二次关闭归R270C。

**全阶可和偏离与字符互素。** [R236字符定理](../results/R236-appendix-real-dyadic-factor-character-coprimality-and-all-order-deviations.md)对非零主行、任意a,b∈ℓ²/c∈ℓ¹及F_q+v_c−λ给：早偏离处理全λ；否则α=a_ja、δ=c_ja，gcd(q−λ,αq'+δ)=1足循环，至多p−1候选。实际dyadic A幂、核内字符单位和C/Fourier均付，不除G_n本体。p≥2且j_c≤j_a的F_p+v_c已全闭；二次唯一候选λ*=(δ/2α)²确有单位置零输出例。一般late-c的λ0不能由这条字符判据排除。

**迟首位规则慢偏离已升为全阶闭合。** [二次完整定理](../results/R236-appendix-two-site-scalar-bezout-and-late-support-quadratic-cyclicity.md)的双池条件保持：各N位、min物理位≥μN、max|a|≤C/√N，跨池d_N=min|a_kc_j−a_jc_k|>0且log⁺d_N⁻¹=O(N^1.5)。[全阶完整证明](../results/R236-appendix-all-order-resonant-two-site-bezout-and-derivation-budgets.md)给任意固定非恒定q、任意λ，(Σq_kF_k+v_c−λ)e^w非零循环。这里F_k保R270C的精确共振修正，不换成普通点态u^k。

真实ΔG_n逐位含u_j^n而无Boolean一次；完整导子壳/4pr自然jets付系数与重复位。一次系数4a_jP_q'(X_M)+4c_j被同一pair消成标量，r对给r!u_F、两次r!恰为有界双池弱平均。局部T_tail+A U_h(X)保左右A四次成本；没有对未知限制取逆或偷换点态幂。

**自动双池与双幂夹界。** [排序定理](../results/R236-appendix-automatic-separated-pools-and-two-power-envelopes.md)用nρ_n²→0给无穷固定比例降幅ρ_KN≤δρ_3N；最终|c|≈|a|^κ、κ>1/c∈ℓ¹和全局log⁺ρ_n⁻¹=O(n^1.5)即付det。此支允许主零位另有任意ℓ¹辅助。两侧ρ_n≈n^−σ、σ>1/2还许c_-|a|^(κ_+)≤|c|≤c_+|a|^(κ_−)、1<κ_−≤κ_+；第二短池置N^τ、τ>(κ_+−1)/(κ_−−1)仍有多项式det。

**全部非可和主行，且只需指数种子。** [完整二分/Sylvester逆](../results/R236-appendix-nonsummable-main-dichotomy-and-all-order-sylvester-inverses.md)：κ>2，若所有充分大物理位c_-|a_j|^κ≤|c_j|≤c_+|a_j|^κ，且liminf_n log⁺ρ_n⁻¹/n<∞，则全部固定非恒定q、λ的(F_q+v_c−λ)e^w循环；所有ℓ²\ℓ¹主行自动满足。有限头任意例外允许，主零位在此新定理须最终c=0。首次降幅保前幅度指数下界，第二池可用或真辅助尾极小；后支用全阶Sylvester恒等式/单次p变量Cauchy付同核乘积逆，Γ_Y=O(N²)，自然jets与四次配对齐备。

两范围独立，细节见正式稿。扣除旧锚/快类后的可和极快行、无比较辅助、普通点态q(u)及一般独立慢多辅助仍开。

**其他实际预算保独立范围。** [固定盘逆](../results/R236-appendix-fixed-disk-kernel-inverses-and-sparse-linear-deviations.md)对无限S上|a/c|≤K、S辅助L_N=O(N^1.5)有效，S外任意主/辅助；[辅助尺度共同圆](../results/R236-appendix-auxiliary-scale-joint-resolvent-and-independent-tail-gaps.md)取δ_N=c_N*、r_N=εNδ_N²，双删除及一次联合Cauchy给L_N=O(N^1.5)、Γ_Y(r_N)=O(N²)充分。含任意主行配辅助双侧α≤1伸缩指数，或Σ_(n>N)c_n*=o(Nδ_N²)、L_N=O(N)长平台；明确正相位例Y∉G。旧[主尺度共同圆](../results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)/[子支撑](../results/R236-appendix-supported-deviation-arbitrary-background-and-empty-spectrum-scope.md)也保各自假设，不互换排序/半径。

**旧空谱范围。** [审计](../notes/2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)按R134/138/155：非ℓ1且可和相位缺陷first已空谱，有界A′扰动及首一自然多项式有真有界逆并保持未知限制；任意复ℓ²权/ℓ¹辅助早已覆盖。居中ℓ¹和全C慢分支仍需证，不能免费取二次分歧根。

[R257/258](../results/R258-entire-selfadjoint-kernel-transport-and-actual-tail-mobius-domains.md)的整自伴运输不回传原M点乘域/不变格；R224公共像/尾商障碍保留。

[R259](../results/R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)闭同幂尾p>1/2；[R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)闭排序limsup nρ_n>0的任意复行及物理重排，允许全部复first指数和有限联合解析Bell芽。其完整域导子代数无maxF成本；剩余解析分支须nρ_n→0且排序复和→Φ(0)，一般行重根另证。

[R264–266](../results/R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md)已闭α≤3/2的解析Bell/简单根及α≤1全重数；R268严格扩展后，规则1<α≤3/2的普通点态全部重数仍开。

**高阶导子及剩余短和。** [纯提升障碍](../results/R236-appendix-high-degree-raising-band-obstruction-and-range-projections.md)给r≫√Q的有界提升弱趋0；[全域双导子](../results/R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)付[ad_T^(2r)U_N](../C_Q^r)†强趋I、r=ηQ<Q/2、伪逆≤e^(Q/2)及全部carry。它不是单个导子像；核配对完整Leibniz在1<α<3尚余末O(N^((1+α)/4))项。[两位校准](../notes/2026-11-13-two-bit-pseudoinverse-calibration-central-next.md)排共同尺度粗吸收；须核内抵消或适配降阶，α=3不自动短段。

**旧快类。** [R236核查](../results/R236-appendix-existing-fast-classes-for-supercubic-sorted-rows.md)据R175：排序ρ_k≤Be^(−βk^α)、α>3已给非零q(u)e^w循环及标准主理想/普遍表示，无需下界。α=3时首阶r的β>80r⁴/3给限制稠密/强主理想，β>400r⁴给标准范数理想；均严格充分。单个四次幂界不等于G。剩余1<α≤3须扣这些旧例。

[R270第六附录](../results/R270-appendix-disjoint-slow-point-polynomial-products-and-head-masks.md)：物理不交慢模式的已知点态循环因子可相乘，故∏(uν−λν)^mν e^w循环。mixed词域/Bell已付，共享有限头仅保单atom；同模不同根、atoms之和不能这样相乘。

## 1. 一般向量的矩分离与有限二阶以上输入

R101全矩分离仅有限Walsh次数两端；任意非零L²循环性仍开，无最高锚。一般二阶核、gauge差在未知核上的像、双独立慢模式仍未闭。R130/131/143付二阶闭域及跨核配对，但closure(A^hX_g)域可扩大，不能取消A^h后补DomX_g。R29/44/51平滑及R163/165的Lp(p>2)/Orlicz交织障碍保留；有限柱近交换非精确Nj交织，R255/237仅明确正态子类。

## 2. 不变限制中的一阶闭乘子值域

R125/128/140给真实闭稠密限制、保M的收缩正则R(t)及图核心。任意复ℓ²非零first是否在每个未知不变M上dense仍开，准确等价closure S(t)M=M；不能用全H单射稠密、C保核或四正分量代替。正行、可和相位缺陷非ℓ¹、R151的G及R140明确四次尾型/80r⁴/3类已付普遍范围；一般慢S(t)不自动属G。C对称Volterra双倍反例排抽象捷径，R143只付跨核域；R176共同谱不排单点拟幂零分支。

## 3. 任意有界有限 chaos、范数代数及完整交换子

每个非零X∈Acal是否单射稠密、一般A′元素是否无非零核仍未知。R32无零因子仅在代数内部；R88纯/真实对应不保乘法或核。R92固定有限chaos有界乘子恰对应有连续代表的有界函数且属Acal；f(0)≠0可逆，零锚已覆盖一阶、局部有限支撑、R133首行和非零的行ℓ¹等类，一般有界二阶尤其无限低位行和消去仍开。

R143假想核的首位闭图须TBT=α₀及真实域；其完整附录付清尾平方差和最大商图，在分母有限放大dense时有图核心/C自伴，仍无排核矛盾。R124余数B₀或零常数B_s不保证再有界除A，首阶r>1不能自动归首阶1。

一般闭理想标准性已被R185/R188实际边界核否定：非标准主理想J无限余维且不含任何A幂、与指定G/bounded K零交；原H上S仍单射稠密，因此不直接给Haar不变子空间。进一步闭理想分类和这些J的精确闭结构仍开。R116/R118/R175/R179快类标准性、R140强主理想与范数理想区别及R121根式非闭保持。R112/R119已排绝对可和归一化幂的泛覆盖；Thomas、Peters、GT相关外部判据不能未经实际条件核对直接套用。

[R256](../results/R256-bounded-weighted-composition-commutants-of-the-radial-haar-model.md)已完整分类可测nonsingular底映射上的有界加权复合交换子：仅cA^n，n为普通非负整数。非整数2-adic平移由两个高位柱的正常质量与归一化幂交换估计矛盾排除；反向整数权本质无界。条件只需径向η_j→0，包含当前实际权。一般非复合A′元素、原核与普通不变格仍未知。

## 4. 相对乘积、多项 cocycle 与混合解析芽

[R189一个空谱锚](../results/R189-appendix-one-empty-anchor-two-additive-direction-kernel-elimination.md)：X为可和相位缺陷非ℓ1first、Y为任意第二first/有界加性模式，允许Acal快gauge增量扰动；所有实际非零G[X,Y]最大实现单射稠密。只消Y后把E(X)用L=X⁻¹变为旧R189普遍dense分子ρ(L)，真实深域跨核排除单核；有限多模式总类秩≤2且含实际空谱组合也得。全阶双共振q及正慢u/交替慢v的[v²−u³+(2−6u)s₂−8s₃−λ]e^w已循环；普通v²−u³、三独立类/双全C方向及新多项式普遍限制范围仍未付。

R127相对ℓ¹两乘积已闭；一般复杂相位相对ℓ²、三以上cocycle、非解析闭包和一般实际有界商仍开。R146/148单慢加快、R129/135单轴解析、R152有界加性和R153纯FracG各保原范围，超越分支未普遍限制dense。

R160自然二阶慢Bell可首阶1且四次尾型零，不能收入G。R77/79/82临界多尺度中间参数未闭，R83真实芽/轴谱接口保留。R162纯虚倾斜有界线性同构不保乘法；R147–150的指数权点态循环不代一般H向量乘指数。

仍可寻找固定单射R∈A′使所有非例外ζ有B(RM,UζM)=0：此时closureRM非零且含于M即可用R122，无须先dense。当前辅助因子依ζ变化，可数全H稠密像之交不自动与未知M非零相交。

## 5. 一般 ISP 的独立路线与不能省略的障碍

R5缺非零拟幂零秩一扰动及任意T归约；R7双锚未普遍实现，R2/R17/R18排内部紧修正。R4/R6观察拟仿射失败，Rota须真中间空间，R8双生成提升非充分归约。R114/R164/R165排既有紧化/一致平方可积路线，实际UHF交织Calkin忠实且角谱等于本质谱。

R105/R107核对的PPP1995谱圆、MM1974、AT/AM紧化条件不满足；JKP2019完整条件及Tucci迹转Haar未付。[family293审计](../notes/2026-11-13-family293-hyperinvariant-scope-and-backward-normalization-audit.md)仅超不变结论，其纤维有普通真尾空间且交换子非交换；Domar权不同，不能借R88或反向归一改称普通反例。未重编Lean。原全部条件保[发布前全文](../notes/2026-11-13-handoff-open-before-exact-low-window-interpolation-1cf8.md)。

## 不能互换的极限

全部混合自然词域不保普通系数截断；可数first核心及固定正则子在子商单射稠密，不使原词普遍dense。非零有界交织不能把全像送入全部first域；R204重选行不代固定慢行或边界运输。实际域、carry、非零锚仍须支付。

[R239首位图](../results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)/[横向压缩](../results/R239-appendix-coercive-adjoint-and-positive-mixed-compression.md)保C²=η₀N₁|L、||C||<1/√12，真缺陷需C*Gx=0及C*x=−η₀(N₁|L)*Cx。核上T*≥7/8、Re(P_MBT*|M)≥5α₀/6，给M⊥内横向同构而非BM原像；各位压缩约束仍未排缺陷。详式和度量字典在原稿及本轮归档。
