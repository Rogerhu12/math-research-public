# 固定 M14 尾的度量误差分解与有效加密方向

会话 Astra-visible-flex-78718bd0，研究者 `/root/independent_audit`（按新根 README §13 已转为实际研究角色）。本记录随实际计算继续更新；不增设独立重跑或审查门。

## 1. 问题和可直接使用的事实

当前 root 的 M14 成功联解末尾包是
`2026-11-10-78718-numerical-m14-restart8000-02_tail_0003.json.gz`，
SHA256 `c253eedbf3a4711ad79740d655262a5991e803e38dab2b4a248c386db9efcb7d`。
其有限尾为 M14、角间隔 3、N512、物理深度 12、parts8、每小段 steps32；864 个射击小段、865 个状态节点。
这个计算使用原来的同一个物理背景及全部固定层，不调整 taper、cap 或层的参数。

原末包的实际诊断标量为

| 量 | 浮点值 |
|---|---:|
| 最后 shooting residual | 1.233790464730497e-9 |
| sampled actual metric | 8.563817432971632e-9 |
| full Darboux residual | 4.908281612096834e-5 |
| normalized full defect | 0.0025241524815893656 |
| physical holonomy residual | 2.6273373837052295e-18 |
| formal curvature | 6.428917734248775 |

这里的 sampled metric 是原 `actualMetricFromDarbouxJets` 在有限状态及其原方程导数上计算的量。它既不等于最终 Fourier/Hermite XYZ 图的连续上界，也不自动给一个向外有理下界。它的用途是辨别实际误差来源。

## 2. 原公式怎样区分误差

原 `f6tail_momentum_physical_jets.mjs` 从有限动量方程隐式微分角向 root，得到实际有限 ODE 的高度二 jet；没有用另一套演化方程代替它。原 `f6tail_actual_metric.mjs` 用同一二 jet 重建周期平面发展。设

$$
S=r^2-u_\theta^2,\qquad \Delta=ES-r^2u_r^2,
\qquad \Omega=\frac{\mathcal D E^2r^4}{\Delta^{3/2}},
$$

其中 $\mathcal D$ 为该高度的完整 Darboux 残差。周期原函数 $P\Omega$ 参与径向 curl 修正，角 holonomy 的偏差也参与该修正。最终以重建的 $F_r,F_\theta$ 计算归一化基本形式的 RR、RT、TT 三项及对称二阶矩阵的谱范数。

因此应分别测试：同一有限状态的角求积、同一小段的径向 IVP 积分，以及改变有限 Fourier 维数后的局部方程。提高 N 不等于提高 M；提高径向 steps 也不会改变一个已经保存的原生节点所定义的局部有限方程残差。

## 3. 原生节点和局部径向加密：已经实际执行

脚本 `../scripts/78718-tail-fixed-state-metric-research.mjs` 直接从原物理构造器生成同一背景并细分；不构造稳定图、不求 shooting、也不运行 BVP。对每个小段左右原生端点，按原 portRatio 把存档动量换回该段坐标，使用原 split-flux engine、原 physical-jets 和原 actual-metric 函数。所有状态仅在终端中读取，不输出数组。

第一条启动因缺少 `CLOSING_TAIL_CACHE` 环境变量真实 exit1（工具 ebccce），在进入诊断前停止。补上已有源码缓存路径之后，实际 d79833/session67953 → 687a08 自然 exit0，耗时 13.15 秒。结果是
`2026-11-10-78718-tail-fixed-state-metric-research-01.json`（39,980 bytes）。

全部 1,728 个小段端点中最大值位于 cell0、stage31、rawSegment5、part0、x=0，半径约 0.5122175963387381：

| 量 | 浮点值 |
|---|---:|
| metric | 6.0040053252682555e-9 |
| RR | 6.004003960669024e-9 |
| RT | 6.305837147372512e-11 |
| TT | 8.881784197001252e-16 |
| 径向 curl 修正的最大欧氏长度 | 3.002119337919676e-9 |
| full Darboux residual | 2.67084038321386e-5 |
| root relative residual | 3.308123006236476e-15 |

cell1–cell11 各自全部原生节点的 metric 最大值均小于 3.35e-15。这里只报告这些节点，不能据此抹去未采样的内部区间。

在峰值同一状态上将 N512 提高到 N1024、N2048，metric 分别约为
6.0040053e-9、6.0040100e-9、6.0072918e-9。不同 N 同时改变最大值的采样角网格；后续将单独比较公共角点，不能把这几个网格最大值的差直接叫作求积误差。不过这些值已经排除“仅将 N 提高就把该固定态误差降至 2e-9”的数值解释。

对 stage31、32、30、33 分别保持原存档左状态不变，用 steps32、64、128 积分同一局部 IVP；各档均完整检查本段每个积分节点。峰值段的 metric 不随径向加密下降：

| stage | steps32 最大 metric | steps64 | steps128 |
|---|---:|---:|---:|
|31|6.0040053e-9|6.0040053e-9|6.0040053e-9|
|32|6.0040053e-9|6.0040082e-9|6.0040093e-9|
|30|4.2896530e-9|4.2896530e-9|4.2896530e-9|
|33|3.9795308e-9|3.9795351e-9|3.9795333e-9|

加密后的 IVP 端点不再严格满足原 S32 shooting 节点；例如 stage32 的 S64/S128 相对状态差约为 1.78e-7/1.89e-7。这只是固定初值积分误差的定位，不能把它解释成新的 shooting 解。尤其不能把分段独立积分后不一致的端点直接拼成新的实际曲面。

**已得到的研究结论：** 此 M14 尾已经在原生节点上保留约 6e-9 的主要 RR 误差，其局部来源是完整残差的径向发展修正；单独提高 N 或把这些局部 IVP 的 S32 提高至 S64/S128 均不消除它。主候选的同 g 高模推进需要继续考虑这一有限 M 来源，同时把最终 XYZ 表示误差另行量化。

## 4. 与已有 M12 结果的关系

不重新运行旧 M12。已有 `2026-11-09-db6f-tail-m12-critical-two-grids.md` 记录，同一 M12 原生 CP 的两档实际导出图 sampled XYZ metric 分别为约 1.96721814e-8 与 1.96724320e-8；增加表示网格没有消除该级别的误差。该文也明确更细的导出改变阶段端补偿，不构成重新 shooting 收敛。R21 对其同一实际图给出的完整连续上界约为 2.334387e-8。

这些是不同图和不同诊断口径，不能直接拿旧 M12 的严格上界与本次 M14 source-jet 采样值作收敛率证明；它们共同支持把源截断和表示积分分开处理。

## 5. 内部峰、公共角点与真正遗漏频率：已实际完成

`../scripts/78718-tail-metric-location-research.mjs` 对 cell0 的 72 个小段各检查原 S32 的 33 个节点，总计 2376 点。实际 cfbc92/session46139 → 014eef 自然 exit0，17.927 秒，结果 `2026-11-10-78718-tail-metric-location-m14-01.json`（40,008 bytes）。

原 audit 的峰 8.563817432971632e-9 完全复现在 stage40、rawSegment3、part7、x=0.375，r≈0.4351210262850741。RR 恰为该值，RT≈9.19e-11、TT≈4.44e-16，径向 curl 修正长度≈4.28208e-9。

对这同一状态，N512/N1024/N2048 在原 512 个公共角点上的 metric 分别为 8.563817432971632e-9、8.563820097506891e-9、8.563817432971632e-9，差仅约 2.7e-15。二 jet 在公共点的最大差为约 6.22e-14，重建径向向量差约 1.44e-15。

对 Ω 的数值 Fourier 分解给出：保留 0…42 的最大幅度约 1.49636e-16，而遗漏频率 45、48 幅度分别约 1.19086084e-5、7.71515373e-6。这精确定位了有限 M 角投影留下的残差。频率检查到 180；它是浮点定位，没有支付无限剩余项。

在该状态补零到更高 M、再重解角 root 并计算新局部 ODE jet，M16/M18/M22/M26 的 metric 分别约 1.118e-9、2.020e-10、7.438e-11、8.989e-12。新 root 会改变 u_r 约 1e-6，不能把这些行当作已经完成径向演化的新尾。

## 6. 当前 M15 首响应：内点比原生节点更重要

读取当前真正 N512 首包 `2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz`，SHA256 `a88f0a8eaff38a6fca9576550ef04d538c8b8d1fe55715df6d0439f27801c919`。它的 residual=6.266872045838407e-10，两个 history 行，audit=false；主 outer 还未完成，不能称最终 M15 联解。

原生端点/两个局部小段的实际 c010c2/session40833 → 623300 exit0，8.215 秒，报告 `2026-11-10-78718-tail-fixed-state-metric-m15-first-01.json`（23,701 bytes）。原生端点峰为 4.876884175358421e-9，局部 stage31 的 S32/S64/S128 峰均约 4.88320115e-9。

但随后对 cell0 完整 2376 点扫描的真实 fc528e/session27364 → c15c22 exit0（17.715 秒）发现内部峰反而是 **1.4909764312065477e-8**，位置 stage40、x=0.40625、r≈0.4351418479524458。报告 `2026-11-10-78718-tail-metric-location-m15-first-01.json`（39,660 bytes）。

因此，M15 原生节点小于 M14 并不支持“整个尾也改善”的判断；不同 outer 阶段还不能构成单调 M 收敛序列。此峰 RR≈1.491e-8、RT≈1.518e-10、TT≈9.99e-16，仍为同一类型的遗漏高频来源。保留至 45 的 Ω 频率最大约 1.62e-17，遗漏 48/51 幅度约 2.32871e-5/2.12691e-5；N 加密在公共角点的差约 2.5e-15。

| 零补后的局部 M | 此 M15 峰状态的新局部 metric |
|---|---:|
|16|9.854586036084356e-9|
|17|8.48185388591105e-9|
|18|3.4034151052964043e-9|
|22|2.2034574559074343e-10|
|26|8.688117284977835e-11|

这里 u_r 的变化达到约 3.9e-6。这些值只为下一次真正高 M 同 g 联解提供数值方向；即使 M22 局部值较小，也未给其全尾误差界。

## 7. 已完成的数学解释与继续研究

完整解析结论直接写入 [R85](../results/R85-darboux-curl-and-tail-metric-frequency.md)：从同一个高度和径向 g 推出连接 curl、真实周期发展修正、RR/RT/TT 恒等式，以及完整 Fourier 卷积权；另说明有限角数组的 Gram 恒等式及其不能自动冒充实际 XYZ 插值图的导数。

关键结构是保留模的精确积分有限系统满足 Π_M Ω=0，而遗漏模仍存在。旋转背景的线性化中，Ω=a_k cos(kθ) 导致 RR≈2r a_k/[E(k²−1)] cos(kθ)，RT 多一个 1/k 衰减；当前数据符合该结构。实际离散投影还保留 aliasing 项，N 加密的公共角点比较支持它目前不是主要误差。

下一步继续对有限 M 尾的实际升频余量作有效定位，并由主计算真正推进同 g 高模联解；不重启独立重复 BVP，不把局部预测当作新解。

## 8. 表示误差的已有参照，以及零动量补齐造成的新峰

读取已经完成的实际 M14 导出 `2026-11-10-78718-post-restart8000-storage-v2-run-01/tail-manifest.json` 的标量：21030 个跨、21031 个节点，sampled `totals.metric=8.57521241748103e-9`，`sourceMetric=8.563936608002002e-9`，差约 1.13e-11；`stageMaxFirstCorrection≈1.80427e-10`。这是同次实际导出的已有采样，支持当前约 8.6e-9 的主要来源仍是有限源频率，不是目前 critical 表示本身。没有把它当作连续上界，也未重跑导出。

随后对 M15 原轨道在 cell0 每段的 1/8 网格及该段旧峰，共 680 点，做 M18/M22 的局部零动量补齐：峰迁移至 stage34、x=0.125、r≈0.48461851182189386，M18/M22 分别达到约 9.600185e-9/5.710711e-9。数据在 `2026-11-10-78718-tail-local-mode-sweep-m15-first-01.json`，脚本 `../scripts/78718-tail-local-mode-sweep.mjs`；真实 d51727/session78112 → ba5e29 exit0。

这一结果否定了“只看旧 stage40 峰就预判 M22 全尾足够”的做法，但也不是新 M22 解的失败。因为当前坐标的动量是完整非线性角连接的投影，给新增动量 π 置零会改变旧 u_r；它不是保留原几何的一阶升频。

## 9. 保留 Q/L 的几何升频：已实现真正暖启动转换

原引擎的 `toRaw` 返回 Q 与 L 的物理尺度坐标。使用

`old.toRaw → raw 的 Q/L 补零 → new.initializeFromRaw`

可以保留非线性 root 的实际高度和径向一 jet，再由该角连接产生所需的新高模 π。完整命题、正定 Jacobian、跨 N 的均值重求及全节点 port 规范已直接登记 [R86](../results/R86-geometric-momentum-prolongation.md)。

在上节新 stage34 峰，N512 的比较为：

| M | π 高模直接置零 | Q/L 几何升频 |
|---|---:|---:|
|18|9.60018509e-9|7.88519205e-10|
|22|5.71071146e-9|2.43855219e-10|
|26|4.43703872e-9|1.11865300e-10|
|32|3.45610501e-9|3.29023502e-11|
|40|2.08777768e-9|9.48019441e-12|

局部几何升频后的公共角点 u_r 差不超过约 4.1e-16；N512→1024 重求均值后的实测差也在这个量级，但跨 N 不宣称严格相同或逐位保持。报告 `2026-11-10-78718-tail-geometric-mode-embedding-stage34-01.json`，真实 5a4939/session58657 → 833bc4 exit0。保留一 jet 后新的二 jet 是正权 Galerkin 修正；其固定截面的加权残差随增加空间不增，连续投影下趋零，详见 R86。这个局部结论没有给全尾的统一存在区间。

与 numerical_recovery 分工后，已直接写可用生产函数 `../scripts/78718-tail-geometric-warm-remesh.mjs` 和新入口 `../scripts/78718-prefix-tail-geometric-worker.mjs`。后者基于原 trial worker，仅更改初猜坐标转换与诊断，保留真正的 DN/ODE/Jacobian/分支/残差；原正在运行的 M15 源未改。

全 865 个节点的实际 M15→M22 转换已经完成，报告 `2026-11-10-78718-tail-geometric-warm-probe-m22-01.json`，真实 8fdf73/session46809 → 31b1a1 exit0。Q 差为零；N512 的最大公共角点 u_r 差约 5.8094e-16，N1024 约 5.8009e-16。新增高 π 最大可达原低 π 范数的约 5.125%，因此早先 π=0 的改动不应忽略。

当前数学与实际实现已经交给主数值线，接下来由该线用真正方程求解新初猜。这里的全部点值仍是局部定位和暖启动性质，没有冒充新的完整高 M 闭图。

最后将第 8 节同一 680 点粗网格换成 Q/L 几何嵌入，M18 的局部峰为 3.2874822863959724e-9（stage40、x=0.5），M22 为 3.3281116909387705e-10（stage31、x=0）。所以 stage34 的修复不是仅把大误差转移到某个同样大的已检查点；M22 在这次有限采样中有明显更大余量，M18 仍超过 2e-9。实际数据在 `2026-11-10-78718-tail-geometric-mode-sweep-m15-first-01.json`，程序 `../scripts/78718-tail-geometric-mode-sweep.mjs`，80f5b3/session70151 → f78afa exit0。此比较仅指导实际升频，不把有限网格或固定旧轨道升级成新解或连续证书。

## 10. 连续证书的旧上界差不是新的固定误差下限

为准备真正高模图，读取了旧 M12 的已有连续报告说明及现有 `db6f-audit-tail-metric-curvature.py::metric_residuals`、`db6f-audit-metric-polynomial.py::P.norm`。旧 M12 sampled metric≈1.96721814e-8，连续上界≈2.33438682e-8；最坏证书 span17148 正在第一物理 cell 的 r≈0.435 区域，而不是一个独立的深尾瓶颈。

这个约 3.7e-9 的差不能直接当作未来候选的固定包装下限。现有后端先在多项式系数上抵消背景项，实际使用

$$
\begin{aligned}
E_{res}&=2R_r+R_r^2+T_r^2+Z_r^2+2wZ_r,\\
F_{res}&=(1+R_r)(R_\theta-T)+T_r(r+R+T_\theta)+(w+Z_r)Z_\theta,\\
G_{res}&=(R_\theta-T)^2+2r(R+T_\theta)+(R+T_\theta)^2+Z_\theta^2.
\end{aligned}
$$

这里 R/T/Z 是实际图相对旋转背景的扰动。背景的 $w^2$ 没有作为两个独立区间作差；w 包宽度只乘扰动导数。若背景包引入统一误差 $|\delta w|\le\epsilon_w$，上述未归一化残差的新增包围宽度最多分别是 $2\epsilon_w\|Z_r\|_\infty$、$\epsilon_w\|Z_\theta\|_\infty$、0，归一化再用实际 r/E 正下界。

`P.norm` 使用每个 Fourier 系数的径向 Bernstein 包围，再做 Fourier l1；其与角上确界的差也随实际残差系数而变，未给出一个与新候选无关的常数差。旧完整背景包的 w remainder 最大值约 2.60962e-7（仅读取 6211 盒的聚合标量；没有把这个全局最大数脱离当地 Z 导数套作精度判决）。

因此下一张真正高模图先使用现有相同背景包和连续后端。若实际最坏行仍受背景或径向 Bernstein 包围影响，再针对这些行细化；目前不预先创建新证书家族或重算整张旧图。

## 11. 同方程尾变分流的 Fourier 乘积加速

为使真正 W22 推进更可行，使用有限求积下的三角乘积恒等式，把原 Jacobian 的六组权函数乘积从每个角点逐项形成 M² 矩阵，改为积累到 2M 的离散 Fourier 矩后装配；同 N 的全部 aliasing 保留，不改原 root 或 split RHS。完整代数和实现已直接登记 [R89](../results/R89-tail-fourier-product-variational-flow.md)。

第一版的十点真实 6bb428/session90311 → 08cfb7 exit0，完整标量报告 2026-11-10-78718-tail-fourier-product-benchmark-01.json：M22/N512，局部 Jacobian 合计加速 1.859 倍，所有十点 RHS 差为零。完整可选 flow 与 worker 已交 numerical，显式 tail-jacobian=fourier；默认原后端不变。单个真实短 stage31/32 步报告已有，state 差为零、变分逐行尺度差约 3.405e-13、耗时比1.399；其末工具回执遭上下文截断，后续 session unknown，不补造自然 exit，报告身份与准确范围见 R89 §7。

随后按根建议，把原 root 中 B=I+〈b c_i c_j〉 的 Gram 装配也改为有限 cosine 矩，原残差、分支、Newton/线搜索/容差均原样。这不是另一个物理 root。新工厂 [78718-tail-fourier-root-split-engine.mjs](../scripts/78718-tail-fourier-root-split-engine.mjs) 返回完整引擎，便于与根的全节点切线暖启动组合，不再复制 DN worker。

合并版真实 51e8fe/session79263 → 39f2fa 自然 exit0，7.908 秒，报告 2026-11-10-78718-tail-fourier-root-benchmark-01.json（16,181 B）。同十点 root 总计1.798倍、完整 Jacobian3.138倍；同一个32步 stage31 的完整 flow2.757倍，末状态最大差6.94e-18、末变分shape逐行尺度差3.439e-13。十点Newton次数逐点相同，root λ最大差6.94e-17；完整代数及误差口径在R89§9。

这些计时只属于同一固定几何暖启动的有限实验，没有运行新DN/BVP，也没有代付全尾metric。原M15主计算一直保持原源；新的工厂选择仅供后续真实联解使用。

## 12. 当前 M15 延拓的 leading 敏感性与数值 floor

为定位第 2 外请求中约 0.2% 的首高度变化为何使内 Newton 缓慢，保存了实际 call2/iteration5 的一个小型 UNCONVERGED 快照：2026-11-10-78718-tail-branch-call2-iteration5-input.json.gz，262748 B，SHA256 21e0fe2c2da4d0826968e501c75ea00d032ab725af39468c3d13a464ad2cd4c7。它的 normalized residual 为 0.0804869996、minA 为 0.0719541152；首高度相对已收敛首尾增加 0.00198404885。这不是已经求解的第二个尾响应，故下面的差异不能直接称作已收敛 DN 对 H 的导数。

只对 stage32…40 的既有输入局部积分、三个已保存失败小段及指定固定点作诊断，没有启动完整 DN/BVP。程序为 [local-diagnostic](../scripts/78718-tail-branch-local-diagnostic.mjs)，真实 f1064a/session88870 → e9163f exit0，7.028 秒；报告 2026-11-10-78718-tail-branch-local-diagnostic-01.json（20967 B，SHA256 80fadc3b0452c7802ec84f07c66958551c0cdc061d17d6c3fd8b6634ad20ffa5）。

最小值准确复现于 stage37、x=0.265625 的 RK 子阶段，r≈0.457186443、w≈0.00727756826。旧首尾在同一点同角的 A≈0.1052980343，当前为0.0719541152。物理分解为

$$
A=1+K+E P_\theta
=\frac{r u_r+E u_{\theta\theta}}{rw},
\qquad
\Delta A=-0.0333439191,
$$

其中 $\Delta K\approx-0.0007220541$，
$E\Delta P_\theta\approx-0.0326218650$，角高度二阶项占本次下降的约97.83%。
等价的 $\Delta L+W\Delta P_\theta$ 分解虽有
$\Delta L\approx-0.03334219$，但 $L=K+P_\theta$，不能把它误解为径向斜率主导。
实际 $\Delta u_r\approx-5.2548\times10^{-6}$，
$\Delta u_{\theta\theta}\approx-1.08534\times10^{-4}$。

三个保存的 trial 原拒绝均真实复现：

|Newton 步因子|原拒绝的局部点|仅把同点诊断 floor 改为 $10^{-10}$ 后|
|---|---|---|
|1|stage36入口|默认或当前接受态初猜仍失败|
|1/2|stage36入口|找到 residual 约 $10^{-16}$ 的 root，minA≈0.0409031413|
|1/4|stage37，x=0.171875|找到 root，minA≈0.04990593385|

后两点的 D、S 仍接近1，说明这些固定输入确实被原 A>0.05 数值 guard 挡住；没有因此调整主运行的 guard，也未声称较低 floor 已被整条尾接受。

为补清首个 RK 子阶段没有“上一点 root”的情况，又用真正当前接受态的同点 root 作初猜，并在固定截面上用32步线性状态延拓。程序 [point-continuation](../scripts/78718-tail-branch-point-continuation.mjs)，真实 bd52c5/session76583 → 892ed9 exit0，3.453秒；报告 2026-11-10-78718-tail-branch-point-continuation-01.json（11612 B，SHA256 e4e33775203d6609f0dbdf9d7f720bb7d88135d9b21b75079639cc08c705a7ee）。

原 floor 下三点仍均失败，较低 floor 下只有半步和四分之一步两点成功。全步在较低 floor 的固定截面延拓中，走到90.625%时 minA≈0.001402214，下一格失败。它不能证明该全步不存在其它正 A root；但当前证据不支持把失败归结为单纯换一个容易得到的 Newton 初猜。

按根要求，同时在 stage36/37 的接受态以及两个已得到正 root 的失败点作 Q/L→W22 同点几何嵌入。接受态的两个原生点 A≈0.0891919347、0.0755799725；新 M22 默认 root 都实际成功。两个低 floor 点的新 A 仍约0.0409031、0.0499059，未被升频“修好”。精确理由已补入 [R86第9节](../results/R86-geometric-momentum-prolongation.md)：同 g、同求积、同 Q/L 的一 jet 嵌入保持 A、D、S；新高模演化可以改变后续 A，但纯坐标嵌入不能提高同点 leading。

主 M15 原进程后来由根按研究调度主动停止，根已启动真正 M15/W22、Fourier-root 加全节点切线暖启动的新路线。上述局部诊断不代替它的收敛、全角正性、metric 或 reach；若未来采用较低 floor，也须使用新图自己的正性及 reach 计算，不能转用旧 A>0.05 的预算。

## 13. 新 W22 首次 Newton 的 trial8/9：接近 A=0，但须另看 Gauss 曲率

根实际启动的 fast02 首请求保持旧 M15 首尾的全部 H，低15项逐项相同，新增高H全零。几何暖启动保证同点一jet保持，并不保证新的W22整段ODE或shooting残差小；其首norm992.422不能解释为metric992。

从实际 iteration1 保存了接受 trial9 的小快照
2026-11-10-78718-tail-w22-branch-call1-iteration1-input.json.gz，
386180 B，SHA256 66d469c1cf73c57984c18533bebde9391fffd74b3dae18148736320b6d1f3ae3。
它对应已接受的1/512 Newton步、norm990.99164。对照原
2026-11-10-78718-numerical-m15-w22-fast-02_tail-trial-call1-iteration0-trial8.json.gz
中1/256步的stage35输入，只局部重放这个小段及固定失败点，没有完整DN/BVP。

[邻近root程序](../scripts/78718-tail-w22-branch-neighbor-diagnostic.mjs)
使用与实际worker相同的完整Fourier-root工厂。真实091513/session89609 → 9e08f0 exit0，2.905秒；报告
2026-11-10-78718-tail-w22-branch-neighbor-01.json，5868 B。

失败恰在stage35入口，r≈0.473823542。已接受trial9同点A≈0.1025425664；trial8在原floor .05下用接受态root初猜仍失败，但低floor默认初猜、接受态初猜及32步固定截面状态延拓都成功，A仅≈0.0014904603。D≈0.999927881、S≈0.999999166。因此它不是简单的线性root初猜失误，而已经很接近实际leading为零的区域。

两者在该角的差为

$$
\Delta A\approx-0.1010521061,\quad
\Delta K\approx-0.0020126136,\quad
E\Delta P_\theta\approx-0.0990394925.
$$

角二阶变化中，原≤45频率贡献≈−0.0692574058，新48…66频率贡献≈−0.0297820867。高模Newton修正还通过耦合显著改变了低模，不能把整个变化都归给新高模本身。这里没有走完放宽floor后的trial8段，也没有把这个固定点root记为接受的尾。

进一步只用这个固定点的两份高度一jet计算精确等距延伸所必需的形算子。完整命题已补 [R86第10节](../results/R86-geometric-momentum-prolongation.md)：

$$
b=\frac{wU}{r\sqrt D},\qquad
c=\frac{wA}{r\sqrt E\sqrt D},\qquad
a=\frac{K_g+b^2}{c}.
$$

这由 $\operatorname{Hess}_g u=n_3\mathrm{II}$ 和 Gauss 方程直接推出；与已经得到的实际有限投影二jet是不同对象。[点计算程序](../scripts/78718-tail-w22-leading-curvature-point.mjs) 真实f2e969/session49417 → cf99b5 exit0，报告
2026-11-10-78718-tail-w22-leading-curvature-point-01.json，3218 B。

低A点的 $K_g\approx-1.7562231e-5$，
$b\approx2.3050735e-4$、$c\approx2.2831349e-5$，
Gauss强制 $a\approx-0.76688844$，必要shape样本最大≈0.766889；
接受trial9同截面样本最大≈0.0573113。这两个有限点记录尚未显示宏观reach尺度的必要曲率失败，不能据此丢弃所有较低floor路线。

但是trial8的有限投影ODE只给 formal curvature≈0.0599468，同时最大逐点Darboux残差≈1.72616e-5。因此前者不能充当精确Gauss所要求的shape。即使局部metric误差因高频积分很小，也仍需同g加密来消除该来源，不能仅降低guard就支付G5。

根随后实际观察fast02 exit2，原bootstrap在iteration2约norm498.756、minA≈0.05458后线搜索拒绝；失败原样保留。根正推进真正较小H的W22解再向原H延拓，g、最终H和最终BC保持；这些局部数据只用于研究路线判断，没有把中间小H或失败点称作完成结果。

## 14. 半 H 的动量同比缩放失败后，几何缩幅已进入真实计算

fast03 的真正半 H 请求仍沿用无 tangent 时的 Q/π 同倍率 fallback，根实际观察其自然 exit2，14.3486秒；首evaluate即发生root line search失败，未留下完成的shooting迭代。它并不说明半H的真解不存在，因为非线性π的同比缩放不是同一jet的几何缩幅。

按根要求实现 [geometricAmplitudeWarm](../scripts/78718-tail-geometric-amplitude-warm.mjs)：同M/N沿R86节点规范转换到raw Q/L，对这两组一起乘比例，再用原mean root及π投影初始化。node0先乘portRatio进入cell0规范，存回时再除；其余节点用cell[i−1]首profile/x0。调用者保留新H的线性边界修正及真正DN全部方程，不把helper当成功求解。

完整证明直接写入 [R94](../results/R94-geometric-amplitude-warm-mean.md)。核心均值项为

$$
d(s)=\lambda_0(s)-s\lambda_0^0,\qquad
u_r^s=w+s(u_r^0-w)+wd(s),\qquad
A^s=1+s(A^0-1)+d(s).
$$

只保证非均值jet精确缩放，不假定d的符号，也不由缩幅自动推出正分支。均值root的局部IFT、严格单调及完整A/S/D公式均已给出。

helper被numerical接入后，根真实启动fast04（3787e9/session83728），保持g、最终H、floor .05及最终成功条件。该运行的实际12:10:53.077事件已读取成
[小标量摘录](2026-11-10-78718-tail-geometric-amplitude-warm-actual-01.json)
（1265B，SHA256 f28772aada0f11ab154b14b32461eac98dd8e30dcae300e18c6165234769976e）：
865节点M22/N512、s=.5，Q缩放差0，非均值u_r缩放Fourier-l1差2.24748e-17；
mean偏移1.62543e-4，π相对同比缩放偏移0.557998，
root残差5.03384e-14，样本minLeading.561749/minD.995847。
均值及非线性动量差都是真实可见的，不能省略。

随后真实首shooting evaluate成功完成，仍有很大的归一残差；本节不把它说成已收敛的半H尾，更不说原H的闭面已完成。根独占该主会话观察。生产helper/root/flow版本在该运行期间保持不动，没有为此再开重复DN。

## 15. 已有连续尾图的背景余项预算：关键点不是全局包余项的直接复制

为准备未来真正新尾图的连续metric计算，只读取已经存在的M14有限图
`2026-11-10-78718-post-restart8000-storage-v2-run-01/tail-manifest.json`，
以及同一已审物理背景的旧M8 lowmetric packet。本节没有重新求解旧尾，也没有把旧图的几何证书转给未来W22图。

写背景图为 $F_0=(r\cos\theta,r\sin\theta,z_0(r))$，$w=z_0'$，
扰动为 $V=R e_r+T e_\theta+Z e_z$。原backend先形成

$$
\begin{aligned}
E_{\rm res}&=2R_r+R_r^2+T_r^2+Z_r^2+2wZ_r,\\
F_{\rm res}&=(1+R_r)(R_\theta-T)+T_r(r+R+T_\theta)+(w+Z_r)Z_\theta,\\
G_{\rm res}&=(R_\theta-T)^2+2r(R+T_\theta)+(R+T_\theta)^2+Z_\theta^2.
\end{aligned}
$$

背景自身的 $w^2$ 已精确相消。设一个背景包内 $w=p+e$、$|e|\le\varepsilon$，
其中本次选 $p$ 为所存各系数下端点组成的多项式；那么在相同真实 $g$ 的正交归一框架中，
仅省略 $e$ 对残差矩阵造成的改变量恰为

$$
\Delta M=
\begin{pmatrix}
2eZ_r/E&eZ_\theta/(r\sqrt E)\\
eZ_\theta/(r\sqrt E)&0
\end{pmatrix},\qquad E=1+w^2.
$$

因此在 $r\ge r_*>0$ 的区域，若 $|Z_r|\le B_r$、$|Z_\theta|\le B_\theta$，则

$$
\|\Delta M\|_{\rm op}\le
2\varepsilon B_r+\frac{\varepsilon B_\theta}{r_*}.
$$

这是同一真实 $g$ 下的**分子余项贡献**；没有声称把归一框架也换成 $1+p^2$ 后仍是同一个差值。
取包内局部坐标 $t\in[0,1]$ 时，可安全使用

$$
\varepsilon=\varepsilon_{\rm analytic}
+\sum_j(c_j^+-c_j^-).
$$

各系数端点都是精确binary数；该和先用Fraction精确构造，之后用原外向区间算术上包。
实际 $B_r,B_\theta$ 使用原连续图的积分节点值、原径向Hermite多项式及Fourier/Bernstein范数，
不是从角采样最大值推成全角界。选定的每个新图span均落在一个旧背景包物理区间内；只做这些交集，未产生或声称完整的新转移包。

[局部预算程序](../scripts/78718-tail-background-error-budget.py) 的真实执行
561014/session6658 → 0d3381 exit0，4.534秒，峰RSS约406MB，0 ODE/0 DN。
完整小报告为 [background-error-budget-01](2026-11-10-78718-tail-background-error-budget-01.json)。

|查询半径|M14完整小span|背景解析余项|$B_r$|$B_\theta$|背景对metric的额外贡献上界|
|---|---|---|---|---|---|
|0.435121|18157|$5.40519\times10^{-9}$|0.00524364|0.000336790|$6.08694\times10^{-11}$|
|0.43514185|18160|$9.33229\times10^{-10}$|0.00530124|0.000337070|$1.06175\times10^{-11}$|
|0.4738235418774|18453|$6.62863\times10^{-13}$|0.00452238|0.000620848|$6.86601\times10^{-15}$|
|0.4846185|18525|$5.95019\times10^{-13}$|0.00456629|0.000673727|$6.26331\times10^{-15}$|
|0.5122|18709|$4.63167\times10^{-13}$|0.00461624|0.000806683|$5.00766\times10^{-15}$|

表中展示的界均向上放宽；JSON保留实际binary64外向端点。低metric背景包的全局最大解析余项
$2.60963\times10^{-7}$ 出现在 $r\approx0.230706$，不在旧M14/M15主要metric峰的
$r\approx0.435$。尤其不能把它直接当作所有新图的metric误差下限。

这里的约 $6.09\times10^{-11}$ 是既有图在一个完整小span上已算出的额外预算，仍不是整个尾的最大值。
它表明该处背景余项尚不足以解释旧有限图的约 $8.6\times10^{-9}$ 真metric残差，
也不足以单独解释旧证书与样本之间数 $10^{-9}$ 的宽差。
未来W22真解仍须使用自己的导数场、有限图和实际最大行；若其证书余量不足，应先区分几何残差、
Fourier三角不等式、径向Bernstein范围及背景余项，再按真正主导项加密。

## 16. 同一峰附近两个span的包络分解：没有固定的数 $10^{-9}$ 证书宽差

继续使用第15节的同一既有有限图和同一背景包，只取前两个完整span。
新研究程序 [local-metric-budget](../scripts/78718-tail-local-metric-budget.py)
重建原系数层面的 $E_{\rm res},F_{\rm res},G_{\rm res}$，比较以下三种连续界，
没有改动图、多项式、背景、节点或物理参数。

设在真实 $g$ 的正交归一框架中，残差矩阵为

$$
M=\begin{pmatrix}a&b\\b&c\end{pmatrix}.
$$

若 $|a|\le A$、$|b|\le B$、$|c|\le C$，原backend使用
$\max(A+B,B+C)$。由对任意向量逐分量取绝对值，
$|Mx|\le\begin{pmatrix}A&B\\B&C\end{pmatrix}|x|$，
再用非负对称矩阵的最大特征值，可得较紧的连续界

$$
\|M\|_{\rm op}\le
\frac{A+C+\sqrt{(A-C)^2+4B^2}}2.
$$

这一步仍使用原Fourier-l1分量界。进一步保留每个角区间上的符号及分量范围时，
直接使用精确恒等式

$$
\|M\|_{\rm op}=
\frac{|a+c|+\sqrt{(a-c)^2+4b^2}}2.
$$

等式来自两个实特征值 $((a+c)\pm\sqrt{(a-c)^2+4b^2})/2$；
对右边逐次使用原外向区间运算，仍是整个角区间的上界。
每个残差多项式先合并正负Fourier系数，再把径向多项式变成Bernstein系数范围；
角范围直接复用原backend的有理Machin/Taylor三角区间表。
这里角表覆盖 $\phi=3\theta$ 的完整一周，因所有残差均三重周期，所以也覆盖全部物理角。
径向细分只限制已经相消后的同一个残差多项式，不重新积分或插值。

真实执行 2b2fb6/session18777 → 25ac95 exit0，81.669秒，峰RSS约408MB；
其中75.723秒为一次性原三角表构建，0 ODE/0 DN。
完整标量记录为 [local-metric-budget-01](2026-11-10-78718-tail-local-metric-budget-01.json)。

下表统一以 $10^{-9}$ 为单位，所有展示上界均向上放宽：

|实际span|原系数l1/行和|仅Perron包络|64角区间，径向1段|256角区间，径向1段|256角区间，径向4段|
|---|---|---|---|---|---|
|18157，包含r=.435121|9.043406|8.921323|8.861192|8.735293|8.664309|
|18160，包含r=.43514185|8.850706|8.733358|8.687592|8.593247|8.520043|

仅径向4分但仍用原l1/行和时，两行分别为8.967008、8.783553。
因此这里的放宽来自多个小项：混合分量的行和替代、角频率取绝对值，以及有限径向区间范围；
它不是必须给每个新候选另外加上的固定常数。

已有manifest记录这幅旧图的全局有限采样metric约 $8.5752124\times10^{-9}$。
第一行原界与这个采样最大值的数值差约 $4.68\times10^{-10}$，细分后约 $8.91\times10^{-11}$。
这只是为了判断预算量级：全局采样最大值不自动属于这一个span，也不是严密的连续下界，
故这两个差值没有被列为新的严格误差证书。第二行的上界小于全局采样最大值并不矛盾，
因为它只覆盖另一个完整小span。

结论限于这些已经计算的旧图区间。原始l1/行和方法可以先用于未来新尾图，
若实际最坏行的余量不足，再按本节的同多项式细分压缩范围；
不必因旧M12另一张图的约 $3.7\times10^{-9}$ 宽差而预先认定G5不可达到。
完整新尾图的存在、自己的连续metric、reach和闭合条件都尚未由本节支付。

## 17. fast05最坏stage12：实际root精度及Jac/plain两路的有限比较

本节针对根真实低振幅fast05运行所保存的iteration3；不是最终原H解。
输入 `2026-11-10-78718-numerical-m15-w22-fast-05-iteration3-root-diagnostic-input.json.gz`
为385541B，SHA256 `18996bebb3b93b2b092c31e7e16f956a3826071133d40c01ac20dfe931adf7d9`。
实际最坏shooting项在stage12、rawCell0/rawSegment7、分量42即π的63频率：
绝对残差 $2.141778724366807\times10^{-12}$，
归一scale $0.0006419043268729995$，归一残差约 $3.3366011642270125\times10^{-9}$。

先作0 ODE的两端代数根比较。映射严格按原core：x=0取node13，x=1取node12并给π乘该stage的portRatio；这里portRatio恰为1。
旧root名义相对阈值 $8\times10^{-14}$，另名tight工厂为 $4\times10^{-15}$，
两者保留同一物理方程、Q/π状态和Gram公式。新工厂同时把舍入fallback改为 $2\times10^{-14}$。
没有据此预先断言tight会改善真实shooting残差。

[点诊断](../scripts/78718-tail-root-precision-point-diagnostic.mjs) 真实
b153f3/session7091 → 565062 exit0，2.698秒；报告
[root-precision-point-01](2026-11-10-78718-tail-root-precision-point-01.json)。
首次工具1d5524在导入前因缺少 `CLOSING_TAIL_CACHE` 早退；新诊断已与所选sourceRoot一致地选用原已审缓存，之后才产生上述实际数学计算，原生产源没有改动。

|原状态端点|旧root实际相对残差|Newton步数|Gram最小特征值近似|条件数近似|63频率root残差所对应的π误差|
|---|---|---|---|---|---|
|node13/x0|$9.19341\times10^{-17}$|2|0.99886457|1.00237834|$3.96363\times10^{-19}$|
|node12/x1|$1.65085\times10^{-16}$|2|0.99943153|1.00122564|$1.50331\times10^{-18}$|

后列是原moment残差除以实际π→moment比例，未乘任何沿程放大因子。
Gram的角权重 $A/D^{3/2}$ 及实际浮点矩阵的Gershgorin范围也在报告中；特征值来自小型对称Jacobi算法，仅作浮点条件诊断，不冒称外向区间证书。
两端的tight默认初猜、以及从旧L再启动tight，全部L系数、mean、Gram、A、D都与旧解逐位相同。
因此这两点没有出现“停在宽阈值上”的现象。

根随后明确授权只对这个stage作原/tight与needJac=true/false的四路原S32流比较。
[单段程序](../scripts/78718-tail-root-precision-stage-flow.mjs) 使用实际完整split工厂：
true调用 `flowStateWithJacobian`，false按原core对每个profile执行32次 `rk4`。
保留actual cusp选项；该stage的breakpoint数为0，两条实际网格逐项相同。
真实 b81351/session7943 → a398a9 exit0，3.727秒；报告
[root-precision-stage-flow-01](2026-11-10-78718-tail-root-precision-stage-flow-01.json)。

四路全部成功，44个shape输出、mean，以及最坏63频率残差都逐位相同；
四路均准确重现已保存的 $3.3366011642270125\times10^{-9}$ 归一残差。
原/tight的Jac流沿整个stage所得maxRootRelative均为
$1.6457031643868078\times10^{-16}$，minA≈0.99867609、minD≈0.99964158。
因此**对这个实际最坏段**，两种具体猜测已经被排除：
名义root阈值太宽，以及计算Jac与不计算Jac时的state舍入路径不一致。
没有把本段有限观察外推成所有stage都无需精度研究。

该次完整Jac还给出了另一条实际线索：max矩阵元约 $2.42110\times10^{13}$，
无穷范数约 $2.42890\times10^{13}$；π63输出行的绝对值和约 $1.26943\times10^{13}$。
这属于本stage的流敏感性，不能归给接近单位的代数root Gram。
矩阵采用实际Q/π单位，故单凭大矩阵范数还不能认定某项误差已被如此放大；
须与实际输入变化逐分量相乘。当前报告只保存了这些标量，没有保存完整Jac数组，
后续不能声称凭此文件即可取出逐项 $J\,\delta y$。

## 18. 零Newton方向的真实回缩偏置及其单段放大

geometric作者另作了真实v2几何回缩的零方向检查：不是直接走step=0快捷分支，
而是设置 $\delta=0,\lambda=1$，实际执行raw转换、均值root和动量重投影。
原字节报告为 `2026-11-10-78718-geometry-retraction-roundtrip-01.json`，
SHA256 `a362888d83a83af9c0fb6cfc445f7a91d9de6871224a28a122fcb55768e20287`。
本节只读取其中node12/13的原状态和实际roundtrip状态，逐项验证它们属于同一份第17节snapshot。

原算法的两端Q偏置都严格为0；node13的π最大偏置约 $2.22\times10^{-16}$，
node12约 $1.78\times10^{-15}$。高频63的对应偏置分别约
$3.96363\times10^{-19}$、$1.50331\times10^{-18}$。
这些数虽小，但不能只与每点root的条件数比较。

根授权仅对同stage12重建一次base Jac并保存，再对roundtrip输入实际求一次普通段流。
令 $F$ 是已按portRatio归一后的原段流，$y$ 为node13，$z$ 为node12，
$\Delta y,\Delta z$ 为两端真实roundtrip偏置；shooting残差的变化应比较

$$
\Delta R=F(y+\Delta y)-F(y)-\Delta z,
\qquad
\Delta R_{\rm lin}=J(y)\Delta y-\Delta z.
$$

程序 [retraction-bias-stage-flow](../scripts/78718-tail-retraction-bias-stage-flow.mjs)
只执行这两个段流。真实 5a3873/session45893 → 544d27 exit0，3.086秒；
报告 [retraction-bias-stage-flow-01](2026-11-10-78718-tail-retraction-bias-stage-flow-01.json)。
完整44×44的归一Jac、base输出和mean已保存于同名
`-base-jacobian.f64.gz`，15662B，SHA256
`4f477ea21c3e1d98edd1dc76cf3346676a3a809eb49a68a0bef6cec321d61da9`，
以后对新小扰动作线性乘法不必重建本次J。

按真实Q/π单位分块，已有实际浮点量为：

|输出/输入块|最大矩阵元绝对值|最大行绝对值和|
|---|---|---|
|Q←Q|约 $7.2230\times10^5$|约 $7.2541\times10^5$|
|Q←π|约0.0587903|约0.0592793|
|π←Q|约 $2.4211\times10^{13}$|约 $2.4289\times10^{13}$|
|π←π|约 $1.97061\times10^6$|约 $1.98467\times10^6$|

因为本次 $\Delta Q=0$，大到 $10^{13}$ 的π←Q块**没有**进入回缩偏置的线性贡献。
实际相关的是π←π块：63频率的同频元素约 $-1.0836802\times10^6$，
66频率约 $-1.9706073\times10^6$。

base段流再次逐位重现原保存残差。零方向roundtrip后的归一stage残差则从
$3.336601164\times10^{-9}$ 增到 $3.990094934\times10^{-9}$。
实际变化向量的归一最大值约 $1.081470503\times10^{-9}$，
线性预测为 $1.293706447\times10^{-9}$，两者差的归一最大值约
$2.12236\times10^{-10}$。后一个差保留为真实观测；没有把全部偏移说成已被线性化精确解释。

在原最坏63频率，预测变化约 $-4.43909\times10^{-13}$，
实际约 $-5.18568\times10^{-13}$；该项变小。
但66频率从约 $1.86706\times10^{-12}$ 增到
$2.56126\times10^{-12}$，成为新的较大项。
因此不能只跟踪一个原最坏分量，就断言回缩在总体上改善了残差。

作者同时记录的中心差分回缩，在node12/13上都逐位等于原状态。
对于确定的同一段流，这使零方向不再产生本节测得的输入常偏置；
这里没有为该恒等输入额外再跑一次相同流，也没有提前宣称未来完整Newton已经收敛。
原/tight根的第17节四路观察和本节结果共同表明：
消除这次实际坐标roundtrip偏置，比仅因名义阈值而强制tight root更有直接依据。
是否还需加密shootingParts，应依据修正后真实残差和流敏感性继续决定，不能由本节的有限两点观察替代。

## 19. 唯一旧stage12的P16/S16两半段：同轨道而局部增益降低

根的实际fast06采用了中心差分回缩后，残差仍在约 $3\times10^{-9}$ 附近慢降。
为判断下一步数值shooting细分的具体影响，只对第17、18节同一份旧fast05/iteration3的stage12作局部实验，
没有扩大到整尾或另外运行DN。

原stage是P8的rawSegment7/part3，原profile局部S32。
新P16对应同一raw区间的part6和part7，每半段S16；两者都只改变数值分段，
总raw RK密度仍为每原profile256步。这里实际配置的linearSteps也为256，不能误记成512。

先从原node13按**原profile和原步长**实际执行前16个RK步取得中点。
新两半段分别从原node13和这个实际中点出发，各运行一次完整Jac流；
原node12端点不作修改。原完整stage的J及输出直接读取第18节已保存的二进文件，没有重新跑整个旧stage。

程序 [half-stage-gain-diagnostic](../scripts/78718-tail-half-stage-gain-diagnostic.mjs)
真实 ab6859/session5390 → acceb4 exit0，4.267秒。
报告 [half-stage-gain-01](2026-11-10-78718-tail-half-stage-gain-01.json) 为6281B，
SHA256 `72ae5e63a92f87921a762b279b41e5806ac146e54e1a403bfa7e98dd110a18bb`。
实际中点及两半完整J、输出和mean保存在
`2026-11-10-78718-tail-half-stage-gain-01-half-jacobians.f64.gz`，31329B，
SHA256 `5bdaa2fee413b3e306cf4c0e6b4db1cc7bb4932d2b22ccaa17eac27b951f39de`。

|实际局部流|π←π块最大元绝对值|π63←π63同频元素|π63输出行的π块绝对值和|
|---|---|---|---|
|旧完整P8/S32 stage12|约 $1.970607\times10^6$|约 $-1.083680\times10^6$|见第18节已存完整J|
|P16/S16第一半，fine stage25|约2538.806|约−1855.041|约1890.398|
|P16/S16第二半，fine stage24|约4950.734|约−3544.254|约3607.314|

不能把π←π两个标量相乘代替完整Jac的链式法则，因为Q/π交叉块也参与组合。
完整44×44矩阵按 $J_2J_1$ 相乘后，与旧完整J的最大逐项差约1.8711；
用每个旧矩阵元的 $\max(1,|J_{ij}|)$ 缩放后，最大差约 $1.9166\times10^{-12}$。
这是浮点变分计算与组合的差异，保留记录而未当作严格Jac证书。

对实际shape状态则有更强的观测：新第一半输出与原RK中点**逐位相同**，
第二半终点与原完整stage输出也**逐位相同**。
两个局部mean-height相加与旧整段mean相差约 $-8.67\times10^{-19}$，没有把mean说成逐位一致。
由于旧node12仍保留，第二半的初始shooting残差仍是原 $2.141778724366807\times10^{-12}$；
细分并未凭空把已有失配设为零，而是为后续真实Newton提供了增益更小的局部块。

此单段结果支持尝试P16/S16而不改变既有离散轨道；它没有证明所有stage或最终原H都已具有足够数值余量。
根随后实际启动fast07的P16/S16主路线（be42ba/session67954），由根独占观察。
本节到此停止旧图局部扩扫，不追加P32；下一项尾部metric检查等待真正最终原H的自有响应。
