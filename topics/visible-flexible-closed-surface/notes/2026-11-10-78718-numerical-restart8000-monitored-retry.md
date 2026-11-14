# 8000-01 会话不可恢复与 8000-02 的持续工具观察

日期：2026-11-10；Astra-visible-flex-78718bd0 / root。
状态：8000-01 自然出口未知；8000-02 实际启动并持续观察，未完成。

## 1. 已观察到什么

01 原实际启动为16c14e/session2770，首包局部9ab005 exit0；这些事实保留。
随后 root 的 write_stdin(2770) 与旧认证shell均返回 Unknown process id。
不能据此推断进程成功、失败或仍活跃，更不能用保存的初始RUNNING状态代替出口。
4a6c59读取小摘要，050b28完整列出该stem的文件名/大小/mtime，均未发现
CP、summary或guard-completion。reproduction仅保存06:37:37的RUNNING_ORIGINAL_TRUE_OUTER。
实际快照70ce19为root-unavailable-session，2141B、SHA
`a1b489d0bfb6bdc5c618057236f388c665981524134d2167b75ff2246df58934`。
未覆盖任何01数据；未推断工具句柄失效原因。其他tool进程的/proc视图
不能用来判定这个旧作业的存活，更没有按重用的PID发送信号。

## 2. 另名重算与相同问题

新stem为 `2026-11-10-78718-numerical-m14-restart8000-02`。
使用同一套已经完整独审的九件新源、相同已知失败direct-CSC run02 CP及
它的自有tail_0003、同一初猜、同g/M14/N512/W14/max8000/原tol及BC。
只有输出命名空间改变；未从未知01的活动文件产生初猜。

纯prepare：bb6f3b/session21514→3e79b0，真实exit0，181绑定、0solver。
该次同批之前的观察文件写入因相对cwd错误失败且零文件产生；随后70ce19
用绝对路径补写。这个I/O失误不是prepare或数学求解失败。
资源guard纯准备88e195，真实exit0、184绑定、0solver。
root实际启动ef2882/session72917；start观察写入152a37真实exit0。
所有原6GiB/进程DATA、Node1536、磁盘阈值及数学参数原样保留。

## 3. 实际工具回执的持续保存

root 的 functions.exec 控制cell32调用实际exec_command启动上述冻结guard命令，
随后每次以write_stdin(session72917,yield_time_ms=1000)继续等待工具自然返回。
当前工具的空轮询实际约5秒；没有从guard文件推断退出。每12次报告一次实际
轮询回执。控制cell保存原始工具返回；若真正收到exit_code及chunk_id，才调用
`78718-record-root-tool-observation-v1.py --phase complete` 写入root真实出口记录，
并哈希该stem的现存闭存文件。完整数学final仍必须另行真实执行。
若工具句柄再次失效，控制cell只写unavailable记录，绝不填造exit code。

recorder是纯记录器，不调用solver，也不把任何guard字段转成工具出口。
调用者必须提供实际工具返回。自然completion要求真正exit_code、receipt及已结束
的tool状态；start/unavailable使用不同status，无法支付冻结final的成功观察条件。
时间是保存观察的时刻，不冒充精确进程wall-end。
本记录不宣称工具失效问题已根治，也不宣称新BVP或整图成功。

## 4. 冻结入口和记录器身份

| 文件 | B | SHA256 |
| --- | ---: | --- |
| `scripts/78718-record-root-tool-observation-v1.py` | 3721 | `d7115aa54f2148ea579161e164de5c79585269dc5522f13b1b1bb228c8d4440b` |
| `notes/2026-11-10-78718-numerical-m14-restart8000-02-launch.json` | 103214 | `0a84349dbfbaf00c7670fe846605209fd8350722c439a0fd5c39931826de012d` |
| `notes/2026-11-10-78718-numerical-m14-restart8000-02-guard-launch.json` | 53915 | `41eb98c8d4c1b001cecec0f8b9ed00023a4ceaa0b418f2d5a3dee09899ae908a` |
| `notes/2026-11-10-78718-numerical-m14-restart8000-02-root-observed-start.json` | 2035 | `4e7c5acab66d45e72201a877e8296c868f1c7399d10fdc52474f0580ac9f5dbc` |
