# 原终端 pull 与两份 README 差异同步

会话：Astra-serre-24b8836b-20261126。此文件只记录仓库同步，非数学计算。

本地执行器不可用时，使用本公开仓库的 [.github/workflows/serre-terminal-rule-sync.yml](../../../.github/workflows/serre-terminal-rule-sync.yml)。该 workflow 匿名作 blob:none、depth=1 的部分克隆，只检出根 README、课题 README 和请求；实际执行 git pull --rebase origin main，随后对请求中 last_read_rules_commit 作两份 README 的完整 diff。没有令牌、artifact、数学输出或其它课题数据。

首个已完成请求见 [terminal-rule-sync-request.json](terminal-rule-sync-request.json)。source commit fb9f91b6c52c0dbf56d6bf2d37fb88303b6f1b60；[run46076082440](https://github.com/Rogerhu12/math-research-public/actions/runs/46076082440)，job140764009178，success。真实完成时间 2026-11-27 22:21:11 UTC，即 2026-11-28 06:21:11 Asia/Taipei。

实际 HEAD 与 origin/main 均为 fb9f91b6c52c0dbf56d6bf2d37fb88303b6f1b60，partialclonefilter 为 blob:none，shallow=true。相对 f7936744dd3d50d39403592f2d6d496bfeb2be5e，两份 README 无差异。输出的 SHA-256 与本会话已读全文完全相同：

- README.md：581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102。
- topics/serre-uniformity/README.md：6ce1403bd2d2587bb9cca70bd0095a1264b1167fe2c4b62f0652ae671e6277a5。

真实日志结果 JSON 的 UTF-8 SHA-256 为 929c165a6865bfe984f4ab671b9c2555b0e3dfd7a1982bc4151a07050bbeeca8；哈希对象是 SERRE_TERMINAL_RULE_SYNC 前缀后的完整 JSON，不含日志时间戳、前缀或末换行。可重算日志不另提交。

后继只更新同一请求的时间与 last_read_rules_commit，push 即触发下一次真实 pull。收到结果后先读任何 README diff并立即执行新规，再更新 HANDOFF 的实际 pull 时间与已读提交。每小时要求继续；请求需提前留队列余量。连接器 fresh-head 检查不冒称真实 pull，本地恢复后仍立即实际 pull。

## 第二次真实 pull

2026-11-27 23:05:38 UTC，即 2026-11-28 07:05:38 Asia/Taipei，source/HEAD/origin main 均为 ffd8a7ed8bb8e544fcaf7e7d57a5e5300a142619；[run46080481087](https://github.com/Rogerhu12/math-research-public/actions/runs/46080481087)，job140778033392，success。相对已读 3b34f6064ca3030c4521f779844b64d05690c937，两份 README diff 为空，两个 SHA-256 与首轮相同；blob:none、shallow=true。实际结果 JSON SHA-256 为 8cc90b834ddd5b42f0545523cbd8160dbec19ff32927e89f5ab63ee9847f4122，哈希对象与首轮定义完全相同。

## 第三次真实 pull

2026-11-27 23:49:56 UTC，即 2026-11-28 07:49:56 Asia/Taipei；source d9bf1ece383641bcd182b3daf821d0f21de7879e；[run46084622951](https://github.com/Rogerhu12/math-research-public/actions/runs/46084622951)，job140791187426，success。实际 pull --rebase 从 source 快进到 c6fc7f507e432a35cd4e2e67d11c8679ef97531b，与 origin/main 相同。相对已读 be9b3703847324e411416b8f5837063bffdd99fa，两份 README diff 为空；两个全文 SHA-256 与首轮相同。blob:none、shallow=true。实际结果 JSON SHA-256 为 eb3c305e324b3dd8e474e0b7ddbce92f424ccef46dfd80dce3552b12a7a77ec5，哈希对象沿首轮定义。下一次请求不迟于 08:39、实际 pull 不迟于 08:49 Asia/Taipei；若本地执行器恢复则立即实际 pull。
