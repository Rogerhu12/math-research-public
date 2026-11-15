# R302. 共享有限 root 轨迹的批列等价与完整112两端响应

类型：已证明；有限实表达、固定执行分支下的条件定理。  
作者：exact_refinement（AI协作）；日期：2026-11-15。

本结果接[R283](R283-finite-root-trace-differentiation-with-literal-tables.md)，只证明新增的共享轨迹执行、全列线性组合和完整两端消去；不把源码发布、浮点非零pivot或有限残差当作严格非共振证明。当前独立实现见[完整接口](../notes/2026-11-15-native-persistent128-final-components-and-shared-trace-interface.md)。源码在公开提交d70e89b2b0ded8a694dfcce1e94bf90c25b483ec中；本文没有新的数值结果。

## 302.1 固定的对象和三个不同层次

取一个真实保存的全节点状态 $y=(y_0,\ldots,y_D)$，其中 $y_n\in\mathbb R^{2m}$。本课题有限布局为 $m=112,D=576$，全状态每段加两个mean分量后为226维，原边界及shooting行数为

$$
m+2mD+m=2m(D+1)=129248.
$$

每个原root/RK查询的几何、角表、gram表和常数是各自实际导出的有限字面数。它们不由一个较短“理想表”互相推导或覆盖；特别是原 $F$ 与迭代矩阵 $C$ 各按其完整原公式、独立表和求和路径定义。本文不假定 $C=F_e$。

必须区分：

1. 将这些字面数解释为准确实数、固定每个已实际选中的分支后，得到的有限实算术表达；
2. 在binary128等有限算术中数值评价上述表达的链式微分；
3. 包含每次IEEE舍入及分支选择的离散程序映射。

本文的导数定理针对第1层。第2层是实现的数值近似，需要自己的读回、误差和条件性评价；本文不证明其数值误差界。本文不声称第3层的导数等于第1或第2层。共享一份名义轨迹还不证明邻域中分支不变。

所有参与公式的实平方根自变量须严格正、三角对角须非零、其余显式分母须非零。若实际分支的每次停止、回溯、域测试均有相应严格余量，则有限次连续测试在一个邻域保持该轨迹，下面的导数也就是该邻域内所选实程序的导数。处于比较边界时，只保留强制固定轨迹表达的导数解释，不补作稳定性结论。

## 302.2 一份实际轨迹足够供任意多列复用

一次成功root调用从 $e^0=0$ 开始。在第 $i$ 个实际接受的更新之前，记录

$$
e^i,\quad F_i=F(e^i,t,x),\quad
C_i=C(e^i,t,x),\quad
C_i=L_iL_i^{\mathsf T},\quad
L_i u_i=F_i,\quad L_i^{\mathsf T}s_i=u_i,
$$

以及该更新的实际回溯数 $k_i$，即 $\alpha_i=2^{-k_i}$。实际更新是

$$
e^{i+1}=e^i-\alpha_i s_i.
$$

这里 $x$ 是完整当前输入，$t$ 是按原Pi/几何字面数形成的目标。记录使用接受更新**之前**的 $e^i,F_i,C_i,L_i,u_i,s_i$。被拒绝试探、末停止条件和fallback分支只决定这份有限轨迹，不作为一个额外接受更新加入。

设输入的任意 $b$ 个方向为 $v_1,\ldots,v_b$。对每列分别按R283微分，取 $\dot e^0_j=0$，且

$$
\dot F_{i,j}=D F(e^i,t,x)
      [\dot e^i_j,\dot t_j,v_j],\qquad
\dot C_{i,j}=D C(e^i,t,x)
      [\dot e^i_j,\dot t_j,v_j].
$$

对第 $j$ 列的Cholesky微分、前代回和后代回仍为R283的逐项公式：

$$
\dot L_{ii}=
\frac{\dot C_{ii}-2\sum_{k<i}L_{ik}\dot L_{ik}}
     {2L_{ii}},
$$

$$
\dot L_{ij}=
\frac{\dot C_{ij}
-\sum_{k<j}(\dot L_{ik}L_{jk}+L_{ik}\dot L_{jk})
-L_{ij}\dot L_{jj}}{L_{jj}},\qquad i>j,
$$

$$
L\dot u_j=\dot F_j-\dot L_j u,\qquad
L^{\mathsf T}\dot s_j=\dot u_j-\dot L_j^{\mathsf T}s.
$$

随后

$$
\dot e^{i+1}_j=\dot e^i_j-\alpha_i\dot s_{i,j},
\qquad
\dot L_{\mathrm{return},j}=\dot t_j+\dot e^{\mathrm{last}}_j.
$$

最后一式中的 $L_{\mathrm{return}}$ 是root返回的动量系数，和Cholesky因子 $L_i$ 是不同对象。

**命题302.1。** 在302.1的条件下，对任意有限列数 $b$，先只算一次名义轨迹并保存上述中间量，再逐列执行这些微分，与分别在同一名义输入上重新执行相同强制轨迹的 $b$ 次R283单列微分，在准确实算术中结果相同。

**证明。** 名义 $e^0,t,x$ 与所选轨迹相同，因此各次单列计算的全部名义 $e^i,F_i,C_i,L_i,u_i,s_i$ 相同。第0次方向初值也相同。若某次更新前的方向相同，$DF$、$DC$作用于同一方向三元组，所得 $\dot F,\dot C$ 相同。Cholesky公式按行列递推且对角非零，故 $\dot L$唯一相同；两次三角代回解唯一，故 $\dot u,\dot s$相同；用同一个实际 $\alpha_i$ 更新，下一次 $\dot e$相同。有限归纳至返回点，返回系数及每个角行的微分相同。无更新直接返回时，归纳为空，仍有 $\dot L_{\mathrm{return}}=\dot t$。fallback返回当前 $e$时也不添加一个不存在的更新。证毕。

这个论证只要求按实际公式分别微分 $F,C$，从未使用 $C=F_e$；也不把有限Newton求解改成一个隐式精确根。

**数值实现边界。** 若两种数值实现的名义字逐项相等，且每列方向运算的括号、顺序和舍入环境相同，则相同操作的确定性给出逐字相等。新源码仍对每列执行R283的完整F/C value-shadow身份检查。它共享的是实际root分支搜索、名义Cholesky和名义代回，不保证所有名义运算已消除，也没有已支付的速度提升比例。若将来改用不同批量求和或BLAS顺序，则只能先援引实表达等价，不能沿用逐字相等结论。

## 302.3 共享完整四field后再做RK列递推

对一个原原子步记其完整226维RHS为 $f$、步长为 $h$。四个名义field分别是

$$
a=f(y),\quad b=f(y+ha/2),\quad
c=f(y+hb/2),\quad d=f(y+hc).
$$

每个field均按302.2保存自己的实际root轨迹。任一方向 $v$ 的更新为

$$
\begin{aligned}
\dot a&=Df(y)v,\\
\dot b&=Df(y+ha/2)(v+h\dot a/2),\\
\dot c&=Df(y+hb/2)(v+h\dot b/2),\\
\dot d&=Df(y+hc)(v+h\dot c),\\
v^+&=v+\frac h6(\dot a+2\dot b+2\dot c+\dot d).
\end{aligned}
$$

四个名义field及其括号完全在列循环之前确定；方向不得反馈进名义状态。对每个已保存的原cusp原子步依次应用命题302.1和链式法则，即得到整个原段的方向映射。几何、步长和分段点固定为导出的各自字面数，不把 $h$换成一个不同舍入路径下的端点差。

因此在准确实算术中，整个段微分对输入方向线性。给定全224个shape基向量、两个mean初方向为0，所得226×224矩阵记为 $\widehat T_n$。在第 $n$ 段结束后，原Pi端口除以该段实际ratio；Q行及两mean行不除。把shape端口后的224×224矩阵记为 $T_n$，两mean行记为 $B_n\in\mathbb R^{2\times224}$。

段 $n$ 的输入节点是 **$n+1$**，输出节点是 **$n$**。全shooting线性化的段行是

$$
T_n h_{n+1}-h_n.
$$

不把节点方向反接，不把端口前矩阵用于端口后原行，也不清除cut或far分量。

## 302.4 完整两端边界问题及唯一性条件

记 $P_Q,P_\Pi$为选取前后 $m$行的投影，原末端图为 $G_D$。给定完整物理高度变化 $\delta H\in\mathbb R^m$及明确声明的cut强迫矩阵 $F_H\in\mathbb R^{m\times m}$，有限线性边界问题为

$$
P_Q h_0=F_H\delta H,\qquad
h_n=T_n h_{n+1}\ (0\le n<D),\qquad
P_\Pi h_D=G_D P_Q h_D.
$$

令

$$
U_D=\begin{pmatrix}I_m\\G_D\end{pmatrix},
\quad
A_0=T_0T_1\cdots T_{D-1}U_D,
\quad
C_0=P_Q A_0.
$$

**命题302.2。** 上述问题对每个右端 $F_H\delta H$有唯一解，当且仅当cut参数映射 $C_0$可逆；这里“每个右端”指任意cut Q右端，或者假定 $F_H$可逆。若只给一个秩亏强迫族，则其相容性不推出对任意cut右端的唯一可解性。

**证明。** far条件准确等价于存在唯一 $a\in\mathbb R^m$使 $h_D=U_Da$，因为 $P_QU_D=I_m$。所有段等式再唯一确定 $h_n=T_n\cdots T_{D-1}U_Da$，故cut条件化为 $C_0a=F_H\delta H$。$C_0$可逆给存在唯一解；若它不可逆，则齐次问题有非零 $a$及非零 $h_D$，所以不能对任意cut右端唯一可解。证毕。

该命题保全部112个自由far模态；“高109”没有被删去，也没有将无穷尾非共振当作一个已付条件。当前 $G_D$本身是实际有限模型输入，本文不证明其对真实无限尾的误差界。

## 302.5 不形成完整乘积的全维QR传递

直接形成 $A_0$不是证明或求解的必要步骤。先做完整列QR

$$
U_D=Z_D R_D,\qquad Z_D^{\mathsf T}Z_D=I_m.
$$

依次从 $n=D-1$到0做

$$
T_n Z_{n+1}=Z_n R_n,\qquad Z_n^{\mathsf T}Z_n=I_m.
$$

所有 $R_n$均为 $m\times m$。设这些列QR均满列秩，且 $P_Q Z_0$可逆。对完整112个高度列，定义

$$
C^{\mathrm{resp}}_0=(P_QZ_0)^{-1}F_H,\qquad
C^{\mathrm{resp}}_{n+1}=R_n^{-1}C^{\mathrm{resp}}_n,\qquad
X_n=Z_n C^{\mathrm{resp}}_n.
$$

**命题302.3。** 每个 $X_n\in\mathbb R^{2m\times m}$的所有列恰为命题302.2的节点响应；此算法不需要形成normal matrix，也不需要截去弱奇异列。

**证明。** cut式直接给 $P_QX_0=F_H$。由QR关系，

$$
T_nX_{n+1}
=T_nZ_{n+1}R_n^{-1}C^{\mathrm{resp}}_n
=Z_nC^{\mathrm{resp}}_n=X_n.
$$

$Z_D$与 $U_D$列空间相同，故 $X_D$满足far条件。这些等式给存在性。反向任何满足far和段方程的响应都在这些满秩列空间内，cut处由可逆 $P_QZ_0$唯一确定系数，再由各可逆 $R_n$唯一恢复，因此解唯一。证毕。

这里的 $R_D$只为给 $U_D$的正交基，不参与从 $C^{\mathrm{resp}}_0$向外的递推；不额外乘它或漏掉一个stage因子。

若 $C_0$可逆，则每个到cut的前缀复合都不能把far列空间压低秩。因此上面所需的各满列秩条件在准确实模型中成立，且 $P_QZ_0$可逆。反之，算法的这些条件也给命题302.2的唯一性。它们是准确实条件；在浮点源码里仅检查计算到的pivot非零，不构成这些条件的严格认证。

## 302.6 全部原行和两个mean的可核对身份

对于任意数值计算得到的全部 $X_n$，必须分别读回

$$
E_{\mathrm{cut}}=P_QX_0-F_H,
$$

$$
E_n=T_nX_{n+1}-X_n,\qquad 0\le n<D,
$$

$$
E_{\mathrm{far}}=P_\Pi X_D-G_D P_QX_D.
$$

按cut112、全部576×224段行、far112的原顺序叠成129248×112矩阵。取实际原 $\sigma_n>0$时，可以报告每个行/列的原尺度读回及最大项；完整行账不能只由少数最坏行替代。

准确实求解时这些矩阵全为0。浮点读回不是严格外包；很小的读回只有在另付逆算子或条件界时才能转换成响应误差界。本文不把它设为原非线性接受前的新门。

两个mean方向在每段独立从0开始。第 $n$ 段两行响应是

$$
M_n=B_n X_{n+1},
$$

完整总mean-height响应为按原累加定义把两行及全部段相加。端口只作用shape Pi行；不对mean加ratio，也不凭几何mean理论不依赖shape便删掉实际第二行的原数据。

## 302.7 物理高度列与338行不能偷换对象

当前独立实现明确采用局部cut扩展

$$
Q_{\mathrm{target}}(H+\delta H)
=Q_{\mathrm{saved\ target}}+r^{-4}\delta H,
\qquad
F_H=r^{-4}I_m.
$$

其中半径及求幂括号按该新接口声明；保存的原target字不被重新计算替换。这是局部实表达/数值扩展，不是原IEEE除法映射的导数。cut的profile(1)值和末RK查询geometry若在原有限路径下相差末位，两者均保留并记录，不能强行据字不同就把它们合并。

令 $G_0=P_\Pi Z_0(P_QZ_0)^{-1}$。原cut物理jet程序接收节点Pi时还乘自己的实际 $\rho$。所以对cut Q的第 $k$个方向，root/RHS变分的完整种子是

$$
(e_k,\rho G_0e_k,0,0).
$$

第一slope行的完整链式规则为

$$
D_H(\mathrm{slope})_{\cdot k}
=\frac1{r_x}D_y(\mathrm{RHS}_Q)
  [(e_k,\rho G_0e_k,0,0)]
+\frac4r e_k.
$$

meanSlopeCorrection的列为

$$
D_H(\mathrm{meanSlopeCorrection})_k
=\frac1{r_xr^4}D_y(\mathrm{RHS}_{\mathrm{mean}})
 [(e_k,\rho G_0e_k,0,0)].
$$

这两式是原cut第一导数表达的链式规则；实现还保存RHS表达和原直接cut表达的实际名义读回，避免把有限路径的恒等式误说成逐字相同。

原338行顺序是slope112、second112、meanSlopeCorrection、meanSecondCorrection、height112。当前实现沿原worker合同，仅第一112和meanSlope行采用上述有限轨迹RHS微分；second及meanSecond仍按原C-based物理jet程序在完整 $G_0$图上的对称差分，height保原对称差分读回。因此即使338×112全部形成，也不声称338行均已得到准确解析Jacobian，不声称原second的有限差分误差已被严格控制。

## 302.8 物理审计和最终接受仍是独立责任

完整段变分、全112边界逆和338读数只支付各自声明的有限对象。原物理审计另从每个真实128节点 $n+1$开始，按自己的profile/k闭查询和原cusp-aware推进重新求根、计算全部角行。不能把段RK的四field抽样充当原audit所有查询。

原physical jet中径向动量导数由原 $C$方程形成。这是一个独立有限程序；它一般不能仅因名字叫radial derivative就等同于实际有限root轨迹对半径求导。将来要付后一对象，须按原几何变化、独立字面表语义及完整已选root轨迹另作微分，或者证明所需误差/等价条件。本文不把这一差别抹掉。

因此下列蕴含全部不成立：

- 224个段列完整 $\Rightarrow$ 全112两端响应已求出；
- 两端线性读回小 $\Rightarrow$ 原非线性native已接受；
- 338×112数组完整 $\Rightarrow$ 全部338行均为解析导数；
- 原C-based物理程序审计完成 $\Rightarrow$ 连续ODE/真实无限尾/同场metric证书完成；
- 末点满足某个shooting容差 $\Rightarrow$ 原fullDN的真实当前H、FD、最终J和fresh audit责任都已完成。

实现只允许按实际完成范围分别置相应组件flag；没有完成的阶段、列、角查询、审计或源现场不得靠旧64数据、删除后的hash或另一状态的回执填补。共享轨迹证明和源码发布也不把这些flag预先置真。
