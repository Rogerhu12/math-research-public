# R451 接口 — 真正完整 M 后的闭面、live metric、全 pair reach、独立 held 与公共材料 API

作者：OpenAI ChatGPT /root/exact_refinement（AI），2026-11-16。

## 1. 当前交付与边界

本包有12个独立运行源、一份条件证明和本接口。没有 workflow/request、实际 M、实际父场、运行号或新参数选择。源未在本地导入、AST、编译、科学执行、fixture 或测试；本地只写/读完整文本、形成差异和核字节身份。所有数学执行仍限定未来公开 Actions，root 唯一发布。

证明为 results/R451-complete-M-closed-geometry-and-common-material-registration.md，17245 B，SHA256 1ae001cd265314a8989b175ee45e7e0d29ce726d75d673c3372ff41193faf56a。

本次用 R442 当前 M 的真实 checkpoint，重新运行完整 radial/atlas/shared/live metric/block reach；独立 held 只在前三依赖完成后另行调用。原全 native/FD/physical/mean/全角/final 接受不改，原 clock/owner/quiet/必要读回保留。它不复用旧场几何结果。

R442 的20运行件已经原字节刊于22a454e3a4705fef552a1938beef655a8bd1ac53；其原 proof/interface 和完整 source closure 是本包上游。R441 原运行基线刊于 f2c5653000abedf08622e5e703dffd314aac662a，R448三编排源基线刊于4af72dc1cc28c5eb6485ac8f829b544630db3b31。R447 baseline helper 为完整小blob4ceff286d6df8fc12ec5c659ca1c60009da2bfee。

**真实兼容边界：** 新五阶段入口只消费 R442 owner。原193和joint203仅是它们真实 origin/deadline 来源；R442 原父集合仍是 R400/R431/R441/自身M。没有注册 R448→M，未声称 M→R448 双向联合已经完成；没有注册未来 R449/205。旧数学 consumer/source/schema 原样保留，不能给旧112 helper改标签称M。

## 2. 完整发布表

以下12件发布到 topics/visible-flex-larger-amplitude/computations/；完整当前字节均在独立工作目录 current-C-modes-postsolve-R451。

| 角色 | 文件 | bytes | SHA256 |
|---|---|---:|---|
| prefixMetric | geometry_20261116_continuous_ten_M_prefix_metric.py | 32797 | 56a3a9fed5b52130199e0fd6d6d6d72d6d12a82fbbf9c248e77608e8bfd056be |
| atlas | geometry_20261116_current_C_M_original_cuff_atlas.py | 29387 | 97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621 |
| cut | geometry_20261116_current_C_M_accurate_cut_patch.py | 26078 | 747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492 |
| cap | geometry_20261116_current_C_M_fixed_cap_balls.py | 23637 | 21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a |
| metric | geometry_20261116_current_C_M_live_query_complete_metric.py | 55048 | fc35c6408aacbf2131a89fbac37ca4ae98c1665d9fbdc4ba78a50a43ca7f3a47 |
| reach | geometry_20261116_current_C_M_complete_reach_cover.py | 60459 | e69cf21c3800c8ca8b145ac0ea89233ed59571a6c51ca02a7078211b2d254210 |
| block | geometry_20261116_current_C_M_complete_block_reach_cover.py | 45618 | 1915bc51508f2a2f8028594a8808fdeb902ea88782a161d94dae14da6b41340e |
| held | geometry_20261116_current_C_M_held_and_rigidity_inputs.py | 53783 | 9c5615bbf8f0c895d75b84d7aed0f4297a10c3b0b624336d93bb37b150715c51 |
| material | geometry_20261116_current_C_M_common_material_phase.py | 35335 | db7df14743f1f91dc507918e1676ee8198227a8f28c60d25fc55c83993af7fb7 |
| postsolve | geometry_20261116_current_C_M_postsolve_geometry.py | 61527 | c5aeb8ba8cfd1aebeeaf4f0305006398fedbc3de868f9e74a78135129d548642 |
| postHeld | geometry_20261116_current_C_M_postsolve_held.py | 43979 | 0020018c238f18f5afc9b9ac343d50b053a052bcc752d362e7f1bc1cd8b70647 |
| reader | root_20261116_current_C_M_postsolve_necessary.py | 27197 | e48b7b2626d478efb1e591db462a49bbc5b50573547ced0ce6bd122b8d4445da |

下表是每份完整 diff 的实际原基线。prefixMetric 的旧源在 R441 中仍保持 R400 字节；atlas至held 是已刊 R441；postsolve/postHeld/reader 是已刊 R448；material 是已刊 R447。没有以未发表草稿为基线。

| 角色 | 原文件 | bytes | SHA256 |
|---|---|---:|---|
| prefixMetric | geometry_20261115_continuous_ten_frozen450_prefix_metric.py | 32761 | 011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84 |
| atlas | geometry_20261116_current_C_resolution_original_cuff_atlas.py | 29116 | d0b03a367f3ece13b06949d5218a992e6ee3e9a41364499070d3f5f475a150a0 |
| cut | geometry_20261116_current_C_resolution_accurate_cut_patch.py | 26070 | 8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52 |
| cap | geometry_20261116_current_C_resolution_fixed_cap_balls.py | 23665 | ca53bdc5c0cdd5764065301f0edb1259d083fdffa9f3d767a5a38b4a7cafe364 |
| metric | geometry_20261116_current_C_resolution_live_query_complete_metric.py | 55053 | fd263af28a7d55a7246a49283d367e420786f48f16556dd5a7d61406b1c8459b |
| reach | geometry_20261116_current_C_resolution_complete_reach_cover.py | 60452 | 745b245eddd27c10522012756a33bd842b3883d918845de49cc2cdacbeed1a05 |
| block | geometry_20261116_current_C_resolution_complete_block_reach_cover.py | 45582 | f27556bcfbeb72ac3ad7142bbc5089e1168fdc7966fe91757e1a201b7dbfe957 |
| held | geometry_20261116_current_C_resolution_held_and_rigidity_inputs.py | 53737 | 144da57a9d55547fa3b85ccb43c0f4261db2e2dcb41e91094c8d3a16c9b7d7b1 |
| material | geometry_20261116_current_C_common_material_phase.py | 31871 | 305eaf50958788caa2a7d0174f361cb08d3cf47e08fd3a7c3f9b9c44292a4ab8 |
| postsolve | geometry_20261116_current_C_radial_resolution450_postsolve_geometry.py | 57405 | 64086e8dc283507442ab519f7fa139b748259948d2e9c5a419227363b33c67b8 |
| postHeld | geometry_20261116_current_C_radial_resolution450_postsolve_held.py | 43989 | 8ffa2e6fe2f9e30f5c4aada0f9adcbb9af2e28152e0ce019291bda5bffffbbcb |
| reader | root_20261116_current_C_radial_resolution450_postsolve_necessary.py | 27246 | a087f6b4fe1ace727c2867eab5d34a8915fec1a007996bb96ced8392d289c71f |

每件都有 role-complete-baseline.diff。manifest 记录完整原/新 bytes/SHA、公路径、本地路径及 diff 身份；这些比较文件只是可重得的临时工作材料，不要求入 Git，也不成为运行或数学门。

## 3. 哪些数学本来通用，哪些确实改维度

| 责任 | 实际处理 |
|---|---|
| prefix 精确 Hermite | 原338换为实际3M+2；三nodal jet、全部六系数、M个core完整核形状；所有零模均值保 |
| 材料 Phi | 原112换为实际M；准确 dyadic core 到 density/sine 的完整公式保留；原rho正下界不减 |
| shared/radial | 直接使用R442109507cd/db1f6fd3/86a88a66，N/steps/完整FFT与576/577责任保，非只重标 |
| cut target | 原R416三个准确C径向jet与全角复合不改；新M source tuple/target/CP字段真实绑定 |
| 固定帽 | 原Cartesian图、全部markers、disk分区/六jet/球公式不改；新shared/atlas来源 |
| metric | 原R251四严格测试、准确十族全支撑、prefix/尾/帽目标与全root计划不改；R426 live-query原provider复用 |
| reach | 原R422 AA/CC/AC全集、两反射片、self/缝/全marker/法向与相位责任不改；R435整块与singleton frontier保 |
| held | 原PrefixProofNodeAngles(field.M)、全prefix/尾/两帽/marker和O(3)责任不改；新实际field依赖 |
| 公共材料 | 原R447首112 capture原样；当前图接受新完整M，准确实逆/六jet链式仍原公式 |
| 编排 | 原五阶段、独立held、绝对钟和quiet保；新增真实R442 parent/schema/布局检查；不调用旧112科学入口 |

R442的完整求解尺寸仍是4M+2，物理3M+2、core M、native2M+2及两均值、M×2M far、(3M+2)×M endpoint。旧节点高模零只属于初猜。几何源不能因为初猜零就删新频率、core、native方向或角采样。

## 4. 真实来源闭包

新闭包是按实际调用分层的完整来源，不把一个未执行的同名旧模块当新运行：

1. postsolve 绑定 R442 owner47fc1aba、driver395da6c8、checkpoint18399ec7；当前 Saved86a88a66、radial109507cd、shareddb1f6fd3、profilecc70e769、全部 native/worker/client/bridge/utility 从 R442实际闭包继续核。
2. prefixMetric直接绑定新Saved、原72c4635e完整十族factory、675ab8df完整jet解释器、a601e5b5四Loewner核。
3. cut绑定新Shared/PrefixMetric、原72c4635e和675ab8df；准确target/C/cut模型与全部source件仍须通过实际原loader。
4. atlas绑定新CP/profile/shared与原72c4635e/f12f7470；cap绑定新shared/atlas、原a3ada50b帽数学及原mixed-phase球核。
5. metric绑定新cut/prefix/atlas/cap和原a601e5b5/f12f7470/07fc4e41 live provider/28b7245a原R418算法来源。固定旧query和新query保持各自真实身份。
6. reach绑定新cut/atlas/cap及原675ab8df、0b52a408局部cuff、f6214d1d完整相位、原mixed-normal/diameter核；block只加载新reach并保原R435算法。
7. held绑定新cut/atlas/cap及原675ab8df、a40dc7a5完整prefix非平面核、原mixed-normal/diameter核。无metric或reach通过依赖。
8. material绑定实际对象的class module：旧R416/R441两完整来源分支保，新R451cut747b9d1f/Saved86a88a66/Shareddb1f6fd3明列；原Active675ab8df。首材料数据仍来自R437d7d01460、原Saved1c7a2e1c的真实capture。
9. postHeld只复用原79296f4f reader里的标准库 process_quiet；不调用它的112数学selector/build。它选择本新postsolve source/schema/input三元组，并实际调用该模块的绑定、producer_completed和OwnedChild。
10. 本包需要原proof文件的实际bytes/SHA，沿源码PROOF_PINS完整核；其中R443实际110de42a仍是完整闭目标材料拉回来源，R447实际e24b6c26是全实逆/强C2来源。

R442原native/求解完整 source-root 由真正 checkpoint/actual_runtime_source_closure 绑定，不因本新后继省掉。实际 Actions 必须同时保有这些原小源及原同job数据；文件缺失不能凭SHA恢复科学对象。manifest是发布目录，源码内固定pin和原loader才是运行时消费合同；不追加一个独立source审计程序。

## 5. 五阶段输入的真实 schema 和路径

主入口：

    python geometry_20261116_current_C_M_postsolve_geometry.py \
      --input ACTUAL_INPUT_JSON \
      --input-sha256 ACTUAL_INPUT_SHA256

输入schema为：

    R451-current-C-complete-M-same-job-live-query-block-geometry-v1-input-v1

结果schema为：

    R451-current-C-complete-M-same-job-live-query-block-geometry-v1

必需路径/身份字段：

| 字段 | 必须指向 |
|---|---|
| upstream_kind | 字面R442-complete-M |
| namespace | 原owner已有RUNNER_TEMP内namespace；不得重建或改名字冒同现场 |
| upstream_launch_directory | 当前真实R442 owner的输出目录 |
| upstream_result_sha256 | 若给出，必须是该真实owner result原SHA；当前代码支持省略后读取真实文件 |
| job_deadline / job_deadline_sha256 | 原193或joint203同一份实际deadline文件 |
| geometry_directory | 当前M owner真实fresh采样result目录，逐receipt对上CP |
| continuous_e_directory / continuous_e_result_sha256 | 当前CP/采样同一原C目录及result |
| computations / proof_directory | 当前明确source closure与原proof真实路径 |
| source_topic | 与R442输入tail_source_root相同的原runtime source-root |
| first_shared_directory / first_shared_result_sha256 | 首次真实完整shared field/plan，不是自行合成construction |
| out | namespace内新的独占兄弟目录；不能覆写原owner/场/C树 |

current/fixed target、actual_resolution、全部10字、数组及native/final acceptance都取自真实CP，不由输入另塞一个宣称成功的布尔。新prefix/cut/shared会真正加载当前M的全数组。

### 5.1 原 clock 和 resource 字段

resources精确提供：

- free_bytes_reserve；
- node_heap_mib；
- child_shutdown_reserve_seconds；
- stage_budgets_seconds，键恰为 radial_replay、original_cuff_atlas、shared_field、metric、reach，每项显式正资源秒。

原deadline schema可且只可为真实origin对应的 request193-owned-job-science-deadline-v1 或 request203-owned-job-science-deadline-v1。schema/source/recipe/bytes/SHA/run/commit一起核；science_seconds_from_namespace=18900、readback_reserve_seconds=2700保原来源。每子阶段按当时剩余时间和shutdown reserve裁剪，资源未付保未开始原因；没有为新M重新开18900秒。

radial命令继续使用原capacity loader07d45b95。仅在这个真实子进程环境显式写：

    VISIBLE_FLEX_SOURCE_TOPIC = actual source_topic
    VISIBLE_FLEX_TAIL_MODE_CAPACITY = actual checkpoint M
    VISIBLE_FLEX_TAIL_CAPACITY_RECORD = this geometry output/radial-capacity-record.json

这个差异解决新M调用不能继承原origin的112容量。元数据保存 actual_radial_capacity_binding 和返回后的 actual_radial_capacity_receipt；reader把它们原样作为必要生命周期字段返回。N/steps不在此回退到旧值。

### 5.2 construction 与真实首闭面

construction键恰为cut_correction_width、cap_height、fixed_cap。fixed_cap包含完整markers列表，可真空但不能自动补空。原first plan里的每个数按实际float64 word或准确整数比较，包含符号零、marker顺序与全部字段；cuff保持原实际C word。

首shared可且只可是原R4096a5f949a、R4411ceda9d3、R442db1f6fd3三元来源；首CP target与首shared target完全绑定。current-M target只去已声明M元数据/schema/specification SHA后比较完整其余字段。此字段比较不声称首次与当前Phi/core/SE2逐词相同。

fixed_closed_construction记录原首次result/plan/CP、完整construction词、首/当前target身份、首/当前M和R443 proof。它明确记录M材料API已注册但在本五阶段未执行；不以输入相同ten字就宣称全闭g已经在同材料图中实际验证。

### 5.3 metric 和十一项同C query 参数

metric原六参数保留：eta、interval_bits、sqrt_bits、initial_angular_depth、max_depth、max_visited_cells。eta保原准确有理文本，不由新M选择。

c_queries精确含原R426十一项：

| 参数 |
|---|
| precision_bits |
| integral_absolute_bits |
| integral_relative_bits |
| analytic_guard_bits |
| integral_evaluation_limit |
| value_width_bits |
| integral_max_depth |
| inverse_max_depth |
| max_panels |
| max_nodes |
| budget_seconds |

原CLI资源域完全保留，参数逐项显式传 --c-query-… 。provider从同现场原complete-source-radial-panels和source-piece-index重建原source视图，保同C/同lambda/同根族；不是从删失SHA重新制造原数据。缺这些真实payload只得到该live query责任未付，不把另一个run当当前C。

### 5.4 reach 原全部参数

reach包含curvature_upper、target_reach、active_depth、curvature_max_depth、pair_max_depth、interval_bits、sqrt_bits、max_cells、max_pair_nodes、max_pairs、cache_entries、max_constant_levels，以及R435的max_block_nodes、max_union_cells、block_cache_entries。

K和tau保原准确有理文本，原全部曲率/距离/法向/local-path和相位判据不变。没有新增M-dependent接受阈值、没有把失败块当删除pair的许可。

## 6. 五个角色及实际完成语义

| stage | 当前producer | 需要前项 |
|---|---|---|
| radial_replay | R442109507cd完整M/2means重放 | 实际R442接受和源绑定 |
| original_cuff_atlas | 新97e4a49f原C cuff/准确target attachment | 相同实际CP；radial失败仍可独立返回atlas |
| shared_field | R442db1f6fd3完整节点/系数 | radial与atlas的真实完整结果 |
| metric | 新fc35c640同C live-query完整metric | 完整shared/atlas |
| reach | 新1915bc51全block/singleton reach | 完整shared/atlas；不以metric通过为门 |

procedure.json保五行started/status/原child exit/error/完整未访阶段。producer_completed仍按原已刊source合同处理真实completed/error等，不把编排退出0当math完成。

new_cut还会建立独立准确field identity和准确target成员；旧数值native结果、准确有限几何解释、相对准确C的目标包含、全局reach和held分别读回，不互相冒充。

## 7. 必要 reader 和临时数据责任

主reader：

    python root_20261116_current_C_M_postsolve_necessary.py \
      --directory ACTUAL_POSTSOLVE_DIRECTORY \
      --out ACTUAL_NECESSARY_JSON

结果schema：

    R451-current-C-complete-M-block-postsolve-one-necessary-conclusion-v1

唯一frame：

    BEGIN_CURRENT_C_TEN_FROZEN_M_BLOCK_POSTSOLVE_NECESSARY
    END_CURRENT_C_TEN_FROZEN_M_BLOCK_POSTSOLVE_NECESSARY

它只读标准库JSON/实际metadata，不导入科学或重新算数值。必须见procedure真正finally返回和每个原owner/group静止才读closed结果。保存五角色实际源/结果原SHA/bytes、原失败字符串、当前部分scope和原rank/地址；原stderr只按既有8192字节必要excerpt及完整身份返回，省略正文范围明确，不把大stderr或科学树编码拆传。

metric保完整原未付root/cell地址和R426必要state；reach保完整当前block、singleton空间/相位、curvature/frontier与未开始后缀；它们不由计数推造成功。原历史大ledger值不返，只保身份和明确未逐值读取范围。

90000字节是单份必要结论界限。超限明确summary/readback incomplete并exit70；不会拆包、截取原数组或借多个摘要绕界。原详细临时文件仍留在Actions，当前程序不cleanup。未来外层只有在所需readback成功、原owner静止后才可按原namespace生命周期清理；否则保partial并留至runner销毁。

## 8. 独立 held 的真实调用

入口：

    python geometry_20261116_current_C_M_postsolve_held.py run \
      --input ACTUAL_HELD_INPUT_JSON \
      --input-sha256 ACTUAL_HELD_INPUT_SHA256

输入schema：

    R451-current-C-complete-M-same-job-held-after-shared-v1-input-v1

输入字段严格为schema、postsolve_directory、postsolve_procedure_sha256、postsolve_input、postsolve_input_sha256、witness_plan、witness_plan_sha256、held、resources、out。

held参数仍是原active_depth、position_max_depth、position_radius_goal、interval_bits、sqrt_bits、max_position_cells、max_prefix_points、max_tail_witnesses；resources只含held_budget_seconds、child_shutdown_reserve_seconds、free_bytes_reserve。没有新namespace/deadline长度。witness_plan仍是原R425完整schema，不能把新的点计数当旧完整witness证明。

本source只注册本次c5aeb8ba postsolve结果/input完整三元组。它复用真实Procedure.bind再核相同CP/clock/C/源，要求radial/atlas/shared各有实际完成回执；不要求metric/reach通过。其调用newheld9c5615bb保全prefix/尾/两帽/全markers/O(3)与全部原未付字段。

读回：

    python geometry_20261116_current_C_M_postsolve_held.py readback \
      --directory ACTUAL_HELD_OUTPUT \
      --computations ACTUAL_COMPUTATIONS \
      --out ACTUAL_HELD_NECESSARY_JSON

单份必要frame为BEGIN_R451_CURRENT_C_FROZEN_M_HELD_NECESSARY / END_R451_CURRENT_C_FROZEN_M_HELD_NECESSARY。独立90000字节限制、quiet、原metadata/error/未完成scope和不cleanup责任保持。whole-image/rigidity/Delta-E各自责任不是一个source guard的布尔别名。

## 9. 公共材料 M API：真实可调用但默认不强制执行

新增geometry_20261116_current_C_M_common_material_phase.py绑定原R447的准确数学解释。本包postsolve PINS包含其db7df147完整SHA，fixed_closed_construction记actual API file/SHA与executed=false；这只登记真实可调用源，没有强制新增第六阶段。

未来在同一个已加载准确cut对象的Actions进程中，调用：

~~~python
material = Material.bind_loaded_common_material(
    current_accurate_cut_bundle,
    first_material_transport=actual_first_R437_record,
    first_material_sha256=actual_first_record_sha,
    first_plan=actual_first_plan,
    first_assembly=actual_first_assembly,
    budget_check=existing_absolute_deadline_check,
)
definition = material.describe()
cell = material.evaluate_active_cell(
    actual_piece_index, complete_radial_interval, complete_common_q_interval,
    complete_original_time_interval, actual_lower_sheet,
    interval_bits=explicit_interval_bits,
    max_inverse_steps=explicit_optional_inverse_work,
)
~~~

这是接口形状，不是已经调用或填写真实数据。API不自己建进程、时钟、输出目录或删除数据。其可选cell结果属于当前进程，encode_active_cell仅显式序列化给内部临时消费者，不打印、不split、不返大science树。

当前图注册：

| family | 实际source |
|---|---|
| R416-original-resolution | 原28417b93 cut / 1c7a2e1c Saved / 6a5f949a shared |
| R441-current-resolution | 原8811f89c cut / fb6e181c Saved / 1ceda9d3 shared |
| R451-current-M | 新747b9d1f cut / 86a88a66 Saved / db1f6fd3 shared |

旧两branch仍要求完整原target identity相等。新M branch保同一实际R442全target/C/根族/DAG/十词，仅去已声明M表示字段。加载对象class module、源basename/SHA、实际binding和七元组owner关系都对应，不只看schema名称。

**首次材料记录仍是原R437d7d01460的完整112 capture。** 它读实际首plan/assembly/target/全部core词、原rho下界和完整registration/gauge；没有合成首M记录，没有从旧hash恢复。当前M可不同，但Saved.M、field.M、core长度都必须同一个真实值。

原准确式为 $R_\alpha K_M(x,I_M(\Theta_0(q)-\alpha))$，保全实lift、完整逆像盒、全部M项及两均值。不同M不改变原六jet链式；所有可选精度/迭代只是work参数，未达宽度不创建native门。该API没有执行全closed sweep，也没有自己消费已付metric/reach/held证明并将总flag置true；条件转移在R451/R447纸证中明确。

## 10. 实际依赖原件和报告字段

同job需要直到全部已接消费者结束仍真实存在：

- R442 owner result/input/adapter-status/close/lease、原origin result/input/recipe/deadline；
- 当前完整checkpoint、所有fullDN/physical/nodal/core成员和原source/runtime receipts；
- fresh完整当前M geometry/config/rows/far/point采样结果；
- 原C result、input-binding、query-plan、query-results；
- 原C large-arrays/complete-source-radial-panels.jsonl 和 source-piece-index.json；
- 首次真实shared result/plan/assembly及要执行材料API时的真实R437 capture；
- 当前完整radial节点/系数账、atlas、shared全部成员和geometry consumers的临时账。

缺原件的scope诚实未付。不要用一个成功父SHA代替当前数组，不从旧大账hash重建未知值，不把R442最新M场冒旧193/450字段。

五阶段输出保upstream_frozen_M_acceptance_observed、actual_refined_M_selected、actual_frozen_M_not_resolved_again、selected_upstream_kind、actual_resolution、source/input/CP所有身份，另保old_parent_geometry_certificates_reused=false。凡未实际启动/未返回/预算截止的数学scope不补默认成功。

source中complete_task_certified仍false；所有几何原结果各自存在时才返回其原字段。source_only与数学完成、传输完成、进程正常退出明确分开。

## 11. 当前没有付的责任

本次没有实际M/R442 solve，没有新radial/field/metric/reach/held/raw物理结果，没有保证原18900秒能完成任一未来M；没有证明随着M→∞的统一收敛或准确continuous C ODE的真实轨迹。

没有原R448父到M的新组合，没有未来205分支，没有首个M的R437 capture producer。公共材料API只把当前M放到真实首次112图下，不能把默认未执行写成已执行。原第一闭面W/H/markers/材料和尾帽解释仍是固定全闭g的必要条件。

R451程序也不自派发；root按完整文本/来源正常集成并独占发布。不存在本包额外要求的fixture、代理复审、批准或数值对拍前门。
