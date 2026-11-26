# 有限头坐标的非 Fredholm 性与实际 Haar 头图的无限余维

作者：AI-assisted GPT-6 Astra Pro；会话 `Astra-ISP-8542378f-20261127`。日期：2026-11-27（Asia/Taipei）。

**状态：已证明；前稿的直接原空间推论。** 本稿接[原尾根重数与投影距离](../results/R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md)。旧 [R164](../results/R164-invariant-projections-high-bit-essential-rigidity.md) 已给相关矩形角中的 Fredholm 算子必须是真正同构。本稿不把这条旧结构重复计为新结论：新增的是前稿根重数排掉整个有限头同构情形，因此每个真有限头坐标映射都不 Fredholm。下述原核/像证明还明确定位失败在哪个实际空间。

## 1. 每个真有限头坐标映射都不 Fredholm

取原 Haar 分解
$$
H=\mathbb C^N\otimes K,\qquad N=2^m,\qquad
A^N=\beta_{N-1}I_N\otimes B_m,
\qquad K=L^2(\mathbb Z_2,\mu).
\tag{1.1}
$$
$B_m$ 是原权 $\alpha_{m+v_2(z)}$ 的尾，单射、稠密像且拟幂零。
令 $Q=Q_0\otimes I_K$ 为任意秩 $k$ 的有限头投影，$0<k<N$。
设 $M$ 是闭 $A$-不变空间，并记
$$
F=Q|_M:M\longrightarrow QH,\qquad L=\operatorname{Ran}F.
\tag{1.2}
$$

**命题。** $F$ 不 Fredholm。更确切地：

1. $\ker F$ 若非零，则维数无限；
2. 若 $L$ 闭，则 $\operatorname{codim}_{QH}L$ 要么为零，要么无限；
3. 若 $F$ 有下界且 $M\ne0$，则 $L$ 是非零、真、无限维、无限余维的闭子空间。

**证明。** 因 $Q$ 与 $I_N\otimes B_m$ 交换，
$$
\ker F=M\cap Q^\perp H
$$
对 $A^N$ 不变。若该核有限维且非零，则 $A^N$ 在其上单射，但其限制仍拟幂零。有限维拟幂零算子是 nilpotent，不能单射，矛盾。这证明第一项。

对 $x\in M$，
$$
(I_k\otimes B_m)Fx
=\beta_{N-1}^{-1}F A^Nx\in L,
\tag{1.3}
$$
故 $L$ 及其闭包在整个原 $QH\simeq K^{\oplus k}$ 上对 $I_k\otimes B_m$ 不变。若 $L$ 闭且其正交补为非零有限维，则该补对 $I_k\otimes B_m^*$ 不变。$B_m$ 稠密像，故 $B_m^*$ 单射；它同样拟幂零。因此上述有限维非零限制再次既单射又 nilpotent，不可能。这证明第二项。

若 $F$ Fredholm，闭像及有限核、有限余核由前两项升级为核零和余核零。于是 $F$ 是到整个 $QH$ 的有界同构，恰被前稿的根重数定理排除。因此 $F$ 不 Fredholm。

最后，$F$ 有下界时，核零且像闭。像若为整个 $QH$，仍与根重数定理矛盾，所以其余维无限。$M\ne0$ 时像非零；由 (1.3)、$B_m$ 单射且拟幂零，像不可能非零有限维。第三项得证。$\square$

没有把“有下界”直接当成“满射”；相反，第三项证明这里有下界时必须出现无限余维的真实像。

## 2. R231 的 Haar 高位图必须保留真、无限余维底空间

本节只用 [R231](../results/R231-bounded-high-bit-graph-linear-root-cost-and-central-escape.md) 的**原 Haar** 设置，不使用负整数边界表示中的 R239 图。

R231 假设 $0\ne M=\ker T$ 是原 $A$-不变闭空间。对某一位 $j$，其真实 Walsh 删除满足
$$
\|b_jf\|\ge\beta_j\|f\|\qquad(f\in M),\qquad \beta_j>0.
\tag{2.1}
$$
抽出第 $j$ 位，在该位的 Walsh 基中
$$
b_j(u,v)=(v,0).
$$
所以坐标投影 $Q_j(u,v)=(0,v)$ 在 $M$ 上有同一个下界，且 R231 已得到
$$
M=\{(G_jy,y):y\in L_j\},
\qquad L_j\subset H^{\widehat j}\text{ 闭},
\qquad G_j\in B(L_j,H^{\widehat j}).
\tag{2.2}
$$
该删位空间仍包含第 $0,\ldots,j-1$ 位的完整有限头，不能删除这份重数。

取完整头 $N=2^{j+1}$。$Q_j$ 是此头内秩
$$
k=2^j
\tag{2.3}
$$
的真正有限头投影；换 Walsh 基只作这个有限头的酉基变换。因此 §1 第三项直接给
$$
\boxed{
L_j\ne0,\qquad
\dim L_j=\infty,\qquad
\operatorname{codim}_{H^{\widehat j}}L_j=\infty.
}
\tag{2.4}
$$

这里排除满射使用的是完整原幂
$$
A^{2^{j+1}}=\beta_{2^{j+1}-1}
I_{2^{j+1}}\otimes B_{j+1}.
$$
若 $L_j$ 是整个删位空间，将从同一个 $A|_M$ 得到
$I_{2^j}\otimes B_{j+1}$ 的有界 $2^{j+1}$ 次根；根重数要求
$2^{j+1}\mid2^j$，不成立。

不能只使用 R231 的
$R_j^2=\eta_jB|_{L_j}$ 来声称重数矛盾：当 $j\ge1$，二确实整除剩余的低头重数 $2^j$。必须保留原 $A$ 的整个 $2^{j+1}$ 次幂，才能得到 (2.4)。

R231 转回物理基时，$G_j-I$ 是 $L_j$ 上的有界可逆算子，所以物理图参数化的底空间仍是同一个 $L_j$；(2.4) 同样适用，不因基变换而换成整个尾。

## 3. 仍需处理的实际核/像

本推论把已付头图中的未知底空间准确限定为一个有无限余维的真闭空间。它没有构造其中的循环向量，也没有证明其范围对尾伴随不变。后续若对该底空间使用原尾的全空间逆、字符或根分类，必须先支付相应的定义域与满射；目前只能使用 (1.3) 的实际单向不变性。
