# 同半步：完整 J/QR/首线性解成功后第三次外部 SIGKILL；字节不变 I/O 继续实际求解

## 真实线性结果和退出

`loop-margin325-half-actual-r3` 保持全部 13 物理方向的同一半步、M32/1280 角/35 参数/2590 初节点和新 H 的完整审计。批量改为 12、RHS 用 2 线程。它真正完成了首个全部 432 回调的 Jacobian、QR 和首个线性解：

| 量 | 实际结果 |
|---|---:|
| Jacobian 磁盘字节 | 460075656 |
| QR 磁盘字节 | 851514112 |
| 完整矩阵 infinity norm | 1648602.8924937935 |
| 首 RHS infinity norm | 0.00017109996701994835 |
| 线性解 infinity norm | 110.16461965479844 |
| 完整线性残差 infinity norm | 7.064254780100865e−18 |
| 原 normwise backward error | 3.8896288011978736e−26 |
| QR 时间 | 15.318208724 秒 |

这只是原线性系统的数值解，不是连续逆算子证书或非线性接受。原日志随后给出固定物理 Newton merit=0.013706817343524141。在首个 trial 返回之前进程于 2026-11-14 08:14:31.585273 UTC 被信号 9 终止；原监督进程 `wait4` 实际收到 `exitcode=−9`，外层 `137`，墙钟 734.558288955 秒，峰 RSS 464276 KiB，supervisor 没收到外部信号。初始 H 通过逐位匹配，整个首 J 期间没有 Node 子进程。没有任何半步 Newton trial 或接受步已被观察到，不能称为数学失败。

23 件、10991333 bytes 的完整原输出已 hardlink 保存在 `strong-work/margin325-half-r3-recovery/`，索引逐件给出 SHA256。J/QR 是原匿名临时文件，随真实被杀进程消失，未保存；不把线性残差记录称为完整 J/QR 包。

## I/O 执行选项的实际验证

已有匿名 arena 会产生约 1.31 GB 的 J/QR 文件页，这些页的资源占用不等于进程 RSS。信号原因仍未知，不能断言 OOM。本轮只为自有 arena 加了独立可选执行入口：原 `_write/_read` 字节及全部数学保持原样，每完成 32 MiB 写入后 `fdatasync`，再对该自有 regular file 调用 `POSIX_FADV_DONTNEED`；完成读取后只建议释放已读范围。它不改宿主机设置、不修改或删除他人文件、不更改数学门。内核页驱逐是 advisory，并非已证明的总内存上界。

先真实运行原 arena 与带选项的 arena 各一遍，比较跨 12 行写/7 行读、跨边界覆盖、单行读、负零、C/F 数组布局和全部字节 SHA256。两遍结果逐位相同，实际执行 4 次清页周期，0 次 I/O advice 失败；运行 0.418354295 秒、峰 78668 KiB、exit 0。此检查只验证存储字节，不声称求解过物理场。

新源为 `strong_20261114_disk_page_budget.py`、`strong_20261114_page_bounded_entry.py`、`strong_20261114_disk_page_budget_check.py`，均独立保存，旧文件未改。

## 正在继续的 r4

`r4` 于 08:25:33.210888 UTC 真实启动，session **28520**。原半步数学候选和所有门不变；radial batch=24、collocation batch=12、2 个 RHS 线程，以避免 13 点局部 FD 调用为了多出的 1 点构造线程副本；使用新的独立 256 MiB complete-input prefix cache，旧满目录保留。08:27:30 已完成 52/432 个 J 回调，峰约 317280 KiB，原初始 scaled collocation/BC 不变，新缓存确实有写入，仍无 Node。

日志：`/workspace/scratch/ffc1334c1988/strong-work/loop-margin325-half-actual-r4.log`。
检查点：`/workspace/scratch/ffc1334c1988/strong-work/runtime/topics/visible-flex-larger-amplitude/new/loop-margin325-half-actual-r4-*`。
可由所属 supervisor 使用的停止文件：`/workspace/scratch/ffc1334c1988/strong-work/loop-margin325-half-actual-r4.stop`。不得从另一个 exec 命名空间按旧 PID 发信号。

[数据、真实退出、原 argv、I/O 逐位检查和现场索引](2026-11-14-strong-resume-half-third-sigkill-and-page-IO-r1/archive.json)已经冻结。本条仅记录该时刻运行状态，不预先宣称 r4 成功、失败或新曲面存在。
