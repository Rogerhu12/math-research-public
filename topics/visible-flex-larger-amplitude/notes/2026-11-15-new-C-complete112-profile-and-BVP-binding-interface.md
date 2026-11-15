# 新 C / R300 v3 → 完整 112 模式物理接口

作者：AI（geometry）。日期：2026-11-15。

## 1. 已实现的边界与仍缺的真正尾部

本项给出独立可执行的 profile/线性行来源适配器。它读取实际 R300 v3 factory 的 result 和准确 expression definition，核原 core、九参数 recipe、同 C cut 三盒及原二阶 jet reader；创建已发表 numerical profile 的真实对象；保全部 112 场模式；提供三 active、全九 frozen、全九 active view；可以构造原完整物理 flow / R252 boundary，以及把完整旧场重参数后重新求全部 RHS。

它还能读实际 R324 的全部 112 个完成或未付行，保不可除的 Robin 关系。只有原 producer 已实际完成全部分母验证和商，才生成公开标记的数值线性近似。

**没有实现新 C 的非零非线性 TailClient，没有执行 full-DN Newton、原 FD、完整 RMS 或最终 fresh audit。** 源码的线性对象 `.solve()` 明确报错，不能冒充原 live client。旧 finite-tail ready/零响应/旧 checkpoint 不被重新标成新 C。

当前没有已接受的新场；没有选择未来的实际参数、采样点、工作流或阈值。148 的实际非共振结果仍待原回执，本接口没有预填任何非零分母。

## 2. 运行件与冻结依赖

新文件：

| 文件 | UTF-8 bytes | SHA-256 |
|---|---:|---|
| `computations/geometry_20261115_continuous_C_full112_binding.py` | 42658 | `c0bda3350b30b9659c326112eaf8f411d0bb6f825a7a3f81fcc6c7502ed3f952` |

它不修改下列已发表源：

| 原入口 | SHA-256 | 复用范围 |
|---|---|---|
| `geometry_20261115_continuous_nine_scalar_factory_v3.py` | `0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e` | 准确 R300 expression、原 C 三盒 |
| `geometry_20261115_continuous_nine_scalar_numeric_v3.py` | `7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60` | 原 point/batch/raw jets 与公开有限编译 |
| `geometry_20261115_continuous_nine_augmented_v3.py` | `d86f6fdf3cf59df3d45c907c655fe54ab830180facd27b7402e649b2e14d151b` | 只替当前 scalar_jets，继承物理与 J |
| `geometry_20261114_full_dn_augmented.py` | `f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e` | 全 338+112+k 行、完整增广与分离边界 |
| `geometry_20261114_r225_free_core_bvp.py` | `a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08` | 原完整 FFT Frenet RHS |
| `geometry_20261114_full_dn_boundary.py` | `4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2` | MaterialTrace、公共材料角、原 cut 检查 |
| `geometry_20261114_physical_test_boundary.py` | `3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681` | 原 R252 finite physical-angle 全边界与 J |
| `geometry_20261115_stored_C_finite_head_flux.py` | `4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d` | 可选：实际同 C 全112 cut 列/商 |

准确 factory 的尾来源保持：

- C v3 producer：`f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df`；
- 原 cut reader：`1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed`；
- model：`R286-original-stored-continuous-model-convention-C-v1`；
- deep definition：`original-exact-root-family`。

CLI 只实例化 factory 产物、numerical profile 与 flow 模块，按选择读取 actual linear。调用完整物理 API 时额外核实际加载的 f76/a1e/3975/4517 源。将来原完整 BVP 的其他原 source closure 仍由其原入口保留，本短表不替代那个闭包。

## 3. 已有 BVP 主体无需重造

| 既有入口 | 已实现部分 | 新 C 必须真实提供的部分 |
|---|---|---|
| `geometry_20261114_full_dn_solve.py`，`c6a1f4d8…` | 真实 H 外层、actual tail J、affine inner map、原 preflight/fresh audit | 当前 profile、完整初猜、真正新 C live owner |
| `geometry_20261114_physical_test_full_dn.py`，`abbf1a53…` | 原 R252 FD/fullmain/最终物理验收入口 | 当前真实 H/J response 与来源 |
| `geometry_20261114_physical_test_response.py`，`83ce3877…` | 原完整有限边界方向 FD | 新 C actual anchor，不能改旧 zero-anchor 标签 |
| `geometry_20261114_lifted_modes_banded_full_dn.py`，`390387db…` | 完整带状行布局、原求解实现 | 真当前 flow/boundary/完整初猜 |
| `geometry_20261115_nine_control_full112.py`，`00e4d2c3…` | 三 active/六 frozen 的 453 编排切点 | 其旧 scalar/zero-J/input 硬绑定不适用；只复用组织方式 |

准确切点是 `make_profile / constructor / boundary / initial_guess / load_client / scalar_spec`，不是改写 Newton 主循环。旧九 wrapper 的 `SharedNativeClient` 保一位 live owner、当次 H 与真实返回/关闭语义；新 owner 必须由新 C producer 真正建立。

原 `AffineTail.set` 读取响应的 `jets.slope` 和 `heightJetJacobian.reshape(338,112)[:112]`。原 `final_height_seam` 还读取 `jets.second`、`meanSlope`、`meanSecond` 并 fresh 求 prefix 末导数。单独 112 个线性斜率不具备这些生产责任。

## 4. 三个对象分别保留

### 4.1 准确新目标

准确目标由实际 expression DAG、完整 pieces/supports、九参数、原 core 与同 C 三个 semantic cut leaves 决定。在公共材料域上

$$
g_{\rm true}=L_{\rm true}^{2}\,du^{2}
+a(L_{\rm true}u;p)^{2}\,d\theta^{2},\qquad 0\le u\le1.
$$

三个 leaf 是同一声明 C 下的 $E(R),E_r(R),E_{rr}(R)$。原结果均匀包围允许根族，不据此选一个数值根序列。实际 `chosen_root_scope` 完整保留；原 finite 48 选择器没有被重解释成此连续目标。

### 4.2 有限数值 profile

原 v3 compiler 明确把给定 cut 盒的中点编译为 binary64 leaf，再由同一有限多项式求点值及导数。它产生 $L_{\rm num}$ 和有限函数 $a_{\rm num}$；新适配器不重实现该算式、不截九控制、不改其 point/batch 顺序。

数值解用 $s_{\rm num}=L_{\rm num}u$。保存 `numeric_compilation_sha256`、cut 全词和完整 export。三个 leaf 中点是否由一个真实根序列共同实现未证明；该有限函数不被改称准确目标。

最终对同一准确场的原 target metric 责任仍交 [R326](../results/R326-common-coordinate-target-enclosures-and-same-field-metric-transfer.md) 及完整区间消费者，有限采样不支付此项。

### 4.3 实际 R324 线性区间

R324 列是同一声明 C 下完整表达的区间推进，均匀覆盖每一个允许的固定根序列。它不是旧 finite-tail zero-J，也不等于对每个模式独立取中点后恰好获得的某一同根尾算子。

可选数值线性近似逐行保存原区间、准确中点、实际 float 词和准确舍入偏差。不同模式中点与 cut 三叶的共同根实现继续未付。

## 5. 实际 factory/result/definition 绑定

`CurrentProfile(factory_directory, actual_result_sha, code_directory)` 全读实际 result bytes 及其指向的完整 definition；核原 core/model recipe receipts、actual tail/cut receipts、三片 dyadic 包围、原 binary cut 与全条件 scope。

recipe 的 JSON 数字与 definition 的有理字符串按原 factory 的 `Fraction.from_float` 语义核同；不因表示形式不同误拒实际同一值。

已建完整 definition 而给定九参数区间域未付时，保留原 false；不把原 interval 工作未完加成新非线性接受门。每个 view 当前 p 来自显式新 recipe，并保存全部九词；不暗用 definition 旧初始 p 或旧场的参数。真正冻结同 g 时须取实际选择的全部九 p。

## 6. 三种完整 view 与方阵责任

| view | active 参数 | 固定参数 | augmented 维数 |
|---|---:|---|---:|
| `three-active` | $p_1,p_2,p_3$ | 实际六个 $\theta_i,\eta_i$ | $338+112+3=453$ |
| `all-nine-frozen` | 0 | 实际全部九 p | $338+112=450$ |
| `all-nine-active` | 9 | 无删减 | $338+112+9=459$ |

原 $T=M=112$ 方阵关系为 fixed inlet core 数 $K=$ active 数 $k$。不能把 459 称作 453，也不能把三 active 搜索称作同 g 全冻结精化。

`view(p, mode)` 返回原 numeric 类/原 FrozenShapes/FrozenNine 的真实实例，只在这个新对象附实际 cut 描述，不改原类、磁盘源或旧全局 profile。

## 7. Cut 与完整材料角链式

实际数值 cut 来自该次原 compiler 的 leaf：

$$
R=R_{\rm original\,binary},\quad
a_s=-E_0^{-1/2},\quad a_{ss}=-\frac{E_1}{2E_0^2}.
$$

本 R300 inward collar 的 $\epsilon_r=-1$；$\epsilon_h$ 由实际问题显式传入。没有改名义 cut，没有把自然 $R_{\rm out}$ 归一为 cut，也没有把 $B'$ 换为目标。

`endpoint_record` 保存实际末二 jet、原数值参考、全部词与差、原 $5\times10^{-12}$ 输入检查的诊断。该容差不证明准确实端点恒等或 C²。真正调用原边界仍执行其原检查，未改阈值。

原完整边界保

$$
H=\epsilon_hP(c)z,\qquad
\gamma=\frac{\epsilon_h\epsilon_r}{\sqrt{E_0}},\qquad
R_\phi=z_{s,\mathrm{nonmean}}-\gamma S(c)\mathcal D(H).
$$

原材料角与物理角有限规则彼此独立，全 $dP/dc,dS/dc$ 混合项保留。有限材料角/物理角截断不被称作连续带宽恒等；mean/second-height 最终责任仍要求真正返回，不能补零。

`CurrentProfile.boundary(...)` 实际调用原 `PhysicalTestBoundary`。调用方 tail_map 必须诚实区分 linear/affine/真非线性；构造成功不改变 `current_C_nonlinear_tail_verified_by_this_binding=False`。

## 8. 原完整 RHS 与新 scalar

`CurrentProfile.flow(original_augmented_module, actual_probe, profile, workers)` 使用已发表 d86 wrapper，核实际加载的 f76 及 a1e FFT 源。probe 保完整 $M=112,n=338$ 与全部偶频。

每次原 RHS 调用先形成该节点全部当前 scalar jets，再交原 `BatchedFFTFlow`；不复用旧按 s 缓存的 scalar。保实际完整物理场、112 core 常行、全部 active 行以及原 complex-step J 算法。继承关系不是已经数值执行的验收。

调用者仍保 supplied probe 的原完整来源。新适配器不构造假旧 accepted 文件，也不改原 probe 其他方法。物理域仍由当次实际求值/原 guard 判断。

## 9. 完整旧 699/453 初猜只保真实原输入

`read_complete453_guess` 接收实际 source 文件及 SHA、mesh/states 的 RFC6901 pointer、当前三 active 值和本源 owner/profile/flow。

它全读原 JSON（原 gzip 支持），核完整 $N\times453$、全部有限列和全有序 mesh。真实 $N=699$ 就保 699 个节点；不取低模子集。

$$
u_i=s_i^{\rm old}/s_{N-1}^{\rm old},\qquad
s_i^{\rm new}=L_{\rm num}u_i.
$$

原 338 物理列和 112 core 列逐解码浮点值复制，三 active 行显式换为当前 p；保存原/new mesh、公用 u、旧/新 p 全词。未导出到原 JSON 的负零信息不冒恢复。没有私自投影 core、改零 cut 或改入口值制造可行性。

随后在全部新节点求当次完整 RHS，旧 RHS 从不复用。原节点/中点/full-RMS preflight 仍须原 full 求解器实际执行。旧 g、accepted、merit、BC/RMS 均不继承。

原 flow 始终按 $s_{\rm num}$ 求物理导数；需要公共 u jet 时完整乘 $L_{\rm num},L_{\rm num}^2$。准确目标仍用 $L_{\rm true}$，由 R326 另作误差比较。

## 10. 全112 Robin 行和可除图

`CurrentLinearRows(directory, actual_result_sha, profile_owner)` 完整读取 R324 result、input binding 与全 mode stream，顺序为 $m=2,4,\ldots,224$，包括全部 unstarted/unfinished 行。

原 C binding 逐字核同，仅排除 R324 已声明不定义 C 对象的 query/work/runtime 信息。配置、两个 frozen 输入、源、浅段、warp、模型声明、binary cut 不变。允许不同真实 run 生成同对象，但分别保各自 run/source/result，不能冒同次运行。

已付原列 $(u_m,k_m)$ 中 $k_m=dH_m/dr$，非除式为

$$
-k_m H_m+u_m H_{m,r}=0.
$$

它不要求 $u_m\ne0$。仅当原行区间确实排除零且 producer 实际给商，才读 $d_m=k_m/u_m$。本消费者不重新推进、不补分母、不另选 pivot、不从小残差推非共振。完整 report、全 stream、可选 diagonal 必须一致；原完整未付 suffix/error 不丢失。

只有全 112 图均已付时，`numerical_linear_model` 才取逐行有理中点后转 binary64，保：

- 原完整区间及准确有理中点；
- 真实 float 词；
- float 是否仍落在原区间；
- float 减原区间的准确有理范围；
- 不保证全部 midpoint 对应同一根序列。

舍入信息不是新增验收门。若 float 因窄盒/舍入落在原盒外，如实标记，不静默宣称仍被盒包住。

得到的 `NumericalLinearTail` 仅给完整 `slope=J H`、$112\times112$ J 和 `actual_nonlinear_solve=False`，不能被传作原 `AffineTail.set` 所需的真实 anchor。它没有制造 338×112 全 native jet。

## 11. 可执行 CLI 与真实计划

~~~sh
python computations/geometry_20261115_continuous_C_full112_binding.py \
  --factory-directory "$ACTUAL_FACTORY_DIRECTORY" \
  --factory-result-sha256 "$ACTUAL_FACTORY_RESULT_SHA" \
  --parameter-recipe "$EXPLICIT_CURRENT_RECIPE" \
  --parameter-recipe-sha256 "$EXPLICIT_CURRENT_RECIPE_SHA" \
  --sample-plan "$EXPLICIT_COMPLETE_PLAN" \
  --sample-plan-sha256 "$EXPLICIT_COMPLETE_PLAN_SHA" \
  --code-directory "$ACTUAL_COMPUTATIONS_DIRECTORY" \
  --out "$RUNNER_TEMP/current-C-full112-binding"
~~~

可选成对参数：

~~~sh
  --finite-head-directory "$ACTUAL_R324_DIRECTORY" \
  --finite-head-result-sha256 "$ACTUAL_R324_RESULT_SHA"
~~~

不预填实际未来 SHA。顶层只标准库，数值实例化前检查 `GITHUB_ACTIONS=true` 和 `Rogerhu12/math-research-public`；数值 runtime 为原 NumPy 路径。本地只有源码/AST。

参数 recipe：

- schema `R300-new-C-complete112-profile-view-recipe-v1`；
- `field_modes=112`；
- 完整 `parameter_order=[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]`；
- 完整实际 `nine_parameters`；
- 显式 `view`。

采样 plan：

- schema `R300-complete-public-u-profile-sampling-plan-v1`；
- `coordinates="public-u"`；
- 完整 `queries` 列表，每项含准确有理 `u`，可附来源标签。

源不自动选 query。请求有理 u、实际 float u 词、实际 s 词同时保留；不把有理→binary64 当准确相等。原数值 profile 的查询并非准确目标的闭区间证书。

## 12. 输出、失败与 rule15

顶层 schema 为 `R300-new-C-complete112-profile-and-linear-binding-v1`。

| 暂存文件 | 完整范围 |
|---|---|
| `result.json` | 来源、scope、runtime、真实末端诊断、样本/线性身份 |
| `large-arrays/complete-requested-numeric-profile-samples.jsonl` | 每个原 query 的 jet/control/u-jet、原词、域与异常 |
| `large-arrays/current-complete-profile-specification.json` | 原完整 export、全部九参数与数值编译 |
| `large-arrays/complete112-disclosed-linear-model.json` | 仅实际全 graph 存在时写：112 原区间与数值取值 |

非有限展示值为 null，但保完整原 float 词；每个原 query 都记，异常 query 和 scalar 域失败分开。样本返回不是连续域证。未付 linear、主流程异常、未实现 nonlinear 分开报告。

摘要上限 90000 B，单完整 JSON 用 BEGIN/END 和实际 bytes/SHA 输出；超限返回 70、保临时原 result，不截字段。正常来源/采样读取 exit 0，捕获的阶段异常 exit 2。实际域失败样本仍是读值，不能据此声称执行了完整 BVP。

输出须是 `RUNNER_TEMP` 下不存在的新 owned 目录，不覆盖任何原 factory/linear/recipe/plan/code。无 artifact/Release 上传；未来 workflow 必须完整必要读回后 always 删除自己的可重算 temp。本项未创建 workflow，也不改 147/148。

## 13. 真正非线性 C provider 尚需哪些实现

这些是原 full-DN 已有的生产责任，不是新增完成标准：

1. **同 C 数值几何/根选择。** 明示实际根族选择以及每个积分点 $R,w,R_x,w_x$ 的同表达求值。如果先取一个有限近似，独立身份并保对准确 C 的误差责任，不能用盒中点宣称准确几何已选定。
2. **同新模型完整非线性尾方程。** 原 Fourier root/RHS/RK/guards 可复用公式结构，但每个几何值、远端图和节点状态须来自该新模型；旧 finite-ready、旧 zero-J、旧 577-node 状态不能换标签。
3. **每次真 H 的完整返回。** 保全部112高度、实际 solve/J、second/mean 等 jet、真状态/计数与 audit。同 H 非 audit cache 只能属于同一 live owner 的真实运行。
4. **有限头/深端责任。** R312/R324 是线性列与图；全 $u_m$ 非零不自动证明非零非线性远端、截断误差或完整可解性。
5. **原外层组织。** 新真实 owner 接 actual-H→原 FD→原 fullmain→fresh audit，保原 tol、BC/RMS、回溯与最终 mean/second/seam。不能只做固定 Robin BVP 后写原 success。

本次实际完成 profile、数值 cut、完整 flow/boundary API、全旧场→新初猜、真实全线性行几个可执行边界。当前未发现已完成的新 C 非线性 producer；未用新 schema 或构造成功冒这些数值工作已付。

## 14. 源级验证和依据

本地仅实际源码 SHA/字段阅读与新源 AST，不 import 科学模块、构造 profile、求任何 jet、推进尾部或算矩阵。

直接复用 [R300](../results/R300-continuous-nine-control-scalar-family-and-cut-calibration.md)、[R312](../results/R312-continuous-C-complete112-zero-tail-and-head-connection.md)、[R324](../results/R324-continuous-C-finite-head-flux-and-closed-tube.md)、[R326](../results/R326-common-coordinate-target-enclosures-and-same-field-metric-transfer.md) 的已付范围，不重复设证明门。

[R322](../results/R322-actual144-original-cut-twojet-and-complete-domain.md) 是原144 cut 三盒的实际结果；此源仍绑定实际传入 factory/run/result，不硬写那次数值，也不由一次 cut 包围推新场或全局 metric 已通过。
