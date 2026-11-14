# 二位标量消元前的交接和开放问题

2026-11-13 05:46:04 UTC；固定main 49e9ef8cd803bb9fc122262b7e3c8e64b5ea476f。全文保留，链接按notes位置调整。

## 原 HANDOFF.md

# 交接

## 目标、负责人和规则检查点

- **目标未完成：** 必须完整解决可分无穷维复Hilbert普通ISP。Haar普通不变格、边界N=M及一般正常湮灭者仍未知；规范单模式全部多项式加权输入现已循环。不降低README完成标准，不以阶段或时长收尾。
- **负责人及分工：** Astra-ISP-1cf8c51d负责，0c继续贡献。1cf用R213–229、R240–271；0c用R230–239。新编号先登记，独占git/index，不动他人未发布文件。
- **最后实际pull/规则：** 2026-11-13 01:06:52 UTC，cdb9429c93f969d1054d8e1e49643add83457c24；真实git pull --rebase origin main，两README差异空。每小时至少一次，终端恢复即补。
- **0c 最近实际 pull：** 01:06:17 UTC / bfe9f2c0b2977d4bab3d14793c3f247374e81303，两README差异空。02:06:00、03:05:54、03:31:22、04:23:57、05:20:35的真实pull调用均在执行前报No usable execution environment；API非pull，恢复立即补。
- **已读规则blob：** 根 f787a306d90892d8dec765dc59747d60ba39f055；题 6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd。每次实际pull均比较两README，有变只读差异立即照做并记SHA；至少每小时pull。
- **API后备检查点：** 2026-11-13 05:44:27 UTC / main a08e2093a7ebab7b972b38e1e9a78e15b7c224bf，两README blob同上未变；API非pull，终端恢复即补。
- **发布：** 完整结论单独推；终端可用用git，拒推即pull --rebase。仅失联用根§8小文本；API不算pull。令牌仅命令行，不写文件/config/提交；不force、不写根LOG；Markdown<100KB、H<10KB，合并最新main。

## 恢复记录与模型

工作树：1cf /tmp/isp-1cf8c51d-math-research；0c /tmp/isp-0c017065-math-research-20261113-0030。[本次前H/open全文](../notes/2026-11-13-handoff-open-before-auxiliary-scale-circle-0c.md)保旧文/归档链。

模型：H=L²(Z₂)，A为真实Haar加权odometer；N_j=A^(2^j)/d_j=E_j+η_jE_j*N_(j+1)，η_j≤e^(−770·16^j)，Y=N/(1+N)、V=I−2Y，V_J1=χ_J。Haar/边界E为e₁₀/e₀₁。A′交换、C对称，R88有界SOT多项式逼近。UHF仅运输全空间；未知限制像、C保核/局部等向不免费，危险平方保a_*=0。

## 1. 原 Haar 正常湮灭者

S_N/Y全H单射稠密已证，普遍强主理想仍开。失败有正有限秩正常见证；R228/229反例排抽象降秩一，R242窄矩阵/垂直商图已付但不免费图稠密。
**R255最优端点：** r=√3的正正常真空分解已付真实carry/最小闭域，排E_√3有限见证；更小r无统一乘法界，且有正秩一态无因子（非湮灭者）。一般正常性不保此矩。
R235原保函数非负锥与R237 Walsh对角/有限带/entrywise-ℓ¹及可实现乘积基类仍有效；均不扩一般正常态。

**R235相对迹/能量：** 连续/a.e.+双边UI、g(v₂)=o(n^3/4)已排，一般L∞非湮灭反例不扩真态。真湮灭必u_m²+v_m²≥λ_m−2λε_m、(2^(2^m)+1)δ_m≥λ(1−2ε_m)，全G∈A′的|φ(T_mG)|≤h_mλε_m||G||；待预算内右因子反驳。
**R237相对密度：** 固定Q∈Acal的QAcal同范数强/强*逼近QA′，q_m可搜索完整尾交换子；不含非UHF左因子或无界右因子。
R248阻尼D不交换；R250稀疏图未证A+不变。其逆D域零、余图闭像非紧及矩下界退化已付，不能撤阻尼或自动配对。
**R253/R237尾右测试：** 真湮灭者迫q_m↓0；正右因子Σc_BN_B在|B|≤b_m≤2^(4m)等预算内仍真空比指数衰减，最高物理位不限。该锥上界不限制完整q_m；复杂相位/一般A′右因子仍开。
**R244：** 正真空锚及秩一σ(MU+F)=C仍保。广义Ri付Mi=Ri⁻¹Di，共同R理想/像/Γ_R参数无关；真空原像⇔全部无重复自然子词域。新有限秩：P_i=∏_(k≠i)Ri付所有指定输入，ΣMjP_i fj=0、φ(P_i A′)=0，不能再删第二因子。rank2交叉R1f2/R2f1域、单Ri理想湮灭及Q向量配对已付；Q有J²=−I、无循环向量，Γ_R⊊Γ_min⊊Γ_max两商∞。仍缺Cf交叉域/真空，未赋商正密度；旧聚合全Gram准则保。
**R267/A–D：** 原逆积Pg=1；前向块可1∉RanP。第四附录零参数平顶积非零且P=A^rR_r对全部r，PW_n收缩强*趋I，有限旗子商单射稠密。F_A=∩A^rA′同范数强*稠密、AF_A=F_A、F_A∩UHF=0；共同幂原像为有限闭交换域图核心。P无真空原像；指定配对等价Σ_J|φ(PV_J)|²有限，真湮灭矩及S分母仍开。
**R230固定态块界：** 同一非湮灭f、q_i=16^i排全部纯交换可逆收缩块的合格收敛逆源，完整实际Gram比值指数log5/2，有限完整源组合亦排。负实g∉H_√3；非块/无真空原像未覆盖。
**R230真密度/证书：** m_B=L_Bρ_B、LL*=[[2,2],[2,6]]^⊗n；全列carry及真全G残量已付，纯右列必须保非正交叉约化ρT_m。Slater正对偶给δ_m≥λ(1−μ)−||u||||T*m_B||，理想内近真空收缩a<1/2可给正余量。任意n位统一范数定位却有τC_n≥√(2^m)/144→∞，最优正密度常数亦C_n≥5^(n/2)。全空间右因子/真密度专属仍开，完整常数保R230正式附录。
**R230/261规范族：** 非负ℓ²控制非零收缩积，完整次数逆e^{o√q}，β<1/2共同域非像；普遍配对/分母已排，专属仍开。

**R253/263：** 全A^r不能有界除S；同一H_(1/(60e²))向量不在两RanS，规范/全域分母已排，专属仍开。

## 2. 两个实际边界的 N=M

T=T_N,T_Y，M=kerT，N=closure BM，D=M⊖N。R187/200给M∩RanB^r⊂N，有限孔核仅真空；R234模N已闭，R238原J_q成本不能当模N成本。环境坏见证在M⊥，横向T*M同构不是BM原像；旧通量/头Jordan/平方γ各保原范围，详归档。
**R239全q/最小能量：** R271先得log^(4/3)权阶。原η/大窗低投影e−74d⁴、真实lift e−75d⁴；d≈log^(1/3)q，K*=3(16/770)^(1/3)。c>K*权核入N、真D尾常数K*/2；Σ1/[ell(1+λ²)]发散足N，所需无权增长未得。G=FF*=D0P_kerS D0*，实际r=Avq自动D^d，λ²=〈G⁻¹r,r〉；压缩须真Schur补。窄带正/倒能量仍容慢尾。
**局部最优/真实原始块：** 全低输出最小能量logΛ=Θ(log^(4/3)q)，无限尾亦然；改选实际头的坏单位v还满足||P_Mv||→0。新相容真空b_t保Db_t=b_(t−1)、||b_t||²≤K/(t!S_J^t)，J=m+2q时K→1。任意前缀中间投影P且D_IP=PD_I=0给真实λ^P≤√K||P||[τ_q+√d e−72d⁴||w||]→0；原λ与补块λ差亦→0。2r位均权原始投影经实际对角相似/张量，r=floor(m^.25)使||P||→1、log rank=(2log2−o1)q。完整固定前缀投影唯一且||P_full||≥(q+1)⁻¹[((m+2q)!m!)/((m+q)!)²]²=e^((4log2−o1)q)，不能据高秩补全稳定覆盖。
**闭链/剩余泄漏：** 相容Rt给RanS/S*闭、头旗Riccati准确G。真实核仅余末端〈w_(q+d+1),D*z_d〉及carry×对偶范数；Tr((A*)†)非零排幂零截断。加宽Gram正罚项/固定m有限窗降至无限尾均付，无统一速率。其余原始方向和删除链仍开。

**R271：** 平方旧跨头Smith(2d−1,2d+1)、新4d排稠密像D交织；单上块修复仍依Q。新原线性残量范围R=⊕_(i<d−1)e_i kerD^(d−i−1)，原正交基、必要充分；全部可行链还满足i≤d−t、D^(d−i)c_ti=0。Gflag=D0P_KflagD0*是旧G对整个R⊥的Schur补，完整对偶inf仍待统一下界。

## 3. 危险核、中央闭图与系数行

**先扣旧范围：** R134/R138/R155：非ℓ¹且存在θ使Σ(|a|−Re(e^−iθa))有限，则first空谱；任意有界A′扰动/首一有界系数自然多项式有真正有界逆，全部未知不变限制保持域并双射。任意复ℓ²权/ℓ¹辅助早已覆盖，同射线不重计。ℓ¹且a*+Σa≠0时近共振目标为Acal单位。
**R268–270：** 非首一G[X_b]最大闭包/排核/全H循环iff底座归R152/183；有限R^L核核心，不称自然域闭。R270B二阶消去给θ=2与全F_p，E给独立超三次快辅助Σh_kF_k；任意排列/重叠均付。R236零输出分类保来源。R270F允许物理不交慢模式已知点态因子相乘，纯平移幂适用；共享有限头只保单atom。
**R236全阶偏离/字符互素：** 任意a,b∈ℓ²、c∈ℓ¹的F_q+v_c−λ：早偏离给全λ；否则α=a_ja、δ=c_ja，gcd(q−λ,αq'+δ)=1足循环，至多p−1个核候选。有限dyadic差真实提出A幂，核内字符单位/R151/C配对排核，不除G_n本体。p≥2且j_c≤j_a全部闭合；二次仅候选λ*=(δ/2α)²有真零例，late-c留λ0；p1须防α+δ=0。
**首c较晚的实际预算：** 固定盘：无限S上|a/c|≤K、辅助排序L_N=O(N^1.5)，核内整逆给循环。新辅助圆：δ_N=c_N*、r_N=εNδ_N²，双删除后共同二重Cauchy只付一次B/Y；L_N=O(N^1.5)、Γ_Y(r_N)=O(N²)足循环，主a可任意ℓ²。含辅助双侧伸缩指数0<α≤1及Σ_(n>N)c_n*=o(Nδ_N²)、L_N=O(N)长平台；旧主尺度/子支撑准则保原独立范围。一般late-c临界仍待双池新稿。
**其余界：** R259/260/R264–266的解析简单根/α≤1重数保原范围。R236双导子投影不直接排核，1<α<3的Leibniz末短和未控，两位校准排粗吸收。α>3及α=3大β特例属旧快类；单个四次幂界不是G。剩余1<α≤3扣除旧特例；中央旧域/运输/family293与详式保正式稿/归档。


## 紧接稿及持续执行

1cf已推R147 10543bf9、R271旗51b2adb6；本次推R244删一分母。待核插值252a641ee319b6d22836767a154c529e9de368aa；代理续联合旗能量、first谱集中及最小比例图。
0c边界三稿f52bafce已回读；本次辅助圆完整稿。二位Bézout08f5414b2ccb96cc6a97528a7a4b8fa7095cc91c已独核待推，可闭规则慢幂迟首位二次；全阶扩展另核。三代理继续真实补块、不规则偏离和全空间右因子。
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

[压缩前全文](../notes/2026-11-13-open-after-R262-rebase-before-condense-1cf8.md)及results.md保留全部旧接口。以下列五组原问题及当前三接口。

## 共同适用边界

R125/R128/R140/R176/R184已付清真实闭域、通常伴随、自然多项式和共同正则器。全H单射稠密不自动传未知不变限制或有限放大子商；G的普遍范围不能扩成一般慢Acal。UHF只运输全空间范数，不运输未知Haar子空间。Haar正常态、边界奇异态、固定次数和实际全部向量不可混同。危险平方点态应用始终保留a_*=0；全等向不能换成局部等向，C未必保M，压缩交换子不能丢中央耦合。所有“已证明”均为中间结论。

## 当前接口一：原 Haar 慢符号的正常湮灭者

[删一预解因子](../results/R244-appendix-cofactor-input-domains-and-individual-resolvent-annihilation.md)：真有限秩矩迫每个P_i=∏_(k≠i)Ri满足P_i f_j∈DomMj、ΣMjP_i f_j=0及φ(P_i A′)=0。rank2即单Ri理想湮灭，并有准确商向量配对；未得Cf交叉域，不能再删第二因子。

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**已经排除的类。** [R255最优次数端点](../results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)给E_√3(ρ)=Σ3^|F|〈ρχ_F,χ_F〉有限时的真实真空分解并排正湮灭者；carry、最小域及非负张量化均付。√3端点最优，较小r的正秩一反例不是湮灭者。一般正常性/有限秩不保此矩；R235另排保非负锥的正态，Hilbert正或C实不蕴含保锥。

**相对迹的范围与真湮灭约束。** [连续核](../results/R235-appendix-continuous-kernel-relative-tail-traces.md)及[正尾耦合](../results/R235-appendix-tail-couplings-almost-everywhere-continuity-and-bounded-obstruction.md)排连续核、a.e.连续有界F、双边UI无界F及g(v₂)=o(n^3/4)类；恒模正秩一负极限证明一般L∞不够。[真湮灭能量](../results/R235-appendix-annihilator-tail-coupling-energy-and-right-tests.md)无需正则性即给u_m²+v_m²≥λ_m−2λε_m、(2^(2^m)+1)δ_m≥λ(1−2ε_m)，且对全部G∈A′有|φ(T_mG)|/h_m≤λε_m||G||。下一步须从真矩方程找到预算ε_m||G_m||→0而耦合配对非零的实际右因子，不能替换为任意点乘相位或普通L²逼近。

[R237及附录](../results/R237-actual-walsh-diagonal-normal-module-and-slow-annihilator-exclusion.md)排Walsh对角、有限翻转带、entrywise-ℓ¹及可实现正交乘积基（Σ|ν_j|²<∞）中的对角/有限头块正态，含无指数次数矩例。复密度仅推出A′功能及迹零，正性才给ρ=0；任意基混合及一般正常态不自动覆盖。C实循环秩一态可无ℓ¹对角表示。

**当前配对条件。** R244逐列域Rf_i∈DomX_Cfi加非零锚足排见证；[聚合逆图](../results/R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)在Pg=1及强单位下将指定真空表示等价为有限Walsh全Gram有界。真实逆图已付；真湮灭必须对每个P使全Gram发散，正常性不够。

[预解图与正真空锚](../results/R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md)给RH⊂∩DomMi、Rg=1时正锚Trρ，秩一真湮灭必σ(MU+F)=C。[广义预解与有限词域](../results/R244-appendix-generalized-resolvent-unit-classes-and-vacuum-word-domains.md)给任意Li=MiUi+Fi的实际预解Ri满足Bézout恒等式及Mi=Ri⁻¹Di最大商；共同R=∏Ri的代数主理想、实际值域与Γ_R不随全部允许选择改变。真见证迫Γ_R距真空≥√Trρ，虽各单图投影稠密。1∈RH等价某个排列全部至多2^r个无重复自然子词在1上有定义，亦等价所有排列；rank2还原两交叉域。**无广义预解分支或共同高阶域缺口尚未排除，调参数不能改变它。**

[秩二有界链](../results/R244-appendix-rank-two-koszul-defect-and-double-common-graph-gap.md)的Q有J²=−I、JT=T*J，非零Q无限维且无循环向量。真rank2正迹迫Γ_R⊊Γ_min⊊Γ_max，两商无限维；Ri_Q=0、Di_Q单位。仍须由实际正矩证明共同最小图达最大交域或链正合。

[R267 Blaschke逆族](../results/R267-appendix-blaschke-block-strong-units-and-linear-degree-inverse-type.md)有Pg=1和收缩强单位，逆线性下型κ=log(4/3)−1/4；[前向族](../results/R267-appendix-forward-blaschke-strong-units-without-vacuum-preimage.md)则1∉RanP但全部有限旗子商单射稠密，完整逆范数carry已付。原逐列配对可用；R244聚合逆图仅适用于有真空原像者。指定全列矩及S分母仍开。

[R267第四附录](../results/R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)给同一非零收缩P∈∩A^rA′、PW_n收缩强*趋I，有限旗子商单射稠密。该理想同范数强*稠密、AF_A=F_A、F_A∩UHF=0；共同幂原像为有限闭交换域的图核心，不是PH自动入域。1∉RanP，配对⇔Σ_J|φ(PV_J)|²有限；用P1作第二向量会取消正则化。真湮灭专属全矩界及P∈SA′仍开。

**固定非湮灭态的完整块边界。** [R230完整Gram](../results/R230-appendix-arbitrary-contractive-block-gram-and-complete-source-obstruction.md)对同一f、q_i=16^i排所有纯交换有限块可逆收缩的合格收敛逆源：原实际最优列比值指数log5/2，有限完整源组合亦排。[负实粗源](../results/R230-appendix-negative-real-rough-sources-and-large-column-obstructions.md)的真实g∉H_√3保留；无真空原像/非块路线未覆盖。

**任意真密度的完整矩与正性。** [R230新附录](../results/R230-appendix-positive-density-moments-dual-certificates-and-localization-obstruction.md)给m_B=L_Bρ_B=ΣTr(ρ_BD_F*)χ_F，任意R的完整Gram为||R*m_B||；LL*=[[2,2],[2,6]]^⊗n，K_n=(4+2√2)^(n/2)，实际全部列误差≤λd_B、d_B=8n(3√2)^nη_minB。正常尾只给||m_B−λΩ||≤2K_n√(λδ_m)，没有指数速率，也没有固定相干分量。

R235全G湮灭给完整实际右残量≤λε_m(K_n+d_B)，纯列另付λκ_md_B，κ_m=||T_m||/h_m。它依赖非正交叉约化Tr_(B^c)(ρT_m)/h_m，不能仅凭ρ_B写成K_B*m_B；后一步另需全空间定位τ并付λτK_n。

**正性证书与被排除的定位法。** 有限块零字符T的准确对偶为inf{μ:μI−ΠΩ+Re(TX_u)≥0}，规范迹严格可行；证书给δ_m≥λ(1−μ)−||u||||T*m_B||。若理想内R=TX_v收缩且||RΩ−Ω||≤a<1/2，则显式μ=(1+a)/(2−a)、u=v/(2−a)。预算内全空间右因子仍待构造。

同时[一次尾定位障碍](../notes/2026-11-13-first-tail-obstruction-to-uniform-full-moment-localization-normal-complex.md)对任意n物理位上的任意有界K_B，q=2^m，有τ≥q²/[8√3(n+2q+1)^(3/2)]。即使最优统一正密度矩常数C_n也≥5^(n/2)，因此τC_n≥√q/144→∞；不仅粗K_n费用失败。不能先范数截块再对全部密度统一放大。继续保留全空间T_m和非正交叉密度，或证明真湮灭密度专属消去；本障碍不限制后二者。

R242窄矩阵图非全域，普通稠密不代图稠密。R248阻尼D不交换，撤阻尼/Sδ单射未得，纯常数核反阻尼违反正常高位消失；R250稀疏图逆域零、余图闭像非紧且矩界退化，未证A+不变。详式保归档。

**不能再用的捷径。** R228/229及9维例排C实化和任意降秩一；R240固定连续正循环态排有限/规范正first族的普遍真空配对，但该态非湮灭者。有限组合、两端可变分解和真湮灭者专属R仍开，原量词保正式稿/归档。

R210–211奇异正态/Cantor族不具Haar正常性；固定正则端、Fock及增生平滑等旧障碍保归档，不代表真实正常矩。


[R253相位消元](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)给I⊗Q_m∈S Acal及真正常见证必要q_m↓0。[非负右因子障碍](../results/R237-appendix-nonnegative-tail-right-factors-and-vacuum-ratio-obstruction.md)在|B|≤b_m、limsup b_m/2^(4m)<770/(16log2)时统一给真空比≤3(1+1/√2)^−floor(2^(2m/3)/4)，最高位不限；完整相位/一般尾A′因子下界仍开，不能把该锥当完整q_m。


[R253域附录](../results/R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md)：真实图carry已付，D∞不含RanS；有限first预解积非S有界右倍数，专属配对仍开。

**已排除的通用正则化。** R230/R261规范正积的累计ℓ²、完整逆e^{o√q}及共同子半次数域非像，旧Cayley方向增益、R253全A^r有界除S失败和R263同一H_(1/(60e²))向量不在两RanS，均保于[本次完整归档](../notes/2026-11-13-handoff-open-before-residual-flags-1cf8.md)及results原稿。像含该小指数域的有界分母不能除S；这些结论不排真见证专属配对。



[R237相对主理想密度](../results/R237-appendix-asymptotically-contractive-principal-ideal-approximation.md)对固定Q∈Acal付QAcal同范数强/强*逼近QA′，q_m可搜全部尾A′；非UHF左因子/无界右因子不覆盖。R230/R263已排规范无限正积为Q_m有界倍数，一般右因子仍开。



## 当前接口二：实际边界的除法饱和

固定两个实际边界T_N/T_Y，M=kerT、N=closure BM、D=M⊖N。R187/200已给各有限稳定像及M∩RanB^r⊂N，有限孔核仅真空；真正问题是**无权核内稠密与N=M**，不将环境有限孔稠密当核内核心。

**旧接口保原范围。** R234模N已闭；[R238原J_q](../results/R238-actual-slow-formal-inverse-fixed-hole-layers-and-canonical-right-inverses.md)成本不等于R239已付模N成本。环境Γ坏见证在M⊥、横向T*M不是BM原像；真幂界只用真H输入，不能取消头Jordan/旧链与未知尾。全部旧预算、平方γ及不同窗口范数保于[全文归档](../notes/2026-11-13-handoff-open-before-exact-boundary-gram-0c.md)和原正式稿。

**全整数窗口和真正最小Gram。** [R239全q](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原η_(m−1)、q≤exp(d³/4)，低投影e−74d⁴/真实lift e−75d⁴；每整数q取d≈log^(1/3)q，K*=3(16/770)^(1/3)给c>K*权核入N、真D全序列尾常数K*/2，权阶先属R271。原最小λ修复窗口ell=d+m的覆盖≤2使Σ1/[ell(1+λ²)]发散足N；真D倒能量≤8τ_Q²/||w||⁴，λ²=O(q log^(2/3)q loglogq)足但未得。

[准确Gram](../results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)：S c=(Ac1+Dc2,…,Acd)、K=kerS、F c=Dc1满射，G=FF*严格正。实际r=Avq由D^kr=(−1)^kA^(k+1)v_(q−k)自动D^d，λ²=〈G⁻¹r,r〉。伴随链与消kerA*的Schur补不可省；窄输入带覆盖≤4的正能量结合倒能量仍允许慢尾。逐头残量仅(Kp k1,0)、旧d核阶/保底块；Tr(ApKp)≠0排纯头交换子修复。

**局部最优障碍与真实坏方向的分离。** [原局部能量](../results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)给全部低输出单位球logΛ_q=Θ(log^(4/3)q)，任意有限/无限高尾都保下界，c0≈.1747818至K*。[新完整附录](../results/R239-appendix-unweighted-primitive-removal-high-rank-blocks-and-full-projection-obstruction.md)改选x=(A*)^te0/||(A*)^te0||，相同坏单位v满足||P_Mv||≤2/√(m+1)+exp(−(c0−o1)log^(4/3)q)→0；原C=P_V|M，准确C*v=P_Mv。该族并非真实核内坏向量。

**真实原始分量现可无权消去。** 后尾J=m+2q的同一相容真空原像满足Db_t=b_(t−1)、||b_t||²≤K/(t!S_J^t)，K≤exp(2d²/J^.75+8d/J^.25)→1。配对原始源的有限/无限真正最小能量由ρ²Q与KQ夹住。更一般，任意前缀q孔投影P满足D_IP=PD_I=0时，真实源Pr有合法修复λ^P≤√K||P||[τ_q(w)+√d e−72d⁴||w||]；若||P||受控则趋零，且|λ−λ^(I−P)|≤λ^P。完整D_m仅与P交换，不把D_mP写成零。

**高秩扩块与完整前缀障碍。** 每2r位均权中间原始正交投影经实际对角相似后，log||P_block||≤2048r⁴/(j+1)²；张量到前2q位给||P_q^(r)||≤exp(2048r³/(m+1))，rank=Cat(r)^floor(q/r)Cat(q mod r)。取r=floor(m^.25)，范数趋1、log rank=(2log2−o1)q，上述全部真实分量均有无权小修复。可完整覆盖中间原始空间的投影却唯一，其互补子集矩阵元给||P_full||≥(q+1)⁻¹[((m+2q)!m!)/((m+q)!)²]²=exp((4log2−o1)q)。同前缀完整分析/重构乘积亦必指数大；高秩不等于稳定覆盖，继续真实范围/移动前缀和其余删除链。

**完整链仍缺的控制。** [闭链/Riccati](../results/R239-appendix-closed-repair-chain-riccati-and-terminal-leakage.md)付固定尾塔闭像、极小伴随链取得、准确头旗Gram。真实配对余项恰为末端〈w_(q+d+1),D*z_d〉及carry乘对偶范数；两型实际Tr((A*)†)=−(d−2)c2≠0，不可用A^d=0截断。加宽Gram为旧能量加正末端罚项、固定m有限最小值下降至无限尾，但无统一速率。无权N=M仍开。

[R271平方局部型](../results/R271-appendix-square-head-smith-types-and-old-head-single-block-correction.md)给旧跨头Smith(2d−1,2d+1)、新4d，排稠密像D交织。固定混合核有限孔/正指数核心不传原核；上角残量可用旧d头修复，最多增2d孔但成本仍依Q。

[R271残量正交旗](../results/R271-appendix-orthogonal-residual-flags-and-exact-source-gram.md)：整个低输出残量范围准确R=⊕_(i<d−1)e_i kerD^(d−i−1)，必要与充分均付；原正交坐标无Jordan条件数。全部可行链自动有i≤d−t、D^(d−i)c_ti=0，故Gflag=D0P_KflagD0*准确等于旧G对整个R⊥的Schur补。对偶inf保全部伴随链，不以环境D*替换；**真实旗Gram统一下界与N=M仍开。**

## 当前接口三：规范单模式全部重数已关闭，继续一般行与多个模式

[R147慢辅助首位切片](../results/R147-appendix-bounded-slow-auxiliary-slices-and-polynomial-cyclicity.md)：任意ℓ²主/权、有限ℓ¹辅助，最高系数r_p(β)≠0，首联合位F(z,β)与F(z−2a,β−2c)互素即循环。全部(F−λ)^m仅留有限切片碰撞值；真Bell/有界A^h差商/深域消元均付，无空谱/熵/辅助尾率。不可约慢例u³+v²仅留2±10/(3√3)。R236全阶共振加偏离判据归其原结果；最高字符零、晚首碰撞及双无界仍开。

**既有单模式。** [R236](../results/R236-appendix-all-multiplicities-of-canonical-weighted-polynomials.md)的规范、临界弱ℓ¹、σ>1幂尾及α≤1指数子序列类均已闭，全部真实域/重数证明保留；R268给更广准则。

**更多排序行。** [R268](../results/R268-entropy-budget-weak-l1-bandwidth-and-all-multiplicity-cyclicity.md)沿N满足sup_(k≥N)kρ_k≤DNρ_N、Σ_(k≤N)log(ρ_k/ρ_N)=O(N²)、logρ_N⁻¹=O(N^1.5)，则全部q(u)e^w循环。实际成本E_N+log^(4/3)ρ_N⁻¹+N²及jets/ad域已付；未满足准则的little行、1<α≤3剩余带仍开。

[R269](../results/R269-analytic-a-coefficient-bell-polynomials-and-finite-head-multimode-cyclicity.md)给熵主行解析A首一/有限头点乘及ℓ¹主行有限头P；[R270A](../results/R270-appendix-maximal-root-multiplicity-and-same-order-nonresonance.md)按最大根重数μ许c=O(|a|^max(2,μ))，最高重根保复比例非共振，小o无需速率。

[R270第二附录](../results/R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md)付局部二阶消去∈G。[第三附录](../results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md)的§§1–8独立重证R183无界/R152有界G[X_b]排核；新增应用在§§9–10：θ=2及F_p=p![t^p]exp[tu+Σ_(n≥2)2^(n−1)t^n v_n/n]、v_n=Σa_j^n(χ_j−1)的全部非零有限线性组合循环。无限主支撑自动非零，单支撑a*=−a保真实零例。

[第四附录](../results/R270-appendix-arbitrary-fast-leading-coefficients-maximal-closure-and-cyclicity.md)重证R183无界/R152有界已付的非首一G[X_b]：最大闭包C自伴、单射稠密、全H循环iff；只在R^L M配对，不假设D∞或自然域闭。无界非零据R171。[范围审计](../notes/2026-11-13-r184-r186-scope-audit-and-finite-word-subquotient-corollaries-kernel.md)同时扣除R184/R186旧联合域；任意词、矩形分母及多模式子商仅为推论。

[第五附录](../results/R270-appendix-fast-auxiliary-modes-and-resonant-polynomial-modules.md)给任意ℓ²主/权及独立超三次快辅助z的Σh_k(z)F_k非零组合循环；p≤1去掉R157的ℓ¹主行，不需最高快字符锚。全重叠mixed jets、一次快项/二阶carry的G归属及自然域均付；高阶仍限明确共振F_k，普通q(u)慢Bell与一般独立慢辅助未全闭。

[R236零输出分类](../results/R236-appendix-resonant-polynomial-zero-output-and-leading-order.md)：a∈ℓ¹、s=a*+Σa、μ=mult_s q、L=支撑数，T_q=Σq^(r)(s)e_r(a_j(R_j−I))为零⇔L<μ；非零首阶为最早μ个位的2^j之和，μ=0为单位。无限支撑循环及二次关闭归R270C。

**全阶可和偏离的字符互素。** [R236完整定理](../results/R236-appendix-real-dyadic-factor-character-coprimality-and-all-order-deviations.md)对非零主行a及任意复a,b∈ℓ²、c∈ℓ¹，研究(F_q+v_c−λ)e^w、deg q=p≥2。首c早于首a给全部λ；否则α=a_ja、δ=c_ja，gcd(q−λ,αq'+δ)=1足循环，至多p−1个核候选{q(z):αq'(z)+δ=0}。有限dyadic差真实提出A幂，核内字符单位加R151/C/Fourier排核；不除G_n本体，不把单射稠密称预解。

**已闭与临界。** p≥2且j_c≤j_a时(F_p+v_c)e^w全部循环，无尾预算，含全行κ>2及交替慢幂1/2<σ<1；空主行退化见[二次原定理](../results/R236-appendix-earliest-support-dyadic-quadratic-cyclicity.md)。二次仅余λ*=(δ/2α)²，单位置确有零输出例。late-c的所有λ≠0已闭，λ0仍开；一般q−λ平方自由亦闭。p1可能抵消，c0旧共振非零结论不重列开放。遗漏首位的纯κ慢幂临界核仍需真实限制密度，移出低头会留下2H X'。

**旧主尺度与固定盘准则。** [主尺度共同圆](../results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)/[子支撑](../results/R236-appendix-supported-deviation-arbitrary-background-and-empty-spectrum-scope.md)保原假设和物理排列；不把辅助排序偷换为主排序。[固定盘核内逆](../results/R236-appendix-fixed-disk-kernel-inverses-and-sparse-linear-deviations.md)只需无限S⊂{c≠0}上|a/c|≤K、S辅助排序L_N=O(N^1.5)，S外任意ℓ²主/ℓ¹辅助。核内整逆、双删除与真实jets均付，允许指数稀疏线性偏离及任意其余尾。

**独立辅助尺度共同圆。** [新完整定理](../results/R236-appendix-auxiliary-scale-joint-resolvent-and-independent-tail-gaps.md)取全部辅助排序δ_N=c_N*，r_N=εNδ_N²、L_N=1+log⁺δ_N⁻¹。从辅助前N位同时删主最大N/4及物理低N/4，余位|a|≤2||a||₂/√N；在同一双圆一次求值∏[1−(2a_j/c_j)²(B−Y)]⁻¹，只付Γ_B(r_N)+Γ_Y(r_N)。若L_N=O(N^1.5)、Γ_Y(r_N)=O(N²)，任意独立a,b∈ℓ²的二次偏离循环。核上逆/全部域与固定小θ四次预算保持原空间。

原正锥与全复方向Laplace预算给两类明确辅助：双侧排序伸缩指数0<α≤1，或沿N有L_N=O(N)且Σ_(n>N)c_n*=o(Nδ_N²)。后者含N_k=2^(p^k)、c_n*=N_k^−ν分块，ν>1、p>(2ν−1)/(ν−1)。c0=0可遗漏主首位，主行仍任意；正相位指数例的Y∉G已由τ₄反证付清。规则慢幂纯κ的更强新闭合接下一份双池稿，不由本共同圆宣称。

**既有空谱锚须先扣除。** [完整范围核对](../notes/2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)直接按R134/R138/R155：a非ℓ¹而某θ的Σ(|a|−Re(e^−iθa))可和时，first已空谱，任意有界A′扰动和首一有界交换系数多项式均在指定自然域有有界逆；逆与域保持全部未知不变限制。故近共振对任意c∈ℓ¹、任意复ℓ²指数权早已循环，不要求相位/辅助预算；同射线例不登记新增。a∈ℓ¹且a*+Σa≠0时目标是范数代数单位。真正剩余是居中有界行与全平面连续谱慢分支，不能借R259解析分支处理未经支付的二次分歧平方根。

R224公共像及未知尾商度量障碍保原范围。

[R257/258](../results/R258-entire-selfadjoint-kernel-transport-and-actual-tail-mobius-domains.md)付真实伴随/整自伴核运输、UM矩及闭核尾Möbius域，不回传原M点乘域或不变格。

[R259](../results/R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)闭同幂尾p>1/2；[R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)闭排序limsup nρ_n>0的任意复行及物理重排，允许全部复first指数和有限联合解析Bell芽。其完整域导子代数无maxF成本；剩余解析分支须nρ_n→0且排序复和→Φ(0)，一般行重根另证。

[R264–266](../results/R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md)已闭α≤3/2的解析Bell/简单根及α≤1全重数；R268严格扩展后，规则1<α≤3/2的普通点态全部重数仍开。

**高阶导子及剩余短和。** [纯提升障碍](../results/R236-appendix-high-degree-raising-band-obstruction-and-range-projections.md)给r≫√Q的有界提升弱趋0；[全域双导子](../results/R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)付[ad_T^(2r)U_N](../C_Q^r)†强趋I、r=ηQ<Q/2、伪逆≤e^(Q/2)及全部carry。它不是单个导子像；核配对完整Leibniz在1<α<3尚余末O(N^((1+α)/4))项。[两位校准](../notes/2026-11-13-two-bit-pseudoinverse-calibration-central-next.md)排共同尺度粗吸收；须核内抵消或适配降阶，α=3不自动短段。

**旧快类。** [R236核查](../results/R236-appendix-existing-fast-classes-for-supercubic-sorted-rows.md)据R175：排序ρ_k≤Be^(−βk^α)、α>3已给非零q(u)e^w循环及标准主理想/普遍表示，无需下界。α=3时首阶r的β>80r⁴/3给限制稠密/强主理想，β>400r⁴给标准范数理想；均严格充分。单个四次幂界不等于G。剩余1<α≤3须扣这些旧例。

[R270第六附录](../results/R270-appendix-disjoint-slow-point-polynomial-products-and-head-masks.md)：物理不交慢模式的已知点态循环因子可相乘，故∏(uν−λν)^mν e^w循环。mixed词域/Bell已付，共享有限头仅保单atom；同模不同根、atoms之和不能这样相乘。

## 1. 一般向量的矩分离与有限二阶以上输入

R101完成有限Walsh次数两端的全矩分离；任意非零L²向量对实际A的循环性仍开，一般无限次数没有最高系数锚。一般二阶闭乘子的核、gauge差Qζ在未知核上的稠密像、两个独立慢方向和一般慢平方共振仍未闭。R130/R131二阶闭域与R143合法跨核配对已付；Δ=closure(A^hX_g)域可能严格更大，不能取消A^h后直接加入DomX_g。

R29/R44/R51平滑障碍、R163/R165对固定Lp(p>2)/超二次Orlicz的限制交织障碍保留。有限柱近交换不能升为归一化N_j精确交织；R255/R237均只排明确正常态子类。

## 2. 不变限制中的一阶闭乘子值域

对R125闭一阶X_a及任意非零闭不变M，R128已给真实闭稠密限制X_(a,M)、保M的收缩正则R(t)与有界S(t)=X_aR(t)。**任意复ℓ²非零行是否总有closureRanX_(a,M)=M仍开。** R140准确化为closureS(t)M，固定R(t)M是真图核心；全H单射稠密不能代该结论。C未必保M，四个正分量的稠密像不能传复杂线性组合。

正系数、可和相位缺陷的非ℓ¹类和已知特殊可逆类已完成；全C谱不决定限制像。R151的G在全部不变子商及有限放大普遍dense、R140明确四次尾型和80/3幂类亦已闭，但不能把任意慢S(t)收入G。共同C对称Volterra双倍反例排一般捷径；其平方零不属于实际Acal。R143无界gauge域步骤已付，实际限制像仍决定有限Fourier支撑推进。

## 3. 任意有界有限 chaos、范数代数及完整交换子

每个非零X∈Acal是否单射稠密、一般A′元素是否无非零核仍未知。R32无零因子仅在代数内部；R88纯/真实对应不保乘法或核。R92固定有限chaos有界乘子恰对应有连续代表的有界函数且属Acal；f(0)≠0可逆，零锚已覆盖一阶、局部有限支撑、R133首行和非零的行ℓ¹等类，一般有界二阶尤其无限低位行和消去仍开。

R143假想核的首位闭图须TBT=α₀及真实域；其完整附录付清尾平方差和最大商图，在分母有限放大dense时有图核心/C自伴，仍无排核矛盾。R124余数B₀或零常数B_s不保证再有界除A，首阶r>1不能自动归首阶1。

一般闭理想标准性已被R185/R188实际边界核否定：非标准主理想J无限余维且不含任何A幂、与指定G/bounded K零交；原H上S仍单射稠密，因此不直接给Haar不变子空间。进一步闭理想分类和这些J的精确闭结构仍开。R116/R118/R175/R179快类标准性、R140强主理想与范数理想区别及R121根式非闭保持。R112/R119已排绝对可和归一化幂的泛覆盖；Thomas、Peters、GT相关外部判据不能未经实际条件核对直接套用。

[R256](../results/R256-bounded-weighted-composition-commutants-of-the-radial-haar-model.md)已完整分类可测nonsingular底映射上的有界加权复合交换子：仅cA^n，n为普通非负整数。非整数2-adic平移由两个高位柱的正常质量与归一化幂交换估计矛盾排除；反向整数权本质无界。条件只需径向η_j→0，包含当前实际权。一般非复合A′元素、原核与普通不变格仍未知。

## 4. 相对乘积、多项 cocycle 与混合解析芽

R127关闭相对ℓ¹两乘积；强乘积扩展仍需真实有限换因子一致范数。开放：一般复杂相位相对ℓ²尾且两个换因子方向均未证有界的R16对；三个以上独立乘法cocycle组合；多个独立慢加性方向的混合解析芽、非解析范数闭包和非正规多快参数混合芽；一般实际有界商分类。R146/R148的一个慢加快范围、R129/R135单方向解析闭商、R152 gauge增量在G及K(S)、R153纯FracG都不自动解决这些范围；超越分支仍未普遍限制dense。

R160自然慢二阶Bell项可首阶1且四次尾型零，不能直接收入G，慢v²−v(0)²仍须实际机制。R77/R79/R82临界二尺度L_p^r+cL_q（q=1+r(p−1)）的一般中间参数与更高联合尾未全部关闭；纯尾小时间负率/外部参数区不能当全区间排核。R83真实芽/闭轴谱接口保持。R162纯虚ℓ²倾斜的A′有界线性同构不保乘法，不能据此传核性质；R147/R149/R150的指数加权点态多项式也不代表任意H向量乘指数保持循环。

仍可寻找固定单射R∈A′使所有非例外ζ有B(RM,UζM)=0：此时closureRM非零且含于M即可用R122，无须先dense。当前辅助因子依ζ变化，可数全H稠密像之交不自动与未知M非零相交。

## 5. 一般 ISP 的独立路线与不能省略的障碍

R5仍缺可用非零拟幂零秩一扰动及任意T无损归约；R7双锚未为任意T实现，R2/R17/R18排内部一致紧修正。R4/R6标量观察拟仿射失败，Rota闭像须在指定空间找真中间空间；R8双生成提升不作一般T充分归约。

R114限制交织紧化失败；R164的实际UHF/不变投影/零延拓交织代数在Calkin忠实完全等距，角谱等于本质谱，Fredholm矩形交织必同构。R165一致平方可积类亦保距离，不能据此判普通格平凡。R105/R107核原文：当前centered模型不满足PPP1995谱圆条件，MM1974无所需无条件ordinary结论，AT紧化/AM-compact支配失败；JKP2019完整附加条件与Tucci迹向Haar转移未得。

[family293一手审计](../notes/2026-11-13-family293-hyperinvariant-scope-and-backward-normalization-audit.md)的固定版只给相应超不变结论；其逐纤维S有非零真普通尾空间、S′非交换，不能借当前R88改称普通反例。Domar紧纤维与当前径向权不同，原单重遍历A无任意标量交换子以完成共同纤维反向归一。未执行Lean重编译。所有旧原句、条件和未闭方向完整保于[本轮归档](../notes/2026-11-13-handoff-open-before-zero-free-and-all-real-blocks-0c.md)，普通ISP仍开。


## 不能互换的极限

全部混合自然词域不保普通系数截断；可数first核心及固定正则子在子商单射稠密，不使原词普遍dense。非零有界交织不能把全像送入全部first域；R204重选行不代固定慢行或边界运输。实际域、carry、非零锚仍须支付。

[R239首位图](../results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)/[横向压缩](../results/R239-appendix-coercive-adjoint-and-positive-mixed-compression.md)保C²=η₀N₁|L、||C||<1/√12，真缺陷需C*Gx=0及C*x=−η₀(N₁|L)*Cx。核上T*≥7/8、Re(P_MBT*|M)≥5α₀/6，给M⊥内横向同构而非BM原像；各位压缩约束仍未排缺陷。详式和度量字典在原稿及本轮归档。
