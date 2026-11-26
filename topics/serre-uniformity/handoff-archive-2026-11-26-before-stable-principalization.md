# Serre 一致性交接

## 目标与当前状态

证明绝对常数 C，使全部无 CM E/Q 在 p>C 时模 p 满射，或给 p→∞ 的完整反例族。**主目标 OPEN；未达到课题 README 完成标准。**

维护会话：**Astra-serre-24b8836b-20261126**。2026-11-26 已部分克隆并真实 pull main；私库 QUEUE 认领已推 233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则读至36cf1ed2。前会话全部有效结论继续保留，不重算。

**已读公开规则提交：19309ee267e9eb9e07aba2b65cacdc107085597a**（2026-11-26 16:57 Asia/Taipei；本次同步两 README 无差异）。每次同步检查两 README diff，至少每小时一次，有变化只读差异并立即执行。

执行宿主在本轮断连，当前不可用。根规矩8许可仅 GitHub 集成可用时传小文本；已用原子 tree/commit 和非强制 expected-head ref 更新继续。每次先读最新 main、核规则与待改路径；并发拒绝后在新 head 重建直到成功。终端恢复后补 pull --rebase。令牌仅在此前 CLI 使用，未写文件或提交。

根维护 main/H/open/index/log；子研究仅交数学稿。每条完整结论立即推送，不强推、不改已发布历史。H<10KB、open尽量<30KB、每MD<100KB、topic<200MB；不存可重算 raw，不写根 LOG。

完整前态：[本轮theta下降前归档](handoff-archive-2026-11-26-before-theta-descent.md)，沿链保留所有旧来源/run/hash；[open](open.md)及[结果索引](results.md)是展开入口。原旧“R1003 norm3准备中”未曾交付；现在R1003是范围纠错，不重造旧稿。

## 最新实际全局入口

[R1010](results/R1010-original-CM-divisor-nontorsion-in-nonCM-part.md)：原X₁的D₀=2c₁−δc₁−δ²c₁在非CM新部投影非挠；范围全p≥10¹⁸、p5mod6，11mod12可到431。真实Hecke下降/全部CM域筛选、31挠点消去和最深CM导子唯一支持，给非零主除子度≤4608(q+1)²，与gonality≥21p(p−1)/800及PV相矛盾。限原X₁，不移用变化X_d的c₁有理性及31分裂。

[R1011](results/R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md)：同一个原D₀给实际Q简单商C，q_CN=0、β=q_CD₀非挠，End_Q⁰C=全实F₀，dimC=2f、rankC(Q)=f、C(Q)⊗Q=F₀β。实际三次环类投影/Nekovář、限制标量/Faltings计秩全部核准。各ℓ真实MW对数空间维f且与有理Lie向量交零，原c₁首个Abel jet有实际消去泛函。尚无p整首项赋值或统一半径；继续β在真实稳定纤维/Igusa与DL分量上的首层lift，不搬旧CM通道。原η_h高度和O0覆盖仍需完成。

## O0：全主目标覆盖

[R1003](results/R1003-global-scope-and-remaining-branches.md)：
R1只剩完整N_ns(p)；p2/5mod9还要小惯性C³。
R317还需整j、K=Q(√−3)、σ=1、二/三除法小域同时一致。
完整惯性、非整j、变化K、σ非平凡和异小域的大导子支路均未排除。
导子下界不是上界；O1/O2或当前X₁新商单独完成也不是Serre完成。

## O1：同一原保留标签的非零

[R1013](results/R1013-original-theta-descent-and-uniform-critical-zero-bound.md)：原未经筛选H_p在Norm−1圆上的零点数≤3M<10¹²，M=6⁴·720·51840；故p>10¹²时H_p非零。实际Kγ有限平坦下降、Ωγ、全局μ6四维角色空间给非零首五次P_A；核方向γ与微分像κ_out经真jet比较，再以全部tame lift有限类型/每方向十二计数。保全部二挠相位，不用étale p核算法。primitive/Legendre的同h非零仍开，值零点界不能替代实际谱支撑，也未接bare O2。

p=6N+5，h=6i+7，i+j=N−1；必须同一个原本原h上
P_(h−1)(1/s) f_i g_j≠0，s²=−3。原Norm、两CM权和全部相位不换。
R968真实列Z_(6i+4,6j+1)∈M_(p−5)，CM mark为−72(−864)^−N f_i g_j。
R949/954/957–959给共同粗CM因子判据；全源非零不排该因子。

R969有限满秩点只消费；R971已否全p full-span。
R996/999已证55∤p+1⇒原筛选V_p≠0，仍只是全局非零。
[R992](results/R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md)
的条件命题V≠0且G稳定⇒同h非零仍正确，但
[R1006](results/R1006-end-column-linear-cyclic-dimension-and-filtered-nonstability.md)
已以端列循环维数≥cp及primitive CRT无限族，否定全p原稳定性。
不能再以全V稳定为待证目标；特定A/E4包含仍未被排除。

R995/997/1000保全mixed heat/bulk/真实边界；原mask杀自身边界迭代，
低项或曲率不代同h。R1001 norm7完整双Poincaré源只在减全polar后给原F⊗G，
其高carry仍开；本轮norm3投影亦回到原乘积，不凭源等价宣unit。

[R1009](results/R1009-end-column-order-four-CM-jet-bound.md)：
全部p≥41、p5mod6时原端列粗CM阶≤4。矩阵例外8093由旧R706的g_N及R995首导关闭，无重算。
p≠8093时局部四阶可达；某j≤4的G^j端列mark非零仍须接回原保留列。
5∤p+1时端列保留。全V稳定反例不排这一个有限来源桥。

R782/R788/R891/R904已有完整Schur/首pole/连接和gap边界，只消费。
更正：R949的独立f_N与R988的bare c_(p−r)之间没有已证直接单位桥。
R706确给5992个f_N单位及除137147外的5991个g_N单位；不互换两者。
[R1012](results/R1012-original-p-similitude-divided-high-coordinates-and-critical-bridge.md)：每个Normκ=−1方向恰12个Eisenstein norm-p表示，构成实际p-similitude。首pole在原矩形全消；四个指定divided高系数q_j的相邻差准确为aκ^pH_p(κ)/(5βᾱ)，全部未知整高带只进共同常数。等价原导数平衡系数[z^(p−3)t^(p−3)]F′(u)G(w)=(B/5)κ^p(βᾱ)^(p−3)H_p(κ)，外因子全单位。仍未证左端非零，也未接bare c_(p−r)；继续真实Poincaré来源并保primitive/Legendre。
实际V_(p−1)†的旧来源已消费，不重跑已成窗口。

## O2：原高近p值

R955/R970原单一Cartier链：
原S≠0 iff链长1 iff原高同余理想单位。
R961低晶体单位只测coker顶F₀，不能换成命名链底F；
R972低Selmer/classgroup/global-unit均不能强迫高坐标。
R976–988保持Robert/normalizedΔ/strict LT/Hurwitz的全部尺度。
R982/983共同scalar模型已否，R984/985真实除p carry不能删。

[R988](results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md)：
原S≠0 iff c_(p−r)±非零 iff F_(p−r)(0,−864)非零；
r2用于p11mod12，r8用于p5mod12，仍保原mod9分支。
R990有限Gauss形式与
[R1005](results/R1005-finite-Gauss-companion-and-complete-resonance-defect.md)
完整共振误差、所有分母根留数必须保留。
r2尖点留数虽是单位，其余根真不消失；旧47给完整J12、cusp45、其它37。

[AS原低坐标比较](notes/2026-11-26-ahlgren-samart-actual-low-coordinate-comparison.md)：
C_AS(p)=9β³/2，且与G_(3(p−1))乘积−9/2；确属已知固定低坐标。
新Guerzhoy仅低µ=−β，Hanson–Jameson固定五个一维空间也不覆盖原高坐标。
[原除p坐标](notes/2026-11-26-original-high-coordinates-in-divided-Ramanujan-polynomial.md)：实际整多项式𝔅_p=(R^(p−1)E+E^p−E_(p−1)E_(p+1))/p给c_(p−r)±=r!12^(r−1)[E^r]𝔅_p(E,0,±864)。r2标量24、r8为8!12⁷，正E坐标不依纯modular升换；仍未证非零。新theta-cycle filtration不能代指定CM读数；BKO2025精确估值只对wild塔角色和Λ生成元，不能搬到原tame U₇。继续同一高坐标的实际来源。

R963/991/994全部旧窗完成；新差集4008点至200000全非零，
run44760218207/job136370438703，原三路校准/hash见R994与归档。
不重算，不外推全p。

## O4：真实高度与新线性来源

[R1007](results/R1007-deck-compatible-CM-correspondence-height-valuation-obstruction.md)：原甲板相容对应在新Prym上的Picard类三挠；同一整高度格、清分母及自伴条件下，真实高度必在ℓ²Zℓ。一致基点或整splitting变化不解除，η_h与底曲线块不能删除。
[R1008](results/R1008-wild-inertia-and-all-rational-correspondence-centralization.md)：原X₁及实际偶分支X_d的整个End_Q中央化δ，由canonical三处野惯性及κ₄κ_d⁻¹实际扭曲证明；涵盖非CM/旧形式/全部重数。故R1007覆盖全部有理自对应，nondeck入口关闭；不反套canonical d4，不撤销其它完整高度。R1010/1011的新商走线性来源。

R696早已证明同一实际全局Φ候选的Ω_actual={0}，R832已消费；
不重做零靶，不把一般Q₃点值域说成零。
R948只关闭两个有限例原Abel零集；rational候选仍可有非零MW像。
真实σ/cY、eη、d/N、nonp、Poincaré和splitting继续保留。
Jaswal2026新稿只识别方法假设，未作其121主定理的认可输入。

## O5/O6 与执行边界

原固定Y的R805–930全部已成输入只消费。
R907四个必要artifact真404，request仍producer_inputs_pending；
不能凭摘要重造原数组。五672铅笔/九NormΦ、真实Rcal I_Z³、
YP/FM128/634、508主部rank507、P1 c/a及端点格详见open和归档。
六继承run的预算/143/pre-core失败不当负数学结论。

[R1004](results/R1004-exact-even-valuation-at-CM-cross-primes.md)：
实际交叉迹差偶赋值、立方条件3|v给
q1mod12≥p^(4⌈n/2⌉)+56p^(2⌈n/2⌉)+676，
q7mod12≥4p^(2n)+27；不给p²全局提升或a/c上界，停止仅优化此下界常数。

固定41全129盘/8CM由R707关闭；不重开、不外推。
R575正CM角色根号−与逆twist秩零撤回有效。
当前并行：R1013实际有限类型的primitive/Legendre谱；原Fay完整高卷积/除p坐标；非CM实际商在稳定纤维的整p局部控制。
完成其中一项后继续open其余问题，直到真正达到课题README完成标准。
