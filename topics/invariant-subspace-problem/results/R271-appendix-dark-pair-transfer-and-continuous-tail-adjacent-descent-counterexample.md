# R271 附录：相邻暗对背景把第一下降反例接入真实连续尾

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：完整证明；根代理与 kernel_resume_1cf 已独立核查真实最小原像、配位奇偶、完整远尾误差及高孔层量词。所有最小原像和高度投影均取在真实无限连续尾的原 Hilbert 范数中。

本文把[七位反例](R271-appendix-seven-bit-counterexample-to-universal-adjacent-descent-order.md)接到原权 $b_j=(j+1)^{-2}$。未选位置全部保留：有限部分配成严格的 $D$-核向量，无限远尾保留在伴随误差中。实际最小原像用对偶下界和显式试探上界控制，不使用核投影连续性或全层一致谱隙。

## 1. 真实对象与结论

在[占据交换子稿](R271-appendix-occupation-commutator-known-source-minimum-energy.md)的有限子集尾模型中，令
$$
D_m=\sum_{j\ge m}b_jE_j,\qquad b_j=(j+1)^{-2},\qquad d=2^m.
$$
第 $p$ 孔层为 $\mathcal H_p$。真空是无孔向量，不是 Haar 参考向量。置
$$
E_{h,p}=\ker D_m^h\cap\mathcal H_p,\qquad
U_{h,p}=E_{h,p}\ominus E_{h-1,p}.
$$
固定 primitive 孔数 $s$，以下两个块作用于相邻实际高度：
$$
A_{2,s+1}=D_m|_{U_{2,s+1}}:U_{2,s+1}\longrightarrow\ker D_m\cap\mathcal H_s,
$$
$$
A_{3,s+2}=P_{U_{2,s+1}}D_m|_{U_{3,s+2}}.
$$
它们是尾部第一下降块，不能与有限头 $A_m$ 混同。

**定理 1.1。** 存在整数 $m_0$，使对每个 $m\ge m_0$ 及每个整数
$$
s\ge4d=4\cdot2^m,
$$
真实连续尾均不满足
$$
A_{3,s+2}A_{3,s+2}^*
\le2A_{2,s+1}^*A_{2,s+1}.                     \tag{1.1}
$$

更一般，定义允许取无穷大的真实比较常数
$$
\mathfrak c_{m,s}
=\sup_{0\ne x\in U_{2,s+1}}
\frac{\|A_{3,s+2}^*x\|^2}{\|A_{2,s+1}x\|^2}.
\tag{1.2}
$$
分母对非零 $x$ 为正，因为 $U_{2,s+1}\perp\ker D_m$。则
$$
\boxed{\displaystyle
\liminf_{m\to\infty}\ \inf_{s\ge4\cdot2^m}
\mathfrak c_{m,s}\ge\frac83.
}                                                     \tag{1.3}
$$
因此每个固定 $C<8/3$ 在所有足大 $m$、全部上述高孔层上都不是有效的统一常数。本文没有证明 $8/3$ 足够，也没有给实际 $\mathfrak c_{m,s}$ 的统一上界。

量词中的 $s$ 是 primitive 孔数，所比较高度为 $h=2$，中间实际孔层为 $p=s+1$。这里没有把 $s$ 当成旧窗口宽度。特别地，在旧允许区间 $4d\le q\le\exp(d^3/4)$ 中，取 $s=q$ 或 $s=q+t-1\ge q$ 都落在本结论的量词内。

## 2. 不依赖全局谱隙的最小原像传递引理

将布尔位置分成有限活跃集和其余背景，写
$$
\widehat D=D_{\rm a}\otimes I+I\otimes D_{\rm b}.
$$
设背景向量 $\chi$ 满足
$$
\|\chi\|=1,\qquad D_{\rm b}\chi=0,\qquad
\delta=\|D_{\rm b}^*\chi\|.
$$
取活跃的单位 primitive 向量 $g$，即 $D_{\rm a}g=0$、$\|g\|=1$。设 $v_2,v_3$ 分别是有限活跃空间中
$$
D_{\rm a}v_2=g,\qquad D_{\rm a}^2v_3=g
$$
的最小范数解，并取 $w$ 使 $D_{\rm a}^*w=v_2$。记
$$
a=\|v_2\|^2,\qquad b=\|v_3\|^2,\qquad \tau=\|w\|^2.
$$
本稿使用的有限活跃算子满射到第1孔层，故这些向量存在。

令 $G=g\otimes\chi$。在整个背景仍保留的真实空间中，$x_2,x_3$ 分别是
$$
\widehat D x_2=G,\qquad \widehat D^2x_3=G
$$
的最小范数解。这里的活跃 $g,w$ 属于第1孔层，$\chi$ 属于固定背景孔层；两个最小化分别在对应总孔层进行。若在全空间最小化，由正交孔数分级也得到同一最小元。
两个解集都非空：$v_2\otimes\chi$ 和 $v_3\otimes\chi$ 分别是解。解集是闭仿射子空间，故各有唯一最小元；不需要假设整个像闭。置
$$
a_{\rm full}=\|x_2\|^2,\qquad b_{\rm full}=\|x_3\|^2.
$$

**引理 2.1。**
$$
\boxed{
a_{\rm full}\ge\frac{a^2}{a+\tau\delta^2},
\qquad b_{\rm full}\le b.
}                                                       \tag{2.1}
$$

**证明。** 第二式用试探解 $v_3\otimes\chi$ 即得。对第一式，令 $W=w\otimes\chi$，则
$$
\langle G,W\rangle=\langle D_{\rm a}v_2,w\rangle
=\|v_2\|^2=a.
$$
而
$$
\widehat D^*W=v_2\otimes\chi+w\otimes D_{\rm b}^*\chi.
$$
两项的活跃孔数不同，因而严格正交，故
$$
\|\widehat D^*W\|^2=a+\tau\delta^2.
$$
对任意 $\widehat D u=G$，Cauchy--Schwarz 给
$$
a^2=|\langle u,\widehat D^*W\rangle|^2
\le\|u\|^2(a+\tau\delta^2).
$$
取最小值即得。证毕。

### 2.2 候选比较必满足的标量条件

因为 $\widehat DG=0$，两个真实最小解分别属于实际 $U_2$、$U_3$。更准确，$x_2\perp\ker\widehat D$ 且 $\widehat D^2x_2=0$；$x_3\perp\ker\widehat D^2$ 且 $\widehat D^3x_3=0$。

$\widehat D x_3$ 属于 $\ker\widehat D^2$ 并满足 $\widehat D(\widehat D x_3)=G$。将其正交投影到 $U_2$ 正好去掉 $\ker\widehat D$ 分量，因此
$$
A_3x_3=x_2,\qquad A_2x_2=G,                 \tag{2.2}
$$
这里暂以 $A_2,A_3$ 记 $\widehat D$ 的真实块。若 $A_3A_3^*\le C A_2^*A_2$，则
$$
a_{\rm full}^2
=|\langle x_3,A_3^*x_2\rangle|^2
\le b_{\rm full}\|A_3^*x_2\|^2
\le C b_{\rm full}.                          \tag{2.3}
$$
从而真实比较常数至少为
$$
\boxed{
\mathfrak c\ge
\frac{a_{\rm full}^2}{b_{\rm full}}
\ge \frac{a^4}{b(a+\tau\delta^2)^2}.
}                                                       \tag{2.4}
$$
这是对完整最小原像的下界，不是把活跃子空间误当成实际高度空间。

## 3. 连续尾中的精确背景与完整伴随误差

先用七个活跃位置。取强位 $m$，并令 $\ell_m$ 为满足
$$
\ell_m\ge\sqrt{10}(m+1)-1,\qquad
\ell_m-m-1\ \text{为偶数}
$$
的最小整数。于是
$$
0\le\ell_m+1-\sqrt{10}(m+1)<2.
$$
六个弱活跃位置为 $\ell_m,\ldots,\ell_m+5$。对给定 $s\ge4\cdot2^m$，置
$$
K=m+2s+5.
$$
当 $m$ 足大时，$\ell_m+6<K$。

将两个区间
$$
[m+1,\ell_m),\qquad [\ell_m+6,K)
$$
内的整数各按相邻两位配对。两个区间长度都为偶数，因此没有遗留位置。它们共含 $2s-2$ 个位置，即 $s-1$ 对。对一对相邻位置 $j,j+1$，定义
$$
\chi_j=
\frac{b_{j+1}e_j-b_je_{j+1}}
{\sqrt{b_j^2+b_{j+1}^2}}.
\tag{3.1}
$$
$\chi_j$ 是单位一孔向量，且准确满足
$$
(b_jE_j+b_{j+1}E_{j+1})\chi_j=0.
$$
令 $\chi$ 为所有这些向量的张量积，并在全部 $j\ge K$ 的位置取无孔真空。于是 $\chi$ 是背景中的单位 $(s-1)$ 孔向量，且
$$
D_{\rm bg}\chi=0.
$$
所有未选位置仍属于 $D_{\rm bg}$。

同位计算给
$$
\|(b_jE_j^*+b_{j+1}E_{j+1}^*)\chi_j\|^2
=\frac{(b_j^2-b_{j+1}^2)^2}{b_j^2+b_{j+1}^2}.
$$
不同对被升为两孔时，以及远尾新生一个孔时，所得向量两两正交。因此完整背景伴随的范数为
$$
\|D_{\rm bg}^*\chi\|^2
=\sum_{\text{配对 }j,j+1}
\frac{(b_j^2-b_{j+1}^2)^2}{b_j^2+b_{j+1}^2}
+\sum_{j\ge K}b_j^2.                         \tag{3.2}
$$
这里明确保留了无限远尾项。

由
$$
\frac{(x^2-y^2)^2}{x^2+y^2}\le2(x-y)^2,\qquad
0<b_j-b_{j+1}\le\frac2{(j+1)^3},
$$
以及级数积分估计，
$$
\|D_{\rm bg}^*\chi\|^2
\le\frac8{5(m+1)^5}+\frac1{3K^3}.            \tag{3.3}
$$

现在统一归一化
$$
\widehat D=D_m/b_m,\qquad b_m=(m+1)^{-2}.
$$
这不改变任何核或高度空间，比较常数 (1.2) 也不变。引理中的归一化背景满足
$$
\delta_{m,s}^2
\le\frac8{5(m+1)}+\frac{(m+1)^4}{3K^3}
\le\kappa_m,
$$
$$
\kappa_m=
\frac8{5(m+1)}
+\frac{(m+1)^4}{3(m+8\cdot2^m+5)^3}
\longrightarrow0.                           \tag{3.4}
$$
这一收敛对全部 $s\ge4\cdot2^m$ 一致。

## 4. 活跃最小逆的有限维连续性

归一化活跃权为
$$
c_0=1,\qquad
c_i=\frac{(m+1)^2}{(\ell_m+i)^2}\quad(1\le i\le6).
$$
它们趋于 $(1,1/10,\ldots,1/10)$。在活跃第1孔层令
$$
w_1=6^{-1/2}\sum_{i=1}^6e_i,\qquad
\gamma_c=6^{-1/2}\sum_{i=1}^6c_i,
$$
$$
g_c=\frac{w_1-\gamma_ce_0}{\sqrt{1+\gamma_c^2}}.
\tag{4.1}
$$
这里 $e_0$ 表示强活跃位有孔。准确有 $\|g_c\|=1$、$D_{\rm a}(c)g_c=0$。

有限层 $D_{\rm a}(c):\mathcal H_2^{\rm a}\to\mathcal H_1^{\rm a}$ 和
$D_{\rm a}(c)^2:\mathcal H_3^{\rm a}\to\mathcal H_1^{\rm a}$ 都满射。一个直接验证如下：若
$$
R_p(c)e_I=\Bigl(\prod_{i\in I}c_i\Bigr)e_I,
$$
则
$$
D_{\rm a}(c)|_{\mathcal H_p^{\rm a}}
=R_{p-1}(c)^{-1}D_{\rm a}(1)R_p(c).
$$
其幂也满足相应式，故秩与所有权等于1时相同。在七位情形，
$$
D_{\rm a}(1)D_{\rm a}(1)^*=5I+\mathbf1\mathbf1^*,
$$
$$
D_{\rm a}(1)^2(D_{\rm a}(1)^*)^2
=40I+20\mathbf1\mathbf1^*
$$
作为第1孔层上的算子均正定。

因此
$$
w(c)=[D_{\rm a}(c)D_{\rm a}(c)^*]^{-1}g_c,\qquad
v_2(c)=D_{\rm a}(c)^*w(c),
$$
$$
v_3(c)=(D_{\rm a}(c)^*)^2
[D_{\rm a}(c)^2(D_{\rm a}(c)^*)^2]^{-1}g_c
\tag{4.2}
$$
在这些正权附近连续，且是整个活跃布尔空间中的真实最小原像。记
$$
a_m=\|v_2(c)\|^2,\quad b_m^{\rm inv}=\|v_3(c)\|^2,\quad
\tau_m=\|w(c)\|^2.
$$
用 $b_m^{\rm inv}$ 区别原位权 $b_m$。由七位反例的准确计算，
$$
a_m\longrightarrow a_0=\frac{2050}{53},\qquad
b_m^{\rm inv}\longrightarrow b_0=\frac{38000}{53},
\qquad \sup_{m\ {\rm 足大}}\tau_m<\infty,
$$
$$
\frac{a_0^2}{b_0}=\frac{8405}{4028}>2.         \tag{4.3}
$$

## 5. 真连续尾的反例

取
$$
G_{m,s}=g_c\otimes\chi\in\ker D_m\cap\mathcal H_s.
$$
它是单位真实 primitive 向量。使用第2节的真实最小原像和 (3.4)，对每个 $s\ge4\cdot2^m$ 有
$$
\mathfrak c_{m,s}
\ge
\frac{a_m^4}
{b_m^{\rm inv}(a_m+\tau_m\delta_{m,s}^2)^2}
\ge
\frac{a_m^4}
{b_m^{\rm inv}(a_m+\tau_m\kappa_m)^2}.
\tag{5.1}
$$
右端不依赖 $s$，并趋于 $8405/4028>2$。故对所有足大 $m$ 和全部上述 $s$，(1.1) 失败。定理 1.1 得证。

这里的真实反例测试向量可以定义为
$$
f_{m,s}
=\frac{x_2}{\|x_2\|},\qquad
x_2=\operatorname*{argmin}_{\widehat D x=G_{m,s}}\|x\|.
$$
它准确属于完整连续尾的 $U_{2,s+1}$。证明没有断言 $v_2(c)\otimes\chi$ 本身属于这个实际高度空间，也没有把任何环境伴随替代为受限伴随。

## 6. 真实连续尾中 $8/3$ 的必要下界

七位计算的同一对称家族允许一个强位、任意偶数 $r\ge6$ 个相同弱位 $\varepsilon>0$。记其最小原像范数平方为 $a(r,\varepsilon)$、$b(r,\varepsilon)$。七位稿已准确证明
$$
\frac{a(r,\varepsilon)^2}{b(r,\varepsilon)}
=
\frac{2(r-2)((r-1)\varepsilon^2+2)^2}
{(r-1)(1+r\varepsilon^2)((r-2)\varepsilon^2+3)}
\longrightarrow_{\varepsilon\downarrow0}
\frac{8(r-2)}{3(r-1)}.                       \tag{6.1}
$$
固定一个这样的 $r$ 和 $0<\varepsilon<1$。将弱活跃簇放在
$$
\ell_m+1=\varepsilon^{-1/2}(m+1)+O(1),
\qquad \ell_m-m-1\ \text{为偶数},
$$
取 $r$ 个连续位置，并改取
$$
K=m+2s+r-1.
$$
两个背景区间长度仍为偶数，准确有 $s-1$ 个暗对；(3.2)--(3.4) 的估计不变，仅末项中的 $K$ 改为该值。对每个固定 $r,\varepsilon$，当 $m$ 足大时活跃簇位于 $K$ 之前，而且有限活跃最小逆连续趋于 (6.1) 的模型。

故 (5.1) 的同一证明给
$$
\liminf_{m\to\infty}\inf_{s\ge4\cdot2^m}\mathfrak c_{m,s}
\ge\frac{a(r,\varepsilon)^2}{b(r,\varepsilon)}.
$$
先令 $\varepsilon\downarrow0$，再令偶数 $r\to\infty$，即得 (1.3)。这里只逐个使用固定的有限模型，不需要对增长的 $r$ 作未经证明的统一连续性估计。

## 7. 对原 Schur 能量问题的准确范围

本稿关闭了普遍异权候选，也进一步关闭了该候选在真实连续尾的全高孔层版本。其证据是原 Hilbert 范数中的真实最小原像，而非删去未选位置、换度量或有限数值实验。

但 $G_{m,s}$ 只被证明属于完整 $\ker D_m$。本文没有证明它来自原边界向量 $w\in M\ominus N$，没有证明它是完整低链投影后的返回源 $F P_ZS_1^*z_2$，也没有证明它属于实际 $\zeta$ 或 $\sigma$ 的更窄来源。因此本稿没有给 $E_2$ 或原不变子空间问题一个反例。

仍需沿[真实末块返回源笔记](../notes/2026-11-13-actual-last-block-return-source-and-complete-low-chain-projection-1cf.md)支付实际同源修复的 $Q$-范数，或证明只在实际 Schur 源上的较弱比较。式 (1.3) 也不排除常数大于等于 $8/3$ 的有效比较；本稿不宣称这样的上界成立。

后续[全高度平方比较下界](R271-appendix-two-cluster-minimal-inverses-and-squared-all-height-comparison-lower-bounds.md)已用两簇全阶真实最小逆和暗对高阶矩，把本稿h2的8/3必要下界提高到4，并对每个固定h给出[h/(h−1)]²必要下界。全部未选位和真实最小原像仍保留；该后续结果仍未给统一上界或窄Schur源的实现。
