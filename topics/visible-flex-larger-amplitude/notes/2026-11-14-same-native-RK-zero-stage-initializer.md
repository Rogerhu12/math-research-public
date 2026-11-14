# 2026-11-14：保持原尾方程的同 RK 零态初猜接口

状态：**源码推导与独立初猜模块已完成；尚未执行数值**。本接口不是一次新的 native DN 成功。原 cold-residual probe 现已实际完成，见[全stage回执](2026-11-14-actual-cold-tail-no-J-stage-replay.md)：初值身份相等、最坏stage11、两端条件为零；本模块是否改善内部残差仍须自己的Actions。模块为 [geometry_20261114_zero_rk_stage_initializer.mjs](../computations/geometry_20261114_zero_rk_stage_initializer.mjs)。

本次只读来源为原公开仓库的：

- topics/visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs；
- 同目录 78718-prefix-tail-tangent-fourier-worker.mjs、78718-tail-tangent-predictor.mjs、950f-tail-subdivision.mjs；
- 同目录 78718-tail-fourier-product-jacobian.mjs、78718-tail-fourier-product-flow.mjs、78718-tail-fourier-root-split-engine.mjs；
- repro/source-root/topics/large-amplitude-twist-flex/scripts 下的 general_root_tail_momentum.mjs、f6tail_momentum_split_flux.mjs、f6tail_cusp_grid.mjs；
- 本题 closure_linear_stage_graphs.mjs、tail_resumable_engine.mjs 及 exact_20261114_seeded_zero_tail_client.py。

仅用小文件 git show / 本地读源，没有扩大检出，也没有运行这些构造器。

## 1. 当前三套步数的精确对应

本次 request17 的真实配置保留：

| 项目 | 原配置值及其作用 |
|---|---|
| modes / quadrature / spacing | 112 / 2048 / 2，全部保留 |
| physical depth / shootingParts | 8 / 8，实际 576 个 stage、577 个 shooting 节点 |
| linearFar | 48，决定原 deep linear boundary 的构造终点 |
| linearSteps | 2048；deep 未细分物理 cell 的每个 profile 用 2048 步 |
| 有限 stages 的线性图步数 | max(8,ceil(linearSteps/shootingParts))=256，每个 stage profile |
| steps | 12，实际有限非线性 cellFlow 每个 stage profile 的 RK4 步数 |
| auditSteps | 12，只供原实际 audit 使用，不能代替求解步数 |
| solveTolerance / maxIterations | 2e-9 / 32，初猜器不改动 |
| cuspAwareFlow | true；实际 profile 的 integrationBreakpoints 仍参加原 RK 网格 |

subdividePhysical 依次遍历物理 cell；每个原 profile 按逆 segment 顺序及逆 part 顺序生成 stage。stage 的局部坐标增加方向是原 cellFlow 从深侧 shooting 状态到浅侧输出的方向。通常每 stage 只有一个重新参数化的 profile；模块仍完整遍历 live stage.profiles。

**不能全局改 linearSteps 来声称“只改初猜”。** 原 core 中：

1. graphs[depth] 进入实际远端方程
   $\pi_{\mathrm{deep}}-G_{\mathrm{deep}}Q_{\mathrm{deep}}=0$，
   也进入 Newton correction 和 full tangent predictor 的远端矩阵；
2. gains[n][0] 决定原残差尺度
   $\mathrm{scale}_{n+1}=\mathrm{scale}_n/|\mathrm{gain}_{n,0}|$；
3. 内部 graphs/gains 同时供原 cold initial 使用。

新模块因此一项也不改。它只保存私有 candidateGraphs 和 transferDenominators，最后把完整节点数组作为原 solve 的 initial 选项传入。

## 2. 原有限 RHS 在精确 zero 上确为逐模线性化

这不是理想圆的替代方程。原有限 momentum 状态的 shape 分量是

$$
(Q_1,\ldots,Q_M,\pi_1,\ldots,\pi_M),
$$

还有两列由原 RHS 积分的均值高度；shape RHS 不依赖这两列的已有值。在精确 $Q=\pi=0$ 时：

- 原 momentum root 的 target、$L$、$P,P_\theta,K,U$ 全为零，$S=D=A=1$；
- 原 Fourier-product Jacobian 的六组 nonlinear moment、right 及 correction dL 均逐项为零；
- 显式 split linear flux 保留完整频率，不通过一个可能有正交求积舍入的稠密 Gram 近似线性部分；
- mean correction 行对 shape 的导数为零；纯背景 mean 行也不依赖 shape。

因此对每个频率 $m=\mathrm{spacing}(j+1)$，在 orientation=+1 下，shape 线性化严格分解为

$$
\frac{d}{dx}
\begin{pmatrix}Q_j\\ \pi_j\end{pmatrix}
=
\begin{pmatrix} d_m&A\\B_m&-d_m\end{pmatrix}
\begin{pmatrix}Q_j\\ \pi_j\end{pmatrix},
$$

其中同一原 profile 的量为

$$
d_m=(m^2-4)\frac{r_x}{r},\qquad
A=\frac{\sqrt{12}\,\mu\,r_x}{r^8w},\qquad
B_m=-\frac{m^2(m^2-1)r_xr^6w}{\sqrt{12}\,\mu}.
$$

**直接推导。** 原 root 在零态的一阶项是

$$
\delta L_{j+1}
=\frac{\sqrt{12}\mu}{\sqrt2\,r^4w^2}\delta\pi_j,
\qquad \delta L_0=0.
$$

将其代入原 split RHS 中

$$
Q'_j=\frac{r_x}r
\left[(m^2-4)Q_j+\frac{\sqrt2w}{r^3}L_{j+1}\right],
$$

及

$$
\pi'_j=4\frac{r_x}r\pi_j+
\frac{\sqrt2 r^3r_xw^2}{\sqrt{12}\mu}\,
m\left[-mL_{j+1}+(m^2-1)
\frac{-mr^3Q_j}{\sqrt2w}+\mathrm{nonlinearFlux}_j\right]
$$

即可得到矩阵。nonlinearFlux 至少二阶，故其零态导数为零。各 retained mode 的一阶公式互不耦合；这依赖**精确 zero base**，不适用于一般非零 shooting 解的 Jacobian。

源码模块刻意按原 Fourier-product Jacobian 的 sigma、pref、targetFac、pFac 乘法顺序计算四个条目；没有用另一组 log/exp 公式替代。数学上的逐模分解已由源公式证明；完整 native RK 与小块传播的浮点结果仍不预称逐位相同。

## 3. 同一个 RK12 线性 stage map

零态 shape 在原 RK 的每个内部点仍为零，因此对原 RK 组合求导，得到的正是用同一 RK4 在上述时间依赖线性系统上推进单位阵。每个 stage 的最终 momentum 行还要除以原 cell.portRatio，正如原 cellFlow 的输出转换。

模块使用 live cell.engine.geometry(profile,x)，并要求调用方提供**原 pinned integrationGrid 函数**。它镜像原 78718-tail-fourier-product-flow 的两个分支：

- 有 cusp：原 integrationGrid(steps,cuts)，$h=x_{k+1}-x_k$；
- 无 cusp：ordinaryH=1/steps，$x=k\,\mathrm{ordinaryH}$。

每步用 $x,x+h/2,x+h$ 的同一实际几何。保留该分支是为了避免把另一源中的 $k/\mathrm{steps}$、$(k+1)/\mathrm{steps}$ 舍入顺序冒作逐位相同。

原非变分 rk4/cusp wrapper 与变分 flow 在实算术中是同一 RK 组合，但逐次浮点网格/加法顺序不应被未经检查视为完全相同；模块的身份明确是原**变分** RK 网格。最终实际 nonlinear evaluate、完整 J、Newton、所有 guards 和 audit 始终由原 worker 执行，模块不替换其中任何一个。

## 4. 保持原 far graph 的反向图与完整候选状态

设算出的第 $n$ 个 stage、模式 $j$ 的二维块为

$$
T_{n,j}=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
\binom{Q_n}{\pi_n}=T_{n,j}\binom{Q_{n+1}}{\pi_{n+1}}.
$$

以原 live far graph 为固定终值 $\gamma_{D,j}=G_{\mathrm{deep},j}$，反向定义

$$
u_{n,j}=a+b\gamma_{n+1,j},\qquad
\gamma_{n,j}=\frac{c+d\gamma_{n+1,j}}{u_{n,j}}.
$$

给定完整原请求 $H$，使用原转换 $Q_{0,j}=H_j/r_{\mathrm{cut}}^4$，再令

$$
Q_{n+1,j}=Q_{n,j}/u_{n,j},\qquad
\pi_{n,j}=\gamma_{n,j}Q_{n,j}.
$$

在精确算术中，这满足同 RK 零态线性化的所有 stage 拼接、原 Dirichlet 高度及原 far Robin 条件。它只是非线性问题的一个初猜，没有删除任何高度模，也没有把小 $H$ 截为零。

模块对非有限二维块、数值行列式为零、非有限/零图分母及非零数的传播下溢明确失败，不声称失败代表不存在非线性解。接近奇异的分母、块规模和候选图规模记录在 diagnostics 中；没有调宽原容差。原 graphs/gains/完整非 I/O 参数与 stage layout 在构造前后及每次 predict 时做精确数值身份哈希核对，防止初猜计算改变原问题。

## 5. 调用接口与最小接入点

模块只导出工厂，不启动 worker、不调用 solve：

    import {createZeroRKStageInitializer}
      from './geometry_20261114_zero_rk_stage_initializer.mjs';

    const zeroRK = createZeroRKStageInitializer(dn, {
      radius: zero.radius,
      integrationGrid,             // 原 pinned f6tail_cusp_grid 的导出
      expectedSteps: 12,
      sourceIdentity: {
        sourceSHA256: consumedSourceHashes,
        physicalIdentity: storedGeometryIdentity,
        backendIdentity: {
          tailJacobian: 'fourier-root-and-product-moments-v1',
          ...otherOriginalBackendIdentity
        }
      }
    });

    const guess = zeroRK.predict(req.height);
    const sol = dn.solve(req.height, {
      ...originalSolveOptions,
      initial: guess.states
    });

工厂数值构造仅允许在本公开仓库 Actions 中执行。sourceIdentity 是调用方已核验的原源、calibration、profile fingerprint 和 backend 身份；模块记录其哈希，**不谎称自己重新核验了调用方的源文件**。它另外记录实际 stage 几何/RK 网格、二维块、原 far graph、完整 H 和候选 states 的哈希。

若接入原 worker 的冷启动分支，原有效 tangent predictor 应优先。仅在没有已有 initial 的情况下明确选择此候选，并保证原 solve 接收的 req.height 一字不改。候选已经按原 $H/r^4$ 保留第零节点，不需要再用旧细图作 boundary correction。所有原 progress、trialDiagnostic、jacobian、audit 和接受选项原样保留。

没有改变配置，不新增“低于某个 H 阈值才使用”的规则，也不把该候选包装成已收敛响应。若使用调用方已有的 completed-zero 缓存，其原严格命中条件仍保持不变；此模块本身不读写该缓存。

## 6. 已完成 zero 响应能复用什么

原 completed zero checkpoint 保留完整 577×224 shooting shape 状态和完整物理输入，适合绑定零态身份。但只把它填入 initialCheckpoint 并不足以启用原 tangent predictor：

- 原 worker 把 checkpoint 装到 last；
- tangentPredictor 仍为 null；
- 对非零首请求，fallback 的首模比值是非零/0，不能通过 $(.25,4)$；
- 于是没有 initial，仍落回原 fine-graph cold initial。

真正恢复原 createPhysicalHeightTangentPredictor，需要**同一实际 RK、同一全部配置、同一 stage layout/cusp grid、同一 far graph**下的每 stage 完整 flow Jacobian。原 JSON 响应中的 cut heightJetJacobian 不能替代这些内部流矩阵。已有 strong_full_flow_tangent_storage 可保全这样的真实已计算 sidecar，但不能捏造当前 zero 包已经包含它。

可选的正确路径是：

1. 在同一 live worker 真正执行 zero 请求并保留原完整 stage tangent，再对完整新 $H$ 调用原 predictor；这是一次实际计算，需 Actions；
2. 若有已完成同配置的全 stage sidecar，严格核参数、物理源、far graph、全部状态/矩阵哈希后恢复原 predictor；
3. 当前独立模块从原零态代数线性化新建同 RK 小块初猜，仍对新 $H$ 执行全部原非线性计算。它不把这一新计算宣称为旧 sidecar 的缓存恢复。

非零 base 的响应通常具有完整模式耦合，必须使用其真实完整 stage Jacobian。不同 steps、shootingParts、quadrature、physical depth、far graph 或物理标量的结果只能在明确身份下作为另一个问题的初猜，不能冒充同配置的完成缓存；本模块没有实现这种跨配置复用。

## 7. 当前尚未支付的事项

本文给出的是完整源接口和源公式推导。request19 已定位 request17 原 cold residual；是否改善本次实际初猜，仍须后续明确选择的 Actions 计算。二维图能构造也不保证全非线性问题有可接受解；近零 H 也不自动保证深侧传播或图条件良好。

目前没有声称新 seed 通过 nonlinear guards、原 2e-9 shooting 容差、完整 native J、最终 audit、prefix 联解或闭面几何门。没有运行本模块数值，没有修改 exact 的 cold probe、原方程或共享工作流。

