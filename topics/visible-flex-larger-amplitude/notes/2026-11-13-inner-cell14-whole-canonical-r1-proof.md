# Cell14 原完整 canonical 矩阵的真端点读出

作者：geometry_audit（GPT-6 Astra Pro，AI 辅助），2026-11-13。

本件只使用原 `positive-highband-38` 的 cell14 正矩阵、R42 的同对象完整强包络、原 ready 的半径/端点 w 公式。没有保存的 cell14 continuous-strip panels，因此不声称逐片精度，不重做 ODE、径向积分或源场求值。主包 SHA256 `9b9e07878503a05fdce7efa5141b7689035bfaa2b2e9aa3313e09beb5d9e010c`，producer SHA256 `2b10e184e1b104b3beb3a9139f2c7b0f3c1b21fce9fcecfa994de62f0baa9a4c`；实际正式 exit0，0.5104秒、31,528KiB，46门。收益需要实际完整场消费者判定，核本身不证明 truecut。

## 规范

当前胞元为14，输入在 cell15 外端。原连续宽满足 `tau15_out=tau14_in`，程序准确核对。输出在 cell14 外端，尚不是最终 cell12 cut。输入绝对强量为

\[
H_{15}=\sum_m(1+m)e^{m\tau_{15,out}}
(|B_{15}p_m|+|\kappa_m|).
\]

当前 frame 的 `|B14 p|+|kappa|` 由 `J=max(1,B14/B15)` 支付。原变量为 `Y=(Q,Xi/nu_m)`、`nu_m=m²(m²−1)/12`。真实输入 w 使用 `closed_port_w(ready,15)`；真实输出 w 使用 `closed_port_w(ready,14)`。mu 用当前 cell14 的常量，不能将其误换为输出节点归一的 mu13。

所有物理半径使用已付全局 `rC<=r<=R=(257/256)rC`。对窗 `[lo,hi]`，输入两分量分别受

\[
c_{in}=\left(\frac1{B14_{lo}\,lo\,rC^3},
\frac{R^4w_{in,hi}}{\sqrt{12}\mu_{14,lo}\nu_{lo}}
\max(1,hi/B14_{lo})\right)
\]

乘弱 balanced 量控制。输出转换行向量为

\[
c_{out}=\left((B14_{hi}\,hi+hi^2)R^3,
\frac{\sqrt{12}\mu_{14,hi}\nu_{hi}}{rC^4w_{out,lo}}\right).
\]

若 A 是覆盖该窗的原正矩阵，绝对强输入到绝对强输出的列为

\[
K_{abs}=2J\frac{1+hi}{1+lo}
e^{-lo(\tau_{14,in}-\tau_{14,out})}\,c_{out}A c_{in}.
\]

原因子2保留，整胞元条带损失只用于从内端传入的量。`input_absolute_mass_to_cut` 再除真实 w_out。94 与96继续共用原 `[94,96]` 矩阵；13个新窗中只覆盖前11个，末两窗和无穷带保留原核。

## Cell15 完整规范包络

由原 R42 density 各胞元行的真实字段构造

\[
V^{max}_{strong,n}=\overline X_n
\left(a_n R^3+\frac{\sqrt{12}\mu_{n,hi}}{rC^4w_{n,min}}\right),
\quad V'=\frac{257}{256}V_{strong}.
\]

这是完整胞元包，故合法控制其外端值。程序实际得 `Vprime15_upper≈3.21925500451e−50`。字段 `input_cell15_Vprime_mass_to_absolute_endpoint` 为 `K_abs*Vprime15_upper`；对应 cut 字段再除真实 w_out。它将先前的归一全场帽转成绝对点态输入，没有把一个上界当成点态下界或倒置不等式。94对应列约8.38995759559e−41，绝对输入列约2.60617987200e9；数字大小不代表可删除该项或保证有收益。

## Cell14 完整两材料源

本件直接使用 R42 强 V，不是旧 q 包络，所以只需额外 S²，S=257/256；不再付或省略 sigma 比例。原物理 kappa 源材料仍为

\[
d_1=V'^2/(rw),\qquad d_\lambda=|w_r/w|V'^2/w.
\]

由 canonical 转换 `r^4*w/(sqrt(12)*mu14)` 和原 density 的完整 `normalized_width_upper`、`TV_log_w_upper`，分别有

\[
I_1\le\frac{R^4(V^{max}_{strong,14})^2}{\sqrt{12}\mu_{14,lo}}
\,width_{14},\qquad
I_\lambda\le\frac{R^4(V^{max}_{strong,14})^2}{\sqrt{12}\mu_{14,lo}}
\,TV_{14}.
\]

其中 `width14` 是原已证 `integral dr/r` 的上界，TV为完整 `integral |dlogw|` 上界。这正是冻结 `tail_r33_middle_causal_box.py` 中完整 own 源公式的两材料分开版本。

原正比较生成器逐点非负，故完整 A 控制所有内部 suffix（见 `2026-11-13-inner-cell12-canonical-forced-r2-proof.md` 的同一原矩阵论证）。每材料绝对输出核为

\[
K_{source,abs}=2(1+hi)S^2
\frac{c_{out,0}A_{01}+c_{out,1}A_{11}}{\nu_{lo}}I_{mat}.
\]

强迫项没有免费乘整个 cell14 的条带衰减。再除真实 w_out 得 `source_two_material_to_cut`；未除的字段为 `source_two_material_to_absolute_endpoint`。源里的 Q、DQ、完整 T、mean/逆等由原完整源消费者另付，两个材料均完整保留。

## 消费约束

组合 cell14→cell13→cell12 时，每段的真实物理端点、相邻 B frame、连续 tau 和单位必须相接；不能把本件 `/w14` 输出直接当 absolute H14。采用 absolute 字段最直接。若已有更紧同对象同单位界，允许逐项取 min；所有 cell14 自身源和 cell15 传入都必须保留。共享窗质量在正列聚合后只支付一次，不能对每窗各花一份再冒作相同质量。

此核只适用于旧 g 的原 R100 全场或已独立成立的较小域；不改变 far、无穷带、mean/逆，也不迁移给 strong 新g。manifest 固定全部输入、源、主包、资源与此证明。
