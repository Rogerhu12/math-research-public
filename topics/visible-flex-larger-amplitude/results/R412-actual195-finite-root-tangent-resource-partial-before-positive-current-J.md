# R412：actual195 有限 root 轨迹切向在首个正高度完整 J 返回前资源停止

作者：ChatGPT（AI；exact_refinement），2026-11-16。

**可信度：数值证据（本次公开 Actions 的有限输出）；执行范围和未完成责任据原记录与绑定源码确认。** 零高度请求返回原 norm=0；首个正高度请求在切向形成中触及原 18,000 秒期限。正高度完整 current J、R273 校正、原试步、FD、完整 fullDN 与最后物理审计均未完成。本节不是非零 native 接受、严格舍入误差证书或准确曲面存在性证明。

## 412.1 实际执行及唯一原读回

实际源提交为 4ad7fb771218585af1091c9d322c9d61b64a949c；公开 [run 43771125613](https://github.com/Rogerhu12/math-research-public/actions/runs/43771125613)，attempt 1。compute job 132987043859 为 failure；report job 133078432173 为 success。compute 的科学步骤 10 失败，必要读回步骤 11 与清理步骤 12 均成功。report 的绿色只表明报告完成。

两 job 的官方 connector 日志各取一次。下表前两项是 connector 返回 UTF-8 文本的字节身份，不冒称 HTTP 原响应、压缩日志包或 GitHub 内部存储的字节身份。

| 原件与口径 | bytes | SHA-256 |
|---|---:|---|
| compute connector 返回文本 | 158984 | 4a4359484aa30db04ad8a3b2c9f750e94f13f081e0141cabea107a5665751b03 |
| report connector 返回文本 | 88836 | 47473f2fa81028c7aa7447a925ac8448e8d0edac4f85530057d5b7fa11d37247 |
| 两 job 唯一真实 necessary 帧正文，不含分隔 LF | 41421 | e43d25f621c9e5542a442dc3d3ea42a454b4e2036036722b383e1fb844068229 |
| 原 Actions science-stdout-stderr.log | 12921 | 346429b6f5fc8fcb2bca628d2a70cbd4ebba7a5c1a8a6647b9e15b8c7d33d43b |
| 原 Actions 全 native trace，12 条 | 5392 | 3283703a18322307f912e41eac47707ba96fb6b41a7e330011e76c310769bb47 |

真实帧名为 BEGIN_REQUEST195_FINITE_TRACE_R273_NECESSARY_SUMMARY / END_REQUEST195_FINITE_TRACE_R273_NECESSARY_SUMMARY。解析视图只去除每物理行行首的单个运输 BOM 与锚定 timestamp，不更改所报原文本身份；排除带 ANSI 的命令回显。compute 与 report 正文逐字相等，不以两个独立科学执行计数。

necessary 的 schema 为 request195-original64-finite-trace-r273-necessary-readback-v1，summary_complete=true、transport_complete=true、errors=[]。其完整小正文已读；大 root tapes、节点数组、精确行账及完整内部对象没有重新导出。仅 canonical parsed JSON 身份的字段不冒充原序列化文件 SHA。本节只保必要结论、参数及来源，不把可再生现场提交 Git 或 Release。

## 412.2 本次对象、原方法和新切向的边界

request 是 public-six-control-finite-trace-r273-request.json，SHA fd65aeff4517f481f1a78ad23c2b3514c9df6ec58c433d693788de5df000787b；recipe 是 actual119-batch3-finite-trace195-lambda0p001-recipe.json，SHA 70145aca5431029987f5c79d9fcd9830e5a4112c1e17d5626a9a2a139e93f124；workflow 是 visible-larger-public-six-control-finite-trace-r273.yml，SHA 0a18de732a08670b8a65c4ab61436655396066081aa7fba057fbddc9c507e4c2。必要 reader SHA 为 b6d22546b7258e0dc23f016238d7e0ed4769fa35f602d3db503f49f6ca45bbd9。

原四输入如下；原两份几何 ready、78 份恢复来源及全部 127 pin 仍由该完整 request 绑定。它们不是本次已接受的非零尾锚。

| 输入 | bytes | SHA-256 |
|---|---:|---|
| accepted | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail_anchor | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| tail_config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

六参数原字面为
$$
p=(0.41654476801167684,\ 0.23884336093393582,\ 0.5270922473095916,\
-0.13437878055563054,\ -0.005765450212224129,\ 0.4141025261683763),
\qquad \lambda=0.001.
$$
这是从上述原来源重新构成的 699 节点初猜，不是 actual172 末状态续接。初始 collocation max 为 6.8749454041621035e-6；该值不是已达 1e-6 的结论。

保留 M=112、N=2048、576 尾 stage、每普通段 steps=12、224 形状列、226 完整状态及双 mean。native 原门为 32 轮、每轮 10 档、严格残差下降与原 D/S/A，容差 2e-9；原外层最多 8 轮、17 档、collocation 1e-6、BC 1e-11、boundary FD 5e-5 均未减。material/physical 角数各 4096，max_nodes=1200，jac_workers=2，科学期限 18000 秒，science step 330 分钟、compute job 350 分钟。

新切向对象由 [R411](R411-original64-finite-root-trace-matched-variation-and-full-return.md) 及 [完整195接口](../notes/2026-11-15-request195-original64-finite-trace-r273-complete112-interface.md) 定义：保原 noJ primal 的有限 root/RK 字词与分支决定，对这次成功有限 root trace 的准确实表达式作数值线性化。它逐式传播原残差 F、独立 225 个 Gram cosine moment、实际 Cholesky 因子及两次三角回代；不把 Gram 直接认作 F 的导数，不以 C 逆替换实际因子链。零更新 root 的导数为初值映射导数。原成功 normal/fallback 返回含 0..29 次接受更新；第 30 次接受更新可能在原循环结束后伴随 iteration-limit 抛错，未冒作成功分支。

本次原 source manifest 实际报告：

| 运行来源 | SHA-256 |
|---|---|
| 新 variation kernel | 742ab15a2168084167eeab9879a074ee1cd586d33f324e837223134a8cbf9705 |
| 新 loader | 55b2a4a344ae2eb7d78f26b7954b20f9cbe4e4969588bf3a236e7828d6f299ae |
| 原 noJ primal + 新 trace flow | a7a90668a7d2f4df93e0bd03d665f439dab2fb2461bedf544725cd01c2a7b470 |
| 原 root | cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88 |
| 原 split | a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372 |
| 实际观测 root | ff1f1f7987ae6280020bbd16d91235903f9f59ec35e5fae670271edc2bc67fff |
| 实际 matched split | 22acf3d75360ba002c8d4f5bdedaa1f7201b5e2faec83c882c91bd6fe3977ae5 |

loaded_root、loaded_split、original_root_and_rhs_primal_arithmetic_recovered、original_capacity_source_unchanged、no_original_disk_source_modified 都为 true。root 原 policy 为 iterations=30、backtracks=20、stop=8e-14、fallback=5e-12。新源没有逐角 primal-shadow 字词相等的额外通过门，没有 fixture；方向的实际非有限错误与来源/尺寸核对仍按原声明处理。

这组身份及实际计数证明新路径被执行，不证明其数值误差界，也不证明邻域内 root 分支恒定、IEEE 舍入映射可微，或本次新 J 已通过 FD。

## 412.3 原有限预检通过，完整高度未裁模态

原 nodes、midpoint、左右 Lobatto 查询均执行，complete_preflight_passed=true，原全部节点保留、无新增 preflight 节点、invalid_RMS_points=0。原最小 beta² 为：

| 查询族 | 原最小 beta² |
|---|---:|
| nodes | 0.0022538385815712436 |
| midpoint fraction=0.5 | 0.002267325049764346 |
| left fraction=0.17267316464601146 | 0.002245239130645116 |
| right fraction=0.8273268353539885 | 0.002259211840830444 |

这是有限查询域结果；不推全连续域或闭面度量结论。实际准备文件为 2475684 B / a747c7dc9acc4fb26e1179e765d3ee4e0685d8f2dab11f7abdb1373f50faa69f。

请求的 H* 为全部 112 binary64 字词，未把高模清零。前 3 项为 0.0008954476172889355、5.023344896215423e-7、-2.0011103217478445e-7；其余原项在原 necessary 中完整保留。下表按原 little-endian float64、shape=[112]、896 bytes 身份：

| 请求向量 | SHA-256 |
|---|---|
| 原完整 H* | d19e25eabad7f2c84ecdd10580caee1c3b41ef9d1e0a1a3ae07c58486277eced |
| call 1 零向量 | d54f02b97ed5bc2a642756268b41d4b8f7a077e73224e1580d22436834a14db5 |
| call 2，s=1/64 的实际全向量 | fb6da818e40bcdaa0bc57ceb9a86d5ae2845132054389a2eac73ea866283a032 |

三者 negative_zero_columns=[]。上述精确身份只是原请求向量，不被当作被删现场的可续状态。

## 412.4 两个实际请求及首个正高度的真实停止点

| 字段 | call 1 | call 2 |
|---|---|---|
| s | 0 | 1/64 |
| requested jacobian / audit | false / false | false / false |
| 原耗时（秒） | 5063.5455199240005 | 12912.70058027 |
| 原 response | converged=true、residual=0 | failed=Error: finite-trace-direction-resource-budget |
| 原 iteration 事件数 | 1（iteration=0） | 0 |
| 原 trial 数 | 0 | 0 |
| checkpoint | 有 | 无 |
| 最后完整 response J / audit | 无 / 无 | 无 / 无 |
| 高度路径接受 | true | false，resource partial |

中间请求 jacobian=false 只决定是否返回最终边界 response J；它不跳过原 Newton 求解内部 current withJ。零请求实际 iteration=0 的 norm=0、minA=1、minD=1，原返回 actual_nonlinear_solve=true、finite_tail_only=true。返回的 112 height/slope/second 模态均为零；meanSlope=0.08000000000000027、meanSecond=-1.866666666666673、两 mean correction=0。没有以零响应称完整非零耦合 fullDN 已接受。

两原 response 文件分别为：

| 原文件 | bytes | SHA-256 |
|---|---:|---|
| true-tail_0001.json.gz | 9903 | cc18c53ae52185e54544eba3310869f616756cfeb361d72f87d98e820884edb8 |
| true-tail_0002.json.gz | 8387 | d2c186891ec362ec57417830202548bf03117f4d7bb235e31c9ab6b66d1d6b83 |
| call-0001/finite-trace-native-return.json | 9400 | 8e750d687b40c2f484e445b1115e5f848411fd6ba0cae981bd32fe70ca5e41f2 |
| call-0002/finite-trace-native-return.json | 11776 | b84011bcf3ccae9f2b00e5965781d1e98bc7f25e842bc926214048c5197831ae |

call 2 保原零父的 full nonlinear shooting tangent warm。原 maxChartCondition=385639393697279100000，maxRelativeCorrection=3.844494357362678e+252。原事件 scope 明示只是初猜，成功仍由原 nonlinear residual/guards 决定。本次不能由这些巨大数值证明唯一失败原因或构成新拒绝门。

实际 failure 给出 tailStage=368、tailRawCell=5、tailRawSegment=7，finite_trace_variation.resource_budget=true，original_root_trace=null。原错误链在 resourceCheck → differentiatedOriginalSolve → finiteRootDirection → completeFiniteRootTraceJacobian → fromCaptured → oneOriginalStep → flowStateWithJacobian。被保存错误文本 1974 B / 930f30a2b73554024ec115ee917c92bfd1b9f780b7e347e3f63dea1ed836da8d；necessary 只保其必要前缀和完整身份，不声称全栈正文已返。

由该实际地址和原 resourceCheck 可确定：本次在正高度 current withJ 的有限 trace 切向过程中耗尽共同 deadline。call 2 尚未产生 iteration 事件、lastIteration=null，没有完整 current J 及当前 residual 返回，没有 R273 snapshots/校正方向提交，更没有原十档试步。Stage 368 是原异常地址；不能推 stage 369..575 已算，不能把并行 stage 的已完成集合凭此猜成连续前缀，也不虚构具体 angle、因子索引或停止的列。

原高度路径最后记录 phase=protocol-or-record-partial、resource_partial=true、last_converged_s=0、last_converged_call=1，完整 endpoint=false。已有 2 个带 response 的请求，不是 2 个接受。python 的 FloatingPointError 包装含同一资源错误；其后 binding_or_protocol_exception 为 “Not an unambiguous identity-bound original mathematical refusal”。这是拒绝把资源事件当数学拒绝的分类结果，不是另一个 D/S/A 数学事实，也没有据此自动缩小 s 继续试验。

有一个易误读字段必须单独说明：source_failure_context.cold_first_complete_withJ_evaluate_did_not_return_by_pinned_source=false。其原代码只检测“冷首求值、特定 momentum D/S/A 字符串、无 warm/iteration/trial”的狭窄合取。本次有 warm 且错误为资源期限，故该狭窄标记为 false；它不表示正高度完整 withJ 已返回。本节按实际 failure/iteration/response 判定，不能由该字段反推已完成。

## 412.5 全 224/226 责任及累计计数的正确解释

原 8 个 engine 的 metadata 计数已读。下列第二列是 call 1 结束时累计值，第三列是 call 2 失败时累计值，**包含前一请求，不是第二请求独立差值**。

| 原计数名 | call 1 后 | call 2 failure 时 |
|---|---:|---:|
| root_returns | 27772 | 45540 |
| zero_update_returns | 27772 | 27772 |
| normal_returns | 27772 | 45540 |
| fallback_returns | 0 | 0 |
| original_root_evaluations | 27772 | 102308 |
| original_line_trials | 0 | 28384 |
| differentiated_accepted_updates | 0 | 28383 |
| complete_local_jacobians | 27772 | 45539 |

call 1 的返回迭代 histogram 为 n=0:27772，其余 n=1..29 为 0；call 2 failure 时为 n=0:27772、n=1:9072、n=2:6776、n=3:1920，其余为 0。这里的 original_line_trials 是原局部 root 内部的最多20档搜索，不是 native 的每轮10档试步。native 的 actual_original_trial_count 始终为 0，两种账不能混合。

两次统计 actual_engine_count=8，indices=0..7，missing_counter_scopes=[]，original_all576_stages_addressed=true。后者记录完整 stage 地址的配置/收集范围，不等于当前正高度全部576段完成，更不等于全部原 RK 步、最终338×112 J 或物理审计完成。计数是实际调用次数而非互异状态个数，不由它反造全 stage 完成清单。

从源码也能解释 root_returns=45540 而 complete_local_jacobians=45539 的记账顺序：root 返回分支进入 finiteRootDirection 时先递增前者，完整 RHS 切向形成后才递增后者。此处只是记账顺序和实际不完整 local evaluation，不把差 1 推成漏掉一个数学模态。

实现 groups 的实际 local field 源 SHA 为 165599fc678d14ded320a49f7b97363717c0eaa398138e4a6600e44dfa1a9f45；stage variation SHA 为 03572f3bf6e7c186bd8b181f7ac1653c402e488ad44ae70079e64fa93cdc5526；原 noJ RK SHA 为 0538526dd947cc2d658656b586b5f78f63844b036afa49f5fcefa51a7d927d1a。它们与运行 manifest 一同确定实际路径。

R273 原计划仍是当前完整 129248 行、577 penalty node blocks、224 形状列、226 含 mean 状态，eta=1、原 exact-workers=2、factor上限2GiB；原 QR 9b951f95 与 dyadic 0bc8f978 未换。实际 current_R273.started=true 只表示 hook/来源目录已启动；call 1 snapshots_completed=0、directions_returned=0，call 2 对应字段 null，两次 original_journal_rows=0，all_observed_current_corrections=[]、correction_count=0、all_original_banded_solve_reports=[]。不能据 started、目录或 call 1 的 summary 文件名声称已形成一个 R273 校正。

## 412.6 原预算、规则监视、必要读回与实际清理

原 rules runner 从 2026-11-15 22:47:12 UTC 至 2026-11-16 03:47:12 UTC；sync_rounds_started=7，periodic_sync_failures=[]、README_change=null、science_terminated_for_actual_rule_change=false、scientific_checkout_modified=false，原 argv 和预算保留。

实际 science process：

- phase=wall-clock-budget-partial；
- scientific_wall_clock_seconds=18000，elapsed_seconds=18000.163997215；
- budget_exhausted=true，external_signal=null；
- scientific_child_returncode=-15，wrapper_returncode=124；
- owned_group_quiescent_after_return=true。

这不是 GitHub 的350分钟 job硬杀，也不是本轮 README 变化中断。原资源检查先留下切向失败地址/response，外围deadline受控停止，故数学未付范围和工程退出有各自记录。原 rules result 的 partial_scientific_files_not_removed=true 表示规则runner当时不擅删现场；之后独立必要读回/cleanup确实执行，不应误把前一标记解释成最终保留 raw。

readback 前后对同一 process-status.json（5387 B / fa7a1c8c0535d89359a5bdc0d5c683a4a3cc7362d336837fc6b235a90b3ed686）检查，launcher_reap_claim=true；两次 group 的 members/live/errors 均空，quiescent=true，signals=[]，没有为清理额外信号原共享 rules PGID。原 rules parent 另外返回静止回执。

实际 2026-11-16T03:47:13.6632365Z 的 request195-conditional-owned-cleanup-v1 事件明确：

- complete_readback_and_quiescence_authorized=true；
- scalar_step_outcome=success、original_rules_parent_quiescent=true；
- removed=true；
- readback marker SHA 929c8e518d7f0b2ca14e84ab9467eb5670310317f79e18d8ac8afc50baf6f7d7；
- 原 rules parent receipt SHA b0163cce6d32958fe76b95c5332bd1166c53ab5881110cfb27be3cddca5841a4；
- no_artifact_release_or_git_raw_upload=true，cleanup_is_not_an_original_scientific_acceptance_gate=true。

因此本次是真实必要读回及 owner/parent 静止后删除 namespace。以后只能从脚本、参数和原来源重新计算，不能从 checkpoint SHA 伪续已删的 zero/warm/current 状态。

## 412.7 已付范围、未付范围和下一具体障碍

| 责任 | 本次实际状态 |
|---|---|
| 四原输入、两 ready、127 source pin、原六参数/λ | 已绑定并执行 |
| 原699节点及有限 RHS/RMS 域预检 | 原有限查询通过 |
| 原全112 H 请求，无高模裁剪 | 零与 s=1/64 两请求都有原字词身份 |
| 原 noJ primal 轨迹 + 新有限 trace 切向入口 | 已实际运行；原 branch counters 有非零更新 |
| 零 H 原 native 求解 | 原 response norm=0；无最终 J/audit 请求 |
| 首个正 H 当前完整576阶段 withJ/residual | 未返；stage368 切向资源停止 |
| 当前全行 R273 correction | 0 个已提交 |
| native 原每轮10档试步 | 0 条；无数学回溯拒绝记录 |
| s=1 完整 H* endpoint | 未起 |
| 三方向/三步边界FD及原全DN | 未起，原字段 null/空 |
| 最终338×112完整边界J、双mean及物理audit | 未付，不由局部计数替代 |
| 非零完整Cartesian闭面与课题完成标准 | 未付 |

adapter.success=false、new_coupled_finite_acceptance=false、full_Cartesian_closed_surface=false；height_path.original_full_DN_accepted=false、final_original_audit_done_by_bootstrap=false。原 boundary_FD、boundary_FD_groups、original_full_DN、accepted_result、original_outer_history、full_result_identity 都为 null，fullDN预检亦 null。不存在可给下游的非零接受父。

[R369](R369-actual172-current-H-complete-secant-and-trial-decomposition.md) 的 finite_secant 与当时模型方向差距，不能由本次资源停止证明已解决或已否定。195 没有得到正高度完整 J，未形成方向，未观察该方向的实际小步响应，因此既不能把此次失败归为原 finite-root 隐式 J 缺口，也不能归为 D/S/A、roundoff、真实 pole、某个未见 root分支或 warm唯一原因。

实际优先障碍是**完整有限 trace 切向尚未在原单次预算内形成**。此处不以盲增预算、减模态/列、删除 means 或更换接受门解决。源码中 residualAndGramDirection 已把224列作为同一批处理，fromCaptured 也没有重跑原 root/RHS；所以“每列重复求一遍 primal”不是这份195实现的正确描述。其实际昂贵正文仍包含全113×113因子的224方向微分、两个完整三角回代、全角 flux 及每个原 RK stage 的226×224传播。下一优化须针对这些明确环节保持原 noJ primal、原选中有限root轨迹、全部列/means和最终边界责任；如改变浮点累加顺序，须独立声明数值实现与来源，不能凭准确实恒等式声称逐字相同或误差已证。

本次没有逐函数计时，因此不能从总耗时指定唯一热点，更不能预估某一改写可在6小时内完成。已有零请求5063.5455秒及正请求12912.7006秒仍未返的真实数据足以否定“本次已付完整正高度方向”的说法，也给下一完整实现明确的资源约束。所有后继科学仍只在新的公开Actions现场执行，原195源与结果不改。

## 412.8 复现和证据边界

复现使用固定 source 4ad7fb771218585af1091c9d322c9d61b64a949c 的完整 request、recipe、workflow、127 pin和四输入/两ready。必要输出按本节41421B身份复核；原大数组只在当次 Actions 临时目录存在，本节不补造已删逐 stage/逐root/逐角清单。

本结论只做原文本读取、来源/字节身份、原控制流和整数 metadata 的检查，没有本地科学求值、编译、AST、对拍、fixture 或新 FD。新的完整方向/物理接受必须来自后继实际原输出，不能由本节的受控停止与成功传输替代。
