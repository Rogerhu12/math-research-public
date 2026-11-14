# 零初态八轮对照的关闭证据独核

审查者 `/root/tail_theory`，2026-11-09。**PASS：原文件 / 来源 / 配置 / 目标 / 日志的独立只读核对。数值状态仍为未解。** 本审查没有重求原 DN，没有新的 root 或 RK 调用，也没有把工具退出码当成数学成功。

root 记录自己实际观察终端 session 18291 自然 exit 0，保存的 worker exit code 也为 0。审查者没有重新观察该工具会话，而是重新读取其已关闭响应、日志、复现记录和来源文件。正式响应 `prefix-zero-initial-s025-original-pilot01_tail_0001.json.gz` 的 SHA256 为 `7a5f0b57fabdd58000905d61644513a292ab5f7d6b8fe7ee0fc0375866301442`。

## 1. 同一问题和明确的零初猜

审查者独立复核全部 61 个 launch 绑定与实际 response 的八项直接来源 SHA，核输入配置、实际诊断配置、response config 的带类型 canonical JSON 一致性。原 M15、N256、p8、depth12、steps32、guard `.05`、原容差 $2\times10^{-9}$ 保持，迭代预算明确为 8。

输入 shape states 全零，但 `cutHeight` 标签仍是非零请求。实际请求、seed 标签和输出 checkpoint 标签逐项相同；另从冻结 affine 目标用二进精确缩放 `ldexp(H_j,-2(j+1))` 重算，确认是同一 $s=.25$ 的逐模目标。`correctInitialBoundary` 确为 JSON false，没有隐式加回线性边界初猜。

输出 865 个 staged state、每个 30 个 shape 槽均为有限实数；13 个 raw state 与 `rawNode` 所索引的 staged state 一致。此处有限性只检查保存的有限离散状态，不代付连续角 / 径向正性或曲面证书。

## 2. 残差和 trial 账本

response history 含八个 Newton 基点。trace 中另外八条 `phase=correction` 只是同一基点的消元诊断，不能与前者相加声称有十六轮。首基点实际记录的 norm、minA、minD 均为 1，与零形状的代数预测一致。

全部 66 个 trial 中，八个标为 accepted，其余 58 个均为 residual-not-decreasing；它们没有被误记为 moment guard 拒绝。每个接受 trial 的 base norm、步长与相应 history 一致，其 norm 严格下降，并等于下一基点的 norm。接受步长依次为
$$
1/32,\ 1/32,\ 1/128,\ 1/128,\ 1/256,\ 1/256,\ 1/512,\ 1/512.
$$

最后一次接受后，原 solver 在预算用完时重新评估当前 state；最终 response、summary、trace response 和最后 accepted trial 的残差完全一致：
$$
0.9163518748162202>2\times10^{-9}.
$$
它不等于最后一个历史基点的较旧残差，这一区别与原 `solve` 的最后重评估代码吻合。输出明确 `converged=false`、`audit=None`。

## 3. 正常退出与保存的异常文字

summary 的 `error` 并非空值：原 client 在完整保存 `converged=false` 响应后，按既有协议抛出 `Weighted finite DN trial failed` 的 `FloatingPointError`；原 runner 捕获它、关闭 worker、写 summary，并自然结束。其 response 自身没有 `failed` 异常字段。

因此，正常工具 / worker 退出、summary 存在此异常文字、有限 solver 未收敛三者一致。审查器最初把 summary.error 误预设为空而安全拒绝；逐行核原 client / runner 协议后修正这一检查，再独立执行全部核对通过，没有改动任何输入、响应或原求解源码。这只是审查器对现有记录语义的修正，不能把它解释成新求解成功或额外的 numerical crash。

## 4. 可复查记录与结论范围

独立只读脚本为 `scripts/db6f-tail-audit-zero-pilot-close.py`，不导入数值 solver。它对以上全部交叉关系执行检查，实际 exit 0；输出为 `2026-11-09-db6f-tail-audit-zero-pilot-close.json`，SHA256 `a7bd5f7625125bcb0e6ce8febdab71ac8548b43fdf3b0919028ba8f421d6567b`。

该结果只说明显式零初猜在这八轮预算内没有达到原容差。不能推出它永远不收敛、解不存在，或整条幅度延拓失败；也不得把这个 `converged=false` checkpoint 计为 continuation 的成功 warm、目标 $s=1$、完整前缀联解或 README 完成。主幅度延拓继续使用它自己最后一次真实成功的状态。
