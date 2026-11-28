# R12 附录：原逆变量与同一平坦分母的联合解析来源、普遍单射及严格扩大闭场

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整的真正联合来源。** 本稿处理 $\sum_{j\ge0}P^j f_j(C^{-1})$ 的一个明确双系数类，不再只是把单变量函数改名。对每个非零双变量来源，实际有界分子在全部原有限放大旗商上单射、稠密值域，最大分式有原参数图核心。证明还显示：同一个实际 $P$ 在此前的单变量闭场上代数超越；$e^P$ 又不属于该旧场与 $P$ 生成的有理函数场。

新输入是同一 $P$ 的非线性幂预算及其解析逆费用。这里仍未构造 $Y^2=CP^2$；本稿最后准确划出联合解析类之外尚须寻找的来源。

## 1. 固定两个实际变量和双系数类

固定原 Haar 尾 $C=A^{(m_0)}$，取[定量稿](R267-appendix-quantitative-positive-common-denominator-and-strict-superquartic-inverse-cost.md)的同一个 $P$，记
$R_n=C^{-n}P$。沿用[单变量整逆稿](R12-appendix-quantitative-flat-entire-inverse-sources-and-universal-closed-fractions.md)的

$$
F_f=\sum_{n\ge0}a_nR_n,\qquad
F_fF_g=P F_{fg},\qquad C F_{zf}=F_f.
\tag{1.1}
$$

[同分母非线性幂稿](R267-appendix-same-positive-denominator-exact-power-cost-and-neumann-budget.md) 已付

$$
\log(-\log\|P^n\|)=\frac{\log16}{48}n^{3/2}+o(n^{3/2}),
\tag{1.2}
$$

以及对每个 $\varepsilon>0$ 的全参数预算

$$
\mathcal R_P(t)=\sum_{n\ge0}t^n\|P^n\|,\qquad
\log^+\mathcal R_P(t)\le K_\varepsilon[1+\log(2+t)]^{1+\varepsilon}.
\tag{1.3}
$$

这些上界下降到每个原有限放大旗商。$P_Q$ 的单射、稠密值域仍由同一个收缩强单位支付。

定义 $\mathscr B$ 为下列双变量解析芽的并：

$$
F(z,w)=\sum_{n,j\ge0}a_{n,j}z^n w^j,\qquad
|a_{n,j}|\le A\rho^{-j}e^{-c n^p}
\tag{1.4}
$$

其中某些固定 $A<\infty,\rho>0,c>0,p>4$ 同时适用于全部 $n,j$。
$F$ 对 $z$ 整，对 $w$ 在 $|w|<\rho$ 全纯。它不是任意两变量全纯函数类。

$\mathscr B$ 是代数，包含多项式、旧快速整函数以及任意只依赖 $w$ 的收敛芽。加法取共同参数；乘法在 $n$ 方向用
$k^p+(n-k)^p\ge2^{1-p}n^p$，在 $j$ 方向把 $(j+1)\rho^{-j}$ 吸入更小正半径，便得到同型预算。乘 $z$、乘 $w$、除去有限 $w$ 阶也保持此类。

写 $F=\sum_j f_j(z)w^j$，定义实际有界分子

$$
\boxed{\mathcal A_F=\sum_{j\ge0}P^jF_{f_j}
=\sum_{n,j\ge0}a_{n,j}R_nP^j.}
\tag{1.5}
$$

双和在算子范数中绝对收敛：$n$ 方向由同源 $R_n$ 预算控制，
$j$ 方向由 $\sum\rho^{-j}\|P^j\|<\infty$ 控制。无需 $\rho>\|P\|$。
全部系数互相交换、保持原旗，且

$$
\boxed{
\mathcal A_F\mathcal A_G=P\mathcal A_{FG},\quad
C\mathcal A_{zF}=\mathcal A_F,\quad
P\mathcal A_F=\mathcal A_{wF},\quad
\mathcal A_1=P,\quad\mathcal A_z=R_1,\quad\mathcal A_w=P^2.}
\tag{1.6}
$$

## 2. 一个完整的 $L^q$ Jensen 预算

以下初等事实用于实际解析分母，避免把点态除法当作一致界。

**引理 2.1。** 设非零整函数 $f$ 的增长满足

$$
\log^+M_f(R)=O([\log(2+R)]^\sigma).
$$

则对每个固定 $q\ge1$，当 $r\ge1$ 时，

$$
\left(\frac1{2\pi}\int_0^{2\pi}
[\log^-|f(re^{it})|]^q\,dt\right)^{1/q}
=O_{f,q}([\log(2+r)]^\sigma).
\tag{2.1}
$$

**证明。** 先剥 $f(z)=z^s h(z)$ 并除去 $h(0)\ne0$ 的常数，使新的整函数在 $0$ 等于 $1$。$r\ge1$ 时 $z^s$ 不增大所需负对数；常数只添固定项。

选不穿零点的 $R_0\in[2r,3r]$。用圆盘 $|z|<R_0$ 中全部零点（含重数）的有限 Blaschke 积 $B$ 写 $f=Bg$。$g$ 在该圆盘内无零；边界 $|B|=1$。置
$L=\log M_f(R_0)\ge0$。调和函数
$u=L-\log|g|\ge0$ 满足
$u(0)\le L$，因为 $f(0)=1$ 且 $|B(0)|\le1$。
Harnack 不等式给 $|z|=r$ 上 $u\le3L$，故
$\log^-|g|\le2L$。

每个 Blaschke 因子
$b_a(z)=R_0(z-a)/(R_0^2-\overline a z)$ 的
$-\log|b_a(re^{it})|$ 有与 $a,r,R_0$ 无关的固定 $L^q$ 界。
确切地，它至多为
$\log4+\log^-|e^{it}-a/r|$；
单位圆与半径 $\delta$ 圆盘的交弧长度为 $O(\delta)$，
所以后者的分布尾为 $O(e^{-t})$，给全部有限 $q$ 的一致可积性。

零点数由半径 $2R_0$ 的 Jensen 公式控制：
$N(R_0)\log2\le\log M_f(2R_0)$。
将各因子的 $L^q$ 范数相加，得到
$\|\log^-|f(re^{it})|\|_{L^q}\le C_q\log M_f(6r)$。
代入假设即得 (2.1)；边界半径用邻近圆极限处理。证毕。

## 3. 同一 $P$ 的真正解析分母费用

设 $F\in\mathscr B$ 的最低非零 $w$ 系数为 $f_0$，即暂已提出可能的有限 $w$ 幂，且 $f_0\not\equiv0$。由 (1.4)，可取一个标量函数 $M(R)\ge e$，使

$$
|f_j(\lambda)|\le\rho^{-j}M(R)\quad(|\lambda|\le R),\qquad
\log M(R)=O([\log(2+R)]^\sigma),\qquad
\sigma=\frac p{p-1}<\frac43.
\tag{3.1}
$$

对于 $f_0(\lambda)\ne0$，在原空间或任意旗商上有实际分解

$$
F(\lambda,P_Q)=f_0(\lambda)(I+P_QV_{\lambda,Q}),
$$

$$
V_{\lambda,Q}
=\sum_{j\ge1}\frac{f_j(\lambda)}{f_0(\lambda)}P_Q^{j-1},
\qquad
\|V_{\lambda,Q}\|\le
L_\rho\,\frac{M(R)}{|f_0(\lambda)|},\quad
L_\rho=\sum_{j\ge1}\rho^{-j}\|P^{j-1}\|<\infty.
\tag{3.2}
$$

所有级数范数绝对收敛。(1.3) 及
$(P_QV_{\lambda,Q})^n=P_Q^nV_{\lambda,Q}^n$
给真逆，而非仅形式逆。因而对每个 $\varepsilon>0$，

$$
\boxed{
\log^+\|F(\lambda,P_Q)^{-1}\|
\le K\,[1+\log M(R)+\log^-|f_0(\lambda)|]^{1+\varepsilon}.}
\tag{3.3}
$$

常数依赖固定 $F,P,\varepsilon$，不依赖 $Q$ 或 $R$。
$f_0(0)=0$ 时，只在引理 2.1 的标量 Jensen 步骤剥该零点；
不错误地把整个 $F(z,w)$ 都除以同一个 $z$ 幂。

由引理 2.1，(3.3) 在半径 $R$ 圆上的均值满足

$$
\frac1{2\pi}\int_0^{2\pi}
\log^+\|F(Re^{it},P_Q)^{-1}\|\,dt
=O([\log(2+R)]^{\sigma(1+\varepsilon)}).
\tag{3.4}
$$

离散的 $f_0$ 零点不妨碍这个可积界。正是 (1.2) 的新非线性幂费用使
$\varepsilon$ 可以任意小；仅有共同整数逆或固定四次幂界不足以自动给此预算。

## 4. 联合差商与同旗的原预解系数

对每个 $f_j$ 取
$g_{j,\lambda}(z)=(f_j(z)-f_j(\lambda))/(z-\lambda)$，并定义

$$
\mathcal G_\lambda=\sum_{j\ge0}P^jF_{g_{j,\lambda}}.
\tag{4.1}
$$

(1.4) 的统一参数、同 $R_n$ 的单变量差商估计，以及
$\sum\rho^{-j}\|P^j\|<\infty$，给算子范数整性及

$$
\log^+\sup_{|\lambda|\le R}\|\mathcal G_\lambda\|
=O([\log(2+R)]^\sigma).
\tag{4.2}
$$

逐项绝对收敛允许准确相加，得到

$$
\boxed{(I-\lambda C)\mathcal G_\lambda
=C\mathcal A_F-CP F(\lambda,P).}
\tag{4.3}
$$

该式保持同一来源，并下降到每个原旗商 $Q$。

**定理 4.1。** 每个非零 $F\in\mathscr B$ 在每个非零有限放大原旗商 $Q$ 上满足

$$
\ker\mathcal A_{F,Q}=0,\qquad
\overline{\mathcal A_{F,Q}Q}=Q.
\tag{4.4}
$$

**证明单射。** 假设 $\mathcal A_{F,Q}x=0$、$x\ne0$。先提出 $F$ 的最低 $w$ 幂；由 $P_Q$ 单射可以取消它，故设 $f_0\not\equiv0$。
令 $p_0=P_Qx\ne0$。所有系数与
$F(\lambda,P_Q)^{-1}$ 交换，因此在 $f_0(\lambda)\ne0$ 时，
$F(\lambda,P_Q)^{-1}x$ 仍属于同一核。将 (4.3) 作用于这个实际向量，得到

$$
\mathcal G_{\lambda,Q}F(\lambda,P_Q)^{-1}x
=-C_Q(I-\lambda C_Q)^{-1}p_0.
\tag{4.5}
$$

内积取第一变量线性，设整个标量函数

$$
H(\lambda)=
\langle C_Q(I-\lambda C_Q)^{-1}p_0,p_0\rangle.
$$

由 (4.5)，其圆周零点以外的对数满足
$\log^+|H|\le
O(1)+\log^+\|\mathcal G_{\lambda,Q}\|
+\log^+\|F(\lambda,P_Q)^{-1}\|$。
对半径 $2R$ 圆积分，再用 $\log^+|H|$ 的 Poisson 核上界 $3$，
(3.4)、(4.2) 给

$$
\log^+M_H(R)
=O([\log(2+R)]^{\sigma(1+\varepsilon)}).
\tag{4.6}
$$

选 $\varepsilon>0$ 使 $\sigma(1+\varepsilon)<4/3$。

另一方面，同一个 $Q$ 的真实弱返回

$$
C_Q^{2^j}/d_j\xrightarrow{\mathrm{WOT}}\tfrac12I_Q,\qquad
-\log d_j\le500\,16^{m_0+j}
$$

给
$|\langle C_Q^{2^j}p_0,p_0\rangle|\ge d_j\|p_0\|^2/4$
对充分大 $j$ 成立。此即 $H$ 的第 $2^j-1$ 个系数。
置 $n=2^j$、$R_j=\exp(1000\,16^{m_0}n^3)$，
Cauchy 系数界给

$$
\log M_H(R_j)\ge250\,16^{m_0}n^4
$$

对充分大 $j$ 成立，违反 (4.6)。所以核为零。

**证明稠值。** 若 $\overline{\mathcal A_{F,Q}Q}$ 是真闭空间，它因交换性而
$C_Q$ 不变。再取这个闭像商，得到一个非零原旗商，上面的
$\mathcal A_F$ 诱导零算子，违反刚证明的单射性。故 (4.4) 成立。
全过程没有使用未知 $Q$ 的正真空或 $P_Q$ 幂范数下界。证毕。

特别 $\mathcal A_F=0$ 当且仅当解析芽 $F=0$；(1.5) 是忠实的联合来源。

## 5. 最大闭分式与原参数图核心

对 $F,G\in\mathscr B$、$G\ne0$，定义

$$
\Gamma S_{F/G,Q}
=\{(x,y)\in Q^2:\mathcal A_{F,Q}x=\mathcal A_{G,Q}y\}.
\tag{5.1}
$$

它是闭、稠密定义的算子图。这个最大图本身是
$C_Q\oplus C_Q$ 的实际闭不变子空间，从而也是某个有限放大原旗商。
由 (4.4)，同一对角分母 $\operatorname{diag}(\mathcal A_G,\mathcal A_G)$
在该图上稠值，其像满足

$$
(\mathcal A_Gx,\mathcal A_Gy)
=(\mathcal A_Gx,\mathcal A_Fx).
$$

所以准确有

$$
\boxed{
\Gamma S_{F/G,Q}
=\overline{\{(\mathcal A_{G,Q}h,\mathcal A_{F,Q}h):h\in Q\}}.}
\tag{5.2}
$$

同一结论也用于真实分母积
$\mathcal A_G\mathcal A_K$，因为它在每个原旗商上仍单射稠值。
利用 (1.6) 取消公共的单射因子 $P_Q$，以及这些同分母参数核心，得到

$$
\overline{S_{F/G,Q}S_{H/K,Q}}=S_{FH/(GK),Q},\qquad
\overline{S_{F/G,Q}+S_{H/K,Q}}=S_{(FK+HG)/(GK),Q}.
\tag{5.3}
$$

例如自然乘积包含全部准确参数对
$(\mathcal A_G\mathcal A_Kh,\mathcal A_F\mathcal A_Hh)$；
它们是相应最大乘积图的核心。非零分式翻转图即为逆。
由 (4.4)，交叉相乘也证明这个 $\operatorname{Frac}\mathscr B$ 表示忠实。

两个坐标的实际含义是

$$
\boxed{S_z=C_Q^{-1},\qquad S_w=P_Q.}
\tag{5.4}
$$

$z$ 的域仍准确为 $\operatorname{Ran}C_Q$；$w$ 在全 $Q$ 上有界。
全部限制及再商的图像闭包与 (5.1) 相容。
非零分式在真实域中保持每个闭 $C_Q$ 不变子空间；
再对其逆应用一次，给
$[S_{F/G,Q}x]_{C_Q}=[x]_{C_Q}$。
原整个 Haar 空间的同一 $J$ 对称与 (5.2) 还给
$S_{F/G}^*=JS_{F/G}J$；不向未知商附加共轭。

这些图论步骤沿用此前已付的最大图方法；
新增的是 (4.4) 的完整双变量实际来源，而非再次登记抽象分式等价框架。

## 6. 它严格超出此前的单变量场

记旧单变量闭场为
$\mathbb K_0=\operatorname{Frac}\mathscr E_{>4}$，其变量 $z$ 实现为 $C^{-1}$。
它自然嵌入本场的 $w$ 无关部分。

**定理 6.1。** 实际有界算子 $P$ 在该嵌入的 $\mathbb K_0$ 上代数超越。
特别 $P\notin\mathbb K_0$，新场不是旧场的另一种表示。

**证明。** 若存在有限非平凡代数关系
$\sum_{j=0}^d h_j(C^{-1})P^j=0$，其中 $h_j\in\mathbb K_0$，
在已付的闭场运算中乘以共同分母，得到

$$
\sum_{j=0}^d f_j(C^{-1})P^j=0,
\qquad f_j\in\mathscr E_{>4},\quad \text{不全为零}.
$$

这正是非零解析芽
$F(z,w)=\sum_{j=0}^d f_j(z)w^j$ 的最大实现为零。
乘回同一 $P$ 后有 $\mathcal A_F=0$，违反定理 4.1。证毕。

联合的无限 $j$ 范围也是真扩大。$e^w\in\mathscr B$，其实际实现为有界单位 $e^P$。若 $e^P\in\mathbb K_0(P)$，清分母会得到某个非零有限表达式

$$
\sum_{k=0}^d p_k(z,w)e^{kw}=0,\qquad
p_k(z,w)\in\mathscr E_{>4}[w],
$$

在实际算子上为零。此表达式属于 $\mathscr B$。它不可能是零解析芽：
固定一个使各非零系数不全消失的 $z$，得到非零的标量指数多项式；
沿实 $w\to+\infty$，最大 $k$ 的非零多项式不能被较小指数项抵消。
这与忠实性矛盾。因此 $e^P\notin\mathbb K_0(P)$。

## 7. 已付的非线性作用与剩余二次源

真正新支付的是：一个全 $H$ 有界、全旗普遍的平坦锚 $P$，
可以与旧逆变量按 (1.4) 联合取无限解析级数，
其每个非零分子及每个分母都保真实原图核心。
(3.2)–(3.4) 明确给出了所用非线性逆费用。
这里既没有任意多来源的联合闭性，也没有任意双无限 Laurent 来源。

本联合场仍不含 $S^2=C_Q$ 的稳定闭根。
若有这样的非零最大分式 $S_{F/G,Q}$，
由自然平方闭包及忠实性须有

$$
zF(z,w)^2=G(z,w)^2.
\tag{7.1}
$$

比较最低 $w$ 次数，双方必须具有同一阶。
取消它后，在 $w=0$ 得到非零整函数 $f,g$ 的
$zf(z)^2=g(z)^2$，其 $z=0$ 阶数一奇一偶，矛盾。
所以不能从这个联合解析场中选出同一 $P$ 的平方分子 $Y$。

这条边界只针对已完整定义的 $\mathscr B$。全原交换代数中仍可能有不属于该联合解析类的复抵消来源；它们的实际构造或排除都尚未完成，普通 ISP 也未因此解决。
