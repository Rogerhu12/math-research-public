# 原真 H 重验提前完成审计：仅 Python 调度的准备结论

## 结论和边界

新增 `computations/strong_eager_true_H_audit_initial_laws_actual_bvp.py` 已完成源变换核验、真实 q106 接受点的生产入口 prepare-only，以及 q098/q106 两个真实完整尾审计包的协议回放。没有启动 Node，没有解出新的尾或 BVP，也没有测得下一轮实际节省多少时间。当前正在运行的 q122 生产任务没有改变。

这里的改变只有一项：完整前缀原始 RMS 通过以后，原 `solve_coupled` 中唯一的 `Hnew` 真尾重验请求同时要求原完整审计，即 `audit=False` 改为 `audit=True`。初始仿射锚请求、原 Jacobian、物理边界检查、所有尾方程/容差/正性/线搜索以及最后 `finalize_output` 的独立审计请求和接缝验收都保留。原 MJS 文件未改；Python 新源单独登记哈希。

最后原请求若处在完全相同的全 28 项 H，已有 `strong_actual_recorded_tail_port.py` 的 `cached-exact-audited-live-H` 分支可复用刚刚真正算完的完整响应。它继续增加逻辑调用计数、写标准响应包，`origin` 指向真实后 RMS 包；不把 flow-J 存储或 warm 初猜当作新解。若物理输出端 H 有任何实际浮点数值不同，则走原 live 分支再完成完整审计。该判断使用原 `np.array_equal`，并非容差近似；本次回放还额外验证了所用全部 H 的字节相等。

## 身份和运行条件

新入口要求显式传入 `--initial-audited-tail-packet` 和 `--initial-audited-tail-ready`，以实际安装原 recorded port；不接受强制每个 live 响应审计的 release 标志。后 RMS 标准包的 `request.audit` 自身为 true，不只是在底层暗中多算一份 audit，因此可继续通过原完整已审计包校验器。

原校验器核全部源文件、完整 H、完整 `(3M+2)M` Jacobian、真正 audit、converged/residual 和 ready；参数比较只排除既有四个 I/O 键。原 live 创建继续核全部非 I/O 参数、cut、linearSlope、存储几何指纹及数值源表。新的调度源不混入旧数值包的 `source_sha256`，不会重标旧响应来源。

增加审计后，如果该次真实物理边界还未通过，可能多付一次审计成本。若最后 H 发生变化，也不保证省掉重复工作。所有收益必须由未来实际运行报告；此准备结论不改变任何数学完成声明。

## 已实际执行

| 检查 | owned exit | 墙时（秒） | 峰 RSS（KiB） |
|---|---:|---:|---:|
| 完整源变换、可逆性、AST | 0 | 1.029041288 | 17824 |
| 真 q106 生产 prepare-only，31 参数/116 BC | 0 | 1.016778737 | 22956 |
| q098/q106 真审计包协议回放，29 门 | 0 | 5.028749291 | 37312 |

回放先用真实 q098 同 H 已审计包，再把真实 q106 完整已审计响应作为唯一允许的第二响应。stand-in 不做新数值计算，也不对其它 H 返回任何数值响应。它验证后 RMS 的实际 `audit=True` 请求、最终逻辑 call 3、完整来源路径、原 `verified_packet`、全 H 字节、2408 项 J；1 ULP 不同 H 必须进入原 live 入口。缺少请求 audit/J、缺少完整 J/audit、残差超容差或 modes 改变都被原校验器拒绝。

第一次协议运行仅因一个旧临时 ready 路径不存在而在读取输入时失败；没有启动 Node 或写出数值结果。随后从 SHA 已核的 q106 正式主包原样提取 ready，SHA 为 `c78ff7ca7c3a7e4e79ea383212337447c4ad8dd0991a3414856bf6de3870e3ee`，与此前记录相同，再用新 r2 前缀正式完成。失败的资源记录与日志一并保留。

## 文件与重放

`2026-11-13-strong-eager-true-H-audit-preparation-manifest.json` 列出本批全部文件、长度和 SHA。生产准备的 `*-plan.json` 保存完整命令；资源报告保存实际子进程命令与 owned wait4 exit。`*-preparation-verification.json` 将新旧生产准备的完整 profile、非 I/O 尾配置、目标核、参数数目、边界数目、节点及批次逐项比较。完整数值包仍沿用已经发布的 q098/q106 文件，没有重复保存原全态数组。

该入口准备好供下一真实 initial-laws 候选使用。其数学候选仍须经过原完整 warm 域评估、原 BVP/RMS、当前 H 真尾全 J/正性/审计、原物理边界与最终接缝门；这里没有可转移到新候选的闭曲面或 reach 证书。
