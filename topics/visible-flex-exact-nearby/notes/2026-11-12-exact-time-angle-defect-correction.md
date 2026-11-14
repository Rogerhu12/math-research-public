# 准确有限缺陷修正：真实单点及连续角弧验证

2026-11-12，root。本文记录已经实际运行的高精度修正，不把它升级为完整返回证书。
对象始终是准确 affine δ₃ 图，输入对象 SHA256
`e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f`。
参考为 `r61_step3_shared_forward/manifest.json` 定义的完整有限 Fourier/Bernstein
函数，取第 419 段的归一时间 `[31/64,33/64]`。所有参考分片和依赖源的 SHA
均保存在输出；缺少可重建分片时必须按原 manifest 重建，不能用下列摘要代替输入。

## 1. 修正定义及其准确端点

写物理时间为 `τ=c+hu`，`−1≤u≤1`，原参考为 `Y₀(u,x),L(u,x)`。
始终保留完整的有限 Fourier 参考函数。第 j 次使用

\[
 Y_j=Y_0+P_j,\quad q=e^L,\quad
 e_{0,j}=\partial_\tau Y_j-f(\tau,Y_j),\quad
 e_{1,j}=\partial_\tau L-f_\theta(\tau,Y_j).
\]

`Pj` 是保存了准确实虚 Fraction 系数的有限多项式；连续角弧版本还含有限变量 v。
生成器以截断 jets 选择近似修正

\[
 \Delta P\approx-q(u)\int_{-1}^u h e_{0,j}(s)/q(s)\,ds.
\]

这只是选择一个有限候选。取各非恒定系数的准确 dyadic 中点以后，对每个 v 次数
及实虚部单独设置

\[
 [u^0v^b]\Delta P=-\sum_{a=1}^{m-1}(-1)^a[u^av^b]\Delta P.
\]

所以 `ΔP(−1,v)≡0` 是准确多项式恒等式，不依赖区间包含零的判断。
两次修正都已另由独立脚本用 Fraction 重加；连续角弧共 128 个实虚端点和全部为零。

没有假设选出的修正是某个 Newton 算子的收缩迭代，也没有由低精度 ODE 解推断
最终精度。每次选择以后，从头计算新 `Yj` 对同一真实无限 primitive 场的残差。

## 2. 重新支付真实场、外域及解析尾

单点源为 `scripts/fourfold_phase_time_defect_correction.py`，SHA256
`b97888c6f4d70d402a8f2ae2be476d0107a48747fcc21a8995618c41b6b74f43`；
连续角弧源为 `scripts/fourfold_phase_time_angle_defect_correction.py`，SHA256
`db724477755627087c43de4e05bc29cd940a706d7803263561491549604a33a8`。
两者均使用已验证的真实根 refinement，而非旧 binary64 根及其参数导数。

角弧设 `x=1/2+i/512+v/4096`，真实 `|v|≤1`；验证外盘为 `|u|≤8,|v|≤4`。
原函数 `Y₀` 在这个外双盘上的完整有限 Fourier 像由旧参考界计算。
`Pj(u,0)` 的所有时间系数直接进入新的中心轨迹；其非恒定角项另加

\[
 \sum_{b\ge1,a\ge0}|[u^av^b]P_j|8^a4^b
\]

到完整外盘像及状态管中，然后重新检查几何分母和解析分支。
不能只用截断后的角 jet 充当原 Fourier 函数，也不能沿用未支付修正幅度的旧域门。

`X_θ=S−JX` 的角递推仍使用真实无限 primitive 的第零角系数；由于修正的时间
次数已大于七次，第零角系数现在保留全部 m 个时间系数，不能沿用原 degree 7
参考专用的前八项。该源确实作了这一更改。其余角项由准确微分恒等式递推。

残差界是保留系数的绝对和，加完整双 Cauchy 余项，再加原参考 `Y₀,τ`、`Lτ`
的角 Taylor 尾。修正是确切的有限双变量多项式，不产生新的遗漏参考角尾。
`qmin,qmax` 也包含完整 L 的角尾。每次还核对全部保留时间系数的
`∂v f=fθ ∂vY` 恒等式；这项重叠检查仅为辅助，连续界来自上述系数和尾。

## 3. 实际结果

单点 `x=1/2+i/512`，192 bits、时间次数 32：

| 修正次数 | 严格 e₀ 上界 | 严格 e₁ 上界 |
|---|---:|---:|
| 0 | 6.598994×10⁻¹⁰ | 1.440349×10⁻⁷ |
| 1 | 1.627749×10⁻²⁰ | 1.440352×10⁻⁷ |
| 2 | 8.940703×10⁻²⁷ | 1.440352×10⁻⁷ |

最终时间 Cauchy 尾小于 `7.07006e−31`；R60 给匹配左初值的物理误差
小于 `1.72058e−30`。完整三次验证耗时约 14.12 秒。
报告 `2026-11-12-R61-step3-time-defect-correction.json` SHA256
`8d876613382780fff1eb918abcd7d9542b63fdf2716f6e28c1c426516a946768`。

连续角弧同样使用 192 bits，时间次数 32、角次数 31：

| 修正次数 | 严格 e₀ 上界 | 严格 e₁ 上界 |
|---|---:|---:|
| 0 | 7.419680×10⁻¹⁰ | 1.622911×10⁻⁷ |
| 1 | 1.060085×10⁻¹⁹ | 1.622914×10⁻⁷ |
| 2 | 8.539827×10⁻²⁰ | 1.622914×10⁻⁷ |

最终 e₀ 尾小于 `8.539826e−20`，已主导总界。R60 匹配左初值的物理误差
小于 `1.644447e−23`。完整三次验证耗时约 226.67 秒。
报告 `2026-11-12-R61-step3-time-angle-defect-correction.json.gz` SHA256
`ea1e956cec4fcb80906f9d953c2f5a77538cfc6db75a7c0ccabe3a91028b4c33`。
两份独审见 `2026-11-12-full-time-outer-and-defect-independent-audit.md` 和
`2026-11-12-time-angle-defect-independent-audit.md`。

## 4. 局部误差与全腿传播的界限

两份报告的 R60 都取匹配左初值，即初始误差为零。它们证明这段真实流与修正参考
的局部误差，不证明从整腿起点进入本段的真实轨迹具有相同左值。
连续整腿必须把前一段 `P_end(x)` 准确传入后一段左初值，或支付实际跳跃。
若在每段独立重置 `P_left=0`，原累计误差会通过跳跃重新进入，不能因此声称
全局误差获得同样改善。第二腿还必须继承第一腿完整的轨迹及参数误差。

本计算确认了有限 dyadic 缺陷修正在真实连续弧上的精度。现有逐弧实现每次约
75 秒，全时间/全圆直接重复的成本过高。后续采用整物理角 Fourier 场的批量构造，
仍须重新支付 Fourier alias、真实外带、复合及所有时间/参数误差。
当前没有完整返回残差、全参数变分或 KAM 通过结论。

重放命令（在课题目录，单线程 BLAS）：

```bash
python scripts/fourfold_phase_time_defect_correction.py --out notes/2026-11-12-R61-step3-time-defect-correction.json
python scripts/fourfold_phase_time_angle_defect_correction.py --out notes/2026-11-12-R61-step3-time-angle-defect-correction.json.gz
```
