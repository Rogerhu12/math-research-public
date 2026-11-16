# R483：完整 coast range helper、五个实际 metric 视图与调用接口

作者：OpenAI / ChatGPT exact_refinement agent  
日期：2026-11-16  
状态：独立 requestless 运行源、字面 source plan 和条件接口；没有新请求、工作流、dispatch 或实际科学结果。这里只完成文本组成与真实字节身份，未执行 import、AST、编译、对拍、fixture 或科学计算。

## 1. 交付与范围

本次交付三个小运行件：完整 coast Bernstein helper、标准库 source-view generator、五视图的完整字面 plan。另交[R483 条件证明](../results/R483-complete-coast-Bernstein-ranges-in-current-metric-consumers.md)。它们只改变已有准确 prefix target 的范围求值，不改变原完整十族定义/field/数值 compiler/目标 C 或 native 求解。

直接作用点是原 R400 Prefix.inspect 的 target 参数，以及原 R459 Measurement.target 内的真实 prefix closed_range 调用。五个生成源有自己的新 basename、schema、frame、完整 bytes/SHA。它们运行时确实调用新 helper，不只是新增一个未被使用的函数。

R418 固定 query、R426 original112 live query、R441 resolution112、R451 completeM 及 R459 原三族 evidence 是本次来源。**R464 incremental-M union 未注册**。原 72c factory 的 main/prove_domain 和 result 身份保持不动，故其初点域未付也不被本稿改成已付。后续 216 若消费 214 的实际 union 三层链，必须独立接在其真实生成视图之后，明确新的实际 family、schema 与全 diff；本接口不冒称已经完成。

### 1.1 正式小运行件

|角色|basename|字节|SHA256|
|---|---|---:|---|
|准确 coast helper|geometry_20261116_complete_coast_bernstein_enclosures.py|18291|3730c62b5c1a40fb594c9a2d9ed95a523a9134f12eb0b8def59c764d79e3edae|
|Actions 源视图生成器|root_20261116_complete_coast_metric_source_views.py|8742|d149d85103fd555908239f71f963b575a8197a210584d0b043b5d9415c106ae1|
|完整字面计划|r483-complete-coast-metric-source-plan.json|31012|7e71fe0cbff882060bb64b576f3b9e5f56fc6b548f97d1786587ad1bceef00d1|

三件进入 computations。科学 proof 进入 results，本接口进入 notes；五个展开源仅在暂存目录供全文阅读，并由未来 Actions 生成。完整 diff/manifest 是暂存发布材料，不另存五份重复大源码。

## 2. 每个真实基线和新输出

下表只列本次字面变换的直接基线。它不代替原 consumer 的完整递归 source pins。

|键|原 basename|原字节|原 SHA256|
|---|---|---:|---|
|fixed|geometry_20261115_current_C_ten_complete_relative_metric.py|49975|28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590|
|original|geometry_20261115_current_C_ten_live_query_complete_metric.py|55040|77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892|
|resolution|geometry_20261116_current_C_resolution_live_query_complete_metric.py|55053|fd263af28a7d55a7246a49283d367e420786f48f16556dd5a7d61406b1c8459b|
|modes|geometry_20261116_current_C_M_live_query_complete_metric.py|55048|fc35c6408aacbf2131a89fbac37ca4ae98c1665d9fbdc4ba78a50a43ca7f3a47|
|evidence|geometry_20261116_fixed_target_complete_metric_evidence.py|62091|494fea70b97404af2be8ef0f3d685fadc2f59c6a30ea3af771de98a56b868b05|

|键|生成 basename|生成字节|生成 SHA256|
|---|---|---:|---|
|fixed|geometry_20261116_current_C_coast_fixed_query_complete_metric.py|51403|53a1e04bd1c28fc9e0430fbc2ced9d7e91870b2b610af9b29d8fd4a590aebd90|
|original|geometry_20261116_current_C_coast_live_query_complete_metric.py|56226|fb6f05cc505727401e165d2a65f6c5071b3b253f281f6ee84ef4b52b60aab535|
|resolution|geometry_20261116_current_C_resolution_coast_live_query_complete_metric.py|56258|37db784cada1a426eaf0aa59f04d10c1da0c3bdad4e1102c5e9712b1d1dfa61b|
|modes|geometry_20261116_current_C_M_coast_live_query_complete_metric.py|56210|44f5b66d59b35d35ff5e59da1496820fc23afb7b5c0430f2d4b2d6a31d54b25b|
|evidence|geometry_20261116_coast_fixed_target_complete_metric_evidence.py|62889|1d11359f03cd88b028c22201cef68a401fd9589a59718e813ac3cdc4c63461ab|

|键|实际新 schema|BEGIN/END 之间的 frame 标识|字面替换条数|
|---|---|---|---:|
|fixed|R483-current-C-fixed-query-coast-Bernstein-complete-metric-v1|R483_CURRENT_C_FIXED_QUERY_COAST_METRIC_SUMMARY|15|
|original|R483-current-C-original112-coast-Bernstein-live-metric-v1|R483_CURRENT_C_ORIGINAL112_COAST_LIVE_METRIC_SUMMARY|18|
|resolution|R483-current-C-resolution112-coast-Bernstein-live-metric-v1|R483_CURRENT_C_RESOLUTION112_COAST_LIVE_METRIC_SUMMARY|18|
|modes|R483-current-C-completeM-coast-Bernstein-live-metric-v1|R483_CURRENT_C_COMPLETE_M_COAST_LIVE_METRIC_SUMMARY|18|
|evidence|R483-fixed-target-coast-Bernstein-complete-metric-evidence-v1|R483_COAST_FIXED_TARGET_METRIC_EVIDENCE|21|

frame 表内标识在实际输出前缀分别加 BEGIN_、END_；每个必要正文仍只有一个完整 JSON。evidence 的 measure-input、compare-input、actual-series schema 分别由表内 schema 加 -measure-input-v1、-compare-input-v1、-actual-series-v1 派生。不能给新入口旧 R459 input schema 后伪称它已经绑定新实现。

### 2.1 原数学 source 与原对象仍固定

原工厂为 geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py，SHA256 72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682。新 helper 使用其原 Box、CONTROL_TERMS、bump_polynomial、differentiated 和不变的非 coast piece_range。它不调用 factory.main 或重写 definition.source_sha256。

四个 metric 视图的全部既有 SOURCE_PINS 保留，另加新 helper 和实际基线 source 身份。运行时 old baseline 仅核原字节，不能把它作为新 view 执行文件。其余 Cut/Prefix/Kernel/C/Cuff/Cap/Live 加载器继续按原 source tuple 运行。M 的 Prefix/field 仍为完整动态 M 实现；不能以 original112 视图接受 M 场。

evidence 的 FAMILIES 明确改指三个新 live view 完整 tuple，保原 original112、resolution112、completeM 字面 family。它真实加载每个所选 view 的 COAST_NAME，并继续加载该 family 原 Cut/Prefix/Kernel/C/Cuff/Cap/Live。原 R457 common-material 来源、原 full target/first material/完整帽与目标签名保持原字节/规则。R464 union 不在这三个 tuple 中。

## 3. Helper 的实际 API 与包含条件

helper schema 为 R483-complete-ten-coast-Bernstein-range-adapter-v1。它是库，没有独立科学 CLI。

主要调用是 CoastTargetRange(original_target)。original_target 必须已经由原真实 complete-ten loader 成功绑定，包含 Factory、definition、model、values、parameters、pieces、supports、length、numeric_length、binding 等原属性。适配器保 original 引用，但不写其属性、不写 current.target，也不改任何模块的全局函数。

适配器实现：

- closed_range(left,right)：沿原准确有理数数值坐标，返回 (three_jets,radial_metric,report)；真实参数范围是 $0\le left\le right\le L_{\rm num}$。
- describe()：返回新 range implementation 与原完整目标/definition/C 输入绑定的独立 receipt、所有十个准确词、piece/support 数、实际 coast 选择/原回退原因和未支付范围。
- status()：返回开始/完成/缓存命中/全部候选/coast 原公式/原 factory 候选计数及最后原查询地址；这些计数不等于全域完成。
- 其余原只读属性经 __getattr__ 委托到 original，原 target.binding 数学身份保持不变。

底层 piece_range(Factory,model,values,piece,local,include_controls) 返回 (three_jets,scope)。context 参数只给同一已绑定适配器的预先形成 coast 结构；所有当前视图实际使用 include_controls=True。

coast_context 从准确 DAG 识别共享 anchor/width 及线性系数 $-\kappa\ell$，读取原准确常数 $\kappa$，不使用区间商反求。第三支撑的三个项索引 $2,5,8$ 全部合并为次数至多 8 的准确 $P$，其他七项由真实支撑闭端点和原零二 jet 证明为零；第十项仍保在全部 control_terms 中。若结构或其他支撑排除条件未满足，使用原 Factory.piece_range，不新增科学拒绝。

选中时保原恒等式

$$
a=A-\kappa\ell t+\ell^2P(t),\qquad
a_s=-\kappa+\ell P'(t),\qquad
a_{ss}=P''(t).
$$

半径使用完整 $3\times9$ 二维 Bernstein 系数；速度使用两个完整 $\ell$ 端点各八个系数；二阶导数使用七个系数。所有未达最高次数的零槽仍保留。每个宽度/局部闭端点都在包围内，没有长度样本或四角 radius 代替全矩形。

准确位置仍按 $s_{\rm true}=L_{\rm true}s_{\rm num}/L_{\rm num}$。适配器对每个原 piece 形成与 actual local_interval 的闭交，遍历全部片后 hull 三 jet。它不令 coast 局部 $t=u$、不以名义片查找忽略 seam，也不把 numeric length 等同准确 length。radial metric 沿原 $(L_{\rm true}/L_{\rm num})^2$ 返回；物质角密度仍由原 field/Kernel 形成。

所有区间运算与科学调用只能在指定公共仓库的 Actions 内。当前文本交付没有运行这些 API。

## 4. 真实调用位置与不变部分

### 4.1 四个 metric 视图

genuine Cut.load_accurate_cut_field 返回后，视图构造 prefix_range=CoastTargetRange(current_bundle.target)。随后 inspect_cell，及 live 路径的 inspect_cell_once，都显式接收 prefix_range。原 prefix 分支把它传到 Prefix.inspect；两处 live retry 的实参也同步。current_bundle.target 本身不动。

新增两类来源记录：

- large-arrays/same-target-coast-range-binding.json：新适配器 describe 的实际内容，作为 members.prefix_range_implementation；
- binding.actual_prefix_range_implementation 及实际 result/summary 的 actual_prefix_range_work。

原 field evaluate、所有六 jet、全 M/means、Loewner 四不等式、eta、完整片 universe、root_plan、all pending/coverage、两帽/反射/native/collar/tail 均按各原基线原文。原 scalar radius 正下界不足仍是原未决；不据新范围直接宣称 scalar speed 或全域 factory 已证。

### 4.2 新 evidence 视图

Measurement.bind 真实加载所选新 metric source 和 helper，原 current field 与 common material 照原 binder形成。Measurement.target 的 prefix 分支改为 self.prefix_range.closed_range；原径向 C 和其 live-query 路径保持不动。

因此其完整闭域误差上界工作和逐个真实时间/空间见证都消费新 coast 范围，而非只在一个 metadata 描述里登记新 source。compare 的层级关系、同 first B/完整闭面目标/原 clock、sup 严格下降充分条件、仅上界改善与区间重叠未决的区分都不改。有限 t 网格没有变成全 t 证明。

原 source 中的 R459 方法名称和历史错误说明是其算法来源；实际 INPUT_SCHEMA/SERIES_SCHEMA/frame/source bytes 已全部是本稿新身份。

## 5. 源视图生成 CLI 与生命周期

生成器只在未来已授权 Actions 实际运行。调用形式为：

    python -u "$COMPUTATIONS/root_20261116_complete_coast_metric_source_views.py" \
      --computations "$COMPUTATIONS" \
      --plan "$COMPUTATIONS/r483-complete-coast-metric-source-plan.json" \
      --plan-sha256 7e71fe0cbff882060bb64b576f3b9e5f56fc6b548f97d1786587ad1bceef00d1 \
      --out "$OWN_NAMESPACE/R483-source-generation"

COMPUTATIONS 必须是当前 GITHUB_WORKSPACE 内真实 checkout 的 topics/visible-flex-larger-amplitude/computations 目录；包括实际 repro/source-root checkout 的这个真实后缀。它不能是复制了一小部分依赖的私有源码树。OUT 必须是 RUNNER_TEMP 内全新目录，不能拥有 source 目录或覆盖已有结果。调用者须把 helper/generator/plan 及全部原完整 source 闭包置于实际目录并逐真实输入合同绑定。

生成器操作次序：

1. 核实际 public Actions/repository、路径、plan 完整 bytes/SHA/schema。
2. 核 helper 原字节；读取五个完整原基线。按 plan 的顺序逐条检查 before 字面出现次数等于声明 count，形成新 source。
3. 核五个完整输出 bytes/SHA，且新名字彼此不同，不等于任一 baseline/helper，也不覆盖已有文件。
4. 在真实 computations 以新名字逐个独占写入并 fsync，再读回核完整字节。只有全部完成才 completed=true。
5. 在 OUT/result.json 留实际 run/source/plan/helper/baseline/output receipt、当前/失败位置、错误类型/完整字符串与 elapsed；只输出一个 metadata frame BEGIN_R483_COMPLETE_COAST_SOURCE_VIEWS / END_R483_COMPLETE_COAST_SOURCE_VIEWS。

原来源不修改，生成器不 import、AST、compile 或执行科学源码。未来正常工作流的原语法阶段可检查所生成源码，但本交付没有新增对拍、独立审计或数学前门。

计划只覆盖本次变换，**不是 transitive 科学闭包清单**。未来 caller 必须保原各入口的全部 old pins、原输入/compiled module source dependencies、proof/owner，另列三小运行件及五个真实生成输出；不能把五个基线或新 direct_source_closure 当整个依赖图。

全部基线/输出形成后才写新文件，减少半套源的机会；但写入/I/O 仍可能中断。若发生中间错误，实际已写 outputs 和 current_view 如实保，不能执行为完整五视图。早期路径/plan 绑定失败发生在状态对象以前，可能没有 result.json；caller 应保原 stderr/exit、science unstarted，并跳过未经授权的 cleanup，不构造不存在的 receipt。

生成器没有 child、owner quiet、raw cleanup、全局 science clock 或新预算。其 source generation 完成不代表科学结果完成；后续仍使用原 job 的绝对钟和必要读回/quiet 合同。

## 6. 实际 metric CLI：原参数完整保留

四个视图的 main CLI 与各原基线相同。共同字段如下：

|字段|原责任|
|---|---|
|--computations|实际源码目录，默认新 view 的真实 HERE|
|--directory / --result-sha256|相应 family 实际准确 field 目录和原 result 身份|
|--checkpoint-directory / --proof-directory|原 checkpoint 与 proof 真实目录|
|--cuff-atlas / --cuff-atlas-sha256|同 field 的真实 cuff atlas|
|--continuous-e-result / --continuous-e-result-sha256|同现场完整 C 的原 result|
|--eta|原严格 metric 目标，非新 solver 门|
|--interval-bits / --sqrt-bits|原区间/树平方根工作精度|
|--initial-angular-depth / --max-depth|原完整角格与空间细分上限|
|--max-visited-cells / --budget-seconds|原完整访问计数与工作时间|
|--out|新鲜输出目录，原 raw/ledger 生命周期|

三个 live view 另保原十一项必填 C query 参数：

|CLI|原 c_queries 键|
|---|---|
|--c-query-precision-bits|precision_bits|
|--c-query-integral-absolute-bits|integral_absolute_bits|
|--c-query-integral-relative-bits|integral_relative_bits|
|--c-query-analytic-guard-bits|analytic_guard_bits|
|--c-query-integral-evaluation-limit|integral_evaluation_limit|
|--c-query-value-width-bits|value_width_bits|
|--c-query-integral-max-depth|integral_max_depth|
|--c-query-inverse-max-depth|inverse_max_depth|
|--c-query-max-panels|max_panels|
|--c-query-max-nodes|max_nodes|
|--c-query-budget-seconds|budget_seconds|

fixed view 不虚构这十一项，也不重新求 C。live view 沿原 R426 的同现场 source-piece-index/complete-source-radial-panels、全部1440片、原全根族、真实自然域和原 primitive/query 引擎；本稿不重算 C 的旧累计径向端点或全头总和，不把 fixed cut 盒当可任意收缩的实数名字。

当前没有选择真实新 parent，也没有填未来 eta/budget/precision 数字。实际 caller 只能使用明确授权的工作参数与同 job 的真实 receipt。新 helper 没有覆盖任何原参数的默认值。

## 7. Evidence CLI 与精确 input 字段

新 evidence 提供原三个操作：

    python -u "$COMPUTATIONS/geometry_20261116_coast_fixed_target_complete_metric_evidence.py" \
      measure --input "$ACTUAL_INPUT" --input-sha256 "$ACTUAL_INPUT_SHA"

    python -u "$COMPUTATIONS/geometry_20261116_coast_fixed_target_complete_metric_evidence.py" \
      compare --input "$ACTUAL_SERIES_INPUT" --input-sha256 "$ACTUAL_SERIES_INPUT_SHA"

    python -u "$COMPUTATIONS/geometry_20261116_coast_fixed_target_complete_metric_evidence.py" \
      readback --directory "$ACTUAL_MEASUREMENT" \
      --result-sha256 "$ACTUAL_RESULT_SHA" --out "$FRESH_READBACK"

measure input schema 为 R483-fixed-target-coast-Bernstein-complete-metric-evidence-v1-measure-input-v1。精确顶层键仍为：

    schema, label, namespace, computations, proof_directory, job_deadline,
    first_material_transport, first_plan, first_assembly, field,
    work, c_queries, time_grid, out

job_deadline、first_material_transport、first_plan、first_assembly 与 field 的 cuff_atlas、continuous_e_result 都是原真实 file/bytes/sha256 三字段 descriptor。原 first B 缺失只能使该角色未付，不能制造 B 或阻止其它原精化角色。

field 精确键为 family、directory、result_sha256、checkpoint_directory、cuff_atlas、continuous_e_result；family 只允许本接口已列三值。每份目录、原 C/root、实际 field、target、完整材料与两帽仍由其原 binder实读。

work 精确十一键仍为：

    budget_seconds, free_bytes_reserve, interval_bits, sqrt_bits,
    initial_angular_depth, max_depth, max_cells, measurement_width_goal,
    metric_reference_eta, max_inverse_steps, max_phase_query_cells

c_queries 为 §6 的原十一键。time_grid 精确为 subdivisions 和 witnesses；每个 witness 仍有 kind、coordinate、q、lower。prefix coordinate 是公共 $u$ 的准确有理文字，radial coordinate 是原径向坐标；所有实际 $k=0,\ldots,n$ 和全闭片 membership 仍真执行。没有凭有限时间点宣布全相位成功。

compare input schema 为 R483-fixed-target-coast-Bernstein-complete-metric-evidence-v1-compare-input-v1，键仍为 schema、namespace、measurements、out。members 必须是真实当前源 result descriptor；不能把原 R459/未来 union 的异源 result 改 schema 后混入。

## 8. 读回、未决与清理责任

四 metric 视图保原 closed_metric_summary、closed_metric_summary_bytes、closed_metric_summary_sha256 step outputs。evidence 保原 metric_evidence_summary 及对应 bytes/sha256。实际 frame 已按 §2 全部更新。

新增 actual_prefix_range_work 只列必要计数和最后地址；完整候选范围报告仍在原临时 ledger/原结果路径。没有把它变成大数组新拆包。原 R459 measure 的 necessary_coverage 当前 stack/rank/path/depth/fallback、未退/已退范围与 ledger 身份分界保持原责任；原已退未付叶若仅存 ledger 身份，本文不声称全部原节点正文已回传。Series necessary 仍是原小 series 对象，而非大 field 数据编码。

每次必要 summary 超 90000 B，仍按原路径报真实 bytes/SHA、返回 70；不截断、不拆包、不扩大上限，也不保证未知实际必要正文必然小于上限。完整 result 与科学是否完成、必要读回是否完成分列。

新 source generator 的必要 receipt 本身也单份≤90000 B；过限返回70，明确不授权 raw 清理。所有新件都没有自动 rmtree、kill 或替代外层 quiet。未来 outer 仍须在真实科学阶段结束、全部自身 child 静止、必要原错误/未返范围读回之后才按原规则清理。缺输入、未启动、异常、预算、外部信号与格式超限不能互相冒名。

## 9. 条件证明和来源债务

本稿依 [R481](../results/R481-fixed-ten-semantic-domain-and-complete-coast-polynomial-enclosures.md) 已刊 22205 B /7e1402a14835ead50bfa1fe3157746d0ef0d3323f8047a06577678dbc2d16585，commit 36d5ab6dfba0ff82b1a6ad2667ac541c9d20f2d7。完整 27/16/7 系数包含论证和公共坐标全片覆盖见 R483 正文，字节身份见 publication manifest。

新包不保证区间逐次包含于旧算法的范围、不保证某真实未决由依赖损失造成、不保证速度或内存改善。固定 cut 叶、原累计 C/head 端点、平方根精度与实际 current field 形成误差仍是原问题；只改 coast 多项式求值不会自动解决它们。

当前源码没有在本地执行，后续 Actions 的正常解析与实际科学结果须如实记录。未生成新 field、未复用旧场证书、未迁移 native/J/FD/全DN 接受、未补初点 factory域，未把 scalar solver tolerances 当全域 metric 的误差地板。

## 10. 完整差异与发布映射

当前五视图完整差异分为 fixed.complete.diff、original.complete.diff、resolution.complete.diff、modes.complete.diff、evidence.complete.diff；合并稿 five-consumer-views.complete.diff 为 41195 B /ed8eaf07a8fd10edfc17e9bef7ab26b90cbeb96f7705685f1bdb929f830af519。各差异都从 §2 的正式冻结原基线开始，没有把原审稿或已运行源偷偷改写。

小 helper/generator 是新增文件，其全文即新增差异；plan 明确保存每条 before/after/count 与五个完整输出 SHA，不把科学 raw 数据藏入 source plan。展开 review 源的数学正文除上述实际 target 参数和 range 调用外，保原算法、阈值、时钟和来源加载路径。

发布仅需三小运行件、R483 正文、本接口，共五件；暂存 manifest、完整 diff 和 generated-review-only 供主控逐字核源，不进入 topic 存量。后续 216/R487 入口将另据 214 真 union 三层来源给完整 caller 差异；当前没有为它创建参数、request、workflow 或成功 receipt。
