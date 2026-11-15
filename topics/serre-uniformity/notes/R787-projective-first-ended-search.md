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

## 已完成的纯IO诊断（18:31 UTC）

[只读 run43747260495](https://github.com/Rogerhu12/math-research-public/actions/runs/43747260495)、job132913195823、source5317c0cd20dbd17588020b9f4e29f4b1dd1dfe2d 已成功。脚本11571 bytes/SHA256 `3332e8647bc1c0ada4ffa72b9ecc573c0cb80ecebf0635e912b5b4ffa5885d98` 只读旧产物；没有重做 LLL、旧行或任一数学计算。30个非carrier manifest成员连同manifest/reference实际读取校验；189MB载体只核已登记身份，没有冒称重新下载全载体或整ZIP。

实际完整 manifest 为5793 bytes、31条，SHA256 `422319cdb4ecdaaa54dfa5231855a4ae32cb72e67e1331bb51855876a72b9192`；ZIP另含manifest/reference，共33文件。小IO artifact14175065759、708676 bytes、ZIP SHA256 `d4c52df8588b1cdd181faff6f4eae3cff8cbca682843221d7c708c2adc17fdcd`，到期2026-11-16T18:31:57Z。

**五个初始节点全在首个坐标 C0 失败，接受前缀长度均为0。每个28维格的28个已核同余 LLL 行全部且仅因 denominator_bound 被拒绝；zero_delta、nonunit_delta、unchanged_or_duplicate 计数均为0。** 没有可接受子节点，因此实际只完成5个根节点，余队列0。原乘法常数K的十进制长度为59位；固定界为：

| shift | 分子上界十进制位数 | 分母上界十进制位数 |
|---:|---:|---:|
| 0 | 1906 | 1906 |
| 256 | 1983 | 1829 |
| −256 | 1829 | 1983 |
| 1024 | 2214 | 1598 |
| −1024 | 1598 | 2214 |

准确 stage manifest 为5612 bytes，SHA256 `7dbb5dfc32031878f7705222079dffefa327108ecf47de1a644e050e71a44301`；原子 queue 为4430 bytes，SHA256 `f4cd0e66a3f78aa6961abd0b875cf0eec17bd4f345a423455a11bc6831c87259`。这些实际状态否定“增大96节点预算即可继续本队列”的设想：当前队列已经空，节点上限不是原因。

$2KND<M$ 只用于固定矩形内的交叉积唯一性，并不是最终准确关系认证的必要条件。故本次输出只说明旧有限候选全部越过该充分界；既不证明没有更宽的准确候选，也不证明430位不足。下一次应采用确实不同的同时坐标候选机制，并保存全部新短行；是否成功仍由原free模式、Z展开、B非零及完整129×280准确式决定。原artifact未保存被拒短行，不能声称从旧小记录恢复它们。
