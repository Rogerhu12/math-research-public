# Request168：同 C 全 112 物理 far 射影传播、有向单位边界及原 native 接线

作者：AI（geometry agent）。日期：2026-11-15。状态：五份独立源码及 R357 证明已冻结；没有本次实际 far 行、零响应、敏感度或审计结论。全部科学只能在 Rogerhu12/math-research-public 的公开 Actions 执行。

本接口保留 actual153 的 C 输入、原物理 far 选择、576-stage 场采样、完整112一般 Robin native 与原请求语义。它将有限 far 传播改为 R347 的完整两坐标射影表示，再按 R357 逐候选形成同一原列的有向单位 Robin 行。旧153和159源码、运行及结果不改写。

## 1. 原实际缺口与本次改变

Actual153 的完整 C/deep 来源已经产出，但其物理 far 传播在频率18到达共享200000 work-unit，最后当前栈和后缀完整保存，native 未启动。该事实见 [R342](../results/R342-actual153-complete-C-and-partial-physical-far-native-unstarted.md)。不能仅提高一个 cap 就宣称已解决完整112问题，也不能将原宽矩形重标为射影列。

本次实际源码改变有三层：

1. 直接调用已冻结 R347 的完整矩阵 Taylor/Duhamel、两 chart 严格 pivot、非零振幅符号及因子链。全部继承误差仍乘完整输入盒。
2. 对每个真实物理 far 的全部闭逆像候选，先形成原 Q/Pi 行，再以严格正范数和振幅符号归一；只有同取向的单位行才跨候选 hull。
3. 对所有已提交/未提交、空间/行范数、数值代表/准确族以及进程/读回状态分别给出真实记录。

没有将物理高度隔零作为 far 行条件。端点 chart 可以除任一个已经严格证明非零的坐标；这里的“无 height division”专指不为构造 far Robin 行求高度商 DN，不应误读为 R347 从不使用第0端点 chart。

## 2. 冻结文件与复用范围

所有运行文件均置于 computations/，正式完整 SHA 如下。

| 文件 | Bytes | SHA256 |
|---|---:|---|
| geometry_20261115_current_C_projective_radial_sampling.py | 60118 | b290dd6030224efc36bfeb30a53e00d76c43c924ae67a0c068e0d23d4d82d8c4 |
| geometry_20261115_current_C_projective_native_worker.mjs | 18206 | c3d5c745f34621fc4817d77377895d3534ad37967da89b2c17ee3faabd6862ed |
| geometry_20261115_current_C_projective_tail_client.py | 23090 | 23824ecbe00d997a0268d0a1438d460f45fa4c4a9de2f05ff6467f0e6f6b5654 |
| geometry_20261115_current_C_projective_native_launch.py | 18218 | ae54abbb383269cbd2fd111c08a103b7eb8a14b15db01d09c2fcc8227488bf9d |
| root_20261115_current_C_projective_native_scalar_readout.py | 33600 | 8a3ddc5d59244b245292bd5a0e3fb33768527017148cc4e697d2f2cf771989e7 |

直接复用原实际完整数学源：

- R347 projective driver：geometry_20261115_stored_C_finite_head_projective.py，77731 B / 5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216。
- R324 原 flux 源4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d，作为 R347 的原公式来源绑定，未修改。
- 原 C v3 f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df、v2 004010b6…、v1 9aa0da45…。
- 原 R312 deep source fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a。
- 原 native owner fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349。
- 原 synchronous bridge 67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286。
- 原 general Robin chain 946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5。
- 其原 R273 factor、原 noJ-matched variational engine、root/RHS/RK、全部 source restore 及 runtime 仍由原完整源码闭包绑定，不换旧 J 或有限尾图。

R347 proof 仍为15106 B / 29f79e1fff0fb872f1ae4920ff4ecbe459ca8aeb84f8dea639dd4bbe42f577f0。新增 [R357](../results/R357-original-C-oriented-unit-Robin-family-enclosures.md) 为12355 B / 286f17eeab74b44716985fd199d5085cde667fb2626a9eb508ef72d35bc29140。采样器分别实际核这两份完整 proof 字节。

worker/client 仅改新的 sampler/worker basename 与 sampler result schema。反向替换这些明确字符串后，逐字等于原153的两个文件。它们保持原 wire protocol schema、geometry array bundle v1、owner、linear child 与实际请求语义。这是兼容的数据布局，不是把旧 producer 身份改成新来源；运行中每个源的完整 SHA、实际 run/source、result SHA 都重新绑定。

## 3. 完整输入与 CLI

sampler 输入仍为同一 job 的真实 C 输出目录和 R312 输出目录。其 result SHA 在实际生成后读取，不预填。F.bind_inputs 保留完整同 C 输入、160×9原片、全部六 primitive、真实 cut 域及 deep/root family 的原条件。

完整 CLI：

    python geometry_20261115_current_C_projective_radial_sampling.py
      --cover-directory ACTUAL_C_DIR
      --cover-result-sha256 ACTUAL_C_RESULT_SHA
      --far-directory ACTUAL_DEEP_DIR
      --far-result-sha256 ACTUAL_DEEP_RESULT_SHA
      --code-directory ACTUAL_COMPUTATIONS
      --proof ACTUAL_R347_MD
      --unit-row-proof ACTUAL_R357_MD
      --precision-bits 256
      --linear-budget-seconds EXPLICIT_LINEAR_SECONDS
      --sampling-budget-seconds EXPLICIT_SAMPLING_SECONDS
      --max-panels EXPLICIT_PANEL_LIMIT
      --free-bytes-reserve EXPLICIT_FREE_RESERVE
      --max-depth 32
      --local-defect-bits 12
      --panel-norm-limit 1/2
      --taylor-terms 24
      --max-geometry-cache-records 65536
      --sample-max-nodes EXPLICIT_SAMPLE_NODES
      --sample-inverse-depth 24
      --sample-value-bits 32
      --steps 12
      --out FRESH_OWNED_SAMPLER_DIR

新增参数只有 unit-row-proof 与 free-bytes-reserve；proof 现在指 R347。源码 max-panels 默认25000000、free reserve默认2147483648，但工作流必须显式列实际选值。最终168 request已显式选择 linear14400s/25M panels、sampling1800s及free reserve2147483648B。它们是本次公开请求的资源计划，不是已经发生的完成结果或完成保证；实际启动裁剪见§12。

sampling 与 linear 使用两个独立 phase 计数器。同一次 far 点的初始逆像采样时间继续计入 sampling；传播期间该时钟暂停，之后恢复，不能重新把初始采样时间清零。两者实际结束时冻结 elapsed receipt，避免把后来的数值采样计入已结束 linear phase。原绑定/runtime setup 位于这些 phase clock 之外，必须由工作流的实际 step/job 硬限覆盖。

每次可用检查至多隔1秒或256个 check 观察自有 out 所在文件系统；低于声明 free reserve 时记录实际容量并作 WorkStop。记录原栈/后缀及 last-paid；不等到一般 OSError 后才宣称账完整。若 OS 异常本身使写出失败，仍只能由原错误流和已完成文件说明范围，不能保证任何基础设施故障都可完整恢复。

## 4. 明确物理 far 与原采样表达不变

choose_far_radius 沿原153真实源码：选择 cell8 / segment8 对应原完整 source piece 的右端半径盒，再取严格大于其上界的最小适用 binary64 后继字词，并核它严格位于真实 cut 以内。

它不是把不确定 C node 半径重标为一个准确字词。实际选择、原 source panel、全 radius box、binary word、cut word 和 family domain 条件仍全部写出。此次没有预填 actual153 的0.05056158669090205；新 run 须从其真实完整输入求得自己的值。

原 InverseSampler、numerical_representative、radial_grid、choose_far_radius、finite_point_required、raw_array 等12个原定义逐文本保持。原全576 outward affine stage、577 nodes、全部 RK4 参数字词、audit节点、x+h舍入可能越名义端点时的真实物理采样检查都保留。没有 clip、复用旧图/gain或只采每 stage 一个代表点。

far 的数值 $\mu$ 现在在传播前用完全相同的原表达

    exp(7*log(actual_rFar) + actual_far_sample.numeric_logw)

形成，以便在每个候选上直接形成原 Q/Pi 行。后续原577节点循环照旧计算；必须与其末节点 $\mu$ 原字词逐位相同。没有由精确区间中点偷偷定义另一套动量坐标。

## 5. 射影传播与单位行

本次直接调用冻结 R347 的 initial_column、advance_candidate、state_record、candidate_record、GeometryCache 及 pending_description。新的 point_column 只将终点责任接到显式物理 far 的完整逆像叶，并以 R357 形成完整边界表示。

对每条候选，源记录：

- 两分量完整 tube、固定 balance 二幂、原实际 panel；
- 非零振幅符号、log区间、因子链 SHA、此前 factor count、pending exact二幂；
- 同一候选的完整正 w；
- 全部 Q/Pi 齐次行系数；
- 为改善量级去掉的同一个正二幂；
- 从完整区间端点求出的准确 squared-norm lower/upper；
- 完整范数球与严格正条件；
- sign(a_f)·R/||R||₂ 的完整两分量区间。

全部候选都合法规范后，才能对同取向单位行逐分量 hull。不能在此之前混合不同振幅的列。若某候选的 norm 下界未隔零且尚可细分，就细分同一个原闭 panel；达到max-depth后保全该候选未付范围，不伪造行。

完整空间传播与完整单位行分别有：

- complete_required_far_propagation；
- complete_unit_row_family_enclosed；
- complete（仅该mode两种责任都已付时true）。

某mode空间完成但行范数仍未付，仍可继续后面的模式；其全部原候选和未付行条件保留。遇实际传播/资源停止则记录当前mode完整未付栈和全部未开始mode。不能把任何部分合法 unit hull 叫作完整 far 行。

## 6. 事务式原账与字段

详细 ledgers 都在独占 out/large-arrays/，原 descriptor 带完整 file/bytes/SHA/rows：

| Ledger | 实际范围 |
|---|---|
| coefficient-boxes | 原完整区间系数和每个原 source panel 来源 |
| sample-inverse-leaves | 全部被实际物理采样使用的闭逆像叶 |
| complete-unpaid-scope | 当前完整栈、所有后缀、表示条件未付 |
| far-accepted-panels | prepared 的完整输入、矩阵/误差、pivot/factor及拟输出 |
| far-complete-tubes | 每个原逆像候选的完整tube/符号/行范数/单位行 |
| far-panel-commits | 哪些 prepared panel/tube span 已成为已付前缀 |
| far-inverse-leaf-coverage | 每个mode、每个原闭叶的实际完整覆盖与行条件 |
| far-all-mode-rows | 每个实际模式的完整状态/计数/last-paid/未付 |
| numeric-point-values-and-errors | 原所有实际stage field的数值字词、准确区间与误差 |

far-accepted-panels 名称沿原路径但其行 schema 明确 prepared，不能仅按其行数冒已接受前缀。只有 far-panel-commits 指出的 span 才已付。

模式摘要包括 complete_step_rows、complete_far_tube_rows、complete_panel_commit_rows、complete_far_leaf_coverage_rows、uncommitted_written_step_span、uncommitted_written_far_span、uncommitted_transaction、last_unaccepted_candidate、complete_current_factorized_state、complete_pending_scope。全部 root/factor依赖保留，原 QF=1 巨大矩形列不物化。

顶层 result.json 新 schema：

    current-C-projective-physical-radial-samples-and-general-far-v1

保 source_sha256、run_id/source_commit、原 input_binding、original scope、actual_R347_proof、actual_R357_proof，并另列 complete_factorized_far_modes、complete_unit_far_row_modes、两个实际 phase resource receipts。error=null 也不能独自解释为完整；必须看 completed/native_geometry_ready 和完整模式范围。

## 7. 数值矩阵与原 geometry bundle

全部112 mode的 unit row family 均已付后，才形成 actual-general-far-row-intervals-and-representatives.json。每mode的原两系数区间、两个实际代表字词、准确区间减代表误差、所有候选spans、范数/振幅条件都保留。

原 112×224 far_matrix 仍每行只在 Q_i 与 Pi_i 两列有系数。由逐mode原序构造，其他所有分量仍为原完整0，不删模态。不重新引入 node graph 或高度 DN。

geometry.json 的 schema 仍是 current-C-native-radial-geometry-bundle-v1，数组结构完全相同：

- node_radii：[577]；
- node_mu：[577]；
- field_geometry：[576,完整field数,5]，列 x/r/drdx/logw/dlogwdx；
- far_matrix：[112,224]。

numeric_geometry_identity 和 far_identity 明确绑定新的 sampler、实际 R347 source、完整 unit-row 源 JSON、原 C 输入与所有数组 SHA。原 R324 源继续记为真实4531；不把新5440值填进旧公式来源字段。

单位行等价于同一个准确齐次边界，但数值行的缩放与旧153不同，阻尼方向的残差权重及浮点轨迹可能变化。本次不声称旧方向、旧norm或旧finite output逐字不变。实际 owner、QR、全部112敏感度和审计会一致消费同一新矩阵。

对准确 C 的统一根族包围与数值边界矩阵仍是不同对象。exact_global_C_realization_of_numeric_representatives_certified=false、exact_global_same_C_and_infinite_nonlinear_DN_not_certified=true 保留；没有为数字代表选择一个共同全局根族。

## 8. 原 native 接线和真实请求范围

新 worker/client 只适配 producer 身份，原 owner/bridge/chain数学字节不动。维数仍 M=112、K=224、depth576、nodes577、rawNode=[0,72,...,576]；原32iterations、10试探、strict original noJ norm下降、2e-9容差、eta1 correction、eta0全112 RHS与两个mean、338响应及fresh audit责任保持。

launcher CLI仍原：

    python geometry_20261115_current_C_projective_native_launch.py
      --geometry-directory ACTUAL_SAMPLER_DIR
      --geometry-result-sha256 ACTUAL_RESULT_SHA
      --recipe EXPLICIT_CURRENT_RECIPE
      --recipe-sha256 ACTUAL_RECIPE_SHA
      --computations ACTUAL_COMPUTATIONS
      --source-topic ACTUAL_RESTORED_SOURCE_TOPIC
      --out FRESH_NATIVE_OUT

recipe protocol仍 current-C-complete112-native-execution-recipe-v1，但 source_sha256 中 SAMPLER/WORKER/CLIENT/LAUNCHER/READER 改为本次新basename和完整SHA，加入实际5440依赖；旧原源码继续在恢复树/闭包里作真实来源。

最终168 recipe选择与153相同的明确新全112 +0H实验，全部112字词、空负零sidecar、原height SHA、jacobian/audit请求和一次protocol call均原样保留。本文不生成某个尚不存在的非零H或accepted anchor。实际完整current-profile/BVP产生的新H须后继真正调用这个live client，不复用旧zero J。

## 9. 外部中断和 owned child

独立新launcher同时修复原153的信号所有权缺口。原client另开session/PGID；如果规则runner只停止launcher组，不能任由该自有client组逃逸。

本源复用已发表159的 live_group、signal_owned_group、stop_owned_group 三个helper原文本：

- 捕获SIGTERM/SIGINT，先保原信号号/名称/elapsed和external_interruption；
- handler不抛异常，覆盖Popen返回与process变量赋值之间的ownership空隙；
- 若已拿到自有PGID，立即转发TERM；
- 正常控制流停止自有组并确认实际quiescence；外部中断用2秒TERM、2秒KILL、1秒join的显式快速范围；
- 原墙钟资源停止与external interruption分别记录，不叫数学拒绝；
- 全部stdout/stderr路径与字节identity保留，原reader再完整分段输出；
- 原组未能确认静止时，completed=false，cleanup不得删除仍可能写入的数据。

无原迭代数、试步数、阈值或数学返回被信号逻辑更改。

## 10. 完整读回与清理条件

新reader CLI仍：

    python root_20261115_current_C_projective_native_scalar_readout.py
      --sampler-directory ACTUAL_SAMPLER_DIR
      --sampler-result-sha256 ACTUAL_RESULT_SHA
      --launch-directory ACTUAL_NATIVE_OUT
      --out FRESH_READBACK_OUT

原15个通用读函数逐文本不变，包括完整12000B字节分段、JSON坏文件/尾行保存、语义大对象拆分、原native trial/trace/linear child读回。没有在本地或reader中计算norm、ODE、方向、interval或矩阵。

新的完整读取责任：

1. far-all-mode-rows：每一行完整输出，保全实际端点factorized state、所有候选/未付计数。
2. far-complete-tubes：每条完整候选，包括真实两个区间、原振幅符号、范数上下界及单位行。
3. far-inverse-leaf-coverage：每个原叶闭区间与完整覆盖责任。
4. complete-unpaid-scope：所有原条目完整输出。
5. actual-general-far-row-intervals-and-representatives.json：存在则全部112原行逐行输出，即使后来field sampling失败。
6. coefficient-boxes、far-accepted-panels、far-panel-commits：流式完整SHA/bytes/物理行数与原declared rows核对，明确没有逐值独立算术审计，且prepared行不自动计为paid。

所有原值保在 stdout 的有名 bounded semantic blocks。超过90000 B时用原完整分成员协议；不截trial/候选、不仅保hash代替整个原小行，也不把所有大块拼为一个巨型JSON上传。大数组/factor不进Git、Release或artifact。

reader输出 schema 为 current-C-projective-native-complete-scalar-readback-v1。GITHUB_OUTPUT键沿原 native_summary/native_summary_bytes/native_summary_sha256，完整index超过界时使用原分段索引。只有不存在读取错误时 exit0，并写 readback-complete.json；否则 exit2且不写complete marker。这个returncode只表示metadata读取范围，不是native或数学接受门。

工作流必须在所有实际scalar读回完成、marker匹配同run/source以及原拥有进程真实quiescent后，才删除本次独占临时根。不能根据单一job/step success或error=null删未读数据。所有错误路径和未启动scope仍应进原日志，然后按原Rule15保脚本、参数、run与SHA。

## 11. 已完成的静态范围

本次实际完成的是小文本源码构造、完整diff、字节SHA和逐文本同一性：

- 12个sampler原定义完全相同；
- worker/client反向明确身份替换后分别逐字同原；
- 15个reader原定义完全相同；
- launcher的三owned-group helpers逐字同已付159；
- owner/bridge/general-QR/原数学运行源未改。

当前终端不可用；没有本地Python AST、Node语法执行或任何scientific import。实际Actions需在科学前对全部新Python源码做compile/AST、对worker做Node语法检查，并核真实来源闭包。此工程前置不是附加数学fixture，不延迟R357条件证明登记。

本接口不预造168 run、source commit、结果SHA、工作量或任何通过结论；以实际主控发布的完整request/workflow为准。

## 12. 最终运行三件与资源事实

下列三件构成此次明确的168运行请求。原153的原始输入、C3600秒、1440片及六primitive、两个闭查询、全112深端频率均保持；新增的是已声明的射影传播及单位取向行，而不是仅改资源后重标旧数值轨迹。

| 路径 | bytes | SHA256 |
|---|---:|---|
| computations/current-C-projective-native-zero112-recipe.json | 7250 | 1e185c333e1345bf977001c4ff363022417d0a43b90ca014b0d0c8050e6627a9 |
| computations/public-current-C-projective-full112-native-request.json | 26217 | d6b87eb9b3d2207171aeb5a11eb5e32c7a422a27030949458a33549ee9583aaa |
| .github/workflows/visible-larger-public-current-C-projective-full112-native.yml | 79848 | c88fed7dfc6827d0c98d965ec41a3aff8c079dae0ada92135cd8d96c6ccaea7a |

工作流的最后一处修正是报告器 NATIVE_SUMMARY 的允许schema改为 current-C-projective-native-complete-scalar-readback-v1，与新reader实际输出一致。五件科学/读取源与recipe/request身份没有随该修正改变。

完整计算源码直接pins为25件；另外原R347/R357证明和全部原出处分别核对。嵌入的标准库owned-process helper为13175B/SHA e8418e10afe0cf519b2d6ea747feb57ffa9dc74f8cd797661b0525a1122d1176，负责原argv、启动资源裁剪、真实PID/start_ticks和自有PGID身份，不运行数学。

资源计划从独占namespace建立时起安排18900秒科学与2700秒读回余量，job的360分钟是平台硬限。原C步75分钟，deep步5分钟，cut读回10分钟，sampling步285分钟，native步75分钟；后续C/far/rules摘要各5分钟、native全scalar读回30分钟，合计45分钟只是预留计划。各步timeout不相加成为另一个保证。

sampling在实际rules-runner启动之后重新观察剩余namespace时间，先预留native声明的3600秒，再以同一个非负比例裁剪linear14400秒和sampling1800秒。原source绑定/runtime setup不在这两个phase计时中，故18900秒在该段是启动资源分配时点，**不是所有科学阶段通用的绝对kill钟**。真正平台硬限仍为该步285分钟及整个job360分钟。裁剪不足时诚实保partial；不降低任何误差、域或接受条件。

native在自己实际rules启动后取原3600秒与namespace正剩余的最小值；若发生裁剪，另写明确仅改process budget的actual-runtime-native-recipe.json，保原recipe和实际recipe两份SHA及变动字段。原每次QR child1800秒、32迭代、10试探、2e-9、eta1/eta0均不改变。一次原明确+0H请求仍要求全J与独立fresh audit，没有用资源计划宣称它已经发生。

32GiB初始容量和2GiB动态reserve均为资源范围，不是数学门，也不保证全部多调用fullDN容量；168本身只有这一个明确protocol请求。资源中断、规则变更或外部信号与数学拒绝分开记账。

清理依赖全部实际读回步骤成功、同run/source的readback marker、父PID/start_ticks及确属新session科学组的真实静止。父Python可能继承runner公共组，不能要求该公共组为空。规则runner临时mirror位于out外；只读rule-sync/owner/resource receipts不会递归打印其clone。无法确认静止或读回失败时保原未读范围，不主动删除，直到runner自身生命周期终止。

未有本次actual run、source commit或结果时不填写它们。本文的源码/资源身份不构成任何已接受native、当前C精确实现、无限DN或闭场证书。
