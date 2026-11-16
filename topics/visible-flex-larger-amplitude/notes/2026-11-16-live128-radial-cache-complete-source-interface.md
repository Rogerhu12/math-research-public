# R518：原 full112/live128 完整链的局部径向缓存接线接口

作者：ChatGPT（AI），2026-11-16 UTC。

本页配套 [R518条件结论](../results/R518-live128-radial-cache-complete-source-composition.md)。**已完成源码/来源组合；没有运行新科学、没有指定新公开request/actual结果，也没有更改现有221。** 原R515局部数值实现已发表；本页给未来公开Actions可直接使用的实际caller、source view与必要读回合同。无需独立fixture、benchmark或新增科学门。

## 1. 本条四份公开文件

| 路径（topic内） | B | 完整SHA256 |
|---|---:|---|
| computations/root_20261116_live128_cached_radial_source_views.py | 17055 | c694b2b937d8953169fb62c869e4ebe7acdf421eae12ea1393b7faee9e4d9f69 |
| notes/r518-live128-cached-radial-complete-source-plan.json | 48391 | 4f2097053bddff0bf07a18f09ffa846bd64eb2fa6dd3d9707ab7f24f3ef62f6b |
| results/R518-live128-radial-cache-complete-source-composition.md | 15739 | 8f8819d69cef31d113c87b4f7a53bcd4ce9a0e6fb557d7ac1516e6dd312ac7f6 |
| 本接口 | 由最终交接manifest记录 | 不将自己的SHA嵌入自己 |

交接manifest仅供发布者取文件，不是新增数学输入，不进Git。12份展开source、engineering view、compiler生成CPP和任何实际科学raw均不在本条Git清单中。

原基线提交 `8b352f90b97f7c340a2fbebbb11c19080d9a5e08`；原请求实际路径：

`topics/visible-flex-larger-amplitude/computations/public-live128-scoped-original-full112-FD-fullDN-request.json`，

54884 B/`0fa9fe29153913252fd569cb2b99711c85b0afe72d8bc576adf629bd3e3f789e`。

R515已发表提交 `02320c3a035d03c31c4e1fada1d19d9661bf7179`。本条不复制它的两个公开代码：

| R515已有文件 | B / SHA256 |
|---|---|
| geometry_20261116_native_physical_radial_mode_cache128.hpp | 5253 / 959d43bffc27665f30dffe4e98bb00fc007ee10fc3f3e519589c0c3d854fcd51 |
| geometry_20261116_native128_physical_radial_cache_source.py | 13235 / 22e64c73005918527815269930f94ad4413bbc129120cb9dd5686a78a58873c6 |

另完整绑定R515来源JSON：8662 B/`5950052fac0d9c23e96f29421c03df79f4748828b2d7a6e9a4ed7f40bd090666`。其完整kernel/component literal合同保留，本条component输出仍0a7f原字。

## 2. 明确集合和真实HERE

- 原请求的336个文件pin逐项保留，含真实metadata `source-dependencies.json`。
- 新增到该集合的公开代码是上列R515两件和本条generator，共3项。因此339个public文件。
- 12个独立source view均从已发表baseline生成，加入当前集合成为351项。
- 已发表R515 JSON plan另按repository相对路径在 `published_metadata_dependencies` 绑定，不假作source-only代码。
- 351是实际绑定集合，不说成自动扫描得到的全库递归import证明。原未改的数学模块/动态import与原78 public_resume来源仍按原caller实读。

生成器本身必须就在实际 `GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations`。新view直接在这个真实目录使用新名；不另造一个让 `HERE.parents[2]` 指向错误仓库的private源根，也不改GITHUB_WORKSPACE或sys.path。Git HEAD必须是本次GITHUB_SHA。原文件不覆盖，已有任何目标新名都会明确停止，不静默复用旧job文件。

在进入原科学前，未来入口须先恢复/checkout全部339公开文件的真实字节，以及原请求和两个plan。未生成的12项不能当作公共Git文件去下载或提前读取；执行顺序是**绑定generator/公开祖先→生成完整新source→取得实际派生请求→原prepare/run**。本条不提供自动Git push、ref变更或dispatch命令。

## 3. source prepare完整CLI与返回

以下只描述未来Actions调用，没有在本地执行：

~~~bash
COMP="$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations"
TOPIC="$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude"
python -u "$COMP/root_20261116_live128_cached_radial_source_views.py" \
  --plan "$TOPIC/notes/r518-live128-cached-radial-complete-source-plan.json" \
  --plan-sha256 4f2097053bddff0bf07a18f09ffa846bd64eb2fa6dd3d9707ab7f24f3ef62f6b \
  --upstream-request "$COMP/public-live128-scoped-original-full112-FD-fullDN-request.json" \
  --out "$RUNNER_TEMP/R518-live128-source-view-metadata"
~~~

generator schema：`R518-live128-radial-cache-source-view-preparation-v1`。

plan schema：`R518-live128-radial-cache-complete-source-plan-v1`。

固定输出：

| 实际路径 | 内容与责任 |
|---|---|
| RUNNER_TEMP/R518-live128-source-view-metadata/source-views.json | 全部public读核、12view实际文件/完整SHA/替换receipt、真正未生成role、实际错误；是完整source metadata |
| 同目录derived-component-contract.json | 从原221请求形成的新完整内部组件合同，写成后真实计算SHA |
| 实际computations下12个新文件 | 对应下表的完整输出，没有旧文件被换字 |

成功时写GITHUB_ENV：

~~~text
R518_COMPONENT_REQUEST=<真实 derived-component-contract.json 绝对路径>
R518_COMPONENT_REQUEST_SHA256=<实际写出全文的 SHA256>
R518_COMPONENT_RUNTIME=<实际新 owned_run.py 绝对路径>
R518_COMPONENT_READER=<实际新 necessary.py 绝对路径>
R518_COMPONENT_NAMESPACE=<RUNNER_TEMP/visible-live128-cached-radial-R518>
R518_SOURCE_VIEW_RECEIPT=<真实 source-views.json 绝对路径>
~~~

这些环境变量只供后续步骤；不假称当前进程已自动source了新环境。完整request SHA依实际plan路径、本次Git source和实际receipt而形成，不能在本文预填、不能复用旧0fa9作新SHA。

生成器只做文本/JSON/完整identity：不import科学模块、不AST、不compile、不启动owner、不创建科学钟。它在写第一个新source前已在内存完成所有输出及完整SHA核；写失败时完整source receipt仍逐实际记录已写/未写范围，不用成功声明覆盖异常。失败退出2；source-return所选metadata若超90K则70，只有真实本地完整receipt身份，未返回正文不作成功截断或拆包。

source-return帧为：

~~~text
BEGIN_R518_SOURCE_VIEW_PREPARATION
<一份完整必要source metadata>
END_R518_SOURCE_VIEW_PREPARATION
~~~

所选source-return含全部新output与literal替换receipt、原request/plan/generator身份、实际derived请求、错误/未生成role；原339个逐文件receipt在完整本地source-views.json中，公开返回其完整文件身份和实际读核计数。这个范围不声称root逐项读过所有public源字节，更不声称任何科学已经运行。

## 4. 真派生合同；221仅内部祖先号

新schema：

`R518-live128-cached-radial-original-full112-component-contract-v1`。

该对象保 `request_number=221`，**仅为冻结原组件合同的内部编号**。它不是新actual221，不代未来外层request号。外层如果以后决定执行，应另记录真正request/run/attempt/head；本条没有占号或触发任何run。

变更的metadata键只有：

~~~text
schema, operation, namespace,
execution_entry, scientific_entry, necessary_reader,
source_sha256, source_contract, R518_source_composition,
results, publication
~~~

原repository/request_number/lanes/reviewed_README_blobs、original_inputs/actual63/actual91_artifact、runtime/live_call_resources/resources、original_scientific_contract/arithmetic/retention逐对象不变。source_contract完整保旧声明作为 `inherited_frozen221_source_contract`，新count及当前view责任另列，不把旧“14source未改”解释为当前12view都仍是旧字节。

`R518_source_composition` 含原请求完整identity、新plan/generator actualreceipt、生成receipt真实路径、本次actualcheckout source、内部编号边界。新derived请求自己的SHA不是字段自指；写成后由收据和CLI参数绑定。完整source receipt最后记录derived identity，而请求只写该receipt路径，因而没有互相嵌入SHA的循环。

## 5. 12个实际source view

文件名均在plan的 `views[].output.file` 与 `roles` 中完整给出。下列全部输出身份均由纯字面操作形成；尚无运行结果。

| role | 原完整SHA | 新B / 完整SHA |
|---|---|---|
| components | 2369787d7454c4f3d0e9f91cbf4f82327f73046bc637c6180361bff877d0b866 | 32429 / 0a7f47213789bc4779a6241b121f636d2356302b9f258fdf7a94b3dec4b02f8b |
| owner | 5c1d4908fe6cca3917ef8ad6ed6269251e29b99efbb81e54b91b4f43391fc3b5 | 18902 / 561c1db5122086abab05aa968db4597b46fad77ab887bd7c5faac985a6bdd3ae |
| assembly | 08d48b55934e5306258d70a26aa8f8f57c89f71b45f6175b777ab46405cd43eb | 28615 / 2807377e96e127af2aee6ca3257bafbd8f6b884a5c80e0959d985e8b4d35bffc |
| system | e37b13457b9dd9cbd0e918a2bf98988b5027b49fad5c54ffd824016dd2efa7c2 | 29003 / 1cf6338e47541cb3af65d507de462dd6143f35aea7661575e8bc45c07fb5c86b |
| qr | faac8b013b9151ba92760962d4303c847301a9057834e7230ab37ea6d0c04b49 | 21844 / 9c2cf83ec714f1e225071228320c169416a6ff86eddce0c717163a323a3a83dd |
| pipeline | 137cc95996dca1d876640fb81e4fd3290d41e32e9b23027cb29d103b5cb0eda8 | 19348 / 436db54132702cf448169e93a1d6d6d1327a63d5fbce1de1c4dd30ec87912fcd |
| call | c20af799243d35a045c9c5be7900fbd19bb8b391acb9efb26fe9c5265566cd21 | 34383 / e9978c3a4692cee5ab7c27339272a45c18ffe5108fd32e8e3531cc4044b29296 |
| worker | 8cc51b3e1a1c232c8b5769ef1cfc39261deb7aba84d0b8365b62cbf88c270b72 | 8181 / 16dd7cb9f1ee91c43d06620aebc3cdf2e67fe75d416caf3c1d118aff9f3e39ae |
| client | 9f32e5ddd376016e51f678d9f0328727e63d8aacb5c4583046dc705949cc1894 | 31726 / d4b9a1cae39c744e1b579faa4d3559a5fe2ad3e33a052324cb3099d3c26f56aa |
| fulldn | 63bbbefcfda8ae5761be314da743afc5291ad1a83749cf6d554003d429f5508e | 36808 / 9799a1b33ae52d1e5137ac51207bf48b01d41753732ec67225f738e17f764f91 |
| runner | 6f211144ec8411f60981d699841e18c75d7f3f8000ee8ba8fe5d500322ad8dde | 39021 / 86e416fb5d905bc85864931953d2fbc978f0585f117269b295c5bab3de0cefbe |
| reader | 687168ef5ec3414c79667deda4df40c233e60265c1b12605c40a891964f709a7 | 38722 / c186444eacb89add6e75ff6730851978ad8ba581f99dd447154fd5c258b15c2a |

全部12个展开源合计338982 B，仅未来Actions内部生成。计划不保存它们作为base64、压缩源码或分块数据；只保存完整明示literal差异，旧source全文pin和最终输出SHA。这里不是规避科学raw输出预算。

每个file单独的 `view.baseline` 给真实原名/bytes/SHA；`patches` 给id/before/after/count；`output` 给新名/bytes/SHA。12个role共71个明确literal替换项，不对运行输出作字符串编码。

尤其：

- owner完整embedded VIEW_PLAN仍以8855原wrapper为baseline；它的完整derived engineering文本为39154 B/`ce39e94d07b279bf136bd2af007e3f0f664015e37be3a8ea2197b7cd392696b7`。
- system的 `SNAPSHOT_LAUNCHER/SNAPSHOT_HOOK` 真指向新client/call；QR指向新system，pipeline/client对应实际pin。
- client旧18 pin原样保留，再加8下层view和2R515源码成为28；fullDN旧所有pin同样保，并加入新client和新下层。
- component仍R515原0a7f，stage/precision/RK/226双mean/所有224列没有新视图数学变更。
- response assembler仍实读同call全部实际component和末128、packet、原H身份，不能只拿sourceSHA造响应。

## 6. 原完整执行CLI与实际生命周期

取得上一节成功写出的环境值后，原外层各mode仍使用同一新真实derived请求：

~~~bash
python -u "$R518_COMPONENT_RUNTIME" prepare \
  --request "$R518_COMPONENT_REQUEST" \
  --request-sha256 "$R518_COMPONENT_REQUEST_SHA256" \
  --namespace "$R518_COMPONENT_NAMESPACE"

python -u "$R518_COMPONENT_RUNTIME" run \
  --request "$R518_COMPONENT_REQUEST" \
  --request-sha256 "$R518_COMPONENT_REQUEST_SHA256" \
  --namespace "$R518_COMPONENT_NAMESPACE"
~~~

未来workflow应保原always读回/quiet/清理分支；这里没有用上一mode是否数值成功替代必要范围。原runtime还保 `rules/science/quiet/cleanup` modes，不要求调用者手工另起科学子时钟。

runtime schema：`R518-live128-cached-radial-original-full112-owned-procedure-v1`。

它在真实source/input准备完成后，按原R508 `run` 一次形成 `R493-original-full112-live128-job-deadline-v1`，总19200秒；在rules与第一次factory之前开始。保旧输入恢复在该科学钟之前的既定范围，不把source准备声称为计入本不存在的更早科学钟。每H/call、owner、replay、component和组装均消费原绝对截止，不能reset。

| 原资源/范围 | 保留值或语义 |
|---|---|
| job/科学step | 350分钟 / 320分钟 |
| 总科学钟 / 末reserve | 19200 s / 120 s |
| 开始可用盘 / 退出保留 | 68719476736 B / 2147483648 B |
| owner / fresh replay | 上限6000 / 1200 s |
| stages / boundary / endpoint / audit | 上限8000 / 600 / 600 / 1800 s |
| native threads | 4 |
| Node heap / Jacobian workers | 6144 / 2 |
| exact workers / factor bytes | 2 / 2147483648 |
| uncached calls | 原外循环上界18 |
| 原初猜 | actual63真实prefix；actual91 failed73完整原artifact仅tail guess |

所有cap按当前剩余绝对钟clip，不许加和变新总预算或声称所有call能完成。64GiB启动门、原内存/磁盘要求不降低。每个worker属于原真实pid/start_ticks/uid/pgid/sid/namespace链；R508已修的限定归属算法、unknown保留、wait/reap、静止后读回/删除均整段原样。

新generatormetadata输出只为source，不是科学raw。旧runtime cleanup仅删除自己的原声明科学namespace；独立source metadata与工作树临时view随Actions现场生命周期结束，不能当作已刊科学数据。未来外层如额外删除source metadata，须保必要的真实source收据直到读回完成。

## 7. 原数学门完整保留

固定112、spacing2、576段/577节点、每节点224、局部226含双mean、全部224方向；输出顺序仍height112/mean1/slope112/mean1/second112，总338，混合338×112响应。

原owner32迭代×10试步、2e-9残差门；完整direct/separated两组各10个FD方向、三步长层/两Richardson层、5e-5原相对阈值及适用收缩；原inner17试步、RMS1e-6、boundary1e-11；fullDN末同当前H fresh audit、原物理RMS与domain全部保持。没有增加“全338解析J”、另一个numeric shadow对拍、独立审计或fixture。

R515只改变物理读回内部有限径向字的重复形成。原原理上已重关联的stage recorded-factor数学与原误差欠项没有被这次source连接支付。source complete、compile return、四component complete和原fullDN accepted分别由实际原字段负责，不互相推定。

## 8. 必要reader和compiler source选择

新reader schema：

`R518-live128-cached-radial-original-full112-necessary-v1`。

~~~bash
python -u "$R518_COMPONENT_READER" \
  --request "$R518_COMPONENT_REQUEST" \
  --request-sha256 "$R518_COMPONENT_REQUEST_SHA256" \
  --namespace "$R518_COMPONENT_NAMESPACE" \
  --out "$RUNNER_TEMP/visible-live128-cached-radial-R518-necessary.json"
~~~

帧：

~~~text
BEGIN_R518_LIVE128_CACHED_RADIAL_ORIGINAL_FULLDN_NECESSARY_SUMMARY
<一份完整必要ASCII JSON，至多90000 B>
END_R518_LIVE128_CACHED_RADIAL_ORIGINAL_FULLDN_NECESSARY_SUMMARY
~~~

它调用实际新runtime的原quiet；未证静止不读科学。原calls、owner/trial/replay、四component所有原必要completion/max/errors/partial地址、projection、原FD层与fullDN结果、rules、stderr和file identities原选择不减。

新增来源字段是逐component `physical_compiler_sources`。它覆盖boundary的height forcing、endpoint主编译、audit主编译；stage没有被虚构一个physical source调用。summary缺失时仍检查真实source binding文件，但不能因其存在就说compile启动或返回。

每项新source数据含：

- 实际source preparation receipt是否返回、完整binding文件存在性/bytes/SHA；
- adapter、upstream factory、准备祖先CPP、最终CPP与实际路径、原R283prefix和全部copied header身份；
- 原binding已有的范围布尔，不补默认“通过”；
- 同source path实际lifecycle返回行的原index、started/returncode/timeout/elapsed/allowance等，以及完整binding canonical相等与否。

receipt形成在process manager调用之前。返回行为空既不证明compile未启动，也不证明成功；已返回的进程仍可能失败。原requested argv与actual argv完整保于binding文件，其全文身份在必要摘要，未选进正文的命令/祖先嵌套值不冒root逐值读过。

新必要摘要加 `R518_source_composition` 和“request_number只是内部组件号”标志。source/hash不会补任何原数值、C²或native接受。旧reader的完整stderr按原规则保留；单份超90K则70，保完整本地overflow identity，`necessary_readback_complete=false`，禁止cleanup，不扩预算或拆编码。没有未来容量保证。

## 9. quiet后cleanup

~~~bash
python -u "$R518_COMPONENT_RUNTIME" cleanup \
  --request "$R518_COMPONENT_REQUEST" \
  --request-sha256 "$R518_COMPONENT_REQUEST_SHA256" \
  --namespace "$R518_COMPONENT_NAMESPACE" \
  --summary "$RUNNER_TEMP/visible-live128-cached-radial-R518-necessary.json"
~~~

原runtime实际CLI的summary参数名/路径须沿最终源；同源run/request/schema、单份完整necessary、真实再次quiet全部满足才删除。科学失败可以在完整必要范围和静止成立后清；必要失败/unknown不可清。不会删除公共原源或其它namespace。

## 10. 尚未执行、未来接线边界

本条未增加workflow/ref，没有任何新run id、编译结果、计时、FD或接受值。后续入口若沿该固定输入执行，可以直接绑定这份source plan与实际派生合同；若另换真正输入，必须另明确其新来源，不能以本条初猜标签代替值。真实操作仍由原public Actions、原runtime和原数学门支付。

原221、当前其它run与本条source-only对象分开记账。不得将R515局部条件证明、12view身份或351计数解释为全链完成、准确连续C目标、完整闭面g、全t强C²或性能改善。
