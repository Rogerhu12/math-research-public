# R565 — request237：完整整数首乘积、真实当前 owner 与原完整投影模型入口

作者：ChatGPT（AI 协作者 /root/amplitude）  
日期：2026-11-16（UTC）

**可信度：已证明，限本文明确的有限字算术、来源组合和控制流条件命题；request237 的实际编译、求解、replay、完整模型、FD/fullDN、必要读回及清理尚未执行。** 本文不以 source preparation、完整源码集合、统计计数或 GitHub job 状态替代原数值接受。实际结果预留 R566，须另据唯一官方终态报告。

## 565.1 本次对象和准确继承边界

本次从正式 request236 来源头 e6d389dfe1f79669f5b616497dc91bf92a70637d 派生独立入口。原236的417项完整源映射逐值保留，原输入、参数、19200秒总钟、所有资源上限、完整列和原接受函数不变。236的运行结果不被读取为新初值、已接受父、旧J或replay；旧236不被追改。

本次唯一新增数值实现是 R564：在原 root residual、root Gram 和 primal flux 三处，实际第一乘积满足严格字资格时，以完整113×53位整数乘积和一次最近偶数舍入形成原RN128字；其余情况实际执行原Q乘法。这个字再进入原R561第二乘法选择器。R550同root已接受完整RootEval的下一迭代复用、R535本地有限词共享、全部原试步与方向算术仍保留。

这里必须区分两个事实：

- 原第一乘积的 RN128 结果字与原求和次序保留。
- 快捷分支**没有执行原第一条Q乘法指令**。

当前request、plan、owner、reader和实际compiler返回均据此区分。原R561祖先仍按原字保存，它关于自己的首乘法描述不被追改；当前R565不把祖先的指令事实误套到新分支。不声明浮点异常标志等价，不把所有输入有限误说成所有中间结果有限。

本次仍是原有限prefix/full112问题。没有换成准确连续C族，没有构造或证明完整闭面，也没有增加“全338解析J”条件。R534的当前128值与once-RN64完整线性模型是原已声明的两个不同对象，原诚实guard沿用。

## 565.2 可独立审查的完整文件身份

下表均为完整UTF-8文件身份；除workflow外，路径相对本题。生成器、计划、request和本文按普通Git文本发布；展开caller和C++ include不另存入Git。

| 当前文件 | bytes | SHA256 |
|---|---:|---|
| computations/root_20261116_live128_lifted_product_projected_source_views.py | 38098 | ee6bad1b586c77e94e54714ecff05a980ce9ad11bc50658a55583fd372ddc6f2 |
| notes/r565-live128-lifted-product-projected-model-complete-source-plan.json | 71039 | 6d6ff7d6f95f83e809fc0e260765a47185011ca86e2cc62c0a4dcf544f9789f1 |
| computations/public-live128-root-lifted-product-projected-model-original-full112-FD-fullDN-request.json | 96574 | fff570a800581ed22887734b467ad1b368cdd8d17d9df04ba49ad1e05c6bf605 |
| .github/workflows/visible-larger-public-live128-root-lifted-product-projected-model-original-fullDN.yml | 23955 | 0059a6c510d453b63f05fe9fe49ea574a0ad14cc5d1d2842949c82e4a28003fb |

正式236四来源为：

| 角色 | bytes | SHA256 |
|---|---:|---|
| root_20261116_live128_dyadic_projected_source_views.py | 37603 | 0f984347d801b3b8132b7814494b3f883f72ef1bd73d00aa15d01b767c2de85c |
| notes/r562-live128-dyadic-projected-model-complete-source-plan.json | 64999 | a72e2d5a225a977c6eec7d3f7d65066b102a405b1362af5b855d38495b8c4780 |
| public-live128-root-dyadic-projected-model-original-full112-FD-fullDN-request.json | 97937 | 299cf5532e510c3629354347d1ba03aa57135077a1530b605867b0f71e08cb45 |
| .github/workflows/visible-larger-public-live128-root-dyadic-projected-model-original-fullDN.yml | 23459 | b683e42765e1ca758ddf8d189fbb501057f733e5dcc920594a9e9878ea082b66 |

本次直接使用R564三个完整执行来源：

| 文件（相对本题） | bytes | SHA256 |
|---|---:|---|
| computations/root_20261116_exact_lifted_factor_product.hpp | 10146 | bb4dfb08db7c4593afd93addb804a20876e0bb1facb1bc7e8a7e3f9aaeb40cc1 |
| computations/root_20261116_exact_lifted_factor_product.py | 19738 | 2f2cf734f2012d64ea5d19c1e8bed0ee95918b8e24fab0d4f8766ae0e174c0de |
| notes/R564-exact-lifted-factor-product-complete-source-plan.json | 13514 | cd4c90cbfc9e48acdd06a692885121627355df477955104981713d248cafca4a |

R564完整算术与安装证明为 results/R564-exact-binary64-factor-products-and-complete-integer-rounding.md，27336 B / 22a7dea15cbf1f9ed287aa90d76f37a7d23ec5ebbb1d33d7eed277e53b926f10。本文采用这组完整冻结字节；其实际公开登记由root在本入口正式派发前完成，不把detached source commit写成已经发布的main。

原祖先计划亦逐件绑定：

| 计划 | bytes | SHA256 |
|---|---:|---|
| R561-normal-dyadic-average-complete-source-plan.json | 13708 | 5667d987ea5b7387bb0c4f6c61d86cd9ea94035299da91d3c7889fb1cde5f5a7 |
| R550-accepted-root-evaluation-complete-source-plan.json | 12303 | 14b5c02071359276be2988dc273d6864df3d61e728df10df5b1bddc498134457 |
| R535-native-root-finite-words-complete-source-plan.json | 10232 | f3b7900f0e670441404c707dce2144241ee9b72581c5999dd8ce95b91764607b |

R561 adapter为18526 B / 9d954a23b1a8991c4aff38c1ffb6879229552cc9894ba70e7c3fb485fa928082，R550 adapter为16634 B / 66c2ff0d0b29c41cef00cc6a77764e4e168d2885c52b3f56c2abd961fad8f97c。19738 B的R564 adapter与这些祖先是不同文件，不能互换身份。

## 565.3 三处首乘积的完整字条件与证明

本节是R564源级定理在实际三调用点的应用，完整边界见上述R564正文§564.2–6。Q仍为原GNU little-endian IEEE binary128：16字节、113位有效数、15位指数；unsigned __int128与原byte布局按实际声明检查。helper每次读取真实fegetround，要求FE_TONEAREST；不修改舍入模式。资格不符是实现回退，不是新的科学拒绝门。

原三个右因子是实际packet/table里的cs[i]、gc[k]、sn[j]，不是重新生成的理想三角函数。每次仍读取实际左因子quad、value、f。非有限输入先处理为原乘法回退，故不会把零乘无穷误当零。两个输入有限之后，任一实际字为带符号零时，符号异或形成准确乘积零；正零与负零不合并。

对于两个非零normal字，令左significand为A、右53位整数为B：

$$
A=2^{112}+f_a,\qquad
B=(2^{112}+f_b)/2^{60}.
$$

右fraction最低60位须实际全零，而非仅凭“来自binary64”的来源名假定。于是

$$
2^{112}\le A<2^{113},\quad
2^{52}\le B<2^{53},\quad
ab=(-1)^{s_a\oplus s_b}AB\,2^{e_a+e_b-2\cdot16383-164}.
$$

原binary64 subnormal准确提升到更宽Q后也可能属于这个normal/53位域；本实现依然只根据当次Q字资格选支，不对输入名补数值性质。

把A分成低64位与余下高49位：

$$
p_0=A_{\rm lo}B,\qquad
L=p_0\bmod2^{64},\qquad
H=A_{\rm hi}B+\lfloor p_0/2^{64}\rfloor.
$$

则完整整数积为P=H·2^64+L。p0小于2^117，H小于2^102，均在实际unsigned __int128中容纳；没有截掉低尾、采用有符号溢出或浮点近似。P的最高位只能为164或165，令额外位为b∈{0,1}，需丢弃d=52+b位。

因为d<64，所有被舍弃的位都在L的低d位中：

$$
S=(H\ll(64-d))\;|\;(L\gg d),\qquad
r=L\bmod2^d.
$$

比较完整r与2^(d−1)，小于半间隔不进位，大于半间隔进位，正好一半仅当S最低位为1时进位。这是原最近偶数规则，没有先舍入一部分再舍入另一部分。规格化输出的带偏置指数为e_a+e_b−16383+b；进位到下一binade再准确加1。只有规格化前后都在normal域内才快捷返回。边界、subnormal、overflow或不合资格的因子实际回到原left*factor；代码不自行猜测原结果。

**命题1（首乘积字）。** 在所声明ABI、当次实际舍入模式和资格条件下，每个快捷返回的Q字与原乘法RN128字相同，包括有限输入的带符号零；其它输入执行原乘法。证明由完整P、全部余数和原偶数规则及normal范围检查直接得到。这个命题不声称NaN载荷、异常标志或不同运行的资源前沿相同。

形成的原首乘积字继续交给未改R561第二乘法选择器：N确为正2的幂、原实际inverse字准确、首积为±0或缩放后仍normal时做原准确dyadic位操作，否则原product*inverse。没有把inverse预乘进factor，也没有移动第二乘法或交换求和次序。

三个实际调用点保原全部角n和列索引、完整原 += 与每项顺序。对任何共同到达的完整累加前缀，前一sum相同、下一输入项相同，原Q加法也相同。相同字进入原root/Gram/flux和其后未改的试步判断；该归纳不把实际时钟导致的不同停点当相同执行。原trace方向正文全保，只改include来源、当前primal调用的统计传递和新统计序列化。

## 565.4 明确的432项来源组成

本次集合是：

| 来源集合 | public | generated | total |
|---|---:|---:|---:|
| 原236全部来源 | 354 | 63 | 417 |
| R564 header与adapter | 2 | 0 | 2 |
| R564两个include | 0 | 2 | 2 |
| 当前独立generator | 1 | 0 | 1 |
| 当前十个caller view | 0 | 10 | 10 |
| 本次真实并集 | 357 | 75 | 432 |

这里的数目表示实际明确source map的并集，不冒成任意动态import闭包的普遍定理。每个旧417名字和完整SHA原值都保留；旧生成源仍按原计划真实生成，不能把它们误列为仓库里已有的公共文件。原R562和更早caller作为来源祖先留存，当前科学调用的是下表十个独立view。

当前R565计划含61个逐字replacement，全部before/after/count及完整基线、输出bytes/SHA在该普通JSON中。Actions在实际原computations目录生成；先核公开generator及原输入来源，运行真实source-only祖先，再对每个明确view按顺序替换，并核完整输出和逆向恢复。原源文件不覆盖。新输出已存在时只能接受完整同字，不能给不同文件贴旧SHA。

| 当前角色 | 实际basename | bytes | SHA256 |
|---|---|---:|---|
| owner | geometry_20261116_live128_lifted_product_projected_same_call_owner.py | 26325 | b92065dd41d918046bd04c10ec4edec3e118090347691b91f0ee779c903bc8dd |
| system | exact_20261116_live128_lifted_product_projected_current576_system.py | 29071 | f2f9db0189412c8dc2f75cda57627a03137dbf83d863d53033e0e2de40fcb346 |
| qr | exact_20261116_live128_lifted_product_projected_current576_chain_qr.py | 21855 | 579977e8b794eb21c314465e0d74b0157769f77d13918a6f631d9c694ff604aa |
| pipeline | geometry_20261116_live128_lifted_product_projected_call_pipeline.py | 43265 | d1b36754b39c168e3421d7ce804fd9b25e04583cf4b94ef3d907c127a83e077d |
| call | geometry_20261116_live128_lifted_product_projected_current_call.mjs | 45455 | 504a7314bb0242455dae2fdb9853dee135387ab9459ed7e72b6d710c46757573 |
| worker | geometry_20261116_live128_lifted_product_projected_worker.mjs | 8321 | 57379bef7abd1483df1a10ff1ad1ab7256ccc9a2ae1f4d0fb548bc66dbc304af |
| client | geometry_20261116_live128_lifted_product_projected_tail_client.py | 39043 | c2bd41b83f178bce138370433c5790b88233eeafff326ff7684a5e27350677db |
| fulldn | geometry_20261116_live128_lifted_product_projected_original_full_dn.py | 44874 | 1d5299ed8cc90de02ca0dbd1f2ca1358cbc421e6b1ddaea74534c8831788f325 |
| runner | geometry_20261116_live128_lifted_product_projected_owned_run.py | 39404 | d61c81c14532bd5be2dc5a5f718196be1be922082a419e06dcc2c5463574b1ff |
| reader | root_20261116_live128_lifted_product_projected_necessary.py | 62562 | 9d3b25b88f31b7d1ddc383d566b13a10d845759ab7887aa2946b0b7d578d1d68 |

三个R534实际科学消费者保持原文件、完整原字节：

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| boundary | geometry_20261116_live128_projected_model_boundary128.cpp | 12844 | 0364ea5cc8173f40dbe7a375fbca798987dcd75b4f67b90470c638352ae8ecb9 |
| components | geometry_20261116_live128_projected_model_final_components.py | 38561 | c4b3a5eb05fc4d4ae6767c2c08f75ea38a5a5538366fcd3264ff59cec17bb04e |
| assembly | geometry_20261116_live128_projected_model_response_assembly.py | 33269 | 863790de6c0c2020d79150ac99134b2a8ee74592cc42669127ca7df296a0f21a |

R564两件include为：

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| primal | root_20261116_exact_lifted_factor_product_primal128.cpp | 26887 | 5a13551c0d68f3e12577d2da9c096bfb340a27787ac5bf3b658cf6fb9973e798 |
| trace | root_20261116_exact_lifted_factor_product_trace128.cpp | 36019 | ed8c674215ffe1f94a65010d115447804d07812b7f5f70c387b080f56c140447 |

primal相对R561仅七处完整literal，trace三处；真实callers另有自己的来源/当前schema/读回变换。所有完整替换表已随原plan保留，不依赖未公开的私库，也不靠sys.path加入未绑定目录来补来源。

## 565.5 source preparation与原scope一次安装

当前HERE为实际GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations。所有真实loader、owner和compile参数使用同一目录，不能把生成源放到另处而保旧computations标签。source准备目录为RUNNER_TEMP/request237-source-preparation，并保同次四环境键：GITHUB_REPOSITORY、GITHUB_RUN_ID、GITHUB_RUN_ATTEMPT、GITHUB_SHA。

实际prepare按此顺序执行：

1. 核完整236 request、R562 generator/plan、R534 core plan与当前计划，真调用原R562 source-only prepare，重生并核原417来源。
2. 核原source receipt、实际child返回与当前HERE，不把其源码准备等同编译或求解。
3. 真调用R564 adapter，传当前R564和完整R561/R550/R535四份计划。R564内部真实R561→R550→R535准备；三个祖先均source-only，没有安装任何owner compiler hook。
4. 读取并核实际R564/source-binding.json，保完整source_result、R561/R550/R535祖先对象、四headers、两个当前include及所有原地址/错误。
5. 按本次完整literal plan生成十caller，完整核432公开/生成来源，写source-views.json及source-map.json。只有真实全范围满足原来源条件才置prepare.complete。

R564子进程stdout自身若遇90KB超限，可以返回70并留下完整binding文件；当前source record仍保该真实事实与文件身份。它不会因此自动成为owner可用的成功准备。本次owner安装明确要求R564_child.returned=true且actual_exit=0、outer preparation.complete=true；任何失败依原范围报告，本文不预称body必fit。

实际每个current owner原globals形成后、首次main编译之前调用当前install_exact_lifted_factor_product。它核当前owner完整identity在本次prepared generated列表中，真实HERE一致、独占源目录非symlink、四run键一致。它从固定当前R564/source-binding.json读取完整对象，核同child.source_result，再装实际19738字节adapter。

实际owner record保三项原固定键：

- root_finite_word_cache_source_preparation：本次source-views.json的真实descriptor。
- root_finite_word_cache_source_binding：actual_file与完整actual_binding。
- root_finite_word_cache_compiler_installation：真实R564 install_owner_compiler返回。

这三个键的历史命名保持原消费者合同，不表示当前只执行R535。它们初始存在且为null时与缺失严格区分。

安装器要求原scope中R564/R561/R550/R535 hook标记均尚不存在；只在真实原owner_scope里一次直装R564，不能先装R561或R550再叠R564。原main与compile_owner实际__globals__必须同一scope；原persistent main、solve、replay及limits正文不变。旧owner源码43371 B / 767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322的完整identity在plan中保存，原persistent CPP仍22364 B / 7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd。

完整原compile函数3860 B / be019045058f4616f98b07e19c0d8d3901e979ce2b1ba7d4259c65fcae4ae46d，当前明确derived函数6909 B / 7c332e958280eaf84d18dbf60ab545c2cb6fbbb1f5eb8b533528415e647e83dd。当前函数的整个old/new、唯一anchor次数、正向和逆向完整SHA由R564 plan负责。原main随后才实际g++，使用四个真实header和当前include。

actual compilation.root_finite_word_cache_compilation_source_binding来自这个真正编译接点。source-only prepare的compiler_completed=false和安装返回的actual_compile_not_yet_called=true均保持；新reader不以来源完整或安装成功补“已编译”。失败compile、实际stderr、未开始owner或缺失组件仍分别保留。

## 565.6 当前128状态、完整64模型与原诚实guard

原R534 defer仍在真实owner/replay之后按原控制流调用。每次当前物理H、当前packet和当前state都重新经过原完整source/input binding，actual owner128最终状态与fresh128 replay继续是值和接受责任的来源。

原R534模型仍把同一次真实owner的完整577×224状态做一次RN64投影，再由**同一个已加载DN engine**在这个明确投影点形成全部576 cell、226局部量、224方向、两个mean。它不是旧112初猜上的J，也不是声称投影点已成为新的native接受状态。当前64模型每个有限结果字用原整数位式准确lift为同值128；非有限按原失败路径，不当作数值容差。

原112 boundary、mixed338×112 endpoint、独立audit与原assembly三消费者仍为§565.4原字。R515物理角循环内的有限径向词共享来源仍按原公开source注册，没有新增跨H/cache。R522 paired128 stage来源留在祖先集合，但当前R534 projected64 stage路径不假称运行了那条旧paired stage。

原system真实检查仍是：

~~~python
B.same(current['same_call_complete128_value_components_and_explicit64_linear_model_required'], True,
       'Current128 values/replay and the explicit complete projected64 linear model are required')
~~~

正文显示时空格仅为可读排版；完整source中的原after字面与现有R551/R562修复保持，plan登记当前system真实f2f9db01身份。旧same_call_complete128_final_components_required不再被读取，也不填一个假的旧true来冒全128导数。已经发表的旧229/231契约缺口是来源事实，不成为本次未来数值失败预判。

**命题2（实际正向消费）。** 若本次各原环节按其原条件完整返回，新caller确实把当前R564 owner128/replay、原R534全模型、原边界/混合末端/独立audit送到原full112/FD/fullDN函数；没有由complete旗标代原接受函数。此命题不把投影64模型等同于owner128完整程序的解析导数，也不新加该等同性验收门。

## 565.7 完整原输入、数值范围及接受责任

以下八个原JSON对象在本次request中逐值保留：original_inputs、actual63、actual91_artifact、runtime、live_call_resources、resources、original_scientific_contract、reviewed_README_blobs。所有原控制词、类型和数字层级保留。request只作普通完整JSON空白布局收紧以低于100KB，未编码科学对象、删字段、改负零或代换原值。

actual63真实prefix与actual91 tail仍沿原公开来源恢复；后二者仅承担原声明的输入/初猜责任，不能继承旧native接受或J。原78source及原其余闭包真实恢复，不因当前432计数而省略它们。

| 原科学范围 | 本次保持 |
|---|---|
| field/tail modes与spacing | 112 / 112 / 2 |
| radial stage / node | 576 / 577 |
| 每node shooting state | 224 |
| 完整local RK state | 226，含两个mean |
| 每stage方向列 | 224，全部形成 |
| owner原迭代 / 每轮trial | 32 / 10 |
| owner solve tolerance | 2e−9 |
| physical输出 | 338，原slope112、second112、两mean、height112次序 |
| requested physical J | mixed338×112，原有限差分/混合语义保持 |
| FD groups | direct_boundary与separated_boundary |
| 每组FD方向 / step层 / Richardson层 | 10 / 3 / 2 |
| FD相对阈值 | 5e−5，原全部适用收缩保持 |
| prefix inner原trial | 17 |
| prefix RMS / boundary阈值 | 1e−6 / 1e−11 |
| 原physical RMS/domain/fullDN | 全部原函数及阈值 |
| 最后fresh audit | 同一真实current H，原要求保持 |

外部noJ请求不意味着内部可省J、mean、predictor或完整physical读出。原same-H cache只有实际完成该current call之后才成立；本次不借source准备造cache。可选predictor沿原可选失败规则，不增加验收条件。

原native/fullDN、每个FD contraction、最后audit与程序completed分开报告。统计、compile success、stage全范围输出、或assembler返回了JSON均不能自动付原native/fullDN接受。原混合338×112消费者允许其已声明有限差分列，不为“全解析J”另立门。

## 565.8 原绝对钟与全部资源上限

| 资源 | 原值 |
|---|---:|
| job timeout | 350 min |
| science step timeout | 320 min |
| 唯一科学总钟 | 19200 s |
| readback/cleanup reserve | 120 s |
| factor cap | 19200 s |
| owner cap / replay reserve | 6000 s / 1200 s |
| stage cap | 8000 s |
| boundary / endpoint cap | 600 s / 600 s |
| audit cap | 1800 s |
| threads | 4 |
| Node heap | 6144 MiB |
| jac workers / native exact workers | 2 / 2 |
| native max factor bytes | 2147483648 |
| startup free storage | 68719476736 B |
| resource free stop | 2147483648 B |
| uncached protocol calls最多声明数 | 18 |

其余runtime仍为max_nodes1200、material/physical角4096/4096、outer_iterations8、extension_step0.005、taper_fraction0.4、native_eta原字符串“1”。

来源准备及初始输入恢复仍在原science clock之前；原钟schema为R493-original-full112-live128-job-deadline-v1，在原规则同步与首次native factory之前建立。新H不重开钟，per-call/per-component各cap按真实剩余钟裁剪，不能把各cap相加成为额外总预算。原startup/free门不降低。

source准备step10分钟、input恢复step30分钟、science320分钟、source读回5分钟、science必要20分钟、cleanup5分钟、report5分钟保持。资格分支减少或增加的真实耗时会改变资源停点；本证明不承诺更快、特定覆盖比或所有可能call都能完成，也不把实际资源partial算成数学反证。

## 565.9 全部RootStats、51新计数与last责任

新RootStats成员exact_lifted_factor_product，schema为R564-exact-lifted-factor-product-v1，含root_residual、root_gram、primal_flux三个路径。每条实际保以下17字段：

~~~text
terms
exact_normal
exact_signed_zero
original_multiply
fallback_layout
fallback_rounding
fallback_left_nonfinite
fallback_factor_nonfinite
fallback_left_subnormal
fallback_factor_subnormal
fallback_factor_precision
fallback_result_range
rounding_below_half
rounding_exact_half
rounding_above_half
rounded_up
carry_to_next_exponent
~~~

三条路径共51个计数另加各自last_present与**整个last**。last包括phase、angle_zero_based、index_zero_based、left_biased_exponent、factor_biased_exponent、result_biased_exponent、discarded_bits、integer_rounding_formed、rounding_relation、rounded_up、carry_to_next_exponent。缺失、显式null、未发生调用和已开始未完成是不同事实，不能互补。

一次整数舍入已经形成、随后指数进位越出normal而回退时，last仍保该已发生的整数事实；成功normal的rounding_*计数只按实际快捷返回更新。零分支指数0不冒normal，未形成舍入的rounded_up/carry为null。不得用自拟counter守恒式补未返回字段或构造科学门。

实际stage聚合仍按原stage索引join，last来自该原次序中最后实际last_present记录，不能当worker墙钟profile。计数只解释已执行分支，不表示速度或误差。

科学reader仍保**完整RootStats字典**，并非只按17字段白名单挑新成员。原R53518项、R550 primal/trace_variation各13项、R561三路径各10项与全部last/unknown成员均保留。旧root counters只计实际执行工作，不补假想省去次数。

原八张具名完整表继续保完整root_statistics、root_finite_word_cache、owner_compilation、root_cache_compile_binding、三个准备/安装对象及physical_source_input_binding。只有整对象类型/值/负零完全相同才具名共享，并在实际引用context给出完整逆。NaN不被当作可相同字对象。实际physical-source-input-binding.json仍从同call原文件读取全manifest，来源copy成功不被推成owner成功。

source preparation、installation与真实compilation分别保；当前R564 source_binding里未知的新成员也完整进入必要scope，不因旧字段名筛掉。统计表示本身不增加数值验收门。

## 565.10 原70读回与两个固定可逆来源表

本次source reader真实调用原R562 reader；原R562仍真实调用R551，后者再调用R547。没有把祖先读回假设成已经成功，也不读取旧run已删除的文件。

当前逻辑按实际同job文件处理：

1. 核RUNNER_TEMP/request236-source-preparation/source-views.json的真实descriptor、原run键与原schema。
2. 真运行原R562 readback，完整保command、started/returned、exit及实际stdout/stderr身份。
3. 真读同job request236-source-preparation-necessary.json。若为正常原完整返回，直接选整个必要对象。
4. 若原transport确为70，保原child70、fallback的necessary_readback_complete=false及完整descriptor；只从该descriptor指向的固定同job request236-source-preparation/necessary-source-overflow.json读完整字节，核bytes/SHA及attempted身份。
5. 由实际完整文件选原完整necessary对象，然后才按本层固定表示组织。不能仅嵌overflow descriptor就声称原102KB以上范围已读，也不能因本层读到完整文件改写原exit70或false。
6. 新层complete仅判断自己的完整选择/传输责任。原prepare失败、compile未起、科学未起各自仍原值。

R551/R547内部的原body、固定表定义、独立catalogue、错误和未生成后缀均保在其原namespace，当前catalogue不能解释旧索引。本层catalogue基于完整原236417map加本次15项，实际432项逐path/SHA绑定。

只有两类明确的来源metadata行使用固定表：

- verified_ancestor_sources/verified_public_sources等已知inventory行。完整path和SHA须等于绑定catalogue才用索引；实际bytes、原行序、原key序及缺键/null均保。未知shape完整字面保。
- literal_changes/replacements的固定六列id、count、before_bytes、before_sha256、after_bytes、after_sha256。完整SHA字串只按准确相同值共享；原列值、key-set/顺序及行序保，不删任何identity。

source_result等整对象引用仅在与另一个已真实完整读取的source record**有序JSON全部相等**时使用，引用有原角色、file identity和完整逆。未知member保全文。这不编码任意科学树，也不拆成多个正文规避90KB。

每个实际stderr包括真实零字节文件，都保path/bytes/SHA及完整读取内容；未生成不可冒空文件。原sourcestdout保全部身份，实际选定对象由原完整文件读取，不从截断预览恢复。

本层source和science是原两个不同语义scope，**各自一份≤90000 B**；超限仍70。完整body实际写入当前临时文件并保身份，返回false/descriptor时不能宣称完整传输。再次超限不删原字段、不拆分、不做通用数值编码、不保证未来fit。workflow对transport失败覆盖任何此前true输出，cleanup不会沿旧true执行。

## 565.11 真实schema、路径与CLI

| 用途 | 当前schema |
|---|---|
| request | public-live128-root-lifted-product-projected-model-original-full112-FD-fullDN-request-v1 |
| source | R565-root-lifted-product-current-owner-projected-model-source-preparation-v1 |
| plan | R565-root-lifted-product-current-owner-projected-model-complete-source-plan-v1 |
| owner | R565-current-H-root-lifted-product-owner128-before-projected-model-v1 |
| policy | R565-current-H-root-lifted-product-live128-projected-model-client-policy-v1 |
| pipeline | R565-current-H-root-lifted-product-live128-projected-model-call-pipeline-v1 |
| fulldn | R565-live128-root-lifted-product-projected-model-actual63-H-original-FD-and-complete-fullDN-v1 |
| runner | R565-live128-root-lifted-product-projected-model-original-full112-owned-procedure-v1 |
| reader | R565-live128-root-lifted-product-projected-model-original-full112-necessary-v1 |

实际路径变量为：

~~~text
VISIBLE_COMPUTATIONS=GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations
VISIBLE_BASE=RUNNER_TEMP/visible-live128-root-lifted-product-projected-model237
VISIBLE_NECESSARY=RUNNER_TEMP/visible-live128-root-lifted-product-projected-model237-necessary.json
VISIBLE_SOURCE_PREPARATION=RUNNER_TEMP/request237-source-preparation
~~~

完整外层source命令：

~~~bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_lifted_product_projected_source_views.py" prepare \
  --plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/r565-live128-lifted-product-projected-model-complete-source-plan.json" \
  --plan-sha256 6d6ff7d6f95f83e809fc0e260765a47185011ca86e2cc62c0a4dcf544f9789f1 \
  --computations "$VISIBLE_COMPUTATIONS" --out "$VISIBLE_SOURCE_PREPARATION"
~~~

该prepare内部实际R564命令为：

~~~bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_exact_lifted_factor_product.py" \
  --source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R564-exact-lifted-factor-product-complete-source-plan.json" \
  --average-source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R561-normal-dyadic-average-complete-source-plan.json" \
  --reuse-source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R550-accepted-root-evaluation-complete-source-plan.json" \
  --word-source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R535-native-root-finite-words-complete-source-plan.json" \
  --binding-out "$VISIBLE_SOURCE_PREPARATION/R564/source-binding.json"
~~~

这个内部命令由真实prepare持有独占输出目录，不要求操作者另外重复执行。原输入准备与科学run依次：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_lifted_product_projected_owned_run.py" prepare \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-lifted-product-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 fff570a800581ed22887734b467ad1b368cdd8d17d9df04ba49ad1e05c6bf605 \
  --namespace "$VISIBLE_BASE"

PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_lifted_product_projected_owned_run.py" run \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-lifted-product-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 fff570a800581ed22887734b467ad1b368cdd8d17d9df04ba49ad1e05c6bf605 \
  --namespace "$VISIBLE_BASE"
~~~

独立always source必要步骤调用同source命令的readback mode，plan/planSHA/computations/out全部相同。science必要命令：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/root_20261116_live128_lifted_product_projected_necessary.py" \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-lifted-product-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 fff570a800581ed22887734b467ad1b368cdd8d17d9df04ba49ad1e05c6bf605 \
  --namespace "$VISIBLE_BASE" --out "$VISIBLE_NECESSARY"
~~~

两份frame准确为：

~~~text
BEGIN_R565_LIFTED_PRODUCT_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY
END_R565_LIFTED_PRODUCT_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY

BEGIN_REQUEST237_LIFTED_PRODUCT_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
END_REQUEST237_LIFTED_PRODUCT_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
~~~

workflow中真实request/gen/planSHA均为§565.2最终值，无零占位符。工作流仅显式workflow_dispatch，由root正式发布后单次派发；当前稿不含实际未来run/source/job值，不把后来同步的main head偷代published科学来源。

## 565.12 原owned quiet、report及清理

原PID/PGID/SID、/proc startticks、registered/suspected descendants及原unknown范围保留。science reader实际调用原quiet，不以父进程returncode、job结束或来源complete推所有子孙静止。新caller/namespace/source绑定独立，旧正在运行的236/232/224/227不被操作。

cleanup要求source_readback_complete和science necessary_readback_complete两个真实条件，并由原runtime重新核same-source/run/request、namespace所有权和真实quiet。科学失败若其全部必要范围已经读完且quiet成立，仍可按原规则清理；必要body未返、超限、unknown/quiet未证则skip。source及科学两种不同complete保持，不把其中一项扩成另一项。

原cleanup命令仍由当前owned_run.py cleanup消费同request/requestSHA/namespace及--summary "$VISIBLE_NECESSARY"。不删除其他题、其他run、无关临时目录。源准备行政目录和checkout生成文件随原runner生命周期结束，不把科学namespace的removed=true写成整个RUNNER_TEMP都清空。

report独立读已保存的source/science step body并核原bytes/SHA，原字重印两个语义frame；缺失时输出实际absence，不造科学结论。report成功不提升science失败，超限70不解释为数值失败。所有raw只留本job临时范围，必要读回与quiet后按原规则清理，不上传大artifact或把raw表入Git。文件SHA无法恢复已经删除的科学内容。

## 565.13 完整条件结论与明确未付事项

**命题3（来源和原消费者组合）。** 在所列实际公开来源、真实Actions同job环境以及原步骤分别完成的条件下：

1. 当前owner确实在原scope中一次安装R564，用两件当前include及四祖先headers，保原main/CPP/replay/R534 defer，不是只改来源名字。
2. 三处快捷首乘积执行完整整数RN128，有限字等价条件如命题1；其它情况原乘法。R561第二乘法、原全部累加、root方向/试步/门保持。没有宣称所有首Q乘法指令保留。
3. 原当前128值/replay、同DN投影64全模型、全部576/224/226/双mean、112boundary、mixed338×112、独立audit和FD/fullDN原门沿真caller实际相接。
4. 新51项计数及全部last、unknownRootStats和实际compile/source/installation从本次原件选入。历史原70/false保留，新层完整选择独立判断，两个90000上限不提高。
5. 原绝对钟、内存磁盘、各cap、owned quiet和清理范围不变。任何当前准备、编译、来源或传输旗标均不自动付原native/fullDN接受。

本文构造仅是源文、普通JSON、逐字变换、metadata哈希/长度与完整来源并集；未本地导入数值源、执行AST、编译、运行科学、fixture或测试。Actions中原有syntax/compile/科学步骤属于完整实际入口，不是新增独立前门。

仍未付：本次实际编译成功；R564三path实际覆盖与计数；owner接受和fresh replay；完整当前模型及末消费者；FD/fullDN所有原判定；必要body真实体积；实际quiet/cleanup；耗时、加速比或资源覆盖改善。没有预称任意新场、接受父、连续C²或闭面几何完成。后续R566仅从其真实官方终态归责。

## 565.14 容量、保存与引用

题内当前generator、plan、request三件合计205711 B；workflow在题目录外23955 B。本文最终实际bytes在交接manifest单列，与205711相加得到本次准确topic增量。R564四件属其独立发布，不能重复算到本条，也不能为容量任删它们或其他科学来源。

当前request为普通完整JSON+末LF，96574 B；减少空白不改变任何字段、类型、数组次序或原八对象。十展开caller共360175 B，两新include共62906 B只在Actions生成，Git保完整literal计划和每件完整SHA；不重复刊展开文本或大diff。临时交接manifest不是科学输入，也不另入Git。

直接依据包括：已刊R491原fullDN正向消费者合同；R529/R532/R534当前投影模型、同DN与准确lift来源；R535/R550/R561完整祖先；R549实际source70范围；正式e6d389d所含R562完整入口；本条所列R564完整header/adapter/plan/证明。每一实现事实均由上表完整身份和本条实际literal plan定位，算术论证只在所列条件内成立。固定历史及容量删移由root独立行政操作，不能被本文当成任意动态依赖不存在的证明。
