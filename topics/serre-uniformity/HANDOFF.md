# Serre 一致性交接

## 目标、授权与维护

证明绝对C使所有无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，尚未达README标准。**

**维护会话：serre-public-astra-20261120-de0a3e3b。** 已部分克隆并真实pull main，接手serre-public-astra-20261115。压缩前逐字状态在[最新H归档](handoff-archive-2026-11-20-before-combined-window-receipt.md)，沿链保全部旧source/SHA/尺度/失败边界，不重做已登记结论。

**已读规则提交：6048938e89d320648d9b9c21fbba4038d83e1ec5**（2026-11-20T15:22:23.916190+00:00；终端真实git pull --rebase origin main，两README无diff）

两README完整已读，SHA256 root 581402c2 / topic 35f82f3d。每结论立即推；每push前且至少每小时真实pull；每pull检查两README，有变只读diff立刻照办并记已读SHA。NFF/lock-ref竞态立即pull --rebase再推直到成功，禁force。PAT只CLI，不入文件/提交；root独占main/H/open/index/log。

新数学只本公开仓库Actions，本地只纸证/IO/schema/hash/AST。raw不入Git/Release；本轮stdout和scratch，无artifact。H<10000B、open<30000B、每MD<100000B、topic<200MB；log Asia/Taipei且每次≤5行，不写根LOG。已成结果不因压缩重跑。

## O1：同一个原本原标签的三个因子非零

p=6N+5，h=6i+7，i+j=N−1，须同h使原primitive/Legendre mask下P_(h−1)(1/s)fi gj≠0。R949/954/957–959全失败 iff (1+24X)|原B_p(C,X)，X0=−1/24，fine额外阶3。R964逆CM族只控h_(i+2)；R966/968完整heat/Gaussian源给Z_i∈M_(p−5)，mark/E6^N=−72(-864)^−N fi gj。须实际filtered span含A/E4或mark functional非零。

R969三点actual span核已过；R971严格排全p full-span，未排特定A/E4包含。R945中央零与完整S单位并存，完整trace不推同h；R734原primitive Legendre单位已成不能独完O1。

[R992](results/R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md)：在整个原M_(p−5)、F=Y^NP(z),z=X³/Y²上，真实Serre D给 **G(F)=[D²(XF)+X²F/144]/[X²(1−z)]**，全表观分母消去。诱导L=z(1−z)∂²+(4/3−7z/3)∂−55/144，Jacobi B_d有互异λd=−(d+5/12)(d+11/12)、mark1；kerG正是Tate A/E4，标量B_k(1)^−1。**原filtered V≠0且G(V)⊂V⇒同h三因子非零**，两假设均尚未一般证明。旧R969p227 central i18为pivot（组合13）、全局非零但mark0，严格排逐列本征；三个旧满秩点的G稳定无需重算。原E+帧G(F)(0,864)=(25F−D³F)(0,864)/144；下一步是actual heat/kernel作用，不能从算子与mask交换冒稳定。

[R995](results/R995-original-mixed-source-for-the-first-coarse-CM-normal-jet.md)：原E−/Y−864、K=G⊗H+6F⊗Y_s、∇=∂−6ζ下，Π4DJ=Π4D²J=0使完整D³(∇²J)的两个中间Leibniz块真消；实际三支为G‴/216⊗𝒜+12uF′⊗(3𝑀−12G)+F⊗(12𝑀−144G+6ℛ)。复用旧MH3–4热式，全部P1/P2/P3与216P1P2保留，𝒜=∇²H‴，ζ修正不消G‴支。Ψ_ij首项=(a+1)(a+2)(a+3)g_(i+1)𝒜_j/216；原G(Z)mark=(25Z+Ψ)/144，E−正号/原mask/尺度不换。两个实际Taylor阶≤p−4,p−5、ζ权≤p−2，均整。root/literature逐式独审；新项尚无原retained关系，不冒G稳定或同h。

## O2：原完整trace及高坐标单位

R955/R970整个原CM packet为Cartier nilpotent单链，L=dim包=rank level9高权p−1/p−7完整classical Hecke模；**原S≠0 iff L1 iff完整η_f单位 iff准确TU adjoint值单位**。保Γ6/Γ036整格、det返回、σ⁻¹T_p和2/3 type，无两Weil增倍；坏链是真非CM congruence。

R958 r2原moment S^p=−216c_momℓ(R_F)，R_F=−2D^(2N+1)β²C^p，目标moment仍开。R960/965真实Igusa因子h=L+1，κ=(1/p)[x^((p²−1)/3)]a^(2p+2)=36α=−g_pT=−g_pS^p/432，g_p=48[x^(m+1)]a²单位。**不能把该因子换成固定CM椭圆源height2**；链顶单位不推链底。

R973/R983原四点balanced/pure与独立核已认证，sources/jobs/hashes见回执及H归档，只消费不重跑。

R974原TU格Ω_f±/P_n整，adjoint=u_n c_n P_n²/(Ω+Ω−)，u_n=2^(n+2)3^((n−8)/2)(n−1)!单位；原先只得c_n单位⇒η单位⇒S非零；R988现从实际Cartier/Robert源补逆向，仍不假period比单位。KS/Manin/3Euler/i尺度保。

R975 U_n=n!(n−1)!c_n整heat递推，U_n=F_n(12g2,−216g3)/12，F_n=(R^(n−1)E)|E0；Wilson c_(p−r)=−r!(r−1)!F_(p−r)(0,−864)/12。n<p均整，近p阶单位仍开，不从R^p高导数单位反除。

R972/R976–980真实ring-class/AH/Robert/normalized Δ完整源及全部尺度见最新H归档。原χ faithful、e=m=(p+1)/3、两个HT条件互补；global unit线γ0单位、S非零 iffγ1非零，cσ不交换两线。fixed7真实unit生成元，原half norm后取log、strict LT和η均保；高pure/lowpure各自Robert mirror不同对，低unit不能移给高。R988下文已给高γ1与balanced准确尺度，period比不反除。

R982原theta/Robert对称已排literal共同α/ξ模型；R983又以独立exact rational反例排指定factorial共ξ，均不排真正mixed比较。

R981原pure留数/唯一共振/two-digit压缩与R983四点全核已成；R983 run44748379140准确否定指定factorial共ξ模型（41/47差10/31），不重跑。

R984–987真实Frob整核、strict坐标carry、global rational LT实现及Poincare两open Cartier全证，准确公式/源/边界见最新H归档及各结果。保μbar=−β、R_T=R_tg+μC_g、首carry−3T^(p+6)/7、𝒯=Z+β^-1J_s^p、参数误差q−3与首分母pL_p=−βZ；R594/R658旧formal分解不重登。真实gluing给C(xZ^jω)=β^(1−j)j!L_jω，非共同scalar；第二Frob有限取消和theta曲率−βW不推near-p unit。

[R988](results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md)：完整Cartier与真正theta对称给 **G_(j(p−1))=−j!β^−j c_j+，1≤j≤p−2**；原r2/8、n=p−r有G_high=−β^(r−1)c_n+/(r−1)!、G_highstar=β^r c_n+/r!。原AH高坐标 **γ1=−24η^(−(m−b))(χσ−1)β^(r−1)c_n+/r!**，所有外因子单位、c_n+=−c_n−，故 **原S≠0 iff c_(p−r)±单位 iff F_(p−r)(0,−864)非零**，补成R974逆向而不反除period比。实际p-basis b0=−βB_(p−1)、b6=−β7 B_(p−7)/6!，参数差首影响q−3完整保。低a3/9 pure显式−β−3、−8β−9/35只校准已知unit；真正near-p系数全p单位、同h与height仍开。

[R990](results/R990-original-hypergeometric-fixed-r-coefficient.md)：原(E,X,Y)=(0,0,864)的三Ramanujan ODE逐式匹配 A=2F1(1/12,7/12;2/3;z)、B=2F1(5/12,11/12;4/3;z)，T=−uB/(24A)、z=u³/432。m=(p−r)/3、k=floor(p/12)时B真截成degree k Jacobi多项式；H=((1−z)B²)^−1、f_i=H_i/(1−3i)、Q=4+12zB′/B−z/(1−z)，**c_(p−r)+=(-32)^m(r−1)! [z^m]Qf^−r/4**。全分母在m<ℓ=(p+1)/3内单位，固定r2/8给O(M(p))、O(p)内存。B根/三个cusp极部准确、首resonance Hℓ=B(1)^−2单位；不能跨ℓ反除，目标系数非零仍开。

## 当前实际工作：两新窗口完成后继续一般非零

R991已完整认证R989旧r8差集349点（1000..20000），原三路/全hash见回执与H归档；不重跑。

[R994](results/R994-certified-original-combined-windows-through-200000.md)：R993公开run44760218207/job136370438703/source248592d7fabd01b1b8c548237400767e9ecec001已成功，531.337922156s且final预算真/exit0。新r8的20000..200000共2622点（20021..199877），新r2的100000..200000共1386点（100019..199967），总4008全非零/无尾段；各行首两点20021/20117/100019/100103原三路一致、完整wp ODE及全部首resonance核过。root纯IO逐块重组8段contract/7段summary，核全部sources/列表/rows/flags；payload2865567B SHA e764dff838bb24b18c8fec7f7634c2044f403e59e23a349cc00d0554c000dc8d。R988给这两个有限集原S单位，不推全p/同h/height；current R993 request完成，禁止重触发。method c1913358/script2e60046f及全部pins在回执，无raw artifact。

继续R995实际filtered关系；R996在审原端列尖点非零（5∤p+1整族），R997在写原J与UH36完整源桥，O2实际残数/period defect的非退化仍开。下一理论空号R998。主目标OPEN。

## 继承任务与永久边界

[open](open.md)、[结果索引](results.md)与[H归档](handoff-archive-2026-11-20-before-rational-LT-jet.md)保全部来源/run/hash。R963允许r2的1000<p≤1e5全部1582点无零、R967κ/g_p尺度、R969/R973均已完只消费。R944/947/950低GM单位、R946/951/952 whole Bol/两个radical、R956紧支coker/λ尺度、R962 r8左项零与α8式已成；whole饱和须全𝒰包零，R953高Hasse不换低极部，R961链顶非链底。

O3–O6见open/归档。原J_h两CM权、det/Igusa/fullNorm/ζ²、a_h/normal顶项和全j平方比保；R913两权非O1评价权。R948 Abel盘零仅中心，不排非零MW像/证height。

固定Y的R805–930全部W/两图/jets/7K trace/五Z两权/30连接/Artin迹只消费，λ0=1/首项比非height。R907四必要artifact真404，待原字节，不以摘要代数组。五672铅笔/九NormΦ/端点格未成；Φ=QZ/qχ正乘、DN先−dlogQN再Gal7、254极阶/U272/两t/dual7保全。真正Rcal I_Z³、YP/FM128/634、508rank507、P1 c/a、σ/cY/eη/d/N/full nonp/Poincare/splitting/height仍开。R870须真实合法niPiξj非零；YL1零非rank0，UE=dY+2period、End⁰G=F/torus≥g+1、μ3qφ*=0均不删Y。

R317仅完整Nns、p2/5mod9、a³+db³=1/p|b，D/bc无界。R707固定41全129盘/8CM不外推；R575正CM根号−、逆twist秩零撤回、R706 h1零保留。非挠/log/rank/低单位/深盘数非height。旧失败/空artifact/已成Hurwitz block曲率/p²无新约束不重做；budget false FINAL不构成负结论。主目标仍OPEN。
