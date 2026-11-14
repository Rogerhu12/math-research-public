# 外头 cell10：同候选五正积分及完整连续 J 的实际执行

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

这是 [R60](../results/R60-compatible-outer-cell11-complete-mean-defect.md) 条件工具在
相邻实际 cell10 上的独立数据应用。真实 g、完整 M20 端点 Q/L、五积分候选定义、
$\tau=1/64$、192 bit Arb、端点有限逆次数 8 均保持。它支付该候选的连续缺陷上界，
不把该胞元或外头宣称为精确径向解。

## 1. 全部真实面板与原数学函数

`tail_outer_positive_moment_groups.py` 逐字导入已执行的
`tail_outer_positive_moment_panels.py` 数学函数，并检查其 SHA
`d5fb54fe3e0e8db26cabe83fbab6c59ef9f085ce98d2ad26afe9453b50a25d9b`。
所有 source 范围、正 $r_x$ 下界、R26 母积分宽度约束、五个真实加权积分及
prefix/suffix 方法均由原函数计算。新入口直接按9段保存，省略可重建 display 字符串；
每个其余精确字段均经输入/重读 payload SHA 比较。

正式 session `16588`，最终工具块 `c1b6fe`，退出码 0、无终止信号：
61.232 秒，峰 RSS 56500 KiB。共5248面板，九段分别为
$1,951,16,1805,16,1708,16,734,1$。完整覆盖、所有原母区间、精确子宽度和的交集、
五总积分严格正、所需背景正性及全部非 display 字段保留等七门全真。
最大的单文件为2375585字节；没有生成一个注定超过仓库限制的中间全 cell 包。

## 2. 完整 mean、实际径向导数及 J

`tail_outer_candidate_defect.py` 复用已经冻结的候选/完整 mean 残差源，
对这5248个真实面板全扫描。正式 session `78768`，最终工具块 `f525d9`，
退出码0、无终止信号：70.900秒，峰RSS32252 KiB。
完整 mean 小根、R33 工作域、R44 Wiener leading 三门均真。

下表十进制界均向上留有余量；实际比较用 JSON 中完整 dyadic 端点。

| 同一个实际兼容候选的量 | cell10 全径向、全角上界 |
|---|---:|
| $R_\tau=\|P\|_{\tau,1}+\|\bar K\|_{\tau,1}$ | $1.118059\cdot10^{-13}$ |
| $|c|$ | $5.000221\cdot10^{-26}$ |
| 各 source 片自身坐标的 $|c_x|$ | $9.255946\cdot10^{-25}$ |
| 完整非线性源 $\|N\|_{\tau,1}$ | $2.314337\cdot10^{-25}$ |
| 完整非均值第二残差 $\|R_\perp\|_{\tau,1}$ | $1.470805\cdot10^{-12}$ |
| $\|\mathcal J\|_{\tau,1}$ | $1.470805\cdot10^{-12}$ |
| 实际 Darboux 缺陷 $|\mathscr D(\widehat h)|$ | $9.046967\cdot10^{-20}$ |
| 物理非均值第二源 $\|(w/r_x)R_\perp\|_{\tau,1}$ | $4.939556\cdot10^{-17}$ |
| 实际 $\|\widehat h_{\perp,rr}\|_{\tau,1}$ | $2.469601\cdot10^{-17}$ |
| 实际 $|\widehat h_{0,rr}-w_r|$ | $2.860131\cdot10^{-32}$ |

$R_\tau$ 的最坏已包围面板为段3、面板1804。
$\mathcal J$ 的最坏已包围面板为段5、面板10；物理 Darboux 缺陷和物理第二源均在
段3、面板0。完整 JSON 保存各自准确 $x$ 区间、半径及 $w$ 范围。
本次残差仍主要由实际线性候选项贡献；完整有理源和 mean 导数已经计算，没有
因其小而删除。

## 3. 与 cell11 的候选接缝以及仍缺的全局门

两胞元共享 node11 的同一个准确 binary Q/L 和同一真实 $r,w,w_r$。
`finite_saved_endpoint` 的物理两阶 jet 可将 $s=r_x/r$、$\ell=w_x/w$ 中的共同
$r_x$ 消去：$H_r$ 仅依赖 $r,w,Q,L$，$H_{rr}$ 仅再依赖真实 $w_r$。
因此左右 source 坐标长度不同不改变所**定义**的物理端点两阶 jet。
R48 分别精确匹配这些端点，故两个非均值候选以 $C^2$ 拼接。
相同完整 mean 小根的唯一性与 R60 的导数恒等式给相同 mean slope/物理导数；
mean 高度必须从一个全尾常数统一积分。

这只是两个候选之间的兼容接缝，不是两条精确解的接缝。
node12 还要支付 R58 真内头与保存候选的实际低动量和全部高迹差；
cells0–9 还没有本工具的连续证书；实际外端有限 Schur 逆、全部高频有界核、
参数域包含及前缀接合仍分别缺失。
具体需要的输入与正核方案见
[外头 Green/Schur 支付表](2026-11-12-tail-outer-green-schur-payment-plan.md)。

完整源、九段数据、正式资源与结果由
[cell10 稳定执行清单](2026-11-12-tail-outer-cell10-executed-manifest.json)列出。
清单中的数学 payload 摘要、输入 SHA 与原命令足以在环境丢失后真正重算，
不能用摘要中的数值重造一次未执行的结果。
