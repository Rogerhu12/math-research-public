# R264 — 原 native 初猜的下溢契约与完整舍入误差账

日期：2026-11-14。状态：已证明（完整条件代数命题）及源码契约核对；含实际公开 Actions 22 的一个已记录事件。不含新数值计算，不把初猜或 no-J 探针当作已接受尾解。

## 264.1 结论和适用范围

原 finite-tail shooting 求解器允许某些深节点分量为零。对于同一完整物理高度向量 \(H\)、同一离散参数、同一实际远端 Robin 图和原残差尺度，可以把有限乘除运算自然舍入得到的深处零保留在一个**未接受的完整初猜**中，再由原完整非线性求解与审计决定是否接受。这不要求、也不允许把非零 cut 高度阈值化为零。

同 RK 初猜器 v2 对“两个非零有限数相乘，或非零有限数除以有限非零数，结果却为零”的拒绝，是该新初猜器增加的保护，并非原 native 的科学接受条件。保留真实舍入零与删除相应 Fourier 模式不同：前者仍保存所有节点、所有 \(2M\) 分量；原完整耦合流、Newton 修正、Jacobian 和最终审计仍可在这些分量产生非零量。

本文证明的误差账相对于**实际存储的 binary64 传输块、图、分母和状态**。它不把这些量当成精确 ODE 基本解，不从小下溢量推断几何误差小，也不新增任何课题完成门。

## 264.2 原源码契约

核对基准为公开仓库提交 `364ebd962d66c3157ffce346ceed105cb27ff514`。主要源码：

- [`78718-tail-tangent-core.mjs`](../../visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs)：`initial`、`scaleFor`、`evaluate`、`solve` 及 `createCompactTailDN.solve`。
- [`78718-tail-fourier-root-momentum.mjs`](../../visible-flexible-closed-surface/scripts/78718-tail-fourier-root-momentum.mjs)：`geometry`、`evaluateL`、`root`。
- [`78718-prefix-tail-tangent-fourier-worker.mjs`](../../visible-flexible-closed-surface/scripts/78718-prefix-tail-tangent-fourier-worker.mjs)：完整请求、可选 initial、原 solve 与 response 路径。
- [`tail_resumable_engine.mjs`](../computations/tail_resumable_engine.mjs)，SHA256 `1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8`：原图插入及已接受 trial 的恢复记录，不另设下溢门。
- [`exact_20261114_true_tail_client.py`](../computations/exact_20261114_true_tail_client.py)，SHA256 `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09`：完整有限 \(H\)、原收敛和残差、完整 jets/J，以及请求的 audit 检查。
- [`geometry_20261114_zero_rk_stage_initializer_v2.mjs`](../computations/geometry_20261114_zero_rk_stage_initializer_v2.mjs)，SHA256 `c6146b9566031ec636949f94bcbbe4b6fd051002bdb5949a6c70821e0d0c1879`：待区分的新增初猜保护。

上述三个 78718 源分别具有 SHA256 `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`、`cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88`、`36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a`；已与实际22的 `verified-launch-intent.json` 中 `current_sources` 和 `original_source_sha256` 两表及公开 Git 字节逐项相核。

原 `initial(target)` 直接执行

\[
Q_{0j}=\mathrm{target}_j,\qquad
\Pi_{0j}=\operatorname{RN}(G_{0j}Q_{0j}),
\]
\[
Q_{n+1,j}=\operatorname{RN}(Q_{nj}/\mathrm{gain}_{nj}),\qquad
\Pi_{n+1,j}=\operatorname{RN}(G_{n+1,j}Q_{n+1,j}).
\]

这里没有“非零输入必须给非零输出”的检查。`solve` 对传入的 `opts.initial` 复制为完整 `Float64Array`，随后进入原 `evaluate`。在其原始契约中，初猜可以有较大残差，可以不满足远端条件；是否收敛由后续实际过程决定。

原 `evaluate` 检查每个 stage 的完整向量残差、全部 cut 分量和全部深端 Robin 分量，其归一化为

\[
\sigma_0=\max(10^{-250},\|\mathrm{target}\|_\infty),\qquad
\sigma_{n+1}=\operatorname{RN}
   (\sigma_n/|\mathrm{gain}_{n,0}|).
\tag{1}
\]

式 (1) 的小数常数表示原 JavaScript 字面量 `1e-250` 的实际 binary64 值；以下误差账使用实际保存的 scales，不以精确实数常数重算它。这里是原 `gains`，不能换成新初猜器的私有传输分母。完整原 `root` 仍要求几何参数可表示、\(D,S,A\) 均高于原 `projectionFloor`，并按原 SPD/局部 Newton 路径求根。原外层保持原容差、line search、完整 J 和所请求的审计。

零分量本身不违反这些门。特别地，在原几何点及全部相关系数合法有限、整个形状态 \(Q=\Pi=0\)，并采用原默认 root 初值 \(L=0\) 时，源码给出 \(P=P_\theta=L=0\)，故 \(D=S=A=1\)，原 root 残差为零。此事实不保证“仅某一高模为零、其余模式非零”的任意态也处于原正性域；后者仍必须实际求值。

| 检查 | 所属契约 | 本文处理 |
|---|---|---|
| 完整有限 \(H\)、固定源/配置/实际远端与原 scales | 原接口及当前身份要求 | 全部保持 |
| 私有 \(T,g,u\) 有限，所用分母 \(u\ne0\) | 当前初猜图的可计算条件 | 保持；不把它叫作原非线性科学门 |
| 有限 \(g,Q\ne0\) 而 `g*Q===0` 即拒绝 | v2 新增初猜保护 | 可只记录真实舍入损失，保留实际运算结果 |
| 有限 \(Q\ne0,u\ne0\) 而 `Q/u===0` 即拒绝 | v2 新增初猜保护 | 同上 |
| 非零 \(H\) 在原 cut 转换中变零 | v2 的入口保护，非原 native 检查 | 本次后继范围仍保留，不放宽入口 |
| 非有限结果、原 root/流正性、原残差与最终实际审核 | 原运算/接受路径 | 不修改、不绕过 |

有限 \(T\) 的行列式诊断同样属于私有构造：图公式只除 \(u=a+b g_{n+1}\)。v2 已对有限舍入行列式零保留记录而不据此拒绝；本文不以此证明 \(T\) 可逆或线性积分准确，也不要求再修改任何剩余构造拒绝。

## 264.3 算术约定与一个舍入到零的引理

令 \(\mathbb F\) 为有限 binary64 数。进行实数代数时将正负零均解释为实数零；记录身份时保留二者不同的 64 位模式。令 \(\operatorname{RN}\) 为 ECMAScript `Number` 的最近值、等距取偶数舍入。其最小正非零值为

\[
\mu=2^{-1074}.
\]

ECMAScript 规范的 Number 定义及 `Number::multiply`、`Number::divide` 规定这一数值集合和对应乘除规则；此处仅使用有限乘除，不把 `Math.exp`、`Math.sqrt`、`**` 或整个 RK 计算当成精确实函数。

规范依据：[ECMA-262 §6.1.6.1、§6.1.6.1.4–5](https://tc39.es/ecma262/multipage/ecmascript-data-types-and-values.html#sec-ecmascript-language-types-number-type)。

**引理 264.1（真实下溢的精确局部损失）。** 设有限非零操作数的精确实乘积或商为 \(x\ne0\)，商的分母非零。若该有限运算给出带符号零，则

\[
0<|x|\le\frac\mu2,\qquad
\eta=\mathbb R(\operatorname{RN}(x))-x=-x.
\tag{2}
\]

其零符号由乘除的操作数符号确定。反过来，\(0<|x|\le\mu/2\) 时，最近值、等距取偶数规则给出相应符号的零。

**证明。** 实数零与最近非零 binary64 值之间距离为 \(\mu\)。在相邻两个值的中点，零的有效数为偶数，故中点也舍入到零；中点外最近值不再是零。符号规则由原乘除运算给出。实数解释后的结果为零，因此误差恰为 \(-x\)。证毕。

这不是手工设定的 epsilon 截断。尤其 \(\mu/2=2^{-1075}\) **不能再作为 JavaScript Number 数值写入报告**：它会再次舍入成零。应保存精确比值或可恢复它的运算描述，例如操作种类、两操作数与结果的 `float64le` 位串，再以整数/有理数解码。对 binary64 商，精确商一般不是有限二进制小数；不能以格式化的短十进制近似充当精确损失。

本文以下所有等式中的已存储数，都按其实际 binary64 位模式解释为精确有理数。cut 所用 \(R_4\) 是原程序实际 `radius**4` 的返回值；不在这里把它替换成真实半径的精确四次幂。

## 264.4 保持原 cut 与远端的有限初猜命题

设 \(M\) 为完整模式数，\(d\) 为完整 stage 数。对每个模式 \(j\)，已有实际保存的

\[
T_{nj}\in\mathbb F^{2\times2},\qquad
g_{nj}\in\mathbb F,\qquad
u_{nj}\in\mathbb F\setminus\{0\},\quad 0\le n<d,
\]

以及 \(g_{dj}=G_{dj}\)，其中 \(G_d\) 是原 live native 的实际远端图，逐项复制且未改动。所有物理 \(H_j\) 原字节保持，定义原转换

\[
\widehat q_{0j}=\operatorname{RN}(H_j/R_4),
\tag{3}
\]

并保留既有入口有限性与非零 \(H\) 转换保护。接着逐节点执行

\[
\widehat\pi_{nj}=\operatorname{RN}(g_{nj}\widehat q_{nj}),
\qquad
\widehat q_{n+1,j}=\operatorname{RN}(\widehat q_{nj}/u_{nj}).
\tag{4}
\]

**命题 264.2（有限舍入初猜）。** 如果 (4) 的实际结果均有限，则把其中由原乘除自然产生的零原样保存，会得到完整 \((d+1)\times2M\) 初猜；这不改变 cut 请求 \(H\)、原 target 转换、原远端算子、原 \(M,d\)、原 scales 或后续任何原接受条件。

**证明。** 初始数组每行具有完整 \(2M\) 分量。(3) 与原 DN 的 target 转换相同，(4) 只把实际运算结果赋给对应位置，故不会删除节点或模式。有限零仍是合法的有限数组元素。最后一行用原远端 \(G_d\)，而整个构造只使用私有 \(g,u\)，无须写入原 live `graphs/gains`。将此数组通过原 `opts.initial` 传入时，原 `solve` 仍按原 \(H\) 重新构造 target/scales 并执行全部原流、残差和求解路径。因此改变的是待检验初值，不是原问题或其接受定义。证毕。

命题并不保证构造完成：之后仍可能出现非有限结果，或既有私有 chart/原 geometry 拒绝。也不保证新初猜的原 no-J 残差更小、Newton 收敛、完整 J 有效或 audit 通过。

这里的“保持 cut”指保存全部原物理输入和原转换；不宣称

\[
\operatorname{RN}\!\left(R_4\operatorname{RN}(H_j/R_4)\right)=H_j
\]

逐位恒等。后续实际 jets 仍由原程序计算，不能用此初猜命题冒充物理高度六 jet 的精确匹配。

## 264.5 包含图舍入的精确局部残差恒等式

固定一个模式，暂省略下标 \(j\)。将真实保存的每个分量按精确实数解释，记

\[
v_n=\binom{1}{g_n},\qquad
\widehat y_n=\binom{\widehat q_n}{\widehat\pi_n},
\]
\[
\eta^q_n=\widehat q_{n+1}-\frac{\widehat q_n}{u_n},\qquad
\eta^\pi_n=\widehat\pi_n-g_n\widehat q_n,
\qquad
\xi_n=\binom0{\eta^\pi_n},
\tag{5}
\]

以及实际图的代数缺陷

\[
\Delta_n=T_n v_{n+1}-u_n v_n.
\tag{6}
\]

即使每个 \(g,u\) 来自预定 Riccati 公式，也不能未经计算宣称 \(\Delta_n=0\)：乘法、加法和除法都已各自舍入。

**定理 264.3（共享实际节点的局部恒等式）。** 对任意满足上述有限性条件的节点，均有精确实数等式

\[
\boxed{
T_n\widehat y_{n+1}-\widehat y_n
 =u_n\eta^q_n v_n
  +\widehat q_{n+1}\Delta_n
  +T_n\xi_{n+1}-\xi_n .}
\tag{7}
\]

**证明。** 由 (5)，

\[
\widehat y_n=\widehat q_n v_n+\xi_n,
\qquad
u_n\widehat q_{n+1}-\widehat q_n=u_n\eta^q_n.
\]

再用 \(T_n v_{n+1}=u_n v_n+\Delta_n\)，得

\[
\begin{aligned}
T_n\widehat y_{n+1}-\widehat y_n
&=\widehat q_{n+1}(u_n v_n+\Delta_n)
  -\widehat q_n v_n+T_n\xi_{n+1}-\xi_n\\
&=u_n\eta^q_n v_n+\widehat q_{n+1}\Delta_n
  +T_n\xi_{n+1}-\xi_n.
\end{aligned}
\]

证毕。

因此，不需要记录每次普通浮点乘除的中间值，也能由完整的 \(T,g,u,\widehat y\) 恢复 (5)–(7)。专门的 underflow 事件记录用于识别真实损失位置，不能代替其余普通舍入和图缺陷的账。

取任一标准 ℓp 向量范数（1≤p≤∞）及其诱导矩阵范数，故 ∥(0,η)∥=|η|，(7) 给出

\[
\|T_n\widehat y_{n+1}-\widehat y_n\|
\le |u_n\eta^q_n|\,\|v_n\|
 +|\widehat q_{n+1}|\,\|\Delta_n\|
 +\|T_n\|\,|\eta^\pi_{n+1}|+|\eta^\pi_n|.
\tag{8}
\]

若要与原 stage 残差尺度比较，(7) 或 (8) 必须除以原 \(\sigma_n\)。height 传播 \(n\to n+1\) 的误差虽存于目标节点，其该 stage 残差不是未经传输便除以 \(\sigma_{n+1}\)。记录源、目标两个 scales 或其明确的原记录引用可消除这一歧义。

**零后的传播。** 若一次实际除法得到 \(\widehat q_{n+1}=0\)，之后同模的有限非零分母除法仍给带符号零，乘以有限 \(g\) 也给零。正常的零继续传播不应反复计为新 underflow。对于选定零态分块，首次跨越这一零的局部实残差恰为

\[
T_n\widehat y_{n+1}-\widehat y_n=-\widehat y_n.
\]

这仅是选定分块的结论。原非线性 stage 同时消费所有模式，不能据此把该模式从原流中删除。

## 264.6 全段传播与“绝对量极小”的局限

仍固定一个模式。以实际保存的 \(u,g\) 定义一个精确有理数参考递推

\[
q_0^*=\widehat q_0,\qquad
q_{n+1}^*=q_n^*/u_n,\qquad
\pi_n^*=g_nq_n^*.
\tag{9}
\]

这不是精确 ODE 解，也未假设满足实际 \(T\) 的无缺陷图关系。

**定理 264.4（实际分母下的舍入传播）。** 设 \(e_n=\widehat q_n-q_n^*\)。则

\[
e_0=0,\qquad e_{n+1}=e_n/u_n+\eta^q_n,
\]
\[
\boxed{
e_n=\sum_{k=0}^{n-1}\eta^q_k
        \prod_{\ell=k+1}^{n-1}u_\ell^{-1},\qquad
\widehat\pi_n-\pi_n^*=g_ne_n+\eta^\pi_n .}
\tag{10}
\]

相应绝对上界由各项取绝对值求和得到。

**证明。** 将 (5) 的第一式减去 (9) 即得递推；从 \(e_0=0\) 逐次代入得到有限和，空积取 1。第二式由 (5) 直接得出。证毕。

即使首次丢失量不超过 \(2^{-1075}\)，后续 \(u^{-1}\) 仍可能放大它。特别地，实际浮点序列归零后，(9) 的未舍入参考序列可能因后续小分母重新变大。因此不能仅凭“进入 subnormal 区”推断全段状态差、原归一化残差或最终 DN 误差可忽略。

反之，初猜没有义务先把 (10) 证到某个新阈值再进入原求解器。(7)–(10) 是诊断和追溯公式；实际原非线性残差与原接受流程仍是本计算路径的判据。

## 264.7 原 far 浮点零与精确实缺陷

因为 \(g_d=G_d\)，精确实数 Robin 缺陷为

\[
\widehat\pi_d-G_d\widehat q_d=\eta^\pi_d.
\tag{11}
\]

而原 native 执行的是

\[
\operatorname{RN}\!\left(
\widehat\pi_d-\operatorname{RN}(G_d\widehat q_d)\right).
\tag{12}
\]

如果初猜的最深动量正是同一次形式的乘法返回值，则 (12) 数值上为零。这并不推出 (11) 也为零。如果最深 \(\widehat q_d\) 本身为零且 \(G_d\) 有限，那么 (11) 才也确实为零。该区分不改变原 far 方程或原验收，而是防止把浮点重复运算得到的零错误解释成精确实数证书。

也不能据若干深处形状分量为零就宣布存在解析轴对称 collar、无穷尾已闭合或获得光滑极限。那些几何结论仍需原课题规定的同场验证。

## 264.8 与真正非线性残差的精确账面关系

将全部模式的 \(T_n\) 组装为按原 \(Q\)/\(\Pi\) 排列的块对角矩阵 \(\mathcal T_n\)。设实际原 `cellFlow` 在完整输入 \(\widehat Y_{n+1}\) 上返回的浮点向量为 \(\widehat\Phi_n(\widehat Y_{n+1})\)，并定义

\[
N_n=\widehat\Phi_n(\widehat Y_{n+1})
       -\mathcal T_n\widehat Y_{n+1},
\]
\[
\epsilon^R_n=
\operatorname{RN}\!\left(\widehat\Phi_n(\widehat Y_{n+1})-\widehat Y_n\right)
 -\left(\widehat\Phi_n(\widehat Y_{n+1})-\widehat Y_n\right),
\]

其中第二式逐分量解释。于是原存储的 stage 残差满足

\[
\widehat R_n=
\left(\mathcal T_n\widehat Y_{n+1}-\widehat Y_n\right)+N_n+\epsilon^R_n.
\tag{13}
\]

这是加减同一项得到的恒等式。\(N_n\) 包含原非线性作用、模式耦合、选定零态传输与实际流的差，以及相应浮点求值差；未经额外分析不能仅称其为一个已证的 \(O(\|Y\|^2)\) 余项。实际浮点归一化本身也会舍入，原报告的最大范数不因此自动成为严格区间界。

若要逐项严格重建 (13)，须保留实际 flow 的减法前输出，或为未保存的减法前值给出有向误差包络。仅凭最终浮点 residual 与输入相加，通常不能无损恢复该输出。当前最小 probe 只需保全部原 residual 和原 scales 以重建原数值范数；这足以履行该探针任务，不应把缺少 (13) 的逐项严格证书变成新的科学门。

原 no-J 与 with-J 路径的浮点运算次序还可能不同。no-J 回执只是该真实调用的结果，不能替代将来原完整 J、最终实际 audit 或整个 coupled 接受结果。

## 264.9 实际 Actions 22 的针对性适用

公开实际 run `43604874829`，job `132477286262`，artifact `14118131680`。完整包中 `same-RK-candidate-native-probe-v2/summary.json` 记录：factory 已完成，candidate 尚未完成，`evaluate_calls=0`，原方法、图、gains、远端和布局保持。

`initializer-v2-construction-045-000.json.gz` 的事件 `sequence=1426` 保存：

| 字段 | 实际存储值 |
|---|---|
| `kind` | `prediction-height-rejected` |
| `source_node` → `target_node` | 261 → 262 |
| `mode` / `zero_based_mode_index` | 112 / 111 |
| `Q` | `-5e-324` |
| `denominator` | `275.8821411118115` |
| `next_Q` | `0` |
| `nonzero_underflow` | `true` |

这里 JSON 的 `Q` 恢复为最小负 binary64 数 \(-\mu\)。把实际分母 binary64 值记为 \(u\)，已存数值直接给出 \(u>2\)。所以，无需重算任何 ODE 或初猜，即由引理 264.1 得

\[
0<\mu/u<\mu/2,\qquad
\operatorname{RN}(-\mu/u)=-0,\qquad
\eta^q_{261}=\mu/u.
\tag{14}
\]

v2 该事件仅将结果序列化为 JSON `0`，没有另存此字段的符号位；式 (14) 的负零来自已核乘除语义，不能称为该 JSON 已独立保存的结果位证据。后继事件应直接保存其 float64 位串。

因此本次停止确实落在新增“非零除法结果为零”保护上；没有运行原 candidate no-J 流，故既不能说原流已接受该候选，也不能说原流在此处违反正性或残差门。最小有据后继是保留原 H/cut 和全部模式，只对真实有限私有乘除下溢记账并继续生成完整候选，再执行原一次 no-J 探针；不自动推断可以省略原求解、完整 J 或最终审计。

这里仅利用实际已记录操作数及 \(u>2\) 的代数事实，没有本地重演数值模型、继续预测、求新原残差或改写实际回执。

## 264.10 后继最小记录契约

每次真实非零操作数乘除得到带符号零时，保留：

1. 原 source/config/H/cut 身份和初猜器的新 source 身份；不能冒 v2 原 SHA。
2. 操作种类、节点（除法同时保源/目标节点）、模式和频率；两个实际操作数及实际结果的 `float64le` 位串。
3. 精确损失描述 `stored_result - exact_operation(decoded_operands)`，可只保存可重建 recipe；不能把损失再次转 Number 而报零。
4. 原 residual scale 的位身份：乘法保同节点，跨节点除法明确源和目标两个 scales 或原 scales 的可核引用。
5. 本次与累计真实 underflow 数；输入已经为零而继续得到零，不冒作新损失。
6. 完整候选的全部节点/分量、signed-zero 身份、hash、原 `rawNode` 对应关系，以及完整原 no-J stage/cut/far 残差、原 scales 和实际失败位置。

原非有限检查、有限非零分母检查、cut 转换保护、source/物理配置和 live 数据不变检查都保持。实际事件账与 (7)–(13) 不新增通过阈值；它们说明发生了什么以及哪些量尚未获证。若原 no-J 尚未运行或未完成，完整非线性残差表必须继续标为不存在。

## 264.11 与课题完成标准的关系

本结果解决的是“初猜自然深处零是否违反原求解契约”及如何保留可核误差账。它不证明非线性尾解存在，不证明新的 coupled 父场已接受，不证明同 \(g\) 收敛、全域 operator/曲率、reach、held amplitude、闭曲面或全相位族条件。所有这些仍须由本公开仓库对实际同场对象继续完成；不能借初猜的符号零或原浮点残差零跳过。
