# 历史读取回执的完整 JSON 空白整理（RET92）

本批固定完整旧版本为 `9c32ec31ec8bf8c61da0774a37e4cfdda48de791`。32 份 notes/actual64–99 原报告身份、completed-reader addendum、字节 crosswalk 和 request 静态读取回执均先核树大小小于 100,000 字节，再完整读取。全部属于历史读取记录；不改其中被引用的原报告、数组、源、request、workflow 或当前实际输入。

变换仅移除双引号字符串外 ASCII 空格、制表符、回车、换行，并保留一个末尾换行。所有键、顺序、数值字面、转义、字符串、布尔、null、数组元素保持原字。没有 parse/stringify 重写数值。原记载的 source 和 artifact 身份、whole-hash 验证结果、实际原数值、失败、未导出 full-factor 边界、unknown/null 和 no-new-acceptance 语义均完整保留。一次旧记录的成功读取不改成完整科学认证，原未完成范围不被补齐。

32 份原文件共 956,596 字节，当前完整输出共 805,578 字节，毛减少 151,018 字节；扣除本说明和完整映射后的净额在总表给出。复用 RET91 完整 `scripts/resume_20261126/reproduce_complete_historical_note_json_lexical_format.mjs`，不新增运行源。所有当前及历史科学源码字节不变，没有科学运行、AST、数值试例、基准或重放门。

原内部 SHA、文件大小、source commit 及引用仍是原历史身份，不改成新文本的身份。若历史消费者或旧脚本要求原整文件 SHA，须用总表 fixed commit:path 恢复完整原件后继续原验证；不能在读到新格式后放松 guard，也不能贴原 SHA 冒当前字节。旧源、原实际结果及所有原参数不需要根据本格式操作重新执行。

可选完整文本再生参数：

```sh
node scripts/resume_20261126/reproduce_complete_historical_note_json_lexical_format.mjs \
  --manifest COMPLETE_MAP \
  --source-directory COMPLETE_FIXED_OLD_CHECKOUT \
  --output-directory SEPARATE_OUTPUT_ROOT
```

映射逐件保旧、新 bytes / SHA-256 / Git blob SHA 与原 schema。每个新体与其词法变换完整相等，并再次整理不变。根发布前仅对32个改写目标核 fresh original path/blob/bytes；所有未列文件原字不写。该代理只保护 unreferenced 完整 blobs，未写 refs、queue、request 或 workflow，未触发任何网络运行。
