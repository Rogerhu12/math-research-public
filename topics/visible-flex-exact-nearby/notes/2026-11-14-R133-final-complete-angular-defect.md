# R133：原中心全径向、全角圆周的实际角向几何缺陷

2026-11-14，visible-exact-astra-ac0d。

**实际计算已完成。** [完整角缺陷定理](../results/R133-supplement-complete-angular-model-geometry-from-moving-residual.md)的消费者现已在原 `ac1d5b98…` 中心上运行完毕，耗时 17.043567 秒，覆盖 7,722 个共同闭区间及全部 6,143 个原接口。原生报告没有失败；[四片无损索引](2026-11-14-R133-final-complete-angular-defect-parts.json)保存原报告的全部 6,871,825 字节，其 SHA256 为

```
7a3dd2c1d48b611f5d9a6bd8c2d7ebeeeb4c2f6a7c2bcc4f61f4d012be4e2f90
```

[消费者源码](../scripts/fourfold_codazzi_moving_geometry_angular_defect.py)的 SHA256 是 `2450201aec8f44477b71b3809d81bf99798c363dc0401c2391883ad332d2ab2b`。

## 1. 同对象输入和实际运算

输入是已经完成的 7,296 行原 moving 残差、完整 strict 负侧证书和完整 positive 证书。消费者检查原中心、实际 $\alpha,\nu$、目标对象及两份系数报告的完整字节身份。唯一不在前两份系数覆盖中的 root 小区间按其真实 candidate cubic 和真实 scalar germ 新算，保留全部 65 个实系数。没有重新运行原 primitive 残差，也没有以数值网格插值代替系数覆盖。

共同范围为 $0\le r\le25/8$、全实角圆周，以及实际原仿射中心 $\eta=\eta_0=-7789843107295549/4611686018427387904$。规范化残差乘了原精确 $\alpha$；偶源均值、接口均值、全部角模式和原 model anchor 缺陷均保留。

定义径向模型 $Q_r=Q\Omega_r$、$F_r=Qf_r$，以及

\[
E=Q_\phi-Q\Omega_\phi,\qquad P=F_\phi-Qf_\phi.
\]

在每个实际闭区间上，消费者准确积分定理中的三角 majorant 至三次多项式；其传播没有一般矩阵指数的放大。每个原接口的左右值另付 $E,E_\phi,P,P_\phi$ 跳费，全部 6,143 个接口被实际消费。

## 2. 全圆周的实际上界

| 量 | 全区间严格上界 |
|---|---:|
| $\|E\|$ | $3.127699\times10^{-8}$ |
| $\|E_\phi\|$ | $4.222016\times10^{-6}$ |
| $\|P\|$ | $4.956566\times10^{-8}$ |
| $\|P_\phi\|$ | $7.013365\times10^{-6}$ |
| $\|F_{\phi\phi}\|$ | $5.970523$ |
| $\|Q_{\phi\phi}\|$ | $4.646383$ |

最后两行包含完整模型连接和上述缺陷，分别使用

\[
\|F_{\phi\phi}\|\le(\|\Omega_\phi\|+\|E\|)\|f_\phi\|
                  +\|\partial_\phi f_\phi\|+\|P_\phi\|,
\]
\[
\|Q_{\phi\phi}\|\le\|\Omega_\phi\|^2+
 \|E\|\|\Omega_\phi\|+\|\partial_\phi\Omega_\phi\|+\|E_\phi\|.
\]

对于每个象限的 512 个准确角点 $\phi_k=\pi k/(2\cdot512)$，包括真正的四次旋转接缝，连续线性插值的误差不超过 $\Delta\phi^2\sup\|\partial_\phi^2\cdot\|/8$。实际位置、框架误差分别严格小于

\[
7.024610\times10^{-6},\qquad5.466695\times10^{-6}.
\]

所有逐区间界和接口后状态都在完整原生记录中，可用于比全局最大值更精细的后续连续网格估计。

## 3. 尚须接入的误差

这里的 $F,Q$ 是从规定旋转 model anchor 出发的准确径向 ODE 模型；本篇闭合的是其连续角方向。原浮点径向积分的 directed 误差由另一个正在运行的消费者负责。真实外部固定帽的世界坐标锚、连续修复中心的转移费和最终精确非线性解的比较，也仍须分别支付。

因此本篇不把浮点点云直接宣布为闭合嵌入曲面，不由这些角向界直接推出 reach 或课题最终完成。下一项是将完整径向误差与这里的逐区间二阶界组合为真实双线性网格包络，并继续同对象精确解的构造。
