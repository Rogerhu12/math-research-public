# 已知 cut 方向帽消费者 v3：准确入口与原 dyadic 首节点

本版本保留 v1、v2 的原字节和真实失败。它不更换原候选、完整
1977 格 cap native、Hessian、cut 行、原 767 MB matrix artifact 或参数域。

公开 v2 run `43609037484` 实际 child 返回 1，完成的新单列格为 0。
其原 native SHA256 为
`9f8ed802456a6098e2b7ba03cb1f31f7dbcec62be426bd3d7c3d4ee0f14d42a4`；
真实 artifact process SHA256 为
`b764d91ef2aa45f02c10b5f66802ee0f1965f1a748b1997d8da72e27db92a56c`。
已完成的 receipt-only run `43610342605` 只读取原字节，确认前六门通过、
第七门 `all_original257_states97_columns_and_exact_shared_endpoints_retained`
失败。它未运行任何数学 producer。

原 descriptor 明确分别记录

$$
L=\frac9{10},\qquad
r_0=\frac{8106479329266893}{9007199254740992}
=\operatorname{binary64}(0.9).
$$

这两者不相等。v2 新加的 $r_0=L$ 门不是原科学对象的正确身份门。
原 packed-v5 残差消费者保留同一准确 Hermite 三次片，在第一格允许
从 $r_0$ 向左延伸到 $L$；原边界消费者也在准确 $L$ 直接评价该 Hermite
片后与真实 inlet 比较。

v3 据此同时修正以下三处，而不是仅删除拒绝门：

1. 首节点必须仍为原 binary64 数，并与原 descriptor 的
   `exact_proposal_left_float` 完全一致；descriptor 的
   `exact_requested_left` 仍须准确为 $9/10$。
2. 第一条完整连续格采用原 packed-v5 相同的 Hermite 外推范围条件，
   其余格保留原节点内范围条件。全部 1977 格的 interval/index 仍逐条匹配。
3. 新单列入口先调用原有向 `hermite_series` 和 `evaluate` 在准确
   $L$ 求值，再右乘同一准确 dyadic 方向 $w_0$。直接取 `state[0]`
   不能代表准确 $L$ 的值，本版本不再采用该做法。右端 $25/8$ 本身为
   dyadic，原右端值处理保持不变。

除上述原入口实现的一致性修正外，v2 的全 97 输入、257 物理态、
完整 angular 255 支撑、八项连续平方费用、六项端口费用、独立 mean、
真实 Robin、Hessian residual bridge、moving high 输出及未改善格的
原 HS 界均保留。所有旧已完成数学格只消费一次。本次此前没有完成的新
one-column 格，故无需重跑或丢弃任何成功前缀。

新 worker 会先读取并出版 v2 的原失败收据，并保留其中 v1 失败身份；
随后只运行原计划的 16 个新单列格。数学 child 若再次失败，原
failure/gates/成功 cell index 会立即保存为小文本，原完整 native 和
日志照常保留。不能把通过来源和端口的一致性门称为已完成全部 1977 个
新单列计算，亦不能把某已知方向误差收紧授予完整边界 operator。
