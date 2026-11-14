# R76 独立审查

2026-11-12，reproduce_newton。完整读取 R76 正文及其有向预算源码，并核对 R69 中旧复矩阵模数的构造。未发现实质数学或实现缺口；本次没有重新运行整段几何证书或重复 R69/R74 大计算。

## 冻结身份

- results/R76-actual-weighted-exterior-robin-and-mean-preserving-positive-inverse.md：SHA256 f86111528fce63c398f75b9891f8105ba6198661f9e15fb71c78a9fa61a77275，19725 B。
- scripts/fourfold_phase_weighted_exterior_robin.py：SHA256 eccac6190c801bddea6afec4d401085fa113c8adc8aee4c5e09eea24e8888d16，10825 B。
- notes/2026-11-12-actual-weighted-exterior-robin-certificate.json：SHA256 a5e33d55ca33532fef000cfd46e40c964fdfd904fe466dc5b280d1160dd30f05，15928 B。

## 关键核查

1. 真实复角流的首次出管证明保留了实轴改进界。bootstrap 管宽 σ₀/20 给指数 I_r+I_c/19，实际像落到 σ₀/40 后，Jacobian 及逆的指数收紧为 I_r+I_c/39。其辐角界与 μ=49/(50M)、扇形斜率 10/49 相容。没有使用一个未经证明的同宽复逆角图。

2. 边界算子是 C_H* |D| C_H；在真实测度下确有两个密度 H′(x)H′(y)。据此核对差核的两阶和一阶极点均消去，对角常数为 (2/3)H‴/H′−(H″/H′)²+(H′²−1)/3。近对角梯形余项给出的 M₂²+(2/3)MM₃ 与分母 μ² 正确。远离对角时，短弧与补弧同时使用 Re H′>0，才得到折回后的 |a|≥μd 及 |Im D|≤|a|/4；正文已保留这一步。差核乘法项和积分项各付 M_K/2，完整 L² 费为 M_K。

3. 真实 Robin 余项没有被省略。稳定线有理项在零模准确为零；双密度拉回后的 resolvent 核由完整 Poisson 积分得到。q≥1/2 的积分产生可积对数界，q≤1/2 部分的 8/b₋ 有余量。真实尾的 2⁴⁵ 因子包括正负模与 m=4j。误差 E 的全 Fourier 级数在已付共同复平移域绝对收敛，不能误读为任意两个独立复角变量的同宽界；正文已经明确仅需共同平移。

4. Fourier lag 交换估计使用算子值投影，而不是把每个矩阵元的界直接相加。固定 lag 的矩阵是一个移位乘对角块，因此乘上有界的权比差确能按其 supremum 控制该 lag 的算子范数。两种指数的 Lipschitz 常数≤1，正负 s 和截断权均满足同一差界。边界主项 c₀|D| 准确交换，归一边界余项的两条 trace 只产生 C_t。

5. 物理均值运输是必要且准确的。ℓ_s(e)=ℓ(e)=1，T_s v=v−eℓ_s(v) 将 X 双射到 ker ℓ_s，逆为 z−eℓ(z)。在固定空间上的 trial 使用 T_s，test 使用 T_−s，因为实际 test 是 W_s w。该正负号与 b_s(v,w)=b(W_s⁻¹v,W_s w) 一致。运输差费和形式差费给 N*=2N₀+3M*T₀，Neumann 门没有假设角权保持原物理平均。

6. 全 Poisson/source/contact 估计保留真实平均通量 λ₀。test 延拓 E_−(h)+eη 的 ℓ_−s 恰为 η，故 contact 不是人工零均值投影的输出。常数角模的权为一，原均值 pivot 可以保留；它只提供一条与中央系统相接的关系，不能删除全局均值行。负权使用 Fourier completion 与对偶配对，正文没有把所有负解析权元素当作普通分布。

## 有向实现与范围

R69 的 complete_positive 源确以 Mc=Mphysical·Jc 构造旧复矩阵模数。新预算使用旧分子上端点除旧 Jc 下端点，再乘新 M，因此 R76 的这一步不是从一个无关系的旧上界反推真实物理系数。

源码逐项核对两个输入的 origin、direction、准确参数区间及关联 SHA；所有范数上界、正性下界、Neumann 比率都沿安全方向计算。first_moment 用 expm1 支付小宽度差分；完整无限尾仍以非零 Arb 球参与。实际选定 |s|≤2⁻¹⁰⁰ 的范围与两种角权、两种符号一致。

本次通过只授 R76 显示的能量/trace/contact 角权接口。实际 far-bump 选择的参数连续性、高阶径向窗口、中央反馈逆、全局非线性收敛、reach 与可见幅度仍未由本篇解决。

