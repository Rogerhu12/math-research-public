# 低内存 C² 比较适配层独立审查

审查者：`/root/tail_theory`，2026-11-09。作者为 `coupled_prefix`，审查者未参与该适配层实现。

结论：**静态实现与作用域审查 PASS；独立小规模精确索引复核 PASS。** 此审查不重复原比较器的全部证明，也不把尚未完成的真实两图运行当成已完成证书。

审查目标为 `scripts/db6f-prefix-tail-c2-stream.py`；精确绑定记录在 `notes/2026-11-09-db6f-tail-review-c2-stream.json`，包含目标脚本及审查脚本 SHA256。

## 1. 存储变换

已审 `StreamingExactIntegratedTail.span_polys(index)` 供应原物理 span 上的 $F,F_r,F_{rr}$，轴顺序是 `(degree, coefficient)`，次数分别为 5、4、3。新适配层为每个 batch 分配 `(batch, unionCoefficient, degree)` 数组，将对应的上下端点分别转置并赋给唯一的 signed-mode 槽。赋值不作浮点算术；未出现的频率精确填零。

公共 planar 模由两个有符号整数模集合的并集得到，height 模独立取并集。两者放在不重叠的系数块中，故同名整数不会误合并 planar 和 height。底层构造器已经拒绝同一块内重复模。`P,C` 与新块边界一致，原比较器的角导数权重和 planar/height 范数分界因此仍正确。

缓存键为本次原 span 索引的完整有序元组。第一次请求构造全部三阶数组，后两次请求复用同一数组；下一 batch 索引变化后重建。重复索引按行重复正确填入，不因字典或排序丢掉原顺序。当前比较器传入一维整型索引数组，符合此适配层约定。

## 2. 原比较算法保持不变

三个替换仅改变数据供应：manifest 路径映到已加载对象，`exact_nodes` 读已审精确有理节点，`polynomials` 返回按需批量视图。原 `db6f-tail-c2-compare.py` 的背景参数同值检查、精确共同分割、span 包含检查、仿射限制、向外 Bernstein/Fourier 界及最大值汇总均未改写。

因此新的输出仍只比较两个有限扰动在共同外域上的差。同一旋转背景在该比较中相消；R6 圆领、可能略异的外域端条带、完整闭图的高度归一均不在范围内。报告明确记录这些限制，以及“同 CP 不代表相同内部 RK 评价或相同阶段补偿”。这符合当前两档 critical 表示比较的用途。

## 3. 独立索引复核

`scripts/db6f-tail-review-c2-stream.py` 从目标脚本 AST 提取实际的 `BatchPolynomials` 和 `OrderView` 类。使用两个含不同 signed planar 模与不同 height 模的微型几何对象，逐一给每个阶、每个原系数及每个 span 填入可辨别的精确二进标记。检查一个含重复 span 的 batch、一个单 span batch以及同键缓存复用。

全部 2,250 个被复制的上下端点与预期逐值相同；全部 1,650 个缺失频率槽精确为零。这个检查只验证存储/轴变换，不声称支付任何新的数学误差项。

未发现必须修改的问题。真实 critical 两档的连续比较结果仍由作者完成运行后另行报告。
