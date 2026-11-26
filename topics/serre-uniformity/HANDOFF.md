# Serre 一致性交接

## 目标与当前状态

证明绝对常数 C，使全部无 CM E/Q 在 p>C 时模 p 满射，或给 p→∞ 的完整反例族。**主目标 OPEN；未达到课题 README 完成标准。**

维护会话：**Astra-serre-24b8836b-20261126**。2026-11-26 已部分克隆并真实 pull main；私库 QUEUE 认领已推 233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则读至36cf1ed2。前会话全部有效结论继续保留，不重算。

**已读公开规则提交：525393dd4ffec62a2d81e30a62723b21766d6493**（2026-11-26 15:00 Asia/Taipei；本次同步两 README 无差异）。每次同步检查两 README diff，至少每小时一次，有变化只读差异并立即执行。

执行宿主在本轮断连，当前不可用。根规矩8许可仅 GitHub 集成可用时传小文本；已用原子 tree/commit 和非强制 expected-head ref 更新继续。每次先读最新 main、核规则与待改路径；并发拒绝后在新 head 重建直到成功。终端恢复后补 pull --rebase。令牌仅在此前 CLI 使用，未写文件或提交。

根维护 main/H/open/index/log；子研究仅交数学稿。每条完整结论立即推送，不强推、不改已发布历史。H<10KB、open尽量<30KB、每MD<100KB、topic<200MB；不存可重算 raw，不写根 LOG。

完整上一版交接及全部来源/run/hash：
[本轮高度前归档](handoff-archive-2026-11-26-before-height-obstruction.md)、
[接手前归档](handoff-archive-2026-11-26-before-resume.md)、
[open](open.md)、[结果索引](results.md)。
归档沿链保留旧尺度和已成计算。原旧 HANDOFF 的“R1003 norm3准备中”没有实际交付稿；现在 R1003 是下述范围纠错。

## O0：全主目标覆盖必须保留

[R1003](results/R1003-global-scope-and-remaining-branches.md)：R1只剩完整非分裂正规化子 N_ns(p)。p≡2,5 mod9 来自另加的小惯性 C³；R317还需整j、K=Q(√−3)、σ=1、小二/三除法域同时一致。完整惯性、非整j、变化K、σ非平凡和异小域的大导子支路没有被当前 CM 证明链排除。导子下界不是上界。O1/O2 是指定辅助源；即使全解决，也不能单独宣 Serre 完成。

## O1：原同一标签的三个因子非零

p=6N+5、h=6i+7、i+j=N−1。必须在同一个原本原 h 上使
P_(h−1)(1/s) f_i g_j≠0；s²=−3，全部原 Norm/两 CM 权/相位不换。
R968 的实际列 Z_(6i+4,6j+1)∈M_(p−5)，CM mark为
−72(−864)^−N f_i g_j。R949/954/957–959给全失败的原粗 CM 因子判据。
R898 已把原 theta 向量、有限环面、Legendre 相位及两筛接到同一整源；
抽象不可约或单位 content 不决定指定 jet。

R969 三个实际满秩点只消费；R971 已否全p full-span。
R996/999 已证 **55∤p+1⇒原筛选空间 V_p≠0**，只是全局非零。
旧中央227/857的零和替代标签均已登记，不重算。

[R992](results/R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md)：
原 G 归一到
L=z(1−z)∂²+(4/3−7z/3)∂−55/144，Jacobi简单谱、各本征 mark1，
ker G为Tate A/E4。条件命题 V≠0 且 G(V)⊂V⇒同h非零仍正确。

**[R1006](results/R1006-end-column-linear-cyclic-dimension-and-filtered-nonstability.md) 已否定全p原稳定性。**
原端列的固定 Eichler germ在q^p前精确匹配；十二阶Fuchs系统/有理无穷远指数、
Jacobi带宽首尾系数与固定Taylor子式证明循环维数≥cp。
原本原标签数在一个无限允许素数等差族上小于cp，而端列被保留；
所以该族充分大p均不稳定。不能再把全p稳定当待证目标。
这不排原 mark 非零或特定 A/E4 包含。

R995/997/1000 全部 mixed heat、bulk和边界已成；原mask杀自身边界迭代，
不能以低项或曲率代同h。R1001 norm7真双Poincaré源减全polar后恢复 F⊗G，
但全乘积高carry仍开；norm3源同样不能单独给非零。
R1002 原W_(p−9)/η4权p−11，十步方程有四自由CM jet；
准确端列432D³f+75XDf−9Yf，mark79R0−96R1，局部方程不能固定它。

本轮续查已消费：R891 的36个E[6]基点判据、R904六通道Wronskian与度数界，
均不能排互补零；top f_N 已重合于O2高权链底，不能当独立低单位。
继续实际非端点两筛、特定A/E4包含或新的全局标记输入。

## O2：原完整 trace 与高 Artin–Hasse 坐标

R955/R970 原CM packet是单一Cartier链；
**原S≠0 iff链长1 iff原高同余理想单位**。
低权晶体单位只检测coker顶，R961不能搬到命名链底 F。
R972低Selmer/classgroup为零、global-unit低坐标单位，均不强迫高坐标单位。
R976–980原Robert单位/normalizedΔ/strict LT/pure Hurwitz反射的全部尺度保留；
Frobenius共轭指数不是同一坐标。R982/983共同scalar/factorial模型已否。
R984/985的真实除p carry不能删。

[R988](results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md)：
原S≠0 iff c_(p−r)±单位 iff F_(p−r)(0,−864)非零；
r=2用于p11mod12，r=8用于p5mod12，并保p2/5mod9。
低unit及整性不是这个近p值的unit。

R990固定 A=2F1(1/12,7/12;2/3;z)、B=2F1(5/12,11/12;4/3;z)，
ℓ=(p+1)/3、m=(p−r)/3<ℓ，B为degree floor(p/12)的真实Jacobi多项式。
H=((1−z)B²)^−1、f_i=H_i/(1−3i)、Q=4+12zB′/B−z/(1−z)，
c_(p−r)+=(-32)^m(r−1)! [z^m]Q f^−r/4，首共振Hℓ=B(1)^−2。

[R1005](results/R1005-finite-Gauss-companion-and-complete-resonance-defect.md)：
指定P=A截到ℓ−1，完整Wronskian是1−z^ℓ C/B(1)²，
C+3zC′=B、C(1)=B(1)²、P顶系数−16/(7B(1)²)。
原目标准确为[z^m]QB^r/P^r，须保所有分母根。
§5原r2取S=P−P(1)z^ℓB/B(1)，cusp留数
−28853B(1)^6/36864在全原r2类为单位，但其余根不消失：
旧47值给J12、cusp45、其余和37。完整全和非零仍开。
旧R973的B字段10不是c45−（后者4）。

R963/991/994全部旧有限窗口已完成：新两行到200000共4008点均非零，
run44760218207/job136370438703，原三路校准/hash见R994及交接归档。
不重跑、不过度外推。正在核 modified Serre derivative/权参数导数的原递推，
尚未形成新非零结论；不把Gaussian或split-CM异常素数表当原高坐标反例。

## O4：真实全局高度

[R1007](results/R1007-deck-compatible-CM-correspondence-height-valuation-obstruction.md)：
原X₁→Y、μ3固定c0、N=φ*φ_*、qN=0。
甲板相容对称对应有 ND_Z(c0)=3D_Z(c0)，
D_Z(y)=D_Z(c0)−2Z[y−c0]。
在真实整格、同一高度b(M,M)⊂ℓZℓ、N/Z自伴及
NG=0、ZG=λG、λ∈ℓZℓ时，b(G,D_Z(y))∈ℓ²Zℓ；
新 valuation-QC 所需赋值1无法由这些原纯CM对应实现。
对一致换基点仍成立，整splitting改变也不解除模ℓ²障碍。
这不删除η_h，底曲线块和其它完整高度方法仍开。

[R1008](results/R1008-wild-inertia-and-all-rational-correspondence-centralization.md)：
原canonical level6p全H¹在三处野惯性平凡；原κ₄κ_d⁻¹扭曲将一个野惯性元素实现为δ，实际偶分支d∈Q₃ cubes。故整个End_Q(J_d)均中央化δ，包含非CM/旧形式/全部重数。R1007的三挠Picard投影及ℓ²高度整除因此适用于全部有理自对应，关闭原曲线上的新nondeck入口；保留底曲线η_h、其它完整高度及O0范围。
不能把canonical d4反套本定理；整个H¹的来源与MY/Carayol局部定理已逐项核读。

Jaswal 2026新预印本只作方法假设来源，未把其121主定理当已认可输入；
一般p在水平处坏约化，不能直接套辅助好素ℓ的整性。
R1007自足证明不依赖该预印本结论。

R948只证两个有限例原Abel零集为中心；rational候选仍可能有非零MW像。
非挠、log、rank、低unit或深盘简单根都不是height。
原σ/cY、eη、d/N、完整nonp、Poincaré和splitting必须保留。

## O5/O6 与当前续做方向

原固定Y的R805–930全部已成输入只消费。R907四个必要artifact真404，
不能用摘要重造原数组。五672铅笔/九NormΦ、真实Rcal I_Z³、YP/FM、
端点格与P1 c/a等断点详见open和归档；失败预算不当负数学结论。

[R1004](results/R1004-exact-even-valuation-at-CM-cross-primes.md)：
实际CM交叉迹差在p5mod12有精确偶赋值；立方条件给3|v。
原pⁿ同构迫q1mod12≥p^(4⌈n/2⌉)+56p^(2⌈n/2⌉)+676，
q7mod12≥4p^(2n)+27；相邻奇/偶层检测阈值相同。
它不给全局p²提升或a/c上界，停止仅优化此下界常数。
继续真正参数/高度控制并覆盖O0其它分支。

固定41的R707全129盘/8CM已经关闭，不能外推一般p。
R575正CM根号−和逆twist秩零撤回继续有效。
当前三线：原同h非零；原高近p值；底曲线高度/全局覆盖。
完成任何一个仍须接open其余问题，不把中间结果当主目标完成。
