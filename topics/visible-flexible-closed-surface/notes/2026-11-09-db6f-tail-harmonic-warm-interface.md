# 外部逐模 harmonic warm 的最小接口：仅初猜、尚未生成

日期：2026-11-09。作者：`/root/tail_theory`。

状态：只读接口方案。没有生成候选 checkpoint、配置、变换程序或启动命令；没有计算任何变换后的 state 数组，没有调用 root、flow、RK、Jacobian、求解或认证后端。当前 continuation 的活跃请求不变、不停止。本稿不给出新初猜的残差、正性或收敛保证。

## 1. 目的与已读闭合来源

备用思路是在另一个独立运行中，把最近成功的同模数、同网格 finite DN 状态按存储模态逐模乘幂，再交给**原 worker**。它只改变初猜，原 moment 方程、RK、shooting 残差、cut/Robin 边值、guard、tol 和最终验收均保持原样。

本次只读核查使用已关闭的 continuation02 call 9（$s_0=13/16$）：

- 文件：`2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02_tail_0009.json.gz`；SHA-256 `78d7e112d4823a717d0f46549b9f88d11872dbe390f40f70d295278ed50320e8`。
- 原响应 `converged=true`，残差 $3.796278258536727\times10^{-10}<2\times10^{-9}$；请求为 `jacobian=false, audit=false`。这是已成功的有限 DN warm，**没有**完整 prefix 联解或几何认证。
- 同名 call009 的 root 闭合审计 SHA-256 `8ae901094b155204c4ead255fd8222290d45ac6e7e4124f0f19832b076c6b12b`。
- 实际保存 `states` 为 $865\times30$，全数值有限且不是 bool；`rawNode` 有 13 个整数，逐项为 $72n$；`rawStates` 为 $13\times30$ 且逐值等于 `states[rawNode[n]]`。
- `checkpoint.cutHeight` 与原 `request.height` 逐值相同，长度 15；保存的实际 `response.jets.height` 则是另一个字段，不能将二者语义混用。

源码、配置、固定 affine 目标及闭合响应的来源绑定列于同名 `-sources.json`。本稿没有查看当前活跃请求的 state 或 trace。将来若选择另一个 last-success，必须重新绑定它并重复这些只读门；本稿的 call9 观测不能自动替它作证。

## 2. 坐标与原生数值参数

状态每行的前 15 项是 $Q_j$，后 15 项是保存坐标 $\Pi_j$。数学下标 $j=1,\ldots,15$ 对应 JSON 下标 $j-1$；实际 Fourier 频率是 $3j$。**缩放指数是 $j$，不是 $3j$。**

保存的 $\Pi$ 已有原 shooting 节点的 momentum normalization。原 `cutJets` 临时乘 $\rho_0=2^a$ 后再调用 root；本变换应直接对保存的 $Q_j,\Pi_j$ 乘同一个因子，不新增或消去这次 gauge。因子对同一模的两半都相同，所以它与固定的 momentum gauge 乘法相容。

当前已关闭源的必要数值定义为：

| 字段 | 保存 checkpoint | 原配置或含义 |
|---|---:|---|
| `modes` | 15 | 15 |
| `spacing` | 3 | 3 |
| `physicalDepth` | 12 | 配置 `depth=12` |
| `depth` | 864 | shooting stage 数，不是配置的 raw depth |
| `shootingParts` | 8 | 每 raw profile 分 8 段 |
| `steps` | 32 | 每 stage 原生 RK 步数 |
| `quadrature` | 256 | 原 moment 角求积 |
| `projectionFloor` | 0.05 | 配置无覆盖，原 core 默认值 0.05 |
| `linearFar`, `linearSteps` | 32、256 | 两者均保留 |
| `linearMethod` | `stable-momentum-cusp-subdivision` | 原配置为 `projective`，该保存标签由原 core 派生 |
| `solveTolerance` | $2\times10^{-9}$ | 原值 |
| `rhsEvaluation` | `split-linear-flux-v1` | 原 split 包装派生 |

原配置的 `maxIterations=36`、所有 cusp/engine 配置保持不变。不能为“参数相等”把配置 `depth=12` 改写成 864，或把派生 `linearMethod` 标签反写进原配置。物理参数及原生数值设置均由同一冻结源码和配置复用，不能只比较上述小表而忽略其余定义。

## 3. 拟议变换的精确定义

设选择一个 $0<s_0<s_1\le1$。先核旧闭合请求逐值等于原 controller 对固定目标 $h^*$ 的 $h(s_0)$，随后**独立沿用原 controller 公式**生成新请求标签

$$
h_j(s_1)=s_1^jh_j^*,\qquad j=1,\ldots,15.
\tag{1}
$$

若 $s_1=1$，使用原 `goal.copy()` 分支，而不是累计乘比例。此标签是物理高度，不额外乘或除 $c^4$；不能用旧 `jets.height`、旧请求累计乘幂、或变换后节点反推值替代固定路径的 (1)。

实算术中拟议因子与状态为

$$
\gamma_j=(s_1/s_0)^j,\qquad
\widetilde Q_{n,j}=\gamma_j Q_{n,j},\qquad
\widetilde\Pi_{n,j}=\gamma_j\Pi_{n,j},
\quad n=0,\ldots,864.
\tag{2}
$$

未来若实现，建议把 binary64 运算规则固定为：先按 NumPy binary64 计算一次 `s1/s0`，以 `np.arange(1,M+1)` 计算一次 15 个幂因子；每个因子复用于全部节点的该模 $Q$ 与 $\Pi$。逐项乘法使用 binary64，最后独立检查所有结果 finite、因子正且 finite。报告准确记录该规则；不要声称它与对每个模分别计算 `hnew/hold` 逐位相同。任何非有限结果直接拒绝，不能夹值或改 floor。本稿尚未运行这些乘法或生成因子数组/新 state。

`rawNode` 原样复制；`rawStates` 必须从**已经生成的同一份** `states` 按 `rawNode` 重取，不能另外乘旧 raw 数组而留下不同舍入或索引路径。预备器应拒绝不为 $865\times30$、不是 $13$ 个合法节点索引、旧 raw 数据与索引不一致等输入。

原深端 Robin 关系是逐模线性的。因此在理想实算术中，同模的两半同乘 $\gamma_j$ 使原深端残差也同乘 $\gamma_j$；这不支付非线性 stage matching。归一化 moment root 是 nonlinear map，物理 slope、second jets 和实际曲率不能按 (2) 缩放。

## 4. 新记录的最小 schema；严禁复制旧响应外壳

未来应从空白对象构造新记录，采用顶层 `checkpoint` 分支。下表是 schema 说明，**不是已生成的候选 JSON**。

| 路径 | 类型、内容与语义 |
|---|---|
| `status` | 字符串 `UNSOLVED_HARMONIC_WARM_ONLY` |
| `preparation_only` | JSON `true` |
| `actual_solver_runs` | 整数 0 |
| `source_checkpoint` / `source_checkpoint_sha256` | 已关闭真实成功响应的路径和文件哈希，仅 provenance |
| `source_target_prefix` / `source_target_prefix_sha256` | 固定 affine 目标路径和哈希 |
| `source_scale` / `target_scale` | 本次准确 $s_0,s_1$ |
| `transformation` | 明记 (2) 的模索引、binary64 规则、保存 $Q/\Pi$ 两半同因子；无 root/flow |
| `checkpoint.parameters` | **完整复制源 checkpoint 的参数对象**，不改变物理/原生数值定义；其中旧 I/O 文本只属源记录，不是新运行配置 |
| `checkpoint.states` | 未来按 (2) 生成的 $865\times30$ 有限数值数组 |
| `checkpoint.rawNode` | 源的 13 个整数索引原样复制 |
| `checkpoint.rawStates` | 从新 `states` 逐索引重取的 $13\times30$ 数组 |
| `checkpoint.cutHeight` | 长度 15 的**新请求目标标签** (1)，不冒称已测的新节点实际高度 |
| `checkpoint.scope` | 明记 UNSOLVED、仅初猜、新目标标签与当前 state 边界可能不同、旧 jet/Jac/audit 失效 |

顶层必须**没有** `response`、`seam`、旧 `request` 或旧 response 的其他字段。原因不仅是诚实性：worker 的解析优先级为 `record.response?.checkpoint`、`record.seam?.tail_checkpoint`、`record.checkpoint`、裸对象；保留旧外壳可能使它误选旧 checkpoint。原 runner 也优先选择 `response.checkpoint`。

以下旧结果一律不复制进新候选记录，也不以乘法更新：

- `converged`、`residual`、`history`、`lastIteration` 及任何成功/认证状态；
- 整个 `jets`（包括 height、slope、second、mean corrections、`minLeading`、`minD`、formal curvature 等），`cutRaw`、mean height 结果；
- `heightJetJacobian`、`graphJacobian`、linearized flow Jacobians、Newton 修正或 chartCondition；
- `audit`、metric/fullD/curvature/holonomy 数字及旧几何证书。

即使若干几何背景字段不受此变换影响，也不要在新记录中保留混合了无效 nonlinear jets 的旧 `jets` 对象。只保留源文件哈希，使读者能查看来源；不能让旧 `converged=true` 冒充新 state 已解。旧文件不改名覆盖，新文件使用独立 stem、禁止覆盖写入，gzip 且小于 5MB，保存压缩文件哈希。实际审计和 source map 的来源绑定应独立明确，不把旧 response 的来源字段伪装成新程序已运行的证据。

## 5. 原 loader、remesh 和边界修正为何兼容

### 5.1 loader 接受明确 UNSOLVED 初猜

原 trial worker 的 initial checkpoint 门只要求 `parameters`、`states`、`cutHeight` 及参数相容；它并未要求 `converged=true`。原 trial runner 同样只要求这些字段及固定 modes/steps/quadrature/spacing。因而上述顶层 `checkpoint` schema 可作为明确未解的初猜输入；无须伪造 `response` 或成功状态。

但这个容许初猜的门不是完整数据验证器。未来预备器仍须主动核长度、finite 非 bool 数值、整数索引、raw 对应、同 g/原生参数、已关闭成功来源、源哈希和准确固定路径目标，不能把“loader 没拒绝”写成有效性证明。

### 5.2 同模、同 p8/d12 网格的 remesh 只复制节点

此处 $M$、physical depth 和 shootingParts 均保持不变。`remeshCheckpoint` 在旧/new parts 相等时，对每个 stage 的 `rawLeft=k/8` 计算 $z=8\,\mathrm{rawLeft}=k$。因为这些坐标为精确 dyadic，`nearest=k` 分支直接 copy 原节点，不进入额外 RK 插值。

若每 raw cell 有 $J=9$ 个 profile，该 stage 的旧节点索引公式为

$$
\mathrm{oldRaw}[n]+(J-1-j)8+8-k,
$$

恰等于对应的新节点索引；raw 端点另直接复制。物理深度没有增加，末尾线性补深循环为空。因此全部 $865$ 节点仅逐项装载新数值，不需要 raw lift、变模或重求流。源码确实会构造 engine 闭包；这里“无 RK 插值”不等于声称未来完整 worker 启动不调用任何 root。其原 startup/真实求解会照常执行。

### 5.3 使用新目标标签，避免二次缩放

worker 初次载入时以 `prior.cutHeight` 设置内部 `last.jets.height` 标签，之后按新请求首模除此标签首模得到 warm ratio。若把 `checkpoint.cutHeight` 写成新的 (1)，并对原 worker 发送同一个 (1)，该比例严格为 1（有限非零同一 binary64 数除自身）。因此它不会再次把 (2) 整体乘一个首模比例。

随后的原默认 `correctInitialBoundary!==false` 计算

$$
\Delta_j=h_j(s_1)/c^4-\widetilde Q_{0,j}
$$

并用原线性 shooting 初猜响应补偿。因此实际进入原 solve 的初猜，在实算术表示下为

$$
y_n^{\rm init}=\widetilde y_n+\mathcal L_n(\Delta).
\tag{3}
$$

这个修正付掉旧 cut 残差和独立计算目标时的差异；不得禁用它，也不自行调用 `cutJets` 来构造一个貌似已审的初猜响应。源 `cutJets` 的 height 是 $c^4Q_0$；两端保持同一固定 $c$，所以 (2) 不需要额外 $c^4$ 换算。`cutHeight` 作为请求标签的语义必须在 scope 中公开，正如原失败/未收敛 checkpoint 一样。

若反而保留旧 $h(s_0)$ 标签，worker 将再乘近似 $s_1/s_0$，通常变成第 $j$ 模多乘一个首模比，然后再修边界；那已不是本稿提议的初猜。因此不能这样实现。

## 6. 仅未来可执行的最小运行入口与禁止项

若以后获得明确实施指令，可以用已审原 `db6f-prefix-tail-trial-run.py`，输入上述新 warm 与原 continuation02 配置。它会为一个**新的独立输出 stem**设置 `initialCheckpoint` 和 trace/iteration/trial 路径；`--max-iterations` 必须显式给原值 36，避免 runner 缺省 2 意外缩短预算。原 `solveTolerance=2e-9`、floor 0.05、所有原生数值参数不改，`correctInitialBoundary` 仍保持未设置，不引用零态 pilot 的 false 配置。该 runner 的真实请求为 `jacobian=true,audit=false`；这不是完整 final audit 或 prefix 联解。

本稿没有生成这个命令或运行文件。未来 launch 清单还应固定实际运行源码、配置、输入和输出路径哈希；启动前重核本方案与来源没有变化。

**不能**直接把 UNSOLVED warm 交给原 continuation controller 的 `--resume-checkpoint`。该入口明确要求闭合响应 `response.converged` 且残差低于原 tol、旧请求逐位对应给定 $s$；为了让它接受而伪造成功响应是错误的。必须先由原 worker 真实求得成功响应，才能按原恢复规则讨论继续。原 controller 还要求 $0<s_{\rm resume}<1$；若独立目标正好为 1，成功后需按原最终 DN audit/完整 prefix 流程处理，不能伪造 controller 的 target-audited 标志。

## 7. 可以和不可以据此声称什么

可以声称：在上述固定维数/坐标/参数和明确标签语义下，这是一种能够被原 loader 读取、仍由原边界修正与原 nonlinear shooting 验收的外部初猜。变换本身不改变 $g$ 或待求边值方程，所有旧成功证据仍仅属于旧记录。

不能声称：这种初猜比当前 uniform+linear predictor 更好，新的 root 满足 guard，残差下降，原 solve 必成功，或任何 M15 closed surface 已完成。shape 高模依赖非线性 root，(2) 没有 positivity 保证。当前 continuation 已经具有自己的自然 rollback 路径；本方案不修改、抢占或停止该活跃过程。
