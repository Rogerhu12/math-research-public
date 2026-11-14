# 原 cell8 的真实 low46 齐次继续传播

作者：exact_closure（GPT-6 Astra Pro，AI-assisted），2026-11-13。

本条严格接续已正式完成的 cell9 主包（SHA `c19d33f403f42c0b98ada4572aa58f860f17d922cd5e353d680d477d75640c07`），不重复 cell11/10/9 的 ODE。原背景的 cell8 九段、全部46频、真实 far-linear S0 列，以及原 node10 两个 Cauchy 基列的共同尺度全部继续保留。

## 同一对象与完整门

新的原 `OuterCell` 控制逐项核实：cell8 的 valley control 为零，没有 custom pulse/valley cap 或 warp weight；原完整 raw w 上界严格小于原 cap 阈值。这个身份仅用于原 cells8/7 的新生产者，不用于后续有真实 cap/valley 的 cells6..0。九段端口由原 R26 宽度与真实 node9 端口交核，不重新积分旧几何。

传播方程、24阶有符号 Taylor、92模共同导数余项、160位临界括区和 `2^-100` 余项门与前一条 cell9 证明完全相同。Arb256位、单线程。每个成功步额外保存任意部分时间的有符号 Peano 包，读出前核 F=√(r w³)>0 及全部有限值。

`lambda_m=prescribed_outer_Q/true_S0_Q(node10)` 与原 CL−LR、R141 u 的初K复半径均从已成 cell9 的准确保存字段消费；同 node10 height 给初P误差准确0。新 cell8 的基列仍是从 node10 连续传播的基列，没有在 node9 错误丢掉既有误差。初点 F0 从原保存包重新向外包住，端口分子只用合法上界。原复参数域仍是 R141 expanded profile，未扩大。

保存的逐模式双分量帽先在每一段、再在整个胞元取各自径向 supremum，最后才求 strong Fourier 和；次序与 cell9 相同。

## 实际结果

全部 219 门通过，正式退出0；wait4墙时 373.388977289 s，峰值 35296 KiB。九段全部完成，1312 个 Taylor 子步、4 个160位临界括区；1208 次原数学门要求的细分被保留统计。原完整原子 profiles 共 113 个压缩片，SHA、字节与顺序在主包；它们是可再生派生数据，按规矩11留 scratch。

整 cell8 的低46齐次 strong 帽（原σ=1/64）为

\[R_{8,\mathrm{hom}}\le 8.4109666389124428e-05<2^{-13}<1/128.\]

这是同真实 node10 Cauchy 数据的**齐次**贡献，未加 cell9 或 cell8 内生成的完整非线性源。因而该数字不能冒作这两胞元的完整场帽，也不能从 `Rhom<1/128` 直接宣称非线性自映。原完整均值、逆和所有非低频仍需在实际新段源预算中支付。

本次主包SHA `062a9ed72fc3a1841691bc8b7b785f8aaa75fb3694501a5ec38e6267e23cc332`，资源SHA `dd25c3ed4607e973401bd76df8a2f7046a7a476d64d3aede8ddc58a62c3b0329`，源SHA `d34c1e1a7c5933921d5aceeab159eab558b7198af8ee68eca86d4aca407bc0ab`。原输入、前一真实主包及资源全部在 config.additional_input_hashes 中绑定；复现命令完整保存在正式资源的 command 字段。任何重放必须换新输出前缀并保留256/24/160/100及96MiB门。
