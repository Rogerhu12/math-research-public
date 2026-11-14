# 新机制文献核查（2026-11-14）

状态：**文献核查与候选分析；没有完成本课题**。本记录由 literature 子任务撰写，未改动根规则、课题规则或其他任务状态。下列“未找到”是检索结论，不是不存在性定理。仓库内 R520 等主张仍须按其证明和代码单独核对，不能由公开文献的历史状态判定真伪。

## 1. 公开文献的准确边界

| 文献 | 已核对位置与实际结论 | 对本题的限制 |
|---|---|---|
| Mohammad Ghomi, *Open problems in geometry of curves and surfaces*, 2019（最后修订 2019-09-02） | §1.1，书内 p.5，Problem 1.1，将闭 $C^2$ 曲面连续等距弯曲列为问题；同时解释成对等距与连续可弯的区别。<https://ghomi.math.gatech.edu/Papers/op.pdf> | 这是 2019 状态，不能直接宣称至 2026 仍无解。局部凹凸翻转仅给离散端点。 |
| Michael T. Anderson, *Local rigidity of surfaces in space forms*, arXiv:0709.3202 | arXiv v3（2009-09-06）明确 withdrawn。<https://arxiv.org/abs/0709.3202> | 旧个人主页 PDF 仍声称解决，但**不得把它当成立的局部刚性定理**。 |
| Alec Payne 与 Andrew Sageman-Furnas，*Flexible Smooth Immersions of Cylinders in R^3*，2023 讲座 | UCSD 官方活动，2023-11-16，摘要宣布非极小、非可展的光滑浸入圆柱；闭曲面部分明言是 speculative approaches。<https://math.ucsd.edu/seminar/flexible-smooth-immersions-cylinders-r3> | 仅核到讲座摘要，没有可复核全文/公式，不能视作闭嵌入族。2026-11-14 所见 Payne 作者主页论文表亦未列出该稿。<https://sites.google.com/view/alecpayne> |
| A. I. Bobenko, T. Hoffmann, A. O. Sageman-Furnas, *Compact Bonnet pairs: isometric tori with the same curvatures*, Publ. Math. IHÉS **142** (2025), 241–293 | Main Theorems 1–2 / Theorem 9 给非全等实解析等距浸入环面对；§9 Question 1 明确把两个曲面均为嵌入列为问题。<https://doi.org/10.1007/s10240-025-00159-z>；可读全文 <https://sites.math.duke.edu/~bryant/Eilenberg/CompactBonnetPairs.pdf> | 不是固定度量下的连续族，且不是已证嵌入。文内参数族是“许多对”，不是同一度量上的一条弯曲路径。 |
| I. Kh. Sabitov, *Bendable Surfaces without Visible Deformations of Their Shape*, Math. Notes **110** (2021), 126–134；俄文 Mat. Zametki **110** (2021), 119–130 | 原刊摘要指出圆柱/锥面的 slide bendings 可不由环境刚体运动给出，但像作为点集不变。<https://www.mathnet.ru/eng/mzm13037>；DOI <https://doi.org/10.4213/mzm13037> | 必须区分材料点运动、像的运动与握持区。该文不是闭曲面构造；单独重参数化若在开握持区恒等，则在连通度量上只能是恒等。 |

Bonnet 文章另有两个有用的核查点：其引言 pp.244–245 区分 CMC associated families、Bonnet families 与 Bonnet pairs；非恒定平均曲率的紧曲面不能有三种同度量同平均曲率浸入。因此不能用保持平均曲率的 Bonnet 关联族直接补出本题。

## 2. 可计算的经典机制：Bour、T-surfaces、可弯管

1. Edmond Bour, *Théorie de la déformation des surfaces*, Journal de l'École Polytechnique, tome 22, cahier 39 (1862)。本次没有逐页核到 1862 原版，不为它编造定理编号。现代原始研究对其局部螺旋—旋转等距族给出了精确重述：R. Caddeo、I. I. Onnis 与 P. Piu, *Bour's theorem and helicoidal surfaces with constant mean curvature in the Bianchi–Cartan–Vranceanu spaces*, Annali di Matematica **201** (2022), 913–932（2021 online），Theorem 2、Remark 2，在 Euclidean 参数处退化为经典 Bour 定理。<https://doi.org/10.1007/s10231-021-01143-0>。螺距非零时角变量走一周会产生轴向平移，故闭合需额外的周期条件。
2. Ivan Izmestiev, Arvin Rasoulzadeh, Jonas Tervooren, *Isometric Deformations of Discrete and Smooth T-surfaces*, Computational Geometry **122** (2024), 102104；arXiv:2302.08925v1（2023）。已直接读到 §§4–5：Theorem 4.3 是参数化，Theorems 5.2、5.4、5.5、5.7 给 translation、molding、axial、一般 T-surfaces 的等距族，并要求相应高度导数不消失。<https://arxiv.org/html/2302.08925v1>；<https://doi.org/10.1016/j.comgeo.2024.102104>。
3. Kiumars Sharifmoghaddam, Rupert Maleczek, Georg Nawratil, *Generalizing rigid-foldable tubular structures of T-hedral type*, Mechanics Research Communications **132** (2023), 104151；arXiv:2301.09969。作者论文摘要涉及离散、半离散和光滑等距可弯管。<https://arxiv.org/abs/2301.09969>；<https://doi.org/10.1016/j.mechrescom.2023.104151>。本次尚未逐页核全稿；“tubular”不意味着紧致无边界。

这些公式很适合给新数值求解器做**精确局部基准**，但闭合、握持、全程 reach 三项都要另外求解。

## 3. 直接推导：两个简单闭合陷阱

### 3.1 纯重参数化无法固定开握持区

**已证明（标准事实在本处的应用）。** 设 $F:M\to\mathbb R^3$ 为连通 Riemannian 曲面的嵌入，$\phi$ 是其内蕴等距变换，且 $F\circ\phi=F$ 在非空开集成立。则嵌入性给 $\phi=\mathrm{id}$ 在该开集；在那里任取 $p$，有 $\phi(p)=p$、$d\phi_p=\mathrm{id}$。等距变换与指数映射相容，所以它在 $p$ 的正规邻域恒等，沿连通曲面有限串正规邻域延拓即全域恒等。因而只有 $F_t=F\circ\phi_t$ 的纯材料滑移不满足本题非零握持位移。这个结论**不排除**同时施加环境刚体运动、在对称握持片上抵消滑移的组合机制；组合机制要直接代入本题 $\delta_{\rm E}$ 定义检查。

### 3.2 双闭平面平移曲面的标准标量变形被卡住

**已证明（仅限所述模型）。** 取两条正则闭平面曲线
$$\alpha(u)=(a(u),0,c(u)),\qquad\beta(v)=(0,b(v),d(v)),$$
考察 $X(u,v)=\alpha(u)+\beta(v)$ 的标准分离变量等距变形，其中 $c'_\lambda=\lambda c'$、$d'_\lambda=\lambda^{-1}d'$。第一基本形式相等迫使
$$
(a'_\lambda)^2=(a')^2+(1-\lambda^2)(c')^2,\qquad
(b'_\lambda)^2=(b')^2+(1-\lambda^{-2})(d')^2.
$$
闭曲线坐标 $a,b$ 各自有极值。正则性说明 $a'=0$ 处 $c'\ne0$，$b'=0$ 处 $d'\ne0$，所以平方非负分别要求 $\lambda^2\le1$ 与 $\lambda^2\ge1$。在正参数支只剩 $\lambda=1$。这甚至不需要检查曲面是否嵌入；更原始的问题是这类双闭平面平移曲面可能本来就有秩退化。它排除的是一个显式公式，不是一般闭可弯曲面。

### 3.3 一般标准 T 族不能保留闭 profile

**已证明（仅限下述标准 T 族，不是全局不可弯性）。** 设 $v\in\mathbb R/L\mathbb Z$，$f,z_0$ 为 $C^1$ 周期函数且 $(f'(v),z_0'(v))\ne(0,0)$。考虑
$$X_t(u,v)=(\gamma_t(u)+f(v)\xi_t(u),z_t(v)),$$
并假定 $|\xi_t(u)|^2=|\xi_0(u)|^2+t$、$X_t$ 与 $X_0$ 的第一基本形式相同。这正是上述一般标准 T 变形的归一化形式；这里只使用其 $G$ 系数，直接得到
$$z_t'(v)^2=z_0'(v)^2-tf'(v)^2.$$
若 $t>0$，在周期函数 $z_0$ 的任一极值处有 $z_0'=0$；profile 正则性给 $f'\ne0$，上式右边为负，矛盾。若 $t<0$，右边在每个 $v$ 严格为正；于是连续函数 $z_t'$ 在连通圆上不消失、不变号，故 $\int_0^L z_t'\,dv\ne0$，不能周期。因而只有 $t=0$ 可闭合。若 $z_0$ 恒定，任一点均可用于 $t>0$ 的论证，$t<0$ 的论证不变。

这里的“profile 正则”由 $X_0$ 是浸入直接推出：若 $f'=z_0'=0$，则 $\partial_vX_0=0$。本结论允许自交，不依赖 reach；它说明现成公式的双周期化在到达这些后续检查之前就已失败。多片接合、改变共轭网或不保持此分离形式的变形不在结论范围内。

## 4. 三条可立即做的候选实验

- **A：T-surface 局部关节 + 非共轭网闭合。** 用上述 Theorem 5.7 的精确等距局部片作初值，增广求解末端位置/切平面/二阶 jet 匹配、固定握持片和全程自交约束。先检查周期导数是否被高度极值或角单值性锁死；不把上下边简单重合当成 $C^2$ 闭合。此路线的新内容必须在闭合，而不是局部等距公式。
- **B：由紧 Bonnet 对导出的非保平均曲率分支。** 用文章 §8 的小型周期离散模型作 continuation 初值；只保第一基本形式，释放平均曲率，沿度量映射的核寻找分支，再提高频率和网格。这里可能有分岔机制，但没有已证闭嵌入分支；离散等距在加密后也可能刚化。不能把 Bonnet 对之间插值当等距。
- **C：由光滑可弯管求反射/旋转成组闭合。** 对一段可弯管的端面全 $2$-jet 和刚体单值差做随 $t$ 的恒等匹配；若采用多个模块，模块数和所有几何参数固定后再验证误差趋零。Bour 非零螺距的位移单值差给一个直接可计算的障碍；T 管的高度极值和角周期给另一个。候选须把这些量作为方程求零，不能靠堆多层稀释缺陷。

目前最便于独立实现和误差归因的是 A；B 的数值起点现成但嵌入性困难；C 可共享 A 的端面匹配求解器。三者目前均仅为启发式研究方案。

## 5. 力学中“零刚度”不等于本题精确等距

S. Kok, A. Amoozandeh Nobaveh, G. Radaelli, *Neutrally stable double-curved shells by inflection point propagation*, Journal of the Mechanics and Physics of Solids **171** (2023), 105133。原刊摘要与全文摘要说的是经厚度优化获得近常能量/近零载荷路径，并用实体样件验证；不是紧闭曲面的精确等距定理。<https://doi.org/10.1016/j.jmps.2022.105133>，作者机构全文 <https://pure.tudelft.nl/ws/portalfiles/portal/141023244/1_s2.0_S0022509622003052_main.pdf>。因此这类文献可以指导机械外观和选形，不能代替本题误差 $10^{-6}$ 与固定参数加密收敛。

## 6. 2025 年可弯多面体新机制及其光滑边界

Zeyuan He 与 Simon D. Guest, *A new method for generalizing non-self-intersecting flexible polyhedra*, arXiv:2505.05629v1（2025-05-08）。原文 §2 的 base + crinkle / collar crinkle 给大幅度、可多自由度的无自交闭多面体；§3 第五点把光滑极限明确作为未来方向，仍没有给光滑闭曲面。<https://arxiv.org/html/2505.05629v1>。它是比反复优化轴对称扭转更不同的**离散机制来源**，但 $C^2$ 化本身正是待解部分。

本题可取其 collar-crinkle 运动作为目标形变或 continuation 初值；必须同时求一个固定光滑度量，不能只把每个时刻的棱独立圆滑后宣称等距。独立圆滑通常改变各时刻度量；网格加密只会更准确地测出这个固定缺陷。若用细化多面体序列，则需检验二阶导数/曲率的一致控制与同一光滑度量极限，而不只是 Hausdorff 形状趋近。
