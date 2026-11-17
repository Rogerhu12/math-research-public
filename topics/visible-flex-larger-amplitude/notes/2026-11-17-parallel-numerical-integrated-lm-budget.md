# R647：完整 T 坐标 Pr LM 新预算

## 固定任务和已付第 0 步

本次是原 `1662ee34…` 暖场的一个新完整预算：同 Hold g、602 节点、M160/N2048、全部 580328 个原节点/中点/边界标量行，原 325+157 BC 及其 target 逐字保留。不从旧 `bf5a…` 未达标终态初始化，不改 raw 行权，也不调用完整二次谱的新行。

固定复用 `ef81…` 的可逆 T 和 `7aff…` 的初始完整列尺度 S、BTS 仿射修复和投影 Π。全部 U 和全部 trapezoidal compatibility defects D 都保留。方向与正则化目标为

\[
\delta x=d_0+TS\Pi z,\qquad
\min_z\|r+Jd_0+JTS\Pi z\|_2^2+\mu^2\|z\|_2^2.
\]

新坐标改变步范数，不能称与旧 S-only LM 的正则目标等价。列 moments/尺度不重算。

第 0 方向直接使用已完成 `2754…` 源的 `de935…` 报告和 `eb3e5…` 真实方向。它由原暖场计算，damp=1、LSMR 128 次，真实满步 SSE=`3.481273683531508e-6`、ratio=`.999999531353289`，其全部 8192 角 node+mid 分支门已付。新源只核身份、Y/U 和 raw 残差，**不重跑该 LSMR 或物理审计**。按冻结接受规则记为第 1 次代数接受，下一方向索引为 1，damp=.5；不是物理合格父。

## 新预算与接受规则

最多 24 个逻辑方向（包括缓存 0）、最多 20 次接受。**其余每方向 maxiter 固定为 512**；这是相对旧预算的新迭代上限，不隐藏成旧算法未变。atol=btol=`1e-8`，conlim=`1e6`；有限 `istop=7` 不冒称线性收敛，所有状态和显式 normal 残差完整记录。

只评价 alpha=1。`pred=SSE-||r+Jδ||²` 仍含全部原行。仅当全残差有限、pred>0、实际 SSE 严降、ratio≥`1e-4`、BC≤`1e-11` 后，调用原 P.physical_samples：8192 角、全部 602 node 与 601 实际 cubic midpoints 的 rho/Q/W/H/正法速度均正，才接受。Gram 不要求中间单调，但完整记录；代数终门仍 node/mid max≤`1e-8` 与 BC≤`1e-11`。

接受且 ratio>.75 时 damp 除 2；ratio<.25 时乘 2；其余不变。拒绝留原点，damp 乘 2。没有删模、换 g、改容差、加节点或改方向/接受总额。LSMR 异常诚实保留前次接受点并终止；非有限方向/模型按原拒绝规则计入预算。

## 保存与同预算恢复

源码在 scratch，所有原始状态、方向和报告仍只在 scratch：

- 每个接受点单独 NPZ 保存完整 Y/U，不覆盖既有异值；每个返回方向保存 z 及可定义的真实 dY/dU。
- `direction-NNN.ready.json` 绑定源/base/damp/方向 SHA，写于 LSMR 结束后；若恢复时存在，直接复用，不能重算该 LSMR。
- `direction-NNN.evaluation.json` 保存完整候选残差摘要、ratio、8192 审计及接受/拒绝。恢复时直接消费已完成评价，不重审其分支。
- 每一个完成方向，包括拒绝，都原子提交 checkpoint：history、accepted/directions/damp、状态 SHA、原 policy 和 identities。已完成逻辑计数不会刷新。
- active-call 每 16 次乘积记录阶段、当前索引/base/damp、Jv/Jᵀv 次数与耗时。若执行器中断，仅未形成 durable ready 的调用可按同索引同 damp 重启；旧 active 记入 partial_runs，次数是已见下界，不能隐去或叫数学失败。恢复需显式 `--resume` 且同源/同policy/同已保存 SHA。
- 所有关键文件经临时文件、flush/fsync、rename 发布，避免读半写文件。末态复用最后接受点同二进制 SHA 的完整物理审计，并保存共同隐式加速度供唯一 C² 读者；不把非零 Pr 残差上的加速度解释为精确解的导数。

prepare-only 已实际通过，未运行任何新方向。算法源 `parallel-implicit-integrated-budget.py` SHA256：
`0f2691136d584101317cbbde796050c8896d610f5df186665d2fe92e7db09213`。
准备报告 `parallel-implicit-integrated-budget-once.preparation.json` SHA：
`77b3c37e3cd5d162f64e0833c177278f0e453f7367596c487fb221364e3d678c`。
完整来源 SHA 在该报告；新运行尚未因准备检查启动。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-implicit-integrated-budget.py \
 --topic math-research-public/topics/visible-flex-larger-amplitude \
 --problem-source parallel-model-implicit-frenet-newton.py \
 --warm parallel-hold-m160-short-bvp-warm.json.gz \
 --polynomial-source parallel-root-implicit-frenet-probe.py \
 --matrix-source parallel-root-implicit-matrix-free.py \
 --coordinate-source parallel-root-integrated-coordinate-preparation.py \
 --prepared parallel-root-integrated-coordinate-preparation.prepared.npz \
 --preparation-report parallel-root-integrated-coordinate-preparation.json \
 --first-direction parallel-implicit-integrated-direction-once.direction.npz \
 --first-report parallel-implicit-integrated-direction-once.json \
 --work parallel-implicit-integrated-budget-work \
 --out parallel-implicit-integrated-budget-once.json
```

准备检查在同命令追加 `--prepare-only`，恢复仅追加 `--resume`，不更换目录或输出前缀来刷新预算。实际启动和终态另记，不把这份计划当已完成的数值结论。

## 实际启动补记

根会话已完整读取算法及原规则关系；随后唯一真实 session99082 启动。缓存0直接记 accepted1/directions1，SSE3.481273683531508e−6；方向1由µ=.5进入新的512上限，原数学总额不刷新。accepted001 NPZ 的SHA为 `1f8cb0f0a8cfc8d2e783db34eaee2596c35454b3abce36faa892147c97de5f53`。实际启动preparation重新记录运行耗时，SHA为 `e86e5d4f016e53fc798910f2a1dee29d4876f53e38528bdd72b2635e495ee3e0`；上文77b3仍准确识别此前prepare-only，不混作同一文件版本。源码在仓库的规范路径是 `scripts/parallel_20261117_implicit_integrated_budget.py`，字节与0f269原运行源完全相同。numerical为唯一实际终态读者；运行未完成，不预填结果。
