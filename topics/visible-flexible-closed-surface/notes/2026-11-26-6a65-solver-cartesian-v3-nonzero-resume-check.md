# 独立 Cartesian v3：保留非零父态的真实有限身份核验

**可信度：已执行的有限接口/身份核验；没有新增实际 Cauchy 或 Cartesian LM 接受，没有连续或 reach 证书。**

v2 完整实验每次以零校正建立自己的新基线。v3 增加自己的 checkpoint 与 matching observer 输入，从保存的完整非零 Cartesian 向量继续同一固定 g、同一空间和同一完整 13 行目标。原 Cauchy 状态与计数仍不能被这个独立模型改写。

## 1. 冻结源与实际回执

| 文件（相对课题） | SHA-256 |
|---|---|
| scripts/6a65-cartesian-independent-experiment-v3.py | ff8070b7915fb3d312f1e6cfcd075f7833708df89129f2cd562a3826d9d67358 |
| scripts/6a65-cartesian-resume-v3-identity-fixture.py | 534a7bab868d06cd1461cf6351904f5fa89b38d4c1cfcc043bfa85f8be85ab32 |
| 原 v2 scripts/6a65-cartesian-independent-experiment-v2.py | 8959a77106e563174c8233b369472dd0fa3e79aa2ff850e560c88e3a4099b418 |

v3 为 33,695 字节，保留已冻结 v2 的完整值、J/JT、LSMR、Armijo 和密观察链。新文件没有覆盖当前正在运行的 cold job 的冻结 v2。小 fixture 与 raw 报告只验证这里的身份/向量接续门，不把 synthetic identity 冒充实际 oracle。

实际命令：

    python /tmp/visible-flex-6a65e705/solver-work/recovered-sources/6a65-cartesian-resume-v3-identity-fixture.py --output /tmp/visible-flex-6a65e705/solver-work/cartesian-resume-v3-identity-fixture01-report.json

实际 OS exit 0，程序内计时 0.003452275996096432 秒。小报告 SHA-256：

    2dbd6f2f9d1aa9b5770bf76b996c617d744c0b70d33613b1c1079cb52defb16e

这份报告明确 actualCauchySourceConsumed=false、completeLMAcceptances=0、syntheticIdentityFixtureOnly=true。源码、命令和确定的测试向量足以复算；报告不作为大型产物提交。

## 2. 保留和拒绝的内容

测试使用实际建立的 J4/M4、52 列基，将全部 52 个系数设成确定的非零值。身份门返回的向量与输入逐值相同，并保留 own accepted=2、own attempts=3。兼容同一冻结 epoch 内的 v2 父态时，也保留相同非零向量和计数，没有回到零。

以下 17 类改动在真实调用 prepare_cartesian_resume 时各自抛出 ValueError：

1. 原 Cauchy 状态字节身份。
2. 实际 run ID。
3. 冻结 source epoch。
4. 完整固定 g/source identity。
5. 完整 quadrature SHA。
6. 数值配方 SHA。
7. 完整参数维数。
8. 原 Cauchy 已接受数。
9. 两端六jets固定回执。
10. 完整 13 行回执。
11. 完整算子源码字节。
12. accepted 数超过真实 attempt 数。
13. 截断的系数向量。
14. 非有限系数。
15. observer 所指 Cartesian 状态字节。
16. observer 所指原 Cauchy 状态字节。
17. observer 的角 primitive 未变回执。

测试中的 SHA 字符串为明确的合成身份占位，不能证明任何 actual Cauchy 输入有效。生产 run() 仍先启动真实 oracle、独立计算原文件/参数/源码哈希，再构造完整固定源 identity；身份门只比较这个实际结果与父态，不替代真实来源验证。

## 3. 生产入口与不变项

首次独立实验使用原有 CLI。续算必须成对增加：

    --cartesian-state ACTUAL_OWN_CARTESIAN_CHECKPOINT
    --cartesian-observer ITS_ACTUALLY_EXECUTED_MATCHING_OBSERVER

其余参数仍为 --scripts、--candidate、--source、--observer、--prefix、--recipe、--source-epoch 和 --run-id。这里 --source/--observer 始终指原 Cauchy 输入及其真实观察；新增两个参数指独立 Cartesian 模型自己的状态及观察。四个原件都必须实际存在，不能用日志中的哈希替代文件。

生产复核包括完整原状态/候选/原 observer 的字节身份、同一 run/epoch、固定 metric/source identity、basis.definition、维数、gridSHA、全部 pointConfig、配方，以及实际 matching Cartesian observer 的状态哈希和三项未变回执。当前 revision 或同一冻结 epoch 中的原 v2 entry 字节才可作为父入口；v3 额外保存 stream、完整点算子和 oracle adapter 的字节身份，后续不得悄悄换算子。

每次尝试先对实际保存向量完整重评 baseline，随后执行相同全列、全 13 行 LSMR/LM 与实际完整 Armijo 试步。若接受，own 累计接受数恰加 1；若合法未接受，完整输入向量与累计接受数保留。attempt 数记录真实调用次数，不把拒步写成接受。每次仍实际执行密观察，产生自己的 observer 字节哈希；完整源和 fixed g 不因 observer 加密而改变。

新状态和标量报告分别写明 parentCartesianStateSHA256、parentCartesianObserverSHA256、priorOwnAcceptedSteps、priorOwnAttemptCount，以及 ownAcceptedStepsAddedThisAttempt。原 Cauchy 计数增量始终为 0。父原件在进程末再次核 SHA，拒步会检查实际保留向量。

## 4. 本次边界与下一实际支付

本次 --help 导入实际 exit 0，17 个身份拒绝和非零接续也已真实返回。尚未用本 v3 在一个实际 Cauchy checkpoint 上执行新增 LM；当前 cold job 的一次 v2 尝试和长强分支 Cauchy 步数必须各自按各自真实回执报告。

后续同 job 协调者应先真实产生或消费上述父原件，再调用 v3。若另开 job 重生旧前缀，旧科学接受只作恢复输入，不记为新的研究结果；结束 job 的 raw 不得从不存在的路径或日志哈希冒充为仍存活输入。
