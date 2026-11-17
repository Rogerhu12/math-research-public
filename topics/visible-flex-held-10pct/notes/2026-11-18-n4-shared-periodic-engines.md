# n4 实际尾完整状态上的同 μ 引擎共享等值检查

维护日期：2026-11-18（UTC+8）。本条将已登记的最小共享引擎改动
独立用于 n4 的 periodic 求积源；不以 m3 的有限态对照代替 n4 检查。
证据见 [shared_periodic_n4_m20.json](../scripts/resume_n4_tail/shared_periodic_n4_m20.json)，
采集程序见 [record_shared_n4_comparison.py](../scripts/resume_n4_tail/record_shared_n4_comparison.py)。

## 改动范围

从当前 `transfer_work/periodic-source` 另建独立副本，使用
[install_shared_tail_engines.py](../scripts/resume_m3/install_shared_tail_engines.py)
仅将一次 DN 内相同物理 $\mu$ 的引擎缓存，以及 split 替换时的重复对象
集合处理移植过去。缓存不跨越 DN，不跨越模式数、求积数或物理设计；
原 periodic imports、`sparseGlobalSolve`、其组装、求积式、ODE、根守卫、
缩放残差和所有接受门保持不变。客户端另外记录标准错误与退出码。

## 独立 n4 完整态结果

使用已接受的实际 M20 尾第 4 次响应，哈希
`295220ca244328b5daae7d2ebfc804e630c08e1339b1c30170c89f5d2751362b`。
参数为 spacing 4、$N=512$、shootingParts 8，全部 576 个 stage。
由 [compare_shared_tail_state.mjs](../scripts/resume_m3/compare_shared_tail_state.mjs)
在同一完整有限状态上重放原实际残差与完整 Jacobian。

| 检查 | 结果 |
|---|---:|
| 比较标量条目数 | 990,760 |
| 残差、flow、flow Jacobian 最大差 | 全部 0 |
| deep graph、gains、全部 graphs 最大差 | 全部 0 |
| 原残差范数 | $1.6649396764925328\times10^{-9}$ |
| 共享源残差范数 | $1.6649396764925328\times10^{-9}$ |
| 原引擎实例数 | 576 |
| 共享引擎实例数 | 8 |
| 跨同引擎 stage 的返回数组变异 | 0 |
| 重入后导数、Jacobian、根量差 | 全部 0 |

所有比较量按 Float64 字节累计得到同一个哈希：
`dada87a4f42e40408177c0f64405f215d8222ae5771d57c07a3630b74050245c`。
这直接检查了共享 scratch 数组造成别名变异的风险，而不只比较最终范数。

## 源身份与可复现命令

安装器哈希为
`578c8397f38acb63891095cdefa2490ea70182d538ab00937192eafeb4cddb66`；
本次完整态对照程序哈希为
`503c7dd581163e141cb2f96918a2ae8629df44fdd8eabc6292a3af29816bd1dd`。
独立副本三个改动文件的哈希是：

- core：`84f944c560dcb65dc3f6fda2e97f3ebc549f1dbcdcc1fe2525324561d754c3be`；
- split：`e93b9e946e8b9b5916bfefc8bc64b44094eb5c62a6eff1eab73f2381d6c2d55a`；
- client：`d25e1b388ae1ab1bb46d720ebe250fd4be5a0653f4dca64619dcdc79a5240e1b`。

完整安装来源、改前哈希、物理与离散参数、对照命令及输出哈希都在标量记录中。
原、共享两次完整评估分别用时约 34.14 与 30.76 秒；两套实例在此测试中
同时存在，因此此时间或 RSS 不能用作普遍提速或节省内存的证据。

本条没有新求解一次尾，也不声称所有状态都已作逐位测试。
它允许后续在独立副本中尝试原方程的实际求解；后续结果仍必须逐次通过原门。
