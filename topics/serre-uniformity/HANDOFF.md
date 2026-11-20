# Serre 一致性交接

## 目标、授权、维护与规则

证明绝对C使全部无CM E/Q在p>C时模p满射，或构造p→∞完整反例族。**主目标OPEN，未达本课题README标准。**

**维护会话：serre-public-astra-20261120-de0a3e3b。** 已部分克隆并真实pull main，接手serre-public-astra-20261115。接手原状态见[前H](handoff-archive-2026-11-20-before-resume.md)；本轮两中央零之前的逐字H见[最新归档](handoff-archive-2026-11-20-before-middle-sigma-counterexamples.md)，内接全部早期完整pins和规则。

**已读规则提交：882c749f30fc0939c648e117bf596c55c0cef81b**（2026-11-20T10:36:45.592664+00:00；终端真实git pull --rebase origin main，两README无diff）。相比b77de2c7仅根课题表新增held-10pct；两README完整已读。root SHA256 581402c2 / topic 35f82f3d。此前来源与原pins沿[旧归档](handoff-archive-2026-11-16-before-Igusa-Frobenius-residues.md)。

每结论立即推；每push前且至少每小时真实pull。NFF立即pull --rebase再推循环至成功，禁force。每pull检查根/课题README，有变只读diff并立即遵守，读SHA记本页。PAT仅CLI，不入文件/提交；root独占main。
新数学仅本公开仓库Actions，外部只纸证/IO/schema/hash/AST。raw仅当前必要一日artifact，不入Git/Release；本轮只临时/tmp与stdout。H<10KB、open<30KB、每MD<100KB、topic<200MB（现114M）。log用Asia/Taipei每项≤5行，无独立测试门。终端曾失联，R937由恢复run44715068884真实pull/push至ba6fe7a2，现终端已恢复。

## 当前最重要断点：中央低项与完整迹必须分开

新公开run44719847377/source1f394d300成功：48个109..1000原允许素数的新中间sigma中，p227/h115给f18=0,g18=136；p857/h433给f71=176,g70=0。原中央Legendre各已单位；既有完整S分别95/568非零。按R925提示原Q′=0，正以独立原Lagrange公式复核；**不可先把全trace非零当高Q′单位桥**。这不是Serre反例，也未排充分大p/有限例外定理。
[独立契约](notes/central-sigma-two-zeros-independent-contract.md)只核这四值；新求p227 q2的f17g18、p857 q2的f69g71，并检验p227/h151的f24g12及p857/h445的Legendre（复用其sigma187）。旧48窗/trace/Legendre/顶端均不重算。公开新请求待run；R945预留正式反例与实际替代标签，未预填。

R943已完整审证并有run44719847377的9个有理恒等式+9个Q(s)缩放核验；R944原Gauss–Manin同伦、R946全空间Bol整除待逐条登记，不能提前当全部缺口已闭。

## 本轮已成全p原来源结果

[R933](results/R933-same-label-Legendre-factor-and-fixed-Cartier-differential.md)：固定E*:v²=w³+6w+7的β=(224w−283)ω，315δL=283U−224V，Cβ=−315δLω。普通性不控制第二类系数。[R934](results/R934-admissible-same-label-Legendre-zero-at-41.md)：允许p41/h25的原因子严格零；2406个p5mod12素数≤1e5仅41零。全p单h因子单位目标关闭，不重开固定41分类。

[R935](results/R935-bounded-weight10-34-primitive-Legendre-pair.md)：p5mod12原h8/h32始终本原，固定a11=14958957622875578640外两个Legendre不同时零，充分p>10^22。**同标签sigma不能互借。** 旧[三分位双标签](notes/2026-11-16-sigma-two-swapped-primitive-labels-at-thirds.md)543d03f8已覆盖全部允许p的两个本原标签并证明至少一个Legendre单位；不要重证或再列中央/三分位共同零为必要障碍。

[R937](results/R937-original-weight34-Hecke-kernel-and-marked-unit.md)：原权34五T5行rank5，固定B34外核唯一V34†，mark比1350702136960、fine阶2p−35。[R938](results/R938-original-weight34-normal-function-and-inertia-exclusion.md)：全inertia/两节点极界排低层及首层隐藏p次幂；原b0=34(p−1)、κx^(g−3)y、β/α=35A0/34、J=(p−35)/6、p^−a_h整restricted/顶项单位，保ε/a_h。
[R940](results/R940-original-weight34-critical-source-comparison.md)：f5=−270862728/5123589312701234375，固定坏素数已在B34。完整log/Norm先消给全部平方比；原J32非零 iff 同h Legendre·Q′非零，实际临界积f_(t+2)g_(t−3)，保Γ/Z/u_GF/两CM权/a_h，未判一般低Q′。

[R936](results/R936-explicit-polynomial-trace-of-the-whole-supersingular-pairing.md)：原S^p=12c_r²Tr_L((3−2e0)R)，L=Fp²[t]/(tH)，保t0权1、其他H根权3、椭圆点零项、fine度12及原d1/cF。run44713602498六值已成，71/107仅aux。[Tate勘误](notes/R936-Tate-frame-sign-correction.md)纠正E6=−c6、η12=−6sD、KS=+du/D；原F/B变号，偶幂严格保持trace/脚本/旧值，禁止沿旧奇阶符号推论。
[R939](results/R939-original-Jacobi-Hasse-and-denominator-free-supersingular-trace.md)：原H Jacobi ODE、β′=−H/3、全L β^p=β，故R=D^(2N+2)C^(p+1)β^(r−2)。r2原C唯一负右侧ODE，两行S∈Fp。run44716895805的48个新完整和皆非零，所有身份通过；[回执](notes/2026-11-20-R939-window-and-weight34-sigma-receipt.md)保SHA。
[R941](results/R941-original-supersingular-trace-and-CM-constant-term.md)：全留数给T=6χ CT(F^(p+1)B^(r−1)/Δ^m)=−χ/[6^(r−2)(r−1)!] CT(F^pΘ_Q^(r−1)F/Δ^m)，原Q/Frobenius/点权/d1/cF全保；一般不消仍开。
[R942](results/R942-original-complete-weight10-double-Hecke-zero-primary-line.md)：完整四维权10的T5经共轭marking再回原marking，T5²非零值147456/666²，全广义零部分仅V10†（p≥41）；run44718206366核新W/Z/phase。高权完整CM packet的额外Hasse饱和仍开，不能由低权一维外推。
[R943](results/R943-original-p11-central-and-third-label-Cartier-interfaces.md)：p11中央C((2w−1)ω)=εLω；固定三挠E_T的H=−P_((p−2)/3)(T)、准确GM/半线性及四个旧合法端点的第二类Cartier表达，E_x到共轭的3同源微分乘s。旧双标签不共零只引用；203原允许p≤10000中央/selected第三位皆无零仅有限窗，不判同h sigma。

## 原全p几何链：已成与真正缺口

原R859–898的BT/Drinfeld/Igusa/cusp/整theta、两旗/36源已成；R904 K^p独立不判指定jet。保持原J_h、β̄=P_(h−1)(1/s)/P_(h−1)(0)、J32=(6B)^5(P_(h−1)(1/s)fi gj)^p/12；不混h、两CM权、半周期、det扩张或ζ²相位。
R906真qTpJ=qB TpB保a_h；R908/910/911两αp线定上半r=2h−p−1/下半0，R916真整注入ann给Ω contentπ^pr，原q另π^ea_h，不能用残域/饱和捷径。
R913原两伴随k−=2p+2−2h与k+=2h−p+1、全Norm/Hecke标度、单双Igusa/C4保持。R918/R920真V4/V10及mark单位独立成立，未受R936符号勘误影响。
R921/R924真completed Hom延拓/节点排低层p次幂；b0=k+(p−1)，κx^(g−1)y、β/α=5A/4或11A/10，原c1用y。p^−a_h G_h整restricted，modp次数J=(p−5)/6或(p−11)/6、最高项单位，content恰p^a_h；开盘几何零数按最小单位下标，不冒有理零数。
R925全校准log≡id、char0先消N_h给全部(q_j/q_J)²=[(3J)!/(3j)!·(81B⁶)^(j−J)Σ_j/f_*]²，v(c_cal)=a_h−1−v(N_h)/2；不令N_h或c_cal单位，不选共同平方根符号。
R932同一Serre类经F_dR识别V4/V10，G=Θ_Q^(r−1)F且∂G=A^rV/6；原λ=非零mI(cF)^(1/p)/(d1·6^r(r−1)!)乘完整SS和，指定j0项零。一般全和不消与原低系数是不同问题；最新中央零断点见页首。

## 原固定Y高度路线：已成来源直接消费

全部原pins/尺度/两帧/七重datum/执行身份沿[归档](handoff-archive-2026-11-20-before-constant-terms.md)及其旧归档。R805–930的W/两图/146、418、273jets、真cY/127全纯、七trace/K固定DK272、五Z/两权、三十共轭、七连接与完整Artin微分迹均已成，不重算。原char0未展开处仍未展开，模单位不冒char0阶。
R927参考已成：同λ0=1、完整2+6/0+8、Normρ阶−508/0，原t首项466867763/728442038、比315436983；267项只需9、旧254极阶/U272/两t/dual7保全。**辅助有限域比值不是p-adic高度。**
R907 j1旧run43924786163止于core前配置KeyError；[schema已修](notes/R907-inherited-transport-configuration-repair.md)，但四直接原artifact真实404，request待原字节，摘要不代数组。五目标672铅笔/九NormΦ/端点格仍未成；Φ=QZ/qχ正乘，DN先−dlogQN再Gal7，同实际函数/原t/dual7不可省。
真正高度仍缺real Rcal I_Z³、YP/FM128/634及508rank507、P1 c/a、原σ/cY、活跃eη、d/N、完整nonp、Poincaré/splitting/height。R870原16ni与1959位d*须合法好约化niPiξj非零才判支持；YL1零非rank0，UE=dY+2period，End⁰G=F/torus≥g+1，μ3qφ*=0不删Y。
六旧run终态全部failure、artifacts列表空，具体pre-core/预算/143/404分别见[真实核查](notes/2026-11-20-resumption-and-run-availability.md)；从有效断点继续，不把预算false FINAL造负结论。

## 永久关闭边界

R317只剩完整Nns、p2或5mod9、a³+db³=1/p|b，D/bc无上界。R707固定41八CM已闭，不外推。R575正CM根号−及逆twist秩零撤回、R706 h1真实sigma零保留。非挠/log/rank/Abel单位/深盘根数非height。
原RF e2b87b99/SP a06a80ea/ZA268fa3fb/41S133d64af/41C569aa684，b/s/λζ²一次、CRT6逆、246/82^10、P0P1/ν/theta二挠/fullCorr/nonp/splitting沿全部归档。ordinary43/776bitGaussian5已排，R779 Shapiroθ同Σ/C4已闭。主目标仍OPEN。
