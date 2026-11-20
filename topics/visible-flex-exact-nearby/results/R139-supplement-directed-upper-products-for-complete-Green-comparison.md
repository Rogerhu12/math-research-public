# R139 补篇：完整 Green 正比较中的有向上端点乘积

2026-11-20，`visible-exact-astra-ac637-20261120`。

**状态：本文的包含修复已证明，源码只经AST；第三次原L尝试仍为0 scalar失败，不宣称预算门已过。** 修复只影响 `_complete_modal_norm_comparison` 的正比较标量，不改变任何有符号中心核、原参考解、参数或目标。

## 1. 第三次实际失败的准确边界

公开 [44723722475/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44723722475) 的原L三量续算失败。153个parent、155个比较panel、全部4650旧行及4801交段的私有context已经准备完整；`saved_record_count=0`、`new_records={}`、`completed_targets=[]`，当前目标仍为 `complete_low_family_feedback_necessary_budget`。因此原三量和母合同50量均没有成功记录可重算。已成功的独立mean-atom三条不受影响，仍冻结只读。

唯一child返回1，wall `79.36432353400001` 秒。四次实际pull均与已读README匹配。完整失败由原候选API的严格 `nonnegative square root` 检查发出；traceback定位到 assembly 第438行的完整反向三角平方表达。正pivot及Riccati endpoint-hull准备已通过至此，不能把此失败解释成参考分母或实际算子奇异。

| 完整保存文件 | 字节数 | SHA256 |
|---|---:|---|
| [actual](../notes/low_family_budget_ci/run-44723722475-1/actual-scientific-conclusion.json) | 86795 | `3bb5b0912b7d0fa418ced7074e7b0e19a4ba07a458d9c37e55ed06dda52bc09a` |
| [execution](../notes/low_family_budget_ci/run-44723722475-1/execution.json) | 56874 | `53e9c468ced57040c3e58bd514aab6f328155f9dcf584ca94597ac87c5bb6840` |
| [report](../notes/low_family_budget_ci/run-44723722475-1/report.md) | 528 | `38c38b8f73797aa412d9b9a507c45bd8225bc668f6b91c211dbba8ec6b86092d` |

完整v3清单、所有旧失败及消费标记保持原样。新续算必须用新marker，并保存本次全部失败对象；不重复独立atom、已成endpoint或任何旧范数目标。

## 2. 原完整比较表达与表示问题

原正参考已经证明 `p,H,K,g>=0`，原固定 `q>0`，decay和原子权也非负。此处的 `K` 是参考profile名称，不是内禀曲率。对任一接收panel `i`、源panel `k` 和原模态 `j`，body的两方向费用分别为

\[
d_{ik}\sqrt{(p_i^2+q_i^2)(H_k^2+K_k^2)},\qquad i\ge k,
\]
\[
d_{ik}\sqrt{(K_i^2+q_i^2H_i^2)(1+p_k^2)},\qquad i\le k.
\]

同panel的两个三角都保留。`d_ik` 是原所有中间完整段的有序decay乘积上界；两个可变端片的decay只用已经证明的上界1。低块仍另保真实mean核及全部193 atoms。

一个包围非负量的对称球即使lower为0，其两个副本的普通区间乘积仍可能因依赖丢失而含负下端点；例如把两个副本当独立的中心/半径表达时就会发生。这是区间表示的外包损失。直接删除平方根的非负检查不成立，且会使错误输入难以被发现。

## 3. 保持正比较的修复

若有限非负真量 `x` 已被球 `X` 包围，且原API已验证 `lower(X)>=0`，令

\[
u_X=\operatorname{upper}(X).
\]

有向端点是一个确定的非负数，且 `0<=x<=u_X`。上节两个表达都是各非负变量上的单调函数，所以将每个 `p,H,K,q` 换为其有向上端点、然后按原表达有向求乘积、和及平方根，仍给完整真量的上界。全部原子正比较同理：先将 `g`、`theta`、右向decay取有向上端点，再作原行列和乘积。没有对有符号矩阵执行此替换，也没有把某个原上界相减。

源码因而只在这个**正比较的私有副本**中存 `p/H/K/g` 上端点，`q` 在输出权处也取上端点；weighted-outer原子先取两个因子各自的上端点。原 `profiles.at`、有符号kernel/source列和上下文数据保持原对象。原 `api.upper` 与 `api.sqrt` 的严格非负/有限检查全部保留。

此修复不会凭空缩小预算；它恢复的是原完整单调表达可合法执行的包围。算出的新完整row/column/norm仍必须通过R139的准确必要比较，失败上界仍不得解读为真实范数下界。参数域、96/64模态范围、独立mean、193 atoms、真根、普通dr、所有中间decay和原七port范围均未改变。

本机仅核源码和AST，不导入科学模块。修复后的三个原目标须在公开Actions首次完成后才能登记其数值结论。
