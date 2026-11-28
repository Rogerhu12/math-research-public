# R267 后续：同一实际范数稠密分母中的加权平方曲线

日期：2026-11-29（Asia/Taipei）。作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。

本稿更换原全因子构造的实际有限块，保留原 Haar 算子、完整 carry 和同一二次目标。新块在指定 $L$ 后具有可和的算子范数误差，所以其固定平坦分母与全部非零参数平方分子真正落进同一个已付范数稠密主理想类。它不沿用旧等权块的范数来源，也没有证明平方分子的一致范数或单列强紧性。

## 1. 只含偶次幂的实际加权块

固定原尾 $C=A^{(m_0)}$、$c=\|C\|$、$\mathscr A=C'$，并使用同一
$$
N_j=C^{2^j}/\|C^{2^j}\|,\quad
a_j=(j+1)^{-1},\quad
Z=I+\sum_{j\ge0}a_j(I-N_j)(I+N_j)^{-1},\quad L=Z^{-1}.
$$
令 $\mathscr B=\overline{L\mathscr A}^{\,\|\cdot\|}$，采用[实际范数理想稿](R12-appendix-actual-norm-ideal-full-multipliers-quasimultipliers-and-common-inverse-core.md)的 $\Omega(\mathscr B)$。

对 $N\ge2$，只在 $1\le j<N$ 求和，记
$$
s_N=\sum_{1\le j<N}a_j,\quad
g_N^2=\sum_{1\le j<N}a_j^2,\quad
e_N=\sum_{1\le j<N}a_j\eta_j,\quad
\kappa_N=\sqrt{s_N^2+4g_N^2}+2e_N,
$$
$$
F^{\mathrm e}_N=\frac2{\kappa_N}\sum_{j=1}^{N-1}a_jN_j.
\tag{1}
$$
[共同幂范数逼近稿](R12-appendix-accretive-sources-norm-approximated-by-common-power-quasiaffinities.md)的加权 Pauli 与完整 Cayley 证明逐项适用这个删去单个首项的和：它仍为收缩，并且
$$
\delta_N^2:=\|(I-F_N^{\mathrm e})L\|^2
\le\frac2{\kappa_N}
\left[(\kappa_N-s_N+6e_N)\|L\|^2+\|L\|\right]
\longrightarrow0.
\tag{2}
$$
因为有限和 $\sum_{j=1}^{N-1}a_j\Re V_j$ 仍不超过完整原 $Z$ 的实部形式，(2) 没有改变原来源域。

每个 $F_N^{\mathrm e}$ 是保函数正锥的原多项式，只含偶次 $C$；其最低次为 $C^2$，准确写成
$$
F_N^{\mathrm e}=C^2G_N(C),\qquad G_N(0)>0,
\tag{3}
$$
其中 $G_N(C)$ 是原范数多项式代数中的有界单位。$F_N^{\mathrm e}$ 本身不是单位。由 (2) 和 $\operatorname{Ran}L$ 稠密，它强*趋于 $I$。

## 2. 一次固定选择与完整尾范数费用

置
$$
M_\nu=(\nu+1)!,\qquad d_\nu=M_{\nu+1}-M_\nu.
$$
选严格递增的 $N_\nu$ 和正数 $\zeta_\nu$，使
$$
F_\nu=F^{\mathrm e}_{N_\nu},\qquad
\|(I-F_\nu)L\|\le\frac{2^{-\nu-8}}{1+d_\nu},\qquad
0<\zeta_\nu\le\frac{2^{-\nu-8}}{1+d_\nu}.
\tag{4}
$$
这是由 (2) 支付的原选择，无需另加执行或有限数值筛选。

定义
$$
Z_\nu(z)=(1-\zeta_\nu)F_\nu+z\zeta_\nu C/c.
\tag{5}
$$
对 $|z|\le R$，
$$
\|Z_\nu(z)\|\le1+R\zeta_\nu,\qquad
\|(I-Z_\nu(z))L\|\le\delta_{N_\nu}+(1+R)\zeta_\nu.
\tag{6}
$$
对 $\nu\ge1$ 令 $p_\nu=d_\nu/2$；这些都是正整数。置
$$
K_N=\sum_{\nu\ge N}p_\nu\zeta_\nu,\qquad
H_N(R)=\sum_{\nu\ge N}p_\nu
\bigl(\delta_{N_\nu}+(1+R)\zeta_\nu\bigr)\quad(N\ge1).
$$
两个尾和都趋零。完整有限乘积的同源望远镜给
$$
\left\|\left(\prod_{\nu=N}^{M-1}Z_\nu(z)^{p_\nu}-I\right)L\right\|
\le e^{RK_N}H_N(R).
\tag{7}
$$
同一估计对任意两截断的差应用，支付强*尾极限
$$
T_N(z)=\mathrm{strong*}\!-\!\lim_{M\to\infty}
\prod_{\nu=N}^{M-1}Z_\nu(z)^{p_\nu},
$$
$$
\boxed{\|T_N(z)\|\le e^{RK_N},\qquad
\|(T_N(z)-I)L\|\le e^{RK_N}H_N(R).}
\tag{8}
$$
这些估计在 $|z|\le R$ 一致。强收敛由稠密的 $\operatorname{Ran}L$ 延拓；对伴随使用全部因子与 $L$ 的交换及稠密的 $\operatorname{Ran}L^*$，没有把强极限自动改成强*。

记 $T(z)=T_1(z)$。有限乘积整个，紧参数逐向量一致收敛与局部一致范数界给 $T$ 为 $B(H)$ 范数全纯函数。这不声称未乘 $L$ 的有限乘积范数收敛。

## 3. 真正范数稠密乘子像

固定 $z$，在切口 $N$ 将前缀写成
$$
A_N(z)=\prod_{\nu=1}^{N-1}Z_\nu(z)^{p_\nu}
=C^{e_N(z)}G_N(z).
\tag{9}
$$
$z=0$ 时 $e_N(z)=2\sum_{\nu<N}p_\nu$；$z\ne0$ 时
$e_N(z)=\sum_{\nu<N}p_\nu$。各情形的 $G_N(z)$ 都是有界可逆原解析芽，因为每个因子的准确最低次系数非零。这里只对固定参数、有限前缀断言单位。

再使用共同幂范数逼近稿中包含 $j=0$ 的原加权收缩
$$
J_M=C\,U_M,\qquad U_M\text{ 为有界单位},\qquad
\|(I-J_M)L\|\to0.
$$
置
$$
W_{N,M}(z)=G_N(z)^{-1}U_M^{\,e_N(z)}.
$$
准确原乘法给
$$
T(z)W_{N,M}(z)=T_N(z)J_M^{\,e_N(z)}.
\tag{10}
$$
因而
$$
\|(I-T(z)W_{N,M}(z))L\|
\le e^{|z|K_N}
\left(H_N(|z|)+e_N(z)\|(I-J_M)L\|\right).
\tag{11}
$$
先固定 $N$ 令 $M$ 大，再令 $N$ 大。右侧趋零，而 (10) 的范数至多 $e^{|z|K_N}$。在 $\mathscr B=\overline{L\mathscr A}$ 上，由一致有界性延拓，得到
$$
T(z)W_n(z)b\to b\quad\text{于算子范数，}\qquad b\in\mathscr B.
\tag{12}
$$
所以 $\overline{T(z)\mathscr B}=\mathscr B$，这里 $T(z)$ 是实际有界乘子，尚未要求它自身属于 $\mathscr B$。

(9) 中 $e_N(z)\to\infty$，尾积有界，故同时
$$
T(z)\in\mathfrak F:=\bigcap_{k\ge1}C^k\mathscr A.
\tag{13}
$$
(10)–(11) 也给原 $H$ 上的有界强*单位；所有因子属于原 $\mathscr A$ 并保持普通旗。故同一 $T(z)$ 在全部原普通旗及固定有限放大旗上准亲和。这里只压缩真实强*单位，不从全空间性质免费下降到商。

## 4. 固定原二次目标与全部分子

令
$$
\widehat P(z)=CZ_0(z)T(z)^2.
$$
定义 $a=\zeta_0/c>0$、
$W=(1-\zeta_0)F_0/C$。这个 $W$ 是有界、拟幂零的奇次原多项式。对 $s\ne0$，同一实际零点芽给
$$
B(s)=\sqrt a\,s\sum_{k\ge0}
\binom{1/2}{k}\left(\frac{W}{as^2}\right)^k,\qquad
\widehat X(s)=CB(s)T(s^2).
\tag{14}
$$
级数逐非零 $s$ 在算子范数绝对收敛，且 $B(s)$ 是原解析单位。于是
$$
\widehat X(s)^2=\widehat P(s^2),\qquad
\widehat X(-s)=-\widehat X(s).
\tag{15}
$$

由 $F_0$ 的最低次准确为 $C^2$，写
$$
(1-\zeta_0)F_0=C^2G_0(C),\qquad G_0(0)>0.
$$
$G_0$ 为偶多项式。取其正规零点平方根芽 $g_0$，定义固定分母
$$
\boxed{\widehat Q=Cg_0(C)T(0).}
\tag{16}
$$
则 $g_0(C)$ 及其逆都在原范数多项式代数，并且
$$
\boxed{\widehat P(0)=C\widehat Q^{\,2}.}
\tag{17}
$$
$\widehat Q\in\mathfrak F$，且由 (12)、原 $C$ 在 $\mathscr B$ 上的稠密乘子像及解析单位，有
$\overline{\widehat Q\mathscr B}=\mathscr B$。同理，每个固定
$\widehat X(s)$、$\widehat P(z)$ 都具有此范数稠密乘子像，且在全部原 Hilbert 旗上准亲和。

全部 $\nu$ 的原收缩乘积还给，令
$K=\sum_{\nu\ge0}d_\nu\zeta_\nu<\infty$，
$$
\|\widehat P(z)-\widehat P(w)\|\le cK|z-w|
\quad(|z|,|w|\le1).
\tag{18}
$$
这里使用 $d_0=1$ 与 $2p_\nu=d_\nu$，没有换平方或尾指数。

## 5. 真正属于同一 $\Omega(\mathscr B)$ 的二次近似

固定任意 $\Re\theta>0$，使用已经付清 $P_\theta=Z^{-\theta}\in\Omega(\mathscr B)$，置
$$
v=\widehat QP_\theta,\qquad u(s)=\widehat X(s)P_\theta.
\tag{19}
$$
由于上述每个乘子在 $\mathscr B$ 上有范数稠密像，
$$
\boxed{v,\ u(s)\in\mathfrak F\cap\Omega(\mathscr B)\qquad(s\ne0).}
\tag{20}
$$
这是实际元素，不只是 Hilbert 准亲和分母。两者在原 $H$ 以及所有原旗上的准亲和来源也同时保留。

同一固定 $v$ 满足
$$
\boxed{
\|u(s)^2-Cv^2\|
\le cK\|P_\theta\|^2|s|^2,\qquad0<|s|\le1.
}
\tag{21}
$$
$u(s)$ 是穿孔平面上的 $\mathscr B$ 范数全纯函数。每个分子各自有界；没有从 (21) 推出其在 $s\to0$ 时一致有界。

这与旧等权曲线的范数分离相容：这里的块是 (1)，它们在完整 $L$ 后具有 (2)、(4) 的额外范数来源；旧等权块并不满足这些估计。本稿也没有复开已排的单独分母 $P_\theta$：固定目标是更强的实际共同幂分母 $v=\widehat QP_\theta$。

## 6. 单列接口与仍未付的量

若 $s_j\to0$ 使 $u(s_j)\Omega$ 强收敛，则 (21) 的同列双线性矩与循环源 $v\Omega$ 给[单前向列定理](R267-appendix-single-forward-column-compactness-and-original-stable-root.md)的最大闭稳定平方根。没有要求原全域 $vH$ 预先进入该根域。

还保留直接原超不变接口，包括 $m_0=0$。首位符号 $\gamma$ 满足
$$
\gamma(\widehat X(s))=i\widehat X(is),\qquad
\|\bigl(\gamma(\widehat X(s))+i\widehat X(s)\bigr)
\bigl(\gamma(\widehat X(s))-i\widehat X(s)\bigr)\|
\le2cK|s|^2.
$$
若 $u(s_j)\Omega$ 强收敛，以固定
$F_+=\sqrt2(I+C/c)^{-1}$、
$F_+\Omega=e_+$，可把它准确搬到非零首位本征源
$P_\theta\gamma(P_\theta)e_+$：
$$
\widehat X(s)P_\theta\gamma(P_\theta)e_+
=\gamma(P_\theta)F_+u(s)\Omega.
$$
[原首位双线性桥](R12-appendix-first-bit-gauge-zero-divisors-and-single-forward-column-hyperinvariants.md)遂给同一 $C$ 的非平凡超不变子空间；该桥的零列分支使用 $\widehat P(0)$ 单射，仍适用。

目前尚未证明这个真实单列强子列，也未构造 $u\in\mathscr B$ 满足
$u^2=Cv^2$。新增量是 (20)–(21)：完整原二次近似现在确实发生在同一个实际范数稠密主理想类中，不能再用缺少 $\Omega(\mathscr B)$ 来源来替代这个仍须解决的奇列费用。
