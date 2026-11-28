# 原 R53 同输入积分缓存：真实 M32 块核对后用于后继

这是消除重复计算的执行改进，不是新的 λ 前沿、完整 Jacobian 求解证明或闭合曲面结论。
真实标量、输入绑定和源码哈希见
`2026-11-28-design-core-cache-m32-block.json`。

## 同一输入与可变数组

原 `MaterialFlattenedSupportCore.evaluate(theta)` 即使对象及 theta 未变，
仍重做位置积分；它写出的 `_cache_theta/_cache_jets` 原本只供参数导数读取。
原 Jacobian 的 δ 中心差分反复构造 Flow，使各 Flow 的 lift 缓存失效，
从而在不同径向块再次计算同一个 core 的同一个角网格。

新 `material_core_evaluate_cache.py` 逐字节绑定 theta，并以 SHA-256 绑定
core 的全部实例数据，递归包括原支撑核、参数、派生积分表、节点和求积权重。
仅排除原函数不读取、会覆盖的两个输出缓存，以及本 memo 自身；未知数据类型旁路
到原函数。函数/provider 身份和原 evaluator 源码另有记录。每 core 最多保留两项，
条目总字节数有 128 MiB 上限；逐条淘汰只影响性能。

保存的结果和 jets 都是私有只读副本。命中时返回新的可写数组，并恢复独立的
`_cache_theta/_cache_jets` 副本。因此下游对返回值或原输出缓存的原地写入不会污染
后一次求值。没有改变求积、几何、未知量、域条件或门槛。

## 本次实际核对范围

输入是原 `.004/M32` 求解记录所绑定的完整升模初猜；其哈希与该 run 的
`inputs` 一致。选取其 879 个真实节点中跨全径向分布的 32 个节点，保留全部
97 个状态分量及 32 个参数列，按原 block16 调用。并未组装全局 collocation
矩阵，也未执行 BVP 步。

原 evaluator、memo 冷启动及热启动所得 RHS、全部 `dy` 和 `dp` 数组逐位相等。
原 6.664 s，冷启动 3.937 s，热启动 1.357 s；这些是当前并发环境的实际计时，
不是固定加速比保证。峰 RSS 为 376012 KiB，13 次命中、2 次未命中、0 次旁路。
另外对返回的 F、原 jets 和 theta 做隔离写入后再次求值，全部恢复原值，
返回数组仍可写。

独立 `prefix_resource_driver_v4.py` 通过原 portable loader 安装该 memo。
它继承已核的 Fourier CSR 缓存与径向批处理，并兼容完整 BlockQR 入口。
实际 `BlockQR → v4 → 原 portable` probe 读取已接受 M32 final raw（原求解已
由 879 点加密到 944 点），在全部 944 节点通过初域检查；
probe 没有调用 BVP 或 QR 因子，也不是接受场。

## 使用交接

正在运行的原 `.004/.008/.016` bootstrap 未改。只停止了尚未求解的旧 QR 等待进程
（实际退出码 130），随后更新尚未执行过 BVP 的 dispatcher，并在新输出树重新等待。
新的后继将从真实 `.016` 与较早的真实接受场继续，所有新阶段使用 v4，
M≥40 另用完整 BlockQR。缓存命中不是接受条件：每个新场仍须实际通过原求解、RMS、
物理 BC 与完整 metric 审计；完整 tail、闭合、共同二阶喷流、reach 和保持幅度均未由此支付。
