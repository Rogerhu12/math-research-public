# 保留已发布高度行，分开记录浮点评价重放

日期：2026-11-14。状态：针对实际回放失败的独立数值接口修复；不改变物理模型、原优化约束或求解预算。

新增 `scripts/frame_published_height_rows.py`，原 joint driver 只改为调用它，并记录两份数值身份。已发布 `frame_height_polytope.py`、`frame_height_quartic.py`、模型源码和四份输入均保持原样。

## 1. 实际失败发生在优化之前

公开 run `43633105146` 的 `quartic_joint_audit` 在阶段 `original-fixed-T-polytope-numerical-replay` 停止。完整源状态、原 source、固定 $g$、坐标和准确系数检查已通过；尚未调用 quartic 或 joint 优化器。

失败输出给出：

| 比较 | 结果 |
|---|---:|
| 重建 $A$ 的最大差 | $0$ |
| 重建 $b$ 的最大差 | $3.885780586188048\times10^{-16}$ |
| 原数值定义 SHA | `fca55130a2c176eb6e882a65f6c26b37c895a130b5d8d04149fb6e5ce4e6cc12` |
| 本次重建数值定义 SHA | `57c5e61c5ec96a3a5f861e1cd2b882c53699fff2f5a26237e28de0db28a02c22` |

证据为 `notes/actions-43633105146-1-quartic_joint_audit/quartic-joint-audit.json` 及同目录 summary。旧回执完整保留，不能把这次失败写成数值求解的阴性结论。

原 gate 要求整个数值字典逐位相同，其中还包含 $X$ 的字节哈希、各行的浮点压缩值和见证的 `compressed_bound`。即使数学模型、坐标和系数相同，重新进行角平均、原函数求积、矩阵乘法和最大值压缩，也不能直接假设所有浮点中间结果逐位可重现。现有失败报告没有保存完整的新 $X$，所以没有把差异归因于某个未经观察的 CPU kernel、BLAS 归约或缓存路径。

## 2. 两个对象分别绑定

本次选择保留**原已发布的数值可行域**：

$$
A_{\rm pub}c\le b_{\rm pub},\qquad \ell\le c\le u.
$$

适配对象 `PublishedHeightRows` 直接复制原记录的 $A,b$、帽截距、帽 target 和见证；`numerical_definition` 及 `sha256` 保留原记录逐位不变。它们仍是优化器和选点使用的约束，绝不换成重新评价得到的一组行。

本次目标函数使用新重放的 $X_s,T$ 和共同参考状态，并按已发表的准确四次结构计算。用于该目标的当前 $X$、坐标等另有冻结数组哈希，新的 `replay_evaluation_definition` 明确记录原 $X$ 哈希与当前 $X$ 哈希。因此原 constraint 记录中的 `input_X_sha256` 是**原发布时的来源数组**，不冒称它等于当前对象的 `.X`。

原 quartic 构造器仍要求当前目标 data 的 $X$/坐标与适配器的当前 $X$/坐标逐位相同；只是这份当前数组身份和原约束身份被准确分开了。

## 3. 仍然严格相等的部分

新 helper 使用同一个 `proposal_polytope` 从实际问题重新建立完整数学 provenance，不把原 provenance 盲目塞入新对象。下列项目仍严格相等：

- 四份原输入字节及全部旧 loader 的 source/状态检查；
- 完整物理状态、$u/v$ 准确系数、不可变高度基、完整 $g$；
- T family、高度基、core、cap 和评价规则的准确来源；
- 全部实际径向/角节点，$I$ 的字节哈希；
- 原高度参考系数、盒、球半径、signed-height target；
- 完整矩阵 $A$，另以 binary64 位检查；
- 数值记录的字段集合、见证类型与坐标布局。

真正的行、节点、模型或系数改变不能借数值容差通过。

## 4. 唯一允许的重放差异

仅当前 $X$ 的重新评价哈希、边界 $b$ 的浮点压缩值、帽截距/target 的重新计算及相应见证数值，进入下面的明确回放检查：

$$
\varepsilon_{\rm replay}=64\,\varepsilon_{64}\,S,
$$

其中 $S$ 是 $1$、球半径、帽截距/target 的绝对值、当前 base、$Gc$、旧/新 $b$ 绝对最大值的最大数。最大行差和帽标量差均须不超过这个值。

此外，原报告的每个压缩见证在同一实际坐标下重新评价，仍须在该容差内给出其原行值。若舍入使等价极值点的 argmax 改变，报告明确记录，不把它误认为新物理见证；旧见证仍须独立通过。原 `horizontal_failure` 诊断也不得改变。

**这是浮点评价重放容差，不是已证明的舍入误差上界、求积误差界或连续几何界。** 它不替代也不修改优化的 row tolerance、盒条件、signed-$z$ 条件或最终完整几何重建。实际优化始终保留原 $A,b$，因此即使新的压缩行末位略宽或略窄，也不会偷偷改变可行域。

## 5. 只新增针对性人工分支

新的 `--check-only` 只用三径向、四角、两高度变量的显式数组，不评价研究核心、不调用优化器。它覆盖：

1. 将参考 $X_z$ 和帽截距移到相邻 binary64 值，允许这一次重放，但检查原 $A,b$、截距和原数值 SHA 逐位保留。
2. 把真实行改变 $10^{-6}$，必须拒绝。
3. 改节点、参考系数或数学 provenance，必须拒绝。
4. 将当前数组交给已发表的 quartic 构造器，检查目标冻结的是当前 $X$ 哈希，而约束仍绑定原数值 SHA。

```bash
python topics/visible-flex-new-mechanism/scripts/frame_published_height_rows.py \
  --check-only --out "$RUNNER_TEMP/published-height-rows-development.json"
```

该小检查拟在公开 Actions 执行；本地只作 AST 解析和文件哈希，没有数值通过声明。无需重复已通过的完整 joint 人工链。通过后继续原已授权的一次 quartic 和一次 joint 实际阶段，仍不是追加旧求解预算。
