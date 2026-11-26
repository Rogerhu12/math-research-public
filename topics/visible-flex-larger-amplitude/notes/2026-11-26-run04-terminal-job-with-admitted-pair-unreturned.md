# Run04 job终止时第50项的准确未返边界

记录时间：2026-11-26 22:07 UTC。课题完成标准仍未达到。本文只登记公开运行的已见终态，不补写被中断的科学结果。

## 1. 已见事实

公开运行为 [45857104277/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45857104277)，job为 `140038237351`。2026-11-26 22:05:45 UTC，GitHub jobs API仍返回该job与第5步科学控制器为 `in_progress`；22:07:10 UTC再次实际读取时，两者均为 `completed/cancelled`。第10步checkout清理与Complete job返回success；setup-python的post步骤为skipped。这不同于另一次“job取消而科学step已success”的情况。

同次公开小索引的Git blob为 `0d554c1f8c416a7923386830f1c688d29fba108e`。其中最后记录时间仍是 **21:49:59 UTC**，阶段名完整为：

`followup:complete-normalized-SO3-after48-original64-and-pure-single-admission-20261126-run04`

状态是 `running`，实际子进程退出码尚未记录。它证明原单准入pair已真实启动，不能再称只是排队。索引分卷列表仍只覆盖实际1–49；没有第50项完整返回记录。

依据文件为 [运行索引](2026-11-26-public-actions-45857104277-1.md) 与 [实际46–49完整紧凑卷](2026-11-26-public-actions-45857104277-1-part-005.md)。后一文件的完整UTF8为36272B、SHA256 `f8cd7d4919f4270f6fe5729e707bf788c314837c1f20b2a371b27296f923dcf4`、Git blob `3b92cd5f5587f1aa5e7a53be5c972551de45e2a0`。其最后已完整返回父仍是实际48的 `a801cf94cea863374b4453046c09bfb95a24903a8e6bb0e0a7ccbf6915de4b37`；实际49为对应纯归因。

## 2. 已启动的完整请求

该pair源码为 `run_normalized_so3_complete_pair.py`，SHA256 `789f36c490f5f3dbe3e00f627264b048819c4fedda01917c5242e5298ca64801`。完整参数文件为：

[resume-20261126-run04-after48-complete-pair-parameters.json](../computations/resume-20261126-run04-after48-complete-pair-parameters.json)

其13765B、SHA256 `9b04a891a68ddb5f62a851f3b5b7eade9e06a2108e8f8c579e24f04914c68e00`。入口ready为8923B、SHA256 `3eaebd1a787e9d04090c9b14a3073fc7a5cdac2793d97ea5ede9fd1c15e1e41c`。两者及实际48/49结论、完整队列归档在提交 `d1fe0918d7d18b4358dbc699bdb710efb5094222` 发布。

科学child保原 `6c594f20...` launcher、`892f349b...` 全体driver、完整1×64 metric／4×64 restoration、15次ray、8轮SOC、实际父上的两项显式阻尼0.01与全部六地点来源。输出目标是 `so3-closed-actual-profile-cached-backtracked-SOC-v2-fourth/`。其后才是原 `009e1e1d...` 完整纯reader；该reader不会重跑场或方向。

wrapper只保证**在科学child已返回**时继续尝试pure，不能使Actions硬时限消失，也不能保证父进程被取消后仍能运行pure。原workflow为350分钟job预算。这个预算与本次job的时间相符，但本文没有取得受限的原始退出日志，因此不把“具体哪个进程收到哪种终止信号”写成已读事实。

## 3. 不得越过的结果边界

现在能确定的是：第50项已经进入实际执行，而job及科学控制器随后被取消，没有公开完整第50项返回。

现在不能确定的是：科学child已做多少QP推进、是否完成某个真实trial、是否已经发现新地点、是否写出局部report、是否有完整final、是否启动或完成pure。这里的“未公开完整返回”既不等于科学失败，也不等于没有文件或没有新地址。没有据旧a801继承第四方向的任何metric、几何、缓存、停滞或收敛结论。

既有实际48/49结论不受影响：第三方向已完整返回并接受SOC，有限max约0.0339045651、QP仍64次iteration_limit。这远未满足课题的连续完成标准。

## 4. 继续责任

新公开runner应从可公开复现的完整源及全参数再生原必要输入与全部适用方向历史，保留第四方向的完整既定命令，而不能从SHA捏造原raw。新runner产生的第四report是其自身实际记录，不能冒称原第50项字节副本或原第50项成功结果。

完整源归纳表明该族新物理地址只来自原完整历史集合与实际固定观测网格；该结论不消除保护行、typed分支、永久memory、实际网格字节及先后选择的算法责任。仅相同命令、相同计数或相同网格规模都不证明跨runner地点集合逐字相同。06方案明确保留完整再生链，再在其真实完成父上启用已刊当前8列全空间PCG机制，继续完整非线性筛查。

没有科学数组、逐点报告或完整日志被复制到Git、Release或artifact。此次只读取GitHub job元数据、公开小索引及已限定的紧凑卷。
