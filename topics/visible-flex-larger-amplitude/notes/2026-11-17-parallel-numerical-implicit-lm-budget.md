# 固定完整 Pr 的唯一 LM 后继预算

这是执行前冻结的预算定义，不是数值收敛结论。[完整入口源码](../scripts/parallel_20261117_implicit_lm_budget.py)，17058 B，SHA256 `927f403f984c88471dedaf14988b6cd25ebd44b5ce3d0a1e6a0bcc57ea20cc0d`。根会话已授权此单次有限预算；没有从旧 `5b965` 失败终态初始化。

## 不变的问题和已经付过的第 0 步

固定原 `1662` 的 602 节点、M160/N2048、全部独立 Y/U 变量、580328 个节点/实际中点/边界残差、原 scalar profile、325/157 边界以及 `Pr_tol=1e-8,bc_tol=1e-11`。不改 raw 行权重，不换边界目标，不删角模。

直接复用此前一次方向的初始完整列范数、正对角 S 和两个 scaled boundary QR 的 Q；不重算列范数或其整数 BB 秩证。后续数值边界坐标始终使用这同一个 S 和 Q。原 tiny BC 残差只通过 `B S Q` 的小型方阵求仿射修正 d0；方向为 `d0+SΠz`，全 J 和 Jᵀ仍包含所有原 BC 行。每个试点都再次核原 BC≤1e−11，浮点投影不冒称逐位准确线性可行。

先前已付的唯一 damp1 方向和满步物理审计作为 **direction0 / accepted step1**：

- 原 raw SSE `1.5321026127227238e−4`。
- 线性模型 SSE `5.45386957703086e−5`。
- 满步实际 SSE `5.4538649626341434e−5`。
- 8192 全节点和实际三次中点的 rho/Q/W/H/normal 全正。

不重复该 LSMR 和物理审计。只为取得当前完整残差数组，重算同一个满步的原 Pr residual 并逐值核成本及 Y/U SHA。由这一步的实际/预测下降率，后继 damp 为 .5。

## 固定数量与接受规则

最多 **24 个方向，包含缓存 direction0**；最多 **20 次接受，包含已有满步**。每个新方向仅调用一次完整 LSMR，`maxiter=128,atol=btol=1e-8,conlim=1e6`，初值为零。所有有限退出状态（包括预算退出）和显式正则 normal residual 原样记录，不把 `istop=7` 或一般有限返回称为线性收敛。

在当前基点用当前完整 Jacobian 计算

\[
 \operatorname{pred}=S_0-\|r+J\delta\|^2,
 \qquad
 \operatorname{ratio}=\frac{S_0-S(X+\delta)}{\operatorname{pred}}.
\]

只尝试完整 `alpha=1`，没有额外 alpha 扫描。接受须同时满足：

1. 全残差有限，`pred>0`，ratio 有限且至少 `1e-4`，真实 raw SSE 严格下降，全部原 BC≤1e−11。
2. 仅在上述代数门通过后调用原 `P.physical_samples`：8192 角、602 个节点、601 个实际公共三次中点；rho、Q、W、H、正分支 normal velocity 全正，全部所需量有限。

接受后 ratio>.75 则 damp÷2；ratio<.25 则 damp×2；其余不变。拒绝始终保留当前基点、damp×2，并复用该基点的 matrix-free J 缓存。固定 S 永不重算；接受后重新建当前局部数值缓存，无需全局 Jacobian 或 dense 列范数。

中间 Gram 不要求单调：唯一第0步已经显示兼容行下降可伴随单位速度误差上升。正分支门仅是指定有限采样网格的门，不是全角/全径向严格证书。没有私增 RMS 点、缩小物理容差或用更稀角网代替已有门。

## 保存、失败和终态责任

每个新真实方向保存 dY/dU/z 和其基点 SHA，每个被接受的代数态保存完整 Y/U。全部 raw 在独占仓库外 work 目录，原始数组不写入 Git；完整算法源码随本条公开。拒绝态不作后继父，异常保留最近接受态；不会以放宽容差、增加预算或重开同一 run 消解失败。

满足全部原 Pr/BC 容差、用尽24方向或20接受预算之一时结束本次 run。终态完整调用原 8192 物理审计，并调用 `terminal_common_jets` 保存所有节点的隐式 common accelerations、C_U 条件估计/线性残差/缺失节点。原 level-set 加速度定义和 C1 公共三次的限制不变。输出始终标 `accepted_parent=false`，保留全部状态、节点/中点/BC 残差；不由 finite algebraic convergence 自动宣布原显式 BVP、C2 Gram、reach 或全题完成。

## 实际输入身份和启动命令

- 原 warm：`1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057`。
- 原 Problem 源：`5b965b9c4f9979a5b8dcc38661de027570d04d55aceb86de0dc7b1217fb03aac`；多项式源 `ba0b17fc85af8510c7c45b22a8facecd59061f53b3f7fd4adb48d3380c74e1a2`；matrix-free 源 `ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4`。
- prepared NPZ：`d742521c362b0f680bf53a329784a516416da83fbfd226a23f3a4cb051c7a36c`；preparation report：`f691e4e31d53d04a10a4c16be6c23bf15fa0c7aaed56d2338c214b40e2618224`。
- direction0 NPZ：`5629db05e0cc7b014c6eb4375badb35ea1d408f40d8cdbccef88122e6150798e`；方向 report：`5ac4371a2ff1b7be659a21a507e62d9974c75878308610d095389cefda1b1a7f`。
- 满步 physical report：`ebb364fee7e9a8d5fdfb587a1d89c440f4159862c8453105edf07dcf06c6fd84`。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_lm_budget.py \
 --topic math-research-public/topics/visible-flex-larger-amplitude \
 --problem-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_newton.py \
 --warm parallel-hold-m160-short-bvp-warm.json.gz \
 --polynomial-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_probe.py \
 --matrix-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_matrix_free.py \
 --prepared parallel-implicit-lm-direction-once.prepared.npz \
 --preparation-report parallel-implicit-lm-direction-once.preparation.json \
 --first-direction parallel-implicit-lm-direction-once.direction.npz \
 --first-report parallel-implicit-lm-direction-once.json \
 --first-physical parallel-implicit-lm-fullstep-physical.json \
 --work parallel-implicit-lm-budget-work \
 --out parallel-implicit-lm-budget-once.json
```

每次方向前与终态均核源和输入 SHA。此预算的后续数值终态另记，不回改本冻结定义。

## 唯一执行已实际启动

上述927f403f源和全部缓存身份冻结后，numerical_route已按完整CLI唯一起跑，输出 `parallel-implicit-lm-budget-once.json`，work为 `parallel-implicit-lm-budget-work`。它是本次完整预算的唯一终态读者；geometry接其真实终态共同二jet，不读正在变化的checkpoint。原819片Gram与818胞曲率批次继续各自原计划。此处只登记启动，不预填收敛或验收。
