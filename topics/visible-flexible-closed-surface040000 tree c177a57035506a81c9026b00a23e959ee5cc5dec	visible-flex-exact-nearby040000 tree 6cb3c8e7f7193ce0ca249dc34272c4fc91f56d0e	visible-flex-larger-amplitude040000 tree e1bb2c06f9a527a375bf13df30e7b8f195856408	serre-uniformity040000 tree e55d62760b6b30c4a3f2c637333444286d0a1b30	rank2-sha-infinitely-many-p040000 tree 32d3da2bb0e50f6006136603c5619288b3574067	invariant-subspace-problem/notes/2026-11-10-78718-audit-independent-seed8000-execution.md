# 独立公开 M14 seed8000 的实际执行记录

执行者：Astra-visible-flex-78718bd0 / `/root/independent_audit`，2026-11-10。
状态：**因根 README 第13条取消强制独立重复，已于2026-11-10主动中断；实际工具 exit130；不是数学成功或失败。** 本文件可随新的真实执行事实追加，冻结主程序/输入/审稿不改。

## 已授权的固定工作

使用已全文独审的公开 M14 种子及其自有尾包0002，完整原W14/物理BC/outer联解，节点预算8000。具体165输入/167guard绑定及全部不变物理门见 [完整入口审稿](2026-11-10-78718-audit-independent-seed8000-entry-v1.md)，SHA `4bf8d07536b0df21f824bf06ba753af3905d6db252744b46b58fadf0aeeff9e3`。执行者不参与种子选择或数值调参。

root 实际主进程自然退出后给出资源启动信号，本人读取固定 guard 中的 `executor_start_command` 并逐参数执行。guard-launch 49,374 B，SHA `5dad81b17ce9e382933f10bf4e52c0c4cd6fee6bb86c8e54c93e4cc839a26e4b`。cwd 为当前 math-research 根目录。资源 wrapper、源、数值参数、actor均未修改。

## 真实启动与独占观察

- 主命令启动工具 `7d2471`，真实 session `23125`。
- 固定独立 recorder 记录启动，工具 `e78093` 自然 exit0。
- [启动观察](2026-11-10-78718-independent-m14-seed8000-01-independent-observed-start.json)：2,074 B，SHA `9d4fdb7c7d03b65668619b9ac3ad2dd1f35c693ee7393dd0d5763aae2ef93445`；记录时间2026-11-10 08:21:04 UTC，actor `/root/independent_audit`。
- 一个持续 functions cell `g3:81` 约每5秒真实轮询该 session，每10次只输出标量回执；保存实际start/poll/自然exit返回，结束时直接交固定recorder。只由本人消费该session，未消费任何root主/审计session。
- 当前最近本地记录为poll80、真实chunk `e3dc1a`，仍返回活动session；没有exit_code，未见自然出口。

工具 `3eaa8d` 只读文件元数据：本轮 reproduction 148,260 B，内部自报 `RUNNING_ORIGINAL_TRUE_OUTER`；自身尾包0001及首请求绑定已存在。没有把大 reproduction 或数值数组读进对话。该自报、尾包存在和guard-live均不代替完整自然出口或final；本轮尚无自己的observed-exit/最终成功CP声明。

## 后链和完成门

已审两条独立actor成功后计划见 [完整后链审稿](2026-11-10-78718-audit-independent-post-plans-v1.md)，SHA `18d96e7886d9b01501f19a5f6f25c5640e00dce909cb5fb042d47b2cc5724de7`。本人的静态和负门不产生候选argv，不运行producer。

只有本人真实自然exit0、固定独立recorder及完整final实际重放全部通过后，才用自己的CP/末尾生成计划并执行自己的连续证书和网格链。root的退出、成功图或其证书都不能代付。实际输出若不同，各自完成同一图自己的全链；原终门26件参照和1个待解析后代仍按原清单在消费前取齐。

若工具会话不可用，保留实际错误和未观察出口的状态；不得从guard、自报、mtime推断自然成功/失败，也不为恢复观察重复启动solver。任何监控接管必须指向原session并重新取得真实工具回执。


## 2026-11-10 08:50 后：同一工具会话的观察接管

原 `functions` 观察单元 `g3:81` 多次 wait 只返回 running，没有新的内部 heartbeat；本轮 `load` 中五个先前记录键均不再可见。不能由该现象推主进程成功、失败或仍运行。真实只读回执 **0345b0** 于 08:50:07 UTC 检查本 stem：无独立自然出口、guard-completion、CP、summary；reproduction 的 `RUNNING_ORIGINAL_TRUE_OUTER` 只保留为文件自述。

按 root 已授权的接管协议，只终止旧观察单元 `g3:81`，**没有向求解器发终止、没有重新启动求解器、没有改变任何冻结源或参数**。实际 **8dde7b exit 0** 重读固定独立 recorder 后，新独占 `functions` 单元 **g3:123** 调用 `write_stdin` 接回原 **session 23125**。

第一笔真实返回 **cc1593** 含同一 `session_id=23125`，没有 `exit_code`；随后真实 heartbeat **c394d0**（接管后 poll 10）、**595bd1**（poll 20）、**df908e**（poll 30）同样返回该会话。因此此处可以恢复“已实际观察到仍运行”的有限状态，而没有自然退出结论。新单元继续单独持有 23125，遇自然整数出口时按原固定 actor recorder 写观察，遇工具错误时只写不可用状态。此前的启动观察和所有产物保持原字节，不用本记录替代实际完成门。


## 2026-11-10 09:40–09:41 UTC：第二次仅观察包装接管

恢复上下文后，旧观察 cell `g3:123` 的多次 wait 只返回包装仍 running，未给出新的内部主 session 回执；相关内存 store 键不再可见。这些现象不证明主计算成功、失败或停止。实际 `b6dde2`（09:40:23 UTC）检查本次 stem：没有独立自然出口观察、unavailable 观察、guard-completion、CP 或 summary；reproduction 仍自报 `RUNNING_ORIGINAL_TRUE_OUTER`，其存在也不替代实际进程观察。

按 root 已授权的同 session 安全接管方式，仅终止 `g3:123` functions 观察单元，未给 solver 发信号，未重启或改变任何源、参数、初猜和 actor。新独占观察 cell 为 `g3:191`；实际首个 `write_stdin(23125)` 返回 **`98c00b`**（09:41:05 UTC），仍给出相同 session `23125`，没有自然 exit。以后由该 cell 独占读取此主 session，并在实际整数 exit 返回后调用同一冻结独立 recorder；如工具不可用则只能记录 unavailable，不能冒称自然出口。


## 2026-11-10：新规则下主动停止重复计算

实际 `f53706` 全文读根 README 新第13条及题 README：强制冻结、未参与者独审、机械核验、独立重跑要求作废。root 据此明确要求终止只为独立重复而运行的 session23125，并转实际研究。

执行时先只结束观察 cell `g3:191`，随后向同一工具 session23125 真实发送 Ctrl-C。工具 **b77c54** 返回 **exit130**，没有仍运行 session。该退出是研究调度下人为中断，不是自然数学成功，也不判为数学失败。没有重启求解器、改源/参数或覆写已有输出；没有调用旧自然成功记录流程。

已有输出的当前身份及真实中断返回存于同 stem `-intentional-stop.json`。后续不再为此重复计算建立独立验收链；此前完成的审查记录作为历史材料保留，不作为今后工作的强制流程。该代理转入实际研究，不再保持未参与候选优化的角色限制。
