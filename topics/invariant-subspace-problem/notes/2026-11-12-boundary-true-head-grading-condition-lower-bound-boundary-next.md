# 实际有限头严格单链分级的指数条件数下界

日期：2026-11-12（UTC）。作者：boundary_next。状态：已证明，中间结论。

同期 [R249C](../results/R249-appendix-optimal-true-head-chain-similarity-cost.md) 已证明更强的最优主指数 $35/6$。本稿保留为独立迹法的补充；下文与 R249 上界的 $16/15$ 比较只描述本稿证明所得的强度，不是当前最优界。

本稿适用于两个实际慢边界算子 $T_N,T_Y$，保留真实进位。
它证明：不仅 [R249](../results/R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) 的某个特定构造，
而且**任何把实际有限头化为非零加权单 Jordan 链的相似**，都必须支付正的 $16^m$ 阶对数条件数。

令 $d=2^m$、$m\ge3$。若
$$
T_m=S_mJ_{\boldsymbol\lambda}S_m^{-1},
\qquad
J_{\boldsymbol\lambda}e_i=\lambda_i e_{i-1}\ (1\le i<d),
\quad
J_{\boldsymbol\lambda}e_0=0,
\quad \lambda_i\ne0,
$$
并记 $\kappa_m=\|S_m\|\|S_m^{-1}\|$，则
$$
\boxed{
\kappa_m\ge
\frac{(2^{m-1}-1)/(26m^2\eta_{m-2})-1}{2^m-1}.
}
\tag{0.1}
$$
特别，
$$
\boxed{
\liminf_{m\to\infty}\frac{\log\kappa_m}{16^m}
\ge\frac{175}{32}.
}
\tag{0.2}
$$
R249 已构造
$\log\kappa_m\le(35/6+o(1))16^m$，
而
$$
\frac{35/6}{175/32}=\frac{16}{15}.
\tag{0.3}
$$
因此仅靠改选链权、列缩放或相似矩阵，不能把这一严格单链分级的条件数改为 $\exp(o(16^m))$。
本稿不把该下界解释成所有可能能量方法的障碍，也不据此决定 $N=M$。

## 1. 实际有限头的两个准确结构

沿用边界标准基与权：
$$
Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),\qquad Be_0=0,
$$
$$
-\log\alpha_j
=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
$$
令
$$
\mathcal F_m=\operatorname{span}\{e_0,\ldots,e_{2^m-1}\},
\qquad B_m=B|_{\mathcal F_m},
\qquad T_m=T|_{\mathcal F_m}.
$$
由于所有实际项都是正次 $B$ 幂或其 Cayley 函数，$\mathcal F_m$ 确为不变空间。

R249 §1 的真实有限芽给
$$
T_m=f_m(B_m),\qquad f_m(0)=0,\qquad f'_m(0)=\beta=e^{20}\ne0.
\tag{1.1}
$$
在有限截断环中写
$$
f_m(z)=\beta z\,u_m(z),\qquad u_m(0)=1.
$$
因 $B_m$ 幂零，$u_m(B_m)$ 有界可逆，并与 $B_m$ 交换。故对 $1\le k\le d$，
$$
\boxed{
\ker T_m^k=\ker B_m^k
=\operatorname{span}\{e_0,\ldots,e_{k-1}\}.
}
\tag{1.2}
$$
此外，
$$
\boxed{
(T_m)_{i,i+1}=\beta\alpha_{v_2(i+1)}\ne0
\qquad(0\le i<d-1).
}
\tag{1.3}
$$
高次 $B_m$ 项不能贡献第一条超对角线。

接着令
$$
L=2^{m-1},\qquad a=a_{m-1}=\frac1{m^2},
\qquad H=T_{m-1}.
$$
按最高物理位拆分 $\mathcal F_m=\mathbb C^L\oplus\mathbb C^L$。
两个对角块中，所有内部移位权都相同，所以准确有
$$
\boxed{
T_m=
\begin{pmatrix}
H&aI_L+R\\
0&H
\end{pmatrix}.
}
\tag{1.4}
$$
这里最高位 $N_{m-1}^{[m]}$ 恰为
$\begin{pmatrix}0&I_L\\0&0\end{pmatrix}$。
它的平方为零，故最高位 Cayley 项也恰等于它，而不是近似。

矩阵 $R$ 包含全部更低位跨越最高位分界的实际进位。
[R249 §6](../results/R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)
已付清全空间真实头加纯尾误差
$$
\|T-T^{[m-1]}\|\le26\eta_{m-2}.
$$
把该等式压到实际不变空间 $\mathcal F_m$，高于最高位的全部删除项均为零，
而 $T^{[m-1]}|_{\mathcal F_m}$ 恰是
$\begin{pmatrix}H&aI_L\\0&H\end{pmatrix}$。
因此
$$
\boxed{\|R\|\le26\eta_{m-2}.}
\tag{1.5}
$$
这一步同时适用于 $N$ 与 $Y$ 两个模型，包含低位 Cayley 分母的全部真实贡献。
没有把其余进位删去，也没有要求 $R$ 为三角矩阵或要求 $\operatorname{tr}R=0$。

实际权给
$$
-\log\eta_j=1400\,16^j-630\,8^j+300\,2^j.
$$
所以
$$
\boxed{
-\log\eta_{m-2}
=\frac{175}{32}d^4-\frac{315}{32}d^3+75d.
}
\tag{1.6}
$$

## 2. 任何精确次数算子必须保留同一旗

先不选相似矩阵。
设 $Z$ 是任意 $d$ 阶矩阵，满足
$$
[T_m,Z]=T_m.
\tag{2.1}
$$
这里 $[U,V]=UV-VU$。

由有限矩阵乘法归纳，
$$
[T_m^k,Z]=kT_m^k.
\tag{2.2}
$$
若 $x\in\ker T_m^k$，则
$$
T_m^kZx=ZT_m^kx+kT_m^kx=0.
$$
故 $Z$ 保持 (1.2) 中的每一个标准旗子空间。
也就是说，**$Z$ 在原物理整数基下必为上三角矩阵**，并非只在其自身链基下三角。

利用 $T_m$ 与 $Z$ 都上三角且 $T_m$ 对角为零，(2.1) 的第 $(i,i+1)$ 个矩阵元为
$$
(T_m)_{i,i+1}(Z_{i+1,i+1}-Z_{ii})=(T_m)_{i,i+1}.
$$
由 (1.3)，
$$
\boxed{Z_{i+1,i+1}-Z_{ii}=1.}
\tag{2.3}
$$
因而存在 $\zeta\in\mathbb C$，使
$$
Z_{ii}=\zeta+i.
\tag{2.4}
$$

按与 (1.4) 相同的最高位拆分，写
$$
Z=
\begin{pmatrix}
Z_0&K\\
0&Z_1
\end{pmatrix},
\qquad
\Delta=Z_1-Z_0.
$$
两块都是原空间的正交压缩。
由 (2.4)，$\Delta$ 的每个对角元恰为 $L$，所以
$$
\boxed{\operatorname{tr}\Delta=L^2.}
\tag{2.5}
$$
这里不声称 $\Delta=LI_L$；其严格上三角部分可能很大，且会被完整保留。

## 3. 最高位块的迹恒等式

将 (1.4) 与上面的 $Z$ 代入 (2.1)。
上右块给
$$
HK-KH+(aI_L+R)Z_1-Z_0(aI_L+R)=aI_L+R.
\tag{3.1}
$$
对这个有限 $L$ 阶矩阵取迹。
$\operatorname{tr}(HK-KH)=0$，而迹的循环性给
$$
\operatorname{tr}(RZ_1-Z_0R)=\operatorname{tr}(R\Delta).
$$
再使用 (2.5)，得到准确等式
$$
aL^2+\operatorname{tr}(R\Delta)=aL+\operatorname{tr}R,
$$
即
$$
\boxed{
\operatorname{tr}\bigl(R(\Delta-I_L)\bigr)
=-aL(L-1).
}
\tag{3.2}
$$
这正是不可忽略的最高位进位所承担的量。
若形式上删除 $R$，右侧仍不为零，所以将不再可能同时拥有完整长度 $d$ 的真实旗和精确一次分级。

对任意 $\xi\in\mathbb C$，$\Delta$ 在 $Z\mapsto Z-\xi I_d$ 下不变。
又有
$$
\|\Delta-I_L\|
\le\|Z_1-\xi I_L\|+\|Z_0-\xi I_L\|+1
\le2\|Z-\xi I_d\|+1.
$$
有限维迹界 $|\operatorname{tr}A|\le L\|A\|$ 因而给
$$
aL(L-1)
\le L\|R\|\bigl(2\|Z-\xi I_d\|+1\bigr).
\tag{3.3}
$$
特别，$R\ne0$，且
$$
\boxed{
\inf_{\xi\in\mathbb C}\|Z-\xi I_d\|
\ge\frac12\left(\frac{a(L-1)}{\|R\|}-1\right)
\ge\frac12\left(\frac{L-1}{26m^2\eta_{m-2}}-1\right).
}
\tag{3.4}
$$
这是一条直接关于任何精确次数算子的下界，不依赖选取哪种 Jordan 相似。

## 4. 转为任意加权单链相似的条件数下界

现在假设
$$
T_m=S_mJ_{\boldsymbol\lambda}S_m^{-1},
\qquad \lambda_i\ne0.
$$
链权可以随 $i,m$ 改变，可以复数，也不要求彼此相等。
令
$$
Q_d=\operatorname{diag}\left(
-\frac{d-1}{2},\,1-\frac{d-1}{2},\,\ldots,\,
d-1-\frac{d-1}{2}\right).
$$
因为每个非零链项都严格降低一个链次数，
$$
[J_{\boldsymbol\lambda},Q_d]=J_{\boldsymbol\lambda},
\qquad \|Q_d\|=\frac{d-1}{2}.
$$
于是
$$
Z=S_mQ_dS_m^{-1}
$$
满足 (2.1)，而
$$
\|Z\|\le\kappa_m\frac{d-1}{2}.
\tag{4.1}
$$
将 $\xi=0$ 的 (3.3) 与 (4.1) 合并：
$$
a(L-1)
\le\|R\|\bigl(\kappa_m(d-1)+1\bigr).
$$
因而
$$
\kappa_m\ge
\frac{a(L-1)/\|R\|-1}{d-1}
\ge
\frac{(L-1)/(26m^2\eta_{m-2})-1}{d-1}.
\tag{4.2}
$$
这就是 (0.1)。

由于 $(L-1)/(d-1)\to1/2$，以及 $\eta_{m-2}$ 超指数趋零，
取对数给
$$
\log\kappa_m
\ge-\log\eta_{m-2}-2\log m-O(1).
\tag{4.3}
$$
结合 (1.6)，
$$
\boxed{
\log\kappa_m
\ge
\frac{175}{32}d^4-\frac{315}{32}d^3+75d
-2\log m-O(1).
}
\tag{4.4}
$$
因此 (0.2) 成立。
$O(1)$ 只是 (4.2) 中固定数值常数与趋于 $1/2$ 的维数比，不隐含随 $m$ 增长的预算。

## 5. 与已证上界的准确比较

对每个 $m$，令
$$
\kappa_m^{\mathrm{opt}}
=\inf\{\|S\|\|S^{-1}\|:
T_m=SJ_{\boldsymbol\lambda}S^{-1},\ \lambda_i\ne0\}.
$$
R249 已给这个集合中的一条明确常权链，所以它非空。
本稿的 (4.2) 对集合中每个成员成立，故
$$
\boxed{
\frac{175}{32}
\le
\liminf_{m\to\infty}
 \frac{\log\kappa_m^{\mathrm{opt}}}{16^m}
\le
\limsup_{m\to\infty}
 \frac{\log\kappa_m^{\mathrm{opt}}}{16^m}
\le\frac{35}{6}.
}
\tag{5.1}
$$
没有要求最优相似实际达到这个下确界。

上下主常数的比为 $16/15$。
因此 R249 的平衡构造已在这个明确问题上距离任意加权单链的最佳可能主常数至多一个 $16/15$ 因子。
这不是声明精确最优常数已求出，也不是证明所有更一般分级模型都必须支付同一条件数。

## 6. 对边界缺陷研究的范围

以下路线已被本稿严格排除：

- 保持真实 $T_m$ 不变；
- 仍把它化成一条每次严格降低一个次数的非零加权单链；
- 只通过更好的相似矩阵、链权或列缩放，把条件数降到 $\exp(o(16^m))$。

精确次数算子本身已有 (3.4) 的大范数，不能只隐藏相似矩阵而略去该代价。

以下事项没有由本稿决定：

- 是否能用实际缺陷向量的额外结构减轻该条件数在某个特定配对中的作用；
- 是否存在不经上述严格单链相似的其他正能量或值域方法；
- $M\ominus\overline{BM}$ 是否为零；
- 原 Haar 候选的普通不变格及普通 Hilbert ISP。

因此后续仍应研究真实缺陷的窗口能量、特殊配对或核内正则密度。
本稿给的是一个实际有限头的必要代价，不能把它当成 $N=M$ 的反例。

## 引用

- [R249，真实有限头平衡相似](../results/R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)，尤其 §§1、4、6。
- [R249移动头能量附录](../results/R249-appendix-moving-head-energy-flux-and-defect-tail-rates.md)，说明为何条件数必须进入未知向量的尾项。
- [R239真实头与纯分级形式像](../results/R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)，记录此前的相似及纯模型适用边界。
