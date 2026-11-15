# 真九控制冻结450：连续 scalar 与同场相对 metric 的独立适配

作者：ChatGPT /root/geometry（GPT-6 Astra Pro，AI-assisted）；主控完整读取并发布。日期：2026-11-15。分类：完整数学接口及可执行源码适配。

## 1. 本次支付的具体责任

本接口把实际被原入口接受的 `nine-control-all-frozen-same-metric450-complete-physical-DN-v2` 场接到已有同场连续 metric 消费器。九个系数全部冻结，原338个物理状态、450个完整状态、112个 core/tail 模式、全均值、唯一 SE(2)、shared-B、完整材料切口及两帽保留。没有实际 accepted450 场输入，没有实际连续 E 查询结果，也没有运行本组件；本文不填任何实际场 SHA、阈值通过、reach、held 或任务完成值。

新增运行文件是：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261115_nine450_scalar_interval.py` | 16807 | `0c4353d18f1b6b2290cac6907c26a78f04d17909b3a9c83aeac696f29a44f6a0` |
| `geometry_20261115_nine450_shared_field_relative_metric.py` | 44796 | `4b13425a34d8de2d168632fa0c24474542257e51fb60c2ed5a0b8501beadc975` |

旧 a601 入口、九450生产者、原 shared-B 内核、原九 scalar 家族和 R286 生产者均没有改写。新的完整指标结论使用自己的 schema；不把九控制字段改标签交给旧 v3/v4 reader。

与旧 a601 相比，实质新增三处接线：

1. 明确把真实 `FrozenNineProfile.designed_nine` 和 `frozen_design_scalar_profile` 接到0865已经实现的完整九 scalar 解释器；空 active 向量不等于九个几何系数为零。
2. 用69bb的 `load_shared_bundle` 读取真实新 guard 与完整七元组，保留已绑定的实际场；旧 active 数学内核只负责同一七元组的准确有限表达及六 jet。
3. 实际消费9aa0生成的 R286 模型 C 的闭径向查询包围，显式支付当前场 radial domain 与自然外半径的包含责任；保留原两个固定帽的同图 target，局部相对误差仍恒为零。

这不是新 native 验收器，也不改变原 RMS、BC、容差、回溯、迭代或同 $g$ 精化条件。

## 2. 冻结依赖与真实入口

下列源字节在本次源码核中直接读取，运行时再次核定。薄适配只调用这些既有定义，不生成替代原式。

| 定义或接口 | SHA256 |
|---|---|
| 九控制完整 family / ScalarExpression | `086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629` |
| 九450 v2 scalar profile | `5e95afdb82f83a276003e6a4846e20893b7eb7f2b44b309d56950f11dbfaa0d3` |
| 九450 v2完整原 full-DN入口 | `92cfb0701824df770dfcd009a623e84695e72fe9c489d70537d8983415adc7e8` |
| 九450 SavedPrefix | `e8deb4136dbaf021d2648e02a2cdb774db4ebe1836b239b609472c596fc70404` |
| 九450 shared closed dispatcher | `69bbba2647b2356f2c4023c74a938e29d1b93effcb1c99385fdaa73b78b9d17d` |
| 原 a601 relative metric 内核 | `a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17` |
| 完整准确 finite field / 六 jet | `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` |
| 原两固定帽 graph 定义 | `a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e` |
| 原有限 Gauss scalar/Taylor-Bernstein 内核 | `a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703` |
| 原严格 cell/Arb primitive | `1774f8da00ccd8ced6199e85d1fda6f455a224eed7d20d1a92ac04df3801e2ce` |
| R286原冻结数据连续 E 生产者 | `9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed` |
| R286完整证明 | `81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb` |

`checked_runtime` 在科学 imports 前要求 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。它核定当前源码与全部继承闭包；family、profile、原 prefix、SavedPrefix/dispatcher 各自已冻结的完整依赖仍由自己的检查函数保留。没有把 parent producer 的 closure 增补成另一个 producer 身份。

新七元组入口精确为：

```text
geometry_20261115_nine_control_shared_closed_dispatch.load_shared_bundle(args)
-> (paths, plan, assembly, table, saved, A, binding)
```

它原样执行实际450接受来源、原 native 全 tail/config/H/J/cut、单次配准与新 guard 的合同。`M.initialise_runtime` 仍初始化原数值辅助类，但其返回的旧 loader 被命名为 `unused_legacy_loader`，没有用于读取当前场。

## 3. 同一个九 scalar 对象，而非旧三参数标签

### 3.1 完整定义

令原三个支撑宽度为原字面 $w_i>0$，左端为 $\ell_i$；即使记录中的 `right` 与实数 $\ell_i+w_i$ 有舍入差异，数学支撑仍依原公式使用后者。设

$$
x_i=(s-\ell_i)/w_i,\qquad P(x)=64x^3(1-x)^3,\qquad t_i=2x_i-1,
$$

并令 $b_i(s)=w_i^2P(x_i)$ 在 $0<x_i<1$ 成立，在支撑外及两端取零。全九实函数为

$$
a_9(s)=a_3(s;p_1,p_2,p_3)
 +\sum_{i=1}^3\theta_i b_i(s)t_i
 +\sum_{i=1}^3\eta_i b_i(s)t_i^2.
$$

$a_3$ 是嵌套 `original_three_parameter_specification` 对应的完整原三参数实表达，包含原精确 Hermite scalar 首段、原 turn 的48个 Gauss节点/权重、原 bridge 的64个节点/权重、全部 phase/mask/clip、coast 和实际存储构造常数。它不是重新拟合的 scalar，不把独立返回的 `ap/app` 当作有限 Gauss 半径的解析导数。

本适配直接调用0865的 `export_scalar_descriptor` 与 `ScalarExpression`。它核9个系数的完整 binary64 字词、9个 `(left,right,stored_width)` 字词、冻结 canonical scalar identity、原 nested spec 和原有限求和合同。原冻结对象的 `bumps=[]` 只说明当前无自由 active 参数；真正九个物理支撑从 `designed_nine.bumps` 取得。

### 3.2 真导数与分支

在任一不跨原分支或支撑端点的区间，所有函数均是明确解析表达。若把一个支撑的贡献写为 $w_i^2P(x_i)q_i(t_i)$，其中 $q_i(t)=p_i+\theta_i t+\eta_i t^2$，则真正导数是

$$
\frac{d}{ds}\{w_i^2P(x_i)q_i(t_i)\}
=w_i\{P'(x_i)q_i(t_i)+2P(x_i)q_i'(t_i)\},
$$

$$
\frac{d^2}{ds^2}\{w_i^2P(x_i)q_i(t_i)\}
=P''(x_i)q_i(t_i)+4P'(x_i)q_i'(t_i)+4P(x_i)q_i''(t_i).
$$

$P$ 在两端至少三阶消失，因此这些新增 polynomial controls 各自的0/1/2阶端点 jet 为零。这个事实没有支付原 finite-Gauss base 不同 masks、rounded 接口常数之间的全局 $C^2$ 兼容。

`branch_derivative_enclosure(left,right)` 在真实分支上用 `arb_series` 对上述完整实函数求导；它只返回该分支延拓的 value/first/second 包围。它不声称跨端点导数存在。`envelope` 复用 a9a 的 Taylor/Bernstein 机制，由本对象的 `value` 和 `exact_degree` 动态参与：even/odd/quadratic 的最高新增多项式次数分别是6/7/8。没有调用原 `returned_ap` 代替解析导数。

实际 metric cell 使用 a601 的 `closed_scalar_range`：先按完整 breakpoints 切开，在内部按真正选中的分支求区间值，再合并两个闭端点各自按原 mask 选出的实际值。因此不假定两个相邻分支在 rounded 接口处相等。两条一次 source 支撑边界同时保留：记录的 `right` 和原公式的 `left+stored_width`。

### 3.3 三种对象明确区分

v2原 point 路径先形成冻结 added-shape base，再以原 `control_jets @ p` 加 even 项；batch 路径用原 `einsum`。设计 family 原点求值的加法顺序不同。九项在实数中交换求和相同，不推出 binary64 点/批运算逐位相同。

新的 descriptor 同时保：

- 完整九控制实表达与来源；
- v2 原 point/batch 路径合同及原 zero-skip；
- 实际重建时复制的全部原有限 Gauss 构造常数；
- 可选的实际 live-profile sidecar 来源。

默认从 accepted checkpoint 重建的 descriptor，明确 `actual_live_runtime_constants_verified=false`。本版即使外部JSON声称 `origin=actual-live-profile`，且 checkpointSHA、exporterSHA与数学表达全部匹配，也只记录 `supplied_descriptor_declares_matching_live_provenance=true`，不会把历史现场来源提升为已验证。`actual_live_runtime_constants_verified` 在本版始终为false，完整 prefix数学计算不因此停下。

可执行现场API已经存在：

```python
# 只能在未来真实450运行仍持有其实际profile对象时调用；这里不执行。
runtime = scalar_adapter.checked_runtime(code_directory)
sidecar = scalar_adapter.export_scalar_descriptor(
    runtime, actual_live_frozen_profile, actual_live_frozen_profile.specification,
    checkpoint_sha256=actual_completed_checkpoint_sha256,
    origin="actual-live-profile")
```

参数必须是该次实际运行的live对象，不能重新调用重建器后改一个origin。当前冻结92cf入口没有调用这个新API，也没有在其实际完成记录中绑定该sidecar。未来若要支付历史live来源，须在新的独立producer或可逆薄hook中、原profile仍活着时导出，完成记录明确绑定该调用源码、实际checkpoint、sidecar字节SHA及canonical scalar身份。可以先写checkpoint、再输出绑定checkpoint的sidecar、最后另写完成事件，从而不产生自引用hash。仅这段调用模板或外部JSON标签都不是该事件已经发生的证据。

本版的导出字段还明确 `origin_is_caller_declaration=true` 与 `actual_live_execution_attested_by_this_exporter=false`；消费者不认证不存在的现场事件。没有 actual450 或 live记录时，原 source-only范围保持。此来源缺口不是暂停 metric运算的额外门：仍可证明当前完整重建实表达的界，但不冒已认证了历史浮点求值。

## 4. 同场准确有限 $F$ 及完整拉回

实际场完全复用675ab `ExactFiniteField`，不调用浮点 renderer 的 `.jets()` 标签作为导数。其全部 prefix物理 nodal值、一阶/二阶保存系数被当作真正 Hermite多项式的系数；其后对所得多项式和三角表达真正求导。

保留的内容包括：全部112 core；全部338物理分量与 $z_0$；全部 native径向节点；每个实际 FFT节点从零频到 Nyquist 的完整复系数字；同一 shared-B 实 Hermite 多项式；同一唯一 SE(2)；整个 cut 的0/1/2阶差补丁；上/下完整反射片。节点字节不能无损表示为原 complex128 时沿旧入口明确报错，不假定额外精度已经被保留。

以 $q=\phi/(2\pi)\in[0,1]$ 为计算角坐标。原完整材料角是

$$
\theta=\Phi(\phi)=\phi+\sum_{m=1}^{112}
 \frac{(1-4m^2)c_m}{2m}\sin(2m\phi),
$$

$$
\theta_q=2\pi\left(1+\sum_{m=1}^{112}(1-4m^2)c_m\cos(2m\phi)\right)>0.
$$

正下界取原 SavedPrefix 的完整 R237 密度证据与当前区间包围的交集；不是新增任意正 floor。prefix按物理 $\phi$ 表达，native/collar通过 $\Phi(\phi)$ 作真正复合。六个 jet 槽是

$$
F,\ F_u,\ F_q,\ F_{uu},\ F_{uq},\ F_{qq}.
$$

因此自动保留 $U_{\theta\theta}(\theta_q)^2+U_\theta\theta_{qq}$ 及 $U_{r\theta}\theta_q$ 等混合项。完整 cut差亦如此。有限 $\theta$ 频带经过 $\Phi$ 复合通常没有相同的有限 $\phi$ 频带；代码不作这种截断，也不把 prefix的有限 $\phi$ 展开冒充材料角有限展开。

## 5. 实际9aa0连续 E 输出的接入

### 5.1 独立、显式的目标选择

CLI选择串固定为：

```text
R286-convention-C-all-original-exact-root-sequences
```

它表示采用 R286 **额外明示的约定 C**，在同一原冻结参数、浅部160个 calibration行、原 frozen warp系数和全部原片式基础上形成连续实积分对象。深部保全部满足原精确校准方程且位于 $[1/2,2]$ 的根序列；当前界对每个这样序列同时成立。没有静默挑某个未知根，也不把另一个 R26数值证书或旧48步 selector 输出替换过来。

这是目标模型层的明示选择。原已接受450有限场仍原字节；不能由此宣称它已是该连续目标的认证解，或连续对象已经由旧有限代码唯一指定。具体比较的是这个真实有限 $F$ 与声明的 $g_C$。

### 5.2 必需实际输出及身份

传入一个真实 `--continuous-e-result` 与该文件实际 SHA，程序沿其 descriptor 完整读取：

| 原件 | 来源与用途 |
|---|---|
| `result.json` | 9aa0实际source、run/source commit、完整head/根存在/接点条件、自然 $R_{out}$、未付suffix |
| `input-binding.json` | 实际config、两ready、原源码、R286证明、全部原参数、160行、frozen warp、source fingerprints、约定 C |
| `query-plan.json` | 全部原请求，绑定该 input-binding，保实际闭端点与原查询顺序 |
| `query-results.json` | 所有实际返回 query及未访后缀、每个完整包围的原 exact dyadic端点 |

同一报告中其余 source/primitive/inverse/unpaid ledgers 的原 descriptor完整保留在新结果，但本消费者不把它们再次全部读取或重算，也不声称本地审过其 payload。科学意义来自实际 pinned9aa0运行所输出的范围及 R286证明，不来自 JSON schema本身。新组件不是重新执行 producer 的独立区间审计器。

同时核当前实际场 config与 producer physical_parameters的原 geometry字段、同 `profile_fingerprint`、原 source revision、原背景输出 source SHA、实际 cuff、原 frozen warp全字词。当前完整场、complete scalar、材料 core和 source table身份另入 `field_tail_identity`。不会因为某个 filename类似就认同同 $g$。

### 5.3 自然外半径与局部可用范围

令 producer证明的自然半径为

$$
R_{out}\in[L_R,U_R].
$$

它不是强制等于原 binary `rCut` 的另一个名字。若报告含完整 `whole-natural-domain` 查询，则其 $E$ 包围可保守用于当前场的

$$
[r_{cuff},\min(r_{cut}^{F},L_R)].
$$

如果当前场的 cut落在 $(L_R,U_R]$，上端包含关系仍未证；如果 cut超过 $U_R$，报告明确其超出已证自然定义域。都不重选 warp、不压缩径向坐标、不改 cut、不延拓一个未定义目标。当前metric格只在实际有效闭 query区间的并覆盖内被支付，其他格返回未付。

对于实际 `closed-rational-radius-interval` 查询，保持其原exact左右端点和 domain证明。任一 query的实际 `complete_closed_domain_bound` 与连续model-family条件已证，便可使用其保守包围。`work_resolution_complete=false` 可能只是希望得到更窄包围的工作预算未付；不把它加作数学有效性的额外门。反之，未访query、source未完成、原根存在/保护端兼容未证或整个query域未证，不能当作已付范围。

所有有效query都保原顺序记录，再按它们的有效径向区间组装目标覆盖。相邻闭区间允许共享端点；未覆盖的真实间隙不能被省略。重叠query的界取保守并包，而不根据中心点切换。$E_C=1+w_C^2\ge1$ 的解析事实用于与原输出包围相交；它不是样本推断。

目前132尚没有在此接入一个实际完成结果；本接口没有预先填写任何可用 query或自然cut包含结论。

## 6. 四个原 Loewner 测试及其完整理由

令同一格上的几何 Gram阵为

$$
G=\begin{pmatrix}E&B\\B&C\end{pmatrix}
=\begin{pmatrix}F_u\cdot F_u&F_u\cdot F_q\\F_u\cdot F_q&F_q\cdot F_q\end{pmatrix}.
$$

在 prefix取

$$
g=\operatorname{diag}(1,a_9(s)^2\theta_q^2),
$$

在 collar/native取

$$
g_C=\operatorname{diag}(E_C(r),r^2\theta_q^2).
$$

这都是同一材料目标在实际 $(u,q)$ 图中的拉回，绝不使用 $1+B'(r)^2$ 代替原声明目标。

设对角元素的严格正上下界满足 $0<\ell_i\le g_{ii}\le u_i$，请求的原相对误差为 $0<\varepsilon<1$。构造

$$
P=(1+\varepsilon)\operatorname{diag}(\ell_1,\ell_2)-G,
\qquad N=G-(1-\varepsilon)\operatorname{diag}(u_1,u_2).
$$

逐格保持原四个严格下界：

$$
P_{11}>0,\quad\det P>0,\quad N_{11}>0,\quad\det N>0.
$$

二阶对称阵的首顺序主子式判据给 $P,N\succ0$。又因

$$
(1+\varepsilon)g-G\succeq P,\qquad
G-(1-\varepsilon)g\succeq N,
$$

可得

$$
-\varepsilon I\prec g^{-1/2}(G-g)g^{-1/2}\prec\varepsilon I.
$$

因此相对算子范数严格小于 $\varepsilon$。正则坐标改变下该广义特征值/相对算子结论不变，故使用真实材料拉回是充分的。四个区间下界没有全部严格为正只表示当前包围未支付；不会被解释为该点或整场的反例。对角目标正下界未证时同样只保未付。

代码直接调用 a601的 `angle_density`、`loewner_certificate`、`closed_scalar_range`，没有修改上述式子或改用分量最大值。prefix与tail每次完整保存同场六 jet和目标来源。

## 7. 两个原固定帽为何仍是误差零

原帽定义为完整闭 Cartesian圆盘上的

$$
F_+(x,y)=(x,y,H+b_+(x,y)),\qquad
F_-(x,y)=(x,y,-H-b_-(x,y)),
$$

$$
b_\pm(x,y)=\sum_{j\in\text{该帽}}A_j
\max\left(0,1-\frac{|(x,y)-c_j|^2}{R_j^2}\right)^4.
$$

同一原 R14/R248 target正是 $I+Db_\pm\otimes Db_\pm$。故该图的诱导 metric与 target完全一致；反射不改变 Gram阵，$H$ 的任意原有限值也不改变导数。整闭disk包括极点及cuff边界，局部算子误差恒为零，不需要角向采样。

旧 a3ada读取器有意只接受旧 ac635 wrapper；直接给它69bb的真实新guard会被拒绝。本次独立 `cap_identity_for_nine450` 核新的 shared schema、69bbwrapper、实际loader名、未变ac635内核、完整450field identity、plan/assembly/source哈希、原H/cuff与所有marker，然后通过窄 `bind_geometry` 接口复用原 a601帽target数学消费者。原输入文件、guard和旧 a3ada模块一字不改，不构造冒名的旧plan。

该局部零误差不证明两帽分离、全曲面嵌入、帽与活动片的 $C^2$ 接合、target在cuff的全atlas兼容、reach或held。原marker支撑是否严格在自帽内部也按实际原数记录，而不是从schema默认为真。

## 8. 全闭格、资源部分结果与全相位范围

根分区复用原a601的准确规则：两张完整反射片；每个原 prefix span、collar/native span、shared-B节点、cut_patch边界、全部scalar/mask/support端点和实际target query端点；完整 $q\in[0,1]$，两圈闭端点都保留。没有固定最多128个坏格或仅取每坏格几个children的截断。

每次四分子格仍是原完整四个闭矩形。显式预算或异常结束时保存：当前root的完整剩余DFS stack、所有未访root的准确rank后缀、不可变全root计划、已访问每个terminal格及全部未付原因。旧完整DFS循环在 source-only AST比对中，除新 target参数及进度标签外相同。没有把未遍历空间视为已付。

`completed=true` 表示分区遍历完成，不表示各格已认证。证明chartwise整片界还要求所有terminal格支付。原cap恒等责任单独列明。全局标准4、实际 $C^2$ seams、原target atlas兼容、浮点renderer到准确表达的误差桥，始终不能由 `completed` 推出。

沿原 R248的已证实际family合同，活动材料图的相位是 $R_\alpha F_0(u,\theta-\alpha)$。全角界可经参数平移与刚体旋转传递；固定帽target仍同图误差零。但这只在真实完整family接合及其目标atlas兼容责任已付后才能组成全闭面结论。本适配保留该条件范围，不从一个phase0包围自动生成全场 $C^2$/reach证书。

## 9. CLI与原文件依赖

两运行件必须与本次明确的冻结依赖放在同一个实际 `--code-directory`。所有科学只在公开Actions。标准依赖为原 NumPy 和 `python-flint==0.9.0`；不需要新的数据库、网络或新求解器。

### 9.1 只导出当前重建 scalar descriptor

```bash
python computations/geometry_20261115_nine450_scalar_interval.py \
  --checkpoint "$ACTUAL_ACCEPTED450" \
  --code-directory computations \
  --out "$RUNNER_TEMP/nine450-current-real-scalar.json"
```

这会执行原SavedPrefix恢复和表达复制，并明确是重建sidecar；它不伪造实际 live provenance。

### 9.2 完整 metric组件

```bash
python computations/geometry_20261115_nine450_shared_field_relative_metric.py \
  --directory "$ACTUAL_NINE_SHARED_DIRECTORY" \
  --source-directory "$ACTUAL_NINE_ORIGINAL_CLOSED_DIRECTORY" \
  --descriptor "$ACTUAL_SHARED_B_DESCRIPTOR" \
  --checkpoint "$ACTUAL_ACCEPTED450" \
  --port "$ACTUAL_COMPLETE_PORT" \
  --config "$ACTUAL_ORIGINAL_CONFIG" \
  --tail-response "$ACTUAL_COMPLETE_NATIVE_RESPONSE" \
  --complete "$ACTUAL_COMPLETE_TAIL_READOUT" \
  --source-topic "$RESTORED_ORIGINAL78_TOPIC" \
  --continuous-e-result "$ACTUAL_R286_RESULT" \
  --continuous-e-result-sha256 "$ACTUAL_R286_RESULT_SHA256" \
  --tail-model-choice R286-convention-C-all-original-exact-root-sequences \
  --eta "$EXPLICIT_REQUESTED_RELATIVE_ERROR" \
  --precision-bits 192 --initial-angular-depth 3 --max-depth 10 \
  --max-visited-cells 1000000 --budget-seconds 3600 \
  --out "$RUNNER_TEMP/nine450-metric"
```

参数变量全部指未来真实原件；这里没有实际producer/run/SHA占位值冒身份。`--eta`必须明确给定，本接口没有选择实际未来阈值。

`--basename`与`--source-basename`默认均为`surface`，对应原五件plan/assembly/phase0mesh/background/normals路径。原closed loader所要求的全部native分块、config、源恢复及原原件仍必须齐全；本接口没有改成仅sample mesh或summary可代全场。

可选 `--scalar-descriptor` 与 SHA成对提供，核完整表达匹配并保原供给来源声明；本版不会仅凭声明认证实际live构造事件。可省略连续E两参数，此时prefix/帽仍按真实表达处理，但所有tail格明确未付，绝不取reference table的点值补作连续界。提供E文件却不显式选择模型C会报输入身份错；这只是防止改标签，不是新的数学验收条件。

### 9.3 schema与临时输出

| 对象 | schema或文件 |
|---|---|
| scalar适配 | `frozen-nine450-exact-real-scalar-interval-adapter-v1` |
| 完整scalar descriptor | `frozen-nine450-complete-scalar-real-expression-v1` |
| metric结果 | `frozen-nine450-shared-field-R251-relative-metric-model-C-v1` |
| 输入 | `large-arrays/input-binding.json` |
| 全field表达 | `large-arrays/same-exact-finite-field-expression.json` |
| 全scalar表达 | `large-arrays/same-scalar-expression.json` |
| 显式tail目标责任 | `large-arrays/required-original-tail-target-identity.json` |
| 原帽定义 | `large-arrays/original-fixed-cap-target-identity.json` |
| 全root计划 | `large-arrays/planned-closed-roots.json` |
| 逐格完整journal | `large-arrays/relative-metric-cells.jsonl.gz` |
| 完整已访/未访责任 | `large-arrays/coverage-and-pending.json` |
| 主结果 | `result.json` |

结果分别给 complete-prefix、实际live scalar来源声明及未付事件、完整active chartwise界、两帽0、连续模型C查询实际情况、自然cut包含、原未访/分辨率未付，以及 global seams/standard4始终未由本组件自动支付的标志。原计算exception单独记录；预算或不够强的区间界不是native科学拒绝。

Rule15下这些详细数组/逐格数据只在请求自有临时目录生成。之后公开工作流应读取真实紧凑结果/未付范围与文件SHA，再清理自己的临时输出；本次不创建workflow、不上传raw，也不预造一个可执行的实际场请求。

## 10. 官方 Acb/Arb API核实与静态范围

本次重新读取 python-flint **0.9.0官方文档**：

- [Acb integration与sqrt](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral)：`acb.integral` 接收 `(x,analytic)` callback；非解析区域须返回非有限包围，带branch-cut的sqrt须传递analytic标志。
- [Arb构造、lower与man_exp](https://python-flint.readthedocs.io/en/latest/arb.html)：tuple表示二进制mantissa/exponent；lower/upper给向外舍入的exact端点，`man_exp`要求exact finite输入。

9aa0使用两参callback，原sqrt传递analytic，端点先lower/upper再man_exp。新消费者只用保存的mantissa/exponent重建有理端点，不解析display字符串。此为官方接口源核，不是本地import、数值实验或对任何实际积分成功的声明。

静态检查记录 `nine450-metric-source-only-check.json`：5516B / `ce7836d34815eb23433aadd68524ace4a3ccfca5f9bc4a389548210c76dca058`。内容包括两源AST/compile、完整直接pins、原完整DFS AST同一性、原数学helper AST身份、九value直接委托、无顶层NumPy/flint/scipy import及未执行科学标志。

相对旧a601完整diff `nine450-metric-versus-a601.diff`：61700B / `f7c60d6245a421af7dc274b6ed64d43716ef7b0a2edadfe3560193b2173a40a7`。检查脚本仅解析源码，没有导入任何新组件或构造场。

本次没有实际 accepted450、实际query、实际metric值、有效误差阈值通过或失败、连续全场成功等数值。所付的是已有准确表达的真实接口与完整责任接线；已冻结科学源、原验收和原未付责任均保持。
