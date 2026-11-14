# R259 小核心同伦备用诊断接口

2026-11-14。**源码准备；只做 AST 静态检查，尚未运行新数值。当前主线仍是实际 request17 的下降 warm、真正新 H 尾与原 full-DN。本文不触发另一个 Actions，也不把备选研究变成主线的附加验收门。**

完整条件推导见 [R259](../results/R259-small-core-homotopy-and-resonance-conditions.md)。新独立源为 [small_core_resonance](../computations/geometry_20261114_small_core_resonance.py)，不改已发布的 trust/物理角/带状求解器。

## 实际对象

输入严格绑定原 accepted96 `b4d2b98a…`、M112 原699准备 `0f94dd88…`、真正完成的 T112 零尾/J `e788a28d…`、配置 `01930f3b…`。全部 SHA 与 trust 入口同一组。源保持当前 complete scalar 公式和三个 prefix 支撑，只把候选控制 $p$ 明确作为诊断输入；没有移植旧A的 scalar 或成功身份。

在圆子空间用原 `q=ap/a` 构造实际 collocation：每个半径 cell 是一个可直接消元的1×1线性方程，完整均值高度用同一个原 Simpson 规则累计。低三模使用实际 node/mid 半径及 $W=\sqrt{1-(qR)^2}$ 的2×2原线性化块。它既不以理想连续圆的采样值冒有限解，也不使用独立 app 当有限 Gauss 半径的导数。若一个被消元块不可逆或传输非有限，报告此实现失败，不能推断完整 BVP 不存在。

## CLI 与成本边界

需要与原主线相同的 NumPy/SciPy，以及已有 operator lane 使用的 `python-flint`。默认仅评估给定控制，不搜索、不启动 Node：

```bash
python computations/geometry_20261114_small_core_resonance.py \
  --accepted "$ACCEPTED96" --prepared "$ORIGINAL699" \
  --tail-anchor "$TRUE_ZERO112" --tail-config "$CONFIG112" \
  --parameters 0 0 0 --newton-steps 0 \
  --interval-bits 160 --interval-depth 14 --out "$OUT/resonance"
```

同一入口的 `--newton-steps 8 --backtracks 12` 可选择一个显式有限的候选搜索，但仅在**实际读出的完整 J 严格对角且三个目标都非零**时执行。该搜索求三条单位 transmission 条件；每次真实候选重建整个圆 collocation 和三个模态，按真实低维残差的方向斜率回溯，不修改原任何 full-DN 门。它没有自动触发后续非零 $\lambda$ 求解。

这不是新的全 Jacobian/带状分解任务：每个控制评估只用699个1×1块和三个2×2链。默认额外付九个原完整 FFT 方向核对及一次完整 node/mid/RMS 域读出；不重新计算真零尾、不调用新的 native tail。实际耗时仍待首次 Actions 回执，不预报为已测速度。

## 输出与范围

`resonance-status.json` 保存完整真实 J 的非对角数量/大小、全部112条首阶右残差、低三模传输轨道大小/重代回残差、小块条件、3×3参数响应及三档独立实差分。即使非对角很小也原样保留。若非对角耦合存在，默认输出真实高行泄漏，明确高自由 core 的 Schur 消元尚未计算；不把低三行零当完整首阶条件。三个目标中有零时也不把其单位共振强加为一阶必要条件。

`complete-scalar-domain.json.gz` 用完整 scalar descriptor 和 Arb，对所有原分片、控制支撑、Gauss phase/clip/mask 分界覆盖 $a>0$ 与独立返回 ap 的绝对值小于1。它针对同一声明的实函数表达式，包含完整三个 $p$，不是节点采样界；普通 binary64 运算误差、有限 Gauss 半径与 ap 的真导数关系、C² 分片接缝和实际圆半径 $R$ 的全域 Frenet 条件另记为未由此证书支付。不能把它冠名为整面 metric/operator 证书。

`circle-reference.json.gz` 保存全部699×453状态/RHS、完整均值高度、实际 scalar 规范及全部三个单位低模轨道。固定目标在这里明确为零，`success=false`、`new_coupled_finite_acceptance=false`。它不是一个非零小幅完整 parent。该场另经原完整 FFT、原 Hermite 中点、原 RMS 查询和九个真实 complex JVP 回读，误差如实保留。

所有候选阈值、数值奇异值和可选搜索都只作诊断。尚未证明高模式非共振或3×3区间 transversality，尚未求出实际非零 $H$ 的尾。若这条备选被采用，必须从实际候选另造明示的非零 $\lambda$ 全场初猜，再通过原完整场/FD/真实尾/RMS/BC/最终 audit，逐站续到目标幅度。直线的三个首阶共振不排除 $(\lambda,\lambda^2,\lambda^3)$ 等其他路径；后者需要对应完整非线性阶数的条件，当前入口不计算它们。
