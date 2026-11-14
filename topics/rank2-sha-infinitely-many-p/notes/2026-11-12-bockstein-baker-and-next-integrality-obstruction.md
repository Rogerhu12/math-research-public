# 两行 Bockstein 后：Baker–Brumer 的确切边界和下一次整除障碍

**状态：已证明的边界与未闭合尝试。** 使用 R35–R36 的 $D_p$、$\lambda_p$、$N_p$、$F_p=\theta^2G_p$，其中 $\theta=T-p$。本文不修改已经冻结的结果。

R36 已得到实际整泛函和具体的 $p=13$ 非零值。这里继续检查两条可能把它推进到变动素数的路线：对具体 $G_p(p)$ 应用 Baker–Brumer，以及在它为零时继续作 Bockstein 除法。

## 1. 所需的不等式不是有限层对数非零

R36 对每层 $n$ 和每个合格辅助素位 $w$ 给出准确取值
$$
\mathscr V_{p,n,w}
=p^{b_p}u_nG_{p,n}\in R_n,
$$
所以其中心评价为
$$
e_n(\mathscr V_{p,n,w})
=-\frac{p^{b_p}}{1+i}G_p(p)\pmod{p^n}.
\tag{1.1}
$$
要从这对泛函得到证书，需要某个 $n$ 满足
$$
v_p(G_p(p))+b_p<n.
\tag{1.2}
$$
所有层同时失败，当且仅当 $G_p(p)=0$；单个有限层的 $G_{p,n}$ 在 $\mathbb Q_p[\Gamma_n]$ 中非零并不排除这件事。

此前 unit-character-nonvanishing 笔记用有限阿贝尔层的 Kronecker 极限公式及 Baker–Brumer 定理，证明目标有限字符的椭圆单位局部对数非零。对每一个有限阶 $\tau$，这个方法至多给出相应
$F_p(\tau(\gamma)-1)\ne0$。有限阶字符的点与 $T=p$ 不同；前者的非零性没有给出 (1.2)。

一个直接的代数检验是
$$
F(T)=(T-p)^3,\qquad G(T)=T-p.
$$
所有有限阶点 $T=\zeta-1$ 上 $F(T),G(T)$ 都非零，因为有限阶单位根 $\zeta$ 不等于 $1+p$；但 $G(p)=0$，且 $e_n(G\bmod\omega_n)=0$ 对每个 $n$ 成立。这个例子还具有 $\mu=0$，故加上该条件也不修复推理。

## 2. 范数相容的真实单位也可人为增加这个中心零

这个边界不只是任选形式级数造成的。设 $\varepsilon_n=\Phi(P_{\pi^n})$ 是投影前的实际代数单位，$z_n=e_{\widetilde\chi}\varepsilon_n$ 是 R36 的字符分量。以加法记号定义
$$
z'_\infty=(\gamma-(1+p))z_\infty.
$$
投影前的乘法记号为
$$
\varepsilon'_n=\frac{\varepsilon_n^{\gamma_n}}{\varepsilon_n^{1+p}},
\qquad z'_n=e_{\widetilde\chi}\varepsilon'_n.
\tag{2.1}
$$
每个 $\varepsilon'_n$ 仍是代数的全局单位，范数相容性仍成立。字符分量本身只在 $p$-完备化中使用，不将 Teichmüller 幂误称为代数单位。其局部 Coleman 系数是
$$
F'_p(T)=\theta F_p(T)=\theta^3G_p(T).
$$
在每个有限阶字符上，新增因子 $\zeta-(1+p)$ 非零，故原有有限字符对数的非零性也保留。然而两行一次 Bockstein 后的中心二阶值必为零。

系统 (2.1) 失去了生成整个 $C_\infty^{\widetilde\chi}$ 的原始性；它不是本曲线原始 $\Phi$ 的反例。它严格说明：只使用“各层为代数单位、范数相容、各有限字符局部对数非零”这三项输入的 Baker–Brumer 论证，不能推出原始系统的中心阶恰为二。还必须实质使用一个能控制中心零阶的原始性或整格输入。

## 3. 中心二阶值的 Mellin 表达不是一个已知的有限代数线性型

把 $F_p\in\mathbb Z_p[[\Gamma]]$ 看作 $\Gamma\simeq\mathbb Z_p$ 上的有界测度 $\mu_p$。用 $a\in\mathbb Z_p$ 参数化 $\gamma^a$，有
$$
F_p(T)=\int_{\mathbb Z_p}(1+T)^a\,d\mu_p(a).
$$
在 $T=p$ 处逐项求导合法，得到
$$
G_p(p)=\frac{F_p''(p)}2
=\frac1{2(1+p)^2}
\int_{\mathbb Z_p}a(a-1)(1+p)^a\,d\mu_p(a).
\tag{3.1}
$$
又因 $F_p'(p)=0$，可以写成
$$
G_p(p)
=\frac1{2(1+p)^2\log_p(1+p)^2}
\int_{\mathbb Z_p}(1+p)^a
\log_p((1+p)^a)^2\,d\mu_p(a).
\tag{3.2}
$$
这里的测度和 LT 归一化随 $p$ 变化。尚无证明把 (3.1) 化成有限个固定代数单位对数的代数系数线性型；(3.2) 还包含平方矩。Baker–Brumer 的定理处理有限个对数的代数系数**线性**关系，并不自动处理这个积分或平方关系。

即便逐个有限层展开为有限字符的代数单位对数，也必须得到随 $n$ 足够强的赋值上界来推出 (1.2)。域次数已经为 $(p-1)p^{n-1}$，辅助主化单位还随 $n$ 改变；定性的有限层非零不能作为这样的上界。本次没有取得可用的定量估计。

## 4. 第三次中心除法需要一个新的整行关系

写 R36 的两行整泛函为
$$
f_1=p^{b_p}\mathcal L_n/\theta,\qquad
f_2=v_w/\theta
\quad\text{于}\quad
\operatorname{Hom}_{R_n}(U_{\mathfrak q},R_n).
$$
令 $\bar f_i=e_n\circ f_i$。想在不额外乘入 $p$ 的情形再除一次中心，必须找到
$$
\bar a\bar f_1+\bar b\bar f_2=0
\quad\text{于}\quad
\operatorname{Hom}_{R_n}(U_{\mathfrak q},S_n),
\tag{4.1}
$$
其中 $\bar a,\bar b$ 至少一个为 $S_n$ 的单位。取提升 $a,b\in R_n$ 后，R36 的 $\ker e_n=\theta R_n$ 说明
$$
(a f_1+b f_2)/\theta
$$
在整个 $U_{\mathfrak q}$ 上是整泛函。因为关系是原始的，可以把 $(a,b)$ 补成 $\operatorname{GL}_2(R_n)$ 矩阵，保留另一行，再计算新的外积值。

但 $e_n((f_1\wedge f_2)(\epsilon_{2,n,w}))=0$ **不蕴含** (4.1)。只需看明确反例：
$$
U=R_n^2,\quad f_1=e_1^*,\quad f_2=e_2^*,\quad
\epsilon=\theta e_1\wedge e_2.
$$
外积值是 $\theta$，中心评价为零；两行的模中心约化却仍是 $S_n^2$ 的对偶基，不存在任何原始关系 (4.1)。零值可能来自被评价元素在整外积格中的非原始性，而不是两行的退化。

因此不能仅因 $G_p(p)=0$ 就宣称第三次 Bockstein 泛函存在，更不能不断形式微分到特征级数的第一个非零导数，便得到整 Rubin–Stark 证书。R36 中前两次除法的整性来自两个实际来源：严格 MW 字符检测辅助类，以及全局 Kummer–Artin 互反式。当前还没有为 (4.1) 找到相应的新全局输入。

另外，固定辅助素数只能在有限多个 $K_n$ 中完全分裂；R35 是对每个 $n$ 重新选择 $\mathfrak q$。不能把固定 $w$ 的 $S$-单位格误当成所有层上相容的秩二自由 $\Lambda$-模，再对它任意求导。

## 5. 现有 fine Mordell–Weil 结构结果没有消去这一障碍

另核对了 M. F. Lim 的 *On fine Mordell-Weil groups over $\mathbb Z_p$-extensions of an imaginary quadratic field*，arXiv:2308.04096v3，Theorem 5.4 与 Question 3。其单 $\mathfrak p$ 塔定理先假设每个有限层的 fine Sha 有限；完整 fine Selmer 的相应特征理想公式仍在 Question 3 中提出。

对本题的基层 $K$，usual $\pi^\infty$ Kummer 局部项在 $v\ne\mathfrak p$ 处为零：局部 $\pi$-完备化在那里至多有限，张量可除群后消失。故该文的 $\pi$-primary fine Selmer 在基层就是 R34 的严格 Selmer。R34 的全局 MW 局部满射又给 R35 (5.1)，所以基层 fine Sha 实际等于普通 $\Sha(E/K)[\pi^\infty]$。于是其 $n=0$ 假设已经包含本题逐个 $p$ 的有限性，不能用该定理补上第三次整行关系或变动 $p$ 的非零性。

这次尝试的结论是：已把第三次操作需要的新条件准确定位到 (4.1)，而非模糊地要求更多导数；尚未证明该条件或 (3.1) 的跨素数非零。原 R35 保留的较宽目标仍是 $N_p$ 对无穷多个 $p$ 有限。

## 来源

- A. Brumer，*On the units of algebraic number fields*，Mathematika 14 (1967)，121–124，[DOI](https://doi.org/10.1112/S0025579300003703)。本题已用的准确有限字符形式见 unit-character-nonvanishing 笔记及其中的 Sharifi Theorems 1.5.17、1.5.21 引用。
- M. F. Lim，*On fine Mordell-Weil groups over $\mathbb Z_p$-extensions of an imaginary quadratic field*，Theorem 5.4、Question 3，[作者预印本](https://arxiv.org/pdf/2308.04096)。
- 本仓库 R34–R36；(2.1) 的单位构造只用于检验推理边界，不替换原始椭圆单位生成元。
