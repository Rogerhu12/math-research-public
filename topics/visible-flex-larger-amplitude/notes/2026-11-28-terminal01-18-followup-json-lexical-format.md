# 已官方终态01–18旧 followups 的完整词法格式整理（RET90）

完整读取19份20261126/27旧followups（包含03b）后，13份本来已紧凑且原字不动；只有02、03、03b、06、11、18六份可删除字符串外ASCII空白，毛减少52,345字节。20261120的三个更早文件没有纳入，也没有写25及26–33的队列、请求、源码或参数。

## 官方终态与触发范围

六个实际运行的官方终态已在本题完整RET62/63/64来源账中保留，本次逐完整账读取并按精确JSON指针引用：

| 标签 | 实际run/attempt | 官方结论 | 原API updated_at |
|---|---|---|---|
|02|45800076687/1|completed/cancelled|2026-11-26T16:08:26Z|
|03|45811843606/1|completed/failure|2026-11-26T12:21:48Z|
|03b|45820592817/1|completed/success|2026-11-26T18:07:36Z|
|06|45904402595/1|completed/success|2026-11-27T04:00:29Z|
|11|46000835895/1|completed/failure|2026-11-27T12:53:58Z|
|18|46062343475/1|completed/cancelled|2026-11-28T02:05:35Z|

官方success、failure、cancelled均不改写逐步的科学返回或原未知。原失败、未完成父场、取消原因、各步缺输出和实际结论仍在完整来源账及原步骤记录，不由本格式整理补值。

五份对应workflow已整读：SO3-02、axisymmetric-03、normalized-parent-06、parallel11、parallel18的push.paths都只匹配各自actions-request路径。03和03b是同一workflow先后不同请求版本；当前03请求文件的request_id已是03b且followup_file指03b，本批不把它冒充原03的请求。两个旧完整followups仍各保原parent_request_id，原03请求版本由RET64完整历史合同恢复。

本批没有改任何request或workflow，没有dispatch、重新排队、改finish_when_done或假定已终态runner可续接。因此这些followups字节格式变化不匹配上述旧workflow的push触发路径。五份现存request与五份controller也完整读取，仅作为不变来源记录保留。

## 唯一文本变换与恢复

六份改件的完整原文固定在公开提交 `57bbee6ddee60445db5209074809f2269a9703c3`；每件原和新bytes/SHA256/Git blob均在映射中。字符串内所有字节与转义保持；字符串外仅删除ASCII空格、TAB、CR、LF，末尾一个LF。全部键、成员、数组顺序、命令参数、selector、预算、source/hash、数字token（包括-0、指数和大整数）、布尔和null原字不变。JSON解析只用于完整格式读取，不用于生成新正文。

新正文再次词法处理仍自身，保护时核实际完整Git blob。没有科学、AST、编译、fixture、benchmark或原科学重跑。既有manifest_bytes及whole SHA引用仍指原历史全文，不改标签。严格原whole读者应先用固定提交:原路径恢复全部旧字节，再核原身份；新紧凑体不冒旧SHA。

完整再生直接复用RET88已保护的3718字节通用词法再生器，schema和完整file_map合同原样，不重复源码：

```text
node scripts/resume_20261126/reproduce_complete_archival_metadata_json_lexical_format.mjs --manifest COMPLETE_MAP --source-directory COMPLETE_FIXED_OLD_CHECKOUT --output-directory SEPARATE_OUTPUT_ROOT
```

所有原文本和参数仍在当前六份完整JSON中，格式不是删参或摘要。根代理只在fresh HEAD六原bytes/Git blob精确相同后普通写新blob；本代理没有写ref、request或当前活动队列。映射给完整13个未改文件的身份和实际毛/净成本。
