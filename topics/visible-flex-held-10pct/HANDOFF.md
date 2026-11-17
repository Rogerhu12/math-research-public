# HANDOFF — visible-flex-held-10pct

维护会话：**Astra-held10-f00f08c9-20261117**（AI）。开始：2026-11-17 19:55（UTC+8）。状态：**进行中，尚无满足全部完成标准的候选**。

## 目标、规则与同步

构造连通闭曲面的连续 $C^2$ 等距嵌入族，固定有内点握持区 $H$，$\operatorname{diam}F_0(H)\ge0.2D$，整像 Hausdorff 变化 $\delta_{\rm hold}\ge0.1D$，含反射取商的 $\delta_{\rm E}>0$，全时 reach $\ge0.03D$。同一固定度量、物理参数和时间范围下，最大相对度量误差不超过 $10^{-6}$ 并随空间、频率、时间加密下降。材料点位移不是 $\delta_{\rm hold}$。

- 已部分克隆、仅稀疏检出本题，执行真实 `git pull --rebase origin main`；根 README（含授权）和本题 README 全文已读。
- 已读规则提交：`81510c5054544f1383de024dea494123d558dcc0`。2026-11-17 20:43:45（UTC+8），真实 pull/rebase 后双 README 差异为空。下次真实 pull 最迟 21:43:45；每次 pull 后比较这两份 README，只读变化并立即执行。
- 每个有意义的新结论与本文件同时更新，提交前 pull、核规则后普通 push；非快进立即 pull --rebase 再推。禁止 force push。令牌只在命令行临时使用。
- 只有完整证明进 `results/`；数值证据和缺口分别标明。可重算数据、网格和渲染不提交，只保存生成脚本、参数、运行标识和 SHA-256；单 Markdown <100KB，本文件 <10KB。不写根 LOG。

## 开题核对

1. 本题此前只有 README，无既有结果；已创建本 HANDOFF、open 和 log。
2. 已读 `visible-flexible-closed-surface/README.md` 的指标定义及其 HANDOFF。其 R114 声称固定几何的数值基础结果：$D\le3.787020263962$、$\delta_{\rm hold}/D>0.0527832$、reach$/D>0.0312033$、metric $\le1.2567\cdot10^{-9}$。这不是本题的 10% 解，当前仅作为待定点核验的来源，未独立重算或升级为严格存在。
3. 已读 `visible-flex-larger-amplitude`、`visible-flex-new-mechanism`、`visible-flex-exact-nearby` 的 HANDOFF：它们尚无满足各自主目标的完整候选，有限参数优化与条件证明不能直接替代本题验收。避免重复其已登记的推导；优先提取几何公式和简洁生成器。
4. 文献核查已记入 [开题核查](notes/2026-11-17-literature-and-source-scope.md)：Sabitov 的滑动柱/锥像集合不变，球盖拼接还缺材料兼容；Ghomi–Qiu–Raffaelli–Zhang 2026 §1 明说其非刚性构造尚不知是否连续柔性，不能把 $X±εY$ 当固定度量路径；T-surfaces 的带边显式族仍缺周期闭合。主会话已核前三者原始入口及 Ghomi 全文关键段。未取得全文的条目已逐项标明。
5. 定点读 R114、R17、R25 及现成刚体片审读：flat17 过渡前缀切口高度约1.7713、尾仅增高约0.052，主要直径成本在前缀。R114 的完整相位周期已全覆盖；现成开放运动刚体片不能直接提供杠杆。以上是沿用原结果，不重复登记新定理。
6. 旧题约0.063的具体记录是未解暖场的有限点云双向扫描，不能当成已闭合/已收敛实体的连续上界；本题不会据此宣称现有10%解。

## 当前工作

**新主线R3：换握持放大。** 实际圆弧局部片的phase运动为QαX+bα；对整个族取逆刚体运动固定该片，D/reach/g/δE全保留。三重对称给整像dH≥√3|c|sin(kα/2)。k4、|c|≥.88、A=.14、D≤3.9、reach≥.118、H跨s±.42给held/D>.10800及Hdiam/D>.21519。前提仍未实现；true_a在做圆弧外支撑基及真实prefix，new_construction独立算窗口/传播，主会话保持完整集合证明与marker/闭合预算。

- 主会话：核对 R114 的实际构造，研究可见振幅与完整闭合尺寸的关系，建立本题的简洁可复现计算。
- 并行 `true_a_analysis`：既有 true A 族的位移、直径和 reach 结构；只读原题，不重复其运行日志。
- 并行 `new_construction`：新机制与闭合/握持设计。
- 并行 `literature_mechanisms`：文献核验已成；转入 Gauss–Codazzi 短前缀与平端退化的独立分析。

复现与精化：`scripts/recover_prefix.py` + `prefix_recovery_manifest.json` 定点恢复旧q18/q20开放前缀，数据仅落scratch。q18保持物理delta=.17053856686761762与角向chart不变，M10→M16的采样metric L1从1.61704e-6降到2.54853e-7；端口非均值高度仍约.00976。M24仍在计算，不宣称完成；详见 notes/2026-11-17-archived-prefix-recovery-and-fixed-g.md。

小切口计算：新增 `scripts/smallcut_prefix_sweep.py` + SHA清单，把cut降至.30/.35并重算线性chart与真实非线性前缀。r=.30、curvature=4、peak_fraction=.2已在新恢复环境通过q=.02/.04/.06；q=.06 metric≈4.07e-8、κ≈4.416、端口H≈.000727。旧p=.5在更小q出现负根域失败，不是不存在证明。本题独立 `.github/workflows/held10-smallcut-research.yml` 以最多2个并发跑8个不同新桥参数，输出仅日志摘要/hash，手动dispatch被GitHub以`Resource not accessible by personal access token`拒绝（HTTP403），现改为仓库已授权的普通push/指定请求文件触发；尚无CI数值结果。

三场BVP：已实现完整Gauss–Codazzi并精确约束圆领端两jet；B=.9的24控制/4模重建metric约.0289，B=.7约.444，均淘汰。低频/末端残差不随简单加密消失，详见 notes/2026-11-17-gc-complete-bvp-attempts.md。继续小切口高振幅与振荡端表示，不将有限失败升级为不存在定理。

直接半帽：16次已结束试验的源码、参数和hash已存 `scripts/cap_design/`；负K入口最好一轮metric=.01410，密网曲率14.455，见证/支撑采样预算接近达标但等距失败。放宽E的后续曲率18.707，淘汰；见 notes/2026-11-17-direct-cap-design-batches.md。继续真实弧长重参数化及角模扩充。

新短尾：已恢复旧q20前缀完整端口。新短尾固定E版metric≈.002、κ≈12.12；自由E版独立网格发现退化E与κ≈5.7e6，明确淘汰（notes/2026-11-17-first-short-collar-trials.md）。继续较短弧长、曲率/正支撑约束和厚尾设计。两条路线均未获全部条件。

已证新结论：[R1](results/R1-mild-ellipse-ten-percent-geometry-window.md) 给 $A=1,B=.7$、$r_{cap}=.25$ 的具体条件窗口：完整包络 $r\le1.05,|y|\le.75,|z|\le.6$ 与支撑≥.08、曲率≤12时，held/D≥.10336、Hdiam/D≥.20672、reach/D≥.03307。连接器、连续包围、固定g精化及δE>0仍未付，**不构成完成**。R2给三场Gauss–Codazzi方程及平面圆领端点引理；短椭圆圆整试算在0.28弧长内降径向差，但仍未圆领，见 notes/2026-11-17-gc-short-prefix-experiments.md。下一项见 [open.md](open.md)。本题未达标准，继续推进；达到后继续提高比例。
