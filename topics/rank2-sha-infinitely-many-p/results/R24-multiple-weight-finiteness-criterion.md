# R24：显式局部单位基、全权对数矩与双权初级有限判据

**可信度：已证明。** 本结果拓宽充分条件，不证明其对无穷多个素数成立。固定
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),
$$
并始终设 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$。取 $\pi=\psi(\mathfrak p)$，所以 $\pi\bar\pi=p$。沿用 R19 的固定函数 $\Phi$ 与迹序列 $a_n$，以及 R20 的 $\rho_E$、$\Delta\times\Gamma$、$\widetilde\chi$、$e_\chi$ 和参数
$$
\rho_E(\gamma)=1+p,\qquad \mathcal A=\mathbb Z_p[[T]],\qquad T=\gamma-1.
$$
记 $\delta=\omega_E^{-1}$，其中 $\omega_E=dx/(2y)$；这是 $O$ 附近的不变微分算子，在坐标上满足 $\delta x=2y$。令
$$
\lambda_k=\delta^k\log\Phi(O).
$$
本文的 $\lambda_k$ 是一个对数矩，不是 Iwasawa 的 $\lambda$ 不变量。

**后续加强。** [R25](R25-lambda-controls-finite-selmer.md) 已利用原始 Galois 模的无有限子模性质，将本文的双权结论加强为整个初级部分为零；[R26](R26-maximal-ideal-order-and-finite-selmer.md) 又把它统一为 $G_p\notin(p,T)^2$ 的有限 Selmer 判据。以下保留只用中心零点阶所得的有限性证明。

## 0. 结论

存在一个下文明确构造的局部单位塔基 $u_\infty$，使
$$
e_\chi\bigl(\Phi(P_{\pi^n})\bigr)_n=H_p(T)u_\infty,
\qquad H_p(T)=(T-p)^2G_p(T).\tag{0.1}
$$
$H_p$ 与 R20 的特征级数只差 $\mathcal A$ 单位，且
$v_pH_p(0)=\nu_p$。

对每个 $k\ge p$、$k\equiv1\pmod{p-1}$，定义
$$
x_k=(1+p)^k-1,
\qquad
c_k^+(E)=(\Omega_E^+)^{-k}L(\bar\psi^k,k)\in\mathbb Q.
$$
则有完整赋值比较
$$
\boxed{\quad
v_pH_p(x_k)=v_p\lambda_k
=v_p\bigl((k-1)!c_k^+(E)\bigr).
\quad}\tag{0.2}
$$
这里比较的是中心级数在指定权的特化；不声称它与 $\nu_p$ 的完整赋值相同。

特别地，以下双权条件足以证明初级有限：
$$
\boxed{\quad
\min\left\{
v_{\mathfrak p}(a_{(p-3)/2}),\,
v_{\mathfrak p}(a_{p-2})
\right\}\le3
\quad\Longrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}.
\quad}\tag{0.3}
$$
等价的临界值表述是
$$
v_p(c_p^+)\le3
\quad\text{或}\quad
v_p(c_{2p-1}^+)\le2.\tag{0.4}
$$
第一种情形由 R20 已给出整个初级部分为零；本节的中心零点阶论证对第二种情形先给有限，R25 的有限 Selmer 比较进一步给初级部分为零。

写 $G_p(T)=g_0+g_1T+\cdots$。两个权同时不能满足 (0.3)，恰好等价于
$$
g_0\in p^2\mathbb Z_p,
\qquad g_1\in p\mathbb Z_p.\tag{0.5}
$$
若第一条件成立而 $g_1$ 是单位，则权 $2p-1$ 的矩恰有赋值 $3$，给出原权 $p$ 判据没有覆盖的有限性证书。第 6 节还给出 $g_1\bmod p$ 的明确矩公式。

## 1. 定义在 Zp 上的严格 Lubin–Tate 坐标

由于 $[\pi](t)\equiv t^p\pmod p$ 且线性项为 $\pi t$，$\widehat E$ 是参数 $\pi$ 的 Lubin–Tate 形式群。Lubin–Tate 的严格同构定理给出
$$
X=X(t)\in t\mathbb Z_p[[t]],\qquad X'(0)=1,
$$
将它变成满足
$$
[\pi]_{\mathcal F}(X)=\pi X+X^p\tag{1.1}
$$
的形式群 $\mathcal F/\mathbb Z_p$。

这个同构定义在 $\mathbb Z_p$ 上，并非仅在非分歧扩张上存在。可直接参见 Coates–Wiles 1978，§1，p.5，式 (5) 前的严格同构陈述；他们的 $\mathcal O_{\mathfrak p}$ 在分裂情形就是 $\mathbb Z_p$。

选相容扭点 $[\pi]P_{\pi^{n+1}}=P_{\pi^n}$，令
$$
\xi_n=X(P_{\pi^n}).
$$
于是 $\pi\xi_{n+1}+\xi_{n+1}^p=\xi_n$。特别地，$\rho=\xi_1$ 满足
$$
\rho^{p-1}=-\pi,\qquad
v_{F_1}(\rho)=1,\qquad v_{F_1}(p)=p-1.\tag{1.2}
$$
对 $\zeta\in\mu_{p-1}$，$\zeta X$ 与 (1.1) 交换且线性项为 $\zeta X$，由 Lubin–Tate 同态的唯一性，
$[\zeta]_{\mathcal F}(X)=\zeta X$。故 $\rho$ 是 $\widetilde\chi$ 的本征向量。

## 2. 一个完全显式的范数相容局部单位基

令 $\beta\in1+p\mathbb Z_p$ 是满足
$$
\beta^{p-1}=1-\pi\tag{2.1}
$$
的唯一元素；其存在唯一性由 Hensel 引理给出。定义
$$
f(t)=\beta-X(t),\qquad
w_n=\beta-\xi_n\in U_n.
$$

**引理 1。** $(w_n)_n$ 范数相容，且
$$
u_\infty=e_\chi(w_n)_n
$$
是 $U_\infty^\chi$ 的 $\mathcal A$ 基。

**证明。** $F_{n+1}/F_n$ 的 $p$ 个共轭 $\xi_{n+1}$ 正是
$Y^p+\pi Y-\xi_n$ 的全部根。因此
$$
N_{F_{n+1}/F_n}(\beta-\xi_{n+1})
=\beta^p+\pi\beta-\xi_n
=\beta-\xi_n.
\tag{2.2}
$$
同样，在形式群上有精确恒等式
$$
\prod_{z\in\mathcal F[\pi]}
\bigl(\beta-(X+_{\mathcal F}z)\bigr)
=\beta-(\pi X+X^p).
$$
没有被省略的范数常数。

只需证明第一层的 $e_\chi w_1$ 为 $U_1^\chi$ 的基，因为 R20 已证明
$U_\infty^\chi$ 自由秩一及
$U_\infty^\chi/TU_\infty^\chi\simeq U_1^\chi$。
在第一层，$e_\chi$ 消去常数 $\beta$，而
$$
\log(1-\rho/\beta)
=-\sum_{n\ge1}\frac{\rho^n}{n\beta^n}.
$$
第 $n$ 项的 $F_1$ 赋值为 $n-(p-1)v_p(n)$。最小值 $1$ 只在 $n=1,p$ 出现；其他项至少为 $2$，这是 R16 使用的同一估计。利用 (1.2)、(2.1)，最低项为
$$
-\frac\rho\beta-\frac{\rho^p}{p\beta^p}
=-\frac\rho\beta
\left(1-\frac{\pi}{p(1-\pi)}\right)
\equiv(-1+\bar\pi^{-1})\rho
\pmod{\rho^2}.
\tag{2.3}
$$
R7 的统一非异常性给出 $\bar\pi\not\equiv1\pmod p$。故首系数非零，且 $e_\chi$ 保留它。R16 已证明 $U_1^\chi$ 是秩一格、其所有对数的赋值至少为 $1$；(2.3) 因而证明 $e_\chi w_1$ 原始。Nakayama 引理现在给出 $u_\infty$ 为塔上的基。$\square$

## 3. 连续 Coates–Wiles 矩与 Λ 等变性

对 $v_\infty\in U_\infty$，令 $F_v(t)\in\mathbb Z_p[[t]]^\times$ 为 Coleman 级数，满足
$$
F_v(t(P_{\pi^n}))=v_n\qquad(n\ge1).
$$
其存在唯一性见 Coleman 定理，亦见 Rubin 的 Remark 12.5 和 Coates–Wiles 的 §§2、4。所有 $v_n$ 为主单位，所以 $F_v(0)\in1+p\mathbb Z_p$。对 $k\ge1$ 定义
$$
\operatorname{CW}_k(v_\infty)
=\left.\delta^k\log F_v(t)\right|_{t=0}\in\mathbb Z_p.
\tag{3.1}
$$
整性可直接检查：$\delta\log F_v=(\delta F_v)/F_v$ 为整幂级数，$\delta$ 的系数也整；继续作用 $\delta$ 保持整性。

下面明确说明需要的连续性，避免仅在有限群环上写等式。赋予整幂级数系数逐项的 $p$-进拓扑。集合
$$
\{F\in\mathbb Z_p[[t]]^\times:F(0)\in1+p\mathbb Z_p\}
$$
为紧空间。在每个固定扭点上的取值连续，因为整系数级数的尾项被该扭点的幂一致控制。只取其中满足全部实际有限层等式
$$
N_{F_{n+1}/F_n}\bigl(F(t(P_{\pi^{n+1}}))\bigr)
=F(t(P_{\pi^n}))\qquad(n\ge1)
$$
的子集 $\mathscr C$。每层取值与有限域范数均连续，所以 $\mathscr C$ 闭，因而紧。Coleman 存在定理给出 $\mathscr C\to U_\infty$ 满射。

这个映射也单射。若两个级数的全部扭点取值相同，它们之差在无限多个不同的开单位圆盘点上为零。一个非零 $F\in\mathbb Z_p[[t]]$ 的非零系数赋值有最小值 $\mu$；除以 $p^\mu$ 后，存在第一个单位系数，其位置记为 $d$。Weierstrass 分解将 $F$ 写成 $p^\mu$、次数 $d$ 的 distinguished polynomial 和幂级数单位之积。最后一个因子在开单位圆盘上处处非零，故 $F$ 在该圆盘至多有 $d$ 个零点（按重数计）。上述无限个零点因而强迫差级数为零。

因此 $\mathscr C\to U_\infty$ 是紧空间到 Hausdorff 空间的连续双射，从而为同胚。式 (3.1) 只依赖 $F_v$ 的前 $k$ 个系数和 $F_v(0)^{-1}$，所以 $\operatorname{CW}_k$ 是连续的 $\mathbb Z_p$-线性映射。这里不需要另证形式范数算子的拓扑性质。

对 $\sigma\in\Delta\times\Gamma$，互反律及 Coleman 唯一性给出
$$
F_{\sigma v}(t)=F_v([\rho_E(\sigma)]t).
$$
不变微分的链式法则于是给出
$$
\operatorname{CW}_k(\sigma v)
=\rho_E(\sigma)^k\operatorname{CW}_k(v).
\tag{3.2}
$$
当 $k\equiv1\pmod{p-1}$ 时，$\operatorname{CW}_k(e_\chi v)=\operatorname{CW}_k(v)$。
有限群环在完成群环中稠密，且 $x_k=(1+p)^k-1\in p\mathbb Z_p$，故由连续性，(3.2) 延伸为
$$
\operatorname{CW}_k(A(T)v)
=A(x_k)\operatorname{CW}_k(v)
\qquad(A\in\mathcal A).
\tag{3.3}
$$

## 4. 显式基在全部所需权上的矩都是单位

记 $A=\bar\pi\bmod p\in\mathbb F_p^\times$。有 $A\ne1$。

**引理 2。** 在约化形式群上，
$$
\delta^p=A\delta.\tag{4.1}
$$
并且对 $k=1+j(p-1)$、$j\ge1$，
$$
d_k:=\operatorname{CW}_k(u_\infty)
\equiv-A^{j-1}(A-1)\pmod p.
\tag{4.2}
$$
特别地，每个 $d_k$ 都是 $\mathbb Z_p$ 单位。

**证明。** 为固定 Hasse 标量的方向，在严格 LT 坐标中直接计算。令
$B(X)=\log_{\mathcal F}'(X)\in\mathbb Z_p[[X]]$；这是归一化的不变微分系数，且 $B(0)=1$。微分
$\log_{\mathcal F}(\pi X+X^p)=\pi\log_{\mathcal F}(X)$，得到
$$
B(X)=\left(1+\frac p\pi X^{p-1}\right)B(\pi X+X^p).
$$
约化模 $p$ 并只看到次数 $p-1$，
$$
B(X)=1+A X^{p-1}+O(X^p),\qquad
\delta=(1-A X^{p-1}+O(X^p))\frac d{dX}.
$$
特征 $p$ 中导子的 $p$ 次复合仍是导子；它也平移不变，所以 $\delta^p$ 为 $\delta$ 的常数倍。取作用于 $X$ 后在 $O$ 的值，Wilson 定理给出该常数为
$-A(p-1)!=A$。这证明 (4.1)，并明确排除了倒置 $A$ 的规范错误。

令
$$
\ell(t)=\delta\log f(t)=\frac{\delta f(t)}{f(t)}
\in\mathbb Z_p[[t]].
$$
由于严格坐标导数为一，$\ell(O)=-\beta^{-1}\equiv-1\pmod p$。
对任意可逆函数 $f$，整数系数的 Bell 多项式恒等式给出
$$
\frac{\delta^pf}{f}
\equiv\delta^{p-1}\ell+\ell^p\pmod p.\tag{4.3}
$$
解释其模 $p$ 简化：完整 Bell 展开中对应分拆
$\sum j m_j=p$ 的系数是
$p!/\prod m_j!(j!)^{m_j}$。除了 $m_1=p$ 和 $m_p=1$ 两种分拆外，分母均不含 $p$，故其系数被 $p$ 整除；保留下来的两项正是 (4.3)。

由 (4.1)，左边为 $A\ell$，所以
$$
\delta^{p-1}\ell=A\ell-\ell^p.
\tag{4.4}
$$
对任意整数 $m\ge1$，(4.1) 还给出
$\delta^{m+p-1}=A\delta^m$。因 $p-1\ge1$，对 $j\ge1$ 可反复使用，得到
$$
\begin{aligned}
\delta^{1+j(p-1)}\log f(O)
&=\delta^{j(p-1)}\ell(O)\\
&=A^{j-1}\bigl(A\ell(O)-\ell(O)^p\bigr)\\
&=-A^{j-1}(A-1)
\end{aligned}
\pmod p.
$$
$\ell(O)$ 的约化属于 $\mathbb F_p$，故其 $p$ 次幂等于自身。又相应权的 $\operatorname{CW}_k$ 保留 $\chi$ 投影，所以这正是 (4.2)。$\square$

注意 $j=0$ 不使用 (4.2)：此时 $d_1=-\beta^{-1}$ 本身也是单位，但它的约化为 $-1$。

## 5. 全权比较与初级有限性

由 [Coleman 塔笔记](../notes/2026-11-12-phi-coleman-tower.md)，固定 $\Phi(t)$ 本身就是 $\varepsilon_\infty=(\Phi(P_{\pi^n}))_n$ 的 Coleman 级数，且 $e_\chi\varepsilon_\infty$ 生成 $C_\infty^\chi$。故引理 1 的基唯一确定 $H_p\in\mathcal A$：
$$
e_\chi\varepsilon_\infty=H_p(T)u_\infty.
$$
R20 的中心因子及主猜想比较给出 (0.1)，并给出
$$
s_p^\infty\le\operatorname{ord}_{T=p}H_p,
\tag{5.1}
$$
其中 $s_p^\infty$ 是 $\operatorname{Sel}_{p^\infty}(E/\mathbb Q)$ 的 $\mathbb Z_p$ 余秩。R4 给出 $s_p^\infty\ge2$；R7 使用的 $p$-parity 定理与根数 $+1$ 给出它为偶数。

对 $k\equiv1\pmod{p-1}$、$k\ge p$，(3.3) 和引理 2 给出精确等式
$$
\lambda_k=H_p(x_k)d_k,
\qquad d_k\in\mathbb Z_p^\times.\tag{5.2}
$$
这直接证明 (0.2) 的第一个等号。整个证明没有借用 Rubin Theorem 12.10 与 CLS 插值式之间的全权阶乘规范化比较。

为解释第二个等号及临界值，R19 式 (11)–(12) 对每个奇数 $k\ge3$ 给出
$$
\lambda_k=-2f^k(k-1)!\,
(\Omega_E^+)^{-k}L_{\mathfrak f}(\bar\psi^k,k),
\qquad f=34(1+i).
\tag{5.3}
$$
这里 $\Omega_E^+=\Omega_\infty$ 已在局部输入笔记中证明。因为所需 $k\equiv1\pmod{p-1}$ 且 $p\equiv1\pmod4$，所以 $k\equiv1\pmod4$；$\psi$ 的有限字符取值于 $\mu_4$，其 $k$ 次幂仍是原字符，故 $\bar\psi^k$ 的精确导子仍为 $\mathfrak f$。因此此处的 $L_{\mathfrak f}$ 就是 primitive $L$ 函数。其归一化值属于 $K$（CLS Theorem 2.3），又由 $E/\mathbb Q$ 的复共轭关系为实数，故属于 $K\cap\mathbb R=\mathbb Q$。

所有所列 $p$ 都有 $p\nmid2f$。由 (5.3)，
$$
v_p\lambda_k=v_p((k-1)!c_k^+).
$$
这给出 (0.2) 的第二个等号，并保留了完整阶乘。

更一般地，令
$$
e_k=v_p(x_k-p)=1+v_p(k-1).
$$
由 (5.1)，$(T-p)^{s_p^\infty}$ 整除 $H_p$，所以
$$
v_p\lambda_k\ge e_k s_p^\infty.
\tag{5.4}
$$
于是
$$
v_p((k-1)!c_k^+)<4e_k
\quad\Longrightarrow\quad s_p^\infty=2
\quad\Longrightarrow\quad\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}.
\tag{5.5}
$$
这类多权充分判据已包含在 CLS 2009 的 Proposition 2.4、Theorem 2.5 及式 (32)–(33) 的论证中；这里补的是与原固定 $\Phi$、局部基及两个最低权的准确比较，不将充分判据的形式推广声称为新的无穷性定理。

对 $k=p,2p-1$，均有 $e_k=1$；此外
$$
v_p((p-1)!)=0,\qquad v_p((2p-2)!)=1.
$$
R19 的 $\lambda_{2n+3}=4a_n$ 现在给出 (0.3) 与 (0.4)。若后一个权成功而第一个权失败，单用本节的余秩比较只能推出有限；初级部分为零的加强使用 R25 的额外模块比较。

## 6. 两个权恰好检测了哪两个系数

记
$$
k_1=p,\quad k_2=2p-1,\quad x_1=x_{k_1},\quad x_2=x_{k_2}.
$$
二项式展开给出
$$
x_1\in p^2\mathbb Z_p,
\qquad x_2\equiv-p\pmod{p^2},
\qquad v_p(x_i-p)=1.
\tag{6.1}
$$
因此
$$
G_p(x_1)\equiv g_0\pmod{p^2},\qquad
G_p(x_2)\equiv g_0-pg_1\pmod{p^2}.
\tag{6.2}
$$
由于 (5.2) 的 $d_{k_i}$ 为单位，两个 $\lambda_{k_i}$ 都被 $p^4$ 整除，当且仅当 (6.2) 的两项都属于 $p^2\mathbb Z_p$。相减即得等价条件 (0.5)。

特别地，若 $g_0\in p^2\mathbb Z_p$、$g_1\in\mathbb Z_p^\times$，则
$$
v_p\lambda_p\ge4,\qquad v_p\lambda_{2p-1}=3,
\qquad v_p c_{2p-1}^+=2.
\tag{6.3}
$$
在此情况下还得到一个没有未知周期的明确式。因为
$$
\frac{(x_2-p)^2}{p^2}\equiv4\pmod p,
\qquad d_{2p-1}\equiv-A(A-1)\pmod p,
$$
由 (5.2)、(6.2) 可得
$$
\boxed{\quad
g_1\equiv
\frac{\lambda_{2p-1}}{4p^3A(A-1)}
=\frac{a_{p-2}}{p^3A(A-1)}
\pmod p,
\qquad\text{只要 }\lambda_p\in p^4\mathbb Z_p.
\quad}\tag{6.4}
$$
这里 $A$ 任取其在 $\mathbb Z_p^\times$ 的提升；分母中的 $A(A-1)$ 为单位，而 $\lambda_{2p-1}\in p^3\mathbb Z_p$ 由 (6.2) 已知，故商确实整。

两个条件的组合不依赖基的选择：若 $G_p$ 改乘单位 $v(T)$，则常数项乘 $v(0)$；在 $g_0\in p^2$ 的前提下，一次项模 $p$ 也只乘 $v(0)$。因此 (0.5)、(6.3) 的有无与 R20 的 $g_p$ 给出同样判定；(6.4) 的数值则采用本文明确选定的 LT 基。

**更多同支权在固定门槛 $3$ 下不提供新条件。** 对 $k=1+j(p-1)$、$j\ge1$，有
$$
x_k\equiv(1-j)p\pmod{p^2}.
$$
若 $p\nmid j$，则
$$
v_p(x_k-p)=1,\qquad
G_p(x_k)\equiv g_0+(1-j)pg_1\pmod{p^2}.
$$
所以 (0.5) 成立时全部这些权的矩都在 $p^4\mathbb Z_p$ 中；若 $p\mid j$，则 $v_p(x_k-p)\ge2$，中心二重因子本身已迫使 $v_p\lambda_k\ge4$。反之，两个初始权中的成功当然也是某个同支权的成功。因此“存在一个同支权使 $v_p\lambda_k\le3$”与 (0.3) 完全等价。对于更靠近中心的权，(5.5) 使用更大的门槛，不能与这里的固定门槛混淆。

## 7. 当前跨素数缺口

R20 的小深度路线只需 $g_0\notin p^2$。现在一个更宽的充分条件是
$$
g_0\notin p^2\mathbb Z_p
\quad\text{或}\quad
g_1\notin p\mathbb Z_p.
\tag{7.1}
$$
它等价于固定迹序列在两个指数
$(p-3)/2$、$p-2$ 处不同时落入 $\mathfrak p^4$。第 6 节明确说明了权 $2p-1$ 新增的信息，而非仅重写权 $p$ 的条件。

已知的 $\mu=0$ 不保证 (7.1)：一个级数可以常数项属于 $p^2$、一次项属于 $p$、二次项为单位。固定函数与塔范数也不保证 (7.1)，人为中心因子笔记已经给出这类一般方法的严格边界。仍需证明原 $\Phi$ 的这两个指定矩对无穷多个 $p$ 不同时有额外整除，或找出其他足以完成初级有限性的跨素数信息。

## 引用

- J. Coates, A. Wiles, *On p-adic L-functions and elliptic units*, J. Austral. Math. Soc. Ser. A **26** (1978), 1–25：§1 p.5 的严格 LT 同构，Theorem 4 的同类范数相容局部基，§4 的 Coates–Wiles 同态；[DOI](https://doi.org/10.1017/S1446788700011459)。本文对所需基、范数、原始性及全部相关权的单位值给出了直接证明。
- K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*：Remark 12.5 的 Coleman 插值，Proposition 12.2、Theorem 12.9 的 Selmer 与特征理想比较；[作者讲义](https://swc-math.github.io/notes/files/99RubinCM.pdf)。本结果不使用其 Theorem 12.10 的全权印式。
- J. Coates, Z. Liang, R. Sujatha, *The Tate-Shafarevich group for elliptic curves with complex multiplication* (2009)：Theorem 2.3、Proposition 2.4 式 (28)、Theorem 2.5、式 (32)–(33)；[arXiv:0901.3832](https://arxiv.org/abs/0901.3832)。高阶迹的常数使用 2010 后续论文勘误后的版本，如 R6、R19。
- 本仓库 R4、R7、R16、R19、R20，以及 `notes/2026-11-12-phi-coleman-tower.md`、`notes/2026-11-12-coleman-mu-lambda-attempt.md`。
