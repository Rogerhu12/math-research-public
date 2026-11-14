# 临界网格增量导出器的独立方法审查

2026-11-09，Astra-visible-flex-db6f0b0e / independent_geometry。

**方法与第一档完整数据结构审查 PASS，限于明确的有限映射定义。** 新临界网格不改变目标旋转背景，不改变共同端迹的积分 Fr 表示，也不把有限差分或新的网格提案变成源 ODE 的严格证明。源码审查、完整网格计划重放、正式第一档 finished/hash/精确分区核对均已完成。

## 1. 冻结源码与差异

新文件 `scripts/db6f-tail-critical-increment-export.mjs` 的 SHA256：

`89307bf2ca1b191c9a6850227d597325ec3c1923e2b8067a20bea58991f82175`。

比较基线 `scripts/db6f-tail-increment-export.mjs` 的 SHA256：

`4cedf4d5abf08852bd73ec35e91193e2f764d14f75d6646c582be8a2b76d9b3b`。

逐行 diff 表明所有新改动限于：临界网格参数的读取与有效性检查、`criticalLayers`/`makeGrid` 的节点提案、网格计划保存和最坏样本位置记录。二进数据布局、来源两阶 jet 的提取、每 stage 的三次 Fr 修正、midpoint 泡函数、精确积分图、半径增量归一、拼块和 collar 端迹导出均与基线相同。我另行读了完整新文件与读取器，没有只以“小 diff”代替表示审查。

完整表示读取器 `scripts/db6f_tail_integrated.py` SHA256 为 `4714e67860c80ecffc691d0d1e797bf5e8fa62062a4292730646abdf7f6e87ae`。现有连续后端仍从保存的 binary 数据与精确积分定义几何，不调用这里的源求解器。

## 2. 临界提案只影响数值分割

新函数在 source 的 integrationBreakpoints 内部估计

$$
w_x=\exp(\log w)(\log w)_x,
\qquad
\ell_c=\frac{K(1+w^2)^{3/2}|r_x|}{|\widehat{w_{xx}}|},
$$

其中分母是局部对称差分。通过筛选的正尺度只用于加入

$$
x_c\pm\ell_c\operatorname{expm1}(k\rho)
$$

中属于 (0,1) 的节点。原来的均匀节点、0/1 和源分段点全部保留，再去除相同 binary 节点并排序。这个尺度公式没有进入任何严格误差上界，因此它的有限差分误差不损害后续保存图的定义；节点选得不够好只会影响后续认证或收敛表现。

`createRecalibrationFactory` 的输入仍为原 checkpoint/config。criticalRatio、criticalCells、criticalBaseSteps 只流向分割函数，不流向物理背景构造。正式第一档输入是 M12 最终真正联解 `_tail_0018`，不是早期 warm 或 padded-cut 响应。冻结物理字段与厂函数输出作相等检查；源文件绑定保留。已有同 g 审查仍适用。

## 3. 真正物理半径与 midpoint 的语义

每个正的局部径向积分浮点数 ell_i 被保存后，即被解释为精确二进有理数。导出器以 BigInt 求它们的精确和，并定义

$$
\beta=\frac{r_{out}-r_{in}}{\sum_i\ell_i},\qquad
r_j=r_{in}+\beta\sum_{i<j}\ell_i,
\quad L_j=\beta\ell_j>0.
$$

所以两个 binary 锚点精确匹配，展示用累计半径可以接近或偶尔在浮点精度下重合，却不会让正的精确跨消失。读取器和已审连续后端使用 radialGeometry，而不相减展示半径。新的网格不改变这一定义。

midpoint source 参数由局部积分二分提出；其状态由数值 RK 积分给出，再应用保存的 stage 修正。它是一个**数值生成的中点 Fr 数据**，没有被证明等于真实源解在精确物理中点的导数。保存后，该 binary 数作为新有限四次 Fr 在精确局部 t=1/2 的规定值；这个插值恒等式是精确的。累计半径与 source 半径的数值差另有 `maxSourceRadiusDisplayDifference`，不能由该采样量推成全域严格误差。

## 4. 共享两阶 jet 仍给精确 C² 图

每跨保存 u0、u1、um 三个 Fr 值与两端 Frr 值 f0、f1。该跨长度记为 L，令 vj=L fj，四次 Fr 多项式为

$$
P(t)=H_{00}u_0+H_{01}u_1+H_{10}v_0+H_{11}v_1
+\bigl(16u_m-8(u_0+u_1)-2(v_0-v_1)\bigr)t^2(1-t)^2.
$$

它匹配规定的两端 Fr/Frr 和中点 Fr；位置由 L∫P 精确递推，所以跨界位置、Fr、Frr 都相等。源生成中的 stage 端迹缺陷不会破坏此事实：新 stage 的初行不另存一套端值，而复用上一跨的末行；文件分块和 raw-cell 接口复制整行；读取器要求相邻重复行全部相同。

stage 三次 Fr 修正及其解析导数在浮点评估后成为上述节点数据的一部分。它使数值 source 与 checkpoint 端迹接近相容，但不等于解了一个精确 ODE 修正问题。每档都保存 first/second endpoint defect 和最大修正诊断，这些量及源网格误差仍须随实际求解加密检查。

平面带符号频率满足 m≡1 mod 3，高度是非负三倍 cosine 模；使用同一组有限实系数。F、Fr、Frr 的逐点连接也使纯角和混合二阶导数连接。因此这是完整 Cartesian C² 表示，不只是母线的 C²。

## 5. 平面 Frr 的有限差分限制

审读实际调用的 `f6tail_relative_spatial_jets.mjs`：平面 Frr 是对平面 Fr 沿 **stage 参数 x** 的有限差分，再除以当前 r_x。离端点足够远时使用对称四点模板，靠 stage 端点使用五点单边模板；各扰动状态来自一次数值 RK 传播。高度 Frr 则使用保存状态与方程公式。

因此 `radialDifferenceStep=5e-5` 是源参数步长，不是一个经过证明的统一物理半径步长，也不是误差界。尤其在含绝对值的临界点，不能援引光滑函数的四阶模板阶数。已记录的临界点差分诊断必须保留。该限制影响“逼近源真导数”的解释，不影响保存 binary 系数所定义的有限 C² 图及随后直接针对它的连续 metric/curvature 认证。

## 6. 独立计划重放

独立运行新 exporter 的 plan-only 路径，参数与第一档相同：depth8、steps64、N512、degree192、criticalRatio .1、criticalCells={0}、criticalBaseSteps64。完整输出为

`2026-11-09-db6f-audit-critical-plan-r01-grid-plan.json`。

与作者计划比较：输入 hash、完整 physicalStats、288 个 stage 的全部 gridPlan 字段逐项相同；总节点18,553；只有一个 stage 获得临界层。这里重放的是完整有限网格计划，尚不是全量源数据再导出。

## 7. 第一档完成后的整包核查

第一档 manifest `2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json` 已 finished，SHA256 为 `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`。

独立重新读取全部压缩二进块，逐文件校验哈希；23个文件接口均逐字节相同，所有保存值有限。重新用 Fraction 对18,552个正径向增量求和，验证内锚、归一比例、外锚及物理 rCut 的精确等式，并核正 collar 环域。节点总数18,553、完整 Fourier 系数数141、模式唯一性和三重频率条件均与格式相符。完整 gridPlan 与前面的独立计划重放相同。最大单个压缩文件4,418,763 bytes，小于5MB。

机器审查记录为 `2026-11-09-db6f-audit-critical-exporter.json`。这次完整数据结构检查不重复数值源积分，也不从有限源 samples 推出连续误差证书。

## 8. 作用域

通过的是新增网格方法、沿用表示的数学一致性、完整计划、正式参数语义以及第一档全部有限数据结构。每个新有限图的 metric、曲率、支撑及共同端迹仍须单独重算。更密网格不会把旧 M8 或 M12 uniform 的证书自动变成新图证书。导出加密也不是重新 shooting，更不单独支付固定 g 的 G5。
