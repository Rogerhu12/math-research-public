# R262 保护查询的一模型 warm / 新 FD 接口

该入口是 request18 的真实诊断之后新增的优化算法。数学依据为
`results/R262-Hermite-RMS-domain-gradient-and-projected-descent.md`，域梯度
来自已冻结 `geometry_20261114_hermite_domain_constraints.py`。
原 request17/18 三源及该域模块均未覆盖。
实际 request18 事实只保留正式记录
`2026-11-14-actual-request18-converged-linear-direction-domain-limit.md`。

新独立源：

| 文件 | SHA256 | bytes |
|---|---|---:|
| `geometry_20261114_protected_tangent_warm.py` | `b126ba6a203cbf97c4c9658abe70e9bf38ad259b2eab89bfed4c6e03f4d97fad` | 23355 |
| `geometry_20261114_protected_tangent_response.py` | `91a77def3f72a588d044e6b52c7254e541384df47e42ede638bec8f6a782f5c0` | 2307 |

只有 AST 静态检查，尚无这两个新源的科学数值回执。原完整边界 FD 的源体
仍逐字锁定 SHA `7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78`；
薄 response 入口仅识别新 optimizer schema，并补全新旧 producer 身份。

## 1. 一次调用先核真实域行，再做一个模型

```sh
python computations/geometry_20261114_protected_tangent_warm.py \
  --accepted "$ACCEPTED96" --prepared "$ORIGINAL699" \
  --tail-anchor "$COMPLETED_ZERO112" --tail-config "$CONFIG112" \
  --resume "$REQUEST18/constrained-warm/warm-001.json.gz" \
  --expected-resume-sha 1dbdcc8fbb9dd7d4571259679a97dca5ee635fab88dece584d3a44727da477c3 \
  --out "$FRESH_OUT" --iterations 1 --lsmr-iterations 200 \
  --damping 270 --damping-attempts 5 --line-search-steps 17 \
  --budget-seconds 1200 --jac-workers 2 --angles 4096
```

默认保护实际 interval473 / fraction `0.17267316464601146` /
physical-phi index0。该角属于原物理 RHS 的2048点角网格；`--angles4096`
是既有完整边界的角数。

同一进程先重建原真实状态及所有域回执，然后写 `domain-row.json`，实际
执行完整原 nodal RHS / spline complex 与三层差分梯度检查。此实现检查通过
后才构造原完整 collocation Jacobian 和伴随，再验证实际投影算子并运行
一个模型。无需另重复一遍成功的原准备场或另解 native tail。

scaled 方向严格恢复为 `z=P(solution/C)`。LSMR 实际动作/伴随为
`[A P C^-1; lambda P C^-1]` /
`C^-1 P(A.T*w_top+lambda*w_bottom)`；其内部 `damp=0`。
预条件 C 来自原**未投影**列范数的正对角，报告不把它称作新投影矩阵的
精确列范数。正则 penalty 始终用实际投影后 z。

暂用与 request18 相同的 lambda270，以便辨别此次 tangent 方向限制的实际
影响。每次线性尝试保留200步上限和原容差；后续实际 merit / 原完整域回溯
保持原17档与规则，不能因域保护而跳过其它角或查询。

## 2. 完整回执与保存

`model-000.json` 保存实际原线性残差的物理/右边界最大值、最坏物理单元/行、
带正则 residual、投影 KKT residual、原域行乘子、`B z`、`Pz-z`、真正
`gdot` 和全部 trial。每档另保存实际保护点 beta²，但不把它替代原域检查。
约束只属于优化方向，精确受限驻点也不是原 BVP 零点。

`direction-XX.json.gz` 保存实际使用的完整 scaled/coefficient 方向，供失败
后只读重构，不保存一个未投影向量冒称实际方向。这些原始 Actions 数据
允许超过 Git 单文件发布限；出版策略不能使数学运行提前失败。

若有真实下降，保存 `warm-001.json.gz`，含全部699个 augmented 状态/RHS、
真实 p 序列化、父 warm SHA、完整新旧 producer ledger、实际 H 和保护点回执。
它仍 `success=false`、`new_coupled_finite_acceptance=false`，没有自动调用
native。成功退出只表示保存了合法下降 warm。

若未取得原标准下的实际下降或发生异常，保留完整状态/失败原因，不造 warm。
后续若从本算法保存的 warm 再开一模型，必须显式给该真实输入 SHA，完整
producer 与相同 scalar/mesh 身份继续核验。

## 3. 对新 warm 重新运行原完整边界 FD

```sh
python computations/geometry_20261114_protected_tangent_response.py \
  --accepted "$ACCEPTED96" --prepared "$FRESH_OUT/warm-001.json.gz" \
  --tail-anchor "$COMPLETED_ZERO112" --tail-config "$CONFIG112" \
  --out "$FRESH_FD_OUT" --angles 4096
```

这是原完整 Rphi 三步差分 / Richardson / `5e-5` 门的实际新执行。新 schema
不冒称旧优化器产物；报告绑定新 warm 真实 SHA，消费源账同时列出冻结原
FD 源体与新入口。既有完整 full-DN 入口可以消费此报告，但仍须实际求解
新 H、完整外层/内层、原 RMS/BC 与最终 fresh audit。

此次受保护 warm 尝试和独立 native cold-start 探针可并行；不能把任一项的
成功当作另一项已完成。没有完整接受场之前，不进入已接受同 g 精化或闭面
幅度收尾。
