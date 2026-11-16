# Request225：配对 stage / 局部径向缓存 live128 原完整 full112 接口

作者：ChatGPT（AI 助手）  
日期：2026-11-16

本页配套 [R527条件结论](../results/R527-live128-paired-stage-and-radial-cache-complete-chain.md)。**完整源码、参数、workflow和必要读回已实现；尚未将本页准备时间冒成actual225运行。** 实际运行、终态与未完成范围由R528另记。原221运行及原源不改；本页不把原stage或physical局部算术命题升级成native/FD/fullDN已通过。

## 1. 六份发布件与来源

topic前缀是 `topics/visible-flex-larger-amplitude/`。只发布下列正常源码、计划、请求和文档；展开view、完整diff和交接manifest不入Git。

| 路径 | B | 完整SHA256 |
|---|---:|---|
| computations/root_20261116_live128_paired_cache225_source_views.py | 22915 | b30d418965454b63d5a0e8f6bc50277e38849e959e24ec92552bc722ec83a3ce |
| notes/r527-live128-paired-cache225-complete-source-plan.json | 55391 | 6e8109e64bafb6e78428298ccc25a5b4d71df29c0b224b0ea20076da006dd1c6 |
| computations/public-live128-paired-cache-original-full112-FD-fullDN-request.json | 64734 | 42fe3eff48338d540707c690d6aadd0cfdfeaa278a1145b1db885bea9df37285 |
| 根路径 .github/workflows/visible-larger-public-live128-paired-cache-original-fullDN.yml | 18518 | 5ed7a2c3fd2fdab0d2fe02aeb050a07e3bfe8f3344b23ba3bd16f7573b274d53 |
| results/R527-live128-paired-stage-and-radial-cache-complete-chain.md | 18592 | 2b6a237c372c3fa448ce1b522d2da230c2d372b5f88a759ed70515508f41c9e9 |
| 本接口 | 最终manifest给真实完整身份 | 不在自身嵌入自身SHA |

固定原221请求54884 B / `0fa9fe29153913252fd569cb2b99711c85b0afe72d8bc576adf629bd3e3f789e`，来源 `8b352f90b97f7c340a2fbebbb11c19080d9a5e08`。R515发布 `02320c3a035d03c31c4e1fada1d19d9661bf7179`；R518发布 `bfe02a5249db7c01665fef163034d436d66ebdbd`；R522发布 `3514dfb8333ec3d42cf62ba6165c0f799dd3bf6f`。

R522正式component是33416 B/`93ecdd83…`，不是旧33207 B draft。原R518的32429 B/`0a7f4721…`只是本次内存重建的组件祖先，不作为实际current component安装。

## 2. 当前 schema、目录和计数

| 对象 | 当前准确值 |
|---|---|
| 请求schema | `public-live128-paired-cache-original-full112-FD-fullDN-request-v1` |
| request_number | 225 |
| 科学namespace | `RUNNER_TEMP/visible-live128-paired-cache225` |
| 源准备metadata目录 | `RUNNER_TEMP/request225-source-preparation` |
| 源准备schema | `R527-live128-paired-cache-source-view-preparation-v1` |
| 来源计划schema | `R527-live128-paired-cache-complete-source-plan-v1` |
| client policy | `R527-current-H-live128-paired-cache-client-policy-v1` |
| owned runtime | `R527-live128-paired-cache-original-full112-owned-procedure-v1` |
| 科学necessary schema | `R527-live128-paired-cache-original-full112-necessary-v1` |
| 原唯一deadline schema | `R493-original-full112-live128-job-deadline-v1`，由当前真实225源写 |
| 科学necessary文件 | `RUNNER_TEMP/visible-live128-paired-cache225-necessary.json` |
| 源necessary文件 | `RUNNER_TEMP/request225-source-necessary.json` |

原336public项逐值保留；6新增public形成342；实际3个R522与11个R527输出形成14；最终source map356。`generated_source_sha256` 仅列14个实际输出。原request内旧source_contract作为 `inherited_frozen221_source_contract` 完整保留，历史336/219/221说明不是当前文件计数。

三个独立metadata计划仍是原R515 8662/5950052f、R518 48391/4f209705、R522 16347/724e46e0。新R527计划在其外给所有实际连接，不把JSON计划混入只允许可执行源码的子列表，也不把旧view当作公开文件下载。

## 3. 源生成的真实CLI与失败语义

公开Actions中，`GITHUB_WORKSPACE` 是真实checkout，`VISIBLE_COMPUTATIONS` 是该checkout的topic `computations`。所有14新source实际写在该目录，使其 `HERE/__file__`、原public_resume、cpp include和当前client loader路径相符。源码新名不覆盖旧公开文件。

~~~bash
R225_REQUEST="$VISIBLE_COMPUTATIONS/public-live128-paired-cache-original-full112-FD-fullDN-request.json"

python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_paired_cache225_source_views.py" prepare \
  --request "$R225_REQUEST" \
  --request-sha256 42fe3eff48338d540707c690d6aadd0cfdfeaa278a1145b1db885bea9df37285 \
  --out "$RUNNER_TEMP/request225-source-preparation"
~~~

生成器先绑定当前source、请求、完整计划、原221请求、342public文件与3metadata计划。随后从公开原件重建全部12个R518输出文本，核全部原完整身份；它们不写出、不import、不执行。再形成11个当前caller，逐项核before/count和完整输出。

真实R522子过程使用未改CLI：

~~~bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_native128_paired_digit_source_views.py" \
  --computations "$VISIBLE_COMPUTATIONS" \
  --namespace "$RUNNER_TEMP/request225-source-preparation" \
  --plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/r522-native128-paired-digit-source-plan.json" \
  --plan-sha256 724e46e0d70aefd70309e03d77d4719666058e56001c7a78f7544bada76b9ce7 \
  --out "$RUNNER_TEMP/request225-source-preparation/R522"
~~~

它只生成源码，不启动科学clock。外层保实际argv、启动/返回、returncode、stdout/stderr身份、真实R522回执。3个实际输出核同后，11caller才逐件排他写入。每写一件更新实际receipt和未生成后缀。

source准备失败不产生科学成功receipt；当前phase、原错误及已经返回/尚未返回范围保留。若R522子过程失败，其原views/not_generated范围仍在本次metadata中，不把source receipt存在等同于全部3件完成。若还没生成necessary reader，后续科学读回可能是“程序未存在/summary未返”，report如实写缺失，不调用旧reader冒当前225。

源readback的CLI与prepare相同，只将mode换为 `readback`。它先绑定实际请求/计划，再从本job源回执读必要scope；普通源失败的scope若已完整读回，可以是 `necessary_readback_complete=true` 且 `source_preparation_complete=false`。科学未开始仍由其他字段独立记录。

## 4. 十四份真正生成源

下表是本次真实生成的全集合；不另外提交这些展开文件。原R522三份保持其已发表计划输出字节。

| role / basename | B | SHA256 |
|---|---:|---|
| operator / `geometry_20261116_native_paired_digit_operator_trace128.hpp` | 29617 | 082d5a1fdd900071fb1cc008304c5a4c97bce92b173851bda1514ec1682eb7be |
| stage / `geometry_20261116_native_paired_digit_stage128.cpp` | 12880 | 49a7e226eadc7748d5d2b3f94119c2e4dd7024348e6878c673e73b1a33db3b55 |
| components / `geometry_20261116_live128_paired_digit_final_components.py` | 33416 | 93ecdd833922f833bdb50a8f264bc5db1913f5ce16dbb0cb4f7fbc7d285070f1 |
| owner / `geometry_20261116_live128_paired_cache225_same_call_owner.py` | 18905 | a587dd6833532c60296ed40ce105d9c190717071e8d6fb3e137f79a27d9209be |
| assembly / `geometry_20261116_live128_paired_cache225_response_assembly.py` | 28613 | 5fa469847019a8fdaf040245a93ff6a447da13ecda468fc6285f90e2c096504c |
| system / `exact_20261116_live128_paired_cache225_current576_system.py` | 29007 | 6158c460dc9abd7ea153a0b2708decdf1378f8b0a79e46bbe947d4d8b59074f6 |
| qr / `exact_20261116_live128_paired_cache225_current576_chain_qr.py` | 21846 | 9e393cd970554e48203f80f86d6734a74ba67ff7bfa51964cbd5ff9d4450b48c |
| pipeline / `geometry_20261116_live128_paired_cache225_call_pipeline.py` | 19356 | c01aae5614d00c746c671eb98abcdc6ab90aa39366e8c0a7d3b5da3ed83fd515 |
| call / `geometry_20261116_live128_paired_cache225_current_call.mjs` | 34385 | c9f83fd2f1db33c66dae653291bf48db7e2cfe3a8f5f87b4ba01b92d6626eb50 |
| worker / `geometry_20261116_live128_paired_cache225_worker.mjs` | 8183 | 0be16b9bbfd1635c5bc0155f45b222534486c5491e1e6c14b32ad8e605ffb2bf |
| client / `geometry_20261116_live128_paired_cache225_tail_client.py` | 32147 | cfcc205cf0c291dc6a4dfd280a4c60f67f1d84062761e68c62117714867cb328 |
| fulldn / `geometry_20261116_live128_paired_cache225_original_full_dn.py` | 37222 | 4c5c0c0dab7fe1b96dc4065acc4c027ea872fedbf6b4f750f462cb0af6ee3aca |
| runner / `geometry_20261116_live128_paired_cache225_owned_run.py` | 38997 | 9e3d7508cfd771e34003e6056020b316cd227f92154280a449226d415f86f400 |
| reader / `root_20261116_live128_paired_cache225_necessary.py` | 41304 | 85631e35dc9f8f3e2ce5b19a05e8b540ee802b2e8c9e6b3cb01cb3c730cbe8e3 |

source map中的全部原336、6newpublic、14actual没有重名。新client下层31项包括原18项、8新lower views、R515两公开源及R522operator/stage/kernel3项。新fullDN保所有原祖先literal keys，同时将真实client、worker、pipeline、owner、assembly/system/QR/component指向本表当前源。

owner私有engineering文本39152 B / `ea97b5f7abf5842acf2d74907ab361fff1002a7f8a774aefbb2c568eeb33e729` 按原合同在call内形成，原38408 B祖先wrapper并未覆盖。这里不把私有wrapper另算成Git公开view；它由原owner的完整工程计划绑定。

## 5. 原数据与恢复合同

原六份输入完整字典与221逐对象相同，Git来源commit均为 `8bd267107cc8710d371f3b62c02986655ac965b0`：

| 用途 | B | 完整SHA256 |
|---|---:|---|
| historical accepted prefix | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| actual63 warm-001 gzip | 4799943 | 6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a |
| actual63 driver-status gzip | 231286 | 6443fce5e818ff20fd36075f6038ee60630d0b77e8ed2304d41e4d072ea6a005 |
| 原112 tail config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| frozen ledger-ready | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| frozen stored-ready | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |

ledger-ready保原完整64字符SHA，继承R508已付修正，未重新引入R502所记的旧63字符错误。

actual63 warm/status与其真实producer关系由原准备代码核；status解压后1810333 B / `8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46`。这对原件是新prefix初猜，不能从旧intent或下载清单替代。

actual91尾初猜仍取原run43672150224、artifact14145200674、名字 `visible-mainline-modelresponse-43672150224-1`，完整zip10267458 B / `78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6`。它不是prefix，不附带旧accepted/native保证。若官方原artifact无法取得，真实prepare失败，不从hash重造内容。

原78完整source恢复仍走原 `exact_20261114_public_resume.py`，实际source-root在当前namespace的真实repro树。新caller仍以真实目录读原恢复模块。全部网络读取使用原公开Actions凭据的环境变量；不将token写入计划、request、回执或Git。

## 6. 当前 H 的完整执行

原准备阶段：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_paired_cache225_owned_run.py" prepare \
  --request "$R225_REQUEST" \
  --request-sha256 42fe3eff48338d540707c690d6aadd0cfdfeaa278a1145b1db885bea9df37285 \
  --namespace "$RUNNER_TEMP/visible-live128-paired-cache225"
~~~

原科学阶段仅将mode改 `run`，其余实际输入同上。runtime按原程序创建唯一deadline，然后原rules模块从独立sparse mirror真实pull/rebase、比较已读双README，再执行科学子进程。当前schema/policy/ns是225；原clock schema沿R493但payload真实绑定225source/run。规则模块只在内存用实际已读README文本更新原BASELINES，并写来源receipt，原科学checkout不被规则mirror修改。

每个实际H的完整链保持：

1. original64真实withJ，原current576完整残差/矩阵与R273全部行；
2. 同当前H persistent128，原32×10试步与原residual门；
3. 当前末state的独立fresh replay；
4. 全stage576×224、boundary112、mixed endpoint338×112、完整audit；
5. 明确128→64投影与原normal response；
6. 原完整FD、prefix/fullDN和最终同H fresh audit。

每节点shooting state224项、局部RK226项/双mean、577个radial node资料、576个stage、338输出是不同布局，不互换概念。338输出顺序仍height112、mean1、slope112、mean1、second112。

component33416/93ec实际调用R522配对stage和R515 physical qualifier。原boundary高度forcing、endpoint和audit全部角查询仍付；只共享单次 `physical_jets` 中有限径向词。原所有 $C$ 解、角向求和、mixed导数、mean、domain检查和错误都保留。

## 7. 算术身份与原门

R522在原完整dyadic输入上计算两条独立准确整数和，分别经原RN113一次舍入；同left plane只共享载入/移位。非packed、wide或全零条件沿原两次完整dot fallback，原nonfinite检查继续。完整已返回点积与原R414字等价，不能推出旧whole-run trace、资源停止顺序、FD结果或速度相同。

R515缓存只在单次原physical调用有效，不跨state、H或query；非有限词按原位置重算，不以缓存绕过原错误。原R493组装的projection仍RN-even且signed zero保，原hex residual/mean和worker正文直通不变。

原阈值与迭代：

| 项目 | 原值/范围 |
|---|---|
| field/tail modes | 112 / 112，spacing2 |
| 原native迭代和档位 | 32次 × 10档 |
| 原solve tolerance | 2e-9 |
| FD分组与方向 | direct_boundary、separated_boundary，各10 |
| FD层 | 原3step、2Richardson、全部原适用contraction |
| FD相对阈值 | 5e-5 |
| prefix内层档位 | 17 |
| prefix RMS / boundary | 1e-6 / 1e-11 |
| 最终责任 | 原完整物理RMS/domain、同当前H fresh audit、原fullDN判据 |

没有新全解析338J、shadow对拍、benchmark或fixture门。现有mixed J仍合法，但需原实际FD/fullDN自行返回。source complete、compiler return、component complete、normal response、FD pass和fullDN accepted严格分层。

## 8. 原资源与单钟

| 资源 | 原保持值 |
|---|---|
| job | 350分钟 |
| science step / 总科学钟 | 320分钟 / 19200秒 |
| readback/cleanup终末保留 | 120秒 |
| 初始可用盘 | 68719476736 B（64 GiB） |
| 可用盘资源停止保留 | 2147483648 B（2 GiB） |
| owner / replay cap | 6000 / 1200秒 |
| stage / boundary / endpoint / audit cap | 8000 / 600 / 600 / 1800秒 |
| C++线程 / exact workers | 4 / 2 |
| Node heap / Jacobian workers | 6144 / 2 |
| 最大factor字节 | 2147483648 |
| max nodes / material / physical angles | 1200 / 4096 / 4096 |
| outer iterations / extension / taper / eta | 8 / 0.005 / 0.4 / 字面“1” |
| 原声明最多未缓存protocol calls | 18，不保证全部可完成或可存放 |

每个call cap按同一真实deadline剩余裁剪，不重新启动19200秒；不能把表中各cap相加当总允许量。源准备、runtime安装、原输入恢复发生在原科学clock之前，但仍受job350分钟硬上限；科学clock含原规则同步。实际预备耗时可能使job先耗尽，不保证完成任何特定轮数。

workflow新增sourceprepare10分钟、source-readback5分钟；原restore30、science320、necessary20、cleanup5、report5保持各真实step上限。它们不是可相加的job总时间。startup容量不足按原实际停止，未清scientific数据；只有原声明的unused runner SDK目录可以沿原workflow释放。

## 9. 两类真实 compiler receipt

stage实际绑定路径：

`<namespace>/<call>/owner/final-components/stages/compile/paired-digit-source-binding.json`。

必要reader的新 `paired_source_binding` 无论component summary有无返回都会读取该文件存在性/完整identity；若返回dict，完整保存原 `paired_digit_compile_source_binding`。此dict是源码/argv/flags来源metadata，没有state/J/ledger数值数组。原lifecycle中每个带同key的返回行保原index、进程状态，并报告与文件的canonical严格相等；不因相等添加科学通过门。

R515保三个实际编译site：

| component/site | 相对component目录 |
|---|---|
| boundary / height-forcing | forcing-compiler/compile/physical-radial-mode-cache-source-binding.json |
| endpoint / main | compile/physical-radial-mode-cache-source-binding.json |
| audit / main | compile/physical-radial-mode-cache-source-binding.json |

原R518选择器保这些文件的完整bytes/SHA、actual/prepared source、header copies、完整作用范围标志与对应返回进程index/fields。其余完整binding仅本job身份，不冒全正文已返回。旧compile.command仍是qualifier前的requested argv；actual_executed_source与实际binding给出最后执行源。

只有binding文件不等于编译已执行。实际compile可能尚未起、未返回、超时或失败；reader保存原process/summary/error地址。不得从sourcePrepared推断四组件完成，更不得推FD/fullDN accepted。

## 10. 两个独立必要scope与精确帧

source-preparation scope帧：

~~~text
BEGIN_REQUEST225_SOURCE_PREPARATION_NECESSARY
...一个完整ASCII JSON body，含末LF...
END_REQUEST225_SOURCE_PREPARATION_NECESSARY
~~~

科学scope帧：

~~~text
BEGIN_REQUEST225_PAIRED_CACHE_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
...一个完整ASCII JSON body，含末LF...
END_REQUEST225_PAIRED_CACHE_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
~~~

source必要schema为源schema加 `-necessary`。它保当前run/request/plan/source、完整源回执identity、14actual输出、12内存ancestor身份、原R522子返回、原phase/错误/未生成地址。完整342文件逐项receipt仍在绑定的本job源回执内，必要body只保count和该完整原件identity；这是来源metadata选择，不是科学数值账本搬运。

科学readback CLI：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/root_20261116_live128_paired_cache225_necessary.py" \
  --request "$R225_REQUEST" \
  --request-sha256 42fe3eff48338d540707c690d6aadd0cfdfeaa278a1145b1db885bea9df37285 \
  --namespace "$RUNNER_TEMP/visible-live128-paired-cache225" \
  --out "$RUNNER_TEMP/visible-live128-paired-cache225-necessary.json"
~~~

原选择范围保全部原返回trial必要标量/地址、未访和失败、FD原layers与contraction、fullDN原返回、双mean、四组件完成/未完成、原stderr及实际quiet。新增仅实际两个compiler来源选择，不复制raw state/J/大ledger。

两个scope各自≤90000 B。超过上限明确70，并返回该未完整读scope的完整选中对象bytes/SHA；本job保原对象。不分包、不字典编码科学树、不截断后声称成功，未知实际body大小不预保证通过。科学body没有因source body而拆分；两者职责和生成程序不同。

compute的source/necessary outputs均带精确body bytes/SHA。report先返回source scope，再以 `if: always()` 返回科学scope，即使前一个出错也不掩盖后者。report逐字核body+LF与run/source/request，不从job success或failure标签推数学结果。缺scope时明确absent/未返，不能用祖先reader输出替代。

## 11. 生命周期、保留与清理

原R508 scoped-lifecycle合同保留。登记真实pid/startticks/uid/pgid/sid与实际namespace；原rules创建的独立session由runtime捕获并登记，science同pid exec在启动前登记。当前真实后代和可读namespace证据属于责任范围，真实own/可疑own不可读仍unknown。不能将所有同uid但env不可读的外部进程冒成own，也不能普遍忽略PermissionError。

科学reader先求实际quiet，不能证明即不读/删科学raw。runtime finally仍尝试原登记组终止/等待并记录reaped/unknown，静止不是一个仅由step返回码得出的推断。

workflow清理要求 source_readback_complete 与科学 necessary_readback_complete 均true，再调用当前runtime `cleanup`，由其重新核原request/run/source/ownership和实际quiet。最后一次quiet若不通过，明确removed=false。科学失败但必要范围完整已读、所有own静止时，允许原namespace清理；必要未返、超限或quiet未知时明确skip，raw留至runner销毁。

源码准备metadata和两个小necessary文件均在科学namespace之外。原cleanup仅删除当前 `visible-live128-paired-cache225`；它不删除科学checkout、其他namespace或source-preparation目录，不发布大artifact，也不把raw提交Git。

cleanup的skip分支沿R508采用单个quoted Python命令，不重引嵌套heredoc语法错误。新source必要读取失败会阻止删除；它不阻止已授权科学阶段的运行或降低数学门。

## 12. workflow、发表与实际责任

workflow同时支持 `push` 当前请求路径和 `workflow_dispatch`。恢复发布使用 `GITHUB_TOKEN` 时，普通push不保证触发科学；root须在真正发布后调用官方dispatch并核实际run/head。本文不预填那些尚未发生的身份。

workflow compute保 `contents: write / actions: read`；正常Ubuntu/Python3.12.14/Node24.22.1、numpy2.3.5、scipy1.17.0和原C++编译环境沿221。所有代码只在未来实际Actions按原语法检查和科学命令执行。本地只作文本、JSON、hash与完整diff构造。

六发布件中topic新增为生成器、计划、请求、证明与本接口；workflow在根.github。14展开源码及11caller完整差异仅在临时/交接环境，旧公开文件与运行221不修改。manifest不额外成为科学输入或通过门。

当前R527支付完整来源/调用连接和原合同保持；以下仍待实际225/R528：输入恢复、source生成与原语法实际成功、当前H各真响应、全部四组件、实际FD/fullDN、真实资源前缀与最终readback/cleanup。完成source组合不等于支付这些运行事实，也不等于本课题README闭曲面与全t精化标准。
