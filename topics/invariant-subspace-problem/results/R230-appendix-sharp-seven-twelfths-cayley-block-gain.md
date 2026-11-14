# R230 附录：有限块 Cayley 算子在全 Walsh 向量上的准确幂指数：$7/12$

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065。

**状态：完整证明。** 对前稿的有限物理块 Cayley 算子，本稿证明全块 Walsh 向量的范数恰为 $Q^{7/12}$ 阶。此前所用 $c\sqrt Q$ 下界仍然正确，但不是该向量的最佳幂指数。结论来自一个正积分、准确比值和 $Q^{2/3}$ 宽窗口；不依赖数值证据。实际 carry 的传递仍使用前稿的有界扰动公式。

## 1. 对象与主结论

在 $Q$ 个物理位上置
$$
S_Q=\sum_{j=1}^QE_j,\qquad
K_Q=\frac{2S_Q}{Q+1},\qquad
F_Q=(I-K_Q)(I+K_Q)^{-1},
$$
其中 $E_j=e_{10}^{(j)}$。令 $\chi$ 为全 $Q$ 位 Walsh 积。

**定理。** 对所有整数 $Q\ge1$，
$$
\boxed{
e^{-66}Q^{7/12}\le\|F_Q\chi\|\le100Q^{7/12}.
}
\tag{1.1}
$$
常数只为完整明确预算，不声称最优。特别该范数同时有 $O(Q^{7/12})$ 上界和同阶下界。

## 2. Poisson 截断的准确表示

前有限块稿已经逐项证明：在占据数 $k$ 的点上，
$$
F_Q\chi=\chi(2I_k-1),\qquad
I_k=\int_0^\infty e^{-t}\left(1+\frac{2t}{Q+1}\right)^kdt\ge1.
\tag{2.1}
$$
记
$$
x=\frac{Q+1}{2},\qquad
p_k=2^{-Q}\binom Qk,\qquad
J_k=e^x x^{-k}k!.
$$
变量替换 $u=t+x$ 及整数阶不完全 Gamma 积分的有限分部积分给
$$
\begin{aligned}
I_k
&=e^x x^{-k}\int_x^\infty e^{-u}u^kdu\\
&=x^{-k}k!\sum_{r=0}^k\frac{x^r}{r!}
=J_k\,\Pi_k,
\end{aligned}
\tag{2.2}
$$
其中
$$
\Pi_k=e^{-x}\sum_{r=0}^k\frac{x^r}{r!}
=\mathbb P\{Z_x\le k\},
\qquad Z_x\sim\operatorname{Pois}(x).
$$
这里 Poisson 变量只是一组明确的非负系数；其均值与方差均为 $x$，可由指数级数逐项计算。

定义
$$
A_k=p_kJ_k^2.
$$
直接消去阶乘后得到关键的准确比值
$$
\boxed{
\frac{A_{k+1}}{A_k}
=\frac{4(k+1)(Q-k)}{(Q+1)^2}
=1-\frac{(2k-Q+1)^2}{(Q+1)^2}.
}
\tag{2.3}
$$
令 $k_0=\lfloor Q/2\rfloor$。分别代入偶数、奇数 $Q$，均得到
$$
\boxed{
A_{k_0}=\frac{e^{Q+1}Q!}{(Q+1)^Q}.
}
\tag{2.4}
$$

注意 $A_k$ 本身在整个区间并不是中心峰值分布；(2.3) 的比值至多为 $1$。在中心以下不能删去 Poisson 因子再求和。下面将中心以下与以上分别控制。

## 3. 所需阶乘估计的初等证明

对每个整数 $n\ge1$，
$$
\boxed{
e^{-1/4}\sqrt n\,(n/e)^n
\le n!
\le9\sqrt n\,(n/e)^n.
}
\tag{3.1}
$$

证明。用有限分部积分得
$n!=\int_0^\infty e^{-t}t^n\,dt$。令
$g(t)=-t+n\log t$，其最大值在 $t=n$。

在 $|s|\le\sqrt n/2$ 上，$|s/n|\le1/2$，且
$\log(1+u)\ge u-u^2$ 对 $|u|\le1/2$ 成立。因此
$$
g(n+s)-g(n)\ge-s^2/n\ge-1/4.
$$
这个区间的长度为 $\sqrt n$，给出 (3.1) 的下界。

在 $n/2\le t\le2n$ 上，$g''(t)=-n/t^2\le-1/(4n)$，故
$$
g(t)\le g(n)-(t-n)^2/(8n).
$$
中段积分至多
$\sqrt{8\pi n}\,e^{g(n)}$。在 $0<t\le n/2$ 上 $g'(t)\ge1$，其积分至多 $e^{g(n/2)}\le e^{g(n)}$；在 $t\ge2n$ 上 $g'(t)\le-1/2$，其积分至多
$2e^{g(2n)}\le2e^{g(n)}$。因为 $\sqrt{8\pi}+3<9$，得到上界。证毕。

将 (3.1) 代入 (2.4)，并用
$(Q/(Q+1))^Q\ge e^{-1}$，可得
$$
\boxed{
e^{-1/4}\sqrt Q\le A_{k_0}\le9e\sqrt Q.
}
\tag{3.2}
$$

## 4. 中心以上的三次衰减与总上界

令 $N=Q+1$。由 (2.3)，对 $\ell\ge1$，
$$
A_{k_0+\ell}
=A_{k_0}\prod_{s=0}^{\ell-1}(1-d_s),
\qquad
d_s=\frac{(2(k_0+s)-Q+1)^2}{N^2}.
$$
无论 $Q$ 奇偶，都有 $d_s\ge4s^2/N^2$。因此
$$
\boxed{
A_{k_0+\ell}
\le A_{k_0}
\exp\left(-\frac{4(\ell-1)^3}{3N^2}\right).
}
\tag{4.1}
$$
求和并以积分比较三次指数尾，可得
$$
\sum_{\ell=0}^{Q-k_0}A_{k_0+\ell}
\le5N^{2/3}A_{k_0}.
\tag{4.2}
$$
例如将首两项单独取出，再代换 $t=N^{2/3}u$；积分
$\int_0^\infty e^{-4u^3/3}du<2$ 即足够。

在中心以下，$I_k$ 随 $k$ 递增，所以
$$
I_k\le I_{k_0}\le J_{k_0}\le9e\sqrt Q
\qquad(0\le k\le k_0).
\tag{4.3}
$$
当 $k_0\ge1$ 时，最后一步由 (3.1)、$x-k_0\le1$ 和
$(k_0/x)^{k_0}\le1$ 得到；$Q=1$ 时也直接成立。

因为 $I_k\ge1$，有 $|2I_k-1|\le2I_k$。将两区分别相加，使用
$\Pi_k\le1$、(3.2)、(4.2)，得到
$$
\begin{aligned}
\|F_Q\chi\|^2
&=\sum_{k=0}^Qp_k(2I_k-1)^2\\
&\le4(9e)^2Q+4\sum_{k\ge k_0}A_k\\
&\le324e^2Q+
180e\sqrt Q\,(Q+1)^{2/3}\\
&\le10^4Q^{7/6}.
\end{aligned}
\tag{4.4}
$$
最后可用 $Q+1\le2Q$、$e<3$。这给出 (1.1) 的上界。

## 5. $Q^{2/3}$ 宽窗口给同阶下界

先设 $Q\ge4096$，置
$$
M=\lceil Q^{2/3}\rceil.
$$
考察
$$
k_0+M\le k<k_0+2M.
\tag{5.1}
$$
这些指标都不超过 $Q$。因为 $M\le(5/4)Q^{2/3}$，对 (2.3) 中
$0\le s<2M$，
$$
d_s\le\frac{4(s+1)^2}{(Q+1)^2}
\le25Q^{-2/3}<1/2.
$$
用 $\log(1-u)\ge-2u$（$0\le u\le1/2$），以及
$\sum_{s=1}^{\ell}s^2\le\ell^3$，得到对全部 $0\le\ell\le2M$
$$
\begin{aligned}
\log\frac{A_{k_0+\ell}}{A_{k_0}}
&\ge-2\sum_{s=0}^{\ell-1}d_s\\
&\ge-\frac{8\ell^3}{(Q+1)^2}\\
&\ge-128.
\end{aligned}
\tag{5.2}
$$
最后一个常数可由
$8(2M)^3/(Q+1)^2\le64(5/4)^3=125$ 直接核实。

对于 (5.1) 的 $k$，
$$
k-x\ge M-1\ge\tfrac12Q^{2/3}.
$$
由 Poisson 均值、方差及 Chebyshev 不等式，
$$
1-\Pi_k
=\mathbb P(Z_x>k)
\le\frac{x}{(k-x)^2}
\le4Q^{-1/3}\le1/4.
$$
特别 $\Pi_k\ge1/2$。因此 (5.1) 中的每一项满足
$$
p_kI_k^2=A_k\Pi_k^2
\ge\frac14e^{-128}A_{k_0}.
$$
该窗口有 $M\ge Q^{2/3}$ 项。又 $2I_k-1\ge I_k$，所以 (3.2) 给
$$
\|F_Q\chi\|^2
\ge\frac14e^{-128-1/4}Q^{7/6}
\ge e^{-132}Q^{7/6}.
\tag{5.3}
$$
这证明 $Q\ge4096$ 时的下界。

若 $1\le Q<4096$，则 $I_k\ge1$ 给 $\|F_Q\chi\|\ge1$，而
$e^{-66}Q^{7/12}\le e^{-66}4096^{7/12}
=128e^{-66}<1$。故同一常数覆盖全部 $Q$，定理证毕。

## 6. 实际 carry 和全局参数接口

前有限块稿的真实远块构造为
$$
K^{\rm act}
=\frac{2\sum_{j=r}^{r+Q-1}N_j}
{Q+1+2Q\varepsilon},
\qquad
\varepsilon\ge\max_{r\le j<r+Q}\eta_j.
$$
在 $4\varepsilon(Q+1)\le1/2$ 时，已证明
$$
\|F^{\rm act}-F_Q\otimes I\|
\le16(Q+1)^2\varepsilon.
\tag{6.1}
$$
因此本稿的下界准确传递为
$$
\boxed{
\|F^{\rm act}\chi_J\|
\ge e^{-66}Q^{7/12}-16(Q+1)^2\varepsilon.
}
\tag{6.2}
$$
真空范数和均值仍保持原来的 $O(Q^{-1/2})$、$O(Q^{-1})$ 估计；本稿没有改变它们。对
$R^{\rm act}=I+\lambda F^{\rm act}$，增生扩张性给
$\|R^{\rm act}\chi_J\|\ge\lambda\|F^{\rm act}\chi_J\|$。

这给已单独证明的自适应块无穷乘积构造一个参数替换。若
$$
Q_i\asymp i^a,\qquad \lambda_i=i^{-b},
$$
则真空漂移和方差分别有
$$
O(i^{-a-b}),\qquad O(i^{-a-2b}),
$$
而选中全块 Walsh 向量的单因子增益至少是
$$
c\,i^{7a/12-b}
$$
（实际扰动先取到比任意这些幂都小）。同时满足可和漂移、可和方差及正幂增益的一个范围为
$$
\boxed{
\frac{12}{19}<a<1,\qquad
1-a<b<\frac{7a}{12}.
}
\tag{6.3}
$$
第二个方差条件在此自动满足。

对远窗口 $n\le i\le2n$，其总 Walsh 次数
$q_n\asymp n^{1+a}$，因子增益的乘积为
$\exp(cn\log n)$。所以将 (6.3) 代入那个完整全局构造，得到可选的逆测试增长指数
$$
\beta=\frac1{1+a}\in\left(\frac12,\frac{19}{31}\right).
$$
这里的全局强收敛、循环锚及同一收缩强单位仍由该全局构造另行证明；不能只从本稿有限块估计推出。此参数接口也不提供完整次数空间的统一上界、慢符号分母或见证专属配对成功。

本稿直接接 [R230有限块构造](../results/R230-appendix-finite-block-cayley-vacuum-and-walsh-gain.md) 与 [自适应全局构造](../results/R230-appendix-cayley-block-strong-units-and-super-square-root-inverses.md)。并行 [R267 Blaschke线性下型](../results/R267-appendix-blaschke-block-strong-units-and-linear-degree-inverse-type.md) 已给更强的全局方向增长，本稿的新结论是这个特定有限 Cayley 块的双边锐幂阶及对应参数细化，不重报全局最强范围。
