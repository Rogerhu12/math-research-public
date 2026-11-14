# 出生一既有正边表示的恢复：Newton 差的正系数展开与逐边界限

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态：旧身份的准确恢复与两项方法补充，不新登记协方差或正边定理。**

完整 Schur、条件子集协方差和全部正边公式已经逐式出现在 [R239 倒数权对偶附录 §7–7.1](../results/R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)；[R271 任意正权出生一首边 §2](../results/R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)及[原连续尾全部高度稿 §2](../results/R271-appendix-original-birth-one-all-height-polynomial-first-return-anchor.md)也已使用同一身份。本稿 §§1–2 只是为当前推导重写这些旧入口，不能计作新增结论。

这里独立补充的范围仅为 §3 对边系数 Newton 差的完整 Catalan 单项式展开，以及 §4 排除逐条边直接套相邻序的具体实际参数。它们没有证明一般相邻矩阵序，也不改变先完整逆后压缩的定义。全部陈述先限于有限个正权。

## 1. 旧完整 Schur 与实际定长协方差的恢复

取 $M\ge2$、$b_i>0$、$z_i=b_i^2$，令 $b=(b_i)$、$K=b^\perp$。记
$$
e_k=e_k(z_1,\ldots,z_M),\qquad
F_n=\frac{d^n(d^*)^n}{(n!)^2}\bigg|_{\mathcal H_1}.
$$
对 $0\le n\le M-2$，实际 primitive 精度为
$$
C_n=\left(P_KF_n^{-1}|_K\right)^{-1}.
$$
把它在 $\mathbb Cb$ 上延拓为零，记为 $\widetilde C_n$。完整 Schur 补给
$$
\widetilde C_n=F_n-\frac{F_nbb^*F_n}{b^*F_nb}.
\tag{1.1}
$$
右式消去 $b$，其在 $K$ 上正是 $C_n$，并非仅仅压缩 $F_n$。

令 $k=n+1$。在所有 $k$ 元物理子集上取概率
$$
\mu_k(I)=\frac{z_I}{e_k},\qquad z_I=\prod_{i\in I}z_i.
$$
实际完整输入列直接给
$$
\langle F_nx,x\rangle
=\sum_{|I|=k}z_I\left|\sum_{i\in I}\frac{x_i}{b_i}\right|^2,
\qquad b^*F_nb=k^2e_k.
$$
代入 (1.1)，得到对所有 $x\in\mathbb C^M$ 成立的精确式
$$
\boxed{\langle\widetilde C_nx,x\rangle
=e_{n+1}\operatorname{Var}_{\mu_{n+1}}
\left(\sum_{i\in I}\frac{x_i}{b_i}\right).}
\tag{1.2}
$$
复值方差按 $\mathbb E|X|^2-|\mathbb EX|^2$ 定义。该式已把 nuisance 均值完整消去。

在硬端 $n=M-1$，完整 $F_n$ 秩一，(1.1) 仍有严格正的标量分母，且准确为零；(1.2) 中抽样子集只有一个，方差亦为零。这里仅得到真实硬端精度零，不构造不存在的旧 $\Gamma_{M-1}$。

## 2. 旧全部实际边正权 Laplacian 的恢复

对不同 $i,j$，记 $e_r^{ij}=e_r((z_\ell)_{\ell\notin\{i,j\}})$，约定 $e_0^{ij}=1$、超出范围或负下标为零。定义
$$
\Delta_n^{ij}=(e_n^{ij})^2-e_{n-1}^{ij}e_{n+1}^{ij},
\qquad v_{ij}=b_je_i-b_ie_j.
$$
**既有正边身份。** 对全部 $0\le n\le M-1$，在完整一孔物理空间上有
$$
\boxed{\widetilde C_n
=\sum_{1\le i<j\le M}
\frac{\Delta_n^{ij}}{e_{n+1}}\,v_{ij}v_{ij}^*.}
\tag{2.1}
$$
当 $n=M-1$ 时右边按上述约定准确为零。

证明：定长占据指标 $\xi_i=1_{i\in I}$ 满足 $\sum_i\xi_i=k$，所以协方差矩阵的每行和为零。对 $i\ne j$，直接计数给
$$
\mathbb E\xi_i=\frac{z_i e_{k-1}(z_{\widehat i})}{e_k},\qquad
\mathbb E\xi_i\xi_j=\frac{z_iz_j e_{k-2}^{ij}}{e_k}.
$$
使用
$$
e_{k-1}(z_{\widehat i})=e_{k-1}^{ij}+z_j e_{k-2}^{ij},
$$
以及 $e_k=e_k^{ij}+(z_i+z_j)e_{k-1}^{ij}+z_iz_je_{k-2}^{ij}$，完全展开后交叉项消去，得到
$$
e_k\operatorname{Cov}(\xi_i,\xi_j)
=-\frac{z_iz_j}{e_k}
\left((e_{k-1}^{ij})^2-e_{k-2}^{ij}e_k^{ij}\right).
\tag{2.2}
$$
协方差行和零将对角元也唯一确定，因此
$$
e_k\operatorname{Var}\left(\sum_i g_i\xi_i\right)
=\sum_{i<j}\frac{z_iz_j\Delta_{k-1}^{ij}}{e_k}|g_i-g_j|^2.
$$
令 $g_i=x_i/b_i$ 即得 (2.1)。

## 3. 补充：每条边的自足正系数展开

下面不用额外的矩阵不等式。对任意 $m$ 个正变量 $t_1,\ldots,t_m$，设 $t_A=\prod_{i\in A}t_i$。逐个比较两个乘积的有序子集对，得到
$$
\boxed{
e_n(t)^2-e_{n-1}(t)e_{n+1}(t)
=\sum_{r=0}^{\min(n,m-n)}
\frac{1}{r+1}\binom{2r}{r}
\sum_{\substack{|A|=n-r,\ |B|=2r\\A\cap B=\varnothing}}
t_A^2t_B,
\quad 0\le n\le m.}
\tag{3.1}
$$
确切地，对固定的重复指标集合 $A$ 和单次指标集合 $B$，$e_n^2$ 中的系数是 $\binom{2r}{r}$；$e_{n-1}e_{n+1}$ 中的系数是 $\binom{2r}{r-1}$。二者之差为显示的正整数。$r=0$ 时第二项系数为零。

应用于删去 $i,j$ 后的 $m=M-2$ 个变量，得到：对全部合法 $0\le n\le M-2$，每个 $\Delta_n^{ij}$ 严格正。于是 (2.1) 是一个保持完整物理指标的正边表示；其核恰为 $\mathbb Cb$，因为 $v_{ij}^*x=0$ 对所有边等价于全部 $x_i/b_i$ 相同。故 $C_n>0$。特别 $n=0$ 时 $\Delta_0^{ij}=1$，(2.1) 准确给出 $I-bb^*/\sum_i b_i^2$。

## 4. 补充：实际参数明确排除逐边相邻序

目标的一孔相邻序等价于
$$
C_{n+1}\preceq C_n C_{n-1}^{-1}C_n
\quad\text{在 }K\text{ 上}.
\tag{4.1}
$$
(2.1) 尚未支付 (4.1)，而且各条边系数本身甚至未必满足相同的标量相邻序。

例如取真实四位权 $b=(6,6,1,1)$，选边 $(1,2)$，其余两个平方权为一。该边在三个高度的系数为
$$
a_0=\frac1{74},\qquad
a_1=\frac3{1441},\qquad
a_2=\frac1{2664}.
$$
直接交叉相乘得
$$
a_1^2<a_0a_2,
\qquad
9\cdot74\cdot2664=1{,}774{,}224
<1441^2=2{,}076{,}481.
$$
所以单条边的标量系数比较不能代替完整矩阵序；不同物理边的共同作用必须保留。这只是对一个拟用推理的准确范围说明，不是一般相邻矩阵命题的反例。
