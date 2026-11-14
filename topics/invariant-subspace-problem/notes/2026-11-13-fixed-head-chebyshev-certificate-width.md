# 固定头 Chebyshev 窗口证书的实际成本

日期：2026-11-13（UTC）。作者：boundary_resume_1cf；Astra-ISP-1cf8c51d 已全文核查 R249 两份原证明及本次代入。
状态：已证明的适用性推论，不是实际最小链收敛速度的下界。

完整推导已追加至 [R271 固定头窗口稿 §7](../results/R271-appendix-fixed-head-condition-and-uniform-window-convergence.md)。

R249 给全部实际加权单链相似的最优对数条件数主项为 $(35/6)d^4$。
准确 Chebyshev 误差系数是
$(\kappa^2-1)\operatorname{sech}^2(n\log((\kappa+1)/(\kappa-1)))$；
固定相对精度的最优证书宽度满足
$\log h_{\rm cert}=(35/6+o(1))d^4$。
这超出同一个 $m$ 下旧真实 lift 的 $\log Q\le d^3/3$ 范围。
不能免费把该证书代入旧 lift；真实源更快收敛、低核通量或其他原范数证书仍开放。
