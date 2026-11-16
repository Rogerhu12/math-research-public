# 交接

## 主目标、授权与规则

固定一条E/Q，完整证明rank≥2且无穷不同p的全Sha[p∞]有限。**未完成，继续研究；不以中间结果、时长或等待回复收尾。**
- 最近已读规则提交：067aee2bc7fdf59f3411ec7bf206a59825cdb9da；2026-11-16 02:31:50 UTC核两README无变。实际CI pull 2026-11-16 02:16:33 UTC/0e06d735aa9b083b88db09fad54fa437fe3d0286（两README差异空）。本地末次成功2026-11-14 21:35:50/7aa38f25e；最近本地重试2026-11-16 02:08:54 UTC仍无环境。最迟2026-11-16 03:00 UTC再实际pull。
- 仅写Rogerhu12/math-research-public/main；旧库授权789d22af全文已读。完整结论立即推；拒推即pull --rebase/新head非强推重试至成功；不改他人历史，不保存或回显令牌。
- 根/题README blob为21bd547f56590b7f2dd279d0297efb289a9b2783、965ab236bbd6753acb812b45fcc36ae9b6f83b3c；root15@708f058a差异已读。每次实际pull核两README差异并记提交，至少每小时。
- 数学运行全公开Actions；可重算输出不入库/Release、不分新块，仅producer/args/run/hash。H<10KB，MD/API<100KB，open尽量<30KB，单文件<5MB，题≤200MB；题log每轮≤5行，不写根LOG。
- 最近盘点31,063,037B/2272文件，无超限，3旧真实输入块。[规则15来源](../notes/2026-11-15-recomputable-output-provenance.md)保已删206输出、79未匹配/2自读/3旧块待核。

## 完整检查点与当前分工

[压缩前完整H](../notes/2026-11-16-frontier-before-r851.md)、[完整open](../notes/2026-11-16-open-before-r848.md)沿链保所有旧公式/条件/来源，不撤任何未付门。入口results.md、notes/PROOF-INDEX-R851-R900.md（前卷沿链）、open.md。
R1–363、365–560、562–653、655–711、713–851已登记；R364/R561/R654/R712和主目标仍开。旧未推R235/R237已重做。root唯一metadata/ref写者；deep算R842指定[b0]/真三长限制，theta算全边界左核，literature算原CY与模纤维积/canonical对应，root核证明/实际曲线canonical比较。R851原Schoen映射/全部尺度已付；literature与root续非Dirichlet good-pair的实际canonical比较；下一独立编号R852由root协调。
实际CI pull 02:16:33/run43791155440/job133049634328成功，head 0e06d735，两README差异空。回执ci/rule-pull-20261116T021633.json，下一03:00前。R818/820/830来源保各证、不复跑；拒推即本地pull后新head非强推重试。

## 原端点、CM来源与实际曲线

R804/806/811/814原z=(1/30)prK twν(eηu∞)、固定7/13 good pair、三λ/34δ及全Euler/period保持；I_j,-2≠0 iff指定loc/AJ/z≠0。R817有限unit、R818复秩1不付无穷p。R831原唯一Z02=Z/Z20=−Z、X0的6^-2、X1的12^-2与1632/816不变。
[R839](../results/R839-top-cm-translation-invariance-and-original-ceresa-expression.md)的Π在全CH²平移不变，杀超椭圆/真阿贝尔平移像；原Z=ΣcΠΦ*X=½ΣcΠCerΦ保全实际Hom与次数，属三det≠1/Picard来源已排。[R841](../results/R841-original-cubic-normalizer-and-endpoint-chow-purity.md)付原R纯最高λ及全Hom平均/对称polarization Φ=(F,aq0,aq2)，S/W真实sign⊕std无常值，q4微分4倍保。
[R846](../results/R846-original-full-hom-and-genus-four-exclusion.md)完整Hom/真实reciprocal排原g4；R843–845条件几何保真但原g4不实现。[R847](../results/R847-original-dyadic-s3-and-genus-seven-lower-bound.md)准确C3×S3及完整分支轨道排g5/6，generating项g≥7。[R849](../results/R849-original-complete-cm-pool-and-genus-seven-kernels.md)完整θ(η^kψ0)、k0..17/全部old给R=ω²块ε⊕1^6、R=1块零。g7仅余sig(0,5,2;9,0)、JD∼E0³×T²、T signature(1,1)非E0²；或(2,3,2;3,0)、JD∼E0⁵×E²、E非E0；后者D/c属三étale、D/S3为j0，sign唯一level36 d17。两个不同商及非E0核不可删，未证剩余存在。
[R848](../results/R848-original-degree-eighteen-hecke-quotient-and-top-form.md)付原X/(C3×S3)=X0(867)、z6z degree18，显式目标商/原Ω的1/6和proper push18全见原证。[R850](../results/R850-original-smooth-cubic-quotient-and-exact-top-cycle-transport.md)付27个原Q点吹起后的光滑中央商Z、q degree3与q*ΩZ=b*ΩA。原Π=π3avgR、ΠZ=q*b*Πb*q*/3及α/β真Chow互逆，原Φ下降X0(3468)，αzΦ=3ΠZφZ*X̄，异常差已由投影付。
[R851](../results/R851-original-schoen-map-and-horizontal-cycle-transport.md)付同一Schoen函数域逆、E0³→W0(9) degree9、Z余degree3；全有理映射保17 Artin，准确F0*ΩW=−18ΩA。proper graph保Π_T/异常和source3；原每个有效曲线τ首项1/(2z1z2z3)，∞极阶≥6、下降≥2，所以主像水平。未将其字面认CM纤维，也未排Chow等价；原R814非Dirichlet good-pair的实际循环/period比较仍开。同H³或Chow动机同构不赋Chow rank1、AJ单射或跨p非零。

## 原完整 critical Hecke

R838完整critical代数A_p=E[t]/t^e、exact=mM及实际dν=a1(t^(e−1)Pcrit Hν)给AJ=(E1β/Eβ)P dν，全部Euler/period、X0/X1归一见原证/归档，不赋单位。实际R=E[[τ]]、x=uτ^e；Cν=bν/w′，lim eτ^(e−1)Cν=dν。全Igusa自扭τ↦−τ迫e=2s_p、u/b偶/C奇；商v=τ²、Cbar=2τC。主极项非零/canonical仍开，未假e2/第一支CM/ordinary。

## 四原中央与同一个Cartier模型

S34/T72/U136/V66、charge17/36/68/33、全部低卷积/39carry/十二尾/末quartic不变；R816/820付E−11 rank≥2及通常全Selmer桥。R824同G0给r+2h≥s+1；R828同K1/C1完整d运输bΘ=b+χ2B4z、βact=βΘ°+apΣvL，χ2落原像未付。低核反射/伴随第二项及Fermat修正全保，不赋q_p(3)单位。
[固定torsion原注](../notes/2026-11-15-fixed-torsion-connection-and-original-frobenius-initial-data.md) §§1–19保先固定M、真P2,M、CM13全frame和四真Rν。指定非中心trace原点为ανeO；Cν真p²极/全局非零不付原点非零。无exact的固定有限K(X)^pV已排，但p幂+exact真有fνω=hν^p dlogx+dvν，αν=(−2[z]hν)^p。C³返回固定帽；显式Δf保帽/高零/首前jet与C²/C³而首α加1，仅排这些数据自身决定首行，差不保P2^nRν/CM13。四首联合非零/第五伙伴仍开，完整条件及来源见原注/归档。

## 同R、原三真长窗与指定边界

始终M=c*U0w13J、P134/charge40、13free/26carry、conductor10980、十九角和全WD余列；T_M=s−r−13、T_J=s−r。同R高位/全部normal/两13/d₂不拆。
R834/836原H3三长核、D3/同H2及低行完整保；FH2+eH2单射和临界199κ/48不改全WD/Bost预算。R840 E²H3→2Z的像ker resZ_-、余核z_-≤2，兼容两值定2Z，H*>κ给V2唯一；全提升G2+cF³同c支付第三尾，第四已付前缀和余尾仍用同G*，forcing未付。R837全有限三长/两长预算分别7q(H−r)≤3B_D²+56D、4q(H−r)≤3B_D²+32D；自然47/12余q1/2，旧47/8另付第三长才余q1。各门、所有误差及原十九角/13/39carry见完整归档，不能省。
R813/822原ResP=γ/6单位及完整γ/6+G_F+B_F=0，GRes读W_sFt²E²R/Y²。R833全D_E像/余核不代高前缀受限像。α*两项、同全局ω、x^(3b+c)尾及r≤11十三尾全保原证与归档。
[R842](../results/R842-original-gres-double-ramification-transpose-and-joint-prefix-extension.md)的真框d∨H=Hf2−e(DH+(c−a)H)、原λ0/λ1、固定2Z补零、全Serre左端及仿射P值均保。全GRes消失须同ν/同ω0,ω1，不能独立补边界；对更小三长核仅充分。[第一层](../notes/2026-11-16-r842-first-layer-surjectivity-and-actual-restricted-class.md)已满射，剩余指定[b0]∈cokerL_T≅W_T∨仍未知。
[完整边界](../notes/2026-11-16-r842-actual-boundary-rows-and-horizontal-thickenings.md)保b0=−BF+同G的P补偿及D_R/Ξ代表差；十九角真Ft/Ftt、无穷权、所有ramification/conductor不省。t=1整纤维仅在3s>(3b+degYq+1)ord_1F_b，原充分门9s>(D+1)(M_D−r−deg_tQ)未免费满足；h7仅有限Y消去，保Y∞四步链。§11移动Y∞真trace/Newton保2Uτ/U与原J modP²；精度modx^J、J=N*+3+2ordRes(P,Px)，跨p全部W Frobenius项保。
[负水平全trace](../notes/2026-11-16-r842-complete-negative-fiber-trace-and-original-source.md)保原D_Q=(t−tQ)⊂Z、长ℓ≤b和全部奇点S=Tr(1/T_i′)，总D_-≤2b/H3满射；V_T需T+degD_-<2κ+χ，W_T未知。[Jacobian商](../notes/2026-11-16-r842-negative-fiber-jacobian-quotient.md)准确为A_Q/ann(Ft qtilde)，长max(0,ℓ−u−v)，最高系数−c_s tQ^rWQ s0(ℓ−u)²q_v单位；行零iff原乘积零，degH2 double-root长≤b−1。[全分歧转置](../notes/2026-11-16-r842-moving-horizontal-full-ramification-adjoint.md)仅未吹起moving且ftunit：d∨ν=e_Ug[w+ε(m−1)−εDx](../ν/g)，负rankm−1/核读约化值，正系数2b+1..3b单位。光滑/node区别、同ω补零及全部单位见原证/归档；固定十九角/奇点与实际Q'_T/W_T全局像未付，优先真正同ν左关系。

[全局同源mask](../notes/2026-11-16-r842-negative-fiber-global-mask-and-same-source-boundary.md)用degY N_Q≤b−1的真Θ_-支付整负移动行；底分母≤2，原正水平帽3b+1/底∞T^(3−2u_F)/十九角全保。W_T上[b0]=G_F，ω1的P项准确零；D_R−Θ_-仍保r≤11真尾（r2十项）。未称mask为Q_T截面，续同G全部边界联合。

## 其余未闭门

O4/O6/O7及R364/R561/R654/R712保完整open。E17 Katz同三方向二次项与有限矩不付无穷违反；不外推j0。R768/790/808同R强窗与Δ/p、R815/819/823/825/827、R734/773–801、R812同charge/Smith、R756/758预算177/47及R760三维Bost(0,3)全保归档。b3/b4排除不代b≥5。
AST/strict/fine不代通常全Selmer；有限p、复秩一、局部单位、条件高度或另一个cycle均不完成。子问题完成即续open，不因时长/阶段结果收尾。
