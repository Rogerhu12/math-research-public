# 原命令外层空间保护器：源码及明确生产路径独审

2026-11-09，`/root/tail_theory`。本轮全文读取 supervisor，核根的真实定向测试报告，并独立执行生产 argv/来源/路径预检。没有启动数学 solver，也没有重复父/孙 heartbeat 测试。

**结论：对下述冻结源码、原 resume03 launch 和明确生产参数，静态审查及真实路径预检 PASS。** 保护器降低共享盘再次耗尽的风险，不是对任意外部写入速率的绝对保证；其记录不替代控制器状态与根的实际工具退出观察。

## 1. 绑定与检查结果

| 对象 | SHA256 |
|---|---|
| `scripts/db6f-root-run-space-guarded.py` | `cf1e2364300015c841b2070be51e948dc7ba37ef5b98eef0441819bca1e6aabd` |
| 原 `prefix-amplitude-resume03-launch.json` | `0e0f020b7c879790d9e6b3726f324cbde6a2c724f43b3dca5fff30d370a42e3c` |
| 根的 `root-space-guard-directed-check.json` | `dd55296087499e29723bffa178ae08939acfca32eddcbaccf2492b09d3b6556a` |
| 自有 `tail-review-space-guard-paths.json` | `02a7ff0e155bda7d03f80b2666f01b86443142516ff120cc74c6149bb32bf867` |

自有检查程序为 `scripts/db6f-tail-review-space-guard-paths.py`，实际 receipt `f3ffa6`、exit 0。它重新核全部 83 个启动绑定与上表来源，没有调用 supervisor 或其 child。

## 2. 原数值命令保持原样

supervisor 读取固定 launch.command 的字符串 argv，直接传给 `subprocess.Popen`，不使用 shell，不重写任一数值参数或 config。cwd 来自同一 launch，stdout/stderr 写原 `out_prefix + '-run.log'`。`start_new_session=True` 为这个新 child 建独立 session/进程组；原 Python controller 启动 Node worker 时没有另开 session，因而沿用该组。

所有 SIGSTOP、SIGCONT 及异常清理信号都发送给此 `process.pid` 对应的新组，不向根、旧运行、git 或任意全局进程扫描发送。它不修改 engine、目标、初猜、容差、正性门或离散网格。暂停期间程序停在原执行位置，恢复后继续；墙钟耗时日志自然会包含停顿，不能据此假称与未停运行具有相同时间记录。

生产阈值严格为 512 MiB（536870912 B）暂停、768 MiB（805306368 B）恢复、每 2 秒检查一次。`free_bytes` 使用 `statvfs` 的 `f_bavail * f_frsize`；启动前先要求达到恢复阈值，避免一启动就处于不足区。滞回避免单阈值附近反复切换。测试可通过函数参数注入可用空间序列；生产 CLI 不暴露该注入入口，按默认真实文件系统函数执行。

## 3. 退出、异常与记录身份

循环以实际 child.poll 为条件。正常完成记录 `process.returncode`，没有根据日志推断 exit。若 Python 能捕获的异常发生且 child 仍活，先 SIGCONT 再 SIGTERM，等待后必要时 SIGKILL；这一顺序避免让已停止的自有组成为无法处理终止信号的孤儿。外部直接杀死 supervisor 等不可捕获情形不在该控制流的清理保证内。

每个调度事件写独立 backup；完成后才另写 primary observation。JSON 通过临时文件、fsync、replace 发布。若完成时 primary 因磁盘再次报 OSError，错误写入 backup，不能伪称 primary 已存在。返回值来自真实 child；负的信号返回值在 CLI 转成 $128+|\mathrm{signal}|$，原有符号仍保存在记录中。

这些是 supervisor 观察到的 controller child 结果，不是 worker 的直接退出值，更不是根工具本身的实际 receipt。源码保持 `tool_exit_observed_by_root=false`；根仍须实际等待本工具退出，并核 controller 的 status/flags、最终真实响应与 worker 记录。原 controller 可 catch 数值/运行异常后 exit 0，因此 child exit 0 单独不构成目标成功。

## 4. 明确生产路径支付的防碰撞条件

根给定的 primary 是本题 notes 下 `2026-11-09-db6f-root-amplitude-resume03-child-execution.json`；backup 为 `/dev/shm/db6f-root-amplitude-resume03-child-execution.json`。完整 argv 已保存在自有路径报告中。预检实际确认：

- primary、backup、各自 `.tmp`、原 run.log 和 controller reproduction 六路径互异；
- 新记录路径及临时文件均未存在，不与 83 个绑定输入或 guard/launch/test 文件重合；
- primary 不占用原 controller 的 O03 前缀，backup 明确位于 `/dev/shm`；
- Python 和输出父目录存在，当前 `f_bavail` 达到 768 MiB 启动门。

因此 guard 启动时预建的唯一 O03 文件仍是原 controller 明确允许的 run.log；第一次事件只写 `/dev/shm`，不会让原 out-prefix 拒覆盖门误拒。

源码显式防止 primary observation 等于 controller reproduction，但没有为任意 backup 参数重复同一通用禁止式。因此本审查没有将其宣称为任意 CLI 路径都安全的通用工具；上面的明确生产路径检查实际支付了本次 backup 的隔离条件，无须改动被冻结来源。路径新鲜性是本次预检时的事实，supervisor 启动时仍自行拒绝已有文件并重新核绑定。

## 5. 根的实际定向测试与作用范围

根已报告真实测试 receipt `1a2a47`、exit 0。冻结报告显示父与孙两份 heartbeat 在三次观察中都维持相同计数，随后同一个 child PID 恢复，父/孙各完成全部 24 次更新并实际退出 0；controller reproduction 哨兵不变。测试使用受控可用空间回调，没有运行数学 solver。

首测试 receipt `5523f6` 的失败也保留：当时将 namespace 内的 Popen PID 对应到另一 procfs 视图，所读状态不是目标进程。后测改用两个真实 heartbeat 文件，没有修改 guard 源码。本独审不将首失败改写为成功，也不把后测试扩张为真实 solver 已经启动或所有可能的异常路径都已动态测试。

2 秒轮询不能阻止其他写者在两个检查之间消耗超过剩余空间；backup 本身也依赖其文件系统可用。因此这是审查通过的外层调度保护，而非绝对 ENOSPC 排除定理。实际数学验收、独立运行和 README 完成标准全部保持原要求。
