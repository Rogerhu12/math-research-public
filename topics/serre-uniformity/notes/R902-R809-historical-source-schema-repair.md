# R902 首次来源读取失败及 R809 原阶段格式修复

本条仅记录公开执行的真实失败与输入读取修复；没有新的数学结论，也没有已成 R902 阶段需要重算。

## 实际失败

- run **43879863247**，compute job **133342701870**，source **e7156baa787b071ee0e663ec1a038761376a3e7a**。
- wrapper 的 source_review 在原第610行访问旧阶段的顶层 result 时触发 KeyError；发生于 prepare 内，数学 core 尚未执行。
- 原 full-outputs-manifest.json 为282字节，SHA256 **5b0fc124dcd0b6d766bfa13bcdac1694e7bb80a6ee9bd5cb6e4933c65744c7c4**。仅有失败接收记录等三项；没有完整 input carrier。
- 原一日 artifact **14232680090**，1498字节，SHA256 **33ca3e27e9e7c48902459997f98d1c099d2539e956dc7322476acbb42268d076**；过期时间2026-11-17 13:52:57 UTC。失败记录不冒充数学反例或完成证书。

## 精确修复

原 R809 core SHA256 **dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d** 的 store 只把 complete 和完整 configuration 加入阶段 JSON；结果标识在 configuration.result 中。原 S5 index 与六C的正常 index/group 因而没有顶层 result。已成旧 wrapper 同样按此原格式读取。

R902 的 core Source.stage 和 wrapper source_review 只将已有 R827 历史分支扩为 **R827、R809**：

1. 必须不存在顶层 result，且完整 configuration 逐字匹配原 source tag。
2. configuration.result 必须等于该原 producer 的 result。
3. 其余 producer 仍要求顶层 result 精确匹配；报错加 group/file 便于定位。
4. 所有原文件字节数、SHA、完整 manifest、输入对象、单位图、原 target configuration、尺度断言和数学步骤不变。

修复后 core 为91925字节，SHA256 **b0f5510e3279d77462f6e15634d754f3e99f21db3510b2ce7afabd74aa564ee1**；wrapper 为73390字节，SHA256 **db561206e2a964db520de684975545f03b87017406aad1bcd9c02f7d204d3726**。helper、method、workflow保持原字节。

首run从未进入数学核，因此新的请求仍 resume=null，保原30对和300分钟预算；完整 R893/R896 输入及271件必要已成来源直接复用。仅做源码逐行差异与 AST 读取，没有在公开 Actions 之外执行数学。
