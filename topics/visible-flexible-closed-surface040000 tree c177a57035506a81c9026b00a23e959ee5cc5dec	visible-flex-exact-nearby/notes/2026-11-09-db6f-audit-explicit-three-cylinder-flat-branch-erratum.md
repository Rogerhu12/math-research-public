# 三片柱弯稿：式 (8) 的一个排版字符

2026-11-09，作者 `/root/independent_geometry_continued_2`。

冻结原稿
`2026-11-09-db6f-audit-explicit-three-cylinder-flat-branch.md` 的 SHA256 是
`ec4c52b1abafb44b300ae20956bc1308c9b522b62a9cff1a70208a65326117ee`。
原脚本与原报告也保持封存，不覆盖、不重写。

root 全文检查发现式 (8) 第二项的 `sin` 少一个 LaTeX 反斜杠。
正式采用文本可仅作以下单字符插入：

```diff
-T_\lambda(s)=\cos(\lambda b(s))n_j-sin(\lambda b(s))e_z,
+T_\lambda(s)=\cos(\lambda b(s))n_j-\sin(\lambda b(s))e_z,
```

这是排版勘误。正弦的数学含义、负号、全部公式和论证不变；作者符号脚本
自始使用 `-sp.sin(phi)`。正式结果与冻结稿的正文差分应只包含这个反斜杠，
并另加审查状态/来源前言。

原先两次实际运行没有将外层工具退出元数据持久化。为留下可核查的实际
进程退出证据，新增的 receipt 脚本只把同一纯公式检查器重放到一个新的
`-receipt-replay.json` 路径，捕获子进程 PID、UTC 起止时间、return code、
stdout/stderr，并检查重放报告与封存报告逐字节相同、全部冻结来源在进程
前后哈希相同。它不改封存文件，也不生成网格、运行主求解器或读取候选数据。
