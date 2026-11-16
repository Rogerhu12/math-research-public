# request235：完整来源生成、原精化科学与必要读回接口

**可信度：已证明（限完整固定来源、确定性文字构造和实际 Actions 的原控制流条件）；未执行本入口的科学计算。** 这是一份完整可调用入口合同。实际 request235 的结果归 R560，本文不预置实际run/head、接受状态、误差下降、原生成失败已修复的实测结果或清理完成。

作者：OpenAI / ChatGPT exact_refinement（AI）。日期：2026-11-16。条件证明见 [R559](../results/R559-actual-source-engine-interface-and-complete-generation-readback.md)；实际来源停止见 [R546](../results/R546-actual230-source-materialization-stop-and-complete-returned-scope.md)。

## 1. 原因、最小变化及现有科学范围

actual230在来源生成索引6停止，六个前序来源层返回。它没有启动完整C及后续数学链。原必要正文没有返回该层完整子异常，故本文只把原 `ValueError` 与生成位置归作实际记录。对固定源码的单独结论是：旧生成器读取冻结R496引擎不存在的 `module.HERE`；该引擎的真实接口是自身文件路径以及 `main` 内的 computations/workspace 检查。

本入口改为核真实 `module.__file__`。冻结引擎和49项当前scientific source计划原字不变。另增加一个公开的生成必要读回命令和一个公开cleanup委托护栏，使下游生成文件缺失时仍能报告真实未到达/错误/skip。入口保持R544对原native argv和闭面ENTRY的修复；不删除原guard，不复活旧未付raw。

初点仍为原明确R503 coast-base参数，沿真实准确C完整头、全部query/cut/deep112、全部far及真实径向点，完整453→同点450；随后原完整闭面/held、五factor真mesh、M128 union、全部新场geometry/metric/reach/held/common material、nested t与临时显示都保持。same-C额外八个数学角色仍是冻结的request230来源。新增文件只承担源码生成、来源绑定、相同科学编排和必要返回，不引入R556并行far或任何新的native算法。

## 2. 公开文件和容量

下表是全部六个运行发布件。主题内路径相对 `topics/visible-flex-larger-amplitude/`；工作流位于仓库 `.github/workflows/`。

|角色|文件|字节|SHA256|
|---|---|---:|---|
|generator|computations/root_20261116_current_C_actual_engine_source_views.py|16553|e094576644fc7a048de8f47af02b49aab776162a66de538e21b044326df936dc|
|composer|computations/root_20261116_request235_sampling_refinement_composition.py|74598|090f33c586fd3667c2cb630ad364d83c8b1a52cb2298a43813db3fbfc209b5c7|
|entry|computations/root_20261116_request235_actual_source_entry.py|35660|fafe3ec5306b252e9189a39f8a5f82491c1bb54cc868e7304fb39222d2683fe8|
|metadataPlan|notes/request235-complete-generation-metadata-source-plan.json|90706|a13eca1ca47d21ba5f5afc42fecd4a6e9d0d9794f21bf961cd570edc7db93913|
|outer|notes/current-C-complete-generation-refinement235-request.json|40569|35c1e4230d5ae9b48157d280028cc5f364113a00b2df1041b2193087fe6d4378|
|workflow|.github/workflows/visible-current-C-generation-complete-refinement235.yml|91176|a65d73cbb8f974c8d7a3e9e6e6a29d846877a84999c516b506019865674ab5d6|

另公开两份正文：`results/R559-actual-source-engine-interface-and-complete-generation-readback.md` 与本notes接口。**八个正式文件**以外，完整diff、source展开、交付manifest都不入Git，也不保存科学原数据。

五个主题内运行件共258086B；工作流91176B单列，不计topic。R559证明19949B；本接口27279B；本批topic净新增305314B，含工作流的全部八件共396490B。每件<100000B。仓库当时剩余空间由发布者按真实树元数据另核；不会删必要字段、编码payload或提高单体上限来适配容量。

## 3. 当前请求、内部祖先与实际路径

外层请求：

- basename：`current-C-complete-generation-refinement235-request.json`。
- schema：`public-current-C-same-semantic-head-bound235-request-v1`。
- request_number：235。
- workflow：`visible-current-C-generation-complete-refinement235.yml`，支持原push范围和 `workflow_dispatch`。正式发布/dispatch由主控独占；文件存在或push标签不等于运行。

实际内部来源合同：

- schema：`public-current-C-bound235-coast-base-source-closure-request-v1`。
- request_number：235。
- 仍存于工作视图中的原220合同pathname。这是路径兼容，不是旧220请求原字节，也不是旧run。
- 完整字节只在本次Actions由固定repaired222对象和明确新source映射形成；实际bytes/SHA记录在 `source-binding235/result.json:actual_derived_request`。没有提前填一个未来哈希。
- 后续全部inner caller读取 `REQUEST235_CURRENT_INNER_SHA256`，不能拿frozen220的99218B/f6ca…、repaired222的99330B/2d1c…或旧230actual值替代。

唯一namespace：

```text
$RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205
```

唯一新工作视图与env：

```text
$RUNNER_TEMP/request235-runtime-metadata-workspace
$RUNNER_TEMP/request235-runtime-env.sh
```

entry先记录 `source-binding235/namespace-start.json`，再读取/复制/形成来源；所有准备计入同一原namespace起点。原checkout里的220/222/230来源文件保持原字节。新工作视图普通文件来自该checkout，`.git`关联真实对象库；entry不移动branch/ref或修改原checkout。source env显式导出实际 `GITHUB_WORKSPACE`、`VISIBLE_COMPUTATIONS`、`VISIBLE_BASE`、两个REQUEST235工作目录和真实inner SHA，并cd到实际视图。GitHub保留变量不通过 `GITHUB_ENV` 假写；每个实际run块显式source该脚本。

内部原路径 `request220-derived205-dispatch.json`、`request220-composition.json`、`refinement220-request.json`、`refinement220` 保留其原caller合同。里面的actual run/source、当前request身份和source map都是真235形成值。祖先文件名与本次完整对象身份必须分列。

## 4. 完整来源545项及生成顺序

原535项逐值保留：原293public＋242generated。新增4public＋6generated后，当前297public＋248generated＝545。没有用新name覆盖旧pin，也没有把历史生成输出冒成Git公开文件。新JSON计划只是有明确用途的公开元数据，仍按原source-only分类，不交给源码专用解析器。

九层依赖顺序如下；前六层和其179个输出均原字不变：

|索引|来源层|输出|receipt目录|
|---:|---|---:|---|
|0|R464 union-M原完整来源|15|source-views|
|1|R483完整coast range|5|source-views-coast483|
|2|R487完整三级coast消费|13|source-views-coast216|
|3|R496 zero-linear native|49|source-views-native496|
|4|R498完整gzip|51|source-views-gzip218|
|5|R503完整coast-base政策，保原222分类修正|46|source-views-coast-base220|
|6|新R559真实引擎，历史217八件＋当前R544四十九件|57|source-views-binding235|
|7|原230六个metadata输出|6|source-views-metadata230|
|8|本次235六个metadata输出|6|source-views-metadata235|

当前source准备父目录为 `source-materialization235`。索引6的真实producer为公开新生成器，schema `R559-complete-current-C-binding-source-generation-v1`；它仍消费原R544完整49view plan及原historical217完整plan。历史R544生成器留在public闭包作祖先，本次不再调用其缺失属性接口。

所有literal基线、出现次数、目标bytes/SHA、schema和真实输出位置都检查；对新输出只独占创建，不覆盖旧源。现有Actions源码语法检查保留。这里没有在本地运行导入、AST、编译或科学求值，也没有新增数值对拍门。

本次新metadata输出如下。它们真实写在同一 `VISIBLE_COMPUTATIONS`，不公开展开副本：

|角色|生成basename|字节|SHA256|
|---|---|---:|---|
|owner|geometry_20261116_request235_owned_roles.py|25728|20f0d82f0fa576292a1ae9d3ddbae889f806d210aa7b42d7c541514996f609c0|
|runner|geometry_20261116_request235_joint_refinement.py|48824|4f467b928ae8ef11c50f56884a858c8769409a2805ca52cdbdea7b5d6c73b75a|
|reader|root_20261116_request235_refinement_necessary.py|44534|53254693871d728d04efd7d20500e3d633f77e230281d76c3c8631021cec5afb|
|same_composer|root_20261116_request235_same_C_composition.py|29444|6ff55739b0c0855dea5af1f3f5deed4983c050ab06242cf666a1b107a749fb29|
|same_runner|geometry_20261116_request235_same_C_refinement.py|45658|694826d1927ad70d1f6c908f1c7640cd8f4dafe7321e4fe28c7e2470ffadd07d|
|same_reader|root_20261116_request235_same_C_necessary.py|35746|8608d163d22a28ee5381f68b837fc41dcae4deeb3cced7bc43b44160ca830f51|

这些调用者相对于原230版本的更改仅是实际235producer/schema/pin/路径、生成必要scope接线及当前读回/清理接口。原科学阶段体、参数和成功谓词保持。原230六件也由其固定计划真实生成和绑定，因此新的六件不是省略祖先后假称原535完整。

## 5. 八个same-C数学角色保持冻结来源

新的same-C runner/composer/reader schema使用235，但以下实际数学源与自己的schema/frame仍明确是request230来源，bytes/SHA不改。它们在新run中运行时继续记录该run/source；没有拿旧230的数值结果作为输入。

|角色|实际生成basename|字节|SHA256|
|---|---|---:|---|
|head|geometry_20261116_request230_same_C_full_head.py|42314|a46fb5c36dc0304dbd71e6ddf054b72551a08d2116e36f0453c9f02b546f6739|
|leaf|geometry_20261116_request230_same_C_leaf_target_cut.py|35531|ffc7e77bff220b1b046cd831bd99eddc5aa4e586eb4a09afab3c9705331c494d|
|bridge|geometry_20261116_request230_same_C_metric_family.py|12376|2db28f661562836dbe253130c01b7975881c07958f686a7df418c6377ece05d6|
|tail|geometry_20261116_request230_same_C_tail_queries.py|29686|613a4054d84347f1bd367919dfb1fb174655b4ef54929d754e7537b74117a4cc|
|metric0|geometry_20261116_request230_same_C_original112_metric.py|57273|486fbd45dd419c8b430a972b974b018df725e8c184aef42f9566c5964a4b9eba|
|metric1|geometry_20261116_request230_same_C_resolution112_metric.py|57300|fd020ca0e92e4c6d8dadaca495255fdf74498a5824137f2788f9bcb78c83edc6|
|metric2|geometry_20261116_request230_same_C_incremental_M_metric.py|57465|de2683e5f9a3f5dbf76881f7429c6631c1a493bf00881a47160b6dc7feb1e8b7|
|evidence|geometry_20261116_request230_same_C_metric_evidence.py|65329|a95af2e6c240ef920a6fb8cd730f82812acb2d6e4a28d76a4cfe9a5e0c3039d6|

`same-C235-source-views/result.json` 是当前登记receipt，不重复生成这八件。它绑定真实 `source-views-binding235/result.json` 及当前545来源，而不是因目录名有same-C就声称源已形成。

保留的数学链为：R489同准确C完整1440头/六primitive重算、R492同语义叶与cut、R495对应actual field loader、R500由新头回答完整tail E(r)查询、R504全metric/evidence与实际family注册。原有效粗界在新查询未付时保持；新的cut交集不变成中点参数或新场。没有新声称whole-tail Er/Err已收紧，也不以仅盒变窄改变同一场的真实误差。

真实阶段名称保持八项：

```text
head_recompute
level0_metric
level0_measure
level1_metric
level1_measure
level2_metric
level2_measure
compare
```

first slot在真实首shared及其原必要读回之后、原联合精化之前。successors slot在真实mesh/M及其各自几何/evidence/display返回之后。缺少真正字段或父返回就记录相应未付/未起；没有把source准备完成当字段存在。level0/1/2分别使用original112/resolution112/incrementalM实际family，同一compare使用相同evidence源码/schema。

## 6. 真实CLI与调用责任

下文 `OUTER` 表示实际工作目录中的235小请求，`INNER` 表示同视图原220 pathname内本次形成的完整235 inner，`BASE` 为唯一namespace，`COMP` 为实际computations。两个请求身份不能混用。完整可复制命令和原所有step参数均在发布workflow；下表给每个真实CLI责任。

|实际源|命令/API|请求与用途|
|---|---|---|
|公开entry|initialize|外层235；建立唯一起点、形成当前工作视图/inner/dispatch/原deadline|
|公开composer|materialize|真实inner＋实际SHA；顺序执行九层完整来源生成|
|generated same-C composer|bind / preflight / prepare|外层235；绑定当前actual inner，执行原完整PYPINS，再登记8same-C源|
|generated owner|prepare|真实inner＋实际SHA；绑定297public/248generated和原owned环境|
|generated joint runner|原rules/run与原role调用|真实inner，执行原完整mesh/M/几何/evidence/display|
|generated same-C runner|rules或run，--phase first或successors|外层235，8个真实same-C阶段|
|公开composer|generation-readback|真实inner；独立读取来源生成必要scope，不导入生成科学reader|
|公开composer|readback|真实inner；原完整composition具名关系必要scope|
|generated refinement reader|readback / component / cleanup|真实inner；原全部精化来源与原9outcome清理合同|
|公开entry|readback / cleanup|外层235；actualsource准备必要scope；经原完整条件委托|
|generated same-C composer|readback / cleanup|外层235；same-C来源必要scope与原清理委托|
|generated same-C reader|无额外operation，真实3outcomes|外层235；全部8stage必要正文、原owner quiet、marker|
|公开entry|guard-cleanup|外层235；生成文件尚缺时可读地报告skip，正常时委托原链|

共同必要参数为 `--request`、`--request-sha256`、`--base`、`--computations`。same-C runner还须 `--source-topic "$VISIBLE_SOURCE_TOPIC"` 与 `--proof-directory "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/results"`。`VISIBLE_SOURCE_TOPIC` 是原恢复步骤的真实来源目录；不能改称另一未定义环境变量。

例如，独立来源生成读回的真实形式为：

```bash
source "$RUNNER_TEMP/request235-runtime-env.sh"
python -u "$VISIBLE_COMPUTATIONS/root_20261116_request235_sampling_refinement_composition.py" generation-readback \
  --request "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/current-C-coast-base-zero-linear-gzip-incremental-M-refinement220-request.json" \
  --request-sha256 "$REQUEST235_CURRENT_INNER_SHA256" \
  --base "$VISIBLE_BASE" --computations "$VISIBLE_COMPUTATIONS"
```

发布workflow在这条命令外显式裁原21600s总namespace剩余、上限300s；例子不另起钟。same-C必要reader的三个原参数是 `--prepare-outcome`、`--first-outcome`、`--successors-outcome`，取实际step outcome，不推算。公开guard另收 `--new-composition-outcome`、`--new-readback-outcome` 和 `-- cleanup ...` 原完整后缀；它不能自行忽略后缀或直接删namespace。

原222 PYPINS全文19255B/cc39da8308e718f4b755670730d855c204c0785a9ebb21b025b62868cf1b0281仍作明示祖先。当前preflight只按新真实inner、composer、545计数及真正235workflow路径重绑元数据；全部原scientific断言保持。旧222原block检查的是旧220workflow，这一点不被本次回填为它已检查过235。

## 7. 科学与资源参数保持

本次不重写原source math。全部初始输入、准确十词、完整C/root族与原query语义由当前inner和所有固定source保持；旧run任何已付域或native结果均不转移。

|责任|本入口保留值或范围|
|---|---|
|唯一科学计划|namespace起点＋18900s|
|必要读回预留|2700s；job360min|
|首C|原完整1440 ordered head、six primitives、全部原query/cut|
|首deep/far|全部112模式、全部候选与原实际rFar/μ、原数值行选择与全momentum消费|
|首点采样|原浅inverse深度2、value32、1M工作限；所有实际点/原完整未访|
|完整解算|原full453后同点frozen450，全部native/J/FD/原final predicates|
|精化|真实R456五factor方案、随后M128 union，原全部新场几何/独立held|
|原startup与停止|32GiB原startup要求和原资源/owned stop，不降低|
|新来源必要scope|每次最多300s且裁原21600s剩余；不重启科学钟|
|same-C头总段|1800s＝1650head＋120cut＋30shutdown|
|same-C每metric|240s|
|same-C每measurement|300s|
|same-Ccompare|120s|
|原末测量/关闭预留|900s|

原deadline字段明确不是对全部前置步骤重新施加一个全局绝对kill；实际phase仍由原caller/owner及其本来剩余裁剪控制。生成准备耗时计入原起点；即使新工程接线正常，也不保证原有限job能完成全部精化。所有未开始后缀、实际超时、异常、每个未付科学范围照原返回。

same-C head参数：precision384、integral absolute128/relative112、guard8、evaluation_limit100000、value_width32、max_depth48、query_depth16、max_panels400000、max_query_nodes400000。measurement：interval256、sqrt128、initial angular depth2、max_depth20、max_cells100000、width_goal `1/100000000`、reference_eta `1/1000000`、max_inverse_steps80、max_phase_query_cells100000。后二者及width goal是原工作/报告参数，不是新的BVP接受门或metric floor。

live C query参数：precision256、absolute128/relative128、guard8、evaluation_limit200000、value_width80、integral_depth40、inverse_depth40、max_panels100000、max_nodes200000、budget900。三个时间划分4/8/16；四个witness均为prefix公共u=1/2，q=0或1/4，各upper/lower。全时域责任来自原准确共轭与全域测量，有限t点只按原实际工作记录。

没有原metric/reach成功或first-material B前门；缺B只使依赖它的测量未付。新metric/evidence返回partial不能被格式化器改为科学失败或隐藏后继原可做工作。原whole field Hermite/ODE/material/两帽/反射/全角定义不改，细化包围不会让同一准确场的真实误差sup自行改变。

## 8. 完整生成必要scope的数据合同

公开 composer 的generation-reader schema为：

```text
request235-current-C-actual-source-composition-v1-generation-necessary-v1
```

单body frame为：

```text
BEGIN_REQUEST235_COMPLETE_SOURCE_GENERATION_NECESSARY
END_REQUEST235_COMPLETE_SOURCE_GENERATION_NECESSARY
```

body保留本次repository/run/source、自身source、实际inner identity、实际computations、完整父materialization identity与原record、九层original结果/当前内层结果/原error/frontier、完整stderr和读错。每层独立保 `actual_parent_return`、`control_flow_scope`、原缺失标志、生成器/plan/receipt目录及实际观察计数。

全部248声明地址按原计划次序用固定四列：

```json
["basename","actual_bytes","actual_sha256","matches_declared_identity"]
```

不存在为 `[basename,null,null,null]`。真正读错另有完整错误和地址，不把不可读当不存在已证；匹配false不改称缺失。该固定表只承载源码身份，既不把科学数组转编码，也不以原哈希替代未来原件。

五个具名重复来源字段 `outputs/generated_sources/original_sources/required_public_sources/historical_stages` 各保原type、item_count、canonical_selected_bytes、canonical_selected_sha256；完整原result identity另保。其他原成员原样返回。这个必要scope明确不是完整original result重构；没有声称从identity可以恢复其正文。原科学样本/账本不属于这五名，本reader不读或缓存科学数组。

父已进入某层而无returned项时，仍读取该索引真实stderr；新引擎原stderr文件存在而原reference未返时，也有显式 `original_result_reference_returned=false`。完整源/结果读取核真实路径、非symlink、前后stat及字节身份。所有errors保持原字符串及traceback，既不缩成512字符，也不按count掩盖未到达。

关键分责：

- `source_generation_completed` 只取本次父真实completed。
- `complete_necessary_readback` 只在所有实际必要读取无错误时为true。
- 文件不存在可完整记录为不存在；不能据此说它已生成。
- unknown或未到达不等于科学未通过；所有后续科学范围由各自原producer返回。
- `immutable_source_metadata_only_no_process_quiet_claim=true`、`scientific_modules_imported_or_evaluated=false`、`raw_deleted=false` 是scope边界。

body完整形成后才比较90000B。≤90000时返回frame及 `generation_summary/generation_summary_bytes/generation_summary_sha256`；完整读回0，不完整2。超限70，仅原完整必要body的bytes/SHA及overflow事件、无frame正文、无marker、不拆包。原完整临时summary文件存在不代表正文已成功回传。未知实际错误字符串长度不能提前保证fit。

输出位置：

```text
source-generation235-readback/summary.json
source-generation235-readback/readback-complete.json
```

marker schema是 `request235-current-C-actual-source-composition-v1-generation-readback-complete-v1`，绑定当前source/actual_request/summary，且明确scientific generation success不要求、没有quiet或删除许可。

## 9. 所有旧必要范围和原始正文身份

原五primary语义body保持：C、cut twojet、deep far、construction、BVP两阶段。旧完整closed geometry/held、rules、refinement、composition、source-entry与same-C各自scope保持，当前只是追加来源生成这一有独立语义的body，不是拆分一个原>90KB科学对象。

旧composition使用已刊 `root_20261116_complete_source_composition_relations.py`，8567B/7bc351fe46ce6c8bf94ba067b106a0a21bd89950277910fe46006c502815b163。完整原object所有必要成员沿原具名关系合同保持；只有严格更小时选关系表示。超过90000仍70且无marker。原文件大小和实际被选择必要body大小分别记录，不能把R546原composition文件110653B直接当未返回必要body大小。

same-C reader保主完整8stage汇总，并调用原head、3metric及3measure/compare各自已经定义的必要scope；每个语义body各≤90000，不能把其中超限对象人为再分片。原科学exit2仍可以有完整必要body；科学成功不成为读回的新门。反之，body溢出、缺source、读取错误或ownedunknown仍阻止相应完整marker。旧reader的既有通用选择边界不由本接口扩大成“全部科学原树已返”。

本次公开generation reader不同于composition的完整关系：前者只对必要来源状态和完整输出地址作选择，五具名重复provenance保身份；后者对原已选完整composition object作可逆关系。两者不能都笼统叫“原完整result已回传”。

report job对generation body只做实际bytes/SHA校验并重复compute同一正文。缺body明确unavailable/exit2，不能从本地文件SHA恢复。原refinement正文仍只一份，same-C新正文的完整各scope在compute log；report只给它们真实identity/outcomes。job的success/failure不是任何科学通过判据。

## 10. 清理、ownership与实际失败路径

公开entry的guard-cleanup在生成文件不存在时也可加载。其顺序为：

1. 绑定真实235外层、base、工作视图及当前composer。
2. 核generation marker/summary及actual inner与preparation中的actual_derived_request一致。
3. 核真实generated same-C composer完整source并保全部cleanup后缀。
4. 委托same-C来源/necessary/owned quiet条件。
5. 委托entry原actualsource必要marker及真实inner/dispatch/base条件。
6. 委托refinement reader的原九outcomes、所有原markers与actual owned quiet，最后由原函数决定是否删除。

任一新公开guard步骤失败，输出事件 `request235_cleanup_skipped_before_generated_entry`，保原异常及traceback，标明generated cleanup未调用、原cleanup未调用、raw_deleted=false、quiet未推断，返回2。它没有临时“尽力清理”删除分支。实际缺env时workflow也从公开checkout路径调用entry，得到明确错误/skip；不是尝试运行一个尚未生成的cleanup文件而丢失控制范围。

generation marker只是不可变来源scope。原owner仍核实际PID/startticks/pgid/sid/boot和后代、冲突/unknown等责任；可疑own不可读仍保unknown。source读取成功、metadata count相同、外部同uid存在与否均不能替代该判断。所有写入者未静止时不允许读删raw的原条件保持。

原九outcomes仍为C、cut、construction、far、BVP、rules、closed、refinement、composition，另加本次来源entry和same-C完整必要护栏。旧科学closed marker保真实冻结schema `request230-bound-coast-closed-postsolve-readback-complete-v1`，不是误用旧运行；它的actualsource/run/body绑定必须本次真返回。

原attempt230没有执行清理，本文不修订该实际事实。本次是否成功静止、真正删除或保留，只能由实际R560原事件记录；没有预设success或removed=true。

## 11. 逐类保留的未付范围

源码生成、科学执行、必要传输、所有权静止和删除是五类不同责任。只有第一类闭包全部成立才可进入对应真实科学caller；并非所有public/expectedSHA存在就证明transitive科学函数已经执行。

运行到任意停止点时要保：

- 初始C、query/cut、deep112、far及point sampler的完整已付/未付与真实stored/decoded账。
- full453与frozen450各自实际启动、native/J/FD/final门、所有trial/失败地址和未启动后缀。
- 首闭面construction与共同材料/帽/held的真实source和范围。
- mesh/M两级真实父链、每个新场重做的geometry及原metric/reach/held。
- same-C完整重算头与旧粗界、新叶/新tail query的实际已付范围，三个field的metric/evidence与comparison原结论。
- 各必要scope真正正文尺寸/身份/错误，以及缺marker使清理停止的实际原因。

没有first450不能改写成“同C重算失败”；source生成未完成也不能用科学阈值解释。只改包围不改变场的真实误差，只有upper改善不等于sup严格下降。原native/RMS容差仍不自动成为整个闭面relative metric floor。R514/R521等后续条件常数不在本入口冒成已支付的数值界。

本入口不改变raw退休原则：所有仍被消费者需要的原C/head/query/ledger、geometry/checkpoint及来源生成原件都在原namespace生命周期内保留；完整必要与quiet满足后按原cleanup退场。未返原件不从SHA恢复，不把旧run的删除raw当本次输入。

## 12. 发布和实际回执

本批完整条件与真实接口已成，但实际运行以发布后的正式head、官方单dispatch回执及run/jobs为准。原230request/workflow/source完全冻结。本次workflow的 `workflow_dispatch` 使正式发布路径能在真实Git push后调用官方触发；没有使用push成功冒充workflow已开始。

预留actual235结论R560。唯一终态读者在结束后按官方两个job的实际必要正文逐scope读取，区分connector文本身份与HTTP原bytes，科学结果与metadata事实分列。运行中仅取官方metadata，不读取大科学日志。报告不得以成功body数量、source535→545、或job颜色填补未运行/未返范围。

正文中源码保持命题以 [R559](../results/R559-actual-source-engine-interface-and-complete-generation-readback.md) 为依据；这里没有要求额外fixture、独立审核job、数值对拍或新接受门。所有源准备和原科学都只在未来正式Actions实际执行。
