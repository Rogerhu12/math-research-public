# Request204：限定 stage 统计类型后的完整原 final128 链

作者：ChatGPT（`/root/amplitude`），2026-11-16。本文主体是冻结时的独立源码、来源和运行合同；实际发布后绑定见第11节。编译、数值输出或性能结论仍须实际终态。发布由协调方统一执行，实际结论预留 R446。

## 1. 本次要完成的具体工作

本请求从真实可恢复的 actual91 输入重新生成 fresh64 现场、完整当前 R273 方向与持久 binary128 owner，随后请求完整 $576\times224$ stage maps、112 维 boundary、$338\times112$ mixed endpoint response 和独立原 audit。全部原数学范围、32×10 上界、原接受标准和总钟均继承 actual199 的冻结入口。

唯一新的 C++ 正文变化已在 [R445](../results/R445-single-qualified-SIMD-stats-type-and-unchanged-stage-body.md) 发表：原 stage 第 44 行的局部声明 `BatchStats literal_stats;` 改为 `simd_digit_trace128::BatchStats literal_stats;`。其余 stage 字节在 R445 的逆替换范围内完全一致；本请求使用该已发表独立源，未另改 C++ 算术、循环、列范围、统计操作或时间检查。

[R424](../results/R424-actual199-persistent128-acceptance-SIMD-type-compile-block-and-partial-audit.md) 已记录 actual199：run `43775312697`、source `51a38839e6dd2763a3fbe2796715bcc0479d3b01`、compute `133000173495`、report `133030931599`。两个 job 的 success 不代表 stage 成功：该次 stage 编译返回 1，原 stderr 为 3462 B / `e3e62b675de0e6ff10fb5354c5248ad9baf1635ecda3d43fe28555b9532cf2d7`，明确报告上述类型歧义。该次 stage 科学程序未启动，boundary、endpoint 未启动，也未观察实际 SIMD backend。

同一次 actual199 的 owner 原 alpha 1 已接受，norm 原词为 `9.68582474751023176056740816374984163e-11`，独立 replay 原词相同；独立 audit 只完成 560/576 个 stage、7305/7488 个 query 和 6771 次 atomic advance。stage 560、561 的 query 9 与 stage 562 的 query 4 已读出，其后 primal advance 未付；stage 563 的 query 0 未完成，564–575 未启动。这些只是本次工程接续的实际动机。旧 raw 已清理，不作为本请求状态、矩阵、audit 或已接受锚；新的 owner、stage 及 audit 是否重现均待 Actions 实付。

本次不需要另造 fixture、微基准、数值对拍、rank 门或额外 stage 逆替换运行检查。原源码 pin、真实编译命令与实际输出身份继续承担来源绑定；R445 是已经发表的源级限定结论。

## 2. 发布文件与 89→94 来源集合

所有 computations 文件位于 `topics/visible-flex-larger-amplitude/computations/`；workflow 位于 `.github/workflows/`；本文位于本课题 `notes/`。本次包含七个新发布文件，另显式引用已发表的 R445 stage。完整 94 项来源字典逐项在 request 内，不以本表替代。

| 角色 / basename | UTF-8 bytes | SHA256 |
|---|---:|---|
| 已发表 stage：`geometry_20261116_native_simd_stats_qualified_stage128.cpp` | 12691 | `eca87efc267d692e401d2ed49904d3d8e73cc16cad12eb3ae24042328f81025e` |
| component launcher：`geometry_20261116_native_simd_stats_qualified_final128.py` | 31930 | `e5c85e6bf5e864de39b0675f997c716466ead0dd158a6c22b73c714257e7433f` |
| bridge：`geometry_20261116_native_simd_stats_qualified_final128_bridge.mjs` | 15829 | `718f1c475b4722eaddeae9eb5bf610c438f2a0c221a7e26e10850fbf00126471` |
| same-job helper：`geometry_20261116_native_simd_stats_qualified_final128_same_job.py` | 38408 | `8855ef79037bf552f44bd926e92ff5b2874fa17e8e35e1773c6344b71fd2c37c` |
| necessary reader：`root_20261116_native_simd_stats_qualified128_necessary.py` | 37574 | `93335c21f6129b1f7ae5c62b2ae7db5e90039fcb30ccfdef1a3951985cb24ee7` |
| request：`public-native-simd-stats-qualified-final128-request.json` | 76649 | `7e6f600e76ea5023c63e98fe0a3899e0eb532d7d65f672a59f5bc4411e9bd871` |
| workflow：`visible-larger-public-native-simd-stats-qualified-final128.yml` | 31909 | `b5854ae59730074bd2f634c011fec64d39e5c77498e0b9f537534dd117d07ce0` |

原 request199 为 67933 B / `7901f228bef74811d70e93fefe3eb8bc8e70675bfc4ffcc2d841112d889125d5`，其 `source_sha256` 实际含 89 个不同 basename。本次保留这 89 个键和值，追加上表 stage 和四个新运行/读回源，得到 94 项；workflow 的原 89 个 `required` 名称也完整保留，再追加这五个名称。没有通过全局换名删除旧 pin。

新 `input_contract.independent_new_source_count=5`、`total_source_count=94`。旧 request199 内继承的 `7/84` 字段另置于明确的 `historical_count_fields_in_original199_request`；它们不是本次计数，也不是原 request199 实际字典长度。新 `frozen199_source_baseline` 保留其 source commit、request/workflow 原 bytes/SHA、89 项范围和旧入口的历史角色。

R445 stage 的公开 commit 为 `00dd915451868adb3557f24c67b4579033139ed5`，Git blob 为 `16559cb793d00206a616ab982334ac9b8da695f3`。四新入口、request、workflow 的小文本 blob 在完整 `publication-files.json` 中列明；同目录完整差异和来源字节回执只供源级复核，不是计算产物，也不作为新的运行门。

## 3. 实际编译源与保留的历史限定视图

新 launcher 将旧 `geometry_20261115_native_simd_digit_operator_stage128.cpp` 保留为 `BASELINE_STAGE`，pin 仍为 `b6537c6ce86754a6a2a75eb928e543a7083fa2311eb70a4764066f2a70dda91a`。`STAGE` 则明确指向本次 R445 新文件及 `eca87efc…`。`OWN_PINS` 同时含二者；旧文件只供原来源核对，新文件是真正传给 g++、复制至本次自有编译目录的 translation unit。request 的 `persistent128_experiment.stage_derivative_executable_source`、`qualified_JSON_compilation.actual_independent_stage`、`exact_digit_implementation.stage` 都指向同一新文件。

`compile_stage()` 和 `bound_process()` 的数值/编译流程沿原文：只把实际 translation-unit 路径指向本次编译目录中的新 stage；原 flags 仍为 `-std=gnu++17 -O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math`，链接 `-lquadmath`。无全局 `-mavx2`、`-march=native`、新依赖或性能门。

以下原作用源保持全部字节：SIMD operator header `b183eeec…`、R405 exact digit kernel `5c2a0cb1…`、R414 SIMD digit kernel `1695b945…`、hoisted header `ab246a53…`、通用参数非空 fallback 的原 R305 header 及原 v2 JSON qualifier。新 compiler binding 保留实际 source copy/命令/sha，并增加原 stage baseline receipt 与 `stage_single_stats_type_qualified=true`。

[R423](../results/R423-qualified-column-environment-calls-and-unchanged-numerical-program.md) 的 `qualified_recorded_source()` **整个函数逐字保留**。它仍从原 b16 header 与已发表 f82 header 读取，保原三次 `column_environment(parameters,field,col,state.columns)` 的明确 namespace 视图、原逆替换检查和实际编译 include receipt。其历史 schema `native199-three-call-source-view-v1` 不改成 204：它标识同一个已发表三调用源变换，不是本 job 的请求号。实际 include basename 仍为原 b16 文件名，但临时 include 字节明确来自 f82；旧 b16 的字节从不冒充实际执行的 f82 字节。

本次 scope 和 necessary reader 对应保留三项准确字段：

- `three_call_namespace_fix_retained=true`；
- `original196_header_and_digit_kernel_bytes_unchanged=true`；
- `stage_single_stats_type_qualified=true`。

旧 current scope 中的 `independent_three_call_namespace_fix_only` 与“stage 字节未变”的合并断言不再作为本次字段。旧 request199 的变更描述被明确保留在历史对象内；当前源码和 request 不把新增的类型限定说成只有三调用限定。

## 4. 当前 schema、编号及来源依赖

| 实际对象 | 当前 schema |
|---|---|
| request | `public-native-persistent128-simd-stats-qualified-final-components-request-v1` |
| same-job procedure | `native-persistent128-simd-digit-stats-qualified-same-job-final-components-procedure-v1` |
| component launcher summary | `native-persistent128-simd-digit-stats-qualified-final-components-launch-v1` |
| stage scientific report | `native-persistent128-complete-simd-dyadic-recorded-stage-maps-v1` |
| necessary readback | `native-simd-digit128-stats-qualified-complete-chain-necessary-readback-v1` |
| compiler input binding | `native128-simd-stats-qualified-operator-compiler-input-v1` |

stage report schema 沿原 R414 实际 stage 输出，类型限定并未创造新的数学 report；不能为了换请求号把真实 stage schema 改标签。component/helper/reader 有独立当前 schema 和源 SHA。bridge 通过环境传入本次 helper 的实际源 SHA，helper 固定新 bridge 与新 component launcher 的 SHA；这样保留原无自引用 hash 环的接线。

reader 的 `build().request_number` 与 `main()` 的 request guard 两处均为 **204**。workflow 的 request schema、number、lane、component source/schema、report schema、所有当前事件、summary framing、close receipt 和 owned directories 均同步。原请求 192/196 的实际错误给出了为什么两处常数都要准确的来源证据；本次不以存在新源码推断已成功读回。

lane 为 `nativesimdstatsqualifiedfinal128`。stdout 分隔符为 `BEGIN_VISIBLE204_NECESSARY_SUMMARY` / `END_VISIBLE204_NECESSARY_SUMMARY`；GITHUB_OUTPUT 三键仍为 `scalar_summary`、`scalar_summary_bytes`、`scalar_summary_sha256`。打印分隔 LF 不计入该 scalar body 的 bytes/SHA；临时 `necessary-summary.json` 的末 LF 和原 file receipt 另按真实字节处理。

## 5. 同一个新现场内的完整科学链

实际 job 使用原 complete actual91 artifact、两份历史 ready 输入、原 78 source 恢复与已 pin 的 numerical slope adapter。它建立一次 fresh64 当前现场，支付原完整 withJ、R273 全行/节点 penalty，然后生成本次 packet 与完整 physical geometry/table binding。旧 133、140、160、186、190、192、196、199 的已删 final state、stage maps、audit 或 SHA 均不作为可恢复 raw。

持久 C++ owner 保原 binary128 state、完整 226 态和 129248 行 residual。fixed initial fresh64 J 只作近似 chord；每轮当前 binary128 residual 投影至 64 位供原 QR，解回后按原 lifted sigma 在 binary128 中形成方向。不能把旧 64 J 叫作当前 128 exact Jacobian。原 32 方向×10 alpha、严格原 norm 降低、原 $2\times10^{-9}$ 门、原 root 有限停止/回溯及独立 replay 仍保。

owner 返回且真实末态仍在时，helper 顺序调用 `stages → boundary → endpoint → audit`。stage 要求完整 0..575、column 0..223；boundary 只消费真实完整 stage 所需数据，endpoint 只消费真实完整 boundary。独立 audit 按原资源保留，即使 stage/boundary 不完整也仍有自己的原路径和未付记录。未完成的前件不能用旧 schema、旧数组或 guessed success 代替。

R402 算子仍是原 recorded coefficients、literal sine/cosine/Gram 与实际名义 Cholesky 因子的准确实线性对象。名义因子乘积没有被认成原 C；所有原 `C*ds-right` 读数、逐 factor/两次回代、原 root trace、全部 224 列和原状态均保。R405/R414 的 once-RN113 dot 合同覆盖完整 dyadic dot；它不支付小 H 系数重关联或完整方向/ODE 的严格外包。实际 CPU 选择 AVX2 或完整 scalar fallback 是程序分支，既不是科学门，也不能从 source presence 预报其统计。

mixed endpoint 仍沿原 $338\times112$ 定义：first112/meanSlope 用当前 trace/RHS 方向；second/meanSecond/height 保原对称差分程序。独立 physical audit 的 C-based radial 公式不冒称有限 root trace 的准确径向导数。即使所有有限 component 完成，也不因此直接给出 native/fullDN 接受或几何定理；原 flags 逐项返回。

## 6. 原输入、原 rules runner 与唯一总钟

actual91 artifact 固定 run `43672150224` / artifact `14145200674`，名称 `visible-mainline-modelresponse-43672150224-1`，ZIP 10267458 B / `78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6`。其 source 为 `b78f0dd1471a118d2ed21467602509d188c2ab67`；完整输入、result/binding 与选中初猜身份在 request 原对象中逐值保留。这是原失败 guess 的真实来源，不是新的 accepted checkpoint。

两份 ready 从 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复到本次 RUNNER_TEMP：原 ledger ready 109004 B / `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6`；stored ready 29774 B / `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d`。仍只接原 `VISIBLE_FLEX_FROZEN_LEDGER_READY`、`VISIBLE_FLEX_FROZEN_STORED_READY` 槽，逐历史 blob/bytes/SHA 验证，不查当前 main 已删的 raw 路径，不重归档输入。

原 rules runner `root_20261114_current576_rules_runner.py` 保原源码和 2700 s 周期、真实 pull/rebase、H 唯一规则同步行、发现新规则时停止原 science 进程组。只依当前已明确读过的 README 原文更新其内存 BASELINES：根 blob `21bd547f56590b7f2dd279d0297efb289a9b2783`，课题 blob `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。science 保 triggering checkout。setup 沿原 `merge.stat=false`；不因历史 raw 删除让 diffstat 读取大量旧 blob。

| 资源项目 | 原显式值 / 实际责任 |
|---|---|
| 整体 science monotonic cap | 19200 s，fresh64 factory/J/R273/exports/编译均计入 |
| readback / cleanup reserve | 120 s；原末 60 s、child grace 与 quiet 规则保留 |
| owner 总 cap | 6000 s，含 owner 内 fresh replay |
| fresh replay reserve | 1200 s，实际余钟不足时保原明确资源分配记录 |
| stage scientific cap / overhead | 8000 s / 345 s |
| boundary scientific cap / overhead | 600 s / 720 s |
| endpoint scientific cap / overhead | 600 s / 345 s |
| independent audit scientific cap / overhead | 1800 s / 345 s |
| threads | 4 |
| science step / compute job | 330 / 350 min |
| 原 native iterations / trials / tol | 32 / 10 / `2e-9` |
| 原 R273 eta / workers / factor bytes | `1` / 2 / 2147483648 |

各 cap 是上界，不保证全部 576×224 在余钟内完成。component 的编译、binding 与内部读回消耗同一 allowance；原 30 s component cleanup reserve、15 s child grace 及 audit reserve 都保留。bridge 询问同一 Python monotonic deadline，不混用 Node 时钟、不在 component 启动时重启总钟。源中的原 `19900` 参数上界没有因请求编号替换而变成 `20400`。

## 7. 可直接执行的 workflow 接线

新 request path 的 push 触发新 workflow，concurrency 为 `visible-larger-public-native-simd-stats-qualified-final128`，不取消旧请求。新 compute 沿原 Python/Node/npm 无新增依赖；Python `compile(...,'exec')` 与 `node --check` 仍只在 Actions 原前置执行。此交付未在本地进行 AST、编译、导入科学模块、fixture 或数值运算。

原 rules runner 的 `--command` 中用既有 bootstrap 去掉 `GH_TOKEN/GITHUB_TOKEN/MR_TOKEN` 后执行新 helper。实际参数完整沿 request 读入，等价的 current argv 为：

```text
geometry_20261116_native_simd_stats_qualified_final128_same_job.py
  --total-seconds 19200 --readback-cleanup-reserve-seconds 120
  --final-stages-seconds 8000 --final-boundary-seconds 600
  --final-endpoint-seconds 600 --final-audit-seconds 1800
  --seconds 6000 --threads 4 --fresh-replay-reserve-seconds 1200
  --matched-trace none --final-stage-columns 0
  --original91-directory $VISIBLE_PARENT91
  --source-topic $VISIBLE_SOURCE_TOPIC --out $VISIBLE_OUT/native-work
```

`--final-stage-columns 0` 只禁用旧 owner 的重复列 loop；随后独立 component 仍实际请求全部 576×224，不能把这个 0 当缩列。component helper 的 `--operator-components`、输入 packet/binding/owner/current state、绝对 deadline、各科学 cap、全部列范围和四个消费者按原全文构造，没有独立短 benchmark 阶段。

三棵自有临时树独占为：

- `$RUNNER_TEMP/visible-native-simd_stats_qualified_digit-final204`；
- `$RUNNER_TEMP/actual91-exact_digit-final204-parent`；
- `$RUNNER_TEMP/native-simd_stats_qualified_digit-final204-public-original-source`。

owner/components 位于第一棵树的 `native-simd_stats_qualified_digit-final128-owned-work`，probe 仍为 `native-work`，close record 为 `native204-child-close.json`。always reader 接这三者、当前 request 和 `necessary-summary.json`。report job 只接本 compute 的三个 scalar 输出和真实 compute result，核 bytes/SHA/schema 后打印同一必要正文；缺输出只报告缺失，不补全数值。

## 8. 单份 90KB 必要范围与诚实的未付责任

reader 继承原 182→199 的必要选择，不传整棵科学数据树。它在 Actions 内读取真实 owner/probe/component 原 metadata，保原数字 token、全部原 owner trial/evaluation 行及各自 key-set；只有整个原 evaluation 字典字面相同才引用同一正文，缺键不等同 null。stage 未完成记录保全部实际 stage/input/output 地址，只有全部非地址字段原文相同才分组；失败 stage 同样保每个明确地址和原错误。成功大列、factor、矩阵和 angular 表只返回原 identity/count，reader 不重新读算 numeric arrays，也不据成功数推未访后缀。

四 component 的 original scientific/procedure/transport flags、process returncode、resource partial、实际 scope、completed/unfinished 地址、实际 integer/SIMD backend/counters 和原误差项继续按实际字段选择。`three_call_namespace_fix_retained` 等三字段同步进入 current necessary keep。scientific child 的 exit 70 与必要摘要自身的 protocol 70 保持分列；缺记录不能变成 stage 数学失败。

engineering stderr/compiler stdout 在 Actions 内完整读其原文件以取身份，但正文是原有必要选择：普通错误文本不超过 6000 B 时可完整返回，较大文本选原匹配首四/末四行，或无匹配时首三/末三；文件集合原 necessary text 总 cap 为 16000 B，完整小文件只在原 `<=4000 B` 及余量条件下返回。其余保原 file/line bytes/SHA、匹配数、选择说明。科学大 stdout 不冒充错误日志搬回。本文不声称所有 traceback、compiler 输出或成功数值表均公开逐字返回。

必要 ASCII JSON 硬上限仍为 **90000 B**，包括临时文件 framing 检查。若超限或 metadata 不完整，reader 明确 `summary_complete=false` / `transport_complete=false` / 70，保超限 bytes/SHA 与真实可用范围；不分片、不编码科学数据、不删除 trial 字段来伪装完整，也不许据本次静态文件长度预测未来必定低于 90KB。正常 report 的 body identity 与文件末 LF 分开。

## 9. 原静止、条件清理和异常边界

same-job helper 沿原 owner/probe 临时 metadata reversals、precleanup hook 和生命周期。原数值 owner 的每方向 raw 退休规则不变；末态和各 component 输入/输出留在同一 job 至原消费者、necessary reader 完成。helper 在实际 fresh child poll/wait 后写 `native204-child-close.json`；reader 核 child reaped 和同用户 `/proc` cmdline 中本请求 owner/probe 路径的静止观察，相关 unreadable 记录不会默认为 quiet。

workflow 最后仅在 necessary schema/current provenance、`summary_complete`、`transport_complete`、`cleanup_allowed` 及 child reaped 同时成立后，再扫描三棵自有路径。任何匹配或 unreadable、必要摘要缺失/超限均明确 skip cleanup。只有真 quiet 后才删本请求三棵树；actual91 readonly 目录按原同属主、非 symlink 约束恢复 owner 权限再删。该工程合同不增数学接受门，也不宣称能恢复 runner teardown 后的 raw。

没有新 artifact、Release、Git raw 或归档上传。未来如果本次仍工程失败或资源 partial，新的实验必须从同公开 input/source 真重生原前缀，不能用本次摘要、word、hash 或已删父件冒充活跃 owner。后续实际 R446 将分别记 job 状态、编译状态、科学阶段、完整/未付地址、必要传输与清理，不以 job success 代数学完成。

## 10. 本地完成范围与复核材料

本地仅做源码文字替换、JSON 字段选择、文件字节/hash 和完整文本 diff：原 89 pins 逐值保留，当前 94 名与实际新五名一致；原 `inputs`、geometry inputs、compiler、wall-clock 对象、eta/workers/factor/native 阈值等 JSON 值不变；原 `qualified_recorded_source()` 全段逐字同；当前声明中的 stage、component/helper/reader schema 与编号相互吻合。所有运行与科学效果仍由公开 Actions 真实执行确定。

交付目录为 `/workspace/visible-larger-working/native-qualified204/`。每个新运行源、request 和 workflow 都有相对冻结199的 `*.complete.diff`；已发表 stage 有独立 R445 单声明差异。`publication-files.json` 给完整公开 path、local path、bytes、SHA256、Git blob 及 stage 已发表标志；`complete-difference-index.json` 给全部差异身份。准备脚本和文字回执仅解释源制作，不加入 workflow，不成为新的审计或准入步骤。

本次没有实际 source commit/run/job 可预填。根协调方发布后绑定新的真实 source/run；本 agent 独占终态必要日志读取并形成 R446。任何新的 compile、SIMD backend、全 stage 完成、native/fullDN/几何结论必须来自该真实返回。

## 11. 发布后的实际source/run绑定

[204实际运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43789310271)已由公开push启动，source189579b508930d99d9c2dbc481967fd972766919，官方in_progress；入口request7e6f600e/workflowb5854ae5未改，R446由amplitude唯一终态读回。当前仅元数据，未取运行中日志，编译/native/组件完成不预填。

触发提交的源文件、request和workflow字节与第2节完全相同。本文后加元数据绑定不触发另一科学运行；两份README经最近真实pull核对未变。初始官方元数据没有提供任何编译或数学通过证据。
