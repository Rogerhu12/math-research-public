# R267 附录：同一双平坦来源的负 P 整函数在全部原旗上的单射与稠值

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整的实际范围结论。** 本文保持此前固定的原 Haar 尾 $C$、定量分母 $P$、双平坦分母 $Q$ 及唯一逆 $Q_{a,b}$，没有为未知旗另选来源。此前双圆相位只给整个双逆级数在全空间的忠实性；本文对其中真正无限的单变量负 $P$ 来源，证明全部原有限放大旗商上的单射与稠密值域。证明使用同一 $Q$ 的实际逆费用，不把全空间真空下界搬到未知子商，也不假设规范相位酉保持旗。

这没有构造 $Y^2=CQ^2$。一般二变量无限和的旗上范围仍然开放。

## 1. 固定原来源与同向量的下界

沿用[双平坦来源正文 §§1–4](R267-appendix-same-flat-denominator-all-inverse-powers-and-double-flat-source.md)。原尾 $C=A^{(m_0)}$，全部算子均在原 Haar 表示中，且

$$
C^aP^bQ_{a,b}=Q,\qquad
\|Q_{a,b}\|\le A_aM_b.
\tag{1.1}
$$

这里 $A_0=1$，$M_b=\prod_{\nu=1}^{b+1}\omega_{n_\nu}$，$n_\nu=2^{32+10\nu}$；$\omega_n$ 正是该正文 (4.5) 的有限实际预算。特别写

$$
D_b=Q_{0,b},\qquad P^bD_b=D_bP^b=Q,\qquad \|D_b\|\le M_b.
\tag{1.2}
$$

$P,Q,D_b$ 保持每个原有限放大闭不变旗，而且 $P,Q$ 在每个非零旗商上单射稠值。这个事实由各自的真实收缩强单位支付。

设 $\mathcal K=M/N$ 是任意这样的非零旗商。以下下标 $\mathcal K$ 都表示实际诱导算子，不是另一个模型。由 (1.2)，对每个 $x\in\mathcal K$，

$$
\boxed{
\|P_{\mathcal K}^{\,b}x\|
\ge \frac{\|Q_{\mathcal K}x\|}{M_b}
\qquad(b\ge0).
}
\tag{1.3}
$$

这是 $D_{b,\mathcal K}P_{\mathcal K}^b x=Q_{\mathcal K}x$ 的直接范数估计。若 $x\ne0$，分子严格正。它不要求未知旗含有原真空向量，也没有把 $\|P^b\|$ 的全空间下界当作限制的下界。

## 2. 已固定 M 的准确三级对数尺度

置

$$
\kappa=30\log2.
$$

存在只依赖固定原尾的常数 $c_*,C_*>0$，使对所有充分大整数 $b$，

$$
\boxed{
\exp(c_*2^{30b})\le \log M_b\le
\exp(C_*2^{30b}).
}
\tag{2.1}
$$

特别

$$
\log\log\log M_b=\kappa b+O_{m_0}(1).
\tag{2.2}
$$

这里只估计已经定义的 $M_b$，没有更换实际 $Q$ 或逆像。

**证明。** 写 $\alpha_\ell=e^{-L_\ell}$。原权给

$$
L_\ell=\frac{280}{3}16^\ell-90\,8^\ell+300\,2^\ell-\frac{850}{3}.
$$

$L_0=20$，而 $L_\ell-20\,16^\ell$ 从零开始，其相邻差为

$$
1100\,16^\ell-630\,8^\ell+300\,2^\ell>0.
$$

因此 $L_\ell\ge20\,16^\ell$。对原 $d_j=\|C^{2^j}\|$，结合已付上界得到

$$
20\,16^{m_0+j}\le-\log d_j\le500\,16^{m_0+j}.
\tag{2.3}
$$

原整数幂范数的二进乘积式及最高非零位给 $\|C^r\|\le e^{-r^4}$（$r\ge1$）。于是对 $t\ge0$，

$$
\mathscr R_C(t)=\sum_{r\ge0}t^r\|C^r\|
\le3\exp\bigl((\log^+t)^{4/3}\bigr).
\tag{2.4}
$$

例如对 $x=\log^+t$，用 $rx-r^4\le x^{4/3}-r^4/2$ 后求和即可。

记旧块
$q_\nu=256\nu^2$、
$m_\nu=1+256\sum_{i<\nu}i^2$、
$b_\nu=m_\nu+q_\nu-1$。
在原 $\omega_n$ 公式中，$L_n+64n-1=m_n+64n$。因 $\mathscr R_C\ge1$，由 (2.3)，

$$
\begin{aligned}
\log\omega_n
&\ge20\,16^{m_0+m_n+64n}
      -500n\,16^{m_0+m_n}\\
&\ge10\,16^{m_0+m_n+64n}.
\end{aligned}
\tag{2.5}
$$

第二行对 $n\ge1$ 成立。另一方面，原预解参数
$t_\nu=2q_\nu d_{m_\nu}/d_{b_\nu}$ 满足
$\log^+t_\nu\le\log(2q_\nu)+500\,16^{m_0+b_\nu}$。
把它代入 (2.4)，再代回原 $\omega_n$ 的全部有限乘积，使用
$m_n,b_n,m_n+64n=O(n^3)$，得到固定常数 $K_{m_0}$ 使

$$
\log\omega_n\le\exp(K_{m_0}n^3)\qquad(n\ge2).
\tag{2.6}
$$

而 $m_n\ge32n^3$ 对 $n\ge2$ 成立，所以 (2.5) 也给
$\log\omega_n\ge\exp(k n^3)$，其中 $k>0$ 固定。
最后

$$
n_{b+1}^3=2^{126}2^{30b},
$$

在 $M_b=\prod_{\nu\le b+1}\omega_{n_\nu}$ 中以下一个最大项作下界、全部项作上界，即得 (2.1)。$\square$

## 3. 对应整函数增长的两个 elementary estimates

在充分大 $R$ 上记

$$
\mathcal L(R)=(\log R)\log\log\log R.
$$

以下所有极限均为 $R\to\infty$。对固定整数 $s\ge1$，(2.1) 给

$$
\limsup\frac{\log^+\sum_{n\ge0}R^n/M_{sn}}{\mathcal L(R)}
\le\frac1{s\kappa}.
\tag{3.1}
$$

当 $s>1$ 时，同样有

$$
\limsup
\frac{\log^+\sum_{n\ge1}
n(1+R)^{n-1}M_{n-1}/M_{sn}}{\mathcal L(R)}
\le\frac1{s\kappa}.
\tag{3.2}
$$

另一方面，若一个 $H$-值整函数 $H(\lambda)=\sum h_n\lambda^n$ 满足

$$
\|h_n\|\ge c/M_{n+1}\qquad(n\ge0),\qquad c>0,
$$

则

$$
\liminf\frac{\log M_H(R)}{\mathcal L(R)}\ge\frac1\kappa,
\qquad
M_H(R)=\max_{|\lambda|=R}\|H(\lambda)\|.
\tag{3.3}
$$

这些估计可直接由整数切点证明。置 $x=\log R$。上界取
$n_+=(1+\epsilon)\log\log x/(s\kappa)$：
在此切点以上，(2.1) 的下界使 $\log M_{sn}$ 超过任意固定倍数的 $nx$；余和可用几何和控制。切点以下的项数只产生 $o(\mathcal L(R))$。对 (3.2)，因 $s>1$，有
$\log M_{n-1}=o(\log M_{sn})$，故相同论证适用。
下界用向量 Cauchy 估计 $M_H(R)\ge R^n\|h_n\|$，取
$n_-=\lfloor(1-\epsilon)\log\log x/\kappa\rfloor$。此时由 (2.1) 的上界，
$\log M_{n_-+1}=o(x)$，而
$n_-x/\mathcal L(R)\to(1-\epsilon)/\kappa$。
最后令 $\epsilon\downarrow0$。这保留了全 $R$ 的 liminf/limsup，没有假定在每个半径换一个来源向量。

## 4. 单次八倍预算已经支付所有旗的实际范围

**定理 4.1。** 设 $f(w)=\sum_{n\ge0}c_nw^n$ 非零，并满足同一个实际预算

$$
\boxed{\sum_{n\ge0}|c_n|M_{8n}<\infty.}
\tag{4.1}
$$

则级数

$$
B_f=\sum_{n\ge0}c_nD_n
=\sum_{n\ge0}c_nP^{-n}Q
\tag{4.2}
$$

范数绝对收敛，属于原 $C'$。它在每个非零原有限放大不变旗商上单射且值域稠密。

这里 $P^{-n}Q$ 指 (1.2) 的有界实际逆，绝非在整个空间上单独使用无界 $P^{-n}$。

**证明。** (2.1)、(4.1) 首先给 $f$ 整，(4.2) 也由 $\|D_n\|\le M_n$ 绝对收敛。定义同源向量差商算子

$$
G_f(\lambda)=
\sum_{n\ge1}c_n\sum_{j=0}^{n-1}\lambda^jD_{n-1-j}.
\tag{4.3}
$$

它在每个紧 $\lambda$ 集上范数绝对收敛。逐个有限和准确望远镜，再由范数收敛，得到

$$
\boxed{
(I-\lambda P)G_f(\lambda)
=P B_f-f(\lambda)P Q.
}
\tag{4.4}
$$

注意外面的 $P$ 和同一个 $Q$ 都不能删去。由 (3.1)–(3.2)，

$$
\limsup\frac{\log^+M_f(R)}{\mathcal L(R)}
\le\frac1{8\kappa},\qquad
\limsup\frac{\log^+M_{G_f}(R)}{\mathcal L(R)}
\le\frac1{8\kappa}.
\tag{4.5}
$$

这些全空间上界下降到任意原旗商。

反设在某个非零旗商 $\mathcal K$ 上有 $x\ne0$ 且
$B_{f,\mathcal K}x=0$。$P_{\mathcal K}$ 拟幂零，故

$$
H(\lambda)=P_{\mathcal K}
(I-\lambda P_{\mathcal K})^{-1}Q_{\mathcal K}x
$$

是 $\mathcal K$-值整函数。由 (4.4)，

$$
f(\lambda)H(\lambda)=-G_{f,\mathcal K}(\lambda)x.
\tag{4.6}
$$

其第 $n$ 个 Taylor 系数为
$P_{\mathcal K}^{n+1}Q_{\mathcal K}x$。将 (1.3) 用于同一个
$Q_{\mathcal K}x$，得

$$
\|P_{\mathcal K}^{n+1}Q_{\mathcal K}x\|
\ge\frac{\|Q_{\mathcal K}^{\,2}x\|}{M_{n+1}}.
\tag{4.7}
$$

$Q_{\mathcal K}$ 单射，所以分子严格正。因此 (3.3) 给

$$
\liminf\frac{\log M_H(R)}{\mathcal L(R)}\ge\frac1\kappa.
\tag{4.8}
$$

另一方面，标量 Jensen–Poisson 商估计从 (4.6) 给出

$$
\log M_H(R)
\le3\bigl(\log^+M_f(2R)+\log^+M_{G_f}(2R)\bigr)
+O_f(\log R)+O_x(1).
\tag{4.9}
$$

为付清原点零和向量域：若 $f$ 在原点零到 $m$ 阶，仅在该标量估计中写
$f(\lambda)=a_m\lambda^m f_0(\lambda)$、$f_0(0)=1$。
(4.6) 使右侧向量函数也可除以 $\lambda^m$。对每个单位连续线性泛函作用于 $H$ 后，Jensen 给
$\operatorname{mean}\log^-|f_0|\le
\operatorname{mean}\log^+|f_0|$。
半径 $2R$ 到 $R$ 的 Poisson 核至多为 $3$，所以得到 (4.9)，且右侧不依赖该泛函。取其上确界即是向量范数。没有把所有系数算子同时除以一个未支付的原幂。

由 (4.5)、$\mathcal L(2R)/\mathcal L(R)\to1$，(4.9) 给

$$
\limsup\frac{\log M_H(R)}{\mathcal L(R)}
\le\frac{6}{8\kappa}=\frac3{4\kappa},
$$

与 (4.8) 矛盾。所以全部旗上的核都为零。

最后若某个 $B_{f,\mathcal K}$ 值域不稠密，令其值域闭包为 $L$。
它是 $C_{\mathcal K}$ 不变闭空间，对应原来的一个更大下旗。
在非零商 $\mathcal K/L$ 上，$B_f$ 是零算子；这与刚证的全旗单射性矛盾。因此其值域稠密。$\square$

## 5. 同一来源的闭商与更一般单项式方向

旧双逆类中只含 $w$ 的元素满足全部预算
$\sum|c_n|M_{2^kn}<\infty$，特别满足 (4.1)。因而此前仅有的全空间忠实性，在这一整个单变量子类上现在已经提高为全部原旗的 quasiaffinity。

对该全尺度单变量代数的非零 $g$，定义实际最大商

$$
S_{f/g}=B_g^{-1}B_f,\qquad
D(S_{f/g})=\{x:B_fx\in\operatorname{Ran}B_g\}.
\tag{5.1}
$$

它是闭、稠密定义的算子。其图为有界核
$\{(x,y):B_fx=B_gy\}$，是原 $C^{(2)}$ 不变闭空间。
定理 4.1 也应用于这个图空间，因此对角 $B_g$ 在该图上的值域稠密。该值域包含于下列参数图，而下列参数图本身包含于最大图：

$$
\{(B_gx,B_fx):x\in H\}.
$$

故这是真实图核心。相同论证适用于每个原旗商，而非仅环境空间。
完整乘积关系仍是
$B_fB_g=Q B_{fg}$，来自原同源卷积；没有把 $P^{-1}$ 当成全域有界算子。

同一论证还支付原双逆类中的每个固定单项式方向。若 $a\ge0,b\ge1$ 为整数，置
$T=C^aP^b$。真实逆为 $Q_{an,bn}$，预算
$A_{an}M_{bn}$，且

$$
Q_{an,bn}T^n=Q.
$$

它的预算满足 (2.1) 的同类上下界，三级对数斜率为 $b\kappa$；$A_{an}$ 的增长比 $M_{bn}$ 小，不改变此斜率。
若 $\sum|c_n|\Lambda_{8(a+b)n}<\infty$，则相同差商证明给

$$
\sum_{n\ge0}c_nQ_{an,bn}
$$

在所有原旗上单射稠值。下界常数是 $1/(b\kappa)$，上界至多
$6/[8(a+b)\kappa]<1/(b\kappa)$。$b=0$ 的纯 $C^{-1}$ 方向已经由此前临界单变量来源支付，不在此重计。

## 6. 保留的实际缺口

本文没有对任意二变量 $F(z,w)$ 的整和 $B_F$ 得到全旗单射性。对未知旗，不能施用前稿双圆相位做 Fourier 取消，因为规范酉未证保持该旗。

新的证据来自同一真实逆预算和同一向量的 (1.3)、(4.7)。它关闭了负 $P$ 的全部单变量及固定单项式方向的范围缺口，并给它们的最大闭商实际参数核心；它不提供场外的平方分子，也不把这些范围结论称作普通 ISP 的完成。
