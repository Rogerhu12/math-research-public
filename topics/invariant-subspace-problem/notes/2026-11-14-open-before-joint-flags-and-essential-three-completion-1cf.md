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

0c本轮压缩前的全部接口及旧链另保[完整全文](open-archive-2026-11-14-0055-0c.md)；与1cf最新边界/R150压缩合并，保双方新结果与原范围。

## 共同适用边界

已证闭域/共同正则器只按原范围使用：全H稠密不传未知限制/有限旗，G不扩一般慢Acal，UHF不运输未知Haar格。正常态/边界奇异态、固定次数/全部向量不同；C未必保M，全等向不代局部等向，不能删域或压缩中央耦合。所有结果仍为中间结论。

并行压缩前的H/open全文、准确范围与全部旧链分别保[1cf全文](notes/2026-11-13-handoff-open-before-nonreduced-closure-2220.md)及[0c全文](notes/2026-11-13-handoff-open-before-single-block-jets-and-complete-tail-metric-0c.md)。本页未列出的旧缺口并未关闭。本轮压缩前全部接口、量词及原链接另保[本次全文](open-archive-2026-11-13-2353-0c.md)（a054cd5268c3d855733bd17a70f6a693219668ec）；仅压缩重复已付背景，不改变未闭状态。

## 当前接口一：原 Haar 慢符号的正常湮灭者

令S_N=Σ(j+1)⁻²N_j、S_Y=Σ(j+1)⁻²N_j(I+N_j)⁻¹。两者全H单射稠密已证；是否在所有不变限制及有限放大子商中单射稠密仍开。强主理想失败准确等价于存在正有限秩Haar正常态ρ使φρ(SAcal)=0。不能任意降秩一，也不能以WOT/SOT代ultraweak。

**已排范围与未付部分。** R235/R237/R255已排连续/a.e.+双边UI、保函数非负锥、Walsh对角/有限带/entrywise-ℓ1、合格乘积基块正态及E_√3范围；一般正常正有限秩仍开。R228的C平均可保同泛函而增秩，R229不许一般秩一纯化。真实右矩仍须ε_m||G_m||→0且φρ(T_mG_m)/h_m不消失，普通L²逼近不付此预算。完整原稿链接及端点保本次归档。

**正常源与物理度量。** R230/R244保最小秩双参数和真实保锚源发散/归一弱零，hp/vp不换；真实密度头矩保τ、||v_p||≤10^(p/2)τ，真核δ_p无速率。R236实际MP/联合高幂保同ζ/ρ、原头carry、q1全row像及高q指定目标；MP上界失败不当费用下界。真实双侧正合同不能免费跨次数，全部式与旧入口保[本次全文](notes/2026-11-13-handoff-open-before-interior-node-publication-2220.md)。

**忠实首列及修复。** 完整good列在n,q→∞、M=o16^n一致WOT0，精确单向量支持可提升为完整列；仅近支持不够。G=I、q=n/M=n⁴原坏列O(n^−1/2)、均值1，修复至少(1/(4√2)+o1)e^(n/64)−1且距good趋1。没有精确支持的实际目标、有预算修复及完整联合尾正常锚仍开，全部全树/早吸收费用保归档。

**既有正常尾接口。** 原完整商距离/cb与固定非标量远尾费用发散，翻转分支的精确像、双向源与全部单位逆保持；h递推上型700/3已付。正k的175/16及额外k的26075/512、73325/512仅为变化起点族，不能当固定理想全层上型。平方根次数联合关系仅按原尺度、指定右因子成立，真空比衰减且一致WOT0；算子值Walsh全列/尾交保完整tuple、正常余式与同一正部分迹。全部参数、源费、量词、证明入口原样见[正常接口全文](open-archive-2026-11-13-2353-0c.md)；固定原理想廉价全层、一般gauge、统一正常锚及实际完整右因子仍开。

**此前的指定二次核与完整尾接口。** 完整U坐标、固定起点全层生成元/原源、normal/cb余式、真核图和单向量flip等价均按原稿保留，全部费用及链接见[0c完整接口](open-archive-2026-11-14-0055-0c.md)。现下方原Haar二次排核已使这个指定T的真核、相应图缺陷和first-flip分支为零；不再把它的非零flip/图核心列为当前缺口。一般迟首行、其他辅助系数及无该核来源的正常见证仍须逐族证明。

[实际慢正二次核已排除](results/R236-appendix-actual-slow-positive-quadratic-kernel-exclusion-by-joint-inverse.md)：对每个固定k，原T=(ΣaiNi)²−Σai²Ni²+Σ_(i>k)ai²Ni、ai=(i+1)^−2单射且像稠密。保真低头/纯高尾仅作辅助；同删池背景的全部2r逆联合Laplace主费e^(256M²)，全域高导子产生一致有界WOT单位，真实carry余量≤e^(−19r⁴)。原核上的局部矩阵完整配对恒等排核，不要求C保核。所以上述指定first-flip原核/图核心分支已闭且无非零实例；不排一般正常主理想态或未知不变子商。

[原Haar混合N/Y复相位二次核已排除](results/R236-appendix-complex-mixed-cayley-quadratic-joint-inverse.md)：逐位Xi∈{Ni,Ni(I+Ni)^−1}、任意复ai且|ai|=(i+1)^−2，原T=(ΣaiXi)²−Σai²Xi²+Σ_(i>k)ai²Xi均单射稠密。旋转Laplace把全部复移位乘积仍付e^(256M²)，混合carry误差342η和导子120的预算仍由e^(−19r⁴)压过。与R200负边界上的线性T_N/T_Y明确不同；那些核含e0，N=M及一般正常主理想不由本稿闭合。

[相对辅助下界的原Haar二次排核](results/R236-appendix-polynomial-relative-auxiliary-quadratic-exclusion.md)对|ai|上下比较(i+1)^−2、b∈ℓ1且高位|bi/ai|≥c(i+1)^−2，T=X²−Σai²Xi²+ΣbiXi单射稠密，任意复相位/逐位N-Y/有限首位例外均可。q=ceilσr²、σ=min(1/4,sqrt(c/A)/16)使联合逆主费≤4r⁴、实际误差≤e^(−43r⁴)，有界WOT平均常数e^(1/σ)。不需横截矩阵池下界；规则纯Y/bi=ai²与旧矩阵池的重叠已准确标明。

[原Acal右源/同ρ正常商泄漏](results/R236-appendix-actual-right-sources-and-normal-quotient-leakage.md)把全部背景逆换成原Acal真R_F，以最高多项式差付比较而不乘第二个巨大逆；辅助T=X²+Y的实际高导子仍有界WOT趋I。固定πX=πY=0及同ρ上，高位双向泄漏由原Walsh minus质量精确支付；πT=0后全部端点/中段交叉块保留，真实列为P_L E_F* R_F T^sρ½等，其Γ下界liminf≥τ。尚未把增长源列余额压至零，不将正常性无速率尾界乘逆费。











**余正常接口。** 固定正常矩仅c0/o(m^(k/2))，不付平方和；正Walsh迹尾δ无速率，不能当新ann。远尾擦除保锚须carry×聚合费→0，非UHF强单位不付未知限制。真ann迫q_m↓0，周期r≤q/100、deg≤q³、exp参数≤q⁶指定滤波已排；非周期/超预算/真密度专属和全部q_m仍开。旧平方选择器、张量、热球、纠缠与无速率预算保本次全文，固定非ann例不外推。

## 当前接口二：实际边界的除法饱和

固定负边界ℓ²(N0)上的线性 $T_N,T_Y$（R200 §1），$M=\ker T$、$N=\overline{BM}$、$W=M\ominus N$。核至少含e0；它们不是上方已排核的原Haar二次式。R187/200 已付各有限稳定像及 $M\cap\operatorname{Ran}B^r\subset N$；普通无权 $N=M$ 仍开。环境有限孔稠密、模N成本、M外坏见证和横向 $T^*M$ 同构不提供核内原像。所有旧常数、失败路线、完整尾旗和逐层证书保[本次全文](notes/2026-11-14-open-before-exact-top-and-rank-two-reduction-1cf.md)。

**合法窗口与真实费用。** [R239全整数窗](results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)保原carry、低投影 $e^{-74d^4}$、零源lift $e^{-75d^4}$，$d\asymp\log^{1/3}q$；$K_*=3(16/770)^{1/3}$、$c>K_*$权核及真D尾常数 $K_*/2$ 已付。$\sum1/[\ell(1+\lambda^2)]=\infty$ 足N，$\lambda^2=O(q\log^{2/3}q\log\log q)$ 足但未得。真 $\lambda^2=\langle G^{-1}r,r\rangle$ 保全部Schur；$Q_1^\circ=O\mathcal G\mathcal G^*O^*$、$H_2^\circ=S_HS_H^*+\mathcal R(I-\Pi)\mathcal R^*$ 不替旧通量。

**准确源流与原bare/flat。** [全部源流像及纤维](results/R271-appendix-exact-left-source-flow-range-and-minimal-upward-extension.md)给 $\operatorname{Ran}\mathcal T=\ker\iota_0^*(L+B)$，上源 $-AD^\dagger r+Ag$、非首头primitive $g$ 及原 $A_0^{-1}$均保。它不是实际M来源的定义。[截断与未来带](results/R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)给同一个左最小者的所有cut仍最小，$\Xi^2=\alpha^2+\lambda_{\rm flat}^2$ 的密窗和至多 $2d$ 尾能量。裸 $\alpha\le\lambda$，混合flat不能换成模型坐标费。

**当前实际余商。** [精确好top两费余商](results/R271-appendix-exact-two-fee-good-top-quotient-and-tail-adaptive-mode-deletion.md)从同一原 $u_Q$ 的不交窗选 $b\ge Q/2$、$K\asymp Q/d$，使 $\Xi_b^2\le2\varepsilon_m^2/K$，$Q=\lfloor e^{d^3/4}\rfloor$。只在top真 $\mathfrak M_b=B_b+L_bG_bL_b$ 投影到原廉价闭像与负图的交Z；准确余条件为 $\iota_Z^*\mathfrak M_b\widehat r_b=0$。若 $\lambda|_Z\le C\alpha$，左改变量平方 $\le C\varepsilon_m^2/K$、完整top右费差 $\le\sqrt2 C\varepsilon_m/\sqrt K$。同一新top的所有cut保整流，全部primitive与单步逆反馈平方和一次付清；低窗真未来带加top Pythagoras给总 $\Xi^2\le2[(1+\sqrt{C/K})^2+1/K]\varepsilon_m^2$。不把该式改成每窗独立正交或模式坐标消失。单个这样的实际good-top余源若有 $\mu^2/\Xi^2=O(Q/d)$ 即排非零W；此比较未得。旧[负图交旗](results/R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)、总H/加权H整流仍按各自范围有效。

**大模式与精确低角谱余商（已付左像）。** [新完整约束Schur](results/R271-appendix-large-triplet-and-low-angle-good-top-quotients.md)利用good-top只需保同w的左像：λ≤γ α且γ=O(K)即付µ改变量、整流/全feedback与累计两费，但不保证普通完整顶λ差趋零。原同配对可取R=floor√Q/64、s=R−1、T=2R−1、θ≤27/512，γ/K→0，全位置/birth与负图闭交已付。另取裸归一角C的E=1_[K^-2,1](C)，与完整共同费用负图P1(I+H)u=0交；真M2顶投影后保同w、ΣXi²≤(8+2/K)ε²。高E坐标由含约束乘子的完整KKT确定，低F坐标f的两费为D−B*A^-1B+T*S^-1T，左费为(X*,I)H(X,I)，所有Schur交叉与正修正保留。仅这些实际f上的O(K)比较仍开；不把高谱坐标设零，也不免费合并两类删除或付纯SH†。

**多个原廉价旗的同时实际余商。** [加权投影谱的新完整证明](results/R271-appendix-joint-paid-flag-spectral-quotient-at-an-actual-good-top.md)在同一D、同一M2下取各真投影P_j，T=Σw_jP_j；T≥δ像通过实际分解p=Σw_jP_jT^-1p付µ²≤barC·Xi²/(2δ)、λ²≤overline(C²)Xi²/δ，谱逆支付全部重叠。原大triplet、角C≥K^-2与首3头三旗可同时用；取δ=ε/||w||→0，原good-top µ改变量²≤ε||w||、相容整流/全部反馈及累计两费趋0，top原Xi²≤2ε²/K不变。新残源满足Σ||P_j rhat||M²≤3δXi²，保同w及完整共同费用负图；不是各旗坐标零或旧单旗精确KKT。新范围完整λ差只得2Kε||w||，未付趋0；实际O(K)比较仍开。

**同一原头的模型运输。** [完整左右及全核源旗](results/R239-appendix-full-right-fee-transport-and-model-kernel-source-flag.md)与原天然Schur/裸/flat运输保同一 $g=\mathcal B_\square\Gamma r$、全部自由primitive和物理旗；$\lambda_A\le(1+\rho)\lambda_\square+\rho\mu_A$及反向已付，$\rho\le e^{-d^4/20}$。模型g落全核头原像旗时 $\alpha_A\le\lambda_A\le\alpha_A+2\rho\mu_A$，$\mu_A^2\le c_\rho\Xi_A^2$、$c_\rho\to1/2$；真实M2投影只能到负图闭交。通用Jordan条件数平方不付余比较。旧锚/锐常数/自然域保归档。

[退化头完整源流](results/R239-appendix-degenerate-head-full-source-flow-and-model-window-family.md)对所有核头 $S_0=\ker T\cap\mathscr R$ 给 $Bs=G^{-1}s=K_{\rm tail}s$，不假物理约化；源像是其 $(L+B)$ 正交补，四块保全部 $(h+1,h-1,h-3,h-1)$短旗。原Q顶部先cut至Q−d，只运输一次，所有模型cut至Q−2d保持同w与完整四核头负图及两费和。不同窗独立运输不作整流。

[同未来带双投影角](results/R239-appendix-future-band-projection-angle-and-complete-common-cost-negative-graph.md)在裸归一 $u=B^{1/2}r,H=B^{-1/2}LB^{-1/2},C=B^{1/2}GB^{1/2}\le I$ 下给 $(I-C)^{1/2}z=C^{1/2}(I+H)u$ 与 $\|u\|^2+\|z\|^2\le\|y_{\rm future}\|^2$。实际源满足全部 $\ker(I-C)$ 负图及非闭值域逆域。固定高谱阈值c的正resolvent校正支付同w与累计 $\Xi^2\le4d\,\mathrm{tail}^2/c$；余条件保低C完整左Schur，未付普通右费、逐孔相容或免费c趋零。[原首头商三度量](results/R239-appendix-first-head-quotient-and-actual-row-graph-metrics.md)保真实首行及每孔权，裸低/完整右旗不同。

**真幂、两道桥及失败捷径。** [原真幂底项/两过滤桥](results/R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)给 $\alpha^2=\sum\|(D^{j+1})^\dagger A^jr\|^2+\|\mathcal G^\dagger\zeta\|^2$，实际返回 $-\mathcal R\mathcal G^\dagger\zeta$ 保两道受限 $D_3^*$、先逆后压缩及真实头旗。原primitive真逆19/10、顺次/真幂二步差距只是底项。[新原完整伴随桥](results/R271-appendix-original-tail-restricted-adjoint-bridge-cubic-energy-lower-bound.md)保完整 $P_K$，真 $\|D^\dagger C_0^*f\|^2\ge J^3/[192(m+2)^{13}]$；同源 $r=A^3xD^2(D^*)^2f$、$A^5x=0$ 可仅有 $\zeta_1$，却有独立q的便宜两层完整右链和小 $\mathcal G^\dagger\zeta$。这排raw第一桥分步捷径，未付纯 $S_H^\dagger\mathcal R\mathcal G^\dagger\zeta$、原flat或固定W来源。外桥坏向量、B2/H2不保桥核、低边释放及中间 $\Xi=FB^*RA G_{\rm eff}^{-1/2}$ 的完整交叉反馈仍开。 新[单jet头Schur](results/R271-appendix-single-jet-head-schur-and-pure-versus-completed-high-energy.md)对同源准确给 $\alpha^2=\|c\|^2-\langle M^{-1}\sigma,\sigma\rangle$、$\lambda^2=\|c\|^2-\langle(M+K)^{-1}\sigma,\sigma\rangle$；新高能量是 $Z(I+Z)^{-1}$ 矩，$\le4\|A^3x\|^2/(25m^{10})$，纯高费是同源 $Z$ 一阶矩，不能免费控制。按 $\ker A^2$ 保原首行长跳v、完整补块逆及非交换H1，实际第二返回精确经 $M_\perp^{-1}VH_1\mathcal S^{-1}\sigma_1$；只付新能量的零返回商小界。

**任意固定原源头的完整廉价旗。** [前三头原比较](results/R271-appendix-three-original-source-heads-and-uniform-complete-to-bare-bound.md)保全部原尾核阶，kerA²有λ²<37α²、kerA³有λ≤13κ α，κ只取固定首三头二维逆。[每个固定h的完整后向头补全](results/R271-appendix-every-fixed-original-head-flag-and-paid-backward-head-completion.md)已延至整kerA^h：先用实际B_h倒解所有出生一jet，再只用正向D从后向前补高输出，首行Dv2=0与全头/尾旗/封口逐项付。明确C_h(m)含两个有限几何和，κ_h≤2·7^(h−2)δ_h^−(h−1)，δ_h为原相邻η乘积；固定h与m/q一致。选C_hat_h²≤K即得h(m)→∞，在真实负图闭交M2投影后µ改变量²≤ε²/√K、完整顶λ差≤√2ε并保整流/全feedback。余条件只是真M2正交；不当物理头坐标零，没付h=d−1整个源、真正bare选择子的pureSH†或对固定W的矛盾。 [明确增长的dyadic整旗](results/R271-appendix-dyadic-original-heads-birth-one-repair-and-explicit-growing-quotient.md)进一步保原d尾旗，以含首primitive的出生1修正、一次原Σ_n相似付Γ≤e^(20H⁴)，完整λ≤8e^(20H⁴)同源真幂底项根。可取H=2^floor(3m/4−2)~d^.75，C_H²/K≤512d e^(−3d³/32)，真M2投影的原左/完整顶费差分别≤8√d e^(−11d³/128)ε与32√d e^(−3d³/64)ε；保同w/全flow/全部feedback，不付余源固定物理测试或pureSH†。

**原回缩可删范围。** [低Q全位置联合](results/R271-appendix-low-triplet-count-joint-retraction-and-original-high-energy-bound.md)保同一真实配对的至多R个完整triplet和所有指定远尾 $K_b$，原全部头/旗、$TB=I$及cross-birth均付。必须保active $t\ge\max(0,2r-1)$、短塔 $\theta<1/2$；不可联合不同配对或任意birth。[前缀分割](results/R271-appendix-linear-triplet-count-distortion-by-prefix-splitting.md)给 $\theta\le1/8,m\ge47$ 时 $C<32(1+R/m)$，同固定映射有匹配线性下界，非能量下界。上面good-top可付 $R\sim m\sqrt{Q/d}/128$；依同w尾选 $\sigma=\min[(\|w\|/\varepsilon)^{1/2},(d/m^2)^{1/4}]\to\infty$ 可扩σ倍且完整顶费差仍趋零。余高Q/全模式未付。强位-boson三费双夹、两强位原A完整二次型、任意primitive birth与整birth窗无计数损失的全部常数保归档。

[实际W角度门槛](results/R271-appendix-actual-defect-angle-and-window-distortion-barrier-for-retraction-sources.md)用原零源lift付回缩左像与固定W的分离：支撑带 $[q-T,q]$、失真χ给整窗必要 $\sum\chi^{-2}/(T+1)\to0$；有界χ仍不能替实际W源。χ趋1时才有对任意固定H向量的分离。primitive源的左最小者严格在q层。回缩source和固定M图来源不可混同。

**相邻尾Gram的未闭部分。** 原正权出生一首末边、四头+池全出生16/首降64、低占据矩形及原 $h=o(m)$ 范围已付；两/三独立头+池、两大等权组、三同权头+一位+池的全高度c1，以及二大组+一位h2/3/4按原证书保留，后者h≥5及任意多组仍开。Hankel/Stieltjes/分子一般充分性、Pearson松弛、首外延拓充分性均已排，不能删真实交叉Schur。

[出生一实际Riccati/负根正核](results/R239-appendix-birth-one-riccati-negative-root-kernel.md)、[三正参数归一](results/R239-appendix-birth-one-actual-three-positive-parameter-normalization.md)、[完整P2正分解](results/R239-appendix-birth-one-normalized-middle-quartic-positivity.md)保真实Zj负根、赔率p<r、θ∈(0,1)、全部shear项；首/第二/末第二边已付，任意两组全高度仍需实际共同源。Casimir/curvature/caps/五层外延拓的精确非实际反例及全部整数证书在本次归档中，不能冒作原反例。

[实际相邻比Stieltjes/高阶核](results/R239-appendix-birth-one-adjacent-ratio-stieltjes-and-higher-kernel.md)自足实稳定铅笔/Rolle及留数方向给Zj/Zj1=C+Σcν/(z+λν)，C≥0,cν>0,λν≥0，保强制零极点。全部归一导数矩及p/1−p局部化正性来自同一真实有限概率核，沿权比而非高度；一阶方差cap恰是既有J/K正性，不冒作增强。高阶精确生成式/81组校准已付，与完整四次的额外正组合尚待用。


**其他原边界接口。** 真实尾理想/双宽商能量与负配对、固定比例平方平均、原bare首段真幂参数化、$k\ge5d/8$深jets Schur保原完整flag/flat费用。两带比例不能直接取交；原输出切分只付末段渐近任意比例<0.450155。天然四块移两高位精确为 $A_{m-2}+D_{m-2}$，真重排同向量，但新合法上窗仍按新头h。其余未付回馈、无权增长与纯高逆继续。

[出生一有界普通权比全高度](results/R239-appendix-birth-one-bounded-ordinary-contrast-all-heights.md)对任意q,L与任意正异常权，若z=max(a²/b²,b²/a²)≤(11+4√6)/5，整个K1全部合法相邻阶严格c1。P1在δ≤0或B≥0完整支付，δ>0真实联合域迫K<Nm/M；五系数规范反射给P3，P2接全域正分解。实际η,uη<λ/4把λ=(z−1)²/z≤12/5送入两正域；固定h≥6可放至12(h+2)/(5(h−2))。大普通权比余域、一般出生仍开。

[出生一任意权比第三/末第三边](results/R239-appendix-birth-one-two-group-singleton-third-and-antepenultimate-edges.md)保整个K1及固定三维全逆，q,L≥4时q=4+x,L=4+y,z=1+u的完整四次三分子分别有12528/20539/10415个严格正整数项，度64/76/60，正常数；原始下降积不假正。小组全高度与倒数权补全部边界。故任意异常权的全高度扇区提高到λ≤8/3、z≤(7+2√10)/3；固定h≥8可到8(h+2)/(3(h−3))，h≤7全域。一般剩余只n,m≥4。

[两组加一位整个K1全高度已闭](results/R239-appendix-birth-one-two-group-singleton-all-heights-strict-bound.md)：任意q,L≥1、全部三正权，在原整个出生一层、每个合法n均Γn Γn1^-1 Γn≺Γn−1。首三末三与小组旧定理保全部边界；n,m≥4的剩余δ>0,B<0域由真实可行式严格得K<2N/3，v=1−T后的完整二次三系数全正，常数又有四个正δ系数。接P2全域与准确反射P3，保三维全逆再压二维及组内标准分量。这一有限子问题关闭；继续一般出生s≥2/更多权组、原边界与正常商，普通ISP仍开。



[两物理头/真实两下降度量](results/R239-appendix-two-physical-heads-and-true-two-descent-metrics.md)只用Ae1=e0，保g=c+bA2=(A²)0,rest，左负Schur与完整/裸右分别准确化为D²真MP原像及全部kerD²自由项。右首源−x1−bx2保符号；裸j≥2为(D^j)†D^(j−2)g h，投影损失恰高返回。三实际费各与参照图在同一1+||D||²+||b||²≤38内Loewner比较，不除tiny头枢轴；非交换flat与实际负图不能据此免费替换。

[同未来带付两头负图/连续两下降Schur](results/R239-appendix-paid-two-head-negative-graph-and-coupled-two-descent-schur.md)任意闭源X若λ≤c_Xα，则同未来带给||P_(B½X)(I+H)u||≤sqrt(c_X²−1)||y||，不假X约化两右Gram。全正resolvent付χ(t)²+2µ(t)²≤缺陷²；首两头仅损ν≤1/m，全部原窗/同w/归一累计预算保留。两头真实L+B Schur含完整BR2交叉；再用原g=c+bA2准确接−x1−by=−g h_q，两下降首自由量与全部裸投影保留，未付最终余费。

[全尾近共同前缀/增长多头负图](results/R239-appendix-near-common-full-tail-prefix-and-growing-negative-head-graph.md)原V=1⊕V+使u_i=e0*(D^(i+1))†A^ir，Σ||u_i||²≤α²不付逆条件数。完整候选的D0项与正次D项物理正交，故λ²≤(1+φ²)α²，φ=ν||V+||sqrtγ_(K−1)。取最大dyadic K且e^(221K4/16)≤sqrt m，K→∞、φ≤[m(1−m^-2)]^-½→0；同未来带付整个前K源头L+B负图，保所有窗/原w/归一累计费。完整尾阶保持，增长图不当物理坐标零。

[逐列原头预算/立方根对数负前缀](results/R239-appendix-columnwise-head-budget-and-cubic-log-negative-prefix.md)对任意整数K保原相容V_m，完整链卷积付Ψ=Σ_(j<K)||V_m e_j||ν^j及λ²≤(1+Ψ²)α²，没有段数损失。Ve1=e1、j≥2列费≤e^(3536j4)，取K=max(2,1+floor((logm/7072)^(1/3)))即Ψ≤2/[m(1−m^-½)]。同未来带付整个原前K头L+B负图，保全部窗/原w/归一累计两费；全尾阶及反馈保持，非坐标截断。




[全尾低物理头/全深度宽源带](results/R239-appendix-full-tail-low-head-source-strip-and-bare-to-complete-right-bound.md)源只限前K物理头，保原d全部E_(d−i−1)尾阶。原裸真幂投影Σ||(D^j)†A^(j−1)r||²≤α²，一次小头κ_K构造合法完整链，λ≤κ_K√Σν^(2i) α、µ²≤C_Kχ²/2。K2无相似费，Γ恰整条全深度宽K对角带。真M投影保负图/两费；K≈d^(3/4)/4可保至少半窗同w且C_Kd/|I|≤2d(1−m⁻²)^−½e^(−803d³/4096)。累计上界保留，余图不当坐标零。

[增长模型核幂/原同源可付图](results/R239-appendix-growing-model-kernel-powers-and-actual-paid-source-graph.md)对天然四块模型的全部kerT^K源，仅付Jordan每串底K层条件数。Jh+J3显式三串逐总度det−1，底K条件数≤18(K+2)^4；原低头Vn前缀真一致，保3≤ell≤n。由同p完整/裸运输及原flat配对，X={r:T^K B_TΓr=0}有µ²≤4Cχ²；K=H−2,H≈d^(3/4)/4给C≤e^(d³/16)。X同时包含旧全模型核旗与全深度低头带，无夹角；多数原窗同w/原累计预算保持，余图仍为真M正交。



## 当前接口三：一般系数行、多个模式与中央域

完整已付行类、种子/比较/最高字符条件、全部旧公式及原稿链接保[本次前全文](notes/2026-11-13-handoff-open-before-faithful-vacuum-support-0c.md)。这里列下一实际缺口，未列的旧接口保持原状态。

1. **普通慢行与未知限制。** 实u奇次全部位移/幂闭，偶次余α^(2k)；有限谱部分须共同存在才能跨行。实负正定辅助已闭，正号碰撞/双无界未闭。1<α≤3普通全部重数、居中迟首κ>2的λ0及无副本重根仍开。主/辅助尺度、种子、零位置、ΓY预算不得互换；全H单射稠密不传未知M。
2. **原双行见证。** 真迟首核给同一ζ和正秩一ρ同时湮灭SA′、TA′、ZA′，S=X+Hζ、Z=Y−B0+Hζ²。整函数全右替换(X,Y)→(−Hζ,B0−Hζ²)和快混合矩已付；这些必要增长界有固定非湮灭正态反例，仍欠实际联合非零快证书/来源特殊正常锚。不能跨ζ混用ρ。
3. **导子及实际源。** 固定阶ad强单位给全部广义核全等向及kerT^n⊂closureRanT^m；不付实际值域或限制稠密。全域高导子有强单位但不是单个导子像，短Leibniz末段/实际伪逆费用仍开。纯等权高ad WOT0只限其原模型。
4. **有限复模式。** ≤5正实log复二次全Q已闭；指定六模式F²的全部λ,w已由真实Bell逆/有理jet证书闭合。[指定六模式F³第三矩](results/R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)付16维完整Schur和17低变量加权六次R3，仍须证明有实际逆的B_r自然幂∈gradR3；普通first Bell分母次数障碍不等于非循环。一般Σ内、无池、无限模式及更高幂仍开。
5. **相对乘积与自然域。** 相对ℓ1双乘积、单慢加快、快分式和空谱锚两方向按旧条件保留；复杂相对ℓ2、三以上cocycle、双全C与非解析闭包未闭。正自然词、热/预解和共同正则子须保原域；可数全H稠密像之交不保证与未知M非零相交。

### R150 六模式三次：当前完整范围和剩余层

原 $F^2$ 全参数已闭，$F^3$ 的全局自然幂/实际逆仍开。下列均为指定原K与物理Hankel形式矩的结论，不代普通ISP。压缩前每条中间支撑/消元与证书入口保[本次全文](notes/2026-11-14-open-before-exact-top-and-rank-two-reduction-1cf.md)。

**本质三维全部均值的完整分类。** [非割线mean](results/R150-appendix-nonsecant-mean-essential-three-complete-critical-classification.md)、[秩二mean](results/R150-appendix-rank-two-mean-essential-three-complete-critical-classification.md)及[秩一mean总分类](results/R150-appendix-rank-one-mean-essential-three-complete-critical-classification.md)完整覆盖原3×4 Cat(y)的所有非零秩；零mean由原J3可逆排。essT3=3下完整临界当且仅当y/H/V全支撑W±且Q±整除完整T3，三原匹配Bell值全类零。全部H/V退化、内外mean、共同E3/E4/E5与∞均保；充分性来自完整原形式矩和全部梯度，非仅highest。仍不把分类当全局Jacobian自然幂或指定算子实际逆。

**已闭的全部低本质三次层。** [essT3≤3三匹配Bell消失总定理](results/R150-appendix-all-essential-cubic-dimensions-at-most-three-have-zero-matched-bell-values.md)不留均值秩假设：ess≤2的原最高式迫T3=0，ess3由上列全部Cat秩分类给W±/Q±。因此任意一个原匹配Bell非零的完整临界点必须essT3∈{4,5,6}；这仍须同六个mean与十一个二阶完整梯度。T3=0不是充分临界条件，尚未得到全临界点消失、B_r自然幂Jacobian归属或原算子逆。

**Cat1 的共同支撑归约。** [正确 conormal 缺陷和内支](results/R150-appendix-rank-one-mean-five-dimensional-bound-and-inside-five-space-exclusion.md)保完整 physical tangent2，先给共同E≤5，再以两个真实annW方向和两顶单项式排内mean共5，不假V满秩。[外mean共5排除](results/R150-appendix-rank-one-mean-outside-five-space-exclusion-and-common-four-bound.md)以两个完整收缩式迫g=2s+R3、V满五维，mean二jet的完整T3准确抵消；R上squarezero零则J3禁，非零分别为原physical cusp或纯tangent conic禁阻。因此Cat1/essT3=3在原highest下全部共同支撑≤4，包含∞/低局部系数0且不需低梯度。[共同三维完整分类](results/R150-appendix-rank-one-mean-common-three-dimensional-critical-classification.md)已证明任意共同E3必physical length3；三不同全部零系数分支经完整低梯度迫全等向，2+1及3jet由原contact/N/双块禁阻全排。因此此子类完整临界iff W±且Q±|T3，三Bell零；13条BigInt作者恒等式已付。新[内mean二jet块排除](results/R150-appendix-rank-one-inside-double-mean-block-four-space-is-empty.md)先排mean重数1，再保完整 $H_D=ay^2+2\beta yu,V_D=c_0y^3+3\beta y^2u$ 的21条BigInt原低块，把mean重数2、所有Rdouble/reduced及VR零/一/二项全排，不假V满秩。[整个外mean空截面](results/R150-appendix-rank-one-mean-outside-essential-three-section-is-empty.md)在不假H/V满秩下先证共同E4必physical g4，完整unit λ收缩使mean块长≤2且T3全部抵消；余长2降本质，余长3由J3/cusp/tangent conic排尽。最后[内mean三/四jet整支排除](results/R150-appendix-rank-one-inside-triple-and-quadruple-mean-block-four-space-is-empty.md)穷尽(n,j)=(3,2),(3,1),(4,3),(4,2)，以完整局部张量、两cube换元、原接触及distinct polar/cusp/conic禁阻全排；14条作者BigInt恒等式已付。由此Cat1/ess3完整临界iff W±且Q±|T3，三Bell零，合Cat2/3闭全部本质三维。全局自然幂、实际逆及本质≥4仍开。

**Cat2闭合链与下一层。** 原共同支撑≤4、全部外mean、倍D、Rdouble、κ零、约化R cubic都已排；[低V全类](results/R150-appendix-rank-two-mean-essential-V-at-most-three-complete-critical-classification.md)用42条原低梯度与全部零系数分类给iff。最后满V4 conic由纯two-value几何迫K(X,Z)=0，highest再迫mean/R正交；保两种D块的完整Γ_y给F0、Γ_R给n0，违E4全等向，见总分类完整证明。**本质T3三维只余Cat(y)=1；零mean已由原最高Hankel系数映射排。** 本质≥4和全局匹配Bell自然幂/实际逆仍开，低本质旧范围保持。

**已排V4的原张量，仍供其他层比较。** 约化mean写 $x=a v(s),z=b v(t),y=x+z$，$H_D=\rho(x^2+z^2),V_D=\rho(x^3+z^3),\kappa=1-2\rho$；doublemean写 $y=a v_0+b v_1$，$H_D=h v_0^2,V_D=(3h/2)yv_0^2,\kappa=1$。第三矩均为 $\kappa y^3-6yH_R+4V_R$，但D块的全部原低梯度不能删。所有复权不加正性。

**可复用的纯原K禁阻。** [物理切向非平方整除](results/R150-appendix-original-physical-tangent-polars-never-square-divide.md)为全部s证 $p_s\nmid(p'_s)^2$；[异点平移切向](results/R150-appendix-no-physical-shifted-tangent-conic-companion.md)证 $p_s\nmid(p'_s-cp_t)^2$。物理/割线方向的尖点两种放置全排；[物理pair gcd≥3](results/R150-appendix-physical-tangent-cubic-gcd-only-zero-and-infinity.md)恰0/∞且准确3。含physical firstjet的conic中物理值坐标不可能是切线；[κ非零doublejet cubic](results/R150-appendix-no-physical-tangent-two-jet-cubic-companion.md)由完整gcd与squarefree残值根全排；[κ零double block](results/R150-appendix-zero-cube-coefficient-double-physical-block-is-empty.md)仅highest/ess3已排。这些均保∞，按各自前提用，不把任意conic或任意E4免费排除。 新[不同physical值极线平方禁阻](results/R150-appendix-distinct-physical-value-polars-never-square-divide.md)对全部projective s≠t证 $p_s\nmid p_t^2$，不含临界或均值假设；剩双q根模式迫三physical点全等向，再由P±/E8保次数模103 Bézout排尽，0/∞原接触单排。

[两个原物理值的conic伴随迫正交](results/R150-appendix-two-physical-value-conic-companions-force-orthogonality.md)：κvw≠0且T3=κY³−6Y(hX²+kZ²)+4(vX³+wZ³)的原投影像为非退化conic，则K(X,Z)=0，无Cat/critical假设。若配对非零，两个physical自接触迫2重覆盖在两源分歧，唯一基点有限且异于源；四个完整对称方程无除特殊因子地产生两degree8整数eliminants，mod103显式互素1及全∞例外排尽。九项BigInt原K重构随稿；正交情形仍须付实际D块低梯度。

**其余既有与仍开范围。** 原本质≤2/低Gauss/非零y且T3零/有限原子与两原子局部分类、两平面完整矩判据及正平面非零分支局部 $J^3\subset I\subset J$ 保归档，未付全局自然幂或局部单位的实际算子逆。最高投影次数仅三种类型，不能替低梯度。meanCat≤1、本质≥4、全局匹配Bell自然幂、指定实际逆以及全部普通域问题继续。

## 其他仍开放的路线与不可互换的极限

一般L²循环性、非标准主理想分类、完整A′核、外部紧交织继续。R12紧夹积/自伴链障碍及R14指定硬谱截断非紧与faithful弱极限已付；它们不排所有外部方法。family293仅超不变/有限因子投影范围，不是普通ISP答案。

同一物理源、原核旗、自然域和正常预算按已付范围使用；环境/有限模型不替实际来源，全部旧限制保本次全文。继续上述未闭接口，完成标准不变。
