# 完整旧保全JSON的纯词法空白整理

日期：2026-11-28 UTC；会话Astra-larger-e4e2a2bf-20261126。状态：完整文本格式整理，不是新的数学结论或科学运行。

本批只改87份已刊保全元数据JSON的排版。原文件均小于100000字节，原完整身份固定在提交 f687c963cbc899e211a3d083c12b2f1b7e322d4d。所有字符串内容、转义、数字字面（含可能的负零和大整数）、键序、数组序及标点保持；只删字符串外的ASCII空格、tab、CR和LF，再保一个末尾LF。没有先解析数字再序列化，也没有去字段、用选定值替原对象、编码科学raw或移动目录。未变的89份不写回，四份byte-delta文件也未纳入。

完整文件映射见 [总表](../computations/complete-retention-json-lexical-format-delivery.json)。其中每项有原完整bytes/SHA256/Git blob及当前完整bytes/SHA256/Git blob；所有原非空白字符的序列保留。原87份合计 3744100 字节，当前合计 3175068 字节，仅这些原文件释放569032字节；新增总表/本文/完整再生器的费用另计，不能把569032冒作净额。

## 历史身份的解释与原文件恢复

旧保全记录内的脚本、输入、输出、原参数、run、SHA及失败/未知仍按它们原来的时间和对象解释。本批不把历史SHA递归换成当前SHA，不把已结束运行、旧字段或旧文件字节改写成新的观测。JSON值完全不变，旧文件内记载的原身份也完全不变。

当前排版文件有新的whole身份。任何必须读取原字节的旧reader、完整文本再生器或whole-hash绑定，先从总表的 preformat_fixed_commit 加完整 path，或 original.sha 对应的whole Git blob，恢复原整个文件到隔离历史checkout；不把当前格式化文件提交给一个要求旧字节的接口。当前阅读JSON值可用现文件；校验当前字节可用总表的current对象。

例如对总表任一成员恢复：

```sh
git show f687c963cbc899e211a3d083c12b2f1b7e322d4d:FULL_REPOSITORY_PATH > FULL_REPOSITORY_PATH
```

原whole字节、原SHA和旧参数不需要通过近似反缩进来猜；它们已在不可改写的Git历史中。所有旧证据、原结论、旧失败和未知仍完整可取。

## 完整文本再生方法

[完整Node再生器](../scripts/resume_20261126/reproduce_complete_retention_json_lexical_format.mjs)逐原完整文件读取并按字符串/转义状态去空白，输出对应完整文件；它不import科学模块，不进行AST/fixture/数值计算，不加入科学队列作准入门。输入目录必须是已恢复原字节的独立checkout，输出为新目录。

```sh
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_complete_retention_json_lexical_format.mjs --manifest topics/visible-flex-larger-amplitude/computations/complete-retention-json-lexical-format-delivery.json --source-directory ORIGINAL_CHECKOUT --output-directory NEW_DIRECTORY
```

科学源、活跃request/queue、当前数值参数文件、raw、原接受场、参考输入、所有证明与Markdown结论均没有进入本批。只有已登记87个保全元数据路径改排版，不扩展到同目录其他文件。当前运行仍按原源码和原参数继续；本次的目的只是保留完整记录并使后续完整求解包能在原200MB限制内出版。
