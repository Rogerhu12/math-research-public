# 周期平移、极点分支与整个 germ 的数域

日期：2026-11-12。**状态：以下平移递推、局部次数及无周期命题已证明；尚未构造可供 Herblot 同时使用的额外算术 germ。**

本篇继续同一解析映射的多 germ 路线。它区分一个代数函数值、一个代数留数，
以及定义在固定数域上的整个形式曲线。后者才是所需输入。

## 1. 固定对象与所需条件

取
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
f=34(1+i),\quad b=2+i,\quad \Lambda=\Omega\mathbb Z[i].
$$
令 $\ell$ 为此前的 $\delta\log\Phi$，也可以取已经证明非零的
$\mu_4$ 不变部分 $\ell_0=(\ell+\ell\circ[i])/2$。
本篇两个选择均适用，只需下列性质：

- $\ell\in K(E)$ 非常数，在 $O$ 正则且至少二阶消失；
- 全部极点都是简单极点，包含在 $S^*=E[f]$ 中；
- $[b]$ 在 $S^*$ 上为双射。

令 $h(z)=\ell(\operatorname{Exp}_E z)$。固定 $m\ge1$，写
$$
F(z)=\sum_{n\ge0}C_n h(z/b^{m+n}),
\qquad C_n=\binom{m+n-1}{n}.
\tag{1.1}
$$
此级数在避开其离散极点集的紧集上正常收敛，并给出
$$
(\sigma_b-1)^mF=h,\qquad \sigma_bF(z)=F(bz),\qquad F(0)=0.
\tag{1.2}
$$
前篇已证明 $F$ 不代数于 $\overline K(E)$，以及
$z\mapsto(\operatorname{Exp}_Ez,F(z))$ 的复增长阶数至多为二。
这些结论对 $b=2+i$ 仍成立，不要求 $b\equiv1\pmod f$。

Herblot Definition 5.4 要求同一参数曲线上的点 $w_j$ 两两不同，
**没有要求像闭点 $x_j$ 两两不同**。因此两个不同周期处即使给出同一个函数值，
只要整个 germ 满足所需定义域和算术条件，原则上仍可以计入。
相反，$b^n\cdot0=0$ 一直是同一个参数点，不能重复计数。

在 Herblot Theorem 6.1 中，还须验证每个 germ 定义在其指定数域上，
并具有 $\alpha_j$-arithmetic 的全部 jet 评价界；仅有 $F(w_j)$ 代数不够。
准确阈值见此前 `2026-11-12-herblot-trace-curve-threshold.md`。

## 2. 非零周期处的精确 Taylor 公式

取非零周期 $\lambda=\Omega\eta$，$\eta\in\mathbb Z[i]\setminus\{0\}$，并置
$$
P_n=\operatorname{Exp}_E(\lambda/b^{m+n}).
$$
这些是 $b$-primary 扭点。因 $(b,f)=1$，它们与 $E[f]$ 的交集只有 $O$；
而 $\ell$ 在 $O$ 正则。因此 $F$ 在每个周期处正则。

对任意固定 $k\ge0$，正常收敛允许逐项微分，得到
$$
\boxed{\quad
\frac{F^{(k)}(\lambda)}{k!}
=\sum_{n\ge0}C_n b^{-(m+n)k}
\frac{(\delta^k\ell)(P_n)}{k!}.
\quad}
\tag{2.1}
$$
右端每一项都代数。但这些项并不落在一个预先固定的数域中。
下面给出本例的具体次数下界，而非只指出扭点层数在增加。

### 2.1 固定五进处的 Eisenstein 证明

令 $\mathfrak b=(2+i)$。曲线在 $5$ 处有良好普通约化，
$K_{\mathfrak b}=\mathbb Q_5$。取 Hecke 值 $\pi=\psi(\mathfrak b)$，
它是 $b$ 的一个单位倍数。因此 $E[b^N]=E[\pi^N]$。

严格 Lubin–Tate 坐标把形式群的 $[\pi]$ 写成
$$
g(T)=\pi T+T^5.
$$
该坐标定义在 $\mathbb Z_5$ 上，坐标和逆坐标均保持有限扩张中的点域。
可用 Coates–Wiles 1978，§1，p.5，式 (5) 前的严格同构陈述；
R24 使用了同一原始结果。

一个本原 $\pi^N$-division 坐标是
$$
Q_N(T)=\frac{g^{\circ N}(T)}{g^{\circ(N-1)}(T)}
=\pi+\bigl(g^{\circ(N-1)}(T)\bigr)^4
\tag{2.2}
$$
的根。此多项式首一、次数 $4\cdot5^{N-1}$，
模 $\pi$ 等于 $T^{4\cdot5^{N-1}}$，常数项恰为 $\pi$。
所以它是 Eisenstein 多项式。
所有 $E[\pi^N]$ 点都属于这个连接形式部分，故每个本原点满足
$$
[K_{\mathfrak b}(P):K_{\mathfrak b}]=4\cdot5^{N-1},
\qquad [K(P):K]\ge4\cdot5^{N-1}.
\tag{2.3}
$$

令 $s=v_b(\eta)$。当 $m+n>s$ 时，$P_n$ 的精确阶理想为 $(b^{m+n-s})$。
对固定 $k$，有理函数 $R_k=\delta^k\ell$ 仍非常数：
其在一个简单极点的导数有非零的 $k+1$ 阶主部。
设有限态射 $R_k:E\to\mathbb P^1$ 的次数为 $e_k$。
纤维次数给出
$$
[K(P_n):K(R_k(P_n))]\le e_k.
$$
结合 (2.3)，得到
$$
\boxed{\quad
[K(R_k(P_n)):K]\ge
\frac{4\cdot5^{m+n-s-1}}{e_k}.
\quad}
\tag{2.4}
$$
式 (2.1) 中非零的 $K$ 系数 $C_nb^{-(m+n)k}/k!$ 不改变这个次数。
因此对每个固定导数阶数 $k$，其逐项代数求和法本身使用无界次数的数域。

**边界。** (2.4) 不证明无限和的值超越，也不证明它不在某个固定数域中。
无界次数的项可以发生特殊消去。它证明的是：
“每项代数，因此整个平移 germ 在一个数域上”不是一个有效的下降论证。
需要另有控制整个无穷和的恒等式。

## 3. 所有倍乘周期 germ 的准确递推

固定上述 $\lambda$，定义原点附近的解析 germ
$$
H_n(z)=F\bigl(b^n(z+\lambda)\bigr)-F(b^nz),\qquad n\ge0.
$$
把 (1.2) 分别用在 $b^n(z+\lambda)$ 和 $b^nz$。
因为 $b^n\lambda\in\Lambda$ 且 $h$ 为椭圆函数，右端相消，所以
$$
\Delta_n^mH_n=0,
\qquad \Delta_nH_n=H_{n+1}-H_n.
\tag{3.1}
$$
令 $G_{\lambda,j}=\Delta_n^jH_n|_{n=0}$。有限差分恒等式给
$$
H_n(z)=\sum_{j=0}^{m-1}\binom njG_{\lambda,j}(z).
$$
换元 $z\mapsto z/b^n$，得到同一函数的精确平移式
$$
\boxed{\quad
F(z+b^n\lambda)
=F(z)+\sum_{j=0}^{m-1}\binom nj
G_{\lambda,j}(z/b^n).
\quad}
\tag{3.2}
$$
特别地，$F(b^n\lambda)$ 是 $n$ 的次数至多 $m-1$ 的多项式，
其系数是未知数 $G_{\lambda,j}(0)$。
当 $m=1$ 时这些函数值相同，但不同参数点处的整个 germ 一般不同。

若 $J_k(n)=[z^k]F(z+b^n\lambda)$，则也可以写成
$$
(b^kE_n-1)^mJ_k(n)=h_k,
\qquad E_nJ_k(n)=J_k(n+1),
\tag{3.3}
$$
其中 $h(z)=\sum h_kz^k$。
对 $k>0$，$J_k(n)-F_k$ 是 $b^{-nk}$ 乘一个次数至多 $m-1$ 的多项式；
对 $k=0$，$h_0=0$，得到通常的多项式解。

这说明递推所需的未知输入恰是最初 $m$ 个平移 germ，或等价的
$G_{\lambda,0},\ldots,G_{\lambda,m-1}$。
式 (3.2) 没有证明这些解析函数的全部系数属于某个固定数域，
也没有给出它们的全部有限位 jet 范数界。
即使最初几个函数值已知代数，也不能删除后面这两个条件。

## 4. 同一函数没有任何非零椭圆周期

**命题 4.1。** 若 $\lambda\in\Lambda$ 且 $F(z+\lambda)=F(z)$，则 $\lambda=0$。

**证明。** 在 $S^*=E[f]$ 上置
$$
r(s)=\operatorname{Res}_s\ell\,\omega_E,
$$
并在非极点处置零。这个有限向量非零。因 $[b]$ 置换 $S^*$ 且 $|b|>1$，
算子 $1-b^{-1}[b]^*$ 可逆，故存在 $s\ne O$，使
$$
L_s=\sum_{j\ge0}b^{-j}r([b]^js)\ne0.
\tag{4.1}
$$
取 $z_s=\Omega\eta/f$ 为 $s$ 的复对数，用 CRT 使 $b\nmid\eta$。
在 $z_n=b^{m+n}z_s$ 处，(1.1) 只有前 $n+1$ 项可能有极点。
总留数为
$$
A_n=b^m\sum_{j=0}^n C_jb^j r([b]^{n-j}s),
\qquad
\frac{A_n}{b^{m+n}C_n}\longrightarrow L_s\ne0.
\tag{4.2}
$$
最后的极限由 $C_{n-j}/C_n\to1$、$0\le C_{n-j}/C_n\le1$
以及几何级数支配收敛得到。特别地，$|A_n|\to\infty$。

现在假设非零 $\lambda=\Omega q$ 为 $F$ 的周期，令 $s_0=v_b(q)$。
当 $m+n>s_0$ 时，
$$
v_b(b^{m+n}\eta+fq)=s_0.
$$
第 $j$ 项在 $z_n+\lambda$ 有极点的必要条件是
$$
b^{m+j}\mid b^{m+n}\eta+fq,
$$
故只能有 $m+j\le s_0$。
这是一组与 $n$ 无关的有限指标。
每一项的留数是 $C_jb^{m+j}$ 乘有限集合中的一个 $r(s')$，
所以 $F$ 在 $z_n+\lambda$ 处的留数一致有界。
周期性却要求它等于 $A_n$，与 (4.2) 矛盾。证毕。

这进一步说明，在一个扭点处重新解同一形式差分方程，不会自动得到
原来 $F$ 的平移 germ。例如令 $[b]P_0=P_0$，取一个复对数 $z_0$，
使 $\lambda=(b-1)z_0\in\Lambda\setminus\{0\}$。
当 $m=1$ 且有关 germ 正则时，如果 $F(z+z_0)$ 同时满足局部方程
$$
F(bz+z_0)-F(z+z_0)=h(z+z_0),
$$
则与全局方程相减得到
$F(bz+bz_0)=F(bz+z_0)$，使 $\lambda$ 成为非零周期，矛盾。
若 $h(z_0)\ne0$，常数项本身已经排除任何正则局部逆像。
对 $m>1$，局部和全局方程仍含不同的周期平移项；本篇不把这个
$m=1$ 的短反证未经证明地扩展成全部高阶情形。

## 5. 极点给代数像与代数切线，但尚不给整个算术 germ

式 (4.2) 的 $z_n$ 给出另一种候选，因为
$$
\bigl(\operatorname{Exp}_Ez_n,F(z_n)\bigr)
=([b]^{m+n}s,\infty)
$$
总是一个代数点。留数 $A_n$ 也属于固定域 $K(E[f])$。
当 $n$ 足够大时 $A_n\ne0$，写
$$
F(z_n+u)=\frac{A_n}{u}+B_n+B_{n,1}u+\cdots.
$$
在 $\mathbb P^1$ 的无穷远坐标中，图像 germ 为
$$
\frac1{F(z_n+u)}=\frac{u}{A_n}
-\frac{B_n}{A_n^2}u^2+\cdots.
\tag{5.1}
$$
因此代数留数只控制第一阶切线；下一阶已经涉及未知正则部分 $B_n$。

这些正则部分也可精确归为有限个未知解析 germ。
在 $z=b^{m+n}(z_s+v)$ 处，(1.1) 的尾项是
$$
\sum_{k\ge1}C_{n+k}h((z_s+v)/b^k).
\tag{5.2}
$$
因 $C_{n+k}$ 是 $n+k$ 的次数 $m-1$ 的多项式，(5.2) 是
$$
U_j(v)=\sum_{k\ge1}k^j h((z_s+v)/b^k),
\qquad 0\le j\le m-1,
\tag{5.3}
$$
的有限线性组合，其系数是 $n$ 的有理多项式。
各 $U_j$ 在 $v=0$ 附近正则并正常收敛，因为 $b\nmid\eta$。
前面有限项的 Laurent 系数都在固定域 $K(E[f])$ 中；
未知输入恰落在这些尾项 germ 中。

式 (5.3) 的取值点为 $\operatorname{Exp}_E(z_s/b^k)$。
乘以 $f$ 后是本原 $b^k$-division 点，所以其点域次数仍至少为
$4\cdot5^{k-1}$。固定有理函数的取值次数也由 (2.4) 的同一有限纤维论证增长。
这仍不是尾和超越的证明；它再次精确标出所缺的数域下降。

Herblot 并不因这些极点的代数像只落在有限集合里而禁止计数。
若能证明无限多个不同的 $z_n$ 上，整个 germ 均定义在一个固定数域 $L$ 上，
且都有同一有限算术常数 $\alpha\le A$，那么对任意有限子集可在
$(E\times\mathbb P^1)_L$ 视为 $\mathbb Q$-簇后应用该定理。
各闭点次数为 $[L:\mathbb Q]$，Zariski 维数为二，增长阶数至多二，故
$$
\#J\le4A[L:\mathbb Q].
\tag{5.4}
$$
任意大的有限子集会矛盾。这说明上述统一输入不可能同时成立，
但现有公式没有指出是数域条件还是算术预算条件失败，亦未构造出
足以超过阈值的一组可用 germ。

## 6. 分布关系目前控制的对象

椭圆函数或椭圆单位的同源范数、迹分布关系对完整有限纤维求和。
本篇 (2.1)、(5.3) 使用的是逐层选定的一支除法点。
一条完整纤维的迹是代数数，并不使各支的无限尾和分别落在同一个数域。

更直接地，$F$ 由命题 4.1 没有非零格周期，因此它不是 $E$ 上的单值函数。
在 $E[b]$ 上写 $\sum_{Q}F(P+Q)$，若未同时指定各个复对数的提升，
甚至不是与选择无关的迹。改变提升正好引入第 3 节的未知周期平移 germ。
先对已知有理函数 $h$ 作完整有限迹，可以产生另一条已知形式级数；
这与证明它等于同一解析映射在一个额外参数点处的 germ 是两件不同的事。

目前多 germ 路线的具体缺口是：对至少一个有限组非零周期或扭点提升，
控制 (3.2) 的初始 germ，或等价地控制 (5.3) 的全部 Taylor 系数及其
统一有限位 jet 范数。仅控制函数值、留数或任何固定阶 jet，均没有完成这一步。

## 来源

- M. Herblot，*Algebraic points on meromorphic curves*，
  [作者原文](https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf)，
  [arXiv:1204.6336](https://arxiv.org/abs/1204.6336)，
  Definition 2.4–2.5、Definition 5.4–5.5、Theorem 6.1；已逐项读取。
- J. Coates 与 A. Wiles，*On $p$-adic $L$-functions and elliptic units*，
  J. Austral. Math. Soc. Ser. A **26** (1978)，1–25，§1，p.5，
  [DOI](https://doi.org/10.1017/S1446788700011459)；严格 Lubin–Tate 坐标亦在 R24 核过。
- 本课题 `2026-11-12-additive-cm-difference-inverse.md`、
  `2026-11-12-inert-weighted-order-sum.md`、
  `2026-11-12-herblot-trace-curve-threshold.md`。
- 本篇的平移递推、Eisenstein 次数、无周期证明及尾项分解均给出完整推导。
