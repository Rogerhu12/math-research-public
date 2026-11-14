# R152：最大 CM 同余深度与精确的幺幂余核缺陷

日期：2026-11-12。**状态：已证明。** 本文计算实际异常曲线的一个完整整表示不变量，精确说明常用秩一 Euler 系统假设在何处失败；不推出 Mordell–Weil 秩一，也不把这个不变量当作完整 Euler 系统误差项。

## 1. 定理

沿用 R19、R128。设实际无 CM 曲线 $E/\mathbb Q$ 满足
$$
E[p]\simeq A[p],\qquad A:y^2=x^3-x,\qquad p>37.
$$
在本题剩余分支中，$p\equiv3\pmod4$，存在 $|Z|>1$，使
$$
\operatorname{den}j(E)=|Z|^p,\qquad
v_q(\Delta_{E,\min})=p\,v_q(Z)\quad(q\mid Z).
$$
每个 $q\mid Z$ 是乘法约化素数。置
$$
g=\gcd_{q\mid Z}v_q(Z),\qquad M=pg.
$$
R128 已证明：$M$ 的素因子均为 $3\pmod4$，$(M,Z)=1$，且对全部奇数 $m$，
$$
E[m]\simeq A[m]\quad\Longleftrightarrow\quad m\mid M.\tag{152.1}
$$

固定 $\ell\mid M$，写 $n=v_\ell(M)>0$、$T=T_\ell(E)$、$V=T\otimes\mathbb Q_\ell$，并记
$$
G_\ell=\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q(\mu_{\ell^\infty})).
$$
对满足 $\dim_{\mathbb Q_\ell}V/(\tau-1)V=1$ 的 $\tau\in G_\ell$，定义
$$
a(\tau)=\operatorname{length}_{\mathbb Z_\ell}
\bigl(T/(\tau-1)T\bigr)_{\rm tors}.
$$
下面还会直接证明这种 $\tau$ 存在。

**定理 152.1。** 有
$$
\boxed{\min_{\substack{\tau\in G_\ell\\
\dim V/(\tau-1)V=1}}a(\tau)=n=v_\ell(M).}\tag{152.2}
$$
具体而言，每一个这样的余核都有形状
$$
T/(\tau-1)T\simeq\mathbb Z_\ell\oplus\mathbb Z/\ell^{a(\tau)}\mathbb Z,
\qquad a(\tau)\ge n,\tag{152.3}
$$
而选择适当的真实乘法素数 $q\mid Z$ 及 $\tau\in I_q$，可使 $a(\tau)=n$。

因此不存在 $\tau\in G_\ell$ 使整余核自由秩一。换稳定整格、扩张系数环或作二次扭曲，均不能消除这项缺陷。

还有一个不要求 $\tau$ 在特征零幺幂的有限层结论。对 $1\le r\le n$ 及任意 $\tau\in G_\ell$，存在 $0\le b\le r$ 使
$$
E[\ell^r]/(\tau-1)E[\ell^r]
\simeq(\mathbb Z/\ell^b\mathbb Z)^2.\tag{152.4}
$$
$b=0$ 表示零群。因此非零余核从不循环，更不可能自由秩一。

## 2. CM 整坐标与有限层余核

令 $\mathcal O=\mathbb Z_\ell[i]$。由于 $\ell\equiv3\pmod4$，它是未分歧二次扩张的整数环；$A[\ell^r]$ 是 $\mathcal O/\ell^r\mathcal O$ 上的自由秩一模。

取由 $1,i$ 给出的 $\mathbb Z/\ell^r$ 基，令
$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
C=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$
CM 自同构 $[i]$ 定义在 $\mathbb Q(i)$ 上，且其 Galois 共轭为 $[i]$ 或 $[-i]$。因此每个 Galois 矩阵在 $A[\ell^r]$ 上都形如
$$
aI+bJ\quad\text{或}\quad(aI+bJ)C.\tag{152.5}
$$
第二种矩阵迹为零。这只是 CM 自同构的等变性，不需要把任意抽象正规化子与实际像相混。

对 $\tau\in G_\ell$，Weil 配对给 $\det\rho_E(\tau)=1$。若模 $\ell^r$ 矩阵属于 (152.5) 的第二种，则
$$
\det(\rho_E(\tau)-I)=1-\operatorname{tr}\rho_E(\tau)+\det\rho_E(\tau)
=2\pmod{\ell^r}.
$$
因 $\ell$ 为奇素数，$\tau-1$ 可逆，余核为零。

若它属于第一种，$\tau-1$ 就是 $\mathcal O/\ell^r\mathcal O$ 上乘某个元素 $u-1$。这个元素生成的理想恰为 $\ell^b\mathcal O/\ell^r\mathcal O$，其中 $0\le b\le r$，故余核为
$$
\mathcal O/\ell^b\mathcal O\simeq(\mathbb Z/\ell^b\mathbb Z)^2.
$$
经 (152.1) 转回 $E[\ell^r]$，即得 (152.4)。同一论证也适用于任意好素数 $t\ne\ell$ 的 Frobenius，只要 $t\equiv1\pmod{\ell^r}$；这里只使用行列式模 $\ell^r$ 等于一。

## 3. 特征零秩一强迫整矩阵至少深到 $\ell^n$

现设 $\tau\in G_\ell$ 且 $V/(\tau-1)V$ 维数为一。记
$$
U=\rho_E(\tau),\qquad N=U-I.
$$
$N$ 在 $\mathbb Q_\ell$ 上秩一，且 $\det U=1$。所以 $U$ 的两个特征值都为一，从而
$$
\operatorname{tr}U=2,\qquad \operatorname{tr}N=\det N=0,
\qquad N^2=0,\qquad N\ne0.\tag{152.6}
$$

用 $E[\ell^n]\simeq A[\ell^n]$ 选择并提升一个整基。第二种 (152.5) 的矩阵迹为零，不能与迹二同余，故
$$
U\equiv aI+bJ\pmod{\ell^n}.
$$
迹式给 $2a\equiv2\pmod{\ell^n}$，于是
$$
N\equiv bJ\pmod{\ell^n}.\tag{152.7}
$$

若 $b\not\equiv0\pmod{\ell^n}$，写 $a_0=v_\ell(b)<n$。由 (152.7)，$N$ 的全部元素都被 $\ell^{a_0}$ 整除，而
$$
\ell^{-a_0}N\bmod\ell
=(\ell^{-a_0}b\bmod\ell)J
$$
可逆。这与 $N$ 在特征零秩一矛盾。因而 $b\equiv0\pmod{\ell^n}$，继而
$$
\boxed{U-I\in\ell^n\operatorname{End}_{\mathbb Z_\ell}(T).}\tag{152.8}
$$

秩一整矩阵的 Smith 形只有一个非零因子。该因子的赋值是矩阵元素赋值的最小值，故 (152.8) 证明 (152.3) 及 $a(\tau)\ge n$。这个论证使用真实的特征零秩一；不能只从 $(U-I)^2\equiv0\pmod{\ell^n}$ 推出 (152.8)。

## 4. 实际 Tate 惯性达到下界

有限多个正整数 $p\,v_q(Z)$ 的最大公因数为 $M$，故可取 $q\mid Z$ 使
$$
v_\ell\bigl(p\,v_q(Z)\bigr)=n.\tag{152.9}
$$
由 $(M,Z)=1$，$q\ne\ell$。若 $E$ 在 $q$ 非分裂乘法约化，只需取未分歧二次扩张使其成为 Tate 曲线；该二次扭曲在 $I_q$ 上平凡。

令 $\mathfrak q_E$ 为 Tate 参数。其赋值为
$$
v_q(\mathfrak q_E)=v_q(\Delta_{E,\min})=p\,v_q(Z)=:c.
$$
在通常的整 Tate 基中，惯性表示为
$$
\rho_E(\sigma)=
\begin{pmatrix}1&c\,t_\ell(\sigma)\\0&1\end{pmatrix}
\quad(\sigma\in I_q),\tag{152.10}
$$
其中 $t_\ell:I_q\twoheadrightarrow\mathbb Z_\ell$ 是固定单位根基后的 tame $\ell$-角色。公式也可直接由 Tate 参数的 $\ell^k$ 次根得到：单位部分的这些根都可在最大未分歧扩张中选取，只有一致化元的赋值 $c$ 贡献惯性。

取 $t_\ell(\tau)=1$。因为 $q\ne\ell$，所有 $\ell$ 次幂单位根在 $q$ 处未分歧，所以
$$
\tau\in I_q\subset G_\ell.
$$
此时 $\tau-1$ 的唯一非零 Smith 因子为 $c$，因而
$$
T/(\tau-1)T\simeq\mathbb Z_\ell\oplus\mathbb Z_\ell/c\mathbb Z_\ell,
\qquad a(\tau)=v_\ell(c)=n.
$$
这证明等号和所需 $\tau$ 的存在；不需要借助未给定深度的开像定理。

## 5. 改变整格、系数或二次扭曲无助于自由秩一

由 $A[\ell]$ 的实际非分裂正规化子像，$E[\ell]$ 绝对不可约。任意 $G_\mathbb Q$-稳定 $\mathbb Z_\ell$-格 $T'\subset V$，缩放后可设 $T'\subset T$ 且 $T'\not\subset\ell T$。其模 $\ell$ 像非零且稳定，所以等于 $T/\ell T$。Nakayama 引理给 $T'=T$。故全部稳定格互为位似，不能靠选择另一格消除挠部分。

对有限系数扩张的整数环 $R$，平坦性给
$$
(T/(\tau-1)T)\otimes R\simeq R\oplus R/\ell^{a(\tau)}R;
$$
非零挠部分仍在。剩余表示在扩域后仍绝对不可约，同样排除另选非位似稳定 $R$-格的办法。

最后，定义任何椭圆曲线的最小缺陷为 (152.2) 的左端（若没有相应 $\tau$，取无穷）。这个最小值在二次扭曲下不变。事实上，若 $U=I+N$、$N^2=0$，在二次扭曲角色 $\chi(\tau)=1$ 时沿用 $\tau$；若 $\chi(\tau)=-1$，则改取 $\tau^2$，在扭曲后的表示上得到
$$
\rho_{E^\chi}(\tau^2)=(I+N)^2=I+2N.
$$
$2$ 为 $\ell$ 单位，缺陷不变。反向再扭一次给相反不等式，遂得相等。

## 6. 与秩一 Euler 系统假设的准确关系

Mazur–Rubin，*Kolyvagin Systems*，Memoirs of the AMS **168**, no. 799 (2004)，§3.5、假设 (H.2)（印刷 p. 27），要求存在固定全部 $\ell$ 次幂单位根的 $\tau$，使 $T/(\tau-1)T$ **自由秩一**。定理 152.1 证明它在本题全部 $\ell\mid M$ 处失败，最小挠部分阶恰为 $\ell^n$。

[该文原文 PDF](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf)，另见 §3.6 对此 $\tau$ 的 Chebotarev 使用，以及 §6.2 的椭圆曲线应用。

失败不是剩余绝对不可约性的失败，也不意味着 Kato 的几何 Euler 系统不存在。特别是，先张量 $\mathbb Q_\ell$ 后确有秩一余核；本文精确计算的是重新回到整格时不能抹去的挠部分。若使用带误差项的其他定理，仍须逐项证明它的全部假设与误差公式，不能把 $n$ 自动认作所有误差项之和。

R149 的实际新形式中心值只控制模 $\ell^n$；旧稳定化中心值可以有更高的 Euler 零阶数。本文说明这个 $n$ 也恰是上述整秩一接口的最小缺陷。两个深度相同并不提供额外消去：它既不把旧形式的 $sn$ 阶零移给新形式，也不把非零 Selmer 类提升成有理非挠点。$s>0$ 的全局排除仍需新的输入。
