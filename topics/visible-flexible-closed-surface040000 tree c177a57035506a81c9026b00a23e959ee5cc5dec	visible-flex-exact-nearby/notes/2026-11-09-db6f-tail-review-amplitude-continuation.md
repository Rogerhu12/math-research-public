# 同一物理度量下的尾边值振幅延拓：独立审查

审查人：`/root/tail_theory`，2026-11-09。**结论：本文所绑定的控制器、客户端差分及实际输入的轻量独审 PASS。** 这是已审数值流程，不是任何一次真实尾求解的成功报告，也不保证延拓到达 $s=1$。作者 `/root/coupled_prefix` 在本审查完成后执行真实计算，结果由其单独保存。

## 1. 冻结范围

被审文件及 SHA256：

| 文件 | SHA256 |
|---|---|
| `scripts/db6f-prefix-tail-amplitude-continuation.py` | `23f75c9ecc2825e4a8314468775c40b06b6b47439edd0d0ed9a69a9fb5e298a9` |
| `scripts/db6f-prefix-tail-continuation-client.py` | `cd9b25521427dcefebd5baddcf6a105c58c53f495cf8692fb725d49e4558a564` |
| `notes/2026-11-09-db6f-prefix-tail-amplitude-continuation-method.md` | `3fae1b9c9c28a5942e527cacf2710d5de1edd29b0418657441bb339d9334b77d` |

审查实际输入为 `db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from-affine-tail-config.json`（SHA `c10cc42bca5a30922ce29f2cb8a7f9f65cdab66d3f525b96fdf4b6a0396414df`）及辅助 prefix `db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz`（SHA `4a13e13223047c995acd855db93007ed57bf0471214229c62adb5d7543425190`）。两者均在本题 `notes/2026-11-09-` 下。

已独立逐项检查辅助 CP 的 21 项 `physical_tail_parameters` 与配置相同。原离散参数是 M15、N256、physical depth12、每段 p8/s32、原尾残差容差 $2\cdot10^{-9}$，原 `maxIterations=36`。配置未显式提供 `projectionFloor`；它沿用未变 core 的默认 `.05`，不是把缺失键当作零。源 worker/core/split 的哈希也在机读审查中绑定。

## 2. 模态与物理高度

控制器直接读取辅助 CP 的 `predicted_cut_height`。该向量已是原 DN 接口的物理高度系数，包含 prefix 的 $\sigma q$ 因子。原 `DN.solve(height)` 将它除以 $r_{\rm cut}^4$ 后送入 shooting；控制器没有重复转换。

对于保存下标 $j=0,\ldots,M-1$，数值请求使用

$$
H_j(s)=s^{j+1}H_j^{\rm target}.
$$

`np.arange(1,M+1)` 与这个下标约定相符。物理角频是 $3(j+1)$，不应再把指数乘 3。中间向量由浮点运算计算并按实际请求保存；没有把浮点幂运算说成严格实数恒等式。

特别地，`s==1` 分支显式执行 `goal.copy()`，最终带 tangent/audit 的请求也独立执行 `goal.copy()`。所以最终目标不是累计加步、反复缩放或舍入后的中间向量。在此实际输入中，首、末系数分别约为 $-0.0008134333256853195$ 和 $8.873136367407456\cdot10^{-16}$；初始 $s=.25$ 只把边值变小，没有改背景参数。

这些中间边值通常不等于原完整 prefix 的切口。中间成功只支付该边值下的有限尾 DN，原完整 prefix 仍未解。即使目标 DN 成功，下一步也必须由真实耦合器重新求解完整 prefix/tail 边界条件。

## 3. 原求解器与回退

逐行核对了原 worker 的 `last` 更新和 warm 构造：

1. 全新运行只移除配置中的 `initialCheckpoint`，用原 `tail.initial` 建立小目标的线性初猜。控制器改写的其他键只是记录文件路径。
2. 原 worker 的 warm 状态由 `map` 复制；原 `tail.solve` 又逐行复制到新的 `Float64Array`。失败尝试不能修改保存的旧成功数组。
3. worker 只有 `sol.converged` 才赋值 `last=sol`。异常或正常返回但不收敛均保留前一成功状态。
4. 每次中间请求 `jacobian=False,audit=False` 只省掉额外端口 tangent 和源几何审计。原 shooting 每次 Newton 所用的变分 Jacobian、RK、moment root、guard、line search 和归一残差均未改。
5. 控制器进一步要求 `converged` 为真且有限、非负的 `residual` 严格小于原配置容差。它没有把较大残差重标为成功。

首个小目标失败时，下一请求的 $s$ 减半；已有成功 $s_*$ 后，失败目标增量减半为 $(s-s_*)/2$。后续 warm 仍来自原 worker 保留的成功状态，失败响应只留作诊断。成功时根据 history 长度调整下一步长，这只决定下一个尝试的边值，不改变任何一次原方程求解的接受规则。

到达最大尝试次数或最小步长时，输出状态分别为 `UNCONVERGED_CONTINUATION_ATTEMPT_LIMIT` 和 `UNCONVERGED_CONTINUATION_STEP_LIMIT`。它们都不构成无解结论。运行预算是实际有限计算的保护边界，不是数学延拓定理。

## 4. 目标求解、审计和保存

中间目标 $s=1$ 的第一次真实 DN 收敛只设置 `target_reached=True`。随后 `audit=True` 强制绕过客户端的同高度缓存，并显式请求原 `jacobian=True`。只有这一调用成功，才设置 `target_audited=True`。最终状态名称仍含 `PREFIX_STILL_UNSOLVED`。

若最后 audit 调用失败，异常记录保留已经发生过的目标 DN 收敛，`target_audited` 保持假，状态为未收敛异常。没有用已达到目标的旧响应冒充最终审计。自然进程退出码也不单独证明数值成功，必须读上述状态、残差与响应。

派生客户端相对已审 `db6f-prefix-tail-trial-client.py` 的源码差分仅为两处：正确记录自己的文件名；把完整响应从直接独占写入改为临时文件写入/fsync 后以 hard link 原子发布，再删除临时名字。输入请求、缓存、worker、响应解释和异常规则全文相同，独立脚本以反向文本替换检验了这一点。hard link 拒绝覆盖旧目标文件；发布前数据已经完整关闭。

每次收到完整响应后才关闭该次 trace/trials 名称，再发送下一请求。progress 原子替换；初始 input binding 不覆写；每个响应的 hash 与 call 编号进入账本。既有迭代 recovery 仍明确为未收敛中间态。

## 5. 独立轻量执行核查

独立脚本 `scripts/db6f-tail-review-amplitude-continuation.py`，SHA `daf7ea24b0511ddbfc4b2ecda39156b1b5863c63c0d8b35b4310ae3c6b5cb85f`，实际退出码 0。输出 `notes/2026-11-09-db6f-tail-review-amplitude-continuation.json`，SHA `7c208e3aed06f24e6f217ec12d6068a9bba5772500815613ed82a08ec2d5e87f`。

它运行冻结控制器的原 `main`，只把外部 worker 接口替换为确定性 mock，分别覆盖：

| 控制流程 | 请求数 | 核查结果 |
|---|---:|---|
| 起始失败、成功、已成功后再失败、回退后达到目标 | 11 | 回退目标正确，最后单独 audit，最终 prefix 仍未解 |
| 所有小目标失败 | 11 | 正确触发最小步长限制，不报告目标成功 |
| 尝试次数耗尽 | 2 | 正确未收敛状态 |
| 目标第一次成功，但最后 audit 失败 | 8 | `target_reached=True` 与 `target_audited=False` 保持区分 |
| 从合法 $s=.5$ 响应恢复，首尝试失败后继续 | 10 | `.625` 失败后退至 `.5625`，随后正常走到目标 |

每一例都检查实际目标向量、原配置除记录键/warm 键外逐项不变、全调用日志独立关闭及最后目标逐项等于原数组。初始四分之一缩放另外以 `ldexp` 独立核对每一模，避免只用同一表达式自验下标。

**这些 mock 执行没有计算真实尾、没有认证真实 root，也不验证原 ODE 的数值精度。** 原 worker 数学与只增记录分支的独审见 `db6f-audit-m15-entry-diagnostics`；本报告新增的是延拓控制层和保存语义。

## 6. 范围结论

本方法可以作为原问题的数值初猜路径：物理度量保持冻结，最终目标保持原物理高度，原 guard/残差标准保持。它没有声称所有中间边值一定可解、正支路必能延到 1、失败意味着不存在正支路，也没有支付径向 BVP、完整 prefix 联解、实际全域 metric 或无限非线性尾的存在性。

真实运行的每个已收敛或失败步骤应继续保存，并由主会话更新 HANDOFF。后续只有真正达到目标、完成原审计、完成真实 prefix/tail 校正的候选，才能进入新的全 XYZ 导出与同 $g$ 连续证书。
