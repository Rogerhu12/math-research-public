# 当前 C 连续十族真 450 → 完整径向读数与共享闭场接口

**作者：geometry agent（AI）。日期：2026-11-15。状态：独立源码及结构接口；没有填入未来 accepted parent、计划参数或实际几何证书。**

完整数学证明见 [R409](../results/R409-current-continuous-ten450-full-radial-shared-background-and-seam-construction.md)。本文件说明实际 CLI、七元组、来源闭包、临时文件与下游责任。它不复制证明作为额外验收门，也不阻止 193 先按原门完成独立 453→450。

## 1. 两个最终运行文件

| 文件 | bytes | SHA-256 | Git blob |
|---|---:|---|---|
| [geometry_20261115_current_C_ten450_radial_readout.mjs](../computations/geometry_20261115_current_C_ten450_radial_readout.mjs) | 23039 | 5cc3134ed58aed45efea012219aa2e889624c47b41d5ee9f558da231806ab568 | 94d02ecfdd27c31fa4948f1919244167bab4ecde |
| [geometry_20261115_current_C_ten450_shared_field.py](../computations/geometry_20261115_current_C_ten450_shared_field.py) | 48583 | 6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3 | afffa5d69e2ee69c9574300850c5fc6ff42530db |

两个源各自要求 GITHUB_ACTIONS=true 及 GITHUB_REPOSITORY=Rogerhu12/math-research-public。源码读取、文字差异与身份已准备；没有本地 import、AST、编译或科学执行记录。公开 Actions 自己负责相应实际运行及必要结果读回。本文不预填尚未产生的 request/run。

三类顶层 schema 分别为：

- Node：current-C-ten450-complete-radial-Cartesian-readout-v1；
- Python：R409-current-C-ten450-shared-background-complete-field-v1；
- 几何计划：R409-current-C-ten450-shared-field-plan-input-v1。

R400 checkpoint 必须是 R400-current-continuous-ten-complete-physical-DN-checkpoint-v1。它与 finite 185/189 的十族、旧 frozen-nine450 和旧 stored-tail schema 不兼容；不能只换标签。

## 2. 真正的生产顺序与输入边界

唯一可用的上游是同 job 实际连续十族 full453 接受后，冻结其末十词，再运行全新的完整 full450；由原 LiveCheckpointWriter 现场捕获完整末状态、当前 H、真实响应及原门。R409 不提供一个把 453 删三行变成 accepted450 的入口。

新径向入口再使用该 true450 checkpoint 中的最终原生响应，保留全部 577×224 状态、负零、全 338×112 heightJetJacobian、两个均值、原独立 all-stage audit、实际 worker/sampler/runtime/config。原 policy 为 32 次迭代、10 试步、2e-9 容差、sensitivity_eta=0、2048 角点及实际原 steps；接口不另改数值预算。

R409 额外执行 root、RK、FFT 和新字段构造。这是新的科学重放，不是仅原件读取。它没有新的原生 nonlinear solve，也不重新接受原父。构造是否结束不改变上游已发生的原验收结果。

同 job 的当前 geometry 目录必须仍在；Node 的 checkpoint manifest.run_id/source_commit 必须等于本次 GITHUB_RUN_ID/GITHUB_SHA。所有临时输出必须新建在实际 RUNNER_TEMP 之下。以后若需要跨 job 重建，须按原脚本/参数实际重生全部输入，不把本项 same-job 声明改成历史原件仍常驻。

## 3. Node 完整径向入口

命令结构如下；大写符号是未来实际路径或数值占位说明，不是可直接派发的默认参数。

    node --import COMPUTATIONS/exact_20261114_tail_capacity_loader.mjs \
      COMPUTATIONS/geometry_20261115_current_C_ten450_radial_readout.mjs \
      ACTUAL_RADIAL_INPUT_JSON

同一模块也导出 async produce(spec)。spec 的实际字段如下：

| 字段 | 含义 |
|---|---|
| schema | current-C-ten450-complete-radial-Cartesian-readout-v1-input-v1 |
| computations | 此次真实 checkout 的 computations 目录 |
| source_topic | 恢复后的 visible-flexible-closed-surface topic 根，内含原 repro/source-root |
| checkpoint_directory | 真450的 R400 checkpoint 目录 |
| checkpoint_sha256 | 实际 checkpoint.json SHA-256 |
| geometry_directory | 这次最终原生响应实际使用的完整当前 C geometry 目录 |
| out | 尚不存在的本 job 自有 RUNNER_TEMP 子目录 |
| budget_seconds | 显式有限正数，入口开始计时 |
| free_bytes_reserve | 显式非负安全整数，按实际 out 文件系统检查 |

本源不为 future field 选择 steps、cuff、cap_height、W 或任何门值。读取步骤数来自真实 config，全部 576 stage 都使用它。

worker 不硬锁到旧179名字。代码在实际 config.source_sha256 中找到唯一文件名以 _native_worker.mjs 结尾且 SHA 等于 response.checkpoint.source_sha256 的项，再调用其原导出：

    loadGeometry(geometry_directory, geometry_result_sha256,
                 actual_sampler_sha256, original_steps, out)

因此同接口的实际 187/193 worker 可以接入，而旧未匹配 worker 不能凭名称混用。sampler 来源也从当前 geometry result.source_sha256 与 config 完整 source map 唯一绑定。

### 3.1 必需原状态及来源核

读取 final_native、native_configuration 等原 checkpoint 成员时逐 bytes/SHA 核对。恢复负零后要求原 raw_states 为完整 <f8、C order、shape=[577,224]、completed=true，整体及每 node SHA 都一致。全部原 runtime 及 config source_sha256 文件实际核回。

同一 current_target_identity、original_native_binding、final_native receipt 与原 C 输入绑定贯穿结果。几何中的 node_radii、profiles、portRatio、mu 和所有 x 字词直接来自原 loadGeometry，不从静态旧 ready 重建。

### 3.2 完整输出及均值

实际节点数是 576*steps+1。每节点临时 raw 文件 shape=[2048,12]，列名按 result/complete 原字段保存：dx、dy、shape_height、dx_r、dy_r、full_height_r、dx_theta、dy_theta、height_theta、full_height_rr、height_rtheta、height_thetatheta。

重要临时文件：

| 文件 | 内容 |
|---|---|
| result.json | 完整/partial 状态、所有身份、计数与 pending |
| complete.json | 仅全部阶段成功后形成；全部节点描述、两个均值锚与完整源关系 |
| nodes/node-*.f64le.gz | 每节点全部角点十二列原字词 |
| complete-radial-nodes.jsonl | 每个已提交节点的完整描述与原 domain 读数 |
| actual-stage-replay.jsonl | 所有阶段返回、原均值增量、内点 x+h/next-grid 字词关联 |
| loadGeometry 自有记录 | 该实际 geometry 的使用与观测信息 |

原两个均值分别以实际完整增量从内端反向累加。内点使用同一 stage 中的实际均值返回加对应内端锚。反向加法顺序只定义新读数，不承诺逐词等于父 reduction。未回完整均值时不能构造完整新背景。

完整返回保留 new_root_and_RK_scientific_replay=true、geometry_or_metric_acceptance_created=false。completed 只指本径向任务的全部数据返回。

## 4. Python prepare 输入与计划

在实际 Node result 完成后调用：

    python COMPUTATIONS/geometry_20261115_current_C_ten450_shared_field.py prepare \
      --computations COMPUTATIONS \
      --checkpoint-directory ACTUAL_CHECKPOINT_DIRECTORY \
      --checkpoint-sha256 ACTUAL_CHECKPOINT_SHA \
      --radial-directory ACTUAL_RADIAL_DIRECTORY \
      --radial-result-sha256 ACTUAL_RADIAL_RESULT_SHA \
      --plan ACTUAL_PLAN_JSON \
      --plan-sha256 ACTUAL_PLAN_SHA \
      --budget-seconds EXPLICIT_SECONDS \
      --free-bytes-reserve EXPLICIT_BYTES \
      --out FRESH_OWNED_OUTPUT_DIRECTORY

prepare(args) 是同一科学 API。绑定/setup 异常可由 CLI 写入实际 wholly-unpaid result；调用 API 的外层也应保它实际抛出的异常，不能把没有 result 当空成功。

计划只有下列必需结构。实际参数尚未给定；本接口不生成假计划：

| 计划字段 | 要求 |
|---|---|
| schema | R409-current-C-ten450-shared-field-plan-input-v1 |
| checkpoint_sha256 | 同一个真450 checkpoint |
| cuff | 显式有限 binary64 数，严格大于零 |
| cut_correction_width | 显式有限 binary64 正数 W |
| cap_height | 任意显式有限 binary64 高度 H，不要求 H>0 |
| fixed_cap.markers | 完整列表；可为空，但不能默删原已指定 marker |
| markers[].upper | 严格 bool，指定实际帽 |
| markers[].center | 两个有限 binary64 Cartesian 坐标 |
| markers[].radius | 正的有限 binary64 半径 |
| markers[].height | 有限 binary64 bump 高度 |

准确字词检查 $0<cuff<rFar<cut-W<cut$。每个 marker 支撑必须严格在 cuff 圆盘内部；半径与中心平方条件都按字词提升的有理数比较。不是仅检查中心落在帽内。

prepare 不从 plan 信任外部伪造的 ap/app：它由实际 saved.profile 读取这两个字词，写入新 declared_cut_radial_chart_jets。实际原生 cut 半径是 seam 中的 cut；profile 返回半径若有字词差异，写入诊断而不改原目标。ap<0 是该已选 seam 方向的构造条件；由此局部 r(s) 多项式有合法逆，仍不等于准确标量目标导数已经获证。

## 5. Python 科学构造内容与存储

每个完整径向节点形成 shape=[3,1025,3]、dtype=<c16 的全部 coefficient 数据，保 DC、Nyquist、三个坐标和三个径向 jet。水平第二节点数据使用明示的相邻非均匀差分，是新定义数据；不称原 point evaluator 的准确二阶导数。

R249 入口投影只改第一个节点的原三个块；完整 correction witness 与连续差值界重新生成。随后准确共享节点背景、全角 cut 修补、完整 collar 和帽参数都由这些实际输入形成。新的 B、准确原目标、数值渲染分列，R400 未投影 prefix metric 不继承。

临时输出：

| 文件/目录 | 内容 |
|---|---|
| coefficients/node-*.c128le | 每节点完整 binary64 复系数原字词 |
| node-coefficient-identities.jsonl | 所有已提交 coefficient 描述 |
| radial-definition.json | 完整径向节点顺序、全部 coefficient、原重放身份及定义范围 |
| plan.json | 独立 R409 plan、全切口/相位/配准和新 loader guard |
| assembly.json | 全场来源、反射/均值/入口/帽及明确未付几何责任 |
| shared-background.json | 准确有理 B 节点、系数及原差值包围 |
| target-contract.json | 原连续十 DAG 与模型 C 目标，不是 B′ 目标 |
| result.json | 所有文件 bytes/SHA、完整或 partial、source/run/field 关系 |

背景以新 RK 大均值和当前 w/wr 字词为定义数据，加明确 cuff 节点 (H,0,0)。小均值保留在扰动 Fourier 的竖直零模态中；两均值没有合并后丢失责任。完整全角 patch 使用保存的真实 prefix 全338节点，不只匹配 2048 个点。

所有 payload 大小随真实 steps/节点/模式增长。本文不给压缩率或全部内存/磁盘容量承诺。源在显式检查点执行 wall/free-space 判断；外层 Actions 仍须保真实 step/job 上限与进程停止。单次底层调用不被本 source 的 wall check 自动抢占。

## 6. 七元组 load_shared_bundle 的精确协议

guard 路径固定为：

    geometry_20261115_current_C_ten450_shared_field.load_shared_bundle

参数对象包含 computations、directory、result_sha256；可额外给 checkpoint_directory 进行实际路径重定位，内容与 source/target 身份仍严格核回。

返回次序是：

| 位置 | 变量 | 实际含义 |
|---:|---|---|
| 0 | paths | radial/plan/assembly/background/target 的实际文件路径及已核成员 |
| 1 | plan | 独立 R409 plan；完整 phase_rule、所有径向/帽与 guard |
| 2 | assembly | 新完整有限表达、配准、均值、入口投影及未付责任 |
| 3 | target | 新 target-contract 对象；不是旧 stored 几何表 |
| 4 | saved | 已作本次 R249 投影的 ContinuousTenSavedPrefix |
| 5 | A | CurrentSharedAssembly，拥有同一个 saved/tail/B/plan |
| 6 | bindings | 完整 current target、真450、全部源及 payload 关系 |

loader 会重新加载 R400 prefix、执行原 DDY 路径并重复准确入口构造，再核完整 prefix definition 身份。因此它不是单纯文件读回；再次执行也属于 Actions 科学范围。跨环境重建若改变定义字词，不能以“数值近似”放行。它不会调用旧几何 loader 作为备用。

第3项 target 与旧七元组的 table 名称虽然占同一位置，语义不同。675 ExactFiniteField 只把该项保作绑定对象，不用旧表生成新场；其他消费者若实际读取旧表数值，必须显式适配，不得盲用相同 tuple 长度宣称兼容。

bindings 明确没有 supplied mesh/normals，也没有 inherited complete-pair/curvature/metric/held 证书。闭几何 guard 内 legacy_tail_or_B_reconstruction_authorized=false，防止旧 e70d/6b06 回退。

## 7. exact_field API 与实际六 jet

    bundle, field, Active, Background = exact_field(args)

exact_field 先取得上述完整七元组，再使用 pin=675ab8df 的 ExactFiniteField 类，注入 numpy 和 python-flint 的 arb/ctx/fmpq。它不调用该旧脚本 initialise_runtime，也不触发其旧 stored-tail/B binding。

可调用 field.pieces、field.evaluate(piece,radial,angular,lower)、field.expression_identity()。所有参数范围、精度及预算由未来实际消费者明确给出。本接口未默设所需曲率 K、metric eta 或 reach tau。

field.evaluate 的输出为三坐标 Jet2，六个分量按 value/u/q/uu/uq/qq 排列。其角坐标 q 是归一化物理角，phi=2πq；tail 里面另完整复合 Phi(phi)。prefix、full Fourier、B、切口角函数及全部 mixed 项由同一个准确表达求导。下片只按真实整片反射变换。

此675 API只给活动prefix/tail/collar/cut patch及其反射片的六jet。两帽是同plan中独立Cartesian bump准确图面；当前入口没有运行其区间六jet或全帽覆盖，不能由活动片piece列表推帽证书。

每片覆盖端点必须闭合。field.pieces 保留所有 prefix 节点、所有 native/B 节点、cuff/far/cut-patch-start/cut 的联合分割。它没有借 worst≤128 或每坏对4个 child 充当全覆盖。

数值 CurrentSharedAssembly 的 prefix_jets、tail_jets、phase_jets、cap、cap_normals 供明确的 rounded 渲染用途。它们不与 exact_field 的准确式逐词等同；例如记录角 beta 的真实三角函数与拟合矩阵字词可能不同。任何基于 renderer mesh 的误差转移都必须另有界，当前未付。

## 8. 原目标 g 的接口，不允许 B′ 回退

target.complete_current_ten_target 逐字段保同真450目标。前缀在数值 s 坐标上的目标准确系数为 $(L/Lnum)^2$ 与 $a(Ls/Lnum;p10)^2$。tail 仍需原 C 的完整 E(r) 区间生产器覆盖实际 collar 到 cut；两个端点的单盒不能代整个域。

全域相对 metric 仍使用原四 Loewner 条件，保 Gram 的交叉项、完整十控制、共同材料角与全部两阶混合项。当前 source 只提供新 exact field 和目标绑定，不宣称原旧 metric CLI 已认识这个新 guard。

原R400 prefix_metric可提供同目标和完整piece机制，但入口投影后要让消费者明确吃同一新的 saved/field 并重算；不能把其原结果贴在新的几何上。帽内可用固定帽自身诱导目标给零相对误差，cut/cuff目标atlas和所需E域仍要独立完成。

新B不选一个共同准确C根，数值profiles也不等于全根族共同成员。当前C的自然Rout不被平延拓；若所需域超出已付准确范围，保持明确未付。表达构造成功不解除这个对象责任。

## 9. 精确源依赖与运行时闭包

下面列直接固定边。表中 SHA 是代码约束，未来 workflow 应从真实 checkout 按这些版本准备，不能从相近文件名选择。

| 依赖 | SHA-256 |
|---|---|
| geometry_20261115_continuous_ten_frozen450_saved_prefix.py | 1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520 |
| geometry_20261115_continuous_ten_frozen450_checkpoint.py | 43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae |
| geometry_20261115_continuous_ten_same_metric_profile.py | 3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6 |
| geometry_20261114_shared_background_normal_form.py | da4a0b5004ef8466119025d8e39e23ffb0366a5367e6761c8321299aeb19c3f9 |
| geometry_20261114_inlet_parity_normal_form.py | ce5f287c1de870b6bf71d1650d6942e23fd2bdd23a25af72ec5b637599a97410 |
| geometry_20261115_shared_active_interval_balls.py | 675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b |
| geometry_20261114_large_core_saved_prefix.py | 51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0 |
| geometry_20261115_current_C_general_robin_native.mjs | fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349 |
| exact_20261114_tail_capacity_loader.mjs | 07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395 |
| 原 source_topic 内 f6tail_relative_development.mjs | 90878cc529bb842743602547d997922de69c8e8966a9fd08ea8a353be1d1ff6e |

最后一项的准确相对路径为 repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_relative_development.mjs。

这些不是完整 runtime 的替代清单。还必须保：

- R400 SavedPrefix 的完整 ORIGINAL_SOURCES、其 checked_sources 的 checkpoint/profile/kernel 边；
- R400 profile 内的连续十 factory72c4635e、numeric7dedb713、augmented a248e957，以及原完整物理 ODE、boundary、same-C binding 的固定边；
- R400 checkpoint 的原 full_dn_solve c6a1、full_dn_augmented f76b、physical boundary3975、cut audit7a54和真实 source closure；
- 真 final_native 配置的全部 config.source_sha256 与 original_runtime_sha256，实际 worker/sampler 也在其中；
- 背景/投影纯数学模块在正常 import 路径中的原源闭包。

Node 会按真实配置完整逐文件核源；Python 新源核自己的 SOURCE_PINS 并继续调用上述原严格加载器。已有193完整闭包应在同job保持，无须把历史科学重新当新门跑一次。依赖身份相同不等于科学成功。

## 10. 完整与 partial、外部信号和清理

Node partial 有 actual_nodes/total_nodes、completed_stages/current_stage/current_step、全部 uncreated_node_indices、未提交 stage 范围、两均值和完整新场未付标记；同存实际 root/RK 次数与错误文本。它不会把未返回数组补零。

Python partial 有 coefficient_records_completed、实际已写ledger身份、uncommitted_coefficient_suffix和完整闭表达未付。若信号在特殊底层调用中延迟返回，必须由外层记录实际终止；不是任意单调用都被即时抢占。

两个入口都区分 ResourceStop、ExternalStop 与其它真实异常。deadline/disk不足只表示任务 partial，不推原场失败。输入不匹配或构造条件未付也不会修改原 BVP 的接受记录。

各自 CLI 完成通常返0，明确 partial 返2；Node绑定fatal可返1，Python setup异常保现场后仍异常退出。直接API的调用者不得只看有无文件：须按真正completed及所有pending/error读回。

源码自身不删除输入或原始输出，也不上传artifact。外层只有在必要结果完整读取、来源范围明确、自有科学进程已止之后才清理自有临时目录。未读完整部分继续保未付，不能“清理完成”冒“完整科学结论”。

## 11. 必要小摘要与不应回传的大对象

当前没有新workflow/reader被伪造为已执行。以后同job可直接读取必要小scalar摘要：

- 实际checkpoint/run/source/target/worker/sampler/full closure身份；
- Node完成/partial、全部阶段/节点计数、错误与准确未付范围；
- Python完成/partial、完整coeff/B节点计数、定义和payload身份；
- 实际R249差值界的必要极值及其作用域、切口字词差异、完整目标未付标志；
- 新表达来源/guard与任何真正已运行的后继消费者结论。

单份必要读回仍遵原90KB约束。不得把全部2048×12节点、多MB plan/definition、全部系数或六jet树编码分包给工具再拼回；大原件只在Actions临时域完整处理，摘要给身份及诚实未逐值工具审计范围。本文不省略source所保存的大原件，也不承诺未来所有错误文档都自然适配单份容量。

## 12. 193 与后继消费者接点

193应先独立完成实际连续十族453→同参数450及原末门。若成功，保同job：

- 真checkpoint目录与checkpoint.json SHA；
- 实际current geometry目录、最终native配置和原完整source闭包；
- computations与source_topic实际目录；
- 运行namespace、真实remaining资源和进程所有权。

然后可明确创建本Node spec，实际运行径向重放；其完成后再创建明确的新几何plan并调用prepare。plan的cuff/宽度/帽参数必须来自随后真实选择，本文不代填。

如果当前193只保下游槽而未调用这两个源，报告就只能说槽已接、R409未运行。即使本构造全部返回，也只能说同数据的新精确有限闭场已定义。完整metric、正则性、连续曲率、全部空间—相位pair、reach、held及原README最终范围仍按实际结果推进，不能把本构造完成当任务完成。
