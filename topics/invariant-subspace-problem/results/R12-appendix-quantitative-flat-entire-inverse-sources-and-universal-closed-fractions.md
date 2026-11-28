# R12 附录：同一定量平坦分母的快速整函数逆源与全部原旗的最大闭分式场

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整实际来源与全旗图核心定理。** 对原 Haar 尾 $C$，本稿从一个固定的定量平坦分母 $P$ 构造 $F_f=\sum a_n C^{-n}P$。系数以某个严格大于四次的指数衰减时，每个非零 $F_f$ 在全部原有限放大不变子商上单射、稠密值域。由此获得同一分子分母的最大闭图、真实参数图核心及闭包场运算。证明使用同一子商上的真实 dyadic 幂弱极限，没有把原空间稠密性自动传给闭图。

这不是任意整函数的演算，也不是闭平方根的存在定理。最后明确证明本稿的忠实分式场本身不能提供 $S^2=C$ 的稳定闭根。

## 1. 同一实际分母及系数代数

固定原 Haar 尾 $C=A^{(m_0)}$，取[定量共同分母稿](R267-appendix-quantitative-positive-common-denominator-and-strict-superquartic-inverse-cost.md)明确构造的同一个 $P$。记

$$
R_n=C^{-n}P\in C',\qquad R_0=P,\qquad C^nR_n=P.
\tag{1.1}
$$

这里每个 $R_n$ 在全 $H$ 上有界，且已经支付同源预算

$$
\log^+\|R_n\|
\le K_{m_0}n^4
\exp\!\left(300[\log(2+n)]^{2/3}\right)\quad(n\ge1).
\tag{1.2}
$$

同一 $P$ 有 $W_j\in\mathcal A=\overline{\mathbb C[I,C]}^{\|\cdot\|}$，满足

$$
\|PW_j\|\le1,\qquad PW_j\longrightarrow I\quad\text{强*}.
\tag{1.3}
$$

因此 $P$ 在全部有限放大中的原闭不变旗子商上单射、稠密值域。[R88](R88-riesz-basis-bounded-multipliers-strong-closure.md) 的原有界强多项式闭包保证本稿全部有界交换系数保持这些旗。

定义整函数代数

$$
\mathscr E_{>4}
=\left\{f(z)=\sum_{n\ge0}a_nz^n:
\exists\,p>4,\ c>0,\ A<\infty,\quad
|a_n|\le A e^{-c n^p}\ (n\ge0)\right\}.
\tag{1.4}
$$

多项式包含在内；它在加法、乘法、乘以 $z$、除去有限阶零点及固定点差商下封闭。乘法取两个来源的共同较小指数 $p>4$，用

$$
j^p+(n-j)^p\ge2^{1-p}n^p
$$

控制卷积，再把因子 $n+1$ 吸入较小的正指数常数。除去有限零点只平移系数；固定点差商的预算也见第 3 节。

对 $f\in\mathscr E_{>4}$ 定义

$$
\boxed{F_f=\sum_{n\ge0}a_nR_n.}
\tag{1.5}
$$

(1.2) 使该级数在算子范数中绝对收敛。对每个 $x$，它确实是
$\sum a_n C^{-n}(Px)$ 的 $H$ 范数和；没有在 $P H$ 之外预置一个无界逆幂级数。

## 2. 真实乘法、整除与全部原旗

由原 $C$ 单射及有界交换关系，

$$
R_jR_k=P R_{j+k},\qquad C R_{n+1}=R_n.
\tag{2.1}
$$

绝对双和给准确的有界恒等式

$$
\boxed{
F_fF_g=P F_{fg},\qquad
C F_{zf}=F_f,\qquad
F_1=P,\qquad F_z=R_1.}
\tag{2.2}
$$

特别 $f\mapsto F_f$ 是带固定因子 $P$ 的乘法表示，不把它误写成通常的有幺代数同态。对每个 $r$，

$$
F_f=C^rF_{z^rf};
\tag{2.3}
$$

所以全部 $F_f$ 是原各整数幂的实际有界共同倍数。

若 $Q=M/N$ 是任意有限放大 $C^{(d)}$ 的原闭不变旗子商，以下系数均在同一 $Q$ 上诱导，且范数不增加。写作 $C_Q,P_Q,R_{n,Q},F_{f,Q}$；(1.1)–(2.3) 在该商上保留。[R140 §§1、2、6](R140-invariant-subquotient-type-and-fixed-first-regularization.md) 已付

$$
C_Q\text{ 单射、稠密值域、拟幂零},\qquad
\frac{C_Q^{2^j}}{d_j}\xrightarrow{\mathrm{WOT}}\frac12 I_Q,
\quad d_j=\|C^{2^j}\|.
\tag{2.4}
$$

这里的 $d_j$ 是固定环境尾的真实归一化常数。式 (2.4) 来自同一原幂经旗商诱导；不以未知商自身范数替换分母。定量稿还给

$$
-\log d_j\le500\,16^{m_0+j}.
\tag{2.5}
$$

## 3. 同源差商的低对数增长

若 $f$ 满足 (1.4)，固定 $\lambda\in\mathbb C$，定义整差商

$$
g_\lambda(z)=\frac{f(z)-f(\lambda)}{z-\lambda}.
$$

从准确有限差幂展开，

$$
F_{g_\lambda}
=\sum_{n\ge1}a_n\sum_{k=0}^{n-1}\lambda^{n-1-k}R_k.
\tag{3.1}
$$

(1.2) 蕴含存在有限常数 $B_f$，使
$\max_{k<n}\|R_k\|\le B_f e^{(c/2)n^p}$。因此对 $|\lambda|\le R$，

$$
\|F_{g_\lambda}\|
\le AB_f\sum_{n\ge1}n e^{-(c/2)n^p}(1+R)^n.
\tag{3.2}
$$

右侧在每个紧 $\lambda$ 集一致收敛，故 (3.1) 是算子范数意义的整函数；逐个固定 $\lambda$ 时，它也证明 $g_\lambda\in\mathscr E_{>4}$。例如先以 $n\log^+|\lambda|\le(c/2)n^p+O_\lambda(1)$ 控制系数尾，再缩小指数常数。

置

$$
\sigma=\frac p{p-1}<\frac43.
$$

将 $n\log(1+R)-(c/4)n^p$ 最大化，剩余
$\sum n e^{-(c/4)n^p}$ 可和，便得

$$
\log^+\max_{|\lambda|\le R}\|F_{g_\lambda}\|
+\log^+\max_{|\lambda|\le R}|f(\lambda)|
=O_f\!\left([\log(2+R)]^\sigma\right).
\tag{3.3}
$$

这一步保留同一个 $R_k=C^{-k}P$ 的实际范数费用。

差商的标量恒等式与 (2.2) 给

$$
\boxed{(I-\lambda C)F_{g_\lambda}
=C F_f-f(\lambda)CP.}
\tag{3.4}
$$

此式及 (3.1)–(3.3) 原样下降到同一旗商 $Q$。

## 4. 每个非零分子在全部原子商上单射

**定理 4.1。** 若 $f\in\mathscr E_{>4}$ 且 $f\ne0$，则对每个非零有限放大原旗商 $Q$，

$$
\ker F_{f,Q}=\{0\}.
\tag{4.1}
$$

**证明。** 假设 $F_{f,Q}x=0$ 且 $x\ne0$。若 $f$ 在 $0$ 有阶数 $s$ 的零点，先写 $f=z^s h$；由 $C_Q^sF_{f,Q}=F_{h,Q}$，仍有 $F_{h,Q}x=0$。再除以 $h(0)\ne0$，故可从此假设 $f(0)=1$。不能对有零点的原 $f$ 直接使用 Jensen 的常数锚。

令

$$
p_0=P_Qx\ne0.
$$

非零性由 (1.3) 的同一商上强单位给出。因 $C_Q$ 拟幂零，$(I-\lambda C_Q)^{-1}$ 对全部 $\lambda$ 是有界整函数。将 (3.4) 作用于 $x$，得到

$$
F_{g_\lambda,Q}x
=-f(\lambda)C_Q(I-\lambda C_Q)^{-1}p_0.
\tag{4.2}
$$

内积取第一变量线性，设

$$
H(\lambda)=
\langle C_Q(I-\lambda C_Q)^{-1}p_0,p_0\rangle,\qquad
G(\lambda)=\langle F_{g_\lambda,Q}x,p_0\rangle.
$$

二者整，且

$$
f(\lambda)H(\lambda)=-G(\lambda).
\tag{4.3}
$$

由 (3.3)，$f,G$ 均有不超过 $\sigma<4/3$ 的对数增长。

这里可完整控制商，而无需选择避开所有零点的射线。记 $M_u(R)=\max_{|\lambda|\le R}|u(\lambda)|$。Jensen 公式及 $f(0)=1$ 给圆均值

$$
m_{2R}(\log^-|f|)
\le m_{2R}(\log^+|f|)
\le\log^+M_f(2R).
\tag{4.4}
$$

由 (4.3)，几乎处处
$\log^+|H|\le\log^+|G|+\log^-|f|$。
对次调和函数 $\log^+|H|$，半径 $2R$ 圆到半径 $R$ 圆的 Poisson 核最多为 $3$。因此

$$
\log^+M_H(R)
\le3\bigl(\log^+M_G(2R)+\log^+M_f(2R)\bigr)
=O([\log(2+R)]^\sigma).
\tag{4.5}
$$

圆上有限零点的对数可积；也可先取不穿零点的邻近半径再极限。若 $G$ 恒零，(4.3) 已直接迫 $H=0$，下述系数同样给矛盾。

另一方面，$H$ 的 $\lambda^{2^j-1}$ 系数是
$\langle C_Q^{2^j}p_0,p_0\rangle$。同一商上的 (2.4) 给充分大 $j$ 时

$$
|\langle C_Q^{2^j}p_0,p_0\rangle|
\ge\frac14d_j\|p_0\|^2.
\tag{4.6}
$$

置 $n=2^j$，取 $R_j=\exp(1000\,16^{m_0}n^3)$。Cauchy 系数界与 (2.5)–(4.6) 于是给

$$
\begin{aligned}
\log M_H(R_j)
&\ge (n-1)\log R_j+\log d_j+\log(\|p_0\|^2/4)\\
&\ge 250\,16^{m_0}n^4
\end{aligned}
\tag{4.7}
$$

对充分大 $j$ 成立。(4.5) 却只给 $O(n^{3\sigma})$，而 $3\sigma<4$，矛盾。证毕。

## 5. 全旗稠密值域及忠实性

对非零 $f$ 和任意 $Q$，令
$L=\overline{F_{f,Q}Q}$。它是闭 $C_Q$ 不变空间。若 $L\ne Q$，则真实再商 $Q/L$ 仍是有限放大原旗子商，且 $F_f$ 在该非零商上诱导零算子，违反定理 4.1。因此

$$
\boxed{\ker F_{f,Q}=0,\qquad
\overline{\operatorname{Ran}F_{f,Q}}=Q
\quad(f\ne0).}
\tag{5.1}
$$

这一步使用真实闭像再商，不假设未知 $Q$ 继承原共轭，也不从环境空间稠密值域外推。特别 $f\mapsto F_f$ 忠实：$F_f=0$ 当且仅当 $f=0$。

(2.3) 及 (5.1) 给一整类新的实际平坦普遍分母。它们非零时均在原 UHF 代数外，依赖原共同倍数理想与 UHF 的零交定理；没有将这个零交结论反过来当作单射性来源。

## 6. 同一分子分母的最大闭图与真正参数核心

取 $f,g\in\mathscr E_{>4}$，$g\ne0$。在每个 $Q$ 上定义准确最大图

$$
\boxed{\Gamma S_{f/g,Q}
=\{(x,y)\in Q^2:F_{f,Q}x=F_{g,Q}y\}.}
\tag{6.1}
$$

$F_{g,Q}$ 单射使它是算子图；有界核表示使图闭。交换性给全部参数对

$$
(F_{g,Q}h,F_{f,Q}h)\in\Gamma S_{f/g,Q}\qquad(h\in Q).
\tag{6.2}
$$

(5.1) 使定义域稠密；若 $f\ne0$，也给该闭算子单射、值域稠密。

现在严格支付核心。令 $\mathcal L=\Gamma S_{f/g,Q}$。它是
$C_Q\oplus C_Q$ 的闭不变子空间。若原 $Q=M/N$，则 $\mathcal L$ 的原像是 $M^2$ 中包含 $N^2$ 的闭 $C^{(2d)}$ 不变空间，所以 $\mathcal L$ 本身也是适用 (5.1) 的实际有限放大原旗子商。

故同一个对角分母
$\operatorname{diag}(F_{g,Q},F_{g,Q})|_{\mathcal L}$
在 $\mathcal L$ 上稠密值域。对 $(x,y)\in\mathcal L$，其像准确为

$$
(F_{g,Q}x,F_{g,Q}y)
=(F_{g,Q}x,F_{f,Q}x),
$$

已在 (6.2) 的参数图内。于是

$$
\boxed{\Gamma S_{f/g,Q}
=\overline{\{(F_{g,Q}h,F_{f,Q}h):h\in Q\}}.}
\tag{6.3}
$$

这里应用的是同一最大闭图上的真实分母稠值，远强于单独的
$\overline{F_{g,Q}Q}=Q$。抽象闭图步骤与 [R199 §6](R199-positive-inverse-sums-universal-calculus-and-countable-sources.md) 一致；本稿的新输入是 §§1–5 已完整建立的原 $C^{-1}$ 快整函数来源，不能从旧正逆类直接套出它。

同一论证对分母 $F_{g,Q}F_{k,Q}$ 也成立：两个因子都在每个原旗商上稠值，所以其积在该商上仍稠值。该事实将在闭包乘法中使用。

## 7. 忠实分式场、原乘积闭包与全部旗相容

在有理表示中，(2.2) 的公共因子 $P_Q$ 单射，所以可以准确取消。若 $fk=hg$，则
$F_fF_k=F_hF_g$；结合各分母单射，(6.1) 给

$$
S_{f/g,Q}=S_{h/k,Q}.
\tag{7.1}
$$

反之，若两最大图相同，测试共同输入
$F_{g,Q}F_{k,Q}u$，得到
$P_QF_{fk-hg,Q}u=0$。由 $P_Q$ 单射及 (5.1)，必有 $fk=hg$。所以该表示在每个非零 $Q$ 上忠实。

自然和、自然积满足最大图包含。具体地，若
$y=S_{h/k,Q}x$、$z=S_{f/g,Q}y$，则

$$
F_{g,Q}F_{k,Q}z=F_{f,Q}F_{h,Q}x;
$$

取消 $P_Q$ 给 $F_{gk,Q}z=F_{fh,Q}x$。另一方面，对每个 $u$，

$$
x=F_{g,Q}F_{k,Q}u,\quad
y=F_{g,Q}F_{h,Q}u,\quad
z=F_{f,Q}F_{h,Q}u
\tag{7.2}
$$

确实属于这个自然乘积的图。(7.2) 是同一最大图以真实分母
$F_gF_k=P F_{gk}$ 给出的参数核心；第 6 节末段证明它图稠密。自然和同理，用参数输出
$(F_fF_k+F_hF_g)u$。因此

$$
\boxed{
\overline{S_{f/g,Q}S_{h/k,Q}}=S_{fh/(gk),Q},\qquad
\overline{S_{f/g,Q}+S_{h/k,Q}}=S_{(fk+hg)/(gk),Q}.}
\tag{7.3}
$$

没有把未经闭包的自然乘积域称作已闭。非零分式的逆由翻转最大图直接给

$$
S_{f/g,Q}^{-1}=S_{g/f,Q}.
\tag{7.4}
$$

故 $\operatorname{Frac}\mathscr E_{>4}$ 在每个这样的 $Q$ 上有忠实最大闭分式场。

对整函数 $f$，$S_{f,Q}=P_Q^{-1}F_{f,Q}$，而

$$
S_{1,Q}=I_Q,\qquad
S_{z,Q}=C_Q^{-1}\text{，其域准确为 }\operatorname{Ran}C_Q,\qquad
S_{1/z,Q}=C_Q.
\tag{7.5}
$$

例如 $R_{1,Q}x=P_Qy=C_QR_{1,Q}y=R_{1,Q}C_Qy$，
由 $R_{1,Q}$ 单射得到 $x=C_Qy$，支付 (7.5) 的完整域。

若 $M\subset Q$ 闭且 $C_Q$ 不变，$x\in M\cap D(S_{f/g,Q})$，
则 $F_g S_{f/g,Q}x=F_fx\in M$。商 $Q/M$ 上的 $F_g$ 单射迫
$S_{f/g,Q}x\in M$；参数核心在 $M$ 内也完整成立。对旗再取商，原图像的闭包等于相应最大商图：它包含参数图，反包含来自有界核式 (6.1)。不声称未经闭包的商图已经闭。

对非零分式及其逆各用一次这种域内不变性，还得准确的循环空间等式

$$
[S_{f/g,Q}x]_{C_Q}=[x]_{C_Q}\qquad(x\in D(S_{f/g,Q})).
\tag{7.6}
$$

原整个 Haar 空间上，所有有界系数具有 R24 的同一 $J$ 对称性。参数算子
$S_0(F_gh)=F_fh$ 的双线性转置域准确由 $F_fx=F_gy$ 给出；
(6.3) 给 $\overline{S_0}=S_{f/g}$，故
$S_{f/g}^*=J S_{f/g}J$。对子商不额外断言它继承原 $J$。

## 8. 已付范围与真正未构造的根

本稿给的是具有 (1.4) 明确系数来源的场。临界四次系数并没有纳入：前稿证明每个固定 $x\ne0$ 都满足
$\log\|R_nx\|/n^4\to+\infty$。例如系数 $a_n=e^{-c n^4}$ 时，单项 $a_nR_nx$ 已不趋零，因此该同源级数甚至不能在该非零 $x$ 上范数收敛。这一结论只针对该固定分母的普通逐项范数求和，不涉及其他实际来源的临界构造。

本场也不能给原稳定平方根。若某个非零分式 $S=S_{f/g,Q}$ 满足
$D(S^2)=D(S)$ 且 $S^2x=C_Qx$ 于其稠密域，则自然平方的闭包为有界全域 $C_Q$。(7.3)、(7.5) 及忠实性迫

$$
\frac{f^2}{g^2}=\frac1z,\qquad zf(z)^2=g(z)^2.
\tag{8.1}
$$

在 $0$ 比较非零整函数的零点阶数，左侧奇、右侧偶，矛盾。等价地，不能从本稿的同源有界分子 $F_f,F_g$ 得到
$F_f^2=C(F_g)^2$ 的非零平方关系。

这只关闭本稿这一忠实快速整函数逆源族。它没有证明一般非零平坦分母或原全交换子不能有平方分子，也没有排除未知原旗上的非局部闭根。后续仍须构造本场之外的实际二次来源，或给出另一条原普通不变格的完整输入。
