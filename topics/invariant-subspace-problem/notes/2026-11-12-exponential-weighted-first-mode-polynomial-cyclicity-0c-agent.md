# R147：任意第一阶指数权重下的一模式点态多项式循环性

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。

状态：完整证明。倾斜 Bell 系数、首字符及基向量传递由根代理提出，本文逐式核验并写全。它将 R144 的平移互素判据推广到任意复第一阶指数权重，并完成 R145 全部真空整轨道及其非零第一阶混合导数的循环性。

不把点乘 $e^v$ 当作全 $H$ 上的有界算子，也不从循环向量取极限推出循环性。

## 1. 主定理

取任意两个复第一 chaos 向量

$$
u=c_u+\sum_{j\ge0}a_j\chi_j,\qquad
v=c_v+\sum_{j\ge0}b_j\chi_j,
\qquad a,b\in\ell^2.
$$

先设 $u$ 非常数，记

$$
j_0=\min\{j:a_j\ne0\},\qquad
h=2^{j_0},\qquad a=a_{j_0}\ne0,
\qquad b=b_{j_0},\qquad d=d_{j_0}=W_h.
\tag{1.1}
$$

单个 $a,b$ 只表示这个首位上的两个系数。

**定理 1.1。** 若非零标量多项式 $q$ 满足

$$
\boxed{\gcd(q(w),q(w-2a))=1,}
\tag{1.2}
$$

则点态向量 $q(u)e^v$ 属于 $H$、非零，并对实际 $A$ 循环。允许 $q$ 有重根，也允许 $u,v$ 的位支持任意重叠。

由此得到：

1. 对任意 $\rho\in\mathbb C$、整数 $p\ge1$，$(u-\rho)^pe^v$ 循环。
2. 对任意非零第一阶向量 $u$，$ue^v$ 循环；若 $u$ 是非零常数，直接归于 $e^v$。
3. 对固定次数 $p\ge1$ 的非恒定 $q$，令
   $$
   \mathcal E_q(a)=\{q(c):q(c)=q(c-2a)\}.
   $$
   则 $|\mathcal E_q(a)|\le p-1$，且
   $$
   \lambda\notin\mathcal E_q(a)
   \Longrightarrow (q(u)-\lambda)e^v\text{ 循环}.
   \tag{1.3}
   $$
   此充分判据留下的候选集与指数方向 $v$ 无关。

若 $u$ 为常数，$q(u)e^v$ 恰在 $q(u)\ne0$ 时循环。非零常数多项式 $q$ 总可直接处理。以下主证明取 $q$ 首一、次数 $p\ge1$；一般首项系数只需乘回非零标量。

## 2. 任意复第一阶指数都是 R16 循环乘积

先完整核验作为基向量的 $e^v$。对每个位定义

$$
g_j(\varepsilon)=
\frac{e^{b_j(-1)^\varepsilon}}
{\sqrt{\cosh(2\operatorname{Re}b_j)}},
\qquad \varepsilon\in\{0,1\}.
$$

局部平方均值为1，而

$$
\mu_j:=\frac{g_j(0)+g_j(1)}2
=\frac{\cosh b_j}{\sqrt{\cosh(2\operatorname{Re}b_j)}}
=1+O(|b_j|^2)
$$

对充分高的位成立。因此 $\sum_j|1-\mu_j|<\infty$，R16 的归一化乘积判据使
$G_N=\prod_{j<N}g_j$ 在 $H$ 中收敛到范数为1的非零循环向量 $G$。
有限多个局部均值为零不影响该判据的尾部收敛。

标量乘积

$$
K_N=\prod_{j<N}\sqrt{\cosh(2\operatorname{Re}b_j)}
$$

趋于有限正数 $K$，因为对实数 $x$ 有 $0\le\log\cosh x\le x^2/2$。
于是 $e^{v_N}=e^{c_v}K_NG_N$ 在 $H$ 中收敛。
另一方面 $v_N\to v$ 于 $H$，可取几乎处处收敛子列，再取上述 $H$ 收敛的几乎处处子列，识别极限为点态 $e^v$。所以

$$
\boxed{e^v=e^{c_v}KG\in H\text{ 且循环}.}
\tag{2.1}
$$

这个证明没有要求 $e^v$ 或 $e^{-v}$ 本质有界。

## 3. 二模式整 Bell 函数、单位与真实循环基

令 $X=X_u$ 为 R125 的实际闭第一阶乘子。R145 对模式 $(u,v)$ 构造

$$
\mathcal B(s,t)
=\lim_{N\to\infty}\prod_{j<N}H(sa_j+tb_j,V_j),
\quad
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z).
\tag{3.1}
$$

极限在参数紧集上一致按算子范数收敛，是 $\mathcal A$ 值整函数。
其依据是 $\|H(z,V_j)-I\|\le C_T|z|^2$ 于有界参数集，以及
$\sum_j|sa_j+tb_j|^2$ 的紧集一致尾控制。

每个局部因子的字符为

$$
\chi(H(z,V_j))=e^{-z}(\cosh z+\sinh z)=1.
$$

因此有限乘积及极限均为 $\mathcal A$ 的单位；逆在参数紧集上同样按范数收敛，且是整函数。这里使用 $\mathcal A$ 的唯一字符结构：字符为1的元素可逆。等价地，它与 $I$ 的差在根基中，逆由拟幂零幂级数得到。

R145 的共同整向量为

$$
\mathcal V(s,t)=\mathcal B(s,t)^{-1}e^{su+tv},
$$

并已通过各个通常伴随的有限柱图核心证明

$$
\mathcal V(s,t)\in\bigcap_{n\ge0}\operatorname{Dom}X^n,
\qquad X^n\mathcal V(s,t)=\partial_s^n\mathcal V(s,t).
\tag{3.2}
$$

记

$$
B_*:=\mathcal B(0,1),\qquad
\xi:=\mathcal V(0,1)=B_*^{-1}e^v.
\tag{3.3}
$$

由 (2.1) 及 $B_*^{-1}$ 是有界交换单位，$\xi$ 循环。由 (3.2)，它属于 $X$ 的全部自然幂域。

## 4. 倾斜系数确实留在首位尾代数

定义

$$
\widetilde B(s)=\mathcal B(s,1)B_*^{-1},
\qquad \widetilde B_k=\left.\frac{d^k}{ds^k}\widetilde B(s)\right|_{s=0}.
\tag{4.1}
$$

这是范数整单位函数，$\widetilde B_0=I$，$\chi(\widetilde B_k)=0$（$k\ge1$）。一般 $\widetilde B_1\ne0$。

更关键的是，

$$
\boxed{\widetilde B(s),\widetilde B_k\in\mathcal A_h
:=\overline{\mathbb C[I,A^h]}.}
\tag{4.2}
$$

这不是仅从形式首阶猜测。有限截断的准确比值是

$$
\mathcal B_N(s,1)\mathcal B_N(0,1)^{-1}
=\prod_{j<N}
H(b_j+sa_j,V_j)H(b_j,V_j)^{-1}.
\tag{4.3}
$$

若 $a_j=0$，该局部比值恰为 $I$。所有非平凡项都有 $j\ge j_0$，故其
$V_j$ 属于 $\mathcal A_h$；局部因子及逆也在该代数中。
每个逆还是真正的一元解析芽作用于 $A$：在形式原点 $V_j=1$，局部 $H$ 的值为1，所以标量解析倒数存在。

有限比值在紧 $s$ 集上按范数趋于 (4.1)，因为分子与固定分母逆均如此收敛。闭代数及 Cauchy 导数于是给 (4.2)。低于 $j_0$ 的指数系数 $b_j$ 已精确取消，未带入错误的低阶项。

### 4.1 首形式系数

在最低非零位，写 $x=z^h$，则

$$
V_{j_0}=1-2x/d+O(x^2),\qquad
H(t,V_{j_0})
=1+\frac{e^{-2t}-1+2t}{d}x+O(x^2).
$$

其他非平凡局部比值从 $2h$ 或更高开始。因此

$$
\boxed{
c_h(\widetilde B(s))
=\frac{e^{-2b}(e^{-2as}-1)+2as}{d}.
}
\tag{4.4}
$$

$c_h$ 是 R32 的连续真实形式系数；所以有限乘积的这个恒等式通过范数极限保持，局部一致收敛也允许微分。得到

$$
c_h(\widetilde B_1)=\frac{2a(1-e^{-2b})}{d},
\qquad
c_h(\widetilde B_k)=\frac{e^{-2b}(-2a)^k}{d}\quad(k\ge2).
\tag{4.5}
$$

一阶系数还有绝对范数和表示

$$
\widetilde B_1
=\sum_j a_j H'(b_j,V_j)H(b_j,V_j)^{-1}.
\tag{4.6}
$$

对于充分高的位，$H'(b_j,V_j)=O(|b_j|)$，逆范数一致有界，所以项范数由 $C|a_jb_j|$ 控制；有限初段另行保留。Cauchy–Schwarz 保证可和。这特别核实了任意重叠复系数时的有界对数导数。

## 5. 指数加权的真实向量恒等式

由 $e^{su+v}=B_*\widetilde B(s)\mathcal V(s,1)$，逐次微分并使用 (3.2)，得

$$
u^n e^v
=B_*\sum_{k=0}^n\binom nk\widetilde B_k X^{n-k}\xi.
\tag{5.1}
$$

所有导数都是真正的 $H$ 导数；因此也证明这些加权点态幂属于 $H$。
也可直接核验可积性：$\|u^ne^v\|_2\le\|u\|_{4n}^n\|e^v\|_4<\infty$，其中第一项由 Rademacher 矩界控制，第二项由 §2 对 $2v$ 使用得到。R145 的局部一致指数级数使这些点态导数与上述 $H$ 导数一致。
定义首一有界系数多项式

$$
P(w)=\sum_{k=0}^p\frac{\widetilde B_k}{k!}q^{(k)}(w)
\in\mathcal A_h[w].
\tag{5.2}
$$

则 $\chi(P(w))=q(w)$，且

$$
\boxed{q(u)e^v=B_*P(X)\xi.}
\tag{5.3}
$$

这里 $\xi\in\operatorname{Dom}X^p$，所以代入完全合法；不假设自然 $P(X)$ 闭。
由 (4.5) 与有限 Taylor 恒等式，

$$
\boxed{
c_h(P(w))
=\frac{e^{-2b}[q(w-2a)-q(w)]+2a q'(w)}d.
}
\tag{5.4}
$$

## 6. 一个固定有界正则化及核内深域

复用 R128 的四个非负分量，取任意固定参数 $t>0$，得到单射收缩

$$
R=R(t)\in\{A\}',\qquad
RH\subseteq\operatorname{Dom}X,\qquad Z=XR\in\{A\}'\subseteq B(H).
$$

全部有界交换子的域交换给

$$
R^nH\subseteq\operatorname{Dom}X^n,
\qquad X^kR^n=Z^kR^{n-k}\quad(0\le k\le n).
\tag{6.1}
$$

故

$$
S:=P(X)R^p\in\{A\}'
\tag{6.2}
$$

是全空间有界算子。若 $P(w)=\sum C_kw^k$，它就是有限有界和
$\sum C_k Z^kR^{p-k}$。令 $M=\ker S$，这是闭 $A$-不变空间。

需要核内深域稠密，而非仅在 $H$ 中稠密。对每个正分量预解式，

$$
R_\nu(s)=R_\nu(t)
\left[\frac tsI+\left(1-\frac ts\right)R_\nu(s)\right].
$$

交换 $s,t$ 给括号的有界逆；相乘可由预解式恒等式直接核验，或由 $R_\nu(t)$ 单射取消。因此四分量乘积满足

$$
R(s)=R(t)U(s,t),\qquad U(s,t),U(s,t)^{-1}\in\{A\}'.
$$

R88 使单位及逆保持 $M$，所以对固定整数 $n$，
$R(s)^nM=R(t)^nM$。又 $R(s)^n\to I$ 强收敛于 $s\downarrow0$，故

$$
\boxed{R^nM\text{ 在 }M\text{ 中稠密}.}
\tag{6.3}
$$

若 $n\ge p$，域交换及 $Sv=0$ 给

$$
P(X)R^nv=R^{n-p}Sv=0,
\qquad R^nv\in\operatorname{Dom}X^n
\quad(v\in M).
\tag{6.4}
$$

## 7. 实际 gauge 消元及有限自由模 Bézout

固定 $\zeta^h\ne1$ 的 dyadic gauge。R125 给包含定义域的恒等式

$$
U_\zeta XU_\zeta^*=X+D,\qquad
D=A^h d_\zeta(A),\quad
d_\zeta(0)=-2a(\zeta^h-1)/d.
\tag{7.1}
$$

$D$ 是有界真正解析乘子，并与 $X$ 域交换，所以有限归纳给
$U_\zeta\operatorname{Dom}X^n=\operatorname{Dom}X^n$。
置

$$
Q_\zeta(w)=\sum_{k=0}^p
\frac{\gamma_\zeta(\widetilde B_k)}{k!}
q^{(k)}(w+D).
\tag{7.2}
$$

若 $x\in\operatorname{Dom}X^p$，则

$$
Q_\zeta(X)U_\zeta x=U_\zeta P(X)x.
\tag{7.3}
$$

这里的 coefficient difference 具有真实有界除法。R124/R139 对
$T\in\mathcal A_h$ 的有限 gauge 余数分解给

$$
\gamma_\zeta(T)-T=A^h C_\zeta,
\qquad C_\zeta\in\mathcal A_h.
\tag{7.4}
$$

具体地，若 gauge 阶为 $N>h$，写 $T$ 的实际有界余数分解为
$\sum_{r=0}^{N/h-1}A^{rh}T_{rh}$、$T_{rh}\in\mathcal A_N$。零余数在差中消失；其余有限项均可提出 $A^h$。这就是 (7.4)，不能仅由形式常数项为零替代。

应用于 (4.2) 的全部系数，再用 (7.1) 对 $w+D$ 展开，得到

$$
\boxed{Q_\zeta(w)-P(w)=A^h L_\zeta(w),
\qquad L_\zeta\in\mathcal A_h[w],\quad\deg L_\zeta\le p-1.}
\tag{7.5}
$$

取 $h$ 次形式系数。系数 gauge 差贡献为 $(\zeta^h-1)c_h(P(w))$，$w$ 的平移只需保留 (7.1) 的首项及 $\chi(P)=q$，贡献为
$-2a(\zeta^h-1)q'(w)/d$。两个正阶项相乘从 $2h$ 起。由 (5.4)，准确抵消后

$$
\boxed{
\chi(L_\zeta(w))
=\frac{e^{-2b}(\zeta^h-1)}d
\,[q(w-2a)-q(w)].
}
\tag{7.6}
$$

因 $e^{-2b}\ne0$，主假设 (1.2) 等价于
$\gcd(\chi(P),\chi(L_\zeta))=1$。

由于 $P$ 首一，$\mathcal A_h[w]/(P)$ 是以 $1,w,\ldots,w^{p-1}$ 为基的有限自由模。乘以 $L_\zeta$ 的矩阵，在角色 $\chi$ 下成为
$\mathbb C[w]/(q)$ 中可逆的乘法矩阵。原矩阵行列式的字符非零，因而是 $\mathcal A_h$ 的单位。伴随矩阵给真正的有界系数逆。
将它作用于常数类 $1$，再对首一 $P$ 作长除法，得到

$$
\alpha_\zeta(w)P(w)+\beta_\zeta(w)L_\zeta(w)=1,
\tag{7.7}
$$

其中 $\deg\beta_\zeta\le p-1$；$p\ge2$ 时可取
$\deg\alpha_\zeta\le p-2$。$p=1$ 时直接取 $\alpha_\zeta=0$、
$\beta_\zeta=L_\zeta^{-1}$。

合并 (7.5)—(7.7)，有实际有界系数消元式

$$
\boxed{
A^h=(A^h\alpha_\zeta(w)-\beta_\zeta(w))P(w)
+\beta_\zeta(w)Q_\zeta(w).
}
\tag{7.8}
$$

只用了 $P$ 与对应的单个 $Q_\zeta$，没有加入其他 gauge 多项式并假设共同核。

## 8. 深核跨配对、有限 Fourier 支撑与有界核消失

取

$$
x\in R^{2p}M,\qquad y\in U_\zeta R^{2p}M.
$$

由 (6.4)、(7.1)—(7.3)，两者都属于 $\operatorname{Dom}X^{2p}$，且

$$
P(X)x=0,\qquad Q_\zeta(X)y=0.
\tag{8.1}
$$

这里直接选择酉像深域向量，没有把共轭后的正则化误写成未共轭的 $R$。

把 (7.8) 作用于 $x$。所有次数至多 $2p-1$，故真实自然域足够。
有界系数都 $B$ 对称并与 $X$ 域交换；$X^*=CXC$ 使每个自然多项式在对应幂域上 $B$ 对称。因此

$$
\begin{aligned}
B(A^hx,y)
&=B\bigl(Q_\zeta(X)\beta_\zeta(X)x,y\bigr)\\
&=B\bigl(\beta_\zeta(X)x,Q_\zeta(X)y\bigr)=0.
\end{aligned}
\tag{8.2}
$$

特别地 $\beta_\zeta(X)x\in\operatorname{Dom}X^p$；这一点由
$x\in\operatorname{Dom}X^{2p}$ 及 $\deg\beta_\zeta\le p-1$ 保证。

由 (6.3)，(8.2) 连续延拓为 $B(A^hM,U_\zeta M)=0$。R23 的
$\overline{A^hM}=M$ 再给

$$
B(M,U_\zeta M)=0\qquad(\zeta\notin\mu_h).
\tag{8.3}
$$

为明确最后的全 $H$ 排核，任意 $r,s\in M$ 的反射乘积
$r(y)s(-1-y)$ 属于 $L^1$。式 (8.3) 使其全部 $\mu_h$ 以外的 dyadic Fourier 系数为零，故它是模 $h$ 的柱函数。
若 $M\ne0$，其总本质支撑为全测：可数稠密族的支撑并在 $A$ 的正权移位下模零集不变，odometer 遍历性排除中间测度。

在每个模 $h$ 柱上，选择 $r_i,s_i\in M$，使反射乘积在正测子集不为零；可数总支撑保证这样的选择。该乘积已是柱常数，故整个柱上为非零常数。对任意 $r\in M$，$r(y)s_i(-1-y)$ 也为柱常数，所以 $r$ 在该柱上的限制是 $r_i$ 的标量倍数。于是 $\dim M\le h$。
但单射拟幂零 $A$ 不允许非零有限维不变空间，故 $M=0$。

因此 (6.2) 的 $S$ 单射。它是有界交换子，R88 的 $C$ 对称性使其值域稠密。由 $\xi$ 循环，$S\xi$ 也循环。
最后，$\xi\in\operatorname{Dom}X^p$ 及真实域交换给

$$
\boxed{
S\xi=P(X)R^p\xi
=R^pP(X)\xi
=R^pB_*^{-1}[q(u)e^v].
}
\tag{8.4}
$$

右侧的 $R^pB_*^{-1}$ 是有界交换子，保持 $\operatorname{cyc}_A(q(u)e^v)$。该空间已含循环向量 $S\xi$，故等于 $H$。定理 1.1 得证。

这一步没有要求 $P(X)$ 自然实现闭，也没有假设 $M\subseteq\operatorname{Dom}X^p$；使用的是明确构造的稠密深域。

## 9. 推论、线性情形核验与全部混合整轨道导数

对 $q(w)=(w-\rho)^p$，其唯一根与平移后的唯一根相差 $2a\ne0$，所以 (1.2) 成立。得到全部 $(u-\rho)^pe^v$。
对固定 $q-\lambda$，互素失效恰要求某个 $c$ 满足
$q(c)=q(c-2a)=\lambda$。非零差多项式 $q(w)-q(w-2a)$ 的次数为 $p-1$，故候选值至多 $p-1$ 个，证明 (1.3)。

一阶情形也可直接核对。此时
$P(X)=X+\widetilde B_1$（取 $q(w)=w$），而

$$
-2a/d+c_h(\widetilde B_1)=-2ae^{-2b}/d\ne0.
$$

这正是 R142 的尾代数有界扰动核判据，和上述一般消元一致。

### 9.1 R145 的每个整基向量都循环

对任意有限第一阶模式 $u_1,\ldots,u_d$，R145 定义

$$
\mathcal V(t)=\mathcal B(t)^{-1}
\exp\left(\sum_{\nu=1}^dt_\nu u_\nu\right).
$$

括号内仍是第一阶 $\ell^2$ 向量。因此 §2 给其点态指数循环；
$\mathcal B(t)^{-1}$ 是有界交换单位，故

$$
\boxed{\mathcal V(t)\text{ 对每个 }t\in\mathbb C^d\text{ 循环}.}
\tag{9.1}
$$

R145 已证明它属于全部混合自然乘积域，并且
$X_\nu\mathcal V(t)=\partial_{t_\nu}\mathcal V(t)$。若每个被微分的模式
$u_\nu$ 非零，R132 可逐因子传递循环性，得到

$$
\boxed{\partial^\alpha\mathcal V(t)\text{ 循环}
\quad\text{若 }u_\nu\ne0\text{ 对所有 }\alpha_\nu>0.}
\tag{9.2}
$$

允许非零常数模式。若某个被微分模式为零，对应导数为零，必须排除。
这不是从整函数的循环基向量取极限推导导数循环，而是对每一级已经核实定义域的闭第一阶乘子应用传递定理。

点态 $\partial^\alpha e^{\sum t_\nu u_\nu}$ 仍是多模式点态乘积乘指数，需另带 R145 的 Bell 修正；(9.2) 不能擅自去掉这些修正。

## 10. 准确范围

本稿完成任意第一阶指数权重下的一变量平移互素判据、全部平移点态幂，以及全部实际混合整轨道导数。指数方向允许任意相位、任意慢的平方可和尾，也可与多项式方向完全重叠。

未证明一般 $f\in H$ 的循环性与 $e^vf$ 的循环性等价。点乘 $e^v$ 通常不是全 $H$ 上的有界算子，甚至不能保证任意 $f\in H$ 的乘积仍在 $H$。也没有清空 (1.3) 的平移碰撞候选，更未把一变量 Bézout 单位搬到任意多模式点态多项式。

依赖：R16 的收敛乘积循环性；R125/R128/R132 的闭第一阶和正则化；R124/R139 的真实有限余数除法；R144 的有限自由模消元机制；R145 的多模式 Bell 函数及整向量域。所有本次新增倾斜公式、单位与尾代数归属、深域配对及基向量传回均在正文写明。
