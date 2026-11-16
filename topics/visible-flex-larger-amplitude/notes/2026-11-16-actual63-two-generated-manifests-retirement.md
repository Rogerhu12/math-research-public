# actual63 两项历史生成清单的当前树清理

作者：AI（geometry 调查，root 审读与发布）；日期：2026-11-16。依据根 README 第15条，本次用普通提交删除下列两个已核生成输出；不改写历史。调查和复核仅用源码文字、JSON/Git 字节元数据与已有结论，没有科学执行、项目导入、AST、编译、测试或新科学门。

## 结论与范围

本次普通提交只删除下表两条当前树路径，保留所有源码、配方、原始输入、warm/status 父数据以及已有紧凑结论。两件共 **1,441,937 B**，是 actual63 在运行时产生的重复来源描述/导出清单，不是当前 203–209 的直接输入或本次所核传递输入。210 尚处于已形成的 208 来源视图计划；所核计划保持原输入，不将此结论扩张为未写出的未来入口。

本建议不删除整个 actual63 目录，不删除较小的 condensed-array-manifest.json，也不声称旧科学数组可从两个 SHA 恢复。普通删除保留历史提交；若将来需要两份确切旧字节，可从已存在的发布头 cfd63e66a3d6090f86fa906b46dec8db808b04a6 的对应路径取回，另核大小/SHA。科学重做须用原输入和明确新运行，不能把重新运行当成必然逐字复制旧耗时、路径或浮点输出。

## 两个实际删除路径

共同前缀：
`topics/visible-flex-larger-amplitude/notes/public-actions-43646179305-1-condensedqp/eighteen-condensed-warm/`

| 后缀 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| domain-operator/manifest.json | 493850 | ff034c85815a98bba2cc1745e3e7a1416c309e656c69b572e15f5f0bb3fcb23f | f99e636ec715a7aa315662dcdec4c08869954a82 |
| optimization-intent.json | 948087 | 688c586b83ad9d1c1cc16526b885c594e471ec3d6e2afeb29ea27f0c1c860f94 | 9e85b2729322e51de9ff697367cbd8cfe7a1851f |

大小与完整 SHA256 由 root CLI 对实际 Git blob 仅作字节身份复核提供；本调查没有通过 connector 搬运两份大正文。Git tree 也核了两项 blob/size。当前附近目录仅保留 JSON 索引，原 domain/condensed NPZ 已不在该当前树中，不能把这个 manifest 当成仍持有全部数组的证明。

基于 root 官方 topic tree **6110ed1e148be26d517c5cb99b42ebe90f3a3dab** 的 198,551,390 B 快照，仅去这两件会成为 **197,109,453 B**，在 200,000,000 B 下余 **2,890,547 B**。这是该树的纯字节差，不包含之后的新提交。

本次操作前另核官方 tree `83ee7c1ce8ed4cb3630d0c058943a5f4841479f9`（R473提交 `f7b46ef6f8bd81385e71f193377e16c5f8c4e755`）：9235 blobs、198614173字节、9609 entries，未截断。删除两项释放1441937字节；本记录和索引文本也有增减，因此推送后的实际目录大小另据官方树记入 HANDOFF，不把上述早期快照差额冒作现值。

## 真实产生来源与可重做合同

- 原 request **63**；source **db6d728f30ee2d0c9ea62c96c622d8d85d2354b2**。
- Actions run **43646179305**；prefix compute **132604404966**；原工作流 `.github/workflows/visible-larger-public-condensed-qp.yml`。
- 原 request SHA256 **9b38956b965ae98fc238eb4e688b4b39383f47f1a42e2023210b507e697b6608**。当前保留的 `notes/public-actions-43646179305-1-condensedqp/followup-request-identity.json` 保存完整 request/逐源身份，不能删除它。
- 主 producer `geometry_20261114_eighteen_query_condensed_warm.py`，39705 B / **b9f7d9150c57cff485f5f891881870095fc91f7a58fd40f63544e6bb9c3ef335**。
- 域 producer `geometry_20261114_eighteen_query_domain_operator.py`，29265 B / **ec43c049542f523e1c4f2b1956c07a9216497eb066a8f6f22ceddd8f11e2c051**。
- 原观察入口 `geometry_20261114_eighteen_query_collocation_observer_warm.py`，16720 B / **6ad75ce4b350aee4ae52afe2c6045f50d657931419ef7c4b46d0758db3acd1ca**。
- 原 engine `geometry_20261114_full_angle_projection_warm.py`，36439 B / **7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152**。

亲读上述 engine 的构造/写入控制流：它由当前 prepared/accepted/zero-anchor/config、传入 resume 的 producer、源表及坐标图构成 identity，执行 `write(args.out / "optimization-intent.json", identity)`；十八查询包装器只给该输出加入当次查询/支撑/父来源说明。后续恢复读取的是显式 resume warm 与 parent-status，核它们内部的 identity/源表，不把历史 optimization-intent 文件再次作为独立科学输入。

亲读十八查询域类 `export(directory, row_chunk=256)`：它从本次实际对象生成数组文件，取 `self.description()`，加入本次 files 与 artifact_scope，最后写新目录 `manifest.json`。这份 493850 B 文件是生成输出索引，不能替代被索引的 NPZ，更不是原优化目标的独立定义。

原 source/request 的完整重做条件仍保留：actual62 run **43642866864**、source **cc813fa7521098fdeba86b8bf8c0fe7d8c96bba0**，warm **4792420 B / dffaa532026e07357d5115089d968c1be4472c44d9a5f5da25ebcb3e2291ac73**，decoded status **1466059 B / 4f8239522cef511aca6721ddc9c4541cc9d4e65db3e7260d277b090ad226c054**；原 accepted/prepared/anchor/config 四件与原公开源码恢复。一次完整十八查询模型：699 节点、112 模态、B=5749、原 C=4059、18×2048=36864 角行；lambda270、LSMR200、projection200、17 原试探、overall1200 s、candidate600 s、trial reserve90 s、recovery reserve30 s、working512、dual200。没有为整理运行这些算法。

因此“可再生”指原完整 source/request/实际父输入明确指定了生成程序；不承诺未来环境浮点或资源走向与旧 run 逐词相同，也不借旧清单制造任何新实际结果。

## 已有紧凑结论必须保留

1. `notes/2026-11-14-actual-request63-nearest-midpoint480.md`：真实 alpha1/128 原 warm，1/64 首邻拒绝的 midpoint480，完整原试探/域失败范围与未付责任。
2. `notes/2026-11-14-actual63-complete-original-byte-readback.md`：原单次完整字节读回 run43647823666 / job132609418459、全部数组核对范围及未读巨大 QR 因子的责任边界。
3. `notes/2026-11-14-actual63-primary-identity-readback.json`：1773 B / **265e8c76b7e7c6269bc60b9cc152fc4d6d7243e9ca1ba87c59bc5a97066ff953**。
4. 原 `followup-request-identity.json`、T112-config.json、parent62/restore-identity.json、较小 condensed-array-manifest.json，以及所有被当前入口实际需要的科学父数据/源码。

这些结论已将 actual63 的有限 warm 与真正已接受 BVP/闭面分开：merit 43.794243580548255→43.79041968996707、FD 当次通过，均不表示非零 native、完整 BVP 或课题成功。本调查不改写这些事实。

原详细 completed-prefix-readback 46059 B / **b138fdaaae3c9c4174043326cc2d2fb0cc740d903725cc82dea809ddacdf1a5d** 曾加入 **ffa3daf2e2bfd8783e64ba25f0626f2f9054a097**，之后已按根15从当前树删除。本调查只读取了该历史小回执，不把它伪装成当前保留文件；现有两篇紧凑说明与 primary identity 仍是当前记录。

## 当前 203–210 的实际输入与传递路径

| 入口 | 本次亲读的实际恢复/消费路径 | 对两候选当前路径的关系 |
|---|---|---|
| 203 | 原 request.inputs 与 construction_inputs 恰五件：两 ready、2161 B 原 config、2614352 B 原 accepted、4220043 B complete453 seed；workflow 逐件从 8bd267107cc8710d371f3b62c02986655ac965b0 取明确路径。actual180 重建另由原165三个明确 JSON 与实际180小摘要/选定配方构成；十族 pipeline 只读同 job restored-selection、fresh C/cut/core。 | 不读取两旧清单；同 job 所写 result/manifest 不是历史 actual63 路径。 |
| 204 | 原完整 actual91 archive：run43672150224、artifact14145200674、10267458 B / 78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6；workflow 明确调用 root_20261115_fetch_native_word_parent91.py，完整包临时保留并传 --original91-directory；另恢复两 ready 与公开源码。 | 即使原 archive 内存在历史 lineage，也不是对当前两文件的路径读取。本建议不改 archive、原91读取或两 ready。 |
| 205 | 保203五原件/原165与180结构配方恢复；另显式 actual202-accurate-ten-candidate-input.json 2165 B / c980e9d4c6e15455459dc91a890b4fd9d8b02bced26eecd5d632ff9d250dbd4d。新 pipeline 的 construct 从此显式十词与旧结构配方生成本 job 目标，不接受旧180域结论代替。 | 无两候选输入；同 job native/accepted450/几何仍全新。 |
| 206 | tabular producer 调用 restore_inputs：四原件从 918fdb11dbb7a424b6149b405e2c7fab3cc0c737 的明确路径取。restore_parent 核完整 actual98 archive/run43677587785/artifact14147700690，却只解压 warm4927052 B/b59f40c0... 与 status3379453 B/b7ad389f... 两个明确成员，随后删临时 archive；不读其它旧清单。 | 已亲读恢复函数和 thirty-nine _run_engine → 原 bind_parent：嵌入的历史 producer 是对象身份比较与逐源码校验，不触发实际63清单路径打开。 |
| 207 | 明确引用完整205 contract，再以当 job 实际 accepted450/checkpoint/far/config 作 R456→M128 的父；新级结果均来自该 job。 | 不从任一历史 actual63 输出取值或补数组。 |
| 208 | 四原件 accepted/prepared/anchor/config，固定8bd267历史；两 frozen ready；actual119 batch3 六词配方、fresh-circle-low-three-linear；公开源码恢复。 | 亲读 request.inputs，exact 对入口原 source 的独立已读确认同此范围；不消费实际63两清单。 |
| 209 | 原完整205合同 + R456 真加密父 + R462/463/464 真 union；prepare先绑定已刊源码，再生成15新源码视图，之后绑定输出；原112 far是本 job 实际205 sampling，非旧63。 | 新 sampler/config/CP/各级几何来源都同 job 明确传递，不是静态历史 domain/optimization 文件。 |
| 210 当前计划 | 直接以208已刊 request40395 B/435e90b6... 与 source9b05bfc5... 为基线的11份源码视图；生成器只读明确 public computational sources/request/plan/recipe，保原208科学输入。当前不对尚未冻结的新最终 request 作断言。 | 所核计划无候选路径；若将来修改输入，应按新实际合同另核，不据本表预先授权删除其它文件。 |

203/205 的原165恢复器 `root_20261115_restore_actual165_coast_inputs.py` 也已实际核读：仅官方 run43736208020/job132879253906/source1f2ec637... 的三个指定语义成员 original-input-binding.json、original-target-result.json、original-construction-summary.json。它不沿嵌入来源递归恢复 actual63 旧目录。

共同 `computations/source-dependencies.json` 现有91个明确 source/reference条目（869436630c99aa5a68afb55bd8877c826034d117来源，866846 B），两候选均不在其中；实际准备程序选取的78公开源子集因而也没有两候选。这里检查的是源清单成员，不是用全文无命中代替上述运行控制流核对。

## 本次删除边界

本次仅删除这两条当前树文件。仍不删除 actual98 warm/status、原91 archive、四原件/两 ready、当前已冻结配方/源码/必要证明，以及无法确认现用的其它大文件。没有把“未在 source text 出现 run63”当作唯一证据，没有把删除历史目录整体视为安全，也没有新增科学门或科学运行。

