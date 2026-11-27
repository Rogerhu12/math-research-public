# Retention39：十四份旧 standalone optimization-intent 生成记录

## 1. 范围与完整恢复定位

本次只准备将以下十四份独立 `optimization-intent.json` 生成记录从当前树退存，总计 **1,237,451 字节**。完整科学源码、原请求、全部参数、真实结论、父 warm/status 与其原有恢复关系均保留。此说明和配套清单本身没有删除文件、修改运行队列或写 Git ref；普通保全提交由 root 执行。

[完整 provenance](../computations/legacy-standalone-intents-retention39-provenance.json) 为 **69597 字节**，SHA256 **`61e24084e6e17eb3f23c534f5a46f10866d947d9fe7069ef4bca26aa2528f62a`**。它保留十四个对象的全路径、Git blob、长度、完整 SHA256、真实原 run/source commit、完整 workflow/request 的身份、原科学命令和实际父关系。全部原对象的统一固定恢复提交是：

`1340d243733c1693ac57aa04043b7b9194fd14ed`

下表路径相对 `topics/visible-flex-larger-amplitude`。这些大小与 Git blob 已分别从该固定提交的真实目录元数据核对。范围精确到十四个文件，不包括同目录任何其他文件。

| 实际 run / request | 原路径 | 字节 | 原 Git blob |
|---|---|---:|---|
| 43598917532 / 17 | `notes/public-actions-43598917532-1-coupling112trust/constrained-warm/optimization-intent.json` | 2999 | `eac64056a266a083bbfa61bd7f24ab0253d438ca` |
| 43602070499 / 18 | `notes/public-actions-43602070499-1-trustresume/constrained-warm/optimization-intent.json` | 3043 | `6404481242a4b1ae9d5d3562a08113fd530b21ce` |
| 43603477207 / 20 | `notes/public-actions-43603477207-1-trustprotected/protected-warm/optimization-intent.json` | 10417 | `1d9cf499a44a6f77e760b9f3a5182e0f40b67231` |
| 43604874829 / 22 | `notes/public-actions-43604874829-1-trustmultiline/multiline-warm/optimization-intent.json` | 18746 | `bfa842128c2e52995fd44774cbe2ca383836b2b7` |
| 43608931469 / 26 | `notes/public-actions-43608931469-1-angleprojection/full-angle-warm/optimization-intent.json` | 27981 | `9e2e597442ec6a2109fc2d04f9742b601ac99ba0` |
| 43610469627 / 27 | `notes/public-actions-43610469627-1-sevenprojection/seven-angle-warm/optimization-intent.json` | 44702 | `871c8ce48ce5f25dded0f2a9fb0e5578864eb91c` |
| 43612331803 / 29 | `notes/public-actions-43612331803-1-observedseven/observed-seven-warm/optimization-intent.json` | 63195 | `59a944996043c6d2e5ed324a91991b41a79f3fb6` |
| 43614132961 / 30 | `notes/public-actions-43614132961-1-fullhprojection/full-H-warm/optimization-intent.json` | 83771 | `909a6a854c5af624e1d3cf55c9eca1304be2d25b` |
| 43614990381 / 32 | `notes/public-actions-43614990381-1-mixedquery/mixed-query-warm/optimization-intent.json` | 85625 | `23864a3d32466a8138f6e508806b7034dfd94a2b` |
| 43616658549 / 35 | `notes/public-actions-43616658549-1-tenquery/ten-query-warm/optimization-intent.json` | 116417 | `13d03526a4227b3c9313b5d30c3730a9457d0944` |
| 43618014985 / 37 | `notes/public-actions-43618014985-1-elevenquery/eleven-query-warm/optimization-intent.json` | 151073 | `fa0a22f520bf312d89ddc1b20c075978954ba5a2` |
| 43620111146 / 39 | `notes/public-actions-43620111146-1-twelvequery/twelve-query-warm/optimization-intent.json` | 189804 | `f6f3a7269343d6ac5a8e55ecaae6592a0e193022` |
| 43621054216 / 40 | `notes/public-actions-43621054216-1-twelvequeryqr/twelve-query-qr-warm/optimization-intent.json` | 195828 | `115d2eea06671ce72dfc2808ffc681e0d430d148` |
| 43623850723 / 42 | `notes/public-actions-43623850723-1-twelvequeryqr/twelve-query-qr-warm/optimization-intent.json` | 243850 | `0d9883994065a8df26b0d45c915c01c8f025bf76` |

前四份为 2,999、3,043、10,417、18,746 字节的小 JSON，本次已完整读取并核完整 SHA256。后十份的全 SHA256 直接复用已刊 retention28 provenance，且其路径、Git blob 与长度逐项相同；没有把旧全 SHA 说成本次重新读取大体所得。其中五份超过 100,000 字节，均未取正文。其余六位数父 warm/status 与二进制输入同样只读目录元数据。

十四项 SHA256 都有上述实际来源，不以 canonical JSON 摘要替代文件原字身份。完整 SHA 均在清单中；这里不重复展开第二张摘要表。

## 2. 为什么这些文件是可再生输出

分类依据是实际写入者及其完整输入，不依据文件名猜测。

`geometry_20261114_constrained_trust_warm.py` 先读取原 accepted/prepared/tail-anchor/tail-config，以及指定时的完整 parent warm。resume 检查读取 parent 的 `optimization_warm` 和原 mesh/profile/边界约束，再构造 identity，写出 `optimization-intent.json` 及初始 `driver-status.json`。若后续真的接受一个 warm，完整 identity 会进入新的 `optimization_warm`，并保留在 status 中。

`geometry_20261114_protected_tangent_warm.py` 与 `geometry_20261114_multiline_tangent_warm.py` 保留原输入全 SHA 和真实 parent warm 守卫；新 identity 的 `resume_producer` 来自 parent 内完整 `optimization_warm`。原三 query 定义、切空间政策和所有数值参数在各完整源内。两者写 standalone intent/status 后才进入主 `problem.evaluate`，并在实际新 warm 中继续保留完整 provenance。

后十份属于完整 full-angle 及其 seven/observed/full-H/mixed/ten/eleven/twelve/QR 后继。`geometry_20261114_full_angle_projection_warm.py` 的原输入读取和完整 parent 检查保持；它把 identity 写为 standalone intent，同时写入 status，新 warm 又保留 `optimization_warm=dict(identity,...)`。这些后继的完整源码、原生 query/策略和 read/write 关系已保存在原 source catalog 与 retention34/35/36 的完整审读记录中。本次没有重复复制这些数值生成数组。

本次完整读取了上述四个主写入源，以确认早期四份与后续共同引擎的具体读写边界。对于其余 wrapper，沿用已刊完整源和原参数恢复链，不冒称本轮重新全文审过所有依赖。各命令实际读取的是 `--resume` 指定的完整 warm，及明确需要时的 `--parent-status`；没有将 standalone intent 当作数值场输入。

此结论只覆盖这些真实生产/接续接口。若未来某个历史审计工具需要 standalone intent，应恢复该完整原文件后再消费，不以本说明的摘要代替它。

## 3. 完整源码与所有原参数保留在哪里

现有 [retention28 provenance](../computations/legacy-domain-manifests-retention-28-provenance.json) 为 86,924 字节，SHA256 `fde1e2a196a0bc5f3ca3aa0a1b2f2c1897239b7ba085583dd9c487b9a202f6a1`，Git blob `e1ca66df6b533a36d3a0ee49d4f907e8b3e8428a`。它保留 31 个完整来源文件的路径、长度和全 SHA，后十份 intent 的全源映射与完整 T112 config。前四份实际 source map 的 9、9、11、12 项也均逐项落在这个准确 catalog 内。本次共比较 **267 个已有声明的 source SHA**，均等于该 31 源 catalog 中的对应身份；这只是已有完整身份的比较，不冒新的数值验证。

十四份原 `.github/workflows/visible-larger-public-mainline.yml` 与 `computations/public-mainline-request.json` 已按各真实 run 的 `head_sha` 完整读取。清单逐项记下原 source commit、workflow/request 的整 SHA、Git blob、长度和完整原命令，原文件即可独立恢复每一个参数、默认值及分支。含其他并行 lane 的 request22、39、42 也原样保留，没有只抄本 lane 后删掉其他请求。

本次只将原科学命令的逐字连续文本放入新清单。完整 workflow 仍是环境、条件分支、原 setup、source restoration、后续 readout/publisher 的权威来源。对 request18 的 `WARM_ARGUMENTS`，清单另外明确实际 `trustresume` 分支为 `--resume … --iterations 1 --lsmr-iterations 200 --damping 270`，保留原 parent 全 SHA guard；没有误用同工作流另一 lane 的 `3/80/1` 默认数组。

全部主写入源的真实身份如下。其其他依赖仍由上述完整 catalog 和每项 source-map 指针恢复，不把默认值换成新的简表。

| 完整主源 | 字节 | SHA256 |
|---|---:|---|
| `geometry_20261114_constrained_trust_warm.py` | 19341 | `5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2` |
| `geometry_20261114_protected_tangent_warm.py` | 23355 | `b126ba6a203cbf97c4c9658abe70e9bf38ad259b2eab89bfed4c6e03f4d97fad` |
| `geometry_20261114_multiline_tangent_warm.py` | 25563 | `84318d97b5ce05282890710f71ffe0794896c2e88c498e8618a41625884aa359` |
| `geometry_20261114_full_angle_projection_warm.py` | 36439 | `7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152` |
| `geometry_20261114_seven_query_projection_warm.py` | 7431 | `f6598a5e4738f6c2c310eccc9fd791b68c3731ad3fc3adfd83414450d95c8394` |
| `geometry_20261114_observed_seven_projection_warm.py` | 13822 | `94395d54fcf58941180de23731fc2b5bb41fed8608dbda4c17903fffc862e228` |
| `geometry_20261114_full_metric_projection_warm.py` | 30576 | `8fb6411e7b876713725a80c2dbe9e322cc277001b0692ccc59e0edd59ec4e8b0` |
| `geometry_20261114_mixed_query_projection_warm.py` | 10173 | `d74d7a1c86cb131d262025cffa079a1a01a1ed7e5128ea339744c61cf4cfeac6` |
| `geometry_20261114_ten_query_projection_warm.py` | 13061 | `90e22ebbd0089970a77986f1be9352a1ec1581346a2fe2ef25478720136f6941` |
| `geometry_20261114_eleven_query_projection_warm.py` | 13402 | `6aed0dda5515945c73413884fb98d1719eb23fc40ff6b7388805f6108816c298` |
| `geometry_20261114_twelve_query_projection_warm.py` | 15035 | `10ed25405930f3775d8fb88f007aa50be4a53f4b3421904be959f1890ed67477` |
| `geometry_20261114_twelve_query_qr_projection_warm.py` | 29331 | `4b768828f754f75d760980d596f198984e92f5ceac79832123c74e42985a5c67` |

共同原科学环境为 Python 3.12.14、Node 24.22.1、NumPy 2.3.5、SciPy 1.17.0，均出现在十四份原 workflow。原 source restoration 实际调用 `exact_20261114_public_resume.prepare_public_source`；其完整恢复器、91 项原 source-dependencies 账本及对应恢复链继续引用 retention34/35/36 的已刊完整记录。

具体预算与参数全部未变：第一项原 `3` 次迭代、LSMR `80`、damping `1`；实际接续为原 `1/200/270`；各原命令的 `17` 条 line search、`1200` 秒预算、`2` workers、`4096` angles，以及各自 damping attempts/projection sweeps 都逐字保留。full-H 的 `600/180` 秒与两条 QR 的 `300/90` 秒、`1200` products、`64` inner iterations、`1e-8` 相对容差、`200` dual sweeps、`none` column-preconditioner 均仍在完整原命令里。两条 QR 的 max-active 分别是 **16 与 32**，没有合并成同一参数。

## 4. 原输入与完整 T112 config

下列输入恢复定位按第一项实际 source commit `4b8b2bfdd417f76574dcc2a8e2353c4c2dce3e21` 真实目录元数据取得。全 SHA 来自完整原 guard/已有参数记录，未整读大原输入。完整路径、Git blob 和固定恢复提交都在清单中。

| 原输入 | 字节 | 原 SHA256 |
|---|---:|---|
| accepted099 | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared112 | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| original_tail_anchor | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| complete_T112_config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| original_boundary_response_check | 38794 | `4bacf0bdbf00fd919e4de48f0b36c8322d2ea26539abeac9b9ddcf7c0db6bf7f` |

原 workflow 核 prepared112 和 boundary response-check 的原 SHA，随后复制原 `prepared.json.gz`、`response-check.json` 与完整 `T112-config.json` 到当次输出目录。完整 config 的原 160 项 valleyControls、全部 caps/warp/mesh/modes/quadrature/solver 参数保留在原 2,161 字节文件中，且 retention28 的 `entries[0].complete_config` 也保留完整对象。新清单仅精确引用该文件与原对象，不再复制其数组，也不把重序列化的 JSON 当作原字节。

这四个科学输入与恢复步骤实际检查的 response-check 均不在删除范围。参数来源是原真实输入，不由十四份 intent 的摘要推测。

## 5. 每个实际父关系与旧结果恢复

下表按原科学命令排列。所有非空 parent warm，以及六项显式 parent-status，其原路径、严格原 SHA、字节数、Git blob 和正确不可变恢复提交已保存。目录元数据确认文件确实存在于所列提交；没有假设它们仍在当前 main，也没有整读任何大型 parent。

| 子 run | 原 parent warm | parent-status |
|---|---|---|
| 43598917532 | 原 prepared112，未指定 resume | 未传此选项 |
| 43602070499 | `public-actions-43598917532-1-coupling112trust` / `warm-003.json.gz` | 未传此选项 |
| 43603477207 | `public-actions-43602070499-1-trustresume` / `warm-001.json.gz` | 未传此选项 |
| 43604874829 | `public-actions-43603477207-1-trustprotected` / `warm-001.json.gz` | 未传此选项 |
| 43608931469 | `public-actions-43604874829-1-trustmultiline` / `warm-001.json.gz` | 未传此选项 |
| 43610469627 | `public-actions-43608931469-1-angleprojection` / `warm-001.json.gz` | 未传此选项 |
| 43612331803 | `public-actions-43610469627-1-sevenprojection` / `warm-001.json.gz` | 未传此选项 |
| 43614132961 | `public-actions-43612331803-1-observedseven` / `warm-001.json.gz` | 原 workflow 显式要求 |
| 43614990381 | `public-actions-43612331803-1-observedseven` / `warm-001.json.gz` | 未传此选项 |
| 43616658549 | `public-actions-43614990381-1-mixedquery` / `warm-001.json.gz` | 原 workflow 显式要求 |
| 43618014985 | `public-actions-43616658549-1-tenquery` / `warm-001.json.gz` | 原 workflow 显式要求 |
| 43620111146 | `public-actions-43618014985-1-elevenquery` / `warm-001.json.gz` | 原 workflow 显式要求 |
| 43621054216 | `public-actions-43618014985-1-elevenquery` / `warm-001.json.gz` | 原 workflow 显式要求 |
| 43623850723 | `public-actions-43621054216-1-twelvequeryqr` / `warm-001.json.gz` | 原 workflow 显式要求 |

两个分支尤其不能按时间顺序补父：`mixedquery` 仍取 `observedseven` 的真实 warm，未改用 `full-H`；首次 `twelvequeryqr` 仍取 `elevenquery` 的真实 warm/status，未改用 `twelvequery`。末次 request42 QR 才取实际 request40 QR 的完整 warm/status。request18 则保留原 `warm-003.json.gz`，不误改成 `warm-001`。

恢复 parent 使用各子运行原 source commit 中确已存在的对象，这是原 workflow 当时实际消费的身份。后继 request45 对 actual42 的完整 warm/status 恢复链已在 retention36 全账本保留；本次不删除、不重写这一链。原 status 及 warm 内的完整 producer provenance 也不因删除 standalone 副本而被改动。

实际 GitHub API 记录中，两项 workflow 的整体结论为 failure，其余为 success；清单逐 run 保存其真实状态。这个字段只表示该 workflow 的返回状态，不能替代原 warm 接受结果，不能推论 failure run 没有已产生的 warm，更不能把 success 称为新闭面完成。原真实科学说明和输出恢复记录全部保留，本次不再重述或重算其数值结论。

## 6. 当前研究入口与准确原字恢复

[retention34 完整审读](2026-11-27-legacy-condensed-intents-retention34-readonly-review.md) 已逐源检查当前 axisymmetric warm 入口：从固定 accepted099 恢复，再执行本次完整 prefix 链，后续 pulse/assembly/Hold/mode 消费实际新产文件。它不把这批旧 standalone intent 当数值输入。这里复用该已刊精确输入链结论，不另设一次历史扫描或科学重跑作为出版门。

需要原 intent 时，可在独立 scratch 用 `git show <固定提交>:<完整路径>` 输出原始字节，再核字节数、Git blob 和清单中原 SHA256。通过原 Git 对象恢复不要求旧 Actions artifact 仍未过期，也不要求重新求解。对父 gzip/raw JSON，同样先核原字节身份，不应先解压重压或 JSON 重序列化再声称全 SHA 相同。

若确有科学再生需求，应使用原 source commit 的完整 workflow/request、全部原输入和参数，在授权 Actions 中执行。即使公式和参数相同，也不承诺另一轮浮点执行逐字重现；精确历史原字已有上述固定 Git 恢复位置。退存动作不触及任何当前变量、阈值、预算、已发现材料地点或未知历史义务。

## 7. 交付与边界

配套 provenance 的 `delete_entries` 精确列出上述十四路径，使用普通 tree 删除条目；本说明没有执行它们。独立小 delete-entries JSON 仅便于 root 操作，可不重复入库。净空间应由 1,237,451 字节减去实际入库的新清单与本说明计算，不把保留历史 Git blob 说成仓库历史已被物理清除。

本次工作限于完整小文本/原 workflow/request 读取、目录元数据、已有 SHA 比对及内存 JSON/文本检查。没有读取后十份 intent 正文，没有拉取大型 warm/status/二进制原件，没有本地科学计算、AST/compile 或新科学返回。原 sources/requests/config、全部原参数和真实结论原样保留，当前 actual10 研究继续推进。
