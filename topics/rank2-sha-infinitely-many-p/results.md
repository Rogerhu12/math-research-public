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
