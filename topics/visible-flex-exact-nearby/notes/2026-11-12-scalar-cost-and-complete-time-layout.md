# 真实标量采样成本与完整时间布局的缩减

本次只比较准确 $\delta_5$ 同一已付实际域，不改变主场公式、无限 Fourier
尾或真实时间域。完整重放入口和数据分别保存在下列脚本与 JSON 中。

## 1. 时间布局的安全缩减

原 adaptive 选择将保留时间次数一次加 8，可能越过已足够的布局。
`scripts/fourfold_minimize_time_layout.py` 接收已经通过的
`(N,K,Nt,m)` 和**原来的完整 budget 函数**，向下逐个偶数 $N_t$ 尝试
$m=N_t$，每次重新付全部时间 alias、时间尾、角 alias 和完整角尾。
阈值仍为原 `target/4` 的有向下界；没有放宽误差目标。

API 为

```python
new_layout, trials = minimize_time_layout(budget_function, old_layout,
                                          target=original_target)
```

这里只选择零节点噪声的解析布局，之后仍调用原入口核实际节点球、DFT、
精确系数选择及压缩费用。第一次失败即停止，不宣称穷尽所有 $m$ 后取得
全局最优。field 和 finite-density budget 使用同一接口。

从实际已经完成的叶证书重放，结果为：

| 段 | 场不同时间节点 | 密度不同时间节点 | 本次预算搜索 CPU |
|---|---:|---:|---:|
| 14 | $19\to16$ | $19\to16$ | 场 0.038 秒，密度 0.271 秒 |
| 13 | $19\to16$ | $19\to16$ | 场 0.043 秒，密度 0.226 秒 |
| 1 | $27\to26$ | $15\to15$ | 场 0.022 秒，密度 0.089 秒 |

其中第 14 段 field 的 $(N_t,m)=(30,30)$ 完整解析费约
$9.257663\cdot10^{-22}$，原目标的四分之一约为
$4.072584\cdot10^{-21}$。保留同一 $N=2048,K=1023$，不涉及角重采样。
密度的对照使用其原准确有限 $P$ 的实际外域；未来若先换了场布局，仍须
由新的有限 $P$ 重算密度外域后调用 helper，不能直接复制旧 $P$ 的模数。

重放报告为 `notes/2026-11-12-complete-budget-time-layout-comparison.json`；
入口 `scripts/fourfold_saved_time_layout_comparison.py` 读取报告内列明的
3 个已完成证书。没有为这些比较重采真实场。

## 2. 192 与 320 bit 的同对象试算

在 ordinary14，固定 primitive/root 节点数均为 1024、最终物理角网格
2048、$u=i$，分别 fresh 构造实际模型。两次精度计算的全部 2048 个节点
球相交，所有真实分母门通过。

| 精度 | 首次 sample CPU | 节点分量最大半径 |
|---|---:|---:|
| 320 bit | 0.456 秒 | $6.602378\cdot10^{-63}$ |
| 192 bit | 0.533 秒 | $2.520194\cdot10^{-50}$ |

另一次每精度连续 3 次同节点重采，192 bit 的中位数 CPU 为 320 bit 的
约 0.9104，后两次均值比约为 0.8445。所有运行的 CPU 时间在
0.456--0.784 秒之间变化，精度降低未表现出足够稳定的大收益。
192 bit 的点值精度远足够当前场目标，但这不是完整时间圆周噪声证书。

两个入口为 `fourfold_scalar_field_precision_benchmark.py` 与
`fourfold_scalar_field_precision_repeat.py`，对应
`2026-11-12-ordinary14-field-precision-benchmark.json` 和
`2026-11-12-ordinary14-field-precision-repeat.json`。

## 3. primitive640、root1024

同一 ordinary14、$u=i$、最终 2048 角点，在不修改任何冻结场源的情况下，
primitive 节点数 640、root 节点数 1024、320 bit 实际通过。
初始化 CPU 3.239 秒，sample CPU 0.496 秒；节点分量最大半径
$<3.853059\cdot10^{-37}$，包含真实无限 primitive 费用。

若仅作布局假设，假设所有时间点都有该同一最大节点费用，原完整矩形的
噪声项约为 $9.802746\cdot10^{-30}$，远低于实际 field target
$1.629034\cdot10^{-20}$。**该假设未被此单点试算证明**；每个真正叶仍须
执行全部节点费用门。实际输出保存在
`notes/2026-11-12-ordinary14-primitive640-benchmark.json`。

这次单点 CPU 在 1024 节点已有波动范围内，不能据此宣称 37.5% 或其它
固定 CPU 降幅。它给出的是可试用 640 的真实接口和精度证据，不是对全部
550 段的统一精度或速度承诺。
