# 原35代数与完整奇点门的独立临时 Actions 执行包

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。2026-11-16。

本包只调度[已冻结原数学入口](2026-11-16-r150-original-pencil-trace-and-complete-singularity-interface-789f.md)。它与正在运行的 Bell/Singular 长任务使用不同 workflow、request、工作目录、并发组及执行身份目录。没有历史数学输入，不安装 Singular。

## 1. 固定任务与预算

唯一任务为 complete-original-pencil-trace-and-singularity-gates：

~~~text
--helper {scripts}/2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py
--field-driver {scripts}/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py
--out {work}/original-pencil-trace-and-complete-singularity-gates
--through complete --through-degree 8 --seconds 180 --memory-mib 768
~~~

仅数学程序真正返回预算75才在相同 source、out、binding 上依次增加到360、720秒。完整已成 phase 被按双SHA核验后直接复用；未成 RREF 不冒作可恢复。MemoryError、输入、语法或数学乘回失败都不自动重试。

三个数学预算合计1260秒，已经超过20分钟。因此 workflow 的完整硬界设30分钟，session自身26分钟、从job开始最多28分钟；每次新启动前还要求整段外墙加120秒发布余量均能放入界内。通常首个180秒完成即结束，不空等30分钟。每段外墙为数学预算加60秒。

## 2. 精确规则检查与持久范围

wrapper只对已审 Bell session 做如下隔离改动：

- request、临时目录、execution目录、并发标记改为本任务名称；
- deadline由80/88分钟改为26/28分钟；
- job起始变量改为 R150_PENCIL_JOB_STARTED_UTC；
- bootstrap文字改为本题对象。

授权 token、实际 pull/rebase、双 README 检查、只合并 HANDOFF 读规标记冲突、进程组终止、主源码及全部依赖SHA、实际Python解析、完整临时回执散列和 source/parameter/run-only 发布逻辑不变。

每次数学步骤前和发布前实际 pull/read 双 README；长过程接近28分钟也实际重读。本轻任务的硬界不让30分钟规则间隔过期。初始指纹与2026-11-16 08:42:33真pull一致，冻结时另经连接器核两原blob仍相同：

~~~text
README.md
21bd547f56590b7f2dd279d0297efb289a9b2783
topics/invariant-subspace-problem/README.md
4d6570e9cf346431ab781a1290076a6321aaaa00
~~~

完整数学结果只留临时phase和job日志。仓库提交的执行身份只包括脚本、参数、run、退出码、时长和输出SHA，明确移除数学 result。没有数组进仓库、Release或新数学artifact。

## 3. 固定路径和全部 pins

| 对象 | 路径 | blob | 字节 | SHA256 |
|---|---|---|---:|---|
| 数学源码 | notes/2026-11-16-r150-original-pencil-trace-and-complete-singularity-gates-789f.py | 9c0575db323f24cd278429d4cd787e48b642d062 | 26614 | 4d0fd8ddaa51725b60705813555502036fed310979542aeb2cac8b320b57d326 |
| 数学 inputs | notes/2026-11-16-r150-original-pencil-trace-and-complete-singularity-inputs-789f.json | 63f9908ceeb91e834563a7cf6008f49de956f815 | 3741 | a7193fe13f0a1c5b0a8e31a3104cfe4f129d1f98550728b3eca2e71762eb4524 |
| 数学 interface | notes/2026-11-16-r150-original-pencil-trace-and-complete-singularity-interface-789f.md | cb75451705f0a1f45c681ec955742e62319c9f17 | 9924 | ad771e15a428370c56ab398d1a774af70b1f4f4b3d8fa2a3eb347b78a405dd03 |
| session wrapper | notes/2026-11-16-r150-original-pencil-trace-session-789f.py | b32c3be00d8a4e4894c5f034112feb22fccdda79 | 17929 | b72550fe35e9f931a5f1f671a65ceef497fed1af07acf057ea7ed70c674c758c |
| request | notes/2026-11-16-r150-original-pencil-trace-session-789f-request.json | d60cf2bff480289fb279aabdeadddf2a7785d44d | 3411 | 3a6cf655b987c88bb3d06ac71feeedf24dfcebcbb8651b49e4e3918affd874e1 |
| workflow | .github/workflows/invariant-subspace-r150-original-pencil-trace-session.yml | 124a118709e4417f6508db6b878fc7fc7ff194d2 | 1633 | 5f18ce0d175a6c58f159e388959943cd741a144df82c3b167e8d9f3476aae69e |

notes路径均相对 topics/invariant-subspace-problem；workflow相对仓库根。两个原模型依赖已在主线，request和数学inputs均锁其完整SHA。

每次实际执行身份将写到：

~~~text
topics/invariant-subspace-problem/notes/r150-original-pencil-trace-execution-789f/
<RUN>-complete-original-pencil-trace-and-singularity-gates.json
<RUN>-complete-original-pencil-trace-and-singularity-gates-resume2.json
<RUN>-complete-original-pencil-trace-and-singularity-gates-resume3.json
~~~

只会产生实际执行的相应文件，未运行的续接不会伪造身份。

## 4. 运行前边界

所有数学门仍未执行。源码只在真原单位、完整乘法/余因子乘回和完整Macaulay行来源通过后报告相应结论。迹为零只保有限域结果；某级rank不足只保该级原完整信息。两个有限域原系数正门的E提升分别依赖同原D-free35定理和原E系数单位伴随，不能把任意模127数值结果升成原理想的判定。Bell=1的全部其余原关系仍开。
