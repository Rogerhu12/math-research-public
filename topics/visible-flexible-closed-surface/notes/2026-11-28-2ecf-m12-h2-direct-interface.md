# M12 完整 Gram 的 H2 增量直接 LM 接口

2026-11-28，Astra-visible-flex-2ecfcd69 / m12_solver。**可信度：已执行有限线性接口检验；新全半体数值步尚待实际运行。**

## 为什么改变求解方式

前次真实的 M48 完整 H 两个 run 虽使独立采样 metric 峰下降到约 $7.7\times10^{-10}$，但 R236 连续界和 R226 reach 传递同时变差：h487 的连续 metric 界 $5.50069\times10^{-5}$、reach$/D$ 下界 $0.00963478$；h509 分别为 $5.40371\times10^{-5}$、$0.00962138$。见原 notes 中 run 45851669566 和 45857469750 的完整摘要。当前只保留 H1-M48（run 45847254548）为已通过旧连续几何验证的暖续，而不把两个坏界冒作合格。

原 $g$、源、中央及真平 cuff 的两阶迹、全部三项 Gram 残差和全部角列保持。新方向解

$$
(J^TJ+\lambda S_2)d=-J^Tr,\qquad\lambda>0.
$$

$S_2$ 是固定材料图上增量的离散正定二次型

$$
\int\bigl(|d_{ss}|^2+2|d_{s\theta}|^2+|d_{\theta\theta}|^2+|d_s|^2+|d_\theta|^2+0.01|d|^2\bigr)\,ds\,\frac{d\theta}{2\pi}.
$$

这里只惩罚一次步长 $d$，非线性目标仍为原始 Gram 能量；它没有把当前场正则化后定义成新度量。内置旧完整 Gram 装配保留所有跨角耦合；直接带状 Cholesky 和用真正物理 $J,J^T$ 计算的迭代精化取代限额 LSMR。每步仍按原非线性能量下降和完整训练峰不超过原峰的1.001倍接受；另有二阶增量筛选，不把该浮点筛选称为严格 reach 证书。新场必须再消费 R226/R236。

$S_2$ 的角向积分可以精确分离：planar 复列范数为 1，非零 height cosine 列范数为 $1/2$，零 height 列范数为 1。第 $k$ 个通道为

$$
\nu_k\{B_2^TWB_2+(2k^2+1)B_1^TWB_1+(k^4+k^2+0.01)B_0^TWB_0\}.
$$

全部实际 Gauss 权正，带宽仍为五个径向邻块。只要 $B_0$ 在这些结点列满秩，该式因 $0.01 B_0^TWB_0$ 而严格正定，故上述有限 LM 方向唯一；这不声称原无正则无限维线性化有统一逆。

## 实际有限检验

新 fixture 使用真实生产 B-spline/Fourier 基、非零 77 列、2304 完整物理行，并用直接 Cartesian 二阶导数行独立构造 $R$，比较 $S_2$ 与 $R^TR$。全部真实 exit 0。

- `H2_band_relative_error`: `1.0993746427934572e-15`。
- `H2_operator_relative_error`: `1.3696756197703997e-15`。
- `actual_regularized_normal_relative_error`: `1.4792879111254213e-15`。
- `dense_to_banded_physical_direction_relative_error`: `1.5967597142956131e-14`。
- `minimum_H2_eigenvalue`: `9.6809197845908415`。
- `nonzero_off_channel_Gram_fraction`: `0.82701630007933946`。

运行命令：

```bash
OPENBLAS_NUM_THREADS=3 OMP_NUM_THREADS=3 MKL_NUM_THREADS=3 python 2ecf-m12-h2-direct-lm-fixture.py --scripts <topic>/scripts --out <scratch>/h2-direct-fixture.json
```

实际参数与源码身份：

- `2ecf-m12-h2-direct-lm.py` SHA-256 `a7e5229793ceb4753b74f8063a8abc3b7d99280a16e69cab9a7e0c844b794117`。
- `2ecf-m12-h2-direct-lm-fixture.py` SHA-256 `90ad91125f2228d4a53b7e0be31ad137cb28a1223e32b3340cb8a55b6733dec7`。
- `h2-direct-fixture-v2.json` SHA-256 `2ea85852891080fc586200a36891a63f824e5ae44e5dae49ff6fc15e594bbd47`。

报告正文和数组只留 scratch，不入库。本检查不是研究场、更不是第 5 条完成。实际 h487 原输入重生已启动，随后将按同一 $g$ 执行此新直接步并保留全域连续预算；若停滞必须真实扩大空间，不能更改原参数冒充加密。
