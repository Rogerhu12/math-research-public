# R294：出生一全部高度的共同对角比较与真实端点 Newton 正块

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态：以下文献应用、共同代理相邻序及有限／无限行的夹逼已证明。** 定长子集协方差定理明确归于 Cesari–Colomboni；按课题 README，其所用下界及伪逆界的[完整仓库证明](R294-appendix-complete-proof-of-the-normalized-covariance-input.md)现已补齐。本文始终保留同一个物理 $K_1$；没有从三个单高度夹逼推出原 $\Gamma$ 的非交换相邻序。一般出生、原 graph 返回源及 ISP 完成标准均未由本文关闭。

## 1. 外部输入与准确对象

所用文献是 Tommaso Cesari and Roberto Colomboni, *Sharp Normalized Covariance Bounds and Constant-Stretch Correlated Sampling on the Hypersimplex*, arXiv:2607.13990v2，2026-09-08。

- [arXiv 版本记录](https://arxiv.org/abs/2607.13990v2)；
- [arXiv HTML 全文](https://arxiv.org/html/2607.13990v2)；
- [PDF](https://arxiv.org/pdf/2607.13990v2)。

其 Theorem 1.1 对任意 $M\ge2$、正权 $z_i$ 及 $1\le k\le M-1$ 的定长分布
$$
\mathbb P_k(I)=\frac{z_I}{e_k(z)},\qquad |I|=k,
$$
给出
$$
\Sigma_k\succeq Q_k:=D_k-\frac{v_kv_k^*}{V_k},
\quad D_k=\operatorname{diag}(v_k),\quad
(v_k)_i=\operatorname{Var}(1_{i\in I}),\quad V_k=\sum_i(v_k)_i.
\tag{1.1}
$$
该新来源的专用代数已全部在上述附录展开：Schur删位和的系数公式、双区Pieri计数、反演正性、删位矩阵负超平面和真实协方差回代均不再以外文定理编号代证。

Corollary 1.2 相应给出 $y\perp\mathbf1$ 时的伪逆二次型上界 $y^*\Sigma_k^\dagger y\le\sum_i|y_i|^2/(v_k)_i$。这里使用 v2 的系数一，不使用 v1 的系数二，也不将其外推为不同 $k$ 之间的定理。

本课题的对应关系已由 [R239 §7](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)建立。取
$$
d=\sum_{i=1}^M b_iE_i,\quad b_i>0,\quad z_i=b_i^2,
\quad B=\operatorname{diag}(b_i),\quad K=b^\perp,\quad P=P_K.
$$
对所有合法 $0\le n\le M-2$，定义
$$
F_n=\frac{d^n(d^*)^n}{(n!)^2}\bigg|_{\mathcal H_1},
\qquad \Gamma_n=P F_n^{-1}|_K.
\tag{1.2}
$$
完整 $F_n$ 严格正定；始终先求完整逆，再压缩到 $K$。令 $k=n+1$，则其真实精度的零延拓为
$$
\widetilde C_n=e_k B^{-1}\Sigma_kB^{-1},
\qquad \widetilde C_n|_K=\Gamma_n^{-1},\quad
\ker\widetilde C_n=\mathbb Cb.
\tag{1.3}
$$
(1.3) 是旧完整 Schur 身份，本稿不将其重新登记。

## 2. 不混淆伪逆同余的真实 Gram 夹逼

协方差 $\Sigma_k$ 的非对角项负、行和零，故它是一个正边图 Laplacian，度数恰为 $(v_k)_i$。对任意 $x$ 和任意常数 $c$，
$$
x^*\Sigma_kx
=\sum_{i<j}c_{ij}|x_i-x_j|^2
\le2\sum_i(v_k)_i|x_i-c|^2.
$$
对 $c$ 取最小值得到 $\Sigma_k\preceq2Q_k$。结合文献 (1.1)，
$$
Q_k\preceq\Sigma_k\preceq2Q_k.
\tag{2.1}
$$
两矩阵核都为 $\mathbb C\mathbf1$，在该核的正交补上可反转。若 $y\perp\mathbf1$，则 $Q_kD_k^{-1}y=y$，所以
$$
y^*Q_k^\dagger y=\sum_i\frac{|y_i|^2}{(v_k)_i}.
$$
从而
$$
\frac12\sum_i\frac{|y_i|^2}{(v_k)_i}
\le y^*\Sigma_k^\dagger y
\le\sum_i\frac{|y_i|^2}{(v_k)_i}.
\tag{2.2}
$$

现在取 $f\in K$。$Bf\perp\mathbf1$，而 (1.3) 的真实逆满足
$$
\boxed{\langle\Gamma_nf,f\rangle
=\frac1{e_{n+1}}(Bf)^*\Sigma_{n+1}^\dagger(Bf).}
\tag{2.3}
$$
这不是对奇异矩阵伪逆作任意同余。确切地，
$e_{n+1}^{-1}PB\Sigma_{n+1}^\dagger Bf$ 属于 $K$；用 (1.3) 乘回它，投影删除的部分只是 $b$ 的倍数，而 $Bf\perp\mathbf1$，结果准确是 $f$。故 (2.3) 的确是原 $\Gamma_n$。

记 $e_r^i=e_r((z_j)_{j\ne i})$。包含／不包含 $i$ 的概率分别为
$$
\pi_{k,i}=\frac{z_i e_{k-1}^i}{e_k},\qquad
1-\pi_{k,i}=\frac{e_k^i}{e_k}.
$$
因此定义
$$
\boxed{g_{n,i}:=\frac{z_i}{e_{n+1}(v_{n+1})_i}
=\frac{e_{n+1}}{e_n^i e_{n+1}^i},\qquad
A_n=P\operatorname{diag}(g_{n,i})|_K.}
\tag{2.4}
$$
所有分母在合法高度严格正。将 (2.2) 代入 (2.3)，得到主结论
$$
\boxed{\frac12 A_n\preceq\Gamma_n\preceq A_n
\qquad(0\le n\le M-2).}
\tag{2.5}
$$
两个常数与位数、正权比和高度无关。全部 $A_n$ 均由同一个物理坐标系中的对角算子压到同一个 $K$，但不同 $A_n$ 不因此自动交换。$n=0$ 时 $g_{0,i}=e_1/(e_1-z_i)$；$\Gamma_0=I_K$ 并未被误写成 $A_0$。

## 3. 每个对角系数全高度 log 凸

固定 $i$，令 $E_j=e_j^i$、$t=z_i>0$。对合法内部高度 $1\le n\le M-3$，设
$$
a=\frac{E_n}{E_{n-1}},\qquad
b=\frac{E_{n+1}}{E_n},\qquad
c=\frac{E_{n+2}}{E_{n+1}}.
$$
删一位后的标量 Newton 不等式给 $a>b>c>0$。由于 $e_j=E_j+tE_{j-1}$，完全消去公共项后有
$$
\boxed{
\frac{g_{n,i}^2}{g_{n-1,i}g_{n+1,i}}
=\frac{c(b+t)^2}{b(a+t)(c+t)}<1.}
\tag{3.1}
$$
这里严格号由准确差式
$$
b(a+t)(c+t)-c(b+t)^2
=bc(a-b)+b(a-c)t+(b-c)t^2>0
\tag{3.2}
$$
直接支付。不需要假定删位后的任意矩阵彼此交换。

逐坐标的二乘二矩阵
$$
\begin{pmatrix}g_{n-1,i}&g_{n,i}\\g_{n,i}&g_{n+1,i}\end{pmatrix}
$$
因而严格正定。把其直和在两个分量上同时压到同一个 $K$，得到一个真正共同正块
$$
\boxed{\begin{pmatrix}A_{n-1}&A_n\\A_n&A_{n+1}\end{pmatrix}>0.}
\tag{3.3}
$$
对 $A_{n+1}>0$ 作 Schur 补，得全部代理高度的准确相邻序
$$
\boxed{A_nA_{n+1}^{-1}A_n\prec A_{n-1}.}
\tag{3.4}
$$
本证明是先保留共同二乘二块再压缩，未将原 $\Gamma$ 的非交换乘积标量化。

## 4. 已付的混合正块与逐向量比较

由 (2.5)，两个实际端点均满足 $\Gamma_{n\pm1}\succeq A_{n\pm1}/2$。因此
$$
\boxed{\begin{pmatrix}
\Gamma_{n-1}&A_n/2\\A_n/2&\Gamma_{n+1}
\end{pmatrix}\succeq0,}
\tag{4.1}
$$
并且
$$
\boxed{A_n\Gamma_{n+1}^{-1}A_n\preceq4\Gamma_{n-1}.}
\tag{4.2}
$$
这是保留实际两个端点的共同正块；中间项是明确的 $A_n$，不是 $\Gamma_n$。

另对每个固定 $f\in K$，(3.1) 与 Cauchy–Schwarz 给
$$
\langle A_nf,f\rangle^2
\le\langle A_{n-1}f,f\rangle\langle A_{n+1}f,f\rangle.
$$
故实际 Gram 有逐向量标量界
$$
\boxed{\langle\Gamma_nf,f\rangle^2
\le4\langle\Gamma_{n-1}f,f\rangle
\langle\Gamma_{n+1}f,f\rangle.}
\tag{4.3}
$$
(4.3) 也不是目标算子序，因为它不含 $\Gamma_{n+1}^{-1}$ 的实际跨方向作用。

## 5. 无限正 $\ell^2$ 行的固定高度延拓

同一结论适用于可数无限正 $b\in\ell^2$，此时任意固定有限高度均合法。下面支付极限，不把无限 $B^{-1}$ 当成有界算子。

令 $S=\sum_i b_i^2<\infty$。固定孔层有
$\|d:\mathcal H_{p+1}\to\mathcal H_p\|\le\sqrt{(p+1)S}$，所以 $F_n$ 有界。实际条目为
$$
(F_n)_{ii}=e_n^i,\qquad (F_n)_{ij}=b_ib_j e_{n-1}^{ij}\ (i\ne j).
$$
对角差趋零，非对角平方和至多 $S^2e_{n-1}^2$，故 $F_n=e_nI+\text{紧算子}$。若 $F_nf=0$，则全部 $(n+1)$ 元子集上的 $\sum_{i\in I}f_i/b_i$ 为零；交换两个指标后迫全部比值相同，再代回子集和得零。因此 $F_n$ 是无核的正 Fredholm 算子，有有界逆。这也是 [R271 原连续尾全高度稿 §2](R271-appendix-original-birth-one-all-height-polynomial-first-return-anchor.md) 中不依赖具体尾速率的同一论证。

对截断 $b^{(N)}=(b_1,\ldots,b_N,0,\ldots)$，将对应完整一孔 $F_n^{(N)}$ 视为首 $N$ 位物理矩阵与 $e_n(z_1,\ldots,z_N)I$ 的直和。固定层上的 $d^{(N)}\to d$ 为算子范数收敛，故 $F_n^{(N)}\to F_n$；又 $P_N\to P$，于是完整逆及相应零延拓 Gram 也为算子范数收敛。

相应对角系数在 $i\le N$ 使用首 $N$ 位的 (2.4)，在 $i>N$ 取 $1/e_n(z_1,\ldots,z_N)$。首部删位对称和的截断误差由尾质量统一控制；而 $e_r^i\to e_r$ 随 $i\to\infty$，且 $\inf_i e_r^i>0$ 对每个固定 $r$ 成立。因此这些对角算子在算子范数中收敛到 (2.4) 的无限对角算子。该算子有界且有正下界。

有限头上的 (2.5) 与尾直和上的平凡夹逼，遂在共同空间的范数极限中给出无限行的 (2.5)。对任意固定相邻三高度，(3.1) 可由有限对称和极限得到，或直接使用无限行上的标量 Newton；共同块 (3.3) 与相邻序 (3.4) 的非严格形式，以及 (4.1)–(4.3)，因而仍成立。这里所有极限只在固定有限高度取，不宣称同时对增长高度有额外收敛速率。

## 6. 为何这尚未支付原非交换相邻序

待证原式仍是
$$
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\preceq C\Gamma_{n-1}.
$$
从 (2.5) 不能把 (4.2) 中的 $A_n$ 直接换成较小的 $\Gamma_n$，因为 $X\mapsto X\Gamma_{n+1}^{-1}X$ 对一般非交换正矩阵不保序。

这一逻辑缺口有一个准确的抽象例子。取 $t>0$，
$$
A_-=\operatorname{diag}(t^2,1),\quad A_0=I,\quad
A_+=\operatorname{diag}(t^{-2},1),
$$
$$
G_-=A_-,\qquad G_+=A_+,\qquad
G_0=\begin{pmatrix}3/4&1/4\\1/4&3/4\end{pmatrix}.
$$
则 $A_0A_+^{-1}A_0=A_-$，并且对三层同时有 $A_j/2\preceq G_j\preceq A_j$；然而
$$
\langle G_0G_+^{-1}G_0e_2,e_2\rangle
=\frac{t^2+9}{16},\qquad
\langle G_-e_2,e_2\rangle=1.
$$
所需统一常数随 $t\to\infty$ 无界。这个例子只排除“逐项两倍夹逼自动推出算子相邻序”的推理；它不是实际 Boolean 模型，不是原矩阵猜想的反例。

后续需要利用真实 $\Gamma_n$ 与这些特殊 $A_n$ 的共同物理结构来控制中间方向的变化。本文已经给出统一两倍夹逼、共同代理 Newton 块和实际端点的混合正块；没有将尚缺的中间传输费用隐藏在常数中。


## 7. 同一物理源也不使代理的相邻广义谱比一致有界

下面只是进一步定位尚缺的真实混合项费用，不能当作 $\Gamma$ 反例。取实际四位权
$$
b=(r,r,1,1),\qquad t=r^2\ge1,
\qquad e_2=t^2+4t+1,\quad e_3=2t(t+1).
$$
同一个 $K=b^\perp$ 含两条单位方向
$$
u_S=(e_1-e_2)/\sqrt2,\qquad u_W=(e_3-e_4)/\sqrt2.
$$
它们分别处于强组、弱组的标准差分支，并为 $A_1,A_2$ 的共同特征向量。由 (2.4)，
$$
a_{1,S}=\frac{e_2}{(t+2)(2t+1)},\qquad
 a_{2,S}=\frac{2(t+1)}{2t+1},
$$
$$
a_{1,W}=\frac{e_2}{t(t+2)(2t+1)},\qquad
 a_{2,W}=\frac{2(t+1)}{t^2(t+2)}.
$$
故 $A_1A_2^{-1}$ 在这两个共同方向上的特征值之比准确为
$$
\boxed{\frac{a_{1,W}/a_{2,W}}{a_{1,S}/a_{2,S}}
=\frac{t(t+2)}{2t+1}\longrightarrow\infty.}
$$
因而不能用特殊 $A_n$ 相邻广义度量的统一条件数去补第 6 节缺口，即便所有源都保在同一实际 $b^\perp$。在这个对称例子中，真实 $\Gamma_n$ 也保上述不同群表示，不在两方向间旋转，所以该例没有否定原相邻序。一般权下必须支付的仍是真实 $\Gamma_n$ 的混合项与原度量运输。
