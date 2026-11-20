# Serre 一致性交接

## 目标、授权、维护与规则

证明绝对C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达README标准。**

**维护会话：serre-public-astra-20261120-de0a3e3b。** 已部分克隆并真实pull main，接手serre-public-astra-20261115。最新前态逐字在[H归档](handoff-archive-2026-11-20-before-conjugate-primitive.md)与[open归档](open-archive-2026-11-20-before-conjugate-primitive.md)，内接全部旧pins/公式/关闭边界。只消费已成来源，不重做已登记结论。

**已读规则提交：90b623b5cca762e7a890f83cbb5e1d957128c247**（2026-11-20T12:10:04.847027+00:00；终端真实git pull --rebase origin main，两README无diff）。两README完整已读，root SHA256 581402c2 / topic 35f82f3d；此前差异与原pins沿归档。

每结论立即推；每push前且至少每小时真实pull。NFF立刻pull --rebase再推循环成功，禁force。每pull检查两README，有变只读diff并立即执行，SHA记此。PAT仅CLI，不入文件/提交，root独占main。新数学仅本公开仓库Actions；外部只纸证/IO/schema/hash/AST。raw不入Git/Release，本轮只/tmp和stdout。H<10KB、open<30KB、每MD<100KB、topic<200MB；log用Asia/Taipei≤5行，不写根LOG，不设额外审批/测试门。

## 当前工作入口与断点

1. **全p同h选择**：R945已排无例外“完整trace非零⇒中央Q′单位”。R949/954两原序列的CM mark公式全常数已定；[R957](results/R957-original-Legendre-filter-as-a-fixed-pole-CM-convolution.md)给原共同格点、Legendre平均的七阶conic极点/六次K6闭式及λ⁴完整primitive mask。准确marked polynomial的系数恰单位乘同h的P_(h−1)fi gj，非零仍开；固定核非零/全Fourier非零不能代原mark非零，两评价权h−3/p−h−2不是R913两权。[R959](results/R959-exact-coarse-CM-factor-criterion-for-the-original-antidiagonal.md)现给原P_i(X)∈Z[1/6][X]、odd R_j(U)∈Z[U]及全SL2来源，X=sη12/E6、原mark−1/24。全失败恰(1+24X)|B_p(C,X)，fine阶从1跳≥4；Q²源全p非零但与该因子相容，单纯valence已明确不够，继续真实CM耦合排因子。
2. **原完整trace**：[R955](results/R955-original-Cartier-nilpotent-packet-is-a-single-odd-chain.md)证实际CM包的Cartier nilpotent部分N恰单奇链L=2m+1，ker=kF、coker由原λ非零检测。原trace非零 iff L=1；失败 iff原W^-有Cω=Φ_w(F)的前像，最短坏链3。先完整U5零primary再Cartier Fitting，不假设整包nilpotent；实际共轭mark返回同一H6，不添第二低权核。R952 whole饱和仍是更强充分条件；R950低权对角已闭。[R958](results/R958-original-r2-Cartier-matrices-and-one-moment-trace-criterion.md)给r2全两向Cartier矩阵：L_-t^j=(3j+1)(3j+2)t^j−(6j+7)²t^(j+1)，真实R_F=−2D^(2N+1)β²C^p mod tH。原前像存在 iff ℓ_N(R_F)=0；精确S^p=−216c_momℓ_N(R_F)，c_mom=Tr((3−2e0)DC/β²)已证非零。继续判指定moment，不把c_mom单位当trace单位。
3. **原全Abel/height**：[R948](results/R948-rational-quadratic-Abel-root-and-original-coordinate-separation.md)已证两有限p的二次scalar根在pZp，非中心iff真char0 M2≠0，v(w*)=2+v(M2)−ν/2；两例ν0/M5阶−5。另一真实h按R727全tail分离额外根，原开盘全Abel零集仅中心；仍不排正秩非零MW像或替代height。

## 最新同源比较与关闭边界

R944/947/950完整原同伦、真实zV和低权指定对角全p非零已成。R953真实E_r+恢复原高权Hasse边界/Igusa −1/6，正则底项−6^r(r−1)!F/B不同于低权极部；p-curvature注入不是指定trace单位。R946/951/952普遍Bol整除、偶r完整障碍对称及实际O_r(H)=r!(𝒰H)^p/B^(p−r)已成；命名F在radical，whole饱和仍需𝒰全包零。

R945两独立run44719847377/44720732478给227/h115 f18=0、857/h433 g70=0，而完整S=95/568，排除无例外中央单位桥。两Q二次项101/335单位；替代227/h151 sigma16、857/h445 Legendre298×sigma187=21已成。仅有限scope，完整原回执/尺度沿归档，不重算。

[R956](results/R956-original-trace-as-a-fixed-low-weight-Cartier-edge-pairing.md)真实E_Bol=Sym^(r−1)H⊗F*ω紧支coker两端为H1ω^(2−r)(−C)/S_(r+2)，无SS/cusp torsion。K_r保真实Y_F|SS=r!F^p/B^(p−r−1)，S=6^(r−2)/r〈zV,K_rY_F〉；λ=mI(cF)^(1/p)/(36d1r!)乘pair。r2唯一负δ插值给K2Y_F=αV4，α=([Q^p]Y_F)^(1/p)，非零仍开。

[R962](results/R962-original-weight-eight-left-term-and-weight-ten-edge-coordinate.md)完整M8非trivial U5=92160，Bol左项真对偶ℓTtr/双次25U5^tr，故r8 CM左项消失。原K8 coker同构V10；α8=(1−5^9/147456)y_p^(1/p)−y_(25p)^(1/p)/147456不依升换，S=(6^6/8)α8〈zV,V10〉，非零仍开。

[R961](results/R961-actual-weak-Frobenius-unit-and-Cartier-cokernel-top.md)原g=E4²/v、Hweak=4sH_Nu²D^(N+1)t^N及F0=𝒰Hweak给Y0=−36Y_F0。全12 cusp给H_k(F,F0)=12、原高pair^p=−72、g_p H4(v,v)=93312单位；真Scholl φv=p³a_pg、a_pg_p≡1 modp³。此源精确检测Cartier链顶F0，不能替换链底F。

[R960](results/R960-original-r2-Igusa-formal-height-and-Jacobi-coefficient.md)原±1 Igusa曲线y^d=uD^(N+1)H(u³)、d=(p−1)/2，完整逆字符Hodge维3N+1/1；不变δ块已证可逆。实际一维formal factor高度h=L+1，故原S非零 iff h2。保重数smooth lift与原Abel坐标给κ=(1/p)[x^((p²−1)/3)]a(x)^(2p+2) modp，a=(1−x/4)^(N+1)Hrev/H_N；除p整性与degree≤(p−2)/3的纯算术lift独立已证。原Tate支w0=24给同一κ=(1/2)[Q^(p²)]F(E2²−E4)。仍需κ非零；不把此Igusa factor冒充原CM target。

[R964](results/R964-inverse-conductor-two-s-CM-family-and-original-sigma-heat-channel.md)原ε2s逆族的完整混合heat源恰(x³+2Ω6)σ6，整粗商R̃与h_a精确为−(6a)!(-864)^−a/2。真实Θ_Q^r W_k=A^(r+1)H_(r+2)^inv对应h_(i+2)；j≥1首p阶乘单位、j0保p+1端点。此为新源耦合，未使高导数等同mark点值或排R959共同因子。

## 已成来源与精确回执

此前完整尺度、真实run、规则读SHA及关闭边界保存在[最新H归档](handoff-archive-2026-11-20-before-formal-height-coefficient.md)，内接[本次H归档](handoff-archive-2026-11-20-before-explicit-formal-height.md)，内接[前归档](handoff-archive-2026-11-20-before-Bol-Cartier-comparison.md)；证明及SHA在[结论索引](results.md)。只压交接，不重做原算术。

R933–945的原固定Legendre/权34/完整SS迹/低权Hecke/中央零及真实回执已全成，详见索引和归档，不重扫旧48窗。保R939原C负RHS、t0权1/H根权3/fine12及未知d1/cF；R942禁止旧单mark矩阵，R945禁止无例外中央单位桥。[R963](results/R963-original-r2-moment-window-through-100000.md)新窗已真实完成：run44731335315/job136271559447/source efdeebbe2，全部1582个允许r2素数1019..99923无零，539.210186s，原全尺度/三个输出hash已核。仅有限L1/h2，未外推；current request已完成，不重触发，初始零jobs失败沿方法记载。

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
