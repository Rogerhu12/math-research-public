# R631：硬总核心与可变度量静态设计的完整接口

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。
**状态：源码完成，尚无本新范围的 Actions 数值结果或宏观连接解。**
新文件为 `r631_radius080_hard_trace_design_20261128.py` 与
`r631_radius080_convex_core_input_path_20261128.py`。
它们消费真正重建的 R=.8 factory；原 R=.85 target86da 不参与这里的接受或误差结论。

## 1. 真正的1451自由列与硬总 trace

在默认 $J=48$ 时，设计坐标包含新 factory 的全部1130列（含 H），
224个新增compact列、96个真实全平tail列，共1450列；再追加一个真实新R=.8 $F_2\cos2\theta$ post自由列，共1451列。
这个新列的初值为0，准确嵌回前述新seed；全部原1450列都保留。
它的core trace是 $B_{0,2}=-3\mathrm{amp}/R$、
$B_{1,2}=-4\alpha B_{0,2}/\{R(1+\alpha)\}$，与其他列一样准确消元。
因此inner j2 germ幅度也能在静态设计中变化，不把新R=.8调H与硬core j2人为过约束。
amp在这里是数值单位，不能把它误当实际核心或tail幅度已冻结。
给外部指定的**总**核心 $P$，按同一仿射表示消元所有核心边界控制：

$$
f=f_{\rm seed}+L(x-x_{\rm seed})
 +A\{P-P_{\rm seed}-B_0(x-x_{\rm seed})\}
 +B\{\mathcal T(P)-\mathcal T(P_{\rm seed})-B_1(x-x_{\rm seed})\}.
$$

A覆盖2到48全部24模；B和 $\mathcal T$ 保留至96的全部48从属模式。
因此自由优化不能抹掉外部指定的非圆核心。
所有旧bare列的真实核心导数都在 $B_0,B_1$ 中，不只减新增core列。
完整固定P方向为 $L-AB_0-BB_1$，六jets和全部1451列位置Jacobian已实现。

新factory本身的 R602 sampled projection 与新的 complete Laurent core target
是同一个准确多项式表达式的不同数值评价。
源码把它们的数值差通过同一个 B 项显式带入当前实际高度，
并把差值单列为 roundoff/root 观测，不能把该差值另冻成一个数学设计参数。
本 seed 是新设计初值，未冒充任何旧已接受字段。

## 2. H 是真实设计变量，E 并未暗中冻结

A使用新seed的固定 $W_{\rm seed}$ 定义。
当前 H 的 gain 支持在 .61 前结束，所以核心邻域的 $W_H$ 与 $W_{\rm seed}$ 完全一致；
由此 $P_0[A]=1,P_1[A]=0$ 对所有当前 H 仍成立。
H的角向高度方向为0，而 mean slope 方向是实际 $\delta W,\delta W'$。
不能将这一点误称 H 已被冻结。

每个静态设计点都重新求自己的完整 turning root。其隐式方向保留

$$
\delta e=
\frac{2\langle\delta N/u\rangle+\langle N\,\delta\mathrm{shift}/u^3\rangle}
 {\langle N/u^3\rangle},\qquad
\delta E=2W\delta W+\delta e.
$$

新Jacobian保留全部 $\delta E$、权重、两次 primitive 和离解项。
外部 $P$ 方向仍为 $A\dot P+B D\mathcal T(P)\dot P$，再进入同一个实际
turning/位置链；没有把它当固定g方向。

work/fine所声明的全部径向点都保留。加频到更高J时可以明确指定grid role，
而不是因为角点增加就不知不觉改掉work网格。
系数消费者把完整原pre-tanh与全部post项先合在一起再取范数。
新参数化保留真实tail列，不用有限mouth下的零延拓代替它们。
设计阶段的mean高度是原真实 $h(R)=.04$ 与新 $W_H$ 的全区间积分定义；
这不消费旧固定E响应的 $s$-anchor，也不声称已付全部源积分误差。

## 3. R631路径从自己的真实核心起步

新 `Radius080ConvexCoreInputPath` 消费刚重建的 R=.8 hard-P模型。
它复用已写清的normal-angle方程，具体输入换为本对象自己的 $P_{\rm seed}$、
$R=4/5$、$\epsilon=1/20$ 和 R631 的严格常数。
旧R=.85源码只作为通用方程实现使用，没有借其seed、数组、accepted状态或E。

法线角仍是 $\phi$，右端支撑仍为 $\theta=\phi=0$，
$Y_\theta=R(-\sin\phi,\cos\phi)$、$\psi=\phi+\pi/2$。
首 $\mu=0$ 逐项返回本新seed的P系数。
每个μ的返回值都有完整P、Pdot、N/2N谱差和ODE/求积误差观测；
未假定J48足够，也未对原连接宣布可达性。

### 小非圆seed也可消费R631的统一核心界

这不需要把实际seed冒称精确圆。令其正偶余弦系数绝对值和为 $a\le1/5$。
准确 turning 方程和 $|P_{\rm seed}|\le a$ 给

$$1-2a\le e_{\rm seed}\le1+2a,\qquad
1-4a\le u_{\rm seed}^2\le1+4a.$$

第一组界的证明是：若e低于左端，则全角 $u^2<1$，turning均值大于1；
若e高于右端，则全角 $u^2>1$，均值小于1，均矛盾。
因此seed的曲率半径在 $R\sqrt{1/5}$ 与 $R\sqrt{9/5}$ 之间，
严格包含于R631所需的 $(7/50,17153/1000)$。
同周长支撑插值把这个界传给全部设计μ，再由
$u=\rho/R$、$e=\langle u^2\rangle$ 得

$$\rho>7/50,\quad u<17153/800,\quad e<460,\quad |P|<230.$$

生成器对literal输入系数用有理数和检查 $a\le1/5$，不因float求积而假装满足此条件。
这些是准确连续核心输入的纸面界，不能移给其有限J投影或整个闭曲面。
球/条带/跨片reach和最终固定g精化仍须实际完成。

所有实现目前只有源级和AST检查；没有本地科学运行，也没有把新范围登记成已求解。
下一实际运行应同时消费本新输入、真实全位置解算与必要几何读数，
而不是另加一个重复旧诊断的资格门。
