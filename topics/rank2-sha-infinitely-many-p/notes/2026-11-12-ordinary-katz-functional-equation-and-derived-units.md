# 普通中心的函数方程：反圆变量不被反转

日期：2026-11-12。状态：角色计算已证明；文献的条件与无条件部分已逐项核原文。
本文不增加无穷素数非消失结论，也不改变 R51 的判据。

## 1. 先固定同一个 Katz 分支

令 $\tau$ 为 $K=\mathbb Q(i)$ 的复共轭，$\epsilon$ 为 $p$-进圆分角色。
使用 Galois 角色，令 $\phi$ 是本题的自对偶中心，故
$$
\phi^\tau=\epsilon\phi^{-1}.
\tag{1}
$$
普通反圆角色 $\rho$ 满足
$$
\rho^\tau=\rho^{-1}.
\tag{2}
$$
R51 的实际平方关系是
$$
F_p^{\Theta,-}(T)=U_p(T)J_p(T)^2,\qquad U_p(0)\ne0,
\quad J_p(0)=0.
\tag{3}
$$
这里需要证明的是 $J_p'(0)\ne0$，不能另换一个相似的中心。

Castella，*Tamagawa number conjecture for CM modular forms and
Rankin–Selberg convolutions*，Proc. London Math. Soc. **131** (2025)，e70089，
Theorem 2.2.1 与 Definition 2.2.2（作者 PDF pp.7–8）给出同一 CM type
的 Katz 函数方程，其角色变换为
$$
\xi\longmapsto \xi^{-\tau}\mathbb N^{-1}.
$$
在该文的几何 reciprocity 约定中 $\widehat{\mathbb N}=\epsilon^{-1}$，
所以 Galois 形式准确为
$$
\mathcal D(\xi)=\epsilon(\xi^\tau)^{-1}.
\tag{4}
$$
该处等式允许 $p$-进单位因子；本文只需要其准确的角色变换。
原文指向 de Shalit 1987，Theorem II.6.4。

[作者全文](https://web.math.ucsb.edu/~castella/Katz.pdf)；
[出版 DOI](https://doi.org/10.1112/plms.70089)。

## 2. 点点固定，不是 $T\mapsto(1+T)^{-1}-1$

由 (1)–(2) 直接计算
$$
\begin{aligned}
\mathcal D(\phi\rho)
 &=\epsilon(\phi^\tau\rho^\tau)^{-1}\\
 &=\epsilon(\epsilon\phi^{-1}\rho^{-1})^{-1}
 =\phi\rho.
\end{aligned}
\tag{5}
$$
因此 (4) **固定整个反圆直线的每一个角色**。
尤其不能从此推出
$$
J_p(T)=\pm V_p(T)J_p((1+T)^{-1}-1).
\tag{6}
$$
这不是漏掉一个可忽略的单位：式 (6) 本身的变量变换就不同。

再令 $\kappa=\langle\epsilon\rangle$。对足够小的 $s,t\in\mathbb Z_p$，
$$
\mathcal D(\phi\kappa^s\rho^t)
 =\phi\kappa^{-s}\rho^t.
\tag{7}
$$
这准确表明函数方程反射的是圆分方向。

另一方面，不带 $\tau$ 的 Tate duality 变换为
$$
\xi^*=\epsilon\xi^{-1}.
$$
它把 $\phi\rho^t$ 送到 $\phi^*\rho^{-t}$，而
$\phi^*=\phi^\tau$ 是共轭中心。若再以复共轭把中心送回 $\phi$，
也同时把 $\rho^{-t}$ 送回 $\rho^t$，仍得到 (5)。
不能只保留其中一次对反圆角色的取逆而丢掉另一次。

R48 的实结构也只给实际测度的单位缩放 push-forward；
它没有提供 (6)。在没有额外恒等式前，
$\operatorname{ord}_0J_p=1,2,3,\ldots$ 都没有被这一函数方程排除。
因此“若首导数为零则阶数至少三”，以及据此放宽首权估值门槛，
均不是已经证明的结论。

## 3. Agboola 2026：新的导出类公式仍有明确假设

独立核对的来源为 A. Agboola，
*On values of the Katz two-variable $p$-adic $L$-function*，
Annales mathématiques du Québec (2026)，
[正式出版页](https://doi.org/10.1007/s40316-026-00273-2)；
[2026-04-30 最终作者版](https://web.math.ucsb.edu/~agboola/papers/katzval.pdf)。

有用的**无条件维数比较**是 Theorem B／Theorem 7.3：
在其角色与非零局部化假设下，
$n_{\mathfrak q}(\phi^*)=n_{\mathfrak q}(\phi)-1$。
它比较两个 restricted Selmer 群的完整秩；
并未把任一个秩认定为 Mordell–Weil 秩。
所以未知的 Tate–Shafarevich 方向不会在这个减一式中自动消失。

Theorem A／Theorem 6.3 的精确零阶和 leading term 则要求 restricted
regulator 非零；§6 的完整版本另列 torsion、无有限子模与弱 Leopoldt 条件。
Remark 5.6 明确把有关配对的非退化保留为猜想。
更不能从 §10 抽出 Proposition 10.4 当作独立的无条件导出类非零定理：
§10 开头（最终版 pp.44–45）已同时假设两个 restricted regulators 非零，
并假设所列局部化秩均为一。

Theorem 9.8 本身是局部显式互反律：
在其 crystalline、局部 Hodge–Tate 权非零等假设下，
导出局部类的 logarithm／dual exponential 等于相应 Katz 导数乘一个明确因子。
构造局部类及互反等式没有另行证明该导数非零。
§10 的全局导出类比较不能抹去其运行假设。

这里还要区别两个符号：
该文 $\phi^*=\phi^{-1}\epsilon$ 是不带 $\tau$ 的 Tate dual，
而 §1 的 Katz 函数方程使用 $\mathcal D(\phi)=\epsilon(\phi^\tau)^{-1}$。
混用两者会错误地产生反圆变量的奇偶性。

## 4. 一个不满足所需量词的 theta 非消失定理

T. Finis，*Divisibility of anticyclotomic L-functions and theta functions with
complex multiplication*，Ann. of Math. **163** (2006)，767–807，
Theorem 1.1，准确地固定 split 塔素数 $p$，另取估值素数 $\ell\ne p$，
再让字符的 $p$-power 导子增长。
其“除有限多个字符”的结论不能取对角 $\ell=p$，
也不控制固定字符处的首导数。

[出版原文](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p02.pdf)。
这不否定其他对角定理存在；仅记录这一已核定理的准确适用范围。

R51 的实际 sigma 乘积、加法卷积与可核的正权 Newton 差分证书，
仍见[普通斜率工作笔记](2026-11-12-ordinary-theta-slope-convolution-and-weight-moments.md)。
