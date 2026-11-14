# R133 补充：实际正高块内主体与真实切口迹的双输出

## 本次实际结论

公开 Actions [43639514776](https://github.com/Rogerhu12/math-research-public/actions/runs/43639514776) 的 consume job 实际执行了新消费者，11 个科学门全部通过，child return code 为 0。科学运行用时 30.811261697999996 秒，子进程记录 35.001307279 秒。它消费原 4650 格正区证书和原 7721 格 M32 双向交叉费用；只把正区旧格在准确 $c=9/10$ 分开，得到 4651 个新权重格和完整的双向源平方核。

原 4650 次 target、Riccati 参考、高块收缩、帽残差和有限 Green 全部没有重算。本条只授固定物理 $\eta_0$、原 $\nu$、仿射参数偏移 $0$、修补 M32 中心的给定完整低头正高块接口。所有 $|j|\ge97$ 均被覆盖。

## 两种实际输出保持独立

采用原同一全局 $Z$ 参考。新输出分别是正区内段 $[r_*,9/10]$ 上的完整高 pair 普通径向 $L^2$，以及准确 $r=9/10$ 的高 even 圆周 $L^2$ 迹。后者直接消费全频重构行，不由径向 $L^2$ 推迹。

准确切口落在原正区第 3304 格内。其已付全频 $W$ 下界大于 $0.7736940625718$，因而
$$
\|h_{2,H}(9/10)\|_{L^2_\phi}
 <0.595330881947\,\|Z(9/10)\|_{\ell^2}.
$$
这是原完整重构门与新 even 行门的合法最小值；独立 even mean 属于低头，未被删除。内正主体的重构平方积分小于 $1.454093548215$，根 collar 则按真实覆盖长度不超过 $9/10^6$、完整重构因子 $3$ 单独相加。

下面每个数均向外取大于原 Arb 上端的十进制数。七列顺序、单位和全部源定义继承原正根图合同；各行输出按对应输入范数的正线性组合相加。

| 原输入 | 根 unstable $Z$ 输出 | 正内主体 pair $L^2$ | 切口高 even $L^2$ |
| --- | ---: | ---: | ---: |
| 根 stable $Z$ 端口 | 0.436007718096 | 1.731669643158 | 0.854899741296 |
| collar 普通 $L^2_rH^{1/3}$ 源 | 0.012924069463 | 0.015585026789 | 0.007694097672 |
| 正主体普通 $L^2_rH^{1/3}$ 源 | 0.181137705128 | 0.218432436851 | 0.107836869748 |
| 外 mean、完整 head 与加权跳负荷 | 1.436007718096 | 1.731669643158 | 0.854899741296 |
| collar 加权 affine 跳负荷 | 1.436007718096 | 1.731669643158 | 0.854899741296 |
| 接口 stable $Z$ 跳 | 0.435529048857 | 1.731048644804 | 0.854614774715 |
| 接口 unstable $Z$ 跳 | 1.000478669240 | 0.009022789539 | 0.000284966581 |

## 对给定低头源的新实际列

原 M32 的已知 $A_{HL}$ 有完整输出带 $97\le |j|\le160$。本次只对这条已知有限带源付 $(1+640^2)^{1/6}$；没有将该有限带支持转授给未知高反馈。

旧 4650 行的 source frame、真实衰减与新 7721 行的逐格 $c_{HL}$ 全部保留。两次新平方核按互不相交的两个源窗计算。所获原对角解算器的 $Z$ 上确界费用为：

| 低头输入窗 | 新平方核门 | 原统一乘积门 |
| --- | ---: | ---: |
| $[r_b,9/10]$ | 130.227357408 | 143.076650932 |
| $[9/10,25/8]$ | 39.985132333 | 132.007461328 |

每个窗只在两个完整合法门中取小。原 source-frame 字段与 reconstruction 字段保持各自单位；没有把它们当成相同记录。根 collar 的 head 源另付真实完整项，然后用互不相交径向输入窗的欧氏合并，把 collar 与内主体列合成为完整内头列。

令 $H_{\rm in}=\|h_L\|_{L^2([0,9/10]\times S^1)}$，$H_{\rm cap}=\|h_L\|_{L^2([9/10,25/8]\times S^1)}$。由这些已知 head-driven 源贡献的新界为
$$
\begin{aligned}
\|Z_{u}(r_*)\|&<
187.497517220\,H_{\rm in}+57.418958639\,H_{\rm cap},\\
\|h_H\|_{L^2([r_*,9/10]\times S^1)}&<
226.101680824\,H_{\rm in}+69.241039838\,H_{\rm cap},\\
\|h_{2,H}(9/10)\|_{L^2_\phi}&<
111.623062290\,H_{\rm in}+34.183279287\,H_{\rm cap}.
\end{aligned}
$$
这里还要加上上表中根 stable、独立源、外 mean/head 端迹和各真实接口跳列。外帽低头 $H_{\rm cap}$ 与终端低头/mean 迹不能置零，也不能由内段 $H_{\rm in}$ 免费替代；它们需要真实全模帽 Poisson 接口。非正区高解和根 incoming 端口仍由独立的负区返回问题决定。

## 原字节和过程

本次目录为
[notes/positive_high_weighted_body_cut_ci/run-43639514776-1-positive-high-weighted-body-cut](../notes/positive_high_weighted_body_cut_ci/run-43639514776-1-positive-high-weighted-body-cut)。

- native：native/complete-positive-high-weighted-body-and-cut-ports.json.gz，3,715,980 字节，SHA256 为 54b3940463e8efca02c136fdb2fc5bd2a0ff8a7f57b604db86ba67cec620e6b2。
- 仓库过程：process.json，13,346 字节，SHA256 为 cecc2d2e703d849f8c216303a7010befa71a0e9d2c81b0cb57c7af417fe7aad1。
- 精简证据：evidence/complete-positive-high-weighted-body-cut-summary.json，35,088 字节，SHA256 为 8fdca559e91e67f11e864ddb4fab02c48a383f6be292070e3ff9a538e5f941d5。
- 科学 source：scripts/fourfold_codazzi_positive_high_weighted_body_cut_ports.py，SHA256 为 f12f2ee1e0e3d64ac59f4e126a431af49eb95686de8142184343ad59ae85253f。
- 原正主体 native eefb94952a409473fed7f9c34afc9214a3346d8c3b19ed7e0a7fc6fd06f48a68、原图 native 2425a0338b958be5d7fb48c955b5a5ce59348f05f1832ab50a81d6cf7dbbc501、原 body-cross native a12fd95f9ebaf50cc6fb0db7c97d0416152c985b739ad19fcdc730a12c82ef09 均保持原字节。

实际读入的原 body 和 cross 的 artifact 过程 SHA 分别是 48baba77aaff9956c66357da2f52812a53b9b6efca3708ce3bea418beaed3f65 和 cb669c338a5ead80fcbcecb7e3cd43413f44ace9d3d9a05b416f6fc1a82315dc；它们与各自仓库过程快照分别保存，未伪称字节相同。

本次 4 次真实 pull 的 README 差异均为空。读到的 after 提交顺序为 b7d065c79b5170248517f7b7a929b4c00147d259、同一提交、29e2aa699c783e7cdc362b5b58d107ad47a4fe76、a62b45b24db9925f136b288481b257ab4fea8839。已人工审读规则提交仍为 ee26c0a65a2e63c15f2ccfba6714181584416542。

## 范围

本条完成两个不同输出及给定低头的两窗源列，不授全低高 Schur、负高 BVP 逆、非零 $\delta$ 转移或真正全 PDE 的 $\nu$ 响应误差。上述列是当前可用上界，不能解释成真实反馈的下界。有限 193 响应已成的 $1/200$ 门与本条保持不同证明范围；它仍需完整未知高反馈接合。

参见 [双输出合同](../notes/2026-11-14-R133-positive-high-inner-body-cut-trace-contract.md)、[实际 M32 body-cross](R133-supplement-actual-M32-body-cross-weighted-Green.md) 及 [全频帽边界和 Poisson 接口](R133-supplement-full-frequency-moving-cap-boundary-and-Poisson-interface.md)。
