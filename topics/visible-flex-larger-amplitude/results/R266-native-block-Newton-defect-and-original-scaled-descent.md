# R266 — 原 native 块 Newton 缺陷、原尺度下降与可逆缩放

日期：2026-11-14。状态：完整条件代数证明；原源码符号和归一化已核。不含新的数值计算，不声称实际25已经满足任何下降充分条件，不新增求解或课题完成门。

## 266.1 范围与原源码身份

本结果研究原完整 finite-mode、finite-depth native multiple-shooting 系统的一次校正。所有 modes、stages、cut 输入、far Robin 图和原残差尺度保持。它不把初猜器的私有 Riccati 图替换到原问题，也不把一个高条件数直接判作线性校正错误。

核对源码为 [78718-tail-tangent-core.mjs](../../visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs)，SHA256：

    ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3

相关实际入口是 scaleFor、evaluate、correction、solve。[tail_resumable_engine.mjs](../computations/tail_resumable_engine.mjs) 的原共享图插入和 accepted-trial 记录不改变这些残差、校正与 line-search 方程；其 SHA256 为：

    1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8

原程序在每次迭代以 withJac=true 得到基点残差和完整 stage Jacobian，用 correction 得到全部节点的校正，再对十个步长 $1,2^{-1},\ldots,2^{-9}$ 调用原 evaluate(...,false,scales)。只在原返回的归一化最大残差严格下降时接受。本文不修改这个规则，也不保证其中某个有限步长必定成功。

## 266.2 完整有限数组的精确代数模型

设 $M$ 为原模式数，$N$ 为原 stage 数，$K=2M$。第 $n$ 个完整节点记为

$$
y_n=(q_n,p_n)\in\mathbb R^{2M},\qquad 0\le n\le N.
$$

输入 $t\in\mathbb R^M$ 是原 cut target；远端图 $G_\infty$ 是原实际保存的对角矩阵。实际保存的每个有限 binary64 数在本节中均解释为对应的精确实数；不重新求 ODE、不重算 far 图、不从短格式化十进制替代实际位模式。

令 $\widehat r_n\in\mathbb R^{2M}$ 为原已计算的 stage 残差，$\widehat r_c\in\mathbb R^M$ 为原 cut 相减所得残差，$\widehat r_f\in\mathbb R^M$ 为原 far 相乘/相减所得残差。源码中的方向是

$$
r_n=F_n(y_{n+1})-y_n,\qquad
r_c=q_0-t,\qquad
r_f=p_N-G_\infty q_N.
\tag{266.1}
$$

这里的 $F_n$ 在谈连续数学函数时才有精确函数含义；带帽的残差首先只是原实际返回的浮点数组。特别是 $\widehat r_n$ 不必逐位等于“将实际 flow.out 先解释成实数再减实际 $y_n$”的精确差，因为原减法本身已经舍入。

把 stage、cut、far 行按固定顺序堆叠为 $\widehat r$，总行数为

$$
2MN+M+M=2M(N+1).
$$

令 $J_n$ 为原已保存的完整 $2M\times2M$ stage Jacobian。它定义一个精确实线性算子 $A$：

$$
(A\delta)_n=J_n\delta_{n+1}-\delta_n,
\tag{266.2}
$$

$$
(A\delta)_c=P_q\delta_0,\qquad
(A\delta)_f=P_p\delta_N-G_\infty P_q\delta_N.
\tag{266.3}
$$

$P_q,P_p$ 分别取前、后 $M$ 个分量。此处构造 $A$ 只使用已保存的 $J_n$ 和原边界，不声称这些 $J_n$ 就是任何连续数学 flow 的精确导数。

原实际尺度为

$$
\sigma_0=\operatorname{stored}\!\left(\max(10^{-250},\|t\|_\infty)\right),\qquad
\sigma_{n+1}=\operatorname{stored}\!
 \left(\sigma_n/|\mathrm{gains}_{n,0}|\right).
\tag{266.4}
$$

小数字面量和各次除法均按原实际位模式固定，gains 是原 native 的 gains。以下假设实际 $\sigma_n$ 有限且严格正，以便它们定义一个范数；若实际尺度为零或非有限，不能套用该范数命题。这是命题的数学适用条件，不是给原 solver 添加一个新门。

定义固定权矩阵 $W$：stage $n$ 的全部 $2M$ 行乘 $1/\sigma_n$，cut 全部 $M$ 行乘 $1/\sigma_0$，far 全部 $M$ 行乘 $1/\sigma_N$。于是

$$
\|v\|_{\sigma,\infty}:=\|Wv\|_\infty
=\max\left\{
 \max_{n,j}\frac{|v_{n,j}|}{\sigma_n},
 \max_j\frac{|v_{c,j}|}{\sigma_0},
 \max_j\frac{|v_{f,j}|}{\sigma_N}\right\}.
\tag{266.5}
$$

这正是原 evaluate 所使用的分量和尺度；式 (266.5) 是其精确实数解释。原 JavaScript 计算商和最大值后返回的有限数仍可能有舍入差，266.5 节明确处理这一区别。每次 solve 的 target 固定，因此 line search 沿用同一组原 $\sigma$，不随 trial 重新定义一个较容易的范数。

## 266.3 实际校正的完整线性缺陷

**定理266.1（不精确校正的精确恒等式）。** 对任意完整有限校正数组 $\delta$，不论它由 Riccati、带状消元、QR 或其他途径得到，定义

$$
e:=A\delta+\widehat r.
\tag{266.6}
$$

则该实际有限数组模型在任意实步长 $\lambda$ 的预测残差为

$$
m_\lambda:=\widehat r+\lambda A\delta
=(1-\lambda)\widehat r+\lambda e.
\tag{266.7}
$$

这里 $e$ 必须包含全部 stage、cut 和 far 行，分别为

$$
e_n=J_n\delta_{n+1}-\delta_n+\widehat r_n,
$$

$$
e_c=P_q\delta_0+\widehat r_c,\qquad
e_f=P_p\delta_N-G_\infty P_q\delta_N+\widehat r_f.
\tag{266.8}
$$

**证明。** 将 (266.6) 中 $A\delta=e-\widehat r$ 代入定义即得 (266.7)；(266.8) 是按 (266.2)–(266.3) 展开。没有可逆性假设，也没有用到 $J_n$ 是精确导数。证毕。

**推论266.2（原范数下的充分线性下降）。** 令

$$
\rho=\|\widehat r\|_{\sigma,\infty}>0,\qquad
\epsilon=\|e\|_{\sigma,\infty}.
$$

若 $\epsilon\le\eta\rho$，其中 $0\le\eta<1$，则对每个 $0<\lambda\le1$，

$$
\|m_\lambda\|_{\sigma,\infty}
\le[1-\lambda(1-\eta)]\rho<\rho.
\tag{266.9}
$$

**证明。** 对 (266.7) 使用三角不等式，且 $1-\lambda,\lambda$ 非负。证毕。

这个条件仅是充分条件。若 $\epsilon\ge\rho$，不能反推每个 $m_\lambda$ 都不下降，因为不同残差分量及符号可能抵消。可以直接计算更精确的模型下降量

$$
g_\lambda:=\rho-\|m_\lambda\|_{\sigma,\infty}.
\tag{266.10}
$$

若 $g_\lambda>0$，它是该步长在实际有限数组模型内的真实代数余量；仍不是原非线性 trial 已经下降。

### 浮点“缺陷报告”的身份

若一个工具用浮点点积得到 $\widehat e$，它首先是对 (266.6) 的一次数值求值，不是自动精确的 $e$。令

$$
\xi_{\rm lin}:=\widehat e-e.
$$

如果已独立控制 $\|\xi_{\rm lin}\|_{\sigma,\infty}\le b_{\rm lin}$，才有

$$
\epsilon\le\|\widehat e\|_{\sigma,\infty}+b_{\rm lin}.
\tag{266.11}
$$

也可以将已保存的 binary64 分量解码为精确有理数，直接求同一有限数组模型的 (266.8)。未给舍入界的普通浮点结果可以诚实报告为诊断，不能把“多用了一种浮点算法”当作严格上界。该区别包括严重抵消、subnormal 和重新舍入到零的项；参见 R264 的位模式约定。

## 266.4 与连续数学 flow 的差别必须单列

本节及以下下降判据只考虑原回溯范围 $0<\lambda\le1$。

为分析真实 nonlinear trial，另指定一个连续比较残差映射 $R:\mathcal U\to\mathbb R^{2M(N+1)}$，其 stage、cut、far 形式为 (266.1)，其中原 target 和实际 far 图固定。假设 $R$ 在所考察路径上可微。$\mathcal U$ 必须位于所选物理/root 分支内，涉及的真实曲线和几何量均有定义。

$R$ 可以是明确指定的精确 ODE shooting map，或另有完整定义的实数离散 map。选择哪个对象，必须在实际误差账中说明。本文不对 literal IEEE 程序逐步映射假设光滑；浮点舍入、分支与 stopping decisions 的映射一般不能直接当作这里的 $R$。

设当前实际节点数组为 $Y$。把原 trial 的乘法与加法结果记为

$$
\widehat Y_\lambda=Y+\lambda\delta+h_\lambda,
\tag{266.12}
$$

其中 $h_\lambda$ 是实际 trial 数组相对理想实数加法的差。原 $\lambda=2^{-k}$ 虽是精确可表示的数，乘法可能下溢，加法也仍会舍入；不能因此把 $h_\lambda$ 默认为零。

定义

$$
a_0:=R(Y)-\widehat r,\qquad
d:=(DR(Y)-A)\delta,
\tag{266.13}
$$

$$
q_\lambda:=R(Y+\lambda\delta)-R(Y)-\lambda DR(Y)\delta,
\tag{266.14}
$$

$$
v_\lambda:=R(\widehat Y_\lambda)-R(Y+\lambda\delta),\qquad
a_\lambda:=\widehat r_\lambda-R(\widehat Y_\lambda).
\tag{266.15}
$$

$\widehat r_\lambda$ 是原 no-J trial 实际返回的完整残差。$a_0,a_\lambda$ 包含实际 flow、root、RK 和残差形成与选定 $R$ 的差；它们不只表示最终一次加减的 roundoff。尤其基点 withJac=true 和 trial withJac=false 是源码中的不同调用路径，仅在某一基点恰有同一 norm，不足以证明它们在邻域中等于同一个精确函数。

$d$ 是实际校正方向上的导数误差。它不能因为数组名叫 J 或来自 variational engine 就自动设为零。若参考对象是精确 ODE flow，有限 RK/root/差分线性化误差仍须计入；若参考对象是某个精确离散 map，也须核原已算 tangent 确为该 map 的导数。

**定理266.3（完整 nonlinear trial 身份）。** 在上述各量有定义时，

$$
\boxed{
\widehat r_\lambda
=(1-\lambda)\widehat r+\lambda e
 +a_0+\lambda d+q_\lambda+v_\lambda+a_\lambda.}
\tag{266.16}
$$

**证明。** 从 $R(\widehat Y_\lambda)+a_\lambda$ 出发，先用 (266.15) 换成 $R(Y+\lambda\delta)+v_\lambda+a_\lambda$，再用 (266.14) 展开为 $R(Y)+\lambda DR(Y)\delta+q_\lambda+v_\lambda+a_\lambda$。代入 (266.13)，最后使用 (266.7)，即得结论。证毕。

cut、far 对 $Y$ 为仿射，因此它们在参考 $R$ 中的 $q_\lambda$ 为零；参考边界使用同一个实际 far 图时，$d$ 的这两组行也为零。但它们的残差形成和 trial 节点舍入仍进入 $a_0,a_\lambda,v_\lambda$。只检查 stage 行不等价于检查完整系统。

节点舍入项也可具体控制：若从 $Y+\lambda\delta$ 到 $\widehat Y_\lambda$ 的线段留在同一参考域，且沿线段 $\|WDR\|_{X\to\infty}\le K_\lambda$，则积分公式给出 $\|v_\lambda\|_{\sigma,\infty}\le K_\lambda\|h_\lambda\|_X$。$h_\lambda$ 可由实际节点、实际校正、步长和 trial 节点的精确位模式恢复；不得未经域与导数界检查就把该上界视为已付。

## 266.5 回到原报告 norm 的充分条件

令

$$
E_\lambda:=
 \|a_0\|_{\sigma,\infty}
 +\lambda\|d\|_{\sigma,\infty}
 +\|q_\lambda\|_{\sigma,\infty}
 +\|v_\lambda\|_{\sigma,\infty}
 +\|a_\lambda\|_{\sigma,\infty}.
\tag{266.17}
$$

由 (266.16)，

$$
\|\widehat r_\lambda\|_{\sigma,\infty}
\le \|m_\lambda\|_{\sigma,\infty}+E_\lambda.
\tag{266.18}
$$

这里可以用对误差总和的更紧上界替代逐项三角界；逐项式的用途是把来源分开，不能宣称这些上界已由本证明计算出来。

原程序返回的基点、trial norm 分别记为 $\widehat\rho_0,\widehat\rho_\lambda$。若有对应的实际标量求值误差界

$$
|\widehat\rho_0-\rho|\le\nu_0,\qquad
|\widehat\rho_\lambda-\|\widehat r_\lambda\|_{\sigma,\infty}|
 \le\nu_\lambda,
\tag{266.19}
$$

这些标量误差也有直接身份。对某次已保存的残差向量，记每个原归一化商的实际返回值为 $z_i=\operatorname{stored}(|r_i|/\sigma_i)$。在这些商均有限时，原 max 精确选择其中一个值，故

$$
\left|\max_i z_i-\max_i\frac{|r_i|}{\sigma_i}\right|
\le\max_i\left|z_i-\frac{|r_i|}{\sigma_i}\right|.
$$

这是 max 对无穷范数的1-Lipschitz 性质，逐分量比较即可证明；右边可由实际位模式与精确有理商恢复。它不包含 stage 流误差，后者已在 (266.17) 单列。

以下条件足以保证源码所要求的实际严格比较：

$$
E_\lambda+\nu_0+\nu_\lambda<g_\lambda
\quad\Longrightarrow\quad
\widehat\rho_\lambda<\widehat\rho_0.
\tag{266.20}
$$

**证明。** 由 (266.18)–(266.19)，

$$
\widehat\rho_\lambda
\le\rho-g_\lambda+E_\lambda+\nu_\lambda
<\rho-\nu_0\le\widehat\rho_0.
$$

证毕。

更易用但可能更松的充分条件是

$$
\lambda\bigl(\rho-\epsilon-\|d\|_{\sigma,\infty}\bigr)
>
\|a_0\|_{\sigma,\infty}
+\|q_\lambda\|_{\sigma,\infty}
+\|v_\lambda\|_{\sigma,\infty}
+\|a_\lambda\|_{\sigma,\infty}
+\nu_0+\nu_\lambda.
\tag{266.21}
$$

其证明是先对 (266.7) 使用 (266.9) 的同一三角估计，再套 (266.20)。式 (266.21) 明确显示：小的线性缺陷、足够准确的方向导数和受控的 nonlinear/算术余项是不同问题。

原实际 trial 直接核 $\widehat\rho_\lambda<\widehat\rho_0$ 时，当然不需要额外先证明 (266.20)。本结果提供解释与充分条件，不把它加成运行原 solver 的新准入条件。

## 266.6 小步长存在性的准确适用条件

固定任意状态空间范数 $\|\cdot\|_X$。假设 $R$ 连续可微，理想路径 $Y+s\delta$ 在 $0\le s\le\lambda$ 内位于 $\mathcal U$。积分形式给出

$$
q_\lambda=\int_0^\lambda
 [DR(Y+s\delta)-DR(Y)]\delta\,ds.
\tag{266.22}
$$

因此

$$
\|q_\lambda\|_{\sigma,\infty}
\le \lambda\|\delta\|_X
 \sup_{0\le s\le\lambda}
 \|W[DR(Y+s\delta)-DR(Y)]\|_{X\to\infty}
=o(\lambda).
\tag{266.23}
$$

若还有导数 Lipschitz 常数 $L\ge0$，

$$
\|W[DR(Y+h)-DR(Y)]\|_{X\to\infty}\le L\|h\|_X,
$$

则

$$
\|q_\lambda\|_{\sigma,\infty}
\le \tfrac12 L\lambda^2\|\delta\|_X^2.
\tag{266.24}
$$

**推论266.4（理想模型内的局部下降）。** 假设 $a_0=a_\lambda=v_\lambda=0$，norm 无求值误差，且

$$
\gamma:=\rho-\epsilon-\|d\|_{\sigma,\infty}>0.
$$

那么在保持参考函数有定义的充分小正步长上，残差严格下降。如果有 (266.24)，任何同时满足域要求、$0<\lambda\le1$ 和

$$
\tfrac12 L\lambda\|\delta\|_X^2<\gamma
\tag{266.25}
$$

的步长均足够；当 $L=0$ 时右侧正即已满足余项条件。

**证明。** (266.23) 使余项最终小于 $\lambda\gamma$；或直接用 (266.24) 代入 (266.21)。证毕。

这里有三个不可省略的限制：

- 该论证不保证原十个步长中有一个满足 (266.25)。例如理论所需上界可以比 $2^{-9}$ 更小。
- 在实际浮点程序中，基点/求值误差存在非零底限时，继续把 $\lambda$ 变小会使理论下降量也趋零，未必改善判据；实际 trial 还可能舍入回原节点而只能得到相同 norm。
- 参考函数在小邻域光滑，不能单独保证原 root 求解器在每个浮点 trial 都完成。原 positivity、root solver 和全部实际 guards 仍由原程序执行。

因此“精确 Newton 方向在足够小步长下降”不能直接解释成“原有限十步回溯应当成功”，更不能在原失败后直接断言方向一定错误。

## 266.7 任意可逆行/列缩放及其浮点限制

**定理266.5（精确变换等价性）。** 设 $L,C$ 是任意同阶可逆实矩阵。原有限数组线性系统

$$
A\delta=-\widehat r
$$

与

$$
(LAC)z=-L\widehat r,\qquad \delta=Cz
\tag{266.26}
$$

具有一一对应的解。无需假定 $A$ 可逆；若一个系统无解或有多个解，另一个系统也对应如此。

**证明。** 用可逆 $L^{-1}$ 左乘第二式，并代入可逆变量映射 $\delta=Cz$，得到第一式；反向同理。证毕。

对于任意未完全求解的 $z$，设

$$
\widetilde e=LACz+L\widehat r.
$$

对应原缺陷满足

$$
e=L^{-1}\widetilde e,\qquad
\|e\|_{\sigma,\infty}
=\|WL^{-1}\widetilde e\|_\infty
\le\|WL^{-1}\|_\infty\|\widetilde e\|_\infty.
\tag{266.27}
$$

列缩放不会从数学上删掉任何模式或节点，但最终必须用实际恢复的完整 $\delta$ 回到原 (266.8)、原 $\sigma$。缩放后的一个很小 residual 数字本身没有原残差含义；把所有行乘任意很小正数即可使该数字很小，而原 $e$ 不变。若特取 $L=W$ 并确实按精确变换形成数组，则 $\|\widetilde e\|_\infty=\|e\|_{\sigma,\infty}$。

### 实际保存的缩放矩阵并非自动精确变换

如果实际程序形成的是已舍入数组

$$
\widetilde A=LAC+\Delta_A,\qquad
\widetilde r=L\widehat r+\Delta_r,
$$

并把恢复后的实际方向记为

$$
\widehat\delta=Cz+h_C,
$$

那么，令 $\widetilde e=\widetilde A z+\widetilde r$，其精确原缺陷为

$$
\boxed{
A\widehat\delta+\widehat r
=L^{-1}(\widetilde e-\Delta_A z-\Delta_r)+Ah_C.}
\tag{266.28}
$$

**证明。** 展开 $\widetilde e=LACz+L\widehat r+\Delta_Az+\Delta_r$，左乘 $L^{-1}$ 后加上 $Ah_C$。证毕。

若报告的 $\widetilde e$ 又是浮点 matvec 求值，其自己的求值误差仍须按 (266.11) 处理。最直接的实际诊断是：保留恢复后的原完整 $\widehat\delta$，用原完整 $J_n,\widehat r_n,\widehat r_c,\widehat r_f,G_\infty,\sigma$ 重新记录 (266.8)。这样不会因缩放、重排行、列参数化或求解器自己的 residual 定义而漏掉原缺陷；是否是严格包络仍按实际误差账如实说明。

## 266.8 原 Riccati 消元在精确代数中的含义

把每个实际 $J_n$ 按 $q/p$ 分块：

$$
J_n=
\begin{pmatrix}T_{11,n}&T_{12,n}\\T_{21,n}&T_{22,n}\end{pmatrix}.
$$

原校正方程是

$$
\delta_n=J_n\delta_{n+1}+\widehat r_n.
\tag{266.29}
$$

从 far 边界开始定义

$$
\Gamma_N=G_\infty,\qquad b_N=-\widehat r_f.
$$

假设已经有 $\delta p_{n+1}=\Gamma_{n+1}\delta q_{n+1}+b_{n+1}$，再定义

$$
C_n=T_{11,n}+T_{12,n}\Gamma_{n+1},\qquad
D_n=T_{21,n}+T_{22,n}\Gamma_{n+1},
$$

$$
t_n=T_{12,n}b_{n+1}+\widehat r_n^q,\qquad
u_n=T_{22,n}b_{n+1}+\widehat r_n^p.
\tag{266.30}
$$

若每一步所需 $C_n$ 可逆，则

$$
\Gamma_n=D_nC_n^{-1},\qquad
b_n=u_n-\Gamma_nt_n.
\tag{266.31}
$$

给定 cut 条件 $\delta q_0=-\widehat r_c$ 后，先取
$\delta p_0=\Gamma_0\delta q_0+b_0$，再向前恢复

$$
\delta q_{n+1}=C_n^{-1}(\delta q_n-t_n),\qquad
\delta p_{n+1}=\Gamma_{n+1}\delta q_{n+1}+b_{n+1}.
\tag{266.32}
$$

**命题266.6（原消元的精确等价性）。** 若上述所有逆存在，(266.30)–(266.32) 的精确实运算给出原全部 stage/cut/far 校正方程的唯一解，故其 $e=0$。

**证明。** 代入 (266.29) 的上半块得到
$\delta q_n=C_n\delta q_{n+1}+t_n$，下半块得到
$\delta p_n=D_n\delta q_{n+1}+u_n$。消去 $\delta q_{n+1}$ 即得 (266.31)，所以每次反向图更新等价于原两块方程及下一节点图关系。最后 cut 指定唯一 $\delta q_0$，(266.32) 逐节点唯一恢复全部分量。反向构造已包括 far，正向恢复满足每个原 stage，因而是完整唯一解。证毕。

源码正是这个符号方向：bs[depth]=-ev.end，t 加 stage 的 q 残差，u 加 p 残差，cut q 校正为 target 减当前 q。不能因误换 stage 方向而把后续缺陷写成相反符号。

### chart condition 不能替代完整缺陷

原 maxChartCondition 计算的是各步已形成矩阵 C 和其显式计算逆 Gi 的浮点量

$$
\operatorname{stored}\bigl(\|C\|_\infty\|\mathrm{Gi}\|_\infty\bigr).
\tag{266.33}
$$

只有在 Gi 确实等于 C 的精确逆、范数计算也按精确实数解释时，它才是该 C 的精确 $\kappa_\infty(C)$。它不是整个 shooting 矩阵 A 的条件数，也不是 (266.6) 的残差。实际反向图、右端和正向恢复还有各自的浮点舍入。

两个简单反例说明不能作相反推断：

1. 对 $C=\operatorname{diag}(1,\varepsilon)$，$0<\varepsilon<1$，条件数为 $1/\varepsilon$，可任意大。右端 $(1,0)$ 的解 $(1,0)$ 仍可给零残差。因此大条件数不强迫本次右端出现大缺陷。
2. $C=I$ 的条件数为1，但若恢复的校正本身不解原右端，原残差仍可任意大；小的局部条件数也不控制其他 stage、图传播、矩阵形成、导数误差或 nonlinear 余项。

甚至中间图 chart 奇异也不等价于全 A 奇异。取 $M=1,N=2$，

$$
J_0=J_1=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad G_\infty=0.
$$

齐次 stage 方程使 $\delta_0=J_0J_1\delta_2=\delta_2$；cut $\delta q_0=0$ 与 far $\delta p_2=0$ 强迫全部校正为零，所以完整方阵 A 可逆。但最后一层 $C_1=0$，以 $\delta p_1$ 表成 $\delta q_1$ 函数的该 Riccati chart 失效。失效的是选定图坐标，不是全部边值线性问题没有唯一解。

这些反例不证明实际25属于其中哪一种情形。实际因果必须由原完整 e、参考导数误差及真实 trial 回执区分。

## 266.9 实际记录可以回答什么

若实际原 correction 已返回完整有限 $\delta$，下列同次、同基点数据足够定义本文的有限代数模型：

- 全部原 stage 的实际 J、原残差，完整 cut/far 残差；
- 原 target、far 图、gains 与实际 $\sigma$；
- 原完整基点和返回的完整校正，保留实际位模式；
- 各原 trial 的实际步长、节点更新、原 norm 或原拒绝类型及位置。

保留各 $C,\mathrm{Gi},\Gamma,b$ 可以进一步定位消元中的误差，但它们的 condition 数字不能代替回原方程后的 e。若只保留总 norm、maxChartCondition 和 line-search failure，尚不足以判断此次校正是否解准了自己的完整有限线性模型。

这份记录可按下列顺序解释，而无需先改变原验收条件：

| 已有证据 | 能得到的结论 | 尚不能得到的结论 |
|---|---|---|
| 完整有限数组的原尺度 e 小 | 此实际校正近似解了自己的完整数组线性模型 | J 是精确 DF；原 nonlinear trial 必下降 |
| 某步实际模型 $g_\lambda>0$ | 该有限模型在该步预测下降 | 真实 flow/算术余项小于该余量 |
| 完整误差账满足 (266.20) | 原返回 norm 必严格下降 | 其他科学接受门已完成 |
| 原 trial 实测 norm 严格下降且过原 guards | 原这一次 line search 可接受 | 全部 Newton 收敛、完整 J/audit 和闭面标准已完成 |
| 某个 chart condition 极大 | 该局部表达对舍入可能敏感，值得结合原缺陷定位 | 本次完整线性缺陷一定大或全 A 必奇异 |

本结果允许比较保持原方程的可逆行/列缩放或其他线性求解后端，但不预先选择新算法、不减 modes、不改 cut/far、不改 $\sigma$、不扩大原容差，也不把新增诊断设为继续原计算的审批门。

