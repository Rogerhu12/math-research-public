# B030：完整物理接受与后端轨道分离，保留同一次 SLSQP 的内部历史

日期：2026-11-27。会话：Astra-new-mechanism-1f4a61a4-20261127。
状态：明确新续算输入和源码；本地仅文本、AST、原日志/JSON和SHA256处理，无科学求值。主课题未完成。

## 1. 实际瓶颈与本次改变

[原回溯自然终态](2026-11-26-r566-working-backtrack-natural-final.md)已在完整物理门下取得24次真实接受，$\eta$从 $.25895160785933824$ 降为 $.252604422421174$。但源码每当接受的回溯fraction小于1，就立即抛出 `RestartWorking`。
最后一次接受仅是后端提案的 $1/64$，随后从这个小步重新建立SLSQP。原48次后端启动均没有自然返回；每个启动只完成一个Jacobian。这个明确的重启原因已由源码和原日志共同确定，不猜测旧外部shutdown原因。

本次只改变这一类人工重启：**同一后端调用里的raw轨道与通过全部物理门的best轨道分别保存。** 若只有best因一个已完整资格的缩短步改善，继续原SLSQP调用，保留它自身的raw点、梯度及内部拟Newton矩阵。回调不把缩短q写回SLSQP数组，也不把它称为raw点。
真实工作行/物理库交换、Phase I切换和后端自然结束依旧按原逻辑重启；不是忽略新增约束来强行保留历史。

## 2. 入口严格是实际末态

源科学 run `45851261982`、job `140017925998`、commit `d99eef5312b0c49d78431cc9596f4d48fbc4baa8`。
源运行的自然FINAL由只读恢复 run `45858771537` / job `140043978370`完整公开。新会话只读取这份已有恢复日志，330242 B / SHA256
`6b6c923d4c95994a8f9cb0201370de28126bda033cac91a6bccec15c26974d93`。
其中原FINAL 187092 B / SHA256
`37a188e7e1180036faee661ce07a277e18546101453ed929b83b52149f8e55b0`，与既登记原证据逐字相同；没有重新运行优化或原恢复器。

继承：

- 实际81q SHA256 `59f9471635dc6b99ab73bf4d2e9ab90e6d1c3e12144d6d2766450dd921dbe1a0`；
- 585个必要径向位置、1310个必要峰轨道、1536个整圈FFT点、294个working行；
- 实际trust和原proposal均为 $.3003387451171875$，原trust决定尚未完成；
- pending物理峰/working行均为空；
- 真完整fine/原角峰资格 $\eta=.252604422421174$、几何违约0；
- 实际working可行基epigraph $.25260441924759375$；
- 最后完整必要行数2080010；完整fine为1172×3072，并保所有原角峰定位。

原未接受的大步epigraph $.2507015087316525$ 及raw q仍仅是源记录，本次不以其替换入口。
源SLSQP的内部BFGS/工作数组从未输出，**没有恢复旧内部历史**；所说“保留历史”仅指本次真正新建的同一个SLSQP调用不再因缩短best改善被人为中断。

新stdin配置201987 B / SHA256
`42ec72958995bb906e191c0a16a8520a9972098ceb0128a1fbde6cce34584371`。
里面的 `complete_original_FINAL_JSON` 是上述公开原FINAL的逐字JSON，作为明确下一段所需完整物理库/真实状态/成本参数，原21.77MB日志不提交。
物理定义和更早祖先通过已经绑定的原公开request读取；不复制私有正文，也不对原48个Jacobian或24次接受作科学重演。

## 3. 为什么两条轨道可以共存

每次SLSQP启动时固定working集合及原信赖盒。原 `WorkingRows.fun/jac` 仍是同一组物理函数，只依赖传入的raw变量；它们不读取外部best来改变目标或导数。native SLSQP的拟Newton更新由它自身实际询问的raw点和梯度形成。

回调另外拿raw提案向当前完整合格best作回溯，并完成原全部资格检查。这是候选生成/过滤步骤，不是对SLSQP迭代数组的改写。原fun/Jac cache以实际变量字节作key；回调在缩短点求值之后，后端再查询raw点时会按原规则读取或重算对应key，不能把缩短点的导数冒作raw点导数。

本次信赖盒也保持冻结。raw点位于该盒内，已保留best也位于该盒内，二者线段仍在盒内；源真实q进入新后端前按原物理盒核对。接受best后不重新围绕best移动盒，不偷偷改变仍在运行的约束问题。

因此停止抛出该特定 `RestartWorking` 不要求假装后端接受了缩短点。实现明确记录：raw backend q、实际retained q、接受fraction、原冻结盒、working行数、两种q的SHA及本次内部历史是否仍在同一调用。自然返回时，只有raw终点才是自然OptimizeResult；缩短候选另标 `source_is_terminal_backend_point`，不会被命名为raw自然返回。

这里没有声称这种策略必然收敛或提高效率。其新可检验目标是让一个真实working子问题完成多轮后端迭代，同时继续提供只经全部物理门接受的best。若未选原行阻碍它，原真实交换仍会中断并扩充working库。

## 4. 所有实际接受门逐项保留

以下算法块从源实现逐字保留：

1. 向实际best q及其真实working可行epigraph回溯 $1,1/2,\ldots,2^{-16}$；没有放大工作行容差。
2. 全必要coarse统一角行和全部真实角峰轨道，任何未表示物理行违规都拒绝并给working交换见证。
3. 完整fine，以及原same-q nested FFT均值、metric分量、曲率差门。
4. 全部原角bracket定位、未完成候选处理、真实几何margin和epigraph资格。
5. 实际完整metric严格改进，或完整几何恢复；best q只在这些门全通过后改变。

新增物理峰仍进入完整pending库；新增working见证仍使原后端重启。Phase I真正恢复后也继续强制重新选择metric行。只有“无库变化、无phase变化、缩短best接受”这一处不再强制重启。
原不同时间尺度、全部reach相关必要约束、原物理函数/AD/整圈1536均值不改。当前仅为静态度量设计；没有将局部working矩阵合格冒作完整等距族。

## 5. 文件、实际计费和后继范围

- `scripts/r566_backend_preserving_backtrack_20261127.py`；
- `computations/request-r566-backend-preserving-20261127.json`；
- `.github/workflows/visible-r566-backend-preserving-20261127.yml`；
- lane `rounded-core-B030-backend-history`，公开单job，科学2400秒、预留30秒、job50分钟。

输入保留全部源成本：新段以前已知科学下界7616.754391252秒，三次旧未刷写工作仍未知。新段的全部oracle、Jacobian、回溯、完整fine和峰定位费用按原活跃/退休实例一次归并；没有把省掉重启自动记为负成本，也不把源费用计作本次新求值。
新增计数 `backend_histories_continued_after_shortened_full_acceptance` 区分保留同一调用的真实次数；每次原始事件输出当前raw/best和固定后端身份。源同q同物理库已付baseline与旧方向/restriction检查不重跑，旧未保存Jacobian矩阵不冒已获得。

另外从每次已计算的 `active_rows.fun` 向量和同序working descriptors读取各field最小值，记入raw提案与逐级回溯记录。这只复用当前真正求解已有的数值，不增加geometry、value或AD查询；它将明确区分实际约束回缩由哪些几何组或metric上界组引起。旧日志没有这些分组，本次不倒推或补跑旧49/48步来制造它们。

来源绑定22项，AST、request字节和公开FINAL身份已作静态核对，没有在本地import任何科学源码。实际双仓pull/规则差异/QUEUE仍由现有runner先执行，再移除凭据开始科学。所有科学输出仅stdout；可重算数组、raw和artifact不入库。

达到当前数值误差要求之后仍须真正完成固定g精化、整个C²时间族、宏观握持变化、全域嵌入/reach与可再生网格；本次不因单纯保留后端历史或一段下降就结束课题。
