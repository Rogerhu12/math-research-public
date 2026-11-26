# 892f / 72f / e716 的永久几何地址集合闭包：完整源码审查

2026-11-26，Astra-larger-e4e2a2bf-20261126 / geometry。本条只读已刊完整源码，给跨 run 再生时的**地址来源范围**；没有科学执行，没有比较未知未来场，没有改算法、参数、历史或完成标准。不是新的连续几何定理，不重新登记 R703/R707 等已证内容。

## 1. 精确范围与结论

固定一次实际完整算子 `q`。定义其有限几何地址集合

$$
G=\{(c_p,\operatorname{hex}(u_p),\operatorname{hex}(\phi_a)):
0\le p<P,\ 0\le a<N\},
$$

其中 $c_p,u_p$ 分别是实际 `q.observation_cells`、`q.observation_u`，$\phi_a$ 是实际 `q.phi`，$N=\texttt{full_N}/4+1$。这里 hex 是工作 binary64 的准确字面身份；不按近邻、四舍五入或模周期合并地址。

令 $P_0$ 包含完整初始 curvature/radius memory，以及本次显式供给 `prior_rejection_requests` 的真实历史报告可能引入的所有 literal 地点。则当前这条实现之后产生的每一个永久**地址**都属于

$$
P_0\cup G.
$$

特别地，来源于新物理场的新增极值搜索没有连续改变 $u$ 或 $\phi$：它只能选择原有限 grid 的地点，或把已有永久/历史地点转入另一类别、升级 protected、增加实际主曲率分支或直径 partner。所选极点、类别、保护标志和先后次序会随真实场变化；本结论没有断言这些结果跨 run 相同。

历史输入若含 $G$ 外的 arbitrary 地址，这些地址必须照旧保留并真实读取。若未把某个 prior report 所含地址计入 $P_0$，上述结论不能改写成“只有初始显式两数组与 $G$”。这项独立的历史导入通道不能漏掉。

## 2. 已核完整 source 身份

以下文件均小于100KB。本次核了完整小文件字节SHA并定点阅读所有地址生成/复制分支；没有读取大科学报告。

| 源 | 字节 | SHA256 |
|---|---:|---|
| `scripts/resume_20261126/fullclosed_so3_cached_interior_separation_soc.py` | 75059 | `892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8` |
| `scripts/resume_20261126/so3_closed_meridian_geometry.py` | 43884 | `72f3825913c9ac07b30dcbc47f34e4d8ad901c2f6b6cab0cdc50f35ab99a3cc6` |
| `scripts/resume_20261126/complete_normalized_parent_so3_rows_soc.py` | 40993 | `e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021` |
| `scripts/resume_20261120/fullclosed_point_inequalities_v2.py` | 12166 | `e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8` |
| `scripts/resume_20261120_curvature_qp.py` | 21839 | `a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854` |
| `scripts/resume_20261126/so3_closed_meridian_operator.py` | 38764 | `234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42` |

这些 source guard 同时留在实际 driver/helper，不能把这项审查无条件外推到未核的未来消费者。

## 3. 72f 完整 scan 的集合归纳

`_location` 只有两个分支：已给 `cell/u/phi` 时保其准确解析值；已给 `stage/angle` 时直接索引三套实际 carrier 数组。`_grid_location` 只在后者附上 stage、angle、s 元数据，没有求新地址。`_key` 使用 `(cell, u.hex(), phi.hex())`，`_remember` 只增加该 key 或将已有 protected 从 false 升为 true。

`_ensure_grid` 遍历 `q.grid_fields` 的全部角块，要求不重叠且完整覆盖。每个块都包含全部 $P$ 个观测径向位置。它的所有新候选都来自现成数组下标：

- 主曲率最大值和最大半径是 `argmax` 后 `unravel_index`，再经 `_grid_location`。
- body diameter 和 paired witness-distance 的 bounded pool 是 `_block_candidates` 在已完整读取的块上 `argpartition/argsort` 后取下标，再经 `_grid_location`。
- 原 pure `pick_extremes` 也只从 `np.unravel_index` 返回下标；其邻近去重只筛已有下标，不生成连续邻居。

因此这些新地址全在 $G$。随后 `scan` 把两 memory 取 union，逐一读六个 world jet、两支主曲率和全部幅度不等式。若某永久点更新 worst/farthest/pool，只复制当前 union 内的同一个地点。`_offer` 只按原 key 保留排名，没有插值或局部优化。

最后 `_remember` 添加的 worst/farthest/pool 仍来自该 union 或 $G$。`_new_locations` 只取与传入 memory 的 key 差，并另报 protected 升级；升级没有新地址。发生 incomplete scan 时，异常分支返回的 memory 也只由此前这些合法复制构成，没有“失败后补点”的连续搜索。

## 4. 原192 selector 没有隐含连续点移动

e783 的全部 curvature 候选来自两处：72f shim 返回的 grid 极值；或传入 `witnesses` 的同一 literal 地点。半径 partner 同理来自 grid 半径极点和已给 `radius_witnesses`，另有无地点地址的 `fixed_core`、`cap_height` 标量分支。

容易误读的是 protected-neighborhood：它按同一 cell、`abs(phi-seed_phi)<=protected_angle_radius` 从**已经存在的** `witness_details` 选择当前最大者。它没有计算 `seed_phi±radius`，没有细化 $u$，没有对邻域做连续极值搜索。`diversity_u/diversity_phi` 也只是选择已有 candidate 的间距规则。故 row selector 不会向 $P_0\cup G$ 外引入地点。

72f 追加幅度行只消费 scan 的两个已有 pool，距离地点始终保 ± 两行；cap/height 行没有新物理地址。不同分支、不同 partner 和保护状态可新增约束行，但不等于新增径向/角向地点。

## 5. e716 与完整 driver 的继承闭包

`prior_rejection_requests` 只从实际传入报告中查找完整、同模型、真正拒绝的72f几何记录，复制其 worst 或幅度 pool 地点。该函数不继承旧物理值，并对不同模型拒绝。`seed_before_qp` 对这些历史地点重读当前父的两主曲率分支；直径 partner 来自**当前** scan 的 farthest，或 cap/core 标量。历史地址属于定义中的 $P_0$；当前 partner 已由第3节覆盖。

`extend_from_rejected_geometry` 同样只消费本次真实 rejected scan 的 worst/farthest/pools。`_append_descriptors` 对它们做 key 去重、在原完整父处生成行，并将已有地点添加到 protected curvature 或 radius memory。它不会改地点数值。若新父处出现负 bound，返回实际失败；这一路也没有另选连续点。

`read_fixed_values` 只读取已经冻结的全部 row descriptor 地点和原 partner；SOC projection 的结果是完整**自由变量向量**的修正，不是物理地址坐标的修正。主 driver 的 `scan` 包装在每次真筛后调用 `remember`，ray/SOC/final-selection 的每个完整 scan 都走同一路径。`add_location` 只是解析/索引、hex 去重和 protected 升级。

由此对任意有限个外方向、ray、SOC轮及最终选择重读作归纳，地址 union 始终包含于 $P_0\cup G$。实际次数、极值选择和 ray 接受与否都不参与这个集合证明。报告递归收集器对其他结构字段的识别边界应由该收集器的独立源码审查负责；本条不把未读任意 JSON 当成已核地点集。

## 6. 跨 run 可以推出什么，不能推出什么

若两个实际 run 的三套地址 carrier（含shape、dtype和binary字）完全相同，则其 $G$ 相同。不能只因 N、mesh数量、同一argv或同一source名相同就推出此事。若要称同一物理材料点，还须另外核准确符号mesh/固定父材料图的语义；几何模块已明确旧 normal-angle literal 在新表示中作为固定父 chart 的 $\phi_0$ 读取，不能冒物理证书传递。

在已真实完整扫描该 $G$ 的当前场上，所有从旧扫描新选出的 grid 地址确已参与该场的有限几何真值最大值。这只解释**有限点真筛的集合覆盖**，不是用一套计数替代原地点/历史，也不是删除报告的授权：

- $G$ 外的全部继承 arbitrary 地点仍须单独重读。
- protected 标志、两分支/partner、历史真实拒绝触发的 typed separation，以及最后追加memory后的候选重新选择，均影响实际算法，不能由 $G$ 的集合包含关系删去。
- 新 field 的物理值、残差、微分行、Phi、接受判断必须完整重读，不能转移旧返回。
- `q.domain` 的额外密集 core-angle 正性采样、内部 meridian 积分节点及 inverse-chart 的 $\phi_c$ 是其他数值求值责任，不是这条永久几何memory的新地址生成器；它们不把本结论升级成连续覆盖或全域证书。

因此完整保留44/46/48/新50等实际方向与来源链是相容的；本审查只给“新增有限几何地点来自何处”的准确源码边界，不建议以名义同网格省略历史或当前真读。
