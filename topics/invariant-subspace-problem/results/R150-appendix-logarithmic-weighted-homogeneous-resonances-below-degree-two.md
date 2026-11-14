# R150 附录：对数幂中心、次数小于二的加权齐次共振与非零参数

日期：2026-11-13（UTC）。作者：kernel_resume_1cf / Astra-ISP-1cf8c51d；AI 辅助：GPT-6 Astra Pro。
状态：已证明。

本稿推广[完全居中临界幂](R150-appendix-centered-critical-powers-gradient-tail-cancellation-and-nonzero-parameters.md)，但不重复其 $\alpha=(1,1/k)$、$G(x,y)=y^k-x$ 的旧范围。新增的是任意固定有限个正实对数权、任意在中心曲线上相消的加权齐次标量多项式，以及整个外层多项式的完整 Bell 排核。证明不要求把一个梯度坐标解成独立 first，也不使用未知核上的无界逆。

## 1. 原行、固定中心常数及结论

对每个固定实数 $\rho>0$，定义
$$
a_j^{(\rho)}
=\frac{\rho(\log(j+2))^{\rho-1}}{j+2},
\qquad j\ge0.
\tag{1.1}
$$
这是一条正的 $\ell^2\setminus\ell^1$ 行。存在唯一实常数 $\kappa_\rho$，使
$$
\sum_{j<n}a_j^{(\rho)}
=(\log(n+2))^\rho+\kappa_\rho
+O\!\left(n^{-1}(\log(n+2))^{\rho-1}\right).
\tag{1.2}
$$
其证明见下一节。采用同一个固定原函数
$$
\boxed{
u_\rho=-\kappa_\rho+\sum_{j\ge0}a_j^{(\rho)}\chi_j.
}
\tag{1.3}
$$
这里没有随 $n$ 调整函数的常数。

固定有限模式数 $\ell\ge1$ 和正实权
$\alpha_1,\ldots,\alpha_\ell$，写 $u_\nu=u_{\alpha_\nu}$，
$X_\nu=X_{u_\nu}$ 为原规范闭 first。

设非零标量多项式 $G\in\mathbb C[x_1,\ldots,x_\ell]$ 对这些权齐次，准确说每个非零单项式 $c_\beta x^\beta$ 都满足
$$
\sum_{\nu=1}^{\ell}\alpha_\nu\beta_\nu=D
$$
，其中
$$
\boxed{0<D<2,\qquad G(1,\ldots,1)=0.}
\tag{1.4}
$$
权可以是不满足有理比例的任意正实数；只要求原有限支撑确实满足上述等式。

**定理 1。** 对每个标量多项式 $Q\in\mathbb C[z]$ 满足 $Q(0)\ne0$，以及任意原复 $\ell^2$ first 指数
$$
w=w_*+\sum_jw_j\chi_j,
$$
都有
$$
\boxed{Q\bigl(G(u_1,\ldots,u_\ell)\bigr)e^w
\text{ 对原实际 }A\text{ 循环}.}
\tag{1.5}
$$
特别，对全部 $\lambda\ne0$、整数 $r\ge1$，
$$
\boxed{[G(u_1,\ldots,u_\ell)-\lambda]^r e^w
\text{ 循环}.}
\tag{1.6}
$$

这是对完整原点态多项式重新排核，不从单独循环的因子推断其点态乘积循环。结论不声称 $G(u)e^w$ 或 $G(u)^re^w$ 本身已循环；零参数仍不由当前测试排除。

## 2. 真实前缀中心与非整数对数尾

令
$$
F_n=\{0,\ldots,n-1\},\qquad S=S_n=\log(n+2),
$$
并记每个原 first 的准确中心
$$
s_{\nu n}=-\kappa_{\alpha_\nu}
+\sum_{j<n}a_j^{(\alpha_\nu)}.
$$

### 2.1 求和常数和实际误差

函数
$f_\rho(x)=\rho(\log x)^{\rho-1}/x$ 最终正且递减，
且其原函数为 $(\log x)^\rho$。
在最终递减区间，求和与逐个单位区间积分之差的尾由该处的函数值控制。
有限低位只改一个固定常数。因此
$$
\sum_{j<n}f_\rho(j+2)-(\log(n+2))^\rho
$$
收敛到有限数 $\kappa_\rho$，余项为
$O(f_\rho(n+2))$，即 (1.2)。
于是
$$
\boxed{
s_{\nu n}=S^{\alpha_\nu}
+O(n^{-1}S^{\alpha_\nu-1}),\qquad
p_{\nu n}:=s_{\nu n}/S^{\alpha_\nu}
=1+O((nS)^{-1}).
}
\tag{2.1}
$$
所有常数允许依赖固定的有限权族，不依赖 $n$。

加权齐次性是原有限多项式的逐单项式恒等式。它给
$$
(\partial^\beta G)(s_n)
=S^{D-\alpha\cdot\beta}
(\partial^\beta G)(p_n).
\tag{2.2}
$$
因 $p_n\to\mathbf1$ 且 $G(\mathbf1)=0$，
$$
\boxed{G(s_n)=O(n^{-1}S^{D-1})\longrightarrow0.}
\tag{2.3}
$$
特别，此处没有把实际中心精确等同于形式中心 $S^\alpha$。

### 2.2 覆盖全部远尾的统一估计

对任意固定 $R\ge0$，有
$$
\boxed{
\sum_{j\ge n}\frac{[1+\log((j+2)/(n+2))]^R}{(j+2)^2}
\le \frac{C_R}{n}.
}
\tag{2.4}
$$
直接证明是把 $x_j=\log((j+2)/(n+2))$ 按区间
$[h,h+1)$、$h=0,1,\ldots$ 分组。
每组位数不超过 $C(n+2)e^h$，每个分母至少为
$(n+2)^2e^{2h}$，故该组至多
$C(1+h)^Re^{-h}/(n+2)$；对 $h$ 求和得到 (2.4)。

这条界处理任意大的 $j/n$，而不只处理 $j$ 与 $n$ 同阶的近尾。
因此后面所有非整数幂 $(1+x_j/S)^\rho$ 均有实际一致预算。

## 3. 冗余的实际梯度变量与全尾相消

在原共同深词域上定义
$$
\boxed{
U_n=\sum_{\nu=1}^{\ell}G_\nu(s_n)(X_\nu-s_{\nu n}),
\qquad
V_{\nu n}=S^{D/2-\alpha_\nu}(X_\nu-s_{\nu n}),
}
\tag{3.1}
$$
其中 $G_\nu=\partial_\nu G$。
这些变量允许线性相关。我们不选一个可能消失的梯度系数作分母，也不宣称某个自然无界和已经在最大交域上闭。

### 3.1 梯度尾：Euler 恒等式与实际中心误差

记
$$
g_\nu=G_\nu(\mathbf1),\qquad
G_\nu(s_n)=S^{D-\alpha_\nu}(g_\nu+e_{\nu n}),
\quad |e_{\nu n}|\le C/(nS),
\tag{3.2}
$$
这是 (2.1)—(2.2) 的有限多项式估计。
逐项对加权齐次等式求导给 Euler 关系
$$
\sum_\nu\alpha_\nu x_\nu G_\nu(x)=DG(x).
$$
在 $\mathbf1$ 处，
$$
\boxed{\sum_\nu\alpha_\nu g_\nu=0.}
\tag{3.3}
$$

$U_n$ 的原补集行准确为
$$
d_{n,j}=\sum_\nu G_\nu(s_n)a_j^{(\alpha_\nu)},
\qquad j\ge n.
$$
置 $x=\log((j+2)/(n+2))\ge0$。由 (3.2)，
$$
d_{n,j}
=\frac{S^{D-1}}{j+2}
\sum_\nu\alpha_\nu(g_\nu+e_{\nu n})
(1+x/S)^{\alpha_\nu-1}.
\tag{3.4}
$$
对每个固定实指数 $\rho$，在 $y\ge0$ 上有
$$
|(1+y)^\rho-1|\le C_\rho y(1+y)^{R_\rho},
\qquad
|(1+y)^\rho|\le C_\rho(1+y)^{R_\rho}
$$
，取充分大的固定 $R_\rho\ge0$ 即可。
用 (3.3) 消掉常数项，再用 $S\ge1$ 和 (3.2)，得到某个固定 $R$ 下
$$
\boxed{
|d_{n,j}|
\le
\frac{C S^{D-2}}{j+2}
(x+n^{-1})(1+x)^R.
}
\tag{3.5}
$$
其中 $n^{-1}$ 项完整支付实际 $s_n$ 与形式中心的误差。
由 (2.4)，
$$
\boxed{
g_{U,n}:=\|d_{n,\ge n}\|_2
\le C n^{-1/2}S^{D-2}.
}
\tag{3.6}
$$

### 3.2 二阶变化变量的补集和有限头

$V_{\nu n}$ 的补集行为
$S^{D/2-\alpha_\nu}a_j^{(\alpha_\nu)}$。
同样用 (2.4)，准确得到
$$
\boxed{
g_{V_\nu,n}\le C n^{-1/2}S^{D/2-1}.
}
\tag{3.7}
$$
因为 $D<2$，有 $S^{D-2}\le S^{D/2-1}$，所以有限族的共同尾尺度为
$$
\boxed{
\varepsilon_n=g_{U,n}+\sum_\nu g_{V_\nu,n}
\le C n^{-1/2}S^{-(2-D)/2}.
}
\tag{3.8}
$$

另一方面，正行的头和为 $O(S^{\alpha_\nu})$。
由 (3.2)，$U_n$ 的有限头绝对系数和至多 $CS^D$，
每个 $V_{\nu n}$ 的有限头绝对系数和至多 $CS^{D/2}$。
它们的实际头均为这些系数乘 $(V_j-I)$ 的有限和，故带有 R251 的真实 $N_j$ 因子。

## 4. 原多项式的完整有限 Taylor 展开

在已付的原共同域中，有限 Taylor 恒等式给
$$
\boxed{
G(X)=G(s_n)I+U_n+
\sum_{|\beta|\ge2}
\frac{(\partial^\beta G)(p_n)}{\beta!}
S^{D(1-|\beta|/2)}V_n^\beta.
}
\tag{4.1}
$$
这里 $V_n^\beta=\prod_\nu V_{\nu n}^{\beta_\nu}$，全部混合词取原共同域中的相同值；和只有有限项。
式 (4.1) 来自 (2.2) 及
$X_\nu-s_{\nu n}=S^{\alpha_\nu-D/2}V_{\nu n}$。

所有 $|\beta|\ge2$ 项的标量系数一致有界，且当 $|\beta|>2$ 时趋于零。
没有要求二阶 Hessian 非退化，二阶项可以部分或全部为零。
若某个梯度方向恒为零，(3.6) 仍成立。

固定非恒定 $Q$，记 $m_Q=\deg Q$，并令
$$
K(x)=Q(G(x)),\qquad m_0=\deg K.
$$
将 (4.1) 代入整个 $Q$，给出固定次数、系数一致有界的
$U_n,V_{1n},\ldots,V_{\ell n}$ 多项式。
其常数项准确为
$$
Q(G(s_n))I\longrightarrow Q(0)I.
\tag{4.2}
$$
对后续 Bell 偏导则无需重新选梯度坐标：直接使用
$$
X_\nu=s_{\nu n}+S^{\alpha_\nu-D/2}V_{\nu n}.
\tag{4.3}
$$
$K$ 中每个单项式的原权不超过 $m_QD$。
(4.3) 的常数及变量系数均不超过 $CS^{\alpha_\nu}$。
因此对每个固定 $\beta$，把 (4.3) 代入
$(\partial^\beta K)(X)$ 后，全部标量系数都至多为
$$
CS^{m_QD}.
\tag{4.4}
$$
这支付的是原各偏导的有限单项式预算，不是把“普通总次数下降”误当成多尺度小量。

## 5. 所有混合 Bell 系数的真实头与小补集

以下保留全部原混合累积量。
令
$$
H(\xi,V)=e^{-\xi V}(\cosh\xi\,I+V\sinh\xi),\qquad
B_w=\prod_jH(w_j,V_j),
$$
$$
\mathcal B_w(t)
=\prod_jH\!\left(w_j+\sum_\nu t_\nu a_j^{(\alpha_\nu)},V_j\right)
H(w_j,V_j)^{-1}.
\tag{5.1}
$$
把 $w$ 加作 [R145 §§2、8](R145-multimode-bell-mixed-domains-cyclicity.md) 的额外实际模式，
在其参数1处取共同整轨道，得到循环向量
$\xi_w=B_w^{-1}e^w$ 的全部原 $X_\nu$ 混合自然域。
[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) 给规范最大图及原指数图核心。

记 $L_j(\xi)=\log H(\xi,V_j)$，取字符为零的规范对数。
[R154 §3](R154-supercubic-modes-all-polynomials-exponential-weights.md) 的实际参数积分给
$$
L_j^{(h)}(w_j)=N_jU_{hj},\qquad
\sup_j\|U_{hj}\|<\infty
\quad(h\ge1\text{ 固定}).
\tag{5.2}
$$
一阶另保留
$$
L_j'(w_j)=w_jN_jW_j,\qquad\sup_j\|W_j\|<\infty.
\tag{5.3}
$$
这是由 $L_j'(0)=0$ 对统一小圆盘中的实际 $L_j''/N_j$ 商沿线段积分得到；
有限低位分别处理。并非因字符为零就有界除以 $N_j$。
[完全居中临界幂稿 §§4–5](R150-appendix-centered-critical-powers-gradient-tail-cancellation-and-nonzero-parameters.md) 已完整给出这一加强。

本稿各行虽不可和，但都在 $\ell^2$。
高位的统一估计
$$
\|L_j(w_j+\xi)-L_j(w_j)\|
\le C(|w_j||\xi|+|\xi|^2)
$$
使 (5.1) 的对数在原点邻域按绝对范数局部一致收敛，
其中 $\xi=\sum_\nu t_\nu a_j^{(\alpha_\nu)}$。
故任意固定多重导数可以逐项计算：
$$
\kappa_\delta
:=\partial^\delta\log\mathcal B_w(0)
=\sum_j\left(\prod_\nu
(a_j^{(\alpha_\nu)})^{\delta_\nu}\right)
L_j^{(|\delta|)}(w_j),\qquad \delta\ne0.
\tag{5.4}
$$

取整数
$$
M\ge \max(1,D,m_QD)
$$
并只保留 $1\le|\delta|\le m_0$ 的有限族。准确拆分
$$
\boxed{S^M\kappa_\delta=H_{\delta n}+E_{\delta n},}
\tag{5.5}
$$
其中有限头来自 $j<n$，由 (5.2)—(5.3) 有
$$
H_{\delta n}=\sum_{j<n}N_jB_{\delta j,n},\qquad
\sum_{\delta,j<n}\|B_{\delta j,n}\|\le CS^M.
\tag{5.6}
$$

为完整支付补集，置 $A_0=\max_\nu(\alpha_\nu-1)_+$。
各原行满足
$a_j^{(\alpha_\nu)}\le C(\log(j+2))^{A_0}/(j+2)$。
$|\delta|\ge2$ 时，乘积尾和不超过
$CS^{m_0A_0}/n$；$|\delta|=1$ 时，由 (5.3) 和 Cauchy–Schwarz 不超过
$CS^{A_0}n^{-1/2}\|w_{\ge n}\|_2$。
因此
$$
\boxed{
\max_\delta\|E_{\delta n}\|
\le
CS^{M+m_0A_0}
\left(n^{-1}+n^{-1/2}\|w_{\ge n}\|_2\right)
\longrightarrow0.
}
\tag{5.7}
$$
这也覆盖非整数正权和任意固定 $\ell^2$ 指数列；不要求 $w$ 有额外尾速度。

令 $C_\beta^w=\partial^\beta\mathcal B_w(0)$。
当 $\beta\ne0$ 时，$C_\beta^w$ 是有限组 $\kappa_\delta$ 的固定有限多项式，且没有常数项。
完整原 Bell 为
$$
P_K(X)
=\sum_\beta\frac{C_\beta^w}{\beta!}
(\partial^\beta K)(X),\qquad C_0^w=I.
\tag{5.8}
$$
原真实生成式是
$$
K(u)e^w=B_wP_K(X)\xi_w.
\tag{5.9}
$$

对于 (5.8) 的 $\beta=0$ 项，使用 §4 的整体表达式。
对于 $\beta\ne0$，使用 (4.4)，并在每个 Bell 单项式中用 (5.5)。
若该单项式含 $h\ge1$ 个累积量，其数值系数至多为
$$
CS^{m_QD-Mh}\le C.
\tag{5.10}
$$
于是 (5.8) 成为固定次数、固定个数字母的精确多项式；
字母为 $U_n,V_{\nu n}$、$H_{\delta n}$ 和小有界算子 $E_{\delta n}$，
所有数值系数一致有界。

把 $E_{\delta n}$ 吸收进有界交换系数，再把 $U_n,V_{\nu n}$ 拆成真实有限头与补集 first。
全部显式头字母共同取 $A_n$ 为 $1$ 与所有头绝对系数总和的最大值，仍有
$
\boxed{1\le A_n\le CS^M,}
\tag{5.11}
$$
补集 first 族的共同尺度是 (3.8)。
若把所有显式头和补集 first 字母置零，剩余算子常数为
$$
\boxed{Q(G(s_n))I+o(1)\longrightarrow Q(0)I.}
\tag{5.12}
$$
每个非基础 Bell 项剩下时至少含一个 $E_{\delta n}$，所以 (5.7)、(5.10) 支付这里的 $o(1)$。
没有把零字符 Bell 系数本身当作单位，也没有丢弃混合 cumulant。

## 6. 增长头、小常数和整个有限柱的根界

本节复用已证真实 carry 关系
$$
N_j^2=\eta_jN_{j+1},\quad
\eta_j\le e^{-770\,16^j},\quad\|N_j\|\le1.
$$
若一个有限头字母为
$\sum_{j<n}N_jB_j$，其中 $B_j\in A'$ 彼此交换，
其物理支撑不必限于前 $n$ 位。
任意总长度 $h$ 的混合头词至多为 $A_n^h$；
当 $h\ge\max(2n,16)$ 时，[R251 §2](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md) 的进位计数给
$$
\|\text{头词}\|
\le A_n^h e^{-\gamma h^4},
\qquad \gamma=770/16^4.
\tag{6.1}
$$
证明只需将全部交换 $B_j$ 移开，保留实际 $N_j$ 产品。
对应的伴随版本同样成立。

令 $\mathsf Q_n=Q_{F_n}$ 为整个前 $n$ 位的柱投影。
同一 R251 补集次数尺度和固定有限多行极化给：任何总长度 $j$ 的混合补集伴随词在整个 $\mathsf Q_nH$ 上都有准确自然域，并满足
$$
\|\text{该词}\,\mathsf Q_n\|
\le(C\varepsilon_n\sqrt j)^j.
\tag{6.2}
$$
所有有界系数保持原共同词域并可移到左侧；
不要求它们在补集的指数次数范数中有同样预算。

置 $\kappa=2-D>0$，取
$$
\boxed{p_n=\lceil nS^{\kappa/2}\rceil.}
\tag{6.3}
$$
则 (3.8)、(5.11) 给
$$
p_n/n\to\infty,\qquad
\varepsilon_n\sqrt{p_n}=O(S^{-\kappa/4})\to0,
\qquad
(n/p_n)\log A_n=O(S^{-\kappa/2}\log S)\to0.
\tag{6.4}
$$

设 $\mathscr T_n$ 是这些伴随字母的一个固定次数多项式，
系数一致有界、算子常数项 $\Delta_{0n}$ 的范数趋零。
记固定展开次数上界为 $D'$，并令
$$
\delta_n=A_ne^{-\gamma(2n)^3}\to0,\qquad
e_n=\|\Delta_{0n}\|+C\varepsilon_n\sqrt{D'p_n}\to0.
$$
展开 $\mathscr T_n^{p_n}$，把小算子常数也记作一个尾字母。
每项的头长度 $h$、无界尾长度 $j$ 和常数字母数 $c$ 满足
$p_n\le h+j+c\le D'p_n$。
固定字母数与系数界只付 $C_0^{p_n}$。

$h\ge2n$ 时，用 (6.1) 得 $\delta_n^h$，连同 (6.2) 和小常数字母，
总费用至多 $C_0^{p_n}(\delta_n+e_n)^{p_n}$。
$h<2n$ 时，$j+c\ge p_n-2n$，总费用至多
$C_0^{p_n}A_n^{2n}e_n^{p_n-2n}$。
所以
$$
\boxed{
\|\mathscr T_n^{p_n}\mathsf Q_n\|^{1/p_n}
\le C_0\left[
\delta_n+e_n+
A_n^{2n/p_n}e_n^{\,1-2n/p_n}
\right]\longrightarrow0.
}
\tag{6.5}
$$
若 $e_n=0$，低头部分没有非零项，按零解释。
此处只需 $\|\Delta_{0n}\|\to0$，不要求长迭代中 $p_n\|\Delta_{0n}\|\to0$。

## 7. 原最大核、真实域与目标循环性

非零常数 $Q$ 的结论直接来自 $e^w$ 循环；以下取 $\deg Q\ge1$。
令 $\mathcal P_K$ 为 (5.8) 的原规范最大闭实现。
R186 给其完整 $C$ 自伴性和 $\xi_w$ 的图核心。
若 $\ker\mathcal P_K\ne0$，令 $\Pi$ 为该核的正交投影。
在原共同伴随深词域上，
$$
\Pi P_K^*=0.
$$
取
$$
\boxed{\mathscr T_n=I-\frac{P_K^*}{\overline{Q(0)}}.}
\tag{7.1}
$$
由 (5.12)，其算子常数项趋于零，所有其他系数与头尾预算正是 §§5–6 所付者。

对每个固定 $n$，(3.1) 只是原 first 的有限线性组合，
补集 first 也只从这些行减去有限有界头。
因此所需有限词恒等式均在同一个原共同深域中成立。
R251 把整个 $\mathsf Q_nH$ 送入任意所需有限混合伴随词域；
所有有界系数属于 $A'$ 的伴随代数并保持这些域。
故对有限整数 $p_n$ 可逐次使用 (7.1)，严格得到
$$
\Pi\mathsf Q_n=\Pi\mathscr T_n^{p_n}\mathsf Q_n.
\tag{7.2}
$$
整个过程不把 $n$ 依赖系数穿过 $\Pi$，也不向未知核赠送额外自然域。

(6.5) 使右侧范数趋零，而 $\mathsf Q_n\to I$ 强，故 $\Pi=0$。
所以 $\mathcal P_K$ 无核；其原 $C$ 自伴性给像稠密。
最后，(5.9) 的完整原指数图核心及有界交换单位 $B_w$
给 $K(u)e^w$ 循环，完成 (1.5)—(1.6)。

## 8. 原临界幂之外的明确类

### 8.1 任意有限整幂的临界曲线

取不同正整数 $p,q$ 和任意 $0<D<2$，令
$$
x=u_{D/q},\qquad y=u_{D/p}.
$$
$G(x,y)=y^p-x^q$ 对原权 $(D/q,D/p)$ 齐次，权次数为 $D$ 且
$G(1,1)=0$。
因此
$$
\boxed{
[(u_{D/p})^p-(u_{D/q})^q-\lambda]^r e^w
\text{ 对全部 }\lambda\ne0,r\ge1,w\text{ 循环}.
}
\tag{8.1}
$$
例如 $D=3/2,p=3,q=2$ 给
$[(u_{1/2})^3-(u_{3/4})^2-\lambda]^re^w$。
这里各原常数始终按 (1.3) 固定。

### 8.2 真混合三模式

取权
$$
(\alpha_1,\alpha_2,\alpha_3)=(1,1/2,3/4),\qquad D=3/2,
$$
和 $G(x)=x_1x_2-x_3^2$。
于是
$$
\boxed{
[u_1u_{1/2}-(u_{3/4})^2-\lambda]^r e^w
\text{ 对全部 }\lambda\ne0,r\ge1,w\text{ 循环}.
}
\tag{8.2}
$$
证明包括 $x_1x_2$ 的真实混合 Bell 累积量，未把不同模式当作不交支持。

两例都还允许把括号内未减 $\lambda$ 的整个共振量送入任意
$Q$ 满足 $Q(0)\ne0$。固定复数倍的模式重标及固定可逆线性换元，
也可按[多尺度稿 §5](R150-appendix-multiscale-column-budgets-bell-covariance-and-full-plane-joint-polynomials.md)
的真实 Bell 协变恢复原向量，不新增未经支付的无限模式。

## 9. 去重与剩余范围

完全居中临界幂稿已经给出
$\alpha=(1,1/k)$、$D=1$、$G(x,y)=y^k-x$ 的全部非零参数及
$Q(0)\ne0$ 结论。本稿对此只作明确推广：
有限任意正实权、全加权齐次有限支撑、实际 Euler 梯度尾，
以及不可删的混合 Bell 预算。

此前直接多尺度判据要求原中心值占最大单项式尺度的固定比例；
本稿中 $G(s_n)=O(n^{-1}S^{D-1})$，所以那个要求并不成立。
旧单一线性中心的最高普通符号判据也不能自动消去这些中心曲线上的共振根。

$D<2$ 用在 (3.8)、(6.4)：二阶变化尾留下
$S^{-(2-D)/2}$，从而可同时令迭代次数远大于头位数而让尾根费用趋零。
这是一条已证充分范围，不是对 $D\ge2$ 的反例或不可能性声明。
本稿也未处理 $Q(0)=0$、一般非齐次更深相消、无限模式或任意向量循环性。
真正常见证的源上界、无权核内饱和及普通复 Hilbert ISP 仍开放。

## 10. 中心曲线的消失重数：扩大到 D<2m

日期：2026-11-13（UTC）。作者：kernel_resume_1cf / Astra-ISP-1cf8c51d。
状态：已证明。本节独立扩大主稿的范围。

本节保持 §§1–2 的同一有限权族 $\alpha_\nu>0$、原函数
$u_{\alpha_\nu}$、固定常数 $\kappa_{\alpha_\nu}$、$S=\log(n+2)$
和实际中心 $s_{\nu n}$。
但不再要求 $D<2$。

设非零 $G$ 对 $\alpha$ 加权齐次，权次数为 $D>0$，
并且 $G(\mathbf1)=0$。定义它在 $\mathbf1$ 的普通有限消失重数
$$
m=\min\{|\beta|:(\partial^\beta G)(\mathbf1)\ne0\}\ge1.
\tag{10.1}
$$
这是原有限标量多项式的重数，不是实际算子的核重数。

**强化定理。** 如果
$$
\boxed{D<2m,}
\tag{10.2}
$$
则对每个标量多项式 $Q$ 满足 $Q(0)\ne0$、每个原复
$\ell^2$ first 指数 $w$，
$$
\boxed{Q(G(u_{\alpha_1},\ldots,u_{\alpha_\ell}))e^w
\text{ 对原实际 }A\text{ 循环}.}
\tag{10.3}
$$
特别包含全部 $[G(u)-\lambda]^re^w$，其中 $\lambda\ne0,r\ge1$。
$m=1$ 恢复主稿 $D<2$；新增范围在 $m>1$。

### 10.1 局部标量曲线只用于证明有限单项式消失

选取线性切向坐标和 $\ell-1$ 个横向坐标：
$$
x_1=1+\alpha_1t,\qquad
x_\nu=1+\alpha_\nu t+v_\nu
\quad(2\le\nu\le\ell).
$$
这等价于取线性泛函 $\ell_0(z)=z_1/\alpha_1$，满足
$\ell_0(\alpha)=1$；没有除以某个可能为零的 $G$ 梯度。

定义真正的有限多项式
$$
\mathfrak G(t,v)
=G(1+\alpha_1t,\,1+\alpha_2t+v_2,\ldots,
1+\alpha_\ell t+v_\ell).
$$
我们先证明
$$
\boxed{
[t^jv^\beta]\mathfrak G\ne0
\quad\Longrightarrow\quad j+2|\beta|\ge2m.
}
\tag{10.4}
$$

在 $t=0$ 的小邻域，选值为1的标量解析幂
$$
\rho(t)=(1+\alpha_1t)^{1/\alpha_1},\qquad
\psi_\nu(t)=\rho(t)^{\alpha_\nu}-1-\alpha_\nu t.
$$
于是 $\psi_\nu(t)=O(t^2)$。
加权齐次的逐单项式恒等式给每个多重指标 $\gamma$
$$
(\partial^\gamma G)(\rho(t)^\alpha)
=\rho(t)^{D-\alpha\cdot\gamma}
(\partial^\gamma G)(\mathbf1).
\tag{10.5}
$$
因此所有 $|\gamma|<m$ 的原导数在整条局部曲线上都为零。

令 $v_\nu'=v_\nu-\psi_\nu(t)$。
在这些局部标量坐标中，沿横向变量展开，
$$
\mathfrak G(t,v)
=\sum_{|\beta|\ge m}
h_\beta(t)\prod_{\nu=2}^{\ell}
\bigl(v_\nu-\psi_\nu(t)\bigr)^{\beta_\nu},
\tag{10.6}
$$
其中 $h_\beta(t)$ 在零点解析。
对横向变量而言求和有限；(10.5) 正是所有低于 $m$ 阶项消失的理由。

赋 $t$ 权1、每个 $v_\nu$ 权2。
每个 $\psi_\nu(t)$ 的 Taylor 阶数至少2，所以 (10.6) 不含权小于
$2m$ 的单项式。
$\mathfrak G$ 原来是有限多项式，其低权系数因此准确为零，得到 (10.4)。

这里只借局部解析坐标证明原有限标量多项式的系数恒等式。
下文不把 $\rho$、$\psi_\nu$ 或任何非线性解析换元代入无界算子。

### 10.2 实际线性切向、横向 first 及完整远尾

在原共同深词域中，置
$$
Z_{\nu n}=\frac{X_\nu-s_{\nu n}}{S^{\alpha_\nu}},
\qquad
\mathsf t_n=\frac{Z_{1n}}{\alpha_1},
\qquad
\mathsf n_{\nu n}=Z_{\nu n}-\alpha_\nu\mathsf t_n
\quad(2\le\nu\le\ell).
\tag{10.7}
$$
它们全是原 first 的有限线性组合。
以下从不假设这些自然差已经在最大交域上闭。

对 $j\ge n$，令 $x=\log((j+2)/(n+2))$。
$\mathsf t_n$ 的准确补集行为
$$
\frac{1}{S(j+2)}(1+x/S)^{\alpha_1-1}.
$$
$\mathsf n_{\nu n}$ 的准确补集行为
$$
\boxed{
\frac{\alpha_\nu}{S(j+2)}
\left[
(1+x/S)^{\alpha_\nu-1}
-(1+x/S)^{\alpha_1-1}
\right].
}
\tag{10.8}
$$
后一方括号的常数项真实抵消。
用 §2.2 覆盖全部 $j/n$ 的指数分组估计，得到
$$
\boxed{
g_{\mathsf t,n}\le C n^{-1/2}S^{-1},\qquad
g_{\mathsf n_\nu,n}\le C n^{-1/2}S^{-2}.
}
\tag{10.9}
$$
确实，(10.8) 的绝对值至多为
$C x(1+x)^R/[S^2(j+2)]$，其中 $R$ 固定；
其平方和由 (2.4) 控制。
这一步同样保任意非整数正权和所有远尾。

每个 (10.7) 的有限头绝对系数和均为 $O(1)$，
因为各原正行头和为 $O(S^{\alpha_\nu})$。
原实际中心已经包含在 $X_\nu-s_{\nu n}$ 中，
没有因 (10.7) 引入额外条件收敛的标量尾和。

### 10.3 缩放与真实中心误差

令
$$
\delta=\frac{D}{2m}\in(0,1),\qquad
\boxed{
\mathsf V_n=S^\delta\mathsf t_n,\qquad
\mathsf U_{\nu n}=S^{2\delta}\mathsf n_{\nu n}.
}
\tag{10.10}
$$
由 (10.9)，这个有限族的共同补集尺度满足
$$
\begin{aligned}
\varepsilon_n
&\le Cn^{-1/2}
\bigl(S^{\delta-1}+S^{2\delta-2}\bigr)\\
&\le\boxed{Cn^{-1/2}S^{\delta-1}.}
\end{aligned}
\tag{10.11}
$$
其显式有限头预算为 $O(S^{2\delta})$。

实际代入仍只用有限线性式：
$$
X_1=s_{1n}+\alpha_1S^{\alpha_1-\delta}\mathsf V_n,
$$
$$
X_\nu=s_{\nu n}
+\alpha_\nu S^{\alpha_\nu-\delta}\mathsf V_n
+S^{\alpha_\nu-2\delta}\mathsf U_{\nu n}
\quad(\nu\ge2).
\tag{10.12}
$$
记 $p_{\nu n}=s_{\nu n}/S^{\alpha_\nu}$。
由 (2.1)，$p_n-\mathbf1=O((nS)^{-1})$。
定义有限多项式
$$
\mathfrak G_n(t,v)
=G(p_{1n}+\alpha_1t,\,
p_{2n}+\alpha_2t+v_2,\ldots).
$$
逐系数有
$$
\mathfrak G_n-\mathfrak G=O((nS)^{-1}).
\tag{10.13}
$$

实际原多项式为
$$
G(X)
=S^D\mathfrak G_n
(S^{-\delta}\mathsf V_n,S^{-2\delta}\mathsf U_n).
\tag{10.14}
$$
对 $\mathfrak G$ 的每个单项式，(10.4) 给归一系数因子
$$
S^{D-\delta j-2\delta|\beta|}\le1.
$$
对 (10.13) 的误差，每个反缩放因子不超过1，
故其全部系数最多为
$$
CS^{D-1}/n\longrightarrow0.
\tag{10.15}
$$
所以 (10.14) 的全部系数一致有界，而其常数
$G(s_n)=O(S^{D-1}/n)$ 趋于零。

这支付的是实际中心，不能只在形式点
$(S^{\alpha_\nu})_\nu$ 上验证 (10.4) 后忽略误差。
固定外层 $Q$ 后，整个 $Q(G(X))$ 的基础多项式同样有一致有界系数，
其常数趋于 $Q(0)\ne0$。

### 10.4 全部原 Bell 项与增长头根界

令 $K=Q\circ G$。
继续使用 §5 对原 $X_\nu$、原指数 $w$ 定义的全部混合累积量；
不在无界算子上执行 (10.6) 的非线性变换。

$K$ 的原单项式权均不超过 $(\deg Q)D$。
在 (10.12) 中，各 $X_\nu$ 的常数和变量系数均为
$O(S^{\alpha_\nu})$。
故每个固定原偏导 $(\partial^\beta K)(X)$ 的代入系数仍至多为
$CS^{(\deg Q)D}$。

选固定整数
$$
M\ge\max(1,D,(\deg Q)D).
$$
§5 的完整真实分解继续成立：
$$
S^M\kappa_\gamma=H_{\gamma n}+E_{\gamma n},
\qquad
H_{\gamma n}=\sum_{j<n}N_jB_{\gamma j,n},
$$
$$
\sum_{\gamma,j<n}\|B_{\gamma j,n}\|\le CS^M,\qquad
\max_\gamma\|E_{\gamma n}\|\to0.
\tag{10.16}
$$
其尾仍由 (5.7) 的有限对数幂乘
$n^{-1}+n^{-1/2}\|w_{\ge n}\|_2$ 支付；
$D$ 大于2不影响这个极限。
每个非基础 Bell 单项式至少含一个累积量，故全部偏导系数依
$S^{(\deg Q)D-Mh}\le1$ 被吸收。

由于 $2\delta=D/m\le D$，新的线性字母与 Bell 头合并后仍取 $A_n$ 为 $1$ 与全部头绝对量的最大值，满足
$
1\le A_n\le CS^M.
$$
把所有显式头及补集 first 字母置零，完整 Bell 常数按算子范数趋于
$Q(0)I$。全部一阶指数项和高阶混合 cumulant 均保留。

现在取
$$
\boxed{N_n=\lceil nS^{1-\delta}\rceil.}
\tag{10.17}
$$
由 (10.11)，
$$
N_n/n\to\infty,\qquad
\varepsilon_n\sqrt{N_n}
=O(S^{-(1-\delta)/2})\to0,\qquad
(n/N_n)\log A_n=O(S^{-(1-\delta)}\log S)\to0.
\tag{10.18}
$$
且 $A_ne^{-\gamma(2n)^3}\to0$。
§6 的完整根界因此适用，包括趋零的小算子常数字母；
不要求 $N_n$ 乘其范数趋零。

若原规范 $\mathcal P_K$ 有非零核，取其正交投影 $\Pi$，
在原共同伴随深域使用
$$
\mathscr T_n=I-\frac{P_K^*}{\overline{Q(0)}}.
$$
整个前 $n$ 位的柱投影 $\mathsf Q_n$ 保有全部所需有限混合词域，
故
$$
\Pi\mathsf Q_n=\Pi\mathscr T_n^{N_n}\mathsf Q_n.
$$
根界使右端范数趋零，而 $\mathsf Q_n\to I$ 强，矛盾。
原 $C$ 自伴性、指数图核心与 $B_w$ 单位随后给 (10.3)。
这里未知投影始终位于左侧，未与任一变化字母交换。

### 10.5 超过权次数二的真三模式例

取
$$
(\alpha_1,\alpha_2,\alpha_3)=(1,1/2,3/4)
$$
并令
$$
\boxed{
G(x_1,x_2,x_3)
=(x_1-x_2^2)^3+(x_3^2-x_2^3)^2.
}
\tag{10.19}
$$
第一括号的权为1，第二括号的权为 $3/2$，所以 $G$ 的权次数为
$D=3$。
在 $\mathbf1$ 处两括号均为零，第一项的普通阶至少3；
第二项的二阶齐次项为
$(2h_3-3h_2)^2\ne0$。
因此
$$
m=2,\qquad D=3<4=2m.
$$
强化定理给
$$
\boxed{
\left[
(u_1-u_{1/2}^2)^3+
(u_{3/4}^2-u_{1/2}^3)^2-\lambda
\right]^re^w
\text{ 对全部 }\lambda\ne0,r\ge1,w\text{ 循环}.
}
\tag{10.20}
$$
原中心常数仍完全由 (1.3) 固定。
这是对一个同时涉及三个原慢模式的完整点态向量重新排核，
不由括号中的各个共振因子单独循环来推断。

### 10.6 与旧临界 Newton 范围的重叠

对二模式权 $(1,1/k)$ 及
$G(x,y)=y^L(y^k-x)^m$，有
$D=L/k+m$，且在 $(1,1)$ 的消失重数正是 $m$。
条件 $D<2m$ 恰为 $L<km$，已经被同一完全居中幂稿的临界 Newton 补节覆盖。
本节将这部分明确扣为旧交集；新增在于一般有限权族及中心曲线上的高重横向相消，例如 (10.19)。

端点 $D=2m$ 时 (10.11) 不再给所需趋零的额外尾因子。
当前证明不宣称该端点失败，也不声称条件必要。
$Q(0)=0$、一般非齐次更深相消、无限模式、真正常见证上界及普通 ISP
仍不由本节完成。

