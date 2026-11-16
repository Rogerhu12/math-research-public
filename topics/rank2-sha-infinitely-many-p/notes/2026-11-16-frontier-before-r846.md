# 交接

## 主目标、授权与规则

固定一条E/Q，完整证明rank≥2且无穷不同p的全Sha[p∞]有限。**未完成，继续研究；不以中间结果、时长或等待回复收尾。**
- 最近已读规则提交：7ce65434aa245b51c4037d1a6b76f94d242427cc；2026-11-16 01:28:07 UTC核两README无变。实际CI pull 2026-11-16 01:05:15 UTC/ed489dd492f33fa2db74c969dd54fdd407322d06（两README差异空）。本地末次成功2026-11-14 21:35:50/7aa38f25e；最近本地重试2026-11-16 01:25:58 UTC仍无环境。最迟2026-11-16 01:50 UTC再实际pull。
- 仅写Rogerhu12/math-research-public/main；旧库授权789d22af全文已读。完整结论立即推；拒推即pull --rebase/新head非强推重试至成功；不改他人历史，不保存或回显令牌。
- 根/题README blob为21bd547f56590b7f2dd279d0297efb289a9b2783、965ab236bbd6753acb812b45fcc36ae9b6f83b3c；root15@708f058a差异已读。每次实际pull核两README差异并记提交，至少每小时。
- 数学运行全公开Actions；可重算输出不入库/Release、不分新块，仅producer/args/run/hash。H<10KB，MD/API<100KB，open尽量<30KB，单文件<5MB，题≤200MB；题log每轮≤5行，不写根LOG。
- 最近盘点30,729,195B/2245文件，无超限，3旧真实输入块。[规则15来源](../notes/2026-11-15-recomputable-output-provenance.md)保已删206输出、79未匹配/2自读/3旧块待核。

## 完整检查点与当前分工

[压缩前完整H](../notes/2026-11-16-frontier-before-r842-negative.md)、[完整open](../notes/2026-11-16-open-before-r839.md)沿链保所有旧公式/条件/来源，不撤任何未付门。入口results.md、notes/PROOF-INDEX-R801-R850.md、open.md。
R1–363、365–560、562–653、655–711、713–845已登记；R364/R561/R654/R712和主目标仍开。旧未推R235/R237已重做。root唯一metadata/ref写者；deep算R842指定[b0]/真三长限制，theta算全边界左核，literature算原genus4全Hom排除(R846)，root核证明/实际曲线canonical比较。R845显式2-torsion/2、4核已付；literature续R846原g4排除，下一独立编号R847由root协调。
实际CI pull 01:05:15/run43784143660/job133027873174成功，head ed489dd4，两README差异空。回执ci/rule-pull-20261116T010515.json，下一01:50前。R818/820/830来源保各证、不复跑；拒推即本地pull后新head非强推重试。

## 原端点、CM来源与实际曲线

R804/806/811/814原指定z=(1/30)prK twν(eηu∞)，全7/13 good pair、三角色/34δ、Euler/period保原证；I_j,-2≠0 iff指定loc/AJ/z≠0。R817有限unit、R818复秩1不付无穷p。R829同q0零；R830原q/q⁴局部向量已付。R831矩阵仅Z02=Z、Z20=−Z，X0系数6^-2、X1的12^-2及1632/816全保，不加端点。R832真Chow/mixed rank0、R841原R纯最高λ及degree3商/1/9提取均见原证；都不当canonical比较。
[R839](../results/R839-top-cm-translation-invariance-and-original-ceresa-expression.md)：Πtop全CH²平移不变，杀超椭圆/真阿贝尔平移内曲线。原Z=ΣcΠΦ*X=½ΣcΠCerΦ保全部实际Hom/次数。属三自同构det≠1以同源运输和Kimura零幂等杀最高像，故Picard y³=f4不可供应原最高λ；未假高CH实现忠实。
[R841](../results/R841-original-cubic-normalizer-and-endpoint-chow-purity.md)：whole g-packet Hom平均、双线性/最高swap负号/W4给原对称polarization(F,a q0,a q2)。S半平移给L=[[-1,0,0],[0,-1,-1],[0,0,1]]、q4微分4倍、det1。生成像g≥4；g4必D:y³=d x(x⁴+Ax²+B)，r signature(3,1)、s=(-x,-y)、JD∼E0⁴。全部有限系数/次数保。
[R843](../results/R843-actual-genus-four-quotient-and-cm-three-isogeny.md)：H=D/s为w²=z⁶−2Az³+A²−4B，规范Hμ:Y²=X⁶+μX³+1。真degree2商E±及α=q−,*r q+*满足α∨α=3；完整T=−27(μ+2)/(μ−2)与X0(3) j/Fricke729/T均付。
R843 A精确fiber product：z=y/x,U±=x±√b/x，两j0商U±²=z³−a±2√b，逆x=(U++U−)/2。V4 norm给JD→JH×𝓔+×𝓔− degree16，再JH→E+×E− degree4，总64；JD∼E0²×E+²，原JD∼E0⁴ iff E+为K-CM。V4最高三ω空间det均+；原全系数/推前次数不变。

[R844](../results/R844-original-genus-four-cm-order-seventeen-and-two-neighbors.md)：仍条件于原g4项。全Hom定义在Hη=H34/C18；τ=σ³对F为−1、对whole g Hom同ω，使D,r,s/原映射下降F3=K(∛17)，保y³=d x(x⁴+Ax²+B)真twist。Prym∼Bf×Bg的End角色仅1,1,ϑ,ϑ^-1（ϑ阶6）迫β=√B∈F3；两j0商c±=d⁴(−A±2β)，r=c+/c−的Kummer域H34、v_F3(r)=n与6互素。μ²=r+r^-1+2，v17(j±)=|n|/6非整数；CM主定理与degree≤6迫两整数order恰17，K(μ)=H17=K(17^1/6)，A²−4B∈17F3×²。三个真2邻点order34/j域H34；三同源为唯一horizontal3/阶2 Artin。未认原q/q4/canonical或非零g4存在。

[R845](../results/R845-original-two-torsion-field-and-cyclic-four-isogenies.md)：同E+的P_i=(ω^iρ+ω^-iρ^-1,0)，μ=−(ρ³+ρ^-3)，Fourier逆付L(E+[2])=L(ρ)。实际规范2同源φ_i、核C_i及微分倍率1齐付；φ_j φ_i∨在i≠j循环4、i=j为[2]，与原3同源的互素方块交换。原g4条件下ρ³=(A−2√B)/√Δ，Kρ=H34=H17(E+[2])。保原6/12/1632/816与全系数；原q/q4及canonical仍未认。

## 原完整 critical Hecke

R838完整critical代数A_p=E[t]/t^e、exact=mM及实际dν=a1(t^(e−1)Pcrit Hν)给AJ=(E1β/Eβ)P dν，全部Euler/period、X0/X1归一见原证/归档，不赋单位。实际R=E[[τ]]、x=uτ^e；Cν=bν/w′，lim eτ^(e−1)Cν=dν。全Igusa自扭τ↦−τ迫e=2s_p、u/b偶/C奇；商v=τ²、Cbar=2τC。主极项非零/canonical仍开，未假e2/第一支CM/ordinary。

## 四原中央与同一个Cartier模型

S34/T72/U136/V66、charge17/36/68/33、全部低卷积/39carry/十二尾/末quartic不变；R816/820付E−11 rank≥2及通常全Selmer桥。R824同G0给r+2h≥s+1；R828同K1/C1完整d运输bΘ=b+χ2B4z、βact=βΘ°+apΣvL，χ2落原像未付。低核反射/伴随第二项及Fermat修正全保，不赋q_p(3)单位。
[固定torsion原注](../notes/2026-11-15-fixed-torsion-connection-and-original-frobenius-initial-data.md) §§1–19保先固定M、真P2,M、CM13全frame和四真Rν。指定非中心trace原点为ανeO；Cν真p²极/全局非零不付原点非零。无exact的固定有限K(X)^pV已排，但p幂+exact真有fνω=hν^p dlogx+dvν，αν=(−2[z]hν)^p。C³返回固定帽；显式Δf保帽/高零/首前jet与C²/C³而首α加1，仅排这些数据自身决定首行，差不保P2^nRν/CM13。四首联合非零/第五伙伴仍开，完整条件及来源见原注/归档。

## 同R、原三真长窗与指定边界

始终M=c*U0w13J、P134/charge40、13free/26carry、conductor10980、十九角和全WD余列；T_M=s−r−13、T_J=s−r。同R高位/全部normal/两13/d₂不拆。
R834/836原H3三长核、D3/同H2及低行完整保；FH2+eH2单射和临界199κ/48不改全WD/Bost预算。R840 E²H3→2Z的像ker resZ_-、余核z_-≤2，兼容两值定2Z，H*>κ给V2唯一；全提升G2+cF³同c支付第三尾，第四已付前缀和余尾仍用同G*，forcing未付。R837全有限三长/两长预算分别7q(H−r)≤3B_D²+56D、4q(H−r)≤3B_D²+32D；自然47/12余q1/2，旧47/8另付第三长才余q1。各门、所有误差及原十九角/13/39carry见完整归档，不能省。
R813/822原ResP=γ/6单位及完整γ/6+G_F+B_F=0，GRes读W_sFt²E²R/Y²。R833全D_E像/余核不代高前缀受限像。α*两项、同全局ω、x^(3b+c)尾及r≤11十三尾全保原证与归档。
[R842](../results/R842-original-gres-double-ramification-transpose-and-joint-prefix-extension.md)：真框d∨H=Hf2−e(DH+(c−a)H)，十九角/两lift齐付；λ0=t^r(Eq)A_s、λ1=t^rqA_s保原密度/固定2Z补零，E²q按兼容关系合并。GRes|P_T=0 iff同ν、ω0/1∈Q_T满足λ0−d∨ν=resω0、λ1+eν=resω1；保全Serre左端，仿射值−ResP((j0ω0+j1ω1)/e²)。对更小三长核仅充分。
[第一层](../notes/2026-11-16-r842-first-layer-surjectivity-and-actual-restricted-class.md)：T>2κ使Q_T→(ωN⁻¹)|Z满射，先延拓λ1第一层、ν0唯一；剩余[b0]∈cokerL_T≅原W_T∨，L_T来自真Q'_T=H0(ωN⁻²(TP))。指定二层类/真三长核限制未知。
[实际边界](../notes/2026-11-16-r842-actual-boundary-rows-and-horizontal-thickenings.md)：同提升G_V给b0(V0)=−BF(qt^rG_V)+ResP(V1ω1/e²−Ξ_R)，全部ψ分支而非theta g轴。完整D_R=c_s ER{−d(WFt/e)+(W'Ft+WFtt)dt/e}与Ξ差保。q=Yqtilde时非固定Y0横截边界真为c_s t^rW Ft/FY·qtilde·V0（最多两点），旧FH消去不能搬来；Y∞保N*+m与N*两个jet。十九角原Ft/Ftt运输、无穷uF+4V及减1、全部ramification/conductor与同ω下降保。横截补零：Y0为w1∈(e),w0∈(e²)；Y∞为w1∈(e),w0+3bw1∈(e²)。尚未判全局[b0]非零或无解。

边界§9–10：同q t^rH3在3s>(3b+degYq+1)ord_1F_b时整t=1纤维残数消去；充分原门9s>(D+1)(M_D−r−deg_tQ)，未预付成立。原t^rF³q∈WD另迫h7纤维有限Y全消，保Y∞/四步链/移动正水平。均仅删B_D子块，B_F与P代表补偿逐字保留。

[负水平有限行](../notes/2026-11-16-r842-negative-horizontal-finite-euler-rows.md)：光滑Ftunit的Z_Q=k[x]/x^m上D3=Dx，指定残数=c_s tQ^r[x^(m−1)]A(Dx+1)²(qtilde·V0)，最高jet系数单位。光滑FYunit的二重水平切点全D_R残数零，奇点不外推。原degH2迫z_-=2及c=μd1；横截平方自由两根总边界是二次值商准确行(k1,k0−h1k1)。W_T的实际像未知，全部其它边界/同P补偿保。

## 其余未闭门

O4/O6/O7及R364/R561/R654/R712保完整open。E17 Katz同三方向二次项与有限矩不付无穷违反；不外推j0。R768/790/808同R强窗与Δ/p、R815/819/823/825/827、R734/773–801、R812同charge/Smith、R756/758预算177/47及R760三维Bost(0,3)全保归档。b3/b4排除不代b≥5。
AST/strict/fine不代通常全Selmer；有限p、复秩一、局部单位、条件高度或另一个cycle均不完成。子问题完成即续open，不因时长/阶段结果收尾。
