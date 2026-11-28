# 历史说明JSON完整词法空白整理

会话 Astra-larger-e4e2a2bf-20261126，AI-assisted。2026-11-28 07:56:55 UTC。

## 范围和实际改变

本次完整读取102份原notes小JSON；96份只删除字符串外的ASCII空格、tab、CR和LF，6份无变化。去掉的空白合计458116B。每份原文件和新文件均小于100000B；全部完整旧/新路径、bytes、SHA256和Git blob列在[总表](../computations/historical-notes-complete-json-lexical-format-delivery.json)。本次不退任何文件，不读取大文件/二进制，也不生成数值raw。

原数字token（含所有整数精度、指数写法、负零）、字符串/转义、键序、数组序、参数、来源与失败未知逐字保。转换器识别字符串和反斜杠转义，只在字符串外删四种JSON空白，再加结尾LF。没有把JSON解析后的Number重新序列化；原文件只作完整JSON合法性读取，转换始终用原全文。因而没有删字段、改参数、缩问题或压成摘要。

只涉及既有旧manifest、stable-batch、行政publication和session-recovery-plan；ci-recovery/public-actions目录、活queue/request、科学程序、证明以及当前科学输入没有编辑。旧清单里的源码/数学信息原字保留，此整理不主张其科学结论正确或完整，也不补未知身份。

## 原whole身份及旧读者

本次所有原文件的固定恢复提交为`9eb3fd8d960b61be6ea2440a47580f15923ac0ed`。已刊RET81等旧记录给出的selection/manifest whole身份继续表示该完整历史版本；不能把旧SHA冒作当前格式文件SHA。先前原文件未曾因此丢失：按固定提交和原路径，或按原Git blob，恢复整个文件即可。

历史科学或行政读者若钉住旧whole hash，须先在独立历史checkout恢复所需完整原文件与它的全部原输入，再照原完整命令消费。新总表的current是本次只改空白后的当前字节；original是可逐字恢复的原字节。原文件内写的历史source/output哈希都未修改为当前值。此恢复合同也适用于互相选择的旧stable-batch和其原publication回执。

## 完整再生器

[完整再生器](../scripts/resume_20261126/reproduce_historical_notes_json_lexical_format.mjs)由先前完整3694B/blob360c09a86237840e913c5a45cc3ca1075d87f444文本工具改明确schema/notes目录和自身名称，词法转换函数保持原字。工具使用总表逐项读取whole原文件，按原身份确认，形成whole新文件并按新身份确认。没有启动科学、AST、compile、fixture、benchmark或独立审核。它用于文本恢复，不插进任何科学队列。

```sh
node scripts/resume_20261126/reproduce_historical_notes_json_lexical_format.mjs \
  --manifest computations/historical-notes-complete-json-lexical-format-delivery.json \
  --source-directory <包含topics原全路径的历史仓库根> \
  --output-directory <独立的新全文输出根>
```

命令中的script/manifest相对路径以课题目录为工作目录；两个directory分别是有完整仓库路径结构的根，不把topic目录误作仓库根。整个操作只保护完整文本和普通新增提交；不改写Git历史，不以编码或分片搬运数组。数学与实际运行责任保持。
