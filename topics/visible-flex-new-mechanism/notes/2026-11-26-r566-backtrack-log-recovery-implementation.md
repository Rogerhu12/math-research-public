# B030 回溯自然终态日志恢复（仅元数据）

source run **45851261982** / job **140017925998**，commit `d99eef5312b0c49d78431cc9596f4d48fbc4baa8` 已由 Actions 元数据确认 completed/success。2026-11-26 16:20 UTC 后两次完整 job log 连接器请求均返回 Transport closed，没有取得日志正文，不能据成功状态推断科学结果。

本包沿用已发布且实际使用过的 completed-job 只读恢复器；只改变确切 run/job/commit、独立文件名/schema、当前 DEFINITION tag，以及状态小结中的 actual working base extra、真实 selected fraction 和接受计数。完整请求绑定源码与 workflow。

只读 GitHub 的原自然终态身份，再一次流式读取全部原 stdout；逐字节 SHA-256、解析全部带 tag 的 JSON、核每个完整81q的二进制身份与累计计数不倒退，保所有实际 q 变化小结、原累计成本、pending/trust和最后完整原 FINAL 字节。新增摘要不运行任何模型、ODE、优化、SciPy、NumPy或科学检查。没有原日志重放、文件、artifact、Release、Git写入；仅输出小型完整解析收据与一条原始完整最终状态。原 signed redirect 不携带 GitHub credential。

source `scripts/r566_backtrack_log_recovery_20261126.py`：14514 bytes / SHA-256 `497156742c3f46ec2ac81f6d03f57d52770703e0c126c43fd2b20ddd4dc86eed`。
workflow `.github/workflows/visible-r566-backtrack-log-recovery-20261126.yml`：1727 bytes / SHA-256 `3eb7c5c4a93f85fec9c67bb3049cc932752d3bebe93127463df4fda064671f15`。
request `computations/request-r566-backtrack-log-recovery-20261126.json`：1832 bytes / SHA-256 `2549c60106b2cc77ca6652128fb252d875b25eec9301806499c7ec4fa2b02ae6`。

单公开job、8分钟timeout，只有 repository actions:read/contents:read 所需权限。恢复失败或没有 FINAL 时保留最后可读状态及未知后续费用，不冒完整科学结果。root 审阅后 CLI 发布；本地仅 AST/JSON/source identity，不执行解析远端或科学。
