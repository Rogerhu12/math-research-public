# 半整数权热族的标量单值性障碍

日期：2026-11-12。状态：本篇只证明一个完整族的线性微分边界。
它不排除实际素数对角的有限 Frobenius 比较；主目标仍是
[canonical 除 $p$ 行](2026-11-12-canonical-divided-heat-row-and-cm-type.md)
在实际向量上的非零性。

## 1. 实际 Fourier 族与一族准确的延拓分支

沿用[实际热公式](2026-11-12-inert-critical-heat-derivative.md)的

$$
 F(\tau)=\sum_{n\in\mathbb Z}a_n
                 \exp\!\left(\pi i\tau\frac{n^2}{17^2}\right),
 \quad
 a_n=\begin{cases}
 \lambda(n)\zeta_{289}^{19n^2},&17\nmid n,\\
 0,&17\mid n,
 \end{cases}
 \quad\lambda(3)=-i.
 \tag{1}
$$

这是实际非零的半整数权族；例如已证 $B_4\ne0$。
为避免依赖未指定的半整数权乘子系统，直接取偶格 $34\mathbb Z$，定义

$$
 \vartheta_r(\tau)=\sum_{k\in\mathbb Z}
       e^{\pi i\tau(34k+r/34)^2},\qquad r\in\mathbb Z/1156\mathbb Z.
$$

$a_n$ 的周期整除 $578$，所以
$F=\sum_{a\bmod578}a_a\vartheta_{2a}$。
令 $M=2312=2\cdot34^2$。逐项可见
$\vartheta_r(\tau+M)=\vartheta_r(\tau)$。
一次 Poisson 求和给

$$
 \vartheta_r(-1/\tau)
  =\frac{\sqrt{-i\tau}}{34}
       \sum_{s\bmod1156}e^{2\pi i rs/1156}\vartheta_s(\tau).
 \tag{2}
$$

改变 Fourier 指数正负只改变有限矩阵的逆，不改变下面的结论。
有限 Fourier 矩阵可逆；将 (2)、$T^{-Mn}$ 和逆变换合成，得

$$
 \gamma_n=\begin{pmatrix}1&0\\Mn&1\end{pmatrix},\qquad
 F(\gamma_n\tau)=\epsilon_n(Mn\tau+1)^{1/2}F(\tau),
 \quad \epsilon_n\ne0.
 \tag{3}
$$

$\epsilon_n$ 仅记录一致选根的常数相位；它不依赖 $\tau$。
这里重要的是有限 theta 矩阵在 $T^{Mn}$ 上准确为单位矩阵，
不是某个只在实际 $F$ 上数值核过的特征关系。

令 $\lambda_{\rm Leg}(\tau)$ 为 Legendre 模参数。
$M$ 是偶数，故所有 $\gamma_n\in\Gamma(2)$ 都固定这个参数。
因此，作为 $\lambda_{\rm Leg}$ 的局部函数，$F$ 的解析延拓包含
(3) 的所有分支。基点可选在 $\tau=i$ 的一个任意小邻域内、且
$F$ 不为零的点；$F(i)=0$ 不影响该论证。

## 2. 这些分支有无限线性维数

对任意有限个互异正整数 $n_1,\ldots,n_s$，假设这些分支有线性关系。
在 $F\ne0$ 的小开集除去共同因子，便得到

$$
 \sum_{j=1}^s c_j(Mn_j\tau+1)^{1/2}=0.
 \tag{4}
$$

这些平方根的分支点是两两不同的 $-1/(Mn_j)$。
把 (4) 沿避开有限个分支点的路径延拓到其中一个点的穿孔邻域，
再沿该点绕一周。只有相应的一项变号；与原式相减，得到对应
$c_j=0$。逐项如此，所有系数都为零。

所以 $F$ 的解析延拓分支张成无限维复向量空间。
一个有限阶线性微分方程的所有解析延拓解则始终位于有限维解空间。
由此严格得到

$$
 \boxed{\quad
 F(\tau(\lambda_{\rm Leg}))\text{ 不满足任何非零的有限阶
 线性微分方程，系数在 }\mathbb C(\lambda_{\rm Leg})
 \text{ 或其有限代数扩张中。}
 \quad} \tag{5}
$$

代数扩张情形可由限制标量化为有理函数系数方程。
若某个候选方程还有额外的有限奇点，可将上述路径稍作变形以避开它们；
不需穿过微分方程的奇点，也不会改变每个 $\gamma_n$ 的延拓作用。
本证明不依赖 $F$ 的某一非零 Taylor 系数的大小。

## 3. 对固定秩热连接路线的准确含义

有限 theta/Weil 表示确实在 (2) 中出现。
但完整标量 $F$ 还带有 (3) 的半权因子；有限矩阵本身没有消除它。
所以不能仅凭有限 theta 向量，就把实际标量族认定为一个固定有限秩
代数连接的水平分量：这种认定会给出 (5) 所排除的线性方程。

这一论证与整数权的情形不同。半权因子的平方是
$Mn\tau+1$，不再有彼此独立的平方根分支点。
同样，实际 $F$ 与一个非零参考半权 theta 的比值，在共同有限级别上
是一个权零模函数，因而代数于 Legendre 参数。这两个事实都不与
(5) 矛盾。

但是先在函数层面除去参考，与对实际 Taylor/Mahler 变换后取参考商，
是不同的运算。后者仍保留参考与全部高 jet 的交叉项，已在
[共同参考解析行](2026-11-12-inert-fixed-isogeny-jets-and-normalized-rows.md)
中准确写出。因此本篇不将权零代数商认定为目标的完整周期对象。

尤其，(5) 没有排除以下可能：仅在 $N=(p+1)/2$ 的素数对角上，
实际 $R_NF(i)/p$ 存在一个另外证明的有限 Frobenius 或 Bockstein 比较。
这样的比较仍值得研究；它必须准确给出整格、实际提升和求值行，
不能从完整族的有限 theta 维数直接推得。
