# M15 前缀 / W22 真尾：同 N512 的实际运行入口

会话：Astra-visible-flex-78718bd0；作者：`/root/numerical_recovery`；2026-11-10。

## 可以直接执行的命令

从仓库根目录运行，使用全新的输出 stem。仅在前一个重计算实际结束后单开；本命令本身没有被本文作者启动。

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  topics/visible-flexible-closed-surface/scripts/78718-run-prefix-mode.py \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier \
  --tail-jacobian fourier-root --tail-predictor tangent \
  --max-nodes 8000 --data-gib 6 --node-heap 1536 \
  --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-02
```

这里诚实使用旧的 2633 节点 M15 UNSOLVED warm；旧主程序首 inner 的 5345 节点结果没有落盘，不在输入中冒充恢复。真尾种子是本轮已闭存的 M15/N512 首响应，尚不是 M15 最终联解。两份输入的 cut H 相等。

### 各项实际作用

| 显式选项 | 改动 | 保留 |
|---|---|---|
| prefix `--jacobian fourier` | R88 的六 JVP/有限 Fourier 积装配 | 原 RHS、BC、物理参数和容差 |
| `--transforms fourier` | R90 的长精度合成/投影；复数实虚分开 | 同 N 点方程、完整圆柱基、原范数 |
| `--tail-jacobian fourier-root` | 尾根 Gram 的 Fourier 积矩，以及 R89 变分装配 | 原 root residual/Newton/floor、split 状态 RHS、RK4/cusp 网格 |
| `--tail-predictor tangent` | R92 从本次已收敛 W22 的全节点切线预测下一 H 初猜 | 真 nonlinear shooting、原 line search/残差/BC |

客户端用环境变量选择数值算法，不给物理 cfg 添加键。组合 worker 为 `78718-prefix-tail-tangent-fourier-worker.mjs`，内部选择完整 engine 工厂，不为每个组合复制一个 worker。ready 会给出 `fourier-root-and-product-moments-v1` 和 `full-shooting-tangent-v1`；实际 packet 保存真实 source SHA。原 `original`、仅 `fourier`、`linear` 仍可显式选择。当前 `tangent` 只接到两种 Fourier 尾后端；不会静默改变用户选择。

第一笔 W22 bootstrap 没有自己的收敛切线，故使用 R86 的旧 Q/L 几何延拓以及原线性边界修正。只有实际 W22 收敛后，worker 才保留本来已经计算的 Js 并构造 R92 预测；不可把旧 M15 Jacobian 当 W22 的切线。若切线构造/预测失效，保存原因后回到原 warm；成功由未改的非线性求解判断。

## N512 与原要求

前缀 M15 的基规则仍是 `N >= max(512,8*(3M+1))`。尾引擎本来要求 `N > 4*spacing*W`；W22、spacing3 时是 `N > 264`。此前通用封装把 `8*(3W+1)=536` 经验选点式也当成显式输入下限，使 N512 无法选择；本轮只去掉这个额外限制，保留 N≥512 及真实引擎条件。自动选 N 的默认经验式仍给 W22/N1024；本命令明确选择 N512。

当前 M15 原尾在 N512→2048 固定态诊断的误差变化约 1e−15，主要差异来自频率截断而非已测角求积。R86 的 W22/N512 几何嵌入后 680 点局部向量场 metric 峰约 3.33e−10，这是选真实 W22 的依据之一，**不是新 W22 尾或整图已通过**。新高坡、高二 jet 与完整 XYZ 接缝都由自己的后端计算承担。

## 实际已完成的范围

工具 `fbc9ee` 自然 exit 0，0.540 秒；上述全部数值选项加 `--prepare-only`，另用 `...m15-w22-fast-prepare-01` stem，真正构造了原 2633 点初猜：M15/N512、W22/N512，H 差 0，前缀最大谱权 2048。0 DN、0 BVP，未运行根/射击或 predictor。报告 `2026-11-10-78718-numerical-m15-w22-fast-prepare-01-mode-run.json` 为 13,709 B，SHA `bd6cbdcac175b826203b623bf555addc7a5ae42c5ba0963ae7cab12fd21401c3`。完整命令及真实终端回执在 `2026-11-10-78718-numerical-m15-w22-fast-preparation-observed.json`。语法检查 `8247f1`、`510e68` 也实际自然 exit 0。

driver 当前 26,515 B / SHA `62625d2ca59a7d2cfd9d9b72b6b5ac4b2d3ebc327eef20f9716c4470b0d334de`；组合 worker 12,156 B / SHA `70f2c6f6648dcf0f616a328f22cc3d362529fde3248f6cbd9392e1a0334dfc00`。这只是历史实际入口说明，不设重新冻结或独审门。

### fast-01 实际启动失败与默认字段修正

根先实际将旧 61908 主计算人为结束（工具 `f5f4cc`，exit 130），如实记录为调度停止，不判数学失败。随后根以 `...fast-01` stem 真启动；工具 `22838b` 自然 exit 2，约 0.11 秒，原 summary 保存 `KeyError('projectionFloor')`，没有进入真 DN/BVP。旧输出全部保留，不复用此 stem。

原因是通用 adapter 曾误写 `cfg['projectionFloor']`；已存种子的 cfg 合法地省略这个默认字段。原控制器与原/新 core 构造均使用默认 `.05`，已存种子的实际 `parameters.projectionFloor` 也恰为 `.05`。只将 adapter 改为原形式 `cfg.get('projectionFloor', .05)`；不向 cfg 添加键，也不改变实际 floor。`correctInitialBoundary` 等已有默认读法仍保留。

实际 `5b3e1a` 自然 exit 0 的只读确认输出 effective floor=.05、saved runtime floor=.05，0 DN/BVP。修后 adapter `78718-tail-mode-continuation.py` 为 5,310 B，SHA `3e9b1835f6c2cbf1cc40fc6e49894d3004199e898da630d500e951f11b2c951e`。上面的命令改用新 `fast-02` stem；本文不把纯 prepare 当成已经经过 constructor 或真求解。

## 资源、观察与后续数学

单个进程 DATA 上限 6 GiB，Node old-space 1536 MiB，单个文件上限 4,999,999 B。两者是每进程限制，不能证明聚合内存足够。最近只读全局观测为 MemTotal=10,206,472 kB、MemAvailable=3,463,456 kB；当时旧主还占资源，故不并开第二个重计算。保 M15 前缀相同节点的显式 CSC 约为全 M22 的 47.15%，但不能把它当作 LU 或总峰值预测。

新的 mode-run/JSONL 会记录尾初始化、RHS Jacobian、LU、inner 返回与实际快照。每次 inner 返回后，立刻保存 `<stem>_inner_0001.json.gz` 等物理 quintic 候选以及原 cubic/节点；全部标注 outer UNSOLVED。可在下一真 DN 期间对自己的已闭存候选运行严格入口工具，不再等待整个 outer 的最终 CP。快照本身不改算法；详见 `2026-11-10-78718-numerical-inner-snapshot.md`。

真正有限联解成功后仍须对完整 W22 包、完整 signed XYZ common-cut 和同一 g 做连续全图指标，并满足原 2e−9、reach、可见幅度、保持带及非全等条件。有限成功或任何小样本加速测试都不代付这些数学要求。
