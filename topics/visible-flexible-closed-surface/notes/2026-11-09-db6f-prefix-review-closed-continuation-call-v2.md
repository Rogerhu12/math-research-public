# 闭 continuation call 元数据检查器 v2：差分独审

审查者 `/root/coupled_prefix`，2026-11-09。**静态差分与指定 call001 纯 metadata 独立重放 PASS。** 不改变 v1 审稿/输出，不重跑数学求解。

冻结 v2：`scripts/db6f-root-audit-closed-continuation-call-v2.py`，SHA256 `11ce0ce2446955093a1be749534f73017d22df55fad3d2276bdf46b5df4be2e1`。我逐行审查相对已审 v1 `6e43e269…` 的完整差分，确认仅增补输入关联和数据结构断言，没有改变响应、尺度表达式、残差门或生成原数据。

- launch argv 在这条固定 controller 管线中全部是 key/value 对；长度、重复 key 与 controller 绝对路径检查正确。新断言把 runtime original config、target、resume record 连接回 launch 的对应参数，而非仅接受 runtime metadata 的自报路径。
- controller/client 当前 SHA 对应 runtime binding；resume SHA 同时等于实际文件与 launch 已冻结的响应 SHA。target 的保存高度向量也必须与 runtime binding 全值相同。
- 响应 source 字典现在要求恰好包含原 continuation client 的八个源，再逐个匹配 66 文件冻结来源；遗漏源不再能只靠其余成员检查通过。
- 完整 stage 节点数等于 resolved `depth+1` 且等于原真实 warm；rawNode 必须逐值等于该已绑 warm 的映射，各索引为非 bool 的合法整数，rawStates 必须等于这些索引处的 full states。此指定 warm 已有 865/13 完整布局的独立核查，因此当前链条覆盖原映射。
- scale 明确拒绝 bool。原参数/guard/物理路径、闭日志检查和中间 `audit=False` 的范围保持。

独立命令仅将 v1 重放命令中的脚本名换成 v2，输出改为 `2026-11-09-db6f-prefix-review-continuation02-call001-metadata-replay-v2.json`；实际 exit 0。新输出与作者 `2026-11-09-db6f-root-continuation02-call001-closed-audit-v2.json` **逐字节相同**，SHA256 均为 `b4c59aa5b882dbeb78c5eec56528c7509023af04d1f6412f3d89629887453e33`。

数学状态不因加固而改变：call001 是 $s=.3125$ 的原方程有限 DN warm，保存 residual 为 $2.467580868048873\times10^{-10}$，5 个 history 基点。这里没有独立重新求解、最终 $s=1$ 审计、前缀联解或连续几何声明。v1 当前数据也不撤销，其缺少的通用断言已由我的独立补核支付；未来闭 call 可使用 v2。
