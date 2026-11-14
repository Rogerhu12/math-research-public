# R203：UHF 内的有理严格循环性与可闭性障碍

日期：2026-11-12（UTC）。作者：literature。根代理预留 R203。

状态：完整实际算子证明。结论适用于指定的 UHF 内交换代数，不推广到整个交换子代数。慢符号在任意不变限制上的稠密像问题仍未解决。

## 1. 记号、输入与主结论

沿用实际 Haar 表示
$$
H=L^2(\mathbb Z_2,\mu),\qquad
\mathfrak C=\{A\}',\qquad
\mathcal A=\overline{\mathbb C[A]}^{\|\cdot\|},
$$
以及实际物理张量 UHF 代数 $\mathfrak U$。
$\mathcal A\subseteq\mathfrak U\cap\mathfrak C$。

R88 给出
$$
\mathfrak C=\overline{\mathbb C[A]}^{\mathrm{SOT}},
\qquad \mathfrak C\text{ 交换}.
\tag{1.1}
$$
$1$ 是 $A$ 的循环向量。
令
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad V_j1=\chi_j,
$$
并记纯局部算子 $V_j^0=I-2E_j$。
已有真实 carry 估计给
$$
\sup_j\|V_j\|\le6,\qquad
\|V_j-V_j^0\|\longrightarrow0.
\tag{1.2}
$$

记 $\mathcal D$ 为有限柱空间。对 $a\in\ell^2$，R125 先定义
$$
X_{a,0}v=\lim_{m\to\infty}\sum_{j=0}^{m}a_jV_jv
\qquad(v\in\mathcal D),
$$
再构造其闭包 $X_a=\overline{X_{a,0}}$ 及通常伴随。
$\mathcal D$ 同时是 $X_a$ 和 $X_a^*$ 的图核心；
有限系数截断在 $\mathcal D$ 上分别收敛到二者。
这里不把任意域向量上的原顺序部分和收敛作为闭实现的定义。若 $a\ne0$，则
$$
f_a=X_a1=\sum_j a_j\chi_j
$$
为循环向量。
首先记录 R171 的一阶情形（第5.1节的有限生成加强还将使用其任意次数版本）：
$$
\boxed{
a\in\ell^2\setminus\ell^1,\quad
0\ne B\in\mathfrak U,\quad C_0\in B(H)
\ \Longrightarrow\
BX_a-C_0\text{ 在 }\mathcal D\text{ 上无界}.
}
\tag{1.3}
$$

这里“有理严格循环向量”采用原始文献 [BDDP] 的定义：对一个含单位元的代数 $\mathfrak D$，向量 $h_0$ 满足，对每个 $h\in H$，存在 $C_h,D_h\in\mathfrak D$，使
$$
D_hh=C_hh_0,\qquad \ker D_h=\{0\}.
\tag{1.4}
$$
它要求带单射分母的精确表示，不能以普通循环性替代。可闭性性质则要求：每个与该代数按真实定义域交换的稠密域线性算子都可闭。

**定理 1.1。**

1. 对任意可数向量族 $(h_r)_{r\ge1}\subset H$，存在同一个非负系数列
   $a\in\ell^2\setminus\ell^1$，使全部 $h_r\in\operatorname{Dom}X_a$。
   可以取 $a_{j_n}=1/n$，其余系数为零。
2. 任何含单位元的交换代数
   $$
   \mathfrak D\subseteq\mathfrak U\cap\mathfrak C
   $$
   都没有有理严格循环向量。
3. 若上述 $\mathfrak D$ 还包含 $A$，则它不具有可闭性性质。具体地，对任意非零
   $a\in\ell^2\setminus\ell^1$，
   $$
   \mathfrak D1\cap\mathfrak D f_a=\{0\},
   \qquad
   \overline{\mathfrak D1}
   =\overline{\mathfrak D f_a}=H,
   \tag{1.5}
   $$
   因而能写出一个与 $\mathfrak D$ 交换、稠密定义但不可闭的线性算子。

4. 更强地，对上述任意 $\mathfrak D$，不存在有限族
   $h_1,\ldots,h_d\in H$，使每个 $h\in H$ 都可写成
   $$
   D_hh=\sum_{i=1}^d C_{h,i}h_i,\qquad
   D_h,C_{h,i}\in\mathfrak D,\quad \ker D_h=\{0\}.
   \tag{1.6}
   $$
   即使允许随 $h$ 改变的单射分母，也不存在这种有限有理模生成。

所以这些结论特别适用于 $\mathcal A$。
没有把 $\mathfrak C$ 的全部元素假定属于 UHF，也没有假定全部非零 $\mathfrak C$ 元素单射。

## 2. 实际高位算子弱趋于零

先证明
$$
\boxed{V_j\longrightarrow0\quad\text{于 WOT}.}
\tag{2.1}
$$

若 $u,v$ 均只依赖某个固定有限头，则当 $j$ 位于该头之外时，
$$
\langle V_j^0u,v\rangle
=\langle u,v\rangle\langle V_j^01,1\rangle=0,
$$
因为 $V_j^01=\chi_j$ 且 $\chi_j$ 均值为零。
有限柱向量稠密，而 $\sup_j\|V_j^0\|<\infty$，所以
$V_j^0\to0$ 于 WOT。
(1.2) 随即给出 (2.1)。

这里使用的是实际算子对纯算子的范数误差。
没有把弱收敛变成强收敛，也没有在移动输入上使用强极限。

## 3. 任意可数向量族的共同正一阶定义域

给定 $(h_r)_{r\ge1}$。
递归选择严格递增的指标 $j_1<j_2<\cdots$，要求当 $n>m$ 且 $r\le n$ 时，
$$
\left|
\langle V_{j_n}h_r,V_{j_m}h_r\rangle
\right|\le2^{-n-m}.
\tag{3.1}
$$
在第 $n$ 步只有有限多个条件。
由 (2.1)，每个固定 $V_{j_m}h_r$ 都是合法的弱测试向量，故可以同时满足它们。

定义
$$
a_{j_n}=\frac1n,\qquad a_j=0\quad(j\notin\{j_n:n\ge1\}),
\tag{3.2}
$$
并置
$$
X^{(N)}=\sum_{n=1}^N\frac1nV_{j_n}.
$$
显然 $a\ge0$、$a\in\ell^2\setminus\ell^1$。

固定 $r$，取 $N>M\ge r$。
利用 (1.2) 和 (3.1)，
$$
\begin{split}
\left\|\sum_{n=M+1}^N\frac1nV_{j_n}h_r\right\|^2
&\le36\|h_r\|^2\sum_{n>M}\frac1{n^2}\\
&\quad+
2\sum_{M<m<n}\frac{2^{-m-n}}{mn}.
\end{split}
\tag{3.3}
$$
右端随 $M\to\infty$ 趋零。
因此存在 $y_r\in H$，使
$$
X^{(N)}h_r\longrightarrow y_r.
\tag{3.4}
$$

这仍只是一列有界截断作用的收敛；以下识别真实闭算子域。

对任意 $v\in\mathcal D$，R125 的伴随图核心给
$$
(X^{(N)})^*v\longrightarrow X_a^*v.
$$
于是
$$
\langle y_r,v\rangle
=\lim_N\langle h_r,(X^{(N)})^*v\rangle
=\langle h_r,X_a^*v\rangle.
\tag{3.5}
$$
因为 $\mathcal D$ 是 $X_a^*$ 的图核心，
$$
(X_a^*|_{\mathcal D})^*=X_a.
$$
由 (3.5)，
$$
\boxed{h_r\in\operatorname{Dom}X_a,\qquad X_ah_r=y_r.}
\tag{3.6}
$$
这证明定理 1.1 第1项。

选出的系数列依赖给定可数族。
本结论不声称存在一个无界 $X_a$ 的定义域包含全部 $H$。

## 4. 闭一阶乘子与全部交换子的定义域交换

本节明确后文清分母时使用的域事实。
R125 已有
$$
A\operatorname{Dom}X_a\subseteq\operatorname{Dom}X_a,\qquad
X_aAx=AX_ax.
$$
因此对每个多项式 $p$，
$$
X_ap(A)x=p(A)X_ax\qquad(x\in\operatorname{Dom}X_a).
$$

给定 $T\in\mathfrak C$，由 (1.1) 选网 $p_\alpha(A)\to T$ 于 SOT。
对固定 $x\in\operatorname{Dom}X_a$，
$$
p_\alpha(A)x\to Tx,\qquad
X_ap_\alpha(A)x=p_\alpha(A)X_ax\to TX_ax.
$$
$X_a$ 闭，故
$$
\boxed{
T\operatorname{Dom}X_a\subseteq\operatorname{Dom}X_a,\qquad
X_aTx=TX_ax.
}
\tag{4.1}
$$
这里只对两个固定向量使用强逼近；不需要逼近网的统一算子范数界。

## 5. 没有 UHF 内的有理严格循环向量

设
$$
\mathfrak D\subseteq\mathfrak U\cap\mathfrak C
$$
是含单位元的代数，反设 $h_0$ 满足 (1.4)。

用第3节选择 $a\ge0$、$a\in\ell^2\setminus\ell^1$，
使 $h_0\in\operatorname{Dom}X_a$。
将 (1.4) 用于 $X_ah_0$，得到 $A_0,B\in\mathfrak D$，满足
$$
BX_ah_0=A_0h_0,\qquad \ker B=\{0\}.
\tag{5.1}
$$

再取任意 $h\in\operatorname{Dom}X_a$。
选择 $C_h,D_h$ 满足 (1.4)。
由交换性与 (4.1)，所有下式均在真实定义域内：
$$
\begin{split}
D_hBX_ah
&=B X_aD_hh\\
&=B X_aC_hh_0\\
&=C_h B X_ah_0\\
&=C_hA_0h_0\\
&=A_0D_hh.
\end{split}
$$
取消单射 $D_h$，得到
$$
BX_ah=A_0h
\qquad(h\in\operatorname{Dom}X_a).
\tag{5.2}
$$

$B$ 单射，所以 $B\ne0$，且 $B\in\mathfrak U$。
(5.2) 在 $\mathcal D$ 上尤其成立，与 (1.3) 矛盾。

因此
$$
\boxed{
\mathfrak D\subseteq\mathfrak U\cap\mathfrak C
\Longrightarrow
\mathfrak D\text{ 没有有理严格循环向量}.
}
\tag{5.3}
$$
证明没有要求候选 $h_0$ 预先是普通循环向量。

第5节的清分母结构与 [BDDP, Proposition 4.6] 一致；
这里已给完整证明，并使用本模型第3节来保证所选无界乘子确实在 $h_0$ 上有定义。

### 5.1 有限有理模生成也不可能

反设某个有限族 $h_1,\ldots,h_d$ 满足 (1.6)。
第3节给同一个非负 $a\in\ell^2\setminus\ell^1$，使所有
$h_i\in\operatorname{Dom}X$，其中 $X=X_a$。

分别将 (1.6) 用于 $Xh_j$：
$$
D_jXh_j=\sum_{i=1}^d C_{ji}^{\,0}h_i,
\qquad \ker D_j=\{0\}.
$$
令
$$
B=\prod_{j=1}^dD_j,\qquad
C_{ji}=\left(\prod_{\ell\ne j}D_\ell\right)C_{ji}^{\,0}.
$$
则 $B$ 单射，$B,C_{ji}\in\mathfrak D$，且
$$
BXh_j=\sum_iC_{ji}h_i.
\tag{5.4}
$$

不能在 (5.4) 上直接反复使用 $X$：目前只知道 $h_i$ 在一阶域中。
改用 R128 的有界单射正则子
$$
R\in\mathfrak C,\qquad
RH\subseteq\operatorname{Dom}X,\qquad
S=XR\in\mathfrak C.
$$
对 $h_j\in\operatorname{Dom}X$，(4.1) 给 $RXh_j=Sh_j$。
将 (5.4) 左乘 $R$，得到全有界矩阵恒等式
$$
(BS I_d-RC)\begin{pmatrix}h_1\\ \vdots\\h_d\end{pmatrix}=0,
\qquad C=(C_{ji})_{j,i=1}^d.
\tag{5.5}
$$
矩阵各项属于交换代数 $\mathfrak C$。
因此通常的伴随矩阵恒等式合法，给
$$
\Delta h_i=0\quad(1\le i\le d),
\qquad
\Delta=\det(BS I_d-RC).
\tag{5.6}
$$
$\Delta$ 是一个有界交换子，且可展开为
$$
\Delta=B^dS^d+\sum_{k=1}^d E_kS^{d-k}R^k,
\qquad E_k\in\mathfrak D.
\tag{5.7}
$$
例如 $E_k=(-1)^kB^{d-k}e_k(C)$，其中 $e_k(C)$ 是主子式之和。

任取 $h\in H$，用 (1.6) 表示它。
由交换性与 (5.6)，
$$
D_h\Delta h
=\sum_iC_{h,i}\Delta h_i=0.
$$
取消单射 $D_h$，得到 $\Delta h=0$。
所以
$$
\Delta=0\quad\text{在全部 }H.
\tag{5.8}
$$

现在才转到具有全部自然幂域的测试向量。
R171 给 $\mathcal D\subseteq\operatorname{Dom}X^d$。
由 (4.1) 及 $S=XR$，对 $v\in\mathcal D$ 和 $0\le m\le d$，
$$
S^m v=R^mX^mv.
$$
因而 (5.7)—(5.8) 给
$$
0=\Delta v
=R^d\left(B^dX^d+\sum_{k=1}^dE_kX^{d-k}\right)v.
\tag{5.9}
$$
$R^d$ 单射，故括号在全部 $\mathcal D$ 上为零。
其最高系数 $B^d$ 是非零 UHF 元素，其余系数有界。
这与 R171 的次数 $d$ 结论矛盾。

故不存在 (1.6)。
这个加强没有要求原有限生成向量 $h_i$ 属于任何高阶自然幂域；
高阶演算只在 R171 已证明合法的有限柱测试空间上执行。

## 6. 两个稠密轨道模的交为零

现在进一步假定 $A\in\mathfrak D$。
任取 $a\in\ell^2\setminus\ell^1$，令
$$
X=X_a,\qquad f=X1.
$$
R125 给 $f$ 循环；所以
$$
\overline{\mathfrak D1}
=\overline{\mathfrak Df}=H.
\tag{6.1}
$$

反设存在关系
$$
Bf=C_01,\qquad B,C_0\in\mathfrak D.
\tag{6.2}
$$
对任意多项式 $p$，由 (4.1) 及交换性，
$$
BXp(A)1=Bp(A)f
=p(A)Bf
=C_0p(A)1.
\tag{6.3}
$$

为应用 R171，须把 (6.3) 延到全部有限柱，不能只假设多项式真空轨道自动是所需图核心。

每个有限柱向量 $v$ 可写成
$$
v=F(A)1,
\tag{6.4}
$$
其中 $F$ 是在零点附近真正解析的标量芽。
事实上每个 Walsh 单项式由不同位的有限乘积
$\prod_{j\in J}V_j1=\chi_J$ 给出，而每个 $V_j$ 是 $A$ 的真实有理单位演算。

选多项式 $p_n$ 使
$$
p_n(A)\longrightarrow F(A)\quad\text{按算子范数}.
$$
(4.1) 给
$$
p_n(A)1\to v,\qquad
Xp_n(A)1=p_n(A)f\to F(A)f=Xv.
$$
将 (6.3) 取极限，得
$$
BXv=C_0v\qquad(v\in\mathcal D).
\tag{6.5}
$$
若 $B\ne0$，则 (6.5) 与 R171 矛盾。
所以 $B=0$，且 (6.2) 中的公共向量为零。
又因 $1$ 循环，$C_01=0$ 还给 $C_0=0$。

因此
$$
\boxed{\mathfrak D1\cap\mathfrak Df=\{0\}.}
\tag{6.6}
$$

## 7. 实际稠密域非可闭交换算子

由 (6.6)，可在代数直和
$$
\operatorname{Dom}Z=\mathfrak D1\mathbin{\dot+}\mathfrak Df
$$
上定义
$$
Z(x+y)=y,\qquad
x\in\mathfrak D1,\quad y\in\mathfrak Df.
\tag{7.1}
$$
定义域稠密。
对每个 $T\in\mathfrak D$，两个直和分量都由 $T$ 保持，
所以
$$
T\operatorname{Dom}Z\subseteq\operatorname{Dom}Z,\qquad
ZT=TZ\text{ 于 }\operatorname{Dom}Z.
\tag{7.2}
$$

取固定 $0\ne y\in\mathfrak Df$。
由 $\mathfrak D1$ 稠密，存在 $y_n\in\mathfrak D1$ 使 $y_n\to y$。
于是
$$
y-y_n\longrightarrow0,\qquad
Z(y-y_n)=y\ne0.
\tag{7.3}
$$
故 $Z$ 不可闭。

这给完整的实际反例：
$$
\boxed{
A\in\mathfrak D\subseteq\mathfrak U\cap\mathfrak C
\Longrightarrow
\mathfrak D\text{ 不具有可闭性性质}.
}
\tag{7.4}
$$
这里并非仅由“没有有理严格循环向量”倒推可闭性失败。
(7.1)—(7.3) 独立给出了具体的非可闭算子。
这种稠密直和构造可与 [BDDP, Lemma 3.4] 对照。

## 8. 为什么不能推广到全部交换子代数

R128 对任意非零一阶 $X=X_a$ 给出有界单射正则子
$$
R\in\mathfrak C,\qquad
RH\subseteq\operatorname{Dom}X,\qquad
T=XR\in\mathfrak C.
$$
$X$ 单射，故 $T$ 单射；由共同共轭对称，$R,T$ 都值域稠密。

对 $f=X1$，真实域交换给
$$
Rf=RX1=XR1=T1.
\tag{8.1}
$$
因此
$$
\mathfrak C f\cap\mathfrak C1
$$
包含非零向量 $Rf$，甚至包含一个循环向量：
$f$ 循环且 $R$ 是有界稠密像交换子，所以 $Rf$ 循环。

这正好阻止把第6、7节的直和构造照搬到 $\mathfrak C$。
同时由 R171，任何这样的非零正则子 $R$ 都不可能属于 UHF。

本稿没有决定：

- $\mathfrak C$ 是否存在有理严格循环向量；
- $\mathfrak C$ 是否具有可闭性性质；
- 每个有限秩泛函在 $\mathfrak C$ 上是否存在循环第一因子的单向量表示；
- 具体慢 $S_N,S_Y$ 的强主理想是否包含单位的强极限。

这些是不同的问题，不能用文献中的单向蕴含混同。

## 9. 原始分解定理的适用边界

### 9.1 已核来源

[BDDP] H. Bercovici, R. G. Douglas, C. Foias, C. Pearcy,
*Confluent operator algebras and the closability property*,
Journal of Functional Analysis 258 (2010), 4122–4153,
DOI [10.1016/j.jfa.2010.03.009](https://doi.org/10.1016/j.jfa.2010.03.009)。

已核作者预印本 [arXiv:0908.0729v2](https://arxiv.org/pdf/0908.0729)：
Definition 4.1 在 PDF 印刷第7页；
Theorem 4.4 在第8页；
Proposition 4.6、Definition 4.7、Proposition 4.8 在第9页；
稠密直和的可闭性障碍 Lemma 3.4 在第4页。
原定理从交换代数的有理严格循环向量推出可闭性。
原文的 confluence 还要求任意两非零向量有共同的单射算子像；
Proposition 4.8 将其等价为有理严格循环性加全部非零代数元素单射。
这些都是额外前提，不能由本模型已经有一个普通循环向量来替代。

[DH] K. R. Davidson, R. Hamilton,
*Nevanlinna–Pick Interpolation and Factorization of Linear Functionals*,
DOI [10.1007/s00020-011-1862-7](https://doi.org/10.1007/s00020-011-1862-7)。

已核 [作者全文](https://www.math.uwaterloo.ca/~krdavids/Preprints/DavHamNP.pdf)：
Theorem 5.2 在 PDF 印刷第19页、证明在第20页；
Corollary 5.3 及其后的 cyclic/outer 说明在第20页。
这里完整 Pick 核的乘子代数具有 $\mathbb A_1(1)$ 分解；
该证明还允许第一向量为相应乘子代数的循环向量。
它不是任意交换、有循环向量的算子代数定理。

### 9.2 该标量乘子模型不能直接实现本题代数

给一个自含的适用性检验。
设 $\mathcal K$ 是某集合上的标量函数再生核 Hilbert 空间，
$M_\varphi$ 为一个有界乘子。
对每个非零点核 $k_x$，
$$
M_\varphi^*k_x=\overline{\varphi(x)}\,k_x.
\tag{9.1}
$$
所以若 $M_\varphi$ 拟幂零，则所有有效点上的 $\varphi(x)=0$，
因而 $M_\varphi=0$。

更一般，设 $\mathfrak B$ 是包含实际 $A$ 的赋予算子范数的代数，
且
$$
\Phi:\mathfrak B\longrightarrow\operatorname{Mult}(\mathcal K)
$$
是有界代数同态。
因为
$$
\|\Phi(A)^n\|
=\|\Phi(A^n)\|
\le\|\Phi\|\,\|A^n\|,
$$
实际 $A$ 的拟幂零性给 $r(\Phi(A))=0$。
由 (9.1)，$\Phi(A)=0$。
由于 $A\ne0$，这样的同态不可能忠实。

因此 [DH] 的标量完整 Pick 乘子模型不能通过一个有界忠实表示直接套到 $\mathcal A$ 或 $\mathfrak C$。
这不否定它们可能有某种独立证明的 $\mathbb A_1$ 性质，
也不排除更大的非交换压缩模型；
只是精确排除直接把现有标量乘子定理当成所缺分解的接口。

## 10. 与慢符号问题的关系

本稿给出了两个实际障碍，而没有宣称解决慢符号问题。

一方面，在 $\mathfrak U\cap\mathfrak C$ 内寻找普通文献所用的有理严格循环性或可闭性，已经被第5、7节排除。
另一方面，第8节说明全 $\mathfrak C$ 确实多出了非 UHF 正则子，因而较大的因子分解问题仍有内容。

对全空间已稠密像的慢符号，循环第一因子分解足以推出强主理想单位；精确的有限秩、WOT/SOT 与正常泛函区别见
[泛函接口与固定真空障碍笔记](../notes/2026-11-12-slow-symbol-functional-factorization-interface-and-vacuum-obstruction-0c-agent.md)。
本稿不把 [BDDP] 的可闭性结论改写为该分解性质，也不把第9节的模型障碍误称为分解不存在。

## 11. 内部证明依赖

- [R88：完整交换子及强多项式闭包](../results/R88-riesz-basis-bounded-multipliers-strong-closure.md)；
- [R125：全部 $\ell^2$ 一阶乘子的闭实现与循环性](../results/R125-all-l2-first-chaos-closed-multiplier-cyclicity.md)；
- [R128：真实正则化与定义域](../results/R128-first-chaos-invariant-parts-and-resolvent-regularization.md)；
- [R171：无界一阶乘子的 UHF 最高系数障碍](../results/R171-uhf-leading-polynomials-of-unbounded-first-multipliers.md)。

所有使用 R171 的地方都在原 Haar 空间的全部有限柱上建立了真实算子关系。
没有把该全空间测试结论传给未知不变限制。
