# 第28次旧派生清单保留处理：十份 domain manifest

本次按根 README 的 raw 保留规则，只从当前树移出下表十份历史运行生成的 `domain-operator/manifest.json`，合计 **2,590,917 bytes**。全部原配置、完整 `optimization-intent.json`、原输入、所有完整源码及其余 sibling 原样保留。没有运行科学程序，没有把派生数组或历史输出改名当作原始输入提交。

## 1. 固定恢复与逐件身份

全部十份准确原字节都在已公开固定提交 `1f102dc8df41ada504a9d30e56bad92be01bde90`。本次先查大小，再流式核 whole-file SHA256；同时逐件核当前工作树 Git blob 及固定历史 blob 的大小相同，没有整读这些大 JSON 的数组。

| 原 topic 相对路径 | bytes | SHA256 |
|---|---:|---|
| `notes/public-actions-43623850723-1-twelvequeryqr/twelve-query-qr-warm/domain-operator/manifest.json` | 337154 | `d76c49ab742ab7f43a2dd3c888cb4d6f0bcb5eac9f43ec6c9cd624ab16ddc7cc` |
| `notes/public-actions-43621054216-1-twelvequeryqr/twelve-query-qr-warm/domain-operator/manifest.json` | 337146 | `bf275ecdaf1288ff8b961264afd09f70dd121e8f457c29628c26ed29aba4bcb5` |
| `notes/public-actions-43620111146-1-twelvequery/twelve-query-warm/domain-operator/manifest.json` | 337146 | `c2eff3284fed6d294434d4b8be82fcaf8e25394e33caa21d32854ea139b16094` |
| `notes/public-actions-43618014985-1-elevenquery/eleven-query-warm/domain-operator/manifest.json` | 310216 | `13f62ebdf20b7a44b1a71ab01fe4dae934429fbfcbebaed4b0108e24b8ba330f` |
| `notes/public-actions-43616658549-1-tenquery/ten-query-warm/domain-operator/manifest.json` | 286178 | `54d90b2521bc538bf12f65234cc9cf4074db776532ed217c0ac3857e61af686a` |
| `notes/public-actions-43614990381-1-mixedquery/mixed-query-warm/domain-operator/manifest.json` | 258962 | `e3eae53de48e197f4bd4169c30d6b6da85210fd12147e2c54aceeb2c40df2300` |
| `notes/public-actions-43610469627-1-sevenprojection/seven-angle-warm/domain-operator/manifest.json` | 193501 | `5a431c41bc6508a2556321682e3157bbff59dff6d85122c10285d12536d8ed0c` |
| `notes/public-actions-43612331803-1-observedseven/observed-seven-warm/domain-operator/manifest.json` | 193496 | `00c1439c9b6e176a3cb26c56a53dbb0c65edc4ac40e651d3f07b3377a0732668` |
| `notes/public-actions-43614132961-1-fullhprojection/full-H-warm/domain-operator/manifest.json` | 193495 | `1a949ada2d51d44678beab947028047e742fff7587002b9ccd7c3685deebe716` |
| `notes/public-actions-43608931469-1-angleprojection/full-angle-warm/domain-operator/manifest.json` | 143623 | `b06b88f5d426c84a6e7697d561caa7cc68e523d6414d2d6d647cc08e9acdac11` |

完整 Git blob、原 intent/配置的 whole-file 身份、全部来源声明和31份实际完整源的身份保在 [保留来源账本](../computations/legacy-domain-manifests-retention-28-provenance.json)。该文件为 86924 bytes，SHA256 `fde1e2a196a0bc5f3ca3aa0a1b2f2c1897239b7ba085583dd9c487b9a202f6a1`。它保留完整原小 T112 配置和原顶层完整 source map；不替代仍留在原处的完整 intent。

## 2. 原参数完整留在原处；读取范围明确

十份原 `T112-config.json` 均为2161 bytes，whole SHA256 `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`；每份原文件及其完整配置值均保留。十份完整 `optimization-intent.json` 分别为243850、195828、189804、151073、116417、85625、44702、63195、83771、27981 bytes，全部原路径不动。它们保有原 prepared/accepted/anchor/config 身份、真实 resume、完整嵌套 resume_producer、原网格、查询及投影参数。

本次对每份 intent 只读至多前16384 bytes，解析其中完整的顶层 `source_sha256` 对象及顶层身份字段，未整读大 intent。此前已经实际完整读取的44702-byte 小 intent 也不因此被改写为全部十份均已完整读过。全部原参数仍由各原完整文件保存；不存在的 request-identity 文件没有被补造，未凭部分元数据虚构科学 argv 或预算。

十份原顶层来源声明共有226项、31种完整源码；逐项与当前完整源码的 SHA256 相符。root 对全部61个不同文件（十份清单、十份 intent、十份配置、31份源）核当前 Git blob 与固定提交相同并核 blob 大小，未把后来修订的源冒作旧版本。

## 3. 实际生产路径

root 完整读取 `geometry_20261114_full_angle_domain_operator.py` 的 export（原655–708行），再完整读 mixed-query export 与其全部差异；ten/eleven/twelve 三个 export 的后续差异仅 query 数量的 docstring 和 artifact_scope。五份完整源都保在 computations 中：

| 完整生成源 | bytes | SHA256 |
|---|---:|---|
| `geometry_20261114_full_angle_domain_operator.py` | 38319 | `af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7` |
| `geometry_20261114_mixed_query_domain_operator.py` | 26683 | `34115f81cf5a09c3d07a6b79f408459fb014ca580ad0a992f8a639ff937ba854` |
| `geometry_20261114_ten_query_domain_operator.py` | 27338 | `5c9b145862a4f12cbbc5334e1b96e540458a58908c4889b966979995700d5dbd` |
| `geometry_20261114_eleven_query_domain_operator.py` | 27346 | `55358acb92bac869ba2ca1daf2da7772d57be31ccd1fcfd9f7324af80f8ea20b` |
| `geometry_20261114_twelve_query_domain_operator.py` | 27284 | `6a428d2f8412659cbd318321aa992c3b4565ff41177131a9cc9d268c6fbb7b1f` |

这些 export 都从本次真实完整 capture、已有 fixed factors、全角 rows 和 endpoint J/P 写出全部 payload，再把 `description()` 及所写文件身份写为 manifest。mixed/ten/eleven/twelve 还完整写出原 midpoint 输入。它们拒绝覆盖旧文件，最后清空 factor cache；清单是实际运行的派生输出，不是该次模型的初猜。

实际调用者 `geometry_20261114_full_angle_projection_warm.py` 原465行调用 `domain.export(args.out/"domain-operator")`。seven/observed-seven 的原链指向此 engine，mixed/ten/eleven/twelve 分别设置自己的完整 capture 和 domain 类后调用同一 engine；full-metric 与 twelve-query-QR 的完整上层源及参数照原处保留。全部31份完整源的身份均在账本中；本次没有执行它们。原源码中的历史 artifact 文字按历史保留，不授权新增 raw 上传。

## 4. 恢复与消费责任

在 scratch/runner 中用 `git show 1f102dc8df41ada504a9d30e56bad92be01bde90:topics/visible-flex-larger-amplitude/<表中路径>` 取得所需清单，并核对应完整 SHA。固定历史能恢复原字节，单靠 SHA 或重新运行不能保证逐字复制原浮点记录。

恢复清单不等于恢复它枚举的完整 payload；真正运行旧动态读者时仍须供给所有实际原输入和载荷。没有声称所有动态消费者已枚举，也不允许缺清单时改成空列表、删行或默认成功。现有未知科学返回、原失败、旧结论、06/07历史责任、08/09新计算与全部完成标准均不因本次保留处理改变。
