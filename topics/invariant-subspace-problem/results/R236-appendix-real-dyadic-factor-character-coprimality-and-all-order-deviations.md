# R236 附录：真实最低因子、字符互素与全阶可和偏离

日期：2026-11-13（UTC）。作者：central_review。供主会话独立核验后登记。
状态：本稿给完整证明的充分判据及其全阶应用。
它保留列明的临界核候选值，一般 Hilbert ISP 仍未完成。

## 1. 原模型与一条一般判据

沿用原 Haar 模型 $H=L^2(\mathbb Z_2)$、原单射拟幂零算子 $A$、
代数
$$
\mathcal A=\overline{\mathbb C[I,A]}
$$
及其唯一字符 $\chi$。
令 $X=X_b$ 为任意非零复 $\ell^2$ 主 first
在任意复 $\ell^2$ 指数权下的实际闭实现。
记原双线性配对
$$
\mathcal B(f,g)=\int f(y)g(-1-y)\,d\mu(y).
$$
R176 给全部自然幂域、最高系数可逆的自然多项式闭性、
完整 $C$ 自伴性、核内一阶有界限制及循环图核心。
Dyadic gauge 满足
$$
\gamma_\zeta(X)=U_\zeta XU_\zeta^*=X+D_\zeta,\qquad
U_\zeta\operatorname{Dom}X^p=\operatorname{Dom}X^p,
\tag{1.1}
$$
其中 $D_\zeta$ 是实际真解析有限头。

取首一自然多项式
$$
P(X)=X^p+\sum_{k<p}E_kX^k,\qquad E_k\in\mathcal A,
\tag{1.2}
$$
准确域为 $\operatorname{Dom}X^p$。
其字符多项式为
$$
p_0(z)=z^p+\sum_{k<p}\chi(E_k)z^k.
\tag{1.3}
$$

**定理 1（实际因子—字符互素判据）。**
假设存在有限 dyadic 子群 $\mu_H$，使对每个
$\zeta\notin\mu_H$，都有实际恒等式
$$
\gamma_\zeta(P(X))-P(X)
=
A^{r_\zeta}Q_\zeta(X)
\quad\text{于 }\operatorname{Dom}X^p,
\tag{1.4}
$$
其中 $r_\zeta$ 是非负整数，
$Q_\zeta\in\mathcal A[z]$ 的次数不超过 $p$。
这些是实际有界系数的有限多项式，
不是仅有形式系数阶数的断言。
令
$$
q_{\zeta,0}(z)=\chi(Q_\zeta(z)).
$$
若
$$
\boxed{\gcd(p_0,q_{\zeta,0})=1
\qquad(\zeta\notin\mu_H),}
\tag{1.5}
$$
则
$$
\ker P(X)=0,\qquad
\overline{\operatorname{Ran}P(X)}=H.
\tag{1.6}
$$
对每个循环的自然域向量 $\xi$，
$P(X)\xi$ 非零且循环。

常数最高系数非零时先除以该标量即可；
定理不要求不同 $\zeta$ 的因子或逆有一致范数预算。

### 1.1 核上字符互素确实给有界逆

反设 $M=\ker P(X)\ne0$。
R176 给
$$
M\subset\mathcal D_\infty(X),\qquad X_M=X|_M\in B(M),
$$
且所有 $\mathcal A$ 系数保持 $M$。
固定 $\zeta$，在 $B(M)$ 中取由
$X_M$、原多项式与 $Q_\zeta$ 的全部系数限制
生成的含单位交换 Banach 代数 $\mathfrak D$。

对任意 $E\in\mathcal A$，
$$
E_M-\chi(E)I_M
$$
拟幂零，因为原 $E-\chi(E)I$ 拟幂零且限制不放大幂范数。
因此每个 $\mathfrak D$ 字符 $\varphi$ 均满足
$$
\varphi(E_M)=\chi(E).
\tag{1.7}
$$
由 $P(X)_M=0$，
$$
p_0(\varphi(X_M))=0.
\tag{1.8}
$$
而 (1.5) 给
$$
\varphi(Q_\zeta(X_M))
=
q_{\zeta,0}(\varphi(X_M))\ne0.
$$
故 $Q_\zeta(X_M)$ 在 $\mathfrak D$ 中可逆，
特别在 $M$ 上有真实有界逆。

这一步没有假设 $X_M$ 拟幂零。
当 $p_0$ 有多个非零根时，仍由 (1.8) 和互素性处理全部根。
也可把有限标量 Bézout 恒等式
$up_0+vq_{\zeta,0}=1$
代入 $X_M$，把其系数字符误差写成有限个交换拟幂零项，
得到同一个单位结论。

### 1.2 限制稠密与正确的跨核配对

R151 §3.1 对非零真解析 $A^{r_\zeta}$ 给
$$
\overline{A^{r_\zeta}M}=M.
$$
结合 (1.4) 及刚得到的核内逆，
$$
\overline{(\gamma_\zeta P-P)M}=M.
\tag{1.9}
$$
令 $M_\zeta=U_\zeta M$。
自然域等式 (1.1) 给
$$
M_\zeta=\ker\gamma_\zeta(P(X)).
$$
对 $f\in M$、$g\in M_\zeta$，两者均有全部所需自然域，
所以
$$
\mathcal B((\gamma_\zeta P-P)f,g)
=
\mathcal B(f,\gamma_\zeta P\,g)-\mathcal B(Pf,g)=0.
$$
由 (1.9) 的左端稠密性，
$$
\mathcal B(M,U_\zeta M)=0
\qquad(\zeta\notin\mu_H).
\tag{1.10}
$$
没有假定 $CM=M$，也没有把原空间的 $C$ 自伴性下降到限制。

### 1.3 有限 Fourier 例外完成排核

对 $f,g\in M$，
$$
\mathcal B(f,U_\zeta g)
=
\zeta^{-1}\int f(y)g(-1-y)\zeta^{-y}\,d\mu(y).
$$
故 $f(y)g(-1-y)$ 的 Fourier 支撑包含于有限群 $\mu_H$。
有限柱条件期望在 $L^1$ 收敛，使该乘积在每个模 $H$ 柱上为常数。

若 $M\ne0$，取可数稠密族定义其总本质支撑。
$AM\subset M$ 与 $\omega>0$ 几乎处处使该支撑在 odometer 下平移不变，
遍历性遂迫其全测。
反射后的总支撑也全测。
因而在每个柱上可选 $f_0,g_0\in M$，
使 $f_0(y)g_0(-1-y)$ 在正测集上非零；
它是柱常数，所以在整柱几乎处处非零。
任意 $f\in M$ 的 $f(y)g_0(-1-y)$ 同样是柱常数，
故 $f$ 在该柱上为 $f_0$ 的标量倍数。
于是 $\dim M\le H$。

原 $A$ 单射且拟幂零，不允许非零有限维不变空间。
矛盾，所以 $M=0$。
完整 $C$ 自伴性给稠密像，R176 的循环图核心给最后的循环结论。
定理 1 得证。

## 2. 明确的全阶共振族与任意可和辅助

取
$$
u=a_*+\sum_j a_j\chi_j,\qquad
w=b_*+\sum_j b_j\chi_j,\qquad a,b\in\ell^2(\mathbb C),\quad a\ne0.
\tag{2.1}
$$
定义
$$
v_n=\sum_j a_j^n(\chi_j-1)\quad(n\ge2),
$$
$$
F_k
=
k![t^k]\exp\left(
tu+\sum_{n=2}^k\frac{2^{n-1}}n t^n v_n
\right),\qquad F_0=1,\quad F_1=u.
\tag{2.2}
$$
例如
$$
F_2=u^2+2v_2,\qquad
F_3=u^3+6uv_2+8v_3.
$$
这是 R270C 已证明的实际共振族。

令
$$
q(z)=\sum_{k=0}^p q_kz^k,\qquad p\ge2,\quad q_p\ne0,
$$
并记
$$
F_q=\sum_{k=0}^p q_kF_k.
$$
另取任意 $c\in\ell^1(\mathbb C)$，置
$$
v_c=\sum_j c_j(\chi_j-1).
\tag{2.3}
$$
偏离可慢、可任意排列、可与主支撑任意重叠，
不要求属于快辅助类。

我们研究
$$
\boxed{(F_q+v_c-\lambda)e^w,\qquad\lambda\in\mathbb C.}
\tag{2.4}
$$

令
$$
j_a=\min\{j:a_j\ne0\},\quad
m_a=2^{j_a},\quad
\alpha=a_{j_a}\ne0.
\tag{2.5}
$$

**定理 2。**

1. 若存在 $j<j_a$ 使 $c_j\ne0$，则 (2.4) 对每个
   $\lambda\in\mathbb C$ 均非零且循环。

2. 若全部 $j<j_a$ 都有 $c_j=0$，记
   $$
   \delta=c_{j_a}.
   $$
   则
   $$
   \boxed{
   \gcd(q(z)-\lambda,\ \alpha q'(z)+\delta)=1
   }
   \tag{2.6}
   $$
   足以使 (2.4) 非零且循环。

特别，第二种情形仍可能有核的标量位移只在
$$
\boxed{
\mathcal E_{q,\alpha,\delta}
=
\{q(z):\alpha q'(z)+\delta=0\}.
}
\tag{2.7}
$$
因为 $p\ge2$，第二个多项式恰为 $p-1$ 次且非零，
所以
$$
|\mathcal E_{q,\alpha,\delta}|\le p-1.
\tag{2.8}
$$
候选集合不是非循环集合的断言；
某些候选可能由其他定理已排除。
本文不推断其他位移属于预解集：单射稠密像不等于满射或有界逆。

## 3. 实际自然算子与全阶系数

置
$$
t_j=e^{-2b_j},\qquad
R_j=V(t_jN_j),\qquad X=X_b.
$$
R270C §10 的真实有限 jet 公式给
$$
G_n=(-1)^{n-1}(n-1)!
\sum_j a_j^n(R_j-I)^n\in\mathcal G,\qquad n\ge2,
\tag{3.1}
$$
以及
$$
P_q(z)
=
\exp\left(\sum_{n=2}^p\frac{G_n}{n!}\partial_z^n\right)q(z).
\tag{3.2}
$$
由于 $q$ 次数有限，右侧只是有限和。
其系数属于 $\mathcal G$，且
$$
\chi(P_q(z))=q(z),\qquad P_q(X)e^w=F_qe^w.
\tag{3.3}
$$
这些恒等式来自已付清的原自然幂 jet 收敛，
没有把 $e^{tX}$ 当作全空间有界指数。

令
$$
Y=\sum_j c_j(R_j-I)\in\mathcal A,\qquad \chi(Y)=0,
$$
$$
T_\lambda=P_q(X)+Y-\lambda I,\qquad
\operatorname{Dom}T_\lambda=\operatorname{Dom}X^p.
\tag{3.4}
$$
最高系数为固定非零标量 $q_p$，所以 R176 适用。
准确有
$$
T_\lambda e^w=(F_q+v_c-\lambda)e^w,
\tag{3.5}
$$
且 $e^w$ 循环并给该算子的图核心。
归一成首一后，其字符多项式为
$(q-\lambda)/q_p$。

## 4. 只除有限 dyadic 差，不除整条快系数

固定 $\zeta\in\mu_{2^h}$。
高位 $j\ge h$ 的 $R_j$ 完全不变，因此
$$
D_\zeta=\gamma_\zeta X-X
=
\sum_{j<h}a_j
[V(t_j\zeta^{2^j}N_j)-V(t_jN_j)]
\tag{4.1}
$$
为真解析有限头，且实际存在真解析芽 $d_\zeta$ 使
$$
D_\zeta=A^{m_a}d_\zeta(A).
\tag{4.2}
$$
其常数为
$$
d_\zeta(0)
=
-\frac{2\alpha t_{j_a}}{d_{j_a}}
(\zeta^{m_a}-1).
\tag{4.3}
$$

同样，(3.1) 的每个 dyadic 差只有有限项。
由于 $(R_j-I)^n$ 在标量变量 $A=z$ 的零点至少消失 $n2^j$ 阶，
准确有
$$
\boxed{
\gamma_\zeta G_n-G_n
=
A^{n m_a}H_{n,\zeta}(A),
}
\tag{4.4}
$$
其中 $H_{n,\zeta}$ 是真正收敛的解析芽。

(4.4) 不是 $G_n/A^{n m_a}$ 有界的断言。
原 $G_n$ 可能没有这种有界首阶商。
这里只消去已经变成有限真解析头的差。

写
$$
P_q(z)=q(z)+R_q(z),
$$
$R_q$ 的每个系数是有限个 $G_2,\ldots,G_p$ 的无常数多项式，
故其字符为零。
对这些有限乘积使用逐因子差分恒等式；
每项都含至少一个 $\gamma_\zeta G_n-G_n$，
其余因子是 $G_k$ 或 $\gamma_\zeta G_k$。
由 (4.4) 且 $n\ge2$，得到实际有界系数分解
$$
\boxed{
\gamma_\zeta R_q(z)-R_q(z)
=
A^{2m_a}L_\zeta(z),\qquad
L_\zeta\in\mathcal A[z].
}
\tag{4.5}
$$
$L_\zeta$ 一般不是纯标量解析演算；
本稿只需要其每个系数是实际有界 $\mathcal A$ 元素。

现在在标量多项式变量 $z$ 中有限展开
$$
\gamma_\zeta P_q(z+D_\zeta)-P_q(z).
$$
(4.2)、(4.5) 给实际分解
$$
\boxed{
\gamma_\zeta P_q(z+D_\zeta)-P_q(z)
=
A^{m_a}K_\zeta(z),\qquad
K_\zeta\in\mathcal A[z].
}
\tag{4.6}
$$
并且
$$
\boxed{\chi(K_\zeta(z))=d_\zeta(0)q'(z).}
\tag{4.7}
$$

核对 (4.7)：$q(z+D)-q(z)$ 的一次项为 $Dq'(z)$；
更高 $D$ 幂除去 $A^{m_a}$ 后仍含正次 $A$。
$\gamma R_q-R_q$ 由 (4.5) 除去 $A^{m_a}$ 后仍含 $A^{m_a}$。
$D\,\gamma R_q'(z)$ 除去 $A^{m_a}$ 后，
其剩余 $R_q'$ 系数字符仍为零；
更高 $D$ 项同样不贡献字符。
因此只有 $d_\zeta(0)q'(z)$ 留下。
这完整支付了每个低阶系数，而不只检查最高两项。

## 5. 任意可和偏离的首位与字符多项式

### 5.1 没有比主首位更早的偏离

假设 $c_j=0$ 对 $j<j_a$。
范数绝对收敛及有限 gauge 固定位给
$$
\Delta_\zeta Y
=
\sum_{j<h}c_j
[V(t_j\zeta^{2^j}N_j)-V(t_jN_j)].
$$
因此存在真正解析芽 $y_\zeta$，使
$$
\Delta_\zeta Y=A^{m_a}y_\zeta(A),\qquad
y_\zeta(0)
=
-\frac{2\delta t_{j_a}}{d_{j_a}}
(\zeta^{m_a}-1).
\tag{5.1}
$$
允许 $\delta=0$；这时该常数就是零。

由自然域恒等式、(4.6) 和 (5.1)，
$$
\gamma_\zeta T_\lambda-T_\lambda
=
A^{m_a}Q_\zeta(X),
\tag{5.2}
$$
其中 $Q_\zeta\in\mathcal A[z]$，且
$$
\boxed{
\chi(Q_\zeta(z))
=
-\frac{2t_{j_a}}{d_{j_a}}
(\zeta^{m_a}-1)\,[\alpha q'(z)+\delta].
}
\tag{5.3}
$$
对 $\zeta\notin\mu_{m_a}$，外面标量非零。
(2.6) 正是定理 1 所需的字符互素条件
（归一化的 $q_p$ 不改变互素性）。
因此定理 2 的第二项成立。

### 5.2 存在更早的偏离

令
$$
j_c=\min\{j:c_j\ne0\}<j_a,\qquad m_c=2^{j_c}.
$$
(4.6) 可继续写成含 $A^{m_c}$ 的实际分解；
除去它后还含 $A^{m_a-m_c}$，所以全部系数字符为零。
而
$$
\Delta_\zeta Y=A^{m_c}\widetilde y_\zeta(A),
$$
$$
\widetilde y_\zeta(0)
=
-\frac{2c_{j_c}t_{j_c}}{d_{j_c}}
(\zeta^{m_c}-1)\ne0
\qquad(\zeta\notin\mu_{m_c}).
\tag{5.4}
$$
故
$$
\gamma_\zeta T_\lambda-T_\lambda
=
A^{m_c}\widetilde Q_\zeta(X)
$$
的系数字符多项式为非零常数。
它与每个 $q-\lambda$ 互素，定理 1 给全部 $\lambda$ 的结论。
定理 2 得证。

## 6. 直接推论

### 6.1 全阶共振加首支撑有序的任意可和偏离

设 $c\ne0$，且
$$
j_c\le j_a.
$$
对每个整数 $p\ge2$，取 $q(z)=z^p$、$\lambda=0$。
若 $j_c<j_a$，由定理 2 第一项直接成立。
若 $j_c=j_a$，则 $\delta\ne0$，
$$
\gcd(z^p,\ p\alpha z^{p-1}+\delta)=1.
$$
因此
$$
\boxed{
\left[F_p+\sum_j c_j(\chi_j-1)\right]e^w
\text{ 非零且循环}\qquad(p\ge2).
}
\tag{6.1}
$$
主行任意复 $\ell^2$，偏离任意复 $\ell^1$，指数权任意复 $\ell^2$；
不存在尾率要求。
例如在全部非零主位取
$0<|c_j|\le C|a_j|^\kappa$、$\kappa>2$，
主零位令 $c_j=0$，即可满足此结论。

$p\ge2$ 不能在此删除。
当 $p=1$ 且首位匹配时，字符常数为 $\alpha+\delta$，
须另要求它非零才能直接用本判据。
例如 $a\in\ell^1$、$c=-a$、$a_*=-\sum_j a_j$，
则 $u+v_c=0$，确有零输出。

### 6.2 任意可和二次偏离最多一个字符候选

取 $q(z)=z^2$，假设主首位之前没有偏离。
则 (2.7) 简化为
$$
\boxed{
\lambda_*=\left(\frac{\delta}{2\alpha}\right)^2.
}
\tag{6.2}
$$
所以对每个 $\lambda\ne\lambda_*$，
$$
\boxed{
\left[
u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)-\lambda
\right]e^w
\text{ 非零且循环}.
}
\tag{6.3}
$$
如果首位偏离非零，$\lambda_*\ne0$，
于是原无标量位移的二次目标直接闭合。
如果首位偏离为零，$\lambda_*=0$，
正是当前一般首位遗漏的困难值。
若偏离早于主首位，则由定理 2 第一项没有任何候选值。

该候选不能在没有其他条件时直接删除。
例如主行只有一个非零系数 $\alpha$，
辅助也仅在同位取 $\delta$，
并令
$$
a_*=-\alpha-\frac{\delta}{2\alpha}.
$$
直接展开得到 $F_2+v_c=\delta^2/(4\alpha^2)$ 为常数，
故在 $\lambda=\lambda_*$ 时输出恰为零。

### 6.3 首位遗漏与平方自由字符

在主首位之前及主首位本身均无偏离时，$\delta=0$。
此时 (2.6) 就是
$$
\gcd(q-\lambda,q')=1.
$$
因此只要 $q-\lambda$ 平方自由，
任意后续可和偏离都被处理；
特别 $q(z)=z^p$、$\lambda\ne0$ 全部适用。
未由此处理的标量位移只在 $q$ 的临界值中。

如果 $c=0$，R270C 已对每个实际非零共振多项式给更强结论，
所以本稿不把该无偏离情形的候选重新登记为未闭。

## 7. 仍未闭的低头情形

取全平面连续谱主行
$$
a_j=(-1)^j(j+1)^{-\sigma},\qquad \frac12<\sigma<1,
$$
并令
$$
c_0=0,\qquad c_j=\beta|a_j|^\kappa\omega_j\quad(j\ge1),
\qquad\kappa>2,\quad \beta\ne0,\quad|\omega_j|=1.
$$
这里 $j_a=0$、$j_c=1$、$\delta=0$。
本稿证明其全部二次非零标量位移 $\lambda\ne0$ 循环，
但没有排除 $\lambda=0$ 的核。

对于 $\lambda=0$，
(5.3) 的字符多项式是非零标量乘 $z$，
与原 $z^2$ 有公共零点。
核上剩余因子仅是拟幂零，不是单位。
R270C/D 的全空间循环性等价没有提供其在未知限制上的稠密像；
R184 的普遍正则分母也不能被替换为这个一般分子。
本稿保留这一准确缺口。

## 8. 来源

- [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  实际自然多项式、全部域、完整 $C$ 自伴、核内有界 first 与图循环。
- [R151](../results/R151-quartic-analytic-approximation-gauge-stability.md) §3.1：
  真解析 $A^r$ 在任意不变限制上的稠密像。
- [R270C](../results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md) §10：
  共振 $F_p$、实际 $G_n$ 与有限自然 jet 恒等式。
- [首支撑有序二次源稿](../notes/2026-11-13-earliest-support-dyadic-quadratic-cyclicity-central-review.md)：
  本稿一般因子判据的二次起点及完整逐柱 Fourier 排核。
- [R184](../results/R184-universal-subquotient-regularization-and-closed-polynomial-koszul-calculus.md)、
  [R270D](../results/R270-appendix-arbitrary-fast-leading-coefficients-maximal-closure-and-cyclicity.md)：
  未知限制上的分母／分子与全空间循环 iff 的准确边界。
