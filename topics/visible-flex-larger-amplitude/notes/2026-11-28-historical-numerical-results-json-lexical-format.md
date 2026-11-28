# 历史数值结果的完整 JSON 词法整理（RET93）

## 范围与实际字节

本批依据根授权，只整理更早非活的完整结果 JSON；文件不删除。固定原版本为 `f020f0a86ce3bce9d15f3cc1ab10edf45f3b2c13`。先由完整树取得每件 size / Git blob，随后只完整读取小于 100,000 字节的 UTF-8 JSON。198 份完整候选中，165 份纳入格式整理，26 份原本已经是相同紧凑文本，7 份具有输入、控制或系数配方作用而排除。165 份原体 3,143,154 字节，新体 2,310,514 字节，毛减少 832,640 字节；扣除本说明和完整映射后的净额在总表给出。

纳入者是既有有限 trace、线性/非线性诊断、曲率与几何 screen、精确预算、比较、失败/中断及历史资源结果。全部原数值字面、字符串、数组、字段和成员顺序保留在原路径当前文件里。没有用新摘要替换结果，没有删除原行、系数、阶段、控制样本、日志状态或数组成员，没有把数据分块或编码进说明。内嵌原配置、source/parameter/run 身份、整资源 argv、结果范围、错误和 unknown/null 同样原字保留。

## 严格排除

所有当前 CLI 输入、活跃源码实际输入、port、parent91、实际参数/ready/request/queue、唯一恢复输入以及活跃 run 均不在变更表。Nelder、已排除 control-response/MIDX 缺口不重开。本批没有读取大于等于 100,000 字节的正文或任何二进制体。

完整读后明确排除七件：q095 rms-mesh 额外节点计划、两个 bounded-curvature-core 系数初猜配方、controlled-continuations 控制/检查点路由、vu032 radius profile 程序，以及两份 input-adapter identity 元数据。它们的整身份与原因列在总表，仅作未改记录。另26件已经紧凑的文件也是未改记录；发布者不得根据这些记录删除或重写它们。

## 唯一变换

使用已刊 RET91 完整 3,705 字节 `scripts/resume_20261126/reproduce_complete_historical_note_json_lexical_format.mjs`。逐字符跟踪 JSON 双引号和反斜杠转义，只删除字符串外的 ASCII 空格、制表符、回车和换行，再保留一个末尾换行。所有字符串内部字节和转义序列保持不动，数值词从不经过浮点解析后重写；大整数、指数、负零及小数末位均保持原字。JSON.parse 只检查结构，不生成当前正文。

每个完整新文件等于其原体的这一词法输出；再次应用词法输出不变。每个旧、新完整 UTF-8 文件均记录 bytes、SHA-256 与 Git blob SHA。这些文本操作不构成科学测试，没有运行科学模块、CAS、AST、数值试例、benchmark、replay 或新准入条件。

## 科学结论与历史身份不变

有限筛查仍是有限筛查；条件预算仍只保原条件范围；失败、未付 mean/outer/whole-image/reach、未收敛及未知原因不被修改为成功。原解、原工作点与样本不因少了缩进而变化。此批既不重算也不重新论证任何数值结果，不把旧 producer/source 的未知边界补成已知。

文件中内嵌的 source SHA、输入 SHA、旧 report SHA、run/commit、file bytes 等身份继续按原历史对象解释。若某旧消费者以 whole-byte 哈希读这些旧结果，须从固定 Git 版本恢复完整原件再运行其原 guard。不能把新紧凑体贴上旧 whole SHA，也不能因格式不同跳过原验证。原完整数据和参数仍留在当前文件；原精确字节另有固定 Git whole 恢复。

恢复一条时使用映射中完整路径：

```sh
git show f020f0a86ce3bce9d15f3cc1ab10edf45f3b2c13:topics/visible-flex-larger-amplitude/notes/EXACT_RESULT.json > restored/EXACT_RESULT.json
```

这是原全文恢复，不是从摘要或字段重建。输入目录应保留原相对路径，若后续旧工具同时验证多个历史文件，应恢复其原完整版本集合。

## 完整再生与发布责任

```sh
node scripts/resume_20261126/reproduce_complete_historical_note_json_lexical_format.mjs \
  --manifest COMPLETE_MAP \
  --source-directory COMPLETE_FIXED_OLD_CHECKOUT \
  --output-directory SEPARATE_OUTPUT_ROOT
```

整组完整映射没有截数组，165条变更和全部未改/排除身份都在一个小于100,000字节的完整 JSON 中；每个结果文件也完整独立保护。没有新运行源，此处只引用已刊格式化器的确切 whole 身份。

根发布者负责 fresh 树的165条 original path/blob/bytes 相等后普通提交。fresh guard 只针对要写的165条；26未改和7排除记录是固定历史完整身份，不是额外当前发布门。本代理只创建 unreferenced 完整 blobs，没有写 ref、queue、request、workflow 或触发 Actions。新旧文本映射本身不是完整目标的科学进展。
