# Serre 一致性交接

## 目标、授权与维护

证明绝对C使所有无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，尚未达README标准。**

**维护会话：serre-public-astra-20261120-de0a3e3b。** 已部分克隆并真实pull main，接手serre-public-astra-20261115。压缩前逐字状态在[最新H归档](handoff-archive-2026-11-20-before-pure-Hurwitz-residue.md)，沿链保全部旧source/SHA/尺度/失败边界，不重做已登记结论。

**已读规则提交：8c807fbbf31c66c1fb57b453ea56f4f9c7bf7443**（2026-11-20T13:53:52.947330+00:00；终端真实git pull --rebase origin main，两README无diff）

两README完整已读，SHA256 root 581402c2 / topic 35f82f3d。每结论立即推；每push前且至少每小时真实pull；每pull检查两README，有变只读diff立刻照办并记已读SHA。NFF/lock-ref竞态立即pull --rebase再推直到成功，禁force。PAT只CLI，不入文件/提交；root独占main/H/open/index/log。

新数学只本公开仓库Actions，本地只纸证/IO/schema/hash/AST。raw不入Git/Release；本轮stdout和scratch，无artifact。H<10000B、open<30000B、每MD<100000B、topic<200MB；log Asia/Taipei且每次≤5行，不写根LOG。已成结果不因压缩重跑。

## O1：同一个原本原标签的三个因子非零

p=6N+5，h=6i+7，i+j=N−1，须同h使原primitive/Legendre mask下P_(h−1)(1/s)fi gj≠0。R949/954/957–959全失败 iff (1+24X)|原B_p(C,X)，X0=−1/24，fine额外阶3。R964逆CM族只控h_(i+2)；R966/968完整heat/Gaussian源给Z_i∈M_(p−5)，mark/E6^N=−72(-864)^−N fi gj。须实际filtered span含A/E4或mark functional非零。

R969有限113/131/227全mask rank10/11/19与组合/额外q核已过，不重跑；R971以M0=37182145、2φ(M0)<M0及Dirichlet排全p full-span，未排特定A/E4包含。R945中央零227/f18、857/g70与完整S单位并存，**全trace单位不推同h中央单位**；R734 Legendre单位已成但不能独完O1。

## O2：原完整trace及高坐标单位

R955/R970整个原CM packet为Cartier nilpotent单链，L=dim包=rank level9高权p−1/p−7完整classical Hecke模；**原S≠0 iff L1 iff完整η_f单位 iff准确TU adjoint值单位**。保Γ6/Γ036整格、det返回、σ⁻¹T_p和2/3 type，无两Weil增倍；坏链是真非CM congruence。

R958 r2原moment S^p=−216c_momℓ(R_F)，R_F=−2D^(2N+1)β²C^p，目标moment仍开。R960/965真实Igusa因子h=L+1，κ=(1/p)[x^((p²−1)/3)]a^(2p+2)=36α=−g_pT=−g_pS^p/432，g_p=48[x^(m+1)]a²单位。**不能把该因子换成固定CM椭圆源height2**；链顶单位不推链底。

R973原E−:y²=x³−1/g3=4/无Gaussian，balanced c_n=[z^n w^(n−1)]σ(z+w)/(σzσw)，n=p−r。公开run44740851091/job136303836405/source f3f947dab32911ac0a40040ceb24242d4595488d已完15.197670298s，41/47/227/857 residues13/4/171/317，旧B11/10/179/489；exact rational与single-pole核全过。rows9079B/hash3539d7b3/prefix4aa3136e/summary21210cd6已纯IO核，只消费，不重跑。

R974实际TU整parabolic格Ω_f±/P_n整，P_n=(Ω−/(2πi))^n；adjoint=u_n c_n P_n²/(Ω+Ω−)，u_n=2^(n+2)3^((n−8)/2)(n−1)!单位。因此**c_n单位⇒η_f单位⇒S非零**，只单向，不预设period比单位。KS/additive Manin cosets/3处Euler/i相位保全。

R975 U_n=n!(n−1)!c_n整heat递推，U_n=F_n(12g2,−216g3)/12，F_n=(R^(n−1)E)|E0；Wilson c_(p−r)=−r!(r−1)!F_(p−r)(0,−864)/12。n<p均整，近p阶单位仍开，不从R^p高导数单位反除。

R972 a=r+1=3/9,n=p+1−a,m=(p+1)/3,b=a/3；χ核是真conductor-p环类域L，L_P=Qp²(ϖ)、ϖ^m=−p。low HT kill u1/high kill u0，u0=AH(ϖ^b,λ1)、u1=AH(ϖ^(m−b),λ0)。DDR Fil有+1、upper breaks b/m与1−b/m；DFG全部假设、低T=O、Euler/loc给global H1=1,H2=0,A_L^χ=0。实际unit线log modp=γ0λ1ϖ^b+γ1λ0ϖ^(m−b)，γ0≠0，**S≠0 iffγ1≠0**。整log只用e=m<p−1；cσ保两线。

R976 fixed7 U7=V7^(σ−1)，V7=Norm_(ray H_p/L)Ψ(1;p,7⁻¹p)，σ=Frob_(2+s)。48及χσ−1全原p单位；OV完整格/Rubin same-χ finite Gras与A_Lχ0给eχU7生成真实unit格，ray w_R精确取消。log〈U7〉=ΣB_jϖ^j给γ0=B_b^p、γ1=B_(m−b)。R977原E+/g3−4/Δ−432和φ*ω_C=ω给D_C=p12Δ(pτ)/Δτ，V7²=ξ²D_C⁴，logU7=2log(D_C^σ/D_C)，v_ϖD_C=4；δ=D_C/ϖ⁴的近顶log仍未知。

R978 strict整LT g′0=1，τ^(p²−1)=p，X=τ^(3(p−1))，ϖ=ηX、η^m=−1。F7(gT)=Δ⁴T48H(T)/7，先半kernel整norm得V7=ξC0X8G(X)，再e=m取log；j−m vp(j)≥m排j≥m高carry。定义log(σz/z)=−ΣG_Nz^N/N，所选N=3(p−1)j的regularizer48单位，准确B_j=24η^(−j)(ζ^j−1)G_N/N。低G_(a(p−1))单位，**S非零 iff高G_(n(p−1))单位**；高低指标和p²−1不提供非零传递。

R979同一normalized discriminant的Cayley u给T=Ω²Imζ·u/π=−3旧PL参数，log[Δτ/((1−u)^12Δζ)]=12Σ(n−1)!c_nT^n；原n3mod6有c_n+=−c_n−，粗W=T³的m−b项与c_n成unit比。D_C=[p(1−u_p)]12 expG_+(T_p³)，保Ω²相位/p12，尚无W→ϖ整transport。

R980 published Robert1980 level1 Thm8原S_k恰G_k；E+的E4=0/E6=864、B_p=E_(p+1)单位。t=a,n有G_(t(p−1)+p+1)=B_pG_(t(p−1))/(12t)。低star4p−2/10p−8已单位，高star np+a仍未知；两反射对不相连，γ1=−288η^(−(m−b))(χσ−1)B_p^−1G_(np+a)。1978 pair只至少一非零，1986单项结论须F/Q abelian而此处dihedral不符。

R982 theta对称Hjj=jH_(j−1,j+1)，c3+=1/6、c6+=−1/900单位；literal barλ→λ^p加共同α/ξ会迫α/β同时−3/2与−6/5，故模型严格不成立。仅排共同标量，不排index-factorial/Gamma/carry或单near-p比较。

R981新pure Hurwitz留数/两digit压缩已独立纸核：s=x^−1/2，f=L(s)/s，(N−1)G_N=[X^(N/6)]C f^(1−N)避N−2除p；f=A(X)C(X^p)+c_pX^eD(X^p)保唯一resonance，输入/末收缩O(p)、中间长度O(p²)。四行bounded powers与独立strip-p/positive-power/Lagrange channel，41/47另exact rational ℘；小j3/6只诊断factorial候选25β³G_K6=4G_K3，不assert。B_p=12(-1)^((p+1)/6)B_old，原c_n+取负。

**current request已替换为R981新pure四点计算，尚待公开run回执；不重触发R973。** root核script/方法hash及sparse路径后推送；四p41/47/227/857，只small41/47加j3/6。继续真p-Frobenius/Guerzhoy整余项和实际双变量比较，未预设高unit。R983预留回执；R984由literature研究真正有限整Poincare对象。

## 继承任务与永久边界

[open](open.md)、[结果索引](results.md)与[H归档](handoff-archive-2026-11-20-before-pure-Hurwitz-residue.md)保全部来源/run/hash。R963允许r2的1000<p≤1e5全部1582点无零、R967κ/g_p尺度、R969/R973均已完只消费。R944/947/950低GM单位、R946/951/952 whole Bol/两个radical、R956紧支coker/λ尺度、R962 r8左项零与α8式已成；whole饱和须全𝒰包零，R953高Hasse不换低极部，R961链顶非链底。

O3–O6见open/归档。原J_h两CM权、det/Igusa/fullNorm/ζ²、a_h/normal顶项和全j平方比保；R913两权非O1评价权。R948 Abel盘零仅中心，不排非零MW像/证height。

固定Y的R805–930全部W/两图/jets/7K trace/五Z两权/30连接/Artin迹只消费，λ0=1/首项比非height。R907四必要artifact真404，待原字节，不以摘要代数组。五672铅笔/九NormΦ/端点格未成；Φ=QZ/qχ正乘、DN先−dlogQN再Gal7、254极阶/U272/两t/dual7保全。真正Rcal I_Z³、YP/FM128/634、508rank507、P1 c/a、σ/cY/eη/d/N/full nonp/Poincare/splitting/height仍开。R870须真实合法niPiξj非零；YL1零非rank0，UE=dY+2period、End⁰G=F/torus≥g+1、μ3qφ*=0均不删Y。

R317仅完整Nns、p2/5mod9、a³+db³=1/p|b，D/bc无界。R707固定41全129盘/8CM不外推；R575正CM根号−、逆twist秩零撤回、R706 h1零保留。非挠/log/rank/低单位/深盘数非height。旧失败/空artifact/已成Hurwitz block曲率/p²无新约束不重做；budget false FINAL不构成负结论。主目标仍OPEN。
