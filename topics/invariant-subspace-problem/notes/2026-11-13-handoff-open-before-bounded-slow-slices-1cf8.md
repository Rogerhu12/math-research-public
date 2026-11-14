# R147Slices 发布前 HANDOFF/open 完整原文

核读 main：86e94d6ba9a6c00b44d0cb7e1f0ea43f6e02e909。两README blob未变；终端unavailable，按根§8小文本后备，API不计实际pull。

## HANDOFF.md 原文

# 交接

## 目标、负责人和规则检查点

- **目标未完成：** 必须完整解决可分无穷维复Hilbert普通ISP。Haar普通不变格、边界N=M及一般正常湮灭者仍未知；规范单模式全部多项式加权输入现已循环。不降低README完成标准，不以阶段或时长收尾。
- **负责人及分工：** Astra-ISP-1cf8c51d负责，0c继续贡献。1cf用R213–229、R240–271；0c用R230–239。新编号先登记，独占git/index，不动他人未发布文件。
- **最后实际pull/规则：** 2026-11-13 01:06:52 UTC，cdb9429c93f969d1054d8e1e49643add83457c24；真实git pull --rebase origin main，两README差异空。每小时至少一次，终端恢复即补。
- **0c 最近实际 pull：** 01:06:17 UTC / bfe9f2c0b2977d4bab3d14793c3f247374e81303，两README差异空。02:06:00、03:05:54、03:31:22、04:23:57、05:20:35的真实pull调用均在执行前报No usable execution environment；API非pull，恢复立即补。
- **已读规则blob：** 根 f787a306d90892d8dec765dc59747d60ba39f055；题 6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd。每次实际pull均比较两README，有变只读差异立即照做并记SHA；至少每小时pull。
- **API后备检查点：** 05:25 UTC/main 4eb1f5a7663c0e762865de09cfd8f3462d26e856，两README blob同上未变；API非pull，终端恢复立即补。
- **发布：** 完整结论单独推；终端可用用git，拒推即pull --rebase。仅失联用根§8小文本；API不算pull。令牌仅命令行，不写文件/config/提交；不force、不写根LOG；Markdown<100KB、H<10KB，合并最新main。

## 恢复记录与模型

工作树：1cf /tmp/isp-1cf8c51d-math-research；0c /tmp/isp-0c017065-math-research-20261113-0030。[正密度矩前H/open全文](notes/2026-11-13-handoff-open-before-positive-density-moments-0c.md)保旧文/归档链。

模型：H=L²(Z₂)，A为真实Haar加权odometer；N_j=A^(2^j)/d_j=E_j+η_jE_j*N_(j+1)，η_j≤e^(−770·16^j)，Y=N/(1+N)、V=I−2Y，V_J1=χ_J。Haar/边界E为e₁₀/e₀₁。A′交换、C对称，R88有界SOT多项式逼近。UHF仅运输全空间；未知限制像、C保核/局部等向不免费，危险平方保a_*=0。

## 1. 原 Haar 正常湮灭者

S_N/Y全H单射稠密已证，普遍强主理想仍开。失败有正有限秩正常见证；R228/229反例排抽象降秩一，R242窄矩阵/垂直商图已付但不免费图稠密。
**R255最优端点：** r=√3的正正常真空分解已付真实carry/最小闭域，排E_√3有限见证；更小r无统一乘法界，且有正秩一态无因子（非湮灭者）。一般正常性不保此矩。
R235原保函数非负锥与R237 Walsh对角/有限带/entrywise-ℓ¹及可实现乘积基类仍有效；均不扩一般正常态。

**R235相对迹/能量：** 连续/a.e.+双边UI、g(v₂)=o(n^3/4)已排，一般L∞非湮灭反例不扩真态。真湮灭必u_m²+v_m²≥λ_m−2λε_m、(2^(2^m)+1)δ_m≥λ(1−2ε_m)，全G∈A′的|φ(T_mG)|≤h_mλε_m||G||；待预算内右因子反驳。
**R237相对密度：** 固定Q∈Acal的QAcal同范数强/强*逼近QA′，q_m可搜索完整尾交换子；不含非UHF左因子或无界右因子。
R248阻尼D不交换；R250稀疏图未证A+不变。其逆D域零、余图闭像非紧及矩下界退化已付，不能撤阻尼或自动配对。
**R253/R237尾右测试：** 真湮灭者迫q_m↓0；正右因子Σc_BN_B在|B|≤b_m≤2^(4m)等预算内仍真空比指数衰减，最高物理位不限。该锥上界不限制完整q_m；复杂相位/一般A′右因子仍开。
**R244：** RH⊂∩DomMi、Rg=1给正锚Trρ；秩一真湮灭必σ(MU+F)=C。有限广义Ri的Bézout付Mi=Ri⁻¹Di；共同R的理想/实际值域/Γ_R参数无关。1∈RH⇔某排列全部无重复自然子词在1上有域⇔所有排列。新rank2：Q=ker[R1,−R2]/closure Ran[R2;R1]有J²=−I、JT=T*J且无循环向量；正迹迫Γ_R⊊Γ_min⊊Γ_max，两商均无限维。Ri_Q=0、Di_Q单位，不能降无界商。真矩尚未排共同域缺口；旧聚合全Gram准则保。
**R267/A–D：** 原逆积Pg=1；前向块可1∉RanP。第四附录零参数平顶积非零且P=A^rR_r对全部r，PW_n收缩强*趋I，有限旗子商单射稠密。F_A=∩A^rA′同范数强*稠密、AF_A=F_A、F_A∩UHF=0；共同幂原像为有限闭交换域图核心。P无真空原像；指定配对等价Σ_J|φ(PV_J)|²有限，真湮灭矩及S分母仍开。
**R230固定态块界：** 同一非湮灭f、q_i=16^i排全部纯交换可逆收缩块的合格收敛逆源，完整实际Gram比值指数log5/2，有限完整源组合亦排。负实g∉H_√3；非块/无真空原像未覆盖。
**R230真密度/证书：** m_B=L_Bρ_B，LL*=[[2,2],[2,6]]^⊗n，K_n=(4+2√2)^(n/2)；全列carry d_B=8n(3√2)^nη。真全G残量≤λε_m(K_n+d_B)，纯右列加λκ_md_B；非正交叉约化ρT_m不能由ρ_B替代。正对偶μI−ΠΩ+Re(TX_u)≥0给δ_m≥λ(1−μ)−||u||||T*m_B||；理想收缩真空误差a<1/2给μ=(1+a)/(2−a)。但任意n位定位τ=||T_m/h_m−K_B||与最优统一常数C_n≥5^(n/2)满足τC_n≥√(2^m)/144→∞，不能统一范数截断。继续全空间右因子/真密度专属证书。
**R230/261规范族：** 非负ℓ²控制非零收缩积，完整次数逆e^{o√q}，β<1/2共同域非像；普遍配对/分母已排，专属仍开。

**R253/263：** 全A^r不能有界除S；同一H_(1/(60e²))向量不在两RanS，规范/全域分母已排，专属仍开。

## 2. 两个实际边界的 N=M

T=T_N,T_Y，M=kerT，N=closure BM，D=M⊖N。R187/200给M∩RanB^r⊂N，有限孔核仅真空；R234模N已闭，R238原J_q成本不能当模N成本。环境坏见证在M⊥，横向T*M同构不是BM原像；旧通量/头Jordan/平方γ各保原范围，详归档。
**R239全q/最小能量：** R271先得log^(4/3)权阶。原η/大窗低投影e−74d⁴、真实lift e−75d⁴；d≈log^(1/3)q，K*=3(16/770)^(1/3)。c>K*权核入N、真D尾常数K*/2；Σ1/[ell(1+λ²)]发散足N，所需无权增长未得。G=FF*=D0P_kerS D0*，实际r=Avq自动D^d，λ²=〈G⁻¹r,r〉；压缩须真Schur补。窄带正/倒能量仍容慢尾。
**局部坏族/真实范围：** 配对纯核/实际头κ_t≥e−100t⁴给logΛ_q=Θ(log^(4/3)q)，下c0≈.1747818上K*，无限尾同阶。真实投影同一观测≤2τ_q²+e−143d⁴||w||²，坏单位输入原像须大；未控完整λ。
**闭链/Riccati/泄漏：** 相容Rt的有限Jordan相似给RanS/S*闭及极小链取得。头旗kerA^(d−t+1)上Wd=I、Wt=I+At*(DtWt+1⁻¹Dt*)⁻¹At，G=D0W1⁻¹D0*。真核仅余末端〈w_(q+d+1),D*z_d〉及carry×对偶范数；实际Tr((A*)†)=−(d−2)c2≠0，不可幂零截断。加宽正罚项/固定m有限窗降至无限尾已付，无统一速率；逐头原范围保留。

**R271平方局部型：** 旧跨头Smith为(2d−1,2d+1)，新为4d，排具有稠密像的D交织。解析纯尾等价给每个固定混合核有限孔核心，不传原核。实际残量仅上块，可保底块用旧d头修正，成本仍依Q。

## 3. 危险核、中央闭图与系数行

**先扣旧范围：** R134/R138/R155：非ℓ¹且存在θ使Σ(|a|−Re(e^−iθa))有限，则first空谱；任意有界A′扰动/首一有界系数自然多项式有真正有界逆，全部未知不变限制保持域并双射。任意复ℓ²权/ℓ¹辅助早已覆盖，同射线不重计。ℓ¹且a*+Σa≠0时近共振目标为Acal单位。
**R268–270（G排核底座归R152/183）：** 熵主行全部重数/有限头及所列非共振已闭。任意ℓ²主行的非零G[X_b]有C自伴最大闭包、单射稠密，核用有限R^L核心；不称自然域闭。θ=2及全部F_p、独立超三次快辅助Σh_k(z)F_k已闭；R151/R154许任意物理排列。R236有限支撑零输出⇔L<mult_s(q)，首阶保原稿，不重计R270C。 第六附录保全部mixed词域，物理不交慢模式的已证点态qν可相乘；任意纯平移幂均适用。有限共享头只给单atom掩码，不取atoms之和。
**R236全阶偏离/字符互素：** 任意a,b∈ℓ²、c∈ℓ¹的F_q+v_c−λ：早偏离给全λ；否则α=a_ja、δ=c_ja，gcd(q−λ,αq'+δ)=1足循环，至多p−1个核候选。有限dyadic差真实提出A幂，核内字符单位/R151/C配对排核，不除G_n本体。p≥2且j_c≤j_a全部闭合；二次仅候选λ*=(δ/2α)²有真零例，late-c留λ0；p1须防α+δ=0。
**首c更晚/固定盘：** j_c>j_a只得2Dζ(X+Kζ)、Kζ(0)=0，R270C/D不给未知限制密度。新：无限S上|a/c|≤K、辅助排序L_N=O(N^1.5)，核内(I+2(a/c)X_M)逆在固定盘一致有界，双删除选位/真实jets/弱平均及四次局部配对给循环；S外任意ℓ²主行、ℓ¹偏离。交替慢幂c0=0、S={2^k−1:k≥1}上c=γa、其余纯κ适用，遗漏首位且全纯κ仍开。旧共同圆/子支撑、尾间隙长平台准则保独立范围，快d另付壳。
**其余界：** R259/260/R264–266的解析简单根/α≤1重数保原范围。R236双导子投影不直接排核，1<α<3的Leibniz末短和未控，两位校准排粗吸收。α>3及α=3大β特例属旧快类；单个四次幂界不是G。剩余1<α≤3扣除旧特例；中央旧域/运输/family293与详式保正式稿/归档。


## 紧接稿及持续执行

1cf已推R244广义e0195da9、秩二7bb2593；本次补R152/183归属，R184/186域稿只为旧推论。待核R147首位切片d181814654f3a1b59f354eb6d553ad4569a1c80b；三resume代理续特殊源、慢耦合、真共同域。
0c闭链43bd4049、全阶互素4eb1f5a7(PR320)已回读；本次真密度矩/定位。边界渐近正交坏族e2f3f0d4196c600a9eb254c2ffdc8ae3f797b33d待读；三代理接late-c临界核、最优链泄漏、全空间右因子。
完整证明即推，再接open；H更新，逐pull核规，不以阶段/时长收尾。


## open.md 原文

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

[压缩前全文](notes/2026-11-13-open-after-R262-rebase-before-condense-1cf8.md)及results.md保留全部旧接口。以下列五组原问题及当前三接口。

## 共同适用边界

R125/R128/R140/R176/R184已付清真实闭域、通常伴随、自然多项式和共同正则器。全H单射稠密不自动传未知不变限制或有限放大子商；G的普遍范围不能扩成一般慢Acal。UHF只运输全空间范数，不运输未知Haar子空间。Haar正常态、边界奇异态、固定次数和实际全部向量不可混同。危险平方点态应用始终保留a_*=0；全等向不能换成局部等向，C未必保M，压缩交换子不能丢中央耦合。所有“已证明”均为中间结论。

## 当前接口一：原 Haar 慢符号的正常湮灭者

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**已经排除的类。** [R255最优次数端点](results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)给E_√3(ρ)=Σ3^|F|〈ρχ_F,χ_F〉有限时的真实真空分解并排正湮灭者；carry、最小域及非负张量化均付。√3端点最优，较小r的正秩一反例不是湮灭者。一般正常性/有限秩不保此矩；R235另排保非负锥的正态，Hilbert正或C实不蕴含保锥。

**相对迹的范围与真湮灭约束。** [连续核](results/R235-appendix-continuous-kernel-relative-tail-traces.md)及[正尾耦合](results/R235-appendix-tail-couplings-almost-everywhere-continuity-and-bounded-obstruction.md)排连续核、a.e.连续有界F、双边UI无界F及g(v₂)=o(n^3/4)类；恒模正秩一负极限证明一般L∞不够。[真湮灭能量](results/R235-appendix-annihilator-tail-coupling-energy-and-right-tests.md)无需正则性即给u_m²+v_m²≥λ_m−2λε_m、(2^(2^m)+1)δ_m≥λ(1−2ε_m)，且对全部G∈A′有|φ(T_mG)|/h_m≤λε_m||G||。下一步须从真矩方程找到预算ε_m||G_m||→0而耦合配对非零的实际右因子，不能替换为任意点乘相位或普通L²逼近。

[R237及附录](results/R237-actual-walsh-diagonal-normal-module-and-slow-annihilator-exclusion.md)排Walsh对角、有限翻转带、entrywise-ℓ¹及可实现正交乘积基（Σ|ν_j|²<∞）中的对角/有限头块正态，含无指数次数矩例。复密度仅推出A′功能及迹零，正性才给ρ=0；任意基混合及一般正常态不自动覆盖。C实循环秩一态可无ℓ¹对角表示。

**当前配对条件。** R244逐列域Rf_i∈DomX_Cfi加非零锚足排见证；[聚合逆图](results/R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)在Pg=1及强单位下将指定真空表示等价为有限Walsh全Gram有界。真实逆图已付；真湮灭必须对每个P使全Gram发散，正常性不够。

[预解图与正真空锚](results/R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md)给RH⊂∩DomMi、Rg=1时正锚Trρ，秩一真湮灭必σ(MU+F)=C。[广义预解与有限词域](results/R244-appendix-generalized-resolvent-unit-classes-and-vacuum-word-domains.md)给任意Li=MiUi+Fi的实际预解Ri满足Bézout恒等式及Mi=Ri⁻¹Di最大商；共同R=∏Ri的代数主理想、实际值域与Γ_R不随全部允许选择改变。真见证迫Γ_R距真空≥√Trρ，虽各单图投影稠密。1∈RH等价某个排列全部至多2^r个无重复自然子词在1上有定义，亦等价所有排列；rank2还原两交叉域。**无广义预解分支或共同高阶域缺口尚未排除，调参数不能改变它。**

[秩二有界链](results/R244-appendix-rank-two-koszul-defect-and-double-common-graph-gap.md)令Q=ker[R1,−R2]/closure Ran[R2;R1]，显式J²=−I、JT=T*J迫非零Q无限维且无循环向量。真rank2正迹给非零商类；共同最小图在分母坐标中循环，故Γ_R⊊Γ_min⊊Γ_max，两级商均无限维。Ri_Q=0、Di_Q单位，原最大无界商不能自动下降。**仍须从实际正矩证明共同最小图达到最大交域或该链正合。**

[R267 Blaschke逆族](results/R267-appendix-blaschke-block-strong-units-and-linear-degree-inverse-type.md)有Pg=1和收缩强单位，逆线性下型κ=log(4/3)−1/4；[前向族](results/R267-appendix-forward-blaschke-strong-units-without-vacuum-preimage.md)则1∉RanP但全部有限旗子商单射稠密，完整逆范数carry已付。原逐列配对可用；R244聚合逆图仅适用于有真空原像者。指定全列矩及S分母仍开。

[R267第四附录](results/R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)给同一非零收缩P∈∩A^rA′、PW_n收缩强*趋I，有限旗子商单射稠密。该理想同范数强*稠密、AF_A=F_A、F_A∩UHF=0；共同幂原像为有限闭交换域的图核心，不是PH自动入域。1∉RanP，配对⇔Σ_J|φ(PV_J)|²有限；用P1作第二向量会取消正则化。真湮灭专属全矩界及P∈SA′仍开。

**固定非湮灭态的完整块边界。** [R230完整Gram](results/R230-appendix-arbitrary-contractive-block-gram-and-complete-source-obstruction.md)对同一f、q_i=16^i排所有纯交换有限块可逆收缩的合格收敛逆源：原实际最优列比值指数log5/2，有限完整源组合亦排。[负实粗源](results/R230-appendix-negative-real-rough-sources-and-large-column-obstructions.md)的真实g∉H_√3保留；无真空原像/非块路线未覆盖。

**任意真密度的完整矩与正性。** [R230新附录](results/R230-appendix-positive-density-moments-dual-certificates-and-localization-obstruction.md)给m_B=L_Bρ_B=ΣTr(ρ_BD_F*)χ_F，任意R的完整Gram为||R*m_B||；LL*=[[2,2],[2,6]]^⊗n，K_n=(4+2√2)^(n/2)，实际全部列误差≤λd_B、d_B=8n(3√2)^nη_minB。正常尾只给||m_B−λΩ||≤2K_n√(λδ_m)，没有指数速率，也没有固定相干分量。

R235全G湮灭给完整实际右残量≤λε_m(K_n+d_B)，纯列另付λκ_md_B，κ_m=||T_m||/h_m。它依赖非正交叉约化Tr_(B^c)(ρT_m)/h_m，不能仅凭ρ_B写成K_B*m_B；后一步另需全空间定位τ并付λτK_n。

**正性证书与被排除的定位法。** 有限块零字符T的准确对偶为inf{μ:μI−ΠΩ+Re(TX_u)≥0}，规范迹严格可行；证书给δ_m≥λ(1−μ)−||u||||T*m_B||。若理想内R=TX_v收缩且||RΩ−Ω||≤a<1/2，则显式μ=(1+a)/(2−a)、u=v/(2−a)。预算内全空间右因子仍待构造。

同时[一次尾定位障碍](notes/2026-11-13-first-tail-obstruction-to-uniform-full-moment-localization-normal-complex.md)对任意n物理位上的任意有界K_B，q=2^m，有τ≥q²/[8√3(n+2q+1)^(3/2)]。即使最优统一正密度矩常数C_n也≥5^(n/2)，因此τC_n≥√q/144→∞；不仅粗K_n费用失败。不能先范数截块再对全部密度统一放大。继续保留全空间T_m和非正交叉密度，或证明真湮灭密度专属消去；本障碍不限制后二者。

R242窄矩阵图非全域，普通稠密不代图稠密。R248阻尼D不交换，撤阻尼/Sδ单射未得，纯常数核反阻尼违反正常高位消失；R250稀疏图逆域零、余图闭像非紧且矩界退化，未证A+不变。详式保归档。

**不能再用的捷径。** R228/229及9维例排C实化和任意降秩一；R240固定连续正循环态排有限/规范正first族的普遍真空配对，但该态非湮灭者。有限组合、两端可变分解和真湮灭者专属R仍开，原量词保正式稿/归档。

R210–211奇异正态/Cantor族不具Haar正常性；固定正则端、Fock及增生平滑等旧障碍保归档，不代表真实正常矩。


[R253相位消元](results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)给I⊗Q_m∈S Acal及真正常见证必要q_m↓0。[非负右因子障碍](results/R237-appendix-nonnegative-tail-right-factors-and-vacuum-ratio-obstruction.md)在|B|≤b_m、limsup b_m/2^(4m)<770/(16log2)时统一给真空比≤3(1+1/√2)^−floor(2^(2m/3)/4)，最高位不限；完整相位/一般尾A′因子下界仍开，不能把该锥当完整q_m。


[R253域附录](results/R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md)：真实图carry已付，D∞不含RanS；有限first预解积非S有界右倍数，专属配对仍开。

[R230规范积](results/R230-appendix-positive-infinite-resolvent-inverse-tests-and-pairing-obstruction.md)累计非负ℓ²⇔非零收缩积/同组强单位，固定连续正非湮灭f排普遍配对。[R261锐性](results/R261-appendix-sharp-square-root-degree-exponent-and-common-subhalf-range-obstruction.md)给完整逆e^{o√q}、任意ε√N域入像，存在共同全部β<1/2域仍非像；只限规范族。


[旧Cayley块](results/R230-appendix-sharp-seven-twelfths-cayley-block-gain.md)给Q^(7/12)方向增益；R267B线性逆下型更强，均未付全Gram/S分母。

[R237相对主理想密度](results/R237-appendix-asymptotically-contractive-principal-ideal-approximation.md)对固定Q∈Acal付QAcal同范数强/强*逼近QA′，q_m可搜全部尾A′；非UHF左因子/无界右因子不覆盖。R230/R263已排规范无限正积为Q_m有界倍数，一般右因子仍开。

[R253幂除法](results/R253-appendix-positive-order-and-bounded-power-division-obstruction.md)排全A^r有界除S及尾Q_m造尾幂/单Y，无需运输未知R；一般右因子仍开。

[R262/263](results/R263-positive-exponential-degree-range-obstruction-and-infinite-denominators.md)给同一H_(1/(60e²))向量离开两RanS；像含此域的有界R不能作S右倍数。只排该范围分母，不排专属配对。

## 当前接口二：实际边界的除法饱和

固定两个实际边界T_N/T_Y，M=kerT、N=closure BM、D=M⊖N。R187/200已给各有限稳定像及M∩RanB^r⊂N，有限孔核仅真空；真正问题是**无权核内稠密与N=M**，不将环境有限孔稠密当核内核心。

**旧接口保原范围。** R234模N缺口已闭；[R238](results/R238-actual-slow-formal-inverse-fixed-hole-layers-and-canonical-right-inverses.md)的原J_q成本≥d₀/α_q，不等于[R239高位平均](results/R239-high-bit-averaged-boundary-right-inverses-modulo-stable-range.md)已付的模N成本。[环境阈值](results/R239-appendix-actual-boundary-range-threshold-chernoff-refinement.md)的Γ≈2.360343347坏见证在M⊥；首位小图/横向T*M强耦合仍不是BM原像。R245真幂界只可作用真H输入，头Jordan条件数、R247通量、R249旧链常数不能取消未知尾。全部详细旧预算、平方γ、原线性四次窗λ及其不同范数/窗口保于[本轮全文归档](notes/2026-11-13-handoff-open-before-exact-boundary-gram-0c.md)及链接原稿。

**全整数窗口和真正最小Gram。** [R239全q](results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原η_(m−1)、q≤exp(d³/4)，低投影e−74d⁴/真实lift e−75d⁴；每整数q取d≈log^(1/3)q，K*=3(16/770)^(1/3)给c>K*权核入N、真D全序列尾常数K*/2，权阶先属R271。原最小λ修复窗口ell=d+m的覆盖≤2使Σ1/[ell(1+λ²)]发散足N；真D倒能量≤8τ_Q²/||w||⁴，λ²=O(q log^(2/3)q loglogq)足但未得。

[准确Gram](results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)：S c=(Ac1+Dc2,…,Acd)、K=kerS、F c=Dc1满射，G=FF*严格正。实际r=Avq由D^kr=(−1)^kA^(k+1)v_(q−k)自动D^d，λ²=〈G⁻¹r,r〉。伴随链与消kerA*的Schur补不可省；窄输入带覆盖≤4的正能量结合倒能量仍允许慢尾。逐头残量仅(Kp k1,0)、旧d核阶/保底块；Tr(ApKp)≠0排纯头交换子修复。

**全低输出最优值确有4/3障碍。** [局部最小能量](results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)以相邻位纯核h/共纯核g、内积≥e−1/3及||(D*)^t g||≤√t!S_J^(t/2)得到λ²≥Σ||A^t x_g(v)||²/(t!S_J^t)。实际有限头A^te_t=κ_te0、κ_t≥e−100t⁴给logΛ_q=Θ(log^(4/3)q)，c0≈.1747818至K*；任意宽度含无限高尾亦同阶。真实核投影却使同一观测≤2τ_q²+e−143d⁴||w||²，坏单位输入原像范数至少exp[(c0−o1)log^(4/3)q]。观测上界并非完整λ上界，也未称坏输入不在真实线性像。

**固定链闭像与准确递推现已付清。** [R239闭链](results/R239-appendix-closed-repair-chain-riccati-and-terminal-leakage.md)用同一相容Rt将有限尾塔有界相似为有限Jordan块张量恒等，故RanS/S*闭、实际伴随极小链z_y取得。头旗V_t=kerA^(d−t+1)上Wd=I、Q_t=D_tW_(t+1)^−1D_t*、W_t=I+A_t*Q_t^−1A_t，准确G=D0W1^−1D0*，完整保自由kerD分量。固定m,q有界不等于预算内一致界。

真核逐层配对给〈r,y〉=−Σ〈w_(q+t),f_y,t〉+〈w_(q+d+1),D*z_y,d〉+真实carry/投影误差，||f_y||²=〈Gy,y〉。取y=G^−1r后，未控量准确是末端泄漏和小误差乘对偶范数。实际z_y,d=−(A*)†D*z_y,d−1；两型原头Tr((A*)†)=−(d−2)c2≠0，A^d=0不能让这条传播自动截断。加宽窗口的Gram等于旧能量加正末端罚项；固定m下有限窗口最小值降到无限尾值，但无统一速率。继续控制真正最优链的末端配对，而非替换为环境范数。

[R271平方局部型附录](results/R271-appendix-square-head-smith-types-and-old-head-single-block-correction.md)准确给旧跨头Smith指数(2d−1,2d+1)、真实新头4d；原拟幂零D允许全部解析单位实际求值，核阶不同排具有稠密像的D交织。每固定混合核有限孔/正指数核心已付，但无统一头范数且不传原核。真实平方上角残量仅(Δ(D)y,0)、D^(2d)r=0，可保底块用旧d头修正，最多增2d孔；成本仍依Q，**最小能量与无权N=M未闭。**

## 当前接口三：规范单模式全部重数已关闭，继续一般行与多个模式

**既有单模式。** [R236](results/R236-appendix-all-multiplicities-of-canonical-weighted-polynomials.md)的规范、临界弱ℓ¹、σ>1幂尾及α≤1指数子序列类均已闭，全部真实域/重数证明保留；R268给更广准则。

**更多排序行的全部重数。** [R268熵预算](results/R268-entropy-budget-weak-l1-bandwidth-and-all-multiplicity-cyclicity.md)沿N只需sup_(k≥N)kρ_k≤D Nρ_N、Σ_(k≤N)log(ρ_k/ρ_N)=O(N²)、logρ_N⁻¹=O(N^(3/2))，即全部q(u)e^w循环。真实联合成本E_N+log^(4/3)ρ_N⁻¹+N²及全部jets/ad自然域已付；含弱ℓ¹加子序列指数下界、对数修正和超指数长平台。未满足准则的little行、规则1<α≤3剩余带及无界弱上常数仍开。

[R269](results/R269-analytic-a-coefficient-bell-polynomials-and-finite-head-multimode-cyclicity.md)闭熵主行的解析A首一/有限头点乘，ℓ¹主行任意非零有限头P循环。[R270第一附录](results/R270-appendix-maximal-root-multiplicity-and-same-order-nonresonance.md)保完整mixed jets及真实辅助位移，按最大根重数μ允许c=O(|a|^max(2,μ))，最高重根另须所列复比例非共振；小o无需速率。

[R270第二附录](results/R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md)付局部二阶消去∈G。[第三附录](results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md)的§§1–8独立重证R183无界/R152有界G[X_b]排核；新增应用在§§9–10：θ=2及F_p=p![t^p]exp[tu+Σ_(n≥2)2^(n−1)t^n v_n/n]、v_n=Σa_j^n(χ_j−1)的全部非零有限线性组合循环。无限主支撑自动非零，单支撑a*=−a保真实零例。

[第四附录](results/R270-appendix-arbitrary-fast-leading-coefficients-maximal-closure-and-cyclicity.md)重证R183无界/R152有界已付的非首一G[X_b]：最大闭包C自伴、单射稠密、全H循环iff；只在R^L M配对，不假设D∞或自然域闭。无界非零据R171。[范围审计](notes/2026-11-13-r184-r186-scope-audit-and-finite-word-subquotient-corollaries-kernel.md)同时扣除R184/R186旧联合域；任意词、矩形分母及多模式子商仅为推论。

[第五附录](results/R270-appendix-fast-auxiliary-modes-and-resonant-polynomial-modules.md)给任意ℓ²主/权及独立超三次快辅助z的Σh_k(z)F_k非零组合循环；p≤1去掉R157的ℓ¹主行，不需最高快字符锚。全重叠mixed jets、一次快项/二阶carry的G归属及自然域均付；高阶仍限明确共振F_k，普通q(u)慢Bell与一般独立慢辅助未全闭。

[R236零输出分类](results/R236-appendix-resonant-polynomial-zero-output-and-leading-order.md)补充R270C的有限支撑边界：a∈ℓ¹、s=a*+Σa、μ=mult_s(q)、L=非零支撑数时，T_q=Σ_r q^(r)(s)e_r(a_j(R_j−I))，输出为零当且仅当L<μ；非零首阶是最早μ个物理位的2^j之和，首系数准确非零，μ=0时为单位。无限支撑循环性及精确二次关闭均已属于R270C，本次不重复计作新增范围。

**全阶可和偏离的字符互素。** [R236完整定理](results/R236-appendix-real-dyadic-factor-character-coprimality-and-all-order-deviations.md)对非零主行a及任意复a,b∈ℓ²、c∈ℓ¹，研究(F_q+v_c−λ)e^w、deg q=p≥2。首c早于首a给全部λ；否则α=a_ja、δ=c_ja，gcd(q−λ,αq'+δ)=1足循环，至多p−1个核候选{q(z):αq'(z)+δ=0}。有限dyadic差真实提出A幂，核内字符单位加R151/C/Fourier排核；不除G_n本体，不把单射稠密称预解。

**已闭与临界。** p≥2且j_c≤j_a时(F_p+v_c)e^w全部循环，无尾预算，含全行κ>2及交替慢幂1/2<σ<1；空主行退化见[二次原定理](results/R236-appendix-earliest-support-dyadic-quadratic-cyclicity.md)。二次仅余λ*=(δ/2α)²，单位置确有零输出例。late-c的所有λ≠0已闭，λ0仍开；一般q−λ平方自由亦闭。p1可能抵消，c0旧共振非零结论不重列开放。遗漏首位的纯κ慢幂临界核仍需真实限制密度，移出低头会留下2H X'。

**旧尾部准则保独立范围。** [共同圆](results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)/[子支撑](results/R236-appendix-supported-deviation-arbitrary-background-and-empty-spectrum-scope.md)沿N要求L_N=O(N^1.5)、Y_S在ερ_N^(2κ−2)上的log预解O(N²)，完整主/权仍任意ℓ²。弱ℓ¹、σ>1幂、α≤1指数及尾间隙Σ_(n>N)ρ_n^κ=o(ρ_N^(2κ−2))、L_N=O(N)适用；长平台可非弱ℓ¹且辅助非快。S可遗漏最早主位；S外快d吸到B−Dfast仍另付真实反射壳。全部参数及常数在[本轮全文归档](notes/2026-11-13-handoff-open-before-fixed-disk-kernel-inverses-0c.md)。

**固定盘核内逆的新范围。** [R236新附录](results/R236-appendix-fixed-disk-kernel-inverses-and-sparse-linear-deviations.md)只要求无限S⊂{c≠0}上|a_j/c_j|≤K及辅助幅度排序L_N=O(N^1.5)。同一真实核上X_M拟幂零，所以(I+zX_M)^−1在|z|≤2K有有限常数；L_j=8a_jX_M+4c_j的逆成本≤C_M/(4|c_j|)。辅助/主排序双删除保Σ_F|a|=Oθ(1)，全部实际jets/carry/局部配对只付rL_N，无全空间Y预解。S外主/辅助任意ℓ²/ℓ¹，允许a_j=0。

独立例为交替a_j=(−1)^j(j+1)^−σ、1/2<σ<1，c0=0，S={2^k−1:k≥1}上c=γa，其他j≥1为β|a|^κω。j_c=1>j_a=0，S上L_N=O(N)、a/c固定。若撤去稀疏线性修正、首位仍0且其余全纯κ，则a/c→∞，不得把固定盘常数用于增长盘，此情形仍开。

**既有空谱锚须先扣除。** [完整范围核对](notes/2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)直接按R134/R138/R155：a非ℓ¹而某θ的Σ(|a|−Re(e^−iθa))可和时，first已空谱，任意有界A′扰动和首一有界交换系数多项式均在指定自然域有有界逆；逆与域保持全部未知不变限制。故近共振对任意c∈ℓ¹、任意复ℓ²指数权早已循环，不要求相位/辅助预算；同射线例不登记新增。a∈ℓ¹且a*+Σa≠0时目标是范数代数单位。真正剩余是居中有界行与全平面连续谱慢分支，不能借R259解析分支处理未经支付的二次分歧平方根。

R224公共像及未知尾商度量障碍保原范围。

[R257/258](results/R258-entire-selfadjoint-kernel-transport-and-actual-tail-mobius-domains.md)付真实伴随/整自伴核运输、UM矩及闭核尾Möbius域，不回传原M点乘域或不变格。

[R259](results/R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)闭同幂尾p>1/2；[R260](results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)闭排序limsup nρ_n>0的任意复行及物理重排，允许全部复first指数和有限联合解析Bell芽。其完整域导子代数无maxF成本；剩余解析分支须nρ_n→0且排序复和→Φ(0)，一般行重根另证。

[R264–266](results/R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md)已闭α≤3/2的解析Bell/简单根及α≤1全重数；R268严格扩展后，规则1<α≤3/2的普通点态全部重数仍开。

**高阶导子及剩余短和。** [纯提升障碍](results/R236-appendix-high-degree-raising-band-obstruction-and-range-projections.md)给r≫√Q的有界提升弱趋0；[全域双导子](results/R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)付[ad_T^(2r)U_N](C_Q^r)†强趋I、r=ηQ<Q/2、伪逆≤e^(Q/2)及全部carry。它不是单个导子像；核配对完整Leibniz在1<α<3尚余末O(N^((1+α)/4))项。[两位校准](notes/2026-11-13-two-bit-pseudoinverse-calibration-central-next.md)排共同尺度粗吸收；须核内抵消或适配降阶，α=3不自动短段。

**既有快类的准确剩余范围。** [R236范围核查](results/R236-appendix-existing-fast-classes-for-supercubic-sorted-rows.md)直接以d_j(q(u))≤L_q|a_j|套R175：仅排序上界ρ_k≤Be^(−βk^α)、α>3已使全部非零q(u)e^w循环，并有实际标准主理想与普遍表示公式，无需下界，属于旧定理推论。α=3时，实际首阶r的β>80r⁴/3给限制稠密/强主理想，β>400r⁴给标准范数理想；均为严格充分阈值。单个||T^k||≤Ke^(−dk⁴)不等于R151解析余尾G条件。后续指数带应是1<α≤3扣除既有阈值特例，而不是全部α>1。

[R270第六附录](results/R270-appendix-disjoint-slow-point-polynomial-products-and-head-masks.md)付物理支撑两两不交的慢模式点态积：各qν(uν)e^w已有单模式结论时，其乘积循环；R144/R147的纯平移幂遂给任意ℓ²不交模式的∏(uν−λν)^mν e^w，无熵/空谱锚要求。全部mixed自然词域和各自Bell修正已付；有限共享头只保单atom掩码。**同模不同根、不同atoms之和及一般慢耦合不能这样相乘。**

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

[R256](results/R256-bounded-weighted-composition-commutants-of-the-radial-haar-model.md)已完整分类可测nonsingular底映射上的有界加权复合交换子：仅cA^n，n为普通非负整数。非整数2-adic平移由两个高位柱的正常质量与归一化幂交换估计矛盾排除；反向整数权本质无界。条件只需径向η_j→0，包含当前实际权。一般非复合A′元素、原核与普通不变格仍未知。

## 4. 相对乘积、多项 cocycle 与混合解析芽

R127关闭相对ℓ¹两乘积；强乘积扩展仍需真实有限换因子一致范数。开放：一般复杂相位相对ℓ²尾且两个换因子方向均未证有界的R16对；三个以上独立乘法cocycle组合；多个独立慢加性方向的混合解析芽、非解析范数闭包和非正规多快参数混合芽；一般实际有界商分类。R146/R148的一个慢加快范围、R129/R135单方向解析闭商、R152 gauge增量在G及K(S)、R153纯FracG都不自动解决这些范围；超越分支仍未普遍限制dense。

R160自然慢二阶Bell项可首阶1且四次尾型零，不能直接收入G，慢v²−v(0)²仍须实际机制。R77/R79/R82临界二尺度L_p^r+cL_q（q=1+r(p−1)）的一般中间参数与更高联合尾未全部关闭；纯尾小时间负率/外部参数区不能当全区间排核。R83真实芽/闭轴谱接口保持。R162纯虚ℓ²倾斜的A′有界线性同构不保乘法，不能据此传核性质；R147/R149/R150的指数加权点态多项式也不代表任意H向量乘指数保持循环。

仍可寻找固定单射R∈A′使所有非例外ζ有B(RM,UζM)=0：此时closureRM非零且含于M即可用R122，无须先dense。当前辅助因子依ζ变化，可数全H稠密像之交不自动与未知M非零相交。

## 5. 一般 ISP 的独立路线与不能省略的障碍

R5仍缺可用非零拟幂零秩一扰动及任意T无损归约；R7双锚未为任意T实现，R2/R17/R18排内部一致紧修正。R4/R6标量观察拟仿射失败，Rota闭像须在指定空间找真中间空间；R8双生成提升不作一般T充分归约。

R114限制交织紧化失败；R164的实际UHF/不变投影/零延拓交织代数在Calkin忠实完全等距，角谱等于本质谱，Fredholm矩形交织必同构。R165一致平方可积类亦保距离，不能据此判普通格平凡。R105/R107核原文：当前centered模型不满足PPP1995谱圆条件，MM1974无所需无条件ordinary结论，AT紧化/AM-compact支配失败；JKP2019完整附加条件与Tucci迹向Haar转移未得。

[family293一手审计](notes/2026-11-13-family293-hyperinvariant-scope-and-backward-normalization-audit.md)的固定版只给相应超不变结论；其逐纤维S有非零真普通尾空间、S′非交换，不能借当前R88改称普通反例。Domar紧纤维与当前径向权不同，原单重遍历A无任意标量交换子以完成共同纤维反向归一。未执行Lean重编译。所有旧原句、条件和未闭方向完整保于[本轮归档](notes/2026-11-13-handoff-open-before-zero-free-and-all-real-blocks-0c.md)，普通ISP仍开。


## 不能互换的极限

全部混合自然词域不保普通系数截断；可数first核心及固定正则子在子商单射稠密，不使原词普遍dense。非零有界交织不能把全像送入全部first域；R204重选行不代固定慢行或边界运输。实际域、carry、非零锚仍须支付。

[R239首位图](results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)/[横向压缩](results/R239-appendix-coercive-adjoint-and-positive-mixed-compression.md)保C²=η₀N₁|L、||C||<1/√12，真缺陷需C*Gx=0及C*x=−η₀(N₁|L)*Cx。核上T*≥7/8、Re(P_MBT*|M)≥5α₀/6，给M⊥内横向同构而非BM原像；各位压缩约束仍未排缺陷。详式和度量字典在原稿及本轮归档。
