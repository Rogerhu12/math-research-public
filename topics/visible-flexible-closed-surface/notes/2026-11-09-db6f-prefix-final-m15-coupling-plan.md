# M15 最终目标尾成功后的原前缀联解入口

会话 `/root/coupled_prefix`，2026-11-09。**条件式准备；尚未启动本计划的求解，M15 完整前缀仍未解。** 当前 continuation02 由 root 持有工具会话。本稿没有将其正在产生的状态认作成功。

## 1. 允许接续的唯一输入

目标仍是已冻结的 `flat17` 度量和同一 affine M15 前缀：

- prefix restart：`2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz`，SHA256 `4a13e13223047c995acd855db93007ed57bf0471214229c62adb5d7543425190`，连同它的两个 gzip 系数块；它继续明确标为 `UNSOLVED`、`actual_nonlinear_tail=False`。
- 原实际前缀命令绑定：`2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from-affine-input-bindings.json`，SHA256 `457d4a5fbbb3730eafb2b4f6f8d4fc5429676d877e7a346d59b49fcf1b930913`。
- 真尾初猜只能来自 `2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02` 的最终目标记录：请求严格为保存的 `predicted_cut_height` 原向量，`jacobian=True`、`audit=True`；原 shooting 残差小于 $2\times10^{-9}$，705 项原 DN Jacobian 有限，完整 source audit 已实际返回。

准备器 `scripts/db6f-prefix-prepare-final-m15-coupling.py` 只读 JSON/gzip、核 SHA256，写新 config/启动绑定，不导入数值求解器或启动子进程。它要求已闭合的 progress/reproduction 全字段一致，controller 状态为 `TARGET_DN_CONVERGED_AND_AUDITED_PREFIX_STILL_UNSOLVED`，`target_reached` 与 `target_audited` 都为真、`last_converged_scale=1`、原 worker exit code 为 0。另要求 root 实际观察工具自然退出的记录，绑定该最终 progress/reproduction/config/response，不能用 `/proc` 不存在代替退出证据。

原配置、冻结源、最后真实 $s=.25$ warm、continuation02 恢复绑定和重启核查的全部文件一起入新清单。准备器比较所有原物理与数值设置，仅允许 `initialCheckpoint` 和日志/恢复文件路径变化；$M=15,N=256,\text{depth}=12,\text{parts}=8,\text{steps}=32$、36 轮上限、tol $2\times10^{-9}$、guard $.05$ 均不改变。`audit.actualMetric` 保留其**有限 source-jet 诊断**含义，不当作全 XYZ 的连续 metric 证书。

## 2. 已实际核查的重启几何与 cut 高度

`scripts/db6f-prefix-check-final-m15-restart.py` 已以原 wrapper、原构造器、原 `preserve_restart` 实际执行并自然 exit 0；没有创建 tail client、没有调用 shooting/RK/`solve_bvp`。报告为 `2026-11-09-db6f-prefix-final-m15-restart-check.json`，SHA256 `c9390004df97d2db00e7ba2ac87eba95a6f256be95ea4f3ed12368ed4e13d2c6`，44 个源与输入绑定。

| 检查项 | 实际结果 |
|---|---:|
| 原与重启节点数 | 2633 / 2633 |
| 全部物理网格节点 | 逐位相同，最大差 0 |
| gauge $q_g$、warp reference | $.1$、$.1$ |
| 恢复的实际入口 support 振幅 | $.09999976661892393$ |
| 桥符号 $\sigma$ | $-1$ |
| 重启参数最大浮点重建差 | $1.1811874449461218\times10^{-17}$ |
| 入口系数残差 | 0 |
| 最小数值 / 物理跨度 | $2.1515810365\times10^{-5}$ / $4.3500146760\times10^{-5}$ |
| 重启 cut $H$ 与旧真实 DN 请求 | 逐位相同 |
| 重启 cut $H$ 与保存的 affine 目标 | 三个槽有差，最大 $1.6940658945086007\times10^{-21}$ |

原初始化使用
$$
H=\sigma q_g Y_Z(s_{\mathrm{cut}}).
$$
物理 support 振幅由 $p_0=\log(q_{\mathrm{actual}}/q_{\mathrm{seed}})$ 恢复。$q_g$ 是固定归一化，不是把实际 support 振幅锁定成常数；15 个原自由参数仍全部交给前缀 BVP。保存物理网格经原 chart 反解/正解和节点合并后本例逐位保持。局部入口修正的支撑在前半 ramp 内，cut 处为零；不改变物理度量。

最终 continuation 的 $s=1$ 请求复制保存的 affine 目标原字节；前缀重启则由保存 PPoly 重新求值。两者上表中的微差不得偷偷消去。新 worker 从真正的最终 response 读取 `response.checkpoint`；其初始 ratio 约为 1，随后按原代码为全部模加入
$$
\Delta Q_j=H_j/r_{\mathrm{cut}}^4-Q_{0,j}^{\mathrm{initial}}
$$
的有限线性 warm 解，再以原方程真实 DN 检验。因此不覆盖前缀 cut 值，也不把旧 response 改标签为新高度的解。

新 config 来自原 from-affine actual 配置，**不从零态 pilot 复制**。保留 `correctInitialBoundary` 缺省真；准备器拒绝出现该键的意外覆盖。全部高模请求非零，原 `harmonicAmplitudePredictor` 的“高模全零”分支不触发。`tail_theory` 已对这条原 worker 管线作只读接口复核：checkpoint 只提供 states/parameters/cutHeight，不覆盖本次 config flags；fresh client 缓存为空，微差仍经真 DN。

## 3. 原 argv 与真实验收

唯一变化是 `--tail-config` 和 `--out-prefix` 的新路径。继续用原 `db6f-prefix-flat-trial-coupled.py`：它只是把 shared client 导入重定向到已审 trial diagnostic client，BVP、BC、RK、root guard、outer 检验均没有变化。

| 选项 | 保持值 |
|---|---|
| 物理 profile/chart/linear port | 原命令所绑定文件 |
| `--restart` | 上述 affine M15 CP |
| `--amplitude / --warp-reference` | `.1 / .1` |
| `--modes` | `15` |
| prefix `--angular / --audit-angular` | `512 / 1024` |
| tail angular quadrature | `256` |
| `--nodes / --max-nodes` | `1601 / 4500`；原 saved-mesh 路径实际用 2633 初始节点 |
| `--tol / --bc-tol / --physical-bc-tol` | `2e-9 / 1e-8 / 2e-11` |
| 其余旗标 | `--fixed --warmup-scales --lagged-tail --preserve-restart-mesh` |

`--warmup-scales` 后面立即接 `--lagged-tail`，所以列表为空；不在已有目标真解之后重新请求一串小幅边值。原 `solve_with_actual_tail` 首先在真实重启高度取原 DN/J。每次 inner BVP 只暂用该点的 affine slope DN；成功后必须在候选高度重新调用真实 DN，再以原 `o.bc` 验收。原 outer 上限 8 次、缩放 BC 门 $10^{-8}$ 和 physical BC 门 $2\times10^{-11}$ 都保留。

实际运行完成后不能只看工具或 Python exit 0：原 main 会捕获数值异常并写 summary。至少要同时核

1. `solver_success=True`，无 `error`，原 collocation residual 达到原 tol；
2. 最后 `actual_outer_checks` 是真 DN 校正，原 BC 残差达门，不能拿 inner affine 成功代替；
3. 最后 `seam_audit` 真正调用 `jacobian=True,audit=True`，对应保存的 tail response `converged=True` 且残差达原 tol；
4. 单列 mean/nonmean 两 jet mismatch、source metric、实际 XYZ metric；不能把 Darboux/fullTensor 当 metric，也不能挪用旧 M8/M12 的连续证书。

后续还需同 $g$ 的最终 tail N512 真校正、实际 XYZ 表示与公共 C²接缝、连续 metric/曲率/reach/矩证书和未参与优化者全流程。此准备不会代付 README 第 5 门或精确无限尾存在。

## 4. 条件式操作入口

现在只检查是否就绪，不写文件、不启动：

```bash
python scripts/db6f-prefix-prepare-final-m15-coupling.py --check-current-gate
```

root 观察 continuation02 真成功自然结束后，保存其实际工具退出记录，使用与已闭 recovery 记录相同的 schema：`status=observed-process-completed`、`actual_exit_code=0`、`observer=/root`、真实会话号/观察时间/stem，以及至少 progress、reproduction、config、final response 四件的 SHA256/bytes。再在本题目录运行准备器：

```bash
python scripts/db6f-prefix-prepare-final-m15-coupling.py \
  --observed-execution notes/2026-11-09-db6f-root-amplitude-continuation02-observed-execution.json
```

这仍不会启动求解，只生成新 stem `2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-after-amplitude` 的 `-tail-config.json`、`-launch-gate.json` 和 `-input-bindings.json`。root 核对绑定后，在仓库根目录以输出中的完整 `actual_launch_command` 运行原 `db6f-prefix-run-bound-command.py`；stdout/stderr 写该 stem 的 `-run.log`。长进程工具会话继续由 root 持有。

实际风险是目标 $s=1$ 的 DN 尚未到达，且一个已解固定 cut 的尾并不保证随后自由 cut 的联解收敛。原 BVP 自适应节点还会有已观察过的内存峰值，正式启动应由 root 协调正在运行的任务。若最终门尚缺，准备器明确拒绝生成 ready launch，不改 guard、容差或物理问题来绕过它。
