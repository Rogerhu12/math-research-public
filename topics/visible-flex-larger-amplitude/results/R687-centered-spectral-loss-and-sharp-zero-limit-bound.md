# R687：中心化正谱目标的正项表达与趋零最大误差界

2026-11-26，Astra-larger-e4e2a2bf-20261126 / solver。

**状态：已证明。** 新增内容是中心化目标的无常数相减表达、扣去所有观察项共同常数底后的有限最大误差上界，以及明确依赖 $L/\epsilon$ 的残差 Hessian 权比上界。这些都是有限残差空间的代数命题，没有新的科学运行、候选或几何证书。

[R660](R660-positive-spectral-Gram-blocks-and-maximum-control.md) 已经证明正谱目标的共同常数底、全部正权观察行的零集、固定阶段参数和真实回溯责任；[R664](R664-positive-spectral-residual-Hessian-and-true-gradient-pullback.md) 已经给出准确正残差 Hessian；[R673](R673-full-Phi-damping-face-gap-and-true-ray-continuation.md) 已经区分块权跨度与完整场条件数，并证明有限预算可行模型步的下降性质。本文不重新将这些结论登记为新增结果。

## 1. 同一有限目标的中心化表达

保留全部有限观察块 $E_i=E_i^T\in\mathbb R^{2\times2}$ 和严格正权 $\nu_i$，$\sum_i\nu_i=1$。取整数 $k\ge1$、$p=2k$、$\epsilon>0$、$\sigma>0$。沿 R660 定义

$$
\Phi=\sum_i\nu_i\sigma^{-2k}
\operatorname{tr}(E_i^2+\epsilon^2I)^k,
\qquad
\Phi_0=2(\epsilon/\sigma)^{2k},
\qquad S=\Phi-\Phi_0.
\tag{1}
$$

**命题 1。** 有准确恒等式

$$
S=\sigma^{-2k}\sum_i\nu_i\sum_{j=1}^k
{k\choose j}\epsilon^{2(k-j)}\|E_i^j\|_F^2.
\tag{2}
$$

特别地，记

$$
\widehat S=\frac{\sigma^{2k}}{k\epsilon^{2k-2}}S,
\qquad Q=\sum_i\nu_i\|E_i\|_F^2,
\tag{3}
$$

则

$$
\widehat S
=Q+\sum_i\nu_i\sum_{j=2}^k
\frac1k{k\choose j}\epsilon^{2-2j}\|E_i^j\|_F^2
\ge Q.
\tag{4}
$$

当 $k=1$ 时第二重和为空，$\widehat S=Q$。

**证明。** 因为 $E_i^2$ 与 $I$ 对易，二项展开给出

$$
(E_i^2+\epsilon^2I)^k
=\epsilon^{2k}I+\sum_{j=1}^k
{k\choose j}\epsilon^{2(k-j)}E_i^{2j}.
$$

对称性给 $(E_i^j)^T E_i^j=E_i^{2j}$，故
$\operatorname{tr}(E_i^{2j})=\|E_i^j\|_F^2\ge0$。取迹、乘正权求和，常数项恰是 $\Phi_0$，证明 (2)。分离 $j=1$ 项并乘 (3) 的正常数即得 (4)。证毕。

式 (2) 不需要先算两个近等的标量再相减；可直接累加正系数乘平方范数。也可用两个特征值的偶次幂实现同一表达。实际浮点矩阵乘法、谱计算或高次幂仍有舍入、溢出和下溢责任，本文没有把该表达冒称向外舍入算法。

中心化只减常数，因此 $D S=D\Phi$、$D^2 S=D^2\Phi$，同阶段任意两点的精确差相同。归一化 (3) 则确实把梯度和 Hessian 同乘正常数。在 $E_i\to0$ 时 (4) 给统一的二次主项 $Q$；它不声称不同 $k,\epsilon$ 的整个目标只差全局比例。

## 2. 扣掉常数底后的有限最大误差上界

记

$$
M=\max_i\|E_i\|_{\rm op},\qquad
\nu_{\min}=\min_i\nu_i>0,
\qquad
f(t)=\frac{(t^2+\epsilon^2)^k-\epsilon^{2k}}{\sigma^{2k}}
\quad(t\ge0).
\tag{5}
$$

**命题 2。** 有

$$
\nu_{\min} f(M)\le S\le2 f(M).
\tag{6}
$$

因此

$$
\sqrt{\bigl(\epsilon^{2k}+\sigma^{2k}S/2\bigr)^{1/k}-\epsilon^2}
\le M\le
\sqrt{\bigl(\epsilon^{2k}+\sigma^{2k}S/\nu_{\min}\bigr)^{1/k}-\epsilon^2}.
\tag{7}
$$

另有不需先求相近正数之差的上界

$$
M^2\le\frac{\widehat S}{\nu_{\min}}
=\frac{\sigma^{2k}S}{k\epsilon^{2k-2}\nu_{\min}}.
\tag{8}
$$

**证明。** 令 $\lambda_{i,1},\lambda_{i,2}$ 为 $E_i$ 的两个实特征值。由 (1)，

$$
S=\sum_i\nu_i\sum_{a=1}^2 f(|\lambda_{i,a}|).
$$

$f$ 连续严格递增于 $[0,\infty)$，$f(0)=0$。每个 $|\lambda_{i,a}|\le M$，而 $\sum_i\nu_i=1$，故 $S\le2f(M)$。有限集合中有某个 $(i,a)$ 取到 $M$；该项的权至少为 $\nu_{\min}$，其余项非负，故 $S\ge\nu_{\min}f(M)$。把单调函数 $f$ 反解即得 (7)，根内非负由 $S\ge0$ 保证。

再由某个最大特征值有 $Q\ge\nu_{\min}M^2$，结合 (4) 即得 (8)。证毕。

式 (7) 的左界与 R660 将原 $\Phi$ 写成 $S+\Phi_0$ 后的左界相同；新增改进在右界：所有其它观察项的共同常数底先被准确扣除。R660 原右界在 $S=0$ 时为

$$
\epsilon\sqrt{(2/\nu_{\min})^{1/k}-1},
$$

它一般仍为正；本文 (7) 和 (8) 则在 $S\to0$ 时趋零。小 $\nu_{\min}$ 仍会使界变松，本命题不删去小正权观察行来改善数值。

对于 (7) 中任一 $a\in\{2,\nu_{\min}\}$，根内也有准确恒等式

$$
\bigl(\epsilon^{2k}+\sigma^{2k}S/a\bigr)^{1/k}-\epsilon^2
=\epsilon^2\operatorname{expm1}
\left(\frac1k\operatorname{log1p}
\left(\frac{\sigma^{2k}S}{a\epsilon^{2k}}\right)\right).
\tag{9}
$$

这提供另一种避免最终相近数相减的实现表达，不自动保证普通 `log1p`、`expm1` 为严格区间界。需要证书时仍须按原向外运算规范求值。

## 3. 显式的残差 Hessian 权比上界

沿 R664 记

$$
h(t)=t\left(\frac{t^2+\epsilon^2}{\sigma^2}\right)^{k-1},
\qquad H_F(E)=Dh(E)
$$

并以 Frobenius 内积把 $H_F$ 视为对称矩阵空间上的正定线性算子。这里不包括场 Jacobian，也不包括完整目标 Hessian 中的残差二阶导数项。

**命题 3。** 若 $\|E\|_{\rm op}\le L$，则在 $k=1$ 时 $H_F=I$；在 $k\ge2$ 时

$$
m I\preceq H_F(E)\preceq m\,\chi_k(L/\epsilon) I,
\qquad
m=(\epsilon/\sigma)^{2k-2},
\tag{10}
$$

$$
\chi_k(r)=(1+r^2)^{k-2}\bigl(1+(2k-1)r^2\bigr).
\tag{11}
$$

**证明。** R664 已给出 $H_F$ 在谱 Frobenius 正交坐标中的三个特征值：
$h'(\lambda_1)$、$h'(\lambda_2)$ 和两者之间的正差商平均。其中

$$
h'(t)=\frac{(t^2+\epsilon^2)^{k-2}
[\epsilon^2+(2k-1)t^2]}{\sigma^{2k-2}}.
\tag{12}
$$

对 $k\ge2$，它是 $t^2$ 的系数非负多项式，故在 $|t|\le L$ 上介于 $h'(0)=m$ 与 $h'(L)=m\chi_k(L/\epsilon)$ 之间。差商等于沿两实特征值间线段的 $h'$ 积分平均，该线段仍位于 $[-L,L]$，所以同样满足这两个界。谱定理给 (10)。$k=1$ 时 $h(t)=t$，结论直接成立。证毕。

p=4 时 $\chi_2(r)=1+3r^2$；p=8 时 $\chi_4(r)=(1+r^2)^2(1+7r^2)$。因而在同一已知残差范围内，可以明确量化改变 $p$ 或 $\epsilon$ 对块权跨度的作用。这里的谱是 Frobenius 正交坐标的谱；对原三项坐标 $(e,f,d)$ 的矩阵 $T^*H_FT$，由于 $T^*T=\operatorname{diag}(1,2,1)$，可据此得到 $\kappa_2(T^*H_FT)\le2\chi_k$，不能漏掉坐标因素而把 (11) 直接称为原三项 Euclidean 块条件数。

更不能把它称为整个受约束 QP 的条件数。完整 Jacobian、母空间、冗余列、阻尼和活动面责任仍如 R673、R685 所述。

## 4. 对当前实现的准确用途与边界

1. 如果后续实现中心化统计，应直接用 (2) 求值并独立保留原 $\Phi$ 字段及参数身份；记录其与原目标精确对应的常数。真实回溯在同一阶段可用中心化值。若同时采用 (3) 的单位，则梯度、模型、阻尼平方和绝对停止阈值必须按 R673 的同比例规律协调。
2. 新 $p/\epsilon$ 阶段仍对应 R660 已证的同一有限残差零集，但它改变了求解目标，不能跨目标减 $\Phi$。当前旧 planner 的 p8 守卫应由明确的新版本处理，不能重写父报告假装未换目标。
3. 保持原 $\Phi$ 而改变正 Gram 模型也可以沿 R664、R673 的下降命题提出方向；这不是本文新增的下降定理。若以新块 $\widetilde B^T\widetilde B$ 替换旧块、却仍要求原真实梯度，必须同步把虚拟右端改为 $\widetilde B^{-T}g_0$，不能保留旧虚拟右端或改成 $\widetilde B r$。同一新块的粗预条件器也需一致重建。

本文没有增加先通过 fixture 或审查才能继续的门。尚未实现或科学执行中心化求值、目标 continuation 或改变 Gram 的新方向，当前约百分之一的 metric 缺陷也不由本文下降。式 (7)–(8) 仅控制全部有限观察值；连续曲面误差、固定 g 的实际精化收敛、全族 reach 与幅度标准仍须在实际候选上完成。
