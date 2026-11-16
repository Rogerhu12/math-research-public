# R527：同一当前 H 的 live128 配对 stage 与局部径向缓存完整调用链

作者：ChatGPT（AI 助手）  
日期：2026-11-16

**可信度：已证明的有限来源组合与条件保持命题。** 本文给出 request225 的实际源码组成、算术适用范围和原消费者保持条件。没有在本地执行科学程序、导入科学模块、编译、AST 检查、fixture 或 benchmark；没有本次 native、FD、fullDN 接受或耗时结果。实际225结果另由 R528 记录。

## 1. 本条支付的具体缺口

[R522](R522-complete-dyadic-matrix-pairs-and-shared-integer-plane-loads.md) 的完整 dyadic 配对点积已经接到三个实际 source views：operator、stage 和 final-components。R522 的 final-components 同时保留 [R515](R515-physical128-local-radial-mode-word-sharing.md) 的物理径向词缓存。但是仅生成这三个文件，原 live128 owner、assembly、protocol、fullDN 和 necessary reader 不会自动接受新的来源 tuple。

[R518](R518-live128-radial-cache-complete-source-composition.md) 已给出十二个真实调用层的径向缓存来源组合。本条沿其公开有限替换计划，保留原221全部336项祖先，另形成当前225的11个调用源，并实际调用原R522生成器写出其3个未改输出。新调用链真实使用配对 stage、缓存物理组件和原完整末门。

原221请求、原运行及其输出均不改。225采用新的请求 schema、namespace、client policy 和必要读回帧。原221的数值输入、所有阈值、资源上限及原320分钟科学时钟不重定标，不将一个源码标签当成已经发生的运行。

## 2. 固定祖先与完整有限集合

原221静态请求为：

- `public-live128-scoped-original-full112-FD-fullDN-request.json`，54884 B；
- SHA256 `0fa9fe29153913252fd569cb2b99711c85b0afe72d8bc576adf629bd3e3f789e`；
- 公开来源 `8b352f90b97f7c340a2fbebbb11c19080d9a5e08`。

本条引用的三个已发表源码族分别是 R515 `02320c3a035d03c31c4e1fada1d19d9661bf7179`、R518 `bfe02a5249db7c01665fef163034d436d66ebdbd`、R522 `3514dfb8333ec3d42cf62ba6165c0f799dd3bf6f`。本条实际输入的三个完整 JSON 计划为：

| 计划 | 字节数 | SHA256 |
|---|---:|---|
| R515物理缓存计划 | 8662 | 5950052fac0d9c23e96f29421c03df79f4748828b2d7a6e9a4ed7f40bd090666 |
| R518十二层计划 | 48391 | 4f2097053bddff0bf07a18f09ffa846bd64eb2fa6dd3d9707ab7f24f3ef62f6b |
| R522三层配对计划 | 16347 | 724e46e0d70aefd70309e03d77d4719666058e56001c7a78f7544bada76b9ce7 |

原336项按原basename和完整SHA逐项保留。新增公开文件只有R515缓存头、R515 adapter、R518生成器、R522配对头、R522生成器和本条生成器，共6项。R518生成器作为完整已发表来源被绑定；其旧12个输出不要求是Git文件，也不在本次目录落盘或执行。

因此本次明确集合是

$$
336+6=342\quad\hbox{公开文件},\qquad
3+11=14\quad\hbox{实际生成文件},\qquad
342+14=356.
\tag{527.1}
$$

三个JSON计划在独立metadata依赖中读核，不伪装成Python/C++代码。原336中本来包含的 `source-dependencies.json` 仍按原metadata身份保留。式(527.1)是明确有限文件集合的大小；不声称算法自动发现了任意未来动态import的传递闭包。实际原callee的source检查、恢复来源和路径检查继续执行。

## 3. 真实生成、目录与错误前缀

生成器要求实际公开Actions仓库、当前 checkout HEAD 等于本次 `GITHUB_SHA`，并要求自己的 `HERE` 恰为

`GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations`。

本条静态225请求与完整55391 B计划先按完整字节绑定。原221请求以及所有342个公开文件逐件实读；三个已发表计划分别核字节数和SHA。对每一个R518输出，生成器从其真实公开baseline开始，逐个核明确的非空before及count，应用计划after，最后核整个输出字节数和SHA。得到的十二段文本仅为内存祖先。

随后对11个指定祖先再次施行本条计划列出的有限替换，核全部最终输出。每个输出有互异新basename，预先不在真实HERE中，不覆盖任何公开文件。原R522生成器通过其真实CLI运行，输出同一HERE中的三个正式R522文件；源生成回执必须属于本job/run/attempt/source。其3个文件逐件核回R522原字节后，11个新caller才逐件以排他方式写出。

**命题527.1（实际目录与来源）。** 若本条 `prepare` 返回complete，则356个明确文件在实际科学目录中具有请求所列的完整身份；本次14个生成文件是原计划指定的字面结果。原12个R518输出没有冒成已发表文件或科学执行结果。所有新callee的实际 `__file__/HERE` 与原恢复树的实际位置一致。

**证明。** 公开文件由本次实读核定。十二中间文本分别由完整已付baseline与有限替换确定，整个输出身份核回原计划；第二层11个输出亦如此。R522为本次真实子进程且回执属于本次source，三个文件再按整个字节核回。输出basename互异且不与342公开文件冲突，各排他写入同一实际HERE。原路径表达式未被改成虚拟目录；原public_resume恢复树仍由原准备流程真实产生。上述各检查成立后，完整map与请求的356项相等，故结论成立。证毕。

若生成失败，源码准备保已生成的实际文件、当前phase、明确未生成的caller后缀、R522子进程的实际启动/返回信息及原错误。若异常发生在R522输出途中，其原回执中的 `views/not_generated` 保相应范围；外层不补造3个已完成输出。若异常早于正常source receipt，原stdout事件和后续读回error如实记录缺失，不能制造complete。

源码准备不启动科学时钟，不调用科学模块、编译器、数值程序或旧raw恢复。正常Actions原语法检查仍在下一步骤执行，未增加科学对拍或独立验收门。

## 4. 十四个实际输出及真实调用边

三个配对输出保持原R522完整字节：

| 角色 | 字节数 | SHA256 |
|---|---:|---|
| final-components | 33416 | 93ecdd833922f833bdb50a8f264bc5db1913f5ce16dbb0cb4f7fbc7d285070f1 |
| operator | 29617 | 082d5a1fdd900071fb1cc008304c5a4c97bce92b173851bda1514ec1682eb7be |
| stage | 12880 | 49a7e226eadc7748d5d2b3f94119c2e4dd7024348e6878c673e73b1a33db3b55 |

另外11个新caller的完整basename、bytes、SHA均在本条计划中。其实际边为：

| 调用者 | 本条实际变更 | 保持的原责任 |
|---|---|---|
| owner | 私有engineering计划指向R522组件及其schema | persistent128求解、当前H、fresh replay、原资源裁剪 |
| assembly | 绑定实际新owner和R522组件 | 同call完整state/jets/J、投影、双mean与正常response |
| system / QR | 实际call/client和system身份 | 原current576矩阵、原全部行、R273形成与消元 |
| pipeline | 绑定新owner/assembly/system/QR | 当前H与capture同一、原完整调用顺序 |
| current-call / worker | 真实新client/current-call | 原完整协议、原响应正文、原输入验证 |
| client | 新pipeline/owner等真实tuple和新policy | 原原生调用、同H缓存条件、完整返回范围 |
| fullDN | 实际新client及下层来源 | 原非线性外循环、FD、所有旧接受门 |
| owned runtime | 新225请求、namespace、policy、fullDN | 原唯一时钟、原进程登记与静止合同 |
| necessary reader | 两类compiler回执与225帧 | 原trial、FD、fullDN、错误、未访地址和90K限制 |

client原18个lower-source pin保留，并加入8个当前下层view、R515两个公开源和配对operator/stage/kernel三项，共31项明确下层source。fullDN同样保原所有祖先literal keys，当前 `CLIENT_NAME` 则指向真实新client。旧basename仅作祖先时仍保原SHA，不允许把旧名下的内容偷偷替换为新实现。

owner的私有engineering wrapper由原38408 B源码和原工程计划形成，本次完整39152 B / `ea97b5f7abf5842acf2d74907ab361fff1002a7f8a774aefbb2c568eeb33e729`。这里的变化是实际component/来源schema；原求解、fresh replay、四组件、deadline与临时raw合同保留。该wrapper仍在当前call真实生成；不是从旧204/215清理后的hash恢复state。

## 5. 配对点积与缓存在同一组件中的组合

令本次真实stage的有限binary128输入列为 $b,c$，实际左行为 $a$。R522证明新 `dot_pair` 的两个**完整返回**分别等于原R414/R405完整dyadic和最终一次RN113：

$$
\operatorname{pair}(a,b,c)
=
\left(
 \operatorname{RN}_{113}\!\sum_i a_i b_i,\;
 \operatorname{RN}_{113}\!\sum_i a_i c_i
\right).
\tag{527.2}
$$

该命题包括原完整signed significand、指数、抵消、subnormal、ties-to-even与原signed-zero规则。宽指数或原packing条件不满足时，对两输出分别沿原完整dot fallback。原finite checks仍处理非有限结果；不声称NaN payload、失败先后或资源中断的路径逐字相同。

R515缓存的对象是**一次真实 `physical_jets` 调用内**不随角行改变的实际有限径向词。其原依赖field/state/geometry、精度、舍入环境和算式没有改变；只共享已形成的有限词。非有限词仍沿原位置重算原表达式。所有角向项、原累加顺序、原 $C$ 求解和输出仍按原数学形成。不存在跨查询、跨H或跨state的缓存。

**命题527.2（实际两接点不相互替代）。** 在命题527.1的来源条件下，真正进入stage编译时调用R522的配对stage源；真正进入boundary高度forcing、endpoint或独立audit的物理编译时调用R515原adapter。每个实际编译都由原组件的process管理执行一次最终argv，两类变化没有互相覆盖，亦不把仅准备过的中间CPP冒成已编译source。

**证明。** 正式R522组件33416/93ec从R515已给组件中间文本形成，其physical qualifier和原非stage委托保持。它仅在原stage编译位置用配对stage/operator/kernel组合，并把实际编译来源写到 `paired-digit-source-binding.json`；其他编译仍进入原R515 adapter。该adapter先由原工厂形成R493 CPP，再按原R515有限替换形成最终物理CPP，原process只执行最后actual argv。新owner绑定的COMPONENTS与实际93ec schema一致，assembly和pipeline逐层接受同一真实tuple，故两条编译分支均从实际owner可达。证毕。

**命题527.3（有限算术保持范围）。** 固定相同的实际完整输入、原精度/舍入环境，且对应完整输出按原资源合同返回时，本条对stage的新增数值变化受式(527.2)约束，对physical的新增数值变化受R515调用内有限字共享命题约束。原名义因子/finite-trace derivative的限制、原mixed-J范围及IEEE整体导数未付部分不因此改变。

**证明。** 除两已发表数学接点外，本条11caller差异限来源名/SHA/schema、明确policy/namespace、编译来源的metadata读取及固定请求接线。每个完成的配对输出由R522保证原完整dot字；每个共享物理词由R515保证原调用内的相同有限字。其余原计算按同样的数据边继续。因此局部命题可组合。资源poll和执行顺序可能改变，实际完成前缀、耗时或接受序列不能从该条件归纳预先推出。证毕。

这不是相对于R305旧顺序浮点图的整体逐字等价，也不是原精确Frenet函数或IEEE roundmap的全导数证明。没有速度改善测量；不能由减少源码中的重复载入预填walltime收益。

## 6. 同一 H、真实初猜与完整状态责任

本次仍从原actual63的真实prefix warm/status、原accepted/config/ready文件和原78公开恢复树重新形成原有限问题。actual91尾部字只作原授权初猜；不是prefix状态，也不带来旧native成功。固定SHA仅证明原输入字节来源，不能复生已删除的任何旧实际state/J。

每个当前H仍由原current-call执行完整original64 withJ capture、原R273全部576段/224方向，再交同call persistent128 owner，原32次迭代和每次10档试步。实际返回的末128state经独立fresh replay，然后同一状态形成stage、boundary、mixed endpoint和audit。原响应组装只接受这些当前call来源；原同H缓存仅在当前真实call已返回后按原规则允许。

下列尺寸必须区分：

| 对象 | 原完整责任 |
|---|---|
| 每个shooting node保存的物理状态 | 224项 |
| 每个局部RK状态 | 226项，包含两mean |
| 完整stage rectangle | 576段 × 224方向 |
| 径向状态资料 | 577个node，不能改称577项局部状态 |
| 原物理jet输出 | 112 height + 1 mean + 112 slope + 1 mean + 112 second = 338 |
| 原完整物理J | 338 × 112，原mixed导数合同 |

原投影仍是明确整数RN-even binary128→binary64，signed zero保留；原hex residual/mean以及normal-response的JSON文本转发保持。worker不经一次Node parse/stringify改写响应字值。可选预测子失败不新增接受门，旧状态也不冒新的当前H解。

## 7. 原消费者、门和唯一时钟

原fullDN入口的有限问题没有换成连续C或新的闭曲面目标。112/224、576段、338输出、全部原mean、原输入维数和实际FD/fullDN调用均保留。原合同中的数值门为：

- owner原32×10，原solve tolerance `2e-9`；
- FD两组，每组10方向，原3个step层、2个Richardson层、相对阈值 `5e-5`，所有原适用contraction；
- prefix原17档，RMS `1e-6`、boundary `1e-11`；
- 原所有物理RMS/domain和最终同H fresh audit。

组件complete、响应返回、FD通过、fullDN accepted是不同真实层次。没有新“全338解析J”门，也不删除原mixed-J门。必要读回来源相等只记事实，不另作为数值通过标准。

科学时钟仍19200秒，最末120秒保留原readback/cleanup；job350分钟、science step320分钟。时钟在原输入恢复完成后、规则同步和第一个native factory之前建立，所有当前H、FD及fullDN共享。每次call不能重开19200秒。owner6000、replay1200、stage8000、boundary600、endpoint600、audit1800等仅为原总钟剩余内裁剪的上限，不是可相加的新时间总额，也不保证一轮完成。

原64GiB启动盘和2GiB停止保留、线程/内存/最多未缓存call声明保持。准备源码和普通语法检查不产生第二个科学钟。规则同步仍在原独立sparse mirror执行；它明确不修改科学checkout，故不能把规则记录的main前进误说成当前科学源已替换。

## 8. 两类编译回执的必要读回

新reader保持原scientific scope，并真正读取以下实际文件；即使component summary尚未返回，也先报告该文件存在或缺失。

1. stage：`owner/final-components/stages/compile/paired-digit-source-binding.json`；
2. boundary：`owner/final-components/boundary/forcing-compiler/compile/physical-radial-mode-cache-source-binding.json`；
3. endpoint、audit：各自 `owner/final-components/<name>/compile/physical-radial-mode-cache-source-binding.json`。

第一类保存整个原 `paired_digit_compile_source_binding` 一次。它只含明确源码、argv、source receipt和范围标志，不含state、J、科学ledger或数值见证数组。返回的lifecycle行保原索引和实际进程字段，并记录其binding与文件的完整canonical相等结果；该布尔不是额外gate。

第二类沿R518保原完整binding文件身份，选择其actual/prepared source、header复制、R515范围和返回进程。其他原binding正文仍由本job文件身份承载，不冒称根端全树逐值阅读。requested compile.command与qualifier后的actual argv分责保持。

仅有source binding不证明编译已启动或成功。没有返回process行，只证明该返回集合为空；可能编译未起、仍未返回或此前已中断，必须与原lifecycle/error/quiet一起解释。新reader不凭source identity补造compiler成功。

## 9. 有限必要body、进程静止与清理

两个不同的必要对象分别是：

- 新source-preparation metadata：14输出、12文本祖先身份、真实R522子过程、phase、原错误和未生成范围；
- 原完整科学necessary：实际call/trial、FD、各组件完成或未访、fullDN返回、两个mean、原错误与新增compiler receipt选择。

它们是两个不同语义scope；不把一个超限科学body拆成两份。每个body独立90000 B上限，超限明确70，完整选中对象留本job且scope未完整返回，不分段、不改成全树字典编码。未来的实际body大小未知，本文不承诺通过容量。

原R508进程判断保持：只把真实登记pid/startticks/uid/pgid/sid、实际后代或可读namespace来源所确定的进程纳入责任；真实own或可疑own不可读仍unknown并阻止读删。不同的同uid进程不因环境不可读自动被判own。只有原登记组可被终止。quiet不证，不读科学raw也不清namespace。

最终删除需要科学必要scope完整、新source必要scope完整，以及原同source/run/request所有权和真实quiet。科学失败但其完整必要scope已读时可以按原规则清理；读回失败、超限、真实own未知或source读取未完则明确skip。source准备目录在科学namespace之外，仅是本job临时metadata，未新增raw上传或Git归档。

## 10. 可复现交付与尚未支付

本条生成器22915 B / `b30d418965454b63d5a0e8f6bc50277e38849e959e24ec92552bc722ec83a3ce`，完整计划55391 B / `6e8109e64bafb6e78428298ccc25a5b4d71df29c0b224b0ea20076da006dd1c6`，给出11个完整before/after/count及全部输出身份；R522三输出按其原计划真实生成。展开源和完整diff只作临时文本交接，不入Git。

独立225请求64734 B / `42fe3eff48338d540707c690d6aadd0cfdfeaa278a1145b1db885bea9df37285`，workflow18518 B / `5ed7a2c3fd2fdab0d2fe02aeb050a07e3bfe8f3344b23ba3bd16f7573b274d53`。workflow同时声明push与workflow_dispatch；真正source/run/head只由实际公开发布和官方启动产生，不写进本证明作预定事实。

[完整调用接口](../notes/2026-11-16-request225-live128-paired-cache-original-full112-interface.md)给出CLI、目录、所有14输出、旧输入、各scope帧和错误口径。本条支付的是两已付数学接点在当前H完整调用链中的真实来源组合，以及上述原合同保持条件。R528仍须记录真实执行前缀、算术/域/FD/fullDN结果、原资源停止和实际清理；本文不替代它，也不宣称README的完整闭面目标已完成。
