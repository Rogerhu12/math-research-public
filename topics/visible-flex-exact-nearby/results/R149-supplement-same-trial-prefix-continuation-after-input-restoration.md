# R149 TC continuation：原输入重物化后同一个完整残差前缀的续算

**已证明（metadata 修复不改变数学对象或已完成量）。**
会话 `visible-exact-astra-fb31ed6-20261127`，2026-11-27。

本说明对应独立
`fourfold_codazzi_true_root_trial_continuation_owner.py`。原正在执行的
`fourfold_codazzi_true_root_trial_owner.py` 和本次已钉住的输入完全
不修改。适配器不自动启动，不允许把仍在运行的执行当成已结束前件。

## TC-C1 实际计数的含义

run `45889161044/1` 的完整 execution 将必要 Hermite 输入重物化
如实记为 `old_numerical_producers_called=1`。其完整
`necessary_input_reconstruction` 同时保留：

- 单独 child 数为1、returncode0、`complete=true`；
- 原 nodal answer 的完整 SHA；original nodal QR 没有重新求解；
- 重物化的6144-piece整 cubic 与原 cubic SHA 完全一致；
- 14份原 direction shards 的全部 bytes/SHA逐一匹配；
- 所有 mean/nonmean 列及原 one-sided derivatives 完整保留；
- 原 residual/norm 目标调用数为0，未发布新数组。

原 owner 的两处 predecessor gate 却要求该 producer 计数精确为0，
因此会拒绝这个已经如实保存的必要输入恢复。把旧执行计数改写为0
不是修复。本适配器保留整个旧 execution，只在两处 gate 调用完整
恢复资格函数：它要求上述全部字段、原 immutable container、原
runtime、`OPENBLAS_CORETYPE=unset`、原 source、全 cubic SHA、全部
14 shard SHA 和完整 direction index SHA。任何未付的旧数学目标
重跑均不能通过这个 gate。

## TC-C2 原数值源码保持逐字相同

适配器加载的完整原 owner 必须为63363 B，SHA-256
`193a317166204eef3870f12e5aee08be5a3de46e18b65de4b471b2a478f253dc`。
源码上的替换是有限、显式且逐项计数的：

1. `SOURCE_PATH` 改为适配器自身路径，使 actual 正确记录实际执行源；
2. 四个 predecessor/prefix source 等式改为完整 source 兼容检查；
3. 两个 owner-manifest 全等式改为完整原 owner/本适配器绑定检查；
4. 两个错误的 producer==0 判据改为 TC-C1 的完整恢复资格；
5. 插入三个只读 metadata 函数，不导入数值模块。

其他原源码逐字保留。特别是所有 parameters、radial trial、true
root、exact certificate partition、integrands、全96列/all5 sources、
有向累加和、finite signed pairing、最终 norm 公式及完整读回全部
保持不变。

九个 `scientific_sources` 字段中，八个原 numerical source 的 SHA
必须全部相同；只有 `owner` 可从上述精确63363B源过渡到这个明确的
metadata adapter。旧完整 owner 源同时作为新 manifest 的
`original_TC_owner` 全文件输入，原 manifest 中的 owner bytes/SHA/
Git blob 必须与它完全一致。以后同适配器的连续续算也要求 owner
本身全等；任意第三个 owner 不被兼容函数接受。旧源身份不会被
改名成本适配器的新 SHA。

## TC-C3 原完整 trial 与完整累加器继续使用

原 `proposal_identity` 必须精确一致，包括全部4个 endpoint 数组
的完整 shape/bytes/SHA、trial definition SHA、certificate plan
SHA、真 root index 和原 proposal source SHA。因此由私有临时载体
不能持久保存而必要进行的 trial 重物化，只能恢复同一个精确 trial；
不能更换浮点近似、改网格或接受新 SHA。该重物化不提供新数学结论。
原 nodal BVP/QR 不求解；原 finite trial 的选择算法若为重物化所需
则照原 immutable runtime 执行，随后以全部整数组 SHA 验明原件。

所有已经正式完成的 matrix/negative/positive 自然对象必须整份
消费，并按原 bytes 原样继承；其原 producer manifest SHA 永久
保留。不能删除一个已完成对象，再把它列入新目标。三项都完成时
拒绝启动任何新科学。

完整 radial prefix 保留所有96列、全部5种 source 的非负 directed
binary64平方和及 canonical hex 编码。继续从保存的 `next_cell`
开始；此前的积分 cell 不再计算。原 proof 的分段可加性与非负上界
累加表明，前缀原上界加未完成 cells 的新上界，仍是同一完整原
积分的上界。最后完整负、正两侧对象及其 norm 只在全所需 cell 到齐
后形成。

## TC-C4 运行边界

新 generator 要求完整 actual 前件 manifest、execution，以及该
execution 列出的每个自然数学对象。原 `actual_child_returncode`
必须已经是整数；`null` 的运行中快照仍拒绝。原已失败分支如实
保留其 failure，不重标为成功。新的科学目标恰是尚未完成的完整
原对象，发布仍执行周期 pull/README 差异检查、完整容量规则和
非快进立即 rebase/push。

本说明不认定当前 run 已经结束，不宣称尚未计算的剩余 residual，
也不授予真实 PDE inverse、signed finite inverse、physical means、
$\nu$/phase Schur 或课题完成标准。
