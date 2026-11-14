# 两个不同幂尾的三变量芽商忠实性与轴商的全平面谱

日期：2026-11-12（UTC）。子任务：critical_kernel。母会话预留结果号：**R83**。

**状态：以下真实值域包含判据、具体闭轴商的空预解集及谱分类已证明。** 一般三变量芽算子的单射性没有被假定或宣布；临界轴商的点谱仍与实际核问题对应。

## 1. 模型与范围

固定 $1<p<q<\infty$，使用实际算子
$$
L_s=\sum_{j\ge0}\gamma_{s,j}(N_j),\quad
\gamma_{s,j}(x)=\log(1+x)-\log(1+(1-\theta_{s,j})x),\quad
\theta_{s,j}=(j+2)^{-s}.
$$
这些级数与局部解析界对所有 $s>1$ 成立；代数/值域部分不需要各指数已有负 BW 证书。记
$$
\mathscr O_3=\mathbb C\{z,w,v\},\quad
\ell_s(z)=\sum_j\gamma_{s,j}(z^{2^j}/d_j),\quad
d_j=W_{2^j},\quad\Lambda_j=-\log d_j.
$$
$\ell_s$ 只被当作形式级数，不声称在非零圆盘收敛。

将证明形式曲线 $(z,\ell_p,\ell_q)$ 对 $\mathscr O_3$ 忠实，且对非零 $F,G\in\mathscr O_3$，
$$
\boxed{
\operatorname{Ran}F(A,L_p,L_q)\subseteq
\operatorname{Ran}G(A,L_p,L_q)
\iff F/G\in\mathscr O_3.}
\tag{1.1}
$$
这只判定任意有界因子的存在性。若一般 $G(A,L_p,L_q)$ 有核，有界解可以不唯一；不能预设解属于交换子，更不能先约去 $G$。

## 2. 实际有界因子的形式入口，不要求交换性或单射

沿用 R49/R68 的等距含单位 $*$-表示
$$
\pi:C^*(I,A)\longrightarrow B(\ell^2(\mathbb N_0)),
$$
其中
$$
\pi(A)e_k=a_{v_2(k+1)}e_{k+1},\qquad
\pi(A)^ne_k=\frac{W_{n+k}}{W_k}e_{n+k}.
$$
有限变量范数解析演算与连续形式系数相容：
$$
c(F(A,L_p,L_q))=F(z,\ell_p(z),\ell_q(z)).
\tag{2.1}
$$

**引理 2.1。** 假设形式分母 $G(z,\ell_p,\ell_q)$ 非零。若任意 $B\in B(H)$ 满足
$$
G(A,L_p,L_q)B=F(A,L_p,L_q),
$$
则形式 Laurent 商 $R(z,\ell_p,\ell_q)=F(z,\ell_p,\ell_q)/G(z,\ell_p,\ell_q)$ 无负阶。写为 $\sum r_nz^n$ 后，
$$
\boxed{|r_n|W_n\le\|B\|.}
\tag{2.2}
$$

**证明。** 从实际关系直接得 $FF^*\le\|B\|^2GG^*$。这里只把 $F,G$ 及该正序不等式通过 $\pi$ 转移，不对任意 $B$ 应用 $\pi$。

在 $\operatorname{Ran}\pi(G)^*$ 上定义
$S(\pi(G)^*x)=\pi(F)^*x$。正序界使它良定义、有界，范数至多 $\|B\|$。延伸到该值域闭包并在正交补置零，取伴随 $T=S^*$，得到
$$
\pi(G)T=\pi(F),\qquad\|T\|\le\|B\|.
$$
写 $Te_0=\sum b_nW_ne_n$，则 $|b_n|W_n\le\|B\|$。下三角逐坐标比较给
$$
G(z,\ell_p,\ell_q)\sum_{n\ge0}b_nz^n=F(z,\ell_p,\ell_q).
$$
每个坐标只含有限项。非零形式分母的 Laurent 商唯一，故结论成立。证毕。

没有使用 $G[A,B]=0$，没有假设 $B$ 与 $A$ 交换，也没有假设 $G$ 单射。

## 3. 三变量形式可除性与负阶导数

**引理 3.1。** 若 $F,G$ 收敛、$G\ne0$，且 $F=GQ$ 对某个三变量形式幂级数 $Q$ 成立，则 $Q$ 收敛。

**证明。** 取可逆线性坐标变换，使 $G$ 对最后变量 $u$ 正规；可取其最低非零齐次项不为零的方向作为 $u$ 轴。Weierstrass 准备给 $G(y,u)=U(y,u)P(y,u)$，其中 $U$ 为单位，$P$ 是 $u$ 的 $d$ 次首一多项式，其余系数在 $y=0$ 处为零。

为自含说明解析除法，取小圆 $|\zeta|=\rho$，使 $P(y,\zeta)$ 对小参数不为零。令 $f=F/U$，并定义
$$
Q_{\rm an}(y,u)=\frac1{2\pi i}\int
\frac{f(y,\zeta)}{P(y,\zeta)(\zeta-u)}\,d\zeta,
$$
$$
R_{\rm an}(y,u)=\frac1{2\pi i}\int
\frac{f(y,\zeta)}{P(y,\zeta)}
\frac{P(y,\zeta)-P(y,u)}{\zeta-u}\,d\zeta.
$$
二者解析，$\deg_uR_{\rm an}<d$，且 Cauchy 公式给
$f=PQ_{\rm an}+R_{\rm an}$。

形式除法唯一性可逐次模参数理想证明：若 $PQ_0+R_0=0$、$\deg_uR_0<d$，模 $(y)$ 时 $P=u^d$，故 $Q_0,R_0$ 都模 $(y)$ 为零。再逐次模 $(y)^n$，仍由 $u^d$ 项迫每一层为零。形式环中这些理想的交为零。比较已给的形式除法与上述解析除法，得 $R_{\rm an}=0$、$Q=Q_{\rm an}$。证毕。

这没有使用二变量中清分母所得的 $z^N$ Bézout 关系。

**引理 3.2。** 假设 $G(z,\ell_p,\ell_q)\ne0$。若 $R=F/G$ 非全纯，则某个有限混合横向导数
$\partial_w^\alpha\partial_v^\beta R$ 沿形式曲线具有负阶。

**证明。** 若全部这些导数沿曲线无负阶，则
$R(z,\ell_p(z)+s,\ell_q(z)+t)$ 的形式 Taylor 系数全在 $\mathbb C[[z]]$ 中，所得展开属于 $\mathbb C[[z,s,t]]$。合法连续形式平移
$s=w-\ell_p(z)$、$t=v-\ell_q(z)$ 给 $F/G$ 的形式幂级数实现。引理 3.1 迫它解析，矛盾。证毕。

## 4. 连续高位即可检出二方向对称张量

记 $\delta_j=((j+2)^{-p},(j+2)^{-q})$。

**引理 4.1。** 对非零对称 $d$ 重线性型 $T$，$d\ge1$，存在 $\kappa>0$、$b\ne0$，使
$$
\boxed{
T(\delta_J,\ldots,\delta_{J+d-1})
=bJ^{-\kappa}(1+o(1)).}
\tag{4.1}
$$

**证明。** 令
$$
a_k=T(e_1^{\,d-k},e_2^{\,k}),\quad0\le k\le d,
$$
并取最小的 $k_0$ 使 $a_{k_0}\ne0$。展开给
$$
T(\delta_J,\ldots,\delta_{J+d-1})
=
\left(\prod_{i=0}^{d-1}(J+i+2)^{-p}\right)
\sum_{k=0}^da_k e_k\bigl((J+i+2)^{-(q-p)}:0\le i<d\bigr).
$$
$e_k$ 为初等对称多项式，且
$e_k=\binom dkJ^{-k(q-p)}(1+o(1))$。因为 $q-p>0$，最低非零 $k_0$ 给唯一最慢幂次：
$$
b=\binom d{k_0}a_{k_0},\qquad
\kappa=p(d-k_0)+qk_0.
$$
证毕。

因而两尾不需要不同倍数的远位，连续高位的斜率变化已足够。$p\ne q$ 不可删除。

## 5. 混合高位系数的精确主项与错误项

令 $R=F/G$ 已有非零形式分母。固定总导数阶 $d\ge1$，并取
$$
t=\min_{\alpha+\beta=d}
\operatorname{ord}_z
[(\partial_w^\alpha\partial_v^\beta R)(z,\ell_p,\ell_q)],
$$
忽略恒零分量，假设至少一个非零。令 $T$ 是这些导数在固定次数 $z^t$ 上的非零对称系数张量。置
$$
N_J=\sum_{j=J}^{J+d-1}2^j,\qquad
P_J=\sum_{j=J}^{J+d-1}\Lambda_j.
$$
则
$$
[z^{N_J+t}]R(z,\ell_p,\ell_q)
=e^{P_J}T(\delta_J,\ldots,\delta_{J+d-1})
+\sum_{j=J}^{J+d-1}E_{J,j},
\tag{5.1}
$$
其中
$$
|E_{J,j}|
\le C_d\exp\left(
\sum_{i=j+1}^{J+d-1}\Lambda_i+\frac35\Lambda_j\right).
\tag{5.2}
$$

### 5.1 同时控制两个低位曲线

令 $\ell_{s,<k}=\sum_{j<k}\gamma_{s,j}(z^{2^j}/d_j)$，取 R68 的外圆
$$
r_k=\tfrac12e^{-\Lambda_{k-1}/2^{k-1}},\qquad\rho_k=r_k^2.
$$
外圆上全部低位输入由 $2^{-2^j}$ 支配，对每个固定 $j$ 趋零。因此两个曲线都一致趋零。

若形式分母首阶为 $g$，其固定有限 jet 最终与低位截断相同。R68 的外圆 Cauchy 界、内圆主项比较与辐角原理于是原样给：内圆中除原点 $g$ 阶零点外无其他零点。每个固定混合导数的分母为 $G^{\alpha+\beta+1}$、分子解析，所以
$$
\left|[z^n]R_{\alpha,\beta}(z,\ell_{p,<k},\ell_{q,<k})\right|
\le C_{\alpha,\beta}
\rho_k^{-n-g(\alpha+\beta+1)}.
$$
对 $\alpha+\beta\le d$、$n\le2^{k+1}+|t|$，因
$\Lambda_k\ge16\Lambda_{k-1}$，得到
$$
\left|[z^n]R_{\alpha,\beta}(z,\ell_{p,<k},\ell_{q,<k})\right|
\le e^{(3/5)\Lambda_k}
\tag{5.3}
$$
对充分大 $k$ 成立。增加一个曲线坐标不改变这个指数预算。

### 5.2 高阶分支严格不贡献

任意 $h$ 阶混合导数沿低位曲线的形式阶至少为 $-g(h+1)$。第 $k$ 位向量增量的两个分量都从 $2^k$ 阶开始，其至少二次 Taylor 分支的阶至少为
$$
2^{k+1}-g(h+3).
$$
当前目标次数为
$$
\sum_{i=J}^k2^i+t\le2^{k+1}-2^J+t.
$$
当 $2^J>|t|+g(d+3)$ 时，二次以上分支严格超出目标。一次分支中局部函数的二次以上项同样从 $2^{k+1}$ 阶开始，也不贡献。高于最后选定位的全部局部项也由同一形式阶界排除。

因此每层只剩零次项与精确的一次方向导数
$$
d_k^{-1}D_{\delta_k},\qquad
D_{\delta_k}=\theta_{p,k}\partial_w+\theta_{q,k}\partial_v.
$$
连续取到全部一次分支给 (5.1) 主项；第一次选择零次分支只可能发生在 $d$ 个选定位之一，给出恰好 $d$ 个错误项。残余方向导数是有限阶混合偏导的线性组合，系数由 $|\theta_{s,j}|\le1$ 一致控制，故 (5.3) 给 (5.2)。

末端固定的 $z^t$ 系数确为全曲线的 $T$，因为高位截断不改变任何固定有限 Laurent jet。没有遗漏同一高位的多次项。

### 5.3 归一化真实系数发散

引理 4.1 给主项模 $e^{P_J}|b|J^{-\kappa}(1+o(1))$。每个错误项与之之比至多
$$
C J^\kappa
\exp\left(\frac35\Lambda_j-\sum_{i=J}^j\Lambda_i\right)
\le C J^\kappa e^{-(2/5)\Lambda_J}\to0.
$$
所以
$$
\boxed{
[z^{N_J+t}]R(z,\ell_p,\ell_q)
=b e^{P_J}J^{-\kappa}(1+o(1)).}
\tag{5.4}
$$

若 $t=-s<0$，R13/R70 的实际二进位权恒等式为
$$
W_{N_J-s}=\frac{e^{-P_J}}{a_JW_{s-1}}.
$$
故
$$
\boxed{
[z^{N_J-s}]R(z,\ell_p,\ell_q)W_{N_J-s}
=
\frac{bJ^{-\kappa}}{a_JW_{s-1}}(1+o(1)),
}
\tag{5.5}
$$
其模趋于无穷。这里仅在形式系数中作代数，没有在 Hilbert 空间上作形式除法。

## 6. 形式忠实性与真实值域包含判据

**定理 6.1。** 每个非零 $H\in\mathscr O_3$ 满足
$$
H(z,\ell_p,\ell_q)\ne0,\qquad H(A,L_p,L_q)\ne0.
\tag{6.1}
$$

**证明。** 若沿曲线为零，则存在有限正阶 $d$ 的横向混合导数沿曲线非零；否则全部 Taylor 系数为零，经形式平移会迫使 $H=0$。取该阶的最低形式次数 $t\ge0$ 及非零张量，在第 5 节取分母一，(5.4) 给原 $H$ 沿曲线的一列非零系数，矛盾。算子结论由 (2.1) 得到。证毕。

**定理 6.2。** 对非零 $F,G$，以下等价：
$$
F/G\in\mathscr O_3;
\quad
\exists B\in B(H),\ F(A,L_p,L_q)=G(A,L_p,L_q)B;
\quad
\operatorname{Ran}F(A,L_p,L_q)\subseteq\operatorname{Ran}G(A,L_p,L_q).
\tag{6.2}
$$

**证明。** 第一项经解析演算推出第二项，再推出第三项。若第三项成立，为每个 $x$ 选取 $Gy=Fx$ 在 $(\ker G)^\perp$ 中的唯一解 $y=Bx$。该处处定义线性映射的图闭合，故 $B$ 有界；此步不要求 $G$ 单射。

最后若第二项成立，定理 6.1 保证形式分母非零。非全纯商由引理 3.2 有有限混合导数负阶。若原商已有负阶，引理 2.1 直接矛盾；否则取某个有负阶的正总导数阶，第 5 节的 (5.5) 违反 (2.2)。故商全纯。证毕。

一般 $G$ 的有界解可能因核而不唯一；不将存在性判据误写成所有解都属于 $\mathcal A$。

## 7. 具体闭轴商与空预解集

额外取 $1<p<q\le12/5$，使两个 $L_p,L_q$ 已由 R61 证明单射稠密。固定整数 $r\ge1$，定义
$$
X=L_q^{-1}L_p^r,\qquad
\operatorname{Dom}X=\{f:L_p^rf\in\operatorname{Ran}L_q\}.
\tag{7.1}
$$
它闭合：$f_n\to f,Xf_n\to g$ 时，$L_p^rf=L_qg$，所以 $f$ 属于定义域且 $Xf=g$。

因为
$$
L_qH\subseteq\operatorname{Dom}X,\qquad X(L_qh)=L_p^rh,
$$
它稠密定义、单射且值域稠密。反向最大商 $L_p^{-r}L_q$ 是其实际逆，含精确逆图定义域。芽 $w^r/v$ 与 $v/w^r$ 均非全纯；由定理 6.2，两个方向都不可能有界，其定义域也都不是全空间。

**定理 7.1。**
$$
\boxed{\rho(X)=\varnothing,\qquad\sigma(X)=\mathbb C.}
\tag{7.2}
$$

**证明。** 若 $\lambda$ 为预解点，则 $B=(X-\lambda)^{-1}\in B(H)$，并有
$$
(L_p^r-\lambda L_q)B=L_q.
$$
定理 6.2 迫 $v/(w^r-\lambda v)$ 全纯。$\lambda=0$ 时 $w^r$ 不整除 $v$；$\lambda\ne0$ 时，在假定的解析可除恒等式中置 $v=w^r/\lambda$，给 $0=w^r/\lambda$，矛盾。证毕。

同一值域判据还说明 $X-\lambda$ 对每个 $\lambda$ 都非满射：否则每个 $L_qg$ 都属于 $\operatorname{Ran}(L_p^r-\lambda L_q)$，又产生被排除的值域包含。

### 7.1 严格保留未知点谱

精确地，
$$
\boxed{\ker(X-\lambda)=\ker(L_p^r-\lambda L_q).}
\tag{7.3}
$$
右边向量自动属于定义域，所以包含定义域问题。

若此核为零，$L_p^r-\lambda L_q\in\mathcal A$ 的复对称性给其值域稠密。又
$$
(X-\lambda)(L_qh)=(L_p^r-\lambda L_q)h,
$$
所以 $X-\lambda$ 的值域稠密但非满射，即连续谱。若核非零，则为点谱。采用互不相交的谱分类，
$$
\boxed{
\sigma_p(X)=\{\lambda:\ker(L_p^r-\lambda L_q)\ne0\},\quad
\sigma_c(X)=\mathbb C\setminus\sigma_p(X),\quad
\sigma_r(X)=\varnothing.}
\tag{7.4}
$$
没有把空预解集误写为无条件的全平面连续谱。

## 8. 非临界与临界的区别

令 $q_*=1+r(p-1)$。若 $q<q_*$，以已证的 $L_q$ 作 BW 主变量，$L_p^r$ 的 Gevrey 权 $r(p-1)>q-1$ 给主时间上的 $e^{o(M)}$ 增长；R69 的实际搬运处理全部非零系数。若 $q>q_*$，给 $L_p$ 权 $p-1$、$L_q$ 权 $q-1$，$w^r+cv$ 的唯一最低权项是 $w^r$；R75 处理全部系数。零系数由 $L_p$ 单射直接处理。

因此
$$
q\ne1+r(p-1)
\ \Longrightarrow\
\boxed{\sigma(X)=\sigma_c(X)=\mathbb C,\quad\sigma_p(X)=\varnothing.}
\tag{8.1}
$$

临界情形的核仍须实质论证。R75 的小型判据排除零附近的一整个点谱邻域；$r=2$ 时 R82 又排除所有足够大模长及更优复外部区域。因此临界平方商的可能点谱被限制在一个有界环形区域内，但本条不证明它为空。被排除点谱的参数是连续谱点，而不是预解点。

## 9. 二阶轴商的明确高位见证

写
$$
\ell_q(z)=\beta z+\cdots,\qquad\beta=2^{-q}/d_0\ne0.
$$
对 $R(w,v)=w^2/v$，有
$$
\partial_w^2R=2/v=(2/\beta)z^{-1}+\cdots.
$$
同阶中含 $q$ 方向的贡献按更快负幂衰减，所以
$$
[z^{3\cdot2^J-1}]R(z,\ell_p,\ell_q)W_{3\cdot2^J-1}
=\frac{2}{\beta a_J}J^{-2p}(1+o(1)).
\tag{9.1}
$$
这直接排除任意有界 $L_qB=L_p^2$。

对 $\lambda\ne0$，
$$
R_\lambda(w,v)=\frac{v}{w^2-\lambda v}
=-\lambda^{-1}-\frac{w^2}{\lambda^2v}+\cdots.
$$
其 $\partial_w^2$ 的首极点为 $-2/(\lambda^2\beta)z^{-1}$；其余更高项在这个导数阶没有负阶。因此
$$
[z^{3\cdot2^J-1}]R_\lambda(z,\ell_p,\ell_q)W_{3\cdot2^J-1}
=-\frac{2}{\lambda^2\beta a_J}J^{-2p}(1+o(1)).
\tag{9.2}
$$
$\lambda=0$ 时 $v/w^2$ 本身已有负形式阶。预解集排除因此有具体真实带权系数发散见证。

## 10. 边界

本条的三变量忠实性指解析关系及真实有界值域因子的忠实性，不是一般三变量芽算子全部单射。没有把二变量图芯、Bézout 或完整解析分式谱分类未经证明搬到三变量。

具体轴商的闭性、稠密域、逆图、预解集与谱种类各有独立论证。它们解释为何排除许多临界核参数仍不能得到有界预解；不构造新的不变子空间，不宣称一般 Hilbert ISP 完成。

