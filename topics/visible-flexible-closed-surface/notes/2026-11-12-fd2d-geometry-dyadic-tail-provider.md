# R170 的显式 finite provider 与完整 archive-native 入口

本组在已闭 [R170](../results/R170-dyadic-Bernstein-box-for-the-same-flat-tail.md) 之上补可直接集成的域接口。数学字段仍用原 P1、独立 tail16、中央 Fourier、七个 profile 参数、完整 atlas/lifting 和 R153/R155。当前主求解 Context、QP、接受流程和全部冻结源码均未改。

## Provider 与 QP 行

`scripts/fd2d_gc_dyadic_tail_problem.py` 提供真实新类 `DyadicTailRefinedDAE`。其显式 factory 为：

```python
problem = create_dyadic_tail_problem(
    candidate, saved_field=field, split_cells=(), **original_v3_arguments)
vector, refinement = problem.inject_saved_field()
rows = scaled_tail_linear_constraints(problem, parameters, parameter_scale)
```

factory 继承现有 `MidpointRefinedFixedTailDAE` 的实际保存网格恢复，不替换现存 live 对象的类型。`tail_class` 选择真实新 `DyadicBernsteinFlatDevelopableFamily`；新的 `parameter_domain` 仅以准确子盒证书替换旧 tail min/max，中央有限曲率、profile 线性域和实际 operator 有限性判据保持原式。

当 QP 变量为 $z$、实际参数增量为 $dp=\operatorname{diag}(p_s)z$ 时，`rows['matrix']` 是 128 行完整参数矩阵，其 tail 段为 $S\operatorname{diag}(p_{s,\mathrm{tail}})$，其他列准确为零；返回增量上下界和准确有理右端。调用者须去掉旧 tail 的逐分量 Bounds，保中央/profile/gap 的所有原约束。缩放矩阵与普通右端是浮点求解表示，接受参数仍由准确有理域检查决定。

新的 Context 投影不能再对 tail 使用 `[0,1.2]` clip；应显式调用已闭收缩工具并保存其真实参数变化，随后重新评实际目标。`checked_search_domain` 始终调用当前 problem 的 `parameter_domain`，其中央舍入比较逻辑可沿用，但报告需注明现在是明确的新 tail 域。该组不声称 Context/QP 已自动切换。

## 保存与完整 native

新 `checkpoint_arrays` 保持原 v3 调用签名，另外写入 `tail_search_domain_kind`、完整 `tail_search_domain_definition` 和准确证书。它移除三个旧求值数组 `full_gauss_nodes/codazzi_cells/omitted_codazzi_cells`，防止修改控制后借旧诊断；调用者可随后附上实际新求值。原数学表示标签继续表示同一组函数，而独立 domain packet 明确新的参数合法性条件。

`scripts/fd2d_gc_dyadic_tail_archive_native.py` 是一个真正的新完整 decoder，具有自己的 class/schema。它的显式布局构造与元数据绑定来自已冻结独立 tail reader 的逐字逻辑副本，保原源 SHA；完整求值方法继续继承冻结 `PositiveTraceNativeField` 链。新增的必需 domain packet、真实新 tail 类和准确 PSD cut 判据替换旧全局系数符号判据。没有将负控制传给旧 native guard，没有伪造正参数或旧类名字。

```python
native = bind_dyadic_tail_archive_native(
    actual_new_archive, foundation_definition=old_complete_definition)
# native.definition() 保存后：
body = load_dyadic_tail_archive_body_reader(new_complete_definition)
```

foundation 只提供准确绑定的 candidate、中央固定包与 reference 输入。所有实际 raw、参数、mesh、窗、atlas、lifting、domain 和布局都来自新 archive。本入口因而允许未来 raw/中央/profile 一起更新，而不限于前一闭组的固定父字段加 tail override。

新字段仍只声明准确 cut 的值和角向两 jet；不把 $h=0$ 的径向 II 导数设成零。R162 原来依全局非负 Bernstein 系数导出的特定高阶零点常数也不从域扩大自动继承；这不影响 R170 已证的标准尾部 $C^2$、曲率、法球和高度结论。

## 本次唯一小核

真实命令使用已闭 23b4 parent definition 和 R136 半径包。owner session `73984`，首回执 `a8b27b`，完成回执 `36b392`，自然退出 0，脚本计时约 3.71235 秒。

实际布局为 K31、129 个保存径向节点、95 个 raw 列、独立 tail16、完整 54 参数，tail slice 为 `[31,47]`。初始恢复逐字保持原字段与参数；随后仅将 tail 设成 R170 的明确负全局系数例子，构造一个**未求解的 fixture**。旧 global box 在首判据拒绝它；新准确子盒允许它。本次只在一个真实径向点消费 operator 有限性判据，不运行 whole F/J、normal、BVP 或 body ODE。

该 fixture 实际保存、原样 restart、完整新 native 解码及 body cut 路由均通过。恢复向量和 native mesh/raw/parameters 逐字相同；128×54 行嵌入的数值对照差 $5.55\times10^{-17}$；真实 cut 六项对直接新 tail 的差 $1.11\times10^{-16}$。fixture 不是新的 accepted 解，也没有继承原态的残差、连续正域或几何证书。

该真实输入、源码、报告、完整定义和退出回执由本组 manifest 绑定。其余主线可在自然边界另名接入；本组不改变当前运行。
