# Serre 一致性交接

## 目标、授权与维护

证明绝对C使所有无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，尚未达README标准。**

**维护会话：serre-public-astra-20261120-de0a3e3b。** 已部分克隆并真实pull main，接手serre-public-astra-20261115。压缩前逐字状态在[最新H归档](handoff-archive-2026-11-20-before-original-unitary-source.md)，沿链保全部旧source/SHA/尺度/失败边界，不重做已登记结论。

**已读规则提交：8e97376ea301fd22494040758b4ec089efde2ea0**（2026-11-20T15:33:42.650809+00:00；终端真实git pull --rebase origin main，两README无diff）

两README完整已读，SHA256 root 581402c2 / topic 35f82f3d。每结论立即推；每push前且至少每小时真实pull；每pull检查两README，有变只读diff立刻照办并记已读SHA。NFF/lock-ref竞态立即pull --rebase再推直到成功，禁force。PAT只CLI，不入文件/提交；root独占main/H/open/index/log。

新数学只本公开仓库Actions，本地只纸证/IO/schema/hash/AST。raw不入Git/Release；本轮stdout和scratch，无artifact。H<10000B、open<30000B、每MD<100000B、topic<200MB；log Asia/Taipei且每次≤5行，不写根LOG。已成结果不因压缩重跑。

## O1：同一个原本原标签的三个因子非零

p=6N+5，h=6i+7，i+j=N−1，须同h使原primitive/Legendre mask下P_(h−1)(1/s)fi gj≠0。R949/954/957–959全失败 iff (1+24X)|原B_p(C,X)，X0=−1/24，fine额外阶3。R964逆CM族只控h_(i+2)；R966/968完整heat/Gaussian源给Z_i∈M_(p−5)，mark/E6^N=−72(-864)^−N fi gj。须实际filtered span含A/E4或mark functional非零。

R969三点actual span核已过；R971严格排全p full-span，未排特定A/E4包含。R945中央零与完整S单位并存，完整trace不推同h；R734原primitive Legendre单位已成不能独完O1。

[R992](results/R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md)：全M_(p−5)上真实G(F)=[D²(XF)+X²F/144]/[X²(1−z)]无表观分母；Jacobi简单谱/各mark1、kernel=Tate A/E4。**原filtered V非零且G稳定⇒同h三因子非零**；不需满秩。旧p227中央pivot非零global/零mark已排逐列本征；旧三个满秩点不重算。E+标记(25F−D³F)/144，全部谱/尺度/条件保最新H归档及结果。

[R995](results/R995-original-mixed-source-for-the-first-coarse-CM-normal-jet.md)：复用旧MH热式，原Π4D³(∇²J)完整三支G‴/216、12uF′、F及全部ζ修正已核；原E−标记(25Z+Ψ)/144保正号/mask，两个Taylor阶≤p−4,p−5、ζ权≤p−2均整。新partner ∇²H‴不是旧g；所有式/尺度见结果与最新H归档，尚无原retained关系，不冒稳定。

[R996](results/R996-original-end-column-cusp-unit-and-filtered-space-nonzero.md)：原末列Z_(p−7,1)=12T_(p−7,3)的完整norm-one Gaussian给尖点常数233/(p−7)!；p233为8mod9，原允许类排除，故此列全p全局非零。原h=p−4的primitive iff5∤p+1、Legendre=P4(1/s)=19/9单位，故 **5∤p+1整族的原filtered V≠0已证**。5|p+1时此列被删；CM mark/实际G稳定仍开。一般cusp完整式a!CT Z_ab=[v^b](∂−6ζ0)²Π3(e^v(1−v/2)^(-b−6))保全Gaussian/ζ，首p整界和单Bernoulli简式已核，不假其为原Legendre。

[R997](results/R997-original-epsilon-vector-and-unitary-boundary-source.md)：实际原ε-vector=(6d0)^−1Σ_(r mod6)ε(r)Ψ_(Hr)确在旧UH36空间，靠CM整源/108基独立性/常数theta矩阵证明，非仅coset支持。**λ^−1J(λu,λv)=Θε(v,u)**保交换轴/Gaussian/相位；原Π4变t轴、L²变z轴，lift Lz³Lt²与w_d→w_(−d)保同h。完整首p矩形整；其source须保bulk [𝒟,Lz]=−wp∂t−6Dζ+(3X0/2)t及Π shift。原边界首导数(B/6)γ_(p−1)(z)G″(t)被Π4杀；指定critical Π4Lz²𝒟^kR在k≤7全零，k8仅两端且g2/h2准确单位（89被mod9排），不是R995 D³Z/原critical单位。旧UH/MH曲率不重登；root/audit全文独审。

## O2：原完整trace及高坐标单位

R955/R970整个原CM packet为Cartier nilpotent单链，L=dim包=rank level9高权p−1/p−7完整classical Hecke模；**原S≠0 iff L1 iff完整η_f单位 iff准确TU adjoint值单位**。保Γ6/Γ036整格、det返回、σ⁻¹T_p和2/3 type，无两Weil增倍；坏链是真非CM congruence。

R958 r2原moment S^p=−216c_momℓ(R_F)，R_F=−2D^(2N+1)β²C^p，目标moment仍开。R960/965真实Igusa因子h=L+1，κ=(1/p)[x^((p²−1)/3)]a^(2p+2)=36α=−g_pT=−g_pS^p/432，g_p=48[x^(m+1)]a²单位。**不能把该因子换成固定CM椭圆源height2**；链顶单位不推链底。

R972–985的完整ring-class/AH/Robert/normalized Δ/strict LT源与全部尺度见最新H归档及各结果：原χ faithful、两HT条件互补，global unit线γ0单位、S非零 iffγ1非零，cσ不换两线。fixed7真实生成元与半norm、ϖ=ηX相位保；高pure/低pure属不同mirror，低unit不能搬给高。R975原整heat给所有n<p的c_n整但近p单位未证；R974 TU原period不反除。R973/R983四点完整核只消费；R982/983只排指定共同α/ξ及factorial模型。R984/985真一次Frob整余项及strict除p carry−3T^(p+6)/7不能删。

R986/987真global rational LT与Poincare两open源：𝒯=Z+β^-1J_s^p、误差首q−3，R594/R658旧formal分解不重登；gluing给C(xZ^jω)=β^(1−j)j!L_jω，pL_p=−βZ。第二Frob有限取消/曲率−βW不推near-p单位；完整公式和来源保最新H归档。

[R988](results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md)：完整Cartier与真正theta对称给 **G_(j(p−1))=−j!β^−j c_j+，1≤j≤p−2**；原r2/8、n=p−r有G_high=−β^(r−1)c_n+/(r−1)!、G_highstar=β^r c_n+/r!。原AH高坐标 **γ1=−24η^(−(m−b))(χσ−1)β^(r−1)c_n+/r!**，所有外因子单位、c_n+=−c_n−，故 **原S≠0 iff c_(p−r)±单位 iff F_(p−r)(0,−864)非零**，补成R974逆向而不反除period比。实际p-basis b0=−βB_(p−1)、b6=−β7 B_(p−7)/6!，参数差首影响q−3完整保。低a3/9 pure显式−β−3、−8β−9/35只校准已知unit；真正near-p系数全p单位、同h与height仍开。

[R990](results/R990-original-hypergeometric-fixed-r-coefficient.md)：原(E,X,Y)=(0,0,864)的三Ramanujan ODE逐式匹配 A=2F1(1/12,7/12;2/3;z)、B=2F1(5/12,11/12;4/3;z)，T=−uB/(24A)、z=u³/432。m=(p−r)/3、k=floor(p/12)时B真截成degree k Jacobi多项式；H=((1−z)B²)^−1、f_i=H_i/(1−3i)、Q=4+12zB′/B−z/(1−z)，**c_(p−r)+=(-32)^m(r−1)! [z^m]Qf^−r/4**。全分母在m<ℓ=(p+1)/3内单位，固定r2/8给O(M(p))、O(p)内存。B根/三个cusp极部准确、首resonance Hℓ=B(1)^−2单位；不能跨ℓ反除，目标系数非零仍开。

## 当前实际工作：两新窗口完成后继续一般非零

R991已完整认证R989旧r8差集349点（1000..20000），原三路/全hash见回执与H归档；不重跑。

[R994](results/R994-certified-original-combined-windows-through-200000.md)：R993公开run44760218207/job136370438703/source248592d7fabd01b1b8c548237400767e9ecec001已成功，531.337922156s且final预算真/exit0。新r8的20000..200000共2622点（20021..199877），新r2的100000..200000共1386点（100019..199967），总4008全非零/无尾段；各行首两点20021/20117/100019/100103原三路一致、完整wp ODE及全部首resonance核过。root纯IO逐块重组8段contract/7段summary，核全部sources/列表/rows/flags；payload2865567B SHA e764dff838bb24b18c8fec7f7634c2044f403e59e23a349cc00d0554c000dc8d。R988给这两个有限集原S单位，不推全p/同h/height；current R993 request完成，禁止重触发。method c1913358/script2e60046f及全部pins在回执，无raw artifact。

继续R995实际filtered关系；R996已证5∤p+1整族原V非零，继续5|p+1与actual G作用；R997已证完整原源/边界深度，继续Tε真实bulk。R998已冻结新j1尖点exact核：method ec9edd29/script b4a76a3d，30s/全试除/双有理通道；现提交公开请求，无prime窗口，R999待回执；O2残数/period defect非退化仍开。主目标OPEN。

## 继承任务与永久边界

[open](open.md)、[结果索引](results.md)与[H归档](handoff-archive-2026-11-20-before-rational-LT-jet.md)保全部来源/run/hash。R963允许r2的1000<p≤1e5全部1582点无零、R967κ/g_p尺度、R969/R973均已完只消费。R944/947/950低GM单位、R946/951/952 whole Bol/两个radical、R956紧支coker/λ尺度、R962 r8左项零与α8式已成；whole饱和须全𝒰包零，R953高Hasse不换低极部，R961链顶非链底。

O3–O6见open/归档。原J_h两CM权、det/Igusa/fullNorm/ζ²、a_h/normal顶项和全j平方比保；R913两权非O1评价权。R948 Abel盘零仅中心，不排非零MW像/证height。

固定Y的R805–930全部W/两图/jets/7K trace/五Z两权/30连接/Artin迹只消费，λ0=1/首项比非height。R907四必要artifact真404，待原字节，不以摘要代数组。五672铅笔/九NormΦ/端点格未成；Φ=QZ/qχ正乘、DN先−dlogQN再Gal7、254极阶/U272/两t/dual7保全。真正Rcal I_Z³、YP/FM128/634、508rank507、P1 c/a、σ/cY/eη/d/N/full nonp/Poincare/splitting/height仍开。R870须真实合法niPiξj非零；YL1零非rank0，UE=dY+2period、End⁰G=F/torus≥g+1、μ3qφ*=0均不删Y。

R317仅完整Nns、p2/5mod9、a³+db³=1/p|b，D/bc无界。R707固定41全129盘/8CM不外推；R575正CM根号−、逆twist秩零撤回、R706 h1零保留。非挠/log/rank/低单位/深盘数非height。旧失败/空artifact/已成Hurwitz block曲率/p²无新约束不重做；budget false FINAL不构成负结论。主目标仍OPEN。
