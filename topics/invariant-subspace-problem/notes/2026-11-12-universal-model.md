# 2026-11-12：普适后移模型、循环性和交织运输

状态：研究笔记。已完成的自含路线障碍分别登记为 R3、R4、R6；完整 Hilbert ISP 未解决。本笔记只记录模型计算、文献范围和仍未跨过的步骤。

## 1. Rota 闭图模型：完整公式

先对任意有界 $T$ 乘一个非零小常数，使 $\|T\|<1$。这不改变其闭不变子空间格。令
$$
\mathcal K=\ell^2(\mathbb N_0;H),\qquad
B_\infty(h_0,h_1,\ldots)=(h_1,h_2,\ldots),
$$
定义
$$
Jx=(x,Tx,T^2x,\ldots).
$$
于是
$$
\|x\|^2\le\|Jx\|^2
=\sum_{n\ge0}\|T^nx\|^2
\le\frac1{1-\|T\|^2}\|x\|^2.
$$
故 $J$ 到其像 $\mathcal M=JH$ 是有界同构，而且 $\mathcal M$ 闭。逐项计算给出
$$
B_\infty J=JT,
\qquad
B_\infty|_{\mathcal M}=JTJ^{-1}.
$$
若 $L\subset H$ 闭且 $T$-不变，则 $JL$ 在 $\mathcal M$ 中闭且 $B_\infty$-不变；反过来也成立。因此此模型的确完整保留目标问题，但并没有自动给出 $\mathcal M$ 内的非零真闭不变子空间。

此构造属于 G.-C. Rota, *On models for linear operators*, Comm. Pure Appl. Math. **13** (1960), 469–472。出版社页面核对 DOI：<https://doi.org/10.1002/cpa.3160130309>。原定理允许谱半径小于 $1$；上述范数小于 $1$ 的版本已足够覆盖经缩放的任意算子。

令
$$
Q=J^*J=\sum_{n\ge0}(T^*)^nT^n.
$$
该级数在算子范数中收敛，$I\le Q\le(1-\|T\|^2)^{-1}I$，且
$$
T^*QT=Q-I.
$$
到 $\mathcal M$ 的正交投影为
$$
P_{\mathcal M}=JQ^{-1}J^*,
\qquad
(P_{\mathcal M})_{ij}=T^iQ^{-1}(T^*)^j
\quad(i,j\ge0).
$$
验证：该算子自伴，平方等于自身，像为 $JH$；矩阵块公式由 $J$ 的坐标定义立即得到。

这把模型子空间的几何写得很显式，但 $Q$ 一般不与 $T$ 交换。Stein 方程本身没有产生新的 $T$-不变子空间。

## 2. 为什么不能直接使用后移的大量特征向量

对每个 $|\lambda|<1$，
$$
\ker(B_\infty-\lambda I)
=\{(v,\lambda v,\lambda^2v,\ldots):v\in H\}.
$$
但
$$
\mathcal M\cap\ker(B_\infty-\lambda I)
=J\ker(T-\lambda I).
$$
证明只需比较第零和第一坐标，或者使用 $B_\infty J=JT$ 及 $J$ 单射。因此只要 $T$ 没有特征值，$\mathcal M$ 就与后移的每个特征空间交零。

这完全可以发生在很简单的正例中：$T=M_{t/2}$ 于 $L^2[0,1]$ 没有特征值，却有所有支集型闭不变子空间。其 Rota 模型不能靠“从环境特征空间中取一个向量”发现这些子空间。

## 3. 若压缩到标量后移，闭性可能彻底丢失

R4 给出精确的矩变换
$$
(Xf)_n=\int_0^1f(t)(t/2)^n\,dt,
\qquad BX=XT.
$$
该 $X$ 单射、稠密像、Hilbert–Schmidt，且有限秩逼近指数快。然而每个非零 $Xf$ 都是标量后移 $B$ 的循环向量。因此每个真闭 $B$-不变子空间的拉回都是零；原算子的每个非零不变子空间的像反而在整个模型空间中稠密。

相关经典文献是 Bernard Virot, *Modèles d'opérateurs linéaires et translations unilatérales simples*, Bull. Soc. Math. France **100** (1972), 157–175，§2 的 Proposition 1 及其 corollaire、§4 的 Proposition 3，原文 <https://numdam.org/item/10.24033/bsmf.1734.pdf>。§4 Proposition 3 的核型拟仿射构造与这里的矩变换相联系；R4 的全部证明已经独立写出，不作新颖性宣称。

所以单向拟仿射把模型变成标量后移，并没有保留“非零真闭”这个核心条件。缺失的并不是一个可由稠密性补上的拓扑小步骤。

进一步，R6 已证明这是一个通用障碍：若 $\|T\|<1$ 且 $y$ 对 $T^*$ 循环，则 $X_yh=(\langle T^nh,y\rangle)_n$ 是 Hilbert–Schmidt 拟仿射；$X_yh$ 对标量后移循环，当且仅当 $h$ 的 $T$-循环空间无限维。因此只要 $T$ 没有特征值，这个观察模型的所有真闭不变子空间拉回都为零。R6 给出解析因子分解和压缩循环性的完整证明。

## 4. 稠密循环核心和有界多项式逼近

R3 完整证明了以下两种不同障碍。

- 对 $T=M_t$ 于 $L^2[0,1]$，每个非零多项式都循环，但 $1_{[0,1/2]}$ 不循环。若用循环多项式逼近这个向量，再用算子多项式逼近常函数 $1$，则逼近算子范数与输入误差的乘积不能趋零。
- 对 $T^*$ 没有特征值的算子，$\operatorname{Alg}_{\rm WOT}(T)x$ 对每个非零 $x$ 都是真、第一纲 $F_\sigma$ 子空间。若 $x$ 循环，则对稠密 $G_\delta$ 集中的目标，任何多项式逼近序列的算子范数都必须趋于无穷。这是严格循环代数的经典机制，见 R3 中 Embry (1973) 的出处与证明。

因此，试图以有界多项式范数来完成“每个非零向量都循环”的反例构造，会引入一个反而迫使不变超平面存在的过强条件。真正的反例若存在，必允许严重的逼近放大。

## 5. 2026 年 10 月原文的范围

已核对 João Carmo、Ben-Hur Eidt、Waleed Noor，*Universal operators: topology and consequences of ISP failure*, arXiv:2610.22694v2，v1 于 2026-10-15、v2 于 2026-10-19。

原文入口：<https://arxiv.org/abs/2610.22694>；HTML：<https://arxiv.org/html/2610.22694v2>。本环境的终端 HTTP 可读取原始 HTML。

其中 Theorem 2.1 是条件性结论：若完整 Hilbert ISP 有反例，则每个普适算子都有连续统多个两两交零的极小无限维闭不变子空间，并可使限制可逆、幂按预定几何速率衰减。Theorem 3.9 与 Corollary 3.15 进一步研究仿射复合算子的径向零模型及相关等价表述。它们没有给出完整问题的肯定或否定答案。

本轮对 Theorem 2.1 的图空间构造做了直接检查：先把假设存在的反例平移成可逆算子 $A$，再把 $A\oplus A\oplus LI$ 放入普适模型；标量块限制普适性给出的缩放量。子空间 $\{(x,tx,0):x\in H\}$ 两两交零，且同构常数中的 $\sqrt{1+|t|^2}$ 因子彼此抵消。此处没有从可分性得到矛盾：两两交零不意味着两两正交。

## 6. 仍未解决的具体步骤

对任意 $T$，Rota 的 $\mathcal M=JH$ 是闭且显式的；但尚不能从它的投影矩阵或 Stein 方程构造一个满足
$$
\{0\}\ne\mathcal L\subsetneq\mathcal M,
\qquad B_\infty\mathcal L\subseteq\mathcal L
$$
的闭子空间。把 $J$ 换成容易构造的紧拟仿射，则 R4 说明所有自然拉回可能全为零。

因此下一步若继续该方向，应寻找一个能保证模型子空间与目标不变子空间非零相交的**额外定量条件**，并证明该条件对一般 $T$ 成立。单独的稠密性、紧性、轨道幂衰减、环境算子有大量特征向量，以及稠密代数核心上全向量循环，均已在上述计算中显示不足。这样的通用额外条件本轮尚未获得。
