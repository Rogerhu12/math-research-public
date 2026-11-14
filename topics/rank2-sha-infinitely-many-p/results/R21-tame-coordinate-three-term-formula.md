# R21. Tame 参数下的三个对角项及严格尾界

**状态：已证明。** 日期：2026-11-12。会话：Astra-rank2-Sha / cm_iwasawa_routes。

本结果为 R19 的固定 $\Phi$ 给出一个有限精度公式：在有限局部 $\mathfrak p$-division 域中，归一化后的 $\chi$ 对数投影模 $p^4$ 只需三个对角系数。证明保留系数可能具有的 $p$ 分母，并准确核对第一个对角系数与不变对数矩的关系。

## 1. 记号和 tame 参数

取与 R16、R19 相同的 good split $p\ge13$、$p\ne17$，固定 $\mathfrak p\mid p$，并令
$$
F_p=K(E[\mathfrak p])_{\mathfrak P},\quad
G_p=\operatorname{Gal}(F_p/\mathbb Q_p),\quad
\rho=t(P_\pi),\quad t=-x/y.
$$
沿用赋值 $v_{F_p}(\rho)=1$，故 $v_{F_p}(p)=p-1$。字符 $\chi:G_p\to\mathbb F_p^\times$ 为 torsion 作用字符；其 Teichmüller 提升记作 $\widetilde\chi$。

对 $\zeta\in\mu_{p-1}\subset\mathbb Z_p^\times$，形式群乘法 $[\zeta]_E(T)$ 属于 $\mathbb Z_p[[T]]$。可将其定义为整数乘法在 $\mathbb Z_p$ 中的系数逐项极限；每个固定次数的系数在乘数上是连续函数，故该极限仍 integral。定义
$$
\tau_p(T)=\frac1{p-1}\sum_{\zeta\in\mu_{p-1}}
\zeta^{-1}[\zeta]_E(T)\in\mathbb Z_p[[T]].
\tag{1}
$$
它的首项为 $T$，因此具有 integral 复合逆 $T_p(U)\in U\mathbb Z_p[[U]]$。

令
$$
u=\tau_p(\rho),\qquad \beta_p=u^{p-1}.
$$
对 $g\in G_p$，$gP_\pi=[a_g]P_\pi$，且 $a_g\bmod\mathfrak p=\chi(g)$。在 $K_{\mathfrak p}=\mathbb Q_p$ 内，$a_g-\widetilde\chi(g)\in p\mathbb Z_p$，而 $[p]P_\pi=O$，故
$$
g\rho=[\widetilde\chi(g)]_E(\rho).
$$
将其代入式 (1)，可得
$$
u=e_\chi\rho,\qquad gu=\widetilde\chi(g)u.
\tag{2}
$$
又因 $\tau_p(T)=T+O(T^2)$ integral，$v_{F_p}(u)=1$。于是
$$
\beta_p\in\mathbb Q_p,\qquad v_p(\beta_p)=1.
\tag{3}
$$
其中第一条来自 $\widetilde\chi(g)^{p-1}=1$，第二条来自赋值归一化。

## 2. 对数系数的正确整性

R19 的固定函数
$$
\Phi(t)=\frac{\operatorname N_{M/K}(1+\alpha t)}
{\operatorname N_{M/K}(1-\alpha t)}
$$
在所有目标素数处属于 $1+t\mathbb Z_p[[t]]$，且 $\Phi'(0)=0$。令
$$
\mathcal V_p(U)=\Phi(T_p(U))\in1+U\mathbb Z_p[[U]],
\qquad
C_p(U)=\log\mathcal V_p(U)=\sum_{n\ge1}c_nU^n.
\tag{4}
$$
关键整性是
$$
\boxed{\quad n c_n\in\mathbb Z_p\quad(n\ge1).\quad}
\tag{5}
$$
证明：
$$
C_p'(U)=\mathcal V_p'(U)/\mathcal V_p(U)\in\mathbb Z_p[[U]].
$$
因此只能一般地断言 $v_p(c_n)\ge-v_p(n)$，不能把每个 $c_n$ 都看成 integral。由 $T_p'(0)=1$ 和 $\Phi'(0)=0$，另有
$$
c_1=0.
\tag{6}
$$

## 3. 投影、归一化与三个保留项

由式 (5)，级数 $\sum c_nu^n$ 收敛，因为
$$
v_{F_p}(c_nu^n)\ge n-(p-1)v_p(n)\longrightarrow+\infty.
$$
因此可以逐项施加连续的有限群投影。式 (2) 表明，仅当 $n\equiv1\pmod{p-1}$ 时该项保留下来。于是
$$
e_\chi\log_p\Phi(\rho)
=u\sum_{k\ge0}c_{1+k(p-1)}\beta_p^k.
\tag{7}
$$
记
$$
\mathcal Q_p=\frac{e_\chi\log_p\Phi(\rho)}u\in\mathbb Q_p.
$$
则
$$
\boxed{\quad
\mathcal Q_p\equiv
c_p\beta_p+c_{2p-1}\beta_p^2+c_{3p-2}\beta_p^3
\pmod{p^4}.
\quad}
\tag{8}
$$
下节证明包含全部系数分母的严格尾界。注意这三个系数属于 $C_p(U)$，不是未经换元的 $\log\Phi(t)$ 的三个同次系数。

为与 R16 的单位深度对接，R16 已证明
$$
v_{F_p}(e_\chi\log_p(1+\rho))=1.
$$
由式 (2)，其与 $u$ 之比为 $\mathbb Z_p^\times$ 中的元素。因此 R19 中 $e_\chi\Phi(P_\pi)$ 的单位深度恰为
$$
\nu_p=v_p(\mathcal Q_p),
\tag{9}
$$
零值仍记为无穷。特别地，式 (8) 右侧模 $p^4$ 非零即给出 R16 的 $\nu_p\le3$ 判据。这里没有遗漏单位格的归一化因子；它只乘以一个 $p$-adic 单位。

## 4. 所有 $k\ge4$ 的尾项确实落在 $p^4$

置 $n_k=1+k(p-1)$。由式 (3)、(5)，
$$
v_p(c_{n_k}\beta_p^k)\ge k-v_p(n_k).
$$
我们证明对任意 $p\ge5$、$k\ge4$，
$$
k-v_p(1+k(p-1))\ge4.
\tag{10}
$$
当 $k=4$ 时，$n_k=4p-3$ 不被 $p$ 整除，结论成立。对 $k\ge5$，有
$$
1+k(p-1)<p^{k-3}.
$$
其 $k=5$ 情形等价于 $(p-1)(p-4)>0$；由 $k$ 到 $k+1$ 的归纳成立，因为将右侧乘以 $p$ 后的增长严格超过左侧的线性增长。如果 $v_p(n_k)\ge k-3$，就会有 $n_k\ge p^{k-3}$，矛盾。故 $v_p(n_k)\le k-4$，证明式 (10)。

式 (7) 的尾级数收敛，每项都落在闭集 $p^4\mathbb Z_p$ 中，所以其和也落在其中。这证明式 (8)。本论证尤其覆盖那些 $n_k$ 本身被高次 $p$ 整除的项，并非只对最初几个 $k$ 作估计。

## 5. 第一个系数就是第 $p$ 个不变对数矩

以下只作特征 $0$ 的形式幂级数运算。令 $\operatorname{Exp}_E(z)$ 为 $z=\log_E(t)$ 的形式逆，写
$$
\operatorname{Exp}_E(z)=\sum_{m\ge1} e_mz^m,
\qquad e_1=1.
$$
定义不变对数矩的指数生成级数
$$
F(z)=\log\Phi(\operatorname{Exp}_E(z))
=\sum_{m\ge1}f_mz^m,
\qquad
f_m=\frac{\delta^m\log\Phi(O)}{m!}.
\tag{11}
$$
R19 给出 $f_1=0$。

因为 $[\zeta]_E(\operatorname{Exp}_E(z))=
\operatorname{Exp}_E(\zeta z)$，式 (1) 给出
$$
\tau_p(\operatorname{Exp}_E(z))
=\sum_{m\equiv1\ (p-1)}e_mz^m
=z+e_pz^p+e_{2p-1}z^{2p-1}+\cdots.
\tag{12}
$$
记其复合逆为 $z=z(U)$。因 $f_1=0$，在 $F(z(U))$ 的 $U^p$ 系数中，来自一次非线性换元的唯一可能较低项 $f_1z$ 已消失；其他 $z^m$ 的首个改动次数至少为 $m+p-1>p$。所以
$$
\boxed{\quad c_p=f_p=\frac{\delta^p\log\Phi(O)}{p!}.\quad}
\tag{13}
$$
由 R19 的式 (6)，进一步有
$$
c_p=-\frac{2f^p}{p}\,c_p^+(E).
\tag{14}
$$
这里左侧是 tame 参数的一个对数系数，右侧 $c_p^+(E)$ 才是 CLS 特值，二者不同记号来源务必区分。由于 $v_p(\beta_p)=1$，式 (8) 第一项的赋值恰等于 $v_p(c_p^+(E))$。

## 6. 其余两个系数的精确有限公式

为避免含混地把后两项丢弃，令 $a=e_p$、$b=e_{2p-1}$。式 (12) 的反演到所需次数为
$$
z(U)=U-aU^p+(pa^2-b)U^{2p-1}+O(U^{3p-2}).
$$
将其代入式 (11)，只需比较次数相差 $p-1$ 的项，得到
$$
\begin{aligned}
c_{2p-1}&=f_{2p-1}-pa f_p,\\
c_{3p-2}&=f_{3p-2}-(2p-1)a f_{2p-1}
 +\left(\frac{p(3p-1)}2a^2-pb\right)f_p.
\end{aligned}
\tag{15}
$$
第二式中 $f_p$ 的系数来自
$$
p(pa^2-b)+\binom p2a^2
=\frac{p(3p-1)}2a^2-pb.
$$
更高的反演项只可能通过 $f_1z$ 影响本次目标次数，而 $f_1=0$，所以没有漏项。式 (5) 独立保证 $c_{2p-1},c_{3p-2}\in\mathbb Z_p$，即使式 (15) 的各个形式指数系数单独含有 $p$ 分母。

这些式子不把 $\operatorname{Exp}_E$ 或 $z(U)$ 的形式展开当作可以在 $P_\pi$ 上直接求值的解析逆。$P_\pi$ 是 torsion，$\log_E(P_\pi)=0$；在该边界处擅自用形式逆消去对数会出错。实际求值与尾项收敛都在 integral 参数 $U=\tau_p(t)$ 中完成，式 (11)–(15) 仅用于识别有限个形式系数。

本结果给出可证明、可计算的有限表达式；它本身仍没有证明式 (8) 对无穷多个 $p$ 非零。其与 R20 的 Iwasawa 比较可以互相解释，但本证明不以 R20 为输入。
