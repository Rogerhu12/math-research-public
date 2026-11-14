# R144：一模式平移消元——任意幂循环及至多 p−1 个点态多项式例外

日期：2026-11-12。作者：l2_moments；一般次数消元由根代理提出并共同逐域核验。
状态：完整证明，已完成逐域核验。它加强并包含 R142 的根差判据，取消简单根假设。平方的初始独立推导保留在同日 quadratic-first-mode-resultant-kernel-exclusion 笔记，本文 §8 也写出其显式消元式。

本证明只使用第一阶闭乘子的真实幂域和一个有界正则化乘子。一般高阶点态符号不需要预先具有 $C$ 自伴闭实现；也不把全空间稠密值域误用为任意不变限制的稠密值域。

## 1. 主定理

设
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,\quad a\ne0,
$$
并记
$$
j_0=\min\{j:a_j\ne0\},\qquad
h=2^{j_0},\qquad a=a_{j_0}\ne0,\qquad d=d_{j_0}=W_h.
\tag{1.1}
$$
以下单个 $a$ 表示首个非零系数。

**定理 1.1。** 对任意非零标量多项式 $q$，若
$$
\boxed{\gcd(q(w),q(w-2a))=1,}
\tag{1.2}
$$
则 $q(u)$ 对实际 $A$ 循环。允许 $q$ 有重根。

(1.2) 等价于没有两个不同根之差为 $2a$；重数本身不造成障碍。非零常数多项式直接成立。

**推论 1.2。** 对任意 $\rho\in\mathbb C$、整数 $p\ge1$，
$$
\boxed{(u-\rho)^p\text{ 对 }A\text{ 循环}.}
\tag{1.3}
$$
因为 $(w-\rho)^p$ 与 $(w-\rho-2a)^p$ 没有共同根。

**推论 1.3。** 给定次数 $p\ge1$ 的非恒定标量多项式 $q$，令
$$
\mathcal E_q^{\rm shift}(a)
=\{q(c):q(c)=q(c-2a)\}.
\tag{1.4}
$$
则
$$
\boxed{
|\mathcal E_q^{\rm shift}(a)|\le p-1,\qquad
\lambda\notin\mathcal E_q^{\rm shift}(a)
\Longrightarrow q(u)-\lambda\text{ 循环}.
}
\tag{1.5}
$$
不再需要添加临界值集合 $\{q(c):q'(c)=0\}$。

特别地，
$$
u^2-\lambda\text{ 循环}\quad(\lambda\ne a^2),
\tag{1.6}
$$
所以任意非常数第一 chaos 的平方都循环，没有相位或有限秩条件。
对交替模式 $u=\sum_{j\ge0}(-1)^j(j+1)^{-1}\chi_j$，结论为所有
$u^p$、$(u-\rho)^p$ 均循环，且 $u^2-\lambda$ 对 $\lambda\ne1$ 循环。
剩余候选 $u^2-1$ 不被本文自动排除。

## 2. 第一阶闭乘子和 Bell 多项式

令 $X=X_u$ 为 R125 的闭第一阶乘子。它满足
$$
X^*=CXC,
$$
有限柱为 $X$ 与 $X^*$ 的图核心，全部有界交换子保持其域并与之域交换。
R134 进一步证明
$$
1\in\operatorname{Dom}X^n\quad(n\ge0).
\tag{2.1}
$$

R134 的实际 Bell 系数由
$$
B(t)=\lim_{N\to\infty}
\prod_{j<N}e^{-ta_jV_j}
\bigl(\cosh(ta_j)I+V_j\sinh(ta_j)\bigr)
$$
在紧圆盘上的算子范数一致极限定义，
$B_k=B^{(k)}(0)$。它们满足
$$
B_0=I,\qquad B_1=0,\qquad
B_k\in\mathcal A_h:=\overline{\mathbb C[I,A^h]},
\qquad\chi(B_k)=0\quad(k\ge1),
\tag{2.2}
$$
以及真实向量等式
$$
u^n=\sum_{k=0}^n\binom nk B_kX^{n-k}1.
\tag{2.3}
$$
所有 $u^n$ 属于 $L^2$，由复 Rademacher 有限矩界保证。

将 $q$ 除以非零首项系数，可设其首一且次数为 $p\ge1$。定义有界系数多项式
$$
P(w)=\sum_{k=0}^p\frac{B_k}{k!}q^{(k)}(w)
\in\mathcal A_h[w].
\tag{2.4}
$$
于是 $P$ 首一、$\chi(P(w))=q(w)$，并且
$$
\boxed{P(X)1=q(u)}
\tag{2.5}
$$
在已知的自然域 $\operatorname{Dom}X^p$ 上合法。
本文不假设自然 $P(X)$ 是闭算子。

## 3. 固定有界正则化及其所有幂

把 $(a_j)$ 分成实部、虚部的四个非负 $\ell^2$ 部分。R128 给
$$
R_\nu(t)=(I+tX_{b_\nu})^{-1},\qquad
R(t)=\prod_{\nu=1}^4R_\nu(t)\in\{A\}',
$$
其中零部分取恒等。对每个 $t>0$，
$$
\|R(t)\|\le1,\qquad R(t)\text{ 单射},\qquad
R(t)H\subseteq\operatorname{Dom}X,\qquad
Z(t):=XR(t)\in\{A\}'.
\tag{3.1}
$$
另有 $R(t)\to I$ 强收敛。

固定一个 $t>0$，以下简记 $R=R(t)$、$Z=XR$。真实域交换给
$$
R^nH\subseteq\operatorname{Dom}X^n,\qquad
X^kR^n=Z^kR^{n-k}\quad(0\le k\le n).
\tag{3.2}
$$
这可逐阶归纳；$Z$ 与 $R$ 都有界且交换，所以右边是全空间有界算子。

因此
$$
\boxed{S:=P(X)R^p\in\{A\}'}
\tag{3.3}
$$
是一个真实有界乘子。若 $P(w)=\sum_{\ell=0}^pC_\ell w^\ell$，
则它就是有限有界和
$$
S=\sum_{\ell=0}^pC_\ell Z^\ell R^{p-\ell}.
$$
定义
$$
M=\ker S.
\tag{3.4}
$$
它是闭 $A$ 不变空间。

### 3.1 固定参数的深域在核中稠密

R140 证明两个参数只差有界交换单位：
$$
R(s)=R(t)U(s,t),\qquad U(s,t),U(s,t)^{-1}\in\{A\}'.
\tag{3.5}
$$
直接公式来自
$$
R_\nu(s)=R_\nu(t)
\left[\frac tsI+\left(1-\frac ts\right)R_\nu(s)\right];
$$
交换 $s,t$ 给括号的有界逆。

所有有界交换子保持 $M$，故对任意固定整数 $n$，
$$
R(s)^nM=R(t)^nM.
$$
又 $R(s)^n\to I$ 强收敛，所以
$$
\boxed{R^nM\text{ 在 }M\text{ 中稠密}.}
\tag{3.6}
$$
若 $n\ge p$，则对 $v\in M$，
$$
P(X)R^nv
=S R^{n-p}v
=R^{n-p}Sv=0.
\tag{3.7}
$$
同时 $R^nv\in\operatorname{Dom}X^n$。这给核内任意固定有限深度的实际自然幂域，不需要把全部核直接放进 $\operatorname{Dom}X^p$。

## 4. Gauge 后的系数差真实地含一个 $A^h$

固定 dyadic $\zeta$。R125 给包含定义域的等式
$$
\gamma_\zeta(X)=U_\zeta XU_\zeta^*=X+D,
$$
其中 $D=D_\zeta(A)$ 是有限真正解析和。它与 $X$ 域交换，所以归纳得
$$
U_\zeta\operatorname{Dom}X^n=\operatorname{Dom}X^n
\quad(n\ge1).
\tag{4.1}
$$

设 $\zeta^h\ne1$。最低局部项给
$$
D=A^h d_\zeta(A),\qquad
d_\zeta(0)=-\frac{2a}{d}(\zeta^h-1).
\tag{4.2}
$$
令
$$
Q_\zeta(w)=\sum_{k=0}^p
\frac{\gamma_\zeta(B_k)}{k!}\,q^{(k)}(w+D).
\tag{4.3}
$$
这是 $P(X)$ 在自然幂域上的真实 gauge 多项式；若
$y=U_\zeta x$、$x\in\operatorname{Dom}X^p$，则
$$
Q_\zeta(X)y=U_\zeta P(X)x.
\tag{4.4}
$$

对每个 $B_k\in\mathcal A_h$，R139 的实际余数分解给
$$
\gamma_\zeta(B_k)-B_k=A^hC_{k,\zeta},
\qquad C_{k,\zeta}\in\mathcal A_h.
$$
这个分解在 $h=1$ 时同样成立；零余数在差中消失，正余数的有限和可提取 $A$。另外，
$q^{(k)}(w+D)-q^{(k)}(w)$ 每个系数都有真正的 $D$ 因子。故
$$
\boxed{Q_\zeta(w)-P(w)=A^hL_\zeta(w),
\qquad L_\zeta\in\mathcal A_h[w],\quad
\deg L_\zeta\le p-1.}
\tag{4.5}
$$
这里使用实际有界商；没有从“常数特征为零”直接推断可除 $A^h$。

## 5. 首字符等于标量的有限平移差

R142 已核算
$$
c_h(B_k)=\frac{(-2a)^k}{d}\quad(k\ge2).
\tag{5.1}
$$
它来自最低局部生成函数的 $z^h$ 系数
$(e^{-2at}-1+2at)/d$。常数项及一次项均为零。

计算 (4.5) 的 $h$ 阶系数即可取得 $L_\zeta$ 的字符。来自 $D$ 的一阶平移贡献为
$$
-\frac{2a(\zeta^h-1)}d\,q'(w).
$$
来自 $B_k$ 的 gauge 差贡献为
$$
\frac{\zeta^h-1}{d}
\sum_{k=2}^p\frac{(-2a)^k}{k!}q^{(k)}(w).
$$
两个正阶系数相乘的项从 $2h$ 开始，故不参与。合并有限 Taylor 公式得
$$
\boxed{
\chi(L_\zeta(w))
=\frac{\zeta^h-1}{d}\,[q(w-2a)-q(w)].
}
\tag{5.2}
$$

于是，在主定理假设 (1.2) 下，
$$
\gcd(\chi(P),\chi(L_\zeta))=1.
\tag{5.3}
$$
重根不会影响这个互素判断。$L_\zeta$ 的最高项字符为
$-2ap(\zeta^h-1)/d\ne0$，所以当 $p\ge2$ 它的次数恰为 $p-1$。

## 6. 有界系数的 Bézout 证书

为避免只引用形式 resultant，直接给有限矩阵证明。
因为 $P$ 首一，
$$
\mathcal A_h[w]/(P)
$$
是以 $1,w,\ldots,w^{p-1}$ 为基的自由 $\mathcal A_h$ 模。
乘以 $L_\zeta$ 的映射由一个 $p\times p$ 有界系数矩阵表示。
在字符 $\chi$ 上，该矩阵成为
$\mathbb C[w]/(q)$ 中乘以 $\chi(L_\zeta)$ 的映射。

由 (5.3) 和标量 Euclidean 算法，这个标量映射可逆。
因此原矩阵行列式的字符非零；$\mathcal A_h$ 的唯一字符说明该行列式为单位。
用伴随矩阵得到实际有界系数逆。把它作用于常数类 $1$，得到某个
$b_\zeta(w)$、$\deg b_\zeta\le p-1$，使
$$
b_\zeta L_\zeta\equiv1\pmod P.
$$
对首一 $P$ 作多项式长除法，便有
$$
\boxed{a_\zeta(w)P(w)+b_\zeta(w)L_\zeta(w)=1}
\tag{6.1}
$$
于 $\mathcal A_h[w]$。当 $p\ge2$，可取
$\deg a_\zeta\le p-2$；$p=1$ 时 $L_\zeta$ 已为有界单位，直接取
$a_\zeta=0$、$b_\zeta=L_\zeta^{-1}$。

结合 (4.5)，(6.1) 给精确的消元式
$$
\boxed{
A^h
=\bigl(A^h a_\zeta(w)-b_\zeta(w)\bigr)P(w)
+b_\zeta(w)Q_\zeta(w).
}
\tag{6.2}
$$
所有系数都在 $\mathcal A_h$ 中。它们可以依赖 $\zeta$ 且范数很大；
证明不需要关于 $\zeta$ 的一致界。

## 7. 在深核上跨配对，随后排除有界核

取固定深度 $n=2p$。由 §3，
$$
x\in R^{2p}M,\qquad
y\in U_\zeta R^{2p}M
$$
都属于 $\operatorname{Dom}X^{2p}$，并且
$$
P(X)x=0,\qquad Q_\zeta(X)y=0.
\tag{7.1}
$$
第二个式子由 (3.7)、(4.4) 得到。这里没有把 $\gamma_\zeta(S)$ 的正则化因子错误地继续写作 $R$；直接选 $y=U_\zeta R^{2p}v$ 正好给所需的 $Q_\zeta$ 核向量。

将 (6.2) 作用于 $x$。因
$\deg b_\zeta+p\le2p-1$，所有乘积在所取自然域上有定义。
有界系数均对 $B$ 对称并与 $X$ 域交换，所以对应多项式在自然幂域上对
$B$ 对称。于是
$$
\begin{aligned}
B(A^hx,y)
&=B\bigl(Q_\zeta(X)b_\zeta(X)x,y\bigr)\\
&=B\bigl(b_\zeta(X)x,Q_\zeta(X)y\bigr)=0.
\end{aligned}
\tag{7.2}
$$
另一项因 $P(X)x=0$ 消失。

$A^h$ 有界，$R^{2p}M$ 在 $M$ 稠密，其酉像在 $U_\zeta M$ 稠密，
所以 (7.2) 延拓为
$$
B(A^hM,U_\zeta M)=0.
$$
R23 的 $\overline{A^hM}=M$ 进一步给
$$
\boxed{B(M,U_\zeta M)=0\quad(\zeta\notin\mu_h).}
\tag{7.3}
$$
R122/R125 的 Fourier 核机制遂适用：反射乘积只有有限群 $\mu_h$ 的 Fourier 支撑；
非零闭 $A$ 不变空间的总本质支撑为全测；逐个低头柱得到有限限制秩，
从而 $\dim M\le h$。单射拟幂零 $A$ 不容许这样的非零有限维不变空间。
因此 $M=0$。

由 (3.3)，$S$ 是有界交换子。$M=\ker S=0$ 与其 $C$ 对称性给
$\overline{\operatorname{Ran}S}=H$，所以 $S1$ 循环。又 (2.1)、域交换及
(2.5) 给
$$
S1=P(X)R^p1=R^pP(X)1=R^pq(u).
$$
$R^p\in\{A\}'$ 保持 $\operatorname{cyc}_A(q(u))$，其中已经含循环向量
$R^pq(u)$，故 $q(u)$ 本身循环。主定理证毕。

## 8. 平方的显式低阶核验

对 $q(w)=w^2-\lambda$，
$$
P(w)=w^2+B_2-\lambda I.
$$
记 $C=B_2-\lambda I$、$D=\delta X$、$E=\delta B_2$、
$K=D^2+E$。这时
$$
Q(w)=P(w)+2Dw+K.
$$
直接恒等式为
$$
K^2+4D^2C
=(K-2Dw)Q(w)+(4D^2-K+2Dw)P(w).
\tag{8.1}
$$
两个差 $D,E$ 都是真正解析芽；其首阶系数分别为
$-2a(\zeta^h-1)/d$、$4a^2(\zeta^h-1)/d$。故真解析商 $E/D$ 的常数为
$-2a$，并有
$$
K^2+4D^2C
=D^2\bigl[(D+E/D)^2+4B_2-4\lambda I\bigr].
\tag{8.2}
$$
方括号字符为 $4(a^2-\lambda)$。$\lambda\ne a^2$ 时，
(8.1) 本身已经给出 $A^{2h}$ 乘单位的跨核消元；一般证明的 Bézout 证书将其精简为 (6.2) 的 $A^h$。

另一方面，
$$
\gcd(w^2-\lambda,(w-2a)^2-\lambda)\ne1
\iff\lambda=a^2.
$$
所以平方仅剩这个平移碰撞候选，重复根 $\lambda=0$ 不再是障碍。

## 9. 任意固定多项式的 p−1 个候选值

对固定次数 $p$ 的非恒定 $q$，两个多项式
$q(w)-\lambda$ 与 $q(w-2a)-\lambda$ 有共同根，当且仅当存在 $c$ 满足
$$
q(c)=q(c-2a)=\lambda.
$$
因 $a\ne0$，
$$
q(w)-q(w-2a)
$$
的次数恰为 $p-1$，首项系数为 $2ap$ 乘原首项系数。因此它至多有
$p-1$ 个不同零点，相应 $\lambda$ 值也至多 $p-1$ 个。这证明 (1.5)。

特别地，单根位置即使带任意重数，也不会与其平移 $2a$ 相交；
由此得到全部 $(u-\rho)^p$。若 $u$ 为常数，仍应另行判断输出是否为零。
有限支撑向量则由 R11 另外处理每个非零有限柱输出。

本稿没有把有限候选集自动清空。对纯有限柱 $u=a\chi_{j_0}$，
$u^2-a^2=0$，故任意最终无例外表述必须保留“输出非零”的条件。
对于无限交替模式的非零 $u^2-1$，当前消元仍产生字符为零的 resultant，
需要新的实质论证。

## 10. 与此前结果的关系及边界

R144 保留 R134 的真实 Bell 范数系数和幂域，但不使用空谱。
它通过有界正则化核代替未知高阶闭乘子核，因而也不依赖一般高阶
Dirac/Carleman 条件。R142 的简单根版本及其 $2p-2$ 个候选值现在被本条
更强的结论覆盖；其有界根分裂证明仍是独立的有效结构记录。

唯一变量的重要性在于：标量 $q$ 与其平移互素，就在
$\mathbb C[w]/(q)$ 中给可逆乘法矩阵。对多个独立模式，两个互素多项式
通常仍可能有共同零点，不能直接把这个一变量 Bézout 单位结论搬过去。
一般多模式点态多项式、无限秩有限 chaos 及完整 Hilbert ISP 仍未因此解决。
