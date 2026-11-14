# R266 发布前 HANDOFF/open 完整原文

核读 main：544bec1ba1437ddf314f17c0df7536b7ef941459。两README blob未变；终端unavailable，按根§8小文本后备，API不计实际pull。

## HANDOFF.md 原文

# 交接

## 目标、负责人和规则检查点

- **目标未完成：** 必须完整解决可分无穷维复Hilbert普通ISP。Haar普通不变格、边界N=M及一般正常湮灭者仍未知；规范单模式全部多项式加权输入现已循环。不降低README完成标准，不以阶段或时长收尾。
- **负责人及分工：** Astra-ISP-1cf8c51d负责，0c继续贡献。1cf已用R213–229、R240–265，R266预留其余一般行，R250–269预留；0c用R230–239。新增编号先登记，各自独占git/index，不动另一工作树未发布文件。
- **最后实际pull/规则：** 2026-11-13 01:06:52 UTC，cdb9429c93f969d1054d8e1e49643add83457c24；真实git pull --rebase origin main，两README差异空。每小时至少一次，终端恢复即补。
- **0c 最近实际 pull：** 2026-11-13 01:06:17 UTC，读过 bfe9f2c0b2977d4bab3d14793c3f247374e81303；两README差异空。其后终端回执未取回。约01:09环境再次失联，恢复立即补pull。
- **已读规则blob：** 根 f787a306d90892d8dec765dc59747d60ba39f055；题 6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd。每次实际pull均比较两README，有变只读差异立即照做并记SHA；至少每小时pull。
- **API后备检查点：** 再次失联实测exec恢复超时；按根§8小文本续作，核至748b4d66b4bca1b54fe02b8fff1b6b516e0d82b5，两README blob未变。API不算pull，终端恢复即停API写入。
- **发布：** 完整结论单独推；终端可用用git，拒推即pull --rebase。仅失联用根§8小文本；API不算pull。令牌仅命令行，不写文件/config/提交；不force、不写根LOG；Markdown<100KB、H<10KB，合并最新main。

## 恢复记录与模型

工作树：1cf /tmp/isp-1cf8c51d-math-research；0c /tmp/isp-0c017065-math-research-20261113-0030。[R244聚合稿前H/open](notes/2026-11-13-handoff-open-before-R244-aggregate-graph-1cf8.md)保完整原文和历轮归档。

H=L²(Z₂)，Af(y)=w(y)f(y−1)；N_j=A^(2^j)/d_j=E_j+η_jE_j*N_(j+1)，η_j≤e^(−770·16^j)，Y_j=N_j(I+N_j)⁻¹，V_j=I−2Y_j，V_J1=χ_J。Haar/边界E分别e₁₀/e₀₁；C f(y)=overline(f(−1−y))。A′交换、C对称且有R88有界SOT多项式逼近。UHF只运全空间；未知限制像、C保核和局部等向均不免费，危险点态平方须a_*=0。

## 1. 原 Haar 正常湮灭者

S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²Y_j全H单射稠密已证；普遍强主理想及未知限制像仍开。失败有正有限秩正常见证，不自动降秩一。R228/R229及9维例已排抽象纯化；R242最小秩的窄矩阵像/垂直商图已付，普通域稠密不是图稠密。
**R255最优端点：** r=√3的正正常真空分解已付真实carry/最小闭域，排E_√3有限见证；更小r无统一乘法界，且有正秩一态无因子（非湮灭者）。一般正常性不保此矩。
R235原保函数非负锥与R237 Walsh对角/有限带/entrywise-ℓ¹及可实现乘积基类仍有效；均不扩一般正常态。

**R235相对迹/耦合：** 连续核任意迹类Tr(ρP_m)/h_m→Trρ。正特征F若有界且μ-a.e.连续，或a.e.连续且||F||²对两个真实边缘均UI，仍得λ；径向g(v₂)=o(n^(3/4))已验证。反例|f|=1、正秩一比值趋负数，可C实化秩≤2；非负f₀比值趋0，故正常性/L∞/连续对角均不够。要从湮灭方程迫加权头误差趋零，不能用普通迹范数替代。
**R237相对密度：** R88初等扩张与真实条件期望付统一误差；固定Q∈Acal时Q Acal同范数强/强*稠密于Q A′，故q_m允许全部尾交换子右因子。无q_m下界，不扩非UHF左因子或无界右因子。
R248真实阻尼近核及纯核已构造；纯核违反正常c₀，D不交换故原A′不能全域撤D。
**R250/A/B/C：** 稀疏D真实交织及小图未证A+不变；逆D域零、L闭像有下界，L*D⁻¹图稠密全直和；正规余图在kerS12中闭像非紧。固定矩下界随c退化，继续正常矩/专属配对。
**R253/A/B/C：** I⊗Q_m∈S Acal；正尾迹距λ真空≤2√(λδ_m)，迫δ_m≥λq_m²/4及q_m↓0。恒等因子比指数趋零仅是一项测试，不是q_m上界。真实非消失下界仍开，规范P分母已排。
**R244聚合目标：** P∈A′、1∈RanP、有一致有界强单位PU_n→I时，g=P⁻¹1循环、G=P⁻¹=X_g，有限柱为完整图核心。正常φ的φ(PF)=B(Fh,1)⇔φ(F)=B(Fg,h)⇔|φ(X_u)|≤C||Gu||；同一强单位付逆图极限。真正正Gram常数c_m↑，非零正慢湮灭者须对每个P有c_m→∞。找专属P使supc_m<∞已足够，不必逐列配对域；此界仍未知。
**R230/261及锐性：** 累计非负ℓ²⇔非零规范P且有收缩强单位；真实逆零型、完整次数e^{o√q}成本，每个ε√N域入像。单坐标b_j=[√(j+2)log(j+2)]⁻¹例逆≥exp(c√m/logm)，全部β<1/2共同域非像，半阶指数不可降。普遍配对及S有界分母已排，专属仍开。

**R253域/除法：** 全first共同域及全部次数光滑域非RanS，排有限first预解分母；实际边界核的正序运输给全部r≥0的A^r∉S B(H)、RanA^r⊄RanS及固定链比≥c_rm，无需定义未知π(R)。亦排Q_m右因子造尾幂/单Y_j，未决定一般强单位或专属配对。

**R262/R230/R263次数域：** 先前对数/全部严格次线性域障碍已付。R263用同一真实孔链取m=ceil(60e²q)，在固定σ*=1/(60e²)端点保1/m残量，给同一f∈Hσ*同时离开两个RanS。故每个像含Hσ*的有界R均不在任一S B(H)；无需全部尺度逆成本。规范无限P及尾Q_m分母已由R230排除，R244专属配对仍开。

## 2. 两个实际边界的 N=M

T=T_N,T_Y，M=kerT，N=closure BM，D=M⊖N。R187/R200给全部有限阶稳定像及M∩RanB^r⊂N；有限孔次数核只有真空，核内正则向量稠密仍未知。
R234旧模N缺口已闭；R238真逐层J_q逆仍付≥d₀/α_q，R239高位平均已付模N一致。
**指数界：** R239对c>c*=2+2log(3/2)给真实X_c右逆和M∩X_c⊂N；whole N⊥必要Γ≈2.360343347>59/25。坏见证在M⊥，不下传D；D专属层增长与尾通量仍开。
R245有限次数高幂衰减不适用于形式h。R247错位窗口迫A_NB_N≥cN及Σ4^k/A_(2^k)²<∞；D专属h_q=O√(qlogqloglogq)足排缺陷，未证。
**R249/A/B/C：** 任意复杂非均匀单链最优logκ主率35/6，跨头方向付carry175/2、外κ余245/3。非零缺陷尾率liminf≤c*/28、limsup≤4c*/7；网格16及未知度量尾仍在，须新能量或D专属分布。

**R239首位/横向：** M={(x,−Cx)}、C²=η₀N₁|L、||C||<1/√12，缺陷为C*Gx=0。核上||T*w||≥7||w||/8、Re(P_MBT*|M)≥5α₀/6；P_MB:T*M→M同构，但T*M⊂M⊥，不是BM原像。
**R254/A–E：** 解析消混合项付35/6 D⁴；保混合的有限孔右逆靠(Q_mH)^d=0，成本14dq+14d²+O(d log(m+q+d))。新伴随多项式2d−2带宽使修正低部自动在纯核，真交集V=kerD^(2d)∩ker(P≤q−2P_m)满足q=25d³时dist(u,V)²≤τ_q²+e^(−1000d⁴)||u||²。收缩投影与粗P≤q交换，高部为纯核投影；低部仅余q−1、q两层输出。两层未除，V不等全混合核或N；接R239正则提升前半桥。

**R239混合低孔提升：** 真G:X7→X3、TG=I；V=kerP_m∩tail孔≤Q为闭交，Λ=J_m−GTJ_m送V入M∩X3⊂N。Q=50d³,m≥4时δ≤e^(−1000d⁴)，dist(Ju,N)≤(5/4)dist(u,V)+(27η_m+δ)||u||；D向量到V有明确非零距离。前半桥仍开，纯尾核不能替换V。

## 3. 危险核、中央闭图与系数行

**R236规范全重数：** 全部q(u)e^w已循环；原独立证明付分阶阶乘幂、Hermite/Bézout、真实Boolean和弱平均，现为下述临界弱ℓ¹定理的子类。
**R236临界弱ℓ¹全重数：** 0<limsup nρ_n≤sup nρ_n<∞时，任意复相位/物理排列/first指数下全部q(u)e^w循环。真实δ壳付含误差词及输入jets，无maxF；同幅桶τ≈1/N、一次Bézout e^(KN²)、小c弱平均及四次ad闭合。little类、无界弱上常数及多模式另做。

**R236更快幂行全重数：** 任意固定σ>1、0<limsup k^σρ_k≤sup k^σρ_k<∞时，任意排列/复相位/first权的全部q(u)e^w循环。X全H有界；实阶乘指数nσ−1给Bézout输入exp(O(N^θ)),θ=2σ/(2σ−1)<2，由弱平均与四次ad吸收。涵盖k⁻²，仍非全部little行。

R251/252的排序中心和弱ℓ¹聚点圆盘按原有限谱量词保留。




**R259/260：** 同幂p>1/2及排序limsup nρ_n>0的任意复行/物理重排全部解析Bell核已排，允许复first权；简单根循环。任意跨度完整域导子预算已付，剩余解析分支须nρ_n→0及排序复和→Φ(0)。

**R264/265：** 平方高位平均全H弱趋非零标量I；精确Bell逐位因子不付幅度比，选秩准则r2^rρ_k→0及limsup r⁻³log(1/ρ_(k+q+h))<5/6给任意重排α≤3/2指数尾排核，允许上下率不同、复first权、有限解析芽；简单根循环。

中央旧域/准确尾像、R256加权复合分类、R257/258核运输及family293审计完整保留在[本轮旧H](notes/2026-11-13-handoff-before-continuous-kernel-relative-traces-0c.md)及正式稿；不免费转域、转表示或改成普通ISP结论。

## 紧接稿及持续执行

0c历轮完整回执及压缩前H见[本轮归档](notes/2026-11-13-handoff-before-mixed-low-hole-regular-lift-0c.md)，保留全部早期归档入口。
1cf R261已main 62b94aa750cfd91137f676bd256e5264b5d9133d；R264已main dc50ad7，R265已main 23a67cf；R263已main b3dce79；R261锐性已main 0941d4e7；normal_states继续专属配对，boundary接交集顶部两层能量。
0c规范/临界弱ℓ¹/σ>1全重数、连续核及尾耦合均有正式稿；[本轮档](notes/2026-11-13-handoff-before-tail-couplings-and-bounded-obstruction-0c.md)保最近回执与旧H/open。接拉伸指数谱、正常专属信息与混合核前半桥。
每项完整证明后立即单独推，再接open下一缺口；保持H更新，逐次pull核两README，不以中间结果或时长收尾。


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

**连续核及较弱尾耦合类已排除。** [连续核相对迹](results/R235-appendix-continuous-kernel-relative-tail-traces.md)给任意连续核迹类Tr(ρP_m)/h_m→Trρ。[正尾耦合附录](results/R235-appendix-tail-couplings-almost-everywhere-continuity-and-bounded-obstruction.md)把正特征映射推进到有界μ-a.e.连续，以及无界a.e.连续且两真实边缘下||F||²一致可积的情形；负柱相关及遗漏下界验证径向g(v₂)=o(n^(3/4))类，含无R255端点矩的无界复相位例。真实输入/输出耦合、全部carry与UI双边Cauchy–Schwarz均付清。反向有|f|=1的正秩一态使同一比值趋负数（可C实化秩≤2），非负f₀也可使比值趋0；它们不是湮灭者，但排除从一般L∞/正常性/连续点态对角推相对迹极限。**下一步须用湮灭方程本身迫加权头逼近或寻找其他测试，不能只套普通L²逼近。**

[R237及附录](results/R237-actual-walsh-diagonal-normal-module-and-slow-annihilator-exclusion.md)排Walsh对角、有限翻转带、entrywise-ℓ¹及可实现正交乘积基（Σ|ν_j|²<∞）中的对角/有限头块正态，含无指数次数矩例。复密度仅推出A′功能及迹零，正性才给ρ=0；任意基混合及一般正常态不自动覆盖。C实循环秩一态可无ℓ¹对角表示。

**当前充分条件。** R244逐列域Rf_i∈DomX_Cfi加非零锚已足排见证；新[聚合逆图判据](results/R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)更弱：若P∈A′、1∈RanP并有一致有界强单位，g=P⁻¹1循环，φ(PF)=B(Fh,1)准确等价于有限Walsh列|φ(X_u)|≤C||P⁻¹u||。实际逆图核心及同一强单位极限均已付，真正正Gram常数c_m有界恰对应此表示。非零正慢湮灭者须对每个P有c_m↑∞；仍须用其特殊矩方程找P使supc_m<∞，不把一般正常性当充分条件。

R242的最小秩窄矩阵模/共同闭图保留：宽度<d的源属N，窄行像闭包一致；去垂直后共同图真无界、非全域，N仅普通稠密而图闭真小，不能将普通密度改成图密度。

R248另将正常矩列经自适应逐位阻尼实现为真H向量hδ，稀疏保留无限个δ_j=1，真实有界Sδ满足Sδhδ=0且hδ常数为φ(I)。全部局部carry、有界变形、Aδ高幂强单位和Sδ稠密像已支付；Dδ不在原A′，Sδ单射未得，任何非零原交换子也不能全域撤销阻尼。特殊变形核的正常矩约束与R244指定输入R仍开。

R250及三个附录给稀疏D下的真实有界C对称交织Hδ及近真空小图，但未证A+不变。逆D域零、L闭像有下界，L*D⁻¹图闭包全直和；正规余项L_rough∈kerS12仍闭像非紧。固定矩下界随阻尼退化，O(c)不能升o(c)。继续高阶正常矩、正性或R244专属配对，完整成本见正式稿及本轮前档。

R248附录明确构造有无限稀疏δ_j=1的纯变形慢和非零Haar核，常数系数1；其反阻尼一次矩沿配对位≥1，违反任何正常泛函的高位消失。仅靠保留无限无阻尼位不能排变形核，必须使用特殊正常矩条件；此例未吸收实际carry。

**不能再用的捷径。** R228的C实化及支撑约束不保持任意解析共轭湮灭。R229及9维实幂零正权回文移位反例说明指定正泛函确可最小正表示秩二；它们不是本慢理想的分离见证。R240的连续严格正、C实且循环f仍无固定真空表示，X_f1=f而f不在DomX_f；该f本身不湮灭S。其三附录排任意有限first预解式/正first半群混合乘积，可数正半群乘积的非零弱/强极限仍是单一ℓ² first半群；非负无穷预解式的普遍配对现已由R230逆测试附录排除；有限线性组合、两端可变分解及湮灭者专属R仍开。

R210–211给真正奇异正湮灭态和连续Cantor族，Banach商有ℓ¹子列且高位测试不弱零；这不是Haar正常见证。高位正条件化的全交换子单位球误差可控，但极限杀紧算子而逃离正常性；不能借极限排原见证。固定真空/有限次数正则端、指定Fock和弱稠密自伴包模型、单正锚或有限最终不交正锚的解析增生平滑均已有反例或障碍，完整范围见存档。仍需实际正常矩方程，不以这些失败路线代结论。


[R253相位消元](results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)给I⊗Q_m∈S Acal及非零Q_m；同一正态尾迹距λ真空≤2√(λδ_m)，迫δ_m≥λq_m²/4、1≥q₀≥q₁≥…>0且正常见证要求q_m→0。**实际q_m非消失下界仍开。** [恒等测试附录](results/R253-appendix-identity-multiplier-vacuum-ratio-decay.md)现证明|ω_m(Q_m)|/||Q_m||≤3(1+1/√2)^−floor(2^(2m/3)/4)（充分大m），两种慢符号均适用。真实有限头相位积精确化为纯尾D_m^(2^m)，carry误差远低于真空矩尺度；基本对称多项式计数和有限高位偏转给指数放大。这里只计算W=I，不能反推q_m上界；必须利用非平凡真实尾交换子右因子。部分迹仍不改善无穷指数矩。


[R253域附录](results/R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md)用真实末端链及全部图范数carry证明D∞不含于RanS。D∞保全部有限first自然词且含于任意有限预解积的像，故该积不能作S有界右倍数；不排无限积或见证专属配对。

[R230无穷积及逆测试](results/R230-appendix-positive-infinite-resolvent-inverse-tests-and-pairing-obstruction.md)：累计非负行ℓ²恰给非零P和收缩强单位，真实逆词Hσ→Hτ范数收敛。R240同一连续正循环f对所有规范P及有限混合因子仍不满足配对域；f非湮灭者，R244专属选择仍开。若指定Pf_i∈DomX_Cfi成立，强单位自动给锚；迹类另付绝对和。

[R261零型逆](results/R261-infinite-positive-resolvent-inverses-zero-type-degree-domains.md)给完整次数≤q成本e^{o√q}，每个ε>0平方根次数域入RanP，有限混合因子同样。[实际锐性附录](results/R261-appendix-sharp-square-root-degree-exponent-and-common-subhalf-range-obstruction.md)取固定b_j=[√(j+2)log(j+2)]⁻¹，以真实尾积/低头00行及carry给逆≥exp(c√m/logm)，同一全部β<1/2共同域仍非RanP。平方根指数不能统一降低；这不是正常湮灭者，R244专属配对仍开。

[R237相对主理想密度](results/R237-appendix-asymptotically-contractive-principal-ideal-approximation.md)给真实UHF初等扩张及||Ψ_nF−E_nF||≤o(1)||F||；对固定Q∈Acal，QAcal同范数强/强*逼近QA′，故q_m可准确搜索全部尾A′右因子。规范非零无限正积不能等于Q_mG（任意有界G），已由R230/R263排除；不能再作为未构造的候选。其他尾右因子仍开，非UHF左因子和无界随动右因子不在此密度结论内。

[R253全空间幂除法附录](results/R253-appendix-positive-order-and-bounded-power-division-obstruction.md)明确抽出R174/R185/R188边界无限核的更强推论：全部r≥0都有A^r∉S B(H)、RanA^r⊄RanS。若SR=A^r，单射性迫RS=A^r，故全空间A*r A^r≤||R||²S*S，两边都在UHF而可送边界；不定义π(R)或运输未知子空间。真实固定长末端链另给比率≥c_rm。由有限相位积提升，尾Q_m也不能有任何有界右因子把它变成尾幂、单个Y_j或通常全纯单位倍数。**下一乘子候选须避开这些已排类**；一般Q_mF、上述规范类之外的强单位及q_m非消失仍开。

[R262](results/R262-logarithmic-degree-domain-and-quantitative-slow-range-obstruction.md)给对数次数域；[R230拉伸域/无限分母](results/R230-appendix-stretched-degree-domains-and-infinite-resolvent-denominator-obstruction.md)排全部规范无限P及有限混合分母。[R263固定正指数域](results/R263-positive-exponential-degree-range-obstruction-and-infinite-denominators.md)进一步给同一f∈Dom e^{N/(60e²)}同时离开两个慢值域：真实高位孔链在该固定权端点残量趋零，闭图及两个真子空间引理付共同性。任何像含此固定域的有界R均非两S的右倍数；R244见证专属配对仍开。

## 当前接口二：实际边界的除法饱和

对T=T_N,T_Y，记M=kerT、N=closure BM、D=M⊖N。**N=M及其反面均未证明。** R187/R200给各阶稳定像、BM满有限jet以及M∩RanB^r=B^rM⊕Ce₀⊂N；问题等价于真实右移域在M稠密、forward主子模除z饱和。

R209已关闭无限支撑可和Cayley符号的全部有限孔次数返回刚性：有限次数输入输出迫输入有限头，核仅标准有限旗，无支撑间隙要求。环境有限次数稠密不自动传核内；两个慢核除真空外必须有无界孔次数。R223给一般实际Bell边界核及每个有限头的真实线性延拓，未得整个核稳定像稠密。

**固定层与模N已闭。** R234及五附录先后付清三次权、p>4/3、临界大常数4/3权及X_(24,1)真实右逆，原有限测试相容性(7.4)已闭，不再列为待证。[R238](results/R238-actual-slow-formal-inverse-fixed-hole-layers-and-canonical-right-inverses.md)用实际形式逆的最高位一次展开证明每个固定孔层是H向量，并给唯一规范有限三角J_q；J_q自身成本至少d₀/α_q，不代表模N成本。[R239](results/R239-high-bit-averaged-boundary-right-inverses-modulo-stable-range.md)以精确N_jE_j*=P_j⁰和高位平均使新右逆落入真实RanB^r，随后用M∩RanB^r⊂N证明模N等于J_q，扩展由有界性和N闭性支付。

**指数上界。** [实际指数权附录](results/R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md)的一次共同截平付清真实有限头及全部carry，对每个κ>κ**=2+2log(3/2)≈2.81093给
X_κ={v:Σ_q e^(κq)||P_qv||<∞}上的真右逆，且对全部f∈N⊥，规范形式T*h=f的层满足||h_q||≤Cκe^(κq)||f||。T与T*保每个X_κ，M∩X_κ⊂N。尾阻尼h^(m)=r^(N_tail)h确为H向量并给真实残差与配对，但遗漏项(1−r)C_tail h^(m)没有消失界，尾算子1/m量级不能抵消既得e^(κm)。对d∈D、f∈M有精确边界通量关系；还须证明该通量为零或核内正则向量稠密。

**任意小指数权路线已否定。** [纯创建附录](results/R239-appendix-pure-tail-creation-exponential-singular-bounds.md)给逐层最小增益的真实指数上、下界；[实际阈值附录](results/R239-appendix-actual-boundary-range-exponential-degree-threshold.md)进一步用真实头顶部杀掉伴随头，取m=O(logq)，以实际算子范数付清全部carry。原γ₀=(3+log3)/2界已由[Chernoff精化](results/R239-appendix-actual-boundary-range-threshold-chernoff-refinement.md)加强到Γ=4+½log90−π√(3/2)−2/45+2/729−2/9477≈2.360343347，有限有理证书严格给Γ>59/25。对任意κ<Γ，构造同一个v∈X_κ而v不属RanT_N∪RanT_Y，因此不存在定义在整个X_κ的任何右逆。π_NJ_q在整个N⊥上亦至少以相反指数增长。当前必要Γ与充分κ**之间及两个端点尚未决定。这一坏见证T*w_q在M⊥，**没有给D专属下界**；不能以它断言D非零或排N=M。D专属更小指数增长、总Σ_q||h_q||²及跨次数能量仍是实际开放接口。

[真实头Jordan附录](results/R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)付清cond≤exp(221·16^(m−1))及纯有限头/纯尾分级形式像；移动斜投影的条件数仍未与未知f的尾速率配平，纯模型不能无证迁给实际T。R245完整借位计数给||T^kP_≤q||≤6^k exp[−(770/256)(k−q)_+⁴]，不限制最大位置；局部预解式界只针对真H输入，不能把形式h当全Hilbert向量。

R249及全部附录已付真实有限头、双向Lagrange和跨头进位：任意非零、复数、非均匀单链权的最优logκ主率仍为35/6；精确carry方向保175/2衰减，能量外κ后余245/3。更换一般链权不能改善环境主成本。真实正能量含κ_m·τ_(n−2^m+1)²和已付κ_m²carry，非零缺陷迫liminf(−logτ_q)/q≤c*/28、limsup≤4c*/7；16倍网格和未知度量尾均保留，尚无相反尾界。

R247用h_<n与w_≤n错开一层，准确消掉纯创建而保真实carry窗口；令A_N=||h_[floor(N/2)−1,3N]||、B_N为同窗w范数，非零D迫A_NB_N≥cN、A_N/N→∞及Σ_k4^k/A_(2^k)²<∞。因此D专属h_q=O(√((q+1)log(q+2)loglog(q+e^e)))已足排D，但目前只得指数上界。下一步为D专属分布、反能量尾级数或不依赖环境相似范数的正能量；whole N⊥坏见证不能代替。原详细预算见正式R247/R249附录及[压缩前open](notes/2026-11-13-open-before-R256-1cf8.md)。

**其他已证限制。** R214最高位必要多项式尾与R216最低全孔前缀指数界是不同投影；环境(B*)^k下界不自动下传压缩。R226真实有限头右移在B图半范数中误差趋零但未加权T残差爆炸，核内距离缺陷恰D；R226A有限秩交换子为e₀⊗d且两两积零，标准高孔副本只给M⊥奇异列，不取消D。R220及附录以真实反射核证明纯慢D₀与实际T的像互不包含、D₀−TU及D₀−UT对所有有界U有正本质范数距离；绝对carry小不等于相对除法小。整个核上的绝对除法域闭包恰N，越出N则除法部分和范数趋无穷，尚未证该域在M稠密。R174及闭关系加强说明代数Haar/边界运输的图闭包为直和，不能借可闭交织解决边界内部N=M。

首位真实根图已补[缺陷正交度量字典](notes/2026-11-13-single-bit-true-defect-metric-and-compressed-square-1cf8.md)：W对应G=I+D*D下的ker(D*G)，不等于直接拿环境Z*求核。平方关系给D*u=−η₀ C_K*Du，但小压缩伴随量不自动产生零阶下界。继续检验改换平方核符号的有限头预算，不能忽略删首位后的16倍权尺度。


[R254平方头](results/R254-square-kernel-true-head-similarity-and-mixed-tail-obstruction.md)给实际尾头d的logκ≤(75/2+o)d⁴，按原总头D=2d为75/32；N/Y分式和双向Lagrange预算完整，carry937η_m乘κ²余1325d⁴。形式像F*h′=(I+Z*Z)u不增指数率。实际2A_mDtail及Y解析项尚未同分级，不能代入R249能量或报新尾率；平方头最优性未称。


[R254剪切附录](results/R254-appendix-first-tail-shear-cost-obstruction.md)及[解析尾换元附录](results/R254-appendix-analytic-tail-similarity-condition-number-obstruction.md)已排一整类消混合项方法：任意固定目标头、任意可逆零阶矩阵的解析U(D)若精确把F_m+2A_mD+D²变成J+D²，完整κ(U)仍付原35/6 D⁴。证明用同一D的二阶不变旗并验证U及逆均保旗；纯尾任意bit且所有局部删除中央化子可用，真实尾仅第一个bit可用。原跨头carry未删，不扩近似换元。须继续保混合项的其他分级、非齐次通量或D专属正能量。

[R254纯尾约束](results/R254-appendix-high-order-pure-tail-kernel-constraint-without-similarity.md)与[保混合有限孔右逆](results/R254-appendix-mixed-finite-hole-right-inverse-and-equation-repair.md)的实际成本均已付。[同时交集逼近](results/R254-appendix-simultaneous-pure-kernel-and-low-mixed-equation-approximation.md)用伴随多项式2d−2带宽实现兼容性：对V=kerD^(2d)∩ker(P≤q−2P_m)，q=25d³有dist(u,V)²≤τ_q(u)²+e^(−1000d⁴)||u||²。投影为收缩且与粗P≤q交换，高部是纯核投影；低部P_m输出仅余q−1、q两层。需真实消去这两层再接下述R239桥，不能免费等同全kerP_m。

**混合低孔核到稳定像的反向桥已付。** [R239正则提升附录](results/R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md)补出真正G:X7→X3，未从旧G:X_c→H猜输出域。对V_(m,Q)=kerP_m∩tail孔≤Q构造Λ=J_m−GTJ_m∈M∩X3⊂N；完整加权carry给Q=50d³,m≥4时||Λ−J_m||≤e^(−1000d⁴)，图差≤27η_m。于是dist(Ju,N)≤(5/4)dist(u,V)+(27η_m+δ)||u||，缺陷D上则有一致非零距离下界。现在应证明实际u到这个**混合核闭交**的距离趋零，或找等效D专属能量；R254的kerD^(2d)纯尾投影还不够。

## 当前接口三：规范单模式全部重数已关闭，继续一般行与多个模式

**规范单模式已收案。** [R236全部重数](results/R236-appendix-all-multiplicities-of-canonical-weighted-polynomials.md)证明交替调和行、任意复ℓ² first指数及每个非零q的q(u)e^w循环，含旧混合重根悬例。[分阶预算](results/R236-appendix-factorial-cumulant-powers-and-joint-resolvent-budgets.md)、保重数Hermite/Bézout、真实carry/自然域及非零弱平均的完整证明均保留，现被临界弱ℓ¹定理覆盖。

**临界弱ℓ¹全部重数也已关闭。** [R236任意跨度附录](results/R236-appendix-arbitrary-multiplicities-for-critical-weak-l1-rows.md)对0<limsup nρ_n≤sup nρ_n<∞的全部复系数行、任意物理排列和first指数证明所有q(u)e^w循环。δ=[X,·]真实导子壳付清每个含误差词和反射输入的全阶jets，不含最大选中位；固定数目同幅桶、完整保重数逆与小参数弱平均完成原自然域配对。**下一项：** nρ_n→0的行、sup nρ_n=∞的全部重数、多个独立慢模式及一般向量；不同排序衰减须重新配平分阶预解增长与原四次ad预算。

**更快幂衰减排序行的全部重数已闭。** [R236实阶乘附录](results/R236-appendix-all-multiplicities-for-faster-polynomial-sorted-rows.md)对任意σ>1且0<limsup k^σρ_k≤sup k^σρ_k<∞，允许复相位、任意物理排列与first指数，证明所有q(u)e^w循环。原X此时为Acal中的有界全域元；真实正锥分阶预算是(k!)^(1−nσ)，共同Bell圆周把Bézout成本降至exp(O(N^θ)),θ=2σ/(2σ−1)<2，实际四次ad吸收。它关闭k⁻²等little类的同字符混合根；一般little行、几何/更快谱及1/2<σ<1的全部重数仍须各付预算。

**中央工具保留，规范接口结案。** [固定r反射附录](results/R236-appendix-all-finite-range-closures-by-high-bit-reflections.md)等给规范核的全部N_r=M、D_H=0与准确逆域；规范核现为零。R212–236及R257的真实域、Bell和伴随工具保留完整证明，只在原假设下可复用，不能自动把其他压缩核判全等向。

R224的完整gauge/Bell公共像障碍、非闭预解像和一般尾商交织度量等仍按原范围存在；本次没有关闭任意有界二阶乘子、一般正常见证或所有Hilbert向量循环。

[R257](results/R257-uniform-adjoint-analytic-radius-and-local-kernel-flow.md)及[R258](results/R258-entire-selfadjoint-kernel-transport-and-actual-tail-mobius-domains.md)给伴随统一阶乘域与整自伴方向真实核运输；UM有全部指数矩，尾Möbius及逆保明确闭核。完整域证明已存，不能回传原M点乘域或原A不变格，留作一般实系数工具。

[R259](results/R259-multivariate-bell-branches-complex-tilts-and-simple-root-cyclicity.md)闭同幂尾p>1/2；[R260](results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)闭排序limsup nρ_n>0的任意复行及物理重排，允许全部复first指数和有限联合解析Bell芽。其完整域导子代数无maxF成本；剩余解析分支须nρ_n→0且排序复和→Φ(0)，一般行重根另证。

[R264弱平均](results/R264-square-window-weak-averages-and-rearranged-geometric-bell-kernels.md)及[R265逐位因子](results/R265-bitwise-bell-factorization-and-three-halves-exponential-tails.md)闭双侧e^(−βn^α)、0<α≤3/2的任意重排行，允许上下率不同；准确Bell因子使互异主项只付r2^r max|a_j|，无幅度比，配平方弱极限与四次ad。选秩及不同上下幂已付。任意first权/有限解析芽排核及简单根循环；一般行重数、超临界或大跳跃行仍开。

## 1. 一般向量的矩分离与有限二阶以上输入

R101完成有限Walsh次数两端的全矩分离；任意非零L²向量对实际A的循环性仍开，一般无限次数没有最高系数锚。一般二阶闭乘子的核、gauge差Qζ在未知核上的稠密像、两个独立慢方向和一般慢平方共振仍未闭。R130/R131二阶闭域与R143合法跨核配对已付；Δ=closure(A^hX_g)域可能严格更大，不能取消A^h后直接加入DomX_g。

R29小矩、R44/R51统一平滑障碍仍有效。R163/R165排非零限制交织把整个像送进固定Lp(p>2)或固定超二次Orlicz；小测度仍保全部算子范数。有限柱与A的超快近似交换不能提升为归一化N_j的精确交织。R255/R237的正常态排除均有明确范围，不覆盖任意有限秩。

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

- R5秩一扰动仍缺可用非零拟幂零扰动；一般T未无损归约有限阶拟幂零类。
- R7非退化弱投影双锚点未为任意T实现，R2/R17/R18排若干内部修正和一致紧控制。
- R4/R6排直接标量观察拟仿射拉回；Rota闭像模型须在指定不变空间内找真中间空间。R8二生成odometer只给指定提升方向，不是一般T充分归约。
- R114限制交织紧化失败；R164由UHF、不变投影和子商间交织零延拓生成的C*代数在Calkin忠实完全等距，角谱等于本质谱，Fredholm矩形交织必实际同构。R165连一致平方可积类距离也保留；不能据此断言普通不变格平凡。
- R105/R107原文核验表明实际centered模型不满足PPP1995谱圆条件，MM1974不给所需无条件ordinary ISP；正左右半交换子的AT紧化及AM-compact支配入口失败。JKP2019完整附加条件尚未取得，Tucci迹表示未证可转当前Haar表示。

[外部family293一手范围审计](notes/2026-11-13-family293-hyperinvariant-scope-and-backward-normalization-audit.md)已核固定版本的超不变结论、真实Lean入口及后向归一。其逐纤维S有显式非零真普通不变尾空间，S′非交换，故不能借本模型R88桥改称普通反例；Domar紧纤维假设与当前径向权不同。共同纤维归一在原单重遍历A中缺少任意标量交换子，不给合法反向交织。未执行Lean重编译，也未关闭普通ISP或实际边界缺陷。

## 不能互换的极限

连续循环输入可在全部混合自然词域而普通系数截断发散。可数first共同核心、各固定正则子的有限子商单射稠密，不使原词乘正则子普遍dense；非零有界交织不能把全像送入全部不可数first域。R204重选增长行不代固定慢行速率或边界运输。实际域、carry与非零锚仍须支付；中间接口不等于普通ISP完成。

[R239首位小图附录](results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)已付两个实际边界核的统一量化：C²=η₀N₁|L且||C||<1/√12，首位占满质量<1/13，环境B*下界>α₀√(12/13)，但跨到M⊥的耦合也有>α₀√(131/156)下界，不能传成限制伴随下界。真实缺陷准确对应C*Gx=0、G=I+C*C，并有C*x=−η₀(N₁|L)*Cx；须继续利用所有位的真实缺陷约束，仍未排kerC*。既有首位字典与本稿Y消元式已证明同核。

[R239横向正压缩附录](results/R239-appendix-coercive-adjoint-and-positive-mixed-compression.md)再给两个实际核的||T*w||≥7||w||/8与Re(P_MBT*|M)≥5α₀/6。故T*M是M⊥内闭空间，P_MB:T*M→M为有界同构；P_MT也满射并有范数≤8/7的横向右逆。对缺陷d，B*d和T*d仍可同时落在M⊥且具有正配对，这与缺陷条件相容。**剩余目标依旧是核内原像，不能把这些横向原像改称BM的原像。**
