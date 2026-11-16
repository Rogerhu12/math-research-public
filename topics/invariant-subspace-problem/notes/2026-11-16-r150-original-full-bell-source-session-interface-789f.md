# 完整原 Bell 来源与特征零提升：独立 Actions 执行包

作者：Astra-ISP-789f / normal_annihilator。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

本包把已冻结的完整原齐次来源程序和原 $E$ 支撑提升消费者放入同一个临时 Actions job。它不恢复历史数学大数组。当前状态为源码准备，尚未运行；首次执行会实际解析全部 Python 源、运行双 degree 接口自测，再作原模型数学。没有预填原理想判空、来源次数或精确提升结果。

## 1. 执行顺序与完成范围

第一任务保留全部 $17$ 个原变量和全部 $18$ 个原生成元，对固定合法 coefficient place $127,d=100$ 计算权 $5,\ldots,9$ 的完整来源前缀。先实际核 $(x^2-\tau^2,x\tau)$ 在二阶没有纯 $\tau$ 幂，再把相同前缀连同原来源续到三阶，核出 $\tau^3$ 及完整独立乘回。

第一任务的数学预算依次为 $600,1200,1800$ 秒。**只有源程序真实 exit75** 才进入下一预算；同源码、同 out、同 binding、同 through-degree=9，不反复执行同 600 秒。保留所有已完成原基/来源次数，未完成的当前次数可重做。语法、输入、内存、原身份验证失败不会被默默当作预算继续。

第一任务 exit0 后启动第二任务，在同 tmp 内读取实际正来源。如果没有正来源，第二任务准确记录 completed-prefix。存在正来源时，以 $600$ 秒 / $4$ GiB 求原 $E$ 候选，并核完整三个原多项式分量。只有三者全零才给特征零 $1$ 来源；有限域正证单独不升级。

两个数学入口的来源与证明分别见：

- notes/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-interface-789f.md；
- notes/2026-11-16-r150-original-full-bell-exact-support-lift-interface-789f.md。

## 2. 相对已审 session wrapper 的窄改动

本 wrapper 从 c29935b83498d6ce4bbe96d58953096ab17bb775 原样继承已授权 MR_TOKEN 命令行认证、稀疏 checkout、实际 pull/rebase、双 README fingerprint、HANDOFF readmarker 唯一冲突恢复以及 manifest-only 出版逻辑。未改仓库权限，未保存或打印令牌。

本次改动限定为：

1. 独立 request 路径、工作目录、workflow concurrency 名及执行记录目录。
2. 增加请求给出的 wrapper SHA 门。
3. 对真实预算75使用严格递增的 budgetResumeSeconds，不改变数学来源和语义 binding。
4. 运行数学子进程时每 20 秒轮询；距离上次实际规则读取达到 28 分钟即在后台数学继续使用不可变临时源码的同时，实际 pull 并核两份 README。
5. 外墙到达或基础设施异常时终止整个数学进程组，防止子 engine 或单位求解器留在后台。原源程序的错误和回执照存。
6. workflow 硬限 90 分钟；session 限 80 分钟，同时受 workflow 起点后 88 分钟限制。开任何数学尝试之前，必须能容纳其完整外墙加 120 秒收束时间；不足时不启动新的数学阶段。

每次数学阶段开始前和每次发布前都实际 pull。根规则不变时只记录实际 fingerprint 和提交；若发生真实差异，完整差异打印在 job 日志，当前执行停止，不假称已读新的规则。根可按新规则续接任务。

## 3. 完整三件调度 pin

| 文件 | 完整 blob | 字节 | SHA256 |
|---|---|---:|---|
| notes/2026-11-16-r150-original-full-bell-source-session-789f.py | fa1668cbc7101a7039c97e39abcfab21cf3c703a | 17948 | 0b0406cd92f4db4d1b5e89663cd72d24016baa2d3f2e1710502e780cae1e823c |
| notes/2026-11-16-r150-original-full-bell-source-session-789f-request.json | 731dd47e3f6130f49dd83e1b16c01920ff360782 | 5001 | 06886ca659f30e7c15cd31c40a92c09c72184ccd8e623f0ca5303f2aa8d38cfc |
| .github/workflows/invariant-subspace-r150-original-full-bell-source-session.yml | 4ccc6a2cecdf5502d57a9ac3449027cb699f6541 | 1943 | f0bf314c0d420ecf4fa0e4b249e576c36252bdce20f1446d611b8b53f3b39711 |

前两路径相对本课题，workflow 路径相对仓库根。request 初始规则读取提交采用当前实际 HANDOFF 所记
2596c21030c29e59e9b9d28ccd84a6ef1816d89b；根 README blob 为
21bd547f56590b7f2dd279d0297efb289a9b2783，课题 README blob 为
4d6570e9cf346431ab781a1290076a6321aaaa00。
本包制作时已再次读取两份规则，fingerprint 相符；这不是虚构一次本地 git pull，首次 job 仍必须实际 pull/核对。

## 4. 原数学程序及唯一 helper

| 角色 | 完整 blob | 字节 | SHA256 |
|---|---|---:|---|
| field 原来源程序 | c5e81e3e97d0123df214a994667c5b046171ec82 | 31156 | da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d |
| 原 $E$ 提升程序 | 6aa939b35d07aa9599635089152f5339cf49bff9 | 26209 | c9ea32d71c00a874d79bef49fd6c3b27236e68d7afe70d94289746a9c5ceed25 |
| 未修改的原物理 helper | 7e5244c7c9177d483bb2dbe2a1dc7a2dc86904a3 | 16964 | 31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10 |

request 固定这些 source SHA，并在每次实际启动前从当前提交提取小源码、核 SHA、执行 Python compile 语法门。全部数学数组均来自本次原小模型生成，不读取任何先前失效 tmp。

workflow 安装 python-flint==0.9.0 和系统 Singular。Singular 的实际版本与二进制 SHA 由 field driver 记录；不以 package 名称替代实际接口自测。

## 5. 同 job 临时续接与最终身份

初始只有两个数学任务。任务结束后保留 300 秒空闲窗口，便于在同一 job 追加有独立 step id 的后继；它复用相同 tmp，仍受整体时限。新任务不得依赖一个预算75步骤的“成功”；应依赖已成的真实成功祖先，或由自己严格读取实际 checkpoint。任何跨 job 后继均须重建，不声称 tmp 仍存活。

执行记录统一写到：
~~~
notes/r150-original-full-bell-source-execution-789f/<run>-<step>.json
~~~
这里的持久文件只含脚本/参数、run、实际执行提交、真实秒数、退出码、输出字节/SHA 和规则读取身份。数学 result 从出版对象中明确剔除；完整回执及可续数学状态留在临时工作区，主要结果与诊断在 job 日志。未使用上传 artifact、Release、仓库分块或其他数组存储。

源码语法、Singular 双级自测、任一原身份或单位求解失败，均保留准确日志/回执身份。未运行、预算停止或仅有限域成功时，均不得记录为特征零临界理想已闭。
