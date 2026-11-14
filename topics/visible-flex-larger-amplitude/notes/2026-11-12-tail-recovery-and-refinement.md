# 低 H4 真实尾的恢复与同 H 精化

2026-11-12，tail_refinement（visible-larger-astra-20261112 子任务）。

**状态：恢复和数值精化进行中，不是更强前缀、无限尾或闭曲面完成结论。**

## 恢复边界

旧工作区 `/workspace/scratch/83b864ada613` 已不存在；仓库中仅有外倍数计划及原始成功尾，未包含中断前的最终外倍数响应。因此按 `numerical-neck-q070-tail24-external-plan.json` 重做这条指定路径。没有将旧交接里的完成计算误写成已保存数据。

新增 `computations/tail_replay_saved_plan.py` 先核对原完整方向、原成功响应和原 probe 源码的 SHA256，然后只重定位 source 和输出路径；数值、物理参数和全部命令行浮点字面量保持不变。

```bash
python computations/tail_replay_saved_plan.py \
  --plan notes/numerical-neck-q070-tail24-external-plan.json \
  --source-topic /workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface \
  --out-prefix notes/2026-11-12-tail-external-m24
```

目标保持完整原 18 项 $H$，M24 另补 6 个严格零高项；所有模式统一外倍数放大至 $H_2\simeq-1.2\times10^{-4}$。每一步均求原非线性尾，名义外倍数为 $2,3.5,5.337898277389474$。外倍数不是已实现的更强前缀幅度。

2026-11-12 02:47 UTC，第一步外倍数约 2 已通过原 $2\times10^{-9}$ 容差：4 次 Newton，最终归一残差 $1.1889256579839407\times10^{-9}$，$H_2=-4.4961516223829795\times10^{-5}$，cut 首 slope 为 $-5.329879568929848\times10^{-4}$。它的响应为 `2026-11-12-tail-external-m24-response_0001.json.gz`；本步没有额外全尾 audit，不能提前沿用目标点几何量。外倍数 3.5 的下一步已启动，使用真实全 shooting 切向初猜。恢复执行的完整入口记录在 `2026-11-12-tail-external-m24-replay-plan.json`，进程每轮保存迭代恢复包。

## 精化选择与实际 g 的含义

新增 `computations/tail_defect_spectrum.mjs` 在原实际 RK 审计网格上定位完整物理 Darboux 缺陷及原 profile 规范化缺陷的最坏点，并分解相应完整角向缺陷。M24/spacing2 的保留物理频带为 $0\le m\le48$，不是 $m\le24$。输出包含保留频带和更高频带的 RMS、采样上确界、主要系数，以及离散 Fourier 重构误差。

跨 shooting 子分段比较时，使用

$$
\mathcal R_{\rm original}
=\operatorname{shootingParts}\,
\left|\mathcal D\,E^2r\,r_x/w^2\right|.
$$

`fullD` 为物理 Darboux 缺陷，不乘这个坐标因子。角向频谱仅诊断下一档应当升频还是加密径向步长；它不代替重新求解，也不证明连续空间或全时 reach。

新增 `computations/tail_refine_exact_response.py` 从一个成功响应直接复制完整 physical H，增模时只追加严格零；一次只改变模式数、径向步数或审计步数中的一项。它冻结原物理构造、求解容差和全部共同 source hash，输出所有配置差异。后续用现有 `numerical-tail-compare-refinement.py` 对实际成功响应作严格同 H 比较。

此处冻结的是原存数定义的 $g_{\rm stored}$：`calibrationSteps=512`、`warpSteps=16` 及原全宽校正构造均保持。构造器内部用于物理背景的源固定 `modes=1`，实际尾模式数和 ODE 步数不进入其物理轮廓定义。没有把 $g_{\rm stored}$ 偷换成精确校准根定义的 $g_{\rm root}$，也没有把另行提出的有理深尾构造记入这条同 g 链。

## 待返回的实际结果

三步恢复尚在执行；最终响应返回后首先做完整 Darboux 频谱诊断，再据此选择一项真正同 H/g 精化。成功终态及其比较数据将追加在本节，不用中间 Newton 迭代替代成功响应。

2026-11-12 03:20 UTC，外倍数3.5已连续接受三个完整 Newton 步，残差为
$440.7865\to15.8568\to0.120369\to1.0813461\times10^{-5}$。
03:32 UTC 的第四个试步又降至 $2.76634601645\times10^{-10}$ 并被接受，但下述
回算故障使它没有落为成功响应，不能据此计作第二个成功尾。

### 原 worker 的回算中断及实际恢复

03:39 UTC 检查返回值时发现，原 worker 在最后一次 Jacobian 回算期间已经终止。
调用方只观察到 `Weighted tail worker stopped`；后续缩步请求立即发生
`BrokenPipeError`，没有执行新的非线性试验。原 probe 的
`stopped_reason=minimum homotopy step` 在这里是死进程上的控制流结果，
不能解释为非线性分支障碍。本次记录没有给出 worker 的信号或退出码，原因未证实。

×2 成功响应原封保留。旧的迭代包和失败摘要分别逐字冻结为
`2026-11-12-tail-external-m24-interruption-iteration.json.gz` 与
`2026-11-12-tail-external-m24-interruption-summary.json`，SHA及解释见
`2026-11-12-tail-external-m24-interruption.json`。
最后实际保存的迭代是 ×3.5 的 $1.08134611528\times10^{-5}$ 状态，
只是新的初猜；已接受的 $2.7663\times10^{-10}$ 试步没有被保存为完成结果。

新增 `tail_resume_interrupted.py` 读取上述冻结包，逐项核对完整 H 与原报告中的
精确浮点缩放顺序，然后先真正求成这个 ×3.5 请求，再向原最终
×5.337898277389474 请求推进。原物理参数、M24/512/depth8/parts8/steps12、
原 $2\times10^{-9}$ 容差及最大迭代数均不变，只采用下述已验证的同 g 存储适配器，
Node heap 限512MiB，记录实际子进程退出码与峰 RSS。恢复输出另用
`2026-11-12-tail-external-m24-resume-*`，不覆盖旧成功响应和故障证据。

这次 bounded 恢复完成了初始真实 Jacobian（残差
$1.08138038258\times10^{-5}$）并再次接受完全相同的
$2.76634601645\times10^{-10}$ 试步，但仍在下一次完整 Jacobian 回算期间被
SIGKILL。新 driver 明确保存 `worker_returncode=-9`、child峰RSS405232KiB、
heap上限512MiB，总时长941.893秒；原因仍未确定。数据和SHA冻结于
`2026-11-12-tail-external-m24-resume-interruption.json`，该前缀的 summary、trace、
trials、iteration 均已停止写入。它们不包含新的完整成功响应。

因此另建 `tail_resumable_engine.mjs`、`tail_resumable_worker.mjs`、
`tail_resumable_client.py` 和 `tail_resume_resumable.py`。新适配器在原 line search
已经接受后，立即通过原 progress recorder 把完整 trial states 写入原
`iterationCheckpointFile`，明确标记 `accepted-trial-recovery-only`。此时即使残差
低于门槛，仍不报告成功；原全 Jacobian 回算、正分支门槛、收敛条件和后续 audit
继续执行。源内存替换有唯一性断言，并验证去掉这个 progress 回调后，代码逐字符
等于已核对的原内核加共享稳定图入口。静态组装记录为
`2026-11-12-tail-accepted-trial-adapter-manifest.json`。
原 `tail_stored_*` 文件没有被改动，正在使用它们的其他任务不受影响。

主会话现安排现有数值作业收尾后给下一次恢复一个独占窗口，本支暂不另启大作业。
之后从第二次最后真正保存的迭代继续，具体入口为：

```bash
python computations/tail_resume_resumable.py \
  --prior-summary notes/2026-11-12-tail-external-m24-interruption-summary.json \
  --iteration notes/2026-11-12-tail-external-m24-resume-iteration.json.gz \
  --source-topic /workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface \
  --out-prefix notes/2026-11-12-tail-external-m24-resumable \
  --node-heap 512
```

这里仍先真正求成 ×3.5，再求原最终完整 H；没有跳过失败点、放宽门槛或把接受试步
改称成功包。

### 原 g 的低内存数值适配器

新增 `tail_stored_geometry.mjs`、`tail_stored_engine.mjs`、`tail_stored_worker.mjs`
和 `tail_stored_client.py`，供后续同 g 精化采用。它们继续逐字调用原
`createRecalibrationFactory(config).assemble()`，保留原160个胞元及全宽 warp
alpha；没有导入或构造有理深尾模型。仅把每个私有 profile 点缓存限制为96项，并使
各线性模式在同一物理采样点共享几何系数计算，各模式自己的 RK4 算术次序、cusp
拆分、归一化及原非线性方程和验收门槛保持。

共享助手为 `closure_bounded_point_cache.mjs`、`closure_linear_stage_graphs.mjs`。
后者的历史导出名含 `Rational`，但函数只推进调用方给定的 physical profiles，
不构造新 g。原 g 适配器把其 hash、明确源内存替换、全部物理参数和冻结 alpha
写入记录，并在缓存替换前后核对160胞元每段7个采样处的
`[r,drdx,logw,dlogwdx]` 指纹严格相等。

必要的端到端对照由 `tail_stored_adapter_check.py` 实际顺序调用两个 worker：
M3、N64、depth4、parts4、steps4、linearFar12、linearSteps64，完整物理
$H=(-10^{-6},-2\times10^{-9},10^{-10})$。两次都真正解非线性尾并做全部有限
Darboux 审计，残差均为 $2.4569446494384523\times10^{-10}$；parameters、cut、
linearSlope、全部 shooting states、jets、端点 Jacobian、Newton history 和全 audit
逐值严格相等。原 worker 32.27秒，缓存适配器45.68秒（含全 head 指纹），
该测试峰 child RSS 为142040KiB。完整记录是
`2026-11-12-tail-stored-adapter-check-comparison.json` 及同前缀两个压缩响应。
它检查数值适配器是否保持原计算，不将这个小测试计作高幅尾或闭合结果。

恢复初始化后又利用已有的两个 ready 记录作生产分辨率核对：
M24/N512/depth8/parts8/linearFar48/linearSteps512 下，原 worker 与新 worker
除输出/初猜路径外的全部参数、完整零态 cut jet 及24个线性 slope 逐值严格相等，
所有共同 source hash 一致，见 `2026-11-12-tail-stored-m24-ready-equivalence.json`。
它验证实际所用配置的初始化，没有把尚未返回的恢复请求计作成功。

后续精化脚本可显式选择 `--client stored-bounded` 或带即时恢复记录的
`--client stored-resumable`；默认仍为原 analytic-first。
小检查完成时没有打断原三步 M24 进程；原进程随后意外终止，才按上一节从真实
保存状态启用此适配器恢复。

`tail_defect_spectrum.mjs` 也已改用这个同 g 适配器构造审计引擎。在上述已保存的
M3 完整成功响应上独立重扫144 stages、720径向点，与源全 audit 的物理 `fullD`
及原坐标规范化最大缺陷之差均严格为0，角向离散重构误差
$1.8871\times10^{-25}$。测试结果为
`2026-11-12-tail-stored-adapter-check-spectrum.json`。其高频主项为物理频率8、
高于该测试的保留频带6；这是工具验证，不预先断言目标 M24 的频谱。

频谱工具又加入同一扫描中已有端点 jets 的接缝核对：按可自由平移的高度均值
对齐，逐角比较非零模高度、物理梯度，以及 $g$ 的单位正交径向/角向基中
$\operatorname{Hess}_g h$ 的算子范数跳差；cut 则比较积分终点与保存的 cut 节点。
它不把分段 ODE 自动改成全局 C² 浸入。M3 的143个内部接缝实测最大非零模高度差
$3.1764\times10^{-22}$、梯度差 $5.5511\times10^{-17}$、Hessian 跳差
$4.4409\times10^{-16}$；cut 的储存节点 Darboux 值与原响应逐值一致，
原全 audit 最大值也保持不变。记录为
`2026-11-12-tail-stored-adapter-check-spectrum-seams.json`。
下一步 M24/M32 对照会同时报告这些有限接缝量和完整 Darboux 频谱。

具体地，对 $g=E(r)\,dr^2+r^2d\theta^2$，代码比较的 Hessian 矩阵为

$$
\begin{pmatrix}
\dfrac{h_{rr}-E'h_r/(2E)}{E}
&\dfrac{h_{r\theta}-h_\theta/r}{r\sqrt E}\\[4pt]
\dfrac{h_{r\theta}-h_\theta/r}{r\sqrt E}
&\dfrac{h_{\theta\theta}+rh_r/E}{r^2}
\end{pmatrix}.
$$

对差矩阵 $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$，算子范数
直接按 $|(a+c)/2|+\operatorname{hypot}((a-c)/2,b)$ 计算。
这是物理径向坐标中的高度二阶量，不以分段 profile 参数的二阶导数代替它。

### 完整非线性 D–N 对 m4 不能忽略

对已保存的基点成功响应和新的外倍数2成功响应，取同一 worker 的真实有限线性坡度 $D_m$，比较

$$
\Delta S_m(H)=S_m^{\rm nonlinear}(H)-D_mH_m.
$$

| 外倍数 | $|H_2|$ | 最大 $|\Delta S_m|$ | 达到模式 | $\Delta S_2$ | mean slope correction |
|---|---:|---:|---:|---:|---:|
| 1 | $2.24807581119\times10^{-5}$ | $1.38392410785\times10^{-7}$ | 4 | $1.46716001893\times10^{-8}$ | $2.05616801016\times10^{-7}$ |
| 2 | $4.49615162238\times10^{-5}$ | $5.50286965354\times10^{-7}$ | 4 | $1.15322301512\times10^{-7}$ | $8.22432136433\times10^{-7}$ |

最大修正的 m4 分量均为负。其大小约占该模式线性坡度的27%和54%；首模 m2 的相对修正远小于这个量。这是两点实际计算，不是已证明的渐近阶，但说明后续强前缀需要匹配完整非线性 D–N，不能只依据首模线性坡度几乎不变判断完整接合误差很小。此比较不增加新的求解，直接由上述响应的 `jets.slope`、完整 `request.height` 及 `2026-11-12-tail-external-m24-summary.json` 中 `ready.linearSlope` 重算。

## 高模线性端口的实际接口依赖

strong_branch 后续需要 M>32 的 smallcut30 线性接口。固定原工具 `950f-tail-linear-cusp.mjs` 的 64 模、2048 步、far48 实算在完成 39 项后以 exit137 结束，没有完整 64 模端口。原因未由现有进程输出证明，不能写成数学障碍。原始部分结果改名为 `2026-11-12-tail-linear64-r2048-original-partial39.json`，中断说明为 `2026-11-12-tail-linear64-interruption.json`，不把其中 `modes:64` 的请求值误当作完成项数。

为降低保留几何点的内存成本，新增 `computations/tail_linear_port.mjs`。它只将独立的模式推进按胞元交错排列，每一模式的 cusp-split RK4 运算顺序逐字保持原函数；某胞元完成全部模式后释放其私有 point/profileSource/integrand/integrate 闭包，不再访问该胞元。不会修改固定源文件或正在运行的非线性 worker。

必要的小规模实现核对使用 3 模、64 步、far12：新旧工具的物理参数、cut、stats、全部 slope、logHeightGain 均逐值严格相等，结果为 `2026-11-12-tail-linear-cell-major-check.json`。该新工具本次测得峰 heap 37.0 MB、RSS 95.1 MB；这是此低阶运行的测量，不是64模的资源保证。

随后主会话查得全机 available 仅约1.85GB，要求避免与非线性尾并行的大线性任务。刚启动的64模 cell-major 重跑已主动中止（SIGINT，exit130，无成功输出）；非线性尾继续运行。待其结束或内存恢复后再顺序完成64模的2048/4096步对照，然后保留原32个已发布坡度逐字、只追加真实高模积分值。没有用外推或部分结果填充端口。

为避免需要 M36 时被完整64模接口阻塞，已将中断前真正完成的39行另行包装成 `computations/tail_smallcut30_port39_r2048.json`。它明确只有39模，原32项逐字保持，只加入物理频率66至78的七项实际2048步值；新增项的分辨率对照尚待。此文件只能按这一明确的有限线性设计等级使用，不能称作完成64模接口或已通过新增高模的收敛核对。

新增 `tail_linear_port_shared.mjs` 为上述共享系数方法的完整线性端口入口，继续使用
同一个旧 g。必要的3模/64步/far12对照中，原工具的 config、stats、cut、所有
slope 与 logHeightGain 全部逐值严格相等，见
`2026-11-12-tail-linear-shared-check.json`；该测试峰 RSS 为136852KiB。
后续高模端口可顺序使用这一入口，仍需实际完成2048/4096步两个分辨率，不能
用低阶一致性取代高模收敛数据。

主会话随后允许这个256MiB heap、单进程入口运行。完整64模/2048步/far48
在169.803秒成功完成，实测峰RSS280720KiB，输出
`2026-11-12-tail-linear64-r2048-shared.json`。它与原工具已完成的39项在生产
分辨率下逐值严格相等：所有 slope、logHeightGain 以及 config、stats、cut 均一致，
见 `2026-11-12-tail-linear64-r2048-legacy-check.json`。
4096步对照随后在321.454秒完整成功，实测峰RSS288228KiB，输出
`2026-11-12-tail-linear64-r4096-shared.json`。两档 config、cut、stats 逐值相等。
新增32个高模式中，最大绝对 slope 差为
$2.42623857048\times10^{-4}$，发生在物理 $m=94$，其细网格 slope 为
$-32854.9717859$，相对差 $7.38469\times10^{-9}$。
按 $|D_{4096}-D_{2048}|/\max(1,|D_{4096}|)$ 计的最大差为
$5.37302\times10^{-8}$，在物理 $m=76$；该处 slope 约2.44311618，绝对差
$1.31269\times10^{-7}$。逐模式数据为
`2026-11-12-tail-linear64-resolution.json`。

正式有限线性设计端口为
`computations/tail_smallcut30_port64_r4096.json`：原32个已发布值逐字保留，
物理频率66至128追加自4096步真积分，并保留两档对照及原32项的文件SHA。
它不提供非线性 D–N 或无限尾证明。高模 $m=94$ 的大坡度也表明，后续若遇到
Dirichlet 图条件数恶化，应检查完整二维 trace 或混合端口，而不是把斜率坐标
本身的近竖直误作线性解不存在。


## 第三次恢复已正式越过外倍数3.5（2026-11-12 04:51 UTC）

在强分支进程正式退出后，按主会话串行安排启动 `tail_resume_resumable.py`，
输出前缀为 `2026-11-12-tail-external-m24-resumable`。几何、原完整边界向量、
M24/N512、depth8/parts8/steps12、solveTol2e-9 及原接受门槛全部保持；
适配器新增的唯一求解期行为是接受试步后的 recovery-only 立即落盘。
用 `tail_session_watch.py` 记录实际 `write_stdin` 轮询时刻、工具会话状态、
trace 进展、可用内存与磁盘；工具外壳 exit0 不被当作数学成功。

04:48:36 UTC 的接受试步残差为 $4.1495190246767057\times10^{-10}$，
即时检查点已成功写入并另存为
`2026-11-12-tail-external-m24-resumable-accepted-call1.json.gz`（283104字节，
SHA256 `8c4cd779282e713a27e70588f96fb697e41e5e1b41e9b19b64a5deb2c53738dd`）。
它仍明确是 `iteration-recovery-only`，不以它代替成功响应。
随后完整 Jacobian 再计算结束，真正得到并保存
`2026-11-12-tail-external-m24-resumable-response_0001.json.gz`
（289449字节，SHA256 `7750816472435736958e22ba571e7875001b7176b6a904b9dd868c7728d54065`）。

该响应 `converged=true`，残差同为 $4.1495190246767057\times10^{-10}$，
$H_2=-7.868265339170214\times10^{-5}$，完整24分量与原外倍数3.5请求一致，
末6分量仍严格为零，577个 shooting states 完整保存。
最后一次完整检查的 minA 为0.6044561315025782，minD 为0.999801283794；
cut 首模 slope 为 $-9.323096316987383\times10^{-4}$。
本次请求耗时484.088秒。它是按原同伦路径保存的中间点，`audit=null`，
没有把端点诊断或尚未完成的目标全审计附会给它。
同一 worker 随即以原 tangent predictor 继续完整最终 $H_2=-1.2\times10^{-4}$；
此段写入时最终响应尚未返回。

### 无线性图的同状态审计入口与水平图二阶诊断

新增 `tail_defect_spectrum_nograph.mjs`，直接使用原
`950f-tail-subdivision.mjs:subdividePhysical` 和原 Fourier-root split 引擎。
由于审计读取已经保存的真实 shooting states，不求初猜、Newton 或线性边界图，
省去原入口构造后未用的 stable graphs。保存态、物理 profiles、RK 审计网格、
Darboux/频谱/有限接缝计算保持同一实现。
在既有 M3 成功响应上，除来源元数据与运行时间外，所有旧输出字段逐值严格相等；
加入下述新诊断后复核仍逐值相等。最终检查耗时12.823秒、峰RSS135772KiB，
对应记录 `2026-11-12-tail-spectrum-nograph-hessian-equivalence.json`，
原含图扫描为48.508秒。这是实现核对，不是高幅结果。

按 R21 的水平投影公式，在同一批源 ODE jets 上另外记录
$v=(h_r/\sqrt E,h_\theta/r)$、$n_z^2=1-|v|^2$ 及

$$
\left\|n_z^{-2}(I-vv^T)^{-1/2}\operatorname{Hess}_g(h)
(I-vv^T)^{-1/2}\right\|_{\mathrm{op}}.
$$

用稳定的秩一公式
$(I-vv^T)^{-1/2}=I+vv^T/[n_z(1+n_z)]$，无需在 $v=0$ 除以 $|v|^2$。
对独立特征分解及已知径向图的代数核对见
`2026-11-12-tail-horizontal-hessian-algebra.json`，相对误差均小于
$5\times10^{-16}$。M3 实现核对的46080个角向采样点给出
$\min n_z^2=0.8620687348630647$、最大上述范数9.749209891214974，
没有非正 $n_z^2$；这些数值只属于该低阶工具测试。
正式 M24 终态扫描将在同一流程记录这些量，并明确其等级仍是有限网格源 ODE
高度 jet 诊断，不是尚未建立的全域 Cartesian 插值、全角区间包络或闭合曲面证书。


已成功保存的外倍数3.5响应也延续完整 D–N 对照：m4 修正
$\Delta S_4=-1.656642526620882\times10^{-6}$，其绝对值是同模线性坡度的
0.929321947211151；m2 修正为 $+6.211068916320674\times10^{-7}$。
mean slope/second correction 分别为 $2.518394132088452\times10^{-6}$ 和
$9.548023764873748\times10^{-5}$。完整三点向量与响应哈希见
`2026-11-12-tail-nonlinear-dn-ray-through-x3p5.json`。
这仍只是原 q070 完整边界方向的外部容量路径；其他强前缀实际产生的向量须独立
完成全分量/mean 接合，不把其首模幅度落在此范围内当作已经匹配成功。


## 完整终 H 正式恢复成功（2026-11-12 05:22 UTC）

`tail_resume_resumable.py` 的第二个请求已完整完成最后 Jacobian、端点导数及全尾
Darboux 审计，正式响应为
`2026-11-12-tail-external-m24-resumable-response_0002.json.gz`
（301831字节，SHA256 `26032018bfd38a66aeceff84255d51a939a977eaf5bcbd70df476437c0433bac`）。
工具会话和 worker 均正常 exit0；总运行2383.9526秒，其中终 H 请求1826.9076秒，
峰 child RSS 为429492KiB。原18个完整边界分量、末6个严格零及全部原 g_stored
参数保持不变，$H_2=-0.00011999999999999999$，外倍数5.337898277389474。

| 量 | 此次正式终态 |
|---|---:|
| 原归一化 shooting 残差 | $2.362754975804353\times10^{-10}$ |
| 源 audit `fullD` | $3.9838637249211005\times10^{-9}$ |
| 源分段坐标 `normalizedFullDefect` | $4.615919517908019\times10^{-7}$ |
| 原 profile 坐标归一缺陷（上项乘8） | $3.692735614326415\times10^{-6}$ |
| 源 audit `actualMetric` | $2.2559735717749018\times10^{-13}$ |
| 源 audit `formalCurvature` | 7.9942546936068855 |
| 源 audit `minLeading` | 0.3788028508906775 |
| 源 audit `minD` | 0.9996963353417263 |
| cut 首模 slope | $-0.0014205594760717819$ |

最后完整 Newton 流的内部取样给出 minA=0.37877861403184593、
minD=0.9996962591711811；与上表 audit 网格不同，不把两种取样最小量混写。
这些数字恢复了 HANDOFF 中旧未推送终态到其记录的数值精度，但不是逐位一致性
声明，也不是精确无限尾或实际强前缀接合。
原 profile 归一二阶缺陷仍大于 $10^{-6}$，所以接着诊断频谱并做同 H/g 单项精化。

终 H 的接受状态在最终复核前也已冻结为
`2026-11-12-tail-external-m24-resumable-accepted-final.json.gz`
（282914字节，SHA256 `9a6fc88b06bc8472a27845d1cafd4a7ba173997ecef172f9caaf51272d67a2e9`）；
它保留恢复语义，正式审计结果以上述 response_0002 为准。
本轮活跃 trace、summary、iteration 和 session-watch 已随 worker 正常退出而固定。

完整四点非线性 D–N 账本为
`2026-11-12-tail-nonlinear-dn-ray-through-target.json`。终点 m4 修正
$-3.7098382133321962\times10^{-6}$，绝对值为同模线性坡度的
1.3645520602130214；m2 修正为 $+2.2660617697118583\times10^{-6}$。
mean slope/second correction 为 $5.85624496331094\times10^{-6}$、
$2.2174475017771014\times10^{-4}$。有限 deep 节点最大
$|Q|=1.982114282921276\times10^{-17}$、
$|\pi|=6.577640840967323\times10^{-16}$；它们服从此有限线性 Robin 闭口，
不单独构成真正无限尾的边界证明。


## 完整 M24 频谱决定升 M，而不是先加径向步数

同态审计 `2026-11-12-tail-external-m24-final-spectrum.json` 已成功完成，
664546字节，SHA256 `3c4b2fa24dd566f5cf2177e55ca81398f09c94e1371cdcec7ce2ceb810d88f5a`。
扫描覆盖全部576段、7488个径向取样及3833856个角点；耗时160.790秒，
峰RSS295664KiB。其物理 fullD 与正式响应 audit 逐值相同；原 profile 归一最大值
仅因乘法次序有 $4.24\times10^{-22}$ 舍入差。

物理和原 profile 归一缺陷的最大点均位于 stage32、rawCell0、rawSegment4、
该段外端 $x=1$、$\theta=0$。最大 Fourier 幅为物理频率50的
$2.1206290029599116\times10^{-9}$，已经超出 M24 保留频带48。
后续主项为频率52、54、56，幅分别约
$8.4183\times10^{-10}$、$4.3641\times10^{-10}$、$2.4370\times10^{-10}$。
带外能量占比0.9999999999116869；保留频带 RMS 只有
$1.5563561766423658\times10^{-14}$，带外 RMS 为
$1.656138097507468\times10^{-9}$。
离散 Fourier 重构误差 $1.3669\times10^{-22}$，不把这个谱分解当连续角向包络。

575个有限内部接缝中，最大非mean高度差为
$1.3552527156068805\times10^{-20}$，物理梯度差
$5.898059818321144\times10^{-17}$，协变Hessian算子范数跳差
$2.664545423456969\times10^{-15}$。
cut 积分终点与保存节点的高度、梯度逐值相等，Hessian跳差
$4.4410\times10^{-16}$。这些是有限分段源 ODE 的相容性检查，仍不是全局
C² Cartesian 重建或精确闭曲面的证书。

同一批 jets 的水平图诊断给出
$\min n_z^2=0.862049348880797$、图Hessian最大范数9.792329424867141，
没有非正 $n_z^2$。该范数峰在
$r=0.18085309461437976$、stage56、rawCell0、rawSegment1、$x=0.25$、
$\theta=0.5031456984264903$；该点内蕴正交Hessian的
$(rr,r\theta,\theta\theta)$ 分量为
$(7.361637704056747,-8.12724726186615\times10^{-5},1.8771454434497203)$。
图Hessian范数不等于 principal curvature，也不因其较粗充分界未满足就宣布reach失败。
相应更强的条件性整图引理已完整证明为
[R25](../results/R25-entire-graph-curvature-and-reach.md)，仍要求真实全域图/延拓和曲率证据。

据此选择唯一数值改动 M24→M32：原24个完整物理 H 系数逐项严格保留，
新加8个 Dirichlet 系数严格为零；N512、steps12、auditSteps12、depth8、parts8、
solveTolerance2e-9以及全部原 g_stored 构造量不变。
精确计划与原24项守卫见 `2026-11-12-tail-fixed-h-m32-plan.json`。
主会话安排的 exact 深尾、root 加密和 strong q.09 已依次完成后，
此精化已接独占窗口启动，输出前缀 `2026-11-12-tail-fixed-h-m32`，
使用 stored-resumable 及512MiB heap；此段写入时尚无 M32 正式成功结果。
正式 coarse/fine 对照将继续使用保存的完整 H、source SHA、g 字段和原 profile
归一缺陷，不能仅凭本频谱预测就记作二阶缺陷已经下降。


## M24→M32 同 H/g 单项精化正式完成（2026-11-12 05:50 UTC）

M32 worker 与工具会话均正常 exit0，正式响应为
`2026-11-12-tail-fixed-h-m32-response_0001.json.gz`，405553字节，
SHA256 `757dd01bb246b0e2bfbc7d12d20cfa13e235792193f35d4724eda07f5b705f6a`。
完整运行793.9907秒，峰 child RSS499588KiB；没有放宽2e-9求解容差，
最后残差为 $1.4911055292433237\times10^{-9}$。
在正式响应前已冻结 accepted-final 恢复包376461字节，
SHA256 `53bbdbca49e360f6bfc84d4fb06836fe70845edf595253c9a9547e87a23520fb`。
结束后所有 summary/trace/trials/iteration/session-watch 均已固定，数值窗口交给
strong 的 fresh q090 c6-held，再由主会话安排实际尾联解。

严格对照为 `2026-11-12-tail-fixed-h-m24-m32-comparison.json`：
原24个完整 H 分量逐项严格相同，新8个系数严格为零；所有物理构造字段、
physical depth 和23个共同 source SHA 一致。实际配置差异只有 modes24→32
及四个初猜/输出路径；N512、steps12、auditSteps12、parts8和tol不变。
初始化的额外核对为 `2026-11-12-tail-fixed-h-m32-ready-equivalence.json`，
原24个线性坡度、零态cut全部标量/原24分量、warp alpha 和全部 profile 指纹一致。
完整 factory 参数 manifest 还带有 modes 和路径字段，比较已逐项列出这些允许差异，
没有误称整个 manifest 字典逐字相等。

| 完整有限尾 audit 量 | M24 | M32 | M32/M24 |
|---|---:|---:|---:|
| 物理 fullD | $3.9838637249211005\times10^{-9}$ | $2.8580463918102173\times10^{-9}$ | 0.7174056617 |
| 原 profile 归一二阶缺陷 | $3.692735614326415\times10^{-6}$ | $1.884478770591488\times10^{-7}$ | 0.0510320523 |
| actualMetric | $2.2559735717749018\times10^{-13}$ | $7.349679568999704\times10^{-14}$ | 0.3257874853 |
| formalCurvature | 7.9942546936068855 | 7.9942546936068855 | 1 |
| minLeading | 0.3788028508906775 | 0.3788026693030439 | 0.9999995206 |
| minD | 0.9996963353417263 | 0.9996963353417263 | 1 |

因此本次真正降低了同一 H/g 的二阶缺陷：原 profile 指标改善19.5955278倍并降至
$10^{-6}$ 以下；物理 fullD 也降低约28.26%，其改善幅度应单独报告，
不能把前一指标的19.6倍套用给物理 fullD。
共同 cut slope 最大差为 $7.162734552861406\times10^{-16}$，
共同 cut second 最大差为 $1.6665724914720147\times10^{-14}$；
新增 slope、second 分量最大值分别为
$1.8537190709189638\times10^{-19}$、$3.6075415003968827\times10^{-16}$。
mean slope/second correction 差分别为
$8.470329472543003\times10^{-21}$、$-5.421010862427522\times10^{-19}$。
这些是真实完整响应的比较，不把极小 cut 差误当成内部二阶缺陷没有变化。

M32 的以上极值来自全有限尾源 audit 网格。为按约定及时交出唯一大数值槽，
没有另做 M32 全频谱/有限接缝扫描；因此不把 M24 的最坏位置、R21图Hessian峰
或接缝数值当作 M32 已测结果。当前仍缺连续角/径向包络、真正Cartesian重建和
精确无限尾接合，以及实际强前缀完整向量族的非线性闭合。
该外部容量 ray 及其离散精化自身不构成闭曲面或强幅族完成声明。

本轮曾遇可用磁盘显示为零，但接受状态已成功写入；一次额外的只读会话内存备份
也验证了gzip完整性。空间恢复后求解/审计正常完成，没有数学参数变更。
正式成功响应核对完成后已释放这份临时内存副本，不另存不必要的大中间数据。
此次成功采用串行大作业、定期真实 session 轮询和即时恢复记录，
不能由这一个组合实验断言此前 SIGKILL 的唯一原因。
