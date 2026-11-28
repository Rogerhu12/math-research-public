# 旧交付与完整返回归档 JSON 的词法格式整理（RET88）

本批只整理 48 份已完整读取的历史元数据。其中 44 份删除字符串之外的 ASCII 空白并保留末尾一个换行，4 份本来已经紧凑，保持原字。44 份的毛字节减少为 236,497；完整映射记录本说明、完整再生器和映射自身的新增成本后给出净额。没有删除文件、字段、数组成员、参数、实际结论或失败记录。

## 1. 固定原全文与对象范围

全部原件固定于公开仓库 Rogerhu12/math-research-public 提交 `78010fa1368c31e733d2f8cdacfc53537de2c225`。每一改件均在完整映射的 `complete_file_map` 中给出准确路径、原 whole bytes / SHA-256 / Git blob，以及格式化后的同三身份。没有用相似名称、旧运行编号或准备状态替代实际字节身份。

第一逻辑组是旧源锁表、源或参数来源说明、显示字段对应表和 run21 的两份完整参数交付 binding。这些 binding 是描述当前科学来源和完整参数的交付文件；本批没有修改实际数值输入、实际场 binding、任何运行脚本或任何命令行词。旧 J1845 / N4096、run09 / run10 / run11 / run12、原 run16 / run18 / run21 / run23 的来源、准备状态、未知父场和历史责任仍逐 token 保留。

第二逻辑组是旧02–09运行的完整返回归档和对应 ledger。部分归档是原完整队列的历史快照，可能同时保留当时已返和当时尚未返的步骤。本批不把名称中的 completed 或 returned 扩大成“所有嵌入步骤都成功”。原状态、actual input/output records、全部 argv / selectors、原 queue header、source commit、returncode、missing outputs、summary errors、cleanup 和所有未知项都原样保留。当前 followups、request、ready 和 workflow 文件不在此批修改范围内。

没有改动25–33活动运行的源码、参数、输入、队列或请求。没有修改 R724–R730、half / halfwave 源族、原始科学数组、实际报告、证书或固定数学定义。未修改既有科学预算、32阶段、角域、径向域、参数精度或读取范围。

## 2. 唯一文本操作

完整词法循环逐字符维护“字符串内 / 字符串外”和反斜杠转义状态。字符串内所有字节及转义写法保持原样；字符串外仅删除空格、制表、CR、LF。完整输出末尾增加一个 LF。键名、对象和数组顺序、重复键（若原件存在）、全部数字 token（包括 -0、指数写法和大整数）、布尔值、null、标点和字符串逐字保留。

没有对原数值或对象执行 parse 后再序列化。JSON.parse 只用于整件格式有效性读取；新正文完全来自词法循环。每一新正文再次经过同一循环时原字不变。whole UTF-8 bytes、SHA-256 和 Git blob 都由完整正文计算并在保护时核对实际 Git blob。

这不是科学计算，不执行 F / J / J*、均值根、normal stages、积分、区间费用、AST、编译、数值样例或性能测试；也不要求重放旧科学或网络事件作为准入条件。

## 3. 原 whole-hash 读者和历史引用

原文件内部的 manifest_bytes、source SHA、输出 SHA、旧表自身身份、历史路径和所有引用均保持原 token，仍表示它们原来所指的完整历史字节。格式化后文件的新 whole identity 只由本批映射给出；绝不把新字节标成旧 SHA。

已读的历史构造器说明这一边界：J1845 参数构造器先读取并核对完整 shared provenance；run21 normal / moment / R723 mesh 参数构造器核对完整父参数和 binding；run19 参数构造器核对旧 display 全文。这些可选历史文档构造器的源及 guard 原字保留。若以后使用这种严格读者，先从固定原提交恢复它要求的完整旧文件，再运行原读者；本批没有松开任何 hash guard，也不声称直接拿当前紧凑体可通过旧 whole-hash 等号。

旧02–09归档的原说明把完整历史步骤和返回记录与当时活动队列分开。其完整说明和所读构造器身份保存在映射的 historical_reader_and_explanation_records 中。该列表是本次实际阅读范围，不冒称穷尽仓库全部可能读者。任何其他历史读者都适用同一个固定原全文恢复合同。

## 4. 完整恢复与再生

原件恢复使用固定 Git 对象，不通过重新运行科学推算旧正文。对映射中的每一路径 PATH，从 `78010fa1368c31e733d2f8cdacfc53537de2c225:PATH` 取完整原文件，在独立原件目录恢复同一路径；核对记录的原 bytes、SHA-256 和 Git blob。Git blob 身份也可直接恢复同一完整原对象。

本批完整再生器为：

`topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_complete_archival_metadata_json_lexical_format.mjs`

它从已刊 complete-delivery 词法再生器完整派生，只改再生器 basename 和两个 schema 字面。全部循环、严格原件等号、严格新件等号、路径范围、独立输出目录及拒绝覆盖不同文件的行为保持原字。此三处替换作完整反向文本替换，准确恢复原父正文。

完整命令接口：

```text
node scripts/resume_20261126/reproduce_complete_archival_metadata_json_lexical_format.mjs --manifest COMPLETE_MAP --source-directory COMPLETE_FIXED_OLD_CHECKOUT --output-directory SEPARATE_OUTPUT_ROOT
```

COMPLETE_MAP 是本批完整映射。源目录与输出目录必须不同；全部改件按原完整 topic 路径输出。已有不同输出不被覆盖。四份已紧凑对象无需重写，仍在映射中保留其完整身份。此再生器是可审查的文本构造说明，不是科学入口的新门。

## 5. 出版和适用边界

本代理只创建未引用的完整 UTF-8 blobs，不更新 refs、queue 或 request。根代理出版时仍对全部 44 个待替换路径作 fresh HEAD 的原 bytes / Git blob 精确比较；并发改变的路径不能强行以旧版本覆盖。原全文永久由固定提交和原 Git blob 定位，历史身份没有移到不存在的假路径。

138 份另行只读的旧RET≤82 / retirement / q090恢复账共7,364,362字节已全部紧凑，词法处理后原字相同，因此没有为它们生成替换或额外零收益交付包。没有为达到目标净额扩大到当前科学输入或改变参数。
