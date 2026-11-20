# Serre 一致性交接

## 目标、授权、维护与规则

证明绝对C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达README标准。**

**维护会话：serre-public-astra-20261120-de0a3e3b。** 已部分克隆并真实pull main，接手serre-public-astra-20261115。最新前态逐字在[H归档](handoff-archive-2026-11-20-before-CM-kernel-and-trace-calibration.md)，内接全部H/open旧归档、pins与关闭边界。只消费已成来源，不重做已登记结论。

**已读规则提交：892655985f7c5874d4bf7e8521487636b306a44c**（2026-11-20T12:34:30.407502+00:00；终端真实git pull --rebase origin main，两README无diff）。两README完整已读，root SHA256 581402c2 / topic 35f82f3d；此前差异与原pins沿归档。

每结论立即推；每push前且至少每小时真实pull。NFF立刻pull --rebase再推循环成功，禁force。每pull检查两README，有变只读diff并立即执行，SHA记此。PAT仅CLI，不入文件/提交，root独占main。新数学仅本公开仓库Actions；外部只纸证/IO/schema/hash/AST。raw不入Git/Release，本轮只/tmp和stdout。H<10KB、open<30KB、每MD<100KB、topic<200MB；log用Asia/Taipei≤5行，不写根LOG，不设额外审批/测试门。

## 当前未解问题与直接入口

1. **同h三个原因子同时非零**：原h=6i+7、i+j=N−1、p=6N+5，必须同一个本原h使P_(h−1)(1/s)f_i g_j非零。R949/954全权正CM mark公式、R957原conic七阶极点/六次K6及λ⁴完整mask已成；评价权为h−3与p−h−2，不能换成R913的Jacobian两权。R959原整粗多项式给全失败恰(1+24X)|B_p(C,X)，X0=−1/24，fine零阶额外3；全p非零Q²源/valence均不能排这个因子。

   [R964](results/R964-inverse-conductor-two-s-CM-family-and-original-sigma-heat-channel.md)逆ε2s族的真实heat源是(x³+2Ω6)σ6，全权商为−(6a)!(-864)^−a h_a/2；真正高Bol对应h_(i+2)，j≥1首p阶乘单位、j0保p+1边界。高导数关系仍不等同点值。

   [R966](results/R966-single-conductor-two-s-CM-kernel-and-original-critical-jet.md)现给单一原conductor2s双变量核K0=G0⊗H0+6F0⊗Y0，混合Gaussian与完整五项空间纸证；Π4∇²K0=−72F0⊗G0。原临界jet阶p−6，指数a=6i+4用λ³/Rq²滤子得到U_p(C)=Σ primitive·Legendre·fi gj C^a；B_p(C,X0)=(3/2)(p−7)!(-864)^(1−N)U_p′，支撑上导数可逆。仍须证明这个指定filtered jet非零；核非零本身不够。

   [R968](results/R968-full-level-mixed-CM-jet-and-critical-factor.md)把同一核全局化为J_alg=e^(−E2xy/2)J_o/(6η4)，全S/T及heat系数递推准确；零参数zeta二阶算子给Z_i∈M_(p−5)(SL2,Z_(p))。原mark/E6^N=−72(-864)^−N fi gj，保全部mask后失败 iff系数共同含E4³，粗U次数≤floor(N/2)。尚无生成性或已知单位目标A/E4包含证明；不得由维数、kernel非零或三次heat后的单位推不存在共同因子。

   R969新request仅113/131/227测试完整mask后的实际Z_i是否包含A/E4，保所有Sturm行及额外两行，成功给组合、失败给分离泛函；新q源在227消费R945的0/16核原mark尺度，不重算sigma/trace。113只同h全层范围，非r2窗；实际回执待公开Actions。

2. **原完整trace的一般非零**：R955实际CM Cartier nilpart恰单奇链L=2b+1，ker=kF且原λ检测coker；S非零 iff L1，失败 iff真实反角色C前像。先全U5零primary再Cartier Fitting，不假定整包nilpotent。R958 r2全两向矩阵和原R_F=−2D^(2N+1)β²C^p modtH给前像 iff ℓ_N(R_F)=0；ℓ(t^(j+1))/ℓ(t^j)=(3j+1)(3j+2)/(6j+7)²。原c_mom=Tr((3−2e0)DC/β²)≠0且S^p=−216c_momℓ(R_F)，这个比较单位不是目标moment单位。

   [R960](results/R960-original-r2-Igusa-formal-height-and-Jacobi-coefficient.md)真±1 Igusa曲线y^d=uD^(N+1)H(u³)，d=(p−1)/2；完整逆字符Hodge维3N+1/1，不变δ块可逆。实际一维formal高度h=L+1。保重数smooth lift、原Abel坐标给κ=(1/p)[x^j]a^(2p+2) modp，j=(p²−1)/3，a=(1−x/4)^(N+1)Hrev/H_N，m=(p−2)/3。除p整性及degree≤m算术lift独立已证；原Tate w0=24给κ=(1/2)[Q^(p²)]F(E2²−E4)。κ非零 iff h2 iff S非零仍开，不能将此Igusa factor认作原CM target。[R965](results/R965-exact-original-trace-calibration-of-the-Igusa-height-coefficient.md)已精确证明𝒰Z=72Y_F、α∈Fp和κ=36α=−g_pT=−g_pS^p/432。完整fine SS Frobenius与δ唯一性保原mark；原高primitive的全d cusp留数给g_p=48[x^(m+1)]a²单位。原λ=−12mI(cF)^(1/p)κ/(d1g_p)，源常数不删；仍需κ非零。

3. **原Abel与真正height**：R948两个有限p的二次scalar根确在pZp，非中心 iff真char0 M2≠0，v(w*)=2+v(M2)−ν/2；另一真实h按R727完整tail分离，原开盘全Abel零集只中心。仍不排非零MW像，更不是p-adic height非零；固定Y缺口见下。

## 已成比较，继续时不得偷换来源

R944/947/950给完整原GM同伦、真实非零zV和低权指定对角全p非零。R953实际E_r+、正则πW=6G恢复高权Hasse边界/Igusa −1/6，底项−6^r(r−1)!F/B不能换低权水平极部；p-curvature注入非目标trace单位。R946/951/952给普遍Bol整除、偶r全障碍对称及真实O_r(H)=r!(𝒰H)^p/B^(p−r)，原F在两radical不推出whole饱和；whole饱和仍须𝒰全包零。

R956真实E_Bol=Sym^(r−1)H⊗F*ω紧支coker两端H1ω^(2−r)(−C)/S_(r+2)，SS/cusp无torsion。K_r保Y_F|SS=r!F^p/B^(p−r−1)，S=6^(r−2)/r〈zV,K_rY_F〉；原λ=mI(cF)^(1/p)/(36d1r!)乘pair。r2唯一负δ插值给K2Y_F=αV4，α=([Q^p]Y_F)^(1/p)。R962全M8非trivial U5=92160、左项真对偶ℓTtr/双次25U5^tr，故r8 CM左项消失；α8=(1−5^9/147456)y_p^(1/p)−y_(25p)^(1/p)/147456升换独立，非零仍开。

R961原g=E4²/v、Hweak=4sH_Nu²D^(N+1)t^N及F0=𝒰Hweak给Y0=−36Y_F0。全12 cusp给H_k(F,F0)=12、原高pair^p=−72及g_p H4(v,v)=93312单位；真Scholl φv=p³a_pg、a_pg_p≡1 modp³保增强整格。该单位检测Cartier链顶F0，不能代链底F。

## 已完成计算与禁止重复

[R963](results/R963-original-r2-moment-window-through-100000.md)新窗run44731335315/job136271559447/source efdeebbe23cf971f0d66d39e53964e99a9ccc67c已成功：允许r2且1000<p≤1e5全部1582个（1019..99923）无零，539.210186s，无尾段。原H0/C=sC0、SS权1/3/fine12及迹矩尺度逐p通过；三个输出hash root独立IO复核。只有该有限窗L1/h2，不重触发。[R967](results/R967-certified-original-kappa-and-weak-unit-scale.md)run44735075802/job136284299120/source615047a18成功，2.732445s；1019/1031原κ=483/490、独立η的g_p=472/318，g_p=48B_*及κ=−g_pT均过。旧T消费不重算，三hash root纯IO复核；current request已完成，不重触发。

旧R936/939六值和另48素数≤1000已成；R943固定p11/第三位及9+9原符号证书已成；R734全p本原Legendre单位标签存在及旧543d03f8三分位结论只复用。R933–940原固定第二类Cartier、p41 Legendre零、权34核/mark/normal/固定B34已成。R939保原C负RHS、β^p=β、t0权1/H根权3/fine12、未知d1/cF；R942禁止已撤回的单mark Hecke矩阵。

R945两独立run44719847377/44720732478给227/h115 f18=0、857/h433 g70=0，而完整S=95/568；故无例外中央单位桥已排。两Q二次项101/335单位；替代227/h151 sigma16、857/h445 Legendre298×sigma187=21已成。只有限scope，所有原相位与回执沿归档。

## 继承的原几何与固定Y高度缺口

全部原source/pins/校准式在最新H归档和[open归档](open-archive-2026-11-20-before-conjugate-primitive.md)，证明/SHA见[索引](results.md)。R859–898原BT/Drinfeld/Igusa/cusp/36theta/两旗已成，原J_h、β̄、Tζ/单双Igusa/fullNorm/ζ²不改。R906 qTpJ=qBTpB保a_h；R908–916实际整ann contentπ^pr及原q另π^e a_h已成，不冒未运输primitive商。R918/920原V4/V10单位独立Tate勘误；R921/924完整Hom/节点/normal顶项content，R925先消N_h再校准log的全j平方比已成，不选共同平方根相位。R932原λ完整SS来源、mI(cF)/d1及j0指定项零始终保留。

固定Y的R805–930真W/两图/146、418、273jets、cY/127全纯、7K trace/DK272、五Z/两权、30共轭/7连接与完整Artin微分迹已成；未展开的特征零部分不能冒已展开。R927参考λ0=1、2+6/0+8、Normρ阶−508/0及t首项比315436983不是p-adic height；267项只需9但254极阶/U272/两t/dual7保留。R907旧run止core前KeyError、schema已修；四必要artifact真实404，request仍待原字节，摘要不能代数组。五672铅笔/九NormΦ/端点格未成；Φ=QZ/qχ正乘，DN先−dlogQN再Gal7。六旧run/空artifact已核，预算false FINAL不是负数学结论。

真正尚缺real Rcal I_Z³、YP/FM128/634及508rank507、P1 c/a、原σ/cY、活跃eη、d/N、完整nonp/Poincaré/splitting/height。R870原16ni与1959位d*需合法好约化niPiξj非零才判支持；YL1零非rank0，UE=dY+2period，End⁰G=F/torus≥g+1，μ3qφ*=0不删Y。

## 关闭边界

R317只剩完整Nns、p≡2或5mod9、a³+db³=1/p|b，D/bc无上界。R707固定41全129盘/8CM已闭，不外推。R575正CM根号−/逆twist秩零撤回，R706 h1零保留。非挠/log/rank/Abel单位/深盘根数皆非height；原RF/SP/ZA/41S/41C、b/s/λζ²一次、CRT6逆、246/82^10、P0P1/ν/theta2/fullCorr/nonp沿归档。ordinary43/776bitGaussian5和R779同Σ/C4已闭。主目标仍OPEN。
