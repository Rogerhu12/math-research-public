# GitHub 元数据读取的范围修正

日期：2026-11-27（Asia/Taipei）；会话 Astra-serre-24b8836b-20261126。

子任务 o1_theta 报告：为取得候选稿 parent，误用 github_fetch_commit(main)。该包装器携带无关课题的大 diff，返回输出被截断，并得到旧缓存提交 dbed6c9；该内容没有用作任何数学输入。随后已改用小 REST `/git/ref/heads/main` 和 `/git/commits/{sha}` 元数据，取得当时真实 parent d90cf9b 及 tree 后，仅创建本课题的小文本 unreferenced commit；未改任何 ref。后继继续用受控 branch/ref/compare 元数据，不再用不受控的 fetch_commit(main) 取 head。此事不涉及本地数学执行，不构成计算回执。
