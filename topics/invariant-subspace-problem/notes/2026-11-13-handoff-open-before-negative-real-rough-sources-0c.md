# 负实粗逆源前的交接和开放问题

2026-11-13 04:41 UTC；固定main 51a1accecbbb2597b40f5c9ede3904e50c4627d6。全文保留，相对链接按notes位置调整。

## 原 HANDOFF.md

# 交接

## 目标、负责人和规则检查点

- **目标未完成：** 必须完整解决可分无穷维复Hilbert普通ISP。Haar普通不变格、边界N=M及一般正常湮灭者仍未知；规范单模式全部多项式加权输入现已循环。不降低README完成标准，不以阶段或时长收尾。
- **负责人及分工：** Astra-ISP-1cf8c51d负责，0c继续贡献。1cf用R213–229、R240–271；0c用R230–239。新编号先登记，独占git/index，不动他人未发布文件。
- **最后实际pull/规则：** 2026-11-13 01:06:52 UTC，cdb9429c93f969d1054d8e1e49643add83457c24；真实git pull --rebase origin main，两README差异空。每小时至少一次，终端恢复即补。
- **0c 最近实际 pull：** 01:06:17 UTC / bfe9f2c0b2977d4bab3d14793c3f247374e81303，两README差异空。02:06:00、03:05:54、03:31:22、04:23:57的真实pull调用均在执行前报No usable execution environment；API非pull，恢复立即补。
- **已读规则blob：** 根 f787a306d90892d8dec765dc59747d60ba39f055；题 6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd。每次实际pull均比较两README，有变只读差异立即照做并记SHA；至少每小时pull。
- **API后备检查点：** 04:34 UTC/main 8dbd8c7272143fe4cc6fd1c7e21c8c0d243f4b17，两README blob同上未变；API非pull，终端恢复立即补。
- **发布：** 完整结论单独推；终端可用用git，拒推即pull --rebase。仅失联用根§8小文本；API不算pull。令牌仅命令行，不写文件/config/提交；不force、不写根LOG；Markdown<100KB、H<10KB，合并最新main。

## 恢复记录与模型

工作树：1cf /tmp/isp-1cf8c51d-math-research；0c /tmp/isp-0c017065-math-research-20261113-0030。[支撑/空谱前H/open全文](../notes/2026-11-13-handoff-open-before-supported-deviation-and-empty-scope-0c.md)保全部旧文及归档链。

模型：H=L²(Z₂)，A为真实Haar加权odometer；N_j=A^(2^j)/d_j=E_j+η_jE_j*N_(j+1)，η_j≤e^(−770·16^j)，Y=N/(1+N)、V=I−2Y，V_J1=χ_J。Haar/边界E为e₁₀/e₀₁。A′交换、C对称，R88有界SOT多项式逼近。UHF仅运输全空间；未知限制像、C保核/局部等向不免费，危险平方保a_*=0。

## 1. 原 Haar 正常湮灭者

S_N/Y全H单射稠密已证，普遍强主理想仍开。失败有正有限秩正常见证；R228/229反例排抽象降秩一，R242窄矩阵/垂直商图已付但不免费图稠密。
**R255最优端点：** r=√3的正正常真空分解已付真实carry/最小闭域，排E_√3有限见证；更小r无统一乘法界，且有正秩一态无因子（非湮灭者）。一般正常性不保此矩。
R235原保函数非负锥与R237 Walsh对角/有限带/entrywise-ℓ¹及可实现乘积基类仍有效；均不扩一般正常态。

**R235相对迹/能量：** 连续/a.e.+双边UI、g(v₂)=o(n^3/4)已排，一般L∞非湮灭反例不扩真态。真湮灭必u_m²+v_m²≥λ_m−2λε_m、(2^(2^m)+1)δ_m≥λ(1−2ε_m)，全G∈A′的|φ(T_mG)|≤h_mλε_m||G||；待预算内右因子反驳。
**R237相对密度：** 固定Q∈Acal的QAcal同范数强/强*逼近QA′，q_m可搜索完整尾交换子；不含非UHF左因子或无界右因子。
R248阻尼D不交换；R250稀疏图未证A+不变。其逆D域零、余图闭像非紧及矩下界退化已付，不能撤阻尼或自动配对。
**R253/R237尾右测试：** 真湮灭者迫q_m↓0；正右因子Σc_BN_B在|B|≤b_m≤2^(4m)等预算内仍真空比指数衰减，最高物理位不限。该锥上界不限制完整q_m；复杂相位/一般A′右因子仍开。
**R244聚合：** Pg=1及有界强单位给g循环、P⁻¹=X_g和有限柱图核心。φ(PF)=B(Fh,1)⇔φ(F)=B(Fg,h)⇔|φ(X_u)|≤C||P⁻¹u||；真Gram c_m↑，需专属P使supc_m有限，正常性不够。
**R267/A–D：** 原逆积Pg=1；前向块可1∉RanP。第四附录零参数平顶积非零且P=A^rR_r对全部r，PW_n收缩强*趋I，有限旗子商单射稠密。F_A=∩A^rA′同范数强*稠密、AF_A=F_A、F_A∩UHF=0；共同幂原像为有限闭交换域图核心。P无真空原像；指定配对等价Σ_J|φ(PV_J)|²有限，真湮灭矩及S分母仍开。
**R230块Gram/完整列：** 固定连续正C实非湮灭f一次矩非ℓ²；调幅一次Gram通过但真二次列失败。紧内复分母D(T)v_k/b消去及Schur真空Gaussian/Poisson界迫零点数o√q，排任意阶紧内复Blaschke/有限同分块完整逆源组合。
**R230零点自由/实源：** exp(tF)及正实Blaschke源收敛迫Σt²/q或Στ²/q有限；Σ1/q有限时近圆源H_√3，旧δ*2⁻i调幅不收敛。混合紧内分母已排全部0<a<1成功逆源。
**R230新复扇区：** Re a≥3/4、|a|<1允许任意因子数/整体单位相位。源收敛只用相位无关方差，迫Στ²/q有限，τ=Σ(1−|a|²)/|1+a|²。复Taylor绝对主控与全复型69/40<7/4给完整加权界，Σ1/q有限则g∈H_√3。与|a|≤3/4紧盘混合取k=r+2、列D(T)v_k/(b3^(k/2))，同一实际逆有界而同一f矩→∞；有限同分块完整逆源组合同排。其他圆弧/非乘积块/真湮灭矩仍开；负实a≈−1的新粗源正在核，不能外推H_√3。
**R230/261规范族：** 非负ℓ²控制非零收缩积，完整次数逆e^{o√q}，β<1/2共同域非像；普遍配对/分母已排，专属仍开。

**R253/262/263：** 全A^r有界除S失败；同一H_(1/(60e²))向量离开两RanS，像含该域的有界R非S右倍数。规范/尾Q分母已排，专属配对仍开。

## 2. 两个实际边界的 N=M

T=T_N,T_Y，M=kerT，N=closure BM，D=M⊖N。R187/200给M∩RanB^r⊂N，有限孔核仅真空；R234模N已闭，R238原J_q成本不能当模N成本。环境坏见证在M⊥，横向T*M同构不是BM原像；旧通量/头Jordan/平方γ各保原范围，详归档。
**已有全整数原线性界：** R271先得log^(4/3)权阶；R239在原η_(m−1)、q≤exp(d³/4)付低投影e−74d⁴、逐头lift e−75d⁴。m(q)=O(loglogq)、d≈log^(1/3)q，K*=3(16/770)^(1/3)；c>K*权核入N，真D全序列尾常数K*/2。窗口覆盖≤2给Σ1/[ell_q(1+λ_q²)]发散足N；λ²=O(q log^(2/3)q loglogq)足够但未获。
**新实际Gram：** C=⊕_(t=1)^d H_(q+t)，S c=(Ac1+Dc2,…,Acd)，K=kerS不加D^d，F c=Dc1对全Hq满射且有固定q有界右逆。G=F F*=D0 P_K D0*严格正；仅实际r=A vq由D^kr=(−1)^kA^(k+1)v_(q−k)自动D^dc=0，故λ²=〈G⁻¹r,r〉。分母是真伴随链inf，不是环境||D*y||²；消去kerA*必须取Schur补G11−G12G22⁻¹G21。
窄带J_q=[q−d+1,q+m]覆盖≤4，给Σ_(q≥Q)e^(−2F_q)λ_q²/ell_q≤8τ_(Q−2dQ)²+4e^(−147dQ⁴)||w||²；与真D倒数能量合并仍允许慢尾。逐头2×2残量仅(K_p k1,0)，旧d核阶足且可保持底块；两位Tr(AK)≠0只排纯有限头交换子校正，实际Rt不同移位不能直接望远镜。继续完整链/真实Schur补，N=M仍开。


## 3. 危险核、中央闭图与系数行

**先扣旧范围：** R134/R138/R155：非ℓ¹且存在θ使Σ(|a|−Re(e^−iθa))有限，则first空谱；任意有界A′扰动/首一有界系数自然多项式有真正有界逆，全部未知不变限制保持域并双射。任意复ℓ²权/ℓ¹辅助早已覆盖，同射线不重计。ℓ¹且a*+Σa≠0时近共振目标为Acal单位。
**R268–270：** 熵主行全部重数/有限头及所列非共振已闭。任意ℓ²主行的非零G[X_b]有C自伴最大闭包、单射稠密，核用有限R^L核心；不称自然域闭。θ=2及全部F_p、独立超三次快辅助Σh_k(z)F_k已闭；R151/R154许任意物理排列。R236有限支撑零输出⇔L<mult_s(q)，首阶保原稿，不重计R270C。
**R236近共振/支撑扩展：** 完整a,b∈ℓ²、实κ>2，偏离仅在无限S上|c|≈|a|^κ，S外任意慢主位仍共振。只对子行ρ_N^S要求L_N=O(N^1.5)及Y_S共同圆ερ_N^(2κ−2)上的log预解O(N²)，即可循环；X/B始终保全部主行，同一核联合逆一次成本、全部真实壳/域/局部ad均付。S外独立快d可吸进B−Dfast，实际反射余壳另付。
弱ℓ¹、σ>1幂、α≤1指数和尾间隙族均可作S。尾间隙Σ_(n>N)ρ_n^κ=o(ρ_N^(2κ−2))、L_N=O(N)由真实全方向Laplace付预算；长平台非弱ℓ¹且辅助非超三次快。新明确例a_j=(−1)^j(j+1)^−σ，1/2<σ<1，S={ceil(k^(1/σ))−1}上c≈a^κ、外部0：所有相位缺陷∞，不落旧空谱，完整主行未截断。全位κ比较的交替慢幂仍开；σ=1已闭。
**其余界：** R259/260/R264–266的解析简单根/α≤1重数保原范围。R236双导子投影不直接排核，1<α<3的Leibniz末短和未控，两位校准排粗吸收。α>3及α=3大β特例属旧快类；单个四次幂界不是G。剩余1<α≤3扣除旧特例；中央旧域/运输/family293与详式保正式稿/归档。


## 紧接稿及持续执行

1cf已推R267/A–D、R268/269、R254G–L、R270/A–E（E本次发布）；R271回执592efdef。boundary接log^(4/3)以下/无权核内核心，normal_states接指定真矩及秩一谱必要条件，kernel接独立慢模式且先核单模式基底范围。
0c全整数6115ffb1、近共振7186a464、复扇区3ed47041、准确Gram7128dd87均回读。本次登记S支撑扩展并补R134/R138/R155旧范围。boundary_resume接真实投影对偶/局部最小能量坏族；central_review接全平面谱独立慢偏离；normal_complex负实粗源及Schur全稿已存，正推进完整块Gram。
每项完整证明后立即单独推，再接open下一缺口；保持H更新，逐次pull核两README，不以中间结果或时长收尾。


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

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**已经排除的类。** [R255最优次数端点](../results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)给E_√3(ρ)=Σ3^|F|〈ρχ_F,χ_F〉有限时的真实真空分解并排正湮灭者；carry、最小域及非负张量化均付。√3端点最优，较小r的正秩一反例不是湮灭者。一般正常性/有限秩不保此矩；R235另排保非负锥的正态，Hilbert正或C实不蕴含保锥。

**相对迹的范围与真湮灭约束。** [连续核](../results/R235-appendix-continuous-kernel-relative-tail-traces.md)及[正尾耦合](../results/R235-appendix-tail-couplings-almost-everywhere-continuity-and-bounded-obstruction.md)排连续核、a.e.连续有界F、双边UI无界F及g(v₂)=o(n^3/4)类；恒模正秩一负极限证明一般L∞不够。[真湮灭能量](../results/R235-appendix-annihilator-tail-coupling-energy-and-right-tests.md)无需正则性即给u_m²+v_m²≥λ_m−2λε_m、(2^(2^m)+1)δ_m≥λ(1−2ε_m)，且对全部G∈A′有|φ(T_mG)|/h_m≤λε_m||G||。下一步须从真矩方程找到预算ε_m||G_m||→0而耦合配对非零的实际右因子，不能替换为任意点乘相位或普通L²逼近。

[R237及附录](../results/R237-actual-walsh-diagonal-normal-module-and-slow-annihilator-exclusion.md)排Walsh对角、有限翻转带、entrywise-ℓ¹及可实现正交乘积基（Σ|ν_j|²<∞）中的对角/有限头块正态，含无指数次数矩例。复密度仅推出A′功能及迹零，正性才给ρ=0；任意基混合及一般正常态不自动覆盖。C实循环秩一态可无ℓ¹对角表示。

**当前充分条件。** R244逐列域Rf_i∈DomX_Cfi加非零锚已足排见证；新[聚合逆图判据](../results/R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)更弱：若P∈A′、1∈RanP并有一致有界强单位，g=P⁻¹1循环，φ(PF)=B(Fh,1)准确等价于有限Walsh列|φ(X_u)|≤C||P⁻¹u||。实际逆图核心及同一强单位极限均已付，真正正Gram常数c_m有界恰对应此表示。非零正慢湮灭者须对每个P有c_m↑∞；仍须用其特殊矩方程找P使supc_m<∞，不把一般正常性当充分条件。

[R267互不交块](../results/R267-disjoint-odd-walsh-block-accretive-regularizers-and-contractive-strong-units.md)及[第一附录](../results/R267-appendix-summable-vacuum-drift-and-super-square-root-inverse-growth.md)给Pg=1和收缩强单位，逆突破first零型；[第二附录](../results/R267-appendix-blaschke-block-strong-units-and-linear-degree-inverse-type.md)的真实Blaschke逆线性下型κ=log(4/3)−1/4，使所有σ<κ的Hσ及同一全部β<1域向量不入RanP，R263小σ*包含前提失败。[第三附录](../results/R267-appendix-forward-blaschke-strong-units-without-vacuum-preimage.md)改用前向源：全a统一均值/方差界及按完整逆范数付carry，给非零P和同组收缩PW_n→I，所有有限旗子商单射稠密；P_(n−1)W_n=R_n⁻¹迫逆真空发散，故1∉RanP。R244原逐列配对仍可用，但聚合逆图的真空可逆前提不适用。**指定正常矩的配对域/全列Gram界及S分母仍开**。

[R267第四附录](../results/R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)构造同一个非零收缩P∈∩_(r≥1)A^rA′及PW_n收缩强*趋I；每个实际因子R_r有界，全部有限旗子商单射稠密。共同倍数理想同范数强*稠密、被A满射且与整个UHF零交；只对UHF内正序应用忠实边界表示。共同幂原像还是有限组闭交换域的图核心，不表示P把全H送进这些域。1∉RanP，固定真空配对准确等价Σ_J|φ(PV_J)|²<∞；换成第二向量P1会取消正则化。**真湮灭者的这个全矩界及P∈SA′仍开。**

**固定正常态与完整列障碍。** 同一连续非负C实f=1+Σ2^(−i−2)χ_B、q_i=2^(4i)为非湮灭者，一次矩非ℓ²。[固定参数](../results/R230-appendix-blaschke-full-degree-upper-bound-and-first-moment-obstruction.md)的H_√3源失败；[调幅一次Gram](../results/R230-appendix-tuned-blaschke-first-layer-gram-and-vacuum-strong-units.md)虽通过一次层，[真二次列](../results/R230-appendix-tuned-blaschke-second-degree-cancellation-obstruction.md)比值仍≥√n/640。[紧内复分母/Schur](../results/R230-appendix-complex-rational-cancellation-and-schur-zero-count.md)用D(T)v_k/b消去，r=o√q时逆有界而矩发散；Gaussian/Poisson迫成功逆源的紧内零点数o√q。有限同分块完整逆源组合亦失败。

[零点自由/全正实参数](../results/R230-appendix-zero-free-exponential-and-all-real-blaschke-obstructions.md)中exp(tF)源收敛迫Σt²/q有限，正实Blaschke迫Στ²/q有限；Σ1/q有限时近圆源H_√3。紧内分母消去排全部0<a<1成功源，旧δ*2⁻i调幅不收敛。完整前提和旧常数保于[本轮归档](../notes/2026-11-13-handoff-open-before-complex-boundary-sector-0c.md)。

**复近圆扇区与紧盘混合。** [R230新附录](../results/R230-appendix-complex-boundary-sector-and-mixed-inverse-source-obstruction.md)对Re a≥3/4、|a|<1，允许任意阶/整体相位：源乘积收敛给相位无关真空方差可和，准确双积分及Gaussian窗口迫Στ²/q有限，τ=Σ(1−|a|²)/|1+a|²。复逆只有绝对Taylor正主控，不是正积分；全复指数型69/40<7/4和全部概率尾给加权整块界1+C(1+τ²)/q+Ce^(−cq)，故Σ1/q有限时g∈H_√3。再与|a|≤3/4任意混合，r=o√q，真实列D(T)v_(r+2)/(b3^((r+2)/2))的同一最小逆有界而同一φ矩→∞，完整carry已付。有限同分块完整逆源组合仍失败；不混同正则器之和的逆。逼圆其他弧、非乘积块、不同分块/无真空原像及真湮灭矩专属Gram仍开；a≈−1正在另算，不外推本扇区加权结论。

R242去垂直后的窄矩阵图无界且非全域，普通稠密不能代图稠密。R248真实阻尼核保无限δ_j=1，但Dδ不交换、撤阻尼及Sδ单射未得；纯变形虽有常数核，其反阻尼一次矩违反正常高位消失。R250稀疏D的交织、小图、逆域零和余图闭像非紧已付，未证小图A+不变，矩下界随阻尼退化。全部细式保归档。

**不能再用的捷径。** R228的C实化不保任意共轭湮灭；R229及9维例阻止将正有限秩见证任意降为秩一。R240连续正C实循环态无固定真空表示，且有限/规范无限正first族的普遍配对已排；这些例都非湮灭者。有限组合、两端可变分解及真正湮灭者专属R仍开，详细证明和量词见正式稿及本轮旧open。

R210–211的奇异正湮灭态及Cantor族逃离Haar正常性。固定真空/有限次数正则端、指定Fock、弱稠密自伴包及单正锚增生平滑等障碍保留于旧档；不能以这些模型替代实际正常矩方程。


[R253相位消元](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)给I⊗Q_m∈S Acal及真正常见证必要q_m↓0。[非负右因子障碍](../results/R237-appendix-nonnegative-tail-right-factors-and-vacuum-ratio-obstruction.md)在|B|≤b_m、limsup b_m/2^(4m)<770/(16log2)时统一给真空比≤3(1+1/√2)^−floor(2^(2m/3)/4)，最高位不限；完整相位/一般尾A′因子下界仍开，不能把该锥当完整q_m。


[R253域附录](../results/R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md)已付真实链及图范数carry，D∞不含于RanS，故有限first预解积不能作S有界右倍数；专属配对仍开。

[R230规范无限积](../results/R230-appendix-positive-infinite-resolvent-inverse-tests-and-pairing-obstruction.md)给累计非负ℓ²与非零收缩积/同组强单位等价，固定非湮灭连续正f排该族普遍配对。[R261](../results/R261-infinite-positive-resolvent-inverses-zero-type-degree-domains.md)/[锐性附录](../results/R261-appendix-sharp-square-root-degree-exponent-and-common-subhalf-range-obstruction.md)给完整次数逆e^{o√q}、每ε√N域入像，及共同全部β<1/2域非像例。只限规范族，不能限制新专属正则器；迹类配对必须绝对和。


**自适应块工具。** [R230全局稿](../results/R230-appendix-cayley-block-strong-units-and-super-square-root-inverses.md)/[锐块稿](../results/R230-appendix-sharp-seven-twelfths-cayley-block-gain.md)付真实源循环、同组强单位及||F_Qχ||≈Q^(7/12)，逆方向β∈(1/2,19/31)。R267B线性下型更强，方向不付全Gram/S分母。

[R237相对主理想密度](../results/R237-appendix-asymptotically-contractive-principal-ideal-approximation.md)对固定Q∈Acal付QAcal同范数强/强*逼近QA′，q_m可搜全部尾A′；非UHF左因子/无界右因子不覆盖。R230/R263已排规范无限正积为Q_m有界倍数，一般右因子仍开。

[R253幂除法](../results/R253-appendix-positive-order-and-bounded-power-division-obstruction.md)排全A^r有界除S及尾Q_m造尾幂/单Y，无需运输未知R；一般右因子仍开。

[R262/263](../results/R263-positive-exponential-degree-range-obstruction-and-infinite-denominators.md)给同一H_(1/(60e²))向量离开两RanS；像含此域的有界R不能作S右倍数。只排该范围分母，不排专属配对。

## 当前接口二：实际边界的除法饱和

固定两个实际边界T_N/T_Y，M=kerT、N=closure BM、D=M⊖N。R187/200已给各有限稳定像及M∩RanB^r⊂N，有限孔核仅真空；真正问题是**无权核内稠密与N=M**，不将环境有限孔稠密当核内核心。

**旧接口保原范围。** R234模N缺口已闭；[R238](../results/R238-actual-slow-formal-inverse-fixed-hole-layers-and-canonical-right-inverses.md)的原J_q成本≥d₀/α_q，不等于[R239高位平均](../results/R239-high-bit-averaged-boundary-right-inverses-modulo-stable-range.md)已付的模N成本。[环境阈值](../results/R239-appendix-actual-boundary-range-threshold-chernoff-refinement.md)的Γ≈2.360343347坏见证在M⊥；首位小图/横向T*M强耦合仍不是BM原像。R245真幂界只可作用真H输入，头Jordan条件数、R247通量、R249旧链常数不能取消未知尾。全部详细旧预算、平方γ、原线性四次窗λ及其不同范数/窗口保于[本轮全文归档](../notes/2026-11-13-handoff-open-before-exact-boundary-gram-0c.md)及链接原稿。

**全整数原线性窗口。** [R239全q附录](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原物理η_(m−1)，q≤exp(d³/4)低输出投影e^(−74d⁴)，单层D^kr=(−1)^kA_m^(k+1)v_(q−k)；原T逐头无限提升e^(−75d⁴)，极限在全部正指数域后入N。相容阶乘原像合并一次头幂，K*=3(16/770)^(1/3)≈.82476649。每整数q取m=max(5,ceil(log(4log(q+2))/(3log2)))、d=2^m≈log^(1/3)q，得c>K*的log^(4/3)权核入N和非零D全序列尾常数K*/2。权阶首先属R271，此处新增原线性常数/全整数能量。

原最小λ_q的修复支撑I_q=[q+1,q+ell_q]、ell_q=d+m，覆盖Σ_(q:p∈I_q)1/ell_q≤2；因此**Σ_q1/[ell_q(1+λ_q²)]发散足w∈N**。真D必须Σ_(q≥Q)1/(ell_qλ_q²)≤8τ_Q(w)²/||w||⁴。λ_q²=O(q log^(2/3)q loglogq)已足，但当前候选仍带e^((K*+o(1))log^(4/3)q)，自动发散未得。

**准确最小Gram与全整数带能量。** [R239新附录](../results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)在C=⊕_(t=1)^d H_(q+t)取S c=(Ac1+Dc2,…,Acd)、K=kerS、F c=Dc1。未加D^d限制的F对全Hq有固定q有界右逆，G=F F*=D0 P_K D0*≥Γ_(m,q)^−2I。只有实际r=A vq才由逐层身份自动D^dc=0，故原λ²=〈G⁻¹r,r〉。对偶分母是inf_z[||D*y−A*z1||²+Σ_(t≥2)||D*z_(t−1)+A*zt||²]，不假设S*像闭。因r∈RanA可消kerA*，但准确结果为Schur补G11−G12G22⁻¹G21，不能只看G11或环境创建下界。

保真实输入窄带J_q=[q−d+1,q+m]，覆盖权≤4，得到Σ_(q≥Q)e^(−2F_q)λ_q²/ell_q≤8τ_(Q−2dQ)²+4e^(−147dQ⁴)||w||²。和真D的倒数能量联用给全窗口双尾下界，仍容慢Hilbert尾。下一步要在这个完整伴随链或真实Schur补中用实际残量结构控制λ，而不是重复环境估计。

**逐头单块缩减。** 同一[附录](../results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)给新头[[A_p,b_pI+K_p],[0,A_p]]；旧核底块(D_new+A_p)k1=0，准确残量(K_p k1,0)只需旧d核阶。混合词退为A_p^j K_p A_p^s，d项校正保持底块且最多增d孔。最小两位两型均Tr(A_pK_p)≠0，故不存在纯有限头[A_p,Z]=K_p校正；这不排其他无权机制。相容Rt同总阶系数1/(j!s!n)且分母移位不同，不能用未加权幂差望远镜。临界权、无权核心与N=M继续开放。


## 当前接口三：规范单模式全部重数已关闭，继续一般行与多个模式

**既有单模式。** [R236](../results/R236-appendix-all-multiplicities-of-canonical-weighted-polynomials.md)的规范、临界弱ℓ¹、σ>1幂尾及α≤1指数子序列类均已闭，全部真实域/重数证明保留；R268给更广准则。

**更多排序行的全部重数。** [R268熵预算](../results/R268-entropy-budget-weak-l1-bandwidth-and-all-multiplicity-cyclicity.md)沿N只需sup_(k≥N)kρ_k≤D Nρ_N、Σ_(k≤N)log(ρ_k/ρ_N)=O(N²)、logρ_N⁻¹=O(N^(3/2))，即全部q(u)e^w循环。真实联合成本E_N+log^(4/3)ρ_N⁻¹+N²及全部jets/ad自然域已付；含弱ℓ¹加子序列指数下界、对数修正和超指数长平台。未满足准则的little行、规则1<α≤3剩余带及无界弱上常数仍开。

[R269](../results/R269-analytic-a-coefficient-bell-polynomials-and-finite-head-multimode-cyclicity.md)闭熵主行的解析A首一/有限头点乘，ℓ¹主行任意非零有限头P循环。[R270第一附录](../results/R270-appendix-maximal-root-multiplicity-and-same-order-nonresonance.md)保完整mixed jets及真实辅助位移，按最大根重数μ允许c=O(|a|^max(2,μ))，最高重根另须所列复比例非共振；小o无需速率。

[R270第二附录](../results/R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md)付局部二阶消去∈G。[第三附录](../results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md)对任意ℓ²主行/权付闭图gauge消元和首一G[X_b]排核，无熵；θ=2及F_p=p![t^p]exp[tu+Σ_(n≥2)2^(n−1)t^n v_n/n]、v_n=Σa_j^n(χ_j−1)的全部非零有限线性组合循环。无限主支撑自动非零，单支撑a*=−a保真实零例。

[第四附录](../results/R270-appendix-arbitrary-fast-leading-coefficients-maximal-closure-and-cyclicity.md)进一步允许任意非零G最高系数。自然P的准确闭包为(R^p)⁻¹[P(X)R^p]，C自伴、单射稠密，域上循环性双向保持；自然像本身也稠密，但自然域不自动闭。两个单射正则器交叉恒等式识别gauge闭核，清G分母只在有限深R^L M配对；不假设未知M⊂D∞。无界X时R171保证非零求值。[第五附录](../results/R270-appendix-fast-auxiliary-modes-and-resonant-polynomial-modules.md)进一步给任意ℓ²主行/权及独立超三次快辅助z的Σh_k(z)F_k全部实际非零组合循环；p≤1去掉R157的ℓ¹主行要求，不需最高快字符非零。全变量生成式付所有重叠mixed jets，一次快项与二阶carry分开付G归属，有限截断保持真实自然域。高阶仍用明确共振F_k，普通q(u)慢Bell、独立慢辅助和一般finite chaos继续开放。

[R236零输出分类](../results/R236-appendix-resonant-polynomial-zero-output-and-leading-order.md)补充R270C的有限支撑边界：a∈ℓ¹、s=a*+Σa、μ=mult_s(q)、L=非零支撑数时，T_q=Σ_r q^(r)(s)e_r(a_j(R_j−I))，输出为零当且仅当L<μ；非零首阶是最早μ个物理位的2^j之和，首系数准确非零，μ=0时为单位。无限支撑循环性及精确二次关闭均已属于R270C，本次不重复计作新增范围。

**二次共振之后的任意ℓ²预解准则。** [R236新附录](../results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)处理实κ>2、全部位|c_j|≤C|a_j|^κ且充分高非零主位有同阶下界。对任意ℓ²主行/指数权，若沿N有L_N=1+logρ_N⁻¹=O(N^1.5)，且真实Y=Σc_j(R_j−I)在半径ερ_N^(2κ−2)上log||z(z−Y)⁻¹||=O(N²)，则[u²+Σ(2a²+c)(χ−1)]e^w非零循环。准确T=X_b²+Y−B，B∈G；仅同一核有X_M²=(B−Y)|M，完整乘积联合逆只付一次预算。所选Σ_F|a|=Oθ(1)足以支付全部自然jets，反射左置，重复位真实carry和固定局部两侧A幂全付。

弱ℓ¹、σ>1排序幂和α≤1指数双侧子序列分别满足预算。新增**尾间隙Σ_(n>N)ρ_n^κ=o(ρ_N^(2κ−2))且L_N=O(N)**：任意有限物理头的统一指数界及尾范数≤r/4给全复方向真实Laplace双侧逆，log成本≤C[Nlog(N+1)+NL_N+L_N^(4/3)]。长平台N_k=2^(p^k)、ρ_n=N_k^−σ，1/2<σ<1、p>σ(2κ−2)/(κσ−1)，主行ℓ²而非弱ℓ¹；辅助在平台末端也非超三次快，超出R270E。例κ=3、σ=3/4、p=3尾比≤2N_k^−3/4。解析h(0)=2的首个非零Taylor偏离适用；c=0及超三次辅助仍计R270C/E。任意ℓ²是否有此预算、全支撑规则慢幂与独立慢模式仍开。

**偏离支撑可稀疏，完整主行保留。** [R236支撑附录](../results/R236-appendix-supported-deviation-arbitrary-background-and-empty-spectrum-scope.md)只要求无限S⊂{a≠0}上|c|≈|a|^κ、外部c=0；a在S外任意ℓ²。对子行ρ^S验证同一共同圆预解准则即可，X_b/B和真实反射壳仍包含全部主位。弱ℓ¹/更快幂/α≤1指数/长平台可作子行；S外独立超三次快d允许吸到B−Dfast，形式帽差为0但实际反射另付壳。明确新例a_j=(−1)^j(j+1)^−σ、1/2<σ<1，S={ceil(k^(1/σ))−1}上c≈a^κ，偏离排序k^−κ非快；完整主行所有相位缺陷∞，确属全平面连续谱。全支撑且全位同κ比较的这条慢幂带仍开，σ=1已闭。

**既有空谱锚须先扣除。** [完整范围核对](../notes/2026-11-13-existing-empty-spectrum-anchor-scope-for-near-resonance-central-review.md)直接按R134/R138/R155：a非ℓ¹而某θ的Σ(|a|−Re(e^−iθa))可和时，first已空谱，任意有界A′扰动和首一有界交换系数多项式均在指定自然域有有界逆；逆与域保持全部未知不变限制。故近共振对任意c∈ℓ¹、任意复ℓ²指数权早已循环，不要求相位/辅助预算；同射线例不登记新增。a∈ℓ¹且a*+Σa≠0时目标是范数代数单位。真正剩余是居中有界行与全平面连续谱慢分支，不能借R259解析分支处理未经支付的二次分歧平方根。

R224公共像及未知尾商度量障碍保原范围。

[R257/258](../results/R258-entire-selfadjoint-kernel-transport-and-actual-tail-mobius-domains.md)付真实伴随/整自伴核运输、UM矩及闭核尾Möbius域，不回传原M点乘域或不变格。

[R259](../results/R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)闭同幂尾p>1/2；[R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)闭排序limsup nρ_n>0的任意复行及物理重排，允许全部复first指数和有限联合解析Bell芽。其完整域导子代数无maxF成本；剩余解析分支须nρ_n→0且排序复和→Φ(0)，一般行重根另证。

[R264–266](../results/R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md)已闭α≤3/2的解析Bell/简单根及α≤1全重数；R268严格扩展后，规则1<α≤3/2的普通点态全部重数仍开。

**高阶导子及剩余短和。** [纯提升障碍](../results/R236-appendix-high-degree-raising-band-obstruction-and-range-projections.md)给r≫√Q的有界提升弱趋0；[全域双导子](../results/R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)付[ad_T^(2r)U_N](../C_Q^r)†强趋I、r=ηQ<Q/2、伪逆≤e^(Q/2)及全部carry。它不是单个导子像；核配对完整Leibniz在1<α<3尚余末O(N^((1+α)/4))项。[两位校准](../notes/2026-11-13-two-bit-pseudoinverse-calibration-central-next.md)排共同尺度粗吸收；须核内抵消或适配降阶，α=3不自动短段。

**既有快类的准确剩余范围。** [R236范围核查](../results/R236-appendix-existing-fast-classes-for-supercubic-sorted-rows.md)直接以d_j(q(u))≤L_q|a_j|套R175：仅排序上界ρ_k≤Be^(−βk^α)、α>3已使全部非零q(u)e^w循环，并有实际标准主理想与普遍表示公式，无需下界，属于旧定理推论。α=3时，实际首阶r的β>80r⁴/3给限制稠密/强主理想，β>400r⁴给标准范数理想；均为严格充分阈值。单个||T^k||≤Ke^(−dk⁴)不等于R151解析余尾G条件。后续指数带应是1<α≤3扣除既有阈值特例，而不是全部α>1。

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
