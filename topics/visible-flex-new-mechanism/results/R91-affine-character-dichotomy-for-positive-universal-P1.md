# 正长度 universal P1 的仿射整权二分

日期：2026-11-14。完整纸面结果 R91。依赖 [R89](R89-affine-covariance-and-positive-multiple-pair-P1.md) 的真实协变与多 pair 相加、[R90](R90-seven-state-complete-response-and-positive-baseline-system.md) 的有限 Laurent 展开和七状态生成、[R80](R80-complete-third-affine-class-and-P1-endpoint-obstruction.md) 的完整第三仿射可达类。

本结果讨论 **universal profile 算子恒等式**：同一组真实几何控制系数须对所有输入 profile 成立。它不把多个 profile 上的分离泛函当作某一固定 profile 的证书，不声称 R87 的单状态非成员已经解决本结果中的总空间成员问题。

## 1. 对象、右锚与结论

令 $\mathcal W$ 为 R87 已证的真实 36 维第三控制空间。令 $\mathcal B_A(T)$ 为 R78/R89 的两个完整 P1 模式对第三控制 $T$ 的线性响应。它对二阶算子 $A$ 也线性。

标准真实第三端点类取 R89 所用的有理代表，记相应完整双模式基准为 $b=b_{1,0}$。物理状态 $(H,d)$ 满足 $H>0$，其基准记为 $b_{H,d}$，正 bulk 算子记为 $A_{H,d}$。定义真实函数空间

$$\mathcal R_*=
\sum_{H>0,d\in\mathbb R}\mathcal B_{A_{H,d}}(\mathcal W),
\qquad
\mathcal V=\mathcal R_*+
\operatorname{span}_{\mathbb R}\{b_{H,d}:H>0,d\in\mathbb R\}.
\tag{1}$$

这里函数等式按完整原始右 Volterra 表达式解释，不按不完备正规形的代表解释。可先在紧支撑光滑实 profile 的 universal 算子空间中定义它们：右锚取在输入支撑右方，改取更右的锚不改变任何正 profile 次数的原函数。实际几何应用再按 R80/R89 先选有限辅助路径族，随后选择其共同物理区间；不承诺任意预给窄区间或总长度盒。

**定理。** 恰有以下两种情形之一。

1. $b\in\mathcal R_*$。R90 的七个有界真实状态各取一个正完整 frame 周期，并分别选择真实内部第三控制，即能使完整 universal P1 的两模式同时为零。
2. $b\notin\mathcal R_*$。存在整数 $n$ 和定义于真实函数空间 $\mathcal V$ 的实线性泛函 $\Lambda$，满足

$$\Lambda|_{\mathcal R_*}=0,
\qquad
\Lambda(b_{H,d})=H^n>0
\quad(H>0,\ d\in\mathbb R).
\tag{2}$$

因此任何有限个物理状态、任何严格正长度、任何允许的独立真实第三控制都不能给出完整 universal P1 恒等式。

证明如下。第二种情形中的泛函是一个存在性结论；本文尚未证明实际 $b\notin\mathcal R_*$，也没有给出该 $\Lambda$ 的数值系数。

## 2. 完整 pullback 和不变空间

对输入 profile 定义

$$C_{H,d}f(x)=f((x-d)/H).$$

对任意阶的 profile 算子 $F$ 定义共轭

$$({\sf P}_{H,d}F)(f_1,\ldots,f_m)(\xi)
=F(C_{H,d}f_1,\ldots,C_{H,d}f_m)(H\xi+d).
\tag{3}$$

右锚同时作同一仿射变换。对含两个模式的算子，分别作用于两个分量。直接代入给出真实组合律

$$\boxed{{\sf P}_{K,e}{\sf P}_{H,d}
={\sf P}_{HK,d+He}.}\tag{4}$$

特别地，每个 ${\sf P}_{H,d}$ 可逆。记

$$S_H={\sf P}_{H,0},\qquad T_d={\sf P}_{1,d};$$

则

$$\begin{gathered}
S_HS_K=S_{HK},\qquad T_dT_e=T_{d+e},\\
{\sf P}_{H,d}=S_HT_d,\qquad
S_HT_dS_H^{-1}=T_{d/H}.
\end{gathered}\tag{5}$$

R89 的完整协变与同端口控制类给出

$$\begin{gathered}
{\sf P}_{H,d}\mathcal W=\mathcal W,\\
{\sf P}_{H,d}\mathcal B_A(T)
=\mathcal B_{{\sf P}_{H,d}A}({\sf P}_{H,d}T),\\
{\sf P}_{H,d}b=b_{H,d}.
\end{gathered}\tag{6}$$

第二式也可直接从 R78 的原始 $\mathcal K,\mathcal L$ 控制项检查：每项都是 $A,T$ 的组合、极化和共同右原函数，(3) 保留这些操作。这里没有逐段重新设锚，也没有额外未计入的 $H$ 因子。

物理二阶族的 span

$$\mathcal E=\operatorname{span}\{A_{H,d}\}
=\{p_1+4t_1=0\}$$

由 (4) 保持不变。因此 (6) 及可逆性给出

$$\boxed{{\sf P}_{H,d}\mathcal R_*=\mathcal R_*,
\qquad {\sf P}_{H,d}\mathcal V=\mathcal V.}\tag{7}$$

R90 已给 $\dim\mathcal R_*\le252$，且整个 $b$ 轨道有有限 Laurent 展开。故 $\mathcal V$ 有限维。

## 3. 平移幂零、缩放整权：不用三角化定理

R56 的有限分子闭合及 R90 的递归规则还给出更具体的表示性质。每个固定生成元都是有限原始乘积、profile 微分、正次数右原函数与非负坐标幂的组合。在 (3) 下：

- 一个 $m$ 阶输入 jet 乘 $H^{-m}$；
- 一个右原函数节点乘 $H$；
- 一个坐标幂 $x^j$ 变成 $(H\xi+d)^j$。

故在 $\mathcal V$ 的任意固定有限基中，$T_d$ 的矩阵关于 $d$ 是有限次多项式，$S_H$ 的矩阵关于 $H$ 是有限 Laurent 多项式。这些性质先对有限生成元成立，再线性传给一个基；不是把无限 Taylor 级数截断。

设

$$N=\left.\frac{d}{dd}T_d\right|_{d=0}.$$

由 $T_{d+e}=T_dT_e$ 对 $e$ 求导得 $T_d'=T_dN$、$T_0=I$。因 $T_d$ 是有限多项式，比较各次系数得

$$T_d=e^{dN},\qquad N^{D+1}=0\quad\text{对某个有限 }D.
\tag{8}$$

即平移生成元真实幂零。再由 (5) 得

$$S_HNS_H^{-1}=H^{-1}N.\tag{9}$$

对缩放写有限展开

$$S_H=\sum_{n\in\mathcal N}H^nE_n,
\qquad \mathcal N\subset\mathbb Z\text{ 有限}.$$

将此代入 $S_HS_K=S_{HK}$，比较两个独立正变量 $H,K$ 的 Laurent 系数，得到

$$E_nE_m=\delta_{nm}E_n,\qquad \sum_nE_n=I.
\tag{10}$$

因此是准确的实直和分解

$$\mathcal V=\bigoplus_n\operatorname{im}E_n,
\qquad S_H|_{\operatorname{im}E_n}=H^n I.
\tag{11}$$

不存在需要忽略的 $\log H$ Jordan 项。所有缩放特征在 $H>0$ 上严格正。

## 4. 循环商和正字符

取真实函数商

$$U=\mathcal V/\mathcal R_*,\qquad \bar b=[b].$$

由 (7)，全部 $S_H,T_d,N$ 都作用在 $U$ 上。其 Laurent 分解同样由 (10) 给出。根据 (1)，$U$ 由 $\bar b$ 的完整仿射轨道张成：

$$U=\operatorname{span}\{S_HT_d\bar b:H>0,d\in\mathbb R\}.
\tag{12}$$

现在假设 $\bar b\ne0$。子空间 $NU$ 对仿射作用保持不变。平移与 $N$ 交换；缩放满足 $S_HNu=H^{-1}NS_Hu$，逆变换也保持，所以这里确实得到子模。

关键是

$$\boxed{\bar b\notin NU.}\tag{13}$$

否则，因 $NU$ 不变，(12) 迫使整个 $U\subseteq NU$。因反向包含自动成立，$U=NU=N^2U=\cdots$。这与 (8) 以及 $U\ne0$ 矛盾。

在商 $U/NU$ 上，所有平移都成为恒等变换，因为 $e^{dN}-I$ 的像落在 $NU$。缩放仍按有限整数权分解。由 (13)，$\bar b$ 在这个商里至少有一个非零整数权分量，设其权为 $n$。在该权子空间取一个实线性泛函，使其在这个分量上的值为 1，并令它在其他权子空间上为零。得到

$$\lambda(\pi\bar b)=1,
\qquad \lambda S_H=H^n\lambda,
\qquad \lambda T_d=\lambda,
\tag{14}$$

其中 $\pi:U\to U/NU$ 为自然商映射。将它沿两个商映射拉回 $\mathcal V$，记为 $\Lambda$。它湮灭 $\mathcal R_*$，且由 (5)、(6)、(14)

$$\Lambda(b_{H,d})
=\lambda(\pi S_HT_d\bar b)=H^n.
\tag{15}$$

这证明了 (2)，没有使用一个不完备正规形来定义商，也没有将模素数值提升为实符号。

## 5. 正长度排除与七 helper 的反向构造

假设 $b\notin\mathcal R_*$。任意有限真实配置的 universal P1 除去共同正因子后为

$$\sum_{j=1}^m\ell_j
\{b_{H_j,d_j}+\mathcal B_{A_{H_j,d_j}}(T_j)\},
\qquad \ell_j>0,\quad T_j\in\mathcal W.
\tag{16}$$

施加 $\Lambda$ 后，其值准确为

$$\sum_{j=1}^m\ell_jH_j^n>0.\tag{17}$$

所以 (16) 不能为零。这个负结论甚至允许任意正实长度，因而包含真实正整数整圈子类；未用负长度或空 helper。

反之，假设 $b\in\mathcal R_*$。由不变性，每个 $b_{H,d}$ 都在 $\mathcal R_*$。取 R90 的七个具体状态

$$\mathcal S_*=
\{(1,-2),(1,-1),(1,0),(1,1),(1,2),(2,0),(2,1)\}.$$

每个状态取一个正完整 frame 周期，长度相同且为 $\ell=\sqrt2\pi$。七个状态提供的全部响应恰为 $\mathcal R_*$，而它们的基准和也在该空间中。因此存在七个真实 $T_s\in\mathcal W$ 使

$$\sum_{s\in\mathcal S_*}
\{b_s+\mathcal B_{A_s}(T_s)\}=0.
\tag{18}$$

由 R80，各 $T_s$ 的差可用有限真实控制环实现；由 R89，在同一全局 profile、同一右锚和真实历史下，跨 pair 连接不漏入新的 P1 项。七个 helper 的正基准已完整包括在 (18) 中，不是把它们的长度设为零。实际 P1 为 (18) 的共同因子 $4\sqrt2\pi$，故为零。

这只给有限路径在 P1 层的存在性。实际控制系数可为实数；这里七个 bulk 长度已是完整圈整数，不需要把一个未知的实正锥权向量近似成有理数。

## 6. 泛函的真实含义与不可外推的范围

式 (2) 的 $\Lambda$ 定义在真实 profile 算子空间，不是某个形式项的系数投影。因为 $\mathcal V$ 有限维，普通函数评价分离它的元素，所以 $\Lambda$ 可以写成有限个真实评价的实线性组合：评价数据可包含不同的实 profile 对、不同查询点和不同模式的实部或虚部。

理由是：若这些评价的线性 span 不是 $\mathcal V^*$，则存在一个非零 $v\in\mathcal V$ 被所有评价湮灭；按真实函数等式定义，这正是 $v=0$，矛盾。但这个有限评价表示一般可能需要多个不同 profile，本文没有证明可以只用某一固定 profile。

因此，负分支排除的是 universal 算子身份，即同一组几何控制对所有 profile 同时有效。它不排除针对某个特殊 profile 选择控制后支付 P1，也不排除某个三矩圆。若要对固定 profile 得到负结论，仍需 R87 那样在同一 profile 上湮灭所有真实控制列的准确泛函；R86 的左补偿也只能在它自己的共同区间和右因果条件内使用。

当前 R87 已证明标准单 pair 的一个固定 profile 目标不在该单状态响应像中。它没有证明 $b\notin\mathcal R_*$，因为后者允许全部状态的联合控制。两状态任务同样不能仅凭一个未产生关系的正规形，宣布本定理进入负分支。

正分支也仍只支付 universal P1。真实控制环和连接的 $P_0$、完整第四 ruling、所有更高阶、收敛、闭面嵌入、reach 与宏观位移都没有因此支付。固定有限 $N$ 的 $P_0+NP_1$ 还可能有本定理之外的控制机制。

## 7. 可操作的有限后续目标

R90 将全部状态控制压到最多 $7\cdot36=252$ 个真实生成方向；本定理进一步说明，在 universal 算子层，不必同时盲搜任意多个正状态权。决定性的成员问题只有

$$\boxed{b\stackrel{?}{\in}\mathcal R_*.}\tag{19}$$

若找到正关系，须从原始两模式表达式复核；然后七个正整圈 helper 已足够构造 P1 方案。若能证明真实非成员，(2) 保证存在一个不依赖平移 $d$、对缩放只有正整权 $H^n$ 的分离泛函。实际寻找该泛函可先保留真实平移像 $N\mathcal V$ 再分解缩放权，但不能把未经证明的代表秩当作 (19) 的答案。

这没有增加已冻结两状态任务的状态数或预算，也没有在本地执行任何完整目标编译、profile 积分或候选计算。
