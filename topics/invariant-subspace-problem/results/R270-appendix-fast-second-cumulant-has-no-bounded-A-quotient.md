# R270 附录：真实二阶快累积量不能有界除以 A

日期：2026-11-13（UTC）。normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：已证明；Astra-ISP-1cf8c51d 与 kernel_resume_1cf 全文核对原系数、dyadic gauge 和权跳跃。该反例记录已排除的全累积量有界除法路线。
这里的负结论只关于有界因式分解，不与 R151 的强主理想近单位、单射稠密性或正四次幂型矛盾。

## 1. 固定原实例

取原实际正行
$$
a_j=\frac1{j+2},\qquad w=0,
$$
以及实际 $N_j=A^{2^j}/d_j$，$d_j=\|A^{2^j}\|$。
R270B 的二阶共振累积量是
$$
G_2=-4\sum_{j\ge0}a_j^2N_j^2(I+N_j)^{-2}.
\tag{1.1}
$$
它按范数绝对收敛，真实属于 R151 的 $\mathcal G$，字符为零。
置 $B=-G_2$。

**命题。** 不存在 $T\in B(H)$ 使
$$
AT=B.
\tag{1.2}
$$
特别 $G_2\notin A\{A\}'$，也不能用任何正整数幂 $A^m$ 作有界除法。
同样不存在 $TA=B$ 的有界左商。

## 2. 对任意有界商的实际系数下界

记 $W_k=\|A^k\|$，$\gamma_k(E)$ 为 $E\in\mathcal A$ 的忠实连续形式系数。
对 dyadic 根 $\zeta$，原酉 gauge 满足
$$
\gamma_\zeta(A)=\zeta A.
$$
令
$$
\mathcal E_{k,m}(S)
=\frac1{2^m}\sum_{\zeta^{2^m}=1}\zeta^{-k}\gamma_\zeta(S),
\qquad \|\mathcal E_{k,m}(S)\|\le\|S\|.
\tag{2.1}
$$
此式对任意 $S\in B(H)$ 都有定义。

固定 $E\in\mathcal A$、固定 $k\ge0$。
先对有限多项式检查，再用规范闭代数中的范数逼近和 (2.1) 的收缩性，得到
$$
\mathcal E_{k,m}(E)\longrightarrow \gamma_k(E)A^k
\quad\text{算子范数}.
\tag{2.2}
$$
有限多项式的不同非负次数在充分大的 $2^m$ 下不会混到同一余类；
所以此处没有假定 $E$ 的形式级数本身范数绝对收敛。

若 $AT=E$，则真实 gauge 恒等式给
$$
A\mathcal E_{k,m}(T)=\mathcal E_{k+1,m}(E).
\tag{2.3}
$$
左侧第二因子一致有界；取其 WOT 收敛子网。
由 (2.2)、有界左乘的 WOT 连续性和 $A$ 的单射性，其极限只能是
$\gamma_{k+1}(E)A^k$。
WOT 闭球于是给
$$
\boxed{
\|T\|\ge |\gamma_{k+1}(E)|W_k\qquad(k\ge0).
}
\tag{2.4}
$$
这个必要界不要求预先知道 $T\in\mathcal A$，甚至不要求预先知道 $T$ 与 $A$ 交换。

事实上，当 $E$ 与 $A$ 交换时，$AT=E$ 自动推出
$A(TA-AT)=0$，故 $TA=AT$。
若原先是 $TA=E$，则 $(TA-AT)A=0$；$A$ 值域稠密也迫 $TA=AT$。
因此左右有界商在本实例中等价。

## 3. 二阶实际系数没有符号消去

R270B 的真实范数展开为
$$
B=4\sum_{i\ge0}\sum_{k\ge2}
a_i^2(-1)^k(k-1)\frac{A^{k2^i}}{d_i^k}.
\tag{3.1}
$$
固定 $n=2^j$。
在形式次数 $2n=2^{j+1}$ 上，可能的 $i$ 只有 $0\le i\le j$，
相应 $k=2^{j+1-i}$ 全部为偶数。
所有贡献同号，所以
$$
\begin{aligned}
\gamma_{2^{j+1}}(B)
&=4\sum_{i=0}^j
a_i^2(2^{j+1-i}-1)d_i^{-2^{j+1-i}}\\
&\ge 4a_j^2d_j^{-2}.
\end{aligned}
\tag{3.2}
$$
连续系数提取与 R270B 的收敛展开保证 (3.2) 是实际系数，不是未定义形式级数的比较。

## 4. 真实 dyadic 跳跃使商范数无界

R109 给准确公式
$$
d_j=e^{-\Lambda_j},\qquad
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j,
\tag{4.1}
$$
以及原二进位权乘积
$$
W_{2^{j+1}-1}=\prod_{i=0}^{j}d_i.
\tag{4.2}
$$
因此
$$
\begin{aligned}
\log\frac{W_{2^{j+1}-1}}{d_j^2}
&=2\Lambda_j-\sum_{i=0}^j\Lambda_i\\
&=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\end{aligned}
\tag{4.3}
$$
右侧趋于正无穷。
把 $k=2^{j+1}-1$ 代入 (2.4)，再用 (3.2)，得到
$$
\|T\|\ge
\frac4{(j+2)^2}
\exp\left[
\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}
\right]\longrightarrow+\infty.
\tag{4.4}
$$
矛盾，命题得证。

## 5. 与快类正结论的准确关系

$G_2$ 是非零快类元素；R151 仍给它的单射稠密性、所有有限放大不变限制上的稠密像和严格正的真实四次幂型。
这些性质不推出 $G_2=A T$ 的全空间有界因式分解。

后续 Euler 近单位证明应使用有限个真实快系数的联合幂界
$$
\left\|\prod_{\nu=1}^L E_\nu^{n_\nu}\right\|
\le C^n e^{-c n^4/L^3},\qquad \sum_\nu n_\nu=n,
$$
而不从完整快累积量提出有界 $A$ 因子。
对固定有限物理头提出一个 $A$ 仍合法，本命题没有否定该局部步骤。

来源：
- [R109](R109-invariant-restriction-exact-quartic-type.md)：(4.1)–(4.2) 的真实权及 dyadic 跳跃。
- [R270B](R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md)：(1.1)、(3.1) 的实际收敛展开与快类归属。
- [R151](R151-quartic-analytic-approximation-gauge-stability.md)：连续系数、gauge、快类真实幂型及强主理想结论。
