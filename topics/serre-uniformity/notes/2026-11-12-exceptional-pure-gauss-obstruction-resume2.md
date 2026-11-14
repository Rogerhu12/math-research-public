# Exceptional Fourier：纯 Gauss 恒等式的边界与 content 的精确判据

日期：2026-11-12。状态：**准确的代数接口与失败路线；没有证明一般 $p$ 无 exceptional。**

本篇接 [R92](../results/R92-small-level-fourier-units-and-actual-integrality.md) 和
[Cayley 笔记](2026-11-12-cayley-cubic-fibres-and-exceptional-content-resume2.md)。
这里不扩大已排除水平的列表，也不以随机模型或有限样本替代全称结论。
要处理的仍是同一个素理想内三色 Fourier 和同时为零；此外还有独立的三次 Brandt 周期非消失缺口。

## 1. 一个精确的整系数 content 判据

沿 R92 记 $n=(p-1)/2$，并令
$$
D_p(U)=\operatorname{Res}_T\bigl(\Psi_p(T),A_p(T)+U B_p(T)\bigr)
\in\mathbb Z[U],\qquad \deg D_p\le n.
$$
因为 $\Psi_p$ 首一，resultant 可以无分母地约化到任意特征。
若 $t_1,\ldots,t_n$ 是 $\Psi_p$ 在代数闭包中的根（计重数），则
$$
D_p(U)=\prod_{i=1}^n\bigl(A_p(t_i)+U B_p(t_i)\bigr).
\tag{1.1}
$$
因此，对任意素数 $\ell$，以下两条件等价：

1. $\ell$ 整除 $D_p$ 的每一个整数系数；
2. 在 $\overline{\mathbb F}_\ell$ 中，$\Psi_p,A_p,B_p$ 有共同根。

证明是把 (1.1) 约化到 $\overline{\mathbb F}_\ell[U]$，利用该多项式环为整环：乘积是零多项式，当且仅当其中一个线性因子是零多项式。这里甚至不需要根互异。对 $\ell\ne2,p$，R92 的
$$
A_p(t)=P_0(\xi),\qquad
(\xi-\xi^{-1})B_p(t)=P_1(\xi)-P_2(\xi),\qquad
\sum_jP_j(\xi)=0
$$
说明这也等价于三色共同零点。最后一步除以二，所以本篇的反向等价明确排除 $\ell=2$；R92 的充分 Bézout 判据则不需要这个限制。

若 $\ell>n$，还可等价改为
$$
\ell\mid D_p(0),D_p(1),\ldots,D_p(n).
\tag{1.2}
$$
因为次数至多 $n$ 的非零多项式在 $\mathbb F_\ell$ 中至多有 $n$ 个不同根。
实际 Tate 分母满足 $\ell>p+1$，所以 (1.2) 对所有实际候选都适用。
这解释了只取 $D_p(0)$ 与最高次系数可能留下假共同素因子的原因：这些因子可以来自不同的 $\Psi_p$ 根。

判据没有证明 $D_p$ 的 content 为一。它给完整的固定 $p$ 检测方法，以及一般证明所需控制的准确整系数对象。

## 2. 纯 Gauss 与 Jacobi 型卷积仍不足

令 $V=\mathbb F_{p^2}=\mathbb F_p(\tau)$，$\tau^2=z$ 为非平方。
取函数 $f:V\to\{0,1,\omega,\omega^2\}$，令 $f(0)=0$，且在每条非零 $\mathbb F_p$ 直线上为常数。
假设射影直线上的三色大小都为 $(p+1)/3$。对任意非平凡加法角色 $\psi$，定义
$$
\mathcal F f(u)=\sum_{v\in V}f(v)\psi(\operatorname{Tr}_{V/\mathbb F_p}(uv)).
$$
对 $u\ne0$，唯一垂直直线为 $\mathbb F_p\tau/u$。逐条直线求和得到
$$
\mathcal Ff(u)=p f(\tau/u),\qquad \mathcal Ff(0)=0.
\tag{2.1}
$$
的确，垂直线给 $p-1$，其余每线给 $-1$，而全部射影线的 $f$ 值之和为零。

若还假设
$$
f(\tau/u)=f(u)^{-1}\quad(u\ne0),
\tag{2.2}
$$
并把 $f^{-1}(0)$ 定义为零，则
$$
\boxed{\mathcal Ff=p f^{-1},\qquad
f*f=p f^{-1},\qquad
f*f^{-1}=p^2\delta_0-\mathbf1_V.}
\tag{2.3}
$$
其中卷积在 $V$ 的加法群上取。第二、三式分别由 Fourier 变换后
$p^2f^{-2}=p^2f$ 和 $p^2\mathbf1_{V\setminus\{0\}}$ 得到；Fourier 变换可逆。
这些等式都是整数圆分环上的恒等式，也可在任何特征不为 $p$ 的域内约化。
真实三次乘法角色当然满足 (2.2)，但 (2.2) 比乘法性弱得多。

### 2.1 同时满足 (2.3) 且有三色共同零的明确非 Cartan 例子

取 $p=41,z=3$，把有限点 $b$ 对应到直线 $[1+b\tau]$，无穷点对应到 $[\tau]$。
给无穷点颜色零，有限三色取
$$
\begin{aligned}
B'_0={}&\{0,1,4,6,14,16,17,24,25,27,35,37,40\},\\
B'_1={}&\{2,3,7,8,10,12,18,19,21,26,28,30,32,36\},\\
B'_2={}&\{5,9,11,13,15,20,22,23,29,31,33,34,38,39\}.
\end{aligned}
$$
它们分割 $\mathbb F_{41}$，大小为 $13,14,14$；加上无穷点后三色都为 $14$。
负号交换颜色一、二并保持颜色零；对 $b\ne0$，$b\mapsto1/(3b)$ 保持每一个颜色，且交换 $0,\infty$。
所以 $b\mapsto-1/(3b)$ 反转颜色，正是 (2.2)。因此齐次延拓的 $f$ 满足全部 (2.3)。

然而，$\ell=83$、$\xi=4\in\mathbb F_{83}$ 满足 $\xi^{41}=1$、$\xi\ne1$，并且精确整数模幂给
$$
\sum_{b\in B'_0}4^b=
\sum_{b\in B'_1}4^b=
\sum_{b\in B'_2}4^b=0\pmod{83}.
\tag{2.4}
$$
这里 $83\equiv1\pmod{41}$、$83>42$，且 $83\nmid41(41^2-1)$。
三次单位根可以放在 $\mathbb F_{83^2}$，不影响三个 $0/1$ 和已在 $\mathbb F_{83}$ 中消失。

这**不是实际 exceptional 反例**。其不满足乘法性可以用单一乘法检验看出：$1\in B'_0$，但
$$
(1+\tau)^2=4+2\tau=4(1+21\tau),\qquad21\in B'_1.
$$
故 $f((1+\tau)^2)\ne f(1+\tau)^2$。
该例仅严格排除了只用平衡、齐次性、负号/倒数对称、纯 Gauss 和以及 (2.3) 的一般证明。
不需要再扩大抽象例子族；实际问题的额外输入已经明确定位到完整乘法结构。

## 3. 必须保留的额外关系

真实角色满足，对所有 $b,c\in\mathbb F_p$ 且 $1+zbc\ne0$，
$$
f\!\left(\frac{b+c}{1+zbc}\right)=f(b)f(c).
\tag{3.1}
$$
分母为零时乘积落在无穷点，颜色为零。这是全部 Cartan Möbius 作用，不只是倒数作用。
目前尚未从 (3.1) 导出在 $\mathbb Z[\zeta_p]$ 中产生单位的三色 Bézout 关系。
把 (3.1) 错当成 Fourier 频率的线性代换仍不合法：$b\mapsto\xi^b$ 只保持加法，不是跨特征域同态。

有限群阶在 $\ell$ 下可逆给完全可约性，但不自动保证特定非零 $U$ 字符线投影到 $C^3$ 不变二维空间后非零。
同样，(2.3) 是整个二维加法空间的 Fourier 可逆性信息；本题共同零点位于某一条仿射线的三个部分和，不能由整个空间的可逆性直接排除。

本篇的所有新增断言都已在上文直接证明；不调用未发表的“无 exceptional”猜想作为输入。
