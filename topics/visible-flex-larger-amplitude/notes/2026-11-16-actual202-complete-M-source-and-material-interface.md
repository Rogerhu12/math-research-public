# actual202205 → complete M → 首次同构造闭面：R457 源接口

作者：OpenAI ChatGPT /root/amplitude（AI），2026-11-16。

正式条件结论为 [R457](../results/R457-actual202-complete-M-source-and-first-material-registration.md)。本接口交付六个独立可执行/可调用来源视图，没有请求、未来参数或运行结果。临时 publication-files.json 是供唯一发布者取件的清单，不拟作为科学结果入库。

## 1. 最终文件与父源

| 新源码 | 字节数 | SHA-256 |
|---|---:|---|
| geometry_20261116_current_C_actual202_frozen_M_owned_launch.py | 72739 | 23a3b218662003d74824ad19b48bda9b641346a3d15cbf108885ed995e2aee40 |
| geometry_20261116_current_C_actual202_M_common_material_phase.py | 38151 | 059d0df3ab5957b8ba5adf69e305ee4663ba06378242fe4c5f2116bab437af41 |
| geometry_20261116_current_C_actual202_M_postsolve_geometry.py | 71452 | a177cd7a80ede901843763f90d52d3a0c723d76b0c2be381122d91e6a68394bb |
| root_20261116_current_C_actual202_frozen_M_necessary_readout.py | 29934 | fff29708f5c2ea24415392444af8860b06cf9a62db5fa24b57a1d1637dc6a753 |
| root_20261116_current_C_actual202_M_postsolve_necessary.py | 27343 | 9e4a00dc5ce3c3299d7d0cf43387139bd20dc6713d092b9d79ce99dca9305605 |
| geometry_20261116_current_C_actual202_M_postsolve_held.py | 44390 | 99634dccd54de2f33e27c63039aa9747b08ce026f3232c576596fbdbd2a10936 |

条件结论为 R457-actual202-complete-M-source-and-first-material-registration.md，18406 字节，SHA-256 f7242649f641c2b03cc34aaf52abf049c0a911210c6ca427e835a643d9dd5334。

| 新角色 | 实际父源 SHA | 差异范围 |
|---|---|---|
| M owner | 47fc1aba734742c67d772eac7479a4f56165f711c5f646f4ff6e47c17c53829b | 205来源/候选receipt；真实R456父/原配置及far来源；旧R442-M与新自身M父分开 |
| owner必要reader | 845f4d8414905ee308bb2deb6db3628f1b63eb25ffb69875b78f818e9b2658d0 | 新owner/source/schema；候选来源小字段；新标记 |
| 五阶段runner | c5aeb8ba8cfd1aebeeaf4f0305006398fedbc3de868f9e74a78135129d548642 | 新owner/material来源；205钟；R452真实first source A/B |
| 五阶段reader | e48b7b2626d478efb1e591db462a49bbc5b50573547ced0ce6bd122b8d4445da | 新runner身份；紧凑A/B来源；新标记 |
| 独立held wrapper | 0020018c238f18f5afc9b9ac343d50b053a052bcc752d362e7f1bc1cd8b70647 | 并列真实R451/R457五阶段tuple；自身新schema/标记 |
| 公共材料API | db7df14743f1f91dc507918e1676ee8198227a8f28c60d25fc55c83993af7fb7 | R437/R452首112来源并列，R452真实A/B绑定；逆/六jet正文不变 |

R442 已刊22a454e3a4705fef552a1938beef655a8bd1ac53；R451已刊7a1a30ef879197237e063dae5380b047ba4de957。其原20运行源和12后处理源没有复制为20/12个新文件，也没有在原路径覆盖。新源仍直接调用真实旧科学文件。

## 2. 精确 schema、来源与角色

M owner schema：

    R457-current-C-actual202-capable-frozen-M-owned-launch-v1

其输入加后缀 -input-v1。原数值 driver 仍为 geometry_20261116_continuous_ten_frozen_M_refinement.py，395da6c8d43c0d31e59c58a2089fb4b116900a9b3192fa8d76456fc680adde12；原 driver/recipe/checkpoint schema均保持R442，不能为了新编排改标签。

M owner reader schema：

    R457-current-C-actual202-capable-frozen-M-one-necessary-readback-v1

五阶段runner schema：

    R457-current-C-actual202-capable-complete-M-live-query-block-geometry-v1

其输入加 -input-v1，upstream_kind 唯一为 R457-complete-M。这个角色指本新owner，并不允许把旧47fc输出直接改名作为该upstream；旧47fc可作为新owner真实父，由新owner重新完整求解。

五阶段reader schema：

    R457-current-C-actual202-capable-complete-M-block-postsolve-one-necessary-conclusion-v1

独立held schema：

    R457-current-C-actual202-capable-complete-M-held-after-shared-v1

输入和necessary输出分别加 -input-v1、-necessary-v1。其SUPPORTED_POSTSOLVE显式保真实旧c5ae/R451及新R457 source/schema/input三元组。未注册R456、R441新视图或任意同字段但不同source的程序。

公共材料schema：

    R457-current-C-actual202-capable-complete-M-common-material-phase-v1

describe和cell分别加 -definition、-complete-active-six-jets。

新增205 origin严格为：

| 字段 | 值 |
|---|---|
| kind | actual202205 |
| launcher | geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py |
| launcher SHA | 227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7 |
| launcher schema | R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1 |
| driver | geometry_20261116_actual202_accurate_ten_full453_frozen450.py |
| driver SHA | 56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615 |
| driver schema | R449-actual202-projected-accurate-ten-joint-full453-to-frozen450-physical-DN-v1 |
| deadline schema | request205-owned-job-science-deadline-v1 |
| adapter | geometry_20261116_actual202_accurate_ten_candidate.py |
| adapter SHA | ee3675ce3465930f2ce32283a468f5fad464639ca6ccda6352f027f00f0c6c38 |

原193/joint203三元组原样保留。actual202205尚未真实返回时，不能填其accepted父；本接口不作此断言。当前冻结205只执行它原来的首次闭面链，本条需以后新的实际完整入口接在cleanup前。

## 3. M owned launcher 的完整调用合同

实际公开Actions调用形式：

    python COMPUTATIONS/geometry_20261116_current_C_actual202_frozen_M_owned_launch.py \
      --input ACTUAL_NEW_M_INPUT.json --input-sha256 ACTUAL_NEW_M_INPUT_SHA

输入必须来自本次实际namespace，使用本节的输入schema，并显式给出以下字段；大写占位名不是已选择数值或可直接派发配方。

| 字段 | 实际内容 |
|---|---|
| namespace | RUNNER_TEMP内本次唯一已有总namespace |
| origin_launch_directory | 真实原193/joint203/actual202205 BVP-launch目录 |
| parent_launch_directory | 真实原450或已注册精化/M owner目录 |
| job_deadline, job_deadline_sha256 | 原origin实际消费的同一deadline文件和SHA |
| computations | 完整已pin运行源码目录 |
| accepted, accepted_sha256 | 与origin.actual_input_files.accepted相同原输入 |
| tail_config, tail_config_sha256 | 与origin.actual_input_files.current_native_config相同原输入 |
| tail_source_root | origin实际command中唯一--tail-source-root |
| out | fresh同namespace独占后继目录 |
| field_modes | 显式整数，实际绑定后须大于真实parent的M |
| max_nodes | 原完整seed/preflight容量，显式整数 |
| refinement_factors | field_and_native_angles/native_steps/material_angles/physical_angles四个正整数 |
| deep | 原完整C/deep输入与明确工作精度 |
| sampling | 原cover/far来源、proof和全部明确采样参数 |
| resources | deep/sampling/BVP和静止/磁盘的明确资源值 |

deep的键集恰为 config、config_sha256、ledger_ready、ledger_ready_sha256、stored_ready、stored_ready_sha256、proof、tail_proof、mode_extension_proof、precision_bits。

sampling须给cover_directory、cover_result_sha256、far_directory、far_result_sha256、proof、unit_row_proof、parameters。parameters原键为precision_bits、linear_budget_seconds、sampling_budget_seconds、max_panels、free_bytes_reserve、max_depth、local_defect_bits、panel_norm_limit、taylor_terms、max_geometry_cache_records、sample_max_nodes、sample_inverse_depth、sample_value_bits、representative_max_precision_bits。原128–8192工作精度和原各范围保持；本接口不替调用者选择。

若 `parent_launch_directory` 是 R456，owner 由真实 parent result/schema/source 识别；调用方不另填伪 parent-kind。它读该父真实 bf7d checkpoint 和9d765 driver、b778 client/5f14 sampler/43ab worker；从 `same_original_far_family_reuse.original_directory/original_result` 及配置 `R456_same_far_fresh_grid_origin.original_config` 取得保留的原 actual193/203/205 far/config。上述原现场文件须仍在同一 namespace，不能由 SHA 恢复。原 cover/far/proof 参数仍指向这同一 C/root 原来源；M 后继将重新计算完整新 M deep/far 行。

允许的真实父为 origin 的 accepted450、原 R441 resolution450、R456 same-far resolution450、旧 R442-M 或新 R457-M，以及仅原193对应的 R431 mesh450。每个均须同 origin、同原 deadline、实际已接受/已结束/静止，不能用 schema 单独识别。R456 情况使用 `parent_kind=actual-R456-same-far-resolution450`，必要摘要保 `actual_same_far_parent_binding`。完整 `395da`/`18399` 不修改：`select_native_family` 保存实际父 client，`bind_current_native` 的原允许变动集合之外保留全部 R456 配置；`run_sampling` 从父配置复制再加入真新 M source。这使下一 job 可按真实 R456→M 顺序组成联合精化，不是两条平行轨道冒同一序列。

resources键集恰为 deep_process_budget_seconds、sampling_process_budget_seconds、refinement_process_budget_seconds、child_shutdown_reserve_seconds、minimum_free_bytes_at_start、free_bytes_resource_stop。前三上界分别裁到原总钟的实际剩余部分，不累加成一个新钟。原总科学18900秒、必要读回2700秒和真实namespace创建时刻从origin消费的deadline读取并逐bytes/SHA绑定。

205额外来源读取只发生在原真实453/450与静止已返回后：actual_candidate_binding须和origin.actual_input_files.actual202_candidate_binding同一receipt；其phase=BVP-input-bound、原R449 source、生成recipe及actual_candidate_driver都要同源。它的原Decimal50投影不是 M seed；M seed来自真实parent CP。

实际输出保原R442目录布局：out/result.json、actual-resolution-recipe.json、deep/sampling各真实原文件、refined-BVP/adapter-status.json和亲生M checkpoint目录。launcher继续打印小返回事件，不能凭该event当必要读回完成。

真实M成功使用 current_refined_M_accepted、completed_driver_return、actual_child_exit=0、原adapter接受/native关闭、actual_refined_checkpoint及其driver/writer/shape全部一致。原资源partial、deep未起模式、采样未起/BVP未起、全部异常和静止记录都保留。

## 4. M 必要读回

    python COMPUTATIONS/root_20261116_current_C_actual202_frozen_M_necessary_readout.py \
      --launch-directory ACTUAL_M_OUT --namespace ACTUAL_NAMESPACE \
      --computations COMPUTATIONS --out FRESH_M_READBACK

可选 --entry-stdout、--entry-stderr 指向实际本次入口原日志。其余参数与原845f相同。实际输出键沿原source，BEGIN_R457_FROZEN_M_NECESSARY/END_R457_FROZEN_M_NECESSARY标记独立。

它仍调用原31891fe6 phase reader及22923f44 native必要API，不删FD方向/层或末finalflags。新增actual202_initial_candidate_binding只是receipt、明确资源来源与“未继承finite202接受/J”范围。原普通short/日志选择与长列表身份规则继续存在，不说所有大trace或错误原文都被导出。

一份硬上限90000字节；超限或metadata错误返回不完整，不能截表后伪称complete，也不分包编码全数据。即使完整读回也不证明科学成功，仍须看原scientific flags。

## 5. M 五阶段输入和实际 first A/B

    python COMPUTATIONS/geometry_20261116_current_C_actual202_M_postsolve_geometry.py \
      --input ACTUAL_M_GEOMETRY_INPUT.json --input-sha256 ACTUAL_M_GEOMETRY_INPUT_SHA

除了新schema/upstream_kind，其余原R451字段原样：namespace、upstream_launch_directory、可选upstream_result_sha256、job_deadline和SHA、geometry_directory、continuous_e_directory和结果SHA、computations、proof_directory、source_topic、out；first_shared_directory和first_shared_result_sha256；construction、resources、metric、c_queries、reach。

source_topic仍是原实际runtime源码根，和M owner的tail_source_root一致。环境中原科学consumer实际使用 VISIBLE_FLEX_SOURCE_TOPIC；不要把文稿中的SOURCE_TOPIC作为未经源码读取的新变量。

对于actual202205，额外必须给：

    "first_parameter_procedure": {
      "file": "ACTUAL_FIRST_R452_PROCEDURE_PATH",
      "bytes": ACTUAL_ORIGINAL_BYTES,
      "sha256": "ACTUAL_ORIGINAL_SHA"
    }

路径为真实首次R452 runner的procedure.json。实际大整数、SHA和路径只能从该运行原receipt选择；不是未来占位accepted。旧193/203沿原first shared合同，不接受一个会被忽略的这个新增字段。

读取关系如下：

| 真实字段 | 绑定到 |
|---|---|
| previous.input | 原R452 input schema、upstream_kind=actual202205、initial-construction |
| previous.inputs.original_launch / original_deadline | 当前M源origin和同一个deadline receipt |
| previous.stages中shared_field.original_result | 本次给出的first_shared结果 |
| previous.inputs.genuine_frozen450_checkpoint | first_shared真实原450 checkpoint |
| previous.actual_selected_construction.outputs.first_construction_freeze | 原A文件 |
| previous.actual_material_transport.original_record（如果有） | 原B文件 |

R452 runner与policy分别固定89a90b2d5d762510c228c5d3a4f6fe27a573c890b760268aecace2a44ab9e010、b49769f13f69bf30b82988b1ca57382c602d4b74bc3ae8a6c2b5d1e0ee3df7a8。A/B均读取原完整JSON，但必要摘要只保存receipt和明确范围。

A.current_target_identity与first_shared的原112目标canonical bytes/SHA相等；first/current M目标由原same-target-across-M独立比较。不可拿M表示的canonicalSHA去改写A。完整construction使用原IEEE词递归比较；policy格式的H/W/每个marker side、center、radius、height也逐词核，包括负零。

B存在时还读取first plan/assembly并核B的实际文件receipt；registration、normalization、mean/core gauges及phase规则原文对象一致。B缺失则first_B.actual_record_present=false、actual_common_material_pullback_unpaid=true；不需要metric/reach/held先成功。

五阶段顺序保持：

| 阶段 | 实际程序 |
|---|---|
| radial_replay | 原完整M全部576×steps重放、所有实际角/均值 |
| original_cuff_atlas | 原R451-M atlas，使用完整当前radial及冻结construction |
| shared_field | 原R442-M shared builder，保亲生M场和完整两帽 |
| metric | 原R451完整Loewner/live-C查询程序 |
| reach | 原R451完整block/leaf reach，不依metric成功 |

construction仍恰为cut_correction_width、cap_height、fixed_cap{markers:[完整列表]}；不得在M后按新场重新选择H/markers。

metric六参数：eta、interval_bits、sqrt_bits、initial_angular_depth、max_depth、max_visited_cells。

c_queries十一参数：precision_bits、integral_absolute_bits、integral_relative_bits、analytic_guard_bits、integral_evaluation_limit、value_width_bits、integral_max_depth、inverse_max_depth、max_panels、max_nodes、budget_seconds。

reach十五参数：curvature_upper、target_reach、active_depth、curvature_max_depth、pair_max_depth、interval_bits、sqrt_bits、max_cells、max_pair_nodes、max_pairs、cache_entries、max_constant_levels、max_block_nodes、max_union_cells、block_cache_entries。

resources包含free_bytes_reserve、node_heap_mib、child_shutdown_reserve_seconds及stage_budgets_seconds。最后一个恰含上述五stage的各显式上限，仍受同原deadline裁剪。K、tau和eta不从某个未知实际结果自动选。

必须保留实际continuous-E目录的四metadata以及large-arrays/complete-source-radial-panels.jsonl、large-arrays/source-piece-index.json至live query消费者结束；缺新query payload只按原R426职责返回精化未付，不用旧digest复原。

## 6. 五阶段必要读回及独立 held

    python COMPUTATIONS/root_20261116_current_C_actual202_M_postsolve_necessary.py \
      --directory ACTUAL_M_GEOMETRY_OUT --out FRESH_GEOMETRY_NECESSARY.json

标记BEGIN_R457_CURRENT_C_FROZEN_M_BLOCK_POSTSOLVE_NECESSARY和对应END。GITHUB_OUTPUT键仍postsolve_summary/bytes/sha256/readback_complete，内部JSON已用新schema。新增actual_first_parameter_source_binding给必要来源；实际大区间树/矩阵/mesh/角表仍仅完整身份和原计数，不全传输。

独立held仍使用真实same-job witness_plan和全部八个原参数：

    python COMPUTATIONS/geometry_20261116_current_C_actual202_M_postsolve_held.py run \
      --input ACTUAL_HELD_INPUT.json --input-sha256 ACTUAL_HELD_INPUT_SHA
    python COMPUTATIONS/geometry_20261116_current_C_actual202_M_postsolve_held.py readback \
      --directory ACTUAL_HELD_OUT --computations COMPUTATIONS --out FRESH_HELD_NECESSARY.json

输入键集保持schema、postsolve_directory、postsolve_procedure_sha256、postsolve_input、postsolve_input_sha256、witness_plan、witness_plan_sha256、held、resources、out。held八参数为active_depth、position_max_depth、position_radius_goal、interval_bits、sqrt_bits、max_position_cells、max_prefix_points、max_tail_witnesses；resources为held_budget_seconds、child_shutdown_reserve_seconds、free_bytes_reserve。

它重新绑定实际选中的R451或R457五阶段source/schema/input，并只要求原radial/atlas/shared依赖真实完成。metric/reach布尔仍不是前提。新标记BEGIN_R457_CURRENT_C_FROZEN_M_HELD_NECESSARY和对应END；原postsolve_held_summary输出键保留。没有改变原held/δE科学解释。

每一份≤90000字节，超限诚实不完整。三必要reader不会自行清理原大件；未来整job总owner必须汇总上游/新M/几何/独立held必要读回及全owner静止，才可清理自己的实际namespace。

## 7. 公共材料 API：显式定义而非被动执行

新公共材料文件在五阶段source pins中只是声明可用API；五阶段没有自动调用它，其complete_M_material_map_evaluator_executed仍false。

准确调用接口保持：

    phase = Material.bind_loaded_common_material(
        actual_current_accurate_bundle,
        first_material_transport=ACTUAL_FIRST_B_PATH,
        first_material_sha256=ACTUAL_FIRST_B_SHA,
        first_plan=ACTUAL_FIRST_PLAN_PATH,
        first_assembly=ACTUAL_FIRST_ASSEMBLY_PATH,
        budget_check=HOST_ORIGINAL_ABSOLUTE_CLOCK_CHECK)

首来源现在是两个明确的source/schema组合：

| 首记录 | policy schema | source SHA |
|---|---|---|
| 原R437 | R437-current-ten450-explicit-closed-parameter-policy-v1 | d7d01460f5a22f4fa2ca75ad36475688d65a465ba488d9caff65cb5ef13fb871 |
| actual202 R452 | R452-actual202-ten450-explicit-closed-parameter-policy-v1 | b49769f13f69bf30b82988b1ca57382c602d4b74bc3ae8a6c2b5d1e0ee3df7a8 |

B schema分别为policy schema加-actual-material-transport-record-v1。其完整首材料定义schema分别加-complete112-material-angle-definition-v1；112系数原words/准确dyadic/频率/密度/正弦系数全同原合同。R452分支另外读取B中first_construction_freeze指向的A，核A/B完整相同首定义与clock/CP/target/words。不是把R452 JSON重标R437。

current必须是真实R416、R441或R451-M准确cut bundle及其真实source_bundle七元组；后者依次paths、plan、assembly、target、saved、A、bindings。实际对象的class module/file/SHA核仍保。当前M全系数、双mean、真实native/radial负零和准确C/DAG责任没有改。

describe给准确Theta/唯一实lift inverse/空间C²条件合同。实际方法名及完整签名为：

    phase.evaluate_active_cell(piece_index, radial, angular, time_interval, lower,
                               interval_bits=ACTUAL_BITS,
                               max_inverse_steps=ACTUAL_INVERSE_BUDGET)

radial、angular、time_interval分别是原piece内闭径向、公共首q和原t区间，lower为实际反射侧；两个工作参数是显式keyword。此方法返回value/u/q/uu/uq/qq完整六jet。encode_active_cell(result)仅显式序列化给host原临时输出，不打印分包或创建文件。

B缺失时五阶段可继续，但本可选API不能被声称已经绑定；调用它仍需要真实B/plan/assembly。这不是新增几何门，而是未发生的函数调用不能伪填source。新helper不求BVP、不选M/mesh/角数、不造clock、不写raw，也不制造Loewner/reach/held/C²统一收敛结论。

## 8. 完整来源闭包与总入口责任

六件新源并不替代原R44220源/R45112源闭包。未来总request应逐项保原实际role pins，再加入六件新source以及本分支实际使用的已刊R449/R452来源。owner还明确 pin R456 的 owner/driver/client/sampler/worker 五件（bf7d writer 原已 pin），以实际原父记录注册；不能只加一个新父标签。

M owner直接保留原全部NATIVE_PINS、driver/checkpoint/old43f/lifecycle/deep/R441来源；额外保旧47fc source用于旧M父识别。205实际origin选择时再核56cb/227e/02e/32b和ee367候选源。

新五阶段直接表保原所有科学角色，替换的只是MESH_LAUNCH和MATERIAL role；旧47fc/db7仍以独立baseline pin保留。205 first A/B分支实际核89a/b497源。独立held保旧c5ae和新postsolve两个完整三元组，不drop旧source而假贴新名。

原driver395da、checkpoint18399、profilecc70、fullnative全源/源恢复身份继续真实读取。raw native配置内的M worker/algorithm来源仍由原driver和writer绑定；新owner不把legacy112仅靠维数重标M。

目前没有R457总workflow/request，亦没有选择未来M或资源参数。后继若把205冻结调用链作为内部子合同，必须记录本次真实GITHUB_RUN_ID/SHA，不继承旧205已经清掉的raw。全链精化和新场五阶段必须在同job cleanup之前显式执行。BVP/旧首次几何/新M/新几何/独立held错误和未访范围应分别必要读回，不把任何source发表写成已执行。

## 9. 只做来源文本工作

本次只有源码阅读、文本替换/完整diff、原JSON结构和字节SHA检查。没有import科学、AST、compile、fixture、benchmark或数值求值。没有提出新审批/审计门，也没有修改运行中的204/205或已刊原R442/R451。

附带完整diff和临时清单用于唯一发布者复核真实差异；它们不是实际科学输出、实际全场或未来accepted证书。
