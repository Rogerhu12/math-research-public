# 三份旧 condensed optimization-intent 的第 34 次退存候选只读审查

日期：2026-11-27。此文和配套完整 provenance 只提供退存依据；本次没有删除文件、修改分支或运行科学计算。

## 1. 结论与精确范围

以下三份 `optimization-intent.json` 可以作为**当前目录中的旧生成记录**退存。依据来自原生产源的写入点、后继实际消费入口、完整参数与原字恢复链，不是从文件名判断。固定提交 `cf41802e7a538f1b3595397681d3371aebf4018d` 中，三份原文件的 Git blob 与长度已经逐项重新读取目录元数据核实。当前目录元数据也与之相同。

| 原 run / request | topic 内相对路径 | 字节数 | 原 Git blob |
|---|---|---:|---|
| 43640358327 / 60 | `notes/public-actions-43640358327-1-condensedqp/seventeen-condensed-warm/optimization-intent.json` | 772,554 | `ddf45205f5d11a7e6ef18fc2ac48966222cd8e62` |
| 43638348140 / 58 | `notes/public-actions-43638348140-1-condensedqp/seventeen-condensed-warm/optimization-intent.json` | 690,816 | `c044f6f818bfc9973e9ff4fa7c473010df461016` |
| 43636630003 / 56 | `notes/public-actions-43636630003-1-condensedqp/sixteen-condensed-warm/optimization-intent.json` | 612,911 | `2d85e265d63735ddc74377179dc24190fb98864b` |

三份合计 **2,076,281 B**。这是当前 topic 文件树可减少的毛字节数，不是 Git 历史或远端对象经过垃圾回收后的体积承诺。新增本说明与完整 provenance 的字节仍应计入当前目录容量。

本次始终没有整读这三个大文件，没有从目录元数据推造 SHA256；配套 provenance 的候选 `sha256` 明确为 `null`。原 Git blob、固定提交、完整路径和长度构成此次可复核的恢复定位。

## 2. 为什么这是生成记录

已完整读取原 `geometry_20261114_full_angle_projection_warm.py`，SHA256 为 `7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152`。其主流程从实际输入文件和父 warm 的 `optimization_warm` 建立 `identity`，其中完整保留 `resume_producer=current["optimization_warm"]`；随后明确执行：

```python
write(args.out/"optimization-intent.json", identity)
```

同一个现场 identity 进入 `driver-status.identity`；实际接受的新 warm 又将它写入自己的 `optimization_warm`。16-query 与 17-query 的完整生产源、只读 collocation wrapper 继续注释这一现场对象，再由原写入点输出。嵌套父来源是这些 intent 的实际内容来源，不能把它们当作纯文件名占位符。

已经完整读取的 16/17-query 后继 parent binding 要求的是实际 `warm-001.json.gz`、原 `driver-status.json` 的完整 SHA、完整生产源、accepted/prepared/anchor/config 以及参数身份。物理方向检查入口从 `--prepared` 读取实际接受 warm。这些入口没有打开独立的 `optimization-intent.json`。本结论只覆盖所列明确入口，不宣称任何历史审计程序或未来新程序都不会请求该记录；需要它时必须恢复原字节。

配套 provenance 逐项列出 12 份本次完整读取的小源与源账本，并保留每份完整路径、长度和 SHA256。原 source closure 的其他成员保留在现有全源账本和每次原请求中，没有把未在本次重新全文审读的成员标成“本次已重审”。

## 3. 原生产参数与完整输入没有被削减

已有两份小账本已完整读取，并应原样保留：

- [第 30 次 provenance](../computations/legacy-condensed-manifests-retention-30-provenance.json)，49,041 B，SHA256 `17a1d795952ce8eeda11660f043132bbf5e1cc3b098f5c0f79f4716926eb47fe`。
- [第 30 次全源账本](../computations/legacy-condensed-manifests-retention-30-sources.json)，30,464 B，SHA256 `b853135bb64ca987e701a0da3436e8d602459bfbc55f9da97b3be916bbcd4472`。真实文件名为 `sources.json`，不是 `complete-sources.json`。

三个 `legacy-condensed-source-parameters-run…-retention30.json` 保存了各原 manifest 中全部非文件数组字段；本次完整 provenance 同时嵌入其完整字段值和原请求对象，并记录原文件整 SHA。嵌入值只便于阅读，原 JSON token 与原字身份仍以保留的完整文件为准。

每次实际运行的完整 `.github/workflows/visible-larger-public-condensed-qp.yml` 位于以下真实 source commit：

| Request | 原 source commit | workflow 字节 / SHA256 |
|---|---|---|
| 56 | `b8a19c16fc1363ffa1a66f39b9403e0dfa93e169` | 19,038 / `19042db5c2952eab02a3414cdce469e21f4390af870a6e28e78ad6feb823e91d` |
| 58 | `ba8bc4f4acd547fd5219826da4f6e35f859bca56` | 19,716 / `e20894668ca056f7c66860bd763d7027fdb95b20cd3f1618a4135abf85738dc7` |
| 60 | `da346d172715761d7da23da84c92d97a92b438de` | 19,726 / `3b6dc7385b7a5e06dbcebb09bd3a73c2301cc361fbb9face54e471de14b0530a` |

完整 provenance 保存了三条原科学命令及三条原物理方向检查命令的逐字摘录；其余设置和恢复命令仍在以上完整 workflow 中。原 request56 的完整 5,073 维和 request58/60 的完整 5,411 维局部 B 支持、16/17 个 query、working 512、一次迭代、damping 270、LSMR/projection/dual 各 200、17 条原回溯、1200 秒总预算、600 秒 condensed 预算、90/30 秒保留预算及 4096 角参数均保留，没有借退存改变任何一项。

原公共源恢复器 `exact_20261114_public_resume.py` 的实际调用方法是 `prepare_public_source`。它从完整 91 条 source-dependencies 账本中恢复并核对原 workflow 选择的 78 份公共数值源；不是重新执行该文件另一个独立 RK 读数 main。原请求的 publisher SHA 与当前 publisher 的漂移单独保留，不能用当前 main 代称历史源码。

共同原输入仍明确是 accepted099、prepared112、原 tail anchor、完整 T112 config，以及每次实际父 warm/status 对。其长度、全 SHA 和不可变 Git 恢复位置均在 provenance 中；accepted/prepared 等大输入本次仅核目录元数据和原严格源守卫，不整读。

## 4. 实际父与结果原字恢复链

三个实际父关系为 request 53 → 56 → 58 → 60。每个子运行都留下 `parentXX/restore-identity.json`，记录父 warm 全 SHA、status 压缩字节 SHA、原 status JSON 解压后 SHA 与字节数，并明确没有重序列化原 JSON。

本次同时核实原输出所在的后继固定提交：

| 原输出 | 可恢复它的固定提交 | 原 warm Git blob | 原 status gzip Git blob |
|---|---|---|---|
| actual53 | `b8a19c16fc1363ffa1a66f39b9403e0dfa93e169` | `05c1ca2edd7174388363a7efba2a3429ff8b2fb2` | `8db08609f9535a8faae0c3e602b7a5284ef592f2` |
| actual56 | `ba8bc4f4acd547fd5219826da4f6e35f859bca56` | `defbe0104a97d4bc62a48a011602b109440d5b77` | `1dfd5a14962fc132a8e0de9f367354f319ff8df0` |
| actual58 | `da346d172715761d7da23da84c92d97a92b438de` | `50d87ebd89d609b765eaa1de3e7102fb2d50f667` | `c129e6b39ae160cca7658297e79dc29ba7db78e8` |
| actual60 | `cc813fa7521098fdeba86b8bf8c0fe7d8c96bba0` | `8b2749b69fb76da43dd8f88d867e122a6616b85b` | `1e6bda451b6e8cfc7f51012587f606c34f59afb7` |

这些都是本次真实取得的历史目录元数据，不是假定文件仍在当前 main。原 warm/status 曾因其他已登记退存离开当前目录；此次不删除它们的恢复记录，也不把当前目录只剩 intent 误报为完整科学输入仍在场。

精确恢复 intent 用固定提交的 `git show <commit>:<完整路径>` 输出原始字节到独立 scratch，随后核 `git hash-object` 和长度。此处不需要重新求解原科学问题。对 status，应先核 gzip 原字节，再解压核原 JSON 字节；不得先解析并重排 JSON 再声称通过原 SHA。大原文件不经集成全文读取接口搬运。

## 5. 必须继续保留的真实科学结论

以下三份实际说明均已完整读取，应留在当前 topic：

- [actual56：left468 与 collocation 位置](2026-11-14-actual-request56-left468-and-collocation-location.md)。
- [actual58：quarter-step 与既有域约束](2026-11-14-actual-request58-quarter-step-existing-domain-limit.md)。
- [actual60：left-RMS467 与 seventeen-query 接续](2026-11-14-actual-request60-left-RMS467-limits-seventeen-query-continuation.md)。

| 实际请求 | 接受 alpha | 同一次 fresh merit 起点 → 终点 | 最近较大拒绝 alpha 与实际原因 |
|---|---:|---|---|
| 56 | 1/32 | 44.10538196200878 → 44.084143195501056 | 1/16；原 left RMS interval 468 |
| 58 | 1/4 | 44.08450062286488 → 43.925384505081816 | 1/2；已建模 midpoint 473、475、481 |
| 60 | 1/64 | 43.92644933127726 → 43.91793532799495 | 1/32；原 left RMS interval 467 |

三次完整 affine 方向检查都低于原 `5e-5` 阈值，最大相对误差分别为 `6.957649122839063e-10`、`7.108999873259166e-10`、`7.009663695797188e-10`。这仅记录已经返回的有限检查。三次都只有一次 warm 接受，没有执行并完成新的完整 native tail/full closed BVP，也没有完成研究目标。不同请求重建权重后的 fresh merit 不用来拼成跨轮同一个目标的严格单调链。

## 6. 当前 axisymmetric warm 是否直接消费这三份 intent

本次完整读取以下实际当前入口：

| 源 | SHA256 |
|---|---|
| `scripts/resume_20261120/reproduce_and_solve.py` | `067b3f2e14145a6f88b2d171c555f1174f0505b45a5aaf670c3ec2610f7c286d` |
| `scripts/resume_20261120/rebuild_fullclosed.py` | `4e9ddeaeef2a0ab8b1b38b1412eb066b53578dd649d8f9b4d1a077c7256dee6b` |
| `scripts/resume_20261120/rebuild_closed_warm.py` | `63950b72e75e8b6497ad2119ca16076c2c8749f9615166beb6d52adcab86708e` |
| `scripts/resume_20261126/rebuild_axisymmetric_so3_warm.py` | `561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4` |
| `notes/2026-11-17-parallel-model-fullclosed-hold-warm.py` | `bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3` |

上表五个完整 SHA 与实际取得的完整源码一致。以下说明来自这些入口的完整读写链，不从 intent 缺席猜测递归输入。

实际 recipe 调用 `reproduce_and_solve` 时不带独立 implementation 分支。它先从固定 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 恢复 accepted099 原始输入并核完整 `b4d2…`，然后执行五段新 prefix：`continue0991`、`continue0992`、`refine0992m112`、`continue0993m112`、`continue0995m112`。后续 pulse、assembly、Hold、mode warm 消费本次实际产生的文件和完整 source pins。

这些入口没有读取三份候选 intent，也没有把 request56/58/60 的 standalone identity 当作当前 warm 输入。五段 prefix 的新输出被明确记为新 reproduction，不把新 SHA 假称历史末点。全部 21 个 recipe 声明源 pin 已抄入 provenance；本次完整重读的是上表五个入口与写入者，不宣称对另外 16 份源重复进行了全体审查。

因此，移出这三份旧生成记录不会切断已检查的当前 warm 入口。这个结论不授权删除 accepted099、当前 warm、原参数、生产源、真实状态恢复记录，或任何完整材料点历史。

## 7. 范围、核验与交付

[完整只读 provenance](../computations/legacy-condensed-intents-retention-34-provenance.json) 保留了三候选全定位、三原请求、三个完整参数对象、全部原命令、共同原输入、四组真实 warm/status 恢复链、两份既有 retention30 全源账本、当前入口源闭包，以及上述实际结论的原说明 SHA。

本次仅执行远端公共源码和小元数据读取、内存文本比较、哈希和 JSON 结构检查。执行环境不可用，没有新 AST/compile、科学求值、局部数值试验或原科学重跑；也没有把“未读”填成“通过”。所有三个候选大本体保持未取。

建议 root 在同一次普通保全提交中保留本两件小记录，且只移出第一节三个路径。是否实施与普通提交由 root 完成；此审查本身没有进行删除或 ref 写入。以后若历史审计确实需要完整 intent，应先按固定对象恢复原字，再运行其真实消费者。

## 8. root 实施记录

本节接续上面的只读审查。root 在 `8e32b487661e9ee886f8c4968dcf4d31015e9938` 的完整 topic tree 中核三候选仍与固定 `cf41802e7a538f1b3595397681d3371aebf4018d` 的长度及 Git blob 完全相同，并核十二份完整小源的长度、SHA256 与 Git blob；另阅读原 engine identity 写入、父 `resume_producer`、warm/status 继承、16-query 注释及实际物理方向 consumer 的读写位置。上文完整参数、命令、输入恢复和真实结论原记录均未改。

本次普通提交仅从当前树退存第 1 节三个旧生成 intent，总计 2,076,281 字节，同时保留本说明及完整 provenance。原字恢复位置不变；没有删除完整源、参数、当前状态或结论，也没有另存原始数组或声称历史 Git 对象被清理。三个大本体仍未读取；没有本地科学计算或新 AST/compile。双 README 的完整 SHA 与既读规则一致；这是云端核对，不冒称真实 pull。09、10 的实际执行记录原样保留，研究继续。
