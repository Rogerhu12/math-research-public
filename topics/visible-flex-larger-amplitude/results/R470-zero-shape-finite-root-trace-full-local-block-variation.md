# R470 — 原有限根轨迹在零形状处的完整局部变分分块条件命题

作者：AI（geometry）；日期：2026-11-16。

可信度：**已证明（限下述条件命题）**。本文逐字依据已发表的原有限根轨迹变分、原 no-J 状态流及原端口代码。没有执行科学程序，没有产生新的局部矩阵、运行时间或接受场，也没有修改 request195、request208、request209 或原 kernel。

## 470.1 结论与适用范围

在一个**实际已经返回**的原 root/RHS 现场，若原形状坐标 $Q,\Pi$ 为零、实际返回的全部 $L$ 为零、每个实际角行的 $P,P_\theta,L,K,U$ 为零，且原有限根轨迹没有外给初猜、没有任何已接受 Newton 更新，则原 `initialDirection` 已经给出该固定有限轨迹的完整根方向。原 split RHS 的非线性通量对全部 $2M$ 个形状方向的一阶项为零。其准确实代数因此只余每频率一个 $2\times2$ 块与**完整保留的两个 mean 行**；$M=112$ 时仍是完整 $226\times224$ 局部变分。

这不是把 root 换成隐式根方程的导数，也不要求独立的 `cs`、`sn`、`gramCos` 字面表满足准确正交关系。原 split 程序已经把其所定义的线性通量显式分离；本命题针对这个实际 split 程序，不能据此重标另一套未分离的数值求积 RHS。

准确实分块恒等式本身**不证明**一个稀疏替代实现与原 binary64 程序逐字相等。原程序可能在应当代数消去的乘积之前形成非有限中间量，且完整矩阵的某些零具有负号。一个未来捷径只有在这些工程条件也付清时才能跳过角方向循环；否则必须回到原完整路径。本文不实现这第二套捷径。

本命题不代替原 no-J primal/root、RK 四场、cusp 分割、完整链、QR、cut/far 条件、全部敏感度、FD、最终 replay/audit，也不由某次运行的零更新计数推断每个已删除现场均满足本文的全部前提。

## 470.2 精确源码来源

以下 SHA 是原源文本的 SHA-256；函数名给出真实插槽，不是拟定 API。

| 原源 | SHA-256 | 本文使用的实际正文 |
|---|---|---|
| [finite trace kernel](../computations/geometry_20261115_original64_finite_trace_variation.mjs) | `742ab15a2168084167eeab9879a074ee1cd586d33f324e837223134a8cbf9705` | `dimensions`、`initialDirection`、`finiteRootDirection`、`angularPartials`、`splitRhsDirection`、`completeFiniteRootTraceJacobian` |
| [matched finite trace flow](../computations/geometry_20261115_original64_finite_trace_flow.mjs) | `a7a90668a7d2f4df93e0bd03d665f439dab2fb2461bedf544725cd01c2a7b470` | `field`、`fromCaptured`、`linear`、`oneOriginalStep`、`flowStateWithJacobian` |
| [literal source observer](../computations/geometry_20261115_original64_finite_trace_loader.mjs) | `55b2a4a344ae2eb7d78f26b7954b20f9cbe4e4969588bf3a236e7828d6f299ae` | 原 root 的单锚替换、`target_factor:f`、原返回原因及只记录实际接受更新、原字面表直接暴露与反向恢复检查 |
| `topics/visible-flexible-closed-surface/scripts/78718-tail-fourier-root-momentum.mjs` | `cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88` | `data`、`evaluateL`、`root`、原 `target` 初猜及 root 政策 |
| `topics/large-amplitude-twist-flex/scripts/f6tail_momentum_split_flux.mjs` | `5d77ca058adb634547c91998002eeffb9de5395a9e1e130f7edd4fa65014f578` | 原 split 非线性通量、显式线性通量、两个 mean RHS |
| `topics/visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs` | `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3` | `cellFlow`、`evaluate`、`cutJets`、`heightJetJacobian`、原端口除法与 meanHeight |

一般有限轨迹、成功返回及完整求解范围沿 [R411](R411-original64-finite-root-trace-matched-variation-and-full-return.md)。本文只支付零形状这一特殊条件下的局部简化命题，不重做或扩大 R411 的一般结论。

## 470.3 对象、常数与必须保留的现场

设 $M\ge1$，$N$ 为实际角节点数，$J=M+1$，$K_d=2M$。原状态是

$$
y=(Q_0,\ldots,Q_{M-1},\Pi_0,\ldots,\Pi_{M-1},h_1,h_2).
\tag{470.1}
$$

下标 $K_d$ 表示形状维数，角行里的 $K$ 仍是原 $L-P_\theta$，两者不混同。局部 Jacobian 有 $K_d+2$ 行、$K_d$ 列；它没有删除 mean 状态，也没有给 mean 增添未请求的输入方向。

固定当前实际 profile、$x$、几何记录 $g$、`options` 与字面表。在该局部方向中它们不随 $Q,\Pi$ 改变。记 $r=g.r$，$r_x=g.drdx$，$w=g.w$，$w_2=g.w2$，$E=g.E$，$m_j=\mathrm{freq}[j]$，并用 $c_2,c_{12}$ 表示实际表中 `sq2`、`sq12` 的值。这里不把这些已经形成的 binary64 常数重新解释为另一套无限精度输入，也不假设 $w_2=w^2$ 在字面实数意义严格相等。

在 `splitRhsDirection` 的标量前段之后，记其实际系数节点为

$$
\sigma=r_x/r,\qquad
P_*={o\,c_2 r^3 r_x w_2\over c_{12}\mu},\qquad
p_j^*={-m_j r^3\over c_2 w},\qquad
\ell=\mathrm{trace.target\_factor}.
\tag{470.2}
$$

式 (470.2) 指明源码中的原括号及原形成位置。下文的准确实恒等式可在这些系数节点固定之后阅读：原角与装配表达式用实数运算解释。实际 binary64 装配仍须使用原形成值、原括号和原运算顺序；本文没有给它的舍入误差界。

特别地，$\ell$ 必须取实际 tape 中已形成的 `target_factor`，不能在捷径中重算，更不能把 $P_*\ell$ 强行约成 $\sigma$。原 primal 中

```javascript
const f=orientation*sq12*mu/(sq2*g.r**4*g.w2);
```

先形成一个数值词，再由 observer 保留为 `target_factor:f`。`pref` 在另一段独立形成。准确代数上可约的未舍入表达式，不等于已形成词之间已支付了相等关系。

## 470.4 零现场与有限根轨迹的精确前提

对准备简化的**每一次局部调用**，要求如下条件。

1. 原 `dimensions` 和 tape 来源条件已成立；当前状态有 $K_d+2$ 项，实际 root 有 $J$ 项，实际角行与三张字面表的长度均正确。
2. 原 no-J `rootValue` 和 `stateRhs` 已按原顺序真实执行并返回；本命题只消费这个现场，不预先替换它们。
3. 当前全部 $Q_j,\Pi_j$ 是准确零；实际返回的全部 $L_i$ 是准确零。这里数学上允许正零和负零，逐字版本必须另外保存它们的符号。
4. 每个实际角行的 $P,P_\theta,L,K,U$ 均是准确零。原 $D,S,A$ 分支检查已经由 primal 支付，且所用分母与平方根属于原合法分支。
5. `trace.initial_guess_supplied` 为 false；`trace.accepted_updates.length` 为零；它仍等于 `trace.iterations`；`return_reason` 仍是原允许的 `normal-stop` 或 `original-roundoff-fallback`。任何不符均回到原路径，不能根据输入名叫“zero H”推填这些字段。
6. 本地方向的几何、端口与频率固定。需要声明逐字安全时，还要支付第 470.9 节的完整有限中间算术及 signed-zero 条件。

第 4 条不是声称任意数值表都自动给出这些行。对原已形成的现场可直接观察它；若想从输入零推出，则必须沿原全部形成步骤证明有限性及零传播，不能省去该责任。

**引理 470.1（原有限根方向）。** 在上述前提下，原 `finiteRootDirection` 返回

$$
\delta L_0=0,\qquad \delta L_{j+1}=\ell\,\delta\Pi_j,
\quad 0\le j<M.
\tag{470.3}
$$

**证明。** `initialDirection` 先创建长度 $J K_d$ 的零数组，唯一赋值是

```javascript
dL[(j+1)*K+M+j]=trace.target_factor;
```

原函数随后核成功返回与更新数一致，并只在 `accepted_updates` 上迭代。该实际列表为空，故没有调用残差/Gram 方向、Cholesky 方向或 Newton 方向更新，直接返回原初始方向。这是原有限程序的控制流结论，没有解出或替换任何隐式方程。证毕。

原统计 `root_returns`、零更新计数、原 root 评价数及返回直方图仍应由原 `finiteRootDirection` 增加；一个未来捷径不应绕过这个共同入口。

## 470.5 非线性通量的一阶消去与字面表责任

在一个实际角节点，原 `angularPartials` 的实表达为

$$
K=L-P_\theta,\quad
T=2K+K^2+EP^2,\quad u=w_2T,\quad
D=1-u,\quad S=1-w_2P^2,
\tag{470.4}
$$

以及

$$
A_f(P,P_\theta,L)=
{K+u/(1+\sqrt D)+w_2P^2\sqrt D\over S\sqrt D}.
\tag{470.5}
$$

这里 $A_f$ 只是本文给 `factor` 起的局部符号，不能与原 branch 中的 $A=1+L+w_2P_\theta$ 混同。零行处 $K=T=u=0$、$D=S=1$，故

$$
A_f(0,0,0)=0,\qquad
dA_f=(1+w_2)(dL-dP_\theta).
\tag{470.6}
$$

后一式来自分子的一阶项：$dK+du/2=(1+w_2)dK$；分母在零处为 1，而其导数乘分子零，所以不贡献一阶项。$P$ 的一阶项为零。原非线性通量单点值是 $U A_f$，故当实际 $U=0$ 时

$$
d(U A_f)=dU\,A_f+U\,dA_f=0.
\tag{470.7}
$$

式 (470.7) 对每个完整形状方向分别成立。因而原 `df[col]` 的实值为零，每个模态的有限求和

$$
\mathrm{dFlux}_{j,c}
=\sum_{n=0}^{N-1}{\mathrm{df}_{n,c}\,\mathrm{sn}_{n,j}\over N}
=0
\tag{470.8}
$$

对任意实际有限表项成立。

**这一步不使用离散三角恒等式。** 原 `cs`、`sn` 独立由各自调用形成；`gramCos` 也独立形成。即使把这些字面值视为没有任何准确正交关系的任意有限常数，逐角的零乘积仍使 (470.8) 成立。没有接受 root 更新时 `residualAndGramDirection` 不进入，因而其 `gramCos` 方向求和也不进入该局部路径。

与此同时，不能把上述论证用于未分离原 RHS 中的整个 $(1+K)U/(S\sqrt D)$ 通量。那里的线性 $dU$ 本来非零；本文消去的是实际 split 源中已剥离线性项后的 $U A_f$。原线性项仍必须完整装配。

## 470.6 完整局部矩阵与两个 mean

从原 `splitRhsDirection` 最后的两重循环直接代入 (470.3)、(470.8)，在按每模态 $(Q_j,\Pi_j)$ 排列的坐标中，形状块为

$$
B_j=
\begin{pmatrix}
\sigma(m_j^2-4) & \sigma\,c_2w\ell/r^3\\
P_*m_j(m_j^2-1)p_j^* & 4\sigma-P_*m_j^2\ell
\end{pmatrix}.
\tag{470.9}
$$

不同模态之间的实交叉项为零。原数组的排列仍是全部 $Q$ 后接全部 $\Pi$，所以“分块”是一个排列后结构命题，不许可改变输出布局。四个系数应放在原槽

$$
(j,j),\quad(j,M+j),\quad(M+j,j),\quad(M+j,M+j).
\tag{470.10}
$$

原 first mean RHS 是 $r_xwL_0$，由 (470.3) 得其完整形状方向 $r_xw\,\delta L_0=0$。原 second mean RHS 是 $r_xw$，它通常不为零；只是其**形状导数**为零，因为当前几何固定。因此局部形状方向矩阵为

$$
\mathcal A=
\begin{pmatrix}
\text{全部 $M$ 个 $B_j$，按原 $Q/\Pi$ 槽排列}\\
0_{1\times2M}\\
0_{1\times2M}
\end{pmatrix}.
\tag{470.11}
$$

$M=112$ 时仍有全部 226 行、224 列。second mean 的 primal 积分、两 mean 的每步状态、最终两者之和及完整高度/端点责任全部保留。这里没有把两个 mean 状态置零，也没有把它们从 RHS、RK 或结果中删除。

式 (470.9) 只给准确实结构。若将它实施为数值快路径，不能为了看起来更简洁改变原 `linear=-m*L1+(m*m-1)*p1`、`linear+dFlux` 或最终 `pref*m*(...)` 的括号；也不能由未付的 $P_*\ell=\sigma$ 得出 trace-zero、Hamiltonian 或逐字行列式结论。

## 470.7 RK、cusp、完整阶段与端口

原 `geometry_20261115_original64_finite_trace_flow.mjs` 的 `oneOriginalStep` 先完整执行原 no-J 的四次 `field`，保原 `h*a/2` 等表达式及可复用状态缓冲，并先形成 `nextState`，才对四个已复制现场调用 `fromCaptured`。所以可选捷径的最窄位置在每个已完成现场的局部 Jacobian 内；没有必要也不允许为它重跑或提前替代原 root/RHS。

若到达某 RK 子步时，**实际入射 tangent 已具每模态块结构且两个 mean tangent 均为零**，并且该子步的四个现场都满足第 470.4 节，则在准确实层面，原 `linear(A,T)` 和四级 RK 的完整方向传播保持这两个性质。原因是：不同模态互不耦合的线性算子相乘、相加仍互不耦合；两 mean 的局部形状导数为零且其入射 tangent 为零，所以其 tangent 保持零。原阶段初始形状 tangent 为单位阵、两个 mean tangent 为零，故只有沿此前每个子步均满足这些条件时才能归纳使用该结构。若早先的一般子步已经形成混模或非零 mean tangent，仅当前四个零现场不会把既有 tangent 重新变稀疏或清零；仍须完整传播全部继承方向。某一现场不满足前提便使用原一般矩阵，不能从第一次零状态推断整个链。

在浮点实现层面，原 `linear` 仍按完整三循环逐项累加，包括乘零。将完整矩阵乘法另换成小块乘法可能改变舍入顺序或 signed-zero。因此本文建议的最窄切点只跳过已经另证可跳的**角方向形成**，仍保原完整最终装配、原 `linear`、RK 合成、原 cusp `splitIntegrationInterval` 的实际网格与全部 observer 数据。这并不承诺能消除剩余稠密矩阵乘法成本。

原 core 的 `cellFlow` 创建完整 `Float64Array(K+2)` 并从当前阶段输入复制形状，两个 mean 从该新阶段原定义的零开始。返回时

```javascript
out[j] = j<M ? f.state[j] : f.state[j]/c.portRatio;
J[i*K+j] = f.tangent[i*K+j]/(i<M ? 1 : c.portRatio);
meanHeight = f.state[K]+f.state[K+1];
```

这些是原真实行缩放和完整 mean 汇合。端口为同一阶段对各 $\Pi$ 行的对角缩放，因此准确实上不引入模态耦合；实际实现仍须保原除法与完整端口词，不能仅说是二幂而在未核范围里改写。

cut 方向还有单独的 node0 $\Pi$ 端口乘法。原 `cutJets`、`heightJetJacobian` 与末端完整高度响应不由式 (470.9) 自动给出。尤其原高度 Jacobian 会真实调用 plus/minus perturbed `cutJets`；这些输入通常不是零，必须照原路径执行。局部零处结论也不证明全链非共振、graph 可除、QR 正确或任意 H 的末边界条件。

## 470.8 原有限策略与真实调用边界

原 observer 只记已完成的算术与实际控制流，并通过反向替换恢复检查绑定原 root 文本。原 30 次迭代上限、20 档 backtrack、正常停止和 roundoff fallback 没有被本文更改。

即使零更新返回，原函数可能已付的 root 评价、条件判断或失败分支仍是实际调用责任。`finiteRootDirection` 的零更新特例只说明它不进入“对已接受更新求方向”的循环；不说明 primal 没有调用、无需分支检查或可以用一张旧零响应代替当前返回。

若一个未来实现观察到“no supplied guess + 空已接受更新 + 全实际零行”，并验证数值安全，则可在原 `splitRhsDirection` 中选择零通量路径；它仍消费同一次实际 primal 和当前几何。条件不符是**回到原一般算法**，不是新增数学拒收或停止门。资源耗尽则保原资源异常、当前位置及未访责任，不能用已观察的局部特殊结构忽略原时钟。

## 470.9 逐字等价还欠什么：有限中间量与 signed-zero

### 470.9.1 输入有限不足以保证角 AD 中间量有限

原 `angularPartials(v,g,false)` 仍按原正文形成 $T,u,D,S,\sqrt D,fc,gc,q,factor$ 的值及三个方向。即使零现场所有原输入数值有限，某些方向中间量仍可能溢出。例如 $du/dL=2w_2$，有限但足够大的 $w_2$ 可使该中间量溢出；随后原源码中的 `0*Infinity` 可以形成 NaN。原 `df` 和最终 `finiteArray` 因此可能报告失败。

把这些原算术直接替换成“数学上为零”会把原失败变为成功，不能称为同一数值程序。因此安全实现须为**被省去的原全部操作**给出足以排除非有限的真实条件，或在不能确证时走原路径。只检查最后理论块、只检查输入 `Number.isFinite`、或只检查 branch 的 $D,S,A>\mathrm{floor}$ 都不自动足够。

没有接受更新时 Gram/Cholesky 方向正文本来不执行；不需要为不存在的调用添加审查门。需要保留的是本次实际会执行、拟被省去的 `angularPartials`、`dlv/duv`、`dFactor/df` 与求和形成路径的语义。

### 470.9.2 负零与原全矩阵装配

原 `Float64Array` 初始化为正零，随后乘以负的 $r_x$、$\sigma$、系数或表项可能产生负零。原非线性通量从正零累加；在所有中间量有限且每个 `df` 为某种零的前提下，其原 RN 加法给出的最终通量零还须按实际 JavaScript/运行时运算解释，不能省略最终 `linear + dFlux` 而宣称逐字相同。

更直接地，原第一形状行的交叉零会经过 `sigma*(...)`，第一 mean 零行经过 `g.drdx*g.w*dL[col]`。它们的零符号可能与“新建全零矩阵，只填四个块槽”的默认正零不同。故式 (470.11) 只在实数意义把这些项写为零；它没有授权丢失原符号位。

最薄的未来实现可保原最终两重装配循环及两个 mean 行，明确为已证零的通量使用与原求和相同的零，并保原加零位置；但其逐字安全仍必须由针对该实现的源证明给出。本文没有生成这样的实现或词比较记录。

### 470.9.3 不能升级为 IEEE rounding map 的导数

原 kernel 的对象本就是“固定成功有限实轨迹的数值线性化”。一旦将 binary64 舍入看成输入到输出的精确映射，该映射不是本文使用的光滑实程序。零处消去不修复这个区别；原 forced trace 分支邻域、完整 tangent 舍入误差和准确连续解责任仍未付。

## 470.10 最小可接切点与不变责任

仅作后续实现定位，当前不新增运行源：

1. 保 `completeFiniteRootTraceJacobian` 的 `resourceCheck`、`dimensions` 与原 `finiteRootDirection` 全部调用。
2. 在 `splitRhsDirection` 中、原角方向循环之前，根据该调用的实际 tape/状态/全部角行及明确有限算术条件决定是否适用。
3. 适用时只利用 (470.7) 支付原非线性 `dFlux` 的零值；保完整 $226\times224$ 排列、两个 mean 行、原字面系数/括号/最终装配和原 `finiteArray`。不适用时原角循环逐字执行。
4. 保原 `fromCaptured`、原 full `linear`/RK、cusp schedule、port、链/QR、全部 trial、cut/far、FD、fullDN/final/audit 与原 owner 赋值点。
5. 记录每次实际使用条件的计数/来源与不适用的回退原因；不把缺条件当新数学拒绝，不从事后聚合计数重建已经不存在的完整现场。

这给出了可以继续实现的精确局部切点，也明确指出尚未实现的逐字安全部分。本文没有声称运行时间必下降、某次实际195全部现场合格、另一个 finite/continuous 模型已被认证，或完整课题已经完成。

## 470.11 当前已付与未付

已付的是：在声明的实际零现场和固定有限根返回条件下，根方向的原控制流恒等式、非线性通量逐角一阶消去、不依赖字面表正交的完整局部块结构、两个 mean 的正确责任、以及准确实 RK/端口结构传播。

未付的是：新快捷实现、所有被省略浮点中间算术的统一安全证明、逐字 signed-zero 一致、任何实际场/每阶段条件回执、加速量、全链求解接受、数值 tangent 的严格舍入误差、准确连续解及无限尾/闭面最终证书。原科学入口照常运行，本文不成为它们的新前置条件。
