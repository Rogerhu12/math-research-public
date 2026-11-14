# B=37/100 的单一输运初态审计入口

日期：2026-11-14。状态：独立 driver 已实现，尚待其公开人工完整 IO 检查；没有评价真实新核心。工厂的双侧人工检查已由公开 run `43633105146` 通过，本 driver 不重复该工厂的数学或参数 Jacobian 测试。

文件：`scripts/frame_core_transport_audit.py`。依据[系数输运设计](elliptic-core-design-coefficient-transport-20261114.md)和[工厂实现](elliptic-core-transport-factory-implementation-20261114.md)。本次研究调用只允许新 $B=37/100$，只使用一个原 selected 系数输运初态，不比较多个新核心或新度量，不调用优化器，不加入入口修复或 single-Q。

## 1. 唯一输入与模型路径

真实输入为两份公开原字节报告：

| 输入 | 原始 SHA-256 |
|---|---|
| `notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json` | `6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3` |
| `notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json` | `c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46` |

先由工厂的严格旧 loader 原样核两份输入，再建立新核心和新 seed。新不可变 anchor 仍来自原 enriched 的234个数；原 selected 的153个 $u/v$ 数、9个 height 数、5个 body 数只作为目标初态，在语义列和完整准确基定义匹配后复制。

立即冻结这个目标状态的完整新 $g$，将167维设计态变为162维冻结度量态，并核完整 canonical 物理身份完全相同。原 selected 的冻结 $g$ 仅作来源，不能用于目标对象。

报告保存旧、新 core、旧 selected 物理状态哈希、旧、新完整 metric 哈希、新 $b_0$ 哈希、完整输运回执与新准确系数。若新核心竟保留旧完整 metric 哈希，则拒绝。旧、新 cost 没有混合成一次“下降”记录。

## 2. 查询无关的共同高度和完整查询节点

在新冻结对象外包 `FixedPrimitiveProblem`，默认采用固定120个均匀分区，并加入其准确结构分区，每段 GL8。高度为同一数学函数

$$
z(t)=\sigma w+\int_0^t b_{0,B}(r)\,dr+\sum_j c_j I_j(t).
$$

查询集合不会改变前缀积分，不能为 core、活动片或尾帽分别重设高度。包装前后 canonical 物理身份相同，数值评价定义另行记录。依旧没有连续求积误差界。

几何查询默认121个均匀径向点，另合并以下准确有理节点：

- seed 的 core/三个活动片/尾端分界；
- 不可变 anchor 的全部径向 B 样条 knots；
- 原入口基场 cutoff；
- natural patch 起点、plateau 分界和准确尾端；
- 独立 height 与 body metric 的全部 knots。

这些点形成一个从 $0$ 到 $L$ 的统一 chart。报告保存每类节点来源和完整有理节点列表；评价密度不是物理定义的一部分。完整 chart 与四个稀疏节点 $0,t_c,t_f,L$ 另做同一固定原函数下的六 jet/中心高度比较，直接覆盖先前出现的稀疏查询高度问题。

## 3. 本次输出的几何诊断

首先在完整径向 chart 与384角点评价，保存：

1. 真实 $E-1,F/a$、相对 operator 误差、direct metric 与原 ball/strip 平滑目标的诊断 cost。
2. 实际面积、主曲率样本、坐标 min/max、共同 $b,b_s$、帽高、目标 $K$ 和半径范围。
3. 整个开放 core prefix 的位置六 jet 对照，以及整个开放尾与同一高度 $h=\sigma z(L)$ 的准确六帽位置六 jet 对照。帽高不逐行重拟合。
4. 每径向行的 metric/曲率/面积峰值位置，便于区分入口、主体和 patch 的缺口。
5. 全球、条带、signed height 和下面的镜像、R66 高度必要诊断。

全部曲率、极值和对照都是有限评价；“运行完成”不代表浸入、嵌入、等距、reach 或全包络通过。

## 4. 新核心的 R66 分支

本次标准参数为

$$
B=\frac{37}{100},\quad R=\frac{137}{500},\quad
d=B-R=\frac{12}{125},\quad \tau=\frac{61}{1000},\quad w=\frac1{50}.
$$

这里 $\tau<d<2\tau$。[R66](../results/R66-core-flat-cap-two-normal-reach-height-gate.md) 给完整镜合面 reach 至少为已选目标 $\tau$ 时的必要条件

$$
|h-w|\ge\sqrt{d(2\tau-d)}
=\frac{\sqrt{39}}{125}.
$$

根号下界大于 $w$，因此在标准正帽高分支 $h>0$ 中，必须

$$
h\ge\frac1{50}+\frac{\sqrt{39}}{125}.
$$

这与旧 $B=7/25$ 的门不同。实现不是硬写某个浮点阈值，而是按准确 $d,\tau,w$ 的三段公式记录常数项、根号有理数和分支；人工核心则自动落入自己的分支。

该条件依赖“完整面 reach 至少为本次选定 $\tau$”的假设，不能只凭题目比例而无直径信息推出这个绝对数。实际 $h$ 和根号目前仅浮点评价，因此输出 margin 不是严格区间认证。

## 5. 镜像对诊断

令实际 $U=X_t$、$T=X_\theta/a$、$W=U\times T$。对假设镜合中的两个相反点，法弦半径为

$$
\frac{|X_z|\,|W|}{|W_z|}
$$

（$W_z=0$ 时不提供这个有限上界）。报告最小有限样本和低于 $\tau$ 的样本数，同时报告非正则样本、浮点恰零高度和最小 signed height。

这些点对若未通过，说明所审镜合结构存在具体数值风险；有限点对全部通过仍不能保证其他点对或全曲面 reach。signed 正号是本次 upper 分支的屏障，不能概括为所有单侧嵌入的普遍条件。

## 6. 唯一末次角精化与来源账

末次用相同完整径向 chart、相同162个准确数、相同冻结 $g$、相同新 $b_0$ 和固定原函数规则，将几何查询角点384加倍到768。要求粗角点逐位包含在细角点中，再比较六 jet、$E-1,F/a$、operator 误差和共同中心。

GH、Nb 和固定前缀 GL 在这一次比较中保持不变。因此它隔离的是几何角查询/Pi 评价的变化，不把所有误差揉在一起；本次没有额外 GH/Nb 选档，没有重新优化，也没有借加密修改系数。若这份初态回执显示需要进一步评价精化，应针对实际证据另设单因素审计。

每个 checkpoint 同时写完整 JSON 与紧凑 `-summary.json`。summary 绑定当时完整报告的原字节 SHA，保留输入和源码 SHA、物理/metric 身份、全部全域诊断、core/尾六 jet、镜像、R66、同态精化，省去大 canonical 对象和径向行表。输入 loader 或后续评价异常也保存失败 JSON、summary 和已经完成的诊断，不会只留下空 artifact。

## 7. 公共人工与真实命令

人工检查调用真实 `run_from_files` 全路径，用工厂已经允许的 $A=.9,B=.72\to2/3$ 合成报告，测试成功 IO、完整诊断、同态角精化、四点/完整 chart 的共同高度、拒绝错 SHA 后的失败 summary、输入原字节不变。不再次测试工厂已通过的全部参数 Jacobian。

```bash
python topics/visible-flex-new-mechanism/scripts/frame_core_transport_audit.py \
  --check-only --out "$RUNNER_TEMP/core-transport-audit-development.json"
```

真实单次命令在本公开仓库 Actions 中为：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_core_transport_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
  --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --expected-input-sha256 c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 \
  --expected-anchor-sha256 6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3 \
  --out "$RUNNER_TEMP/core-B037-transported-selected-initial.json"
```

真实路径还必须位于本题公开 notes。当前没有运行以上真实命令，没有新核心实际 cost 或可行性数据。本次结果只能归因于明确记录的“新核心及其派生基场/度量/高度参考”的联合输运设计，不能声称保留旧物理场，也不能把尚未加入的入口修复当成已完成。
