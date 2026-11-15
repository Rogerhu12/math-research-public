# R657 增补 — 原两 Euler 观察的连续前缀与 25/18 接触常数

日期：2026-11-15。**状态：已证明。**

本增补保持 R657 的同一个原来源、完整 $\mathcal C_p$、全部十九角、$w^{13}/U_0$ 和共同 charge 四十。对同一 $P$ 同时观察
$$
\bigl(\Phi(P),\Phi(\mathcal EP)\bigr),
\qquad \mathcal E=Y\partial_Y,
$$
可将连续满列秩前缀进一步缩短。这里 $\mathcal E$ 确实保持原来源，但并不假设它保持任何原核；两输出只是一个显示的联合矩阵，不是从原中央获得的新零条件。

## 1. 精确长度

沿用 [R657](../results/R657-original-long-ordered-prefix-and-quadratic-contact-bound.md) 的
$$
p=6s-1>101,\qquad
f_D=\lfloor9D/2\rfloor+4<p,
$$
原列 $Y^nq_n(t)t^k$、$b_n=A_n+e_{n+1}$，以及
$$
J_n(u)=\left\lfloor\frac{b_n+13-u}{s}\right\rfloor,\qquad
C_u=\sum_{n=0}^{D}(J_n(u)+1)_+,\quad0\le u<s.
$$
定义真正出现于补齐族的节点数
$$
N_u=\#\{0\le n\le D:J_n(u)\ge0\}.
\tag{1}
$$
当 $C_u>0$ 时令
$$
H_u=\max\{N_u,\ C_u-N_u+1\};
$$
当 $C_u=0$ 时令 $H_u=0$。再置
$$
\boxed{
k_1=1+\max_{H_u>0}\{u+s(H_u-1)\}.
}
\tag{2}
$$
因 $C_u\le p$，对非空余类 $1\le H_u\le p$。又 $N_u$ 及
$$
C_u-N_u=\sum_{n=0}^{D}(J_n(u))_+
$$
都随 $u$ 不增，故 $H_u$ 不增，且
$$
\boxed{
1+s(H_0-1)\le k_1\le sH_0\le sp.
}
\tag{3}
$$

**定理。** 把同一联合整评价
$$
P\longmapsto\bigl(\Phi(P),\Phi(\mathcal EP)\bigr)
\tag{4}
$$
的两个分量都限制到原连续普通行
$\gamma_0,\ldots,\gamma_{k-1}$，
$\gamma_j=p^{-\lfloor6j/p\rfloor}w^j$。
若 $k_1\le k\le ps$，则这个 $2k\times N_D$ 原矩阵全列单射。
其全部 Smith 因子非零，并满足
$$
\boxed{
e\le\left\lceil\frac{b_D+13}{s}\right\rceil.
}
\tag{5}
$$
(5) 是同一个数值上界，不宣称联合矩阵与单输出矩阵的各指数相同。

## 2. 两观察的合流消元

取 $\pi^s=p$、$w=\pi z$，并对原列按
$r_{n,k}=13+A_n+k$ 作 R646/R657 的辅助分歧归一。
全 regular 高尾由 R618 严格落入 $\pi$，所以固定余类
$r=u+js$ 的两输出准确约化为
$$
\lambda_{n,k}
\left(
X^j e^{a(n+40)X},\
nX^j e^{a(n+40)X}
\right),\qquad X=z^s,
\tag{6}
$$
其中 $\lambda_{n,k}$、$a$ 为非零剩余域元素。补齐缺失低 $j$ 仍只用于证明独立性，不把它们加入来源。

考虑固定 $u$ 的一个可能线性关系。吸收原单位后，将两输出记为
$$
F(X)=\sum_{n,j}c_{n,j}X^je^{a(n+40)X},\qquad
G(X)=\sum_{n,j}n\,c_{n,j}X^je^{a(n+40)X}.
\tag{7}
$$
实际 $j$ 仍受原下帽和上帽约束；以下可将不存在的补齐系数取零。

假设
$$
F,G\in X^{H_u}k[[X]]
$$
在所用有限窗中成立。普通求导后，有准确低阶身份
$$
\boxed{
F'-a(G+40F)
=\sum_{n,j\ge1}j\,c_{n,j}X^{j-1}e^{a(n+40)X}
\in X^{H_u-1}k[[X]].
}
\tag{8}
$$
这里只从给出的两个输出求右侧，不把 $\mathcal E$ 视为某个已下降到物理像的自由算子。

(8) 的补齐族在第 $n$ 个节点有 $J_n(u)$ 个列，准确总数为
$$
T_u=C_u-N_u.
$$
若 $T_u>0$，其首 $T_u$ 个系数是完整合流 Vandermonde 单位矩阵。
由 $H_u-1\ge T_u$，所有 $j\,c_{n,j}$ 都为零。
由于 $1\le j\le J_n(u)<p$，得到全部 $j\ge1$ 的实际系数为零。
若 $T_u=0$，本来就没有这样的列。

剩下
$$
F(X)=\sum_n c_{n,0}e^{a(n+40)X}.
$$
至多 $N_u$ 个不同节点，而 $H_u\ge N_u$，
故首 $N_u$ 行的普通 Vandermonde 再迫全部 $c_{n,0}=0$。

这里有一个必须保留的特征 $p$ 端点：从 $F$ 的次数 $<H_u$ 求导时，只读取 (8) 的次数 $<H_u-1\le p-1$，即最高为 $p-2$。补齐尾族也只有 $T_u\le p-1$ 列。因此不在 $X^{p-1}$ 行使用
$D(e^{aX})=ae^{aX}$ 的未付截断，也不需要 $p!$。所有用到的阶乘以及 $j$ 均是单位。

故 (6) 在每个余类的首 $H_u$ 个 Gaussian 行上已全列独立。
这些行全位于 (2) 的连续前缀内。

## 3. 原格及 Smith 权完整返回

两个原输出都使用同一来源列权 $r_{n,k}$。
原 $\gamma_m$ 基上的行权仍为
$$
\omega_m=m-s\lfloor6m/p\rfloor,\qquad
1-s\le\omega_m\le s-1.
$$
因此把 R657 的 (17) 在两个输出上各复制一次，
得到一个整且有单位列满秩子式的辅助矩阵。

其整左逆作用于一个原 primitive Smith 向量，仍给
$$
se+1-s\le\max r_{n,k}=b_D+13.
$$
取整恰为 (5)。全部原 $q_n/g/U_0$ 高尾由同一缩放证明处理，
没有在特征零中把各余类强行拆成独立块。

这里的 $\Phi(\mathcal EP)$ 是 (4) 的第二输出。
即使 $P$ 已在某个旧首核中，本文也没有据此令第二输出为零；
需要共同消失时，必须把它明确列为前提。

## 4. 固定未正规双 jet 的二次界

固定特征零原函数
$$
F_P=G_0(w)P(t(w),\mathscr R(w)),\qquad
F_{\mathcal EP}=G_0(w)(\mathcal EP)(t(w),\mathscr R(w)).
$$
R657 已付改变辅助素数只改变 Gaussian 分解，不改变这两个实际级数。
由定理的非零有理子式，对任意非零原 $P$ 有
$$
\boxed{
\min\{\operatorname{ord}F_P,\operatorname{ord}F_{\mathcal EP}\}<k_1.
}
\tag{9}
$$
若第二输出恒零，其阶记为无穷，(9) 仍按原义成立。

现在选辅助素数 $p_D\equiv5\bmod6$，大于
$\max(101,f_D,25D/3)$ 且最小。固定模数的算术级数素数定理给
$$
p_D=\left(\frac{25}{3}+o(1)\right)D,\qquad
s_D=\left(\frac{25}{18}+o(1)\right)D.
\tag{10}
$$
与 R657 一样，只用固定模数六的定理；作者正文见 K. S. Kedlaya，
*Notes on analytic number theory*，§4.4，Theorem 4.12，
[原文](https://kskedlaya.org/ant/chap-primes-in-ap.html)。

$N_0=D+1$ 准确成立。由 $b_n=25n/6+O(1)$，
$$
\frac{C_0}{D}\longrightarrow
\sum_{j=0}^{3}\left(1-\frac j3\right)=2.
$$
故 $H_0/D\to1$，再由 (3) 得
$$
\boxed{
k_1=\left(\frac{25}{18}+o(1)\right)D^2.
}
\tag{11}
$$
所以固定原双 jet 的共同接触满足
$$
\boxed{
\sup_{P\ne0}
\min\{\operatorname{ord}F_P,\operatorname{ord}F_{\mathcal EP}\}
\le\left(\frac{25}{18}+o(1)\right)D^2.
}
\tag{12}
$$

这个常数是本篇“一次导出族补齐”估计在允许辅助比例中的最小主系数。具体地，若 $p_D/D\to\alpha\ge9/2$，则
$$
\frac{C_0}{D}\longrightarrow
C(\alpha):=\sum_{j\ge0}(1-\alpha j/25)_+,
$$
从而主系数是
$$
\frac{\alpha}{6}\max\{1,C(\alpha)-1\}.
\tag{13}
$$
当 $\alpha\ge25/3$ 时，$C(\alpha)\le2$，(13) 至少为 $25/18$。
在 $9/2\le\alpha\le25/3$ 的每个固定整数
$J=\lfloor25/\alpha\rfloor$ 区间内，(13) 为
$$
\frac{\alpha J}{6}-\frac{\alpha^2J(J+1)}{300},
$$
是凹二次式，最小值在端点。
内部端点 $\alpha=25/j$、$j=3,4,5$ 的值分别为
$$
\frac{25}{18},\quad \frac{25}{16},\quad \frac53;
$$
最左端 $\alpha=9/2$ 为 $69/40$。因此 (11) 的选择给本估计的最小值。
这不声称是原双 jet 的最优接触常数。

## 5. 原短截止仍未支付

(12) 是固定特征零空间的共同接触界。
它既不控制所选有理子式在其他素数处的分子，
也不把旧三块原像变成联合矩阵 (4) 的像。

特别在原低 $\ell$ 维数临界
$$
2n_0+\ell\sim\dim\mathcal W_D
\sim\frac{47}{24}D^2,\qquad \ell=o(D^2),
$$
有 $n_0\sim47D^2/48$，仍严格小于 $25D^2/18$。
故本文没有由接触界排除该临界首核，
更没有判定 R651 指定 $\mathcal G_P$ 或同一 $R$ 的 $\Psi_R$ 非零。
原两组十三行、完整 $P_{134}/U_0$、同一 $R$ 和下一位继续保留。
