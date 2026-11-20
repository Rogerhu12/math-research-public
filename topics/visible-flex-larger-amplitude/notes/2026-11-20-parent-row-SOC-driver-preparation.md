# 同完整父行 SOC：真实残差、原范数修正与原/R671 driver 接线

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。**状态：完整小源及精确源码派生已准备；只做源码读取、AST 生成和编译，没有科学执行、没有 SOC 成功候选，也没有更改正在运行的源。** 数学命题直接引用 [R680](../results/R680-true-geometric-step-second-order-correction.md)，不重复编号。

## 1. 此次实际返回支持什么判断

[44758209061/1 的阶段 31–33](2026-11-20-public-actions-44758209061-1-part-002.md) 已实际返回原模型六方向。终态 bundle 为 `e08cc378d49eb8c86b42a0773b6335f2cb3a0412416527ba6590c54db3c81a15`，真 Phi 为 `7.950104188911605e-8`，点态 maxGram 为 `.011733677396962518`。六方向都到 256 次上限，接受的原射线 alpha 依次为 `.5,.5,.125,.25,.25,.25`，末必要点乘积为 `.9919991085630754`。

六个原满步的首次拒绝均明确是 `true_known_point_geometry`；满步实际下降与同一步预测下降的比值从约 `1.075` 到 `1.0066`。R671 实际满步同样因真几何被拒，其 Phi 已到 `8.45616947482e-8`。这给一次几何修正的直接动机，但尚不能证明拒绝来自**已线性化的同一具体行**的二阶项：旧完整 trial 主要报告全最大乘积，没有逐个父行的 $c_i(d)$。

原方向仍是截断 QP 方向：iteration limit、负乘子或未达 projected-gradient 容差均如实保留。它们没有被 SOC 命名变成 KKT 解。32 步重启的真实次数已有报告，但上述数据不构成它是主因的因果证明。本实现不改 QP 求解器、重启政策或预条件器。

## 2. 冻结父行的具体含义

当前 `fullclosed_point_inequalities_v2.py` 的实际源码是

`e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8`。

它对每个选中行记录：

- `curvature_point`：`('grid',stage,angle,branch)` 或 `('arbitrary',cell,u,phi,branch)`；branch 是当前有符号广义主曲率的排序分支。
- `radius_point`：某个 grid/arbitrary 点，或 `fixed_core`、`cap_height`。
- 父点的 `gradient_coordinate_norm`、`current_product`、`normalized_bound` 和 `principal_metadata`。

设同一个父点完整坐标映射为 T。对原返回方向 d，helper 读取的准确有限函数是

$$
c_i(d)=\frac{.03D_i(x+Td)|\kappa_i(x+Td)|-.992}{n_i(x)}.
$$

每个 $D_i$ 保持父行的原伙伴。普通位置取 $2|F|$，固定 core 为 2，帽高为 $2|H|$。不把伙伴换成新 trial 的最大半径，不换主曲率 branch，不重新归一化 $n_i$，也不拿全最大 product 复制到所有行。

grid 行按原 `single_fields` 的 grid 浮点评价约定读取；arbitrary 行按原完整 `fields_at` 读取。grid 不改成数值近似相同的任意角评价。所有位置使用完整 binary tuple，没有 `round13`。

同一读取同时输出

$$
c_i(d)-(C_i d-b_i),
$$

这是该次实际父行的非线性余项。若没有正的父行 residual，helper 不杜撰原因：可能涉及未选伙伴、额外 absolute curvature cap，或两个数值评价的差；此时没有本次 SOC 行集合，直接保原回溯。

## 3. 一次修正与完整旧余量

令 $I=\{i:c_i(d)>0\}$。算法显式接收非负有限参数 tau，并取

$$
h_i=c_i(d)+\mathrm{tau}\,\|d\|^3,\qquad i\in I.
$$

`tau=0` 是明确的无三阶内推版本；正 tau 也只是实际算法参数。当前没有严格 L 或 gamma、没有支付 R680 的 tau 阈值或局部邻域，所以不把数值提案称作定理已经保证成功。

在原增广坐标的欧氏范数中，按两遍 row Gram–Schmidt 构成

$$
C_I=RQ,\qquad QQ^T\approx I,
$$

其中 R 是**下三角**。因此使用

$$
e=-Q^T\operatorname{solve}(R,h).
$$

这与 R680 的列 QR 写法完全一致，但此存储约定下不能错误地解 $R^T$。不显式形成或求逆 $C_IC_I^T$。完整 Q 放在 Actions raw memmap，所有投影/转置用列分块；峰值不需容纳整个 Q。实际 rank cutoff 沿本方向的 QP 参数，记录每行独立余量、R 的奇异值诊断及 Q 正交误差。数值秩不是严格最小奇异值证书。

若所选集合有数值相关行，整次 SOC 提案失败；不删除该行后冒称修复了原集合。没有调用一个从不可行零点启动的 Phase I，也不把 least-squares residual 冒作可行修正。

原完整 T 包含 DI、物理高度、角 $H^2$ 和同范数 coarse 冗余。父行是实际物理 covector 经同一个 $T^T$ 拉回，所以 $\ker T\subseteq\ker C_I$；准确最小范数 e 位于 $\operatorname{ran}C_I^T$，与无用零场坐标正交。没有在某个预条件坐标里另取欧氏范数；独立 CoarseFrame 不是本 helper 的依赖。

提案前重读全部原 $C d$。提案后既读 $Ce$，又独立读 $C(d+e)$，对**全部旧行**输出

$$
s_j=b_j-C_jd,\qquad s_j^{\rm corrected}=b_j-C_j(d+e).
$$

因此未进 I 的近活动行和原正余量都受完整复查。任何旧行超出原数值 feasibility tolerance，立即保原射线回溯。报告保全部余量、最大违反量、$C_Ie+h$、累积与直接乘积差，以及乘回父 norm 后的实际物理线性乘积。允许的数值 tolerance 也乘回各 norm 明示；这不冒严格精确线性可行性。

## 4. helper 的真实 API 与身份

[full_phi_parent_row_soc.py](../scripts/resume_20261120/full_phi_parent_row_soc.py)，30,947 B，SHA256：

`5bc50d6b18223685da8ea355d179191234ad83b5e92fd6313f4070b7e02127c7`。

已由 root 单独发表。本次不修改其冻结字节。

```python
engine = soc_module.ParentRowsSOC(
    problem, parent_x, active_rows, active_bounds, active_metadata,
    geometry_module=geometry_module,
    point_module=point_module,
    observed_module=implementation,
    inequality_module=inequality_module,
    source_sha256_by_role=report['source_sha256_by_role'],
    observation_carrier_sha256=report['observation_carrier_sha256'],
    model_definition=None,  # R671 使用当前 context.definition()
    block_columns=args.active_block_columns,
)
proposal = engine.propose(
    coordinate_step, lift, full_trial_point, full_trial,
    tau=args.soc_tau, workdir=unique_raw_directory,
    rank_tolerance=args.qp_row_rank_tolerance,
    feasibility_tolerance=args.qp_feasibility_tolerance,
)
```

返回 `Proposal(candidate, augmented_step, correction, report)`。前三项是 runner raw 数组；report 可 JSON 序列化。`candidate=None` 表示这次没有可交给完整真接受器的提案。helper 不更新 x、不更新阻尼、不接受任何场。

构造时核当前 row-cache 路径、顺序、字面 bounds、真实 norm/margin 公式，以及 geometry/point/observed/inequality 的源 SHA。R671 还核 canonical definition 和真实 factory `point_adapter`、真实 `fields_block`。非零 lambda 不能用旧 operator 冒读；lambda0 工厂允许使用其准确原类分支，但保其 canonical 身份。身份/API 错误直接抛出，不当作科学失败吞掉。

普通数值奇异点、非有限值、数值相关行可有明确提案失败原因。两端的 gap、曲率符号及帽高符号仅是实际记录，不被误称已控制了整条步路径的光滑分支。

## 5. 原/R671 driver 的精确接线

[derive_full_phi_parent_row_soc.py](../scripts/resume_20261120/derive_full_phi_parent_row_soc.py)，24,122 B，SHA256：

`805823e49970246bf532b65a0caefd88244b414ee52f8f555ff28b745d2fd30a`。

该源从准确冻结的 original `5ef7e268…` 或 R671 `b1b0725a…` 开始，先使用已刊 `100e57c6…` 的完整位置 AST 变换，再生成独立 SOC driver。它不修改两个原文件。十二个指定接点在两个实际源上各匹配一次，并已静态编译。

关键接点是：

1. 增加显式 `--soc-source`、`--soc-tau` 和 Actions 执行限制，核 helper SHA。
2. 将 `A`、`model_residual`、`coordinate_step`、`active_rows/bounds` 的释放延后到整方向结束。原 driver 在首 trial 前已删除这些对象，不能保持原代码清理位置又声称复用了父模型。
3. 原完整满步照常读取 Phi/domain/全量点几何，照常保存其新永久点。只有首个 alpha=1 的目标/domain 通过而实际几何拒绝时，才调用一次 SOC。
4. corrected 候选使用同一原父模型重新读取一次 $A(d+e)$，得到自己的半斜率、预测能量和实际预测变化；不复用未修正 d 的预测分母。
5. corrected 候选再次读取完整原/Gauss Phi、同域条件以及当前全部 grid、永久曲率与永久半径点。原满步刚发现的点也已经在此集合中。修正 trial 的新位置无论接受与否都进入同一永久记忆。
6. 若修正未通过，原 `x+alpha*T*d` 射线的二分回溯继续；不把失败 trial 设成父，不追加第二次修正，不增加本次 QP advances。

实际 corrected 接受沿原规则消费

$$
\Phi_{
m c}<\Phi_0,\qquad
\Phi_{
m c}\le\Phi_0+2\cdot10^{-4}\,s_{
m c},
\quad s_{
m c}=v^TA(d+e),
$$

其中非负半斜率时严格下降已经蕴含该 Armijo 不等式，保原 driver 的写法。目标导数是 $2s_{\rm c}$，没有漏掉二倍因子。预测为

$$
\Phi_{\rm pred,c}=\Phi_0+2s_{\rm c}+\|A(d+e)\|^2.
$$

SOC 真接受后，记录的 `direction_sha256`、坐标范数、endpoint 误差、两 jet 步幅、半斜率、预测和 ratio 切到这一真实修正方向。原返回 QP 的报告仍保原样，并明确 `main_QP_diagnostics_remain_uncorrected=True`；原方向模型另存 `uncorrected_direction_model`，原 trial 列表不被覆盖。修正 raw 另写 `direction-XXX-soc.npz`，含主方向、e、d+e 和原 norm 构件。

阻尼仍用相同更新算式：实际接受的完整方向 ratio 大于 `.75` 则减半至原最小值；接受原半步保持；完整方向拒绝则乘 4。区别是 SOC 接受时 ratio 明确属于 corrected 完整方向。每方向额外写 `damping_after_direction`，终态写 `final_damping`，以便完整来源绑定后交叉读取。旧 QP 诊断与 corrected 模型应分别消费，不能把 corrected 步冒称 QP 的最优或最终迭代点。

成本单列实际额外 J/J* 次数、corrected 模型 matvec、非线性 residual、完整几何读取与用时。没有假造第二次 QP。SOC helper 的全父行真值、两次 literal C 乘积和 QR 诊断保在 raw report。

## 6. 真实完整父 report 的入口

[launch_full_phi_parent_row_soc.py](../scripts/resume_20261120/launch_full_phi_parent_row_soc.py)，19,434 B，SHA256：

`9b7d50fd7d1a0332fc493f848688b792dff39fd2a1af4914349d048abe080d0a`。

默认一次主方向、256 advances、atol=0；tau 必须显式给出。这个准备源没有替 root 选择首个实际 tau，也未排预算。

入口字段为：

| 字段 | 责任 |
|---|---|
| `--model original` 或 `--model R671` | 选择真实完整父的物理模型 |
| `--parent-report`、`--bundle`、`--carrier` | 真实自然完成终态、实际 final SHA、原观察载体 |
| 重复 `--manifest` | 调用者全部旧永久位置；与父 report 全历史精确并集 |
| R671 的 `--node-report`、`--scalar-input` | 425f 入口的同非零 canonical lambda/eta/scalar，keep-q |
| `--parent-source` | 需要时提供实际派生父源码；未来 SOC 父必需 |
| `--soc-tau` | 显式算法参数，不是已付定理常数 |
| `--print-command` | 只做标准库来源/参数准备，不读取科学数组或执行科学 |

首个旧父通过完全未改的 original `18ba10e5…` 或 R671 `425fd1d1…` completed-report 入口，以其 `--print-command` 验证源、终态 bundle、真实末 mu、完整位置、固定 scalar、目标和范数。然后只把其已记录 scientific argv 的 driver 换成新确证 SOC 派生源并加两个 SOC 参数。

实际执行前，沿同一已刊 `4d9dd319…` 的 Locations 读取父 report 和调用者 manifest 的全部历史位置；stage 位置仅在 Actions 中按原 carrier/原 N 解析。所有 u/phi binary 值、保护点、各 trial 的新点以及实际 final memories 都保留。原 manifest 可逐字传入，补充纯位置文件明确只继承位置而不继承旧几何值。

若旧父使用 v3，规划器按其真实 `source_sha256_by_role['qp']` 继承 v3；不回退到默认 v2。显式另选 QP 源仍是独立记录的选择。本次 SOC 本身不接新 PCG。

对未来 SOC 父，`bind_soc_parent` 必须用准确 frozen base、100e 位置变换和本 805 源重建**整个实际 body AST**，同时核 actual 文件 SHA、helper SHA 和报告 schema。然后一个独立、明确标识且只能 `--print-command` 的旧规划器派生版，调用这个新 binder。没有编辑父 report 来冒旧源，没有删除旧 guard，也不只相信 provenance 注释头。终 mu 只在完整新来源绑定后按准确实际规则重放，并与明确的每步/最终字段核对。

若后续另接 PCG，现 805 binder 应严格拒绝新增未知 body；必须有另一份明确完整组合派生及 binder 重建该第二步。本独立 SOC 链不预先接受未来任意变换。

## 7. 实际静态准备范围与未付事项

本次只执行：源码读取、SHA/文件 metadata、纯标准库 AST 变换、编译。没有导入或执行 field/NumPy/SciPy 科学模块，没有试读旧父或新父，没有新 fixture、区间扫描、求解或 Actions 预算。

本地生成的两个完整派生 driver 仅供源码核对，实际 runner 会按其真实路径再生并记录真实 SHA：

| 静态派生文件 | 大小 | 本次完整字节 SHA256 |
|---|---:|---|
| `soc-derived-static-02/original-soc.py` | 52,635 B | `deac5b0680a845c1066d4c3e6f9a46c34aca76b90efa02d12669409d1ef3c76a` |
| `soc-derived-static-02/R671-soc.py` | 58,350 B | `9c992ee674ebe6fea428bdc941722ed72ac2f6c9aac7aaa7e3ba27f46b637f96` |

它们的头包含实际本地输入路径，因此上述文件 SHA 不冒称未来 runner 字节 SHA。数学/执行 body 的确证采用完整 AST 重建，报告仍绑定运行时真实完整文件 SHA。

当前仍没有证据说明一次 SOC 会通过；父行相关、未选点、实际 corrected Phi 或几何均可拒绝。真实全几何只仍是有限必要点 screen，不支付连续 K/reach、metric $10^{-6}$ 或固定 g 的持续精化。

## 8. 新 report 的消费者责任

SOC 真接受时，顶层方向 SHA、半斜率和预测属于实际修正方向；`record.trials` 仍属于未修正射线，主 QP 报告也保原方向。后续归因须分别读取 `record.soc.trial`，以及 `uncorrected_direction_model` 配合原 `trials`。旧 bottleneck 或 saved-ray 消费器若未明确支持此 schema，不得将 corrected 顶层预测与旧射线混用；没有声称这些旧入口已兼容。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
