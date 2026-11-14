# R2：resolvent 半空间内部不存在可直接提取的不变子空间

**状态：已证明的中间结论；不声称新颖；没有解决完整 Hilbert ISP。**

日期：2026-11-12。会话：Astra-ISP-b382c564；并行推导：defect-route。

本条把“小秩一扰动产生不变半空间”的一个标准构造中的障碍写成精确命题。可以使扰动任意小，而构造出的每个半空间里面甚至没有原算子的非零不变线性子空间。与此同时，这些半空间的正交投影强收敛于零。因此，“在所得几乎不变半空间中再取一个真不变子空间”以及“直接令扰动趋零”两种推理均不能由这个构造完成。

## 1. 命题

设 $H$ 为可分无穷维复 Hilbert 空间，$T\in B(H)$，并设

$$
\lambda _0\in\partial\sigma(T)\setminus\sigma_p(T).
$$

存在单位向量 $e$、两两不同的 $\lambda_n\in\rho(T)$、单位向量 $x_n$ 和实数 $a_n>0$，满足：

1. $\lambda_n\to\lambda_0$，$a_n\le 2^{-n}$，且

   $$
   x_n=a_n(\lambda_nI-T)^{-1}e,
   \qquad Tx_n=\lambda_nx_n-a_ne.
   \tag{1.1}
   $$

2. $(x_n)$ 为 Riesz 序列，可以使用以下统一界：

   $$
   \frac12\sum_n|c_n|^2
   \le\left\|\sum_nc_nx_n\right\|^2
   \le\frac32\sum_n|c_n|^2.
   \tag{1.2}
   $$

   $E=\overline{\operatorname{span}}\{x_n:n\ge1\}$ 是半空间，即维数和余维数均无限，并且

   $$\operatorname{dist}(e,E)\ge\frac12.\tag{1.3}$$

3. **不存在非零的 $T$-不变线性子空间 $M\subset E$，即使不要求 $M$ 闭。**

4. 对每个 $m\ge1$，令

   $$E_m=\overline{\operatorname{span}}\{x_n:n\ge m\}.$$

   则 $E_m$ 仍为半空间，存在值域为 $\mathbb Ce$ 的秩一算子 $F_m$，使

   $$
   (T+F_m)E_m\subset E_m,
   \qquad
   \|F_m\|\le\sqrt2\left(\sum_{n\ge m}a_n^2\right)^{1/2}\longrightarrow0.
   \tag{1.4}
   $$

   然而，正交投影 $P_m=P_{E_m}$ 满足 $P_m\to0$（强算子拓扑）。

5. 若闭子空间 $Y\subset E$ 含有某个固定的 $x_j$，则其原算子不变性缺陷有严格下界：

   $$
   \|(I-P_Y)TP_Y\|
   \ge a_j\operatorname{dist}(e,E)
   \ge a_j/2>0.
   \tag{1.5}
   $$

   因而，任何使 $Y$ 成为 $T+F$-不变子空间的 $F$ 都满足 $\|F\|\ge a_j/2$。

本命题的假设涵盖没有特征值的算子，因为复 Banach 空间上有界算子的谱非空紧，而谱边界非空。这里的结论并不否定 ISP：$E$ 自身不是 $T$-不变子空间；$T$ 在整个 $H$ 上可能有很多不变子空间，它们只是不能全部落在这个 $E$ 里。

## 2. 选择 resolvent 向量，并保证半空间和横向分离

从边界点的定义，取两两不同的 $\nu_j\in\rho(T)$ 趋于 $\lambda_0$。由于

$$
\|(\nu_jI-T)^{-1}\|
\ge \operatorname{dist}(\nu_j,\sigma(T))^{-1}
\ge |\nu_j-\lambda_0|^{-1},
$$

这些 resolvent 的范数无界。一致有界原理给出一个非零向量，在该向量上的 resolvent 范数无界。将它归一化为 $e$，再抽子列，可以设

$$
r_j=\|(\nu_jI-T)^{-1}e\|\longrightarrow\infty.
$$

令

$$
v_j=r_j^{-1}(\nu_jI-T)^{-1}e,\qquad b_j=r_j^{-1}.
$$

则 $\|v_j\|=1$，并有

$$
(T-\lambda_0I)v_j=(\nu_j-\lambda_0)v_j-b_je\longrightarrow0.
\tag{2.1}
$$

断言 $v_j\rightharpoonup0$。事实上，单位球中任一子列有弱收敛子子列；若其弱极限为 $v$，由 (2.1) 得 $(T-\lambda_0I)v=0$。因为 $\lambda_0$ 不是特征值，所以 $v=0$。若原序列不弱收敛于零，会有一个固定连续线性泛函在某子列上绝对值有正下界，再取上述弱收敛子子列便矛盾。

逐项抽取子列后，可以同时安排

$$
b_j\le2^{-j},\qquad
|\langle v_j,e\rangle|\le2^{-j-3},\qquad
|\langle v_i,v_j\rangle|\le2^{-i-j-2}\quad(i\ne j).
\tag{2.2}
$$

每一步只约束有限个已经选出的向量，因此弱零性足以满足所有内积条件；$r_j\to\infty$ 保证第一项。

对有限复数列 $(c_j)$，非对角 Gram 项满足

$$
\left|\sum_{i\ne j}c_i\overline{c_j}\langle v_i,v_j\rangle\right|
\le\frac14\left(\sum_j2^{-j}|c_j|\right)^2
\le\frac1{12}\sum_j|c_j|^2.
$$

所以整个 $(v_j)$ 是 Riesz 序列，并满足比 (1.2) 更强的 $11/12,13/12$ 界。特别地，映射

$$J_0:\ell^2(\mathbb N)\longrightarrow H,\qquad J_0(c)=\sum_jc_jv_j$$

有闭值域且有界下限。

现在保留偶数项：

$$
x_n=v_{2n},\qquad\lambda_n=\nu_{2n},\qquad a_n=b_{2n}.
$$

这些向量满足 (1.1)、(1.2) 和 $0<a_n\le2^{-2n}\le2^{-n}$。偶数坐标子空间在 $\ell^2$ 中闭，因此 $E$ 闭且无限维。奇数项 $v_{2k-1}$ 在 $H/E$ 中的像线性无关：如果其一个有限线性组合落在 $E$，对 $J_0$ 的值域使用唯一的 $\ell^2$ 坐标，奇数坐标必须全为零。故 $E$ 的余维数无限。

最后，对于 $u=\sum_nc_nx_n\in E$，由 (1.2)、Cauchy–Schwarz 和 (2.2)，

$$
|\langle u,e\rangle|
\le\left(\sum_n|c_n|^2\right)^{1/2}
     \left(\sum_n|\langle x_n,e\rangle|^2\right)^{1/2}
\le\sqrt2\,\|u\|
     \left(\sum_{j\ge1}2^{-2j-6}\right)^{1/2}.
$$

右端的平方系数为 $2/192=1/96<1/4$。因此 $\|P_Ee\|<1/2$，从而 $\operatorname{dist}(e,E)>\sqrt3/2$；这当然蕴含 (1.3)。

注意 $\lambda_0\notin\{\lambda_n:n\ge1\}$，因为前者属于 $\sigma(T)$，后者属于 $\rho(T)$。抽子列后仍两两不同，而且唯一的聚点仍是 $\lambda_0$。

## 3. $E$ 内不存在非零原算子不变子空间

令 $J:\ell^2(\mathbb N)\to E$ 为 $Jc=\sum_nc_nx_n$。它是有界同构。定义

$$
D=J\operatorname{diag}(\lambda_n)J^{-1}\in B(E),\qquad
\varphi(Jc)=\sum_{n\ge1}a_nc_n.
$$

$D$ 有界，因为 $(\lambda_n)$ 有界；$\varphi$ 有界，因为 $(a_n)\in\ell^2$，且 $J^{-1}$ 有界。由 (1.1)，先在有限线性组合上、再由连续性在整个 $E$ 上，有

$$Tu=Du-\varphi(u)e\qquad(u\in E).\tag{3.1}$$

设 $M\subset E$ 是 $T$-不变线性子空间。若 $u\in M$，则 $Tu\in M\subset E$ 且 $Du\in E$；由 $e\notin E$ 和 (3.1) 得

$$\varphi(u)=0,\qquad Tu=Du\in M.$$

所以 $DM\subset M$。归纳可知，对每个 $k\ge0$，

$$D^ku=T^ku\in M,\qquad\varphi(D^ku)=0.\tag{3.2}$$

这说明此处的 $D$ 的幂与 $T$ 的迭代相等只是在 $M$ 内得出的，未将 $D$ 错当成 $T$ 在整个 $E$ 上的限制。

固定 $u=Jc\in M$。令 $d_n=a_nc_n$。因为 $a,c\in\ell^2$，有

$$\sum_n|d_n|\le\|a\|_2\|c\|_2<\infty.\tag{3.3}$$

设

$$K=\{\lambda_0\}\cup\{\lambda_n:n\ge1\},\qquad\Omega=\mathbb C\setminus K.$$

$K$ 紧且可数，$\Omega$ 连通。为直接验证后一点，对任意 $z,w\in\Omega$，选择不在所有经过 $z$ 或 $w$ 与 $K$ 中一点的可数条直线上的点 $q$；这样的 $q$ 存在，例如任意圆周除去可数集仍有点。折线路径 $z\to q\to w$ 避开 $K$。

由 (3.3)，级数

$$g(z)=\sum_{n\ge1}\frac{d_n}{z-\lambda_n}\tag{3.4}$$

在 $\Omega$ 的每个紧子集上一致绝对收敛，故 $g$ 在 $\Omega$ 上全纯。若 $|z|>\sup_n|\lambda_n|$，可用一致收敛的几何级数与 (3.3) 交换求和，得到

$$
g(z)=\sum_{k\ge0}z^{-k-1}\sum_nd_n\lambda_n^k
    =\sum_{k\ge0}z^{-k-1}\varphi(D^ku)=0.
$$

由连通域上的恒等定理，$g\equiv0$ 于 $\Omega$。

固定一个 $n$。由于 $\lambda_n$ 两两不同且唯一聚点为 $\lambda_0\ne\lambda_n$，可取以 $\lambda_n$ 为中心的一个小圆盘，不含 $K$ 的其他点。在这个圆盘内，(3.4) 中除第 $n$ 项外的级数全纯，理由仍是 (3.3) 和其他分母的一致正下界。因此 $g$ 在 $\lambda_n$ 的留数正是 $d_n$。但 $g$ 在去心圆盘上恒为零，所以 $d_n=0$。

这对每个 $n$ 成立；又因每个 $a_n>0$，故每个 $c_n=0$，进而 $u=0$。于是 $M=\{0\}$。整个论证不曾使用 $M$ 闭。

## 4. 任意小秩一扰动和零强极限

由于 $J$ 是同构，$E_m=J\ell^2(\{m,m+1,\ldots\})$ 闭且无限维；其余维数至少是 $E$ 的无限余维数。

定义

$$F_mh=\varphi(P_mh)e\qquad(h\in H).$$

对于 $u=\sum_{n\ge m}c_nx_n\in E_m$，

$$
|\varphi(u)|
\le\left(\sum_{n\ge m}a_n^2\right)^{1/2}\|c\|_2
\le\sqrt2\left(\sum_{n\ge m}a_n^2\right)^{1/2}\|u\|.
$$

$\|e\|=\|P_m\|=1$，故得到 (1.4) 的范数界。由于 $\varphi(x_m)=a_m\ne0$，$F_m$ 的秩恰为一。对 $n\ge m$，

$$ (T+F_m)x_n=\lambda_nx_n,$$

所以由有限线性组合的稠密性和算子的有界性，$E_m$ 是 $T+F_m$ 的不变半空间。

另一方面，$E_m$ 递减且 $\bigcap_mE_m=\{0\}$，这由唯一的 $\ell^2$ 坐标立即成立。正交投影于是强收敛于零：若 $k\ge m$，则

$$\|P_mh-P_kh\|^2=\|P_mh\|^2-\|P_kh\|^2.$$

右端随 $m,k\to\infty$ 趋零，所以 $(P_mh)$ 为 Cauchy 序列；其极限属于每一个 $E_m$，因而为零。

## 5. 固定保留一个 resolvent 向量的正下界

若 $x_j\in Y\subset E$ 且 $Y$ 闭，则 $\|x_j\|=1$，$P_Yx_j=x_j$，并由 (1.1) 得

$$
(I-P_Y)TP_Yx_j
=(I-P_Y)(\lambda_jx_j-a_je)
=-a_j(I-P_Y)e.
$$

因此

$$
\|(I-P_Y)TP_Y\|
\ge a_j\operatorname{dist}(e,Y)
\ge a_j\operatorname{dist}(e,E)
\ge a_j/2.
$$

如果 $(T+F)Y\subset Y$，则

$$ (I-P_Y)TP_Y=-(I-P_Y)FP_Y,$$

左边不超过 $\|F\|$，从而得到扰动范数的下界。

这排除了在同一个已构造的 $E$ 中一直保留固定 $x_j$、同时仅靠删除尾部或改变子空间使扰动趋零的办法。它不排除更换整个 Riesz 系统、使用非尾部的全新半空间族，或从 $E$ 外取得新信息。

## 6. 文献关系与尚未跨过的难点

- A. Tcaciuc, *The invariant subspace problem for rank one perturbations*, Duke Math. J. **168** (2019), no. 8, 1539–1550；[arXiv:1707.07836v2](https://arxiv.org/abs/1707.07836v2)，[DOI](https://doi.org/10.1215/00127094-2018-0071)。该文研究小秩一扰动；本文使用的 resolvent/basic-sequence 方法属于这一已知路线。
- A. Tcaciuc, *Invariant subspace problem for rank-one perturbations: the quantitative version*, J. Funct. Anal. **283** (2022), no. 5, 109548，Theorem 1.1；[作者机构存档](https://roam.macewan.ca/items/a84e5fe0-6b46-4860-8a99-1c87bf84b4d0)，[arXiv:2006.11954v2](https://arxiv.org/abs/2006.11954v2)。它对任意无穷维复 Banach 空间上的有界算子给出任意小秩至多一扰动的不变半空间；本文没有重证其最一般 Banach 空间版本。

本条直接证明的是一个特定而有用的选择具有哪些局限，不声称所有可能的小扰动构造都逃向零。完整 ISP 仍需一种能保存非零几何信息并最终产生原算子不变子空间的方法；把 R2 的 $E_m$ 当作这种方法的最终输入是不够的。
