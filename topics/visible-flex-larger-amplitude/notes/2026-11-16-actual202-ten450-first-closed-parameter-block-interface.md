# R452：actual202→205 的首次闭面参数、完整五阶段与独立 held 来源接线

作者：AI。日期：2026-11-16。状态：独立来源适配源码；尚无本接线的实际 Actions 结果、接受450父场或几何证书。

## 1. 本次改变与保留范围

R449 把 actual202 的实际末十维候选明确投影并绑定到新的准确连续十族，随后仍须真实完成 full453 与在相同末十词处重新求解的 frozen450。这个新有限求解器的 driver、launcher、recipe 和 request205 截止时间各有自己的身份。原 R437 的 `joint203-frozen450` 来源登记不能代替这些身份。

本次新增四件独立文件：参数 policy、五阶段 runner、必要 reader 与独立 held wrapper。它们保留原 R437 的首次构造算法和读回范围，以实际 `actual202205` tuple 接原 R438 生命周期。原 R437、R438、193、203、R409、R413、R416、R417、R425、R426、R435 的已发表文件均不修改。205 总 helper、总体 owner、request、workflow 由上层独立编排；这四件不代替它们。

准确 target、root family、当前接受450、完整 native 绑定、当前材料角与几何来源仍由原实际文件贯通。新 source 名称本身不支付任何 BVP、连续域、metric、reach、held、δE 或全闭合目标责任。所有几何算术只在本仓库公开 Actions 执行；本文交付时仅进行了源文本、字节身份与完整差异处理，没有本地 import、AST、compile、fixture 或科学运行。

## 2. 新来源 tuple 与原 JSON 兼容

`upstream_kind` 必须为 `actual202205`；实际上游目录由205总 helper读取本 job 的 `BVP-launch/result.json` 后给出。新 runner 用独立环境复制原 R438 `bind_original193` 函数正文，仅把函数名和完整 producer/source/schema/deadline tuple换为本分支。原判断、完整两阶段、当前 checkpoint、十词、原 C 与 geometry 绑定的正文不删减。

新 launcher 的 recipe schema 是 `R449-explicit-actual202-projected-accurate-ten-joint-full453-to-frozen450-recipe-v1`。它实际保存 `actual_candidate_binding` receipt；后闭面层消费这个 launcher 的完整原字节身份及其真实 driver/checkpoint。它不自己重算投影，不把 actual202 的旧有限族末点认作准确连续族的已接受解，也不把 candidate-binding 成功当作 full453 或450接受。

原两个小 JSON 保持原字节：

- `current-ten450-first-closed-parameter-policy.json`：完整构造与 witness 政策。
- `current-ten450-first-closed-work-choices.json`：原五阶段、两次参数动作和 held 的工作参数。

新 policy 显式固定 `POLICY_SCHEMA = "R437-current-ten450-explicit-closed-parameter-policy-v1-recipe-v1"`，不再用新的 producer schema 拼出不存在的 recipe schema。新 runner 也用这个独立常量检查 policy。因此原2198字节 JSON无需重写 schema，原3356字节 work choices亦不改其科学或资源数值。work choices 中关于193/203的历史说明不充当205来源授权；实际来源严格由新的 `actual202205`、实际205截止时间字节及本表精确源身份决定。

policy 的 `INPUT_SCHEMA`、结果 schema、首次 freeze、材料定义、transport schema使用新 R452 前缀。旧 R437 freeze 不能改名当作 R452 freeze：`first_construction` 和 `first_transport` 仍核真实同源、同 policy、同截止时间及原完整对象。policy 保留原193/203明确 origin表项并新增 actual202205；runner保留原 R438 原193/R431分支，加本actual202205分支。原 joint203 首闭面仍使用原 R437 文件；这里没有用新别名覆盖原 joint203入口。

## 3. 四件真实 CLI

以下只说明实际参数形式；路径、SHA、父场及输出均须在同 job 从真实文件生成，不是可预填的接受样例。

```bash
python -u computations/geometry_20261116_actual202_ten450_parameter_block_postsolve.py \
  --input "$POSTSOLVE_INPUT" --input-sha256 "$POSTSOLVE_INPUT_SHA256"

python -u computations/root_20261116_actual202_ten450_parameter_block_postsolve_necessary.py \
  --directory "$POSTSOLVE_DIRECTORY" --out "$POSTSOLVE_NECESSARY_JSON"

python -u computations/geometry_20261116_actual202_ten450_parameter_block_postsolve_held.py run \
  --input "$HELD_INPUT" --input-sha256 "$HELD_INPUT_SHA256"

python -u computations/geometry_20261116_actual202_ten450_parameter_block_postsolve_held.py readback \
  --directory "$HELD_DIRECTORY" --computations "$COMPUTATIONS" --out "$HELD_NECESSARY_JSON"
```

policy helper由 runner以真实小输入调用：

```bash
python -u computations/geometry_20261116_actual202_ten450_closed_parameter_policy.py \
  --input "$PARAMETER_INPUT" --input-sha256 "$PARAMETER_INPUT_SHA256"
```

`PARAMETER_INPUT.operation` 仍仅为 `initial-construction`、`reuse-construction` 或 `held-witnesses`。首次205选择初始分支；未来若另有真实再求解者，仍须独立注册其来源并提供同 job 原 freeze/transport，不能因为 policy有reuse函数就宣称所有后继 mesh/M/角度细化已接通。

本轮只新增四个来源文件，未新增总调用入口或request；205总 helper负责实际创建输入、读回调用与清理 marker。四件均不直接执行 Git、API发布、artifact上传或 raw 删除。

## 4. Runner 的实际输入字段

runner输入schema是本 runner schema 加 `-input-v1`。除新来源名字与原 policy类型兼容外，输入结构沿原 R437/R438。

| 字段 | 实际来源和责任 |
|---|---|
| `namespace` | 当前205自有 RUNNER_TEMP 子树；由总入口创建并记录，不重新开始科学钟 |
| `upstream_kind` | `actual202205` |
| `upstream_launch_directory`、可选 `upstream_result_sha256` | 当前实际 BVP-launch 目录及其完整 result字节 |
| `job_deadline`、`job_deadline_sha256` | 当前 launcher确实使用的 `actual_job_deadline`，不是猜测的同名文件 |
| `geometry_directory` | 真450 checkpoint原 native binding所指的当前 geometry |
| `continuous_e_directory`、`continuous_e_result_sha256` | 同一 geometry/checkpoint消费的原完整 f12f C结果 |
| `computations`、`proof_directory`、`source_topic` | 原计算源、原证明与原Node来源目录；完整源针脚照保 |
| `out` | 当前 namespace 的新自有 sibling输出；不能覆盖原 BVP或输入目录 |
| `construction_policy` | 恰 `{file, sha256}`；原2198字节 policy复制到同 namespace后的真实身份 |
| `construction_mode` | 首次为 `initial-construction`；此时禁止预填 freeze/transport |
| `resources` | 原五 stage caps、两 parameter caps、shutdown/disk/heap显式资源 |
| `witness_resolution` | `interval_bits`、`sqrt_bits` 原明确精度 |
| `metric`、`c_queries`、`reach` | 原完整四Loewner/同C查询/完整块reach输入，不删字段 |

reuse分支另须 `first_construction_freeze` 与 `first_material_transport`，二者各恰 `{file, sha256}`，都是真实同 job 原件。任何分支均禁止外层输入先塞 `construction`；真实参数动作成功后才在新 Procedure 自有内存内填入原五CLI所需对象，原已hash输入文件保持不变。

原 C文件清单是 `result.json`、`input-binding.json`、`query-plan.json`、`query-results.json`、`large-arrays/complete-source-radial-panels.jsonl`、`large-arrays/source-piece-index.json`。前四件按原 binder要求读核；后两件是R426按需精化的真实来源，不从摘要SHA恢复。缺后两件保原明确未付精化范围，不否定原已完整粗界，也不添加新的数学接受条件。

## 5. 原完整接受与同场绑定为何仍然成立

新 `bind_actual202205` 只在自己的函数环境中替换 launcher、driver、deadline及完整源码pin。没有修改已加载 BASE 的全局常量，更没有把旧driver记录的schema改成新schema。原正文逐项保留：

1. 同 job `run_id/source_commit`；真实 launcher source/schema；deadline原bytes/SHA与launcher记录相等；deadline recipeSHA等于实际 upstream recipe。
2. 上游完整driver已返回、实际child exit0、原有限BVP接受、owned group确实quiet；resource/external interruption仍按原字段保真。未接受时返回原not-started后缀，不用小残差推成功。
3. 原 adapter status完整字节、独立新driver身份；`success/new_coupled_finite_acceptance/actual_design453_accepted/actual_frozen450_accepted/native_owner_closed/all_phase_leases_released`均沿原意义；原owner关闭异常仍必须不存在。
4. 两阶段严格为 design453/frozen450，实际维数453/450；每阶段原main接受和完整fullDN exit仍保；十词逐一相同。
5. 真43f writer checkpoint及其 actual driver source；active参数0、fixed core targets0、维数450；明确没有由453删三行重标450。
6. checkpoint的 geometry 与实际输入 geometry result同字节；同一 f12f C结果与原native binding同字节；完整runtime closure、十词和target identity均保留来源。

因此若本分支实际通过原绑定，所接对象就是新 R449原门真正接受的450有限场。它仍不等于准确连续解、C²闭嵌入或课题成功；这些结论需要后续原消费者真实支付。若任何原前提未返，绑定或not-started记录保其真实范围，不伪造父对象。

## 6. 执行顺序与独立责任

原五个科学stage名字、CLI和结果schema均不变：`radial_replay`、`original_cuff_atlas`、`shared_field`、`metric`、`reach`。

完整顺序是：真450绑定；完整径向replay；真实 `construction_parameters`；R413原cuff/target atlas；R409 shared field；真实 `held_witnesses`；R426 metric；R435 reach。外层在真实shared和witness存在时另调用R425 held wrapper。

构造动作必须等完整真实径向返回，因为H来自该径向数据。若径向或构造未产出，剩余依赖保完整not-started地址。R413真实plan与atlas均有原字节身份，shared field由该plan和同一当前径向数据生成，不从旧场复制。

witness动作在shared成功后确定实际首prefix片索引，并保存原完整材料定义/registration。它失败、资源中断或必要stdout超限不会把metric或reach新加一个成功门。原runner依旧记录witness错误并按原独立stage责任继续尝试；是否尚有资源由原同一钟决定。

metric没有证明、严格反证、partial或执行错误，都不成为reach的数学前门。held只需原三真实生产依赖：radial、atlas、shared，加实际witness输入；它不依赖metric/reach成功。缺witness时是held输入未生成，不是δhold/δE反证。

## 7. 首次 A/B 与完整构造定义保持

参见已发表 [R437](../results/R437-first-current-closed-construction-and-material-definition-freeze.md) 与 [R438](../results/R438-original-or-refined450-block-reach-and-held-source-binding.md)。本次policy的 `initial`、`material_definition`、`construction_words`、`first_construction`、`first_transport`、`reuse`、`capture_material_transport`、`witnesses` 数学正文均原样保留。

首次W仍由原明确十进制文本形成binary64；marker scale仍是原 `1/160` 转为同一binary64操作顺序。cuff只取当前原C绑定的 `rCuff` 字词。全部4个marker的side、center、radius、amplitude及负零都写入完整word清单，没有因重叠、负幅度或轴对称猜测省略。

H仍由首次真实R409径向数据计算：当前完整112core与末端全部z系数形成原mean，当前cut径向DC及共同B的inner/cut原数据形成原精确有理定义值，然后仅按原规则RN64。记录投影差和完整计算来源，不加正H修正，不搬旧例子的高度，也不据未来metric/reach结果选H。

第一记录 `first-construction-freeze.json` 保存完整当前十词、target/cuff、A的实际W/H/全marker words、112材料定义、原fullDN来源和原高度形成数据。第二记录 `first-material-transport.json` 只在实际shared存在后保存完整B：当前Phi定义、原SE2 registration、R249 inlet normalization、mean/core gauge、phase rule及各原件身份。记录source/schema独立，但它们所定义的公式和原运算次序不变。

以后reuse不据新径向重选H；它完整消费A/B并保原比较范围。`material_word_difference_is_not_a_solver_or_geometry_rejection`、`actual_common_material_pullback_unpaid`等原语义保留。same W/H/markers或same十词不能直接推出公共材料图中的同一个闭g。当前层仍使用当前求解core对应Phi；R443条件与R447准确材料拉回不是因本来源注册而自动执行。**R447尚未注册actual202205这对新producer身份；本R452不宣称它已调用或通过。**

R425 witness仍为当前真实首个 `kind=prefix,left=0,right>0` 片，在径向0和物理q四个cardinal点、upper侧。记录实际piece index和全部四点；它们只是原全像held消费者的输入，不把四个材料点位移当全像Hausdorff距离，不以旧网格点号冒新场位置。

## 8. 资源、绝对钟与原中断语义

本四源不从总request猜预算，不更改各cap。205总helper应完整复制原work choices，实账列明各stage实际给定与原绝对钟剩余：

- 五stage caps：radial1800s、atlas120s、shared600s、metric1800s、reach1800s。
- 两parameter caps：construction120s、witness120s。
- 独立held cap1800s。
- free reserve 2147483648 B、Node heap12288 MiB、child shutdown reserve30s；query内部预算900s等11字段均原值复制。

这些是显式有限work上限，不是保证全部可用时间相加后能够完成。实际18900秒科学范围从原namespace创建时刻计，2700秒读回预留及原job硬限由总入口承担；本层保原实际deadline receipt，绝不以postsolve开始时刻重开钟。policy还独立核该deadline的18900/2700字段及实际recipeSHA。

所有科学child沿冻结R438 `OwnedChild`：新独占session/PGID、真实PID/start_ticks身份、原绝对截止、外部SIGTERM/SIGINT、TERM→等待→KILL→reap、组quiet及身份冲突记录。参数子程直接复用原完整invoke正文，只有stage row集合和预算字段换为两parameter集合；没有裸 `subprocess.run` 绕过钟。单纯一个parent在共享runner组存活不作为科学组未quiet证据。

runtime或资源不足保原partial、当前/未访后缀，不把停止叫数学失败。一个完整helper结果可能已写文件而自身stdout必要摘要70：runner仅在实际文件completed/error/quiet等原条件全部满足时继续消费，明确记录 `completed_parameter_file_with_stdout_overflow`；这不补称该stdout读回已完成。最终reader仍须自己的完整实际读取及90KB限制。

## 9. 必要读回、完整范围与清理边界

新reader保原R438所有五stage选择器，并逐项加入原两parameter动作。实际geometry对象和大ledger都留同job临时目录。完整block frontier、当前single-rank、union未决及原错误范围按原R438/R435选择器保留；已退未付leaf在原ledger中的地址与完整身份不冒为正文逐行回传。来源/成功大数组的身份读取也不冒逐数值科学复核。

两parameter每个原row包含started/未启动理由/actualexit/resource/external/ownedprocess及原结果来源；有绑定的实际小result时，保operation/completed/returned/error/pending、资源和原deadline、实际选择W/H/全marker、实际四witness、原material记录来源及未执行pullback范围。重复成功构造正文只选择一次；不存在的key不自行填零、未返回不填通过。

新runner必要主schema、held必要schema及frames见末身份表。原step output键不改：reader写 `postsolve_summary/postsolve_summary_bytes/postsolve_summary_sha256/postsolve_readback_complete`；held readback写 `postsolve_held_summary/postsolve_held_summary_bytes/postsolve_held_summary_sha256`。这些是step outputs；总workflow可以仅给report传身份和outcome，原必要全文保compute各自frame，不把它们拼成新的大job输出。

每个原必要对象仍单独限制90000字节，不提升上限、不分包编码。必要输出超过上限，保原requested bytes/SHA、诚实70及raw未读/未删状态；元数据解析失败也不能推原科学反证。没有承诺实际真实场的所有失败scope必定小于90KB。

reader首先确认原五stage与两parameter所有实际owned过程quiet，读取前后重核原文件字节。held另核其独立child和同postsolve来源。四源均不删除raw、不上传artifact、不创建总体清理授权。205总helper/owner必须在其全部原必要读回、真实quiet和原marker条件成立后自行决定清理；缺返回、未知范围、oversize或不quiet均不能从本层一个exit推可删除。

## 10. 调用方必须保留的实际输入与完整依赖

所有新源码要和原R438及原科学来源同处真实computations目录。runner加载原5bb源码并核SHA，reader加载原57413源码，held加载原119ec源码，实际sourceview的字节SHA写入原记录。它们不会把新module仍标旧source；各 `__file__`、producer schema、必要reader schema与实际新源绑定。

原R438直接PINS整体保留，不能只恢复实际205分支看似用到的几个文件。原193与R431支持代码仍由原模块定义，故其已冻结driver/launcher pin也是加载闭包一部分；这不代表此次执行它们。新增actual202205的driver/launcher两件和本四件身份另明确加入请求源闭包。各科学callee自己的全依赖及proof目录仍沿原，不通过少列pin降低它们原guard。

policy direct PINS仍为43f checkpoint、1c7 SavedPrefix、6a5 shared、02bb atlas、28417 accurate-cut、0ff1 caps和675活动sixjet解释器；original JSON的 `geometric_interpretation.source_sha256` 与这组完全同。held仍调用原c87b R425，metric仍原77be+07fc R426并保28b7固定目标消费者，reach仍e3fc R435并真实依赖3ea1 R422。原W/H、marker、cut、全C根族、所有两反射与帽、全phase/完整pair责任都未被新wrapper缩减。

## 11. 本次未支付的责任

没有本来源的实际parent、运行ID、full453/450接受或几何值。实际205会先真实产生准确族candidate recipe并重求两阶段；旧actual202有限族结果不能直接转成新连续族证书。真实原450未返时，下游仍应输出未启动及全部原因。

首次构造由当前径向数据定义不证明该RK轨迹等于准确连续解；原R409/R416准确节点重构、cut atlas与目标g责任按原证明和消费者分别支付。metric、reach、全像held与反射包含δE仍须真实当前场输出；本次不预填K、τ、eta通过，也不从某三维包围盒或t端点推全phase。

R441/R448/R450的后继mesh/角/步数/same-far来源没有因新first-field分支自动接通；变M另有真实全M责任。R447共同材料consumer对actual202205尚未注册，首次A/B记录仅提供未来可绑定的定义数据，不把记录动作称为已施加材料共轭。原有限数据误差、连续收敛与课题最终严格目标均未由本次工程适配证明。

以下冻结表与完整差异记录提供可复核来源。暂存 `source-build-identities.json`、`publication-files.json`、各 `.diff` 只供发布核对；实际拟入库为四源及本接口，原两个JSON继续引用已发表原件。

## 12. Held 的完整小输入与输出协议

held `run` 输入恰含 `schema`、`postsolve_directory`、`postsolve_procedure_sha256`、`postsolve_input`、`postsolve_input_sha256`、`witness_plan`、`witness_plan_sha256`、`held`、`resources`、`out`。不能直接传某个旧 shared/result 的SHA来绕过本次完整 Procedure 绑定。registered procedure 只有本R452 runner/source/schema/input三元；实际 reader也是本R452必要reader。

`held`完整八字段仍为 `active_depth`、`position_max_depth`、`position_radius_goal`、`interval_bits`、`sqrt_bits`、`max_position_cells`、`max_prefix_points`、`max_tail_witnesses`。其中position goal保持原有理字符串；resources保原 `held_budget_seconds`、`child_shutdown_reserve_seconds`、`free_bytes_reserve`。真正全像/完整prefix/tail证明仍由c87b原R425实现，wrapper不重写算法。

frame与schema如下；BEGIN/END必须逐字匹配。

| 对象 | Schema/协议 |
|---|---|
| policy 结果 | `R452-actual202-ten450-explicit-closed-parameter-policy-v1` |
| runner 结果 | `R452-actual202-accurate-ten450-first-parameter-block-postsolve-v1` |
| reader 结果 | `R452-actual202-ten450-parameter-block-postsolve-one-necessary-conclusion-v1` |
| held 结果 | `R452-actual202-ten450-parameter-block-same-job-held-after-shared-v1` |
| runner 输入 | `R452-actual202-accurate-ten450-first-parameter-block-postsolve-v1-input-v1` |
| policy 输入 | `R452-actual202-ten450-explicit-closed-parameter-policy-v1-input-v1` |
| 首次 freeze | `R452-actual202-ten450-explicit-closed-parameter-policy-v1-first-construction-freeze-v1` |
| 材料定义 | `R452-actual202-ten450-explicit-closed-parameter-policy-v1-complete112-material-angle-definition-v1` |
| 材料 transport | `R452-actual202-ten450-explicit-closed-parameter-policy-v1-actual-material-transport-record-v1` |
| held 输入 | `R452-actual202-ten450-parameter-block-same-job-held-after-shared-v1-input-v1` |
| held 必要结果 | `R452-actual202-ten450-parameter-block-same-job-held-after-shared-v1-necessary-v1` |

- 参数动作 frame：`BEGIN_R452_CLOSED_PARAMETER_NECESSARY` / `END_R452_CLOSED_PARAMETER_NECESSARY`。
- 五阶段加参数必要 frame：`BEGIN_R452_PARAMETER_BLOCK_POSTSOLVE_NECESSARY` / `END_R452_PARAMETER_BLOCK_POSTSOLVE_NECESSARY`。
- 独立 held 必要 frame：`BEGIN_R452_CURRENT_TEN_PARAMETER_BLOCK_HELD_NECESSARY` / `END_R452_CURRENT_TEN_PARAMETER_BLOCK_HELD_NECESSARY`。

退出码仍按原实现：runner在无error且all-owned-quiet时0，否则2；已观测signal返回128+signal。policy正常completed为0、资源partial75、外部中断128+signal、其它未完成2，必要overflow70。reader只在原必要scope完整且单份输出合法时0，否则70；held保原完整run/readback失败语义，不把其error当几何反证。

## 13. 最终冻结身份

四源的目标均位于topic `computations/`，本接口位于 `notes/`。表中byte/SHA按实际完整UTF-8原件；下面diff/manifest仅暂存，非新的科学输出。

| 角色 | 文件 | bytes | SHA-256 |
|---|---|---:|---|
| policy | [geometry_20261116_actual202_ten450_closed_parameter_policy.py](../computations/geometry_20261116_actual202_ten450_closed_parameter_policy.py) | 37958 | `b49769f13f69bf30b82988b1ca57382c602d4b74bc3ae8a6c2b5d1e0ee3df7a8` |
| runner | [geometry_20261116_actual202_ten450_parameter_block_postsolve.py](../computations/geometry_20261116_actual202_ten450_parameter_block_postsolve.py) | 26899 | `89a90b2d5d762510c228c5d3a4f6fe27a573c890b760268aecace2a44ab9e010` |
| reader | [root_20261116_actual202_ten450_parameter_block_postsolve_necessary.py](../computations/root_20261116_actual202_ten450_parameter_block_postsolve_necessary.py) | 10412 | `e3a4a70277c3267ff412e1ac3f63590be135ed28f5cfc3c1e553e4e2e9cd7f3c` |
| held | [geometry_20261116_actual202_ten450_parameter_block_postsolve_held.py](../computations/geometry_20261116_actual202_ten450_parameter_block_postsolve_held.py) | 5449 | `8d0927cc335faa6a0a639f0f0ecec063ee2d65bbc0ef11bd990eb118aa971ffb` |

### 13.1 本次实际上游来源

| 来源 | 文件 | bytes | SHA-256 |
|---|---|---:|---|
| driver | [geometry_20261116_actual202_accurate_ten_full453_frozen450.py](../computations/geometry_20261116_actual202_accurate_ten_full453_frozen450.py) | 34835 | `56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615` |
| launcher | [geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py](../computations/geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py) | 20657 | `227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7` |

Driver schema：`R449-actual202-projected-accurate-ten-joint-full453-to-frozen450-physical-DN-v1`。Launcher schema：`R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1`。Deadline schema：`request205-owned-job-science-deadline-v1`。真实 namespace由205入口给出为 `visible-current-C-actual202-ten450-closed-geometry205`，本层仅核实际路径/receipt，不另造创建时刻。

上游最新修订只补R449准确模板必需的原 `cut_radius` 字段，并把helper pin级联到driver/launcher。旧6bb/47f9来源快照已废弃；不得用它们替换本表56cb/227e。当前candidate helper SHA为 `ee3675ce3465930f2ce32283a468f5fad464639ca6ccda6352f027f00f0c6c38`。本四源没有复制该helper算法；真实上游仍须实际完成其自身绑定和全部原门。

### 13.2 原 JSON 与生命周期

| 原件 | bytes | SHA-256 |
|---|---:|---|
| [current-ten450-first-closed-parameter-policy.json](current-ten450-first-closed-parameter-policy.json) | 2198 | `fe932b50f25bd8d77709be1efd26da8c24a7d87f9ad1423bd6a9ebc34c1d0a41` |
| [current-ten450-first-closed-work-choices.json](current-ten450-first-closed-work-choices.json) | 3356 | `8a03c854c93194f6bb3f2f75f06c20bf8397e5b85451ce6a1e7247f0a95c7d08` |

| 不改的原实际生命周期依赖 | SHA-256 |
|---|---|
| [geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py](../computations/geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py) | `5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95` |
| [root_20261116_current_C_ten450_original_or_refined_block_postsolve_necessary.py](../computations/root_20261116_current_C_ten450_original_or_refined_block_postsolve_necessary.py) | `57413c73db29cb9f65451f631771c07c642edf162dfbe6cdbaa292b5fb451fe5` |
| [geometry_20261116_current_C_ten450_original_or_refined_block_postsolve_held.py](../computations/geometry_20261116_current_C_ten450_original_or_refined_block_postsolve_held.py) | `119ec38cc9351a2d040ce8c7101b933e1e572d19deabb7baf62c4c1cec62eada` |

### 13.3 原科学角色的精确来源

| 角色 | 文件 | SHA-256 |
|---|---|---|
| 完整径向 | [geometry_20261115_current_C_ten450_radial_readout.mjs](../computations/geometry_20261115_current_C_ten450_radial_readout.mjs) | `5cc3134ed58aed45efea012219aa2e889624c47b41d5ee9f558da231806ab568` |
| 原cuff atlas | [geometry_20261115_current_C_original_cuff_target_atlas.py](../computations/geometry_20261115_current_C_original_cuff_target_atlas.py) | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` |
| shared field | [geometry_20261115_current_C_ten450_shared_field.py](../computations/geometry_20261115_current_C_ten450_shared_field.py) | `6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3` |
| 完整live metric | [geometry_20261115_current_C_ten_live_query_complete_metric.py](../computations/geometry_20261115_current_C_ten_live_query_complete_metric.py) | `77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892` |
| 同C按需query | [geometry_20261115_same_job_C_live_query_provider.py](../computations/geometry_20261115_same_job_C_live_query_provider.py) | `07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9` |
| 固定盒metric原依赖 | [geometry_20261115_current_C_ten_complete_relative_metric.py](../computations/geometry_20261115_current_C_ten_complete_relative_metric.py) | `28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590` |
| 完整块reach | [geometry_20261116_current_C_ten_complete_block_reach_cover.py](../computations/geometry_20261116_current_C_ten_complete_block_reach_cover.py) | `e3fcd9eb7ed304cd502c7e03186d65a2d414366c8ad47313c5754aa43ded66ad` |
| 逐叶reach原依赖 | [geometry_20261115_current_C_ten_complete_reach_cover.py](../computations/geometry_20261115_current_C_ten_complete_reach_cover.py) | `3ea1ef9fb56ec10301defa18d832681d6061d8646e78893957ca160279b71834` |
| 独立原held/δE | [geometry_20261115_current_C_ten_held_and_rigidity_inputs.py](../computations/geometry_20261115_current_C_ten_held_and_rigidity_inputs.py) | `c87b3a9b9d17f74d8c4f4066f65318e50fed5a56143f620628049a86dcf77ef2` |

### 13.4 实际变更与可复核范围

`four-sources-complete.diff` 是相对发表R437四原件的全部差异，原源SHA分别为 d7d01460、0f03ad49、f6176dba、28b48f0c；全量原字节在本次文本处理中实际核同。变更为新source/schema/module/output身份、新actual202205完整来源登记、显式保旧POLICY_SCHEMA及真实上游修正的pin级联。原构造/完整材料提取/五CLI/两个invoke参数视图/ownedchild/错误和必要selector没有新增科学逻辑。

本次并未执行这些源中的动态sourceview或导入任何数值依赖；动态view仍在公开Actions运行时逐原片段定位与原源SHA绑定。未声称本地编译通过或此次实际场接受。差异文件与manifest是可重算暂存，不替代真实运行日志或几何证据。
