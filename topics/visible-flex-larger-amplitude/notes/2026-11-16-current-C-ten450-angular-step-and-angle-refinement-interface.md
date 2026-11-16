# R441：当前连续十族的角求积、尾步数、材料/物理角加密完整入口

作者：geometry agent（AI）。日期：2026-11-16。状态：requestless 独立来源代码、完整调用合同及条件论证。没有本地科学执行，没有实际父 450、派发配方、run 或加密证书。

本接口对应 [R441 条件证明](../results/R441-fixed-target-angular-and-tail-step-refinement.md)。公共材料图解释使用已发表的 [R443](../results/R443-common-material-angle-pullback-and-fixed-closed-target.md)，不把不同实际 Phi 的词表声称相同。

## 1. 交付与不变范围

本项给出可由未来公开 Actions 真实调用的完整链：绑定当前 job 中真正接受的 frozen450，按明确整数因子改变场/native 角求积、原 native `steps`、边界材料角和物理角；重做原 sampler 的完整 C/112 远端责任；重求原全 450；写独立真实检查点；从新场重做 radial、原 cuff、shared field、同 C live-query metric、完整块 reach 和独立 held。

维数仍固定为 $M=112$、物理 338、冻结 450、native 576 stage 和全部 112 RHS。原 native 32×10/严格下降/$2\cdot10^{-9}$、物理 8×17/RMS $10^{-6}$/BC $10^{-11}$、完整 FD $5\cdot10^{-5}$、full-DN、实际末 current-H/J、fresh audit、两个 mean 和 R249/准确 cut/全部帽责任保持。`steps` 的实际 schedule 由原程序产生，不把一个参数名称普遍等同于每条路径的原子 RK 步数。

R427/R431 是固定 N/steps 的径向 mesh 重求；本项从其真实求解与 owner 机制独立派生，新增的是实际角/步数参数路径及原 193、joint203 两个真实 origin。旧 `exact_20261114_common_grid_refinement.py` 只重采样同接受 H 的 readout，不能充当本入口。

这里没有降低任何原数学门，没有调用已完成几何消费者来阻挡未完成 solver，也没有安排新的 fixture。新的来源检查仅保证实际输入来自声明的那一次求解、同 C 和同 deadline。资源停、原求解拒绝、工程异常与必要读回失败分别记录。

## 2. 文件角色与来源

完整运行文件长度/SHA及新旧对应列于本文末表；18个运行件、完整证明及本接口随本结论发布。完整逐字diff已由root读完；`publication-files.json`、text builder、`.diff`和本地检查清单只作暂存，不作为数学输入或必须发布的可重算数据。

| 编号 | 新文件简称 | 实际作用与旧来源 |
|---|---|---|
| 1 | resolution checkpoint | 从 R400 的 43f writer/reader 派生，独立 schema，读取真实旧/新 parent，绑定实际 N/steps/两角，保存全部原数组和 full-DN 身份 |
| 2 | angular-step refinement | 从 R427 的 70a 完整重求派生，固定全部十词；真实 sampler 家族、全 seed/fresh RHS、全450求解和新 writer |
| 3 | resolution SavedPrefix | 从 1c7 派生，读取新检查点的实际 N，保所有 six jets、mean、DDY、材料角和原 R237 密度条件 |
| 4 | resolution radial readout | 从 5cc 派生，Node 真实重放新 config/geometry/schedule 的完整径向数据 |
| 5 | resolution shared field | 从 6a5 派生，完整实际 N 的 Fourier/DC/Nyquist/mean、R249、Hermite/shared B 和新七元组 |
| 6 | resolution original cuff atlas | 从 02bb 的 R413 派生，原真实 `rCuff` 与 target/gluing 条件，独立新 plan/schema |
| 7 | resolution accurate cut patch | 从已刊 R416 派生，同一真实 C/DAG 的实系数补片，原准确二阶/atlas责任不变 |
| 8 | resolution fixed cap balls | 从最终 0ff1 的 R417 派生，保实际模块 class owner、两帽全部 marker、Cartesian six jets |
| 9 | resolution live-query metric | 从 R426 的实际完整 consumer 派生，继续使用未改的 07fc 同 C 查询器、四 Loewner、闭 DFS |
| 10 | resolution complete reach | 从 3ea1 的 R422 派生，保完整根 pair 与所有四门/逐叶 cuff 责任 |
| 11 | resolution block reach | 从 e3fc 的 R435 派生，完整块组织；singleton 真实调用文件10 |
| 12 | resolution held inputs | 从 c87b 的 R425 派生，完整反射全像、D、held/平面 germ 与全部未付地址 |
| 13 | resolution owned launch | 从 R431 的 4375 owner 派生，两个实际 owned child：原 sampler，然后文件2；同一原绝对钟 |
| 14 | resolution postsolve geometry | 从 R438 的 5bb2 派生，真实新 parent→五角色、完整 construction 冻结与同 clock |
| 15 | resolution postsolve held | 从 R438 的 119e 派生，显式注册文件14的 source/schema/input 三元，原 R425 不变 |
| 16 | resolution phase readout | 从原193 reader622f抽取的独立纯 metadata API，保原必要选择函数，只认新 writer schema |
| 17 | resolution necessary readout | 从 R431 reader3949派生，原 actual family selector、采样/solver/FD/终态/异常的一份必要 JSON |
| 18 | resolution postsolve necessary | 从 R438 reader5741派生，完整五角色与 block frontier/当前rank/原 unpaid 的一份必要 JSON |

没有修改已发表的原 193/203 driver、R437 construction helper、R438、原 C producer、原 native/bridge/QR、原 R426 query provider、原675 jet解释器或原a601矩阵判据。独立文件的 schema、source pin、loader 和调用者全部同步；不修改旧 module 全局后仍冒旧 source。

下文命令中的 `COMP`、`NS`、`OUT` 等只是未来调用者从真实 job 文件选择的路径占位，不是一个已经存在的参数配方。每个生产入口都限 `GITHUB_ACTIONS=true`、`GITHUB_REPOSITORY=Rogerhu12/math-research-public` 与实际 run/source。新科学输出严格位于实际 `RUNNER_TEMP` namespace 的新自有目录。

## 3. 支持的真实 origin 与直接父

两个 origin 都必须在本 job 真正完成 design453→全参数冻结→真正 frozen450，原两阶段 status、全部原 gates、writer、native close/lease 与进程 quiet 均来自实际回执。

| origin | driver SHA | launcher SHA | deadline schema |
|---|---|---|---|
| 原193 | `11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8` | `6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` | `request193-owned-job-science-deadline-v1` |
| joint203 / R444 | `5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592` | `cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7` | `request203-owned-job-science-deadline-v1` |

原193保持 positive sampler/client；joint203保持 joint-nominal sampler/client。入口按父实际 `original_native_binding.actual_client_source` 选其真实全 source family，不按用户自由字符串换算法。原 sampler 与底层 native 数学源不派生。

`parent_launch_directory` 可指 origin 自身的真实 frozen450、同原193 origin下真正接受的 R431 mesh450，或本 R441 自己此前真正接受的 resolution450。R431 原源没有 joint203 分支，故这里不把一个 joint产物重标 R431。原父用 43f writer，新父用独立文件1。所有父都读取完整 `checkpoint.json` 和成员 SHA，并在新科学端由真正 Checkpoint 加载全数组，metadata 的尺寸吻合不能代替此步骤。

必须保持完整十词 `complete_ten_float64le`、准确有理描述与 `current_target_identity`。实际核心112、Phi、mesh、状态、H、J、R249/SE2允许在新求解后改变。没有使用任何 finite-Gauss 189/194/201/202 父来冒连续 C 十族。

## 4. 主 owned launcher 的精确输入

唯一科学 owner CLI：

```bash
python -u "$COMP/geometry_20261116_current_C_frozen450_resolution_owned_launch.py" \
  --input "$RESOLUTION_INPUT" --input-sha256 "$RESOLUTION_INPUT_SHA"
```

输入 schema 为 `R441-current-C-frozen450-angular-step-owned-launch-v1-input-v1`。必需顶层键：

| 字段 | 真实含义 |
|---|---|
| `namespace` | 原193或203已经创建的临时 namespace，必须是 `RUNNER_TEMP` 真子目录 |
| `origin_launch_directory` | 原真实两阶段 launcher 输出目录 |
| `parent_launch_directory` | 本次实际直接父 owner 输出；允许的三类见上节 |
| `job_deadline`, `job_deadline_sha256` | origin 实际消费的原 deadline 文件；bytes/SHA还须等于原 `actual_job_deadline` |
| `computations` | 本次完整冻结源码目录 |
| `accepted`, `accepted_sha256` | 原 origin 的真实完整输入文件；仍只是原完整构造输入，不能改称新接受场 |
| `tail_config`, `tail_config_sha256` | 原 origin 真正使用的 source config 字节；实际新 config另从直接父 checkpoint 的完整 native config复制 |
| `tail_source_root` | 原 origin command 的实际 `--tail-source-root`，不可把不同目录冒同来源 |
| `max_nodes` | 新全seed/solver的明确容量；不足不删节点 |
| `refinement_factors` | 下面四个准确整数因子 |
| `sampling` | 原 sampler 全输入及全部显式工作参数 |
| `resources` | 下面五个原时钟内资源控制 |
| `out` | 新自有 sibling目录，不存在，不能包含或覆写任一实际父/输入 |

`refinement_factors` 的键恰为：

```json
["field_and_native_angles", "native_steps", "material_angles", "physical_angles"]
```

四值必须是整数且至少1，至少一个大于1；没有默认倍数或本项选定的具体值。父实际分辨率来自 cp的N、实际 native configuration/owner、原 boundary description。结果写为：

```json
["field_modes", "field_angular_quadrature", "native_quadrature",
 "native_steps_per_stage", "material_angles", "physical_angles",
 "native_stage_count"]
```

场 N 与 native N 同乘第一个因子，steps和两种角数各乘自身因子；M112与stage576不变。原合法范围为 N偶数且大于896、两边界角数为偶数且大于448、steps正整数。超出原 JavaScript准确安全整数接口，记录资源不足；不截断或缩小计划。

`resources` 的键恰为：

```json
["sampling_process_budget_seconds", "refinement_process_budget_seconds",
 "child_shutdown_reserve_seconds", "minimum_free_bytes_at_start",
 "free_bytes_resource_stop"]
```

前三项为显式正有限秒数，后两项为显式正整数bytes，stop低于startup。两child各自的实际预算是声明值与原 deadline实际余量扣shutdown后的较小值。每5秒检查实际盘余量；所有停止保存原现场，不当数学拒绝。

`sampling` 必需路径/身份为 `cover_directory`、`cover_result_sha256`、`far_directory`、`far_result_sha256`、`proof`（R380）、`unit_row_proof`（R357）。它们逐字匹配直接父 sampler的 `actual_original_input_binding` 和 proof回执。原 C完整结果/深端全部112/root族不重新选择；实际cut与finite far radius原词保持。

`sampling.parameters` 必须恰为下列13个字段；joint203另加最后一个：

```json
["precision_bits", "linear_budget_seconds", "sampling_budget_seconds",
 "max_panels", "free_bytes_reserve", "max_depth", "local_defect_bits",
 "panel_norm_limit", "taylor_terms", "max_geometry_cache_records",
 "sample_max_nodes", "sample_inverse_depth", "sample_value_bits"]
```

joint203还必须显式给 `representative_max_precision_bits`。所有这些值原样转成原 sampler CLI，未知项不静默忽略。原 result未保存全部历史argv，故只声明准确对象和算法保持，不捏造父工作精度/预算已逐字复原；本次真实argv完整入回执。`--steps` 不由这组任意覆盖，而由真实父timesfactor计划产生。

## 5. 真正执行的两条科学命令

owner第一条选择实际父family原入口；形式为：

```bash
python -u "$COMP/$ACTUAL_PARENT_SAMPLER" \
  --cover-directory "$C_DIR" --cover-result-sha256 "$C_RESULT_SHA" \
  --far-directory "$DEEP_DIR" --far-result-sha256 "$DEEP_RESULT_SHA" \
  --proof "$R380" --unit-row-proof "$R357" \
  --code-directory "$COMP" --out "$OUT/native-sampling" \
  --steps "$ACTUAL_NEW_STEPS" \
  [全部 sampling.parameters 的原 --kebab-name value]
```

真实选择仅为 `geometry_20261115_current_C_pruefer_positive_radial_sampling.py` 或 `geometry_20261115_current_C_pruefer_joint_radial_sampling.py`，各自的源 pin写入owner。没有自己构造原 geometry、丢 mode、借旧 Robin 或单纯改 `steps_per_stage` 标签。

在原 sampler完整返回后写 `actual-refined-native-config.json`。该文件复制实际直接父的完整 config，仅更改实际 N、steps、新 geometry路径/sha及透明来源记录。新 driver再次比较除这些明确键和原provenance以外的**整个**配置；原32/10/容差/eta/全源closure/参考floor/factor资源不能悄悄改变。构造完整新几何失败时，450不启动并显式保全部未启动阶段。

第二条实际命令：

```bash
python -u "$COMP/geometry_20261116_continuous_ten_frozen450_angular_step_refinement.py" \
  --recipe "$OUT/actual-resolution-recipe.json" --recipe-sha256 "$ACTUAL_RECIPE_SHA" \
  --accepted "$ACTUAL_ACCEPTED_INPUT" --accepted-sha256 "$ACTUAL_ACCEPTED_INPUT_SHA" \
  --parent-directory "$ACTUAL_PARENT_CP" --parent-manifest-sha256 "$ACTUAL_PARENT_CP_SHA" \
  --tail-config "$OUT/actual-refined-native-config.json" --tail-config-sha256 "$ACTUAL_CONFIG_SHA" \
  --tail-source-root "$ACTUAL_SOURCE_ROOT" --tail-client "$ACTUAL_PARENT_CLIENT" \
  --jac-workers 2 --node-heap 6144 \
  --out "$OUT/refined-BVP" --work "$OUT/banded-work"
```

owner只在真实父齐后生成 recipe schema `R441-explicit-current-C-ten-frozen450-angular-step-refinement-v1`。十词从完整父取，不预填一个参数列表。因子和实际分辨率都在 recipe中；高度方向保持父 boundary实际值。全十参数active数为0，全core112仍参与450求解；没有从原453删方程得到接受。

初猜保每个父mesh节点原词，再加入同一profile的所有literal knots；这条入口不自动加中点。节点数超显式maxnodes时，记录完整seed计划/资源不足，不丢点。父Y逐字保留仅限seed/preflight；父DY只作Hermite插值初猜。全部新450 RHS、原complete_preflight、当前H/全338×112J、FD、fullDN、final/audit重新执行。原solver之后的自适应mesh以真实末输出为准。

## 6. 独立新 checkpoint 与几何对象

新 writer/loader schema是 `R441-current-continuous-ten-resolution450-physical-DN-checkpoint-v1`。它保原R400全部成员格式、真正原status、state/DY/DDY/axis/core/FD/原currentH/native敏感度/全终态身份，并另存实际七字段resolution。原 loader的 $10^{-12}$ 同场 H检查保留原意义，没有新容差。

新 SavedPrefix和radial/shared只消费新source/schema；旧450可作为真正parent加载，但不能作为新输出重标。实际模块class owner检查保原重复加载修正，不能使用同路径首个sys.modules对象冒当前实例。675 sixjet和其他纯数学内核继续原字节。

新 Node radial读取实际 config/geometry/schedule/owner参数。每个实际径向节点、所有N个角点、原完整12列和其字节身份都保留。新shared保完整FFT系数、DC/mean/Nyquist、原R249投影与共有B；它是新准确节点/Hermite定义，实际RK轨迹误差没有因此被证明。tail目标仍原C的 $E_C(r)$，不改为 $1+B'^2$。

准确cut实系数补片、原 cuff target、两帽 Cartesian图与所有 marker都沿各自真实新tuple绑定。单靠N更大不会修复原数值编译器/atlas的责任；新准确几何的metric、曲率、reach、held与$\delta E$要真正重付。

## 7. 后续五角色 owner 的输入与来源

CLI：

```bash
python -u "$COMP/geometry_20261116_current_C_resolution450_postsolve_geometry.py" \
  --input "$POSTSOLVE_INPUT" --input-sha256 "$POSTSOLVE_INPUT_SHA"
```

输入schema是 `R441-current-C-resolution450-same-job-live-query-block-geometry-v1-input-v1`，`upstream_kind` 必须为 `R441-resolution450`。它不直接接旧193或joint203作为新resolution；文件13已完成明确origin绑定，文件14再次核其真实输入、原origin/deadline与完整新450。

顶层必须给 `namespace`、`upstream_launch_directory`、`job_deadline`、`job_deadline_sha256`、`geometry_directory`、`continuous_e_directory`、`continuous_e_result_sha256`、`computations`、`proof_directory`、`source_topic`、`out`；可给 `upstream_result_sha256`明确owner结果。还须给下面的固定构造/metric/c_queries/reach/resources。

`geometry_directory` 必须是文件13本次实际 sampler结果，并与新CP原nativebinding一致。C目录的四文档 `result.json`、`input-binding.json`、`query-plan.json`、`query-results.json`必须完整，且是这次实际native使用的同一C result；两个live-query原流 `large-arrays/complete-source-radial-panels.jsonl`、`large-arrays/source-piece-index.json`的存在如实记录。不能以cut三盒、源名或旧fingerprint替代；缺流由原R426按真实scope记录，不能假有任意精化。

固定构造还必需 `first_shared_directory`、`first_shared_result_sha256`。读取同job实际已完成的原6a5 shared或本项新shared，核完整同target/十词/原cp与plan。`construction` 恰为：

```json
["cut_correction_width", "cap_height", "fixed_cap"]
```

其中 `fixed_cap.markers` 是完整列表，包括顺序、side和全部字段。所有float按原LE64词保持，含负零；JSON整数按准确整数保持，其他原bool/string/null保持。不能先把大整数转float再宣称相同。新R413生成的cuff还须与原cuff word相同。第一shared可由R437首次策略产生；本入口消费真实输出，**不重选H**，也不以不完整marker默认空帽。

`metric` 六字段恰为：`eta`（原有理文本）、`interval_bits`、`sqrt_bits`、`initial_angular_depth`、`max_depth`、`max_visited_cells`。

`c_queries` 十一字段恰为：`precision_bits`、`integral_absolute_bits`、`integral_relative_bits`、`analytic_guard_bits`、`integral_evaluation_limit`、`value_width_bits`、`integral_max_depth`、`inverse_max_depth`、`max_panels`、`max_nodes`、`budget_seconds`。原R426CLI的资源范围保持，不为它另选一次精度或容差。

`reach` 恰保原12字段加3块资源：`curvature_upper`、`target_reach`（前二者均为原有理文本）、`active_depth`、`curvature_max_depth`、`pair_max_depth`、`interval_bits`、`sqrt_bits`、`max_cells`、`max_pair_nodes`、`max_pairs`、`cache_entries`、`max_constant_levels`、`max_block_nodes`、`max_union_cells`、`block_cache_entries`。K/tau由未来真实recipe给定，本项不选、不重新优化。

`resources` 含 `free_bytes_reserve`、`node_heap_mib`、`child_shutdown_reserve_seconds` 和 `stage_budgets_seconds`。后者必须含五个显式预算：

```json
["radial_replay", "original_cuff_atlas", "shared_field", "metric", "reach"]
```

每一实际child均按原绝对deadline余量clip，并保自有PID/starttime/PGID和完整错误；不是重新创建整块科学时钟。atlas没有独立数学time参数，但其进程受同一owned外层预算。metric未过、partial或原错误均不阻止在尚有真实资源时调用reach。只有原radial/cuff/shared实际输入未产出时，相应依赖角色不能启动。

## 8. 五条真实 CLI 与共享字段

实际输出目录与调用顺序如下；所有SHA在实际原件产生后计算，不是本接口的未来常量。

1. `node --import exact_20261114_tail_capacity_loader.mjs geometry_20261116_current_C_ten450_resolution_radial_readout.mjs radial-input.json`。输入绑定新CP、实际geometry/source_topic、实际预算与盘reserve，输出`radial_replay/result.json`。
2. `geometry_20261116_current_C_resolution_original_cuff_atlas.py --computations ... --checkpoint-directory ... --checkpoint-sha256 ... --proof-directory ... --construction ... --construction-sha256 ... --out ...`。写`original_cuff_atlas/r409-original-cuff-plan.json`与`original-cuff-target-atlas.json`；路径名保原producer合同。
3. `geometry_20261116_current_C_ten450_resolution_shared_field.py prepare`，完整CP参数加 `--radial-directory --radial-result-sha256 --plan --plan-sha256 --budget-seconds --free-bytes-reserve --out`，写`shared_field/result.json`。
4. `geometry_20261116_current_C_resolution_live_query_complete_metric.py`，绑定shared/result、CP/proof/cuff-atlas的实际路径/SHA，原6个metric参数、`--continuous-e-result --continuous-e-result-sha256`、全部11个`--c-query-*`参数、`--budget-seconds --out`。
5. `geometry_20261116_current_C_resolution_complete_block_reach_cover.py`，同一shared/CP/proof/cuff-atlas，原12参数、全部3块资源、`--budget-seconds --free-bytes-reserve --out`。

node内存heap只是原真实resource。所有完整active/反射/cut-patch/collar/caps、全phase、全部pair/块frontier、当前single-rank和R282逐叶责任保持。没有只验证端点t，也没有凭3D大盒推出未检点之间的reach。

## 9. 独立 held 与 reflection-inclusive δE

文件15输入schema为 `R441-current-C-resolution450-same-job-held-after-shared-v1-input-v1`。其CLI：

```bash
python -u "$COMP/geometry_20261116_current_C_resolution450_postsolve_held.py" run \
  --input "$HELD_INPUT" --input-sha256 "$HELD_INPUT_SHA"
python -u "$COMP/geometry_20261116_current_C_resolution450_postsolve_held.py" readback \
  --directory "$HELD_OUT" --computations "$COMP" --out "$HELD_NECESSARY_JSON"
```

顶层恰为 `schema`、`postsolve_directory`、`postsolve_procedure_sha256`、`postsolve_input`、`postsolve_input_sha256`、`witness_plan`、`witness_plan_sha256`、`held`、`resources`、`out`。实际procedure/source/input三元只接文件14的明确新身份；旧wrapper不被改标签。

`held` 保原8字段：`active_depth`、`position_max_depth`、`position_radius_goal`（原有理文本）、`interval_bits`、`sqrt_bits`、`max_position_cells`、`max_prefix_points`、`max_tail_witnesses`。`resources`恰为`held_budget_seconds`、`child_shutdown_reserve_seconds`、`free_bytes_reserve`。没有deadline重启字段。

Witness仍用原 `R425-current-accurate-active-quarter-turn-witness-plan-v1` 真实输入；原位置、piece、radial、q/lower和所有来源由实际caller决定。仅依赖同场radial/cuff/shared实际返回，并重新执行完整source/CP/C/firstconstruction/deadline绑定；不依赖metric或reach成功。全像、D、原marker、完整prefix/tail/反射与所有未访scope照原R425。没有材料点位移代替集合held、没有core直径代替完整闭F0直径。

## 10. 同一闭目标与 R443 的责任

原target身份保持并不意味着新core→Phi原词不变。文件14保存第一shared/plan/CP和当前来源，精确冻结W/H/全marker/cuff，同时显式记录第一→当前映射是 $\Theta_{\rm current}^{-1}\circ\Theta_{\rm first}$，公共prefix为 $u=s_{\rm numeric}/L_{\rm numeric}$，radial同物理r，帽为Cartesian恒等加边界粘接共轭。

只有原正密度条件真实成立时才能用R443的可逆图变换。四Loewner的同eta解释依赖相同Jacobian合同变换；它不是本接口计算了psi的区间逆。新consumer在当前真实图中付原target bound，之后才可依R443解释为同一闭target的bound。图变化不影响像集几何，但不能把旧场metric/reach/held数值证书自动转给新场。

帽常数H不进入cap target Gram；仍冻H是完整本次construction策略。准确C的cut实系数/公共图三阶与帽cuff条件继续由真实R416/R413负责，数值ap/app标签不替这些证明。这里没有从有限程序成功推统一C²收敛或无限DN。

## 11. 必要读回、quiet、异常与临时数据

450必要reader CLI：

```bash
python -u "$COMP/root_20261116_current_C_frozen450_resolution_necessary_readout.py" \
  --namespace "$NS" --launch-directory "$OUT" --computations "$COMP" \
  --out "$RESOLUTION_READBACK_DIR" \
  [--entry-stdout "$ENTRY_STDOUT" --entry-stderr "$ENTRY_STDERR"]
```

`--out`是新的sibling目录。原entry日志参数可选；内层sampling/refinement的完整log原件由owner回执绑定后选择必要error，完整大stdout仅身份。输出`resolution_summary`、`resolution_summary_bytes`、`resolution_summary_sha256`到独立实际`GITHUB_OUTPUT`，并保原JSON文件与stdout BEGIN/END。新reader不是科学重算器。

该reader按实际origin选择positive或joint原metadata selector，完整读原sampler result、所有mode/unpaid流及对应原期望SHA；保未启动scope、每个必要原FD层、物理门、native每call范围、真正最后call的必要细项、新CP全部成员身份、全resolution与原scope。成功大矩阵/完整候选管不回传正文。source16只提供原必要函数的新CPschema适配，未导入科学driver进行求值。

五角色必要reader CLI：

```bash
python -u "$COMP/root_20261116_current_C_resolution450_postsolve_necessary.py" \
  --directory "$POSTSOLVE_OUT" --out "$POSTSOLVE_NECESSARY_JSON"
```

它保五stage完整启动/未启序列、原flags/错误/预算；reach保完整必要block frontier、当前singleton/phase事务、union与原unpaid范围。已退栈失败leaf的全部地址仍在原ledger，必要正文保原身份/计数/明确范围；不宣称所有巨大ledger行已由工具逐值回传。成功coeff/panel/commit大表只是完整SHA/行数。

五角色reader输出`postsolve_summary`及bytes/SHA；held输出`postsolve_held_summary`及bytes/SHA。各自均是单份≤90000B必要JSON，不把多份大表拼成新总JSON，也不用分段/编码运输raw。必要字段仍超限就写明确fallback并返回70，原科学状态保持未知/已知的准确范围，不提高上限。

任何reader只在实际owner finally/完整child receipt返回且PID/starttime/自有组静止后读取可变输出。原launcher父可能在runner共享PGID中，只核它自己的PID/starttime；仅真正new-session child检查整自有组。source16/17区分 `actual_parent_resolution` 与launcher的 `parent_resolution`，缺原键不填零；新writer target核的键是 `same_ten_target_identity_verified_by_actual_resolution_writer`。

reader与owner均**不删除raw**。失败、未回收、未必要读回或70时保临时现场。后继实际workflow必须先读这些原scope及原origin读回，再按其既有授权只清自有namespace；本项没有声称已实现一个未来的always清理step或规则workflow。无artifact上传、无Release、无新run。

## 12. 源码依赖与可复现边界

各运行文件自己的完整pin表是执行时的唯一源码白名单，清单表不能替代实际校验。文件2实际载入原193 runtime、根据父来源载入原positive或joint full453数学内核，但只运行新K0完整450；新writer/source/runtimeclosure写真实身份。原factory72c/numeric7ded/augmented a248、profile3bc、bindingc0bd、原fae native/67e3 bridge/946251 QR与全原runtime继续自己的字节。

几何源继续原675准确finite jet、a601四Loewner/闭DFS、R281/R282/R279/R248/R24的已发表纯消费者及完整条件。新源6–12的完整diff主要是source/schema/loader替换，未重复制造数学定理。实际运行所需旧源码和proof必须随未来工作流真实恢复，不以“已发表”免除文件存在/实际SHA。

`first_shared_directory`必须保有真实plan与真实cp；`continuous_e_directory`必须保有实际四文档和live查询所需原流；原采样family也须保原完整C/deepfar输入。根15下这些raw仅同job临时保存；跨run需要按已有来源真正重生，不允许从摘要/SHA补造文件。本项不提供跨runpayload恢复器。

本轮只作文本读写、差异、hash和纸面论证，没有本地import/AST/compile/科学/测试。未来Actions必须执行正常源码语法与真实调用；本项没有把这些未执行步骤列为已通过。不会因为此源码发布等待独立fixture作为科学前门。

## 13. 尚未支付的范围

尚无实际original193/joint203 accepted450被本入口消费，尚无新resolution结果、实际资源成本、误差缩小或全场证书。M维数扩展由独立R442负责；本项不把动态N误说成动态M。stage576深度、finite-far物理点、准确global C选择/无限DN、连续/舍入误差、uniformC²收敛和所有README最终量均不因接口完成而已付。

目前可完成的下一实际动作是：未来原job真正产生接受450且有原时钟余量时，明确给四因子和全部资源/原参数，调用文件13；真实新450后调用14，held15独立；必要读回17/18/15-readback完成后再按调用者的真实清理策略收尾。此处没有为尚未发生的父、参数或budget预填值。

## 14. 冻结字节表

以下表由同目录最终文本原字节生成；每个运行件另附对原来源的完整 unified diff。正文不把差异行数当测试或数学通过。

<!-- R441_FINAL_SOURCE_TABLE -->

| 新运行文件 | bytes | SHA256 | 原来源 SHA256 |
|---|---:|---|---|
| `geometry_20261116_continuous_ten_resolution_checkpoint.py` | 43561 | `bf7dedd2135e3f6b54bc806a17064428111b502b6ddb8572ec66a883b1ce34ad` | `43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae` |
| `geometry_20261116_continuous_ten_frozen450_angular_step_refinement.py` | 43518 | `bf1f8d2dda15584791147f97dc6f313435c16d080acaa49ef418c2df06d503b3` | `70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928` |
| `geometry_20261116_continuous_ten_resolution_saved_prefix.py` | 19180 | `fb6e181cd0ddfb34cc70c874c119ceb149850ce8756d1f2f0dd775175e99cffb` | `1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520` |
| `geometry_20261116_current_C_ten450_resolution_radial_readout.mjs` | 23527 | `3d711d395693cdf8ad222e0838bb29b99ffb5043defb8a66c992dc854df018f4` | `5cc3134ed58aed45efea012219aa2e889624c47b41d5ee9f558da231806ab568` |
| `geometry_20261116_current_C_ten450_resolution_shared_field.py` | 49116 | `1ceda9d32cfcf50e28e737cd0aee981cb8dc2329027aa2967d08532a1ea6e935` | `6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3` |
| `geometry_20261116_current_C_resolution_original_cuff_atlas.py` | 29116 | `d0b03a367f3ece13b06949d5218a992e6ee3e9a41364499070d3f5f475a150a0` | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` |
| `geometry_20261116_current_C_resolution_accurate_cut_patch.py` | 26070 | `8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52` | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` |
| `geometry_20261116_current_C_resolution_fixed_cap_balls.py` | 23665 | `ca53bdc5c0cdd5764065301f0edb1259d083fdffa9f3d767a5a38b4a7cafe364` | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` |
| `geometry_20261116_current_C_resolution_live_query_complete_metric.py` | 55053 | `fd263af28a7d55a7246a49283d367e420786f48f16556dd5a7d61406b1c8459b` | `77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892` |
| `geometry_20261116_current_C_resolution_complete_reach_cover.py` | 60452 | `745b245eddd27c10522012756a33bd842b3883d918845de49cc2cdacbeed1a05` | `3ea1ef9fb56ec10301defa18d832681d6061d8646e78893957ca160279b71834` |
| `geometry_20261116_current_C_resolution_complete_block_reach_cover.py` | 45582 | `f27556bcfbeb72ac3ad7142bbc5089e1168fdc7966fe91757e1a201b7dbfe957` | `e3fcd9eb7ed304cd502c7e03186d65a2d414366c8ad47313c5754aa43ded66ad` |
| `geometry_20261116_current_C_resolution_held_and_rigidity_inputs.py` | 53737 | `144da57a9d55547fa3b85ccb43c0f4261db2e2dcb41e91094c8d3a16c9b7d7b1` | `c87b3a9b9d17f74d8c4f4066f65318e50fed5a56143f620628049a86dcf77ef2` |
| `geometry_20261116_current_C_frozen450_resolution_owned_launch.py` | 47863 | `2247aa97c4ed63c9065d1e326fb78b84500ee7b834f0970905e977773bcea8df` | `4375375b343bc2e3b359a2e1ca566bb6648e08b691d7208cced348f185272868` |
| `geometry_20261116_current_C_resolution450_postsolve_geometry.py` | 57572 | `ae9970eafa70f7138f9fcc31677f0910f092b4076fb1719c8097e3b9d76c0120` | `5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95` |
| `geometry_20261116_current_C_resolution450_postsolve_held.py` | 44141 | `207bf087b1c4dbc852a79ce7b005df805c9b0051af342cd26c47cdf72f4b61fe` | `119ec38cc9351a2d040ce8c7101b933e1e572d19deabb7baf62c4c1cec62eada` |
| `root_20261116_continuous_ten_resolution_phase_readout.py` | 18700 | `448c35c390abd78d169db8bad0c292d89b18cb0109fe5216420b5133479132bf` | `622f4f3c8255a4980e931457f912cca1ee00d25af965da18f39aecc6860c8d72` |
| `root_20261116_current_C_frozen450_resolution_necessary_readout.py` | 28492 | `dcc2900b203a33dcfd2e87e9a99ee74782edbec2bef9eb02fe28f9d1da08322f` | `3949b61a4d7c5d96b5751f33ca1fd20288a176b73a9df97dd087ae828e65428c` |
| `root_20261116_current_C_resolution450_postsolve_necessary.py` | 27225 | `cfb46af0e0c489b604f2956f484cfe789fb2dfe432ac18a9dfaf6d19fae4e63a` | `57413c73db29cb9f65451f631771c07c642edf162dfbe6cdbaa292b5fb451fe5` |
