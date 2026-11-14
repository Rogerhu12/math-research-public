# R106：完整七场有限源核与准确尺度校准

2026-11-13，constructive-route。

新源 scripts/fourfold_subprincipal_root_regularized_fft.py 读取已执行完成的
seven-field Fourier 报告，逐项验证对象、根证、source/dependency 和全部
coefficient shard SHA；尚未有实际候选输入可供本源运行。

它输出同一个实际正根的完整有限数据：

- 正则一形式密度 $\mathcal R_\sigma+\partial_\theta S_{\rm reg}$ 的偶 $s$ 部分；
- $s$ 乘一个 $\rho$ 多项式的奇 $s$ 部分；
- cut 的 $s^{-3}$、$s^{-1}$ 与普通三部分，已准确合成 $B-V_\rho/4-\sigma L_\theta/4$；
- 根端 $\sigma L_\theta(0,\theta)/4$，仍须乘真 $J_0$。

所有角卷积用充分 zero-padding 的完整 acb DFT；保留到真实支持和，
无输出频率截断。中间球包围完成的有限表达式，再选准确 dyadic 中点，
完整 finite arithmetic Wiener 费另计，不和真实输入误差混为一项。
径向 scale 与物理 $\theta$ 导数 $4ik$ 均显式保留。

有限输入误差使用 seven-field 报告已经支付的较小 bidisk，而不是只有
真实模长界的较大 bidisk。两次角损失在其中分配。程序从实际根证读取
整个参数盒的 $\rho_c=t(p)-r_{\rm cut}$，用 $c_{\min}$ 支付所有负次幂，
用 $c_{\max}$ 与其平方向外包住实际正则源圆盘。它没有以 cut 中点替代
真实 cut，也没有支付后续若选有限端点位置时的额外误差。

准确代数校准已实际在 V8 BigInt 执行：

    scripts/fourfold_root_seven_scaled_identity_exact.mjs
    notes/2026-11-13-R106-seven-scaled-identity.json

六例使用 scale $1,1/1024,3/8192$ 与两种实际支符号，对完整
Laurent 多项式逐项比较直接
$G/s^4-\partial_sB-\partial_\theta(vB)+\partial_\theta S_{\rm reg}$
和缩放后的七场核公式，全部相同。故意漏掉径向 scale 因子时，
四个非单位 scale 校准均检测到非零缺陷。
自由 Tricomi 的完整 cut 系数准确为 $-5/48$，包括不可删的 $V_\rho$ 项。

这六例没有实际几何数据，也没有执行 native FFT。它们证明/校准的是
有限代数与归一化，不是候选七场值、整个真射线积分或 R104 cutoff。

有实际 seven-field 输入后，在课题目录执行：

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python scripts/fourfold_subprincipal_root_regularized_fft.py \
      data/R106/root_seven_field_first_layout/report.json \
      --sigma 1 --working-strip 1/800 \
      --out-dir data/R106/root_regularized_complete_first

源可以输出完整合法但过粗的费用；complete 不等于 R104 已可用。
实际积分还需要同一参数、同一标签的全时拉回及两个根/严格区的完整接线。

当前使用普通全时 $e_J$ 乘根大密度会过粗。后续接同一个 $g_0$ 缺陷坐标
的二阶一形式拉回，以有符号有限时间积分保留主修正。旧 endpoint 的
omitted_local_J 预算使用完整对称时间区间的奇偶相消，不能当作任意部分
时间的局部误差。该步会保留完整局部时间多项式，或另付部分时间预算，
不会把终点证书静默推广到叶内部。
