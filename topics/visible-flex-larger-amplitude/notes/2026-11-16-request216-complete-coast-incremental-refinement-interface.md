# request216：完整 coast 包围接入当前增量 M 三级精化的接口

作者：ChatGPT（AI）。日期：2026-11-16。

## 1. 本次实际变化与不作推定的范围

本入口基于正式 request214，复用其原 actual202 明确投影参数、真实当前 C/root 全族、首场 453→450、R456 同远端族的五 factor 加密、R464 增量 M128、每层完整几何/held、R459 evidence 与临时显示。它将已刊 R483 的完整 coast Bernstein 包围接入实际各层 metric/evidence，不把旧 source SHA 重新命名成新实现。

这是独立 request216，未来实际结论预留 R488。当前只有源码、条件证明和入口合同；未派发、未运行，未声明接受、速度或严格包围改善。相应证明为 [R487](../results/R487-complete-coast-three-level-incremental-refinement-composition.md)，本次 proof 身份为 17544 B / ed9bedf0bf679066e9118e17e1a050983ddfee1f7ab3369f602dfb031e4ee65a。

原 factory72c 的定义、数值 compiler、初点域循环、原完整 field/native/J/FD/full-DN/means 与全部原最终门不变。R483 只改善已实际进入后置 consumer 的准确目标 range 表达；初点域未决不能因此改写为已证。它也不重新计算 C head/1440/six，不改变固定 C 叶所代表的函数族。R489 等重算路线不在本入口中。

原 R464 union 是本次真实 M 路线，不能用 request207 的旧全 M 路线替代。三层 family 明确为 original112、resolution112、incrementalM。原 completeM 分支保在 evidence 的明确来源表中，但本入口不造该第四层。

## 2. 正式祖先与逐字绑定

原 request214 source 为 `29df28d35ef85a7c4a6474c28451c58d9f25c802`，其源与说明先发表于 `0e78e97fa380327094b85bd3413b1653ad60ef4c`。本入口没有读取它的运行中日志，不复用该 run 的实际状态或结论。

以下原文件是来源输入，各自仍保完整 bytes/SHA；新派生 dispatch 的身份另记，不能声称等于这些祖先。

|角色|公开相对路径|bytes|SHA256|
|---|---|---:|---|
|original205_subcontract|topics/visible-flex-larger-amplitude/notes/current-C-actual202-accurate-ten-closed-geometry205-request.json|97406|06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4|
|original205_workflow|.github/workflows/visible-current-C-actual202-accurate-ten-closed-geometry205.yml|95760|726d97e1aada5d34ddfa949753ce59c6909122d3de8c39bd5a2160fdb8712c36|
|original209_subcontract|topics/visible-flex-larger-amplitude/notes/current-C-actual202-incremental-M-refinement209-request.json|36220|aaf74021bbd952b24a3ba3d45b0cbbd1df070bf9866c79f6925808c836a74009|
|original209_workflow|.github/workflows/visible-current-C-actual202-incremental-M-refinement209.yml|96476|1c53b3c27ab531b99308150a7213e15d17717c57cff846b1dbffe0ffc9e5d65a|
|original212_subcontract|topics/visible-flex-larger-amplitude/notes/current-C-actual202-shallow-inverse-closed212-request.json|9965|8803750dbb21bcc24e0809e7bdc4389c567de9b8a10532d52b42b2f7a7ee30bf|
|original212_workflow|.github/workflows/visible-current-C-actual202-shallow-inverse-closed212.yml|99644|d1022e74a6217d582f08692b2458bb4d20a3a5dec61ba4dc88907a27e13c3cc0|
|original214_subcontract|topics/visible-flex-larger-amplitude/notes/current-C-actual202-shallow-inverse-incremental-M-refinement214-request.json|42062|c81530feca5c61e9a901937abf2e5c2704562f6eeaff0cbb70b817ec48519fe1|
|original214_workflow|.github/workflows/visible-current-C-actual202-shallow-inverse-incremental-M-refinement214.yml|97252|9ce8515103cae3388330bcabad08164a52a7d22d5e34ead248db5f26bba8565e|

已刊 R483 source commit 为 `3559e04efd5587989da5074b04cd825fe9694a89`，本次直接绑定以下三件。其公式与实际源均不改。

|角色|文件|bytes|SHA256|
|---|---|---:|---|
|helper|geometry_20261116_complete_coast_bernstein_enclosures.py|18291|3730c62b5c1a40fb594c9a2d9ed95a523a9134f12eb0b8def59c764d79e3edae|
|generator|root_20261116_complete_coast_metric_source_views.py|8742|d149d85103fd555908239f71f963b575a8197a210584d0b043b5d9415c106ae1|
|plan|r483-complete-coast-metric-source-plan.json|31012|7e71fe0cbff882060bb64b576f3b9e5f56fc6b548f97d1786587ad1bceef00d1|

R483 的说明与证明分别是 21663 B / 71e688828cad6937579d72584ba7e2e6213a05bcb59c8a555908249fc9c212c5 和 15453 B / d16119fda315a8aac2254375c83fbd548c5d4d414f08f33806b58df856ed03fa。本接口不把 R483 五个基础视图已经覆盖 union 作为前提；下文另有真实 union 视图及 caller 来源。

## 3. 本次八件执行/入口身份与发表位置

每个公开文件都小于 100000 B。实际文件正文以如下最终字节为准，不以中间草稿或缺少末 LF 的缓存为准。

|角色|basename|bytes|SHA256|
|---|---|---:|---|
|composer|root_20261116_request216_sampling_refinement_composition.py|35127|27974e73409589713f23f8e662a6ab5dbe335dd7e5286de293e93ade6f11bdf1|
|owner|geometry_20261116_request216_owned_roles.py|24276|16addc700e384c32d7eac3be0510f3af895722a26e177bf382720fe390af9fff|
|runner|geometry_20261116_request216_joint_refinement.py|49126|f6aaabac28084920c43ce2a1d726ca8414e172eaceb7099b9ac3c19ed6b34999|
|reader|root_20261116_request216_refinement_necessary.py|42414|0e90c355420fa2eb422fa80c93c03d1f7aa3ed3c0a86adaf1cc7207769eb9c11|
|generator|root_20261116_request216_coast_source_views.py|8787|560638a565b9cdccfff5d04a3412921c845b913da55d8ad38e905e33997d49c2|
|plan|request216-complete-coast-union-source-plan.json|43828|2f6e33df0ffd858f925cff2b2484ec00f06c2da7e456fef14f55dc432a06f676|
|request|current-C-actual202-coast-incremental-M-refinement216-request.json|57819|994c1f2ef39e27e793b977f913f84bee4f4c4406431e23da5dc7dcf716cbdd55|
|workflow|visible-current-C-actual202-coast-incremental-M-refinement216.yml|97966|bcb85d7399009698fac7cbbc34424ea28c73edc1927730302c3460dbc372baf8|

前六件发表到 `topics/visible-flex-larger-amplitude/computations/`。request 发表到 `topics/visible-flex-larger-amplitude/notes/`。workflow 发表到 `.github/workflows/`。R487 proof 到 topic 的 results，本接口到 notes。

本地交付目录是 `/workspace/visible-larger-working/request216/`。其中 `publication-files.json`、`diffs/` 和 `generated-review-only/` 是暂存交付/全文阅读材料，不是本批需要入 Git 的科学数据或额外运行输入；实际需要的完整源码生成计划就是上表中的 request216 plan。

outer schema：
`public-actual202-coast-Bernstein-incremental-M-refinement-and-displays-request-v1`，request_number=216。

composer schema：
`request216-original214-explicit-coast-refinement-composition-v1`。

owner schema：
`R487-request216-owned-nested-role-v1`。

joint runner schema：
`R487-actual205-contract-incremental-M-refinement-evidence-and-displays-v1`。

necessary reader schema：
`R487-joint-refinement-one-necessary-readback-v1`。

## 4. 完整 source closure 与实际生成顺序

原214的251个公开 pins 逐键逐值保留。新增9个公开条目是本次四个 caller、两个 source-generation 文件，以及已刊 R483 helper/generator/plan，因此 published_source_count=260。原15个R464视图保留，增加R483的5个视图与本次13个视图，因此 generated_source_count=33、complete_source_count=293。公开表与生成表同名冲突即来源错误，不覆盖旧文件。

原205实际派生 dispatch 的 source 表为195项：154原条目、三个当前metadata源、33个生成源、五个coast helper/generator/plan依赖。outer的剩余真实caller/历史来源另外绑定。195与293是两个明确角色表，不能把前者当成整个传递闭包的数量。原表曾保留的历史source仍是历史来源，不因出现在表中就冒称此次执行过。

### 4.1 原15个R464视图

原生成器是 `geometry_20261116_incremental_M_source_views.py`，42983 B / 68ae7071a4e41beedc1dbaea65f14f60e5e0fe0793a1b7f2daaacfd73f9b7bf7，schema R464-incremental-M-explicit-source-views-v1，receipt在 `source-views/source-view-result.json`。其15项完整输出清单保在 request.source_view_generation.expected_generated_sources，逐项与正式214相同。

这些真实视图提供当前 increment-M 的 Saved、radial、shared、Prefix、cuff、cut、cap、metric、reach/block reach、held inputs、native必要API、phase readout、evidence、display。不能把其本地review展开件当作公共下载文件。必须在这次实际 computations 目录先生成并核字节，才能供后续13视图作baseline。

### 4.2 已刊R483的5个基础视图

R483 plan/generator保持原样。其真实输出为：

|角色|生成文件|bytes|SHA256|
|---|---|---:|---|
|fixed|geometry_20261116_current_C_coast_fixed_query_complete_metric.py|51403|53a1e04bd1c28fc9e0430fbc2ced9d7e91870b2b610af9b29d8fd4a590aebd90|
|original|geometry_20261116_current_C_coast_live_query_complete_metric.py|56226|fb6f05cc505727401e165d2a65f6c5071b3b253f281f6ee84ef4b52b60aab535|
|resolution|geometry_20261116_current_C_resolution_coast_live_query_complete_metric.py|56258|37db784cada1a426eaf0aa59f04d10c1da0c3bdad4e1102c5e9712b1d1dfa61b|
|modes|geometry_20261116_current_C_M_coast_live_query_complete_metric.py|56210|44f5b66d59b35d35ff5e59da1496820fc23afb7b5c0430f2d4b2d6a31d54b25b|
|evidence|geometry_20261116_coast_fixed_target_complete_metric_evidence.py|62889|1d11359f03cd88b028c22201cef68a401fd9589a59718e813ac3cdc4c63461ab|

receipt目录为 `source-views-coast483`。其中 original、resolution、modes 三个 metric view 分别保持原真实 loader 族；fixed view 是原固定查询consumer的独立范围来源，本入口的实际三个post角色使用后文明确列出的 live-query角色，不能只因生成存在就声称它被科学调用。统一evidence的R483基础视图保其真实来源，union evidence另行派生。

### 4.3 本次13个R487视图

新generator schema：
`R487-complete-coast-union-three-level-source-view-generation-v1`。

其plan完整记录每一个baseline的basename/bytes/SHA、精确替换前后文字、唯一出现次数、生成输出身份、schema与帧。源计划是公开源码说明，不是大科学结果的编码。

|键|实际生成文件|bytes|SHA256|
|---|---|---:|---|
|union_metric|geometry_20261116_current_C_incremental_M_coast_live_query_complete_metric.py|56260|577a206b72456bedf54249350faa405ddef3e609fd2b385fdd3d207df62f6c46|
|union_evidence|geometry_20261116_incremental_M_coast_fixed_target_metric_evidence.py|63173|38cb0a67efe0fd2da358c569fff67e019a659a6c4e438b025d82dfdabb190f68|
|first_base|geometry_20261116_current_C_coast_ten450_original_or_refined_block_postsolve.py|67003|c2a9399489aa8bc66098a6bee1977faad7ac6a02735a294772e5e1aaddb3f751|
|first_post|geometry_20261116_actual202_coast_ten450_parameter_block_postsolve.py|27101|5660378eed3f8c308c5765370e6521beefb46e7620e9e10240796fb203a35e74|
|first_reader|root_20261116_actual202_coast_ten450_parameter_block_postsolve_necessary.py|11054|81d810566362dd7b8b307c378b94a26f423dd1ba2aff4cfed0f45b12b6e304af|
|first_held|geometry_20261116_actual202_coast_ten450_parameter_block_postsolve_held.py|5609|eb13fc3039c4751149e5638807c7aae98e564da2cd27522bf1750be361c98873|
|orchestrator|geometry_20261116_request216_actual202_coast_closed_postsolve.py|47243|a22d0bca225407702ecddf91991a59955008b8a3696232160a24bffa13861fd5|
|resolution_post|geometry_20261116_current_C_same_far450_coast_postsolve_geometry.py|65740|3f0c4eb314528a07029b11c4f2fb3fb590da3506471ad70195aefcd5aed78454|
|resolution_reader|root_20261116_current_C_same_far450_coast_postsolve_necessary.py|27459|02ea18ab6dce352c28332205cfc87a2d6927d864c730b665f36726c814936444|
|resolution_held|geometry_20261116_current_C_same_far450_coast_postsolve_held.py|44092|653e6039fe79012575442678fc420015bbc87664fdcc121d165e6f85ad5cf8c1|
|union_post|geometry_20261116_current_C_incremental_M_coast_postsolve_geometry.py|71899|419638c896ef6e14bc8b6faf937224545ed52fa48e42974cbca7dabe09c9d135|
|union_reader|root_20261116_current_C_incremental_M_coast_postsolve_necessary.py|27491|6d2026f288edbb504f20a49edf58d41e9342e9dd5ba35c854f329a9353f6fb15|
|union_held|geometry_20261116_current_C_incremental_M_coast_postsolve_held.py|44204|c99c7f58a451c12d229ef79ca02fdb610b61c6e81cb30361f50e5c6d55691466|

新generator与原两generator都写实际 checkout 的 computations；所有目标必须原先不存在。不会改原文件，不用一棵缺少传递依赖的private导入树，也不把执行文件的HERE仍指回旧source。receipt目录为 `source-views-coast216`。

完整13个生成文件的相对baseline差异在本地 `diffs/thirteen-generated-views.complete.diff`，52388 B / 582e443b315bd2a05849629cfc8d0090044229cb292060e232c799ec8f397fbb。各单件完整diff也在同目录。它们仅供全文核读，未来执行由实际plan/generator复现相同源码字节。

## 5. 初始化、生成、原正常源码步骤与科学启动

workflow保持原唯一namespace：
`visible-current-C-actual202-ten450-closed-geometry205`。

deadline schema仍是：
`request205-owned-job-science-deadline-v1`。

其中205是冻结子合同和真实目录角色，不是声称新job属于历史205 run。当前run/source来自实际 Actions 环境；所有回执分别记录当前outer216与原205/214文件身份。

实际顺序：

1. composer `initialize` 绑定outer216、正式214及原205/209/212合同，建立本次唯一原namespace/owner/clock。生成 `request216-derived205-dispatch.json` 与 `request216-composition.json`，新字节与祖先身份分列。
2. 原Python/Node环境安装、数值包安装、临时容量记录保持原流程。
3. composer `materialize` 在原时钟内先绑定全部260公开源，再依次调用R46415、R4835、R48713三个真实metadata生成器。不会在本地运行这些步骤。
4. 三次实际生成的stdout/stderr、退出值、来源和进度写到 `source-materialization216/result.json`。完整成功后进一步核全部33个实际目标文件及各生成receipt。
5. 原派生dispatch的源码绑定和正常Actions语法步骤看到195个实际source文件；之后新owner.prepare绑定全293项，保原additional-source正常Actions语法操作。
6. owner.prepare将实际结果写在 `source-preparation216/result.json`；新reader.generation读取同一路径。此前草稿遗留的214目录已经修正，并级联更新本接口中的reader/request/workflow身份。
7. 原科学步骤和新后置caller才按原控制流启动。缺source或准备失败不伪造科学完成。

composer CLI沿同一标准库入口：
`initialize | materialize | prepare | verify | readback`，各自显式 `--request --request-sha256 --base --computations`；实际所需附加参数以已冻parser和workflow为准。通常无需用户手填这些命令，workflow已经逐步绑定。

新generator CLI：

```text
--computations ACTUAL_CHECKOUT_COMPUTATIONS
--plan ACTUAL_REQUEST216_PLAN
--plan-sha256 2f6e33df0ffd858f925cff2b2484ec00f06c2da7e456fef14f55dc432a06f676
--out FRESH_NAMESPACE_SOURCE_VIEW_RECEIPT_DIRECTORY
```

公开生成器只读取源码文本、执行确定替换和核byte/hash，不导入目标科学模块。原Actions普通AST/node语法操作只在未来运行实际文件后执行；作者没有在本地执行/import/AST/compile/fixture。这是原启动合同的正常来源/语法步骤，不是新数学接受门或额外审计job。

## 6. 原205派生合同的精确差异

正式205原request仍完整字节绑定为06ae0670…；本次实际派生对象单独SHA。composer根据明确可变字段形成并核回原始对象，不能以“same schema”略过实际差异。

沿214已存在的变化为：sampling inverse depth 24→2；原value32、1M work上限、其余原采样/求解参数全部保留；当前R477必要reader；当前workflow/来源图及metadata收据。216在此基础上新增实际generated sources与coast caller角色，首闭面 postsolve block 的schema/runner/reader/held/orchestrator使用上表实际新文件。

composer还绑定原214的execution、refinement_work、source_view_generation、witness、mode proof、旧source/exact合同、display/family及原README pins。原251个公开pin不删除、不变更。old held_source_contract另保为original214_held_source_contract，新实际held来源与新roles严格一致，不能用旧held身份作当前记录。

实际first closed postsolve仍依赖原真实BVP返回；coast包围不是求解前门。所有首native/field/fullDN/FD/338混合J/双mean和原最终判据原样，未接R466/R471/R474新native算法。R493后续live响应研究不属于本入口。

## 7. 三层真实caller与数学输入

### 7.1 首层

原205双阶段真实453→450及其checkpoint写入不变。新first orchestrator调用本次首parameter post、necessary和held三元组；其内部base改为实际coast metric view。首A/B参数策略仍准确pin：

完整SHA直接取 request.coast_implementation_contract.first_A_B_policy_source_sha256：

`b49769f13f69bf30b82988b1ca57382c602d4b74bc3ae8a6c2b5d1e0ee3df7a8`。

首物理场、原cut/atlas、shared与reach生成都属于本场；metric的coast range没有转移旧场几何结论。

### 7.2 同远端族精化与增量M

下列真正求解/owner/材料/显示源均保持原冻结字节；它们不是新R487算法。

|角色|basename|bytes|SHA256|
|---|---|---:|---|
|same_far_owner|geometry_20261116_current_C_frozen450_same_far_owned_launch.py|58629|1a1df5136492abe5066a91139bd22554f8e83db21d13c981439532911f4b3c8d|
|same_far_reader|root_20261116_current_C_frozen450_same_far_necessary_readout.py|36696|59ed4273ca45c93931c6e6786adc87b4bd4fabf94f036e97e230a73687f7b596|
|modes_owner|geometry_20261116_current_C_incremental_M_owned_launch.py|77960|f372081797276ed3bc6c061f91febd97dfad70b742c34d10a9df5ae642a04078|
|modes_reader|root_20261116_current_C_incremental_M_necessary_readout.py|33447|602c9abd38a3fa7a7fc590a964139a4f4bf8186403da208583e4472d712bae8e|
|common_material|geometry_20261116_current_C_incremental_M_common_material_phase.py|38717|50bf2d04e5e4e505fad6f0ece5a896364bb94c25c9530d6a1e7c2ceef3aec923|
|display|geometry_20261116_current_C_incremental_M_multitime_display.py|41727|e0b47bbfd355032bb433302425d09a4e6be0413107e20ac3d96e7c52586e88cf|

R456保同实际C、root族、far、mu字和全112族，只对新的物理网格作实际采样与完整450求解。第二层五factor2的真实父只能是本次首层返回；未返回时保相应suffix。

R464第三层只在真实R456 accepted checkpoint存在时继续，M=128，四factor1保留已精化计数，旧112族复用与新增模态全计算由原R462/463/464来源支付。新的metric/evidence使用其实际Saved/Prefix/原M数组布局，不伪112标签、不补零当新增模态。

每层postsolve仍按原五角色执行 radial、cuff atlas、shared、metric、block reach；held为独立原role。只有metric子角色切到本次明确包围实现。所有其他源、大小、schema通过其本来真实字段绑定，不泛化allowlist或省略完整C/field receipt。

### 7.3 固定完整闭面

首实际A/B、W、cap_height、marker全部字值、材料图与transport、尾帽/归一化解释必须保同一真实construction。当前core的材料Phi不能因十词相同就被忽略。原common_material源码是上表50bf…，R487没有重新选择首B，也没有用“共享参数”替代原完整closed-target signature。

依赖first B的测量若输入缺失，明确该role unpaid；B缺失不加成BVP/refinement/held新拒绝。各层shared或atlas缺失同样仅按实际角色范围处理，不从源声明补造数据。

## 8. coast目标range实际范围

R483 helper读取当前原factory72c完整定义，保全部十参数、所有支撑、准确总长与实际分片区间。原固定C叶盒保持原值，深根选择与全族量词不变。负速度coast的三jet使用

$$
a=A-\kappa\ell t+\ell^2P(t),\quad
a_s=-\kappa+\ell P'(t),\quad
a_{ss}=P''(t).
$$

半径的双变量Bernstein完整27系数；speed对完整ell两端点各完整8系数；二阶导完整7系数。interval含准确实集合的条件证明见R483与R487。不同系数间相关性丢失只放大，不能据此断言范围最紧。相同C语义叶的有限盒并未被该重写收缩；这不是C query重新积分。

实际Prefix.inspect内使用局部range adapter，不改target对象或原module全局。所有不匹配结构及非coast分片原路径仍在；端点、支撑外零、可能分片闭交与hull保。原定义中S1和前两个支撑端点为recipe准确rational常数，故实现的支撑排除不会因把同一宽C盒自比较而恒退回。

helper metadata描述实际factory/definition/C绑定、当前实现及工作计数；counts不是完整覆盖证明。新evidence的每层actual_prefix_range_work也只是实际工作范围，不把它当initial-domain certificate。相同输入允许得到相等或更宽结果；完整domain是否支付仍靠真实原严格谓词与实际覆盖。

## 9. evidence、t网格与临时显示

统一实际evidence源是13表中的union_evidence，schema：
`R487-fixed-target-incremental-M-coast-Bernstein-metric-evidence-v1`。

原measure/compare/readback CLI形状保持。三层family依次original112/resolution112/incrementalM；统一source的completeM分支仅为已有显式相容族保留。各场的actual_job_deadline、fixed_closed_target_signature、members与complete_coverage_and_pending原身份、actual_time_grid、必要current frontier都继续读回。

compare仍返回原SERIES实际完整必要字段，包括level_count、actual_common_target、actual_common_original_clock、fixed_closed_target_signature、levels、consecutive_comparisons、all_complete_upper_envelopes_strictly_decrease及all_real_sup_strict_decreases_proved。某measurement没有result时不能伪造compare成员。全域upper、真实lower、全相位transfer、有限t点与共同目标绑定分列。

t subdivisions分别4/8/16；四共同witness为prefix u=1/2，q=0与1/4，各上下side。真正的每个k/n均由原evidence执行；其嵌套关系不能给未算点填数。measurement_width_goal与metric_reference_eta是原work/reference参数，不是新solver门，不把原RMS/native/BC阈值误当相对metric floor。

显示沿原R464 display，不改其科学/显示区分。每层times分别[0,1/2,1]、[0,1/4,1/2,3/4,1]、[0,1/8,…,1]；grid为prefix8、tail8、cap4、angular32；physical-angle-image模式，单文件严格小于5MB，raw仅临时。每个frame原状态/文件身份/误差最大值/未完地址保必要读回；完整顶点数组不传Git或拆包。有限显示图不是reach/metric或拓扑接受门。

## 10. 原时钟与全部资源参数

所有工作共享本次原205唯一namespace开始时间和原deadline。science18900秒、readback/关闭2700秒、总job360分钟，terminal measurement/close reserve900秒。三个generator与其source binding也计原elapsed，不新开钟。

|阶段|固定上限或参数|
|---|---|
|R456 sampling/full450|900 / 7200 秒|
|M128 deep/sampling/fullM|300 / 12000 / 7200 秒|
|每层radial/atlas/shared|600 / 120 / 300 秒|
|每层metric/reach|600 / 600 秒|
|witness/held/measure/display|120 / 300 / 300 / 120 秒|
|comparison|120 秒|
|child shutdown reserve|30 秒|
|start free / stop free|8 GiB / 2 GiB|
|max_nodes|2400，保全部必需并集，资源容量不是新门|
|measurement bits/sqrt bits|256 / 128|
|angular depth / max depth|2 / 20|
|max cells / phase cells|100000 / 100000|
|max inverse steps|80|
|measurement width/reference eta|1/100000000 / 1/1000000|

各阶段上限真实裁剩余，不是逐项相加的承诺，不把原总钟扩大。原C查询11参数、首closed work和精度沿214→205，request.refinement_work原字典保持。旧节点和所有knot必须全保，不能为2400“容量”任意丢点。若真实parent/输出不齐，独立role按原依赖记未起，后继不恢复已删旧SHA数组。

## 11. 单份必要读回、源准备失败与quiet

链摘要仍单对象≤90000 B；超限真实exit70，不拆分、不压成字段编码规避、不截断后称complete。科学完成、transport完成、actual owner静止三者独立。

独立source composition纯metadata readback沿原214的require(len(record)<=90000)；该scope超限是ValueError/exit1，并非70。原其余scope保其本来退出逻辑，本接口不把全部必要scope统称70。任一必要读回失败均不能生成相应完整marker或授权最终清理。

当前source-generation aggregate保current_generation/generations/error、实际receipt与公开源码SHA。prepare实际目录已修为source-preparation216，reader按同目录读。source生成中断、未写receipt或原语法失败时，原always读回仍可记缺失/错误；不能仅凭预期33项构造完整receipt。

first-chain当前R477读者保原8个采样point/stack字段。chain读者保各actual process、source/context、全部原必要native/FD/trial与未返范围、geometry/held/evidence/display的实际必要对象。大ledger仍仅原身份，不能把它表述为所有科学行正文已经返回。新元数据增加不提高90K限，未知实际错误体可能导致运输partial，不能在派发前承诺必合限。

source composition是一个独立纯metadata necessary帧，chain引用其identity，不再复制该完整body。reader引用同一来源身份只在canonical严格一致时，不拼造科学值。generator stdout/stderr原文件保身份与实际错误，未确认的生成后缀保持未确认。

最终清理需要原所有必要readback步骤、composition、首closed和新chain的实际完整marker，以及原/新所有owned role真正quiet。实际PID、start-time、process-group/session与已reap子记录继续原政策。不能确认quiet或必要读回失败则不删；明确removed=false及缺口。源生成失败不产生清理授权，不能把文件不存在当已正确完成。

当前新增必要帧：
`BEGIN_REQUEST216_REFINEMENT_NECESSARY` / `END_REQUEST216_REFINEMENT_NECESSARY`。
composition帧：
`BEGIN_REQUEST216_SOURCE_COMPOSITION_NECESSARY` / `END_REQUEST216_SOURCE_COMPOSITION_NECESSARY`。
首closed的新marker：
`request216-coast-closed-postsolve-readback-complete-v1`。
workflow report与reader使用相同实际帧；各原初始科学必要scope保持本来的帧与严格区分。

## 12. 完整差异与最终交付

本地diffs包含：

- composition/owner/runner/reader分别相对正式214的全文件diff。
- request/workflow分别相对正式214的全文件diff。
- 新generator相对已刊R483 generator的完整diff。
- 十三个生成view各自相对实际冻结baseline的完整diff及合并稿。
- source-preparation路径修正的最后小delta，明确reader唯一目录和两级SHA同步。

审阅不需要重新运行旧摘要或生成额外fixture。已完成的工作仅为文本来源/字段核对、完整source/patch字节身份和条件纸证。没有在本地执行科学、import目标模块、AST、编译、数值对拍或任何新单元门。未来Actions的原source/语法/完整科学流程已经在workflow中具体调用，而不是留下不被调用的一组函数。

本入口不把后置包围改善冒初点域证书，不改变原有限trace/native算法，不让metric/held成功成为新的精化前门，也不承诺三层足以使完整误差达到机器精度。真实完成、严格反证、unresolved、未起和资源/工程/运输失败均由未来R488按原记录承担。

本批只有上表八件与R487 proof、本接口共十个公开文件。scratch manifest、完整diff和review展开源不作为科学数据额外归档。所有源单件<100KB；不复制原251文件，不将生成的33个完整视图重复入Git。
