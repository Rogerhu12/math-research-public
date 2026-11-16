# R573 — request240：准确 root 合成乘积接入原当前值、完整投影模型与原 FD/fullDN

**可信度：已证明（限本文来源组合、逐字实现与所列条件命题）；本入口的实际编译、求解、模型、FD、fullDN、审计与资源完成尚未执行或支付。**

作者：ChatGPT / GPT-6，2026-11-16（UTC）。本条是独立完整组件与执行入口，实际结果预留 R574。没有从来源生成成功、统计存在、程序 complete 或 job 标签预填数值接受。所有科学计算仍只在本库公开 Actions 内进行；本文制作只处理源码、普通 JSON 和字节身份。

## 573.1 完成的工作和准确边界

本条以完整 R565/request237 为祖先，接入 R572 的五个 root 合成乘积。R572 逐调用复用原 R564 的完整整数乘积与一次 RN128 算法；其资格不成立时执行原 Q 乘法。改变的是当前声明的乘积实现，不是缩减模式、角点、root 试步、stage、方向列或均值。

当前入口保留 R535 的同 root 固定词/U 词、R550 的同 root 下一迭代完整接受值复用、R561 的第二次 dyadic 归一化选择和 R564 的三个角向首乘积。原持久 owner 的 CPP/main/solve/replay、当前 H、原32次/10试步、2e-9 容差、原绝对钟及每个实际门不变。R572 不新建状态、H、几何或角表缓存。

本条同时保留 R534 的诚实精度合同：当前 owner128 值与 fresh replay 权威；在同一 Node/DN、同次当前完整状态的一次 RN64 投影上形成全576/224的模型，再将其有限64位字准确 lift 为128位传原边界/末端消费者。该投影模型不被称作 owner128 程序的全解析导数或另一个已接受解。原 mixed338×112 合同和原 affine FD/fullDN 门照常消费它，不增全解析门或模型对拍门。

原 request237 与其来源是重建字节的祖先。本次 request240 必须在自己的真实 run/source 中重新完成输入恢复、当前 H 调用、owner、fresh replay、模型、末端、FD 和最终审计。不得继承旧运行接受、J、merit 或缓存。

## 573.2 完整交付与祖先身份

下表列最终生成器、完整来源计划、完整请求和工作流。证明自身最终 bytes/SHA 由交接 manifest 记录，避免自引用；manifest 仅用于传递，不是新的科学输入。

| 交付件 | 完整 bytes | SHA-256 |
| --- | --- | --- |
| `root_20261116_live128_synthesis_product_projected_source_views.py` | 38611 | `3bb1084dfb44d675db8f186b138c5fb68ac6da9a1978f25c013e2bc5609f9cf2` |
| `notes/r573-live128-synthesis-product-projected-model-complete-source-plan.json` | 82812 | `85fdec3e86821a8a6f85828bbf399347fbd7c3d57e97ab2ad1404561945974ed` |
| `public-live128-root-synthesis-product-projected-model-original-full112-FD-fullDN-request.json` | 97177 | `e4ad6178a06d2cf270f3469c4cbcce4747c8876e7c95c50f829be58c9f6c437a` |
| `.github/workflows/visible-larger-public-live128-root-synthesis-product-projected-model-original-fullDN.yml` | 24295 | `722ef48081d5d6e4ee58c9a77cf376832682ab050c4e04fb4e71596d4fafeca6` |


完整 R565/request237 正式来源：`99347c619e66946b758f6f731ce0a4f76d41fa9e`。祖先请求 public-live128-root-lifted-product-projected-model-original-full112-FD-fullDN-request.json 为96574 B / fff570a800581ed22887734b467ad1b368cdd8d17d9df04ba49ad1e05c6bf605；祖先生成器38098 B / ee6bad1b586c77e94e54714ecff05a980ce9ad11bc50658a55583fd372ddc6f2；祖先 plan71039 B / 6d6ff7d6f95f83e809fc0e260765a47185011ca86e2cc62c0a4dcf544f9789f1。当前生成器实际读取并核这三件全文；祖先 request 数、schema、432个总 pin、75个生成 pin及 R534 core plan 全部核对。

R572 执行源和两件实际 include 的独立身份如下。两件 include 由公开 Actions 从完整 plan 生成；不把它们假作已在 Git 的公开文件。

| R572 来源 | bytes | SHA-256 |
| --- | --- | --- |
| `root_20261116_exact_root_synthesis_products.hpp` | 2380 | `a715367b67448c85c6ff180ad24f915334f188751df5d3a2adca5ed3535e5f9a` |
| `root_20261116_exact_root_synthesis_products.py` | 20999 | `cdc734c9b704ffa77f46b32054cff1dbae4df10e91f6be66f4ddeb53a4237fcf` |
| `notes/R572-exact-root-synthesis-products-complete-source-plan.json` | 14796 | `25e8a39b5c8beaaa0b8b049d79f0e5d278622aa4f62e156fcd50cfceb50f1a64` |
| `root_20261116_exact_root_synthesis_products_primal128.cpp` | 27592 | `8952e5a65a04e918d00ef990a1355ba3c1912284dfc2c482d8f861aa896b660a` |
| `root_20261116_exact_root_synthesis_products_trace128.cpp` | 36252 | `138c6aaaba86628befd71b398bd2d393e661cb4abdab7781d6ef1ba0bebe05bb` |


R572 原 compiler 插口仍是 geometry_20261115_native_persistent128.py，43371 B / 767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322。原 compile_owner 函数3860 B / be019045058f4616f98b07e19c0d8d3901e979ce2b1ba7d4259c65fcae4ae46d；本次明确派生函数7525 B / 898388a3dbcae98c950496bbfa705e2cfa1241f979a6c170f960a3370efa5957。持久 CPP 22364 B / 7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd 本体原字保留。实际 include、compiler 函数和来源 receipt 分别有新身份，不重标为原 primal/trace 字节未变。

## 573.3 源集合与十个实际 caller

来源集合是可审查的有限明确集合：

| 集合 | public | generated | 总数 |
| --- | ---: | ---: | ---: |
| 完整原237 | 357 | 75 | 432 |
| R572 新 header/adapter | 2 | 0 | 2 |
| 本条生成器 | 1 | 0 | 1 |
| 本条十 caller | 0 | 10 | 10 |
| R572 两 include | 0 | 2 | 2 |
| 当前完整并集 | 360 | 87 | 447 |

原432每个 basename→完整SHA逐值保持，不删除被当前链替代的历史源。原75个生成文件仍由真正祖先生成器在本 job 重建，不从公共 Git fetch一个不存在的生成文件，也不只把计数当递归导入完整性证明。

十个 caller 的每个 baseline、完整 before/after 字面、准确 occurrence count、输出 bytes/SHA 都在本条 plan。总61条文字替换，完整展开364421 B仅在 Actions。逆序替换能恢复每个完整冻结 baseline；这是有限字节计划的声明，不是新增科学测试或原门。client/fullDN 的旧来源更新块完整保留，再追加当前来源，旧 pin 不因新名字而消失。

| 真实角色 | 生成文件 | bytes | SHA-256 | 完整 literal 数 |
| --- | --- | --- | --- | --- |
| owner | `geometry_20261116_live128_synthesis_product_projected_same_call_owner.py` | 26666 | `2af373696034e49f61e6dcc49707e668ed60d600b5a4f9dbf0d71d85cd24ad17` | 9 |
| system | `exact_20261116_live128_synthesis_product_projected_current576_system.py` | 29077 | `b196cd850f00bfba64a3bda44f129cc2c290fb73bd5da54db4bdf15da495df14` | 1 |
| qr | `exact_20261116_live128_synthesis_product_projected_current576_chain_qr.py` | 21858 | `ae98a05e6b68c17b56a966710760fee27ca4a613e3c3396dbe8f75580870cd7f` | 1 |
| pipeline | `geometry_20261116_live128_synthesis_product_projected_call_pipeline.py` | 43286 | `1ad21f183fb98e859086d96048063a25aaa749803d68bfa67801a4df665ab666` | 3 |
| call | `geometry_20261116_live128_synthesis_product_projected_current_call.mjs` | 45476 | `cf59d20d7fbd315b5a4250f2e691c10292030805c79430a4fa71e1755a98f0c8` | 4 |
| worker | `geometry_20261116_live128_synthesis_product_projected_worker.mjs` | 8327 | `ecad08d60e9bcf668e2c5c82771627cae2c7160f806b8f2573e90dacb898f021` | 2 |
| client | `geometry_20261116_live128_synthesis_product_projected_tail_client.py` | 40476 | `3c35e7a802abdfe4857b59f6335e515207b67b312a1a08c07ff7e39ddd98e83f` | 5 |
| fulldn | `geometry_20261116_live128_synthesis_product_projected_original_full_dn.py` | 46439 | `721aaa94d4bd70fed644aed0ee62e0d19ba526aadd1e6793645636a90f445b63` | 6 |
| runner | `geometry_20261116_live128_synthesis_product_projected_owned_run.py` | 39422 | `13c3de46ba8f4bcadf82856d72bf330bdf9088d9b06a7f4afd7dfdf658cf3658` | 15 |
| reader | `root_20261116_live128_synthesis_product_projected_necessary.py` | 63394 | `e48c769418ffac56a2e931cbee4bc4474ad2067007e561c2aaa49f9a4291701b` | 15 |


原 R534 components/boundary/assembly 及其数学体无新副本；R572 include 仅改变公开 plan 的七条 primal 和三条 trace 文字。当前 owner/pipeline/source policy、reader 与真正新文件名同步；系统 honest guard 仍消费实际存在的新字段，不复活旧的“全128 final components”虚假布尔值。

实际 schema：

| 用途 | 实际 schema |
| --- | --- |
| request | `public-live128-root-synthesis-product-projected-model-original-full112-FD-fullDN-request-v1` |
| source preparation | `R573-root-synthesis-product-current-owner-projected-model-source-preparation-v1` |
| source plan | `R573-root-synthesis-product-current-owner-projected-model-complete-source-plan-v1` |
| owner | `R573-current-H-root-synthesis-product-owner128-before-projected-model-v1` |
| pipeline | `R573-current-H-root-synthesis-product-live128-projected-model-call-pipeline-v1` |
| pipeline input | `R573-current-H-root-synthesis-product-live128-projected-model-call-pipeline-input-v1` |
| policy | `R573-current-H-root-synthesis-product-live128-projected-model-client-policy-v1` |
| fullDN | `R573-live128-root-synthesis-product-projected-model-actual63-H-original-FD-and-complete-fullDN-v1` |
| runner | `R573-live128-root-synthesis-product-projected-model-original-full112-owned-procedure-v1` |
| necessary | `R573-live128-root-synthesis-product-projected-model-original-full112-necessary-v1` |


原组件、边界、装配、stage clock schema 保 R534 原值。原 job clock schema保 R493-original-full112-live128-job-deadline-v1；schema相同不能替代实际文件、run、request、source和同目录身份核对。

## 573.4 真实源码生成、同目录和一次直接安装

源码生成目录必须是实际 $GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations。生成器、祖先、当前 caller、include和它们的 HERE 都在这一真实目录。额外源准备元数据仅在 $RUNNER_TEMP/request240-source-preparation；当前科学 namespace 是 $RUNNER_TEMP/visible-live128-root-synthesis-product-projected-model240。没有把新视图留在另一个目录却把 computations 标成原目录。

实际顺序如下：

1. 绑定当前 plan、当前生成器、冻结237请求/plan/gen和 R572/R564/R561/R550/R535 五份根计划。核真实公开 Actions 仓库与四run字段。初始记录 complete=false、error=null、当前 phase和全未生成角色。
2. 在同一 HERE 调用原 R565 的 source-only prepare；原完整432来源逐字恢复并重新核每个 SHA。祖先元数据目录仍按其原 schema 使用 request237 名称；它是当前 job 内的来源阶段，不是调用原237科学。
3. 当前十个 caller 逐完整 before/count/after 在内存形成，核完整输出 bytes/SHA；无新模块导入、AST、编译或数值调用。原文件或已有输出不得被偷偷覆盖。
4. 真调用 R572 adapter。该 adapter source-only 递归准备 R564→R561→R550→R535；允许实际同目录已生成且同SHA的祖先，仍读核完整来源。两新 include实际写出，绑定完整 R572 source-binding。
5. 只有实际 R572 child返回0、完整binding同run/source/HERE、每件输出完整身份一致，才写十个新 caller和447完整map。实际 child退出码、stdout/stderr、已生成和未生成 suffix始终留证。source-only complete不声称g++已执行。
6. 工作流随后对真实447 source作原有 Python compile/Node syntax 检查。仍是原入口检查，只在 Actions执行。它不等于科学计算、owner接受或正确性验证。
7. 当前 owner调用时实际读取同job source-views receipt，并验证自己确在本次生成列表中。读取 R572/source-binding.json 全文，核与 source record同一个完整对象，核20999 B/cdc7 adapter，然后将它直接安装到未被其它根适配器安装的原 owner_scope。

R572的直接安装拒绝先有 R564/R561/R550/R535 hook的scope；祖先 prepare不安装hook。当前source generator自身也不装hook。声明的“one direct installation”因此是真调用关系，不是仅改metadata文字。

原R534 defer仍在编译接点装完后以原来源明确替换 owner-finally的组件交接函数，保完整owner/replay先行与原raw存活。它记录旧同步post没有执行，而非伪造旧stage/boundary/endpoint/audit complete。

## 573.5 五个乘积的条件数学命题

记原binary128一次乘法结果为
\[
  \operatorname{RN}_{113}(x y),
\]
其中 \(x,y\) 是该原式在本次状态/角点上实际形成的二进制字，而非理想三角函数值。R572逐次调用未改的R564 helper：其资格实际核字布局、当前rounding mode、两输入分类、右因子有效位数和结果范围。合格 normal路径以完整113×53整数乘积、完整低位余数和tie parity执行一次 nearest-even；不截掉乘积尾位。实际有限signed zero按原sign规则处理；任何其它情况执行原 \(x*y\)。

**命题1（单乘积字值）。** 在R564给出的支持布局、rounding和每调用资格内，helper输出与原该Q乘法的RN128结果字相同；资格不成立走原乘法。此处沿用R564完整整数舍入证明，R572没有改变其算法或放宽资格。它不声称所有首乘法指令仍被执行，也不声称异常标志或NaN payload同一。

五个新增调用点保如下原词、条件与地址：

| 统计 path | 原分支 | 本次真实左操作数 | 本次真实右操作数 |
| --- | --- | --- | --- |
| fixed_fallback_P | !fixed_used | momentum[j] | sn[j] |
| fixed_fallback_Pt | !fixed_used | pt[j+1] | cs[j+1] |
| L | 原每个mode | L[j+1] | cs[j+1] |
| evaluation_u_words | u_used | u_words[j] | sn[j] |
| evaluation_u_fallback | !u_used | (-m*L[j+1]+(m*m-1)*momentum[j]) | sn[j] |

最后一行仍先按原括号和原运算次序算完整左表达式，再对其本次结果字与sn[j]调用helper。没有将 \(-mL+(m^2-1)p\) 展开、交换加法，或以理论恒等式代替literal表。Pt的频率因子已在原pt[j+1]中按原式形成，R572不再次归并它。

**命题2（当前root合成）。** 比较同一实际输入、同一精度与原执行顺序，忽略未承诺的资源前沿和fenv副作用等价。对每个实际执行的角点n和mode j，原P、Pt、Lv、U的每一个原加法保持位置及顺序；以命题1逐项替换原乘积，可归纳得到该合成序列的输出字相同。这里不需要所有中间乘积normal：不合格路径真执行原式。原NaN/Inf路径不凭“输入有限”排除，相关特殊字落原乘法；不泛称其NaN payload或异常标志由整数路径认证。

R535的fixed_used/u_used资格、固定词构造、U词构造和缓存寿命不改。固定词成功时P/Pt走的仍是原cache路径，R572两条fixed_fallback统计只在原fallback分支出现；不能从五条path名字推每条都实际覆盖。U的word路径和fallback路径互斥，实际计数区分，不人为补另一条执行。

原R564三个角向首乘积保原字实现；R561第二次product*inverse的选择保原字；全部+=、root trial顺序、判定、停止位置、时间检查位置以及R550下一迭代接受值资格均保。原R535 header本体、R564 header本体、R561/R550本体不因本条而改动。R572不追加跨root/跨stage/跨H状态。

因此，可获得的是原同词有限算术路径的条件等价，不是相同墙钟、相同资源停止前沿、相同浮点异常标志或速度保证。原deadline可能让不同实现走到不同实际前缀；实际结果必须仍记录全已完成/partial/未访问范围，不能把条件等价延伸成整run完成。

## 573.6 原编译器接点与20件真实依赖

R572从原767a的完整compile_owner函数按四条明确文字变换形成7525 B的新函数；原持久CPP和其main/solve/replay不复制改算法。当前ORIGINAL_CPP/TRACE_CPP变为实际R572 include名；原standalone main截取规则用于实际新trace，而不谎称原R283 prefix逐字未变。

20件真实依赖按层分为：

- R535/R550/R561/R564/R572的五件header；
- 每层primal/trace两件，共十件生成include；
- 五件相应adapter。

compiler在g++前按真实HERE逐件核bytes/SHA；原ownerCPP和原工程wrapper自己的来源核仍另在原合同内，不把20这个列表当全部文件无须来源证明。原编译flags、线程、精度、CPP主文件和原资源参数保持。

安装与编译是不同事件。当前owner-call-procedure真实记录三个字段：source preparation文件descriptor；source binding的actual_file和完整actual_binding；compiler_installation返回body。初始null与未生成字段严格区分。它们存在不能证明compiler完成。

真实编译结果只能来自原owner summary内 compilation.root_finite_word_cache_compilation_source_binding：完整R572 binding（包含actual_R564_source_binding递归祖先）、实际命令、生成include、返回码、executable、stdout和stderr，以及真实compiler_completed。没有把source-prepared当compiler_completed，也不覆盖编译错误为数值失败。

当前布尔值明确：

~~~text
one_direct_R572_installation_without_prior_R564_R561_R550_or_R535_hook = true
root_primal_uses_declared_R572_exact_root_synthesis_products_source = true
original_synthesis_product_RN128_words_and_sum_order_preserved = true
original_R535_fixed_and_U_word_constructions_unchanged = true
original_R564_three_angular_average_products_unchanged = true
literal_first_Q_multiply_preserved_at_all_changed_sites = false
floating_exception_flag_equivalence_not_claimed = true
~~~

这些是源码责任说明，真实执行是否到达仍由本次调用记录决定。

## 573.7 原当前值与投影模型的正向消费链

新source关系是 owner→pipeline/current_call→worker/client→system/QR/fullDN→runner/reader，真正原packet和同call身份沿每件文件传递。source表中的旧caller只作祖先，不代替新caller本次执行。

原流程先形成真实当前H/完整原64 withJ快照与literaltrace packet，重新执行持久128 owner；它的全部577×224状态、残差、两mean和fresh replay保持。final complete、below_original_tolerance和independent_fresh_replay_complete都按原真实字段核，而非从新统计或compiler成功补出。

owner ready后，当前Node在同一个真实DN引擎内，用本次完整128状态的一次RN64投影计算新576个stage的全226×224方向、全224×224 port后映射及两组2×224 mean。每个有限binary64结果按原R532整数位式准确lift为相等binary128字，±0保，非有限实际结果走原明确失败。旧配对stage来源仍保历史，不能称它在当前R534模型分支执行。

随后原112boundary、真实mixed338×112末端与原独立物理audit按本次完整状态/来源消费。输出338行准确顺序仍是slope112、second112、meanSlopeCorrection1、meanSecondCorrection1、height112；旧历史request的另一个描述仅作为历史metadata，不改变真实消费者。

系统的真实诚实guard继续读取：

~~~text
same_call_complete128_value_components_and_explicit64_linear_model_required
~~~

其含义是当前128值/replay加显式完整投影64线性模型；不补旧same_call_complete128_final_components_required=true冒成全128解析模型。本条保留已在232/236/237采用的真正guard修复。

原10个direct、10个separated方向组、3步长层、2 Richardson层和5e-5 FD相对门照旧。原affine FD是否付其implementation合同，由原结果判断；它不被提升为重新求每个方向的非线性DN。原fullDN现有finite difference列并不因“非全部解析”而新增接受障碍。最后当前H fresh audit、原RMS/边界/domain门仍是原实际终判。

## 573.8 未改的输入与科学对象

以下八对象逐值与完整237同；表中身份采用普通JSON.stringify紧凑UTF-8（不加LF）仅用于本条元数据核对，实际原请求和大输入各自仍按原完整文件身份恢复。

| 原对象 | 紧凑 UTF-8 JSON bytes | SHA-256 | 与完整237同对象 |
| --- | --- | --- | --- |
| `original_inputs` | 2406 | `f4f19b6929cee42f694e2539b5bcd8f91b44db57f1081dc207cb09d26fb4edb7` | true |
| `actual63` | 567 | `917036e46adcf1bd6bbad0a140875bf13cab53c9b45bb1efb46f7e11ca0e43cb` | true |
| `actual91_artifact` | 406 | `86e1820e3c8c575f010427737e8456d0225601784929f0cd79451c28dcf62d58` | true |
| `runtime` | 241 | `984018fb006629e20c6ddfd4efc924950ec8e52b5cff04b39290d37840c66b77` | true |
| `live_call_resources` | 209 | `5b12271a1c0a2a3df0c3c5e474edd53ebcbece920b34014a62a70f5127a5b71a` | true |
| `resources` | 611 | `71ca1c2e355d12d0e388cce2c2e5416e8ba09493c3d654af20c6a6b2ada84106` | true |
| `original_scientific_contract` | 1598 | `6116d0cf0f266b69ed585ab66a34c68a308e1a5740afb36e0611edd58cfdb0ed` | true |
| `reviewed_README_blobs` | 148 | `231384d8f954eb0ffef05a48ee77ccf2d1ad381f22ea8004c158072aadff1929` | true |


lanes仍唯一 live128-original-full112，没有换连续C/十参数/闭面目标。

原输入保actual63完整warm/status/port来源、原acceptedprefix和两个ready。actual63只供原prefix初猜，不继承当前fullDN接受；actual91完整artifact只取原failed73全tail初猜，不取其prefix、response、接受state或cache。仍执行原78公开数学源恢复，原大件只在Actions按原位置和完整SHA读取，不把tool里的摘要冒原输入。

为避免request不断复写同一历史说明，本条arithmetic的R535/R550/R561/R564描述采用**固定完整237请求+准确JSON pointer**，并另列本次current_owner_installation。实际source生成会读该祖先请求全文、核完整SHA，再准备所有原件；四项源计划与全部sourcepins仍直接绑定。本次R572五path合同完整列在当前request。本表示只去掉重复的来源说明，不是科学数组编码，不改变这八对象、实际runtime参数、任何原数字类型或源图。当前caller不读取这些历史arithmetic描述来选择数值路径；它们通过实际源计划和真scope安装接线。

原fixed-cache词、准确乘法资格和fallback、replay/owner同源责任仍由实际源码执行。不得以描述pointer代替一份未读取、未核身份的来源或科学结果。

## 573.9 原预算、clock和资源前沿

原资源如下，均直接保在请求的runtime/live_call_resources/resources对象：

| 项目 | 原值 |
| --- | ---: |
| job timeout | 350 min |
| science step与总科学钟 | 320 min / 19200 s |
| reader/cleanup reserve | 120 s |
| owner cap / fresh replay reserve | 6000 s / 1200 s |
| stage / boundary / endpoint / audit cap | 8000 / 600 / 600 / 1800 s |
| owner threads | 4 |
| 启动最小free | 68719476736 B |
| 科学资源stop free | 2147483648 B |
| 原outer iterations | 8 |
| 原推导最大uncached call数 | 18 |
| node heap / jac workers | 6144 MiB / 2 |
| max_nodes / material / physical angles | 1200 / 4096 / 4096 |
| 原extension_step / taper_fraction | 0.005 / 0.4 |

原depth576、nodes577、tail112、spacing2、224state/方向、226local含双mean及338×112全部保。原native exact workers2、最大factor2147483648B与native_eta="1"保。

source准备和原输入恢复在原science clock启动前进行；本条没有把它们假称已经消耗19200科学钟，也没有为owner或新H重开clock。run()只在不存在job-deadline.json时创建原绝对deadline，起点在rule sync和首次native factory前。每个owner及后消费者的cap按该实际剩余时间裁剪；cap相加不构成总预算承诺。

原owner分配保audit allowance与330/345等原开销常数，replay按owner剩余裁；保少于原最低owner/replay额度时的ResourceStop。没有因R572可能省工作而缩减guard，也不因此预判现在预算足以完成全链。内存磁盘检查、备用SDK删除范围、原unknown PID责任均不变。

## 573.10 完整统计和科学必要读回

当前reader从真实owner、final/replay及每个实际evaluation读取完整RootStats；不只读declared计数名字。所有原unknown成员留在整对象中。

新增exact_root_synthesis_products有五个准确path，每个保以下17项及完整last/last_present：

~~~text
terms, exact_normal, exact_signed_zero, original_multiply,
fallback_layout, fallback_rounding, fallback_left_nonfinite,
fallback_factor_nonfinite, fallback_left_subnormal,
fallback_factor_subnormal, fallback_factor_precision,
fallback_result_range, rounding_below_half, rounding_exact_half,
rounding_above_half, rounded_up, carry_to_next_exponent
~~~

每项统计只算本次实际工作；未到path、缺字段、显式null、0不能互相冒充。last完整保实际angle/mode及原R564 last字段，不只返回计数总和。原统计join按原stage索引顺序，而不是把并发最后完成者当原最后地址。

原R53518项/full last、R550 primal与trace每path13项、R561三path×10、R564三path×17及原所有RootStats依旧。新五path统计不证明角点覆盖、root收敛、全stage完成或耗时归因。

科学reader仍只在原具体字段应用八张具名整对象表：RootStats、root_finite_word_cache、owner_compilation、root_cache_compile_binding、三个source/installation记录和physical_source_input_binding。只有整个JSON类型和值严格相等才共享；NaN不共享，bool/int/float不混，负零区分，缺失与null分开。行数组次序保，完整对象内unknown字段保；字典序不声称原stdout字节序。

表的逆明确：按original_record_indices还原每个record；每列取constant或对应original_values；只在声明的ref位置解其准确catalogue。RootStats中只额外展开原root_finite_word_cache引用；compilation中只额外展开原root_finite_word_cache_compilation_source_binding引用。没有通用科学树压缩或任意数字编码。

原当前call/owner/current-model/四consumer/FD/fullDN/rules/errors/partial及未起范围选择全部保持。原错误选择限制保持，不把原日志摘选说成完整所有stderr。当前owner安装/source-binding/编译完整对象分别选入；五原physical-source-inputs同字复制receipt与manifest的真实范围继续保留。

最终fullDN_accepted只读原status.full_BVP_accepted is True；不会由新R572状态、component complete或deferred hook里的false推相反数值结论。必要读取完成和数学完成是不同布尔。

## 573.11 source必要范围、原70与固定具名表示

source reader实际调用原R565 readback，后者沿真实祖先链读原R562/R551/R547必要选择。若原层返回70和false，当前层保它真实退出码、fallback正文和身份，不把它改成0/true。

原层的完整本地对象在同job $RUNNER_TEMP/request237-source-preparation/necessary-source-overflow.json。只有descriptor指向准确固定路径、完整bytes/SHA/attempted字身份都同、schema/run/plan/source同，当前层才真正读取该完整文件。它没有用不足90K的overflow descriptor假恢复旧102413或后续对象。旧完整对象缺失、被删或不匹配时，当前body报明确error/incomplete。

普通原返回0/2时，读取实际普通完整body；同一transport与完整对象只按同文件identity作明确引用。真正当前source record和完整祖先必要对象分别独立选入，整对象严格有序相等时才消除重复嵌入。

source表示只两张固定语义表：

1. verified_ancestor_sources/verified_public_sources中恰file/bytes/SHA三个字段的实际行，file必须等HERE/name，SHA必须逐值等完整432+当前15map；真实bytes保，原行次序/键次序保，未知形状原文。catalogue来自真实已读完整祖先请求和显式当前增量，没有补未观察文件大小。
2. literal_changes/replacements的固定六列id/count/before_bytes/before_sha256/after_bytes/after_sha256。所有实际字段的存在性、null、原键次序保；完整SHA字符串只在这个具名列的字典中共享，不截断hash，不压任意对象。

当前R572 source_binding递归包含actual_R564/R561/R550/R535所有返回字段，unknown新binding保全。每个实际source stderr逐文件保path、bytes、SHA和完整UTF-8-surrogateescape内容，存在的空文件保其真实identity，不将缺文件填为空。stdout完整内容如已独立选入原body则只保对应文件身份，不重传同一body。

当前necessary_readback_complete由真实全层必要对象与当前实际return字段判断，不要求每个祖先transport0；源码生成complete、必要读取complete、compilercomplete、科学接受各自独立。若当前总body>90000字节，仍保存临时完整对象、只返真实overflow descriptor并exit70；不增大90K、不分片、不保证未来容量、不按未来容量删失败/未访字段。科学必要另有同样独立90K/70合同。

## 573.12 实际 CLI、工作流和报告

公开工作流仅workflow_dispatch；root发布后单次真实派发。当前稿没有未来run/job/source值。相应checkout为blob:none的明确稀疏集合，保祖先全部plan并添加R572和本条plan；没有为了读取source字节获取全部科学raw。

source prepare命令：

~~~bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_synthesis_product_projected_source_views.py" prepare \
  --plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/r573-live128-synthesis-product-projected-model-complete-source-plan.json" \
  --plan-sha256 85fdec3e86821a8a6f85828bbf399347fbd7c3d57e97ab2ad1404561945974ed \
  --computations "$VISIBLE_COMPUTATIONS" \
  --out "$RUNNER_TEMP/request240-source-preparation"
~~~

其内部真实root source-only命令为：

~~~bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_exact_root_synthesis_products.py" \
  --source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R572-exact-root-synthesis-products-complete-source-plan.json" \
  --product-source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R564-exact-lifted-factor-product-complete-source-plan.json" \
  --average-source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R561-normal-dyadic-average-complete-source-plan.json" \
  --reuse-source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R550-accepted-root-evaluation-complete-source-plan.json" \
  --word-source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R535-native-root-finite-words-complete-source-plan.json" \
  --binding-out "$RUNNER_TEMP/request240-source-preparation/R572/source-binding.json"
~~~

真实runner prepare/run分别调用同参数：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_synthesis_product_projected_owned_run.py" run \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-synthesis-product-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 e4ad6178a06d2cf270f3469c4cbcce4747c8876e7c95c50f829be58c9f6c437a \
  --namespace "$VISIBLE_BASE"
~~~

prepare只将上述mode换为prepare；readback source只将source命令mode换readback。science必要：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/root_20261116_live128_synthesis_product_projected_necessary.py" \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-synthesis-product-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 e4ad6178a06d2cf270f3469c4cbcce4747c8876e7c95c50f829be58c9f6c437a \
  --namespace "$VISIBLE_BASE" --out "$VISIBLE_NECESSARY"
~~~

work env：VISIBLE_BASE为前述当前240namespace；VISIBLE_NECESSARY是同名namespace加-necessary.json；VISIBLE_SOURCE_PREPARATION为request240-source-preparation。所有真实request/gen/planSHA已写当前workflow，不用旧237SHA冒本次对象。

两个原语义scope各有一个完整body，compute/report核相同bytes/SHA原字传递：

~~~text
BEGIN_R573_SYNTHESIS_PRODUCT_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY
END_R573_SYNTHESIS_PRODUCT_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY
BEGIN_REQUEST240_SYNTHESIS_PRODUCT_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
END_REQUEST240_SYNTHESIS_PRODUCT_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
~~~

report成功不是科学成功，未返回body只报告实际absence；它不自行填native/fullDN结果。两种always读回步骤各自独立，前一70不阻后一必要职责。

## 573.13 原owned lifecycle与清理

原PID/PGID/SID及/proc startticks、registry、suspected descendant和unknown责任全保。原SIGTERM→SIGKILL/实际静止算法保持；不把父returncode、job完毕或sourcecomplete当完整子树quiet。不同正在运行namespace不受本条操作。

science reader先执行原quiet；未证静止时不继续冒读全部科学文件。清理同时要求source必要和science必要完整，且原cleanup再次核当前request/source/run、namespace和真实quiet。任一必要body缺失或70、unknown/quiet未证则原skip，不为腾容量删除科学数据。科学失败若必要完整且真实静止仍按原条件清理；这不改变其原失败原因。

只清本次被原owner管理的科学namespace。源码生成在checkout、source-only元数据在独立RUNNER_TEMP目录，随原runner生命周期结束；不把科学namespace removed=true写成整个runner所有内容已删。没有新增artifact、raw上传、或将Actions必要/raw输出写入Git对象。来源SHA不能重建已清理的科学内容。

## 573.14 完整条件结论与未付结果

**命题3（真实组合）。** 若本文实际公开来源、原输入、同job环境以及各原阶段分别完整执行，当前owner在原scope只安装R572一次；五个新增乘积按命题1/2保原RN128词和合成次序，原祖先数值合同及fallback不变；原当前128值/replay、同DN完整投影模型、全部列与两mean、boundary/mixed338/独立audit和原FD/fullDN沿当前真caller接通。完整统计、source/installation/compile与原necessary从本次真实文件选入。source/transportcomplete不代数值接受，原资源前沿不承诺同一。

这是来源/控制流/条件算术结论。没有在本地运行scientificimport/AST/compile/science、fixture或测试；只形成有限源码文字计划、普通JSON和实际字节身份。Actions中的原syntax检查、g++和科学步骤没有被增加为独立预验收实验。

尚未付：本次真实编译；每path实际工作和资格分布；owner接受/fresh replay；当前576完整模型；全部末consumer；FD/fullDN最终原判定；必要body实际体积；实际quiet/cleanup；性能和资源覆盖。R574仅在其真实官方终态后记录，不能继承237或其它run结果。没有连续C²/闭面几何、全参数域或任意新误差定理的附带主张。

## 573.15 容量和可恢复来源

题内gen/plan/request三件合计 218600 B；workflow在题外 24295 B。本文最终bytes另列manifest，与前三件相加给本条准确topic增量。R572四件为其独立发布，不重复记为本条新增。实际十caller364421 B与两include63844 B仅Actions生成，不刊展开源、大diff或科学raw。

每个当前文件均<100000 B；request仍为完整普通JSON+LF，历史描述只按§573.8完整固定来源指针表示，不以压缩科学字段满足限额。若后续容量不足，由root按实际固定历史与当前消费者另行处理；本条不授权删除任意旧source/input。

直接来源：完整R565冻结请求/plan/gen和本文447map；R572三件完整来源及其五path计划；R564完整113×53 RN128证明；R561/R550/R535原祖先；R529/R532/R534同DN当前投影模型；R491原native/fullDN正向消费者；R549实际source70责任。所有实现事实以本文文件身份和完整literal计划定位，所有数值/资源结论仅在明确条件内成立。
