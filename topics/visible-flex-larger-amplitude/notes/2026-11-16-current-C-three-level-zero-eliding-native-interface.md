# R496 — 三层 current-C 零系数线性作用的完整源接口

作者：OpenAI / ChatGPT amplitude agent（AI）。日期：2026-11-16。

**状态：独立 source-only 组合已完整形成；R496 的科学、资格分布、速度、native 接受、几何及材料结果尚未执行。** 此接口不派发请求，不修改冻结214/216，不把本计划的文件生成等同编译或求解。未来218整体入口另行绑定实际 run/source 和完整原门。

## 1. 可发表文件与临时来源

本次只发表两件小 Python 源、一份普通 literal source plan、R496 证明和本接口。49 个展开 Python/MJS 源不是 Git 预存文件，须在实际 Actions 按计划生成，保到必要消费者/读回/quiet 完成后按原规则清理。临时 publication-files.json 仅供根代理收取，不能误称数学输入。

| 类别 | 相对 topic 路径 | bytes | SHA-256 |
|---|---|---:|---|
| 生成器 | computations/root_20261116_current_C_zero_linear_source_views.py | 11895 | 4d4c507edd571b67655fd2e66fb4bcfa173b1239928443831a81a925c4869ec4 |
| 统计必要读取 | computations/root_20261116_current_C_zero_linear_statistics_readback.py | 5941 | 0b875858a99692d43b3a29387829884abf2ef31856c9ddc1d0ce0307dbb69ef0 |
| 普通源计划 | notes/request218-current-C-zero-linear-source-plan.json | 77274 | e1bef5ad7727107014c9a4c494b22fd066a2866b7f5d97eb8dc1a424b0268360 |
| 条件证明 | results/R496-current-C-three-level-native-zero-elision-source-registration.md | 19163 | 45d5198024b702ceab5180cfb5c42d6926a08d08479f980b18b8bd856fb89303 |

真正新增的算术 caller 已刊于 R494：geometry_20261116_current_C_noj_zero_eliding_variational_engine.mjs，12857 B / eafb41179f08105ac2cbc2708a3db84e1a3ae14eeec67027a94d3d7db70ea3c4。所用 R474 helper 是 geometry_20261116_finite_trace_zero_coefficient_linear.mjs，4832 B / eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02。两者本次不改。

基线为公开216 commit 634c4c85dbdb402965d5dc0bbc1ab756878ce87d；原 request JSON 57819 B / 994c1f2ef39e27e793b977f913f84bee4f4c4406431e23da5dc7dcf716cbdd55。其原公开源及三份生成计划必须各自保留。新49视图使用其中公开原件和旧33生成原件，不能把旧生成文件假列为该 commit 的公共 Git 文件。

环境失效后的本版是明确重建的新版本，替代未完整保全的早稿及75475/fe75恢复草稿。所有当前全文在代理 store；本接口与计划的完整身份才是封口版本，不借旧磁盘 path/hash 声称原文仍可读取。

## 2. 生成器的实际调用与写入顺序

生成器仅接受：

- --computations：真实 GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations；
- --plan：实际普通计划文件；
- --plan-sha256：上表 e1bef5ad… 完整 SHA；
- --out：RUNNER_TEMP 内一个不存在的新专属收据目录。

生成器必须本身位于该 computations，GITHUB_ACTIONS=true，GITHUB_REPOSITORY=Rogerhu12/math-research-public。它不支持把视图写到别处再标旧 computations，也不覆盖旧文件。每次生成要求所有新目标不存在；不能将部分生成后的目录当成全成功，不能用第二次运行隐去首次失败。

计划 schema 是 R496-current-C-zero-linear-three-level-source-view-plan-v1，生成 result schema 是 R496-current-C-zero-linear-three-level-source-generation-v1。计划中 views 每项恰为 role/baseline/output/applications；baseline/output 含完整 file/bytes/sha256。literal_patches 是普通 before/after 字符串字典；每个 application 只引用 patch 和正整数 count。不是 patch 可执行程序、科学数组编码或压缩载荷。

真正调用示意中，R496_COMP、R496_PLAN、R496_OUT 都应由未来原 owned workflow 给出实际路径，不能是本稿预填的科学父件：

```sh
python "$R496_COMP/root_20261116_current_C_zero_linear_source_views.py" \
  --computations "$R496_COMP" \
  --plan "$R496_PLAN" \
  --plan-sha256 e1bef5ad7727107014c9a4c494b22fd066a2866b7f5d97eb8dc1a424b0268360 \
  --out "$R496_OUT"
```

所有49个候选完整文本都在写任何输出前形成、核全部 literal count 及全文 bytes/SHA。随后逐新名 xb 写入、fsync、读回核；受保护 public helper 和原 baseline 均不覆盖。result.json 记录 actual_computations、run/attempt/source_commit、生成器、计划、全部实际原件、全部输出及 current_view。完整成功退出0；受控异常退出1；必要 JSON 超90000 B退出70并保原完整 result、不授权清理。前置校验尚未建 state 时可能只有 stderr，不能虚构 result。

输出帧为 BEGIN_R496_CURRENT_C_ZERO_LINEAR_SOURCE_VIEWS / END_R496_CURRENT_C_ZERO_LINEAR_SOURCE_VIEWS。其 result/scientific_computation_started=false 的含义仅为生成器未执行科学；整个 job 后续可执行真科学。外层仍须先绑定生成器本身与计划，不能以生成器的 source 字段替代这一步。

## 3. 49个实际输出 identity

下表给实际新文件；完整 baseline 字节、所有替换次序/次数和每个 output 已在同一计划逐项列齐。所有相对文件均位于真实 computations；旧原件不改。不得把下表生成输出列入公共 fetch 集合。

| role | 实际新文件 | bytes | SHA-256 |
|---|---|---:|---|
| first_worker | geometry_20261116_current_C_zero_linear_joint_native_worker.mjs | 19445 | 06c56288722cdd4f28bbfef4fb849b25fbd97eb632c4c4043a7c1da9facb58b1 |
| first_client | geometry_20261116_current_C_zero_linear_joint_tail_client.py | 23358 | c0372b5b23b843dbbc932cb15360502af2c4b2e3ee9f7740c902021b057556d7 |
| same_worker | geometry_20261116_current_C_zero_linear_same_far_native_worker.mjs | 19844 | 5c51e556ecb4041e76caa4ebd361e666bcd07160c901abe25e72ab8951a19392 |
| same_client | geometry_20261116_current_C_zero_linear_same_far_tail_client.py | 23438 | 9cf7771497375d2ebbe0f21d6ca059108cf28f01e7d8ee5beb56fe7e9051ec21 |
| union_worker | geometry_20261116_current_C_zero_linear_incremental_M_native_worker.mjs | 19749 | 860b59615813304c95a69016a3021a9120692f08d9ec8acfd71740cd5510e39b |
| union_client | geometry_20261116_current_C_zero_linear_incremental_M_tail_client.py | 23956 | 13c0c9c92c7ad1626141cb9ec97a536dc30865dc52dbe151d4e46dcb36943098 |
| first_legacy | geometry_20261116_current_C_zero_linear_joint_full453_physical_dn.py | 65403 | 04969b25721248d8ac5032d3c980cb081b00476016bc7be1c1efc6439a74810a |
| first_hook | geometry_20261116_actual202_zero_linear_ten_live_full_DN_hooks.py | 10766 | 296baa0986d1b378808ba488936f040f92bf6933a593a24caf1a4734d41a375b |
| candidate | geometry_20261116_actual202_zero_linear_accurate_ten_candidate.py | 32082 | dfa4046eeaa9198470897920552af2ce8fe5882f0b42285049016c14d208bb71 |
| first_driver | geometry_20261116_actual202_zero_linear_ten_full453_frozen450.py | 34862 | 6590636cdd019f9597d4d72f4ccfa86b2dc4e06f8b1e720e352badcd3acb05db |
| first_launcher | geometry_20261116_actual202_zero_linear_ten_full453_frozen450_launch.py | 20665 | 3e9086e61a66a226147f0b977039440e4f4c87152de6ffcf8f4821002a608410 |
| pipeline | geometry_20261116_actual202_zero_linear_ten_pipeline.py | 32055 | 2101d07627245fd53b8190869ffe8a3a7ad5dfff7aa6649023cc3d82a05b7019 |
| first_owner | geometry_20261116_actual202_zero_linear_closed_owned_process.py | 14812 | 419215a322b4ab0763d9e8a7b192225422a3453fec11485cd0f8f28c09c77f96 |
| same_sampler | geometry_20261116_current_C_zero_linear_same_far_resampling.py | 51367 | 5cb69b92c1cdf1d95b613f62d260b5dbbf9f95169d984f78999d3cf17b3d8c2a |
| union_sampler | geometry_20261116_current_C_zero_linear_incremental_M_far_union.py | 53547 | 7d1aaa9504fd8fe2722ab58a5e1cf1b53e152c921848f9030c27144fc10fcf72 |
| same_driver | geometry_20261116_continuous_ten_zero_linear_same_far_refinement.py | 55299 | d70f9077fc7e242a64bf2ce32f90c1529e4912bc16090a604ff417baab87a2a7 |
| union_checkpoint | geometry_20261116_continuous_ten_zero_linear_incremental_M_checkpoint.py | 55959 | 9f5cfe7ff6662846f585983668364e4390024ce219fac239ead10c67e604e295 |
| union_driver | geometry_20261116_continuous_ten_zero_linear_incremental_M_refinement.py | 51992 | 673f38a6b1d0950341210e26300600c1a49968882b12339c615a031c12370f9b |
| same_owner | geometry_20261116_current_C_zero_linear_same_far_owned_launch.py | 57191 | 9105721025e2c92aede14de392fcee9aa92df5d0e77d863e194fa5dedabfda0e |
| union_owner | geometry_20261116_current_C_zero_linear_incremental_M_owned_launch.py | 77205 | f6b48b0b362ab910cecdc534536362cff75a0fd3ffd8253f5ea6691ad49f495b |
| union_phase_reader | root_20261116_continuous_ten_zero_linear_incremental_M_phase_readout.py | 19739 | ddc47ce8c7987a1a642238828ecb677c04e659b6536d8efabea570ca1e7ffb5c |
| first_reader | root_20261116_actual202_zero_linear_two_phase_necessary_readout.py | 31061 | badade0aab176d37151eebbd6492403a6fc4ab9bc2cdbc04b413827d9425cb64 |
| same_reader | root_20261116_current_C_zero_linear_same_far_necessary_readout.py | 37602 | a4cec35339e165f57e1b324ce3a8795f057118161d4d67bed1883561e05a5419 |
| union_reader | root_20261116_current_C_zero_linear_incremental_M_necessary_readout.py | 34447 | 18eac288631a80bc9762f2cce12385c15c7a66405f5ca30e2b6bb720db4fc7b1 |
| first_policy | geometry_20261116_actual202_zero_linear_ten450_closed_parameter_policy.py | 37969 | 1da1e1d0fe462048ab48cfcfb94f48eee47e07c9099507c21bbcba09cc8dcdc0 |
| union_saved | geometry_20261116_continuous_ten_zero_linear_incremental_M_saved_prefix.py | 19282 | f99951807476de57eed78a34ec65c589b71627b61f06bb924f229514747e122e |
| union_prefix | geometry_20261116_continuous_ten_zero_linear_incremental_M_prefix_metric.py | 32834 | 545e00a8f47f653d790566f7d67922203e860c1181d82f10faf80029823ff8b7 |
| union_radial | geometry_20261116_current_C_zero_linear_incremental_M_radial_readout.mjs | 24165 | a4cfda370f9afa20c8efcefa908d421af49d8cf65cd37dd1d03634ec0e65ba62 |
| union_shared | geometry_20261116_current_C_zero_linear_incremental_M_shared_field.py | 49547 | af6db833813f350d2302a43fec5ec36af64850461f3bba3c1c88f39082202714 |
| union_cut | geometry_20261116_current_C_zero_linear_incremental_M_accurate_cut_patch.py | 26167 | 6a56bf1431a864f05d99db204ce406e350f357d4d58f30b6b78442038d42d681 |
| union_atlas | geometry_20261116_current_C_zero_linear_incremental_M_original_cuff_atlas.py | 29488 | 8c21154b3f0fba5914c5bf6e2eab7e0f3ca8eefe1a761d66b08940f58d9f83b4 |
| union_caps | geometry_20261116_current_C_zero_linear_incremental_M_fixed_cap_balls.py | 23692 | e8f30a8490db96c53de03f08f6d2c9ca470a96500d0550096a0b2c0665d7113f |
| union_reach | geometry_20261116_current_C_zero_linear_incremental_M_complete_reach_cover.py | 60534 | e7f8b58f79dafbcf2ae8eca5e90f6eaa936551b02e04bbf0d03a10c976b5035e |
| union_block | geometry_20261116_current_C_zero_linear_incremental_M_complete_block_reach_cover.py | 45645 | 061f9e2f9e359628475b49ba8d45597d9ce9aa717c72db53673400556bc508ed |
| union_held_consumer | geometry_20261116_current_C_zero_linear_incremental_M_held_and_rigidity_inputs.py | 53858 | cddc0a9ffba4726f92a244eb92bac5d8e0f2da045bdaa044f1b9ce140f11a577 |
| union_material | geometry_20261116_current_C_zero_linear_incremental_M_common_material_phase.py | 38801 | 7ba82e6a76f1f46e242290af8d51abb99e9e591aff32d9d8fa90866858ed4ed8 |
| union_metric | geometry_20261116_current_C_zero_linear_incremental_M_coast_live_query_complete_metric.py | 56320 | f705683a78f6db55aaf838b4c4b09f5d5fae6932c99f7be3cc83d1d7a7b7eacb |
| evidence | geometry_20261116_zero_linear_incremental_M_coast_fixed_target_metric_evidence.py | 63233 | c284c4e492390355af0e0a797abe7ca737d9e333ed9a2dafa2b055c8e8dc235c |
| display | geometry_20261116_current_C_zero_linear_incremental_M_multitime_display.py | 41798 | f2d5765804a2cd342625a760837316b393ec27579a58eb10e5feffdd13bea067 |
| first_post | geometry_20261116_actual202_zero_linear_coast_ten450_parameter_block_postsolve.py | 27158 | 41a5793e84472ee6a501eecc4029eff67201f440db3079972e1bdd0d133eb1a1 |
| first_postreader | root_20261116_actual202_zero_linear_coast_ten450_parameter_block_postsolve_necessary.py | 11148 | 284b36a9cca3c49138fbf0d30dd22fe59b56bcb1d4b1472f0fd424d066c28b77 |
| first_held | geometry_20261116_actual202_zero_linear_coast_ten450_parameter_block_postsolve_held.py | 5691 | 0a14386cd8fdac85970cfa0ba278bef86c8220615d476605690827793200518c |
| first_post_entry | geometry_20261116_request218_actual202_zero_linear_coast_closed_postsolve.py | 47367 | 7dcfd4610460ed8ea6da62ca54201cfed24f99d7551431762315ac2a788088d6 |
| same_post | geometry_20261116_current_C_zero_linear_same_far450_coast_postsolve_geometry.py | 65813 | 7dfecc1bdc8cd9a102fbd2341914838e824a8f9d58e3faebb661b87d8c1fc544 |
| same_postreader | root_20261116_current_C_zero_linear_same_far450_coast_postsolve_necessary.py | 27529 | b5bc8d1af3c77cb1f1baef3c1f54aa6b7e3da256a693aa89b56cdca1e5488a28 |
| same_held | geometry_20261116_current_C_zero_linear_same_far450_coast_postsolve_held.py | 44186 | c858b16ee63609e0ac2a4cedd0696b09932fe0997d134dbe608c9d783ba62634 |
| union_post | geometry_20261116_current_C_zero_linear_incremental_M_coast_postsolve_geometry.py | 72168 | 6c30265342a9faebf69f6e474dbda2a02af891e7075e6b91300cc0128c77c31f |
| union_postreader | root_20261116_current_C_zero_linear_incremental_M_coast_postsolve_necessary.py | 27573 | 34c8265c9603e274007aaafe151f4fcb3f4f7deab6ac678b58403dbd52961293 |
| union_held | geometry_20261116_current_C_zero_linear_incremental_M_coast_postsolve_held.py | 44310 | 236b8bd526e2daa346202d92eaa72ceb484421c56fbe46b13e61cedf540d7180 |

## 4. 三层 schema、父件与实际 runtime

| 项 | 实际 schema / family |
|---|---|
| 首 candidate | R496-actual202-new-accurate-ten-zero-linear-candidate-adapter-v1 |
| 首 recipe | R496-explicit-actual202-projected-accurate-ten-zero-linear-full453-to-frozen450-recipe-v1 |
| 首 driver | R496-actual202-projected-accurate-ten-zero-linear-full453-to-frozen450-physical-DN-v1 |
| 首 launcher | R496-actual202-zero-linear-full453-frozen450-owned-process-launch-v1 |
| 首 pipeline | R496-actual202-zero-linear-ten-construction-v1 |
| 新 origin kind | actual202218 |
| same-far owner | R496-current-C-zero-linear-same-far-owned-launch-v1 |
| same-far driver | R496-current-C-zero-linear-same-far-frozen450-original-full-DN-v1 |
| same-far recipe | R496-explicit-current-C-zero-linear-same-far-frozen450-refinement-v1 |
| M owner | R496-current-C-zero-linear-incremental-M-owned-launch-v1 |
| M driver | R496-current-C-zero-linear-incremental-M-original-full-DN-v1 |
| M recipe | R496-explicit-current-C-zero-linear-incremental-M-refinement-v1 |
| M checkpoint | R496-current-continuous-ten-zero-linear-incremental-M-physical-DN-checkpoint-v1 |

首层仍用原43f checkpoint schema；same-far仍用原bf7d schema。它们动态核真实 driver/client/worker 和完整 runtime closure，不能由 schema 相同省来源检查。M有新真正CP文件/schema，并完整绑定新 union/native family。R462 union 的数学 result/config/geometry 格式保持原格式；其新 source_sha256 与实际 view全文另外严格绑定，不将格式兼容宣称源字节未变。

首层、same-far和M worker分别使用 R496-current-C-first112-zero-eliding-live-native-worker-v1、R496-current-C-same-far112-zero-eliding-live-native-worker-v1、R496-current-C-incremental-M-zero-eliding-live-native-worker-v1。全部先按原 source map 加载原完整 runtime，再调用 R494 binder。原 noJ 祖先 f9b 和原 product 205b 的收据保持；actual receipts.noJ 是新 caller 且嵌套原 noJ/helper/product receipt。config.original_runtime_sha256 不是新工厂身份的替代品。

same-far/M owner的 ORIGINS 只注册本新 actual202218 首 origin tuple。留在读取器中的旧 parent 分支仍必须满足同一实际新 origin/deadline及原CP/driver完整来源；这不授权跨旧run借父。未来三层原始计划应按“首真实450→新same-far真实450→新完整M”顺序建立每个 actual_parent_checkpoint，不预填任一级接受。

## 5. 首链四phase与原205内部合同

pipeline 的 phase choices 仍恰为 selection、construction、binding、readback；命令仍为：

pipeline.py PHASE --request ACTUAL_COMPONENT_REQUEST --base ACTUAL_BASE --code-directory ACTUAL_COMP。

REQUEST_SCHEMA 仍为 public-actual202-accurate-ten450-closed-geometry-request-v1；NAMESPACE 仍为 visible-current-C-actual202-ten450-closed-geometry205；deadline仍为 request205-owned-job-science-deadline-v1。这些是新job内明确复用的原205子合同，实际 GITHUB_RUN_ID/SHA必须是新job。不能把原字符串当旧205实际run，不能用改origin标签伪造原文件。

未来218外层需在新job实际生成/绑定独立 derived205 component request：保全部原数学/资源参数，明确更新 candidate/helper/driver/launcher/pipeline/reader/owner及 native_source_additions 的实际 source identity；旧公开pins作为来源保留。不能改冻结205请求正文；不能在 candidate.bind 后静默改已绑定recipe。

构建必要读回仍只在 sampling/config 完成和 binding 返回后、BVP之前执行一次，覆盖真实 selection/prepare、factory和binding全部已生成/错误/未起内容。原帧 BEGIN_REQUEST205_ACTUAL202_TEN_CONSTRUCTION_NECESSARY 是继承的 producer 格式，不是旧run证明。binding phase用原owned独立role，不能复用已写xb的construction收据。

首 launcher CLI保留全部真实路径及摘要：

- --recipe、--recipe-sha256；
- --accepted、--accepted-sha256；
- --complete-seed；
- --factory-directory、--factory-result-sha256；
- --tail-config、--tail-config-sha256、--tail-source-root；
- --candidate-binding、--candidate-binding-sha256；
- --computations、--out、--job-deadline。

candidate binding正文、generated_BVP_recipe和配置必须是同一个实际新source结果，显式 sampling_startup_reserves_original_BVP_seconds在生成前由原参数合同决定。来源改动不把旧finite-Gauss十词变成准确continuous-C接受，也不把factory requested-domain未决新增为BVP前门。

首 driver仍design453→frozen450：同真实现场raw client lease，原fresh H/FD/末J/audit、真实cp和第二阶段fresh完整450输入。原数学函数、阈值、phase顺序均未改变。读取仍消费实际两个phase的original字段，不按returncode单独推接受。

## 6. same-far/M owner的输入与真实输出

两owner都用 --input PATH --input-sha256 SHA。输入schema为各owner schema加-input-v1。以下共同路径必须实际存在/生成于同namespace：

namespace、origin_launch_directory、parent_launch_directory、job_deadline、job_deadline_sha256、computations、accepted、accepted_sha256、tail_config、tail_config_sha256、tail_source_root、out。max_nodes必须显式。out须新而专属，computations须真实HERE。

same-far资源字段恰为 sampling_process_budget_seconds、refinement_process_budget_seconds、child_shutdown_reserve_seconds、minimum_free_bytes_at_start、free_bytes_resource_stop；M另外必有deep_process_budget_seconds。这些是原钟内cap，不相加重开科学钟。原 free-space stop 必须小于 startup reserve。

same-far refinement_factors保原五个正整数且至少一个>1；M保原四个正整数及field_modes>112，并要求实际新M大于实际父。不能在M参数中多塞steps字段：实际native步数从真实parent.actual_resolution乘原明确factor继承。原输入的全部sampling work参数和deep精度/来源字段仍必填，R496不替未来request选择新数值。

same-far sampling保 cover/far目录与resultSHA、proof/unit_row_proof、original_sampling_directory/resultSHA及原parameters。M sampling明确分 original_far_directory/resultSHA 和新的deep输出；deep保持原config、ledger_ready、proof、tail_proof、mode_extension_proof等完整原来源。所有SHA是实际文件receipt，不是仅标签。

owner读取 origin.result.json，再按 origin.actual_job_deadline 的原file/bytes/SHA核输入deadline；绝对截止仍由该文件namespace创建时间加原science_seconds_from_namespace得到。accepted parent不同于原112 far输入；M保原112 config、原far全部行和μ，但新M deep/J/native/fullDN仍真算。原modes兼容键若存在必须实际新M，spacing沿原明确兼容合同，其余policy逐字段保留。

关键结果保持实际out/result.json和adapter/CP原路径，字段包括 origin_launch、actual_job_deadline、actual_parent_checkpoint、actual_parent_checkpoint_directory、actual_resolution、actual_adapter_status、actual_refined_checkpoint、actual_refined_checkpoint_directory、owned_group_quiescent_before_readback、resource_stop、error。same-far真正接受字段是 current_refined450_accepted；M为 current_refined_M_accepted。字段缺失/false/未起依实际保留，不造新父。

新same-far driver修正真实legacy/hook选择：新04969 legacy→新296baa hook；原c71d→原62010 joint hook；原ff667→原bedb positive hook。此源事实不被用来归因未到该位置的214/216实际结果。原FD仍先行，未移动或删门。

## 7. 每级几何、held与材料/显示family

五stage顺序保持 radial_replay、original_cuff_atlas、shared_field、metric、reach；各stage原参数/单独预算/同绝对clock/own child生命周期不变。新source只是实际来源登记，R483 coast数学正文未改。完整reach/held独立于metric接受，不增科学前门。

首post source/schema见表和计划，input schema在其schema后加-input-v1，CLI --input/--input-sha256。新首入口helper为 geometry_20261116_request218_actual202_zero_linear_coast_closed_postsolve.py；它绑定实际新首owner/launcher/driver/policy/readers，保原子合同生成/必要清理状态。其独立外层schema为 request218-actual202-zero-linear-coast-closed-postsolve-v1，完成marker为 request218-zero-linear-coast-closed-postsolve-readback-complete-v1；原science/pipeline内部205名称有上节明确责任。

后两层post输入schema分别为：

- R496-current-C-zero-linear-same-far-resolution450-coast-block-geometry-v1-input-v1；
- R496-current-C-zero-linear-incremental-M-coast-block-geometry-v1-input-v1。

实际upstream_kind分别是 R496-zero-linear-same-far-resolution450 和 R496-zero-linear-incremental-M。post需first_shared_directory/resultSHA、upstream_launch_directory、job_deadline/SHA、geometry_directory、continuous_e_directory/resultSHA、computations、proof_directory、source_topic、out及namespace；必须来自真实新CP和实际首shared，不能从摘要恢复已删raw。

construction恰为cut_correction_width/cap_height/fixed_cap，后者完整markers名单。后级必须逐IEEE词复用首次actual construction，不能按新radial重选H。resources给全部五stage预算、free reserve、node heap和shutdown reserve；metric/reach/c_queries所有原键仍明确填写，c_queries仍11项。新方程/接受门未加入这些参数。

post的原C四metadata与两source-panel/index数据必须保到最后metric/provider结束。原原始far账本还须满足same/union后继的实际消费责任，不能以几何使用了四小JSON为由删去其他后继所需数据。

| 用途 | 首112 family | same-far112 family | 新union M family |
|---|---|---|---|
| R496 evidence FAMILIES | original112 | resolution112 | incrementalM |
| R496 display FAMILIES | current112 | resolution112 | incrementalM |
| common material current family | R416-original-resolution | R441-current-resolution | R496-zero-linear-incremental-M |

new material source同时登记 original-R437 和 actual202-R496 的实际首记录，后者严格绑定本新policy文件/SHA/schema。当前M使用真实新cut/saved/shared modules，不冒旧类身份。A与B分别按真实firstprocedure、shared、CP、target、十词、deadline和fullconstruction绑定。B不存在明确材料测量未付，不挡原native或独立held。

evidence CLI是measure/compare --input --input-sha256；readback --directory --result-sha256 --out。其schema为R496-fixed-target-zero-linear-incremental-M-coast-Bernstein-metric-evidence-v1，measure/compare各原schema后缀不变。common material的准确API evaluate_active_cell/encode_active_cell及完整逆/六jet原文不改。

display CLI --input --input-sha256；schema为R496-current-accurate-zero-linear-incremental-M-multitime-display-v1，input后缀-input。每个压缩/未压缩显示文件仍严格<5MB，真实未访/中断保留，多个t是显示样本。physical-angle-image不冒固定首q顶点对应。入口ORIGINS已同时核新首launcher schema/SHA及原205deadline；不能只改其中一个。

各reader/held保持原CLI。same/M held分别run --input --input-sha256及readback --directory --computations --out。frames是明确当前R496前缀；若某个 inherited event或inner mathematical schema仍含R452/R456/R464/R487，是源内格式/事件来源，不代表实际旧run。外层必须按完整实际schema/source/run消费，不只按帧字符串。

## 8. 统计流与原必要读回的确切范围

worker实际文件为 CLIENT_DIRECTORY/native/actual-zero-eliding-linear-statistics.jsonl。每条含location、actual_call、worker_source及完整statistics；locations是runtime-bound-before-owner、ready、native-progress、native-response、native-failure、session-returned，保持实际发生顺序。三worker全文SHA分别在上表，不接受仅名字吻合。

metadata-only helper没有CLI主执行；各新necessary reader在原owner静止之后调用read_actual_native_statistics(client_directory, expected_worker)，expected_worker恰给file/bytes/sha256。它读全部流且前后核完整identity；空/缺文件分别处理，缺文件不补0。残缺末行/重复成员/来源不符如实报错，不悄悄丢弃。

返回每个原nine counters及fallback_reason_counts、last_observation、engine started/constructed、scope原值。正文完整返回最后一条原record，首条只identity/地址，全流给数量/locations/真实call地址计数和SHA。它不聚合科学数据、不重算J、不推最后记录之后的进展，也不声称root逐值读了全部中间记录。

首reader把actual_zero_eliding_linear放入actual_shared_native；same/M reader放入其必要native对象。此字段在native未起时仍明确exists=false。M phase reader本身只修真实driver/CP绑定；外围Mnecessary承担统计流读取，不能将phase读者不存在这个字段误称未接。

原FD逐方向、错误、partial、真实native/final flags选择保留；新元数据同单份90000B限制，超限仍真实处理。原200/182等选择的缩短字符串或大树identity不自动扩大为全文原错误读取。本接口不保证未来每份输出低于90KB，更不将旧未返正文用作容量fixture。

## 9. 原门、生命周期与当前资源风险

新局部helper只在实际A与被用T有限时省零项；不合格原完整循环，保原root/RHS/J和所有native/fullDN门。原FD、全残差、当前H、finalJ/audit须仍实际支付；全338解析J不是新增前门。coast/accurate C域责任与native数字接受仍分清。

原18900秒science与2700秒规则/读回/关闭合同保持，所有上限由同原deadline裁剪。新generator/worker/logger/reader会有资源开销，未承诺速度；source准备不能重启BVP钟。原PID/PGID/session/startticks、quiet、未知组保raw和条件cleanup不变。

actual212的唯一读回负责人已报告：depth2采样完整，但首BVP启动自由空间11761553408 B低于原34359738368 B；far-accepted-panels约95028212980 B。R496没有解决这项存储问题，不降低32 GiB门，不把exit124冒timeout或数学拒，也不先删R456/R462后继还读的完整账本。未来218应引用R478正式结论及其实际scope；若另接独立已证明的账本生命周期修正，应给新真实来源，不静默混入本49视图。

raw cleanup只能在原科学停止、必要范围已读且owned子树静止后由原outer规则决定。source generator不删科学raw，统计helper不授权清理；新post的未完成也不能被completed flag掩盖。原源/输入/参数/预算/门与未来额外资源层须各自明示。

## 10. 未来218入口的待交接范围

本五件可先独立登记。未来218须另给完整request/workflow/owned runner/necessary composition，不得仅拿本计划名派发：

1. 保全部冻结216公开pin和旧三套生成合同；按原真实顺序生成旧33，再生成新49。
2. 分开public、historical generated、current generated集合，按文件实际并集计数，不把旧生成33或新49写成公共Git文件。
3. 在同一实际computations更新原205子合同的明确source fields和new native additions；数学、参数、reserve及原clock不静默更改。
4. 首新450后接真same-far，再真union M；每层自己fresh全门、五geometry/held、evidence/display消费真实新family。任一级未起/失败不填未来父。
5. 原七必要读回与新增source/statistics/层级必要读回维持90KB/70/quiet合同；当前raw何时可退须沿最后真实消费者，不由本静态证明放行。
6. 所有执行和科学算术仅公开Actions。本文形成过程只读取源文本、普通JSON及字节身份，没有本地科学、import、AST、compile、fixture或benchmark。

完整替换正文已经在77274B普通计划；不再把49展开源复制入Git。此接口不预填218 run、不声称改善运行速度或已达到题目的全域/全t/闭面完成标准。
