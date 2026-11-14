# 同一显式对称 step02：根 Taylor 首相位稳定计算

2026-11-12；**高精度诊断，不是有向 beta 证书或全反馈逆。**

对象固定为 `type_fixed_step02_analytic_smoothing_inputs.npz`，SHA256
`bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532`。
按 R33 显式平均：半径和物理 beta 为偶函数，gamma 和储存 slope 的准确积分高度
为奇函数。这里没有额外 Gaussian 平滑；也没有把原始二进制 knots 默认为对称。
采用 R37 的同一个完整零阶项，负核心上
`ell = d_theta log(Fz/r) - d_theta log|F|`、`chi=1`。

## 方法与修复

新源 `scripts/fourfold_phase_beta_taylor.py` 把 binary64 标量输入按整数比准确读入
mpmath，在实际共同多项式 span 内直接做局部 de Boor 幂级数算术。先对指定有限
原函数的目标曲率求高精度根，再由 K 的 Taylor 系数准确形式除去 rho，构造
`kappa = sqrt(-K/rho)` 和 R50 的有界系数。完全没有从远离根的样本拟合后外推到零。

保留原始 `fourfold_phase_beta_probe.py` 不改。其平滑 bulk 评价在新源内仅把同一
有限 Fourier 多项式的均匀角网格求值换成零填充逆 FFT；系数、径向导数、Parseval
目标度量和积分单元完全相同。四个根内点与旧直接 Fourier 求和比较，原始 J 的差
不超过 `1.50e-8`；乘 rho^(5/2) 后与根 Taylor 的最大差约 `1.91e-11`，是普通浮点
一致性检查。第一次旧 bulk 求和过慢而被中止，根系数已经保存；下列两份是改进
后完整再现的报告，不以中止运行冒充完成。

## 两份独立完整报告

| 设置 | collar | degree 16 的 beta |
|---|---:|---:|
| mp60，quarter 256，角积 512，逐 cell Gauss16 | 1/2048 | 36.80161106729078 |
| 同上 | 1/4096 | 36.80161102236866 |
| mp80，quarter 512，角积 1024，逐 cell Gauss24 | 1/2048 | 36.80161113407938 |
| 同上 | 1/4096 | 36.80161104855984 |

报告分别在 `2026-11-12-beta-taylor-mp60-q256-a512.json` 和
`2026-11-12-beta-taylor-mp80-q512-a1024.json`，含每个 degree、两项积分、对象定义、
根 Newton 轨迹、源哈希和未付误差。四个末值的最大跨度约 `1.12e-7`，目前误差
明显在 binary64 bulk，而非根 Taylor 的高阶截断；这句话是诊断，不是上界证明。

两份 root Taylor 的前两普通 rho 系数为

```
g0 = -0.00642827750125572645682867163260736...
g1 = -1.37314483715196699847556783021168155...
```

16 阶 collar 积分约为 `530.2114097609404250` 和
`1305.4032590204483364`。degree12 到 degree16 的 beta 改变量分别约
`3.61e-13` 和 `1.29e-16`。R46/R50 的四重归一化已保留：当前 beta 是物理频率
`n=4j` 时 `1/j` 的系数；径向显式对称后 beta 恰为正半核有限部积分的 `1/2`。

再现命令（从课题目录运行）：

```sh
OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_taylor.py \
  --frozen-inputs data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --quarter-nodes 256 --angles 512 --dps 60 --degrees 6 8 10 12 16 \
  --collars 1/2048 1/4096 --gauss 16 \
  --out notes/2026-11-12-beta-taylor-mp60-q256-a512.json

OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_taylor.py \
  --frozen-inputs data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --quarter-nodes 512 --angles 1024 --dps 80 --degrees 8 12 16 \
  --collars 1/2048 1/4096 --gauss 24 \
  --out notes/2026-11-12-beta-taylor-mp80-q512-a1024.json
```

## 正在付的严格误差

数值代理另已付同一**无限**原函数的真根窄区间
`[.23836991573145,.23836991573148]`，见独立 tight-root JSON；这不自动把有限原函数
Taylor 系数转授给无限对象。新 `fourfold_phase_beta_interval.py` 使用 Arb/acb 原生
幂级数，正在逐项加入原函数尾/alias、角均值、径向解析余项和 bulk 积分误差。
当前 raw finite arithmetic 的球半径约给 collar `2.1e-6`/`4.6e-6`；只说明中心球
算术可用，还不是完整 beta 区间。选固定物理切点 b 并用 eta=t-b 的球积分，可避免
将根误差与发散 bulk 端点误差分别作不必要的大数估计。

仍须有向舍入、全部无限尾、Taylor 余项、角积分与径向积分的同时误差预算。
R46 的完整网络 frame、正帽/普通源、真实参数族、低频块、Newton 及固定握持的
有限幅精确闭族仍是不同输入，本笔记没有授予它们。
