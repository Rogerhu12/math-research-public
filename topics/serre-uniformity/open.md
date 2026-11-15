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

全部旧公式、已成输入的source/run/SHA、闭合路线和来源逐字存于[此次R801前open](notes/2026-11-15-open-before-R801.md)，内接此前归档。下述为当前可执行缺口；不重算已成阶段，不把算法存在写成实际数值。

### 原规范高度与真正全p排除

R575真正正商是Ψθκ4、根号负，旧相反扭向秩零应用撤回。R616/R726已给全部充分大允许p的原β非挠、rank=dim、原log同构；R719/R722真实有限迹和完整尾已成，不再加因子数前提。复非消失不代同标签模p单位或高度排零。

R593/R596保原η_h、χ、μ3 tensor与清分母；R690/694/696实际坏靶Ω={0}。R724完整保原MW/第二类周期、Hecke轨道、因子2、Poincaré/universal extension、非p项、规范平方线丛刚性化和全尾，不假设高度矩阵可逆。真正缺原β/η、规范高度jets与(724.33)有限Bézout及其对全p存在。R785 Rosati压缩保CM值和切向两列，实正定不代p进非零。R730/R742/R744全尾和Weierstrass接口已成；深度4/5/6实际根与原高度未得。

### 原p41函数与高度输入

R735/R738/R745原模型、4920陪集/800闭链/六Hodge、R754 period/Hom、R759完整Z格rank12/O_K6均已成。原b=r0⁶、L/K7、M/L40、αs/CRT6逆/ζ²一次/246、c1=4424/c0[2876,2822,2823]必须保持。Y genus127；R764全格cusps/c0映O，R769低degree≤693完整分支关闭。单p41工作服务真实高度输入，不重开R707分类。

已成且禁止重算：R774共同56Hodge三积，R775 M2/M6/M12及普通power1..6配方，R781原f4的R0..142与κ幂，R786原power1..5 q0..128，R790原146个M2的CM值/首粗导，R791原Hom/实下降，R794五维低次数η基，R795原1506个V6 q0..81，R796原CM的144条全局二次关系及length2，R798真实1506选行minor和690个τ³V3积。具体真实来源、耗时与输出SHA保各certified结果和上述归档。

**R787**：run43683912711/source eab5e58bbf951c48ccf13a109bbdf0b0289a6f23于11:06:48UTC实际BudgetStop，未有原完整A/B。原V5 1234列、129条件、14分支同主元同自由坐标，core93d3d72b不变；artifact14159006977为5,148,711,108B/32652fdb，manifest613f436b共1517项。同核续算run43708449812/sourceac5998f3已运行（wrapper42157e0d/request583e43be）：逐1517输出/1372原输入真SHA后恢复每prime最新完整Dixon及所有其它已成阶段、原输入包；原数学核/配置不变，不改用R802或预填kernel。结果仍只认真实非零A/B及全129×20准确代回。

**R797/R799/R800**：公开run43693453831/43695571499/43696070150已success，完整输出已由公开纯IO run43699442183核过；三者的准确实际结果均已登记，原回执/每项SHA可直接消费。分别为五条新映射170/172/176/193/196条件的原Laurent；原V6尾82..108和新V7/V8最小短基；146原M2尾129..195。R797最后清行另需各自κ^N，仅增一次乘法，不能多跑R_N。所有raw仅一日活跃artifact/bundle。

**R801（证明及实际长尾均已成）**：[原证明](results/R801-original-minimal-long-tails-and-exact-relation-interface.md)、[真实结果](results/R801-certified-original-power6-to8-long-tails.md)。run43701282817/source92961ce5，796.738575秒；V6[109,142)、V7[96,176)、V8[109,196)，原基/尺度不变。完整30,781输出/30,773stage、ZIP/5组bundle与冻结verify逻辑全核。实际依赖闭包将全部power2..5都补至195，故原方法提醒的七八铅笔V3至136/149缺口已关闭，不得重算。原6/7/8 Schur真秩d−20的实际minor、第二关系/690+e认证仍未执行；R787成功后第一六次关系直接τ(A,B)，五新κ^N各仅一次补乘。函数、极除子、η和高度仍未成。

R793保原V6 142条件、第二关系/rank1116及264维残余；固定degree272的Jacobian表示和主函数G=s/(fτ^(m−3))保全常数。R798只已得短坐标和锚点积，未得全乘法表或完整基逆。R796更高CM局部阶数只在实际R787分子分母共同零阶需要时追加，不先生成155/156全部jet。

**R792**证明和工程已成，唯一待R787真实producer。保c(f)=−ζ²f、y0=√−3v0及指定实嵌入Fb=Q(b)的唯一立方根；21次Q分解唯一奇因子与三次gcd。只求原β_C/真实vβ，不在未知有限核中选原A前像。原K上CM值/首jet先算再扩L；两个值与首导全零才消费更高jet。

**R802（已证明）**：[原半线性奇偶与七次字段](results/R802-original-semilinear-parity-and-degree-seven-relations.md)区分c0、σ−1与全局cY，原扭曲给q/v负号；原y奇阶在Fb(tξ)、偶阶在sFb(tξ)，κ固定，R_m带s^(m mod2)。原全球±截面掩码保82¹⁰，固定B与反固定A的非零关系可在七次Fb求解；七分支必须同自由归一，末端两真实右端恢复原1234基并全129×20认证。实际r±/minor/kernel尚未计算，当前不改R787。

**R803（已证明）**：[单原映射复用与694维混合比值](results/R803-original-single-map-reuse-and-mixed-Hodge-ratios.md)给42项/1680Q行的准确M6注入、四条原补行和五个旧56张量新收缩；U0不重算，一个694有理块至多84右端并全行代回。保原T为Galois+目标同构，由Uj/U0、原A/B及Wronskian给真实x比和群律，不除未知整同源。真Norm与b⁷/Nb、符号变换主函数、反实Lambda/s、原R794矩阵和全部高度常数保持。较小符号路线m≤8、N≤202，仅真选该消费者时补V8 q196..201。[R803实际六组坐标已认证](results/R803-certified-original-M6-mixed-Hodge-ratios.md)：run43702905620/source2a3f5be76，2127.991746秒；原694块p1000000007/det637607829，84右端均368 Dixon位/full1680。31manifest项/33ZIP/781原输入已公开IO全核；这些右端不重解。全局函数约分/KM接口、2torsion刚性化及实际η/高度仍缺，不能以表达式存在代替这些工作。

**R804（已证明）**：[原五低次数映射的整数循环复用](results/R804-original-selected-map-reuse-in-integral-cyclic-module.md)只读实际R794见证，五a(T)与C/C逆全整数；八个群律节点精确得到原五map。U6由原P线性组合，无第六混合求解；relative-x与y的DAG保原T⁷=ζ²、CM和完整Galois运输。仍原N≤196，函数合成无需五套Schur，β点值可在R792成功后先消费。两张反对角图的立方理想/min valuation及支撑saturation已严格给完整极除子公式；实际全局gcd/quotient/saturation适配尚缺，不能默认大算术闭点可拆小片。真正η、原刚性化和高度仍未求。

**R804点消费者工程冻结pending**：[接口](notes/R804-original-CM-point-consumer-interface.md)，coreecd9fc2a/wrapper5126b836；原R791已含实际sigma/rho，四组25文件即可，不搬旧R754大包。旧R735/R791/R794三组18项IO全核；唯一待真实R792，未启用请求。Hom映射不同不能推出特化点不同，按实际点完整处理O/反点/二挠/doubling，核原T7=ζ²与八节点最终字，并用真群律核vβ。该点值任务不消费R803，不给原A有限核前像/极除子/η/高度。

**R805（证明完成，实际铅笔/整基已认证，其余adapter待执行）**：[正规两图及三重数缩小](results/R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)、[完整契约](notes/R805-original-affine-integral-basis-and-polar-ideal-method.md)。原τ=e0、σ=e1+n e73在至多273候选有无基点铅笔，需真实690 minor；旧n=0模缺秩只复用、不误判特征零。R=S⊕S(−1)^144⊕S(−2)^127给272维原整基，primitive乘法/真实Krylov后在同一字段做两图HNF极理想，不能用奇异平面环代正规环。M6清极θ由5列残余核取得，3新增右端共一个V4块/full55项，不能把Uj直接塞V3。全部E_g=B+3D_g，B恰20cusp+P0；trace radical逐重数、两图重合/度数全验。六个Ddegree395/488/500/527/551/569，先按完整理想取V3非零u再flip，不假定569情形globally generated；标准degree272第二flip仅需≤297P。原ηprincipal为mathcalG³，三同源后mathcalG⁹R；真实多项式成本、二挠比较和c0刚性化仍保留。[实际铅笔/整基](results/R805-certified-original-affine-pencil-free-basis.md)已由run43705580592完成：n1/p739/det509,488,332，1/144/127分次、690 S行及两个新积的41项齐；15.520676秒。完整1322输出manifest项/1324ZIP/1272原输入经公开IO run43706758013全核。此处选择和已成前缀不得重做；其余极理想/η/高度仍未执行。

R791实下降三同源与R794低次数五基的双向变换保全原极化/η。C′:Y²=X³−27b、ψD=[1−ζ²]、微分因子3、主函数(-27)等全部常数必须保留；实际对称代表的二挠刚性化比较尚未求。


**R806原primitive乘法已激活**：[执行契约](notes/R806-original-primitive-multiplication-and-cyclic-certificate-method.md)e73f66bd；run43707290840/source75b1d56c，coreb014f9b3/wrapperb199f040。R805/R786真实两组输入，原690行集不重选、272生成性V3右端、全820模筛和实际272 cyclic determinant；仅成功候选做34×8 Dixon/full820及带权支撑核。AST已通过，实际候选/非零minor/准确乘法尚待返回；不把幂环当整闭，不做无需求的巨大完整Q(z) Krylov逆。

**R807原M6一次清极已实际完整认证**：[结果](results/R807-certified-original-M6-pole-clearing.md)。run43707939269/source2c44d025，375.019515秒；原962块p1000000007/det290159643。真实138×5残余rank2/kernel3，θ=e0−112648621e1/282292255+223442698e2/282292255，原λ3/4=0，无新增pair-tail。五选行投影各488 Dixon位；三成员690/691/693为336/464/472位，692由既成投影与核合成，四条全1100准确认证。1003完整manifest项/1005ZIP/997原输入与冻结verify经公开IO run43709814489全核。只需后继六个θU_j正规向量，不重算θ、8右端或旧前缀；极理想/η/高度仍未执行。

### 全p sigma：同一个真正可见标签的三个单位

真正目标为同一primitive/Legendre可见h的N_h与两个Cartier量同时为单位；不能拼R734/R741/R737不同标签。R739真实p41/h37否定筛内逐项单位反射；固定有限窗不外推。R697/698原平方根、R782/R784全wedge/筛保持左逆、R788跨p六核与Schur只给结构，不排有限域相消。C13单位不能消N+1高带；D/D6闭包恰L(pO)，固定维闭合捷径关闭。

[Hurwitz刚性](notes/2026-11-15-sigma-Hurwitz-block-rigidity.md)给全部a_(p+n)=κn a_(n−1)，高块由首p×p唯一决定；升p²/Hirota不增独立信息。[Serre/Cartier](notes/2026-11-15-sigma-Serre-duality-and-Cartier-pairing.md)给真实有限Serre类与独立Cartier秩一单位C(x⁴ω)=(4/7)Bω，但权5为零时低极阶Cartier自动零，两者尚无桥。[cosigma闭合](notes/2026-11-15-sigma-cosigma-descent-and-closed-critical-channel.md)保半周期常数、degree3平移截面、rank4核；x²σ⁶整行列消失，总阶p−6未筛全零仍等价原F/G，不产生新非零。

[原模参数heat连接与奇部可分平凡化](notes/2026-11-15-sigma-modular-heat-connection-and-odd-tame-trivialization.md)已证明：保原c=0，六截面在模参数heat下准确闭合，但a=0非L稳定。辅助E27上奇连接显式代数水平基在全部允许p≥41零曲率；首p截断严格保Hasse边界源，原A(P0)=0、DA(P0)=B，逆水平矩阵的源两分量为单位。[原首p oscillator](notes/2026-11-15-sigma-first-p-oscillator-curvature-and-Hasse-source.md)已严格求得A''=−XA/4、全局Cartier(A⁻²ω)=ω和(D−O)^p=(A∂z+6DAz)²/12，P0上3B²z²。Lens变换仅在A非零函数域证明，正则算子延至P0；保原Hasse源及全部横向导数。把这些式子转成固定原F/G的critical、同primitive/Legendre支撑仍缺，未筛全零尚未排除。

[原全六有限heat连接](notes/2026-11-15-sigma-full-heat-tame-trivialization-and-even-source.md)已完整平凡化：偶部是Lamé5X/16与15X/4的张量，经det−108的明确矩阵精确同构；第二连接的平方根覆盖Wronskian²−27/4，全部允许p可分/零曲率。偶部首p源−z^(p−1)(AeH/6+DAeR/2)及完整原值基p曲率已保留，F/G均纳入同一覆盖。有限单位矩阵只保全向量非零，不保某个Taylor标签；真正缺口是源传播经原critical、primitive和Legendre投影后不能全消。

[原critical对角运输障碍](notes/2026-11-15-sigma-critical-projection-curvature-obstruction.md)已证：双变量完整曲率在P0为3B²(z²+t²)I8，原N维稀疏空间经R^(2N+6)的所有最大子式均为单位，核一维且满支撑。故在原W上无漏出的水平对角作用只能常数；真正primitive×Legendre权对全部允许p不恒定，不能有该水平延伸。非水平交换子与真正Cartan混合仍保留，不将抽象满支撑核当实际sigma向量。 已有源单位不能通过删除交换子直接变成筛后单位；继续真实非对角表示及原配对，不再寻找该已排除的对角延伸。

[五次水平lift/Legendre矩阵系数](notes/2026-11-15-sigma-horizontal-quintic-lift-and-Steinberg-coefficients.md)已证：Lz=A∂z+6DAz、Lt同式，Lz²Lt³水平且P0=(6B)^5z²t³，原h无溢出送至总阶p−1。真实O2旋转a²=2s/(s+1)的归一T̂=a^(1−p)T对角恰P_(h−1)(1/s)，原平方常数准确α₀s/6。全偶空间真字符ρ(q)=q^((p+1)/2)J_(√q)^−1在u/v基给q^−h；原z/t系数仍被非对角混合，原period/split向量及所需配对尚未识别，未证同标签非零。 全部原八通道和偶/奇Hasse源保留；源传播的真实字符投影尚未等同原同标签乘积，下一步必须完整原配对而非取旋转对角后冒认水平。

**R808（已证明）**：[原cuspidal Gram商与真实period/split/Howe链](results/R808-original-cuspidal-Gram-quotient-and-Howe-chain.md)。R727全部群元素的整Gram把原轨道格非退化约化商准确识别为Sym^(2r)det^(−r)，r=min(h−1,p−h)；原e0、Frob-Hermitian、Tζ平均像和N_h同时运输。位置Cartan与链内SL2严格区分，链中心规范与Hasse连接准确匹配；实际sigma原单项式仍经Kraw混合，同h配对非零未得。 原period/split有限商的识别已关闭；继续完整八通道源到原同标签Cartier量的真实配对，不重复有限norm识别。

**R810（已证明）**：[原toric完整单位偶矩与曲率链配对](results/R810-original-toric-unit-moments-and-curvature-chain-pairing.md)。原P_T exp(tE)P_T=P_r(1+2t²/3)P_T给全部(2j)!·binom(r,j)binom(r+j,j)/3^j单位；完整Hankel非退化，原toric线的E链和观测链均为基。K^p(P0)=3B²E的压缩高偶矩仍为单位，但P_T不水平、P_TKP_T零曲率，真实源方程必须保[ K,P_T ]v。实际u_h在Legendre零时不能归一，整链非退化不保证原指定系数；继续原z/t到同h的完整源配对，未筛与primitive/Legendre共同非零均仍OPEN。

### ordinary真实值与原全局对偶

原p43、776bit q已Gaussian5排除，不是Serre反例。R773/776/779/780原格/cochain/real/NT像已成，三个Norm/深度自动，不决定真实Robert值。R783原Θ=B−iA=13b、b=10Θ、Ω₂/ε=22−2Θ，坏值Θ=11；平衡jet Θ=−iKq，坏Kq=11i。实际Robert/Kummer/Shapiro、global dual、Θ仍缺。保Euler因子和一次交叉相位，不做巨大q挠点枚举；真K子域乘积/43次幂及小11次角色都不能代χ±1。

## 运行和续接

根会话独占main/共享索引；各子代理只交专属小文本或核心源码。R787同核断点续算运行，R806 primitive运行，R807清极已完整认证；R803混合比值/R805整基/R801长尾已完整认证；R797/R799/R800完整输出IO已过，R800/R799/R797实际结果均已登记。终端失联时按根§8用小文本API，公开Actions承担实际pull和输出IO；最近真实pull与规则提交以HANDOFF为准。每结论立即提交，按原source+数学tag续接；不重算旧前缀，不把success状态代完整输出，不把中间输入完成代主定理。
