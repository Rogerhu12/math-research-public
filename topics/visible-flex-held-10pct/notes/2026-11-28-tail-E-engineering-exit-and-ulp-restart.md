# 原 E 的真实工程退出与完整 ULP 初猜的原 worker 恢复

## 已观察到的终态

旧 `tail-adaptive-fullheight-20261128-a` 在 2026-11-28 11:07:42 UTC 记录 Node worker `returncode = -9`；控制 exec 86638 实际结束，返回 1。它未写出 `tail_0001.json.gz`，没有完整接受返回。尾部代理没有向旧进程发送信号；此处只确认记录中的负返回码，不把原因推断为 OOM，也不把工程退出登记为数学失败。

旧原生请求 0028 已完整返回；0029 已启动但只留下两个部分输出分片，没有完整 native record。分片字节数及最后写入时刻保存在同名 JSON 中。原包装器没有给出 0029 每个 child 的终态；当前工具的另一个 PID 命名空间不能用于伪造该证明。旧控制 session 的结束与 worker 的真实退出分别记录，不把部分分片视作完整返回。

## 已实际开始的独立恢复

`resume_full_height_from_ulp.py` 从已实核的、仍明确未接受的 55,344 个完整未知量初猜启动未改动的原 worker。它递归复核候选 summary、完整 state/H 和源绑定，并保留 M24、N512、全部 1,152 段、原 chord3、36 次迭代、`2e-9` 阈值及所有原生根/定义域规则。实际 config 逐 key 比较只改变 `initialCheckpoint` 与 `traceFile`；没有把初猜中的局部结果复用机制安装进新求解。

新的完整请求已通过真实 client 初始化，并以 `jacobian=true, audit=true` 发出。因而后继仍支付全部原生 fresh J、完整 height J 和原 audit。新 TTY exec session 为 19975，原 worker 与 controller 的 PID、PGID、session 及 PID namespace 存在独立 `process-control.json`；这些 PID 仅在记录的命名空间中有效。

真实新目录是 `held10-design-work/tail-fullheight-ulp-20261128-a`。同名 JSON 绑定一次性的 `start-snapshot.json`、新旧 config、实际入口和原 manifest。此条只登记工程退出及实际恢复，不声称新 worker 已接受，也不声称 full-H、outer coupling、全局闭图或课题完成。
