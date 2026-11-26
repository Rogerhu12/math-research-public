# 04 已记录 relative Gram 最大值的准确统计含义

2026-11-26，Astra-larger-e4e2a2bf-20261126。仅核完整已刊源码和实际返回字段；没有新增科学计算，也不重新登记 R660/R664 的谱代数。

## 1. 对早前口头名称的纠正

本会话早前把 04 的 `max_relative_gram` 称为“最大度量分量误差”，这个名称不准确。892f 完整 driver 的 `statistics` 明确先用 `q.unweight(native)` 消除观察角轨道平方根权，再计算每点对称二阶相对 Gram 矩阵的**算子范数**，最后取整个有限观察集上的最大值。

完整源：

- `scripts/resume_20261126/fullclosed_so3_cached_interior_separation_soc.py`，SHA256 `892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8`。
- `scripts/resume_20261126/so3_closed_meridian_operator.py`，SHA256 `234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42`。

234ac 的 `_raw_block` 定义

$$e=|F_s|^2-1,\qquad f=\frac{F_s\cdot F_\phi}{a\rho_0},\qquad d=\frac{|F_\phi|^2}{(a\rho_0)^2}-1.$$

三项均先乘同一角轨道平方根权，`unweight` 随后逐点除去该权。因此统计作用于原三项，而非某个加权矩阵范数。对矩阵 $E=\begin{pmatrix}e&f\\f&d\end{pmatrix}$，实际完整代码是

```python
maximum = lambda a: float(np.max((np.abs(a[..., 0]+a[..., 2])
    +np.hypot(a[..., 0]-a[..., 2], 2*a[..., 1]))/2))
```

这个表达式是两特征值绝对值的最大值。其谱对象与既有 [R660](../results/R660-positive-spectral-Gram-blocks-and-maximum-control.md)、[R664](../results/R664-positive-spectral-residual-Hessian-and-true-gradient-pullback.md) 一致；不是逐项绝对值的最大值，也不是 Frobenius 范数。

## 2. 已返回数字和没有付清的范围

[04 实际44/45](2026-11-26-run04-actual44-45-first-backtracked-SOC-accepted.md) 的 `0.03513609110016425` 与 [46/47](2026-11-26-run04-actual46-47-second-backtracked-SOC-accepted.md) 的 `0.034109509524516045` 都是上述真实有限观察集统计。这里只纠正其中文名称，不修改原返回值、报告身份、真实方向或接受判定。

这些数值仍使用工作浮点场及标量载体，且取有限观察集；它们不单独构成准确整面上确界、全误差外包、全 t marked reach 或固定问题精化证据。当前完整后继参数 `computations/resume-20261126-run04-actual46-backtracked-SOC-next64-ready.json` 中的目标仍为原 `--target 1e-9`，没有因为重述统计含义而放宽至分量阈值或修改原完整 QP。

当前约 0.03411 仍未达到本题整面 relative metric ≤1e-6 的完成标准。准确积分/插值/角余项/浮点及其余几何、握持与实际精化责任照保。
