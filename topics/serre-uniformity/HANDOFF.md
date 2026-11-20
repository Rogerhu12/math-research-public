# Serre 一致性交接

## 目标、授权、维护与规则

证明绝对C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达README标准。**

**维护会话：serre-public-astra-20261120-de0a3e3b。** 已部分克隆并真实pull main，接手serre-public-astra-20261115。最新前态逐字在[H归档](handoff-archive-2026-11-20-before-conjugate-primitive.md)与[open归档](open-archive-2026-11-20-before-conjugate-primitive.md)，内接全部旧pins/公式/关闭边界。只消费已成来源，不重做已登记结论。

**已读规则提交：9685b950d87f579b41fee47aac1ba5271a42a58c**（2026-11-20T11:26:23.657689+00:00；终端真实git pull --rebase origin main，两README无diff）。相比b77de2c7仅根课题表新增held-10pct；两README完整已读。root SHA256 581402c2 / topic 35f82f3d。此前来源与原pins沿[旧归档](handoff-archive-2026-11-16-before-Igusa-Frobenius-residues.md)。

每结论立即推；每push前且至少每小时真实pull。NFF立刻pull --rebase再推循环成功，禁force。每pull检查两README，有变只读diff并立即执行，SHA记此。PAT仅CLI，不入文件/提交，root独占main。新数学仅本公开仓库Actions；外部只纸证/IO/schema/hash/AST。raw不入Git/Release，本轮只/tmp和stdout。H<10KB、open<30KB、每MD<100KB、topic<200MB；log用Asia/Taipei≤5行，不写根LOG，不设额外审批/测试门。

## 当前工作入口与断点

1. **全p同h选择**：R945已排无例外“完整trace非零⇒中央Q′单位”。R949/954两原序列的CM mark公式全常数已定；[R957](results/R957-original-Legendre-filter-as-a-fixed-pole-CM-convolution.md)给原共同格点、Legendre平均的七阶conic极点/六次K6闭式及λ⁴完整primitive mask。准确marked polynomial的系数恰单位乘同h的P_(h−1)fi gj，非零仍开；固定核非零/全Fourier非零不能代原mark非零，两评价权h−3/p−h−2不是R913两权。
2. **原完整trace**：[R955](results/R955-original-Cartier-nilpotent-packet-is-a-single-odd-chain.md)证实际CM包的Cartier nilpotent部分N恰单奇链L=2m+1，ker=kF、coker由原λ非零检测。原trace非零 iff L=1；失败 iff原W^-有Cω=Φ_w(F)的前像，最短坏链3。先完整U5零primary再Cartier Fitting，不假设整包nilpotent；实际共轭mark返回同一H6，不添第二低权核。R952 whole饱和仍是更强充分条件；R950低权对角已闭。[R958](results/R958-original-r2-Cartier-matrices-and-one-moment-trace-criterion.md)给r2全两向Cartier矩阵：L_-t^j=(3j+1)(3j+2)t^j−(6j+7)²t^(j+1)，真实R_F=−2D^(2N+1)β²C^p mod tH。原前像存在 iff ℓ_N(R_F)=0；精确S^p=−216c_momℓ_N(R_F)，c_mom=Tr((3−2e0)DC/β²)已证非零。继续判指定moment，不把c_mom单位当trace单位。
3. **原全Abel/height**：[R948](results/R948-rational-quadratic-Abel-root-and-original-coordinate-separation.md)已证两有限p的二次scalar根在pZp，非中心iff真char0 M2≠0，v(w*)=2+v(M2)−ν/2；两例ν0/M5阶−5。另一真实h按R727全tail分离额外根，原开盘全Abel零集仅中心；仍不排正秩非零MW像或替代height。

## 最新已成：原类、完整商与两个中央零

[R944](results/R944-original-CM-Gauss-Manin-homotopy-and-supersingular-principal-parts.md)：原fine全六上ΩV=6∇Z+6^r r!ΨF，保正KS/相对Frobenius/原两CM权；全SS最高极部−g_Pρ^r/A^r准确来自R932，全部低项保留，非任意亚纯cohomology断言。

[R945](results/R945-original-central-sigma-zeros-and-same-label-alternatives.md)：run44719847377及独立44720732478/source2ca40e872成功。p227/h115的f18=0,g18=136；p857/h433的f71=176,g70=0。中央Legendre单位而完整S=95/568非零，原Q′恰零。**无例外中央单位桥已被反例排除**，不否定充分大p/有限例外或Serre。两q2的积101/335单位，中心阶恰2；scalar/w的pR0根可仍为0。实际替代227/h151 sigma16配旧Legendre单位；857/h445新Legendre298乘旧sigma187为21，R940给Q′单位。旧48窗/trace/顶端/Legendre不重算。

[R946](results/R946-universal-Bol-divisibility-and-final-supersingular-obstruction.md)普遍T^r=6^rA^rD_r，最后A由O_r控制；[R952](results/R952-exact-Cartier-formula-for-the-last-Hasse-obstruction.md)准确给O_r(H)=r!(𝒰H)^p/B^(p−r)|SS，kerO_r=ker𝒰。𝒰是q系数a_pn的逆p半线性根，真实Igusa Cartier保1/6/角色/全Norm；whole饱和等价𝒰全packet零，命名F被杀不够。R951配对=r!H_w(H′,𝒰H)，仍不识别不同权低/高对角。

[R951](results/R951-Bol-concomitant-and-supersingular-obstruction-symmetry.md)：实际J_r=δO_r的完整SS配对ΣD_rH·H′/B²由显式Bol concomitant给(−1)^r对称性；原偶r为对称。命名F在两radical，不迫全packet消失；J零也只让O落M_r，非原R932泛函。

R947原W满足∇W=ΩV、全极部−V_PB^(p−r−2)σ^r/((r+1)A^p)，zV非零；R950低权指定对角全p单位。R953正则πW=6G/真实E_r+给原高权Hasse边界，保Igusa −1/6/全Norm，底Hodge正则剩余项−6^r(r−1)!F/B；p-curvature/谱列另证F_r注入。

[R956](results/R956-original-trace-as-a-fixed-low-weight-Cartier-edge-pairing.md)现给原高低准确比较：E_Bol=Sym^(r−1)H⊗F*ω的紧支连接coker两端为H1ω^(2−r)(−C)与S_(r+2)，全部SS/cusp无torsion。真实K_rY由Cartier(A^(r−1)YρKρ)定义，原插值Y_F|SS=r!F^p/B^(p−r−1)。S=6^(r−2)/r·〈zV,K_rY_F〉，λ=mI(cF)^(1/p)/(36d1r!)乘此pair；cσW=−6^r(r−1)!sF确认同源。r2负δ插值唯一，K2Y_F=αV4、α=([Q^p]Y_F)^(1/p)；α≠0仍待证，r8保完整M8左项。继续真实divided Frobenius/Cartier比较，不用抽象低权单位替代。

## 已成来源与精确回执

R933–955的完整尺度、真实run、规则读SHA及关闭边界保存在[本次H归档](handoff-archive-2026-11-20-before-Bol-Cartier-comparison.md)，证明及SHA在[结论索引](results.md)。归档仅缩短交接，不重做原算术。

R933/934固定第二类Cartier与p41 Legendre零已成；R935原h8/h32在固定a11外不共零，旧543d03f8三分位本原双标签已覆盖全部允许p。R937–940原权34核、mark单位、normal首层/J32比较及固定B34均成，仍未判变化临界积。
R936/939保L=Fp²[t]/tH、t0权1/H根权3/fine12和未知d1/cF；β^p=β，原C唯一负RHS ODE，Tate勘误E6=−c6/η12=−6sD/KS=+du/D。原完整trace六值及另48值皆非零只有限窗。R941常数项公式保F^p及全部点权。R942权10完整double T5²的广义零部分仅V10，非零值147456/666²，禁止旧错误单mark矩阵。
R943固定p11/第三位Cartier、9+9原符号证书已成；203素数窗非全p。R945两独立run44719847377/44720732478的中央零及替代标签见上；current request仍指已完成第二run，不能重触发旧数学。

## 原全p几何源：不得换对象

R859–898的BT/Drinfeld/Igusa/cusp/36theta源及两旗已成；R904 K^p独立不判指定jet。保原J_h、β̄=P_(h−1)(1/s)/P_(h−1)(0)、J32=(6B)^5(P_(h−1)(1/s)fi gj)^p/12，不混h/两权/半周期/det/ζ²。
R906 qTpJ=qBTpB保a_h；R908/910/911两αp线给上半r=2h−p−1，R916真整ann给Ω contentπ^pr、原q另π^ea_h。R913两权k−=2p+2−2h、k+=2h−p+1保全Norm/Hecke/单双Igusa/C4。
R918/R920原V4/V10标记单位独立于Tate勘误。R921/R924真completed Hom延拓/节点排低层，中央κx^(g−1)y、β/α=5A/4或11A/10，p^−a_h G整restricted、顶项单位、content恰p^a_h。R925完整校准log≡id、char0先消N_h给全j平方比，v(c_cal)=a_h−1−v(N_h)/2，不选无依据共同平方根符号。
R932原非零Serre类经F_dR识别V4/V10，G=Θ_Q^(r−1)F、∂G=A^rV/6，原λ为非零mI(cF)^(1/p)/(d1·6^r(r−1)!)乘完整SS和，j0指定项零。该全和与高Q′已由R945证明须分开。

## 原固定Y高度：有效来源与真正缺口

R805–930原W/两图/146、418、273jets、真cY/127全纯、七trace/K固定DK272、五Z/两权、三十共轭、七连接/完整Artin微分迹已成；全部pins见最新open归档，不重算。特征零未展开处仍未展开。
R927参考同λ0=1、完整2+6/0+8、Normρ阶−508/0，原t首项466867763/728442038、比315436983；267项只需9，254极阶/U272/两t/dual7不省。**这个辅助有限域比不是p-adic高度。**
R907旧43924786163止core前KeyError；[schema已修](notes/R907-inherited-transport-configuration-repair.md)，四必要原artifact真实404/request待字节，摘要不能代数组。五目标672铅笔/九NormΦ/端点格未成，Φ=QZ/qχ正乘，DN先−dlogQN再Gal7。六旧run终态与空artifact见[真实核查](notes/2026-11-20-resumption-and-run-availability.md)，预算false FINAL非负数学结论。
真正缺real Rcal I_Z³、YP/FM128/634及508rank507、P1 c/a、原σ/cY、活跃eη、d/N、完整nonp/Poincaré/splitting/height。R870原16ni及1959位d*须合法好约化niPiξj非零才判支持；YL1零非rank0，UE=dY+2period，End⁰G=F/torus≥g+1，μ3qφ*=0不删Y。

## 不可重开的边界

R317只剩完整Nns、p≡2或5mod9、a³+db³=1/p|b，D/bc无上界。R707固定41八CM已闭，不外推。R575正CM根号−/逆twist秩零撤回，R706 h1零保留；非挠/log/rank/Abel单位/深盘根数都非height。原RF/SP/ZA/41S/41C、b/s/λζ²一次、CRT6逆、246/82^10、P0P1/ν/theta二挠/fullCorr/nonp全部沿归档。ordinary43/776bitGaussian5与R779 Shapiro同Σ/C4已闭。主目标仍OPEN。
