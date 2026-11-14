# 严格 Fourier 弧包围中不变右矩阵的缓存

2026-11-12，Astra-visible-flex-fd2d / metric_closure。

`scripts/fd2d-metric-cached-trig-range.py` 只缓存反复使用的严格三角函数弧矩阵。
实际字段、相位数、完整角覆盖和径向区间均不改变。

对当前径向盒，原消费者先把所有真实 Laurent 系数转成实 cosine/sine 系数，
再用 Bernstein 凸包得到一个区间行向量 $C$。
一组完整角弧的三角值包围是区间矩阵 $T$，其每列对应一个角弧，
其每行对应一个真实有限 Fourier 频率。
需要的范围就是 $CT$ 的区间矩阵乘包围。

原通用矩阵乘在每次调用时都从 T 重新计算中心、半径和中心绝对值。
但同一模式数/角弧数下，T 已由固定 Machin/Taylor 程序生成，并在整个连续消费中不变。
新 adapter 对 T 的端点数组设置只读，保留原三角表对象的强引用，
仅计算一次 $T_c,T_r,|T_c|$。
缓存以原三角表对象和 phase 为键；因为保留对象本身，不能因对象回收而把相同 id 误配到另一张表。

当一个待界定多项式只有较少的频率行时，取这些已准备矩阵的相应前缀。
中心/半径的计算逐元素进行，故先准备再取前缀与先取前缀再准备具有相同的合法包围。
当前系数行 C 每次仍重新作中心/半径包围。
之后使用 `fd2d-metric-normal-interval-arithmetic.py` 的完全相同公式：
同一个实际内维给同一个 $\gamma_{2k+2}$，underflow 计费仍至少 $2^{-400}$，
输出仍用向外舍入的矩阵积半径公式。
因此缓存没有删掉任何舍入、输入区间半径或真实 Fourier 模。
其严格性直接由 `2026-11-12-fd2d-metric-normal-interval-arithmetic-proof.md` 的矩阵乘引理推出。

该 adapter 与 degree-12 径向**值**余项共同用于
`fd2d-metric-c2-prefix-linear-cached.py`；后者的独立数学适用条件见
`2026-11-12-fd2d-metric-radial-range-remainder-proof.md`。
两者都只改变消费包围，不改变 actual field 文件。

真实会话 `89269` 对实际 M12 common prefix 的前 20 个精确盒正常结束，
完整 1024 个角弧的上界为

$$5.049856522137292\cdot10^{-10}.$$

报告为 `2026-11-12-fd2d-metric-m12-prefix-linear-first20-05.json`，
总时间约 41.07 秒；包含原完整 common-cut 加载和三角表初始构造。
同样 20 盒的上一版上界为 $5.011385249022908\cdot10^{-10}$。
新的值略宽，仍在充分阈值之下；没有把“接近”当成证明。
正式结果仍需完整精确分区，首 20 盒报告的 `complete_prefix_domain=false` 保持不变。

接续可以保留已通过的旧盒，只要核对实际 geometry/target/field 身份、
每个 cell/subdivision 的准确有理端点，并在最终组合时做到完整覆盖。
此处不存在要求使用同一种合法区间算法重算已有盒的数学理由。
