# R271 附录：原连续尾完整相干列的 Bernoulli 池原像与精确小残量

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文在原无限连续权 $b_i=(i+1)^{-2}$ 上，直接为完整相干列 $(D^*)^k\Omega$ 构造一个 Hilbert 原像候选，保留其准确残量。候选的费用接近该完整列的标量必要下界，残量在 $k\le\kappa x$ 时指数小。随后使用原有的**全孔层**右逆给出准确修复预算；没有把 primitive 限制逆的多项式界用于一般残量。

具体新增范围是下述 (2.4)、(3.3) 及其完整高步版本 (6.3)。完整一阶 MP 在 $k=o(x)$ 的相干列上渐近达到标量下界。对任意固定正比例 $k/x$，本文保留 (4.2) 的实际修复项，没有证明它可由一个只依赖该比例的常数支付，也没有证明原返回或 $N=M$。

## 1. 原空间、完整列与一个必要下界

取整数 $x\ge1$。在以有限子集 $I\subset\{x,x+1,\ldots\}$ 为正交基的 Boolean Hilbert 空间中，记 $\mathcal H_k$ 为 $|I|=k$ 的层，并令
$$
D=D_x=\sum_{i\ge x}b_iE_i,\qquad
b_i=(i+1)^{-2},\qquad z_i=b_i^2,\qquad
S_y=\sum_{i\ge y}z_i.
\tag{1.1}
$$
由于 $\sum b_i<\infty$，$D$ 是完整直和空间上的有界算子。以下所有 $D^r$ 都是这个同一算子的真幂。

置
$$
\omega_k=(D^*)^k\Omega
=k!\sum_{|I|=k}b_Ie_I,\qquad
b_I=\prod_{i\in I}b_i,
$$
$$
\sigma_k^2=\|\omega_k\|^2=(k!)^2e_k(z),\qquad e_0=1.
\tag{1.2}
$$
$e_k(z)$ 是全部原无限权的第 $k$ 个基本对称和，有限且严格为正。

若 $Dy=\omega_k$，则
$$
\langle y,\omega_{k+1}\rangle
=\langle Dy,\omega_k\rangle=\sigma_k^2,
$$
所以
$$
\boxed{\|y\|\ge\ell_k,\qquad
\ell_k:=\frac{\sigma_k^2}{\sigma_{k+1}}.}
\tag{1.3}
$$
这是完整物理列的必要下界，不是把压缩逆当作完整逆。

## 2. 一个有限随机池给出的准确候选

固定
$$
t=z_x=(x+1)^{-4},\qquad p_i=z_i/t\in(0,1].
\tag{2.1}
$$
令 $\mathcal P$ 为独立 Bernoulli 子集，位 $i$ 的纳入概率为 $p_i$。因为 $\sum_i p_i=S_x/t<\infty$，$\mathcal P$ 几乎处处有限。$p_x=1$ 只表示最左位必入，不产生任何分母问题。

对有限 $J$ 令 $N_{J^c}=|\mathcal P\setminus J|$，并定义
$$
a_J=\mathbb E\frac1{1+N_{J^c}}
=\int_0^1\prod_{i\notin J}(1-p_i+p_is)\,ds.
\tag{2.2}
$$
乘积在 $[0,1]$ 上收敛；也可先取有限尾，再按有界收敛取极限。

在 $\mathcal H_{k+1}$ 中定义坐标
$$
(q_k)_J=\frac{k!}{t}b_Ja_J,\qquad |J|=k+1.
\tag{2.3}
$$
下一节将直接证明 $q_k\in\mathcal H_{k+1}$，所以这里没有预先假定一个随机向量的 Bochner 可积性。

**精确恒等式。** 有
$$
\boxed{
Dq_k=\omega_k-r_k,\qquad
(r_k)_I=k!b_I\prod_{i\notin I}(1-p_i),\quad |I|=k.
}
\tag{2.4}
$$

证明。固定 $|I|=k$，写 $N=N_{I^c}$。由独立性及非负项求和，
$$
\begin{aligned}
\sum_{i\notin I}p_i
\mathbb E\frac1{1+N_{(I\cup\{i\})^c}}
&=\mathbb E\left[
\sum_{i\notin I}
\frac{\mathbf1_{\{i\in\mathcal P\}}}{N}
\mathbf1_{\{N>0\}}\right]\\
&=\mathbb P(N>0).
\end{aligned}
$$
因此
$$
(Dq_k)_I
=\frac{k!}{t}b_I\sum_{i\notin I}z_i a_{I\cup\{i\}}
=k!b_I\left[1-\prod_{i\notin I}(1-p_i)\right],
$$
即 (2.4)。无限和可由 Tonelli 处理；证明 $q_k$ 有限范数后，该坐标等式就是有界 $D$ 的 Hilbert 等式。

特别，$r_k$ 不是被省去的 nuisance。因 $p_x=1$，它仅可能支撑在包含 $x$ 的集合上；一般不属于 $\ker D$。$k=0$ 时 $r_0=0$。

## 3. 真候选费用与残量费用

对 $|J|=k+1$，设
$$
\lambda_J=\sum_{i\notin J}p_i
\ge\frac{S_{x+k+1}}t.
$$
利用 $1-a\le e^{-a}$，
$$
a_J\le\int_0^1e^{-\lambda_J(1-s)}ds
\le\lambda_J^{-1}\le\frac{t}{S_{x+k+1}}.
$$
所以
$$
\boxed{
\|q_k\|
\le\frac{k!\sqrt{e_{k+1}(z)}}{S_{x+k+1}}.
}
\tag{3.1}
$$
这也完成了第 2 节所需的 Hilbert 收敛。

准确计数给
$$
(k+1)e_{k+1}
=\sum_{|I|=k}z_I\sum_{i\notin I}z_i
\le S_xe_k.
$$
结合 (1.3)、(3.1)，
$$
\boxed{
\frac{\|q_k\|}{\ell_k}
\le\frac{(k+1)e_{k+1}}{e_kS_{x+k+1}}
\le\frac{S_x}{S_{x+k+1}}.
}
\tag{3.2}
$$

另一方面，对 $|I|=k$，删去任意 $k$ 个位置后仍有
$$
\sum_{i\notin I}p_i\ge S_{x+k}/t.
$$
由 (2.4) 的逐坐标同号表达，
$$
\boxed{
\|r_k\|\le\varepsilon_{x,k}\sigma_k,\qquad
\varepsilon_{x,k}:=\exp(-S_{x+k}/t).
}
\tag{3.3}
$$
更准确地，
$$
\|r_k\|^2
=(k!)^2\sum_{|I|=k}z_I
\prod_{i\notin I}(1-p_i)^2.
\tag{3.4}
$$

原连续尾的积分界为
$$
\frac1{3(y+1)^3}\le S_y\le\frac1{3y^3}.
$$
故
$$
\frac{S_x}{S_{x+k+1}}
\le\left(\frac{x+k+2}{x}\right)^3,
\qquad
\frac{S_{x+k}}t
\ge\frac{(x+1)^4}{3(x+k+1)^3}.
\tag{3.5}
$$
若 $0\le k\le\kappa x$，则特别有
$$
\boxed{
\|q_k\|\le(\kappa+3)^3\ell_k,\qquad
\|r_k\|\le
\exp\left[-\frac{x}{3(1+\kappa)^3}\right]\sigma_k.
}
\tag{3.6}
$$
常数不含头维数、末端截断或最大位置；这是原无限连续尾同一列的预算。

## 4. 准确全层修复，以及目前未被免费消去的项

[R234 截平纯尾权附录](R234-appendix-flattened-tail-creation-and-critical-four-thirds-bound.md) §1 (1.5) 给出整个 $\mathcal H_k$ 上的有界右逆
$$
DQ_{x,k}=I_{\mathcal H_k},\qquad
\|Q_{x,k}\|\le12\,512^k(x+k+1)^{3/2}.
\tag{4.1}
$$
它不是 primitive 限制逆。于是
$$
y_k=q_k+Q_{x,k}r_k
$$
确实满足 $Dy_k=\omega_k$；完整层的 MP 也存在并满足 $\|D^\dagger\omega_k\|\le\|y_k\|$。

再由
$$
\frac{\sigma_{k+1}^2}{\sigma_k^2}
=(k+1)^2\frac{e_{k+1}}{e_k}
\le(k+1)S_x,
$$
得到完全明确的完整 MP 上界
$$
\boxed{
1\le\frac{\|D^\dagger\omega_k\|}{\ell_k}
\le
\frac{S_x}{S_{x+k+1}}
+
12\,512^k(x+k+1)^{3/2}
\sqrt{(k+1)S_x}\,
e^{-S_{x+k}/t}.
}
\tag{4.2}
$$
这里第一项没有次数指数；第二项保留原全层修复费用。不能把 $512^k$ 替为 primitive 一阶 Gram 的多项式费用。

一个无条件的增长高度推论是：对任意整数序列 $x\to\infty$、$k=k(x)=o(x)$，
$$
\boxed{
\frac{\|D_x^\dagger(D_x^*)^{k(x)}\Omega\|}
{\sigma_{k(x)}^2/\sigma_{k(x)+1}}
\longrightarrow1.
}
\tag{4.3}
$$
确实，(3.5) 给第一项趋于 $1$；第二项的对数至多
$$
k\log512+O(\log(k+2)+k/x)
-\frac{(x+1)^4}{3(x+k+1)^3}
=-\frac x3+o(x).
$$
下界来自 (1.3)。

对于固定但任意的正比例 $k/x$，(4.2) 本身未必给一致常数。本稿没有省略这一仍需解决的结构化修复问题。

## 5. 对同一 coherent forcing 残量的准确一阶接口

沿用[同实际测试的最小相干代表](R271-appendix-same-actual-test-minimal-coherent-representative-and-exact-residual.md)。若 $C^h=0$，则其真实残量按正交远孔层为
$$
[(C+D)f_{\rm coh}]_{j-1}
=\frac{(-C)^ja}{\sigma_j^2}\otimes\eta_j,\qquad
\eta_j=D\omega_j-\alpha_j\omega_{j-1},
\qquad
\alpha_j=\frac{\sigma_j^2}{\sigma_{j-1}^2}.
\tag{5.1}
$$
这里 $a=H_{\rm coh}^{-1}g$ 保持原完整逆。

因为 $\omega_j=D^*\omega_{j-1}\in(\ker D|_{\mathcal H_j})^\perp$，
$$
D^\dagger D\omega_j=\omega_j,
\qquad
D^\dagger\eta_j=\omega_j-\alpha_jD^\dagger\omega_{j-1}.
$$
任何真原像 $v=D^\dagger\omega_{j-1}$ 满足
$\langle\omega_j,v\rangle=\sigma_{j-1}^2$。因此
$$
\boxed{
\|D^\dagger\eta_j\|^2
=-\sigma_j^2+\alpha_j^2
\|D^\dagger\omega_{j-1}\|^2.
}
\tag{5.2}
$$
这是同一完整 MP 的精确相消，不先分别估两项。

记 (4.2) 右侧为 $A_{x,k}$。则
$$
\|D^\dagger\eta_j\|^2
\le(A_{x,j-1}^2-1)\sigma_j^2.
\tag{5.3}
$$
所以对任意 $J<h$，
$$
\boxed{
\left\|
(I\otimes D^\dagger)
P_{\mathrm{far}<J}(C+D)f_{\rm coh}
\right\|^2
\le
\left[\max_{0\le k<J}(A_{x,k}^2-1)\right]
\sum_{j=1}^{J}\frac{\|C^ja\|^2}{\sigma_j^2}.
}
\tag{5.4}
$$
输出的不同远孔层正交，故没有再付 $J$ 次 Cauchy。特别，若 $J=o(x)$，方括号趋零；这是一阶完整 $D^\dagger$ 对该同源低高度残量的真实小量。

(5.4) 不涵盖 $h\asymp x$ 的全部层，也不等于 $(C+D)^\dagger$ 或原 joined/source-return 的界。进一步的 $C$ 修正、核投影与两端 partial 仍须保留。

## 6. 同一随机池的任意有限步版本

这一节记录同构造的准确高步形式，不另换权或强头。给定整数 $r\ge1$，对 $|J|=k+r$ 设
$$
a_J^{(r)}
=\mathbb E\frac{N_{J^c}!}{(N_{J^c}+r)!}
=\frac1{(r-1)!}\int_0^1
\prod_{i\notin J}(1-p_i+p_is)(1-s)^{r-1}\,ds.
\tag{6.1}
$$
定义
$$
(q_{k,r})_J=\frac{k!}{t^r}b_J a_J^{(r)}.
\tag{6.2}
$$
则
$$
\boxed{
D^r q_{k,r}=\omega_k-r_{k,r},\qquad
(r_{k,r})_I=k!b_I\,\mathbb P(N_{I^c}<r).
}
\tag{6.3}
$$
证明只需固定 $I$ 并把 $r$ 次删除按无序新增集 $L$ 求和。条件于 $\mathcal P$，
$$
r!\sum_{\substack{L\subset\mathcal P\setminus I\\|L|=r}}
\frac1{(N_{I^c})_{\underline r}}
=\mathbf1_{\{N_{I^c}\ge r\}},
$$
独立性给出 (6.3)。所有项非负，Tonelli 合法。

令 $\lambda=S_{x+k+r}/t$。由 (6.1)，
$$
a_J^{(r)}
\le\frac1{(r-1)!}\int_0^\infty e^{-\lambda u}u^{r-1}du
=\lambda^{-r}.
$$
所以
$$
\boxed{
\|q_{k,r}\|
\le\frac{k!\sqrt{e_{k+r}}}{S_{x+k+r}^r},
\qquad
\frac{\|q_{k,r}\|}{\sigma_k^2/\sigma_{k+r}}
\le\left(\frac{S_x}{S_{x+k+r}}\right)^r.
}
\tag{6.4}
$$
最后一个比值的分母同样是任何 $D^r y=\omega_k$ 的必要下界，使用
$(D^*)^r\omega_k=\omega_{k+r}$。上界逐次使用
$(k+\ell)e_{k+\ell}\le S_xe_{k+\ell-1}$。

残量始终保准确的少位事件。一个可直接使用的界为
$$
\|r_{k,r}\|
\le\sigma_k\inf_{a>0}
\exp\left[
a(r-1)-(1-e^{-a})\,\frac{S_{x+k}}t
\right].
\tag{6.5}
$$
这是对整数事件 $N\le r-1$ 的 Chernoff 界。$r=1$ 取 $a\to\infty$ 即回到 (3.3)。当 $r$ 大于外池的有效位数时，(6.5) 可以接近 $1$；本文不把任意高步残量一律称为小量。

## 7. 尚未关闭的实际边界

本稿的随机池只是一种在原完整物理空间内构造向量的方法，未将原连续尾换成有限随机模型。所有等式都使用原 $D_x$，所有费用都在原 Hilbert 内积中。

已付的是：完整相干列的显式候选、准确结构化残量、明确全层修复界，以及 $k=o(x)$ 的完整 MP 渐近最优性和同源一阶残量小量。未付的是：$k\asymp x$ 全高度上的一致修复、原 $C+D$ 的完整返回、帽测试与全部 partial 的共同运输。特别，不从指数小 $r_k$ 和一个仍随 $k$ 指数增长的完整右逆，免费推出原 $N=M$。
