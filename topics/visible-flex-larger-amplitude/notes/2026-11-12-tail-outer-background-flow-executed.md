# 实际外头 m2/m4 背景列：两胞元完整流与区间表示修复

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

## 1. 实际结果及范围

同一个 R26 真实背景、同一份 node12 完整 46 模真实线性列、固定全程 $\mu_*=\mu_{11}$，模式 $m=2,4$ 已经过外侧胞元 11、10 的全部 **10,793 个面板**。正式 session 25589 的资源记录为 exit code 0、无 signal、35.508020 秒、峰值 29,208 KiB。最大正 Peano 积分乘积小于 $3.498\times10^{-7}<1/64$。

两个模式在 node11 和 node10 的真实高度分母区间均排除零。下表是主包精确 dyadic 端点的保守小数显示；单位是 node12 的一个 canonical $Q_m$，物理高度不是 $Q_m/w$。

| 外向终点 | $m=2$ 的物理 $H_m/Q_m(\mathrm{node12})$ | $m=4$ 的物理 $H_m/Q_m(\mathrm{node12})$ |
|---|---:|---:|
| node11 | $[-11.368,-1.1502]$ | $[-379.04,-14.298]$ |
| node10 | $[1.0280\times10^5,2.1678\times10^7]$ | $[1.2884\times10^7,3.1066\times10^{10}]$ |

这只支付两个模式、两个胞元的背景列；不是完整 46 模外 cut 的 Schur 逆，更不是非线性外头解。保存包同时包含两条独立基列、其基本矩阵、精确 determinant-one 恒等式的区间相容检查、完整 projective 恢复状态以及连续胞元上背景列的物理帽。

## 2. 先前失败与准确修复

首轮 session 39389 使用未修改的 `tail_outer_background_column_flow.py`，在 cell11、segment3、panel0、$x\in[0,1/16]$、$m=2$ 正常退出：exit code 1、无 signal、3.941638 秒、29,592 KiB。原源、失败位置、输出和资源记录全部保留。

原算法直接对宽正区间作多个 Arb 球乘法。该面板的 $r,w,\Delta r$ 都严格正，但 $B$ 的对称球包围延伸到负数，从而触发“正积分 range 失正”检查。以同一输入的单调端点计算，$B$ 的真实下界仍大于 $0.1182$，上界小于 $230.039$。这不是真实流的奇性。

独立适配器 `tail_outer_background_positive_endpoints.py` 对下列**原积分**只改变区间求值方式：

$$
A=\int\sqrt{12}\mu_*\left(\frac{r_c}{r}\right)^{2u_m}r^{-8}\frac{dr}{w},
\qquad
B=\int\frac{\nu_m\sqrt{12}}{\mu_*}\left(\frac r{r_c}\right)^{2u_m}r^6w\,dr,
$$

其中 $u_m=m^2-4\ge0$、$\nu_m=m^2(m^2-1)/12>0$。每个因子单调，故分别用正输入端点组成严格正下界与上界，给出同一真实积分的合法包围。如果把这两个端点转回 Arb 对称球时再次出现负下端，适配器使用向上舍入的 24-bit dyadic $U$，以精确 midpoint/radius 元组构造 $[0,U]$。真实积分的严格正性已由分离端点证明；Peano 定理只要求积分系数非负，因此保存球采用零下界完全合法。

适配器逐次检查包围包含两端点且下端非负，固定原源 SHA，保留同一正乘积门、同一面板、同一精度、同一真实 slope 输入和全部列推进。原数学源未被改写。适配器统计及两份源 SHA 在独立 `-positive-endpoints.json` 中，主包和每胞元 checkpoint 也记录全部实际源 SHA。

## 3. 全频齐次能量预算的实际含义

[背景流证明](2026-11-12-tail-outer-background-positive-flow-proof.md) 的同面板计算给所有偶频齐次传播充分界

$$
\|\Phi^{PK}_m\|_2\le \exp(D+m\Gamma).
$$

node12 到 node11 的 $\Gamma<0.081793$；到 node10 的累计 $\Gamma<0.191060$。后者已经超过 R61 的真实 node12 条带与外 $1/64$ 条带之差 $0.128810830748\ldots$。因此，这个具体粗齐次能量界不足以独自承担完整外头的高频传播。它没有给真传播的反向下界，也不构成不存在性结论。

实际全频 Green/Schur 路线仍应保留两点边界和带符号基本列，或进一步支付更紧的位置/材料核。不能将一个不够紧的初值能量界自动替换为已证的无限频率有界算子。

## 4. 机器可读字段与恢复

主包为 `notes/2026-11-12-tail-outer-background-flow-m2m4-11to10-r2.json`。各 `cell_rows[].modes[]` 中：

- `b0_endpoint.Q`、`H_per_unit_shallow_Q`、`global_Xi` 是有符号独立 dyadic 端点范围；`height_chart_excludes_zero` 是实际排零结果。
- `global_gauge_fundamental_matrix` 是从同一个 node12 起、同一个全局 $\mu_*$ 中的基本矩阵，不在胞元交界重置规范。
- `b0_endpoint.projective_state` 与 `basis_states` 保留 pivot、sign、分离共同幅度端点及比值球。它们可用来扩展到更外胞元，而无须重算已经完整保存的两胞元。
- `all_mode_homogeneous_energy` 是上述充分上界，不能当作真增长率。

每个完成胞元另有 `-completed-cell011.json`、`-completed-cell010.json`。目前生产入口尚未提供从这些状态继续的 CLI；后续若加恢复入口，应保留其规范、全部 source SHA、实际节点和已累计能量项。完整执行命令由 r2 的 `-resource.json` 保存。

## 5. 与下一实际缺口的连接

R61 提供完整有符号中心差 $\beta$ 与全部 46 参数导数校正 $\Delta B$。后续外 cut 的参数矩阵应为 $S_0=R\Phi B_0U$，其中 $U$ 是真实 canonical 参数轴；$R\Phi\beta$ 与候选残差的源贡献应先保留符号再作共同参数范数估计。本次两胞元列是该计算的实际输入，尚未把其余十胞元或全部模式补齐。

均值高度的单切口自由平移见[独立说明](2026-11-12-tail-mean-height-translation-and-one-cut.md)。它处理题目没有指定的绝对高度，不替代真实导数接合、完整源核、参数包含或全闭曲面几何。
