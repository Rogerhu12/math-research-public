# 原430位 projective 首轮有限候选搜索的实际结束记录

**状态：已完成的公开计算记录；未得到原 A/B 关系。** 本记录只登记实际执行边界，不把固定有限搜索的失败当作430位不足或关系不存在的证明。原同核 Dixon 续算继续。

## 真实来源与执行

| 项目 | 实际值 |
|---|---|
| 公开 run / job | [43745966802](https://github.com/Rogerhu12/math-research-public/actions/runs/43745966802) / 132909298032 |
| source commit | d71d40bb6cbea1cecc9c23f2efd47401da35cc53 |
| projective core SHA256 | e0a5ad95b06bbd75319b1464f5c1b629d3f64d919758fbe7e0a76ad3c41963cb |
| IO wrapper SHA256 | b2c4efda15f7a0f8857f24f0b20484f719a46f963666e691c25b2371c3fe9a9b |
| 数学耗时 | 71.02357375700004 秒 |
| 数学进程退出码 | 2 |
| 结束 UTC | 2026-11-15T18:20:50.050311+00:00 |
| artifact | 14173922406；189847233 bytes；33 files |
| artifact ZIP SHA256 | 37d11e2835b4963cbebfc4c7e199e0fc218251442c372c78fc7e21a4d2cbef23 |
| core receipt SHA256 | d6e40af94cb2d553c46804b1e89cfbfd65b4e3ac9c544d1b1d16ab1a195ba4c6 |
| 未完成 certificate SHA256 | 380717ae1b382198ed282e72e2e20c9180a926d5d63d4a62f1e35594f8ccedd5 |
| artifact 到期 UTC | 2026-11-16T18:20:50Z |

原输入仍是 run43708449812 的完整430位 checkpoint；其 run/source/manifest/lift pins 与[方法](R787-original-projective-reconstruction-method.md)、[430位原断点](R787-430-digit-checkpoint-and-same-core-continuation.md)一致。没有增加 Dixon 位数、重新求14个分支逆或重做旧 Laurent 行。

## 日志实际确认的边界

最终 `PROJECTIVE_RUN_RECEIPT` 与 `PROJECTIVE_PRESERVED_IO_REVIEW` 一致：`complete=false`、`candidate_search_exhausted=true`、`search_node_budget_reached=false`、`exact_verified_orders=0`、`same_normalized_1186_direction_verified=false`。全部已完成阶段保留。因核心返回2，workflow的容错 compute 步骤显示 success 并不表示关系成功；verify 按未完成状态返回1，整体 run 失败是正确的语义。

结束后的同次 IO 校验确认全部 output manifest 文件及1380个活跃输入的 bytes/SHA 正确。旧载体1372成员全hash后，实际保留 R787 的1242项、R781的134项与R786的4项。新必要输入载体 `R787-retained-producer-inputs.tar.gz` 为189156436 bytes，SHA256 `6f56f1c8cde9c1e5885d36e417d8144c6e84204eabb5b67f6b8d30148af48b20`。这是实际新产物；不把旧载体摘要冒充它。

## 解释和继续的准确范围

当前代码使用五个固定唯一性矩形和每个失败探针的至多28个 LLL 行，每节点只保至多8个可接受子节点。队列耗尽只否定这次有限候选集合。它没有给实际解的高度上界，故不能推断430位必不足；尤其需区分分母界限筛除、非单位筛除及其它拒绝原因。准确节点数量、首个失败坐标和各拒绝计数以随后纯 IO 提取的小记录为准，本记录不预填它们。

接续先读原 artifact 的 rectangles、scan、LLL-children、node、queue 和完整 manifest；不重复已经完成的数学阶段。只有根据实际小记录提出不同候选机制或必要更高精度后，才发新的算术请求。原 run43737413555 的同核430位续算保持运行。R792/R804/R809 的真实 A/B 消费入口仍未激活；beta、极理想、eta、规范高度与全p主目标均未因此完成。

原始机器文件仅保存在一日活跃 artifact；本 Git 记录只含脚本/请求引用、来源 pins 和上述解释。
