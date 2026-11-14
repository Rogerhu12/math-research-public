# 时间场批处理：三个已测但未采用的方案

2026-11-12，root。以下有限节点实验用于定位整圆验证的算术瓶颈，均没有
证明完整角圆或完整真实返回，也不替代原直接场实现。

## 原生多点评价

`fourfold_phase_batch_time_primitive.py` 将保留时间项按 `θ=θ₀+d(u)` 展开，
对每个频率和时间系数用 `acb_poly.evaluate` 同时评价多个 `exp(4iθ₀)`。
16 标签、时间次数 16 的实验：几何准备约 11.80 秒，批评价 14.84 秒；
原直接实现在四个独立标签上只用约 .768 秒。
所有保留系数与直接球相交，但部分场系数半径膨胀到 .358 和 .428。
因此该实现既未提速，也不满足所需精度。报告
`2026-11-12-batch-time-primitive-sixteen-labels.json` 保留了这一失败。

## 普通正负频率 Horner

`fourfold_phase_field_time_horner.py` 仅计算一次 `exp(±4iθ)`，分别对正负频率
作 Horner；有限频率截断的保留时间系数费另用外时间盘支付。
degree128 时 16 场约 3.22 秒，degree192 时约 2.57 秒。
但后者的 f、fθ、fθθ 球半径反而约为 `3.9e−6,.000224,.0284`。
原因是已有输入球误差被多次复矩形旋转放大；这不是实际几何分母出现零。
两个报告 `2026-11-12-time-field-Horner-degree128.json` 和
`2026-11-12-time-field-Horner-degree192.json` 均保留，未将其视为验证器加速。

## 中点 Horner 与独立解析误差

`fourfold_phase_field_time_centered_horner.py` 对系数和 θ 取准确 dyadic 中点，
在额外 160 bits 保护精度下作 Horner；原输入球不确定性另按完整外时间盘计费。
频率 n 的误差由

\[
 e^{nW}\{\epsilon_c e^{n\epsilon_\theta}
       +C_c(e^{n\epsilon_\theta}-1)\}
\]

控制，再按时间 Cauchy 分摊到保留系数。舍去频率及真实无限 primitive 尾另计。
degree192 实测的 f、fθ、fθθ 半径恢复到约
`1.4e−26,1.9e−25,1.95e−23`，但 16 场约 4.404 秒，仍未快于直接评价。
报告 `2026-11-12-time-field-centered-Horner-degree192.json`。

中点与解析误差分离的思想可用于后续整角 FFT，但这三个已保存实现目前均未
成为全圆验证主路线。下一实现需同时实测算术成本和误差传播，并支付真实
Fourier alias、外带、时间余项及非均匀复合，才可替换直接场。
