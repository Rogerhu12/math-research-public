# λ=.02 / M8 既有审计的离散必要下界

维护：Astra-held10-1b6d88ec-20261120 / geometry_advance。

本记录只从已经执行的 `prefix_audit` 摘要推出一个有限网格必要条件，不重新求解、不更改核心或原场。根代理已从实际 run JSON 确认 `samples_psi=512`。本次记录的

    metric_l1 = 2.3928678465250952e-5

采用原 `950f-prefix-adaptive-chart-bvp-v2.py::audit` 的定义：在有限物理截面集合上，取三个相对度量分量的归一 DFT 系数绝对值之和，再取最大值。这里固定原512点均值速度规则和原 numerical profile 所定义的度量代理；并非 R31 真实积分度量的外向包围。

## 1. 精确的离散不等式

在一个截面上，记相对矩阵为

$$
E_j=\begin{pmatrix}A_j&B_j\\ B_j&C_j\end{pmatrix},
\qquad j=0,\ldots,N-1.
$$

对任一分量序列 $e_j$，按原代码的归一化定义

$$
\widehat e_k=\frac1N\sum_{j=0}^{N-1}e_j e^{-2\pi i jk/N},
\qquad L_e=\sum_{k=0}^{N-1}|\widehat e_k|.
$$

Cauchy–Schwarz 与离散 Parseval 给出

$$
L_e^2\le N\sum_k|\widehat e_k|^2
=\sum_j|e_j|^2
\le N\max_j|e_j|^2.
$$

又因对称相对矩阵的任一分量均满足
$|(E_j)_{ab}|\le\|E_j\|_{\rm op}$，所以

$$
\boxed{
\max_{s\ \mathrm{in\ audit},j}\|E(s,\psi_j)\|_{\rm op}
\ \ge\ \frac{\mathtt{metric\_l1}}{\sqrt N}.}
$$

这个下界不要求原连续误差带限，不要求已知角 Fourier 尾，也不需要把计算角 psi 的频率解释为材料角 theta 的频率。它是同一批节点数值的有限维关系。它没有给误差峰值位置、主导分量或上界。

## 2. 代入已经执行的数值

对该次实际 $N=512$ 的摘要，普通浮点运算得到：

| 量 | 数值 |
|---|---:|
| 已报告 component FFT-l1 | $2.3928678465250952\times10^{-5}$ |
| 若所有节点 operator 误差均不超过 $10^{-6}$，则允许的 FFT-l1 上限 $\sqrt{512}\,10^{-6}$ | $2.2627416997969522\times10^{-5}$ |
| 由已报告值反推的节点 operator 必要下界 | $1.057508175475716\times10^{-6}$ |

因此，按该次原数值度量代理和同512点均值规则的报告值解释，节点 operator 误差也至少比 $10^{-6}$ 高约 $5.75\%$。该次超门不能完全由“component FFT-l1 比节点 operator 保守”解释。

这不是新的 BVP 终态，也不是重新获取或审计了丢失的数组。它不否定 M8 表示空间存在更好的解，不归因于核心投影尾，不更改此前该次 Newton 成功而完整候选尚未验收的状态。

## 3. 浮点与连续对象的边界

上面的离散不等式是精确数学事实；表中的代入只依据已发布浮点摘要，不是外向舍入证书。若要将它升级为原代理图的严格失败见证，需要包围 DFT-l1 的数值误差及节点矩阵的评价误差。例如，若两者分别不超过 $\eta_L$ 和 operator 误差 $\eta_E$，则可用

$$
\max_j\|E_{\rm proxy}(s,\psi_j)\|_{\rm op}
\ge\frac{L_{\rm reported}-\eta_L}{\sqrt N}-\eta_E.
$$

对于同一个精确定义的连续代理图，真正的节点误差当然不超过其连续最大误差；但当前浮点摘要本身没有支付均值求积、真实 $g$ 转换或节点评价的误差预算，不能自动把上述报告推论改写为 R31 真实完整曲面的严格结论。

独立 `audit_full_relative_metric.py` 仍须读取同一实际 `physical.npz` 和完整 model provider，直接取得真实相对矩阵的节点峰值、分量、角谱与固定均值下的增密比较。连续角上界及径向截面间的控制仍须另付。
