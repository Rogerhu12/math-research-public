# R236 附录：全部固定阶通常伴随域与中央耦合的高阶正则性

日期：2026-11-12（UTC）。独占作者：critical_kernel。

状态：完整的实际固定阶结论。承接[真实二阶域附录](../results/R236-appendix-second-order-adjoint-domains-and-bounded-central-products.md)，以下先证明真实嵌套交换子的算子范数收敛，再支付每一阶定义域。结论包括全部自然幂的通常伴随同域和中央外块在每个固定幂域中的有界性。它仍不给中央逆的值域控制；末节明确保留这一差别。

## 1. 设置和一次弱域传递

沿用实际 Haar 模型
$$
X=a_*I+\sum_{j\ge0}a_jV_j,\qquad a\in\ell^2,
\qquad
V_j=(I-N_j)(I+N_j)^{-1}.
$$
令 $X_N=a_*I+\sum_{j<N}a_jV_j$。R125/R161 给共同有限柱图核心 $\mathscr D$，满足
$$
X_Nf\to Xf,\qquad X_N^*f\to X^*f
\quad(f\in\mathscr D),
$$
以及 $\operatorname{Dom}X=\operatorname{Dom}X^*$。
所有 $V_j$ 彼此交换，$\|V_j\|\le6$。R161 的真实进位界为
$$
\|[V_i^*,V_j]\|\le
648\,\frac{\alpha_{\max(i,j)}}{\alpha_{\min(i,j)}}
\quad(i\ne j),\qquad
\|[V_i^*,V_i]\|\le72.
\tag{1.1}
$$
特别，当 $i\ne j$ 且 $\max(i,j)=m$ 时，第一式至多为
$648\eta_{m-1}$。这里
$$
\eta_j\le e^{-770\,16^j}.
$$

**弱域传递引理。** 若 $B_N,D_N\in B(H)$，
$$
B_N\to B,\qquad D_N\to D
$$
均按算子范数收敛，并且
$$
[X_N,B_N]=D_N,
$$
则
$$
B\operatorname{Dom}X\subseteq\operatorname{Dom}X,\qquad
[X,B]=D
\tag{1.2}
$$
在真实完整域上成立。

证明只需对 $f,g\in\mathscr D$ 使用
$$
\langle B_Nf,X_N^*g\rangle-\langle B_NX_Nf,g\rangle
=\langle D_Nf,g\rangle.
$$
取极限后，以 $\mathscr D$ 是 $X^*$ 的图核心判定 $Bf\in\operatorname{Dom}X$；
再对任意 $f\in\operatorname{Dom}X$ 作图核心逼近，并用 $X$ 闭性延拓。
这里不要求 $B_N$ 保持有限柱，也不假定 $X_N$ 在任意 Hilbert 输入上收敛。

下文写 $\delta_X B=[X,B]$，每一次都表示已经由这个引理付清的完整域等式。

## 2. 自交换子所有固定阶导数的真实范数级数

令
$$
C_N=[X_N^*,X_N],\qquad C_N\to C_a
$$
为 R161 的实际算子范数极限。
对整数 $r\ge1$，
$$
\operatorname{ad}_{X_N}^{\,r-1}C_N
=-\operatorname{ad}_{X_N}^{\,r}X_N^*.
\tag{2.1}
$$
展开右端，出现一个星号位置 $i$ 和 $r$ 个非星号位置
$j_1,\ldots,j_r$，其系数的模为
$$
|a_i|\prod_{\ell=1}^r|a_{j_\ell}|.
$$

因为所有 $V_j$ 交换，导子 $\operatorname{ad}_{V_j}$ 彼此交换。
所以在每个嵌套交换子中，可把任意一个非星号叶位置移到最内层，先与 $V_i^*$ 交换。

分两种情况：

- 若全部 $r+1$ 个位置都为 $i$，最内层成本至多 $72$，
  其余每层成本至多 $2\|V_i\|\le12$。
- 若元组不恒定，令 $m$ 为全部位置的最大值。
  如果星号位置 $i=m$，选一个小于 $m$ 的叶位置；
  如果 $i<m$，选一个等于 $m$ 的叶位置。
  两种情况的最内层交换子都至多为 $648\eta_{m-1}$。
  剩下每层仍只付 $12$。

记 $s_m=\sum_{j\le m}|a_j|$。于是对所有有限截断统一有
$$
\boxed{
\left\|\operatorname{ad}_{X_N}^{\,r-1}C_N\right\|
\le
12^{r-1}\left[
72\sum_i|a_i|^{r+1}
+648\sum_{m\ge1}\eta_{m-1}s_m^{r+1}
\right].
}
\tag{2.2}
$$
第二项把最大位置恰为 $m$ 的系数总和粗略放大为 $s_m^{r+1}$，因此没有漏掉元组或隐含的项数。

因 $s_m\le\sqrt{m+1}\|a\|_2$，右侧对每个固定 $r$ 有限。
截断差只含至少一个大于截断阈值的指标；其全同位部分由
$\sum_{i\ge N}|a_i|^{r+1}$ 控制，混合部分由
$\sum_{m\ge N}\eta_{m-1}s_m^{r+1}$ 控制。
两尾都趋零，所以 (2.1) 对每个固定 $r$ 按算子范数收敛。

把相邻两阶的极限代入 (1.2)，逐阶得到：
$$
\boxed{
\delta_X^n C_a\in B(H)\quad(n\ge0),
\qquad
(\delta_X^nC_a)\operatorname{Dom}X\subseteq\operatorname{Dom}X.
}
\tag{2.3}
$$
这不是在未共同定义的无界乘积上形式交换；实际范数收敛先于每次弱域判据。

## 3. Bell 系数的通常伴随也有全部固定阶导数

令
$$
B_2=\sum_i a_i^2(I-V_i^2),\qquad
B_{2,N}^*=\sum_{i<N}\overline{a_i}^{\,2}(I-(V_i^*)^2).
$$
$B_{2,N}^*\to B_2^*$ 按算子范数收敛。
对 $r\ge1$，展开
$\operatorname{ad}_{X_N}^{\,r}B_{2,N}^*$。
非星号叶位置依然可重排。

最内层交换子满足
$$
\|[V_j,(V_i^*)^2]\|
\le2\|V_i\|\|[V_j,V_i^*]\|.
$$
因此全同位成本至多 $864$，混合元组最大位置为 $m$ 时成本至多
$7776\eta_{m-1}$。由同一求和，
$$
\boxed{
\left\|\operatorname{ad}_{X_N}^{\,r}B_{2,N}^*\right\|
\le
12^{r-1}\left[
864\sum_i|a_i|^{r+2}
+7776\sum_{m\ge1}\eta_{m-1}
 \left(\sum_{i\le m}|a_i|^2\right)s_m^r
\right].
}
\tag{3.1}
$$
每个固定 $r$ 的右侧有限，且相同尾估计给范数 Cauchy。
由 (1.2)，
$$
\boxed{
\delta_X^rB_2^*\in B(H)
\quad\text{且保持 }\operatorname{Dom}X
\quad(r\ge0).
}
\tag{3.2}
$$
$r=0$ 的域保持用一阶极限支付。

## 4. 准幂零全纯演算的导数与真实逆域

这里给出使用 $Y=\phi(B_2)$ 时所需的逆域事实，而不把任意有界算子的逆域保持当成自动成立。

设 $B\in B(H)$ 准幂零，且 $B,\delta_XB,\ldots$ 都满足 (3.2) 型条件。
有界乘积的 Leibniz 公式在完整一阶域上成立。
对固定 $n$，$\delta_X^n(B^k)$ 是最多 $k^n$ 个有序项的和；
每项至多有 $n$ 个被求导的因子，其余原始 $B$ 因子可合并为至多 $n+1$ 个连续幂块。

给任意 $\theta>0$，准幂零性给
$$
\|B^\ell\|\le M_\theta\theta^\ell\quad(\ell\ge0).
$$
把每个连续幂块这样估计，并把固定阶导数因子分别取范数，得到
$$
\boxed{
\|\delta_X^n(B^k)\|
\le C_{n,\theta}(1+k)^n\theta^k
\quad(k\ge0).
}
\tag{4.1}
$$
常数可吸收至多 $n$ 个缺失原始因子及 $\theta^{-n}$；它与 $k$ 无关。

因此对每个 $z\ne0$，取 $0<\theta<|z|$ 后，
$$
(zI-B)^{-1}=\sum_{k\ge0}z^{-k-1}B^k
$$
及每个固定阶 $\delta_X$ 导数都按算子范数收敛。
对这些部分和使用闭图极限，逐阶得到实际逆保持域，以及相应有界导数。
在离 $0$ 正距离的固定轮廓上，可取同一 $\theta$，故这些收敛和估计一致。

所以若 $\psi$ 在零点邻域解析，通常全纯演算满足
$$
\psi(B)\in C^\infty(\delta_X)
\tag{4.2}
$$
，其中本稿的记号只表示每个固定阶导数有界且保持完整域，不声称一个额外的 Banach 代数范数或任意导数阶的一致常数。

应用于 $B=B_2^*$、$\psi(z)=\overline{\phi(\overline z)}$，得到
$$
\boxed{Y^*\in C^\infty(\delta_X).}
\tag{4.3}
$$
另一方面，$Y\in\mathcal A$ 与全部 $X_N$、$X$ 域交换，所以
$Y\in C^\infty(\delta_X)$，其正阶导数为零。

## 5. 分支自交换子对 $T$ 的全部固定阶域保持

二阶附录已经严格证明
$$
K_Y=[X^*,Y]\in B(H),\qquad
C_T=C_a-K_Y-K_Y^*+Y^*Y-YY^*.
\tag{5.1}
$$
还需验证 $K_Y$ 的高阶，而不能仅由其有界性作结。

置 $K_{Y,N}=[X_N^*,Y]$。二阶附录的 Bell 交换子估计对第一行系数线性连续，故
$$
K_{Y,N}\longrightarrow K_Y
$$
按算子范数收敛。更明确地，
$[X_N^*-X_M^*,B_2]$ 的范数由
$$
7776L_\eta\|a^{(N)}-a^{(M)}\|_2
\left(\sum_j|a_j|^4\right)^{1/2}
$$
控制，再经同一个固定全纯轮廓得到 $Y$ 的估计。

由于 $[X_N,Y]=0$，真实有界 Jacobi 恒等式给
$$
[X_N,K_{Y,N}]=-[C_N,Y],
$$
以及对每个 $r\ge1$，
$$
\operatorname{ad}_{X_N}^{\,r}K_{Y,N}
=-[\operatorname{ad}_{X_N}^{\,r-1}C_N,Y].
\tag{5.2}
$$
§2 和 (1.2) 因而给 $K_Y\in C^\infty(\delta_X)$。
同时由完整通常伴随域式，
$$
K_Y^*=-\delta_XY^*,
$$
故 (4.3) 给 $K_Y^*\in C^\infty(\delta_X)$。
由 Leibniz 公式，(5.1) 得
$$
C_T\in C^\infty(\delta_X).
\tag{5.3}
$$

令 $T=X-Y$。因为 $\delta_XY=0$，在上述完整域代数上
$$
\delta_T=\delta_X-\operatorname{ad}_Y,\qquad
[\delta_X,\operatorname{ad}_Y]=0.
$$
故有限二项式直接给
$$
\boxed{
\delta_T^rC_T\in B(H),\qquad
(\delta_T^rC_T)\operatorname{Dom}T
\subseteq\operatorname{Dom}T
\quad(r\ge0).
}
\tag{5.4}
$$
$C_T$ 自伴。取通常伴随的域判据还给
$$
\delta_{T^*}^{\,r}C_T
=(-1)^r(\delta_T^rC_T)^*,
\tag{5.5}
$$
以及每个算子对 $\operatorname{Dom}T^*$ 的真实保持。
因此两侧的固定阶导数条件均已支付。

## 6. 全部自然幂的通常伴随同域

先记一个域归纳事实。若 $B,\delta_TB,\ldots$ 满足 (5.4) 型条件，则对每个有限 $p$，
$$
B\operatorname{Dom}T^p\subseteq\operatorname{Dom}T^p,
$$
且
$$
T^pBf=\sum_{\ell=0}^p\binom p\ell
(\delta_T^\ell B)T^{p-\ell}f
\quad(f\in\operatorname{Dom}T^p).
\tag{6.1}
$$
对全部导数同时作归纳即可：每次将一阶域等式用于已经落入所需域的向量。
特别，$C_T$ 保持所有自然幂域。$T^*$ 一侧由 (5.5) 同样成立。

二阶附录已证明
$$
TT^*f=T^*Tf-C_Tf
\quad(f\in\operatorname{Dom}T^2)
$$
及 $\operatorname{Dom}T^2=\operatorname{Dom}(T^*)^2$。
对每个 $p\ge1$，进一步有
$$
\boxed{
T^*\operatorname{Dom}T^{p+1}
\subseteq\operatorname{Dom}T^p,
}
\tag{6.2}
$$
以及
$$
T^pT^*f
=T^*T^pf-
\sum_{\ell=0}^{p-1}
T^\ell C_TT^{p-1-\ell}f
\quad(f\in\operatorname{Dom}T^{p+1}).
\tag{6.3}
$$

为明确 (6.2) 的域，假设已经证到 $p-1$。
对 $f\in\operatorname{Dom}T^{p+1}$，
前阶公式的第一项是 $T^*T^{p-1}f$；
因 $T^{p-1}f\in\operatorname{Dom}T^2$，二阶结论使它属于 $\operatorname{Dom}T$。
其余各项由 (6.1) 也在 $\operatorname{Dom}T$。
因此 $T^{p-1}T^*f\in\operatorname{Dom}T$，
这支付了 (6.2)，再作用一次 $T$ 得 (6.3)。

反复使用 (6.2)，得到
$\operatorname{Dom}T^n\subseteq\operatorname{Dom}(T^*)^n$。
由 (5.5) 交换两侧，得到反向包含。因此
$$
\boxed{
\operatorname{Dom}T^n=\operatorname{Dom}(T^*)^n
\quad\text{对每个有限 }n\ge1.
}
\tag{6.4}
$$
同时，这个共同域中每个长度不超过 $n$ 的 $T,T^*$ 有序混合词均真实有定义：
每个 $T$ 或 $T^*$ 都将当前自然域阶数降低至多一。

本稿不声称某个单独混合词的最大定义域必等于这个共同自然域；
这里只给共同自然域上的完整混合词作用。

R176 已证明 $T^n$ 闭且 $C$ 自伴，准确域为 $\operatorname{Dom}X^n$。
所以 (6.4) 还使各固定阶共同自然域成为等价图范数的 Hilbert 空间。
每个上述混合词作为这一个固定阶图空间到 $H$ 的映射有界：
逐步把 $T,T^*$ 看作相邻完整图空间之间的全域闭映射即可。
不需要给所有阶数一个未经证明的统一常数。

## 7. 同一个未知核的两侧高阶正则性

设 $M=\ker T$，并有 R236 的等向条件 $M\perp CM$。
因为 $M$ 被 $T$ 杀掉，$CM=\ker T^*$ 被 $T^*$ 杀掉，(6.4) 给
$$
\boxed{
M\cup CM\subseteq
\bigcap_{n\ge1}\operatorname{Dom}T^n
=
\bigcap_{n\ge1}\operatorname{Dom}(T^*)^n.
}
\tag{7.1}
$$
每个 $T^n|_{CM}$、$(T^*)^n|_M$ 都是有界映射，理由是闭图定理和 R176 的真实自然幂闭性。
这只提供对每个固定 $n$ 的有限常数，不声称其随 $n$ 的增长是指数型。

令 $K=(M\oplus CM)^\perp$，仍写
$$
T=
\begin{pmatrix}
0&F&D_0\\0&T_K&H_1\\0&0&0
\end{pmatrix}.
$$
逐次使用 (7.1) 和真实三块域，归纳得到
$$
\boxed{
H_1(CM)\subseteq\bigcap_{r\ge1}\operatorname{Dom}T_K^r,
\qquad
F^*(M)\subseteq\bigcap_{r\ge1}\operatorname{Dom}(T_K^*)^r.
}
\tag{7.2}
$$
并且对每个固定 $r\ge0$，
$$
T_K^rH_1,\qquad (T_K^*)^rF^*
$$
都是全域有界的矩形算子。取伴随，$FT_K^r$ 在自然域上的作用也有有界延拓：
$$
\widehat{FT_K^r}=((T_K^*)^rF^*)^*.
\tag{7.3}
$$

这里的归纳没有跳过中央域：
$Tz=(D_0z,H_1z,0)$ 对 $z\in CM$；
它属于 $\operatorname{Dom}T^n$，所以其中央分量属于
$\operatorname{Dom}T_K^n$。
反向对一般 $(m,k,z)$ 再用 $H_1z$ 已具有的全部固定阶中央域，得到
$$
\boxed{
\operatorname{Dom}T^n
=M\oplus\operatorname{Dom}T_K^n\oplus CM.
}
\tag{7.4}
$$
对 $n\ge2$，准确块式为
$$
\boxed{
T^n=
\begin{pmatrix}
0&\widehat{FT_K^{n-1}}&FT_K^{n-2}H_1\\
0&T_K^n&T_K^{n-1}H_1\\
0&0&0
\end{pmatrix}
}
\tag{7.5}
$$
在 (7.4) 的完整域上成立，所有外块均有界。

比较通常伴随或使用 (6.4) 的同一个分解，亦得
$$
\operatorname{Dom}T_K^n=\operatorname{Dom}(T_K^*)^n.
\tag{7.6}
$$
这些具体中央自然幂闭性和 $C_K$ 自伴性还可从 (7.5)、R176 的 $T^n$ 及有界外块直接读出。
不将此自动外推为任意未建立域分解的商空间定理。

## 8. 对 $J_H$ 的全部正阶控制与尚未解决的零阶成本

现在再假设旧 $T_K$ 单射，并沿用
$$
D_H=\{c\in CM:H_1c\in\operatorname{Ran}T_K\},\qquad
J_Hc=T_K^{-1}H_1c,\qquad
\overline{D_H}=CM_0,\quad M_0=M\ominus N.
$$
由 (7.2)，对每个 $c\in D_H$，
$$
J_Hc\in\bigcap_{n\ge1}\operatorname{Dom}T_K^n,
\qquad
T_K^nJ_Hc=T_K^{n-1}H_1c.
\tag{8.1}
$$
于是对每个固定 $n\ge1$ 都有实际常数 $C_n<\infty$：
$$
\boxed{\|T_K^nJ_Hc\|\le C_n\|c\|\quad(c\in D_H).}
\tag{8.2}
$$
仍没有得到零阶估计 $\|J_Hc\|\le C\|c\|$。

若 $D_H$ 不是 $CM_0$ 中的闭子空间，则闭算子 $J_H$ 必在其定义域上无界。
可以取 $\|c_\nu\|=1$、$\|J_Hc_\nu\|\to\infty$，并置
$$
x_\nu=J_Hc_\nu/\|J_Hc_\nu\|.
$$
这些向量满足
$$
\boxed{
\|x_\nu\|=1,\qquad
x_\nu\in\bigcap_n\operatorname{Dom}T_K^n,\qquad
\|T_K^nx_\nu\|\to0
\quad\text{对每个固定 }n\ge1.
}
\tag{8.3}
$$
它们还弱收敛于零。事实上，任何弱收敛子列的极限 $x$ 连同
$T_Kx_\nu\to0$ 落在 $T_K$ 的弱闭图中，因此 $T_Kx=0$；
单射性给 $x=0$。可分 Hilbert 空间的弱序列紧性保证这就给整个有界序列的弱零性。

所以闭图分支若失败，其放大可以集中在中央算子的零谱尺度上，
并且所有固定正幂都同时看不见这个放大。
单凭 (8.2) 的任意多有限阶估计不能反推出 $J_H$ 有界。

前附录的正则图 $Q=\overline{P_{M_0}FT_K^{-1}}$ 也满足：
对每个固定 $r\ge1$，自然域上的
$$
QT_K^rx=P_{M_0}FT_K^{r-1}x
\quad(x\in\operatorname{Dom}T_K^r)
$$
具有有界延拓。它同样没有给 $Q$ 自身的通常范数界。

若相反 $D_H=CM_0$，则 $J_H$ 有界，并由 (8.1) 连续映入所有固定中央图域。
此前的有界斜投影及 $\delta:CM_0\to N$ 分支仍适用。
这份新高阶正则性尚未把该分支变成矛盾，也没有证明 $N=M$。

## 9. 适用范围与停止外推的位置

以上固定阶结论适用于任意复杂 $a\in\ell^2$ 和
$Y=\phi(B_2)$ 的实际解析分支，不要求相位一致或快速系数。
具体原危险点态平方与 $T$ 的核等式仍只引用 R208 §7 的 $a_*=0$ 设置。

本稿完成的事项是：

- 实际嵌套交换子的逐最大位绝对求和；
- 每阶弱式到真实完整域的传递；
- 准幂零全纯演算的逆域和导数；
- 两侧全部固定自然幂同域；
- 中央耦合在每个固定图域内的有界性。

没有完成的事项仍为：

- $H_1(CM)$ 是否足够落入 $\operatorname{Ran}T_K$；
- $D_H$ 是否闭，或 $J_H$ 是否有零阶有界估计；
- 旧中央核单射支是否可能，及原慢平方核是否为零。

因此后续需要的是实际逆尺度或相对零阶信息，而不是继续无控制地增加固定正幂的次数。


## 已核引用

- [R161：通常伴随同域与真实自交换子](../results/R161-first-chaos-adjoint-domain-and-selfcommutator.md)，完整图核心、极化式与跨位进位界。
- [R176：自然多项式的完整闭域与 C 自伴](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)，各固定自然幂的闭性和准确域。
- [R236 正则中央图附录](../results/R236-appendix-regular-central-range-graph-and-relative-coupling-estimate.md)，D_H、J_H、Q 的真实定义域和值域边界。
