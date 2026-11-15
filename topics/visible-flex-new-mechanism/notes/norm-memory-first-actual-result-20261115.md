# 同一精确物理状态转移与 norm-memory 的第一次完成实际

日期：2026-11-15。维护：ChatGPT /root/tail_cost（GPT-6 Astra Pro，AI-assisted）。

**公开 Actions 已完成一次新的 norm-memory 优化阶段。** 原完成态的精确159独立坐标、163物理坐标、永久度量 \(g\)、基准 \(b_0\) 及五维高度映射 \(H\) 均准确转移；没有执行旧优化器。两完整网格上的最大真实度量误差由
\[
0.2663817176174397
\quad\longrightarrow\quad
0.26636627797457657
\]
下降 \(0.000015439642863102065\)。最终点通过原两网格物理门、旧度量预算与精确物理盒；**新目标 \(13/50=0.26\) 仍未达到**。

本稿只消费已经完成的公开日志。没有重新运行开发检查、研究计算、旧恢复优化或新优化；没有在本地作新几何评价。对11个模型及费用瓶颈的进一步解释另记，不延迟这一已完成事实的登记。

## 1. 公开身份与输出

| 项目 | 准确身份 |
|---|---|
| 完成 run | [43741276060](https://github.com/Rogerhu12/math-research-public/actions/runs/43741276060) |
| 研究 job | [132894771246](https://github.com/Rogerhu12/math-research-public/actions/runs/43741276060/job/132894771246) |
| 科学 source | c30e7ea00a9ae06356409d5fdae289dfecf2210d |
| workflow | .github/workflows/visible-norm-memory-transfer.yml |
| request | computations/request-norm-memory-transfer.json |
| 返回状态 | complete-two-grid-norm-direction-memory-transfer-audit |
| 新阶段 | norm_direction_memory_stage |
| 原完整 decoded UTF8 日志 | 3,443,509 B；SHA256 5e3be6e199829aee81de637c9e856a5ca0b91caa2154cefec913461c48c136e8 |
| 原 NORM_MEMORY_COMPLETE JSON 子串加单个 LF | 868,908 B；SHA256 f14909e957164ea1bc92363ec228b91cf2adff773270108afe9005d4856d12bf |
| runner 临时 audit-summary.json | 1,336,320 B；SHA256 20821072c90a43e57c8f8b8a12e9b79fd0bd1f6fd66afa4b4dee46ade5f1723d |
| runner 临时 audit.json | 22,153,847 B；SHA256 4b5d7691b7ba9bcf052386f8d2614e44cda702d7343820f87677778be476b3fb |

临时 JSON 没有提交、上传 artifact 或放入 Release。公开保留源码、参数、run、hash 和人类结论。完整日志包含11条 NORM_MEMORY_MODEL；第10条所在行带 UTF8 BOM，解析时只去该行首 BOM，没有漏掉该模型或重写其 JSON 内容。上表原日志 hash 仍保留全部原字节。

## 2. 首次失败事实与本次实际复用的开发证据

前一 run
[43740751558](https://github.com/Rogerhu12/math-research-public/actions/runs/43740751558)，job132893148520，source 3821b425d6405116a44c3ada28d1cc84d50e0a5b，已通过12个新增人工接口检查，之后在实际转移 gate 停止；旧优化及新科学优化调用都为零。

失败是准确的哈希口径错误：新 helper 用整个 metric_model 描述对象的 hash，与原报告中 mathematical_definition 子对象的 hash 比较。前一个精确物理 identity gate 已通过，不能把该错误解释为真实度量漂移。本次只改为核验
\[
\operatorname{hash}(\texttt{mathematical\_definition})
=\texttt{mathematical\_definition\_sha256}
=\text{请求固定的数学定义 hash},
\]
并将 \(b_0\) 的 hash 检查独立报告。原数学定义、门、算法和预算未因此改变。

本次实际输出 NORM_MEMORY_DEVELOPMENT_REUSED，确认：

- 复用上次12个全部通过的新增检查，本次开发执行数为0；
- 110个未变依赖在本 runner 内逐个匹配；
- 已测 recover_reference_heights 函数文本 hash 不变；
- 改动的度量 metadata gate 在本次实际转移中执行并通过。

上次开发原 JSON 子串加 LF 为12,726 B，SHA256
a49ab07833b9c1b0208e3e0cda52b5933673e1bc5846ec638b2d9deb859bcdfd。
其原日志为95,304 B，SHA256
1139f0c7b79ba0ade1de081fe4324d8d4846870282e8ec66e63da904e1fd45c6。
被复用的函数为708 B，SHA256
278c8b7c92c63844d8dcda0691ca18552317e75673463096a00ce9b6693a4e7b。
这不是把已通过检查重新标成一次新执行。

## 3. 转移的是原精确物理态；行池重新初始化的范围明确

唯一旧完成输入是 run43728280256、job132854922848、source
7329385a2dd84a40a271181c017c9a4028ae0f31 的原日志。其字节与 hash 由本次 runner 实际绑定：

- 原日志10,217,369 B，SHA256
  65c4dbae5dd981eae9bb8fa6ffccd338c6988e1b4e1778813ef839025421fddd；
- 原实际 payload SHA256
  472214901278f46f7257787407f7818dd69f05bbc3c420773c7c77ab83e9d060；
- 原最后接受点来自模型5、trial1；最后模型6未完成，未把它计作一次成功；
- 原106源码与原 receipt、本次当前源码的绑定核对通过；
- 精确159和163列表从原完成输出读取，没有把九个物理高度重新舍入成另一模型；
- 旧优化器调用为0，旧开发套件调用为0。

恢复九个参考高度时先在有理数中计算
\[
c_{\rm reference}=c_{\rm physical}-H\tau,
\]
再严格验证所需 binary64 表示。实际结果确认同一九高度参考、同一准确五维 \(H\)、同一163物理末态、同一 \(g,b_0\)。

新 runtime 参考的切向标签显式改变：

| 字段 | 准确值 |
|---|---|
| 原 coordinate definition hash | b685021195473c8b1fede24bc27a90b105cf9ea327eeeb99933b68b78b1d9816 |
| 新 coordinate definition hash | b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580 |
| 原完整参考标签 | 26b4095f68ff238ed04c9e450a53b70a373e6739876ac53cddc9a36a54f9df25 |
| 新 runtime 参考标签 | 262fb5b2535157edfd292f13bf0bf0c3f190d5b6332fd26eba5efcf70d83690b |

把这一参考标签换回原值后，其余 coordinate definition 字段与原 hash 全部匹配。这不是声称恢复了原 runtime 对象或旧完整参考切向向量。原完成态的 coarse/fine \(\eta\) 与最大曲率经本次普通值入口重新评价，四个记录的差均为0。

原后期完整行池没有保存在旧日志中，因此本次明确建立新池：保24份已存输入的全部 coarse/fine 行，再加入原六模型日志中实际存在的原行标签。原24输入计数为4414/3790，合并后种子计数4414/3821；原日志可读的行标签分别152/254个。没有宣称恢复所有后来历史行池。之后的当前态初始化及行学习仍走原入口。

## 4. 唯一新优化阶段的结果

本次仍使用同一原预算：12个共享 LP、40个共享完整值调用、120秒 active 上限；每个 LP 原10秒上限，单主模型至多3个 inner LP。未增加半径或改原物理接受门。

| 项目 | 实际结果 |
|---|---:|
| 新科学阶段调用 | 1 |
| 旧优化器／旧 prefix 恢复优化 | 0 |
| 外模型数 | 11 |
| 主 LP | 12 |
| SOC LP | 0 |
| 新接受步数 | 8 |
| 接受步的实际 fraction | 全部1 |
| 共享完整值调用，含初始化与trial | 24 |
| 独立末端同态两网验值 | 2 |
| 合计计数完整值调用 | 26 |
| 退出原因 | shared-primary-plus-SOC-LP-budget-exit |
| 起始 body radius | 0.000125 |
| 最后 body radius | 0.0000625 |
| 最后增长成功 streak | 1 |

模型2、3、4、6、7、8、9、11得到新接受点。模型1、5、10返回最后已接受点；不能把它们的未接受 \(\eta\) 改善计入最终进展。模型8用了两个 inner LP，其余模型各一个。

norm-memory 只保存原网格/branch 行标识、unit-ball 方向及其来源，不搬用旧数值 \(A,b\)。模型初期每次按当前中心重建7行，后增至9行；最终 bank9个条目、21次插入、0次驱逐。12次向内 binary64 调整已记录，方向范数按原精确 binary64 有理数核验。内模型的完成不能代替真实两网格验收。

所有返回的11个提案都记录 returned_epigraph_gap_met=true。这只是浮点凸模型的 gap 条件，不是原曲面可行性或连续等距证书。本次没有发生 SOC，因此没有新增的 SOC 成功或持径效果可宣称。

## 5. 原完整验收的实际边界

普通值入口仍在相同160个径向节点及原384/768两套完整均匀角网格上评价。selected Jacobian 的计算方式不改变这些普通验值节点。

| 真实量 | 起点 | 终点 |
|---|---:|---:|
| coarse \(\eta_{\max}\) | 0.26638171726382853 | 0.26636627797457657 |
| fine \(\eta_{\max}\) | 0.2663817176174397 | 0.26636627784699285 |
| coarse 最大绝对主曲率 | 57.9999624436237 | 57.99997281528704 |
| fine 最大绝对主曲率 | 57.99998339453157 | 57.9999935999559 |

最终两网格的原物理 gate、旧预算 \(167/625\) 和准确163物理盒通过；精确盒违反数为0，未裁剪坐标。原硬曲率上界58及其数值容差保留。终点 fine 曲率与58的距离很小，不能将其解释为连续曲率余量。

终点还记录：

- coarse/fine 内 strip 余量分别约 \(3.95229\times10^{-8}\)、\(3.95193\times10^{-8}\)；
- 两网格非正则样本数均0，球、正高度和 mirror 条件仍过原门；
- 最终独立精确盒检查通过；
- affine cap 高度余量约 \(-2.78\times10^{-17}\)，重构 cap 余量约 \(-5.55\times10^{-17}\)。它们在原 \(10^{-9}\) 高度容差内被接受，不能写成浮点余量均非负；
- \(\eta\le13/50\) 的新目标仍失败；相应完整新度量合格标志为false；
- 原离散验值不授连续 metric、嵌入、全表面 reach 或有限等距族。

因此，完成态表示“一次新方法执行并保住原合格恢复点、取得上述实际下降”，不表示研究目标已经完成。

## 6. 费用按实际字段分别记录

| 费用字段 | 实际数值 |
|---|---:|
| prepare_elapsed_seconds | 8.848614827999995 s |
| optimization_active_seconds | 38.00514557300002 s |
| run_audit_elapsed_seconds | 150.84028645900003 s |
| process_total_elapsed_seconds | 159.688904402 s |
| 峰值 RSS，Linux KiB | 2,883,936 |

prepare 是原24报告和原完成日志的只读消费、同物理状态重建，不包含旧优化器重跑。audit/process 与 active 的计时范围不同。当前原字段没有把非 active 差额完整细分，本稿不把全部差额归因于网络、JSON保存、物理计算或模型本身。后续费用解释将据源码计时区间和原日志另列。

selected Jacobian 记录 coarse7.628204546 s、fine20.534712244 s；分别11次refresh、110/297批次。完整原163列几何 Jacobian 在这些新 selected 路径中调用数仍为0。此处是本轮实际费用，不拿与旧不同路径、不同接受序列的运行作受控加速比较。

八次接受多于某旧运行的接受数，并不足以单独证明 norm-memory 的因果收益；本稿只记录本轮实际用了12个 LP、11个主模型及其真实接受结果。新的 norm bank、当前行池以及真实路径均应作为后续比较的输入范围。

## 7. 源绑定、规则同步与保留的下一步

本次五新源的 SHA256：

| 源文件 | SHA256 |
|---|---|
| frame_metric_norm_direction_memory.py | f1e62dd9525b5d5b9fe692b903b1b976e04fc46fc8b221788ec60b7b7338def1 |
| frame_metric_norm_memory_recovery.py | 5ebf71025fd1ad122f4c9bdcc7d1c4e14c1789858147a0b076aa3c5b06ebda32 |
| frame_metric_norm_memory_transfer.py | d7816486b01b2373e60ed4e11ab44eb988fad717183baba14e5c13f6b0450f7f |
| frame_metric_norm_memory_audit.py | c53fda1d683550778f553ce403b444ef3bf0ce1db501f5a18272d0f0d857a09f |
| frame_metric_norm_memory_development.py | 244dfbca5085832cbf93457a83f0fcf89bc551db221325a0061fcb163d6259b7 |

公开真实 pull/read 于17:28:35.298991Z完成，before/after均为本次source；根 README blob 21bd547f56590b7f2dd279d0297efb289a9b2783、本题 README blob d0432faff569c8e9af7ed4809847e12880976c11 均无差。

私有实际 pull/read 于17:28:38.580634Z完成，read SHA
797d316120034d95fac313f0c5518c43167c0b84，根 README blob
5ba164843b1f5802184178a82d786264404873a3；规则无差，QUEUE本会话唯一且ongoing。原私有正文未公开。

后继应先解释本次真实限制：小半径模型的预测与实际偏差、三个未接受模型中的曲率/新行、记忆方向重建的实际费用，以及 active 与流程时间的分账。当前结果不授权增加旧预算或重复同一阶段来替代新机制；也不从一次成功推出新方法已解决曲率、完整 metric 或连续几何门。
