# 完整均值校正到相位方向 Z 的实际 L2 预算

## 1. 公开实际结果

公开 Actions run `43589465579` 已真实成功。它只消费此前已完成的主体
7721 格和两条完整标量 mean-error 流，不重算任何原主体格。新的 v2
数学消费者实际退出码为 0，10 个门全部通过；数学计时 2.022430132 秒，
外层实际子进程记录 5.000534868 秒。

在原完整物理反射 L2 Gram（mean 权重 1，所有非零 sine/cosine 权重 1/2）
及全径向 `[0,25/8]` 上，它严格给出

\[
 \boxed{\ \|q_\star-Z\|_{L^2_rL^2_\phi}
       <4.572198020300\,10^{-6}.\ }
\]

这里 `q_star` 是原完整有限响应 trial 加上独立真实标量 mean 校正。
它不是未知的真实完整 PDE 参数响应。由这项已付费用，留给真实响应的
准确充分预算为

\[
 \|q_\nu-q_\star\|_{L^2_rL^2_\phi}
 \le 0.004995427801979700
 \quad\Longrightarrow\quad
 \|q_\nu-Z\|_{L^2_rL^2_\phi}<1/200.
\]

左边仍须由真正完整 Green 逆、正确背景算子、全 regular 边界及高频
连接证明。相位线的已证响应误差门随后才能使用；本结论没有提前授予它。

## 2. 三个保留区别的方向

原完整 finite trial `q_raw` 的 index SHA256 为
`ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6`。
它有完整 193 个物理状态，原均值未从求解中删除。完整标量消费者构造

\[
 q_\star=q_{\rm raw}+e_z e_2,
 \qquad \psi_\star=\psi_{\rm raw}+e_\mu e_2.
\]

两条校正消除了各自的准确 mean 残差并保留独立真实 mean 边界条件。
所有原非均值 PPoly 跳仍留在主体合同中，不因 mean 完成而消失。

相位方向 Z 则是同一原 full trial 的逐段 exact 连续值修补，其 definition
SHA256 为
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`。
Z 与 `q_raw`、`q_star` 都不同，尤其右端完整物理方向偏移及独立 mean
偏移必须保留。新 native 将原右端全部偏移原样记录。

## 3. 完整有向积分与实际数值

每格原 `entire` 均值区间先按原成功 native 的同 index、同精确区间
逐行核对，再与原 residual-row 的 mean 区间核对。原 source 将前者
重新构造并再次记录为后者；v2 正确要求后者包含前者，并使用它们的 union
计算费用。全部 7721 格按准确有理数恰覆盖 `[0,25/8]`，没有遗漏或重复。

若 `E_z,j` 是这一完整均值绝对界，则

\[
 \|q_\star-q_{\rm raw}\|_{L^2_rL^2_\phi}
 \le\left(\sum_j(r_j-l_j)E_{z,j}^2\right)^{1/2},
\]

伴随使用同样公式。下表是向外舍入后的易读界；原 native 保存完整有向值。

| 完整已付量 | 严格上界 |
| --- | ---: |
| 全响应 mean 校正的 L2 范数 | `4.572198019895e-6` |
| 全响应 mean 校正的径向一致绝对值 | `1.216751281227e-5` |
| 全伴随 mean 校正的 L2 范数 | `1.900374572191e-5` |
| 全伴随 mean 校正的径向一致绝对值 | `2.508759702009e-5` |
| `[0,9/10]` 响应 mean 校正 L2 | `4.571217391206e-6` |
| `[9/10,25/8]` 响应 mean 校正 L2 | `9.469052467760e-8` |
| `[0,9/10]` 伴随 mean 校正 L2 | `1.845113358611e-5` |
| `[9/10,25/8]` 伴随 mean 校正 L2 | `4.549507759147e-6` |
| 原 full trial 到 Z 的完整 L2 差 | `4.051522658681e-16` |
| 完成 mean 的响应 trial 到 Z 的完整 L2 差 | `4.572198020300e-6` |

最后两行还消费了原方向 native 已证的完整 A_(1/64) 角零阶 pair 范数，
该范数支配物理 L2。乘上准确区间长度平方根 `sqrt(25/8)`，得到原
full trial 到 Z 的全体积费用，再用三角不等式加入真正 mean 校正费用。

完整 response/adjoint 残差范数在本次还由全部原行重新累加核对，分别
小于 `0.001284069679776154` 与 `0.000182077135241679`。
这些是残差，不是响应误差。完整 signed dual 残差积分仍包含零，
因此它不能单独给出非零 Schur 或消去任何剩余响应逆门。

## 4. 原始证书、失败保留与范围

| 输入或输出 | SHA256 |
| --- | --- |
| 原完整主体和两条 mean-error 流 | `a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870` |
| 原完整显式连续方向 native | `87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88` |
| 本次独立 v2 消费 source | `ec04c5ed1aac332845c29c060d5a756d152089c0f41b268a103d2f31f2ccc033` |
| 本次实际成功完整 native | `bd69c985ddaad53152867538980cb59ca28f4c6d27e27b30a6f9dd7137baad99` |

公开原记录位于
`notes/body_mean_norm_ci/run-43589465579-1-complete-mean-norm-and-phase-direction/`，
包括实际 `process.json`、完整 `native/complete-body-mean-norm-and-phase-direction-native.json.gz`
和 `evidence/complete-mean-norm-summary.json`。

原 v1 run `43588192611` 因区间包含方向写反而失败；其前五个实际门、
失败 native 和 source 均保留。v2 使用单独 source，并未修改或替换原
主体科学结果。详见 `notes/2026-11-14-R133-body-mean-norm-v2-reenclosure.md`。

本次相位接线仅使用仿射参数偏移 eta=0（即固定物理η0）；原主体证书的全 `1/1000000000` 参数半宽
没有转授成相位比较的另一背景。原 ac1 算子与其独立连续修补背景的变化、
所有高输入反馈、完整源和接口、真实 full response 以及非线性背景变化
仍须在对应方程中支付。当前结论只将已完成 mean 校正准确接入已完成 Z。
