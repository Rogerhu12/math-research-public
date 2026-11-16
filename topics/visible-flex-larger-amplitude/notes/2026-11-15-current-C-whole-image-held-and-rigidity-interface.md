# 当前准确 C 十参数闭场：整面 held 与含反射刚性输入接口

**作者：geometry agent（AI），2026-11-15。状态：源码与完整条件证明，未执行。没有实际 accepted 450、实际 witness 计划、资源运行或几何成功。**

## 1. 文件、已有边界与唯一对象

本接口对应 [R425 完整证明](../results/R425-current-C-whole-image-held-and-reflection-rigidity-inputs.md) 与独立运行源：

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| [geometry_20261115_current_C_ten_held_and_rigidity_inputs.py](../computations/geometry_20261115_current_C_ten_held_and_rigidity_inputs.py) | 53711 | `c87b3a9b9d17f74d8c4f4066f65318e50fed5a56143f620628049a86dcf77ef2` |
| [R425-current-C-whole-image-held-and-reflection-rigidity-inputs.md](../results/R425-current-C-whole-image-held-and-reflection-rigidity-inputs.md) | 22444 | `26adc968486cc29ca752da3fd2257ff4dbd4320cf0f6cc9f73f611ab3d981a1b` |

拟发表位置分别为本 topic 的 `computations/`、`results/` 及本 `notes/`。完整差异和静态文本身份回执只留临时工作目录，不作为数据提交。没有改动 R409/R413/R416/R417/R418/R422 或正在运行的科学入口。

源 schema 是 `R425-current-C-ten450-whole-image-held-and-planar-germ-inputs-v1`。其对象只有：真实同场 R409 七元组来源所定义的 R416 准确 cut 场，加上同一 R413 原 cuff、R417 完整两帽。它不把原七元组里的数值 renderer 当作 R416 修补后的准确场，不使用旧 finite 背景构造器，不将原 RK 数值轨迹冒成准确 C。

R425 完成的是消费者来源桥。它既不生成新的 accepted 450，也不在原 full453/full450 的验收链上增加 held、planarity、marker 或 reach 前门。没有实际场时不能通过源码、SHA、schema 或空计划补造输入。

## 2. 七项直接源绑定和原传递依赖

源码先按原文件全部字节核对以下七个直接源。它们的依赖闭包仍由各原入口按其原合同读取，不把“七项直接源”误称为全部 runtime 只有七个文件。

| 准确 basename | SHA-256 |
|---|---|
| `geometry_20261115_current_C_accurate_cut_patch.py` | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` |
| `geometry_20261115_current_C_original_cuff_target_atlas.py` | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` |
| `geometry_20261115_current_C_ten450_fixed_cap_balls.py` | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` |
| `geometry_20261115_shared_active_interval_balls.py` | `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` |
| `geometry_20261114_prefix_exact_nonplanarity.py` | `a40dc7a50d90694006342ec964f18fac90bb2743ad622e1b715d920d376c1aa6` |
| `root_mixed_phase_normal_balls.py` | `ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6` |
| `geometry_20261115_shared_curvature_diameter_budget.py` | `b1c2dfb9bd99c0777805da938c38e428da32db8ed5fa6238c9433ed9aede5ad0` |

实际调用点如下。

| 原文件/函数 | 新入口使用的确切范围 |
|---|---|
| R416 `load_accurate_cut_field(args)` | 完整当前场、十族准确 target、C/DAG、原七元组来源和准确 patch；保原 450/checkpoint/proof/source 身份 |
| R413 `bound_json`、`bind_loaded_shared_bundle` | 原 cuff atlas 文件全部字节及实际字段；不改 cuff，不用自然 outer 充 flat cuff |
| R417 `bind_loaded_shared_bundle`、`CurrentTenFixedCaps.cell` | 全 marker、两侧图、闭圆盘、Cartesian 位置和原临时六 jet 记录 |
| 实际 `current.Active.vector_ball` | R416 当前值区间的球包含；核真实模块路径和 675 源 SHA，不调用旧初始化器 |
| R254 `NodeAngles.at`、`hermite_position`、`AffineWitness` | 完整当前共享节点上的准确有理前缀证明；不调用旧 `certify_prefix` 文件入口 |
| 原 kernel `sqrt_upper` | 准确有理平方根上界；新 `sqrt_lower` 用 $x/U$ 导出下界 |
| `ImageBounds` | 仅完整当前位置球/盒的 $D$ 汇总；不调用旧 curvature binder、旧 marker layout 或旧 reach 状态 |

R417 使用的是实际对象 `type(A).__module__` 的原 owner 检查，沿最终 `0ff1fa60…` 修订；不是 `sys.modules` 中第一个同路径类。R425 不重新引入旧的类身份歧义。

python-flint 与原解释器 runtime 仍须由未来公开 Actions 的原依赖环境提供。此入口设置实际 `interval_bits`，结束后恢复原 `ctx.prec`；没有在本地 import 来假装 API 已执行。

## 3. 必须来自真实同场的文件

### 3.1 原 R409 当前输出

`--directory` 是原当前 R409 shared-field 目录，`--result-sha256` 是该目录原 `result.json` 的全部字节 SHA。R416 原 loader 接管该结果的原来源、节点、B、全部尾和 checkpoint 读取。可用原 `--checkpoint-directory`、`--proof-directory` 指明真实恢复位置；这些参数不改变原身份合同。

仍需真实完整 453 接受后固定实际末十词，再独立完整 450 的原 checkpoint。不得删去 453 三行生成假 450；不得借 finite-Gauss 185/189 的参数或结果重标为连续 C；不得只拿摘要或 SHA 补造已清理的原数组。R409 的原节点投影及新准确有限对象也不被重新称为原 native 接受轨迹。

### 3.2 R413 cuff atlas

`--cuff-atlas` 和 `--cuff-atlas-sha256` 给出实际原 atlas JSON 及全部字节。R413 按其原 schema 检查它与七元组中当前 C `rCuff`、plan、marker、背景和 target 的关系。R425 没有新增 $E=1+B'^2$ 目标，没有把 cut 三盒当作 whole-tail 度量，也没有借旧标签为任何域外环带付费。

### 3.3 当前 quarter-turn 见证计划

小计划必须全部不超过 90000 B，具有准确 key 集：

```json
{
  "schema": "R425-current-accurate-active-quarter-turn-witness-plan-v1",
  "points": [
    {
      "piece_index": "实际整数，不能使用此占位字符串",
      "radial": "实际准确有理字符串",
      "q": "实际准确有理字符串，位于 [0,1]",
      "lower": "实际布尔值，不能使用此占位字符串"
    }
  ]
}
```

上面只是字段说明，**不是可运行计划或未来点选择**。`points` 须非空；实际 `piece_index` 必须是 Python JSON 整数，`lower` 必须是 JSON 布尔。每行恰四个字段，径向点在该实际 piece 的闭区间中，`q` 是归一化物理角。源码保整个实际 row，不以默认值补缺 key。

`--witness-plan-sha256` 绑定全部原字节。见证只对当前准确点作精确四分之一周旋转，记录其位于 $F_1(M)$ 的 R248 材料逆运输依据；不主张物理 `q` 只需平移，也不将材料点位移当作 Hausdorff 距离。

## 4. 原片全集、实际运算和数学来源

`PositionCover.root` 懒生成全部 $2P\,4^d$ 活动根及两个完整帽根，$P=\operatorname{len}(current.field.pieces)$，`d=active_depth`。每个活动根有 `lower/piece_index/radial/angular/path/depth/root`；每个帽根有 `upper/path/depth/root`。两种反射、全部原尾/B/cut 端点、collar 和完整角圆均在真实 piece 表中。

位置覆盖采用闭 DFS。活动二分交替径向/角向，帽沿 `0,1,2,3` 四叉路径。帽相切边界不省。最大深度达到时，仍可保存完整合法包含球；`all_requested_work_resolution_met=false` 不把已覆盖区域变成未付几何域。只有仍有未访问根或前沿才使全像覆盖未完成。

每个见证对每个终端位置球的下界完整进入临时 ledger。全格访问后对每见证取最小、再对所有见证取最大。`ImageBounds` 同时汇总整个带 marker 的 $F_0$。任何 partial 的“已访问子集最小值”都不升级成全像下界或完整 $D$。

`PrefixProof` 在原每个真实前缀单元使用全 `3M+2`、$z_0$、原共享节点 Hermite 和完整 R254 网。每次最多只在找到严格非共面四点后提前结束该单元；这时已有充分证明。没有找到时完整候选网仍全部走完，才能报告准确平面单元。预算中断不会等价为准确平面。

`TailProof` 读取当前全部 `tail_coefficients`，保 DC/Nyquist、三坐标和各阶数据；按 `(tail_span, cut_patch)` 组合连续原多项式域，保所有实际子片索引。准确同半径差只消去共同 B 及对应 cut 常数差。patch 中使用当前 R416 的 `target_first_multiplier`、`target_second_multiplier`、`target_first_in_second_multiplier`，保同一 C 根族的完整区间；不用旧数值 `ap/app`、新根中点或重建旧 finite 尾。

十七个原 radial fractions 均在实际闭组内。每个尝试记录 exact radius、运算类型、非零判断和原差矩阵/行列式。未 patched 的准确零与 patched 含零区间分开。任何一个严格非零见证才覆盖该多项式组的所有实际 B 细分；否则完整组责任仍未付。此路线不以一个 cardinal 行列式恒零推出曲面平面。

## 5. 可执行 CLI：全部资源由实际请求显式提供

入口是 `main(argv=None)`，程序 API 是 `produce(args)`。没有本接口指定的新 request 或默认科学阈值。未来同 job 原 raw 清理前可调用：

```sh
python COMPUTATIONS/geometry_20261115_current_C_ten_held_and_rigidity_inputs.py \
  --computations COMPUTATIONS \
  --directory ACTUAL_R409_DIRECTORY \
  --result-sha256 ACTUAL_R409_RESULT_SHA256 \
  --checkpoint-directory ACTUAL_450_CHECKPOINT_DIRECTORY \
  --proof-directory ACTUAL_PROOF_DIRECTORY \
  --cuff-atlas ACTUAL_R413_ATLAS_JSON \
  --cuff-atlas-sha256 ACTUAL_R413_ATLAS_SHA256 \
  --witness-plan ACTUAL_SMALL_PARAMETER_PLAN \
  --witness-plan-sha256 ACTUAL_PLAN_SHA256 \
  --active-depth EXPLICIT_NONNEGATIVE_INTEGER \
  --position-max-depth EXPLICIT_NONNEGATIVE_INTEGER \
  --position-radius-goal EXPLICIT_POSITIVE_RATIONAL \
  --interval-bits EXPLICIT_INTEGER \
  --sqrt-bits EXPLICIT_INTEGER \
  --max-position-cells EXPLICIT_POSITIVE_INTEGER \
  --max-prefix-points EXPLICIT_POSITIVE_INTEGER \
  --max-tail-witnesses EXPLICIT_POSITIVE_INTEGER \
  --budget-seconds EXPLICIT_POSITIVE_SECONDS \
  --free-bytes-reserve EXPLICIT_NONNEGATIVE_BYTES \
  --out NEW_OWNED_OUTPUT
```

所有大写项是必须替换的实际参数占位，不能从本接口拼造 accepted 输入。两个目录覆盖参数在原 loader 能自行定位时可省，其余 `required=True` 参数必须给出。`--free-bytes-reserve` 的唯一默认值为 `2147483648`，资源计划也可显式覆盖。

`--out` 必须是尚不存在的 owned 目录；`temporary_output` 先解析实际符号链接和路径，要求它严格位于已存在的 `RUNNER_TEMP` 下，不能等于该根，也不能包含实际 `computations/directory/witness_plan/cuff_atlas/checkpoint_directory/proof_directory` 或本定义源码。调用方仍须只给自己的临时根。路径/参数检查发生在目录创建和 `Budget` 前；这种工程输入错误可只有原 stderr，不预造科学失败或完整 result。

原参数校验：`0 <= active_depth <= 30`、`position_max_depth >= 0`、`64 <= interval_bits <= 8192`、`16 <= sqrt_bits <= 4096`；位置目标准确为正，三个工作上限正，墙钟有限正，保留磁盘非负。位置目标不是 error/refinement/BVP 接受容差。

`Budget` 在 fresh owned 输出目录创建后、全部源/数据绑定之前启动，`producer_elapsed_seconds` 包括绑定与 setup。检查发生在所列工作边界；单次解释器或整数操作不被强行中断，所以它不是绝对硬杀钟。未来 workflow 须诚实披露其原 step/job 硬限，而不能从本字段推断无条件读回余量。

SIGTERM/SIGINT 只登记信号，由下个安全边界形成 `Stop`，以保当前事务和原数据；这不承诺外部 SIGKILL 后仍可写回。磁盘检查作用于实际 owned 输出所在文件系统。R425 不新生原生 BVP、不加入 solver call 门、不改变原 parent 验收或已接受 tau。

## 6. 临时输出全集与可读语义

所有文件 exclusive create；JSON 为准确有理字符串的规范单行 JSON 加 LF。原数据文件或 proof/source 文件不被重写。流账为 gzip JSONL，每行有完整 ordinal，并记录 decoded bytes/SHA 和压缩文件 bytes/SHA。

| 相对输出 | 实际内容与范围 |
|---|---|
| `input-binding.json` | 当前 R416 完整 binding、原 R409 result、R413 atlas/attachment、R417 原全帽、实际 target 身份、七直接源和所有资源 |
| `actual-complete-marker-conditions.json` | 全 marker 的实际有理参数、支撑圆心、同帽分离、完整四点 determinant 和原 R238 条件 |
| `actual-accurate-quarter-turn-points.json` | 计划中每个真实点的原参数、位置盒/球和准确旋转球 |
| `large-arrays/complete-current-piece-universe.json` | 完整原 piece 表、两反射/两帽声明及当前 witness 身份 |
| `large-arrays/complete-current-position-cover.jsonl.gz` | 每次完整闭 split、严格盘外排除、终端值包围和每个实际 witness 的距离下界 |
| `whole-image-position-result.json` | 覆盖/工作状态、所有 witness 子集最小值、全覆盖后实际 held/D/H 比例和未访全集 |
| `large-arrays/complete-current-prefix-nonplanarity.jsonl.gz` | 每个已完成原前缀单元、完整准确四点/basis、实际参数和分类 |
| `large-arrays/complete-prefix-proof-result.json` | 完整网、全部已完成单元和当前 basis/candidate/单元后缀 |
| `large-arrays/complete-current-tail-nonplanarity.jsonl.gz` | 每个原实际 radial 尝试及完整差矩阵、严格区间或准确有理值、完成组记录 |
| `large-arrays/complete-tail-proof-result.json` | 全组/所有原 piece 映射、所有尝试及当前/未访组责任 |
| `large-arrays/actual-current-C-cut-differences.json` | 只有实际 patched 尝试需要并产生时才存在；全 nodal cut 差、实际 SE2、当前 C 乘子及完整 0、1、2 阶差盒 |
| `large-arrays/actual-used-complete-field-identity.json` | 实际用到的当前准确场表达与来源；无额外求解 |
| `result.json` | 完整原本项结果与原文件身份；可大于回传限，仅临时 |
| `necessary-summary.json` | 单份必要摘要，正常时不超过 90000 B |
| `necessary-readback-over-budget.json` | 只在必要摘要超限时记录原 attempted bytes/SHA、完整结果身份及读回未完成 |

错误发生在输入绑定阶段时，尚未实际形成的文件不会伪造。所有原 SHA 只是已读来源或输出身份，不代表工具已经逐值复核临时大矩阵。R425 不实现这些大文件的上传、分片回传、Git/Release 保存或无条件删除。

## 7. 关键结果字段及停止范围

`position` 中保原完整 `whole_marked_F0_D`、`fixed_hold`、`per_witness_visited_subset_distance_lower` 和 limiting domain。仅全像覆盖完成才给 `delta_hold_lower`、完整 `D` 和两项实际比值。判定键 `README_held_fraction_paid`、`README_fixed_H_fraction_paid` 正是原 $1/5$ 充分比较，不改更强/更弱课题标准。

`prefix` 区分完整搜索、准确非平面已付单元、准确平面单元和资源未访。`tail` 区分完整组、成功非零 witness、准确 cardinal 多项式恒零、固定 C 区间含零及未访。正常必要摘要不搬整网或大 determinant witness，但全部原件身份、已付数、原 planar indices、当前 candidate 和完整后缀保持。

这里不能按少量 shooting 端点估计尾组体量：原 R409 `geometry_20261115_current_C_ten450_radial_readout.mjs` 明确保留 `576*config.steps+1` 个节点；Shared 原 loader 核此完整数量，675 `make_pieces` 按全部径向节点/背景分点/cut 边界形成闭片，`TailProof` 再按 `(tail_span,cut_patch)` 合并同一个多项式。它可有数千个完整成功组。因此本必要摘要不逐个复制成功组的完整 `group/actual_piece_indices/successful_attempt`。

新的 `compact_tail` 只在必要读回层采用以下范围，原 `report()`、所有科学计算、临时完整结果和 ledger 一字不变：

- `successful_group_indices_half_open_ranges` 完整表示全部成功组索引；`successful_group_count/successful_original_radial_piece_count` 保实际总数。
- `successful_candidate_index_counts/successful_arithmetic_counts/successful_strict_sign_counts` 保成功见证的实际序号、运算类型和严格符号分布；`completed_attempt_count` 含所有已完成组的全部尝试数。
- `completed_unproved_groups` 逐个保留所有已完成未证明组的原对象，包括完整 group、每个实际子片地址、全部原 attempts、准确恒零标志及原失败语义。它们没有被成功计数替代。
- `pending` 原字段全部保留，并增加 `current_group_definition`，给出当前组实际左右端点、tail_span、patch 和完整子片列表。候选游标/已返尝试/候选后缀与完整未访 group 后缀均保留。
- `complete_group_definitions_identity/complete_original_group_status_identity` 是原完整对象的 canonical bytes/SHA；同时保完整原文件及 ledger 身份。成功组逐个数值 witness、长子片表只在这些临时原件，未作为工具已取正文冒称逐值核验。

半开区间只是实际连续索引集合的摘要，不编码矩阵或原大 JSON。极端失败组、当前组或其它必要数据仍可超过限额；此时保原退出 70，不承诺必然小于 90KB，不截失败/未访范围来凑大小。

核心组合键是：

- `complete_current_active_nonplanarity_proved`：完整前缀与全部 tail/collar/patch 组都已由本入口证明。
- `same_field_R238_marker_conditions_paid`：原四 marker 充分条件在当前全列表上准确成立。
- `same_field_whole_continuous_image_change_proved`：完整全像下界严格正。
- `all_R238_hypotheses_except_global_embedding_paid` 与 `conditional_Euclidean_quotient_distance_strictly_positive_if_same_field_embedding`：上三项齐，且始终按 R409/R416 原结构定义理解；它们不是实际全局嵌入或无条件 $\delta_E$ 证书。

以下字段仍固定 false：实际全局闭嵌入、实际 $\delta_E$、实际 reach/metric/same-$g$ 精化、原 RK 到准确新场的误差、任务完成。`quantitative_delta_E_lower_not_computed=true`。不能据此组件返回 0 宣布课题通过。

`error` 是实际 Exception；`resource_stop` 是明确资源/外部信号 Stop；`resource_partial` 不冒准确几何失败。完整停止地址包括：

1. position 的 current root、完整闭 DFS frontier、半开未访 root suffix；
2. prefix 的 current cell、next candidate、当前完整 basis 原件身份、候选 suffix 和 cell suffix；
3. tail 的 current group、candidate、已返回尝试和完整 group suffix；
4. 尚未开始的完整 binding/positions/prefix/tail 标记。

在每个逻辑工作开始前递增的实际工作计数包含最终失败或中断的尝试；不能把它直接等同成功终端数或已付 witness 数。原账分别记录 completed/terminal。

## 8. 单份必要读回、退出和清理边界

stdout 使用唯一块：

```text
BEGIN_R425_CURRENT_C_HELD_RIGIDITY_SUMMARY
<single necessary JSON with LF>
END_R425_CURRENT_C_HELD_RIGIDITY_SUMMARY
```

正常摘要文件全部 bytes/SHA 对应 GITHUB_OUTPUT 三个键：`current_held_summary`、`current_held_summary_bytes`、`current_held_summary_sha256`。它们不是大数组下载入口。若必要摘要本身超过 90000 B，原结果仍完整写在临时目录；只输出小 fallback，退出 70，不截断必要地址，不传编码块、不创建额外 artifact。成功组的范围/分布摘要消除了已定位的重复元数据，不是任意输入体量的保证。

正常完成或诚实资源 partial 返回 0；内部错误返回 1；实际已登记并读回的 SIGINT/SIGTERM 返回 `128+signal`；摘要超限优先返回 70。这些退出值用于工程读回，不是数学验收。不能用 job success 推断所有数学条件 true。

R425 本身不删除临时原件。未来同 job 编排必须在实际子进程停止、必要结果读回完成之后，按原 owned-directory 范围清理。若摘要超限、读回失败、进程仍活动或外部硬中断，不能称原大见证已返回完整。根规则要求可重算大数据仅临时保留，不能用分包方式绕过。

## 9. 与原消费者的真实差异

原 `geometry_20261114_shared_background_held_hausdorff.py` 包装旧 shared loader。新源不保留该旧 loader 路径：它从 R416 获取新的准确 patch 表达，再从 R413/R417 核同一原 C cuff/帽；整个 position cover 独立于旧 normal-ball/reach 包或 R418 成功。

前缀直接复用已证 R254 纯函数。尾部只复用 R258/R274 的完整数学结构，显式增加当前 C 实系数 cut 差适配，避免旧 `prefix_cut_terms` 的数值 `ap/app`。固定帽和 `D` 只用已发纯函数/同场字段，不另造新数学条件或再做一次旧 theorem fixture。

新源的 full diff 相对原 shared-held 源保留在临时工作目录，便于来源核阅；不以 diff 代替完整当前源，不把自动源比较当新的接受门。本次没有发布 request、workflow、未来 450/阈值或数值结果。

## 10. 明确仍未付的课题责任

本组件没有实际输入运行，当前没有可刊的 held、H、D、germ、marker 或 $\delta_E$ 数值。源码即使未来付齐其三组输入，仍须同一准确场的实际全局嵌入才能应用 R238；定量欧氏商距离不由该紧性证明产生。

完整同目标 metric 与同 $g$/同十词求解精化、全相位 reach、实际 accepted parent、当前原生轨迹到准确有限场的误差与最终网格展示均保持各自原责任。R416 切口 C 盒是固定来源包围；空间细分/算术精度不能保证它们自动收紧。后继同语义 C 精化应由真实独立生产器及绑定完成，本入口不预借 R426 的未来结果。

全文只支付当前同场的来源、完整域及既有几何命题的准确应用。实际课题未完成；继续推进不以此组件或一次预算结束为终点。
