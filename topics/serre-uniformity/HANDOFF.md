# Serre 一致性交接

## 目标、授权与维护

证明绝对C使所有无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，尚未达README标准。**

**维护会话：serre-public-astra-20261120-de0a3e3b。** 已部分克隆并真实pull main，接手serre-public-astra-20261115。压缩前逐字状态在[最新H归档](handoff-archive-2026-11-20-before-Hurwitz-reflection.md)，沿链保全部旧source/SHA/尺度/失败边界，不重做已登记结论。

**已读规则提交：cbffb49f57d36f2e2e1cf586daf41b5c4f84e181**（2026-11-20T13:42:48.613966+00:00；终端真实git pull --rebase origin main，两README无diff）

两README完整已读，SHA256 root 581402c2 / topic 35f82f3d。每结论立即推；每push前且至少每小时真实pull；每pull检查两README，有变只读diff立刻照办并记已读SHA。NFF/lock-ref竞态立即pull --rebase再推直到成功，禁force。PAT只CLI，不入文件/提交；root独占main/H/open/index/log。

新数学只本公开仓库Actions，本地只纸证/IO/schema/hash/AST。raw不入Git/Release；本轮stdout和scratch，无artifact。H<10000B、open<30000B、每MD<100000B、topic<200MB；log Asia/Taipei且每次≤5行，不写根LOG。已成结果不因上下文压缩重跑。

## 当前O1：同一个原本原标签的三个因子非零

p=6N+5，h=6i+7，i+j=N−1；须同h使P_(h−1)(1/s)f_i g_j≠0，保原primitive/Legendre mask。R949/954/957–959的实际完整源给全失败 iff (1+24X)|原B_p(C,X)，X0=−1/24，fine额外阶3。R964逆CM族控制h_(i+2)不是fi，j0保p+1阶乘；R966原秩二核和R968完整Gaussian/heat/zeta给Z_i∈M_(p−5)、mark/E6^N=−72(-864)^−N fi gj。目标为实际filtered span含A/E4或mark functional非零，不能代全源非零。

R969公开run44736934491/job136290572303三点113/131/227全mask rank10/11/19、A/E4组合及两额外q行通过，有限且不重跑。R971以M0=37182145、2φ(M0)<M0及Dirichlet严格排除全p full-span；未排特定A/E4包含/原mark单位。R945中央零227/f18、857/g70与完整S单位并存，**全trace单位不推出同h中央单位**；R734本原Legendre单位标签已成，不能单独完成O1。

## 当前O2：原完整trace的普遍单位

R955/R970：整个原CM packet为Cartier nilpotent单奇链，L=dim包=rank原primitive level9高权p−1/p−7的完整classical局部Hecke模。原S≠0 iff L1 iff高CM完整η_f单位 iff TU准确Manin-period-normalized adjoint值单位；坏链是真正level9非CM congruence。原Γ6/Γ036整格、det返回、σ⁻¹T_p、2/3 type与multiplicity均已核，不按两Weil分量增倍。

R958 r2原两向Cartier的唯一momentℓ给S^p=−216c_momℓ(R_F)，R_F=−2D^(2N+1)β²C^p，c_mom单位但目标moment单位未证。R960真实Igusa字符因子高度h=L+1，κ=(1/p)[x^((p²−1)/3)]a^(2p+2)；R965准确κ=36α=−g_pT=−g_pS^p/432，g_p=48[x^(m+1)]a²单位。**Igusa因子不能认作原CM椭圆源**；低/弱Frobenius单位只测链顶，未证链底或h2。

R973原balanced c_n=[z^n w^(n−1)]σ(z+w)/(σzσw)，E−/g3=4/无Gaussian，n=p−2/p−8。公开run44740851091/job136303836405/source f3f947dab32911ac0a40040ceb24242d4595488d已完15.197670298s，41/47/227/857 residues13/4/171/317、原B11/10/179/489。exact rational与single-pole核全过；rows9079B/hash3539d7b3/prefix4aa3136e/summary21210cd6已root纯IO核。**current request已完，不重触发**；无旧trace/同h重算。

R974实际TU整parabolic格Ω_f±/P_n整，P_n=(Ω−/(2πi))^n，准确adjoint=u_n c_n P_n²/(Ω+Ω−)，u_n=2^(n+2)3^((n−8)/2)(n−1)!单位。因此 **c_n单位⇒高η单位⇒S非零**，只单向，未证period比单位。KS/additive Manin cosets/3处Euler/i符号已核，全文及hash在归档。

R975通用U_n=n!(n−1)!c_n整heat递推已成，U_n=F_n(12g2,−216g3)/12、F_n=(R^(n−1)E)|E0；Wilson c_(p−r)=−r!(r−1)!F_(p−r)(0,−864)/12。所有n<p整，近p阶单位仍开，不能从R^p高导数单位反除。

[R972](results/R972-original-two-Artin-Hasse-lines-and-ring-class-regulator.md)：a=r+1=3/9,n=p+1−a,m=(p+1)/3,b=a/3。原χ核恰conductor-p环类域L，L_P=Qp²(ϖ)、ϖ^m=−p。真实low/high HT给低kill u1、高kill u0，u0=AH(ϖ^b,λ1)、u1=AH(ϖ^(m−b),λ0)；DDR Fil阈值有+1、upper breaks b/m与1−b/m。DFG全部minimal/irred/short-crys核准，低T=O、Euler/loc给global H1=1,H2=0,A_L^χ=0及真实原始global-unit线。其log modp=γ0λ1ϖ^b+γ1λ0ϖ^(m−b)，γ0≠0，**S≠0 iff高η单位 iffγ1≠0**。普通log整同构仅真正e=m<p−1成立；cσ保两线，不交换。

[R976](results/R976-fixed-Robert-unit-and-original-high-coordinate.md)：U7=V7^(σ−1)，V7=Norm_(ray H_p/L)Ψ(1;p,7⁻¹p)，σ=Frob_(2+s)。regularizer48及χσ−1全原p单位；OV完整elliptic格、Rubin same-χ finite Gras和A_L^χ0给eχU7生成真实global-unit格。ray w_R可含p但同一complex regulator精确消去。log〈U7〉modp=ΣB_jϖ^j时γ0=B_b^p、γ1=B_(m−b)，低非零，高仍开。

R977原E+g3−4/Δ−432、真实C=<Ω/p>和φ*ω_C=ω给D_C=p^12Δ(pτ)/Δτ∈L；F7=Δ⁴/ψ7的完整半kernel norm得V7²=ξ²D_C⁴、logU7=2log(D_C^σ/D_C)，v_ϖD_C=4。δ=D_C/ϖ⁴的log系数有γ0=2(χσ−1)d_b^p、γ1=2(χσ−1)d_(m−b)，低unit、高仍开。未把ϖ冒flat/GM坐标或把源height2搬给Igusa因子。

[R978](results/R978-original-Robert-coordinate-and-pure-Hurwitz-mirror.md)：源E+的[-p]modp=T^(p²)，Milne严格整LT同构g′0=1取τ^(p²−1)=p、X=τ^(3(p−1))、ϖ=ηX且η^m=−1。F7(gT)=Δ⁴T48H(T)/7，H∈1+T⁶O[[T]]；完整半kernel先给V7=ξC0X8G(X)、G整，再于e=m<p−1取log，所有j≥m项按j−m v_p(j)≥m严格消失。纯σ定义log(σz/z)=−ΣG_N z^N/N；仅所选N_j=3(p−1)j<m·3(p−1)=p²−1经unit regularizer48证G_N/N整，并准确B_j=24η^(−j)(ζ^j−1)G_N/N modp。低G_(a(p−1))单位，**S非零 iff G_(n(p−1))单位**；高低指标和p²−1不提供反射非零。保原root/embedding，未引新period、未在高ramification直接截σ log。

[R979](results/R979-balanced-Kronecker-and-normalized-discriminant-Taylor-source.md)：同一实际discriminant有准确Ramanujan/Cayley源，u=(τ−ζ)/(τ−barζ)、T=Ω²Imζ·u/π（原PL参数的−3倍），log[Δ(τ(u))/((1−u)^12Δζ)]=12Σ(n−1)!c_nT^n。E−/E+保Ω²相位，实际n3mod6有c_n+=−c_n−；粗W=T³的m−b项准确12(n−1)!c_n，是p-unit比例。D_C=[p(1−u_p)]^12 exp G_+(T_p³)保原p12及normalized differential；仍无W到ϖ的整比较，不能将complex式代为p-adic截断。

[R980](results/R980-original-level-one-Hurwitz-reflection-and-distinct-mirror-pairs.md)：Robert1980 level1 Thm8完整适用，原S_k恰G_k、源E4=0/E6=864，B_p=E_(p+1)(E+,ω)单位。对t=a,n有G_(t(p−1)+p+1)=B_pG_(t(p−1))/(12t) modp。低star=4p−2/10p−8已单位；高star=np+a=p²−rp+r+1单位仍恰S非零，**两反射对不相连**。原γ1=−288η^(−(m−b))(χσ−1)B_p^−1G_(np+a)，γ0保p次embedding。Robert1978 pair只至少一非零；Gillard1982高level排N0不妨Robertlevel1；1986共轭单项等价须F/Q abelian，本环类域dihedral不适用。

在推R981真实canonical f(X)=L(s)/s的两digit Lucas/共振压缩及新pure系数校准method/consumer；尚未执行。旧R973 c_n/B只消费，先纸证后公开Actions；root独占workflow/request/git。agents只写独占稿，继续双变量整Frobenius比较，不预设W=ϖ或高低unit互推。

## 已成输入、继承任务和永久边界

[open.md](open.md)、[索引](results.md)与[最新H归档](handoff-archive-2026-11-20-before-Hurwitz-reflection.md)保全部来源/SHA/run/scale。R963允许r2的1000<p≤1e5全部1582点无零；R967原κ/g_p两点校准；R969/R973有限新量均只消费。R944/947/950低GM单位、R946/951/952 whole Bol/两个radical、R956真紧支coker及λ尺度、R962 r8左项零与α8式已成。whole饱和须𝒰全包零；R953高Hasse不能换低极部，R961链顶F0单位不等链底F。

O3–O6见open及归档。R948原Abel开盘零仅中心仍不排非零MW像或证height。R859–932原J_h两CM权、det/Igusa/fullNorm/ζ²、a_h/normal顶项及全j平方比不丢；R913两权不是O1评价权。

固定Y的R805–930全部W/两图/jets/7K trace/五Z两权/30共轭连接/Artin微分迹只消费；λ0=1、首项比非height。R907四必要artifact实404，request待原字节，摘要不代数组。五672铅笔/九NormΦ/端点格未成；Φ=QZ/qχ正乘，DN先−dlogQN再Gal7，254极阶/U272/两t/dual7保全。真正Rcal I_Z³、YP/FM128/634、508rank507、P1 c/a、σ/cY/eη/d/N及full nonp/Poincaré/splitting/height仍开。R870须实际合法好约化niPiξj非零；YL1零非rank0，UE=dY+2period、End⁰G=F/torus≥g+1、μ3qφ*=0均不删Y。

R317仅完整Nns、p2/5mod9、a³+db³=1/p|b，D/bc无界。R707固定41全129盘/8CM闭不外推；R575正CM根号−及逆twist秩零撤回、R706 h1零保留。非挠/log/rank/低单位/深盘根数不代height。旧失败run/空artifact/已成Hurwitz-block曲率/p²无新约束不重复；budget false FINAL非负数学结论。主目标仍OPEN。
