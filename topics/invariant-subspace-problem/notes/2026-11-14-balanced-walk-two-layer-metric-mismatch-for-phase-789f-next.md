# 高维 up/down 正序与真实偶相位的两层度量不兼容

日期：2026-11-14（UTC）。代理：literature_audit / 789f。

**状态：下面的度量识别与不兼容式已直接核准；没有从所引随机游走定理取得新的相位上界。** 本稿保存一次定向核查，避免把同名包含矩阵或高维 harmonic 空间直接当成原物理 MP 源。

## 1. 一手来源及准确可用的正序

N. Anari、K. Liu、S. Oveis Gharan、C. Vinzant，*Log-concave polynomials II: High-dimensional walks and an FPRAS for counting bases of a matroid*，Annals of Mathematics 199 (2024), 259–299：

- [正式论文页面](https://annals.math.princeton.edu/2024/199-1/p04)。
- [作者预印本全文入口](https://arxiv.org/abs/1811.01816)。

本次取得并读到预印本完整官方文本的 §2.4、§3，特别 Lemma 3.5。它在 balanced face 权的内积中给出
\[
P_k^{\wedge}\preceq \frac{k}{k+1}P_k^{\vee}
                 +\frac1{k+1}I.
\tag{1.1}
\]
假设是纯的、零局部谱扩张的加权单纯复形；强 log 凹齐次分布是文中构造这一结构的来源。这里 \(\wedge\) 是先加再删，\(\vee\) 是先删再加。定理的伴随和 Loewner 序按各层的 balanced 权内积取，不能无条件转成原子集正交基的欧氏内积。

## 2. 乘积顶权的全部低层权

设最大层为所有大小 \(d\) 的子集，给顶层权
\[
w_d(T)=z_T=\prod_{i\in T}z_i,\qquad z_i=b_i^2>0.
\]
按论文的 balanced 递推 \(w_j(I)=\sum_{J\supset I,\ |J|=j+1}w_{j+1}(J)\)，准确有
\[
\boxed{
w_j(I)=(d-j)!\,z_I\,e_{d-j}(z_{[M]\setminus I}).
}
\tag{2.1}
\]
这是逐层求和的恒等式：对固定 \(I\)，一个 \(d\) 子集扩张有 \((d-j)!\) 种加入顺序。也可由
\(\sum_{i\notin I}z_i e_{q-1}(z_{[M]\setminus(I\cup\{i\})})=q e_q(z_{[M]\setminus I})\)
直接归纳。

专取偶临界池 \(M=2s\)，原源层 \(j=s-1\)，而最大层 \(d=s+1\)。相邻三个层的 balanced 权为
\[
\boxed{
\begin{aligned}
w_{s+1}(T)&=z_T,\\
w_s(J)&=z_J e_1(z_{[M]\setminus J}),\\
w_{s-1}(I)&=2z_I e_2(z_{[M]\setminus I}).
\end{aligned}}
\tag{2.2}
\]
特别中层并不是单纯的 \(z_J\) 权。

## 3. 与完整 \(\Gamma_1,\Gamma_2\) 的准确比较

记 \(I_{j,k}\) 为行由 \(j\) 子集、列由 \(k\) 子集索引的无权包含矩阵，\(D_j=\operatorname{diag}(b_I)\)。原完整归一幂 \(d^n/n!\) 的 Gram 准确为
\[
F_{n,j}=D_j^{-1}I_{j,j+n}
      \operatorname{diag}(z_T)I_{j,j+n}^*D_j^{-1}.
\tag{3.1}
\]
原 \(\Gamma_{n,j}\) 是先取这个完整 Gram 的逆，再压到真实 \(\ker d\cap H_j\)。

固定最大层 \(s+1\) 时，两步顶包含数组的权确与 (3.1) 的 \(F_{2,s-1}\) 相同。但是同一 balanced 复形的一步中层数组给出的矩阵是
\[
\boxed{
F^{\rm bal}_{1,s-1}
=D_{s-1}^{-1}I_{s-1,s}
\operatorname{diag}\!\left(z_J e_1(z_{[M]\setminus J})\right)
I_{s-1,s}^*D_{s-1}^{-1},
}
\tag{3.2}
\]
原来的则是
\[
F_{1,s-1}
=D_{s-1}^{-1}I_{s-1,s}
\operatorname{diag}(z_J)I_{s-1,s}^*D_{s-1}^{-1}.
\tag{3.3}
\]
乘在每个 \(J\) 上的外部权和 \(e_1(z_{[M]\setminus J})\) 一般不恒定。不能通过一个整体标量同时把 (3.2) 化成 (3.3)，也没有已付的统一条件数界允许将它丢掉。

反过来，若选择最大层 \(s\)，使其顶权对应原 \(F_{1,s-1}\)，同一个复形就没有 \(s+1\) 层，不能同时提供原 \(F_{2,s-1}\)。此外，Markov 归一化及 harmonic 正交补仍使用 (2.1) 的权，不能在完成全部 nuisance 消元前改成原 primitive 源。

## 4. 对当前相位任务的结论

真实偶相位包含同一原源的
\[
H_0=G^{-1}L-2G-A_0A_0^*,
\qquad G=\Gamma_{1,s-1},\quad L=\Gamma_{2,s-1}.
\]
式 (1.1) 是一条实际矩阵正序，但本次核查尚未给出将它的 balanced 单顶层度量与上述跨两个顶层的完整逆同时匹配的算子同构。用谱值排序、同一个包含数组或强 log 凹的名称替代这个接口都不合法。

本稿仅排除“把已发表 up/down 界直接套入当前 \(G,L\)”这一步，未否定这些随机游走方法将来经额外共同度量论证的用途，也未给相位或原 Boolean 加强序的反例。该文献支路在明确 (3.2)–(3.3) 后停止；当前数学任务仍是实际物理相位的统一预算。
