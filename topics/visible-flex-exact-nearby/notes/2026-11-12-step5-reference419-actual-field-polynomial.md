# δ5 / segment 419 主 germ 的完整连续场多项式包

## 已完成结果

已经真实运行并完成同一个准确 δ5 图、segment 419 主 germ 的连续场近似。对象参数为
\[
\delta_5=-7789843107295549/4611686018427387904,
\]
准确时间端点为
\[
4466727694628647/9007199254740992,\quad
282639970307159/562949953421312.
\]
\(\tau=\tau_c+hu\)，\(|u|\le1\)。所选径向 germ 是
\[
[8173936700574847,\ 8286623314361713]/72057594037927936.
\]

真实场是 \(f=d\theta/d\tau\)，所选分支 \(\sigma=-1\)。它使用真实无穷角原函数与同一目标 \(E,K\)，并有完整有向预算。有限 \(P\) 的定义与系数保存证明见
[exact-field-polynomial-preservation](2026-11-12-exact-field-polynomial-preservation.md)。

对物理角带 \(s=81/10000\)，得到
\[
\sup_{|u|\le1}
\left\|\partial_\theta^q(f-P)(u,\cdot)\right\|_{\mathcal A_s}
\]
的以下上界。这里 \(\mathcal A_s\) 为频率 \(4k\) 的加权 Fourier 绝对和范数，因此也控制该带内逐点误差。

| 物理角导数阶 \(q\) | 节点与 DFT 误差 | 完整混叠 | 真角频尾 | 全部遗漏时间阶 | 总误差严格小于 |
|---:|---:|---:|---:|---:|---:|
| 0 | \(3.009\,10^{-35}\) | \(1.449\,10^{-35}\) | \(1.247\,10^{-21}\) | \(2.213\,10^{-23}\) | \(1.269\,10^{-21}\) |
| 1 | \(2.130\,10^{-31}\) | \(1.038\,10^{-31}\) | \(9.144\,10^{-18}\) | \(2.941\,10^{-21}\) | \(9.147\,10^{-18}\) |
| 2 | \(1.508\,10^{-27}\) | \(7.426\,10^{-28}\) | \(6.710\,10^{-14}\) | \(7.816\,10^{-19}\) | \(6.710\,10^{-14}\) |

本表各项均向上舍入；完整 Arb 球保存在报告中。主导项是真角频尾，不是原函数的节点误差。第零时间阶的完整保留 Fourier 系数噪声为约 \(1.35212\,10^{-62}\)，第 52 阶约 \(1.69934\,10^{-91}\)。

## 有限对象与预算参数

- 实物理角采样点 \(N=4096\)，保留 \(|k|\le1800\)。
- 保留时间阶 \(0,\ldots,52\)，共 53 个系数。
- 原函数 quarter FFT 为 1024 点，工作精度 320 bits。
- 独立联合解析域为 \(|u|\le3,\ |\operatorname{Im}\theta|\le1/64\)。
- 此 germ 的真实场外域模数 \(M<4.303428\)。
- 保存 \(P\) 的 14 个 gzip 分片总计 **8,496,113 bytes**，最大单片 683,933 bytes。
- 所有准确 dyadic 系数、分片 SHA、字节数、形状和完整时间覆盖均已重新读取通过。四个独立直接 Fourier 求值节点的全部保留 \(f\) 系数也与批量结果相容。

实际运行用时为 wall 274.1034 秒、进程 CPU 56.5652 秒。wall 时间受同环境并发影响；该单次结果不构成全分支一小时可完成的结论。有限场整圆求值阶段 wall 173.0003 秒，保存对象所用 DFT 为 8.2816 秒。

## 固定输入与输出身份

| 文件 | SHA-256 |
|---|---|
| `scripts/fourfold_phase_actual_field_fourier_package.py` | `c5198dcc172d4c2ef271370d4fc9b1bf39c749f20e04835e4c39cccf7498734a` |
| `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json` | `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848` |
| `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_root_tight.json` | `489268d254c2a9454ccbee32a4821d9bf577279490f76c9cc6f8d902a5e64e0b` |
| `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json` | `e1a2c3f327c3a36e33c412e76c70eebd185f224ea938dcdea93ee30ab9a05f90` |
| `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_main_actual_field_fourier.json` | `b8990af160ac31055cd8afe9118706e297bdb2578398a069191b418df67744a7` |
| `data/phase_ring_continuation/step5_reference419_main_field_polynomial/manifest.json` | `4b33966313c4fdde253ffca05d21a49692186d8263f9f7f069804632b22b6613` |

其余实际源码依赖的完整哈希在数值报告中；每个精确系数分片的哈希在 \(P\) 的 manifest 中。精确重跑命令在保存证明笔记第 5 节。当前已完成的新报告与旧执行器中断的摘要作业严格区分；没有恢复或冒用旧作业的“完成”状态。

## 对后续工作的直接用途和限制

`load_polynomial` 可直接读回准确有限 \(P\)，供构造／修正非均匀参考的 \(P(u,Y(u,x))\) 使用。因为 \(P\) 已保存成准确 dyadic 对象，未来的有限复合误差可以与本报告的真场近似误差分开付费。

当前只授予主 germ 的解析外延。此时间段实际还与另外两个共同 span 相交，它们所负责的短时间子集仍须用各自 germ 或有证明的差分补偿覆盖。这里没有把主 germ 的 \(P\) 当成完整 piecewise 实际场，也没有授予完整流误差、返回映射残差或 PDE 完成结论。

