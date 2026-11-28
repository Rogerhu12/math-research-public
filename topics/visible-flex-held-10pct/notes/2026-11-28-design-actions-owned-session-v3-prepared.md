# Actions v3：保持 leader 身份直到同会话后代清理完毕

日期：2026-11-28 UTC。此记录只处理执行生命周期；不是新的数值接受场或数学结论。

## 实际缺口与修正

冻结的 v2 在 `Popen.poll()` 已取得 leader 退出码后会直接清空 active；若顶层异常结束但孙进程尚活，原 PGID 后代可能遗留。独立 v3 保留 `start_new_session=True` 所建 leader 的 PID、PGID、SID、start_ticks、UID，用 `waitid(... WNOWAIT)` 观察退出而不 reap。每次信号前重新核 leader 身份；原 PGID 通过被保留的 leader 身份锚定，其他同 SID 进程组通过 PID/start_ticks/SID/UID 核实后的 pidfd 发信号。先确认没有同会话活进程，最后才 wait/reap leader；正常全部结束时不发额外信号。

规则变动的暂停/恢复及主动停止都复用同一 ownership 对象。数值输入、完整方程、矩阵、原验收门、冻结数值 worktree、terminal git 发布、330 分钟 worker 与 350 分钟 job 设置均继承 v2。v1/v2 保持原字节不改；实际首次 dispatch 选择 v3 workflow。

## 一次有限实际核验

`held10-design-work/ci-owned-session-lifecycle-20261128/check.py` 于本会话真实 exit 0。正常 child 退出 0、无活后代，cleanup 的信号列表为空。第二个是明确人工构造的生命周期探针：leader 留下同 SID、另一个 PGID、忽略 SIGTERM 的后代后退出 7。核验观察到未 reap 的 zombie leader 身份；对该后代的 pidfd 发 TERM 后再 KILL，确认无活后代，最后取得 leader 原退出码 7。探针没有运行 BVP，没有调用 Git，没有把人为异常记成原数学失败。逐项观察、实际源码与输出 SHA 见同名 JSON。

worker/helper 编译、worker --help、workflow YAML、内嵌 Python 编译与 shell 语法检查均过。没有补做任何数值/Jacobian 试验。

## 实际执行入口

- workflow：`.github/workflows/held10-design-mapped-v3-20261128.yml`。
- request：`ci/mapped-design-v3-command.json`。
- worker：`scripts/resume_20261128/design/ci_terminal_worker_v3.py`，新增依赖 `owned_process_session.py`。
- 数值入口仍是冻结 `ci_frozen_chain_entry.py`、`ci_fresh_design.py`、`ci_q_material_recovery.py`。
- 本记录落盘时未 dispatch；实际 runner 返回必须另行如实登记，不能把本准备记录当作新计算已启动或已接受。

每个新源及三个数值入口的完整 SHA 见同名 JSON。后续由 root 统一提交和实际 dispatch，继续恢复必要输入并推进 λ=1；原课题最终完成标准仍全部有效。
