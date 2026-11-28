# 原 generic 8outer 观察器的真实 ENOSPC 终态

2026-11-28。此前实际运行的工具 session `80294` 在本次 `write_stdin` 真实返回 exit `1`，tool chunk `18df46`。

第一次异常位于 `observe_owned_original_command_v2.py` 第 95 行调用 `event('live_original_process_sample', ...)`，第 55 行向 `events.jsonl` 的 `stream.write` 抛出 `OSError: [Errno 28] No space left on device`。随后 finally 路径第 122 行调用 `event('observer_exception_or_interruption_cleanup', cleanup=owner.cleanup(), ...)`；它的事件文件 open 再次抛出同一 ENOSPC。工具返回的栈显示 cleanup 参数表达式已经返回后才进入事件写入，但没有保存下来的 cleanup 结果可读；这里不伪造该结果、独立子进程返回码或具体科学终态。

最后亲读的实际原前缀进展在 17:07 UTC：879→880→881→883→887→895→911→943→1007 节点，第 9 行 RMS `1.38e-6`、BC `4.82e-9`，原网格规则拟加 128 点。该时仍没有 inner 完整 raw 返回或新 native 响应；仅原全 H 包的严格相同请求复用已登记。该日志不能变为随后完整返回的证据。此终态是执行/观察器写盘异常，不是数学失败。

紧接着的真实目录检查仅见部分 `math-research-public/topics/.../scripts`，原 `held10-design-work`、`held10-analytic-work`、`held10-linear-work` 均不存在。这是可读工作区状态，不据此杜撰删除原因或其他代理作业的退出原因。旧工作区中的唯一 full-H F 包、V/q/CSR 及该活算的可重算字段在当前目录视图不可用。

独立固定 g 仿射前缀 v3 的 session `17784` 已在此前真实 exit 0，并已亲读完整 run、raw/physical 的 SHA 与原 RMS/BC/metric 全过的小记录；它与上述 generic 作业不同。其后新 `request_refined_fixed_q_actual_tail.py` 只写源及 py_compile 成功，遵守资源门没有 spawn 新 native。因此没有新的 full-H/J/audit 或最终 physical-H 包可宣布。

范围：只记录真实工具终态及最后已观测状态。原 generic 全 8outer 未完成；任何后继均须从可验证科学输入实际重新执行，不能把本记录当作成功。
