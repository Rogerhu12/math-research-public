# R625：同完整行、同Euclidean惩罚的QR/SVD方向

日期：2026-11-27；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

此新helper只消费当前求解已经必需的完整Jac，经原末10个线性端条件准确消元，
以及实际触发的L/h活动坐标准确消元后形成的A、b。
所有原微分行和原row scale保留；剩余列不再缩放。
新活动面与非线性物理盒的选择由实际driver负责，本helper不更改它们。

## 数学恒等与惩罚规范

原LSMR对正$\lambda$求的是

$$
\min_x\ \|Ax-b\|_2^2+\lambda\|x\|_2^2.
$$

其中x是原mixed物理坐标的剩余增量。
已准确指定的端增量对Euclidean惩罚只贡献常数；硬设为0的活动增量同理。
不能借列归一化把惩罚改成$\lambda\|Dx\|^2$。

对完整方阵或高矩阵取薄QR及R的完整SVD：

$$
A=QR,\qquad c=Q^Tb,\qquad R=U\Sigma V^T.
$$

由于$Q^TQ=I$，目标中与x有关的项是$\|Rx-c\|^2+\lambda\|x\|^2$。
所以唯一阻尼解为

$$
x_\lambda=V\operatorname{diag}\left(\frac{\sigma_i}{\sigma_i^2+\lambda}\right)U^Tc.
$$

全部奇异值进入同一个表达式，包括小于数值rank报告阈值的值。
$\sigma_i=0$时滤波值自然为0，并非截秩。
源码用`(sigma/hypot(sigma,sqrt(lambda)))/hypot(...)`计算同一滤波，避免先平方大奇异值。
没有构造$A^TA$，也没有重新计算Jac。

原65点网的形状包括1216×1216、1216×1215和1216×1214；
若后继真实范围采用129点网，同样支持2432×2432及少1/2列。
每一个真实Jac、实际活动mask的因子只需建立一次，所有正lambda复用。
信赖域预测与接受仍由driver用原未缩放完整matrix/residual进行。

## 接口与费用

源码：`scripts/r625_complete_rows_euclidean_qr_svd_agent.py`。

```python
factor = EuclideanCompleteRowFactor(A, b, clock, shared_counts, label)
free_solution, report = factor.solve(positive_lambda)
factor.receipt
factor_receipts()
```

`clock.check(str)`直接使用原科学时钟；`shared_counts`为原driver共有dict，
所有转换、QR、SVD、滤波、残差/驻点matvec、失败和partial时间显式累加。
`factor_receipts()`保留小记录，即使构造器在异常/时钟中断后没能装入driver缓存，
仍可在FINAL取到实际阶段、形状、来源hash和已付时间；不保存原矩阵或因子数组。

每次必要线性解同时报告真实原scaled残差$Ax-b$和
$A^T(Ax-b)+\lambda x$的数值范数。这些只是已执行求解的观察，
不会产生新的诊断资格门，也不据小残差推断非线性物理域可行、逆证书或整体收敛。
原端h接近上界的真实约束仍必须由driver按同一物理盒保留。

本地仅源码、纸面恒等、AST与hash；没有科学执行或重复已付Jac/探针。
