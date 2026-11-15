# R351 完整 literal 七状态离散链的三列伴随与新增零jet控制响应

作者：ChatGPT /root/amplitude；日期：2026-11-15。

状态：条件准确实数代数、冻结源码对应与可实施接口。本文不调用新的科学计算，不给实际157的未知矩阵、秩或驻点结论，也不把Decimal50或IEEE算术形成的导数当成准确导数证书。原163只读结果与本证明是两条不同责任。

## 1. 对象、固定系数与实际源码

对象是已冻结 geometry_20261115_nine_control_decimal_literal_model.py（2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75）中 LiteralCircleModel._evaluate 的完整699节点、698区间、三低模及完整112右残差有限模型。154/157的二阶实现继承其同一primal表达；本文不把该有限模型改成连续ODE，也不把其固定binary64表重新解释为准确连续几何系数。

网格、步长、node/mid基函数表、三个频率、cut scale、height sign、原112×112尾端J及三个target作为明确字面输入。模型将原binary64词准确提升为Decimal输入；运行中的乘除、平方根和累加仍有舍入。

准确实数证明采用这些有限字面系数作为实常数，并把原算术表达解释为实数表达。另行说明形成的局部线性化在浮点下能代表什么。两者不能混写。

当前实际模型先形成标量表 $(a,a')$，然后取

$$
q=\frac{a'}a.
$$

这里 $a'$ 的坐标必须与原表第二列相同。若新shape以归一化公共坐标定义，其导数需要原完整坐标链因子；不能直接把公共坐标导数填进原物理导数列。

令 $N=698$，节点为 $j=0,\ldots,N$，中点为 $j+\tfrac12$。使用三个平方频率 $\kappa\in\{4,16,36\}$。原初始化为 $r_0=1$，各模态 $y_0^{(\kappa)}=(1,0)^T$。所有新shape仍以同一个完整有限模型评价，不覆盖这些原初值。

## 2. 七状态的完整单元映射

定义

$$
x_j=\bigl(r_j,y_j^{(4)},y_j^{(16)},y_j^{(36)}\bigr)\in\mathbb R^7,
\qquad z_j=(q_j,q_{j+1/2},q_{j+1})\in\mathbb R^3.
$$

单元步长为固定 $h_j$。原半径消元系数为

$$
\ell_j=-1-\frac{h_j(q_j+2q_{j+1/2})}{6}
-\frac{h_j^2q_{j+1/2}q_j}{12},
$$

$$
\rho_j=1-\frac{h_j(q_{j+1}+2q_{j+1/2})}{6}
+\frac{h_j^2q_{j+1/2}q_{j+1}}{12}.
$$

当 $\rho_j\ne0$ 时，

$$
r_{j+1}=-\frac{\ell_jr_j}{\rho_j},
\qquad
r_{j+1/2}=\frac{r_j+r_{j+1}}2
-\frac{h_j(q_{j+1}r_{j+1}-q_jr_j)}8.
$$

在三个局部位置定义 $s=qr$、$v=\sqrt{1-s^2}$。原矩阵逐项为

$$
B_\kappa(q,r)=
\begin{pmatrix}
q(1-\kappa)&-v\kappa/r\\
s\,q(\kappa-1)/v&q\kappa
\end{pmatrix}.
$$

实现应保原先形成 $s=qr$ 再作下行乘除的顺序；上式作为实数公式可化简，不能据实数恒等式宣称重新形成的浮点词不变。

记 $B_L,B_M,B_R$ 为上述三个实际局部位置的同一模态矩阵，原两个2×2行块是

$$
L_{j,\kappa}=-I-\frac{h_j(B_L+2B_M)}6
-\frac{h_j^2B_MB_L}{12},
$$

$$
R_{j,\kappa}=I-\frac{h_j(B_R+2B_M)}6
+\frac{h_j^2B_MB_R}{12}.
$$

在 $R_{j,\kappa}$ 可逆时，

$$
y_{j+1}^{(\kappa)}=-R_{j,\kappa}^{-1}L_{j,\kappa}y_j^{(\kappa)}.
$$

因此存在明确的完整映射

$$
x_{j+1}=\Phi_j(x_j,z_j).
$$

半径是此映射的第一状态，绝不能只反传三个模态而冻结 $r_j$、$r_{j+1/2}$、$s$ 或平方根。原高度累计不进入本有限三残差的右端，因而不必放进最小七状态；原最终circle/几何高度检查仍须完整执行，不能因本伴随不使用它就删除该最终责任。

**光滑域。** 准确实数证明要求涉及的 $r$ 为正、$1-(qr)^2>0$、$\rho_j\ne0$ 且三个 $R_{j,\kappa}$ 可逆。在这个开域内，每个 $\Phi_j$ 光滑。接近域边界、有限程序某个除数成为零或分支改变时，本证明不提供跨边界可微性或有限差分有效性。

## 3. 完整终端映射与不能删掉的直接项

记 $e_2=(0,1)^T$，$J$ 为原完整112×112字面尾端矩阵，$\gamma$为原cut scale，$\varepsilon$为原height sign，$t_k$为原三个target。令

$$
\psi_k=e_2^TB_{\kappa_k}(q_N,r_N)y_N^{(\kappa_k)},\qquad
n_k=\varepsilon t_k e_2^Ty_N^{(\kappa_k)}\quad(k=0,1,2),
$$

且 $n_k=0$ 对其余109项。完整右残差为

$$
\mathcal R_i=-\gamma\sum_{\ell=0}^{111}J_{i\ell}n_\ell
+\mathbf 1_{i<3}t_i\psi_i,\qquad i=0,\ldots,111.
$$

即使只有三项 $n_\ell$ 非零，也必须保完整112行及原所有非对角耦合；不能从“只有低三模”推高109右残差为零。源码的 exactly_diagonal_as_original_record 是已经绑定的有限矩阵属性，不能由小数值或近似对角性临时替代。

当原固定分支为exactly_diagonal时，原优化三残差是

$$
F_k=\psi_k-\gamma\varepsilon J_{kk}e_2^Ty_N^{(\kappa_k)}.
$$

否则原优化三残差为 $\mathcal R_{0:3}$。这是原源码的两种固定定义，伴随必须使用该次真实分支，不能把其中一种重新命名为另一种。

把优化三残差写成

$$
F=T(x_N,q_N;\theta)\in\mathbb R^3,
$$

其中 $\theta$ 收纳所有固定终端输入。直接终端项包括：

- $B_\kappa(q_N,r_N)$ 对 $q_N$ 的直接变化；
- $B_\kappa$ 对 $r_N$ 的变化，属于 $T_x$ 而非应被删掉的常数；
- 三个 $y_N$ 的变化；
- 若另一个问题让 $\gamma,\varepsilon,J,t$ 变化，则还有 $T_\theta\,\delta\theta$。

例如完整 $\mathcal R_i$ 的变化始终是

$$
\delta\mathcal R_i
=-\delta\gamma\sum_\ell J_{i\ell}n_\ell
-\gamma\sum_\ell\delta J_{i\ell}n_\ell
-\gamma\sum_\ell J_{i\ell}\delta n_\ell
+\mathbf1_{i<3}(\delta t_i\,\psi_i+t_i\,\delta\psi_i).
$$

本有限模型固定 $\theta$，因此其 $\delta\theta=0$ 是对象定义给出的结论。它不能转用到真正current native/fullDN中而漏掉当前响应的重新形成。新增紧支撑零jetshape也不能作为删除原112终端矩阵、target或cut责任的理由。

## 4. 三列离散伴随恒等式

在上述光滑域取准确局部导数

$$
A_j=D_x\Phi_j\in\mathbb R^{7\times7},\qquad
C_j=D_z\Phi_j\in\mathbb R^{7\times3}.
$$

这里 $C_j$ 仅表示三个局部 $q$ 输入导数，与其他课题中的投影C或native momentum C无关。

取三列终端伴随

$$
\Lambda_N=(D_xT)^T\in\mathbb R^{7\times3},
\qquad
b_N^{\rm direct}=(D_qT)^T\in\mathbb R^{1\times3},
$$

并反向递推

$$
\Lambda_j=A_j^T\Lambda_{j+1}.
$$

单元三输入贡献为

$$
G_j=C_j^T\Lambda_{j+1}\in\mathbb R^{3\times3}.
$$

其三行分别加到node $j$、mid $j+\tfrac12$、node $j+1$；node $N$另加 $b_N^{\rm direct}$。这些位置共享同一个 $q$ 输入，必须累加，不能重复视作相互独立的物理设计量。

由
$\delta x_{j+1}=A_j\delta x_j+C_j\delta z_j$，
逐项相乘得到

$$
\Lambda_{j+1}^T\delta x_{j+1}
-\Lambda_j^T\delta x_j
=\Lambda_{j+1}^TC_j\delta z_j.
$$

对所有单元求和即得

$$
\boxed{
\delta F
=\Lambda_0^T\delta x_0
+\sum_{j=0}^N w_j\,\delta q_j
+\sum_{j=0}^{N-1}w_{j+1/2}\,\delta q_{j+1/2}
+D_\theta T\,\delta\theta.
}
$$

其中 $w$ 是上述累加后的三维列向量。证明是完整有限链的望远镜相消，不需要可逆 $A_j$，也不对传递矩阵作长距离显式连乘。只要局部映射的导数存在，就能对全部三个输出同时进行一次反向递推。

**原start项。** 对当前固定模型，$x_0=(1,1,0,1,0,1,0)$ 不依赖九参数，故 $\delta x_0=0$。这不是“高模很小”或“shape在左端小”的近似。若后续模型改变初始归一化、初始模态或延拓种子，则该项必须恢复；helper应返回 $\Lambda_0$，不能将其永久丢弃。

## 5. 从每个q输入收缩到实际C²零jetshape

设 $h$ 是原标量系数的实际变化，$\delta a=h$、$\delta a'=h'$，且 $a\ne0$。准确商法则给出

$$
\delta q=\frac{a h'-a'h}{a^2}.
$$

以原固定node/mid位置采样这一表达，代入伴随恒等式，得

$$
D F[h]
=\sum_jw_j\frac{a_jh'_j-a'_jh_j}{a_j^2}
+\sum_jw_{j+1/2}
\frac{a_{j+1/2}h'_{j+1/2}-a'_{j+1/2}h_{j+1/2}}{a_{j+1/2}^2},
$$

这里已明确使用当前固定start及固定终端输入。若新shape的定义还影响这些输入，就必须加回上一节的start/直接终端项。

例如 $h=bP$，其中 $b,b',b''$ 在支持端点都为零，$P$是端点附近光滑的多项式，则

$$
h=bP,\quad h'=b'P+bP',\quad
h''=b''P+2b'P'+bP''
$$

在两个端点均为零。把其延拓为支持外零函数，所得shape为C²且有零2-jet。这个结论只说明函数族的拼接责任，不说明其响应非零或补秩。

若支持严格在固定初末端点内部，$h=h'=0$ 于末节点，故这一shape的 $\delta q_N=0$，直接 $D_qT$ 项对它的收缩消失；但通过链传递产生的 $\delta r_N,\delta y_N$ 通常不为零，不能因此删整个终端导数。helper仍保所有节点权重和终端直接项，允许独立核这项确实因所给shape的零jet而消失。

原九列本身也是这一公式的特例：$h_i$等于原control表第i列所代表的shape。可与同一点原完整forward9动作作只读差异报告。但有限差异不等于证明准确，出现差异时不能把新伴随自动宣布优于原forward。

## 6. 新增方向能够解决什么

令 $J_{\rm old}\in\mathbb R^{3\times9}$ 为准确旧九列响应，新增shape响应为 $K\in\mathbb R^{3\times m}$。则

$$
\ker[J_{\rm old},K]^T
=\ker J_{\rm old}^T\cap\ker K^T.
$$

因此扩展响应满行秩，当且仅当旧响应左零空间中没有非零向量同时湮灭所有新增响应。单纯使用可逆九维换基不会改变旧响应的准确秩；新增函数在函数空间线性独立，也不推出 $K$ 去掉了旧左零空间。二者必须分别说明。

对原全三merit $W=\tfrac12F^TF$，新shape方向的准确斜率为

$$
D W[h]=F^TD F[h].
$$

若该数不为零，则选择 $\eta=-\operatorname{sign}(D W[h])$，准确方向 $\eta h$有严格负斜率。只要原当前点处于合法开域、目标可微，就存在足够小的正步长满足原Armijo条件

$$
W(p+\alpha\eta h)
\le W(p)+c_A\alpha\,D W[\eta h],
\quad
c_A=\frac{3602879701896397}{18014398509481984}.
$$

$c_A$是原binary64字面0.2的准确提升，不是新换成有理数 $1/5$。存在性来自一阶展开及 $0<c_A<1$；有限20档不保证命中，形成的Decimal50斜率也没有自动证明其准确符号。真实接受仍必须由原完整非线性评价、原域和原字面Armijo完成。

该命题不要求改变全三残差权重、舍弃某个方程或引入额外inner-target门。它也不保证存在有用新增shape、一次大下降、完整方程有根或最后非零场成立。若所允许shape空间被同一个准确非零左泛函全部湮灭，这种局部扩展也不能恢复该行方向；需要如实记录，而不是无限增加同类小步。

## 7. 浮点形成的局部线性化与误差边界

实际helper可以沿同一原局部表达，用原Jet在每cell的七状态和三个q输入上形成7×10的局部变分，再反传三列。它复用原2×2显式det/回代算术、原矩阵乘积顺序和平方根路径；不能只以一个理想逆矩阵公式替代具体程序而宣称浮点字面导数一致。

必须区分：

1. **准确实数有限模型。** 从原字面系数出发，用准确实数执行原表达和准确导数，前述恒等式严格成立。
2. **形成系数的线性系统。** 给定任意已形成矩阵 $\widehat A_j,\widehat C_j,\widehat T_x,\widehat T_q$，把它们当准确实系数，正向线性递推与反向收缩之间仍有同一代数恒等式。
3. **实际Decimal计算。** 原primal、局部Jet、反向矩阵乘法和shape收缩各有舍入；实际存档状态可能不是准确实轨迹，各局部形成系数也未被区间包围。这是新的近似动作，既非IEEE离散舍入映射的导数，也非已证明的准确实导数。

若需要后验界，可将真局部系数与形成系数之差及primal轨迹误差显式列为 $E_{A,j},E_{C,j},E_{T,x},E_{T,q}$。对任意给定方向，正向误差可按

$$
\|e_{j+1}\|
\le \|A_j\|\,\|e_j\|
+\|A_j-\widehat A_j\|\,\|\widehat{\delta x_j}\|
+\|C_j-\widehat C_j\|\,\|\delta z_j\|
+\text{明确的形成/传播舍入界}
$$

逐步外包，再带入终端直接项。没有这些有效外包，就不能用原FD的整列relative error替代最小奇值或弱方向的误差证书。本文不凭原未读矩阵填写任何此类误差上界。

局部primal回放与原state的逐word比较可定位重形成差异；比较为true也只证明这些有限输出词一致，不能越级成为全变分准确性证明。原parameter50位字符串是真实有限输入，不伪称对应未知更高精度解。

## 8. 最小可实施接口及工作量

独立requestless helper可提供：

- 从原真实model/state建立698个局部7×10变分及终端完整112/原三输出的8输入变分；
- 完整三列反向链与node/mid三行权重，保start cotangent、直接末节点q项、原完整终端J及分支身份；
- 对显式提供的node/mid shape值与同坐标导数表作收缩；
- 对旧九列表输出同点的原forward读回差异，并为新增shape输出完整三响应及完整112终端响应责任；
- 记录每个局部primal的原字比较、来源、费用和异常，但不据此新增科学接受门。

698次局部10列forward及一次三列reverse的成本与新增shape数分离。取得权重后，每个shape只需在1397个实际node/mid点收缩；这比为大量候选shape各自重新跑完整699节点forward更适合先选择有实际响应的新方向。局部7×10表和权重为Actions临时数据，可在使用后销毁，只按规则保源码/参数/运行及完整选择读回。

完整112新shape响应可通过同一局部线性化前传所给shape的7状态，再乘已保完整112终端导数及直接项；不重新导入旧native初猜，也不冻结高109行。主优化的三列伴随与完整112责任因此明确分工，不能以三列伴随替代真正非线性native、cut sensitivity、全场FD、fullDN或final audit。

本接口不选择尚未读回的父点、新shape阶数、支持或运行编号，不改现157/163科学源。实际实施应先使用已确认原参数来源，再明确新族及新producer身份；所有新科学算术仅在公开Actions中执行，原全三merit、域、预算及最终门保持。
