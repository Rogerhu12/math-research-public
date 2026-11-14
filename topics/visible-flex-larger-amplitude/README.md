# 把“瘪易拉罐”的弯曲幅度做大

## 问题

`topics/visible-flexible-closed-surface` 在 flat17 参数下得到了一个数值上的闭曲面等距弯曲族，俗称“瘪易拉罐”，参数和数据见该课题的 HANDOFF。它目前的指标是：
- M12 网格上，$\delta_{\rm hold}/D>0.0528$，reach$/D>0.0312$，$\delta_{\rm E}>0$；
- 整面度量误差约 $2.6\times10^{-8}$。

拿在手里看，弯曲仍然不够明显。本题要把弯曲幅度做大。可以从 flat17 出发，也可以换别的机制。

记号 $D$、握持区 $H$、$\delta_{\rm hold}$、$\delta_{\rm E}$、reach 的定义，都与 `topics/visible-flexible-closed-surface/README.md` 相同。

## 完成标准

给出满足以下全部条件的解，由可复现的脚本生成：

1. $M$ 是连通闭曲面；对每个 $t$，$F_t$ 是 $C^2$ 嵌入，$t\mapsto F_t$ 在 $C^2$ 拓扑下连续。
2. 握持区 $H$ 的内部非空，$\operatorname{diam}F_0(H)\ge0.2\,D$，并且 $\delta_{\rm hold}\ge0.2\,D$、$\delta_{\rm E}>0$。
3. 对每个 $t$，reach $\ge0.03\,D$。
4. 全部 $F_t$ 对同一个度量 $g$ 等距：在整个曲面和全部 $t$ 上，诱导度量相对 $g$ 的最大相对误差不超过 $10^{-6}$。
5. 必须是某个精确解的近似：度量、参数和 $t$ 的范围都不变，在网格、频率和 $t$ 的加密下，等距误差持续下降，直到机器精度或求解容差。
6. 嵌入性和 reach 在全部 $t$ 上检查，不只检查端点。
7. 提供若干个 $t$ 的网格文件（单个文件小于 5 MB），并说明数值解与严格存在性之间还差什么。

**更强的目标：** $\delta_{\rm hold}$ 和 $\delta_{\rm E}$ 越大越好。达到完成标准后继续推进，并报告能做到的最大 $\delta_{\rm hold}/D$、$\delta_{\rm E}/D$ 和 reach$/D$。

以下只算中间进展：
- $\delta_{\rm hold}<0.2\,D$ 或 reach $<0.03\,D$ 的解，不论按环宽或其他长度算比例有多大；
- 带边的曲面片或环带；
- 某些时刻不嵌入的族；
- 误差不随加密趋于零的近似解；
- 只靠层数、尺度比等渐近参数把固有缺陷压小的构造；
- 不可能性或障碍类结果。

## 来源

- `topics/visible-flexible-closed-surface`（flat17 的参数、脚本和数据）、`topics/large-amplitude-twist-flex`、`topics/smooth-unrippled-twist-flex`、`topics/explicit-flexible-closed-surface`、`topics/flexible-surface-model`、`topics/continuous-flexibility-swarm`。
