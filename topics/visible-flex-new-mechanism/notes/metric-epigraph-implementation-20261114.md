# 固定度量最大误差求解器：实现与唯一实算配置

日期：2026-11-14。

状态：源码完成，等待公开 Actions 的针对性人工检查和一次实际调用。本说明不记任何尚未运行的检查为通过，不报告新的实际几何结果。

数学依据见 `notes/fixed-g-metric-minimax-epigraph-design-20261114.md`。本次新增 `scripts/frame_metric_epigraph.py` 与 `scripts/frame_metric_epigraph_audit.py`，不修改已发布的求解器、基场、完整度量、帽、共同高度原函数或参数基底。

## 1. 实际用途与起点

上一轮真实恢复求解的直接度量平方平均成本降低，但最大误差仍约为 $0.8882$，入口径向压缩与曲率峰没有随平均成本同步改善。本轮更换目标，直接最小化同一有限采样集上的最大度量算子误差。此前 quartic 和 L2 joint 求解的预算均不重复。

唯一实际起点是 `actions-43635770962-1-joint_resume/quartic-reused-joint-resume.json.gz` 已选出的完整 163 维状态：

- 物理状态 SHA256：`81a154d3464fd329bd384572fbf9f067c93a9e588f454c909f9e1ba239905433`。
- 完整固定度量 SHA256：`fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`。
- 原始 234 维 $c_0$ 只作为已有基场与不可变 $b_0$ 的来源；新的当前状态不会替换它。
- 不使用全局语义输运的新 $B=.37$ 失败状态，也不切换到局部新核心的另一度量。

该起点、度量和数值回放事实来自上述公开报告；本说明没有在本地重新评价它。

## 2. 正辅助变量与真实度量行

记 $U=X_s$、$T=X_\theta/a$。框架参数化保持 $|T|=1$ 与 $G=a^2$，因此

$$
e=|U|^2-1,\qquad f=U\cdot T,\qquad
\eta=\frac{|e|+\sqrt{e^2+4f^2}}2.
$$

新增一个所有采样点共用的辅助变量 $\delta\ge10^{-8}$，约束为

$$
c_-=\delta-e-\frac{f^2}{\delta}\ge0,\qquad
c_+=\delta+e-\frac{f^2}{\delta}\ge0.
$$

在 $\delta>0$ 下，这两式与 $\eta\le\delta$ 等价。实现保留除以 $\delta$ 的形式，拒绝 $\delta=0$，不把未除式在零处的退化当作可行性。

对任意物理参数 $p$，

$$
e_p=2U\cdot U_p,\qquad
f_p=T\cdot U_p+U\cdot T_p,
$$

$$
(c_\mp)_p=\mp e_p-\frac{2f}{\delta}f_p,
\qquad
(c_\mp)_\delta=1+\frac{f^2}{\delta^2}.
$$

目标严格为 $\min\delta$。旧的平均度量成本和 smooth-positive 球/条带成本仅保留在完整几何审计中，明确标为旧诊断量，不参与本次目标。

## 3. 不变物理条件与明确的新采样条件

原有物理参数盒逐位读取保留，包括已有 $u/v$、单个 $Q$ 和九个高度系数；没有 clip、refit 或增加新的物理系数。原公开帽高仿射行及其数值截距完整复用。共同高度仍由同一个查询无关原函数定义。

本次同时要求当前真实重构位置满足：

$$
\sigma X_z\ge\frac1{10000},\qquad
|X|\le\frac{101}{100},\qquad
|X_y|\le\frac{39}{100}.
$$

其中 $\sigma$ 是端口侧别。这些是本次求解的硬采样约束；旧条带目标为 $0.38$，这里明确改变为 $0.39$，不把旧约束冒称相同。球与条带条件若将来在完整曲面上连续成立，支持已有宏观幅度预算；有限节点通过不构成该连续结论。

球和两侧条带的参数导数分别为

$$
-\frac{2X\cdot X_p}{R_{\rm ball}^2},\qquad
-\frac{(X_y)_p}{p_y},\qquad
\frac{(X_y)_p}{p_y},
$$

其中 $R_{\rm ball}=101/100$、$p_y=39/100$。高度行导数是 $\sigma(X_z)_p$。当前 $u/v$ 变化会改变这些量，因此每一个试探点都重建；不复用固定 $T$ 高度多面体的旧位置行。

显式数值选择容差为：物理盒 $0$；帽高 $10^{-9}$；帽高仿射式与共同原函数一致性 $10^{-10}$；signed-z、归一化球/条带行、两条除式与独立最大 $\eta$ 各 $10^{-9}$。这是冻结的浮点评价规则，不是连续误差包围。

## 4. 一次几何缓存、辅助身份与选点

物理状态是原 163 维向量。求解器向量为它后接 $\delta$，共 164 维；`identity`、`state_record`、固定度量以及最终完整系数中都不加入 $\delta$。检查点另外保存 $\delta$ 的 binary64 有理身份。

每一个不同物理向量只调用一次当前 `geometry(..., jacobian=True)`，供目标、目标梯度、全部非线性行及其 Jacobian 共用。单独改变 $\delta$ 不增加物理几何计数。缓存保留：

- 普通位置完整二 jet、$T$ 及其角/径导数、共同高度与度量诊断；
- $e,f,\eta,e_p,f_p$；
- 位置 Jacobian $X_p$。

计算完 $e_p,f_p$ 后不长期保留额外的 $U_p,T_p$ 大块数组。合并约束 Jacobian 按需创建，不叠加存入缓存。真实 $100\times192$ 工作网格的 $6N\times164$ Jacobian 为 18,892,800 个 binary64，即 151,142,400 字节，约 144.14 MiB；它不包括 SciPy SLSQP 工作区和瞬时几何数组。报告实际缓存、单次 Jacobian 和进程峰值 RSS，不把这一静态数组量称为完整进程内存上界。

所有候选都通过独立选择器：原帽高、原盒、当前 signed-z、球、条带、正 $\delta$、两条除式和直接计算的 $\max\eta\le\delta+10^{-9}$ 必须同时通过。最后一项不能由“多项式余差很小”替代。

检查点分别记录：

1. 全部约束通过的最低辅助 $\delta$ 点；
2. 全部约束通过的最低真实 $\max\eta$ 点；
3. 最低 $\delta$ 试探点，允许它不可行，并明确标记。

最终采用第 2 类，真实最大误差相同时以较小 $\delta$ 决胜。`SLSQP.success` 不直接决定接受。预算耗尽、几何异常或求解器返回失败时仍保留已验证的最佳候选；如果起点本身没有通过新硬门，则保存完整诊断并不调用优化器。

## 5. 唯一预算与最终同态评价

工作节点沿用已发布 joint 的准确 100 层径向节点和 192 角点；输入回放须核对完整节点定义，不只是数量相同。仅一次 SLSQP：80 次迭代、120 个不同物理几何评价、300 秒。每 10 个物理评价或 60 秒保存一次原子检查点；退出时再保存。辅助变量的额外取值单独计数。

最终精确重放被选的全部系数，核对完整 $g$ 和 $b_0$ 不变，再在同一个物理状态上评价：

- 原工作网格；
- 121 个均匀径向基础节点加入完整结构与入口节点，实际 160 层，角数 384；
- 相同 160 层、角数 768。

保存完整位置端口二 jet、度量分布、曲率、signed-z、帽高、镜像点对、球与条带诊断，以及同系数 $\Pi$ 角加倍差。细网格可能出现 $\eta>\delta$；该失败如实保留，不抬高辅助变量、不换状态、不再次优化。曲率和非局部厚度没有包含在 epigraph 等价式中，最大度量误差下降不意味着曲率下降或 reach 已付。

## 6. 六输入来源与人工覆盖范围

实际 driver 严格消费六个已经发布的完整报告。前五个仍由已有恢复器验证，随后独立核第六个完成状态的全部来源、配置、163 个 binary64 有理系数、完整 canonical 状态、原帽高行、原盒、工作节点和固定度量。

| 输入 | 解码后 SHA256 |
| --- | --- |
| 原 independent-height selected | `c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46` |
| 原 enriched $c_0$ | `6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3` |
| short paired/bounded 审计 | `9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c` |
| accepted 九高度审计 | `f457282f0a21cd27802748066537caa4cf90c687c63c73d62b0391ce2435d1a3` |
| 已完成 quartic、未调用 joint 的报告 | `e344e6e0a62be10dfa8dad4f52e4b889191f462b97bb19dd4b1cc0283f6f33dc` |
| 完成的恢复 joint 报告 | `40deb9dffa6882b14dd445d981f2ed09b1f4d488dbaa83e952c768537f91375d` |

人工检查分两部分：明确不是曲面的三变量数组模型核除式/真实 $\eta$、全部新约束 Jacobian、四回调缓存、仅改 $\delta$ 的复用、异常保留可行初态及一次小型人工 SLSQP；小椭圆人工载体则走完整六输入 IO、全部调用签名、最终同态评价、错误第六 SHA/状态/帽高行拒绝及 summary 字节绑定，完整模型路径只评价，不运行旧优化器或新优化器。

每个输入失败、评价失败和检查点均保存小 summary。完整报告保留复现所需来源与状态；summary 删去巨大 canonical 和径向逐行数组，保留科学诊断和完整报告字节 SHA。人工 fixture 均明示其人为来源，不伪造真实 Actions 成功记录。

## 7. 公共 Actions 命令

仅公开仓库 `Rogerhu12/math-research-public` 的 Actions 可以运行实际分支；输入必须位于本课题 `notes` 下。人工检查命令为：

```sh
python topics/visible-flex-new-mechanism/scripts/frame_metric_epigraph_audit.py \
  --check-only \
  --out "$RUNNER_TEMP/metric-epigraph-development.json"
```

同一新源完成针对性人工检查后，唯一实际命令为：

```sh
python topics/visible-flex-new-mechanism/scripts/frame_metric_epigraph_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
  --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --short-audit topics/visible-flex-new-mechanism/notes/actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz \
  --height-audit topics/visible-flex-new-mechanism/notes/actions-43630874689-1-height_polytope_audit/height-polytope-bounded-audit.json.gz \
  --prior-joint-audit topics/visible-flex-new-mechanism/notes/actions-43634358250-1-quartic_joint_audit/quartic-joint-audit.json.gz \
  --resume-audit topics/visible-flex-new-mechanism/notes/actions-43635770962-1-joint_resume/quartic-reused-joint-resume.json.gz \
  --expected-input-sha256 c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 \
  --expected-anchor-sha256 6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3 \
  --expected-short-sha256 9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c \
  --expected-height-sha256 f457282f0a21cd27802748066537caa4cf90c687c63c73d62b0391ce2435d1a3 \
  --expected-prior-joint-sha256 e344e6e0a62be10dfa8dad4f52e4b889191f462b97bb19dd4b1cc0283f6f33dc \
  --expected-resume-sha256 40deb9dffa6882b14dd445d981f2ed09b1f4d488dbaa83e952c768537f91375d \
  --out "$RUNNER_TEMP/frame-metric-epigraph-audit.json"
```

这轮的结论只由实际回执决定。无论求解器的退出字样为何，完整嵌入、固定握持、连续同度量精化及全曲面 reach 都仍须分别支付。
