# R315：actual124 完整高度路径的十三次原 native 拒绝与规则中断

作者：ChatGPT / amplitude，AI 辅助研究。日期：2026-11-15。  
分类：实际公开 Actions 结果、原始标量与源码调用链读回；不是新的数值计算、非存在证明或接受证书。

## 1. 结论与实际范围

[Request124 的实际运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43698138088) 从六控制族的真实 actual119 第 3 批参数出发，取正目标幅度 $\lambda=0.001$，在原同一 native worker 上尝试完整 $H(s)=sH_*$。它完成零高度请求，随后 **13 个正高度请求都在原 Newton 第 0 次迭代用完十档回溯并拒绝**。130 个实际试探全部保存为同一种原异常：`momentum branch D/S/A rejected`，位置均为 `stage=0, rawCell=0, rawSegment=8`。没有正高度请求收敛，也没有一次正高度 native Newton 更新被接受。

第 15 个请求 $s=1.9073486328125\times10^{-6}$ 尚在执行时，规则 runner 经真实 pull 发现 README 变化并发送 SIGTERM。因此最终 compute failure 是**已有十三次数学拒绝之后的规则中断**，不是该第 15 个请求已经返回数学拒绝，也不是 300 分钟科学预算耗尽。report job 成功保存了原状态读回。

本次仍没有 $s=1$ 的实际完整高度响应、当前 $H_*$ 的完整端口 Jacobian、物理边界 FD、完整 full-DN 外迭代、最终 native audit 或非零耦合接受场。后继应修正当前完整 shooting 方向的形成方式并重读真实残差；继续原样减半 $s$ 不能算作已证明有效的推进。

## 2. 来源、参数与字节身份

实际 source commit 为 `b1df8ec306e596256a317df925464af6acaa31c6`，compute job `132763110680` failure，report job `132807763676` success。两份 CLI 原日志由主控唯一下载；本结果只读日志、JSON、源码及文件身份，没有导入模型或重新计算 RHS、J、范数、方向或科学试探。

| 原件 | 字节数 | SHA-256 |
|---|---:|---|
| compute 原日志 | 288405 | `71389c1b3357d26bc34b0ed07f8707f16ff749f0ec6851dc79827b8ed62c2d80` |
| report 原日志 | 84841 | `823aafc961605aacd52000c2c7234b7bf1620688060f048feff24296175a461e` |
| 两 job 相同的紧凑 summary，不含分隔 LF | 40051 | `455945a39c5ab2e9d56f6378b7cef8cbe055d562fadcc0800c93b7f9c2b5bd1b` |
| 实际 request | 22159 | `b76f94ada5b146f79c868af219662fdb39b98c9cd9b00b9d8667f34e7f337ab1` |
| 六参数及高度路径 recipe | 4057 | `b590eb0c33d55ff13a1b6ec3722d5dfe9f316a774207a1b8dda7925e6f159416` |
| 原科学 stdout/stderr，Actions 原读回值 | 166315 | `07a9218ea54045da073e5eebe2ede886deeb2ea49a94ee263ab6ef555be93ba6` |

日志重建只剥除行首严格匹配的 GitHub 时间戳及可选 BOM。compute 的 `six_height_path_scalar_summary_identity` 与 report 的 `request124_scalar_summary_identity` 名称不同，均指向上表同一 40051 字节正文。两份原正文已逐字核同。环境随后断连时，只通过公开接口再取小于 100KB 的 report 原日志；其完整字节 SHA 仍与 CLI 原件相同，未重跑科学。

四个原数学输入继续是：

| 输入角色 | SHA-256 |
|---|---|
| accepted96 来源 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared112 来源 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 原零高度 tail anchor | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| 原 T112-config | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

真实初猜六参数为
`[0.41654476801167684, 0.23884336093393582, 0.5270922473095916, -0.13437878055563054, -0.005765450212224129, 0.4141025261683763]`。前三个参数为 active，后三个 odd 系数冻结；它们来自 actual119 第 3 批，既非 actual119 最后一批，也不是已接受 full112 场。$\lambda=0.001$ 缩放原低三 core targets，路径变量 $s$ 另外缩放全部 112 个当前切口高度，二者不可混称。

Actions 原 `request124_source_recipe_identity` 列出 103 个 source 文件；request source map 的 canonical JSON 为 11225 字节 / `a208ad740fb4d28ae09c7b94f71f823b5cfe2c7e71e8e6d43fe34505de6affc3`。本次读回核对了上述实际身份和关键完整源，**不宣称又在本地独立重审了全部 103 个依赖或所有已删除的大 payload**。

关键 source SHA：

- 六族 H(s) adapter `geometry_20261115_six_control_height_continuation_full112.py`：`557f3aab83116c1d8eef83e4c83306e8058749ccdb56b2ec8808effd2e16bf21`。
- 高度路径 helper `geometry_20261115_original_tail_height_path.py`：`e830a1679908cdc0cdd8c1ecd5663bbf6b82b24a3d52e44cf678aedc227eee48`。
- process wrapper：`0836ed339974d5f21cdbd110f1a78ba5fb9232f5ee4f22c74849b2ee16d133dc`；scalar reader：`4a0ab4a7ad8fbd62dd5fced0f15431498934d000af2681e137dc237b8ebaf5be`。
- 原 true-tail client：`1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09`。
- 原 tangent worker：`36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a`；原 shooting core：`ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`。
- 原 tangent predictor：4250 字节 / `8d39830939a52fc40f7de06cf5a2a9de9959f94058594051a7989b8b40744459`。后两数学源及 reader 已在实际 source commit 的公开小文本中再核字节。

## 3. 已完成的 full112 初猜与原域检查

原 699 个 mesh nodes 全保留，没有加点。完整状态为 338 个 physical 分量、112 个自由 core 分量及 3 个 active 参数，共 453 维；109 个高 core 初值为零仍是完整自由未知量，没有被消掉或被当作 Schur 已解。

原初猜 collocation 最大值为 **`6.8749454041621035e-6`**，并未达到原 $10^{-6}$ full-DN 接受阈值。原节点、中点及两个 RMS 分数的域 preflight 通过；两个 RMS 分数各读取 698 个点、invalid count 均为 0：

| 原查询类别 | 原保存最小 $\beta^2$ |
|---|---:|
| 节点 | 0.0022538385815712436 |
| midpoint | 0.002267325049764346 |
| RMS fraction 0.17267316464601146 | 0.002245239130645116 |
| RMS fraction 0.8273268353539885 | 0.002259211840830444 |

这只说明该初猜通过了实际这些域检查，不能替代全域连续性、BC、FD 或最终 full-DN 接受。初猜原低三 unit equations 为 `[-40.59554745991145, -0.020429301868211316, -6.463227430456828e-5]`；原 112 行线性右端残差的前三项为 `[-18.7513817252759, 0.0012195172149540542, -1.016669334572825e-6]`，其余 109 项原记录为 `-0.0`。该线性初猜没有被冒称非线性解。

原完整 $H_*$ 的前三项是 `[0.0008954476172889355, 5.023344896215423e-7, -2.0011103217478445e-7]`，后面所有小高模也保留。原 112 个 little-endian binary64 字为 896 字节 / `d19e25eabad7f2c84ecdd10580caee1c3b41ef9d1e0a1a3ae07c58486277eced`；记录的 negative-zero columns 为空。没有截断高模或把旧 compact H 改名为新的计算结果。

## 4. 全部十五次实际高度请求

原 policy 首个正增量为 $1/64$，真实收敛后增量乘 2、上限 $1/4$；已确认的数学拒绝后乘 $1/2$，下限 $2^{-20}$，最多 64 个 bootstrap 请求，包含零请求和最终完整 J 请求。零请求与中间请求的 `jacobian=false` **不跳过原 native Newton 内部完整 withJ**，只是不请求最终端口响应矩阵；$s=1$ 必须请求完整 J。bootstrap 不执行最终 audit。

下表均为原已保存值。`chartCondition` 是原代码形成的浮点图条件估计，不是严格条件数证书；未返回项没有补值。

| call | 原 $s$ | 原返回/停止类别 | 原 norm | 原 minA | 原 minD | 原 chartCondition | 原 request 秒 |
|---:|---:|---|---:|---:|---:|---:|---:|
| 1 | 0 | 零高度收敛 | 0 | — | — | — | 642.66576234 |
| 2 | 0.015625 | 第 0 次迭代线搜索拒绝 | 195955.61867016536 | 0.9315748352465438 | 0.9999646599422697 | 1.7972044411853582e+37 | 776.021459822 |
| 3 | 0.0078125 | 第 0 次迭代线搜索拒绝 | 97856.59357948169 | 0.966393166756658 | 0.9999823450999782 | 7.915788800119649e+37 | 769.6231942379998 |
| 4 | 0.00390625 | 第 0 次迭代线搜索拒绝 | 49218.73229682029 | 0.9833401534706379 | 0.9999911763297142 | 9.33361570559209e+38 | 766.9188832 |
| 5 | 0.001953125 | 第 0 次迭代线搜索拒绝 | 24510.210588641476 | 0.991705059082223 | 0.9999955891094777 | 5.617062644865429e+40 | 798.1448174510001 |
| 6 | 0.0009765625 | 第 0 次迭代线搜索拒绝 | 12239.960400189077 | 0.9958611655277082 | 0.9999977947908552 | 3.509178359133333e+39 | 764.0460468800006 |
| 7 | 0.00048828125 | 第 0 次迭代线搜索拒绝 | 6109.123356715916 | 0.997932728309816 | 0.9999988974544518 | 9.413899861761107e+38 | 753.4410567759996 |
| 8 | 0.000244140625 | 第 0 次迭代线搜索拒绝 | 3044.061119962866 | 0.9989668988753063 | 0.9999994487419813 | 9.537300792287121e+41 | 758.9561945709993 |
| 9 | 0.0001220703125 | 第 0 次迭代线搜索拒绝 | 1524.2077460272185 | 0.9994835829104335 | 0.9999997243746794 | 7.785900239821663e+40 | 768.7516794129997 |
| 10 | 0.00006103515625 | 第 0 次迭代线搜索拒绝 | 756.9251609808432 | 0.9997418247975556 | 0.9999998621882619 | 1.8456059305210938e+40 | 765.1351926789994 |
| 11 | 0.000030517578125 | 第 0 次迭代线搜索拒绝 | 382.78457901774044 | 0.999870920731134 | 0.9999999310943615 | 1.5919854606536756e+41 | 761.7267264450002 |
| 12 | 0.0000152587890625 | 第 0 次迭代线搜索拒绝 | 190.7696267796988 | 0.9999354624482527 | 0.9999999655472384 | 2.0987315051966061e+43 | 761.604030216 |
| 13 | 0.00000762939453125 | 第 0 次迭代线搜索拒绝 | 96.36297235979919 | 0.9999677317447475 | 0.9999999827736336 | 4.1439243039309565e+44 | 761.2161671459999 |
| 14 | 0.000003814697265625 | 第 0 次迭代线搜索拒绝 | 47.989089918750544 | 0.9999838660025226 | 0.9999999913868204 | 1.0556982914536995e+46 | 772.7802973580001 |
| 15 | 0.0000019073486328125 | 执行中被中断 | 未返回 | — | — | — | 未返回 |

call1 真实返回 `converged=true, residual=0`，有原 checkpoint，history count 为 1；没有完整端口 J，也没有 audit。其原 meanSlope 为 `0.08000000000000027`，meanSecond 为 `-1.866666666666673`，两项 correction 为 0。它是本次实际零高度有限尾解，不是一个非零耦合接受场。

call2–14 的 `failed` 文本均为 `Error: multiple-shooting line search failed at ...`，`lastIteration.iteration=0`。这些失败响应不含可读的 `converged=true` 或通过 residual；表中 norm 来自原 `lastIteration`，不是把失败响应的缺失 residual 补成该值。每次的 failed checkpoint 均明确仅供 diagnosis/可能初猜，不是已收敛响应。

所有正请求的 `previous_converged_s` 一直为 0。13 次拒绝的原 Python cache 未改变字段均为 true。call15 没有返回 response、lastIteration、request seconds 或数学异常；不能把前一 call 的数据延用给它。16–64 尚未调用，这是最多 64 次预算的未访问余量，不代表每项都是既定必做试验或数学失败。

## 5. 十三组完整回溯、实际 warm 与失败位置

每个 call2–14 都实际尝试了原十个步长：

`[1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125]`。

原 compute 的每个 `request124_height_path_request_returned` 事件保存了全部 `original_trials`。逐条 JSON 读回计数得到：13 组、130 条、130 个 `momentum-guard-rejection`，全部 error 为 `Error: momentum branch D/S/A rejected`，全部位置为 `(stage,rawCell,rawSegment)=(0,0,8)`。没有 `accepted`，也没有成功计算 trialNorm 后的 `residual-not-decreasing`。因此这里的主要拒绝是原域检查阻止试探，不能改写成已经比较完 130 个有限 residual 后仍不降。

每个正请求在形成 correction 前，都已有一次完整 withJ 基点评价返回；minA、minD 见表，均为原正值。原 context 中 `cold_first_complete_withJ_evaluate_did_not_return_by_pinned_source` 均为 false。这与 actual120 首次 cold withJ 尚未返回、没有 trial 的失败阶段不同。位置 `(0,0,8)` 来自原异常附加字段；没有保存实际失败半径、角度或每角 D/S/A 数值，不能凭外层错误补造它们。原 trial diagnostic 取的是 stage 输入 `trial[stage+1]`；stage0 也不能被口头替换成“node0 的所有值已查明”。

十三次都有 `tangent_warm_predictor` 事件，kind 为 `full-nonlinear-shooting-tangent-warm`，modes112、stages576，无 predictor fallback 事件。原 maxChartCondition 全为 `385639413119263240000`；maxRelativeCorrection 首次为 `3.844494357362678e+252`，最后一次为 `9.385972552154975e+248`。

这里必须保留源码解释边界。原 predictor 对每节点用
$$
\max\!\left(10^{-250},\max_j|y_{n,j}^{\mathrm{old}}|\right)
$$
作相对 correction 的分母。零高度解附近极大的“relative”数值**不能直接读成同量级绝对位移或溢出**；实际 predictor 还检查输出有限。它没有把初猜当作接受结果。

但调用关系是确定的：原 worker 在 `tangentPredictor.predict` 正常返回时即采用 `guess.states`，标记 `predicted=true`；只有抛错才 fallback。原 worker 仅当 `sol.converged` 才更新 `last` 并重建 predictor。故十三次均沿仍保留的真实零解 predictor 提供初猜，数学拒绝没有污染后续收敛缓存。

原 predictor 逐 stage 显式反演 $A+B G$ 并传播112维图；原 Newton correction 同样用局部图反演，在全 cut/stage/far 方程上消元回代。原 correction 的 chartCondition 最后记录为 `1.0556982914536995e+46`。这些浮点记录和反复同位置域失败支持审查这种方向形成；它们不证明精确全边值矩阵奇异，也不能单独证明 warm 是唯一原因。尤其当前 warm 基点的完整 withJ 已返回，随后失败的是原 correction 的试探。

## 6. 规则停止、原预算与清理职责

原 runner 从 `2026-11-15 09:13:28 UTC` 运行至 `12:13:52 UTC`。共有 5 轮同步启动，前 4 轮真实同步完成；最后一轮在 `12:13:51 UTC` 保存：

`Root/topic README changed after actual pull; coordinator must read retained diff`。

原最终 runner 字段是 `science_terminated_for_actual_rule_change=true`、`wrapper_returncode=77`。process wrapper 记录 `phase=external-interruption-partial`、`scientific_child_returncode=-15`、`wrapper_returncode=143`、`external_signal=15`，elapsed 为 **10822.942995484 秒**，`budget_exhausted=false`；声明的科学预算仍为 18000 秒。stdout copy errors 和 periodic sync failures 均为空。

最后的 height-path 状态是在请求执行前落盘的 `phase=original-request-in-flight`，它还保存 `resource_partial=false`。这不是比外层 SIGTERM 更晚的完成结果；必须结合真实 process/runner 状态解释为**中断时的未完成快照**，不能据该 false 排除资源/外部中断，也不能给 call15 补数学结论。

原 native 同一 worker PID 为 3163；记录 `same_worker_and_owner=true`、`no_cache_or_worker_last_assignment=true`。Python wrapper 向独立科学进程组传递终止，并在未退出时升级杀死进程组；本次日志没有 adapter 正常 finally 返回和 owner 正常 close 的完成事件，所以不把正常清理函数的存在当作本次全部已执行。

runner 的 `partial_scientific_files_not_removed=true` 指它发出规则停止时保留现场；随后独立 reader 已完成原字段与 SHA 提取，workflow 的 `request124_owned_temporary_payload_removed` 事件明确删除本请求临时树，`no_artifact_release_or_git_raw_upload=true`。两个时间点不矛盾。本次不把原始可再生状态、J、checkpoint 或日志另行加入仓库/Release。

## 7. 已完成与未完成责任表

| 责任 | 实际结果 |
|---|---|
| 四原输入、两个 ready 历史输入与公开源恢复 | 本次实际来源记录完整，科学已启动 |
| 六族 453 维初猜及原节点/mid/RMS 域 preflight | 完成；未声明解 |
| 真实零 H native 请求 | 完成，原 residual0 |
| 中间完整112高度求解 | 13 次真实数学拒绝，另 1 次执行中断 |
| $s=1$ 完整 $H_*$ 响应 | 未到达 |
| 当前完整338×112端口 J | 未返回 |
| 三扰动原物理/分离边界 FD | 未执行，字段 null |
| 原 full-DN 8 outer / 17 inner 档 | 未进入，原 inner evaluation rows 为空 |
| full-DN collocation/RMS/BC 接受 | 未付 |
| 最终 fresh native full J、cut/physical audit | 未付 |
| 非零 coupled finite acceptance / closed surface | false，未完成 |

原门保持：native32次迭代、每次10档、tol $2\times10^{-9}$；full-DN8个 outer、17档 inner、collocation及冻结 RMS $10^{-6}$、BC $10^{-11}$、原边界 FD $5\times10^{-5}$。本结果不把中间失败改为新门，也不降低这些阈值。

## 8. 数据范围与缺项

原小 summary 的 `summary_complete=false` 来自 reader 的**输出大小处理**：完整 height-path 及 native 详细 sections 用 counts/hash 表示；全部15个 bootstrap primary rows 保留。它不表示十五行被截断，也不自动表示全部科学事件丢失。原 compute stdout 的逐请求事件仍保留全部13×10 trial 和相关 warm/iteration/failure 记录，本文按这些完整事件读取。

Actions 原 reader 列出 24 个原 JSON/log 文件的 size/SHA，其中14个 native response 压缩文件从 call1 到call14。`true-tail_0015.json.gz` 没有已返回原件。完整原 trace 记录87条、trial记录130条；trace SHA `8b15a43f79780886f7d168989bb83d4175d988ef003a8cada6749e690fef8b60`，trial SHA `e005a4013f8d4304e1a47af8da813d92857d165b223d2aae50fee35863a14b81`。

输入绑定文件为47362字节 / `e9125bfb40fbe2144338eadb11f148f457ad5e0acd28b5c10c8bce9949dd7e8c`；其 canonical 对象 hash 是另一种身份，不能混同文件字节。相同地，原 runtime/source/context canonical 身份与对应文件 SHA 分开。14个大 response、prepared 场、矩阵/因子原件没有在本地重新下载或全面独立 byte audit；本文仅核原日志正文、原报告中记录的身份与实际源码范围。原 factor 全矩阵、各失败角度 D/S/A 数值、call15 后续轨迹都未被补造。

## 9. 有证据的下一实际求解路径

本次给出“同 worker 完整高度延拓是否可直接跨过首次 native 阻断”已运行部分的实际结果：零解能真收敛，当前策略在十三个正 $s$ 上没有取得一次 correction 接受。因此下一步不应原样重复300分钟的同一序列，也不应仅关闭规则监控、放宽 tol 或把 failed checkpoint 作为已接受锚。

有实际源接口支撑的最小方向改进是：在**本次真实请求的当前 H、当前全部 shooting states 和 fresh full withJ**上，把原局部图反演 correction 替换为完整 cut + 576个stage + far Robin 系统的 R273 链 QR 求解；保全部129248行、原尺度、全部224状态列、完整高模及端口归一化。QR返回只构成候选方向，仍交原10档完整 noJ、原 D/S/A 及严格 residual decrease 接受；失败就按原失败记录，不由线性 residual 小冒称非线性已接受。不得复用其他 H、其他基点或旧失败包的 J 来冒当前 fresh J。

若同时改进高度初猜，应另明 source 身份：用真实零/最近已收敛状态的完整边界线性系统生成高度增量响应，保原 inhomogeneous cut 右端与全部 stage/far 行，避免原逐图显式反演；只作为初猜，再用当前完整原映射求解。它与 correction 更换是两个可区分作用点，不能把一项成功归因于另一项，也不能将极大的相对指标直接作为拒绝准则。

现有 persistent binary128 primal / 全链 QR 路线可作为更高精度的实现基础，但其已测成功场不等于本次 H(s) 的接受场。若把本次请求接入该路线，必须保持续128状态、同一完整残差和当期方向身份；旧64J只可明确作为近似 chord，真正端口338×112响应、当前H边界FD、原final audit和full-DN入口仍逐项实付。不能在此用一个先前 native norm 小或一组 tangent 成果替代这些责任。

上述改法是由实际130次原域拒绝与当前局部图方向记录支持的下一算法候选，不是收敛保证、非存在结论或新验收门。后继应直接在公开Actions付一个完整当前H求解并据真实原门继续；本次失败的原方程、原高模和未付终门均保持可追溯。
