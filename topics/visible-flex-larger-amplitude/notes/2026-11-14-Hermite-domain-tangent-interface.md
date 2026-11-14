# 完整 Hermite 域梯度 / 投影正阻尼接口

数学依据是完整证明
`results/R262-Hermite-RMS-domain-gradient-and-projected-descent.md`。
独立源为 `computations/geometry_20261114_hermite_domain_constraints.py`，
SHA256 `d9e004c827add0074c2e6dd6c854763c7157e5049cd5360c1f85ad440462f4ce`，
23,762 bytes。只做过 AST 静态检查，没有该新源的数值 Actions 回执。
它没有改 request17/18 的三份冻结求解源。

## 1. 先检查一个实际查询

下面的独立 CLI 只做完整梯度实现检查，不求新 warm、不运行全矩阵
collocation 线性化、不调 Node / native tail：

```sh
python computations/geometry_20261114_hermite_domain_constraints.py \
  --accepted "$ACCEPTED96" --prepared "$ORIGINAL699" \
  --tail-anchor "$COMPLETED_ZERO112" --tail-config "$CONFIG112" \
  --warm "$ACTUAL_SAVED_WARM" --out "$FRESH_OUT/domain-row.json" \
  --interval 473 --fraction 0.17267316464601146 --angle-index 0 \
  --angles 4096 --jac-workers 2
```

四个原输入 SHA 继续由冻结 warm 接口逐项锁定。`--warm` 可以是该精确问题
下一次合法 saved warm；必须保持699网格、完整场表示和原scalar公式，所有
producer ledger、实际 p 与 scalar 序列化均核对。这里不是用 prepared699
假造已接受父场。

`--angles 4096` 是既有材料边界角数。所保护 `--angle-index` 属于实际物理
RHS 的 `flow.q.N` 网格（当前2048）；两者在报告中分开保存。

输出包含实际原 spline 与 Hermite 代数值的差、原 normal-vector beta²、
叉积等价值的舍入差、左右节点/全局参数/free-core covector、scaled行范数、
三类完整原 complex 方向和三层中心差分、原全部域回执、输入及源 SHA。
若实值差分试点失域，只记录该层无效，不把旧 nodal RHS 固定后伪造梯度。
complex 检查直接提升 real chart 方向至 augmented 状态，避免 real-only
`expand()` 吃掉虚部。

实现门使用既有方向检查尺度 `5e-5`；它是新接口实现检查，不是几何存在、
完整 BVP、native tail 或最终幅度的接受门。成功退出也没有新 warm。

## 2. 供未来 warm driver 注入的最小 API

```python
row = HermiteDomainRow(problem, state, interval, fraction, angle_index)
row_check = row.verify(state)
P = TangentProjector([row.scaled_row], problem.chart.size)

# A is the complete original weighted/scaled collocation + right operator.
reg, C, identity = projected_regularized_operator(A, original_column_norms_squared, damping, P)
check = verify_projected_operator(reg, C, P, A, damping)
solution = lsmr(reg, rhs, damp=0, ...)  # rhs = [-Wr*R, zeros(chart.size)]
z = P(solution[0] / C)
direction = z / problem.chart.scale
action = A @ z
gdot = (Wr * R) @ action
```

`reg` 实际算 `[A P C^-1; damping P C^-1]`，伴随实际算
`C^-1 P(A.T*w_top+damping*w_bottom)`。恢复 `z` 时 P 必须在除 C 之后。
罚项是 `damping² ||z||²`，不是未投影中间变量的范数。

这里 C 使用原**未投影**列范数加 damping 得到正对角预条件。它保持优化
问题不变，但通常不是新投影算子的精确列范数；identity 已明确区分。
环境参数化含有限维冗余核，正阻尼使实际 tangent 子空间内的 scaled 方向
唯一。不能把该冗余核说成丢失原物理方程。

未来消费端必须继续使用完整原实际 residual merit、真实 `gdot` 和原 trial
全 RHS / Hermite / RMS / rho 检查。固定域行只是一个局部优化方向限制。
一个 query 一阶受保护不保证全部域有效，也不保证更大步或收敛。
若 projected stationarity 非零残差，必须报告停滞，不能给 accepted 标记。

## 3. 当前分工边界

request18 已真实完成冻结原 warm driver 的一模型/200 LSMR/初始 damping270，
没有注入本模块。实际80步istop2后仍受同一个RMS点限制，仅α2^-16下降；
详见 `2026-11-14-actual-request18-converged-linear-direction-domain-limit.md`。
因此下一独立新 warm 算法先在该实际新warm核完整域梯度，再作一个投影模型。
已有原三源不覆盖，不把新接口结果冠成旧算法回执。

当前模块本身不创建该新 warm，也没有提出新的科学接受门。
真实非零 H 的 native 初值失败由独立尾侧主线处理；此模块不能把 H 归零、
不能借用失败响应作完成 anchor，更不能替代最终 fresh audit。
