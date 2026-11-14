# R239 附录：两种正权任意重数的完整高度二 primitive Gram 最优统一常数

- 日期：2026-11-13。
- 作者：Astra-ISP-0c；central_review 已对完整 423 行证明独立核验，包括完整逆、全部重数、谱隙、系数与最优性。
- 状态：完整有限维定理。普通 ISP、一般异权相邻序、原连续尾的窄返回费用仍开。
- 扣除旧范围：两个/三个独立异常位、四异常位的整个高度二，以及任意独立头的饱和固定线已有证明。本稿的新参数是两种共同正权的重数均可任意增长；整个高度二 primitive 空间与所有重数一并处理。
- 既有接口：[完整固定块 MP](../results/R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md) §§1–4；[饱和固定线及正交串](../results/R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md) §§8–9。下面给出本次新增的谱隙和系数证明，并明确完整逆如何归入各块。

## 1. 定理与实际逆的约定

取两个位数组，大小为非负整数 $M,N$，满足

$$
M+N=2s+2\ge2.
$$

两组的删除权分别为 $a,b>0$：

$$
D=a\sum_{i=1}^{M}E_i+b\sum_{i=M+1}^{M+N}E_i,
\qquad
K_s=\ker D\cap\mathcal H_s.
$$

在完整孔层 $\mathcal H_s$ 上先取逆，再压到 primitive：

$$
F_n=\frac{D^n(D^*)^n|_{\mathcal H_s}}{(n!)^2},
\qquad
\Gamma_n=P_{K_s}F_n^{-1}|_{K_s},
\qquad n=0,1,2.
\tag{1.1}
$$

这些完整逆存在。有限正权删除与等权删除在各层之间由可逆对角权相似，故秩相同；等权正交升降串给 $D^n:\mathcal H_{s+n}\to\mathcal H_s$ 在 $n\le M+N-2s=2$ 时满射。此秩论证不改变任何实际范数。

定义

$$
C_{M,N}=
\begin{cases}
\dfrac{p+1}{2(p+2)},& M\ne N,\quad p=\min(M,N),\\[6pt]
\dfrac14,&M=N=1,\\[6pt]
\dfrac{q-1}{2q},&M=N=q\ge2.
\end{cases}
\tag{1.2}
$$

**定理。** 对所有 $a,b>0$，

$$
\boxed{\Gamma_1\Gamma_2^{-1}\Gamma_1
\preceq C_{M,N}\Gamma_0,\qquad C_{M,N}<\frac12.}
\tag{1.3}
$$

$C_{M,N}$ 是在两权比 $a/b>0$ 上统一成立的最小常数。若 $M\ne N$ 且 $p\ge1$，或 $M=N=q\ge3$，则每个固定正权比的 (1.3) 均为严格算子序，但权比趋零或无穷时可逼近该统一常数。

若某组为空，则 $C_{M,N}=1/4$ 且等号；$M=N=2$ 的整个空间也有最佳常数 $1/4$。$M=N=1$ 时最佳常数为

$$
\frac{a^2b^2}{(a^2+b^2)^2}\le\frac14.
$$

整体乘常数使 $\Gamma_n$ 乘该常数的 $-2n$ 次幂，故相邻比不变。以下令 $b=1$，把 $a/b$ 简写为 $a$。

## 2. 两组的完整正交串与 primitive 块

对 $T$ 个等权位，记删除为 $D_T$。若 $\zeta$ 是第 $j$ 层的单位 primitive 向量，置

$$
m=T-2j,\qquad
\zeta_r=\frac{(D_T^*)^r\zeta}
{\sqrt{r!\,m^{\underline r}}},
\qquad 0\le r\le m.
$$

由 $[D_T,D_T^*]|_{\mathcal H_p}=(T-2p)I$ 直接归纳，

$$
D_T\zeta_r=\sqrt{r(m-r+1)}\,\zeta_{r-1}.
\tag{2.1}
$$

各串正交，并同时约化 $D_T,D_T^*$。低半层上升单射使第 $j$ 层的 primitive 重数为

$$
\binom Tj-\binom T{j-1}>0,
\qquad 0\le j\le\lfloor T/2\rfloor.
$$

逐层望远镜求和给全维数，故这些串穷尽整个位组，而不只给置换固定部分。

分别对两个组作此分解。一个双串由出生 $j,k$ 指定，其长度为

$$
m=M-2j,\qquad \ell=N-2k.
$$

它酉等价于 $m$ 个共同权 $a$ 的对称串与 $\ell$ 个单位权的对称串之张量。原第 $s$ 层在其中的相对出生为

$$
t=s-j-k=\frac{m+\ell-2}{2}.
\tag{2.2}
$$

该双串同时约化完整 $D,D^*$，又保持孔层。因此 $F_n$、其完整逆、primitive 投影及 $\Gamma_n$ 全部按同一正交分解分块。这里没有先压缩再取逆的交换。

说明相对 primitive 的维数。在相对第 $t$ 层，基向量由头孔数 $r$ 与池孔数 $t-r$ 指定。删除矩阵是相邻两对角矩阵，所有合法下降系数均严格为正。若 $0\le t\le\min(m,\ell)$，输入、输出维数分别为 $t+1,t$；从一端依次消元得满行秩，核为一维。若

$$
\min(m,\ell)<t\le(m+\ell)/2,
$$

两维数相等，非零端点开始的同一消元给可逆，核为零。负出生没有目标。

由 (2.2)，在 $t\ge0$ 的块上，非零 primitive 恰须

$$
|m-\ell|\le2.
\tag{2.3}
$$

两长度同奇偶，所以只有两种情形：

- $m=\ell=q\ge1$，相对出生为 $q-1$；
- 两长度相差二，记较短长度为 $m_0\ge0$，相对出生为 $m_0$。

每个非零块的 primitive 都是一维，所有重数仍在直和中保留。

## 3. 等长双串：准确的三个实际 Gram

先看两组均为 $q\ge1$ 的对称串，权为 $a,1$，出生 $q-1$。写

$$
z=a^2,\qquad
W(z)=\sum_{r=0}^{q}z^r,\qquad
B(z)=\sum_{r=0}^{q-1}(r+1)(q-r)z^r.
\tag{3.1}
$$

使用固定块 MP 公式中的相同头坐标 $x_i=1$，故缺失集合 $R$ 上的线性和为 $|R|=r$。此源同时对两组置换固定，张成当前 primitive 线。

三个未归一 Gram 恰为

$$
\begin{aligned}
H_0
&=\sum_{r=1}^{q}
 \frac{\binom qr}{\binom q{r-1}}z^r r^2
 =\sum_{r=1}^{q}r(q+1-r)z^r
 =zB(z),\\
H_1
&=\min_{\xi\in\mathbb C}\sum_{r=0}^{q}z^r|r-\xi|^2
 =W(z)\operatorname{Var}_{\mu_z}(r),\\
H_2
&=\sum_{r=0}^{q-1}
 \frac{\binom qr}{\binom q{r+1}}z^r(r-q)^2
 =B(z),
\end{aligned}
\tag{3.2}
$$

其中 $\mu_z(r)=z^r/W(z)$。端点没有优化参数；最高阶的强制常数为 $q$。

这些是完整空间的最小范数。具体地，在池固定坐标中，第 $q$ 层到第 $q-1$ 层的删除满射有一维核，全部原像正是参数 $\xi$ 所给的族；两端原像唯一。对池置换平均不增范数并保输出，所以实际最小解就在该族。头权共同又使唯一最小解对头置换固定，故与当前双串完全一致。也可直接使用所引 MP 稿的逐子集有限差分和完整核正交证明。

在源归一后，

$$
\gamma_0=1,\qquad \gamma_1=H_1/H_0,\qquad
\gamma_2=H_2/H_0.
$$

所以相邻常数准确是

$$
\frac{\gamma_1^2}{\gamma_2}
=\frac{H_1^2}{H_0H_2};
\tag{3.3}
$$

源 Gram 没有被省略。

## 4. 等长双串的显式谱隙

令

$$
c_r=(r+1)(q-r),\qquad 0\le r\le q-1,
$$

并定义 $q\times(q+1)$ 矩阵

$$
(\mathsf B_a f)_r
=\sqrt{c_r}\left(\sqrt a\,f_r-a^{-1/2}f_{r+1}\right).
\tag{4.1}
$$

其核为一维，由 $(1,a,\ldots,a^q)$ 张成。行 Gram 的对角与相邻项分别为

$$
(\mathsf B_a\mathsf B_a^*)_{rr}
=(a+a^{-1})c_r,\qquad
(\mathsf B_a\mathsf B_a^*)_{r,r+1}
=-\sqrt{c_rc_{r+1}}.
$$

因此准确有

$$
\mathsf B_a\mathsf B_a^*
=\mathsf B_1\mathsf B_1^*
 +(a+a^{-1}-2)\operatorname{diag}(c_r).
\tag{4.2}
$$

令 $c_{-1}=c_q=0$。因为

$$
2c_r-c_{r-1}-c_{r+1}=2,
$$

向量 $g_r=\sqrt{c_r}$ 满足
$\mathsf B_1\mathsf B_1^*g=2g$。更直接地，对任意复向量 $y$，

$$
\boxed{
\left\langle
(\mathsf B_1\mathsf B_1^*-2I)y,y
\right\rangle
=
\sum_{r=0}^{q-2}c_rc_{r+1}
\left|
\frac{y_r}{\sqrt{c_r}}-
\frac{y_{r+1}}{\sqrt{c_{r+1}}}
\right|^2\ge0.
}
\tag{4.3}
$$

$q=1$ 时右侧为空和，等式仍成立。又 $\min c_r=q$，故

$$
\mathsf B_a\mathsf B_a^*
\succeq
\left[2+q(a+a^{-1}-2)\right]I.
\tag{4.4}
$$

非零奇异值平方相同，所以 $\mathsf B_a^*\mathsf B_a$ 在其核的正交补上也有相同下界。

记 $\bar r=\mathbb E_{\mu_z}r$，取

$$
u_r=\sqrt{\mu_z(r)}(r-\bar r).
$$

它正交于 $(a^r)_{r=0}^{q}$，且
$\|u\|^2=\operatorname{Var}_{\mu_z}(r)$。利用
$\sqrt{\mu_z(r+1)}=a\sqrt{\mu_z(r)}$，精确计算得

$$
\|\mathsf B_a u\|^2
=a\sum_{r=0}^{q-1}c_r\mu_z(r)
=\frac{aB(z)}{W(z)}.
\tag{4.5}
$$

(4.4) 因而给

$$
H_1=W\operatorname{Var}_{\mu_z}(r)
\le
\frac{aB(z)}{2+q(a+a^{-1}-2)}.
$$

代入 (3.2)–(3.3)：

$$
\boxed{
\frac{H_1^2}{H_0H_2}
\le
\frac{1}{[2+q(a+a^{-1}-2)]^2}
\le\frac14.
}
\tag{4.6}
$$

当 $a=1$，均匀分布的方差为 $q(q+2)/12$，且
$B(1)=q(q+1)(q+2)/6$，所以 $H_1=B(1)/2$，确取 $1/4$。当 $a\ne1$，(4.6) 的最右不等式严格。

本节的谱隙作用在明确的有限加权秩分布上；它没有将任意异权多维源的协方差替换成秩方差。

## 5. 相差二的双串：完整 Gram 与精确系数正性

现在看较短长度 $m\ge0$、较长长度 $m+2$，相对出生 $m$。交换两组并整体缩放后，可设短组权为 $a$，长组权为一，仍记 $z=a^2$。

这是饱和固定 primitive 线。完整最小解的准确平方范数为

$$
H_k=\sum_{r=0}^{m}
 \frac{(k+r)!\binom mr z^r}
 {(m+2)^{\underline{k+r}}},
\qquad k=0,1,2.
\tag{5.1}
$$

可以从未归一对称池向量的范数与唯一池固定原像直接得到 (5.1)；所引饱和证明 §8 给了完整有限差分、全核正交及最高阶核验。$m=0$ 时它是两位真空的直接公式，仍有效。

三式有相同公因子 $[(m+1)(m+2)]^{-1}$。删去这个不影响相邻比的公因子，置

$$
\begin{aligned}
A(z)&=\sum_{r=0}^{m}(m+1-r)(m+2-r)z^r,\\
B(z)&=\sum_{r=0}^{m}(r+1)(m+1-r)z^r,\\
C(z)&=\sum_{r=0}^{m}(r+1)(r+2)z^r.
\end{aligned}
\tag{5.2}
$$

实际相邻比正是 $B(z)^2/[A(z)C(z)]$。

令 $d=m+1$，考察

$$
P(z)=dA(z)C(z)-2(d+1)B(z)^2.
\tag{5.3}
$$

$A,C$ 互为次数 $m$ 的反转，$B$ 回文，所以 $P$ 关于次数 $2m$ 回文。只须核验低半系数 $0\le k\le m$；这一区间的卷积完全不见 $r>m$ 的截断。

把 (5.2) 的三个系数公式形式延伸到 $r\ge0$，其生成函数分别为

$$
\frac{d(d+1)-2d(d+2)z+(d+1)(d+2)z^2}{(1-z)^3},
\qquad
\frac{d-(d+2)z}{(1-z)^3},
\qquad
\frac{2}{(1-z)^3}.
$$

按 (5.3) 合并分子，得到

$$
\frac{4(d+2)z[d-(d+1)z]}{(1-z)^6}.
\tag{5.4}
$$

因此低半的准确系数为

$$
\begin{aligned}
[z^k]P
&=4(d+2)\left[
d\binom{k+4}{5}-(d+1)\binom{k+3}{5}
\right]\\
&=\boxed{\frac{4(d+2)}5(5d-k+1)\binom{k+3}{4}}.
\end{aligned}
\tag{5.5}
$$

二项式下标过大时取零。$k=0$ 的系数为零；若
$1\le k\le m=d-1$，则该系数严格为正。回文性支付剩余所有系数。

所以 $m\ge1$、$z>0$ 时 $P(z)>0$，并且

$$
\boxed{
\frac{B(z)^2}{A(z)C(z)}
<
\frac{m+1}{2(m+2)}<\frac12.
}
\tag{5.6}
$$

当 $m=0$，$A=C=2,B=1$，相邻比恰为 $1/4$，与 (5.6) 中的非严格端点一致。

在 $z\downarrow0$ 时，直接读常数项：

$$
\frac{B(z)^2}{A(z)C(z)}
\longrightarrow\frac{m+1}{2(m+2)}.
\tag{5.7}
$$

反转给 $z\uparrow\infty$ 时相同极限。因此这一双串的统一常数已经最优，不能再降。

## 6. 全空间拼合与最优统一常数

第 2 节已将整个 $K_s$ 正交分解成第 4、5 节的标量 primitive 块。各块中的 $\Gamma_n$ 都来自完整逆。因此全空间相邻常数就是这些块的标量相邻比的最大值。

若 $M\ne N$，由于总数为偶数，两数至少相差二。令
$p=\min(M,N)$。任意相差二块的较短长度至多 $p$，所以 (5.6) 给上界
$(p+1)/[2(p+2)]$，并支配等长块的 $1/4$。

这个最长饱和块确实出现。例如 $M<N$ 时，取

$$
j=0,\qquad k=(N-M-2)/2.
$$

两串长度恰为 $M,M+2$，两 primitive 重数均为正。于是 (5.7) 证明上界在权比上最优。$p=0$ 时仅余两位真空块，等号为 $1/4$；$p\ge1$ 时每个有限正权比严格小于统一常数。

若 $M=N=q\ge2$，相差二块须有不同的组出生数，较短长度最多为 $q-2$，并由 $(j,k)=(1,0)$ 或 $(0,1)$ 实际达到。因此最大统一常数是

$$
\frac{(q-2)+1}{2((q-2)+2)}
=\frac{q-1}{2q}.
$$

$q=2$ 时饱和块短长度为零，恒给 $1/4$；$q\ge3$ 时统一常数严格大于 $1/4$，各固定正权比上的所有块都严格低于它。再次用 (5.7) 得到最优性。

最后 $q=1$ 只有等长一位双串，直接由 (3.2) 得
$a^2/(1+a^2)^2$，其统一上界 $1/4$ 在 $a=1$ 达到。整体恢复权 $b$ 即为定理第 1 节的表达式。证毕。

## 7. 已付范围与后续接口

本稿给的是任意两种正权、任意有限重数、整个高度二 primitive 的准确相邻序及最优统一常数。两组的置换串同时约化算子及伴随，因此完整 MP 与全部重数都已支付；没有从某条固定线免费推广。

谱隙证明解决共同头权的最短 penultimate 对称线，回文正系数证明则加强相差二的共同权饱和线。任意异权的六矩测试、一般更高高度的双串、三个以上共同权组，以及原无限连续尾的真实 Schur 返回能量，都不由本稿自动完成。下一步仍应在实际完整最小逆中处理这些未闭范围。
