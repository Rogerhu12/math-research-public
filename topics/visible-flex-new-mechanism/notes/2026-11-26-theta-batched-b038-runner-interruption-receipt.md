# 分批真实角峰续接 B038：runner 中断与最后完整检查点收据（2026-11-26）

## 原日志身份与实际终止

本收据登记 run [45796862274](https://github.com/Rogerhu12/math-research-public/actions/runs/45796862274) 的 B038 job [139829637782](https://github.com/Rogerhu12/math-research-public/actions/runs/45796862274/job/139829637782)。只在 job 自然 completed/failure 后读取完整原 stdout，不读在途 stdout，不以本地科学执行补日志。

- source commit：cada9c850a1a90a6709bf182bac8b8414497919b。
- 入口 SHA256：ff24fbe2e74a8caf15b78defae454eb36280c310c725a8f9d7a623a511811140。
- request：203607 B，SHA256 1cf3ff0fd598356b7e047fb12a37fa8e12e48c587b2e758ea4247f42f863f22f。
- 完整原 stdout：870264 B，SHA256 b61b3ac15f1f06f7bc76e06deee6cf9d716269ca781e10290a63657ff064c1b4。
- 最后完整 OUTER（outer=2）原 JSON：73733 B，SHA256 cccf85b4464aa97fdd35f03646943f02b5c45c193c4608a66a80d5415a3df262。
- 最后完整 START（outer=3）原 JSON：41697 B，SHA256 1552090fd66c1f2f03607f9b1be1e5995d5fa6ca6d9a6a8603dd8f0a77b453ec。
- 原日志仅保留 Actions 与 scratch；q/峰库仅按后继真实输入需要另作小配置，不复制到本收据。

末尾直接证据是 10:08:07.3656513 UTC 的 runner shutdown signal，随后 10:08:07.7671759 UTC operation canceled。主科学 step 显示 cancelled，job conclusion 为 failure。日志**没有 THETA_PEAK_FINAL、FINAL_IDENTITY、INVERSE_ACTIONS_FINISHED 或自然 OptimizeResult**。因此不能补造自然终态、精确最终科学秒数、最终计数器，不能把 runner 中断称为已声明时钟或容量门返回。这里登记最后完整可识别检查点和已付中间工作。

实际公开 git pull 于 09:58:20.672716 UTC 完成，到 1f42cce3087ba23d38d469aebc03bf35f59ac49c；根/课题 README blob 仍为 282e86b03385d3b6245ce7100ae2e2af7b103c2d / d0432faff569c8e9af7ed4809847e12880976c11，diff 空。实际私库 pull 于 09:58:23.838250 UTC 完成，HEAD 815ee053703dabb40f8b477e7cbe441de5daf8d7，根 blob 5ba164843b1f5802184178a82d786264404873a3 未变，QUEUE 本会话进行中。

## 已付输入与分批定位实际效果

来源是 run 45790610433/job139808369258 的真实保留 q 与全部 actual/pending：470 径向、1536 均匀角、508 额外峰轨道，trust=.9010162353515625。该来源最后941×3072扫描曾因518候选整批被拒，尚不能称角峰已完整准入。

本次 outer0 **实际完成全部518候选、3697目标评价**，解除了这个具体未付定位，不改来源的旧结论。重新得 eta=.5194593774637183、raw V=0，进入 metric 后端。后续所有记录的定位批次都完整结束，512 是 batch size，不是总候选 cap。

物理输入 p=.8、q=.18、rounding=.2，几何预算 R=1.012、Y=.3928、tau=.06072，Ebar 下界 .25、det 下界 .1、working margin .001 与 raw fine 容差1e-8均不变。旧均匀1536实际约束与全部峰库保留；无重做已付 parity/方向核。每次 q 改动仍改变设计度量。

## 按实际资格区分的记录

| 记录 | 实际径向/峰库 | fine 网 | eta 观察 | raw V | 资格 |
| --- | --- | --- | ---: | ---: | --- |
| outer0 START | 470/508 | 941×3072 | .5194593774637183 | 0 | 518候选已完整定位 |
| outer1 callback1 | 479/517 | 959×3072 | .49459115918844376 | 0 | 当时 fine metric 改善 |
| outer2 START，同上一 q | 499/537 | 999×3072 | .49459115918844376 | .000005476319124397833 | 新细网丢 raw 几何，转 restoration |
| outer2 callback1 | 499/537 | 999×3072 | .4946622256480169 | 0 | 真实几何恢复；不是 eta 改善 |
| outer3 START，同恢复 q | 500/538 | 1001×3072 | .4946622256480169 | 0 | 566候选已完整定位的最后检查点 |
| outer3 callback1 | 500/538 | 1001×3072 | .47731378309058914 | .00000159309473346525 | 拒绝；其 q 未写出 |

outer1 的另一个 trial 虽 eta=.4638610682808568，但 raw V=.0029367768678265627，已拒绝。不能拿更低的 trial eta 代替最后合格 q。

最后完整 START 的 q 与 outer2 OUTER 的 last_accepted_or_restoration_q 逐项相等；其实际500径向/538峰库分别逐项等于 outer2 的下一提议，故这些点已真正构造并进入 outer3 后端，不再只是提议。实际 trust 一直 .9010162353515625。

最后可恢复 q 的1001×3072完整扫描与566候选定位结果：

| 量 | 数值 |
| --- | ---: |
| eta（网格与观察最大均为此值） | .4946622256480169 |
| eta 位置 | s=.36328125，theta=0 |
| raw 几何最大违约 | 0 |
| 球半径最大 | 1.0099729278716987 |
| abs y 最大 | .3925971876417379 |
| abs 主曲率最大 | 16.453678487964922 |
| 曲率位置 | s=.69609375，theta=pi/2 |
| mean E 最小 / 最大 | .33988471700177075 / 8.686844326232608 |
| det 最小 | .2355007965858372 |
| z 最小 | .02 |

其 curvature-plus raw slack=.0009326422107700516，比 working margin 少 .00006735778922994842；raw 门仍满足。上述是已完成的有限观察，不是连续 reach 或全角证明。

## 可恢复与未刷出的状态边界

最后 START 完整给出 accepted q、500实际径向、538实际峰轨道、trust，并给出两个新增 pending curvature-plus 峰：

- s=.6949218749999999、theta=pi/2、working violation=.000056471902391107796；
- s=.697265625、theta=pi/2、working violation=.000045006593766715695。

随后最后 callback 报 total_pending_peak_orbits=3、new_pending_peak_count=1，但未输出该新增峰坐标，也未输出被拒 trial q。runner 在下一完整检查点之前被中断。因此只能恢复最后 START 的完整实际状态及两个已写出 pending；还有**一条只知计数、不知坐标的未刷出 pending**。不能把下一输入称为包含关闭瞬间全部 pending，也不能靠猜测该坐标补齐。

若后继从上述最后完整检查点继续，应把这个缺失作为原中断的明确限制，并在新源码中逐 callback 刷出新峰和必要已接受 q，使后续外部中断不会再次丢失。所需重评是新检查点完整接受门的一部分，不是重跑全部已完成 outer。

## 成本：已记录下界与未刷出区间均保留

最后完整 OUTER 在 10:05:56.2789849 UTC 报科学累计 **444.54369729100006 s**，之后 outer3 又执行完整定位、Jacobian、被拒 callback 及后续未刷出工作。444.54369729100006 s 只是本次精确记录的下界，不能冒作总成本。

DEFINITION 于 09:58:31.7910532 UTC 输出，runner shutdown 于 10:08:07.3656513 UTC 输出，两者墙钟间隔575.5745981 s；这覆盖后续已发生而没有最终计数的约131 s 区间。它是日志墙钟跨度，不是补造的进程精确计时。输入链此前已付2668.197903319 s；已登记累计下界约3112.74160061 s，此外仍须携带上述未刷出中断区间成本，不能清零。

可逐条从原日志核验的已完成工作：

- 4次 START、3次 OUTER、5次 callback；1次当时 metric 改善、1次真实 restoration 改善，其余3次拒绝。
- 5个完整 Jacobian、30个方向块；最大值重构差均0；这些 Jacobian 独立计时合计约342.892632146 s。
- 6次完整定位、12个 batch、3314候选全完成、22812次已完成定位目标评价；没有定位 clock partial 或未完成候选返回。
- 最后 outer3 Jacobian 实际 rows=1754520、uniform径向500、角1536、额外实际反射点2152。
- 最后被拒 callback 的 nested FFT 观察差：metric components1.9984014443252818e-15、relative mean E5.409655201508143e-16、tau-curvature3.104356771643779e-15。
- 没有最终 oracle totals；不能把上述可见完成数说成整个 job 的精确总数。

## 科学范围

分批接口完成了旧518候选缺口并产生新的可恢复几何合格 q，eta约.494662。job失败来自原日志所示外部 runner shutdown；同时科学工作也远未完成。固定 g 精化、连续二维误差、全 pair reach、有限等距族及 README 全部门均未获得。后继必须从本收据识别的完整检查点出发，不能升级被拒 trial 或虚构 FINAL。
