# R139 补篇：完整均值观测给既定比较配方的有限必要门

2026-11-20，visible-exact-astra-ac637-20261120。

**已证明。** 不计算任何 signed-profile whole-box 值，也不完成原五图50条中的任何标量，就能对 R139 的固定低族比较数给出一个有限下界。它来自原完整193观测块中保留的物理均值行；只排除一种充分上界配方，不是实际算子范数的下界。

## 1. 同一个正比较，保持原数值含义

沿用 [R139](R139-necessary-budget-for-fixed-W2C-comparison.md) 的同一个 WVC 参考、真实根、155个完整比较panel、全族参数域、独立mean与193观测。原源码是
`fourfold_codazzi_collar_dual_feedback_math._complete_modal_norm_comparison`
及 `fourfold_codazzi_signed_semiseparable_kernel_math` 中的
`PointwiseNormComparison`、`PositiveComposition`、
`complete_positive_comparison_norm`。

每个完整panel记为 $I_k$。以下是原源码实际选定的非负有向上端数，不以显示小数或下端代替：
$$
h_k=\operatorname{upper}(|I_k|),\qquad
a_k=\operatorname{upper}(A_{L,\mathrm{fee},k}\,S^{-1}_{\mathrm{norm},k}).
\tag{A.1}
$$
真实首panel的不确定根仍由原 `domain.full_length(k)` 包围。
全部family项已经包含在原 $A_{L,\mathrm{fee}}$ 中；此处不删
非局部primitive、独立mean、角导数、参数差或collar。

令原 Green 正比较的完整body核上界为 $g_{ik}\ge0$，
完整193观测块的上界为 $b_k\ge0$。
`atoms(k)` 的定义准确以 `answers=[api.one]` 开始，再对全部模式
取最大值。因此这是原**选定比较数**的恒真关系：
$$
b_k\ge1 \quad\hbox{对每一个完整panel。}
\tag{A.2}
$$
这个1保留了真实物理mean的root观测；没有把193个观测变成193个
互相独立的标量费用，也没有把mean从输入空间删除。

## 2. 完整Schur行列数的下界

记原算法的行、列上界数为 $R,C$，最后所选低族比较数为 $L$。
原 `forward(1)` 包含完整atom输出
$$
\sum_k h_k b_k a_k.
$$
原 `reverse(body=1,atoms=1)` 在每个输入panel还包含
$$
a_k\left(\sum_i h_i g_{ik}+b_k\right).
$$
所有其他项非负，逐次取上端及记录读回只会增大原配方数。
故定义有限正数
$$
S=\sum_k h_k a_k,\qquad M=\max_k a_k,
\tag{A.3}
$$
就有
$$
\boxed{R\ge S,\qquad C\ge M,\qquad L^2\ge RC\ge SM.}
\tag{A.4}
$$
其中 $L$ 按原源码先算 $\sqrt{RC}$ 再取上端；不需要原
body kernel 或任何 $p,H,K,g$ whole-box 私有包络已经可计算。
完整body和其余192个观测只会加大这个正比较，故它们无需在本
**必要性检验**中重新计算。原算子、父目标和所有范围仍保留。

结合 R139 已证明的必要条件 $L<1/128$，得到
$$
\boxed{SM\ge1/16384\quad\Longrightarrow\quad
\hbox{固定原W2C充分比较配方不能通过。}}
\tag{A.5}
$$
R139 的门下界仍至少为 $30793/30720>1$。
反向不成立：$SM<1/16384$ 不证明原门通过，也不证明 $L$ 小。

## 3. 有向保存和新的独立目标

新诊断只生成三条独立下界记录：

1. $S_\ell\le S$，来自完整和的有向下端；
2. $M_\ell\le M$，来自完整最大值的有向下端；
3. $P_\ell\le S_\ell M_\ell\le SM$，使用前两条保存后读回的下端。

每条记录保存一个准确有向下端的十进制外包球；读回必须取该球
的**下端**。判定只使用第三条读回下端与准确 $1/16384$ 比较。
不能把和或乘积的上界超过阈值当作(A.5)的证明。
所有记录先原子保存并读回，再作最终判定。

这三条属于独立的 `complete_low_family_mean_atom_necessary_floor`
目标。原 `complete_low_family_feedback_row_ratio_upper`、
`column_ratio_upper`、`norm_upper` 均没有因此完成；原五图50条
仍是0条新完成。两次原运行 `44716804300/1`、`44719196440/1`
的完整0scalar失败及其标记保持原样。

完整native输入、153个参考定义、全部4650原row/4801闭交和
family系数的私有上下文可为这个新目标重新材料化；它们没有
作为新的独立已完成norm目标保存。本诊断不调用旧producer，
也不重新求值任何已完成的旧科学界。

本文只证明(A.1)--(A.5)及保存语义。实际 $S_\ell,M_\ell,P_\ell$
仍须由公共Actions运行首次给出。若必要门排除原配方，后继可
改进均值分块比较或直接认证连续中心；实际奇异性、全频逆、
两个RHS、原7ports和最终精确族均不由这个排除结论得到。
