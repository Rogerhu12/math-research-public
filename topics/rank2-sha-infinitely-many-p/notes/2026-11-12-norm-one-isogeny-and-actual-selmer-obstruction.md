# 实际范数为零阿贝尔簇、增广同源与 Selmer 障碍

日期：2026-11-12。状态：以下几何、局部及正合列比较均已证明。
它们不证明指定 Heegner 点的增广像非零。

沿用 R103–R111：$E:y^2=x^3-17x$，$F=\mathbb Q(\sqrt{-15})$，
$p\ge7$ 在 $F$、$\mathbb Q(i)$ 中分裂且 $p\ne17$。
取实际辅助素数 $\ell$，其在两虚二次域均惰性，
$v_p(\ell+1)=1$。令 $L=L_p$ 为环类域的次数 $p$ 循环子扩张，
$\Gamma=\langle\tau\rangle$，$\lambda\mid\ell$。
$L/F$ 仅可能在 $\lambda$ 分歧，且在该处全分歧。

## 1. 目标增广商来自一个实际同源

令
$$
\mathcal B=\operatorname{Res}_{L/F}(E_L),\qquad
\mathcal A=\ker(N:\mathcal B\longrightarrow E),\qquad
\Delta=\tau-1.
\tag{1}
$$
在 $\overline F$ 上，$\mathcal B=E^p$，$N$ 为各坐标之和，
所以其核连通；$\mathcal A$ 是维数 $p-1$ 的阿贝尔簇。
特别地
$$
\mathcal A(F)=\mathcal M:=\ker(N:E(L)\to E(F)).
$$
循环移位减恒等给同源
$$
\Delta:\mathcal A\longrightarrow\mathcal A,
\qquad \ker\Delta=\operatorname{diag}E[p],
\qquad \deg\Delta=p^2.
\tag{2}
$$
确切地，核由常数坐标 $(T,\ldots,T)$ 组成，和为零恰要求 $pT=0$。
在 Lie 代数的和为零子空间上，特征值是
$\zeta_p^j-1$，$1\le j\le p-1$，故
$$
\det(d\Delta)=\prod_{j=1}^{p-1}(\zeta_p^j-1)=p.
\tag{3}
$$
于是 R104 的目标商准确为
$$
B=\mathcal M/\Delta\mathcal M
=\mathcal A(F)/\Delta\mathcal A(F).
\tag{4}
$$

### 1.1 同源 Kummer 类与 $c_Q$ 完全一致

取 $Q\in\mathcal M$，置
$D=\sum_{j=1}^{p-1}j\tau^j$，选 $Z\in E(\overline F)$ 满足 $pZ=DQ$。
在以 $\tau^j$ 标记的 $p$ 个坐标中，定义
$$
r_j(Q)=\sum_{h=0}^{j-1}\tau^hQ,\qquad
\mathbf Z_j=Z+r_j(Q),\qquad 0\le j<p.
\tag{5}
$$
因为 $NQ=0$，有
$$
\sum_{j=0}^{p-1}r_j(Q)=-DQ,
\qquad\sum_j\mathbf Z_j=0,
\qquad\Delta\mathbf Z=(\tau^jQ)_j.
$$
故 $\mathbf Z$ 是 $Q$ 在同源 (2) 下的实际倍点。
若 $g|_L=\tau^k$，则 Galois 作用在坐标上为
$(g\mathbf Z)_j=g\mathbf Z_{j-k}$。由 $NQ=0$ 得
$$
(g\mathbf Z-\mathbf Z)_0
=gZ-Z-r_k(Q)=c_Q(g).
\tag{6}
$$
差的全部坐标相同，属于 (2) 的对角 $E[p]$。
所以在这个明确识别下
$$
\boxed{\quad\delta_\Delta(Q)=c_Q.\quad}
\tag{7}
$$
没有未定单位、额外 $p$ 因子或未说明的同源规范。
其在 $L$ 上的限制仍是 $DQ$ 的乘 $p$ Kummer 类。

## 2. 局部交集由真实局部范数给出

对 $F$ 的任一位 $v$，写 $K=F_v$，$L_v=L\otimes_FK$；
它可能是域的乘积。记
$$
\mathcal H_f(v)=\delta_p(E(K)/pE(K)),\qquad
\mathcal H_\Delta(v)
=\delta_\Delta(\mathcal A(K)/\Delta\mathcal A(K))
\subset H^1(K,E[p]).
$$
准确有
$$
\mathcal H_f(v)\cap\mathcal H_\Delta(v)
=\delta_p\bigl(N E(L_v)/pE(K)\bigr).
\tag{8}
$$
证明：由 (1) 的连接映射记
$\partial_N:E(K)\to H^1(K,\mathcal A)$。
若 $p\widetilde R=R$，则对角点
$(\widetilde R,\ldots,\widetilde R)\in\mathcal B(\overline K)$
的范数为 $R$。其 Galois 差说明
$\delta_p(R)$ 经 $E[p]\hookrightarrow\mathcal A$ 的像恰为
$\partial_N(R)$。这个像为零当且仅当 $R\in N E(L_v)$。
同源 Kummer 正合列又把该零核识别为 $\mathcal H_\Delta(v)$。
这证明 (8)，也允许所有局部 $p$ 挠点。

### 2.1 辅助素数以外，局部范数满射

对每个 $v\ne\lambda$，
$$
N E(L_v)=E(F_v).
\tag{9}
$$
若 $v$ 分裂，结论显然。否则 $L_v/F_v$ 是次数 $p$ 的不分歧扩张。
在好约化处，有限剩余域上连通光滑群的范数满射：
对 Frobenius $\varphi$，给定 $\varphi y=y$，由 Lang 定理取
$(\varphi^p-1)x=y$；则 $z=(\varphi-1)x$ 满足
$(\varphi^p-1)z=0$ 及
$(1+\varphi+\cdots+\varphi^{p-1})z=y$。
形式群各过滤商的范数是剩余域 trace，亦满射；
逐次提升并取完备极限得到形式群范数满射。
这包括 $v\mid p$：本题在 $p$ 好约化，且 $L/F$ 在 $p$ 不分歧。
不能把 $p$ 位改成一个未经证明的分裂假设。

唯一坏约化有理素数为 $2,17$。由于 $j(E)=1728$ 整，均为潜在好约化；
椭圆曲线这类 Néron 组件群的几何阶只含 $2,3$，因而与 $p\ge7$ 互素。
连通部分使用前述不分歧范数论证，组件群上乘 $p$ 可逆。
将一个基域点的组件先写成 $p$ 倍，便把剩余问题降到连通部分，
证明这两个坏位上的 (9)。复位没有障碍。

### 2.2 必须保留同源微分的行列式

对非阿基米德局部域 $K$ 上的阿贝尔簇同源自映射 $\phi$，
在足够小的形式开子群上用 Haar 测度比较，得到
$$
\frac{\#A(K)/\phi A(K)}{\#A(K)[\phi]}
=|\det(d\phi)|_K^{-1}.
$$
将它分别用于 $\Delta$ 与 $[p]:E\to E$，由 (2)–(3) 得
$$
\#\mathcal H_\Delta(v)
=\#E[p](K)\,|p|_K^{-1}
=\#\mathcal H_f(v).
\tag{10}
$$
在 $v\nmid p$，$|p|_K=1$；在 $v\mid p$，
$|p|_K=p^{-[K:\mathbb Q_p]}$。
不能因 $\dim\mathcal A=p-1$ 而把这里的因子误写成
$|p|_K^{-(p-1)}$；同源是 $\Delta$，其行列式确为 $p$。
由 (8)–(10)，
$$
\mathcal H_\Delta(v)=\mathcal H_f(v)\qquad(v\ne\lambda).
\tag{11}
$$

### 2.3 辅助位上是完整的横截条件

在 $\lambda$ 全分歧且剩余域不变，R106 已证明
$NE(L_\lambda)=pE(F_\lambda)$，故 (8) 的交集为零。
还需识别整个 $\mathcal H_\Delta(\lambda)$，不能只给交集。

若 $Q\in\mathcal A(F_\lambda)$，则
$p\bar Q=\overline{NQ}=0$，所以
$\overline{DQ}=p(p-1)\bar Q/2=0$。
$DQ$ 落在形式群，因 $\ell\ne p$ 而可除以 $p$。
由 (6)，其同源 Kummer 类限制到 $L_\lambda$ 为零。
另一方面，$a_\ell(E)=0$，在剩余域 $\mathbb F_{\ell^2}$ 上
Frobenius 对 $E[p]$ 的作用为 $[-\ell]=1$；惯性亦平凡。
因此 $E[p]\subset E(F_\lambda)$，
$$
\dim_{\mathbb F_p}
\ker\bigl(H^1(F_\lambda,E[p])\to H^1(L_\lambda,E[p])\bigr)=2
$$
由 inflation–restriction 直接得到。
(10) 使 $\mathcal H_\Delta(\lambda)$ 也恰有 $p^2$ 个元素，故
$$
\boxed{\quad
\mathcal H_\Delta(\lambda)
=\ker\bigl(H^1(F_\lambda,E[p])\to H^1(L_\lambda,E[p])\bigr)
=\mathcal H_{\mathrm{tr}}(\lambda).
\quad}
\tag{12}
$$

## 3. 实际两个 Selmer 条件的交集

由 (11)–(12)，$\operatorname{Sel}_\Delta(\mathcal A/F)$ 在
$H^1(F,E[p])$ 中恰为：辅助位使用横截条件，其余地方使用
$E$ 的通常条件。于是
$$
\operatorname{Sel}_\Delta(\mathcal A/F)
\cap\operatorname{Sel}_p(E/F)
=\operatorname{Sel}_p^{\lambda=0}(E/F).
\tag{13}
$$
结合 (4)、(7)，R111 的子群准确为
$$
\iota(B_{\mathrm{Sel}})
=\delta_\Delta\bigl(\mathcal A(F)/\Delta\mathcal A(F)\bigr)
\cap\operatorname{Sel}_p^{\lambda=0}(E/F).
\tag{14}
$$
实际 $Q_{\ell,p}$ 是这个同源上的指定整数点。
同源 Kummer 正合列同时保留
$$
0\to\mathcal A(F)/\Delta\mathcal A(F)
\to\operatorname{Sel}_\Delta(\mathcal A/F)
\to\Sha(\mathcal A/F)[\Delta]\to0.
\tag{15}
$$
这里不能仅由一个 Selmer 类的存在，反过来声称它来自指定的点。

## 4. 局部范数与全球范数之间恰是一个指定 Sha 核

令
$$
V_\lambda=\ker\bigl(E(F)/pE(F)\to E(F_\lambda)/pE(F_\lambda)\bigr),
\qquad\mathcal N=NE(L)/pE(F).
$$
由 (9) 和辅助位的范数等式，局部处处为范数的基域点模 $p$
恰是 $V_\lambda$。对 (1) 取全局及所有局部上同调，得到准确同构
$$
\boxed{\quad
V_\lambda/\mathcal N
\simeq
\ker\bigl(\Sha(\mathcal A/F)
\longrightarrow\Sha(\mathcal B/F)\bigr)
\simeq
\ker\bigl(\Sha(\mathcal A/F)
\longrightarrow\Sha(E/L)\bigr).
\quad}
\tag{16}
$$
箭头为 $R\mapsto\partial_N(R)$；第二个同构由 Weil restriction
和局部 Shapiro 同时给出。

证明不需假设 Sha 有限。若一个 Sha 类在 $\mathcal B$ 中为零，
全局正合列使它来自某个 $R\in E(F)$；局部为零恰说 $R$ 处处是范数。
其核是 $NE(L)$，即得 (16)。
因为 $N(\operatorname{diag}R)=pR$，该核被 $p$ 杀掉。
又 $\Delta:\mathcal B\to\mathcal A$ 限制为 $\Delta_\mathcal A$，
所以 (16) 的像实际上还被 $\Delta$ 杀掉。

因此 R111 的 strict 消失核商 $V_\lambda/\mathcal N$ 已经接回
这个真实范数为零阿贝尔簇的 Sha，而不是一个任意有限向量空间。
证明这个商消失仍不能代替证明实际 $[Q_{\ell,p}]$ 非零。

## 5. 中心 $-I$ 确实给完整的无局部条件上同调提升

令 $T=E[p]$、$J=\mathcal A[p]$。
(1) 的 $p$ 挠点序列为
$$
0\to J\to\mathcal B[p]\xrightarrow{N}T\to0,
\qquad
\mathcal B[p]\simeq T\otimes_{\mathbb F_p}\mathbb F_p[\Gamma].
\tag{17}
$$
$F(T)/F$ 的像是 R104 的 Cartan 正规化子，阶与 $p$ 互素。
故 $L\cap F(T)=F$。在 $J$ 的有限 Galois 像中，元素
$(-I,1)$ 是中心元素并作用为 $-1$；在 Cartier 对偶 $J^D$ 上也如此，
因为 $\det(-I)=1$，故其 cyclotomic 作用平凡。

Sah 的一行计算使有限像的 $H^1(-,J^D)=0$。
再对任意完整全局 $H^1(F,J^D)$ 类限制到分裂 $J^D$ 的域：
若限制非零，则它成为非零有限平移 homomorphism；Chebotarev 在
完全分裂于模分裂域的好位检测这个非零平移。
所以完整局部核为零：
$$
\Sha^1(F,J^D)=0.
$$
Milne（2006），I, Theorem 4.10(a)，取 $S$ 为全部位，遂给
$$
\Sha^2(F,J)=0.
\tag{18}
$$
若 $\kappa\in\operatorname{Sel}_p^{\lambda=0}(E/F)$，
每个局部类都可由 $E(L_v)$ 点的 Kummer 类 corestrict 得到：
辅助位取零，其余位用 (9)。因此 (17) 的连接类局部处处为零，
由 (18) 全局为零。Shapiro 给
$$
\operatorname{Sel}_p^{\lambda=0}(E/F)
\subseteq
\operatorname{cor}_{L/F}H^1(L,E[p]).
\tag{19}
$$
特别地，这也适用于实际 $c_{Q_{\ell,p}}$。
这里没有要求或证明提升满足通常 Selmer 局部格，
也没有给预先固定分歧集合上的提升。
完整 $\Sha^2(J)=0$ 不等于 $\Sha(\mathcal A)[p]=0$；
(16) 中的真实点范数障碍仍然保留。

若要把 (19) 改为 $\operatorname{cor}\operatorname{Sel}_p(E/L)$，
可以准确写其余配对条件：在 (17) 上给 $\mathcal B[p]$ 通常 Kummer
局部格，给 $T$ 其范数像，给 $J$ 前者的逆像。
Morgan–Smith（2024），Theorem 2.1，给相应有限 Selmer 群配对，
其左核准确为 $\operatorname{cor}\operatorname{Sel}_p(E/L)$。
故中心 $-I$ 消去的是 (18) 的完整局部核；
通常局部格留下的是这个明确配对，而不是同一个已经消失的群。

### 5.1 剩余配对的对偶对象恰为 strict $\mathcal A^\vee$

记 $\mathscr W_J(v)$ 为 $\mathcal B[p]$ 通常 Kummer 格在
$H^1(F_v,J)$ 中的逆像。这个格可完整算出：
$$
\mathscr W_J(v)=
\begin{cases}
\delta_p(\mathcal A(F_v)/p\mathcal A(F_v)),&v\ne\lambda,\\
H^1(F_\lambda,J),&v=\lambda.
\end{cases}
\tag{20}
$$
若 $v\ne\lambda$，(9) 及 (1) 的局部正合列说明
$H^1(F_v,\mathcal A)\to H^1(F_v,\mathcal B)$ 单射。
一个 $J$ 类在 $\mathcal B[p]$ 中落在通常 Kummer 格，
等价于其在 $H^1(F_v,\mathcal B)$ 中像为零；单射使它在
$H^1(F_v,\mathcal A)$ 中也为零，恰好就是 $\mathcal A$ 的
通常乘 $p$ Kummer 条件。反向由点的 Kummer 自然性直接成立。

在 $\lambda$，$T$ 是平凡二维模，而
$J=T\otimes I$，$I$ 为 $\mathbb F_p[\Gamma]$ 的增广理想。
$I^\Gamma$ 与 $(I^D)^\Gamma$ 均为一维；这里
$\mu_p\subset F_\lambda$，故 Cartier 对偶的 twist 不改变维数。
于是
$$
\dim H^0(F_\lambda,J)=\dim H^0(F_\lambda,J^D)=2,
\qquad \dim H^1(F_\lambda,J)=4.
$$
最后一个等式是剩余特征不同于 $p$ 的局部 Euler 特征公式及局部对偶。
又 $H^0(F_\lambda,\mathcal B[p])\to H^0(F_\lambda,T)$
是常数坐标上的乘 $p$，故为零；(17) 的长正合列因而给一个
二维核
$$
\ker\bigl(H^1(F_\lambda,J)\to
H^1(F_\lambda,\mathcal B[p])\bigr).
$$
$\mathcal B$ 的通常 Kummer 格也为二维，且其范数像为零，
因为 $NE(L_\lambda)=pE(F_\lambda)$。
长正合列保证该整个二维格均可提升；加上上述二维核，
$\mathscr W_J(\lambda)$ 已占满四维空间，证明 (20)。

在 Cartier 对偶 $J^D=\mathcal A^\vee[p]$ 上取正交局部条件。
通常 Kummer 格的正交补恰为对偶阿贝尔簇的通常 Kummer 格；
这是局部 Tate 对偶与乘 $p$ 正合列的兼容性
（Milne（2006），I, Theorem 3.2、Corollary 3.4）。
而 (20) 在 $\lambda$ 的整个空间，其正交补为零。因此上述配对准确为
$$
\operatorname{Sel}_p^{\lambda=0}(E/F)
\times\operatorname{Sel}_p^{\lambda=0}(\mathcal A^\vee/F)
\longrightarrow \tfrac1p\mathbb Z/\mathbb Z.
\tag{21}
$$
若 $\operatorname{pr}:\mathcal B^\vee\to\mathcal A^\vee$
为 (1) 中包含映射的对偶，则 Morgan–Smith Theorem 2.1
还使 (21) 下降为有限群的完美配对
$$
\frac{\operatorname{Sel}_p^{\lambda=0}(E/F)}
 {\operatorname{cor}_{L/F}\operatorname{Sel}_p(E/L)}
\times
\frac{\operatorname{Sel}_p^{\lambda=0}(\mathcal A^\vee/F)}
 {\operatorname{pr}_*\operatorname{Sel}_p(\mathcal B^\vee/F)}
\longrightarrow\tfrac1p\mathbb Z/\mathbb Z.
\tag{22}
$$
Weil restriction 的主极化及 Shapiro 已用于第一个分母。
第二个分母确落在 strict 群中，这是对偶局部条件和 (20) 的结论，
不额外假设 $\mathcal A$ 主极化。
式 (22) 明确给出仍待消去的通常格障碍；它没有证明任一商为零，
更没有证明指定 $c_{Q_{\ell,p}}$ 非零。

## 6. 实际长增广块与普通 Cassels–Tate 配对

R109 的整个长块
$\mathbb F_p[\Gamma]\,\delta_p(X_\ell)$ 在
$\operatorname{Sel}_p(E/F[\ell])$ 中来自实际 Mordell–Weil 点。
每个 $\Delta^kX_\ell$ 及 Gauss 算子作用后的点都是如此。
其 Sha 像全部为零，所以经典 Cassels–Tate 配对拉回到 Selmer 后，
在这个完整实际长块上恒为零。
普通交替性因此不把已经证明的超过一半的增广长度提升为完整长度。
若改用导出的配对或高度，需要另行证明它与指定 Heegner 类的比较；
本文没有把普通配对的这个零值换成导出配对的非零输入。

## 已使用的外部输入

- R104、R106、R111：实际循环域、全局无 $p$ 挠点、正规化子像、
  辅助位范数及指定下降类；几何坐标和局部比较在本文证明。
- J. S. Milne（2006），*Arithmetic Duality Theorems*, 2nd ed.，
  I, Theorem 4.10(a)，印刷第 56–57 页，
  [作者正式全文](https://www.jmilne.org/math/Books/ADTnot.pdf)。
  使用 $S$ 为全部位的版本；不把它误作固定有限 $S$ 的局部格消去。
- A. Morgan、A. Smith（2024），
  *Field change for the Cassels–Tate pairing and applications to class groups*，
  Research in Number Theory **10**, Article 61，
  [正式全文](https://link.springer.com/article/10.1007/s40993-024-00545-2)，
  Theorem 2.1 的准确左核。未使用任何未经证明的配对满射或 Sha 有限性。
