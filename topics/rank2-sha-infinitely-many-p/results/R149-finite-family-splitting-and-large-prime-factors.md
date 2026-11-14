# R149：十六个固定辅助域的分裂补集与小余因子联合选择

日期：2026-11-12。**状态：已证明的筛法结论；实际迹非零另需输入。**

## 结论

对固定偶数 $B$、$D\mid B$ 及单位剩余类集合
$\mathcal S\subset(\mathbb Z/D)^\times$，置
$\epsilon=|\mathcal S|/\varphi(D)$。若 $1/2<\vartheta<1$，则
$$
 \#\{\ell\le x:\ell\text{ 素},\ \ell\equiv-1\ (B),
    \ p=P^+(\ell+1)>x^\vartheta,\ p\bmod D\in\mathcal S\}
 \le\left(64\epsilon\frac{1-\vartheta}{\vartheta^2}+o(1)\right)
                          \frac{x}{\varphi(B)\log x}.
$$
常数 $64$ 不依赖固定模数；误差的阈值允许依赖它们。

因此取十六个平方类独立的固定虚二次域 $F_j$，并让
$B$ 包含其全部导子，则“$p$ 在所有域都惰性”的坏类密度为
$2^{-16}$。在 $\vartheta=667/1000$ 时，坏辅助素数的准确
系数小于 $0.00075$，而 R126 的固定进程 Fouvry 下界余量
大于 $0.001359$。

删除该补集后，仍有 $\gg_B x/\log x$ 个实际素数对，满足
$$
 \ell\equiv-1\pmod B,\qquad
 p=P^+(\ell+1)>x^{667/1000},\qquad
 \ell+1=pu,\qquad u\ll p^{333/667},\qquad u^2=o(p),
$$
且 $\ell$ 在每个 $F_j$ 惰性，$p$ 至少在一个 $F_j$ 分裂。
有限鸽巢原理给某个固定 $F_j$ 的无穷分裂输入。
还可以同时删去任意 $o_B(x/\log x)$ 个辅助素数例外。

## 完整证明

[完整证明](../notes/2026-11-12-finite-family-splitting-and-large-prime-factors.md)。

原两线性式是 $a+Dt$ 与 $Bm(a+Dt)-1$。完整局部根数为
$0,1,2$，从而奇异级数恰为
$\mathfrak S(Bm)D/\varphi(D)$。
Selberg 权取 $R=N^{2/5}$，误差为
$O(N^{4/5}(\log N)^6)$；Euler 乘积的 Markov 截断给主常数
小于 $62.5$，留余量取 $64$。
关键的准确平均是
$$
 \sum_{m\le M}\frac{\mathfrak S(Bm)}m
                    \le\frac B{\varphi(B)}(\log M+1),
$$
因此不会留下可随域集增长的未知 $B$ 常数。

## 尚未由本结果支付

将此选择用于 $E389$ 所需的十六域原完整类群首 jet 证书，
现已由 [R150](R150-sixteen-fields-and-complete-class-st-jets.md) 单独支付并在其 §7 合并。
该证明保留总和；本筛法没有拿单中心非零代替总和，也没有将两个正密度集合直接相交。
即使这些原点输入完成，本结果仍不证明 $a\le1$、指定 CM
纤维两矩非零，或主课题的 Sha 无穷初级有限性。
