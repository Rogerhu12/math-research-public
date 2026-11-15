# 113有限root迭代的逐步变分：当前源码可实现的最小接口

AI 协作记录：ChatGPT，2026-11-15 UTC。

完整条件代数证明见 [R283](../results/R283-finite-root-trace-differentiation-with-literal-tables.md)；本文保留具体源码接口与费用说明。

本稿只读 `geometry_20261115_native_primal128.cpp`（SHA256 `1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d`）及其packet语义，聚焦 `root_evaluate`、`root_matrix`、`spd_solve`、`root`、`rhs`、`rk4`。没有修改113、执行数值、构造fixture或新请求；113修复版仍等待实际输出。

## 1. 先定义要线性化的有限程序

对一次原RHS现场固定所有几何及表字面系数。令 $y=(Q,\Pi)$ 为224个shape输入，$t(y)$ 为113维momentum目标，$e$ 为113维root未知量。当前代码使用两个必须区分的映射：

$$
F(e,y)=e+\operatorname{quad}(t(y)+e,Q),\qquad C(e,y)=\texttt{root\_matrix}(\texttt{root\_evaluate}(e,y)).
$$

$C$是**实际Newton迭代所用的矩阵**。它经过独立 `gram` 角表和原乘积矩装配；不能在冻结字面系数语义下直接把它命名为 $F_e$。本设计既不改变这个矩阵，也不要求它先等于理想root Jacobian。

在一个实际完成的固定执行分支内，root程序从 $e_0=0$ 开始，依次执行

$$
s_i=\operatorname{SPDsolve}(C_i,F_i),\qquad e_{i+1}=e_i-\alpha_i s_i,
$$

其中 $\alpha_i=2^{-k_i}$ 是原20档中真正被选中的值；最终返回 $L=t(y)+e_n$。正常停止和roundoff fallback都返回最后实际迭代点，而不是理想方程的精确根。30步耗尽、20档全拒且不满足fallback、原域错误及预算错误没有合法root输出，不能由变分包装替它们生成成功root。

这里的可证明导数首先指固定执行分支、固定字面系数下的实算术程序延拓。binary128执行及其AD仍有舍入；不把不连续的IEEE舍入函数声称为通常光滑函数，也不把AD数值称为无误差精确Jacobian。

## 2. 每次迭代真正需要传播什么

给定shape方向 $v$，初值为 $\dot e_0=0$，而 $\dot t$ 来自原 `fac*Pi`。每个已执行迭代需要

$$
\dot F_i=D_eF\,\dot e_i+D_yF\,v,\qquad
\dot C_i=D_eC\,\dot e_i+D_yC\,v.
$$

若 `SPDsolve` 指实算术中准确求解 $C_i s_i=F_i$，则直接微分给出

$$
C_i\dot s_i=\dot F_i-\dot C_i s_i,
\qquad
\dot e_{i+1}=\dot e_i-\alpha_i\dot s_i,
\qquad
\dot L=\dot t+\dot e_n.
$$

这些式子通过逐步链式法则归纳，给出**有限次迭代输出**的导数，不需要 $F(e_n,y)=0$，也不把未收敛root误当精确隐式根。$C_i$可以与 $F_e$ 不同；只要实际分支中的线性解存在，公式仍成立。

但若直接拿已舍入的 $s_i$ 和128线性解套这条恒等式，它只是相应线性解的数值变分模型。记实际线性解残差为 $\ell_i=C_i s_i-F_i$，对实际所定义的可微返回映射恒有

$$
C_i\dot s_i=\dot F_i-\dot C_i s_i+\dot\ell_i.
$$

因此不能把省略 $\dot\ell_i$ 的高效版本冒成字面128 Cholesky程序的exact导数。若要更贴近原有限算术路径，可对现有 `spd_solve` 三层循环逐原语传播，见第4节。两种实现须用不同 `derivative_semantics` 元数据描述。

## 3. 原角向表达式的方向作用，不借连续恒等式

所有 $r,r_x,w,w^2,E,\sqrt2,\sqrt{12}$、frequency、cosine、sine、gram 都作为各自原字面系数保留，本段对它们取零方向。不是令某些系数由另一些重新推导。

原代码的每个角度先形成 $P,P_t,L_v,U$，方向直接用同一有限求和：将momentum和 $L=t+e$ 替为其方向，原cosine/sine常量不动。接下来逐式取导：

$$
\begin{aligned}
K&=L_v-P_t,& \dot K&=\dot L_v-\dot P_t,\\
T&=2K+K^2+EP^2,& \dot T&=2(1+K)\dot K+2EP\dot P,\\
u&=w^2T,& \dot u&=w^2\dot T,\\
D&=1-u,& \dot D&=-\dot u,\\
S&=1-w^2P^2,& \dot S&=-2w^2P\dot P,\\
a&=\sqrt D,& \dot a&=\dot D/(2a).
\end{aligned}
$$

为避免在 $u=0$ 或某个分子为零时引入没有必要的除法，可用原有乘除顺序的方向商法。例如

$$
f_c=\frac{u(2+a)}{2a(1+a)^2}
$$

直接对分子、分母求方向，再用 $(\dot n-f_c\dot d)/d$，不先求 $\dot u/u$。$g_c=w^2(P^2+ST/(1+a))/(Sa)$ 同理。随后对原

$$
q=\tfrac12(K^2+EP^2)+KP_t+Tf_c+(1+K)P_tg_c
$$

逐乘积求导，并以原cosine字面表投影：

$$
\dot F_j=\dot e_j+\frac1N\sum_n \dot q_n\,c_{nj}.
$$

`root_matrix` 则独立使用源码中的

$$
a_m=L_v+w^2P_t,\quad
 d_m=\frac{u(a+(1+a)^{-1})}{Da},\quad
 b=a_m+(1+a_m)d_m.
$$

其方向为 $\dot b=(1+d_m)\dot a_m+(1+a_m)\dot d_m$；$\dot d_m$仍对该原有理式求导，不改写成另一个依赖理想恒等式的表达式。用原 `gram` 字面表得到 $\dot b_k$ 后，按 `root_matrix` 的同一 `j==0`/其它分支装配 $\dot C$，常数单位阵的方向为零。这样没有假定cosine与gram两套既有浮点表精确满足实三角乘积关系。

原域比较仍只由primal的 $D,S,A$ 决定。方向传播不修改它们、不以方向值放行一次原本失败的trial。

## 4. `spd_solve` 的具体逐步变分

当前函数先做Cholesky $C=RR^T$，再前后代回。对其实际执行的下三角循环，若

$$
v_{ij}=C_{ij}-\sum_{k<j}R_{ik}R_{jk},
$$

则

$$
\dot v_{ij}=\dot C_{ij}-\sum_{k<j}(\dot R_{ik}R_{jk}+R_{ik}\dot R_{jk}).
$$

对角支用 $\dot R_{ii}=\dot v_{ii}/(2R_{ii})$；非对角支用

$$
\dot R_{ij}=\frac{\dot v_{ij}-R_{ij}\dot R_{jj}}{R_{jj}}.
$$

若前代回 $Rz=F$，则逐行

$$
\dot z_i=\frac{\dot F_i-\sum_{k<i}(\dot R_{ik}z_k+R_{ik}\dot z_k)-z_i\dot R_{ii}}{R_{ii}}.
$$

后代回 $R^Ts=z$ 同理传播，保原顺序和实际factor。它不需要理想隐式root或对 $F$ 再求二阶导；需要的是**实际迭代矩阵生成程序**的一阶方向导数。

这些是相应实算术循环的链式法则恒等式。将其在记录的128值上执行仍是有舍入的变分计算。若用原factor求解 $\dot F-\dot C s$ 以降低成本，应明确采用线性求解映射近似，而不是说已逐原语微分了有限Cholesky返回值。

## 5. 分支、停止和不需要传播的 rejected trial

固定分支的导数无需对 `max/abs` 范数或布尔比较求导。它们负责选择实际迭代次数、是否fallback、被选中的回溯指数。被拒绝trial在该固定分支上不改变返回状态，可以仅保其primal判断记录，无需为每个被拒绝点都求一份J。

但这不是无条件可微性结论。若停止或trial比较恰落边界，或扰动导致另一条回溯/域分支，固定分支J只描述原分支，不自动描述邻域。预算中断同样是无完整返回值，不能被当作一条可求导的成功root。初次 `e=0` 就返回也必须原样保留：该分支返回 $L=t(y)$，故导数是 $\dot t$，不是事后补上理想隐式根响应。

建议只记录已发生的 `iteration_count`、`accepted_backtrack_indices`、`return_reason`、原residual/scale和停止比较值，以及分支顺序的hash。它们是解释实际算术的责任记录，不新增候选或最终接受阈值。

## 6. 最小源码接口与作用范围

未来独立实现可以在保持原primal语句的前提下增加可选trace：

- `root(..., RootTrace*)`：保实际 $e_i$、原返回root、每次矩阵/factor/step与被选中的alpha；只需当前RHS现场的临时数据。
- `root_trace_jvp(trace, state_direction)`：选定并明示第2节求解映射版或第4节逐循环版；返回 $\dot L$、最后角向rows的方向与语义记录。
- `rhs_jvp`：对当前split flux的原因子和原投影求方向，使用同一 $\dot L$；两条mean输出也保留，其中背景mean项对shape输入的方向为零。
- `rk4_jvp`：沿原四次真实RHS状态及同一step几何、cusp次序组合方向。输出stage224行前保226态；端口仍按原ratio除法。

这样逐stage提供匹配所选变分语义的完整作用，外层cut、576段stage、far及原scales都保留。初始可做一个完整方向作用，而不先物化全部129248平方矩阵；是否进一步形成全部stage块，等待113实际费用和残差证据。

## 7. 开销的具体来源

设一次root实际接受 $I$ 个Newton更新、角数 $N$、模数 $M$、$J=M+1$，一次传播 $q$ 个shape方向。

- 每方向角向field/quad与gram方向形成仍需 $O(NM)$ 工作，不能因为已有理想Fourier公式就把原字面表替换掉。
- 用原factor的线性求解映射版，每方向的 $\dot C s$ 和代回为 $O(J^2)$；primal factor的 $O(J^3)$ 只付原一次。该高效版的线性求解残差语义须保留。
- 逐Cholesky原语版直接传播factor方向，每方向还需 $O(J^3)$；224列全付会明显更贵，不能用一个JVP的成本声称已获得完整J。
- rejected-root trials无需额外方向传播。trace可以在一个RHS或一RK步消费后释放，不累积全576段、全部外层迭代的raw。
- 完整stage J仍可按列块或JVP逐付；root误差/有限分支语义与真实完整非线性回溯始终分开。

这些是算法量级，不是已测runtime、误差界或收敛保证。原113二配置、7200秒预算、原64控制均保持；本设计没有增加新的实施或调度。
