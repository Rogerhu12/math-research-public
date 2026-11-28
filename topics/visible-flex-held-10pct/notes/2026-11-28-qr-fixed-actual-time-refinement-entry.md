# 新 QR 固定完整度量场的时间精化诊断入口

**可信度：可执行来源准备；未有真 fixed 输入，因此无新数值结果。** 本条为 README 第5项补独立的时间离散入口，不把增加采样点数本身当作等距误差下降，也不代替全部时间、全部空间的连续证书。

## 固定对象和近似族

新源 `scripts/resume_20261128/analytic/qr_fixed_actual_time_refinement.py` 的 SHA256 是 `231a6726b6c4d3aecd4767dbcedd97889f3272a76f5407e8d9bf3fe57aad9364`。它只通过已发布 `qr_fixed_actual_cartesian_prefix.accepted_fixed` 读取真实 own-KIND fixed-g 结果，再由原 `load_closed_map` 读取完整尾、最终 physical-H、全谱、全部共享两jet和有限均值。所有时间层使用同一个源、同一物理目标度量、同一完整几何定义、柱长、规范R67帽、cut-width、握持区和明确有理相位区间。没有再求 BVP 或 native，没有按时间层删 Fourier 模。

在每个固定材料点 $p$，取同一时间网格 $t_i=i/n$，对真实握持坐标中的 $F_{t_i}(p)$ 使用 `CubicSpline` 的 not-a-knot 线性插值算子。该算子的系数只依赖时间，因此对空间求导与插值可交换：程序对位置、一阶和二阶的全部六组三维 jet 应用同一算子，所得一阶导数确实属于同一个时间插值曲面族。它没有以另一套无关差分导数计算度量，也没有宣称插值族已经通过嵌入/reach门。

默认时间间隔数为8、16、32、64；必须严格递增并嵌套。所有层与原实际有限场均在同一个严格更细的时间网格上比较，默认其分母为最大层的4倍。材料站点固定，覆盖上下前缀、正柱、切口邻域、完整尾、deep collar及规则Cartesian盘/极点；站点只用于诊断，不构成空间上确界。全部时间层都在同一 $[0,1]$、同一 $\alpha(t)=(4/5)t$（运行时须显式传入）中，原准确圆弧/保护窗合同会执行核验。

## 计算的量及限度

在每一站点，目标度量使用原物理图：前缀 $\operatorname{diag}(1,a(s)^2)$，尾部 $\operatorname{diag}(1+w(R)^2,R^2)$，Cartesian帽为 $I+df\otimes df$。对第一导数矩阵 $J$ 使用该目标的Cholesky归一，报告 Gram 缺陷的算子范数。各层另给位置、一阶、二阶 jet 对原有限场的差，以及相邻层完整两jet差。

原有限场的采样等距误差下限单独保留；时间插值误差趋小不表示该有限场已等距到零。各层误差是否下降由实际数值报告，不强制写成 true，也不覆盖不单调结果。报告明确 `global_metric_certified=false`、`reach_certified=false`、`C2_limit_proved=false`、`readme_completion_claimed=false`。还须对同一最终场完成真实空间/频率精化和全时连续误差、几何证书；有限采样本身不支付这些义务。

## 真实执行检查和后继命令

本次只实际执行 `py_compile` 与 `--help`，二者 exit0；运行回执见同名JSON。没有真实完整 fixed 场可用于阳性诊断，未构造替代场或重跑旧1152尾段。科学数组及完整运行报告仍只在 scratch。

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/qr_fixed_actual_time_refinement.py \
  --source-run "$ACTUAL_FIXED_RUN" \
  --geometry-bundle "$ACTUAL_FIXED_COMPLETE_BUNDLE" \
  --phase-end 4/5 --held-width 27/50 \
  --cylinder-half-length 0.0025 --cut-width "$ACTUAL_FROZEN_CUT_WIDTH" \
  --intervals 8 16 32 64 --outdir "$NEW_TIME_DIAGNOSTIC_DIRECTORY"
```

柱长和cut-width必须使用后续真实选定并冻结的值；上式的0.0025仅是显式调用示例，不替代该选择。实际执行后按同一个固定问题继续加密，不能换源或参数来制造下降。
