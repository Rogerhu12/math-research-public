# Serre 一致性交接

## 目标、授权与维护

证明绝对C使所有无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，尚未达README标准。**

**维护会话：serre-public-astra-20261120-de0a3e3b。** 已部分克隆并真实pull main，接手serre-public-astra-20261115。此前逐字状态在[最新H归档](handoff-archive-2026-11-20-before-original-ring-class-regulator.md)，沿链保全部旧source、SHA、尺度、失败边界，不重做已登记结论。

**已读规则提交：9ba76b815f0d8fad591c63aa9290eb77406011b0**（2026-11-20T13:23:11.225392+00:00；终端真实git pull --rebase origin main，两README无diff）

两README完整已读，SHA256 root 581402c2 / topic 35f82f3d。每结论立即推；每push前且至少每小时真实pull；每pull检查两README，有变只读diff立刻照办并记已读SHA。NFF/lock-ref竞态立即pull --rebase再推直到成功，禁force。PAT只CLI，不入文件/提交；root独占main/H/open/index/log。

新数学只本公开仓库Actions，本地只纸证/IO/schema/hash/AST。raw不入Git/Release；本轮stdout和scratch，无artifact。H<10000B、open<30000B、每MD<100000B、topic<200MB；log Asia/Taipei且每次≤5行，不写根LOG。已成结果不因上下文压缩重跑。

## 当前O1：同一个原本原标签的三个因子非零

p=6N+5，h=6i+7，i+j=N−1；须同h使P_(h−1)(1/s) f_i g_j≠0，保原primitive/Legendre mask。R949/954/957–959完整mark/conic/K6给全失败 iff (1+24X)|原B_p(C,X)，X0=−1/24；fine零阶额外3，不能用全源非零/valence代共同因子排除。R964逆ε2s族控制h_(i+2)，不是fi，j0须保p+1阶乘。

R966准确单核K0=G0⊗H0+6F0⊗Y0，Π4∇²K0=−72F0⊗G0；原临界jet给U_p(C)，原B_p(C,X0)为准确单位乘U_p′。R968完整Gaussian/heat/zeta给实际Z_i∈M_(p−5)(SL2,Z_(p))，mark/E6^N=−72(-864)^−N fi gj，全mask后失败 iff全系数共同含E4³。A/E4是同权mark单位目标。

[R969](results/R969-certified-filtered-full-level-span-at-three-primes.md)run44736934491/job136290572303已成：113/131/227完整mask列16/19/35、rank10/11/19，全空间；A/E4组合和额外两q行通过。227旧0/16只消费，新mark0/64、scale4；report21986B/hash7c3e1e25由root纯IO核。有限，不重跑。

[R971](results/R971-complete-Wilson-Fourier-source-and-filtered-span-obstruction.md)完整Wilson–Fourier源保全部Gaussian/zeta/范数逆幂/有限角色；Sturm Norm<p/2时ν=t^6碰撞恰unit×Q*同射线，非普通Vandermonde。**全p full-span已排除**：M0=37182145、2φ(M0)<M0，Dirichlet无穷多允许p=6M0t−1,t2mod6时列数≤tφ(M0)−1<dim=M0t/2。只继续特定A/E4包含或原mark functional非零；较弱目标未被否定。

## 当前O2：原完整trace的普遍单位

R955原Cartier nilpart单奇链L，ker=kF，原λ检测coker，S≠0 iff L1。R958 r2两向Cartier完整，真实反角色前像 iff ℓ_N(R_F)=0；
R_F=−2D^(2N+1)β²C^p，
ℓ(t^(j+1))/ℓ(t^j)=(3j+1)(3j+2)/(6j+7)²，
S^p=−216c_momℓ(R_F)，c_mom=Tr((3−2e0)DC/β²)是比较单位、不是目标moment单位。原C负RHS、β^p=β、t0权1/H根权3/fine12、d1/cF均保。

R960真实±1 Igusa y^d=uD^(N+1)H(u³)，d=(p−1)/2，高低Hodge维3N+1/1；δ不变块可逆，一维formal高度h=L+1。原平滑lift/Abel给κ=(1/p)[x^j]a^(2p+2)，j=(p²−1)/3，a=(1−x/4)^(N+1)Hrev/H_N，m=(p−2)/3。其整性、degree≤m lift独立已证。**不能把此Igusa因子认成原CM target。**

[R965](results/R965-exact-original-trace-calibration-of-the-Igusa-height-coefficient.md)全fine SS原框架给𝒰Z=72Y_F、α∈Fp、κ=36α=−g_pT=−g_pS^p/432。原高primitive全d cusp给g_p=48[x^(m+1)]a²单位；λ=−12mI(cF)^(1/p)κ/(d1g_p)。κ一般非零仍开。

[R970](results/R970-original-Cartier-packet-and-high-CM-congruence-ideal.md)两行w=p−1/p−7的**整个**原CM包nilpotent，
L=dim M_CM=rank S_w(Γ0(9))_m，
S≠0 iff高CM完整classical η_f单位 iff TU准确Manin-period-normalized adjoint值单位。Γ6→Γ0(36)整格、Q、det返回d/h0差r0、rawHecke及σ⁻¹T_p完整；2/3实际type和H6 multiplicity给level9一线，不按两Weil分量加倍。坏链是实际primitive level9非CM congruence；r2还等价κ≠0。全p η单位未证，不搬固定低权period，不声称S=L值或valuation等式。

[R973](results/R973-certified-balanced-Kronecker-coefficients-at-four-primes.md)新balanced系数c_n=[z^n w^(n−1)]σ(z+w)/(σzσw)，原E0:y²=x³−1、g3=4、无Gaussian，n=p−2/p−8。run44740851091/job136303836405/source f3f947dab32911ac0a40040ceb24242d4595488d已成功15.197670298s：41/47/227/857 residues13/4/171/317，全unit；exact rational和原−B single-pole独立核全部过。模权2n与CM权n+1区分。rows9079B/hash3539d7b3、prefix4aa3136e、summary21210cd6均root纯IO核；current request已完，不重触发。无旧trace/同h重算，只有限结论。

[R974](results/R974-original-balanced-coefficient-and-one-sided-CM-period-bridge.md)已完整纸证：原Manin periods Ω_f±/P_n均p整，P_n=(Ω_−/(2πi))^n；KS一般整性定理去unit regularizer、critical additive periods及12个真实Manin cosets直接给整parabolic格。原TU值准确为u_n c_n P_n²/(Ω+Ω−)，u_n=2^(n+2)3^((n−8)/2)(n−1)!单位，保3处primitive3/4删除、n奇的i符号及E±1尺度。故 **c_n单位⇒η_f单位⇒原S非零**；不是逆向或数值等式。R973四点可直接消费，all-p c_n单位仍开。

[R975](results/R975-original-balanced-Kronecker-integral-heat-recurrence.md)原c_n的通用U_n=n!(n−1)!c_n满足U1=0,U2=−g2/12，U_n=(6g3∂g2+g2²∂g3/3)U_(n−1)−(n−1)(n−2)g2 U_(n−2)/12，因此U_n∈Z[1/6][g2,g3]、n<p时c_n整。保原g3=4、E4=12g2/E6=−216g3和polar κ0=1；U_n=F_n(12g2,−216g3)/12，F_n=(R^(n−1)E)|E=0。Wilson准确给c_(p−r)=−r!(r−1)! F_(p−r)(0,−864)/12 modp；所需F值非零仍开，不能倒推高导数单位。

[R972](results/R972-original-two-Artin-Hasse-lines-and-ring-class-regulator.md)已闭实际local/global判据：a=r+1=3/9，n=p+1−a，m=(p+1)/3，b=a/3；χ=(ψ/ψc)^a residual的核恰conductor-p环类域L/K，degree m，L_P=Qp²(ϖ)、ϖ^m=−p。真实低/高HT条件分别是AH双对偶线L0=kill u1与L1=kill u0，u0=AH(ϖ^b,λ1)、u1=AH(ϖ^(m−b),λ0)；DDR Fil阈值有+1，upper breaks b/m与1−b/m。DFG全部minimal/irred/short-crystalline假设已核，低T=O⇒lowSelmer0，Euler/loc得global H1恰1、H2=0及A_L^χ=0；真实global-unit χ线原始。其log modp=γ0 λ1ϖ^b+γ1 λ0ϖ^(m−b)，γ0≠0且 **原S≠0 iff高η单位 iff γ1≠0**。普通log整同构仅在真正e=m<p−1的L_P成立；cσ保两线不交换。高γ1全p非零仍开，无trace数值等式。

[R976](results/R976-fixed-Robert-unit-and-original-high-coordinate.md)已把R972 global-unit源固定为U7=V7^(σ_h−1)，V7=Norm_(ray H_p/L) Ψ(1;p,7⁻¹p)，h=(2+s)、Nh=7；(7)的Norm49 regularizer=48，χ(σ_h)−1的分子只含2/3/19，所以全原p均单位。OV完整elliptic lattice、Rubin same-χ finite Gras及R972 classgroup零给eχU7真实生成全unit χ格。ray w_R可含p，已用同一complex regulator公式精确消去，未当unit。若log〈U7〉modp=ΣB_jϖ^j，则γ0=B_b^p、γ1=B_(m−b)准确无尺度，B_b非零，**原S≠0 iff B_(m−b)≠0**。近顶值一般非零仍开。

在审R977实际p-isogeny quotient的normalized discriminant、R978严格整Lubin–Tate/完整半kernel norm的原pure BH系数；未登记前不当既成定理。各agent只写独占稿，root审后每结论单推。

## 已成计算与比较：只消费

R963允许r2的1000<p≤1e5全部1582个无零；R967两点原κ/g_p尺度通过；run/source/全部hash在最新H归档，均不重跑。R945严格排完整S单位⇒中央同h单位：227/h115 f18=0但S95，857/h433 g70=0但S568；替代h及Q²单位已成。R734全p本原Legendre单位标签、旧48素数/六值/9+9证书只复用。

R944/947/950低GM单位、R946/951/952 whole Bol/两个radical、R956真紧支coker及全部λ尺度、R962 r8左项零和α8公式均沿归档。whole饱和须𝒰全包零；R953高Hasse不能换低极部，R961链顶F0单位不能代链底F。

## 继承O3–O6、真正height及关闭边界

[open.md](open.md)与[索引](results.md)保全部任务；详细source/SHA/尺度在[最新H归档](handoff-archive-2026-11-20-before-original-ring-class-regulator.md)及[open旧归档](open-archive-2026-11-20-before-conjugate-primitive.md)。

R948原Abel全开盘零集只中心仍不排非零MW像，更非height非零。R859–932原J_h两CM权、det/Igusa/fullNorm/ζ²、a_h/normal顶项与全j平方比不丢。R913的Jacobian两权不能换O1评价权。

固定Y的R805–930全部W/两图/jets/7K trace/五Z两权/共轭连接/Artin微分迹只消费；λ0=1及首项比不是height。R907四必要artifact实404、request待原字节，摘要不能代数组；五672铅笔/九NormΦ/端点格仍缺。Φ=QZ/qχ正乘，DN先−dlogQN再Gal7，254极阶/U272/两t/dual7完整。真Rcal I_Z³、YP/FM128/634、508rank507、P1 c/a、σ/cY/eη/d/N、nonp/Poincaré/splitting/height仍开。R870实际合法好约化niPiξj非零才判支持；YL1零非rank0，UE=dY+2period、End⁰G=F/torus≥g+1、μ3qφ*=0均不删Y。

R317仅完整Nns、p2/5mod9、a³+db³=1/p|b，D/bc无界；R707固定41全129盘/8CM闭，不外推。R575正CM根号−与逆twist秩零撤回；R706 h1零保留。非挠/log/rank/低单位/深盘根数均不能代height。旧六失败run/空artifact/已成Hurwitz-block曲率/p²无新约束不重复；budget false FINAL非负数学结论。主目标仍OPEN。
