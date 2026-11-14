# 同一普通段的独立扩域模型与完整有限复合成本

2026-11-12。以下均为已实际运行的有限或有向计算；不外推为完整
550 段的时间或误差结论。原失败报告和所有已冻结源保持原字节。

## 1. 第 18 段：Q640 扩域失败，独立 Q1024 扩域通过

输入是 `step5_sharp_time_domain_full/forward_0018_r.json.gz`，SHA256
`e63bbecf45c2b607836f66c12e30b1fc32e71f7d03a898ccdbc6fc0530c673d7`。
真实对象、时间端点、唯一共同样条 germ 均不改变。实际场采样的
primitive Q640 已通过原域费用，但 Q640 的更大域构造在除法处拒绝：
`leading term in denominator is not nonzero`。原失败保存在
`step5_expanded_time_domain_full/forward_0018_e63bbecf45c2_main0_optimal_R6_S12.json.gz`。

用同一冻结扩域源、独立 Q1024 模型重新支付所有无限原函数、
曲率与时间余项后，真实 `|u|≤6`、物理角带 `|Im θ|≤1/64` 的门通过：

- `D_lower > 0.10823482781546531531`；
- 完整真实 `|f| < 4.281891765258545505`；
- 全部实际共同 germ 覆盖完成（本段只有一个）；
- 新模型、根精化及扩域合计 CPU 6.475601329 秒，wall 37.8044 秒。

重放命令（课题根目录）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_expand_optimal_time_domain.py \
  --domain data/phase_ring_continuation/step5_sharp_time_domain_full/forward_0018_r.json.gz \
  --out data/phase_ring_continuation/step5_expanded_time_domain_full/forward_0018_main0_optimal_R6_S12_Q1024.json.gz \
  --R 6 --S 12 --nodes 1024 --bits 320 --radial-degree 96 \
  --germs 0 --curvature-outer 8
```

扩域源 SHA256 为
`f79ec42d43185a272dab5e23d5c752f10fca10e31a20f0aa52f78ace5681e25b`。
此入口在未传 `models` 时以 `root_nodes=nodes=1024` 构造新模型。
报告保留的 `independent_root_nodes=512` 是旧 retained-coefficient
输入的来源字段，不是这次新模型的配置。新费用、来源和其数学
适用范围均在新报告内独立记录。

独立模型只支付扩域；后续 Q640 节点采样仍按自身原域 primitive
误差合同检查，不从 Q1024 报告免费取得节点精度。旧 Q640 拒绝
不证明真实几何在该域有零点。

## 2. 第 419 段：保留全部有限模式的复合

实际输入来自永久 419 小包和已保存的 Q1024 场矩形，真实对象
身份逐项核对。有限场含全部 `|k|≤518` 模式和 12 个时间系数；
物理角频率是 `4k`。在准确 `u=5i/4`、4096 个实初始标签上计算
同一个完整有限 `P(u,Y(u,x))`，没有截去任何有限模式。
实际物理角像的最大虚部约为 `0.001922337185986038`。

| 实角锚点 | 有限 Taylor 半径 | 阶数 | CPU 秒 | 完整有限评价误差上界（约） |
|---:|---:|---:|---:|---:|
| 512 | 1/64 | 52 | 0.3083184 | 8.433e−43 |
| 512 | 1/32 | 44 | 0.2014954 | 1.086e−43 |
| 512 | 1/16 | 54 | 0.2748133 | 1.017e−43 |
| 256 | 1/32 | 52 | 0.1722231 | 2.085e−43 |
| 1024 | 1/32 | 41 | 0.3148757 | 3.367e−43 |
| 512 | 3/64 | 48 | 0.2221846 | 4.588e−43 |

全部六个配置的 4096 个有向值逐点相交；最快配置的四个不等距
节点另与直接完整 Laurent 求和相交。完整有限误差包括所有
有限模式的 Taylor 余项、系数和角输入误差、算术半径。较大的
Taylor 半径只用于有限 Laurent 多项式的全模数，不拓宽真实
无限场的解析域。真实 `f−P` 与连续标签重构费用仍须另付。

重放（输出同名报告，故需要保留旧报告时请先另存）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_actual_finite_composition_cost.py
```

结果源和所有输入 SHA、逐配置完整有向费用、四个直接核查记录
保存在 `2026-11-12-actual419-finite-composition-cost.json`。运行脚本
仅消费已保存的数学输入，不再采样真实几何。

## 3. 后续使用范围

主代理已决定在下一控制器版本试用有限半径 `1/32`、256 锚点，
并在低 Q 扩域拒绝时单独建立 Q1024 域模型。每个实际调用仍须
通过完整费用门；本记录不宣称其他段自动通过。后续研究转向
实际双通道、含均值的有限低块，不继续为几个百分点重复布局。
