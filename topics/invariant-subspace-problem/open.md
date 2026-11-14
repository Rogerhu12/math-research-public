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

0c本次压缩前的完整接口、H和队列见[全文](notes/2026-11-14-handoff-open-queue-before-next-birth-checkpoint-0c.md)；闭合的出生一大权比已移出当前缺口，双方边界/R150的新结果及全部旧范围均保留。

## 共同适用边界

已证闭域/共同正则器只按原范围使用：全H稠密不传未知限制/有限旗，G不扩一般慢Acal，UHF不运输未知Haar格。正常态/边界奇异态、固定次数/全部向量不同；C未必保M，全等向不代局部等向，不能删域或压缩中央耦合。所有结果仍为中间结论。

并行压缩前的H/open全文、准确范围与全部旧链分别保[1cf全文](notes/2026-11-13-handoff-open-before-nonreduced-closure-2220.md)及[0c全文](notes/2026-11-13-handoff-open-before-single-block-jets-and-complete-tail-metric-0c.md)。本页未列出的旧缺口并未关闭。本轮压缩前全部接口、量词及原链接另保[本次全文](open-archive-2026-11-13-2353-0c.md)（a054cd5268c3d855733bd17a70f6a693219668ec）；仅压缩重复已付背景，不改变未闭状态。

## 当前接口一：原 Haar 慢符号的正常湮灭者

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**已排范围与未付部分。** R235/R237/R255已排连续/a.e.+双边UI、保函数非负锥、Walsh对角/有限带/entrywise-ℓ1、合格乘积基块正态及E_√3范围；一般正常正有限秩仍开。R228的C平均可保同泛函而增秩，R229不许一般秩一纯化。真实右矩仍须ε_m||G_m||→0且φρ(T_mG_m)/h_m不消失，普通L²逼近不付此预算。完整原稿链接及端点保本次归档。

**正常源与物理度量。** R230/R244同ρ保锚源、hp/vp区分及无速率δ，R236同ζ/ρ高幂MP与原carry预算全部保[完整接口](notes/2026-11-14-open-before-serre-ci-789f.md)；双侧正合同不能免费跨次数，MP上界失败不作费用下界。

**既有首列/正常尾接口。** 全树完整good列WOT0、原坏列与指数修复下界、固定尾normal/cb距离发散、单位逆及各层原上型/聚合量词均保[完整快照](notes/2026-11-14-open-before-serre-ci-789f.md)。精确支持、预算内修复、固定原理想廉价全层及统一正常锚仍未付，不把变化起点族当固定理想或用移动右测因式化。

**完整尾接口。** U坐标、固定起点全层生成元、normal/cb余式与原源费用保[0c全文](open-archive-2026-11-14-0055-0c.md)。下述指定二次核已排，但一般迟首行、其他辅助系数及无该核来源的正常见证仍须逐族证明。

**已排的原Haar二次核。** [固定慢正族](results/R236-appendix-actual-slow-positive-quadratic-kernel-exclusion-by-joint-inverse.md)及[逐位N/Y、任意复相位族](results/R236-appendix-complex-mixed-cayley-quadratic-joint-inverse.md)在 |ai|=(i+1)^−2 下已单射稠密，指定first-flip真核/图分支关闭。[相对辅助扩展](results/R236-appendix-polynomial-relative-auxiliary-quadratic-exclusion.md)保 |ai|双侧比较(i+1)^−2、b∈ℓ1且高位|bi/ai|≥c(i+1)^−2，允许有限首位例外；κ>2更快辅助未自动覆盖。证明费用及全部旧范围保[本次压缩前全文](notes/2026-11-14-open-before-R274-789f.md)。这些是全H结果，不传未知子商；R200负边界线性T_N/T_Y仍含e0，其N=M仍开。

[原Acal右源/同ρ正常商泄漏](results/R236-appendix-actual-right-sources-and-normal-quotient-leakage.md)已把背景逆换成真R_F∈Acal，T=X²+Y的高导子在全H有界WOT趋I。固定πX=πY=0及同ρ，所有端点/中段来源及双向Walsh-minus泄漏完整保留，真实Γ的liminf≥τ；正常性没有提供可乘增长逆费的尾速率。

[同正常商真联合逆/有限总度预算](results/R236-appendix-joint-right-inverse-on-the-same-normal-quotient.md)用πX_F=−ΣF aiπXi和n>r的真实重复位carry，一次截整个逆乘积至总度r，显式Neumann余项支付log||πR_F||=O(rlogr+rlogP)。同池导子兼容；商像及物理B_R/F_R*两泄漏的准确分解保留。下条已另构造真廉价提升，不把商像界本身当物理界。

[真廉价尾提升/同商低输入导子单位](results/R236-appendix-cheap-physical-tail-lifts-and-quotient-derivative-units.md)直接在原全H以总度r及真实carry构造Rtilde=P_F(−Z_F)^−1∈≥P尾，log范数O(rlogr+rlogP)，同原R的准确差为−X R D_F Rtilde并付完整原源。cheap U的全导子主项以E_F≈∏Xi解析近似消πX，得到同E上有界WOT趋I且log输入O(rlogr)，不含exp(CP²)大逆。所有同ρ端点/中段块和差源(ad EF*)_EN H_N B_X保留，未从廉价提升推出商为零。

[固定二阶强单位/显式Walsh来源场](results/R236-appendix-fixed-second-commutator-and-explicit-walsh-source-field.md)直接取r1及池[P,2P)，真实Rtilde_i=(bi−2ai²Xi)^−2范数O(P8)，原carry全付；Φ(ad_T²U_P)强趋I_E、输出一致有界。实际逆可换成W_P=P^-1Σbi^-2(2Q_i^-−2ai²Zi/bi)，指定正权时自伴。全部来源是固定Kρ=ρT²−2TρT+T²ρ的ABρ/ρFG/−2BρF三块，Kρ³0且Tr0；准确加权单点矩余额趋τ。仅c0/有限秩/自伴性不付尾速率，仍保原两行零式及来源。

[完整局部矩阵/真实来源部分迹](results/R236-appendix-full-local-matrix-commutators-and-true-normal-source-marginals.md)单点zi=O(η_(i−1))、qi/bi²→τ/2。任意r位的整个M_(2^r)有ad_T^(2r)D/[(−1)^r(2r)!∏bi²]≈d_F(D)∏πXi，实际cb误差e_(P,r)对r≤P一致趋0。真Kρ,2r部分迹除∏bi²后、固定r统一迹范数趋(−1)^r(2r)!τE_F/2^r；全部原A′右测仍保同ρ。用H_i=I−Xi明确否定移动右测的免费统一因式化，三块所有二项来源保留；尚未推出一般正常商为零。

[任意秩正常正源的多项式柱尾](results/R236-appendix-polynomial-cylinder-tail-for-all-normal-positive-annihilators.md)对原Xi=N/Y、双侧|ai|≈(i+1)^−2与TrρXG=0(G∈Acal)，用真实增生Cayley收缩选择器及同ρ正性，得q_P/τ≥(a_-/A)²/[9·2^30 P³]，阈值与秩/放大无关，故TrρM³=∞。四相位扇区、真实尾/头carry与gentle费用全付；p>1推广的临界位置矩2p−1也发散。R213旧同量级只适指定核向量，本稿独立提升到全部正常ann；更慢尾和两行共同零式继续。

[任意高位集合统一正源能量](results/R236-appendix-uniform-high-bit-set-energy-for-normal-positive-annihilators.md)：同一原正ρ对每个有限I有泄漏≥ΣI|a_i|²/(9·2^26 A²)，阈值不依跨度/秩/放大；得完整ell2柱尾与原E正压缩、Walsh删除O(i²)逆。原N源b_iB_j仍未付，不能移作商逆。

[正常见证的真实双侧源/临界图域](results/R236-appendix-true-twosided-normal-sources-and-critical-position-graph-obstruction.md)：非正σ仍有集合迹尾≥|Trσ|·||a_I||₂/(3584A)。原XA′零才允许固定H,K∈A′；非零TrρKH禁止两侧真实M^(3/2)图域费用可和，阈值不免费统一到移动因子。

[固定有限原行/完整纯尾源类已闭](results/R236-appendix-fixed-finite-rows-complete-tail-source-embedding-and-normal-closed-range.md)：真实固定首列矩阵U∈M_d(B_n)可逆，任意完整C_P右系数受同一个cb源范数下界；每层WOT/uw闭，递减交恰span(S_i)，零字符行与所有原n尾目标有统一正距离。指定双慢行显式3/23单位费及完整均值零柱锚P^(−3/2)最优；低头依赖原源仍开。


[R272 正常预对偶修复](results/R272-normal-predual-tail-repair-and-exact-positivity-obstruction.md)已付σ_P→ρ迹范数、保A′泛函/迹/固定尾及消raw远尾；C=P0CQ非零即失自伴，至正锥距离||C||1。[R274 最后一阶障碍](results/R274-full-commutant-basis-and-last-raw-moment-obstruction.md)给ord1、q=2^P的整个A′尾基；保非零ν消前q−1个raw矩后，第q矩=−νQ_P≠0，原全右零式恰归νQ_P C_P=0。固定行可修复，移动q/首列逆费用不能删；完整旧接口保[压缩前全文](notes/2026-11-14-open-before-R276-789f.md)。

[R276 正头完成紧凸判据](results/R276-positive-head-completion-and-compact-numerical-radius-criterion.md)：原S=[[Z,t],[I,Z]]的单位规范化后，同一正尾ν的全部正完成非对角块为X=√νK√ν、w(K)≤1/2。原全理想零式iff ν(Z²−t)∈N且νZ+X+X*t∈N；X集迹范数紧，最小商距离达到，完整数值半径对偶式(5.2)可给严格排除证书。raw唯一Stein解仅为额外特例；须对实际相容ν_m链证明某步距离>0，不能把N内非零缺陷删零或免费移动Z_m/单位逆成本。

**余正常接口。** 固定正常矩仅c0/o(m^(k/2))，不付平方和；正Walsh迹尾δ无速率，不能当新ann。远尾擦除保锚须carry×聚合费→0，非UHF强单位不付未知限制。真ann迫q_m↓0，周期r≤q/100、deg≤q³、exp参数≤q⁶指定滤波已排；非周期/超预算/真密度专属和全部q_m仍开。旧平方选择器、张量、热球、纠缠与无速率预算保本次全文，固定非ann例不外推。

## 当前接口二：实际边界的除法饱和

固定负边界ℓ²(N0)上的线性 $T_N,T_Y$（R200 §1），$M=\ker T$、$N=\overline{BM}$、$W=M\ominus N$。核至少含e0；它们不是上方已排核的原Haar二次式。R187/200 已付各有限稳定像及 $M\cap\operatorname{Ran}B^r\subset N$；普通无权 $N=M$ 仍开。环境有限孔稠密、模N成本、M外坏见证和横向 $T^*M$ 同构不提供核内原像。所有旧常数、失败路线、完整尾旗和逐层证书保[本次全文](notes/2026-11-14-open-before-exact-top-and-rank-two-reduction-1cf.md)。

**合法窗口与真实费用。** [R239全整数窗](results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原carry、低投影 $e^{-74d^4}$、零源lift $e^{-75d^4}$，$d\asymp\log^{1/3}q$；$K_*=3(16/770)^{1/3}$、$c>K_*$权核及真D尾常数 $K_*/2$ 已付。$\sum1/[\ell(1+\lambda^2)]=\infty$ 足N，$\lambda^2=O(q\log^{2/3}q\log\log q)$ 足但未得。真 $\lambda^2=\langle G^{-1}r,r\rangle$ 保全部Schur；$Q_1^\circ=O\mathcal G\mathcal G^*O^*$、$H_2^\circ=S_HS_H^*+\mathcal R(I-\Pi)\mathcal R^*$ 不替旧通量。

**原源流。** [全像/纤维](results/R271-appendix-exact-left-source-flow-range-and-minimal-upward-extension.md)保Nsrc=ker i0*(L+B)、真MP/primitive与原同未来；环境源不能替代。

**同一good-top的增长负前缀。** [M3完整+flat定理](results/R271-appendix-full-plus-flat-negative-prefix-repair-and-complete-top-cost.md)付初次λ/Xi/µ，近共同log^(1/3)旗保原锐K预算。[新宽旗](results/R271-appendix-wide-negative-source-prefix-and-exponential-effective-window-budget.md)另取h~d^.75/8的完整L+B负前缀与H=2h真M2头交，有效Keff≥e^(59d³/256)/(2^19d)；按Keff重选R~σm√Keff/128及角阈，后续λjoint≤√2||w||ρ^.25，不乘巨大c到未知尾率。全顶部完整链差/同w/相容低流/反馈保，固定Gram相应须O(Keff)，未证明；初M3、后M2与旧未来范围分清。

**旧大范围。** R~√Q/角C≥K^-2旧单旗只付左像，全部cross-head KKT与未付普通右费保快照，不能套到联合余源。

**同D内两旗联合。** [完整定理](results/R271-appendix-tail-adaptive-joint-quotient-with-complete-top-cost-transport.md)付µ²≤||w||²ρ/√K、λ²≤2||w||²√ρ及a0+b0<2族；同闭交/精确头/两费Pythagoras/全低流保留。旧R~√Q的大范围仅付左像，不能套其单旗KKT到联合余源。

**固定测试Gram。** [原最小双链](results/R271-appendix-fixed-physical-tests-and-minimum-two-chain-local-gram.md)保A_n=−D_UK D_KK^-1i_n、K_n,h=A_n*(R_D−R_Z)A_n及Γ斜条带。固定n的O(K)足杀w，非零w反迫同一f≥c²K/(8ε²)；真实跨头上界仍缺。

**固定测试伴随流。** [正耗散/整段正交](results/R271-appendix-fixed-test-adjoint-source-flow-and-joint-good-top-budget.md)同b付测试窗4n/K与弱误差2√(2n)ε/K，端点守恒。[裸商](notes/2026-11-14-actual-test-flow-filtered-bare-chain-and-primitive-free-source-kernel-2220.md)付primitive-free v/t、全部缩头和a1=D†(t_b−e1)，真幂保e；输入/物理误差平方和及最低泄漏已付，e右逆与端点不可删除。

**真正测试端点。** [同f端点截断](notes/2026-11-14-fixed-test-endpoint-truncation-and-small-two-fee-source-kernel-2220.md)保q_end−k_end，准确µ(t−s)²+||Y_f||²=Δ、Xi(s)²≤2||Y_f||²、Δ≤4n/K；不交窗混合Gram不是纯两费Gram。新[同余商测试族运输](notes/2026-11-14-fixed-physical-test-family-in-the-common-wide-quotient-boundary-2220.md)用ρ̂=max(ρ,Keff^-1/4)固定同一个M3/精确M2头/联合两旗映射，同时处理实际r和所有f∈T_n。测试左像与P_b f之差算子范数≤√n[2/√K+√2a′+√2Keff^-1/8]→0，测试两费≤4n/Keff、与rhat处于全部相同约束；测试修正λ至多O_n(Keff^3/16)，与原flat配对仍小。主<Lrhat,Shat f>准确保留<w,f>，其趋零/所需局部Gram及λ(Shat f)仍开。

**已付的原头运输与角度接口。** [完整左右运输](results/R239-appendix-full-right-fee-transport-and-model-kernel-source-flag.md)保同g/全部primitive/物理旗、ρ≤e^−d⁴/20，µ/Xi比较只用于真负图闭交。[退化头完整源流](results/R239-appendix-degenerate-head-full-source-flow-and-model-window-family.md)保全部四短旗、同w及一次运输，不能独立运输不同窗。[同未来双投影角](results/R239-appendix-future-band-projection-angle-and-complete-common-cost-negative-graph.md)保完整负图/非闭值域逆域，固定高谱阈只付指定窗预算；低C完整左Schur、普通右费、逐孔相容和免费阈值趋零仍未付。原三度量/首行/各孔权、全部常数与公式保[本次全文](notes/2026-11-14-open-before-R277-789f.md)，裸低与完整右旗仍不同。

[R277 原零源商一孔行分类](results/R277-original-source-quotient-one-hole-rows-and-complete-leakage.md)：实际连续尾全部c∈ℓ1的κ_c能保kerℬ（甚至仅保模任意K≤d−2前缀）iff c=λb；非比例有同一真MP塔的完整d−1源头泄漏。压缩交换子模零源为零不够，合法负前缀正规方程本身亦不能消此泄漏；C=Σb³E的未压缩graph小范数不能直接下降。须实际构造带修复作用并付跨birth真MP/高返回，或利用未知实际W源另有约束；未据合法环境反例否定N=M。

**真幂、两道桥及失败捷径。** [准确底项与两桥](results/R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)保α²=真幂底项+||Gcal†ζ||²。原19/10、P_K伴随q³及单ζSchur全稿见快照：raw首桥可巨大而同源完整链便宜，不能作pure/实际W反例；自由中段与真实flat来源仍保原限制。

**原头逐列低泄漏。** [完整新界](results/R271-appendix-columnwise-low-height-leakage-and-sharp-cubic-log-common-cost.md)以同源真幂底项付λ/ψ/真正c−a，列界e^(134j⁴)；kfast用268得δ²≤50(k−1)/(3m³)，kwide用134得δ²≤3logm/(67m)，可直接代入M3负前缀。H~d^.75大旗及真正pure低对角范围见主稿/快照；高对角、实际测试端点仍开。

**实际裸首头pure。** [准确高域Schur与深段局部化](results/R271-appendix-pure-return-from-actual-bare-first-head-and-depth-localization.md)固定f=−e0*a，pure=−(I−PkerSH)Hf，不改低链；前K段费用平方≤2(K−2)SΦ²，K≤2零。原good-top的H~d^.75低深度指数付清；源F_h且K≥h时深尾准确为e0*I G†ζ深jet，非整ψ支持。全actual pure的e^(25d⁴/2)粗界仍不足；真实深段加权尾及端点继续。 [有限失败路线](notes/2026-11-14-finite-first-jet-gram-square-shortcut-fails-kernel-2220.md)以完整有理两投影证13<pure/||σ||²<14，否普适Kpure≤Mker²；头η/孔窗非原参数且σ不保窄ζ来源，不能作实际反例。

**原回缩范围。** 全位置低triplet/birth联合/线性失真及原来源分离见快照；同pair限定保留，不免费联合不同配对划分。

[实际W角度门槛](results/R271-appendix-actual-defect-angle-and-window-distortion-barrier-for-retraction-sources.md)用原零源lift付回缩左像与固定W的分离：支撑带 $[q-T,q]$、失真χ给整窗必要 $\sum\chi^{-2}/(T+1)\to0$；有界χ仍不能替实际W源。χ趋1时才有对任意固定H向量的分离。primitive源的左最小者严格在q层。回缩source和固定M图来源不可混同。

**相邻尾Gram的未闭部分。** 既有出生一首末边、有限头/池和两组＋一位全出生全高度范围，以及旧松弛反例的准确量词，保[此前全文](notes/2026-11-14-open-before-R274-789f.md)与下方R273；更多权组及无限尾仍开。

**其他原边界接口。** 新[原连续尾birth1全高度顶桥](results/R271-appendix-original-birth-one-all-height-polynomial-first-return-anchor.md)对完整真幂逆先全逆后压K，给τ_t/(t+1)^17≤H_t^-1≤τ_t及全部旧列非交换乘积≤(h+2)^61 S_m H_(ℓ−1)；最高d无新列，D1*真实Θ锚费≤(d+2)^(61/2)√S_m，q/m一致。原正边网络/标量Newton没有外推为矩阵Newton；a≥2、Γ跨birth及无速率锚乘增长仍开。双宽商/负配对、深jet Schur、天然四块真重排等范围全保快照；两带不可免费取交，无权增长/指定回馈/pure继续。


[两组＋一位全出生全高度](results/R239-appendix-two-weight-groups-one-exceptional-all-births-all-heights-strict-bound.md)的严格c1已闭。[R273](results/R273-two-exceptional-weights-complete-schur-recovery.md)恢复两组＋两异常位：出生一3D及2≤t≤min(q,L)的4D完整MP/单参数Schur，保两硬端；相邻矩阵序和高端其他出生仍开。证明细节/148例核对见正文，不能由消元前标量序跳到同源矩阵序。

[R281 极强位全高度传输](results/R281-heavy-bit-height-transfer-and-sharp-universal-first-edge-lower-bound.md)把旧第n+1边回传至新第n边，保完整同源PSD块与有限强权阈值。全出生首边与全高度的最优普适常数相同；等权中央边迫该常数≥1，真实八位birth2首比22801/43836>1/2。一般上界1仍开；不能用强等权池压δ而省掉内部出生，真实密度只趋1/2上方。

[R283 精确配对填充](results/R283-exact-singlet-padding-and-half-density-universality.md)以同时被D,D*消去的真实反对称对，令全部旧Γ成为新共同约化块，最高合法高度不变。对任意ε,δ0>0，全部有限问题均可精确嵌入δ<δ0且1/2<sδ<1/2+ε；因此该薄带的最优普适首边常数已与一般问题相同。未进入R279已付低占据区，不能省掉新增出生。

[R279 全高度仿射 MP 比较](results/R279-bosonic-affine-primitive-gram-transfer-and-low-occupation-bounds.md)给 X_n≥I+(n/r)(X_r−I)，全有限合法范围/无限正 ℓ² 行均成立。全部低占据相邻常数改善，首边 sδ≤1/(2√2) 已得 c1；原慢尾范围 s≤(m+1)/(6√2)，未覆盖一般巨出生。真硬核 Γ2=2I+4L*L+M*M 的联合 M 能量仍缺平方下界；[共同 annihilator 反例](notes/2026-11-14-common-annihilator-affine-sharpness-789f-next.md)说明仅 Euler/全坐标不变性不足，反例不是 Boolean。

[R275 一位全高MP/三次创新](results/R275-one-bit-full-primitive-schur-recursion-and-innovation.md)保任意旧正权、同源/顶硬端；旧两birth有c1则两对角继承。余完整创新正块(5.2)须由同一B与旧G/L支付。[联合占据附录](results/R275-appendix-joint-occupation-blocks-and-first-edge-necessary-bound.md)已付全高四项H、W/SI−W跨birth正块，并付a²≥Σb²/4时首边上左必要块；全首边交叉/一般高度仍开。[首边SOS](results/R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md)付真实3块等价，S1/S2加旧低birth第二边足全部新权，但两候选一般正性未证。任意birth1首/末边已由R271闭；高birth/graph仍开。 [R278 Serre积分](results/R278-boolean-serre-finite-top-integration-and-weighted-birth-traces.md)给全部真实跨birth桥的精确首边身份及加权迹消去；尚缺同一G1度量的正运输/Gram，不能删负桥项。

**其余已付的原头、完整图和共同费用接口。** 两物理头/两下降真 MP、同未来负图、全尾近共同前缀、逐列立方根对数头预算、统一左核图/低头反馈、完整接合正 Gram、Boolean 两带/Γ 收缩、固定低行四次费用、D2 三次权顶锚、全深度宽源带及增长模型核幂的准确公式、常数和每条原稿链接，保 [压缩前全文](notes/2026-11-14-open-before-R279-789f.md)。它们均保同一未来/同源/真正负图及原累计费，仍不支付固定测试局部 Gram O(Keff)、ordinary 右费、pure 深段与高 birth D1*/Γ 合并；不能把裸/完整 Schur 或坐标截断互换。

## 当前接口三：一般系数行、多个模式与中央域

完整已付行类、种子/比较/最高字符条件、全部旧公式及原稿链接保[本次前全文](notes/2026-11-13-handoff-open-before-faithful-vacuum-support-0c.md)。这里列下一实际缺口，未列的旧接口保持原状态。

1. **普通慢行与未知限制。** 实u奇次全部位移/幂闭，偶次余α^(2k)；有限谱部分须共同存在才能跨行。实负正定辅助已闭，正号碰撞/双无界未闭。1<α≤3普通全部重数、居中迟首κ>2的λ0及无副本重根仍开。主/辅助尺度、种子、零位置、ΓY预算不得互换；全H单射稠密不传未知M。
2. **原双行见证。** 真迟首核给同一ζ和正秩一ρ同时湮灭SA′、TA′、ZA′，S=X+Hζ、Z=Y−B0+Hζ²。整函数全右替换(X,Y)→(−Hζ,B0−Hζ²)和快混合矩已付；这些必要增长界有固定非湮灭正态反例，仍欠实际联合非零快证书/来源特殊正常锚。不能跨ζ混用ρ。
3. **导子及实际源。** 固定阶ad强单位给全部广义核全等向及kerT^n⊂closureRanT^m；不付实际值域或限制稠密。全域高导子有强单位但不是单个导子像，短Leibniz末段/实际伪逆费用仍开。纯等权高ad WOT0只限其原模型。
4. **有限复模式。** ≤5正实log复二次全Q已闭；指定六模式F²的全部λ,w已由真实Bell逆/有理jet证书闭合。[指定六模式F³第三矩](results/R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)付16维完整Schur和17低变量加权六次R3，仍须证明有实际逆的B_r自然幂∈gradR3；普通first Bell分母次数障碍不等于非循环。一般Σ内、无池、无限模式及更高幂仍开。
5. **相对乘积与自然域。** 相对ℓ1双乘积、单慢加快、快分式和空谱锚两方向按旧条件保留；复杂相对ℓ2、三以上cocycle、双全C与非解析闭包未闭。正自然词、热/预解和共同正则子须保原域；可数全H稠密像之交不保证与未知M非零相交。

### R150 六模式三次：当前完整范围和剩余层

原 $F^2$ 全参数已闭，$F^3$ 的全局自然幂/实际逆仍开。下列均为指定原K与物理Hankel形式矩的结论，不代普通ISP。压缩前每条中间支撑/消元与证书入口保[本次全文](notes/2026-11-14-open-before-exact-top-and-rank-two-reduction-1cf.md)。

**已闭全部低本质三次层。** [总定理](results/R150-appendix-all-essential-cubic-dimensions-at-most-three-have-zero-matched-bell-values.md)：essT3≤3临界三Bell零；ess≤2仅迫T3=0，rank1/ess3为空，Cat2/3的W±/Q|T3判据保。非零Bell余点必ess4/5/6，自然幂未付。

**高本质rank1原中心17式。** [泛参数全分类/有限Σ](results/R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md)给M5泛秩4354、Σ={gΔ=0}外恰H=h y²,V=(6h−1)y³/4，Δ为全部4354子式gcd。[逐点秩控制](results/R150-appendix-rank-one-noncontact-centered-rank-controls-macaulay-projection.md)及完整数域重建器付rankP≤124+2rankAy。[P+](results/R150-appendix-rank-one-Pplus-means-complete-critical-classification.md)、[P−](results/R150-appendix-rank-one-Pminus-means-complete-critical-classification.md)、[E8](results/R150-appendix-rank-one-E8-means-complete-critical-classification.md)分别以固定D原大秩4352/不可约子式提升，全部十四共轭仅纯mean/T3=0。加四接触点的切向型，原Ay所有rank8参数已全17式闭，任意振幅/任意H,V秩均保。当前有限余集只可能g≠0且rankAy9，Δ尚未显式求尽或清空。[参数域原理想证书计算](notes/2026-11-14-rank-one-parameter-ideal-ci-plan-789f.md)已按新规由CI改当前环境：特征0九个准确横向平方的原生成元lift及分母，另有限域作发现；尚无运行结论。其他mean秩的高ess仍另开。

**Cat1旧链。** 共3–5/重数/∞旧证书全保快照；rank1/ess3为空，不外推高本质。

**Cat2旧链。** ess3全退化iff W±且Q|T3已闭，主稿/原低梯度链全保快照；高本质未闭。

**已排V4的原张量，仍供其他层比较。** reduced/double mean的完整H/V/T3块式保快照，不能删D块低梯度或给复权加正性。

**纯原K禁阻。** tangent/value、两向cusp、conic/cubic等已闭原核禁阻全保快照，只在原physical条件使用。

[two-value conic禁阻](results/R150-appendix-two-physical-value-conic-companions-force-orthogonality.md)保全部原参数/∞；不扩任意非physical或高本质类。

**其余既有与仍开范围。** 有限原子/两平面/局部J³⊂I⊂J等已闭范围见快照；最高式不能替低梯度。高本质、全局匹配Bell自然幂、局部单位的实际算子逆及普通域仍开。

## 其他仍开放的路线与不可互换的极限

[R280](results/R280-odometer-weighted-factor-and-closed-sublattice-exclusion.md)已排任意可测复权的全部真加权因子不变空间，因而排闭逐点子格及相位共轭保正投影；每个非零轨道仅已证闭子格生成H。一般L²线性循环性、非标准主理想分类、完整A′核、外部紧交织继续。R12紧夹积/自伴链障碍及R14指定硬谱截断非紧与faithful弱极限已付；它们不排所有外部方法。family293仅超不变/有限因子投影范围，不是普通ISP答案。

同一物理源、原核旗、自然域和正常预算按已付范围使用；环境/有限模型不替实际来源，全部旧限制保本次全文。继续上述未闭接口，完成标准不变。
