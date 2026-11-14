# 同一完整内头的真实 cut 高读出：physical 源与 canonical 初值列

作者：exact_closure（GPT-6 Astra Pro；AI 辅助），2026-11-13。

## 实际结论

不改变 R100 已存在完整解、原六个复积轴单位域或 transverse 共同 ℓ¹ 半径 1/32，以真实 cell13 场作为 cell12 初值，重新消费原保存正传播数据。真实 τ_b 头条带上，与旧 R100 `617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9` 完全相同规范的三带质量为

\[
q_{94..184}\le4.126008334895\cdot10^{-61},\qquad
q_{186..8190}\le4.361260926424\cdot10^{-56},\qquad
q_{8192..\infty}\le2.031027433060\cdot10^{-69}.
\]

near 帽比前一 whole-cell12 读出的 1.075735e−54 显著收紧。rest 使用同场旧帽与新端点帽的 min，infinite 保留前一完整同点正帽。全部 mean/逆、真实 far 与所有频率仍被覆盖；这不是外段 cut 已闭合的声明。

physical endpoint 运行正式退出0，34.5705425739秒/42968 KiB；它单独没有改善旧帽，完整失败预算保留。canonical 交叉消费正式退出0，0.8397634029秒/42548 KiB，主输出 SHA256 为 `5741ce64f40e252c7b568bc8be61ae14695a41faf6fbaa3cbac13eaab5c9a5c9`。没有重跑 ODE、Green、径向积分或 scalar endpoint 计算。

## 实际场、初值与源的分解

前一完整非线性641包已给同一 F=C_S+Λd+e 的所有原坐标帽。cell13 的 near/rest 共同 strong 质量分别为 r_N,13、r_R,13。它们包含从全部更深胞元进入的真实源及同一 R18 far 影响，不能把更深贡献删除；同时也不把已经包含的那些源再次沿全头积分。

cell12 的完整源分成已付 N(C_S+Λd) 两种材料源，以及完整 e 变化。后者保留准确中心二次支撑、完整 Q(e)、mean/逆 T 和真实场依赖。source 使用前一步已付半径，初值可使用最终较紧半径，因为两种帽同时约束同一实际场。

V′=S Vs，S=257/256。旧 q panel 的 physical 包络记 V_q，Vs=σ_n V_q。所有 1873 个 cell12 panel、1975 个 cell13 panel 都按原九段顺序和精确有理端点核对；V′13(boundary) 由最后一个真实 cell13 panel 向上界控制。初值 frame 改变付 max(1,B12/B13)。原 τ13,outer→τ12,inner 不增宽，既有下降不重复收费。

## 已存 physical 正传播的 endpoint 消费

对每个有限窗 [lo,hi]，沿用原 R55 两材料 producer 的递推

\[
H_{next}=e^{q\,down-lo\,J_{lo}}H_{old}+emitted,
\quad q=\max(0,1-lo/B),
\]

及原每 panel 的 d1、dℓ 发射上界。唯一读出变化是保留终点 H_end，不再取整胞元的径向最大值。于是两材料真实 cut 源列为

\[
K_{i,end}=\frac{2(1+hi)(S\sigma_{12})^2H_{i,end}}{w_b},
\quad i=1,\ell.
\]

这直接输出物理 balanced P/K；源重权为 (Sσ12)²，不能再除目标 σ 或 V。初值已经含 strong 权 1+m，故其列为

\[
K_{in}=\frac{2\,jump\,G_{end}V'_{13}(boundary)}{w_b},
\]

没有额外 1+hi。因子2保守支付两个物理分量。原严格正 w_b 下界与同一真实 r、μ 由保存 R61 cut 包绑定。

finite near 的五窗和 rest 的七窗完整覆盖各自全部正偶频率；对一个 band 的共同初值质量和共同源质量，在相应列上取窗最大值。不能把每个窗都视作一份独立 full-band 初值。完整 inverse/mean 余项在所消费的每一共同 source 预算中仅付一次。

单独的 scalar 初值列在 near 上过粗：原 lognorm 的 G_end≈1.17e15，给 incoming≤5.679633e−45，反而大于旧 whole-cell 帽。因此该计算 formal0 只代表所声明的真实正上界已计算成功，不代表改进门通过；原数字和资源全部保留。

## 原 canonical 正矩阵的初值列交叉

原 `closure-positive-highband-38` 保存 cell12 的真实正矩阵 A，坐标为 (Q,Ξ12/ν)，ν=m²(m²−1)/12。其尚未付胞元角宽损失。当前初值从同一点的物理 (B12 p,κ) 直接逆变换，因此不另乘 cell13→12 的 canonical ρ；出口也用 μ12 转回物理，不换成外侧 μ11。

令 r_c 为原 ready 的准确二进制 rCuff，R=257r_c/256，w_in≤μ12,hi/r_c^7。对共同 physical strong 初值 H，先除以 1+lo，canonical 两列可用

\[
c_{in,Q}=\frac1{B_{lo}\,lo\,r_c^3},
\quad
c_{in,\Xi}=\frac{R^4 w_{in,hi}}{\sqrt{12}\mu_{lo}\nu_{lo}}
\max\{1,hi/B_{lo}\}.
\]

后一个 max 正是共同 |κ|+|Bp| 质量的线性变换费用。A 后乘实际完整条带损失 exp[−lo(τ_inner−τ_outer)]。物理输出两权为

\[
c_{out,Q}=(B_{hi}\,hi+hi^2)R^3,
\quad c_{out,\Xi}=\frac{\sqrt{12}\mu_{hi}\nu_{hi}}{r_c^4w_b}.
\]

再付 (1+hi)/(1+lo)、2 jump V′13(boundary)/w_b 即得 canonical 初值列。所有矩阵只在其原覆盖窗及子窗内使用；没有 cell12 canonical 矩阵的最上两窗保留独立 physical 列。对每窗取两条有效初值列的 min。

geometry_audit 独立核对了原 A 的坐标、μ/ρ 约定、首尾角宽方向、输入与输出 strong 权比，以及上述所有转换。全部算术采用 Arb256，有限/严格正分母逐项检查，输出向上160 bit dyadic。

## 最终正分账与剩余用途

near 最终界为新 canonical incoming，加原两材料完整参考源与完整 e 源；其主导项是完整 e 源约4.126004e−61。参考源约3.902176e−69仍保留。rest 新 endpoint 总界较粗，故最终仍使用旧已付 whole-cell 帽；∞全部保持旧完整帽。没有从舍入后的总量中相减任何项。

这说明 next 必须继续保留 near94 与 near96 的真实频率支持、rest 子窗质量或更紧参数域，不能把 scalar formal0 或这条 near 改进写成全部曲面完成。小 export 已提供原规范 exact 三带、参数域、头条带、primary/resource SHA 与 complete mean/inverse/far 门，供外段同场有限代入直接消费。
