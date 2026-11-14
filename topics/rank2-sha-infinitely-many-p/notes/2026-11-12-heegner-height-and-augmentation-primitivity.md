# 原 Heegner 点的跨素数不可除性与导数的增广层缺口

日期：2026-11-12。状态：§1–4 的高度界、原点不可除性和整代表预算已证明。
§5 给出一个精确的整群环检验，说明原点的 $p$-不可除性还缺哪一层；
它不是本题实际 Heegner 点的反例。没有得到无穷多个 $p$ 的 Sha 有限性。

沿用[单素数实际点判据](2026-11-12-one-prime-heegner-class-and-explicit-points.md)：
$E=E_{17}$，固定一次辅助虚二次域 $F$、有理模参数化
$\pi:X_0(N_E)\to E$，$P[\ell]\in E(F[\ell])$ 为原 Heegner 点，
$Y_\ell=\sum_{\tau\in\mathcal C_\ell}\tau D_\ell P[\ell]$。
记 $h_F$ 为 $F$ 的类数、$q=\ell+1$、$n=p^{M_\ell}$。
注意 $q,n$ 均随所选辅助素数而变，且 $n\mid q$。

## 1. 固定参数化下原点的高度为 $\asymp\log\ell$

存在只依赖于 $E,F,\pi$ 的正常数 $c_1,c_2,C$，使所有充分大的
惰性素数 $\ell\nmid N_ED$ 满足
$$
c_1\log\ell-C\le\widehat h(P[\ell])
                  \le c_2\log\ell+C.
\tag{1}
$$
特别地，$P[\ell]$ 对所有充分大的此类 $\ell$ 均为非挠点。

证明如下。令 $x_\ell\in X_0(N_E)$ 是相应 CM 点，
$j_\ell=j(x_\ell)$。它对应的椭圆曲线有 CM 阶
$\mathcal O_\ell=\mathbb Z+\ell\mathcal O_F$，并有次数 $\ell$ 的
同源到一个最大阶 CM 椭圆曲线：在格模型中将一个可逆
$\mathcal O_\ell$ 理想延拓为 $\mathcal O_F$ 理想即可。
最大阶端只有固定有限多个 $j$ 值。
Pazuki（2019）Theorem 1.1(1) 因而给
$$
h(j_\ell)\le C_F+12\log\ell.
\tag{2}
$$

另一方面，CM 阶高度差公式在 $\ell$ 惰性时准确为
$$
h_{\rm Fal}^{\rm stab}(\mathcal O_\ell)
-h_{\rm Fal}^{\rm stab}(\mathcal O_F)
=\left(\frac12-\frac1{\ell+1}\right)\log\ell.
\tag{3}
$$
例如可直接由 Barquero-Sanchez–Cadwallader–Cannon–Genao–Masri
（2017）Theorem 1.3 及其 $e(\ell)$ 定义得到：
$\chi_D(\ell)=-1$、$v_\ell(\ell)=1$ 使 $e(\ell)=-2/(\ell+1)$。
高度差不受稳定 Faltings 高度的整体常数规范影响。
Silverman 的模高度比较（Pazuki 同文式 (50) 给出显式版本）有
$h(j)\ge12h_{\rm Fal}^{\rm stab}-C_0$，因此
$$
h(j_\ell)\ge
\left(6-\frac{12}{\ell+1}\right)\log\ell-C_F'.
\tag{4}
$$

最后，$j:X_0(N_E)\to\mathbb P^1$ 与 $\pi:X_0(N_E)\to E$
都是固定非恒定有限态射。它们拉回的正次数除子都是 ample。
对两个 ample 除子 $A,B$，取足够大的固定整数 $r,s$，使
$rA-B$ 和 $sB-A$ 都为 ample；相应高度有统一下界，故
两种高度在全体代数点上互相控制到固定乘法、加法常数。
再用固定 $E$ 上 Weil 高度与典范高度的有界差，得到
$$
c\,h(j(x))-C\le\widehat h(\pi(x))
                     \le C' h(j(x))+C''.
$$
配合 (2)、(4) 即证 (1)。这里没有把单个复嵌入的 $j$ 大小
当作绝对高度，也没有把 Galois 迹的高度与原点高度混同。$\square$

## 2. 阿贝尔扩域的统一正下界

Baker（2003）Theorem 1.1 对固定 CM 曲线 $E/F$ 给出
一个有效正常数 $c_{E,F}>0$，满足
$$
R\in E(F^{\rm ab}),\ R\text{非挠}
\quad\Longrightarrow\quad
\widehat h(R)\ge c_{E,F}.
\tag{5}
$$
该定理不要求 CM 的全部自同态已在 $F$ 定义；也可先通过固定
扩域 $F(i)$ 使用它。Baker–Silverman（2004）Theorem 0.1
还给出一般阿贝尔簇版本。

环类域 $F[\ell]/F$ 是阿贝尔扩张，所以 (5) 对其中的所有非挠点
有同一个常数，不随 $[F[\ell]:F]=h_Fq$ 下降。
因此对任何实际点 $Z\in E(F[\ell])$，
$$
0<\widehat h(Z)<c_{E,F}p^{2M}
\quad\Longrightarrow\quad
Z\notin p^M E(F[\ell]).
\tag{6}
$$
证明：若 $Z=p^M R$，则 $R$ 非挠且在同一阿贝尔域中，
由 (5) 得 $\widehat h(Z)=p^{2M}\widehat h(R)\ge c_{E,F}p^{2M}$。

## 3. 对原 $P[\ell]$，Linnik 的量级确实足够

**命题。** 对单素数稿中所有充分大的 $p\in\mathcal P_F$，
可选一个 $\ell$，使它在 $F$ 和 $\mathbb Q(i)$ 中均惰性、
$\ell\equiv-1\pmod p$，且
$$
P[\ell]\notin pE(F[\ell]).
\tag{7}
$$

证明。$F\ne\mathbb Q(i)$，故两个二次特征独立。
取固定 $a\in(\mathbb Z/(68|D|))^\times$，使它在两个特征上的值
都是 $-1$。对 $p\nmid68D$，CRT 可同时指定
$$
\ell\equiv a\pmod{68|D|},\qquad \ell\equiv-1\pmod p.
$$
Linnik 定理给这条进程中的一个素数
$$
\ell\le C_F p^L
\tag{8}
$$
其中 $L$ 是固定绝对常数。无需使用最优的 $L$。
另一方面 $\ell+1$ 同时被 $4,p$ 整除，故 $\ell\ge4p-1$，
所以 $\ell\to\infty$。
由 (1)，$P[\ell]$ 非挠且
$$
\widehat h(P[\ell])\le C_1\log p+C_2<c_{E,F}p^2
$$
对充分大的 $p$ 成立。应用 (6) 的 $M=1$ 即得 (7)。$\square$

这是真实 Heegner 点的跨 $p$ 不可除性，输入域 $F$ 和参数化均固定。
但单素数 Sha 判据要求的是 **$Y_\ell$** 不可除，尚不能将 (7)
移到 $D_\ell P[\ell]$ 或其类群和上。

## 4. 对实际导数，现有高度预算不够

典范高度的平方根在模掉挠子的实向量空间上是范数；Galois 保持它。
由 $\sum_{j=1}^{q-1}j=q(q-1)/2$ 得到准确上界
$$
\widehat h(Y_\ell)
\le\left(\frac{h_Fq(q-1)}2\right)^2\widehat h(P[\ell])
\ll_{E,F,\pi}q^4\log\ell.
\tag{9}
$$
若想仅以这项上界和 (6) 证明导数不可除，必须使
$Cq^4\log\ell<c_{E,F}n^2$。
但 $n=p^{M_\ell}\mid q$，且这里甚至 $4n\mid q$。
所以该上界除以 $n^2$ 仍至少有 $q^2\log\ell$ 的量级；
对任何趋于无穷的辅助素数选择都不能得到所需的小量。
这是这组**上下界的证明能力**不足，并不是断言实际
$\widehat h(Y_\ell)$ 必有 $q^4\log\ell$ 的下界。
将 (8) 的 Linnik 指数改善为任意固定指数，也不改变这个比较。

可以合法地将群环系数模 $n$ 化到平衡区间。
记 $r_n(j)\in[-(n-1)/2,(n-1)/2]$ 为 $j$ 的平衡剩余，置
$$
Z_{\ell,p}=\sum_{\tau\in\mathcal C_\ell}
 \sum_{j=0}^{q-1}r_n(j)\tau\sigma_\ell^jP[\ell].
\tag{10}
$$
这是同一域中的实际点，且 $Y_\ell-Z_{\ell,p}\in nE(F[\ell])$。
每个剩余出现 $q/n$ 次，故
$$
\sum_{j=0}^{q-1}|r_n(j)|=\frac{q(n^2-1)}{4n},
\qquad
\widehat h(Z_{\ell,p})
\le\left(\frac{h_Fq(n^2-1)}{4n}\right)^2\widehat h(P[\ell]).
\tag{11}
$$
它将原始系数上界改善到 $O(q^2n^2\log\ell)$，但除以 $n^2$
仍为 $O(q^2\log\ell)$，没有达到 (6)。

不能把 $Y_\ell/q$ 或 $Y_\ell/n$ 当作已在 $E(F[\ell])$ 中的点
直接使用 (5)。在张量 $E(F[\ell])\otimes\mathbb Q$ 中除法虽然存在，
所得向量不满足 (5) 的整点归属前提；证明这种归属恰是原问题。

### 4.1 范数为零本身没有小导数算子界

在本节的额外 CM 惰性条件下，$a_\ell=0$，所以
$N_{G_\ell}P[\ell]=0$。在一个复特征 $\sigma\mapsto\zeta\ne1$
上，群环恒等式 $(\sigma-1)D=q-N$ 给
$$
D(\zeta)=\frac q{\zeta-1}.
\tag{12}
$$
在 $\zeta=e^{2\pi i/q}$ 的二维实正交表示中，其算子范数为
$q/(2\sin(\pi/q))\asymp q^2$，尽管 $N=0$。
因此仅用范数零关系，不能把通用 $q^2$ 范数增长改成一个统一常数。
这是精确的表示论界；没有宣称实际 Heegner 点实现这个极端。

## 5. 原点不可除与所需增广原始性差一层

下面的局部整格模型将缺口写得很具体。
令 $G=C_p=\langle\sigma\rangle$，并令
$$
\mathcal O=\mathbb Z_p[\zeta_p],\qquad
u=\zeta_p-1,\qquad \sigma\cdot x=\zeta_p x.
$$
则 $N_G=0$、$p\mathcal O=u^{p-1}\mathcal O$，并且
$$
D=\sum_{j=1}^{p-1}j\sigma^j
\quad\text{作用为}\quad
\frac p{\zeta_p-1}=\frac pu.
\tag{13}
$$
所以对任何 $x\in\mathcal O$，
$$
Dx\notin p\mathcal O
\quad\Longleftrightarrow\quad x\notin u\mathcal O.
\tag{14}
$$
而 $x\notin p\mathcal O$ 只给 $v_u(x)<p-1$。
例如 $x=u$ 非零且不属于 $p\mathcal O$，但 $Dx=p\in p\mathcal O$。
这个模型还满足与实际 Heegner 点相同的范数零关系，
故 (7) 与该关系在逻辑上不足以推出导数不可除。

实际剩余条件是相应 $p$-Sylow/增广分量中的原始性，
还要保留 $\mathcal C_\ell$ 的和。不能把一个非零原点模 $p$
自动放到该分量的最底层。
本模型没有断言实际点等于 $u$，也不排除实际几何还提供
更强的增广原始性定理；它精确指出高度方法目前没有给出的那一步。

固定有限多个 $\ell$ 不能绕开这个问题：这些 $\ell$ 支持的 $p$
都整除固定非零整数的乘积 $\prod_\ell(\ell+1)$，故只有有限个。
下一步必须控制随 $p$ 变化的实际导出点，不能只增加固定辅助点的
高度精度或改进最小素数上界。

## 来源

- M. H. Baker（2003），*Lower bounds for the canonical height on elliptic
  curves over abelian extensions*，International Mathematics Research Notices
  **2003**(29), 1571–1589，Theorem 1.1；
  [作者预印本](https://arxiv.org/pdf/math/0212132)。
- M. Baker、J. H. Silverman（2004），*A lower bound for the canonical height
  on abelian varieties over abelian extensions*，Mathematical Research Letters
  **11**, 377–396，Theorem 0.1；
  [全文](https://arxiv.org/pdf/math/0312393)。
- F. Pazuki（2019），*Modular invariants and isogenies*，International Journal
  of Number Theory **15**(3), 569–584，Theorem 1.1(1)、式 (50)；
  [作者 v5](https://arxiv.org/pdf/1611.01094)，
  DOI 10.1142/S1793042119500295。
- A. Barquero-Sanchez、L. Cadwallader、O. Cannon、T. Genao、R. Masri（2017），
  *Faltings heights of CM elliptic curves and special Gamma values*，
  Research in Number Theory **3**, article 13，Theorem 1.3 及 §1 的 $e(p)$；
  [正式全文](https://link.springer.com/article/10.1007/s40993-017-0077-7)。
- T. Xylouris（2011），*On the least prime in an arithmetic progression
  and estimates for the zeros of Dirichlet L-functions*，Acta Arithmetica
  **150**, 65–91，Introduction 的 Linnik 定理；
  [正式全文](https://www.impan.pl/shop/en/publication/transaction/download/product/83078)。
  本文只需存在一个有效绝对指数，不使用任何未核的最优数值。
