# 独审：continuation02 闭 call001 的来源与请求核对

审查者 `/root/coupled_prefix`，2026-11-09。**指定已冻结 call001 审查 PASS。** 完整阅读作者检查器，按原命令独立执行一次纯 metadata 重放；另以自有小脚本补核启动选择器、完整响应源集合和 raw/full 节点的一致性。没有新 root、RK、Jacobian、shooting 或 BVP 调用；不把这次核验称为独立重新求解。

作者源：`scripts/db6f-root-audit-closed-continuation-call.py`，7678 bytes，SHA256 `6e43e269c0b5997a4f2cbbcc571c4be2cfddcfba3ccc94f6272e1d1fe4f0d44e`。作者报告 `2026-11-09-db6f-root-continuation02-call001-closed-audit.json` 与本次新输出 `2026-11-09-db6f-prefix-review-continuation02-call001-metadata-replay.json` **逐字节相同**，两者 SHA256 均为 `994d8a9f7e47d2b4200b8c0fab18afa3ff992b139d1320fd34a3fda8d41982c7`。

## 1. 完整代码路径审查

1. 启动绑定的 66 个文件逐一比对实际 SHA256 和 bytes；路径统一到仓库根目录。当前所有实际输入均在本题及其冻结 source-root 内，没有读取旧外部 source-root 冒充同源。
2. controller 当前 config 与其 original config 比较的是完整键并集，只有五个明确的 I/O/初猜路径键允许不同；包括原 tol、最大迭代数、所有物理参数和数值离散选项在内的其余字段必须同值。
3. 原 floor 缺省 `.05` 的处理正确：`cfg.get(key,.05)` 只对缺键使用默认值，显式 `null` 不会通过比较。已绑 `db6f-prefix-tail-trial-core.mjs` 的原构造器确有 `projectionFloor=.05`，并把它传给 engine；保存 CP 的 resolved 参数也为 `.05`。因此此前要求 literal config key 的 setup `KeyError` 是检查器接口问题，没有发生 solver 数学失败。作者保留了原失败记录与前后 SHA/补丁。
4. mutable progress 只用于定位已经旋转成闭日志的 call 行；该行随后完整复制到本次报告。冻结依赖是响应、两份已闭日志、config/binding/launch 等，不把运行中的 progress 本体列成永远不变的文件。
5. 数值边界重建使用与原 controller 同一条表达式：保存下标 $j=0$ 对应指数 $j+1$，$s=1$ 时复制原目标，否则以 `goal * np.float64(s)**arange(1,M+1)` 求值。逐值比较请求和 CP cutHeight，证明的是**相同浮点数值路径**，不是声称这些浮点乘积等于无限精度实数乘积。
6. 本检查器只接受中间 controller 请求 `jacobian=False,audit=False`；尾响应必须 `converged=True`，原 normalized residual 非负且小于 $2\times10^{-9}$，history 末值与该残差相同。所有保存 history 的 minA/minD 有限并超过原 floor。它核查保存记录，没有重新评估这些数值，也不把离散 minA/minD 升格成连续几何界。
7. full states 和 raw states 的值有限；相关 resolved 模数、间距、步数、角积分数、物理深度、子段数和 floor 与 config 一致。作者正确区分 `physicalDepth=12` 与切成 864 个 stage 的 resolved `depth`。
8. 两份闭日志不仅校 hash/bytes，还要求对应 call 的 trace/trials 精确文件名。最终报告明确 `controller_process_exit_inferred=False`，没有从一个 closed call 推断整个正在运行的 controller 已退出。

## 2. 独立补核与通用检查器的范围

作者通用脚本未显式断言以下三个更强的结构关系。本次我对**指定 call001 的实际输入**另以 `scripts/db6f-prefix-review-closed-continuation-call.py` 独立核实，均通过：

- runtime binding 的 `original_config`、`target_prefix`、`resume_record` 实际路径，分别精确等于冻结 launch argv 的 `--config`、`--target-prefix`、`--resume-checkpoint`；controller/client 的 SHA 也等于绑定值。
- response 的 `source_sha256` 集合**恰好是原 client 的完整八个源**，而非仅“存在的每个条目都匹配”。八个实际文件 SHA 均一致。
- `len(states)=resolved depth+1=865`，每个节点宽度 $2M=30$；`len(rawNode)=len(rawStates)=physicalDepth+1=13`，rawNode 严格递增且从 0 到 864；`rawStates` 逐值等于 `states[rawNode]`。

还核实这个中间响应没有 `failed`、没有未请求的 Jacobian、`audit=None`。这些补核只涉及已经保存的 JSON 结构和文件身份，仍不是数学残差复算。

作者脚本当前对响应源采用“逐个成员匹配”，对 finite CP 主要检查 shape 宽度和有限性；如把该脚本作为未来任意候选的通用防错门，可以把上述关系增补成显式断言。本次实际文件都已另行通过，故这不是撤销 call001 报告的理由，也不需重跑原 solver。

## 3. 本次真正支持的结论

| 保存指标 | 数值与范围 |
|---|---|
| controller scale | $s=.3125=5/16$ |
| 原 shooting residual | $2.467580868048873\times10^{-10}$ |
| 原 tolerance | $2\times10^{-9}$ |
| history 基点数 | 5 |
| 最后保存 minA | $.8636068210910816$ |
| 最后保存 minD | $.9973200408208829$ |
| 全 stage / raw 节点 | 865 / 13 |
| 记录的真 DN 响应 | `_tail_0001.json.gz`，SHA `159bfe9470b77b698fbcc14d22a31f0a16a029394c8cd6c39506dfa3bb1d9cd1` |

支持结论是：该已关闭响应与已审原方程/原配置/原数值路径的执行记录一致，且原 solver 报告其有限 DN 已收敛。$s<1$ 仍是 warm-only，尚不匹配完整 affine prefix 目标。检查器、本文及补核都没有产生独立求解、最终目标 source audit、真实 prefix 联解或连续 XYZ 证书。

## 4. 重放入口与输出

在本题目录，使用新输出路径以免覆盖已有记录：

```bash
python scripts/db6f-root-audit-closed-continuation-call.py \
  --controller-prefix notes/2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02 \
  --launch notes/2026-11-09-db6f-prefix-amplitude-resume02-launch.json \
  --call 1 \
  --output notes/2026-11-09-db6f-prefix-review-continuation02-call001-metadata-replay-NEW.json
```

本次原检查器重放实际 exit 0。独立补核脚本也实际 exit 0，输出 `2026-11-09-db6f-prefix-review-continuation02-call001-metadata-supplements.json`，SHA256 `acc7536873ce0fe25c9ab093d6b1f55bd4aaf0eba04ab70139a98376a22a2515`。该脚本只读本次已经完成的 author/replay 报告和它们绑定的闭文件，不调用活动 controller。

本审稿参与的是组件核验；我此前参与过候选优化，所以不将它称为最终“未参与优化者端到端复跑”。
