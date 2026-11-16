# R467：actual208 的有限 root 收缩实际执行、正高度资源停止与完整必要读回

作者：ChatGPT（AI 协作）。日期：2026-11-16。

**结论性质：实际数值执行与原记录证据。** 本文确认公开 Actions 的实际来源、执行范围、原退出和读取/清理事实；不把 binary64 计算或计数器解释为严格圆整证书，不宣称当前非零有限尾根、完整当前 Jacobian、FD、full-DN 或闭曲面已经通过。

## 467.1 这一次实际得到什么

Request208 确实执行了 R465/R466 的 recorded-factor 收缩路径。原 worker 的零高度请求在 5774.443653623 秒后返回 converged=true、residual=0；同 worker 随后请求 $H=2^{-6}H_\ast$，在 12195.315082156001 秒后返回原错误：

> Error: finite-trace-direction-resource-budget

该错误的已返回地址是 tailStage=366、tailRawCell=5、tailRawSegment=8。原 native completion 明列 finite_trace_variation.resource_budget=true。这一正高度请求没有返回一次完整 native iteration、没有原 trial、没有当前 R273 snapshot 或 correction direction；完整端点 $H_\ast$、要求 Jacobian 的端点请求、原 FD/full-DN 及最终 audit 都没有开始。最后已收敛的高度比例仍为 $s=0$。

新增收缩有真实执行记录：累计 28278 次收缩更新开始和完成，累计 6334272 个方向列返回；精确形成的 backsolve 缺陷中有 3193204 个非零分量，3164179 个分量的显式 binary64 投影改变了原准确值。没有记录到非零缺陷投影消失、投影溢出或旧 factor-loop fallback。但是这些是累计局部操作记录，不能代替同一当前状态的全部 576 段、226 状态、224 方向、338×112 端点返回及原接受门。

原科学和 wrapper 都退出 75；wrapper 的 budget_exhausted 字段实际为 false，external_signal 为 null。必须同时保留这两个外层字段和内层资源错误，不能改写成“外部 SIGTERM 杀死”或“原数学拒绝”。

单份必要正文为 53307 字节，compute/report 中逐字一致；完整必要选择器的所有字段及两次原请求事件均已读。实际 cleanup 在完整读回及真实 owner/规则父进程静止后记录 removed=true，临时科学对象已经删除，不能凭身份恢复当前状态继续运行。

## 467.2 公开实际身份与唯一日志读取

| 项目 | 实际值 |
|---|---|
| 请求 | 208，attempt 1 |
| source/head | 9b05bfc5160bf667cde0cb0ba059b0c8b0332bd5 |
| 官方 run | [43804793905](https://github.com/Rogerhu12/math-research-public/actions/runs/43804793905) |
| 创建时间 | 2026-11-16T04:33:13Z |
| compute job | [133092971995](https://github.com/Rogerhu12/math-research-public/actions/runs/43804793905/job/133092971995)，completed/failure |
| report job | [133209057444](https://github.com/Rogerhu12/math-research-public/actions/runs/43804793905/job/133209057444)，completed/success |
| 原科学规则窗口 | 2026-11-16 04:34:07 UTC 至 09:34:08 UTC |
| 原科学总上限 | 18000 秒，step 330 分钟，job 350 分钟 |

Compute 第 1–9 步成功，包括原来源/配方绑定、四数学输入、两原几何输入和原 78 source 恢复；第 10 步科学返回失败；第 11 步必要读回、第 12 步条件清理均成功。Report 的成功只确认单份必要正文运输完成，不改变 compute 的数学/资源结论。

每个终态 job 只经官方 connector 读取一次。下表哈希作用于 connector 返回的完整已解码文本重新编码所得 UTF-8 字节，**不是** GitHub 原始 HTTP 响应字节身份。

| 完整日志 | UTF-8 字节数 | SHA256 |
|---|---:|---|
| compute | 177965 | 4ba72176b3f435efa5c50b9a6d53362a063ca2c6e54d1e19e6b906e13c0e8179 |
| report | 112635 | 1343717bdd32840af56de96655844e0f4b3536f561f2aedfc117d7b1266ccd49 |

解析视图仅在每个物理行的开始去单个运输 BOM 和锚定的 GitHub timestamp；原完整字符串不改。Compute 874 个物理行，report 76 个物理行；各发现一个物理行首 BOM。正文帧是 BEGIN/END_REQUEST208_CONTRACTED_TRACE_R273_NECESSARY_SUMMARY，compute 在物理行 768–770，report 在 71–73。两帧 body 都是：

- 53307 字节，SHA256 d5b5cbea483664e68a91f337cad0b6560e2d246bdb34e1b1b5dd0850d95ed165；
- 身份不含分隔 LF；
- schema=request208-original64-contracted-trace-r273-necessary-readback-v1；
- summary_complete=true，transport_complete=true，errors=[]。

Report 环境打印中再次出现的同一正文不当作另一独立科学事件。运输没有拆包、语义分段或大科学树编码。本文的“完整读回”始终指该已公开选择器的必要范围，不能扩成全部 root tape、逐角矩阵、全部原 traceback 或完整科学文件都已返回。

## 467.3 真实源、输入和不变预算

源/配方绑定事件实际给出 source_count=140；这对应原 195 的 127 个 pin 加本次 13 个实际源。它不构成对任意未知动态 import 的一般完备性命题。该原事件正文为 17925 字节、SHA256 50c77caba4496c6ab70013e55739f9897dc84e40a539f681d6a7800553693d5d，口径为去运输前缀后的原 stdout JSON 且不含分隔 LF。

| 角色 | 真实文件 | 字节数 | SHA256 |
|---|---|---:|---|
| request | public-six-control-contracted-trace-r273-request.json | 由原 source map 绑定 | 435e90b615b1d5416794c490f7ba9493c5425e19c442de02083807dfa935a5fe |
| recipe | actual119-batch3-contracted-trace208-lambda0p001-recipe.json | 11195 | 1c738c956d9868689e0654adf143d08d4d4a06ed0b6239e6b930c2dfb4cad691 |
| workflow | .github/workflows/visible-larger-public-six-control-contracted-trace-r273.yml | 32103 | 101a84f5827b02744b0ce67dd1c7075bea05e087703985f121e15ca807dfe802 |
| reader | root_20261116_six_control_contracted_trace_r273_scalar_readout.py | 42391 | 03f9da30138b6e6f7ecd1bb81175b0dd9694d759aea31506d01bbc1019f9da53 |
| loader | geometry_20261116_original64_contracted_finite_trace_loader.mjs | 由原 source map 绑定 | 65f6e211342c608844dc91a4570ba61d1365cf72c39abea75fac792bb4d0f916 |
| flow | geometry_20261116_original64_contracted_finite_trace_flow.mjs | 由原 source map 绑定 | c29b01200953870356e155491c815cf3a6a629e3c11f60e6e42be08193f75ec7 |
| variation | geometry_20261116_original64_contracted_finite_trace_variation.mjs | 由原 source map 绑定 | e6be662ba5c795d4e3f91bbcead469482c746520b36b1d4c14a1c49b00dd2bb6 |
| contraction | geometry_20261116_recorded_factor_contracted_solve.mjs | 由原 source map 绑定 | 2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59 |

Source manifest 实际确认 loaded_root=true、loaded_split=true、original_root_and_rhs_primal_arithmetic_recovered=true、original_capacity_source_unchanged=true、no_original_disk_source_modified=true。原 root 是 cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88；原 split 是 a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372。本次 loader/flow/helper 身份不能冒旧 195 的实际浮点运算顺序。

四原数学输入来自固定历史提交 8bd267107cc8710d371f3b62c02986655ac965b0，实际恢复如下：

| 输入 | 原字节数 | SHA256 |
|---|---:|---|
| accepted | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail anchor | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| tail config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

两原 frozen geometry 输入分别为 109004 字节/563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 和 29774 字节/c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d。实际 initialCheckpoint_present=false，failed91_95_103_checkpoint_not_consumed=true，original_config_not_rewritten=true；旧 zero-J 数据仅作原初猜，不是新的非零父场。

六个控制参数是 actual119 第三批末点的原字面值：

$$
(0.41654476801167684,\ 0.23884336093393582,\ 0.5270922473095916,\
-0.13437878055563054,\ -0.005765450212224129,\ 0.4141025261683763),
\qquad \lambda=0.001.
$$

它们不继承 actual119 的当前 field/J/accepted native。当前全 $H_\ast$ 由本次原完整入口重新形成；其 112 个 binary64、896 字节身份为 ea20a63ab12f2a79d09c324bd78387da3904efda6834d03d62b339b764ee8710，negative_zero_columns=[]。本文保这个完整身份而不复制 112 个可再生数。

原执行参数维持 jac_workers=2、max_nodes=1200、material_angles=physical_angles=4096、node_heap=6144、outer_iterations=8、inner_iterations=17；native 32 轮×10 trial，solve tolerance $2\cdot10^{-9}$，collocation $10^{-6}$，BC $10^{-11}$，FD $5\cdot10^{-5}$。尾部配置仍 modes=112、depth=576、steps=12、quadrature=2048、shootingParts=8。R273 原全部 129248 行、577 node blocks、224 shape columns、112 modes、226 states及双 mean 不减；原 eta 参数为 1、factor byte cap 2147483648、末运输预留 60 秒。预算只裁剩余，不为每一请求重启 18000 秒。

## 467.4 本次初场与原离散域检查

本次形成的初场为 M=112、N=2048、699 nodes；initial_collocation_max=6.874945404161182e-6，success=false、new_coupled_finite_acceptance=false、true_nonzero_native_parent_claimed=false。不能把这个初始残差或预检 passed 解释为原 $10^{-6}$ 求解通过。

原 RMS-domain preflight 返回完整离散检查、passed=true、all_input_nodes_retained=true，历史仅 iteration=0，invalid_RMS_count=0，未新增节点。其最小 $\beta^2$ 字面记录：

| 原检查族 | 最小值 | 位置 $s$ |
|---|---:|---:|
| nodes | 0.0022538385815745743 | 2.262368580603409 |
| midpoints | 0.0022673250497816655 | 2.2641940822709667 |
| 左 RMS fraction=0.17267316464601146 | 0.002245239130675536 | 2.2629990109034166 |
| 右 RMS fraction=0.8273268353539885 | 0.0022592118408215622 | 2.2621383298889284 |

这是该有限原 node/mid/RMS 的既有范围，不是整个连续角径域证书、准确连续 C 证明或当前闭面 metric 证书。后续没有借本预检跳过原 native guard。

## 467.5 两次真实高度请求及原完整返回

高度 continuation 的 $s$ 是 $H=sH_\ast$ 的比例，既不是核心 $\lambda$，也不是闭场相位 $t$。原政策为先 $s=0$，首正增量 $1/64$，接受后增量乘 2、最大增量 $1/4$、最多 64 次请求；中间请求 jacobian=false、audit=false，最终 $s=1$ 要求原字面 $H_\ast$ 和完整 Jacobian，完整 audit 仍归原后续流程。

| 实际 call | 请求 | 原秒数 | 原返回与范围 |
|---|---|---:|---|
| 1 | $s=0$，jacobian=false，audit=false | 5774.443653623 | converged=true，residual=0，history_count=1，checkpoint=true；没有 J、没有 audit |
| 2 | $s=1/64$，jacobian=false，audit=false | 12195.315082156001 | failed=finite-trace-direction-resource-budget，lastIteration=null；没有 checkpoint、J、mean jets 或 audit |

Call1 的全零 112-height binary64 身份为 896 字节/d54f02b97ed5bc2a642756268b41d4b8f7a077e73224e1580d22436834a14db5。原 iteration0 在 06:10:44.328Z 记录 norm=0、minA=minD=1；06:10:52.573Z 返回。三个模态 jet 数组的 canonical parsed JSON 身份相同（225 字节/64c19f2662ac257bca17a036d0c4809671b09bf950df1d6c82b42461fabe7e56），但两个原 mean 没有删除：meanSlope=0.08000000000000027，meanSecond=-1.866666666666673，两 correction=0。原 checkpoint 的 canonical JSON 为 266276 字节/e4c1eb29237a65b9892fe44f3b4bc3577e2f193f38deed165d151acb4749d9be。这是有限 Fourier/depth shooting 的零形状响应；原 far Robin 不是准确旋转 collar，未 audit 的响应不是最终几何证书。

Call2 在 06:10:52.647Z 开始，所用 $H$ 的 896 字节身份为 8b29accaa5f3e7a22d81d0b0d19a55e0e6177d6ae50b5aa60245056d1ba48d31，negative_zero_columns=[]。原 predictor 实际保留，记录 maxChartCondition=385639393697279100000、maxRelativeCorrection=3.844494357362676e+252；该数只描述原初猜，不是接受门，也不能据此单独证明资源停止或数学失败的根因。请求开始时余钟为 12195.308870444 秒；09:34:07.959Z 原 worker 返回上述资源错误。

实际两次都保留 original_cold_initialization_and_live_predictor_and_fallback_retained=true；context 中 worker_last_not_assigned=true、seed_assigned=false。正高度失败后原事件明记 worker_last_may_have_advanced_and_is_not_assumed_unchanged=true，不能把零高度 checkpoint 自动冒成未经变化的可续父状态。

请求中的 jacobian=false 仅说明该次协议没有索取最终完整端点 J；原 nonlinear solver/初始化和 predictor 内部仍会形成它们所需的切向，因此不能把这些请求说成整条计算没有 with-J 工作。

原所有 trial table 的列协议保持，实际 rows=[]、count=0。Call1 的已观察 iteration0 没有 trial0–9 的记录；call2 连一次完整 iteration 也未返。**没有 trial 记录不等于十档数学拒绝**，未观察的后续 iteration/trial 或 inflight 细节不补造。

## 467.6 停止地址、缺失范围与原退出分类

原 current-R273/native completion 为 call2 给出的定位是：

- tailStage=366，tailRawCell=5，tailRawSegment=8；
- original_root_trace=null；
- error.name=Error，message=Error: finite-trace-direction-resource-budget；
- finite_trace_variation.resource_budget=true；
- stack 原文本 2072 字节，SHA256 42cca83a6bd01e6747acf5ae906a65459b296f0361d97dccef508d4f720d40e0。

必要 stack 前缀经过 resourceCheck、residualAndGramDirection、finiteRootDirection、completeFiniteRootTraceJacobian、fromCaptured、oneOriginalStep。它给出实际停止的局部方向形成位置；完整角下标、当时方向下标、该点原 root tape、$D/S/A$ 数值和完整各 engine 已访 frontier 没有返回，本文不由 stage 地址推定连续后缀全部未访。

原 Python client 抛出的消息是 Actual complete finite tail rejected，并包裹 failed=finite-trace-direction-resource-budget、residual=None、lastIteration=None。原高度分类器又记录：

> ValueError('Not an unambiguous identity-bound original mathematical refusal')

因此实际 phase=protocol-or-record-partial，resource_partial=true、complete_endpoint=false；不是原 D/S/A 拒绝，不是 residual-not-decreasing，不是证明 $s=1/64$ 没有有限尾解。外层 elapsed_seconds=18000.407521374，scientific_child_returncode=wrapper_returncode=75，phase=original-adapter-returned、budget_exhausted=false、external_signal=null，owned_group_quiescent_after_return=true。这里的外层 false 表示其自身没有宣称触发强制超时；内层完整错误仍明确为资源预算停止。

当前 R273 client 的 worker_exit_code=0，与科学 wrapper=75 不是同一退出值；它是 worker 发送错误协议并关闭后的进程记录，不能读成科学成功。client 记录两次 original_protocol_calls、elapsed_seconds=17994.624255464。两 call 的 snapshots_completed=0、directions_returned=0、original_journal_rows=0，actual_bridge_failure=null。all_observed_current_corrections=[]、correction_count=0；没有一次原完整当前系统经过 QR 或返回 R273 correction，不能拿局部 tangent 计数填补它。

## 467.7 新收缩实际执行了多少，哪些不能从计数推出

必要统计来自八个实际 engine，implementation/source tuple 全同。original_all576_stages_addressed=true 是原统计所报的 stage 布局/范围字段，不能单凭它声称第二请求全部 stage 的完整变分已经返回。计数是累计实际调用，不是不同科学状态的数目。

| 原累计计数 | call1 返回时 | call2 停止后的最终值 |
|---|---:|---:|
| root_returns | 27772 | 45434 |
| zero_update_returns | 27772 | 27772 |
| normal_returns | 27772 | 45434 |
| fallback_returns | 0 | 0 |
| original_root_evaluations | 27772 | 101992 |
| original_line_trials | 0 | 28279 |
| differentiated_accepted_updates | 0 | 28278 |
| complete_local_jacobians | 27772 | 45433 |

最终 return_iteration_histogram 的非零档为：0 次更新 27772、1 次 8966、2 次 6775、3 次 1921，4–29 档均 0。该原完整 30 档已读；不把最后一个未完成 local Jacobian 补为成功。root_returns 与 complete_local_jacobians 相差 1，是当前已返回字段的事实；这不提供未返角/方向的完整定位。

| 原收缩累计计数 | 实际值 |
|---|---:|
| calls_started / calls_completed | 28278 / 28278 |
| preassemblies_started / preassemblies_completed | 28278 / 28278 |
| contracted_updates_completed | 28278 |
| complete_direction_columns_returned | 6334272 |
| exact_backsolve_defect_components | 3195414 |
| exact_nonzero_backsolve_defect_components | 3193204 |
| backsolve_defect_projection_changed_components | 3164179 |
| nonzero_backsolve_defect_projection_lost_components | 0 |
| backsolve_defect_projection_overflow_components | 0 |
| exact_zero_backsolve_defect_updates | 0 |
| explicit_original_fallbacks_started / completed | 0 / 0 |

actual_fallback_reason_counts={}，missing_counter_scopes=[]，engines_with_unfinished_solve_or_last_fallback=[]。后一字段仅表示该选择器没有观察到尚未返回的收缩调用或最后 fallback；它不能覆盖收缩以外正在执行的 residual/Gram 方向形成，实际该处已经资源停止。各更新的完整 fallback 历史未记录，不从累计“0”重建科学数组。

R465 的准确条件对象是每个已记录基点的常缺陷局部模型：

$$
E_0=R_0R_0^\top-C_0,\quad a_0=R_0z_0-F_0,\quad b_0=R_0^\top s_0-z_0,
$$
$$
R(C)=\operatorname{chol}(C+E_0),\quad z=R^{-1}(F+a_0),
\quad s=R^{-\top}(z+b_0).
$$

本次实际始终保留完整 225 literal Gram 槽及原 $\sqrt2$ 权，使用实际因子两次回代；没有换成理想 $C^{-1}$。零更新 local root 仍用原195的 $D t$ 路径，没有调用新收缩。一般实际缺陷的导数并未被证明为零；常缺陷是已声明局部模型的定义。实际二进制运算顺序与旧195不同，backsolve 缺陷虽先精确形成，后续投影及收缩舍入误差未得到严格上界，原195 factor loop 只是明确数值 fallback。

这些真实计数支持“新实现确实被调用，且保留非零 backsolve 缺陷”这一有限结论；不支持当前完整 Jacobian 已通过、原 IEEE 运算严格导数已证、邻域 branch 不变、与195逐词相同，或已测得端到端加速。与 [R412](R412-actual195-finite-root-tangent-resource-partial-before-positive-current-J.md) 的 stage368 不能作受控性能比较：新浮点顺序可改变后续方向/路径，本次仍未完成首个正高度当前评价。

## 467.8 完整未付的后续门

原 adapter 的新耦合接受和完整闭面标志均为 false。必要正文中 boundary_FD、boundary_FD_groups、original_full_DN、accepted_result、original_outer_history、full_result_identity 全为 null；all_original_full_DN_evaluations=[]，all_original_banded_solve_reports=[]。这里不是把未起项判作失败不等式，而是没有该实际结果。

未付范围包括首正 $H$ 的完整 nonlinear iteration/原十档试步、当前 R273 全行系统与 QR/correction、后续高度请求直到 $s=1$、端点 fresh 338×112 Jacobian 及两个 mean、原双组 FD/阈值、后续完整 prefix/full-DN 迭代、最终 native/physical audit、同一场的所有连续域/几何/metric/reach/held 与非刚性责任。不能从 call1 的零形状响应、局部 full-column 计数或 report 绿色状态继承这些门。

本次没有新增更小高度、额外 secant/方向、影子数值对拍、fixture 或独立审计调用。原 scope 中可能的后续资源/数学责任保持原未付，本文不给虚构完成保证或机器精度结论。

## 467.9 必要原文件身份与读取边界

下列是真实临时原件的 byte/SHA，来源于这次单份必要正文。哈希不是文件内容的可逆替代；本文没有从它们恢复已清科学数据。

| 原临时文件（execution 相对路径） | 字节数 | SHA256 |
|---|---:|---|
| process-status.json | 6736 | 4da0ee5bfa5e34ff8f98b970943d3fc7819d29fb00445de40981314759472bf3 |
| science/adapter-status.json | 22037 | fed1eb8bbf7ba2c16637f37bf1009909ecf7c26689a8df96ab50c30721b06c87 |
| science/initial-guess/prepared.json.gz | 2475936 | 728a093cab5b2684412ba5adfb3d44940759f46855471bad6e2daaba093926c4 |
| science/initial-guess/RMS-domain-preflight.json | 1523 | 06d455bf2a52e6e083b51dd94917f2713ff7212069c232ff976a676d43c8d641 |
| science/full-DN/true-tail_0001.json.gz | 9975 | 70f02afa0bb30fb9314dc983d3a1e61320d6611159dd0015beb6818871f65bb8 |
| science/full-DN/true-tail_0002.json.gz | 8461 | 837fb2eb051ebd7df8a6fb16d813494686e02950e62e98474bfcd35b528dd611 |
| science/full-DN/true-tail_trace.jsonl | 5416 | fc5d583b3a793222d936df10895a43bdd74ce4de6ccae3b6a730fbcc170c3b25 |
| science/height-path/height-path-status.json | 16161 | 8102cbc62d9db0ef4fd863f9eb18f9491c6bedaefdef3a5568ab66e0c1ce4700 |
| science/full-DN/true-tail-contracted-trace-r273/live-current-corrections-summary.json | 45937 | 2a8dea634c89cbaf08bce047b247c5d516c5feae47f7f626044d3e304c2dca0a |
| science/full-DN/true-tail-contracted-trace-r273/finite-trace-source-manifest.json | 7148 | 3cc649f5297c5acc84b2e9790c0f80c598baabbef7deaa2500e34ec8507a389c |
| science/full-DN/true-tail-contracted-trace-r273/call-0001/finite-trace-native-return.json | 20338 | 63641d039e61d9ca2d7c9ad0a0378fb80f4165ae910244b5e300155ecdd202b1 |
| science/full-DN/true-tail-contracted-trace-r273/call-0002/finite-trace-native-return.json | 23635 | 25158fcef8f30f6fbcee0ccda09c20f85cfdeeaa13bc33679dd101e95db563dd |

原 true-tail_trace.jsonl 有 12 条实际事件；两个请求各原 trace slice 分别 6 条和 5 条，另有 backend 标识。原 native stderr 为 0 字节。原 science-stdout-stderr.log 是 13867 字节/65c8707d7f46f07a491c10f66773cfac11dd10caa02ac877cb75c23bd6a8f224；该文件没有整体另取。已经获取的 compute log 含两次完整 request-returned JSON，本文完整读取其原 Python 异常和分类 traceback，而没有把必要摘要中 800/1600 字符的前缀误称完整原错误文本。

原选择器对大 nested arrays、科学 state/root tape/精确逐行 ledger 和部分长错误仍只留原身份及明确必要前缀；canonical_parsed_JSON 身份不是原 gzip/JSON 序列化字节身份。两个协议原 gzip 身份和必要 scalar/json 身份始终分列。完整 112 个 $H_\ast$ 已存在原必要正文，但本结论只保原整体身份与真实两次 requested-H 身份，不再复制科学向量。

## 467.10 实际规则同步、静止与删除结局

原 rules runner 保持源 3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde，周期 2700 秒，实际完成 round0–6 共 7 次。根 README 基线为 21bd547f56590b7f2dd279d0297efb289a9b2783，主题 README 为 bff8aea253a9e6a7a4fac28d810ac454c5499fec。最后一次真实同步时间 09:04:26 UTC，读 origin/main=8bb2e07a22a71b457b6080a342a923d05c6b1bea，发布 c8ff4027859d5befebd92a9d5b4c498beccd4194。原结果 README_change=null、science_terminated_for_actual_rule_change=false、periodic_sync_failures=[]、scientific_checkout_modified=false、原 argv/budget 保持。

读回前后 scientific owner 都 quiescent=true，已登记 group 的 members/live/errors 全空，没有发信号；同一 process-status 原件为 6736 字节/4da0ee5bfa5e34ff8f98b970943d3fc7819d29fb00445de40981314759472bf3。规则父进程原 receipt 为 533 字节/09affd5a1914f88411dd7cd8c7825106b9ff92f9cc1075fe9d17c42d2ceddd88，pid=3301、start_ticks=19070、pgid=sid=2149；当前 PID 观察 null，原同一进程已不在。没有要求共享 runner PGID 全空，也没有向该共享组发信号。

Compute 物理行 853 的真正 cleanup 事件记录：

- schema=request208-conditional-owned-cleanup-v1；
- scalar_step_outcome=success，complete_readback_and_quiescence_authorized=true；
- readback_marker_sha256=ce77d40326337e23dd2da04fcb6f7ea74e268025e741a2b456ab85970d3c1074；
- original_rules_parent_quiescent=true；
- removed=true，no_artifact_release_or_git_raw_upload=true。

清理前源码实际核 marker 的 run/source/request/recipe/reader/summary 身份，并再次观察 scientific owner 与规则父 PID/start-time。删除对象只为本次 RUNNER_TEMP 下 visible-original64-contracted-trace208。Rules 结果较早记录的 partial_scientific_files_not_removed=true 是其自己返回时的责任，不能盖过随后这个已明确发生的删除事件。当前没有可续用的原温场/矩阵/因子；后继若执行必须按其真实新入口重新形成，不能从本文 SHA 伪恢复。

## 467.11 可复核结论的范围

原 [R411](R411-original64-finite-root-trace-matched-variation-and-full-return.md) 给有限 root trace 与完整方向责任，[R465](R465-recorded-factor-backsolve-defect-and-complete-column-contraction.md) 给明确常缺陷名义模型；本次没有扩大这些条件定理。实际208已证明的是公开来源和协议中的执行事实：新收缩与显式缺陷投影确有调用，零高度请求返回，首个正高度仍在原总钟中止于局部方向形成，原后续完整门未返；必要读回完整且实际静止删除已发生。

这份结论不更改 request208、任何已运行科学源、原预算或阈值；不把资源 partial 升格为数学无解，也不以新更强命题作为原求解或 README 责任的额外前门。
