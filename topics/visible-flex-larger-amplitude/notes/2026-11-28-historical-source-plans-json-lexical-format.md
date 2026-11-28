# 旧源码构造计划的完整 JSON 空白整理（RET91）

## 范围与结果

固定读取版本为 `9c32ec31ec8bf8c61da0774a37e4cfdda48de791`。本批完整读取 notes 下 51 份 R495–R617 / request217–251 源码构造说明；50 份只删除 JSON 字符串外的 ASCII 空格、制表符、回车和换行，1 份已是相同紧凑文本，保持原字。50 份旧体共 2,227,014 字节，整理后 1,918,551 字节，毛减少 308,463 字节。完整映射给出每个旧、新文件的字节数、SHA-256、Git blob SHA 和原 schema；净额扣除本说明、映射及新 3,705 字节完整格式化器后计算。

这些文件是历史 source-view、generator、literal-patch、source-role 和编译接口的完整计划。部分包含完整源码字符串与原参数；所有这些字符串内部的字节、转义以及字面参数全部保持。此项没有删除源计划、补丁、源角色、结论、失败、未知项或任何数组成员，也没有更新任何内部旧 SHA。原科学源码文件、proof、ready、request、queue、实际输入和返回数据均不在改写表中。

## 精确变换与完整性

变换逐字符识别双引号字符串及反斜杠转义；仅在字符串外丢弃四种 ASCII 空白。保留原对象成员顺序、数值字面（包括指数、大整数与负零）、布尔、null、标点、字符串与全部转义，最后保留一个换行。原文本不经 parse/stringify 重序列化。读取时的 JSON.parse 只用于检查原对象结构；正文输出由词法变换直接得到。

每个完整原文件均先按树元数据验证大小小于 100,000 字节，再完整读取并核对 SHA-256 与 Git blob SHA。完整新体也逐一计算这两个身份，验证再次词法整理不变。没有读取大于等于 100,000 字节的文件或二进制体，没有数值运行、AST、基准、科学重放或新准入条件。

## 原整文件哈希仍指向原版本

源码计划里的 source hash、parent plan hash、manifest 大小及其他身份字面仍是原有历史身份，绝不解释为整理后当前文件的 whole hash。旧 source generator、optional reproducer、原 ready 或完整来源验证器如果要求原 whole hash，须从固定版本恢复完整原件，再运行原工具；不能在哈希验证失败后放松检查，也不能把新文件贴上旧身份。

完整旧文件可用下列方式恢复到独立目录，保留原相对路径：

```sh
git show 9c32ec31ec8bf8c61da0774a37e4cfdda48de791:topics/visible-flex-larger-amplitude/notes/EXACT_OLD_PLAN.json > restored/EXACT_OLD_PLAN.json
```

实际路径和完整 whole identities 以映射中的每一条为准。恢复时不要只截取 JSON 字段，不要用重新序列化的对象冒原字节。所有旧人写说明、源码的数学内容、原失败与未完成结论保持原有含义；格式整理不表示原请求执行成功。

## 当前科学与旧重现入口分离

本批没有改动当前科学模块或 CLI。当前 33 / 28 接续顶层完整 138 source roles 与全 CLI 的已读范围没有这些 notes/source-plan JSON 路径；这不是对所有历史工具无依赖的断言。旧构造器可以继续把这些文件作为可选复现输入，但旧 whole 验证必须按上一节读取固定完整原件。没有向任何运行源增加 alias，没有修改 workflow 或 request，也没有触发工作流或写 ref。

## 完整格式化器

新文件 `scripts/resume_20261126/reproduce_complete_historical_note_json_lexical_format.mjs` 从已刊 RET88 的完整 3,718 字节格式化器派生。只有脚本显示名、两个结果 schema 与允许的目录前缀四处字面替换；完整反替得到原父体。词法算法、每个原新 whole-byte/hash 验证、独立输出目录、拒绝覆盖不同已有文件和全部 CLI 保持。映射同时记录父源完整身份与全部四项替换；不是省略正文的伪代码。

```sh
node scripts/resume_20261126/reproduce_complete_historical_note_json_lexical_format.mjs \
  --manifest COMPLETE_MAP \
  --source-directory COMPLETE_FIXED_OLD_CHECKOUT \
  --output-directory SEPARATE_OUTPUT_ROOT
```

这里没有运行该可选文件重现器，更没有将其作为科学执行前门。当前已保护的是全部 50 个完整新 JSON、完整格式化器、说明与映射。根发布者按最新树逐项核对这 50 个 original path/blob/bytes 后作普通提交；本代理没有更新任何 refs，已紧凑的原文件不写改。
