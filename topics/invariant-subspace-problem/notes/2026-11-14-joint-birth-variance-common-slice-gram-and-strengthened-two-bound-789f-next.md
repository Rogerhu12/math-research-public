# 出生与方差共同增长：三个切片的共同商 Gram 及真实加强常数二

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：全部定理已证明。** 本稿把 degree-two 条件 Gram 推广到完整 $\bigoplus_{j\le s}K_j$，并始终固定同一个中心 product 测度，同时条件到 $k-1,k,k+1$。两个真实低阶回归因此位于同一个共同商中，所付加强常数在下述联合区间中不随出生增长。

主要结论：任意正权的中心 saddle 方差 $V\ge2^{20}s^2$ 时，真实三塔加强式可取常数 $2$；原连续无限尾在 $k=s+n\ge2^{23}s^2$ 时满足该条件。原实际短核旗中 $s\approx k\approx q$，不在这个区间内。

使用 [degree-two 完整条件 Gram 稿](2026-11-14-conditioned-bernoulli-degree-two-full-gram-789f-next.md) 的逐位矩阵、概率主弧和尾弧方法，以及 R296 的完整回归二阶差。下文给出新次数依赖和实际创新的完整证明。

## 1. 三个相邻切片使用同一个 product

取独立 Bernoulli 变量，参数 $0<p_i<1$，并令

$$
N=\sum_iX_i,\qquad \sum_ip_i=k\in\mathbb Z,
\quad a_i=\sqrt{p_i(1-p_i)},\quad V=\sum_i a_i^2.
$$

以 $\chi_i=(X_i-p_i)/a_i$ 的乘积正交基定义 Fourier 次数空间 $\mathcal H_j$。记

$$
d_a=\sum_i a_iE_i,\qquad K_j(a)=\ker d_a\cap\mathcal H_j,
\qquad \mathcal E_{\le s}=\bigoplus_{j=0}^sK_j(a).
$$

注意这里 $a$ 与全部 $K_j(a)$ 都只取于**中心**参数，条件到相邻切片时不改变它们。令 $G_l$ 为同一 $\mathcal E_{\le s}$ 上的条件 Gram，

$$
\langle F,G_lH\rangle=\mathbb E[\overline F H\mid N=l].
$$

**定理 1.** 对每个整数 $s\ge1$，若

$$
\boxed{\quad V\ge2^{20}s^2,\qquad
\epsilon=\frac{128s}{\sqrt V}\le\frac18,\quad}
\tag{1.1}
$$

则同时对 $l=k-1,k,k+1$，

$$
\boxed{\quad \|G_l-I_{\mathcal E_{\le s}}\|\le\epsilon.\quad}
\tag{1.2}
$$

结论对任意有限位数成立，也适用于可数位且 $\sum p_i=k<\infty$。它保留全部次数之间的条件交叉块。

## 2. 主弧：次数依赖只有 $s/\sqrt V$

沿用逐位精确矩阵

$$
M_i(\theta)=
\begin{pmatrix}
\phi_i&a_i(e^{i\theta}-1)\\
a_i(e^{i\theta}-1)&p_i+(1-p_i)e^{i\theta}
\end{pmatrix},\quad
\phi_i=1-p_i+p_i e^{i\theta}.
$$

在 $|\theta|\le1/4$ 上置

$$
\beta_i=\frac{a_i(e^{i\theta}-1)}{\phi_i},\quad
\delta_i=\frac{e^{i\theta}}{\phi_i^2},\quad
 e_i=\beta_i-i\theta a_i.
$$

以 $c_\beta=\sum\beta_iE_i^*$ 表示同系数上升算子；它不被误称为 $d_\beta$ 的 Hilbert 伴随。完整 Gauss 分解及 $d_aP_{\mathcal E}=0$ 给

$$
P_{\mathcal E}e^{i\theta N}P_{\mathcal E}
=\phi(\theta)
P_{\mathcal E}\exp(c_e)D_\delta\exp(d_e)P_{\mathcal E}.
\tag{2.1}
$$

已有逐位界 $\|e\|_2\le2\sqrt V\theta^2$。在次数至多 $s$ 上，

$$
\|d_e\|\le\sqrt s\|e\|_2.
$$

主弧中 $|(\log\delta_i)'|\le4$，所以每个至多 $s$ 项的对角乘积满足 $|\log\delta_I|\le4s|\theta|$。记 (2.1) 中除去 $\phi$ 的压缩为 $H(\theta)$，则

$$
\boxed{
\|H(\theta)-I\|
\le\exp\{4s|\theta|+4\sqrt{sV}\theta^2\}-1.
}
\tag{2.2}
$$

因为 $|\phi(\theta)|\le e^{-V\theta^2/3}$，令 $u=\sqrt V\theta$、$\alpha=4s/\sqrt V$、$\beta=4\sqrt s/\sqrt V$。在 (1.1) 下，两者均至多 $1/256$。用

$$
e^w-1\le we^w\ (w\ge0),\qquad
\alpha|u|\le u^2/12+3\alpha^2
$$

并保留 Gaussian 衰减，主弧误差积分至多

$$
\begin{aligned}
\int_{-1/4}^{1/4}|\phi|\|H-I\|d\theta
&\le\frac2{\sqrt V}\int_{\mathbb R}
(\alpha|u|+\beta u^2)e^{-u^2/5}du\\
&\le\frac{10\alpha+30\beta}{\sqrt V}
\le\frac{160s}{V}.
\end{aligned}
\tag{2.3}
$$

这里 $e^{3\alpha^2}\le2$，且两项实积分分别至多 $5,15$。

## 3. 尾弧：完整原矩阵的正条目控制

若 $|I|,|J|\le s$，对称差至多有 $2s$ 位，其总 Bernoulli 方差至多 $s/2$。从原逐位矩阵直接得到

$$
|\langle\chi_I,e^{i\theta N}\chi_J\rangle|
\le e^{-2(V-s/2)\sin^2(\theta/2)}
\prod_{i\in I\triangle J}2a_i.
$$

右侧正条目核被

$$
P_{\le s}\exp(2c_a)\exp(2d_a)P_{\le s}
$$

逐条目支配，其范数至多 $e^{4\sqrt{sV}}$。所以

$$
\|P_{\le s}e^{i\theta N}P_{\le s}\|
\le\exp\{4\sqrt{sV}-2(V-s/2)\sin^2(\theta/2)\}.
\tag{3.1}
$$

在 (1.1) 及 $|\theta|\ge1/4$ 下，$4\sqrt{sV}\le V/256$；利用 $\sin(|\theta|/2)\ge|\theta|/\pi$，右侧至多 $e^{-V\theta^2/32}$。因此完整压缩和标量特征函数之差的尾弧积分至多

$$
\frac{256}{V}e^{-V/512}\le\frac1V.
\tag{3.2}
$$

这里始终使用原有界矩阵；即使某些 $\phi_i(\theta)$ 在尾弧为零，也不影响估计。

## 4. 相邻条件概率及可数极限

中心特征函数 $\psi=e^{-ik\theta}\phi$ 的主弧 Gaussian 近似给，对 $l=k-1,k,k+1$，

$$
\left|2\pi\mathbb P(N=l)
-\sqrt{2\pi/V}\,e^{-(l-k)^2/(2V)}\right|\le30/V.
$$

这是 degree-two 稿中同一 $L^1$ 误差乘上模为一的相位；故仍有

$$
\mathbb P(N=l)\ge1/(4\sqrt V).
\tag{4.1}
$$

Fourier 反演对三个 $l$ 只相差相位。由 (2.3)、(3.2)、(4.1)，

$$
\|G_l-I\|\le\frac{2(160s+1)}{\pi\sqrt V}
\le\frac{128s}{\sqrt V}.
$$

这证明定理 1。可数极限与 degree-two 稿相同：截断 odds 后调整一个共同参数保持整数均值，$a^{(M)}\to a$ 于 $\ell^2$。对于 $1\le j\le s$，完整 commutator 保证

$$
d_a d_a^*|_{\mathcal H_{j-1}}
\succeq\bigl(V-(j-1)/2\bigr)I,
$$

从而所有涉及的 primitive 投影在截断中强连续，三项条件 Gram 的统一估计传到无限空间。

## 5. 同一个完整商对三个切片都成立

相对于中心 product，$N-k=\sum a_i\chi_i$。对每个 $l=k-1,k,k+1$，逐最高次数分解给

$$
\boxed{
\mathscr P_{\le s}=\mathcal E_{\le s}\ \dotplus\
(N-l)\mathscr P_{\le s-1}.
}
\tag{5.1}
$$

证明是从最高次向下逐层减去 $(N-l)$ 的适当倍数：每层的最高上升都是同一个 $d_a^*$，而上一节的下界保证它满列秩。最后剩余的各齐次项都在 $K_j(a)$。条件 Gram 的严格下界又说明，$\mathcal E_{\le s}$ 在各切片上无额外核。

同理，全部低于 $s$ 次的函数，在三个切片中均可用**同一个** $\mathcal E_{\le s-1}$ 作唯一 canonical 代表。代表之间虽可能不同，但所在的 product 正交空间不变。对可数位使用这些有限次数闭子空间和相应有界三角消元；各下降、上升及对角次数算子均在固定最高次数上有界。

## 6. 任意正权的真实三塔统一估计

取正权 $b_i$、$z_i=b_i^2$，有限位数或 $\sum z_i<\infty$。令 $K=K_s(b)$，$k=s+n$、$n\ge1$，并选中心 saddle $t$ 满足

$$
p_i=\frac{tz_i}{1+tz_i},\qquad \sum_i p_i=k.
$$

有限情形取 R296 的合法相邻边；无限情形取既有完整 MP/回归定义。假设其 $V$ 满足 (1.1)。条件概率 $N=l$ 恰为原 $\mu_l$，三个相邻切片没有被换成别的权。

记真实 $C_j=\Gamma_{j,s}^{-1}$、$L_j=\Gamma_{j,s-1}$、

$$
B_n=C_{n+1}+\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*.
$$

R296 给

$$
Z_nf=(I-\Pi_{\le s-2}^{(k+1)})[\Phi_{s,f}-2q_k+q_{k-1}],
\quad \|Z_nf\|_{k+1}^2=\langle B_nf,f\rangle.
\tag{6.1}
$$

当 $s=1$ 时，所列低二次投影按约定为零。

### 6.1 保源纯化与同一源度量

在中心商中把 $\Phi_{s,f}$ 改成纯最高次 $F\in K_s(a)$，即

$$
\Phi_{s,f}-F\in(N-k)\mathscr P_{\le s-1}+\mathscr P_{\le s-1}.
\tag{6.2}
$$

它在各切片上仅改变低阶函数。对 $H=(N-k)L+L_0$，三个切片上的拟合分别等于 $-L+L_0,L_0,L+L_0$；任何齐次/canonical 代表之差均为 $(N-l)\mathscr P_{\le s-2}$，在新层被真实投影消去。因此 (6.2) 同时保留 $C_{n-1}$、$C_n$ 及完整 $B_n$。

对于 $s=1$，低阶空间是常数，(6.2) 中 $L,L_0$ 为常数，所列二阶差直接为零，无需附加投影。

源映射和其物理 Gram 明确为

$$
D_{t,s}e_I=\frac{t^{s/2}}{\prod_{i\in I}(1+tz_i)}e_I,
\quad T=P_{K_s(a)}D_{t,s}|_K,
\quad A=T^*T=(P_KD_{t,s}^{-2}|_K)^{-1}.
\tag{6.3}
$$

等式来自完整 nuisance 身份 $D_{t,s}d_b^*=d_a^*D_{t,s-1}$ 及完整 shorting；$F=Tf$，所以 $M:=\|F\|^2=\langle Af,f\rangle$。这是三个切片共同使用的原物理源度量。

### 6.2 两个真实回归只付二阶小费用

令 $q_l^{\rm can}\in\mathcal E_{\le s-1}$ 是 $F$ 在第 $l$ 层的真实最优低阶拟合。因为 product 内积中 $F\perp\mathcal E_{\le s-1}$，(1.2) 的完整交叉块界给

$$
\|q_l^{\rm can}\|\le\frac{\epsilon}{1-\epsilon}\|F\|
\qquad(l=k-1,k).
\tag{6.4}
$$

这是在同一个 product 空间中的向量范数，不是两个独立源的逆费用。两个 canonical 拟合代入 (6.1) 与原齐次拟合只差会被投掉的低二次项。又 $F$ 与它们 product 正交，故

$$
\|F-2q_k^{\rm can}+q_{k-1}^{\rm can}\|^2
\le\left[1+\frac{9\epsilon^2}{(1-\epsilon)^2}\right]M.
$$

新层真实正交投影是收缩，而其整个共同 Gram 仍满足 (1.2)。因此

$$
\boxed{
B_n\preceq(1+\epsilon)
\left[1+\frac{9\epsilon^2}{(1-\epsilon)^2}\right]e_{k+1}A.
}
\tag{6.5}
$$

同样的完整低阶 Schur 给

$$
C_{n-1}\preceq(1+\epsilon)e_{k-1}A,
\qquad C_n\succeq(1-\epsilon)e_kA.
\tag{6.6}
$$

### 6.3 保正确次序的共同合同

从 (6.6) 先取逆，再只对同一个合同算子平方：

$$
\begin{aligned}
C_n\Gamma_{n-1}C_n
&\succeq\frac1{(1+\epsilon)e_{k-1}}C_nA^{-1}C_n\\
&\succeq\frac{(1-\epsilon)^2}{1+\epsilon}
\frac{e_k^2}{e_{k-1}}A.
\end{aligned}
\tag{6.7}
$$

最后一步准确使用 $A^{-1/2}C_nA^{-1/2}\succeq(1-\epsilon)e_kI$，而非交换两个不同精度。设 $\rho=e_k^2/(e_{k-1}e_{k+1})\ge1$，由 (6.5)–(6.7) 得

$$
\boxed{
B_n\preceq\kappa(\epsilon,\rho)C_n\Gamma_{n-1}C_n,
\quad
\kappa(\epsilon,\rho)=\rho^{-1}
\left(\frac{1+\epsilon}{1-\epsilon}\right)^2
\left[1+\frac{9\epsilon^2}{(1-\epsilon)^2}\right].
}
\tag{6.8}
$$

在 $\epsilon\le1/8$ 下，

$$
\kappa(\epsilon,\rho)\le\frac{4698}{2401}<2.
\tag{6.9}
$$

这证明任意正权在所列联合方差区间内，完整三塔加强常数可统一取 $2$。特别普通相邻式也成立，但它只用了完整联合结果的一部分。

## 7. 原连续尾的实际联合窗口与条件数

对原 $z_j=j^{-4}$、$j\ge x\ge2$，已证 saddle 方差满足

$$
V(t)\ge\frac{m(t)-3}{4},\qquad m(t)=\sum_j\frac{t}{j^4+t}.
$$

因此

$$
\boxed{\quad k=s+n\ge2^{23}s^2\quad}
\tag{7.1}
$$

保证 (1.1)，从而整个原物理 $K_s$ 在这一共同增长区内有统一加强常数 $2$，且当 $s/\sqrt k\to0$ 时，(6.8) 相对于 $\rho^{-1}\le1$ 的乘子趋于一。

中心单高度还给

$$
\frac1{(1+\epsilon)e_k}P_KD_{t,s}^{-2}|_K
\preceq\Gamma_{n,s}\preceq
\frac1{(1-\epsilon)e_k}P_KD_{t,s}^{-2}|_K.
$$

取前 $2k$ 个原位，$t=(x+2k)^4$ 时它们每个的占据概率大于 $1/2$，故 $t_k\le(x+2k)^4$。由 (6.3) 的正对角范围，得到实际同源条件数

$$
\boxed{
\operatorname{cond}\Gamma_{n,s}
\le\frac{1+\epsilon}{1-\epsilon}\,2^{2s}(k+1)^{8s}.
}
\tag{7.2}
$$

它不是 graph 完整条件数，也没有丢掉原 $K_s$ 的物理压缩。

## 8. 与原 moving-birth 短核旗的准确比较

R271 的 [短核 canonical Fock 塔](../results/R271-appendix-short-canonical-fock-flags-and-q-over-d-prefix-window.md) 使用物理总孔层 $p$、primitive 出生 $s=p-r$ 和创建高度 $r<H$。原实际前缀中 $p=q+t$、$H\le d=2^m$，而 $q\ge4d$；见 [嵌套出生旗](../results/R271-appendix-nested-birth-flags-quotient-energy-and-complete-schur-defects.md) 的完整空间。

所以这些短列满足

$$
s=p-r\ge q-d+1\asymp q,\qquad k=p\asymp q,
\qquad n=r\le d.
$$

它们不满足 $k\ge2^{23}s^2$；事实上任何 Bernoulli 中都有 $V\le k$，所以无法通过改变尾起点来满足本稿的低次数阈值。不能把这里的 $s$ 替换成 head 维数 $d$。

因此本稿支付的是完整 all-birth 的高创建高度联合区，并给其真实三塔共同费用；原短抬高 moving-birth 区间、graph 跨出生 Schur、固定测试锚的未知速度仍需新的预算。这个范围限制来自准确变量对应，而不是单纯常数过大。
