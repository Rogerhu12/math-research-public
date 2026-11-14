# 更温和椭圆核心：旧系数输运与新模型身份

日期：2026-11-14。状态：纸面设计和接口约定；没有实现、没有评价任何新核心。首轮 167 维结果与固定高度原函数审计已公开；本稿仍是独立的新设计准备。

本稿回答如何把原公开 c0 用作 $B=9/25$ 或 $37/100$ 椭圆核心的初值。**可以输运系数，不能声称输运后仍是旧曲面、旧度量或旧 anchor 的准确重放。** 当前没有选择这两个值之一；它们是已明确授权的独立设计候选。

## 1. 共同的条件预算与发生改变的对象

保持主半轴 $A=1$、核心半宽 $w=1/50$、帽内握持半径 $r_c=11/50$。若完整曲面仍满足已采用的球/条带条件

$$
|X|\le101/100,\qquad |X_y|\le19/50,
$$

则核心长轴端点在转过 $\pi/2$ 后仍给像集距离见证 $1-19/50=31/50$。因此 [R40](../results/R40-bent-flat-tail-normal-chord-and-ball-budget.md) 的 $D\le101/50$、$\delta_{\rm hold}/D\ge31/101$ 和握持比例不因 $B\le19/50$ 而变。这里的“若完整曲面满足”仍是必须重新验证的全局前提。

新核心准确为

$$
\Gamma_B(\varphi)=(\cos\varphi,B\sin\varphi,0),\qquad
a_{0,B}=\frac1{2\pi}\int_0^{2\pi}
\sqrt{\sin^2\varphi+B^2\cos^2\varphi}\,d\varphi.
$$

其材料角重新按 $\ell_B(\varphi)=a_{0,B}\theta$ 定义。两次设计的抽象角坐标都记作 $\theta$，不表示同一物理点；准确弧长逆映射 $\varphi_B(\theta)$ 已经改变。

新核心的最小平面曲率半径是 $B^2$；角转速的最大/最小比为 $B^{-3}$。这是纸面比较，不是完整连接面的曲率或 reach 证明。$B=.36/.37$ 在条带边界内尚有余量，但这个余量不能保证活动片仍留在条带中。

本方案暂保 $L=9/10$、core/flat buffer 比例、三段径向比例和 gap、S5/S5/S11 类型不变。新的 $a_{0,B}$ 改变径向 seed 中为支付总半径下降而求出的 $\mu,\nu$，因此完整函数 $a_B(t)$ 和目标度量都改变。即使五个 body 系数仍为零，也**不是**旧 $g$ 的精化。

## 2. 第一步必须是真实读取旧报告

输入仍为原公开 enriched c0 报告。首先必须完整调用现有未改动的 `load_enriched_report`，核它原来要求的源码 SHA、core/port、空间、metric、准确 binary64 有理系数、旧报告 canonical hashes。返回的对象记作 `source_old`，系数记作 $c_0^{\rm old}$，来源回执独立保留。

这个阶段只核旧模型。不得先将 JSON 的 minor 改成新 B，再让旧 loader 对它“通过”；也不得为了重用旧 metric hash 而把新 a0 写进旧 seed 的数值字段。原输入文件与全部旧身份保持原样。

应明确保存两层不同的信息：

| 对象 | 身份含义 |
|---|---|
| 旧 source receipt | 真实公开 c0 的来源、源码和原准确模型 |
| 新 target design | 新核心、重新构造的 metric、角基、固定场和高度基 |
| coefficient transport receipt | 旧系数通过哪一个确定性语义映射进入新设计 |

同一向量的 binary64 数值逐位相同，只能证明这次系数复制没有重拟合，不能证明两个场相同。

## 3. 新对象从构造器重新建立

最小安全工厂应重新构造下列对象，禁止只对旧对象 `copy.copy` 后改 `.port` 或 `.a0`：

1. 新 `EllipticCylinderPort`：$A=1$、精确有理 $B$、$w=1/50$、原 side、fold=2；生成新的 core/port 身份。
2. 新 `NegativeKRadialSeed.from_core`：新 a0 的**准确核心周长来源**，以及原有准确 $L,r_c$、分段和 gap 配置；重新得到全部径向 jet、$\mu,\nu$ 和准确 seed 定义。
3. 新 enriched 场提供器：原 $J=9$、材料模 5、椭圆模 3、u-core 方向、参数布局均可保留，但固定端口、入口 Cauchy 首项及全部 angular tables 必须使用新核心。
4. 新 natural-cap 场提供器：六帽物理定义、$h=1/10$、全平 Gaussian、plateau 参数保留；patch 的源半径用新 seed 的 $a_B(t)$，不沿用旧 heat cache 或旧物理 heat 身份。
5. 新 `IndependentHeightProblem`：其不可变高度基从下节的新 transported anchor 完整角平均重新定义；新 height/boundary/body basis 及全部缓存重新建立。

原径向节点、B 样条 knots 和支持端点只依赖固定的 $L$ 与比例，故这一选择下它们可准确相同。不过仍应比较其完整有理定义，不依据“维度还是 9”自动认定相同。

尾帽的外半径

$$
R=r_c+L\,c_{\rm flat}=137/500
$$

未改变，六个方向与幅值也未变。因此帽自身的准确形状定义和已有 [R44](../results/R44-S9-six-cap-exact-embedding-and-normal-chord.md) 证明仍适用。帽的最终高度依然是共同 $z(L)$；完整连接的高度、包络、跨片距离和 reach 都不能继承。

## 4. 234 个旧 c0 系数的语义输运

旧空间的每列应使用 `(field, radial_index, angular_kind, harmonic_index)` 标签，而不只依赖扁平位置：

- u：5 个 $\sin(2j\theta)$、3 个 $\sin(2j\varphi(\theta))$，以及一个准确 $u_{\rm core}(\theta)$；共 $9\times9=81$。
- v：相同的前 8 个奇角函数；共 $9\times8=72$。
- 固定参考 beta：$j=0,\ldots,5$ 的 $\cos(2j\theta)$ 和 3 个 $\cos(2j\varphi(\theta))$；共 $9\times9=81$。

复制同一标签的系数得到 $c_0^{\rm tr}$。每个值都保留原 $\mathbb Q.\mathrm{from\_float}$ 身份；不做 least-squares 重拟合、不加新模、不在输运时裁剪到 bounds。

这些列在新模型的意义如下：

| 角列 | 输运后函数 |
|---|---|
| 材料 $\theta$ 模 | 同一抽象角函数；其对应物理点已随核心变更 |
| 椭圆 $\varphi$ 模 | 重新使用 $\varphi_B(\theta)$，通常与旧函数不同 |
| u-core 方向 | 新准确端口的 $u_{{\rm core},B}$，通常与旧函数不同 |
| 径向列 | 若全部准确 knots/support 配置相同，则为同一径向函数 |

其中 beta 的 81 个数只定义固定参考高度基，不重新进入 167 维优化变量。

新 anchor 定义应明确命名为 `target-core-transported-enriched-c0`，并同时包含旧 source receipt 和新空间/端口/seed 定义。旧源码中某些 metadata 使用“original enriched anchor”措辞；新独立 wrapper 必须用新 schema 和明确文本覆盖这种可能混淆的标签，不能把目标模型冒充为原报告的原物理 anchor。

## 5. 高度基也重新定义，不能复用旧 mean 缓存

推荐的整套输运选择是：从新 natural 场在固定 $c_0^{\rm tr}$、零 body 控制处计算其准确数学函数

$$
b_{0,B}(t)=\frac1{2\pi}\int_0^{2\pi}
\frac{-\sin\beta_{0,B}(t,\theta)}
{\sqrt{1+v_{0,B}(t,\theta)^2}}\,d\theta.
$$

再令

$$
b_B=b_{0,B}+\sum_{j=1}^{9}g_jC_j,\qquad
z_B(t)=\sigma w+\int_0^t b_{0,B}(r)\,dr+
\sum_{j=1}^{9}g_j\int_0^t C_j(r)\,dr.
$$

这个 b0 始终绑定固定的新 transported anchor；以后当前 u/v/body 改变时它不跟着变化。新初态为输运后的 153 个 u/v 系数、9 个零高度系数和5个零 body 系数。

另一种数学上可定义的设计是刻意继续使用旧 $b_{0,\rm old}$，同时换核心和 T 基场；但它属于不同的混合模型，需要第二个明确高度来源身份。本稿不选择这个混合方式，不让旧缓存偶然造成这种选择。

GH、完整高度均值的 Nb、Pi 查询角数和径向求积仍只是新模型的评价设置。同一新物理身份下分别加密；旧 B=.28 的评价差不能拿来为新 B 的门背书。

## 6. 若以后用首轮 167 维结果作数值初值

原 c0 的 234 个数仍永久定义新 target anchor，不被一次优化结果替换。可另把首轮返回的 u/v、height、body 状态作为 `initializer_state`：

- u/v 按同一列标签复制；
- 只有确认高度基完整准确定义相同，才能将 9 个高度系数直接复制；这只保新增的一维速度函数，不保改变后的 $b_0$ 或总 z；
- body 系数只有在完整 support/weighted-basis 定义相同的情况下才可复制；目标仍是新 seed 乘同一 log 扰动，故得到的是新度量；
- 若任何标签或基定义不同，拒绝直接复制，另行制定公开的转换，不以插零或隐含拟合替代。

初始化系数超出目标 bounds 时，应保存超界诊断并停止该初始化分支，或另行记录有明确授权的新 bounds；不得静默 clip 后仍称原状态输运。零 body 或复制旧 body 是两个不同的设计选择，报告必须写出本次采用哪一个。

## 7. 必须保存的 canonical 身份

建议独立 transport receipt 至少包含：

```text
schema: elliptic-core-coefficient-transport-v1
source_report_bytes_sha256
source_canonical_model_and_space
source_core_port_and_metric_definition
source_c0_exact_rationals
target_core_identity
target_port_identity
target_seed_exact_definition
target_space_definition
semantic_column_map
transported_c0_exact_rationals
coefficient_copy_is_bitwise_equal
physical_field_equality_is_not_claimed
old_metric_refinement_is_not_claimed
target_height_base_definition
tail_physical_identity
entry_repair_definition: null or its complete new identity
```

core、port、完整 seed、natural heat 身份、anchor、height base、模型、空间与状态哈希均重新生成。旧 source 哈希只作为祖先来源保留。不能为了使旧 assertion 通过而替换旧 input 的 source hashes，也不能把新 minor 混入一个仍声称旧 B 的 report。

为了保持已冻结模块不变，可新增工厂及少量 schema wrapper：先真实加载旧 enriched 报告，再从公开构造器重新建立目标对象。数学场及 Jacobian 可复用现有实现，但新 wrapper/source SHA 必须进入输出，且完整 target 身份应经 GH/Nb/冻结 g 的回放测试。

## 8. 人工检查与实际选择的分界

开发检查只用人工温和椭圆：核旧 loader 仍严格读旧身份；目标 B 与 core/port/seed 确实变化；同标签复制有理系数逐位相同；新物理 hash 与旧不同；新端口位置二jet和两端标量一致；GH/Nb 改变不改新模型身份；同一目标 g 冻结后全部位置二jet回放。

公开 Actions 的第一次真实调用应先输出旧源重放、新 core 输运初态及它们的区别，再做新初态评价门。最少保存新的直接 E/F、入口/主体/patch 分布、面积、实际曲率、全坐标范围、球/条带、共同帽高，以及 GH、Nb、Pi、径向求积的分别精化。

仅改变 B 不会消除 [R64](../results/R64-convex-core-entry-seventh-tangent-and-sixth-center-jets.md) 的非圆入口首片五次 v 准确零限制。若同时选择成套入口修复，要把两项变化都写入 identity，不能把新效果单独归因于某一项。已有 167 维真实回执显示入口度量、曲率和高度均未通过；当前先在旧核心、已选固定度量上执行成套入口零步审计，再依据实际输出决定是否另开核心输运设计，或在清楚记录后组合。

本稿没有给新初态成本、误差或可行性预言，没有申请重复旧 250 次求解，也没有改变任何已冻结输出或当前入口审计的输入。
