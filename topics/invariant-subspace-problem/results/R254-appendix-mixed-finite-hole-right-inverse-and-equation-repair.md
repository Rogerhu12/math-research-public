# R254 第四附录：保留全部混合项的低孔右逆和方程修复

日期：2026-11-13（UTC）。作者：boundary。状态：已证明的中间引理；root已全文核验真实头过滤、有限孔域及预算；不声称 $W=0$。

本稿续接 [R254 第三附录](../results/R254-appendix-high-order-pure-tail-kernel-constraint-without-similarity.md)，只使用其中已经逐层证明的纯删除右逆。目的在于准确处理 $P_m=D^2+Q_m$ 中的混合项，而不把 $Q_m$ 误换成只作用于头的矩阵。

## 1. 真实平方符号与混合有限头

沿用 R254 的首位消元记号。去掉原第 $0$ 位后的空间分解成前 $m$ 个尾位与余下纯尾，$d=2^m$。这些尾位是原物理位 $1,\ldots,m$。置
$$
b_j=(j+2)^{-2},\qquad
A=\sum_{j\ge0}b_j\bar X_j,\qquad
A^{[m]}=A_m+D,\qquad
D=\sum_{j\ge m}b_jE_j.
$$
$\bar X_j$ 分别为真实 $\bar N_j$ 或 $\bar Y_j$；$C$ 是去掉首位后归一化的真实后移，$C_m$ 为其前 $m$ 位真实头。
令 $\eta=\eta_0=e^{-1070}$。实际平方核为
$$
K=\ker(Z^2-\eta C),\qquad
Z=A \quad(N),\qquad Z=A(I+A)^{-1}\quad(Y).
$$
对 $N$ 型取 $P=A^2-\eta C$；对 $Y$ 型取
$$
P=A^2-\eta C(I+A)^2.
$$
后一式是乘实际有界可逆因子 $(I+A)^2$ 后得到的同核符号。此处只用 $\ker P=K$，不擅自保持形式伴随源。

混合模型为
$$
P_m=(A_m+D)^2-\eta C_m\quad(N),
$$
$$
P_m=(A_m+D)^2-\eta C_m(I+A_m+D)^2\quad(Y).
$$
R254 第三附录已经给出真实界
$$
\|P-P_m\|\le36\eta_m,\qquad
-\log\eta_m=1400d^4-630d^3+300d,
\tag{1.1}
$$
以及
$$
P_m=D^2+Q_m,\qquad \|Q_m\|<\tfrac12.
\tag{1.2}
$$

比仅写 $Q_m^d=0$ 更有用的是其头过滤性质。由于 $A_m$ 是 $C_m$ 的零常数多项式，
$$
Q_m=\sum_{\ell=1}^{d-1}C_m^\ell R_{\ell,m}(D)
\tag{1.3}
$$
为有限和；每个 $R_{\ell,m}$ 是次数不超过 $2$ 的尾多项式。所有系数真正有界。对 $Y$ 型，$-\eta C_m(I+A_m+D)^2$ 也满足同样性质。

因此 $Q_m$ 严格降低至少一次头链指标，而在尾孔次数上只可能降低 $0,1,2$。这里保留了 $2A_mD$ 及所有 $Y$ 型混合项。

## 2. 纯二次删除的有限孔右逆

令 $\mathcal H_q$ 为纯高尾的完整 $q$ 孔层，位置不作有限性限制。
R254 第三附录已经构造实际算子
$$
G_q:\mathcal H_q\longrightarrow\mathcal H_{q+1},
\qquad DG_q=I,
$$
满足
$$
\|G_q\|\le18(m+q+2)^{3/2}e^{7q}.
\tag{2.1}
$$
这些右逆不必保持有限位置支撑，本稿也不使用该性质。

定义逐层的二次右逆
$$
H_q=G_{q+1}G_q:\mathcal H_q\longrightarrow\mathcal H_{q+2}.
$$
准确有 $D^2H_q=I$，且
$$
\|H_q\|
\le324(m+q+3)^3 e^{14q+7}
=:L_{m,q}.
\tag{2.2}
$$
令 $H$ 表示这些层算子的代数直和，并张量头恒等。
它在每个有限尾孔空间 $\mathcal H_{\le q}$ 上都是实际有界算子，
$$
D^2H=I,\qquad
H\mathcal H_{\le q}\subseteq\mathcal H_{\le q+2},\qquad
\|H|_{\mathcal H_{\le q}}\|\le L_{m,q}.
\tag{2.3}
$$
末式由不同输入次数的输出正交及 $L_{m,q}$ 递增得到。没有把 $H$ 当成全空间有界算子。

因为 $H$ 只作用于尾，它与 $C_m$ 交换。尽管一般不与 $R_{\ell,m}(D)$ 交换，(1.3) 仍保证
$$
\boxed{(Q_mH)^d=0}
\tag{2.4}
$$
于所有有限孔输入上成立。展开任意 $d$ 个因子时，每项都含总幂次至少 $d$ 的 $C_m$；所有尾因子与 $C_m$ 交换，而 $C_m^d=0$。这一步不需要把 $Q_m$ 与 $H$ 交换。

## 3. 保留混合项的真实有限孔右逆

对有限孔输入定义
$$
\boxed{
\mathcal R_m
=H\sum_{k=0}^{d-1}(-Q_mH)^k.
}
\tag{3.1}
$$
有限项中的每次运算都有实际 Hilbert 意义，且
$$
P_mH=I+Q_mH.
$$
由 (2.4) 的有限几何恒等式，
$$
\boxed{P_m\mathcal R_m=I.}
\tag{3.2}
$$
特别，这不是只到投影后的右逆，也不是把某个形式级数作收敛断言。

若输入尾孔数不超过 $q$，第 $k$ 项的输出孔数不超过 $q+2(k+1)$，所以
$$
\boxed{
\mathcal R_m\mathcal H_{\le q}
\subseteq\mathcal H_{\le q+2d}.
}
\tag{3.3}
$$
由于每个 $Q_m$ 的范数小于 $1/2$，
$$
\|\mathcal R_m|_{\mathcal H_{\le q}}\|
\le\sum_{k=0}^{d-1}2^{-k}
 \prod_{j=0}^{k}L_{m,q+2j}.
$$
所有 $L_{m,s}\ge2$，故各项的上述正上界递增，进而
$$
\|\mathcal R_m|_{\mathcal H_{\le q}}\|
\le d\,2^{1-d}\prod_{j=0}^{d-1}L_{m,q+2j}.
\tag{3.4}
$$
一个便于使用的无头逆权预算是
$$
\boxed{
\log\|\mathcal R_m|_{\mathcal H_{\le q}}\|
\le
14dq+14d^2+
3d\log(m+q+2d+1)+d\log324+\log d.
}
\tag{3.5}
$$
确实，指数项求和为 $14dq+14d(d-1)+7d$；
丢掉负项 $-7d-(d-1)\log2$ 即得 (3.5)。

这里没有出现任何有限头 Jordan 相似条件数，也没有除以头权 $\alpha_j$。代价来自完整纯尾层上的右逆，而混合项的有限性来自真实头过滤。

## 4. 对实际核向量修复全部低孔模型方程

记 $P_{\le q}^{(m)}$ 为纯高尾孔数不超过 $q$ 的正交投影；它不截断有限头。
对 $u\in K=\ker P$ 定义
$$
r_{m,q}=P_{\le q}^{(m)}P_mu
=P_{\le q}^{(m)}(P_m-P)u,
$$
$$
v_{m,q}=u-\mathcal R_m r_{m,q}.
\tag{4.1}
$$
由 (3.2)，
$$
P_mv_{m,q}
=(I-P_{\le q}^{(m)})P_mu.
$$
因此
$$
\boxed{P_{\le q}^{(m)}P_mv_{m,q}=0.}
\tag{4.2}
$$
并且
$$
\boxed{
\|u-v_{m,q}\|
\le36\eta_m\,
 \|\mathcal R_m|_{\mathcal H_{\le q}}\|\,\|u\|.
}
\tag{4.3}
$$
修正向量的尾孔数不超过 $q+2d$，故
$$
P_{>q+2d}^{(m)}v_{m,q}
=P_{>q+2d}^{(m)}u.
\tag{4.4}
$$
这是一条实际向量的范数修复结论，不含未知尾部乘大常数的项。

取
$$
q=50d^3,\qquad m\ge2.
$$
由 (1.1)、(3.5)，
$$
\begin{aligned}
\log\frac{\|u-v_{m,q}\|}{\|u\|}
\le{}&
-700d^4+630d^3+14d^2\\
&+3d\log(m+50d^3+2d+1)+d\log324+\log(36d).
\end{aligned}
\tag{4.5}
$$
丢掉了可用的负项 $-300d$。对 $d=2^m\ge4$，
$$
m+50d^3+2d+1\le52d^3,\quad
\log52<4,\quad \log324<6,
$$
$$
\log(36d)\le2d,\qquad \log d\le d/2.
$$
所以 (4.5) 的正余量不超过
$$
630d^3+\tfrac{37}{2}d^2+20d<200d^4.
$$
最终得到
$$
\boxed{
\|u-v_{m,50d^3}\|\le e^{-500d^4}\|u\|,
\qquad
P_{\le50d^3}^{(m)}P_mv_{m,50d^3}=0.
}
\tag{4.6}
$$

更一般地，取 $q=\lfloor\lambda d^3\rfloor$，固定 $0<\lambda<100$，则同一证明给
$$
\|u-v_{m,q}\|
\le
\exp[-(1400-14\lambda+o(1))d^4]\|u\|.
\tag{4.7}
$$
没有声明端点 $\lambda=100$。

## 5. 同一结论的收缩正交投影形式

定义闭空间
$$
\mathcal E_{m,q}
=\ker(P_{\le q}^{(m)}P_m),
$$
并令 $\mathsf E_{m,q}$ 为其正交投影。
由于 $P_m$ 在尾次数上至多下降 $2$，
$$
\mathcal H_{>q+2}\subseteq\mathcal E_{m,q}.
$$
故 $\mathsf E_{m,q}$ 与 $P_{>q+2}^{(m)}$ 交换并在该高尾上等于恒等。
由 (4.2) 及最佳逼近性，
$$
\boxed{
\|(I-\mathsf E_{m,q})u\|
\le36\eta_m\,
 \|\mathcal R_m|_{\mathcal H_{\le q}}\|\,\|u\|.
}
\tag{5.1}
$$
特别 $q=50d^3,m\ge2$ 时，
$$
\|(I-\mathsf E_{m,q})u\|\le e^{-500d^4}\|u\|.
\tag{5.2}
$$
其投影范数为 $1$，且投影后的向量在尾次数 $>q+2$ 处准确等于原向量。

这里 $\mathcal E_{m,q}$ 是“模型的低孔输出方程全部为零”的空间。它不是 $\ker P_m$；其高孔输出仍可非零。对固定 $m$，$\mathcal E_{m,q}$ 随 $q$ 递减，交集才是 $\ker P_m$，相应正交投影也才强趋于 $P_{\ker P_m}$。本稿预算不能在固定 $m$ 下令 $q\to\infty$ 而仍保持误差小。

## 6. 与纯尾高阶约束的关系及下一真实缺口

R254 第三附录给实际 $u\in K$ 到 $\ker D^{2d}$ 的距离估计，在 $50d^3$ 的窗口外只付原向量的普通 Hilbert 尾。本稿给另一个保留全部混合项的收缩投影：在几乎不改变实际 $u$ 的前提下，将同一窗口内的全部 $P_m$ 方程准确修好。

两个投影一般不交换，不能合成后直接声称得到 $\ker P_m$ 的逼近。$\ker D^{2d}$ 的不变性也不意味着约化 $P_m$。同样，低孔方程修复没有给出 $B$ 在实际核 $M$ 内的原像。

下一缺口被准确保留为：能否在共同满足低孔混合方程与纯尾高阶约束的向量上，构造带已付孔次数预算的正能量测试，或实际核内后移原像，并且不在未知 Hilbert 尾前重新引入头条件数。本稿不据此宣称 $N=M$，也不构造非零缺陷。
