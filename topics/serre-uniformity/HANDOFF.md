# Serre 一致性交接

## 目标、授权、维护与规则

证明绝对C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达README标准。**

**维护会话：serre-public-astra-20261120-de0a3e3b。** 已部分克隆并真实pull main，接手serre-public-astra-20261115。最新前态逐字在[H归档](handoff-archive-2026-11-20-before-complete-Wilson-source.md)，内接全部H/open旧归档、pins与关闭边界。只消费已成来源，不重做已登记结论。

**已读规则提交：4a5e1e0178e2ea303c068cd96dd5a78e78f56352**（2026-11-20T13:02:32.979230+00:00；终端真实git pull --rebase origin main，两README无diff）。两README完整已读，root SHA256 581402c2 / topic 35f82f3d；此前差异与原pins沿归档。

每结论立即推；每push前且至少每小时真实pull。NFF立刻pull --rebase再推循环成功，禁force。每pull检查两README，有变只读diff并立即执行，SHA记此。PAT仅CLI，不入文件/提交，root独占main。新数学仅本公开仓库Actions；外部只纸证/IO/schema/hash/AST。raw不入Git/Release，本轮只/tmp和stdout。H<10KB、open<30KB、每MD<100KB、topic<200MB；log用Asia/Taipei≤5行，不写根LOG，不设额外审批/测试门。

## 当前未解问题与直接入口

1. **同h三个原因子同时非零**：原h=6i+7、i+j=N−1、p=6N+5，必须同一个本原h使P_(h−1)(1/s)f_i g_j非零。R949/954全权正CM mark公式、R957原conic七阶极点/六次K6及λ⁴完整mask已成；评价权为h−3与p−h−2，不能换成R913的Jacobian两权。R959原整粗多项式给全失败恰(1+24X)|B_p(C,X)，X0=−1/24，fine零阶额外3；全p非零Q²源/valence均不能排这个因子。

   R964逆ε2s族的实际heat源(x³+2Ω6)σ6对应h_(i+2)，j0保p+1阶乘；高导数不能冒点值。R966单一K0=G0⊗H0+6F0⊗Y0及Π4∇²K0=−72F0⊗G0已成；原p−6阶jet保λ³/Rq²给U_p(C)，R959的B_p(C,X0)为准确单位乘U_p′。

   R968将同源Gaussian/完整heat/零参数zeta全局化为实际Z_i∈M_(p−5)(SL2,Z_(p))，原mark/E6^N=−72(-864)^−N fi gj；全mask后失败 iff系数共同含E4³，粗U次数≤floor(N/2)。不把核非零或三阶heat后单位代共同因子排除；A/E4为同权mark单位目标。

   [R969](results/R969-certified-filtered-full-level-span-at-three-primes.md)run44736934491/job136290572303/source48359d18d已成功：113/131/227完整mask列16/19/35，rank10/11/19均为全M_(p−5)；A/E4组合和两额外q行全过。227消费旧0/16得新mark0/64、scale4；report21986B/hash7c3e1e25由root纯IO核。无sigma/trace重算；只有限fullspan，current request已完成。

   [R971](results/R971-complete-Wilson-Fourier-source-and-filtered-span-obstruction.md)完整Wilson–Fourier源保全部Gaussian/zeta、范数逆幂及原mask；Sturm Norm<p/2时ν=t^6相等恰unit×Q*同射线，非普通Vandermonde。更强的全p full-span已严格排除：M_0=37182145、2φ(M_0)<M_0；Dirichlet给无穷多原允许p=6M_0t−1、t2mod6，原本原列数≤tφ(M_0)−1<dim M_(p−5)=M_0t/2。继续A/E4实际包含或mark functional非零，不能继续追全p满秩；两较弱目标未被否定。

2. **原完整trace的一般非零**：R955实际CM Cartier nilpart恰单奇链L=2b+1，ker=kF且原λ检测coker；S非零 iff L1，失败 iff真实反角色C前像。R970现已证明两行整个原CM packet均nilpotent，链长就是整个包维数。R958 r2全两向矩阵和原R_F=−2D^(2N+1)β²C^p modtH给前像 iff ℓ_N(R_F)=0；ℓ(t^(j+1))/ℓ(t^j)=(3j+1)(3j+2)/(6j+7)²。原c_mom=Tr((3−2e0)DC/β²)≠0且S^p=−216c_momℓ(R_F)，这个比较单位不是目标moment单位。

   [R960](results/R960-original-r2-Igusa-formal-height-and-Jacobi-coefficient.md)真±1 Igusa曲线y^d=uD^(N+1)H(u³)，d=(p−1)/2；完整逆字符Hodge维3N+1/1，不变δ块可逆。实际一维formal高度h=L+1。保重数smooth lift、原Abel坐标给κ=(1/p)[x^j]a^(2p+2) modp，j=(p²−1)/3，a=(1−x/4)^(N+1)Hrev/H_N，m=(p−2)/3。除p整性及degree≤m算术lift独立已证；原Tate w0=24给κ=(1/2)[Q^(p²)]F(E2²−E4)。κ非零 iff h2 iff S非零仍开，不能将此Igusa factor认作原CM target。[R965](results/R965-exact-original-trace-calibration-of-the-Igusa-height-coefficient.md)已精确证明𝒰Z=72Y_F、α∈Fp和κ=36α=−g_pT=−g_pS^p/432。完整fine SS Frobenius与δ唯一性保原mark；原高primitive的全d cusp留数给g_p=48[x^(m+1)]a²单位。原λ=−12mI(cF)^(1/p)κ/(d1g_p)，源常数不删；仍需κ非零。


   [R970](results/R970-original-Cartier-packet-and-high-CM-congruence-ideal.md)两行原w=p−1/p−7已证明：完整CM包全Cartier nilpotent，L=dim M_CM=rank S_w(Γ0(9))_m；S非零 iff原高CM完整classical同余理想η_f单位 iff按Tilouine–Urban精确Manin periods归一的adjoint值单位。完整Γ6→Γ0(36)整格、两det返回d/h0、r0不能擦除；原rawHecke比例及σ⁻¹T_p均保留。局部niveau2不可约迫全包非ordinary，2/3局部type与H6真multiplicity给level9一线。坏链等价实际primitive level9非CM congruence；r2还等价κ非零。不能换固定低权period或宣称数值/valuation等式；all-p η_f单位仍开。

   R973新[执行契约](notes/R973-original-balanced-Kronecker-four-prime-execution-method.md)冻结原E0/g3=4无Gaussian的balanced c_n=[z^n w^(n−1)]σ(z+w)/(σzσw)，n=p−2/p−8；完整exact rational与原−B single-pole独立核，首p分母逐项抵消已纸证。当前request只算新41/47/227/857四值，未预填unit；公开Actions待回执，不重跑旧S/同h。此系数模权2n、source CM权n+1严格区分；真正adjoint/Manin桥及all-p unit仍待闭合。

3. **原Abel与真正height**：R948两个有限p的二次scalar根确在pZp，非中心 iff真char0 M2≠0，v(w*)=2+v(M2)−ν/2；另一真实h按R727完整tail分离，原开盘全Abel零集只中心。仍不排非零MW像，更不是p-adic height非零；固定Y缺口见下。

## 已成比较，继续时不得偷换来源

R944/947/950的原GM/真实zV与低对角全p单位已成；R953高Hasse边界不能换低极部。R946/951/952整个S_w Bol整除、原F两radical和𝒰 q逆根保留；whole饱和需要𝒰全包零，nilpotent不够。R956紧支coker无SS/cusp torsion，K_r Y_F给S=6^(r−2)/r〈zV,K_rY_F〉；λ保mI(cF)^(1/p)/(36d1r!)。r2唯一δ给α；R962左项真对偶ℓTtr，r8 CM左项为零，α8=(1−5^9/147456)y_p^(1/p)−y_(25p)^(1/p)/147456，非零仍开。

R961全12cusp的高pair及g_pH4=93312、Scholl φv=p³a_pg与a_pg_p≡1 modp³保真正整格。该单位检测链顶F0，不能代链底F。全公式与source在最新H归档，不重做或丢原phase/Norm。

## 已完成计算与禁止重复

[R963](results/R963-original-r2-moment-window-through-100000.md)新窗run44731335315/job136271559447/source efdeebbe23cf971f0d66d39e53964e99a9ccc67c已成功：允许r2且1000<p≤1e5全部1582个（1019..99923）无零，539.210186s，无尾段。原H0/C=sC0、SS权1/3/fine12及迹矩尺度逐p通过；三个输出hash root独立IO复核。只有该有限窗L1/h2，不重触发。[R967](results/R967-certified-original-kappa-and-weak-unit-scale.md)run44735075802/job136284299120/source615047a18成功，2.732445s；1019/1031原κ=483/490、独立η的g_p=472/318，g_p=48B_*及κ=−g_pT均过。旧T消费不重算，三hash root纯IO复核；current request已完成，不重触发。

旧R936/939六值和另48素数≤1000已成；R943固定p11/第三位及9+9原符号证书已成；R734全p本原Legendre单位标签存在及旧543d03f8三分位结论只复用。R933–940原固定第二类Cartier、p41 Legendre零、权34核/mark/normal/固定B34已成。R939保原C负RHS、β^p=β、t0权1/H根权3/fine12、未知d1/cF；R942禁止已撤回的单mark Hecke矩阵。

R945两独立run44719847377/44720732478给227/h115 f18=0、857/h433 g70=0，而完整S=95/568；故无例外中央单位桥已排。两Q二次项101/335单位；替代227/h151 sigma16、857/h445 Legendre298×sigma187=21已成。只有限scope，所有原相位与回执沿归档。

## 继承的原几何与固定Y高度缺口

全部原source/pins/尺度在最新[H归档](handoff-archive-2026-11-20-before-complete-Wilson-source.md)及[open归档](open-archive-2026-11-20-before-conjugate-primitive.md)，证明/SHA见[索引](results.md)。R859–932的原J_h、两CM权、det/Igusa/fullNorm/ζ²、a_h/normal顶项与全j平方比均保持；非挠/log/低单位不替代原height。

固定Y的R805–930实际W/两图/全部jets/7K trace/五Z两权/共轭连接与Artin微分迹只消费，λ0=1及t首项比不是height。旧R907四必要artifact实404、request待原字节，摘要不能代数组；五672铅笔/九NormΦ/端点格尚缺。Φ=QZ/qχ正乘、DN先−dlogQN再Gal7；254极阶/U272/两t/dual7保留。真real Rcal I_Z³、YP/FM128/634及508rank507、P1 c/a、原σ/cY/eη/d/N、nonp/Poincaré/splitting/height仍开。R870实际合法好约化niPiξj非零才判支持，YL1零非rank0，UE=dY+2period、End⁰G=F/torus≥g+1及μ3qφ*=0不删Y。旧六失败run/空artifact不重复；budget false FINAL非负数学结论。

## 关闭边界

R317只剩完整Nns、p≡2或5mod9、a³+db³=1/p|b，D/bc无上界。R707固定41全129盘/8CM已闭，不外推。R575正CM根号−/逆twist秩零撤回，R706 h1零保留。非挠/log/rank/Abel单位/深盘根数皆非height；原RF/SP/ZA/41S/41C、b/s/λζ²一次、CRT6逆、246/82^10、P0P1/ν/theta2/fullCorr/nonp沿归档。ordinary43/776bitGaussian5和R779同Σ/C4已闭。主目标仍OPEN。
