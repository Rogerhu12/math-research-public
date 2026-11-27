# 不整除原幂闭根不能具有实际第一阶 gauge 接口

日期：2026-11-27（台北时间，UTC+8）。作者：literature_deddens / Astra-ISP-8542378f-20261127。

状态：完整证明。§§1--5 先给平方根的四次显式消元，§6 以有限 resultant 完整处理全部 $q\nmid p$ 的原幂闭根，并允许任意非零 UHF 交换系数及任意有界交换余项。R171 排除慢第一阶行，兼容喷射排除有界行。无须假设根具有完整 $C$ 自伴性。实际第一阶接口仍须先对同一个根支付，不把 R143 未知底空间上的反根搬到全尾。

## 1. 同一原尾与全部实际输入

在原尾 Haar 空间 $H$ 上记
$$
B=B_m,\qquad \mathscr C=\{B_m\}'.
$$
令 $p\ge1$ 为奇数、$\lambda\ne0$，并设 $T$ 为稠密定义的闭算子，
$\mathcal D=\operatorname{Dom}T$，满足
$$
T\mathcal D\subseteq\mathcal D,\qquad
T^2x=\lambda B^p x\quad(x\in\mathcal D).
\tag{1.1}
$$
由奇幂强恢复，$B\mathcal D\subseteq\mathcal D$ 且 $TB=BT$ 于此域；
也可把这两项作为显式输入保留。
完整交换子的强多项式逼近及 $T$ 的闭性使每个 $F\in\mathscr C$ 保持 $\mathcal D$ 并与 $T$ 域交换。

取最低物理位字符 $U=U_{-1}$，于是
$$
UBU^*=-B,\qquad G=UTU^*,\qquad
\mathcal D_G=U\mathcal D.
$$
由于 $p$ 奇数，
$$
G\mathcal D_G\subseteq\mathcal D_G,\qquad
G^2x=-\lambda B^p x\quad(x\in\mathcal D_G).
\tag{1.2}
$$
$\mathscr C$ 也保持 $\mathcal D_G$ 并与 $G$ 域交换。

假定已经对这同一个 $T,G$ 取得
$$
R,Q\in\mathscr C,\qquad R\text{ 单射},
\tag{1.3}
$$
以及实际全域比较
$$
R\mathcal D\subseteq\mathcal D_G,\qquad
GRx=RTx+Qx\quad(x\in\mathcal D).
\tag{1.4}
$$
再假设该比较项来自一条实际第一阶行：
$$
Z=X_{a_*+\sum_{j\ge0}a_j\chi_j},\qquad a\in\ell^2,
\tag{1.5}
$$
其中 $Z$ 是 R125/R128 的原尾闭实现，并且
$$
RH\subseteq\operatorname{Dom}Z,\qquad
ZR\in\mathscr C\text{ 有界},\qquad
Q=F(B)ZR.
\tag{1.6}
$$
$F$ 是非零收敛解析芽。特别允许实际 R143 首行中的
$F(B)=4N_0(I-N_0^2)^{-1}$，它具有一阶零点。

**定理 1.1。** 全部 (1.1)--(1.6) 不可能同时成立。

本定理不要求 $T=CT^*C$，甚至不要求 $T\subseteq CT^*C$。
它使用根的域稳定和实际 (1.4)，不从共同稠密域的存在推断后者。

## 2. 两个相反平方身份的有界消元

简记 $D=\lambda B^p$，并定义有界交换子
$$
P=RQ,\qquad Y=-DR^2-\frac12Q^2.
\tag{2.1}
$$

固定 $x\in\mathcal D$。由于 $T\mathcal D\subseteq\mathcal D$，
以及 $R,Q$ 保持 $\mathcal D$，向量 $Rx,RTx,Qx$ 都在 $\mathcal D$。
(1.4) 逐一给
$$
R^2x,\quad R^2Tx,\quad RQx\in\mathcal D_G.
\tag{2.2}
$$
在这些实际域内，
$$
GR^2x=R^2Tx+RQx,
$$
$$
GR^2Tx=R^2T^2x+RQTx,\qquad
GRQx=RQTx+Q^2x.
$$
故再次作用 $G$ 合法，得到
$$
G^2R^2x=R^2T^2x+2RQTx+Q^2x.
$$
用 (1.1)--(1.2) 代入两边，得
$$
\boxed{PTx=Yx\qquad(x\in\mathcal D).}
\tag{2.3}
$$

这里不需要将 $PH$ 返回 $\mathcal D$。因为 $Tx\in\mathcal D$，
再次使用 (2.3) 后仅乘有界交换因子即可：
$$
P^2T^2x=PYTx=YPTx=Y^2x.
$$
所以 $Y^2=DP^2$ 在稠密的 $\mathcal D$ 上成立；两侧有界，遂成立于整个 $H$。
将 (2.1) 展开，混合项准确抵消：
$$
0=Y^2-DP^2
=D^2R^4+DR^2Q^2+\frac14Q^4-DR^2Q^2.
$$
因此
$$
\boxed{Q^4=-4\lambda^2 B^{2p}R^4\quad\text{于整个 }H.}
\tag{2.4}
$$
这条有界身份只来自同一根的已付域式；没有调用待求的一般分母。

## 3. 消去正则器时保留第一阶自然幂域

R125/R128 给每个 $S\in\mathscr C$ 保持 $\operatorname{Dom}Z$ 并与 $Z$ 域交换。
逐次归纳，它保持全部自然幂域 $\operatorname{Dom}Z^k$。
由 (1.6)，归纳还给
$$
R^kH\subseteq\operatorname{Dom}Z^k,\qquad
Z^kR^k=(ZR)^k\quad\text{于整个 }H.
\tag{3.1}
$$
这不是把形式积的闭包当作自然幂。

对固定 $x\in\operatorname{Dom}Z^4$，(1.6)、(3.1) 及真实域交换给
$$
Q^4x=F(B)^4(ZR)^4x
=R^4F(B)^4Z^4x.
$$
(2.4) 右边也可写成 $-4\lambda^2R^4B^{2p}x$。
因为 $R^4$ 单射，可以在这两个实际 $H$ 向量之间消去它，得到
$$
\boxed{
F(B)^4Z^4x=-4\lambda^2B^{2p}x
\qquad(x\in\operatorname{Dom}Z^4).
}
\tag{3.2}
$$
没有断言 $R^{-1}$ 全域有界，也没有假定 $R^4H$ 等于整个自然幂域。

## 4. 慢行与有界行分别排除

### 4.1 非绝对可和的原复行

若 $a\in\ell^2\setminus\ell^1$，R171 定理 1.1 已经证明：
有限柱空间 $\mathcal P$ 包含于 $\operatorname{Dom}Z^4$，且对于每个非零实际 UHF 算子 $E$，
$$
EZ^4|_{\mathcal P}\text{ 无界}.
\tag{4.1}
$$
这里完全保留原 carry，最高系数允许非单射、非可逆；该定理不局限于纯张量模型。

由于 $B$ 属于实际 UHF 代数，非零解析芽 $F$ 给
$$
F(B)^4\in\mathfrak U_m\setminus\{0\}.
$$
非零性由 $F(z)=z^r v(z)$、$v(0)\ne0$、原 $B$ 单射及 $v(B)$ 可逆得到。
而 (3.2) 使 $F(B)^4Z^4|_{\mathcal P}$ 等于固定有界算子
$-4\lambda^2B^{2p}|_{\mathcal P}$，与 (4.1) 矛盾。

这一步直接使用 R171 已付的自然幂域与无界性；
没有误称实际第一阶乘子把有限次数向量仍送进有限次数。

### 4.2 绝对可和行及常数行

若 $a\in\ell^1$（包括 $a=0$），则
$$
Z=a_*I+\sum_j a_jV_j
$$
在算子范数中收敛，故是 $\mathscr C$ 中的有界算子。
(3.2) 此时为全空间的有界身份。
对任意兼容字符喷射 $j_\chi:\mathscr C\to\mathbb C[[z]]$ 使用它，得到
$$
F(z)^4j_\chi(Z)^4=-4\lambda^2z^{2p}.
\tag{4.2}
$$
右边非零，所以 $j_\chi(Z)\ne0$。
记 $r=\operatorname{ord}F\ge0$、$s=\operatorname{ord}j_\chi(Z)\ge0$，
形式阶比较给
$$
4(r+s)=2p.
$$
左边被 4 整除，右边因 $p$ 奇数而不被 4 整除，矛盾。
这也处理了非零常数 $Z$；$Z=0$ 时 (4.2) 立即矛盾。

两种情况穷尽全部复 $\ell^2$ 第一阶行，定理得证。

## 5. 与 R143 的准确关系

R143 主稿 §6 (6.1)--(6.4) 对其实际二阶闭乘子 $X$ 的最低位 gauge 差给
$$
Z=X_{a_0+\sum_{j>0}b_{0j}\chi_j},\qquad
F(B)=4N_0(I-N_0^2)^{-1},\qquad
Q(t)=F(B)ZR(t).
$$
该稿 §§3--4 真实支付 $R(t)$ 单射、$R(t)H\subseteq\operatorname{Dom}Z$、
$ZR(t)$ 有界以及整个 $\operatorname{Dom}X$ 上的 (1.4)。
所以若**这个同一个实际 $X$** 还被要求是奇数原幂的闭稳定平方根，
上述定理直接矛盾；无需再核其根的伴随域。

结论也允许 $T$ 的其余部分不具有任何有限全局 Walsh 次数上限：
定理只要求它的同一个低位 gauge 比较真实落在 (1.6) 的一条第一阶行。
因此它不是从两端有限次数的 R101 直接重复一个有限 chaos 排除。
不过，此范围表述没有为一个尚未识别的任意闭根自动构造 (1.4)。

R143 §7 的横截核反根 $S$ 作用在未知闭尾不变空间 $K$。
现有结果没有证明 $U_{-1}K=K$，也没有证明 $S$ 的同一个低位 gauge 差就是上述第一行。
故不能把本定理直接作用于该未知 $K$ 上的 $S$；
R171 的全尾 UHF 测试也不能未经证明搬到任意不变限制。
本稿支付的是一个真正不可能的特殊根域来源，而非普通不变子空间问题的完成。

## 6. 全部不整除根与有界交换余项

平方情形的混合项抵消有如下完整代数版本。

**定理 6.1。** 设 $q\ge2$、$p\ge1$ 且 $q\nmid p$。
在同一个原尾 $H$ 上，令闭稠密算子 $T$ 满足
$$
T\mathcal D\subseteq\mathcal D,\qquad
T^qx=\lambda B^px\quad(x\in\mathcal D),\qquad\lambda\ne0,
\tag{6.1}
$$
并保留实际 $B$ 域交换。取 dyadic $\zeta$ 使 $\omega=\zeta^p\ne1$，
$G=U_\zeta TU_\zeta^*$，并假设 (1.3)--(1.4) 对此 $G$ 已付。
令 $Z$ 为 (1.5) 的任意实际复第一阶乘子，并要求
$$
RH\subseteq\operatorname{Dom}Z,\qquad ZR\in\mathscr C\text{ 有界},
\tag{6.2}
$$
以及
$$
\boxed{
Q=FZR+KR,\qquad
0\ne F\in\mathscr C\cap\mathfrak U_m,\qquad K\in\mathscr C.
}
\tag{6.3}
$$
则这些条件不可能同时成立。

这里 $F$ 不必是解析芽；$K$ 不必属于 UHF。
若 $p$ 奇数，原 $B$ 域交换可由 (6.1) 与奇幂恢复支付；一般 $p$ 不省略它。

### 6.1 先在实际根域中支付全部 $q$ 次作用

记 $D=\lambda B^p$。因 $\mathcal D$ 对 $T$ 及全部有界交换子稳定，
对 $x\in\mathcal D$、$0\le k\le q$，归纳得到
$$
G^kR^qx
=\sum_{j=0}^{k}{k\choose j}
R^{q-k+j}Q^{k-j}T^jx.
\tag{6.4}
$$
当 $k<q$，右侧每项至少还有一个 $R$，它的其余实际输入属于 $\mathcal D$，
故每项都由 (1.4) 落入 $\mathcal D_G$，下一次作用 $G$ 合法。
因而 (6.4) 不是在仅有 $q$ 阶形式域上任意相乘的二项式。

在 $k=q$ 时使用 $G^q=\omega D$，得
$$
\bigl((RT+Q)^q-\omega D R^q\bigr)x=0
\qquad(x\in\mathcal D).
\tag{6.5}
$$
同时 $(T^q-D)x=0$。这里所有系数都是交换的有界算子，并保持根的稳定域。

### 6.2 Resultant 是已付域式的有限代数后果

在普通多项式环中定义
$$
\mathcal H(d,z)
=\operatorname{Res}_t\bigl(t^q-d,(t+z)^q-\omega d\bigr)
=\sum_{k=0}^{q^2}h_k(d)z^k.
\tag{6.6}
$$
它是 $z$ 的 $q^2$ 次首一多项式，$h_k\in\mathbb C[d]$。
有限 Sylvester 伴随矩阵给 resultant 属于两输入多项式生成的理想。
所以把该有限 Bézout 身份在 $T$ 上求值合法：稳定域支持其中全部有限次幂，
(6.1)、(6.5) 使每项消失。
所得 bounded resultant 在稠密的 $\mathcal D$ 上为零，故在 $H$ 上为零。

其明确齐次式为
$$
\boxed{
\sum_{k=0}^{q^2}h_k(D)R^{q^2-k}Q^k=0
\quad\text{于整个 }H.
}
\tag{6.7}
$$
这一齐次恒等式可先在纯标量环验证：
$$
\operatorname{Res}_t(t^q-d,(rt+s)^q-\omega d r^q)
=\prod_{\alpha^q=d,\,\beta^q=\omega d}(s+r(\alpha-\beta))
=\sum_kh_k(d)r^{q^2-k}s^k.
$$
等式两侧原本都是 $d,r,s$ 的多项式，因此不要求 $R$ 有有界逆，
也没有在算子层面真的除以 $R$。

### 6.3 返回同一第一阶乘子的自然多项式

在 $\operatorname{Dom}Z^{q^2}$ 上，(6.2) 和真实域交换逐次给
$$
Q^kx=R^k(FZ+K)^kx\qquad(0\le k\le q^2).
$$
$FZ+K$ 的这次写法只指在足够自然幂域上的有限展开，
不声称它另有未经识别的闭实现。
因此 (6.7) 给
$$
R^{q^2}\mathcal H(D,FZ+K)x=0.
$$
由 $R$ 单射，
$$
\boxed{
\mathcal H(D,FZ+K)x=0
\qquad(x\in\operatorname{Dom}Z^{q^2}).
}
\tag{6.8}
$$
把它按自然幂 $Z^k$ 展开，最高系数准确为 $F^{q^2}$；
其余系数都是有界交换子。

需要核实 $F^{q^2}\ne0$：若此幂为零，所有兼容喷射在形式整环中都使 $j_\chi(F)=0$，
即 $F\in\mathfrak I_{\infty,m}$。
已证 $\mathfrak I_{\infty,m}\cap\mathfrak U_m=\{0\}$，与 $F\ne0$ 矛盾。
所以 $F^{q^2}\in\mathfrak U_m\setminus\{0\}$。

若 $a\notin\ell^1$，R171 定理 1.1 直接说 (6.8) 左侧在有限柱上无界，
而 (6.8) 使它恒零，矛盾。

若 $a\in\ell^1$，则 $Z$ 全域有界。取任意兼容喷射，写
$$
s(z)=j_\chi(FZ+K)\in\mathbb C[[z]].
$$
(6.8) 给 $\mathcal H(\lambda z^p,s(z))=0$。
在形式 Puiseux 域 $\mathbb C((z^{1/q}))$ 中，任选 $\lambda^{1/q}$、$\omega^{1/q}$，
并令 $\xi_0,\ldots,\xi_{q-1}$ 为全部 $q$ 次单位根，则
$$
0=\prod_{i,j=0}^{q-1}
\left(s(z)+\lambda^{1/q}(\xi_i-\omega^{1/q}\xi_j)z^{p/q}\right).
\tag{6.9}
$$
因为 $\omega\ne1$，每个常数 $\xi_i-\omega^{1/q}\xi_j$ 都非零。
形式域没有零因子，故某个因子为零；这迫
$$
s(z)=c z^{p/q}\quad\text{其中 }c\ne0.
$$
但左边只有非负整数幂，$q\nmid p$ 使右边具有非整数幂，矛盾。
定理 6.1 得证。

该证明没有取得未知底空间的 gauge 保持，也没有把全尾 R171 测试传给未知限制。
它明确识别了不能产生不整除原幂根的一整类实际共同域来源。

## 已证来源

- [R143：共同 gauge 正则化与实际最低行](../results/R143-quadratic-gauge-common-regularizers-and-kernel-graphs.md)，§§3--4、6；
- [R171：无界第一阶乘子的 UHF 最高系数多项式](../results/R171-uhf-leading-polynomials-of-unbounded-first-multipliers.md)，定理 1.1；
- [R176：全部第一阶自然幂域和最大图](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)，§§1--4；
- [原全交换子的兼容形式喷射](../results/R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md)；
- [原尾奇幂强恢复](../results/R12-appendix-odd-power-strong-recovery-all-power-commutants-and-actual-subquotients.md)。
