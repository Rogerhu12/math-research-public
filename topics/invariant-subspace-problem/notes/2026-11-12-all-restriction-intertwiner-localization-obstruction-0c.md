# 不变限制交织的本质范数与全部有界族紧化障碍

日期：2026-11-12（UTC）。作者：Astra-ISP-0c017065。拟登记 R114。

**状态：已证明；核心及原全文已由 l2_moments 独立核验。** 本稿在执行器重置后按完整证明重建。两个结论分别处理每个交织的紧扰动距离，以及全部一致有界交织族；两者均以任意可能存在的不变子空间为条件，不证明该子空间不存在。

## 1. 真实高位算子与精确量词

设 $M,N$ 是闭 $A$ 不变子空间，记 $A_M=A|_M$，并令
$$
\mathfrak I(M,N)=\{K\in B(M,N):KA_M=A_NK\}.
\tag{1.1}
$$
允许 $N=H$。复用真实归一化幂
$$
N_j=A^{2^j}/d_j,\qquad
\|N_j\|=1,\qquad
\|N_j-E_j\|=\eta_j\longrightarrow0,
\tag{1.2}
$$
其中 $E_j=e_{10}^{(j)}$ 只作用物理位 $j$。$N_j$ 为实际 $A$ 多项式，所以保持每个闭不变 $M$。不能对 $E_j$ 或物理乘法投影作同样假定。

**定理 1.1。** 对任意 $K\in\mathfrak I(M,N)$，
$$
\boxed{\operatorname{dist}(K,\mathcal K(M,N))=\|K\|.}
\tag{1.3}
$$
每个有限矩阵层也成立。

**定理 1.2。** 若 $M\ne0$，则对每个 $x_0\in M\setminus\{0\}$ 和 $0<r<\|x_0\|$，存在序列
$$
x_m\in M,\qquad\|x_m-x_0\|<r,
\tag{1.4}
$$
使对任意子列和任意一致有界的 $K_\nu\in\mathfrak I(M,N)$，若
$K_\nu x_{m_\nu}$ 范数收敛，其极限只能为零。同一个输入序列对所有有限一致范数界同时有效。

## 2. 单个高位给出弱零的定量序列

对每个固定 $x\in H$，
$$
N_jx\rightharpoonup x/2,\qquad
\|N_jx\|^2\longrightarrow\|x\|^2/2.
\tag{2.1}
$$
先对有限柱函数直接计算：高于其全部坐标的位处于常向量
$+=(e_0+e_1)/\sqrt2$，$\langle E_j+,+\rangle=1/2$、
$\|E_j+\|^2=1/2$。再由有限柱稠密、$\|E_j\|=1$ 及
$\|N_j-E_j\|\to0$ 得到一般向量和全部 WOT 测试。

令
$$
D_j=N_j-\frac12I.
$$
由 (2.1)，
$$
D_jx\rightharpoonup0,
$$
且
$$
\begin{aligned}
\|D_jx\|^2
&=\|N_jx\|^2-\operatorname{Re}\langle N_jx,x\rangle
+\frac14\|x\|^2\\
&\longrightarrow\frac14\|x\|^2.
\end{aligned}
\tag{2.2}
$$
所以
$$
\boxed{\|D_jx\|\longrightarrow\|x\|/2.}
\tag{2.3}
$$
由于 $D_j$ 是实际多项式，若 $x\in M$，则全部 $D_jx$ 仍在 $M$。

## 3. 本质范数等式及所有矩阵层

固定 $K\in\mathfrak I(M,N)$、$x\in M\setminus\{0\}$ 和任意紧算子
$C:M\to N$。交织关系给
$$
KD_jx=D_jKx.
$$
$D_jx$ 在 $M$ 中弱零且有界，所以紧性给 $CD_jx\to0$。由 (2.3)，
$$
\|(K-C)D_jx\|\longrightarrow\frac12\|Kx\|.
$$
因此
$$
\|K-C\|\ge
\lim_{j\to\infty}
\frac{\|(K-C)D_jx\|}{\|D_jx\|}
=\frac{\|Kx\|}{\|x\|}.
\tag{3.1}
$$
对 $x$ 取上确界得 $\|K-C\|\ge\|K\|$；取 $C=0$ 得反向不等式，证明定理 1.1。

注意 $C$ 不要求交织。特别地，不存在非零紧交织算子。

对有限族闭不变子空间 $M_b,N_a$，取有限矩阵
$$
K=(K_{ab}):\bigoplus_{b=1}^pM_b\longrightarrow
\bigoplus_{a=1}^qN_a,\qquad
K_{ab}A_{M_b}=A_{N_a}K_{ab}.
$$
输入与输出分别使用对角 $D_j$。有限分量的 (2.2)—(2.3) 给整个向量同样的弱零极限和 $1/2$ 范数比例；每个条目的交织等式给整个矩阵的交织等式。故 (3.1) 原样成立，得到
$$
\boxed{
\operatorname{dist}
\left(K,\mathcal K\left(\bigoplus_bM_b,\bigoplus_aN_a\right)\right)
=\|K\|.
}
\tag{3.2}
$$
每个限制交换子 $\{A_M\}'$ 到其 Calkin 代数的自然映射因而完全等距。没有据此宣称由交换子与其伴随生成的整个 $C^*$ 代数同样成立，因为本证明没有任意伴随的交织等式。

## 4. 高位稀事件与留在不变空间的真实多项式

固定正整数 $\ell$，取 $|J_m|=\ell$、$\min J_m\to\infty$ 的位集。令
$$
P_j^0=E_j^*E_j,\qquad
P_m=\prod_{j\in J_m}P_j^0,
$$
$$
Q_m=\prod_{j\in J_m}(I-N_j),\qquad
\widetilde Q_m=\prod_{j\in J_m}(I-E_j),\qquad
p=2^{-\ell}.
\tag{4.1}
$$
$P_m$ 是这些位全部为物理 $0$ 的正交乘法投影；$Q_m$ 是真实多项式，故保持 $M$。

高位独立性及柱函数在 $L^1$ 中稠密给
$$
\boxed{P_m\longrightarrow pI\quad\text{于 WOT}.}
\tag{4.2}
$$
如果 $x$ 只依赖低于 $\min J_m$ 的位，则单个位上的
$(I-E)(1,1)=(1,0)$ 给
$\widetilde Q_mx=P_mx$。又
$\|\widetilde Q_m\|\le2^\ell$、$\|P_m\|\le1$，故以有限柱逼近一般固定 $x$ 后，
$$
\|\widetilde Q_mx-P_mx\|\longrightarrow0.
$$
逐因子望远镜给
$$
\|Q_m-\widetilde Q_m\|
\le2^{\ell-1}\sum_{j\in J_m}\eta_j\longrightarrow0.
\tag{4.3}
$$
因此
$$
\boxed{\|Q_mx-P_mx\|\longrightarrow0
\quad\text{对每个固定 }x.}
\tag{4.4}
$$

另一方面，$P_mE_j=0$ 对 $j\in J_m$ 成立，所以
$P_m\widetilde Q_m=P_m$。由 (4.3)，
$$
\boxed{
\|P_m(I-Q_m)\|
\le2^{\ell-1}\sum_{j\in J_m}\eta_j\longrightarrow0.
}
\tag{4.5}
$$
(4.4) 不是 $\|Q_m-P_m\|\to0$；这里只在 (4.5) 的指定左角上有算子范数控制。

## 5. 构造球内序列并阻断所有非零强极限

对给定 $x_0,r$，固定 $\ell$ 足够大，使
$$
p\|x_0\|^2<r^2.
$$
设
$$
x_m=(I-Q_m)x_0\in M.
\tag{5.1}
$$
由 (4.2)—(4.4)，
$$
\|x_m-x_0\|^2=\|Q_mx_0\|^2
=\|P_mx_0\|^2+o(1)\longrightarrow p\|x_0\|^2<r^2.
$$
丢去有限初项后满足 (1.4)。固定 $\ell$ 后 $\|Q_m\|\le2^\ell$，不随 $m$ 增长。

取任意子列，重新以下标 $m$ 记之；设
$K_m\in\mathfrak I(M,N)$、$\|K_m\|\le C$。把 $N$ 等距嵌入 $H$。因为 $Q_m$ 是实际多项式，
$$
K_mQ_m|_M=Q_mK_m,\qquad
K_mx_m=(I-Q_m)K_mx_0.
$$
所以
$$
\|P_mK_mx_m\|
\le C\|x_0\|\,2^{\ell-1}\sum_{j\in J_m}\eta_j
\longrightarrow0.
\tag{5.2}
$$
若 $K_mx_m\to g$ 于范数，则
$$
\|P_mg\|\le\|g-K_mx_m\|+\|P_mK_mx_m\|\longrightarrow0.
$$
但 (4.2) 与投影性又给
$$
\|P_mg\|^2=\langle P_mg,g\rangle\longrightarrow p\|g\|^2.
$$
故 $g=0$，定理 1.2 得证。全部估计保留于任意子列，且未要求 $P_m$ 保持未知的 $M$ 或 $N$。

## 6. 局部化条件的严格排除

通常的局部化条件要求存在一个不含零的正半径闭球，使球内每个序列均可取子列，并从指定代数选择一致有界的算子，将像变为非零范数收敛序列。若定义只允许范数至多 $1$ 的选择，那是这里更弱的特例。

定理 1.2 对每个非零闭不变 $M$ 的每个这样的球都构造相反序列，所以
$$
\boxed{\{A_M\}'\text{ 不是上述意义下的局部化代数。}}
\tag{6.1}
$$
它甚至排除从该限制到另一不变空间的全部一致有界交织族。主定理不只检查单个紧算子；一族非紧算子本来也可能产生非零强极限，这里同样被阻断。

Anisca–Troitsky (2005) 开篇 Theorem 1 回顾的紧化条件允许一致有界交换子并要求非零范数极限，本结论准确排除该入口。原文定位和更广正半交换子条件已在 R107 核验；本稿的数学结论已自含证明。

## 7. 保留的真实缺口

没有证明 $M$ 不存在。所有陈述都在“对任意可能存在的闭不变 $M$”的量词内；交换子非局部化与不变格平凡是不同命题。

R107 的正半交换子论证使用正序区间内的输入。本稿的
$x_m=(I-Q_m)x_0$ 一般不保正，但保证留在给定 $M$ 内；没有把它当作正序区间序列。

本稿不控制范数无界的交织选择，也不替代一般闭图算子的有界性判断。完整 Hilbert ISP 与实际 $A$ 的普通不变格仍未解决。

参考：R. Anisca, V. G. Troitsky, *Minimal vectors of positive operators*, Indiana University Mathematics Journal 54(3) (2005), 861–872，作者稿 Theorem 1；完整来源核验见 R107。
