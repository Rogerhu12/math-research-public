# R174：每个不变限制的末柱集中、UHF 边界状态与负整数移位

日期：2026-11-12。作者：l2_moments。根代理预留 R174。
状态：完整证明。有限维边界不变子空间已分类；没有宣称该边界移位 unicellular，也不把边界表示当作原不变子空间的有界模型。

## 1. 记号和实际近核序列

在原空间 $H=L^2(\mathbb Z_2,\mu)$ 上，
$$
Af(y)=\alpha_{v_2(y)}f(y-1),
$$
其中 $\alpha_j>0$ 严格递减且趋于0。
本算子 $A$ 单射、拟幂零，并属于实际 UHF 代数 $\mathfrak U$。
低位局部矩阵记作 $E_j=e_{10}^{(j)}$。
对 $L\ge1$，令 $\Pi_{1,L}$、$\Pi_{0,L}$ 分别为低 $L$ 位全为1、全为0的物理柱正交投影。

固定非零闭 $A$-不变子空间 $\mathcal M$。
$A_{\mathcal M}=A|_{\mathcal M}$ 仍拟幂零，因为
$$
\|A_{\mathcal M}^n\|\le\|A^n\|.
$$
它不可能有正的下界。否则若
$\|A_{\mathcal M}x\|\ge c\|x\|$，归纳给
$\|A_{\mathcal M}^n x\|\ge c^n\|x\|$，
与谱半径为0矛盾。

因此存在单位向量 $x_n\in\mathcal M$，满足
$$
\boxed{\|Ax_n\|\longrightarrow0.}
\tag{1.1}
$$
这里不需要假设 $A_{\mathcal M}$ 有有界逆，也没有从其像稠密推出任何定量逆界。
由于 $A$ 单射，任何这样的单位序列都弱趋于0：任意弱聚点被 $A$ 杀掉，而只能为0。

## 2. 每个固定末柱上的全部质量集中

换变量 $z=y-1$，得到
$$
\|Ax\|^2
=\int_{\mathbb Z_2}
\alpha_{v_2(z+1)}^2|x(z)|^2\,d\mu(z).
\tag{2.1}
$$
若 $z$ 的低 $L$ 位不全为1，则 $z+1$ 不被 $2^L$ 整除，
所以 $v_2(z+1)\le L-1$，并有
$\alpha_{v_2(z+1)}\ge\alpha_{L-1}$。
由此对全部 $x\in H$，
$$
\boxed{
\|(I-\Pi_{1,L})x\|
\le\alpha_{L-1}^{-1}\|Ax\|.
}
\tag{2.2}
$$
对 (1.1) 的任意近核单位序列，以及每个固定 $L$，
$$
\|(I-\Pi_{1,L})x_n\|\longrightarrow0.
\tag{2.3}
$$
从而
$$
\boxed{\|\Pi_{1,L}|_{\mathcal M}\|=1
\qquad(L\ge1,\ \mathcal M\ne0).}
\tag{2.4}
$$

顺序是固定 $L$ 后取 $n\to\infty$。
没有将 $\alpha_{L-1}^{-1}$ 当作随 $L$ 一致的常数。

## 3. 唯一的 UHF 向量状态极限

令 $\omega_-$ 为 $\mathfrak U$ 的物理全1乘积状态。
如果 $E$ 只作用低 $L$ 位，则
$$
\omega_-(E)
=\langle E e_{1^L},e_{1^L}\rangle,
$$
其中 $e_{1^L}$ 是该有限张量头的单位全1向量。
这些定义在局部代数之间一致，并按范数连续延拓到 $\mathfrak U$。

若 $x_n$ 是 (1.1) 的任意单位近核序列，(2.3) 表明
$$
x_n=e_{1^L}\otimes y_n+o_H(1),\qquad
\|y_n\|\longrightarrow1
$$
对每个固定 $L$ 成立。
所以对每个局部 $E$，
$$
\langle Ex_n,x_n\rangle\longrightarrow\omega_-(E).
$$
任意 $E\in\mathfrak U$ 可用局部算子按范数逼近，而单位向量状态的范数恒为1，
故
$$
\boxed{
\langle Ex_n,x_n\rangle\longrightarrow\omega_-(E)
\qquad(E\in\mathfrak U).
}
\tag{3.1}
$$

特别，将 $E^*E$ 代入：
$$
\|Ex_n\|^2\longrightarrow\omega_-(E^*E).
$$
因此对每个非零闭 $A$-不变 $\mathcal M$，
$$
\boxed{
\|E|_{\mathcal M}\|
\ge\sqrt{\omega_-(E^*E)}
\qquad(E\in\mathfrak U).
}
\tag{3.2}
$$
$E$ 不必保持 $\mathcal M$；这里的限制是从 $\mathcal M$ 到原 $H$ 的算子。
这是向量状态的结论，不是声称整个边界表示有界嵌入 $\mathcal M$。

反过来，若单位向量序列的 UHF 状态趋于 $\omega_-$，
则把 $A^*A\in\mathfrak U$ 代入，利用 $\omega_-(A^*A)=0$，
也得 $\|Ax_n\|\to0$。
因此该状态正好刻画这些单位近核序列的 UHF 状态极限。

## 4. 状态的实际负整数边界表示

取 $\mathcal H_-=\ell^2(\mathbb N_0)$，标准基为 $e_n$。
把 $e_n$ 看作相对物理全1参考态的有限个孔：
第 $j$ 位是孔，当且仅当 $n$ 的第 $j$ 个二进位为1。
对应的 dyadic 整数是 $-1-n$。

局部矩阵代数在这些有限孔态上按通常张量规则作用。
每个低 $L$ 位矩阵在该表示中是完整的 $M_{2^L}$ 矩阵，张量一个非零尾空间，
故其范数不变。
于是局部表示按范数延拓为 $\mathfrak U$ 的等距表示 $\pi_-$。
向量 $e_0$ 是循环的，并实现 $\omega_-$：
$$
\omega_-(E)=\langle\pi_-(E)e_0,e_0\rangle.
\tag{4.1}
$$

令
$$
B=\pi_-(A).
$$
有限头截断 $A_L$ 在全1头上为0，且
$\|A-A_L\|=\alpha_L\to0$，因此 $Be_0=0$。
若 $n\ge1$，物理整数 $-1-n$ 经加1变为 $-n$，
即孔指标从 $n$ 变为 $n-1$。
相应实际权为 $\alpha_{v_2(n)}$。
所以
$$
\boxed{
Be_0=0,\qquad
Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1).
}
\tag{4.2}
$$
这是实际权得到的 backward weighted shift。
其权不是单调趋零的 Donoghue 权：每个奇数 $n$ 的权都等于固定 $\alpha_0$。
本稿不套用那些单调权假设。

因为 $\pi_-$ 等距，
$$
\|B^r\|=\|A^r\|=W_r,
$$
所以 $B$ 拟幂零。
实际初始权乘积满足
$$
\prod_{k=1}^r\alpha_{v_2(k)}=W_r.
\tag{4.3}
$$
(4.3) 也可直接从权计数核对：任意长度 $r$ 的连续整数区间中，$2^k$ 的倍数至少有 $\lfloor r/2^k\rfloor$ 个；区间 $1,\ldots,r$ 同时达到全部这些最小值。将权乘积写成 $\alpha_0^r$ 乘各比率 $\alpha_k/\alpha_{k-1}<1$ 的倍数计数幂，就得到其乘积最大，等于 $\|A^r\|$。对应 dyadic 柱具有正测度，故这里也是实际本质上确界。
由此
$$
(B^*)^r e_0=W_r e_r.
$$
(3.2) 因而给一个明确的原空间推论：
$$
\boxed{
\|(A^*)^r|_{\mathcal M}\|=W_r=\|A^r\|
\qquad(r\ge0,\ \mathcal M\ne0).
}
\tag{4.4}
$$
上界是全空间范数，下界由边界状态获得。
注意 (4.4) 是 $A^{*r}:\mathcal M\to H$；
它不是压缩 $(A_{\mathcal M}^*)^r$ 的范数等式。

更一般，有限多项式 $p(z)=\sum_{k=0}^r c_kz^k$ 满足
$$
\boxed{
\|p(A^*)|_{\mathcal M}\|
\ge
\left(\sum_{k=0}^r|c_k|^2W_k^2\right)^{1/2}.
}
\tag{4.5}
$$

## 5. 边界移位的有限维不变子空间完整分类

由于全部权都非零，
$$
\ker B^r=\operatorname{span}\{e_0,\ldots,e_{r-1}\}.
\tag{5.1}
$$
设 $\mathcal N\subseteq\mathcal H_-$ 是非零有限维闭 $B$-不变子空间，$\dim\mathcal N=r$。
限制 $B|_{\mathcal N}$ 的谱半径为0，因此在这个 $r$ 维空间上是幂零算子，
且 $(B|_{\mathcal N})^r=0$。
所以
$$
\mathcal N\subseteq\ker B^r.
$$
两边维数均为 $r$，故
$$
\boxed{
\mathcal N=\operatorname{span}\{e_0,\ldots,e_{r-1}\}.
}
\tag{5.2}
$$
反向这些初始旗显然不变，故分类完整。

这没有分类无限维闭不变子空间。
特别，本稿没有证明 $B$ 的整个不变子空间格是一条链，
也没有把“所有有限维不变子空间都是旗”误写成 unicellularity。

## 6. 原模型与边界模型之间没有非零有界交织

这一点说明为何边界分类不能直接传回原 $\mathcal M$。

### 6.1 原不变限制到边界

设 $K:\mathcal M\to\mathcal H_-$ 有界并满足
$$
KA_{\mathcal M}=BK.
$$
于是
$$
K N_j|_{\mathcal M}
=\frac{B^{2^j}}{d_j}K.
\tag{6.1}
$$
原模型中已知
$$
N_j\longrightarrow\tfrac12I
\quad\text{弱算子拓扑}.
\tag{6.2}
$$
另一方面，$\|B^{2^j}/d_j\|=1$，
而它对每个固定有限支撑向量最终为0。
故
$$
B^{2^j}/d_j\longrightarrow0
\quad\text{强算子拓扑}.
\tag{6.3}
$$
对固定 $x\in\mathcal M$，(6.1) 左侧弱趋 $\frac12Kx$，
右侧强趋0，得到 $Kx=0$。
因此 $K=0$。

### 6.2 边界到原不变限制

设 $L:\mathcal H_-\to\mathcal M$ 有界并满足
$$
A_{\mathcal M}L=LB.
$$
由 $Be_0=0$ 和 $A$ 单射，得 $Le_0=0$。
若已知 $Le_{n-1}=0$，则
$$
A_{\mathcal M}Le_n
=LBe_n=\alpha_{v_2(n)}Le_{n-1}=0,
$$
再次由单射性得 $Le_n=0$。
归纳和有限支撑向量的稠密性给 $L=0$。

综上，
$$
\boxed{
\text{两个方向都不存在非零有界交织算子。}
}
\tag{6.4}
$$
同一证明也适用于任意固定有限放大：
前向仍用 (6.2)—(6.3)，反向逐分量使用完整的根向量旗与原算子的单射性。

## 7. 与两孔首柱上界的准确关系

有限幅两孔后续笔记在某个额外有界除法关系下给
$$
\|\Pi_{0,L}|_{\mathcal M}\|
\le C(1+\log\log(L+3))^5/L.
$$
本稿无条件给的是相反端的
$$
\|\Pi_{1,L}|_{\mathcal M}\|=1.
$$
两者不矛盾。
用 $A_{\mathcal M}^{-r}$ 迁移两种柱模式会涉及无界逆；
像稠密或饱和性都没有提供所需的统一范数控制。

同样，(3.1) 是逃向物理全1边界的向量状态极限，
而非一个将 $\mathcal M$ 有界送入 $\mathcal H_-$ 的实际交织。
§6 已明确排除了这种有界传输。
因此有限维边界分类不能单独排除原慢共振核。

本稿完成了原不变限制的统一末柱集中、完整 UHF 状态下界、
实际负整数边界移位及其有限维旗分类。
一般慢共振核和完整 Hilbert 不变子空间问题仍未解决。
