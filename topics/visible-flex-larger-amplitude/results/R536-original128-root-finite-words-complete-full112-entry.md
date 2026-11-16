# R536 — 原128局部有限root字词的完整full112执行链

作者：ChatGPT /root，reader协作：amplitude，物理路径子件：geometry（AI-assisted）  
日期：2026-11-16  
可信度：**已证明，限列明来源、有限原表达式及完整返回的条件命题。** 本文交付可执行request226及公开Actions入口；实际结果预留R537，来源与run必须由随后真实单次dispatch确认，不预填。

## 1. 本结论解决的具体接线责任

[R535](R535-original128-local-finite-root-words-and-real-compiler-hook.md)已完整给出原root内固定momentum、pt、P、Pt以及每次evaluation内U系数的有限字词共享、原fallback和实际compiler接点。它本身没有把该接点装入正在执行的owner，也没有使原必要reader返回新统计。本节补齐这两个真实调用处、全部来源级联和独立实验入口。

基线是已刊R527/request225的完整原full112链。全部原342个public源、原初始输入、原数值参数、原paired-stage及物理cache组成继续有效。原R522三件生成源保持原字；R535两件include source由其已刊adapter实际生成。新十一caller只在真正computations中生成，不覆写225源，也不复用旧运行中或已清理的state。

R509中当前H的owner在6000秒内未完成原容差和fresh replay，是本优化对应的具体先行成本。此动机不是加速证明。R534的projected64后置模型不在本请求中注册：本节后置stage仍是原R522完整128配对计算，物理endpoint/audit仍是R515原接点。不能把两条独立实验的模型或性能假设混入本请求。

## 2. 完整发布身份与有限来源集合

路径除workflow外均相对于topics/visible-flex-larger-amplitude。

| 角色 | 路径 | bytes | SHA256 |
|---|---|---:|---|
| 生成器 | computations/root_20261116_live128_root_words226_source_views.py | 30464 | 14a86c71268ccd017c6e85294c7af9b714c2234063c2ef1953caf35458bd6052 |
| 完整字面计划 | notes/r536-live128-root-words226-complete-source-plan.json | 62193 | 772e3da8b00d692672802b0e61f0e038b08b0014b03ad7e136f9cb312412ba69 |
| 实际226请求 | computations/public-live128-root-words-original-full112-FD-fullDN-request.json | 71828 | 668518481e635c4832df3a5ab8a9709585d2358546904cee0eeab0df032e2c64 |
| 公开Actions入口 | .github/workflows/visible-larger-public-live128-root-words-original-full112.yml | 18755 | 0d23754153779173dc6d4973ba06325896f193c0316f043cc10258cae4dd93c1 |

本证明与[完整接口](../notes/2026-11-16-request226-root-finite-words-full112-interface.md)另以实际发布身份记录，不循环写自身SHA。

当前有限source集合恰为345 public +16 generated =361。345保原225全部342个public，另加R535 header、R535 adapter和本生成器。16包括原R522三件、R535两件以及十一新caller。原R518十二个中间view和原R527十一caller都先按已刊plan形成完整文本、核完整bytes/SHA；它们作为中间文本不写出、不导入、不执行。原225完整request及R515/R518/R522/R527/R535全部metadata计划另按完整身份核对。

这不是自动发现无限动态import的断言。每个实际新callee、固有原数学source、真实runtime及其所需source文件均在明确表与原固定恢复关系中承担责任；所有旧336 source pin及225新增六public保持原值。

## 3. 十一个实际新caller

下表各项是完整plan输出，不是已经在科学运行中生成的文件。它们不能在源准备前当普通Git文件下载。

| 角色 | 实际basename | bytes | SHA256 |
|---|---|---:|---|
| owner | geometry_20261116_live128_root_words226_same_call_owner.py | 21969 | 934e92b1d381e5c268346556327fb76147c20e73bb9b4b9ddb6ca91aad7ab3fb |
| assembly | geometry_20261116_live128_root_words226_response_assembly.py | 28611 | 1a67a3fe236b97fca188a9fea454b863855bb3b63260a3d75bff9e272176d620 |
| system | exact_20261116_live128_root_words226_current576_system.py | 29003 | a147c07d859db9207da385f582706fe908d9264aacffbc51b1b62bf6064e4151 |
| qr | exact_20261116_live128_root_words226_current576_chain_qr.py | 21844 | 54ffe440189fdc645e3c6aa8ffab8e6abb6c4e704b97479742bf88e4760137d5 |
| pipeline | geometry_20261116_live128_root_words226_call_pipeline.py | 19340 | cab766daf5549d957454c14ca0365817fdf287a25a01944d597a19c6a4e42318 |
| call | geometry_20261116_live128_root_words226_current_call.mjs | 36879 | aa05fa425b41382b0177772c21b8134040925fdca323e3aa35ab3473c414055c |
| worker | geometry_20261116_live128_root_words226_worker.mjs | 8181 | 39f54dec2d7ff23d28a343296a5b5bfa33085d3ccbf3f96b1545b7cbe08de8f8 |
| client | geometry_20261116_live128_root_words226_tail_client.py | 32599 | dfb8fcf39a118020fc59ea9febc0d2be6bb0d85edd82ac98bf6d8fe645357fa4 |
| fulldn | geometry_20261116_live128_root_words226_original_full_dn.py | 37692 | 97bb244447ef809ed17cf73fe3dde75c440630e9d9441c3b188a73f7d7cd32bc |
| runner | geometry_20261116_live128_root_words226_owned_run.py | 38985 | 8801c39604dfa6c7a6087886fffb3aefefdcf9f1a0c51152acbb6ff93793a0fd |
| reader | root_20261116_live128_root_words226_necessary.py | 52189 | e90e3abd2e40ebd469bcd8d4dd7f221848c9926c91b86c8e2ee29235b1be864a |

计划含78项明确字面修改。每项有完整before/after/count；生成器逐项核原出现次数，逐中间源核完整身份，最终逐新source核全部字节。文本级完整逆可还原相应225原件。这里只进行了源码文字、JSON、字节与身份组成，没有本地AST/import/compile/科学测试或fixture。

R535本次生成的两源仍是primal25230B/3e1cb0a416418fe56fbee889df5debdfc9ed097b797a1b8e086b563ce4fd9241，以及trace34950B/2e122e0ca6ad21e1c11ab711cc5af40a6955d3ff054f6cd445dbd885fbb98b12。原persistent CPP22364B/7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd保持原字。展开源只在Actions临时生成，不重复刊Git、Release或artifact。

## 4. 源准备和真正compiler执行的分层

新生成器在RUNNER_TEMP/request226-source-preparation写真实source-views.json。先核所有public和metadata祖先，完整构造R518及R527中间文本；再实际调用原R522子生成器和原R535 adapter CLI。二者只准备source，不启动原科学总钟、不编译C++、不求值root/RHS/RK。

R535子目录为R535，真实输出source-binding.json。子进程的command、started、returned、exit、stdout/stderr、实际每个generated source是否存在及完整身份、实际binding全部保留。若只生成第一件后失败，第一件的真实身份与第二件未生成状态仍分列；不把整个child失败说成从未写过任何源。

仅两个子生成器及全部十一caller都真实完成后，source-preparation.complete才为true。来源准备自己的单份必要scope与科学必要scope分开；二者都保90000B/70，不能用两份scope拆一份大型科学结果。

## 5. 安装发生在原owner的真实global scope

新same-call owner先按原225完整VIEW_PLAN生成原engineering wrapper，再实际执行其source_scope("owner")。该嵌套VIEW_PLAN连同原derived SHA本节保持原字：其R527内部格式名表示被识别的原engineering祖先，不能全局换标签后仍冒原SHA。

就在得到owner_scope之后、原owner_scope["main"]()之前，新代码调用install_root_finite_words。该函数核：

1. 原固定RUNNER_TEMP/request226-source-preparation/source-views.json，真实当前run四键、request226、R536 schema和complete；
2. actual_computations为真正HERE，generated中本owner完整file/bytes/SHA与实际__file__一致；
3. R535 child确实returned、exit0，binding来自唯一明确R535/source-binding.json路径；
4. 文件完整body与source-preparation里实际source_result相等；
5. 已刊R535 adapter10892B/1c99623e2cd63d0a4700011c96e5054645cf7dd8ee5cf3357f0c77d1727026db真实存在，随后才加载。

接着在这一个owner_scope调用已刊install_owner_compiler。该adapter完整核原CPP/ORIGINAL_CPP/TRACE_CPP与原PINS、实际header和两个新include，验证compile_owner与main共享这一个真实global namespace。它只把声明的原compile_owner函数view装入该scope；原main随后调用到的正是该函数，不是一个未被使用的旁路helper。

原persistent main、solve、line search和fresh replay代码不换。原owner原始source字节仍在且有独立身份；新的实际compiler函数、实际include及header另有完整记录。旧“整个frozen prefix同字”旗明确false，不能靠原source文件还在来冒执行体未变。

## 6. 条件算术与程序选择保持

设一次原root的固定输入为实际p、state、g，某次root_evaluate的变量为实际L。R535只在该root的自动局部对象中缓存原固定momentum/pt/P/Pt；U系数只在该次evaluation内形成。资格检查覆盖所共享的全部实际字词；不合资格时执行原表达式，不跨root、state、L、H或run共享。

在R535列明的完整有限原路径、原Q算术/原编译选项和无资源中断条件下，共享项与原重新形成项有相同输入、相同表达式和原j次序，因此逐字相同。P/Pt的完整角点累加次序保；U系数与原sin乘法和U累加仍按所有j进行。Lv、D/S/A、root quadrature、残差、root矩阵、SPD、RHS及RK结构不减项，不省任何模式、角点、列或mean。

由一次原evaluation的输出字相同，可按原30次root Newton/20次root line trial的实际调用序列归纳；每个数值比较见到同一词，完整原root的选择保持。再沿原RHS/RK、全部576 stage和原native32方向×10 trial归纳，得到同一完整输入且双方都沿完整有限路径返回时，原owner数值词及原数值决定保持。原R522和R515局部条件分别仍由其已刊证明承担，本节未改变它们的输出source。

本命题不把时间行为纳入归纳：完整P/Pt的预形成可能在原早期domain拒绝前先做额外工作，有限资格判断、分配、复制和统计也有成本；时间/内存中断地址可能改变。非有限fallback不承诺NaN payload，sticky floating exception flags未被当作原数值输出。程序的资源错误、来源错误或未执行后缀均不可据此变成数学拒绝。

## 7. 原全部非线性门和资源合同

原M112/N2048、depth576、577×224 owner state、226局部状态、全224方向、338×112响应及两mean保留。当前H的完整J/R273仍重新形成，不用旧H/J/state补父；原fresh replay、所有FD组/层、BC、physical RMS、domain、merit、fullDN及final same-H fresh J/audit都由原消费者决定。

| 合同 | 原值 |
|---|---|
| 总科学钟 | 19200秒，一次建立 |
| owner / fresh replay reserve | 6000 /1200秒 |
| stage / boundary / endpoint / audit | 8000 /600 /600 /1800秒 |
| readback/cleanup reserve | 120秒 |
| 原native iterations / trials / tolerance | 32 /10 /2e-9 |
| 原root Newton / line trials | 30 /20 |
| 外层迭代 / prefix inner trials | 8 /17 |
| RMS / boundary / FD相对阈值 | 1e-6 /1e-11 /5e-5 |
| 原Node heap / native threads | 6144MiB /4 |
| 启动free /运行free资源停 | 68719476736 /2147483648 bytes |
| 原job /science step | 350 /320分钟 |

输入恢复与source准备沿原合同在总科学钟之前；原runner在规则同步和首factory前只建一次钟。compiler安装在实际owner流程内，原g++过程、原编译时限和PGID仍沿R535接点保留。新H、root、trial、源准备receipt或缓存资格都不能重新开科学钟。

本请求仅修正一个原request的说明文字output_jets_order为实际slope112、second112、meanSlopeCorrection1、meanSecondCorrection1、height112。生成器对整个原scientific_contract逐项比较，只允许这一明确old/new说明字段；所有形状、索引和数学值不变，旧221/225请求不追改。

## 8. 真正五原物理source目录

原225 physical packet给出的sourceReceipts来自完整HERE basename列表，原ddbe物理binder却在original_source_root下逐item查文件并要求五个ORIGINAL_PHYSICAL。完整source map存在，不意味着另一个root里有这些文件。

新current_call在同call建立physical-source-inputs：原ac2f core、2b96 physical jets、36e4 actual metric、b12f cusp、206d slope五件均从原实际恢复路径读出，核完整SHA，独占写同字副本并再核bytes/SHA。完整原路径、实际副本、当前call、complete/partial保在physical-source-input-binding.json。

原writeNativeFinal128PhysicalPacket的sourceReceipts只用于校验和来源binding，不参与二进制数值chunk生成。因此改成五个真实副本receipt不改变同一dn/参数下的packet数值运算；binding文字和SHA如实是新的。完整session/snapshot/所有caller source及原函数身份仍分别绑定，没有把全361来源缩成五项。

真实runPipeline("solve-response",ctx,fields)通过最后的fields把original_source_root设成该目录；原pipeline→owner→物理component才真实读到它。若复制失败，部分manifest保留并沿原错误传播，不能先写owner或packet成功。这一源路径修复不混入R534模型、投影或deferred hook。

## 9. 必要reader确实消费新统计与来源

原Reader.evaluation没有选root_statistics，本节在全部旧字段之后按实际存在性加入完整RootStats；原initial/trial/current/final与真实fresh-replay记录均经该接点，额外实际evaluation也带原记录序号。所有原统计成员、新18计数、完整last/last_present、counter scope和实际merge顺序都保留，不补缺值、不从计数反推未返执行。

三个owner-call-procedure新字段先实际置null，之后按真实阶段写source-preparation descriptor、完整source-binding及原compiler installation返回。reader分别保缺键、null和实际字典。owner/summary.json若确有compilation，则读完整原对象及root_finite_word_cache_compilation_source_binding；只在原真正g++0及executable成立时，原R535代码才写compiler_completed=true。reader不代写这个判断。

每call的五物理source manifest也按固定同call路径完整读取；缺文件、JSON null、解析错误、部分五源及完整副本分清。其complete只属源复制，不能授予数值接受。

八个封闭具名catalogue仅用于完整RootStats、cache字典、owner compilation及五类声明的来源记录。完整对象同类型、全键/值、数组次序及±0相等才共享index；NaN不共享。每种表按真实键集合分组，原行index和列常量/完整原值都有明确逆。缺键不能变成null，bool/int/float不混，数值不做舍入或差分编码。具体逆和全部十八字段见完整接口。

此表只还原原选择的metadata，未选数组、缺失文件和科学raw仍不可由SHA恢复。新表头、索引及全部值都计入同一90000B；不能保证任何未来状态都能装下，超限仍70保raw，不分包、不提高原限。

## 10. 真实控制流、错误与清理

workflow独立workflow_dispatch，不设push触发；正式发布后只做一次官方POST，实际head/run再另记。原source生成后真核361项、原Python/Node语法检查只在Actions进行，原输入恢复、原rules runner、原full112科学、always两个必要scope、report和cleanup都已接真实新basename/哈希/schema/frame。

源准备成功不等于compile；安装成功不等于g++返回；g++返回不等于root或native接受；完整必要读回不等于科学成功。它们的实际字段分别保留。没有额外benchmark、短跑、shadow比较、全解析J或模型误差前门。

科学失败/partial的完整必要范围若已真实返回、原quiet及全部原cleanup条件成立，可按原合同删除本namespace。缺必要、90000B超限、未知owner或quiet未证则保raw。workflow在必要文件缺失或后续运输身份校验失败时显式清除同step此前的complete输出，避免一个过早true授权清理；这不改变科学接受条件。

原正在运行的225、224、227及其它支线均不被本请求改写。没有旧已删接受父可继续；本请求仍从原明确初始输入真实重做。

## 11. 完整组合命题

**命题。** 对本文全部实际源和原输入保持完整身份、source准备及真实compiler安装/编译按上述控制流发生的请求，在R535/R522/R515各自列明的有限完整路径条件内，新的原128链向原fullDN提供与原表达式一致的实际owner值及原完整后处理输出，并保留原全部非线性接受条件；其必要reader完整表达规定范围内实际返回的统计、来源、错误和未付状态。

**证明。** 第2–5节给实际唯一caller及compiler接点，不依赖未被调用的helper。第6节由原表达式、原累加次序和实际调用归纳给条件词保持；第7节保全部输入、数值门与原资源政策。第8节给真实物理源路径，不动数值packet。第9节对八种声明metadata表逐索引给逆，故每一原上下文还原全部选定原值；原科学消费者不读取这些表改变接受。第10节给真实workflow/必要/quiet和清理控制流。组合即得命题。证毕。

命题没有预付时间改善、原6000秒内收敛、全部576组件完成、未来90K容量、FD通过或fullDN接受。R537必须由实际新226终态证据填写。闭曲面、同一g、全t C²、全域metric、held/reach/E(3)及固定目标精化仍按课题README另付，本文不把有限程序条件当课题完成。

## 12. 原依据

- [R535完整有限字词及真实compiler证明](R535-original128-local-finite-root-words-and-real-compiler-hook.md)及其source plan/adapter/header：本节实际执行的唯一数值改动。
- [R527完整225来源组合](R527-live128-paired-stage-and-radial-cache-complete-chain.md)、原225 request/plan：本节所有caller的完整文字祖先。
- [R522完整配对dyadic矩阵](R522-complete-dyadic-matrix-pairs-and-shared-integer-plane-loads.md)与[R515物理局部径向词](R515-physical128-local-radial-mode-word-sharing.md)：两种原后置数学范围。
- [R534物理来源路径责任](R534-current-owner128-same-DN-complete64-model-and-original-gates.md)第534.10节；本请求只使用该最小路径子件，不使用其projected64模型。
- 原geometry_20261115_native_persistent128.py、geometry_20261115_native_final128_packet.mjs和geometry_20261115_native_final128_components.py：实际main/compile/replay与物理来源consumer，完整source身份在本plan及冻结请求。
