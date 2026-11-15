# 已付m7同模型接口：身份恢复成功，粗网冷恢复耗尽原时间余额

## 原始执行与准确结局

公开 run43773136836 / job132993290386，源码
403a2fcf430f0ed98b5731256befe36bb833eadf，于2026-11-15 23:12:30 UTC
以 success 完成审计。原job日志535910B，SHA256
cc813391bf5ad57537d9f6d7176d01ece44cbaec42f6e616e22746e18a34fb7c。

审计完整不等于优化成功。真实stage为
shared-value-time-or-pool-budget-exit，理由为
shared curvature-exchange optimization wall budget reached; full-grid best preserved。
当前粗网的一次必要ordinary value冷恢复返回后，原120秒active门已经超限；
随后停止，未进入fine恢复、selected J、完整模型、见证支持或LP11。

本次新共享值1、新model0、新LP0、新SOC0、新接受点0。
原LP账仍10/12，两个未调用槽不能绕过已经耗尽的同epoch时间门。
该一次续算接口的实际结局已经记录，不能重启同m7、重付这次粗值恢复或仅增加
时限来把它改写为成功。后继工作转向真正的新冷评估/缓存持续性机制，并继续open中的理论问题。

## 身份错误已经具体修复

[前次失败及16条收据](paid-attainer-first-checks-and-identity-stop-20261115.md)
和[最小修复](paid-attainer-objective-identity-repair-and-paid-check-reuse-20261115.md)
的两个哈希域在本次都与原记录准确相等：

| 对象 | 原值及本次恢复值 |
|---|---|
| 完整objective定义 | 55d6c6275d51500408c36d8fc40cbe8c687607473baf4f3d1df2e3078ca68fe4 |
| 普通field几何求值定义 | 047cefae968152d170387cf64a9f7b0f132089685472c10868de9379967d93e9 |

完整objective原值来自原MODEL7粗、细两项external_current_cache_binding；
不是将field的047cef改名充当该值。历史initial375与当前438保持各自原事实。

PAID_ATTAINER_DEVELOPMENT_REUSE.passed=true，paid_development_checks=16，
new_development_check_executions=0；本次没有DEVELOPMENT新执行标签。
原143份Python及六份workflow冻结，core/development/recovery无改动；
只有已声明的transfer/resume/audit/workflow四文件变化。原18及更早20/19/26/cache
只消费原回执，无旧优化、旧LP10、旧direction或旧人工研究重放。

## 首次冷恢复的真实成本

| 费用/计数 | 原已付及本次准确值 |
|---|---:|
| 原epoch active | 35.54239845799998秒 |
| 首次身份失败追加active | 0.08626015199990889秒 |
| 本次开始前合计active | 35.62865860999989秒 |
| 首次身份失败prepare | 14.667315975000065秒 |
| 本次prepare | 14.011384722000003秒 |
| snapshot累计initialization | 293.5427817930001秒 |
| 本次定义/计数恢复 | 0.10981774499998664秒 |
| 本次恢复与原recovery完整墙钟 | 205.785849204秒 |
| stage记录本次新active墙钟 | 205.785845752秒 |
| snapshot累计optimization active | 241.3142038439999秒 |
| 原value_geometry | 212.6957086999999秒 |
| snapshot累计value_geometry | 418.14400135099993秒 |
| 本次唯一粗值的value_geometry差额 | 205.448292651秒 |
| 本次进程总耗时 | 224.82047854200002秒 |
| 本次峰值RSS | 548340KiB |
| 累计共享完整值 | 15/40 |
| 本次新完整值 | 1 |
| 原独立末验值 | 2，仍为原收据 |
| 本次额外独立末验 | 0 |

原initialization264.864081096秒加两次必要prepare，得到表中的293.5427817930001。
首次失败process总18.621493514000008秒另列保留，没有在本次计费中消失。

原wall门是在原值调用之间检查，不抢占已经开始的一次ordinary value。
所以这里如实记录累计active241.3142038439999超过120，而不是声称运行在120秒内完成。
该调用返回后没有继续付fine、J或LP。不同墙钟字段在snapshot与报告收尾的不同
时点取得，不将其微小末段差值冒充新的几何调用。

## 未执行的部分与当前物理状态

factorized_selected_J_execution的coarse、fine两侧refreshes、batches、
metric_observable_seconds和total_seconds全部为0；complete_original_grid_oracle_progress为空。
没有全网方向scan、重建当前完整cut模型、加入四见证支持、LP11或SOC12。

当前438 bank输入恢复本身passed=true，原顺序、binary64 normals及
state SHA1a1d55857ed7ae7734054126cec38c9d99e72ce144ab321152c3f5fab8fd10fd相同。
当前模型上的bank/A/J完整绑定仍为pending-restored-model-no-new-LP-yet；
没有把输入恢复通过写成尚未构造的模型绑定通过。
原bank insertions626、evictions0、inward adjustments309仅恢复历史计数，
原rebuild事件没有重执行。学习仍8events、7commits、pending空，state SHA
57aeeb039749c574598477d41764c7651b7314c8530f150c83d3691815ade498。

最佳物理身份仍
e0ab278d1525c90a2be30db12c78e6faac369a8b8d01f0236f4fe6fd02e79f83；
池4432/4525、版本1/2、B=.00025、两streak0，没有新接受点。
原eta=.26623355613853394，原两网最大曲率57.99982504159888，本次eta改进0。
.26目标、主1e−6同g精化以及连续reach均未达。

最终每网十四个true布尔明确来源于run43767357527对这一未变最佳点的独立末验：
cap_and_box_eligible、curvature_lambda_bound_pass、
curvature_scaled_PSD_row_pass、hard_ball_pass、hard_strip_pass、
independent_direct_curvature_pass、independent_direct_mirror_radius_pass、
mirror_polynomial_pass、outer_strip_pass、previous_metric_budget_pass、
regularity_screen_pass、signed_height_pass、
single_grid_admissible_recovery_point、single_grid_hard_gate_pass。

这些不是本次重做了两网十四门的声明。唯一新的粗值没有组成新两网接受回执；
未作额外初末audit，也未用源收据伪装新geometry。eta仍不是delta-hold。

## 可复核的原记录身份

下表为标签原JSON加一个LF；只有身份和人类结论入Git。

| 标签 | 字节 | SHA256 |
|---|---:|---|
| PAID_ATTAINER_REQUEST | 22686 | cb69758c6f3f55b36a3c414544ab29b0324bafdded2893f5749b0b23fb947f85 |
| PAID_ATTAINER_DEVELOPMENT_REUSE | 1843 | 5e5ca516b043cad6f0fc2095c02da7a957678b2c3062889ca48b63354cf1d3e9 |
| PAID_ATTAINER_PRIOR_WORK_REUSED | 1135 | 46480623a3a683dd1a202c9b1f2f47f7105ca43580c5e64d85aa1546a1944661 |
| PAID_ATTAINER_COMPLETE | 427204 | a7d11e25eddac7c020bcf26422dcfd4364cc8fd98c5b7d1e1f3d4dcd09e77db3 |

原request38587B/hash
f79198de2d443175bb7491b6f042a3cca90b2bb39fc74a32dccd2df0929095b6。
临时audit.json4344700B/hash
0d8d692fdd1d4d59bf898390a187fd2a58798182801e330eb4a632609ff4f4c9；
audit-summary.json635544B/hash
6c9e313e2a92030bfddcfd35f91a00c8429c40c1097283b92cecfb64e1056692。
均未提交、未上传Artifact或Release；runner内存中的冷缓存不当作已持久保存。

## 每次实际拉取与规则

公开实际pull为23:08:36.058840至23:08:36.464683 UTC，
before=after=403a2fcf430f0ed98b5731256befe36bb833eadf。
根README与本题README diff均为空，仍为blob
21bd547f56590b7f2dd279d0297efb289a9b2783和
d0432faff569c8e9af7ed4809847e12880976c11。

私有实际pull为23:08:38.980070至23:08:39.556525 UTC，
before=after=88cebd4cb69050a8430a30df3fd63244c20b598d；
根README未变、本题README不存在，QUEUE唯一行仍为本会话进行中。
root已读取双回执；下一actual pull不迟于2026-11-16 00:08:36 UTC。
同模型接口结束不结束主课题，HANDOFF/open继续记录下一真正未付工作。
