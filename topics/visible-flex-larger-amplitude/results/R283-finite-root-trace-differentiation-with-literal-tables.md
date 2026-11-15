# R283：固定字面系数与固定执行分支下，有限root迭代的完整变分

AI 协作证明：ChatGPT，2026-11-15 UTC。

## R283.1 对象与范围

本结果针对 `geometry_20261115_native_primal128.cpp`，源码SHA256为
`1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d`，具体函数为 `root_evaluate`、`root_matrix`、`spd_solve`、`root`、`rhs`、`rk4`。输入packet由原113 bridge生成，SHA256为
`3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8`。

所有原64几何样本、角表、常量、步长、port ratio、scales及far graph，分别解释为其已保存字面值所代表的实数。不同数组不通过连续恒等式重新定义。特别地，cosine、sine与gram是三个独立的固定系数数组；$w,w^2,E$也是分别给定的系数。本结果不要求它们满足理想三角乘积恒等式或 $E=1+w^2$ 的精确实数关系。

“实表达式延拓”指保留源码的各个表达式和迭代步骤，以实算术解释其加、减、乘、除、正平方根与线性代数循环。它不同于逐原语舍入的IEEE程序。证明没有把浮点舍入函数称为光滑函数，没有证明任何当前计算点的branch稳定性、矩阵误差界或非线性收敛，也没有提供新的native成功锚。

## R283.2 实际迭代中的两个映射

记 $M=112$、$J=M+1=113$，shape输入为 $y=(Q,\Pi)\in\mathbb R^{224}$。一次RHS现场的几何、cell参数和角表固定。源码的momentum目标为

$$
t_0(y)=0,\qquad t_{j+1}(y)=\gamma\Pi_j,
\qquad
\gamma=\frac{\mathrm{orientation}\,\sqrt{12}_{\mathrm{lit}}\,\mu}
{\sqrt2_{\mathrm{lit}}\,r^4w^2},
$$

其中各个乘除仍按原表达式理解，$r^4$来自原两次平方。

给定 $e\in\mathbb R^J$，令 $L=t(y)+e$，按 `root_evaluate` 的原有限角和形成

$$
F(e,y)=e+q(L,Q).
$$

另定义

$$
C(e,y)=\texttt{root\_matrix}(\texttt{root\_evaluate}(e,y).\mathrm{rows}).
$$

$C$是源码实际用于Newton步的矩阵，不是以“$F_e$”作为定义。二者是否在某个实际输入上相等，是另一项有限系数问题。本结果既不假定 $C=F_e$，也不凭不同源码表达式就宣称已经测得当前输入的逐项差异。

为使这两个有限映射明确，在角点 $n$，`root_evaluate` 先按原cosine/sine字面表得到 $P,P_t,L_v,U$，然后形成

$$
\begin{gathered}
K=L_v-P_t,\quad T=2K+K^2+EP^2,\quad u=w^2T,\\
D=1-u,\quad S=1-w^2P^2,\quad A=1+L_v+w^2P_t,\quad a=\sqrt D,\\
f_c=\frac{u(2+a)}{2a(1+a)^2},\qquad
g_c=\frac{w^2(P^2+ST/(1+a))}{Sa},\\
q_n=\frac{K^2+EP^2}{2}+KP_t+Tf_c+(1+K)P_tg_c,\\
q_i(L,Q)=\frac1N\sum_n q_n c_{ni}.
\end{gathered}
$$

`root_matrix` 则对同一组实际角向rows形成

$$
a_m=L_v+w^2P_t,\qquad d_m=\frac{u(a+(1+a)^{-1})}{Da},\qquad
b_n=a_m+(1+a_m)d_m,
$$

再使用独立gram表 $g_{nk}$ 定义 $\beta_k=N^{-1}\sum_n b_n g_{nk}$，并对 $i\geq j$ 使用

$$
C_{ij}=\mathbf1_{i=j}+
\begin{cases}
\beta_0,&i=j=0,\\
\sqrt2_{\mathrm{lit}}\,\beta_i,&j=0<i,\\
\beta_{i-j}+\beta_{i+j},&j>0,
\end{cases}
\qquad C_{ji}=C_{ij}.
$$

这些定义直接对应所付源码，不需要把gram系数改成cosine字面表的乘积。

## R283.3 固定分支与定理条件

考虑一条成功返回的有限root执行分支 $\tau$。它指定：

1. 初值 $e_0=0$；实际接受的Newton更新数 $n$；
2. 每个更新所选的回溯指数 $k_i\in\{0,\ldots,19\}$，故 $\alpha_i=2^{-k_i}$；
3. 正常停止或原roundoff-fallback的返回位置；
4. 每个已执行的域检查及比较的结果，包括被拒绝trial的结果。

原源码的成功返回发生在30次外循环之一；因最后一次更新后若仍未返回便会触发iteration-limit，所以成功分支的 $0\leq n\leq29$。耗尽、域异常未被原逻辑恢复、无fallback的line-search失败或时间预算异常，不是本定理中的成功返回分支。

令 $U$ 为shape输入的一个开集，使得沿 $\tau$ 所需的实表达式均有定义，所有用于线性解的Cholesky枢轴为正。若还要求描述未强制分支的原实算术程序，则额外假定该程序在 $U$ 上选择的分支确为 $\tau$。所有相关比较具有严格余量，是保证此附加条件的一种充分方式；本文不声称实际113已经提供这些余量。`max/abs`本身不需要可微，只需要其比较结果不改变返回分支。

若 $\tau$ 来自实际浮点记录，以上实算术分支一致性也不能自动推定：原浮点trace与原实算术程序在同一字面输入上可能因舍入选择不同分支。无此一致性证据时，下文仍可定义并微分强制采用 $\tau$ 的实表达式延拓，但应如实称为该固定trace的变分模型。

**定理。** 在以上定义域内，固定trace的有限返回值 $L_\tau(y)$ 及其所用角向rows是可微的，事实上由有限个光滑实原语组合而成。在每个方向 $v\in\mathbb R^{224}$ 上，其方向导数可由原有限迭代逐步传播，且无需假定最终隐式残差为零或 $C=F_e$。

## R283.4 单次线性解的恒等式及逐循环实现

在一个迭代点记 $r=F(e,y)$、$C=C(e,y)$。实算术中，原 `spd_solve` 的Cholesky及前后代回给出唯一解

$$
Cs=r.
$$

因此对于参数方向，精确恒等式为

$$
C\dot s=\dot r-\dot C\,s.
\tag{283.1}
$$

这里的“精确”限定为这个实线性解映射；它不是把已舍入的 $C,s$ 当作无误差逆。

也可直接微分源码循环。令原下三角factor为 $R$。对

$$
v_{ij}=C_{ij}-\sum_{k<j}R_{ik}R_{jk},
$$

有

$$
\dot v_{ij}=\dot C_{ij}-\sum_{k<j}(\dot R_{ik}R_{jk}+R_{ik}\dot R_{jk}).
$$

正对角和非对角分支分别给出

$$
\dot R_{ii}=\frac{\dot v_{ii}}{2R_{ii}},\qquad
\dot R_{ij}=\frac{\dot v_{ij}-R_{ij}\dot R_{jj}}{R_{jj}}\quad(i>j).
\tag{283.2}
$$

前代回 $Rz=r$ 的第 $i$ 行给出

$$
\dot z_i=\frac{\dot r_i-\sum_{k<i}(\dot R_{ik}z_k+R_{ik}\dot z_k)-z_i\dot R_{ii}}{R_{ii}}.
\tag{283.3}
$$

后代回 $R^Ts=z$ 相应给出

$$
\dot s_i=\frac{\dot z_i-\sum_{k>i}(\dot R_{ki}s_k+R_{ki}\dot s_k)-s_i\dot R_{ii}}{R_{ii}}.
\tag{283.4}
$$

**证明。** Cholesky每个表达式只用已完成的前序条目、加减乘除及正平方根；正枢轴假设使分母非零。逐条应用链式法则即得(283.2)，并由索引归纳得到factor的全部方向条目。前后代回同样按原三角顺序归纳，得到(283.3)–(283.4)。原实Cholesky和代回满足 $Cs=r$，直接微分得到(283.1)。唯一性保证两条实算术求导途径一致。证毕。

实际128实现可以选择按(283.2)–(283.4)传播全部因子化/代回算术，或利用已有factor数值求解(283.1)。二者作为浮点程序的舍入路径不同，不能声称逐字一致。后者尤其不能凭(283.1)就声称已经微分了实际有限Cholesky返回值。

精确地，若某个可微近似解映射返回 $\widetilde s$，令

$$
\ell=C\widetilde s-r,
$$

则代数恒等式是

$$
C\,D\widetilde s=Dr-(DC)\widetilde s+D\ell.
\tag{283.5}
$$

小的线性残差本身不界定 $D\ell$。逐原语AD同样仍是有舍入的变分计算；它可明确描述固定trace实表达式的数值线性化，但不把IEEE舍入映射本身宣称为光滑可微。

## R283.5 有限root迭代的归纳证明

沿固定trace定义

$$
\begin{aligned}
e_0(y)&=0,\\
r_i(y)&=F(e_i(y),y),\qquad C_i(y)=C(e_i(y),y),\\
s_i(y)&=C_i(y)^{-1}r_i(y),\\
e_{i+1}(y)&=e_i(y)-\alpha_i s_i(y),\\
L_\tau(y)&=t(y)+e_n(y).
\end{aligned}
$$

对方向 $v$，初值 $\dot e_0=0$。递推定义

$$
\begin{aligned}
\dot r_i&=F_e(e_i,y)\dot e_i+F_y(e_i,y)v,\\
\dot C_i&=C_e(e_i,y)[\dot e_i]+C_y(e_i,y)[v],\\
C_i\dot s_i&=\dot r_i-\dot C_i s_i,\\
\dot e_{i+1}&=\dot e_i-\alpha_i\dot s_i,\\
\dot L_\tau&=Dt(y)v+\dot e_n.
\end{aligned}
\tag{283.6}
$$

**证明。** 初值为常函数，结论成立。若 $e_i$ 可微，则R283.2中的有限角表达式在原严格域内可微；因此 $r_i,C_i$ 可微。R283.4给出线性解的可微性和方向式。$\alpha_i$在固定trace中是常数，故减法给出下一行。有限次归纳得到(283.6)及最终 $L_\tau$。返回角向rows是同一 $L_\tau,Q$ 的光滑有限表达式，故也可微。整个证明未使用 $r_n=0$，也未使用 $C_i=F_e$。证毕。

特别地，初次停止的 $n=0$ 分支满足 $L_\tau=t(y)$，导数就是 $Dt$。事后对这个返回值再解理想隐式导数方程，会一般地改变该有限分支的导数。

正常停止和fallback仅选择返回位置。固定trace中不需要对其范数比较求导；被拒绝trial也没有改变 $e_i$，因此无需对每个拒绝候选再传播一份输出J。若扰动改变选择或恰位于比较边界，(283.6)不能自动提升为跨分支的统一导数。

## R283.6 字面角表达式的实际JVP

对一次现场的方向，几何和三套角表固定。令 $\dot L=\dot t+\dot e$；$P,P_t,L_v,U$的方向按原有限求和直接计算。接下来有

$$
\dot K=\dot L_v-\dot P_t,\quad
\dot T=2(1+K)\dot K+2EP\dot P,\quad
\dot u=w^2\dot T,
$$

$$
\dot D=-\dot u,\qquad \dot S=-2w^2P\dot P,\qquad \dot a=\dot D/(2a).
$$

对 $f_c,g_c,q_n$ 使用R283.2中原乘除式的乘积/商法则，再按原cosine投影：

$$
\dot F_i=\dot e_i+N^{-1}\sum_n\dot q_n c_{ni}.
$$

分母在原域中非零；无需引入 $\dot u/u$ 等在分子为零时不合法的新表达式。

矩阵方向则从原 $d_m,a_m,b_n$ 出发，

$$
\dot b_n=(1+d_m)\dot a_m+(1+a_m)\dot d_m,\qquad
\dot\beta_k=N^{-1}\sum_n\dot b_n g_{nk},
$$

再按原lower-triangle分支装配 $\dot C$，单位阵部分的方向为零。$d_m$对其原有理表达式直接求导。这里没有用连续三角恒等式替换独立字面gram表，也没有把原Newton矩阵定义偷换为隐式root导数。

因此上述变分所需的是现有有限表达式的一阶方向传播，不要求先建立理想隐式根的存在性或对该理想根求二阶导。

## R283.7 从局部root到完整native残差

原split RHS是同一root返回值及角向rows的有限表达式，所以可把R283.6返回的方向继续通过原linear+nonlinear flux投影。原两条mean状态也保留；其是否依赖shape由原表达式决定，不能因shooting未知量仅224维就删掉226态RHS中的输出责任。

原RK4一步在固定实际step及几何样本上是四次这种RHS的有限组合。对每个真实primal子状态用对应的root trace，按原RK4链式法则传播，得到该分支下stage映射的方向作用；最后保原port-ratio归一化。

原stage残差方向为

$$
DF_n(x)v=D\Phi_n(x_{n+1})v_{n+1}-v_n.
$$

原cut和far方向分别是 $v_{Q,0}$（内部native校正中target固定）以及 $v_{\Pi,D}-G_Dv_{Q,D}$。所有576段、cut、far共129248行和原scales都保留。若对外部物理height输入求敏感度，cut目标的相应方向必须另按同一明确的target形成规则加入。

这仍是固定有限分支实表达式的变分及其数值实现框架，不是完整128实际J已计算的声明，不证明原BVP存在，也不支付cut物理二阶jet、最终DN敏感度或audit的其它消费者。那些缺口已在独立post128接口中列明。

## R283.8 最小源码接口与费用责任

可以把未来独立实现限制为以下责任，而不先重写完整求解器：

1. 原primal `root` 可选输出当前现场的trace：实际 $e_i$、角向rows、迭代矩阵/factor/step、已选回溯指数及返回原因。保持原primal语句与分支权威。
2. `root_trace_jvp` 明示采用“逐factor/代回循环数值变分”还是“精确实线性solve恒等式的数值近似”；不能共用一个exact标签。
3. `rhs_jvp` 和 `rk4_jvp` 只消费同一primal现场与同一固定几何/步表，不重新求另一个root替换基点。
4. trace在当前RHS或RK步消费后释放，只保紧凑分支/身份记录；不新增raw归档或新的数学门。

对一次实际接受 $I$ 个Newton更新的root，记方向数为 $q$。每方向角向求和与矩阵矩方向形成需 $O(NM)$ 工作；利用原factor执行(283.1)的方向乘积与代回为 $O(J^2)$。逐factor循环传播方向则还需每方向 $O(J^3)$。这些是量级，不是实际运行时间或误差承诺。224列全付不能用一个JVP的成本冒称已经完成；原拒绝trial的方向传播在固定trace中可以省去。

任何实际采用均须诚实报告语义、真实root/线性残差、执行分支和完整非线性结果。当前仅完成此条件代数证明与源码接口设计；113原配置、原门与正在执行的实验均未改变。
