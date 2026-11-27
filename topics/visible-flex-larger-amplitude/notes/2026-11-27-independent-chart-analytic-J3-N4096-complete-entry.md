# 独立固定 7c 目标、完整解析 J3 与 packet 的 N2048 → N4096 观察入口

本文件交付完整可执行来源与参数，不报告本次新入口的科学结果。所有本地操作仅处理完整源码、文本、AST、编译和 stdlib 命令行；没有导入或运行 NumPy、Torch、SciPy 科学模块，没有执行 F、J、root、求积或 fixture。新的科学入口只允许公开 Actions。

## Revision2：在准入前修正完整 C1 来源断言

首批未执行候选的 N geometry 构造器从原 `781778dc...` 继承了一处 `normal_frame_C1_reuse.source_sha256 == ba3d68f8...` 的 literal 断言；本包实际 C1 完整源为 `aeda86f6c10054f79758174d978356fc046881b5f3aba9aea91c4b2b50617f35`，所以旧候选会在真实初始化时拒绝正确的新 C1 来源。该候选没有准入或科学执行，不记成一次实际场失败。

Revision2 只将这一条当前 C1 断言钉到实际完整新源，并逐级更新 geometry/driver/launcher/reader、再生器和参数的 whole SHA。全部 normal、解析 J3、frame/detached/adjacent 数学、N observer、history transfer 和科学循环保持原候选字节；geometry 除这一字串外也逐字不变。完整旧候选 blobs 和交付表 `40f28c7e...` 保为历史，不覆盖其来源。实际 literal 搜索中其余 ba3d/8e6 只用于明确历史父来源，不能再误用作当前 policy 的来源。这里不把先前有限范围的源码审读冒成发现此遗漏前已完成了所有跨文件断言核对。

## 1. 确定的输入家族与此次改变

此入口以已经完整冻结的 run08 独立目标为准：完整参考模型为 `492456a67601cac752dc8e5cb79c14eaccc7339b2d3206f0d570bb60b02c5c5e`，完整参考 bundle 为 `eeb55084744c60a5ed2e2bbb4343b01c73028a6ab61b1216142e4b3bf57dd6b4`，全部 160 个固定 chart 系数字的摘要为 `7c4c9b736c0c8081e9f00a131db5fb63af224aa64fb476c07c78c09b5288bb48`。这些不是单独可替换的几个摘要。完整 `105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361` 输入 producer、完整目标定义、全部 160 个 canonical hex 字、准确 scalar 参数、923 个准确 affine 节点、六个实际文件 record、公示返回与完整历史 dc5 carrier 共同进入守卫。

完整原 `4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b` memory 中的独立目标校验没有改成另一套弱验证。新的 N memory 对 `validate_public_binding`、`_validate_independent_target_binding`、`read_carrier`、`_original_p0` 四个函数逐 AST 保持相同。整个 `MaterialEnvelope` 除构造时新增当前观察定义外，原成员行为逐 AST 保持相同。旧 `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e` chart 仅是已说明的历史身份；这里仍明确 `same_original_fixed_chart=false`、`same_mathematical_g_claimed=false`。不会由 N 精化把旧 90 与当前 7c 的两个目标认成同一个。

本次只将当前完整观察层的 full N 从 2048 改为 4096。固定参考仍使用原 N2048、M160、J923、完整 scalar/chart/seed；当前所有外自由坐标、径向物理 quintic、7377 个原观察径向地址、每胞 8 个外积分 Gauss 节点、18 个 literal Q 字、两 bubble、gamma、32 个共同 normal 阶段均保持。这里没有 M320 频率精化，也没有径向 mesh 精化。原 N-only 包中与目标无关的完整 observer、base 和 Q binder 三体逐字复用；真正决定本家族目标的 memory、源闭包与父模型核对均另作完整来源绑定。

run09 已有自己的实际 warm/reference 输入。此交付不预填其与 run08 的全字相等，不把其 old90/d449 输入冒作本包的 7c/eeb。将来接 run09 必须使用其独立完整 producer、memory 与 actual target 验证来源再派生，不可只改这里的几个常量。

## 2. 当前观察载体与准确权重

令旧 quarter 角字为

$$
\phi_j^{\rm old}=\operatorname{binary64}(\pi j/1024),\qquad 0\le j\le512.
$$

新的 1025 个实际角字满足

$$
\phi_{2j}^{\rm new}=\phi_j^{\rm old},\qquad
\phi_{2j+1}^{\rm new}=\operatorname{binary64}(\pi(2j+1)/2048).
$$

偶数位置直接复制实际旧字，不通过另一条浮点表达式重算。observer 保存并严格重读两个完整 literal hex 列表、完整数组摘要和完整定义 identity。新 full-orbit 整数 multiplicity 为

$$
(m_0,\ldots,m_{1024})=(2,4,\ldots,4,2),\qquad \sum m_j=4096.
$$

旧偶数列的权重总数为 2048，新增奇数列也为 2048。每个旧角在新完整平均中的归一化权重是旧完整平均的二分之一。全部权重严格为正；没有删角、抽样 cap 或依误差挑角。

在同一当前 raw 三 Gram buffer 上，若 $L$ 表示一个既定点损失，准确算术中的角平均恒有

$$
\langle L\rangle_{4096}
=\tfrac12\langle L\rangle_{\rm old\ even}
+\tfrac12\langle L\rangle_{\rm new\ odd}.
$$

实现从同一 raw buffer 完整读取 all、old_even、new_odd 三组，沿原全部径向权和同一谱损失参数计算归因。它不追加 F 求值，不拿旧父报告中的 Phi 作偶数组值。纯 reader 保各组实际角数、权质量、损失参数、Phi 与完整最大 Gram 误差，并报告实际浮点 half-sum 差；没有把该差默认为零或把准确恒等式当作已付浮点舍入证书。

N 变化使有限观察目标改变，不能把新旧 finite Phi 或阈值直接相等。若要比较，必须用新当前场的共同偶数角读取；本包已提供这一读取。非多项式 SO3/implicit 场并不因 M160 而自动具有有限角带宽；1025 个角的通过仍不是全角或连续证书。以上是 [R679](../results/R679-dyadic-angular-refinement-and-common-grid-attribution.md) 的实际完整来源适配，不重登记一个泛化结论。

## 3. 固定参考与当前 observer 的真正分离

`so3_angular_refined_smooth_triangle_meridian_operator.py` 的原 33 个类方法中 31 个逐 AST 相同。只改构造与 `domain`：先保原 parent/reference N2048，再建立当前 phi/multiplicity；`domain` 保原固定参考的完整正性采样尺寸，避免因为 `self.full_N` 的含义改动而悄悄改另一项物理筛查。

`reference_full_N=2048`、`current_full_N=4096` 与完整 observer definition 成为新 base 模型的明确字段。所有原 core、三通道 omega、H 的 packing、unpacking、自由掩码、J/J*、径向宽度与外积分不变。完整模型身份变化被如实记录；不是把旧模型 identity 覆写为新 identity。

新的 normal 相对最终 `04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e` 保持全部 52 个类方法逐 AST 相同。解析 J3、C1、detached stage-matrix、adjacent-frame 四个 helper 的完整函数与类数学体也保持；只重新钉新 base/helper/schema 来源。校准 helper 的实际端点/全六jet 内容和冻结原初点规则不变。三维 Newton 的真实 residual、domain、Armijo、每个 stage 的局部矩阵、角 jet solve、完整上游 implicit/adjoint 均不删。

这些来源等式证明“只做已声明的观察与来源适配”。它们不证明两个不同批形/缓存顺序下的浮点 F 逐字相同。准确模型的场包含也以选中同一完整 implicit 分支为条件，不能由有限输入相同直接宣称全角 IFT 已付。

## 4. 原地址、全部 G 与新 typed 政策

新的 `angular_refined_independent_chart_memory.py` 仍完整读取原 P0 的十一份来源、完整 old dc5 carrier、当前 carrier 和当前 preparation 的完整 `new_locations`。其新网格是所有已付旧/当前径向地址的并集，乘以当前全部 1025 个角。旧 513 个角逐字在偶数列，因此原 oldG 和 currentG 的全部物理地址被包含；旧径向地址不同于当前时，仍完整读额外旧径向层，不以“counts 相同”代替字比较。

每份可能含索引的历史在其自身声明的 N 下先解析。`_walk_at_declared_N` 用该 N 创建原 `Locations`，用完整对应 carrier 解析 grid，再将完整 curvature/radius/protected 三类 literal 地址数组转入新 memory。索引历史缺 N、N 不是明确支持的 2048 或 4096、carrier 字不一致均拒绝。绝不将原 `angle_index=j` 直接解释为新 `j/4096`。

新 geometry 除构造/source/schema 的真实绑定外，原 34 个类方法中 33 个逐 AST 不变；整个物理 scan、world dp、两 principal curvature、正负 reach 分支、幅度全筛、原 192-prefix 与 appended 行行为保留。完整原 selector `729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7` 本来按 `screen.q.N` 与实际 shape 工作，源字节不变。近活动行的原 cap32 只约束新工作候选；所有真实拒绝产生的 typed 分离记忆仍 append-only、无该 cap。

reader 仍核 `original_prefix_rows + appended_amplitude_rows + appended_envelope_rows = selected_rows`、原 prefix 字摘要、新 suffix 字摘要、全列与实际 row-cache 字节。失败或部分 scan 保其实际点摘要和 partial scope，不能把缺失字段填作 complete。

## 5. 从真正 N2048 完整父场迁移

支持的实际同目标父来源为完整 `95559b0c...` 家族与最终 `0dfb96e5...` 解析 J3/packet 家族。它们必须先通过各自完整原 reader，包含原 memory `4d92...` 与完整 105289 目标绑定。另一个 cc0a/old90 家族仍可作为未读并行来源义务登记，不能被当成本包的实际同目标完整父。

`compatible_legacy_model` 先核当前全部实际来源和 observer，再核旧父完整模型与旧策略来源。仅对明确改变的 source/schema、observer 三字段、已另核的 working-matrix policy 以及依赖 base identity 的 Q/calibration 字段作规范化。规范化之后，完整 base、完整冻结 chart/scalar/seed、准确径向 mesh、Q18、gamma、tau32、全部 free layout 和其余所有模型参数必须逐对象相等。

这不是只比较 M、J、N 或几个维数。每个 Q/calibration 先核自己的全模型 identity，再变换其依赖 identity；不接受来自别的 base 的同形数组。规范化记录同时保存 old/new 完整模型摘要及完整公共定义摘要；明确没有继承已计算浮点场或旧 finite objective。

完整迁移还读取父 `history.sources` 的全部来源闭包。每份真实文件的 path/bytes/SHA 先后重核，所有原 N2048 索引在旧 N 下解析；完整三类地址及保护集须被新初始 memory 包含。每个 old/current 径向 carrier 成员、全部径向 union/extra 摘要、旧 513 角摘要、完整独立目标对象与新载体作包含核对。

所有父 typed 行按真实 ordinal 无 cap 迁移。完整原 row 与第一发现 point/source/lineage 分别保存；原数值不被当作新场 g。原 `material_envelope_transfer` 整体也保留，因此祖先未读 peer 义务不会在下一次 source/N 转移时消失。纯 reader 会重新读这些完整原报告与来源；不会只相信 transfer 中的几个 `true`。

### 完整 final 只作为新外变量初点

显式 `--material-envelope-seed-report` 与 `--material-envelope-seed-checkpoint` 必须成对，并对应已经完整迁移的真实 terminal parent。原 reader 必须实际验证该 final，所有 13 个 NPZ 成员完整匹配：

- `schema`, `omega_jets`, `core`, `Hcap`, `mesh`, `fixed_parent_core`；
- `zero_closure_model_json`, `zero_closure_model_identity_sha256`, `base_so3_model_identity_sha256`；
- `fixed_scalar_metric_identity_sha256`, `endpoint_root_policy_json`, `working_integration_order`, `working_full_angles`。

原 checkpoint 的 `working_full_angles` 必须是 2048，原 base identity 必须是原父完整 base identity。它们不能与新 N4096 的模型摘要误比较。全部 `omega_jets` 仍为 `(J,3,n)` 的真实 SO3 三通道数据，按原完整 free mask packing；没有照搬别的 R/T/Z 空间布局。新 `q.unpack` 必须逐字重建全 core、全 omega 和 H；整个 mesh、固定 core、固定前三槽、dtype/shape/finite 均核。

冻结 reference model、reference point 和 `base.initial()` 保持原字；复制的是当前外变量初点。之后重新读新初场、normal 根、六jet、Phi、全 geometry 与 norm。旧 root/cache/矩阵/可行性/Phi/证书不迁。

## 6. 独立分支、重启与未知 peer

完整 runtime 有三个明确模式：显式原参考独立分支、经完整父转移后的新分支、同 source 的实际 restart。独立模式拒绝混入旧 final/parent/restart；严格父模式仍要求真实完整终态证据；同 source restart 仍核整个当前模型与 memory，并恢复完整 typed annotation。

独立分支已经有完整 P0 和 old/current G 的永久真筛责任，不需要把某个未来 peer 的 terminal report 伪造为已存在才能执行。未知 peer 的额外 typed 首次发现、顺序和保护来源并不由全 G 的包含自动推得，仍保为后续真实绑定和合并义务。

在 05:02:15 的实际 API 观察中，run07 `45909290354/1` 已为 completed/cancelled；API 的 `updated_at` 是 05:00:28。05:02:15 是观察时刻，不是已知的 child 终止时刻；科学子进程终止时刻与原因仍未知。旧公开 compact 的 step4 停在 running、没有 terminal 科学返回。这里的 `pending` 指未付款的实际报告/地址/typed 来源责任，不声称该工作流仍活着，也不把取消推为无新增点。run08/解析父是否有完整 final，只能在实际 whole reader 读取后决定；本交付未填写不存在的 final hash。

## 7. 完整科学循环与只读 packet

driver 相对完整 `0dfb96e5...` 的 `save_report()` 至末尾科学后缀，仅在 `statistics()` 的同 raw buffer 增加 observer 归因的两行。去掉该明确新增语句后，整个后缀逐字还原，SHA 为 `d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376`。原 Phase I、全部正权 metric 行、完整 C、QP/J/J*、真实 trial descent/domain/geometry、永久记忆、accepted 出口和原两处 packet hook 都保持。

packet helper 只在原完整 registry 增加本新 normal/base/calibration/adjacent/analytic 的整源条目；所有原 packet 函数和类方法保持。仍只保存已存在的当前角/root/stage/J3/J6/J9，不触发新 F/J/root，不升级低阶缓存。current cache point 与 outer point 分别记录，未返/空缓存不冒成完整场，I/O 失败不借旧 packet 冒本次成功。

C1、detached 和 adjacent 的实际命中/成本只由运行后计数给出。N4096 会增加实际观察工作，不存在本地测得的加速、提前收敛或几何改善结论。[R714](../results/R714-normal-frame-exact-zero-and-C1-reuse.md) 与 [R715](../results/R715-reference-centred-normal-sixjets-and-error-ledger.md) 的连续费用边界不因此消失。

## 8. 完整参数与可执行模式

三份 ready 都包含完整实际 argv、两步科学/纯读、64 个运行 source roles、17 个完整 runtime 身份、九份 source-construction 身份与原参数来源。它们均是 `executed=false, queued=false`；不将文件存在当作实际求解成功。

| Ready | 初点/父责任 |
|---|---|
| `angular-N4096-analytic-J3-independent-ready.json` | 实际冻结原参考完整自由点；全 P0/twoG；明确保未知 07/08 来源义务 |
| `angular-N4096-analytic-J3-parent95559-ready.json` | 实际完整 95559 report + final；完整 N2048 地址/typed/13 成员迁移 |
| `angular-N4096-analytic-J3-parent0dfb-ready.json` | 实际完整 0dfb report + final；同样完整迁移，另保其 packet/祖先来源 |

只有 `--angles 2048 → 4096` 是本次新的数值参数。保 `directions=1,maxiter=16`，恢复 `4×64`，`mu=.01`，15 回溯、192 原几何前缀、32 新近活动候选、原所有真实预算与全永久行。normal32、外积分8、seed 径向8、profile16、共同 boundary `1/16`、delta `1/128`、原所有 root/mean 迭代与容差均保。完整来源/outdir/actual parent 路径变更另明列。

科学步的实际 parent 是原 reference 或严格选定的真实旧 final；纯读步一律以原 reference 为 controller parent，所以初场失败并不因新 final 不存在而阻断读数。只清理对应新 outdir 的 `rows-*`，保固定 seed/reference cache 和 packet/raw 供后续同场费用工作；raw 不写 Git。

这些 ready 的 `{work}` 路径要求真实存在相应 run08 7c 输入和完整 105289 proof。新 run 的 warm/reference 若不同，不能按文件同名或参数相似直接准入。09 的新目标入口由其完整新来源另接，不让当前 strict7c 科学 source 临时放宽。

## 9. 可复现的 source-only 交付

九份完整源构造文件包括七个全体派生/增量构造正文、总再生器和完整 ready 构造器。总再生器读取完整 22 个 parent-source 身份，逐序生成 17 个运行体，严格核 64 个 runtime source role、每个全体 SHA/bytes、AST/compile、重复 literal key/keyword、空白与单源小于 100000 bytes。没有导入发出的科学模块。

运行方式：

```sh
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_angular_refined_analytic_envelope_sources.py \
  --topic-directory topics/visible-flex-larger-amplitude \
  --construction-directory topics/visible-flex-larger-amplitude/scripts/resume_20261126 \
  --output-directory /tmp/complete-N4096-source-output
```

在完整已刊目录核逐字再生：

```sh
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_angular_refined_analytic_envelope_sources.py \
  --topic-directory topics/visible-flex-larger-amplitude \
  --construction-directory topics/visible-flex-larger-amplitude/scripts/resume_20261126 \
  --output-directory topics/visible-flex-larger-amplitude/scripts/resume_20261126 \
  --verify-existing
```

实际本地只执行过完整 source replay、AST/compile、三个完整 launcher argv 的 `--print-command` 和 stdlib reader `--help`。这些不是科学或数值测试。旧父 ready 两个完整文件也有 whole SHA guard；ready 构造器只改变已列观察/source/path/mode 字段，保全部原 scalar summary selectors 并新增实际 N/共同 buffer 归因标量。缺实际值时保 null/失败范围，不制造统计。

## 10. 尚未付款的范围与径向后继接口

本入口没有全角、全径向、normal 连续分支唯一性、逆矩阵、积分/三角/舍入、full-t reach 或最终几何证书。准确参考的 profile moment 与总均值费用仍由 [R713](../results/R713-exact-smooth-triangle-moments-and-actual-fees.md) 等同场消费者处理；[R711](../results/R711-smooth-triangle-central-profile-and-geometric-comparison.md) 的 seed 比较不自动迁至新的非零 outer/normal 场。

径向精化还需要分离固定 reference J0 与 current J，保全部准确 affine 旧节点及新增节点的 provider query；新 local-u 不能经一次舍入后塞回旧 cell/u 当作同一个准确地址。还需完整 quintic jet restriction/injection、全部新旧径向观察与积分路径、parent checksum/layout 迁移及其连续费用。这些没有在本 N-only 入口中假称已实现。M320 也是另一份明确固定 M0/current M 的完整布局适配；这里保持 M160，未来组合必须重新闭合其 actual source/model/transfer。

## 11. 完整运行体身份

下表列本次全部 17 个可执行运行体。完整源文件本身是交付；表格不替代源体。前 3 个为原已锁 generic observer/base/Q 完整复用，其余 14 个为本 analytic/7c 家族的独立完整来源。

| 完整文件 | Bytes | SHA256 |
|---|---:|---|
| `angular_observation_refinement.py` | 11045 | `8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3` |
| `angular_refined_analytic_adjacent_matrices.py` | 36734 | `032c69fad6425c7b70d75d288884fff293eaa76b2e1fdfb822b87f2d2b9febfd` |
| `angular_refined_analytic_calibration.py` | 11890 | `186798d2d31924941f7917c32afb856d584ca13dfea8602798e5206e0489af93` |
| `angular_refined_analytic_frame_c1.py` | 35625 | `aeda86f6c10054f79758174d978356fc046881b5f3aba9aea91c4b2b50617f35` |
| `angular_refined_analytic_history_transfer.py` | 74332 | `26e40b278a83a93fc3214af05656f2a3a8b5148f94a6a0f01619eed83a714918` |
| `angular_refined_analytic_normal_stage_jacobian.py` | 24218 | `f497452ff23188bca80556773f7493418e3f60b94108af5e5c92956c82e544b7` |
| `angular_refined_analytic_source_binding.py` | 22857 | `48fecda3f3da2fda7eee3dc37e120ba89448bde7539d2f90c89f4b6791587ef5` |
| `angular_refined_analytic_stage_matrices.py` | 47673 | `0ac33e262d4bb95f84f548b630c955e481430d2cf4b899ec7829bafea845ab3d` |
| `angular_refined_independent_chart_memory.py` | 51425 | `9cf973b75c108ecfee4a5beef792ab81b682e8ba71cf667b2d068bb0c33f0f2e` |
| `angular_refined_smooth_triangle_literal_zero_moment_input.py` | 30940 | `a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d` |
| `fullclosed_angular_refined_analytic_envelope_so3_qp.py` | 83420 | `fbabe2dc44f5f7f406549aaea567892809e139d07eadea4fccbd8f0e6e9dc819` |
| `immutable_angular_refined_analytic_root_packets.py` | 67590 | `fa1f8b0219610602e8c695482e3303c1df6dee7ac3402648e7579ff1f988688c` |
| `launch_angular_refined_analytic_envelope_so3_actions.py` | 21572 | `bf460b1a103b394874b2a898ab9f84eefb1abf1fdb57cfc87334135249ea34c3` |
| `read_angular_refined_analytic_envelope_so3_report.py` | 97700 | `820274bec9f54c017e9473f1f0db2ec5bc38f7a1a91be8b9b6162b76ef39d692` |
| `so3_angular_refined_analytic_envelope_geometry.py` | 68907 | `d04ed9db9756610ab725bcef6e4199611c46cbcc2d7a7e3cf69bd80803eaeefd` |
| `so3_angular_refined_analytic_normal_lift.py` | 96877 | `361df1bcd7034616d3c0830a20444896dd3992a0d1295ec01ab690f94a61262b` |
| `so3_angular_refined_smooth_triangle_meridian_operator.py` | 41592 | `1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529` |

## 12. root 完整再生与当前执行边界

root 完整读取原20589-byte说明及revision2全部实际差异；核当前C1等号修复而不删guard、07只把05:02:15作为观察时刻。30项完整交付逐件核全SHA/bytes，其中3个通用运行体与既刊源逐字相同；其余27个完整文件独立保存。root实际运行16,455-byte总再生器8aace56e，exit0，17运行体整字节再生相同，并独立核64个实际运行来源SHA。没有本地科学或fixture。

三份ready revision1→revision2的递归JSON核对没有删除任何原键、没有改变数组长度；数字变化只在两个构造源的实际bytes记录，原求解数值参数完整保留。所有完整science/pure argv、未知peer义务及原scalar selectors保留；首次生成候选的C1 literal错误不冒实际科学失败。新体只适用已冻结7c/492/eeb输入，09的真实90/d449目标尚须另以全来源适配，不能直接排这三份ready冒同目标。

本次同时纠正完整解析frame说明中的纯读字段层级：pure读取 `analytic_normal_frame.latest_actual_diagnostics.*`，driver对应 `latest_operator_metadata.analytic_normal_frame.*`；只有说明文字改变，14体/全部数学及SHA不变。未产生metadata时保持None，不填虚构0。N与frame均待实际完整场返回，source再生不构成误差精化或完成标准。
