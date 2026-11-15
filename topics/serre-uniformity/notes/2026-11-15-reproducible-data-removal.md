# 2026-11-15 本题可重算数据清理

按根README在137c5a877的第15条，本题以普通提交删除可重算数据，保留源码、参数、运行编号、输出SHA-256和结论。所有旧提交仍保留，不改历史、不强推、不新建Release或永久数据副本。

现有初始main b6dd686c下本题840326974 bytes。计划删除scripts/data全部生成输入/中间表，以及computations中至少100000 bytes的.gz/.jsonl/.csv/.txt/.log，按同一初始清单预计775633196 bytes；以执行时最新main逐文件实际大小为准。证明、研究笔记、源码和小文本来源清单均保留。两个正在运行的R775/R781只读各自固定源提交/已绑定临时artifact，清理不改变其已读输入或core。

脚本scripts/prune_reproducible_data.py只做文件枚举、SHA-256、git rm和普通push，不运行数学。它把每个已删除路径、大小、旧Git blob和SHA-256写入压缩元数据清单，另提交小summary（含实际run、脚本SHA、清理前后字节数与历史取回命令）。不上传原始数据。若规则变化，则输出差异供root续接。

确实需要旧数据时，从summary所记source_commit_before_removal按清单的原路径执行git show；取回的输入只在当前运算中使用，勿重新提交。重算时仍须保原脚本、参数与规范；已登记计算不为此次清理而重做。
