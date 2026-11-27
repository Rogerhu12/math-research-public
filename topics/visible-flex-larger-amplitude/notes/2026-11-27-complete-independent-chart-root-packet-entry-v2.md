# 已有 normal 根缓存的完整不可变记录入口：实际字、两处只读钩子与责任边界

本条交付从已刊 `95559b0c…` 独立固定图完整求解器派生的 **v2 全入口**。它在原 QP 返回和原报告保存位置复制已经算出的当前点、完整角根缓存、全部 normal 段与已有矩阵，另存固定工作积分载体和实际元数据。原科学算法、自由变量、固定目标、范数、μ、Phase I、原几何行前缀、全材料包络、所有真实回溯与判据保持完整。

这是后续同场误差消费者所需的数值输入生产能力。当前交付仅完成纯源码验证，没有本机科学调用，没有新 Actions 数值返回，也没有支付根、积分、参数导数或连续几何误差。不能把一份缓存包的 source/word 校验当作连续根支存在、唯一性或整面认证。

## 1. 完整父来源及最终文件

完整父提交为 `35e4d40fd459bef32055684a1048323f96de4a33`。父 driver 是95559完整独立7c图入口，父 launcher 是104220完整 argv 入口，父 reader 是f382完整纯归因入口。它们原字节保留，当前已经准入的科学源没有被本次修订。

| 新完整文件 | bytes | SHA256 |
|---|---:|---|
| `immutable_normal_root_packets_with_entry_binding_v2.py` | 65063 | `ef0d00b4e07b34283b0c73591fb985b7879a4f221f74895eff7a11a0d2db06b1` |
| `fullclosed_reference_centred_independent_chart_root_packets_so3_qp_v2.py` | 76471 | `86b12daa9401bfdd79ab61e44814d1596633835504e5b4f966b3e9308d9b6ba7` |
| `launch_reference_centred_independent_chart_root_packets_so3_actions_v2.py` | 20744 | `114841d141e7a8eee4f3c0719eace929292432b23147ae109228d63b9ebf3872` |
| `read_reference_centred_independent_chart_root_packets_so3_report_v2.py` | 99080 | `3d99c6097e329a0f3bd03845403566654531657604b8f533002575a2e548284b` |
| `derive_independent_chart_root_packet_entry_v2.py` | 14235 | `a74260695b5512f2621544f6ecb1751c2a226e27017850bdd4cab4af9a6ccd44` |

完整再生/补丁/旧新整文件身份存于 `resume-20261127-independent-chart-root-packet-entry-v2-source-locks.json`，9697 bytes，SHA256 `c3ee334eb1aed8079452e229f60a6e66767ee9fe5ad6941ec751f1664115f358`。不是片段替代整源：每一完整新体均已保存在独立 Git blob，完整再生器核对每个父文件全部字节、每个替换次数、每个输出全部字节，以及完整科学依赖。

新 driver 的 `SOURCE_PINS` 只在父完整角色表上新增真正的 `root_packets` 源。物理 normal 仍为d5da、base仍为6a803、固定目标仍由完整独立7c输入绑定。记录器不是物理方法代理，不把新 source 标签冒称旧原函数，也没有重新解释当前未知/失败点。

## 2. 为什么必须把当前缓存点与外层变量点分开

原 normal 对象通过 `_select_point` 维护当前缓存点。一次真实回溯可能在拒绝候选上留下最后读到的完整缓存，而外层当前接受点仍是上一父点。只看最后一份缓存是否“完整”不足以判断它属于哪个场。

每次 entry capture 因而分别保存：

- 外层当时的完整变量点 SHA；
- normal 对象当前缓存完整点 SHA；
- 两者是否逐实际摘要相等；
- 实际 capture 序号、hook 标签及成功/失败状态；
- 只有本次成功时才引用本次不可变 snapshot；
- 本次 I/O 或内存失败的真实类型、消息、序号及当时点。

记录器不选择新缓存点、不把外层x装入对象、不触发根重求或角阶升级。缓存点不同不会被重标签为外层点。实际失败 capture 的 `snapshot` 必须为 `None`，不能指向上一次成功的 snapshot。纯 reader 将每个 QP capture 与该 QP 原 starting geometry 的点绑定；完整最终报告的最后 capture 另与实际 final geometry 的点绑定。初始场失败时则绑定真实初始完整点，同时保留原失败元数据。

## 3. 两处钩子的完整执行位置

### 3.1 原 QP 返回后

钩子位于原 `qp.solve` 返回、原 `actual_QP_seconds` 和 `actual_QP_operator_counts` 结算之后，尚未计算或切换任何新的非线性候选点。记录标签为实际 phase 与 serial 组成的 `metric-QP-return-k` 或 `restoration-QP-return-k`。

两种 phase 都保持原完整算法。metric 仍使用原完整物理 J/J*、H² 坐标、全行约束与原 μ；恢复阶段仍使用原公共 slack 的全行模型。记录器不把恢复 slack 当作几何可行性，也不把 QP 返回或迭代极限当作收敛。

新增 I/O 时间不藏进已结算的 QP 时间。完整方向总耗时仍自然包含其全部工作；记录器自己的累计实际耗时和操作计数另列。它的科学场、root、J 调用计数恒要求实际为0。

### 3.2 原 save_report

钩子位于原 `q.metadata()` 返回之后，直接消费这个已经读到的整对象。原 envelope metadata、永久位置计数、峰值RSS与报告写盘依旧执行。初始失败、初始成功、每个完整方向结束和最终预算返回沿原调用点触发它；没有为增加记录而额外执行一次F/J、全筛或根求解。

在第一次F之前，初始报告已有记录器完整定义、来源、固定工作载体记录和真实0次capture元数据。此时 latest capture 为 `None`，不是伪造“空场已读”。首F失败的原错误与最后部分根批次仍走完整原报告路径。

## 4. 每个已算缓存角保存的全部输入

记录器遍历当时对象已有的完整 `_root_cache`，没有取样或按预算删角。每个角记录：

- 完整当前x原 dtype、shape、binary64字与内容摘要；
- literal angle hex 和实际缓存插入顺序；
- 实际已完成角阶，order1中未计算的二角jet槽明确标为未计算；
- 完整Z、零控制项以及全部声明的 normal 段；
- 每段已有的η、frame、controls、局部J3；
- 仅在缓存确实已有时保存完整J6或J9，缺失时明确缺失；
- 原 source-bound root protection、已有 frame 来源与分段输入来源记录；
- 完整工作模型、固定标量、真实共同 normal 分区及其工作字；
- 原缓存保护摘要与实际完整元数据文件。

没有顺手调用 `_get_roots` 填补缺角或升级order1。成功的完整角包与最后失败/部分批次分开；后者留在独立、整字节保存的 operator metadata 中。缓存没有保留的历史 request 次序、历史矩阵选择或过去中间点不从最终值推断恢复。

“全部 required 角已记录”只针对真实当前 quarter角数组加两类显式永久位置角的完整清单。记录器同时复制所有已在缓存中的其他角，但这个计数不自动成为全角连续覆盖，也不把未列出的未来 query 叫作已付。

### 4.1 本次 v2 修复的真实数据接口

完整4d92 `load_memory` 与95559 `add_location` 实际传入的是 `dict(cell,u,phi,protected...)`，不是位置三元数组。最初未准入候选的 `_angles` 错把字典当作 `p[0],p[1],p[2]`。独立审查发现后，v2 已按原实际字典字段提取、验证并临时排序所需角。

这不是改历史格式：原 witness/radius 字典完全不写回，protected与typed字段保持原词；原numeric-tuple/signed-zero历史去重逻辑没有修改。只在记录器自己的角索引中按实际 root cache 的 canonical hex区分字，包括正零与负零；不把角wrap或规范化为另一字。旧ccd8/da367/1466/dfaf候选留在审计身份中，未准入、未科学执行、没有产生数值结论。

## 5. 固定工作载体与不可变文件

完整固定载体直接从原对象复制：

- 工作 mesh；
- 原实际 Gauss u、Gauss w；
- 原 quarter角数组；
- 完整 integration query 的 cells、local、s、widths、weights、h、hp、hpp；
- 原整段数量、实际 S carrier、normal分区的准确有理节点与既有float字。

记录器核对torch cells与原整数数组相等，但不重新调用leggauss、不重新计算准确标量或积分，也不把float mesh差当作准确仿射宽度。这解决“后来根据相同阶数重生成节点、便冒称原工作字”的责任缺口。

原参考校准文件只按实际已记录 path/SHA/bytes读整文件并保存不可变副本，不重算参考缺陷。所有新科学数组和完整snapshot只留runner，按内容身份命名。已有不同字节的同名文件不能覆盖；已经登记的记录在再次引用时核实际字节。初次遇到未登记但已有的NPZ，只在完整成员/shape/dtype/原字一致后采用该容器的真实whole-file SHA，不把重新压缩容器当作旧文件字节。

每次 capture 前后核完整缓存保护摘要、当前点、对象/方法/source/共同分区和全部实际科学计数。原物理对象、根缓存、参数及计数不能因拷贝改变。I/O/MemoryError在capture层按真实未完成记录；source/model/shape矛盾不能被伪装为数值成功。没有恢复原数据的失败会诚实保留其责任。

## 6. 纯 reader 与原完整报告

完整reader为99080 bytes，保留父f382的全部固定目标、来源、normal、校准、C1/矩阵、包络、Phase I和真实筛查函数。新短函数只加载已经整文件核SHA的纯记录器，调用 `validate_entry_report`。记录器顶层只有stdlib；纯读不会importTorch/NumPy，也不执行任何科学callback。

完整校验包括：

1. source registry、caller source、whole model、固定定义与真实来源；
2. 每个成功capture的整snapshot及全部角包与数组成员原字；
3. 完整实际工作载体；
4. 全部原已完成metric/restoration方向的QP capture；
5. 该QP父点、最后报告外层点和当前cache点的正确分离；
6. 每次capture的成功或实际缺失，不跨序号回填；
7. 所有来源/值校验与根误差/连续证明责任分开。

纯输出只给实际计数、摘要、记录身份和失败范围。raw数组仍不出runner；摘要数组或8×8矩阵不能通过字符串绕公开raw边界。可按scalar selector公开实际capture数、角数、矩阵块数、耗时、source/point/SHA和完整/缺失状态。原全部方向/报告详值继续由完整reader保存在runner。

## 7. 与解析局部J3入口的兼容版本

另有完整独立源 `immutable_analytic_normal_root_packets_v2.py`，67095 bytes，SHA256 `1e0656b19de4eb78937a9f8305569d7c1cce59f48614fb7a279738942bcd622e`。它保留上述相同capture/entry合同，并明确登记：

| 实际角色 | 完整 SHA256 |
|---|---|
| analytic normal | `04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e` |
| 原完整base | `6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865` |
| 当前adjacent矩阵源 | `8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787` |
| 当前reference校准源 | `4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d` |
| 解析局部J3源 | `64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d` |

真实 `q.analytic_stage_jacobian.matrix/metadata` 的codefile及 `analytic_J3` 角色独立核对，其实际counts也加入capture前后比较，并与传入q.metadata对应对象一致。没有把04f1冒作d5da。解析J3组合driver/reader由独立完整入口派生，不能只换父source标签。这个兼容源不证明新J3与旧AD逐位相同，也不替代新局部导数的舍入误差费用。

完整差异与whole-source身份另保在 `resume-20261127-analytic-normal-root-packet-v2-source-extension.json`，4503 bytes，SHA256 `ccd13a4180431bd13032d5095d640b8e18299aa58224ba2b392509083cbfe15f`。

## 8. 实际完成的源码检查与后续责任

v2六件（含解析兼容helper）已实际执行stdlib AST parse、compile及重复literal字典key检查。完整三entry反向替换逐字还原其父；删去只读钩子及初始记录元数据后，原driver每个函数AST相等。原完整科学后缀恢复SHA为

`3a34eeb13a52579aacafb1598c52a94a42f8db2cfab03a3fef0d64c2b88937d5`。

原reader除read_report外全部既有函数AST保持，原launcher完整parse AST保持。没有本机科学import或fixture。solver scratch尚未执行需要完整repo依赖闭包的build；再生器在公开完整checkout上还会逐一核所有原科学源SHA，这与已经完成的纯文本/AST保留证据分列，不假称未执行检查通过。

未来若在真实完整父场上续接，必须使用独立完整seed/restart binder，保父完整变量、固定目标、范数与全部实际/未知历史责任。本次只读hook不放宽原来源或restart守卫，也不把旧失败源改标签复用。新的实际结果仍须完整公开scalar归因；snapshot只有数值字和工作选支来源，后续准确端点、角jet、积分和完整六jet费用必须逐项另付。全域度量、全t几何、真正固定问题精化及仓库完成标准继续保持。

## 9. root完整公开checkout补核

root已实际执行本包完整标准库再生器，以`--verify-existing`逐字核回driver/launcher/reader/helper四个完整新体，exit0；全部原物理依赖完整SHA均核对。没有导入科学模块或执行F/J/root。§8所说solver scratch未执行build是当时的真实边界，此补充记录随后root实际完成的源码闭包复核，不把先前未执行改写成已执行。
