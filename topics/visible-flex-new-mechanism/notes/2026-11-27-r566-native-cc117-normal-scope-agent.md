# B030：从实际 cc117 原恢复阶段继续的正常 native 范围

2026-11-27。此稿声明一份新的正常续接输入；本地只作文本、AST、JSON/原日志解析和字节身份核对。科学只在本公开仓库 Actions，主线程发布前不触发。

## 1. 为什么这次直接继续当前正常流程

[原自然终态](2026-11-27-r566-native56594-partial2561-natural-final-agent.md)已经闭合原剩余 2561 个峰，得到一次 source restoration 接受和 12 次新 metric 接受。最后保留原物理点
`cc117d48551e8b457bda12450e466f7e2dcff174311675b5e3445487bc9c6a30`，
η=`0.19917454273148172`。它没有自然停滞：原 2370 秒科学工作边界在 outer20 新 Jacobian 尚未完成时返回。

新源 [`r566_native_cc117_normal_resume_20261127.py`](../scripts/r566_native_cc117_normal_resume_20261127.py)只恢复当前必要状态，移除已经完成的 source2561 入口。原正常 for-outer、工作回溯、原接受、全部完整值资格、真实峰、新库交换、native history 延续以及成本退役块与已跑源逐字相同。它不是重放原 40 分钟范围，不重做已闭旧峰，也不新开一个旧资格诊断。

源文件为 59,233 B，SHA256
`f73dc0614460d526ab05623f982a667c15bee883ce619e4d8b2ee839b9732313`。
来源执行源 `r566_native56594_partial2561_20261127.py` 的 SHA256
`c972c56133ff68705a91434d5ceeb404d5d7fe818d2cf168e2ac2b29efdfa09a` 仍被新源准确绑定。

## 2. 原件与当前输入身份

唯一来源为 run45924048811/job140261163768，source/runtime pull 均为
`042435b253617f260442a47fdf4c3d1a92698ae1`。
原 gzip request SHA256
`a89bb1b8886576345ef7bca4f82fd6ff8b32ba257093b719446db3e9e567d884`；
stdout 29,097,972 B / `6c081453125b616e15896b62e0bcbf2c199bf4470aa736274568eeb5a1923ed6`；
唯一原行 FINAL JSON 392,448 B /
`5c5181a8cf7899c19677a02961ed903aab7b1d25fe4891531e65b4c08d96ca19`。

必要输入包含该准确原行 FINAL、原实际 definition 的 physical/geometry 参数和最后 backend 已输出的原标量行数。全部历史费用在 FINAL 中完整嵌套保留；不另存一份大 stdout、重算轨迹或已经完成的峰证书。

physical parameters 的 canonical JSON 为 259 B / SHA256
`4fa67643c13c83e4968938a0185720522c5fb7e1349bb26c78c4af2e27f33798`；
geometry parameters 为 91 B / SHA256
`b733187ae8b75a48b2bc386bc7b8cd23fd1d62f52c51cb193320e22d8e5b861c`。
新源从这些原实际参数直接构造同一个 `hard.Parameters`，不为取得模型定义调用旧 partial 的 `source_input` 或局部化函数。

| 当前对象 | 准确来源 |
|---|---|
| 81 维原物理 q | `cc117d48551e8b457bda12450e466f7e2dcff174311675b5e3445487bc9c6a30` |
| coarse 817 半径 | binary64 `5aa6b17662003fddff6f552c212d368b8af2226240ffc3c59e3fd16a8aedb849` |
| 当前必需 fine 1636 半径 | binary64 `df0f7caa447a3f57536731360a128b9a706d15f293e9b176f33d7de68c0c7d28` |
| 已合格 fine 1630 半径 | binary64 `06628dc4f5a683a451c3af96e2c99f62b08f961c6614425c6de4e46f9b04c5af` |
| 1829 物理峰轨道 | canonical `bd7c8d4225aff8c05bef89b19e35ebbda7cf619201cf1c7e6e2a4a087663e093` |
| 334 working 行 | canonical `9c74630ab5c93f5d21106acea04eeaae13e4f33e3a0031e60cd5758d709bb356` |
| physical / working pending | 0 / 0，原新证据已在当前库中 |
| 原 FFT / fine FFT | 1536 / 3072 |
| 原 actual / proposed trust | 都为 `0.45050811767578125`；decision 未完成 |
| 当前 phase | `geometry_restoration` |
| 当前原 extra | `0.010116929159975741` |
| 已付当前 phase-I scalar rows | 2,261,160 |

current-complete-library-values-known=true 只复用当前 q/当前完整 coarse 行库已付的值选择及行数。保留的 `best_scan`、`best_observed` 与 `best_fine_nodes` 明确仍属于原 1630 网格；`actual_fine_nodes` 是当前 1636，二者分别恢复。后续真正新候选需要当前全 fine 和所有原门，不以 source1630 代付 source1636。

## 3. 准确恢复 best-geo，不再需要逆舍入推测

来源已经准确输出
`g=0.00011692915997574185`。其 margin-state 为单值 lower=upper、possible-count=1，canonical 515 B / SHA256
`1508f53acf269470e335290cb29eba954a795d39be0c1b528135e349516f208d`。
`origin` 保留它从新 paid coarse 做原 max 更新的历史。

新入口用同一个冻结 `OriginalMarginState` 构造器恢复这两个原端点和原 origin，并要求生成的 receipt 与来源逐项相同。它不执行此前的 inverse-rounding 构造，不取 `e-.01`，也不把已合格 fine 的 geometry-violation=0 覆盖这个原工作余量。原 `phase(tolerance)` 必须仍是 geometry_restoration。

原 extra 是已输出值，直接带入初始 x0。若新 trial 真完成恢复，原正常分支才进入 metric；原 phase I 接受可以提高 η，不能用 metric 单调条件替代。若恢复尚未完成，仍用原准确 `g_trial < g_best - 1e-10` 判据。这里原 scalar 已明确，没有额外区间分支或新资格门。

## 4. 真实 H/pending 载入和原语义重置

新范围完整载入原 `actual_curvature_checkpoint`：

- canonical 83951 B / `5194fe701ef8f005ec6e30a7a15e1cc3e235fbf66d8a32db8e6d54173f86c897`；
- 82 维、3403 个 packed LDL entries，binary64 SHA256 `6f2a9a605c4485364a5666501b7a77b13ad2ff6c3eada967a59fe460a9d132e8`；
- 同一模型 identity `8a1abe70f785c8c1d8e80b884aa58299598846c716c1be63b0d7b3e9421414a7`；
- 原行函数 signature `505f8cbcb0a22bc114da97754d0903cee340381ff6237c868c947f04e71452c5`；
- pending 的 82 维 anchor、82 维固定乘子梯度和 23 个准确非零乘子均原样保留。

这些是此前最后一个 **metric** QP 的真实材料。outer20 当前 phase 已变成 geometry_restoration，但它尚未完成新 J，故 helper 尚未在原 job 内完成这次语义重置。新源不修改 checkpoint 的 signature，也不手动把它改称 restoration H。

冻结的 `r566_true_secant_curvature_20261127.py` 自身把 phase 纳入行函数 signature。在新 restoration 原完整 J 到达时，`_prepare` 按原语义判断丢弃旧 metric packed-H 和 pending，并从原 identity 初始化；后续只用同一实际目标/同行定义的已付 J 和 QP 更新。没有跨 phase 固定乘子 secant、没有恢复未输出的 native workspace，也没有为初始化额外跑一个旧 J 或旧曲率诊断。

原 H/pending 仍完整载入是为了保存实际状态和费用，而不是要求它跨目标生效。相同语义下后续行交换所允许的真实 secant/native 初始化继续按原 helper 运作。

## 5. 旧拒绝轨和当前保留轨分别保存

原最后 raw `5fc69e2c…` 工作门失败；后续 fraction1/4 完整 trial `5e199a34…` 的 fine/峰/nested 全闭，却因原 curvature-plus 工作 margin 峰 `0.0001248759423130288` 被准确拒绝。没有未处理峰队列，也没有可以越过原判据的较低 η 新候选。

新入口保留原 `last_trial`、`last_raw_backend_trial`、`last_working_backtrack` 和原 backend-anchor metadata，作为已发生的源证据轨。新的 `q` 始终是 `cc117d48…`；旧拒绝不重新提交，也不自动变成新 callback。第一次真正新 trial 出现后，原正常流程才更新这些轨。

此处保留的是来源 metadata，不是恢复原完整 SLSQP workspace。新 backend 的完整模型请求、实际 QP 和 backtracking 全部按原流程重新产生并计费。

## 6. 必要重建与完整费用范围

来源有 25 个完整 J、1701 个已付方向块，其中 21 个属于最后未闭的新 J。这 21 个部分块已经包含在原 elapsed；原未输出完整矩阵或工作数组，新范围不得宣称复用其数值。新真实 continuation 需要的完整 working J 会实际重建并计费；既有完整 coarse 选择、source2561 局部化、旧已拒 trial 与旧已付 fine 不为此重播。

新范围完整保存来源 cost 对象（canonical 29530 B / `3efa1236aada84335f7407b8444c2da40f1be6affc093ffc510e638cd97227cc`）。此前科学秒数下界 `21840.621857510`、来源所有接受/J/FFT/局部化/native 工作和更早未知删失费用都带入，不能将新 counters=0 误作历史费用清零。

全部 20 个原 common 参数逐项继承：120 outer / 80 maxiter、原 trust 上下限、49 径向基准、1025/2048/1024 各原库容量、原 batch/directions/working witnesses、原角度/峰/nested tolerance、16 回溯步均不改。仍是 2400 秒原总范围、30 秒末预留和 50 分钟 job；没有以完成标准为由硬 kill，也不把耗时到了标作课题完成。

新 native 源下载、编译、import、H 算术、必要模型/FFT 准备、完整 J、失败试步、峰局部化及未闭操作全部进入同一科学时钟。原原子边界协作退出、原 FINAL、partial 队列输出和所有费用出口保留。工作行只是局部矩阵选择，原所有物理行与 full fine/峰/nested 接受门继续存在。

## 7. 源和入口的可核对差异

相对于已跑 56594 源，改变限于：

1. 新来源和输出 schema，以及原源字节绑定；
2. 原实际 definition 参数、原 FINAL、当前库、准确 g 和旧 metric H/pending 的明确入口；
3. 用原已输出单值恢复 g，保 source 已拒轨 metadata；
4. 删除已经闭合的原 source2561 入口，直接进入原正常 for-outer；
5. 新范围的 source/cost 说明与 counters；原旧账完整内嵌。

原正常 for-outer 到所有 inner callback、native 调用、原资格和退役的连续 29,831 B 块与来源逐字相同。`CURVATURE_MODEL_IDENTITY` AST 相同，旧 helper/patch/native build 源全部冻结。

使用已经发布的 gzip stdin 启动器，只给必要续接输入一个 gzip request；不另造新的 runner，不把令牌传给科学子进程。公开/私有规则 pull、README diff、进行中 QUEUE 校验、环境固定与去凭据链保持。workflow 仍使用原 B030 concurrency group 且 `cancel-in-progress: false`，只在该新 request 发布后自动触发一个范围。

本地确认限于源/AST、原日志和 JSON/hash。没有构造科学对象、跑矩阵、求峰或重新检查一个已付物理点。该正常范围仍只是对原静态 B030 输入继续求解；不宣称固定 metric family、连续角度覆盖、全域/全时 reach 或主 README 完成。
