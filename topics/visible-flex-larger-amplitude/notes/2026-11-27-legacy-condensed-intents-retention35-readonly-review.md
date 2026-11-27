# 第 35 批旧凝聚暖场 intent：完整来源与原字节恢复审核

**分类：只读源码与文件保全审核，不是新的数值结果或数学完成证明。**  
**作者：ChatGPT，/root/solver，GPT-6 Astra Pro，AI-assisted。**  
**日期：2026-11-27。**

## 1. 本次结论与实际边界

本次已完成三个旧生成 `optimization-intent.json` 的保全审核。它们分别属于原 request49、51、53，合计 **1,421,301 B**。当前 main 的树元数据与固定恢复提交中的 Git blob、大小逐项相同。审核没有读取这三个大文件本体，没有读取其大 warm/status/FD 本体，没有删除文件、改 ref 或执行科学计算。

完整机器可读台账是 [legacy-condensed-intents-retention-35-provenance.json](../computations/legacy-condensed-intents-retention-35-provenance.json)，**91680 B**，SHA256：

`433e73a3064d11958cb73e707e33c6255075b19551709fb7ee54c1d642fc487a`。

台账逐次保留完整原 request、完整非数组 manifest 参数、原 workflow 的全部科学命令和 FD 命令、源 SHA、直接及隐含输入来源、实际父 warm/status 恢复记录、新 warm/status 身份和真实短结论。原 workflow 其余设置、输入恢复和发布命令均由不可变的整文件 Git blob 保留。这里没有用缩短参数或重新包装的大 raw 替代原对象。

原 intent 的 SHA256 尚未从原字节读得，台账明确写 `null`；没有把某个摘要或重新序列化的 JSON 的 SHA 当成原件身份。恢复时可由原 Git blob 和字节数严格验证，实际需要 SHA256 时再对真正恢复的原字节计算。

本结论只把下列三个路径交给 root 作普通当前树移出；所有源码、配置、请求、真实结论和保全台账继续保留。审核者没有执行移出。

## 2. 三个候选的精确身份

三个路径的共同前缀是：

`topics/visible-flex-larger-amplitude/notes/`。

| 原运行 / request | 前缀后的完整路径 | 原字节数 | 原 Git blob |
|---|---|---:|---|
| 43631235905/1 / 49 | `public-actions-43631235905-1-condensedqp/fourteen-condensed-warm/optimization-intent.json` | 409075 | `630fe7167bae469847b3817dd2f76e61a8563102` |
| 43632815810/1 / 51 | `public-actions-43632815810-1-condensedqp/fifteen-condensed-warm/optimization-intent.json` | 472598 | `57e6d0639362168bca6a60994ffa681447eecc53` |
| 43634517255/1 / 53 | `public-actions-43634517255-1-condensedqp/fifteen-condensed-warm/optimization-intent.json` | 539628 | `3fe1e7b2a782f80175d8f31267dd1aa6ccaefb48` |

三份 intent 的固定恢复提交为：

`cf41802e7a538f1b3595397681d3371aebf4018d`。

本次读取的 main notes 树为 `f4f031a8ef23427e1b217622c3c4645ab9947614`；固定恢复 notes 树为 `14f340ea7cfe05b2efe244bcc08fb105c296cab5`。三原运行目录的当前树与已刊第 34 批快照仍相同；实际逐路径核验记录在台账中。发表前 root 仍应核当前三个精确路径是否保持这些 blob，不根据文件名删除其他文件。

## 3. 为什么它们是生成输出

实际原引擎是：

`computations/geometry_20261114_full_angle_projection_warm.py`，36439 B，SHA256  
`7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152`。

其 `main` 先校原 accepted、prepared、tail anchor、tail config、resume 和冻结源码，读取实际父 `optimization_warm`，再构造当前 identity。明确写点是：

```python
write(args.out/"optimization-intent.json", identity)
```

identity 含真正的 `resume_sha256` 和完整 `resume_producer=current["optimization_warm"]`；同一 live identity 进入 `driver-status.identity`，接受暖场时再进入 `warm.optimization_warm`。输出目录要求为空。十四、十五查询的独立入口在写钩子中加入本次查询、完整源和预算归属，保持原父 producer，不把原父子树重标为新结果。

本次定点读了这两入口的主绑定、写入和实际父校验代码：

| 完整源 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_fourteen_query_condensed_warm.py` | 38790 | `331b59edadfa1fb7d5f8c64e6f0119c63a62f5e2a3df999549ef7effd932aac8` |
| `geometry_20261114_fifteen_query_condensed_warm.py` | 39048 | `f1310edc94fb3a9c9f95b5dad98e7073c1879997b9a9bdf06c5028e91f83351e` |

两完整 response 小源和原 `geometry_20261114_constrained_trust_response.py` 也已读。实际暖场续接和 FD 读取的是完整 warm、原 status、accepted/prepared/anchor/config 与源码；未打开独立 intent 文件。原 response 的 `--prepared` 指向实际新 warm，仍校完整优化来源，原真零 H Jacobian 保持明确 affine。

因此生成输出的分类来自真实写入与消费位置。它不表示每个历史程序都不会读 intent，也不表示当前保留的摘要可以替代原 intent。未来确有消费者需要该文件时，应先按第 7 节恢复真正原字节。

## 4. 完整来源与参数保持

### 4.1 三个原 workflow

三次原运行都使用完整 `.github/workflows/visible-larger-public-condensed-qp.yml`。本次先取树元数据，再读取小于 100000 B 的整 workflow：

| Request | 原 source commit | workflow 字节数 / SHA256 |
|---|---|---|
| 49 | `d5c99bef58700db0da1a3de2faba3e94d60b1dc1` | 17878 / `fa930e7837d89665b92a707285828aefc68a18cfebab02688ed8f548bc3285dc` |
| 51 | `bd3fc94a6092313313daf607328a9695e80c17f4` | 18330 / `9371bdda71991dde9e4c45c6c0d69ce3f647c57af6f02d6e608e7e3c91666075` |
| 53 | `dd3156cfe7e5197029ce45fff5beb53115de3680` | 18300 / `8dccc50d58d6614870d436ef9372aa08324b8f966258b72d1150910213ac1e12` |

对应 Git blobs 分别为 `6aa2522d199dfaa48c1b9920accbf2b2ca53ed0b`、`656d07d3f71fd84d71e2e661ab04de637567b50b`、`5c28692907b759ba76f29ab10547a41a372ff148`。完整原命令已逐字放入台账，包含所有路径、父 SHA、数值开关和预算。

原环境为公开 Actions、Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0，OPENBLAS/OMP/MKL/NUMEXPR 均单线程。job 上限 80 分钟，科学 step 35 分钟、FD step 25 分钟。原 checkout/setup-python 版本与全部恢复程序保留在整 workflow 中，不以当前环境代替。

三次均保全 236036 个原坐标、原699节点、2048物理角、4096角 rho 守卫、原 C 比较、完整 R270 外部条件响应、17 次真实回溯上限、原域与 FD 阈值。原主要预算为 damping270、LSMR200、projection200、dual200、总1200秒、候选600秒、trial reserve90秒、recovery reserve30秒、jac-workers2。工作行49/51为256，53为512。49有14个完整查询/28672行、完整局部4735维；51/53有15查询/30720行、局部5073维。

这些是原完整实验参数，不是新的精简复现提案。各轮实际父和固定权重随续接改变，不能把跨轮 merit 差当成同一模型的预算对照。

### 4.2 已刊完整参数与源码台账

以下记录全部保留：

- [retention30 完整来源](../computations/legacy-condensed-manifests-retention-30-provenance.json)，49041 B，SHA `17a1d795952ce8eeda11660f043132bbf5e1cc3b098f5c0f79f4716926eb47fe`。
- [retention30 全部 77 个源码角色](../computations/legacy-condensed-manifests-retention-30-sources.json)，30464 B，SHA `b853135bb64ca987e701a0da3436e8d602459bfbc55f9da97b3be916bbcd4472`。
- [retention34 完整来源与当前 recipe 依赖审查](../computations/legacy-condensed-intents-retention-34-provenance.json)，93023 B，SHA `f19e26a0cfde7ca23c8a63962c6ac0fac4e286ea84a78019baa7079d106012b2`，实际已刊提交 `68d75a1ff1ad9d56c3cb145e6cdb341bc0340562`。
- 原三参数文件 `legacy-condensed-source-parameters-run43631235905-retention30.json`、`legacy-condensed-source-parameters-run43632815810-retention30.json`、`legacy-condensed-source-parameters-run43634517255-retention30.json`。各完整非数组参数也逐对象保存在新台账内，未删 query、原支持、全变量、源、预算或验收责任。

第 30 批已经保全生成数组目录之外的原 manifest 值与整个来源；本次不再把可重算数组身份长列表抄回新参数文件。原 91 项 source-dependencies 与 workflow 实际调用的 `prepare_public_source` 所恢复78项公开数值源同样有完整文件和 immutable 引用。其单独 main 的其他功能不能冒作本 workflow 实际调用。

原 request identity 文件的 `request_sha256` 在 workflow 中来自原 request 文件的原始字节。新台账明确采用这一原语义，不从本次重新序列化的 request 对象生成替代原 SHA。三个 whole identity 文件及完整 source pins 都继续保留。

### 4.3 共同输入和当前 warm recipe

共同原输入包括 accepted099、prepared112、其既有完整 boundary response、true zero-H T112 anchor 和完整 T112 配置。第 34 批已保留它们的精确路径、原 SHA、大小、Git blob 及公开恢复提交；本台账逐项保留这些记录。T112 配置本次整读2161 B，三原目录为同一 blob，SHA：

`01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。

其全部控制输入保存在新台账，未省略长配置后半段。

当前 SO3 warm recipe 的依赖结论明确复用第 34 批完整审查：实际 `rebuild_axisymmetric_so3_warm → reproduce_and_solve → rebuild_fullclosed / rebuild_closed_warm → pulse/assembly/Hold/mode` 入口链所需的唯一旧 raw 种子为公开 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 的 accepted099。该指定入口链不读取这三份 intent。原21项全源 pins 和五入口文件审查范围均保留在第34批记录中；本次没有重复跑 recipe，也没有宣称全仓库所有旧诊断或未来程序都不会读 intent。

## 5. 真父与新输出的恢复边界

**`cf418…` 只保证这三份 intent 原件；已被旧保全操作移走的 warm/status 不因此重新存在于该提交。** 它们必须按各原 source commit 恢复。

| 所需原 pair | 可恢复的公开提交 | warm SHA256 | 原未压缩 status SHA256 |
|---|---|---|---|
| actual48，供49使用 | `d5c99bef58700db0da1a3de2faba3e94d60b1dc1` | `df6543c9b88c21bd9ea3c046f05a7c292b7d977d09c6ef431e6771560fe14689` | `00c9e73f260d0fa239a17c3973bcbd113d813c079c04451335244e923e85be9e` |
| actual49，供51使用 | `bd3fc94a6092313313daf607328a9695e80c17f4` | `c0d9c6d59e16ef1482f8ee60f9681d8db089b21d68e249adf1830df03be6612b` | `e22fd03b8c24adbd0eeeaf0b084d18944d17e4cd1f4115075cb63d9e9a41aad7` |
| actual51，供53使用 | `dd3156cfe7e5197029ce45fff5beb53115de3680` | `b6620a0ce55be257fc58c29e88187cc602ad08b46c4424903ffddc003b5b1595` | `267451f8eb91ca568ff187bfb39dbd32b22ca844788e1e88165910190ad6f685` |
| actual53，后来供56使用 | `b8a19c16fc1363ffa1a66f39b9403e0dfa93e169` | `e71a5fec344326df3b6c69ec6d298f5079034fb86eb2fa505008c35682010d32` | `6170aba505c2eeb5db9411f13ad502363fe1593a7d4d63faa5f0d0a37fb34938` |

前三 pair 的原目录树元数据本次独立核到；actual53 pair 明确复用第34批已刊的精确恢复表及原 next-run receipt。全部原 `restore-identity.json` 记录完整保留。没有读取这些大 payload 来制造新的“已复现”结论。

actual48 status 为117946 B gzip，解压原1067190 B；actual49原 status 991791 B直接保存；actual51为129683 B gzip，解压1051960 B；actual53为157158 B gzip，解压1251975 B。压缩及未压缩 SHA、全部 Git blob 和 warm 字节数均在台账。恢复时先验传输件，再透明解压，保原字节；不得解析后重新格式化来满足原 status guard。

物理 FD 的原 SHA 与真实结论另保。49/51的 FD 原目录树也已核；53 FD 的大本体未读，其原结论给出的身份保留，但本次没有独立验证其候选历史提交是否仍含该另项输出，因此台账不假写已确认恢复。该 FD 输出不是生成 intent 或续接 warm 所需的输入；其完整原生产程序和参数仍在原 workflow。

## 6. 三次实际结论保持原范围

| 原请求 | 真接受 alpha | 本轮固定权重 merit 起点 → 终点 | 原未完成的最近限制 |
|---|---:|---|---|
| 49 | 1/16 | 44.250102036498696 → 44.20038969249102 | 1/8仍在原 left-RMS469 失败，14个已建模网格全正 |
| 51 | 1/8 | 44.20135024608698 → 44.115161170653145 | 1/4在原中点481、482失败；482已建模，线性正性未保证真实域正性 |
| 53 | 1/64 | 44.11665947585927 → 44.105521474605546 | 1/32仅原未建模中点481失败，15个真实已建模角网格全正 |

科学 job 分别为132558124307、132563011884、132568287151；原暖场耗时365.482310735、349.84839812、562.204670453秒。三次都保存1个接受暖场、`optimization_progress=true`，但始终 `success=false`、`new_coupled_finite_acceptance=false`。

各次真实新 warm 的原完整 affine FD 都在原5e-5门内通过，四阶误差分别为7.070190461766486e-10、7.186294196742241e-10、7.165083799852089e-10。它们没有给当前非零 H 的新 native tail、完整 BVP、连续几何或闭曲面族验收。

保留的完整原说明：

- [actual49](2026-11-14-actual-request49-fourteen-query-and-left-RMS469-limit.md)，18930 B，SHA `eae2a7cc2a41c0feb461d8c225d538311ac01d31af43ee3a75fa923a1411474b`。
- [actual51](2026-11-14-actual-request51-fifteen-query-and-working-row-budget.md)，19122 B，SHA `5e493e5e53c012abedbd3d7565e7d0fdfc0a6cb0857484d2b0db959486d939a6`。
- [actual53](2026-11-14-actual-request53-working512-and-midpoint481-limit.md)，16395 B，SHA `95003ce99275a2d0a1b7eedacb9b0b76141e80d004ce0dbbf71f2be6c83dc062`。

本次只读取这些已经公开的实际结论，不重新计算 merit、矩阵作用、norm、方向、FD或科学数组；也不把49/51/53之间的新权重误当作同一固定目标的直接差值。

## 7. 文件恢复与实施责任

需要原 intent 时，在隔离目录中用原完整路径从 `cf41802e7a538f1b3595397681d3371aebf4018d` 恢复真正 Git blob，核字节数和 `git hash-object` 等于第2节记录。不要通过集成全文工具读取这些超过100KB的本体，也不要把恢复的大 raw 再换个名字放回新参数台账。

若未来需要科学重算，应在公开 Actions 中恢复全部实际源、上述原参数、accepted/prepared/anchor/config 和正确父 pair，保所有变量、查询、原非线性筛与预算。这和恢复原审计字节是两件事：恢复原字节不需要重新执行科学；一次新的数值运行也不保证产生相同历史输出字节。

root 的实际普通移出应只包含第2节三个精确路径；不得改写历史、删源码、删配置或现运行未知结果。新增台账和本说明产生的开销应从1,421,301 B毛节省中扣除，再按真实树重新统计。这里没有实施删除或预报最终仓库大小。

## 8. root 实施记录

2026-11-27 10:27 UTC，Astra-larger-e4e2a2bf-20261126 在普通后继提交中仅移出第2节三个精确旧生成路径；不改写历史，不移出任何原源、参数、请求或实际结论。root 在固定恢复提交 `cf41802e7a538f1b3595397681d3371aebf4018d` 和当前 `b37c509a34b631ef8686dfecb1861ee75106ac1e` 各查三目录，并在发表基点 `27ad8ab24c3a394b836ef6834481597b13b8c884` 再查三目录，均逐字节数/原Git blob同表。三个大 intent 本体未读取。

root 核全部六个小源的完整字节数、SHA256与Git blob；在全文上读十四/十五查询主入口的真实父 warm/status guards、live identity 的 intent/status/warm 写钩子，整读两FD response小源；原完整引擎与共同response复用第34批已读的同字节源码。该范围证明这些特定入口的生成/消费关系，不扩成所有历史/未来程序的无依赖保证。91680 B 完整 provenance 原字节不改；第1–7节保留审核时的只读事实，本节记录 root 的后继实施。

新增台账与本说明计入真实树；毛移出1,421,301 B，原来源与恢复承诺均按第4–7节保留。无科学求值、重新生成历史输出或新数学完成结论。压缩前完整交接另固定在 `5cd30d41213993d3d9278d29ce93e855ffcd756f` 的 `HANDOFF.md`，实际09/10运行块逐字保持。
