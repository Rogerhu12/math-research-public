# R100. 固定辅助域上的单素数 Heegner 类与实际点判据

## 固定一次辅助域

对已证秩二的 $E:y^2=x^3-17x$，Bump–Friedberg–Hoffstein
主定理 (i) 给一个固定虚二次域 $F=\mathbb Q(\sqrt D)$，使
$2,17$ 都分裂且 $L'(E^D,1)\ne0$。故 $E^D(\mathbb Q)$ 秩一、
$\Sha(E^D/\mathbb Q)$ 有限。这个 $F$ 不随 $p$ 改变。

令 $\mathcal P_F$ 为在 $F$ 和 $\mathbb Q(i)$ 均分裂、
$p\ge5$ 且 $p\nmid17D$ 的素数集合；它是无穷集合。
CM 两线在 $p$-惯性上的特征不同而被复共轭交换，故
$E[p]$ 是不可约 $G_\mathbb Q$ 模，且 $E(F)[p]=0$。

## 最小支撑与初级有限性的准确等价

记 $t_p=\operatorname{corank}_{\mathbb Z_p}\Sha(E/\mathbb Q)[p^\infty]$。
在 $F$ 上完整 Selmer 的两个符号余秩为 $2+t_p,1$。
BCGS Theorem A 的不可约版本与 Corollary A 因而给
\[
\operatorname{ord}(\boldsymbol\kappa^{\rm Heeg})=1+t_p.
\]
这里 ord 是非零类所需的最少不同 Kolyvagin 素数数目，
不是整个系统的整除指数；无需其 Theorem B 的满像假设。
所以
\[
\Sha(E/\mathbb Q)[p^\infty]\text{有限}
\iff \exists\ell:\kappa_\ell^{\rm Heeg}\ne0.
\]

对合法单素数 $\ell$，令
\[
M_\ell=\min(v_p(\ell+1),v_p(a_\ell(E)))>0,\quad
D_\ell=\sum_{j=1}^{\ell}j\sigma_\ell^j,\quad
Y_\ell=\sum_{\tau\in\mathcal C_\ell}\tau D_\ell P[\ell].
\]
$P[\ell]$ 是固定模参数化下的实际环类域 Heegner 点。
无 $p$-挠条件给 Kummer 类的唯一下降；Howard 的规范化是
可逆映射 $\chi_\ell^{-1}$ 再张量生成元，并非未经证明的标量单位。
因此进一步准确有
\[
\boxed{\quad
\Sha(E/\mathbb Q)[p^\infty]\text{有限}
\iff\exists\ell:\ Y_\ell\notin p^{M_\ell}E(F[\ell]).
\quad}
\]

## 原始类的局部条件和证书

基底 Heegner 迹为扭点，故基底类为零。
Howard 的完整模 $p^{M_\ell}$ 有限／奇异关系、横截局部条件
给原始单素数类在辅助 $\ell$ 的局部化为零；其复共轭符号为正，
于是它下降到通常的 $\operatorname{Sel}_{p^{M_\ell}}(E/\mathbb Q)$。
这里用完整系数层的论证，没有把模 $p$ 关系直接提升。

对固定已知点 $P=(-1,4),Q=(9,24)$，除掉其格指数的有限素因子后，
该原始类来自 MW，当且仅当某 $a,b\bmod p^{M_\ell}$ 满足
\[
Y_\ell-aP-bQ\in p^{M_\ell}E(F[\ell]).
\]
若 $(a,b)\ne(0,0)$，即给初级有限的充分证书。
另一个充分证书是在其他好约化位检验
$\bar Y_\ell\notin p^{M_\ell}\widetilde E(k_v)$。
有限域中匹配若干点不能证明上述全局归属；
单个点非零或非扭也不能替代不可整除性。

## 证明、来源与剩余任务

[完整证明及 BFH、BCGS、Howard、Zhang 的准确引用](../notes/2026-11-12-one-prime-heegner-class-and-explicit-points.md)
已由根端全文核对，所有关键原始来源已读。
额外要求 $\ell$ 在 $\mathbb Q(i)$ 惰性时，$a_\ell=0$，
每个固定 $p$ 都有无穷多个合法 $\ell$；但未证明可将上面的
充要判据收窄到这个子族。
当前仍须对无穷多个 $p$ 证明真实 $Y_\ell$ 的不可整除性。
