# 结论索引

### 连续几何比较的范围更正及离散障碍（2026-11-27 21:55 UTC）

[完整审计](notes/2026-11-27-original-psi4-common-factor-digit-and-continuity-audit.md)证明：$A=p^2-1,B=p-1$ 与任意固定非零 $K,\zeta$ 下，$g(u)=K\zeta^u((Au)!/(Bu)!)^2/(Au-1)$ 不可能将两个非零连续函数在全部正整数相接；$u_0+p^m$ 的精确估值差为 $(v_p(\zeta)+2p)p^m-2$。原未除幂 Hermite 的 $n!(n+2)!$ 独立保留。实际纯固定幂toric比较仍须核定，不由此宣称书定理反例。

Kriz7.20尚缺本题两个截面的共同连通延拓或真实flat/depletion交织，7.21另需运输评价点与定义域，§9.3负端点primitive还需同一微分/Frobenius归一。故此前旧full54、新六线、新psi4的连续几何cross、H−2/AJ及共同几何F单位登记**均改为明确条件陈述**；本更正优先于下方历史条目。全来源/正整数权、完整图/Artin/p²和直接proper-fp、纯Newton全尾、独立R1049残余及既有signed范围不自动撤回。三个原文件已同步页首更正；下一固定正权精确证书及真实算子比较继续。

所有条目均为已证明的中间结论，主目标尚未完成。编号缺席不表示已完成。

按根规则15，可重算输出只由[脚本、参数、run和hash](notes/2026-11-15-recomputable-output-provenance.md)追溯；不保存可重算日志或结果数据。

## 完整历史与证明分卷

- [本次整理前完整索引](notes/2026-11-28-results-index-before-norm-one-measure.md)：逐字保留截至R1070的全部原条目、更正、原证据及更早归档链。

- [截至R950的完整旧索引](notes/2026-11-26-results-index-through-r950.md)。
- [本次整理前完整索引](notes/2026-11-27-results-index-before-original-inert-residue.md)：保R951至R1049§10的全部条目、更正、真实运行回执与归档入口；因文件接近100KB而移出，本次未删除任何结论。
- [R901–R950](notes/PROOF-INDEX-R901-R950.md)、[R951–R1000](notes/PROOF-INDEX-R951-R1000.md)、[R1001–R1050](notes/PROOF-INDEX-R1001-R1050.md)、[R1051–R1100](notes/PROOF-INDEX-R1051-R1100.md)。
- [当前实际门](open.md)和[交接](HANDOFF.md)保同一原来源、全部未付条件与接续分工。

## 当前新增结论

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

### R1067 §§37–38：原低热卷积与两节点的定向 Frobenius

同R1067(J1–J6)将原I_p全尾准确换成K_f=A^(1/2)f的低热行与固定受迫二阶原函数的完整卷积，所有所需分母在≤(p+1)/4窗为p单位。两实际cusp的最小三次模型经节点归一给b⁴=−18的奇函数边界，两个dlog各贡献一个p，完整分支和系数Frobenius给真实p²算子。仅在已证纯边界空间辨认该算子，不跳到原f卷积、j′或指定原函数值的本征关系。 [同编号后续全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1070 §§15–17：全部原偶导子周期与准确 Rubin λ

原范数17的完整CM gauge在两真实模型间交织同电荷谱；参考谱为整单位。全部primitive p^i点按2p^(2i)标签和完整Klein准周期给原深层Hermite/Klein向量，d·p^(i−1)个正交项经Yang完整归一正好产生p^(−i)，两模型原周期及signed局部估值取比后准确消去。故每个原允许角色vA_p(tν)=2v((λ−1)L(λ−1))，变量并未相认；用所有层及原µ=0得到µ(B34)=0与λ_p=2(1+ord_W B̄34)。没有仅由估值声称全函数相伴；无穷p所需几何阶数上界仍待证明。 [同编号全文](results/R1070-original-norm-one-wild-trace-and-integral-difference-inverse.md)。

### R1070 §§18–20：原中央与Hall的同一整权函数及准确间隙

真实原点jet/全部挠点Hermite泛函在Tη下分别本征η^k、λη^k，Cη循环性给非零参考和。原J谱满足J(η^(du)−1)=17^(−1)(17/a^d)^u J_p(u)/J0,p(u)，原完整首Hall权亦为同一J的λ附近germ，全部Klein、T_g、aϑ和步长因子保留；没有复活已否的普通阶乘cross延拓。结合R707原高度，非零首Hall迫λ_p=2(p−1)v(T_H)≤(3/2+o(1))(p−1)；首Hall零则λ_p≥2p，原中央坏时≥2p+2。充分大p首Hall零恰等价λ_p≥2(p−1)，仍未选择其中分支。 [同编号全文](results/R1070-original-norm-one-wild-trace-and-integral-difference-inverse.md)。

### R1070 §§21–23：全部绝对常数与原 Rubin 整函数的平方

原Klein准周期和完整Miller核证明每层真实单位剩余阶整除8；同模8且norm趋17的实际CM元因此精确给D_a=s1/s17^17，全部谱坐标常数消去。复共轭及ā/a=ζη^s给J_ā=(1+X)^(−s)J_a。BKO Prop3.1的同一原椭圆单位类、实际Betti/CM周期及deRham自然性支付原A_p有限值，含ϑ^(−1)和完整primitive Euler；真实Artin整变量τ(T)=(1+T)^(−1/b)−1后，以整有界性及全奇层无限特化得(A_p)=(J_a∘τ)^2于O[[T]]。所有非算术权零点亦偶重；原中央及首Hall是否消失仍未由此决定。 [同编号全文](results/R1070-original-norm-one-wild-trace-and-integral-difference-inverse.md)。

### R1067 §§39–40：同一全球 Frobenius 差与实际整段共振

固定曲面两个I12边界的常系数rigid/log比较，加真实光滑proper相对H¹及自然Frobenius，给同一E−的F[E−]=p²υ[E(e)]；g特征排除零处自由常数，准确返回T=W P5(xp)−p²υPe。完整Ip从T2/p²已整低窗回到原全f。7p首分母的阶乘与CM常数准确消去，整个A共振段至<11p+4均可除p²；下一首双分母单位再次相消先给p，不据此宣称全图p²整或canonical非零。全球比较仅多删固定有限坏素数，逐系数段仍对原全部好p成立。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

### R1071 实现：完整单右端坐标图的独立软件 PASS

原32源固定请求在公开run46137528591/job140956064113、source4bb9fbcebbb160796da11f08c5d2b7eef4741b44完成。root和代理独立逐完整终日志核8个完整图比较、两厚例必要细化、2次已造ideal后多项式部分篡改及2次真实预算拒绝、真二次底素/模块转置，实际7.582517183秒。完整log31915B、fixture296B、public4645B及各SHA和全部来源保于运行注；不存可重算输出。软件输入PASS，不代306生产或通常全Sha。 [完整运行来源](notes/2026-11-28-original-adaptive-scalar-graph-software.md)。

### R1067 §§41–42：全图两位整性与唯一完整极部多项式

同一原E−的实际两开Frobenius提升与晶体Taylor积分各支付两位p；从固定level3通用log晶体拉回下降、原格比较和proper log复形一次无扭，将有理Frob身份提升为全V上的T/p²整截面。其第二分量模p在所有branch极≤2p、两个cusp零≥1，严格给M_p=x^(16−e)L_eΠ/(1−w)^p、degΠ≤p−1，任一branch整个主部唯一恢复Π。原Ip返回保全f、Hasse低窗与两/三位前缀；适用范围明确再删固定有限模型坏素数，不将端点或长窗代原canonical非零。 [同编号全文](results/R1067-original-first-wild-fixed-geometric-tail.md)。

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

### R1067 §59：真实中心比的新素因子与有限period判据

三原Eisenstein比在大权模任意固定S-unit保持秩2；完整高度/最短向量/Matveev与S3证明后，Fuchs–Pham排除其对数与有限全局单位及阿贝尔点period的关系。只有目标余项进入该有限空间时才得原中央非零。 [同编号全文](results/R1067-original-three-target-units-and-integral-isotropic-source.md)。

### R1067 §60：全部目标导数的一重完整过收敛积分

有限period障碍扩到S外循环群相对紧的一般交换代数群；同一三目标Newton/Borel转换给ΣI′=−∫₀¹D(−t)dt/t，两个端点正则。被积微分未证明代数，不能免费调用广义Jacobian对数。 [同编号全文](results/R1067-original-three-target-units-and-integral-isotropic-source.md)。

### R1067 §61：全三目标resolvent的准确复增长阶

原完整M的复整函数阶恰2/(p−1)，在复无穷本性但p进端点正则。证明保每个真实格和全部最大曲率项，磁平移全圆盘均值消去交叉项；不排除端点值另有period表示。 [同编号全文](results/R1067-original-three-target-units-and-integral-isotropic-source.md)。

### R1067 §62：真实双Jacobi分裂迹与完整纯轴整性

模68射线有联合无穷原惰性p；完整双变量Hecke保所有标记、非primitive和目标Gaussian。固定K=S1G(√−17 z)在原t盘t⁶Zp[[t]]整，来自全部整除法逼近；原J′仍保G的完整倒数。 [同编号全文](results/R1067-original-three-target-units-and-integral-isotropic-source.md)。

### R1067 §63：原纯轴的真全局单位值与范数关系

每个非零p幂挠点的同一K值都是全局S∪p-unit，实际估值6vp(tQ)。整数幂/Teich消除给严格代数性，原完整六组挠除子给全p²范数，不以未证极限单位性或单位非零代中央。 [同编号全文](results/R1067-original-three-target-units-and-integral-isotropic-source.md)。

### R1067 §64：原范数相容级数的固定有理标量3024

原二倍除子、三挠加法及完整S1因子给Mσ=432^(−1/12)、MG=3^(−1/2)、MSMG=1/3024。准确c_p=3024^(1−p²)，所以同一3024K在原LT塔严格范数相容，无须扩标量。 [同编号全文](results/R1067-original-three-target-units-and-integral-isotropic-source.md)。

### R1067 §65：17挠全局单位与三目标完整Heisenberg读者

实际17平移保Teich相位、共同3024及全部17p^r全局单位；原CRT证明S与九H在同一b⊗V17，完整289项回各目标。原三个C_i及参考逆因子照保；偶对数奇矩为零，不能替代原Rubin类。 [同编号全文](results/R1067-original-three-target-units-and-integral-isotropic-source.md)。

### R1071 §17：原下降G3两截面及四个物理理想

真实Z上G3维228、1483系数给整个核；全972乘积秩840认证两截面无公共厚零，物理t⁹/s³准确生成原四理想。原高A/B按Artin 0/2付2095界，保612paired rows及全部后理想回核。 [同编号全文](results/R1071-original-descended-pencils-and-complete-thick-pullbacks.md)。
