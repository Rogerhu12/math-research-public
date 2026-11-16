# R471 — 原有限轨迹中零非线性通量方向的有限算术快路径

作者：AI（amplitude）；日期：2026-11-16。

可信度：**已证明（限本文的来源、实际资格条件与局部控制流命题）；新源码尚未执行，实际适用次数、耗时、完整求解和最终接受均未付。**

## 471.1 结论与最窄变更

本结果实施 [R470](R470-zero-shape-finite-root-trace-full-local-block-variation.md) 所留的一个局部切点：在原 no-J root/RHS 和完整 `finiteRootDirection` 已经真实返回之后，只对 `splitRhsDirection` 的非线性角通量方向选择快路径。选择成功时保留该函数**原先分配的正零 `dFlux` 数组**；随后仍执行原完整末端装配、两个 mean 行及原 `finiteArray`。选择不成功时执行原完整角循环。它既不拒收该状态，也不改变任何科学接受阈值。

该实现没有采用 R470 中更强的小块矩阵替代。原完整局部矩阵、稠密 `linear`、RK、cusp 分段、端口、cut/far、完整列数和所有下游责任仍保留。$M=112$ 时仍形成完整 $226\times224$ 局部方向；两个 mean 的 primal 与方向责任不被删除。

新增条件同时检查**本次现场**与所有被跳过运算中可能非零的中间量。它不只检查输入有限，不将 `pref*target_factor` 约为 `sigma`，也不使用字面三角表的正交恒等式。局部结论是：在资格成立、标准 binary64 RN 算术和相同固定现场下，原角循环的每个最终 `dFlux` 词都是正零，因此原数组已经给出相同词。本文不将这个局部结论扩大为整个运行、资源停止时刻或一般 R466 数值方向与原 195 的逐词等价。

## 471.2 精确来源与独立身份

| 来源 | 字节数与 SHA-256 | 使用范围 |
|---|---|---|
| [R470 条件证明](R470-zero-shape-finite-root-trace-full-local-block-variation.md) | 19507；`6f0eae3da217eab6bde51794e15d3ed36ed116a81eddebe381ea0095b7d40475` | 实际零现场、完整有限根方向、非线性与线性通量的区别 |
| [R466 原 variation](../computations/geometry_20261116_original64_contracted_finite_trace_variation.mjs) | 12270；`e6be662ba5c795d4e3f91bbcead469482c746520b36b1d4c14a1c49b00dd2bb6` | 本次完整文本基线 |
| [R466 原 contraction](../computations/geometry_20261116_recorded_factor_contracted_solve.mjs) | 11427；`2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59` | 原已接受更新的方向求解与其 fallback；本次字节不变 |
| [新资格 helper](../computations/geometry_20261116_zero_nonlinear_split_flux.mjs) | 7111；`e6ce93089c0ee03324fbaeb86ced15b1852b3ad498b322c4adfd959d7c869fde` | 当前现场、稀疏方向、完整角行与所有方向对的有限性 |
| [新 variation](../computations/geometry_20261116_original64_zero_flux_contracted_finite_trace_variation.mjs) | 12597；`d4f2f32b61c084a67615ebb26b88b62c7d18de06056f09f5f68f86efa0f143e0` | 新 schema、helper 调用、角循环分支及独立统计 |

新 variation 的 schema 为 `original64-zero-flux-recorded-factor-contracted-finite-root-variation-v1`，helper 的 schema 为 `original64-zero-nonlinear-split-flux-eligibility-v1`。旧源没有被覆盖或改标签。

相对原 variation 的完整差异只有：解释性文首、新 helper import、新 schema、包住原角循环的条件分支、一个新的统计对象。`finiteRootDirection`、原 fallback 角循环正文、末端装配以及 `completeFiniteRootTraceJacobian` 的函数正文均按文本逐字保留。这个说明来自源码文字比较，不是一次数值执行、测试或性能记录。

## 471.3 调用对象和实际资格

沿原符号，令 $M\ge1$、$N>0$、$J=M+1$、$K=2M$。状态长度为 $K+2$，根方向数组长度为 $JK$。`completeFiniteRootTraceJacobian` 仍按原顺序执行资源检查、`dimensions`、`finiteRootDirection`、`splitRhsDirection`，最后增加原完整局部矩阵计数。

新 helper 在原 `sigma`、`pref`、完整 `pCoefficient` 与所有原工作数组已经形成后调用。它消费同一次实际 `rt`、state、tape、字面表和根方向，不重新运行 primal，不修改任何输入数组。以下资格只决定“可否跳过角方向形成”；不成立返回 false，进入原角循环。

1. $M,N,J,K$、实际数组与角行长度相容，且 $N$ 是正整数。
2. 原 tape 明确无外给初猜，实际 `accepted_updates` 是空数组，`iterations` 为零，返回原因仍是 `normal-stop` 或 `original-roundoff-fallback`。
3. 实际 state 的全部 $Q,\Pi$ 项和返回根 $L$ 均为零，允许正负零。两个 mean 不要求为零。
4. 实际 `target_factor` 有限。根方向与原初始赋值逐词相同：全部默认槽为正零，唯一可能非零槽为 `dL[(j+1)*K+M+j]=target_factor`。此处的 `Object.is` 只选择实现分支；任何不等仍执行原算法，不是数值验收门。
5. 每个实际使用的频率、已形成 `pCoefficient`、`cs[n][j+1]` 与 `sn[n][j]` 有限。未使用的 `cs[n][0]` 不被偷偷加入科学条件。
6. 每个实际角行的 $P,P_\theta,L,K,U$ 均为零。该行照原正文调用 `angularPartials(v,rt.g,false)`；只要求实际 `factor` 的值及三个方向分量有限，且其值为零。
7. 第 471.5 节给出的每个形状方向对的完整可能非零中间量实际形成并为有限值。

`angularPartials` 仍会按原正文计算其 `q`。本角循环并不使用返回的 `q`，也不请求 `bm`，所以 helper 不以这两个未使用结果的有限性另设条件。原成功 primal 已付的分支不会由这个 helper 重做或替代。

本命题针对原单 worker 的实际普通记录和数值数组；在同一局部调用中它们不被外部并发改写。它不是对任意有副作用 getter、代理或外部共享缓冲突变的程序变换定理。

## 471.4 原完整根入口与统计没有被绕开

记 $\ell$ 为本次 tape 已形成的 `target_factor`。原 `initialDirection` 创建正零数组，并只进行上述 $M$ 次赋值。随后原 `finiteRootDirection` 核返回分支和更新数；其实际已接受更新列表为空，因此本次方向就是

$$
dL_{0,c}=+0,\qquad
dL_{j+1,c}=
\begin{cases}
\ell,&c=M+j,\\
+0,&c\ne M+j.
\end{cases}
\tag{471.1}
$$

这里 $+0$ 明确表示原数组的正零词；$\ell$ 若为负零也按原赋值保留。新 helper 的稀疏词检查核的就是这个结果，而不是另造一张理论矩阵。

原 `root_returns`、`zero_update_returns`、normal/fallback 返回计数、原 root 评价数、line trial 数和返回迭代直方图已由原共同入口增加。一般非空更新轨迹仍执行原全部残差/Gram、R466 contraction 或原 explicit fallback、原更新和非有限检查。新 helper 在其后发现不属于空轨迹时返回 false，不改变这些行为。

原 `complete_local_jacobians` 只在完整末装配和原 `finiteArray` 返回后增加。即使 helper 已选择快路径，后续原末端计算若失败，也不会把该调用标成已完成局部矩阵。

## 471.5 稀疏方向的完整有限性

固定一个角行和一个频率 $j$。简记

$$
m=\mathrm{freq}[j],\quad c=\mathrm{cs}[n][j+1],\quad
s=\mathrm{sn}[n][j],\quad p_*=\mathrm{pCoefficient}[j],
\quad f_r=\mathrm{factor}[r].
\tag{471.2}
$$

这些都是实际形成值，$\ell$ 仍取 tape 原词。下面使用代码表达式，保留原求值括号和左结合；不把它们当作可以自由重排的实数公式。

在 $Q_j$ 列，原 `dlv` 从正零开始，每个累加项都是有符号零，因此其结果为正零。原 `duv` 只有第 $j$ 项可能非零；新 helper 形成

```javascript
const q=(m*m-1)*pc;
const duQ=0+(-m*0+q)*sine;
const p=pc*sine;
const pt=m*pc*c;
const dFactorQ=f[1]*p+f[2]*pt+f[3]*0;
```

这里局部变量 `q` 只是原 `duv` 的显式线性系数，和 `angularPartials` 返回的未使用 `a.q` 不是同一对象。

在 $\Pi_j$ 列，原 `p`、`pt` 是三元分支给出的字面正零，只有第 $j+1$ 根方向槽可非零；新 helper 形成

```javascript
const dlPi=0+ell*c;
const duPi=0+(-m*ell+0)*sine;
const dFactorPi=f[1]*0+f[2]*0+f[3]*dlPi;
```

它逐方向检查 `q, dlPi, duQ, duPi, p, pt, dFactorQ, dFactorPi` 全部有限。每行全部 $M$ 个方向对均如此，覆盖所有 $2M$ 列。

**引理 471.1。** 在上述检查和实际稀疏词条件下，原完整角循环被省略的每个方向中间量都有限；helper 所形成的可能非零结果与原循环的对应结果具有相同 binary64 词。

**证明。** 所有非指定根方向槽是正零，所乘频率和表项有限，故各非指定乘积、加法项都是有符号零，不形成 `0*Infinity`。每个 `dlv/duv` 至多有一个可能非零累加项。该项之前，原正零累加器加任意个有符号零仍为正零；该项之后，加零不改变有限非零词。若该项本身下溢为负零，原前导正零将其加为正零，helper 中的显式 `0+...` 恰保留这一点；不能直接用乘积替换它。

唯一可能非零项的原括号分别是 `(-m*0+q)*sine` 和 `(-m*ell+0)*sine`。这些表达式、原 `pc*sine`、原左结合 `m*pc*c` 和原左结合三项 `dFactor` 均实际形成。这里若某个乘法先溢出为无穷，随后乘零会变 NaN，或继续保持无穷；相应完整表达式不会被 finite 检查误认为有限。三项加法也不能把已经产生的无穷恢复成有限数：相反符号无穷只会形成 NaN。因此这些检查排除了本段所有可能非有限的中间情况。

剩余跨 $j$ 项只有有限数与有符号零的乘积以及零加法，前述 signed-zero 结论适用。两类 `dFactor` 使用的 `dlv` 正是原词，且保留原乘法与加法次序，故结论成立。证毕。

对这一结论，必须保留 `angularPartials` 原实际 `factor` 的四个有限结果；仅从理论 $f_0=0$ 或几何输入有限推断它们是不够的。相反，对不进入原 split 角方向结果的未使用 `a.q`，无须人为增加有限性条件。

## 471.6 `dFlux` 的正零逐词结论

**引理 471.2。** 在完整资格成立时，原角循环的每一个 `dFlux` 元素在每次原 $n$ 累加之后均为正零。

**证明。** 原每列的非线性方向为

```javascript
df[col]=duv[col]*a.factor[0]+v.U*dFactor;
```

资格给出 `a.factor[0]` 和 `v.U` 都是某种零；引理 471.1 给出 `duv` 和 `dFactor` 有限。每个乘积因此是有符号零，二者相加仍为某种零，不会产生 NaN。原下一层的 `df[col]*sine/N` 使用实际有限 sine 和正的有限 $N$，故仍是有符号零。原 `dFlux` 由 `new Float64Array(M*K)` 初始化为正零。RN 算术中正零加正零或负零均为正零，归纳得到结论。证毕。

负零加负零会为负零，但此处每次累加的左操作数已由归纳证明是正零，所以这条例外不破坏结论。对于唯一非零方向项下溢的情况，引理 471.1 已单独保留其原前导正零；没有用“实数零不分符号”跳过这一责任。

**定理 471.3（局部快路径）。** 对同一固定现场，在资格成立时，新快路径和原 R466 split 角方向循环给出逐词相同的 `dFlux` 数组；若两条路径均正常完成原末装配及 `finiteArray`，则返回的完整局部方向矩阵逐词相同。

**证明。** 引理 471.2 表明原角循环的结果正是原已经分配的全正零数组，新路径不写该数组。后续使用的 `dL`、所有实际系数和表值均未被 helper 改动。原末装配正文逐字保留，故相同输入词按相同表达式得到相同结果词。证毕。

该结论包含原零符号责任，尤其保留

```javascript
linear=-m*L1+(m*m-1)*p1;
result[(M+j)*K+col]=(col===M+j?4*sigma:0)
  +pref*m*(linear+dFlux[j*K+col]);
```

的原加零位置，以及第一形状行、第一 mean 行中可能产生负零的乘法。它没有把整个结果数组重新构造成只填四个非零槽的默认正零矩阵。第二 mean 的形状导数行仍完整保留，第二 mean 的 primal 值没有被置零。

## 471.7 回退、资源与未完成状态

普通资格不成立只返回 false。原完整角循环正文执行，并按原 `finiteArray` 决定是否有非有限值；helper 不把“未能证明安全”变成科学拒绝，也不以新阈值批准原本失败的状态。

helper 不捕获任何异常。原 `resourceCheck`、分配失败、实际原角计算的异常或其他异常均直接向原调用者传播，不捕获后重跑。它在稀疏行和角行中调用原资源检查；`last_observation` 保留实际已到达的阶段、角和方向对，`calls_completed` 只在正常返回 true/false 时增加。

一次不合资格的零候选可能已经付过部分纯资格计算，随后再付原完整角循环，包括重算原纯 `angularPartials`。这是实现选择的额外成本，不重跑 primal/root，也不换状态或重开预算。额外检查与更少角运算可能改变实际资源消耗和原时钟触发位置，所以本文不声称整个运行具有同样停止时刻、相同已付阶段数量或相同最终资源结论。

## 471.8 统计与完整流程范围

新统计置于原统计对象的 `zero_nonlinear_flux` 下，分别记录开始/正常返回、实际零轨迹候选、成功保留正零通量、原角回退、完整检查过的稀疏项/角行/方向对、原因计数及最后位置。它没有从计数推填未访问现场，没有保存新可重算原科学表，也没有替代原 root/line/更新/局部矩阵计数。

`actual_zero_trace_candidates` 在已核空轨迹及 state/root 零、但尚未核完整角行时增加；它本身不表示最后快路径成功。`certified_zero_dflux_calls` 只表示本文局部资格已全部完成；它不是完整 Jacobian、阶段、BVP、domain 或连续解的接受旗标。

一般非零轨迹继续原 R466 contraction 与显式 fallback。原 R466 本来就是对记录系数 formal map 的另一种浮点实现；本结果没有追溯证明它与原 195 一般方向逐词等价，更没有把它变成 IEEE 舍入映射的导数。

本次没有改动原 flow、loader、原 no-J/root、稠密线性传播、RK/cusp、完整阶段/列、端口、QR、全部实际 trial、FD、fullDN、replay、audit 或 owner。未来透明来源视图必须显式 import 新 variation、登记两新源和真实 schema，不能以旧 e6be 源名声称已使用本结果。该接线和任何实际运行均另有来源责任。

## 471.9 复杂度与当前未付

每个零候选额外核稀疏方向的成本为 $O(M^2)$，每角仍付原 `angularPartials` 及全部 $M$ 个方向对的常数次算术，成本为 $O(NM)$。这替代的只是原角方向形成的 $O(NM^2)$ 循环。原最终完整矩阵装配、原稠密 tangent 传播与整个链的其他成本均未省。

因此有一个明确的局部运算量改进机会，但没有实际速度、适用率或全链收益结论。若条件失败，还可能有额外检查开销。没有以微基准、fixture 或对拍设新前门；没有进行本地科学执行、导入、AST、编译或测试。

当前已付的是：完整源变更、实际资格的充分性、有符号零和有限中间算术的条件证明、原回退/统计/末装配不变责任。未付的是：任何实际调用的条件记录、性能、完整求解接受、一般方向的严格舍入误差、分支邻域、准确连续解和最终闭面证书。
