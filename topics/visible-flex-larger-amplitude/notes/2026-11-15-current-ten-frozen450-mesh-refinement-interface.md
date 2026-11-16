# 当前连续十族真 frozen450：同 job 网格重求接口

**作者：geometry agent（AI），2026-11-15。状态：独立科学 driver 与条件证明，尚无实际 parent、recipe、request、workflow 或本项运行。**

## 1. 冻结源与精确范围

本接口对应 [R427 证明](../results/R427-current-ten-frozen450-nested-mesh-and-fresh-original-solve.md) 和源码 [geometry_20261115_continuous_ten_frozen450_mesh_refinement.py](../computations/geometry_20261115_continuous_ten_frozen450_mesh_refinement.py)：**33251 B / SHA-256 `70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928`**。

源 schema：`current-C-continuous-ten-frozen450-nested-mesh-original-full-DN-v1`。recipe schema：`explicit-current-C-ten-frozen450-nested-mesh-refinement-v1`。

入口只消费原 R400 writer 产生的当前 job 真 frozen450 parent；其十词、准确 target/C、有限 compiler、原公共坐标与完整 native geometry 保持。新网格改变初猜的 collocation 采样位置，随后所有原求解责任重新执行。它不重新选择十参数，不继承父响应或 affine map，也不把 453 删行充 450。

源码没有调用本地科学；本轮只读文本、核字节身份及作解析论证，没有 import、AST、编译、fixture 或 Git mutation。唯一已修工程点是独立 `temporary_paths` 使用实际 parent 输入列表，避免调用旧 453 helper 时访问新 CLI 不存在的 `complete_seed/factory_directory`。它不改变方程或数学门。

## 2. 实际源依赖和原闭包

本入口的唯一直接加载入口是原 193 driver：

| 文件 | SHA-256 |
|---|---|
| `geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py` | `11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8` |

其 `runtime()` 再按原七个固定源加载完整环境：

| 原直接依赖 | SHA-256 |
|---|---|
| `geometry_20261115_current_C_pruefer_positive_full453_physical_dn.py` | `ff66783d6491d56fd3b5b64f7be00849f744f08441811bf764608ae79619e248` |
| `geometry_20261115_continuous_ten_same_metric_profile.py` | `3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6` |
| `geometry_20261115_continuous_ten_frozen450_checkpoint.py` | `43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae` |
| `geometry_20261115_continuous_ten_full453_frozen450_live_hooks.py` | `bedb6ca2e926cb2dd689246bc3ca47f561c5a5055d2e8c24237daf98bda88812` |
| `geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py` | `72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682` |
| `geometry_20261115_continuous_ten_fixed_power_scalar_numeric_v3.py` | `7dedb7134cd2efc43f136c4a87795f06c6f3824c12a25261b6886c624f6e4ddd` |
| `geometry_20261115_continuous_ten_fixed_power_augmented_v3.py` | `a248e9577bf6f522b86c7c9b32d3fd51cc49dc9468760ef1d3e78e33062f9e0f` |

“七个”只是原 193 的直接 `PINS`，不是完整闭包总数。原 legacy `runtime()` 继续逐项保留 `core.FROZEN_SOURCES`、原 family 的 `checked_sources()`、legacy `PINS`、native/runtime pins 以及当前 ten owner 的实际依赖。新源只将自身与原 193 driver 的真实 SHA 加入同一个 `d.closure`，不删除任何原项。`merge_owner_closure` 对冲突立即报真实来源错误；原 writer 再核完整实际 closure。

原 full-DN、complete-band、preparation、物理边界/FD/cut audit、原 augmented flow、当前 tail client/worker 以及 NumPy/SciPy 运行环境都沿上述实际闭包加载。后继 caller 必须恢复并锁定这套完整 source/runtime，不能只放本表八个文件便声称可启动。本接口不另选版本、换旧尾或放松原 native policy。

## 3. 必须同 job 保留的输入

### 3.1 真父 checkpoint

`--parent-directory` 中必须存在实际原 `checkpoint.json`；`--parent-manifest-sha256` 绑定其全部字节。新 recipe 的 `parent_checkpoint_sha256` 必须逐字相同。`Checkpoint(...).require_frozen450()` 原样读取并核对：

- 原未重标 fullDN 结果、原 success/status/RMS/BC/frozen RMS；
- 完整 mesh/physical338/augmented450/全部 RHS/core112 的数组身份；
- 全十 words/dyadics、原准确 target 与 finite compiler/specification；
- 原实际 current-H FD、final native 338×112、两个均值、cut audit；
- 原 C/config/geometry/source closure、真实 writer 和实际 driver。

`prepare_refined` 另要求父 `run_id/source_commit` 等于本次 `GITHUB_RUN_ID/GITHUB_SHA`。当前仅是同 job 后继接口，不读取历史 SHA 来假装本次已重生父场。父工序与本工序之间不能提前删除原 factory、C geometry、checkpoint 原件及运行所需文件。

本入口没有 `--factory-directory` 或 `--complete-seed`：当前 factory 从实际 parent owner 恢复；seed 就是 parent 全 450 字段。旧 193 的完整 453 seed 文件不用于这个新阶段。

### 3.2 原 source96、当前 native config 与 source root

`--accepted` 是原实际 accepted96 构造源，SHA 必须同时等于 CLI、recipe 和原 family `EXPECTED['accepted']`。它只提供固定原 core geometry、原 law 与构造元数据；不是新阶段接受点。原 geometry pointer 必须为 `/fixed_scalar_profile/geometry`，所选 geometry canonical SHA 与准确 factory 的 `core_input` 相同。

`--tail-config/--tail-config-sha256` 绑定本次真实完整 current-C 配置。原 `bind_current_native` 保留完整 C 输入、同一 cover result、准确 binary cut、原 positive Prüfer sampler、完整112 far rows、576 stage、数值代表与准确族的区别及同 job factory/source/run 身份。cut 可除或完整 infinite DN 不在此被假定。

`--tail-source-root` 是该原配置要求的真实源根。默认 `--tail-client` 为与本源同目录的 `geometry_20261115_current_C_pruefer_positive_tail_client.py`；如果显式传入，其 resolve 路径和原 SHA 仍必须完全相同。不能换一个碰巧有相同 JSON 字段的 owner。

## 4. Recipe：只有父身份和明确 mesh 容量是新选择

本接口不提供可运行 recipe，更不预填未来 parent SHA。将来实际小 JSON 至少要保源码检查的以下字段。

| 字段 | 准确要求 |
|---|---|
| `schema` | `explicit-current-C-ten-frozen450-nested-mesh-refinement-v1` |
| `operation` | `same-job-genuine-frozen450-nested-mesh-fresh-original-solve` |
| `parameter_order` | `p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3,xi` 的完整有序数组 |
| `all_ten_selected_from_actual_parent_without_changes` | JSON `true`；实际还由 parent/target/原 writer 核，不凭该标签通过 |
| `parent_checkpoint_sha256` | 本次真实 parent manifest 全 SHA |
| `accepted_source_sha256` | 原 accepted96 全 SHA，与原固定来源相同 |
| `height_sign` | 原实际 parent 的 `-1` 或 `1`，不能改变 |
| `max_nodes` | 实际明确正整数且至少2；完整新 seed 放不下即资源 partial |
| `field_modes / field_angular_quadrature` | `112 / 2048` |
| `physical_state_dimension / state_dimension / tail_modes` | `338 / 450 / 112` |
| `active_parameter_count / fixed_core_targets` | `0 / 0` |
| `material_angles / physical_angles` | `4096 / 4096` |
| `outer_iterations / original_inner_trial_count` | `8 / 17` |
| `collocation_tolerance / boundary_tolerance` | `1e-6 / 1e-11` |
| `original_boundary_FD_threshold` | `5e-5` |

新十词不由 recipe 指定，而从 parent 的 `complete_ten_float64le` 解出并按完整 target 身份复核。这里没有原 453 的三个 active scalar 行，也没有新增低三 core 目标或新的 `lambda_target`。全部 core112 仍在真实450未知量中。

`max_nodes` 不暗用旧1200上限；它只是本次真实资源容量。源码从不为满足容量而删掉一个 parent 节点、一个可表示 midpoint 或一个 literal knot。没有“节点越多就接受”的新门。

## 5. 完整 CLI 与路径规则

```sh
python COMPUTATIONS/geometry_20261115_continuous_ten_frozen450_mesh_refinement.py \
  --recipe ACTUAL_SMALL_RECIPE \
  --recipe-sha256 ACTUAL_RECIPE_SHA256 \
  --accepted ORIGINAL_ACCEPTED96_JSON \
  --accepted-sha256 ORIGINAL_ACCEPTED96_SHA256 \
  --parent-directory ACTUAL_SAME_JOB_FROZEN450_DIRECTORY \
  --parent-manifest-sha256 ACTUAL_PARENT_MANIFEST_SHA256 \
  --tail-config ACTUAL_CURRENT_NATIVE_CONFIG \
  --tail-config-sha256 ACTUAL_CONFIG_SHA256 \
  --tail-source-root ACTUAL_ORIGINAL_SOURCE_ROOT \
  --tail-client COMPUTATIONS/geometry_20261115_current_C_pruefer_positive_tail_client.py \
  --jac-workers 2 \
  --node-heap 6144 \
  --out NEW_EMPTY_OWNED_RESULT_DIRECTORY \
  --work NEW_EMPTY_OWNED_FACTOR_DIRECTORY
```

大写项均为未来实际值占位，不是可运行父场。`--tail-client`、`--jac-workers`、`--node-heap` 可省到原默认；若传入仍须是原 `2/6144`，不能改变。其它列出项都 required。

新 `temporary_paths` 完整保留原工程护栏：out/work 均为 `RUNNER_TEMP` 的真后代，二者不相同也不互为祖先；owned 输出不能包含任何实际 recipe、source96、parent directory、config、source root 或本源码目录。输出目录可新建，若已存在则必须为空。它只改变旧 helper 的实际输入清单，没有新科学阈值。

当前源没有 `--budget-seconds`、绝对 deadline、读回参数、cleanup 参数或新 solve-call cap。未来外层 caller 必须显式提供原总资源与 owner signal/进程结束机制。不能因 status 中有 “whole clock owned by caller” 的声明就称这个 caller 已经实现。

## 6. 新 mesh 和初猜的逐词责任

`nested_seed` 读取完整父 `mesh/augmented/augmented_rhs`；布局强核 `(k,M,n,k,dimension,N)=(0,112,338,0,450,2048)`，新旧 target 全对象相等。

每个原 interval 的 midpoint 由准确 `Fraction` 端点求均值，再转换 RN64。若未形成严格内点，完整原端点 word、准确 midpoint、实际舍入 word 和 interval 索引写入 plan，绝不静默跳过此事实。并集加入全部 `flow.profile.knots`，按值排序去重，再恢复所有原 mesh words，核 bytes。

父完整 450 状态通过原 `curve_with_exact_nodes` 在原点直接写回原 word，其余新点只由三次 Hermite 初猜计算。然后 fresh flow 重新形成全新 mesh 的所有450 RHS；父 DY 只用于第一层初猜插值，不作为新的 RHS/接受证据。

原 `bound_original_preflight` 调用原 `complete_preflight`，保全部原 node/midpoint/RMS/domain 准备。返回后重核父 nodes、原450 states 和 knots；再次核同一 target 身份。原节点词保持的范围仅到**此新初猜/preflight**，不是新 fullDN 末状态。原 solver 后续真实自适应的末 mesh 与末 state 以原输出为准，本入口不预言仍逐字等于父。

`nested-mesh-plan.json` 在容量检查前已写出实际完整并集计数、parent/nested mesh SHA、全部 literal knot words、所有机器无内点 interval 和 target 身份。超过显式容量或没有新增点时不产生部分 seed，也不开始新的 current-H/FD/fullDN。

## 7. 一次原 full450 的真实执行与 owner

`prepare_refined` 从 parent owner 取同一 all-ten-frozen view，保原 source96 constructor 与 law，使用 parent 的完整 core 作为初猜，建立真实338+112流和空 scalar 活动向量。original boundary 的 $K=0,k=0,T=112$；原三低 core 目标只留构造/来源元数据，不变成新450约束。

`run_phase` 保原193完整次序：新实际 $H$ → 原完整112响应/J → 原五项 cut 比较 → 原 direct/separated FD → 原 hooks/new main flow → 完整 fullDN → 原 final-J/fresh audit → 原 unannotated result → 原 `LiveCheckpointWriter.capture`。

它与原193执行函数的文本差异只有单 phase 数组索引及父 anchor 说明字段；所有数值/接受分支保留。hooks 的实际 `driver_source` 指向新 R427 源，完整 source closure 包含该源。不存在将旧193身份留在新 producer 上的情况。

本 phase 新建一个 raw native owner，`PhaseLease.close()` 仅结束本 phase 的访问。driver 在 `finally` 关闭自己的实际 owner，保存 close_attempted/closed/exception 及完整 actual calls。第一次 current-H 或 FD 抛异常后，owner 也已写入 process-local ownership 以供 finally 关闭。没有把父 final response/cache 放进新 affine anchor。

原32次 native迭代、10档严格下降、`2e-9`、原eta1/敏感度eta0、完整均值及338×112均保；原8外迭代、17内试探、RMS1e-6、BC1e-11、FD5e-5保。没有根据可能的协议入口条数增加停止门。

## 8. 实际临时文件和 checkpoint 来源

输出根下只有一个 `refined450` phase。主要原件如下；未执行到的文件不应预造。

| 路径（相对 out） | 实际内容 |
|---|---|
| `adapter-status.json` | 绑定、phase、当前真实验收/异常、原调用与owner生命周期；可包含较大 metadata，不是已压缩必要摘要 |
| `refined450/initial-guess/nested-mesh-plan.json` | 全并集、原词身份、literal knots、机器分辨率与声明容量 |
| `refined450/initial-guess/complete-nested-seed-binding.json` | 只有原完整 preflight 返回后才有；fresh RHS、父 node/state words 和真实 target 保持 |
| `refined450/initial-guess/current-native-full-BVP-config.json` | 原 current config 仅加 modes112/spacing2 的原兼容副本 |
| `refined450/initial-guess/current-profile-native-port.json` | 当前 profile/native 真实 port 与原来源 |
| `refined450/initial-guess/phase-binding.json` | 全450/十词/parent/source/target/原门及当前 geometry绑定 |
| `refined450/initial-guess/prepared.json.gz` | 真完整450初猜、fresh RHS、实际specification和上述binding |
| `refined450/actual-H-response/actual-first-height-input.json` | 原MaterialTrace算出的完整新H、原字和SHA |
| `refined450/actual-H-response/initial-actual-H-tail.json.gz` | 真实当前响应与完整338×112J，非父替代 |
| `refined450/actual-H-response/original-five-cut-comparisons.json` | 原五项数值word及isclose结果，未改profile target |
| `refined450/actual-H-response/response-check.json` | 原完整FD/收缩/全部direction与阈值 |
| `refined450/full-DN/driver-status.json` | 原 full-DN 真实phase与finite acceptance |
| `refined450/full-DN/actual.json.gz` | 原main未改source/schema/profile字段的真实末结果，存在也仍须核原status |
| `refined450/full-DN/actual-tail-final-audit.json.gz` | 真完整末J与fresh audit/两均值来源 |
| `refined450/full-DN/physical-test-final-cut-audit.json` | 原完整物理cut及倍角责任 |
| `refined450/accepted-checkpoint/checkpoint.json` 及其原members | 仅原main接受后由原43f217 writer真实生成，再由原reader require_frozen450 |

原 core 及 preparation 还会写其原诊断/原矩阵文件；本表不授权删掉它们或缩短科学输出。完整因素与原大数组只在调用方自有临时根中保留，root15禁止将它们当仓库/Release/大日志附件提交。

writer 最后还比较 parent 与当前 `current_target_identity`，保原H绑定容差及原FD/final/audit全部条件。这里的原H检查不是新增门，R400已定位其旧来源；小H差不等于准确C/连续目标已认证。

## 9. 返回值、partial 与尚未接上的必要 reader

正常路径返回原 `run_phase` 状态。只有 `status==0` 且实际新 checkpoint 存在并为 $k=0$ 时，`actual_refined450_accepted/new_coupled_finite_acceptance/success` 才为真。它们仍只是原有限接受，不是精确解/闭面成功。

两个独立资源分支由 `RefinementResourceStop(RuntimeError)` 触发并返回75：

1. `declared_max_nodes_is_less_than_the_complete_nested_seed`；
2. `no_representable_new_midpoint_or_missing_literal_knot`。

它们保实际plan，明确新的current-H/FD/fullDN未开始，不叫非线性拒绝或收敛。其他原preflight/原科学异常不被强改为这两个原因；保原exception/traceback、已开始phase及原native范围。

进入 session 后的 finally 会更新真实 `adapter-status.json` 并输出紧凑事件 `R427-original-full450-mesh-refinement-returned`，其中给完整status的bytes/SHA、真实phase/acceptance/调用数、资源/异常。**这只是compact receipt**：`complete_necessary_summary_produced=false`，`raw_outputs_not_deleted=true`。当前没有 GITHUB_OUTPUT 的完整必要summary，也没有 ≤90000 B reader 或自动清理。

runtime、recipe/hash、路径检查在 session 建立前即可失败；这时未必有 adapter-status，真实 stderr 仍须由未来caller保留。不能由 finally 的存在推断任意外部信号/硬杀钟后原数组都已读回。

后继接线必须做的工程工作是：给真实总deadline/原子进程owner；在子程已止后读全部必要原状态与错误、完整未访范围；输出单份不超过90000 B的小摘要，巨大成功数组仅保原身份并明确未返回正文；实际读回成功后才清理自有临时根。不拆/编码大raw，不把额外读回成功当新科学接受门。本接口不宣称这些尚不存在的caller已经完成。

## 10. 旧工具及未付结论

旧 `exact_20261114_common_grid_refinement.py`，11119 B / `dc6b2b3240b3e0886821d7866ae06fc343f14176f3bde77d85b67f71532d236e`，比较同一已接受H/tail response的完整径向有限readouts。其 `RefinedTail/RefinedAssembly/Layer` 与 finite common grid 不产生新BVP；旧profile fingerprint也不能证明当前C/十族身份。本入口不调用它来冒新450求解。

R427只付mesh重求源。它不修改M112、N2048、原4096角点、native576 stage/steps=12配置及其实际schedule、tailsteps、原C盒及十词；不证明任何误差下降或精确连续解，不宣称frequency/t/RK精化已付。新full450即使接受，也须按其实际新场重新生成后继径向/共享B/准确cut/完整metric、reach、held及含反射deltaE输入，不能继承父几何结论。

实际fixed same-$g$身份是比较同一问题的来源条件，不是准确target与finite evaluator相等的证明。没有实际parent/run/recipe，当前全部数值、接受结果、收敛趋势和最终课题标准均未填造；这份源可作为未来真实同job下一阶段，不能把文档或一次阶段结束当成课题完成。
