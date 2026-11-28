# 未解决问题与当前接续

会话：Astra-rank2-Sha-0b097461-20261127；2026-11-28。
**主目标未完成，持续研究，不等用户回复：**固定一条 \(E/\mathbf Q\)，完整证明 \(\operatorname{rank}E(\mathbf Q)\ge2\)，并使无穷不同素数 \(p\) 的通常全 \(\Sha(E/\mathbf Q)[p^\infty]\) 有限。固定有限族的联合无穷非零可用鸽巢，随 \(p\) 换曲线不算完成。

[本次整理前完整 open](notes/2026-11-28-open-before-exact-p-square-characters.md)逐字保留全部旧问题、精确公式、运行与失败、来源及更早归档链；下列只是当前接续，不删除任何未闭门。[results](results.md)、[本卷索引](notes/PROOF-INDEX-R1051-R1100.md)和[HANDOFF](HANDOFF.md)给已证内容与实际执行状态。独立新结论按根规则8放入 results/R编号，旧 notes 路径保转向。

## O新来源：实际 p² 新块、解析运输与同一 canonical 斜率

[R1052](results/R1052-original-unmodified-b2-toric-flat-vanishing.md)已经证明：好点 \(g_2^*F_0\) 的有界性完整成立，但返回原未改动 \(F_0\) 的完整 toric flat 族及实际外权导数恒零。它只杀这个完整和，不能推点级测度支撑、canonical、signed 或 outward 为零；不再重做这条零分支。

[R1054](results/R1054-original-p-square-depleted-source-and-exact-conductor-blocks.md)现给实际通常剔除中剩余的完整来源：
\[
W_p=p^{-4}(g_2^2)^*w_0,\qquad
g_1^*((p\delta)^nA)
=-p^{2n}\delta^nF_0+p^{4n+2}(g_2^2)^*\delta^nF_0 .
\]
真实 cyclic conductor-\(p^2\) 点满足 \(v_p(c_C)=1/p\)、
\(\Omega_2=p^{-2}c_C\Omega_0\)；第二项准确成为
\(p^{-4}(c_C\Omega_0)^{3+2n}r_n^{\rm alg}(E_C)\)。
不能将原点 \(D_{102}\times S_{34}\) 的整性界搬给这个新邻点。

同文§8支付全部有限字。每轴 \(\mathbf Z/p^2\) 的完整 Weil trace 在单位、非平凡主单位和其余元素分别为 \(p^2,-p,1\)，故旧球重数一、非平凡 tame 角色重数零、所有 exact-\(p^2\) 角色重数一。完整矩阵
\(p^{-2}\zeta_{p^2}^{(51/2)(A^2-4AB+B^2)}\)
分成 \(p^{-2}v_0\otimes v_0\) 及全部 wild 逆角色对；旧新混合块为零。每条局部块非零，全局 Hermite/六根/tame 投影仍可能消零。有限环投影保 \(1/[p(p+1)]\)，不能称整幂等元；新 \(p\)-torus 不算入原 full54。

R1054§10现付K的六阶CM Weil绝对相位、字/Haar配对差、完整p² Weyl和及逐h真Jacobi/[p]覆盖字。[R1061](results/R1061-original-p-square-antilinear-gluing-and-full-theta-descent.md)进一步给实际反CM p⁴图群、(34,102)下降、固定δ三盖及非分裂genus2 principal商；完整Miller和c_Q估值、两非平凡3角色/普通trace零、真实periodbasis/positive[-1]均付。§§11–15进一步付全部34²列到两conductor-p²/level68来源的准确加法及反写、实际二/三characteristic、full h/冻结χ及mixed heat；§§16–19已用真实division函数付全阶jet、vZ_Q=−1+p/(p²−1)、各非零平移项独立Lie半径及完整有限精度；§20首graded全Q和及指定(p−7,p−5)差二槽非零已付，但真正critical tame−2首层全消；§21付paired Miller真实F2野角色及完整代数H-trace/period账本；§22现以actual marked身份和共同正整数逼近支付whole归一迹=(p⁻²−1)旧germ、全导数及非平凡Norm纤维的真实critical读者，原λ/λ′由准确有限Fourier式全部返回。下一消费真正R716 canonical tame0/wild分支和完整T_orig余层，未circle字的非零不能推whole临界非零，H也不自动是固定曲面的全局theta截面。

R1054§9现付完整finite intertwiner与真实核/class方向、Tate determinant/cup/KS、三个微分、准确旧项差和全部p+1单位矩阵的正权向量。非平凡wild全和消旧不赋原坏条件给新增ramified字；投回第二输出旧线则新字消失。原惰性2/full9不自动满足AI全局Heegner假设；这里只用同一prime-to-p full-level cover的局部GM/marked构造，classical k=3的局部半径允许p²，不能套two-variable n≥3或直接套全局Thm7.1。

[R1059](results/R1059-original-p-square-source-and-complete-critical-germ.md)现已给同一来源的完整负二germ及斜率：各点裸bounded Q_t输入不变，随权tensor因子j_t留在外权Λ=λj_t；真实Teich逼近与全部Maass尾、v(C)=2的Tate范数收敛支付同一解析恒等。精确保p^-4单位周期及(1−p^-2)旧germ；只有同一full-avatar wild和或R1052原完整germ可去旧。斜率保log、全部Maass、period、det与外权导数。

R1059§8现已付同一Frobenius-rigid primitive和实际有限图的值身份：p^-6Ω_i^-1〈q*G_C−G_i,ω_i〉、全e_i/m_i及旧germ保留；exact-wild完整正交时为−p^-4Σλe_i/(m_iΩ_i)AJ_out。原ψ4十八degree17核、双sign、full9和Artin1/12全部保留，full9中心只在原source本征块平方为1。

[R1060](results/R1060-original-full-gaussian-transpose-and-critical-slope.md)现给A16斜率到原整个双Gaussian来源的真实有限读者：完整逆Maass为指数卷积，有限Newton多项式给B_{i,H,ℓ}和准确槽/period系数精度。保K−old、全source h积分、actual arch与复γ逐槽代数化；图源−6δ/两√6均已付。先冻结Λ(-2)/Λ′(-2)再取全部低槽，不换成Λ(n)或原三个总period产品。§4.1将逆Maass合为e^(βZW)H，β=−C/ρ及vβ=2p/(p²−1)使Gaussian/逆在整闭双盘为单位；H本身范数及canonical completion相认仍须另付，不能删尾。

R1060§§8–11已付whole circle支撑H=W²HΔ、原双PD等距、严格全核闭盘及冻结t的共同Gaussian/−logχ费用。全局theta下降仍先对未circle投影字成立，实际canonical completion必须保全部角槽和真实period/tensor次序；小盘不预付p²挠点平移或各rank1范数。

R1060§§12–13现保completion全部角槽及有限q/r/s表，真实[p]pull的J=p^ℓJ_orig及全尾已付；degree completion另保p²C/p^dC差，不能解析非单位p权。wholecover严格盘至rZ′+rW′>2/(p²−1)，只对已识别[p]*S运输bad，不给新Weyl字零。

R1060§13.1进一步定清边界：同coherent frame的whole临界闭盘Tate延拓恰等价整个μ|Zp×=0；canonical单斜率零不能替此条件。若要用真实挠点或图册上的正则延拓，必须付坐标/线丛及形式log退化的实际比较。

[R1062](results/R1062-original-translated-miller-jets-and-critical-weight-germs.md)进一步付每个实际平移源的全m二项式Tate族、两槽全部非单位费用相消后的单位底数、共同合法子列及精确负二值/斜率。指定Norm纤维的seed endpoint真非零；此输入只能在已付actual graded返回的字使用，未付部分保原T_orig及R1060有限Newton。真正R716 Hall还需负侧tame0，不能以Norm纤维非零略去它。§7现给实际period半线性作用及raw全部jets独立，但canonical读者须消费准确Ω(R′−logU*R)；若完整临界值为零，此法不排canonical斜率零。whole bare µ的Galois作用另保完整Maass三角T_((c²−1)C)D_(c²)，不能仅以LT线缩放替换它。

R1062§8已付同一V_Q的actual even-product及第二盘全单位，原首Gaussian准确限制逐字项级weight半径≤p^(1−2τ)，仍比首wild指数边界小1/(p+1)；不能仅补k!扩大。下一只看完整Hall及原Norm17r参考先作全source相消；该边界不否定whole，也不声称同一exponential权参数直接到T=0。

R1062§9现给正返回：真正j-zero CM除法及连续β把全sigma高尾的归一比值、同一S34/Theta2全部有理因子一起延为每个严格R<R_E盘的norm1单位/逆；Normβ≡17modp，未假定Normβ=17。R632/R635原p幂明确复用。此为physical形式比值的延拓，不能在挠点边界评价各sigma或移出Hall和。§10进一步在实际[p]拉回框架付全scheme kernel匹配、共同J(w,Q)和J−1∈wI_Q；原A34=A2β·φR_T，R_T为(w⊕Q)^6乘整单位且保全部实际中心/外权。全Katz native carry及a_Δ模p²两项已返回；下一核中心比的真正theta-extension余class及完整Hall和的独立低行，不把六重零、同coset或旧自动同余当主非零。

[R1063](results/R1063-original-tame-zero-hall-and-five-layer-miller-return.md)现付真正原tame0 Hall角色和完整中心：Z_Q=Xi、严格LT全坐标、负二连接第五层误差、W_+=hat3W及原Haar d/p²全保。前五层准确是两原B卷积，首项d_-,p−1s_p+1；没有得到任一首系数的无穷单位。§8付原Newton五层；§10 L1–10以完整zeta连接与R618强尾扩大到全部p−1层。最高层修正为−(2γ_+/3)Acan(0)W^(p−2)，原bad使它和常数同时消失，余p−2阶除p jet未被赋零。首个非零jet给paired估值k/(p−1)，仍不自动给原单Hall严格门。§9现付完整non-p/h/Artin整列、十八原商的γ_i/17^(-3−n)、Norm/avatar对偶与全部外权导数，以及原c0/ell单位；其负二返回准确为p^-6Ω^-1×单位×两Hall。单图仍不免费分离；同一单Hall仍需v<2/(p−1)才排canonical坏，正Hall的全五层或有限非零并不完成无穷严格界。原period与actual LT测度/有限域返回正继续接同一斜率，普通disc固定不冒ST扭曲下降。

[R1064](results/R1064-original-book-cartier-dual-period-and-actual-lt-measure-bridge.md)现付原book/dual-LT精确单位、全Galois方向及actual whole µ的全LT盘lift。完整Maass和log−E读者保留；有限F真正bounded字符函数的所有trace-dual坐标返测度；§10结合已发表Fourier等距消去最终different损，actual lift精确等距。§11已构造原单位测度的等距quadratic lift，付P10单位restriction、负一次/负二次低矩、完整Möbius及局部热作用范围；一般Dirac反例不排原actualsource。下一继续原fullMaass来源的全盘/ψ整性与准确下降；普通LT系数固定不是ST扭曲下降，去period完成矩候选若真LA分布反迫flat整分量零。Colović全文已核；本二次域无损返回由BSS加Berger等距已付。原Mahler前缀有明确affinoid精度。§12现付actual A(Q_E)的完整ψ核平均与原单位cut、负二/全log−E及Λ′的无损有界测试；它只用于已有原测度的Fourier像。§13保同一whole系数的F-Tate编码、数字和读者成本与完整斜率有限精度；ordinary H±不因此被认作原单Q提升，实际tensor/连接仍须支付。


[R1065](results/R1065-original-hall-katz-unit-measures-and-canonical-return.md)现已构造两份原H±的真正整Katz primitive测度，完整p核迹只需一个p；K20a/b与I18a另显写E17→E0整列的17^-2固定因子（c0^(0)、L±），不改严格估值门；原wild中心、正质量高共振和、负type4质量零、非基域点的完成tensor测试及d/p² Haar均已支付。实际负二有限测试和前五层逐项返原Hall/原Newton，准确严格门为v_p µ_+(c1^(p+1))=2，等价原s_(p+1)单位。§§8–12现付同一整tensor、实际612ω Gaussian及整个B_r(j)/全斜率测试，模型/p-Haar/period/外权全部保留。该Gaussian在Fourier侧为mixed D_G heat；真正coherent乘法的另一方向现由R1066的逆矩/全移位收缩支付，Katz整性及primitive支撑仍未给该矩等号。W1–26现付真正p²新Weyl列的整框架/原Miller lift、无额外p的ψ0 dual、完整kernel character、唯一coset及原成对反CM图，全部old/new/Haar/finite jet/physical p^-m通过原连接返回；正6q/负4q高系数单位不代严格低矩。R1066现用此actual新dual和完整连接支付全Gaussian交织；下一消费原有限角/source关系争取canonical非零，不能把finite-F普通LT函数直接当原单Q提升。R714/R717/R721/R723已有Cartier/Artin–Hasse首窗与有理极帽，不重复登记。

**下一实质门：**给这个完整转置后的h/finite投影、新增ramified covectors及A16全部权导数到原固定canonical斜率的实际未平均关系。有限图的值不代导数；局部单位矩阵可逆不付该关系，也不套AI全局Heegner定理。[R1058](results/R1058-original-cm-principal-unit-mobius-and-centered-root-trace.md)现已付 CM 主单位的完整居中 Möbius、所有系数和det/KS运输及含全部μp闭盘的真实延拓，并逐点证明与root平均互绕；该作用固定每个μp点，不是根平移。实际原g2²第一轴商核已核。R1059已用同源正权式与真实flat逼近比较负二全germ，§8再给整个有限读数的实际图身份；原avatar/Teich/旧项均保。不能由群阶相同认分支，也不将p^n当解析函数。

[R1056](results/R1056-original-flat-amice-critical-slope-and-bol-primitive.md)提供真正可用的同源读者：临界值是单位 inverse-square 矩，斜率保 log、全部 Maass 修正和外权导数；正 KS/正杯积 Bol 与 R997 一致。直接整 Newton 的值读者用至 \(pH-1\) 阶，斜率用 \(O(p(H+\log_p(H+1)+1))\) 阶及准确额外精度；旧 Stirling 路径另付 \(v_p(N!)\)。R1054 的负端点是原 Coleman 的 \(p^{-6}\) 真 \(Q\) 平均；R1059§8通过整个同源germ识别完整有限图读数，仍不逐根认同CM商点。

[连续性审计](notes/2026-11-27-original-psi4-common-factor-digit-and-continuity-audit.md)继续优先：完整两 Hermite 的
\(K\zeta^u(( (p^2-1)u)!/((p-1)u)!)^2/((p^2-1)u-1)\)
不能在全部正整数连接两个非零连续函数。旧 full54/六线/新 \(\psi_4\) 的连续几何 cross、\(H_{-2}\)/AJ 与共同几何单位仍条件化；固定幂 period 不修这个障碍。原 \(p=227,u=1,n=51526\) 全槽 run46073583710 已付特征零非零，辅助65537不证明227单位，不再执行同一输入。

独立[纯双槽 Newton](notes/2026-11-27-original-psi4-double-slot-newton-and-canonical-slope.md)、完整 full18/Artin/proper-fp 与
\(\mathcal A_k^{\rm out,new}=(p^2-1)I_k^{\rm new}\)
按原范围保留；参考 \(R_3(0),R_5(0)\) 非零不能单独补上述接合。原坏点
\(O_D=(1-p^{-2})G-\lambda_D^*I_D/p^2\)
仍留原 \(G\) 边界；完整 incoming 范数零不删 outward。所有有限2/3/17、wild两陪集、full9和完整权都保留。

[R1066](results/R1066-original-katz-negative-weight-and-full-gaussian-return.md)的N1–19与Z1–22已完成同一新字的负权connection和原coherent/fullMaass返回。实际c_q锁住归一，合法共同权支保prime-to-p角色与p深度；完整S_C S_-C=1靠全移位双卷积，非两个E逐项相消。Z21a给原whole already-Maass germ，全部old/finiteh/差2角投影/17^-2/Haar/Λ′保留。各新字inverse矩非零及测试单位均不传给Hall或canonical。下一须证明原tame平均后的真实低系数于无穷p命中，或同一固定有限族的全来源关系强制至少一个canonical非零；原P10 descent在新表达中的等价重述不新增坏行。


[R1067](results/R1067-original-first-wild-rubin-even-multiplicity.md)现付同一个原第一wild点的偶重数：ord_(tν)A_p=2ord_0H_r，N2/Norm17r参考为单位；全部finiteν、Miller中心、physical导数、Gauss/1/p与含p² CM-pair费用保后相消。exactHall0才迫Φp²及λ≥2e+2(p−1)；中央bad联合该精确零才给λ≥2p+2。下一继续真实λ/低jet约束；不从中央bad、高赋值或Katz整性造wild零。

R1067§§9–14进一步给physical首jet整界及同一actual整Hall源P_H：先保任意原M/cover/连接，再准确除b_M，log全尾给2M1−M2/2和3M1−3M2/2+M3/3。exactHall0⇒[v^(p²−1)]P_H∈p²；bad联合exact0才给三矩行≥2+1/(p−1)。一般ψ0/质量零不自动有额外p，原明确反例已付；模型frame(50)保θ^(Δ−6)及p^Δ H0项。仍需实际源矛盾或由bad可消费的非零高赋值支关系，不能把此行冒作裸S系数或新增自由坏条件。

[R1068](results/R1068-original-b18-katz-inverse-and-hall-coefficients.md)现付原共同B18及D102/S34准确因子，canonical首6不混Dold首2。同一实际T的完整中心/唯一p² lift使A84真整逆落原ψ0 Katz范围，actual Hall a_m准确为102/84逆/16完整有限三卷积；R1067(49)直接成为该全和的p²条件，逆不能移出Hall。普通Cartier另有d/6个角，首漏行−26329/105不消；wholeGaussian/physical/old与E17框架全保。下一查同一实际卷积的非零高赋值含H0行，不把恒等式、单位质量或exactHall0条件当主非零证明。

**R1067§14.1范围收紧：**实际M0/C、M1/C在首挠点的μ_d固定域，其值群1/(p−1)；旧L3/N11与完整Bell尾已无条件给M1−M0∈p，即Uq a_Δ−p a0∈p²。因此exactHall0下(49)和R1068(B25a)的额外p不是相对whole原来源新增forcing，不能拿它重复计收益。继续原p²组合、全部高角和非零高赋值含H0行的实际来源核算。

R1067§15（53）–（58）已付actual δ_k的1≤k≤p−2全Bell差分界及完整含质量二矩行，native M2保ℓ_q的1/p费用。exactHall0分支的a_Δ≥3−1/(p−1)仍不由bad提供；§§16–17已从真正Kato两图/非p288下降逐embedding单位幂付原比较标量的解析性及归一各阶p^j导数界；A(x)=U(G34/G2,17r)²准确保模型/p²/Artin/Gamma/原参考。完整含H0导数门仍只是必要条件；浅层已发现自动相消，不计forcing。§18现已付共同Gaussian的全p−1块算子及逆、全部carry和真实参考17^ρ(17^(p−1))^t；原0块比值不能据此删Gaussian。§19现已付同A_p整性的完整p阶Euler读者（73）–（79）：保所有U/参考导数、log^p全尾及唯一r=p+1首连接，最高行返δ_p−pδ_(p+1)/2和真实ρ=p−2负块。没有外推旧高差分界或赋精确零；§20已评价首连接：目标原质量≥1/(p−1)使其在完整平方Euler和中自动变深，不需bad，也不赋两块相等。当前精度真正剩U(M34/M2)²的bare Katz/Frobenius组合及模型Norm费用；下一用R1062§10全kernel共同族和实际中心余class消费它，不重复已自动的首连接或旧Fermat接口。

R1062§11现支付原中心：全scheme唯一对称lift使C34,T/C2,T′=ε_Q Cβ(Q)，Cβ为真实径向整单位；J在全厚一级群的commutator精确为Fermat-17类，原指定lift相位和λ/λ′全保。G62/G63只在G[p²]完整输入成立，高jet仍用G50；下一消费这个实际有限算子和bare Katz/Frobenius，而非假定q_p(17)对无穷p非零。§12的全translated相对核现已付：ordinary系数和(m)_k给γ_k≥kη，η=1−1/(p−1)，全Δ块/carry及逆均保；a<η仅是算子可作用范围，shifted参考输入的大盘延拓仍未付，未赋whole Hall新半径。须继续原中心/全外权下的实际Euler或canonical读者，不由单字单位核推加权和非零。

R1067§21已把实际比较单位精确化：原b_j/ζ/e_m方块系数1，deRham才一次产生θ^−(2m+1)，故U=U0·17^−m；β尺度后为U0(Normβ/17)^m。λ17的Fermat余类是完整Euler的一项，不能独立判非零。继续与R1062实际中心/full kernel合并；R1062§13现已付N(a)=17规范：真CM除法的finite-flat极限给Cβ(Q)=K_a(Q)，原aT−βT共线half-pairing严格1，指定T′不换。原SL₂球及代表律付λε=λ′，完整Hall回同一H_a的平移值；K_a首Fermat槽及G85两校正全留。R1067续证§§22–23现已把全bare Euler严格压到0..p+2 native乘子，并证明K_a首frame在模p^(p+1)的完整商平方内自动变深；所有log 1/p、Lagrange系数、q-carry和低jet交叉已付。当前剩余明确为式(99)的同一H_a加法和；下一直接消费它及canonical坏后的独立行，不重复已自动的模型/frame项；固定√17物理来源另核全球高度，不把formal函数认成代数或给旧H3中央零。

## O原矩阵：同一个高核、全深 Smith 与严格全局收益

[R1051](results/R1051-original-full-depth-gaussian-node-recurrence.md)已付全部物理行的数字折回、完整节点递推、同一 \(P/R\) 的全精度 \(j!C\) 厚核、Hasse–Hermite 等距 PD 代数及全部截断 Smith。回旧基线保准确 \(E(J)\) 损；普通厚理想范围一般至 \((p-3)/2\)，原 S/T 环至 \(p-2\)，不是免费到 \(p-1\)。首 Bockstein 须满足原低核和同一个 \(R\) 的像条件；canonical 的单一加权槽不是乘法理想，不能变成逐节点消失。

**主门仍为**
\[
\sum_p g_{p,D}\log p>3M_D\log D .
\]
当前付出的收益仅 \(O(M_D)\)。需要随来源增长的真实深度、全部块和同一饱和旗标的全 Smith 指数；不把旧低13、来源秩或环境逆矩阵重复计作新收益。

[正特征森林](notes/2026-11-27-original-positive-characteristic-capped-forest-and-cubic-bound.md)的所有 cap、D-property、原奇点、三层循环、薄X二次界、68角帽、两 carry 与第二余核 Xi 均已付。实际三块是 \((t^H,t^Kh^2,h^3)\)，判别式门只在已超过窄窗列数的范围触发，未达全临界预算。旧 R467 显式二维界和 R637 真短三块范围优先复用，不重做更弱指数；保 \(\deg_Y<p\) 和重复因子例外，不新增中央导数或乘积的零条件。

R1042 的全 Hurwitz 前缀、两变量角结构、全 Euler 与原 q13 回执已付；环境左逆不等于 scalar Schur 的 \((18+o(1))p\) 成本。真实前三秩跳至多1/3/5，三个来源仍在二维角上。需同一前缀和补域的全消元，不能将有限非零秩当中央函数非零。

## O1–O3 / O末窗：原 canonical 联合非零与 B12 真实读者

R959/R970–983 与 R1038 已分别支付固定 E65/E65³/E260/E54925/E8125 及 E3969 的 rank≥2、全角色/周期/平方和通常全 Sha 桥。仍须在同一无穷 \(p\) 集合上至少一条固定来源的原 \(J'\ne0\)，才可有限鸽巢。孤立 \(p\)、质量非零、投影或低 jet 不足。

[R1026§9](results/R1026-extended-flat-window-thirteen-saturation-and-full-contiguous-family.md)的原两个39支顺序，全部 \(H\le p-6\) 比较精度是 \(p^{H+1}\)，非零质量、两 Gaussian 及 \(m_0\log q_\alpha\) 全保。末六权 \(H_t=p-6t\) 同样保这一精度。
[R1028§9](results/R1028-terminal-flat-weights-and-complete-thirtynine-primitive.md)的全权差为 \(c_pA^{p^2}T_t^p\)，全39核点从 \(p(H_t+1)\) 起；native 窗后原四阶 cut 逐纤维无留数。一般 \(c<6t\) 仍盲，\(c=6,t=1\) 只有尚未授权非零的端点候选。所有物理 M、高位、GP10、外权、Newton 和及严格 \(a+2b<3\) 费用保留。

[R1053](results/R1053-original-b12-canonical-reader-and-complete-thirtynine-trace.md)现将原390两来源的真正 B12 商、全部324词和完整有限权，写成 E3969 原 degree378 canonical 必要行。二挠第四 Miller、CM 有理比、O增加六零、\(\pm S\) 与二挠全部阶均保；增加的六零抵消表面六极。完整四次 Cartier 和39支 differential trace 返回同一首行；\(\operatorname{Norm}_\alpha(y)=c_\alpha y\) 使对数方向 trace 标量为1，一般微分仍是 \(39/\alpha\)。theta 中间载体为三个 rank13/degree126 稳定项，不能冒390/39得degree10。

R1053§§8–11现已付真实 reader 到原 P10 的完整39字符配对：Gα的全除子、二挠194d_p−8p极帽及全部非齐次连接费用保留。十三维4jet与原39维长12修改均准确，但不是native极帽。source390与target10的p曲率不匹配，排除免费scalar CM/Miller交织，相关水平Hom为零；该事实不推出canonical非零。下一须真正消费完整配对及费用，或回同一个M/R的实际Schur消元。geometry继续common A24与A18行，不重走已排gauge；不能用环境六阶矩填canonical授权。R1021两δ-new来源、R1022全39支、R1025六权和末两H组合、R953/954全混合界继续按已付范围；坏条件尚未迫所需单位组合为零。

## O相对 / O角：common A24、mixed 除 p 与完整 K/Y 方向

[R1055](results/R1055-original-a24-relative-fiber-and-complete-two-trace.md)已付原 \(T=A_{24}H_{48}\) 相对片的全 \(T_2\)、后继 \(T_\delta\)，准确剥出 \(R_{144}\) 的 old 部分。原 \(J_{1,p}/p\) 仍包含 degree12、两个明定 new 余项及低卷积；\(J_{p,1}/p\) 同时保留。要付余项的真实 finite 来源和原算术返回，不能免费交换 trace 与除 \(p\)，或从相乘关系推新的 \(J\) 零行。

R1040 的原模型/全 HJN 平均、\(\Phi_{126}/\Xi_0\)、G126/\(\Xi_1\) 和 \(J_{G,0}\) 单位保留；未授权 \(J'_G=0\)。R1046 的 K/Y 非零、R1047 norm25 的四 even 角色一次项及 Fuchs–Pham/全尾已付，canonical 坏尚不迫同一角读数零。

[原完整 unitary 字](notes/2026-11-27-original-y-k-rational-unitary-and-precise-p-level-words.md)的全部有限来源、逆Gram、两norm3150/150、六sigma、\(p^{1-n}\) 损、mixed cut、wild与补域均保。原§16已给真正球面 Hecke 反例：完整不读K边际恒零，而同一K/Y读数严格非零；这排“完整Y边际加该球面Hecke就迫K/Y零”。不重算该球面和。下一须真正读K的同解内关系、完整5-old canonical/reference 系数和5-new/p-new补项。

R1055附录现付同一个 \(H_{102}\) 与原四伙伴的全部有理关系：
\(\Phi_{126}^2S^3=\mathscr R\,T^4V\)、\(\Phi_{126}S=\mathscr Q\,A_{24}U\)。
全部有限极、charge、Gaussian和carry保持。实际 E3969 必要零行严格是这个同源唯一平方根的完整 Newton 加权行；下一须在原真实 Schur 行及同一个饱和修正中找到不可消约束，不能将 E 当第五自由高轴，也不由乘积推出新零条件。

## O几何：原54图的全局 normal function 与有权 Manin

原54/27图、η/Cor、最高λ、负9-Weil、两cover及Prym全保。R1039全Jac \(F^2=-q\)、R1041无权 \(q+1\)/半交不付最高加权影子。R1043需原三个完整J全零才给原T_a全p整除；canonical坏尚不迫此条件。Fr−unit核只有p个除点，不可改为全p²。

R1049完整 proper FP/Čech/Frob、全NS与CM Hodge、FL局部格均付：\(AJ(Y_{j0})=pI_{j,p}/(p+1)\)，原 \(h_{j,p}=a_{j,p}^{-1}I_{j,p}\)，log格为pO，模 \(p^n\) split iff \(h\equiv0\)。后继已给完整54有权限制、原weight-p CM来源、全type4 toric平方与 \(h^2\) 残余 canonical 平方，全部p损、period、factorial和Artin/full9保持；几何仍保 \(p>q_0\)。下一是这个真实完整和的无穷非零及原通常全Sha桥，不套任意 syntomic 非零或单点挠提升。

[R1057](results/R1057-original-manin-two-torsion-legendre-wilson-boundary.md)把同一原B的二挠 \(P_q(-1/4)\) 精确返回 Rodrigues 整数卷积；Wilson中央段加两短尾的完整Vandermonde和为零。辅助 \(q=6n+5\) 的所需无穷非零仍开，实正性不付模q非零；q单位倍规范Manin值不读另一个目标 \(p\) 的饱和。下一保原17/η/Cor有权返回或真正canonical除p来源。

R984 Griffiths非零不付逐p AJ；R988 K3–E0²和R990 CM17图零范围保留。R979固定7993 Selbal/strict核与R940全双新κ不判端点，Artin/fine Selmer及已核外部定理负边界沿完整归档，不重做已排输入。

R1053§12现进一步确定完整39核中source Z只在kerδ三点为零，余36点非零；不能由此赋P2(T)非零或删全native连接项。后继仍用实际非齐次配对及同M高尾。

## O厚点：v16 同一原完整厚图生产

**当前实际状态以文末v16 run46126639698为准；下列v13/v15与各软件记录保其原时点，不再表示v15正在运行。**

v13在05:00:05 UTC实际到21000秒，以signal15/exit124结束；完整终日志6357618B/hash7ee50ad82c605644b903739883a41b91fea88abbc3ffd2128e8c1f59301d198b已消费。九个非零scalar纤维阶段全返，原108/54断言已过；A0原MD完整Hermite只返189/306列，41770410次add，四交/Norm/18×9等终门未返。scalar-primary v2软件run46109939554/job140871011216真实PASS，保旧七组和实际projector包装器，结果hash82a97b808bd3ebb916b557065992379693a51089433274554a6ff5424d7b34f6。同一MD的完整U/坐标复用已通过软件v2；v15现接唯一heavy，全部原F_y专门验收保留。

[完整终日志记录](notes/2026-11-28-v13-terminal-and-whole-denominator-return.md)已替换运行中旧快照推断。全部65源、两char0 pins、29/2453/64/minimal/artinian与原数学门不改。下一隔离实现及固定公开软件请求已发布，使用固定Sage10.6官方全多项式HNF，返回实际H=U·MD及全部动态余数，再用同一H的原完整坐标C返回X=C·U、核X·MD=Y·MN；只适用A0 y0/A1 y0 direct endpoints，其它graph及原F_y的真实transpose-HNF验收继续旧路。固定27源软件v1因immutable失败，v2显式copy并核输入状态；v2 run46112089371/job140877645107已实际PASS，七对照/十拒绝/原F/scalar完整门保留，结果hash5f93581839237c9e532074ffcbd7fe263fdf8270ec6b14ff832311ff0538fefa。v15已实际建立run46112816717/job140879915022/sourcee959b4331bb9cd3871c9f05b101d47f2dba9e962；06:05:27UTC仍step4计算，日志BlobNotFound，尚无bindings/原数学回执；不扩大资源或以稀疏/半单影子代全非约化行模。

[原行运算全返回](notes/2026-11-28-original-row-operation-right-return.md)固定18源/420秒软件已实际PASS：run46115906757/job140889570559，结果23db4da527ebb64bc7feb06f8c7d30750bd24de700e653ec8f2200725cde0603；九完整CP/UM/余数比较、十三拒绝与实际Bezout/native全过，未执行原几何或rank306性能。完整Popov商/native循环性条件与D/MD的真实共同content候选保全部nilpotents，实际循环性/content与性能均未宣称，当前v15不改。

[完整Popov商候选](notes/2026-11-28-original-complete-cyclic-denominator-return.md)的固定21源/420秒软件已请求：所有δ标准单项式与Krylov列保幂零厚度，原last vector不cyclic则同M全算法回退；C/U/全原余数、content h^n及全部length恢复。14全比较/17拒错含96维幂零商已实际PASS：run46118066970/job140896222765，结果7c1504a43a9a52ea0dc8251dfd6a2387082dfbd284f697d095f88e235e58bdeb，21源码hash全核，5.736秒。该软件登记时原v15继续；现已终止并接v16，历史软件本身不代生产；接续须诚实分列原full reducer与实际tail phases，M0下降不冒原M全素。

软件与有限几何均不付主无穷p；旧q5/q11/全NS/Br/MW/Manin输入不重做。

## O4、O6、O7与所有其它原门

- O4：原O格 \(Q=\delta^a\varepsilon w\) 需无穷 ordinary \(p\) 有 \(a\le1\)；E17的a偶、E389的 \(\operatorname{length}\Sha_A=2(a+1)\) 不删。
- O6：固定两点饱和λ的全核 \(N_p\) 有限且真 \(q_p=1\) 于无穷p；原Tor、整周期及全部p损保持。
- O7：同解内/闭盘、同Y余数、全Laurent/非恒Y权及全部216管差仍未迫原闭边界全零。
- 原signed绝对整周期只在已付一K单位范围，不能外推跨p非零。全部热jet、半周期连接、paired Lamé/零p曲率不代原p−1及除p后p+1读者；不横向微分单个CM坏条件。

其余全部模型、来源、例外、数学门与失败记录保于开头逐字归档。子问题完成即接下一真实未闭门，达到课题README的完整标准才收尾。


O厚点后继：[逐实际来源返回](notes/2026-11-28-original-streamed-denominator-return.md)已完成隔离源码和固定34源小请求，真实P=E MD、全H/全余数、每个W_i/X_i及原两ideal全保。三个大临时产品全部换为逐全部行断言，X本身的输出风险仍有实际guard；原F_y不改。该固定软件已真实PASS：run46121926002/job140908102059，34源、9全比较/15拒错/4真实端点+4outer/2F及scalar均核；结果1ae2efddbb3dec8f17a8a004266efcb8a939db6da1653bb6ae82bc4414f4f55a。仅软件仍不付rank306性能或原全几何门，后继生产必须另付新outer method身份和四outer回执。v15已真实终止失败；见下列新终态，当前发布v16同输入后继。


### 2026-11-28：固定形式叶的全局费用已付

R1069固定原H=S34,1/Θ2,4913、Q形式叶D1+D4913及两模型微分。Hasse受限p幂准确在inert或17平方处封闭，四类密度1/4；全叶几何稠密r=2，Herblot全部定义/假设给α=1/4最优饱和。完整分母两Θ零陪集与分子最多有限交，原H极计数17πR²/area(Λ)+O(R+logR)，增长阶2。目标inert/square类已自动p-闭合；高斯平衡不降原Smith或canonical成本，仍消费全H_a加法核。 原bad所给B=A/T⁴的localized Euler正在同原Hall商上评价，须保x⁻⁴非交换连接；Pell作用须付整个H¹和所有实际极的边界。未将裸叶或自动曲率改记为canonical新增零行。


### 2026-11-28：Pell 轨道的实际有限维范围

R1069§§8–10支付A=[[33,8],[136,33]]的实际sigma/cube刚性化；P=[[1,4],[4,17]]把(34,−2)变为(2,−34)，AR共轭反射在全H¹为恒等，故A*=R*、全68维±空间36/32。固定原even S后两维全固定；负degree2的Serre微分负号保留。1/Θ两真简单极的边界像仅一维，准确pair(±1/2,0)、全主部边界0；A拉回的全部斜极支撑均保，未把cohom零/单极非零冒作原canonical行。 此层所有Pell幂仅给两种全算子，原S两维上全为恒等，不再把同轨道增加计作独立行。接续回同一H_a有限加法核及原中央/第一wild规范的真实读者比较。


### 2026-11-28：localized Euler 已完成原来源判别

R1067续证§§24–26付原bad的A/T⁴完整非交换Euler，精度p+1+4/(p−1)准确等价原未分歧a₂,a₃∈p²；所有第一wild标签给同一两条件。全native窗增至p+3，保新增−k₁h_Q,2、实际首连接及shifted V₁…V₅，不沿用浅模数消项。ν=1原两CM图/全部Euler给A(q_ac^{du}−1)=C₀17^{−(p−1)u}(J/J₀)²，完整a₃保参考/物理/逆参数；真实semi-linear inversion亦保共轭。全Newton尾给j₂∈p²，localized恰为j₁∈p²且j₁j₂∈p⁵，回同一g₁,g₂两槽，非额外独立forcing。 下一直接研究g₂和原首导数第二位的实质跨p关系，或消费原δ全源返回；不再以多标签、同Euler高层或新增4s累计独立收益。


### 2026-11-28 08:36 UTC：v15真实终态与v16接续

v15真实completed/failure：run46112816717/job140879915022，首306×306/d16官方分母HNF开始后未返回，08:24:51 UTC solver137；不以137判OOM。root核完整终log3987033B/hash9d6856f0ca3cc601d1b24e7241420259c71475f464c9e0df495b31a506a15e56，以及两原PASS/69源、9厚纤维支持、11primary、24residue、44operator。现按[完整v16来源与验收](notes/2026-11-28-original-streamed-shadow-production-v16.md)发布同一workflow的逐行返回：74源均核、全P/H/余数/content/每行XMD保留，四选定图加四post-ideal outer，原F_y与全部后门不变。小软件9.9秒不推断306性能，生产尚无PASS。 正在获取新run/job/source，后续只按实际完整返回更新。持续研究主无穷p门。


### 2026-11-28：原δ全来源已付，继续消完整角尾

R1068 §§10–14给原δ三同源上的完整有理核Rδ=D102/S34(δz)，准确约去(X+4)A3后仍保O二极、两三挠五极及全部其它有限极。全theta lift刚性化与原Haar dual给λε=λ∨，物理完整连接准确相消，原负二读数返同一S34的全部shifted槽，保(−1)^k(k+1)!、δ^(−2−k)、全部Δ carry、独立H+、old及全Maass。首p−1层完整Cartier矩阵为kδB−=R0B+δ+ΣRaS(d−a)δ，R6(0)=89/189单位；原bad没有赋其余角零。三挠点准确零阶还排除正则系数≤4阶Darboux代换，二阶若带极至少补三阶费用。 接续实际带极核的两非平凡三角色及完整Hall转置；有限三角色模块的自动零p曲率不代共同sigma连接的独立坏约束，不以局部两jet拟合做全来源身份。

v16已实际启动run46126639698/job140922574854/source0b550a6b1818b7875ceb5674fd8a8b2c080203b4，08:36:48 UTC创建；固定image已success、认证/计算step in_progress，首运行log尚不可读。唯一heavy仍等实际74源绑定/两原PASS与后续全几何门，不从静审冒PASS。


### 2026-11-28：实际 Lamé 两角色返回完成

R1068 §§15–18逐原两三挠字给a³=−(u+1)、b³=−(u−1)、ab=t及真正Lamé n=1系统，Wr=2，原q3 deck角色/非恒有理水平矩阵全部锁定。六个实际Weyl项全展开成指定E(t),O(t)，得到D102=C U0+B1 U1；两乘积各自为整L102 section，极分别由33/32重零支付，原点首4恰16/49与33/49。相同p² lift及中心给全translated式，负二保所有(−1)^k(k+1)!及kη尾，不重乘δ或dual相位；两个辅助项均未另授canonical零。有限三角色模块p曲率自动零只属其自身，共同sigma/原Maass仍保。 下一消费原g=2/x的固定有理dlog及原两项完整Hall转置，或实际非pull的同源伙伴；单项整首单位、有限模块零曲率都不替指定全和非零。


### 2026-11-28：原两槽的 Riccati 有限输入已付

R1067续证 §§27–28 从原 S34 的固定水平质量及同一 GM 方程，准确返回两个 Riccati 系数 E_N、E_d；g1=a_p E_N/p，g2=(p b_p E_d−γ a_p E_N)/p²。完整 CM 三重型和 étale 整模型支付 d−3 窗口，E_N 须保二次 log 至模 p³，E_d 保一次至模 p²。原坏后的两槽为 2γX−Y 与 Y−γX，未分别赋零。两半权核的全 mixed 卷积又返真实权一周期读者及完整残数；没有将 GM 周期代数化或把该读者认成未付的 crystalline 矩阵元。 下一继续同一共同分子的跨p关系，或在原有限参数cover上支付该权一残数的实际带系数 de Rham/Frobenius返回；普通全卷积不等于Hadamard平方，不丢混合项。主无穷p非零仍未闭，继续。

本地重新partial clone并实际pull两库已成功；根/课题四README未变、QUEUE认领行保持。后续每次推送前继续实际pull并记录读取提交。

### 2026-11-28：原固定权三类及完整 Hasse 缺陷已付

R1067续证 §§29–30 从同一冻结水平质量给原η⁴Θ_fΘ_g固定权三cusp form，准确GM比较常数−4π²iΔ₀^(−1/6)及Petersson/Stokes证明支付该具体parabolic类非零。相邻p/d读者仍保ζ^p与B^(−2)。全mixed式(140)在特征零保e_{m,p}、全部p·Bockstein和中点；g1∈p时Ed/p的下一位须取模p²，不能只用首降阶。原Hasse frame缺陷V满足完整受迫方程，首55/12及所需整窗已付；EN必须保ℓ̂/V全部二次混合至p³，Ed保ℓ̂+2V至p²。固定类非零、首V单位均未替代canonical无穷p非零。

[完整续证](results/R1067-original-first-wild-rubin-native-euler-continuation.md)，(134)–(146)。下一继续同一 moving 主部的实际 Spencer/Frobenius 比较，及原临界 Rankin–Cohen 全 theta 来源；不从非零固定类直接跳到指定除p矩阵元。

### 2026-11-28：原临界 RC 全源与真实 Fermat 余项

R1067续证 §31 逐原冻结γ/δ与所有34×2标签，证明实际半权Rankin–Cohen括号的精确周期规范；二项身份给Q√−17、模2𝔭17的完整68余类调和theta源，不删非primitive项。临界N=(p+1)/2括号在指定CM点真被p²整除，首商准确返回原完整低half卷积；两Frobenius符号分别给D(Hfg)与H(fDg−gDf)。在(-17/p)=-1射线，逐α恒等式的全Fermat差norm给H_(p+1)=68DτΘ+68^pDτ^pΘ−p²Ξ，c_N恰含一p，故保RC Fourier输入至p³。异权q同余仍需原同权E2/Hasse/Spencer和CM除p比较，不直接推出canonical非零。

[同编号完整证明](results/R1067-original-first-wild-rubin-native-euler-continuation.md)，(RC1)–(RC12)。下一消费完整Ξ与(140)/(145)–(146)的同一除p读者；保supersingular CM的Hasse零和全部异权/系数作用费用。

### R1067 §32：实际 Frobenius 行、全局 Cartier 核与完整两位差

[同编号完整续证](results/R1067-original-first-wild-rubin-native-euler-continuation.md)（F1）–（F16）从物理族整晶体给W=M⁻¹CM(t^p)及两归一底行，支付原EN/Ed全部p−2窗与首列除p精度；固定权三截面的两Serre类和真实微分迹准确返回原L_p/L_d，完整h与输出额外p保留。原参数E16的Cartier(ds/H²)=ds^(p)及指定Q_p付全局首层；在同一所缩étale图S=W22、G=W21/p及δ_R=(R^p−φ*R)/p为真实有限精度代数核，F13保p²微分误差，F15/F16保两/三位全部mixed并给准确trace。未把晶体非退化或固定类非零认成原共同分子非零。

### R1070：原同电荷 wild 正则迹、全开盘整逆与准确边界返回

[R1070](results/R1070-original-norm-one-wild-trace-and-integral-difference-inverse.md)在原E17、同一m=34/72、完整T_g/B_m和原j_m上取真实等范数η=A/Ā，Miller/原Legendre相位给Uη(ξ)^m=e_p(−mNormv)。实际p项平均消首边界极并保j_m；全部非平凡角色的正则补项保留。Volkenborn极限满足(Tη−1)Y∞=dlogη·W B_m；完整整位移Φη−W∈pWO+W^(p)O使M=(Tη−1)/W在每个闭r<1为整等距可逆，Y∞=dlogη M⁻¹B_m∈pO[[W]]。原j是同一解的原点值，首层全部值和全jet准确返B_m，所有Q^ℓ整除同等；完整p项CM迹的整像恰QO[[W]]，归一商亦整可逆。头两位只回原R710行，未从j=0推全Q整除；继续同源全角色测度及原period比较。

### R1071：原306维图的单右端、完整坐标核与流式全部返回

[R1071](results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)在同一原N,D/Apéry基证明D·W=qN的单右端确定提升，以及Y={h:hW∈qA}的逐真实坐标完整Hermite。每次失败由完整原残量及同一剩余域LU指出真不整坐标，至多306列严格终止；所有源行返回后才得完整配对图及两理想。原HNF各列次数Σσ控制完整Laurent窗，全部多项式部分返X后原残量准确deg<degM_D，可用完整低次幂零环核回，外门仍重验全部X。可选反向同算法给两真HNF及全多项式双包含，逐行生成X/T并保持原编码而不常驻稠密矩阵。射影极度2256给两图/两方向的分母及权分子同时≤2256、单右端提升总度>4512足够；不作速度保证。当前v16、原F_y与所有后门不变，尚无本新方法数值PASS。

### R1067 §§33–34：原共同分子的单迹一阶与不可漏的第三位尾

[同编号续证](results/R1067-original-first-wild-rubin-native-euler-continuation.md)（G1）–（G10）在固定分歧二盖直接构造相容Frobenius，有限多项式根窗保同一冻结f；两canonical分子准确为同一微分迹的一阶系数kγa_pE_N−pb_pE_d，完整relative系数与除p²费用保留。实际周期B/t的两惰性剩余类同源超几何给短多项式和全p²尾：Ed两位可删除该尾，EN三位准确贡献−3p²I_p/2，故原共同第二位须加−3a_p I_p/γ。尾中每项单位不代表经原f卷积后非零，前缀亦未删；继续完整固定尾的跨p几何来源。

### R1070 §§11–14：同一原中央的整测度、全奇导子与实际Hall归一

[R1070](results/R1070-original-norm-one-wild-trace-and-integral-difference-inverse.md)以真实D=Tη−1构造Cη(Σc_nX^n)=Σc_nD^n1，在每个闭r<1整等距可逆、保常数且交织X/D，得到L=Cη⁻¹Z、L(0)=j/(dlogη)、Cη(XL)=WB。全部primitive p^i点的轨道谱一重穷尽primitive p^(2i−1)根，原循环向量1使每个归一分母真非零，全谱插值保完整U权与B。原Q_i与cyclotomic两整商线性等距，逐全部层vL=vZ=vB，µ/λ也准确保留。首层再以R696/703/716原绝对相位及R1067物理ϑ⁶、√d接到同一Hall、Katz质量和首wild Rubin赋值；X读χ⁻¹而原twist读χ²，不偷换变量。更高导子的原Rubin period仍逐项支付中，尚未据此宣布主目标或新的λ上界。

### R1067 §§35–36：原第三位全尾的固定受迫周期与完整边界

R1067(H1–H7)把同一原p²全尾精确写为两固定3F2受迫周期，并将I_p还原到固定四盖上的同一fJb^(−5/2)乘子及x^(p−1)系数。实际GM forcing为两个有理一形式E±；两cusp的nilpotent留数及完整Hodge过滤各特征维数证明其完整上同调恰为边界一维、无parabolic分量。任意有限覆盖非零留数排除代数原函数；未删除实际f、未把整乘积断言D-finite、未从固定类非零推出原高槽非零。 [完整同编号证明](results/R1067-original-first-wild-rubin-native-euler-continuation.md)。
继续支付原完整低热卷积的Frobenius及全尾第三位，主无穷p非零尚未闭。

### R1067 §§37–38：原低热卷积与两节点的定向 Frobenius

同R1067(J1–J6)将原I_p全尾准确换成K_f=A^(1/2)f的低热行与固定受迫二阶原函数的完整卷积，所有所需分母在≤(p+1)/4窗为p单位。两实际cusp的最小三次模型经节点归一给b⁴=−18的奇函数边界，两个dlog各贡献一个p，完整分支和系数Frobenius给真实p²算子。仅在已证纯边界空间辨认该算子，不跳到原f卷积、j′或指定原函数值的本征关系。 [同编号后续全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。
下一支付全局过收敛比较及规范原函数的完整整性，继续原共同第二位。

### R1070 §§15–17：全部原偶导子周期与准确 Rubin λ

原范数17的完整CM gauge在两真实模型间交织同电荷谱；参考谱为整单位。全部primitive p^i点按2p^(2i)标签和完整Klein准周期给原深层Hermite/Klein向量，d·p^(i−1)个正交项经Yang完整归一正好产生p^(−i)，两模型原周期及signed局部估值取比后准确消去。故每个原允许角色vA_p(tν)=2v((λ−1)L(λ−1))，变量并未相认；用所有层及原µ=0得到µ(B34)=0与λ_p=2(1+ord_W B̄34)。没有仅由估值声称全函数相伴；无穷p所需几何阶数上界仍待证明。 [同编号全文](results/R1070-original-norm-one-wild-trace-and-integral-difference-inverse.md)。
继续真实中央Newton与全部Hall权germ的同谱身份及原B̄几何上界。

### R1070 §§18–20：原中央与Hall的同一整权函数及准确间隙

真实原点jet/全部挠点Hermite泛函在Tη下分别本征η^k、λη^k，Cη循环性给非零参考和。原J谱满足J(η^(du)−1)=17^(−1)(17/a^d)^u J_p(u)/J0,p(u)，原完整首Hall权亦为同一J的λ附近germ，全部Klein、T_g、aϑ和步长因子保留；没有复活已否的普通阶乘cross延拓。结合R707原高度，非零首Hall迫λ_p=2(p−1)v(T_H)≤(3/2+o(1))(p−1)；首Hall零则λ_p≥2p，原中央坏时≥2p+2。充分大p首Hall零恰等价λ_p≥2(p−1)，仍未选择其中分支。 [同编号全文](results/R1070-original-norm-one-wild-trace-and-integral-difference-inverse.md)。
下一全层绝对period与原Rubin整平方、实际模p几何阶数；原中央simple仍须证明。

### R1070 §§21–23：全部绝对常数与原 Rubin 整函数的平方

原Klein准周期和完整Miller核证明每层真实单位剩余阶整除8；同模8且norm趋17的实际CM元因此精确给D_a=s1/s17^17，全部谱坐标常数消去。复共轭及ā/a=ζη^s给J_ā=(1+X)^(−s)J_a。BKO Prop3.1的同一原椭圆单位类、实际Betti/CM周期及deRham自然性支付原A_p有限值，含ϑ^(−1)和完整primitive Euler；真实Artin整变量τ(T)=(1+T)^(−1/b)−1后，以整有界性及全奇层无限特化得(A_p)=(J_a∘τ)^2于O[[T]]。所有非算术权零点亦偶重；原中央及首Hall是否消失仍未由此决定。 [同编号全文](results/R1070-original-norm-one-wild-trace-and-integral-difference-inverse.md)。
继续从同一实际B̄阶数、全平方与固定几何来源证明所需跨p非零。

### R1067 §§39–40：同一全球 Frobenius 差与实际整段共振

固定曲面两个I12边界的常系数rigid/log比较，加真实光滑proper相对H¹及自然Frobenius，给同一E−的F[E−]=p²υ[E(e)]；g特征排除零处自由常数，准确返回T=W P5(xp)−p²υPe。完整Ip从T2/p²已整低窗回到原全f。7p首分母的阶乘与CM常数准确消去，整个A共振段至<11p+4均可除p²；下一首双分母单位再次相消先给p，不据此宣称全图p²整或canonical非零。全球比较仅多删固定有限坏素数，逐系数段仍对原全部好p成立。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。
继续全图整除p²及同一原primitive的有限极部返回，保全EN三位/Ed两位。

### R1071 实现：完整单右端坐标图的独立软件 PASS

原32源固定请求在公开run46137528591/job140956064113、source4bb9fbcebbb160796da11f08c5d2b7eef4741b44完成。root和代理独立逐完整终日志核8个完整图比较、两厚例必要细化、2次已造ideal后多项式部分篡改及2次真实预算拒绝、真二次底素/模块转置，实际7.582517183秒。完整log31915B、fixture296B、public4645B及各SHA和全部来源保于运行注；不存可重算输出。软件输入PASS，不代306生产或通常全Sha。 [完整运行来源](notes/2026-11-28-original-adaptive-scalar-graph-software.md)。

### R1067 §§41–42：全图两位整性与唯一完整极部多项式

同一原E−的实际两开Frobenius提升与晶体Taylor积分各支付两位p；从固定level3通用log晶体拉回下降、原格比较和proper log复形一次无扭，将有理Frob身份提升为全V上的T/p²整截面。其第二分量模p在所有branch极≤2p、两个cusp零≥1，严格给M_p=x^(16−e)L_eΠ/(1−w)^p、degΠ≤p−1，任一branch整个主部唯一恢复Π。原Ip返回保全f、Hasse低窗与两/三位前缀；适用范围明确再删固定有限模型坏素数，不将端点或长窗代原canonical非零。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。
下一完整支付单branch原初值与全部主部，继续两canonical共同第二位。

### R1067 §43：单个 j=1728 主部的原初值与共同第二位

以真实j1728纤维的i作用、det W=p及原Hasse/DH给所需除后首列的准确初值；完整低p水平递推与真h奇偶付e11额外Y^p项。原换提升的两项Qc及Qc²分别以384、8·9216常数恢复整个Π，任一分歧标签都返回同一全局多项式。M6将全Π送回冻结f完整卷积的Ip，M7保EN0三位/Ed0两位并回两canonical的k=1/2及原符号。Π(1)只读端点，未将其q_c条件偷换为原共同分子非零。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1067 §§44–45：原A两位与S三位的完整分歧重建

原Gφ=W21/p在所有有限模p^r下降Y直线且两cusp处消失，任一分歧严格主部唯一恢复；两位Taylor只需真实单位第二列的低p窗，其未知CM提升λ在Gφ/Gφ(P0)精确消去。原第二列S与8p²x^pM的换提升差一致，全球cusp极界及g/h特征迫剩余为−u t L_eP_m，给全V三位等式。N5因此把EN三位、Ed两位都写回冻结f与完整分歧主部，N6仍保两canonical原单位/符号，跨p非零未证。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1071 §9：真实A0正端与公共零方案

同次v16原A0共权12及两完整306 Popov的det度3670，给D∞在整纤维零长2、标量content1。原四∞点及原椭圆方程迫每个可能极为有理单极；R899原π1 germ确定e=1点真单极，因此U恰1、P∞∈{1,2}，有限公共零长1415或1416、全球1416。逐实际LRU代码的整数j单键及细化对角单调，所有驻留窗口系数≤1251846<2000000；不含整X/临时引用/Dixon/RSS，也未宣称图已生成。 [同编号全文](results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)。

### R1072 §1：原完整反圆分平均的显式无根区间

对每个固定ε>0及充分大的原惰性p，令D=φ(p+1)/2，所有i≥(1/2+ε)D的确切阶p^(2i−1)原扭曲均非零，因而原A与B34在这些整层无旋分零。证明保持同一X=(51/π)p^(2i)的完整primitive差；非六次单位方向以相对范数给短向量下界，六个真短线逐一支付，primitive首线及其余格线给一致误差。实际平均趋18π/(17√3)>0，再用未分歧基上同层Galois传播。未由深层非零推中央simple。 [完整证明](results/R1072-original-toric-conductor-cutoff-and-quadratic-moments.md)。

### R1072 §§2–4：原小整数行、准确λ阈值及真实二次矩

原全tame整数行在每层均偶且|A_i,u|≤2(p+1)/3，旋分整基与小代表给非零原P_i严格v_p<1。BHKO Th3.12的真实双线性平方、完整旧项消去及Th4.14–15原period给v(P_i)=v(A_p)+S_i/D_i，故P_i非零恰λ_p<D_i−S_i，零层构成初始段。§1遂给无条件有限λ界；首层插值度恰p−1−λ，λ=2恰原Σu²A_1,u modp非零，原通常Sha桥适用。Weil弧界另给真√p节省；未把µ0或固定行界当中央非零。 [同编号全文](results/R1072-original-toric-conductor-cutoff-and-quadratic-moments.md)。

### R1072 §5：完整原相位的正下界与对数截点

原primitive方向的完整坏位相位在分裂素理想自由群上确为角色；短同步子群不需饱和，以真实tame像注入控制其秩。不同素坐标Poisson测度推前及卷积给同一原相位的严格正下界，保全H_2i与H_(2i−1)两组不同子群和全部长方向误差。统一非零截点缩至i≥100 logp/loglogp，遂log(1+λ_p)≪(logp)²/loglogp。没有排除首层二次矩或中央重零。 [同编号全文](results/R1072-original-toric-conductor-cutoff-and-quadratic-moments.md)。

### R1067 §§46–48：原全部同源Fourier行与径向三位

在固定无穷ray p≡−1 mod(68·6²)，原两unary theta的全p+1同源Fourier向量满足真实Paley本征式；signed Singer精确配对两tame模式。原目标标记、∞同源负号、双格Γ68下降与g(P)=1的Reed–Solomon唯一符号支付所有相对平方根。整形式群旋转及同一水平晶体将全变形jets接回物理EN/Ed；P14在g1∈p时给EN=−u0 c Ed−u0 c²c2d/3 modp³，P15返两canonical。保完整径向二阶及原相位；尚不判该行跨p非零。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1067 §49：原参考确定径向常数与第四物理权

原degree-two参考在同一整旋转框架精确给κ=−(pcσ)²、c/p=−1/κ及γa_pu0 c/p=−b_p；三位原共同分子无未识别单位。将c2d完整换回第四物理权E2d，得到Q6两canonical的准确Ed/p、E2d组合。其条件与原Gaussian两位相同，不重复计作独立强迫；全变形P9继续保留。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1072 §6：原全导子的固定绝对截点

将真实有限分裂Euler多项式乘入原Mellin平均，逐primitive方向完整消去小分裂因子；截断p^512、短窗p^4、粗素阈(logp)^8共同支付径向误差与全部长尾。同向primitive理想乘积的真实tame注入给粗短方向的绝对小界，从而对充分大惰性p及每个i≥1000，原确切导子p^(2i)全部L值非零，原λ_p<p^1999。未调用µ/λ来证明非零，未从深层无根推出中央非零。 [完整证明](results/R1072-original-toric-conductor-cutoff-and-quadratic-moments.md)。

### R1067 §50：同一原关系的互补二次射线

原平方theta的Γ68下降及全部目标标记使M=68已足够，同一全Paley/径向/参考公式适用于无穷子列p≡137 mod204。此时物理j=0仍超奇异，辅助Q(√−17)分裂；∞原同源取正号，σ=1与G²=p完整代入，Q6两canonical不变。分裂性只决定可用原展开，不自动给中央非零。 [完整同编号证明](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1072 §§7–9：原中央非零的有限层整数证书

BHKO真实signed归一与R1070精确Artin比给Θ17²=C*Θ1²·A·A∘ι，原rank-zero参考Θ1整单位；全BT整数递推准确构造Θ17。完整二次矩M_i=Σu²A_i,u满足(−1)^i p^(1−i)M_i≡2[T²]Θ17 modp^i，故原J′非零恰某有限i有p^(2i−1)不整除M_i。原整平方进一步给中央赋值2r、首次检出恰i=2r+1；允许首层未检出，不要求全Brandt行消失。仍须证明无穷不同p检出。 [完整证明](results/R1072-original-toric-conductor-cutoff-and-quadratic-moments.md)。

### R1067 §51：全部变形阶的真实首剩余范围

Moore行列式恒定及全根幂和准确解出原Paley两径向块的全部Z阶共同首剩余：次数≤h时R3是同构，h<r≤d−2时核恰(1−x)^(h+1)倍数。原j1坏、j2/p²单位对应的真实R4二次剩余与所有变形阶相容，故在该首剩余阶继续增加jets不能造矛盾；未宣称任意剩余可提升为原特征零模函数。下一位完整pC及原全局来源仍保留。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1071 §10：原两图的权13整基及21阶厚纤维

真实G_m=H0(mP∞−P)、g559/degP∞306/degP2256给G13维1164并生成整个原图；带权领先矩阵付反图全部s饱和，306行权≤13且总和3120。一个D可逆的原厚纤维只需底总度21，零极完整次数比较即准确恢复G13；保3420未知量、3006约束和原全坐标回代，不以约化点替厚度。低权投影的完整多链Hermite及原两ideal/全X outer均保，实际返回306行还可用RR维数独立认证。尚无本方法实际软件或306生产PASS。 [同编号全文](results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)。

### R1071 §11：完整多链返回接口与逐行驻留界

亲读原完整列Popov、全厚商乘t、δ=0尾、素域admission及真实坐标回代，给各原域的多链全关系和HNF双包含。原任一负源canonical行的全部X至多691866个原域系数；反向独立用零除子。不可变内表示与post-ideal实际两理想各自解出整条X，逐多项式比较并重验全N/D，不以摘要或低次残量代全等式。仅静态接口与证明，未新增软件/生产PASS。 [同编号全文](results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)。

### R1072 §10：原中央首矩的完整调和theta来源

R736真实模p²像线与(28)的符号给原二次矩的整格点多项式，四维全调和投影在整个Q=p²壳保模p³。得到固定层级3·102²、权4p−2的真实尖点形式f_harm，m2=(34/δ)²[q]T_p²f_harm/(36p²) modp；全部2/3/17、12·3重数和非primitive点均保。需要读p f_harm模p⁴，单纯模p约化不付该矩非零。 [完整证明](results/R1072-original-toric-conductor-cutoff-and-quadratic-moments.md)。

### R1072 §§11–12：固定权六首影与完整权二Hecke线

原完整调和theta的p倍模p约化准确为−θ^(p−3)F6，固定权六F6保全部坏位且不预设非零。更强地p^-2T_p²f_harm在p整，全q展开模p落原E17权二新形式线，标量为36(δ/34)²m2；复合范数全部右ideals、非cyclic局部格、BT深二祖先与原X^-消失均保。本征线不强迫标量非零，仍须无穷p原矩检出。 [同编号全文](results/R1072-original-toric-conductor-cutoff-and-quadratic-moments.md)。

### R1072 §13：所有中央有限矩的原权二oldform配对

任意s=2i的原模p^s完整矩阵像线、wild原整数代表u²给真实权二theta，特征零全部q展开准确等于36M_i f_E17(p^s z)。完整右ideal、primitive深s祖先及原X^-父点支付所有系数；同层Petersson配对商就是原整数M_i，故p^(2i−1)不整除的有限证书被原权二配对精确实现。未以复配对非零或固定本征线替代p进中央检出。 [同编号全文](results/R1072-original-toric-conductor-cutoff-and-quadratic-moments.md)。

### R1073 §§1–2：固定E65/E8125原类配对及有限中央证书

固定E65与E8125=5³E65的原Hecke角色差是(Na/5)，实际390导子及5/双13 uniformizer值全部保留。同一原E1单位类精确给A_b(tν)=L_bν/L_1ν，两个真实范数支P±=(A65±A8125)/2。完整奇层Lagrange整余式D_i,±≡[T²]P± modp^i，因此两固定曲线至少一条原中央非零恰某有限证书vp(D)<i；若无穷p检出，固定二元族可用鸽巢。未证明该无穷检出。 [完整证明](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1073 §3：原CM实下降与单一范数支无抵消

原Kronecker完整余类和、CM Galois标量和参考5/双13原Euler给w_b=θ_bL_bν/L_1ν的准确实旋分下降；θ_bA_b的系数共轭等于原倒数T作用。质量/一次项已为零，故u_b=θ_bA_b,2在Z_p。于(5/p)=−1的惰性素数，两个原范数支的中央估值均恰等于min(vA65,2,vA8125,2)，排除配对抵消；单一加号有限证书足以检测该固定二元族。Yang实非负仍不代中央p进非零。 [同编号全文](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1067 §52：九条实际标记同源与三个原中央分支

原R290/R292/R302全部2与17处相位给九条有标记17次同源的精确Jacobi分解，目标端环皆为O17。实际µ3分成三个不同中心，八列Fourier子式与第九竖线独立，原S1不变迫全部系数的准确置换。每支仍为完整物理degree34代数截面并付同一Tate尾，原Jp=3(J[H∞]+J[H13]+J[H1])；中央坏只迫三导数相加零，不将单支换成新Rubin或Selmer来源。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1073 §4：同一二阶的有理数及固定实二次域证书

在原倒数不变参数S=T²/(1+T)中，θ_b sym(A_b)=S H_b且H_b∈Zp[[S]]。全部真实奇层实节点给有理Lagrange数R_bi≡θ_bA_b,2 modp^i，合并后位于同一固定Q(√5)；范数vp<2i正好检出固定二元族。首层完整实迹又给非负有理V_b,p≡−(p−1)θ_bA_b,2/2 modp。复正性和固定数域均未控制其p整除；原参考L分母仍完整保留。 [同编号全文](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1067 §53：三个真实目标周期与两个完整单位读者

真实Vélu微分和sigma加法式给九分支的目标二次指数及全部八个17挠点贡献；原参考theta零会迫目标j=0，故九个原质量均非零。三个目标c_D=17c+e_D、e_D整，原读者J[H]=r_D^u I在全Tate盘准确成立；由三质量和零，中央J′/3=B1(logV1)′+B2(logV2)′。两个单位保完整目标自带导数，所有整数权取真实物理系数比，未把其极限当单个全局代数数的p对数。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1071 §12：完整短厚图与多链的小软件实际 PASS

source6b17ab13cc4d1d38b4854403e5abf9ab471e7bd3/run46145004405/job140978975713的两小checker及独立host实际PASS；43源/同container/资源与完整输出均由root和代理独立核验，8多链+14双图、全部拒绝及真二次π²通过。首轮环境失败保留，不代306生产；v17仍运行。 [完整来源](notes/2026-11-28-original-short-global-graph-software.md)。

### R1067 §54：三实际目标的固定S3域及原中央反射迹

原九核是十七范数平方半集，其内在Heisenberg偶线及S1有理性使G_Q√17准确置换三个物理Zi，质量比Bi/Bj非有理。辅助13三循环与复共轭给实际S3域及唯一二次子域FK；两原射线的p处Frobenius反射把原J′准确化成V3的Qp²迹。迹零仅给反不变线，有限全局代数对数身份未付；原目标导数全保。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1067 §55：实际Gaussian对数和在全部充分大惰性素数非零

原三目标格的最短向量严格区分c_i，再用质量比无理及Fuchs–Pham的p进对数线性无关，证明真Gwt=ΣBi logri非零且超越。原中央完整等式为J′/3=Gwt+ΣI_i′，故尚须排除目标导数总和的精确超越抵消；有限整数权对数的非零不提供极限下界。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1073 §5：原参考全层清分母与正整数中央证书

同一原signed参考的绝对平方U为整单位，消去全变层L分母；固定七乘法及全部原torsion来源给统一固定分母D。完整奇层实Lagrange权加真高迹倍数后严格为正，所得普通整数I_bi≡−DU(0)u_bmodp^i；(5/p)=−1时Ni=5I65²−I8125²的vp<2i准确检测固定二元族。Ni最终非零，但已付普通界Cp^(20i)尚未压过p^(2i)整除，未据正性完成主目标。 [同编号全文](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1071 §13：原A0真实素域分式与每一步完整附块度帽

原A0被逐常数Frobenius固定，原N=N0+αN1、D=D0+αD1的同号非零分量满足NiD=NDi；两图按原权12交叉回核后可在F29求同一个G13，再全原域/原N,D/完整外门验证。真实好不可约π度≤3，厚总度21/22；原D的3670度及其纤维单位不转嫁。有限图U1还严格限制每个Popov旧行、商乘行及更新附块次数≤18，不仅最终行；不作RSS或执行PASS主张。 [同编号全文](results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)。

### R1071 §14：原U17点和准确确定两直接有限图的正负长度

原特征零U17整映射恒等式与全部18尖点标号，结合原A0的两度8处D∞单位和16点F29轨道，迫厚尖点像−T、全部中间像T。三原Artin映射保相同有理三挠值，唯一薄点真单极。因此两直接有限图负长度2255、正长度2256、U1；原A0有限公共零1415、无穷公共零1。没有在正特征由微分零推出常值，反图仍另付。 [同编号全文](results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)。

### R1073 §6：三个固定有理函数的全Katz与有限群环原身份

固定原G_k由七乘法及完整6/390角色平移给出，所有真层L值为同一G的完整点轨道；全p核迹给ψG=−G/p、g=pG+G∘[p]及原整Katz测度。保归一(−p)^−s、平凡项(1+p^−1)、反号层及真实参考，全部有限群环严格满足D_b,s=65A_bD_1,s。原中央坏遂迫每层同一来源T四次整除；未从ψ0或全层身份宣称中央非零。 [同编号全文](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1071 §12：短厚纤维完整两图的生产接续

R1071§12接续：85源v18把同一软件PASS的六模块接回两原端点/四完整图，全部后理想原X与既有下游均保；实际Sage线程与凭据边界由host验证。既有heavy group取消关闭，等待v17；尚无实际生产返回。 [完整生产来源](notes/2026-11-28-original-short-global-graph-production-v18.md)。

### R1071 §15：原A4商和反图三倍极的完整回接

三条原映射逐特征零等变下降到X0(289)，两个物理端点在Z=X0(1156)均为度564。Y→Z忘3度4非Galois；u=(t⁴+18t²−27)/(8t³)及各完整纤维给反图负2253/正2256/U3、配对20次帽。原商整基尚未执行。 [同编号全文](results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)。

### R1071 §16：全部原九点的四次商与厚拉回

实际F17和两个端点同降V4商，当前四交度39840→9960且九点均为商点[4]推回，5/7 Tate的4为单位。原xout的c因子全消，非约化拉回Norm须保multiplicity；旧T/v/辅助分割不逐项下降，18×9仍逐块付。 [同编号全文](results/R1071-original-single-rhs-adaptive-integral-graph-and-streamed-return.md)。

### R1067 §56：原Kummer三扭曲的真实Fourier分量

真实六次域K(17^(1/6))给三投影9Zi=S1+ω^i aH3+ω^−i bH5，保实际两个秩零来源的全部系数与period。a/b=17^(1/6)/(3+√17)>0，原theta估计定两项同号，未由普通权非零推出原中央。 [同编号全文](results/R1067-original-three-target-units-and-integral-isotropic-source.md)。

### R1067 §57：两个原秩零单位与任意精度有限对数读者

实际U=(A3/A5)/(A3/A5)(0)有唯一归一平方根R；三目标导数保真实Y′和J′两个分量。BKO Th3.16与完整全层Lagrange给R′的任意p精度有限全局elliptic-unit对数读者，未将其极限冒称有限全局对数。 [同编号全文](results/R1067-original-three-target-units-and-integral-isotropic-source.md)。

### R1073 §7：全盘原Volkenborn差的整可除性

三固定G_k真实有理下降；开形式盘Volkenborn差精确为log_E·h，h整且ψh=−h。原全权读者保N M_(N−1)h和准确period损失，不能把首阶精度冒称中央二阶精度。 [同编号全文](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1073 §8：原权一来源的整Morava恒等式

固定全水平权一来源、全部p^s循环商和原微分给PΔ f_b=65A_b(Tη−1)PΔ f1。作用来自p-divisible群，非全局椭圆自同构；完整准典点无限与有界WPT证明整盘身份，原反号层保留。 [同编号全文](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1073 §9：固定dR系数的任意精度原中央读者

固定族Ev及水平e0/e1给c_b(n)=65A_b(ρ^n−1)c1(n)，保原微分和形式中心。所有所需同余类有无限非零参考，真t_n²商到任意p精度；两中央坏迫逐权四阶整除。 [同编号全文](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1073 §10：每层唯一指定权的原参考准确估值

全PF递推及整个原半径系数界给vp c1((p+1)p^a)=−p^a；原中央比精确modp^(a+1)。两坏需vp c_b≥4(a+1)−p^a，首层为p³，不把参考非零代目标非零。 [同编号全文](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1073 §11：三个真实Hasse lift的完整三位系数

固定三次族的真实A_r/B_r、三点整数插值给U/V完整modp³窗；目标常数零允许截至k−1，参考不能漏第k位。指定局部Cartier及固定特征零ℋ_b读同一原c_b(p+1)，不冒称参数无关modp³算子。 [同编号全文](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1073 §12：两个真实五同源类的原三位拆分

完整78父源与原5标签给c65=−3(c+−c−)、c8125=−3(c++c−)，两中央坏同时杀两个实际CM类三位读者。保μ3投影、原2/3/双13和准确负号，未给父源额外rank1身份。 [同编号全文](results/R1073-original-fixed-quadratic-curve-pair-and-central-certificates.md)。

### R1067 §58：三个实际投影的绝对系数及Pell范数

原R298/306/307的同一period与平方常数准确给b=−1/(168θ²)、a=−1/[168θ(3+√17)]；原首系数theta界定绝对负号，全部三质量积含固定4+√17，不是新权指数。 [同编号全文](results/R1067-original-three-target-units-and-integral-isotropic-source.md)。
