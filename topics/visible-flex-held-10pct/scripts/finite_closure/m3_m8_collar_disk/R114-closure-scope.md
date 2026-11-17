# R114 / flat17 闭合机制的来源与适用范围

会话：Astra-visible-held10 / literature_mechanisms。2026-11-18 UTC。

本次定点读公共仓库提交 `5e00841fa5d54d9f6e0d0e708d53f3d9b37c8714`，不是重新跑旧计算。逐文件 commit、blob、SHA256 和地址在 `source_ledger.json`。以下 public proofs 已直接读过；文末 private originals 的内容限定来自已保存的 public audit，没有声称重新直接读过私有文献。

## 1. R114 实际采用的是有限 C² 闭合

公共路径前缀均为 `topics/visible-flexible-closed-surface/`。

| 直接读过的文档 | 实际提供的内容 | 当前不能照搬的部分 |
|---|---|---|
| `results/R17-exact-finite-visible-closed-geometry.md` §A1–A4 | 有限 integrated-Fr 尾、共享二阶圆领、common-cut 修正、平盘 pole 图、上下闭合与相位定义 | 原具体 g、尺寸、曲率和 marker 常数 |
| `results/R15-weighted-inner-background-and-collar-bounds.md` §1–3 | 条件旋转背景界；完整 Cartesian Fourier 三个端点 jets 的通用 Hermite 代数界 | (a>7/50,w_{cut}=1/2,B=6.001) 不适用本次 (a\simeq.05,w=.08,K=8) |
| `results/R19-integrated-fr-conditional-c2-convergence.md` | 对一个已存在的 C² 源，integrated derivative 插值的 C² 一致逼近引理 | 不构造精确非线性源、不控制 Fourier 截断或无限稳定图 |
| `results/R18-whole-finite-closed-metric-and-reach.md` | 原完整有限闭面度量和 reach 组合账本 | 旧域、旧端点修正和旧全域证书不能替代新候选 |
| `results/R21-m12-whole-map-and-actual-metric-decrease.md` | 原同 g M8→M12 的完整闭图精化、严格有限界 | 单次下降不等价无限 C² 收敛定理 |
| `results/R114-actual-noncircular-repair-to-original-tolerance.md` | 原非圆 repair 后的实际闭图，整面度量误差 (<1.2566772507606437\times10^{-9})；记录同 g 精化链 | 不是任意新 m3/m4 Dirichlet 输入的精确无限非线性延拓定理 |

旧构造从有限非旋转尾切出完整 (V,V_r,V_{rr})。同一固定旋转背景在正半径 (a=r_{cuff}>0) 上满足 (w,w_r\to0)；五次 Hermite collar 在外端匹配这三个完整 jets，在内端把它们置零。之后接平盘。无限振荡积累在 cuff，不在极点；真正极点处用普通 Cartesian 平盘图。因此有限数组本身不必给出“无穷层非线性解”才能定义一个 C² 闭面，但每层的等距缺陷、拼接代价和全局几何仍需完整审核。

这一机制对当前有限 M8 depth8 状态直接可复用的只有**定义和带前提的估计**。例如精确 Fourier 多项式的端点数据可以直接进入 Hermite 公式；不能由深 H 很小推出完整 (V_{xy},V_z,V_r,V_{rr}) 很小，不能由 finite far Robin 条件推出无限 C² 衰减，也不能把旧 cell 0 的 6.001 曲率常数传给本题。

## 2. 当前已经实际移植的最小链

本次已按 `M3-finite-C2-collar-and-disk.md` 完成：

1. 读取实际 fixed-M8 真实联立状态；由完整源方程恢复 mean/nonmean Cartesian 数据。
2. 用共享端点 derivative jets 与中点 derivative 定义有限 integrated-Fr C² map；对同一明确函数取深端 (A_0,A_1,A_2)。
3. 精确五次 collar 接到 (a\simeq.05) 平盘；保存单一 mean height 刚体规范，整个上侧 z 分量作反射。
4. 重新证明此物理背景的 (|\kappa_i|\le8)；区间积分证明真实径向 normalization 正且背景增高在 [.01722689,.02886511]。
5. 对圆领/盘做 Fraction 几何预算，而外有限尾暂保留采样口径。

源入口如下，均需用本包 74-file manifest 恢复。原70-file manifest 没有前四个脚本，不能因本地旧恢复目录恰好有它们就称闭包完整。

| 脚本 | 用途 |
|---|---|
| `scripts/db6f-tail-increment-export-v2.mjs` | 生成精确定义用的 finite C² derivative 数据；原脚本硬编码 m3 和 metadata B6.001 |
| `scripts/db6f_tail_integrated.py` | 读取精确累计径向坐标、积分 derivative，不把 stored positions 当独立函数 |
| `scripts/db6f-tail-collar-packet.mjs` | 独立深节点诊断；最终拼接应使用 integrated map 自己的 collar jets |
| `scripts/db6f-tail-collar-exact-check.py` | 有理 Fourier 范数、Hermite metric/curvature 代数检查 |
| 本包 `prepare_finite_tail.py` | 透明记录把原 B6.001 metadata 改为 B8.001，保持原数值执行路径 |
| 本包 `finite_closed_tail.py` | 当前实际 collar/盘、全 Cartesian 二阶查询 |

M4 要求显式一般化原 exporter 的 mode selection。把参数 `spacing` 改成4而保留旧 m3投影代码不正确。

## 3. 条件收敛引理究竟能支付什么

公共 R19 对已存在的 C² 源 F，区间长 L、二阶导数模连续性 (omega)，给 integrated-Fr 插值

\[
\|\widetilde F'-F'\|\le3L\omega,
\qquad\|\widetilde F''-F''\|\le\frac{11}{2}\omega.
\]

若输入的一阶和二阶 jets 还有误差 (epsilon_1,epsilon_2)，额外项分别为

\[
3\epsilon_1+L\epsilon_2/2,
\qquad\frac{47\epsilon_1}{5L}+\frac{14\epsilon_2}{5}.
\]

所以必须控制 (epsilon_1/L\to0) 和 (epsilon_2\to0)，不能只说 nodes 加密。更不能先假设待证的精确非线性 F 存在，再把这个插值引理当成它的存在证明。对本题完成标准，仍须同一 g、固定物理参数下实际频率/网格/相位加密后度量误差持续下降；若要严格极限存在，还需提供相应 C² 紧性和缺陷趋零证据。

## 4. 旧无限非线性定理的边界

直接阅读的公共审计：

- `notes/2026-11-09-audit-infinite-tail-applicability.md`，blob `bdaca07798137da9c6a4289901c5076c40b10693`。
- 其来源清单 `notes/2026-11-09-audit-infinite-tail-sources.json`，blob `303f6dbf67c8043fbe2e7a3c73bdbcf5b28121c5`。
- `notes/2026-11-09-db6f-audit-tail-background-proof.md`，blob `10c467f86fc55abab275428d24de983f3cb85234`。

这些审计明确区分：原 R520 是其自身小振幅 mode2 闭族；旧 large R20 是其 literal 参数、even-mode 子空间及受限稳定族；large R28 / 后续 R46 的 deep 根范围只给旋转背景中 (alpha_n\in[1/2,2]) 等信息；R31 的固定背景 taper 是以整个 cell 的 Cartesian C² 衰减和真实径向宽度代价为前提的结论。

当前 m3、default δ0=.006、eta0=.0003、protect160 与旧 R20 literal δ0=.08、eta0=.004、even modes 并不相同。即使深度8状态满足本身的有限 Newton residual，也未提供新的全频非线性稳定图、通过修改头部的受控传播、或指定外口的局部满射。使用 R28/R46 的背景根区间不等于使用它们替当前外口支付这些非线性义务。

公共审计还给了一个有用的条件事实：若真实标量方程、mean root、projection 正性、非特征分支以及所有 cell 两阶匹配都成立，则 m3 的 planar development 和 collar 相位并无额外对称障碍。它没有说某个 finite state 已满足全部条件。

## 5. 下一接口的准确责任

本次 capped tail 的外边界还需要 fixed-M8 prefix 具有同点、同角变量、同刚体规范的完整 Cartesian (X,X_r,X_{rr})；通过这些数据的 literal 修正付清 mixed derivatives 与 metric/curvature 代价，才能声称整个拼接 C²。旧 q02 或旧 512 角接口的近似数值不替代当前 fixed-M8 同点审核。

以后若这个完整有限闭图达到比例，也仍应把“有限 C² 闭图 + 全域误差证书 + 同 g 精化记录”与“精确连续等距闭族的严格存在定理”分开陈述。这正是旧 R114 可以复用的严谨口径。
