# 可弯曲闭曲面：握持变化量做到直径的 10%

> 2026-11-17 作者开题，直接建在本公开仓库，计算用本仓库的 GitHub Actions（根 README 规矩第 13 条）。

## 问题

现有满足"闭合、嵌入、加密收敛"要求的可见弯曲闭曲面，握持变化量都只有直径的几个百分点：
- “瘪易拉罐”（flat17，`topics/visible-flexible-closed-surface` 的 R114）：$\delta_{\rm hold}/D>0.0528$，reach$/D>0.0312$，刚过该课题的完成线 $0.05/0.03$。
- `topics/visible-flex-larger-amplitude` 的 true A 族：$\delta_{\rm hold}/D$ 不超过约 $0.063$。

本题要找握持变化量至少为直径 10% 的可弯曲闭曲面。机制不限，可以从已有的族出发，也可以用别的构造。

$D$、握持区 $H$、$\delta_{\rm hold}$、$\delta_{\rm E}$、reach 的定义，都与 `topics/visible-flexible-closed-surface/README.md` 相同：$\delta_{\rm hold}$ 不做任何刚体对齐；所有比例都用整个曲面的直径 $D$ 归一，不与环宽、经线长等其他长度混用。

## 完成标准

给出满足以下全部条件的解，由可复现的脚本生成：

1. $M$ 是连通闭曲面；对每个 $t\in[0,1]$，$F_t$ 是 $C^2$ 嵌入，$t\mapsto F_t$ 在 $C^2$ 拓扑下连续。
2. 握持区 $H$ 的内部非空，$\operatorname{diam}F_0(H)\ge0.2\,D$，并且 $\delta_{\rm hold}\ge0.1\,D$、$\delta_{\rm E}>0$。
3. 对每个 $t$，reach $\ge0.03\,D$。
4. 全部 $F_t$ 对同一个度量 $g$ 等距：在整个曲面和全部 $t$ 上，诱导度量相对 $g$ 的最大相对误差不超过 $10^{-6}$。
5. 必须是某个精确解的近似：度量、参数和 $t$ 的范围都不变，在网格、频率和 $t$ 的加密下，等距误差持续下降，直到机器精度或求解容差。
6. 嵌入性和 reach 在全部 $t$ 上检查，不只检查端点。
7. 提供若干个 $t$ 的网格文件（单个文件小于 5 MB），并说明数值解与严格存在性之间还差什么。

**更强的目标：** $\delta_{\rm hold}$ 和 $\delta_{\rm E}$ 越大越好；或者严格证明存在满足完成标准比例的精确解。达到完成标准后继续推进，并报告能做到的最大 $\delta_{\rm hold}/D$、$\delta_{\rm E}/D$ 和 reach$/D$。

以下只算中间进展：
- $\delta_{\rm hold}<0.1\,D$ 或 reach $<0.03\,D$ 的解，不论按环宽或其他长度算比例有多大；
- 带边的曲面片或环带；
- 只有 $C^1$、带折痕或带奇点的曲面；
- 某些时刻不嵌入的族，或只有两个端点而没有连续族；
- 误差不随加密趋于零的近似解；
- 只靠层数、尺度比等渐近参数把固有缺陷压小的构造；
- 依赖尚未证明或尚未数值确认的条件的构造；
- 不可能性或障碍类结果。

开工前先核对文献与本仓库现状，把结果写进 HANDOFF。数据按根 README 规矩第 15 条处理，不要把大数组、网格或渲染图读进对话。若得到满足条件的解，把参数、脚本和复现方法写在 HANDOFF 开头。

## 来源

- 本仓库：`topics/visible-flexible-closed-surface`、`topics/visible-flex-larger-amplitude`、`topics/visible-flex-new-mechanism`、`topics/visible-flex-exact-nearby`。
- 私有仓库 `Rogerhu12/math-research`：`topics/continuous-flexibility-swarm`、`topics/large-amplitude-twist-flex`、`topics/smooth-unrippled-twist-flex`、`topics/explicit-flexible-closed-surface`、`topics/flexible-surface-model`。
- 相关的经典微分几何文献，以核查为准。
