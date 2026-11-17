# 纯历史索引备份退役与准确恢复

2026-11-17，Astra-larger-parallel-16f63c8b-20261117。为给实际新数学结论保留根15要求的200MB空间，本次仅普通删除一份重复的历史导航索引；不改写历史，不删除任何科学源、状态、数组、warm输入或当前run来源。

| 字段 | 准确值 |
|---|---|
| 退役路径 | topics/visible-flex-larger-amplitude/results-index-through-request212.md |
| 字节 | 96775 |
| SHA256 | 08874419a11e89ab3056996ceecc2779dfaf02b8516d6052a9a996024074c161 |
| Git blob | 3e48931cecfeb89470bbbec272783f66b38be4e8 |
| 已实核恢复提交 | df8deeeb6832af1170d697681193ceb6adc635d5 |
| 本次删除前头 | 9d2d703e49ba9cd167b57ea038c3f817f120551d |

root 实际比较字节，确认此文件同时与
df8deeeb6832af1170d697681193ceb6adc635d5 的同路径，以及该提交的父版本
topics/visible-flex-larger-amplitude/results.md 完全一致。它是原字索引备份，
不是科学输入或新的证明正文。

完整内容仍可直接阅读[固定版本全文](https://github.com/Rogerhu12/math-research-public/blob/df8deeeb6832af1170d697681193ceb6adc635d5/topics/visible-flex-larger-amplitude/results-index-through-request212.md)，也可准确恢复：

~~~sh
git show df8deeeb6832af1170d697681193ceb6adc635d5:topics/visible-flex-larger-amplitude/results-index-through-request212.md > /scratch/results-index-through-request212.md
~~~

/scratch 替换为仓库外目录。该命令恢复全部原文，不从SHA猜造内容。

## 引用范围核对

在本次实际检出的根文件、.github 与完整本课题中，对完整路径、文件名、SHA256、blob进行文字搜索。原引用只有以下历史Markdown记录：

- log-through-R478-2026-11-16.md 中关于request212时索引原字归档的一行；
- notes/2026-11-16-fixed-f93-historical-administrative-retention.md 的历史Markdown引用表三行（118–120）。

这些表是当时历史事实，保留原字，不把旧表改成新删除清单。非Markdown科学源、入口、reader、guard以及当前H/open中无命中。当前H的活跃科学责任为235–254，未把这个历史导航文件列为运行输入。

该核查范围是实际检出的本课题及根/.github，不冒称扫描了未检出的其他课题。
另一个938674B的旧rawcell manifest因仍有科学消费者及明确保护记录，本次没有删除。

退役毛节省96775B，净节省另减本小说明及同次新科学文本的实际字节；最终总量按当次真实目录/提交计量。旧全部结论、证明、来源及历史位置都可经上面的固定完整版本恢复。
