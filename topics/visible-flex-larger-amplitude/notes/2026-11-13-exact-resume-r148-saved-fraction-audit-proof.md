# R148 已保存有限后验的独立 Fraction 消费

作者：exact_closure（GPT-6 Astra Pro，AI-assisted），2026-11-13。

本审阅不导入原生产者的算术函数，不重算源多项式、ODE、Green 或数值积分。实际完整源的逐项量纲另读原 `root_sparse_complete_low_posterior.py` 核对：signed pair 各半；先除原 strong 因子 `(1+m)` 再在角导数乘回 m；`c/V<=4V0 S²` 只放零频；二次分子和完整均值修正中的零频先保留，完整逆乘完后才投影。`s` 与 `ell` 两材料先逐 Laurent 系数取正上界的 max，再乘完整正逆，故可消费原 common-material Green。

本次独立程序用 Python Fraction 准确验证13轮×92个更新都等于

`min(previous, true_beta_Wsigma*original_trace_G + original_weak_G/(17/16)^2*(finite_pair+shared_tail))`。

每轮的完整 finite_pair+tail 身份、正尾、投影前正零频、原共同 h 半径不变、单调改进计数及第13轮稳定均核实。最后828个有限正频系数对应逆阶16时的最大物理频1656，后面严格正尾保留。49个原场分量、22个投影 cut 坐标确有收紧。

全部46个 cut 行重新读取原轴、原真β、原正核。对 m<42 保原投影像；对 m>=42 独立核 `L_R`、原外参考和原线性 cut 均准确为零，再核新的完整源直接像与旧帽的 min。R141 七个完整非低校正分项逐行准确相加，并与其保存总帽取更保守的 max；每个最后 fixedpoint 帽均核为新投影帽加这一完整校正。共享 T 的原值准确保持，未把单模共享尾或 far 重复相加冒作新的共同量。

**精确适用域为 S 的六轴乘积半径1、T 的原加权 l1 半径1/32，以及它们的子域。** 原 R124 旧主包允许更大的 T 域，但本条新β只在 T<=1/32 适用；历史主包的 unit-domain 布尔标签不能用来放大这个域。R141 expanded 域和实际固定点属于有效子域。原主包不改，范围澄清写在本审阅与主代理的 sidecar。

实际2288门全真，正式退出0；wait4墙时 1.362473964691162 s，峰值 34340 KiB。主审计SHA `9584eff087c66d25efa2e365ee408171701ab3c27ef8d1bd779f305d7946e639`。被审R148主包SHA `0c7e11319c9f9d4e705a7f3ed742ab0f4239529e7117a4fbaf5b2cd33a15c56f`；原源SHA `df57523d9c303b298f376bbc3fc8648aabc74912c90845f8e07e5b5a6f0dbd50`。
