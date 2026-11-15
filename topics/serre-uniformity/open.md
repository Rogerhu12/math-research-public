# 未解决的问题

**R575现行更正。** 实际六层的正CM角色为Ψθκ4，根号−1、中心值零；R348把相反扭向Ψθκ4^-1识别为实际商的论断撤回。后文及历史归档中的该出现性、实际秩零与有理点零像应用均以[R575](results/R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)为准。固定家族的L值与局部代数计算仅按各自假设保留。

## O1：主要目标（OPEN）

证明绝对常数C，使所有无CM的E/Q、所有p>C的模p表示满射；或构造p→∞的完整反例族。等价的主要剩余情形是完整非分裂Cartan正规化子，不再以已由Furio–Lombardo排除的指数3子群为主目标。单p、有限层、条件结果与导子下界均不满足完成标准。

2026-11-13压缩前的完整开放问题、已关闭支路、全部公式和文献边界逐字归档于 [前版open](notes/2026-11-13-open-before-first-canonical-disk.md)。以下保留当前可执行缺口；归档不撤销任何已证结论或限制。

## O2：完整正规化子的高度与有理点

R4排除通常Runge捷径：所有含−I子群覆盖及继续扩域，最小提升域的尖点轨道数恰等无穷位数。须有新的全局信息。R101/R109独立完成p41/47/59/83的全部尖点约化/实分支及169候选，四层有理整j仅CM；一般层与非整j仍开。不能调用有gap的BBM全p≤97分类；公开代码审计不能冒认原gap原因。

## O3：实际Frobenius的统一小素数

真正所缺：为实际异常族找到q<p²/4、商二次特征ε(q)=−1且a_q(E)≠0。R2/3/6/7说明任意固定有限窗口仍可由满像曲线实现；R41/52的正密度依赖导子，不能代替首素数上界。R15/20/119给商域互反及分歧q≡1mod4时q≥p²+4，仍无判别式上界。历史见notes/2026-11-12-open-local-frobenius-history.md。

## O4：二次自扭曲、真实三次角色与共同导子

完整原公式与已关闭小层保留于[before-R753](notes/2026-11-14-open-before-R753.md)。R5商域虚二次、p惰性；统一排除非平凡二次自扭曲的p挠点同构仍等价主目标，Frey–Mazur不能作已证输入。R58/61–67及R317保严格小惯性I_p=C³、p≡2,5mod9；实际三次导子M=Dc²与共同bc均不可自由改变。h3/6/9/12的已闭分支不重开，一般共同中心零及h≥15仍可能。

R236/238/249已给同一实际谱与CM Hilbert诱导的有限商接口；统一有效条件是p≥C_ε(M*)^(1+ε)/h(bc)⇒j(E)整，M*=D(bc)²，有效系数2592。R229/232/233/245给支撑与导子的下界，不能反用为上界；Siegel平方根化简无效。八个hK1且K≠−3的bc指数1.5969787214，K=−3非平凡σ迫b≳p^(2√e)，仍不控制剩余K=−3、σ=1。继续整j真实三次角色联合检测与变化D,b,c的统一上方控制；固定有限Fourier投影或张量不自动共同非零，q=5^203、ell811的真实共同零边界仍须遵守。

## O5：固定层41已完整分类；一般层仍开放

[R707](results/R707-complete-level41-rational-point-classification.md)已从现存完整原证明和公开R709结果重建全部129盘：19普通=16排除+3CM，110超奇异=105排除+5CM。$X_{\mathrm{ns}}^+(41)(\mathbb Q)$恰为八个CM点，判别式−3、−7、−11、−12、−19、−27、−28、−67，无有理尖点。每个保留点的精确j、真实level盘、坏标签、简单根唯一性均完整连接；不依赖遗失R583摘要。

此固定p41子问题关闭；[129行来源账本](notes/R707-all129-disk-ledger.json)和[105盘执行表](notes/p41-SS-disk-progress.md)保存全部索引，原长链/Norm/连接/全尾无需重跑。一般层仍须真实秩受控商、实际全局高度和统一排除，不能从一个有限层外推绝对一致性。此前完整执行状态保全于[分类前open](notes/2026-11-14-open-before-R707-classification.md)。

## O6：固定CM参考及真实高阶障碍

完整三族方程、条件和旧开放项保留于[before-R753](notes/2026-11-14-open-before-R753.md)。固定A:y²=x³−x的三族原始X³−27W²=cZ^p保全互素/奇偶限制；p≡1mod4已排，现余p≡3mod4、g=1/3及变化大3mod4因子。九次幂、49|g、387bit旧R53已关闭不重开；固定m≥7的有限B_m不统一控制变化m，立方不自动升九级。实际惰性Weil扭曲正维商中心L值为零，无秩零捷径；分母与满支撑不可省。

R161/163严格Selmer为零与Robert对偶线仍容许局部S_q零或多支撑相消，须连接实际曲线额外关系。变化CM参考不能套固定A论证；整j时Hasse元素Norm自动，不添独立类群矛盾。原p43、776bitq已Gaussian5排除，非Serre反例；其ordinary见证必须在真实上域，真K子域乘积/43次幂和小11次角色均不能代χ±1。R715以后原整格/Norm与后阶障碍按下文继续，实际b/J/σ₂仍未知。

## 当前执行与精确缺口

全部旧公式、已成输入source/run/SHA与闭路逐字保于[双probe前open](notes/2026-11-15-open-before-projective-two-probe.md)，内接原R820等归档。下述为当前可执行缺口；不重算已成阶段，不把算法存在写成实际数值。

### 原规范高度与真正全p排除

R575真正正商是Ψθκ4、根号负，旧相反扭向秩零应用撤回。R616/R726已给全部充分大允许p的原β非挠、rank=dim、原log同构；R719/R722真实有限迹和完整尾已成，不再加因子数前提。复非消失不代同标签模p单位或高度排零。

R593/R596保原η_h、χ、μ3 tensor与清分母；R690/694/696实际坏靶Ω={0}。R724完整保原MW/第二类周期、Hecke轨道、因子2、Poincaré/universal extension、非p项、规范平方线丛刚性化和全尾，不假设高度矩阵可逆。真正缺原β/η、规范高度jets与(724.33)有限Bézout及其对全p存在。R785 Rosati压缩保CM值和切向两列，实正定不代p进非零。[高度符号核对](notes/2026-11-15-depth-two-symbol-and-original-height-leading-class-audit.md)明确R634已给逐盘非恒零；原D2深度符号不决定c1二阶系数，真正T_p保留第二类周期/原d_i与两Θ列，未新增非零结论。[Poincaré/period审计](notes/2026-11-15-original-height-Poincare-linearization-and-period-determinant-audit.md)进一步核：真实Q点β上保全部非p项，U_i=c(a_iV_i−A_iL_i)线性化；原Picard与ℓ的同一第二类修正在整条局部函数/全部jets准确相消，保实际纤维零阶、M/Norm/C_h及全部刚性化。T_p仍为三列(a_i,L_i,U_i−L_iP_i)秩条件，清Picard分母后为次数d_Y+2的指定period多项式；线性AST不排此式。原Y对合只减少中心列，不给η不变。该笔记§5.1进一步从真实字符格类映射证明：共同群G任何非零torus商必须保整个A、维数≥g+1，且End⁰(G)=F；几何E0^g分解和代数分裂幂等元不提供承载原稠密点的低维torus商，未获得新的six-exponentials非零结论。R730/R742/R744全尾和Weierstrass接口已成；深度4/5/6实际根与原高度未得。

**R823一般p原c1评价强化已证**：[原Hom不分歧](results/R823-original-primitive-Hom-CM-nonramification.md)。在原M2,1≠0时，K有理c1与局部s=a−1使评价核在R819原域作用下稳定，实际Hom拉回基给非零评价，故全部非零实际primitive L-Hom在c1不分歧；R729给充分大允许p前提。保J_h=c_h M2,h s/16+…、原β常数及c0归一化；共同m=1已是R729结论，不重做。未给单位/深度4或高度外积精确阶。

### 原p41函数与高度输入

R735/R738/R745原模型、4920陪集/800闭链/六Hodge、R754 period/Hom、R759完整Z格rank12/O_K6均已成。原b=r0⁶、L/K7、M/L40、αs/CRT6逆/ζ²一次/246、c1=4424/c0[2876,2822,2823]必须保持。Y genus127；R764全格cusps/c0映O，R769低degree≤693完整分支关闭。单p41工作服务真实高度输入，不重开R707分类。

已成且禁止重算：R774共同56Hodge三积，R775 M2/M6/M12及普通power1..6配方，R781原f4的R0..142与κ幂，R786原power1..5 q0..128，R790原146个M2的CM值/首粗导，R791原Hom/实下降，R794五维低次数η基，R795原1506个V6 q0..81，R796原CM的144条全局二次关系及length2，R798真实1506选行minor和690个τ³V3积。具体真实来源、耗时与输出SHA保各certified结果和上述归档。

**R787真实430位BudgetStop后立即续算**：run43708449812/sourceac5998f3完整430位，最新60765868B/SHA00855d88及430条历史由小IO43737168117实读。新run43737413555/job132883028161/source4092d1cc已进行，同core93d3d72b/wrapper42157e0d恢复新manifest1b92c4e5/1262条和原14分支，不回退259、不换R802。详见[430位断点](notes/R787-430-digit-checkpoint-and-same-core-continuation.md)，当前无真实A/B。

**原430位数域共同分母提取（方法已证，首轮有限候选未成）**：[projective契约](notes/R787-original-projective-reconstruction-method.md)9a75fd87保原1186方向、同整阶D/free/Z/129×280准确式与B非零出口，去内容后D/e。run43745966802/source d71d40bb/core e0a5ad95/wrapper b2c4efda在71.023573757秒后exit2，候选队列耗尽而非节点预算，准确验算0阶；全部manifest及1380输入SHA通过。artifact14173922406/189847233B/ZIP37d11e283，真实pins和语义见[首轮结束记录](notes/R787-projective-first-ended-search.md)。纯IO run43747260495已核实际5根均在C0、全部5×28短行仅因D_bound被筛，K为59位；准确manifest422319cd，节点队列已空。充分唯一性界非最终准确式必要条件；改不同同时坐标候选，不重跑旧格或盲增节点，仍无A/B。原Dixon同核续算继续，后继关系消费者未激活。 新[42维双probe方法](notes/R787-original-projective-two-probe-reconstruction-method.md)17c89271/core73bac3a2/wrapperfe276ba3已激活首(C0,C1)/42候选/一格；直接原lift求D，保全部短行，不用充分唯一性高度硬筛，仍原free/Z/129×280唯一成功出口。失败大payload在完整准确拒绝与SHA回执后退役，当前/成功保全；不重做旧28格。

**R809六原C已准确完成**：[实际结果](results/R809-certified-original-six-Hodge-normal-vectors.md)，run43712427063/source91fbd81e，84Q右端/full1380、S5=1234、p1000000007/minor29693114；13341.116785255秒，各最高项零给权4。原冻结verify全部成功；小IO run43733430148仅精读16件4.80MB取得真实manifest/cert/S5/minor，不重算旧行。保82^10、b/s与λ一次；A/B仍待真关系后追加，极理想/eta/高度未得。

**R792/R804待真实准确关系**：原R792 core7b7a5483/wrappercdac2e93保c(f)=−ζ²f、原Fb唯一立方根/21次奇因子，不选同源核前像。[真R824关系入口](notes/R824-original-exact-relation-adapter-to-beta-consumers.md)adapter5a6a100a/corea8a33d32/runner8991eb80已保存pending：任一完成新五次exact及17个129×280块给同原y，不等1186、不造R787、不重插denominator/content；新共同零实际判断。R804现core d8d1a395/wrapper1be08ad8按[双来源接口](notes/R804-original-CM-point-consumer-interface.md)分别消费真R792旧/新point字段；原8节点/例外点/T7/Gal/rho/vβ数学逐字未改。R824后[R809 A/B-only](notes/R809-original-A-B-normal-consumer-from-R824-method.md)corecdc381fc/runner eaf91a35已核pending，只复用原S5和p007逆求28Q/full1380，不重算六C；当前仍无新实际A/B。

**已成原输入禁止重算**：R797/799/800与R801长尾、R803 M6混合比、R805正规整基、R807一次清极均完整IO认证；真实run/source/SHA保各certified结果与R820前归档。原θ=e0−112648621e1/282292255+223442698e2/282292255、λ3/4零；旧power2..5至195已齐。R806原w0=e2/n1乘法34×8列/full820与cyclic已准确认证，R813原g/h两S3各432位/full820/scale6724已准确认证，451ZIP/726输入及冻结verify全核。后继直接消费，不再重复旧前缀。V8 q196..201只在真实选中需要它的消费者时补；κ^N每函数一次。

**R811真实乘法待A/B**：[R824入口](notes/R811-original-R824-normal-input-consumer-method.md)core9760b10a/runnerd56f069a与原ec100a76/64f9bc9a均pending；未有真AB不激活。原基/849bca27不改，全first-column/commutator、两图t⁵、完整unimodular核/HNF与双向Laurent保留；原P及τ全长+σ局部长认证不可省。generic run仅算法证据，不能代原模型；Norm/η刚性化常数不因首一化丢掉。完整契约与来源见本次open归档。

**R822完整极格的充分认证已证**：[全局余长度](results/R822-original-polar-lattices-certified-by-global-colength.md)。候选只需底环子格，完整原MAH=MBW给包含，双向Laurent使两图拼接；真实τ degdet＋σ在0的orddet与独立R791 deg(y)=1206相等后才给全部原极理想。有限域可用原b多项式的全部实际因子与ζ两root计算candidate，按全14原坐标CRT并公平推进真实profiles，最终全char0式/两图/长度必须通过；未知次数/系数不得由1206预填。仍未有原A/B或极格输出，完整char0 transcript保为另一个正确方案。

**R824小权完整极模入口已证**：[原齐次生成与纤维认证](results/R824-original-pole-module-generators-in-weights-five-to-seven.md)。Koszul及RR给M≤4=0、dimM6=300/M7=572；r=dimM5未知，完整自由生成数r/300−2r/r−28、权5/6/7，共272且权和1604。候选只需原完整Laurent129/142/156等式和V7中的真实1778纤维minor，包含＋全长1206认证全极模，不等大MA/MB或首轮normal换基。旧R781 R0..142/H³[129,161)直接复用；只有真需权7才新R143..155/κ156。[旧原非零minor已全源核完](results/R824-certified-original-pole-module-splitting-from-Schur-minor.md)：ell1000000753/branch0，1186det296007862及原20/1234消元minor非零，准确迫r28、28权5＋244权6、无权7。补旧R781 R130..142来源，不新生成尾；原A/B及全272候选仍未得，不改运行core。

**R815原Mg/Γ真实425素数后同核续算**：原run43719622321/source2a3300a9因BudgetStop退出；小IO run43747973677确认g完成425prime、last1000008791、模数12707bits，Γ未开始、无完整operator。manifest4e78095e/3464项，current561995095B/402379e2与425小receipt f136bee8准确匹配；[断点全pins](notes/R815-425-prime-checkpoint-and-same-core-continuation.md)。新原请求ac0870b2只增真实resume，不改80516ff9核心/ab725da0包装/849bca27框架、53源、prime007或原嵌套mode；恢复完整stage和唯一current，从425后继续。保持Mg六模/七准确点与Γ五模/七嵌套准确点、完整[[Γ,W]+MgW′,W]=0及两图因子，不另Mh。


**R787双probe首格实际结束**：[完整实际诊断](notes/R787-two-probe-first-lattice-ended-and-continuation.md)375414b2。run43748801736/894.401秒/42项全拒；小IO43750891953核manifest2a18a2f4/137项、queue2cf3e41f与全部42行。D全unit/8570或8571bits，m0由E0Z0构造强制通过、m1全首次非零。falseFINAL的orders0非逐项失败位置。当前pair1/pos0、余5对，预算尽而schedule未尽；先分析已保存42全基扩56及准确A约束，再激活对应真实消费者，不重算首格、不声称430不足。

**R815三维首prefix真实结束**：[完整诊断与第二列恒等式](notes/R815-projective-first-prefix-ended-and-known-columns.md)91a0456a。run43751142120/source5abcb9cc/core126469e2/wrapper3a0fa603，核心14.461秒/4pairs/28格/84行→58不同候选，全原early式准确拒绝。dg2738bits；重复6483bit D仅过z0[0,0]、z1失败，其余57首z0失败。IO43752277161核manifest1d55aec5/218项、scan87466ebc/next21/fails8，有限策略未尽。原We0=e1严格给Mg e1=Wvg，下一新消费者准确构造两列及最小共同分母、复用旧RR前缀，从21继续；原1652同余/weighted界/7点全式/cyclic与Γ不减。不把已拒D当真全局分母，也不据失败判425不足。

**R814完整降重数接口已证**：[原证明](results/R814-original-cusp-zero-ideal-and-exact-multiplicity-peeling.md)。全完成乘积内积分给C=im[Γ,Mg]恰约化20cusps；完整I的N=im[H,ΓH+MgH′]，P=(N:_R C)逐点max(m−1,0)，sqrtI=(I:_R P)，m0保留。六原E=20cusps+P0+3D，度1206/1485/1521/1602/1674/1728；第一剥后无cusp可省C商。实际原极I/Γ尚缺，η/height未成。

**R825原重数提取已证**：[原结果](results/R825-original-logarithmic-ratio-and-multiplicity-preimages.md)及[AB入口](notes/R825-original-R824-normal-input-consumer-method.md)coref09fae2b/runner43b00855保原89579f79算术、28字段与σ齐次项，仅pending。原E=21固定点+3D，r=y/δy给Jk=R∩(I_(3k+1)+rJ_(k+1))，只适原m0/1mod3；安全K395非实际。P=MaMb/Q=δa·b−a·δb及两图齐次项、272×816全核秩544必须全部投影，不用一般理想商或ambient迹；真实I/P/Q/D待。全SHA与详细公式见本次open归档。

**R820小有限代数入口已证且实际完成**：[完整实际结果](results/R820-certified-original-cusp-finite-algebra-and-ideals.md)run43721747750/source7890fde1、36.411901553秒；原两图rank20/colength20，292步/5380非monic，只有d271=20，600ZIP/598manifest/590stage/289输入全核。原273个S3 q0行/F20值/两锚点及Z^-eps规则保留，C直接供R814，不重算或等大导子。

### 全p sigma：同一个真正可见标签的三个单位

真正目标为同一primitive/Legendre可见h的N_h与两个Cartier量同时为单位；不能拼R734/R741/R737不同标签。R739真实p41/h37否定筛内逐项单位反射；固定有限窗不外推。R697/698原平方根、R782/R784全wedge/筛保持左逆、R788跨p六核与Schur只给结构，不排有限域相消。C13单位不能消N+1高带；D/D6闭包恰L(pO)，固定维闭合捷径关闭。

[Hurwitz刚性](notes/2026-11-15-sigma-Hurwitz-block-rigidity.md)给全部a_(p+n)=κn a_(n−1)，高块由首p×p唯一决定；升p²/Hirota不增独立信息。[Serre/Cartier](notes/2026-11-15-sigma-Serre-duality-and-Cartier-pairing.md)给真实有限Serre类与独立Cartier秩一单位C(x⁴ω)=(4/7)Bω，但权5为零时低极阶Cartier自动零，两者尚无桥。[cosigma闭合](notes/2026-11-15-sigma-cosigma-descent-and-closed-critical-channel.md)保半周期常数、degree3平移截面、rank4核；x²σ⁶整行列消失，总阶p−6未筛全零仍等价原F/G，不产生新非零。

[原模参数heat连接与奇部可分平凡化](notes/2026-11-15-sigma-modular-heat-connection-and-odd-tame-trivialization.md)已证明：保原c=0，六截面在模参数heat下准确闭合，但a=0非L稳定。辅助E27上奇连接显式代数水平基在全部允许p≥41零曲率；首p截断严格保Hasse边界源，原A(P0)=0、DA(P0)=B，逆水平矩阵的源两分量为单位。[原首p oscillator](notes/2026-11-15-sigma-first-p-oscillator-curvature-and-Hasse-source.md)已严格求得A''=−XA/4、全局Cartier(A⁻²ω)=ω和(D−O)^p=(A∂z+6DAz)²/12，P0上3B²z²。Lens变换仅在A非零函数域证明，正则算子延至P0；保原Hasse源及全部横向导数。把这些式子转成固定原F/G的critical、同primitive/Legendre支撑仍缺，未筛全零尚未排除。

[原全六有限heat连接](notes/2026-11-15-sigma-full-heat-tame-trivialization-and-even-source.md)已完整平凡化：偶部是Lamé5X/16与15X/4的张量，经det−108的明确矩阵精确同构；第二连接的平方根覆盖Wronskian²−27/4，全部允许p可分/零曲率。偶部首p源−z^(p−1)(AeH/6+DAeR/2)及完整原值基p曲率已保留，F/G均纳入同一覆盖。有限单位矩阵只保全向量非零，不保某个Taylor标签；真正缺口是源传播经原critical、primitive和Legendre投影后不能全消。

[原critical对角运输障碍](notes/2026-11-15-sigma-critical-projection-curvature-obstruction.md)已证：双变量完整曲率在P0为3B²(z²+t²)I8，原N维稀疏空间经R^(2N+6)的所有最大子式均为单位，核一维且满支撑。故在原W上无漏出的水平对角作用只能常数；真正primitive×Legendre权对全部允许p不恒定，不能有该水平延伸。非水平交换子与真正Cartan混合仍保留，不将抽象满支撑核当实际sigma向量。 已有源单位不能通过删除交换子直接变成筛后单位；继续真实非对角表示及原配对，不再寻找该已排除的对角延伸。

[五次水平lift/Legendre矩阵系数](notes/2026-11-15-sigma-horizontal-quintic-lift-and-Steinberg-coefficients.md)已证：Lz=A∂z+6DAz、Lt同式，Lz²Lt³水平且P0=(6B)^5z²t³，原h无溢出送至总阶p−1。真实O2旋转a²=2s/(s+1)的归一T̂=a^(1−p)T对角恰P_(h−1)(1/s)，原平方常数准确α₀s/6。全偶空间真字符ρ(q)=q^((p+1)/2)J_(√q)^−1在u/v基给q^−h；原z/t系数仍被非对角混合，原period/split向量及所需配对尚未识别，未证同标签非零。 全部原八通道和偶/奇Hasse源保留；源传播的真实字符投影尚未等同原同标签乘积，下一步必须完整原配对而非取旋转对角后冒认水平。

**R808（已证明）**：[原cuspidal Gram商与真实period/split/Howe链](results/R808-original-cuspidal-Gram-quotient-and-Howe-chain.md)。R727全部群元素的整Gram把原轨道格非退化约化商准确识别为Sym^(2r)det^(−r)，r=min(h−1,p−h)；原e0、Frob-Hermitian、Tζ平均像和N_h同时运输。位置Cartan与链内SL2严格区分，链中心规范与Hasse连接准确匹配；实际sigma原单项式仍经Kraw混合，同h配对非零未得。 原period/split有限商的识别已关闭；继续完整八通道源到原同标签Cartier量的真实配对，不重复有限norm识别。

**R810（已证明）**：[原toric完整单位偶矩与曲率链配对](results/R810-original-toric-unit-moments-and-curvature-chain-pairing.md)。原P_T exp(tE)P_T=P_r(1+2t²/3)P_T给全部(2j)!·binom(r,j)binom(r+j,j)/3^j单位；完整Hankel非退化，原toric线的E链和观测链均为基。K^p(P0)=3B²E的压缩高偶矩仍为单位，但P_T不水平、P_TKP_T零曲率，真实源方程必须保[ K,P_T ]v。实际u_h在Legendre零时不能归一，整链非退化不保证原指定系数；继续原z/t到同h的完整源配对，未筛与primitive/Legendre共同非零均仍OPEN。

**惰性Gaussian原源固定分解（已证明接口）**：[四个CM形式与八oldform](notes/2026-11-15-sigma-inert-Gaussian-rayclass-source.md)。原mod6 harmonic7准确分解为F3/F7(level36)和G1/G5(level144)、nebχ12；模6单位相位/π2与1/d原函数常数全部保留，八源矩阵是Z[ζ8,1/2]整基。原p11mod12 Hecke多项式T²+p⁷与U_pJ=−p⁵V_pJ给逐系数整性；由原U及Q正则得八个缩放原CM值的合法评价，真实FG=(c²/32)Σκνeν,p。尚无指定组合非零；固定八运输已由R826准确完成，不用标准七次Eichler积分或Frobenius斜率代值，不新增素数窗。Schütt Thm1.4已独立核全文。SHA c2855a43758242ad1dd2f1ff2f4375ada8a4e9bd36e3e72574b2854ee62a7e30。

**原unitary交叉heat与同h投影接口已证**：[完整笔记](notes/2026-11-15-sigma-unitary-cross-heat-and-primitive-source.md)173077d4。实际H/J/C三同源、完整36theta及full72整模型；原CM整段FG不换。∇=D−M−∂z∂t/6−3Xzt/2，双向Frobenius及两边/角点全保，P0曲率6B²zt。首p按整数差的原Legendre×primitive权W真正水平，∇^(p−1)(W Lz²Lt³R)指定FG/度p+1准确等于6⁶B⁷Σ原同h项；非零仍未知。μℓ仅有共同jet作用，不称原36全局稳定；原FG一次横向源为零，不能用全向量单位替它。旧R739反例仍有效。 这使用不同的实际极化家族，不重开旧6I family已排除的对角延伸；有限W不需完整几何test-vector标记，真正缺口收紧到该指定齐次源非零。§8.1证p=12k+11中央h=6k+7自动primitive，Legendre约化P_(p+1)/2=P_(p−3)/2及辅助j=2048/3；原j0的B单位不能替中央三单位。R829的p47中央乘积21已成，R706的p137147零在g_N而非g_k，不重复扫描。

### ordinary真实值与原全局对偶

原p43、776bit q已Gaussian5排除，不是Serre反例。R773/776/779/780原格/cochain/real/NT像已成，三个Norm/深度自动，不决定真实Robert值。R783原Θ=B−iA=13b、b=10Θ、Ω₂/ε=22−2Θ，坏值Θ=11；平衡jet Θ=−iKq，坏Kq=11i。[实际Shapiro笔记](notes/2026-11-15-original-Robert-Shapiro-second-class.md)337a9892从同一c_s构造Λ#受Σ支持类，p-localization单射逐层给唯一全局低阶gauge和K_glob；−iK_glob+(11i/2)u=d_R，q处完整杀零后唯一a_q满足Θ=i a_q。保原k-linear exact dual的共轭结构和二次restriction因子；q的局部θ-lift不自动给全局strict-p lift。另一侧同Σ支持的θ3 lift已由[exact-dual笔记](notes/2026-11-15-original-exact-dual-theta-lift-and-shifted-cup.md)7388c4be构造：原D0°消去第二障碍，首阶flat iff I0=0，strict-p还需b=0；不称完整晶体。实际原C4除T²后的q杯积为显式coboundary，互反只恢复R779的13bI0+26εb(18b+B_R+11/2)=0，b=0不除，不能重算作独立新方程。Θ数值仍缺。保Euler因子和一次交叉相位，不做巨大q挠点枚举；真K子域乘积/43次幂及小11次角色都不能代χ±1。

## 当前推进顺序与固定边界

完整此前执行/来源逐字保[本次open归档](notes/2026-11-15-open-before-R832.md)，内接全部原证明；当前run/source/断点以HANDOFF为准。

1. 原函数工程继续R827的真实q4两图充分检验、R824的准确27+244方向和R815完整Mg/Γ；R787旧430位BudgetStop已核，新run43737413555从438MB包同核续算中。原1234行/基/旧模分支不重算。R827尚无实际终止层，只有全τ多项式生成与σ∞rank272都过才能转移到char0。
2. 任一实际完成R824五次关系或原R787关系均可在真实来源绑定后给原y。已保存R824→R792入口；新共同零实际判断，后继CM点/R809 A,B正规向量/R811极理想/R825原D和eta依真输出接续。所有旧C0..5、曲率输入、基和算子来源保持不变。
3. 原全p sigma仍缺同一primitive h的Legendre及两Cartier单位。R812全split未筛单位、R829旧p47和16、R826固定八运输/R828两new零、R830 conductor-p权6lift都直接复用。R831完整EO交换代数已成：任意Weil交换子压回EO在old6上标量，不能再用其降FG/HJ。继续真实conductor-p与指定Eisenstein CM配对，不把同Hecke特征当实际同一test vector。
4. 原高度已得下列显式接触阶界，下一缺口仍是实际高度/周期与全尾的共同根证书。不能因知道一个有限截止阶，就任择高度常数或断言原整盘无非中心根。

**R832（新的显式统一接触阶界，已证明）**：[完整证明](results/R832-original-height-explicit-uniform-contact-order-bound.md)。在同一R616前提、原c1与真实外积上，选极阶≤2G第二类代表、R=21G+4的闭合系统，循环行Wronskian给ord Eij≤R−1+binom(R,2)(6G−4)，G=(p−1)²/4。它对任意真实常数组合成立，完整jet关系/原R716提取器可在该预定窗口内取得；不先求Ore算子，不假定T_p非零。界随p增长，无首项赋值或原p^4盘无根；较短已成jet/算子优先复用，不生成巨大新窗口。SHA a25f743c88d2048f969f001cb0e7d5784fe6e7078f7b61a6deed523264758dd2。

根会话独占main/共享索引，子代理只专属稿。所有新数学只用本公开Actions，已成raw不入Git/Release或悬挂blob；公开一日artifact仅当前续接。非快进立即真实pull/rebase循环推，不force；两README每次pull查diff，读过SHA在HANDOFF。主目标仍OPEN，继续推进，不以阶段报告收尾。

**R833原指定超奇异权六评价已精确识别**：[完整证明](results/R833-original-inert-supersingular-weight-six-and-quaternionic-evaluation.md)。同一原P0/微分/全tame level上Γν=β^(6−p)Cν^p，βhat(P0)=12B∈Fp*；原未筛和为(12B)^−5(−120c²/d0)^pΣκν^pΓν(P0)。old d^−6与全部共同相位保留，ε′(w)=ε(barw)^p按p mod24明确运输到R830权6特征。此SS函数全局存在并非指定CM值非零，也非任意JL向量；六项相消及同primitive/Legendre三单位仍真实开放。继续严格排tame M6同eigensystem、定位实际Serre-dual class与指定评价，不重做R830的同q级数filtration结论。

**R834原指定源全局非零及准确Serre-dual test form已证**：[完整证明](results/R834-original-inert-source-nonzero-and-Hecke-Serre-dual-evaluation.md)。纸面实际a5(F3)=307i√2、F7相反，307为7mod12素数，故允许惰性p两组原T5特征不同单位；各组d1首系数κ单位给原V非零，负权Hasse商排全SS恒零，原W=β^(6−p)V^p全局非零。惯性{6−p,6p−1}排整个tame M6同特征，Hecke primary connecting map是同构且δW≠0。原KS配对12Σvu/β；原P0 delta值B，经e转置唯一lift为真实cusp form uP0,e，原未筛和=(12B)^−5K^p〈δW,uP0,e〉。真正缺此指定配对非零；连uP0,e是否非零亦未证明，不把有限域Hermitian式当实正定，不删原primitive/Legendre同h。
