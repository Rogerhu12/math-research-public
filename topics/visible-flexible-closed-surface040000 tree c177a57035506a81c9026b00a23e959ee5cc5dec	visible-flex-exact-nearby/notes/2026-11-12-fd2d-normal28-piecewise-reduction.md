# 28 的完整 normal：逐存储块可恢复规约

本记录绑定 27 的真实接受态 `2b65810c…52ae6f`、原 131 个物理径向节点、中央 31 维 / 尾 16 维 / 轮廓 7 维、gap 0.9 和 R165 完整 coast 求积。51 个实际 normal 片全部自然退出 0。它们不含新的场或新的有限方程。

## 实际恢复过程

两次完整合并、一次四片累计合并和几次短累计合并收到真实 SIGKILL；没有证据确定原因，不能据此称数学失败。累计第 10 片曾被完整保存。另一次纯数组规约在第 14 个输出块明确遇到磁盘 ENOSPC，实际退出 1；这与此前的 −9 分开记录。已闭的 14 个块直接恢复，没有重新算 F 或 J。

另名 `fd2d-gc-piecewise-normal-reduce.py` 只用标准库和 NumPy。对每个不足 1 MB 的原 NPZ 存储块，逐一检查全部输入 manifest、原来源、目标、完整映射身份、实际 row ledger、文件与数组 SHA，再按原 tile ordinal 从零相加。一个数值条目的加法次序保持不变；不同数组之间的调度改变不造成条目之间的数据依赖。映射数组核同后原样保存，不参加相加。每个输出块立即闭存，空间只需要输入小块、累计小块和小型元数据。

完整结果使用明示的新 `fd2d-offline-piecewise-ordered-normal-v1` 格式，明确记录真实 reducer 和 consumer SHA，不假称调用原保存器。`fd2d_gc_piecewise_normal_transport.py` 在数值消费时重新构造原 `LocalNormalSystem`，逐项核实际消元映射、全部节点/相邻块/参数列形状与 SHA，再返回原 class。缩放、阻尼、Schur 和 QP 都在完整未缩放 sum 之后进行。

## 真完成的范围

35 个小块均已实际自然退出 0，峰值不超过 29,064 KiB。最终 controller `50351 / 79771b` 真退出 0，完整 normal manifest 为 `bb50e4ccc1ba7f98f36303631592738815249785ecc9f45a202d465199be4c31`。全部 row ledger 恰好覆盖 51 片；合并残差平方与此前完整实际 F 的保存值相差 `2.1316282072803006e-14`。

这只是同一实际状态和有限目标的完整 normal 恢复。它不是新的接受态，不是 finite convergence，也不是强目标的连续几何证书。其后 gap 0.8 分支若启用，必须单独改唯一 gap 行、重新缩放/Schur/QP并计算真实 F。
