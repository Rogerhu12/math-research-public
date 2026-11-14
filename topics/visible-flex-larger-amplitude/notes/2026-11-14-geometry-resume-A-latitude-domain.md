# 真 A 的纬线圆化与大核心的陡降点域门

作者：geometry_design，AI 辅助，2026-11-14。

**状态：原有限场的数值读出，不是新解或全闭曲面的认证。** 读取本轮恢复的 A `fixed-view-r1` 和原 raw 数组，经原 loader 确认其径向表示为五次 physical polynomial、2590 个节点、97 个状态。未重算 ODE、Jacobian 或 Newton，也没有把原场重新作三次插值。

对 342 个子午站点、每纬线 768 个原角样本，直接从原场的两阶角向导数计算三维纬线曲率 $\kappa_{\rm lat}$。固定 warped metric 的正则点域要求

$$
1-\left(\frac{a'}{a\kappa_{\rm lat}}\right)^2>0.
$$

在实际 A 上，半径跨度与该点域量的变化如下。半径跨度是实际水平距离 $\max\sqrt{X^2+Y^2}-\min\sqrt{X^2+Y^2}$，不把其保存 chart 的一个 Fourier 系数当作不依赖参数化的形状指标。

| 位置 | s | a' | $a\kappa_{\rm lat,min}$ | 半径跨度 | 竖直跨度 |
|---|---:|---:|---:|---:|---:|
| 核 | 0 | 0 | .66548319 | .25063814 | 0 |
| Hermite 末 | .88005441 | .32037232 | .90134653 | .13004183 | .03468672 |
| boost 末 | 1.00643198 | .83322645 | .92038199 | .09585295 | .06228639 |
| 下降 turn 末 | 1.39186605 | -.98 | .98897743 | .01261630 | .06932592 |
| loop 入口 | 2.25987787 | -.985 | .99566226 | .00116036 | .00261378 |
| loop 后回到 r=.35 | 3.14101575 | -.985 | .99998359 | .00000379 | .00009123 |

最小采样点域余量为 `.005131924804641308`，出现在整段末端桥范围；下降 turn 末为 `.018072576856314693`。这解释了为什么 A 能进入 $|a'|=.98$ 的陡降：其实际纬线已显著圆化。它不意味着同一背景可直接接上任意大核。

作为对照，完整 R225 核在本轮同 g 的 M128 入口 $s=.9$ 只有 $a\kappa_{\rm lat,min}\approx .49514$。所以连接到 $|a'|=.98$ 时，纬线形状的改变是实际约束；只在背景上缩短 turn，或者降低某个背景曲率 K，不能替代这一点域检查。当前大核 BVP 继续允许高核模调整，并保留原场点域；本页没有声称该调整已经完成陡降或闭合。

源码：`computations/geometry_20261114_A_latitude_domain_readout.py`。小摘要：`2026-11-14-geometry-resume-A-latitude-domain-summary.json`，含各 phase 的端点、完整输入 hash 与完整读出 hash。实际读出终端退出 0。复现需要按 A 恢复 manifest 先还原原保存场，随后：

```bash
python computations/geometry_20261114_A_latitude_domain_readout.py --runtime-topic RUNTIME_TOPIC --source-topic SOURCE_TOPIC --saved RUNTIME_TOPIC/notes/2026-11-13-strong-q126-m32-fixed-view-r1.json.gz --port RUNTIME_TOPIC/computations/alternative-neck-provider-smallcut30-port32-r2048.json --angular 768 --stations 321 --out A-latitude-domain.json
```

`SOURCE_TOPIC` 为本轮恢复并逐源核对的 `visible-flexible-closed-surface` 源目录；`RUNTIME_TOPIC` 是保存场和原消费源码完整恢复后的本课题目录。读出过程还验证 polynomial degree 为 5，拒绝把三次替代场当作同一输入。
