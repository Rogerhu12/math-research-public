# 接受态之后的连续同 g 精化与完整控制响应入口

## 已完成的可执行结果

新增 `strong_20261114_accepted_sequence.py` 将真正接受的实际端点接入原生产求解链。可选 `response`（当前接受态的固定视图、原完整均值几何审计、十三控制响应）、`refine`（再作 M32→M40、1280→1536 的原同 g 非线性精化和完整均值比较）及 `refine-response`（精化后直接生成新接受态的十三控制响应）。各阶段实际子进程顺序运行，真实退出状态及保留的接受态写入 `sequence-status.json`。它不使用已经停用的公开队列，也不设置运行时长、文件容量或额外批准门。

入口仅接受 `solver_success=true`、`audit_pending=false`、实际非线性尾的原端点；完整原始 collocation、physical quintic、尾 H/J/audit 与必要快照按原 SHA 校验并保留。设计态经原 current-anchor 转换器生成真正固定视图；已有固定态直接使用其原转换报告。新核高模属于 M40 的真正未知，原 g、材料坐标、全 H 非线性尾、RMS、BC 及最终 audit 均沿用原入口。前后接受态还逐项核对物理 profile、尾参数、尾 cut、材料角、固定 gauge 与 meridian length。

输出数据统一使用本地 basename 和相同字节，避免后续机器复用时依赖瞬时工作目录。完整响应所需十三方向及三条 primary 校准向量保留；可重算的 half/forcing 向量及 J/QR 不为发布另复制，摘要明确写出未归档项目，不能把它称为原完整数组包。

## 已实际运行的验证及边界

对真正 A 的 fixed-view/原 raw/原 tail，在独立输出目录运行 `--route refine-response --prepare-only`。最终两阶段分别为原 M40 `--spectral-prepare-only` 和十三控制 `--metadata-only`，均真实 exit 0；共按 SHA 保留 27 个接受态输入。此运行没有启动 Node 尾求解，没有装配大 J，没有 Newton 步，也没有产生新的接受态或新的数值响应。完整机器记录见 `2026-11-14-strong-resume-accepted-sequence-prepare-r1.json`。

新增 `strong_20261114_response_widths.py` 只允许按控制名明确指定差分宽度，完整/半宽物理相对一致性门仍为 2e-4，原 backward 检查及全 32/40 维解均保留。默认将 terminal fraction 的相对宽度从 2e-6 改为 2e-5；A 当前 fraction=.1，故绝对宽度为 2e-6。此前该列物理全/半宽差为 1.53035e-4，完整物理方向很小，消去误差是一个待检验的解释。较宽差分尚未实际重算，不能宣称更精确或已通过。

## 接受态到达后的使用

提供 `--accepted`、`--tail-config`、`--source-topic`、`--frozen-reference-ready`、`--frozen-calibration-ledger`、全新 `--out-dir` 和 `--work`。输入若已经固定而将作 M40 精化，还需其真正 `--fixed-report`。源目录为同题 `computations`，默认原 port32 与精确扩展 port40；入口根据接受态实际物理 port SHA 选择使用，不能把 M40 端点误按 port32 加载。生产运行不带 `--prepare-only`。

这份结论只完成可执行的接受态续算接口，尚未完成 larger-amplitude 的闭曲面、连续族、reach 或大幅见证标准。margin325 的本地实际非线性作业继续单独推进；不会以本接口准备完成作为终点。
