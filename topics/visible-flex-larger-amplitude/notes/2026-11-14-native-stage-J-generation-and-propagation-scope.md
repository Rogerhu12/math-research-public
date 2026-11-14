# 原 native stage J 的生成链、消去位置与传播细分范围

## 结论与证据范围

actual28 的 576 个 $224\times224$ stage Jacobian 来自**解析隐式根导数、有限 Fourier 矩组装、原 RK4 的完整变分传播、原端口行缩放**。它们不是对 shooting 流做实数有限差分，也不是复数步。源码中确有另一份端点 `heightJetJacobian` 对称实差分，但 actual28 在第一次 correction 返回后、任何 trial 之前停止，没有执行最终端点 J 或 audit，不能用那份端点差分解释本批 stage J。

本文只读公开仓库源码、实际原件与已有统计；没有导入数值模块，没有计算新 J、谱、范数、根或流。文件读取时逐项核对实际 `native_intent.json` 的 SHA。本文不是对已保存 J 的严格导数误差证书，也没有为 solver 增设接受门。

实际对象是 [request28](2026-11-14-actual-request28-native-linear-defect.md)：run `43611175099`，source `6bd52b446241be53e8842d4db5a24f9c2069e6e5`，capture result SHA `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`。完整 stage J 原字节 SHA 为 `394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19`。

## 1. 实际后台与不可混淆的源码层次

[实际 ready](public-actions-43611175099-1-nativecorrection/native-correction-capture/native_ready.json.gz)（SHA `1ccf38a6235f67c21d4947ba8147558e994e9df4e44f204a9d53097e070be1d8`）记录：

- `tailJacobian=fourier-root-and-product-moments-v1`；
- `modes=112`、`spacing=2`、`quadrature=2048`；
- `depth=576` 是 shooting stage 数，`physicalDepth=8` 是物理 cell 数；
- `shootingParts=8`、`steps=12`、`cuspAwareFlow=true`；
- 根分支 `projectionFloor=.05`，native 接受容差 `solveTolerance=2e-9`。

下表的 SHA 都是实际输入账中的完整源码 SHA，不用历史注释或当前同名文件猜测后台。`scripts/` 指公开 `topics/visible-flexible-closed-surface/scripts/`；`repro/` 指同课题公开 `repro/source-root/topics/large-amplitude-twist-flex/scripts/`。

| 层 | 冻结文件及关键入口 | SHA256 |
| --- | --- | --- |
| worker 选择与活对象替换 | `scripts/78718-prefix-tail-tangent-fourier-worker.mjs`，`Object.assign(cell.engine,updated)` | `36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a` |
| shooting / 原 stage 保存 | `scripts/78718-tail-tangent-core.mjs`，`cellFlow/evaluate/correction` | `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3` |
| split factory | `scripts/78718-tail-tangent-split.mjs` | `bacb4f2d57d75fa648ae880ef029152263052d6a15030154082732b8a89e1089` |
| 实际完整 root/split/variational engine | `scripts/78718-tail-fourier-root-split-engine.mjs` | `a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372` |
| 隐式根、Gram、分支 | `scripts/78718-tail-fourier-root-momentum.mjs`，`evaluateL/root` | `cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88` |
| 实际 split RHS | `repro/f6tail_momentum_split_flux.mjs`，`rhs` | `5d77ca058adb634547c91998002eeffb9de5395a9e1e130f7edd4fa65014f578` |
| 局部解析导数 | `scripts/78718-tail-fourier-product-jacobian.mjs`，`rhsWithJacobian` | `205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25` |
| 原 RK4 状态和变分 | `scripts/78718-tail-fourier-product-flow.mjs`，`flowStateWithJacobian` | `717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f` |
| 物理段到 shooting 段 | `scripts/950f-tail-subdivision.mjs`，`subdividePhysical` | `e44317579d483147aa7fe73b086aba059695aa0f675b831c178902a2c0cb62e6` |
| cusp 原网格 | `repro/f6tail_cusp_grid.mjs`，`integrationGrid/withCuspAwareRK` | `b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f` |

本课题的 [tail_resumable_engine](../computations/tail_resumable_engine.mjs)（`1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8`）只把原 stable graph factory 接到已冻结共同图，并在已接受 trial 后增加恢复记录。[tail_frozen_worker](../computations/tail_frozen_worker.mjs)（`3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054`）保留原物理数据与上述后台，另在成功返回后替换指定端点导数行。

M112 的内存容量适配器只把三个 constructor 的 64 上限改为 112；[实际 capacity 账](public-actions-43611175099-1-nativecorrection/native-correction-capture/native_capacity.json)记录 Fourier root 的加载后 SHA `612986f68c0cc493de4430dd244d95df9c014630666cc6d0d55a285fa6d0026b`，没有改根容差、RHS 或导数公式。适配器自身 SHA 为 `07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395`。

[实际 core instrumentation](public-actions-43611175099-1-nativecorrection/native-correction-capture/core-instrumentation.json)绑定原 core `ac2fc999…`、原加载时文本 `f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f`、只插入观察器后的文本 `7a3eee7e26167cf63014d7e9d1f0cc0ca0ca8408a331d5d2e81288db3bad3954`，并记录逐字删除插入后可逆。capture launcher/hook 分别是 `0b49f14218e4d62f0b18d77dd3fa8aee1cb6225f84d92bb81dace173cf74dcc0`、`b20aee4da9b9dd927a2d78c6691739508798c81e73501b31e14a43ad55b64d30`。所以这里分析的是实际捕获那一次的算术链。

## 2. 局部根与解析导数：已有小量改写及剩余相减

记频率 $m_j=2(j+1)$，形状状态 $y=(Q,\Pi)$，$M=112$；根变量 $L$ 有 $M+1$ 个正交余弦系数。冻结 profile 给出 $r,r_x,w$，且 $w^2=\exp(2\log w)$、$E=1+w^2$。源码的目标系数为

$$
t=\frac{\sqrt{12}\,\mu}{\sqrt2\,r^4w^2},\qquad
L+q(L,Q)=t\,(0,\Pi).
$$

这里使用实际 `orientation=+1`。$q$ 是 N2048 的原离散角投影。`root` 从目标或显式 guess 开始，最多30次 Newton；它比较 `moments-target`，接受相对阈值 `8e-14`，原 roundoff fallback 为 `5e-12`。相对尺度是 `max(1e-300,maxQuad,max|target|)`，并非把小 H 以某个绝对门槛归零。

逐角的量包括

$$
K=L(\theta)-P_\theta,\quad
u=w^2(2K+K^2+EP^2),\quad D=1-u,\quad S=1-w^2P^2,
\quad A_{\rm guard}=1+L(\theta)+w^2P_\theta.
$$

根守卫要求 $D,S,A_{\rm guard}>.05$。根 Gram 在实数表达中是余弦基下 $A_{\rm guard}D^{-3/2}$ 的乘法矩阵。实际实现先放**精确单位阵**，只投影

$$
b_m=(L+w^2P_\theta)
 +(1+L+w^2P_\theta)\operatorname{expm1}
       \bigl(-\tfrac32\operatorname{log1p}(-u)\bigr)
 =A_{\rm guard}D^{-3/2}-1.
$$

这避免直接把两个约为1的数相减来得到小的非线性 Gram 修正。`q` 还使用 $u/(1+\sqrt D)$、有理化的 `fc/gc` 等公式；split RHS 将已知线性角通量显式提取，只对非线性余项求和。这些改写已经在 actual28 的冻结源码中，不能当作尚未实施的新修复。

局部 Jacobian 使用同一次 `base.root`，由六组离散矩 `FPm, FTm, CKm, CUm, CPm, bmM` 组装右端和投影项。所有列共用一次 $113\times113$ Cholesky，求解224个右端；没有 `F(y+h)-F(y-h)` 或除以扰动高度的步骤。

尤其，对动量列，源码的 `dL` **只保存非线性修正导数**。令 $B=I+C$ 为根 Gram，则其右端为 $-tCe_j$，而完整导数为

$$
\partial_{\Pi_j}L=t e_j+dL_j,
\qquad BdL_j=-tCe_j.
$$

所以它没有先计算 $B^{-1}te_j$ 再减 $te_j$ 来提取小差。源码的 `right[...,M+j]=-targetFac*CC(bmM,...,j+1)` 与 Q 行中另加 `targetFac` 正是这项分离。动量行也把 $4\gamma-m_j^2\gamma$ 预合成 $(4-m_j^2)\gamma$，其中 $\gamma=r_x/r$。

仍实际存在、但尚未定量归因的舍入／相消位置是：

1. 原变量 $K=L-P_\theta$，以及 $U$ 中 $-m_jL_j+(m_j^2-1)p_j$ 的相加。
2. 根残差 `(L+quad)-target`；极小非线性项可能小于 `L` 的 ulp。隐式导数是根方程的解析导数在返回近似根处的计算值，不是对 Newton 停止分支逐条做自动微分。
3. 六组角矩的2048项普通顺序求和，及乘积恒等式中的 `SS(v,i,j)=v[abs(i-j)]-v[i+j]`；`FL=ck-f*cu`、`FQ` 和最终 `df` 还有带符号求和。
4. Cholesky 与三角代回中的 `v-=L*L`、`v-=L*X`。正分支和成功分解不自动给出前向误差界。
5. 正弦余弦表由 `Math.sin/cos` 计算。product-to-sum 是精确三角恒等式，但不同源码对角度乘法的括号次序不同，分别舍入的表不满足逐位精确的乘积恒等式。本文没有为该差异给出未计算的上界。

因此，解析组装消除了“对 tiny H 做差分商”的误差机制，却没有消除一切浮点相消。要量化局部导数误差，还需要同一返回根、原基表、原几何及各投影／线性解的实际误差证据。

在精确零形状参考 $Q=\Pi=0$ 上，根为 $L=0$，六组非线性矩全零、$B=I$。局部形状块按频率独立，实数公式为

$$
\begin{pmatrix}
(m^2-4)r_x/r & \sqrt{12}\,\mu r_x/(r^8w)\\
-m^2(m^2-1)r_xr^6w/(\sqrt{12}\,\mu)&-(m^2-4)r_x/r
\end{pmatrix}.
$$

这个源码恒等式解释了局部频率二次／四次因子和坐标尺度；它没有将 actual28 的非零 H、非零状态或完整非对角 J 替换成零态。actual28 的所有112个 H 分量都非零，已保存最大绝对 H 是 `4.1760413061806626e-17`；小物理高度本身不能控制沿全尾的归一化根变量或变分传播增益。

## 3. stage J 是整段原 RK4 的传播导数

`flowStateWithJacobian` 把 $T$ 初始化为形状坐标上的单位阵。每个 RK 点调用上一节的局部解析矩阵 $\mathcal J$，然后按原循环做

$$
\dot y=f(y,x),\qquad \dot T=\mathcal J(y,x)T.
$$

状态和变分都用同一四阶段 RK4 更新，具体中间状态、$x$、$h$、profile 和 cusp 网格保持一致。代码是普通 binary64 标量乘加循环，没有正交化、QR、对数幅度或稳定子空间分离；也没有使用带误差界的乘加。额外两个均值积分状态不反馈形状 RHS，故变分列只有224个，最后取前224行成为形状 J。

`cellFlow(n,states[n+1],true)` 调用该传播，再把输出动量行以及对应 tangent 行除以实际 `c.portRatio`。这得到保存的 $J_n$，方向是**输入节点 $n+1$ 到输出节点 $n$**。stage 残差是 `flow(states[n+1])-states[n]`，不是反向矩阵求逆。

若局部隐式根精确、使用精确算术和相同 RK 节点，则这种变分 RK 是相应离散 RK 映射的链式导数。实际保存值额外包含返回根误差、局部组装舍入、RK 状态误差及变分矩阵乘加舍入；它不是“原连续 ODE 的精确流导数”，也不是字面 IEEE 分支程序的经典微分证书。

原 J 的最大保存绝对条目是 `1.0007950021979336e29`，其已核原字节位置为 stage58、row223、column111，即 Pi112 对 Q112。它是这些**整段传播后、在 Q/Pi 坐标中的条目**，不是某一点局部导数，也不是条件数、奇异值或误差估计。如此大的条目可以与真实有限段增益、坐标尺度、RK 稳定性及传播舍入同时有关；现有统计没有分解它们。

高增益传播可能让同一 binary64 矩阵中的收缩方向无法可靠分辨，这与之后 Riccati 图或全带求解的误差层次不同。本文没有据 `chartCondition` 或这一个条目宣布该机制已在 actual28 定量成立。

## 4. stage43 与 stage58 的实际坐标和步数

[原 live layout](public-actions-43611175099-1-nativecorrection/native-correction-capture/original-live-identity-before-seed.json) SHA `de9bbf01981f1605c0342817ea520005bf2d0a05f5a755986d50b718b16089a7`，给出 raw-node 索引 `0,72,144,216,288,360,432,504,576`。每个物理 cell 有9个原 profile，每个 profile 分8份。`subdividePhysical` 在 cell 内按原 segment 和 part 的**逆序**登记 shooting 节点，但每个 stage 自身从其局部 $x=0$ 向 $x=1$ 积分。

| 实际索引 | 原物理位置 | part 与原 profile 参数 | 原 withJac 子步 | 端口 |
| --- | --- | --- | --- | --- |
| stage43 | rawCell0 / rawSegment3 | part4，原参数 $[4/8,5/8]$ | 12个 RK4 步、48次局部根／J 点；无附加 cusp 点 | `portRatio=1` |
| stage58 | rawCell0 / rawSegment1 | part5，原参数 $[5/8,6/8]$ | 12个 RK4 步、48次局部根／J 点；无附加 cusp 点 | `portRatio=1` |

两者实际 `mu=1.0048110027994864e-11`，live `profiles=[[]]`。这表示各有一个子 profile，且其 `integrationBreakpoints` 为空，不表示没有 profile 或没有积分步。

子 profile 是 $g(a+(b-a)x)$，其 `drdx` 与 `dlogwdx` 同乘 $b-a=1/8$。stage 的局部实参数长度为1，原 profile 参数长度为 $1/8$，每个普通 RK 步对应原参数长度 $1/96$。这不是物理半径或弧长 $1/96$；物理径向跨度还要由冻结 profile 的端点半径给出，本文没有新增求值。withJac 普通网格的字面次序是 `h=1/12, x=n*h`；no-J 原循环使用 `x=k/steps`，不能未经检查宣称两种浮点生成方式逐位相同。

stage43 的原已报告最坏 correction 缺陷是 Pi110 行（频率220）；stage58 是全 J 最大条目的位置；actual25 的 trial guard 失败在 stage13/raw0/seg7。三者各是明确的统计／方程标签，不能因都属于 rawCell0 就混称为同一个 RK 点或同一个故障。

## 5. 同保存 A 的求解缺陷、J 表示误差、连续流误差分别处理

[actual34](2026-11-14-actual-request34-native-band-exact-defect.md) 用原 J 改走带分解后，stage43/Pi110 的保存数组精确原尺度缺陷仍约 `5.2938027944720596975662930805088451e30`。这是完整范数的一个严格下界，足以说明该方向对**这些保存的有限线性方程**也没有解好。它不需要先判断 J 是否忠实于原数学导数。

同时，换求解器不能修复已经包含在 J 字节中的误差。按 [R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md)，若 $\widehat A,\widehat r$ 是保存数组而 $R,DR$ 是所选数学参考残差及导数，则

$$
R+DR\,\delta
=(\widehat r+\widehat A\delta)
 +(R-\widehat r)+(DR-\widehat A)\delta.
$$

三项不可混用。第一个括号可以由精确 dyadic 读回完整决定；最后一项需要导数误差证据，特别是实际方向可能放大 J 的小绝对误差。即使第一个括号很小，也仍须走原 nonlinear trial；反之，它已巨大时不应仅凭局部图条件数给出唯一归因。

因此当前对**同一保存 A**做幂二行列均衡、单次缩放和精确原方程误差修正是有实际依据的下一步。只要缩放没有下溢／溢出／损位，幂二直接缩放可精确表示；实际形成损失和坐标恢复损失仍须按原字节报告。误差修正右端应来自 $-e$ 的精确 dyadic 值再一次正确舍入，最终仍回原 $\sigma$ 比较。这不证明 J 的导数精度，不声称双精度带分解一定足够。

若后来要提高局部根／投影／传播精度，必须分别绑定新源、新精度、同一冻结几何与原节点；那会生成一份新 J，不能继续冒作 actual28 的 `394ca2cc…`。只提高线性求解或残差精度则可以继续保留这份 A 的身份。两种工作回答的问题不同。

## 6. 有因的最小传播细分：先区分分组与加密

在当前已定位的两个无 cusp 段上，一个更小的后继是把**原12个 RK 步按原次序分成6+6**，增加一个 shooting 节点；先不增加 ODE 步数，不改变原角模式或根公式。必须保留原 profile 对象及逐步原 $x,h$ 字节，不能把重新参数化后“实数上相等”的调用直接当作同一浮点程序。

设原步映射依次为 $\Phi_1,\ldots,\Phi_{12}$。新约束使用

$$
z=\Phi_6\circ\cdots\circ\Phi_1(y_{\rm in}),
\qquad
y_{\rm out}=\Phi_{12}\circ\cdots\circ\Phi_7(z).
$$

在精确算术下消去 $z$ 就是原离散 RK12 映射；每块变分从单位阵重新开始，完整 multiple-shooting 系统不必先把两块乘成可能极大或丢失收缩信息的长传播矩阵。这只是可验证的结构理由，尚未证明本例的短块有足够精度，也未计算任何改善。

现成 `shootingParts` 变更会重参数化 profile、改变默认积分次数和共享图网格，故不是以上逐步同序分组的现成证明。最小独立实现需要明确保全：

- 全112个原 H 的字节、原 cut 半径、冻结 profile/calibration、原 N2048、原 root guards/tolerances、原 far graph 向量及原 raw-depth 截断；
- 原 stage 到新 stage / node 的对应表，逐步原 profile 身份和 $x,h$；原 portRatio 只在原出口执行一次，新增内部端口为1；
- 保留全部旧节点原字节，以原入端进行原 schedule 的短段传播来填新增初猜节点；初猜不冒接受解，原出端残差不被覆盖；
- 原与新尺度账分别明确。不能悄悄用新 gains 生成的 scaleFor 代称原 $\sigma$；对限制到旧节点的结果保留原坐标、原 far/cut、原尺度 readback。若新系统内尺度改变，必须明示，原 native tolerance 与完整实际 trial/验收不放宽；
- 新短块 J 的各自身份、同一基轨道上的组成关系、真实 nonlinear trial 及完整结果。它们不再是原576个 J 的相同字节，也不应把新系统的低残差等同于原连续流精度。

上述组合恒等式首先针对224维形状状态。两个均值积分不反馈形状，但原 `cellFlow` 每次从零开始累积均值，最终 `meanHeightToCut` 又跨 stage 求和；新增 stage 会改变这层加法括号。完整响应必须记录两半的均值及原合并规则，不能只凭形状组合就声称绝对高度／均值的 binary64 字节也一致。

真正把原12步加密到更多步是另一项改变：它保持原连续 ODE/metric/H/far，但改变离散流截断误差，需要同原坐标下的实际比较。先分组、再视真实读回决定是否加密，可以区分“保存长传播矩阵的表示问题”与“原 RK 步长问题”，不用在缺少证据时预先把两者合并。

## 7. 端点差分的确切位置

原 core 的 `heightJetJacobian` 先由 stage J 反向传递 tangent graph，再沿该图对 `cutJets(plus/minus)` 做中心实差分，默认相对步 `1e-4`。成功返回后的 [numerical-tail-slope-jacobian](../computations/numerical-tail-slope-jacobian.mjs)（SHA `206d82d3b41e6b9ce24b26447a2026c19c1c7126765107c23d58e55da25639e2`）以解析 cut chain 替换 slope 和 mean-slope correction 行；second、mean-second 与 height 行仍有原差分来源的明确记录。

这层最终响应确有独立的切向图和差分精度问题。actual28 的 `capture-begin` 明确 `final_endpoint_J_or_audit_computed=false`，所以它没有参与已保存 stage J 的生成或本次 correction。将来原 Newton 成功后，对完整 DN sensitivity 的线性求解是否也需使用稳定的全系统后端，应依据那时的真实响应另行处理，不能把 ready 的线性图或这次失败方向冒成已经验证的 DN 导数。

