# 第六执行窗：真实完整源、46切口与原件恢复

作者：/root（GPT-6 Astra Pro，AI-assisted）；2026-11-13 UTC。

## 实际执行与完整身份

第五窗的 `/tmp/visible-flex-larger-20261112T2304` 已丢失；原 R97 source 的 SHA 从未读出，故没有重建或宣称原 bytes。使用已归档恢复源 `root_full46_source_cut_transfer_recovered_v2.py`（SHA f989a3f2a07b70d0da36be3a05a87509e9d254215d0a11f7726b48b3767189ef）及全部原始完整输入重新执行。

- R97 恢复：owned session26717，正式 tool/wait4 exit0，25门真，0.08721923828125秒/13384 KiB。完整 primary `2026-11-13-root-r97-full46-recovered-r1.json`，SHA 6d25b27b163f631a44c46c830491807e1713e75f831d2cc4e9486b61f8585f9d；resource/console 同批保存。
- R100 逐项完整源：同一 owned 串行入口，正式 tool/wait4 exit0，12门真，0.9004213809967041秒/15612 KiB。完整 primary `2026-11-13-root-r100-source-reweight-r1.json`，SHA 617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9。源 SHA 58e0d7750faa1e9d58458f238c93f7c6cab3803cef3b776c2f01b494287bb5c1。

R100 所有46模、完整 mean/Neumann inverse 与严格非零 far 均保留，使用其新共同参数域；本次不是把旧 R97/R96 域的数值直接挪到新域。得到 βσ < 6.884236842467072e−49，βwide < 1.169846810756964e−48；wide 完整差 < 2.868811333945762e−64，m92 的 βσ < 1.600096588252794e−77。真正证明数在 primary 的有理数/向上 dyadic 字段，以上十进制只为展示。最紧 m92 比旧完整帽改善约6221倍，先前聊天的三千六百倍为口误，此处更正。

## 完整46切口的真实失败预算

新入口 `root_hybrid46_cut_consumer.py` SHA f2e3e819039b3bb22c35ab993e524be56ff13b8b937d86df4805f6dc7646fc59，owned session41865，正式 tool/wait4 exit2，1.69808030128479秒/16148 KiB；完整 primary `2026-11-13-root-hybrid46-cut-r1.json` SHA cf33eba4dcd1ad4e8fea3e667664b9c356db790851ca8e49d9889a62e408d638，计划/资源/console 保留。exit2由已声明的自映/Schur门失败产生，并非积分、输入校验或进程失败。

消费者核验9项完整输入和源 SHA，保持新 R100 的6个独立轴及40项 weighted-l1输出；外 N 保留全部逐模源与 mean，内头保留两strip、原四正源块及非零far。外源从实际 `weak_candidate_cap` 的逐模 canonical-cut 核，除以 `(17/16)^2` 后乘新完整谱的逐模源及 `exp(-(18/125−1/64)m)`。这一正 majorant 有效但径向过粗：m4 约19.61654、m6约90957.59、m8约70741.82、m10约72.55、m12约1866.22（均按各自原轴归一）。尾组外源总界约1044.11961，最小试验半径下内头约91.51944。

保持 S 半径3/4，T依次取1/64、1/32、3/64、1/16、3/32、1/8、3/16、1/4、3/8、1/2，十个情形的完整自映与正2×2 Schur门均不通过。最小半径完整 S/T 值约90957.59/1135.65。这里只证明该组上界未能闭合；没有不动点不存在、原实际曲率失败、全频PDE或闭面的结论。也不能只用纯线性 S<.258282、T<.014912 代替完整 cut。

接着应直接改善同模径向 source/Green 预算、非远内头逐模传递或重新支付更合适的真参数域。不能删除非线性源、重置非零中心、对40个输出以max替代sum，也不能把失败上界解释为数值真实解。

## 同批稳定科学数据

`2026-11-13-closure-middle-and-r100-executed-stable-manifest.json` 保全实际18段 m94/96 与新域谱，`2026-11-13-closure-r101-actual-stable-manifest.json` 保全完整 R101 证明和90项实际检查。中频原积分门全真，但 Γ、初迹和原 generic216/52 的自映/收缩未付。

`2026-11-12-strong-q096-sameg-m28-local-recovery6-r1-stable-files.json` 保全60件完整数据。M28的新H真复核已付solver门；physical_interpolant_begin之后 child signal9，正式 wrapper exit1，死因未知。solver_success=true 不等于 physical_surface=true。原raw、两次实际tail response及冻结身份可供不重跑Newton的后处理恢复。

tail 的13原件及51依赖本窗重新逐件核SHA；不重算旧PM/PA。新111叶的正A和完整J确实执行，并经显式legacy schema reader读取，保持原g及共享非均值二jet；其小Darboux上界属于新的carrier候选。原→carrier→真实解的完整mean、位置/标架与全场误差仍须另付。

实际pull/两README差异的最新记录见同批 HANDOFF；不把API读取当pull。所有新完整数据通过普通Git归档，不拆分经文本集成搬运，不改变冻结的任何 computations/*.mjs。
