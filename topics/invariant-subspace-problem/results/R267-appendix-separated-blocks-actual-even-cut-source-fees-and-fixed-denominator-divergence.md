# R267 附录：分离块选择的实际偶切口来源费用与全部固定分母发散

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：下列存在性及费用下界已证明。** 在[相容有理根](R267-appendix-coherent-bounded-rational-roots-of-one-flat-common-denominator.md)允许的真实多项式块选择中，存在同一个合法选择，使其每个固定正有理数 $t$ 满足
$$
\|Y_NP_t\|\longrightarrow\infty
\quad(N\to\infty,\ N\ {\rm even}),
\qquad
\|Q_N\|\longrightarrow\infty
\quad(N\to\infty).
\tag{1}
$$
这里始终使用[固定分子稿](R267-appendix-fixed-numerator-actual-denominators-and-odd-cut-contractions.md)的同一个实际 $P_t,Y_N,Q_N$。于是这个选择没有强收敛的 $Q_N$ 子列。

本结论只排除下文明确构造的分离块选择；不声称全部合法选择都有此行为，也不排除其他平坦分母下的原二次分子。有限阶喷射只用于取得有限解析前缀的算子范数；将其传到全平坦来源依靠第 4 节的真实张量尾估计。

## 1. 原幂、原系数及记号

令 $C=A^{(m_0)}$ 为一个固定原 Haar 尾，$c=\|C\|$，并记
$$
a_j=\alpha_{m_0+j},\qquad
\beta_n=\|C^n\|=\prod_{h=1}^n a_{v_2(h)},\qquad
\beta_0=1.
\tag{2}
$$
使用[完整兼容喷射](R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md)的真实系数界：
$$
|[z^n]f(z)|\,\beta_n\le\|f(C)\|
\tag{3}
$$
对每个零点附近解析芽 $f$ 成立。这里的 $f(C)$ 由原拟幂零算子演算定义。本文没有把全平坦尾的系数取作非零。

由原权计数，若 $J\ge\ell+1$，
$$
\beta_{2^J-1}
=
\frac{\left(\prod_{j=\ell+1}^{J-1}\beta_{2^j}\right)
\beta_{2^\ell}^{\,2}}{a_\ell}.
\tag{4}
$$
可从 $\beta_{2^{j+1}-1}=\beta_{2^j}^{\,2}/a_j$ 逐次展开得到；这也是[实际 dyadic 平方可除稿](R12-appendix-explicit-dyadic-square-divisibility-and-new-closed-stable-commuting-domain.md)所用的原权身份。

保留相容有理根稿的
$$
M_n=(n+1)!,\qquad d_n=M_{n+1}-M_n,\qquad
\epsilon_n=\frac{2^{-n-6}}{1+d_n}.
\tag{5}
$$
为避免与切口参数混淆，本文将原混合系数记作 $\zeta_n$，即
$$
F_n=F_{m_n,q_n},\qquad
Z_n=(1-\zeta_n)F_n+\zeta_n C/c=C\,U_n(C).
\tag{6}
$$
取 $\zeta_n=\epsilon_n/8$。每个 $F_n$ 都是原多项式收缩，按前稿使前 $n+1$ 个 Walsh 基向量上的正、伴随误差之和不超过 $\epsilon_n/2$。因此 (6) 的全部原强*尾积、相容乘法及所有原旗上的单射稠像结论继续适用。

## 2. 一个真实有限前缀的下界

固定偶整数 $a\ge0$、整数 $p\ge0$、$m\ge1$ 及 $0<\zeta<1$。先固定这些参数，再让整数 $q$ 增大。置
$$
F=\frac2{q+2}\sum_{j=m}^{m+q-1}\frac{C^{2^j}}{\beta_{2^j}},
\qquad
U(z)=\frac{\zeta}{c}
+\frac{2(1-\zeta)}{q+2}
\sum_{j=m}^{m+q-1}\frac{z^{2^j-1}}{\beta_{2^j}},
\qquad
X=C^{a+p+1}U(C)^{p+1/2}.
\tag{7}
$$
分数幂使用在零点取正实值的同一解析支；只对 $U(0)=\zeta/c>0$ 的可逆解析单位取分数幂，没有取 $C^{1/2}$。

令
$$
k=a+p+2,\qquad J=m+q,\qquad \ell=J-k+1.
$$
当 $q\ge k-1$ 时，$\ell\ge m$。有显式下界
$$
\begin{split}
\|X\|\ \ge\ &
\left|\binom{p+1/2}{k}\right|\frac{k!}{2}
\left(\frac{\zeta}{c}\right)^{-a-3/2}
\left(\frac{2(1-\zeta)}{q+2}\right)^k
\frac1{a_\ell}
-B(a,p,\zeta,c),\\
B(a,p,\zeta,c)=\ &
c^{a+1/2}
\sum_{r=0}^{a+p+1}
\left|\binom{p+1/2}{r}\right|
\zeta^{p+1/2-r}(1-\zeta)^r.
\end{split}
\tag{8}
$$

**证明。** 写 $U=u_0+v$，其中 $u_0=\zeta/c$，$v$ 的全部非零次数都是奇数且系数为正。考察
$z^{a+p+1}U(z)^{p+1/2}$ 的第 $2^J-1$ 个系数。
二项式指标 $r$ 若有贡献，就必须满足 $r\equiv p\pmod2$，因为 $a$ 为偶数。对 $r\ge k\ge p+2$，
$$
\operatorname{sgn}\binom{p+1/2}{r}
=(-1)^{r-p-1}=-1.
$$
所以全部这些贡献同为负数，不发生相互抵消。

在 $r=k$ 项中，取 $k$ 个叶次数
$$
2^{J-1},2^{J-2},\ldots,2^{\ell+1},2^\ell,2^\ell.
$$
它们的和为 $2^J$；把每个次数减一，再乘 $z^{a+p+1}=z^{k-1}$，总次数恰为 $2^J-1$。重数为 $k!/2$。乘以原 $\beta_{2^J-1}$ 后，(4) 正好给 $1/a_\ell$，从而得到 (8) 的主项。

二项式前 $a+p+2$ 项，即 $0\le r\le a+p+1$，作为算子的每一项都可写成
$$
\binom{p+1/2}{r}
(\zeta/c)^{p+1/2-r}(1-\zeta)^r
C^{a+p+1-r}F^r.
$$
这里只用非负整数 $C$ 幂。由 $\|F\|\le1$，其范数总和不超过 $B$。再用 (3) 控制这个有限部分的同一加权系数，便得 (8)。解析二项式级数在算子范数下收敛，因为 $v(C)$ 拟幂零；固定的 Taylor 系数中也只有有限个指标有贡献。证毕。

由于
$$
-\log a_\ell=
\frac{280}{3}16^{m_0+\ell}
-90\,8^{m_0+\ell}
+300\,2^{m_0+\ell}-\frac{850}{3},
$$
(8) 对固定 $a,p,m,\zeta$ 在 $q\to\infty$ 时趋于无穷。所有费用均属于原 $C$。

## 3. 在同一个构造中选取偶切口

记
$$
\tau_N=\frac1{2M_N},\qquad
V_N=\prod_{\nu<N}U_\nu(C)^{d_\nu/(2M_N)},\qquad
Y_N=P_{\tau_N}V_N^{-1}.
$$
令 $N\ge2$ 为偶数，并先取整数 $1\le t\le N$。第 $N+1$ 个切口对 $r=t+\tau_N$ 合法，因为
$rM_{N+1}=tM_{N+1}+(N+2)/2$ 是整数。完整原公式给
$$
Y_NP_t=A_{N,t}\,T_{t+\tau_N,N+1},
\tag{9}
$$
其中
$$
\begin{gathered}
A_{N,t}=B_{N,t}\,C^{a+p+1}U_N(C)^{p+1/2},\\
B_{N,t}=\prod_{\nu<N}U_\nu(C)^{t d_\nu},\qquad
a=tM_N,\qquad p=t d_N+N/2.
\end{gathered}
\tag{10}
$$
$a$ 为偶数，$p$ 为非负整数；$B_{N,t}$ 是此前已经固定的有界可逆解析单位。特别它不依赖尚待选择的 $q_N$。

递归作以下**一次固定选择**。在每一步 $n$，先选 $m_n$ 大于此前指定的全部有限前缀长度，并覆盖前 $n+1$ 个 Walsh 测试。固定 $\zeta_n=\epsilon_n/8$，然后选择 $q_n$ 足够大，使前稿要求的两种误差成立。

若 $n=N\ge2$ 为偶数，同时用 (8) 及
$$
\|B_{N,t}X\|\ge\|X\|/\|B_{N,t}^{-1}\|
$$
保证有限组 $t=1,\ldots,N$ 满足
$$
\|A_{N,t}\|\ge16N.
\tag{11}
$$
每个 $A_{N,t}$ 属于 $\mathcal A=\overline{\mathbb C[I,C]}$，因而属于原物理 UHF 代数。这里直接使用 [R9](R9-radial-odometer-and-nilpotent-approximants.md) §3、(3.3) 证明中的有限头截断 $C_L$ 及 $\|C-C_L\|=a_L\to0$；[R174](R174-last-column-boundary-state-and-negative-integer-shift.md) §1 也明确记录了这个 UHF 包含。原尾只需重编号。选共同有限前缀长度 $L_N$ 以及该前缀上的矩阵 $A^0_{N,t}$，使
$$
\|\widehat A_{N,t}-A_{N,t}\|
\le\|A_{N,t}\|/16,\qquad
\widehat A_{N,t}=A^0_{N,t}\otimes I.
\tag{12}
$$
以后所有 $m_\nu$（$\nu>N$）都选得至少为 $L_N$。每一步只有有限多个已指定的 $L_N$，故这种递归可持续。它没有修改任何此前的块；同一完成后的全部 $P_r$ 由这一组块定义。

(11) 本身还不是 (1)，因为未来尾完全平坦。下面单独支付这一步。

## 4. 未来真实尾保留有限范数见证

仍固定上述偶数 $N$ 和 $1\le t\le N$，记 $r=t+\tau_N<N+1$。所有 $\nu\ge N+1$ 的 $rd_\nu$ 都是非负整数。定义**纯原多项式尾**
$$
\widetilde T_{r,N+1}
=\operatorname*{SOT^*\!-\!lim}_{K\to\infty}
\prod_{\nu=N+1}^{K-1}F_\nu^{\,rd_\nu}.
\tag{13}
$$
原 $F_\nu$ 的收缩界、同一 Walsh 正伴随误差和收敛的
$\sum d_\nu\epsilon_\nu$，按前稿相同望远镜证明这个极限存在。这里没有用局部 $E_j$ 替代 $C^{2^j}/\beta_{2^j}$。

直接使用 [R124](R124-dyadic-residue-factorization-and-order-one-kernels.md) §2、(2.2) 的原 dyadic 张量身份（亦见 [R253](R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md) §1、(1.1)–(1.2)）：$C^{2^j}$ 在前 $L_N$ 位上精确为恒等张量一个尾算子，只要 $j\ge L_N$。这些式子对原尾 $C$ 按局部位重编号同样成立。由于 $\nu>N$ 时 $m_\nu\ge L_N$，(13) 因而精确满足
$$
\widetilde T_{r,N+1}
=I_{<L_N}\otimes\widetilde T^{\rm tail}_{r,N+1}.
\tag{14}
$$
这就是自适应选择有限前缀之后再后移未来块的用途。

在同一真空 $\Omega$ 上，
$$
\|(\widetilde T_{r,N+1}-I)\Omega\|
\le\frac r2\sum_{\nu\ge N+1}d_\nu\epsilon_\nu
<(N+1)2^{-N-7}<\frac1{16}.
\tag{15}
$$
故 $\|\widetilde T^{\rm tail}_{r,N+1}\|>15/16$。

另一方面，两个混合来源在全算子范数上满足
$$
\|Z_\nu-F_\nu\|
=\zeta_\nu\|C/c-F_\nu\|\le2\zeta_\nu.
$$
先对每个有限整数幂和有限乘积望远镜，再通过强极限，得到
$$
\begin{split}
\|T_{r,N+1}-\widetilde T_{r,N+1}\|
&\le2r\sum_{\nu\ge N+1}d_\nu\zeta_\nu\\
&\le\frac r4\sum_{\nu\ge N+1}d_\nu\epsilon_\nu
<(N+1)2^{-N-8}<\frac1{16}.
\end{split}
\tag{16}
$$
这里用的是原尾在全 $H$ 上的差，足以作用于真实有限范数见证，不只是固定测试向量上的强误差。

由 (12)、(14)–(16) 及 $\|\widetilde T\|\le1$，
$$
\begin{split}
\|A_{N,t}T_{r,N+1}\|
&\ge
\|\widehat A_{N,t}\widetilde T_{r,N+1}\|
-\|A_{N,t}-\widehat A_{N,t}\|
-\|A_{N,t}\|\|T_{r,N+1}-\widetilde T_{r,N+1}\|\\
&>
\left(\frac{15^2}{16^2}-\frac1{16}-\frac1{16}\right)\|A_{N,t}\|\\
&>\frac12\|A_{N,t}\|
\ge8N.
\end{split}
\tag{17}
$$
其中第一项是精确张量范数
$\|A^0_{N,t}\|\|\widetilde T^{\rm tail}_{r,N+1}\|$。因此 (9) 的完整来源已付下界。整个步骤没有声称有限阶喷射通过平坦尾仍非零。

## 5. 所有固定正有理参数与全部切口分母

先固定正整数 $t$。对所有充分大的偶数 $N$，$t\le N$，故由 (17)
$\|Y_NP_t\|\ge8N$。

再固定任意正有理数 $t$，选一个整数 $k>t$。同族精确乘法给
$$
Y_NP_k=(Y_NP_t)P_{k-t}.
$$
$P_{k-t}$ 是固定、非零、有界的实际算子。因此沿充分大的偶数切口，
$$
\|Y_NP_t\|\ge\frac{8N}{\|P_{k-t}\|}\longrightarrow\infty.
\tag{18}
$$
这仍是同一个完成后的构造，未为不同参数重新选择块。

对 $\tau_N<t$ 的实际固定分母
$$
Q_N=P_{t-\tau_N}V_N
$$
使用已付全域等式 $Y_NP_t=CD_NQ_N$ 和 $\|D_N\|\le1$，得到
$$
\|Q_N\|\ge c^{-1}\|Y_NP_t\|.
\tag{19}
$$
于是偶数切口的分母范数趋于无穷。

若 $N$ 为充分大的奇数，则 $M_{N+1}/M_N=N+2$ 为奇数。固定分子稿的**实际奇数切口收缩**给
$$
Q_{N+1}=Q_NR_{N,N+1},\qquad
\|R_{N,N+1}\|\le1.
$$
因此 $\|Q_N\|\ge\|Q_{N+1}\|$，其右端是下一个偶数切口。故所有切口的
$\|Q_N\|\to\infty$。一致有界原理排除此列的任何强收敛子列。

## 6. 准确后继范围

这个合法选择仍具有此前全部正向结论：每个 $P_r,Y_N,Q_N,D_N$ 各自有界，保全部原旗的单射稠像，$Y_N^2=CD_N$，且 $D_N\to I$ 强*。本稿说明这些性质不会自动支付同一固定 $P_t$ 的来源费用。

结论依赖第 3 节明确安排的有限范数见证与未来块分离。本文没有对未作该分离的选择证明发散，也没有从局部 (8) 单独推出任意全平坦来源的下界。后继若继续这个相容族，需要新的耦合或费用输入；普通 Hilbert 不变子空间问题与任意平坦分母下的原二次分子均未解决。
