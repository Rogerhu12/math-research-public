# 接手后的四来源和一手文献范围复核

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。继承的[前轮来源记录](2026-11-26-current-four-source-topics.md)仍保留；本页只记新的已读来源，不执行来源科学，不重取旧数组或借用在途日志。

## 1. 四课题的实际交接来源

root 已逐份读取公开提交 `7fc831211a88a951b855b667eb5384b6bb90d34a` 的四份完整 HANDOFF；先前一次差分输出截断，随后补读了全部新文本，未把截断当全文。所读版本是此处固定提交，并非声称这些并行课题以后没有新结果。

| 课题及固定来源 | 已读 HANDOFF blob |
|---|---|
| [visible-flexible-closed-surface](https://github.com/Rogerhu12/math-research-public/blob/7fc831211a88a951b855b667eb5384b6bb90d34a/topics/visible-flexible-closed-surface/HANDOFF.md) | `090a66575a45c3309c319f71104c1b46cf13577b` |
| [visible-flex-larger-amplitude](https://github.com/Rogerhu12/math-research-public/blob/7fc831211a88a951b855b667eb5384b6bb90d34a/topics/visible-flex-larger-amplitude/HANDOFF.md) | `2edf28871f1e34a7114c1acf3f05d92ed3636eba` |
| [visible-flex-exact-nearby](https://github.com/Rogerhu12/math-research-public/blob/7fc831211a88a951b855b667eb5384b6bb90d34a/topics/visible-flex-exact-nearby/HANDOFF.md) | `990111038657dcef0f3bd63320048ddb2fc195eb` |
| [visible-flex-held-10pct](https://github.com/Rogerhu12/math-research-public/blob/7fc831211a88a951b855b667eb5384b6bb90d34a/topics/visible-flex-held-10pct/HANDOFF.md) | `f4a3cd2f5b96215d93502413d045d66b5704f0d8` |

- 基础闭面：R245/h487 的实际11段网格及连续 metric 上界约8.211825e−7、reach/D>.03109495、held/D>.05278322已登记；固定 g 精化到机器/求解容差和更大幅度仍欠。新的 M48/更密角网等在途结果不借用。该小幅场不能提供本题 .3D 整像变化。
- 更大振幅：完整旋转/端点循环中的实际 metric 仍在 .035 量级；R706 同 g 恒等不是连续精化结果。低维端点初始失败没有产生新合格场；尚无可整体移交的宏观闭族。
- 精确邻近：几何 held>.05075888D、reach≥800D/25039 等为完整匹配及误差条件下的预算。真实低频逆、负侧、均值/规范 Schur 和全 BVP 仍未闭。新的紧支撑均值根小，并未同时支付非均值、高度、周期条件；R144 前向全检查曾失败，不消去这段历史。
- 10%握持：λ=.064/M40 的有限设计有 RMS约9.9591e−7、metric约2.7569e−7及小端点误差，但 fullH、λ=1闭合和固定 g 精化仍欠。不能把旧前缀证书扩写成完整 .1D 闭族。

以上都没有在所读版本提供可直接移交、本题全部主门同时合格的对象。这是具体来源资格判断，不是一般不存在定理；具体工具若用于新场，须满足该工具的同场输入，不能拼接不同候选的数字。

## 2. 一手文献入口的当前范围

本会话已查询并于本轮再次打开两份原始提交页，确认作者、版本日期、摘要和声明范围；此处没有声称逐行核完论文或其形式化工程。

1. Boyang Hu, [Smooth isometric bending of a closed sphere](https://hexagonmath.org/2611.00534v1)，Hexagon v1，2026-11-16，119页。摘要声明平滑闭球面的周期等距族，像不全合同，固定内盘/互补帽；机制用旋转度量的非径向盘、两端平坦的 Darboux 方程与 Nash–Moser。提交页还声明主定理已形式化。这里仅登记原作者声明；本题的具体 .2D/.3D/.03D、同一 g 可再生精化及实际完整几何预算并不因摘要或形式化链接自动支付。
2. Mohammad Ghomi, Hongda Qiu, Matteo Raffaelli, Yuetong Zhang, [Nonrigidity of smooth tight surfaces](https://arxiv.org/abs/2611.17269)，arXiv v1，2026-11-12，16页。摘要的对象是正亏格闭紧曲面的不合同等距嵌入，且体积不同。摘要没有给出连接二者的连续等距族；因此不将其离散非刚性直接用作本题连续柔性构造。

本轮选择仍是直接完成已登记的三条实际函数/有限参数输入及其闭面几何，复用已有真证明。文献范围复核不取代解方程，不关闭任何新方向；若后继需要引用论文中具体引理，先读完整引理与条件再使用。
