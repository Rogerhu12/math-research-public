# R142：任意复杂一阶模式点态多项式的有限例外判据

日期：2026-11-12 UTC。作者：Astra-ISP-0c017065。

**后续进展：R144 已取消简单根条件，并将候选例外缩至至多 $p-1$ 个；全部 $(u-ρ)^p$ 和 $u^2$ 已关闭。本稿保留其独立的有界根分裂证明，末节原先的候选集仅表示本条当时的界。**

状态：下述定理完整证明。R134 的真实 Bell 修正、R139 的尾余数除法和有界根分裂共同给出新的排核入口，不加可和相位缺陷条件。对一个固定标量多项式的全部常数平移，至多留下显式有限集合；没有把这些候选例外自动判为空。

## 1. 主定理与准确范围

固定实际 $A$ 和范数代数 $\mathcal A=\overline{\mathbb C[I,A]}$。取非常数第一阶向量
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,
$$
并记
$$
j_0=\min\{j:a_j\ne0\},\qquad h=2^{j_0},\qquad
a=a_{j_0}\ne0,\qquad d=d_{j_0}=W_h.
\tag{1.1}
$$
本稿中单个 $a$ 表示这个首位系数；整个序列仍用 $(a_j)$。

**定理 1.1（根差判据）。** 设非恒定标量多项式 $q$ 的全部根 $\rho_1,\ldots,\rho_p$ 都简单，而且
$$
\boxed{q(\rho_i-2a)\ne0\quad(1\le i\le p).}
\tag{1.2}
$$
则点态向量 $q(u)$ 属于 $L^2$、非零，并对实际 $A$ 循环。

式 (1.2) 等价于没有两个根之差等于 $2a$；因为所有根均被逐一测试，也等价于不存在根对之差为 $\pm2a$。这里的 $a$ 由实际物理位次序确定，不能任意换为某个高位系数。

**定理 1.2（固定多项式的有限例外）。** 对任意次数 $p\ge1$ 的非恒定多项式 $q$，定义
$$
\begin{aligned}
\mathcal E_q(a)
={}&\{q(c):q'(c)=0\}\\
&\ \cup\{q(c):q(c)=q(c-2a)\}.
\end{aligned}
\tag{1.3}
$$
则
$$
\boxed{|\mathcal E_q(a)|\le2p-2,\qquad
\lambda\notin\mathcal E_q(a)
\Longrightarrow q(u)-\lambda\text{ 对 }A\text{ 循环}.}
\tag{1.4}
$$
重复值只计一次。对于 $p=1$，集合为空。对于 $q(w)=w^2$，
$$
\mathcal E_q(a)=\{0,a^2\},
\qquad
u^2-\lambda\text{ 循环}\quad(\lambda\notin\{0,a^2\}).
\tag{1.5}
$$

这个结论适用于 R138 的全平面连续谱第一阶模式，例如具有不可和正负质量的交替实系数；不依赖 $X_u$ 有任何有界预解式。R134 的空谱类则已另外完成全部非零点态多项式，不能把本稿留下的例外反说成该类的未知。

若 $u$ 为常数，直接判断 $q(u)$ 是否为零常数即可。若 $(a_j)$ 有限支撑，$q(u)$ 是有限柱，R11 已处理每个非零情形；本稿的有限例外是一个统一充分判据留下的集合，并不表示实际存在不循环向量。

## 2. 一阶闭乘子及一个更一般的有界扰动接口

令 $X=X_u$ 为 R125 的闭第一阶乘子。以下事实均包括定义域：

- $X^*=CXC$，有限物理柱 $\mathcal P$ 是 $X$ 及 $X^*$ 的图核心；
- 所有 $T\in\{A\}'$ 保持 $\operatorname{Dom}X$，且 $XT=TX$ 于该域；
- 每个 dyadic $\zeta$ 双向保持该域，且
  $\gamma_\zeta(X)-X=D_\zeta(A)$ 为有限的真正解析和；
- $X1=u$。

因为 $a_j=0$ 对 $j<j_0$，每个 $D_\zeta$ 只有 $h$ 倍数幂。其首个可能系数为
$$
c_h(D_\zeta)
=-\frac{2a}{d}(\zeta^h-1).
\tag{2.1}
$$
这是 $V_{j_0}=I-2A^h/d+O(A^{2h})$ 的直接展开。只取有限 gauge 差，未对可能发散的 $\sum a_j$ 作常数项求和。

记
$$
\mathcal A_h=\overline{\mathbb C[I,A^h]}.
$$
对其中的有界元素，$c_h$ 是 R32 的连续真实形式系数泛函，$\chi=c_0$ 是唯一字符。

**引理 2.1（尾中的有界扰动）。** 若 $D\in\mathcal A_h$ 且
$$
\boxed{-2a/d-c_h(D)\ne0,}
\tag{2.2}
$$
则 $T=X-D$ 及每个 $T-\lambda I$ 都单射且值域稠密。

**证明。** 有界 $C$ 对称扰动保留闭性、$C$ 自伴性、$\mathcal P$ 图核心、全交换子的域交换以及 gauge 的完整同域性质。

R139 的余数证明也适用于 $h=1$：若 $\zeta$ 的阶 $N>h$，对 $D$ 作 R124 的有限余数分解。只有 $s=\ell h$ 的分量出现；零余数在差中消失，所以
$$
\gamma_\zeta(D)-D
=\sum_{\ell=1}^{N/h-1}(\zeta^{\ell h}-1)A^{\ell h}B_{\ell h}
=A^h C_\zeta,\qquad C_\zeta\in\mathcal A_h.
\tag{2.3}
$$
若 $N\le h$，差为零。这里 $B_{\ell h}\in\mathcal A_N$ 来自实际有界余数除法，不能仅凭形式阶写出 (2.3)。

结合 (2.1)，对所有 $\zeta^h\ne1$，
$$
\gamma_\zeta(T)-T=A^h W_\zeta,\qquad
\chi(W_\zeta)=(\zeta^h-1)(-2a/d-c_h(D))\ne0.
\tag{2.4}
$$
所以 $W_\zeta$ 是 $\mathcal A$ 单位。对
$M=\ker(T-\lambda I)$，闭算子域交换给 $M$ 为闭 $A$ 不变空间。
R23 的 $A^hM$ 稠密，加上单位及其逆保持 $M$，给
$$
\overline{A^hW_\zeta M}=M.
$$

同域 $C$ 自伴跨核配对给
$B(A^hW_\zeta M,U_\zeta M)=0$；$U_\zeta$ 为物理 gauge 酉。
因此
$$
B(M,U_\zeta M)=0
\quad(\zeta\notin\mu_h).
\tag{2.5}
$$
R122 的有限 Fourier 支撑论证现在逐字适用：两两反射乘积只有 $\mu_h$ 模式；
若 $M\ne0$，$A$ 的遍历全支撑迫 $M$ 在每个低头柱上至多一维，
从而 $\dim M\le h$。单射拟幂零 $A$ 不可能有非零有限维不变空间。
故 $M=0$。$C$ 自伴性把通常伴随的核也排除，给值域稠密。证毕。

这个引理允许 $D$ 没有解析加性 gauge 差；所需的是每个差的真实 $A^h$ 因式及其非零字符。

## 3. 真实 Bell 系数和首位形式系数

R134 对所有复杂 $\ell^2$ 系数证明了整个 $\mathcal A$ 值函数
$$
B(t)=\lim_{N\to\infty}\prod_{j<N}b_j(t),
\tag{3.1}
$$
其中局部因子为
$$
b_j(t)=e^{-ta_jV_j}\cdot
\bigl(\cosh(ta_j)I+V_j\sinh(ta_j)\bigr).
\tag{3.2}
$$

每个局部因子与 $I$ 的差在紧 $t$ 圆盘上为
$O(|a_j|^2)$，因此乘积按算子范数局部一致收敛，所有导数同样收敛。
定义
$$
B_k=B^{(k)}(0).
$$
有
$$
B_0=I,\qquad B_1=0,\qquad
B_k\in\mathcal A_h,\qquad\chi(B_k)=0\quad(k\ge1).
\tag{3.3}
$$
因为所有非平凡因子均属于 $\mathcal A_h$，且
$\chi(b_j(t))=e^{-ta_j}(\cosh(ta_j)+\sinh(ta_j))=1$。

R134 还以真实有限部分和伴随图核心证明
$$
1\in\operatorname{Dom}X^p\quad(p\ge0),
$$
以及
$$
u^p=\sum_{k=0}^p\binom pk B_kX^{p-k}1.
\tag{3.4}
$$
这里只使用这些已经证明的幂域和向量恒等式，不假定一般自然幂 $X^p$ 自动闭或自动 $C$ 自伴。
复 Rademacher 矩估计保证每个 $u^p\in L^2$。

首位形式系数可以明确计算。除 $j_0$ 因子外，所有非平凡局部因子的幂都从 $2h$ 或更高开始。把
$$
V_{j_0}=1-2z^h/d+O(z^{2h})
$$
代入 (3.2)，得到
$$
c_h(B(t))=\frac{e^{-2at}-1+2at}{d}.
\tag{3.5}
$$
因 $c_h$ 在 $\mathcal A$ 上连续，有限乘积的这个恒等式通过范数极限保持；
局部一致范数收敛又允许取导数。因此
$$
\boxed{c_h(B_k)=\frac{(-2a)^k}{d}\quad(k\ge2).}
\tag{3.6}
$$

## 4. 任意简单根多项式的真实有界分裂

先将 $q$ 除以首项系数，故以下设其为首一多项式。令
$$
P(w)=\sum_{k=0}^p\frac{B_k}{k!}q^{(k)}(w)
=q(w)+\sum_{k=2}^p\frac{B_k}{k!}q^{(k)}(w)
\in\mathcal A_h[w].
\tag{4.1}
$$
它首一，且 $\chi(P(w))=q(w)$。

假定 $q$ 的根 $\rho_1,\ldots,\rho_p$ 简单。用有限标量参数
$\beta=(\beta_2,\ldots,\beta_p)$ 定义
$$
P_\beta(w)=q(w)+\sum_{k=2}^p\frac{\beta_k}{k!}q^{(k)}(w).
$$
围住各 $\rho_i$ 取互不相交的小圆。参数足够小时，圆周上扰动严格小于 $|q|$，
每个圆内恰有一个根。相应根是收敛解析芽
$$
y_i(\beta)=\frac1{2\pi i}\oint
w\,\frac{\partial_wP_\beta(w)}{P_\beta(w)}\,dw,
\qquad y_i(0)=\rho_i.
\tag{4.2}
$$
这由分母在圆周不消失、参数幂级数一致收敛和留数计数直接得到。
于是标量解析芽恒等式为
$$
P_\beta(w)=\prod_{i=1}^p(w-y_i(\beta)).
\tag{4.3}
$$

将这些芽求值于 $(B_2,\ldots,B_p)$ 不需要它们的算子范数小。
每个 $B_k$ 的字符为零，因此在 $\mathcal A_h$ 中拟幂零。
对给定足够小的 $\varepsilon_k>0$，存在有限 $C_k$ 使
$$
\|B_k^n\|\le C_k\varepsilon_k^n\quad(n\ge0).
$$
若芽 Taylor 系数满足多圆盘 Cauchy 界
$|c_\alpha|\le C\prod r_k^{-\alpha_k}$，取 $\varepsilon_k<r_k$ 即得
$$
\sum_\alpha |c_\alpha|\,
\|B_2^{\alpha_2}\cdots B_p^{\alpha_p}\|
\le C\Bigl(\prod C_k\Bigr)
\prod_{k=2}^p(1-\varepsilon_k/r_k)^{-1}<\infty.
\tag{4.4}
$$
所有参数算子交换，所以绝对收敛级数保留和积恒等式。
置
$$
Y_i=y_i(B_2,\ldots,B_p)\in\mathcal A_h.
$$
则
$$
\boxed{\chi(Y_i)=\rho_i,\qquad
P(w)=\prod_{i=1}^p(w-Y_i).}
\tag{4.5}
$$
对于 $p=1$，没有参数，直接取 $Y_1=\rho_1I$。

## 5. 根的首位系数和严格的非抵消条件

由 (3.6)，$P$ 的首位形式系数为
$$
c_h(P(w))
=\frac{q(w-2a)-q(w)+2a q'(w)}d.
\tag{5.1}
$$
这里使用有限 Taylor 恒等式；$k=0,1$ 项已经明确扣除。

由于 $Y_i\in\mathcal A_h$ 且字符为 $\rho_i$，取恒等式 $P(Y_i)=0$
的 $h$ 次形式系数。两个正阶元素的乘积从 $2h$ 开始，因此只保留线性变分：
$$
q'(\rho_i)c_h(Y_i)+
\frac{q(\rho_i-2a)-q(\rho_i)+2a q'(\rho_i)}d=0.
$$
因 $q(\rho_i)=0$ 且根简单，
$$
\boxed{
c_h(Y_i)=
-\frac{q(\rho_i-2a)+2a q'(\rho_i)}
{d\,q'(\rho_i)}.
}
\tag{5.2}
$$
所以
$$
-2a/d-c_h(Y_i)
=\frac{q(\rho_i-2a)}{d\,q'(\rho_i)}.
\tag{5.3}
$$

在主定理假设 (1.2) 下，每个右侧均非零。引理 2.1 于是证明
$$
T_i:=X-Y_i
$$
单射、值域稠密，并且其每个减标量仍有相同性质。这个步骤是实际闭算子的排核；
不是仅把形式多项式的不同根看作 Hilbert 空间中的可逆因子。

## 6. 同一个有界正则化完成逐因子的循环性传递

R128 将 $(a_j)$ 分成实虚部的四个非负部分，给一个固定 $t>0$ 的
有界注入交换子 $R=R(t)$，满足
$$
R H\subseteq\operatorname{Dom}X,\qquad XR\in\{A\}'\subset B(H).
\tag{6.1}
$$
每个 $Y_i\in\mathcal A_h$ 与 $R$ 交换。因此
$$
T_iR=XR-Y_iR
$$
是有界交换子。$R$ 和 $T_i$ 都单射，故 $T_iR$ 单射；
有界交换子的 $C$ 对称性使其值域稠密。

若 $v\in\operatorname{Dom}T_i=\operatorname{Dom}X$ 对 $A$ 循环，则
$(T_iR)v$ 也循环：这是一个稠密值域有界交换子作用于循环向量。
另一方面，域交换给
$$
(T_iR)v=R(T_iv).
$$
令 $M=\operatorname{cyc}_A(T_iv)$。R88 使 $R$ 保持 $M$，
所以循环向量 $R(T_iv)$ 已在 $M$ 内，从而 $M=H$。即
$$
\boxed{v\text{ 循环且 }v\in\operatorname{Dom}X
\Longrightarrow T_iv\text{ 循环}.}
\tag{6.2}
$$
这一步不要求 $T_i$ 在每个未知不变空间上像稠密。

还须核实迭代中的幂域。任何有界 $Y_i\in\{A\}'$ 都保持
$\operatorname{Dom}X$ 且与 $X$ 域交换；归纳即保持每个
$\operatorname{Dom}X^m$ 并与相应自然幂交换。若
$v\in\operatorname{Dom}X^m$，则
$$
(X-Y_i)v\in\operatorname{Dom}X^{m-1}.
$$
R134 已给 $1\in\operatorname{Dom}X^p$。从循环向量 $1$ 开始，逐个作用
$T_p,\ldots,T_1$，每一步都在所需真实定义域内，且由 (6.2) 保持循环性。

最后，(4.5) 在 $\operatorname{Dom}X^p$ 上是通常的交换算子多项式恒等式，
而 (3.4) 给
$$
\boxed{
T_1\cdots T_p1
=P(X)1
=\sum_{k=0}^p\frac{B_k}{k!}q^{(k)}(X)1
=q(u).
}
\tag{6.3}
$$
所以 $q(u)$ 循环。这完成定理 1.1。非首一情形把非零首项标量乘回即可。

整个证明未假定 $P(X)$ 的自然定义域闭，也未为一般高阶符号声称已有
$C$ 自伴闭实现；(6.3) 及逐步传递只需已经核实的常向量幂域。

## 7. 显式有限例外集的证明和例子

给定次数 $p$ 的非恒定 $q$ 和 $\lambda\in\mathbb C$。
若 $\lambda$ 不属于 (1.3) 的第一部分，$q(w)-\lambda$ 的所有根都简单。
若其两个根 $\rho,\rho-2a$ 同时存在，则
$$
q(\rho)=q(\rho-2a)=\lambda,
$$
正好使 $\lambda$ 落入第二部分。因而 $\lambda\notin\mathcal E_q(a)$
时，定理 1.1 用于 $q-\lambda$，给 (1.4) 的循环性。

$q'$ 的次数为 $p-1$。由于 $a\ne0$，
$$
q(c)-q(c-2a)
$$
也是次数恰为 $p-1$ 的非零多项式，其首项系数为原首项系数乘 $2pa$。
两者各至多 $p-1$ 个不同零点，因此 $|\mathcal E_q(a)|\le2p-2$。
$p=1$ 时两者均为非零常数，例外集为空。

对于 $q(w)=w^2$，临界点为 $c=0$；差式
$c^2-(c-2a)^2=4a(c-a)$ 的唯一零点为 $c=a$。
这给 (1.5)。

例如
$$
u=\sum_{j\ge0}\frac{(-1)^j}{j+1}\chi_j
$$
属于 R138 的全平面连续谱第一阶类，且首位 $a=1$。
因此
$$
u^2-\lambda\text{ 循环}\quad(\lambda\notin\{0,1\}),
$$
以及一般 $q(u)-\lambda$ 在上述至多 $2\deg q-2$ 个候选值之外循环。
这个例子的一阶算子没有任何预解点，故本证明确实不是套用空谱逆算子方法。

## 8. 剩余问题

一般复杂一阶模式在候选例外值处的非零点态多项式仍需另证；
特别上例的 $u^2$ 与 $u^2-1$ 未由本稿处理。有限支撑由 R11、
有限相位缺陷空谱类由 R134 另行完成。

多个独立模式的任意混合多项式仍未被化为这里的一个标量根问题。
一般二阶闭乘子的核、任意不变限制中复杂第一阶的像稠密性、以及完整普通
Hilbert ISP 仍开放。

本稿依赖 R32 的真实连续系数、R124/R139 的实际余数因式、
R125 的闭第一阶和跨核机制、R128/R132 的注入正则化传递，
以及 R134 的 Bell 系数、幂域与向量公式；各新环节在本文均写明了实际作用域。
