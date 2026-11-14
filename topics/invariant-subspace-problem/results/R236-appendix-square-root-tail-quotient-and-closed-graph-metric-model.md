# R236 附录：小平方尾商与真实闭图表示的度量成本模型

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的范围模型。** 这是一个具体 Hilbert 空间模型，不是原 Haar $S_N$ 的商距离下界或反例。它保留非零小的 $t$、$N^2=t$、$G$ 属于真实尾生成代数、闭主理想和正常的忠实半不变表示，显示这些性质仍不能保证等距或给出统一商范数。原全部 dyadic 形式系数、实际权列及尾弱单位没有在模型中出现。

## 1. Volterra 的平方仍生成同一范数代数

在 $H_0=L^2(0,1)$ 上令
$$
(Vf)(x)=\int_0^x f(y)\,dy.
$$
对 $r\ge1$，
$$
(V^rf)(x)=\int_0^x\frac{(x-y)^{r-1}}{(r-1)!}f(y)\,dy,
\qquad \|V^r\|\le\frac1{r!}.
\tag{1.1}
$$
最后一个界来自将 $f$ 零延拓后使用卷积核的 $L^1(0,1)$ 范数。
所以 $V$ 拟幂零。其核为零，其伴随的核也为零，分别由不定积分的导数给出；
因此 $V$ 单射且像稠密。核 $1_{0<y<x<1}$ 平方可积，所以 $V$ 紧。

准确有
$$
\boxed{\overline{\mathbb C[I,V^2]}^{\|\cdot\|}
=\overline{\mathbb C[I,V]}^{\|\cdot\|}.}
\tag{1.2}
$$
只须从偶次幂逼近 $V$。给定 $\epsilon>0$，令
$k_\epsilon(s)=\min(s/\epsilon,1)$，$0\le s\le1$。
则 $\|1-k_\epsilon\|_1\le\epsilon/2$，且
$k_\epsilon(s)=s f_\epsilon(s^2)$，其中
$$
f_\epsilon(u)=
\begin{cases}\epsilon^{-1},&0\le u\le\epsilon^2,\\
u^{-1/2},&\epsilon^2\le u\le1
\end{cases}
$$
是连续函数。用多项式 $p(u)$ 在 $[0,1]$ 一致逼近它，误差可任意小。
例如 Bernstein 多项式的一致逼近由连续函数的一致连续性和二项分布方差趋零直接证明。
那么奇多项式卷积核 $s p(s^2)$ 在 $L^1$ 中逼近常数核 $1$。
每个 $s^{2l+1}$ 核对应 $(2l+1)!V^{2l+2}$，
故所得算子是 $V^2$ 的多项式，并按算子范数趋 $V$。这证明 (1.2)。

这个模型特别提醒：在一般拟幂零范数代数中，“$G$ 属于 $G^2$ 生成的闭代数”并不迫 $G=0$。
原 Haar 代数中的连续形式首项不能被省略或自动传给任意商。

## 2. 范数任意大而平方任意小的实际尾元素

固定 $0<\eta<1$，取 $K\ge1$。
令 $D_K$ 是正乘法算子，乘子在 $[0,1/2)$ 为 $1$，在 $[1/2,1]$ 为 $K$。
则 $\|D_K\|=K$、$\|D_K^{-1}\|=1$。
置
$$
\varepsilon_K=\sqrt{\eta/K},\qquad
G=-\varepsilon_KD_KVD_K^{-1},
\qquad t=G^2,\qquad T=t/\eta.
\tag{2.1}
$$
$G,T$ 都是非零、紧、单射、像稠密、拟幂零的有界算子，且 $-G$ 保持函数非负锥。
由 (1.1)，
$$
\|t\|\le\varepsilon_K^2K\|V^2\|\le\eta/2<\eta.
\tag{2.2}
$$
取单位向量 $f=\sqrt2\,1_{[0,1/2]}$。
在后半区间，$D_KVD_K^{-1}f=K/\sqrt2$，故
$$
\boxed{\|G\|\ge\frac{\sqrt{\eta K}}2.}
\tag{2.3}
$$
因此固定 $\eta$ 时，$\|G\|$ 可以任意大而 $\|G^2\|\le\eta$。
更强的是，由 (1.2) 及相似、非零缩放，
$$
\boxed{G\in\overline{\mathbb C[I,T]}^{\|\cdot\|}.}
\tag{2.4}
$$
所以这不是把一个任意不相关的平方根塞到尾代数之外。

## 3. 完整的一步实际代数与闭尾交

在 $H=\mathbb C^2\otimes H_0$ 上定义
$$
N=\begin{pmatrix}0&t\\I&0\end{pmatrix},\qquad
S=N+I_2\otimes G.
\tag{3.1}
$$
则 $N^2=I_2\otimes t$、$\|N\|=1$。
$N$ 单射、像稠密、拟幂零而非紧。
由于 (2.4)，$I_2\otimes G$ 属于 $N$ 的范数生成代数，所以 $S$ 也是其中的真实元素。

记 $\mathcal C=\{T\}'$。
因 $G$ 属于 $T$ 的范数代数，它与每个 $b\in\mathcal C$ 交换。
直接解 $RN=NR$ 得
$$
\{N\}'=
\left\{
\begin{pmatrix}a&tc\\c&a\end{pmatrix}:a,c\in\mathcal C
\right\}
=\mathcal C\oplus N\mathcal C.
\tag{3.2}
$$
不需要为这个计算预先声称 $\mathcal C$ 交换。

这里 $G^2=t$ 准确成立，所以一次尾交的生成元
$h=G^2-t$ 等于零。
对 $a,c\in\mathcal C$，
$$
S(a+Nc)=S(a+Gc).
$$
因此完整主理想准确为
$$
\mathcal I=S\{N\}'=S\mathcal C.
\tag{3.3}
$$
它是范数闭的：$Sb$ 的左下块就是 $b$，从而 $\|Sb\|\ge\|b\|$。
并且
$$
\boxed{\mathcal I\cap(I_2\otimes\mathcal C)=\{0\}.}
\tag{3.4}
$$
因为 $Sb$ 若为相同的两个对角块，其左下块迫 $b=0$。
于是完整下一尾商距离恰为
$$
\boxed{\operatorname{dist}(G,\mathcal I\cap\mathcal C)=\|G\|,}
\tag{3.5}
$$
它随 $K$ 任意大。

自然包含
$\mathcal C\to\{N\}'/\mathcal I$
是忠实、含单位、契约的代数映射。
然而在当前商中 $G=-N$，故 $G$ 的像范数不超过一。
所以这个包含的逆在其像上的范数至少是 $\|G\|$。
一步有限头、实际小 $t$ 和完整尾交本身都不能给统一的反向等距常数。

## 4. 真实半不变 Hilbert 空间上的忠实正常表示仍会缩范数

具体闭不变空间为
$$
M=\ker S=\{(-Gf,f):f\in H_0\}.
\tag{4.1}
$$
它非零、真闭，且对整个 $\{N\}'$ 不变。
任何单位向量 $h\in M$ 都给真实秩一正常正见证
$\rho=|h\rangle\langle h|$，湮灭 $S\{N\}'$。

对尾系数的限制表示
$$
\pi(b)=(I_2\otimes b)|_M
$$
是忠实、含单位、完全契约且正常的表示。
忠实性来自第二坐标：若 $\pi(b)=0$，则 $bf=0$ 对全部 $f$ 成立。
但 $S|_M=0$ 给
$$
\pi(G)=-N|_M,
\qquad \boxed{\|\pi(G)\|\le1.}
\tag{4.2}
$$
因此即使是具体原空间中的忠实正常表示，依然可能把尾元素的范数缩小任意倍。

令 $Q=(I+G^*G)^{1/2}$。
把 $M$ 与 $H_0$ 酉识别后，该表示准确为
$$
\pi(b)\simeq QbQ^{-1}.
\tag{4.3}
$$
这给出实际度量改变的位置。
$\|Q\|=\sqrt{1+\|G\|^2}$、$\|Q^{-1}\|\le1$；
这些条件数并没有因为表示忠实、正常或来自一个闭不变空间而消失。

## 5. 半群或函数演算也须保留同一个费用

由 (1.1)，每个 $n\ge1$ 有
$\|G^n\|\le K\varepsilon_K^n/n!$。
因此例如
$$
\|e^{zG}\|
\le K\sum_{n\ge0}\frac{(|z|\varepsilon_K)^n}{(n!)^2}
\le K e^{2\sqrt{|z|\varepsilon_K}}.
\tag{5.1}
$$
最后一步用 ${2n\choose n}\le4^n$ 将级数与 $\cosh(2\sqrt{|z|\varepsilon_K})$ 比较。
虽然其增长型随 $K\to\infty$ 变小，前面的实际常数 $K$ 不能删掉；
$\|G\|\to\infty$ 已由 (2.3) 明确证明。
因此只用小平方、谱半径或半群增长型，不能得到所需统一商代表。

## 6. 与原问题的准确区别

本模型没有原 Haar 的全部 dyadic 旋转、连续形式系数及越来越远的弱单位。
尤其 $G^2=t$ 在模型中准确成立，而原首形式阶递推的
$G_j^2-\eta_jN_{j+1}$ 仍具有非零一次形式首项；不能将两者混淆。

它排除的只是如下省略：在原尾商中看到 $\bar G_j^2=\bar t_j$，
或在某个实际半不变空间上看到 $\pi(G_j)=-\pi(N_j)$，
就宣称原尾商范数至多一。
要在原问题中成功，仍须实际证明商包含的反向范数控制，
或构造 $G_j-H_j$ 的有界代表并支付其完整尾来源。


原模型的进一步实质是[正常尾商实现](R236-appendix-normal-tail-ideal-closure-and-finite-amplification.md)中的同一正态分离者和全部 dyadic 尾结构；这里的范围例不替代那一结构，也不否定其有界代表仍可能存在。
