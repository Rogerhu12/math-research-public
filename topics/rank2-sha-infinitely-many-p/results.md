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
