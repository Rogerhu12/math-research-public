# 同节点长精度 Fourier 变换：实际有限测量

会话：Astra-visible-flex-78718bd0；作者：`/root/numerical_recovery`；2026-11-10。

## 范围和真实执行

`78718-prefix-long-fourier-transforms.py` 只替换已识别的完整圆柱 Cartesian `B/B1/B2` 合成与投影；未知表、复制表或局部基使用原方法。原离散节点、物理方程、`er/et` 二进值、投影归一分母不变。实虚部分开 FFT，保留极小 complex-step 的虚部方向，不让实部舍入泄漏覆盖它。

`78718-prefix-long-fourier-research.py` 在已存、仍为 UNSOLVED 的 M15 warm 上取 32 径向点，比较 M15/N512 与补零的 M22/N1024。每项计时取 5 次中位数；不运行 BVP、DN、积分或新候选。实际 `3b97b5`/session 34280 启动，`0ea332` 自然 exit 0。报告 `2026-11-10-78718-numerical-prefix-long-fourier-benchmark-01.json` 为 8,391 B，SHA `ccdc1a2a2ca63eb88d50ee593c7b3fc7ef0acc8cbac2570f783fdd6263bc6db0`；真实回执与命令另存 `2026-11-10-78718-numerical-inner-snapshot-and-fft-observed.json`。

## 测量结果

| 项目 | M15 / N512 | M22 / N1024 |
|---|---:|---:|
| 原 RHS 中位秒 | 0.05361185 | 0.13303373 |
| 新 RHS 中位秒 | 0.01454101 | 0.02711745 |
| RHS 加速比 | 3.68694 | 4.90584 |
| 原 velocity_s 中位秒 | 0.09526571 | 0.17329667 |
| 新 velocity_s 中位秒 | 0.02923939 | 0.05410310 |
| velocity_s 加速比 | 3.25813 | 3.20308 |
| RHS 最大绝对差 | 1.05068e−14 | 9.85553e−15 |
| RHS 相对 L2 差 | 1.65126e−14 | 1.75183e−14 |
| 1e−25 complex-step 方向相对 L2 差 | 1.80591e−15 | 2.36884e−15 |
| 原速度最大绝对差 | 6.82072e−16 | 6.82072e−16 |
| velocity_s 最大绝对差 | 3.17138e−15 | 3.17133e−15 |

表的舍入只用于诊断显示，非严格有向区间。一次表构造约 0.00030 / 0.00050 秒。B/B1/B2 的最大合成差约 3.73e−15 / 1.14e−14 / 5.38e−14。B1 投影原结果因奇偶抵消接近零，所以它的相对差约 1；其绝对差仅约 2e−17，不能将这个相对指标与完整 RHS 相对误差混淆。未知复制基的原 fallback 实际逐项相等。

## 精度与恒等式范围

当前机器 `longdouble` 的 `nmant=63`，含首位共 64 有效二进位；其存储是 128 位，不是 113 位尾数的 IEEE 四倍精度。实际 scipy.fft 保留 `float128/complex256` 容器。逆变换使用 `norm='forward'`，因此直接输入 Fourier 系数；投影用未归一 rfft 的实部/负虚部，再除原保存基范数。

R90 给出完整有限 DFT 数学恒等式、B1/B2 符号、原三角表与理想单位根的差异，以及正根域内的敏感性式。这里的原/新差异是实际有限测试，不是全域舍入误差认证，更不是新图满足 2e−9 的证明。R88 的六 JVP Fourier Jacobian 与本模块分别改 `adapt_fun_jac` 和新 Flow 的 `values/project`；安装顺序保留同一 frame 与全部原 B 表，没有互相覆盖入口。

## 真实运行选择

通用 `78718-run-prefix-mode.py` 已接显式 `--transforms fourier|original`，默认 original。可与 `--jacobian fourier` 及 `--tail-jacobian fourier` 分别选择，实际源与 worker 的返回标签记录在 mode-run。当前旧 M15 主程序没有被改动；后续结果仍以自己的实际收敛、完整真尾和连续全图计算为准。
