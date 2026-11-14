# R163 — 固定完整函数定义的 P1 径向细分与真实浮点注入

**状态：已证明。** 在旧节点全部保留、完整物理参数及 atlas/lifting/非线性窗固定时，实数算术下的 P1 径向细分准确保留 R153/R155 之后的完整场。整帽支撑内的冗余 gauge 可以重新选取而不改变该场。实际 binary64 新系数存在明确舍入，本文如实报告，不把它冒称为 R158 零填充那样的逐字节精确注入。

该能力提供同一物理目标上的细网格初值和自然短批恢复，不执行 BVP，不证明求解或几何完成。单纯细分不减小旧连续场的真实缺陷；需要后续实际求解利用新自由度。

## 1. 完整对象和实数 P1 嵌套

旧径向节点为 $s_0<\cdots<s_N$，每节点 raw 系数向量 $y_i\in\mathbb R^{3K+2}$，三个角向块依次为
$$
(n_0,n_2,\ldots,n_{2K}),\quad
(m_2,m_4,\ldots,m_{2K}),\quad
(l_0,l_2,\ldots,l_{2K}).
$$
记其逐分量连续线性插值为 $Y(s)$。给定有限旧 cell 集合 $I$，每个 $i\in I$ 增加一个严格内部点 $\sigma_i$，理想选择是中点。所有原节点保留；不存在 coalescing、移动旧节点或重新生成物理坐标。

在新节点上定义
$$
\widetilde y(s_i)=y_i,\qquad
\widetilde y(\sigma_i)=
\frac{s_{i+1}-\sigma_i}{s_{i+1}-s_i}y_i+
\frac{\sigma_i-s_i}{s_{i+1}-s_i}y_{i+1}.
\tag{1}
$$
旧 $Y$ 在每个旧 cell 上是仿射函数。每个新子 cell 的两端值由 (1) 给出，故仿射函数的唯一性推出
$$\boxed{\widetilde Y(s)=Y(s)\quad\hbox{于完整原径向域。}}\tag{2}$$
旧节点的左右导数仍是原来对应的单侧导数；新插入点两侧的 raw 斜率等于原 cell 斜率。因此 (2) 同时保持所有存在的单侧径向导数和完整角导数，不是仅保节点值。

设原完整 affine 场为
$$S_0(s,\xi)=\mathcal F_KY(s)+L(s,\xi;p),\tag{3}$$
其中 $\mathcal F_K$ 是既定三块 Fourier 求值，$L$ 包括准确 seed、tail 和冻结 coast lifting。固定原物理参数 $p$、度量 $a_\delta$、角图 $u=U(s,\xi)$、$L$ 的定义及 R153/R155 全部窗。由 (2)，(3) 是同一个完整函数。

在原 R153 定义域上，$n>0$ 的局部变换
$$l_*=(1-w_C)l+w_C(K+m^2)/n$$
输入完全相同，所以输出相同；尾部不借此除以零 $n$。继之 R155
$$
d=n-l_*,\quad h=\sqrt{d^2+4m^2+4K},\quad
E=\frac{w_T}{2}(h-n-l_*),\quad
(n,m,l_*)\mapsto(n+E,m,l_*+E)
\tag{4}
$$
亦收到相同输入。准确 cut 仍直接返回原非负平尾迹。故实数细分保持整个实际非线性场、其真实定义域及已有完整角函数，不引入正尾 $n$ 或额外曲面正则性条件。

## 2. 整帽支撑和冗余坐标的重新计算

新网格第 $j$ 个内部节点的 P1 帽函数 $\varphi_j$ 的闭支撑是
$$\operatorname{supp}\varphi_j=[\widetilde s_{j-1},\widetilde s_{j+1}].\tag{5}$$
因此不能把旧 inactive 节点编号简单沿用或只判断新节点本身位于平台。

### 2.1 R153 的 $l$ 冗余

若 (5) 完整包含于准确 $w_C=1$ 的平台，则任意只加在该帽上的 raw $l$ 角函数，经 R153 后被完全删除。改变它不影响实际 $n,m,l_*$ 及其任何存在的导数。因此可将这些节点的 raw $l$ 系数置零。

若帽支撑碰到 $w_C\ne1$ 的 rim，则原 $l$ 仍乘以非零的 $1-w_C$，必须保留该自由度。本文接口使用保存的物理平台端点和新帽的两个邻节点重算，不按节点中心或舍入的局部采样判定。

### 2.2 R155 的 trace 冗余

在完整 $w_T=1$ 平台上，(4) 只依赖 $d=n-l_*,m,K$，与原 trace $n+l_*$ 无关。给 $n,l_*$ 同加任意 $t$ 时，$d,h$ 不变，$E$ 减少 $t$，所以最终场不变。

若 (5) 完整包含于 $[s_+,S]$，且与 R153 支撑分离，可在该节点将对应 raw 系数改成
$$
\widetilde n_j=(n_j-l_j)/2,\qquad
\widetilde l_j=-\widetilde n_j.
\tag{6}
$$
两分量改变相同，且支撑完整落在平台，所以实际全场准确不变。新消元列是 $l_j$，其匹配的自由方向满足 $\Delta l_j=-\Delta n_j$；完整 Jacobian 的有效列因而仍是 $J_{n_j}-J_{l_j}$。这仅重选已有点态恒等式的冗余坐标，不补新方程。

接口只对上述两类整帽冗余做可选规范化，不调用通用边界重施函数。中央非齐次值、准确尾 cut 和原 rim 自由度不会因此被重新投影。浮点 (6) 对 $d$ 的微小舍入另行计算，见第 5 节。

## 3. 必须固定的定义与必须更新的计算信息

实例先读取实际保存数组及显式 parameter layout，再核对以下完整函数身份：candidate、fixed base $T$、真实 bump supports、中央/尾类型、seed 权重、完整 angular atlas、冻结 coast/reference 求值、R153 平台和 R155 窗。

R155 的 `start / ramp_stop / cut` **直接从保存包复制**。它们不因新 constructor 的另一种浮点加法、默认 mesh 或重新拟合而变化。R153 的物理平台端点亦保持。元数据里只有与 mesh 有关的 inactive 列表允许更新。

必须重新计算的量为：$N,h$, unknown/equation counts、实际新节点上的同一角图、exact central 节点集合、R153 retained Gauss 行与整帽 $l$ 索引、R155 retained 行与成对 trace gauge、所有相应列索引及按节点缓存。旧 operator、Gauss-cell、chunk、known-coast 或内部点缓存不能被当作新网格缓存使用。

每个旧 cell 的原物理区间和全部新子 cell 编号一起保存。若旧内部指导行覆盖旧 cells $I_0$，新选择覆盖它们的所有子 cell。这样不会因插入点使索引移位而把原物理区间误换成别处。

新的节点、每个子 cell 的 Gauss2 求积及内部指导行形成**新的有限离散**。即使实数函数 (2) 完全相同，旧有限残差和新有限残差也不必相同。真实连续缺陷并未由插点自动下降，本文不把有限求积变化冒称几何改善。

## 4. 与独立尾次数的角阶嵌套相容

设 $Z$ 为 R158 的 raw/central 角系数零填充，保持 tail 参数数和 profile 参数数。径向插值 $P$ 作用于节点轴，$Z$ 作用于角系数轴，所以
$$PZ=ZP.\tag{7}$$
这是两个线性映射作用于不同因子的直接恒等式。准确中央和尾函数、完整 lifting、atlas 及非线性变换保持时，两种顺序在实数算术下给同一个最终场。第 2 节的冗余规范化亦逐角系数进行，其完整场不变性独立于 $K$。

实际消费推荐先在原 mesh 上用 R158 完成角零填充，形成明确的 $K=31$、tail count $16$、profile count $7$ 存档，再径向细分。$95$ 个 raw 列和 $54$ 个参数不能经旧 $K+1$ 尾解码器解释。

通用 `v3` factory 按保存的原 kind 或 independent-tail kind 选择原 provider 及其显式 slices。没有 Bernstein 升阶，没有参数截断或填充尾参数，没有为使矩阵方阵而增补残差行。原 $K=15$ 与独立 tail 的 $K=31$ 均复用同一个实数定理。

## 5. binary64 实体的诚实舍入界

保存的新中点可能是准确实数中点附近的 binary64 数 $\sigma$。式 (1) 对任意严格内部 $\sigma$ 都成立，所以其微小坐标偏差本身不妨碍实数嵌套。需要记录的是：新系数以 binary64 算术求值，未必等于 (1) 的准确实数结果。

本 helper 将输入的二进制节点和系数准确转为有理数，计算每个实际新坐标处的准确插值，再与真实保存数比较。若新节点系数误差的最大绝对值为 $e$，因原节点误差为零、误差在新子 cell 上线性，其完整系数 $L^\infty$ 误差不超过 $e$；对应每侧斜率误差不超过 $e$ 除以该子 cell 长度。这个结论属于 raw 插值误差，不自动变成通过相除变换后的全域几何证书。

真实 19 final 六格例子，规范化前的准确界是
$$
e\le2^{-52}=2.220446049250313\times10^{-16},
\qquad
e_{s}\le\frac1{14636698788954}<6.833\times10^{-14}.
\tag{8}
$$
实际新坐标距准确中点最多 $2^{-53}$。整帽 trace 规范化后 $d$ 的最大系数舍入误差为 $2^{-51}$。raw gauge 系数可有约 $1.11254$ 的变化，这是第 2 节的可消坐标，不是把该大数当作实际场变化。

在 R153 原正 $n$ 定义域内，其分式变换连续；R155 的平方根是相应向量范数，保持固定 $K\ge0$ 时有范数 Lipschitz 界。因此小系数误差按这些明确映射传递；若需要全域数值证书，仍要消费实际统一正下界与全角导数界。本次只报告共同点的真实实现差异，没有额外建立那条全域舍入后验，也不因此添加求解门。

## 6. 接口、恢复和真实小核

最初实际六格 helper 为
`scripts/fd2d_gc_midpoint_refined_positive_trace.py`，
SHA256 `10f98ab419c15a4593c28c40cd1309fc4fab9a91e85c714b787fdcb7b58f9158`。
其绑定检查为 `scripts/fd2d-midpoint-refined-positive-trace-check.py`，完整来源保持不变。

当前通用入口是
`scripts/fd2d_gc_midpoint_refined_positive_trace_v3.py`，
SHA256 `58053fbaeb655d7fbec529783576b63d62a25abba0610884e27725fbe1790356`：

- `create_midpoint_refined_problem(candidate, saved_field=..., split_cells=[...], **common)`：构造独立新对象，按保存 kind 选择原布局或 independent-tail 布局。
- `.inject_saved_field(canonicalize_redundant=True)`：返回新向量和明确 definition，参数向量逐字节复制。
- `checkpoint_arrays(problem, vector, candidate_sha256, refinement_definition=...)`：保存原 field schema、全部实际 mesh 相关索引及旧区间到新子 cell 映射。
- 自然短批 restart 使用 `split_cells=()`：恢复保存的实际 mesh 和系数字节，不再次插点、插值或规范化 gauge。保存的 finite 内部行定义原样保留。

此前 `v2` 只补独立 tail 布局；其源码与小数组检查原样保留。`v3` 再补空 split 的明确恢复支路，没有给物理场引入 parent+detail、补偿 lifting 或新数学表示。

### 6.1 真实 19 final 共同点小核

输入为 `notes/2026-11-12-fd2d-raw-bump-stream19-b0004-accepted-0002.npz`，
SHA256 `c56c1046d2c605d9d6c31bd816766c34ed0ca8eba2292e340332f4022eeba901`。
旧 cells $63,65,71,118,119,121$ 各加一个中点；$123\to129$ 节点，原参数仍为 $38$ 个。
原内部 cells $(63,71,118)$ 映到 $(63,64,73,74,121,122)$。

实际执行 **12132**，初始 chunk **2ced88**、最终 **d4092a**，自然 exit **0**；实测 $5.699$ 秒、最大 RSS $88972$ KiB。实体：
`notes/2026-11-12-fd2d-midpoint-refinement-19final-01-field.npz`，
SHA256 `d93a16d60f6379c5cf24bfca91ab60390e65880ca781ad800a9c271a2d1890e1`。

$33$ 个共同径向点乘 $64$ 个共同角度，完整实际值误差最大
$3.553\times10^{-15}$，角一 jet 误差最大 $3.553\times10^{-14}$；
lifting、标量 profile 及角图的此次共同求值差为零。
原 `PositiveTraceNativeField` v2 直接接受新数组及正确新帽索引，不需新 reader schema。
另在 $128$ 个角 jet 点和 $16$ 个内部径向/mixed jet 点，最大 scaled 差为
$2.156\times10^{-14}$。没有请求准确 cut 的未声明径向 II jet。

这些是原完整函数的有界共同点实现检查，不是连续证书。未计算完整目标、Jacobian、body 或 BVP，也没有重跑 K31 的完整字段核。

### 6.2 小数组交换与空恢复

`fd2d-midpoint-refinement-layout-check.py` 仅在上述真实输入数组上比较两种线性操作顺序：$15\to31$，tail $16$、profile $7$，raw 列 $47\to95$、参数 $38\to54$。实际 **82764 / 80fdc2** 自然 exit **0**，$0.393$ 秒，两个顺序的保存数组差为零。它没有构造或求解 K31 场；通用类选择和参数布局独立于这次浮点零差。

`fd2d-midpoint-refinement-restart-check.py` 消费已保存的真实 $129$ 节点实体，用 `v3` 的空 split 支路重建对象。实际 **53923 / bdf9c6** 自然 exit **0**，$0.947$ 秒；原每个数组的 dtype、shape 和字节均保持，仅另加本次恢复 provenance。此核只处理 constructor/数组/布局，没有重复共同场、native、F、J 或 BVP 检查。

参考：R149（固定完整角 atlas）、R153/R155（两种实际非线性场及整帽冗余）、R158（独立尾次数的角零填充）、R162（与本条不同的改初值淡出操作）。
