# R176：完整实际残差的可恢复分段求值

## 1. 结论

对 [R165](R165-grouped-actual-field-Codazzi-quadrature.md) 已明确的有限目标，本结果提供一个新的实际求值入口。它在每个节点、原有 cell block 和内部约束包计算完成后，立即闭存该真实值；重新执行时，只在完整输入、局部输入、参数、有限规则和源码身份全部匹配时复用。

数学字段、保存网格、角模、所有参数、物理 $g$、R153/R155 完整变换、R165 同点求积和原残差行顺序均保持。**函数只返回一个完整残差，或者抛出真实异常。** 不会把尚未覆盖全部行的分片和当作完整 F，不会仅因保存了某些包就宣布接受。

该结果不改变投影、实际域检查、方向或 Armijo 不等式，也不是一个新的非线性求解结果。原执行源和活动 Context 未修改；新值引擎、薄 trial 入口和实际来源各自明确记录。

## 2. 完整分解与不变的行序

设实际投影后的完整有限向量为 $v$。值引擎按下述顺序重建原目标：

| 完整行组 | 实际来源和顺序 |
| --- | --- |
| 全部低频 Codazzi cell 行 | 原 `gauss_cell_codazzi` 的原分块、逐 cell、逐分量/模顺序 |
| bottom | 原所选 node Gauss，随后原末边界、中央约束、另一末边界、最后唯一 gap 行 |
| 内部低频 Gauss | 原选定 cell 顺序及原两个 Gauss 点 |
| 节点 curvature | 原字段、指导上界、权重和排序 |
| 节点 high Gauss | 原完整 Gauss 与同一 Fourier 等距压缩 |
| 全部 high Codazzi | 与低频相同实际 cell 求值所得的原高频排列 |
| 内部 high Gauss | 原同一内部包的高频行 |
| 内部 curvature | 原同一内部包的指导行 |

节点求值仍逐节点调用原 `radial_view(...).evaluate(...)`，只保留原值消费者实际需要的 fields、full Gauss 与两个域诊断标量。之后用原矩阵 `PE`、原边界原始系数和完整真实中央 `axes['gap']` 构造 bottom。没有新增或删除边界行，也没有重新解释 gap 行。

每个 cell block 仍调用原 `gauss_cell_positive_trace_grouped_coast`，其中原 G2 区域与 R165 coast 的完整同点细规则保持；整块返回值连同诊断原样保存。重新装配仍交给原 `gauss_cell_codazzi`，包括它对各数组采用的拼接轴、原 block 顺序、完整 retained/high/omitted 数组及逐块极值聚合。

内部约束仍调用一次原 `interior_gauss_curvature`，参数、选格和顺序保持。节点 curvature/high Gauss 是已经恢复的完整实际节点数据上的原代数运算，没有用旧字段代替新字段。

## 3. 准确缓存身份与完备性证明

每一包的绑定含：

1. 原 Context 的完整绑定，包括物理输入、有限规则与依赖身份；
2. **完整实际向量**的 shape、dtype 和原始字节 SHA；
3. 当前真实值引擎及全部显式 provider/transport 源；
4. 节点或 cell 描述符、准确局部 mesh/vector 身份及全部调用 settings。

全量绑定的规范 JSON SHA 决定该包的目录。它不是只按 cell 编号或文件名缓存，因而某个其他位置的参数或 raw 系数改变，也不能借用旧 trial 的局部包。保存函数调用既有 `save_actual_packet`：无 pickle、分片大小有界、dtype 与原始数据保持，最后通过目录原子重命名发布完整 manifest。未完成 staging 目录不是可读的完成包。

重读时用同一完整预期绑定调用 `load_actual_packet`。它检查 manifest 完成状态、绑定、每个实际传输文件的 SHA/字节数、数组分片连续性、dtype/shape 和重建后的原字节 SHA。一个缺失、损坏或身份不匹配的最终目录会真实报错；不会降为一个看似成功的命中。

现在证明输出与原有限目标相同。固定同一实际 $v$ 和其全部定义。对第一个查询包，若是 miss，直接调用该包的原数学消费者，所以返回原值；若是 hit，完整绑定要求它来自同一输入，而无损重读返回原保存值。对后续包同理，得到每个查询包都是对应原值。全量循环按原顺序查询每个节点和 cell，另核对所有应使用 R165 的 coast cell 恰好出现一次；遗漏或重复即抛出异常。最后仅采用第 2 节的原代数与拼接运算，所以返回完整原目标。

这一论证是对确定的数学消费者及实际已保存数组的复用证明，不声称不同 BLAS 平台或不同数学实现必逐字同一。执行平台或实现发生变化时，新来源必须明确绑定；不能删除其身份以追求命中。实际本轮小核已经对同一次真实求值及重新加载验证逐字相同。

节点和 cell 的中间诊断、grouped rules 也从各完整包恢复。新 metadata 如实区分“本次新求值”与“读入之前的完整真实值”，不把缓存命中记为新执行 F/J。

## 4. 真实 trial 的消费边界

新引擎 `checkpointed_grouped_objective(ctx,v,directory)` 不投影 $v$，也不自己判断域或接受。薄入口 `fd2d-gc-grouped-stage-trial-checkpointed.py` 保留原完整流程：先读取真实基准和方向，做同一投影及域比较，再调用新值引擎，最后用完整真实残差支付

$$
\tfrac12\|F(v+\alpha d)\|^2
<\tfrac12\|F(v)\|^2+10^{-4}\alpha\,DF(v)[d].
$$

只有原不等式严格成立才保存 accepted NPZ；同原入口一样，先保存接受实体及报告，再保存其完整值包。新引擎 source 在 trial 结果中单独记录，不冒称调用了旧 Context 的 whole-value 方法。

旧全局尾控制盒的入口仍执行它原有的域检查。若接 R170 的新尾函数域，调用者必须使用自己明示的新 Context、投影、准确域判定和 trial 来源；可以复用本值引擎的数学分解，但不能借旧入口的 guard 通过负全局控制。本实现没有自动激活任何新分支。

## 5. 实际最小消费检查

使用已经闭存的第 29 轮输入请求，对应第 28 轮新目标的真实接受态

`6668aa11544a18882a778be7ea364faf6c8874a1888fac0a3c87138fcbffe77c`。

实际执行 `71172 / 1086a5 → ba5b94` 自然退出 0，1.848627517 秒，峰值 RSS 105520 KiB。检查只计算：

- 一个真实 node84，其 fields/full Gauss 与已保存实际值包差为 0；
- 一个非零的完整 R165 coast block（节点 74 至 76）。

每个消费者都只调用一次。新对象重启后，9 个实际数组连同原容器、标量和顺序逐字恢复；故意改变完整向量的一个 binary64 值后，旧包没有命中，而是进入明确记录的预期 miss。没有再跑 whole F/J、BVP、标架或 body 来给这个接口增加门槛。第一个启动曾因选错工作目录而真实 exit1，尚未执行数值消费者；该失败与修正工作目录后的成功分别保存，不删改历史。

完整源码、已闭小包、报告和真实退出记录见本结果对应 closed manifest。随后第 30 轮明示 R170 域的独立 trial 入口实际调用此值引擎：全步自然 0、完整范数约 6.29052，按原 Armijo 拒绝；半步自然 0、范数由 4.1885315969 降至 3.6542929578，真实接受实体 SHA 为 `3bceef937899fad65e512e56d3bd747a6d225b20301b64ed9d04582a4f6db981`。这些是两次完整实际 F，来源和全部值包见 `2026-11-12-fd2d-raw-bump-grouped29-dyadic30-closed-manifest.json`。通用旧盒薄入口没有用于负全局尾系数；第 30 轮使用独立新域入口，接受判据保持。该进展仍不构成强目标完成。

## 6. 复现入口

在本 topic 目录作为当前工作目录，局部检查为：

```text
python scripts/fd2d-checkpointed-value-cache-check.py \
  --request notes/2026-11-12-fd2d-raw-bump-grouped29-request.json \
  --out-prefix notes/NEW-local-replay-check \
  --cache-dir notes/NEW-local-replay-check-blocks
```

真正完整试步沿新薄入口使用与原脚本相同的 `--request`、`--out-prefix`、`--direction-id` 和 `--backtracking-index` 参数。绑定不符或不完整数据必须先明确处理，不以更改 guard、补造退出码或覆盖原包绕过。
