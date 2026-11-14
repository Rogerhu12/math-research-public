# matched-cut 原联解关闭后的最小审计清单

状态：**静态检查接口，不是运行结果。** 作者 /root/coupled_prefix，2026-11-09。只依据已冻结源码和新输入，未启动或重复任何 solver。原 same-g N512 后续方案继续适用，不新增数学门槛。

以下令 O 为 notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01。文件均是此真实新身份；不能用 continuation03 的成功记录或 UNSOLVED warm 的字段代替 O 的结果。

## 1. 原源定位与字段来源

这些行号只对来源账本绑定的当前源有效：

| 原文件、行 | 审计依据 |
| --- | --- |
| scripts/db6f-prefix-coupled.py，62–63 | 原 lagged 外层先在实际重启 H 请求 jacobian=true、audit=false |
| 同文件，65–79 | inner affine 仅临时；恢复真 tail 后检查 candidate H 和原 BC，最多八次 |
| 同文件，99、120–123 | summary 初始 success=false；捕获异常后写 error，Python 可以正常退出 0 |
| 同文件，111–118 | 先保存一次 CP，再做 prefix audit 和最终 seam，最后第二次保存与 summary |
| 同文件，33、40–44 | 最终 H 来自已重建物理 PPoly；强制真 jacobian/audit，并记录 mean/nonmean 两 jet |
| scripts/db6f-prefix-tail-trial-client.py，22、33–47 | fresh cache 空；先把真实 response 写入独立 gzip，再检查 failed/converged；同 H 的合法 cache 可复用 |
| 同文件，26–29 | 未来响应使用本 trial client 的八源集合，不是 continuation-client 的集合 |
| scripts/db6f-prefix-run-bound-command.py，12–15、21–32 | 先核所有输入 SHA，等待 Python 子进程退出；从 summary 抄 mathematical_success/error，不能由退出码代付成功 |

coupled 源 SHA256 为 37defb33c031fd967ab0e06e086da56f2d67e30dd88bbbcb8e5e13201476511a；trial client 为 540720f625f192b73e2c814fd80dca1da286902943f8ab8ef0b82209f2589847。其余完整 SHA 在本清单的 sources.json。

## 2. 第一项真正 DN：只审 O_tail_0001.json.gz

空 warmup、fresh client 和原 lagged 路径决定首项真实 request 应是：

- height 逐值等于本次 preparation.json 的 actual_restart_request_height，不能换成历史 H*；那两者已记录约 $10^{-19}$ 的差；
- jacobian=true、audit=false；
- record.config 与 O-tail-config.json 作 typed canonical JSON 同一性比较；八个 source_sha256 必须恰为当前 trial client 源集合，全部重哈希；
- 如果是成功响应，converged 严格为 true，residual 为有限非 bool 数且小于原 $2\cdot10^{-9}$；heightJetJacobian 有 705 个有限非 bool 数；jets 恰有原 17 键，即 14 个有限标量和 height/slope/second 各 15 项；audit 应为 null；
- checkpoint 为同 M15/N256、physicalDepth12/p8/s32/guard .05 的 865×30 有限 states、13 个 rawNode/rawStates；cutHeight 等于这次 request，raw 镜像吻合。

记录本包真实 hash/字节及对应关闭 trace。若实际第一项 request 与准备报告不同，先澄清重启身份，不能悄悄重标旧 warm。真实 failed 包则原样保留 failed/lastIteration/checkpoint 的实际 schema，包括 null；不得补造 705 Jacobian、converged 或 residual。

历史 call001 的真成功只提供初始 states；它没有本次首项 DN/J。工具仍在运行时，可在此独立包完整关闭后陈述首项有限 DN 的结果，但不能据它宣称 prefix 联解成功。

## 3. 外层结束：原来的数值接受条件

真正关闭后，联合读取 O-summary.json、O.json.gz、O-reproduction.json 和 O-run.log，并核新 input-bindings 的实际 SHA/command。若用了额外根会话 guard，另记录那一层的真实工具退出，不覆盖原 reproduction。

要称本次有限原联解成功，至少应同时具有：

1. 实际工具/原 Python 子进程已观察关闭；summary 无 error 且 solver_success 严格 true，CP 中 solver_success 也 true。原 max_rms_collocation_residual 有限且达到原 $2\cdot10^{-9}$；配置中的原 tol 不变。
2. dn_solver 是 outer_actual_inner_affine，actual_outer_checks 最后一行 inner_success=true、actual_boundary_residual 有限且不大于原 $10^{-8}$，actual_tail_residual 小于原 $2\cdot10^{-9}$。这条 BC 包含入口残差及按 bcweights 归一的 terminal 条件；原 bcweights=.002，所以相应物理 terminal 条件是原 $2\cdot10^{-11}$。
3. 最后行的 tail_calls 指到相应的真实保存响应；同 H 的正确 cache 可以使不同 outer 使用同一个原响应，不能人为要求每轮必有一个不同文件。inner_success=true 本身不够，必须有该真实 DN 和原 BC 末门。
4. 最终 CP 的物理 profile、chart、port、tail 参数、q_g、warp_reference 保持原同 g；config 的 M15/fixed_metric/actual_nonlinear_tail、原角数和容差正确。最终 p、support 振幅和自适应节点数可按原 BVP 改变，**不要求它们等于初猜**。系数块的真实 SHA、字节、形状、有限性及递增 mesh 全部核对。

旧 warm 的 solver_success=false 不应复制成新结果；反过来也不能因为 CP 已写出或其中 sol.success=true 就跳过后续审计。原源码第 115 行确实在最终 seam 之前写过一次 CP，因此可能出现“CP 存在，但后续 audit 抛错”的中间文件。

## 4. 最终真实 seam 包是独立必需证据

以完成 CP/summary 的 tail_seam.tail_record 为准定位文件，不猜固定尾号，不从任意最后文件挑一个成功包。tail_calls 应与该最终记录序号一致。核对：

- request.jacobian=true、request.audit=true；audit=true 绕过 client cache，源码确实请求了新实际审计；
- request.height 来自该**最终保存 PPoly** 的末端 $H=-.1\,Y_Z(L)$，不是初始 matched H，也不是某次 inner 的 node-array 高度；三者可能有浮点差，须逐项说明身份；
- config、八源、checkpoint/cutHeight、converged/residual、705 Jacobian 和 17 jets 的门同首项；tail_seam.tail_converged、tail_shooting_residual、tail_jets 与实际 response 一致；
- audit 恰有原八个有限数值字段：fullD、normalizedFullDefect、minLeading、minD、formalCurvature、maxPhysicalPV、actualMetric、holonomy。此次原 auditSteps=32；不能写成新的径向加密；
- CP 与 summary 均包含完整 tail_seam，且最终保存的系数块可读取并匹配 hash。

还须保留 mean_first_actual/expected/mismatch、mean_second_actual/expected/mismatch、nonmean_first_mismatch、nonmean_second_mismatch、cut_metric_fft_l1、cut_metric_c1_fft_l1。它们是原 seam 的诊断数据，不能把“字段存在”当成已经有精确 Cartesian 接缝。本次 M15 seam 的 angular_samples 按源码为 max(512,64M)=960；prefix audit-angular 是1024，两者不要混写。

原程序只对前述 BVP/BC/射击容差作数值成功判定，没有为每个二 jet mismatch 再设同一个 $2\cdot10^{-9}$ 门。本清单不补造这种门。后续公共 C²表示和实际 metric 认证须按真实 mismatch 重做；sourceMetric、实际 XYZ metric 和 fullD/fullTensor 分别报告。

## 5. 退出 0 的三种情况不能混同

| 实际情况 | 可陈述的结论 |
| --- | --- |
| reproduction.exit_code=0，但 summary.error 存在或 solver_success=false | Python 正常退出，原数值任务未成功；按真实 error/失败包归档 |
| CP 有 solver_success=true，但缺最终 tail_seam/实际 audit，或 summary 保持 failure | 只写出了中间 CP，尚不能认作完整有限联解 |
| 原数值门、最终真实 seam 包、闭合文件与实际退出证据全齐 | 可认定本次有限 M15/N256 原联解完成；不等于主问题或 README 第5门已完成 |

如因 ENOSPC、OOM、外部中断或 guard 停止而没有完整关闭证据，应单列运行故障或未知状态，不把它改写成数学无解。失败不改原 guard/tol/g。

原 bound-runner 的 exit_code 是 Python coupled 子进程退出，不是一个独立的 Node worker exit 字段；client.close 有超时 terminate 路径。只能陈述实际观察到的退出身份，不能从 Python 0 推造 worker 0。本清单不新增一个源码未提供的数值接受门。

## 6. 仅在上述真成功之后继续原 N512 计划

复用 notes/2026-11-09-db6f-prefix-final-m15-n512-followup.md：用本次真实完整 CP 及其最终 tail_seam 指向的实际尾作为同 g 初猜，保持 M15/p8/s32/depth12/原 tol，只有尾角求积 N256→512 及各新 I/O 路径变化；必须重新真 DN/原 BC 校正。不能把本初猜的 call001、首次 DN/J 或最后一个无 audit 包当成最终 seam。

该计划的目标 CP 路径用本次实际成功 O 填入，配置若有 trialDiagnosticFile/trialStatePrefix 也指向新 stem；ordinary shared client 的源集合按其自身核对，不套 trial/continuation 集合。其后的实际 XYZ、公共 C²、连续 metric/曲率/reach/矩与未参与优化者重跑仍按既有最小流程完成。本清单不要求新的 LS、额外 RK 加密或额外 C² 到 $10^{-11}$ 门。
