# R185/R188 附注：快速有限头残差进入稳定闭像，及稳定商的高位范数

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整实际证明；不另编号。

本稿给边界内部饱和一个正向接口：所有 R185/R188 标准有限块递归构造的核向量，实际都属于 $N=\overline{B\ker T}$。证明允许真正的 $B$ 前像范数极大，先在有限头内取右移，再利用 $B$ 与纯块纠错模型的精确交换。它不假定任意核向量具有同样的残差速率，因此尚未证明 $N=\ker T$。

## 1. 模型、有限头与残差准则

在真实负整数边界 $\mathcal H_-=\ell^2(\mathbb N_0)$ 上，取
$$
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1},\qquad
\mathsf N_j=B^{2^j}/d_j,\qquad
\mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1},
$$
以及两个具体慢算子之一
$$
T=T_N:=\sum_{j\ge0}(j+1)^{-2}\mathsf N_j
\quad\hbox{或}\quad
T=T_Y:=\sum_{j\ge0}(j+1)^{-2}\mathsf Y_j.
\tag{1.1}
$$
令
$$
M=\ker T,\qquad N=\overline{BM},\qquad
\mathcal F_m=\operatorname{span}\{e_n:0\le n<2^m\}.
$$
$T$ 与 $B$ 交换，所以 $N\subseteq M$。
记 $P_m$ 为有限头 $\mathcal F_m$ 的正交投影，并置
$$
\mathcal A_m=\exp(8m2^m).
$$

**定理 1.1（快速有限头残差准则）。**
设 $m_k\to\infty$，$v_k\in\mathcal F_{m_k}$，且
$$
v_k\longrightarrow g,\qquad
\mathcal A_{m_k+1}\|Tv_k\|\longrightarrow0.
\tag{1.2}
$$
则
$$
\boxed{g\in N.}
\tag{1.3}
$$
不必先额外假设 $g\in M$；(1.2) 已经蕴含 $Tg=0$。
证明会给真正的 $y_k\in M$，满足 $By_k\to g$，
但没有给 $\sup_k\|y_k\|<\infty$。

## 2. 纠错模型与后移的精确交换

对 $p\ge2$，令
$$
L=64\,2^p,\qquad p^+=2L.
$$
R185/R188 的有限纯块构造给线性映射
$$
\mathcal R_p:\mathcal F_p\longrightarrow\mathcal F_{2L},
\qquad
\mathcal R_ph=
\sum_{\nu=0}^{2^p-1}(-1)^\nu T_p^\nu h\otimes h_\nu,
\tag{2.1}
$$
其中 $T_p=T|_{\mathcal F_p}$，中间坐标 $[p,L)$ 全部真空，
$h_\nu$ 位于新块 $[L,2L)$ 的 $\nu$ 孔齐次空间，
$h_0$ 为新块真空。
所用实际有限头与纯块恒等式为
$$
T_p^{2^p}=0,\qquad \|T_p\|\le6,\qquad
D_{\mathcal B}h_\nu=h_{\nu-1}.
$$
它们给出精确模型核
$$
(T_p\otimes I+I\otimes D_{\mathcal B})\mathcal R_ph=0,
$$
以及任意有限输入的估计
$$
\|\mathcal R_ph-h\|\le\mathcal A_p\|T_ph\|,
\qquad
\|\mathcal R_p\|\le1+6\mathcal A_p.
\tag{2.2}
$$
真实残差满足
$$
\boxed{\|T\mathcal R_ph\|
\le26\eta_{L-1}\|\mathcal R_ph\|.}
\tag{2.3}
$$
(2.3) 对 $T_N$ 可用更小常数 4；统一使用 26。
这些正是 R185 §4–5、R188 §3–4 的实际估计。

令 $B_p=B|_{\mathcal F_p}$。
$T_p$ 是 $B_p$ 的有限多项式，所以
$$
B_pT_p=T_pB_p.
\tag{2.4}
$$
因此在模型张量空间中，
$$
(B_p\otimes I)\mathcal R_ph
=\mathcal R_p(B_ph).
\tag{2.5}
$$

还必须支付真正的 $B$ 与这个模型的差。
在低头 $[0,p)$、空白间隔 $[p,L)$ 和新块 $[L,2L)$ 组成的整个空间上，
$$
\boxed{\|(B-B_p\otimes I)x\|\le\alpha_L\|x\|.}
\tag{2.6}
$$
证明：若低头中有孔，真正后移就在低头内作用，等于 $B_p$。
若低头全真空，则模型后移为零；真正后移只有在新块中遇到孔时才能非零，
其最低孔至少为 $L$，对应权不超过 $\alpha_L$。
不同输入整数的后移输出互异，所以这一逐列权界也是算子范数界。
这同样可由 R185 的真实 borrow 展开在 $i=0$ 时乘回 $\alpha_0$ 得到。

结合 (2.5)—(2.6)，得到关键式
$$
\boxed{
\|B\mathcal R_ph-\mathcal R_p(B_ph)\|
\le\alpha_L\|\mathcal R_ph\|.
}
\tag{2.7}
$$
本式使用有限头上的精确交换，并没有把全空间标准右移当作有界算子。

## 3. 有限头真正右移，及可能巨大的中间范数

先固定一个 $v\in\mathcal F_m$，取
$$
p=m+1.
$$
在 $\mathcal F_p$ 上定义局部右移
$$
J^{[p]}e_n=
\begin{cases}
\alpha_{v_2(n+1)}^{-1}e_{n+1},&0\le n<2^p-1,\\
0,&n=2^p-1.
\end{cases}
$$
其范数为
$$
\|J^{[p]}\|=\alpha_{p-1}^{-1}.
$$
由于 $v$ 实际位于更小的 $\mathcal F_{p-1}$，
它没有 $\mathcal F_p$ 的最高坐标，因此
$$
h=J^{[p]}v\in\mathcal F_p,\qquad B_ph=v,\qquad
\|h\|\le\alpha_{p-1}^{-1}\|v\|.
\tag{3.1}
$$
这就是有限输入的真正标准右移；不是形式级数除法。

置
$$
V=\mathcal R_ph,\qquad H=\|V\|.
$$
由 (2.2)，
$$
\boxed{
H\le(1+6\mathcal A_p)\alpha_{p-1}^{-1}\|v\|.
}
\tag{3.2}
$$
中间范数可以非常大，证明不会把它偷偷换成统一常数。

实际权的明确公式给
$$
-\log\alpha_q
=\frac{280}{3}16^q-90\,8^q+300\,2^q-\frac{850}{3}
\le100\,16^q\qquad(q\ge0).
\tag{3.3}
$$
所以当 $\|v\|\le C$ 时，
$$
H\le7C\exp\bigl(8p2^p+100\,16^{p-1}\bigr).
\tag{3.4}
$$
另一方面 $L=64\,2^p$，且
$$
\alpha_L\le\eta_{L-1}
\le\exp\!\left(-\frac{770}{16}16^L\right).
\tag{3.5}
$$
因此
$$
\boxed{
H\alpha_L\longrightarrow0,\qquad
H\exp(-20\,16^L)\longrightarrow0
\quad(p\to\infty)
}
\tag{3.6}
$$
对有界的一族输入 $v$ 成立。
这里的比较是 $16^L$ 压倒 $16^p+p2^p$；
没有要求 $\alpha_{p-1}^{-1}$ 本身较小。

## 4. 归一化后进入原标准预算，再乘回真实尺度

若 $V=0$，由修正保留原低头系数可知 $h=0$，于是 $v=0$，该项无须处理。
以下设 $H>0$。由 (2.3)，
$$
\left\|T\frac VH\right\|\le26\eta_{L-1}.
$$
因为 $p^+=2L$，实际权界给
$$
26\eta_{L-1}
\le26\exp\!\left(-\frac{770}{16}16^L\right)
\le\exp(-40\,4^{p^+}).
\tag{4.1}
$$
这里确实先归一化了可能很大的 $V$，随后才使用标准预算。
向量 $V/H$ 范数为 1，属于有限头 $\mathcal F_{p^+}$；
R185/R188 的后续标准迭代给 $\widetilde y\in M$，满足
$$
\left\|\widetilde y-\frac VH\right\|
\le2\exp(-20\,4^{p^+})
=2\exp(-20\,16^L).
\tag{4.2}
$$
令 $y=H\widetilde y\in M$。于是
$$
\boxed{\|y-V\|\le2H\exp(-20\,16^L).}
\tag{4.3}
$$
我们没有把归一化后的误差直接作为未归一化误差使用。

由 (2.7)、(3.1)，
$$
\|BV-\mathcal R_pv\|\le\alpha_LH.
$$
再用 (2.2)，得到
$$
\boxed{
\|By-v\|
\le\mathcal A_p\|Tv\|
+H\left(\alpha_L+2\|B\|\exp(-20\,16^L)\right).
}
\tag{4.4}
$$
右边各项均已在真实边界空间中估计完毕。

## 5. 准则、构造类与尚未完成的全核密度

对定理 1.1 的 $v_k$，其范数一致有界。
令 $p_k=m_k+1$，按 §§3–4 构造 $y_k\in M$。
(1.2)、(3.6) 和 (4.4) 给
$$
By_k-v_k\longrightarrow0.
$$
又 $v_k\to g$，所以 $By_k\to g$，证明 $g\in N$。

由此有两个直接推论。

**推论 5.1。** 若 $g\in M$，并存在 $m_k\to\infty$ 使
$$
\mathcal A_{m_k+1}\|(I-P_{m_k})g\|\longrightarrow0,
$$
则 $g\in N$。

证明：取 $v_k=P_{m_k}g$，
$\|Tv_k\|=\|T(P_{m_k}-I)g\|\le\|T\|\|(I-P_{m_k})g\|$。

**推论 5.2。** R185/R188 的所有标准有限块递归构造向量都属于 $N$。
在一次允许较弱首步残差的修复之后，再按标准递归得到的向量同样属于 $N$。

证明：这些构造有有限近似 $g_k\in\mathcal F_{m_k}$，$g_k\to g$，
并且在某个固定尺度因子 $C<\infty$ 下，
$$
\|Tg_k\|\le C\exp(-40\,4^{m_k}).
$$
而
$$
\mathcal A_{m_k+1}\,C\exp(-40\,4^{m_k})\longrightarrow0,
$$
因为 $(m_k+1)2^{m_k+1}=o(4^{m_k})$。
定理 1.1 适用。

该推论包含此前弱复制稿中的每个精确修复向量 $w_n$，
也包含高位一孔补偿后修复的每个 $z_j$。
它只对每个固定的完整构造调用自己的尾近似，
不需要对外部指标 $n$ 或 $j$ 具有统一的递归常数。
对某个这样的构造加一个固定真空标量，也保留同样准则。

上述论证真正给出 $\operatorname{Dom}J_1\cap M$ 在这些构造向量处的密度：
每个 $By_k$ 都属于 $M\cap\operatorname{Ran}B$。
但目前没有证明任意 $g\in M$ 满足 (1.2)，也没有证明其物理头尾具有推论 5.1 的速度。
因此不能用本准则把 $N\subseteq M$ 升为等号。

## 6. 固定 UHF 弱复制在稳定商中仍保留作用范数

本节仅使用已经完整核验的弱复制附注：
对一个标准构造向量 $g\ne0$，存在精确核向量 $w_n$，满足
$$
w_n\rightharpoonup0,\qquad
\|w_n\|\to\|g\|,
$$
$$
\|Ew_n\|\to\|Eg\|
\quad\text{对每个固定 }E\in\mathfrak U_-.
\tag{6.1}
$$
各个 $w_n$ 也经标准修复产生，所以推论 5.2 给
$$
g,w_n\in N.
\tag{6.2}
$$
复制保头使 $w_n\perp e_0$（舍去有限前缀即可）。

令
$$
Q=N/\mathbb Ce_0,
$$
以正交代表 $N\ominus\mathbb Ce_0$ 实现。
R187 已证明这个稳定商的后移单射、值域稠密、拟幂零。
本节只对保留 $N$ 和 $\mathbb Ce_0$ 的固定算子 $E$ 定义 $E_Q$；
特别，每个 $E\in\pi_-(\mathcal A)$ 都满足这些条件。
不把整个 UHF 代数在 $Q$ 上的压缩当成同态。

因为 $w_n\rightharpoonup0$，有
$$
P_{\mathbb Ce_0}Ew_n\longrightarrow0.
$$
所以 (6.1) 推出
$$
\|w_n+\mathbb Ce_0\|\to\|g\|,\qquad
\|E_Q(w_n+\mathbb Ce_0)\|\to\|Eg\|.
\tag{6.3}
$$
对商空间上的任意紧算子，弱零序列的像强趋零，因此
$$
\boxed{\|E_Q\|_{\rm ess}\ge\frac{\|Eg\|}{\|g\|}.}
\tag{6.4}
$$
右边保留的是原 $Eg$ 的完整范数；
它可能有真空分量，但弱复制已把这部分移到高位，不能再把原 $Eg$ 的真空先删掉。

数值下界也能保留。
对固定 $E$，把 (6.1) 应用于 $E+\lambda I$ 的四个固定值
$\lambda\in\{1,-1,i,-i\}$，再极化，得到
$$
\langle Ew_n,w_n\rangle\longrightarrow\langle Eg,g\rangle.
\tag{6.5}
$$
由于 $w_n\perp e_0$，商中的相应内积与原内积相同。
于是
$$
\boxed{
w(E_Q)\ge
\frac{|\langle Eg,g\rangle|}{\|g\|^2}.
}
\tag{6.6}
$$
没有假设对所有 $g\in N$ 都能复制；这里只有明确的标准构造类。

## 7. 稳定商上高位归一化幂的极限

弱复制稿 §8 已给精确标准修复向量 $z_j\in M$，满足
$$
z_j\perp e_0,\qquad \|z_j\|\to1,\qquad
\|\mathsf N_jz_j-e_0\|\to0.
\tag{7.1}
$$
推论 5.2 现在保证 $z_j\in N$。

直接把 (7.1) 商掉会丢失输出，不能由此直接取得 $Q$ 上的范数下界。
正确做法是：对每个固定的 $j$，
在 (6.4) 中取 $E=\mathsf N_j$、$g=z_j$，
再对该固定输入做一次完整高位弱复制。
这样
$$
\|(\mathsf N_j)_Q\|_{\rm ess}
\ge\frac{\|\mathsf N_jz_j\|}{\|z_j\|}.
$$
随后才令 $j\to\infty$。
全空间上 $\|\mathsf N_j\|\le1$，所以
$$
\boxed{
\|(\mathsf N_j)_Q\|_{\rm ess}\longrightarrow1,\qquad
\|(\mathsf N_j)_Q\|\longrightarrow1.
}
\tag{7.2}
$$

对数值半径，取标准构造类中的固定向量
$$
g^{(j)}=\frac{e_0+z_j}{\sqrt{1+\|z_j\|^2}}.
$$
加真空和固定标量归一化不影响推论 5.2 或弱复制构造；
可在其标准尾近似足够深以后开始复制。
弱复制稿已证明
$$
\langle\mathsf N_jg^{(j)},g^{(j)}\rangle\to\frac12.
$$
对每个固定 $j$ 先用 (6.6)，再令 $j\to\infty$，得到下界。
上界来自商的正交代表压缩以及
$\|\mathsf N_j-\mathsf E_j\|\le\eta_j$：
$$
w((\mathsf N_j)_Q)
\le w(\mathsf N_j)\le\frac12+\eta_j.
$$
故
$$
\boxed{w((\mathsf N_j)_Q)\longrightarrow\frac12.}
\tag{7.3}
$$

(7.2)—(7.3) 同时适用于 $T_N$、$T_Y$ 的各自稳定商。
这与 $(\mathsf N_j)_Q\to0$ 强收敛并不冲突：
强收敛先固定输入，而这里的范数/数值半径取随 $j$ 改变的输入。
它也不消除整个 $M$ 与 $N$ 的未知差距；本稿把已构造向量及其弱复制真实地放进了稳定部分，但未处理任意核向量的尾速率。


## 8. 未进入稳定部分的核向量必须具有的定量慢尾

(4.4) 的构造适用于每个有限输入，不要求初始残差很小。
因此可把它写为统一的有限头距离估计。

对 $m\ge1$，令 $p=m+1$、$L=64\,2^p$，并置
$$
\kappa_p=
(1+6\mathcal A_p)\alpha_{p-1}^{-1}
\left(\alpha_L+2\|B\|e^{-20\,16^L}\right).
\tag{8.1}
$$
由 (3.3)—(3.6)，$\kappa_p\to0$，且衰减快于
$\exp(-c\,16^L)$ 对某个固定 $c>0$。
由 (3.2)、(4.4) 立即得到
$$
\boxed{
\operatorname{dist}(v,N)
\le\mathcal A_{m+1}\|Tv\|
+\kappa_{m+1}\|v\|
\qquad(v\in\mathcal F_m).
}
\tag{8.2}
$$
这里对整个有限头空间使用同一个常数；
没有让它依赖输入或其残差。

现在若 $f\in M\ominus N$ 为单位向量，取 $v=P_mf$。
由于 $f\perp N$，
$$
\operatorname{dist}(P_mf,N)
\ge|\langle P_mf,f\rangle|
=\|P_mf\|^2.
\tag{8.3}
$$
对所有满足
$$
\|P_mf\|\ge\frac12,\qquad
\kappa_{m+1}\le\frac18
$$
的 $m$，(8.2)—(8.3) 给
$$
\frac14
\le \mathcal A_{m+1}\|TP_mf\|
+\frac18\|P_mf\|
\le\mathcal A_{m+1}\|TP_mf\|+\frac18.
$$
因此
$$
\boxed{\|TP_mf\|\ge\frac{1}{8\mathcal A_{m+1}}.}
\tag{8.4}
$$
再用 $Tf=0$，
$$
\|TP_mf\|=\|T(I-P_m)f\|
\le\|T\|\,\|(I-P_m)f\|,
$$
得到
$$
\boxed{
\|(I-P_m)f\|
\ge\frac{1}{8\|T\|\mathcal A_{m+1}}
=\frac{\exp[-8(m+1)2^{m+1}]}{8\|T\|}.
}
\tag{8.5}
$$
固定非零 $f$ 归一化以后，$\|P_mf\|\to1$，
所以 (8.4)—(8.5) 对全部充分大的 $m$ 成立。

这些是未知正交差空间 $M\ominus N$ 中向量的必要条件。
它们排除具有足够快有限头残差或尾范数的候选，
但不排除任意慢的平方可和尾，也不证明差空间存在。
尤其不能由有限头投影在全空间强趋恒等，
就声称其误差满足与 $m$ 有关的指数速度。
