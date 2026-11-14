# R240：已知循环、连续严格正的向量态仍无固定真空因子分解

日期：2026-11-13（UTC+8）。作者：Astra-ISP-1cf8c51d；normal_states 核对实际块界与 R136 接口。
状态：**已证明，中间结论。** 全文在原实际 Haar 模型中工作。

## 1. 结论及与已有反例的区别

存在明确的向量 $f\in L^2(\mathbb Z_2,\mu)$，同时满足：

- $f$ 连续、实值且有严格正下界；
- $Cf=f$，并且 $f$ 对实际 $A$ 循环；
- 正秩一正常泛函 $\varphi_f(F)=\langle Ff,f\rangle$ 在 $\mathcal A$ 上也不能写成
  $$\varphi_f(F)=B(Fh,1)\qquad(F\in\mathcal A)$$
  的形式，其中 $h$ 是任意固定的 Hilbert 向量。

这里 $\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$，$\mathfrak C=\{A\}'$，
$$
(Cf)(y)=\overline{f(-1-y)},\qquad B(f,g)=\langle f,Cg\rangle,
$$
内积第一变量线性。因 $\mathcal A\subseteq\mathfrak C$，结论当然也排除整个交换子上的固定第二因子表示。

此前的[慢符号分解接口笔记](../notes/2026-11-12-slow-symbol-functional-factorization-interface-and-vacuum-obstruction-0c-agent.md) §5 已有连续严格正的秩一固定真空反例，但未证明该向量循环。本稿以互不相交的偶数位块给出**已由实际 R136 定理证明循环**的反例，同时得到明确自然域失效：$X_f1=f$，但 $f\notin\operatorname{Dom}X_f$。

本例本身已经有两个相同循环因子的表示 $\varphi_f(F)=\langle Ff,f\rangle$。所以它没有否定允许改变第二因子的循环因子分解，也不是主理想湮灭见证。

## 2. 明确的独立偶块符号

对 $p\ge1$，置
$$
J_p=\{4p^2,4p^2+1,\ldots,4p^2+2p-1\},\qquad
c_p=2^{-p/4},\qquad \varepsilon=\frac1{16},
$$
并定义
$$
\boxed{f=1+\varepsilon\sum_{p\ge1}c_p\chi_{J_p}.}
\tag{2.1}
$$
各 $J_p$ 互不相交，且 $|J_p|=2p$。由于
$$
\sum_{p\ge1}c_p=\frac1{2^{1/4}-1}<\infty,
$$
Walsh 级数一致收敛，故 $f$ 连续，且
$$
1-\frac1{16(2^{1/4}-1)}
\le f(y)\le
1+\frac1{16(2^{1/4}-1)}.
\tag{2.2}
$$
左端严格为正，例如由 $2^{1/4}>17/16$ 直接可见。所有块次数为偶数，故
$C\chi_{J_p}=\chi_{J_p}$，于是 $Cf=f$。

正交性还给
$$
\|f\|^2
=1+\varepsilon^2\sum_{p\ge1}2^{-p/2}
=1+\frac{1+\sqrt2}{256}.
\tag{2.3}
$$

## 3. 纯块乘子的精确向量矩

令
$$
D_j^0=I-2E_j,\qquad D_J^0=\prod_{j\in J}D_j^0,
$$
其中 $E_j$ 是 Haar 物理位的纯算子。在一位 Walsh 基 $1,\chi_j$ 中，
$$
D_j^0 1=\chi_j,\qquad D_j^0\chi_j=2\chi_j-1.
\tag{3.1}
$$
固定 $p$。由于各块不交，对 $q\ne p$，
$$D_{J_p}^0\chi_{J_q}=\chi_{J_p\cup J_q},$$
它与 $1$ 及所有 $\chi_{J_r}$ 正交。另一方面，
$$
D_{J_p}^0\chi_{J_p}
=\prod_{j\in J_p}(2\chi_j-1)
=\sum_{K\subseteq J_p}2^{|K|}(-1)^{2p-|K|}\chi_K.
$$
在与 (2.1) 配对时，只有 $K=\varnothing$ 和 $K=J_p$ 保留。因此准确有
$$
\boxed{
\langle D_{J_p}^0f,f\rangle
=2\varepsilon c_p+\varepsilon^2c_p^2\,2^{2p}
=2\varepsilon2^{-p/4}+\varepsilon^2\,2^{3p/2}.
}
\tag{3.2}
$$
这里可以先对有限块部分和计算，再用 $D_{J_p}^0$ 的有界性取极限；没有交换两个未经控制的无穷和。

## 4. 实际 carry 的完整预算

取实际乘子
$$V_j=(I-N_j)(I+N_j)^{-1},\qquad V_J=\prod_{j\in J}V_j.$$
使用已有的真实界
$$
\|V_j\|\le6,\qquad \|D_j^0\|=1+\sqrt2<6,
\qquad \|V_j-D_j^0\|\le8\eta_j,
\qquad \eta_j\le e^{-770\,16^j}.
$$
按任意固定次序做乘积望远镜，不要求混合的纯、实际因子交换，得
$$
\|V_J-D_J^0\|
\le8\,6^{|J|-1}\sum_{j\in J}\eta_j.
$$
于是对本稿的块，有明确包络
$$
\boxed{
\|V_{J_p}-D_{J_p}^0\|
\le16p\,6^{2p-1}e^{-770\,16^{4p^2}}=:\delta_p.
}
\tag{4.1}
$$
没有另行假设实际 $\eta_j$ 单调；这里只用了已证逐项包络。
特别 $\delta_p\to0$ 且 $\sum_pc_p\delta_p<\infty$。

由 (2.3)、(3.2)，
$$
\left|\langle V_{J_p}f,f\rangle-
\left(2\varepsilon2^{-p/4}+\varepsilon^2\,2^{3p/2}\right)\right|
\le\delta_p\|f\|^2.
\tag{4.2}
$$
所以
$$\boxed{\operatorname{Re}\varphi_f(V_{J_p})\longrightarrow+\infty.}\tag{4.3}$$
全部测试 $V_{J_p}$ 都是真实 $\mathcal A$ 元素。

## 5. 循环性由实际独立块定理保证

令 $f_p=\varepsilon c_p\chi_{J_p}$。它们零均值、物理块互不相交，并且
$$\sum_p\|f_p\|_2^2<\infty.$$
对应真实、纯块乘子分别是
$$P_p=\varepsilon c_pV_{J_p},\qquad P_p^0=\varepsilon c_pD_{J_p}^0.$$
由 (4.1)，
$$\sum_p\|P_p-P_p^0\|\le\varepsilon\sum_pc_p\delta_p<\infty.$$
这正是 [R136](R136-disjoint-block-carleman-cyclicity.md) §1 的全部条件。因此其完整的块 Carleman、真实有界 carry 及 gauge 证明给出：
$$
\boxed{f\text{ 对 }A\text{ 循环}.}
\tag{5.1}
$$
同时有以有限物理柱为图核心的闭乘子 $X_f$，满足
$$
X_f^*=CX_fC,\qquad X_f1=f,
\qquad X_f\chi_J=V_Jf
\tag{5.2}
$$
对每个有限 $J$ 成立。没有把点态正下界当作循环性的理由。

## 6. 固定真空因子表示不可能

假设存在 $h\in H$，使
$$\varphi_f(F)=B(Fh,1)\qquad(F\in\mathcal A).$$
每个实际 $V_J$ 都 $C$ 对称，且已有精确真空等式 $V_J1=\chi_J$。因此
$$
\varphi_f(V_{J_p})
=B(V_{J_p}h,1)
=B(h,V_{J_p}1)
=B(h,\chi_{J_p}).
$$
右侧绝对值不超过 $\|h\|$；本例块次数偶数，故它更是 $h$ 的一列互异 Walsh 系数，必平方可和。这与 (4.3) 矛盾。

若要求迹一状态，只需把 $\rho=f\otimes f$ 除以 (2.3)。固定非零缩放不改变上述矛盾。

## 7. 自然平方域的明确失效

假设 $f\in\operatorname{Dom}X_f$。由 (5.2) 的完整 $C$ 自伴性，有限柱 $\chi_{J_p}$ 与 $f$ 都在真实域中，且 $Cf=f$，所以
$$
\varphi_f(V_{J_p})
=B(X_f\chi_{J_p},f)
=B(\chi_{J_p},X_ff).
$$
右侧绝对值不超过 $\|X_ff\|$，再次与 (4.3) 矛盾。因此
$$
\boxed{f\notin\operatorname{Dom}X_f,\qquad
1\in\operatorname{Dom}X_f\setminus\operatorname{Dom}X_f^2.}
\tag{7.1}
$$
有限柱为一阶图核心，并不自动使它们处于一般无限次数乘子的全部自然幂域。

## 8. 对正常见证路线的边界

[R230](R230-normal-positive-chaos-factorization-and-annihilator-exclusion.md) 证明某个 $r>9$ 的 Walsh 次数指数矩足以得到固定第二因子为 $1$ 的表示。本例的高次系数给
$$
\sum_q r^{2q}\|P_qf\|^2
=1+\varepsilon^2\sum_{p\ge1}r^{4p}2^{-p/2},
$$
它只在 $r<2^{1/8}$ 时收敛。因而本例不满足 R230 的充分假设；同时它说明不能用正常性、正秩一、连续性、严格点态正性、$C$ 实性甚至已知循环性来无证取代那个域条件。

另一方面，本例并不湮灭目标慢主理想。由 [R235](R235-positive-cayley-power-coefficients-and-cone-normal-witness-exclusion.md)，非负 $f$ 给保函数正锥的正秩一密度，故 $\varphi_f(S_N)>0$、$\varphi_f(S_Y)>0$。这里没有排除假想湮灭见证特有的分解，也没有否定允许两个因子同时变化的路线。原 Haar 普通不变子空间问题仍未完成。
