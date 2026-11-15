# 四控制小核到非零幅完整112场：现成源码与条件接口

类型：源码与条件数学接口；没有新求解器、请求或数值执行。作者：exact_refinement。日期：2026-11-15。

## 1. 当前边界与最小结论

实际115已把原完整三方程W从6958.22576276662降到1236.0078724708558，八个方向均获原full3接受。但末单位方程仍为 `[-49.71935400957918, -0.03977199754487137, -8.125719463311133e-06]`，原unit/full112候选及非零native标志仍为false。当前下一实际动作是116同源四控制续接；以下只是将来完整场入口的准确边界，不能把未过门的小核点提前标成非零场父件。

现成完整场链条的物理/边界/求解内核可复用，旧入口不能直接吃115的四参数结果：它们硬绑定旧三控制scalar schema、历史warm来源、前三个原大幅core目标，且没有显式λ接口。需要的最小后继是独立的**设计坐标视图、λ目标、初猜及新scalar身份绑定层**，而不是删去高模或把已有accepted记录改标签。本稿不实现该层。

## 2. 三active设计坐标与平方计数

115实际标量记为 $a(s;p_1,p_2,p_3,\theta)$，返回的斜率量另记 $\nu$；本稿不把有限Gauss定义的 $a$ 的解析导数与源返回的 `ap` 静默等同。第四控制使用第二原支撑上的奇形，零端点0/1/2 jet保持原core/cut定义。

最直接的平方视图是固定实际 $\theta_*$，令 $a_*(s;p)=a(s;p,\theta_*)$，只有三个 $p$ 为active。已冻结family的 `ThetaFrozenProfile` 正这样构造。原 `FullDNBoundary` 的计数为 $k=T-M+K$；取 $M=T=112,K=3$，得到 $k=3$。完整物理状态338、core112、参数3，共453；增广后的左边界341、右边界112。109个高core仍是自由未知，未被设置为新增零目标。[1][2]

四控制搜索的完整3×4响应即使满行秩，固定θ后的前三列也可能不可用。反过来，若真实3×4矩阵有秩3，线性代数保证至少有一个非零3×3列minor。将来可以选择其对应三个active设计坐标，并固定余下一个；平方计数仍为453，但必须另有明确规范：完整四坐标顺序、active索引顺序、固定索引与实际值、三个准确control jets、新scalar descriptor和source身份。不能把 `(p1,p2,theta)` 冒充旧 `(p1,p2,p3)`，也不能悄改已经冻结的115 `ThetaFrozenProfile`。

实际115末完整3×4最小奇异值为6.40795078841513，前三列为5.331001439612569；初前三列最小值为9.800236811437901e−5，而完整四列初最小值为83.72860814512897。它们及四列FD都是普通浮点读数，不能代替当前根处精确minor或横截性证明。它们也不自动要求另换active坐标；等实际后继状态再决定，现不引入新的筛选门。

固定θ仅固定了第四形状的设计值。随后三个p若继续变化，整个metric仍在设计族内变化，不能称为same-g求解。真正same-g阶段必须将四个最终值全部固定。

## 3. R259的完整112责任在新family下如何保持

R259已经给出条件性小幅分支结构，不需再证明同一结论。令原三个core目标为 $A$，同伦低模目标为 $c_L=\lambda A$，高模取 $c_H=\lambda d$。在明确固定一个设计坐标的三active图中，用当前family重建完整线性右边界矩阵 $L(p)$。[3]

完整必要条件仍是

$$
L(p_*)\begin{pmatrix}A\\d_*\end{pmatrix}=0.
$$

若当前高109块 $L_{HH}$ 可逆，才可在理论中消去

$$
d=-L_{HH}^{-1}L_{HL}A,
\qquad
f(p)=\bigl(L_{LL}-L_{LH}L_{HH}^{-1}L_{HL}\bigr)A.
$$

当前保存的真实零尾J全部112×112项若确为对角，有限circle传递可逐模解耦。此时低三原单位缺陷乘原非零目标 $A_j$ 给出低三完整右行；其余109在低三种子下观测为零，只说明该种子没有高模右泄漏，**不说明高109可逆**。当前参数/θ下仍须分别支付所声称的高块结论。[3][4]

R277可复用的代数内核是完整两端链的多项式行列式身份，允许局部右传播块奇异；不能为使用单向传递而丢掉不满足该图条件的高模。实际81已经支付的有限binary64高109非奇异只对应实际78旧参数；其Arb实模型另有103个高模在640位未排零。两类旧结论都不能跨新p/θ继承。[4]

R259的局部分支横截矩阵是完整112×112

$$
\bigl[L_{:,H},\ \partial_{p_1}L\,C,\ \partial_{p_2}L\,C,\ \partial_{p_3}L\,C\bigr],
\qquad C=(A,d).
$$

若换active minor，这里三列导数也必须按新明示坐标排列。高块可逆加消去后3×3导数可逆，才对应这个完整条件；只看四控制搜索3×4秩不足以支付它。实际有限浮点小残差/SVD不能冒充精确根或解析尾导数证书。以上是结论范围和数学责任，不新增一个要求先拿证明才准运行原数值求解的门。

在同一有限非线性模型满足所需光滑条件时，R259用 $\mathcal R(\lambda C,p)/\lambda$ 的积分延拓说明λ=0附近局部分支。该结论不保证能走到λ=1，也不排除其他加权同伦；不能从低三近根直接宣布原大幅任务完成。

## 4. 现成源码可复用到哪里

| 原文件/对象 | 可直接复用的职责 | 需要明确的新绑定 |
|---|---|---|
| `geometry_20261115_small_core_four_control_family.py` / `ThetaFrozenProfile` | 当前θ进base、三个原p active、同一数学标量函数 | 实际四参数及新scalar身份；不能声称两个求和顺序逐位同 |
| `geometry_20261114_full_dn_augmented.py` / `AugmentedFlow`、`SeparatedBoundary` | 全物理338、全部core112、三个参数；常数core/p方程与所有导数 | 一个真正3active的新profile，不塞四active进旧平方边界 |
| `geometry_20261114_physical_test_boundary.py` / `PhysicalTestBoundary` | 全112个物理φ测试右行、完整material height映射及core导数 | 明确当前profile/新λ目标/实际native返回，保原physical-test身份 |
| `geometry_20261114_full_dn_solve.py` / `main`、`true_height` | 原完整BVP、真实尾更新、17次Newton回溯、最终RMS/BC与native audit | `main` 当前直接取 `coefficients[:3]`，没有λ参数；需独立显式目标层 |
| `geometry_20261114_lifted_modes_full_dn.py`、`..._banded_full_dn.py` | 112模完整维数、原全部行、完整banded方向与原回溯 | 旧scalar schema、warm出处与旧profile重建器不能接新family后改标签 |
| `geometry_20261114_noj_primal_live_full_dn.py`、`geometry_20261115_completed95_noj_primal_live_full_dn.py` | 一实际worker接当前H→J→原FD→full-DN→fresh audit的编排结构 | 入口要求其指定真实completed父件，失败73/95或小核circle均不能伪装为该父件 |
| `geometry_20261114_same_metric_physical_full_dn.py`、`..._same_metric_full_dn.py` | 真正接受之后冻结scalar、K=k=0、保全112自由core的same-g细化 | 必须先有真实accepted场并冻结四值；此450维阶段不是当前453维设计问题 |
| `geometry_20261114_lifted_modes_after_accept.py` | 真实最终尾response与prefix→cut→有限闭场读出 | 新完整scalar loader/source及同一实际尾；有限闭场仍不支付连续metric/reach证书 |

上述旧链均可保原算法责任，但不是一个现成“115结果→非零λ”的一键入口。旧v3 scalar identity和旧warm来源的硬核是实在的接口边界，应由独立明确adapter处理，不能放宽或伪造它们。

## 5. 最小非零初猜合同

未来实际选择一个小的正λ时，输入应是可重建的短参数recipe与原完整数学输入，不依赖按规则15已删的circle/raw状态。先在当前family、当前三active图里重新形成circle与必要全模传递；从全部112个core系数 $C=(A,d)$ 构造一阶初猜，低三明确固定为λA，高109只是自由变量的初猜，不能据此增加109个零边界条件。

原rawφ切向公式必须保留：频率 $k_j=2j$ 时，单位入口的

$$
T_j=\frac{(1-k_j^2)R-U_j}{k_j},
$$

一般入口幅值 $C_j$ 时把首项换为 $(1-k_j^2)RC_j$。不能偷用material坐标的简式 $-U_j/k_j$。原circle的R/Z/均值继续保留，U/T/H一阶项作为初猜，不作为非线性解或精确可行场。[3]

新入口至少需绑定：完整四参数、active/frozen顺序、λ原字面值、原目标A、当前scalar descriptor/source、原source accepted身份、全部112 core/物理初猜、原mesh、H/尾config与当前worker。原accepted96仍仅为其真实来源，不能通过改 `accepted.core_coefficients` 或success字段让旧入口误以为新λ场已接受。

然后按原完整方程重新计算RHS/J和节点、中点、RMS查询域。actual H必须由当前完整endpoint和material transform生成，再送入真正native非线性solve/J；旧零J anchor可作其明确线性来源，不能替代非零H的真实尾解。没有真实完成的bootstrap时须诚实建立新请求路径，不能冒旧completed-anchor条件已经满足。

## 6. 接受与最终职责不变

现成完整链保留原17次Newton回溯、所有物理/core/参数方程、原RMS≤1e−6和BC≤1e−11；内层使用的affine尾必须明确为线性近似。每个候选的新H都由实际native再评价，并以真实非线性BC决定是否接受该外轮。[2][5]

完整场候选还需冻结当前设计值后的原physical RMS复核、最终实际 `solve(H,jacobian=True,audit=True)`、重新计算原BC、完整height/mean/seam读出。物理φ测试右行与旧material右行的有限离散口径不同，旧seam责任不能被前者通过取代。新native实现若另有精度/表示身份，也必须保实际source/J/audit；不能只靠一次noJ或小核J宣布终检完成。

设计阶段逐λ接受并不证明λ=1可达。在真正需要same-g重网格或闭场时，必须先选定全部四个设计值，使scalar定义、tail config、prefix/闭场loader都绑定同一个最终g。随后已有K=k=0的450维same-g入口才有合适的数学位置；不能在此前移除三个固定core目标来消掉困难。

## 7. 本稿来源与范围

本稿只读以下已发布原文件及实际115原短摘要，不导入科学模块，不执行新的数值计算或构造，不改任何冻结源。实际115 run/source与摘要SHA见[续接116接口](2026-11-15-actual115-four-control-continuation116-interface.md)。源码读取以已发布115触发commit `c9eb007df84297f5345d0e7fab42b845df0bf912` 的定义为参照。

1. [新四控制family与θ冻结视图](../computations/geometry_20261115_small_core_four_control_family.py)，`ThetaFrozenProfile/setup/complete_reference_check`。
2. [全边界计数](../computations/geometry_20261114_full_dn_boundary.py)与[完整增广流](../computations/geometry_20261114_full_dn_augmented.py)。
3. [R259：小核同伦及共振条件](../results/R259-small-core-homotopy-and-resonance-conditions.md)。
4. [R277：两端完整行列式与高模消去](../results/R277-complete-two-end-chain-determinant-and-high-core-elimination.md)。
5. [原full-DN求解](../computations/geometry_20261114_full_dn_solve.py)、[物理测试边界入口](../computations/geometry_20261114_physical_test_full_dn.py)、[lifted入口](../computations/geometry_20261114_lifted_modes_full_dn.py)、[same-g物理入口](../computations/geometry_20261114_same_metric_physical_full_dn.py)、[真正接受后闭场读出](../computations/geometry_20261114_lifted_modes_after_accept.py)。

本稿没有新gate，也没有将来run号或预写结果。116实际返回后应先读其真实停止原因、全部接受与原final flags，再决定继续四控制搜索、选择三active图，或形成独立完整场入口。
