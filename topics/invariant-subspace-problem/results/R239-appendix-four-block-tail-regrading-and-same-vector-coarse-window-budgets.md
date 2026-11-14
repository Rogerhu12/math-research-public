# R239 附录：四块天然模型的真实尾重排、多层顶源与同向量子窗预算

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：下文的尾重排、三层顶源、每个较低截断的真实最小性及裸/平坦未来带投影均已证明。它把前稿同一个原来源得到的四块天然模型向量，送回较小有限头的真实源流；不把旧顶部源当成较小头的新单层源，也不声称温和的模型两费用比较已经闭合。普通 ISP 与无权 $N=M$ 仍为 OPEN。

依赖：[四块头比较](R239-appendix-four-block-head-comparison-and-quarter-depth-source-elimination.md)、[天然零源旗与裸链运输](R239-appendix-natural-four-block-free-flag-and-bare-chain-transport.md)、[一次头条件数的平坦对偶运输](R239-appendix-natural-four-block-flat-dual-transport-with-one-head-condition.md)，以及 [R271 相容截断与原源流](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)。后者的固定层代数将在新的真实分层上使用；涉及其合法窗口结论时，另行检查较小参数的上窗。

## 1. 同一 Hilbert 空间的两种真实分层

固定
$$
m\ge8,\qquad d=2^m,\qquad n=m-2,\qquad h=2^n=d/4,
\qquad 4d\le q\le e^{d^3/4}.
$$
本稿用 $h$ 表示较小头维数，用 $s,t$ 表示新的孔数切口，以免与旧稿的 $p=d/4$ 混淆。

旧分解是 $m$ 位有限头与位置 $j\ge m$ 的尾；新分解把第 $n,n+1$ 两位从头移到尾。因此
$$
\mathbb C^d\otimes\mathcal H^{(m)}_{
\rm tail}
\cong
\mathbb C^h\otimes\mathcal H^{(n)}_{
\rm tail}
\tag{1.1}
$$
是物理基的酉重排，未引入任何相似度量。

令 $\epsilon_n,\epsilon_{n+1}\in\{0,1\}$ 为这两位的占据数。两种孔数严格满足
$$
\boxed{N_n=N_m+\epsilon_n+\epsilon_{n+1}.}
\tag{1.2}
$$
特别，各坐标投影彼此交换，且
$$
P^{(n)}_{\le s}\preceq P^{(m)}_{\le s},\qquad
P^{(m)}_{\le s}\preceq P^{(n)}_{\le s+2}.
\tag{1.3}
$$

记 $b_j=(j+1)^{-2}$，$E_0,E_1$ 为旧四块高二位的物理删除。四块头定义为
$$
A_\square=I_4\otimes A_n+(b_nE_0+b_{n+1}E_1)\otimes I_h.
$$
新尾删除正好是
$$
D_n=b_nE_0+b_{n+1}E_1+D_m.
$$
所以在 (1.1) 的同一物理空间内有精确恒等式
$$
\boxed{A_\square+D_m=A_n+D_n=:L_n.}
\tag{1.4}
$$
这是实际尾位置及实际权 $b_j$ 的恒等式，不是把 $D_m$ 偷换成另一种近似尾。

## 2. 旧顶部源会成为三个新孔层的源

取前两篇运输稿产生的同一个天然模型源 $g$，令
$$
v_\square=E_{\square,q}^{\dagger}g.
$$
它的旧支持在 $N_m\le q$，并满足
$$
(A_\square+D_m)v_\square=g,
\qquad \operatorname{supp}_{N_m}g\subseteq\{q\}.
\tag{2.1}
$$
由 (1.2)，同一方程在新的真实分层中变为
$$
L_nv_\square=f_q+f_{q+1}+f_{q+2},
\qquad f_{q+a}=P^{(n)}_{q+a}g\quad(a=0,1,2).
\tag{2.2}
$$
例如 $f_{q+2}$ 精确来自旧源中两高位均占据的部分。一般不能把 (2.2) 简化成单个新孔数 $q$ 的顶源。

新输入的支持满足 $N_n\le q+2$。旧最小性给
$$
v_\square\perp
\bigl(\ker L_n\cap\operatorname{Ran}P^{(m)}_{\le q}\bigr).
\tag{2.3}
$$
这里保留的是旧物理阶梯支持，不将其扩张为整个新 $N_n\le q+2$ 的核。

## 3. 每个新切口 s≤q 都是真正的较小头左最小者

对 $0\le s\le q$ 定义
$$
w_s=P^{(n)}_{\le s}v_\square,\qquad
r_s=A_nP^{(n)}_sv_\square.
\tag{3.1}
$$
较小头的空间和首输出为
$$
V_{n,s}=\operatorname{Ran}P^{(n)}_{\le s}
\cap\ker(P^{(n)}_{\le s-1}L_n),
\qquad E_{n,s}w=A_nw_s.
\tag{3.2}
$$
在固定 $n,s$，原有限 Jordan 头的右逆证明仍给 $E_{n,s}$ 的闭源像与有界最小逆；它没有使用窗口上界来证明这些代数事实。若 $s$ 太低，短核旗按实际非负孔层截断即可。下文费用窗只使用 $s\ge4h$，故不需要这项低端约定。

对所有 $s\le q$，有
$$
\boxed{w_s=E_{n,s}^{\dagger}r_s.}
\tag{3.3}
$$

证明：式 (2.2) 在新层 $<s$ 的输出为零，且 $L_n$ 只保持或降低新孔数一，故 $w_s\in V_{n,s}$、顶部输出是 (3.1)。任意
$$
z\in\ker E_{n,s}
=\ker L_n\cap\operatorname{Ran}P^{(n)}_{\le s}
$$
都因 (1.3) 而支持在旧 $N_m\le s\le q$。因此 $z$ 属于 (2.3) 的真实旧零源空间。于是
$$
\langle w_s,z\rangle=\langle v_\square,z\rangle=0.
$$
这正是固定源可行空间的最小范数条件，证明 (3.3)。

其结果包括同一个 $v_\square$ 决定的相容源流
$$
P^{(n)}_{\le s}E_{n,t}^{\dagger}r_t=E_{n,s}^{\dagger}r_s
\quad(s\le t\le q),
\tag{3.4}
$$
以及准确的正能量差
$$
\boxed{
\mu_{n,t}(r_t)^2-\mu_{n,s}(r_s)^2
=\|P^{(n)}_{[s+1,t]}v_\square\|^2.
}
\tag{3.5}
$$
特别，$w_q$ 是合法的较小头单层源最小者，而完整 $v_\square$ 一般不是该单层源的最小者。二者准确相差
$$
\|v_\square\|^2-\mu_{n,q}(r_q)^2
=\|P^{(n)}_{q+1}v_\square\|^2
 +\|P^{(n)}_{q+2}v_\square\|^2.
\tag{3.6}
$$
不省略这两个新高层。

## 4. 同一未来带给全部完整平坦测试

现在取整数 $s\ge4h$ 且
$$
s+h\le q.
\tag{4.1}
$$
以真实头 $A_n$、真实尾 $D_n$ 和宽度 $h$ 构成原完整右旗；记
$$
F_{n,s}:\mathscr C_{n,s}\to\mathscr R_{n,s},
\quad
\mathscr U_{f,n,s}=\operatorname{Ran}F_{n,s}^*,
\quad P_{f,n,s}=P_{\mathscr U_{f,n,s}}.
$$
这里
$$
\mathscr R_{n,s}
=\bigoplus_{i=0}^{h-2}e_i
\bigl(\ker D_n^{h-i-1}\cap\mathcal H_s^{(n)}\bigr),
$$
而第 $j$ 右段保留完整联合旗
$\bigoplus_{i=0}^{h-j}e_i(\ker D_n^{h-i}\cap\mathcal H_{s+j}^{(n)})$。

令 $J_{n,s}=E_{n,s}E_{n,s}^*$。同一源 $r_s$ 的平坦链为
$$
c_{n,s}^{\flat}=F_{n,s}^*J_{n,s}^{-1}r_s.
$$
则
$$
\boxed{
c_{n,s}^{\flat}
=P_{f,n,s}P^{(n)}_{[s+1,s+h]}v_\square.
}
\tag{4.2}
$$

证明时保留全部完整右测试。对任意 $a\in\mathscr R_{n,s}$，令
$u=E_{n,s}^{\dagger}a$、$c=F_{n,s}^{\dagger}a$。拼接 $u-c$ 是实际 $L_n$ 的核，支持在新层 $\le s+h\le q$，故也支持在旧层 $\le q$。式 (2.3) 给
$$
\langle J_{n,s}^{-1}r_s,a\rangle
=\langle w_s,u\rangle
=\langle P^{(n)}_{[s+1,s+h]}v_\square,c\rangle.
$$
让 $a$ 遍历整个闭源空间，右最小者遍历整个 $\mathscr U_{f,n,s}$，便得到 (4.2)。没有仅用规范左 primitive 坐标代替全部右测试。

因此
$$
\lambda_{{\rm flat},n,s}(r_s)^2
\le\|P^{(n)}_{[s+1,s+h]}v_\square\|^2.
\tag{4.3}
$$

## 5. 真实低出生旗的裸链投影及累计预算

令 $P_{L,n,s}$ 为这个较小头右旗的实际低出生投影；$P_{b,n,s}$ 为其真正裸最小者空间的正交投影。由于第 $s+j$ 层向量满足新头逐项短核旗，低出生部分的核高度至少为 $j$，故其非零头自动满足 $i\le h-j$。高出生部分在第 $j$ 段落在 $\ker D_n^{j-1}$，不会产生低出生输出。这与 R271 的证明逐项相同，但所有核、位置和权都是新的真实 $D_n$。

于是
$$
\boxed{
a_{n,s}(r_s)
=-P_{b,n,s}P_{L,n,s}
P^{(n)}_{[s+1,s+h]}v_\square,
}
\tag{5.1}
$$
并有
$$
\alpha_{n,s}(r_s)^2
\le\|P^{(n)}_{[s+1,s+h]}v_\square\|^2.
\tag{5.2}
$$
裸投影和平坦投影未被声明正交；正确合计是
$$
\boxed{
\chi_{n,s}(r_s)^2
\le2\|P^{(n)}_{[s+1,s+h]}v_\square\|^2.
}
\tag{5.3}
$$

对任何 $4h\le a\le b\le q-h$，计数每个新孔层最多进入 $h$ 个未来带，得
$$
\boxed{
\begin{aligned}
\sum_{s=a}^{b}\chi_{n,s}(r_s)^2
&\le2h\|P^{(n)}_{[a+1,b+h]}v_\square\|^2\\
&=2h\bigl(\mu_{n,b+h}(r_{b+h})^2-\mu_{n,a}(r_a)^2\bigr)\\
&\le2h\|P^{(n)}_{>a}v_\square\|^2.
\end{aligned}}
\tag{5.4}
$$
等号使用的是同一 $v_\square$ 的 (3.5)，未在每个切口重选独立来源。

## 6. 与同一个原向量及原费用的定量关系

设天然旗运输之前的原来源为 $r$，原真正左向量为 $v$，原费用
$$
\mu=\|v\|,\qquad
\lambda=\|c^{\flat}(r)\|.
$$
前稿的实际锐小量 $\rho$ 给
$$
\boxed{
\|v-v_\square\|
\le\tau:=\rho\lambda+3\rho(1+\rho)\mu.
}
\tag{6.1}
$$
式 (1.1) 是酉重排，故此比较在新分层中原样成立。特别对任意 $s\le q$，
$$
\|E_{n,s}^{\dagger}r_s-P^{(n)}_{\le s}v\|\le\tau,
\tag{6.2}
$$
而 (5.4) 可以由同一个原向量支付：
$$
\boxed{
\sum_{s=a}^{b}\chi_{n,s}(r_s)^2
\le2h\bigl(\|P^{(n)}_{>a}v\|+\tau\bigr)^2.
}
\tag{6.3}
$$
这没有声称每个较小头平坦向量等于某个原平坦向量的投影；(4.2) 的投影对象是同一个模型左向量 $v_\square$。原平坦向量只在已付的误差 $\tau$ 中出现。

若原实际来源满足 $v_m\to w$ 强收敛且 $\tau_m\to0$，则对于任何 $0\le s_m\le q_m$，
$$
\|E_{m-2,s_m}^{\dagger}r_{s_m}-w\|
\le\|v_m-w\|+\tau_m+
\|P^{(m-2)}_{>s_m}w\|.
\tag{6.4}
$$
这里 $P^{(m-2)}_{>s_m}w\to0$ 对任意非负 $s_m$ 都成立：先用有限物理支持向量逼近 $w$，当 $m$ 足够大时，该有限向量在新尾中没有占据。故每个这样的相容子窗最小者仍趋于同一个 $w$。涉及费用时保留 $s_m\ge4h$ 与 (4.1)。

## 7. 上窗检查与准确剩余接口

固定层恒等式 (1.4)、最小性 (3.3)、投影式 (4.2)、(5.1) 本身没有使用 $s\le e^{h^3/4}$。但是原较小参数 $n=m-2$ 的可用统一窗口是
$$
4h\le s\le Q_n:=\lfloor e^{h^3/4}\rfloor.
$$
因此调用只在该窗口证明的任何后续估计时，必须要求
$$
\boxed{4h\le s\le\min(Q_n,q-h).}
\tag{7.1}
$$
调用后续引理时还须遵守其头参数下限；例如该引理若要求 $n\ge8$，本节相应取 $m\ge10$。前述固定层代数及同向量投影本身仍在本文的 $m\ge8$ 范围成立。

旧 $q\le e^{d^3/4}$ 只给 $q\le e^{16h^3}$，不能推出 $q\le Q_n$。同理，(2.2) 的三个新顶源不可冒作 $E_{n,q}$ 的单个源；正确单层源由截断 (3.1) 产生。

若能在 (7.1) 或另一已独立付费的实际子窗族上证明
$$
\mu_{n,s}(r_s)^2\le C_n\chi_{n,s}(r_s)^2,
$$
则 (5.4) 提供同一向量的求和接口。本文没有得到该 $C_n$。一般 Jordan 相似只给含头条件数平方的有限界，仍不足以替代合法三次指数窗口需要的温和界。

新增的闭合部分是：天然四块模型并非一个必须在未知度量中另行比较的抽象模型；它与较小头的实际算子完全相同，但有真实三层顶部源。它的每个较低切口都是可直接应用原源流与未来带预算的真正最小者，并保留同一个原来源的近似向量及误差。
