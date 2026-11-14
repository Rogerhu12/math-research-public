# Newton 主面主导与临界最小 Gevrey 型的伴随矩阵定理

日期：2026-11-12（UTC）。子任务：critical_kernel。母会话预留结果号：**R75**。

**状态：下列抽象定理与所列实际范围已证明。** 本条接续冻结的 R71 稿，不修改该稿。它处理“原主变量仍然主导”的一侧，与 R69/R71 中有效横向尾主导的一侧互补。这里的横向尾无需具有固定相位，也无需自身满足负 BW 判据。

依赖：R60–R61 的严格负 BW 常数；R67 的核上矩阵搬运；R71 的加权 Newton 幂界；已逐式交叉核验的 [R74 精确幂范数稿](2026-11-12-all-power-gevrey-by-exact-norms-0c.md)。R74 使实际横向最小型可用于任意有限 $q>1$；没有扩大基准主指数的负 BW 范围 $1<p\le12/5$。

## 1. Gevrey 型与指数增长

对有界算子 $T$、正权 $\omega>0$，定义
$$
\mathfrak g_\omega(T)
=\limsup_{n\to\infty}
\bigl(\|T^n\|(n!)^\omega\bigr)^{1/n}.
\tag{1.1}
$$
称 $\mathfrak g_\omega(T)<\infty$ 为有限型，称
$\mathfrak g_\omega(T)=0$ 为最小型。

若 $\mathfrak g_\omega(T)=g<\infty$，则对每个 $\varepsilon>0$ 有固定 $K_\varepsilon$，使
$$
\|T^n\|\le K_\varepsilon
(g+\varepsilon)^n(n!)^{-\omega}\qquad(n\ge0).
\tag{1.2}
$$
令 $p=1+\omega$，非负数列的 $\ell^p$ 与 $\ell^1$ 比较给
$$
\|e^{tT}\|
\le K_\varepsilon
\sum_{n\ge0}\frac{[(g+\varepsilon)|t|]^n}{(n!)^p}
\le K_\varepsilon
\exp\{p[(g+\varepsilon)|t|]^{1/p}\}.
\tag{1.3}
$$
所以
$$
\limsup_{|t|\to\infty}
\frac{\log\|e^{tT}\|}{|t|^{1/p}}
\le p\,g^{1/p}.
\tag{1.4}
$$
特别是最小型时，对每个固定 $T_0$，
$$
\sup_{|t|\le T_0M^p}\log\|e^{tT}\|=o(M).
\tag{1.5}
$$
这个统一形式来自先固定 $\varepsilon$、再令 $M\to\infty$、最后令 $\varepsilon\downarrow0$。

### 1.1 有限交换和的最小型闭性

若有限个彼此交换的 $T_i$ 都是权 $\omega$ 的最小型，则它们的和仍是最小型。事实上，对任意 $\varepsilon>0$，取
$$
\|T_i^n\|\le K_i(\varepsilon)\varepsilon^n(n!)^{-\omega}.
$$
在多项式展开中，所有前常数仅乘成固定的
$\prod_iK_i(\varepsilon)$，不变成随 $n$ 增长的幂。用
$n!/\prod_i n_i!\le N^n$ 得
$$
\left\|\left(\sum_iT_i\right)^n\right\|
\le\left(\prod_iK_i(\varepsilon)\right)
[N^{\omega+1}\varepsilon]^n(n!)^{-\omega}.
$$
$\varepsilon$ 任意，故最小型成立。

若 $\omega'>\omega$ 且 $T$ 是权 $\omega'$ 的有限型，则它自动是权 $\omega$ 的最小型，因为
$(n!)^{-(\omega'-\omega)/n}\to0$。

## 2. 伴随矩阵的加权 factorial 估计

令 $b_0,\ldots,b_{r-1}$ 是 $\mathcal A$ 中彼此交换的算子，$r\ge1$。伴随矩阵采用明确的行列取向：
$$
C_{i,i+1}=I\quad(0\le i<r-1),\qquad
C_{r-1,j}=-b_j\quad(0\le j<r),
$$
其余条目为零。行列编号从 $0$ 开始。

置
$$
d_j=r-j,\qquad
N_r=\sum_{j=0}^{r-1}d_j=\frac{r(r+1)}2,\qquad
K_{r,\omega}=rN_r^\omega.
\tag{2.1}
$$

**定理 2.1。** 若 $\mathfrak g_{d_j\omega}(b_j)<\infty$，令
$$
G=\max_{0\le j<r}
\mathfrak g_{d_j\omega}(b_j)^{1/d_j},
$$
则
$$
\boxed{\mathfrak g_\omega(C)\le K_{r,\omega}G.}
\tag{2.2}
$$
因此若每个 $b_j$ 都是权 $d_j\omega$ 的最小型，则
$C$ 是权 $\omega$ 的最小型。特别地，$t=O(M^{1+\omega})$ 时
$\|e^{tC}\|=e^{o(M)}$。

**证明。** 固定 $\varepsilon>0$。由型的定义，可取统一有限常数 $K_\varepsilon$，使
$$
\|b_j^m\|\le K_\varepsilon
(G+\varepsilon)^{d_jm}(m!)^{-d_j\omega}
\quad(m\ge0,\ 0\le j<r).
\tag{2.3}
$$
一条长度 $n$、从列 $\ell$ 到行 $i$ 的矩阵路径，设其中末行第 $j$ 条边出现 $m_j$ 次。每条上对角边的成本为零，末行第 $j$ 条边的成本为 $d_j$；成本都是 $1+\text{行}-\text{列}$。因而
$$
D=\sum_jd_jm_j=n+i-\ell.
\tag{2.4}
$$
路径上的 $b_j$ 彼此交换，故其乘积范数不超过
$$
K_\varepsilon^r
(G+\varepsilon)^D
\prod_j(m_j!)^{-d_j\omega}.
$$
将 $m_j$ 重复为 $d_j$ 个组，总共有 $N_r$ 组、总计 $D$ 个对象。多项式系数界给
$$
\frac{D!}{\prod_j(m_j!)^{d_j}}\le N_r^D.
$$
所以每条路径至多
$$
K_\varepsilon^r
[(G+\varepsilon)N_r^\omega]^D(D!)^{-\omega}.
\tag{2.5}
$$
长度 $n$ 的路径数至多 $r^{n-1}$；用 $r$ 倍最大条目控制整体矩阵范数。对 $n\ge r-1$，$D$ 总在
$[n-r+1,n+r-1]$ 中。$D-n$ 有固定界，所以
$$
\left(\frac{n!}{D!}\right)^{\omega/n}\to1,
\qquad
D/n\to1
$$
一致成立。对 (2.5) 取 $n$ 次根并乘上 $(n!)^{\omega/n}$，得到
$$
\mathfrak g_\omega(C)\le
rN_r^\omega(G+\varepsilon).
$$
令 $\varepsilon\downarrow0$，即得 (2.2)。

有限项 $n<r-1$ 只给指数级数中的一个固定多项式因子，不影响任何型或主时间尺度。证明未使用 $B^{-1}$、形式开根或有界除法。证毕。

## 3. 带定量余量的实际 BW 矩阵判据

固定 R61 的基准对数 $L$，其一阶尾为
$\theta_j=(j+2)^{-p}$，$1<p\le12/5$，并令 $\omega=p-1$。考虑
$$
P(L)=L^r+\sum_{j=0}^{r-1}b_jL^j,
$$
其中每个 $b_j\in\mathcal A$。设定理 2.1 的型有限。

取已认证区间及函数：
$$
[a,b]=
\begin{cases}
[1,20],&1<p\le2,\\
[1/10,30],&2<p\le12/5,
\end{cases}
$$
$$
J_p=g_{a,b}+\int h_p\,d\nu_{a,b}<0,\qquad
I_p=\int_a^b u^{1/p}\,d\nu_{a,b}(u).
$$

**定理 3.1。** 若
$$
\boxed{
J_p+p(K_{r,p-1}G)^{1/p}I_p<0,}
\tag{3.1}
$$
则 $P(L)$ 单射且值域稠密。特别地，$G=0$ 总满足该条件。

**证明。** 若 $P(L)f=0$，令
$$
\mathbf f=(f,Lf,\ldots,L^{r-1}f).
$$
则 $(LI_r-C)\mathbf f=0$，进而
$e^{tL}\mathbf f=e^{tC}\mathbf f$。

按 R67 取 $M=m+2$、$k=\lfloor(3/4)\log_2M\rfloor$，并把真实近似写为
$$
T_k=H_{k,m}+C_m,\qquad
C_m=\sum_{j\ge m}\theta_jE_j.
$$
逐坐标有
$$
e^{tH_{k,m}}\mathbf f-
e^{-tC_m}e^{tC}\mathbf f
=e^{-tC_m}(e^{tT_k}-e^{tL})\mathbf f.
\tag{3.2}
$$
实际误差为
$\exp[-cM^3+O(M^p+\log M)]\|\mathbf f\|$；没有要求伴随矩阵与近似头尾交换。

由 (1.3)、(2.2)，对任意 $\delta>0$，在 $t=uM^p$ 的整个区间上一致有
$$
\log\|e^{tC}\|
\le p(K_{r,p-1}G+\delta)^{1/p}u^{1/p}M+o(M).
$$
因此每个坐标的标量头多项式，次数至多 $M+M^{3/4}$，边界为
$$
\|\mathbf f\|
\exp\left\{
M\left[h_p(u)+
p(K_{r,p-1}G+\delta)^{1/p}u^{1/p}\right]+o(M)
\right\}.
$$
尾范数下界 $e^{-CM}$ 吸收 (3.2) 的误差。条件 (3.1) 允许选取固定小 $\delta$，使 BW 指数仍严格为负。核均值为零，再由 $A$ 不变性及 $1$ 对 $A^*$ 循环得核为零。复对称性给稠密值域。证毕。

若只想使用证书的有理余量，可取
$$
\kappa_p=
\begin{cases}
13/100,&1<p\le2,\\
1/2000,&2<p\le12/5.
\end{cases}
$$
已证 $J_p\le-\kappa_p$，且 $I_p\le b^{1/p}$。于是一个更保守但明确的充分条件为
$$
\boxed{
G<\frac{\kappa_p^p}
{p^p K_{r,p-1}b}.}
\tag{3.3}
$$
这个定量条件允许非零有限型，而非仅仅最小型；它没有假设所有临界幅度都足够小。

## 4. Newton 唯一主项与临界最小型主面的定理

设横向变量 $Y_\ell\in\mathcal A$ 具有有限 Gevrey 型，权为 $\omega_\ell>0$。把部分变量标记为“最小型变量”，即对这些变量有
$\mathfrak g_{\omega_\ell}(Y_\ell)=0$。

给形式变量 $w$ 权 $\omega_0=p-1$，给 $y_\ell$ 权 $\omega_\ell$。设解析芽 $F(w,y)$ 满足：

1. $F(w,0)$ 在 $0$ 的零点阶恰为 $r$，其 $w^r$ 系数 $c\ne0$；
2. 全部非零 Taylor 单项式的加权次数至少为 $r\omega_0$；
3. 加权次数恰为 $r\omega_0$ 的每个单项式，除 $cw^r$ 外，都包含至少一个最小型横向变量。

**定理 4.1。** 在这些假设下，
$$
\boxed{F(L,Y)\text{ 单射且值域稠密。}}
\tag{4.1}
$$

**证明。** 作 Weierstrass 分解
$$
F(w,y)=U(w,y)\left[w^r+\sum_{j=0}^{r-1}b_j(y)w^j\right],
\qquad U(0)\ne0.
$$
正权保证每个有界权范围内只含有限个单项式。单位不改变最低加权次数；在最低权上，乘法只乘上 $U(0)$。因此每个 $b_j$ 的单项式权至少为
$$
(r-j)\omega_0,
\tag{4.2}
$$
而恰好达到此权的单项式，除以固定非零 $U(0)$ 后，正好来自 $F$ 的临界主面，故都含有一个标记的最小型变量。

现证明 $b_j(Y)$ 是权 $(r-j)\omega_0$ 的最小型。达到临界权的项只有有限个。每个这样的单项式中，一个实际变量是其自身权上的最小型，其余变量是有限型；用交换幂乘积和 $(kn)!\ge(n!)^k$，得到该单项式在总权上的最小型。剩余高权级数与临界权之间有一个严格正间隔；R71 的解析 Newton 理想定理给它在更大权上的有限型，因此在临界权上是最小型。最后用第 1.1 节的有限和闭性即可。

定理 2.1 遂给伴随矩阵的 $G=0$，定理 3.1 给 Weierstrass 多项式单射稠密；单位因子可逆，结论成立。证毕。

### 4.1 唯一最小权项

若 $cw^r$ 是 $F$ 唯一的最小权项，则第 3 条无须标记任何变量；所有其他项严格高于主面。因此只需有限型即可。

等价地，Weierstrass 系数满足严格权不等式
$$
\operatorname{wt}(b_j)>(r-j)(p-1).
$$
可以选取固定 $\omega_*>p-1$，使全部系数在权 $(r-j)\omega_*$ 上有限型。于是
$$
\log\|e^{tC}\|=O(|t|^{1/(1+\omega_*)}),
$$
在 $t=O(M^p)$ 上为 $o(M)$。这给另一种直接查看严格主项优势的形式。

### 4.2 与已有总次数定理的关系

若全部横向变量都是权 $p-1$ 的最小型，则“全部总次数低于 $r$ 的项消失”正是第 2 条；每个临界的非纯 $w^r$ 项自动含最小型变量。因此 R69 的总次数定理是本条的一个等权特例。

## 5. 真实局部尾的最小型：任意有限权

R74 已证明：若
$$
Y=\psi(A)+\sum_{j\ge J}f_j(N_j),\qquad
f_j(z)=\xi_jz+\sum_{n\ge2}a_{j,n}z^n,
$$
其中 $\psi$ 是实际零常数标量解析芽，且有统一几何界
$$
|a_{j,n}|\le\Gamma S^{n-1},
$$
则对任意固定有限 $q>1$，有
$$
\xi_j=O(j^{-q})
\quad\Longrightarrow\quad
\mathfrak g_{q-1}(Y)<\infty,
\tag{5.1}
$$
$$
\boxed{
\xi_j=o(j^{-q})
\quad\Longrightarrow\quad
\mathfrak g_{q-1}(Y)=0.}
\tag{5.2}
$$
这些结论对复系数直接成立。

说明 R74 何以取消早先的 $q<4$ 上限：真实全幂范数给
$$
\|N_j^n\|\le
\exp\!\left(n\Lambda_j-\tfrac54\,16^j n^4\right),
\qquad \Lambda_j=O(16^j).
$$
因此低位局部指数的对数界为
$$
O(16^{-j/3}\log^{4/3}(2+|t|)+16^j).
$$
取 $k\asymp\log\log(2+|t|)$，低位总贡献仅为
$O(\log^{4/3}(2+|t|))$。高位用真实进位恒等式得到
$$
\|e^{t\xi_jN_j}\|
\le(1+|t\xi_j|)
\exp(|t\xi_j|\sqrt{\eta_j})
$$
的乘积型上界。
高次项的范数为 $O(\Gamma\eta_j)$。相互交换的实际局部指数分解遂给
$$
\log\|e^{tY}\|
\le C\log^{4/3}(2+|t|)
+\sum_{j\ge k(t)}\log(1+|t\xi_j|).
\tag{5.3}
$$
若 $\xi_j=o(j^{-q})$，后者为 $o(|t|^{1/q})$，且关于复方向一致。
算子值整函数 $e^{zY}$ 的 Cauchy 系数界再给 (5.2)；不需要正性，也不使用早先的 $e^{C|t|}$ 型 Duhamel 误差。

对本条实际 $R_i=L_i-c_iL$，其一阶余项正是
$\epsilon_{i,j}$；高次局部系数满足更强的
$O(j^{-p})S^{n-1}$ 界，故满足 R74 的统一几何条件。高次真实进位全部保留。$A$ 自身在每个有限 $q>1$ 下也属于最小型。

## 6. 不规则复次主尾下的全部高阶主矩取消

令
$$
X=\sum_i a_i(A)e^{-L_i},\qquad
L_i=c_iL+R_i,\quad \alpha_i=a_i(0).
$$
若最小的非零主矩阶为 $r=0$，常数项非零，算子直接可逆。以下假设该阶为 $r\ge1$：
$$
\sum_i\alpha_ic_i^k=0\quad(0\le k<r),
\qquad
\sum_i\alpha_ic_i^r\ne0.
\tag{6.1}
$$
定义临界横向指数
$$
q_*=1+r(p-1).
\tag{6.2}
$$

若
$$
\epsilon_{i,j}=o((j+2)^{-q_*})
\quad\text{对全部 }i,
\tag{6.3}
$$
其中 $\epsilon_{i,j}$ 是 $R_i$ 的实际一阶局部尾，则
$$
\boxed{X\text{ 单射且值域稠密。}}
\tag{6.4}
$$

**证明。** 给 $w=L$ 权 $p-1$；给 $A,R_i$ 权
$q_*-1=r(p-1)$。由第 5 节，这些横向变量都是最小型。解析芽
$$
F(w,y)=\sum_i a_i(y_0)e^{-c_iw-y_i}
$$
的纯 $w$ 项在 $r$ 阶以下消失，且 $w^r$ 系数非零，来自 (6.1)。所有含横向变量的项权至少为 $r(p-1)$，在临界权上的项都含最小型变量。定理 4.1 适用。证毕。

特别地，**真正双重取消**时 $r=2$，$q_*=2p-1$。因此只要全部独立次主尾满足
$$
\boxed{\epsilon_{i,j}=o((j+2)^{-(2p-1)}),}
\tag{6.5}
$$
即使它们完全不规则、持续变相位，也能处理全部二阶临界组合。无需其一次合成尾有幂律或负 BW 结构。

一个更容易检查的严格版本是
$$
\epsilon_{i,j}=O((j+2)^{-q}),\qquad q>2p-1.
$$
选择 $2p-1<\widetilde q<q$，给横向变量有限型权 $\widetilde q-1$；$w^2$ 成为唯一最小权项，亦可直接用第 4.1 节。

若有 $N$ 个两两不同的 $c_i$，Vandermonde 矩阵保证每个非零常数系数组的首次非零主矩阶 $r\le N-1$。所以一个统一的有限充分条件为
$$
\boxed{
\epsilon_{i,j}
=o\!\left(j^{-[1+(N-1)(p-1)]}\right)
\quad\text{对全部 }i.}
$$
有限前缀已经合法提出共同最小 $A$ 次幂后，剩余常数系数不全为零；因而这个条件保证**全部非平凡有限线性组合均单射稠密，从而相应乘积和非零且循环**。

更强但容易识别的例子是全部独立次主尾比每个负幂都快，即对每个有限 $q>1$ 都满足 $\epsilon_{i,j}=o(j^{-q})$。它自动满足每个有限 $N$ 的上述条件。不再需要 R71 超快低位分支的双指数衰减假设；任意相位的 $e^{-\sqrt j}$、$e^{-(\log(j+3))^2}$ 等超多项式尾均在此范围内。

这与 R69 的有效横向主导侧形成互补：

- 若实际合成尾具有可证 BW 指数 $q<2p-1$，使用横向主导；
- 若各独立尾都是 $o(j^{-(2p-1)})$，使用原主变量的临界最小型；
- 在临界有限非零型上，定理 3.1 还给明确的小型余量条件，但不能自动宣布它总成立。

仍未覆盖的一般情形包括：合成横向尾既不具已证 BW 结构，各独立尾又大于或处于不能满足小型条件的临界尺度。这里没有把这些不规则情形默认成正则尾。

## 7. 范围说明

所有矩阵幂和指数估计均在实际有界算子上成立；没有进行形式分母除法。解析 WPT 只用于生成真实的有界矩阵系数，随后每一步均有范数控制。BW 搬运保留了实际进位误差与复对称的稠密值域结论。

对 R16 乘积的任意有限前缀，仍应保留相应解析系数 $a_i(A)$、非零尾归一化常数和共同循环锚，先合法提出有限多项式的共同最小 $A$ 次幂，再按 (6.1) 实际计算主矩。所列条件给这些具体有限乘积和的非零循环性，不是一般 Hilbert ISP 的完成证明。

