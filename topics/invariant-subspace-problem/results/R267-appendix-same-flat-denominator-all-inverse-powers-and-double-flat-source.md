# R267 附录：同一平坦分母的全部逆幂、双平坦强乘积与真实二次来源

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整原来源构造。** 本稿从已经固定的定量正锥分母 $P$ 出发，构造一个新的非零正锥收缩 $Q$。同一个 $Q$ 同时属于全部 $\operatorname{Ran}(C^aP^b)$，全部唯一逆 $C^{-a}P^{-b}Q$ 都是有界原交换子；$Q$ 与这些逆保同一个收缩强*单位，并在全部原有限放大旗商上单射稠值。这些结论不是从全空间非零或稠值推给未知旗。

该构造首次进入 $P$ 的负幂来源。它给严格的新共同倍数理想 $\mathfrak F_P\subsetneq\mathfrak F_C$ 和带实际预算的双逆级数。没有证明 $Q$ 不属于此前联合闭场，也不宣称新双逆级数的每个非零形式都忠实；最后保留了需要真实解决的同 $Q$ 二次式。

## 1. 固定旧 $P$，构造更明确的正强单位

固定原 Haar 尾 $C=A^{(m_0)}$，完全沿用
[定量正锥稿](R267-appendix-quantitative-positive-common-denominator-and-strict-superquartic-inverse-cost.md)
的

$$
P=\prod_{\nu\ge1}T_\nu^+,\quad
q_\nu=256\nu^2,\quad
m_\nu=1+256\sum_{i<\nu}i^2,\quad
b_\nu=m_\nu+q_\nu-1,
$$

$$
T_\nu^+=C^{2^{m_\nu}}U_\nu(C),\qquad
k_n=\sum_{\nu\le n}2^{m_\nu},\qquad
P=C^{k_n}U^{[n]}\Theta_n,\quad
U^{[n]}=\prod_{\nu\le n}U_\nu(C).
\tag{1.1}
$$

这里 $\Theta_n$ 是旧 $P$ 的真实正锥收缩尾积，
$\Theta_n\to I$ 强*；每个 $U_\nu(C)$ 是原多项式代数中的有界单位。
另记 $R_a=C^{-a}P$，已付同一 $R_a$ 的全尺度预算。

先给一个尾真空误差。旧纯尾列的均值为
$\prod_{\nu>n}q_\nu/(q_\nu+2)$，范数不超过一，故

$$
\|\Theta_n^Y\Omega-\Omega\|^2
\le4\sum_{\nu>n}q_\nu^{-1}\le\frac1{64n}.
$$

真实正尾与纯旧尾的范数差不超过
$12e^{-770\,16^{m_{n+1}}}<1/(8\sqrt n)$，于是

$$
\boxed{\|\Theta_n\Omega-\Omega\|\le\frac1{4\sqrt n}.}
\tag{1.2}
$$

对任意整数 $L\ge0,q\ge1$，定义真实有限多项式

$$
E_{L,q}=\frac2{q+2}\sum_{j=L}^{L+q-1}N_j,\qquad
N_j=C^{2^j}/d_j,\quad d_j=\|C^{2^j}\|.
\tag{1.3}
$$

原 $\|N_j-E_j\|\le\eta_j$ 和纯局部下降范数给
$\|E_{L,q}\|<1$。它保持函数正锥，最低次数是 $2^L$。
纯真空误差平方为 $(q+4)/(q+2)^2\le1/q$，全部实际 carry 差不超过
$4e^{-770\,16^L}/(q+2)$，所以

$$
\|E_{L,q}\Omega-\Omega\|\le2/\sqrt q.
\tag{1.4}
$$

取 $L_n=m_n+1$。由 $k_n<2^{m_n+1}$，可以准确写

$$
E_{L_n,64n}=C^{k_n}B_n(C),\qquad
W_n=(U^{[n]})^{-1}B_n(C)\in\mathcal A,
$$

$$
\boxed{V_n:=PW_n=\Theta_n E_{L_n,64n},\qquad
\|V_n\|\le1,\quad V_n\ge_{\rm cone}0,\quad
\|V_n\Omega-\Omega\|\le\frac1{2\sqrt n}.}
\tag{1.5}
$$

特别 $V_n\to I$ 强*。为后面的有限测试记录原来源：由 R88 的准确 Cayley 列，
$\chi_J=\prod_{j\in J}(I-N_j)(I+N_j)^{-1}\Omega$，
且该乘子的范数至多 $6^{|J|}$，故

$$
\|(V_n-I)\chi_J\|\le\frac{6^{|J|}}{2\sqrt n}.
\tag{1.6}
$$

收缩给
$\|(V_n^*-I)\xi\|^2\le2\|\xi\|\,\|(V_n-I)\xi\|$。
因此强*结论使用了原稠密柱基和统一收缩界，不只是真空列。

每个右因子还有有限的准确分解

$$
\boxed{W_n=C^{h_n}g_n(C),\quad
h_n=2^{m_n+1}-k_n\ge0,\quad g_n(C)\text{ 是 }\mathcal A\text{ 中单位}.}
\tag{1.7}
$$

这是非零多项式 $B_n$ 的最低次数与 $U^{[n]}(0)\ne0$ 的直接结果。
后面正是用 (1.7) 构造新 $Q$ 的全旗强单位；不能省掉它。

## 2. 明确子列的非零强*乘积及全部尾积

固定

$$
n_\nu=2^{32+10\nu}\quad(\nu\ge1),\qquad
\mathcal P_r=\prod_{\nu=1}^rV_{n_\nu}.
\tag{2.1}
$$

对 $J\subset[0,\nu)$，(1.6) 及 $6^\nu\le2^{3\nu}$ 给

$$
\|(V_{n_\nu}-I)\chi_J\|\le2^{-17-2\nu},
\qquad
\|(V_{n_\nu}^*-I)\chi_J\|\le2^{-8-\nu}.
\tag{2.2}
$$

所有 $V_n$ 互相交换且为收缩；其伴随也彼此交换。
对固定有限 $J$，乘积望远镜与 (2.2) 使
$\mathcal P_r\chi_J$ 及 $\mathcal P_r^*\chi_J$ 均 Cauchy。
先对柱基，再用统一范数界，得到

$$
\boxed{Q=\operatorname*{SOT^*\!-\!lim}_{r\to\infty}\mathcal P_r,\qquad
\|Q\|\le1,\quad Q\ge_{\rm cone}0,\quad
\|Q\Omega-\Omega\|\le1/256.}
\tag{2.3}
$$

因此 $Q\ne0$。从任意固定 $r+1$ 开始的同一论证给真实尾积

$$
\Psi_r=\prod_{\nu>r}V_{n_\nu},\qquad
Q=\mathcal P_r\Psi_r,\quad
\|\Psi_r\|\le1,\quad \Psi_r\ge_{\rm cone}0,\quad
\Psi_r\to I\ \text{强*}.
\tag{2.4}
$$

$Q,\Psi_r$ 都是原 $C'$ 中的有界算子，因为各有限积属于该强闭代数。
没有把乘积的非零强极限当作可逆，亦不由此直接断言它在未知旗上非零。

## 3. 同一 $Q$ 的实际全旗强单位

置

$$
H_r=\sum_{\nu\le r}h_{n_\nu},\qquad
G_r=\prod_{\nu\le r}g_{n_\nu}(C).
$$

$G_r$ 是 $\mathcal A$ 中的有界单位，(1.7) 给

$$
Q=P^r C^{H_r}G_r\Psi_r.
\tag{3.1}
$$

选 $k_r'=2^{10r+20}$，则对 $J\subset[0,r)$，

$$
\|(V_{k_r'}^r-I)\chi_J\|
\le r\,6^r/(2\sqrt{k_r'})\le2^{-r-11}.
$$

再选
$L_r'=\lceil\log_2(H_r+1)\rceil$、
$q_r'=2^{8r+20}$，令

$$
E_r'=E_{L_r',q_r'}=C^{H_r}B_r'(C).
$$

由 (1.4) 与同一 Cayley 列，
$\|(E_r'-I)\chi_J\|\le2^{-r-9}$ 对上述 $J$ 成立。
准确定义

$$
Z_r=G_r^{-1}W_{k_r'}^{\,r}B_r'(C)\in\mathcal A.
$$

所有因子互相交换，所以

$$
\boxed{K_r:=QZ_r
=\Psi_r V_{k_r'}^{\,r}E_r',\qquad
\|K_r\|\le1,\quad K_r\ge_{\rm cone}0,\quad
K_r\to I\ \text{强*}.}
\tag{3.2}
$$

右侧三个实际收缩给范数界；柱测试与 (2.4) 给强极限，收缩再给伴随强极限。
$Z_r$ 本身不被断言保持正锥。

所有 $Q,Z_r$ 保持全部有限放大原闭不变旗；故 (3.2) 下降到每个实际非零旗商。若该商上 $Qx=0$，交换性使 $K_rx=0$ 对全部 $r$ 成立，强单位迫 $x=0$；其值域闭包又包含 $K_r$ 的像。因此

$$
\boxed{Q_{\mathcal Q}\text{ 在每个原非零有限放大旗商 }\mathcal Q
\text{ 上单射、稠密值域}.}
\tag{3.3}
$$

这里 $\mathcal Q$ 表示子商，避免与算子 $Q$ 混淆。
这一步明确支付了全旗来源，所用不是环境空间非零性。

## 4. 全部混合逆的唯一原式、兼容性与有限预算

对任意整数 $a,b\ge0$，定义

$$
\boxed{
Q_{a,b}
=R_a\left(\prod_{\nu=1}^{b+1}W_{n_\nu}\right)\Psi_{b+1}.
}
\tag{4.1}
$$

由 $C^aR_a=P$ 及真实有限前缀，

$$
\boxed{C^aP^bQ_{a,b}=Q,\qquad Q_{a,b}=C^{-a}P^{-b}Q\in C'.}
\tag{4.2}
$$

$C,P$ 都单射，所以 (4.1) 是唯一实际逆，且任何使用更长前缀的式子都给同一算子。特别

$$
Q_{0,0}=Q,\quad CQ_{a+1,b}=Q_{a,b},\quad
PQ_{a,b+1}=Q_{a,b},\quad
Q_{a,b}Q_{c,d}=Q Q_{a+c,b+d}.
\tag{4.3}
$$

每个等式可乘回同一个单射 $C$、$P$ 幂后检验，未作域外形式取消。
同一个强单位还写为

$$
Q_{a,b}(C^aP^bZ_r)=K_r.
\tag{4.4}
$$

故全部 $Q_{a,b}$ 在每个实际旗商上也单射稠值。
不声称 $b>0$ 时这些逆保持函数正锥。

为给级数实际预算，置

$$
\mathscr R_C(t)=\sum_{\ell\ge0}t^\ell\|C^\ell\|<\infty\qquad(t\ge0).
$$

这是原 $C$ 的整预解范数和，$\|C^\ell\|$ 由原权乘积准确给出。
$U_\nu(0)=2/((q_\nu+2)d_{m_\nu})$。
取
$\delta_\nu=d_{b_\nu}/(2q_\nu d_{m_\nu})$，
则在 $|z|\le\delta_\nu$ 上，
$|U_\nu(z)/U_\nu(0)-1|\le1/2$。
Cauchy 系数界和原幂范数因此给

$$
\|U_\nu(C)^{-1}\|
\le(q_\nu+2)d_{m_\nu}
\mathscr R_C(2q_\nu d_{m_\nu}/d_{b_\nu}).
$$

同时 $\|B_n(C)\|\le2/d_{L_n+64n-1}$，故以下完全由旧原权决定的有限数是合法上界：

$$
\omega_n=
\max\!\left(1,\
\frac2{d_{L_n+64n-1}}
\prod_{\nu=1}^n
(q_\nu+2)d_{m_\nu}
\mathscr R_C(2q_\nu d_{m_\nu}/d_{b_\nu})
\right)\ge\|W_n\|.
\tag{4.5}
$$

令 $M_b=\prod_{\nu=1}^{b+1}\omega_{n_\nu}$，
$A_0=1$，对 $a\ge1$ 取定量稿的

$$
A_a=\exp\!\left(K_{m_0}a^4
e^{300[\log(2+a)]^{2/3}}\right).
$$

则同一来源满足

$$
\boxed{\|Q_{a,b}\|\le A_a M_b.}
\tag{4.6}
$$

这些预算很大，但每项有限、定义明确，且作用于同一个 $Q$；
没有借未知旗上的真空下界。上界当然下降到全部原旗商。

## 5. 一个严格更深的共同倍数理想与闭域核心

定义

$$
\mathfrak F_P=\bigcap_{r\ge1}P^rC',\qquad
\mathfrak F_C=\bigcap_{a\ge1}C^aC'.
$$

(4.2) 证明 $Q\in\mathfrak F_P$，所以该理想非零。
由 $P\in\mathfrak F_C$ 有 $\mathfrak F_P\subseteq\mathfrak F_C$。
但 $P\notin P^2C'$：否则 $P=P^2B$；取消单射 $P$ 后得到 $I=PB$。
又 $B\in C'$ 与 $P$ 交换，故 $BP=PB=I$，使 $P$ 成为有界可逆元，
与其谱半径为零矛盾。因此

$$
\boxed{0\ne\mathfrak F_P\subsetneq\mathfrak F_C.}
\tag{5.1}
$$

同一 $K_r$ 给 $\mathfrak F_P$ 单位球在 $C'$ 单位球中强*稠密：
对 $F\in C'$，$K_rF\in\mathfrak F_P$、
$\|K_rF\|\le\|F\|$ 且 $K_rF\to F$ 强*。
由唯一逆取消还得

$$
P\mathfrak F_P=\mathfrak F_P,\qquad C\mathfrak F_P=\mathfrak F_P.
\tag{5.2}
$$

第二式的反向：若 $F=P^{r+1}B_{r+1}$，则同一个 $C^{-1}F$ 等于
$R_1P^rB_{r+1}$，从而属于每个 $P^rC'$。
这是原 $C$ 与原 $P$ 的共同内部整除。

另由同 $P$ 的新幂定理，对每个固定 $r$，

$$
\|Q^n\|\le\|P^{rn}\|\|Q_{0,r}\|^n,
$$

故

$$
\boxed{\lim_{n\to\infty}
\frac{\log(-\log\|Q^n\|)}{n^{3/2}}=+\infty.}
\tag{5.3}
$$

$Q$ 单射保证各幂非零；范数最终小于一由上述界保证。
先固定 $r$ 应用 $P$ 的确切常数 $(\log16)/48$，
再令 $r\to\infty$，得到完整极限。没有断言一个与之匹配的统一上界。

若 $\mathcal D$ 是一个或有限多个真实闭 $C$-交换算子的共同图域，
R88 的有界强多项式逼近保证全部 $C'$ 保持 $\mathcal D$ 并交换。
由 (3.2)，$Q\mathcal D$ 是 $\mathcal D$ 的共同图核心，并且

$$
Q\mathcal D\subseteq\bigcap_{a,b\ge0}C^aP^b\mathcal D.
\tag{5.4}
$$

(4.1) 给域内的同一实际原像。
仍不能由 (5.4) 推 $QH\subseteq\mathcal D$；
这没有绕过旧全交换子无普遍正则器的反例。

## 6. 带同一来源的双逆级数及准确二次方程

现在变量 $z,w$ 分别表示 $C^{-1},P^{-1}$，与前稿的正 $P$ 变量不同。
取单调权

$$
\Lambda_n=\max\!\left(e^{n^2},
\max_{a+b\le n}A_aM_b\right)\ge1.
$$

令 $\mathscr D$ 由系数满足下式的双整函数组成：

$$
F(z,w)=\sum_{a,b\ge0}c_{a,b}z^aw^b,\qquad
p_k(F):=\sum_{a,b}|c_{a,b}|
\Lambda_{2^k(a+b)}<\infty\quad(k=0,1,\ldots).
\tag{6.1}
$$

此类包含所有多项式和真正无限级数，例如
$\sum_{n\ge1}2^{-n}\Lambda_{2^nn}^{-1}w^n$ 满足每个 $p_k$ 预算。
它是代数：
对非负整数 $s,t$，

$$
\Lambda_{2^k(s+t)}
\le\Lambda_{2^{k+1}s}\Lambda_{2^{k+1}t},
$$

所以卷积满足 $p_k(FG)\le p_{k+1}(F)p_{k+1}(G)$。
因 $\Lambda_n\ge e^{n^2}$，这些级数确在 $\mathbb C^2$ 上整。
乘 $z$、$w$ 也保持此类：对总次数至少一的项用
$2^k(n+1)\le2^{k+1}n$，常数项单独处理。

定义全域有界原分子

$$
\boxed{\mathcal B_F=\sum_{a,b\ge0}c_{a,b}Q_{a,b}.}
\tag{6.2}
$$

由 (4.6) 范数绝对收敛。
(4.3) 及上述完整卷积预算给

$$
\mathcal B_F\mathcal B_G=Q\mathcal B_{FG},\qquad
C\mathcal B_{zF}=\mathcal B_F,\qquad
P\mathcal B_{wF}=\mathcal B_F,\qquad
\mathcal B_1=Q.
\tag{6.3}
$$

这里不自动宣称 $F\ne0$ 便有 $\mathcal B_F\ne0$，
也不自动给所有非零分子的全旗单射性。
此前正 $P$ 解析芽的最低次数证明不适用于本稿的整个负 $P$ 级数。

但是一个真实平方来源已被写成同一实际预算中的精确目标：
对 $F\in\mathscr D$、$Y=\mathcal B_F$，由 $C,Q$ 单射和 (6.3)，

$$
\boxed{Y^2=CQ^2
\quad\Longleftrightarrow\quad
\mathcal B_{\,zF^2-1}=0.}
\tag{6.4}
$$

如果找到这样的 $F$，右侧已保证 $Y\ne0$，
且 $Q^{-1}Y$ 的最大图由[同分母闭根定理](R12-appendix-same-flat-denominator-maximal-stable-root-and-all-flag-cores.md)
给真实稳定闭根；(3.2) 支付其原参数核心。
本稿尚未找到满足 (6.4) 的 $F$，也未证明不存在。

与此前区别是：现在 $QH$ 确实位于每个实际 $P^{-b}$ 的域，
有 (4.1)、(4.6) 的同来源有界原像，二次卷积也在同一预算中合法。
没有将这些负幂仅写成形式分式，没有把共同整数逆直接称作平方根，
亦没有宣称这一特定来源类穷尽所有可能闭根。普通 ISP 继续开放。
