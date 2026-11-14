# R248附录：无限稀疏无阻尼位仍允许纯模型非零核

日期：2026-11-13（UTC+8）。作者：normal_states；Astra-ISP-1cf8c51d 复核。状态：已证明，中间结论。

本附录补充 [R248](R248-adaptive-walsh-damping-of-normal-annihilator-moments.md)，只处理没有 carry 的变形纯慢和，不直接判断真实 $S_\delta$。它说明“$\delta_j=1$ 于无限多个位”不足以单独推出变形慢和单射。正常矩条件仍有额外内容，不能省略。

在 Walsh 单个位基 $(1,\chi)$ 中，设
$$
E_\delta=\frac12
\begin{pmatrix}1&\delta^{-1}\\-\delta&-1\end{pmatrix}.
$$
令 $a_j=(j+1)^{-2}$，取 $\frac12<\sigma<1$。
取稀疏 $I=\{i_n\}$，其中 $i_n\ge2^n$，令
$\delta_i=1$ 对 $i\in I$，其余 $\delta_k=(k+2)^{-\sigma}$。
考虑有界纯算子
$$
S_\delta^0=\sum_ja_jE_{\delta_j}^{(j)}.
$$
有界性由 $\sum_j a_j\delta_j^{-1}<\infty$ 保证。

不妨按严格递增次序列出 $i_1<i_2<\cdots$。为了同时保证配对位可选和有无限多个未配对位，额外要求
$$
k_n<i_n,\qquad k_n\notin I,\qquad k_n\not\equiv2\pmod3,
$$
且 $k_n$ 两两不同。在区间 $[0,i_n)$ 中，不等于 $2\pmod3$ 的整数有
$\lceil2i_n/3\rceil$ 个。此前的升级位至多排除 $n-1$ 个，已用配对位至多再排除 $n-1$ 个；而
$$
\left\lceil\frac{2i_n}{3}\right\rceil
\ge\left\lceil\frac{2^{n+1}}3\right\rceil>2n-2
\qquad(n\ge1).
$$
最后的初等不等式在 $n=1,2$ 直接成立；对 $n\ge3$，由 $2^{n+1}/3\ge2n-1$（从 $n=3$ 起归纳）立即得到。因此所需 $k_n$ 可递归选取。

另一方面，全部 $k_n$ 避开 $2\pmod3$。在 $[0,L)$ 内，$I$ 至多有 $\log_2L$ 个元素，而 $2\pmod3$ 的整数有 $\lfloor L/3\rfloor$ 个。所以
$$
K=\mathbb N_0\setminus\bigl(I\cup\{k_n:n\ge1\}\bigr)
$$
无限；至少 $\{k:k\equiv2\pmod3\}\setminus I$ 为其无限子集。

令 $r_n=a_{i_n}/a_{k_n}\le1$、$\varepsilon_n=\delta_{k_n}$。

单个位有
$$
E_\varepsilon(1,-\varepsilon)^T=0,\qquad
E_\varepsilon(0,2\varepsilon)^T=(1,-\varepsilon)^T.
$$
在有序对 $(i_n,k_n)$ 上置
$$
v_n=e_{00}-\varepsilon_n(1+r_n)e_{01}
+\varepsilon_nr_ne_{11}.
$$
直接代入得到
$$
(a_{i_n}E_1\otimes I+a_{k_n}I\otimes E_{\varepsilon_n})v_n=0.
$$
同时
$$
\langle v_n,e_{00}\rangle=1,\qquad
\|v_n\|^2=1+\varepsilon_n^2[(1+r_n)^2+r_n^2].
$$
由于 $r_n\le1$，有
$$
\sum_n(\|v_n\|^2-1)\le5\sum_n\varepsilon_n^2
\le5\sum_{k\ge0}(k+2)^{-2\sigma}<\infty.
$$
对每个未配对位 $k\in K$，使用未归一化局部向量
$u_k=(1,-\delta_k)$，它满足 $E_{\delta_k}u_k=0$，且
$\sum_{k\in K}(\|u_k\|^2-1)=\sum_{k\in K}\delta_k^2<\infty$。

现将这些互不重叠的两位因子和单个位因子任意逐一列出。每个因子的真空坐标都恰为1。令 $g_L$ 是前 $L$ 个因子的张量积，其余位保持 Walsh 真空。则
$$
\|g_L\|^2=\prod_{\ell\le L}\|v^{(\ell)}\|^2
$$
递增并收敛至有限正数。若 $M>L$，由于新因子均有真空系数1，
$$
\|g_M-g_L\|^2
=\|g_L\|^2\left(\prod_{L<\ell\le M}\|v^{(\ell)}\|^2-1\right)\longrightarrow0.
$$
所以 $g_L$ 在原 Haar 不完全张量积中收敛到 $g\in H$，并且
$$
\langle g,1\rangle=1.
$$
特别 $g\ne0$。这也直接说明所得向量属于原 Haar 表示，而非另选的无限张量积表示。

固定任一两位因子，其加权局部和杀掉全部已包含该因子的 $g_L$；由连续性，它杀掉 $g$。同样，每个未配对位的局部 $a_kE_{\delta_k}$ 杀掉 $g$。由 $\sum_j a_j\|E_{\delta_j}\|<\infty$，可以在范数收敛级数中按这些对和单个位重新分组。因此
$$
\boxed{S_\delta^0g=0,\qquad \langle g,1\rangle\ne0.}
$$

这个 $g$ 的反阻尼系数不是正常矩族。真空系数已经为1；对每个配对位 $k_n$，其 Walsh 一次系数恰为
$$
g_{\{k_n\}}=-\delta_{k_n}(1+r_n).
$$
若试图令 $g_F=\delta_F(-1)^{|F|}m_F$，就必有
$$
m_{\{k_n\}}=1+r_n\ge1.
$$
配对位两两不同，故 $k_n\to\infty$。另一方面，真实 $V_j$ 满足 $V_j\to0$ WOT 且 $\sup_j\|V_j\|\le6$；因此对任何正常泛函 $\phi$，迹类逼近给 $\phi(V_j)\to0$。所以这里反阻尼得到的 $m_F$ 不可能等于某个正常泛函的 $\phi(V_F)$，即使完全不要求该泛函为正。
因此本例不构造正常湮灭泛函，反而说明在变形核中排除特殊 $h_\delta$ 时，必须使用完整正常矩条件；仅用无限多个平衡位或非零常数坐标都不够。

本例没有吸收实际 carry，也不声称小算子误差保留核。

