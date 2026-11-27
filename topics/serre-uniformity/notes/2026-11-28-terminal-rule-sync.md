# 原终端 pull 与两份 README 差异同步

会话：Astra-serre-24b8836b-20261126。此文件只记录仓库同步，非数学计算。

本地执行器不可用时，使用本公开仓库的 [.github/workflows/serre-terminal-rule-sync.yml](../../../.github/workflows/serre-terminal-rule-sync.yml)。该 workflow 匿名作 blob:none、depth=1 的部分克隆，只检出根 README、课题 README 和请求；实际执行 git pull --rebase origin main，随后对请求中 last_read_rules_commit 作两份 README 的完整 diff。没有令牌、artifact、数学输出或其它课题数据。

首个已完成请求见 [terminal-rule-sync-request.json](terminal-rule-sync-request.json)。source commit fb9f91b6c52c0dbf56d6bf2d37fb88303b6f1b60；[run46076082440](https://github.com/Rogerhu12/math-research-public/actions/runs/46076082440)，job140764009178，success。真实完成时间 2026-11-27 22:21:11 UTC，即 2026-11-28 06:21:11 Asia/Taipei。

实际 HEAD 与 origin/main 均为 fb9f91b6c52c0dbf56d6bf2d37fb88303b6f1b60，partialclonefilter 为 blob:none，shallow=true。相对 f7936744dd3d50d39403592f2d6d496bfeb2be5e，两份 README 无差异。输出的 SHA-256 与本会话已读全文完全相同：

- README.md：581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102。
- topics/serre-uniformity/README.md：6ce1403bd2d2587bb9cca70bd0095a1264b1167fe2c4b62f0652ae671e6277a5。

真实日志结果 JSON 的 UTF-8 SHA-256 为 929c165a6865bfe984f4ab671b9c2555b0e3dfd7a1982bc4151a07050bbeeca8；哈希对象是 SERRE_TERMINAL_RULE_SYNC 前缀后的完整 JSON，不含日志时间戳、前缀或末换行。可重算日志不另提交。

后继只更新同一请求的时间与 last_read_rules_commit，push 即触发下一次真实 pull。收到结果后先读任何 README diff并立即执行新规，再更新 HANDOFF 的实际 pull 时间与已读提交。每小时要求继续；请求需提前留队列余量。连接器 fresh-head 检查不冒称真实 pull，本地恢复后仍立即实际 pull。
