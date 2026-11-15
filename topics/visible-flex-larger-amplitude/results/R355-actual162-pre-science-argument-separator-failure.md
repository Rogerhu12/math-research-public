# R355 — actual162 在原科学入口之前的参数分隔符失败

作者：AI（geometry agent）。日期：2026-11-15。状态：实际公开 Actions 终态已读；本次没有启动连续 C、深尾或射影有限头科学。本文记录原值、来源与最小传输修复，不产生新的数学结论或验收条件。

## 355.1 结论与原运行身份

Request162 的第一次运行在原 rules runner 的 argparse 阶段终止。新进程身份包装器使用的内部裸双连字符被外层参数解析器解释为参数终止标记，原科学脚本路径及其参数随即成为未识别参数。C 和 deep 两个包装入口都返回 2；原 rules runner 的初始化、同步与科学子进程启动均尚未进入。

因此，本次没有新的六 primitive、cut jet、112 深尾行、射影 panel、cut 候选或 DN 值。不能把这个工程失败写成 R347 的失败、资源耗尽、分母包含零、共振、非线性拒绝或原课题完成。

| 对象 | 实际身份 |
|---|---|
| Repository | Rogerhu12/math-research-public |
| Run | 43735722483 |
| Source commit | d23db7eba55d73bafcb6f2c8d7f82d87f1d85b3c |
| Workflow | .github/workflows/visible-larger-public-stored-C-projective-head.yml |
| Run created | 2026-11-15 16:29:10 UTC |
| Compute job | 132877793292；failure |
| Report job | 132878305607；success |
| Dispatch request | public-stored-C-projective-head-request.json |
| Request bytes / SHA256 | 20703 / 5b002d6fe786c29e96313129690d7510f9e3e572c1a8b43b88fad01e4de0be18 |
| Actual workflow bytes / SHA256 | 74330 / c9e30f35238e30d307a6253dc1079b9d296bc83d404dcd6c85aa83becc50af08 |

官方定位：[run](https://github.com/Rogerhu12/math-research-public/actions/runs/43735722483)、[compute](https://github.com/Rogerhu12/math-research-public/actions/runs/43735722483/job/132877793292)、[report](https://github.com/Rogerhu12/math-research-public/actions/runs/43735722483/job/132878305607)。来源文件和配方都以这个实际 source commit 为准；后继修补不能反写为本次已执行。

## 355.2 已完成的前置来源工作及其边界

原 job 的步骤 1–9 全部 success：

1. 建立本次独占临时目录 visible-stored-C-projective162 与进程身份记录源。
2. Python 3.12.14 及原区间运行环境安装。
3. 释放声明的未用 SDK 临时资源，记录实际磁盘容量。
4. 核对全部 16 个直接来源、完整查询、proof 和原输入配方。
5. 在 Actions 中对实际 Python 源和工作流 Python heredoc 做语法解析/编译，并对实际 16 个 shell run block 做 bash 语法检查。
6. 恢复三个原输入和原 public source 子集。

原资源记录为：

- free_bytes_before = 92815835136；
- free_bytes_after = 111417032704；
- minimum_free_bytes = 34359738368；
- original_Node_Python_compiler_BLAS_and_sources_retained = true。

这些是资源和工程前置记录，不是数学判据。容量检查成功并不保证任意实际传播都能在其后预算内完成。

原来源事件列出的 16 个名称/SHA 与本次 request 中的 source_sha256 逐项一致。本地读回只比较这些原文本、字节和摘要；没有运行科学源。关键新旧来源如下：

| 来源 | Bytes | SHA256 |
|---|---:|---|
| geometry_20261115_stored_continuous_E_cover_v3.py | 89307 | f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df |
| geometry_20261115_stored_continuous_C_far_graph.py | 16333 | fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a |
| geometry_20261115_stored_C_finite_head_flux.py | 58317 | 4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d |
| geometry_20261115_stored_C_finite_head_projective.py | 77731 | 5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216 |
| root_20261115_projective_head_scalar_readout.py | 19995 | befe77fc70e67260b475073adfa749ebce6e727c956703c7cbc79afe8389e9c3 |
| root_20261115_current_C_native_scalar_readout.py | 29751 | 2f2386afab07e5acc9b6ec155f782cb1ba1c8df5a879607effd5985c151784ff |
| root_20261114_current576_rules_runner.py | 32654 | 3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde |

实际查询文件 original-stored-continuous-E144-queries.json 是 1303 B，SHA256 为 4e59c69fae54045e100180e2d7576b848423a503394ff0b4dd87f6e219b7fd59。它仍要求原 config 的 binary cut 点与 whole natural domain，两者都没有在此次执行中产生科学结果。

预检的成功只说明真实字节身份和语法正确；此次后续失败恰好是合法语法中的 argv 语义错误。不得把预检说成此前已支付运行接口或科学结果。

## 355.3 首错的准确位置

16:30:54.615772 UTC，包装器记录 C-parent-launch。随后原 runner 在 parse_args 处输出：

> error: unrecognized arguments: -- /.../geometry_20261115_stored_continuous_E_cover_v3.py ...

该原错误后面保留了完整原科学参数，包括原三个输入、全部 six primitive、两个查询与 C budget_seconds=3600。16:30:54.616960 的 C-parent-return 记录 actual_exception_type=SystemExit、actual_exception="2"、normal_return=false。16:30:54.627509 UTC，步骤 exit 2。

16:30:55.059289 UTC，far-parent-return 同样记录 SystemExit("2")。其原错误为相同的裸分隔符，后随 geometry_20261115_stored_continuous_C_far_graph.py 和全部 deep 参数。16:30:55.069304 UTC，该步骤 exit 2。

原调用结构是：

    original_rules_runner --out RULE_OUT --command python -u owned_helper exec ROLE -- SCIENTIFIC_SCRIPT ORIGINAL_ARGUMENTS

原 runner 的 --command 使用 argparse.REMAINDER；在本次真实解析中，内部裸 -- 没有作为子进程的普通参数留下，而使其后的路径/参数落入未识别部分。原 runner.main 中的 parse_args 位于 Runner(out)、initialize、sync 和 Popen 之前，因此失败范围由实际 traceback/usage 与这个原源码位置共同确定。

本次只有两个 parent-launch/parent-return 对；没有 C-science-launch 或 far-science-launch，没有 runner 的 startup sync / pull receipt，也没有线性 science launch。输出的 request162_explicit_rules_baseline_update 只是读取并设置已经核过的双 README 比较基准，不是真实 Git pull。本文不把它写成本次规则同步已经成功。

## 355.4 真实步骤 success 与科学未启动的区别

| 原步骤 | Actions outcome | 原实际含义 |
|---|---|---|
| 10：C cover | failure | rules argparse exit 2；C 未启动 |
| 11：cut two-jet readout | success | 原 C result 不存在；输出 unavailable 事件 |
| 12：deep far | failure | 同一 argv 错误；deep 未启动 |
| 13：projective propagation | success | 缺 C/deep 输入，诚实条件退出；driver 未启动 |
| 14：C scalar readback | success | 输出完整缺件范围及进程身份 |
| 15：deep scalar readback | success | 输出完整缺件范围及进程身份 |
| 16：projective/rules readback | success | 完整读取已存在的工程记录；0 mode/0 ledger |
| 17：conditional cleanup | success | 已读完现存范围且原进程静止，删除独占临时根 |
| report job | success | 重复原小摘要与 unavailable 范围；没有科学重算 |

线性步骤的原事件名是 request162_finite_head_actual_input_unavailable。因此 report 的 linear_step_outcome="success" 不能解释成射影传播成功。原 reader 自身明确 reader_success_is_not_scientific_success=true。

C 原摘要主要字段是：

- compute_step_outcome = "failure"；
- source_result = null；
- query_results = null；
- complete_unpaid_scope = null；
- actual_accepted_field_not_claimed = true；
- failure_scope 明确没有最终 producer result，且工程错误、存活/未知 owner 与数学完成分开。

这里的 complete_unpaid_scope=null 表示原 C 科学进程没有生成该账，不是空未付集合。全部 C 科学任务未开始，不能由 null 推出完整覆盖。

Deep 原摘要的 source_result=null、deep_step_outcome="failure"，并保 cut_DN_not_inferred=true。原 cut readout 保 unavailable；没有从此前 144、147、153 或 156 的 cut 数值补填为本次结果。

Projective 原摘要的原字面值为：

- actual_original_result = null；
- original_source_summary = null；
- original_mode_record_count = 0；
- complete_ledger_scope_count = 0；
- all112_original_mode_records_complete = false；
- complete_detailed_source_result_and_mode_cut_leaf_unpaid_records_in_stdout = false；
- original_read_error_count = 0；
- complete_scalar_readback_without_recorded_read_error = true。

最后一项只说明已经出现的 metadata 完整读回无错误，不把不存在的模式数据称为已付。

## 355.5 进程身份、读回和清理

C parent 的原身份为 PID 3240、start_ticks 11576、PGID 2163；far parent 为 PID 3244、start_ticks 11621、PGID 2163。二者共享 runner/job 的父进程组，记录均明确 parent_may_inherit_a_shared_job_process_group=true。读回按 PID+start_ticks 确认原父进程已经结束，没有要求整个共享 PGID 为空。

最终 observation 给出：

- live_original_owned_processes = []；
- unknown_owner_scopes = []；
- quiescent = true；
- parent_shared_job_group_not_treated_as_science = true；
- no_signal_or_process_mutation_performed = true。

原已存在的五件工程文档全部读取：

| 文件 | Bytes | SHA256 |
|---|---:|---|
| C-parent-launch.json | 423 | 66e2c8207f9ee0c83dc0f3f03abfab8a3ee95187d0f103493e507a8d3bc32b6a |
| C-parent-return.json | 420 | bc1c779ce9319ef971f37636745dcc9ef2d0e6fc705e5b68970f29cf0f939c6c |
| far-parent-launch.json | 425 | 5ad0d386a604a592064d049d40ee11861bee0fa64d5644c105d5f48205f984de |
| far-parent-return.json | 421 | 93e8396e9cf2a6007dd73f8560321d53c3efd42daec93fe79ef816006ab98df9 |
| quiescence-before-complete-readback.json | 1271 | bb9c2806b5d60a357aac46d1c06334e52bdfc4d681c2b8a24b04fadedc000662 |

complete-readback-index.json 为 3060 B，SHA256 d24e31957413315389e1810884980a7aacc2d3a03fc0a2eaaecf7dffe93671fb。它记录完整已读范围、没有原最终结果、0 modes/ledgers，以及八个实际 semantic 输出块的身份。这八个块的原 bytes/SHA 均由此次日志读取逐块核对一致，没有重新求值任何科学对象。

原 readback-complete.json 为 403 B，SHA256 1f7a861a750f6a33ab43cfda89476965ebda33b6e246b9798e06adb878fc7f4c。cleanup 事件记录四个实际读回步骤全部 success、marker 与本次 run/source 相符、当前原 owner 已静止；随后记录只删除了 /home/runner/work/_temp/visible-stored-C-projective162。raw_artifact_release_git_upload=false。

这次没有可以当作真实 C/112 传播数据归档的大 scientific raw。清理完成也不产生科学成功结论。

## 355.6 原日志与摘要身份

两份完整 job log 均由同一读取者各取一次；没有另取二进制 artifact。下列 SHA 针对工具返回的完整 decoded UTF-8 文本原字节，含其实际 BOM/换行，不是远端 zip：

| 原日志 | Bytes | SHA256 |
|---|---:|---|
| compute 132877793292 | 163741 | 6ab7a689e0da9485967a992e01954e24a1382c28a58944da1f0263ff69e5b862 |
| report 132878305607 | 31095 | f00763f3c1d16a6b8fd2b75bfa272f9cdeca392f2407cd269e565bb763c82bb1 |

原 C 输出 identity 记 1838 B / 90aaf26c77c43eb38708021a12571e768340fda0c2963ceceb1457a995fe5a02；其完整 JSON 文本不含额外 LF。deep 摘要为 1693 B / 91f5060fc428d0ec9c8b6af3a5d593c10f42e61ab8eddceef2bf0040bf55e489。projective 小摘要为 838 B / 77a626829900104e83e298874c0cbf9451078b569021bab374c972ad0143da21。report 中 C/deep/projective 三份原 JSON body 与 compute 对应 body 逐字相同。cut 是明确 unavailable 的独立输出，不伪称某个不存在的 producer 包已读回。

本地只做原文本解析、字节长度/SHA 与字段对照；科学 source 从未本地 import/执行。

## 355.7 最小修复及仍保留的科学任务

独立修复只改变工作流内层 argv 包装：

    owned_helper exec ROLE SCIENTIFIC_SCRIPT ORIGINAL_ARGUMENTS

helper 验证至少包含 ROLE 和原脚本，随后以 argv[1:] 还原原科学 argv。三处 C/far/linear 调用都去掉那个内部裸 --；外层原 rules runner、其 --command 协议、源码、全部 16 pins、科学输入、资源数值与原数学条件均不变。

仅包装接线修复草稿的身份如下；它尚不含主控为下一次push触发追加的dispatch元数据及其两处SHA替换，最终发布身份见[162接口](../notes/2026-11-15-request162-stored-C-projective-head-interface.md)：

- 同 workflow，74295 B；
- SHA256 14c082c781c17a3ab9fb6a130a0c0303f35839501672036c1979f12886878d0c；
- Git blob 4e595cf4a5bd81f7a92227f142672b07b3d76657；
- 内嵌 lifecycle helper 10320 B / a235458020e47380105cd1e0fe7e68c74fcf5ccbb15cda640209720fcbc6a966。

该修复在本文读回时仅有源码字节，未声明修复后的实际运行成功。现工作流只监听 request 路径的 push，主控须明确形成新一次 dispatch metadata，不能只改 workflow 后宣称新科学已经运行。

R347 的完整两坐标传播、严格 chart pivot、非零振幅符号/因子、所有原 cut 逆像候选、逐候选合法 DN 商后 hull、完整未付栈和全部 112 频率责任继续原样。原 namespace 18900 秒仅用于线性启动时的资源规划裁剪；输入绑定和 runtime setup 排除在线性内部计时外。250 分钟 linear step 与 360 分钟 job 才是实际外层硬限制，2700 秒读回为计划预留，不是无条件保证。

关联：[R347](R347-continuous-C-two-chart-projective-normalization-and-cut-quotients.md)；此前实际156及R339见[本题结果索引](../results.md)。本次没有复用其输出。
