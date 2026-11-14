# R239 附录：原线性大窗口、全整数最小修复能量与准确对数权常数

日期：2026-11-13。作者：Astra-ISP-0c / boundary_next；boundary_resume 独立复核。完整证明见[逐步稿](../notes/2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md)。

[R254L](R254-appendix-factorial-preimages-carry-jets-and-large-low-output-windows.md) 的阶乘原像与 [R271](R271-increasing-head-actual-lift-and-log-four-thirds-stable-range.md) 的逐头平方提升已经证明 $4/3$ 次对数权饱和。本附录独立处理原线性模型，将头长按每个整数窗口选择，改进常数并给原 Hilbert 最小能量的加权覆盖准则；不重复登记既有权阶。

## 1. 结果

对原两个边界 $T=T_N,T_Y$，记 $M=\ker T$、$N=\overline{BM}$、$D_{\rm def}=M\ominus N$，$\mathcal N$ 为原全部物理孔次数。令
$$
K_*=3(16/770)^{1/3}=0.8247664896711043\ldots.
$$
则
$$
\boxed{
M\cap\operatorname{Dom}\exp\!\left(c[\log(2+\mathcal N)]^{4/3}\right)
\subseteq N\qquad(c>K_*).
}
$$
若 $0\ne w\in D_{\rm def}$，则原全部孔尾满足
$$
\boxed{
\limsup_{Q\to\infty}
\frac{\log(\|w\|/\tau_Q(w))}{[\log(Q+2)]^{4/3}}
\le K_*/2.
}
$$
这是缺陷所需的慢尾条件，临界 $c=K_*$ 与无权 $N=M$ 仍未证明。

## 2. 原线性大窗口与准确实际提升

头保留原物理位 $0,\ldots,m-1$。取 $m\ge5$、$d=2^m$，
$$
L_m=A_m+D_m,\qquad
D_m=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad
A_m^d=0,\quad\|A_m\|\le6.
$$
原位号给
$$
\|T-L_m\|\le26\eta_{m-1},\qquad
-\log\eta_{m-1}
=\frac{175}{2}d^4-\frac{315}{4}d^3+150d\ge80d^4.
$$
不能用删首位平方模型的进位常数。

对
$$
4d\le q\le e^{d^3/4},\qquad
R=512\sqrt{q+d+1}(m+q+d+2)^{3/2},
$$
相容原像 $DR_t=R_{t-1}$ 的阶乘细界为
$$
\|R_tf\|\le\frac{R^t}{t!}\mathcal U_R(f),\qquad
\mathcal U_R(f)=\sum_{k\ge0}\frac{R^k}{k!}\|D^kf\|.
$$
局部实际壳 $K_\ell=L_{\ell+1}-L_\ell$ 满足
$$
\|K_\ell\|_{\operatorname{ad}D,R}
\le52\eta_{\ell-1}\prod_{j=m}^{\ell}(1+R(j+1)^{-2})^2.
$$
$\log(2+R)\le d^3$ 时，全部壳和给 $\|L_m-T\|_{\operatorname{ad}D,R}\le e^{-79d^4}$。真实核方程的有限头递推使
$$
\mathcal U_R(w)\le2H_m(R)\|w\|,\qquad
H_m(R)=\sum_{j<d}\frac{R^j}{j!}\|A_m^j\|,\quad
\log H_m(R)\le2d^4.
$$
这是核上的吸收；固定 $R$ 的范数虽与 Hilbert 范数等价，有限源右逆没有被扩大成全空间有界右逆。

令 $v_{m,q}$ 为 $w\in M$ 到
$$
\mathcal H_{\le q}^{(m)}\cap\ker(P_{\le q-1}L_m)
$$
的正交投影。阶乘相容逆修复完整低输出，得到
$$
\|v_{m,q}-P_{\le q}w\|\le e^{-74d^4}\|w\|,\qquad
\|v_{m,q}\|\le\|w\|.
$$
高尾只付 $\tau_q(w)$。残量 $r=L_mv$ 单独在第 $q$ 层，且
$$
D^kr=(-1)^kA_m^{k+1}v_{q-k},\qquad D^dv=D^dr=0.
$$
取 $c_{m,q}=\sum_{j<d}(-A_m)^jR_{j+1}r$，则
$$
L_m(v-c_{m,q})=0,\quad
c_{m,q}\in\mathcal H_{[q+1,q+d]}^{(m)},\quad D^dc_{m,q}=0.
$$

原线性逐头提升另行付清：旧头 $p$、$z=2^p$ 的核向量满足
$D_{p+1}^{z+1}k=0$。新头的相容逆成本不超过 $e^{3z^4}$，而真实残量不超过 $52\eta_{p-1}\|k\|$。每步准确进入新核后重置核阶，完整迭代给
$$
\Lambda^{\rm lin,inc}_{m,Q}:
\ker L_m\cap\mathcal H_{\le Q}^{(m)}\to N,\qquad
\|\Lambda k-k\|\le e^{-75d^4}\|k\|,
\quad Q\le e^{d^3/3}.
$$
迭代差的原次数最多线性增至 $Q_0+5d_n$，范数则以 $e^{-76d_n^4}$ 衰减。因此极限在每个正指数次数域；用旧 $M\cap X_3\subseteq N$，没有循环使用本稿对数权结论。

## 3. 一次头预算与全整数参数

令 $\gamma=770/256$。真实头幂
$$
\|A_m^n\|\le6^ne^{-\gamma(n-m)_+^4}
$$
作用于合并后的 $A_m^{j+k+1}$。由
$$
\sup_{s\ge0}(\Theta s-\gamma s^4)
=\frac3{4^{4/3}\gamma^{1/3}}\Theta^{4/3}
$$
得到
$$
F(m,q)=2\log d+m\Theta+
\frac3{4^{4/3}\gamma^{1/3}}\Theta^{4/3},
\qquad \Theta=\log(12R),
$$
$$
\|c_{m,q}\|\le e^{F(m,q)}\tau_{q-d}(w)+e^{-72d^4}\|w\|,
\qquad F(m,q)\le2d^4.
$$
支付完整修复范数后仍有 $n_{m,q}\in N$，且
$$
\|n_{m,q}-(v_{m,q}-c_{m,q})\|\le e^{-72d^4}\|w\|.
$$

对每个整数 $q\ge128$ 取
$$
m(q)=\max\!\left(5,\left\lceil
\frac{\log(4\log(q+2))}{3\log2}\right\rceil\right),\qquad
d(q)=2^{m(q)}.
$$
准确有 $4d(q)\le q\le e^{d(q)^3/4}$，而
$d(q)\asymp(\log q)^{1/3}$、$m(q)=O(\log\log q)$。故
$$
F(m(q),q)=(K_*+o(1))(\log q)^{4/3}.
$$
带权尾使修复趋零，证明饱和结论。缺陷情形由
$\langle c_{m(q),q},w\rangle\to\|w\|^2$ 得
$$
e^{F(m(q),q)}\tau_{q-d(q)}(w)^2\ge\|w\|^2/4.
$$
对任意大 $Q$ 取 $q=2Q$，即得全序列 $K_*/2$；不付稀疏网格的额外 $16$ 倍。

## 4. 每个整数层的原最小修复能量

对同一 $v_q=v_{m(q),q}$，在原 Hilbert 范数中定义
$$
\lambda_q(w)=
\min\{\|c\|:c\in\mathcal H_{[q+1,q+d(q)]}^{(m(q))},
\ L_{m(q)}c=L_{m(q)}v_q,\ D_{m(q)}^{d(q)}c=0\}.
$$
该闭仿射集非空，唯一最小元 $c_q^{\min}$ 有相同候选上界和实际提升。置 $\ell_q=d(q)+m(q)$，其原全部孔支撑在
$$
I_q=[q+1,q+\ell_q].
$$
这些窗口不必正交，但准确有
$$
\sup_p\sum_{q:p\in I_q}\ell_q^{-1}\le2.
$$
证明只用 $\ell_q\le3q/8$、$p\in I_q\Rightarrow q<p<2q$，以及
$\ell_p\le2\ell_q$。因此加权 Cauchy–Schwarz 和 Bessel 分别给
$$
\boxed{
\sum_{q\ge128}\frac1{\ell_q(1+\lambda_q(w)^2)}=\infty
\quad\Longrightarrow\quad w\in N,
}
$$
$$
\boxed{
0\ne w\in D_{\rm def}\quad\Longrightarrow\quad
\sum_{q\ge Q}\frac1{\ell_q\lambda_q(w)^2}
\le\frac{8\tau_Q(w)^2}{\|w\|^4}
\quad(Q\ \text{充分大}).
}
$$
充分性使用提升后向量的有限正凸平均和统一趋零余项；没有假设无限修复级数条件收敛。

特别，若真实最小能量最终满足
$$
\lambda_q(w)^2=O\!\left(q(\log q)^{2/3}\log\log q\right),
$$
则上述级数由 $\sum(q\log q\log\log q)^{-1}=\infty$ 发散。非零真缺陷必违反这个最终统一增长界。

现有一般候选仍含 $e^{(K_*+o(1))(\log q)^{4/3}}$，不能从普通 Hilbert 尾推出倒数能量发散。继续要证明的是特殊残量的最小修复量本身；环境联合能量或任意昂贵原像均不能替代它。无权 $N=M$ 和普通 ISP 保持开放。
