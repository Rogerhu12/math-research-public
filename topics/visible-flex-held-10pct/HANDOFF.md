# HANDOFF — visible-flex-held-10pct

维护会话：**Astra-held10-f00f08c9-20261117**（AI）。开始：2026-11-17 19:55（UTC+8）。状态：**进行中，尚无满足全部完成标准的候选**。

## 目标、规则与同步

构造连通闭曲面的连续 $C^2$ 等距嵌入族，固定有内点握持区 $H$，$\operatorname{diam}F_0(H)\ge0.2D$，整像 Hausdorff 变化 $\delta_{\rm hold}\ge0.1D$，含反射取商的 $\delta_{\rm E}>0$，全时 reach $\ge0.03D$。同一固定度量、物理参数和时间范围下，最大相对度量误差不超过 $10^{-6}$ 并随空间、频率、时间加密下降。材料点位移不是 $\delta_{\rm hold}$。

- 已部分克隆、仅稀疏检出本题，执行真实 `git pull --rebase origin main`；根 README（含授权）和本题 README 全文已读。
- 已读规则提交：`582b93d463ca19db76d83fddafbd9e94e3d283a4`。2026-11-17 约 20:00（UTC+8）。下次真实 pull 最迟 21:00；每次 pull 后比较这两份 README，只读变化并立即执行。
- 每个有意义的新结论与本文件同时更新，提交前 pull、核规则后普通 push；非快进立即 pull --rebase 再推。禁止 force push。令牌只在命令行临时使用。
- 只有完整证明进 `results/`；数值证据和缺口分别标明。可重算数据、网格和渲染不提交，只保存生成脚本、参数、运行标识和 SHA-256；单 Markdown <100KB，本文件 <10KB。不写根 LOG。

## 开题核对

1. 本题此前只有 README，无既有结果；已创建本 HANDOFF、open 和 log。
2. 已读 `visible-flexible-closed-surface/README.md` 的指标定义及其 HANDOFF。其 R114 声称固定几何的数值基础结果：$D\le3.787020263962$、$\delta_{\rm hold}/D>0.0527832$、reach$/D>0.0312033$、metric $\le1.2567\cdot10^{-9}$。这不是本题的 10% 解，当前仅作为待定点核验的来源，未独立重算或升级为严格存在。
3. 已读 `visible-flex-larger-amplitude`、`visible-flex-new-mechanism`、`visible-flex-exact-nearby` 的 HANDOFF：它们尚无满足各自主目标的完整候选，有限参数优化与条件证明不能直接替代本题验收。避免重复其已登记的推导；优先提取几何公式和简洁生成器。
4. 文献核对进行中：滑动弯曲、旋转对称度量的非旋转嵌入、可固定边界的光滑帽。未核实文献不作为外部定理。

## 当前工作

- 主会话：核对 R114 的实际构造，研究可见振幅与完整闭合尺寸的关系，建立本题的简洁可复现计算。
- 并行 `true_a_analysis`：既有 true A 族的位移、直径和 reach 结构；只读原题，不重复其运行日志。
- 并行 `new_construction`：新机制与闭合/握持设计。
- 并行 `literature_mechanisms`：原始文献核验，明确带边与闭合的区别。

已证新结论：暂无。下一项见 [open.md](open.md)。本题未达标准，继续推进；达到后继续提高比例。
