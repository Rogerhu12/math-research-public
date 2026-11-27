# 完整 Fejér 求解的真实数学标量进度：独立只读观测入口

日期：2026-11-27。状态：全源、完整两模式参数与显示对应已经构造并保护，未执行该独立入口。现有 run12 和已冻结 N/M/J 科学源均未修改。本项不增加科学预审、fixture 或新的数值准入门。

## 1. 已有进度的具体缺口

当前完整不可写点族的 original closure progress 能报告 root phase、点 SHA、角缓存、请求与原计算／命中计数，但不包含真实已经算出的 Phi、完整有限 metric 观测最大 Gram 残差或原完整几何 screen 的违反量。即使原统计函数已经返回，长后继角计算期间仍无法从这种进度判断初始场与实际试点的数值。

本版本由完整阶段 owner 族派生，只追加已完成操作的标量观测。新下层、方程、解法和预算不变；完整 driver/launcher/reader 是明确的新文件与新 whole source SHA，旧完整程序保留。

新观测的唯一数学值来源是**原程序已返回的** statistics、geometry、实际 trial decision 与实际 checkpoint/report save。没有增加 F、J、J*、root、积分或原统计函数调用。完整点 hash 读取与小 JSON I/O 属新增观测成本；本版真实 total wall time自然包含它们，不能说零 CPU/IO 成本或预报加速。

## 2. 完整 source 接线

母体是阶段 owner 完整 source family：driver `050a6067fbb2fb4d054a97bf73899cfe5d4629197e42c39f00846a1f6a63b268`、launcher `8fed7b6a7ff6c988ee2240a4193f9440fd91ef158e5ac47d6248868d4e19214c`、reader `42e198f8d886641048059c3cdd8110b8bc3d000cdf350da1de54ac4bb83014a0`。完整母体总表为 `fixed-fejer-stage-point-complete-delivery.json`，74,078 B，`f0497fee9a867ea1b6aee90f7d15ccd86415e7bcd3aee64e597e18afc7424d04`。

新增一个标准库 helper role `scalar_progress`，并递归更新三上层源。原 119 个 complete source pair 全部原样保留，新表 120 项。normal、不可写点 closure、阶段 owner、adjacent、解析 frame/J3、C1、校准、base/seed/Q/reference、memory/rows/history transfer 均原 whole 字节复用。原完整同目标父模式与未知历史义务全部保持。

| role | 完整文件 | 字节 | SHA256 | Git blob |
|---|---|---:|---|---|
| scalar_progress | `fixed_fejer_actual_mathematical_progress.py` | 26595 | `bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391` | `509d502e13511c3746ba4647a6be32fce165bb61` |
| driver | `fullclosed_fixed_fejer_stage_point_observed_so3_qp.py` | 95632 | `8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d` | `3a537a58e82f152c78d0408c8b2c5f4403af1106` |
| launcher | `launch_fixed_fejer_stage_point_observed_actions.py` | 21794 | `ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa` | `1848230bd8a4f2dbbb4e4281e84d20d3d33ac531` |
| reader | `read_fixed_fejer_stage_point_observed_so3_report.py` | 98763 | `c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f` | `f37f64e9da226b40cc836c1b5f139eec342db764` |

新 report schema 是 `complete-fixed-fejer-stage-point-observed-material-envelope-SO3-QP-v1`；新 readout schema 是 `actual-fixed-fejer-stage-point-observed-envelope-SO3-readout-v1`。数学 normal/model schema 与全部 source-bound working policy 原样。增加的 observer policy属于输出归因，不改变 g、完整控制词、32-stage partition 或选择方程。

## 3. 真实挂点与执行顺序

完整 caller 在原结果已经返回后追加下列观测：

| 原操作 | 新读取的既有结果 | 点归属 |
|---|---|---|
| initial statistics 返回 | 原 Phi、全原 finite metric Gram 最大值及 determinant/E 标量 | 传入该函数的完整 initial x |
| initial geometry 返回 | 原 complete/passed、maximum_physical_g、必要 reach 及既有几何标量 | 同次 scan 的 caller x |
| 每轮 current geometry 返回 | 新永久集合上重新筛过的原 current geometry | 该轮原 current x |
| trial 创建 | 原 index、alpha、phase、serial；统计／几何先设 null | 此次 candidate |
| trial statistics 返回 | 原该次统计；不推断接受 | 此次 candidate |
| trial geometry 返回 | 原该次 screen；未调用时保 null | 此次 candidate |
| trial decision 已写入原 trials | 原 accepted bool 与实际错误字段 | 同一个 candidate |
| accepted checkpoint 已返回 | 原 accepted_statistics、accepted_geometry、accepted_bundle 及真实 phase/serial | 已复制给 current 的原 x |
| final scan/statistics 返回 | 原最后全部筛／统计值 | 原 final x |
| 原 save_report | 保存同点标量 snapshot；原 report 写成功后才写“report saved”进度 | 各记录保自己的点，不借最后根缓存 |

原 `statistics`、`remember`、`scan`、`physical_violation` 的完整函数文本逐字相同。完整 q.residual、statistics、scan、QP solve、q.save、coordinates.lift 和 screen.build_rows 调用及其科学顺序均保。构造器用完整 before/after 片段重放；去掉新增挂点并还原 source/schema 后可逐字还原整原 driver。简单调用次数比较只是补充，不是替代整 source 的依据。

这一版本的 save_report 科学后缀**有明确的新只读挂点**，不冒称仍等于原阶段 owner 20,121 B 的 suffix SHA。原数值语句保；本次新增内容和完整新字节由全 source 构造器记录。

## 4. 点、状态与非有限值

每次挂点在原操作返回后，由完整 caller 调用原 `meridian.array_sha(point)` 取得真实完整点 digest。helper 只接受这个已绑定字符串，不使用最后 root cache 的点 SHA 来替代 caller point，也不重新读取或修改科学数组。

完整统计对象仅新增 `actual_scalar_progress_binding` 元数据；其数值字段照读原 spectral objective 与原统计，不重算。几何对象同样新增自己的完整 scalar binding；若原 complete geometry 自带点 SHA 与 caller point 不符，观测记录失败，不把另一点混入。partial screen 中的正违反量始终为 null；完整且 g 为有限数时，才按原 physical_violation 语义取 max(0,g)。

初始、当前迭代点、最新试点分别保存。一个被拒 candidate 的统计不会取代 current；只有原 accepted 判断已经为真且对应 checkpoint 返回后，才在观测侧更新 accepted current。原 final scan 和统计返回后也仍明确等待最终 report 写入。accepted count 来自原已确认方向与最终 report 列表，不能由 Phi 下降、root 成功或新 point digest 猜测。

每项 statistics 与 geometry 都保自己的完整 point SHA、source、model、事件名及记录时间。current statistics 与 current geometry 的同点关系另列布尔／null；即使它们暂时尚未齐备，也不合成一个跨点“当前场”。缺项或非有限值为 null，不补 0。已成功返回的 initial statistics 在后续初始几何失败时仍只是失败 candidate 的已有观测，不变成 accepted field。

## 5. 有界文件与观测失败

运行目录新增 `actual-mathematical-progress.json`。helper 的 live snapshot只含完整标量归因、计数、短错误、少量 point/source 字符串；文件硬上限 16,384 B，按临时文件加原子替换写入。错误 message 最多 700 字符。最新 trial 的 `actual_read_error` 也只在 observer 副本中截取最多 700 字符，None 原样；原 trial 与完整 report 的错误文本不改。此处是未准入候选最后的有界输出修正，两份完整 step 对象与数值参数逐值未变。全部 scientific raw、NPZ、矩阵、逐点或逐胞数组都不在此文件。

helper 不 import NumPy/Torch，也不持有 q 或任何科学 callback。它不会请求新根或升级角阶。caller 的新增完整 point digest读取次数与秒数分别记录；observer 的事件／写入／写失败／观测失败均区分。增加的 try/except 只包**新增观测工作**，原 residual/statistics/scan/solve/save 的异常处理与传播保持。

新观测失败不改变原 accepted 判据或预算，也不把数学数值补齐。相关 current／trial 标量不能确证时清空为 null并记录 unavailable；原数值程序继续自己的原路径。若 original report serialization 自身失败，它仍按原程序失败，不被 observer吞掉。KeyboardInterrupt等非普通异常不被新增 Exception 分支吞没。

`report['actual_mathematical_observation']` 是原 report 序列化前的完整标量快照，定义该明确时刻。原 write_json 成功后才更新 live 的 last_report_saved_at。live进度可变，任何人都不能把它作为 immutable parent、完整13-member checkpoint、accepted final 或连续证书。

## 6. 原 48 项进度的完整保全与新显示选择

已亲读真实公用控制器 `public_actions_followups_with_active_progress.py`，32,762 B，SHA256 `046f0d7b8d27df95f5249438fdaf435b00c482b009fa8956f27dbdc662a6b314`。其上限是最多四个小文件的 selectors **合计不超过48**，不是每个文件48。

本版 live display明确改为：

- 原 normal 18 项：phase、time、root point、stage、cached angles、请求／返回／失败、原返回、cache hits、强制 stage/final reread、scope start/close、immutable key/full-word counts、两个原成本秒数。
- 新数学 30 项：source/model/target/driver/event/time；initial/current/trial 各自点、Phi、Gram、geometry point、complete 与正违反量；current state、trial accepted、accepted count、report complete/stop、观测失败数。
- 两文件合计48，所有数值项完整保在正式报告；没有声称旧48活映射“原样”。

完整原48每个 label和 dot-path，以及新的18+30全映射，在 `fixed-fejer-mathematical-progress-display-correspondence.json` 完整保存（14376 B，`f649da05f8b74e6ed27cf92ab825ca2cabbdeae77c2c78e603f6f1f09c558372`，blob `141e5866eace9a96220b8160a3409217d784d8b9`）。

此外，在每次原 save_report前，helper对原 `actual-normal-evaluation-progress.json` 作两次完整、有界、逐字相等读取，核其真实 closure source、operator source、同model及原未宣完成标志，将**完整原小文件的全部值**与 actual whole bytes/SHA、canonical value身份存入 full report。缺文件、变化或过大都返回明确 unavailable，不阻科学程序。

原小文件中的 root point仍保自己的身份，绝不被重标为当前迭代点。正式 pure readout的 `mathematical_observation.original_normal_progress_snapshot.complete_value` 保完整原48以及原小文件其他标量。纯读器只验证 full report内不可变的已捕获副本与其完整来源，不在事后再读可变监控文件来改写历史。全部原48在正式 readout中的准确路径也逐项写入上述完整对应表。

## 7. 纯读器与原结果边界

原完整 pure reader继续先核真实 driver与120个 source pair、完整 model/reference/target、input和历史、所有原 own-point snapshots、矩阵/解析frame/closure策略及存在时全final。新增短函数只加载已经全文件SHA验证的标准库 observer，并调用 `validate_report_progress`。

新纯校验检查每个记录的实际 source/model/point、真实 objective key、finite或null语义、complete geometry与其 own point、原 accepted counts/report complete/stop。能与 full report中 surviving initial/current/final对象比较时逐值等号核；若原初始读中途失败而 full statistics对象未进入旧 report键，保其 source-bound returned scalar scope，不把缺对象当完整场。

该纯读步骤不计算 F/J/root，也不为原结果添加连续误差、same-field certificate或收敛结论。完整有限观测上的 max_relative_gram只是原 metric读数；几何 g是原全部finite grid/permanent screen的读数。它们不等于闭面连续 operator norm、全t reach或已付误差。

## 8. 两份完整待执行计划

| 模式 | science / pure argv | science / pure summary | live字段 | 两完整step紧凑字节 |
|---|---:|---:|---:|---:|
| independent | 157 / 7 | 408 / 395 | 18 + 30 = 48 | 92,431 |
| complete-parent | 144 / 7 | 408 / 395 | 18 + 30 = 48 | 91,970 |

全部原数值 argv值与顺序、所有原 398/385 summary selector逐项保留；只另加每step十项数学观测摘要。script／outdir是本版独立名称，原 input与full13父路径不变。实际字段读数仍待真正运行。两完整step分别低于95KB；整 ready也低于100KB，使用完整紧凑JSON，不裁参数。

独立模式仍保原所有 peer／未返历史责任；父模式仍只可用原477499/274d真正返回的complete report和全部13成员，以及其全部typed/protected/inbound历史。同源本版restart遵原全guard。其余 N/M/J 当前族和未知末点没有迁入、清空或冒作实际父。本版与原热路径相同：future run/parent report/checkpoint/model/point/accepted/final均为null。

- independent ready：97225 B，`86d39c01d5a93c5a4d897a02d79bddd23a9b98daa6d6fae6940cc5d348da92f6`，blob `03daa9af5617879a6fea591a2a2d6dfe78e78836`。
- complete-parent ready：96781 B，`a9e2d82e85d1cd9af9255f98fe4b2303666949185040fcfe9cef409b49b49088`，blob `e7c038e4d61133e1af6ddf5d0fd85dd5cc3408d3`。

## 9. 全源与全参数的实际构造

完整 source构造器 `reproduce_fixed_fejer_mathematical_progress_entry.mjs`：12957 B，`f6b30c44180f417d589a8a07fafe04980b18172c5cd4eb8e3815ffc0d8aa9d11`，blob `07de5c3e4414b9d2c064fe19991f253cb2d5f3b7`。它读取三个完整父源和独立完整 authored helper，输出全部四体；三派生体均已JavaScript全文正向构造、逆向逐字回父。原119个完整角色逐pair保留，当前120个角色明确增加observer，不把相同表达式伪装成相同whole source。

完整参数构造器 `make_fixed_fejer_mathematical_progress_ready.mjs`：11170 B，`944d4e58269d6a914333e07aa92ad9dd8c52559a8b92caafac648d58abb15fc1`，blob `794c9d514d4227635ddeaba3b078e98c33fce212`。两整个 hot ready及完整显示对应表作为输入；实际JavaScript重建本两plan逐字相等。原 science/pure每个argv、全部原398/385 summary pair逐项相同，display变化完整记账。

没有执行Python AST、compile、科学导入、fixture、F/J/root、数值验证或实际求解。本版也没有宣称runtime已可观测到任何Phi/Gram/g新值；那些必须等待真实Actions返回已有操作。所有新artifact均是完整公开源、全部参数或说明；raw科学数据继续只在runner。

## 10. 使用边界

本项直接解决“已有原数学结果返回但public progress只见根计数”的来源缺口。它不能让尚未返回的field operation产生数据，也不能从长耗时或新point推断hang、接受或失败。原求解器在新source下仍执行相同完整问题；如实际仍无法在runner时限内自然返回，必须据新的真实phase/own-point数值与成本另作决定，不以小fixture或减预算伪造完成。
