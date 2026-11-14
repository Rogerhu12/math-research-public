# 奇数硬端的桥创新消逆：真实对偶删除的单一范数目标

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：下面的完整消逆恒等式及等价目标已证明；所需统一有限范数界尚未证明。** 与[硬端普适归约](R297-appendix-weak-bit-hard-top-universal-strengthened-equivalence.md)结合后，全部加强相邻序的同常数问题可精确压到本文最后的一个硬端算子。本文不把这个等价目标本身称为已得统一界。

## 1. 固定物理源与真实对偶升降

取 \(M=2r+1\)、\(r\ge1\)、任意正权 \(b_i\)。定义
\[
d=\sum_i b_iE_i,\qquad C=\sum_i b_i^3E_i,
\qquad U=K_r,\quad V=K_{r-1}.
\]
旧上源 \(U\) 的合法高度只有一，低源 \(V\) 的最高高度是三。记
\[
G_1=\Gamma_{1,r},\quad C_1=G_1^{-1},
\quad L_j=\Gamma_{j,r-1}\ (j=1,2,3),
\quad B=C|_U:U\to V.
\]
上出生第二精度只按真正硬端置 \(C_2=0\)，没有 \(G_2\)。

定义实际对偶升、降
\[
e=\sum_i b_i^{-1}E_i^*,\qquad A=e^*=\sum_i b_i^{-1}E_i,
\qquad A_U=A|_U:U\to V.
\tag{1.1}
\]
\(A_U\) 的范围确在 \(V\)，因为 \([A,d]=0\)。这个 \(A\) 使用原物理内积的真实伴随，不是把去权相似当成酉变换。

有准确混合交换关系
\[
[d,e]|_{\mathcal H_j}=(M-2j)I,
\qquad [A,d^*]|_{\mathcal H_j}=(M-2j)I.
\tag{1.2}
\]
有限 Boolean 去权把 \((d,e)\) 同时共轭到无权 \(\mathfrak{sl}_2\) 对，因此真正硬端给
\[
\boxed{
e|_U=\mathcal J_{1,r},\qquad
e\mathcal J_{1,r}=0,\qquad
e\mathcal J_{2,r-1}=\mathcal J_{3,r-1}.
}
\tag{1.3}
\]
第一式因为中间层 \(d:\mathcal H_{r+1}\to\mathcal H_r\) 可逆，且 \(de f=f\) 对 \(f\in U\) 成立。第二式是高度一代数链的结束。

为核第三式，低出生高度三的完整顶逆是 \(e^3/6\)。\(e^2/6\) 是 \(d^2/2\) 对 primitive 输入的一个原像；它与 \(\mathcal J_{2,r-1}\) 之差属于 \(\ker d^2|_{\mathcal H_{r+1}}=\mathcal J_{1,r}(U)\)，恰被 \(e\) 消去。因而第三式是完整最小逆与真实代数端点之间的连接。

## 2. 从一个真实混合交换块消去上源精度逆

先有
\[
\boxed{
A\mathcal J_{1,r}=\iota_U G_1+\mathcal J_{1,r-1}A_U,
}
\tag{2.1}
\]
其中 \(\iota_U\) 是 \(U\hookrightarrow\mathcal H_r\)。证明：\(dA\mathcal J_1=A_U\)，所以它只在 \(U\oplus\mathcal J_{1,r-1}(V)\) 两个正交塔上。其 \(U\) 分量由 \(e|_U=\mathcal J_1\) 取伴随给出，正好是 \(G_1\)；另一分量由一次删除决定。

由 (1.3)，\(A\mathcal J_{3,r-1}\) 在 \(\mathcal J_{2,r-1}(V)\) 塔上的正交投影是
\[
P_{\operatorname{Ran}\mathcal J_{2,r-1}}
A\mathcal J_{3,r-1}
=\mathcal J_{2,r-1}L_2^{-1}L_3.
\tag{2.2}
\]
这里只读取指定真塔分量；更深出生的分量并没有被假定为零。

再使用真实两带式
\[
d^*|_U=\mathcal J_{1,r}C_1-\mathcal J_{2,r-1}B,
\]
\[
d^*\mathcal J_{1,r}=-\mathcal J_{3,r-1}B,
\qquad
d^*\mathcal J_{1,r-1}
=2\mathcal J_{2,r-1}L_2^{-1}L_1
-\mathcal J_{3,r-2}(C|_V).
\tag{2.3}
\]
第二式准确使用上源高度一的硬端。

现在把 \([A,d^*]=-I\) 作用于 \(\mathcal J_{1,r}(U)\subset\mathcal H_{r+1}\)，并投到 \(\mathcal J_{2,r-1}(V)\)。右侧属于正交的 \(\mathcal J_{1,r}(U)\)，投影为零。由 (2.1)–(2.3)，左侧的低塔系数为
\[
-L_2^{-1}L_3B+BG_1-2L_2^{-1}L_1A_U.
\]
因此得到完整非交换恒等式
\[
\boxed{L_3B=L_2BG_1-2L_1A_U.}
\tag{2.4}
\]

对首桥创新
\[
\Delta^*=\tfrac12(L_3BC_1-L_2B)
\]
右乘同一个物理 \(G_1=C_1^{-1}\)，(2.4) 立即给出主要消逆：
\[
\boxed{\Delta^*C_1^{-1}=-L_1A_U.}
\tag{2.5}
\]
尤其必须先合并两个真实创新项；它们分别含有的上源小精度逆不再出现在最终算子中。

## 3. 全部统一加强序的单一硬端范数目标

硬端标准化首费用准确化为
\[
\boxed{
G_1\Delta L_3^{-1}\Delta^*G_1
=A_U^*L_1L_3^{-1}L_1A_U.
}
\tag{3.1}
\]
所以固定 \(\kappa>0\) 的硬端首加强不等式等价于
\[
\boxed{\|L_3^{-1/2}L_1A_U\|^2\le\kappa.}
\tag{3.2}
\]
结合此前已证明的弱位硬端归约和 R293 强位全部高度传输，(3.2) 若对全部奇数位数、全部出生与正权统一成立，就给全部加强高度同一个 \(\kappa\)，因而也给普通相邻序同一个常数。反向也成立。出生零的唯一奇数硬端是单个位，其创新费用为零，故不留下额外例外。

等价的完整正块是
\[
\begin{pmatrix}
\kappa I_U&A_U^*L_1\\L_1A_U&L_3
\end{pmatrix}\succeq0.
\tag{3.3}
\]
这个块是当前需要证明的目标，本文没有把它宣称为已知共同 Gram。

## 4. 完整物理顶逆与可构造的提升准则

令 \(Z_{\mathrm{all}}=\prod_i b_i^2\)，并令 \(D_V\) 表示完整 \(\mathcal H_{r-1}\) 上的对角算子 \(e_J\mapsto b_J^2e_J\)。由 [R239 全出生真实倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)，
\[
\mathcal J_{3,r-1}
=\frac{(-1)^{r-1}}{\sqrt{Z_{\mathrm{all}}}}\,\mathrm{comp}\,D_V|_V,
\]
\[
\boxed{
L_3=Z_{\mathrm{all}}^{-1}P_VD_V^2|_V.
}
\tag{4.1}
\]
因此右端顶度量是完整物理对角压缩，不能将其中的压缩与逆互换。\(L_1\) 则仍是低出生的完整首逆压缩。

如果能够构造一个明确的物理映射 \(W:U\to\mathcal H_{r+2}\)，满足
\[
\mathcal J_{3,r-1}^*W=L_1A_U,
\qquad \|W\|\le\sqrt\kappa,
\tag{4.2}
\]
则把它投到 \(\operatorname{Ran}\mathcal J_{3,r-1}\) 即得 (3.2)。该方程的最小范数解是
\(\mathcal J_{3,r-1}L_3^{-1}L_1A_U\)，其范数正是待证量；仅重写这个最小解不构成费用证明。实际构造需要使用 (4.1) 的补集/乘积结构或其他已付正性。

本文消去了最容易造成伪发散的上源 \(C_1^{-1}\)，但没有单独估计并丢掉 \(L_1\)、\(L_3\) 或 \(A_U\) 中任何一个。一般统一界、真实有限反例与原 graph 接合费用仍需继续处理。
