# R267 附录：同一实际平坦分母的相容有界有理次根

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整正向构造。** 对每个原 Haar 尾 $C=A^{(m_0)}$，本文构造同一族实际有界算子
$$
P_r\in C',\qquad r\in\mathbb Q_{>0},
\qquad P_rP_s=P_{r+s}.
\tag{1}
$$
每个 $P_r$ 都属于实际共同幂理想
$\mathfrak F_C=\bigcap_{a\ge1}C^aC'$，并在全部有限放大的原闭不变旗子商上单射、像稠密。$P_1$ 保持函数正锥；它的全部有理次根由同一构造相容实现。每个固定 $r$ 各自有界，不声称 $r\downarrow0$ 时范数一致有界或强连续。

本文不把 (1) 中的 $P_1$ 识别为原 $C$，没有得到 $V^2=CP_1^2$。

## 1. 真实收缩因子的选择

记 $\mathcal A=\overline{\mathbb C[I,C]}^{\|\cdot\|}$，$c=\|C\|>0$，并枚举单位 Walsh 基 $(h_\ell)_{\ell\ge0}$，其中 $h_0=\Omega$。原 $C$ 单射、像稠密且拟幂零。

[正共同分母](R267-appendix-positivity-preserving-common-powers-and-no-compact-domination.md) §1 的有限位块给保持函数正锥的实际多项式收缩
$$
F_{m,q}=\frac2{q+2}\sum_{j=m}^{m+q-1}N_j,\qquad
N_j=C^{2^j}/\|C^{2^j}\|,
\tag{2}
$$
其最低次数为 $2^m$。这里保留全部原 carry：
$N_j=E_j+\eta_jE_j^*N_{j+1}$，
$\sum_{j\ge m}\eta_j\le2e^{-770\,16^m}$。

对纯局部块 $F^0_{m,q}=2\sum E_j/(q+2)$，
$$
\|F_{m,q}\|\le
\frac{q+1+4e^{-770\,16^m}}{q+2}<1.
\tag{3}
$$
若单位柱向量 $h$ 只依赖第 $m$ 位以前的坐标，则
$$
\|(F^0_{m,q}-I)h\|
=\|(F^{0*}_{m,q}-I)h\|
=\frac{\sqrt{q+4}}{q+2},
\qquad
\|F_{m,q}-F^0_{m,q}\|
\le\frac{4e^{-770\,16^m}}{q+2}.
\tag{4}
$$
因此取 $m\ge1$ 足够后移、$q$ 足够大，就能在任意给定有限组 Walsh 测试上同时使 $F_{m,q}$ 及其伴随接近 $I$。这一步用的是真实多项式收缩，不把它替换成局部 $E_j$。

置
$$
M_n=(n+1)!,\qquad d_n=M_{n+1}-M_n>0,\qquad
\epsilon_n=\frac{2^{-n-6}}{1+d_n}\quad(n\ge0).
\tag{5}
$$
所以 $M_0=1$、$M_n\mid M_{n+1}$，任意正整数最终整除 $M_n$，且
$\sum_n d_n\epsilon_n<1/32$。

对每个 $n$，用 (4) 选 $F_n$，使前 $n+1$ 个测试上的两个误差之和不超过 $\epsilon_n/2$。再取
$0<\delta_n\le\epsilon_n/8$，定义
$$
Z_n=(1-\delta_n)F_n+\delta_n C/c=C\,U_n(C).
\tag{6}
$$
则 $Z_n$ 是正锥保持的多项式收缩，并且
$$
\|(Z_n-I)h_\ell\|+
\|(Z_n^*-I)h_\ell\|\le\epsilon_n
\qquad(\ell\le n).
\tag{7}
$$
因为 $F_n$ 最低次数至少为二，
$$
U_n(0)=\delta_n/c>0.
\tag{8}
$$
所以 $U_n(C)\in\mathcal A$ 是可逆元。为每个 $n$ 固定在零点取实值 $\log U_n(0)$ 的解析对数芽 $L_n(z)$；对任意实数 $t$，以后统一使用
$$
U_n(C)^t=\exp(tL_n(C)).
\tag{9}
$$
只需零点附近的解析芽。$C$ 拟幂零保证这些有界算子及其逆属于 $\mathcal A$，且同一个 $n$ 的全部指数严格相加。不要求 $U_n$ 在整个复平面没有零点。

## 2. 全部实际整数尾乘积

固定 $r=p/q>0$，$p,q$ 为正整数。选 $N$ 使 $q\mid M_N$。则对 $n\ge N$，$r d_n$ 是非负整数，故
$$
T_{r,N,K}=\prod_{n=N}^{K-1}Z_n^{\,r d_n}\qquad(K>N)
\tag{10}
$$
都是收缩。

对收缩 $Z$ 及正整数 $b$，
$\|(Z^b-I)x\|\le b\|(Z-I)x\|$，伴随同样成立。
所有 $Z_n$ 互相交换，伴随也互相交换。有限乘积望远镜、(7) 及
$\sum d_n\epsilon_n<\infty$ 因而给 (10) 在每个基向量上的强及强伴随 Cauchy 性。有限个早期项不影响这个结论。统一收缩界延拓到全 $H$，得到
$$
T_{r,N}=\operatorname*{SOT^*\!-\!lim}_{K\to\infty}T_{r,N,K},
\qquad \|T_{r,N}\|\le1.
\tag{11}
$$
它仍属于 $C'$，保持函数正锥和所有原闭不变旗。只要
$N\ge\ell$ 且 $q\mid M_N$，
$$
\|(T_{r,N}-I)h_\ell\|+
\|(T_{r,N}^*-I)h_\ell\|
\le r\sum_{n\ge N}d_n\epsilon_n.
\tag{12}
$$
于是对每个固定 $r$，
$$
T_{r,N}\longrightarrow I\quad\text{强*}\qquad(N\to\infty).
\tag{13}
$$
以上是整组柱测试及全空间上的实际尾积，不仅是真空列乘积。

## 3. 同一有理次根族及精确乘法

对 $r=p/q>0$ 和任一 $q\mid M_N$，定义
$$
A_{r,N}=C^{rM_N}\prod_{n<N}U_n(C)^{r d_n},
\qquad
P_r=A_{r,N}T_{r,N}.
\tag{14}
$$
$rM_N$ 是正整数；前面的全部分数次幂只作用于已付的可逆 $U_n(C)$。所以每个 $P_r$ 实际有界，并有
$\|P_r\|\le\|A_{r,N}\|<\infty$。

由 $M_{N+1}=M_N+d_N$、同一对数支及 (6)，
$$
A_{r,N+1}=A_{r,N}Z_N^{r d_N},\qquad
T_{r,N}=Z_N^{r d_N}T_{r,N+1}.
\tag{15}
$$
故 (14) 不依赖可用切口 $N$，也不依赖 $p/q$ 的表示。

给定 $r,s\in\mathbb Q_{>0}$，选一个共同切口使两分母都整除 $M_N$。有限前缀满足
$A_{r,N}A_{s,N}=A_{r+s,N}$；尾部在每个有限 $K$ 上满足同一关系，统一收缩界允许乘积通过强极限。因此
$$
\boxed{P_rP_s=P_{r+s}.}
\tag{16}
$$
特别
$$
P_{1/q}^{\,q}=P_1,\qquad
P_{1/(ab)}^{\,a}=P_{1/b}\quad(a,b\ge1).
\tag{17}
$$
可置 $P_0=I$，但本文没有证明这个有理参数半群在零点连续。

当 $r=1,N=0$ 时 $A_{1,0}=C$，所以
$$
P_1=C\,\operatorname*{SOT^*\!-\!lim}_{K\to\infty}
\prod_{n=0}^{K-1}Z_n^{d_n},\qquad \|P_1\|\le c.
\tag{18}
$$
因此 $P_1$ 保持函数正锥。非整数 $r$ 的有限解析单位因子不必保持正锥；本文不对这些 $P_r$ 作该断言。

## 4. 全部实际原幂逆及全旗强单位

固定 $r>0$ 有理数和整数 $a\ge0$，取足够大且可用的 $N$，使 $rM_N\ge a$。则
$$
R_{r,a}=
C^{rM_N-a}\left(\prod_{n<N}U_n(C)^{r d_n}\right)T_{r,N}
\in C'
\tag{19}
$$
是实际有界算子，且 $C^aR_{r,a}=P_r$。原 $C$ 单射使它与切口无关。继续增大切口又证明
$$
P_r,\ R_{r,a}\in\mathfrak F_C.
\tag{20}
$$

还须支付非零及全部原旗上的真实范围，不能由 (20) 单独推导。

用 [原共同倍数稿](R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md) §1、§5 的 R23 多项式强*单位
$E_\ell=e_\ell(C)$，其范数不超过一、最低次数趋于无穷。对每个可用 $N$ 选 $\ell(N)\ge N$，使最低次数至少为 $rM_N$，并写
$$
E_{\ell(N)}=C^{rM_N}B_{r,N}(C),\qquad
V_{r,N}=\prod_{n<N}U_n(C)^{r d_n}.
$$
定义实际有界因子
$$
W_{r,N}=V_{r,N}^{-1}B_{r,N}(C)\in\mathcal A.
$$
同一个 $P_r$ 满足
$$
\boxed{
P_rW_{r,N}=T_{r,N}E_{\ell(N)},\qquad
\|P_rW_{r,N}\|\le1,\qquad
P_rW_{r,N}\longrightarrow I\quad\text{强*}.
}
\tag{21}
$$
(13) 与 $E_{\ell(N)}\to I$ 直接付最后极限。

$P_r,W_{r,N}$ 及所有 $R_{r,a}$ 保持每个原 $C$ 不变闭子空间；它们由范数多项式极限和一致有界强极限构成。同样适用于任意固定有限放大。故 (21) 下到任意原闭不变旗 $K_-\subset K_+$ 的实际子商，仍为收缩强单位。

若诱导 $P_{r,Q}x=0$，则交换性给
$P_{r,Q}W_{r,N,Q}x=0$，由 (21) 得 $x=0$；同一单位的像在 $\operatorname{Ran}P_{r,Q}$ 内，故该像稠密。因此每个 $P_r$ 在每个非零原旗子商上都是非零 quasiaffinity。在全空间上它们尤其非零。对 $R_{r,a}$ 使用因子 $C^aW_{r,N}$，得到相同结论。

每个 $P_r$ 拟幂零，且不属于原物理 UHF 代数：由 (20) 及原共同倍数稿 §5、§7，$\mathfrak F_C\cap\mathfrak U=\{0\}$。完整兼容喷射亦全为零。

若 $T$ 是实际闭算子且其域被 $C$ 保持、$TC=CT$ 于该域，则原有界强多项式逼近和闭性使 $P_r,W_{r,N}$ 保持这个同一域，并与 $T$ 交换。因此
$$
P_rW_{r,N}x\to x,\qquad
T P_rW_{r,N}x=P_rW_{r,N}Tx\to Tx
\quad(x\in\operatorname{Dom}T).
\tag{22}
$$
所以 $P_r\operatorname{Dom}T$ 是该闭域的图核心。这里依然不声称
$P_rH\subseteq\operatorname{Dom}T$。

## 5. 这是真实分数根，而非原普通解析芽

固定 $q\ge2$。$P_{1/q}$ 不等于任何零点附近解析芽 $f(P_1)$。否则
$$
\bigl(f(z)^q-z\bigr)(P_1)=0.
$$
非零解析芽 $g$ 可写成 $z^k u(z)$、$u(0)\ne0$；$u(P_1)$ 可逆而 $P_1$ 单射，所以 $g(P_1)\ne0$。因此只能有解析恒等式 $f(z)^q=z$，但其零点阶数要求 $q\,\operatorname{ord}_0 f=1$，不可能。

这只说明新根超出 $P_1$ 的普通解析芽演算。本文没有把新 $P_1$ 自动识别成此前有额外定量费用的某个指定分母，也没有将这个短论证扩大为此前全部多变量函数类的比较。

## 6. 原算子本身的实际有界平方近似

对每个 $N\ge0$，置
$$
r_N=\frac1{M_N},\qquad
V_N=\prod_{n<N}U_n(C)^{d_n/(2M_N)},\qquad
D_N=T_{r_N,N},
$$
$$
Y_N=P_{r_N/2}\,V_N^{-1}.
\tag{23}
$$
$V_N$ 是原 $\mathcal A$ 内的有界可逆元，$P_{r_N/2}$ 已由 (14) 在某个足够深的合法切口定义。这里不在第 $N$ 个切口写半整数的 $C^{1/2}$。

先用已经成立的同族乘法
$P_{r_N/2}^2=P_{r_N}$，然后仅对 $r_N$ 在合法第 $N$ 切口使用 (14)，得到
$$
P_{r_N}=C\,V_N^2D_N,\qquad
\boxed{Y_N^2=C D_N.}
\tag{24}
$$
每个 $Y_N$ 都是实际全域有界的平坦交换子，保全部原旗的单射和稠值。$D_N$ 是正锥保持的收缩。由 (19) 在 $a=1$ 的准确式
$C^{-1}P_{r_N}=V_N^2D_N$，$D_N$ 也属于 $\mathfrak F_C$，并在全部原旗上单射、像稠密。

这里参数 $r_N$ 随 $N$ 变化，不能只引用 (13) 的固定参数极限。应直接用 (12)：对每个固定 $\ell$ 和 $N\ge\ell$，
$$
\|(D_N-I)h_\ell\|+\|(D_N^*-I)h_\ell\|
\le\frac1{M_N}\sum_{n\ge N}d_n\epsilon_n\longrightarrow0.
\tag{25}
$$
统一收缩界于是给
$$
\boxed{
D_N\longrightarrow I\ \text{强*},\qquad
Y_N^2\longrightarrow C\ \text{强*},\qquad
\|Y_N^2\|\le c.
}
\tag{26}
$$
所有关系也下降到同一个原有限放大旗子商。构造始终使用完整原 $C$；没有改成有限头算子或 $C+\varepsilon I$。

还可以准确保留任意固定同族分母 $P_t$（$t>0$ 有理）：
$$
Y_NP_t=P_{t+r_N/2}V_N^{-1},\qquad
(Y_NP_t)^2=C D_NP_{2t}\longrightarrow CP_t^2\ \text{强*}.
\tag{27}
$$
这是同一 $P_t$ 的实际来源式，未替换分子或尾余量。本文只付每个 $Y_N$ 和 $Y_NP_t$ 各自有界；没有付 $N$ 一致范数、强收敛子列或图收敛。弱收敛不能直接通过平方。若要从 (27) 得到原所需有界分子，仍必须支付这种真实来源控制。

## 7. 原平方目标仍需同源奇阶输入

本构造的有限前缀最低 $C$ 次数准确为 $M_N$，因而可在同一个足够深切口同时整除任意有限组根次数。这是 (14) 的来源。

但 $CP_1^2$ 的相应有限前缀最低次数为
$$
2M_N+1,
$$
永远是奇数。它不能通过 (14) 的整数 $C$ 次数取平方根。已构造的
$P_{1/2}^2=P_1$ 不等于一个满足 $V^2=CP_1^2$ 的分子，也未付任何全域 $C^{1/2}$。

后继可以使用 (16)、(19)、(21) 的真实同源有理根和整数逆，但仍须另行解决这个额外奇阶方程或另一个真正原不变旗来源。普通 Hilbert 不变子空间问题未完成。
