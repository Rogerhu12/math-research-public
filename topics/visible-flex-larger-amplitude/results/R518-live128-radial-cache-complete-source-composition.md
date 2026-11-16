# R518：同 call live128 原完整链的局部径向缓存来源组合

作者：ChatGPT（AI），2026-11-16 UTC。

**可信度：已证明，限本文明确的来源组合、控制流与条件命题。新的 R518 生成器、派生组件、编译、owner、FD、fullDN 与性能尚未实际运行。** 本条没有新的实验编号或实际结果；不改正在运行的221或其他入口。

## 1. 已付局部结论与本条责任

[R515](R515-physical128-local-radial-mode-word-sharing.md) 给出实际 C++ 接点：一次真实 `physical_jets` 调用内，第 $j$ 个径向系数的 field/state/geometry、精度、舍入环境和表达式不随角行 $n$ 改变。独立头文件只共享该原表达式实际形成的有限 binary128 字，包括负零和次正规字；非有限结果仍在原位置重算原表达式。所有角向项、累加顺序、`dP/dPt`、原 $C$ 求解及物理输出保留。该条件命题不声称整次运行逐字相同，不推定编译器未自行消除重复工作，也没有计时结果。

本条把该头文件接到原 [R501](R501-live128-original-full112-same-call-executable-composition.md)、[R508](R508-live128-scoped-ownership-and-original-input-repair.md) 的真实调用链。新增的是来源替换和实际收据消费；未改变原 owner、R273 数值核、stage、原 FD 或 fullDN 接受标准。

公开材料为 [生成器](../computations/root_20261116_live128_cached_radial_source_views.py) 与 [完整字面计划](../notes/r518-live128-cached-radial-complete-source-plan.json)。计划保存每个原文件完整 SHA、每次 `before/after/count`、每个输出完整字节数与 SHA。12份展开文件只在未来 Actions 工作树中生成，不作为本条新增 Git 文件。

## 2. 精确基线与集合

R508/221 基线提交固定为 `8b352f90b97f7c340a2fbebbb11c19080d9a5e08`。原请求实际位于 `computations/public-live128-scoped-original-full112-FD-fullDN-request.json`，54884 B/SHA `0fa9fe29153913252fd569cb2b99711c85b0afe72d8bc576adf629bd3e3f789e`。

R515 已发表提交 `02320c3a035d03c31c4e1fada1d19d9661bf7179` 的5253 B缓存头 `959d43bf…`、13235 B adapter `22e64c73…`、8662 B计划 `5950052f…` 保持原字。component view仍恰为R515已声明的32429 B/`0a7f4721…`，未另写数值实现。

原请求336项按原名、原SHA保留。新增公开依赖只有R515头、R515 adapter、本条generator，共3项；实际生成12项：

$$
336+3=339\ \text{公开输入文件},\qquad
339+12=351\ \text{完整当前文件}.
$$

原336项含 `source-dependencies.json`，它是原metadata；不因不是Python/C++而删除，也不说成执行代码。R515已发表JSON计划在独立 `published_metadata_dependencies` 中完整绑定，不伪装成可执行source-only成员。

集合的势不等于自动发现的递归导入证明。本条断言所列真实来源及原R501/R508闭包的保留。未改的直接/延迟导入仍由原工作目录和原源码负责，没有新增 `sys.path` 旁路、未绑定外部目录或历史hash恢复科学数据。

## 3. 真实目录与生成命题

生成器要求实际public Actions/原仓库、Git HEAD等于本次 `GITHUB_SHA`、自身 `HERE` 恰为 `GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations`。原221请求就在该真实HERE；原336项、3新公开文件、全部view baseline和R515计划均完整读核。

12个输出是互异新名，预先不存在。生成器先在内存完成所有字面替换并核所有输出完整SHA，随后逐件 `xb` 写出。每成功一件立即记录实际receipt并移除相应明确未生成role；异常保留已写范围、剩余role及原错误。没有科学导入、AST、编译或数值试探，不覆盖旧科学文件、原请求或Git ref。

**命题1。** 若实际准备完整返回，则各下游HERE均是原真实computations；由 `HERE.parents[2]`、同目录loader、相对Node import推出的原仓库关系真实。新文件使用自己的完整SHA，旧源未被新身份冒充。

**证明。** 先固定目录/HEAD并按完整public pin实读旧输入。每个输出是唯一baseline经有限明示字面替换的字节串，写出前核完整SHA；新名不与任何public名重合，输出均落在同一HERE，各原目录表达式未换。故实际来源与目录关系逐层成立。证毕。

owner内部仍沿原有独立engineering view机制：38408 B/`8855ef79…`旧wrapper经完整计划成为39154 B/`ce39e94d07b279bf136bd2af007e3f0f664015e37be3a8ea2197b7cd392696b7`。原完整逆替换检查保留。该生成文本不是8855原字，也不是另一已发表文件。原 `compile(changed, baseline_path, ...)` 仍沿旧实现显示baseline路径；真正执行来源必须用actual engineering SHA，不能仅据traceback路径冒称旧文件原字执行。

## 4. 每条实际调用边

| 层 | 新来源责任 | 保留责任 |
|---|---|---|
| outer R508 view | 新fullDN文件/SHA、独立namespace/schema、匹配necessary schema | 原输入恢复、clock、rules、PID/start-ticks、quiet/cleanup |
| fullDN view | 新client名/SHA，保旧pin并加新pin | 原7ba数学体，同一client交给原FD/fullDN |
| client view | 新worker/call/pipeline/QR/system tuple，旧18 pin加新10 pin | 原solve、初猜、cache规则、close、原policy |
| worker/call view | 新相对import、真实新client身份、pipeline input schema | 原snapshot、literal/physical packet、协议、warm、响应转发 |
| system/QR view | 新client/hook名、新system名/SHA | 原全部current576十数组、R273行/缩放/QR/kernel |
| pipeline view | 新owner/assembly/QR/system名与SHA、匹配input schema | clock/factor/solve-response、原子进程和错误路径 |
| owner view | engineering plan接R515 component名/SHA/schema | 原persistent128、32×10、fresh replay、当前H和真末128 |
| component view | R515已声明0a7f原字 | stage/边界/混合endpoint/audit全范围、预算与原门 |
| assembly view | 接受真实新component名/SHA/schema | 准确字投影、完整normal response、原client验收 |
| necessary view | 真读R515 compiler binding和返回进程 | 原trial/FD/fullDN/错误/partial地址和单90K |

system不能略去：原它以 `SNAPSHOT_LAUNCHER`、`SNAPSHOT_HOOK` 的真实文件SHA核snapshot。若只换client/worker而仍指旧名，会用旧身份核真实新snapshot。本条据此产生system view，并在QR/pipeline/client级联真实SHA；该检查含义未放宽。

client原18个 `LIVE_SOURCE_PINS` 逐键保，再加8个实际下层view与R515两源码。fullDN同样保原literal keys；新 `CLIENT_NAME` 指向真新SHA，旧client仍保字面pin。没有全局换表导致祖先丢失。

## 5. 来源闭合与数值条件命题

**命题2。** 在命题1的来源条件下，若原同call消费者按各自原合同返回，则进入physical endpoint、boundary真实height forcing或独立audit时，实际调用已发表R515 adapter。它准备的最终CPP为20048 B/`c0364bcd…`，编译argv仅替换原translation-unit路径；旧R493 19958 B/`5f6b2d3c…`是本次先准备而未由该中间命令执行的祖先。

**证明。** owner engineering plan的新component身份与真实component schema/source SHA一致。该component的 `QUALIFIER`/`OWN_PINS` 已由R515给定；对应编译经同一 `wrapped_base_process`。R515唯一识别原physical g++输入，先委托原工厂准备完整R493CPP，再按计划改include、3个cut调用、1个audit调用，生成最终CPP。旧命令尚未运行；原process manager只以最后actual argv调用一次。非physical分支仍委托原工厂，stage原interception/namespace qualification保持。证毕。

这只识别编译输入，不推定编译已运行或成功。receipt在编译前写出；相应实际进程返回和完整物理输出分别仍由原返回记录支付。

**命题3。** 固定同一实际完整输入、每次原精度/舍入环境和R515条件，本条唯一新增数值变化是R515局部有限字共享。原persistent owner、fresh replay、完整 $576\times224$ stage、局部226行/双mean、边界112、混合 $338\times112$ endpoint、全部独立audit查询及原FD/fullDN判定，没有因本条降维、替换或省略。

**证明。** 计划其余变化限source/schema/namespace/metadata/reader表示和真实pin。actor C++ `7789007e…`、stage `eca87efc…`、SIMD header `b183eeec…`、digit核、原边界以及所有数学函数正文未改。R515唯一numerical delta即所述调用内有限字共享，不用别的call系数、理想三角恒等式或角向重排，不将原 $C$ 换为nominal factor。原stage重关联和混合导数本已具有的误差边界仍按原合同承担，本文不另升级。证毕。

程序complete、source prepared、compiler return、原native gate、全FD、fullDN accepted是不同真实字段。没有全338解析J的新要求；原可用混合导数合同保持。原RMS/domain/终态audit门仍按真实原量判，不能由component完成推全链接受。

## 6. 实际派生合同与SHA无循环

没有新增公开request编号。新schema为 `R518-live128-cached-radial-original-full112-component-contract-v1`；`request_number=221`只表示冻结内部组件合同，不表示新actual221，也不指定未来实验号。后续若调用，必须使用新派生全文真实SHA与该job真正run/attempt/source。

54884 B原文件保持原字。生成器在独立metadata目录写 `derived-component-contract.json`，只变schema/operation/namespace、三执行role、source map/source contract、明确R518来源与结果/发表metadata。原输入、actual63、actual91、runtime、全部预算、科学合同、arithmetic、retention、README、lanes、repository逐对象保留。

新对象保原请求完整身份、实际plan与generator身份、source receipt路径、本次Git SHA；写成后计算新完整bytes/SHA。旧 `0fa9fe29…`只能作祖先，不能传作新 `prepare/run/reader/cleanup` 的request SHA。

依赖无SHA自指：plan绑定已形成generator和12输出；新请求可绑实际plan收据；生成收据最后绑定新请求。请求只写生成收据实际路径，不把该收据自身SHA再写回。各原caller仍以真实请求全文SHA和实际run/source核身份。

## 7. 原钟、资源与进程责任

生成器不创建科学钟；它先于原R508 `prepare`。原输入完整恢复后，原 `run` 在rules和第一次factory前创建唯一 `job-deadline.json`，不移到第一次H以后，不因call/component/compile/组装重启。

保原19200秒、末120秒readback/cleanup reserve、350分钟job/320分钟科学步、64GiB启动可用盘门、2GiB退出保留、4线程、原Node/Jacobian/exact worker内存配置。owner6000/replay1200/stage8000/boundary600/endpoint600/audit1800等都是原剩余绝对钟内上限，非可相加的新总预算或完成保证。资源不足仍走原未起/partial/error。

R508完整进程算法未改：pid/start_ticks/uid/pgid/sid、实际后代、namespace参数/环境；不因同uid接管无关进程，不把unreadable的真实/疑似owned process当quiet。registered group信号、wait/reap、unknown阻断和必要读回后cleanup原样。source准备不产生科学worker。

缓存可能改变耗时，因而同预算下实际已访问范围未必相同；本条不声称whole-run trace或接受序列逐字相同。每个资源cap不是额外科学门。

## 8. 必要读回正向消费

原necessary先实际 `runtime.quiet`；静止未证即不读科学结果。本条保存原全部选择规则、trial/未访地址、FD层、fullDN字段和完整stderr处理。单份ASCII JSON仍90000 B，超限70；原必要对象留本job，未返回不冒已读；不分片、不编码大树，不保证未来容量通过。

新 `physical_source_bindings` 只读以下真实文件：

- boundary：`forcing-compiler/compile/physical-radial-mode-cache-source-binding.json`；
- endpoint：`compile/physical-radial-mode-cache-source-binding.json`；
- audit：其同名真实compile文件。

每份由原 `Reader.get` 记录存在性、完整bytes/SHA和错误。component summary没返回时仍可报告已存在source receipt；不存在不冒空文件。选出adapter/upstream factory、准备祖先CPP、最终CPP与路径、原R283prefix、全部copied header身份和原scope旗标。

另按原lifecycle地址寻找同actual source path的 `live128_physical_radial_mode_cache_source_binding` 返回行，并以完整canonical JSON比较该行与实际binding文件。原started/returncode/wall_timeout/elapsed等及比较结果照实返回。没有返回行只表示该集合空，不能推断“未启动”或“成功”。

原 `compile.command` 是qualifier前的requested命令，不代表该静态名字实际执行。完整binding中actual/original argv和祖先嵌套正文仍在同job文件。本必要摘要选择来源身份和返回进程，其他正文只保文件身份；不说root逐值读过。R515唯一argv路径替换条件仍适用。

原字段缺失/null由原keep规则保留；新增source字段也只选实际有键的记录。最终reader的source composition标签明确221只是内部编号。原native/fullDN false声明不会被source receipt改写为数值失败或接受。

## 9. 完整生成身份和未付范围

下表是字面生成完整身份，非执行结果：

| role | Actions 临时源码名 | B / SHA256 |
|---|---|---|
| components | geometry_20261116_live128_cached_radial_final_components.py | 32429 / 0a7f47213789bc4779a6241b121f636d2356302b9f258fdf7a94b3dec4b02f8b |
| owner | geometry_20261116_live128_cached_radial_same_call_owner.py | 18902 / 561c1db5122086abab05aa968db4597b46fad77ab887bd7c5faac985a6bdd3ae |
| assembly | geometry_20261116_live128_cached_radial_response_assembly.py | 28615 / 2807377e96e127af2aee6ca3257bafbd8f6b884a5c80e0959d985e8b4d35bffc |
| system | exact_20261116_live128_cached_radial_current576_system.py | 29003 / 1cf6338e47541cb3af65d507de462dd6143f35aea7661575e8bc45c07fb5c86b |
| qr | exact_20261116_live128_cached_radial_current576_chain_qr.py | 21844 / 9c2cf83ec714f1e225071228320c169416a6ff86eddce0c717163a323a3a83dd |
| pipeline | geometry_20261116_live128_cached_radial_call_pipeline.py | 19348 / 436db54132702cf448169e93a1d6d6d1327a63d5fbce1de1c4dd30ec87912fcd |
| call | geometry_20261116_live128_cached_radial_current_call.mjs | 34383 / e9978c3a4692cee5ab7c27339272a45c18ffe5108fd32e8e3531cc4044b29296 |
| worker | geometry_20261116_live128_cached_radial_worker.mjs | 8181 / 16dd7cb9f1ee91c43d06620aebc3cdf2e67fe75d416caf3c1d118aff9f3e39ae |
| client | geometry_20261116_live128_cached_radial_tail_client.py | 31726 / d4b9a1cae39c744e1b579faa4d3559a5fe2ad3e33a052324cb3099d3c26f56aa |
| fulldn | geometry_20261116_live128_cached_radial_original_full_dn.py | 36808 / 9799a1b33ae52d1e5137ac51207bf48b01d41753732ec67225f738e17f764f91 |
| runner | geometry_20261116_live128_cached_radial_owned_run.py | 39021 / 86e416fb5d905bc85864931953d2fbc978f0585f117269b295c5bab3de0cefbe |
| reader | root_20261116_live128_cached_radial_necessary.py | 38722 / c186444eacb89add6e75ff6730851978ad8ba581f99dd447154fd5c258b15c2a |

本条没有真实新parent、编译结果、owner数值、H/J、trial、FD误差、native/fullDN接受、全C²/闭面或速度结论。后续公开调用才按原门支付。原同H cache仍只在本次真实响应后使用；actual91 failed73和actual63仍各自只作明示初猜，不从旧结果或SHA继承新解。

实际若在准备/compile/owner/stage/projection/FD/fullDN/quiet任处停，应据该run原返回和必要范围归责。本条不为正在运行的221或其它run补结果，也不添独立benchmark、fixture、审计或接受前门。
