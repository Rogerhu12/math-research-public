# 真实源逼近与相位尾测试的两个误差：不能免费交换的对角极限

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：已核的接口与失败路线记录。** root 全文核验276行，并补足§3对全部子序列的连续凸成本反例。 本文不主张不存在别的参数分离或见证专属估计。它只说明：将目前已证的低放大 $S$ 逼近成本有限性，与 R235 的相位尾 carry 误差直接拼接，不能仅用一个不带速率的对角选择完成证明。下面把共用参数和准确误差逐项写出。

## 1. 两个已证输入

固定最小正秩见证
$$
x=(x_1,\ldots,x_r),\qquad x_i=Cf_i,\qquad
\tau=\sum_i\|x_i\|^2>0,
$$
以及实际交换代数 $\mathfrak C=A'$。原正泛函满足
$$
\phi(SF)=0\quad(F\in\mathfrak C),\qquad
\phi(F)=\sum_j\langle Fx_j,x_j\rangle.
$$

[近源预算主文](../results/R230-appendix-bounded-near-relations-and-quantitative-changing-source-compression.md)
给出实际删除成本
$$
\mathcal C_i(\varepsilon)=
\inf\{1+\|SF\|:F\in\mathfrak C,\
\|(I-SF)E_i x\|\le\varepsilon\}<\infty
\quad(\varepsilon>0).
\tag{1.1}
$$
这里 $E_i$ 删除第 $i$ 行。没有已证的一般上界来控制
$\varepsilon\downarrow0$ 时的 $\mathcal C_i$。

[R235 全右测试附录](../results/R235-appendix-annihilator-tail-coupling-energy-and-right-tests.md)
使用
$$
q=2^m,\qquad
P_m=I_{<m}\otimes Q_m\in S\mathcal A,\qquad
T_m=I_{<m}\otimes D_m^q,\qquad
h_m=\langle T_m1,1\rangle>0,
$$
$$
\|P_m-T_m\|\le e_m,\qquad
\epsilon_m=\frac{e_m}{h_m}
\le
\exp\!\left[-\frac{770}{16}q^4+O(q\log q)\right].
\tag{1.2}
$$
对任意真实 $G\in\mathfrak C$，
$$
\left|\frac{\phi(T_mG)}{h_m}\right|
\le\tau\epsilon_m\|G\|.
\tag{1.3}
$$
纯 $T_m$ 不被当成 $\mathfrak C$ 的元素；它只通过 (1.2) 进入。

记
$$
K_m=\frac{\|T_m\|}{h_m}.
\tag{1.4}
$$
[逐位熵偏转定理](../results/R230-appendix-entropy-tilts-and-growing-period-multivariate-filters.md)
的标量幂结论给
$$
K_m\ge
\exp\!\left(\frac{\pi}{16}q-\frac{m+1}{2}\right).
\tag{1.5}
$$
这里 (1.5) 是放大倍数的下界，不是控制误差的上界。它说明这些测试的通常算子范数代价确实发散。

## 2. 删除方向替换的准确范数预算

选一个满足 (1.1) 约束的真实
$$
T=SF\in\mathfrak C,\qquad
d_j=(I-T)x_j,\qquad
\left(\sum_{j\ne i}\|d_j\|^2\right)^{1/2}\le\varepsilon.
$$

对任意 $B\in B(H)$，Cauchy--Schwarz 给
$$
\left|
\sum_{j\ne i}\langle Bx_j,x_j\rangle
-\sum_{j\ne i}\langle BTx_j,x_j\rangle
\right|
\le
\|B\|\varepsilon
\left(\sum_{j\ne i}\|x_j\|^2\right)^{1/2}
\le\sqrt\tau\,\|B\|\varepsilon.
\tag{2.1}
$$
取 $B=T_m/h_m$，得到
$$
\boxed{
\left|
\frac1{h_m}\sum_{j\ne i}
\bigl(\langle T_mx_j,x_j\rangle
-\langle T_mTx_j,x_j\rangle\bigr)
\right|
\le\sqrt\tau\,K_m\varepsilon.
}
\tag{2.2}
$$

另一方面，$T$ 是可用于 (1.3) 的真实右因子。故
$$
\boxed{
\left|\frac{\phi(T_mT)}{h_m}\right|
\le\tau\epsilon_m\|T\|.
}
\tag{2.3}
$$
选取任意接近下确界的 $T$ 时，右边可控制为
$\tau\epsilon_m\mathcal C_i(\varepsilon)$ 加任意小余量。
注意这里使用的是 $G=T=SF$，所以确实支付 (1.1) 所控制的
$\|SF\|$。若另一构造使用 $G=F$，则须另付 $\|F\|$；
不能用 $\mathcal C_i$ 替代。

因此，仅用 (2.2)--(2.3) 消去这两个误差，所需的充分预算是
$$
\boxed{
K_m\varepsilon(m)\longrightarrow0,\qquad
\epsilon_m\mathcal C_i(\varepsilon(m))\longrightarrow0.
}
\tag{2.4}
$$
这两项趋零本身也还不是主问题的证明；仍须有一个已建立的非零目标配对。本文只讨论支付这两个误差的步骤。

先固定 $\varepsilon$ 及一个 $T$，再令 $m\to\infty$，可以支付 (2.3)，却不能从 (2.2) 得到趋零。
先固定 $m$，再令 $\varepsilon\downarrow0$，可以支付 (2.2)，却没有现成上界支付 (2.3)。
这里说的是**这两个已证上界不足以完成极限**，不是断言实际误差一定达到这些上界。

## 3. 单独的逐点有限性不蕴含任何联合对角子列

以下初等构造使量词缺口明确，而不把它当成实际见证成本的实现。

设 $K_n\to\infty$、$a_n>0$ 是任意指定正数序列。定义
$$
\boxed{
C_*(t)=1+t^{-1}
+\sum_{n=1}^{\infty}2a_n^{-1}(1-K_nt)_+,
\qquad t>0.
}
\tag{3.1}
$$
这里 $(s)_+=\max(s,0)$。因为 $K_n\to\infty$，对任意
$t_0>0$，在邻域 $t\ge t_0/2$ 上只有有限项非零。
所以该级数局部有限，$C_*(t)$ 对每个 $t>0$ 有限且连续。
每个加项都凸且随 $t$ 不增，故 $C_*$ 也凸、随 $t$ 不增，
并且 $C_*(t)\ge t^{-1}$。

对任意 $n$ 及任意 $t>0$，若 $K_nt>1/2$，
则第一项 $K_nt$ 已大于 $1/2$。
若 $K_nt\le1/2$，则
$$
a_nC_*(t)
\ge2(1-K_nt)\ge1.
$$
因此对**所有** $n$ 都有
$$
\boxed{
\inf_{t>0}\bigl(K_nt+a_nC_*(t)\bigr)\ge\frac12.
}
\tag{3.2}
$$
这个结论连另取子序列的可能性也排除了。

所以“每个 $t>0$ 时成本有限”，甚至再加连续性、凸性、
单调性和 $C_*(t)\ge t^{-1}$，
都不能逻辑地推出一个同时支付 (2.4) 的对角序列或子列。
本构造不是声称 (3.1) 是本题某个 $\mathcal C_i$，
更不是构造一个慢理想湮灭者；它只排除从**上述数值信息本身**
抽取所需对角序列的推理。

准确的待估计量可以写成
$$
\mathfrak E_{i,m}
=\inf_{\varepsilon>0}
\bigl(K_m\varepsilon+
\epsilon_m\mathcal C_i(\varepsilon)\bigr).
\tag{3.3}
$$
证明 $\mathfrak E_{i,m}\to0$、证明某个趋零子列，
或以真正源配对替代 (2.2) 而降低其代价，
都是尚需新信息的步骤。

## 4. 当前相位构造没有免费的第二个尾参数

[R253](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)
在实际空间使用
$$
P_m=\prod_{\zeta^{2^m}=1}\gamma_\zeta(S),\qquad
\gamma_\zeta(A)=\zeta A.
\tag{4.1}
$$
$2^m$ 阶相位固定点代数准确是
$$
\overline{\mathbb C[I,A^{2^m}]}
=I_{<m}\otimes\mathcal B_m.
\tag{4.2}
$$
所以消去前 $m$ 位时，同一构造有 $q=2^m$ 个因子。
纯有限头消元把这 $q$ 个因子准确变成 $D_m^q$，
而其 carry 估计以
$e^{-770\,16^{m-1}}=e^{-(770/16)q^4}$ 支付。

把这个构造的尾起点从 $m$ 改成 $M$，
得到的是 $P_M$、$D_M^{2^M}$ 和新的 $K_M$。
并没有保持旧的 $q$、旧的纯尾测试或旧的源重构预算。
此外，保持已选 $P_m$ 不变而只改比较算子，也不会使已存在的
$\|P_m-T_m\|$ 自动变小。

这不排除别的实际两参数构造。若能证明对每个固定复杂度 $n$，
存在额外物理参数 $M$，使源预算 $L_n$ 或目标配对预算不随 $M$ 增长，
而实际误差随 $M\to\infty$ 消失，那么可以先固定
$\mathcal C_i(c(1+L_n)^{-r})<\infty$，再选择足够大的 $M$。
当前 R253/R235 公式本身尚不提供这样的族。

[R267 的共同全部 $A$ 幂强单位](../results/R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)
是另一种实际构造，但其非零平坦算子不属于 UHF。
不能把 $\mathcal A$ 内的忠实形式首阶演算自动用于它，
也不能从全部 $A^k$ 整除推出慢 $S$ 整除。
该稿已经准确保留了这两个范围。

## 5. 一个更贴近真实源的缺行代价

设 $T_n\in S\mathfrak C$，且
$$
\varepsilon_n=\|(I-T_n)E_i x\|\longrightarrow0.
$$
由湮灭式及交换性，对任意 $F\in\mathfrak C$，
$$
\phi(F)
=\sum_j\langle F(I-T_n)x_j,x_j\rangle.
\tag{5.1}
$$
因此若 $h_{i,n}=(I-T_n)x_i$，
$$
\left|\phi(F)-\langle Fh_{i,n},x_i\rangle\right|
\le\sqrt\tau\,\varepsilon_n\|F\|.
\tag{5.2}
$$
若 $h_{i,n}$ 有有界子列，在 $H$ 中取弱极限，
(5.2) 就把同一个 $\phi$ 写成一个一般秩一向量配对，
矛盾于最小一般分离秩 $r\ge2$。所以
$$
\boxed{\|(I-T_n)x_i\|\longrightarrow\infty.}
\tag{5.3}
$$

这也直接对应
[R244 聚合转置代价主文](../results/R244-appendix-aggregate-transpose-source-budget-and-exact-dual-cost.md)
的准确对偶成本。按该文的双线性约定，固定源取
$g=Cx_i$，因为
$B(Fh,Cx_i)=\langle Fh,x_i\rangle$。
于是
$$
\|(I-T_n)x_i\|
\ge c_{(Cx_i),\phi}(\sqrt\tau\,\varepsilon_n),
$$
$$
\boxed{
\mathcal C_i(\varepsilon)
\ge\frac{c_{(Cx_i),\phi}(\sqrt\tau\,\varepsilon)}{\|x_i\|}.
}
\tag{5.4}
$$
$x_i\ne0$ 由最小秩保证。最后一步使用
$\|(I-T)x_i\|\le(1+\|T\|)\|x_i\|$，再取下确界。

(5.3)--(5.4) 是既有聚合对偶的直接应用，不另计独立的新机制。
它说明可能的专属构造也必须控制一个真实缺行向量，
不能仅在全空间算子范数与实际源范数之间省略代价。

目前没有从真实湮灭矩推出 (3.3) 趋零、任何一般 $\mathcal C_i$ 上界，
或任何原正常见证的矛盾。下一步应寻找上述额外两参数族，
或直接估计 (5.1) 中的实际聚合向量及其加权尾配对。
