# 完整 H 候选与原 C 候选比较的实际 warm / FD 薄入口

日期：2026-11-14。

状态：两份独立源码仅经过 AST 与源码静态核对，**未执行数值，未触发 Actions**。它们不改冻结旧求解、原 full-angle 引擎、observer、尾源或 helper。当前可用的父场是 request29 真正产生的未接受 warm，不是完整 BVP 或闭曲面。

## 源与真实输入身份

| 文件 | 字节数 | SHA-256 |
| --- | ---: | --- |
| computations/geometry_20261114_full_metric_projection_warm.py | 30,576 | 8fb6411e7b876713725a80c2dbe9e322cc277001b0692ccc59e0edd59ec4e8b0 |
| computations/geometry_20261114_full_metric_projection_response.py | 2,518 | a24f2e528e35ff7944b56c8fc5a3a1c99ffc7bf2cb5a886cc82990aa85e02117 |

本入口固定消费已推送的完整 H helper：

    geometry_20261114_full_metric_inequality_correction.py
    d5e9432e979859ed7d5277452ac058eb93e99da1cae7f96f700f15d7359d919c

其完整算法、33 次以内 PCG、最多 32 原约束/34 基、1200 次完整 H 硬上限以及全部动作预算见[helper 接口说明](2026-11-14-full-metric-inequality-correction-interface.md)。新入口只作同一模型的接线和比较，不另写求解器。

首次父包硬锁为实际 run 43612331803、source f4896bba、job 132499878558 的 observed-seven-warm：

- warm-001.json.gz：f2e999e7c61d28683dc09adf387e0867b2dd36d271ebe0433fafbec68466fbd9。
- driver-status.json：a24ebbe3d39d64d7676754c67fc56589652bf6fcd31c93c7eca97e1641bebde4。

这两个 SHA 已对下载原字节重新核对。status 的完整 identity 逐键是 warm.optimization_warm 的原值子集；实际父 status 明确 optimization_progress=true、accepted_warm_steps=1，同时 success=false、new_coupled_finite_acceptance=false。入口还核文件名、整份原来源 ledger、mesh、field_representation、完整 scalar schema、固定原输入及实际全局参数，而不是只凭一个新 schema 接受任意数组。

后续若再次消费本入口自身实际产生的 warm，仍要求独立提供真实父 status 与其 SHA，并逐字段验证。完整 resume_producer 子树保持原值；不会把早先五查询/七查询原记录重标为新优化器。

## 同一固定模型中的调用顺序

1. 原冻结七查询引擎照常构造唯一 CompleteLinearization、原权重、完整 A、原 B、真实 LSMR 方向 z0 与原列预条件 C，原实现核仍保留。
2. 拦截原 local_halfspace_projection 调用，仅捕获该次传入的 domain、z0 原字节、C、c 与原总 deadline；原 C 局部投影本身仍执行一次。
3. 在原 choose_feasible_descent 位置，先完整执行冻结原选择函数，得到已实测线性可行且下降的 C 候选，作为真实后备。
4. 若资源预算允许，调用完整 H helper，使用**同一个 A 对象、同一个 b、同一 λ、同一 B/c 和完整 C/z0**。输入身份同时绑定真实父包和 domain.model_sha256。近似逆只生成全局基，未声称得到完整 QP 最优。
5. 用原完整 A/B 读取 H 候选实际向量，再以同一个
   $f(z)=\frac12\|Az+b\|^2+\frac{\lambda^2}{2}\|z\|^2$
   与原 C 候选比较。H 候选只有实际全行可行、实际下降且 f 更小时才替换 C；否则保留 C。有限工作未收敛、无改善或 helper 异常均如实记录。
6. 最终胜出向量重新读取原完整 A、B、gdot、slack，再返回原引擎。其后全部原真实非线性域、固定权重 merit、17 档回溯、RMS 与方向读数原样执行。

完整 H helper 在任何 engine patch **之前导入**，并且检查它保存的选择函数对象确是冻结原函数；因此 helper 内部最后选择不会递归回新 wrapper。所有 module patch 都在 finally 中还原。

原 C 投影记录及其局部乘子仍只解释该原 C 算法，不能移贴为最终 H 候选的 KKT 证据。新 source/schema/选择记录明确区分两者。没有更换原参数 $\lambda=270$、原七查询、2048 个实际角、$\theta=1/2$ 或任何原科学门；同样没有把实际29新发现的 midpoint 障碍偷偷加入 B。

## 后验与完整原数组

输出保留原 C 与 H 的同模型 objective、真实选择及其来源。最终 C 胜时取 μ=0；H 胜时保留 helper 的原非负全行 μ，重新计算

$$
r=A^T(Az+b)+\lambda^2z-B^T\mu,\qquad s=Bz+c.
$$

单列完整原范数、互补和与 R265 单点 E，并把最终点、原 C 零乘子点、helper 的最佳 R267 证据点下界取最大值，评价**实际最终向量**的跨点 gap。后验仍是普通浮点读数，没有外向误差包络；非有限后验仅记录，不作为额外方向/科学接受门。小的预条件残差不替原 r。

新保全文件包括：

- full-H-result.json.gz：helper 全部报告及数组引用。
- full-H-array-manifest.json：所有实际数组压缩分块的文件/shape/dtype/原字节 SHA。
- full-H-final-selected-evidence.json：最终原方向、原 A/B 动作、全行 μ、完整梯度/r/slack 的引用。
- full-H-versus-C-comparison.json：实际候选比较、选择与后验小报告。

完整基、AV、BV、原 raw/best/final 证据都保留。数组按约 2 MiB 原数据量分块，每个块单独压缩；文件大小作为发布元数据记录，不以超过 Git 发布尺寸为由把数学中止。最终 manifest 在所有数组完成后才写入，不包含自身 hash 的循环引用。

## 保留原 midpoint observer

新 Residual 类每次只调用一次原 CompleteResidual.evaluate，再直接复用 request29 冻结 observe_midpoints 函数。原 middle/fm 字节与有限标志不被改写；已有非有限 fm 原字节继续通过 NPZ 保留。observer 后置异常按原方式记录，不改变原判定，不新调用整场 flow 或 Jacobian。

这允许下一实际回执区别“候选仍因未约束的原 midpoint 丢域”和“同模型方向已改善”，但本入口不提前宣称完整 H 会解决该障碍。

## 资源参数与可执行调用

保留原引擎的总 budget-seconds。新参数必须显式给定：

- full-h-budget-seconds：本轮额外完整 H 可选工作时间。
- full-h-trial-reserve-seconds：在原总截止前为后验/保全及原试步保留的时间。

实际 helper deadline 为

$$
\min\{\mathrm{now}+\mathrm{fullHBudget},
      \mathrm{originalDeadline}-\mathrm{reserve}\}.
$$

若原 C 投影结束后已无这段预算，则直接保留原 C 候选，记录 helper 未执行。时间不是强制抢占正在进行的数组操作；helper 的必要有限尾部读数/保全仍可能越过其可选工作 deadline，必须在 Actions 总预算内安排 reserve。原引擎自身在总截止后不再开始下一原 trial，该规则保持不变。

下列变量必须指向真实已保全输入和明确资源分配；示例不捏造实际运行时间或已完成结果：

    python "$C/geometry_20261114_full_metric_projection_warm.py" \
      --accepted "$ACCEPTED96" \
      --prepared "$ORIGINAL_PREPARED112" \
      --tail-anchor "$TRUE_ZERO112" \
      --tail-config "$CONFIG112" \
      --resume "$ACTUAL29/observed-seven-warm/warm-001.json.gz" \
      --expected-resume-sha f2e999e7c61d28683dc09adf387e0867b2dd36d271ebe0433fafbec68466fbd9 \
      --parent-status "$ACTUAL29/observed-seven-warm/driver-status.json" \
      --expected-parent-status-sha a24ebbe3d39d64d7676754c67fc56589652bf6fcd31c93c7eca97e1641bebde4 \
      --out "$OUT/full-H-warm" \
      --iterations 1 --lsmr-iterations 200 --damping 270 \
      --projection-sweeps 200 --line-search-steps 17 \
      --budget-seconds "$TOTAL_SECONDS" \
      --full-h-budget-seconds "$FULL_H_SECONDS" \
      --full-h-trial-reserve-seconds "$RESERVE_SECONDS" \
      --angles 4096 --jac-workers 2

额外整数预算默认沿用 helper：full-h-max-active=32、full-h-max-products=1200、full-h-inner-iterations=64、full-h-inner-relative-tolerance=1e-8、full-h-dual-sweeps=200。C 投影、比较和原非线性回溯动作另由原引擎计时；不能把 helper 的动作上限误称整个 warm job 的上限。

只有上一命令实际产生新的 warm 后，再作原完整边界 FD：

    python "$C/geometry_20261114_full_metric_projection_response.py" \
      --accepted "$ACCEPTED96" \
      --prepared "$OUT/full-H-warm/warm-001.json.gz" \
      --tail-anchor "$TRUE_ZERO112" \
      --tail-config "$CONFIG112" \
      --out "$OUT/full-H-response" \
      --angles 4096

FD wrapper 调用原 constrained_trust_response，完整方向、原三个中心差分步、Richardson 层与原 5e-5 实现门均不改；只认真实新 warm 的 producer schema 并核全部来源。这里继续明确是已完成真 T112 零高 Jacobian 在实际新 H 处的仿射接口检查，**不是该非零 H 的真实 native 解**，更不代替之后完整联解和新 audit。

本轮截至这份说明只有静态实现；没有新 full-H 数值结论。

