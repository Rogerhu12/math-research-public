# 严格 Lubin–Tate 坐标给字符分子的三对角重建

**可信度：已证明。** 日期：2026-11-12。本文补充 [字符有理核笔记](2026-11-12-character-resolvent-rational-kernel.md)。分子 $U_p$ 虽依赖目标字符，但其模 $p^4$ 的系数可由固定椭圆形式指数的三个对角系数重建，不需要另输入未知的 tame 坐标系数。所得公式仍含随 $p$ 增长的指数，尚未给出跨素数非消失。

## 1. 严格 LT 坐标及精确投影

设 $\pi=\psi(\mathfrak p)$，$v_p(\pi)=1$。取 R24 使用的 Lubin–Tate 形式群
$$
[\pi]_{\mathrm{LT}}(X)=\pi X+X^p.
$$
令其规范形式对数为 $\ell_{\mathrm{LT}}$，首项为 $X$。取严格整同构
$$
H(X)=\exp_E(\ell_{\mathrm{LT}}(X))\in X\mathbb Z_p[[X]],
\qquad H'(0)=1.
\tag{1}
$$
对 $\omega\in\mu_{p-1}\subset\mathbb Z_p^\times$，
$[\omega]_{\mathrm{LT}}(X)=\omega X$。

选择非零 LT 核点 $\xi$，使 $H(\xi)=\rho=t(P_\pi)$。于是
$$
\xi^{p-1}=-\pi,\qquad \sigma_\omega\xi=\omega\xi.
\tag{2}
$$
对正整数 $n$ 定义
$$
A_n=\sum_{j\ge0}
[X^{1+j(p-1)}]H(X)^n\,(-\pi)^j.
\tag{3}
$$
因为 $H$ 整，级数收敛，且精确地
$$
e_\chi(\rho^n)=\xi A_n,\qquad
\rho_\chi=\xi A_1,\qquad A_1\in1+p\mathbb Z_p.
$$
所以
$$
\boxed{\quad s_n=\frac{e_\chi(\rho^n)}{\rho_\chi}
=\frac{A_n}{A_1}.\quad}
\tag{4}
$$
模 $p^4$ 时，(3) 可直接截断为 $0\le j\le3$。

这不是把 $\exp_E$ 的无限级数在 torsion 边界代入。式 (3) 中求值的是整同构 $H$；下文对 $\exp_E$ 的使用只在有限个形式系数上进行。

## 2. 低次数 LT 对数的误差很深

由 $\ell_{\mathrm{LT}}(\omega X)=\omega\ell_{\mathrm{LT}}(X)$，到次数 $3p-2$ 为止可写
$$
\ell_{\mathrm{LT}}(X)=
X+\ell_1X^p+\ell_2X^{2p-1}
+\ell_3X^{3p-2}+O(X^{4p-3}).
$$
比较
$\ell_{\mathrm{LT}}(\pi X+X^p)=\pi\ell_{\mathrm{LT}}(X)$ 的三个系数，得到
$$
\begin{aligned}
\ell_1&=\frac1{\pi-\pi^p},\\
\ell_2&=\frac{p\pi^{p-1}\ell_1}{\pi-\pi^{2p-1}},\\
\ell_3&=
\frac{\binom p2\pi^{p-2}\ell_1+
(2p-1)\pi^{2p-2}\ell_2}
{\pi-\pi^{3p-2}}.
\end{aligned}
\tag{5}
$$
因此
$$
v_p(\ell_1-\pi^{-1})\ge p-2,\qquad
v_p(\ell_2)\ge p-2,\qquad
v_p(\ell_3)\ge p-3.
\tag{6}
$$
令
$$
Y(X)=X+\frac{X^p}{\pi}.
$$
则 $\ell_{\mathrm{LT}}-Y$ 到所需次数的系数均在 $p^{p-3}\mathbb Z_p$ 中，且最低次数为 $p$。

还须核查与椭圆指数复合不会损失过多精度。置
$$
e_{n,m}=[z^m]\exp_E(z)^n.
$$
椭圆不变导子为
$$
\delta=\sqrt{1+68t^4}\frac d{dt}.
$$
它保持 $\mathbb Z_p[[t]]$，故
$$
e_{n,m}=\frac{\delta^m(t^n)(0)}{m!},
\qquad v_p(e_{n,m})\ge-v_p(m!).
\tag{7}
$$
当 $m\le3p-2$ 时，$v_p(m!)\le2$。

在
$\exp_E(Y+R)^n-\exp_E(Y)^n$ 中，$R=\ell_{\mathrm{LT}}-Y$ 的每个因子至少有次数 $p$、系数赋值至少 $p-3$。若总次数不超过 $3p-2$，一个包含 $R$ 的项至多还能出现一个来自 $Y$ 的 $X^p/\pi$ 因子；若同时有两个这样的因子，最低次数已为 $3p$。因此连同 (7) 的阶乘，最坏赋值仍至少为
$$
p-3-1-2=p-6\ge7.
$$
于是对所有正整数 $n$，
$$
\boxed{\quad
[H(X)^n]_{\le3p-2}
\equiv[\exp_E(Y(X))^n]_{\le3p-2}
\pmod{p^4}.
\quad}
\tag{8}
$$
这里 $p\ge13$，所以上述误差远高于所需精度。

## 3. 三个固定指数系数的显式组合

记
$$
B_p=\binom{p-1}{2}
$$
（此符号仅用于本文，和前篇的有理主单位因子不混用），并定义
$$
\boxed{\quad
Z_n=
-\pi B_p e_{n,p}
-2(p-1)\pi^2 e_{n,2p-1}
-\pi^3e_{n,3p-2}.
\quad}
\tag{9}
$$
则
$$
A_n\equiv Z_n\pmod{p^4}.
\tag{10}
$$
特别地 $Z_n\in\mathbb Z_p$，$Z_1\in1+p\mathbb Z_p$。

为证明 (10)，将 (8) 代入 (3) 的 $j\le3$ 截断。令
$n_l=1+l(p-1)$。展开 $Y^m$ 后，
$$
[X^{n_j}]\exp_E(Y)^n
=\sum_{l=0}^j
e_{n,n_l}\binom{n_l}{j-l}\pi^{-(j-l)}.
$$
所以 $e_{n,n_l}$ 的总系数为
$$
\pi^l\sum_{j=l}^3(-1)^j\binom{n_l}{j-l}
=-\pi^l\binom{n_l-1}{3-l}.
$$
最后用有限二项和
$$
\sum_{a=0}^{M}(-1)^a\binom Na
=(-1)^M\binom{N-1}{M}.
$$
$l=0$ 时该系数为 $-\binom03=0$；其余三个系数正是 (9)。这个有限求和中的消去不允许推广成在 torsion 点对不收敛的椭圆指数作无限代入。

由 (4) 和 (10)，
$$
\boxed{\quad
s_n\equiv\frac{Z_n}{Z_1}\pmod{p^4}.
\quad}
\tag{11}
$$

## 4. 完整恢复 U_p 模 p^4

写 $p=4r+1$。字符有理核笔记已经证明
$$
\frac{U_p(X)}{D_p(X)}
=\sum_{j\ge0}s_{4j+1}X^{4j},
\qquad\deg U_p\le p-5.
$$
因此
$$
\boxed{\quad
U_p(X)\equiv
\left[
D_p(X)
\sum_{j=0}^{r-1}\frac{Z_{4j+1}}{Z_1}X^{4j}
\right]_{\le p-5}
\pmod{p^4}.
\quad}
\tag{12}
$$
$D_p$ 已由 R29 及 Padé 笔记从固定级数 $\mathscr L$ 重建；(9)–(12) 则从固定 $\exp_E$ 给出全部所需字符分子。因此在这个有限精度内，$U_p$ 不再需要独立的未知坐标系数。

不过输入仍包括
$$
e_{4j+1,p},\quad e_{4j+1,2p-1},\quad
e_{4j+1,3p-2},\qquad 0\le j\le r-1.
$$
它们的指标与数量随 $p$ 变化；式 (12) 不提供一个固定维数的 Frobenius 判定，也不为原始目标的加权迹提供非零保证。

## 5. 直接以三个原始 Coates–Wiles 矩给目标标量

还可不先恢复分子，而直接写目标：
$$
\lambda_m=\delta^m\log\Phi(O).
$$
因为 $\delta\log\Phi$ 在原点有整系数，$\lambda_m\in\mathbb Z_p$。同样的有限形式复合证明给
$$
\boxed{\quad
\mathcal Q_p\equiv
\frac1{Z_1}
\left[
-\pi B_p\frac{\lambda_p}{p!}
-2(p-1)\pi^2\frac{\lambda_{2p-1}}{(2p-1)!}
-\pi^3\frac{\lambda_{3p-2}}{(3p-2)!}
\right]\pmod{p^4}.
\quad}
\tag{13}
$$

这里尾项须单独核查，因为 $\log\Phi(H(X))$ 的系数未必整。若写
$$
\log\Phi(H(X))=\sum c_mX^m,
$$
则 $m c_m\in\mathbb Z_p$：这是整形式单位 $\Phi(H(X))$ 的对数导数整性。投影后第 $j$ 项的赋值至少为
$$
j-v_p(1+j(p-1)).
$$
当 $j=4$ 时，$4p-3$ 为单位；当 $j\ge5$ 时，
$1+j(p-1)<p^{j-3}$，故该下界至少为四，并且实际趋于无穷。因此仅保留 $j\le3$ 合法。

为了使用 (8) 的误差论证，注意
$$
[z^m]\log\Phi(\exp_E(z))=\lambda_m/m!
$$
也满足 (7) 的赋值下界。所以有限复合误差仍在 $p^{p-6}$ 中。最后使用与 §3 完全相同的有限二项和，得到 (13)，再除以 $A_1\equiv Z_1$。

式 (13) 的三个阶乘赋值分别为一、一、二；它们不能被遗漏。R20 已证明 $\mathcal Q_p$ 与首权的截断赋值比较，因此这里出现后两权并不自动产生新的有限性条件。若要使用第二权检测 $g_1$，仍需 R24 的独立权重点比较。

## 6. 目前得到的结论范围

本文消除了“未知 tame 坐标”这一计算输入：三对角项完全由固定椭圆形式指数和显式 $\pi$ 因子给出。它也说明正确字符核与普通范数分母可以在同一有限精度中重建。

但这些重建式没有给 $G_p\notin(p,T)^2$ 的无穷性，也没有给中心有限类群商的满阶循环因子数量上界。有限次数约为 $p$ 的有理核不等于整个 Coleman Mellin 输入在乘法坐标中有理；R23 的超越性障碍仍然适用。

## 依赖

- R24：严格 LT 模型、整同构及目标字符约定。
- R19、R21：固定 $\Phi$、原目标标量及对数导数整性。
- R29 与 Padé 笔记：$D_p$ 的精确重建。
- 字符有理核笔记：$U_p$ 的次数、系数整性及 (12) 所用展开。
- 本文 §2–5 已给所有新截断、误差和有限组合的证明。
