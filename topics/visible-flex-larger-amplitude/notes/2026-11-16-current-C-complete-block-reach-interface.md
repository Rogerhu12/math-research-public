# 当前准确 C 闭场的完整根对块执行接口

作者：OpenAI / ChatGPT（geometry agent，AI），2026-11-16。**独立源码与条件接口，未执行。**

## 1. 本次独立入口与未付范围

入口：`computations/geometry_20261116_current_C_ten_complete_block_reach_cover.py`。

```text
R435-current-C-ten450-complete-hierarchical-root-pair-reach-v1
```

配套证明为 [R435](../results/R435-complete-root-pair-blocks-and-closed-separation-cover.md)。冻结 R422 源、R416 准确场、R417 两帽、R413 cuff/原目标、R418 metric 及已发表 R429/R434 等入口均不修改。本组件没有 request、workflow、实际 accepted450、未来 $K/\tau$ 或实验结果。

本次源身份：

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `geometry_20261116_current_C_ten_complete_block_reach_cover.py` | 45568 | `e3fcd9eb7ed304cd502c7e03186d65a2d414366c8ad47313c5754aa43ded66ad` |

它解决原 R422 按每个根 rank 单独遍历的问题。新增多单元包围只能以**原距离至少 $2\tau$**支付整矩形块；不获证就完整分裂。三角块的全部对角保留并最终交原单 rank 方法。它不从块数减少推出覆盖完成，不从位置球推出 reach，不以 metric 成功作为运行前门。

全部数学模块仅在 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public` 下加载。此次准备只做源文本、纸证、文件 bytes/SHA 与文本 diff；没有本地 import、AST、编译、fixture 或科学执行。

## 2. 原来源与直接依赖

新源首先逐字核冻结 R422，再通过该模块的原 `SOURCE_PINS`、`load` 和原入口加载全部直接几何依赖。表中十件是新层的完整直接边界；其下的实际 accepted450、R409/target/checkpoint、C、factory、scalar、proof 和 native 输入闭包仍由原 loader 按真实 source/result 逐项核，不替换成新标签。

| 原直接源 | SHA-256 | 实际用途 |
|---|---|---|
| `geometry_20261115_current_C_ten_complete_reach_cover.py` | `3ea1ef9fb56ec10301defa18d832681d6061d8646e78893957ca160279b71834` | 原 `Roots`、`CurrentGeometry`、`CurvatureCover`、`PairCover`、距离函数、ledger/budget |
| `geometry_20261115_current_C_accurate_cut_patch.py` | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` | `load_accurate_cut_field`，当前准确场与目标 |
| `geometry_20261115_current_C_original_cuff_target_atlas.py` | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` | 原 atlas bytes/SHA 与同一七元组 attachment |
| `geometry_20261115_current_C_ten450_fixed_cap_balls.py` | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` | 实际类 owner、两帽完整 marker、闭 disk/六 jet |
| `geometry_20261115_shared_active_interval_balls.py` | `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` | 当前 R416 实际持有的完整活动六 jet 模块 |
| `geometry_20261115_local_cuff_cross_gram_owner.py` | `0b52a408e08a12c1a16594658510b589ce20d9b2a75430ed5676869e12290456` | 原逐叶 `CuffOwner.test`、完整系数/常数 |
| `geometry_20261115_rational_phase_cover.py` | `f6214d1dc66f9890e99f5d9bbbc93fa0e6524acd6ac879f0058ea023ebc17537` | 原两闭 RP1、四门顺序、Sturm 严格区间 |
| `geometry_20261115_joint_phase_normal_balls.py` | `c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466` | 原双单端/joint OR |
| `root_mixed_phase_normal_balls.py` | `ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6` | 原有理核、向上平方根 |
| `geometry_20261115_shared_curvature_diameter_budget.py` | `b1c2dfb9bd99c0777805da938c38e428da32db8ed5fa6238c9433ed9aede5ad0` | 原纯 `ImageBounds`，全标记 $F_0$ 的 $D$ |

R416 内部继续明确固定 `6a5f949a` shared、`011ca7db` 当前十族 prefix target、`72c4635e` 准确十族 factory、`675ab8df` 六 jet，以及原 R416 proof `3aac8f52...`。完整转递来源见 [R416 接口](2026-11-15-current-C-accurate-cut-atlas-field-interface.md) 和 [R422 接口](2026-11-15-current-C-complete-reach-cover-interface.md)。没有调用旧 ac635/e70d loader 或 675 的历史 `initialise_runtime`，没有把旧 finite/nine 求值器重标为本对象。

`input-binding.json` 实际记录所有已加载直接源（加本新源）、R416 binding、原 R409 七元组 binding、真实 accepted450 checkpoint、原完整 target identity、R413 atlas/attachment、R417 全 marker/graph identity及明确输入的 $K,\tau$。R417 的实际 `type(A).__module__` 类 owner 处理沿最终 `0ff1`，未退回早期同路径第一个模块的草稿。

## 3. 真正输入、完整 CLI

`--directory` 必须指向实际同 job 的 R409 shared 输出目录；`--result-sha256` 是其中真实 `result.json` 的 SHA。R416 从这个真实来源建立**独立准确 cut 场**。`current.source_bundle` 仅是原来源/定义数据；活动求值使用 `current.field`，不会用七元组内的旧 renderer 代替新 patch。

`--cuff-atlas` 及其 SHA 指向真实 R413 输出，随后按原入口核同原 cuff、cap height datum、原 marker 全列表、原准确 target。全部值来自实际输入，本入口不补值或选择常数。

以下为完整 CLI 形状；尖括号均是后继真实 recipe 必须给定的值，本次没有实例化或运行：

```text
python geometry_20261116_current_C_ten_complete_block_reach_cover.py
  --computations <actual-pinned-source-directory>
  --directory <actual-R409-shared-directory>
  --result-sha256 <actual-shared-result-SHA>
  --checkpoint-directory <actual-original-accepted450-directory>
  --proof-directory <actual-pinned-proof-directory>
  --cuff-atlas <actual-R413-atlas.json>
  --cuff-atlas-sha256 <actual-atlas-SHA>
  --curvature-upper <explicit-positive-rational-K>
  --target-reach <explicit-positive-rational-tau>
  --active-depth <original-root-grid-depth>
  --curvature-max-depth <original-curvature-depth>
  --pair-max-depth <original-space-phase-depth>
  --interval-bits <original-interval-precision>
  --sqrt-bits <original-outward-root-precision>
  --max-cells <original-curvature-cell-attempt-budget>
  --max-pair-nodes <original-singleton-space-phase-attempt-budget>
  --max-pairs <original-flat-rank-exclusive-resource-limit>
  --cache-entries <original-spatial-and-phase-cache-capacity>
  --max-constant-levels <original-cuff-constant-refinement-limit>
  --max-block-nodes <explicit-index-block-attempt-budget>
  --max-union-cells <explicit-original-root-enclosure-attempt-budget>
  --block-cache-entries <explicit-complete-union-cache-capacity>
  --budget-seconds <whole-consumer-cooperative-wall-budget>
  --free-bytes-reserve <owned-output-disk-reserve>
  --out <fresh-owned-child-of-actual-RUNNER_TEMP>
```

`--checkpoint-directory`、`--proof-directory` 保原可选语义，未提供时只沿原 loader 自己已有的来源解析。`--computations` 默认新源所在目录；原 `cache_entries=32`、`max_constant_levels=32`、磁盘保留 `2147483648` bytes 默认值仍是原资源默认，不是新的数学常数。三个新 block 参数必须显式给定。

原范围检查未变：$K,\tau$ 为正有理文字；活动根深度在 $0..30$；最大空间深度在 $0..60$；精度留原深度增长余量；所有计数上限为正；wall 为正有限值。无效参数是来源/资源接口错误，不当作几何失败。

## 4. 具体函数和原接口的差异

| 新函数／对象 | 所做工作 | 原数学是否变化 |
|---|---|---|
| `rank_of` | 原 AA/CC/AC rank 的闭式地址 | 不变；与原平铺枚举同一编号 |
| `initial_blocks` | 三个完整初始块 | 不缩减 universe |
| `block_scope` | family、半开索引范围、原 rank 极值与公式 | 极值不冒连续 rank 段 |
| `split_block` | 三角三分／矩形二分，保所有子集 | 只改变组织 |
| `UnionBounds.range` | 每个原根的真实位置包围及完整坐标 hull | 原求值器不改；没有新法向 |
| `BlockPairCover.attempt_distance` | 整块原静态或整圆距离式 | 仅原 distance 分支 |
| `OnePairRoots` | 单个真实四元组迭代器，其他属性仍原 Roots | 原根与原 rank 不改 |
| `single_pair_type` | 原 PairCover 子类，只覆单 rank 报告 | `run/evaluate/phase_test` 真继承，字节不复制／修改 |
| `BlockPairCover.pending/report` | 全部未退休块及原当前叶栈 | 不伪造平铺 rank 后缀 |
| `produce` | 同原绑定、曲率、全 $D$ 与新块执行接线 | 原 reach 合取条件不改 |

完整原数学 callee 保持可逐一定位：`B.CurvatureCover.run/report`；`B.CurrentGeometry.data/short_path/same_cap_graph`；`B.PairCover.run/evaluate/phase_test`；`B.static_gates`；`B.phase_distance`；`B.split_pair`。新源码不覆写冻结模块的任何全局类或函数，也不 monkeypatch 旧 producer。

`SinglePair` 的自定义 `report` 仅因为层级顺序不等于原 flat rank 顺序。原返回中的 `processed_root_pairs=rank+1` 若直接用于这里会错误暗示较小 rank 已全访问，所以新子类报告准确当前单 rank、原计数、原未退休栈及是否真实结束。原 `run` 仍负责全部科学调用、ledger 与空间／相位 split。

## 5. 根、块及全相位责任

原 $A=2P4^h$ 活动根加两帽保留。块地址如 `AA/0/1` 只是分裂树路径；真正集合由 family/shape/两索引半开区间定义。三角含对角，矩形 AA/CC 均在原上三角，AC 左活动右帽。原 rank 用 R435 式 (435.2) 唯一定义。

整块 AA 使用**同一当前准确 family**的共同材料逆运输和共同刚转；CC 两端固定；AC 使用原完整圆相位距离式。没有按相位端点取样，也没有把固定材料 $q$ 错当等量材料角平移。每个相位的点先通过原 bijective transport 回到完整相位零根域，再由完整根对集合覆盖；并不声称每个原固定材料根自身相位不变。

包含对角的三角统一距离不能过正 $\tau$，故直接保全两个子三角和交叉矩形。没有同 cuff、近邻、同帽或零弦整 rank 的豁免。单 rank 的原 static/两端/joint OR、两闭 RP1 图、原 R282 实际 membership、曲率短路径、同图 R24全部仍执行。caps 只按原严格盘外 empty 处理，闭边界不删；多对层即使遇 empty 记录，也交原 singleton owner。

联合球仅由所有成员原 `position_box` 的坐标 hull 与原有理向上平方根产生。每个完整联合节点保存两子联合的 ordinal，或原 root index 与真实 spatial ID。任一子联合不可用就不能支付；错误记录保留，原 rank 后续仍可由其原空间细分处理。cache eviction 仅导致重算，不更换几何对象或缩小责任。

## 6. 实际资源语义及完整 partial

| 参数／计数 | 准确范围 |
|---|---|
| `max_cells` | 原 CurvatureCover cell attempts，保持原意义 |
| `max_pair_nodes` | 所有被委托 singleton 的原空间／相位 attempts 共用原 Budget |
| `max_pairs` | 原 rank 必须小于此值；不允许一个块夹带越界 rank |
| `max_block_nodes` | 每次 frontier 顶块处理计一次，包括 split 和 singleton delegation |
| `max_union_cells` | 原根位置包围请求次数；可能命中原空间 cache，计数不冒 fresh 六 jet 调用数 |
| `block_cache_entries` | 完整区间联合记录的 LRU 条数，失败包围也可缓存但不支付几何 |
| `budget_seconds` | 原 Budget 的 cooperative wall，含实际几何加载／绑定、曲率、联合、全部块／叶尝试 |
| `free_bytes_reserve` | 原实际 out 所在盘的剩余空间检查 |

wall 起点在冻结 R422 源的 checksum/标准库模块加载、参数验证及新输出目录建立之后；这些前置工作和最终完整报告/读回写入不受内部 deadline 的硬中断保证。内部只在原预算检查点停止，SIGTERM/SIGINT 处理也先登记信号、在下一检查点保事务退出。**本源没有独立绝对 kill clock。** 后继 caller 必须提供真实外层截止时间、结束读回的余量和已停止进程的清理条件；本次没有这些运行接线，不宣称已完成。

原 `max_pairs` rank 边界与新 DFS 次序不同：跨界块先完整分裂，遇完全越界块停止时，尚有某些较低 rank 留在其他 frontier 块中是允许的诚实 partial。输出不给“所有低于当前 rank 已处理”的结论，也不把剩余集合写成一个连续后缀。

`pairs.pending` 返回完整 `complete_unretired_block_frontier`；每项带原集合地址和准确 pair count。当前 singleton 另返完整原 space/phase 栈，未启动时显式返原两个 RP1 闭根或 AA/CC 全相位静态根。当前 union 另返请求区间与全部未返回递归 frame。当前 singleton 的整个 rank 仍留在外层 block 中，这是分层保守描述，不能与内栈再相加为不交计数。

预算在 pop 前检查；完整 split/retirement 先写 ledger 再改变 frontier。已退休但含未付终叶的原根对由全部原 `paid=false` 终叶地址账保留；不会因为 rank 被遍历完就标为已证明。算术异常、深度耗尽、预算停止、输入错误及未启动责任均有独立范围。

资源停止不等于真实短瓶颈或 reach 反证。即使索引分裂可有限结束，实际区间证明仍可能完全不成功；最坏可退回全部二次根对工作并支付额外联合成本。本接口没有加大默认实际预算或承诺速度改善。

## 7. 临时输出与一份必要读回

输出在调用者实际 `RUNNER_TEMP` 下新建自有目录。若 out 等于 temp 根、不是 temp 的子目录、已经存在或包含任何原输入，先报工程错误。此所有权检查不涉及几何门；本源不删除任何输入或输出。

| 临时文件 | 完整内容 |
|---|---|
| `input-binding.json` | 同场／来源／原常数、直接闭包、原数据身份 |
| `result.json` | 当前阶段、全部结果 flags、资源／错误、完整 pending、全部文件身份 |
| `large-arrays/complete-original-root-universe.json` | 原所有 pieces、两 sheet、两帽、完整 rank 定义 |
| `large-arrays/complete-initial-pair-blocks.json` | 三个完整初始块和准确原 rank 公式 |
| `large-arrays/complete-spatial-enclosures.jsonl.gz` | 原实际六 jet／帽空间记录 |
| `large-arrays/complete-curvature-cover.jsonl.gz` | 原完整曲率 closed DFS |
| `large-arrays/complete-original-singleton-space-phase-cover.jsonl.gz` | 原 singleton 全部 gate、split、terminal、异常与 rank |
| `large-arrays/complete-original-rank-block-cover.jsonl.gz` | 全部块距离尝试、完整子块、实际退休或 singleton 委托 |
| `large-arrays/complete-root-interval-position-unions.jsonl.gz` | 全联合闭盒／球、原 spatial ID、两子 ordinal、失败上下文 |
| 其余原 `actual-*.json`、DAG/target/cap binding | 与原 R422 同一完整来源保存 |
| `necessary-summary.json` | 唯一 ≤90000B 的必要原值／范围摘要 |

每条 ledger 带原 ordinal，gzip 成员保压缩与 decoded bytes/SHA、行数。块的新顺序可能让 singleton 原 rank 非单调；必须用 R435 自己的 schema/地址合同消费，不可把本 ledger 当成已经平铺访问的原 R422 全 rank 前缀。

必要摘要保实际完整 block frontier、原当前 singleton 栈、union 未返回 frame、完整曲率 pending、错误／资源、总数／逐 family 数、完整 $D$、全部 reach flags、原 source/run/输入和各全账身份。已经退休的每条成功 block 坐标或每个原叶的大记录不全部搬回；所有终叶失败地址仍在原完整临时账中，摘要明确该未逐值读回范围。没有把 hash 当工具端已审完整数组。

stdout 唯一科学摘要 marker：

```text
BEGIN_R435_CURRENT_C_BLOCK_REACH_SUMMARY
END_R435_CURRENT_C_BLOCK_REACH_SUMMARY
```

随后有 `R435-necessary-summary-identity`；有实际 `GITHUB_OUTPUT` 时保已有键名 `closed_reach_summary`、`closed_reach_summary_bytes`、`closed_reach_summary_sha256`，但路径内容是 R435 自己的 schema。未来 caller 必须显式核该来源，不仅看相同输出键。

必要 JSON 超限返回 70，只给 attempted bytes/SHA 与完整 result 身份，保原临时输出；不能认为科学失败，也不能按“进程曾返回”清理未读数据。正常字段完整写出后，错误返回 1、外部信号返回 $128+\mathrm{signal}$；纯资源 partial 可如原 R422 返回 0，**exit 0 不表示覆盖或 reach 通过**。数学结论必须读取完整实际 flags。

## 8. 结果判定与保留责任

`pairs.complete_root_pair_cover` 只指整个原 rank 集都已由块或原 singleton 完整遍历；`complete_pair_responsibility_paid` 还要求每个原 pair 都真实支付，没有任何未付原终叶。`retired_original_root_pairs` 与 frontier count 的合计必须是原 `planned_original_root_pairs`；报告异常时仍尝试保完整 pending，但不宣称会从操作系统强杀或存储损坏恢复不存在的字节。

原最终合取保持：没有执行错误／资源残留，完整闭场浸入与原 $K$ 包围已付，全部原 pair 已付，且 $K\tau\le1$。只有如此才可设置 `accurate_family_embedding_and_reach_certified`。README 的 $\tau\ge0.03D$ 仍另对整个标记闭 $F_0$ 的原 $D$ 检查，不重新选择 tau。

完整同一准确 target 的 metric、whole-image held、含反射 $\delta_E$、数值 shadow／RK／准确几何比较、真实 BVP/native 接受与同 $g$ 精化仍分别保留。R435 既不要求这些下游门先过，也不声称自己的通过支付它们。

本次不把 R429/R434 中冻结的 reach role 自动替换成新 source，不扩它们的预算或读取合同。后继若要采用 R435，应在真实 caller 中明确新的 source/schema、三个组织资源参数、原所有输入/常数、同一个实际 deadline 与完整必要读回；无实际 recipe/run/父场时不填写成功证书。
