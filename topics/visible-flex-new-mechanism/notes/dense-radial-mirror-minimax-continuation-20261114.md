# 细径向并集上的 minimax 续求：镜像门与两类最优点

日期：2026-11-14。作者：`/root/mechanism`。

**状态：明确的新数值求解配置；尚无本轮实际求解结果。** 这次改变由 [保存 trial 的细网格实际结果](metric-epigraph-saved-trial-first-fine-result-20261114.md) 直接支持：旧工作层漏掉 $s=.7875$ 的帽补丁峰，且旧选择策略会丢掉物理门通过、但辅助 $\delta$ 略低估的好物理场。下面两个新源码不修改已经发布的旧 solver、原 run 或其输出。

## 1. 唯一初态与保持的量

唯一初态为已经完整八输入绑定的物理场

`5d383918734118c105af3cfc2571731cdbefc2ad23939a4eb43a973e50b472ea`。

保持全部 $163$ 维物理系数、永久原 `c0`、固定 `b0`、核心／帽、原系数盒及完整目标度量

`fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`。

帽高仍使用原准确物理定义和该次已冻结的数值仿射行；不把旧 B 的帽高规则换成新 B。物理硬门仍为上半 $z\ge1/10000$、球半径 $101/100$、条带半宽 $39/100$。全部是有限采样求解条件，不是已认证的全域几何结论。

第八输入是只读审计 43639240317 的完整报告。源码重放前七输入的全部物理状态，并核第八份的来源字节、完整 state、零优化／零旧 $\delta$ 修改、准确工作／细网格及物理门记录。错误来源、状态或节点保存小失败 JSON，不进入新几何。

## 2. 工作节点与辅助量明确改变

新径向层是原报告的两个准确有理节点集的排序并集。当前原 $100$ 层是细 $160$ 层的子集，故实际并集为 $160$ 层，保留全部旧结构层并加入漏掉的 $.7875$。角数仍为 $192$，避免同时改变多个昂贵评价因素。节点来源及全部准确有理数进入本轮 objective evaluation identity。

旧 $\delta=.2651667068964935$ 仍保留在 provenance；不会改写它在旧三个网格上的失败。新求解显式赋

$$
\delta_0=\max\left(2\times10^{-8},\ \eta_{\max,\mathrm{new}}+
\frac{1+\eta_{\max,\mathrm{new}}}{10^6}\right).
\tag{1}
$$

这只是新目标中的辅助初值，物理系数和固定度量不变。新完整初态及原始来源先保存，再开始目标评价；不能因预处理或预算退出把已准备的起点丢掉。

## 3. 镜像行与真实筛选

旧目标及两条直接度量行不变：

$$
\min\delta,\qquad
\delta-e-f^2/\delta\ge0,\quad
\delta+e-f^2/\delta\ge0,\quad \delta\ge10^{-8},
$$

其中 $e=|X_s|^2-1,f=X_s\cdot T$。新增一条每点的镜像多项式行，$\tau=61/1000$：

$$
m=z^2|W|^2-\tau^2W_z^2\ge0,\qquad W=X_s\times T.
\tag{2}
$$

这是正高度、正则且对应两个不同材料点时，这些镜像点对 reach 必要条件的无除法形式。它不检查其他点对。平方行也不能独自排重合或退化，因此选择物理场时另外检查：

- 原 cap／box／signed-$z$／ball／strip 采样门；
- (2) 的最小值不少于 $-10^{-12}$；
- 所有样本 $|W|>10^{-10}$；
- 有限直接法弦值 $|z||W|/|W_z|$ 不低于 $\tau-10^{-9}$。$W_z=0$ 的点不提供该类有限上界，单列计数。

旧 $\eta\le\delta+10^{-9}$ 及除式行容差 $10^{-9}$ 保留为独立的辅助可行性记录。它们不再是保存最佳物理场的前提。上述容差都是本轮浮点求解筛选，未充当连续误差界。

对完整参数 $p$，取 $D=z^2W-\tau^2W_z e_z$，准确一阶导为

$$
D_pm=2z|W|^2D_pz
 +2(T\times D)\cdot D_pX_s
 +2(D\times X_s)\cdot D_pT.
\tag{3}
$$

实现直接用交叉积恒等式，不以浮点 $|T|=1$ 作为代数消元。无需高阶位置 Jacobian，也没有除以 $W_z$。目标、目标导数、约束、约束导数继续共享同次完整几何；单改 $\delta$ 不重算物理场。

## 4. 选择策略和预算

每个完成的 trial 保存独立记录：

1. `best_physical_max_eta_point`：通过上述物理／镜像门的真实最大 $\eta$ 最小点；最终采用此项。
2. `best_eligible_direct_max_eta_point`：还通过当前辅助量行的真实 $\eta$ 最小点。
3. `best_eligible_auxiliary_delta_point`：所有行通过时辅助 $\delta$ 最小点。

原始最小 $\delta$ trial 也继续保存，以免隐藏未可行试探。某一物理最佳场若原保存 $\delta$ 仍偏低，最终报告保留该偏差，不自动把它调大。只有 (1) 是这次明确的新辅助赋值。

最多一次 SLSQP：80 次迭代、120 次不同物理几何评价、300 秒活动目标预算；任一先到就保已完成记录。检查点仍每 10 次物理评价或 60 秒保存。旧 quartic、joint、minimax 和只读 trial 审计全部只消费，不重跑。

在 $160\times192$、163 物理参数加一个辅助参数下，返回的七组约束 Jacobian 是 $215040\times164$，单矩阵 282,132,480 字节。当前复用父六组矩阵再加镜像组，拼接瞬时还会保留父矩阵，约 524 MB；这不是整个过程内存上界。缓存额外保留每点一个镜像 Jacobian，不再保两套三向量的一阶 Jacobian。实际报告记录单矩阵字节、缓存字节及 Linux 峰值 RSS。没有同时加入巨大的二jet曲率约束。

## 5. 固定末态审计

选定物理场后先核准确系数逐位、完整 $g$、`b0` 和物理身份；冻结不会改系数。然后在同一 $160$ 径向并集上评价 $192$、$384$、$768$ 角，始终保同一个选中 trial 的原始辅助 $\delta$。报告实际 $E/F$、曲率及峰位、全部基本物理门、镜像值、唯一帽高、端口和区域分布。

当前 $384/768$ 网格可能继续揭示角向漏峰；新末态的 fine auxiliary failure 不被隐藏，也不触发第二次优化。曲率仍可能恶化；即使本轮最大误差下降，也不等于 reach 已改善或完整任务已达标。

## 6. 新源码和人工覆盖

- `scripts/frame_metric_epigraph_dense.py`：独立 subclass、镜像行／导数、两类选择和针对性人工数组检查。
- `scripts/frame_metric_epigraph_dense_audit.py`：八输入严格回放、准确节点并集、唯一求解、完整末态审计和小摘要。

开发检查覆盖新七组解析 Jacobian、四 callbacks 同缓存、单改 $\delta$ 不改物理态、辅助低估但物理更好的点仍保留、镜像失败拒绝、平方行为零却法向退化时拒绝、注入评价错误保留最佳点。完整小人工输入路径采用 `evaluate_only`，覆盖八来源、节点并集、显式新 $\delta$、冻结和末态审计；另拒绝错误第八 SHA、修改物理 state 和修改真实节点。这里没有伪造 Actions 环境，没有本地运行候选。

在公开 Actions 执行：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_metric_epigraph_dense_audit.py \
  --check-only --out "$RUNNER_TEMP/dense-mirror-development.json"
```

唯一研究入口（完整路径相对于仓库根；publisher 按现有规则归档）：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_metric_epigraph_dense_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
  --expected-input-sha256 c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 \
  --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --expected-anchor-sha256 6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3 \
  --short-audit topics/visible-flex-new-mechanism/notes/actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz \
  --expected-short-sha256 9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c \
  --height-audit topics/visible-flex-new-mechanism/notes/actions-43630874689-1-height_polytope_audit/height-polytope-bounded-audit.json.gz \
  --expected-height-sha256 f457282f0a21cd27802748066537caa4cf90c687c63c73d62b0391ce2435d1a3 \
  --prior-joint-audit topics/visible-flex-new-mechanism/notes/actions-43634358250-1-quartic_joint_audit/quartic-joint-audit.json.gz \
  --expected-prior-joint-sha256 e344e6e0a62be10dfa8dad4f52e4b889191f462b97bb19dd4b1cc0283f6f33dc \
  --resume-audit topics/visible-flex-new-mechanism/notes/actions-43635770962-1-joint_resume/quartic-reused-joint-resume.json.gz \
  --expected-resume-sha256 40deb9dffa6882b14dd445d981f2ed09b1f4d488dbaa83e952c768537f91375d \
  --epigraph-audit topics/visible-flex-new-mechanism/notes/actions-43637739532-1-metric_epigraph/frame-metric-epigraph-audit.json.gz \
  --expected-epigraph-sha256 b4d34b0d37928b2f3ffeacf5de3a072068a6314e474fb72c6cd4adb3ae9c5bc5 \
  --trial-audit topics/visible-flex-new-mechanism/notes/actions-43639240317-1-metric_epigraph_saved_trial/metric-epigraph-saved-trial-audit.json \
  --expected-trial-sha256 169e6cb8fa1bf2c5bb5c1821ee09903b344467fff66d7243cede4c938d66e05f \
  --out "$RUNNER_TEMP/metric-epigraph-dense-mirror-audit.json"
```

此处只交付实现及人工检查入口。只有公开运行回执完成后，才能写本轮人工检查通过或给实际求解结果。
