# 冻结 operator 薄层与 R152 严格背景类型的兼容补充

2026-11-12，fd2d geometry。接本轮 `geometry-frozen-operator-projections.md`；原 source、原两点结果及其 manifest 全部保留。

## 1. 具体接口问题和覆盖范围

原两点 operator/局部 `evaluate` 小核确实覆盖了 R155 的背景 view 与 R153 affine view，但它没有调用 R152 的单元 hybrid 入口。静态接口检查随后发现：

`fd2d_gc_positive_gauss_coast_hybrid.py::gauss_cell_positive_gauss_coast_hybrid`

要求实际类型严格为原 `PositiveGaussRawBumpDAE`。这个 guard 用来确保 R152 的 affine lifting 修正作用于正确的 R153 背景，不能只把动态缓存子类改名来越过它。

因此，新 driver 在启用冻结 operator 薄层时，应同时使用本稿的 cell consumer。**四个冻结角矩阵缓存不用于 R152/R153 背景路径。** 节点求值和独立的终端 trace 增量仍可使用缓存；共享 prepared geometry/reference 缓存不受影响。这里没有把有限缓存覆盖范围冒称为全部求解路径均命中。

## 2. 最小适配与不变性

另名文件：

`scripts/fd2d_gc_gauss_cell_frozen_operator_compatible.py`，SHA256
`d5b3828bf52f2778a66541452263aecac47207ac6a2a6ad80c356726a05d9c46`。

该适配器仅对已注册的纯 operator thin class 建立一个 runtime copy。在这个 copy 中，`coast_background_view()` 直接执行冻结的原 `PositiveTraceRawBumpDAE.coast_background_view` 方法，所以生成的对象**确实就是原 R153 类**。原严格类型检查仍执行，并且通过其原来允许的对象。

该原背景移除新共享 operator 缓存的标记，清空其局部 operator packet；已有纯原 R153 的求积/known-lifting view 可以保留，带动态 operator 子类的派生 view 则丢弃。每个视图仍使用同一实际 $s$、角列、参数、完整 lifting、窗函数和 P1 系数。

随后直接调用冻结的原 `gauss_cell_positive_trace`。没有复制或改写 PDE、R152 细求积、R153 商修正、R155 端点差、角漂移项或任何 Jacobian 公式。原 consumer 创建的纯运行视图缓存会回传给原 local problem；没有把字段或数学定义复制回去。

因此，实数算术的完整有限方程和其 Jacobian 保持原定义。该 adapter 改的是一次背景视图的构造路径和缓存使用范围，不是数学场。它没有进程全局 base-class patch，也没有编辑活动 23 或任何旧源。

## 3. 唯一实际单元核查

输入仍为不可变 22 accepted1，SHA256
`4251d15d3c78675ba8bbaf6cc2b71eb82bf78b8b6138e481aead56d73b6a0f68`。

取其实际节点 64、65 构成的单元

$$
[0.6116816746501718,\ 0.6313633493003443].
$$

它与 reference coast 相交，实际触发原 R152 known-lifting 细积分，使用原 Gauss2 非线性项和 order8 的 known-lifting 规则。旧、新 consumer 都在同一个真实保存状态上各计算一次，`jacobian=False`。

真实执行 session `66277`，初始 chunk `994dba`、最终 chunk `1e7677`，自然 exit0；36.605536308 秒，峰值 RSS 102732 KiB。

以下输出全部逐字节相同，最大绝对差为零：

- retained cell 与 retained residual；
- high residual；
- 完整、被省略的角向 Codazzi 单元数组；
- Gauss2 点处的实际 Gauss；
- 实际求积点；
- 原 consumer 已有的全部 `info` 字段。

共享四矩阵缓存的调用数为零，符合本例全部位于 coast 背景路径的明确范围，不把未使用缓存的分支伪报为命中。原两点独立小核已实际验证节点路径的 view 绑定、operator/JVP 及浮点重分配；本次只补真实存在的 R152 入口缺口，没有重复其计算。

核查源：`scripts/fd2d-frozen-operator-cell-compatibility-check.py`，SHA256
`7b73635d0afd83d53fcfa9e54b490409b6e7b750f452c4837b244f3ed441f3bd`。

报告：`notes/2026-11-12-fd2d-frozen-operator-cell-compatibility-check-01.json`，SHA256
`06fa816b366121fc0a02190717150d8ca75cd14e470e863e7cdf27bfd75fab44`。

这不是 whole objective/J、body 或 BVP 运行；本次没有另作 Jacobian 数值复核。完整 Jacobian 路径仍直接调用原 source 中原式，未建立另一个改写版本。

## 4. 新 driver 的直接入口

```python
from fd2d_gc_gauss_cell_frozen_operator_compatible import (
    gauss_cell_positive_trace_frozen_operator_compatible,
)

cell_consumer = gauss_cell_positive_trace_frozen_operator_compatible

result = cell_consumer(
    problem, vector, order=2, high_weight=1.0, jacobian=True,
)
```

normal 与 no-J 路径应传入同一 callable。若 problem 没有启用冻结 operator 薄层，该函数直接使用原 consumer。保存实体的数学 schema、原 source SHA、完整场定义不因 runtime 缓存而变；新 driver 另行记录本 adapter 的来源与明确缓存覆盖范围。
