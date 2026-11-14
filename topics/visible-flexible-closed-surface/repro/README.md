# 本题冻结源代码依赖

`source-root/` 保存本会话实际使用的邻题数学代码及递归本地依赖。没有修改邻题；每个副本的 SHA256 在 `source-snapshot-manifest.json`。这些代码来自前会话已核的来源，保存目的是让复跑不依赖某个临时工作区。

在仓库根目录运行本题脚本时，给出

```bash
--source-root "$PWD/topics/visible-flexible-closed-surface/repro/source-root"
```

尾的 Node 客户端还会设置 `CLOSING_TAIL_CACHE` 为该目录中的 `topics/large-amplitude-twist-flex/scripts`。`closing_tail_sources.mjs` 继续校验既存 Git blob 清单，不因复制而跳过来源检查。

这些副本不代表本题已完成。几何参数、最终输入、各次实验和结论的范围仍以本题 HANDOFF、notes 中的冻结报告及 results 为准。数据文件须通过终端 git 获取；不要用集成工具传递或展开二进制/大型数组。
