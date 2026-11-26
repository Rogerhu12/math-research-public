# v5 最终 actual 设计场到固定问题精化：现有源码的窄缺口

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

这是源码/坐标接口核查，不是新精化执行或存在性结论。已读
`notes/2026-11-26-actual-dn-refinement-entry.md` 及对应 model、step、acceptance、
compare、pipeline 五源。没有运行 BVP、DN 或改在跑文件。R63/R69 不重证。

## 现入口不能直接接 v5

`warm_actual_dn_refine_model.py` 的 accepted_input 只认既有 warm actual 与
actual-refinement 两个 KIND，provider.VERSIONS 仅列 v2/v3。
geometry_spec/require_same_problem 固定 mean1168、qaux 第0坐标。
step 和 acceptance 还调用 `warm_true_dn_solve.validate_warm_source`，要求
真实已接受 λ=1 warm 线性锚，并将 frozen_profile 与该锚逐项绑定。

v5 在真正 full-DN 阶段仍允许 δ 设计，最终 actual δ 可以不同于其线性输入。
因此即使最终 M24、mean1168，也不能只追加 KIND 或改贴 v3/v4 标记。
原 v4 model 还绑定早先 v3 零控制锚的 g；它的严格 validator 不能冒充
“从一个新 actual δ 冻结”的来源检查。几何 baseline 与最终选定的 g 必须
分开记来源，同时都保持不可漂移。

## 最小同 M 坐标传递

输入首先必须是真 λ=1、完整未缩 H/J/audit、原最多八次外迭代及全部 finite 门
通过的 v5 **实际设计**场，绑定 raw/physical/full-H/全部 shooting states、
config、native manifest、Python/core/provider 及其间接依赖。零锚、metric-only、
小 factor 尾或原线性场均不满足这个前提。

令原 raw 参数为 p。冻结
`delta_star = source.physical_profile.delta + p[0]`，核其逐字等于最终
`source.frozen_profile.delta`，并将整个最终 frozen_profile 作为新 cfg。
新固定问题的初始参数是

\[
\widetilde p_0=0,\qquad \widetilde p_j=p_j\quad(j\ge1).
\]

保留原 raw x/Y/cubic、physical x/c、gauge、warp、全部角图与原 literal
chart_join/chart_reference_prefix/chart_breaks；不能让 fixed=True 构造器
默认重新选径向 reference。只在新参数数组中作上述重编码，旧 artifact 不改写。

用同一个**未屏蔽首列的完整 R70 factory**，保完整旧 R53 baseline、窗口、
λ=1、phase_scale 和所有非零高相位。可传实际旧 core.baseline 以保字面对象；
不得重拟合 baseline，也不得把现有非零高相位归零来套旧 zero-control 入口。
v5 wrapper 会把 input_chain[0] 置零，不能直接作为新固定问题的 provider。

此时 qaux=gauge·exp(p̃0)，d1=phase_scale·log(qaux/gauge)。p̃0=0 给 d1=0，
保持当前完整核心值；以后首列链为 (phase_scale/qaux)·qaux=phase_scale。
qaux 只承载解坐标，乘 Y 与 cut H 的数仍是原 gauge。
沿现有 fixed=True/M参数 BVP，应释放 d1 为解未知，保持其余 M−1 高相位；
这不保证新的有限 Jacobian 可逆或收敛。

最窄落地是：新增 v5-actual 来源 validator 与“最终 actual δ 冻结”的
geometry adapter，让**首个真正 fixed-step**显式消费该 actual 设计场作为
完整未接受 initializer，随后仍实跑原 full-H/外迭代/全门。
不必另造一个“已接受线性锚”，也不必谎报一次新 solver success。
design→fixed 这次选择未知空间的步骤不套普通
`same_complete_problem_as_source=true` 标记；后续层才比较同一冻结定义。
若另做无求解的同图重表达，则它须有自己的诚实 provenance 和全图身份检查，
不能重用实际 solver-return 身份。

## Mean、升 M 和尾范围

从**最终源场**固定 N_source=`prefix_audit.samples_psi`、原 literal ψ 节点、
均值 integrand/primitive 起点及 BC normalization；后续 M 变化不改 N_source。
M24/M32/M40 的原默认 N 分别是1168/1552/1936，但实际记录优先。
新的 metric audit 角网格可以加密，必须与定义 Cartesian 图的 mean 网格分开。

现有 `audit_full_relative_metric.audit_loaded_model(mean_nodes=...)` 与
`warm_fixed_m3_compare_c2.complete_jets(...,mean_N,...)` 已支持任意指定 N，
可以直接复用；要改的是五件顶层硬编码1168及相应身份检查、height binding、
seam/primitive 调用和输出。不能仅改 mean 标签而让调用仍用1168。

已有 `warm_actual_dn_refine_model.transfer` 的完整 Fourier blocks 嵌入、
原节点保留、physical quintic 新节点初猜及 R48 系数1 lift 可复用。高相位
零延拓须保持同一无限族的前 M 项，新增 d 为零。它只是初猜，不能晋成接受场。
旧/新实际 controls 的浮点差应如实记录；不把初猜的 roundtrip 差冒充严格同图。

尾 config 保原全部物理背景、cut、有限 depth、shootingParts、calibrationSteps、
warpSteps 和边界构造。现 validate_refinement_definition 已仅允许 runtime
字段以及 modes/quadrature/RK steps 的声明变化，这部分可复用；新 RK 不减且
为整数倍，quadrature 保原严格下界。完整旧 shooting checkpoint 是 warm 初猜，
新目标仍须新完整 H/J/audit 和原外迭代，不回到线性 DN。

当前 C++ 第396/487行与 parallel_native_batch.py 第38行硬限 M≤64。
新序列应在启动前检查全部 levels；M56 的默认 +8/+16 会到72，不能照跑。
源 M>64 不能通过截成64迁入；M64 以上需要另行实际实现/验证 kernel，现入口
没有该能力。已有 step/acceptance 还硬限 workers2：native4 是执行元数据的
显式适配项，不能把4的 manifest 当2。四 worker 不改变固定物理问题。

## 一个容易漏掉的比较分支

`warm_actual_dn_refine_compare.py` 第191–192行目前仅对 `-v3` 后缀取
complementary-arc 真频率，否则取全周期3j。新增 v4/v5 来源时必须显式根据
已绑定的 R70 endpoint_family 且 λ=1 选择 complementary_arc_sine_v1。
只扩 KIND 而沿旧 else 会给错 phase 差界。已有严格 phase 差函数可复用；
这里不重证 R69，也不把有限六jet样本升级为 C² 极限。

本次找到的是上述来源/冻结/动态mean/端点分支缺口。原 actual solver 内核、
全H/最多八次外迭代、完整 lift 与数值六jet函数无需重新发明；实际 λ=1/full-DN
输入到位后再作这些明确接口的窄适配。

## 本次源码绑定

路径相对本课题；在恢复的公共 partial clone 中实读 SHA-256，未改这些源。

| 文件 | SHA-256 |
|---|---|
| scripts/resume_20261126/warm_actual_dn_refine_model.py | 45195b5b2a80a509dbc1882cd8b92a52813c2984198fee61bdafc3f52b7dc3c1 |
| scripts/resume_20261126/warm_actual_dn_refine_step.py | 54d48717642ee1f65eba5d935297eb8e018b2483a06e028f3a502895dd0b324c |
| scripts/resume_20261126/warm_actual_dn_refine_acceptance.py | 3844afaf3ad6c41bcf8370f635bed42c6f1dcec50bc385acb1d59c04d8be446b |
| scripts/resume_20261126/warm_actual_dn_refine_compare.py | d413752429629fe1515c827f820c56b6c91687fb93543163017289b351998579 |
| scripts/resume_20261126/warm_actual_dn_refine_pipeline.py | 047abc9589cfb7df600c0b04d0457543effeda6cb20a1713b51684658f51824a |
| scripts/resume_20261126/warm_delta_phase_factory_v5.py | 56772568ba9ddbfcf78d65cb0104991b694a4806335914762158a58d2391fc83 |
| scripts/resume_20261126/warm_homotopy_core_factory_v4.py | f303897c231639b2dd68854d7bf37cc8862eea4e52b468d5be84c856e84fbcb5 |
| scripts/resume_20261126/warm_supported_core_factory.py | 9192499334d9f8603c812cd95964cc660a065132a82ce240fe2331f64c9b14dc |
| scripts/resume_n4_tail/native_extended/frozen_flow_production.cpp | e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf |
| scripts/resume_n4_tail/native_extended/parallel_native_batch.py | 9177a8499517695deebf00907c64bdc08adc5e5fd2229c8987a2a7ac8ef6bb42 |
