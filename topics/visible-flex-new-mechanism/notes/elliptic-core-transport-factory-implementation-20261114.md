# 新椭圆核心的严格系数输运工厂

日期：2026-11-14。状态：新增独立实现，尚待公开 Actions 的人工检查回执；未在本地导入或运行数值模块，未构造真实 $B=37/100$ 候选。没有改动任何旧源码、旧输入报告或旧物理身份。

实现：`scripts/frame_core_transport.py`。数学设计依据为[原输运稿](elliptic-core-design-coefficient-transport-20261114.md)。本版只接准确核心、原 enriched 列、natural 六帽基场和独立高度表示；没有同时加入入口修复或 single-Q 列。以后组合这些独立包装器必须另存完整模型身份。

## 1. 工厂接口和研究运行边界

主要接口为：

```python
problem, state, receipt = build_core_transport(
    anchor_bytes,
    target_minor='37/100',
    selected_report_bytes=None,
    height_free=9, metric_free=5,
    heat_order=32, height_angular_nodes=384,
    radial_nodes=61, angular_nodes=192, quadrature_order=4,
    support_width='1/10', plateau_fraction='1/3', tau0='1/128',
    expected_anchor_sha256=None, expected_selected_sha256=None,
    initializer_bounds=None,
)
```

真实调用在解析报告和构造核心之前检查 `GITHUB_ACTIONS=true` 及 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。工厂接收原始报告字节，保存字节 SHA；若调用方提供预期 SHA，则必须先相等。后续真实 driver 还应把输入限制在本题公开 notes，并在 workflow 固定所选输入 SHA。

本文件没有真实候选 CLI，只有：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_core_transport.py \
  --check-only --out "$RUNNER_TEMP/core-transport-development.json"
```

人工分支只能接受准确核心 $A=9/10,B=18/25,w=1/50$ 和目标 $B=2/3$；不能借 `artificial=True` 构造本题 $B=37/100$。人工检查保留真实的 $9\times(9+8+9)=234$ 列布局，并检查正、负两个端口。检查失败也写出包含异常类型、traceback 和源码 SHA 的小 JSON。

工厂本身不调用 `geometry`、目标函数、优化器或步长应用；构造器会按指定评价规则预先计算标量基场表。这些计算也属于真实调用的一部分，因此真实工厂并不是可在本地提前运行的“仅元数据”接口。

## 2. 先重放旧模型，再建立新对象

工厂首先原样调用已冻结的 `load_enriched_report`。旧报告的原源码 SHA、基线报告、core/port、space、metric、234 个准确 binary64 有理系数和完整数学状态哈希均按旧 loader 的规则重放。不会改 JSON 的 minor 或将新 $a_0$ 塞进旧模型。

随后新建：

1. `EllipticCylinderPort`，保持旧 $A,w,\sigma$，只选择新的准确 $B$。
2. `NegativeKRadialSeed.from_core`，保持旧准确 $L,r_c$、buffer、三个分段比例、gap 及 S5/S5/S11 类型。$a_0$ 的身份仍为新准确核心周长除 $2\pi$，数值周长不是新的冻结常数。
3. `EnrichedProblem`，保持旧径向和角向标签，重新计算目标核心的材料弧长逆、$u_{\rm core}$、入口 Cauchy 基场和角导数。
4. `TransportedNaturalBodyProblem`，使用新的 seed 和 transported c0 建立 natural 六帽场及全平 Gaussian 定义。
5. `TransportedIndependentHeightProblem`，重新定义不可变 $b_0$，建立独立高度与 body 控制。

改变 $B$ 会改变 $a_0,\mu,\nu$ 和完整 $a(t)$。因此零 body 状态也属于新度量设计；不能称为旧固定 $g$ 的精化。工厂明确要求目标核心身份与旧核心不同，并保存两个准确 seed 定义。

由于 $L,r_c,c_{\rm flat}$ 保持，尾帽外半径 $R=r_c+Lc_{\rm flat}$ 保持，六个幅度和方向也保持；帽自身仍是 [R44](../results/R44-S9-six-cap-exact-embedding-and-normal-chord.md) 的准确对象。它最终放置的共同高度、全连接面包络、非局部距离和 reach 均不继承旧回执。

## 3. 逐标签复制 234 个系数

每列使用四元标签

$$
(\text{field},\ \text{radial index},\ \text{angular kind},\ \text{harmonic index}).
$$

其中角类分为 material-sin/cos、ellipse-phase-sin/cos 和 exact-u-core。先检查源、目标标签集合完全相同，再按显式置换复制。完整有理 clamped knots、degree、保留列和零延拓定义也必须相同。没有插零、拟合、正交化或裁剪。

回执同时保存源、目标的 `Fraction.from_float` 值及 `float.hex()` 字符串；后一项还能区分有理数表示不能区分的正负零。实现用 `uint64` 视图逐位检查复制结果，而不是只用浮点近似相等。

材料 $\theta$ 模的抽象函数保持，物理材料点已经变更；$\varphi_B(\theta)$ 模和 $u_{{\rm core},B}$ 列的函数一般改变。故“数值逐位相等”只证明系数复制准确，不证明旧、新曲面相同。

## 4. 新 anchor 和高度基保持独立身份

`TransportedNaturalBodyProblem` 的 anchor schema 为 `target-core-transported-enriched-c0`。其中同时记录真实旧 source receipt、新 core/port、完整新 seed、新 enriched 空间以及逐列复制回执。父构造器完成后更新 anchor，并清空、重建所有 grid/cache，避免旧 schema 混入缓存元数据。

不可变高度基准确定义为

$$
b_{0,B}(t)=\frac1{2\pi}\int_0^{2\pi}
\frac{-\sin\beta_{0,B}(t,\theta)}{\sqrt{1+v_{0,B}(t,\theta)^2}}\,d\theta,
$$

其中标量场总是目标核心的 transported **原 c0**，且参考 body 控制为零。当前 $u,v$、高度参数、body 参数和后续 initializer 都不替换该参考。

子类将高度 schema 改为 `target-core-transported-c0-angular-mean-height-v1`，并覆盖 `evaluation_variant`。否则父方法会重新构造原始 `IndependentHeightProblem`，丢失新 schema。GH 与 Nb 变体仍使用同一无限 Gaussian、同一准确角平均、同一物理参数；阶数只写入评价定义。`frozen_metric_copy` 保留子类，完整准确 $g$ 冻结前后状态身份必须相同。

本版沿用独立高度表示的数学共同原函数，没有引入逐截面的高度平移。其原始 `geometry` 数值评价仍按查询节点划分径向 Gauss 区间；已知稀疏查询可能评价不准，不能把它当查询无关的连续证书。真实几何 driver 应继续组合现有 `FixedPrimitiveProblem` 的固定结构分区评价，或显式保存同等的固定原函数规则。这个评价包装不改变本工厂的物理身份。

## 5. 可选 selected initializer 的严格范围

默认初态为 transported 的 153 个 $u/v$ 系数，9 个零高度系数和5个零 body 系数。

若提供旧 selected 报告，则先调用未改动的 `load_selected_report`，包括原 anchor 字节绑定、原初态与 selected 全 canonical 状态、逐块准确系数和完整冻结 $g$。只有通过原模型重放后，才输运初值：

- $u/v$ 按同样的语义标签复制；
- 高度基的完整准确 `identity` 必须相等，才复制9个数；
- body family 仅排除有意替换的 `seed_definition`，其余 **全部** family 字段必须相等，包括 support、完整有理 knots、degree、保留列、endpoint weight、零延拓和正半径公式，才复制5个数；两个含各自 seed 的完整 family 哈希另行保存。

复制 body 数只保持同一 log 扰动的系数，目标是新 seed 乘该扰动，所以仍是新 $g$。复制高度数只保持新增速度函数，新的 $b_0$ 和总 $z$ 已改变。

selected 来源回执只进入 initializer receipt，不进入不可变 anchor。人工检查会验证默认零初态与 selected 初值的 $b_0$ 定义完全相同，并在相同评价节点上逐位相同。

工厂不暗中选择求解器 bounds。调用方若传 `initializer_bounds`，必须明确覆盖 $u,v,\mathrm{height},\mathrm{metric}$ 四块；超界直接拒绝，不做 clip。未传时回执明确“没有声明新的 optimizer bounds”，不得据此宣称初值满足未来某个盒。

## 6. 人工检查内容及尚未完成的工作

公开 `--check-only` 准备检查：

| 检查 | 用途 |
|---|---|
| 正、负侧234列逐标签与逐位复制 | 排除布局或系数重解释 |
| 新 core/seed/完整 $g$/heat 身份确实改变 | 排除伪装旧模型回放 |
| 帽物理身份保持 | 区分帽形和整体帽高 |
| selected 的 uv/height/body 准确复制且 anchor 不替换 | 覆盖可选初值分支 |
| core 和开放尾的完整标量二jet、对应径向度量二jet | 排除输运破坏端口 |
| 新准确核心位置二jet与数值重构比较 | 人工数值接口检查，非连续误差证书 |
| 同目标状态冻结 $g$ 后六个位置jet逐值一致 | 防止冻结时偷换场 |
| GH、Nb、冻结变体保新子类与同物理身份 | 防止评价参数混入模型 |
| 错 SHA、坏有理系数、不匹配基、超界、非公开环境 | 覆盖明确拒绝路径 |

检查只用已声明的人工温和椭圆，不评价真实 $B=37/100$，不进行优化。没有提供新核心实际成本、等距误差、曲率、球/条带、帽高或 reach 结论。

下一真实 driver 可把此新核心工厂与已独立发表的入口修复、bounded height、single-Q 逐项组合；每项组合都必须写入完整 model/space 身份，并重新选择符合新核心的 [R66](../results/R66-core-flat-cap-two-normal-reach-height-gate.md) 分支。不能把旧 $B=7/25$ 的帽高阈值直接套给新 $B$，也不能同时更换核心、入口和优化目标后把效果只归因于核心。

## 7. 公开人工检查已通过

2026-11-14 19:39:40 UTC：公开 [run43633105146](https://github.com/Rogerhu12/math-research-public/actions/runs/43633105146)，source `109cdd7f25927645ea6d33045c037cc920a8bc5f`，lane `core_transport_development` 全部通过。脚本仍为 `ea7990328c979f02be7b83db307f5d1b94e69d0ede3e1cc34d9b37a1f357f21d`。

两侧234列逐位、selected三块复制、独立新core/seed/g/heat与不变帽身份、原c0高度anchor、GH/Nb/冻结子类身份全部通过。core/尾标量和metric二jet误差为0，冻结前后六位置jet差为0，人工准确核心位置误差最大1.136e−14。八个错误输入/环境路径全部被拒绝。原始[完整回执](actions-43633105146-1-core_transport_development/core-transport-development.json)保留各侧身份与全部数值。

这只验证人工新旧核心接口，未构造真实B=.37。下一是一个独立的单初态公开审计：严格输运原167 selected，原234保持新anchor，用固定分区原函数评价新物理场和同态加密，不同时优化或加入入口/Q列；真实新g、b0和R66高度分支都另记。
