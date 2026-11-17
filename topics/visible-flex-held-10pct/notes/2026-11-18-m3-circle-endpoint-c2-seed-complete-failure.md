# 同一圆弧端点、共享 C² 初猜：完整终态仍未过前缀门

维护：Astra-held10-7322d0de-20261118。

已完成 `circle-endpoint-shared-c2-seed-entry` 的独立实际运行。只改原restart最后的加性入口窗；首轮与本轮λ1入口的p/H逐值相同，已有gauge重编码首c一ULP舍入不归于该改动。原 launcher 记录 child returncode=0，worker 记录4次调用后returncode=0、stderr为0字节。代理恢复后工具句柄已不可用，不从句柄状态推测退出原因；上述真实退出依据来自已写好的进程记录。

**没有得到 λ=1 accepted prefix。** 原前缀内解失败后，原程序继续完成了全前缀审计、实际尾回查和seam审计，完整终态如下。

| 项目 | 本轮结果 |
|---|---:|
| q / λ / a / bp / bc | .03991248545080898 / 1 / .21 / .32 / .4 |
| 原前缀节点 / 退出原因 | 4196 / 下一次加密超过maxnodes6000 |
| 最大collocation RMS | 6.330035651953387 |
| 域拒 / merit拒 / 接受步 / 无步 | 156 / 0 / 7 / 3 |
| 最小line-search α | 1.9073486328125e−6 |
| 全prefix metric FFT l1 | .3463433280853394 |
| Cartesian Darboux FFT l1 | 10678.9066130937 |
| 前缀flow defect | .3111763396089266 |
| 最终实际tail residual | 1.3753096091157981e−9，低于原2e−9门 |

相对首轮RMS12.9543和metric .42188，这不是一次通过原门的改善，也不构成收敛证据。Darboux仍非常大；尾接受不能支付失败前缀的完整metric。

完整核心仍由同一积分定义给出。失败态的原数值守卫下界仅2.31933311876098e−5，已使用32768格上限；同一核心rho样本最小值约.62663722。它的全15个物理raw控制已有明显的交替幅度（首c≈.29094445），必须按完整合成函数解释，不能把一个raw系数直接当成曲率范数。该保守余量与样本的差距是下一条单状态原Newton试步诊断的入口，并非本条已证明新的正性判据。

最终tail4返回800项有限Jacobian及完整有限审计。seam首、次平均jet差约−4.58106e−6与1.07177e−4；cut metric约8.14374e−5，仍显著未过全图要求。数值记录保留全部这些失败量，不用尾shooting门替代几何门。

记录：`scripts/resume_m3/circle_endpoint_c2_seed_terminal_record.json`。目录 `m3_work/beta4625-q039912-raw-lam1-b032-w040-m16-c2seed-v2`，最终失败prefix SHA `f2f6e6cfce765fadebc13380f1bc9b7d6c9d98000c497982aad04e3bd57e9a25`，最终tail4 SHA `6e818f00428e10e1f0b92bea1b2e1df1d023f41282d2456df3d165e5b30d6853`。三系数分块的完整SHA另列；最终保存与此前只读失败快照的所有物理参数/网格逐值相同，三块解压payload逐字节相同，压缩文件SHA分别保留。

生产accepted loader应继续拒绝本CP。下一项仅按已有失败快照的原J方向判断何处触发域拒，再决定是否添加同定义的更紧正性充分余量；不改本次源或结果。
