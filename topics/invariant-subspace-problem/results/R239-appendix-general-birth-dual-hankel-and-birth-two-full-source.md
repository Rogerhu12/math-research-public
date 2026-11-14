# R239 附录：一般出生的互补Hankel范数及出生二的完整五维源归约

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文证明一般相对出生的完整强制根最小范数与实际有限计数测度之间的精确互补身份，保留同一源、完整层逆和两硬端。结合刚完成的两组加一位出生一全高度定理，整个物理出生二只剩一个明确的五维全逆后压缩二维块。本文尚未证明该新二维块的任意高度相邻序。独立核验：[完整强制根与五维全逆校准](../notes/2026-11-14-general-birth-dual-hankel-interface-check-0c.py)。

输入：[完整一般出生及单比特 MP](R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md)、[全部两权标量范数](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md)、以及[整个出生一全高度定理](R239-appendix-birth-one-two-group-singleton-all-heights-strict-bound.md)。下文的离散互补恒等式有自足有限维证明，不依赖未经证明的正矩阵推广。

## 1. 所有组内自旋分支及真实物理出生

先用 $Q_1,Q_2$ 表示两个物理等权组的大小，异常位仍为单个位。第一组的 Boolean Hilbert 空间分解为等权升降串：组内出生 $i$ 的串长为 $Q_1-2i$，重数为
$$d(Q_1,i)=\binom{Q_1}{i}-\binom{Q_1}{i-1},\qquad0\le i\le\lfloor Q_1/2\rfloor.$$
第二组同理。这里 $\binom Q{-1}=0$。这些是实际正交分解：每条串的标准归一基中，下降系数为 $a\sqrt{r(q-r+1)}$，与 $q$ 位等权对称串相同。组内 $D,D^*$ 同时约化每条串，故完整层 Gram、全逆及 primitive 压缩也同时约化相应张量块。

因此对物理出生 $s$，每对组内出生 $(i,j)$ 产生残余串长
$$q=Q_1-2i,\qquad L=Q_2-2j,\qquad t=s-i-j.$$
按需交换两串使 $q\le L$，并以长串权统一归一化。其真实高度为
$$h=q+L+1-2t=Q_1+Q_2+1-2s,$$
与组内分支无关。异常位仍保留为一条长度一的串。每个分支以重数 $d(Q_1,i)d(Q_2,j)$ 出现；不存在忽略的组内 primitive。

三串张量块的相对 primitive 维数为：$t=0$ 时一维；$1\le t\le q$ 时二维；若 $L\ge q+1$，$t=q+1$ 时一维；其余低半部出生为零。可由两串 Clebsch–Gordan 分解再张量长度一的串，或由相邻两个物理层的维数差直接得到。$q=0$ 退化为两权模型。

$t=0$ 是真实真空标量，严格 Newton 支付全部内部边；$t=1$ 的整个二维块由新出生一全高度定理支付。$t=q+1$ 的一维饱和分支仍用已有任意头饱和固定线及双侧常数，而不能误称两权模型。$q\le3$ 的全部相对出生此前也已经支付。

特别对物理 $s=2$：$i+j=2$ 给 $t=0$，$i+j=1$ 给 $t=1$，$i=j=0$ 给 $t=2$。因此全部新增费用准确集中在原两组都取对称串的唯一 $t=2$ 二维 primitive 块。若较小物理组不超过三，已有旧结论覆盖；真正新增范围可取 $q,L\ge4$，高度 $h=q+L-3\ge5$。

## 2. 共同原源及 $(2t+1)$ 维完整逆

以下固定一个二维分支 $1\le t\le q\le L$，短串和异常位权分别为 $a,c>0$，长串权为一，写 $z=a^2,w=c^2$。令
$$D=q-t+1,\qquad h=q+L+1-2t.$$
$D$ 在这里表示多项式次数；物理降算子写作 $\mathsf D$。

相对物理层 $p$ 的群固定坐标用 $(r,b,l)$ 标记，其中 $r$ 为短组占据、$b\in\{0,1\}$ 为异常位占据、$l=p-r-b$ 为池占据。每个坐标表示该类全部具体子集上的共同振幅；其 Hilbert 平方范数权是 $\binom qr\binom Ll$。在出生层 $p=t$，共有 $2t+1$ 个坐标，尤其 $t=2$ 时为五维。

同一个首一源 $E_w(\alpha,\beta)$ 的两个列向量逐坐标为
$$\begin{aligned}
(E_w)_{(r,b,l),1}&=(-1)^l a^{q-r}c^{1-b}
 \frac{D!\binom{q-r}{D}}{\binom Ll},\\
(E_w)_{(r,b,l),2}&=(-1)^l a^{q-r}c^{1-b}
 \frac{(D-1)!(1-b)\binom{q-r}{D-1}}{\binom Ll}.
\end{aligned}\tag{2.1}$$
只在合法坐标上使用。完整源公式或直接下降相消给 $\mathsf DE_w=0$；两列独立并穷尽该二维 primitive。该 $E_w$ 与所有高度共用。

从层 $t+n$ 到层 $t$ 的 $\mathsf D^n/n!$ 矩阵记为 $A_n$。若输入 $v$、输出 $o$ 的三占据差为 $d_r,d_b,d_l\ge0$ 且和为 $n$，则
$$ (A_n)_{o,v}=a^{d_r}c^{d_b}
 \binom{q-o_r}{d_r}\binom{1-o_b}{d_b}\binom{L-o_l}{d_l};\tag{2.2}$$
否则为零。令 $W_n^{-1}$ 是输入层对角矩阵，其对角为 $1/(\binom qr\binom Ll)$。真正全 MP 形式准确是
$$\boxed{H_n=E_w^*(A_nW_n^{-1}A_n^*)^{-1}E_w,\qquad0\le n\le h.}\tag{2.3}$$
先取完整 $(2t+1)\times(2t+1)$ 逆，再压缩；最高阶也保留。$H_0=E_w^*W_0E_w$ 为真实源 Gram。这是有权 Hilbert 最小逆的标准约束最小化身份，原矩阵全行满秩由已证实际完整 MP 给出。

上述完整源和后文互补公式还适用于没有长度次序的 $1\le t\le\min(q,L)$。将普通短组与异常位一起视为 $Q=q+1$ 个头，原源缺失次数为 $D=q-t+1$；[任意短池的完整源条件](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md) §11.1 只要求 $f(R)=0$ 当 $|R|>L+D$。这里 $t\le L$ 给 $L+D\ge q+1=Q$，故该额外条件为空，两个最高系数仍独立。出生层的 $2t+1$ 个坐标、全部合法支撑与硬端点数也不变，完整 MP 仍按同一短池定理取全逆。因此下文的 $q\le L$ 仅是最初分支整理时的方便约定，不限制这些公式；独立校准另外包含 $q=5,L=4$。

## 3. 实际计数测度与全部 Hankel 行列式

对普通两组定义真正有限非中心超几何权
$$\nu_k(i)=\binom qi\binom L{k-i}z^i,\qquad0\le i\le q,$$
越界二项式为零。只在正权支撑上取内积。记
$$m_r(k)=\sum_i i^r\nu_k(i),\qquad
\Delta_\ell(k)=\det[m_{a+b}(k)]_{a,b=0}^{\ell-1},\quad\Delta_0=1.$$
若支撑点数为 $d_k$，则 $\Delta_\ell>0$ 对 $0\le\ell\le d_k$ 成立，$\Delta_{d_k+1}=0$。这是有限 Vandermonde 平方展开
$$\Delta_\ell(k)=\sum_{i_1<\cdots<i_\ell}
 \prod_{a<b}(i_b-i_a)^2\prod_{a=1}^{\ell}\nu_k(i_a)\tag{3.1}$$
的直接结果。对应首一 $\ell$ 次多项式的最小平方范数为
$$\mathfrak h_\ell(k)=\Delta_{\ell+1}(k)/\Delta_\ell(k).$$
边界 $\ell=d_k$ 时它是支撑点乘积多项式，范数为零；此时不将其倒数当作有限 Gram。

对原高次通道位置 $j$，令
$$k=j+t-1,\qquad C_q=(q!)^2z^q.$$
这里 $0\le j\le h+1$，所以 $t-1\le k\le q+L-t+1$，支撑点数至少为 $t$。在严格内部 $1\le j\le h$，支撑点数至少为 $t+1$。

## 4. 带全部强制根的互补范数定理

原首一最小化的权是
$$\omega_j(r)=\frac{\binom qr z^r}{\binom L{j+r-D}}$$
且只在合法池占据上使用。每个非法 $r\in\{0,\ldots,q\}$ 都必须为多项式的真实根。令 $a_j$ 为首一 $D$ 次最小范数，$b_{j-1}$ 为同权下首一 $D-1$ 次最小范数。则
$$\boxed{a_j=C_q\frac{\Delta_{t-1}(j+t-1)}{\Delta_t(j+t-1)},
\quad0\le j\le h+1,}\tag{4.1}$$
$$\boxed{b_{j-1}=C_q\frac{\Delta_t(j+t-1)}{\Delta_{t+1}(j+t-1)},
\quad1\le j\le h.}\tag{4.2}$$

**自足证明。** 在完整网格 $0,\ldots,q$，记
$$V(x)=\prod_{r=0}^q(x-r),\qquad
\lambda_r=1/V'(r)=\frac{(-1)^{q-r}}{r!(q-r)!}.$$
任何给定的合法值与非法零值有唯一次数至多 $q$ 的插值多项式。设 $s=q-D=t-1$。该插值多项式次数至多 $D$ 且首一，当且仅当
$$\sum_r\lambda_r r^kF(r)=0\ (0\le k<s),\qquad
\sum_r\lambda_r r^sF(r)=1.\tag{4.3}$$
这是 Lagrange 最高系数身份的三角消元：第一个等式消去 $x^q$，以后逐次消去下一最高项，最后固定 $x^D$ 系数。非法值已经准确设零，故没有把非法权放入和式。

以完整合法值作为自由变量，对 (4.3) 的全部约束做加权二次最小化。其约束 Gram 是矩矩阵
$$G_{kl}=\sum_{r\ {\mathrm{legal}}}\frac{\lambda_r^2}{\omega_j(r)}r^{k+l},\qquad0\le k,l\le s.$$
因为支撑点数至少 $s+1$，它严格正。最小范数为 $(G^{-1})_{ss}$；对低次矩作 Schur 补，此值准确为互补权 $\lambda_r^2/\omega_j(r)$ 的首一 $s$ 次范数之倒数。

现在换元 $i=q-r$。直接二项式计算给
$$\frac{\lambda_r^2}{\omega_j(r)}
=\frac1{C_q}\binom qi\binom L{j+t-1-i}z^i
=\frac{\nu_{j+t-1}(i)}{C_q}.\tag{4.4}$$
反射 $r=q-i$ 对首一最高项只带符号 $(-1)^s$，不改变平方最小范数。于是原最小值为 $C_q/\mathfrak h_{t-1}$，即 (4.1)。把原次数减一，互补次数增加一，得到 (4.2)。这使用整个原合法值空间及全部最高系数约束，是精确最小值而非试探上界。证毕。

$j=0,h+1$ 的合法支撑点数恰为 $t$。高次问题仍由 (4.1) 给严格正范数，次低次数问题却已没有首一可行向量。对应 $\Delta_{t+1}=0$；后文直接保留硬端约束，不把无穷数作为矩阵。

## 5. 次首系数与同一源的完整二维形式

若原高次最小多项式写为 $P_j(r)=r^D+c_jr^{D-1}+\cdots$，则全端点准确有
$$\boxed{c_j=-\frac{q(q+1)}2+tq-\Theta\log\Delta_t(j+t-1),
\qquad\Theta=z\partial_z.}\tag{5.1}$$

证明同样从 (4.3) 的完整最小解得出。以互补权 $\lambda_r^2/\omega_j(r)$ 定义的首一 $s=t-1$ 次正交多项式记为 $\pi_s(r)$，其范数记为 $\widehat{\mathfrak h}_s$；注意 $\widehat{\mathfrak h}_s=\mathfrak h_s(\nu_k)/C_q$。最小值向量为 $F(r)=\lambda_r\pi_s(r)/(\omega_j(r)\widehat{\mathfrak h}_s)$。Lagrange 身份应用于 $r^{s+1}P_j$，因其次数为 $q+1$，给
$$\sum_r\lambda_r r^{s+1}P_j(r)=c_j+\sum_{r=0}^q r.$$
另一方面，正交展开使左边等于互补首一 $t$ 次多项式次首系数的负值。反射 $r=q-i$ 把它变为 $tq$ 加上 $\nu_k$ 的首一 $t$ 次次首系数。由 (3.1) 的 Vandermonde 展开，这个次首系数正是 $-\Theta\log\Delta_t(k)$：它是 $t$ 个粒子坐标和的负期望。该论证在支撑恰为 $t$ 个点时仍成立，此时首一 $t$ 次多项式为全部支撑点之积。得到 (5.1)。

所以原 shear 为
$$k_n=c_{n+1}-c_n=-\Theta\log\frac{\Delta_t(n+t)}{\Delta_t(n+t-1)}.\tag{5.2}$$
配合 (4.1)–(4.2)，完整式 (2.3) 准确等于
$$\boxed{H_n=\begin{pmatrix}A_n+B_nk_n^2&-B_nk_n\\-B_nk_n&B_n\end{pmatrix},}\tag{5.3}$$
$$A_n=a_n+wa_{n+1},\qquad
B_n=\frac{wb_{n-1}b_n}{b_{n-1}+wb_n}\quad(1\le n<h),$$
$$\boxed{B_0=wb_0,\qquad B_h=b_{h-1}.}\tag{5.4}$$
这只是将已证完整两通道 MP 的原标量范数换成精确互补行列式；源 $E_w$ 从未改变。$n=0$ 时第零通道没有次低自由度，$n=h$ 时第一通道没有次低自由度，故 (5.4) 是真实硬端最小化。

标准有限 Hankel–Jacobi 身份还给
$$\Theta^2\log\Delta_t(k)=\frac{\Delta_{t-1}(k)\Delta_{t+1}(k)}{\Delta_t(k)^2}
=\frac{a_j}{b_{j-1}}\quad(k=j+t-1).\tag{5.5}$$
为自足证明 (5.5)，对权 $\nu_k(i)$ 的首一正交多项式 $p_j(i)$ 记范数 $h_j$。权的 $\Theta$ 导数为 $i\nu_k(i)$，且 $\Theta p_j$ 次数小于 $j$。对 $\langle p_j,p_l\rangle=0$ 求导：当 $l\le j-2$ 时 $ip_l$ 的次数不超过 $j-1$，所以对应系数为零；当 $l=j-1$ 时 $\langle p_j,ip_{j-1}\rangle=h_j$。因此
$$
\Theta p_j=-\frac{h_j}{h_{j-1}}p_{j-1}.
$$
取 $j=t$ 的次首系数并用它等于 $-\Theta\log\Delta_t$，即得 (5.5)。支撑恰有 $t$ 个点时 $p_t$ 是固定的支撑乘积，$h_t=0$，等式仍成立。

这是粒子坐标的矩行列式，不是声称高度序列 $H_n$ 的全 Hankel 正性。

## 6. 出生二的具体方差与二次残差

现在 $t=2$。令 $Z_k=\Delta_1(k)=\sum_i\nu_k(i)$；对概率 $\nu_k/Z_k$ 记均值 $m_k$、中心矩 $v_k=\mathbb E(i-m_k)^2$、$\mu_{3,k}$、$\mu_{4,k}$。直接中心化矩矩阵给
$$\Delta_2(k)=Z_k^2v_k,$$
$$\Delta_3(k)=Z_k^3\{v_k\mu_{4,k}-\mu_{3,k}^2-v_k^3\}.$$
置
$$W_k=\mu_{4,k}-v_k^2-\mu_{3,k}^2/v_k.$$
这是把 $(i-m_k)^2$ 对常数及 $(i-m_k)$ 正交消去后的真实平方范数。内部支撑至少三点，所以 $W_k>0$；两端支撑两点时 $W_k=0$。

新块的全部高、低原范数为
$$\boxed{a_j=\frac{C_q}{Z_{j+1}v_{j+1}},\qquad
b_{j-1}=\frac{C_q}{Z_{j+1}W_{j+1}}.}\tag{6.1}$$
第二式仅在 $1\le j\le h$ 使用；$c_j$ 及 shear 由 (5.1)–(5.2) 的 $\Delta_2$ 给出。因此在完整五维逆之后，二维差的全部四次项都成为同一实际 $Z_k$、方差和二次残差的有理式。旧两权全高度定理仍支付两条标量范数的严格 log 凸性；不能由这两条标量输入直接删除 shear。

## 7. 不能搬用出生一负实根相位的实际障碍

即使真实乘积权也有下列最小明确例。取 $q=L=4,t=2$，在 $j=1$ 对应 $k=2$。实际计数权为
$$\nu_2=(6,16z,6z^2),$$
所以
$$\boxed{\Delta_2(2)=48z(2+3z+2z^2).}\tag{7.1}$$
二次因子的判别式为 $9-16=-7<0$，故去掉强制单项式后仍有非实根。这是完整实际参数族；不是任意化底测度造成的伪反例。

(7.1) 仅排除把出生一 $Z_k$ 的全负实根表示原样套到 $\Delta_2$。它不是矩阵相邻比较的反例。所有 $\Delta_t$ 仍有 (3.1) 的正有限粒子展开，但粒子和的生成多项式一般并非实根。

独立程序从带全部强制根的原首一最小化分别核 (4.1)、(4.2)、(5.1)，并对 $q=L=4$ 及 $q=4,L=5$ 的 $t=2$、两组有理权、全部高度，用 (2.1)–(2.3) 先取完整五维逆，再与 (5.3)–(6.1) 比较。共 411 项原强制根范数/次首系数身份、40 项完整五维逆身份及 (7.1) 的非实根身份全部通过。其意义是独立校准原源与端点；一般恒等式已由 §§4–5 证明。

下一实际目标是这个 $t=2$ 块的完整相邻四次式。物理出生二其余全部组内分量已经由 §1 归约支付；没有把五维原逆缩成错误的二维原 Gram，也不因正矩行列式就宣布剩余比较成立。
