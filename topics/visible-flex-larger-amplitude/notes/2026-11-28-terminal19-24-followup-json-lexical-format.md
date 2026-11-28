# 已官方终态19–24的完整 followups 词法格式整理（RET89）

本批完整读了六份旧 followups、六份原 workflow、六份 controller、六份原 request 和六份已刊终态说明。只改19、20、21、24四个 followups 文件的字符串外 ASCII 空白，毛减少34,119字节；22、23本已紧凑，保持原字。没有删文件、步骤、命令参数、selector、budget、历史源、失败或未知字段，没有构造新科学结果。

## 1. 先确认的官方终态

| 编号 | 实际run/attempt | 已刊官方状态 | 证据中的完成时间 |
|---|---|---|---|
|19|46076669320/1|completed/success|run updated 2026-11-28T04:00:47Z|
|20|46079535427/1|completed/cancelled|run updated 2026-11-28T04:46:09Z|
|21|46084442413/1|completed/cancelled|run updated 2026-11-28T05:37:58Z|
|22|46090913581/1|job completed/cancelled|job completed 2026-11-28T06:51:08Z|
|23|46094430214/1|job completed/cancelled|job completed 2026-11-28T07:32:27Z|
|24|46096380016/1|job completed/cancelled|job completed 2026-11-28T07:56:19Z|

以上来自本题完整已刊终态笔记，不以墙钟推定。19的官方success不改写其已知准确normal费用失败或课题未完成；20–24原因未知、完整科学自然返回/final/typed等原未知仍按各笔记保留。本批不补这些值，也不改六份终态证据。

## 2. 不触发旧请求，不改活动运行

六份 workflow 的 push.paths 均只有相应 actions-request JSON，并另保原 workflow_dispatch。所有六份 request 和六份 workflow 均不写入、不改动、不 dispatch。因此四个 followups 格式变动不满足这些旧科学workflow的 push 路径条件。控制器和 followups 原读取实现也不修改；原请求中 bootstrap_mode=followups_only、followup_file、原32762字节/046f0d7b…读取器来源记录都原字保留。

19当前留树的完整步骤为7词pure与38词normal费；20、21、24为6词必要输入、26词参考构造及157词science。整数组、输出路径、source SHA、summary/progress字段、cleanup、parent request ID和finish_when_done均按原 token 保持。旧未执行步骤不会因格式整理改成已执行或重新排队。25–33所有文件都不在本批内。

## 3. 字节语义和固定原件

全部原件固定在提交 `b9c4fbd6d0a109177f6d66d1973ee5a3eeed4e8e`，完整映射逐件给原和新bytes/SHA256/Git blob。只删除字符串之外的ASCII空格、TAB、CR、LF，再保留一个尾LF。字符串内容、转义、数字字面（含指数/-0/大整数）、键序、数组序、标点、布尔与null原字不变；不使用parse再serialize来产生新正文。

四个格式化输出都重新通过同一完整词法循环得到自身，实际保护的Git blob与完整正文计算一致。没有科学、AST、编译、数值fixture或性能实验。

所有旧whole SHA仍指固定原全文。若后来需重演历史controller或严格whole-hash文档读者，先从固定提交按完整原路径恢复原件并核原身份；不得把新紧凑体冒旧SHA，也不应向已官方终态runner假称接续。原ready、request、controller、workflow、实际输入和科学数据不变。

本批复用已完整保护的 `scripts/resume_20261126/reproduce_complete_archival_metadata_json_lexical_format.mjs`（3718字节），不给同一算法复制新源码。命令仍是：

```text
node scripts/resume_20261126/reproduce_complete_archival_metadata_json_lexical_format.mjs --manifest COMPLETE_MAP --source-directory COMPLETE_FIXED_OLD_CHECKOUT --output-directory SEPARATE_OUTPUT_ROOT
```

完整映射与RET88使用同一严格schema和字段合同，原件目录、输出目录须分离。根代理只按四份original精确fresh metadata比较后普通提交；本代理仅保护完整blobs，没有ref、queue行为或网络事件复演。
