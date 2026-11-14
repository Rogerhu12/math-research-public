# R156：固定辅助域联合输入上的原始族与准确 Sha 指数

**状态：已证明。** 日期：2026-11-12。

固定 $E=389\mathrm a1$。对 R150、R153 的十六个固定辅助
Heegner 域，保留原完整点
$$
 Q=[t_0]\operatorname{Tr}_{F[\ell]/L}P[\ell],\qquad
 \ell+1=pu,\qquad p\nmid ua_\ell(E),
$$
及范数一簇 $A$、$\mathcal O=\mathbb Z_p[\zeta_p]$。
写 $A(F)\otimes\mathbb Z_p=\mathcal O w$、
$Q=\delta^a\varepsilon w$。在 R150、R153 同一批合法普通
输入上，原整数诱导族模 $\delta$ 原始，且
$$
 \boxed{\quad
 \Sha(A/F)[p^\infty]\simeq M\oplus M,\qquad
 \operatorname{length}_{\mathcal O}M=a+1.
 \quad}
$$
原模 $\delta$ 族的最小非零辅助素因子数准确为
$$
 \nu=\max\bigl(\dim\operatorname{Sel}_p(E/F)^+,
               \dim\operatorname{Sel}_p(E/F)^-\bigr)-1.
$$
没有假设负扭曲的秩或 Sha，也没有新增类数倍数。

## 证明

Zhang（2014）Theorem 1.1 对每个域适用：$N^+=389,N^-=1$，
普通满像 $p$，且 $I_1$ 约化使 $E[p]$ 在 $389$ 分歧。
该定理针对的已是完整类群原族，并允许偶判别式。
R150 的相容分歧理想基使全部类群和与范数、辅助导数和
$\tau-1$ 交换。实际 Kummer 图逐项给
$$
 \overline c_n^A=-t_0a_\ell\,\overline c_n^{E,\mathrm{raw}}.
$$
右边系数是单位，因此同一实际族有非零剩余节点。R146
已支付全部通常局部条件；辅助惰性素数自动在二面体
$L/F$ 分裂。R144 的全精度弱刚性引理于是给深度零。
首项仍为 $(\tau-1)Q$，其自由格指数 $a+1$ 恰等于
stub 深度，得到长度等式。节点逐项零性比较和 Zhang
Lemma 8.4 给最小辅助数公式。

完整证明、有限例外、符号下界和原文页码见
[固定域完整原始族笔记](../notes/2026-11-12-fixed-field-primitive-system-and-exact-index.md)。

R149–R150、R153 已给某个固定 $F_*$ 及无穷多个相同输入，
同时有 $\widehat h(Q)=o(p)$、$a\le(p-3)/2$。本结论在此
同一集合上将长度上界加强为等式。仍未证明 $a\le1$，
故不把它登记为原曲线 Sha 初级有限性的完成。
