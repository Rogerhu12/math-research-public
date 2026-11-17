# 新 wCut=.16 的 q=.015/M20：BVP接受，完整度量未过

维护：Astra-held10-7322d0de-20261118。此条为真实有限终态，不能领取完整等距或幅值达标结论。

从本新 cut 的 q=.01、.0125 两张已接受 M16 完整材料映射作
secant，目标 q=.015/M20，angular1280、maxnodes3600、tol3e-7
及 BC tol1e-8 不变。物理24模端口、eta=.1、lambda=0、精确
reference lift 和全部正性门均按先前定义；未用原 wCut=.08 场。

这轮实际耗时946.12秒，4轮后在867点被原 BVP 接受：

| 项目 | 终态 |
|---|---:|
| delta | .03016176956022264 |
| vd | .25023170207554724 |
| 最大 collocation RMS | 2.99871488794e-7 |
| scaled BC | 1.80675445751e-15 |
| 完整保存图 sampled metric FFT l1 | **1.20585716484e-5** |
| Cartesian Darboux tensor l1 | **.0232142730767** |
| flow defect | .000125410541041 |
| 采样最大主曲率 | 6.96699834367 |
| 采样最小 Frenet root 余量 | .00162295744376 |
| terminal height 最大系数 | 1.09762343242e-5 |

完整 metric 已高于1e-6，因此该行不作为合格近似。二阶缺陷及
root 余量的明显变化也不能被较小的 collocation 残差掩盖。
这不证明该物理 g 或该幅值不存在合格的更精细解。

原 domain Newton 记录了28次接受步、11次域拒绝、8次 merit
拒绝，最小步长 .0078125；没有 no_step。长时间没有首轮标准
摘要只是仍在 Newton 内部，先前始终只标“运行中”，最终并未
擅自取消或宣布失败。这里的终态也没有放宽任何门。

所有源、原参数、真实输出/系数块 hash 和 Jacobian 初值检查在
`scripts/resume_transfer/n4_w016_q015_execution.json`。
它由同目录 `record_w016_prefixes.py --names q015-m20` 提取。

已从本终态的完整 physical_profile 冻结 g，以 M20、tol1e-8、
maxnodes5000 继续真正的固定 g 精化。入口为
`run_observed_fixed.py`，只在已发表 fixed-g driver 外增加原
Newton 调用/异常/耗时计数的日志，不改参数、返回对象或接受
决策；完整命令和变换随运行记录。该精化返回前不计为成功。
新 cut 的圆化主线仍以 q=.0125 的完整 metric 通过态为入口。
