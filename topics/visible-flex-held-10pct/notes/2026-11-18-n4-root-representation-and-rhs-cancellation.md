# n4：点根表示与 RHS 线性抵消的有限定位

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

可信度：**启发式/数值证据；包含对已保存 binary64 操作数的精确有理算术核对**。
接[两档固定系数读数](2026-11-18-n4-frozen-flow-mp60-mp90.md)，本条先读已有全部
192 个已接受 point-root 的 trace，再对 stage 43、38、175 的**首个相同输入 root**
各作一次原算法的新读数。没有新 flow、尾 Newton 或生产修改。

## 已保存与本次新观察的量分开

旧 trace 保存了 $L$、target、moments 和 stop 操作数，**没有保存 quad**。
不能把已舍入的 `moments-L` 冒充旧 quad。
新源 `capture_frozen_root_cancellation.mjs` 只对三处首个原输入执行原 point-root，
直接捕获其 quad、原 RHS 及各线性项操作数，并核对 $L$、target、moments、
err/scale/迭代数与旧 trace 全部逐字节相同。
三处原输入也与已有 MP90 的首 root 输入相同。
以下涉及 quad 的数字都是这次新捕获，不追记成旧运行观察。

## 不是整个非线性修正消失

在每个 stage 的 $64\times20$ 个非均值分量中，$L-\mathrm{target}$ 均非零。
全部这些相减以二进制有理数直接核对都是**精确减法**；最小非零修正仍约为
$1.00228\times10^8$ 个对应 target ULP。
因此不能把现象描述成“整个小修正被 target 吞掉”，也不能说这些减法本身产生误差。

另一个更细的现象确实存在：最终 `moments=fl(L+quad)` 再减 target，
可使本来非零的表示量残差显示为零。
三处新首 root 分别有 9、10、1 个分量满足这一条件。
对已捕获 $L$, target, quad 当作精确二进制有理数计算，最大的隐藏残差分别为

$$
1.4412794993123954\times10^{-20},\quad
3.2690177808095654\times10^{-20},\quad
1.0179006737090529\times10^{-22}.
$$

它们约为该 $L$ 的 $.266$、$.302$、$.060$ 个 ULP。
stage 43 首根的原报告相对残差为 $5.23165\times10^{-19}$，
而上述已表示 $L$/quad 的精确加和残差约 $4.74772\times10^{-17}$；
stage 38 分别为 $1.70078\times10^{-19}$ 和 $5.25117\times10^{-17}$。
两者都仍在原 $8\times10^{-14}$ 正常容差内。
这不是把新残差宣布为原 point-root 的真实方程误差界：quad 本身仍由原浮点求值。

## RHS 的抵消发生在哪里

从原 source 及已保存 state/$L$/冻结系数，逐式派生

$$
Q_j'=\sigma\{(m^2-4)Q_j+C L_j\},\qquad
\mathrm{linearFlux}_j=-mL_j+(m^2-1)p_j.
$$

以“两个已形成操作数绝对值之和/它们精确实数和的绝对值”计，
各 stage 的最大有限抵消比为：

| stage | $Q'$ 括号内两项 | linearFlux 两项 |
|---:|---:|---:|
| 43 | 42.8627 | 42.4365 |
| 38 | 17,644.7 | 49,742.7 |
| 175 | 22,152.9 | 1,509,650.9 |

这些最大比值处的二项相减也都是精确 binary64 减法。
因此再次补偿该最后一次加法没有依据；大的抵消比说明此前形成操作数的误差
可能被相对放大，不能据此把完整 flow 差唯一归因到这里。
尤其 stage 175 最大比值来自极小的 mode 68 项，不能只看比例忽略绝对尺度。

作为带量纲的局部诊断，一个 $L$-ULP 经原动量 RHS 的线性系数、一个原 RK 权重
和原归一尺度换算后，各 stage 的最大值约为
$1.12520\times10^{-10}$、$1.39580\times10^{-10}$、$1.77784\times10^{-10}$，
约为原尾门的 $.0563$、$.0698$、$.0889$。
这只含所显示的线性项，**不含 root/flux 的其他导数、其他 RK 项或后续传播**，
不是整个 stage 的误差界或完整 Jacobian 灵敏度。

## 有具体依据的下一等价表示

原根方程是 $L+q(L,Q)=t$。可把未知量写为独立修正
$\ell=L-t$，在同一真实算术模型中计算

$$\ell+q(t+\ell,Q)=0.$$

这样不需要以两个较大数 `moments-target` 表示小 root 残差。
原 point-root Newton 矩阵代码可沿用，变元对 $\ell$ 的导数为恒等；
原容差、最多迭代数、减半和域门仍应保留。
新的浮点 stop 操作数会变，但对应同一实数残差，不能要求两算法浮点判定逐位相同。

再将 RHS 中 $L=t+\ell$ 的线性部分和 $\ell$/nonlinearFlux 修正分开，
可以避免把修正先编码成完整 $L$ 再从线性项间取差。
固定本次 Number 系数时须保留**字面系数乘积**：三处新点的
`pref*targetFactor-sigma` 精确有理差分别约为
$1.18841\times10^{-19}$、$2.14755\times10^{-19}$ 和 $1.34602\times10^{-18}$；
不能套用未舍入物理公式把它当作浮点恒等式归零。

最小新 flow 方案应把“独立修正 root + 原 RHS”和“独立修正 root + 分离 RHS”
作为清楚的两个算术版本，仍只比较既定三个 stage，并以既有 MP90 流输出为参照。
只看对当前固定 target 的残差更小不足以选算法。
本条未执行任一改变后的 root 或 flow，也未计算新的全 flow Jacobian。

## 执行及来源

三处原 root 新读数句柄 71141 于 `2026-11-18 01:18:32 UTC` 真实 exit 0，
observer 约 2.006 秒；数据在 `n4_work/parts32-first-root-cancellation-v1/`。
`analyze_frozen_root_cancellation.py` 只读这些新记录与旧 trace，
其 Fraction 算术仅用于已保存浮点数的加减身份。

[`raw_primaryb016_lam002_m20_parts32_root_cancellation.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_parts32_root_cancellation.json)
保留源码、原输入、两档旧读数、新 quad/RHS 输出的哈希及具名标量。
所有全向量与 trace 留在 scratch。没有重新尝试旧初值，没有完整尾或前缀的新接受结论。
