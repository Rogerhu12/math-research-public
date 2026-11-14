# 2026-11-14 — R589 有限 Frobenius 整性在真前缀上的使用范围

**状态：已证明的适用边界。** 本条只说明 R589 的 $F^p\in\mathcal A_p$ 不能自行支付困难区间的新饱和整性；不改变 R589/R596 的完整系数、极部及矩阵结论。

保持
$$
\mathcal A_p=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^p),
\qquad
\mathcal A_p[1/p]=K[w]/(w^{ps}),
$$
以及 R596 的原整格与精确前缀
$$
F=P(\boldsymbol F),\qquad P\in K_{D,k}.
$$
原精确前缀给 $\operatorname{ord}_wF\ge k$，所以若 $k\ge s$，
$$
\operatorname{ord}_w(F^p)\ge pk\ge ps.
$$
因此 $F^p$ 在上述**同一有限目标**中已经恒为零。R589 的全非线性整性在这些真实前缀上成立，但其成立本身不给最后一行 $[w^k]F$ 的额外约束。

若 $k<s$，R589 的准确界已经是
$$
v_p([w^k]P(\boldsymbol F))\ge0
$$
对全部原 $D,P$ 成立，所以此处原饱和行本来已整。

这说明：仅凭有限目标内的 $F^p$ 整性，不能跨过 $k=s$ 后的真前缀困难。它也不能用“原九坐标的任意多项式”这一全量词绕开截断零。需要继续使用的是 R596 的实际强化矩阵、非齐次极部约束与真正 Bockstein，或另付更大目标中的额外信息；不能从当前有限 $p$ 次幂结论直接记入新的 cutoff。
