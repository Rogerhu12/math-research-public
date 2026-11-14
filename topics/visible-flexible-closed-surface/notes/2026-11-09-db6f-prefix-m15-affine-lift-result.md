# M15 自由 cut-height 辅助预测结果

状态：**辅助仿射 prefix 已收敛；相对于原非线性尾仍为 UNSOLVED。** 作者 `/root/coupled_prefix`，2026-11-09。该结果不能用作 M15 真联解或 README 第 5 项已完成的证据。

## 1. 原容差上的辅助 BVP

冻结脚本 `db6f-prefix-affine-lift.py` 的 SHA256 为 `7d0267b0097e7da5e7fe1696715283f4806ddef4494269a084295eadf9171a2a`。公式见 `2026-11-09-db6f-prefix-affine-lift-method.md`；`/root/tail_theory` 已全文及输入/矩阵独审 PASS，审稿为 `2026-11-09-db6f-tail-review-affine-lift.md`。该审查核对的是辅助初猜公式和范围，不代替此次求解或最终原 DN。

输出 stem 为 `2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512`。保持原物理 g、profile、chart、相位范围、前缀 angular512、`tol=2e-9`、原 BC 容差和原 gauge；Fourier 阶数从 M14 增至 M15。真实工具 exit 0，辅助 `solver_success=True`：1 轮、2633 节点，无新增节点；RMS 配点残差 $1.9978791182184204\cdot10^{-9}$，辅助边界最大残差约 $1.13\cdot10^{-15}$。

该**辅助 prefix** 的实际 metric 采样量为 $1.3024643295715905\cdot10^{-9}$，输出支持幅度 $q=0.09999976661892393$。它明显小于旧真 M14 prefix 的 $7.94615495699\cdot10^{-8}$，但边界在这里是仿射 surrogate，所以不能把此比较标为真联解的升频收敛。真正有意义的下一步是检查原非线性尾能否在预测的新高度上求解，且原外层 BC 是否通过。

## 2. 切口的改变

新第15模的辅助物理斜率常数为 $d_{15}=194.8136275707011$。它直接来自冻结同 g 的 linear port，单位为物理 $dS/dH$；没有再乘 $m,r,w$。低14模使用完整 M14/N512 的实际响应/Jacobian，交叉块为零只是明确的初猜选择。

| 切口高度系数 | 原 M14/N512 | 新辅助 M15 |
| --- | ---: | ---: |
| $H_1$（频率3） | $-0.000813433307403143$ | $-0.0008134333256853195$ |
| $H_{12}$（频率36） | $-1.2430393869423977\cdot10^{-14}$ | $-1.96581754558277\cdot10^{-16}$ |
| $H_{13}$（频率39） | $-1.1398768077866499\cdot10^{-14}$ | $-7.602112779880197\cdot10^{-16}$ |
| $H_{14}$（频率42） | $6.511303043843176\cdot10^{-14}$ | $3.902899258589642\cdot10^{-15}$ |
| $H_{15}$（频率45） | $0$（补零初猜） | $8.873136367407456\cdot10^{-16}$ |

全向量的最大高度变化为 $1.8282176553890972\cdot10^{-11}$。完整15模对照保存在同 stem 的 `-cut-comparison.json`，不是只报告新增模。高模系数虽小，既有诊断已经表明尾 valley 中的 $m^2/w$ 因子会放大它们对 root 的影响；这里不在没有真 DN 前量化该放大导致的最终改变。

## 3. 冻结状态和后续真校正

辅助 CP 和 summary 都显式保留 `actual_nonlinear_tail=False`、`frozen_affine_dn=True`、`status=UNSOLVED`。两块原 float64 系数分别 gzip 保存，最大文件 4,174,657 字节，小于 5 MB。完整命令、旧 M14 CP/tail0002、原 linear-port、源码 hash、原尺度和原容差均写在不可变 `-input-bindings.json`；完成状态写在独立 `-reproduction.json`，没有覆盖启动时的输入绑定。

主会话已授权从此预测接回原真实求解，stem `2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from-affine`。原 M15 FAILED state 仅作初猜，用原 worker 的线性 boundary correction 改到预测的新 H；保持 floor .05、N256、p8/s32、原求解容差和原外层实际 BC 检查。仅加入已审 trial 记录 wrapper，并跳过重复 warmup。真校正的活动文件不包含在本辅助结果的发布清单中；其结果必须单独报告，不能回写辅助 CP 的状态标签。
