# 十二查询同父场的完整 QR–H 候选入口

日期：2026-11-14。本文登记两个独立新消费者；仅完成源码阅读、标准库 AST/编译检查和冻结源码 SHA 核对，**尚未执行科学计算，没有新的 warm、FD 或 BVP 接受结果**。所有实际运算只允许在 `Rogerhu12/math-research-public` 的 GitHub Actions。

## 1. 本次改变和固定对象

新 warm 入口为 `computations/geometry_20261114_twelve_query_qr_projection_warm.py`，新 FD 入口为同目录的 `geometry_20261114_twelve_query_qr_projection_response.py`。

它们从实际 request37 的同一 warm/status 出发，与 request39 的十二查询 C 候选共用父场。首个父 warm 的 SHA 为 `dd83748341c8d6172096fc644361018be7b29d856de621a0b333104d20aafdb8`，status 的 SHA 为 `37e70ad5a3c9ef828d93bcbf371b3a107e3890026731d7944d98e370987d29e0`。入口没有假设 request39 已产生可用父场；后继只允许本新 schema 的真实 warm/status，并逐项保留和检查其完整 producer。

固定有限模型仍是

$$
A=W_r J S^{-1},\qquad
f(z)=\frac12\lVert Az+b\rVert_2^2+
\frac{270^2}{2}\lVert z\rVert_2^2,
\qquad Bz+c\geq0.
$$

完整 $A$ 使用原全部 699 节点、338 物理状态、109 个自由核参数和 3 个全局控制，共 236036 个精确约束坐标。十二个 typed 查询保留九个完整 left-RMS 网格和三个原始 collocation midpoint 网格，每组 2048 个角，合计 24576 行。原 $W_r,S,b,C,B,c$、$\lambda=270$ 和当前场的所有输入值不重定义。

基线 C 投影仍只允许修改节点 471–482 的物理坐标及三个全局控制，共 4059 列，完整 $B$ 同时保留节点 470。它使用原冻结 `fixed_support_halfspaces` 的有效右端 $c+B_{\rm out}z_{0,\rm out}$，该右端可以为负。原 whole-vector 径向修复和同模型线段选择照常保留，因此最终 C 方向也不声称区外分量逐值固定。

新的 H 候选使用**全部 236036 列**，包括节点 470、全部自由核参数及全局控制。固定支持的描述只适用于 C 基线。H 候选是否采用，取决于原完整模型的实际 $f$ 比较以及后续原始非线性回溯，不由局部投影成本决定。

## 2. 源码身份及复用边界

本次新 warm 源 SHA：`4b768828f754f75d760980d596f198984e92f5ceac79832123c74e42985a5c67`（29331 字节）。

本次新 FD 源 SHA：`721f6337fa5ef07684ff99775c9d4b8e8d98f4b3d3d6a7aa220111a1b4657367`（2489 字节）。

以下冻结源逐字不改：

| 来源 | SHA-256 |
|---|---|
| `exact_20261114_regularized_block_qr.py` | `596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722` |
| `geometry_20261114_full_metric_inequality_correction.py` | `d5e9432e979859ed7d5277452ac058eb93e99da1cae7f96f700f15d7359d919c` |
| `geometry_20261114_full_metric_projection_warm.py` | `8fb6411e7b876713725a80c2dbe9e322cc277001b0692ccc59e0edd59ec4e8b0` |
| `geometry_20261114_twelve_query_projection_warm.py` | `10ed25405930f3775d8fb88f007aa50be4a53f4b3421904be959f1890ed67477` |
| `geometry_20261114_twelve_query_domain_operator.py` | `6a428d2f8412659cbd318321aa992c3b4565ff41177131a9cc9d268c6fbb7b1f` |
| `geometry_20261114_fixed_support_halfspaces.py` | `0c5573ea26d2c69c1a22595e00de9e41b38981793b88f4f52086d7713d111f68` |
| `geometry_20261114_constrained_collocation.py` | `70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8` |
| 原完整 FD 消费者 `geometry_20261114_constrained_trust_response.py` | `7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78` |

新入口在导入冻结选择函数之前保存原函数引用，避免包装后的递归。它从已核 SHA 的 `full_metric_projection_warm.main.choose` 抽取**完整原函数正文**，核对包括内部函数在内的 AST 与冻结源逐项相同，再只绑定新的闭包环境。记录正文 SHA 和 AST SHA；不执行旧 producer 的 `main()`，不重新实现或删除其中的 C/H 比较、R265/R267 后验、最终原 $A/B$ 回读和数组保全。

十二查询入口在 `main()` 内会重新设置 `engine.local_halfspace_projection`，所以新源包装的是它实际引用的 `support.fixed_support_projection`。原 C 投影只调用一次。新源只在原完整 H helper 的两个 `_pcg` 调用位置提供 QR 实现，退出时恢复所有 Python 槽；磁盘上的冻结源不改。

## 3. 唯一线性化、延迟 QR 和原残差

新 `CapturedLinearization` 只代理一次原 `CompleteLinearization` 构造；原算子验证仍运行，实际选择阶段使用它返回的同一个 $A$ 对象与固定 weights。weights 采用与原算子相同的 `np.asarray` 引用，使因子每次输入 SHA 重核同时检查原 live $W_r$。QR 直接消费该实例的 `L/R/P/BY/BC/BP`、入口核映射和 $S$，不重新计算节点 J、边界 J、ODE 或当前场。

完整 square-root 模块分解 $[A;\lambda I]$，保留全部 pure-global 行的累计 QR、每个物理坐标恰一次的正则行及全局正则行恰一次。可选 `--qr-column-preconditioner original-C` 只作显式列变换 $t=Cz$，此时分解的是 $[A;\lambda I]C^{-1}$；原坐标目标和正则项不变。默认 `none`，不存在隐含列变换。

完整精确实数能量不变量和边框正反代证明见 [R268](../results/R268-complete-regularized-chain-border-QR.md)，底层输入、因子布局和浮点范围见 [完整正则 block-QR 接口](2026-11-14-complete-regularized-block-qr-interface.md)。这些证明不把实际浮点 QR 误差宣称为零。

第一次实际请求逆时才初始化、因子化；最多一次 factor。后续 center 和至多 32 个活动行右端重用它。每次返回候选都通过原 `model.proxy_A` 完整读取

$$
r_H=A^T(Az)+\lambda^2z-\mathrm{rhs}.
$$

因子内部的 $R^TR$ 残差另外报告，不能替代此原残差。冻结重构算子还对相同候选和相同原 $Az$ 各执行一次额外 A、AT 读取，检查所传 live 算子与冻结原算子的实际 action 差异。新计数代理只在原 reference action 外记录调用与完成次数，不改变输入、返回值或算术。

`--full-h-inner-relative-tolerance` 仅标记内部求逆的原残差诊断；未达此相对量不被冒称精确逆，也不新增科学接受门。有限返回向量仍只是完整 H helper 可选的子空间基，Gram、原模型梯度、所有 $B$ 行、非负乘子和后验继续由冻结 helper 按完整模型实际计算。

## 4. 失败、预算和 `started=False`

若无预算、QR 因子未完成、三角求解失败或原读回不可用，入口不调用旧 PCG。它返回该调用原封不动的 `initial`，并报告 `started=False, converged=False, original_residual_verified=False`。

冻结 helper 对 center 的初值恰为原 $z_0$；`started=False` 不把它添加成新的中心基。对活动行的初值为零，冻结 helper 在 `active.append` 和 `basis.add` **之前**检查 `started` 并结束本次增基。因此零初值不会被误当成已求得的行逆。原 C 候选及已经真实得到的有限基保留。失败也不触发第二次 factor 或大预算 PCG 重试。

| 选项 | 默认值及含义 |
|---|---|
| `--full-h-budget-seconds` | 必填，有限正数；完整 H 备选的独立可选工作时间 |
| `--full-h-trial-reserve-seconds` | 必填，有限非负数；从原总预算中预留给原回溯及保全 |
| `--full-h-max-active` | 32，允许 0–32；活动约束上限 |
| `--full-h-max-products` | 1200，保留 helper 的完整 H action 上限；不把 QR 因子运算冒算成这些 action |
| `--full-h-inner-iterations` | 64，保留原 helper 接口范围；QR 实现明确不使用 PCG 迭代次数 |
| `--full-h-inner-relative-tolerance` | $10^{-8}$，原残差的内部诊断标签 |
| `--full-h-dual-sweeps` | 200，有限子空间 dual 扫描预算 |
| `--qr-column-preconditioner` | `none`；另可显式选 `original-C` |
| `--qr-store-factors` | 默认关闭；开启才把完整因子保存在独立 artifact 子目录 |

有效 H 截止时间仍使用冻结选择器的

$$
\min\{t_{\rm now}+T_H,\ t_{\rm original\ deadline}-T_{\rm reserve}\}.
$$

因子按完整 front 之间检查截止时间；已经开始的 solve 会完成其强制原残差读回并如实记录越界。完整 H helper 最终证据保全同样保留其原有的有限收尾语义。总预算不足时使用原 C，不保证能开始 H 计算。

一次完整 factor 的数组约 1.49 GB；同时保留原完整线性化约 1.28 GB。还需当前状态、十二查询 B、既有 LSMR/投影数据和 Python/BLAS 内存，因此这两个数字不是整个 job 的 RSS 上界。原模块记录实际峰值 RSS、因子 SHA、初始化/分解/求逆/输入重核耗时。BLAS 单线程沿原设置。没有通过本地数值估算宣称 Actions 实际耗时。

## 5. 原验收和当前身份

冻结选择器仍先取得真实 C 候选，再比较两者在**同一**完整 $f$ 下的实际值。H 只有在原完整 $A/B$ 回读有限、全行 slack 非负、原 $g^Tz<0$、原预测下降正且实际 $f$ 更小时才能被选中；这些都是被复用的原选择器条件。最终方向再执行原 17 档真实非线性回溯、所有原节点/mid/RMS/rho 域检查及原 scalar/BC 读取。只读 midpoint observer 同样保留。

R265/R267 的多证据点下界、完整 stationarity/complementarity 以及最终可行方向分开保存。浮点读数没有被升级为严格区间后验，有限基中问题的解也不称为全 QP 最优。

当前 producer 新 schema 是 `exact-constraint-twelve-query-complete-QR-H-alternative-warm-v1`。原父 `resume_producer` 子树不修改；只给当前 intent/status/warm 补新入口、QR、选择器和完整 source ledger。当前 fixed-support 字段明确移为 `baseline_C_...` 范围。新 FD 入口只把原消费者接到这个真实 schema，并扩展来源账；所有原方向、步长、Richardson 公式和 $5\times10^{-5}$ 门不改，仍是已完成 T112 零高度 J 的显式 affine 代码核验，**不声称求解当前新 H 的 nonlinear native tail**。

## 6. Actions 调用

以下路径与原总预算由 workflow 显式提供；`ACCEPTED/PREPARED/TAIL_ANCHOR/TAIL_CONFIG` 必须与现十二查询实际主线相同。首 request40 的 H 预算保持 actual30 所用的 300 秒、最多 16 活动行、1200 个 helper H action，并预留原回溯 90 秒；`qr-column-preconditioner=none`。这保留已选的工作预算，实际同模型 C/H 比较来自本次同一个父37场，不把不同父场/查询的 actual30 结果当受控比较。输出目录须全新，入口在原 fresh-output 检查之后才创建 QR 数组目录。

```sh
python "$COMPUTATIONS/geometry_20261114_twelve_query_qr_projection_warm.py" \
  --accepted "$ACCEPTED" --prepared "$PREPARED" \
  --tail-anchor "$TAIL_ANCHOR" --tail-config "$TAIL_CONFIG" \
  --resume "$ACTUAL37_WARM" \
  --expected-resume-sha dd83748341c8d6172096fc644361018be7b29d856de621a0b333104d20aafdb8 \
  --parent-status "$ACTUAL37_STATUS" \
  --expected-parent-status-sha 37e70ad5a3c9ef828d93bcbf371b3a107e3890026731d7944d98e370987d29e0 \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --angles 4096 --jac-workers 2 \
  --budget-seconds "$TOTAL_BUDGET_SECONDS" \
  --full-h-budget-seconds 300 \
  --full-h-trial-reserve-seconds 90 \
  --full-h-max-active 16 --full-h-max-products 1200 \
  --full-h-inner-relative-tolerance 1e-8 --full-h-dual-sweeps 200 \
  --qr-column-preconditioner none --out "$RUNNER_TEMP/twelve-query-qr-warm"
```

只有该 warm 实际存在并按原 status 标记取得真实下降后，才用其实际 `warm-001.json.gz` 进入原 FD：

```sh
python "$COMPUTATIONS/geometry_20261114_twelve_query_qr_projection_response.py" \
  --accepted "$ACCEPTED" \
  --prepared "$RUNNER_TEMP/twelve-query-qr-warm/warm-001.json.gz" \
  --tail-anchor "$TAIL_ANCHOR" --tail-config "$TAIL_CONFIG" \
  --angles 4096 --out "$RUNNER_TEMP/twelve-query-qr-response"
```

## 7. 输出和出版

原 warm/status、model、observer、domain-operator、`full-H-result`、`full-H-versus-C-comparison`、R265/R267 最终证据沿冻结消费者保留。新增：

- `block-qr-live-model-binding.json`：唯一 live 实例、实际 $A$ 形状及 weights/S/inlet/b/z0/c 和完整 B 身份。
- `block-qr-inverse-accounting.json`：至多一次 factor、各请求/失败、完整因子报告、helper action 及额外 reference A/AT 调用账。
- `block-qr-inverse-###.json`：每次实际返回的原完整 residual、factor residual、计时和原数组引用。
- `block-qr-inverse-array-manifest.json` 与 `block-qr-inverse-arrays/`：实际 rhs、返回候选及两种 residual 的完整分块原数组。
- 可选 `block-qr-factor/`：完整因子和因子状态；默认只有身份与统计，不导出大因子文件。

调用次数按**已进入 action 的调用**统计，包括中途抛错的调用；额外 reference 同时记录成功完成数。总账的范围是 H helper 加这些额外 reference，不冒称包含先前 LSMR、C 候选和外层选择器的所有 action。成功返回的完整 H 读回计入 helper H 账；异常半途的 A/AT 调用仍在各自调用账中，不虚报成功返回。

`full-H-arrays/`、`block-qr-inverse-arrays/`、可选 `block-qr-factor/` 应作为 artifact-only 大数组树保全，保留其小 JSON manifest/摘要到公开 notes。不能因为单 Git 文件或总出版容量限制而否决数值步骤，不能把仅存 hash 说成已保存所有因子字节。

本文没有触发运行、增加验收门或把当前未接受 warm 宣称为本课题完成。实际结果必须按其回执另记。
