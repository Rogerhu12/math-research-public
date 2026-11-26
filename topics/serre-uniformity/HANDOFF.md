# Serre 一致性交接

## 目标、授权与维护

证明绝对C使所有无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，尚未达README标准。**

**维护会话：Astra-serre-24b8836b-20261126。** 2026-11-26接手；已部分克隆并真实pull main。前态逐字见[接手归档](handoff-archive-2026-11-26-before-resume.md)，旧来源/run/hash沿原归档链保留；不重做已成结论。

**已读公开规则提交：bd8cbb9d84c5ababd78a803ddbc1aea7a3a06a66**（2026-11-26 13:55 Asia/Taipei；终端断连后读取远端main并核两README无diff）。两README已读；每pull核diff记SHA，至少每小时pull。私库根规则已核36cf1ed2；QUEUE认领已推233f7479。

执行宿主现不可用；按根规矩8用GitHub小文本tree/commit及非强制ref更新继续，每次先读main核规则，拒绝即在新head重建，终端恢复后补pull --rebase。

根维护main/H/open/index/log；子研究仅写各自notes。每条结论完整证明后立即提交，push前pull --rebase；NFF立即重复，禁force。凭据只CLI。H<10KB、open<30KB、每MD<100KB、topic<200MB；不提交可重算raw，不写根LOG。已读log/最新notes；R1003只有旧H“准备中”文字，当前树无稿，不当已交付结果。

**范围纠错[R1003](results/R1003-global-scope-and-remaining-branches.md)**：R1只余完整Nns。p2/5mod9仅小惯性C³；R317另需整j、K=Q(√−3)、σ=1、小除法域同一。完整惯性/变化域等未排，导子下界不等于排除；O1/O2只是指定辅助源。

## O1：同一个原本原标签的三个因子非零

p=6N+5，h=6i+7，i+j=N−1，须同h使原primitive/Legendre mask下P_(h−1)(1/s)fi gj≠0。R949/954/957–959全失败 iff (1+24X)|原B_p(C,X)，X0=−1/24，fine额外阶3。R964逆CM族只控h_(i+2)；R966/968完整heat/Gaussian源给Z_i∈M_(p−5)，mark/E6^N=−72(-864)^−N fi gj。须实际filtered span含A/E4或mark functional非零。

R969三点actual span核已过；R971严格排全p full-span，未排特定A/E4包含。R945中央零与完整S单位并存，完整trace不推同h；R734原primitive Legendre单位已成不能独完O1。

[R992](results/R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md)：全M_(p−5)上G(F)=[D²(XF)+X²F/144]/[X²(1−z)]分母消去；Jacobi互异谱、各mark1、kernel=Tate A/E4。**原V≠0且G稳定⇒同h非零**。旧227 central global非零/mark零排逐列本征；E+ mark(25F−D³F)/144。全部源与谱见结果/归档。

[R995](results/R995-original-mixed-source-for-the-first-coarse-CM-normal-jet.md)：原Π4D³(∇²J)完整G‴/216、12uF′、F三支及全ζ修正已核，E−mark(25Z+Ψ)/144和首p整界保；新partner非旧g，尚无retained关系/G稳定。

[R996](results/R996-original-end-column-cusp-unit-and-filtered-space-nonzero.md)：完整norm-one Gaussian给Z_(p−7,1)尖点233/(p−7)!；233为8mod9排除。h=p−4 primitive iff5∤p+1，P4=19/9单位，故该整族V≠0。完整一般cusp保Π3、Gaussian、ζ和平方法及首p界；不假与Legendre相同，不推CM mark。

R997/R1000原ε-vector、交换轴、完整bulk及+8A边界已成；原mask杀全部自身边界迭代，低项48不能代同h。完整尺度与回执见[本轮H前态](handoff-archive-2026-11-26-before-R1004.md)。

[R1001](results/R1001-norm-seven-dual-Poincare-source-and-original-filtered-tensor.md)：真实norm7双Poincaré源在全部极部扣除后给−6Aα F⊗G，Norm Aα=16·19/7单位；完整critical卷积、首p整界和唯一p边界已证明。单balanced trace不代全乘积，高carry仍开。全部尺度与来源见结果及[前态归档](handoff-archive-2026-11-26-before-spectral-route.md)。

[R1002](results/R1002-ten-step-theta-companion-and-four-free-CM-jets.md)：真实W_(p−9)/η4=f权p−11，full Katz输入仍p−9，十步 L=T0…T−9=A^−1(A²D)^10A^−9，右6^−10A11XY。仅有限u至X11、∂u=1+O(X15)，不假完整charp primitive。J=<1,X³,X6,X9,X12>上rank1，kernel为A9u^e(e0/3/6/9)，特解c*X12单位；实际f的ord∈{0,3,6,9,12}且受global weight界。原末列(p−7)!Z=432D³f+75XDf−9Yf，mark/Y0^N=79R0−96R1；局部方程允许该值零或非零，不能代实际global归一。root/audit/literature全文独审，无执行。

## O2：原完整trace及高坐标单位

R955/R970整个原CM packet为Cartier nilpotent单链，L=dim包=rank level9高权p−1/p−7完整classical Hecke模；**原S≠0 iff L1 iff完整η_f单位 iff准确TU adjoint值单位**。保Γ6/Γ036整格、det返回、σ⁻¹T_p和2/3 type，无两Weil增倍；坏链是真非CM congruence。

R958 r2原moment S^p=−216c_momℓ(R_F)，R_F=−2D^(2N+1)β²C^p，目标moment仍开。R960/965真实Igusa因子h=L+1，κ=(1/p)[x^((p²−1)/3)]a^(2p+2)=36α=−g_pT=−g_pS^p/432，g_p=48[x^(m+1)]a²单位。**不能把该因子换成固定CM椭圆源height2**；链顶单位不推链底。

R972–985原ring-class/AH/Robert/normalizedΔ/strictLT所有源、相位和完整尺度在结果/归档。χ faithful、global-unit低γ0单位，高S≠0 iffγ1≠0；cσ不交换HT线。fixed7与半norm保，R975整性不推near-p单位；R974 period比不反除。R982/983指定共同α/ξ/factorial模型已否；R984/985实际除p carry−3T^(p+6)/7不可删。

R986/987真global rational LT与Poincare两open源：𝒯=Z+β^-1J_s^p、误差首q−3，R594/R658旧formal分解不重登；gluing给C(xZ^jω)=β^(1−j)j!L_jω，pL_p=−βZ。第二Frob有限取消/曲率−βW不推near-p单位；完整公式和来源保最新H归档。

[R988](results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md)：真Cartier给G_(j(p−1))=−j!β^−j c_j+（1≤j≤p−2），原n=p−r有G_high=−β^(r−1)c_n+/(r−1)!，γ1=−24η^(−(m−b))(χσ−1)β^(r−1)c_n+/r!。全部外因子单位，c+=−c−，故 **原S≠0 iff c_(p−r)±单位 iff F_(p−r)(0,−864)非零**；不反除period比。低pure单位/真实p-basis/参数差q−3见结果与归档，不代near-p单位。

[R990](results/R990-original-hypergeometric-fixed-r-coefficient.md)：原Ramanujan源A=2F1(1/12,7/12;2/3;z)、B=2F1(5/12,11/12;4/3;z)，T=−uB/(24A)、z=u³/432。m=(p−r)/3<ℓ=(p+1)/3，B为degree floor(p/12)真Jacobi多项式；H=((1−z)B²)^−1、f_i=H_i/(1−3i)、Q=4+12zB′/B−z/(1−z)，**c_(p−r)+=(-32)^m(r−1)![z^m]Qf^−r/4**。全分母单位、首resonance Hℓ=B(1)^−2单位，不可跨ℓ反除；完整ODE/roots/cusps与尺度保结果，目标系数非零仍开。

[R1005](results/R1005-finite-Gauss-companion-and-complete-resonance-defect.md)：原P截到d=ℓ−1，完整Wronskian=1−z^ℓC/B(1)²，P_d=−16/(7B(1)²)、C+3zC′=B、C(1)=B(1)²。原高系数准确[z^m]QB^r/P^r；所有P根留数仍须保，非零未证。

## 当前实际工作：两新窗口完成后继续一般非零

R991已完整认证R989旧r8差集349点（1000..20000），原三路/全hash见回执与H归档；不重跑。

[R994](results/R994-certified-original-combined-windows-through-200000.md)：run44760218207/job136370438703/source248592d7f成功531.337922156s。真正新r8 2622点、新r2 1386点共4008全非零/无尾；四新点原三路、完整wp ODE及各首resonance核过。root纯IO全回执核；payload2865567B SHA e764dff838bb24b18c8fec7f7634c2044f403e59e23a349cc00d0554c000dc8d。仅有限S单位；所有sources/rows/pins见结果与归档，已完不重跑。

继续R1001高carry与本轮norm3源/固定Eichler谱路线（尚为notes候选，旧R1003未交付稿不存在）；R1003编号已用于范围纠错。R1002局部四自由jet已成，继续原全局W/CM归一约束；55|p+1剩余V非零、G稳定、O2近p单位及真正height仍开，主目标OPEN。

## 全局后继

[R1004](results/R1004-exact-even-valuation-at-CM-cross-primes.md)：R320原分支p5mod12的CM交叉迹差有准确偶赋值；实际立方条件另给3|v，pⁿ同构迫q≥p^(4⌈n/2⌉)+56p^(2⌈n/2⌉)+676；q7mod12给4p^(2n)+27。n1/2界相同；该检测器不能给全局p²提升，a/c上界仍开。

## 继承任务与永久边界

[open](open.md)、[结果索引](results.md)与[H归档](handoff-archive-2026-11-20-before-rational-LT-jet.md)保全部来源/run/hash。R963允许r2的1000<p≤1e5全部1582点无零、R967κ/g_p尺度、R969/R973均已完只消费。R944/947/950低GM单位、R946/951/952 whole Bol/两个radical、R956紧支coker/λ尺度、R962 r8左项零与α8式已成；whole饱和须全𝒰包零，R953高Hasse不换低极部，R961链顶非链底。

O3–O6见open/归档。原J_h两CM权、det/Igusa/fullNorm/ζ²、a_h/normal顶项和全j平方比保；R913两权非O1评价权。R948 Abel盘零仅中心，不排非零MW像/证height。

固定Y的R805–930全部原W/两图/jets/7K trace/五Z/30连接/Artin迹只消费；R907四必要artifact真404，待原字节，不以摘要代数组、不重跑。五672铅笔/九NormΦ/真实Rcal I_Z³/YP-FM/endpoint格/P1 c-a仍开；σ/cY/eη/d-N/full nonp/Poincare/splitting/height不能删。全部254极阶/U272/双7/508rank507与符号尺度保open/归档；YL1零非rank0，UE=dY+2period及torus≥g+1保留。

R317只适用上述条件分支，D/bc无界。R707固定41全129盘/8CM不外推；R575正CM根号−、逆twist秩零撤回、R706 h1零保留。非挠/log/rank/低单位/深盘数非height。旧失败/空artifact/已成Hurwitz block曲率/p²无新约束不重做；budget false FINAL不构成负结论。主目标仍OPEN。
