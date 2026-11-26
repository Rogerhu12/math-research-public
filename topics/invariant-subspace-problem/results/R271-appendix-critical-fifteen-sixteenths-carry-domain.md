# 真实 carry 的临界十五十六分之权与一十六分之除法域

日期：2026-11-27（Asia/Taipei）；2026-11-26（UTC）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下真实来源范数、临界端点、图核心及无条件延拓的临界性已证明；未证明 $W$ 的规范原像满足此来源条件。**

本文接[规范来源 carry 范数稿](../results/R271-appendix-canonical-source-carry-norm-total-hole-core.md)。使用其中已付的原 N/Y 两型 $T$、纯创建 $D^*=\sum_i(i+1)^{-2}E_i^*$、$K=T^*-D^*$ 及首缺位投影 $P_q$；每个 $P_q$ 保留全部高物理孔。总孔投影仍记 $\mathsf P_p$，不能与 $P_q$ 交换名称。

## 1. 含第零项的精确临界权

真实权的完整归一化是
$$
L_q:=-\log\alpha_q
=\frac{280}{3}16^q-90\,8^q+300\,2^q-\frac{850}{3},
\qquad \alpha_0=e^{-20}.
\tag{1.1}
$$
又
$$
\eta_q=\frac{\alpha_{q+1}}{\alpha_q},\qquad
-\log\eta_q=1400\,16^q-630\,8^q+300\,2^q,
\qquad \eta_0=e^{-1070}.
\tag{1.2}
$$
沿用 carry 权
$$
b_0=\eta_0,\qquad
b_q=q^{-2}\eta_{q-1}\quad(q\ge1).
\tag{1.3}
$$
置 $\sigma_*=15/16$。对每个 $q\ge1$，直接代入 (1.1) 得到**准确**等式
$$
\boxed{
\frac{b_q}{\alpha_q^{15/16}}
=q^{-2}\exp\left(
-\frac{45}{8}8^q+\frac{525}{4}2^q-\frac{2125}{8}
\right).}
\tag{1.4}
$$
确实，其对数是 $-2\log q+L_{q-1}-L_q/16$，$16^q$ 项完全消去。第零项另外准确为
$$
\boxed{\frac{b_0}{\alpha_0^{15/16}}=e^{-4205/4}.}
\tag{1.5}
$$
不能将 (1.4) 的 $q^{-2}$ 公式套到 $q=0$。

记 (1.4) 指数中的括号为 $E_q$，则
$$
E_1=-\frac{385}{8},\qquad
E_{q+1}-E_q
=-\frac{105}{8}2^q(3\cdot4^q-10)
\le-\frac{105}{2}\quad(q\ge1).
$$
因此
$$
C_*^2:=\sum_{q\ge0}\left(\frac{b_q}{\alpha_q^{15/16}}\right)^2
\le e^{-4205/2}+rac{e^{-385/4}}{1-e^{-105}}
<2e^{-385/4},
\tag{1.6}
$$
且
$$
\sup_{q\ge0}\frac{b_q}{\alpha_q^{15/16}}=e^{-385/8}.
\tag{1.7}
$$

## 2. 实际 carry 在临界 Hilbert 来源空间有界

定义
$$
\mathcal X_\sigma=
\left\{h:\ P_qh\in\mathcal H\ (q\ge0),\quad
\|h\|_\sigma^2:=\sum_{q\ge0}\alpha_q^{2\sigma}\|P_qh\|^2<\infty\right\}.
\tag{2.1}
$$
这是首缺位块的加权 Hilbert 空间，未对高尾总孔数作截断。

前稿的实际 N 型正交列给
$$
\|K_Nh\|\le\sqrt2
\left(\sum_q\rho_q^2\|P_qh\|^2\right)^{1/2},
\quad \rho_q\le3b_q\ (q\ge1),\quad \rho_0\le b_0/3.
$$
前稿保全部 Cayley 逆的估计给
$$
\|K_Yh\|\le10\sum_qb_q\|P_qh\|.
$$
由 (1.6)–(1.7) 和 Cauchy–Schwarz，两者都在 $\mathcal X_{15/16}$ 上有真实有界延拓，而且
$$
\boxed{
\begin{aligned}
\|K_Nh\|&\le3\sqrt2e^{-385/8}\|h\|_{15/16},\\
\|K_Yh\|&\le10C_*\|h\|_{15/16}
<10\sqrt2e^{-385/8}\|h\|_{15/16}.
\end{aligned}}
\tag{2.2}
$$
这些是原算子的范数，不把所有 carry 换成抽象小扰动。尤其 Y 型使用可和比值 (1.6)，不将其重叠的列改成 N 型的正交列。

## 3. 总孔截断的直接来源域证明

这里给前稿依赖的一项简化。只要 $h\in\mathcal X_{15/16}$，每个 $P_qh\in\mathcal H$。而首缺位为 $q$ 意味着至少已有 $q$ 个孔，所以
$$
\boxed{\mathsf P_{\le p}h
=\sum_{q=0}^{p}\mathsf P_{\le p}P_qh\in\mathcal H.}
\tag{3.1}
$$
这是有限个真实 Hilbert 块之和；无需另从 R238 推断。R238 的固定总孔结论仍正确，前稿对它的调用也没有改变结论，但此处的加权来源条件已经直接支付了 (3.1)。

若 $f=T^*h\in\mathcal H$ 按逐行形式成立，置 $h_p=\mathsf P_{\le p}h$。因两组投影交换，支配收敛给 $h_p\to h$ 于 $\mathcal X_{15/16}$，所以 (2.2) 给 $Kh_p\to Kh$ 于 $\mathcal H$。每个整数输出行只用有限输入坐标，故 $D^*h=f-Kh\in\mathcal H$ 是准确的形式等式。纯创建的真实总孔次数关系给
$$
D^*h_p=\mathsf P_{\le p+1}D^*h\longrightarrow D^*h.
$$
于是
$$
\boxed{T^*h_p\longrightarrow f\quad\text{于 }\mathcal H.}
\tag{3.2}
$$
此外
$$
\|Sh\|^2=\sum_q\alpha_q^2\|P_qh\|^2
\le\alpha_0^{1/8}\|h\|_{15/16}^2,
$$
故 $S:\mathcal X_{15/16}\to\mathcal H$ 有界，范数至多 $\alpha_0^{1/16}=e^{-5/4}$，并且
$$
\boxed{Sh_p\longrightarrow Sh.}
\tag{3.3}
$$

也可将此写成闭算子陈述：在 $\mathcal X_{15/16}\to\mathcal H$ 中取纯 $D^*$ 的最大逐行域。它是闭算子，(3.1) 及准确升次数关系证明 $\mathcal H$ 是其图核心。由有界扰动 (2.2)，原 $T^*$ 的最大逐行域具有同一图核心。这里“$\mathcal H$ 是图核心”指来源空间 $\mathcal X_{15/16}$ 中的 Hilbert 输入子空间，不声称整个形式序列空间中的图核心。

## 4. y=Sh 的真实逆权等价式及同 W 用法

令 $P_q^+$ 是输出整数满足 $n\ge1$、$v_2(n)=q$ 的正交投影。它是 $SP_q\mathcal H$ 的输出块，不是 $P_q$ 本身。对形式 $y=Sh$，准确有
$$
\|P_q^+y\|=\alpha_q\|P_qh\|,
$$
因此
$$
\boxed{
\sum_q\alpha_q^{15/8}\|P_qh\|^2
=\sum_q\alpha_q^{-1/8}\|P_q^+y\|^2.}
\tag{4.1}
$$
包含 $q=0$：该块的权分别是 $e^{-75/2}$ 和 $e^{5/2}$，乘入 $\|P_0^+y\|^2=e^{-40}\|P_0h\|^2$ 后相等。若右侧有限，则 $y\in\mathcal H$ 自动成立；没有先行假设它在原 Hilbert 域。

对原
$$
W=\ker T\ominus\overline{B\ker T},
$$
已知 $w_0=0$，故存在唯一规范形式 $h(w)$，$T^*h(w)=w$。如果其**同一来源**满足 (4.1) 的任意一侧有限，则 (3.2) 给 $w\in\overline{\operatorname{Ran}T^*}$，从而 $w=0$。

若已把 $y(w)=Sh(w)$ 作为形式源书写，那么所需额外费用准确是 $\alpha_q^{-1/16}$ 乘输出块后的平方和；仅有 $y(w)\in\mathcal H$ 尚未支付它。也未由 $w\in W$ 自动证明 $y(w)\in\mathcal H$。两种限制都保留。

## 5. 临界指数只对无条件 carry 延拓而言确切

对任意 $\sigma>15/16$，两个实际 $K_N,K_Y$ 都不能有界延拓 $\mathcal X_\sigma\to\mathcal H$。

取 $x_q=e_{2^q-1}$（$q\ge1$），则 $\|x_q\|_\sigma=\alpha_q^\sigma$。N 型中，输出整数 $2^q-1+2^{q-1}$ 的系数准确为 $b_q$，因为只有 $i=q-1$ 项到达该整数，而纯创建不能把已占据的第 $q-1$ 位重置成真空。因此 $\|K_Nx_q\|\ge b_q$。

Y 型该输出系数为
$$
\eta_{q-1}\left(a_{q-1}-\sum_{i<q-1}a_i\frac{d_{q-1}}{d_i^{2^{q-1-i}}}\right).
\tag{5.1}
$$
这是原 Cayley 展开的全部可能贡献：$i=q-1$ 是一次项；所有 $i<q-1$ 的幂数都是偶数，故符号为负。由 $d_{j+1}=\eta_jd_j^2$，括号内各比值至多 $\eta_{q-2}$，所以减去的总量不超过 $2\eta_{q-2}\le a_{q-1}/2$（$q\ge2$）。最后不等式由 $\eta_0<1/16$、$\eta_{j+1}\le\eta_j/4$ 及 $q^2\le4^{q-1}$ 给出。$q=1$ 无相减项。因此
$$
\|K_Yx_q\|\ge\frac12b_q\quad(q\ge1).
$$
由 (1.4)，
$$
\log\frac{b_q}{\alpha_q^\sigma}
=\left(\sigma-\frac{15}{16}\right)L_q
-2\log q-\frac{45}{8}8^q+\frac{525}{4}2^q-\frac{2125}{8}
\longrightarrow+\infty.
$$
故上述测试的输出／输入范数比无界，证明所称临界性。

这只排除更大来源空间上**无条件的 carry 有界延拓**；它不排除利用 $T^*h\in\mathcal H$、$w\in W$ 或其他同源关系得到更强的条件图核心，更没有构造非零 $W$。真正需要继续证明的仍是原 $W$ 对规范来源的额外费用。
