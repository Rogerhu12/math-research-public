# 选定约束行 Jacobian 的径向分解：同一 159 维场的评价设计

## 1. 范围与当前状态

本稿只给出源码可核的等价公式和一个待定实现接口。没有运行新人工、候选几何、计时或求解；没有修改当前已冻结的 SOC 条件持径源码。是否采用本评价方法，须等待该实际试验的结果。这里没有新增自由参数、改变信赖半径或扩大求解预算。

当前 `FiveHeightField` 的 159 个独立坐标由 154 个切向列与五个准确零总积分高度列组成。其完整几何 Jacobian 仍先调用旧 163 列评价，再保留前 154 列并附五列；现有选行方法在完成这个全角张量后才抽取约束点。因此“小的 LP 约束矩阵”并不等于“小的几何 Jacobian 中间张量”。这个实现事实可直接由 [FiveHeightField.geometry](../scripts/frame_five_height_field.py)、[SingleQProblem.geometry](../scripts/frame_entry_single_q.py)、[粗网批评价](../scripts/frame_curvature_epigraph_exchange.py)及[完整细网选行评价](../scripts/frame_metric_spectral_recovery.py)核对。

原 159 首次实际的细网选行 J 与粗网 geometry-J 计时分别约 79.77 秒、35.58 秒；这些是报告中的不同计时范围，存在嵌套，不能相加解释总费用。报告的峰值 RSS 为 3,173,380 KiB。它们只构成本方案的评价动机，并不证明下面的分解已经更快；科学结果仍以[该次实际说明](entry-tail-height159-first-actual-result-20261115.md)为准。

本方案的单一变化是：**先在角向模式和三个径向 jet 方向上收缩选定标量行的微分，再展开各径向系数列。** 原全网值评价、几何门、行池及求解算法保持原定义。下文的等价性是精确算术代数等价；浮点重新结合不授逐位相同。

## 2. 必须保留的真实表示

用 $s$ 表示径向变量，$\theta$ 表示材料角；输出键 `Xs/Xss` 是径向导数，`Xt/Xst/Xtt` 含角导数。记 $\Pi$ 为原零均值角原函数。源码的六个位置 jet 为

$$
\begin{aligned}
X&=a\Pi T+z_c e_z, & X_s&=a'\Pi T+a\Pi T_s+b e_z,\\
X_{ss}&=a''\Pi T+2a'\Pi T_s+a\Pi T_{ss}+b' e_z,\\
X_\theta&=aT, & X_{s\theta}&=a'T+aT_s, & X_{\theta\theta}&=aT_\theta.
\end{aligned}
\tag{1}
$$

本轮 $a,a',a''$ 全部固定；共同 $b_0$ 与其原函数固定于既有参考，当前 $u/v$ 不改变 $b_0$。当前高度只按已经定义的准确有理仿射系数及 null 原函数改变。新评价不得恢复被删除的辅助 $\beta$ 角变量，也不得添加旧实现中与本表示无关的 $\langle dV_z\rangle$。

在数值评价中，$\Pi$ 换为 `periodic_operator(...,-1)` 的同一个 $\Pi_N$：完整均匀角网、同一个角起点、同一 FFT 长度、零频及 Nyquist 规则全部保留。它对每个径向行使用同一线性算子，故下述径向乘法分解在精确算术下也适用于这个离散算子。**不得从去零模 $\Pi_N$ 推断 $\partial_\theta\Pi_N=\mathrm{id}$**；三个含角位置 jet 必须继续使用式 (1) 的原 parent 定义，不从改写后的离散原函数数值求导。原有角截断误差账不会因此消失。

当前列布局为：

| 块 | 独立列索引 | 径向数 | 角向数 | 真实变化 |
|---|---:|---:|---:|---|
| $u$ | $0\!:\!81$ | 9 | 9 | $R^u_jY^u_i$ |
| 原 $v$ | $81\!:\!153$ | 9 | 8 | $R^v_jY^v_i$ |
| 新 $Q$ | 153 | 1 | 1 | $R_Q\widehat Q$ |
| 高度 null | $154\!:\!159$ | — | — | 既有五个 $Z_k,D_k,D'_k$ |

这些索引是当前已发布 family 的事实，不能作为未经检查的通用输入假定。未来适配器须从实际 `FiveHeightField`、`SingleQProblem`、原 space identity 及切片得到布局，再核对这一支持范围；未知 family 应明确拒绝。

## 3. 径向可分离性来自实际列，不能从基场猜测

原场的自然帽、热平滑、固定入口修正可以很复杂；本稿不要求当前 $T$ 本身可分离。只要求每个参数变化的标量列具有源码已有的形式。对于 $q=u$ 或 $v$，

$$
\delta q=R_j(s)Y_i(\theta),\qquad
R^u_j=W_2B_j,\quad R^v_j=W_5B_j.
\tag{2}
$$

真实导数是乘积导数：

$$
R'_j=W'B_j+WB'_j,\qquad
R''_j=W''B_j+2W'B'_j+WB''_j.
\tag{3}
$$

不得把单独 $W_p$ 的左延当光滑函数：源码在入口左侧的 cutoff 分支与右侧不同。是 $W_pB_j$ 乘积借助原 $B_j$ 的端点消失阶付清端口 jet。新实现必须消费现有 `weights`、`bases` 和式 (3)，保留同一端点/样条结点分支。

`SingleQGrid.radial_Q` 正是 $W_5$ 乘第一 retained $B_3$ 及其前两导数；角方向 `angular_Q` 和 `angular_Q_theta` 来自既有准确归一化定义。它单独作为一个模式，不能混进旧八个 $v$ 角模式或重新归一化。原 $\theta/\phi/u_{core}$ 角模式及其角导数照读现有 `angular`、`angular_first`，不拟合、不正交化、不截断。[对应源](../scripts/frame_entry_single_q.py)与[入口乘积列](../scripts/frame_entry_paired_repair.py)已显式实现这些关系。

## 4. 三个径向虚方向的完整六 jet 恒等式

固定当前状态及一个角模式 $Y$。令

$$
F_0=T_qY,\quad F_1=(\partial_sT_q)Y,\quad
F_2=(\partial_s^2T_q)Y,\quad
F_\theta=\partial_\theta(T_qY),\qquad P_j=\Pi F_j.
\tag{4}
$$

$Y$ 不依赖 $s$；$F_\theta$ 包含 $Y_\theta$ 和当前 $u/v$ 的全角导数。源码 `complete_tangent_parameter_jets` 的 `Ts_value_part` 等于 $\partial_sT_q$，其 `Tss` 中 `value` 与 `first` 分别为 $\partial_s^2T_q$ 和 $2\partial_sT_q$。这些量可以在当前标量场上计算，不先形成 81 或 73 个参数列。

由乘法法则和固定 $a,b$，

$$
\begin{aligned}
\delta T&=RF_0,\\
\delta T_s&=RF_1+R'F_0,\\
\delta T_{ss}&=RF_2+2R'F_1+R''F_0,\\
\delta T_\theta&=RF_\theta,\\
\delta X&=RaP_0,\\
\delta X_s&=R(a'P_0+aP_1)+R'aP_0,\\
\delta X_{ss}&=R(a''P_0+2a'P_1+aP_2)
 +R'(2a'P_0+2aP_1)+R''aP_0,\\
\delta X_\theta&=RaF_0,\\
\delta X_{s\theta}&=R(a'F_0+aF_1)+R'aF_0,\\
\delta X_{\theta\theta}&=RaF_\theta.
\end{aligned}
\tag{5}
$$

因此每个选定点只需三个临时微分方向，分别取式 (5) 中 $R,R',R''$ 的系数。这三个方向不是新增物理参数，而是同一个线性微分的代数分解；可用具有指定局部二阶径向 jet 的光滑标量变化理解。它们逐项满足既有微分一致性条件 $\delta X_\theta=a\delta T$、$T\cdot\delta T=0$。

设当前某个标量约束行为 $c=c(X,X_s,T,X_\theta,X_{ss},X_{s\theta},X_{\theta\theta})$。在同一当前几何上，微分 $dc$ 对这些变分线性。分别将三个临时方向送入原行微分，得到 $L_0,L_1,L_2$，则该角模式下九个原径向系数的完整导数为

$$
\frac{\partial c}{\partial q_{ji}}
 = L_{0,i}R_j+L_{1,i}R'_j+L_{2,i}R''_j.
\tag{6}
$$

式 (6) 是先收缩后展开的依据。它保留曲率行对全部位置二 jet 的依赖，不以第一基本形式或一阶近似替代真实二阶几何。

## 5. 五高度列与当前十一组行

对第 $k$ 个既有 null 坐标，记其准确原函数/密度为 $Z_k,D_k=Z'_k$。原 wrapper 已给

$$
\delta X=Z_ke_z,\qquad \delta X_s=D_ke_z,\qquad
\delta X_{ss}=D'_ke_z;
\quad \delta T=\delta X_\theta=\delta X_{s\theta}=\delta X_{\theta\theta}=0.
\tag{7}
$$

直接把式 (7) 附为五列。使用 `null_basis.values` 的现有准确分片定义/评价规则，不能先把九个依赖高度系数舍入后交给旧 163 几何求值。当前非零 null 高度已进入普通几何 $X,X_s,X_{ss}$，故式 (6)(7) 的行微分必须以 **当前真实 159 状态的普通 jet** 为基点，不能用九参考高度的旧几何代替。

选行接口应复用 [selected_spectral_parameter_jacobian](../scripts/frame_metric_spectral_recovery.py)，其参数轴长度由输入推断，允许本处三个临时方向：

- 组 0/1 保当前平滑两谱支，$\epsilon=10^{-8}$，不是旧 Schur 提案；
- 组 2–6 保真实 signed-z、球、两条带、镜像点对多项式及原单位；
- 组 7–10 保固定硬曲率 $58$ 与 scale $100$ 的完整 trace/determinant 四行，调用原二 jet 微分；
- 真实验收仍独立使用原两网真 $\eta$、原 Schur budget、direct $\kappa$、全部物理门及原容差，不能被提案导数替换。

一次批中若无曲率行，可以只形成原接口需要的一阶参数 jet；若有曲率行，必须带全二 jet。同一几何点可以对应多个行组，须按原扁平行 ID、组号及粗/细网标签逐行返回，不去重成不同约束。

## 6. 一个最小适配接口

建议独立函数的逻辑签名为：

```text
selected_rows_jacobian(field159, state159,
    full_radial, full_theta, selected_row_ids,
    authoritative_ordinary_cache, cfg) -> J[rows, 159], diagnostics
```

固定返回当前顺序的 159 列；没有新的辅助优化变量。完整 row ID 仍为 $g(N_rN_\theta)+iN_\theta+j$，粗细网各用自己的 $N_\theta$。

必要来源路径应显式走：

```text
q = field.coordinates.validate(state159)
reference163 = field.coordinates.reference_evaluation_state(q)
single = field.original_problem
grid = single.source.grid_for(batch_radial, full_theta)
fields = grid.fields(reference163)
```

`FiveHeightField.source` 是原切向 family 的元数据代理，不应误把 159 向量直接喂给原接 163 向量的 grid。普通几何从已经绑定当前 state/grid/evaluation identity 的完整值缓存取；高度补量用式 (7)，不重复旧 163 全列 Jacobian。标量 `fields` 必须按当前 u/v 重建并使用同一个 frozen source 的 GH/自然帽/入口规则。

每个径向批保现有最多 16 个 owned 行加 0/L 的批约定。每个模式族仍计算 **全部角网** 的 $F_j,\Pi_NF_j$，再选所需点，最后以式 (6) 展开。这里不能用孤立奇角查询替代 768 网，也不能把 768 角变化传进固定 Nb 的高度均值定义。

最小 objective 适配可只替换 `linear_rows` 内部取得粗/细参数矩阵的路径，保原 `constraint_fun/fine_rows`、全值缓存、pool 学习、row-map、tolerance、primary/SOC 数组 LP 和总步模型记录。旧内部固定曲率辅助列并非物理自由变量，原 `linear_rows` 本来只保前 $n$ 列；新接口不应为省事另改辅助含义。

缓存必须绑定 exact state bytes、完整粗/细角网、径向 owned/query 行、source/evaluation/coordinate identity 和原行顺序。可先仅保与现行同样的 state+pool-version 生命周期，避免同时改变跨 pool 的缓存策略。接受回滚恢复原 ordinary cache 的逻辑不可被选行 J 缓存破坏。未知 family、variable metric、不同 H/reference 或不同角网均应拒绝，不静默退回另一数学定义。

## 7. 内存量级与尚未支付的费用

这些只是形状乘法的容量估计，不是实际测量或 RSS 上界。以 18 个 query 径向行、768 角、binary64、三维向量为例：

- 一个完整 163 列向量 jet 为 $18\cdot768\cdot3\cdot163\cdot8=54{,}079{,}488$ 字节；六个位置 jet 已超过 324 MB，尚不含 $T$、临时角导数/FFT、旧新数组同时存在和普通全网缓存。
- 一个九角模式族的向量 kernel 为 $18\cdot768\cdot3\cdot9\cdot8=2{,}985{,}984$ 字节。四个 $F$ 与三个 $P$ 同时保留约 20.9 MB；顺序处理 $u$ 九模、$v$ 八模、$Q$ 一模，避免把它们与九径向列同时扩张。
- 最终选行矩阵仍为 $m\cdot159\cdot8$ 字节，原 LP 行数、列数和普通全网值缓存都没有减少。复数 FFT 工作区、分配器缓存、原 source grid 的固定帽数组仍需另计。

因此源码可证明的是“不再需要构造全角参数轴 163/159 的位置 jet 张量”，并非全进程内存必降某个比例。GH/固定场构造、普通值几何、最终两网审计、LP、恢复前缀不会自动消失。未来计时须分别记普通值、标量场、angular kernels/FFT、选行收缩/径向展开、粗/细 J 合计、峰 RSS 和总过程时间；不得把重叠 scope 相加。

## 8. 浮点评价身份、首次验证与采用条件

连续物理定义、准确 159 坐标及依赖九高度系数、固定 $g/b_0/c_0$、帽高常量、原盒、原 gate/config/全部池均不变；新数学对象仅是相同微分的分解。实现来源、FFT 批轴形状、收缩次序和新的评价规则应有独立 evaluation identity。浮点结果可能相差末位，甚至在紧约束或 wall budget 下改变 LP/接受轨迹；不能声称重放原 solver 路径或沿用旧 candidate 的通过结论。

只有未来确定需要实现时，首次公共开发应覆盖这个新增接口的具体风险：在允许的小人工实际 family 上，保非零 null 高度及 Q，选粗细网全部十一组（含 fine 奇角、入口与样条结点、端口），对照原完整 Jacobian 和新选行矩阵；另对全部六位置 jet 的方向收缩作直接比较。再检查 row/column 排序、当前场与 reference 的区别、同一原字段的方向差分及严格错身份拒绝。它不是重跑旧 solver 或旧研究的前置机械复验。

这些验证尚未执行，也未设研究重跑请求。若本轮 SOC 持径实际显示主要瓶颈已经不在 Jacobian 时间，不应因为本设计可用就追加一个相同科学问题的求解。若有明确必要的新科学步骤，才把此评价作为可单独记账的实现变更接入该步骤，所有普通几何及原两网验收仍走权威路径。

## 9. 本稿的源码审读范围

本稿只读核了下列当前文件，不调用其开发入口或研究函数：

| 源文件 | SHA256 |
|---|---|
| `frame_entry_single_q.py` | `b0744e42b00854b85ac6828afc4520c0505b5d4800c47ab4d8bb96c84d04e286` |
| `frame_entry_paired_repair.py` | `8f09d96a4377175e0242a37f1450960f0914e28a787699565d437058e7625ac1` |
| `frame_five_height_field.py` | `549e61db392f318260d636d41a090bd56e8c96b2eab580075707b5e25a24f656` |
| `frame_metric_spectral_recovery.py` | `27fcdbc71a6d9d07e0cba962067e61d7f8439ef06d47cdbdf9c669ce1ea2c428` |
| `frame_metric_budget_restoration_rows.py` | `eff06d6c2136b8b13fa86afe915352ee54e5aaae2c4c80551a08355cea2e1d4f` |
| `frame_curvature_epigraph_exchange.py` | `8c26353df012ca61f37149b2e2ab52acaec4ca22fde68017261c0bd68992ebf5` |
| `frame_collar_bvp.py` | `64dffdbfc6456fe022105d264442d307c8f88022cdf755ec0a41ea97fff93d00` |

独立纸核已确认式 (5) 的乘法法则及先收缩后三径向 jet 展开的线性性；特意保留“角位置导数沿用 parent 定义、不能从去零模 primitive 偷推恒等算子”的限制。没有人工 passed 标签、性能结论或新几何结论。
