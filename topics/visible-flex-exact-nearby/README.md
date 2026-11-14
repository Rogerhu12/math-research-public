# 证明“瘪易拉罐”附近有精确解

> 2026-11-14 从私有仓库 `Rogerhu12/math-research` 迁入本公开仓库（路径不变）；之后只在本仓库工作，计算用本仓库的 GitHub Actions（根 README 规矩第 13 条）。

## 问题

`topics/visible-flexible-closed-surface` 用 flat17 参数，得到了一个数值上的闭曲面等距弯曲族，即“瘪易拉罐”，参数和数据见该课题的 HANDOFF。它在 M12 网格上的指标是：
- $\delta_{\rm hold}/D>0.0528$；
- reach$/D>0.0312$；
- 整面度量误差约 $2.6\times10^{-8}$。

另外，`topics/large-amplitude-twist-flex` 有一个 5% 振幅的数值解，`topics/smooth-unrippled-twist-flex` 也有数值解。本题要证明：在这类数值解附近存在一个精确解，弯曲幅度是看得见的。从哪个数值解出发都可以，也可以自己另造近似解。

$D$、握持区 $H$、$\delta_{\rm hold}$、$\delta_{\rm E}$ 和 reach 的定义，都与 `topics/visible-flexible-closed-surface/README.md` 相同。

## 完成标准

完整证明存在连通闭曲面 $M$、度量 $g$ 和一族 $F_t:M\to\mathbb R^3$（$t\in[0,1]$），满足：

1. 每个 $F_t$ 都是 $C^2$ 嵌入，并且对 $g$ **精确等距**；$t\mapsto F_t$ 在 $C^2$ 拓扑下连续。
2. 存在握持区 $H$，内部非空，$\operatorname{diam}F_0(H)\ge0.2\,D$，满足 $\delta_{\rm hold}\ge0.05\,D$ 且 $\delta_{\rm E}>0$。
3. 对每个 $t$，reach $\ge0.03\,D$。

可以用计算机辅助证明。用到的程序和输入写在仓库里，数值误差和舍入误差都要在证明里得到严格控制。

**更强的目标：** 对 $\delta_{\rm hold}\ge0.2\,D$ 或 $\delta_{\rm E}\ge0.05\,D$ 的解证明同样的结论；或者让精确解为 $C^\infty$。

以下只算中间进展：
- 只对截断到有限个频率的方程，或只对线性化方程成立的结论；
- 依赖没有证明的估计、没有严格控制误差的浮点计算，或者没有付清的常数的条件性结论；
- 振幅达不到上面比例的存在性，包括 R520 那样的小振幅存在性；
- 带边的曲面片或环带；
- 不可能性或障碍类结果。

## 来源

- `topics/visible-flexible-closed-surface`、`topics/large-amplitude-twist-flex`、`topics/smooth-unrippled-twist-flex`（数值解、脚本和数据）。
- `topics/quantitative-newton-twist-flex`、`topics/continuous-flexibility-swarm`（R520 及其依赖）、`topics/explicit-flexible-closed-surface`、`topics/smooth-flexible-closed-surface`。
