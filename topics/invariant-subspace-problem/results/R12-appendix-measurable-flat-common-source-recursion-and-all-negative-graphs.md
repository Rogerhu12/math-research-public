# 可测平坦源的真实递推、全部负幂费用及图范数返回

作者：AI-assisted GPT-6 Astra Pro；会话 `Astra-ISP-8542378f-20261127`。日期：2026-11-27（Asia/Taipei）。

**状态：已证明的正向中间结论。** 本稿在原 Haar 空间中给一个明确的非零可测源，构造普通范数统一有界的真实 Deddens 递推，使输出返回该源，并在每个固定原负幂图范数中返回。所有负幂费用及每一步 Deddens 成本均保留原权，且有明确增长上界。实际累计成本仍比已付的同源逆像预算多一个时间因子；本稿不把该差额算作已付，也不声称这些算子保持未知 $A$-不变空间。

## 1. 一个明确避开所有整数的正测集合

原模型仍为
$$
H=L^2(\mathbb Z_2,\mu),\qquad
(Af)(y)=w(y)f(y-1),\qquad w(y)=\alpha_{v_2(y)}\ (y\ne0),
$$
$w(0)=0$，$\alpha_j=e^{-L_j}$ 为原 [R9](R9-radial-odometer-and-nilpotent-approximants.md) 权。对每个普通整数 $z\in\mathbb Z$，定义
$$
q(z)=\left\lceil\log_2(|z|+2)\right\rceil,\qquad
d(z)=6+q(z)+2\left\lceil\log_2(q(z)+1)\right\rceil.
\tag{1.1}
$$
置
$$
\boxed{E=2\mathbb Z_2\setminus
\bigcup_{z\in\mathbb Z}\big(z+2^{d(z)}\mathbb Z_2\big),\qquad
f_0=\mathbf1_E.}
\tag{1.2}
$$
$E$ 是紧集，且没有任何普通整数。其测度严格为正：具有 $q(z)=q$ 的整数个数至多 $2^{q+1}$，所以全部删除集合的测度至多
$$
\sum_{q\ge1}2^{q+1}2^{-6-q}
2^{-2\lceil\log_2(q+1)\rceil}
\le\frac1{32}\sum_{q\ge1}\frac1{(q+1)^2}<\frac1{32}.
$$
从而
$$
\boxed{\mu(E)\ge\frac{15}{32},\qquad
\|f_0\|\ge\sqrt{15/32}.}
\tag{1.3}
$$
这些是有意保守的界，不需要各删除柱相互不交。

对整数 $T\ge0$，记
$$
Q(T)=\left\lceil\log_2(T+2)\right\rceil,\qquad
D(T)=6+Q(T)+2\left\lceil\log_2(Q(T)+1)\right\rceil.
\tag{1.4}
$$
若 $x\in E$、$b\in\mathbb Z$、$|b|\le T$，则 (1.2) 直接给
$$
v_2(x+b)<d(-b)\le D(T).
\tag{1.5}
$$
故原权 $w(x+b)$ 只依赖 $x$ 的前 $D(T)$ 位，并有正的统一下界。

## 2. 一个支付完整权乘积的界

写
$$
W_k(y)=\prod_{a=0}^{k-1}w(y-a),\quad
\beta_k=\|A^k\|,\quad S_k=-\log\beta_k.
$$
对长度为 $k$ 的任何连续整数区间，其中模 $2^l$ 为零的位置数在
$\lfloor k/2^l\rfloor$ 与 $\lfloor k/2^l\rfloor+1$ 之间。另一方面
$$
S_k=kL_0+\sum_{l\ge1}(L_l-L_{l-1})
\left\lfloor\frac{k}{2^l}\right\rfloor.
$$
因此，若该区间平移到某个 $x$ 后所有位置的 $v_2$ 都小于 $D$，且 $k<2^D$，则
$$
\boxed{\beta_k e^{-(L_{D-1}-L_0)}
\le\prod_{b\text{ 在该区间}}w(x+b)\le\beta_k.}
\tag{2.1}
$$
这里上下界都来自所有层的准确计数；没有只保留最深的一项而漏掉其余原乘积。

对 $x\in E$ 及 $0\le a<k$，用 (1.5) 取 $T=k-1$，即得
$$
\boxed{f_0\in\bigcap_{k\ge1}\operatorname{Ran}A^k,}
\tag{2.2}
$$
以及全部原负幂的显式界
$$
\frac{\|f_0\|}{\beta_k}
\le\|A^{-k}f_0\|
\le\frac{\|f_0\|}{\beta_k}
e^{L_{D(k-1)-1}-L_0}.
\tag{2.3}
$$
因为 $A^{-k}=U^{-k}M_{1/W_k}$ 在原值域上成立，这正是原 $L^2$ 范数，不是另设内积。

由
$$
2^{D(T)}\le512(T+2)(Q(T)+1)^2,
\tag{2.4}
$$
原 $L_j=O(16^j)$，以及原 $S_k=O(k^4)$，得到
$$
\boxed{\log\|A^{-k}f_0\|=O\big(k^4\log^8(k+2)\big).}
\tag{2.5}
$$
这个上界同时适用于全部整数 $k$，常数只由已经固定的原权及 (1.1) 确定。

## 3. 在固定非零球内返回的明确整数位移

只删除 (1.2) 中 $q(z)<4$ 的有限多个柱，得到一个 clopen 集 $E^{(4)}$；其指标函数只依赖低 $13$ 位。尾部删除的总测度至多
$$
\frac1{32}\sum_{q\ge4}\frac1{(q+1)^2}\le\frac1{128}.
$$
故对每个 $t\in2^{13}\mathbb Z_2$，
$$
\|U^t f_0-f_0\|
\le2\|\mathbf1_E-\mathbf1_{E^{(4)}}\|
\le\frac1{\sqrt{32}}<\frac12\|f_0\|.
\tag{3.1}
$$

对 $n\ge1$，明确取
$$
b_n=13+\left\lceil\log_2\log_2(n+4)\right\rceil,\qquad
S_n=n2^{b_n},\qquad S_0=0,
$$
$$
k_n=S_n-S_{n-1}-1.
\tag{3.2}
$$
$b_n$ 非递减并趋于无穷，$S_n$ 是严格递增的正偶整数，故 $k_n$ 为正奇整数。还满足
$$
S_n\in2^{13}\mathbb Z_2,\qquad
S_n\longrightarrow0\ \text{于 }\mathbb Z_2,\qquad
S_n\le2^{14}n\log_2(n+4).
\tag{3.3}
$$
定义同一初始源的实际输出
$$
\boxed{f_n=U^{S_n}f_0=\mathbf1_{E+S_n}.}
\tag{3.4}
$$
由 (3.1)，每个 $f_n$ 都属于固定非零球
$B(f_0,1/\sqrt{32})$，而 $\|f_n\|=\|f_0\|$。
又平移表示 $t\mapsto U^t$ 在 $L^2(\mathbb Z_2)$ 上强连续：先对柱函数验证，再用其稠密性和酉性。因此
$$
f_n\longrightarrow f_0\quad\text{于原 }L^2.
\tag{3.5}
$$

## 4. 逐步实际实现及准确成本式

令
$$
\boxed{R_n=\alpha_0^{-1}M_{\mathbf1_{E+S_n}}U^{k_n}.}
\tag{4.1}
$$
因 $E$ 为偶数集的子集，$E+S_n$ 也只含偶数。对输出 $y\in E+S_n$，$y-k_n$ 是奇数，原权在那里恰为 $\alpha_0$。从而
$$
\begin{aligned}
(R_nAf_{n-1})(y)
&=\alpha_0^{-1}\mathbf1_{E+S_n}(y)
w(y-k_n)f_{n-1}(y-k_n-1)\\
&=\mathbf1_{E+S_n}(y)=f_n(y).
\end{aligned}
$$
在输出集之外两侧均为零，故
$$
\boxed{R_nAf_{n-1}=f_n,\qquad\|R_n\|=\alpha_0^{-1}.}
\tag{4.2}
$$
这是真正的同源递推，不是对每一步重新挑选另一个 $f_0$。

[正向加权平移的准确 Deddens 分类](R12-appendix-deddens-algebra-localizing-and-uniform-cost-obstruction.md) 给
$$
c_A(R_n)=\frac{\beta_{k_n}}{\alpha_0}
\operatorname*{ess\,sup}_{x\in E}
\left(\prod_{b=S_{n-1}+2}^{S_n}w(x+b)\right)^{-1}.
\tag{4.3}
$$
区间长度恰为 $k_n$，全部 $b$ 的绝对值不超过 $S_n$。用 (1.5)、(2.1) 取 $D=D(S_n)$，得到
$$
\boxed{R_n\in\mathcal D_A,\qquad
\alpha_0^{-1}\le c_A(R_n)\le\alpha_{D(S_n)-1}^{-1}.}
\tag{4.4}
$$
所有成本均有限；正向位移及真实乘子使分类的必要条件与充分条件都适用。

式 (4.3) 还保留准确有限头表达。令
$$
\mathcal F_D(E)=\{a\in\{0,\ldots,2^D-1\}:
\mu(E\cap(a+2^D\mathbb Z_2))>0\}.
$$
在 $D=D(S_n)$ 时，原乘积在每个这样的柱上为常数，因而
$$
c_A(R_n)=\frac{\beta_{k_n}}{\alpha_0}
\max_{a\in\mathcal F_D(E)}
\prod_{b=S_{n-1}+2}^{S_n}\alpha_{v_2(a+b)}^{-1}.
\tag{4.5}
$$
集合 $\mathcal F_D(E)$ 保留的是实际 $E$ 的正测占用，不把所有模类任意替换成可用来源。若只需一个直接显式预算，(4.4) 不需要求这个占用集合。

由 (2.4)、(3.3) 得
$$
\log c_A(R_n)=O\big(n^4\log^{12}(n+2)\big),
$$
从而这条实际递推满足
$$
\boxed{\sum_{i=1}^n\log c_A(R_i)
=O\big(n^5\log^{12}(n+2)\big).}
\tag{4.6}
$$
这是可实现的上界，不宣称对这一目标族已求出最优累计成本。

## 5. 全部原负幂的实际费用及逐个图范数返回

$E+S_n$ 仍避开全部普通整数，因为 $S_n$ 是普通整数。更定量地，对 $y=x+S_n$、$x\in E$、$0\le a<k$，有
$|S_n-a|\le S_n+k$。由 (1.5)、(2.1)，
$$
\boxed{f_n\in\bigcap_{k\ge1}\operatorname{Ran}A^k,}
\tag{5.1}
$$
$$
\frac{\|f_0\|}{\beta_k}
\le\|A^{-k}f_n\|
\le\frac{\|f_0\|}{\beta_k}
e^{L_{D(S_n+k)-1}-L_0}.
\tag{5.2}
$$
也可以不估计：$\|A^{-k}f_n\|^2$ 恰为
$\int_E W_k(x+S_n)^{-2}\,d\mu(x)$，其被积函数在实际 $E$ 上只依赖前 $D(S_n+k)$ 位。这给对全部 $n,k$ 的原有限头加权平均。

现在固定 $k$。当 $n$ 足够大时，$b_n\ge D(k-1)$，所以 $S_n$ 是 $2^{D(k-1)}$ 的倍数。对 $x\in E$，原 $w(x-a)$ 的 $v_2$ 均小于 $D(k-1)$，于是
$$
W_k(x+S_n)=W_k(x).
$$
因此最终有准确的原值域身份
$$
\boxed{A^{-k}f_n=U^{S_n}A^{-k}f_0.}
\tag{5.3}
$$
用原平移强连续性，得到
$$
\boxed{\|A^{-k}(f_n-f_0)\|\longrightarrow0
\quad\text{对每个固定 }k\ge1.}
\tag{5.4}
$$
也就是说，输出在全部固定负幂的图范数中返回原源。没有将“每个固定 $k$”擅自换成 $k=n$ 的统一结论。

对真正随递推变化的 $k=n$，只能使用已付的 (5.2)；它给
$$
\boxed{\log\|A^{-n}f_n\|
=O\big(n^4\log^{12}(n+2)\big).}
\tag{5.5}
$$
这与实际累计成本 (4.6) 的五次上界不同，不能由 (5.4) 把缺少的时间因子消掉。

## 6. 已触达的接口及尚未支付的保持性

本稿给出了原可测平坦源、同一来源的精确逐步实现、全部负幂的真实预算，以及所有固定图范数的返回。它证明连续整数迹障碍可以通过真实可测目标避开，但也明确展示：很强的源返回性质本身并不等于低累计 Deddens 费用。

后续可在同一源和同一输出上比较其他实际运输实现与 (4.3)，或改变位移调度；不能只用 (5.5) 的标量逆像上界替换尚未构造的算子成本。尤其 $R_n$ 仍未被证明保持某个未知 $A$-不变闭子空间，$U^{S_n}$ 的实际输出也未被证明属于 $\overline{\{p(A)f_0\}}$。故本稿没有得到普通不变子空间，亦没有把另一种表示中的三角性转移回原 Hilbert 空间。
