# R110. 密度一输入的小辅助素数与完整迹高度

固定 $E:y^2=x^3-17x$、$F=\mathbb Q(\sqrt{-15})$，以及 R103 的
输入素数集合 $\mathcal P_F$。任取 $32/17<L<2$。
由 Fouvry（2013）§2.6 Lemma 6 所准确重述的 Mikawa 定理，
对 $\mathcal P_F$ 中相对密度一的 $p$，存在素数
$$
\ell\equiv-1\pmod{1020p},\qquad \ell\ll p^L.
$$
这里使用固定剩余类 $-1$ 和任意整数模数 $1020p$。
原文的异常数为 $O(X/\log^A X)$，可取 $A>1$，
小于输入素数的 $\asymp X/\log X$ 个数。

$\ell$ 在 $F$、$\mathbb Q(i)$ 中均惰性，且避开全部坏素数。
由 $\ell+1<p^2$ 自动得到
$$
a_\ell(E)=0,\qquad v_p(\ell+1)=1,\qquad M_\ell=1.
$$
无需再把辅助进程模数提高到 $p^2$。
同文 Lemma 7 还给：对密度一的 $p\asymp X$，在
$X^L<\ell\le2X^L$ 的上述进程中有 $\gg X^{L-1}/\log X$ 个候选。

令 $\ell+1=pu$，$U\subset G_\ell$ 为阶 $u$ 的子群。
R104 的完整实际迹为
$$
Q_{\ell,p}=\operatorname{Tr}_U X_\ell,
\qquad X_\ell=(1+\tau_{3,\ell})P[\ell].
$$
R105 的固定映射高度界给
$$
\widehat h(Q_{\ell,p})\le u^2\widehat h(X_\ell)
\ll p^{2L-2}\log p=o(p^2).
$$
又 $N_pQ=0$，而 R107 的 $E(F^{\rm ab})_{\rm tors}=E[2]$
使 $Q\ne O$ 自动等价于非挠。因此 Baker 的固定正高度下界给
$$
Q_{\ell,p}\ne O\ \Longrightarrow\ Q_{\ell,p}\notin pE(H_\ell).
$$
在同一非零前提下，真实增广长度至少为
$$
(2-L)\log_2p-\tfrac12\log_2\log p+O(1).
$$

本结果没有证明上述小候选中存在 $Q\ne O$，
也未把不可 $p$ 除升级为 R104 的 $Q\notin\Delta\ker N_p$。
未与任意指定 Kummer 核线的 Chebotarev 条件合并。

[完整证明和准确来源](../notes/2026-11-12-density-one-small-heegner-auxiliary-primes.md)。

后续 [R116](R116-density-one-nonzero-full-heegner-traces.md) 已证明所需实际完整迹
对相对密度一输入可以非零，因而支付本篇高度推论的前提；Δ原始性仍未完成。
