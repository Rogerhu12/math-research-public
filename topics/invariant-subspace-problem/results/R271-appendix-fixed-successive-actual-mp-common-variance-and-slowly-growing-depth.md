# R271 补充：全部固定次数的真实顺次 MP、共同方差窗与同源慢增次数

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 已登记的一次完整 MP 估计在固定方差倍数窗内支付全部输入孔层。本稿继续支付任意预先固定的后继次数，并保留每一次真实 $D_x^\dagger$、原始反馈 $-Cq_r$、全部孔层和同一个完整 Gram 源。共同窗口中的所有中间修正均有显式费用。原同一个 $w$ 的全幂矩可和性进一步允许修正次数缓慢趋于无穷。这里没有把随实际幂零高度增长的全部费用宣称为已支付，也没有把近核向量宣称为稳定子空间 $\overline{B\ker T}$ 中的向量。

依据：

- [固定方差倍数支付全部高度的一次完整 MP](R271-appendix-fixed-variance-full-height-once-mp-and-same-w-summable-correction.md)，尤其原全孔层右逆及准确一次修正；
- [几何起点的原同 W 全塔能量与 R=d 的完整一次 MP](R271-appendix-geometric-cutoffs-same-w-complete-energy-and-d-sized-once-mp.md)，尤其 §7 对任意 $w\in\ker T$ 的直接全幂矩；
- [原连续尾完整 coherent 列及 Bernoulli 原像](R271-appendix-continuous-tail-coherent-columns-bernoulli-lifts-and-exact-residuals.md)。

## 1. 原算子、原完整源和共同窗口

令
$$
D=D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad
S=S_x=\sum_{i\ge x}(i+1)^{-4},\qquad
\omega_j=(D^*)^j\Omega,
$$
其中 $x\ge1$。原全孔层 MP 记为 $Q_D=D^\dagger$；此符号与母支持参数 $Q$ 区别。已证明
$$
DQ_D=I,\qquad
\|Q_D|_{\mathcal H_j}\|
\le12\,512^j(x+j+1)^{3/2},
\qquad
\|\omega_j\|^2\le j!S^j.
\tag{1.1}
$$
(1.1) 的满射和 MP 范数均在完整孔层上成立。其全直和可以无界；以下向量和全部中间像均只有有限孔层。

设实际有限头 $C^h=0$，$h\ge1$，并与所有纯尾算子交换。对任意完整头源 $g$，始终采用原完整逆
$$
H_C(s)=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{j!s^j},
\qquad
a=H_C(s)^{-1}g,
\qquad
E_j=\frac{\|C^ja\|^2}{j!s^j}.
\tag{1.2}
$$
定义
$$
f_s=\sum_{j=0}^{h-1}
\frac{(-C)^ja\otimes\omega_j}{j!s^j},
\qquad
\epsilon_s=\sum_{j=1}^{h-1}E_j,
\qquad
\delta_s=\|g\|^2-\langle g,H_C(s)^{-1}g\rangle.
\tag{1.3}
$$
正规方程和远孔正交给
$$
\delta_s=\|g-a\|^2+\epsilon_s,\qquad
\|f_s-i_0g\|^2\le\delta_s
\quad(s\ge S).
\tag{1.4}
$$

固定整数 $k\ge1$，同时对所有 $1\le r\le k$ 采用同一个 $s$：
$$
c_k=2\cdot512^{2k},
\qquad s\in[c_kS,\,2c_kS].
\tag{1.5}
$$
后面不把第 $r$ 次单独窗口的结论免费搬到 (1.5)；全部中间费用都重新用共同上界 $c_k$ 计算。

## 2. 真实反馈、全部中间母支持与准确终止式

记 $\mathscr L=C+D$。定义真实顺次算法
$$
z_0=f_s,\qquad
q_1=Q_D\mathscr Lf_s,\qquad
q_{r+1}=Q_D\mathscr Lz_r,\qquad
z_r=f_s-\sum_{a=1}^r q_a.
\tag{2.1}
$$
则逐步有
$$
q_r=(-C)^{r-1}Q_D^r\mathscr Lf_s,
\qquad
\mathscr Lz_r=-Cq_r.
\tag{2.2}
$$
证明只用 $DQ_D=I$ 和不同张量因子的交换：若 $\mathscr Lz_{r-1}=-Cq_{r-1}$，则 $Dq_r=\mathscr Lz_{r-1}$，故 $\mathscr Lz_r=-Cq_r$。没有把 $(D^r)^\dagger$ 替换为 $Q_D^r$，也没有把 $DQ_D=I$ 反过来作为任意源上的 $Q_DD=I$。

准确的初始残量行是
$$
(\mathscr Lf_s)_j=
\frac{(-C)^{j+1}a}{(j+1)!s^{j+1}}
\otimes
\left[D\omega_{j+1}-(j+1)s\omega_j\right].
\tag{2.3}
$$
因为 $\omega_{j+1}\in\operatorname{Ran}D^*$，仅在这个实际输入上
$Q_DD\omega_{j+1}=\omega_{j+1}$。由此
$$
(q_r)_{j+r}
=
\frac{(-C)^{j+r}a}{(j+1)!s^{j+1}}
\otimes
\left[
Q_D^{r-1}\omega_{j+1}-(j+1)sQ_D^r\omega_j
\right],
\quad 0\le j\le h-r-1.
\tag{2.4}
$$
当 $j+r\ge h$ 时，头因子由真实 $C^h=0$ 消失。因此所有 $q_r,z_r$ 仍只有远孔层 $0,\ldots,h-1$，而非随着修正次数增加母支持。所有 $Q_D$ 及其组合的输入均在自然域内。特别 $q_r=0$ 对 $r\ge h$ 成立，且 $\mathscr Lz_{h-1}=0$；$h=1$ 时直接有 $\mathscr Lf_s=0$。

更具体地，令 $(f_s)_p$ 为第 $p$ 个远孔行。对 $0\le p<h$，设 $n=\min(r,p)$，则
$$
(z_r)_p=(-C)^nQ_D^n(f_s)_{p-n}.
\tag{2.5}
$$
确实，把 (2.3) 写为 $C(f_s)_j+D(f_s)_{j+1}$ 后，各修正行是
$$
(q_a)_p
=(-C)^{a-1}Q_D^{a-1}(f_s)_{p-a+1}
-(-C)^aQ_D^a(f_s)_{p-a};
$$
从 $a=1$ 到 $n$ 完整相消即得 (2.5)。特别全部修正结束后
$$
z_{h-1}
=\sum_{p=0}^{h-1}(-C)^pa\otimes Q_D^p\Omega.
\tag{2.6}
$$
(2.6) 保留真正顺次 MP 的 primitive 反馈；它也显示初始阻尼在最终尾列中已经相消，只留在 $a=H_C(s)^{-1}g$ 中。

## 3. 任意固定后继次数的全层预算

原完整层估计相乘给
$$
\|Q_D^r|_{\mathcal H_j}\|
\le
12^r512^{rj+r(r-1)/2}
(x+j+r)^{3r/2}.
\tag{3.1}
$$
这对任意 $j\ge0$ 成立，不使用低孔 primitive 压缩。

不同 $j$ 在 (2.4) 中落在不同输出孔层。将其平方中的头因子写成 $E_{j+r}$，并只为上界使用
$\|u-v\|^2\le2\|u\|^2+2\|v\|^2$，得到
$$
\|q_r\|^2
\le\sum_{j=0}^{h-r-1}(A_{j,r}+B_{j,r})E_{j+r},
\tag{3.2}
$$
其中
$$
A_{j,r}=
2\,12^{2r-2}512^{r(r-1)}
\frac{(j+r)!}{(j+1)!}
[s(x+j+r)^3]^{r-1}
\left(\frac Ss\right)^{j+1}
512^{2(r-1)j},
\tag{3.3}
$$
$$
B_{j,r}=
2\,12^{2r}512^{r(r-1)}
\frac{(j+r)!}{j!}
[s(x+j+r)^3]^r
\left(\frac{512^{2r}S}{s}\right)^j.
\tag{3.4}
$$
式 (3.3) 在 $r=1$ 按空乘积理解。

当 $1\le r\le k$ 且 $s$ 在共同窗口 (1.5) 时，
$$
\frac{512^{2r}S}{s}\le\frac12,\qquad
s(x+j+r)^3\le c_k(j+r+1)^3.
\tag{3.5}
$$
第二式用 $S\le(3x^3)^{-1}$ 和 $x+j+r\le x(j+r+1)$。阶乘比逐因子估计后，
$$
A_{j,r}+B_{j,r}
\le
4\,12^{2r}512^{r(r-1)}c_k^r
(j+r+1)^{4r}2^{-j}.
\tag{3.6}
$$
因此令
$$
K_{r\mid k}
=
4\,12^{2r}512^{r(r-1)}c_k^r
\sum_{j=0}^{\infty}(j+r+1)^{4r}2^{-j},
\tag{3.7}
$$
即有完整共同源估计
$$
\boxed{\quad
\|q_r\|^2\le K_{r\mid k}
\sum_{\ell=r}^{h-1}E_\ell
\le K_{r\mid k}\epsilon_s,
\qquad 1\le r\le k .
\quad}
\tag{3.8}
$$
没有截断全部高度中的中段或最高非零项。

这些常数完全显式。由
$(j+r+1)\le(r+1)(j+1)$ 及
$$
\sum_{j\ge0}(j+1)^n2^{-j}
\le n!\sum_{j\ge0}\binom{j+n}{n}2^{-j}
=2^{n+1}n!,
$$
可取
$$
K_{r\mid k}
\le
2^{4r+3}12^{2r}512^{r(r-1)}c_k^r
(r+1)^{4r}(4r)!.
\tag{3.9}
$$
特别 $\log K_{k\mid k}=O(k^2+k\log(k+1))$，其中绝对隐常数不依赖 $x,h,C,g$。$k=1$ 的更锐费用 $1+47616c_1$ 已由旧一次 MP 定理支付；这里新增的是全部固定后继次数及同一个窗口中的所有中间步骤。

## 4. 原强头、原同源与全部母窗

取原真实强头
$$
C=A_m+D_{[m,x)},\qquad R=x-m,\qquad h=2^m+R.
$$
所有原 carry 都仍在 $A_m$ 中。只要原母支持满足
$$
Q\ge R+h-1,
\tag{4.1}
$$
最初完整阻尼列仍有已证明的原低 forcing 同余
$$
P_{V_Q}f_s=P_{V_Q}i_0g,\qquad
P_{K_Q}f_s=P_{K_Q}i_0g.
\tag{4.2}
$$
(2.4) 的全部中间修正也留在同一个母支持内。原同一向量应始终写为
$$
u_g=(P_{V_Q}-P_{K_Q})
\left(z_k+\sum_{r=1}^kq_r\right),
\tag{4.3}
$$
而非删除修正项后把 $(P_{V_Q}-P_{K_Q})z_k$ 重新称为原 $u_g$。

令
$$
A_k=1+\sum_{r=1}^k\sqrt{K_{r\mid k}}.
$$
则 (1.4)、(2.2)、(3.8) 给
$$
\|z_k-i_0g\|\le A_k\sqrt{\delta_s},
\qquad
\|\mathscr Lz_k\|
\le\|C\|\sqrt{K_{k\mid k}\epsilon_s}.
\tag{4.4}
$$
原头上 $\|C\|\le7$。特别，修正后的残量准确为 $-Cq_k$；本节没有为它提供免费 exact regular lift。

## 5. 同一个实际 w 的全塔可和性

采用已登记的实际小前缀参数
$$
m\ge10,\qquad d=2^m,\qquad
R=d,\quad x=m+d,\quad h=2d,\quad Q=2d^3.
\tag{5.1}
$$
原全部母门已在引用稿核实，且 (4.1) 有充足余量。

对任意同一个 $w\in M=\ker T$，令 $g_m=P_{x_m}w$，以及
$$
\mathcal E_m^\omega(w)
=
\sum_{j=1}^{h_m-1}
\frac{\omega_{x_m,j}^2}{\nu_{x_m,j}^2}
\|C_m^jP_{x_m}w\|^2,
\qquad
\omega_{x,j}^2=\frac{S_{x+j-1}}{jS_x},
\quad
\nu_{x,j}^2=(j!)^2e_j(x).
\tag{5.2}
$$
引用稿 §7 保留真实 carry，已经证明
$$
\sum_m\mathcal E_m^\omega(w)<\infty,\qquad
\delta_{m,s}\le\mathcal E_m^\omega(w)
\quad\hbox{对全部 }s\ge8S_{x_m}.
\tag{5.3}
$$
这是原完整 $H_{C_m}(s)^{-1}$，没有将源改为某个不同投影或将能量转到加权最小化。

固定 $k$，任取每个 $s_m\in[c_kS_{x_m},2c_kS_{x_m}]$。于是所有真实中间修正同时满足
$$
\sum_m\sum_{r=1}^k\|q_{m,r}\|^2<\infty,
\qquad
\sum_m\|z_{m,k}-i_0g_m\|^2<\infty,
\qquad
\sum_m\|\mathscr L_mz_{m,k}\|^2<\infty.
\tag{5.4}
$$
每项的明确上界分别为
$\sum_{r\le k}K_{r\mid k}\sum_m\mathcal E_m^\omega(w)$、
$A_k^2\sum_m\mathcal E_m^\omega(w)$、
$49K_{k\mid k}\sum_m\mathcal E_m^\omega(w)$。
同一个 $w\in W$ 时，亦可直接用引用稿的同 $W$ 能量
$\Delta_m^\omega$ 代替 (5.2)，并保留原 (4.3)。

## 6. 在同一物理母窗中缓慢增加修正次数

对固定 $w\in M$，可以在 (5.1) 的全部整数 $m$ 上选择整数
$k_m\to\infty$，并保持
$$
k_m\le m/12,\qquad
s_m\in[c_{k_m}S_{x_m},2c_{k_m}S_{x_m}],
\qquad s_m\longrightarrow0,
\tag{6.1}
$$
使
$$
\sum_m
\left[
\|z_{m,k_m}-i_0g_m\|^2+
\|\mathscr L_mz_{m,k_m}\|^2+
\sum_{r=1}^{k_m}\|q_{m,r}\|^2
\right]<\infty.
\tag{6.2}
$$
允许删除有限个初始 $m$。

证明如下。令
$$
F_k=A_k^2+49K_{k\mid k}+\sum_{r=1}^kK_{r\mid k}.
$$
由 (5.3)，逐次选择严格递增整数 $M_k\ge12k$，使
$$
F_k\sum_{m\ge M_k}\mathcal E_m^\omega(w)\le2^{-k}.
$$
当 $M_k\le m<M_{k+1}$ 时取 $k_m=k$，然后使用共同窗口的全部估计，即得 (6.2)。又 $x_m\ge2^m$，所以
$$
s_m\le2c_{k_m}S_{x_m}
\le\frac43\,2^{18k_m-3m}
\le\frac43\,2^{-3m/2}\longrightarrow0.
$$
所有修正仍留在原 $R+h-1$ 母支持，且每个中间 MP 都在其自然域；这里没有增加原 $Q$ 或改变实际头算子。

## 7. 准确完成范围

本稿支付的是任意固定后继次数，及由同源可和性选择的慢增次数。它显式记录真实最终列 (2.6)，但没有支付在每个实际头上取 $k=h_m-1$ 时增长的全部常数。上面的慢增选择满足 $k_m\ll h_m$，其剩余量仍是实际 $-C_mq_{m,k_m}$。

因此，(6.2) 和原 $P_{x_m}w\to w$ 不能被用来断言 $z_{m,k_m}\in\ker T$ 或 $w\in\overline{B\ker T}$。下一项真实接口仍是：利用同一个 $w$ 的精确层关系降低顺次 MP 的最终费用，或者在原允许费用内对剩余 $-Cq_k$ 给出保持原源的精确 regular correction。
