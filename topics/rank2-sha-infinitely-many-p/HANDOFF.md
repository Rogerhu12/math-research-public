# 交接

## 主目标、授权与规则

固定一条E/Q，完整证明rank≥2且无穷不同p的全Sha[p∞]有限。**未完成，继续研究；不以中间结果、时长或等待回复收尾。**
- 最近已读规则提交：95dd0ceef6cb70de1bf651394b992bc754f70ad5；2026-11-16 00:18:05 UTC核两README无变。实际CI pull 2026-11-15 23:51:29 UTC/9cf90ef5b006ff756939b6d883f8edc2365af57a（两README差异空）。本地末次成功2026-11-14 21:35:50/7aa38f25e；最近本地重试2026-11-16 00:18:05 UTC仍无环境。最迟2026-11-16 00:35 UTC再实际pull。
- 仅写Rogerhu12/math-research-public/main；旧库授权789d22af全文已读。完整结论立即推；拒推即pull --rebase/新head非强推重试至成功；不改他人历史，不保存或回显令牌。
- 根/题README blob为21bd547f56590b7f2dd279d0297efb289a9b2783、965ab236bbd6753acb812b45fcc36ae9b6f83b3c；root15@708f058a差异已读。每次实际pull核两README差异并记提交，至少每小时。
- 数学运行全公开Actions；可重算输出不入库/Release、不分新块，仅producer/args/run/hash。H<10KB，MD/API<100KB，open尽量<30KB，单文件<5MB，题≤200MB；题log每轮≤5行，不写根LOG。
- 最近盘点30,388,126B/2221文件，无超限，3旧真实输入块。[规则15来源](notes/2026-11-15-recomputable-output-provenance.md)保已删206输出、79未匹配/2自读/3旧块待核。

## 完整归档与当前分工

[本次压缩前全文](notes/2026-11-16-frontier-before-r841.md)、[完整open](notes/2026-11-16-open-before-r839.md)沿链保全部旧公式、十九角/ray、run/hash、撤回及未付门。压缩不撤条件。入口results.md、notes/PROOF-INDEX-R801-R850.md、open.md。
R1–363、365–560、562–653、655–711、713–841已登记；R364/R561/R654/R712和主目标仍开。旧未推R235/R237已重做。
root唯一metadata/ref写者，续R839实际Ceresa/canonical比较；deep续R840联合Serre左行/指定trace；theta续原共同多项式/第五Cartier伙伴；literature续原λ相容的实际曲线来源。R840/R841已付，下一编号R842由root协调；结论成即分别推。
实际pull23:51:29/run43777047575/job133005590314，两README blob不变、差异空；回执ci/rule-pull-20261115T235129.json，下一00:35前。R818/820/830成功run/source/args/hash见各证，不复跑；R830初版18/288误用已修。

## 唯一端点、原 CM 类与跨 p

R804/806/811/814只付同原λ的指定z/loc/AJ/I_j,-2非零等价；固定7/13 good pair、全Euler/period/基比见完整归档。R817仅7993三unit及固定cycle独立；R818仅复秩1，其他p/原三I线性和及全Sha7993仍开。R826最高λ在第四槽，Besser两项/U=pφ⁻¹/1+barπ/π²及LLZ germ保。
R829同q0全Chow零；R830相异q4*修复的2/3/17 test vectors、4/12尺度已付，R831全old矩阵[[0,0,Z],[0,0,0],[−Z,0,0]]只留唯一端点；X0/1次数6/12、遗忘1632/816和W4负号保。原AJ/global非零与R814比例仍开。
R832真Chow分解Mλ⊕L(Mγ⊕h1E17³⊕h1E17⁵)，原BFH/KL付全部mixed K点rank0。R841另以原三阶R:z↦z+1/3、q0/q2全交换及modified基点不变直接付Z纯λ；仅h1用忠实性，九项1/9角色提取保两个真实CM分量，degree3商X0(L)→X0(L/3)不当canonical比较。原6/12/1632/816保持、未增端点。[R839](results/R839-top-cm-translation-invariance-and-original-ceresa-expression.md)付Πtop全CH²平移不变，杀任意超椭圆像及真阿贝尔平移内曲线；原Z=Σc_rΠΦr*[X]=½Σc_rΠCer(Φr)，Φr来自真实Jacobian同态有限展开，原q0/q2全保。实际坐标/非零/R814比例仍开。

R838原完整critical块A_p=E[t]/t^e、exact=mM，t=Tℓ*取良好惰性ℓ*；dν=a1(t^(e−1)Pcrit Hν)读cohom商，三端点共用非零P_f,p,ℓ*，不预设e2。附录A保两项消元给Hν=4θ⁻¹g_j^[p](g_k−πVg_k)(Q⁴)，AJ=(E1β/Eβ)P dν；E1β=1−π⁻²，Eβ=(1+barπ/π²)(1+π⁻¹)²(1+barπ⁻¹)。全部4/X1/old尺度保；因子非零不预认单位，Pcrit随p读全尾，指定dν非零/R814比例仍开。

R838附录B付完整变权R=E[[τ]]、τ=Tℓ*、x=w=uτ^e，faithful a1双对偶保原full fiber；实际Hida输入Cν=bν/w′，lim eτ^(e−1)Cν=dν，原AJ=(E1β/Eβ)P乘此主极项。附录C付原R:τ_an↦τ_an+1/3及全Igusa层、E0整packet零、自扭τ↦−τ；e=2s_p、u/bν偶，实际输入反扭故Cν奇，余项O(τ²)。真实商v=τ²保Cbarν=2τCν及lim s_p v^(s_p−1)Cbarν=dν。未假noble/e2/第一支CM或ordinary；读数非零与canonical比例仍开。


## 四中央与三真长窗

原四来源S34/T72/U136/V66、rank2及原ray/Schwartz按完整归档。R816/820付E−11 rank≥2及通常全Selmer桥；R821原charge17/36/68/33、(4,−6,8,−6)、39carry/十二尾/末quartic保。R824同G0/charge40与k13行给r+2h≥s+1；R828同K1/C1完整d运输给bΘ=b+χ2B4z、βact=βΘ°+a_pΣvL，未认χ2落原像。
[全低核反射](notes/2026-11-15-original-first-diagonal-full-reversal-and-rh-convolution.md)：完整R_NH=3rNq_p(3)/8与反射已付；原四Θ^nP/H仍保全部卷积和伴随第二项，不能替bΘ或赋q_p(3)单位。
[有理分部边界](notes/2026-11-15-original-four-diagonals-rational-telescoping-boundary.md)：Legendre/域迹排−x代数primitive，Darboux/最高ζ项排原四同charge有理证书；仅特征零，不代原α非零，p依赖Frobenius仍开。
[固定torsion](notes/2026-11-15-fixed-torsion-connection-and-original-frobenius-initial-data.md)：固定M/Mumford倍率及全cocycle，Z_M严格平移不变、原G_M曲率−mH_M^p。P2,M保四α及Fermat修正，非零E[M]处ord≥p；CM13完整frame与裸迹首差(−γ−1)αS，Norm(γ+1)=21单位，不能赋差零。
[共同Cartier迹](notes/2026-11-15-fixed-torsion-connection-and-original-frobenius-initial-data.md)：交换连接代数普通迹零；实际αν=−Tr(M_fνD^(p−1))|q的非中心插入不可换幂。循环迹降至固定M²乘法矩阵Bν，原点同ανeO、charpoly T^(M²−1)(T−αν)。仍须同P2,M/四Rν的第五伙伴结构，不从固定载体/范数推出非零。
[原Cartier真极](notes/2026-11-15-fixed-torsion-connection-and-original-frobenius-initial-data.md)§13–16：每τ∈D_M的Z_M/G_M/P2,M真极阶p、p²−p−1、p³−p²+p+1。Cν的首极由D^(nν−1)Rν(τ)读，至少3M²−3nν+7点有极阶nν(p²−p+1)−1；各n互异，非零常数组合也真极。保同物理微分的固定tame覆盖/输出frame/exact消元不实现固定全纯Hasse–Witt块。任意输入乘h不在结论内；全球非零不代O处四α不同时零，CM13完整p依赖frame仍保。
R834原Γ4三真长窗T_M=s−r−13，h<T≤2h、T>2κ，全I=FH2+eH2单射，unit秩≥1+(7κ+3χ)/2；原同WD/qsrc/charge40/unit三角及39carry保。贴边h≥max(14,κ+7)，全核注入V_T=H0N³(−TP)再入原Z。
R836原3b<p及三长窗给K3≅kerΘ_T；D3全余核H3^0/F0H2^0、z_-≤2。实际V0先解A_T，同H2唯一实现V1，余F²H1；第三行c_F L(ψe3η)单射，第四短max(ell−r,0)读同G。forcing保w^(13+r)低行及同V/V1/L/G；旧全部q t^rFB族已排，实际余类/全WD/高位仍开。
[R840](results/R840-original-double-ramification-euler-image-and-unique-normal-tail.md)：原E²H3在2Z的全像仍ker res Z_-、余核z_-≤2，来源核FH2+e²H1。兼容(V0,V1)定唯一2Z值；H*=min(T,h+ell_eff)>κ，V2同此值及前缀f2−ηf3若存在则唯一。三曲线值全提升G2+cF³，同c由第三尾6e³η定；第四前min(ell_eff,T−h)已并入V2，余尾仍同G*。全联合Serre左行Q=H0(ωN⁻¹(H*P))、dim H*−(κ+χ)/2保2Z/P所有分支/导子；原trace保qsrc两Euler导数。仅同H3子格，实际forcing/全WD/高位仍开。
R837实权付原三长7q(H−r)≤3B_D²+56D、两长4q(H−r)≤3B_D²+32D，无截除/重数门；准确p界与十九角/13/39carry见原增补。自然三长临界余q1/2，旧47/8另有第三长才余q1；指定forcing未闭。

## 同 R mirror、真实 Euler 像与全边界

始终原M=c*U0 w13J、P134/charge40、13free/26carry、conductor10980、十九角、p²/p³及全部余列。T_J=s−r、T_M=s−r−13；同R*+Kval保全normal/两13/d₂，v_F=eξ非自由，改F提升须同步R。
R768强窗/q/H、R790真实Δ/p、R808同normal近远支保归档；b3/b4全排，b≥5与指定Schur仍开。
R813/R822同R的Xi=Omega/u^p，原点Res=γ/6 unit；IBP真GRes分子W_sFt²E²R/Y²。FH列给Trace_Z(W_sFtH)，光滑可非零/奇点总迹零；全式γ/6+G_F+B_F=0不可删边界。
[完整镜轴/十九角](notes/2026-11-15-original-global-euler-frames-and-complete-alpha-residue-pair.md)：真实ΔR=qsrc t^rFH、A=W_sFt qsrc t^r，Trace=−ResP(AH de/e)−全边界；2Aηde延拓iff杀全H1且唯一，只付α*两项相消。Y∞保全x^(3b+c) jet、3s>(3b+c)deg_tF才杀t1；Y0非固定已杀，r≤11保13尾。α*ω(B0)=ResP(B0ω/(2ηe))−〈D_EB0,ω|Z〉，同全局ω/ηordh与Gorenstein配对保。
R833全D_E像=ker res_Z_-，余核H2^0/F0H1^0，Z_-=C∩H_-长z_-=u−μd1−μ∞1≤2。核Φ(L,V)=[E_+⁻¹(eL)+V]_C，关系(2cF+L0,cF0²+F0L0)，V≤5列；同H1高前缀保。在核上α=[B0/(2ηe)]，normal L仍属原E_q像；不代真Bh/kerα满射。

## 其他完整未闭接口

R835互素导子根数−1障碍、坏位高度/BB/CG2原引用门、E17同Katz三方向及R834有限秩界完整保本次归档，均不外推原跨p。完整旧门见[全文归档](notes/2026-11-15-frontier-before-r837.md)及open：R815/819/823/825/827保同R指定Δ/p，R734/773–801普通同q深浅、R812同charge/Smith、R756/758预算177/47、R760三维Bost(0,3)、O4/O6/O7与R364/R561/R654/R712全开。AST/strict/fine不代全Selmer；子问题完成即续open。
