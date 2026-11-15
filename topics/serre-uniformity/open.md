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

全部旧公式、已成输入的source/run/SHA、闭合路线和来源逐字存于[此次R820前open](notes/2026-11-15-open-before-R820.md)，内接此前归档。下述为当前可执行缺口；不重算已成阶段，不把算法存在写成实际数值。

### 原规范高度与真正全p排除

R575真正正商是Ψθκ4、根号负，旧相反扭向秩零应用撤回。R616/R726已给全部充分大允许p的原β非挠、rank=dim、原log同构；R719/R722真实有限迹和完整尾已成，不再加因子数前提。复非消失不代同标签模p单位或高度排零。

R593/R596保原η_h、χ、μ3 tensor与清分母；R690/694/696实际坏靶Ω={0}。R724完整保原MW/第二类周期、Hecke轨道、因子2、Poincaré/universal extension、非p项、规范平方线丛刚性化和全尾，不假设高度矩阵可逆。真正缺原β/η、规范高度jets与(724.33)有限Bézout及其对全p存在。R785 Rosati压缩保CM值和切向两列，实正定不代p进非零。R730/R742/R744全尾和Weierstrass接口已成；深度4/5/6实际根与原高度未得。

**R823一般p原c1评价强化已证**：[原Hom不分歧](results/R823-original-primitive-Hom-CM-nonramification.md)。在原M2,1≠0时，K有理c1与局部s=a−1使评价核在R819原域作用下稳定，实际Hom拉回基给非零评价，故全部非零实际primitive L-Hom在c1不分歧；R729给充分大允许p前提。保J_h=c_h M2,h s/16+…、原β常数及c0归一化；共同m=1已是R729结论，不重做。未给单位/深度4或高度外积精确阶。

### 原p41函数与高度输入

R735/R738/R745原模型、4920陪集/800闭链/六Hodge、R754 period/Hom、R759完整Z格rank12/O_K6均已成。原b=r0⁶、L/K7、M/L40、αs/CRT6逆/ζ²一次/246、c1=4424/c0[2876,2822,2823]必须保持。Y genus127；R764全格cusps/c0映O，R769低degree≤693完整分支关闭。单p41工作服务真实高度输入，不重开R707分类。

已成且禁止重算：R774共同56Hodge三积，R775 M2/M6/M12及普通power1..6配方，R781原f4的R0..142与κ幂，R786原power1..5 q0..128，R790原146个M2的CM值/首粗导，R791原Hom/实下降，R794五维低次数η基，R795原1506个V6 q0..81，R796原CM的144条全局二次关系及length2，R798真实1506选行minor和690个τ³V3积。具体真实来源、耗时与输出SHA保各certified结果和上述归档。

**R787原A/B仍运行**：run43708449812/sourceac5998f3从旧run43683912711的5.15GB BudgetStop断点同核恢复，core93d3d72b未改。1517输出/1372输入全SHA核后，只保每prime最新完整Dixon及其它已成stage；原V5=1234、129条件/14分支、同主元/自由坐标不变。尚无真实A/B，末端须全129×20准确代回；预算停则同核续算，不换R802。成功立即R792实际CM值/立方根及R809 A/B追加。

**R809原S5运行**：run43712427063/source91fbd81e，core dedb5d61/wrapper3616aac1，[原方法](notes/R809-original-S5-normal-coordinate-consumer-method.md)。四组4117输入已核；六τθU_j共84Q右端、1234列/1380行，A/B后追加28右端同一basis/身份。保82^10、b/s与λ换基一次、τ最高项零，只补真正缺尾。尚无实际minor/新坐标。

**R792/R804工程待A/B**：原R792 core7b7a5483/wrappercdac2e93保c(f)=−ζ²f、y0=sv0、原Fb唯一立方根/21次奇因子，不在未知同源核中选前像；CM值/首jet全零才增加高阶。R804 coreecd9fc2a/wrapper5126b836旧18项IO已核，随后消费R792七新项，保全部例外点/T7/原Gal/rho/vβ，不重求五个Laurent核。

**已成原输入禁止重算**：R797/799/800与R801长尾、R803 M6混合比、R805正规整基、R807一次清极均完整IO认证；真实run/source/SHA保各certified结果与R820前归档。原θ=e0−112648621e1/282292255+223442698e2/282292255、λ3/4零；旧power2..5至195已齐。R806原w0=e2/n1乘法34×8列/full820与cyclic已准确认证，R813原g/h两S3各432位/full820/scale6724已准确认证，451ZIP/726输入及冻结verify全核。后继直接消费，不再重复旧前缀。V8 q196..201只在真实选中需要它的消费者时补；κ^N每函数一次。

**R811真实乘法待A/B**：[两图极前像证明](results/R811-original-normal-polar-ideal-preimages-and-two-chart-certificates.md)/[契约](notes/R811-original-regular-multiplier-and-polar-preimage-method.md)。首scope core849bca27/wrapper2a1d1c28已全文审，实际R806齐，待R809 A/B；r5八模/九准确点，first-column/commutator、两图t^5因子保留。完整unimodular核/HNF和双向Laurent工程另稿已齐；原P不可变作全式验算，次数=τ全长＋σ在0局部长。generic实际run43719858329的四个exit97恢复/五结果同SHA只验证通用算法，不替实际原模型。五函数DAG/Norm/η刚性化常数不得被理想首一化丢掉。

**R822完整极格的充分认证已证**：[全局余长度](results/R822-original-polar-lattices-certified-by-global-colength.md)。候选只需底环子格，完整原MAH=MBW给包含，双向Laurent使两图拼接；真实τ degdet＋σ在0的orddet与独立R791 deg(y)=1206相等后才给全部原极理想。有限域可用原b多项式的全部实际因子与ζ两root计算candidate，按全14原坐标CRT并公平推进真实profiles，最终全char0式/两图/长度必须通过；未知次数/系数不得由1206预填。仍未有原A/B或极格输出，完整char0 transcript保为另一个正确方案。

**R815原Mg/Γ已激活**：run43719622321/source2a3300a9，core80516ff9/wrapperab725da0。R813实际53文件最小输入已核；R817精确证明只需Mg六模/七准确点与Γ五模/七嵌套准确点，We0=e1先核，两Γ列逐系数与完整[[Γ,W]+MgW′,W]=0给唯一原导子。不另CRT Mh，不形成ambient场迹全表；Γσ=tDΓD^-1−t²DMgD^-1diag eps，δσt=−t³DMgD^-1。实际矩阵待到。

**R814完整降重数接口已证**：[原证明](results/R814-original-cusp-zero-ideal-and-exact-multiplicity-peeling.md)。全完成乘积内积分给C=im[Γ,Mg]恰约化20cusps；完整I的N=im[H,ΓH+MgH′]，P=(N:_R C)逐点max(m−1,0)，sqrtI=(I:_R P)，m0保留。六原E=20cusps+P0+3D，度1206/1485/1521/1602/1674/1728；第一剥后无cusp可省C商。实际原极I/Γ尚缺，η/height未成。

**R820小有限代数入口已证**：[原两图cusp理想](results/R820-original-cusp-finite-algebra-and-two-chart-Hermite-ideals.md)。仅273已成S3 q0行同除N0给F20值与Z；两个原锚点避全部cusps，R806 Q-form/忠实扩张给评价满射。逆序Z链≤292候选，实际rank20/minor/全部关系及两图各总度20才认证完整HNF；不预填常数E秩20或Z primitive。第二图用同F的Z^-1/Z^-eps，无需新Fourier或等待大导子，实际289原文件/726载体成员纯IO全核，core25f5582e/wrapper64da6955与request6eb90ef0已激活；数学结果待公开Actions。

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


**惰性Gaussian分支的准确剩余源**：[原harmonic7接口](notes/2026-11-15-sigma-inert-Gaussian-harmonic-seven-source.md)。p11mod12五端项/EO投影给P7/(a²+b²)，严格分解为五阶多项式加H7/(32(a²+b²))；原低jets给五个Qpoly条目，P0均零。余项是指定level6 harmonic theta的一次q原函数，整体由原Q定义，仍有源；其本身非零不等于原CM的FG条目单位。真正原条目代数/period比较与同h primitive/Legendre仍待完成，无新有限窗。


**原末项的全SS同权路线已排除**：[完整障碍](notes/2026-11-15-sigma-endpoint-global-Hasse-obstruction.md)。原[z^(p−7)]xσ6与[z^(p−10)](−xyσ6)都是p整、权p−11的全层模形式；但不存在参数无关的Fp常数αβγ、γ非零使Δ(αf末+βg末)=γDA在全部SS成立。Hasse简单零给模A整除、权2商为零，Tate DA常数1/12矛盾。仅排全SS路线，原j0专属端项关系和同h目标未排除。

**R815执行范围由R817缩小，实际矩阵待算**：[方法](notes/R815-original-normal-derivation-operator-method.md)/[R817两算子证明](results/R817-original-normal-derivation-without-separate-h-multiplier.md)。首次三算子版本尚未执行即被替代：只CRT Mg/Γ，保实际vh；Mg六模点/七准确点，Γ五模点/七嵌套交换子准确点。先源断言We0=e1，再逐系数Γe0=0/Γe1=vh和完整[[Γ,W]+MgW′,W]=0；cyclic唯一给真实导子。不造独立Mh/场迹/全基乘法表，实际两图/尺度不变。R813完整451ZIP/726原输入/冻结verify已核，两个原向量432位/scale6724；R815真实53文件源已核并激活，实际矩阵仍待。

根会话独占main/共享索引；各子代理只交专属小文本或核心源码。R787同核断点续算运行，R806 primitive已准确完成，R813两S3实际完整成功、R815真实请求激活，R807清极已完整认证；R803混合比值/R805整基/R801长尾已完整认证；R797/R799/R800完整输出IO已过，R800/R799/R797实际结果均已登记。终端失联时按根§8用小文本API，公开Actions承担实际pull和输出IO；最近真实pull与规则提交以HANDOFF为准。每结论立即提交，按原source+数学tag续接；不重算旧前缀，不把success状态代完整输出，不把中间输入完成代主定理。


**R812（六case已准确成功，全部split p的未筛配对非零）**：[实际结果与全p推论](results/R812-certified-split-prime-unfiltered-apolar-unit.md)，run43713181015/source2b7183a3。固定六FG均非零、分母121，清分母Norm因子2^38·3^12·5^12·11^24；U分母88、det分母11^6/Norm仅2/3/11。因此每个p≥41、p≡5mod12的原交替卷积Σ(−1)^j f_(N−1−j)g_j为单位，保共同c/Frobenius/Gaussian相位并先代数化再SS评价。完整8文件/6manifest与原verify全核，47.336289秒含拉镜像。原primitive/Legendre同h与p11mod12 Eichler分支仍OPEN，不以未筛代筛后或主定理。

**R816一般p cusp轨道缺口已闭**：[证明](results/R816-original-all-prime-real-cusp-orbit-and-degree-coprimality.md)。原Y_K标准level2p模型的准确剩余域为实Q(ξ_p)^+，c=3m−1与L/K次数m互素，Y_L/X_L全部cusps单轨道；X→Y原三次盖总分歧而剩余域不变。L定义截面全部cusps同阶。R818原首cusp系数char0非零及真实Hom存在、R819原K[T]=Q(ζ_(p+1))秩一与评价核稳定均已证，故每个非零实际primitive L-Hom在全部cusps不分歧；R821现以实际整Hom格/Φ_n(±1)=1证明全部cusp像O，原y在Y的cusp极均简单；非cusp极除子仍待真实函数。原r=x/a与η=h/a阶(p−2)/3；不把char0结论当p单位或同h三单位。
