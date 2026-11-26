# Complete parallel defect results in the existing downstream chain

2026-11-27，visible-exact-astra-fb31ed6-20261127 / positive_inverse。

状态：接线与准入范围更新；尚无新 parallel 六球、NS、signed-loop 或 physical 实际结果。

新的 parallel owner 对应 `complete_R142_low193_parallel_source_slice_continuation_v1`，固定源码 SHA-256 为 `368e0f7f0507c7b926983b25fa09c80630142917a69c6384638ba29c168c5a2d`；DP 适配器固定 SHA-256 为 `ffbbc4bdfc71bfc9289891746ef9d39df7c14f2a900b324aa56dbb4e66de46cc`。旧 sequential PS 实现和哈希继续独立保留。

## 两条实际分支

| 已实际保存的完整结果 | 唯一对应后继 |
|---|---|
| 完整六球且 saved body upper 严格小于1 | NS 四源和完整 point 接续 |
| 完整六球且 saved body upper 不小于1 | R149 signed-loop/coercivity，再接原 CP 四源/point |
| 源片尚未覆盖全部155母格，或 defect 为 null | 继续原源片；不得生成上述后继 |

新 metadata 验证器接受两种全域保存形式：原 `source_integral_prefix` 已有155母格，或同一已保存前缀与至多三个完整互不重叠的 DP 源片无缝覆盖155母格。后一种形式还逐个读取完整三球，验证实际六球中的三个平方上端点至少覆盖这些源片上端点的精确和。只给 cursor、hash、prefix 上界或部分母格都不准入。

这项加和检查仅处理已经保存的 decimal endpoints；不调用数值库、不评价任何源核、不重复已成积分。完整旧 model、1424细格、193 atoms、实际执行的 complete/failed 状态、全部门和原始输出字段仍逐项保留。尤其六球后后处理失败仍保持失败状态，只消费此前实际保存的数学对象。

这里的“已保存六球”指正式 scientific output。PS/DP 的 `finish_defect` 先把六球写到临时 candidate 并逐球核包含，然后将 strict-gate marker、唯一 completed target 和六球一起原子替换正式 output；因此正式六球总有该 target marker。第一份临时 candidate 不具备准入资格；此时若失败，只能利用正式155母格三球做标量续接。只有旧 original R142 的非原子保存路径保留 `completed_targets=[]` 而六球已成的特殊准入，不能将该分支套到 PS/DP 上。

## 变更位置

NS 的 `fourfold_codazzi_low_centre_neumann_prefix_admission.py` 新增 DP 全域准入；NS owner 和 generator 的直接 epsilon 来源可为原 PS 或 DP。NS 保存的 direct provenance 仍指向实际原 scientific/execution/manifest 全件，后续重启不把它换成摘要。

`fourfold_codazzi_low_centre_signed_loop_owner.py` 的 `completed_parent_defect` 新增 DP88 输入分支和 `parallel_whole_six_ball_false_branch` provenance；原77、PS85分支不删除。其 metadata generator 的 AST 白名单加入三个 parallel literal 和纯域验证函数。CP 继续只抽取这些明确的 metadata 函数，固定的 signed-loop 源码哈希同步为 `d55b45eec83c69f201df380703818034a7028b7003c970a2d3c3336c9fa0bb55`。

physical owner 和 generator 只扩展直接 epsilon 来源的 kind 分支。实际58、224、32目标，以及普通源/两个mean/负侧接收器的所有数学定义没有改变。

## 实现核对的具体范围

八个修改的 Python metadata 源均通过 AST 解析。相对修改前仓库版本，NS owner、signed-loop owner、CP owner 从 `publish` 起的完整科学执行尾逐字相同；physical owner 从 `save` 起的完整科学尾逐字相同。修改的是新实际来源的资格和来源追踪，不以测试、模拟数值或虚构 parallel outcome 代替真实结果。

上述源码必须在生成后继 manifest 前固定；等待当前实际源积分结果，不提前创建缺少前件的 executable manifest，不改变任何已启动 run 的固定 inputs。
