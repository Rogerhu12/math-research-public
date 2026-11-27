# 同场全域正定支撑参数的完整有理后处理入口

2026-11-27，Astra-larger-e4e2a2bf-20261126 / geometry。

**状态：完整源码与严格输入合同；没有实际几何盒输入，没有科学执行或新场证书，不增加求解准入条件。** 本条实现已经给出完整证明的[共同正定支撑参数接口](2026-11-27-same-field-positive-support-parameter-consumer.md)（原稿 SHA256 `bb77bf8ff25741311d941e42402f19cb6db954fa6eb86f1385d7f3059aafc545`），并接[同场全时相连续几何合同](2026-11-27-new-envelope-full-phase-continuous-geometry-contract.md)。不重做 R650 的定理，不改变当前场、固定度量、32 段 normal 链、完整自由变量、历史地点、帽或已经运行的入口。

完整执行体为 `scripts/resume_20261126/same_field_positive_support_parameter.py`，源码 SHA256 为 `e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991`。依赖只有 Python 标准库；没有 NumPy、Torch 或科学场模块导入。

## 1. 本消费者究竟完成什么

完整输入给定同一准确物理场的全部闭参数盒。每个盒有

$$
a_i\le F_xN_x+F_yN_y,\qquad
b_i\le F_zN_z,\qquad |N|\le w_i,\qquad w_i>0,
$$

其中准确外向未归一法向为 $N=F_\phi\times F_s$。当前有限几何筛中的相反交叉积不能未经改号直接当这个支撑法向。

同时给定同一场的完整标记曲面直径上界 $D_+>0$、完整活动主曲率绝对值上界 $K_A\ge0$、当前固定帽高度下界 $H_-$、帽半径下界 $R_-$以及完整原配方。程序准确定义 $\tau=3D_+/100$，计算两个全局一维有理可行区间，选择一个共同的正有理 $\beta$，再遍历所有盒和完整帽式复核。没有按胞重新选择参数，没有把几个局部最优参数拼成一个几何证明。

消费者自行核的是完整文件字节、同场身份、准确参数矩形的覆盖算术、准确有理区间交和这些输入推出的代数预算。它**不生成也不重新证明**输入的 $F$、六jet、根分支、全阶尾、积分误差、浮点误差、曲率或直径。所有外部包围和全局几何前提必须有自己的完整生产者和证明；记录中出现 `true` 或哈希一致不会使其数学真实性自动成立。

因此报告始终区分：

- `support_parameter_feasible`：完整已声明盒集合通过同一个 $\beta$ 的准确不等式；
- `conditional_R650_numerical_budgets_paid`：再加同场帽和曲率的数值预算；
- `complete_geometry_certified=false`：本程序没有独自支付外部六jet、闭合、浸入、球面拓扑、接缝、对称或所有物理 phase 的证明。

最后一个 `false` 是这个后处理器的正确职责范围，不表示场不满足要求，也不是一个新的求解失败条件。独立的完整证明可以把其已有且已验证的前提与这里的准确代数结果合用。

## 2. 不默认四分之一角域或径向反射

每个准确原参数片默认覆盖整个 $\phi/\pi\in[0,2]$。默认不是旧 carrier 的 quarter 网格，不从有限地址、奇偶标签或相同源文件名推断完整连续对称。

需要使用较小角基本域时，输入必须明确选择 `proved-fundamental-domain`，并提交一个额外的完整、同场、同 source 的延拓证据。其固定声明包括准确基本域及目标整圈、所有角与反射接缝的 $C^2$ 相容、完整参数微分同胚，以及外向单位法向由固定原点、与全部 $A_\beta=\operatorname{diag}(1,1,\beta)$ 交换的正交映射传送。完整证明源文件和实际同场证据文件的全部字节都会核验。代码只核该来源和声明一致性，不冒充证明了这个连续恒等式。

径向只计算一个反射基本片时，必须另选 `proved-radial-fundamental-domain` 并提交独立同场证明，明确所有被省略的原片、准确无限尾、上下反射、core/cap 端口和接缝。角域证明不能替代径向证明。没有这些合法证明时应提供完整原物理片集合；代码不会把几个 cell 的数量相等当作完整径向覆盖。

无论是否使用基本域，`complete_activity_domain_and_seams` 证据始终独立存在。它绑定完整准确 cover，并承担“这些原参数片确实就是完整物理活动域”及接缝的责任。矩形 sweep 只能证明其给定参数域已经覆盖，不能证明省略的物理片不存在。

## 3. 文件和同场身份

顶层输入 schema 为 `complete-same-field-positive-support-input-v1`。CLI 另要求完整输入 SHA256。每个被引用的文件记录都有 `path`、`sha256`、`bytes`；相对路径以该输入 JSON 所在目录为根。程序读取完整实际字节并重算哈希；处理结束再次核所有输入、checkpoint、完整源、证据、证明文件和本执行体。输出必须是与全部输入路径不重合的全新文件。

`field.definition` 的 schema 为 `complete-physical-field-support-binding-v1`，至少包含：

| 字段 | 完整责任 |
|---|---|
| `mathematical_model` / `mathematical_model_identity_sha256` | 完整实际模型对象及其 canonical SHA256 |
| `current_full_point_sha256` | 全部当前自由量的真实完整身份 |
| `checkpoint_sha256` | 实际同场完整 checkpoint 的字节身份 |
| `fixed_metric_identity_sha256` | 固定准确目标的身份 |
| `fixed_material_chart_identity_sha256` | 固定材料图身份 |
| `source_by_role` | 所有实际场和本合同所用生产者的完整 source SHA256 |
| `normal_convention` | 固定字面 `F_phi cross F_s, accurately outward` |
| `fixed_cap_recipe` | 下述完全固定 R661 p4 配方对象 |

`field.identity_sha256` 是整个 definition 的 canonical SHA256。canonical 算法是 `json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8')` 后 SHA256，保持 Python 默认 `ensure_ascii=True`。`source_files` 的完整 role 集合必须与 `source_by_role` 相同，并逐文件核全文哈希；`checkpoint` 必须实际与 definition 中的 SHA 相同。

没有用过去同名场的 K/D/支撑证书，没有因同一个标量 profile 就迁移另一候选的几何。当前点、模型、checkpoint、材料图、固定度量以及物理 source 都由一个共同身份固定。不同批次的外部证据可以有不同 run/attempt，但必须绑定这个完全相同的场。

## 4. 完整 cover 的准确表示与 sweep

`cover.definition.schema` 为 `exact-affine-physical-patch-rectangle-cover-v1`，另有 `cover.identity_sha256`。definition 包含 field 身份、准确正 $S$ 的有理闭盒、全部原片、外向法向约定和固定字面 `box_boundary_convention='all rectangles closed'`。

每个片有唯一 `id`、完整 `mesh_affine`、`exact_parameter_interval_affine`、角域选择及可选的明确径向基本域选择。affine 二元组遵循已刊标量接口顺序：

$$ (\lambda,\eta)\quad\Longleftrightarrow\quad s=\lambda S+\eta. $$

这不是 `(常数,S系数)`，也不是工作 `mesh` 的浮点差。两端与完整 mesh 的首末 affine 节点逐字相同。对每个准确宽度 $(\lambda_1-\lambda_0)S+(\eta_1-\eta_0)$，代码用当前正 $S$ 盒依系数符号取准确下界。若这组输入尚未证明所有宽度严格正，报告不选择完整几何用的 $\beta$；它不宣称真实网格不合法。

每个盒记录自己的原片、原 cell 编号、准确有理闭局部区间 $[u_0,u_1]\subset[0,1]$ 和准确 $[p_0,p_1]$，其中 $p=\phi/\pi$。cell 的物理地址是准确 affine 节点的 $u$ 插值。全部盒 ID 唯一；重叠盒允许，重复 ID 拒绝。

代码按原 cell 独立进行完整二维覆盖检查。它收集所有准确 $u$ 边界作为 sweep 事件，将全部准确角端点压成基本区间，使用整数 range-add/min 树维护活动矩形的覆盖重数。每个相邻 $u$ 事件之间，每个角基本区间的计数必须至少为一。所有矩形是闭的，有限个闭矩形覆盖全部开 strip 后也覆盖其极限边界；因此没有以面积相等替代边界覆盖。初末事件显式为0和1，缺少原 cell 或中间薄缝都会返回真正缺口。

程序不会仅比较 `declared_box_count`。该数目只核数据完整性；实际全覆盖由上述准确 sweep 独立验证。报告保原 cell 总数、完整覆盖数、缺口 cell 数和最多16个准确缺口；所有实际盒仍完整处理，不把公开缺口列表截断解释成剩余不存在。

## 5. 盒文件和外部证据的完整绑定

`support_chunks` 列出全部实际 chunk 的路径、SHA256、字节数。chunk schema 为 `same-field-outward-support-box-chunk-v1`，必须绑定同一 field/cover/实际 support producer source 和法向约定。每个 chunk 保实际公开 Actions 的 repo、run ID、attempt、source commit；声明包围准确并不免除外部验证责任。

每条 `boxes` 记录含：

- `id`、`patch`、`cell`；
- `u_interval` 与 `phi_over_pi_interval` 两对 canonical 有理字符串；
- `a_lower`、`b_lower`、`normal_norm_upper` 三个 canonical 有理字符串；
- 可选 `normal_norm_lower`，仍须是完整向外下界。

只接受准确整数或最简 `n/d` 字符串，不接受十进制 float 充作有理证书。正常上界必须正；若给法向范数下界，它不得超过上界。缺少下界时保 `null`/missing 计数，绝不补0冒真实值。

一个正的逐胞范数下界有助于直接支付浸入，但 R650 只要求真正完整浸入，并不要求以这一特定数值格式证明它。因此独立完整 `closed_sphere_immersion` 证据始终必需；本程序不会因为一组保守范数下界不正，就把一个已有独立有效浸入证明判成原数学命题失败。报告明确区分“这些盒自身已给正下界”与“外部完整浸入前提仍需验证”。

`bounds` 恰有 `D_upper`、`K_A_upper`、`H_lower`、`R_lower` 四个准确有理值。其来源不是一个未经核对的 summary 标签，而是以下完整证据。每个 `evidence` 条目有 `producer_source_role`、完整 `certificate` 文件记录和非空 `proof_sources` 完整文件列表。

证据文件 schema 为 `same-field-complete-bound-evidence-v1`，包含对应 role、同一 field SHA、实际 producer SHA、完整固定 `claim`、按顺序的 proof source SHA/字节数、`complete=true`、真正整数 `remaining_responsibilities=0` 和实际公开 Actions provenance。代码核全部实际字节并核声明，不能把“当前没有完整证据”改写为零剩余。

所有固定必需角色为：

| 角色 | claim 的明确内容 |
|---|---|
| `current_field_binding` | 当前完整点、checkpoint、完整数学模型三身份 |
| `physical_six_jets` | 同 cover、同 support producer、**全部 chunk SHA/字节顺序**；真实当前 lift 与所有根、标量、积分、节点、舍入、算术费用均已包含 |
| `complete_activity_domain_and_seams` | 完整原径向片、全部准确尾、全部物理接缝 $C^2$，并绑定 cover SHA |
| `closed_sphere_immersion` | 完整标记闭合连通 $C^2$ 球面浸入、实际活动/帽/cuff相接 |
| `all_physical_phases` | 固定原点 z轴，活动旋转、帽固定，准确 $S_\alpha=R_\alpha A\cup C$ 全相位公式 |
| `diameter_bound` | 当前 $D_+$，范围为全部物理 phase 的完整标记曲面 |
| `activity_curvature_bound` | 当前 $K_A$，完整准确 base-phase 活动域及全部尾 |
| `fixed_cap_parameters` | 当前 $H_-,R_-$、固定配方 SHA、物理高度沿 phase 固定、own induced cap metric 与 $C^2$ 接合 |

实际 `claim` 的精确键名和字面在源码 `read_input` 的完整 `claims` 对象中保留；角/径向基本域还分别增加 `validate_cover` 中的完整动态 claim。外部生产者必须输出这些真实声明及完整来源，不能拿其他 scope 的旧报告改 schema。这一输入合同目前尚无实际数据，不声称现有六jet入口已在生成它。

## 6. 固定 p4 帽的边界

源码 `CAP_RECIPE` 固定 R661 的高 $1/1000$、中心尺度 $3/20$、四半径 $1/25,9/200,1/20,11/200$，上三个中心 $(3/20,0),(0,3/20),(-3/20,0)$，下中心 $(0,0)$，以及完整四次图和外向方向。配方必须与当前定义逐项相同。

本程序只复用已经证明的

$$r_b=1/5,\quad L_b=1/20,\quad g_b=1/100,\quad d_b=801/800,\quad K_C\le5.$$

它检查 $R_-\ge1/5$ 以容纳这组支撑盘，并保当前 $H_-$。这些数值不是当前新场的嵌入、闭合、度量或幅度证书；cap metric、接缝和真实场身份仍由独立证据承担。如果换帽配方，不应放宽此 source 的比较，而应给准确新计算和明确新消费者。

## 7. 闭可行与严格超额分开

两个闭可行集合准确为原接口式(5)–(6)。`RationalInterval.impose` 分别处理 $r\beta\ge s$ 的正、负、零系数。负系数给上界，零系数不除法；$r=0,s>0$直接矛盾。端点保开闭性；$\beta>0$ 本来就是开边界。

同一批完整输入另算两个“每个支撑目标均有严格超额”的区间，对应 $r\beta>s$。这不是 R650 新要求。零系数在严格版只有 $s<0$ 才可行；$s=0$ 使严格区间为空，但闭区间仍可合法。

选择策略完全确定：优先使用非空严格区间，若其中1可行先选1；否则选第一个非空分支的有理内部点。两个有限不同端点取中点，无上界时取下界加1；闭 singleton 取其唯一端点。若没有严格区间，照同样规则在闭可行区间选择。最终只输出**一个共同参数**，不声称所有可行参数只有一个。

接着第二遍对每个实际盒及完整帽核

$$ a_i+\beta b_i-\tau\max(1,\beta)w_i\ge0,$$
$$ \beta H_- -g_b-\tau\max(1,\beta)d_b\ge0.$$

右侧目标严格正，所以分子确实为正，使用 $w_i$、$d_b$ 上界作为除数的方向合法。计算完整

$$\sigma_- = \min\left\{\min_i\frac{a_i+\beta b_i}{w_i},\frac{\beta H_- -g_b}{d_b}\right\}.$$

`support_excess_over_target` 是 $\sigma_- -\tau\max(1,\beta)$，可以准确等于0。闭 singleton、零 slack、或 $\max(K_A,5)\tau=1$ 都没有被误判为 reach $\ge\tau$ 失败。严格正的支撑本身仍由 $\sigma_-\ge\tau\max(1,\beta)>0$ 保证。严格超额仅单独报告，有利于后续稳定裕量，不被添加到 README 完成标准。

若闭可行集均空，结论只针对给定保守包围和这族充分条件，不是几何不嵌入或课题无解。若覆盖不全或物理宽度尚未付，程序保完整缺口而不从部分盒选一个冒全域的参数。

## 8. 执行、失败与公开结果

真实输入准备好后，完整 Actions 命令形式为：

```bash
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/same_field_positive_support_parameter.py \
  --input /actual-runner/path/complete-support-input.json \
  --expected-input-sha256 ACTUAL_COMPLETE_INPUT_SHA256 \
  --output /actual-runner/path/fresh-support-parameter-report.json
```

上面是待实际输入的参数形式，`ACTUAL_COMPLETE_INPUT_SHA256` 不是预填数据，当前没有排科学运行。`require_actions` 要求 `GITHUB_ACTIONS=true` 且 public repo 精确为 `Rogerhu12/math-research-public`。本地只做源码 AST/compile，不导入执行本文件，不用人工有理算例造通过报告。

结构不合、缺真实证据、文件字节变化、跨场身份或源错配会明确异常退出，不输出伪装的几何失败结论。合法但没有足够全域覆盖、参数不可行、帽预算未付或曲率预算不足，会完整输出 `not-paid` 或相应 scope；成功完成后处理与达到题目完成标准始终不同。

输出不复制全部盒或可重算 raw。保全部 chunk SHA/字节/实际 run、完整源身份、证据 SHA与固定 claim、cover责任计数、两个严格/闭区间的准确端点和有限矛盾见证、单一参数、$\sigma_-$、所有最小余量和对应盒 ID。stdout 是严格 scalar-only 紧凑 summary，可供现公开控制器读取；完整 result 仍留 runner。

完整 R650 结论还须将这些准确代数预算与外部已经真实支付的全局前提合用。此入口不提前声称新候选已付任何 $A_2$、非全等、held、握持、固定度量误差或全 refinement 责任，也不阻挡当前完整真实方向继续运行。

## 9. 两项完整绑定修订与原数学体保持

本版独立修订原未运行源码 `237e7f3518288fdcf4646f30a35a2a974c4a342f42f1f493536a1f439a627c2c`。原源码与说明原字仍保留；没有科学失败或数值结果被改写。根代理完整源码复核发现并要求修正两项真实绑定缺口：

第一，角或径向基本域的动态 evidence role 不能与8个必需全局角色同名。合并前明确检查两个 role 集合交集，任何碰撞直接拒绝。因此不能用名为 `physical_six_jets` 的基本域声明覆盖原完整物理六jet证据，也不能用减域证明顶替闭合、浸入、全phase或直径/曲率责任。

第二，所有读取过的绝对实际路径使用统一 `bind_used_record`。同一路径再次出现时，标准化的完整 path/SHA256/bytes 记录必须与首次记录完全一致，否则立即拒绝；不能以较晚版本覆盖较早绑定后，只在结束时检查最后版本。执行体自身加入最终重核集合也走同一个守卫，不能覆盖它此前作为 source/proof 被绑定的另一版本。

实际纯源码对照显示，除 `verified_bytes`、`read_input`、`main` 这三处 metadata 接线与新增的统一记录守卫外，所有原 top-level 函数/类 AST 完全相同。两个有理区间、闭/严格边界、sweep、全局选择、逐盒第二遍、R650条件预算和全部科学范围未改。实际只做 AST/compile、重复字面字典键及尾空白检查，没有导入本执行体、科学输入、区间算例或 root/field 计算。

## 10. root 完整复核范围

root 全文读取完整执行体与本说明；首轮显示截断的中段另按明确行段完整补读，没有以截断输出声称全文审完。按完整源码核了负/零系数、闭 singleton、覆盖 sweep 的事件顺序和闭边界、全局唯一所选参数与第二遍余量、外部证据同场身份和只给条件代数结论的范围。没有执行这些有理算法或输入科学样本。

复核发现的两项 metadata 缺口已按第9节实际修订。root 对原稿与 revision2 作完整 AST 差异核对：仅三处接线变化和一个新增路径守卫，另22个原顶层函数/类保持完全相同；包括全部区间、覆盖和科学不等式。AST/compile 已实际通过，未导入本模块、运行 Fraction fixture、构造当前场盒或生成任何数值证书。

完整源码现在可由公开 Actions 按真实输入调用；当前缺同场完整准确六jet/域/几何证明输入，所以没有虚构 ready 参数、候选参数或科学任务。它不影响已运行的求解方向，后续将以真实完整输入消费并把实际返回另列。
