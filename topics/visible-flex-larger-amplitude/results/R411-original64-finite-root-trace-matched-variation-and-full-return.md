# R411：原 binary64 有限 root 分支的匹配切向与完整原生返回接口

AI 协作证明及源码设计：ChatGPT，2026-11-15 UTC。

## R411.1 这里解决的具体不一致

[R369](R369-actual172-current-H-complete-secant-and-trial-decomposition.md) 已分开保存的模型、状态形成、同点 noJ 偏差及真实 finite secant。末轮真实 secant 很大，而该次保存的同点偏差与状态形成项很小。这些原数值不证明唯一原因，也不提供逐个角向 root 的实际分支记录。

原 `78718-tail-fourier-root-momentum.mjs`（SHA256 `cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88`）实际返回有限 Newton／回溯执行的结果。原 `78718-tail-fourier-product-jacobian.mjs`（`205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25`）在该返回点另解最终 Gram 的隐式方向公式。它没有传播实际接受的有限更新及其停止位置。

这两个对象一般不同。尤其原 root 第零次检查直接停止时，返回的根变量就是初始 target；该固定分支的导数由 target 直接决定，不能事后由一个非零隐式校正替代。这是源码可以确定的条件机制，不是对 R369 当前最坏行的根因判定。

本结果把已发表 [R283](R283-finite-root-trace-differentiation-with-literal-tables.md) 的逐执行分支原则明确用于此原 binary64 路径。它不重复建立无限尾或原物理 BVP 的存在性。

## R411.2 精确规定的有限对象

令 $M=112$，$J=M+1=113$，$K=2M=224$，完整 RHS 状态维数为 $K+2=226$。原三套字面角表分别为：

- $c_{ni}$：原 root 的正交 cosine 表，共 $113$ 列；
- $s_{nj}$：原 root 的 sine 表，共 $112$ 列；
- $g_{nk}$：原 Gram cosine 表，共 $225$ 列。

它们分别作为原实际表中浮点字词代表的实常数。不得用连续三角乘积恒等式把一套表替换成另一套表。原 $w,w^2,E,\sqrt2,\sqrt{12}$ 同样分别固定；不额外要求各字面常数满足无限精度恒等式。

固定一次现场的 geometry、cell normalization、profile 位置和原 RK 步长。对 shape 输入 $y=(Q,\Pi)$，原 root 的目标为

$$
t_0=0,\qquad t_{j+1}=\gamma\Pi_j,\qquad
\gamma=\frac{\mathrm{orientation}\sqrt{12}_{\rm lit}\,\mu}
{\sqrt2_{\rm lit}\,r^4w^2}.
$$

原 angular expressions 是

$$
\begin{aligned}
P_n&=\sum_j\frac{-m_jr^3Q_j}{\sqrt2_{\rm lit}w}s_{nj},\
(P_t)_n&=\sum_j\frac{-m_j^2r^3Q_j}{\sqrt2_{\rm lit}w}c_{n,j+1},\
(L_v)_n&=L_0+\sum_jL_{j+1}c_{n,j+1},\
U_n&=\sum_j\left[-m_jL_{j+1}+(m_j^2-1)
 \frac{-m_jr^3Q_j}{\sqrt2_{\rm lit}w}\right]s_{nj}.
\end{aligned}
$$

对每个角点令

$$
\begin{gathered}
K_n=(L_v)_n-(P_t)_n,\
T_n=2K_n+K_n^2+EP_n^2,\
u_n=w^2T_n,\quad D_n=1-u_n,\quad
S_n=1-w^2P_n^2,\quad A_n=1+(L_v)_n+w^2(P_t)_n,\
a_n=\sqrt{D_n},\qquad
f_n=\frac{u_n(2+a_n)}{2a_n(1+a_n)^2},\qquad
g_n=\frac{w^2(P_n^2+S_nT_n/(1+a_n))}{S_na_n},\
q_n=\tfrac12(K_n^2+EP_n^2)+K_n(P_t)_n+
T_nf_n+(1+K_n)(P_t)_ng_n.
\end{gathered}
$$

原实表达式残差与原 Newton 矩阵分别定义为

$$
F(L,y)=L+\frac1N c^Tq(L,Q)-t(y),
$$

以及原 `evaluateL` 中的矩阵 $C(L,y)$。矩阵的 scalar weight 必须沿原程序的表达式：

$$
a_{m,n}=(L_v)_n+w^2(P_t)_n,\qquad
b_n=a_{m,n}+(1+a_{m,n})
 \operatorname{expm1}\!\left(-\tfrac32\log1p(-u_n)\right).
$$

令 $\beta_k=N^{-1}\sum_n b_ng_{nk}$。对 $i\geq j$，

$$
C_{ij}=\mathbf1_{i=j}+
\begin{cases}
\beta_0,&i=j=0,\\
\sqrt2_{\rm lit}\beta_i,&j=0<i,\\
\beta_{i-j}+\beta_{i+j},&j>0,
\end{cases}
\qquad C_{ji}=C_{ij}.
$$

这里 $C$ 的定义是原源码的 Gram 组装，不能改称 $F_L$。与 R283 的 $e=L-t$ 坐标在准确实数中可以互换；新实现仍保留原 binary64 程序的 $L$、`(L+quad)-target` 及所有原数值语句，不先把原 primal 改写成另一种求根方法。

## R411.3 条件命题：固定成功分支

一条原成功 root trace 指定：

1. 原初值 $L_0=t(y)$；本入口没有外供 root guess；
2. $n$ 次实际接受的更新，$0\leq n\leq29$；
3. 每次更新的原回溯指数 $k_i\in\{0,\ldots,19\}$，$\alpha_i=2^{-k_i}$；
4. 原 normal stop 或原 roundoff fallback 返回位置；
5. 已执行的原域检查、比较及被拒绝候选的结果。

这里的 $n\leq29$ 同时适用于两种成功返回：原 `for(it=0;it<30;it++)` 在本轮更新前检查 normal stop；fallback 只在本轮没有接受更新的 `!accepted` 分支内返回。循环外没有 fallback，只有 iteration-limit 抛错。因此 `it=29` 若再接受第 $30$ 次更新，随后只能抛错，不能作为成功返回。观察器在原 `L=trial` 之前记录每次实际接受更新，故这条失败 trace 的第 $30$ 次仍会保留；成功返回统计的 $30$ 个槽恰为 $0,\ldots,29$。

考虑强制采用这条 trace 的实表达式延拓。在某个开集上，假设所需的原分母非零、正平方根有定义、Cholesky 枢轴严格为正。则有限返回值 $L_\tau(y)$ 是光滑函数。它的方向导数可由全部实际接受的更新逐步传播，无需假定最终残差为零，也无需假定 $C=F_L$。

若要把这个结论识别为未强制分支的原实数程序在邻域内的导数，还须该程序在此邻域选择同一条 trace。实际浮点比较产生的 trace 不自动支付这一条件。跨停止边界、回溯切换及 fallback 边界的统一误差界也没有由本命题推出。

**证明。** 初值 $t$ 为线性映射。每次接受的更新依次执行 $F$、$C$、正 Cholesky、两次三角代回和固定 $\alpha_i$ 的仿射更新。它们在上述定义域内均由有限个光滑实原语复合而成。有限归纳即得光滑性。原比较只决定采用哪条分支；固定分支中不对比较自身求导。被拒绝候选不更新 $L$，故不需要为最终输出再传播其切向。证毕。

## R411.4 完整逐循环切向

对方向 $v\in\mathbb R^{224}$，初值为 $\dot L_0=Dt(y)v$。在第 $i$ 个原接受更新中，

$$
\begin{aligned}
r_i&=F(L_i,y),&C_i&=C(L_i,y),\\
R_iR_i^T&=C_i,&R_i z_i&=r_i,&R_i^T s_i&=z_i,\\
L_{i+1}&=L_i-\alpha_i s_i.
\end{aligned}
$$

用原三套字面表对完整有限角向表达式求导，得到 $\dot r_i$ 和 $\dot C_i$。为避免偷换实际数值因子化，本实现选择显式逐因子、逐代回传播。对原 lower factor $R$：

$$
\dot v_{ij}=\dot C_{ij}-\sum_{k<j}
(\dot R_{ik}R_{jk}+R_{ik}\dot R_{jk}),
$$

$$
\dot R_{ii}=\frac{\dot v_{ii}}{2R_{ii}},\qquad
\dot R_{ij}=\frac{\dot v_{ij}-R_{ij}\dot R_{jj}}{R_{jj}}
\quad(i>j).
$$

两次代回为

$$
\dot z_i=
\frac{\dot r_i-\sum_{j<i}(\dot R_{ij}z_j+R_{ij}\dot z_j)-z_i\dot R_{ii}}
{R_{ii}},
$$

$$
\dot s_i=
\frac{\dot z_i-\sum_{j>i}(\dot R_{ji}s_j+R_{ji}\dot s_j)-s_i\dot R_{ii}}
{R_{ii}}.
$$

最后

$$
\dot L_{i+1}=\dot L_i-\alpha_i\dot s_i.
$$

这些式子直接来自原实循环的乘积、商和平方根法则。实际数值实现使用当前 trace 保存的原 $R,z,s$，不事后换成另一次 factorization，不把 $C^{-1}(\dot r-\dot C s)$ 无条件称为已微分的有限字词代回。

**数值范围。** 上式仍以浮点运算实现，故是固定 trace 实表达式的数值线性化。它既不是 IEEE 舍入映射的经典导数，也不自行提供变分舍入误差界。沿用原因子和代回值不会自动支付这些误差界。R305 中近似解缺陷及其导数的区别仍须保留。

零更新成功分支特别满足

$$
L_\tau=t(y),\qquad DL_\tau=Dt.
$$

这给出一个直接可检验的源码语义区别；当前 172 未保存逐根分支，所以本结果不据此填造它有多少次零更新或哪次导致其最坏 secant。

## R411.5 从 root 到原完整 226 态与 576 段

原 split RHS 的 nonlinear factor 是

$$
h_n=\frac{K_n+u_n/(1+a_n)+w^2P_n^2a_n}{S_na_n}.
$$

保留原精确投影的 linear flux 和全部有限 nonlinear flux：

$$
\begin{aligned}
Q_{j,x}
 &=\frac{r_x}{r}\left[(m_j^2-4)Q_j+
   \frac{\sqrt2_{\rm lit}w}{r^3}L_{j+1}\right],\\
\Pi_{j,x}
 &=4\frac{r_x}{r}\Pi_j+
 \frac{\mathrm{orientation}\sqrt2_{\rm lit}r^3r_xw^2}
 {\sqrt{12}_{\rm lit}\mu}m_j
 \left[-m_jL_{j+1}+(m_j^2-1)P_j^{\rm coeff}
       +\frac1N\sum_nU_nh_ns_{nj}\right].
\end{aligned}
$$

两条 mean 输出仍为 $r_xwL_0$ 和 $r_xw$。前者的全部 shape 导数保留，后者的 shape 导数为零，但这个完整输出行不被删除。

新的 withJ 使用原 noJ 的实际 RK 算术顺序：普通位置 $k/\mathrm{steps}$、原局部 cusp split、未切分时保原 $h$、`h*a/2` 的乘除顺序，以及原重复使用的中间 state buffer。每个 RK 步先完成四个原 primal field，再从其已捕获 tape 求全部 $224$ 列，避免方向阶段再次求另一个 root 或 profile 作为基点。

这里的“保 primal”指保原 **noJ** 映射。原产品型 withJ 使用的 grid／增量舍入顺序与 noJ 不完全相同，因此本修订没有宣称新 withJ 的 primal 在所有输入上逐字等于旧 withJ。新的目的正是使 fresh-J 基点和原接受试步使用同一 noJ 计算路径。

完整 stage 残差方向为

$$
D\Phi_n(X_{n+1})V_{n+1}-V_n.
$$

所有 $576$ 段、$577$ 节点、cut $112$ 行、far $112$ 行及原 $129248$ 行顺序与 scales 保留。原 port ratio 继续作用于 Pi 输出及对应全部 Jacobian 行，不反转入端 $n+1$ 和出端 $n$。

## R411.6 原 112 高度与 338 行物理返回

此实现通过同一原 engine 的两个入口提供方向：局部 `rhsWithJacobian` 和完整 `flowStateWithJacobian`。所以现有原调用链可以继续承担：

- 当前完整 $H\in\mathbb R^{112}$ 到原 shooting solve；
- 原 fresh stage J、R273 的全部 cut/stage/far 校正及原十档 noJ 严格残差回溯；
- 原 tangent graph 与当前 H 的原有限差分检查；
- `numerical-tail-slope-jacobian.mjs` 的完整 slope、mean-slope 方向；
- 原 source 对 second、mean-second 和 height 行的对称差分；
- 最终同一完整场的 fresh J、full DN 与原物理 audit。

$338=112+112+1+1+112$ 的行数及 $112$ 高度列不变。一阶行采用新 finite-trace 数值切向；二阶行仍是原方法，不能因更换一阶切向就称完整 $338$ 行已成为解析或严格认证的 Jacobian。

原 audit 的物理 jet 定义不因本实现改成另一个量。它仍必须真正执行并返回原数据；未执行、失败或资源停止不靠新引擎名称补成已通过。末场不存在时，绝不能把历史旧 J 或 audit 粘贴到当前状态。

## R411.7 为什么不能直接复名使用 f9b

已存在 `geometry_20261114_noj_matched_variational_engine.mjs`，SHA256 为 `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9`。它已支付 noJ RK 的词法顺序匹配及原 root/RHS 捕获，但其 `fromCaptured` 仍调用原 `createFourierProductJacobianEngine`。因此它没有微分实际有限 root 更新。

新 flow 可以保留其 RK 正文，但必须独立替换局部方向内核、绑定实际 root tape 和所有字面表，并给新的 source/schema。把 f9b 改标签而不改该调用，不解决本节开头的差异。

## R411.8 执行与剩余责任

原 root 的 $30\times20$、停止 $8\cdot10^{-14}$、fallback $5\cdot10^{-12}$；原 native 的 $32\times10$、$2\cdot10^{-9}$、完整 D/S/A、strict norm descent；原 H/J/FD/full DN/final audit 规则均不因本切向增加或削减接受门。

观测 tape 只读实际原值，不改变其原数值表达式。内存、资源异常以及新方向非有限或内部绑定不一致须作为独立实现／资源失败记录，不冒原 D/S/A 数学拒绝。原 trace 在当前 RK 步消费后释放，仅必要分支计数、source、结果身份和实际错误进入读回。

对每次实际 root 的 $I$ 个接受更新及 $224$ 个方向，逐因子传播确有 $O(IJ^3\cdot224)$ 成本，此外还有全部有限角投影及 RK 矩阵作用。不能用一次方向的费用冒完整 J，也不能以源码可运行承诺原 $32$ 次 native 循环在一个 job 内全部付完。原绝对墙钟总预算必须从完整科学入口开始，保已完成／未开始范围及原末响应。

当前 195 是独立新实现；既有 172、186、190、192 等冻结源与正在执行的现场均未更改。本证明不预填 195 的运行号、结果、收敛或原生成功。它提供的是明确的有限分支对象、全部原返回责任和可实现的匹配切向，不是新前置验收门。
