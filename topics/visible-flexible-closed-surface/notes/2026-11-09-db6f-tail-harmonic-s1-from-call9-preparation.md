# call9 到 s=1 的外部 harmonic warm：实际纯构造记录

日期：2026-11-09。作者：`/root/tail_theory`。

状态：**输入已构造，求解次数为零，候选明确 UNSOLVED。** 原 worker、controller 和活跃 continuation 均未修改。本记录不声称新状态满足原 root guard、stage matching、Robin/cut 方程或任何 metric/曲率门。

## 1. 与已冻结静态方案的关系

先前静态接口稿 `2026-11-09-db6f-tail-harmonic-warm-interface.md`（SHA `194b992a7f13d73138b1c288e6e3c6e84d81af3a3b2f3561c3452ce64fbca5aa`）描述了逐模初猜、原 loader/remesh、请求标签及失效字段。该稿及其来源账本保持原字节。本轮在得到后续实施指令后，只新增纯数据构造器和输入产物，不运行该稿讨论的任何求解入口。

构造器为 `scripts/db6f-tail-prepare-harmonic-s1-warm.py`，SHA `66094a71fd7669faf15e78584c55159e9cd244479b1dada6cffe476181ae75f6`。其 imports 仅为 argparse、copy、gzip、hashlib、json、math、pathlib 和 NumPy；没有导入或调用 solver、client、geometry、flow 或 subprocess。

## 2. 实际来源、变换和观察结果

源是已闭合 continuation02 call9，$s_0=13/16$，响应 SHA `78d7e112d4823a717d0f46549b9f88d11872dbe390f40f70d295278ed50320e8`。它的原残差为 $3.796278258536727\times10^{-10}<2\times10^{-9}$；其原请求没有 audit。构造器核对了对应 root 闭合审计、原 66 件定义清单和该闭合记录的 8 件依赖，并复核响应记录的 8 项源码绑定。去重后新输入绑定 **77 件**来源文件，包括本构造器、原目标和静态方法。

新目标为固定 affine prefix 的 `predicted_cut_height` 的 **`goal.copy()`**；目标来源 SHA `4a13e13223047c995acd855db93007ed57bf0471214229c62adb5d7543425190`。没有把旧请求累计乘幂当作 s=1 目标。

对 865 个节点，使用同一个 NumPy binary64 因子表

$$
\gamma_j=\left(\frac{1}{13/16}\right)^j,\qquad j=1,\ldots,15,
$$

分别乘每行前 15 项 $Q_j$ 和后 15 项保存坐标 $\Pi_j$。指数为存储模态 $j$，不是角频率 $3j$。ratio 和 15 个实际因子的 hexadecimal 浮点表示、NumPy 版本及精确运算顺序保存在输入和 preparation JSON 中。

实际生成的 `states` 是 $865\times30$ 的有限数组；`rawNode` 原样保留，`rawStates` 从新 `states` 按该 13 个索引直接抽取。完整 `checkpoint.parameters` 保持源对象逐值、逐类型相同。构造器没有重新求 mean、高度 jets、slope、root 或残差，也没有继承任何旧结果字段。

本轮命令的真实工具退出码为 0，脚本起止 SHA 相同。可复现命令为：

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/db6f-tail-prepare-harmonic-s1-warm.py \
  --out-prefix notes/2026-11-09-db6f-tail-harmonic-s1-from-call9 \
  --pilot-prefix notes/2026-11-09-db6f-tail-harmonic-s1-original-pilot
```

重复构造必须换两个独立、尚未使用的输出 stem；脚本拒绝覆盖。输入 warm 的字节不依赖这两个输出 stem，因而独立同源重放可以直接比较 warm 文件 SHA；配置和 interface 的路径字段则会随 stem 改变。工具观察单列于 `*-observed-execution.json`，不以退出码冒充任何数学求解成功。

## 3. 已生成的四件输入产物

以下名称均以 `2026-11-09-db6f-tail-harmonic-s1-from-call9` 开头。

| 后缀 | SHA-256 | 字节 | 作用域 |
|---|---|---:|---|
| `-input.json.gz` | `c6a4c0e504802885f358c340c1a23a34355476ee4d241e3ea6b14069b2b4f927` | 270624 | 顶层 UNSOLVED warm；无旧 response、jets、Jacobian、audit、residual 或 history |
| `-config.json` | `6f1398220b3317c3e481b43950eea7b81d6de301a7047069e26821d83db22ac3` | 3000 | 原配置只换五个输入/输出路径 |
| `-interface.json` | `4cf0ddc2b6cfa0b742e5f8bfb04d57d25226388453ac8d613d24ce0ebbffa1ea` | 21691 | 未执行的单请求接口、绑定及关闭方式 |
| `-preparation.json` | `e1b3616a857a4d294066e257e67252bb57a3e5138a229b84fe2dc656f0ac4190` | 4562 | 实际构造方法、有限性/布局检查及上述输出哈希 |

`checkpoint.cutHeight` 明确是 s=1 的**请求目标标签**，不声称等于未经评价的新状态物理 cut jet。原 loader 以此设置内部旧请求标签；发送相同 goal 时比例为 1，不会再次统一放大这个已逐模变换的 state。原 `correctInitialBoundary` 默认启用，随后仍以原 $c^4$ 规范计算并补偿 cut 差异。

参数对象中保存的旧 I/O 文本仍仅表示来源。实际未来运行使用新增的 config，不能把 `checkpoint.parameters` 当作运行配置执行。新 config 的唯一变化是 `initialCheckpoint`、`traceFile`、`iterationCheckpointFile`、`trialDiagnosticFile`、`trialStatePrefix`；其余字段以 canonical JSON 作逐类型比较。原 36 轮、tol $2\times10^{-9}$、默认 floor 0.05、默认边界修正和 M15/d12/p8/s32/N256 均保留。

## 4. 未来单次原求解的接口建议；本轮未执行

建议使用原 `db6f-prefix-tail-continuation-client.py`（SHA `cd9b25521427dcefebd5baddcf6a105c58c53f495cf8692fb725d49e4558a564`）创建一个 fresh `WeightedTailPort`，使用新增 config、相同 source-root 和独立 record prefix。仅发送一次 `solve(goal.copy(), jacobian=True, audit=True)`；无论成功失败均在 `finally` 中调用 `close()`，然后记录实际 worker `poll()` 结果。

这是对先前静态稿中可用于普通 warm 的 trial-run 入口的进一步限定：原 `db6f-prefix-tail-trial-run.py` 写死 `audit=False`，**不能**拿它的输出当作这次要求的 audited 请求。新的独立薄 runner 由另一个代理实现和审查；本构造器不导入它，也未生成或启动运行脚本。

root 若选用不同的未来 runner 输出 stem，可以在该 runner 自己的独立配置中仅更新这五个 I/O 字段，仍须逐项证明原数值和物理定义未变；不能覆盖本轮已冻结的 prepared config。未来真实响应必须独立检验原收敛门、目标、705 项 Jacobian、17 键 cut jets、8 项 source audit、完整 CP 及来源。即使该独立 finite DN 请求成功，它也不是完整 prefix 联解、连续 XYZ 认证或 README 完成。

## 5. 防止元数据误用

新 warm 的顶层状态是 `UNSOLVED_HARMONIC_WARM_ONLY`，`preparation_only=true`，`actual_solver_runs=0`，仅含 `checkpoint` 与明确来源/变换信息。旧收敛标志只在 preparation 的 **source_observed** 项解释旧 call9，不属于新候选。旧 response 外壳从未复制，避免原 loader 的优先级误选旧 checkpoint。

不得将新 warm 传给要求成功响应的 `--resume-checkpoint` 入口，不得为了通过该入口伪造 `response.converged`。本轮也没有调用现有 final-M15 身份门；未来新运行来源必须按其真实来历进行独立核查，不能套用 continuation 已完整结束的状态。原活跃 continuation 继续独立运行。
