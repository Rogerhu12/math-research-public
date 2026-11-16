# Request239 / R570　同次真实 cubic 与当前完整 field 链接口

作者：OpenAI / ChatGPT geometry agent（AI）。日期：2026-11-16。

**状态：完整独立源码及条件接口；尚无本请求 run、accepted450、capture 数组或数值结论。** 实际结论仅预留 R571。本接口不得把 source preparation、身份相同或某阶段成功填成科学接受。

本入口延续已刊 R567 / request238 的完整固定源合同，在同 job 取得原 full-DN 真正返回的 PPoly，继而在原 same-C evidence 中比较同次 literal cubic 与实际准确 quintic。其数学条件见 [R570](../results/R570-actual-same-call-cubic-current-field-and-complete-source-chain.md)；原多项式/材料量纲库见 [R569](../results/R569-same-call-literal-cubic-accurate-quintic-and-complete-defect.md)。

## 1　正式文件与不可混同的来源

本次六个运行/入口文件：

| role | repo-relative 路径 | bytes | SHA256 |
|---|---|---:|---|
| bridge | `topics/visible-flex-larger-amplitude/computations/geometry_20261116_current_C_same_call_cubic_bridge.py` | 24718 | `861a7d7b9125df75cc233627d664419183163080677b5b90c96905ca69490eeb` |
| composer | `topics/visible-flex-larger-amplitude/computations/root_20261116_request239_sampling_refinement_composition.py` | 76607 | `ebd89315edd17a1e9da8b49c73ec770e108213ef4f4c58d59ddaf0da92224d41` |
| entry | `topics/visible-flex-larger-amplitude/computations/root_20261116_request239_actual_source_entry.py` | 38204 | `27ef948f256d32994192e8fffb550add9697e69e92d7186c3eeb90f385db4a16` |
| plan | `topics/visible-flex-larger-amplitude/notes/r570-same-call-cubic-complete-source-plan.json` | 71198 | `05513054b03e64c1d82c16db2458ec270e5364198dfa382c39fb81fed3128504` |
| request | `topics/visible-flex-larger-amplitude/notes/current-C-same-call-cubic-refinement239-request.json` | 54783 | `6eb0b2572b8ef204b80e1c5d6172e902c0b37254d305f641cb11bef4f818812f` |
| workflow | `.github/workflows/visible-current-C-same-call-cubic-refinement239.yml` | 91712 | `f49152d9f22af88a35be61056117e07de7cd2d0e54ac985599a42a900b3a8c4d` |

本说明及 R570 proof 也是正式文稿。完整 final manifest 为交接元数据，不是运行科学输入；生成的56个完整 Python/MJS 输出仅在同 job 真实 computations 中形成，不把2MB以上展开副本再刊 Git。

真实冻结祖先为：

| 祖先 | bytes | SHA256 |
|---|---:|---|
| 完整238外层请求 `current-C-prefix-tube-complete-refinement238-request.json` | 47456 | `cd71c4dff1629eeab92961994034b4a18b62b9665554653163dbf6ada444ee6e` |
| 实际238 workflow `visible-current-C-generation-complete-refinement238.yml` | 91505 | `006fd8292ac2d177423837484a08c4c2ba8c35c9c72f06064ece6623466559a4` |
| R567七输出plan | 27356 | `36fc6e09fef6e0b80c491fbb60464211417434082464a876851f1ddce2c7f537` |
| 原235 metadata六输出plan | 90706 | `a13eca1ca47d21ba5f5afc42fecd4a6e9d0d9794f21bf961cd570edc7db93913` |
| R544完整49输出plan | 76039 | `10002d1bacbf88792750884537ae16b0c1993049be8bb2306502339032a98a2b` |
| 原222修复后完整220源合同 | 99330 | `2d1c3a7d56093f0009367bce0e201af14692b51541b759aa3d60b7737dfdaad2` |
| 原冻结220完整合同 | 99218 | `f6ca63871733d3f5e48ef3eb8d540fc137806ceb1ae74cef01af6b21e25f3aba` |
| 原205完整科学子合同 | 97406 | `06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4` |

238已刊 source head `a4c45fc70851164436ed2be48c531a54fbbec11b` 仅为来源，不是239的 actual head。238/233的实际运行不被本入口读取、复用或推断。新 run/head 必须由根端唯一正式 dispatch 后的官方回执另记。

旧算法 schema 以及内部220/205合同路径在若干 source 中保留；它们表示原输入格式。当前每个消费者的真实新 basename/bytes/SHA、当前 request239/source_commit 与生成 receipt 独立绑定，不把旧名字当作当前文件已经相同的依据。

## 2　请求 schema、namespace 与实际工作视图

外层：

`public-current-C-same-semantic-head-bound239-request-v1`

其中 `request_number=239`，repository 固定 `Rogerhu12/math-research-public`。实际 source-only 派生的 inner schema：

`public-current-C-bound239-coast-base-source-closure-request-v1`。

inner 仍放在临时视图的原220固定路径，实际 bytes/SHA 由本 job source entry 真实写入后读取。不得用冻结220的 f6ca SHA、修复222的 2d1c SHA或本地文字预计值冒当前派生 identity。

唯一 namespace 仍是

`$RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205`。

entry 的唯一 timestamp 先于复制/源形成，原科学18900秒与必要2700秒不重开。工作视图：

`$RUNNER_TEMP/request239-runtime-metadata-workspace`。

环境脚本：

`$RUNNER_TEMP/request239-runtime-env.sh`。

脚本真实导出当前 `GITHUB_WORKSPACE`、`VISIBLE_COMPUTATIONS`、`VISIBLE_BASE`、`REQUEST239_PRIMARY_WORKSPACE`、`REQUEST239_RUNTIME_WORKSPACE` 和 `REQUEST239_CURRENT_INNER_SHA256`。初始 checkout、原真实 Git object database、当前临时 metadata 视图分别记录；不改原 checkout/ref。

actual computations 必须等于当前已加载文件的 HERE，proof directory 是同视图的 topic/results；`VISIBLE_SOURCE_TOPIC` 则仍是原 namespace 内实际恢复的 source subset。所有 caller 使用这些真实路径，不把另一个 clone 的同名文件冒当前模块。

## 3　全部来源集合与生成顺序

实际集合为：

| 范围 | 原238 | 新增 | 本次完整 |
|---|---:|---:|---:|
| public | 302 | 5 | 307 |
| generated | 255 | 56 | 311 |
| 合计 | 557 | 61 | 618 |

新增public是 R569原库、新桥、新composer、新entry和新plan。原557逐名称/完整SHA保留；旧已知 syntax-only历史排除仍只有原两个owner，当前调用不引用它们。

十一层输出数量依次为：

`15 / 5 / 13 / 49 / 51 / 46 / 57 / 6 / 6 / 7 / 56`。

前十层完全沿原已刊输入。新 plan 由原已刊 `root_20261116_current_C_zero_linear_source_views.py`（11895 B / `4d4c507e…`）消费。所有 required_public_sources 都是真 Python 源；不把 JSON政策塞进 source-only 列。新 JSON plan 仍在完整public字节绑定中。

新输出只在全部baseline已真实存在后创建，新basename须不存在；不覆盖旧输出、不把尚未生成的SHA当实际文件。每个新 output 的完整 literal applications、count、baseline和output身份在71KB plan内。只有源码文本形成，无作者环境 Python执行。

当前 same-C八角色由 R544→R567→R570三条真实creator receipt分责：原R544是原七核及原evidence的来源，R567是前一evidence旁诊断的来源，R570才是当前八件实际输出的creator。登记函数不得以旧receipt代替新的source创建。

独立 same-C runtime集合为19件：原四个public C helper、R553/R521、R569/新桥、三个当前metadatacaller以及八个当前同C角色。它与618完整运行源allowlist不是同一个计数。

## 4　三个 driver 的实际 capture 合同

新桥API：

```python
register_runtime(runtime, driver_source)
SolveCapture(runtime, args, problem, phase_dir, phase, driver_source, phase_row)
phase_capture_necessary(phase_directory)
BoundComparison(current, *, angular_count, sqrt_bits, budget_check,
                original_job_deadline)
```

`register_runtime` 绑定四件实际closure成员：R569、R553、R521和桥自身。三个当前driver都在真正原runtime形成后调用它；原checkpoint仍保存实际新closure。

真实solve切点保原顺序：

1. 原完整seed/preflight及scalar/profile准备；
2. 原当前H/完整endpoint Jacobian；
3. 原五cut比较及全部原FD；
4. 新 recorder 上下文中的原 `d.hooks.solve`；
5. 原 driver-status/actual acceptance；
6. `capture.finish` 冻结同次真实对象或记录 unpaid；
7. 原 status/acceptance gate；
8. 原writer的实际CP与全部原audit绑定。

三个实际新driver均新增且只新增以下CLI来源参数：

`--job-deadline PATH --job-deadline-sha256 SHA256`。

这两个值由真实existing owner转发，不能用户填未来deadline，也不按driver启动重算起点。其他originalargv保持。first实际argv完整形状为：

```text
python -u CURRENT_FIRST_DRIVER
  --recipe ACTUAL_RECIPE --recipe-sha256 ACTUAL_RECIPE_SHA
  --job-deadline ORIGINAL_JOB_DEADLINE --job-deadline-sha256 ACTUAL_DEADLINE_SHA
  --candidate-binding ACTUAL_BINDING --candidate-binding-sha256 ACTUAL_BINDING_SHA
  --accepted ORIGINAL_ACCEPTED --accepted-sha256 ORIGINAL_ACCEPTED_SHA
  --complete-seed ACTUAL_COMPLETE_SEED
  --factory-directory ACTUAL_FACTORY_DIRECTORY --factory-result-sha256 ACTUAL_FACTORY_SHA
  --tail-config ACTUAL_CURRENT_CONFIG --tail-config-sha256 ACTUAL_CONFIG_SHA
  --tail-source-root ACTUAL_ORIGINAL_SOURCE_ROOT
  --tail-client ACTUAL_FIRST_3870315A_CLIENT
  --jac-workers ORIGINAL_EXECUTION_WORKERS --node-heap ORIGINAL_EXECUTION_HEAP
  --out ACTUAL_LAUNCH_DIRECTORY/full-BVP
  --work ACTUAL_LAUNCH_DIRECTORY/banded-work
```

refined112/incremental-M的完整driverargv形状为：

```text
python -u ACTUAL_REFINEMENT_DRIVER
  --recipe ACTUAL_NEW_RECIPE --recipe-sha256 ACTUAL_NEW_RECIPE_SHA
  --job-deadline ORIGINAL_JOB_DEADLINE --job-deadline-sha256 ACTUAL_DEADLINE_SHA
  --accepted ORIGINAL_ACCEPTED --accepted-sha256 ORIGINAL_ACCEPTED_SHA
  --parent-directory ACTUAL_ACCEPTED_PARENT_CP
  --parent-manifest-sha256 ACTUAL_PARENT_MANIFEST_SHA
  --tail-config ACTUAL_NEW_NATIVE_CONFIG --tail-config-sha256 ACTUAL_NEW_CONFIG_SHA
  --tail-source-root ACTUAL_ORIGINAL_SOURCE_ROOT
  --tail-client ACTUAL_CURRENT_REGISTERED_CLIENT
  --jac-workers 2 --node-heap 6144
  --out ACTUAL_REFINEMENT_OWNER/refined-BVP
  --work ACTUAL_REFINEMENT_OWNER/banded-work
```

上述占位名仅解释真实owner变量来源，不是预填的父路径或执行配方。真实command由当前已绑定owner生成并完整记录。same-far仍实际复用同job完整原far/μ、重新形成新grid；union仍真实新M deep及新增模态传播、Π列重排，所有新native/J/FD/fullDN重付。

## 5　同次 capsule 的全部输入、输出与失败

每个实际 phase 写：

`same-call-cubic-status.json`

接受后由原R569在同phase新目录写：

`same-call-cubic/result.json` 以及完整九成员：

`mesh.f64le`、`augmented_states.f64le`、
`original_spline_rhs.f64le`、`ppoly_coefficients.f64le`、
`original_rms_residuals.f64le`、`solver_parameters.f64le`、
`physical_states.f64le`、`frozen_physical_rhs.f64le`、
`recomputed_augmented_rhs.f64le`。

R569 result schema：

`R569-same-call-literal-cubic-and-accurate-quintic-v1-capture`。

桥status schema：

`R570-actual-same-call-cubic-capture-and-comparison-v1-phase-capture`。

每个成员保原完整shape、dtype `<f8`、bytes/SHA。PPoly维为原四降幂行×全部span×全部增广列；不以当前675六项系数重建它。所有签名零和原返回有限字保留。原RMS只作为原数据，不是 uniform residual。

普通诊断 setup/copy/write/binding失败进入status，原solve、原返回对象及原acceptance不变。原RuntimeError资源异常继续传播；scope明确未完成。若在result写成前中止，原已写成员保留且necessary列完整identity；没有result不填complete。

桥及原库没有独立cleanup授权。原CP/definition、原fullDN结果、所有原账本都不覆盖。

## 6　当前同C evidence 中的实际消费者

当前 evidence basename：

`geometry_20261116_request239_same_C_cubic_metric_evidence.py`。

schema：

`request239-same-call-cubic-and-complete-metric-evidence-v1`。

真实same-C level0/1/2分别仍对应original112、resolution112、incrementalM。比较与三次measurement使用同一当前evidence，不能混用旧R459或旧R567必要schema。

在当前field/CP已按原family loader绑定后，新 `BoundComparison` 读取该CP自己的phase/capture，继而调用原：

```python
R569.bind_loaded_cubic_quintic(
    current, capture_result=actual_capture,
    capture_sha256=actual_capture_sha,
    angular_count=actual_resolution["field_angular_quadrature"],
    sqrt_bits=original_work["sqrt_bits"],
    budget_check=original_measurement_budget.check)
```

它接收的scalar context来自同一次原prefix `closed_range` 返回，不新增C查询或替换旧factory/target。R569重新验证真实675 coefficient method、完整CP/definition、当前driver与接受fullDN数据、实际材料 `rho_lower`。

新增原cell ledger字段：

- `actual_same_call_cubic_comparison`：完整当前单元诊断；
- `actual_same_call_cubic_retirement`：原split/terminal的分责。

新增measure及compare必要字段：

`actual_same_call_cubic_comparison`。

其中保binding、真实evaluation/terminal计数、三种可用性、退休的partial maxima、所有unpaid terminal地址与实际P/W/d²/错误、完整cell ledger身份、原coverage/error/stop/close_errors。只有原全DFS完成及对应全部prefix terminal已付，才返回相应global-prefix upper；否则只是partial。它不变成全闭域metric或solver floor。

物理角的正确目标是 `diag(mu², A²*rho²)`；实际当前材料密度不能省。P域仍用原 `A²*mu²*W - nu²*|d|^6`。本接口沿R569最终量纲修订，不改原R553/R521的P公式。

原四Loewner/relative-opnorm/refine/root_plan、原full-time共轭、t=4/8/16真实nested queries、tail/collar/patch/帽责任都保持。新诊断不能让原未完成cell被当作退休，不能删pending，不能以两条局部曲线tube代替完整角圈及全闭面。

## 7　真正必要读回及传输边界

三个新phase reader实际调用 `phase_capture_necessary`，均在原quiet后：

| reader责任 | 实际phase位置 | 新必要键 |
|---|---|---|
| first | launch/full-BVP/design453、frozen450 | `actual_same_call_cubic_phases` |
| refined112 | owner/refined-BVP/refined450 | `actual_same_call_literal_cubic` |
| incrementalM | owner/refined-BVP/refined-M | `actual_same_call_literal_cubic` |

此API只用标准库完整读取JSON/流式核成员bytes/SHA；不 import R569数值函数、不重算PPoly、RHS或Bernstein。完整status/result原值及所有成员identity直接保留，未知文件身份也保。原reader先前的另一个scope错误不自动跳过这项独立quiet读回。

refined112的原phase API是R441 `448c35c3…`；union的phase API是原真实 `68c90724…` 的当前来源派生。两者原 `phase_documents` 都不能替这项完整新scope。新总refinement reader的 `solve_view` 明确透传 `actual_same_call_literal_cubic`，不依赖一般 `small`。

完整数组只留同job原件，不进入必要正文。真正新比对失败和所有未付terminal不按成功计数删去。当前各body仍90000 B，超过70，原完整raw保；618-source规模与任意失败数量不保证必fit。

关键frames：

| scope | BEGIN/END中间固定名称 |
|---|---|
| 当前source entry | `REQUEST239_ACTUAL_SOURCE_BINDING_NECESSARY` |
| 十一代完整generation | `REQUEST239_COMPLETE_SOURCE_GENERATION_NECESSARY` |
| 当前source composition | `REQUEST239_SOURCE_COMPOSITION_NECESSARY` |
| 完整refinement | `REQUEST239_REFINEMENT_NECESSARY` |
| same-C source composition | `REQUEST239_SAME_C_SOURCE_COMPOSITION_NECESSARY` |
| 同次cubic measurement/compare | `REQUEST239_SAME_CALL_CUBIC_COMPLETE_METRIC_EVIDENCE` |
| same-C合并必要 | `REQUEST239_SAME_C_COMPLETE_NECESSARY` |

first原R505与successor原R496算法family frame保留，实际producer source descriptor改为本plan真实新文件，报告会包含新scope。其原字段、原errors及原markers不删。same-C首head/三个metric仍其原request230算法schema/frame，真实来源文件已在56表独立登记；不因basename含239就编造新的数值算法schema。

report仍只转发原bounded正文及新增身份/step outcomes；不会把所有full几何raw复制为job outputs。

## 8　完整外层CLI与真实时钟

初始化只从真正checkout调用：

```bash
python3 "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations/root_20261116_request239_actual_source_entry.py" initialize \
  --request "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/current-C-same-call-cubic-refinement239-request.json" \
  --request-sha256 6eb0b2572b8ef204b80e1c5d6172e902c0b37254d305f641cb11bef4f818812f \
  --base "$RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205" \
  --computations "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations"
```

随后每个实际step先source `request239-runtime-env.sh`。源形成：

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_request239_sampling_refinement_composition.py" materialize \
  --request "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/current-C-coast-base-zero-linear-gzip-incremental-M-refinement220-request.json" \
  --request-sha256 "$REQUEST239_CURRENT_INNER_SHA256" \
  --base "$VISIBLE_BASE" --computations "$VISIBLE_COMPUTATIONS"
```

当前同C composer的 `bind`、`preflight`、`prepare`、`readback` 均使用实际239外层请求/其固定SHA及相同base/comp。其中preflight保完整原222 PYPINS科学断言，并按实际current inner SHA/count、当前composer basename与当前239workflow路径作已声明metadata绑定。原sampler schema未改变，不能套用两worker来源的新schema。

正常源必要为 publiccomposer的 `generation-readback` 和 `readback`；新entry有 `readback`、`guard-cleanup`、`cleanup`。完整argv已在本次91KB workflow逐step给出；没有裸无钟科学subprocess。

原首head scope仍1800秒=1650科学+120cut必要+30shutdown；metric240、measurement300、comparison120，所有都裁原绝对clock；原末900保留规则不变。源形成与copy的时间从同一namespace起点计，不另造科学时间。原18900+2700、whole job360分钟和各阶段资源值均继承完整238/205子合同。

原32 GiB启动门、2 GiB运行余量、原采样depth2及value_bits32作为work-only、完整112far/unit rows及所有physical point责任不变。本入口未声明固定预算足以产生任何accepted450。

## 9　正常、部分、recovery与cleanup

新source entry真实receipt为：

`$VISIBLE_BASE/source-binding239/result.json`。

同 job当前inner的真实receipt来自它的 `actual_derived_request`。primary checkout原238/220文件保持；当前工作视图的同路径文件是新形成的实际合同，不能用它反读frozen220原字。

十一代source必要目录：

`source-generation239-readback`。

same-C登记目录：

`same-C239-source-views`；

same-C工作/必要目录：

`same-C-refinement239`、`same-C239-readback`。

实际source、生成preflight、科学未起、普通失败、资源停、capture缺失、measure未启动各自保留。source_generation completed不蕴含science acceptance，necessary complete不蕴含process quiet；二者依原独立谓词。

清理仍须完整原九outcomes、sourcecomposition/11代generation、新sourceentry、same-Ccomposition/necessary以及原owned quiescence全部真实满足。缺marker、unknownscope、超限70或mutable进程仍在，均保raw；不能仅凭capture存在授权删除。

桥没有单独清理方法。capsule完整raw与所有原BVP/cell ledger同namespace保留，只有原最终清理成功event才可宣称removed。原CP还未形成时，一份capture.complete只意味着观察对象已保全，不能替代父资格。

## 10　直接科学输入及原接受责任不变

本次源参数之外，沿真实238完整冻结值：

- R503 explicit coast-base初点；原C/root、全部十词来源；首真实453后同实际末十词冻结450；
- 全原mesh/knots、五factor2的refined112、新M128/fullnewdeep＋旧112/newmodeunion、全部原native stages与steps实际schedule；
- 两mean、全J列、真实当前H、原FD/fullDN、原BC/RMS、final native replay与physical cut audit；
- 同原construction A/B、全部帽markers、原材料定义与尚未付的共同材料责任；
- 原五几何、held、同一g的误差measurement/compare、全t与真实t网格、<5MB显示责任；
- 原原件输入、fresh全far/grid、gzip stored/decoded完整账本、所有源和quiet合同。

新capture保存数据只做诊断，不能替任何下一层真正parent。cap/H/W/ten/eta/K/tau、源root或容差均未被任意重选。若原parent未接受，后继真实refinement与其capture保持原未启动/未付；不从SHA或partial state合成它。

R570比较给出的prefix gap也不是原solver tolerance的量纲转换。欲得到准确全域metric floor，仍需实际cubic residual、全角投影尾/alias、FFT/table形成差、accurate scalar差及完整传播条件；R575另有完整条件库，但本request没有自动调用。

## 11　实际56生成输出的完整身份

以下全部是在公开Actions通过固定plan形成的新源码；不会在作者机器导入或执行。算法schema未改的条目仍保旧格式，而实际source身份以此表和真实generation receipt为准。

| role | 实际新basename | bytes | SHA256 |
|---|---|---:|---|
| first_driver | `geometry_20261116_request239_same_call_cubic_full453_frozen450.py` | 35203 | `51960b100c5d14bb8f8790fca161051e61df8aab93273c59fbec19d4ab91953f` |
| meta_owner | `geometry_20261116_request239_owned_roles.py` | 25730 | `df66d5ee07df57ad2136257a8659a0d51acdc5f2b250d6d314d617cbdf9da4a5` |
| meta_reader | `root_20261116_request239_refinement_necessary.py` | 44584 | `e98445e937f999610bd67cf1d233f34e75530232dc46879447e60340a3903505` |
| meta_same_composer | `root_20261116_request239_same_C_composition.py` | 33381 | `57cb048fb13e776f277422bbaee9a37f9d8023d504650f386bb4870dbb37bd99` |
| meta_same_runner | `geometry_20261116_request239_same_C_refinement.py` | 45658 | `db734305e2c27ed01fbb41a0b4971de226c92cbc2ab3bf08022498c66c0376ae` |
| meta_same_reader | `root_20261116_request239_same_C_necessary.py` | 35746 | `0d19752ff3280a77a6ba8ee522960d3ef1826d2f5439dd15e5e261d8ae2eb75b` |
| first_launcher | `geometry_20261116_request239_same_call_cubic_full453_frozen450_launch.py` | 20615 | `3d6e12241230707ff38567be204d46c059c3aca35f8360d6d90a68d3e0ae865d` |
| first_policy | `geometry_20261116_actual202_captured239_coast_base_zero_linear_gzip_ten450_closed_parameter_policy.py` | 37983 | `feb069b4cadd7d0915bdb57c501f089127fcce893ef7d61b594b78e8d83265e1` |
| 217_head | `geometry_20261116_request239_same_C_full_head.py` | 42275 | `9b777721ab4d6872a05b83c76ac3de2292a7e81b407c05e59aeaf849e6ea9773` |
| first_post | `geometry_20261116_actual202_captured239_coast_base_zero_linear_gzip_coast_ten450_parameter_block_postsolve.py` | 27208 | `23d5f2b99cd1f3dfc967e90db378cbd77aae7b84c305cce723e038b5e3ffe5e8` |
| 217_leaf | `geometry_20261116_request239_same_C_leaf_target_cut.py` | 35531 | `4006dff57a894e26ce4debe8eaa35c3725a3793b84ddd39ca85008ea6c2ad633` |
| first_postreader | `root_20261116_actual202_captured239_coast_base_zero_linear_gzip_coast_ten450_parameter_block_postsolve_necessary.py` | 11237 | `f6ef36b286bf82ae1710ee61b1475af1f0df664bfa0ec2af6536d72bd20fbf42` |
| 217_tail | `geometry_20261116_request239_same_C_tail_queries.py` | 29686 | `d1ea81a9b50a998754bc854a7a42c5fb9ec3ac4c114146af8a7c910e680c0586` |
| first_held | `geometry_20261116_actual202_captured239_coast_base_zero_linear_gzip_coast_ten450_parameter_block_postsolve_held.py` | 5769 | `344c00923ddede5225e3394ea867d439eed2583c394188c643eee64e0b0549cc` |
| first_post_entry | `geometry_20261116_request239_actual202_bound_coast_closed_postsolve.py` | 47503 | `ba8c49fa3894e745557ae9d04e3ae4eb09307ef227e792dbe331e963958b696f` |
| same_worker | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_same_far_native_worker.mjs` | 19900 | `5f12d7d7775e4da1d66c119663897c3487de15663b93fa9a2618ed43d769c319` |
| same_client | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_same_far_tail_client.py` | 23494 | `bef3daf3bef336ae5f1a39471b7d6df5d8dedffc71875cf0bbb550ea035420b3` |
| union_worker | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_native_worker.mjs` | 19805 | `744172e1800295ddab59710b65c790b87c56e3d02431a090c6167c56737a86ad` |
| union_client | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_tail_client.py` | 24012 | `f8ab3769e23a1c9e766b1fc411006ebb23077bf4df7e925bb8edce21ef66f927` |
| first_reader | `root_20261116_actual202_captured239_coast_base_zero_linear_gzip_two_phase_necessary_readout.py` | 32662 | `508885ca68dc0500a8bd5923b2cfb90746ebb118bc4fd25a83cb5160d153a7e9` |
| meta_runner | `geometry_20261116_request239_joint_refinement.py` | 48824 | `622db7398cc4eb6383a1cc78652abe36a4cf7b9810c21ab6cecd9429d79f66e6` |
| same_sampler | `geometry_20261116_current_C_captured239_coast_base_zero_linear_same_far_gzip_resampling.py` | 52151 | `aab3879248821c440871fa4c0d67c9e03eb3796eb70de70ce0e19f92eeda9bff` |
| union_sampler | `geometry_20261116_current_C_captured239_coast_base_zero_linear_incremental_M_gzip_far_union.py` | 55484 | `34eeddf02d3b962cd8c3c57cc33b3bbaf406fc51213e4bb354e417ab8e9b1be7` |
| union_checkpoint | `geometry_20261116_continuous_ten_captured239_coast_base_zero_linear_gzip_incremental_M_checkpoint.py` | 56043 | `2f0e69710f0e09fb6d1ede272130862da1221d2df479790a07a57ba13bd452c0` |
| union_saved | `geometry_20261116_continuous_ten_captured239_coast_base_zero_linear_gzip_incremental_M_saved_prefix.py` | 19310 | `c8bcc4848a501d7ad0277b96e3b3873330a9eea538402d35ecfa2a9c53a0640c` |
| union_radial | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_radial_readout.mjs` | 24193 | `e6a82fe64a29d16e84bdf7bac7bc343db3fe9af3c0b14c5643a6bca2cfbb082d` |
| union_prefix | `geometry_20261116_continuous_ten_captured239_coast_base_zero_linear_gzip_incremental_M_prefix_metric.py` | 32890 | `34f0962868e4d3f5380d481ab3863d72cd1b152b7d0fd82accffa4135a0ea056` |
| union_shared | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_shared_field.py` | 49628 | `66633831e9576b0acdeaa1a68b7a83e2de30b19269b6de31408fa2ef978c6bdd` |
| union_cut | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_accurate_cut_patch.py` | 26248 | `a15d596d48eda963531d54db0ce8b9a55a59840c503e07ea2f56e83000249df2` |
| union_atlas | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_original_cuff_atlas.py` | 29569 | `f80537af9fcf7d1981b1bd86f2fee487373399e712100b5af619c184bcd2565b` |
| union_caps | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_fixed_cap_balls.py` | 23748 | `58e2020af36cd9ba9b91a9fe5fe5a9c5416886c6de7a45a3780aec21be85b32d` |
| union_material | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_common_material_phase.py` | 38968 | `7205fce93be53061714aa8bfc4839116e4702b0a092e44eada6467a0e9b519c9` |
| 217_bridge | `geometry_20261116_request239_same_C_metric_family.py` | 12382 | `18505c4a73a7e09e8cc22079461eaeedbe1d8d669031695baa12bddd3e2f3900` |
| union_reach | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_complete_reach_cover.py` | 60618 | `7795f154f4f2a2258ebdb3340ebcb174b0bf9afcd9dc8667743a588cdcf1bbfa` |
| union_held_consumer | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_held_and_rigidity_inputs.py` | 53942 | `2b593b27f185765cdaec8a3e02c34db0f7ff43193d0334844d1bf64ade317096` |
| union_metric | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_coast_live_query_complete_metric.py` | 56432 | `c666ace931f6028d8d6358c62366cc583890546490578c7a0f91a0181384f732` |
| display | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_multitime_display.py` | 41941 | `57a9a694e086ecf0dcf1cc4f21bffd2aa7f1102e07902d07ce15b9fe22672e4a` |
| 217_metric0 | `geometry_20261116_request239_same_C_original112_metric.py` | 57273 | `a355a75520e74c32e87eba71fea145bf26a995d4c22199ddf873d15755b1d30c` |
| 217_metric1 | `geometry_20261116_request239_same_C_resolution112_metric.py` | 57300 | `76e565fb87490dd2782a03cde53c4c3afbbd2353f24b1c19a92e07900131cd16` |
| 217_metric2 | `geometry_20261116_request239_same_C_incremental_M_metric.py` | 57477 | `6f0f8f06e57ca963754bcc9bffdcafc069e658e33d8308dab5eed7324ba2cb23` |
| union_block | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_complete_block_reach_cover.py` | 45673 | `d28c2c1391ddb09cf04b74e19d778ea6d93479967004f2d8de5165028f55e39b` |
| evidence | `geometry_20261116_captured239_coast_base_zero_linear_gzip_incremental_M_coast_fixed_target_metric_evidence.py` | 63289 | `ace34734150fcca0964e639c05044e2233f27ba3a6497e43ee4f83d3adba147e` |
| same_driver | `geometry_20261116_request239_same_call_cubic_refined112.py` | 56144 | `302e13c6f6ae11809f6469ca38e39c55bd6bdac39fdf2f324479f30fe08066b0` |
| union_driver | `geometry_20261116_request239_same_call_cubic_incremental_M.py` | 52845 | `3c5424c37ac35cde4d55129a34cea69425421faa7d6a97f0fa910f4cde6df715` |
| same_evidence | `geometry_20261116_request239_same_C_cubic_metric_evidence.py` | 69906 | `dc03e07957d4983bd78b9299b79052c203a1e1da2dcbd75fee3a1aaf29562373` |
| same_owner | `geometry_20261116_request239_same_call_cubic_refined112_owned.py` | 57370 | `6bd18cdf13bfee6f88f60db733923e2d132dc2c0937936f2236f72e8f35fb8f2` |
| same_post | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_same_far450_coast_postsolve_geometry.py` | 65888 | `804a0d93d69f58ee699366fc0a0380e7214af853339f5270c2d16ab0c4438645` |
| union_owner | `geometry_20261116_request239_same_call_cubic_incremental_M_owned.py` | 77531 | `288cb2531197ab76eed1276d6af5de332633fa03b61ac9f9413e5a3fe14751bc` |
| union_phase_reader | `root_20261116_continuous_ten_captured239_coast_base_zero_linear_gzip_incremental_M_phase_readout.py` | 19756 | `e0ce1312c959ed7c0c123d9262d19b61e1b0761c9ed8079b11c1dc26b4a457a6` |
| same_postreader | `root_20261116_current_C_captured239_coast_base_zero_linear_gzip_same_far450_coast_postsolve_necessary.py` | 27557 | `ebf8f22c7f0b573448c6ca1cc5b4d83ccc582254cd2543c636b77ed5c7bb9623` |
| same_held | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_same_far450_coast_postsolve_held.py` | 44242 | `c11c1a05c9366015f01bff1e06db2b5ccb7250bed9ea2fc35ce91cf1fc59f458` |
| union_post | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_coast_postsolve_geometry.py` | 72519 | `e398c46d90aff58efd56b815ec17bb4ccb60111bdb64042e90fc36cf1a9f051e` |
| union_postreader | `root_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_coast_postsolve_necessary.py` | 27601 | `2fa2751994d9fc42b56b51a0609f4e9fcc8412d68907168198ffa43f21d9e6e1` |
| union_held | `geometry_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_coast_postsolve_held.py` | 44394 | `ea1feb89b754431435c5c54c78dcd4165b0a1abeff75bf4b5db444f6b2e5bded` |
| same_reader | `root_20261116_current_C_captured239_coast_base_zero_linear_gzip_same_far_necessary_readout.py` | 38807 | `43eb4b2ace963a7249d53e344316e219778b5816da268ec6ea964d8ba40239da` |
| union_reader | `root_20261116_current_C_captured239_coast_base_zero_linear_gzip_incremental_M_necessary_readout.py` | 35584 | `2f27532fe25ef0da70b87f6ce58e124eb854ded8ac513037df9d7ae3c685b850` |

56行中的metadata调用者并非靠改receipt标签生效：原entry先形成完整current source合同，原generation实际写出全部新名，随后真实owner/runner/reader导入这些新路径与其准确SHA。三driver新增参数确由真正launcher传入；所有current CP/Saved/geometry pin都跟随同一实际链。

## 12　完整性边界与作者阶段

本次没有创建科学request的实际run或日志，没有借233/238正在运行的结果，也没有改变其冻结源。root收到完整源码/证明/接口后可按原授权独立发表并单次正式dispatch239；正式run/source/compute必须再由官方元数据确认。

作者仅做完整固定源文字读取、literal substitution/count、JSON来源集合形成和bytes/SHA；不执行Python、AST、compile、science、fixture或独立验证门。源preflight是原公开workflow中的实际工程步骤，没有新增科学门。

所有新常数、capsule、prefix上界与全域结论均需该实际run真正产生。诊断失败既不隐瞒，也不阻原算法因另一个独立科学理由继续；资源deadline则按原所有调用统一生效。

配套完整manifest给出上述六运行件、R570 proof和本接口的最终bytes/SHA/blob。它只包含源码与作者文稿，不含可再生科学raw、原necessary正文或日志。
